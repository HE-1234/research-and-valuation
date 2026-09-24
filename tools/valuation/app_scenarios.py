"""Readable scenario inputs, bound to the working assumptions rather than free-text mappings."""
from __future__ import annotations

import math
import re
from typing import Any

import pandas as pd
import streamlit as st

from valuation.app_core import (
    CASE_LABELS, bump_gen, md, money, num, pct, pct2, per_share, set_in, static_table, w_pct, working,
)
from valuation.app_workspace import saved_comparison
from valuation.schema import WEIGHTED_SCENARIOS, get_path



DEFAULT_SCENARIO_WEIGHTS = {"bear": 0.25, "base": 0.50, "bull": 0.25}


def reset_scenario_weights() -> None:
    """Apply the house mix only on request; preserve every other working assumption."""
    for name, weight in DEFAULT_SCENARIO_WEIGHTS.items():
        path = f"scenarios.{name}.weight"
        set_in(working(), path, weight)
        st.session_state.setdefault("input_errors", {}).pop(path, None)
    bump_gen()


def weight_status(doc) -> bool:
    """Use the same visible validity check on both pages; engine validation remains authoritative."""
    weights = [get_path(doc, f"scenarios.{name}.weight") for name in WEIGHTED_SCENARIOS]
    if any(isinstance(w, bool) or not isinstance(w, (int, float)) or not math.isfinite(w) for w in weights):
        st.error("Enter a weight for each case. Together they must add up to 100%.")
        return False
    if any(w < 0 or w > 1 for w in weights):
        st.error("Each case weight must be between 0% and 100%.")
        return False
    total = sum(weights)
    line = f"Weights add up to {pct(total, 1)}."
    if abs(total - 1.0) > 1e-6:
        st.error(line + " They must add up to 100% before the model computes.")
        return False
    st.markdown(f"**{line}**")
    return True


def scenario_weights(ctx) -> None:
    """Keep the probability choices beside the stories, with the existing bound widgets."""
    doc = ctx.doc
    with st.container(border=True):
        st.subheader("How likely is each scenario?")
        st.markdown("Set the weight you give each story. The default is 25% bear, 50% base, and 25% bull; "
                    "your saved choices stay in place until you edit them. Management is not weighted.")
        for name, column in zip(WEIGHTED_SCENARIOS, st.columns(3)):
            with column:
                w_pct(doc, f"scenarios.{name}.weight", f"{CASE_LABELS[name]} weight (%)", digits=1, step=5.0,
                      help="Your probability for this story. The three weights must add up to 100%.")
                saved_comparison(f"scenarios.{name}.weight")
        valid = weight_status(doc)
        if valid and ctx.result and ctx.result.weighted:
            st.caption(f"Current weighted value: USD {per_share(ctx.result.weighted.per_share)} per share.")
        at_default = all(get_path(doc, f"scenarios.{name}.weight") == weight
                         for name, weight in DEFAULT_SCENARIO_WEIGHTS.items())
        st.button("Reset weights to 25 / 50 / 25", key="reset_scenario_weights", disabled=at_default,
                  on_click=reset_scenario_weights)
        st.caption("These are judgment weights, not measured odds. Changes also appear on Taxes and weights. "
                   "Use Review & save to keep them.")


def readable_driver(text: Any) -> str:
    """Translate recorded field references without trying to pair arbitrary prose with numbers."""
    value = str(text or 'Input not specified')
    replacements = {
        'terminal.roic_premium.value': 'Terminal return premium',
        'terminal.roic_premium': 'Terminal return premium',
        'terminal.growth.value': 'Terminal growth', 'terminal.growth': 'Terminal growth',
        'revenue_growth.values': 'Revenue growth', 'revenue_growth': 'Revenue growth',
        'operating_margin.values': 'Operating margin', 'operating_margin': 'Operating margin',
        'reinvestment_override.values': 'Net reinvestment', 'reinvestment_override': 'Net reinvestment',
        'sales_to_capital.value_late': 'Sales-to-capital, years 6-10',
        'sales_to_capital.value': 'Sales-to-capital, years 1-5',
        'sales_to_capital': 'Sales-to-capital',
        'tax_rate.start': 'Tax rate, years 1-5', 'tax_rate.terminal': 'Terminal tax rate',
        'tax_rate': 'Tax rate', 'cost_of_capital': 'Cost of capital',
        'value_late': 'years 6-10',
    }
    for old, new in replacements.items():
        value = value.replace(old, new)
    return re.sub(r'\s+', ' ', value).strip()


