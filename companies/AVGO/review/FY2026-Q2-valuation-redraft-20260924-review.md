# AVGO FY2026-Q2 valuation redraft — independent review

_Pass 1 of the separately authorized September 24, 2026 redraft. Operating cutoff: June 9, 2026. The reviewer is independent of the analyst and runner. No valuation result was calculated or disclosed._

## Verdict: BLOCKED

The added base-case hypothesis and consensus-fallback explanation are accurate and useful, but they do not make the candidate a complete new valuation. The candidate is numerically identical to the blocked active draft apart from its drafting date; its only substantive change is explanatory text in `scenarios.base.revenue_growth.detail`. All four cases still stop on the same unsupported late-investment inputs, and every equity bridge still stops on the same two unsupported balance-sheet/claim inputs. The exact candidate SHA-256 is `b5e2dbd24aeda7fed2bc544acea4c9baef5eb18245a5ac6039855bfe37c04261`. [Candidate comparison; validation; diagnostics]

This is a new review cycle rather than a third pass on the September 19 workflow. Prior review work is used only as audit evidence for unchanged inputs. The present pass independently rechecked the new consensus/fallback and hypothesis wording, the unresolved cells, their propagation through the model, and the applicable operating, accounting, peer and transition requirements.

### Precise blockers and repairs

| Gap | Affected cell/check | Required repair |
|---|---|---|
| Years 6–10 total investment and the bridge into mature economics remain unsupported. | Every case has `sales_to_capital.value_late: null` and years 6–10 of `reinvestment_override.values` are null; checklist 6, 7, 9, 13, 15 and 16. | Establish a consistent funding hypothesis covering inventory, contract assets/customer advances, supplier commitments, physical replacement and recurring IP/research investment, with the same profit/capital definitions used for the mature-return comparison. A defensible forecast judgment is allowed; reverse-engineering a ratio from the desired terminal return or merely restoring the rejected ratio is not. Then rerun restricted diagnostics and explain every transition flag. |
| Carrying value of corporate investments outside cash equivalents is not established. | `bridge.non_operating_assets.0.value: null`; checklist 13 and 17; every case stops. | Supply a dated stock balance or a documented materiality bound. Do not infer an ending balance from purchases and sales or count pension-plan assets as corporate investments. |
| Present value of the June 8 customer-lease backstop is not established. | `bridge.other_claims.0.value: null`; checklist 13, 16–18; every case stops. | Supply an independently supported fair-value or expected-claim treatment using deployment, fees, default and recovery evidence. Neither zero nor the disclosed $29 billion maximum is presently supported. If scenario-dependent treatment is material and cannot be represented by one shared bridge value, document the engine capability limitation rather than forcing the risk into firm failure or WACC. |

The missing pre-cutoff third-party consensus snapshot is **not itself a blocker**. The cache inventory contains no eligible provider mean, publication date, contributor count, fiscal mapping and GAAP EBIT definition. Rule 10's management-guidance fallback is therefore used honestly: reported TTM sales, Q3 guidance, the FY2026 AI floor and named deployments are separated from analyst extensions. The new paragraph makes this bridge explicit. A future eligible snapshot should replace the fallback for the periods and metrics it actually covers, but management guidance must not be relabeled consensus. [Valuation evidence overview; candidate base revenue detail]

## Independent reconstruction and material bridges

The unchanged base facts still reproduce from the cached filings: TTM revenue is `63,887 + 41,498 - 29,920 = 75,465`; GAAP operating income is `25,484 + 19,351 - 12,089 = 32,746`; acquired amortization is `8,062 + 3,936 - 3,984 = 8,014`; SBC is `7,568 + 4,268 - 3,051 = 8,785`; and R&D is `10,977 + 5,960 - 4,946 = 11,991`. Cash is 19,628, debt carrying amount is 64,907, and rental-basis invested capital is `87,691 + 64,907 - 19,628 = 132,970`. Latest-quarter diluted shares are `4,747 + 129 = 4,876`. These definitions preserve goodwill, expense R&D and SBC, and retain rent in EBIT rather than subtracting ordinary lease debt a second time. [10-K FY2025; 10-Q Q2 FY2026; valuation base evidence]

The new central hypothesis connects the disclosed AI programs and software renewals to the selected component revenue path, an initial scale benefit, later buyer/mix pressure and continuing funding needs. It is a coherent **operating** hypothesis, not a complete cash-flow hypothesis: it expressly concedes that years 6–10 funding cannot be supported. That concession is correct, but wording cannot substitute for the missing investment inputs. The first-five-year overrides remain transparent provisional budgets; the later margin and revenue paths cannot be turned into cash flows without the missing bridge.

