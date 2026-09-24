# AVGO — independent valuation draft review

_Final review: pass 2 of 2, September 19, 2026. Operating cutoff June 9, 2026. Independent reviewer: reviewer subagent, separate from the numerical analyst and runner. No full valuation was requested or disclosed._

## Final verdict: BLOCKED

The second pass accepts the corrected demand checks, growth explanations, guidance inventory and consolidation of shared workings. The late investment problem remains unresolved and is now represented honestly by null inputs. Every scenario stops; a readable draft and successful rendering are not a completed valuation. [Current assumptions; Final validation; Current diagnostics]

The reviewed final input is `../valuation/assumptions.yaml`, SHA-256 `02ed91bdefb6256c38b600829a015ae2ccc686c646724412aeae1442bc77ea6a`. Growth, margins, all first-five-year investment amounts and independently selected terminal return hypotheses are unchanged from pass 1. No owner-edited baseline exists. [Current assumptions; Pass 1 snapshot; Independent comparison]

### Remaining blockers and affected inputs

| Missing support | Current cell/state | Required resolution |
|---|---|---|
| Corporate investment carrying balance outside cash equivalents | `bridge.non_operating_assets.0.value: null` | A dated stock balance or a supported immateriality bound; cash-flow purchases/sales do not establish it. |
| Present value of the June 8 customer-lease backstop | `bridge.other_claims.0.value: null` | An independently supported contingent-claim treatment using deployment, default/recovery or fair-value evidence; neither zero nor the $29 billion maximum is a supported present value. |
| Capital required in years 6–10 and the path into mature economics | Every scenario's `sales_to_capital.value_late: null`; override entries 6–10 also null | A coherent source-grounded operating model connecting payment terms, contract assets, inventory/commitments, equipment replacement and IP spending to mature margins/mix, or a consistently reconciled alternative accounting basis. The model must explain the funding path; an exact future ratio need not appear in a filing. |

These are three distinct limitations. The third is an unsupported economic connection within a forecast, not a general objection to estimating uncertain futures. The earlier operating capital model did not justify the sudden funding increase at maturity; the analyst correctly withdrew that extension instead of inventing acquisitions or increasing terminal returns to remove a warning. The first-five-year budgets and 18%/22% mature-return hypotheses remain useful partial assumptions, but they do not complete the missing capital model. [Current assumptions, base sales-to-capital detail; Pass 1 diagnostic analysis below]

### Disposition of all first-pass repairs

| Repair | Second-pass disposition | Independent verification |
|---|---|---|
| 1. Late funding and terminal transition | **Still BLOCKED; representation corrected** | All four late ratios and all twenty late override entries are null. Story-to-numbers rows also display those nulls. The old investment schedules appear only as rejected diagnostic evidence. No new full-scenario result can be produced. |
| 2. Year-5/mature demand checks | **Resolved as explicit conditional forecasts** | WSTS 2027 non-memory 851,598 × 1.06⁴ = 1,075,123 for 2031; logic 522,820 × 1.06⁴ = 660,048. Each case now gives year-5 mix and chip/AI proportions. Software has a separate expansion of the existing 27,703 TTM franchise, scenario ranges, renewal/competition conditions, accounting caveats and revision triggers. These are analyst demand bounds, not disclosed TAM or retention statistics. |
| 3. Every growth decline above three points | **Resolved** | Independently enumerated all steps: bear 1→2 and 2→3; base, bull and management 1→2, 2→3, 3→4 and 4→5. Every required step has a matching component-growth and operating-driver row. |
| 4. Customer guidance inventory | **Resolved** | Added OpenAI 1.3-GW/2029 arrangement, Meta initial 1-GW delivery, other-customer orders and both Anthropic periods. Quotes match the cached call at lines 31–33. The Anthropic filing/call difference remains labeled and no GW/order amount is added to modeled revenue. |
| 5. Repeated shared workings | **Resolved for the requested consolidation** | Shared accounting resides in base-year detail, amortization in its memo cell, full capital history/method in base sales-to-capital detail and common terminal peer definitions in the base terminal cell. Other cases point to exact cells and retain their own annual arithmetic, ranges and triggers. The draft remains long because it retains four ten-year operating builds; no hard word limit was imposed. |

The software calculations reproduce independently: bear year-5 range 27,703–35,357 and year-10 range 26,345–40,988; base/management 38,855–48,822 and 38,855–62,311; bull 48,822–60,737 and 56,598–89,243. The selected endpoints lie within the corresponding bands. The source connection is the reported existing business and enterprise workload role, primary 9% quarterly recognized growth, the 31% near-quarter guide and the call's 17% ARR wording; the source's machine-transcript limitation still applies. Noncancelable license recognition differs from recurring spending, and the draft does not invent a retention rate, customer count or ARR dollar balance. [Current assumptions, revenue details; 10-K FY2025, Items 1/7 and revenue policy; 10-Q Q2 FY2026, revenue policy and Item 1A; Q2 FY2026 call]

