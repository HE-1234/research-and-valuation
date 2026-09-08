"""``assumptions.md``: rendered from the YAML alone, and written by ``value --render-assumptions``."""

from __future__ import annotations

import shutil
from pathlib import Path

import pytest
import yaml

import valuation
from valuation.cli import main
from valuation.render_assumptions import render_assumptions

HERE = Path(__file__).resolve().parent
FIXTURE = HERE / "fixtures" / "example_assumptions.yaml"
REPO = HERE.parents[2]
COMPANY_FILES = sorted(REPO.glob("companies/*/valuation/assumptions.yaml"))


def load(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_fixture_renders_every_section():
    doc = load(FIXTURE)
    text = render_assumptions(doc)
    for heading in ("# EXMP valuation assumptions as of FY2027-Q2", "## 1. The stories", "## 2. Scenario inputs",
                    "### Bear: reasons", "### Management: reasons", "## 3. Base year", "### Switches", "## 4. Bridge",
                    "## 5. Market inputs", "## 6. Cost of capital inputs", "## 7. Inputs for the diagnostics",
                    "## 8. Management guidance on record"):
        assert heading in text, heading
    assert "## 9. Change log" not in text                       # no changelog in the fixture
    # stories verbatim, one decimal percentages, money with separators, the riskfree sentinel spelled out
    assert "The custom-chip business loses its biggest customer" in text
    assert "| Weight | 25.0% | 50.0% | 25.0% | not weighted |" in text
    assert "10.0% / 6.0% / 4.0% / 4.0% / 4.0%" in text
    assert "| Revenue, trailing twelve months | 8,000 |" in text
    assert "the run's risk-free rate" in text
    assert "400 / — / — / — / —" in text                          # reinvestment override with nulls
    assert "**Revenue growth** — Year one follows the order book" in text
    assert "[Q2 FY2027 call]" in text
    assert "we expect to reach $12 billion in revenue in fiscal 2028" in text
    assert "Traceback" not in text


def test_nulls_show_as_dashes_and_changelog_renders():
    doc = load(FIXTURE)
    doc["scenarios"]["base"]["sales_to_capital"]["value"] = None
    doc["diagnostics"]["final_year_market_size"]["value"] = None
    doc["owner_edited"] = "2026-09-08T10:12:00"
    doc["changelog"] = [
        {"at": "2026-09-08T10:12:00", "path": "scenarios.base.operating_margin.values.4", "old": 0.26, "new": 0.32,
         "note": "owner: depreciation offsets look achievable"},
        {"at": "2026-09-08T10:12:00", "path": "scenarios.base.sales_to_capital.value", "old": 1.5, "new": None, "note": None},
    ]
    text = render_assumptions(doc)
    assert "| Owner edited (last save from the app) | 2026-09-08T10:12:00 |" in text
    assert "## 9. Change log" in text
    assert "| 2026-09-08T10:12:00 | `scenarios.base.operating_margin.values.4` | 0.26 | 0.32 | owner: depreciation offsets look achievable |" in text
    assert "| `scenarios.base.sales_to_capital.value` | 1.5 | — | — |" in text
    assert "| Sales-to-capital, years 1-5 | 1.20 | — | 1.80 | 1.50 |" in text
    assert "| Market size in the final forecast year (USD millions) | — |" in text


@pytest.mark.parametrize("path", COMPANY_FILES, ids=[p.parent.parent.name for p in COMPANY_FILES])
def test_company_files_render(path: Path):
    doc = load(path)
    text = render_assumptions(doc)
    assert text.startswith(f"# {doc['ticker']} valuation assumptions as of {doc['as_of_quarter']}")
    for name in ("bear", "base", "bull"):
        story = (doc["scenarios"][name].get("story") or "").strip().splitlines()[0]
        assert story in text
    assert "## 8. Management guidance on record" in text
    assert len(text.splitlines()) > 100


def test_incomplete_document_does_not_crash():
    text = render_assumptions({"ticker": "X", "scenarios": {"base": {"weight": 0.5}}})
    assert "# X valuation assumptions" in text and "## 2. Scenario inputs" in text


def test_cli_render_assumptions_writes_only_the_markdown(tmp_path: Path, capsys, monkeypatch):
    root = tmp_path
    (root / "AGENTS.md").write_text("# stub\n", encoding="utf-8")
    vdir = root / "companies" / "EXMP" / "valuation"
    vdir.mkdir(parents=True)
    target = vdir / "assumptions.yaml"
    shutil.copy(FIXTURE, target)
    before = target.read_bytes()
    monkeypatch.chdir(root)
    # no network is needed and no --set is honoured; a ticker resolves through the repo root
    assert main(["exmp", "--render-assumptions", "--set", "market.price=1"]) == 0
    out = capsys.readouterr()
    assert "written" in out.out and "assumptions.md" in out.out
    assert "--set overrides are ignored" in out.err
    assert sorted(p.name for p in vdir.iterdir()) == ["assumptions.md", "assumptions.yaml"]
    assert target.read_bytes() == before
    md = (vdir / "assumptions.md").read_text(encoding="utf-8")
    assert md == render_assumptions(valuation.load(target))
    assert "| Price (USD per share) | auto |" in md               # the --set did not leak into the file


def test_normal_run_also_writes_assumptions_md(tmp_path: Path, capsys):
    root = tmp_path
    (root / "AGENTS.md").write_text("# stub\n", encoding="utf-8")
    vdir = root / "companies" / "EXMP" / "valuation"
    vdir.mkdir(parents=True)
    target = vdir / "assumptions.yaml"
    shutil.copy(FIXTURE, target)
    assert main([str(target), "--no-fetch", "--set", "market.price=70", "--set", "market.risk_free_rate=0.0425"]) == 0
    assert (vdir / "valuation.md").exists() and (vdir / "assumptions.md").exists()
    md = (vdir / "assumptions.md").read_text(encoding="utf-8")
    assert "| Price (USD per share) | auto |" in md               # mirrors the file, not the --set overrides
    assert "written" in capsys.readouterr().out


def test_detail_prints_after_the_reason_as_an_indented_paragraph():
    doc = load(FIXTURE)
    doc["scenarios"]["base"]["revenue_growth"]["detail"] = "History: 2022 9.8%, 2023 8.7%, 2024 13.9%.\nBacklog covers year one."
    doc["base_year"]["revenue"]["detail"] = "FY2025 402,836 plus six months."
    text = render_assumptions(doc)
    i = text.index("**Revenue growth** — Backlog plus one new program per year")
    j = text.index("    History: 2022 9.8%, 2023 8.7%, 2024 13.9%.\n    Backlog covers year one.")
    assert i < j < text.index("**Operating margin** — Two points a year")
    assert "- **Revenue**, working notes:\n\n    FY2025 402,836 plus six months." in text


def test_sources_table_is_the_final_section():
    doc = load(FIXTURE)
    text = render_assumptions(doc)
    i = text.index("## Sources")
    assert i > text.index("## 8. Management guidance on record")
    assert "| Tag | Cached file | Date | Note |" in text[i:]
    assert "| [10-Q Q2 FY2027, ...] | `sources/FY2027-Q2/10-Q-FY2027-Q2.txt` | 2026-08-28 | quarter ended 2026-08-01 |" in text[i:]
    assert "| [Q2 FY2027 call] | `sources/FY2027-Q2/transcript.txt` | 2026-08-27 | — |" in text[i:]
    doc["changelog"] = [{"at": "2026-09-08T10:12:00", "path": "horizon", "old": 5, "new": 10, "note": None}]
    text = render_assumptions(doc)
    assert text.index("## 9. Change log") < text.index("## Sources")
    del doc["sources"]
    assert "## Sources" not in render_assumptions(doc)


def test_ten_year_horizon_prints_the_by_rule_line_under_the_per_year_tables():
    """Section 18.4: five explicit years in the table, one line per case for the years the rule builds."""
    doc = load(FIXTURE)
    doc["horizon"] = 10
    text = render_assumptions(doc)
    assert "| Revenue growth, years 1-5 (years 6-10 by rule) |" in text
    assert "| Operating margin, years 1-5 (years 6-10 by rule) |" in text
    assert "| Sales-to-capital, years 6-10 |" in text                       # real model years now
    assert "10 forecast years, then a terminal value: years 1-5 are set below and years 6-10 are built by rule" in text
    # terminal growth is not known until a run fetches the rate, so it is named in words
    assert "- Base, years 6-10 by rule: growth moving from 20.0% to the risk-free rate; margin held at 26.0% " \
           "through year 10." in text
    assert "- Bull, years 6-10 by rule: growth easing from 15.0% to 4.0%; margin held at 34.0% through year 10." in text
    # audit 4, item 2: the verb follows the direction, so a bear path below terminal growth moves up
    doc["scenarios"]["bull"]["revenue_growth"]["values"][4] = 0.02
    assert "- Bull, years 6-10 by rule: growth moving up from 2.00% to 4.00%;" in render_assumptions(doc)
    # the premium row names the new ceilings
    assert "| A large premium is allowed (above base 8, bull 12 points) |" in text


def test_five_year_horizon_says_the_late_ratio_is_for_the_reference_only():
    doc = load(FIXTURE)                                                     # the fixture says horizon: 5
    text = render_assumptions(doc)
    assert "| Sales-to-capital, years 6-10 of the 10-year reference |" in text
    assert "| Revenue growth, years 1-5 |" in text
    assert "by rule" not in text
    assert "5 forecast years, then a terminal value" in text


def test_ten_entry_lists_show_ten_columns_and_no_by_rule_line():
    doc = load(FIXTURE)
    doc["horizon"] = 10
    for name in ("bear", "base", "bull", "management"):
        sc = doc["scenarios"][name]
        sc["revenue_growth"]["values"] = list(sc["revenue_growth"]["values"]) + [0.04] * 5
        sc["operating_margin"]["values"] = list(sc["operating_margin"]["values"]) + [sc["operating_margin"]["values"][4]] * 5
        sc["reinvestment_override"]["values"] = list(sc["reinvestment_override"]["values"]) + [None] * 5
    text = render_assumptions(doc)
    assert "| Revenue growth, years 1-10 |" in text
    assert "| Reinvestment override, years 1-10 (USD millions) |" in text
    assert "by rule" not in text


def test_story_to_numbers_table_prints_under_each_story():
    doc = load(FIXTURE)
    text = render_assumptions(doc)
    i = text.index("The company keeps its two big custom-chip customers")
    j = text.index("How the story becomes numbers:", i)
    assert j < text.index("## 2. Scenario inputs")
    assert "| What the story says | Which input it sets | The number |" in text[j:j + 200]
    assert "| Keeps its two big custom-chip customers and adds a third by year three. | revenue growth, years 1 to 5 | 20% a year |" in text
    # the management table carries a source on one row, so it gets a fourth column
    k = text.index("How the story becomes numbers:", text.index("### Management"))
    assert "| What the story says | Which input it sets | The number | Source |" in text[k:k + 200]
    assert "| 22% a year | [Q2 FY2027 call] |" in text[k:]
    assert "| 32% | — |" in text[k:]
    # a pipe or a line break inside a cell never breaks the table; a malformed row is skipped
    doc["scenarios"]["bear"]["story_to_numbers"].append({"says": "a | b\nc", "drives": "x", "number": 0.04})
    doc["scenarios"]["bear"]["story_to_numbers"].append("not a row")
    text = render_assumptions(doc)
    assert "| a \\| b c | x | 0.04 |" in text
    assert "not a row" not in text
    assert "Traceback" not in text


def test_story_without_a_table_prints_no_table():
    doc = load(FIXTURE)
    del doc["scenarios"]["bear"]["story_to_numbers"]
    text = render_assumptions(doc)
    i = text.index("The custom-chip business loses its biggest customer")
    assert "How the story becomes numbers:" not in text[i:text.index("### Base")]
