"""Screen language: engine messages, cell names and values as the owner sees them (no Streamlit run needed)."""

from __future__ import annotations

import pytest

streamlit = pytest.importorskip("streamlit")

from valuation.app_core import (  # noqa: E402
    dedupe_columns, describe_path, detail_blocks, md, narrow_tables, plain_clause, plain_message, show_value,
    stop_sentence, transposed_table, warning_sentence,
)


def test_weights_message_is_a_plain_sentence_with_percentages():
    text = plain_message("scenarios.*.weight: bear + base + bull must sum to 1, got 1.050000")
    assert text == "The weights add up to 105%; they must add up to 100% (Taxes and weights page)."
    # the same message without the closing stop, for use inside a longer sentence
    assert plain_clause("scenarios.*.weight: bear + base + bull must sum to 1, got 1.050000").endswith(
        "(Taxes and weights page)")


def test_terminal_growth_above_riskfree_names_the_case_the_rates_and_the_checkbox():
    raw = ("scenarios.bull.terminal.growth.value: 0.0600 is above the risk-free rate 0.0475; set allow_above_riskfree: "
           "true and give a reason (section 18.4 rule 5)")
    text = plain_message(raw)
    assert text == ("Bull case: terminal growth 6.00% is above the risk-free rate 4.75%; tick 'Allow growth above the "
                    "risk-free rate' on the Terminal value page or lower the number.")
    assert "scenarios" not in text and "18.4" not in text


def test_null_and_engine_stops_become_words():
    assert plain_message("scenarios.bull.sales_to_capital.value_late is null") == "Bull case, sales-to-capital, years 6-10 is empty."
    assert plain_message("base_year.revenue.value is null") == "Base year: revenue is empty."
    assert plain_message("bull: terminal cost of capital 0.0875 must exceed terminal growth 0.0900") == (
        "Bull case: the terminal cost of capital 8.75% must be above terminal growth 9.00%; lower the growth or raise "
        "the terminal cost of capital.")
    assert plain_message("bear scenario not computed: scenarios.bear.revenue_growth.values.2 is null") == (
        "Bear case not computed: Bear case, revenue growth, Year 3 is empty.")
    assert plain_message("scenarios.base.operating_margin.values: expected 5 entries (horizon 5), got 4") == (
        "Base case, operating margin needs 5 yearly values and has 4.")
    assert plain_message("scenarios.base.operating_margin.values: expected 5 or 10 entries (horizon 10), got 7") == (
        "Base case, operating margin needs 5 or 10 yearly values and has 7.")
    assert plain_message("market.price is a manual value (70.00) from assumptions.yaml or --set, not fetched") == (
        "Market: price is a value written in the assumptions file (70.00), not fetched.")
    assert "--set" not in plain_message("risk-free fetch failed (x); pass --set market.risk_free_rate=<decimal> or write a decimal in assumptions.yaml")


def test_describe_path_and_show_value_match_the_pages():
    assert describe_path("scenarios.base.revenue_growth.values.0") == ("Base case, revenue growth, Year 1", "pct")
    assert describe_path("scenarios.bear.reinvestment_override.values.1") == ("Bear case, reinvestment override, Year 2", "money")
    assert describe_path("scenarios.bull.terminal.growth.value") == ("Bull case, terminal growth", "growth")
    assert describe_path("scenarios.bull.terminal.roic_premium.allow_large_premium") == ("Bull case, 'Allow a large premium'", "bool")
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
    text = md("Zero for the bear (§18.4 rule 5); see reinvestment_override; 1.34× the base; $195–205 billion")
    assert "(by rule)" in text and "the per-year reinvestment overrides" in text and "1.34 x the base" in text
    assert "\\$195" in text and "§" not in text and "×" not in text


