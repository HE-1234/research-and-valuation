# valuation

The free-cash-flow-to-the-firm engine described in the [model specification](../../.claude/skills/draft-valuation/references/model-spec.md). It reads one
file, `companies/<TICKER>/valuation/assumptions.yaml`, and writes one file,
`companies/<TICKER>/valuation/valuation.md`. The owner's judgment lives in the YAML; the
engine only does arithmetic and reports numbers.

## Running

```
uv sync                                  # once; creates .venv with pyyaml, ruamel.yaml, openpyxl, xlrd, pytest
uv run value MRVL --validate             # schema check only, exit 0 or 1
uv run value MRVL --dry-run              # compute and print the results table; write nothing
uv run value MRVL --diagnostics-only     # draft-review JSON, no valuation results; write nothing
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
| `--diagnostics-only` | Compute internally and print only draft-review JSON: market inputs/dates, base year, cost of capital, industry comparisons, operating cash flows and returns by year, transition checks, stopped/skipped cases, and warnings. No valuation results or file writes. |
| `--set PATH=VALUE` | Override a YAML cell in memory (repeatable). Dotted paths with list indices: `scenarios.base.sales_to_capital.value=2.0`, `scenarios.base.operating_margin.values.4=0.34`. Values are coerced: `null`, `true`/`false`, numbers, otherwise strings (`riskfree`, `auto`). |
| `--json` | Print the result as JSON instead of the table (assumptions omitted). |
| `--refresh-data` | Download the seven Damodaran files, rewrite the CSVs and `MANIFEST.md`, exit. |
| `--no-fetch` | No network. `auto` price and risk-free cells must then be given with `--set`; the ERP `auto` still reads the cached dataset. |
| `--render-assumptions` | Write `companies/<TICKER>/valuation/assumptions.md` from the YAML and nothing else: no market fetch, no compute, `--set` ignored. |

Use `--diagnostics-only` during drafting. Its output excludes computed asset/equity/per-share
values, present values, terminal-value share, price-relative valuation ratios, reference
valuations, sensitivities and reverse DCF. `--set` and `--no-fetch` still work. Adding
`--json` or `--dry-run` keeps the restricted output; combinations with `--validate`,
`--refresh-data`, or `--render-assumptions` are rejected before any file access or fetch.
Ordinary `--dry-run` and full `--json` expose valuation results and belong after owner review.
For a requested compute dry run, `--dry-run --json` provides the current result and market
metadata without requiring a saved `valuation.md`. Validation applies supplied `--set`
overrides before checking inputs; it never saves those overrides.

Rate units follow [the assumptions specification](../../.claude/skills/draft-valuation/references/assumptions-spec.md#section-18-4): YAML and `--set` use decimal fractions
(`0.12` = 12%, `1.20` = 120%); the app's percentage fields convert for display and entry.
A return premium of `0.08` adds 8 percentage points to the cost of capital.
Finite premiums at or above `1.0` require `allow_large_premium: true` and a reason,
just like other premiums above the case's warning threshold. The warning remains;
other rate bounds are unchanged. Bear may retain a supported positive terminal premium;
its large-premium warning threshold is 8 points, the same as base. Zero remains allowed,
and all scenarios receive the same transition diagnostics. Existing inputs are not migrated.

To fetch a price while drafting before the valuation inputs are ready, call the market
API directly (the output is a price and timestamp, not a valuation):

```sh
uv run python -c 'import sys; from valuation.market import fetch_price; print(fetch_price(sys.argv[1]))' MRVL
```

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

Analysts never write `owner_edited` or `changelog`; the app maintains them. An authorized
redraft copies the active files byte-for-byte to a unique history directory, prepares a
separate candidate, and promotes it only after PASS and a check for intervening owner edits
([§18.7](../../.claude/skills/draft-valuation/references/workflow-contracts.md#section-18-7)). Copying snapshots does not rewrite YAML. Where ruamel
cannot keep a layout exactly (column-aligned flow mappings, flow mappings split over two
lines) it writes the same mapping on one line; nothing else changes.

## The app (`valuation-app`): a guided walk through the assumptions

```
uv sync --extra app                      # once
uv run --extra app valuation-app         # opens http://localhost:8501; extra args go to `streamlit run`
uv run --extra app valuation-app --server.port 8502
```

The app is local-only: the launcher binds Streamlit to `127.0.0.1` (not reachable from other
machines), opens the browser and silences Streamlit's usage-statistics prompt. Each default can be
overridden by passing the same option, for example `--server.address 0.0.0.0` to expose it on the
network or `--server.headless true` to run without a browser.

The engine never needs streamlit: `uv run value ...` and `uv run pytest -q` work without the
`app` extra (the app tests then skip). The app is a view and an editor of one company's
`assumptions.yaml`; it holds no arithmetic and calls `valuation.compute`, `valuation.impact`,
`valuation.render`, `valuation.render_assumptions` and `valuation.yamlio`. Code: `app.py`
(routing), `app_core.py` (state, widgets, callbacks, charts), `app_pages.py` (one function per
page), `impact.py` (the factor ranking, engine-side and tested).

**Shape (section 18.10).** Fifteen focused pages in a Mercury-inspired workspace: white canvas, quiet sidebar, indigo accents and readable text. Choose any page from grouped sidebar navigation, or follow Back and Next. The company picker is always available. From the factor pages onward, a compact live-value strip keeps the selected case, change since load, market price and quick review/save nearby. Edits persist across navigation and reach disk only when explicitly saved.

| Page | Purpose |
|---|---|
| Overview | As-of dates, market inputs and sources, forecast length, impact ranking and glossary. |
| Scenarios | Three compact path comparisons followed by full-width stories, story-to-number links and expandable editors; management case below. |
| Revenue growth | History, full analyst reasons, annual inputs, automatic fade and scoped reset. |
| Operating margin | The same layout for the margin path. |
| Reinvestment, Cost of capital, Terminal value, Taxes and weights | Four dedicated factor pages in the company's computed impact order. |
| Source facts | Source-linked base-year figures and bridge, with an explicit Edit facts control. |
| Valuation | Case comparison, weighted value and chart against market price, with the other forecast horizon as reference. |
| Analysis | Sensitivity grids and the growth or margin implied by the market price. |
| Cash flow forecast | Case selection and year-by-year results, split into readable sales/profit and cash-flow tables. |
| Simulation | Existing Monte Carlo settings, run, results and reproducible export. |
| Model checks | Diagnostics, transition checks and warnings. |
| Review & save | Unsaved changes, note, Save, Write the report, Record in the repository and guarded Start over. |

**Scenario values.** Each story has current input matrices with one variable per row and up to five year columns, followed by case/terminal settings. Rates are percentages, reinvestment and calculated sales are USD millions, and capital efficiency is a ratio. The matrices read the working assumptions and resolved model path, so owner edits update them. Narrative reasons and sources remain visible; saved free-text number annotations are retained in a clearly labelled reference expander. Management guidance is presented separately with its original classification and coverage limits.

**Weights and sources.** Scenarios has editable bear/base/bull weights and a reset to 25/50/25. Saved choices are preserved; both weight pages share the same edits and require a 100% total. Use Review & save to keep changes. Citation links open a separate evidence view with highlighted exact quotations or retained citation locators. The original document, complete cached text and download remain available. Document-only references state their precision limit and provide phrase search; ambiguous headings remain candidates. Cached file paths open the whole document. Unknown or missing evidence is never given a guessed destination.

**ROIC comparison.** Reinvestment and Operating margin show historical returns and the return implied by each case. The quick identity combines each year's after-tax margin and sales-to-capital ratio; because the model uses that ratio for new investment, it is a diagnostic rather than the forecast's return on total capital. The forecast column reuses the engine's opening-capital calculation and respects spending overrides. Historical evidence lives in each company's optional `valuation/historical-roic.yaml`, separately from owner assumptions; incomplete or future-dated evidence is labelled unavailable. See [the calculation note](damodaran-notes/2026-09-11-roic-comparison.md).

**Motion.** Navigation uses one brief fade and lift, buttons respond to hover and press, and explanations fade in when opened. Input recalculation leaves the page and financial figures steady. Reduced-motion preferences disable these effects.

**Every factor page, top to bottom:** (a) a two-to-four-sentence explanation for the
16-year-old (what the factor is, why it moves the value, how Damodaran treats it) and a
one-line instruction; (b) the company's own history where the YAML carries it
(`diagnostics.historical_revenue_cagr` / `historical_operating_margin`), nothing otherwise;
(c) one bordered block per case in the order bear, base, bull, management (management only when
`computable: true`; otherwise a one-line note saying why it is not computed, with the recorded
guidance in an expander on the revenue and margin pages); each block shows the case name and
weight, the reason in full as normal text, a "Working notes" fold-out when the cell carries a
`detail` (pipe tables render as tables and whitespace-aligned columns as a preformatted block), the source tags in small text (only when there is a source), and the inputs prefilled
with the analyst's values; (d) the live readout "With your current inputs: Bear X / Base Y /
Bull Z / Weighted W per share, against a price of P", each value followed by "(as loaded ...)"
once it differs from the file, and "not computed (see its box)" for a case that stops; (e) Back
and Next. Moving to another page scrolls to its top.

**Screen language.** The owner never sees dotted paths, YAML keys, `--set`, option tokens or
section citations: every engine and validator message goes through `plain_message()` (cases
named, rates as percentages, checkbox names quoted, for example "Bull case: terminal growth
6.00% is above the risk-free rate 4.75%; tick 'Allow growth above the risk-free rate' on the
Terminal value page or lower the number"), every cell is named by `describe_path()` ("Base
case, revenue growth, Year 1"), and text from the YAML goes through `md()`, which also maps
stray keys, section signs and maths symbols in analysts' reasons to words.

**The ranking** (`impact.py`, `impact_ranking(doc, market)`). For the base case as loaded,
each factor gets one plausible nudge and the change in value per share is recorded: revenue
growth +1 point in every explicit year; operating margin +1 point every year; sales-to-capital
+10% of its value (and per-year overrides +10%); cost of capital +0.5 point; terminal growth
+0.25 point, capped at the risk-free rate (so -0.25 point when already at the cap); terminal
return-on-capital premium +1 point; tax rate in the forecast years +1 point. Weights are
excluded because they change no case's value. The list is sorted by absolute change; the
middle pages follow it, with revenue growth and operating margin fixed as pages 3 and 4. The
ranking is recomputed on load, on Save and when a market input changes.

**Formatting rules.** No LaTeX and no `$` in the app's own text (Streamlit reads `$...$` as a
formula; the pages write "USD"); text from the YAML (reasons, quotes, engine messages) is
escaped so it shows literally. No Unicode math symbols. One rule per kind: growth, margins,
taxes, weights and shares of value carry one decimal; market-style rates (risk-free, premiums,
cost of capital, terminal growth) carry two; rates are typed as percentages (12.0 means 0.12
in the YAML, the conversion happens in the widget callback). Money in USD millions with
thousands separators; shares in millions with one decimal; value per share and price to the
cent. Summary tables use `st.table` (they wrap and never scroll). Per-case blocks are bordered
containers; nothing is hidden behind a hover.

**Buttons on Review & save.**

- **Save to the assumptions file** writes only the changed cells through the ruamel writer,
  appends one `changelog` entry per cell (with the optional one-line note typed above the
  buttons), sets `owner_edited`, and regenerates `assumptions.md`. Comments and key order are
  kept. If the file changed on disk since it was loaded (an agent redraft, for instance), Save
  refuses and asks for a reload. Disabled while there is nothing to save.
- **Write the report (valuation.md)** runs the same code path as `uv run value <TICKER>` with
  the Start page's market inputs: archives the current pair to `history/<YYYY-MM-DD-HHMM>/`,
  computes, writes `valuation.md` and `assumptions.md`. Disabled while changes are unsaved.
- **Record in the repository** runs `git add companies/<T>/valuation` and commits as `company-research` with
  `value(<T>): compute <QLABEL> rev N` (N = history folders + 1) when `valuation.md` changed,
  or `value(<T>): owner edits to assumptions` when only the YAML and its rendering changed.
  Output is shown on the page. It never pushes.
- **Start over** (in its own expander at the bottom) reloads the file from disk and returns to
  Start; with unsaved changes it asks for confirmation first.
- If the file changes on disk while the walk is open (an agent redraft, a save from another
  session), every page shows one banner, Save and Write are disabled, the file's edits are not listed
  as unsaved changes, and Start over reloads the new file.

A change that stops a scenario (a null in a required cell, terminal growth at or above the
terminal cost of capital) shows the engine's message in place of that case's number; the
page never shows a stack trace.

Environment variables for tests and scripts: `VALUATION_REPO_ROOT` points the app at another
repository root; `VALUATION_APP_NO_FETCH=1` turns fetching off.

## Monte Carlo simulation

Open **Simulation** in the sidebar, choose one computable case, enter your
ranges and their reasons, set the draw count and seed, then click **Run simulation**. This
uses the current working assumptions, including unsaved edits. Nothing is fetched or saved
by a simulation. Changing assumptions, market inputs, the case or settings hides the old
distribution until you rerun. Settings survive page navigation in the session; reloading the
company resets them. **Download simulation and all draws** preserves the settings, reasons,
full starting snapshot, every attempted draw, errors and summary in JSON. Save and Write the
report continue to apply only to the deterministic valuation.

The three triangular distributions are **user judgments, not calibrated company models**.
Minimum and maximum are hard support bounds; most likely is the mode, not the mean or
median. The initial shifts are all zero and the multiplier is one, so the first run exactly
reproduces the chosen case. No nonzero spread or correlation is supplied or inferred from
the bear/base/bull cases. Record support from relevant operating evidence, comparable
definitions, forecast errors or explicit exploratory judgment in the reason fields.

| Uncertain input | Transformation in each draw |
|---|---|
| Revenue-growth shift | One percentage-point shift across the authored growth path. A five-year path's automatic years 6–10 are rebuilt to reach the original terminal growth. A written ten-year growth path keeps its shape. |
| Year-5 margin shift | One fifth of the shift in year 1, rising to the whole shift in year 5 and later. A separately shaped ten-year margin path is preserved. Terminal margin follows the final forecast margin, as in the existing engine. |
| Capital-efficiency multiplier | Multiplies early and late sales-to-capital together. The engine derives reinvestment from sampled revenue and these ratios using the original lag. Absolute spending overrides stay fixed and are identified in the UI. |

Each driver is drawn once for the entire forecast, expressing persistent operating
uncertainty rather than annual noise. Margin and capital efficiency can use independent
draws, the same rank as growth, or the opposite rank. Independence is an explicit model
choice; rank links impose perfect positive/negative rank dependence, not fitted Pearson
correlations. Two drivers linked to growth are also dependent on one another. Rank links
require nondegenerate growth uncertainty, avoiding a hidden common factor when growth is
fixed. Pick dependencies for a business mechanism, or vary one driver at a time.

Taxes, financing, terminal growth, terminal ROIC premium, base-year facts, bridge and
distress adjustment stay fixed. Terminal ROIC remains terminal WACC plus the premium, and
positive terminal growth still incurs reinvestment at growth divided by ROIC. The simulation
does not independently sample cash flows, reinvestment, ROIC, terminal value, share price or
default events. Fixed commitments and broad software bounds cannot guarantee that a draw
fits a company's capacity, market size or competitive story; those remain owner judgments.

The histogram, mean, median, 10th/90th percentiles, population standard deviation, observed
extremes and frequency above current price are conditional on **valid draws and the selected
assumptions**. Percentiles use linear interpolation at `(n - 1) * p` (inclusive/type 7).
These are assumption-based valuation ranges, not statistical confidence intervals, forecasts
of traded share prices, or probabilities of making money. An asymmetric triangle can change
expected inputs, and a nonlinear DCF's mean need not equal the deterministic value. More draws
reduce Monte Carlo noise, not model uncertainty.

The simulator attempts exactly the requested draw count (1–20,000). Known model/arithmetic
failures and nonfinite results are recorded with inputs and reasons; there is no clipping,
silent omission or replacement sampling. Valid-only summaries can be biased when some draws
fail, so counts and this limitation appear beside results. All-invalid runs show no statistics.
Finite negative equity residuals remain in the distribution with an explanation. Existing
terminal-transition warnings are counted for every case, including bear, without
rejecting flagged observations. JSON represents any nonfinite failed input as an explicit
`nonfinite:...` string; valid numerical outputs are always finite.

The reusable API takes an already computed valuation, so its market snapshot and existing
engine logic are reused:

```python
from valuation import compute, load, simulate, SimulationSettings, Triangle

