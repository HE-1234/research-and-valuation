---
name: compute-valuation
description: Run the DCF engine on a company's reviewed valuation assumptions (companies/<TICKER>/valuation/assumptions.yaml), write valuation.md with bear/base/bull/management values, sensitivities, reverse DCF and diagnostics, and commit. Use after draft-valuation and after any owner edit to the assumptions, e.g. "/compute-valuation MRVL" or "/compute-valuation GOOGL --set scenarios.base.sales_to_capital.value=1.5".
---

# compute-valuation

Arguments: `<TICKER> [--set path=value ...] [--dry-run]`

## Procedure

Read `AGENTS.md` §18 in the repo root first; §18.5 defines what `valuation.md` contains and §18.7 this procedure. The engine lives in `tools/valuation/` and is run with `uv` from the repo root.

1. **Preconditions.** `companies/<TICKER>/valuation/assumptions.yaml` must exist; if not, stop and tell the user to run `draft-valuation`. Run `uv run value <TICKER> --validate`; on failure, show the errors verbatim and stop. If the user gave `--set` overrides, pass them through unchanged; they apply in memory only and are recorded in the output header, never written into the YAML.

2. **Staleness check.** Compare `as_of_quarter` in the YAML with the quarter label in `outlook.md`. If `outlook.md` is newer, say so in the report (the valuation is as of an older quarter) but proceed.

3. **Compute.** Run `uv run value <TICKER> [--set ...]` (add `--dry-run` if the user asked for it). The engine archives the previous `valuation.md` and `assumptions.yaml` into `valuation/history/<YYYY-MM-DD-HHMM>/`, fetches the price, risk-free rate and equity risk premium, computes every case, writes `valuation.md`, and prints the results table and warnings. If a market fetch fails and no manual value exists in the YAML, stop and show the message.

4. **Sanity read.** Open `valuation.md` and check three things before committing: every warning the engine printed is understandable to the owner; no scenario silently skipped (a skipped management case must say `computable: false`); the header shows price, risk-free and ERP dates. Fix nothing in the YAML yourself; if something needs a judgment change, tell the owner.

5. **Commit** `value(<TICKER>): compute <QLABEL> rev N`, where N counts computes for that as-of quarter (count existing `history/` folders plus one). Skip the commit on `--dry-run`.

6. **Report to the user** in a few lines: value per share for each case against the price and its date, the weighted value, the terminal-value share, the reverse-DCF growth, and every warning verbatim. No interpretation beyond that; the owner reads `valuation.md`. Remind them that assumptions are changed in the app (`uv run --extra app valuation-app`, which saves into `assumptions.yaml` with a change log) and that re-running this skill re-computes. If the YAML has a `changelog`, list the owner's changes since the last compute in one line each.
