# Valuation playbook: read before choosing inputs

[Root instructions](../../../../AGENTS.md) own shared boundaries; [model requirements](model-spec.md), [assumptions requirements](assumptions-spec.md), and [workflow contracts](workflow-contracts.md) own valuation rules. This playbook routes the analyst and reviewer to practical references; the [primary-source library](../../../../tools/valuation/damodaran-notes/README.md) preserves Damodaran's teachings and provenance. The procedures below are our implementation of those teachings, not quotations or claims that he uses our exact file formats, scenario weights or warning thresholds.

## Reading and work order

| Decision | Read | Record the application |
|---|---|---|
| Is this model suitable? Always assess before drafting. | [Model selection](model-selection.md) | Evidence note: business/life-cycle classification, model choice, supported treatment and limitations. |
| Are reported figures comparable? Always screen; investigate material items. | [Accounting and reinvestment](accounting-and-reinvestment.md) | Evidence note: reported-to-economic bridge and chosen accounting basis. |
| What do outside analysts expect? Gather before drafting; reconcile before choosing near-term inputs. | [Consensus collection](../../../../docs/sources.md#section-12-6) and [consensus-to-model procedure](business-drivers.md#from-consensus-to-model-inputs) | Dated aggregate snapshot, coverage gaps, period/accounting bridge, implied growth and margins, and selected base-case changes. |
| What business produces these cash flows? Every computable scenario. | [Business drivers](business-drivers.md) | Input `reason`/`detail`: growth build, margin bridge, capital needs and mature-state support. |
| Where does uncertainty enter? Every draft. | [Uncertainty and bias](uncertainty-and-bias.md) | Evidence note: major risks, scenario coherence, weights and price-independence. |
| What did we learn? Read on redraft, on refresh with valuation records, and when freezing the first forecast. | [Forecasts and learning](forecasts-and-learning.md) | Frozen forecast record, later assessments and company-specific lessons. |
| Does the draft hold up? Reviewer reads before its pass. | [Review checklist](review-checklist.md) | Required checks, evidence locators and PASS/REVISE/BLOCKED. |
| Would an illustration help? Optional. | [Historical examples](worked-examples.md) | Identify the useful method; never copy a dated input as a current benchmark. |

Read the relevant references, not all downloaded papers. Open the cached original passage whenever a methodological claim is disputed, a calculation is unfamiliar, or a material choice depends on it. Preserve its title/date and page or section locator. Missing topic evidence triggers a targeted primary-source lookup and cache entry, not invented attribution.

## From evidence to a tested story and inputs

The runner assembles company, consensus and peer evidence before the analyst drafts. Apply [assumptions rule 10](assumptions-spec.md#section-18-4): usable consensus seeds the near-term base-case numbers. Work backward from its implied growth and margins to a business hypothesis: who pays, how demand changes, why the company wins or loses, and what it must spend. Test that hypothesis against the research, operating builds and contrary evidence; retain credible estimates and make visible, supported changes where needed. When consensus is missing, use the documented company-specific fallback. A provisional story need not precede source estimates, and imported numbers do not justify inventing a story to defend them. Revise both narrative and forecast when the evidence disagrees, recording material reconsiderations in the input's working notes.

The owner should see what must be true in one to three plain sentences beside an input. Put the source facts, explicit analyst judgments, calculation, defensible range, target placement and revision trigger in `detail`. Nearby percentages usually cannot be distinguished precisely by evidence; admit that rather than dressing a judgment up as a sourced fact. A story-to-numbers table links explanations to inputs but cannot replace these working notes.

For capital-intensive growth plans, apply the [investment-payoff check](business-drivers.md#investment-payoff-check) before fixing margins or the mature destination. Explicitly assess years 6–10; retaining the default fade and flat margin is an economic choice to explain, not an automatic continuation of year five.

Apply the [case definitions](uncertainty-and-bias.md#apply-to-this-repository) when continuing the base case and forming realistic adverse and favorable outcomes. The probability-weighted value is a separate calculation across scenarios; a DCF of central inputs need not equal the expected value of the outcomes. Preserve owner-set weights, or use the house defaults labelled as assumptions. Analyst estimate ranges do not determine those weights. Management guidance remains separately identified and unweighted.

Before presenting the draft, use only the restricted operating diagnostics permitted by [§18.7](workflow-contracts.md#section-18-7). Neither the current share price, an old valuation result nor a desired upside is evidence for a growth or margin assumption. Legitimate market inputs used by the runner for financing weights do not authorize anchoring operating assumptions to price.

An authorized redraft consults prior forecast assessments and documents which lessons affected which inputs, including justified non-adoption. It does not rewrite historical forecasts or imply a new valuation result before owner review.