### Final verification and all twenty checks

The current saved-file validation exits 1 with the two bridge nulls and four late-ratio nulls, not malformed schema. The current unmodified `--diagnostics-only` command also exits 1 because no complete scenario exists. It would be wrong to replace additional unknown capital inputs with arbitrary values just to obtain a diagnostic. The original operating-only JSON is preserved as `FY2026-Q2-diagnostics-initial-operating-only.json` and in the pass-1 snapshot; it is historical rejected-path evidence, not the final draft's cash-flow forecast. [Final validation; Current diagnostics; Diagnostic scope]

| # | Final answer | Finding |
|---|---|---|
| 1 | Yes | Distinct downside substitution, central repeat-design and upside share-win stories remain. |
| 2 | Yes | Latest run-rate, near-term primary guidance and explicit forward-window assumptions remain sourced and unchanged. |
| 3 | Yes, conditional demand support | Largest relevant company scale, year-5/year-10 chip bounds and separate software franchise ranges are present; competitive access and software renewal assumptions are explicit. |
| 4 | Yes as a margin hypothesis | Endpoint placement against reported/sensitivity peer margins and GAAP reconciliation remains unchanged; it does not by itself establish capital needs. |
| 5 | Yes for operating story | Segment mix, price/competition and spending burdens remain connected; overall cash-flow plausibility is blocked separately by late funding. |
| 6 | **BLOCKED** | Historical, latest-available and industry evidence is researched; late marginal capital efficiency and final-year implied book return are now unsupported/null rather than defended by an incomplete bridge. |
| 7 | Yes for supported early model | One-year investment lag, advance funding and no fictitious capital recovery in contractions remain; late mechanism is an identified gap. |
| 8 | Yes | Shared dated WACC build is unchanged and independently checked in pass 1; no operational-risk surcharge was invented. |
| 9 | **BLOCKED as a complete transition** | Mature return hypotheses retain independent support; the capital path into them is unavailable. No current final-year/terminal cash-flow check exists. |
| 10 | Yes | All scenario tables match current cells, explicitly including null late ratios and override entries. |
| 11 | Yes | Central operating judgments remain price-independent; new ranges describe business outcomes rather than a blanket safety haircut. |
| 12 | N/A | First owner draft; pass-1 to pass-2 changes respond to review, not new owner values or directional valuation targeting. |
| 13 | **BLOCKED only for identified inputs** | All supported arithmetic remains reproducible; new demand ranges/step-downs are explicit judgments with triggers. The three missing-support categories above remain unresolved. |
| 14 | Yes | Independently verified mature-peer definitions and limitations remain intact; no new peer-derived claim was fabricated. |
| 15 | Yes for revenue build/demand check | All forty annual component totals/growth paths are unchanged and reconcile; year-5 and year-10 checks now cover both businesses. This does not certify unmodeled late investment. |
| 16 | **BLOCKED for full model completion** | FCFF suitability and unsupported guarantee/late funding treatment are expressly recorded; the actual null state matches the evidence note. |
| 17 | **BLOCKED for holdings/backstop; otherwise consistent** | Retained rent, goodwill, R&D/SBC expense, shares and taxes are unchanged and checked; missing holdings/claim values are not replaced with zero. |
| 18 | Yes | Cash-flow, systematic-risk and discrete-claim locations remain distinct; weights are labeled assumptions and management is unweighted. |
| 19 | N/A | No eligible prior forecast; no hindsight reconstruction is implied. |
| 20 | Yes, deferred | Post-PASS snapshot requirements remain identified, but no passing forecast is created from a blocked draft. |

The 3P conclusions are now: **possible** demand scenarios within explicit conditional bounds; **plausible** revenue/margin mechanisms, but the full cash-flow plausibility of every scenario is **BLOCKED** by late capital needs; **probable** remains a scenario-level judgment supported by limited near-term delivery evidence, not measured 25/50/25 probabilities. Management's open-ended target floor remains a floor, with analyst timing and later completion separately identified. [Current assumptions; First-pass 3P/source checks below]

The second pass re-read the changed model/accounting/demand applications against the same applicable references, directly checked the new source wording and arithmetic, verified source paths resolve, compared all preserved numerical paths to the reviewed snapshot, and examined both current command outputs. No supported operating number changed to manufacture a pass. All source/peer reconstruction and primary-method checks retained below remain applicable to unchanged facts; the prior final-year results are expressly superseded by the null capital inputs. [Independent review checks; Current assumptions]

