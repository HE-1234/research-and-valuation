# AVGO — valuation base, capital history and accounting screen

_Prepared 2026-09-18. Evidence cutoff 2026-06-09. Money is USD millions; shares are millions. This is source analysis for an initial assumptions draft, not a valuation result. All arithmetic below is calculated from the cited disclosures._

## Decision and unresolved input

Broadcom remains an operating company with identifiable revenue, operating profit and investment; a consolidated FCFF model can describe its semiconductor and infrastructure-software operations if the forecast distinguishes their demand and capital needs. The June 8, 2026 customer-lease backstop adds a material contingent financing exposure, but its existence alone does not establish that the entire company needs a financial-company model. [10-Q Q2 FY2026, Notes 9–11]

**Required check BLOCKED: the value of the Apollo customer-lease backstop.** Its maximum contractual exposure is $29,000, not a disclosed current debt balance or expected loss. Eligible sources establish a five-year term, deployment-dependent exposure and recovery remedies, but do not establish an initial fair value, fee, actual draw schedule, default probability, expected recovery or supported expected-loss range. The June 9 platform/financing releases add committed financing and deployment facts without supplying those inputs. Do not silently record this claim as zero, deduct the maximum as a certain current liability, or invent a discount-rate premium. [10-Q Q2 FY2026, Note 11 and Part II Item 5; Apollo platform release 2026-06-09; Apollo financing release 2026-06-09]

A defensible present value of the claim could be expressed in the engine's existing `bridge.other_claims` field; evidence for the amount is presently missing. A scenario-specific operating loss could also be represented through a properly explained operating forecast if it is truly an operating cost and supported. The current engine has no distinct scenario/year guarantee-payment schedule; `probability_of_failure` applies to failure of Broadcom as a whole and is not a substitute for an individual customer's default. A shared static claim cannot represent different losses conditional on each scenario without a supported approximation. The affected claim value should remain explicitly unsupported/null pending a defensible treatment. [Engine, lines 311–321, 537–546, 561–567]

## Reference → decision → affected evidence

| Reference | Decision | Affected inputs/evidence |
|---|---|---|
| `model-selection.md`, operating company / mixed business / boundary | FCFF suitable for operations; separately assess the guarantee instead of relabeling all Broadcom as a bank | Segment forecast, other claims; guarantee remains unresolved |
| `accounting-and-reinvestment.md`, acquired assets and reinvestment; `growth-and-value.txt`, Paying for Growth / Excess Return Effect | Show full acquisition economics and distinguish negative GAAP net investment from a positive growth-capital ratio | Historical ratios below; reinvestment path; goodwill retained |
| `accounting-and-reinvestment.md`, R&D; `intangibles.txt`, lines 271–314 | Retaining R&D expense is a disclosed simplification; switching it on requires matched historical periods, useful lives, research investment and tax reconciliation | `capitalize_rnd`, capital and forecast margin/reinvestment |
| `accounting-and-reinvestment.md`, leases and equity compensation | No liability-only lease adjustment without checking profit/cash treatment; preserve future SBC expense and distinguish awards already represented in shares | Lease bridge, diluted shares, margin |
| AGENTS.md §18.4 rules 1, 12, 15–16 and §18.11 | Preserve reported base; label all proxies and gaps; do not let schema validation convert missing material evidence into support | Entire note and dependent assumptions |

## Reported TTM base

TTM is Q3 FY2025 through Q2 FY2026, ending May 3, 2026. Reconstruction is FY2025 plus H1 FY2026 minus H1 FY2025; the two half-year columns are from the May 3, 2026 10-Q. [10-K FY2025, Item 8; 10-Q Q2 FY2026, Item 1]