The peer work remains suitable and definition-aware. Qualcomm, Cisco, Microsoft PBP/consolidated and Broadcom history are named, dated and reconciled for goodwill, R&D/SBC and retained-rent accounting. They support the margin placement and an independently chosen range for mature operating returns, but do not prove Broadcom's future marginal sales-to-capital ratio. The 18% central/management and 22% bull mature returns were selected from the peer/history evidence rather than tuned to clear a diagnostic. Their reinvestment implications cannot be fully tested against the current explicit period because the late capital inputs are null. [Mature benchmark evidence]

The demand bridge remains conditional but adequate for the revenue side: WSTS supplies a deliberately broad non-memory/logic ceiling, while the existing 27,703 software franchise, reported sales growth, 17% ARR wording and disclosed enterprise workload role supply a separate software check. The candidate labels market-share and renewal assumptions as judgments and gives ranges and revision triggers. It does not convert gigawatts or platform financing into Broadcom revenue. All four year-5/year-10 builds and margin endpoints are unchanged from the already audited paths; no numerical repair was introduced under the name of a new hypothesis.

## Twenty required checks

| # | Answer | Finding |
|---|---|---|
| 1 | Yes | Bear, base and bull contain distinct delay/insourcing, repeat-design/renewal and sustained-share-win mechanisms, with timing and management responses. Management is separately identified as a hybrid of disclosed targets and analyst completion. |
| 2 | Yes, fallback | No eligible consensus exists in the cache. The documented search criteria and management fallback are adequate and now explicit; guidance, reported facts and analyst extensions are not conflated. |
| 3 | Yes for revenue; incomplete for cash flow | Demand duration, competition and year-5/year-10 scale are tested, but the business path beyond year 5 lacks its required investment path. |
| 4 | Yes | GAAP margin endpoints are placed against named mature observations and an own-company amortization sensitivity with accounting/mix limits stated. |
| 5 | Yes | Larger chip scale is paired with falling later chip margins, lower software mix and ongoing engineering/SBC; the draft does not claim niche margins without the mix bridge. |
| 6 | **BLOCKED** | Firm, peer and industry capital evidence is researched, but it does not establish late marginal capital efficiency. Current diagnostics cannot produce a final-year implied return because every late ratio is null. |
| 7 | **BLOCKED beyond year 5** | The early lag, physical capex and other funding budget are explicit; commissioning, working-capital timing and recurring IP/equipment funding are not reconciled through years 6–10. |
| 8 | Yes | The shared build uses dated beta, debt-cost, capital-structure, risk-free and ERP evidence. Operating/customer risk is not duplicated in WACC, and current price affects financing weights only. |
| 9 | **BLOCKED as a transition check** | Mature premiums have independent support and warning flags are disclosed, but late investment is missing, so final-explicit-to-terminal cash flow and return transitions cannot be tested. |
| 10 | Yes | Story-to-numbers rows match the stored growth, margin, tax, terminal and investment cells, including the null late inputs. |
| 11 | Yes for the operating base | The new central hypothesis is supported by delivery/program and software evidence, includes contrary triggers, and is not an automatic consensus haircut or price-driven story. It remains incomplete as a cash-flow base. |
| 12 | N/A | There is no prior owner-edited or eligible frozen forecast. Relative to the blocked active draft, no numerical input changed; the added explanation does not show directional value targeting. |
| 13 | **BLOCKED for three input categories** | Supported facts and early judgments remain reproducible, with ranges and triggers. Late capital, investment holdings and the lease backstop lack a defensible fact-to-judgment bridge. |
| 14 | Yes | Suitable mature peers were researched with dates, definitions and material limitations. Segment and consolidated observations are not interchanged. |
| 15 | Yes for revenue; **BLOCKED for complete model** | Explicit component revenue reconciliations and demand bounds remain present. Their late funding consequences remain missing. |
| 16 | **BLOCKED for completion** | The evidence note correctly finds FCFF suitable for operations but records the claim-capability and late-funding limits; the YAML matches those limits with nulls. |
| 17 | **BLOCKED for holdings/backstop; otherwise yes** | R&D, acquired amortization, leases, SBC, dilution, taxes and goodwill are treated consistently. The two unresolved bridge values are not disguised as zero. |
| 18 | Yes, with claim limitation visible | Demand risk stays in operating cases, systematic risk in WACC and the customer backstop in the bridge. Weights are assumptions, not measured probabilities; the unsupported claim prevents full scenario assessment. |
| 19 | N/A | No eligible prior forecast or consensus baseline exists, so no hindsight comparison or lesson can be manufactured. |
| 20 | Yes, deferred | The post-PASS snapshot requirements are stated, but a passing forecast must not be frozen while the draft is blocked. |