Both allowed full passes are now used. **Do not commit this as a completed draft, freeze a passing analyst forecast, or direct the owner to compute these unsupported inputs.** Preserve the draft and evidence, state the remaining work, and obtain owner authorization before extending the two-pass review limit. [AGENTS.md §13 and §18.7]

Final-review evidence: `FY2026-Q2-valuation-validation.txt`; `FY2026-Q2-diagnostics-current.txt`; `FY2026-Q2-diagnostics-scope.md`; `../valuation/assumptions.yaml`; `../valuation/assumptions.md`. Primary-source mappings and the preserved first-pass analysis follow.

---

## Preserved first-pass analysis — superseded where stated above

_Pass 1 completed September 19, 2026. The following findings and conditional operating diagnostics describe the preserved initial snapshot, not the final null-capital draft._

## Verdict: BLOCKED, with operating revisions required

The two unsupported bridge balances correctly remain null: the present claim value of the June 8 customer-lease backstop, and the carrying value of corporate investments outside cash equivalents. The backstop's $29,000 million maximum is neither expected loss nor fair value. These missing facts prevent a completed equity valuation in every case. They do not prevent the operating review below. [10-Q Q2 FY2026, Note 11 and cash-flow statement; Valuation base evidence]

The operating arithmetic reconciles, but the transition into the mature period is not yet economically established. In particular, the base, bull and management cases generate final-year book returns far above the named mature comparators, then more than triple net investment in the next year with little change in growth, margins or taxes. The draft asks the reviewer to investigate that difference but does not yet explain the timing or support it. Raising terminal returns to clear the warning is not an acceptable repair. [Pass 1 assumptions; Restricted diagnostics; AGENTS.md §18.2 and §18.4 rules 5, 15–16]

Reviewed snapshot: `FY2026-Q2-valuation-pass1/assumptions.yaml`, SHA-256 `d626d190d64af42ac933a1a69e0ae10f1140e388dbd8a046435c1096a7575412`. The accompanying readable draft and restricted diagnostics are preserved in that folder. Source preparation before this snapshot was not a review pass. [Review artifacts]

### Consolidated repair list for the analyst

1. **Explain and, where required, repair late reinvestment and the terminal transition.** The central case's year-10 investment is $5,632 million, versus $18,247 million in the terminal year; bull is $7,745 million versus $23,972 million, and management is $6,094 million versus $19,706 million. The absent internally developed R&D asset and historical acquisition accounting affect both years; they do not by themselves explain a sudden threefold increase in annual funding. Show whether late forecast growth underpays for capital, whether future growth requires a different type of investment, or whether a supported economic discontinuity warrants keeping the warning. Compare the resulting final-year returns with observed comparators on the stated basis and justify any remaining excess. Revise the capital path for economics if needed, preserving independently selected terminal returns unless their own evidence changes. [Restricted diagnostics; Pass 1 assumptions, scenario reinvestment and terminal cells]
2. **Complete demand checks at both year 5 and year 10.** The WSTS extrapolation and NVIDIA scale comparison are useful; the current detail only calculates market proportions for year 10. Show year-5 semiconductor/AI proportions against an appropriately dated version of the same bound, and each case's year-5 mix. The software comparison explicitly says PBP/Cisco scale does not prove VMware demand: add a defensible source-grounded operating/demand check, such as a transparent expansion of the existing recurring business with a supported range and renewal/competition conditions. A precise 2036 TAM is not required, and the exact future rate may remain an analyst judgment; peer size alone cannot serve as the demand bound. If the permitted evidence cannot support such a substitute, leave that dependent check BLOCKED. [WSTS spring 2026; Q2 FY2026 call; Pass 1 assumptions, revenue details; checklist 3 and 15]
3. **Name the driver of each growth step-down exceeding three percentage points.** The builds reconcile, and the overall stories mention maturation, deployment timing and competition, but several successive reductions currently share a generic explanation. Add a short year-to-year explanation identifying which operating component slows and why for every applicable step, including the management-completion path. This is an explanation requirement, not a request to tune growth rates. [Pass 1 assumptions, revenue details; AGENTS.md §18.4 rule 11]
4. **Finish the management guidance inventory.** Record the unmodeled customer deployment commitments already present in the permitted call: OpenAI 1.3 GW in 2027 within the 10-GW 2029 arrangement; Meta's initial 1-GW order beginning delivery in the second half of 2027; the two other customers' $6 billion orders; and Anthropic's 2026/2027 deployment wording, explicitly retaining the documented discrepancy with the April filing. Mark these as unmodeled context and do not convert GW or orders into additional revenue. The guidance floor and May-to-May mapping already distinguish company wording from analyst completion correctly. [Q2 FY2026 call, lines 31–33; 8-K April 6; outlook.md §3–§5; AGENTS.md §18.4 rule 4]
5. **Consolidate repeated shared detail.** The YAML contains about 21,300 whitespace-delimited words, substantially repeating the same acquisition/R&D discussion and full historical-capital explanation in multiple cells of all four cases. Keep common accounting, history, benchmark definitions and the amortization schedule once in an appropriate shared input detail, reference it by exact cell from case details, and preserve case-specific bridges, ranges, triggers and annual tables. This preserves the evidence while making owner review practical; no new hard word limit is imposed. [Pass 1 assumptions; AGENTS.md §3 and §18.4]