| Input | FY2025 | H1 FY2026 | H1 FY2025 | TTM calculated | Exact cached text locators |
|---|---:|---:|---:|---:|---|
| Revenue | 63,887 | 41,498 | 29,920 | **75,465** | K25:1661; Q26:219 |
| GAAP operating income | 25,484 | 19,351 | 12,089 | **32,746** | K25:1687; Q26:245 |
| Acquired-intangible amortization | 8,062 | 3,936 | 3,984 | **8,014** | K25:1669+1681; Q26:227+239,1193 |
| Stock-based compensation | 7,568 | 4,268 | 3,051 | **8,785** | K25:3309; Q26:1099 |
| R&D expense | 10,977 | 5,960 | 4,946 | **11,991** | K25:1677; Q26:235 |
| Pretax income | 22,729 | 18,325 | 10,575 | **30,479** | K25:1693; Q26:251 |
| Tax provision/(benefit) | (397) | 1,666 | 107 | **1,162** | K25:1695; Q26:253 |
| Operating cash flow | 27,537 | 18,753 | 12,668 | **33,622** | K25:1803; Q26:347 |
| Property/equipment purchases | 623 | 481 | 244 | **860** | K25:1811; Q26:351 |
| Depreciation | 574 | 313 | 284 | **603** | K25:1777; Q26:321 |

Reported TTM operating margin is 32,746 / 75,465 = **43.3923%**; acquired amortization is 10.6195% of revenue and R&D is 15.8895%. Reported effective tax rate is 1,162 / 30,479 = **3.8125%**. H1 FY2026 alone is 1,666 / 18,325 = 9.0914%, and Q2 alone is 820 / 10,130 = 8.0948%. These are reported accounting outcomes, not forecast tax assumptions. [Calculation: 10-K FY2025, Item 8; 10-Q Q2 FY2026, Item 1]

The FY2025 tax benefit includes releases/settlements and excess SBC deductions; fiscal 2026 is subject to CAMT, with a full valuation allowance against CAMT credits. Singapore incentives expire through November 2030 and the Malaysian holiday in FY2028; the company says global minimum tax provisions have materially increased its taxes. A forecast must normalize these items and explain cash-tax timing; neither a permanent 3.8125% tax rate nor an immediate jump to a house 25% rate follows mechanically from these disclosures. [10-K FY2025, Note 12, lines 3439–3527; 10-Q Q2 FY2026, Note 8, line 1131 and Item 1A]

Preserve GAAP EBIT and propose no generic restructuring/acquisition/SBC add-back: restructuring repeats across the five-year record, while the $315 excise-tax reversal in H1 FY2026 is in **other income**, already outside EBIT. Adding it to or subtracting it from operating income would be wrong. [10-K FY2025, Item 8, lines 1671,1683; 10-K FY2023, Item 8, lines 1913,1925; 10-Q Q2 FY2026, Item 2]

## Balance sheet and equity claims

