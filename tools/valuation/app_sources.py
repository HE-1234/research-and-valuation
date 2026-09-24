"""Resolve displayed citations from recorded evidence, never from guessed filing URLs."""
from __future__ import annotations

from dataclasses import dataclass
from html import escape as html_escape
from pathlib import Path
import re
from urllib.parse import quote, urlencode, urlsplit

import yaml


def safe_url(value: str) -> str | None:
    try:
        parts = urlsplit(value)
        if parts.scheme in {"http", "https"} and parts.hostname and not parts.username:
            return quote(value, safe=":/?#=&%+@,;~!$'*-._")
    except ValueError:
        pass
    return None


def source_path(root: Path, ticker: str, name: str) -> Path | None:
    """Allow only research evidence, including explicitly cited peer and method files."""
    root = root.resolve()
    candidate = (root / name if name.startswith(("companies/", "tools/", ".claude/"))
                 else root / "companies" / ticker / name).resolve()
    if not candidate.is_relative_to(root) or candidate.suffix not in {".txt", ".md", ".csv"}:
        return None
    relative = candidate.relative_to(root).parts
    allowed = (relative == ("AGENTS.md",)
               or len(relative) >= 4 and relative[0] == "companies" and relative[2] == "sources"
               or relative[:3] in {("tools", "valuation", "data"), ("tools", "valuation", "damodaran-notes")}
               or relative[:4] == (".claude", "skills", "draft-valuation", "references"))
    return candidate if allowed and candidate.is_file() else None


def original_url(path: Path) -> str | None:
    # A source's own provenance header is stronger than a surrounding manifest.
    with path.open(encoding="utf-8", errors="replace") as handle:
        header = handle.read(3000)
    match = re.search(r"(?im)^\s*(?:URL|Source URL|Original URL):\s*(https?://\S+)", header)
    if match:
        return safe_url(match[1].rstrip(".,"))
    urls = set()
    for manifest in path.parent.glob("MANIFEST*.md"):
        for line in manifest.read_text(encoding="utf-8").splitlines():
            # Only a provenance row explicitly naming this exact cache file qualifies.
            if not re.search(r"(?<![\w/.-])" + re.escape(path.name) + r"(?![\w.-])", line):
                continue
            found = re.findall(r"https?://[^\s|<>`]+", line)
            if len(found) == 1:
                url = safe_url(found[0].rstrip(").,"))
                if url:
                    urls.add(url)
    return next(iter(urls)) if len(urls) == 1 else None


def base_tag(tag: str) -> str:
    value = tag.strip().strip("[]").strip()
    return re.sub(r",\s*(?:\.\.\.|p\.N(?:-M)?|section N).*$", "", value, flags=re.I)


def location_hint(text: str) -> str:
    """Keep explicit locations from guidance notes, never turn a forecast number into a locator."""
    pattern = r"\b(?:speaker paragraphs?\s+\d+(?:\s*[/–−-]\s*\d+)*|Item\s+\d+[A-Z]?|Note\s+(?:[A-Z]|\d+)(?:\.\d+)?|section\s+\d+[a-z]?|(?:PDF\s+)?pp?\.\s*\d+(?:\s*[–-]\s*\d+)?)\b"
    return "; ".join(m[0] for m in re.finditer(pattern, text, re.I))


@dataclass(frozen=True)
class Source:
    tag: str
    file: str
    path: Path
    cached_url: str
    original_url: str | None
    note: str = ""