The investment and backstop gaps are distinct from these repairable operating/explanation issues. The reviewer made no numerical or judgment edits. A wording issue concerning bear-case SBC was returned to the analyst and corrected before the snapshot: forecast SBC remains above current TTM dollars, but does not rise every year. [Pass 1 assumptions]

## Independent fact and bridge reconstruction

All amounts below are USD millions, except shares (millions), rates and ratios. Direct primary-source checks, rather than agreement with gatherer notes alone, support the following results. [Sources listed below]

| Input or evidence | Independently reproduced result | Direct locator and finding |
|---|---:|---|
| TTM revenue | 63,887 + 41,498 − 29,920 = **75,465** | K25 statement of operations, line 1661; Q26 line 219. Pass. |
| TTM GAAP EBIT | 25,484 + 19,351 − 12,089 = **32,746** | K25 line 1687; Q26 line 245. Interest/other income excluded. Pass. |
| TTM acquired amortization | 8,062 + 3,936 − 3,984 = **8,014** | K25 lines 1669/1681; Q26 lines 227/239 and Note 9 reconciliation. Pass. |
| TTM SBC | 7,568 + 4,268 − 3,051 = **8,785** | K25 cash flow and Note 11; Q26 Note 7, line 1099. Pass. |
| TTM R&D | 10,977 + 5,960 − 4,946 = **11,991** | K25 line 1677; Q26 line 235. Pass. |
| TTM tax rate | (−397 + 1,666 − 107) / (22,729 + 18,325 − 10,575) = **3.81246%** | Both statements of operations. This is reported tax, not normalized cash tax. Pass. |
| TTM operating margin | 32,746 / 75,465 = **43.39230%** | Same reported figures. Pass. |
| Cash | **19,628** | Q26 balance sheet, line 135; cash-equivalent composition is already included. Pass. |
| Debt carrying amount | 66,720 − 1,813 = **64,907** | Q26 Note 6, lines 999–1003; alternative fair value 62,505 at line 1035. Pass. |
| Rental-basis starting capital | 87,691 + 64,907 − 19,628 = **132,970** | Q26 balance sheet. Goodwill retained; no ordinary lease debt or research asset added. Pass as disclosed book-capital proxy. |
| Latest-quarter diluted shares | 4,747 + 129 = **4,876** | Q26 Note 5, lines 807–811. Not period-end or H1 shares. Pass. |
| Future awards | **183** RSUs; **20,106** unrecognized compensation | Q26 Note 7; not added to shares or deducted as debt again. Pass. |
| Ordinary leases | Prior FY liability **1,325**, expense **182**, cash payments **277** | K25 Note 6. Zero bridge deduction denotes retained-rent accounting, not an absent liability. Pass. |
| Pension claim | Gross underfunded plans **96**; surplus **57**; net **39** | K25 pension table. Dated gross-deficit carryforward is identified and small; inaccessible surpluses are not cash. Pass with explicit proxy limitation. |
| Uncertain-tax claim | **1,662** | Q26 Note 10, line 1233. Undiscounted convention and exclusion from normal future earnings taxes are explicit. Pass. |
| Corporate investment balance | **Not established** | Q26 purchases 137 / sales 283 are flows, not stock. Null is appropriate; bridge BLOCKED. |
| Customer backstop | **29,000 maximum**, expected/present claim not established | Q26 Note 11, line 1255; June 9 Apollo releases supply no default/recovery/fair-value bridge. Null appropriate; BLOCKED. |
| Current run-rate | 22,187 / 15,004 − 1 = **47.874%** | Q2 release and Q26. Next-quarter total guidance 29,400 explains why forward growth may accelerate. Pass. |
| Segment starting point | **47,762** chips + **27,703** software = 75,465 | K25 Note 13 + Q26 Note 9, using the same FY+H1−H1 calculation. Pass. |
| Acquired amortization schedule | **27,583** remaining | Q26 Note 4. Ten rolling-year deductions sum to 27,583; later-bucket allocation is clearly an analyst interpolation with a range/trigger. Pass. |
| WSTS non-memory bound | 35,712 + 46,436 + 23,002 + 101,662 + 121,966 + 522,820 = **851,598** for 2027 | WSTS table, p.2. At assumed 6% for nine years: approximately **1,438,757**. This is a broad ceiling, not AVGO's TAM. |
| NVIDIA current scale | 215,938 + 81,615 − 44,062 = **253,491** TTM | FY2026 and Q1 FY2027 primary releases. System/platform revenue differs from Broadcom chips. Pass as scale context. |
| Borrowing rate | 4.94% + (4.95% − 4.18%) = **5.71%**, rounded to **5.7%** | January note issue and FRED debt-proxy record. Historical coupon/Treasury spread is a labeled financing proxy, not current quoted yield. Pass. |
| Cost of capital | D/E = 64,907 / (357.61 × 4,876) = **0.03722358**; beta **1.5466556** after leverage; WACC **11.01494%** | Dated market record, cash-corrected Semiconductor beta 1.5046493, 25% marginal tax and 5.7% debt rate. Independently reproduced. |

