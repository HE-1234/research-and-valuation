"""Reproduce Damodaran's AlphabetApr2018.xlsx and NVIDIA2023.xlsx with the engine in 10-year mode.

Inputs and outputs live in ``fixtures/damodaran_workbooks.json`` (extracted by
``damodaran_extract.py``); when the workbooks are present in ``/tmp/damo`` the fixture is
re-checked against them.  Both values of operating assets and per-share values must match
his sheets within 0.1%.

Convention differences found by reading his formulas cell by cell:

* **Alphabet 2018 has no reinvestment lag.**  Row 8 of his Valuation output is
  ``(Rev_t - Rev_{t-1}) / SC``; ginzu and AGENTS.md section 18.3 use a one-year lag
  ``(Rev_{t+1} - Rev_t) / SC``.  The engine's ``reinvestment_lag`` switch (default 1)
  reproduces the 2018 sheet with ``0``; the test also reports how much the section 18.3
  convention changes his value.
* **Alphabet 2018 taxes trapped cash.**  Cell B27 uses ``cash - trapped * (marginal - foreign)``
  = 101,871 - 60,000 * 0.10 = 95,871; the engine's bridge takes that adjusted cash.
* **NVIDIA 2023 is three segments (rest, AI chips, auto chips).**  Every segment shares the
  same tax path, cost of capital path, sales-to-capital and terminal settings, and every
  formula is linear in revenue and operating income, so the sum of his three segment
  valuations equals one valuation on the aggregated revenue and operating-income paths.
  The test rebuilds his segment paths from the Input sheet (market size, share, margin
  convergence) and feeds the aggregate growth and margin lists to the engine.
* **ROIC display.**  Alphabet 2018 divides by end-of-year capital (row 40 uses ``C7/C39``);
  ginzu and the engine divide by start-of-year capital.  This never affects value.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

from valuation.engine import BaseYear, Bridge, ScenarioInputs, rnd_capitalization, run_scenario
from valuation.tests import damodaran_extract as dx

FIXTURE = Path(__file__).resolve().parent / "fixtures" / "damodaran_workbooks.json"
TOL = 0.001            # 0.1%


@pytest.fixture(scope="module")
def data() -> dict:
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


def _close(a: float, b: float, rel: float = TOL) -> bool:
    return math.isclose(a, b, rel_tol=rel, abs_tol=1e-9)


def _base_year(revenue: float, ebit: float, tax: float, invested_capital: float) -> BaseYear:
    return BaseYear(
        revenue=revenue, operating_income_gaap=ebit, one_time_items=0.0, amortization_memo=0.0,
        amortization_addback=0.0, stock_based_compensation_memo=0.0, rnd_expense_memo=0.0,
        rnd_adjustment=0.0, rnd_asset=0.0, rnd_amortization=0.0, adjusted_operating_income=ebit,
        margin=ebit / revenue, effective_tax_rate=tax, invested_capital_reported=invested_capital,
        invested_capital=invested_capital, roic=ebit * (1 - tax) / invested_capital,
    )


def damodaran_fade(g5: float, g_terminal: float) -> list[float]:
    """Rows H2:L2 of his sheet: growth moves from year-5 growth to terminal growth in five steps."""
    return [g5 - (g5 - g_terminal) * k / 5 for k in range(1, 6)]


def damodaran_margin_path(anchor: float, target: float, convergence_year: int, years: int = 10,
                          year1: float | None = None) -> list[float]:
    """Row 4: ``target - (target - anchor) / N * (N - t)`` until year N, then the target.

    Alphabet 2018 anchors on the base-year margin and applies the formula from year 1.  The
    ginzu-style NVIDIA sheet takes year 1 straight from the input cell and applies the formula
    from year 2 with that year-1 margin as the anchor (so the path steps twice between years 1
    and 2); pass ``year1`` for that behaviour.
    """
    path = [target if t > convergence_year else target - (target - anchor) / convergence_year * (convergence_year - t)
            for t in range(1, years + 1)]
    if year1 is not None:
        path[0] = year1
    return path


# --------------------------------------------------------------------------- #
# Alphabet, April 2018
# --------------------------------------------------------------------------- #

def alphabet_inputs(fx: dict, lag: int) -> tuple[ScenarioInputs, BaseYear, Bridge]:
    i = fx["inputs"]
    growth = [i["year1_growth"]] + [i["cagr_years_2_5"]] * 4
    growth += damodaran_fade(growth[4], i["terminal_growth"])
    margin = damodaran_margin_path(i["base_margin"], i["target_margin"], int(i["convergence_year"]))
    inp = ScenarioInputs(
        name="alphabet", horizon=10, growth=growth, margin=margin,
        sales_to_capital=i["sales_to_capital_1_5"], sales_to_capital_late=i["sales_to_capital_6_10"],
        reinvestment_override=[None] * 10, tax_start=i["effective_tax"], tax_terminal=i["stable_tax"],
        wacc=i["initial_wacc"], terminal_wacc=i["stable_wacc"], terminal_growth=i["terminal_growth"],
        roic_premium=i["stable_roic"] - i["stable_wacc"], reinvestment_lag=lag,
    )
    base = _base_year(i["revenue"], i["ebit_adjusted"], i["effective_tax"], i["invested_capital"])
    bridge = Bridge(cash=i["cash_used"], debt=i["book_debt"], leases=i["lease_debt"],
                    minority_interests=i["minority_interests"], non_operating_assets=i["cross_holdings"],
                    other_claims=i["option_value"], probability_of_failure=i["failure_probability"],
                    distress_proceeds=0.0, diluted_shares=i["shares"])
    return inp, base, bridge


def test_alphabet_paths_match_his_sheet(data):
    fx = data["alphabet_2018"]
    inp, _, _ = alphabet_inputs(fx, lag=0)
    for mine, his in zip(inp.growth, fx["paths"]["growth"]):
        assert _close(mine, his, 1e-9)
    for mine, his in zip(inp.margin, fx["paths"]["margin"]):
        assert _close(mine, his, 1e-9)


def test_alphabet_rnd_converter_and_invested_capital(data):
    i = data["alphabet_2018"]["inputs"]
    adj, asset, _ = rnd_capitalization(i["rnd_current"], i["rnd_history_oldest_first"], int(i["rnd_amortization_years"]))
    assert _close(adj, i["rnd_adjustment_to_ebit"], 1e-9)
    assert _close(asset, i["rnd_asset"], 1e-9)
    assert _close(i["ebit_reported"] + i["lease_adjustment_to_ebit"] + adj, i["ebit_adjusted"], 1e-9)
    ic = i["book_equity"] + i["book_debt"] - i["cash_reported"] + i["lease_debt"] + asset
    assert _close(ic, i["invested_capital"], 1e-9)
    assert _close(i["cash_reported"] - i["trapped_cash"] * (i["marginal_tax"] - i["trapped_cash_tax"]), i["cash_used"], 1e-9)


def test_alphabet_reproduces_his_values(data):
    fx = data["alphabet_2018"]
    inp, base, bridge = alphabet_inputs(fx, lag=int(fx["inputs"]["reinvestment_lag"]))
    res = run_scenario(inp, base, bridge, fx["inputs"]["price"])
    his = fx["outputs"]
    for mine, theirs in zip([r.reinvestment for r in res.rows], fx["paths"]["reinvestment"]):
        assert _close(mine, theirs, 1e-9)
    assert _close(res.sum_pv_fcff, his["pv_fcff_10y"])
    assert _close(res.terminal.value, his["terminal_value"])
    assert _close(res.operating_assets, his["operating_assets"])
    assert _close(res.equity, his["equity"])
    assert _close(res.per_share, his["per_share"])


def test_alphabet_section_18_3_lag_convention_difference(data):
    """Known difference: with the one-year lag of section 18.3 his 2018 value moves by a small, stable amount."""
    fx = data["alphabet_2018"]
    inp0, base, bridge = alphabet_inputs(fx, lag=0)
    inp1, _, _ = alphabet_inputs(fx, lag=1)
    v0 = run_scenario(inp0, base, bridge, fx["inputs"]["price"]).per_share
    v1 = run_scenario(inp1, base, bridge, fx["inputs"]["price"]).per_share
    diff = v1 / v0 - 1.0
    # Growth fades after year 5, so the lagged reinvestment is smaller in every year: value goes up,
    # by roughly one percent (recorded in README).
    assert 0.0 < diff < 0.03, diff


# --------------------------------------------------------------------------- #
# NVIDIA, June 2023 (three segments aggregated)
# --------------------------------------------------------------------------- #

def _market_path(now: float, year10: float, mid_fraction: float) -> list[float]:
    """His market-size rows: year 5 = now + mid_fraction*(year10-now); linear in between."""
    g5 = now + mid_fraction * (year10 - now)
    early = [now + (g5 - now) * t / 5 for t in range(1, 6)]
    late = [g5 + (year10 - g5) * k / 5 for k in range(1, 6)]
    return early + late


def _share_path(now: float, year10: float) -> list[float]:
    return [now - (now - year10) * t / 10 for t in range(1, 11)]


def nvidia_paths(fx: dict) -> tuple[list[float], list[float]]:
    """Rebuild his three segment revenue and EBIT rows from the Input sheet and aggregate them."""
    i = fx["inputs"]
    seg = i["segments"]
    n = int(i["convergence_year"])
    rest_growth = [i["year1_growth"]] + [i["cagr_years_2_5"]] * 4
    rest_growth += damodaran_fade(rest_growth[4], i["terminal_growth"])
    rest_rev, rev = [], seg["rest"]["revenue_base"]
    for g in rest_growth:
        rev *= 1 + g
        rest_rev.append(rev)
    rest_margin = damodaran_margin_path(i["year1_margin"], i["target_margin"], n, year1=i["year1_margin"])
    ai = seg["ai"]
    ai_rev = [m * s for m, s in zip(_market_path(ai["market_now"], ai["market_year10"], 2 / 5),
                                     _share_path(ai["share_now"], ai["share_year10"]))]
    ai_margin = damodaran_margin_path(ai["margin_now"], ai["margin_target"], n, year1=ai["margin_now"])
    auto = seg["auto"]
    auto_rev = [m * s for m, s in zip(_market_path(auto["market_now"], auto["market_year10"], 2 / 3),
                                       _share_path(auto["share_now"], auto["share_year10"]))]
    auto_margin = damodaran_margin_path(auto["margin_now"], auto["margin_target"], n, year1=auto["margin_now"])
    for mine, his in ((rest_rev, fx["paths"]["revenue_rest"]), (ai_rev, fx["paths"]["revenue_ai"]),
                      (auto_rev, fx["paths"]["revenue_auto"])):
        for a, b in zip(mine, his):
            assert _close(a, b, 1e-9), (a, b)
    total_rev = [a + b + c for a, b, c in zip(rest_rev, ai_rev, auto_rev)]
    total_ebit = [a * ma + b * mb + c * mc for a, b, c, ma, mb, mc in
                  zip(rest_rev, ai_rev, auto_rev, rest_margin, ai_margin, auto_margin)]
    for mine, his in zip(total_ebit, [x + y + z for x, y, z in zip(fx["paths"]["ebit_rest"], fx["paths"]["ebit_ai"],
                                                                   fx["paths"]["ebit_auto"])]):
        assert _close(mine, his, 1e-9)
    prev = i["revenue"]
    growth = []
    for r in total_rev:
        growth.append(r / prev - 1)
        prev = r
    margin = [e / r for e, r in zip(total_ebit, total_rev)]
    return growth, margin


def test_nvidia_rnd_converter(data):
    i = data["nvidia_2023"]["inputs"]
    adj, asset, _ = rnd_capitalization(i["rnd_current"], i["rnd_history_oldest_first"], int(i["rnd_amortization_years"]))
    assert _close(adj, i["rnd_adjustment_to_ebit"], 1e-9)
    assert _close(asset, i["rnd_asset"], 1e-9)
    assert _close(i["ebit_reported"] + adj, i["ebit_adjusted"], 1e-9)
    assert _close(i["book_equity"] + i["book_debt"] - i["cash_used"] + asset, i["invested_capital"], 1e-9)
    assert _close(i["risk_free"] + i["mature_market_erp"], i["stable_wacc"], 1e-9)


def test_nvidia_reproduces_his_values(data):
    fx = data["nvidia_2023"]
    i = fx["inputs"]
    growth, margin = nvidia_paths(fx)
    inp = ScenarioInputs(
        name="nvidia", horizon=10, growth=growth, margin=margin,
        sales_to_capital=i["sales_to_capital_1_5"], sales_to_capital_late=i["sales_to_capital_6_10"],
        reinvestment_override=[None] * 10, tax_start=i["effective_tax"], tax_terminal=i["stable_tax"],
        wacc=i["initial_wacc"], terminal_wacc=i["stable_wacc"], terminal_growth=i["terminal_growth"],
        roic_premium=i["stable_roic"] - i["stable_wacc"], reinvestment_lag=int(i["reinvestment_lag"]),
    )
    base = _base_year(i["revenue"], i["ebit_adjusted"], i["effective_tax"], i["invested_capital"])
    bridge = Bridge(cash=i["cash_used"], debt=i["debt_used"], leases=0.0, minority_interests=i["minority_interests"],
                    non_operating_assets=i["cross_holdings"], other_claims=i["option_value"],
                    probability_of_failure=i["failure_probability"], distress_proceeds=0.0, diluted_shares=i["shares"])
    res = run_scenario(inp, base, bridge, i["price"])
    his = fx["outputs"]
    for mine, theirs in zip([r.tax_rate for r in res.rows], fx["paths"]["tax"]):
        assert _close(mine, theirs, 1e-9)
    for mine, theirs in zip([r.wacc for r in res.rows], fx["paths"]["wacc"]):
        assert _close(mine, theirs, 1e-9)
    assert _close(his["value_rest"] + his["value_ai"] + his["value_auto"], his["operating_assets"], 1e-9)
    assert _close(res.operating_assets, his["operating_assets"])
    assert _close(res.equity, his["equity"])
    assert _close(res.per_share, his["per_share"])


# --------------------------------------------------------------------------- #
# The fixture matches the workbooks when they are available
# --------------------------------------------------------------------------- #

@pytest.mark.skipif(not (dx.WORKBOOK_DIR / "AlphabetApr2018.xlsx").exists()
                    or not (dx.WORKBOOK_DIR / "NVIDIA2023.xlsx").exists(),
                    reason="Damodaran workbooks not present in /tmp/damo")
def test_fixture_matches_workbooks(data):
    fresh = dx.extract_all()

    def walk(a, b, path=""):
        if isinstance(a, dict):
            assert set(a) == set(b), path
            for k in a:
                walk(a[k], b[k], f"{path}.{k}")
        elif isinstance(a, list):
            assert len(a) == len(b), path
            for k, (x, y) in enumerate(zip(a, b)):
                walk(x, y, f"{path}[{k}]")
        elif isinstance(a, (int, float)) and not isinstance(a, bool):
            assert _close(float(a), float(b), 1e-12), path
        else:
            assert a == b, path

    walk(fresh, data)
