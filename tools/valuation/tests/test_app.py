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
         "taxes_weights", "facts", "results", "analysis", "forecast", "simulation", "checks", "review"]          # the fixture's impact order


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
    """Jump directly to a workspace page, in either direction."""
    target = PAGES.index(page)
    if at.session_state["page"] != target:
        at.sidebar.button(key=f"step_{target}").click().run()
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
    assert "Step 1 of 15: Overview" in progress_text(at)
    table = at.table[0].value
    assert list(table.columns) == ["Factor", "What we nudged", "Change in base value per share (USD)"]
    assert list(table["Factor"]) == ["Operating margin", "Terminal value", "Revenue growth", "Cost of capital",
                                     "Reinvestment", "Taxes and weights"]          # one row per page, largest first
    changes = [abs(float(x)) for x in table["Change in base value per share (USD)"]]
    assert changes == sorted(changes, reverse=True)
    assert not any("With your current inputs" in m.value for m in at.markdown)     # no results before the last page
    # The sidebar is navigation only; the live valuation belongs to the main header.
    assert not at.sidebar.metric
    # All fifteen destinations are directly accessible, grouped by purpose.
    labels = [b.label for b in at.sidebar.button]
    assert labels == ["Overview", "Scenarios", "Revenue growth", "Operating margin", "Terminal value",
                      "Cost of capital", "Reinvestment", "Taxes and weights", "Source facts", "Valuation",
                      "Analysis", "Cash flow forecast", "Simulation", "Model checks", "Review & save"]

    at.button(key="next_btn").click().run()
    assert_clean(at)
    assert at.session_state["page"] == 1 and "Step 2 of 15: Scenarios" in progress_text(at)
    gen = at.session_state["gen"]
    stories = [t for t in at.text_area if t.key.startswith(f"w{gen}:scenarios.") and t.key.endswith(".story")]
    assert [s.key.split(".")[1] for s in stories] == ["bear", "base", "bull"]
    paths = at.table[1].value                                   # the base case's two defining paths, one row per year
    assert list(paths.columns) == ["Year", "Revenue growth", "Operating margin"]
    assert list(paths.iloc[0]) == ["Y1", "20.0%", "18.0%"] and list(paths.iloc[4]) == ["Y5", "20.0%", "26.0%"]
    assert any("Y1 to Y5 are forecast years 1 to 5" in c.value for c in at.caption)
    # Live input matrices map one variable to one value per year, with units.
    chosen = [t.value for t in at.table if "Variable" in t.value.columns and "Year 1" in t.value.columns]
    assert len(chosen) == 4  # Three independent cases plus the computable management fixture.
    base_growth = chosen[1].set_index("Variable").loc["Revenue growth"]
    assert base_growth.tolist() == ["20.0%"] * 5
    base_margin = chosen[1].set_index("Variable").loc["Operating margin"]
    assert base_margin.tolist() == ["18.0%", "20.0%", "22.0%", "24.0%", "26.0%"]
    assert any("How this story becomes numbers" in m.value for m in at.markdown)

    assert not any("With your current inputs" in c.value for c in at.sidebar.caption)      # still none on Stories
    at.button(key="next_btn").click().run()
    assert_clean(at)
    assert at.session_state["page"] == 2 and "Step 3 of 15: Revenue growth" in progress_text(at)
    assert at.metric and not at.sidebar.metric  # the live case is now in the main header
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


def test_valuation_table_and_review_save_with_note_and_regenerated_markdown(repo: Path):
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
    assert "Step 10 of 15: Valuation" in progress_text(at)
    table = at.table[0].value
    assert list(table["Case"]) == ["Bear", "Base", "Bull", "Management", "Weighted expected"]
    assert table.loc[table["Case"] == "Base", "Price"].iloc[0] == "70.00"
    assert table.loc[table["Case"] == "Base", "Value per share"].iloc[0] == f"{after:,.2f}"
    go_to(at, "review")
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
    # after the save the workspace stays on Review, the working copy matches the file and the value stays
    assert at.session_state["page"] == PAGES.index("review")
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
    go_to(at, "review")
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