valuation = compute(load("GOOGL"))  # normal existing compute/market workflow
run = simulate(valuation, SimulationSettings(scenario="base", draws=2000, seed=42))
# All ranges above are initially fixed; set Triangle(minimum, mode, maximum, reason)
# for growth_shift / margin_shift (decimal shifts) and capital_multiplier (unit multiplier).
print(run.summary)
payload = run.to_json()            # no implicit write
```

`valuation.simulation.sample_inputs` transforms a resolved path; `simulate` calls the
existing `engine.run_scenario` for every valid candidate. It uses a local seeded Python RNG
and inverse triangular CDFs. Reproducibility requires the same input snapshot, settings and
model/runtime version. The result records the engine and simulation model versions, input
fingerprint and timestamp. `histogram(run)` exposes the chart's bin counts for reconciliation.
See [method findings and primary references](damodaran-notes/2026-09-10-monte-carlo.md).

## The YAML

The schema is [the assumptions specification](../../.claude/skills/draft-valuation/references/assumptions-spec.md#section-18-4); `tests/fixtures/example_assumptions.yaml` is a complete,
valid example with made-up numbers and comments on every block. Notes beyond section 18.4:

- `scenarios.<name>.terminal.growth.value` may be the string `riskfree`, meaning "the
  risk-free rate used in this run" (the fetched FRED DGS10, or the manual
  `market.risk_free_rate`). The assumptions table shows the resolved number with the note
  "= risk-free rate". A numeric terminal growth above the run's risk-free rate stops that
  scenario unless `allow_above_riskfree: true` with a reason, in which case it computes and
  a warning is printed. When `market.risk_free_rate` is a number the same rule is checked
  statically by `--validate`.
- Any input cell may carry `detail`: the working notes behind a short `reason` (history
  tables, arithmetic). The validator accepts it silently, the app shows it in a "Working notes"
  fold-out under the reason, and `assumptions.md` prints it as an indented paragraph after the
  reason.
- `scenarios.<name>.story_to_numbers` (section 18.4 rule 14) is a list of rows
  `{says, drives, number[, source]}`: a sentence of the story, the input it sets, and the number
  as written in that input. It is Damodaran's own story-to-numbers table. The validator warns
  when a computed case has none (older drafts predate the rule) and errors on a malformed row;
  `assumptions.md` prints it under the story and the app shows it on the stories page.
- `diagnostics.historical_revenue_cagr` and `diagnostics.historical_operating_margin`
  (optional cells, `{value, source, reason}`) feed the "company's own history" columns of
  the diagnostics in section 18.5 item 9; nothing else in the schema carries that history.
- `switches.reinvestment_lag` (optional, `0`, `1`, `2` or `3`, default `1`) is how many years
  ahead a year's spending buys growth: year `t` reinvests `(Rev_{t+lag} - Rev_{t+lag-1}) / S/C`.
  `1` is section 18.3's convention and his ginzu default; `0` reproduces his 2018 Alphabet sheet,
  which has no lag; he used `3` for Nvidia in 2024-25. Anything else is a validation error, and
  any value other than `1` prints a warning. Leave the switch alone unless the company's assets
  take longer than a year to earn anything.
- `horizon` (optional, `5` or `10`, **default `10`**) is section 18.2's structure. At `10` the
  per-year lists may hold five entries (years 1-5 judged, years 6-10 by rule) or ten (the fade
  years shaped by hand); at `5` they hold five and the model stops at year 5. Any other length is
  a validation error naming what the horizon accepts. Whichever horizon a file carries, the other
  structure is computed as a reference value next to every case.

Nulls: a `null` in a scenario cell stops that scenario and the report says which cell. A
`null` in a shared cell (base year, bridge, cost-of-capital build) stops every scenario.
`management.computable: false` skips the management case without error. Rates are decimals;
a rate written as a percent (`12` instead of `0.12`) is a validation error.

## Market data and datasets

- Price: Yahoo chart endpoint (`regularMarketPrice` and its timestamp), browser User-Agent,
  `query1` then `query2`.
- Risk-free rate: FRED `DGS10` CSV, latest non-empty row, with a 20-second timeout and one retry. The
  request identifies itself plainly (`finance-valuation/<version> (python urllib)`): FRED throttles
  browser-style User-Agents coming from scripts, so the browser header is used for Yahoo only.
  If FRED is still unreachable (or fetching is off), the T-bond rate on the latest row of the cached
  `ERPbymonth.csv` is used instead, labelled `Damodaran ERPbymonth T-bond rate (FRED unavailable)`
  with that row's date, and a warning says so; neither the CLI nor the app stalls on FRED. The app's
  Start page shows the fallback as a normal value with a small note and keeps the override box.
- Equity risk premium: the latest row of Damodaran's `ERPbymonth.xlsx` (`ERP (T12m)` column,
  with the month's `T.Bond Rate`), read from the cache.
- Industry figures: `betas.xls` (unlevered beta corrected for cash), `wacc.xls` (cost of
  capital), `capex.xls` (sales to invested capital), `margin.xls` (pre-tax unadjusted
  operating margin), `taxrate.xls` (effective tax rate, average across money-making companies;
  the aggregate column exceeds 100% for some industries and is not used), `histgr.xls` (five-year
  revenue CAGR; `fundgr.xls` is the fallback if `histgr.xls` disappears). Lookup by industry
  name is case-insensitive, exact first, then substring. Each figure has a plausible range
  (`datasets.PLAUSIBLE`); a dataset value outside it (his sheets hold placeholders such as a 7.0
  tax rate) is dropped and shown as "not meaningful for this industry" with the raw number.

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
  `Rev_{T+1} = Rev_T x (1 + g_terminal)`, so the last forecast year's reinvestment is sized for
  terminal growth. At a ten-year horizon this coincides with year-10 growth, as in his sheet.
- **`horizon: 10` is the default** (section 18.2) and follows his structure: years 1-5 use the
  start tax rate, the company cost of capital and `sales_to_capital.value`; years 6-10 fade tax
  and cost of capital linearly to their terminal values and use `value_late`. Per-year lists
  (`revenue_growth.values`, `operating_margin.values`, `reinvestment_override.values`) may hold
  **five entries**, in which case `engine.fade_years` builds years 6-10 by rule (growth linear
  from year-5 growth to terminal growth, the margin held at its year-5 level, per-year
  reinvestment overrides stopping), or **ten**, which are used exactly as written. A file may
  mix the two: each list is judged on its own length.
- **Every case carries a reference run with the other structure** (`engine.reference_inputs`,
  `ScenarioResult.reference`, labelled by `ScenarioResult.reference_label`). At `horizon: 10` the
  reference is the **5-year stop**: the same five explicit years, terminal value at year 5, the
  terminal settings applied in year 6 and the tax rate and cost of capital held at their start
  values, which is bit for bit what the same file computes at `horizon: 5`. At `horizon: 5` the
  reference is the **10-year fade**. The results table, the app and the bar chart name whichever
  applies; the weighted row is the weighted average of the three references.
- `switches.reinvestment_lag` takes 0, 1 (the default), 2 or 3, as his ginzu sheet does (he used
  3 for Nvidia in 2024-25): year `t` reinvests `(Rev_{t+lag} - Rev_{t+lag-1}) / S/C`, and revenue
  past the horizon grows at terminal growth.
- The transition check (section 18.2, diagnostic 7) reports the percentage change in free cash
  flow from the last explicit year to the terminal year and the two returns on capital. A small
  notch downwards is normal, because the terminal year reinvests `g / ROIC` whatever the last
  explicit year spent (his own Alphabet February 2024 sheet is 10.7% down, Microsoft 21%), so the
  check flags only a fall of more than 15% or a terminal return below half the last year's
  implied return. A flagged case also gets a line in the run's warnings. **All cases, including
  bear, receive the same transition checks**; a flag calls for economic review rather than
  changing inputs merely to clear a threshold. Every diagnostic names its cases as
  "Bear case", "Base case", ... and marks a flagged row "(flagged)".
- Terminal return-on-capital premiums (section 18.4 rule 5): bear may use zero or a supported
  positive premium. The house warning thresholds are 8 points for bear/base and 12 for bull;
  above them `allow_large_premium` and a reason are required and the warning remains.
  These thresholds and old worked examples are not economic targets. Compare mature returns
  with normalized company/peer evidence on consistent capital and profit definitions;
  retained or lost advantage must follow the business outcome, not its case label.
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
