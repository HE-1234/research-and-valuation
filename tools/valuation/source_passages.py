"""Conservative, bounded passage previews for cached valuation evidence.

Offsets and highlight ranges refer to the *original* text.  A section heading
locates a part of a document, not proof of a particular assertion.  Only an
exact quote (with whitespace normalized) is reported as an exact text match.
"""
from __future__ import annotations

from dataclasses import dataclass
import re


MAX_MATCHES = 8
MAX_EXCERPT = 1100
MAX_QUOTE = 600
MAX_SCAN = 5_000_000


@dataclass(frozen=True)
class PassageMatch:
    label: str
    start: int
    end: int
    excerpt: str
    highlights: tuple[tuple[int, int], ...]


@dataclass(frozen=True)
class PassageResult:
    # exact_quote: literal wording found; locator: only a structural marker
    # found; unavailable: neither could be safely located.
    status: str
    caption: str
    matches: tuple[PassageMatch, ...] = ()


@dataclass(frozen=True)
class _Anchor:
    label: str
    start: int
    end: int
    highlight_end: int


_ITEM = re.compile(r"(?im)^[ \t]{0,8}Item[ \t]+(?P<number>\d{1,2}[A-Z]?)(?:\.)?(?![\w])(?P<tail>[^\n]{0,160})$")
_NOTE = re.compile(r"(?im)^[ \t]{0,8}Note[ \t]+(?P<number>[A-Z]|\d{1,2})[ \t]*[.\-—–:][ \t]*(?P<tail>[^\n]{0,160})$")
_SECTION = re.compile(r"(?m)^[ \t]{0,3}#{1,6}[ \t]+(?P<number>\d+[a-z]?(?:-[a-z]+)?)[.\s-]+[^\n]{1,150}$", re.I)
_SPEAKER = re.compile(r"(?m)^(?:Operator|[A-Z][A-Za-z'.-]+(?: [A-Z][A-Za-z'.-]+){0,5}):[ \t]+")


def _preview(content: str, label: str, span_start: int, span_end: int,
             hit_start: int, hit_end: int) -> PassageMatch:
    """Put the match near the top without changing source offsets."""
    start = max(span_start, hit_start - 100)
    if start > span_start:
        # A retained line/page break is a clearer excerpt boundary than a
        # partial table row. Otherwise advance to the next word boundary.
        break_at = max(content.rfind("\n", start, hit_start),
                       content.rfind("\f", start, hit_start))
        if break_at >= start:
            start = break_at + 1
        elif not content[start - 1].isspace() and not content[start].isspace():
            boundary = re.search(r"\s", content[start:hit_start])
            start = start + boundary.end() if boundary else hit_start
    end = min(span_end, start + MAX_EXCERPT)
    return PassageMatch(label, start, end, content[start:end], ((hit_start, hit_end),))


def _item_anchors(content: str, number: str) -> list[_Anchor]:
    headings = []
    for match in _ITEM.finditer(content):
        tail = match["tail"]
        # SEC text caches often preserve TOC columns as "| title | 38".
        # This is a clear page-index row; other duplicates remain candidates.
        if re.search(r"\|[ \t]*\d{1,3}[ \t]*$", tail):
            continue
        headings.append(match)
    found = []
    for index, heading in enumerate(headings):
        if heading["number"].casefold() != number.casefold():
            continue
        end = headings[index + 1].start() if index + 1 < len(headings) else len(content)
        found.append(_Anchor(f"Item {number}, candidate {len(found) + 1}", heading.start(), end, heading.end()))
    return found


def _note_anchors(content: str, number: str) -> list[_Anchor]:
    headings = list(_NOTE.finditer(content))
    found = []
    for index, heading in enumerate(headings):
        if heading["number"].casefold() != number.casefold():
            continue
        end = headings[index + 1].start() if index + 1 < len(headings) else len(content)
        found.append(_Anchor(f"Note {number}, candidate {len(found) + 1}", heading.start(), end, heading.end()))
    return found


def _section_anchors(content: str, number: str) -> list[_Anchor]:
    headings = list(_SECTION.finditer(content))
    found = []
    for index, heading in enumerate(headings):
        if heading["number"].casefold() != number.casefold():
            continue
        end = headings[index + 1].start() if index + 1 < len(headings) else len(content)
        found.append(_Anchor(f"Section {number}, candidate {len(found) + 1}", heading.start(), end, heading.end()))
    return found


