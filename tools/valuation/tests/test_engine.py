"""Hand-worked checks of AGENTS.md section 18.3.

The main case is chosen so every number can be verified with a pencil:

    Rev_0 = 1,000; growth 10% for five years; margin 20%; tax 20% (terminal 25%);
    sales-to-capital 2.0; cost of capital 10% (terminal 9%); terminal growth 4%; premium 0.

    Year  Revenue   EBIT    EBIT(1-t)  Rev_{t+1}  Reinv = dRev/2  FCFF      DF          PV
    1     1,100.0   220.0   176.0      1,210.0    55.0            121.0     1/1.1       110.0
    2     1,210.0   242.0   193.6      1,331.0    60.5            133.1     1/1.1^2     110.0
    3     1,331.0   266.2   212.96     1,464.1    66.55           146.41    1/1.1^3     110.0
    4     1,464.1   292.82  234.256    1,610.51   73.205          161.051   1/1.1^4     110.0
    5     1,610.51  322.102 257.6816   1,674.9304 32.2102         225.4714  1/1.1^5     140.0
    (year 5 reinvestment is sized for terminal growth: 1,610.51 * 4% / 2 = 32.2102;
     257.6816 / 1.61051 = 160 and 32.2102 / 1.61051 = 20, so PV_5 = 140 exactly)

    Sum of PV = 4 * 110 + 140 = 580
    Terminal: EBIT_6 = 1,674.9304 * 20% = 334.98608; after 25% tax = 251.23956;
              ROIC = 9% + 0 = 9%; reinvestment rate = 4% / 9% = 4/9;
              FCFF_6 = 251.23956 * 5/9 = 139.577533; TV = 139.577533 / (9% - 4%) = 2,791.55067;
              PV(TV) = 2,791.55067 / 1.61051 = 1,733.3333
    Operating assets = 580 + 1,733.3333 = 2,313.3333
    Equity = 2,313.3333 + cash 100 - debt 200 = 2,213.3333; per share (10 shares) = 221.3333
"""

from __future__ import annotations

import copy
import math
from dataclasses import replace

import pytest

from valuation.engine import (
    BaseYear, Bridge, EngineError, MarketInputs, ScenarioInputs, build_base_year, build_cost_of_capital,
    compute, fade_years, reference_inputs, rnd_capitalization, run_scenario, sales_to_capital_path,
    scenario_inputs, stop_years, tax_path, wacc_path,
)
from valuation.schema import load_yaml
from pathlib import Path

FIXTURE = Path(__file__).resolve().parent / "fixtures" / "example_assumptions.yaml"


def close(a, b, rel=1e-9, abs_=1e-9):
    return math.isclose(a, b, rel_tol=rel, abs_tol=abs_)


def base_year(revenue=1000.0, ebit=200.0, tax=0.20, ic=2000.0) -> BaseYear:
    return BaseYear(revenue=revenue, operating_income_gaap=ebit, one_time_items=0.0, amortization_memo=0.0,
                    amortization_addback=0.0, stock_based_compensation_memo=0.0, rnd_expense_memo=0.0,
                    rnd_adjustment=0.0, rnd_asset=0.0, rnd_amortization=0.0, adjusted_operating_income=ebit,
                    margin=ebit / revenue, effective_tax_rate=tax, invested_capital_reported=ic,
                    invested_capital=ic, roic=ebit * (1 - tax) / ic)


def bridge(**kw) -> Bridge:
    args = dict(cash=100.0, debt=200.0, leases=0.0, minority_interests=0.0, non_operating_assets=0.0,
                other_claims=0.0, probability_of_failure=0.0, distress_proceeds=0.0, diluted_shares=10.0)
    args.update(kw)
    return Bridge(**args)


def hand_inputs(**kw) -> ScenarioInputs:
    args = dict(name="hand", horizon=5, growth=[0.10] * 5, margin=[0.20] * 5, sales_to_capital=2.0,
                sales_to_capital_late=2.0, reinvestment_override=[None] * 5, tax_start=0.20, tax_terminal=0.25,
                wacc=0.10, terminal_wacc=0.09, terminal_growth=0.04, roic_premium=0.0)
    args.update(kw)
    return ScenarioInputs(**args)


