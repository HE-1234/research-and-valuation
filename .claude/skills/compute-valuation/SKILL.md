---
name: compute-valuation
description: Compute valuation results from existing assumptions after the owner requests computation following draft review. Supports in-memory overrides and dry runs; writes and commits a checked report on a normal run. Does not redraft assumptions or change owner judgments. Use draft-valuation when a new draft is needed.
---

# compute-valuation

Arguments: `<TICKER> [--set path=value ...] [--dry-run]`

## Procedure

Read the [root instructions](../../../AGENTS.md), the compute subsection and draft-review boundary in the [workflow contracts](../draft-valuation/references/workflow-contracts.md#computation), the [report requirements](../draft-valuation/references/valuation-output.md), and [market-data fallbacks](../draft-valuation/references/model-spec.md#section-18-8). Run the engine from the repository root with `uv`. For the post-compute record, read [forecasts and learning](../draft-valuation/references/forecasts-and-learning.md). This workflow applies reviewed inputs; it does not repeat the analyst's research or change accounting judgments.

1. **Check prerequisites and validate effective inputs.** Follow [§18.7](../draft-valuation/references/workflow-contracts.md#computation) step 1 and the draft-review boundary. A subsequent compute request is authorization; do not ask the owner to reconfirm that they reviewed the draft. If assumptions are missing, route to drafting only when the request covers it, then stop at owner review. Pass every user-supplied `--set` override unchanged to `uv run value <TICKER> --validate [--set ...]` and to computation. Overrides remain in memory. Inspect errors and stopped cases; do not stop on an error in the original file that the supplied override fixes. If effective inputs still fail, report the errors and affected work. Fix no YAML in this skill; judgment changes require the owner.

2. **Check staleness.** Compare the YAML quarter with `outlook.md`. If the outlook is newer, disclose that the valuation uses older inputs and proceed; do not automatically redraft or request confirmation.

3. **Compute.** For a normal run, retain the source input bytes/hash and exact `--set` arguments before execution so the forecast record can identify effective inputs; keep any provisional copy temporary until success. Follow [§18.7](../draft-valuation/references/workflow-contracts.md#computation) step 2. A normal `uv run value <TICKER> [--set ...]` computes, archives the prior pair through the engine, and writes `valuation.md` and `assumptions.md`. Do not archive a second time. For a requested dry run, use `uv run value <TICKER> --dry-run --json [--set ...]`; this returns the current result and metadata without writing or archiving files. Apply the market module's bounded retries and [§18.8](../draft-valuation/references/model-spec.md#section-18-8) fallbacks. If they fail, report the specific missing input without inventing one.

4. **Inspect this run.** Use the new report for a normal run or current JSON for a dry run, never an older saved report. Apply [§18.7](../draft-valuation/references/workflow-contracts.md#computation) step 3: check warnings, stopped/skipped cases, and market dates/sources. Explain missing dates for manual inputs. Report unresolved defects without claiming completion or silently changing assumptions.

5. **Freeze the forecast and commit a successful normal run.** Apply [§18.12](../draft-valuation/references/forecasts-and-learning.md#section-18-12) to create a separate owner-compute record after successful inspection. Verify the source file did not change during the run; if provenance is ambiguous, report the learning-record gap rather than snapshotting an unverified version. Record exact effective overrides alongside the source YAML; never call the original file alone the effective inputs. This step does not run on a dry run. Follow [§18.7](../draft-valuation/references/workflow-contracts.md#computation) step 4 and [§16](../../../AGENTS.md#section-16). Use `value(<TICKER>): compute <QLABEL> rev N`, counting prior compute commits for that quarter rather than all history folders. Skip the commit on `--dry-run` or a failed sanity check.

6. **Report.** Follow [§18.7](../draft-valuation/references/workflow-contracts.md#computation) step 5: per-share values against price/date, weighted value when available, terminal-value share, reverse-DCF growth, every warning, and any stopped/skipped cases. Report a dry run from its output. Include owner changes since the last compute when that comparison is available. Direct assumption edits to the app; do not ask the owner to type YAML or add interpretation beyond the requested results.