No fabricated reported base number was found. The null balances are visible gaps, not invented zeros. No claim is made that an exact future growth rate, margin or investment ratio appears in a historical filing. [Pass 1 assumptions]

### Mature-peer verification

The peer screen actually researched Qualcomm, Cisco and Microsoft, plus Broadcom's own history. It includes an eroding handset franchise and an acquisition-heavy slower-growth network company, rather than only exceptional successful firms. Microsoft PBP is used for software margin/scale only; its unreported segment capital is not replaced with consolidated capital. [Peer primary filings; Mature benchmark evidence]

| Comparator | Independent FY2025 calculation | Definition assessment |
|---|---|---|
| Qualcomm | EBIT 12,355 / sales 44,284 = **27.90%**; 12,355 × 79% / (26,274 + 14,634 − 13,300) = **35.35%** | Includes patent royalties; excludes no SBC/R&D; restricted cash remains in capital. Current cash plus securities is 5,520 + 4,635 = 10,155. |
| Cisco | EBIT 11,760 / sales 56,654 = **20.76%**; 11,760 × 79% / 58,565 = **15.86%** | Retains goodwill, acquisition amortization and SBC; software/system scope differs from chip revenue. |
| Microsoft PBP | 69,773 / 120,810 = **57.75%** | Allocated costs included; no segment capital or segment tax assumed. |
| Microsoft consolidated | 128,528 × 79% / (268,477 + 51,630 + 27,145 − 75,543) = **37.37%** | Opening debt includes short-term 6,693; finance leases added separately; operating leases retain rent treatment. |
| Broadcom | 25,484 × 79% / 125,896 = **15.99%**; with 8,062 amortization sensitivity: **21.05%** | Goodwill retained, R&D/SBC expensed. Sensitivity is not relabeled GAAP or a future marginal return. |

The peer definitions, source dates, fiscal periods and limitations are adequate. Broad industry sales/capital of 1.2067× semiconductor and 1.5382× software are explicitly separate aggregates; they are not multiplied by unrelated average margins to fabricate an observed industry return. The remaining defect is the connection from these observations to the forecast's much higher final-year returns, not a missing peer-count requirement. [Peer primary filings; Damodaran capex data; Pass 1 assumptions]

## Operating reconstruction and transition

The reviewer independently rebuilt all 40 annual company revenue totals from AI + other chips + software, compounded each stored growth path, recomputed GAAP margin from segment profit less SBC, other costs and acquired amortization, and reproduced all 40 net-investment overrides from the stated funding and physical-depreciation rules. Revenue error is below $0.01 million and investment rounding below $0.001 million; no material arithmetic error was found. The amortization deduction is reversed once through net investment and no R&D/SBC expense is added back. [Pass 1 assumptions; Independent review calculations]

Example, base year 1: chips 89,800 × 64% + software 33,000 × 79% − 122,800 × 9.5% − 7,349 = EBIT 64,527, margin 52.5464%. Net investment = 31,900 / 2.5 + 122,800 × 0.5% − 7,349 = 6,025. The physical check has capex 1,842 and depreciation 726.9, leaving 12,258.9 of the pre-amortization budget for other operating funding. This is transparent judgment arithmetic, not management capex guidance. [Pass 1 assumptions, base margin and investment details]

