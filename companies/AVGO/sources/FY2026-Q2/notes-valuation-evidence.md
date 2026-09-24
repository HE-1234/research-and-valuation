# AVGO valuation evidence and model assessment

_Analyst preparation by the runner, September 18, 2026. Operating evidence cutoff: June 9, 2026; Q2 FY2026 ended May 3. This is analysis, not a company disclosure. No valuation results have been computed._

## Scope and model choice

The research library contains a Q2 FY2026 report and no prior valuation or eligible frozen forecast. The initial target is `valuation/assumptions.yaml`; business.md and outlook.md remain unchanged. The report's indicators remain proposed. [AVGO research files]

Broadcom combines an outsourced chip business, a rapid AI product expansion and established infrastructure software. A consolidated free-cash-flow-to-the-firm forecast can describe the operating business if semiconductor and software demand, margins and capital needs are reconciled separately before aggregation. Financing is not its primary business, but the June 8 customer-lease backstop creates a separate equity claim whose treatment must be supported. [10-K FY2025, Items 1/7; 10-Q Q2 FY2026, Notes 9/11]

The current engine can subtract an independently supported present claim value through `bridge.other_claims`. It cannot itself estimate a contingent guarantee from a schedule of customer defaults, collateral recoveries and lease deployments, or give that bridge claim a different value by scenario. This does not rule out FCFF for AVGO; it limits what can be represented without an externally justified adjustment. [Engine schema/implementation; model-selection reference]

## Consensus coverage and management fallback for the September 24 redraft

No dated third-party analyst-consensus snapshot exists in the permitted pre-cutoff cache. The cached files contain company filings, releases, a machine transcript, peer filings, industry evidence and separately dated market inputs, but no provider mean with fiscal-period mapping, contributor count or GAAP operating-profit definition. Rule 10 therefore cannot seed revenue or EBIT from outside consensus; treating management's targets or this analyst's build as "consensus" would be false. [FY2026-Q2 cache inventory; valuation source manifests]

The candidate instead uses the documented fallback permitted by rule 10. It starts from reported TTM segment revenue, keeps the Q3 total-sales guide and fiscal-2026 AI floor distinct, maps management's named deployment schedule to the May-to-May model window, and labels every extension beyond those disclosures as analyst judgment. For margins, no outside EBIT series is available, so the candidate begins with the reported GAAP/segment reconciliation and tests mix, stock pay, acquisition amortization, research and physical depreciation explicitly. The implied central hypothesis is that disclosed AI programs recur across several generations while most infrastructure-software spending renews; scale helps first, then buyer bargaining, mix and continuing engineering costs normalize profitability. [10-Q Q2 FY2026; Q2 FY2026 release; Q2 FY2026 call; candidate base revenue and margin bridges]

This fallback covers the near-term operating hypothesis, not the missing long-term cash funding. The evidence still does not connect payment terms, contract assets, inventory and commitments, equipment replacement and recurring IP spending into a defensible years 6–10 total-investment path. Consequently all late ratios and overrides remain null. The investment-payoff test is therefore explicit: committed supply/customer arrangements and physical capex can support the early ramp, management could reduce discretionary expansion if demand disappoints but cannot freely exit binding commitments, and no cash-flow recovery is claimed for years 6–10 without the missing funding bridge. [10-Q Q2 FY2026, Notes 2/10/11; candidate sales-to-capital and reinvestment details]

Specific evidence requests to replace the fallback or unblock the model are: (1) a pre-June 9 consensus snapshot showing provider, publication date, contributor count, fiscal-year revenue and GAAP EBIT/operating profit means; (2) dated balances and payment/collection timing for inventory, contract assets, purchase commitments and customer advances tied to the AI ramp; (3) a supported recurring IP/research-capital and equipment-replacement schedule through years 6–10; (4) a dated carrying value or immateriality bound for corporate investments outside cash equivalents; and (5) fair-value, deployment, fee, default and recovery evidence for the June 8 customer-lease backstop. Without these, unsupported historical facts and material funding/claim inputs remain null. [Valuation base evidence; independent blocked review]

Archive/control note: the active `valuation/assumptions.yaml` archived for this redraft has SHA-256 `02ed91bdefb6256c38b600829a015ae2ccc686c646724412aeae1442bc77ea6a`; active `assumptions.md` has SHA-256 `6ce8263bfadbd6c0756b2e9f216943629b0a73c2153bfd6bc2696f916a8694b1`. The candidate is separate, and the active YAML contains no `owner_edited` or `changelog` block, so there is no owner changelog to reconcile at drafting time. [Archived redraft snapshot; active file inspection]

