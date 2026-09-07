"""The ruamel round-trip writer: comments survive, changelog appends, stale files are refused."""

from __future__ import annotations

import os
import shutil
from pathlib import Path

import pytest
import yaml

import valuation
from valuation import yamlio

FIXTURE = Path(__file__).resolve().parent / "fixtures" / "example_assumptions.yaml"
MRVL = Path(__file__).resolve().parents[3] / "companies" / "MRVL" / "valuation" / "assumptions.yaml"

COMMENTED = """\
# Top comment: this file is hand-written and its comments matter.
schema: 1
ticker: CMNT
company: Comment Co.
as_of_quarter: FY2027-Q2
horizon: 5                       # explicit years
base_year:
  period: "TTM"
  revenue: {value: 100, source: "[10-Q]"}   # trailing revenue
market:
  price: auto                    # fetched at compute time
  risk_free_rate: auto
scenarios:
  base:
    weight: 0.50
    story: |
      Line one of the story.
      Line two of the story.
    # a table in a comment
    #   Year  S/C
    #   FY26  2.2
    sales_to_capital: {value: 1.5, value_late: 1.2, reason: "history"}
    operating_margin:
      values: [0.18, 0.20, 0.22, 0.24, 0.26]
      reason: "two points a year"
    terminal:
      growth: {value: riskfree, allow_above_riskfree: false, reason: "default"}
      roic_premium: {value: null, allow_large_premium: false, reason: "none"}
"""


@pytest.fixture
def commented(tmp_path: Path) -> Path:
    p = tmp_path / "assumptions.yaml"
    p.write_text(COMMENTED, encoding="utf-8")
    return p


def comment_lines(text: str) -> list[str]:
    return [line for line in text.splitlines() if line.lstrip().startswith("#")]


def test_round_trip_preserves_comments_and_plain_dict(commented: Path):
    doc = yamlio.load_roundtrip(commented)
    changed = yamlio.apply_changes(doc, [("scenarios.base.operating_margin.values.4", 0.30),
                                        ("scenarios.base.sales_to_capital.value", 2.0)])
    assert [(c[0], c[1], c[2]) for c in changed] == [
        ("scenarios.base.operating_margin.values.4", 0.26, 0.30),
        ("scenarios.base.sales_to_capital.value", 1.5, 2.0),
    ]
    yamlio.save(doc)
    text = commented.read_text(encoding="utf-8")
    for line in comment_lines(COMMENTED):
        assert line in text, line
    assert "# trailing revenue" in text and "#   FY26  2.2" in text
    expected = yaml.safe_load(COMMENTED)
    expected["scenarios"]["base"]["operating_margin"]["values"][4] = 0.30
    expected["scenarios"]["base"]["sales_to_capital"]["value"] = 2.0
    assert yaml.safe_load(text) == expected
    # the engine's read path sees exactly the same dict
    loaded = valuation.load(commented)
    loaded.pop("_path")
    assert loaded == expected
    # block scalar, flow style and the sentinels survive
    assert "story: |" in text
    assert "values: [0.18, 0.2, 0.22, 0.24, 0.3]" in text or "values: [0.18, 0.20, 0.22, 0.24, 0.3]" in text
    assert "value: riskfree" in text and "price: auto" in text
    assert "value: null" in text


def test_riskfree_string_and_null_survive_when_set(commented: Path):
    doc = yamlio.load_roundtrip(commented)
    yamlio.apply_changes(doc, [("scenarios.base.terminal.roic_premium.value", 0.03),
                               ("scenarios.base.terminal.growth.value", 0.04)])
    yamlio.apply_changes(doc, [("scenarios.base.terminal.growth.value", "riskfree"),
                               ("scenarios.base.sales_to_capital.value_late", None)])
    yamlio.save(doc)
    plain = yaml.safe_load(commented.read_text(encoding="utf-8"))
    assert plain["scenarios"]["base"]["terminal"]["growth"]["value"] == "riskfree"
    assert plain["scenarios"]["base"]["terminal"]["roic_premium"]["value"] == 0.03
    assert plain["scenarios"]["base"]["sales_to_capital"]["value_late"] is None
    assert "value_late: null" in commented.read_text(encoding="utf-8")


