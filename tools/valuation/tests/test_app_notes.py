"""Reader checks protect source text and citation destinations during presentation."""
from urllib.parse import unquote_plus

import pytest
import yaml

from valuation.app_notes import note_markdown, readable_tables, split_note
from valuation.app_sources import SourceIndex


def test_note_structure_preserves_code_and_tables():
    title, intro, sections = split_note(
        "# Evidence note\n\n_As of May._\n\n## 1. Economics\n"
        "| Year | Cash |\n|---|---|\n| 2025 | $10 |\n\n"
        "```md\n## Not a section\n```\n\n### Detail\nOriginal wording.\n"
        "## Sources\n[Annual, Item 8]\n", "Fallback")
    assert title == "Evidence note" and intro == "_As of May._"
    assert [s.heading for s in sections] == ["1. Economics", "Sources"]
    assert "| 2025 | $10 |" in sections[0].body
    assert "```md\n## Not a section\n```" in sections[0].body
    assert "### Detail\nOriginal wording." in sections[0].body
    assert split_note("No headings.\nKeep every line.", "Fallback") == (
        "Fallback", "No headings.\nKeep every line.", [])


def test_note_links_keep_original_destinations_code_and_dollar_amounts(tmp_path):
    directory = tmp_path / "companies/EXMP/sources/2026-Q2"
    directory.mkdir(parents=True)
    (directory / "annual.txt").write_text("Annual statement")
    index = SourceIndex(tmp_path, "EXMP", {"sources": [
        {"tag": "Annual", "file": "sources/2026-Q2/annual.txt"}]})
    text = ("Cash is $10, up from $9. [Annual, Item 8] [Unknown]\n"
            "[Annual](https://example.com/annual) `[$10] [Annual]`\n"
            "```md\n[Annual]\n```\n")
    rendered = note_markdown(text, index)
    assert "Cash is \\$10, up from \\$9." in rendered
    assert "[Annual, Item 8](?company=EXMP" in rendered
    assert "locator=Item 8" in unquote_plus(rendered)
    assert "[Unknown]" in rendered
    assert "[Annual](https://example.com/annual)" in rendered
    assert "`[$10] [Annual]`" in rendered
    assert "```md\n[Annual]\n```" in rendered


def test_note_reader_search_and_raw_text_without_writes(tmp_path):
    pytest.importorskip("streamlit")
    from streamlit.testing.v1 import AppTest

    directory = tmp_path / "companies/EXMP"
    (directory / "valuation").mkdir(parents=True)
    (directory / "sources/2026-Q2").mkdir(parents=True)
    content = "# An evidence note\n\nA dated introduction.\n\n## Economics\nCash was $20 million.\n"
    note = directory / "sources/2026-Q2/notes-economics.md"
    note.write_text(content)
    assumptions = directory / "valuation/assumptions.yaml"
    assumptions.write_text(yaml.safe_dump({"sources": [
        {"tag": "Economics workpaper", "file": "sources/2026-Q2/notes-economics.md"}]}))
    before = assumptions.read_bytes()
    at = AppTest.from_string(
        "from pathlib import Path\nfrom valuation.app_sources import source_view\n"
        f"source_view(Path({str(tmp_path)!r}), ['EXMP'])\n")
    at.query_params.update({"company": "EXMP", "source": "companies/EXMP/sources/2026-Q2/notes-economics.md"})
    at.run()
    assert not at.exception
    assert at.title[0].value == "An evidence note"
    assert any("Agent-written analysis" in m.value for m in at.markdown)
    assert any('href="#note-section-0"' in m.value for m in at.markdown)
    assert at.code[0].value == content.strip()  # Streamlit trims the code widget's outer whitespace.
    at.sidebar.text_input[0].set_value("$20 million").run()
    assert not at.exception
    assert any("<mark" in m.value and "$20 million" in m.value for m in at.markdown)
    at.sidebar.text_input[0].set_value("not in this note").run()
    assert not at.exception
    assert any("not found" in c.value for c in at.caption)
    assert note.read_text() == content and assumptions.read_bytes() == before


def test_wide_tables_repeat_labels_and_preserve_every_value_and_alignment():
    table = "| Year | A | B | C | D | E |\n|---|---:|---:|---:|---:|---:|\n| 2025 | $10 | 20% | 30 | 40 | 50 |"
    rendered = readable_tables(table)
    assert "| Year | A | B | C | D |" in rendered
    assert "| Year | E |" in rendered
    assert rendered.count("2025") == 2
    for cell in ("$10", "20%", "30", "40", "50"):
        assert rendered.count(cell) == 1
    assert "|---|---:|" in rendered
    assert readable_tables("```md\n" + table + "\n```") == "```md\n" + table + "\n```"


def test_local_note_links_resolve_only_recorded_evidence(tmp_path):
    directory = tmp_path / "companies/EXMP/sources/2026-Q2"
    directory.mkdir(parents=True)
    for name in ("notes-one.md", "annual.txt"):
        (directory / name).write_text("Evidence")
    index = SourceIndex(tmp_path, "EXMP", {"sources": [
        {"tag": "Note", "file": "sources/2026-Q2/notes-one.md"},
        {"tag": "Annual", "file": "sources/2026-Q2/annual.txt"}]})
    rendered = note_markdown("[Annual](annual.txt) [Missing](unknown.md)", index, index.sources[0])
    assert "[Annual](?company=EXMP&source=" in rendered
    assert "Missing (not in this company's recorded sources)" in rendered
    assert "](unknown.md)" not in rendered
