"""Screen language: engine messages, cell names and values as the owner sees them (no Streamlit run needed)."""

from __future__ import annotations

import pytest

streamlit = pytest.importorskip("streamlit")

from valuation.app_core import describe_path, md, plain_message, show_value  # noqa: E402


def test_weights_message_is_a_plain_sentence_with_percentages():
    text = plain_message("scenarios.*.weight: bear + base + bull must sum to 1, got 1.050000")
    assert text == "The weights add up to 105%; they must add up to 100% (Taxes and weights page)"


def test_terminal_growth_above_riskfree_names_the_case_the_rates_and_the_checkbox():
    raw = ("scenarios.bull.terminal.growth.value: 0.0600 is above the risk-free rate 0.0475; set allow_above_riskfree: "
           "true and give a reason (section 18.4 rule 5)")
    text = plain_message(raw)
    assert text == ("Bull case: terminal growth 6.00% is above the risk-free rate 4.75%; tick 'Allow growth above the "
                    "risk-free rate' on the Terminal value page or lower the number")
    assert "scenarios" not in text and "18.4" not in text


def test_null_and_engine_stops_become_words():
    assert plain_message("scenarios.bull.sales_to_capital.value_late is null") == "Bull case, sales-to-capital, years 6-10 is empty"
    assert plain_message("base_year.revenue.value is null") == "Base year: revenue is empty"
    assert plain_message("bull: terminal cost of capital 0.0875 must exceed terminal growth 0.0900") == (
        "Bull case: the terminal cost of capital 8.75% must be above terminal growth 9.00%; lower the growth or raise "
        "the terminal cost of capital")
    assert plain_message("bear scenario not computed: scenarios.bear.revenue_growth.values.2 is null") == (
        "Bear case not computed: Bear case, revenue growth, Year 3 is empty")
    assert plain_message("scenarios.base.operating_margin.values: expected 5 entries (horizon 5), got 4") == (
        "Base case, operating margin needs 5 yearly values and has 4")
    assert plain_message("market.price is a manual value (70.00) from assumptions.yaml or --set, not fetched") == (
        "Market: price is a value written in the assumptions file (70.00), not fetched")
    assert "--set" not in plain_message("risk-free fetch failed (x); pass --set market.risk_free_rate=<decimal> or write a decimal in assumptions.yaml")


def test_describe_path_and_show_value_match_the_pages():
    assert describe_path("scenarios.base.revenue_growth.values.0") == ("Base case, revenue growth, Year 1", "pct")
    assert describe_path("scenarios.bear.reinvestment_override.values.1") == ("Bear case, reinvestment override, Year 2", "money")
    assert describe_path("scenarios.bull.terminal.growth.value") == ("Bull case, terminal growth", "growth")
    assert describe_path("scenarios.bull.terminal.roic_premium.allow_large_premium") == ("Bull case, 'Allow a premium above 5 points'", "bool")
    assert describe_path("scenarios.base.story") == ("Base case, story", "text")
    assert describe_path("scenarios.base.sales_to_capital.reason") == ("Base case, sales-to-capital, years 1-5 reason", "text")
    assert describe_path("bridge.diluted_shares.value") == ("Bridge: diluted shares (millions)", "shares")
    assert describe_path("base_year.one_time_items.1.value") == ("Base year: one-time item 2", "money")
    assert describe_path("cost_of_capital.terminal.method") == ("Terminal cost of capital: method", "terminal_method")
    assert describe_path("horizon") == ("Forecast years", "int")
    assert show_value(0.2, "pct") == "20.0%" and show_value(0.0425, "pct2") == "4.25%"
    assert show_value(173970, "money") == "173,970" and show_value(12309.0, "shares") == "12,309.0"
    assert show_value("riskfree", "growth") == "equal to the risk-free rate" and show_value(0.04, "growth") == "4.00%"
    assert show_value(True, "bool") == "on" and show_value(None, "pct") == "empty"
    assert show_value("mature", "terminal_method").startswith("Mature company")


def test_md_maps_keys_citations_and_maths_symbols_to_words_and_escapes_dollars():
    text = md("Equal to the fetched rate, by rule (§18.4 rule 5); see reinvestment_override; 1.34× the base; $195–205 billion")
    assert "(by rule)" in text and "the per-year reinvestment overrides" in text and "1.34 x the base" in text
    assert "\\$195" in text and "§" not in text and "×" not in text