def scenario_input_tables(doc, name: str, horizon: int, resolved=None, market=None):
    """Five-year-wide tables. Missing guidance stays missing; resolved fades are clearly labelled."""
    scenario = get_path(doc, f'scenarios.{name}') or {}
    rows = resolved.rows if resolved else []
    growth = get_path(scenario, 'revenue_growth.values') or []
    margin = get_path(scenario, 'operating_margin.values') or []
    spending = get_path(scenario, 'reinvestment_override.values') or []

    def annual(values, index, attr):
        if index < len(rows):
            return pct(getattr(rows[index], attr))
        if index < len(values):
            return pct(values[index]) if values[index] is not None else 'Not supplied'
        return 'By rule' if values and values[-1] is not None else 'Not supplied'

    tables = []
    for start in range(0, horizon, 5):
        periods = list(range(start, min(start + 5, horizon)))
        columns = ['Variable'] + [f'Year {i + 1}' for i in periods]
        data = [
            ['Revenue growth'] + [annual(growth, i, 'growth') for i in periods],
            ['Forecast revenue (USD millions)'] + [money(rows[i].revenue) if i < len(rows) else 'Unavailable' for i in periods],
            ['Operating margin'] + [annual(margin, i, 'margin') for i in periods],
            ['Net reinvestment (USD millions)'] + [money(spending[i]) if i < len(spending) and spending[i] is not None
                                                  else 'Use ratio' for i in periods],
            ['Sales-to-capital (times)'] + [num(get_path(scenario, 'sales_to_capital.' + ('value' if i < 5 else 'value_late')))
                                          for i in periods],
            ['Tax rate'] + [(pct(rows[i].tax_rate) if i < len(rows) else
                            pct(get_path(scenario, 'tax_rate.start')) if i < 5 else
                            pct(get_path(scenario, 'tax_rate.terminal')) if i == horizon - 1 else 'By rule')
                           for i in periods],
        ]
        tables.append((f'Years {start + 1}-{periods[-1] + 1}', pd.DataFrame(data, columns=columns)))
    terminal_growth = get_path(scenario, 'terminal.growth.value')
    if terminal_growth == 'riskfree':
        growth_text = (pct2(market.risk_free_rate) + ' (risk-free rate)') if market else 'Risk-free rate'
    else:
        growth_text = pct2(terminal_growth)
    premium = get_path(scenario, 'terminal.roic_premium.value')
    settings = [
        ['Case weight', pct(scenario.get('weight')) if name != 'management' else 'Not weighted'],
        ['Terminal growth', growth_text],
        ['Terminal return premium', 'Not supplied' if premium is None else num(premium * 100, 1) + ' percentage points'],
        ['Terminal tax rate', pct(get_path(scenario, 'tax_rate.terminal'))],
        ['Cost of capital, year 1', pct2(rows[0].wacc) if rows else
         pct2(scenario.get('cost_of_capital_override')) if scenario.get('cost_of_capital_override') is not None else 'Shared model rate'],
        ['Terminal cost of capital', pct2(resolved.terminal.wacc) if resolved else 'Shared terminal setting'],
    ]
    return tables, pd.DataFrame(settings, columns=['Variable', 'Chosen value'])


def story_assumptions(ctx, name: str) -> None:
    st.markdown('**Current assumptions for this story**')
    st.caption('One variable per row; one forecast year per column. These values follow your current edits. '
               'Forecast revenue is calculated from the growth path. Year 1 is the first forecast year, not necessarily a calendar year.')
    resolved = ctx.result.scenarios.get(name) if ctx.result else None
    tables, settings = scenario_input_tables(ctx.doc, name, ctx.T, resolved, ctx.market)
    for title, table in tables:
        st.markdown('**' + title + '**')
        static_table(table)
    st.caption('Use ratio means the sales-to-capital assumption sizes reinvestment. A spending amount replaces '
               'that ratio for the year. Later years may follow the model’s fade rules; the factor pages show the method.')
    st.markdown('**Case and terminal settings**')
    static_table(settings)
    mappings = get_path(ctx.doc, f'scenarios.{name}.story_to_numbers') or []
    if not isinstance(mappings, list):
        return
    st.markdown('**How this story becomes numbers**')
    st.caption('The analyst’s recorded reasons link to the labelled variables above. Editing a value does not rewrite its original reason.')
    for index, row in enumerate(mappings, 1):
        if not isinstance(row, dict):
            continue
        st.markdown(f'**{index}.** ' + md(row.get('says') or 'No reason recorded.'))
        st.markdown('**Supports:** ' + md(readable_driver(row.get('drives'))))
        if row.get('source'):
            st.caption('Source: ' + md(row['source']))
    with st.expander('Original analyst numbers and mapping notes'):
        st.caption('Saved narrative annotations, preserved for reference. They may contain intermediate calculations '
                   'or differ from your edits; the current assumption tables above show the values used now.')
        for index, row in enumerate(mappings, 1):
            if isinstance(row, dict):
                st.markdown(f'**{index}. ' + md(readable_driver(row.get('drives'))) + '**')
                st.markdown(md(row.get('number') if row.get('number') is not None else 'Not supplied'))