| Item | Supported amount / status | Treatment and locator |
|---|---:|---|
| Cash and equivalents, May 3 | **19,628** | Q26:135; Treasury bills 2,985, deposits 4,003 and money-market funds 2,801 are already included; do not add twice (Q26:621–623) |
| Debt, book carrying amount | **64,907** | Q26:999–1003 = principal66,720 less discounts/issuance costs1,813 |
| Debt, principal | **66,720** | Q26:999,1061; clearly label choice if used in equity bridge |
| Debt, disclosed fair value | **62,505** | Q26:1035; useful comparison, not another liability to add |
| Stockholders' equity | **87,691** | Q26:193 |
| Latest-quarter diluted weighted-average shares | **4,876** | Q26:807–811; 4,747 basic plus129 award dilution |
| Period-end common shares | 4,758 | Q26:185; do not substitute for mandated latest-quarter diluted denominator |
| Operating-lease liabilities at May 3 | **Not disclosed in eligible text/companyfacts extract** | Last disclosed FY2025 amount1,325 =144 current+1,181 long-term, K25:2553–2585; 1,325 carry-forward is an assumption, not a May3 fact |
| Operating-lease ROU asset at FY2025 | 1,318 | K25:2559; not a nonoperating asset |
| Finance leases | FY2025 zero | K25:3177,3183; Q26 debt table has notes and loans and no separate finance-lease line |
| Corporate investments other than cash equivalents | **Carrying balance not disclosed in reviewed eligible text** | Purchases137 and sales283 in H1 confirm investments exist (Q26:353–355). Do not call zero a reported balance or infer ending holdings from net purchases alone |
| Minority interest | No separately reported balance | Q26 balance sheet has total equity87,691 and no noncontrolling-interest line; companyfacts total equity including NCI equals87,691. Zero *separately reported* minority claim is supported, not proof no economically immaterial subsidiaries exist |
| Preferred stock | None issued/outstanding | Q26:183 |
| Pension deficit, latest disclosed | Net39; gross underfunded plans96 | K25:2809–2817,2825–2829,2841–2845. Overfunded plans57 offset aggregate39; inaccessible pension surplus must not be treated as cash. No May3 update located |
| Unrecognized tax benefits and accrued interest/penalties | **1,662** | Q26:1233; timing not reliably estimable. Distinct contingent tax claim; ensure it is not both separately deducted and embedded in forecast cash taxes |
| Legal contingency accrual | No material accrued/disclosed amount | Q26:1247; do not extrapolate this statement to the separately disclosed June8 guarantee |
| Customer-lease backstop | Maximum29,000; fair/expected value unsupported | Q26:1255,2213; new Apollo release evidence discussed below |

Book capital **before operating leases** is 87,691 + 64,907 − 19,628 = **132,970**. Carrying forward the FY2025 lease liability gives **134,295**, but this is expressly a proxy. With principal debt instead of book debt the same lease proxy gives **136,108**; do not silently change debt basis between history, ROIC and the bridge. Goodwill97,801 and acquired intangibles28,333 remain in reported book equity; no goodwill removal is proposed. [Calculation: 10-Q Q2 FY2026, balance sheet and Note 6; 10-K FY2025, Note 6]

With the 134,295 capital proxy, reported TTM EBIT and reported tax give a current ROIC diagnostic of **23.4540%**. This includes goodwill, expenses R&D, uses ending capital rather than an annual average and inherits the unusually low reported tax rate; it is not an estimate of return on future investment and not a terminal target. [Calculation: preceding base/bridge sources]

The quarter's diluted denominator already contains129 million dilutive award shares;183 million RSUs remain outstanding and20,106 of unrecognized compensation is expected over3.0 years. The outstanding RSU count cannot simply be added to diluted shares, because the measures overlap and vesting/service conditions differ. Continue SBC expense in the forecast and describe future award dilution; do not subtract unrecognized future compensation again as a present debt claim. [10-Q Q2 FY2026, Notes 5 and 7, lines 807–811,1099–1127]

The ordinary lease liability is small relative to base capital, but retaining the whole lease expense in operating profit **and** subtracting lease debt without profit/reinvestment reconciliation is conceptually inconsistent. FY2025 lease expense182, cash lease payments277, new ROU assets220 and lease discount rate4.78% are disclosed; current-period lease detail is not. A retained small simplification requires an explicit explanation and reasonable bound, or a consistent rental treatment; it must not be confused with the far larger customer backstop. [10-K FY2025, Note 6, lines 2529–2585; Accounting reference]

## Historical margins and reinvestment on a consistent lag