def test_unchanged_values_are_not_reported(commented: Path):
    doc = yamlio.load_roundtrip(commented)
    assert yamlio.apply_changes(doc, [("scenarios.base.weight", 0.5), ("base_year.revenue.value", 100.0)]) == []


def test_list_index_paths_and_errors(commented: Path):
    doc = yamlio.load_roundtrip(commented)
    yamlio.apply_changes(doc, [("scenarios.base.operating_margin.values.0", 0.19)])
    assert doc.plain()["scenarios"]["base"]["operating_margin"]["values"][0] == 0.19
    with pytest.raises(yamlio.PathError):
        yamlio.apply_changes(doc, [("scenarios.base.operating_margin.values.9", 0.1)])
    with pytest.raises(yamlio.PathError):
        yamlio.apply_changes(doc, [("scenarios.base.weight.deeper", 1)])
    # a new key in an existing mapping is created; a new mapping chain too
    yamlio.apply_changes(doc, [("scenarios.base.cost_of_capital_override", 0.09), ("diagnostics.final_year_market_size.value", 5)])
    plain = doc.plain()
    assert plain["scenarios"]["base"]["cost_of_capital_override"] == 0.09
    assert plain["diagnostics"]["final_year_market_size"]["value"] == 5


def test_story_edit_stays_a_block_scalar(commented: Path):
    doc = yamlio.load_roundtrip(commented)
    yamlio.apply_changes(doc, [("scenarios.base.story", "A new first line.\nA new second line.")])
    yamlio.save(doc)
    text = commented.read_text(encoding="utf-8")
    assert "story: |" in text and "      A new second line." in text
    assert yaml.safe_load(text)["scenarios"]["base"]["story"] == "A new first line.\nA new second line.\n"


def test_changelog_and_owner_edited(commented: Path):
    doc = yamlio.load_roundtrip(commented)
    assert "changelog" not in doc.data
    n = yamlio.append_changelog(doc, [
        {"at": "2026-09-08T10:12:00", "path": "scenarios.base.operating_margin.values.4", "old": 0.26, "new": 0.30,
         "note": "owner: depreciation offsets look achievable"},
        {"at": "2026-09-08T10:12:00", "path": "scenarios.base.terminal.growth.value", "old": "riskfree", "new": 0.03,
         "note": None},
    ])
    assert n == 2
    stamp = yamlio.set_owner_edited(doc, "2026-09-08T10:12:00")
    assert stamp == "2026-09-08T10:12:00"
    yamlio.save(doc)
    text = commented.read_text(encoding="utf-8")
    plain = yaml.safe_load(text)
    assert plain["owner_edited"] == "2026-09-08T10:12:00"            # a string, not a datetime
    assert plain["changelog"] == [
        {"at": "2026-09-08T10:12:00", "path": "scenarios.base.operating_margin.values.4", "old": 0.26, "new": 0.30,
         "note": "owner: depreciation offsets look achievable"},
        {"at": "2026-09-08T10:12:00", "path": "scenarios.base.terminal.growth.value", "old": "riskfree", "new": 0.03,
         "note": None},
    ]
    assert list(plain.keys())[-2:] == ["owner_edited", "changelog"]
    assert text.count("- {at:") == 2                                  # one flow-style line per entry
    # a second save appends (oldest first) and keeps the stamp position
    doc2 = yamlio.load_roundtrip(commented)
    yamlio.append_changelog(doc2, [{"at": "2026-09-09T09:00:00", "path": "scenarios.base.weight", "old": 0.5, "new": 0.6, "note": "x"}])
    yamlio.set_owner_edited(doc2, "2026-09-09T09:00:00")
    yamlio.save(doc2)
    plain = yaml.safe_load(commented.read_text(encoding="utf-8"))
    assert len(plain["changelog"]) == 3 and plain["changelog"][-1]["path"] == "scenarios.base.weight"
    assert plain["owner_edited"] == "2026-09-09T09:00:00"
    # the engine knows these two blocks and does not flag them
    assert not [w for w in valuation.validate(plain).warnings if "unknown top-level key" in w]


