# valuation

The free-cash-flow-to-the-firm engine described in `AGENTS.md` section 18. It reads one
file, `companies/<TICKER>/valuation/assumptions.yaml`, and writes one file,
`companies/<TICKER>/valuation/valuation.md`. The owner's judgment lives in the YAML; the
engine only does arithmetic and reports numbers.

## Running

```
uv sync                                  # once; creates .venv with pyyaml, ruamel.yaml, openpyxl, xlrd, pytest
uv run value MRVL --validate             # schema check only, exit 0 or 1
uv run value MRVL --dry-run              # compute and print the results table; write nothing
uv run value MRVL                        # compute, archive the previous pair to history/, write valuation.md and assumptions.md
uv run value MRVL --set scenarios.base.operating_margin.values.4=0.34 --set market.price=71.2
uv run value MRVL --json                 # the full result as JSON on stdout
uv run value MRVL --render-assumptions   # write assumptions.md from the YAML only; no fetch, no compute
uv run value --refresh-data              # re-download Damodaran's datasets into data/damodaran/
uv run pytest -q                         # the test suite (the app tests skip without streamlit)
uv sync --extra app                      # once; adds streamlit for the interactive app
uv run --extra app valuation-app         # start the app (section 18.10)
uv run --extra app pytest -q             # the test suite including the app tests
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
| `--render-assumptions` | Write `companies/<TICKER>/valuation/assumptions.md` from the YAML and nothing else: no market fetch, no compute, `--set` ignored. |

On a normal run, if `valuation.md` already exists it and `assumptions.yaml` are copied to
`valuation/history/<YYYY-MM-DD-HHMM>/` before the new file is written. The run also rewrites
`assumptions.md` from the YAML on disk. The engine never writes into `assumptions.yaml`.

Python API: `valuation.load(ticker_or_path)`, `valuation.compute(assumptions, market=None)`,
`valuation.render(result)`, `valuation.render_assumptions(assumptions)`. `compute` fetches
`auto` market cells unless a `valuation.MarketInputs` is passed. `valuation.cli.run_and_write`
is the normal run as one function (archive, compute, write both files); the app calls it.

## `assumptions.md`

A read-only rendering of `assumptions.yaml`, written by `--render-assumptions`, by every
normal compute run, and by every save from the app. Sections, in the order of section 18.4:
header (ticker, company, as-of quarter and date, drafted, owner edited if any), the four
stories, one table of scenario inputs (rows are inputs, columns are cases, per-year lists as
`y1 / y2 / y3 / y4 / y5`), a reasons list per scenario (`**input** — reason [source]`), then
base year and switches, bridge, market inputs, cost of capital, diagnostics inputs, the
management guidance table, and the change log when the file has one. Percentages have one
decimal, money is USD millions with separators, and an empty cell is shown as a dash.
Rendering needs only the YAML; an invalid or half-filled file still renders.

## Writing the YAML: `valuation.yamlio`

Everything that writes `assumptions.yaml` goes through `tools/valuation/yamlio.py`, built on
`ruamel.yaml` in round-trip mode, so hand-written comments, key order, block-scalar stories,
flow-style cells, quoting and the `riskfree` / `auto` sentinels survive a save. The engine's
read path stays on PyYAML; the plain dict it reads always equals `yaml.safe_load` of what
the writer saves (tested).

- `load_roundtrip(path)` returns a `Document` (data, path, snapshot of mtime and hash).
- `apply_changes(doc, [(dotted_path, value), ...])` sets cells in place, list indices allowed
  (`scenarios.base.operating_margin.values.4`), and returns `(path, old, new)` for the cells
  that actually changed. Multi-line strings stay block scalars.
- `append_changelog(doc, entries)` appends `{at, path, old, new, note}` rows to `changelog`
  (created if absent, oldest first); `set_owner_edited(doc, iso_timestamp)` sets the stamp.
- `save(doc)` writes atomically (temp file in the same directory, then rename) and refuses
  with `StaleFileError` when the file changed since it was loaded.
- `diff_against_file(path, current_plain_dict)` lists changed paths with the file value and
  the current value; the app's unsaved-changes list and Save are built on it.

Analysts never write `owner_edited` or `changelog`; the app maintains them. Where ruamel
cannot keep a layout exactly (column-aligned flow mappings, flow mappings split over two
lines) it writes the same mapping on one line; nothing else changes.

## The app (`valuation-app`)

```
uv sync --extra app                      # once
uv run --extra app valuation-app         # opens http://localhost:8501; extra args go to `streamlit run`
uv run --extra app valuation-app --server.port 8502
```

The engine never needs streamlit: `uv run value ...` and `uv run pytest -q` work without the
`app` extra (the app tests then skip). The page is a view and an editor of one company's
`assumptions.yaml`; it holds no arithmetic and calls `valuation.compute`, `valuation.render`,
`valuation.render_assumptions` and `valuation.yamlio`.

Layout:

- **Sidebar.** Company picker over `companies/*/valuation/assumptions.yaml`. Market inputs:
  the price (Yahoo), risk-free rate (FRED) and equity risk premium (cached Damodaran row) are
  fetched once per company per session (15-minute cache) and shown with their dates; each has
  an override box, and when a fetch fails the box is empty and asks for a value instead of
  crashing. Horizon 5 or 10 (switching pads or cuts every per-year list and says so). The
  unsaved-changes list (path, file value, current value). Buttons:
  - **Reset to file** reloads the YAML and drops every unsaved edit.
  - **Save to assumptions.yaml** writes only the changed cells through the ruamel writer,
    appends one `changelog` entry per cell (with the optional one-line note typed above the
    buttons), sets `owner_edited`, and regenerates `assumptions.md`. Reasons and sources are
    written only if you edited them; comments and key order are kept. If the file changed on
    disk since it was loaded (an agent redraft, for instance), Save refuses and asks for a
    reload.
  - **Write valuation.md** runs the same code path as `uv run value <TICKER>` with the
    sidebar's market inputs: archives the current pair to `history/<YYYY-MM-DD-HHMM>/`,
    computes, writes `valuation.md` and `assumptions.md`. Refused while changes are unsaved.
  - **Commit** runs `git add companies/<T>/valuation` and commits as `company-research`
    with `value(<T>): compute <QLABEL> rev N` (N = history folders + 1) when `valuation.md`
    changed, or `value(<T>): owner edits to assumptions` when only the YAML and its rendering
    changed. Output is shown on the page. It never pushes.
- **Top of page.** The section 18.5 results table (one row per case plus the weighted row)
  and a bar chart of bear / base / bull / weighted value per share with the price as a dashed
  line and each bar labelled with its 10-year-fade reference.
- **Tabs.** `Bear`, `Base`, `Bull`: the story in a text box, the weight, a by-year table
  (revenue growth, operating margin, reinvestment override; decimals, `0.12` means 12%), and
  one row per single-value input with the reason next to it and the source read-only.
  `Management`: the computable switch with its reason, the guidance table read-only, and the
  same inputs with nulls visible. `Base year & bridge` and `Cost of capital`: sourced facts as
  tables, editable after the "Edit facts" toggle, with the derived numbers (adjusted operating
  income, invested capital, levered beta, cost of equity, WACC, terminal WACC, terminal ROIC
  per case) live. `Sensitivity`: both grids as heatmaps with the case as entered outlined.
  `Year by year` (with a case selector), `Reverse DCF`, `Diagnostics`, `Warnings`.

Every change recomputes at once. A change that stops a scenario (a null in a required cell,
terminal growth at or above the terminal cost of capital) shows the engine's message in place
of that case's numbers; the page never shows a stack trace.

Environment variables for tests and scripts: `VALUATION_REPO_ROOT` points the app at another
repository root; `VALUATION_APP_NO_FETCH=1` turns fetching off.

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
