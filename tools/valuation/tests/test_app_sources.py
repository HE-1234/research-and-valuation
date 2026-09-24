from pathlib import Path

from types import SimpleNamespace
from urllib.parse import unquote_plus

from valuation.app_sources import SourceIndex, highlighted_excerpt, original_url, source_path


def evidence(root, ticker, name, text="Cached filing"):
    path = root / "companies" / ticker / "sources" / "2026-Q2" / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    return path


def test_exact_citations_sections_peers_and_cached_paths(tmp_path):
    filing = evidence(tmp_path, "AAOI", "10-K-FY2025.txt")
    peer = evidence(tmp_path, "PEER", "10-K-FY2025.txt")
    (filing.parent / "MANIFEST.md").write_text(
        "10-K-FY2025.txt | https://www.sec.gov/Archives/company/annual.htm | verified\n")
    doc = {"sources": [
        {"tag": "[AAOI 10-K FY2025, ...]", "file": "sources/2026-Q2/10-K-FY2025.txt"},
        {"tag": "PEER 10-K FY2025", "file": "../PEER/sources/2026-Q2/10-K-FY2025.txt"},
    ]}
    index = SourceIndex(tmp_path, "AAOI", doc)
    text = index.render("[10-K FY2025, Item 8] [PEER 10-K FY2025] [10-K FY2024]", str)
    assert "[10-K FY2025, Item 8](?company=AAOI" in text
    assert "&locator=Item+8" in text
    assert "[PEER 10-K FY2025](?company=AAOI&source=companies%2FPEER" in text
    assert "[10-K FY2024]" in text  # Never invent a nearby year's URL.
    assert index.render("[UNKNOWN 10-K FY2025]", str) == "[UNKNOWN 10-K FY2025]"
    assert index.render("UNKNOWN 10-K FY2025", str) == "UNKNOWN 10-K FY2025"
    assert index.render(doc["sources"][0]["file"], str).startswith("[sources/2026-Q2/10-K-FY2025.txt](?company=")
    assert source_path(tmp_path, "AAOI", doc["sources"][1]["file"]) == peer


def test_ambiguous_provenance_stays_cached_and_header_wins(tmp_path):
    path = evidence(tmp_path, "AAOI", "transcript.txt")
    (path.parent / "MANIFEST.md").write_text(
        "transcript.txt | https://example.com/a\ntranscript.txt | https://example.com/b\n")
    assert original_url(path) is None
    path.write_text("URL: https://example.com/call\nactual text")
    assert original_url(path) == "https://example.com/call"


def test_reject_outside_evidence_and_symlink_escape(tmp_path):
    root = tmp_path / "repo"
    root.mkdir()
    secret = tmp_path / "secret.txt"
    secret.write_text("private")
    cache = evidence(root, "AAOI", "bad.txt")
    cache.unlink()
    cache.symlink_to(secret)
    assert source_path(root, "AAOI", "sources/2026-Q2/bad.txt") is None
    assert source_path(root, "AAOI", "../../../secret.txt") is None
    (root / "private.txt").write_text("private")
    assert source_path(root, "AAOI", "../../private.txt") is None
    assert not SourceIndex(root, "AAOI", {"sources": [{"tag": "secret", "file": str(secret)}]}).sources


def test_placeholder_tags_keep_distinct_method_notes_and_escape_text(tmp_path):
    first = evidence(tmp_path, "AAOI", "first.md")
    second = evidence(tmp_path, "AAOI", "second.md")
    index = SourceIndex(tmp_path, "AAOI", {"sources": [
        {"tag": "[Damodaran notes, horizon and terminal, section N]", "file": str(first)},
        {"tag": "[Damodaran notes, story-to-numbers, section N]", "file": str(second)},
    ]})
    text = index.render("$10 [Damodaran notes, horizon and terminal, section 3c]", lambda s: s.replace("$", r"\$"))
    assert text.startswith(r"\$10")
    assert "first.md" in text and "second.md" not in text


def test_historical_citations_are_indexed_even_outside_valuation_window(tmp_path):
    evidence(tmp_path, "AAOI", "10-K-FY2023.txt")
    directory = tmp_path / "companies/AAOI/valuation"
    directory.mkdir()
    (directory / "historical-roic.yaml").write_text(
        "years:\n- source_paths: [sources/2026-Q2/10-K-FY2023.txt]\n")
    index = SourceIndex(tmp_path, "AAOI", {"sources": []})
    assert "[10-K FY2023, Item 8](?company=AAOI" in index.render("[10-K FY2023, Item 8]", str)


def test_link_keeps_multiple_citation_locators_and_guidance_quote(tmp_path):
    evidence(tmp_path, "AAOI", "release.txt")
    evidence(tmp_path, "AAOI", "annual.txt")
    index = SourceIndex(tmp_path, "AAOI", {"sources": [
        {"tag": "Release", "file": "sources/2026-Q2/release.txt"},
        {"tag": "Annual", "file": "sources/2026-Q2/annual.txt"},
    ]})
    linked = unquote_plus(index.render("[Release, p.3; Annual, Item 8]", str, quote="$255 million to $290 million"))
    assert "source=companies/AAOI/sources/2026-Q2/release.txt&locator=p.3&quote=$255 million to $290 million" in linked
    assert "source=companies/AAOI/sources/2026-Q2/annual.txt&locator=Item 8" in linked
    linked = unquote_plus(index.render("[Annual, Item 8; Note B]", str))
    assert "&locator=Item 8; Note B)" in linked
    assert "&locator=" not in index.render("[Release]", str, locator="Nearest part of year 1: midpoint 272.5")
    # A plain cached file link remains the full document, even when a surrounding row has a quote.
    assert "&quote=" not in index.render("sources/2026-Q2/release.txt", str, quote="some quote")


def test_highlight_markup_escapes_source_html_and_uses_original_offsets():
    text = '<script>unsafe</script> & revenue'
    match = SimpleNamespace(start=40, end=40 + len(text), excerpt=text, highlights=((40, 48),))
    rendered = highlighted_excerpt(match)
    assert "<script>" not in rendered
    assert "&lt;script&gt;</mark>" in rendered
    assert "&amp; revenue" in rendered


def test_pdf_page_count_requires_recorded_source_convention(tmp_path):
    evidence(tmp_path, "AAOI", "transcript.txt")
    evidence(tmp_path, "AAOI", "slides.txt")
    index = SourceIndex(tmp_path, "AAOI", {"sources": [
        {"tag": "Call", "file": "sources/2026-Q2/transcript.txt", "note": "p.N counts PDF pages, not printed numbering."},
        {"tag": "Slides", "file": "sources/2026-Q2/slides.txt"},
    ]})
    assert "&locator=PDF+p.3" in index.render("[Call, p.3]", str)
    assert "&locator=p.3" in index.render("[Slides, p.3]", str)