## Source-tag and invented-number spot checks

The following material items were traced to cached original filings/releases or the peer note's primary locators: TTM revenue, TTM operating income, acquired amortization, SBC, R&D, tax numerator/denominator, cash, debt, diluted shares, the 1,662 uncertain-tax claim, the $29 billion maximum backstop, Q3 total revenue guidance, Q3 AI revenue guidance, FY2026/FY2027 AI wording, WSTS 2027 logic sales, and the Qualcomm/Cisco/Microsoft/Broadcom benchmark rows. No unsupported reported number was found among those checks. The draft correctly calls the software ranges, component splits, mature growth and future margin paths analyst judgments rather than reported facts.

No source-tag wording or typographical repair was necessary. The two null bridge cells and four null late-ratio paths are deliberate evidence-gap representations, not schema mistakes.

## Reference use

| Reference read | Applicable judgment | Cell/evidence section | Finding |
|---|---|---|---|
| Model specification | Five-plus-five explicit path, terminal transition and diagnostics | Horizon; scenario growth/margin/investment; terminal | Ten-year revenue/margin paths exist, but null late investment prevents the required transition test. |
| Assumptions specification and workflow contracts | Rule 10 fallback, rules 15–16, null handling, redraft boundary | Base revenue detail; evidence overview; candidate control | Fallback is explicit and redraft is isolated; required unsupported inputs correctly stay null, so completion is blocked. |
| Analyst playbook and business-drivers guide | Story-to-numbers, segment build and investment-payoff test | All scenarios; base sales-to-capital detail | Operating stories connect to revenue/margins; later investment payoff remains the material omission. |
| Model-selection guide | FCFF suitability and financing exposure | Evidence scope/model choice; backstop bridge | FCFF fits operations, but one shared claim cell cannot manufacture scenario-dependent guarantee economics. |
| Accounting-and-reinvestment guide and cached intangibles teaching | Matched R&D/amortization/SBC/lease treatment | Base year, switches, margins and overrides | Retained-GAAP basis is consistent and limitations are disclosed; no favorable one-sided add-back was found. |
| Uncertainty-and-bias guide | Scenario mechanisms, weights and risk location | Cases, weights and evidence uncertainty map | Scenarios are conditional outcomes; weights are disclosed assumptions; no risk is knowingly counted in both WACC and operations. |
| Review checklist plus a materially omitted topic: late capital/terminal transition | Independent bridge reconstruction | `sales_to_capital.value_late`, late overrides and terminal cells | Missing economic support is substantive and cannot be repaired with prose or threshold tuning. |

## Validation, diagnostics and app check

`uv run value companies/AVGO/valuation/drafts/20260924T000000Z/assumptions.yaml --validate` exits 1 after identifying the two bridge nulls and all four late-ratio nulls; the large-premium warnings are visible and permitted by explicit reasons. The supplied restricted diagnostic log likewise reports that no scenario can be computed. No full result, dry run, equity value or per-share value was produced. [September 24 validation and diagnostics logs]

The required app check is a separate **environment BLOCKED**, not a financial-review finding. The exact-candidate review-only walk did not launch because the Streamlit extra attempted to download missing `pillow==12.3.0` and the network tunnel failed; the installed environment had no Streamlit fallback. No page or interaction was claimed checked, and the recorded pre/post hash shows no save. Repeat that exact-target app walk when dependencies are available. [September 24 app-check record]

Do not promote or commit this candidate as a completed valuation draft, create a passing forecast snapshot, or direct the owner to compute it. Address the three blocker categories together, regenerate the readable draft, rerun validation and restricted diagnostics, repeat the exact-target app check, and return the candidate for pass 2 of this redraft cycle.

## Review evidence

- Candidate: `../valuation/drafts/20260924T000000Z/assumptions.yaml`.
- Active comparison: `../valuation/assumptions.yaml`; candidate differs only in drafting date and the added consensus/hypothesis paragraphs.
- Evidence: `../sources/FY2026-Q2/notes-valuation-evidence.md`, `notes-valuation-base.md`, `notes-valuation-peers.md`, and their cited cached originals/manifests.
- Command records: `FY2026-Q2-valuation-redraft-20260924-validation.txt`, `FY2026-Q2-valuation-redraft-20260924-diagnostics.json`, and `FY2026-Q2-valuation-redraft-20260924-app-check.md`.
- Historical audit evidence only: `FY2026-Q2-valuation-draft-review.md` and the preserved September 19 pass-1 snapshot/diagnostics.
