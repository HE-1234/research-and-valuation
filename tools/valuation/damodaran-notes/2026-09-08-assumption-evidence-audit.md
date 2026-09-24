# Audit: evidence behind valuation assumptions

Scope: the current GOOGL and MRVL assumption files, their draft reviews, the drafting instructions and the validator. This is an assessment of how assumptions are justified, not a verification of the underlying company filings or a new valuation. Existing company inputs and historical review verdicts are unchanged.

## Findings

The drafts contain substantial work: segment revenue builds, margin bridges, reinvestment history, story-to-number tables and source references. The problem is not simply missing prose. Some explanations establish a direction without adequately establishing the level, some required comparisons lack evidence, and diagnostic thresholds can become targets.

| Finding | Evidence in the current files | Implication |
|---|---|---|
| Growth has a build, but its mature scale is not adequately bounded in GOOGL. | The base `revenue_growth` uses 23%, 20%, 17%, 15%, 13%. Its detail projects about USD 1.47 trillion in year 10 and explicitly says no cached source supplies market size or competitor revenue. It uses an older observation from Damodaran about the number of very large companies, plus the subject's backlog and spending. | A large backlog supports near-term demand; it does not establish the market, competitive share or economics ten years out. Naming reasons for deceleration also does not establish the exact yearly rates. |
| Terminal-return justification partly follows the warning threshold. | MRVL base `terminal.roic_premium.detail` says seven points would put terminal ROIC below half of year-10 ROIC and trigger a cliff, while the selected premium is eight points. It says late sales-to-capital and the premium were chosen as a pair. | Joint consistency matters, but the direction of reasoning can become circular. The final-year forecast may itself be wrong. Mature economics must independently support the chosen inputs. |
| Benchmarking is mainly own history, industry aggregates and historical forecasts. | GOOGL's margin detail lists industry rows and Damodaran's old targets for other companies. MRVL's review says its named comparable, Broadcom, has no margin figure in the supplied cache. MRVL's terminal detail approximates industry ROIC by multiplying an industry margin and sales-to-capital. | These references are useful context but do not constitute observed, comparable mature-company results. Separately aggregated ratios need compatible definitions and populations before their product can be interpreted. |
| The workflow restricted the evidence needed for its own review. | Before this correction, rule 3 and the skill prohibited new source research during drafting, while the playbook requested mature comparisons. | Targeted valuation evidence gathering must precede drafting. Full company-report rebuilds are unnecessary for this purpose. |
| Review and validation are different protections. | Both historical draft reviews ultimately say PASS. `schema.py::_check_story_to_numbers` checks row structure and nonempty fields; it does not establish that a story supports a number or that a benchmark is comparable. | A successful validator cannot establish analytical quality. Review must inspect the evidence-to-input connection, not merely confirm a table exists. |

Locations: [GOOGL assumptions](../../../companies/GOOGL/valuation/assumptions.yaml), [MRVL assumptions](../../../companies/MRVL/valuation/assumptions.yaml), [GOOGL review](../../../companies/GOOGL/review/2026-Q2-valuation-draft-review.md), [MRVL review](../../../companies/MRVL/review/FY2027-Q2-valuation-draft-review.md), [validator](../schema.py).

## Method checked against primary sources

Damodaran connects business narratives to valuation inputs and tests the resulting numbers against the narrative. This supports requiring an explicit business assumption behind the number; it does not imply that a persuasive sentence uniquely determines a growth rate. [Damodaran, *Numbers and Narrative*, June 2014](https://aswathdamodaran.blogspot.com/2014/06/numbers-and-narrative-modeling-story.html).

His terminal-value chapter separates the timing of maturity, the mature firm's characteristics and the transition. It discusses returns moving toward industry averages, larger mature firms as evidence for financing choices, and reinvestment consistent with stable growth. It allows growth below the economy's rate. Our 15% cash-flow-drop and 50% ROIC-ratio warning thresholds are implementation choices, not economic targets prescribed by that chapter. [Damodaran, *Terminal Value*, printed pp. 5–6 and 10–13](https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/termvalue.pdf).

These sources were checked for this audit. Older worked examples remain useful illustrations, with their original dates and accounting conventions; they are not current peer observations.

## Corrections to future practice

AGENTS.md §18.4 rules 15–16 now require a traceable explanation for each material judgment: observed facts, explicit business assumptions, connecting arithmetic, a defensible range, the choice within it and a development that would change it. Every explicit growth year must reconcile to the build, with mature revenue and mix checked against demand. Uncertain rates should be labelled judgments, not given invented precision.

The runner now gathers targeted valuation evidence, reusing eligible library sources before fetching missing pre-cutoff sources. A small set of economically relevant mature companies or segments is the starting point. Accounting definitions, business mix, cyclicality and source dates must be reconciled. Where peers are unsuitable, the analyst must document a defensible substitute; a lack of material support remains BLOCKED.

Terminal ROIC must be justified from the mature business before the transition check. Reported and normalized capital measures remain visible. Current depressed ROIC is not a mandatory ceiling, and high modeled final-year ROIC is not a mandatory floor. A warning leads to investigation of the whole forecast; inputs cannot be tuned merely to clear it. Supported discontinuities can remain with explanation and disclosure.

The local draft skill and analyst/reviewer playbook now implement these requirements. No schema, engine or app change is made here: these are analytical review requirements, not new machine-enforced guarantees. Applying them to an existing company requires an explicitly authorized redraft and its normal owner-review boundary. This audit does not reopen or extend a completed company's two-pass review budget.