## Base facts and historical evidence

See `notes-valuation-base.md` for the full source arithmetic, line locators, capital history and unresolved disclosures. The source reconciliation is FY2025 plus first-half FY2026 minus first-half FY2025; year one is a forward twelve-month window from May 3, not fiscal FY2026. [10-K FY2025, consolidated statements; 10-Q Q2 FY2026, consolidated statements]

| TTM item, USD millions | Reconstructed amount |
|---|---:|
| Revenue | 75,465 |
| GAAP operating income | 32,746 |
| Acquired intangible amortization, memo | 8,014 |
| Stock compensation, memo | 8,785 |
| R&D, memo | 11,991 |
| Tax provision / pre-tax earnings | 1,162 / 30,479 |

The reported effective tax rate of about 3.8% includes tax benefits and cannot serve as an unexamined recurring tax assumption. The analyst must distinguish reported figures, the company's non-GAAP guidance and normalized taxes. [10-K FY2025, tax note; 10-Q Q2 FY2026, tax note; Q2 FY2026 call]

## Accounting decisions for the numerical analyst

| Item | Treatment to assess | Cell / implication |
|---|---|---|
| SBC | Keep recurring compensation expensed; do not add back as free cash. Latest-quarter diluted shares include only the disclosed dilution methodology, not every future grant. | GAAP margin; share bridge and dilution note. |
| Acquired amortization | Retain expense by default; show the disclosed runoff and continuing asset replacement in the margin/capital bridge. Cash acquisitions alone omit stock-funded purchase consideration. | Switch false; forecast margin bridge; reinvestment detail. |
| R&D | Retain reported expensing as a documented comparable basis. The mixed software/chip useful life is not independently established; switching only the base-year profit would be an incomplete adjustment. Reported capital therefore excludes internally created research assets and ROIC is not a pure economic return. | Switch false; all peer comparisons same basis. |
| Operating leases | May 3 lease stock not separately disclosed in the extracted filing or eligible SEC companyfacts. A prior-year carryforward must be labelled an estimate, never a May 3 reported number; expense/capital adjustment must be paired or left unresolved. | Bridge and invested capital. |
| Investments | Cash-flow purchases/sales cannot establish a carrying balance. No inference that pension plan assets are corporate investments. | Nonoperating asset bridge. |
| Apollo backstop | Maximum contractual exposure is not fair value. No supported value, fee, deployment schedule or default/recovery model found in eligible evidence. Leave the dependent claim unsupported unless the analyst can defend a complete bounded treatment. | `other_claims`; potential required-check BLOCKED. |

These treatments apply the accounting-and-reinvestment guide and Damodaran's *Valuing Companies with Intangible Assets*, sections on capitalizing R&D and equity claims. The retained GAAP basis is a disclosed simplification, not a claim that research creates no asset. [Accounting reference; Intangibles method]

## Mature benchmarks

See `notes-valuation-peers.md` for the named-company benchmark table and direct filing locators. Qualcomm illuminates fabless chip economics; Cisco adds a less exceptional mature hardware/software outcome; Microsoft's Productivity and Business Processes segment illuminates software scale, with consolidated ROIC and cloud-capital differences separately identified. These are comparators, not automatic targets. Broadcom's own pre- and post-VMware history is necessary because none duplicates its mix. [Peer evidence note]

| FY2025 comparator | Revenue, USD millions | GAAP operating margin | Ending sales/book capital | Operating return at common 21% tax assumption |
|---|---:|---:|---:|---:|
| Qualcomm consolidated | 44,284 | 27.90% | 1.712 | 35.35% |
| Cisco consolidated | 56,654 | 20.76% | 0.963 | 15.86% |
| Microsoft PBP | 120,810 | 57.75% | Segment capital undisclosed | Segment capital undisclosed |
| Microsoft consolidated, distinct from PBP | 281,724 | 45.62% | 0.833 | 37.37% |
| Broadcom consolidated | 63,887 | 39.89% | 0.490 | 15.99% |

All margins and returns above are calculations from eligible primary filings. Returns retain goodwill and expense R&D/SBC; their denominators exclude operating leases on the same retained-rent basis, include finance leases, and subtract cash plus current securities. The common tax rate is a comparison convention only; these are opening-book-capital returns, not observed marginal investment returns. The full peer note shows reported taxes, multi-year observations, amortization sensitivities, reinvestment components and remaining comparability limits. [Peer evidence note]