def _page_anchors(content: str, number: int) -> list[_Anchor]:
    # pdftotext -layout and related extraction retain the PDF page separator.
    # An unmarked text file must not acquire invented page numbers.
    if "\f" not in content:
        return []
    starts = [0] + [match.end() for match in re.finditer("\f", content)]
    if number < 1 or number > len(starts):
        return []
    start = starts[number - 1]
    end = starts[number] - 1 if number < len(starts) else len(content)
    # Highlight the first visible characters because the page break itself is
    # not useful text for the reader.
    hit = re.search(r"\S.{0,75}", content[start:end])
    if hit is None:
        return []
    return [_Anchor(f"PDF page {number}", start, end, start + hit.end())]


def _speaker_anchors(content: str, locator: str) -> list[_Anchor]:
    # Count whole turns, each starting with a speaker label after the first
    # Operator turn. This matches the AAOI machine transcript's source notes.
    # If this structure is absent, paragraph numbers are unverifiable.
    opening = re.search(r"(?m)^Operator:[ \t]+", content)
    if opening is None:
        return []
    turns = list(_SPEAKER.finditer(content, opening.start()))
    wanted: list[int] = []
    for part in re.findall(r"\d+[ \t]*(?:[–-][ \t]*\d+)?", locator):
        nums = [int(x) for x in re.findall(r"\d+", part)]
        if len(nums) == 1:
            wanted.append(nums[0])
        elif len(nums) == 2 and 0 < nums[1] - nums[0] <= MAX_MATCHES:
            wanted.extend(range(nums[0], nums[1] + 1))
    if not wanted or len(set(wanted)) > MAX_MATCHES:
        return []
    anchors = []
    for number in dict.fromkeys(wanted):
        if number < 1 or number > len(turns):
            return []
        turn = turns[number - 1]
        end = turns[number].start() if number < len(turns) else len(content)
        anchors.append(_Anchor(f"Speaker paragraph {number}", turn.start(), end, turn.end()))
    return anchors


def _anchors(content: str, locator: str) -> tuple[list[_Anchor], str, str]:
    markers: list[tuple[int, str, str, str]] = []
    # A single citation can cite several Items and Notes. Gather every explicit
    # marker rather than quietly jumping to the first one.
    item_pattern = re.compile(
        r"\bItems?[ \t]+(?P<head>\d{1,2}[A-Z]?)(?P<tail>(?:[ \t]*(?:,|and|&)[ \t]*(?:Item[ \t]+)?\d{1,2}[A-Z]?){0,5})", re.I)
    for match in item_pattern.finditer(locator):
        numbers = [match["head"]] + re.findall(r"(?:,|and|&)[ \t]*(?:Item[ \t]+)?(\d{1,2}[A-Z]?)", match["tail"], re.I)
        markers.extend((match.start(), "item", number.upper(), "") for number in numbers)
    note_pattern = re.compile(
        r"\bNotes?[ \t]+(?P<head>[A-Z]|\d{1,2})(?:\.(?P<suffix>\d+))?(?P<tail>(?:[ \t]*(?:,|and|&)[ \t]*(?:Note[ \t]+)?(?:[A-Z]|\d{1,2})){0,5})", re.I)
    for match in note_pattern.finditer(locator):
        markers.append((match.start(), "note", match["head"].upper(), match["suffix"] or ""))
        for number in re.findall(r"(?:,|and|&)[ \t]*(?:Note[ \t]+)?([A-Z]|\d{1,2})\b", match["tail"], re.I):
            markers.append((match.start(), "note", number.upper(), ""))
    if markers:
        anchors: list[_Anchor] = []
        labels: list[str] = []
        found_labels: list[str] = []
        missing: list[str] = []
        for _, kind, number, suffix in sorted(markers, key=lambda marker: marker[0])[:MAX_MATCHES]:
            label = f"{'Item' if kind == 'item' else 'Note'} {number}"
            if suffix:
                label += f".{suffix} (parent note only; subpart is not marked)"
            if label in labels:
                continue
            labels.append(label)
            matches = _item_anchors(content, number) if kind == "item" else _note_anchors(content, number)
            anchors.extend(matches)
            if matches:
                found_labels.append(label)
            else:
                missing.append(label)
        if len(markers) > MAX_MATCHES:
            missing.append("further cited markers beyond the preview limit")
        return anchors, "; ".join(found_labels or labels), "; ".join(missing)
    if match := re.search(r"\bsection[ \t]+(\d+[a-z]?)\b", locator, re.I):
        number = match[1]
        return _section_anchors(content, number), f"section {number}", ""
    if match := re.search(r"\bspeaker paragraphs?[ \t]+([\d\s/–-]+)", locator, re.I):
        return _speaker_anchors(content, match[1]), "speaker paragraph(s)", ""
    if match := re.search(r"\bPDF[ \t]+(?:p\.|page[ \t]+)[ \t]*(\d+)(?:[ \t]*[-–][ \t]*(\d+))?\b", locator, re.I):
        first, last = int(match[1]), int(match[2] or match[1])
        description = f"PDF page{'s' if first != last else ''} {first}" + (f"–{last}" if first != last else "")
        if last < first or last - first >= MAX_MATCHES:
            return [], description, "page range is too large or reversed"
        pages = [_page_anchors(content, number) for number in range(first, last + 1)]
        if any(not page for page in pages):
            return [], description, "one or more PDF page breaks are unavailable"
        return [page[0] for page in pages], description, ""
    if match := re.search(r"\bp\.[ \t]*(\d+)(?:[ \t]*[-–][ \t]*(\d+))?\b", locator, re.I):
        return [], f"page {match[1]}", "bare p.N may refer to printed page numbering; PDF-page counting was not specified"
    return [], "exact location", ""


