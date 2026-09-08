"""Every validation rule of AGENTS.md section 18.4, one test each."""

from __future__ import annotations

import copy
from pathlib import Path

import pytest

from valuation.schema import (
    SchemaError, coerce_scalar, get_path, load_yaml, set_path, validate, validate_or_raise,
)

FIXTURE = Path(__file__).resolve().parent / "fixtures" / "example_assumptions.yaml"


@pytest.fixture
def doc() -> dict:
    return load_yaml(FIXTURE)


def errors_mentioning(v, text: str) -> list[str]:
    return [e for e in v.errors if text in e]


def test_fixture_is_valid(doc):
    v = validate(doc)
    assert v.ok, v.errors
    assert not v.shared_nulls and not v.stopped and not v.skipped
    assert v.computable_scenarios() == ["bear", "base", "bull", "management"]


def test_weights_must_sum_to_one(doc):
    doc["scenarios"]["bear"]["weight"] = 0.30
    v = validate(doc)
    assert errors_mentioning(v, "scenarios.*.weight")
    doc["scenarios"]["bear"]["weight"] = 0.25 + 5e-7           # inside the 1e-6 tolerance
    assert validate(doc).ok


def test_management_is_never_weighted(doc):
    doc["scenarios"]["management"]["weight"] = 0.1
    assert errors_mentioning(validate(doc), "scenarios.management.weight")


def test_null_in_scenario_cell_stops_only_that_scenario(doc):
    doc["scenarios"]["base"]["operating_margin"]["values"][4] = None
    doc["scenarios"]["bull"]["sales_to_capital"]["value_late"] = None
    v = validate(doc)
    assert v.ok
    assert v.stopped["base"] == ["scenarios.base.operating_margin.values.4 is null"]
    assert v.stopped["bull"] == ["scenarios.bull.sales_to_capital.value_late is null"]
    assert v.computable_scenarios() == ["bear", "management"]


def test_null_in_shared_cell_stops_every_scenario(doc):
    doc["bridge"]["debt"]["value"] = None
    doc["base_year"]["revenue"]["value"] = None
    v = validate(doc)
    assert v.ok
    assert v.shared_nulls == ["base_year.revenue.value", "bridge.debt.value"]
    assert v.computable_scenarios() == []


def test_reinvestment_override_nulls_are_allowed(doc):
    doc["scenarios"]["base"]["reinvestment_override"]["values"] = [None, 120, None, None, None]
    v = validate(doc)
    assert v.ok and "base" not in v.stopped


def test_management_not_computable_is_skipped_without_error(doc):
    doc["scenarios"]["management"]["computable"] = False
    doc["scenarios"]["management"]["revenue_growth"]["values"] = [None] * 5
    doc["scenarios"]["management"]["terminal"]["growth"]["value"] = None
    v = validate(doc)
    assert v.ok
    assert "management" in v.skipped and "management" not in v.stopped
    assert v.computable_scenarios() == ["bear", "base", "bull"]


def test_horizon_must_be_five_or_ten(doc):
    doc["horizon"] = 7
    assert errors_mentioning(validate(doc), "horizon")


def test_per_year_lists_must_have_horizon_entries(doc):
    doc["horizon"] = 10
    v = validate(doc)
    assert errors_mentioning(v, "scenarios.base.revenue_growth.values: expected 10 entries")
    doc["horizon"] = 5
    doc["scenarios"]["bear"]["operating_margin"]["values"] = [0.1, 0.1, 0.1, 0.1]
    assert errors_mentioning(validate(doc), "scenarios.bear.operating_margin.values: expected 5 entries")


def test_ten_year_horizon_with_ten_entry_lists_is_valid(doc):
    doc["horizon"] = 10
    for name in ("bear", "base", "bull", "management"):
        s = doc["scenarios"][name]
        s["revenue_growth"]["values"] = s["revenue_growth"]["values"] + [0.04] * 5
        s["operating_margin"]["values"] = s["operating_margin"]["values"] + [s["operating_margin"]["values"][-1]] * 5
        s["reinvestment_override"]["values"] = [None] * 10
    assert validate(doc).ok


