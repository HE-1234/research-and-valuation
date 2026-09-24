# Learn from our forecasts without rewriting them

<a id="section-18-12"></a>

## 18.12 Forecast records and learning

Use the record format and comparison procedure below. A passing promoted draft creates an immutable `valuation/forecasts/<UTC timestamp>-analyst-proposal/` containing exact source inputs plus a dated operating forecast; no valuation results are needed. A successful normal compute through the skill creates a separate `owner-compute` record identifying exact input bytes and all effective overrides; dry runs write nothing. Preserve creation time, information cutoff, source hash, model windows, definitions and origin. Existing app/history records can be used only with adequate provenance; do not imply the app automatically captures this new record. Never backdate a reconstruction or rewrite a forecast after observing its outcome.

Refresh assesses only due, comparable targets using new sourced actuals, in `valuation/forecast-reviews/<QLABEL>.md`, separate from management's scorecard. Preserve analyst versus owner origins, all applicable scenarios, original windows and accounting definitions. Record signed errors and an evidence-based explanation, or `not yet due`, `not disclosed`, `not comparable`, `no eligible baseline`. No eligible baseline is a stated gap, not a reason to block company research or fabricate a prediction. Missing actuals stop only the dependent assessment. Material comparisons and provenance are checked in the ordinary independent review, within its two-pass budget.

Write company-specific observations and tentative causes to `valuation/lessons.md` with links to original forecasts and later assessments. On the next authorized redraft the analyst reads these first and states which lessons it adopts, rejects or leaves unresolved, and why. Do not mechanically correct every new input by the previous forecast error; do not select whichever old scenario happened to fit. Supported process-wide changes update the applicable current guide under the [instruction maintenance policy](../../../../AGENTS.md#maintaining-instructions-and-lessons). Neither reviewing forecasts nor logging lessons edits active assumptions, re-values the company, changes locked research indicators or authorizes an extra review round.

This is the repository's implementation of a feedback loop, not a file format prescribed by Damodaran. The conceptual sources are [narrative-and-numbers.txt](../../../../tools/valuation/damodaran-notes/sources/narrative-and-numbers.txt), feedback discussion, and [uncertainty.txt](../../../../tools/valuation/damodaran-notes/sources/uncertainty.txt), hindsight and willingness to be wrong. The requirements above define when this runs.

## 1. Freeze an identifiable forecast

After a passing draft is promoted, the runner creates a unique `valuation/forecasts/<UTC timestamp>-analyst-proposal/` containing a byte-for-byte copy of the selected `assumptions.yaml` and a `forecast.md`. Do not snapshot a rejected candidate as a passing forecast or overwrite an existing record. This is a record of the analyst proposal, not owner acceptance.

After a successful normal compute through the skill, record a separate `<UTC timestamp>-owner-compute/` version. Copy the input YAML and record the exact in-memory `--set` overrides used in that run. The combination, not the unmodified YAML alone, identifies effective inputs. Dry runs produce no record. App-only operations do not currently create these records automatically; use existing timestamped history/changelog only when provenance is sufficient, and disclose the gap otherwise.

`forecast.md` contains:

- Record ID, origin (`analyst-proposal` or `owner-compute`), creation time in UTC, information cutoff, source YAML path and SHA-256, repository revision plus dirty-state disclosure, and any effective overrides. Never include market price, upside or value-per-share in an analyst-proposal record.
- Base TTM start/end dates; the exact start/end dates of each forecast year; units, currency and accounting basis. State any mapping from model years to management's fiscal guidance. Do not call a TTM forecast an upcoming fiscal-year prediction.
- A small table: scenario | metric | target period | forecast | definition | original reason/revision trigger. Record each explicit year's revenue and operating margin, the resulting operating profit, and net reinvestment where the original operating diagnostics or a source-supported bridge establishes it. Include material operating milestones from the existing assumptions; do not invent new company indicators. Copy relevant restricted diagnostics when available, excluding valuation results.
- Resolved non-price model inputs and dates that affect operating targets (for example the risk-free rate used by an automatic growth fade), or an explicit statement that they were not captured. An `auto` token alone cannot reproduce a historical operating forecast.
- Probabilities as originally specified, whether a metric/range is a scenario outcome or an expected forecast, and any limitations. Five-to-ten-year mechanical extrapolations are labelled as such.

Revenue equals preceding revenue times one plus that year's growth; profit equals revenue times margin on the stated basis. Compute these operating quantities without a valuation if needed. Do not invent a reinvestment forecast if required inputs are unavailable. Capture original judgments before looking at their outcomes. A historical file discovered later is a **retrospective reconstruction**, with discovery time and evidence of its original existence; it is not a newly created ex-ante forecast.

## 2. Assess only comparable, due outcomes

On a company refresh, inspect forecast records published before the outcome became known. For each due target use newly cached filings to derive the same period and metric. An annual forecast is not missed after one weak quarter. Quarter progress can be discussed separately without grading an unfinished annual target. Avoid comparing a GAAP actual with an adjusted forecast, or gross capex with net reinvestment. A restatement or segment change requires a visible bridge or `not comparable`.

Write the assessment in `valuation/forecast-reviews/<QLABEL>.md`, separately from management's `scorecard.md`. For each row record: forecast ID/origin | scenario | metric/window | original forecast | sourced actual | signed error | status | explanation. Use `actual - forecast` for absolute error and `(actual / forecast - 1)` for relative error only when the denominator makes that interpretation useful; use percentage points for margin differences. With zero/negative denominators report absolute errors and explain. Valid statuses: `assessed`, `not yet due`, `not disclosed`, `not comparable`, `no eligible baseline`. Use the last status when no original target exists; do not describe that as a missing actual. A point forecast is not a binary management promise.

Assess all applicable original scenarios; do not retrospectively designate whichever was closest as the expected case. Separate analyst-proposal and owner-compute records. Distinguish within-scenario error from scenario-range coverage, and label coverage descriptive rather than a confidence interval. Do not pool multiple versions of the same forecast as independent observations.

## 3. Attribute, then carry lessons forward

Separate what the sources demonstrate from explanations that remain hypotheses. Useful causes include source/definition error, operating-driver error, timing, cycle or external shock, capital-efficiency error, and wrong story. A surprise is not automatically unforeseeable; a single miss is not proof of a permanent bias. Market-price performance does not establish that the operating forecast was right.

Maintain `valuation/lessons.md` with dated entries: forecast/assessment link | observation | plausible cause and confidence | proposed change or monitoring question | later evidence | status. Append follow-up entries rather than silently changing the old prediction or attribution. Correcting a factual error requires a dated correction preserving the earlier assessment.

On the next authorized redraft, read applicable lessons **before choosing new inputs**. Record each lesson adopted, rejected or still unresolved and the affected cell/evidence. Do not mechanically subtract last year's error from next year's growth or move every input in one direction. Apply supported process changes to the relevant current guide under the [instruction maintenance policy](../../../../AGENTS.md#maintaining-instructions-and-lessons). Add a short general decision note only when its reasoning is useful; company-specific lessons stay with the company and link to the full forecast assessment.

## Boundaries and gaps

No baseline means `no eligible baseline`; it does not block research or justify fabricating history. Missing comparable actuals leave that assessment pending while the ordinary company refresh continues. Forecast review is observational: it does not edit active assumptions, recompute valuation, unlock business indicators or authorize an extra company review pass. The existing reviewer checks material actuals and provenance within the normal two-pass budget.