def test_stop_sentence_does_not_double_the_case_name():
    raw = ("scenarios.bull.terminal.growth.value: 0.0600 is above the risk-free rate 0.0475; set allow_above_riskfree: "
           "true and give a reason (section 18.4 rule 5)")
    text = stop_sentence("bull", raw)
    assert text.startswith("Bull case not computed: terminal growth 6.00% is above the risk-free rate 4.75%; tick")
    assert text.count("Bull case") == 1 and text.endswith(".")
    # a message that names the cell (not the case) keeps its words
    assert stop_sentence("bull", "scenarios.bull.sales_to_capital.value_late is null", "not computed with the current inputs") == (
        "Bull case not computed with the current inputs: Bull case, sales-to-capital, years 6-10 is empty.")


def test_md_drops_the_citation_when_the_sentence_already_says_by_rule():
    assert md("Equal to the fetched rate, by rule (§18.4 rule 5); no company grows forever.") == \
        "Equal to the fetched rate, by rule; no company grows forever."
    assert "(by rule)" in md("Zero for the bear case (§18.4 rule 5).")
    assert md("Year  change in Revenue") == md("Year  ΔRevenue")


def test_detail_blocks_keep_tables_and_aligned_columns_readable():
    notes = ("Prose first.\n\n"
             "| Year | Revenue | Capex |\n|---|---|---|\n| FY2023 | 1,457 | 206 |\n| FY2024 | -412 | 336 |\n\n"
             "Year      Revenue  Capex   D&A\nFY2023    +1,457   206     305\nFY2024      -412   336     300\n\n"
             "Closing sentence.")
    blocks = detail_blocks(notes)
    kinds = [k for k, _ in blocks]
    assert kinds == ["text", "table", "code", "text"]
    table = blocks[1][1]
    assert list(table.columns) == ["Year", "Revenue", "Capex"] and list(table.iloc[1]) == ["FY2024", "-412", "336"]
    assert "FY2023    +1,457   206     305" in blocks[2][1]
    assert detail_blocks("Just one paragraph of prose with 12 numbers.") == [("text", "Just one paragraph of prose with 12 numbers.")]


def test_duplicate_and_ragged_pipe_tables_never_break():
    assert dedupe_columns(["Ratio", "Ratio", "Year", "", "Ratio"]) == ["Ratio", "Ratio (2)", "Year", "column", "Ratio (3)"]
    notes = ("| Year | Ratio | Ratio |\n|---|---|---|\n| FY2023 | 2.2 | 107 |\n| FY2024 | n/m |\n| FY2026 | 2.2 | 441 | extra |")
    (kind, table), = detail_blocks(notes)
    assert kind == "table"
    assert list(table.columns) == ["Year", "Ratio", "Ratio (2)", "col 4"]
    assert list(table.iloc[1]) == ["FY2024", "n/m", "", ""] and list(table.iloc[2]) == ["FY2026", "2.2", "441", "extra"]


def test_warning_lines_read_like_the_notes():
    raw = ("bull scenario not computed: scenarios.bull.terminal.growth.value: 0.0600 is above the risk-free rate 0.0475; "
           "set allow_above_riskfree: true and give a reason (section 18.4 rule 5)")
    text = warning_sentence(raw)
    assert text.startswith("Bull case not computed: terminal growth 6.00% is above") and text.count("Bull case") == 1
    assert text.endswith(".")
    skipped = warning_sentence("management scenario skipped: Management gives no targets; see the 'used as' column below.")
    assert skipped == "Management case not computed; its reason and the guidance on record are on the Revenue growth page."
    assert "used as" not in skipped
    assert warning_sentence("market.price is a manual value (70.00) from assumptions.yaml or --set, not fetched").startswith("Market: price")


