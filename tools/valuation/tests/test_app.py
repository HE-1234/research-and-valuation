"""The Streamlit walk, driven headlessly with ``streamlit.testing.v1.AppTest``.

Skipped when streamlit is not installed (``uv run pytest``); runs under
``uv run --extra app pytest``.  The app is pointed at a temporary repository copy that
holds the fixture company, with market cells written as numbers so nothing is fetched.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

streamlit = pytest.importorskip("streamlit")
from streamlit.testing.v1 import AppTest  # noqa: E402

HERE = Path(__file__).resolve().parent
FIXTURE = HERE / "fixtures" / "example_assumptions.yaml"
APP = HERE.parent / "app.py"
PAGES = ["start", "stories", "revenue_growth", "operating_margin", "terminal", "cost_of_capital", "reinvestment",
         "taxes_weights", "facts", "results"]          # the fixture's impact order


@pytest.fixture
def repo(tmp_path: Path, monkeypatch) -> Path:
    root = tmp_path / "repo"
    root.mkdir()
    (root / "AGENTS.md").write_text("# stub\n", encoding="utf-8")
    vdir = root / "companies" / "EXMP" / "valuation"
    vdir.mkdir(parents=True)
    text = FIXTURE.read_text(encoding="utf-8")
    text = text.replace("price: auto", "price: 70").replace("risk_free_rate: auto", "risk_free_rate: 0.0425")
    text = text.replace("equity_risk_premium: auto", "equity_risk_premium: 0.045")
    (vdir / "assumptions.yaml").write_text(text, encoding="utf-8")
    monkeypatch.setenv("VALUATION_REPO_ROOT", str(root))
    monkeypatch.setenv("VALUATION_APP_NO_FETCH", "1")
    return root


def run_app() -> AppTest:
    at = AppTest.from_file(str(APP), default_timeout=120)
    at.run()
    return at


def assert_clean(at: AppTest) -> None:
    assert not at.exception, [e.value for e in at.exception]


def go_to(at: AppTest, page: str) -> None:
    """Click Next until the given page is current."""
    target = PAGES.index(page)
    while at.session_state["page"] < target:
        at.button(key="next_btn").click().run()
        assert_clean(at)
    assert at.session_state["page"] == target


def progress_text(at: AppTest) -> str:
    return at.get("progress")[0].proto.text if at.get("progress") else ""


def readout(at: AppTest) -> str:
    texts = [m.value for m in at.markdown if "With your current inputs" in m.value]
    assert texts, "no live readout on this page"
    return texts[-1]


def test_start_page_shows_ranking_and_next_walks_to_stories_and_revenue(repo: Path):
    at = run_app()
    assert_clean(at)
    assert at.session_state["ticker"] == "EXMP" and at.session_state["page"] == 0
    assert "Step 1 of 10: Start" in progress_text(at)
    table = at.table[0].value
    assert list(table.columns) == ["Factor", "What we nudged", "Change in base value per share (USD)"]
    assert list(table["Factor"]) == ["Operating margin", "Terminal value", "Revenue growth", "Cost of capital",
                                     "Reinvestment", "Taxes and weights"]          # one row per page, largest first
    changes = [abs(float(x)) for x in table["Change in base value per share (USD)"]]
    assert changes == sorted(changes, reverse=True)
    assert not any("With your current inputs" in m.value for m in at.markdown)     # no results before the last page
    # the sidebar shows no value on Start or The stories, only a line saying when it appears
    assert not any("With your current inputs" in c.value for c in at.sidebar.caption)
    assert any("appears here once the factor pages begin" in c.value for c in at.sidebar.caption)
    # the sidebar step list has ten steps, in the impact order for this company
    labels = [b.label for b in at.sidebar.button]
    assert labels[:4] == ["1. Start", "2. The stories", "3. Revenue growth", "4. Operating margin"]
    assert labels[4:] == ["5. Terminal value", "6. Cost of capital", "7. Reinvestment", "8. Taxes and weights",
                          "9. Facts check", "10. Results"]

    at.button(key="next_btn").click().run()
    assert_clean(at)
    assert at.session_state["page"] == 1 and "Step 2 of 10: The stories" in progress_text(at)
    gen = at.session_state["gen"]
    stories = [t for t in at.text_area if t.key.startswith(f"w{gen}:scenarios.") and t.key.endswith(".story")]
    assert [s.key.split(".")[1] for s in stories] == ["bear", "base", "bull"]
    paths = at.table[1].value                                   # the base case's two defining paths, one row per year
    assert list(paths.columns) == ["Year", "Revenue growth", "Operating margin"]
    assert list(paths.iloc[0]) == ["Y1", "20.0%", "18.0%"] and list(paths.iloc[4]) == ["Y5", "20.0%", "26.0%"]
    assert any("Y1 to Y5 are the forecast years" in c.value for c in at.caption)

    assert not any("With your current inputs" in c.value for c in at.sidebar.caption)      # still none on Stories
    at.button(key="next_btn").click().run()
    assert_clean(at)
    assert at.session_state["page"] == 2 and "Step 3 of 10: Revenue growth" in progress_text(at)
    assert any("With your current inputs" in c.value for c in at.sidebar.caption)          # from here on
    # four cases (management is computable in the fixture), five boxes each, prefilled as percentages
    assert len(at.number_input) == 20
    assert at.number_input(key=f"w{gen}:scenarios.base.revenue_growth.values.0").value == 20.0
    assert "History:" in " ".join(m.value for m in at.markdown)                    # diagnostics.historical_revenue_cagr


def test_changing_a_year_one_growth_box_changes_the_live_readout(repo: Path):
    at = run_app()
    go_to(at, "revenue_growth")
    before = at.session_state["last_result"].scenarios["base"].per_share
    line_before = readout(at)
    assert "Base 41.72" in line_before and "against a price of 70.00" in line_before
    gen = at.session_state["gen"]
    at.number_input(key=f"w{gen}:scenarios.base.revenue_growth.values.0").set_value(30.0).run()
    assert_clean(at)
    assert at.session_state["working"]["scenarios"]["base"]["revenue_growth"]["values"][0] == 0.30
    after = at.session_state["last_result"].scenarios["base"].per_share
    assert after > before
    assert readout(at) != line_before and f"Base {after:,.2f} (as loaded 41.72)" in readout(at)
    # the edit survives moving pages
    at.button(key="next_btn").click().run()
    at.button(key="back_btn").click().run()
    assert_clean(at)
    assert at.session_state["working"]["scenarios"]["base"]["revenue_growth"]["values"][0] == 0.30
    assert at.number_input(key=f"w{gen}:scenarios.base.revenue_growth.values.0").value == 30.0


def test_results_page_table_save_with_note_and_regenerated_markdown(repo: Path):
    yaml_path = repo / "companies" / "EXMP" / "valuation" / "assumptions.yaml"
    at = run_app()
    go_to(at, "reinvestment")
    gen = at.session_state["gen"]
    widget = at.number_input(key=f"w{gen}:scenarios.base.sales_to_capital.value")
    assert widget.value == 1.5
    widget.set_value(2.5).run()
    assert_clean(at)
    after = at.session_state["last_result"].scenarios["base"].per_share
    go_to(at, "results")
    assert "Step 10 of 10: Results" in progress_text(at)
    table = at.table[0].value
    assert list(table["Case"]) == ["Bear", "Base", "Bull", "Management", "Weighted expected"]
    assert table.loc[table["Case"] == "Base", "Price"].iloc[0] == "70.00"
    assert table.loc[table["Case"] == "Base", "Value per share"].iloc[0] == f"{after:,.2f}"
    # the file is untouched so far and the unsaved-changes list names the edit in words with page-style values
    assert yaml.safe_load(yaml_path.read_text(encoding="utf-8"))["scenarios"]["base"]["sales_to_capital"]["value"] == 1.5
    changes = [t.value for t in at.table if "Input" in t.value.columns]
    assert changes and list(changes[0].iloc[0]) == ["Base case, sales-to-capital, years 1-5", "1.50", "2.50"]
    assert not any("scenarios." in m.value for m in at.markdown)        # no dotted paths anywhere on the page

    at.text_input(key="save_note:EXMP").input("owner: fabless peers reinvest less").run()
    assert not at.button(key="write_btn").disabled is False or at.button(key="write_btn").disabled   # disabled while unsaved
    at.button(key="save_btn").click().run()
    assert_clean(at)
    assert at.button(key="write_btn").disabled is False
    text = yaml_path.read_text(encoding="utf-8")
    plain = yaml.safe_load(text)
    assert plain["scenarios"]["base"]["sales_to_capital"]["value"] == 2.5
    assert plain["changelog"] == [{
        "at": plain["owner_edited"], "path": "scenarios.base.sales_to_capital.value", "old": 1.5, "new": 2.5,
        "note": "owner: fabless peers reinvest less"}]
    assert "# Example assumptions.yaml following AGENTS.md section 18.4." in text     # comments survive
    md = yaml_path.parent / "assumptions.md"
    assert md.exists()
    md_text = md.read_text(encoding="utf-8")
    assert "## 9. Change log" in md_text and "owner: fabless peers reinvest less" in md_text
    assert "| Sales-to-capital, years 1-5 | 1.20 | 2.50 | 1.80 | 1.50 |" in md_text
    # after the save the walk stays on Results, the working copy matches the file and the value stays
    assert at.session_state["page"] == PAGES.index("results")
    assert at.session_state["working"]["scenarios"]["base"]["sales_to_capital"]["value"] == 2.5
    assert at.session_state["last_result"].scenarios["base"].per_share == pytest.approx(after)
    assert any("Saved 1 change" in s.value for s in at.success)
    assert sorted(p.name for p in yaml_path.parent.iterdir()) == ["assumptions.md", "assumptions.yaml"]


def test_percent_boxes_do_not_create_spurious_changes(repo: Path):
    at = run_app()
    go_to(at, "taxes_weights")
    gen = at.session_state["gen"]
    assert at.number_input(key=f"w{gen}:scenarios.base.tax_rate.start").value == 8.0
    at.number_input(key=f"w{gen}:scenarios.base.tax_rate.start").set_value(16.8).run()
    assert_clean(at)
    assert at.session_state["working"]["scenarios"]["base"]["tax_rate"]["start"] == 0.168
    at.number_input(key=f"w{gen}:scenarios.base.tax_rate.start").set_value(8.0).run()
    go_to(at, "results")
    assert any("Unsaved changes (0)" in e.label for e in at.expander)


def test_terminal_growth_checkbox_toggles_the_riskfree_word(repo: Path):
    at = run_app()
    go_to(at, "terminal")
    gen = at.session_state["gen"]
    box = at.checkbox(key=f"w{gen}:scenarios.base.terminal.growth.value#riskfree")
    assert box.value is True
    box.uncheck().run()
    assert_clean(at)
    doc = at.session_state["working"]
    assert doc["scenarios"]["base"]["terminal"]["growth"]["value"] == pytest.approx(0.0425)
    gen = at.session_state["gen"]
    at.number_input(key=f"w{gen}:scenarios.base.terminal.growth.value").set_value(3.0).run()
    assert_clean(at)
    assert doc["scenarios"]["base"]["terminal"]["growth"]["value"] == pytest.approx(0.03)
    at.checkbox(key=f"w{gen}:scenarios.base.terminal.growth.value#riskfree").check().run()
    assert_clean(at)
    assert at.session_state["working"]["scenarios"]["base"]["terminal"]["growth"]["value"] == "riskfree"


def test_a_null_stops_one_scenario_without_a_traceback(repo: Path):
    yaml_path = repo / "companies" / "EXMP" / "valuation" / "assumptions.yaml"
    text = yaml_path.read_text(encoding="utf-8")
    assert text.count("value_late: 1.5") == 1                     # the bull case
    yaml_path.write_text(text.replace("value_late: 1.5", "value_late: null"), encoding="utf-8")
    at = run_app()
    assert_clean(at)
    result = at.session_state["last_result"]
    assert result is not None and "bull" not in result.scenarios and "bull" in result.stopped
    # the readout shows the engine's message in the bull slot, never a traceback
    go_to(at, "revenue_growth")
    line = readout(at)
    assert "Bull not computed (see its box)" in line and "Base 41.72" in line and "null" not in line
    go_to(at, "reinvestment")
    assert any("Bull case not computed with the current inputs: Bull case, sales-to-capital, years 6-10 is empty" in w.value
               for w in at.warning)
    go_to(at, "results")
    table = at.table[0].value
    assert table.loc[table["Case"] == "Bull", "Value per share"].iloc[0] == "not computed"
    assert any("Bull case not computed: Bull case, sales-to-capital, years 6-10 is empty" in c.value for c in at.caption)
    assert not any("scenarios." in c.value for c in at.caption)


def test_write_valuation_refuses_with_unsaved_changes_and_start_over_reloads(repo: Path):
    vdir = repo / "companies" / "EXMP" / "valuation"
    at = run_app()
    go_to(at, "reinvestment")
    gen = at.session_state["gen"]
    at.number_input(key=f"w{gen}:scenarios.base.sales_to_capital.value").set_value(2.0).run()
    go_to(at, "results")
    assert at.button(key="write_btn").disabled                    # disabled, with a caption saying why
    assert any("Disabled until you save" in c.value for c in at.caption)
    assert not (vdir / "valuation.md").exists()
    # Start over asks for confirmation while there are unsaved changes
    at.button(key="restart_btn").click().run()
    assert_clean(at)
    assert at.session_state["confirm_restart"] is True and at.button(key="restart_yes")
    at.button(key="restart_yes").click().run()
    assert_clean(at)
    assert at.session_state["page"] == 0
    assert at.session_state["working"]["scenarios"]["base"]["sales_to_capital"]["value"] == 1.5
    go_to(at, "results")
    at.button(key="write_btn").click().run()
    assert_clean(at)
    assert (vdir / "valuation.md").exists() and (vdir / "assumptions.md").exists()
    assert "## 1. Results" in (vdir / "valuation.md").read_text(encoding="utf-8")


def test_horizon_switch_pads_lists_and_shows_ten_boxes(repo: Path):
    at = run_app()
    gen = at.session_state["gen"]
    at.radio(key=f"w{gen}:horizon").set_value(10).run()
    assert_clean(at)
    doc = at.session_state["working"]
    assert doc["horizon"] == 10
    assert doc["scenarios"]["base"]["revenue_growth"]["values"] == [0.20] * 10
    assert doc["scenarios"]["bull"]["reinvestment_override"]["values"] == [400, None, None, None, None] + [None] * 5
    assert at.session_state["last_result"].horizon == 10
    assert any("Horizon set to 10" in i.value for i in at.info)
    go_to(at, "revenue_growth")
    assert len(at.number_input) == 40                              # four cases, ten boxes each


def test_commit_messages_follow_section_18_7(repo: Path):
    """Owner edits alone commit as 'owner edits'; a written valuation.md commits as 'compute <QLABEL> rev N'."""
    import subprocess

    def git(*args: str) -> str:
        return subprocess.run(["git", *args], cwd=str(repo), capture_output=True, text=True, check=True).stdout

    git("init", "-q")
    git("-c", "user.name=t", "-c", "user.email=t@localhost", "add", ".")
    git("-c", "user.name=t", "-c", "user.email=t@localhost", "commit", "-q", "-m", "start")
    at = run_app()
    go_to(at, "reinvestment")
    gen = at.session_state["gen"]
    at.number_input(key=f"w{gen}:scenarios.base.sales_to_capital.value").set_value(2.0).run()
    go_to(at, "results")
    at.button(key="save_btn").click().run()
    at.button(key="commit_btn").click().run()
    assert_clean(at)
    assert git("log", "-1", "--format=%s%n%an").splitlines() == ["value(EXMP): owner edits to assumptions", "company-research"]
    assert any("Committed" in s.value for s in at.success)
    at.button(key="write_btn").click().run()
    at.button(key="commit_btn").click().run()
    assert_clean(at)
    assert git("log", "-1", "--format=%s").strip() == "value(EXMP): compute FY2027-Q2 rev 1"
    assert not git("status", "--porcelain").strip()
    at.button(key="commit_btn").click().run()
    assert any("Nothing to commit" in s.value for s in at.success)


def test_no_dollar_signs_math_symbols_or_internals_in_the_apps_prose(repo: Path):
    """Streamlit reads ``$`` as a formula; the owner never sees maths symbols, dotted paths, YAML keys,
    section citations or option tokens."""
    import re

    at = run_app()
    banned = re.compile(r"(?<![\\])\$|[×Σ≤≥−÷→]|§|\b(?:scenarios|base_year|bridge|cost_of_capital|diagnostics)\.\w+"
                        r"|--set|= False|= True|\bnull\b|used_as|reinvestment_override|allow_above_riskfree")
    for page in PAGES:
        go_to(at, page)
        texts = [m.value for m in at.markdown] + [c.value for c in at.caption] + [w.value for w in at.warning]
        for text in texts:
            assert not banned.search(text), (page, text)


def test_company_change_resets_the_walk_to_start(repo: Path):
    import shutil

    second = repo / "companies" / "OTHR" / "valuation"
    second.mkdir(parents=True)
    shutil.copy(repo / "companies" / "EXMP" / "valuation" / "assumptions.yaml", second / "assumptions.yaml")
    at = run_app()
    assert at.session_state["ticker"] == "EXMP"
    go_to(at, "revenue_growth")
    gen = at.session_state["gen"]
    at.number_input(key=f"w{gen}:scenarios.base.revenue_growth.values.0").set_value(30.0).run()
    # the sidebar step list jumps back to Start, where the company picker lives
    at.sidebar.button(key="step_0").click().run()
    assert_clean(at)
    assert at.session_state["page"] == 0
    at.selectbox(key="company_pick").select("OTHR").run()
    assert_clean(at)
    assert at.session_state["ticker"] == "OTHR" and at.session_state["page"] == 0
    assert at.session_state["visited"] == {0}
    assert at.session_state["working"]["scenarios"]["base"]["revenue_growth"]["values"][0] == 0.20   # fresh copy
    assert str(at.session_state["path"]).endswith("OTHR/valuation/assumptions.yaml")


def test_start_page_uses_the_cached_tbond_rate_when_fred_is_unavailable(repo: Path):
    """With `risk_free_rate: auto` and no network the walk still computes; the Start page shows the
    Damodaran T-bond rate as a normal value with a note, not as a warning, and keeps the override box."""
    from valuation import datasets

    yaml_path = repo / "companies" / "EXMP" / "valuation" / "assumptions.yaml"
    yaml_path.write_text(yaml_path.read_text(encoding="utf-8").replace("risk_free_rate: 0.0425", "risk_free_rate: auto"),
                         encoding="utf-8")
    latest = datasets.latest_erp()
    at = run_app()
    assert_clean(at)
    market = at.session_state["market_inputs"]
    assert market is not None and market.risk_free_rate == latest.tbond_rate
    assert market.risk_free_source == "Damodaran ERPbymonth T-bond rate (FRED unavailable)"
    assert at.session_state["last_result"] is not None                    # the walk is not stuck
    assert not any("Risk-free rate" in w.value for w in at.warning)      # no warning box for the fallback
    assert any(f"Fetched: {latest.tbond_rate * 100:.2f}% on {latest.date}" in c.value
               and "Damodaran ERPbymonth T-bond rate" in c.value for c in at.caption)
    assert any("Note: fetching is off" in c.value or "Note: FRED was unreachable" in c.value for c in at.caption)
    assert at.number_input(key="mkt:EXMP:rf").value == pytest.approx(latest.tbond_rate * 100)
    assert any("cached Damodaran ERPbymonth dataset" in w for w in market.warnings)


def test_facts_page_lists_where_the_numbers_come_from(repo: Path):
    at = run_app()
    go_to(at, "facts")
    assert any(e.label.startswith("Where the numbers come from (2 sources)") for e in at.expander)
    tables = [t.value for t in at.table if list(t.value.columns) == ["Tag", "Cached file", "Date", "Note"]]
    assert tables
    first = [str(x).replace("\\", "") for x in tables[0].iloc[0]]        # cells are markdown-escaped for display
    assert first == ["[10-Q Q2 FY2027, ...]", "sources/FY2027-Q2/10-Q-FY2027-Q2.txt", "2026-08-28", "quarter ended 2026-08-01"]


def test_file_changed_on_disk_shows_a_banner_and_disables_save(repo: Path):
    yaml_path = repo / "companies" / "EXMP" / "valuation" / "assumptions.yaml"
    at = run_app()
    go_to(at, "reinvestment")
    gen = at.session_state["gen"]
    at.number_input(key=f"w{gen}:scenarios.base.sales_to_capital.value").set_value(2.0).run()
    # another process (an agent redraft) rewrites the file while the walk is open
    text = yaml_path.read_text(encoding="utf-8").replace("weight: 0.25\n    story: |\n      The custom-chip",
                                                          "weight: 0.25\n    story: |\n      REWRITTEN The custom-chip")
    assert "REWRITTEN" in text
    yaml_path.write_text(text, encoding="utf-8")
    import os, time
    os.utime(yaml_path, (time.time() + 5, time.time() + 5))
    at.run()
    assert_clean(at)
    assert any("changed on disk" in w.value for w in at.warning)
    go_to(at, "results")
    assert at.button(key="save_btn").disabled and at.button(key="write_btn").disabled
    assert not any("Input" in t.value.columns for t in at.table)          # the file's edits are not listed as the owner's
    assert any("Disabled: the file changed on disk" in c.value for c in at.caption)
    at.button(key="restart_btn").click().run()
    assert_clean(at)
    assert at.session_state["page"] == 0 and not any("changed on disk" in w.value for w in at.warning)
    assert "REWRITTEN" in at.session_state["working"]["scenarios"]["bear"]["story"]