The operating-only diagnostic command uses temporary in-memory zero placeholders solely for the two unresolved bridge amounts. Those bridge values do not affect revenue, EBIT, investment, book returns or transition checks; the saved YAML remains null. This is conditional operating evidence and does not establish a complete or passing equity valuation. The scope file documents the command and restrictions. [Restricted diagnostic scope]

| Case | Year-10 FCFF | Terminal FCFF | Change | Year-10 return, opening book capital | Terminal return | Year-10 / terminal investment |
|---|---:|---:|---:|---:|---:|---:|
| Bear | 31,419 | 27,454 | −12.62% | 27.00% | 9.44% | 2,732 / 7,380 |
| Base | 100,664 | 91,237 | −9.36% | 58.18% | 18.00% | 5,632 / 18,247 |
| Bull | 162,932 | 151,825 | −6.82% | 77.57% | 22.00% | 7,745 / 23,972 |
| Management | 108,695 | 98,528 | −9.35% | 60.24% | 18.00% | 6,094 / 19,706 |

All cash-flow drops are smaller than 15%. The non-bear warning is triggered because terminal return is less than half the final explicit year's return; the engine's generic wording about a large cash-flow drop does not identify that distinction correctly. This review uses the actual data and house conditions. The bear is exempt from the warning but its economic transition is still examined. [Restricted diagnostics; AGENTS.md §18.2]

The selected terminal returns themselves have a defensible independent placement: 18% around Broadcom/Cisco normalized outcomes and 22% for an upside franchise still below Qualcomm/Microsoft's research-light book returns. At terminal WACC 9.44%, the premiums are 8.56 and 12.56 percentage points; the explicit large-premium flags are correct. Growth/return implies terminal reinvestment fractions of 16.67% and 13.64%. The unresolved issue is the path into those economics and support for preceding 58–78% book returns. [Pass 1 assumptions; Mature benchmark evidence; Restricted diagnostics]

## 3P test

| Story | Possible | Plausible | Probable as a scenario, not a measured probability |
|---|---|---|---|
| Bear | Total 126,100 and chips 92,600 are below the broad WSTS extrapolation; software bound still needs the explanation in repair 2. | Customer substitution, weak renewals and margin compression are coherent; mature funding transition still needs explanation. | Concentration and self-design risk support a downside outcome; available evidence does not prove a 25% probability. |
| Base | Chips 231,800 are 16.1% of the broad non-memory bound and AI 23.7% of the logic ceiling; source-grounded access/demand conditions need the complete check. | Repeat designs, software retention and expiring acquired charges support strong profits; final-year return/funding remains REVISE. | One quarter of guidance delivery is positive evidence, not a durable forecasting record; the 50% weight is a house assumption. |
| Bull | Chips 348,600 require 24.2% of the broad ceiling and AI 36.2% of logic; this is a demanding competitive outcome, not established market access. | High differentiated-chip margins are possible, but 77.6% final book return and the subsequent funding step remain unresolved. | Multiple design wins and deployments supply an upside mechanism; 25% is explicitly assumed, not inferred statistically. |
| Management | Its near-term floor/timing bridge is arithmetically possible; later demand is analyst completion with the same check outstanding. | The case is transparently hybrid and unweighted; capital transition requires the central repair. | Guidance is management's stated ambition. “In excess of 100,000” has no midpoint; the selected floor is clearly labeled. |

There is no AVGO scorecard or eligible prior analyst forecast. The limited contemporaneous check is Q1's $22,000 million Q2 revenue guide versus $22,187 million actual, and approximately 68% adjusted EBITDA guide versus 15,244/22,187 = 68.71% actual. It supports one delivered quarter, not a multi-year forecast track record. [Q1 FY2026 release; Q2 FY2026 release; Research metadata]

## All twenty checklist questions