def test_rates_are_decimals_not_percents(doc):
    doc["scenarios"]["base"]["tax_rate"]["start"] = 8
    doc["market"]["marginal_tax_rate"] = 25
    doc["scenarios"]["bull"]["terminal"]["growth"]["value"] = 4
    v = validate(doc)
    assert errors_mentioning(v, "scenarios.base.tax_rate.start: rates are decimals")
    assert errors_mentioning(v, "market.marginal_tax_rate: rates are decimals")
    assert errors_mentioning(v, "scenarios.bull.terminal.growth.value: rates are decimals")


def test_growth_written_as_percent_is_rejected_and_large_growth_warned(doc):
    doc["scenarios"]["bull"]["revenue_growth"]["values"][0] = 30
    assert errors_mentioning(validate(doc), "scenarios.bull.revenue_growth.values.0")
    doc["scenarios"]["bull"]["revenue_growth"]["values"][0] = 1.5
    v = validate(doc)
    assert v.ok and any("very large for a decimal rate" in w for w in v.warnings)


def test_large_roic_premium_requires_flag_and_reason(doc):
    prem = doc["scenarios"]["bull"]["terminal"]["roic_premium"]
    prem["value"] = 0.08
    assert errors_mentioning(validate(doc), "allow_large_premium")
    prem["allow_large_premium"] = True
    prem["reason"] = ""
    assert errors_mentioning(validate(doc), "no reason")
    prem["reason"] = "durable moat per business.md section 5"
    v = validate(doc)
    assert v.ok
    assert any("terminal ROIC premium 0.080 is above 0.05" in w for w in v.warnings)


def test_allow_above_riskfree_needs_a_reason(doc):
    g = doc["scenarios"]["base"]["terminal"]["growth"]
    g["allow_above_riskfree"] = True
    g["reason"] = ""
    assert errors_mentioning(validate(doc), "allow_above_riskfree is true but no reason")
    g["reason"] = "a reason"
    assert validate(doc).ok


def test_cost_of_capital_override_warns(doc):
    doc["scenarios"]["bear"]["cost_of_capital_override"] = 0.12
    v = validate(doc)
    assert v.ok and any("cost of capital pinned to 0.1200" in w for w in v.warnings)


def test_switches_warn_and_need_inputs(doc):
    doc["switches"]["addback_acquired_amortization"] = True
    doc["switches"]["capitalize_rnd"] = True
    v = validate(doc)
    assert v.ok
    assert any("addback_acquired_amortization is on" in w for w in v.warnings)
    assert any("capitalize_rnd is on" in w for w in v.warnings)
    doc["switches"]["rnd_history"] = [1, 2]
    assert errors_mentioning(validate(doc), "switches.rnd_history: needs at least 5")
    doc["switches"]["rnd_history"] = [1, 2, 3, 4, 5]
    doc["base_year"]["rnd_expense"]["value"] = None
    assert "base_year.rnd_expense.value" in validate(doc).shared_nulls


def test_cost_of_capital_methods(doc):
    doc["cost_of_capital"]["method"] = "pinned"
    assert errors_mentioning(validate(doc), "cost_of_capital.pinned_value")
    doc["cost_of_capital"]["pinned_value"] = 0.10
    assert validate(doc).ok
    doc["cost_of_capital"]["terminal"] = {"method": "value", "value": None}
    assert errors_mentioning(validate(doc), "cost_of_capital.terminal.value")
    doc["cost_of_capital"]["terminal"] = {"method": "whatever"}
    assert errors_mentioning(validate(doc), "cost_of_capital.terminal.method")
    doc["cost_of_capital"]["terminal"] = {"method": "hold"}
    v = validate(doc)
    assert v.ok and any("'hold'" in w for w in v.warnings)