def test_entirely_blocked_draft_renders_all_pages_and_keeps_missing_inputs(repo: Path):
    """AVGO-shaped shared gaps and unfunded later years must not hide the editable narrative."""
    path = repo / "companies/EXMP/valuation/assumptions.yaml"
    doc = yaml.safe_load(path.read_text())
    doc["horizon"] = 10
    for field, name in (("non_operating_assets", "Unresolved corporate investments"),
                        ("other_claims", "Unresolved customer guarantee")):
        doc["bridge"][field] = [{"name": name, "value": None,
                                  "reason": "The current balance needs evidence.", "source": "[Latest filing]"}]
    for scenario in doc["scenarios"].values():
        scenario["sales_to_capital"]["value_late"] = None
    path.write_text(yaml.safe_dump(doc))
    original = path.read_bytes()
    at = run_app()
    assert_clean(at)
    assert at.session_state["last_result"] is None
    assert any("cannot compute yet" in e.value for e in at.error)
    # A failed ranking uses the default factor order, so follow the observed destinations.
    for index in range(15):
        at.sidebar.button(key=f"step_{index}").click().run()
        assert_clean(at)
        assert at.get("progress")
        assert at.session_state["last_result"] is None
        if index == 1:
            assert any("The base story" in m.value for m in at.markdown)
        if index == 4:  # Reinvestment in the default order.
            gen = at.session_state["gen"]
            field = f"w{gen}:scenarios.base.sales_to_capital.value_late"
            assert at.number_input(key=field).value is None
            assert any(c.value == "3 inputs need attention. See Model checks." for c in at.caption)
            assert not any("No case could be computed" in c.value for c in at.caption)
            at.selectbox(key="watch_case").select("weighted").run()
            assert any(c.value == "Needs all three cases and valid weights. See Model checks." for c in at.caption)
        if index == 13:
            assert any("Bridge: other claim 1" in e.value and "sales-to-capital, years 6-10" in e.value for e in at.error)
        if index == 14:
            assert at.button(key="write_btn").disabled
    # Ordinary edits still work, remain in memory, and never fill evidence gaps with zero.
    at.sidebar.button(key="step_2").click().run()
    gen = at.session_state["gen"]
    at.number_input(key=f"w{gen}:scenarios.base.revenue_growth.values.0").set_value(30).run()
    at.sidebar.button(key="step_1").click().run()
    assert_clean(at)
    working = at.session_state["working"]
    assert working["scenarios"]["base"]["revenue_growth"]["values"][0] == .30
    assert working["bridge"]["other_claims"][0]["value"] is None
    assert working["scenarios"]["base"]["sales_to_capital"]["value_late"] is None
    assert path.read_bytes() == original
    assert list(path.parent.iterdir()) == [path]


def test_review_terminal_rate_survives_missing_quote_and_never_invents_zero(repo: Path, monkeypatch):
    from unittest.mock import Mock
    import valuation

    monkeypatch.setenv("VALUATION_APP_REVIEW_ONLY", "1")
    path = repo / "companies/EXMP/valuation/assumptions.yaml"
    doc = yaml.safe_load(path.read_text())
    doc["market"]["price"] = "auto"
    doc["market"]["risk_free_rate"] = .0475
    doc["scenarios"]["bear"]["terminal"]["growth"]["value"] = "riskfree"
    path.write_text(yaml.safe_dump(doc))
    original = path.read_bytes()
    forbidden = Mock(side_effect=AssertionError("valuation compute called"))
    monkeypatch.setattr(valuation, "compute", forbidden)
    at = run_app()
    assert at.session_state["market_inputs"] is None
    at.sidebar.button(key="step_6").click().run()  # Review mode's default Terminal page.
    assert_clean(at)
    gen = at.session_state["gen"]
    key = f"w{gen}:scenarios.bear.terminal.growth.value#riskfree"
    assert at.checkbox(key=key).label == "Equal to the risk-free rate (4.75%)"
    at.checkbox(key=key).uncheck().run()
    assert at.session_state["working"]["scenarios"]["bear"]["terminal"]["growth"]["value"] == .0475

    # A rate-source failure must stay unavailable, rather than becoming a zero input.
    at.session_state["market_values"]["EXMP"]["rf"] = None
    at.run()
    assert_clean(at)
    gen = at.session_state["gen"]
    control = at.checkbox(key=f"w{gen}:scenarios.bear.terminal.growth.value#riskfree")
    assert control.disabled and "unavailable" in control.label
    assert at.session_state["working"]["scenarios"]["bear"]["terminal"]["growth"]["value"] == .0475
    assert path.read_bytes() == original
    forbidden.assert_not_called()