def test_stale_file_guard(commented: Path):
    doc = yamlio.load_roundtrip(commented)
    # someone else writes the file after we loaded it
    text = commented.read_text(encoding="utf-8").replace("weight: 0.50", "weight: 0.55")
    commented.write_text(text, encoding="utf-8")
    os.utime(commented, ns=(doc.snapshot.mtime_ns + 5_000_000_000, doc.snapshot.mtime_ns + 5_000_000_000))
    yamlio.apply_changes(doc, [("scenarios.base.sales_to_capital.value", 2.0)])
    with pytest.raises(yamlio.StaleFileError, match="changed on disk"):
        yamlio.save(doc)
    assert "weight: 0.55" in commented.read_text(encoding="utf-8")       # nothing was written
    # reload, redo, save works; a touched-but-identical file does not trip the guard
    doc = yamlio.load_roundtrip(commented)
    os.utime(commented, ns=(doc.snapshot.mtime_ns + 5_000_000_000, doc.snapshot.mtime_ns + 5_000_000_000))
    yamlio.apply_changes(doc, [("scenarios.base.sales_to_capital.value", 2.0)])
    yamlio.save(doc)
    assert yaml.safe_load(commented.read_text(encoding="utf-8"))["scenarios"]["base"]["sales_to_capital"]["value"] == 2.0
    # and the snapshot is refreshed so a second save works
    yamlio.apply_changes(doc, [("scenarios.base.sales_to_capital.value", 2.5)])
    yamlio.save(doc)
    assert not list(commented.parent.glob(".assumptions-*.tmp"))       # temp files cleaned up


def test_diff_against_file(commented: Path):
    current = yaml.safe_load(COMMENTED)
    current["_path"] = str(commented)
    assert yamlio.diff_against_file(commented, current) == []
    current["scenarios"]["base"]["operating_margin"]["values"][2] = 0.25
    current["scenarios"]["base"]["terminal"]["growth"]["value"] = 0.04
    current["scenarios"]["base"]["weight"] = 0.5                      # int/float noise is not a change
    current["horizon"] = 10
    current["scenarios"]["base"]["operating_margin"]["values"] += [0.26] * 5
    del current["market"]["risk_free_rate"]
    diff = yamlio.diff_against_file(commented, current)
    paths = {c.path: (c.file_value, c.current_value) for c in diff}
    assert paths["horizon"] == (5, 10)
    assert paths["scenarios.base.terminal.growth.value"] == ("riskfree", 0.04)
    assert paths["market.risk_free_rate"] == ("auto", yamlio.ABSENT)
    assert paths["scenarios.base.operating_margin.values"][0] == [0.18, 0.20, 0.22, 0.24, 0.26]
    assert len(paths["scenarios.base.operating_margin.values"][1]) == 10
    assert len(diff) == 4
    changes = dict(yamlio.changes_from_diff(diff))
    assert changes["market.risk_free_rate"] is None and changes["horizon"] == 10


def test_fixture_and_company_files_round_trip_unchanged(tmp_path: Path):
    """Loading and saving without edits keeps the plain dict; the MRVL file keeps every comment line."""
    for src in (FIXTURE, MRVL):
        if not src.exists():
            continue
        target = tmp_path / src.name
        shutil.copy(src, target)
        doc = yamlio.load_roundtrip(target)
        yamlio.save(doc)
        assert yaml.safe_load(target.read_text(encoding="utf-8")) == yaml.safe_load(src.read_text(encoding="utf-8"))
        for line in comment_lines(src.read_text(encoding="utf-8")):
            assert line in target.read_text(encoding="utf-8"), line
    if MRVL.exists():
        assert MRVL.read_text(encoding="utf-8") == (tmp_path / MRVL.name).read_text(encoding="utf-8")