| Fiscal year | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|---:|---:|
| Revenue | 27,450 | 33,203 | 35,819 | 51,574 | 63,887 |
| GAAP EBIT | 8,519 | 14,225 | 16,207 | 13,463 | 25,484 |
| GAAP operating margin | 31.03% | 42.84% | 45.25% | 26.10% | 39.89% |
| R&D | 4,854 | 4,919 | 5,253 | 9,310 | 10,977 |
| Acquired amortization | 5,403 | 4,359 | 3,247 | 9,267 | 8,062 |
| Cash capex | 443 | 424 | 452 | 548 | 623 |
| Depreciation | 539 | 529 | 502 | 593 | 574 |
| Change in noncash current operating capital, cash-flow proxy | (168) | 1,218 | 858 | 2,647 | 4,882 |
| Cash acquisition spending, net of cash acquired | 8 | 246 | 53 | 25,978 | 0 |
| Business disposal proceeds | 45 | 0 | 0 | 3,485 | 300 |
| Net physical/current investment before acquisitions | (264) | 1,113 | 808 | 2,602 | 4,931 |
| Cash investment proxy including acquisitions/disposals, before acquired amortization | (301) | 1,359 | 861 | 25,095 | 4,631 |
| GAAP net-reinvestment proxy, deduct acquired amortization | **(5,704)** | **(3,000)** | **(2,386)** | **15,828** | **(3,431)** |
| Next fiscal year's realized revenue increment | 5,753 | 2,616 | 15,755 | 12,313 | Not yet known |
| Lag1: next-year increment / GAAP net-reinvestment proxy | Not meaningful | Not meaningful | Not meaningful | 0.778x, cash-only acquisition caveat | Not observable |
| Lag1: next-year increment / pre-amortization cash investment proxy | Not meaningful | 1.925x | 18.298x, acquisition-distorted | 0.491x, cash-only acquisition caveat | Not observable |

Source rows: FY2021–FY2022 K23:1903,1911–1929,2007–2043; FY2023–FY2025 K25:1661–1687,1775–1811. The current-capital proxy is minus the sum of cash-flow changes in receivables, inventory, accounts payable, employee compensation, and other current assets/current liabilities, net of acquisitions/disposals. For FY2025 this is −[−2,717−510−118+300−1,837] =4,882; the reinvestment proxy is623−574+4,882+0−300−8,062 =−3,431. [10-K FY2023, Item 8; 10-K FY2025, Item 8]

These are explicitly **proxies**, not clean recurring marginal-return observations. The aggregated current-capital line mixes tax/interest and operating items; the excluded long-term asset/liability cash-flow changes contain contract assets, contract liabilities, taxes and other items that are not separated. Including the full long-term cash-flow use would add295,436,785,1,990 and3,618 respectively, giving alternative GAAP net-investment figures−5,409,−2,564,−1,601,17,818 and187. Neither mechanical aggregation identifies pure operating reinvestment; use the spread and classification limits visibly. [10-K FY2023, Item 8, lines 2021–2033; 10-K FY2025, Item 8, lines 1789–1801]

The table subtracts acquired-intangible amortization because reported EBIT also deducts it. It does not subtract the entire cash-flow line called amortization of intangible and ROU assets, which would additionally change the lease basis; operating leases have been left within operating expenses for this historical screen. R&D remains expensed and is not added again as investment. The before-acquired-amortization row is a useful physical/current-capital comparison but cannot be combined with retained-amortization EBIT and described as the same complete cash-flow model. [10-K FY2025, Item 8 and Note 6; Accounting reference]

**VMware prevents a cash-only historical ratio from representing full economic capital.** The FY2024 cash-flow acquisition line is25,978, but VMware alone cost79,648 net of acquired cash, including53,398 of stock issued,805 of assumed partially vested awards and23 of accelerated equity. Broadcom also assumed7,518 of debt (1,264 current+6,254 long-term), and acquired Seagate assets for600. Total consideration including stock is real investment regardless of payment form. [10-K FY2025, Note 4, lines 2189–2207,2243–2249,2345]