def test_draft_review_mode_never_computes_fetches_or_writes_a_report(repo: Path, monkeypatch):
    """Even a complete draft can be verified before the owner authorizes valuation results."""
    from unittest.mock import Mock
    import valuation
    from valuation import app_core

    monkeypatch.setenv("VALUATION_APP_REVIEW_ONLY", "1")
    monkeypatch.delenv("VALUATION_APP_NO_FETCH", raising=False)
    path = repo / "companies/EXMP/valuation/assumptions.yaml"
    doc = yaml.safe_load(path.read_text())
    doc["market"]["price"] = "auto"
    doc["switches"]["reinvestment_lag"] = 0  # A non-blocking validator warning must remain visible.
    path.write_text(yaml.safe_dump(doc))
    original = path.read_bytes()
    forbidden = {"compute": Mock(side_effect=AssertionError("valuation compute called")),
                 "ranking": Mock(side_effect=AssertionError("factor ranking called")),
                 "fetch": Mock(side_effect=AssertionError("price fetch called")),
                 "write": Mock(side_effect=AssertionError("report writer called"))}
    monkeypatch.setattr(valuation, "compute", forbidden["compute"])
    monkeypatch.setattr(app_core, "impact_ranking", forbidden["ranking"])
    monkeypatch.setattr(app_core.market_mod, "fetch_price", forbidden["fetch"])
    monkeypatch.setattr(app_core, "run_and_write", forbidden["write"])
    at = run_app()
    assert_clean(at)
    assert at.session_state["market_inputs"] is None
    # Complete the market inputs in memory so the normal app would now compute and rank.
    at.number_input(key="mkt:EXMP:price").set_value(70.0).run()
    assert_clean(at)
    assert at.session_state["market_inputs"] is not None
    for index in range(15):
        at.sidebar.button(key=f"step_{index}").click().run()
        assert_clean(at)
        assert any("Draft review mode" in item.value for item in at.info)
        assert at.session_state["last_result"] is None
        assert not at.error
        assert not any(metric.label == "Current value" for metric in at.metric)
        if index == 13:
            assert any("same year" in warning.value for warning in at.warning)
    assert at.button(key="write_btn").disabled
    # Enforce the same gate in the callback, not only in the disabled button.
    app_core._write_cb(path)
    for mocked in forbidden.values():
        mocked.assert_not_called()
    assert path.read_bytes() == original
    assert list(path.parent.iterdir()) == [path]
    assert not any("scenarios." in c.value for c in at.caption)


def test_write_valuation_refuses_with_unsaved_changes_and_start_over_reloads(repo: Path):
    vdir = repo / "companies" / "EXMP" / "valuation"
    at = run_app()
    go_to(at, "reinvestment")
    gen = at.session_state["gen"]
    at.number_input(key=f"w{gen}:scenarios.base.sales_to_capital.value").set_value(2.0).run()
    go_to(at, "review")
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
    go_to(at, "review")
    at.button(key="write_btn").click().run()
    assert_clean(at)
    assert (vdir / "valuation.md").exists() and (vdir / "assumptions.md").exists()
    assert "## 1. Results" in (vdir / "valuation.md").read_text(encoding="utf-8")


def test_horizon_switch_to_ten_keeps_five_boxes_and_shows_the_fade_line(repo: Path):
    """Section 18.2: ten years means five set and five by rule, so the lists and the boxes stay at five."""
    at = run_app()
    gen = at.session_state["gen"]
    at.radio(key=f"w{gen}:horizon").set_value(10).run()
    assert_clean(at)
    doc = at.session_state["working"]
    assert doc["horizon"] == 10
    assert doc["scenarios"]["base"]["revenue_growth"]["values"] == [0.20] * 5     # untouched
    assert doc["scenarios"]["bull"]["reinvestment_override"]["values"] == [400, None, None, None, None]
    result = at.session_state["last_result"]
    assert result.horizon == 10 and result.reference_label == "5-year stop"
    assert len(result.scenarios["base"].rows) == 10
    assert any("Forecast set to 10 years" in i.value for i in at.info)

    go_to(at, "revenue_growth")
    assert len(at.number_input) == 20                              # four cases, five boxes each
    captions = [c.value for c in at.caption]
    fades = [c for c in captions if c.startswith("Years 6-10 by rule:")]
    assert len(fades) == 4                                          # one per case
    # the base case eases from 20% to the run's risk-free rate in five equal steps, one rounding throughout
    # one rounding for every rate in the sentence, and the last step is the terminal rate itself (item 7)
    assert "16.9% / 13.7% / 10.6% / 7.4% / 4.2%" in fades[1]
    assert "easing to the terminal growth of 4.2% by year 10, from 20.0% in year 5." in fades[1]
    go_to(at, "operating_margin")
    holds = [c.value for c in at.caption if "the margin is held at" in c.value]
    assert holds and "Years 6-10 by rule: the margin is held at 26.0% through year 10." in holds
    # the results table names the other structure
    go_to(at, "results")
    table = at.table[0].value
    assert "5-year stop per share" in list(table.columns)
    assert "10-year fade per share" not in list(table.columns)