# --------------------------------------------------------------------------- #

def test_hand_worked_five_year_case():
    res = run_scenario(hand_inputs(), base_year(), bridge(), price=200.0)
    pvs = [r.pv for r in res.rows]
    assert all(close(pv, 110.0) for pv in pvs[:4])
    assert close(pvs[4], 140.0)
    assert close(res.rows[4].reinvestment, 32.2102)
    assert close(res.rows[4].fcff, 225.4714)
    assert close(res.sum_pv_fcff, 580.0)
    t = res.terminal
    assert close(t.revenue, 1674.9304)
    assert close(t.ebit_after_tax, 251.23956)
    assert close(t.reinvestment_rate, 4.0 / 9.0)
    assert close(t.fcff, 251.23956 * 5.0 / 9.0)
    assert close(t.value, 251.23956 * 5.0 / 9.0 / 0.05)
    assert close(t.pv, t.value / 1.1 ** 5)
    assert close(res.operating_assets, 580.0 + 2791.5506666667 / 1.61051, rel=1e-7)
    assert close(res.equity, res.operating_assets - 100.0)
    assert close(res.per_share, res.equity / 10.0)
    assert close(res.enterprise_value, 200.0 * 10 + 200.0 - 100.0)
    assert close(res.terminal_share, t.pv / res.operating_assets)
    # cumulative discount factors
    for k, r in enumerate(res.rows, start=1):
        assert close(r.discount_factor, 1.0 / 1.1 ** k)
    # implied ROIC uses start-of-year capital rolled forward with reinvestment
    assert close(res.rows[0].roic, 176.0 / 2000.0)
    assert close(res.rows[0].invested_capital_end, 2055.0)
    assert close(res.rows[1].roic, 193.6 / 2055.0)


def test_reinvestment_lag_and_override():
    res1 = run_scenario(hand_inputs(), base_year(), bridge(), 200.0)
    res0 = run_scenario(hand_inputs(reinvestment_lag=0), base_year(), bridge(), 200.0)
    assert close(res1.rows[0].reinvestment, 55.0)         # (1,210 - 1,100) / 2 with the lag
    assert close(res0.rows[0].reinvestment, 50.0)         # (1,100 - 1,000) / 2 without it
    over = run_scenario(hand_inputs(reinvestment_override=[100.0, None, None, None, None]), base_year(), bridge(), 200.0)
    assert over.rows[0].reinvestment_source == "override"
    assert close(over.rows[0].fcff, 76.0)
    assert close(over.operating_assets, res1.operating_assets - (110.0 - 76.0 / 1.1))
    assert over.rows[1].reinvestment_source == "sales_to_capital"


def test_terminal_formulas():
    # No terminal reinvestment when terminal growth is zero or negative (ginzu M8).
    zero = run_scenario(hand_inputs(terminal_growth=0.0), base_year(), bridge(), 200.0)
    assert zero.terminal.reinvestment == 0.0
    assert close(zero.terminal.value, zero.terminal.ebit_after_tax / 0.09)
    neg = run_scenario(hand_inputs(terminal_growth=-0.02), base_year(), bridge(), 200.0)
    assert neg.terminal.reinvestment == 0.0
    assert close(neg.terminal.revenue, 1610.51 * 0.98)
    # Terminal ROIC = terminal WACC + premium; reinvestment rate = g / ROIC.
    prem = run_scenario(hand_inputs(roic_premium=0.03), base_year(), bridge(), 200.0)
    assert close(prem.terminal.roic, 0.12)
    assert close(prem.terminal.reinvestment_rate, 0.04 / 0.12)
    # Terminal cost of capital must exceed terminal growth.
    with pytest.raises(EngineError):
        run_scenario(hand_inputs(terminal_growth=0.09), base_year(), bridge(), 200.0)
    # Losses carry no tax benefit in the explicit years (ginzu row 7).
    loss = run_scenario(hand_inputs(margin=[-0.1] * 5), base_year(), bridge(), 200.0)
    assert close(loss.rows[0].ebit_after_tax, -110.0)