def test_build_null_beta_and_de_are_derived_when_possible(doc):
    doc["cost_of_capital"]["build"]["unlevered_beta"]["value"] = None
    doc["cost_of_capital"]["build"]["debt_to_equity_market"]["value"] = None
    v = validate(doc)
    assert v.ok and not v.shared_nulls
    assert any("unlevered_beta.value is null; the engine takes" in w for w in v.warnings)
    assert any("debt_to_equity_market.value is null; the engine derives" in w for w in v.warnings)
    doc["cost_of_capital"]["build"]["damodaran_industry"]["value"] = None
    v = validate(doc)
    assert "cost_of_capital.build.unlevered_beta.value" in v.shared_nulls
    doc["cost_of_capital"]["build"]["pretax_cost_of_debt"]["value"] = None
    assert "cost_of_capital.build.pretax_cost_of_debt.value" in validate(doc).shared_nulls


def test_market_block(doc):
    doc["market"]["price"] = -3
    assert errors_mentioning(validate(doc), "market.price")
    doc["market"]["price"] = "auto"
    doc["market"]["risk_free_rate"] = "later"
    assert errors_mentioning(validate(doc), "market.risk_free_rate")
    doc["market"]["risk_free_rate"] = 0.04
    doc["market"]["equity_risk_premium"] = 4.5
    assert errors_mentioning(validate(doc), "market.equity_risk_premium")


def test_unknown_scenario_and_missing_scenario(doc):
    doc["scenarios"]["worst"] = copy.deepcopy(doc["scenarios"]["bear"])
    assert errors_mentioning(validate(doc), "scenarios.worst: unknown scenario")
    del doc["scenarios"]["worst"]
    del doc["scenarios"]["bull"]
    assert errors_mentioning(validate(doc), "scenarios.bull: missing")


def test_structural_errors_name_the_path(doc):
    doc["scenarios"]["base"]["sales_to_capital"] = 1.5
    assert errors_mentioning(validate(doc), "scenarios.base.sales_to_capital: must be a mapping")
    doc["scenarios"]["base"]["sales_to_capital"] = {"value": 0.0, "value_late": 1.2}
    assert errors_mentioning(validate(doc), "scenarios.base.sales_to_capital.value: must be positive")
    doc["bridge"]["diluted_shares"]["value"] = 0
    assert errors_mentioning(validate(doc), "bridge.diluted_shares.value: must be positive")
    doc["schema"] = 2
    assert errors_mentioning(validate(doc), "schema: expected 1")
    doc["units"] = "thousands"
    assert errors_mentioning(validate(doc), "units")


def test_unknown_keys_warn(doc):
    doc["extra"] = 1
    doc["scenarios"]["base"]["typo_key"] = 1
    doc["diagnostics"]["other"] = {"value": 1}
    v = validate(doc)
    assert v.ok
    assert any("extra: unknown top-level key" in w for w in v.warnings)
    assert any("scenarios.base.typo_key: unknown key" in w for w in v.warnings)
    assert any("diagnostics.other: unknown key" in w for w in v.warnings)


def test_validate_or_raise(doc):
    doc["horizon"] = 3
    with pytest.raises(SchemaError):
        validate_or_raise(doc)


def test_probability_of_failure_needs_distress_proceeds(doc):
    doc["bridge"]["probability_of_failure"]["value"] = 0.1
    doc["bridge"]["distress_proceeds"]["value"] = None
    assert "bridge.distress_proceeds.value" in validate(doc).shared_nulls
    doc["bridge"]["probability_of_failure"]["value"] = 1.5
    assert errors_mentioning(validate(doc), "bridge.probability_of_failure.value")


# --------------------------------------------------------------------------- #
# dotted paths and --set coercion
# --------------------------------------------------------------------------- #

