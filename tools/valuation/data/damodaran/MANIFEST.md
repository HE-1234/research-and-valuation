# Damodaran datasets (cached)

Fetched 2026-09-07 21:29 UTC by `uv run value --refresh-data`.  Source: Aswath Damodaran, NYU Stern, https://pages.stern.nyu.edu/~adamodar/New_Home_Page/data.html.  Each CSV is the data block of the named sheet, headers kept verbatim.  "Last updated" is the file's own 'Date updated:' cell (industry files) or the latest monthly row (ERP file).

| Dataset | File | URL | Fetched | Last updated in file | Rows | Columns used |
|---|---|---|---|---|---|---|
| erp | `ERPbymonth.csv` | https://pages.stern.nyu.edu/~adamodar/pc/implprem/ERPbymonth.xlsx | 2026-09-07 21:29 UTC | 2026-09-01 | 216 | date = `Start of month`; tbond = `T.Bond Rate`; erp = `ERP (T12m)` |
| betas | `betas.csv` | https://pages.stern.nyu.edu/~adamodar/pc/datasets/betas.xls | 2026-09-07 21:29 UTC | 2026-01-05 | 96 | unlevered_beta_cash_corrected = `Unlevered beta corrected for cash` |
| wacc | `wacc.csv` | https://pages.stern.nyu.edu/~adamodar/pc/datasets/wacc.xls | 2026-09-07 21:29 UTC | 2026-01-05 | 96 | cost_of_capital = `Cost of Capital` |
| capex | `capex.csv` | https://pages.stern.nyu.edu/~adamodar/pc/datasets/capex.xls | 2026-09-07 21:29 UTC | 2026-01-05 | 96 | sales_to_capital = `Sales/ Invested Capital (LTM)` |
| margin | `margin.csv` | https://pages.stern.nyu.edu/~adamodar/pc/datasets/margin.xls | 2026-09-07 21:29 UTC | 2026-01-05 | 96 | pretax_operating_margin = `Pre-tax Unadjusted Operating Margin` |
| taxrate | `taxrate.csv` | https://pages.stern.nyu.edu/~adamodar/pc/datasets/taxrate.xls | 2026-09-07 21:29 UTC | 2026-01-05 | 96 | effective_tax_rate = `Aggregate tax rate` |
| histgr | `histgr.csv` | https://pages.stern.nyu.edu/~adamodar/pc/datasets/histgr.xls | 2026-09-07 21:29 UTC | 2026-01-05 | 96 | revenue_cagr_5y = `CAGR in Revenues- Last 5 years` |

Notes:

- `histgr.xls` existed; `fundgr.xls` was not needed.
- Industry lookups are case-insensitive: exact name first, then substring; the matched name is printed in valuation.md.
- `taxrate.csv` has two `Aggregate tax rate` columns (effective, then cash); the first is used.
- The ERP row used is the last month with a date and a numeric `ERP (T12m)`; `T.Bond Rate` is the 10-year Treasury at the start of that month.
- Latest ERP row: 2026-09-01, T-bond 0.0475, ERP 0.0409.