def test_ten_entry_lists_show_ten_boxes_and_no_fade_line(repo: Path):
    """A file whose analyst shaped years 6-10 by hand gets ten boxes and no rule line (section 18.2)."""
    yaml_path = repo / "companies" / "EXMP" / "valuation" / "assumptions.yaml"
    doc = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    doc["horizon"] = 10
    for name in ("bear", "base", "bull", "management"):
        sc = doc["scenarios"][name]
        sc["revenue_growth"]["values"] = list(sc["revenue_growth"]["values"]) + [0.04] * 5
        sc["operating_margin"]["values"] = list(sc["operating_margin"]["values"]) + [sc["operating_margin"]["values"][4]] * 5
        sc["reinvestment_override"]["values"] = list(sc["reinvestment_override"]["values"]) + [None] * 5
    yaml_path.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True), encoding="utf-8")
    at = run_app()
    assert_clean(at)
    go_to(at, "revenue_growth")
    assert len(at.number_input) == 40                              # four cases, ten boxes each
    assert not any(c.value.startswith("Years 6-10 by rule:") for c in at.caption)


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
    go_to(at, "review")
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


BANNED = (r"(?<![\\])\$|[×Σ≤≥−÷→]|§|\b(?:scenarios|base_year|bridge|cost_of_capital|diagnostics)\.\w+"
          r"|--set|= False|= True|\bnull\b|used_as|reinvestment_override|allow_above_riskfree|allow_large_premium")


def test_no_dollar_signs_math_symbols_or_internals_in_the_apps_prose(repo: Path):
    """Streamlit reads ``$`` as a formula; the owner never sees maths symbols, dotted paths, YAML keys,
    section citations or option tokens."""
    import re

    at = run_app()
    banned = re.compile(BANNED)
    for page in PAGES:
        go_to(at, page)
        texts = [m.value for m in at.markdown] + [c.value for c in at.caption] + [w.value for w in at.warning]
        for text in texts:
            assert not banned.search(text), (page, text)


def test_the_ten_year_walk_renders_every_page_in_plain_words(repo: Path):
    """The default structure of section 18.2, end to end: the Start paragraph, the story clauses, the
    fade lines, the marked year-by-year table and the transition check, none of them leaking internals."""
    import re

    yaml_path = repo / "companies" / "EXMP" / "valuation" / "assumptions.yaml"
    yaml_path.write_text(yaml_path.read_text(encoding="utf-8").replace("horizon: 5", "horizon: 10"), encoding="utf-8")
    at = run_app()
    assert_clean(at)
    banned = re.compile(BANNED)
    assert any("ten years: five you set" in m.value for m in at.markdown)
    for page in PAGES:
        go_to(at, page)
        assert_clean(at)
        texts = [m.value for m in at.markdown] + [c.value for c in at.caption] + [w.value for w in at.warning]
        for text in texts:
            assert not banned.search(text), (page, text)
        if page == "stories":
            # one clause per defining path, each naming its own year-10 number (audit 4, item 3)
            growth = [c.value for c in at.caption if c.value.startswith("Revenue growth: Then")]
            margin = [c.value for c in at.caption if c.value.startswith("Operating margin: Then")]
            assert len(growth) == 4 and len(margin) == 4              # bear, base, bull, management
            assert growth[1] == "Revenue growth: Then easing to 4.2% by year 10."
            assert margin[1] == "Operating margin: Then held at 26.0% through year 10."
        if page == "results":
            assert any("5-year stop per share" in list(t.value.columns) for t in at.table)
        if page == "forecast":
            years = [t.value for t in at.table if "Year" in list(t.value.columns)
                     and "Free cash flow" in list(t.value.columns)]
            assert years and "10 (by rule)" in list(years[0]["Year"])
        if page == "checks":
            diags = [t.value for t in at.table if list(t.value.columns) == ["Item", "Value"]]
            text = " ".join(str(x) for t in diags for x in t["Item"])
            assert "free cash flow (USD millions)" in text            # the transition check is on the page


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
    assert first == ["[10-Q Q2 FY2027, ...]", "sources/FY2027-Q2/10-Q-FY2027-Q2.txt (not cached)", "2026-08-28", "quarter ended 2026-08-01"]


