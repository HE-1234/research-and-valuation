---
name: refresh-company
description: >-
  Update an existing company report with a new quarter: archive the old outlook, grade last quarter's claims into scorecard.md, write the new outlook.md with a tone-shift section, flag changes without editing the body of business.md, and assess due valuation forecasts when records exist without re-valuing. Use when the user asks to refresh, update, or re-run a company after new earnings, e.g. "/refresh-company MRVL with Q2 FY2027".
---

# refresh-company

Arguments: `<TICKER> [with <QLABEL>] [--transcript <local file>]`

If no quarter is given, use the most recently reported quarter after the current `outlook.md` with an earnings announcement and corresponding financial filing, per [§12.5](../../../docs/sources.md#section-12-5). If no newer eligible quarter exists, report that the outlook is current and leave its files unchanged.

## Procedure

Read the [root instructions](../../../AGENTS.md), [research guide](../../../docs/research.md), [sourcing guide](../../../docs/sources.md), and [review guide](../../../docs/review.md) before the dependent work. The refresh procedure is [§15](../../../docs/research.md#section-15). Before fetching, read `companies/<TICKER>/source-guide.md` if present; pass the applicable guides to gatherers, writer, and reviewer.

1. **Preconditions.** `companies/<TICKER>/business.md` and `outlook.md` must exist. If neither exists and the request covers initial research, route to `research-company`; otherwise explain the missing prerequisite under AGENTS.md's opening routing rule. A partial existing report is not permission to rebuild it. Use the existing indicator set under [§8](../../../docs/research.md#section-8), including proposed indicators unchanged; no lock confirmation is needed to finish the refresh.

2. **Resolve the new quarter** and cutoff per [§12.5](../../../docs/sources.md#section-12-5), including equivalent foreign-issuer filings and the transcript-posting exception. Create `sources/<new QLABEL>/`.

3. **Gather** per [§13](../../../docs/review.md#section-13), scheduling `filings`, `transcript`, and `ir` subagents to fit current capacity. The shared rule includes cache reuse, separate manifest parts, prior-quarter guidance materials, and any additional pre-cutoff filings needed for comparisons, incorporated disclosures, or calculations. Apply transcript tiers per [§12.2](../../../docs/sources.md#section-12-2) and any `--transcript` file.

4. **Archive.** Copy `outlook.md` to `quarters/<old QLABEL>-outlook.md` byte-for-byte.

5. **Grade and write.** Launch one writer subagent with: the shared boundaries, [research guide](../../../docs/research.md), [review guide](../../../docs/review.md), `business.md`, the archived old outlook, the current `scorecard.md` (may not exist yet), and all new `notes-*.md`. It must:
   - Grade every claim in old `outlook.md` §5 plus every ⏳ claim carried in `scorecard.md`, per [§9](../../../docs/research.md#section-9), one line of evidence each with source tag.
   - Prepend the new grading section to `scorecard.md` and update the running tally and indicator time series ([§10](../../../docs/research.md#section-10)). Create the file if this is the first refresh.
   - Write the new `outlook.md` per [§7](../../../docs/research.md#section-7), using exactly the existing indicator set under [§8](../../../docs/research.md#section-8) (locked or still proposed) in §1, and including §6 Tone shift compared against the archived outlook and, where useful, the old transcript in `sources/<old QLABEL>/transcript.txt`.
   - Check `business.md` against the new sources and prepend FLAG blocks per [§11](../../../docs/research.md#section-11) where warranted. Never edit the body of `business.md`.
   - If prior valuation forecasts exist, read [forecasts-and-learning.md](../draft-valuation/references/forecasts-and-learning.md) and apply [§18.12](../draft-valuation/references/forecasts-and-learning.md#section-18-12). Compare only due, comparable outcomes in `valuation/forecast-reviews/<QLABEL>.md`; maintain company-specific `valuation/lessons.md`. Preserve original forecasts, origin, dates and definitions. No baseline or missing actuals leaves a stated assessment gap and does not block the company report. Never change active assumptions or compute a new valuation.
   - Run the [§14](../../../docs/research.md#section-14) self-check.

6. **Review** per [§13](../../../docs/review.md#section-13). Launch an independent reviewer covering `outlook.md`, `scorecard.md`, and flags, including the required blind re-grade before opening the scorecard. Apply the shared correction permissions, two-pass limit, and PASS/REVISE/BLOCKED handling. Re-verify every verdict against the cached sources. For forecast assessments, independently derive material actuals and check original dates/definitions before reading the writer's error attribution; include this in the same review budget.

7. **Commit only after PASS.** `refresh(<TICKER>): <new QLABEL>`, following [§16](../../../AGENTS.md#section-16). Otherwise preserve drafts and report incomplete work under [§13](../../../docs/review.md#section-13).

8. **Report to the user** in a few lines: the running tally change, any ❌ or 🔇 verdicts with one line each, the tone-shift headline, any FLAGs raised, transcript source tier, and reviewer verdict. Report material forecast errors/lessons or the absence of an eligible baseline. If `companies/<TICKER>/valuation/` exists, add one line saying the valuation is now as of an older quarter ([§18.7](../draft-valuation/references/workflow-contracts.md#section-18-7)); this skill never re-values.