def test_failure_probability_and_bridge():
    res = run_scenario(hand_inputs(), base_year(), bridge(probability_of_failure=0.1, distress_proceeds=1000.0), 200.0)
    going = 580.0 + 2791.5506666667 / 1.61051
    assert close(res.operating_assets, going * 0.9 + 100.0, rel=1e-7)
    full = bridge(cash=100.0, non_operating_assets=50.0, debt=200.0, leases=30.0, minority_interests=10.0,
                  other_claims=20.0, diluted_shares=10.0)
    res = run_scenario(hand_inputs(), base_year(), full, 200.0)
    assert close(res.equity, res.operating_assets + 100 + 50 - 200 - 30 - 10 - 20)
    assert close(res.enterprise_value, 200.0 * 10 + 200 + 30 + 10 + 20 - 100 - 50)
    assert close(res.upside, res.per_share / 200.0 - 1.0)


def test_reinvestment_lag_zero_to_three():
    """Year t reinvests (Rev_{t+lag} - Rev_{t+lag-1}) / S/C; past the horizon revenue grows at terminal growth."""
    # Revenues: 1,000 / 1,100 / 1,210 / 1,331 / 1,464.1 / 1,610.51, then 4% forever:
    # 1,674.9304 / 1,741.927616 / 1,811.60472064.  S/C is 2.0, so each year's reinvestment is half a step.
    expected = {
        0: [50.0, 55.0, 60.5, 66.55, 73.205],
        1: [55.0, 60.5, 66.55, 73.205, 32.2102],
        2: [60.5, 66.55, 73.205, 32.2102, (1741.927616 - 1674.9304) / 2],
        3: [66.55, 73.205, 32.2102, (1741.927616 - 1674.9304) / 2, (1811.60472064 - 1741.927616) / 2],
    }
    for lag, reinvestments in expected.items():
        res = run_scenario(hand_inputs(reinvestment_lag=lag), base_year(), bridge(), 200.0)
        assert [r.reinvestment_source for r in res.rows] == ["sales_to_capital"] * 5
        for row, want in zip(res.rows, reinvestments):
            assert close(row.reinvestment, want), (lag, row.year, row.reinvestment, want)
    # a longer lag charges each year for growth further out, so year 1 spends more the longer the lag
    firsts = [run_scenario(hand_inputs(reinvestment_lag=k), base_year(), bridge(), 200.0).rows[0].reinvestment
              for k in (0, 1, 2, 3)]
    assert firsts == sorted(firsts)
    # an unknown lag is refused by the validator, not silently taken (see test_schema)
    assert close(run_scenario(hand_inputs(reinvestment_lag=1), base_year(), bridge(), 200.0).operating_assets,
                 2313.3333333333335, rel=1e-9)


def test_ten_year_fade_reference():
    inp = fade_years(hand_inputs())
    assert inp.horizon == 10 and inp.explicit_years == 5
    assert [round(g, 6) for g in inp.growth[5:]] == [0.088, 0.076, 0.064, 0.052, 0.04]
    assert inp.margin == [0.20] * 10
    assert inp.reinvestment_override == [None] * 10
    assert [round(x, 6) for x in tax_path(inp)] == [0.2] * 5 + [0.21, 0.22, 0.23, 0.24, 0.25]
    assert [round(x, 6) for x in wacc_path(inp)] == [0.1] * 5 + [0.098, 0.096, 0.094, 0.092, 0.09]
    assert sales_to_capital_path(replace(inp, sales_to_capital_late=3.0)) == [2.0] * 5 + [3.0] * 5
    res = run_scenario(inp, base_year(), bridge(), 200.0)
    # Independent re-computation of the ten-year model.
    rev, df, total = 1000.0, 1.0, 0.0
    revs = [rev]
    for g in inp.growth:
        rev *= 1 + g
        revs.append(rev)
    revs.append(revs[-1] * 1.04)
    taxes, waccs = tax_path(inp), wacc_path(inp)
    for t in range(1, 11):
        eat = revs[t] * 0.2 * (1 - taxes[t - 1])
        reinv = (revs[t + 1] - revs[t]) / 2.0
        df /= 1 + waccs[t - 1]
        total += (eat - reinv) * df
    tv = revs[11] * 0.2 * 0.75 * (1 - 0.04 / 0.09) / (0.09 - 0.04)
    assert close(res.operating_assets, total + tv * df, rel=1e-9)
    assert res.operating_assets > run_scenario(hand_inputs(), base_year(), bridge(), 200.0).operating_assets