def test_bear_terminal_premium_is_editable_and_large_premium_needs_override(repo: Path):
    """The owner can retain a bear advantage, with the same large-premium control as base."""
    path = repo / "companies/EXMP/valuation/assumptions.yaml"
    doc = yaml.safe_load(path.read_text())
    doc["scenarios"]["bear"]["terminal"]["roic_premium"]["reason"] = (
        "Customer switching costs persist despite weaker demand.")
    path.write_text(yaml.safe_dump(doc))
    original = path.read_bytes()
    at = run_app()
    go_to(at, "terminal")
    gen = at.session_state["gen"]
    keys = [c.key for c in at.checkbox]
    for name in ("bear", "base", "bull"):
        assert f"w{gen}:scenarios.{name}.terminal.roic_premium.allow_large_premium" in keys
    assert not any("stays at zero by rule" in c.value for c in at.caption)
    premium = f"w{gen}:scenarios.bear.terminal.roic_premium.value"
    override = f"w{gen}:scenarios.bear.terminal.roic_premium.allow_large_premium"
    assert at.number_input(key=premium).value == 0.0
    at.number_input(key=premium).set_value(2.0).run()
    assert_clean(at)
    assert at.session_state["working"]["scenarios"]["bear"]["terminal"]["roic_premium"]["value"] == .02
    assert at.session_state["last_result"].scenarios["bear"].inputs.roic_premium == .02
    at.number_input(key=premium).set_value(9.0).run()
    assert_clean(at)
    assert at.session_state["last_result"] is None
    go_to(at, "checks")
    assert any("above 8 points" in e.value for e in at.error)
    go_to(at, "terminal")
    at.checkbox(key=override).check().run()
    assert_clean(at)
    result = at.session_state["last_result"]
    assert result.scenarios["bear"].inputs.roic_premium == .09
    assert any("bear: terminal ROIC premium 0.090" in w for w in result.warnings)
    assert path.read_bytes() == original
    go_to(at, "review")
    at.text_input(key="save_note:EXMP").input("Owner supports a retained advantage in bear").run()
    at.button(key="save_btn").click().run()
    assert_clean(at)
    saved = yaml.safe_load(path.read_text())
    assert saved["scenarios"]["bear"]["terminal"]["roic_premium"]["value"] == .09
    assert saved["scenarios"]["bear"]["terminal"]["roic_premium"]["allow_large_premium"] is True
    assert saved["scenarios"]["base"] == doc["scenarios"]["base"]
    assert {entry["path"] for entry in saved["changelog"]} == {
        "scenarios.bear.terminal.roic_premium.value", "scenarios.bear.terminal.roic_premium.allow_large_premium"}


def test_the_fade_verb_follows_the_direction_of_the_rule(repo: Path):
    """A year-5 growth below terminal growth is raised by the rule, so "easing" would be wrong (item 2)."""
    at = run_app()
    gen = at.session_state["gen"]
    at.radio(key=f"w{gen}:horizon").set_value(10).run()
    go_to(at, "revenue_growth")
    gen = at.session_state["gen"]
    at.number_input(key=f"w{gen}:scenarios.bear.revenue_growth.values.4").set_value(2.0).run()
    assert_clean(at)
    fades = [c.value for c in at.caption if c.value.startswith("Years 6-10 by rule:")]
    assert any("moving up to the terminal growth of 4.25% by year 10, from 2.00% in year 5." in f for f in fades)
    assert all("easing" not in f for f in fades if "from 2.00%" in f)
    assert any("easing to the terminal growth of" in f for f in fades)      # the base case still eases
    at.button(key="back_btn").click().run()                                 # the stories clause follows too
    assert_clean(at)
    assert any(c.value == "Revenue growth: Then moving up to 4.25% by year 10." for c in at.caption)


def test_a_stale_file_disables_every_action_including_commit(repo: Path):
    """Audit 4 blocker: a commit from a stale screen would record somebody else's edits as the owner's."""
    yaml_path = repo / "companies" / "EXMP" / "valuation" / "assumptions.yaml"
    at = run_app()
    go_to(at, "review")
    assert not at.button(key="commit_btn").disabled
    text = yaml_path.read_text(encoding="utf-8").replace("weight: 0.25\n    story: |\n      The custom-chip",
                                                          "weight: 0.25\n    story: |\n      REWRITTEN The custom-chip")
    yaml_path.write_text(text, encoding="utf-8")
    import os, time
    os.utime(yaml_path, (time.time() + 5, time.time() + 5))
    at.run()
    assert_clean(at)
    assert at.button(key="save_btn").disabled
    assert at.button(key="write_btn").disabled
    assert at.button(key="commit_btn").disabled
    captions = [c.value for c in at.caption]
    assert sum("Disabled: the file changed on disk" in c for c in captions) == 2
    assert any("Nothing to record from this session" in c for c in captions)
    assert not any("Will commit" in c for c in captions)


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
    go_to(at, "review")
    assert at.button(key="save_btn").disabled and at.button(key="write_btn").disabled
    assert at.button(key="commit_btn").disabled
    assert not any("Input" in t.value.columns for t in at.table)          # the file's edits are not listed as the owner's
    assert any("Disabled: the file changed on disk" in c.value for c in at.caption)
    at.button(key="restart_btn").click().run()
    assert_clean(at)
    assert at.session_state["page"] == 0 and not any("changed on disk" in w.value for w in at.warning)
    assert "REWRITTEN" in at.session_state["working"]["scenarios"]["bear"]["story"]


