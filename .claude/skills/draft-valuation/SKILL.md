---
name: draft-valuation
description: Draft the DCF valuation assumptions for a company already in the research library, following AGENTS.md §18. Reads business.md, outlook.md, scorecard.md and the cached filings, writes companies/<TICKER>/valuation/assumptions.yaml with bear/base/bull/management inputs, reasons and sources, has a reviewer check every number, then stops for the owner to edit. Computes nothing. Use when the user asks to value, draft a valuation for, or set up a DCF for a company, e.g. "/draft-valuation GOOGL".
---

# draft-valuation

Arguments: `<TICKER> [--redraft]`

## Procedure

Read `AGENTS.md` in the repo root before anything else. §18 defines the method, the `assumptions.yaml` schema (§18.4), the analyst's thirteen rules, and this procedure (§18.7). This skill only sequences the work.

1. **Preconditions.** `companies/<TICKER>/business.md` and `outlook.md` must exist; if not, stop and tell the user to run `research-company`. If `valuation/assumptions.yaml` already exists, stop and tell the user to edit it and run `compute-valuation`, unless `--redraft` was given, in which case move the existing `assumptions.yaml`, `assumptions.md` and `valuation.md` (if any) into `valuation/history/<YYYY-MM-DD-HHMM>/` first. If the archived YAML carries a `changelog`, list the owner-edited cells with their values and hand them to the analyst as the owner's own view (AGENTS.md §18.7 step 1): the analyst still builds every number from the sources and the rules, and where it lands elsewhere its `detail` says so and the report shows both numbers side by side.

2. **Resolve the as-of quarter** from `outlook.md` (its quarter label) and the cutoff date from that quarter's `sources/<QLABEL>/MANIFEST.md`. Create `companies/<TICKER>/valuation/`.

3. **Analyst** (one subagent). Give it: AGENTS.md §3 and §18, the ticker, as-of quarter and cutoff date, the fiscal calendar, the paths to `business.md`, `outlook.md`, `scorecard.md`, and the `sources/` folders it may read (the as-of quarter and the one holding the latest 10-K). It writes `valuation/assumptions.yaml` per §18.4: base year as trailing twelve months from the cached 10-K and 10-Q, bridge from the latest balance sheet, four scenarios with stories (`horizon: 10`: five explicit years per list, years 6–10 by the §18.2 rule), the management case built only from recorded guidance, every number source-tagged, year-1 growth starting from the latest reported run-rate (rule 10), a segment build behind every growth path (rule 11), sales-to-capital set against lagged history (rule 12), a margin bridge showing drag and offsets (rule 13), terminal return on capital below today's (rule 5), every judgment with a `reason` of one to three plain sentences and the working numbers (history, arithmetic, alternatives) in that cell's `detail`. Nothing substantive goes into YAML comments; the owner reads the app and `assumptions.md`, never the raw file. It fetches nothing from the internet. Cells it cannot fill from Damodaran's datasets (unlevered beta, market debt-to-equity) it leaves `null` with the numerator or industry in the reason; the runner fills them in step 4.

4. **Fill market-derived cells.** Run `uv run value <TICKER> --validate`. Fill `cost_of_capital.build.unlevered_beta` from the cached dataset (`tools/valuation/data/damodaran/betas.csv`, industry named in the YAML) and `debt_to_equity_market` from (debt + leases) over the current market cap (`uv run value <TICKER> --dry-run --json` prints the fetched price), recording the dataset date and price date in each cell's `source`. Re-run `--validate` until it passes. Then run `uv run value <TICKER> --render-assumptions` to write the readable `valuation/assumptions.md` (re-run it after any later edit to the YAML in this skill).

5. **Reviewer** (one subagent). Give it AGENTS.md §3 and §18, the YAML, and read access to the same sources. It writes `review/<QLABEL>-valuation-draft-review.md` per §18.7 step 3: every base-year and bridge number re-checked against the cached source; the 3P test on each story; the consistency checks of §18.7 step 4(c) (year-1 run-rate, segment build, lagged sales-to-capital, margin bridge, amortization roll-off, management case only from recorded guidance, terminal rules including terminal return below today's, weights, and the transition check read from `uv run value <TICKER> --dry-run`, recording flags and cash flows but never values per share); a reader check on the stories; PASS or REVISE with a list. The reviewer may fix wording and source tags directly; numbers and judgments go back to the analyst. Maximum two cycles.

6. **Commit** `value(<TICKER>): draft assumptions as of <QLABEL>`.

7. **Report to the user** in a few lines: the four stories in one line each, the five inputs most worth their attention, anything the analyst could not source, the reviewer's verdict, and the exact next step: read `companies/<TICKER>/valuation/assumptions.md`, adjust and compute in the app (`uv run --extra app valuation-app`), or run `/compute-valuation <TICKER>` directly. The owner does not edit the YAML by hand (AGENTS.md §18.7).

Do not compute or report any valuation figure in this skill. The owner reviews the assumptions first; that was a deliberate design choice.