As an **illustrative disclosed-consideration correction**, replacing FY2024 cash acquisition spending25,978 with VMware net consideration79,648 + assumed debt7,518 + Seagate600 increases the GAAP proxy from15,828 to77,616; the one-year-lag revenue-increment ratio falls from0.778x to0.159x. This is not a fully normalized invested-capital rollforward: acquired leases, deferred taxes, fair-value purchase allocations, timing within FY2024, disposals and ongoing integration still differ from ordinary organic investment. The uncorrected18.298x FY2023 ratio similarly credits FY2024's acquired revenue to the prior year's tiny spending. These acquisition-distorted ratios must not be selected as the consolidated forecast ratio simply because they are available. [Calculation: preceding historical cash-flow and purchase-price sources]

A reliable forward choice therefore needs a normalized own-business/peer capital benchmark and a separate treatment of the emerging rack-financing model. With the acquired amortization switch off, explicit reinvestment overrides can legitimately reconcile net investment and amortization run-off if supported; a positive sales-to-capital ratio alone does not discover that schedule. FY2025 has no realized next-full-year revenue numerator at the cutoff and must not be presented as an observed lag1 ratio. [Model formulas and Engine lines 537–549; 10-Q Q2 FY2026, period information]

## Acquired-amortization roll-off and R&D screen

| Disclosed period for assets present at May3 | Acquired-amortization expense |
|---|---:|
| FY2026 remaining half-year | 3,940 |
| FY2027 | 6,818 |
| FY2028 | 5,689 |
| FY2029 | 4,562 |
| FY2030 | 3,378 |
| Thereafter | 3,196 |
| Total amortizable carrying value | 27,583 |

The schedule is for existing intangible assets, not a promise of no further acquisitions. Remaining weighted-average lives are5 years for purchased technology and6 for customer relationships; acquired VMware technology and customer relationships originally had8-year lives. Buildings/leasehold improvements generally depreciate over15–40 years (or shorter leases) and machinery/equipment over3–10 years. These figures inform a two-sided margin bridge: acquisition amortization falls while growth still requires research, physical equipment, working capital and possible new acquired assets. [10-Q Q2 FY2026, Note 4, lines 747–777; 10-K FY2025, Note 4, lines 2269–2285 and Note 2, line 1983]

For a rolling next12-month illustration only, assuming even within-year amortization, the next four model years would bear7,349;6,253.5;5,125.5;3,970 from the currently disclosed schedule. The first equals3,940 +0.5×6,818. The thereafter bucket has no annual allocation; do not fabricate the fifth rolling year from it. Equal half-year allocation is an analyst interpolation, not guidance. [Calculation: 10-Q Q2 FY2026, Note 4]

R&D is material:15.8895% of TTM sales, including stock compensation, and Broadcom describes sustained research as essential to competitive position. Retaining the GAAP expense basis is a permissible simplification only with a visible statement that research capital is absent from book invested capital and GAAP ROIC may overstate returns relative to a capitalized-R&D peer. No double expense should be introduced by also counting unchanged R&D as future reinvestment. [10-K FY2025, Item 1, lines 287–289 and Note 2, line 2063; Calculation: base above]

The current engine's R&D switch adjusts starting profit by current R&D minus historical amortization and adds the unamortized research asset to starting capital. It does **not** generate a future R&D/amortization schedule, additional reinvestment, or a tax-basis ledger. Nor may the annual FY2021–FY2025 R&D list be blindly appended to a May2026 TTM base: FY2025 and that TTM overlap six months rather than representing adjacent annual cohorts. Full capitalization would require matched periods, a defensible research life across both businesses and a future profit/capital/reinvestment/tax reconciliation. This note proposes retaining expense treatment pending that complete work; it does not claim R&D lacks multi-year benefits. [Engine, lines 263–307,537–549; Intangibles teaching, lines 271–314]

## Apollo event and commitments: accounting date and limits

The balance sheet is May3; the backstop agreement is June8 and is disclosed as a subsequent event in the June9 filing. The cached 10-Q does not disclose an initial recognized guarantee liability at June8, so absence from the earlier balance sheet cannot establish zero economic exposure at the valuation evidence cutoff. The filing says the backstop grows as racks are deployed and falls as the customer pays five-year lease obligations, with remedies including assumption of leases or sale of racks. [10-Q Q2 FY2026, Note 11 and Part II Item 5, lines 1253–1255,2213]

