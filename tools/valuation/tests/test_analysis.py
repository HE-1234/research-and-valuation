"""Reverse DCF round trips, sensitivity grids, diagnostics."""

from __future__ import annotations

import math
from pathlib import Path

from valuation import compute
from valuation.analysis import (
    average_growth, fcff_change, reverse_dcf, run_analysis, sensitivity_growth_margin, sensitivity_wacc_growth,
    transition_flag,
)
from valuation.engine import MarketInputs, run_scenario
from valuation.schema import load_yaml
from valuation.tests.test_engine import base_year, bridge, hand_inputs

FIXTURE = Path(__file__).resolve().parent / "fixtures" / "example_assumptions.yaml"
MARKET = MarketInputs(price=70.0, risk_free_rate=0.0425, equity_risk_premium=0.042)


def test_reverse_dcf_round_trip_on_constant_growth_case():
    inp, by, br = hand_inputs(), base_year(), bridge()
    res = run_scenario(inp, by, br, price=200.0)
    rev = reverse_dcf(inp, by, br, price=200.0, target_ev=res.operating_assets)
    assert rev.implied_growth is not None and math.isclose(rev.implied_growth, 0.10, abs_tol=1e-6)
    assert rev.implied_year5_margin is not None and math.isclose(rev.implied_year5_margin, 0.20, abs_tol=1e-6)
    assert math.isclose(rev.base_average_growth, 0.10, abs_tol=1e-9)


def test_reverse_dcf_uses_enterprise_value_by_default():
    inp, by, br = hand_inputs(), base_year(), bridge()
    rev = reverse_dcf(inp, by, br, price=200.0)
    assert math.isclose(rev.target_enterprise_value, 200.0 * 10 + 200 - 100)
    # EV 2,100 is below operating assets 2,313, so the implied growth must be below 10%.
    assert rev.implied_growth is not None and rev.implied_growth < 0.10
    check = run_scenario(inp.__class__(**{**inp.__dict__, "growth": [rev.implied_growth] * 5}), by, br, 200.0)
    assert math.isclose(check.operating_assets, rev.target_enterprise_value, rel_tol=1e-6)


def test_reverse_dcf_reports_when_no_solution():
    inp, by, br = hand_inputs(), base_year(), bridge()
    rev = reverse_dcf(inp, by, br, price=200.0, target_ev=1e12)
    assert rev.implied_growth is None and "upper bound" in rev.implied_growth_note


def test_sensitivity_grids_contain_base_cell():
    inp, by, br = hand_inputs(), base_year(), bridge()
    base_value = run_scenario(inp, by, br, price=200.0).per_share
    g1 = sensitivity_wacc_growth(inp, by, br, price=200.0)
    g2 = sensitivity_growth_margin(inp, by, br, price=200.0)
    for grid in (g1, g2):
        assert len(grid.cells) == 5 and all(len(r) == 5 for r in grid.cells)
        assert math.isclose(grid.cells[grid.base_row][grid.base_col], base_value, rel_tol=1e-12)
    assert math.isclose(g1.row_values[g1.base_row], 0.10) and math.isclose(g1.col_values[g1.base_col], 0.04)
    assert math.isclose(g2.row_values[g2.base_row], 0.10) and math.isclose(g2.col_values[g2.base_col], 0.20)
    # Higher cost of capital lowers value; higher terminal growth raises it.
    assert g1.cells[0][2] > base_value > g1.cells[4][2]
    assert g1.cells[2][4] > base_value > g1.cells[2][0]
    # Higher growth and higher margin raise value.
    assert g2.cells[4][2] > base_value > g2.cells[0][2]
    assert g2.cells[2][4] > base_value > g2.cells[2][0]


def test_average_growth_is_cagr():
    inp, by, br = hand_inputs(growth=[0.2, 0.1, 0.0, 0.1, 0.1]), base_year(), bridge()
    res = run_scenario(inp, by, br, 200.0)
    expected = (1.2 * 1.1 * 1.0 * 1.1 * 1.1) ** 0.2 - 1
    assert math.isclose(average_growth(res), expected, rel_tol=1e-12)


def test_run_analysis_on_example_has_seven_diagnostics_with_dataset_dates():
    result = compute(load_yaml(FIXTURE), MARKET)
    analysis = result.analysis or run_analysis(result)
    assert analysis.scenario == "base"
    assert len(analysis.diagnostics) == 7                      # Damodaran's six plus the transition check
    assert analysis.industry is not None
    beta = analysis.industry.unlevered_beta_cash_corrected
    assert beta.value is not None and beta.matched_name == "Semiconductor" and beta.dataset_date
    text = " ".join(v for d in analysis.diagnostics for _, v in d.rows)
    assert "histgr dataset" in text and "margin dataset" in text
    assert analysis.reverse is not None and analysis.reverse.implied_growth is not None
    # Year-T revenue 8,000 * 1.2^5 = 19,906 against a 60,000 market: no flag.
    assert analysis.diagnostics[1].flag is False
    # Diagnostic 1 says history is context when the path is more than five points off it (rule 11):
    # the base case averages 20% against the recorded 14%.
    assert "context, not an anchor" in (analysis.diagnostics[0].note or "")