def test_working_notes_with_a_duplicate_column_pipe_table_render_without_a_traceback(repo: Path):
    yaml_path = repo / "companies" / "EXMP" / "valuation" / "assumptions.yaml"
    doc = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    doc["scenarios"]["base"]["sales_to_capital"]["detail"] = (
        "Historical ratios.\n\n| Year | Ratio | Ratio |\n|---|---|---|\n| FY2023 | 2.2 | 107 |\n| FY2024 | n/m |\n\n"
        "Year      Capex   D&A\nFY2023    206     305\nFY2024    336     300")
    yaml_path.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True), encoding="utf-8")
    at = run_app()
    go_to(at, "reinvestment")                                    # the page renders to the end: readout and buttons
    assert_clean(at)
    assert readout(at) and at.button(key="next_btn")
    tables = [t.value for t in at.table if "Ratio (2)" in list(t.value.columns)]
    assert tables and list(tables[0].columns) == ["Year", "Ratio", "Ratio (2)"]
    assert any("FY2023    206     305" in c.value for c in at.code)
    go_to(at, "results")
    assert not any("used as" in m.value for m in at.markdown)
    assert not any(m.value.count("Bull case") > 1 for m in at.markdown)     # never the case name twice


def test_live_case_comparison_and_reset_preserve_other_edits(repo: Path):
    at = run_app()
    go_to(at, 'revenue_growth')
    gen = at.session_state['gen']
    base = at.session_state['last_result'].scenarios['base'].per_share
    at.number_input(key=f'w{gen}:scenarios.base.revenue_growth.values.0').set_value(30).run()
    at.number_input(key=f'w{gen}:scenarios.bear.revenue_growth.values.0').set_value(15).run()
    at.selectbox(key='watch_case').select('base').run()
    assert_clean(at)
    assert float(at.metric[0].value) > base
    assert 'since load' in at.metric[0].delta
    at.button(key='reset:scenarios.base.revenue_growth.values').click().run()
    assert_clean(at)
    assert at.session_state['working']['scenarios']['base']['revenue_growth']['values'][0] == .20
    assert at.session_state['working']['scenarios']['bear']['revenue_growth']['values'][0] == .15
    assert float(at.metric[0].value) == pytest.approx(base, abs=.005)
    assert at.button(key='reset:scenarios.base.revenue_growth.values').disabled
    assert 'scenarios.base' not in ' '.join(m.value for m in at.markdown)


def test_quick_save_keeps_reason_and_source_and_rebases_comparison(repo: Path):
    path = repo / 'companies/EXMP/valuation/assumptions.yaml'
    initial = yaml.safe_load(path.read_text())
    at = run_app()
    go_to(at, 'reinvestment')
    gen = at.session_state['gen']
    at.number_input(key=f'w{gen}:scenarios.base.sales_to_capital.value').set_value(2.5).run()
    assert not at.button(key='quick_save').disabled
    at.text_input(key='quick_save_note:EXMP').input('Testing a more efficient business').run()
    at.button(key='quick_save').click().run()
    assert_clean(at)
    after = yaml.safe_load(path.read_text())
    assert after['scenarios']['base']['sales_to_capital']['value'] == 2.5
    for field in ('reason', 'source'):
        assert after['scenarios']['base']['sales_to_capital'][field] == initial['scenarios']['base']['sales_to_capital'][field]
    assert after['changelog'][-1]['note'] == 'Testing a more efficient business'
    assert at.session_state['page'] == PAGES.index('reinvestment')
    assert at.button(key='quick_save').disabled
    assert at.metric[0].delta == '+0.00 since load'
    assert (path.parent / 'assumptions.md').exists()


def test_quick_save_disabled_when_disk_changes_and_stopped_watch_is_explicit(repo: Path):
    path = repo / 'companies/EXMP/valuation/assumptions.yaml'
    at = run_app()
    go_to(at, 'reinvestment')
    at.selectbox(key='watch_case').select('bull').run()
    gen = at.session_state['gen']
    at.number_input(key=f'w{gen}:scenarios.bull.sales_to_capital.value_late').set_value(0).run()
    assert_clean(at)
    assert not any(m.label == 'Current value' for m in at.metric)
    assert any('Value unavailable' in m.value for m in at.markdown)
    assert any('See Model checks' in c.value for c in at.caption)
    path.write_text(path.read_text() + '\n# independent file edit\n')
    at.run()
    assert_clean(at)
    assert at.button(key='quick_save').disabled