class SourceIndex:
    def __init__(self, root: Path, ticker: str, doc: dict):
        self.sources: list[Source] = []
        self.aliases: dict[str, Source] = {}
        ambiguous: set[str] = set()
        entries = [dict(e) for e in doc.get("sources", []) if isinstance(e, dict)]
        # Historical sources can precede the valuation's own evidence window.
        history = root / "companies" / ticker / "valuation" / "historical-roic.yaml"
        if history.is_file():
            try:
                content = yaml.safe_load(history.read_text(encoding="utf-8")) or {}
                for row in content.get("years", []):
                    for file in row.get("source_paths", []):
                        entries.append({"tag": Path(file).stem.replace("10-K-", "10-K "), "file": file})
            except (OSError, yaml.YAMLError, AttributeError, TypeError):
                pass  # Optional history must not prevent the rest of the app from opening.
        for entry in entries:
            name = str(entry.get("file") or "")
            path = source_path(root, ticker, name)
            if path is None:
                continue
            tag = base_tag(str(entry.get("tag") or path.stem))
            cached = "?" + urlencode({"company": ticker, "source": path.relative_to(root.resolve()).as_posix()})
            source = Source(tag, name, path, cached, original_url(path), str(entry.get("note") or ""))
            self.sources.append(source)
            aliases = {tag, name, path.name, path.relative_to(root.resolve()).as_posix()}
            if tag.startswith(ticker + " "):
                aliases.add(tag[len(ticker) + 1:])
            for alias in aliases:
                key = alias.casefold()
                if key in self.aliases and self.aliases[key].path != path:
                    ambiguous.add(key)
                else:
                    self.aliases[key] = source
        for key in ambiguous:
            self.aliases.pop(key, None)
        keys = sorted(self.aliases, key=len, reverse=True)
        self.pattern = re.compile(r"(?<![\w/.-])(?:" + "|".join(re.escape(k) for k in keys) + r")(?![\w/.-])", re.I) if keys else None

    def render(self, text: str, escape, *, quote: str = "", locator: str = "") -> str:
        """Link exact known tags/paths, retaining section locators and escaping all other prose."""
        if not self.pattern:
            return escape(text)
        pieces = re.split(r"(\[[^\[\]]+\])", text)
        return "".join(escape("[") + self._render_fragment(piece[1:-1], escape, citation=True, quote=quote, locator=locator) + escape("]")
                       if piece.startswith("[") and piece.endswith("]")
                       else self._render_fragment(piece, escape, quote=quote, locator=locator) for piece in pieces)

    def _render_fragment(self, text: str, escape, *, citation: bool = False, quote: str = "", locator: str = "") -> str:
        chunks, start = [], 0
        for match in self.pattern.finditer(text):
            if match.start() < start:
                continue
            # A bare own-company alias must never capture the tail of an unknown peer's tag.
            prefix = text[:match.start()].rstrip()
            if citation and prefix and not prefix.endswith(";"):
                continue
            if not citation and re.search(r"\b[A-Z][A-Z0-9.-]+\s+$", text[:match.start()]):
                continue
            source = self.aliases[match[0].casefold()]
            is_file = "/" in match[0] or match[0] == source.path.name
            end = match.end()
            tail = ""
            if citation and not is_file:
                end = text.find(";", end)
                end = len(text) if end < 0 else end
                while end < len(text) and re.match(r"\s*(?:Item\b|Note\b|section\b|speaker paragraph|(?:PDF\s+)?pp?\.)", text[end + 1:], re.I):
                    next_end = text.find(";", end + 1)
                    end = len(text) if next_end < 0 else next_end
                tail = text[match.end():end].strip(" ,\n")
            params = {}
            if not is_file:
                location = tail or location_hint(locator)
                if location:
                    # Some source indexes explicitly define p.N as the PDF page count.
                    if re.search(r"PDF pages?", source.note, re.I) and re.match(r"p\.", location, re.I):
                        location = "PDF " + location
                    params["locator"] = location[:2000]
                if quote:
                    params["quote"] = quote[:2000]
            target = source.cached_url + ("&" + urlencode(params) if params else "")
            chunks.extend((escape(text[start:match.start()]), f"[{escape(text[match.start():end])}]({target})"))
            start = end
        chunks.append(escape(text[start:]))
        return "".join(chunks)


def highlighted_excerpt(match) -> str:
    """All evidence text is escaped; only our own highlight markup reaches the browser."""
    chunks, cursor = (["… "] if match.start else []), match.start
    for start, end in sorted(match.highlights):
        start, end = max(cursor, start), min(match.end, end)
        if end <= start:
            continue
        chunks.extend((html_escape(match.excerpt[cursor - match.start:start - match.start]),
                       '<mark style="background:#fff0a6;color:#272735;padding:1px 2px;border-radius:3px">',
                       html_escape(match.excerpt[start - match.start:end - match.start]), "</mark>"))
        cursor = end
    chunks.append(html_escape(match.excerpt[cursor - match.start:]))
    return '<div style="white-space:pre-wrap;overflow-wrap:anywhere;line-height:1.7">' + "".join(chunks) + "</div>"


def source_view(root: Path, tickers: list[str]) -> bool:
    """A separate, read-only tab; access is restricted to the chosen company's source index."""
    import streamlit as st
    from valuation.source_passages import find_passages
    if "source" not in st.query_params:
        return False
    ticker = st.query_params.get("company", "")
    if ticker not in tickers:
        st.error("This source's company is unavailable.")
        return True
    doc = yaml.safe_load((root / "companies" / ticker / "valuation" / "assumptions.yaml").read_text())
    index = SourceIndex(root, ticker, doc)
    requested = st.query_params["source"]
    source = next((s for s in index.sources if s.path.relative_to(root.resolve()).as_posix() == requested), None)
    if source is None:
        st.error("This document is not available in the company's recorded sources.")
        return True
    content = source.path.read_text(encoding="utf-8", errors="replace")
    locator = st.query_params.get("locator", "")[:2000]
    quoted = st.query_params.get("quote", "")[:2000]
    if source.path.suffix == ".md":
        from valuation.app_notes import render_note
        render_note(source, index, content, ticker, locator, quoted)
        return True
    st.caption(ticker + " / Source document")
    st.header(source.tag)
    st.caption(source.file)
    if source.note:
        st.caption(source.note.replace("$", r"\$"))
    original, download, _ = st.columns([1, 1, 2])
    if source.original_url:
        original.link_button("Open original document", source.original_url)
    download.download_button("Download cached text", content, file_name=source.path.name, mime="text/plain")
    st.caption("Cached research copy. Your valuation edits remain in the original app tab.")
    with st.expander("Search this document", expanded=not bool(locator or quoted)):
        search = st.text_input("Find words in this document", placeholder="Type an exact phrase, then press Enter", max_chars=600)
    result = find_passages(content, locator="" if search else locator, quote=search or quoted)
    st.subheader("Search results" if search else "Referenced passages")
    st.caption(result.caption)
    for match in result.matches:
        with st.container(border=True):
            st.markdown("**" + match.label.replace("$", r"\$") + "**")
            st.markdown(highlighted_excerpt(match), unsafe_allow_html=True)
    if not result.matches and not (search or locator or quoted):
        st.info("This citation names the document without an exact passage. Use the search box to find a phrase or number.")
    with st.expander("Full cached document", expanded=not bool(result.matches)):
        st.code(content, language=None, wrap_lines=True, height=650)
    return True