| # | Answer | Evidence and disposition |
|---|---|---|
| 1 | Yes | Bear explicitly has delays/self-design and weaker renewals; base has repeat programs and bargaining; bull has sustained share wins and supplier/customer funding. Three business outcomes. |
| 2 | Yes, with explicit scenario judgments | Latest 47.87% growth and Q3 29,400 guidance are stated; each first-year AI build separates H2 FY2026 and H1 FY2027. Different downside/upside delivery is a forecast judgment, not an invented reported event. |
| 3 | REVISE | NVIDIA TTM 253,491 supplies relevant leader-scale context, WSTS supplies a labeled broad ceiling; year-5 and software demand checks require repair 2. |
| 4 | Yes | GAAP endpoint margins 36.11/50.33/54.76% are placed against own amortization sensitivity, Qualcomm/Cisco and PBP; segment exclusions are explicitly reconciled. Exact future margins remain judgments. |
| 5 | Yes on the stated scenarios | High chip scale relies on repeated differentiated IP and operating leverage, with falling mature chip margins and smaller software mix; this is not a niche business extrapolated without mix arithmetic. Funding plausibility is separately unresolved. |
| 6 | REVISE | Lagged own history, unusable acquisition-distorted denominators, latest unavailable forward numerator, peer stock ratios and industry ratios are shown; final 58–78% book returns are not yet adequately supported against them. |
| 7 | Yes for mechanism | One-year lag and explicit budgets finance next-year growth; no mechanical inventory recovery in contraction; acquisitions include stock consideration. Magnitude/late maturity still covered by repair 1. |
| 8 | Yes | Shared 11.01494% WACC independently reproduces; dated industry WACC 10.55% is context, not a mandatory band; debt proxy is explicit, with operating/default losses not added again to WACC. |
| 9 | REVISE transition, supported terminal selection | Terminal 18/22% selected independently from mature evidence; no threshold tuning found. Actual late-to-terminal funding must be repaired or justified, rather than leaving instructions to the reviewer. |
| 10 | Yes | Each scenario's table covers growth, margin, ratios, overrides, taxes and terminal inputs; stored number lists match the cells. Shared weights/build are explained separately. |
| 11 | Yes, judgment disclosed | Central AI 72,000 sits within an explicit 65,000–80,000 range with delivery/timing risk; no price target or “choose lower for safety” rule drives it. Tax-claim carrying convention is separately disclosed, not hidden in the operating base. |
| 12 | N/A | Initial draft; no prior owner values or draft exists to compare. |
| 13 | REVISE / BLOCKED as specified | Revenue, margin, taxes, physical budget, market build and terminal target arithmetic reproduce; material ranges/triggers are explicit. Late funding/demand explanation remains REVISE, and the two missing bridge amounts remain BLOCKED. |
| 14 | Yes | Primary peer filings were read and reconstructed above; fiscal periods, SBC/R&D, goodwill, rent, finance leases and absent segment capital are differentiated. |
| 15 | REVISE | Every explicit year reconciles; year-5 proportions/mix and software operating demand need repair 2; generic large-market/peer-size observations do not finish the check. |
| 16 | Yes for routing, BLOCKED for completed equity computation | Evidence note identifies operating FCFF fit and the missing contingent-claim treatment; YAML reflects the limits rather than forcing the guarantee into company failure. |
| 17 | Yes except stated holdings/claim gaps | R&D/SBC expensed, rent retained consistently, goodwill retained, diluted shares not double counted; taxes normalize with explicit limitations and old tax claim separated. Holdings/backstop nulls prevent full completion. |
| 18 | Yes | Demand/substitution affect operations; systematic risk affects shared WACC; customer guarantee is separate; company failure overlay is zero by stated going-concern convention; 25/50/25 weights are assumptions, not confidence limits. |
| 19 | N/A | No eligible original forecast; no retrospective baseline or automatic forecast correction fabricated. |
| 20 | Yes, prospective only | Evidence note and runner workflow specify exact bytes/hash, actual UTC creation, model windows, accounting definitions, origin and resolved non-price inputs after PASS. Execution is withheld while BLOCKED; no passing forecast is claimed. |

## Reference use, accounting capability and reader check

| Reference read | Applicable judgment | Cell/evidence section | Finding |
|---|---|---|---|
| AGENTS.md §§3, 13, 18; draft skill; playbook; review checklist | Review independence, null handling, owner boundary, two-pass limit | Entire review | Applied; missing facts cannot receive PASS with a caveat. |
| Model-selection guide | Mixed operating/financing exposure | Evidence model fit; bridge backstop | FCFF represents operations; engine does not estimate scenario/year guarantee defaults and recoveries. |
| Accounting-and-reinvestment guide; `intangibles.txt`, PDF pp.9–10 and equity compensation discussion | R&D, SBC, goodwill and matched profit/capital treatment | Switches, base, margin/investment, share bridge | Retained reported basis is disclosed; no profit-only capitalization or SBC add-back. R&D omission limits book-return comparability. |
| Business-drivers guide; `growth-and-value.txt`, “Paying for Growth,” “Excess Return Effect,” “Two Dangerous Practices” | Growth funding and mature reinvestment | Scenario overrides and terminal cells | Arithmetic passes; future marginal return is distinct from historical average, but the funding transition still needs its own support. |
| `terminal-value.txt`, PDF pp.10–12, “Project Returns” and “Reinvestment and Retention Ratios” | Mature risk, returns and growth/return investment | Terminal inputs and diagnostic investigation | Premiums are independently justified; the threshold is not a target. No free perpetual growth allowed. |
| Uncertainty guide; `uncertainty.txt`, “Dealing with Uncertainty,” points 2–6 | Fact gaps versus uncertain forecasts; risk location | Evidence uncertainty table; bridge and cases | Explicit future judgments can pass; undisclosed historical holdings and unsupported guarantee value remain gaps. |
| `narrative-and-numbers.txt`, five-step process | Stories, economic reality checks and revision triggers | Story tables, ranges, triggers | Stories and numerical bridges mostly complete; demand/transition revisions are identified. |
| Forecast-learning guide; same original feedback discussion | No hindsight baseline and conditional first snapshot | Evidence completion section | No prior forecast; snapshot only after PASS. |
| Model-selection guide, shrinking-business/capital-release subsection | Reviewer emphasis on a material downside topic | Bear negative-growth years and overrides | The draft does not turn falling sales into invented book-value inventory recovery; negative net investment is explained by acquired amortization. |

