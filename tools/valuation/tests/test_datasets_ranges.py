"""Every industry figure the diagnostics show lies in a plausible range, or is dropped with a note."""

from __future__ import annotations

from valuation import datasets


def test_every_industry_figure_is_plausible_or_dropped_with_a_note():
    table = datasets.load_table("betas")
    industries = [row[table.column("Industry name")] for row in table.rows]
    assert len(industries) > 50
    for industry in industries:
        f = datasets.industry_figures(industry)
        for purpose, v in (("unlevered_beta_cash_corrected", f.unlevered_beta_cash_corrected),
                           ("cost_of_capital", f.cost_of_capital), ("sales_to_capital", f.sales_to_capital),
                           ("pretax_operating_margin", f.pretax_operating_margin),
                           ("revenue_cagr_5y", f.revenue_cagr_5y), ("effective_tax_rate", f.effective_tax_rate)):
            lo, hi = datasets.PLAUSIBLE[purpose]
            if v.value is None:
                assert v.matched_name is None or v.note, (industry, purpose)
            else:
                assert lo <= v.value <= hi, (industry, purpose, v.value)


def test_effective_tax_rate_is_the_money_making_average_not_the_aggregate():
    adv = datasets.industry_figures("Advertising").effective_tax_rate
    assert adv.value is not None and 0.25 < adv.value < 0.30              # 28.1%, not the 116.1% aggregate
    assert adv.column == "Average across only money-making companies"
    semi = datasets.industry_figures("Semiconductor").effective_tax_rate
    assert semi.value is not None and 0.10 < semi.value < 0.25


def test_placeholder_values_are_dropped_with_a_note():
    v = datasets.industry_figures("Rubber& Tires").effective_tax_rate      # his sheet holds 7.0 here
    assert v.value is None and v.note and "not meaningful" in v.note and "7.00" in v.note