def test_transition_check_flags_a_cliff_and_leaves_a_smooth_case_alone():
    """A small terminal-year notch is normal (his own sheets have one); a cliff is not (section 18.2)."""
    by, br = base_year(), bridge()
    # The hand-worked case is a cliff: year-5 cash flow 225.47 against a terminal 139.58, 38% down.
    cliff = run_scenario(hand_inputs(), by, br, 200.0)
    assert fcff_change(cliff.rows[-1].fcff, cliff.terminal.fcff) < -0.15
    assert transition_flag(cliff.rows[-1].fcff, cliff.terminal.fcff, cliff.rows[-1].roic, cliff.terminal.roic)
    # Terminal growth of zero means no terminal reinvestment, so only the tax step remains: 6% down, no flag.
    smooth = run_scenario(hand_inputs(terminal_growth=0.0), by, br, 200.0)
    assert -0.15 < fcff_change(smooth.rows[-1].fcff, smooth.terminal.fcff) < 0
    assert not transition_flag(smooth.rows[-1].fcff, smooth.terminal.fcff, smooth.rows[-1].roic, smooth.terminal.roic)
    # A 10% notch, like his Alphabet February 2024 sheet, is inside the tolerance...
    assert not transition_flag(100.0, 89.0, 0.20, 0.15)
    # ... a 20% one is not, and neither is a terminal return below half the last year's.
    assert transition_flag(100.0, 79.0, 0.20, 0.15)
    assert transition_flag(100.0, 100.0, 0.30, 0.14)
    assert not transition_flag(100.0, 100.0, 0.30, 0.16)


def test_transition_check_diagnostic_reports_the_change_and_warns_when_flagged():
    result = compute(load_yaml(FIXTURE), MARKET)
    diag = result.analysis.diagnostics[-1]
    assert diag.title.startswith("7. The step from the last explicit year")
    assert diag.flag is True
    text = " ".join(v for _k, v in diag.rows)
    assert "a change of -" in text and "to terminal year" in text
    assert "return on capital" in " ".join(k for k, _v in diag.rows)
    assert "A small drop is normal" in (diag.note or "")
    # audit 4: no bare "g", capitalised case names, one spelling of the marker
    assert "reinvests growth divided by the return on capital" in (diag.note or "")
    assert all(k.startswith(("Bear case", "Base case", "Bull case", "Management case")) for k, _v in diag.rows)
    assert "(flag)" not in text.replace("(flagged)", "")
    assert any("is more than 15% below the year-5 free cash flow" in w for w in result.warnings)


def test_the_bear_case_uses_the_same_transition_checks_as_every_case():
    """A zero bear premium does not excuse a large terminal transition."""
    result = compute(load_yaml(FIXTURE), MARKET)
    rows = dict(result.analysis.diagnostics[-1].rows)
    bear = rows["Bear case, free cash flow (USD millions)"]
    # The fixture's zero-premium bear falls 42%, well past the review threshold.
    assert "a change of -42.4%" in bear
    assert bear.endswith("(flagged)")
    assert "expected" not in bear
    assert "(flagged)" in rows["Base case, free cash flow (USD millions)"]
    assert any(w.startswith("bear: the terminal year's free cash flow") for w in result.warnings)
    assert any(w.startswith("base: the terminal year's free cash flow") for w in result.warnings)
    assert "The same checks apply to every case" in (result.analysis.diagnostics[-1].note or "")
    # A file whose only cliff is the bear's must still flag the diagnostic.
    doc = load_yaml(FIXTURE)
    for name, premium in {"base": 0.03, "bull": 0.10, "management": 0.05}.items():
        sc = doc["scenarios"][name]
        sc["terminal"]["growth"] = {"value": 0.0, "reason": "no growth forever"}
        sc["terminal"]["roic_premium"] = {"value": premium, "allow_large_premium": False, "reason": "test"}
        sc["tax_rate"]["terminal"] = sc["tax_rate"]["start"]
    only_bear = compute(doc, MARKET)
    bear_row = dict(only_bear.analysis.diagnostics[-1].rows)["Bear case, free cash flow (USD millions)"]
    assert "a change of -" in bear_row
    assert only_bear.analysis.diagnostics[-1].flag is True
    assert any(w.startswith("bear: the terminal year's free cash flow") for w in only_bear.warnings)


def test_smooth_bear_and_other_transitions_do_not_flag():
    # a file whose terminal settings agree with its last year neither flags nor warns: no terminal growth
    # (so no terminal reinvestment and no revenue step), the same tax rate, and a premium that keeps the
    # terminal return above half the year-5 implied return
    doc = load_yaml(FIXTURE)
    premiums = {"bear": 0.03, "base": 0.03, "bull": 0.10, "management": 0.05}
    for name, premium in premiums.items():
        s = doc["scenarios"][name]
        s["terminal"]["growth"] = {"value": 0.0, "reason": "no growth forever"}
        s["terminal"]["roic_premium"] = {"value": premium, "allow_large_premium": False, "reason": "test"}
        s["tax_rate"]["terminal"] = s["tax_rate"]["start"]
    quiet = compute(doc, MARKET)
    assert quiet.analysis.diagnostics[-1].flag is False
    assert not any("free cash flow" in w for w in quiet.warnings)


def test_roic_only_transition_warning_does_not_claim_cash_flow_fell():
    doc = load_yaml(FIXTURE)
    doc["base_year"]["invested_capital"]["value"] = 500
    bear = doc["scenarios"]["bear"]
    bear["terminal"]["growth"]["value"] = 0.0
    bear["tax_rate"]["terminal"] = bear["tax_rate"]["start"]
    result = compute(doc, MARKET)
    case = result.scenarios["bear"]
    assert case.terminal.fcff >= case.rows[-1].fcff
    warning = next(w for w in result.warnings if w.startswith("bear: terminal return on capital ("))
    assert "below half" in warning
    assert "free cash flow" not in warning