def test_get_and_set_path(doc):
    assert get_path(doc, "scenarios.base.operating_margin.values.4") == 0.26
    out = set_path(doc, "scenarios.base.operating_margin.values.4", 0.34)
    assert get_path(out, "scenarios.base.operating_margin.values.4") == 0.34
    assert get_path(doc, "scenarios.base.operating_margin.values.4") == 0.26     # original untouched
    out = set_path(doc, "market.price", 70.0)
    assert out["market"]["price"] == 70.0
    with pytest.raises(SchemaError):
        set_path(doc, "scenarios.base.operating_margin.values.9", 0.1)
    assert get_path(doc, "no.such.path", "dflt") == "dflt"


def test_coerce_scalar():
    assert coerce_scalar("null") is None and coerce_scalar("~") is None
    assert coerce_scalar("true") is True and coerce_scalar("False") is False
    assert coerce_scalar("12") == 12 and isinstance(coerce_scalar("12"), int)
    assert coerce_scalar("0.34") == 0.34
    assert coerce_scalar("auto") == "auto"


def test_terminal_growth_riskfree_string_is_accepted(doc):
    assert doc["scenarios"]["base"]["terminal"]["growth"]["value"] == "riskfree"
    doc["scenarios"]["bull"]["terminal"]["growth"]["value"] = "RiskFree"
    v = validate(doc)
    assert v.ok and not v.stopped
    doc["scenarios"]["bull"]["terminal"]["growth"]["value"] = "risk free"
    assert errors_mentioning(validate(doc), "scenarios.bull.terminal.growth.value: expected a number")


def test_numeric_terminal_growth_above_manual_riskfree_is_an_error_unless_allowed(doc):
    doc["market"]["risk_free_rate"] = 0.04
    doc["scenarios"]["bull"]["terminal"]["growth"]["value"] = 0.045
    v = validate(doc)
    assert errors_mentioning(v, "scenarios.bull.terminal.growth.value: 0.0450 is above the risk-free rate 0.0400")
    doc["scenarios"]["bull"]["terminal"]["growth"]["allow_above_riskfree"] = True
    doc["scenarios"]["bull"]["terminal"]["growth"]["reason"] = "documented override"
    v = validate(doc)
    assert v.ok
    assert any("bull: terminal growth 0.0450 is above the risk-free rate 0.0400" in w for w in v.warnings)
    # with market.risk_free_rate: auto the check waits for the run (engine test covers it)
    doc["market"]["risk_free_rate"] = "auto"
    doc["scenarios"]["bull"]["terminal"]["growth"]["allow_above_riskfree"] = False
    assert validate(doc).ok


def test_detail_is_accepted_silently_in_cells_and_scenarios(doc):
    doc["scenarios"]["base"]["revenue_growth"]["detail"] = "History table: 2022 9.8%, 2023 8.7%."
    doc["scenarios"]["base"]["detail"] = "Working notes for the whole case."
    doc["base_year"]["revenue"]["detail"] = "FY2025 plus six months minus six months."
    doc["diagnostics"]["historical_revenue_cagr"]["detail"] = "From the ten-year table."
    v = validate(doc)
    assert v.ok and not any("detail" in w for w in v.warnings)


def test_sources_block_is_accepted_silently_and_checked_for_shape(doc):
    v = validate(doc)                                           # the fixture carries two entries
    assert v.ok and not any("sources" in w for w in v.warnings)
    doc["sources"] = [{"tag": "[x]"}, "loose text", {"tag": "[y]", "file": "sources/y.txt", "date": "2026-01-01"}]
    v = validate(doc)
    assert any("sources.0.file: required string" in e for e in v.errors)
    assert any("sources.1: must be a mapping" in e for e in v.errors)
    assert not any("sources.2" in e for e in v.errors)
    doc["sources"] = {"tag": "[x]"}
    assert any("sources: must be a list" in e for e in validate(doc).errors)
    del doc["sources"]
    assert validate(doc).ok
