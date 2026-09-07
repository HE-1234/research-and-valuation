"""Reverse DCF round trips, sensitivity grids, diagnostics."""

from __future__ import annotations

import math
from pathlib import Path

from valuation import compute
from valuation.analysis import (
    average_growth, reverse_dcf, run_analysis, sensitivity_growth_margin, sensitivity_wacc_growth,
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


def test_run_analysis_on_example_has_six_diagnostics_with_dataset_dates():
    result = compute(load_yaml(FIXTURE), MARKET)
    analysis = result.analysis or run_analysis(result)
    assert analysis.scenario == "base"
    assert len(analysis.diagnostics) == 6
    assert analysis.industry is not None
    beta = analysis.industry.unlevered_beta_cash_corrected
    assert beta.value is not None and beta.matched_name == "Semiconductor" and beta.dataset_date
    text = " ".join(v for d in analysis.diagnostics for _, v in d.rows)
    assert "histgr dataset" in text and "margin dataset" in text
    assert analysis.reverse is not None and analysis.reverse.implied_growth is not None
    # Year-T revenue 8,000 * 1.2^5 = 19,906 against a 60,000 market: no flag.
    assert analysis.diagnostics[1].flag is False