def test_the_new_terminal_and_transition_messages_read_as_sentences():
    """Section 18.2 and 18.4 rule 5: the premium ceilings, the bear rule, and the transition flag."""
    assert plain_message("scenarios.bull.terminal.roic_premium.value: 0.15 is above 0.12 for the bull case; set "
                         "allow_large_premium: true and give a reason (section 18.4 rule 5)") == (
        "Bull case, terminal return-on-capital premium 15.00% is above 12 points; tick 'Allow a large premium' on "
        "the Terminal value page or lower it.")
    assert plain_message("scenarios.base.terminal.roic_premium.value: 0.09 is above 0.08 for the base case; set "
                         "allow_large_premium: true and give a reason (section 18.4 rule 5)").endswith(
        "is above 8 points; tick 'Allow a large premium' on the Terminal value page or lower it.")
    assert plain_message("bull: terminal ROIC premium 0.150 is above 0.12 (allow_large_premium is true; reason: "
                         "a durable moat)") == (
        "Bull case: the terminal return-on-capital premium 15.00% is above 12 points, allowed with the reason: "
        "a durable moat.")
    assert plain_message("scenarios.bear.terminal.roic_premium.value: 0.02 must be 0 in the bear case, where the "
                         "moat is gone (section 18.4 rule 5)") == (
        "Bear case, terminal return-on-capital premium is 2.00% and must be zero: the bear case assumes the "
        "advantage is gone, so the return on capital falls to the cost of capital.")
    assert plain_message("base: terminal return on capital 11.75% is at or above the base-year return on capital "
                         "of 6.83% as reported; if that figure is depressed by goodwill from acquisitions, the "
                         "analyst's detail should say what the return is without it") == (
        "Base case: the terminal return on capital 11.75% is at or above the base-year return on capital of 6.83% "
        "as reported; if that figure is depressed by goodwill from acquisitions, the analyst's detail should say "
        "what the return is without it.")
    text = plain_message("base: the terminal year's free cash flow (2,583) is far below the year-10 free cash flow "
                         "(4,198); the terminal settings and the year-10 inputs disagree")
    assert text.startswith("Base case: the terminal year's free cash flow (2,583) is far below the year-10")
    assert text.endswith("the terminal settings and the year-10 inputs disagree.")
    assert "scenarios" not in text and "18.2" not in text


def test_every_warning_and_note_ends_in_a_full_stop():
    """Audit 4, item 10: the owner reads these as sentences, so they close like sentences."""
    for raw in ("scenarios.bull.sales_to_capital.value_late is null",
                "bull: terminal cost of capital 0.0875 must exceed terminal growth 0.0900",
                "base: the terminal year's free cash flow (1) is far below the year-10 free cash flow (2)",
                "switches.reinvestment_lag is 3: reinvestment funds the growth of 3 years later"):
        assert plain_message(raw).endswith("."), raw
        assert not plain_clause(raw).endswith("."), raw
    # a message that already ends in punctuation is left alone
    assert plain_message("Something already ends here.") == "Something already ends here."
    assert plain_message("") == ""


def test_wide_working_notes_tables_are_narrowed_not_scrolled():
    """Audit 4, item 12: a seven-column notes table would scroll sideways at 1180 px."""
    import pandas as pd

    wide = pd.DataFrame([["FY2023", "1", "2", "3", "4", "5", "6"], ["FY2024", "7", "8", "9", "10", "11", "12"]],
                        columns=["Year", "Revenue", "Change", "Capex", "D&A", "Net reinvestment", "S/C lagged"])
    (one,) = narrow_tables(wide)                                   # two rows, so it fits on its side
    assert list(one.columns) == ["Year", "FY2023", "FY2024"]
    assert list(one.iloc[0]) == ["Revenue", "1", "7"]
    assert one.equals(transposed_table(wide))
    tall = pd.DataFrame([[f"FY{2000 + i}"] + ["x"] * 7 for i in range(10)],
                        columns=["Year", "a", "b", "c", "d", "e", "f", "g"])
    parts = narrow_tables(tall)                                    # too tall to turn: cut into two tables
    assert [list(t.columns) for t in parts] == [["Year", "a", "b", "c", "d", "e"], ["Year", "f", "g"]]
    assert all(len(t.columns) <= 6 for t in parts)
    narrow = wide[["Year", "Revenue", "Capex"]]
    assert narrow_tables(narrow)[0].equals(narrow)                 # six columns or fewer pass through
