"""Passage previews identify retained markers without pretending to verify claims."""
from pathlib import Path

from valuation.source_passages import MAX_EXCERPT, MAX_MATCHES, find_passages


ROOT = Path(__file__).resolve().parents[3]


def test_exact_quote_normalizes_whitespace_and_keeps_absolute_ranges():
    content = "Header\nThe company expects\n  $255 million to $290 million\nnext quarter.\n"
    result = find_passages(content, quote="$255 million to $290 million")
    assert result.status == "exact_quote"
    assert len(result.matches) == 1
    passage = result.matches[0]
    assert content[passage.start:passage.end] == passage.excerpt
    start, end = passage.highlights[0]
    assert content[start:end] == "$255 million to $290 million"
    assert passage.start <= start < end <= passage.end
    assert find_passages(content, quote="$255 million to $291 million").status == "unavailable"
    assert find_passages(content, quote="$255 Million to $290 million").status == "unavailable"


def test_exact_match_stays_near_preview_top_even_at_document_end():
    content = ("Table of Contents\n" + "marker row\n" * 80
               + "Guidance: $255 million to $290 million")
    result = find_passages(content, quote="$255 million to $290 million")
    passage = result.matches[0]
    hit_start, hit_end = passage.highlights[0]
    assert hit_start - passage.start <= 100
    assert passage.excerpt.startswith("Guidance:")
    assert content[hit_start:hit_end] == "$255 million to $290 million"
    assert passage.excerpt == content[passage.start:passage.end]

    one_line = "x" * 180 + " quoted words"
    passage = find_passages(one_line, quote="quoted words").matches[0]
    assert passage.start == one_line.index("quoted words")
    assert passage.highlights == ((passage.start, passage.start + len("quoted words")),)


def test_item_toc_row_is_skipped_and_ambiguous_body_headings_are_candidates():
    content = ("Table of Contents\nItem 7. | Management discussion | 38\n"
               "Item 8. | Financial statements | 53\n"
               "Part II\nItem 7. | Management discussion\nFirst body.\n"
               "Item 8. | Financial statements\nSecond body.\n")
    result = find_passages(content, "10-K FY2025, Item 7")
    assert result.status == "locator"
    assert len(result.matches) == 1
    assert result.matches[0].start == content.index("Item 7. | Management discussion\nFirst body")
    duplicate = content + "Item 7. | Another body\nAdditional discussion.\n"
    result = find_passages(duplicate, "Item 7")
    assert len(result.matches) == 2
    assert result.matches[0].label != result.matches[1].label
    assert all("Table of Contents" not in m.excerpt for m in result.matches)


def test_real_aaoi_item_and_note_locators_are_body_locations():
    content = (ROOT / "companies/AAOI/sources/2026-Q2/10-K-FY2025.txt").read_text()
    for locator, heading in (("Item 7", "Item 7. | Management"),
                             ("Item 8", "Item 8. | Financial"),
                             ("Note B.10", "NOTE B—SUMMARY")):
        result = find_passages(content, locator)
        assert result.status == "locator"
        assert len(result.matches) == 1
        assert result.matches[0].excerpt.startswith(heading)
        assert result.matches[0].start > 100_000  # Beyond the early table of contents.
    assert "parent note only" in find_passages(content, "Note B.10").caption


def test_page_locator_needs_retained_pdf_breaks_and_uses_correct_page():
    content = (ROOT / "companies/GOOGL/sources/2026-Q2/transcript.txt").read_text()
    result = find_passages(content, "Q2 2026 call, PDF p.18")
    assert result.status == "locator"
    page = result.matches[0]
    page_starts = [0] + [i + 1 for i, char in enumerate(content) if char == "\f"]
    assert page.start == page_starts[17]
    assert page.excerpt == content[page.start:page.end]
    assert find_passages(content, "Q2 2026 call, p.18").status == "unavailable"
    range_result = find_passages(content, "PDF p.18–19")
    assert [m.start for m in range_result.matches] == page_starts[17:19]
    assert find_passages("Page 18 in prose without preserved page breaks", "p.18").status == "unavailable"


def test_markdown_section_and_speaker_turns_use_structural_markers():
    note = "## 3. Overview\nText\n### 3c. Already invested\nEvidence.\n### 3c-bis. Other\n"
    section = find_passages(note, "section 3c")
    assert section.status == "locator"
    assert len(section.matches) == 1
    assert section.matches[0].excerpt.startswith("### 3c. Already invested")
    assert find_passages("A prose reference to section 3c exists", "section 3c").status == "unavailable"

    transcript = ("URL: https://example.test\nTier: machine\n\n"
                  "Operator: Opening.\n\nLindsay Savarese: Introduction.\n\n"
                  "Chih-Hsiang Lin: Revenue will grow.\n\nStefan J. Murry: Capacity is rising.\n")
    turns = find_passages(transcript, "speaker paragraphs 3–4")
    assert turns.status == "locator"
    assert [m.excerpt.split(":", 1)[0] for m in turns.matches] == ["Chih-Hsiang Lin", "Stefan J. Murry"]
    assert find_passages("No speaker labels here", "speaker paragraph 3").status == "unavailable"


def test_exact_quote_outside_locator_is_flagged_and_missing_quote_falls_back():
    content = "Item 7. | Discussion\nNo guidance.\nItem 8. | Statements\nCash was $20 million.\n"
    mismatch = find_passages(content, "Item 7", "$20 million")
    assert mismatch.status == "exact_quote"
    assert "outside Item 7" in mismatch.caption
    assert content[slice(*mismatch.matches[0].highlights[0])] == "$20 million"
    missing = find_passages(content, "Item 7", "$21 million")
    assert missing.status == "locator"
    assert "do not verify" in missing.caption
    assert missing.matches[0].excerpt.startswith("Item 7")
    assert find_passages(content, "source.txt").status == "unavailable"


def test_multiple_items_and_notes_show_all_available_markers():
    content = ("Item 7. | Discussion\nText.\nItem 8. | Statements\n"
               "NOTE J—Accounts\nValues.\nNOTE K—Debt\nMore values.\n")
    result = find_passages(content, "Item 7 and Item 8, Notes J and K")
    assert result.status == "locator"
    assert len(result.matches) == 4
    assert [m.excerpt.split("\n", 1)[0] for m in result.matches] == [
        "Item 7. | Discussion", "Item 8. | Statements", "NOTE J—Accounts", "NOTE K—Debt"]
    missing = find_passages(content, "Item 8, Notes J and O")
    assert missing.status == "locator"
    assert "Note O could not be located" in missing.caption


def test_real_aaoi_speaker_paragraph_count_is_after_metadata():
    content = (ROOT / "companies/AAOI/sources/2026-09-11-update/transcript-2026-Q2-tickertrends.txt").read_text()
    result = find_passages(content, "speaker paragraphs 3–4")
    assert result.status == "locator"
    assert len(result.matches) == 2
    assert result.matches[0].excerpt.startswith("Chih-Hsiang Lin:")
    assert result.matches[1].excerpt.startswith("Stefan J. Murry:")


def test_bounded_output_on_many_hits_and_one_line_source():
    content = "prefix " + ("$255 million to $290 million\n" * 1000)
    result = find_passages(content, quote="$255 million to $290 million")
    assert result.status == "exact_quote"
    assert len(result.matches) == MAX_MATCHES
    assert all(len(m.excerpt) <= MAX_EXCERPT for m in result.matches)
    assert "More matches exist" in result.caption
    assert find_passages("x" * 5_000_001, quote="xxx").status == "unavailable"
