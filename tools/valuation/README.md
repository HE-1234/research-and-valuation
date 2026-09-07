# valuation

The free-cash-flow-to-the-firm engine described in `AGENTS.md` section 18. It reads one
file, `companies/<TICKER>/valuation/assumptions.yaml`, and writes one file,
`companies/<TICKER>/valuation/valuation.md`. The owner's judgment lives in the YAML; the
engine only does arithmetic and reports numbers.

## Running

```
uv sync                                  # once; creates .venv with pyyaml, openpyxl, xlrd, pytest
uv run value MRVL --validate             # schema check only, exit 0 or 1
uv run value MRVL --dry-run              # compute and print the results table; write nothing
uv run value MRVL                        # compute, archive the previous pair to history/, write valuation.md
uv run value MRVL --set scenarios.base.operating_margin.values.4=0.34 --set market.price=71.2
uv run value MRVL --json                 # the full result as JSON on stdout
uv run value --refresh-data              # re-download Damodaran's datasets into data/damodaran/
uv run pytest -q                         # the test suite
```

The ticker resolves to `companies/<TICKER>/valuation/assumptions.yaml` relative to the
repository root (the directory containing `AGENTS.md`, found by walking up from the current
directory). A path to a YAML file works too.

| Flag | What it does |
|---|---|
| `--validate` | Validate only. Prints every error with its dotted path, every warning, every null that stops a scenario. Exit 1 on errors or when no scenario can be computed. |
| `--dry-run` | Compute everything and print the results table and warnings; write nothing. |
| `--set PATH=VALUE` | Override a YAML cell in memory (repeatable). Dotted paths with list indices: `scenarios.base.sales_to_capital.value=2.0`, `scenarios.base.operating_margin.values.4=0.34`. Values are coerced: `null`, `true`/`false`, numbers, otherwise strings (`riskfree`, `auto`). |
| `--json` | Print the result as JSON instead of the table (assumptions omitted). |
| `--refresh-data` | Download the seven Damodaran files, rewrite the CSVs and `MANIFEST.md`, exit. |
| `--no-fetch` | No network. `auto` price and risk-free cells must then be given with `--set`; the ERP `auto` still reads the cached dataset. |

On a normal run, if `valuation.md` already exists it and `assumptions.yaml` are copied to
`valuation/history/<YYYY-MM-DD-HHMM>/` before the new file is written. The engine never
writes into `assumptions.yaml`.

Python API: `valuation.load(ticker_or_path)`, `valuation.compute(assumptions, market=None)`,
`valuation.render(result)`. `compute` fetches `auto` market cells unless a
`valuation.MarketInputs` is passed.

## The YAML

The schema is AGENTS.md section 18.4; `tests/fixtures/example_assumptions.yaml` is a complete,
valid example with made-up numbers and comments on every block. Notes beyond section 18.4:

- `scenarios.<name>.terminal.growth.value` may be the string `riskfree`, meaning "the
  risk-free rate used in this run" (the fetched FRED DGS10, or the manual
  `market.risk_free_rate`). The assumptions table shows the resolved number with the note
  "= risk-free rate". A numeric terminal growth above the run's risk-free rate stops that
  scenario unless `allow_above_riskfree: true` with a reason, in which case it computes and
  a warning is printed. When `market.risk_free_rate` is a number the same rule is checked
  statically by `--validate`.
- `diagnostics.historical_revenue_cagr` and `diagnostics.historical_operating_margin`
  (optional cells, `{value, source, reason}`) feed the "company's own history" columns of
  the diagnostics in section 18.5 item 9; nothing else in the schema carries that history.
- `switches.reinvestment_lag` (optional, `0` or `1`, default `1`) exists to reproduce
  Damodaran's 2018 Alphabet sheet, which has no lag. Section 18.3 specifies the one-year lag;
  leave the switch alone for company valuations.

Nulls: a `null` in a scenario cell stops that scenario and the report says which cell. A
`null` in a shared cell (base year, bridge, cost-of-capital build) stops every scenario.
`management.computable: false` skips the management case without error. Rates are decimals;
a rate written as a percent (`12` instead of `0.12`) is a validation error.

## Market data and datasets

- Price: Yahoo chart endpoint (`regularMarketPrice` and its timestamp), browser User-Agent,
  `query1` then `query2`.
- Risk-free rate: FRED `DGS10` CSV, latest non-empty row.
- Equity risk premium: the latest row of Damodaran's `ERPbymonth.xlsx` (`ERP (T12m)` column,
  with the month's `T.Bond Rate`), read from the cache.
- Industry figures: `betas.xls` (unlevered beta corrected for cash), `wacc.xls` (cost of
  capital), `capex.xls` (sales to invested capital), `margin.xls` (pre-tax unadjusted
  operating margin), `taxrate.xls` (aggregate effective tax rate), `histgr.xls` (five-year
  revenue CAGR; `fundgr.xls` is the fallback if `histgr.xls` disappears). Lookup by industry
  name is case-insensitive, exact first, then substring.