Stories have four or five connected sentences and contain no crowded numerical lists. Reasons are generally one to three sentences, with working numbers in `detail`; no substantive YAML comments hide assumptions. Repetition in the detailed workings still needs the consolidation in repair 5. Necessary technical terms are primarily in the detailed accounting workings; the headline stories remain understandable. The source map resolves the cited primary files, external-company cache and method notes separately. The reader should be told that market rates/ERP are separately dated September inputs while operating evidence remains June 9. Engine manual-input dates are entry dates; the source record supplies the actual September 17 risk-free and September 1 ERP observation dates. [Pass 1 assumptions; Market inputs; Restricted diagnostics]

## Sources and review evidence

- **K25 / [10-K FY2025]:** `../sources/FY2026-Q2/10-K-FY2025.txt`, statements and Notes 4, 6, 10–13; FY ended November 2, 2025.
- **Q26 / [10-Q Q2 FY2026]:** `../sources/FY2026-Q2/10-Q-FY2026-Q2.txt`, balance sheet, statements and Notes 4–11; filed June 9, 2026.
- **[Q1 FY2026 release], [Q2 FY2026 release], [Q2 FY2026 call]:** `../sources/FY2026-Q2/press-release-FY2026-Q1.txt`, `press-release.txt`, `transcript.txt`. Call is a third-party machine transcript; guidance wording is quoted, reported numbers checked against primary releases/filings.
- **[8-K April 6]:** `../sources/FY2026-Q2/8-K-2026-04-06-google-anthropic.txt`.
- **[Valuation base evidence], [Mature benchmark evidence]:** `../sources/FY2026-Q2/notes-valuation-base.md`, `notes-valuation-peers.md`; direct primary locators verified above.
- **[Peer primary filings]:** `../sources/FY2026-Q2/QCOM-10-K-FY2025.txt`, `CSCO-10-K-FY2025.txt`, and `../../MSFT/sources/FY2026-Q4/10-K-FY2025.txt` (only the eligible FY2025 filing reused).
- **[WSTS spring 2026], [NVIDIA releases], [Apollo releases]:** `../sources/FY2026-Q2/wsts-spring-2026.txt`, `NVDA-release-FY2026-Q4.txt`, `NVDA-release-FY2027-Q1.txt`, `apollo-platform-release-2026-06-09.txt`, `apollo-financing-release-2026-06-09.txt`; original URLs/dates in source manifests.
- **[Market inputs], [FRED debt proxy], [January notes]:** `../sources/FY2026-Q2/valuation-market-inputs.txt`, `fred-treasury-debt-proxy.txt`, `8-K-2026-01-13-notes-offering.txt`.
- **[Damodaran data]:** `../../../tools/valuation/data/damodaran/{betas,capex,wacc,margin}.csv` and `MANIFEST.md`.
- **[Method originals]:** `../../../tools/valuation/damodaran-notes/sources/{intangibles,growth-and-value,terminal-value,uncertainty,narrative-and-numbers}.txt`; locators in the reference table.
- **[Pass 1 assumptions], [Restricted diagnostics], [Review artifacts]:** `FY2026-Q2-valuation-pass1/`; active diagnostic scope in `FY2026-Q2-diagnostics-scope.md` explains conditional bridge placeholders. The independent reviewer reproduced operating arithmetic without calculating asset, equity or per-share values.

One full pass is complete. Apply the entire repair list before the second full pass; no completed-draft commit or passing forecast record is authorized by this BLOCKED verdict. [AGENTS.md §13 and §18.7]