The platform release says the initial35,000 tranche supports Anthropic's previously announced more-than1GW expansion, with deployment beginning in mid2026; Apollo's financing release describes committed capital across a multi-year draw schedule. Neither35,000 of platform financing nor20GW of platform ambitions is Broadcom revenue, Broadcom debt, or an observed recovery value. The release's association with Anthropic clarifies the initial platform's purpose but the 10-Q itself does not name the customer whose lease Broadcom guarantees. The linkage is consistent; do not replace missing legal scope with inference. [Apollo platform release 2026-06-09; Apollo financing release 2026-06-09; 10-Q Q2 FY2026, Note 11]

Separate May3 unconditional purchase commitments total128,110, including55,214 in FY2027 and72,870 in FY2028, and are mainly for inventory. They should first inform revenue/cost/working-capital scenarios; mechanically subtracting all future inventory purchases as debt would double count purchases already reflected in operating profit and investment. Evidence does not reconcile these commitments to transferred Apollo agreements or establish the net residual Broadcom funding obligation after June8. No inference that Apollo removed all128,110 is supported. [10-Q Q2 FY2026, Note 10, lines 1209–1231 and Note 11]

## Remaining gaps and recommended handoff

| Issue | Status | Action for draft |
|---|---|---|
| Backstop economic value and relation to operating assumptions | Material, unsupported after targeted eligible-release search | Explicit null/required-check BLOCKED; leave operating evidence intact |
| May3 lease liabilities and current investment holdings | Not disclosed in eligible text/companyfacts extract | Explicit carry-forward or exclusion assumption with scale bound where defensible; no fabricated reported zero |
| Pension/current contingent-tax treatment | Last pension date stale; tax claim known but payment timing unknown | Explain separate-claim versus cash-tax choice and avoid double counting |
| Lagged marginal capital benchmark | Own-company record distorted by acquisitions, amortization and mixed working-capital lines | Use peer/normalized evidence prepared by runner; do not force arithmetic ratios into forecasts |
| Complete capitalization of R&D | Not prepared; switch does not supply full schedule/taxes | Retain expense basis with stated limitation, or separately complete reconciliation before enabling |

## Sources

- **K25 / [10-K FY2025]** — `10-K-FY2025.txt`, filed2025-12-18, fiscal year ended2025-11-02; line numbers in tables refer to this cached extracted text.
- **K23 / [10-K FY2023]** — `10-K-FY2023.txt`, filed2023-12-14, fiscal year ended2023-10-29; source of FY2021–FY2022 history.
- **Q26 / [10-Q Q2 FY2026]** — `10-Q-FY2026-Q2.txt`, filed2026-06-09, quarter ended2026-05-03; source line numbers refer to this cache.
- **[Apollo platform release 2026-06-09]** — `apollo-platform-release-2026-06-09.txt`, released2026-06-09; primary joint announcement, fetched by runner.
- **[Apollo financing release 2026-06-09]** — `apollo-financing-release-2026-06-09.txt`, released2026-06-09; primary Apollo financing announcement, fetched by runner.
- **[SEC bridge facts precutoff]** — `sec-bridge-facts-precutoff.txt`; runner-filtered companyfacts records with period ending2026-05-03 and filing date no later than2026-06-09; no current lease/investment stock amount found.
- **[Engine]** — repository `tools/valuation/engine.py`, inspected read-only; implementation, not external economic evidence.
- **[Accounting reference]** — `.claude/skills/draft-valuation/references/accounting-and-reinvestment.md`; companion `model-selection.md`; primary teaching `tools/valuation/damodaran-notes/sources/intangibles.txt` and `growth-and-value.txt`.