The cache is `data/damodaran/*.csv` plus `MANIFEST.md` (URL, fetch date, the file's own
"Date updated" cell, the exact column headers used). A failed fetch of an `auto` cell stops
the run with a message naming the `--set` override; numbers written in the YAML are used as
given and flagged in the warnings as manual values.

## How the tests reproduce Damodaran's workbooks

`tests/test_damodaran_workbooks.py` rebuilds `AlphabetApr2018.xlsx` and `NVIDIA2023.xlsx` from
their Input sheets with the engine in 10-year mode (pinned cost of capital, ten-entry growth
and margin lists, his stable ROIC as `roic_premium = ROIC - stable WACC`, cross holdings in
`non_operating_assets`, option value in `other_claims`). The inputs and his outputs were
extracted with `openpyxl` (`data_only=True`) into `tests/fixtures/damodaran_workbooks.json` by
`tests/damodaran_extract.py`, so the tests run without the workbooks; when the workbooks are
present in `/tmp/damo` the fixture is re-checked against them. Both values of operating
assets and both per-share values match his sheets to well inside 0.1% (the reproduction is
exact to floating-point precision):

| Workbook | His operating assets | His value per share | Engine |
|---|---|---|---|
| Alphabet, April 2018 | 596,872 | 968.92 | identical (relative error 0) |
| NVIDIA, June 2023 | 583,005 | 237.55 | identical (relative error 0) |

Convention differences found by reading his formulas cell by cell:

1. **Alphabet 2018 has no reinvestment lag.** Row 8 of his Valuation output is
   `(Rev_t - Rev_{t-1}) / SC`; `fcffsimpleginzu.xlsx` and section 18.3 use `(Rev_{t+1} - Rev_t) / SC`.
   The engine reproduces his sheet with `reinvestment_lag: 0`. With the section 18.3 lag his
   per-share value would be 969.85 instead of 968.92 (+0.095%), because growth fades after
   year 5 so the lagged reinvestment is smaller in every year.
2. **Alphabet 2018 taxes trapped cash** in the bridge: `101,871 - 60,000 x (25% - 15%) = 95,871`.
   The test feeds the adjusted cash; the YAML schema has no trapped-cash cell.
3. **NVIDIA 2023 is three segments** (rest of business, AI chips, auto chips) that share tax,
   cost of capital, sales-to-capital and terminal settings. Every formula is linear in revenue
   and operating income, so the sum of his three segment values equals one valuation on the
   aggregated revenue and operating-income paths. The test rebuilds his market-size, market-share
   and margin-convergence rows from the Input sheet and hands the engine the aggregate growth
   and margin lists.
4. **Margin convergence differs between his sheets.** Alphabet 2018 converges from the
   base-year margin starting in year 1; the ginzu-style NVIDIA sheet takes year 1 straight from
   the input cell and applies the convergence formula from year 2 (so the path steps twice
   between years 1 and 2). The engine takes explicit per-year lists and does not care.
5. **ROIC display.** Alphabet 2018 divides after-tax operating income by end-of-year capital;
   ginzu and the engine use start-of-year capital. This never affects value.

## Conventions where section 18 is silent (taken from `fcffsimpleginzu.xlsx`)

- After-tax operating income is `EBIT x (1 - tax)` only when EBIT is positive; a loss carries
  no tax benefit (Valuation output row 7, no NOL modelling).
- Terminal reinvestment `g / ROIC` applies only when terminal growth is positive (cell M8).
- The `g_T` of section 18.3's terminal block is the scenario's terminal growth input:
  `Rev_{T+1} = Rev_T x (1 + g_terminal)`, so the last explicit year's reinvestment is sized for
  terminal growth. In the 10-year fade this coincides with year-10 growth, as in his sheet.
- `horizon: 10` follows his structure: years 1-5 use the start tax rate, the company cost of
  capital and `sales_to_capital.value`; years 6-10 fade tax and cost of capital linearly to
  their terminal values and use `value_late`. The 10-year-fade reference shown next to every
  case is built from the first five explicit years the same way.
- Implied ROIC divides the year's after-tax operating income by invested capital at the start
  of the year, rolled forward with reinvestment (row 40). Base-year invested capital includes
  the R&D asset when `capitalize_rnd` is on (row 39).
- The R&D converter amortizes each of the last N years' R&D straight-line over N years; the
  research asset is the current year's R&D plus the unamortized part of the past years
  (sheet "R& D converter").
- Terminal-value share is `PV(terminal) / (sum of PV of cash flows + PV(terminal))`, before the
  failure adjustment.
- Sensitivity grids: the cost-of-capital axis moves the company and terminal rates together;
  the margin axis moves the year-5 margin with earlier years moving proportionally (his
  target-margin lever). The reverse DCF solves by bisection on a constant annual growth, and
  separately on the year-5 margin, for operating assets equal to today's enterprise value.