def test_workspace_jumps_preserve_edits_watched_case_and_saved_files(repo: Path):
    """Exploring separate tools keeps the draft live without saving or resetting it."""
    vdir = repo / 'companies/EXMP/valuation'
    saved = {p.name: p.read_bytes() for p in vdir.iterdir()}
    at = run_app()
    go_to(at, 'revenue_growth')
    gen = at.session_state['gen']
    field = f'w{gen}:scenarios.bull.revenue_growth.values.0'
    at.number_input(key=field).set_value(35).run()
    at.selectbox(key='watch_case').select('bull').run()
    value = at.session_state['last_result'].scenarios['bull'].per_share

    for page in ('simulation', 'facts', 'analysis', 'forecast', 'results', 'checks', 'review', 'revenue_growth'):
        go_to(at, page)
        assert_clean(at)
        assert at.session_state['watch_case'] == 'bull'
        assert at.session_state['working']['scenarios']['bull']['revenue_growth']['values'][0] == .35
        current = next(m for m in at.metric if m.label == 'Current value')
        assert float(current.value.replace(',', '')) == pytest.approx(value, abs=.005)
        assert not at.sidebar.metric
        if page != 'review':
            assert not any(b.key in ('write_btn', 'commit_btn', 'restart_btn') for b in at.button)
        assert {p.name: p.read_bytes() for p in vdir.iterdir()} == saved

    assert at.number_input(key=field).value == 35


def test_roic_comparison_updates_from_both_inputs_while_history_stays_fixed(repo: Path):
    evidence = repo / 'companies' / 'EXMP' / 'sources'
    evidence.mkdir()
    (evidence / 'history.txt').write_text('Synthetic test evidence: profit 100, tax 20%, opening capital 500.')
    path = repo / 'companies' / 'EXMP' / 'valuation' / 'historical-roic.yaml'
    path.write_text(yaml.safe_dump(dict(schema=1, ticker='EXMP', as_of_date='2026-08-01',
        years=[dict(period='FY2025', operating_income=100, tax_rate=.2, invested_capital_start=500,
                    source='[Synthetic test annual]', source_paths=['sources/history.txt'])])))
    original = path.read_bytes()
    assumptions = (path.parent / 'assumptions.yaml').read_bytes()
    at = run_app()
    go_to(at, 'reinvestment')
    assert_clean(at)
    assert any('16.0%' in str(t.value) and 'Historical ROIC' in t.value.columns for t in at.table)
    gen = at.session_state['gen']
    at.number_input(key=f'w{gen}:scenarios.base.sales_to_capital.value').set_value(2).run()
    assert_clean(at)
    summaries = [t.value for t in at.table if 'Cost of capital' in t.value.columns and 'Ratio-implied ROIC' in t.value.columns]
    assert summaries[1]['Ratio-implied ROIC'].tolist() == ['33.1%', '47.8%']
    go_to(at, 'operating_margin')
    at.number_input(key=f'w{gen}:scenarios.base.operating_margin.values.0').set_value(30).run()
    assert_clean(at)
    summaries = [t.value for t in at.table if 'Cost of capital' in t.value.columns and 'Ratio-implied ROIC' in t.value.columns]
    assert summaries[1]['Ratio-implied ROIC'].tolist() == ['55.2%', '47.8%']
    assert any('16.0%' in str(t.value) and 'Historical ROIC' in t.value.columns for t in at.table)
    assert path.read_bytes() == original
    assert (path.parent / 'assumptions.yaml').read_bytes() == assumptions