def test_rnd_capitalization_arithmetic():
    # N = 3; current 300; history oldest first [100, 200, 250] = years -3, -2, -1.
    # amortization = (100 + 200 + 250) / 3 = 183.333; adjustment = 300 - 183.333 = 116.667
    # asset = 300 + 250 * 2/3 + 200 * 1/3 = 300 + 166.667 + 66.667 = 533.333
    adj, asset, amort = rnd_capitalization(300.0, [100.0, 200.0, 250.0], 3)
    assert close(amort, 550.0 / 3)
    assert close(adj, 300.0 - 550.0 / 3)
    assert close(asset, 300.0 + 500.0 / 3 + 200.0 / 3)
    # Only the last N years of a longer history are used.
    adj2, asset2, _ = rnd_capitalization(300.0, [999.0, 100.0, 200.0, 250.0], 3)
    assert close(adj2, adj) and close(asset2, asset)


def minimal_doc() -> dict:
    return {
        "base_year": {
            "revenue": {"value": 1000.0}, "operating_income_gaap": {"value": 150.0},
            "one_time_items": [{"name": "charge", "value": 20.0}, {"name": "gain", "value": -5.0}],
            "amortization_of_acquired_intangibles": {"value": 50.0},
            "stock_based_compensation": {"value": 30.0}, "rnd_expense": {"value": 100.0},
            "effective_tax_rate": {"value": 0.2}, "invested_capital": {"value": 800.0},
        },
        "switches": {"addback_acquired_amortization": False, "capitalize_rnd": False,
                     "rnd_amortization_years": 3, "rnd_history": [60.0, 80.0, 90.0]},
        "market": {"marginal_tax_rate": 0.25, "mature_market_erp": 0.045},
        "cost_of_capital": {"method": "build", "build": {
            "unlevered_beta": {"value": 1.2}, "debt_to_equity_market": {"value": 0.1},
            "pretax_cost_of_debt": {"value": 0.06}, "damodaran_industry": {"value": "Semiconductor"}},
            "terminal": {"method": "mature"}},
    }


def test_base_year_switches():
    doc = minimal_doc()
    by = build_base_year(doc)
    assert close(by.one_time_items, 15.0)
    assert close(by.adjusted_operating_income, 165.0)          # 150 + 20 - 5; amortization stays deducted
    assert by.amortization_addback == 0.0 and by.rnd_adjustment == 0.0
    assert close(by.invested_capital, 800.0)
    doc["switches"]["addback_acquired_amortization"] = True
    by = build_base_year(doc)
    assert close(by.adjusted_operating_income, 215.0)          # + 50 amortization memo
    doc["switches"]["capitalize_rnd"] = True
    by = build_base_year(doc)
    # R&D: amortization (60 + 80 + 90) / 3 = 76.667; adjustment 100 - 76.667 = 23.333
    # asset = 100 + 90 * 2/3 + 80 * 1/3 = 186.667
    assert close(by.rnd_adjustment, 100.0 - 230.0 / 3)
    assert close(by.adjusted_operating_income, 215.0 + 100.0 - 230.0 / 3)
    assert close(by.rnd_asset, 100.0 + 60.0 + 80.0 / 3)
    assert close(by.invested_capital, 800.0 + by.rnd_asset)