Use GAAP versus adjusted profit consistently, retain goodwill, and do not treat a segment margin that excludes stock compensation as a consolidated margin. Stock sales/capital, marginal reinvestment and historical average ROIC answer different questions. Prior acquisitions contaminate short-period incremental ratios; no meaningful positive efficiency estimate may be manufactured from a negative net-investment denominator. [Peer evidence note; Base evidence note; Business-drivers reference]

## Demand bounds and their limits

WSTS's June 2 forecast estimates 2027 logic sales of USD 522,820 million and total semiconductor sales of USD 1,913,683 million. These cover competitors and products Broadcom does not sell; the large memory category must not be used as its addressable market. Logic plus relevant adjacent categories can supply a broad ceiling with an explicit extrapolation, but a forecast still needs a plausible share and a separate software demand check. [WSTS spring 2026, pp.1–2]

The June 9 platform releases describe more than 20 GW through 2028, with USD 35 billion of initial financing for more than 1 GW. Financing is not Broadcom revenue and does not disclose its chip content per GW. Do not multiply platform financing by total gigawatts or treat it as incremental backlog on top of already reported contracts. [Apollo platform release June 9; Apollo financing release June 9]

The cached call contains multi-year AI revenue wording and customer deployment plans; use it for exact wording with the existing machine-transcript limitation. The current release and filings supply reported numbers. Existing customer commitments support near-term conversion; no finite contract proves durable excess returns after ten years. [Q2 FY2026 call; Q2 FY2026 release; 10-Q Q2 FY2026, Note 2]

## Uncertainty and price independence

| Uncertainty | Model location | Avoid double counting |
|---|---|---|
| AI deployment and customer in-house design | Semiconductor revenue paths and price/margin mix | Do not add a separate arbitrary discount-rate surcharge for the same expected shortfall. |
| Inventory and binding supply commitments | Working-capital needs and operating downside | Commitments are future purchases, not all current debt; ensure unsold inventory risk is included once. |
| Software renewals and pricing | Software growth and mature margin | Avoid assuming both unchanged retention and unlimited price increases. |
| Customer lease default | Separately supported contingent claim, if available | Distinguish customer failure from failure of Broadcom; don't use the firm's failure multiplier as a substitute. |
| Capital-market systematic risk | Shared cost-of-capital build | Current price enters financing weights only; it does not set operating assumptions. |

Use house 25/50/25 weights explicitly as assumptions. No scenario is a statistical confidence interval. Damodaran's uncertainty discussion supports making transparent future judgments; it does not supply an undisclosed historical liability value. [Uncertainty method, Dealing with Uncertainty points 2–6]

## Market inputs

The runner fetched AVGO's price directly without computing a valuation and separately retrieved FRED DGS10; exact observations and dates are in `valuation-market-inputs.txt`. The industry cache predates the operating cutoff; current market price, rate and ERP are allowed separately dated inputs under §18.8. The analyst leaves price-derived debt/equity and industry beta cells for the runner. [Market inputs; Damodaran dataset manifest]

## Unresolved evidence and completion status

The June 8 backstop is disclosed before the operating cutoff but after the latest balance-sheet date. The June 9 Apollo releases add platform context without establishing a valuation adjustment. The source gap stops a completed equity valuation if no defensible independent claim estimate or bounded treatment can be established; unaffected operating assumptions and research should still be saved and reviewed. [10-Q Q2 FY2026, Note 11; Apollo releases June 9]

The latest lease and investment stock disclosures are also unresolved; distinguish material requirements from explicit immaterial carryforward assumptions. All such choices require reviewer assessment. A successful validator command alone does not close an evidence gap. [Base evidence note; AGENTS.md §13/§18]

No eligible prior forecast exists. After PASS only, freeze exact inputs and operating forecasts with actual creation time, cutoff, source hash, model windows, non-price inputs and accounting definitions. A blocked candidate receives no passing forecast or completion commit. [Forecast-learning reference]

## Sources