def test_scenario_weights_sync_validate_and_save(repo: Path):
    """The stories editor and tax editor operate on one probability mix and guarded save path."""
    path = repo / "companies" / "EXMP" / "valuation" / "assumptions.yaml"
    before = yaml.safe_load(path.read_text())
    at = run_app()
    go_to(at, "stories")
    gen = at.session_state["gen"]
    assert [at.number_input(key=f"w{gen}:scenarios.{name}.weight").value
            for name in ("bear", "base", "bull")] == [25.0, 50.0, 25.0]
    at.number_input(key=f"w{gen}:scenarios.bear.weight").set_value(35.0).run()
    assert_clean(at)
    assert any("110.0%" in error.value and "100%" in error.value for error in at.error)
    at.number_input(key=f"w{gen}:scenarios.base.weight").set_value(40.0).run()
    assert_clean(at)
    result = at.session_state["last_result"]
    assert result.weighted.per_share == pytest.approx(sum(
        result.scenarios[name].per_share * weight
        for name, weight in (("bear", .35), ("base", .40), ("bull", .25))))
    go_to(at, "taxes_weights")
    assert at.number_input(key=f"w{gen}:scenarios.bear.weight").value == 35.0
    assert at.number_input(key=f"w{gen}:scenarios.base.weight").value == 40.0
    at.number_input(key=f"w{gen}:scenarios.bull.weight").set_value(30.0).run()
    at.number_input(key=f"w{gen}:scenarios.base.weight").set_value(35.0).run()
    go_to(at, "stories")
    assert [at.number_input(key=f"w{gen}:scenarios.{name}.weight").value
            for name in ("bear", "base", "bull")] == [35.0, 35.0, 30.0]
    assert yaml.safe_load(path.read_text()) == before
    go_to(at, "review")
    at.text_input(key="save_note:EXMP").input("Owner probability assessment").run()
    at.button(key="save_btn").click().run()
    assert_clean(at)
    saved = yaml.safe_load(path.read_text())
    assert [saved["scenarios"][name]["weight"] for name in ("bear", "base", "bull")] == [.35, .35, .30]
    assert {entry["path"] for entry in saved["changelog"]} == {
        "scenarios.bear.weight", "scenarios.base.weight", "scenarios.bull.weight"}
    assert all(entry["note"] == "Owner probability assessment" for entry in saved["changelog"])
    assert saved["scenarios"]["management"] == before["scenarios"]["management"]


def test_scenario_weight_default_reset_is_explicit_and_scoped(repo: Path):
    """Saved non-default weights survive load; default reset changes no unrelated inputs or disk files."""
    path = repo / "companies" / "EXMP" / "valuation" / "assumptions.yaml"
    doc = yaml.safe_load(path.read_text())
    for name, weight in (("bear", .1), ("base", .6), ("bull", .3)):
        doc["scenarios"][name]["weight"] = weight
    path.write_text(yaml.safe_dump(doc, sort_keys=False))
    original = path.read_bytes()
    at = run_app()
    go_to(at, "stories")
    gen = at.session_state["gen"]
    assert [at.number_input(key=f"w{gen}:scenarios.{name}.weight").value
            for name in ("bear", "base", "bull")] == [10.0, 60.0, 30.0]
    go_to(at, "revenue_growth")
    at.number_input(key=f"w{gen}:scenarios.base.revenue_growth.values.0").set_value(30.0).run()
    go_to(at, "stories")
    at.button(key="reset_scenario_weights").click().run()
    assert_clean(at)
    gen = at.session_state["gen"]
    assert [at.number_input(key=f"w{gen}:scenarios.{name}.weight").value
            for name in ("bear", "base", "bull")] == [25.0, 50.0, 25.0]
    assert at.session_state["working"]["scenarios"]["base"]["revenue_growth"]["values"][0] == .30
    assert at.button(key="reset_scenario_weights").disabled
    go_to(at, "taxes_weights")
    assert at.number_input(key=f"w{gen}:scenarios.base.weight").value == 50.0
    assert path.read_bytes() == original


def test_source_links_and_separate_readonly_source_view(repo: Path):
    cache = repo / "companies/EXMP/sources/FY2027-Q2"
    cache.mkdir(parents=True)
    (cache / "10-Q-FY2027-Q2.txt").write_text("EXMP QUARTERLY FILING\nRevenue table\n")
    (cache / "MANIFEST.md").write_text("10-Q-FY2027-Q2.txt | https://www.sec.gov/Archives/example/quarterly.htm | fetched\n")
    assumptions = repo / "companies/EXMP/valuation/assumptions.yaml"
    before = assumptions.read_bytes()
    at = run_app()
    go_to(at, "facts")
    shown = " ".join(str(cell) for t in at.table for cell in t.value.to_numpy().flat)
    assert "](?company=EXMP&source=" in shown
    source = AppTest.from_file(str(APP), default_timeout=120)
    source.query_params["company"] = "EXMP"
    source.query_params["source"] = "companies/EXMP/sources/FY2027-Q2/10-Q-FY2027-Q2.txt"
    source.run()
    assert_clean(source)
    assert source.header[0].value == "10-Q Q2 FY2027"
    assert "EXMP QUARTERLY FILING" in source.code[0].value
    assert "without an exact passage" in source.info[0].value
    source.query_params["quote"] = "Revenue table"
    source.run()
    assert_clean(source)
    assert any("Revenue table</mark>" in m.value for m in source.markdown)
    assert not source.number_input
    assert assumptions.read_bytes() == before
    source.query_params["source"] = "AGENTS.md"
    source.run()
    assert_clean(source)
    assert "not available" in source.error[0].value
    assert not source.code