def test_cost_of_capital_build_and_terminal_methods():
    doc = minimal_doc()
    market = MarketInputs(price=50.0, risk_free_rate=0.04, equity_risk_premium=0.05)
    coc = build_cost_of_capital(doc, market)
    # levered beta = 1.2 * (1 + 0.75 * 0.1) = 1.29; cost of equity = 0.04 + 1.29 * 0.05 = 0.1045
    # WACC = (1/1.1) * 0.1045 + (0.1/1.1) * 0.06 * 0.75 = 0.095 + 0.0040909 = 0.0990909
    assert close(coc.levered_beta, 1.29)
    assert close(coc.cost_of_equity, 0.1045)
    assert close(coc.wacc, 0.1045 / 1.1 + 0.1 / 1.1 * 0.06 * 0.75)
    assert close(coc.terminal_wacc, 0.085)                      # mature: rf + 4.5%
    doc["cost_of_capital"]["terminal"] = {"method": "hold"}
    assert close(build_cost_of_capital(doc, market).terminal_wacc, coc.wacc)
    doc["cost_of_capital"]["terminal"] = {"method": "value", "value": 0.08}
    assert close(build_cost_of_capital(doc, market).terminal_wacc, 0.08)
    doc["cost_of_capital"] = {"method": "pinned", "pinned_value": 0.11, "terminal": {"method": "mature"}}
    pinned = build_cost_of_capital(doc, market)
    assert close(pinned.wacc, 0.11) and pinned.levered_beta is None


# --------------------------------------------------------------------------- #
# compute() on the example document
# --------------------------------------------------------------------------- #

@pytest.fixture
def example() -> dict:
    return load_yaml(FIXTURE)


MARKET = MarketInputs(price=70.0, risk_free_rate=0.0425, equity_risk_premium=0.042, price_date="2026-09-05",
                      risk_free_date="2026-09-05", erp_date="2026-09-01")


def test_compute_weighted_and_management(example):
    res = compute(example, MARKET)
    assert set(res.scenarios) == {"bear", "base", "bull", "management"}
    w = res.weighted
    expected = sum(res.scenarios[n].per_share * res.scenarios[n].inputs.weight for n in ("bear", "base", "bull"))
    assert close(w.per_share, expected)
    assert res.scenarios["management"].inputs.weight is None
    for sc in res.scenarios.values():
        assert sc.reference is not None and sc.reference.inputs.horizon == 10
        assert sc.reference_label == "10-year fade"
        assert close(sc.enterprise_value, 70.0 * 870 + 4200 + 300 + 0 + 100 - 1500 - 200)
    assert res.scenarios["bull"].rows[0].reinvestment_source == "override"


def test_compute_stops_scenario_with_null_and_skips_management(example):
    doc = copy.deepcopy(example)
    doc["scenarios"]["bear"]["revenue_growth"]["values"][2] = None
    doc["scenarios"]["management"]["computable"] = False
    res = compute(doc, MARKET)
    assert "bear" in res.stopped and "scenarios.bear.revenue_growth.values.2 is null" in res.stopped["bear"][0]
    assert "management" in res.skipped
    assert res.weighted is None
    assert any("bear scenario not computed" in w for w in res.warnings)


def test_terminal_growth_above_riskfree_needs_flag(example):
    doc = copy.deepcopy(example)
    doc["scenarios"]["base"]["terminal"]["growth"]["value"] = 0.05
    res = compute(doc, MARKET)
    assert "base" in res.stopped and "set allow_above_riskfree: true" in res.stopped["base"][0]
    doc["scenarios"]["base"]["terminal"]["growth"]["allow_above_riskfree"] = True
    doc["scenarios"]["base"]["terminal"]["growth"]["reason"] = "test"
    res = compute(doc, MARKET)
    assert "base" in res.scenarios
    assert any("above the risk-free rate" in w for w in res.warnings)


