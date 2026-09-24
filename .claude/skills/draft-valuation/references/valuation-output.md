# Valuation report requirements

Read when computing or changing the report renderer. The [reader rules](../../../../docs/research.md#section-3) apply to report prose. These output requirements do not authorize computation before the [draft review boundary](workflow-contracts.md#draft-review-boundary).

<a id="section-18-5"></a>

## 18.5 Outputs (`valuation.md`, rendered by the engine)

In this order:

1. Header: ticker, as-of quarter, price and its date, risk-free rate and its date, equity risk premium and its date, compute timestamp, engine version.
2. **Results table**, one row per case (bear, base, bull, management if computable, weighted expected): value of operating assets, enterprise value today, equity value, value per share, price, upside or downside, terminal-value share of operating assets, and the reference value per share from the other structure (the 5-year stop when `horizon` is 10; the 10-year fade when it is 5).
3. **The stories**, one short section per scenario, verbatim from the YAML.
4. **Assumptions table**: rows are inputs, columns are cases, per-year lists shown as five columns; followed by a reasoning list per scenario (each cell's `reason` and `source`).
5. **Base year, bridge, cost of capital, and terminal tables** with sources and the derived numbers (adjusted operating income, levered beta, cost of equity, WACC, terminal WACC, terminal ROIC).
6. **Base-case year-by-year table**: one row per model year (ten by default, the fade years marked "by rule"), then the terminal year: revenue, growth, margin, after-tax operating income, reinvestment, free cash flow, discount factor, present value, implied ROIC.
7. **Sensitivity grids** for the base case: cost of capital × terminal growth; average 5-year revenue growth × year-5 margin. Value per share in each cell; the base-case cell marked.
8. **Reverse DCF**: the constant annual revenue growth over the horizon that, with base-case margins, reinvestment, cost of capital, and terminal settings, makes operating assets equal today's enterprise value. Also the year-5 margin that does the same at base-case growth.
9. **Diagnostics** (Damodaran's six plus the transition check): revenue growth vs industry average and the company's own five-year history (labelled as context, not an anchor, per [assumptions rule 11](assumptions-spec.md#section-18-4)); final-model-year revenue vs `final_year_market_size` (year 10 by default; the analyst's `detail` also shows the nearer year the sources actually give); year-5 margin vs industry average and own history; implied ROIC path vs cost of capital; terminal-value share; a flag when value per share is above 2× or below 0.5× the price; and the [§18.2](model-spec.md#section-18-2) transition check (terminal-year free cash flow and return on capital against the final explicit year, flagged on a cliff). Industry figures come from the cached datasets ([§18.8](model-spec.md#section-18-8)) and are labelled with their dataset date.
10. **Warnings**: every rule override, every `null` that stopped a scenario, any fetch that fell back to a manual value.
11. Glossary and Sources (the YAML's source tags mapped to cached files, plus dataset and feed URLs with fetch dates).