- [AVGO research files]: `../../business.md`, `../../outlook.md`; local artifact metadata only.
- [10-K FY2025]: `10-K-FY2025.txt`; origin and filing date in MANIFEST.md.
- [10-Q Q2 FY2026]: `10-Q-FY2026-Q2.txt`; origin and filing date in MANIFEST.md.
- [Q2 FY2026 release]: `press-release.txt`.
- [Q2 FY2026 call]: `transcript.txt`; third-party machine transcript; wording-only limitation as recorded in MANIFEST.md.
- [WSTS spring 2026]: `wsts-spring-2026.txt`; published June 2, 2026; origin in MANIFEST-valuation-runner.md.
- [Apollo platform release June 9]: `apollo-platform-release-2026-06-09.txt`.
- [Apollo financing release June 9]: `apollo-financing-release-2026-06-09.txt`.
- [Base evidence note]: `notes-valuation-base.md`; original filing locators therein.
- [Peer evidence note]: `notes-valuation-peers.md`; exact reused/fetched source paths therein.
- [Market inputs]: `valuation-market-inputs.txt`.
- [Damodaran dataset manifest]: `../../../../tools/valuation/data/damodaran/MANIFEST.md`.
- [Engine schema/implementation]: `../../../../tools/valuation/schema.py`, `../../../../tools/valuation/engine.py`.
- [model-selection reference], [Accounting reference], [Business-drivers reference], [Forecast-learning reference]: `../../../../.claude/skills/draft-valuation/references/` corresponding named guides.
- [Intangibles method]: `../../../../tools/valuation/damodaran-notes/sources/intangibles.txt`, PDF pp.8–12 and equity-options section.
- [Uncertainty method]: `../../../../tools/valuation/damodaran-notes/sources/uncertainty.txt`, Dealing with Uncertainty, points 2–6.

## Targeted drafting follow-ups

NVIDIA's February 25 release gives FY2026 revenue of about USD 215.9 billion; its May 20 release gives current-quarter revenue of USD 81.615 billion, of which about USD 75.2 billion is Data Center. These are a pre-cutoff scale check for a leading AI supplier, not mature economics, Broadcom's addressable market, or proof that Broadcom can capture the same demand. Systems/chip/software scope differs, and annualizing a current quarter is a run-rate calculation rather than a reported full-year result. [NVIDIA FY2026 release; NVIDIA Q1 FY2027 release]

The January 2036 Broadcom note has a 4.95% coupon and the January 6/13 ten-year Treasury rate was 4.18%. Carrying the 0.77-point difference to the current 4.94% Treasury gives a 5.71% borrowing-cost proxy, rounded by the analyst to 5.7%. This assumes an unchanged spread; coupon, issue yield and current traded yield are distinct, and the assumption needs review if credit conditions change. [January 2026 debt issue; FRED debt proxy]

Additional source mapping: [NVIDIA FY2026 release] = `NVDA-release-FY2026-Q4.txt`; [NVIDIA Q1 FY2027 release] = `NVDA-release-FY2027-Q1.txt`; [January 2026 debt issue] = `8-K-2026-01-13-notes-offering.txt`; [FRED debt proxy] = `fred-treasury-debt-proxy.txt`. Original URLs, dates and extraction methods are in `MANIFEST-valuation-runner.md`.

## Disposition after the first independent review and analyst revision

The two balance-sheet/claim gaps remain unresolved. The first operating review also rejected the late-period funding bridge: broadly steady growth, margins and taxes produced a more-than-threefold increase in required net investment on entering the terminal period in the central cases. The researched historical/peer capital definitions did not justify the timing of that change; missing research capital explained part of the high book-return measure but did not explain the cash-funding discontinuity. [Independent valuation draft review, pass 1]

The analyst retained the reviewable first five years and the independent mature-return hypotheses, but changed all four `sales_to_capital.value_late` inputs and years 6–10 reinvestment overrides to null. This is an unsupported long-term modeling choice, distinct from an undisclosed historical fact or a claim that future estimates require certainty. A supported resolution needs a coherent account of how growth is funded as buyer power, supplier commitments and the financing model evolve, using consistent profit/capital definitions; an arbitrary acquisition budget or a return selected to clear a warning is insufficient. [Revised assumptions, September 18, 2026; Independent valuation draft review]

Both validation and an unmodified restricted diagnostic run correctly stop every case. Initial conditional operating diagnostics are retained only with the rejected first-pass snapshot. No completed equity value, passing forecast snapshot or completed-draft commit has been produced. [Validation and diagnostic logs]

Additional artifact mapping: [Independent valuation draft review] = `../../review/FY2026-Q2-valuation-draft-review.md`; [Revised assumptions] = `../../valuation/assumptions.yaml`; [Validation and diagnostic logs] = `../../review/FY2026-Q2-valuation-validation.txt` and `../../review/FY2026-Q2-diagnostics-current.txt`.