def test_terminal_growth_riskfree_resolves_to_the_runs_rate(example):
    doc = copy.deepcopy(example)
    doc["scenarios"]["bull"]["terminal"]["growth"]["value"] = "riskfree"
    res = compute(doc, MARKET)
    for name in ("bear", "base", "bull"):
        inp = res.scenarios[name].inputs
        assert inp.terminal_growth_is_riskfree and close(inp.terminal_growth, MARKET.risk_free_rate)
        assert close(res.scenarios[name].terminal.growth, 0.0425)
    assert res.scenarios["management"].inputs.terminal_growth_is_riskfree is False
    # a different run rate moves the terminal growth with it, never trips the cap rule
    other = compute(doc, MarketInputs(price=70.0, risk_free_rate=0.05, equity_risk_premium=0.042))
    assert close(other.scenarios["base"].terminal.growth, 0.05)
    assert "base" not in other.stopped
    assert not any("above the risk-free rate" in w for w in other.warnings)


def test_numeric_terminal_growth_cap_rule_at_compute_time(example):
    doc = copy.deepcopy(example)
    doc["scenarios"]["bull"]["terminal"]["growth"]["value"] = 0.045     # above the run's 4.25%
    res = compute(doc, MARKET)
    assert "bull" in res.stopped and "above the risk-free rate 0.0425" in res.stopped["bull"][0]
    assert "bull" not in res.scenarios and res.weighted is None
    doc["scenarios"]["bull"]["terminal"]["growth"]["allow_above_riskfree"] = True
    doc["scenarios"]["bull"]["terminal"]["growth"]["reason"] = "test override"
    res = compute(doc, MARKET)
    assert "bull" in res.scenarios
    assert sum("bull: terminal growth 0.0450 is above the risk-free rate 0.0425" in w for w in res.warnings) == 1


def test_null_beta_and_debt_to_equity_are_derived(example):
    doc = copy.deepcopy(example)
    doc["cost_of_capital"]["build"]["unlevered_beta"]["value"] = None
    doc["cost_of_capital"]["build"]["debt_to_equity_market"]["value"] = None
    res = compute(doc, MARKET)
    coc = res.cost_of_capital
    # betas.csv (2026-01-05): Semiconductor unlevered beta corrected for cash is 1.5046
    assert coc.unlevered_beta is not None and 1.4 < coc.unlevered_beta < 1.6
    assert coc.unlevered_beta_note and "Semiconductor" in coc.unlevered_beta_note
    # D/E = (4,200 debt + 300 leases) / (70 x 870 shares) = 4,500 / 60,900
    assert close(coc.debt_to_equity, 4500.0 / 60900.0)
    assert coc.debt_to_equity_note and "price 70.00" in coc.debt_to_equity_note
    assert sum("unlevered_beta.value is null; using" in w for w in res.warnings) == 1
    assert sum("debt_to_equity_market.value is null; derived" in w for w in res.warnings) == 1
    assert set(res.scenarios) == {"bear", "base", "bull", "management"}
    doc["cost_of_capital"]["build"]["damodaran_industry"]["value"] = "No Such Industry"
    with pytest.raises(EngineError):
        compute(doc, MARKET)


# --------------------------------------------------------------------------- #
# Section 18.2: the default ten-year structure and the reference swap
# --------------------------------------------------------------------------- #

def test_horizon_defaults_to_ten(example):
    """A file with no `horizon` key is a ten-year model with five explicit years (section 18.2)."""
    doc = copy.deepcopy(example)
    del doc["horizon"]
    res = compute(doc, MARKET)
    assert res.horizon == 10 and res.reference_label == "5-year stop"
    for sc in res.scenarios.values():
        assert len(sc.rows) == 10 and sc.inputs.explicit_years == 5