def _quote_matches(content: str, quote: str, anchors: list[_Anchor]
                   ) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
    words = quote.split()
    if not words or len(quote) > MAX_QUOTE:
        return [], []
    # Escaped literal tokens, separated only by whitespace.  In particular,
    # case, punctuation and digits are never silently changed.
    pattern = re.compile(r"\s+".join(re.escape(word) for word in words))
    all_hits: list[tuple[int, int]] = []
    located_hits: list[tuple[int, int]] = []
    for match in pattern.finditer(content):
        hit = (match.start(), match.end())
        if len(all_hits) <= MAX_MATCHES:
            all_hits.append(hit)
        if any(a.start <= hit[0] and hit[1] <= a.end for a in anchors):
            if len(located_hits) <= MAX_MATCHES:
                located_hits.append(hit)
            if len(located_hits) > MAX_MATCHES:
                break
        elif not anchors and len(all_hits) > MAX_MATCHES:
            break
    return all_hits, located_hits


def find_passages(content: str, locator: str = "", quote: str = "") -> PassageResult:
    """Return exact quote hits or conservative structural previews.

    `locator` may be a bare locator or a full citation tag. Each preview and
    result count is bounded. A source with no preserved locator marker remains
    available for reading in full, but this function reports no exact location.
    """
    if not content:
        return PassageResult("unavailable", "The cached source is empty.")
    if len(content) > MAX_SCAN:
        return PassageResult("unavailable", "This source is too large for a passage preview; open the full cached text.")
    anchors, description, missing = _anchors(content, locator)
    caveat = f" {missing} could not be located." if missing else ""
    if quote.strip():
        if len(quote) > MAX_QUOTE:
            return PassageResult("unavailable", "The quoted search text is too long for a bounded exact match.")
        hits, located = _quote_matches(content, quote, anchors)
        if hits:
            chosen = located or hits
            matches = tuple(_preview(content, f"Exact quote {i}", 0, len(content), start, end)
                            for i, (start, end) in enumerate(chosen[:MAX_MATCHES], 1))
            extra = " More matches exist; refine the quote." if len(chosen) > MAX_MATCHES else ""
            if locator.strip() and anchors and not located:
                caption = f"Exact wording found in this source, but outside {description}; the cited location is unverified.{caveat}{extra}"
            elif locator.strip() and not anchors:
                caption = f"Exact wording found in this source; {description} could not be located.{caveat}{extra}"
            else:
                caption = f"Exact wording found in this source{' within a cited marker (' + description + ')' if anchors else ''}.{caveat}{extra}"
            return PassageResult("exact_quote", caption, matches)
        if anchors:
            matches = tuple(_preview(content, a.label, a.start, a.end, a.start, a.highlight_end)
                            for a in anchors[:MAX_MATCHES])
            return PassageResult("locator", f"Exact wording was not found. Showing broader {description} marker(s) only; they do not verify the quoted claim.{caveat}", matches)
        return PassageResult("unavailable", f"Exact wording and a reliable location marker were not found in the cached source.{caveat}")
    if anchors:
        matches = tuple(_preview(content, a.label, a.start, a.end, a.start, a.highlight_end)
                        for a in anchors[:MAX_MATCHES])
        extra = " Additional candidates exist." if len(anchors) > MAX_MATCHES else ""
        return PassageResult("locator", f"Located {description} marker(s); these broader locations do not verify a particular claim.{caveat}{extra}", matches)
    return PassageResult("unavailable", f"No exact passage location is available for this citation; open the full cached source.{caveat}")