def test_five_entry_lists_at_horizon_ten_equal_a_ten_entry_twin(example):
    """The rule of section 18.2 must reproduce, to the dollar, what an explicit ten-entry file gives."""
    five = copy.deepcopy(example)
    five["horizon"] = 10
    res_five = compute(five, MARKET)

    ten = copy.deepcopy(example)
    ten["horizon"] = 10
    for name in ("bear", "base", "bull", "management"):
        s = ten["scenarios"][name]
        g5 = s["revenue_growth"]["values"][4]
        gt = MARKET.risk_free_rate if s["terminal"]["growth"]["value"] == "riskfree" else s["terminal"]["growth"]["value"]
        s["revenue_growth"]["values"] = list(s["revenue_growth"]["values"]) + [g5 - (g5 - gt) * k / 5 for k in range(1, 6)]
        s["operating_margin"]["values"] = list(s["operating_margin"]["values"]) + [s["operating_margin"]["values"][4]] * 5
        s["reinvestment_override"]["values"] = list(s["reinvestment_override"]["values"]) + [None] * 5
    res_ten = compute(ten, MARKET)

    for name in ("bear", "base", "bull", "management"):
        a, b = res_five.scenarios[name], res_ten.scenarios[name]
        assert close(a.operating_assets, b.operating_assets, rel=1e-12), name
        assert close(a.per_share, b.per_share, rel=1e-12), name
    # ... and the old fade_years helper is exactly what the engine applied
    inp = scenario_inputs(five, "base", build_cost_of_capital(five, MARKET))
    hand = fade_years(replace(inp, growth=inp.growth[:5], margin=inp.margin[:5],
                              reinvestment_override=inp.reinvestment_override[:5], explicit_years=None))
    assert [round(g, 12) for g in inp.growth] == [round(g, 12) for g in hand.growth]
    assert inp.margin == hand.margin


def test_reference_swaps_with_the_horizon(example):
    """Horizon 10 references the 5-year stop and horizon 5 the 10-year fade, each equal to the real run."""
    five = copy.deepcopy(example)
    five["horizon"] = 5
    ten = copy.deepcopy(example)
    ten["horizon"] = 10
    r5, r10 = compute(five, MARKET), compute(ten, MARKET)
    assert r5.reference_label == "10-year fade" and r10.reference_label == "5-year stop"
    for name in ("bear", "base", "bull", "management"):
        assert len(r10.scenarios[name].reference.rows) == 5
        assert len(r5.scenarios[name].reference.rows) == 10
        # the ten-year model's 5-year-stop reference is the five-year run of the same file
        assert close(r10.scenarios[name].reference.per_share, r5.scenarios[name].per_share, rel=1e-12), name
        # and the five-year model's 10-year-fade reference is the ten-year run of the same file
        assert close(r5.scenarios[name].reference.per_share, r10.scenarios[name].per_share, rel=1e-12), name
        assert r10.scenarios[name].reference_label == "5-year stop"
    assert close(r10.weighted.reference_per_share, r5.weighted.per_share, rel=1e-12)
    assert close(r5.weighted.reference_per_share, r10.weighted.per_share, rel=1e-12)


def test_stop_years_holds_tax_and_cost_of_capital_at_their_start_values():
    inp = fade_years(hand_inputs())
    stop = stop_years(inp)
    assert stop.horizon == 5 and stop.explicit_years is None
    assert tax_path(stop) == [0.20] * 5 and wacc_path(stop) == [0.10] * 5
    assert reference_inputs(inp).name.endswith("(5-year stop)")
    assert reference_inputs(hand_inputs()).name.endswith("(10-year fade)")


def test_terminal_roic_at_or_above_todays_return_warns(example):
    doc = copy.deepcopy(example)
    # base-year ROIC is 7.19%; the base case's terminal ROIC is 8.75% + 3 points, so it warns
    res = compute(doc, MARKET)
    assert any("terminal return on capital" in w and "base-year return on capital" in w for w in res.warnings)
    assert any("terminal return on capital" in w for w in res.scenarios["base"].warnings)
    # a company earning far more today than the terminal settings allow does not warn
    doc["base_year"]["invested_capital"]["value"] = 2000.0
    quiet = compute(doc, MARKET)
    assert not any("base-year return on capital" in w for w in quiet.warnings)
