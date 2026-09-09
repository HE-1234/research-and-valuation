# Sandisk Corporation (SNDK) — IR gatherer notes, Q4 FY2026 (quarter ended July 3, 2026)

- Company: Sandisk Corporation (Nasdaq: SNDK), CIK 2023554. Spun off from Western Digital on February 21, 2025.
- Quarter: Q4 FY2026, quarter ended July 3, 2026 (13 weeks). FY2026 was a 53-week year ended July 3, 2026. Company shorthand in its own tables: "Q4 2026", "Q4'26", "FQ4'26", "Q4'FY26". Prior quarter Q3 FY2026 ended April 3, 2026. Year-ago quarter Q4 FY2025 ended June 27, 2025.
- Results released: 2026-08-05 (call 1:30 p.m. Pacific). FY2026 10-K filed 2026-08-17. As-of cutoff: 2026-08-17. Nothing published after 2026-08-17 was fetched or read. The 2026 Investor Day (August 13, 2026) falls inside the window and is covered in §11.
- Fetch date: 2026-09-08/09 (UTC timestamps in MANIFEST-ir.md).
- Files and tags (all in `companies/SNDK/sources/FY2026-Q4/`):
  - `press-release.txt` → `[Q4 FY2026 release]` (8-K exhibit 99.1, accession 0001628280-26-053346, filed 2026-08-05; reused from cache after verification). Line numbers below ("l.N") refer to this file.
  - `slides.txt` → `[Q4 FY2026 slides, p.N]` ("SNDK Q4-26 Earnings Deck.pdf", 25 PDF pages; N = Nth form-feed page = PDF page = the deck's printed footer "00.0N"; p.25 is a blank back cover).
  - `press-release-FY2026-Q3.txt` → `[Q3 FY2026 release]` (8-K exhibit 99.1, accession 0001628280-26-028879, filed 2026-04-30).
  - `slides-FY2026-Q3.txt` → `[Q3 FY2026 slides, p.N]` ("SNDK Q3-26 Earnings Deck Final.pdf", 18 PDF pages; printed footer "00.0N" = PDF page N; p.11 is blank).
  - `press-release-FY2025-Q4.txt` → `[Q4 FY2025 release]` (8-K exhibit 99.1, accession 0001193125-25-180782, filed 2025-08-14; DFIN-filed).
  - `investor-day-2026-slides.txt` → `[2026 Investor Day slides, p.N]` ("SNDK_Investor_Day_2026_Presentation.pdf", 98 PDF pages, August 13, 2026; N = PDF page; the deck has no printed page numbers).
  - `press-release-investor-day-2026.txt` → `[2026 Investor Day release]` (Business Wire release of August 13, 2026 as posted on investor.sandisk.com; no 8-K was filed for it).
- End-market names: the FY2026 releases use Datacenter / Edge / Consumer. The Q4 FY2025 release used Cloud / Client / Consumer for the same three lines; its Q4 2025 figures (Cloud $213, Client $1,103, Consumer $585) are identical to the "Datacenter / Edge / Consumer" Q4 2025 column in the Q4 FY2026 release, so the renaming is a relabel, not a recast (gatherer observation; no release states this).
- All dollar figures are in millions unless marked "billion", exactly as the source prints them. **Numbers verbatim; gatherer arithmetic is labelled "gatherer arithmetic".** Nothing here is interpretation.

---

## 1. Headline income statement (GAAP and non-GAAP)

Q/Q highlights table as printed [Q4 FY2026 release, "Q4 2026 Financial Highlights", l.30–37]:

| ($ in millions, except per share) | GAAP Q4 2026 | GAAP Q3 2026 | Q/Q | Non-GAAP Q4 2026 | Non-GAAP Q3 2026 | Q/Q |
|---|---|---|---|---|---|---|
| Revenue | $8,965 | $5,950 | up 51% | $8,965 | $5,950 | up 51% |
| Gross Margin | 84.6% | 78.4% | up 6.2 ppt | 84.6% | 78.4% | up 6.2 ppt |
| Operating Expenses | $545 | $551 | down 1% | $484 | $448 | up 8% |
| Operating Income | $7,037 | $4,111 | up 71% | $7,104 | $4,218 | up 68% |
| Net Income | $6,903 | $3,615 | up 91% | $6,162 | $3,675 | up 68% |
| Diluted Net Income Per Share | $43.97 | $23.03 | up 91% | $39.25 | $23.41 | up 68% |

Y/Y highlights table as printed [Q4 FY2026 release, l.39–46]:

| ($ in millions, except per share) | GAAP Q4 2026 | GAAP Q4 2025 | Y/Y | Non-GAAP Q4 2026 | Non-GAAP Q4 2025 | Y/Y |
|---|---|---|---|---|---|---|
| Revenue | $8,965 | $1,901 | up 372% | $8,965 | $1,901 | up 372% |
| Gross Margin | 84.6% | 26.2% | up 58.4 ppt | 84.6% | 26.4% | up 58.2 ppt |
| Operating Expenses | $545 | $480 | up 14% | $484 | $402 | up 20% |
| Operating Income | $7,037 | $18 | * | $7,104 | $100 | * |
| Net Income (Loss) | $6,903 | $(23) | * | $6,162 | $42 | * |
| Diluted Net Income (Loss) Per Share | $43.97 | $(0.16) | * | $39.25 | $0.29 | * |

"* Not a meaningful figure" [l.48].

Fiscal year table as printed [Q4 FY2026 release, "Fiscal Year 2026 Financial Highlights", l.52–59]:

| ($ in millions, except per share) | GAAP 2026 | GAAP 2025 | Y/Y | Non-GAAP 2026 | Non-GAAP 2025 | Y/Y |
|---|---|---|---|---|---|---|
| Revenue | $20,248 | $7,355 | up 175% | $20,248 | $7,355 | up 175% |
| Gross Margin | 71.5% | 30.1% | up 41.4 ppt | 71.6% | 30.3% | up 41.3 ppt |
| Operating Expenses | $2,083 | $3,589 | down 42% | $1,791 | $1,539 | up 16% |
| Operating Income (Loss) | $12,389 | $(1,377) | * | $12,700 | $689 | * |
| Net Income (Loss) | $11,433 | $(1,641) | up 797% | $10,987 | $440 | * |
| Diluted Net Income (Loss) Per Share | $73.76 | $(11.32) | up 752% | $70.88 | $2.99 | * |

Consolidated statement of operations (GAAP) [Q4 FY2026 release, "Consolidated Statements of Operations", l.178–211]:

| (in millions, except per share) | Q4 (Jul 3, 2026) | Q4 (Jun 27, 2025) | FY (Jul 3, 2026) | FY (Jun 27, 2025) |
|---|---|---|---|---|
| Revenue, net | $8,965 | $1,901 | $20,248 | $7,355 |
| Cost of revenue | 1,383 | 1,403 | 5,776 | 5,143 |
| Gross profit | 7,582 | 498 | 14,472 | 2,212 |
| Research and development | 348 | 285 | 1,328 | 1,132 |
| Selling, general and administrative | 197 | 162 | 676 | 573 |
| Goodwill impairment | — | — | — | 1,830 |
| Loss on debt extinguishment | — | — | 46 | — |
| Business separation costs | — | 17 | 25 | 67 |
| Employee termination and other | — | 16 | (2) | 21 |
| (Gain) loss on business divestiture | — | — | 10 | (34) |
| Total operating expenses | 545 | 480 | 2,083 | 3,589 |
| Operating income (loss) | 7,037 | 18 | 12,389 | (1,377) |
| Gain (loss) on equity securities, net | 804 | (1) | 808 | (2) |
| Interest income | 30 | 11 | 70 | 22 |
| Interest expense | (2) | (41) | (73) | (63) |
| Other income (expense), net | (20) | (5) | (177) | (59) |
| Total interest and other income (expense), net | 812 | (36) | 628 | (102) |
| Income (loss) before taxes | 7,849 | (18) | 13,017 | (1,479) |
| Income tax expense | 946 | 5 | 1,584 | 162 |
| Net income (loss) | $6,903 | $(23) | $11,433 | $(1,641) |
| EPS basic | $46.96 | $(0.16) | $77.78 | $(11.32) |
| EPS diluted | $43.97 | $(0.16) | $73.76 | $(11.32) |
| Weighted average shares, basic (millions) | 147 | 145 | 147 | 145 |
| Weighted average shares, diluted (millions) | 157 | 145 | 155 | 145 |

- Non-GAAP interest and other income (expense), net: $8 (Q4'26), $(3) (Q3'26), $(37) (Q4'25), $(69) (FY26), $(109) (FY25) [Q4 FY2026 release, reconciliation, l.316].
- Non-GAAP income tax expense: $950 (Q4'26), $540 (Q3'26), $21 (Q4'25), $1,644 (FY26), $140 (FY25) [l.319].
- Non-GAAP diluted shares: 157 (Q4'26), 157 (Q3'26), 147 (Q4'25), 155 (FY26), 147 (FY25) [l.347].
- Depreciation and amortization: 37 (Q4'26), 36 (Q4'25), 149 (FY26), 163 (FY25) [l.226]. Stock-based compensation (cash-flow statement): 67, 49, 232, 182 [l.227].
- Non-GAAP results as the deck prints them, five-quarter view [Q4 FY2026 slides, p.13]: Revenue $1,901 / $5,950 / $8,965 (Q4'25 / Q3'26 / Q4'26); Gross Margin % 26.4% / 78.4% / 84.6%; Operating Expenses $402 / $448 / $484; Operating Income $100 / $4,218 / $7,104; Interest and Other Income (Expense), net $(37) / $(3) / $8 ("up 367%" Q/Q, "up 122%" Y/Y); Diluted Net Income per Share $0.29 / $23.41 / $39.25; Operating Cash Flow $94 / $3,038 / $7,126 ("up 135%" Q/Q); Adjusted Free Cash Flow $77 / $2,417 / $5,035 ("up 108%" Q/Q).
- Quarterly revenue and non-GAAP gross profit for the last six quarters [2026 Investor Day slides, p.72; Q3 FY2026 slides, p.13]: Q3'25 revenue 1,695 (non-GAAP GP $385); Q4'25 1,901 ($502, 26.4%); Q1'26 2,308 ($691, 29.9%); Q2'26 3,025 ($1,546, 51.1%); Q3'26 5,950 ($4,666, 78.4%); Q4'26 8,965 ($7,588, 84.6%); FY'26 20,248 ($14,491, 71.6%).
- Quarterly non-GAAP operating income [2026 Investor Day slides, p.73]: Q4'25 $100; Q1'26 $245; Q2'26 $1,133; Q3'26 $4,218; Q4'26 $7,104; FY'26 $12,700 (FY'25 $689). GAAP operating income Q1'26 $176.
- Quarterly non-GAAP net income and EPS [2026 Investor Day slides, p.74]: Q1'26 $181 / $1.22 (GAAP $112 / $0.75; 149 million diluted shares); Q2'26 $969 / $6.21 (GAAP $803 / $5.15; 156 million); Q3'26 $3,675 / $23.41; Q4'26 $6,162 / $39.25; FY'26 $10,987 / $70.88.
- **Restatement flag (gatherer observation):** the Q3 FY2026 release printed Q2'26 non-GAAP net income as $967 and non-GAAP EPS as $6.20 [Q3 FY2026 release, l.313, l.316], with "Other, net" 94 and no equity-securities line; the Investor Day deck prints Q2'26 as $969 / $6.21 with "(Gain) loss on equity securities, net (4)" and "Other, net 100" [2026 Investor Day slides, p.74]. Neither document explains the change.
- Gatherer arithmetic: GAAP effective tax rate Q4'26 = 946 / 7,849 = 12.1%; FY26 = 1,584 / 13,017 = 12.2%. Non-GAAP pre-tax income Q4'26 = 7,104 + 8 = 7,112; non-GAAP tax rate = 950 / 7,112 = 13.4% (FY26: 1,644 / 12,631 = 13.0%; Q3'26: 540 / 4,215 = 12.8%). Non-GAAP net income check: 7,112 − 950 = 6,162, matches. GAAP EPS exceeds non-GAAP EPS in Q4'26 and FY26 because the $804 gain on equity securities is excluded from non-GAAP.
- Gatherer arithmetic: annualised Q4'26 revenue = 8,965 × 4 = 35,860; the Investor Day deck rounds this to "$36B" [2026 Investor Day slides, p.58].

"Record" and headline claims, verbatim:
- Title: "Sandisk Reports Fiscal Fourth Quarter 2026 Financial Results" [Q4 FY2026 release, l.8].
- "Fiscal fourth quarter revenue was $8.97 billion, up 51% sequentially, with GAAP net income reported at $6.90 billion ($43.97 diluted net income per share). Sequential revenue growth came approximately one-third from higher volumes and two-thirds from higher pricing. Fourth quarter Non-GAAP diluted net income per share was $39.25." [Q4 FY2026 release, l.12]
- "Fiscal year 2026 revenue was $20.25 billion, up 175% year-over-year, with GAAP net income reported at $11.43 billion ($73.76 diluted net income per share). Revenue outperformance was driven by both our mix shift toward higher-value customers, with Datacenter up 437%, and higher pricing. Fiscal year 2026 Non-GAAP diluted net income per share was $70.88." [l.14]
- "Since announcing five New Business Model ("NBM") agreements during our April earnings call, we have signed five additional agreements, including three NBMs with new customers and two deals expanding on previously signed NBMs." [l.16]
- "Expanded our share repurchase authorization, with Sandisk's Board of Directors approving an additional $14 billion buyback program, bringing total remaining authorization to $15.5 billion." [l.18]
- "Expect first quarter 2027 revenue to be in the range of $10.30 billion to $10.80 billion, with expected Non-GAAP diluted net income per share to be in the range of $44.00 to $46.00." [l.20]
- CEO statement in full: "We closed fiscal 2026 with a leading technology portfolio, established datacenter as a key growth pillar, and deepened our customer partnerships," said David Goeckeler, Chairman and Chief Executive Officer of Sandisk. "Our technology and products are well positioned to create value for our customers and generate growing and durable free cash flow." [Q4 FY2026 release, l.24]
- "Q4 was a proof point: record revenue, gross margin, and EPS, each above the high end of guidance, with $4.5 billion of stock repurchased" [Q4 FY2026 slides, p.3].
- "Fiscal 2026 marks a fundamental inflection point for Sandisk, capping a year in which we reshaped the business toward the highest-value end markets, with Datacenter established as a major pillar of growth" [Q4 FY2026 slides, p.3].
- "Together, these actions are driving structurally higher and more durable earnings power" [Q4 FY2026 slides, p.3].
- Deck headline tiles: "~$9.0B Revenue, +51% QoQ, +372% YoY"; "$39.25 Non-GAAP Diluted Net Income per Share"; "84.6% Non-GAAP Gross Margin"; "$5.0B Adjusted Free Cash Flow"; footnote 2: "Excludes $1,938 million related to NBM prepayments and deposits." [Q4 FY2026 slides, p.6]
- The release itself contains no "record" wording; "record" appears only in the deck (p.3).

## 2. Revenue by end market

Quarterly [Q4 FY2026 release, "End Market Summary", l.65–69]:

| Revenue ($ in millions) | Q4 2026 | Q3 2026 | Q/Q | Q4 2025 | Y/Y |
|---|---|---|---|---|---|
| Datacenter | $2,977 | $1,467 | up 103% | $213 | * |
| Edge | $5,432 | $3,663 | up 48% | $1,103 | up 392% |
| Consumer | $556 | $820 | down 32% | $585 | down 5% |
| Total Revenue | $8,965 | $5,950 | up 51% | $1,901 | up 372% |

Annual [Q4 FY2026 release, l.73–77]:

| Revenue ($ in millions) | 2026 | 2025 | Y/Y |
|---|---|---|---|
| Datacenter | $5,153 | $960 | up 437% |
| Edge | $12,160 | $4,127 | up 195% |
| Consumer | $2,935 | $2,268 | up 29% |
| Total Revenue | $20,248 | $7,355 | up 175% |

- The deck gives the Datacenter Y/Y the release marks "*": "Datacenter Revenue $2,977 million, Increased 103% QoQ, Increased 1,298% YoY"; "Edge Revenue $5,432 million, Increased 48% QoQ, Increased 392% YoY"; "Consumer Revenue $556 million, Decreased 32% QoQ, Decreased 5% YoY" [Q4 FY2026 slides, p.7]. Gatherer arithmetic: 2,977 / 213 = 13.98×, consistent with +1,298%.
- The p.7 chart plots five quarters of stacked end-market revenue (FQ4'25 to FQ4'26) with a non-GAAP gross margin line labelled 26%, 30%, 51%, 78%, 85%; the bars carry no value labels in the text layer (checked with `pdftotext -bbox`), so quarterly end-market values must come from the releases [Q4 FY2026 slides, p.7].

Longer end-market history assembled from the releases (each column verbatim from the release named):

| Revenue (in millions) | Q4 FY24 | Q3 FY25 | Q4 FY25 | Q2 FY26 | Q3 FY26 | Q4 FY26 | FY24 | FY25 | FY26 |
|---|---|---|---|---|---|---|---|---|---|
| Datacenter (was "Cloud") | $170 | $197 | $213 | $440 | $1,467 | $2,977 | $325 | $960 | $5,153 |
| Edge (was "Client") | 1,067 | 927 | 1,103 | 1,678 | 3,663 | 5,432 | 4,069 | 4,127 | 12,160 |
| Consumer | 523 | 571 | 585 | 907 | 820 | 556 | 2,269 | 2,268 | 2,935 |
| Total | $1,760 | $1,695 | $1,901 | $3,025 | $5,950 | $8,965 | $6,663 | $7,355 | $20,248 |
| Source | [Q4 FY2025 release] | [Q3 FY2026 release] | [Q4 FY2026 release] | [Q3 FY2026 release] | [Q4 FY2026 release] | [Q4 FY2026 release] | [Q4 FY2025 release] | [Q4 FY2026 release] | [Q4 FY2026 release] |

- Q1 FY26 by end market is not printed in any cached IR document. Gatherer arithmetic (FY26 minus the three printed quarters): Datacenter 5,153 − 440 − 1,467 − 2,977 = 269; Edge 12,160 − 1,678 − 3,663 − 5,432 = 1,387; Consumer 2,935 − 907 − 820 − 556 = 652; sum 2,308, which equals the Q1'26 revenue printed in [2026 Investor Day slides, p.72]. Not a company figure.
- Gatherer arithmetic, share of revenue: Q4'26 Datacenter 33.2%, Edge 60.6%, Consumer 6.2%; FY26 Datacenter 25.4%, Edge 60.1%, Consumer 14.5%; FY25 Datacenter 13.1%, Edge 56.1%, Consumer 30.8%.
- Bits, volume and pricing, verbatim:
  - "Sequential revenue growth came approximately one-third from higher volumes and two-thirds from higher pricing" [Q4 FY2026 release, l.12; repeated Q4 FY2026 slides, p.6].
  - "Datacenter has grown from 12% of our bits in Q4'FY25 to 38% in Q4'FY26, reflecting the strength of our technology position" [Q4 FY2026 slides, p.8].
  - "Demand from our customers is growing faster than our supply, and we expect bits to remain on allocation beyond calendar 2027" [Q4 FY2026 slides, p.12].
  - "Higher inventory levels reduce sellable bit growth to mid-teens for the full year" [Q4 FY2026 slides, p.16]. The slide does not name the fiscal year (context is the FY2027 outlook page).
  - Exabytes shipped, ASP per gigabyte in dollars, and bit-growth percentages by quarter: not disclosed in the release or deck.
- End-market commentary, verbatim [Q4 FY2026 slides]:
  - Datacenter (p.8): "We scaled compute-focused TLC enterprise SSDs across a broad set of hyperscale and AI infrastructure customers"; "Datacenter is our fastest-growing end market and a central pillar of our long-term growth"; "We expect Datacenter's share of the total TAM to expand from ~30% in CY25 to ~50% in CY26, and to continue outpacing the market in CY27" (source line: "Sandisk Internal Market Model").
  - Edge (p.9): "Edge remains a large and strategically important end market, spanning smartphones, PCs, tablets, and emerging physical AI use cases including automotive, robotics, and on-device agentic AI"; "Near term, PCs and smartphones are working through a period of adjustment as demand shifts toward AI-enabled devices and premium configurations, driving higher storage content"; "In the PC market, OEMs are growing revenue and expanding margin on a more profitable mix reflecting demand for higher-end devices"; "We expect these markets to return to growth in calendar year 2027"; "Longer term, on-device AI and richer content will continue to expand the role of high-performance flash at the Edge".
  - Consumer (p.10): "Sandisk's global consumer presence remains a meaningful differentiator within the industry, giving us a unique connection with end users and channel partners"; "Consumer anchors a balanced portfolio across Datacenter, Edge, and Consumer, adding diversification, margin opportunity, channel reach, and mix flexibility". No reason is given for the 32% sequential decline.
- Technology and product, verbatim [Q4 FY2026 slides, p.5]: "BiCS is recognized as an industry gold standard for NAND, and this year we ramped BiCS 8 to the majority of our bit production"; "BiCS 8 was enabled by innovations like CBA and hybrid wafer bonding"; "This quarter we began shipping our QLC Stargate platform for revenue"; "Portfolio spans performance-intensive compute workloads and high-capacity AI data lakes".
- Market outlook, verbatim [Q4 FY2026 slides, p.12]: "We expect the NAND market to continue growing at an accelerated pace, supported by AI inference as a key tailwind"; "We estimate the NAND market will exceed $300 billion in revenue in calendar year 2026, up 3x year-over-year"; "We expect NAND market revenue of $500 billion in calendar year 2027". Source line: "TechInsights NAND Market Report Q2 2026".
- "The Era of Inference" page, verbatim [Q4 FY2026 slides, p.4]: "AI is fundamentally a memory-centric, storage-intensive problem, and it is reshaping the demand equation for NAND"; "Every AI interaction creates content that must be stored, retrieved, and served at low latency, relying on data storage products including our high-capacity enterprise SSDs"; "NAND is the most scalable semiconductor technology in the world and has become a critical component of AI architecture"; "Our NBMs give customers confidence in long-term supply and give us clearer demand visibility and more durable cash flow".

## 3. New Business Model (NBM) agreements — KPIs not in the 10-K

Deck KPI tiles, verbatim [Q4 FY2026 slides, p.11]:
- "8 Customers signed across Datacenter and Edge"
- "$93.9B Minimum contracted NBM revenue at floor pricing"
- "$59.8B RPO at quarter-end; $91.1B incl. deals signed after quarter-end"
- "$16.5B Financial guarantees: cash deposits and instruments"
- "1/2 of bits committed under NBMs in FY2027"; "~2/3 of bits committed under NBMs in FY2028"; "4+ yrs weighted average duration, up to 5 years"
- Bullets: "Signed five more agreements: three new customers, two expansions; three closed pre-quarter-end and two after quarter-end"; "Pricing blends fixed and variable elements, with the variable portion subject to floors and ceilings — attractive margins even at floor pricing"; "Supply and demand commitments are defined by year and by quarter, giving clearer operational visibility and added financial protection"; "Guarantees release toward the end of each agreement, so coverage relative to remaining obligations rises over time"; "Highly selective on new NBMs: strategic customers, ~five-year duration, growing volumes, and attractive financials".
- Sequence of NBM announcements: "Ended the fiscal third quarter with three signed New Business Model ("NBM") agreements. Signed two additional NBM agreements in the fiscal fourth quarter." [Q3 FY2026 release, l.19]; "Secured three New Business Model ("NBM") partnerships backed by firm financial guarantees, with an additional two NBMs in the current fiscal fourth quarter." [Q3 FY2026 slides, p.3]; then five more per [Q4 FY2026 release, l.16]. Gatherer arithmetic: 5 + 5 = 10 agreements; 5 + 3 new customers = 8 customers, matching the deck's "8 Customers".
- Investor Day detail (August 13, 2026) [2026 Investor Day slides]: "8 Individual Customers"; "DATACENTER-CENTRIC"; "2 Customers Already Expanded Their NBMs" (p.60); "Average Weighted Length of Contract is 4+ Years"; "Longest Engagement is 5 Years"; "Exploring Opportunities to Go Further Out in Time" (p.61); "FY 2027 ~1/2 BITS; FY 2028 ~2/3 BITS" under NBM; NBM pricing "Combination Fixed and Variable (Floor and Ceiling Pricing)", non-NBM pricing "Fluctuate with the Market" (p.62); "$93.9B Total Contract Value (TCV) for the 8 NBM Customers at Floor Pricing"; "$91.1B Remaining Performance Obligation (RPO) for the 8 NBM Customers at Floor Pricing"; "Expect Upside Pricing and Revenue"; footnotes: "1. Total revenue expected, over the life of the agreements, for all agreements that have been signed up through August 3, 2026. 2. This RPO amount includes deals signed through August 3, 2026; the FQ4'26 ending RPO was lower." (p.63); "Total Financial Guarantees of $16.5B Primarily Held by or Provided Through Third-Party Financial Institutions, with $2.5B in Our Cash Balance"; "Unless They Have Prepaid in Cash, Customers Pay for Products in the Ordinary Course and Not Through Amortization of Financial Guarantees" (p.64); "In Each Multi-Year Contract, the Ratio Between the Financial Guarantees and the RPO Increases Over Time"; "Other than Cash Prepayments, the Financial Guarantees Remain Constant until the Final Periods of the Contracts, While RPO Reduces over Time" (p.65); priorities "Execute NBMs with Excellence" and "Remain Highly Selective and Patient in Evaluating Additional NBMs" (p.66).
- Investor Day release wording: "Sandisk has signed NBMs with eight customers, representing approximately 50 percent of bits in FY2027 and approximately two-thirds of bits in FY2028." [2026 Investor Day release, l.26]; "50% FY27 Supply under NBMs with Committed Economics ... Growing to approximately 67% in FY28"; "1 to 5 years, with average weighted length of 4+ years"; "Bigger customers have longer commitments"; "Above market level of volume growth" [2026 Investor Day slides, p.11].
- Gatherer arithmetic: the $2.5 billion of guarantees "in our cash balance" matches the FY26 "Impact of NBM prepayments and deposits" of $2,476 in the cash-flow reconciliation (§4).
- Not disclosed: customer names; the split of the $93.9B by customer or by year; the RPO at quarter-end by end market; what "floor pricing" is in $/GB.

## 4. Cash flow, capital expenditure and balance sheet

Cash-flow reconciliation [Q4 FY2026 release, "Reconciliation of GAAP to Non-GAAP Financial Measures", l.348–354; identical on Q4 FY2026 slides, p.22]:

| (in millions) | Q4 (Jul 3, 2026) | Q3 (Apr 3, 2026) | Q4 (Jun 27, 2025) | FY26 | FY25 |
|---|---|---|---|---|---|
| Cash flow from operating activities | $7,126 | $3,038 | $94 | $11,671 | $84 |
| Purchases of property, plant and equipment, net | (43) | (45) | (45) | (177) | (204) |
| Free cash flow | 7,083 | 2,993 | 49 | 11,494 | (120) |
| Activity related to Flash Ventures, net | (110) | (38) | 28 | (275) | 358 |
| Impact of NBM prepayments and deposits | (1,938) | (538) | — | (2,476) | — |
| Adjusted free cash flow | $5,035 | $2,417 | $77 | $8,743 | $238 |

- Company definitions, verbatim: "Free cash flow is defined as Cash Flow from operating activities less purchases of property, plant and equipment, net. Adjusted free cash flow is defined as Free cash flow plus the activity related to Flash Ventures, net less the impact of cash prepayments under NBM agreements (the "NBM Prepayments") and deposits received and returned under NBM agreements (the "NBM Deposits" and together with the NBM Prepayments, the "NBM Payments"). The Company is adjusting for the NBM Payments because the Company believes that these cash flows are not indicative of the core underlying cash flows of the Company's business." [Q4 FY2026 release, l.384]. "Cash flow from operating activities margin and Adjusted free cash flow margin are calculated by dividing Cash flow from operating activities and Adjusted free cash flow, respectively, by Revenue." [l.386]
- **Definition change (gatherer observation):** the Q3 FY2026 release defined Adjusted free cash flow as "free cash flow plus the activity related to Flash Ventures, net" with no NBM line, and printed Q3'26 Adjusted free cash flow as $2,955 [Q3 FY2026 release, l.325, l.353; Q3 FY2026 slides, p.3, p.7, p.16]. The Q4 FY2026 release adds the NBM Payments deduction and restates Q3'26 to $2,417 (538 lower). Q2'26 ($843) and earlier quarters are unchanged because the NBM line is "—" for them [2026 Investor Day slides, p.75]. The Q4 FY2025 release used the same definition as the Q3 FY2026 release [Q4 FY2025 release, l.361–365].
- Quarterly cash-flow history [2026 Investor Day slides, p.75]: OCF Q4'25 $94; Q1'26 $488; Q2'26 $1,019; Q3'26 $3,038; Q4'26 $7,126. PP&E purchases (45), (50), (39), (45), (43). Free cash flow 49, 438, 980, 2,993, 7,083. Flash Ventures activity 28, 10, (137), (38), (110). NBM impact —, —, —, (538), (1,938). Adjusted FCF $77, $448, $843, $2,417, $5,035. FY'25 column: OCF 84; PP&E (204); FCF (120); FV 358; adjusted FCF 238.
- Older cash-flow columns [Q4 FY2025 release, l.361–365]: Q4 2025 / Q3 2025 / Q4 2024 / FY2025 / FY2024: operating cash flow $94 / $26 / $(130) / $84 / $(309); free cash flow 49 / (18) / (165) / (120) / (338); Flash Ventures activity 28 / 238 / 32 / 358 / 239; adjusted free cash flow $77 / $220 / $(133) / $238 / $(99).
- Deck statements: "$5.0B Adjusted Free Cash Flow" with footnote "Excludes $1,938 million related to NBM prepayments and deposits" [Q4 FY2026 slides, p.6]; "Full-year Adjusted free cash flow of $8.7B, which excludes $2.5B of NBM pre-payments / deposits"; "Annualized Q4 Adjusted free cash flow of $20B" [2026 Investor Day slides, p.58]. Gatherer arithmetic: 5,035 × 4 = 20,140.
- Gatherer arithmetic: Q4'26 OCF margin = 7,126 / 8,965 = 79.5%; adjusted FCF margin = 5,035 / 8,965 = 56.2%; FY26 adjusted FCF margin = 8,743 / 20,248 = 43.2%. The company's own margin figures are not printed in the release.
- Gatherer arithmetic: the Flash Ventures line equals the two cash-flow-statement lines "Notes receivable issuances to Flash Ventures" (123) plus "Notes receivable proceeds from Flash Ventures" 13 = (110) for Q4; (462) + 187 = (275) for FY26 [Q4 FY2026 release, l.255–256].
- Gatherer arithmetic: the cash-flow statement's working-capital lines "Refund liability" 1,360 and "Contract liabilities" 731 sum to 2,091 for Q4 (FY: 1,374 + 1,217 = 2,591) [l.246–247], versus the NBM Payments adjustment of 1,938 (FY 2,476). The release does not reconcile the two.

Consolidated statement of cash flows, selected lines [Q4 FY2026 release, l.217–286] (Q4'26 | Q4'25 | FY26 | FY25):
- Net cash provided by operating activities 7,126 | 94 | 11,671 | 84.
- Changes in accounts receivable (1,982) | (89) | (3,640) | (100); inventories (460) | 81 | (619) | (160); accrued compensation 304 | 59 | 460 | 21; refund liability 1,360 | 4 | 1,374 | 25; contract liabilities 731 | 4 | 1,217 | (11); income taxes payable 730 | — | 1,370 | —.
- Deferred income taxes 162 | (19) | 120 | (12); (gain) loss on equity securities, net (804) | 1 | (808) | 2; unrealized foreign exchange (gain) loss 47 | (19) | 86 | (25); equity loss in investees, net of dividends received 102 | 5 | 160 | 73.
- Investing: purchase of marketable equity securities (970) | — | (970) | —; purchases of PP&E (43) | (45) | (177) | (204); proceeds from dispositions of business — | — | 25 | 401; notes receivable issuances to Flash Ventures (123) | (59) | (462) | (333); notes receivable proceeds from Flash Ventures 13 | 87 | 187 | 515; distributions from Flash Ventures — | — | — | 176; net investing (1,123) | (17) | (1,386) | 556.
- Financing: issuance of stock under employee stock plans 29 | 5 | 53 | 5; taxes paid on vested stock awards (481) | (7) | (630) | (13); repurchases of common stock (4,524) | — | (4,524) | —; proceeds from debt — | — | — | 1,970; repayment of debt — | (100) | (1,900) | (100); transfers to Western Digital — | — | — | (1,887); net financing (4,976) | (102) | (7,001) | 518.
- Cash and cash equivalents: beginning 3,735 | 1,507 | 1,481 | 328; end $4,762 | $1,481 | $4,762 | $1,481.
- Supplemental: cash paid for interest $5 | $37 | $116 | $139; cash received for interest 30 | — | 70 | 2; cash paid for income taxes 29 | 40 | 146 | 50. Gatherer arithmetic: FY26 cash taxes paid (146) versus FY26 GAAP income tax expense (1,584); the balance sheet shows income tax payable, current, of 1,286 at July 3, 2026 (§ below).

Capital expenditure as the company frames it [Q4 FY2026 slides, p.14; Q3 FY2026 slides, p.8]:

| (in millions) | Quarter ended July 3, 2026 | Quarter ended April 3, 2026 |
|---|---|---|
| Revenue, net | $8,965 | $5,950 |
| Sandisk share of JV Gross CapEx | $519 | $195 |
| External funding | $290 | $39 |
| Sandisk wafer purchases (tool depreciation) | $119 | $118 |
| CapEx funding | $409 | $157 |
| Sandisk share of JV Cash CapEx (front-end) | $110 | $38 |
| Purchases of PP&E (backend and offices) | $43 | $45 |
| Total Sandisk Cash CapEx | $153 | $83 |
| % of revenue, net | 1.7% | 1.4% |
| Total Sandisk Gross CapEx | $562 | $240 |
| % of revenue, net | 6.3% | 4.0% |

- Explanatory bullets, verbatim [Q4 FY2026 slides, p.14]: "JV Gross CapEx fluctuates based primarily on node transitions and aligning supply with demand"; "JV Gross CapEx is funded through a mix of external (e.g., subsidies, leasing, vendor terms) and internal sources (e.g., tool depreciation in COGS)"; "Sandisk's share of JV Cash CapEx and PP&E purchases comprise total Cash CapEx, net"; "The majority of the fiscal 2026 CapEx supported BiCS8 technology investments".
- Gatherer arithmetic: Sandisk share of JV Gross CapEx 519 = External funding 290 + wafer purchases 119 + JV Cash CapEx 110 (= 519); Total Gross CapEx 562 = 519 + 43. Full-year gross or cash capex totals are not printed in the deck or release.
- Joint venture framework [Q4 FY2026 slides, p.18; same page in Q3 FY2026 slides, p.10]: "Flash Ventures 49.9% Owned by Sandisk, 50.1% Owned by Kioxia". Flash Ventures "Owns and leases equipment for flash wafer production and R&D line"; "Purchases wafers from Kioxia at cost under foundry agreements"; "Sells wafers to Sandisk and Kioxia at cost plus a small markup"; "Borrows from Sandisk and Kioxia for a portion of their equipment purchases". Sandisk "Funds Flash Ventures' equipment purchases (via loans, equity and lease guarantees) in excess of Flash Ventures' operating cash flow". Kioxia "Owns and operates cleanrooms" and "Provides wafer manufacturing services to Flash Ventures at cost".

Balance sheet [Q4 FY2026 release, "Consolidated Balance Sheets", l.127–172], with the April 3, 2026 column from [Q3 FY2026 release, l.111–149]:

| (in millions) | July 3, 2026 | April 3, 2026 | June 27, 2025 |
|---|---|---|---|
| Cash and cash equivalents | $4,762 | $3,735 | $1,481 |
| Accounts receivable, net | 4,708 | 2,726 | 1,068 |
| Inventories | 2,698 | 2,238 | 2,079 |
| Income tax receivable | 22 | 81 | 66 |
| Other current assets | 590 | 388 | 392 |
| Total current assets | 12,780 | 9,168 | 5,086 |
| Marketable equity securities | 1,777 | (no line) | — |
| Property, plant and equipment, net | 674 | 649 | 619 |
| Notes receivable and investments in Flash Ventures | 678 | 684 | 654 |
| Goodwill | 4,994 | 4,994 | 4,999 |
| Income tax receivable, non-current | 169 | 134 | 80 |
| Deferred tax assets | 66 | 87 | 58 |
| Other non-current assets | 1,369 | 1,359 | 1,489 |
| Total assets | $22,507 | $17,075 | $12,985 |
| Accounts payable | $516 | $416 | $366 |
| Accounts payable to related parties | 460 | 435 | 400 |
| Accrued expenses | 313 | 383 | 274 (Q3 release prints 400) |
| Accrued compensation | 657 | 329 | 173 |
| Refund liabilities | 1,500 | (no line) | 126 |
| Contract liabilities | 849 | 323 | 25 |
| Income tax payable, current | 1,286 | 31 | 43 |
| Current portion of long-term debt | — | — | 20 |
| Total current liabilities | 5,581 | 1,917 | 1,427 |
| Deferred tax liabilities | 161 | 17 | 17 |
| Income tax payable, non-current | 258 | 783 | 131 |
| Long-term debt | — | — | 1,829 |
| Non-current contract liabilities | 393 | 188 | — |
| Other liabilities | 378 | 393 | 365 |
| Total liabilities | 6,771 | 3,298 | 3,769 |
| Common stock | $1 | $1 | $1 |
| Treasury stock | (4,537) | (no line) | — |
| Additional paid-in capital | 10,879 | 11,289 | 11,248 |
| Accumulated other comprehensive loss | (256) | (259) | (249) |
| Retained earnings (accumulated deficit) | 9,649 | 2,746 | (1,784) |
| Total shareholders' equity | 15,736 | 13,777 | 9,216 |
| Total liabilities and shareholders' equity | $22,507 | $17,075 | $12,985 |

- Common stock line as printed: "Common stock, $0.01 par value; authorized — 450 shares; issued and outstanding — 149 shares and 146 shares, respectively (issued and outstanding as of June 27, 2025 - 146 shares)" [Q4 FY2026 release, l.166]; the Q3 FY2026 release printed "148 shares and 146 shares, respectively" [Q3 FY2026 release, l.144]. The printed share count rises from 148 to 149 across a quarter with $4,524 of repurchases; the release does not explain (gatherer observation; treasury stock of $4,537 is shown as a separate line).
- Gatherer observation: the June 27, 2025 "Accrued expenses" is 400 in the Q3 FY2026 release but 274 plus a new "Refund liabilities" line of 126 in the Q4 FY2026 release (274 + 126 = 400), so the Q4 release broke refund liabilities out of accrued expenses; the April 3, 2026 refund-liability balance is therefore not available on a comparable basis.
- Debt: total debt is zero at July 3, 2026 (both debt lines "—"); at June 27, 2025 it was 20 + 1,829 = 1,849 (gatherer arithmetic). FY26 repayment of debt 1,900 (Q3'26: 650; nine months to April 3, 2026: 1,900 [Q3 FY2026 release, l.239]); loss on debt extinguishment 46 in Q3'26. "Announced a $6B share repurchase program following full debt repayment" [Q3 FY2026 slides, p.3]. Interest expense Q4'26 $(2) [Q4 FY2026 release, l.200].
- Marketable equity securities $1,777 is a new balance-sheet line; Q4'26 shows "Purchase of marketable equity securities (970)" and "Gain (loss) on equity securities, net 804" (gatherer arithmetic: 970 + 804 = 1,774, within 3 of the balance). The release does not name the investment. The Investor Day deck has a page headed "INVEST IN THE BUSINESS — NANYA INVESTMENT" whose extracted bullets include "~4% Equity Stake" and "Secure DRAM for eSSD Portfolio" [2026 Investor Day slides, p.7]; no document states that this is the security on the balance sheet.
- Net cash (gatherer arithmetic): cash 4,762 with zero debt = 4,762 at July 3, 2026; the company does not print a "net cash" figure. "Cash and Cash Equivalents of $3.74 billion" at Q3 [Q3 FY2026 slides, p.3].
- Inventory days: not disclosed. Gatherer arithmetic only (GAAP cost of revenue, 91-day quarter): Q4'26 = 2,698 / 1,383 × 91 = 177.5 days; Q3'26 = 2,238 / 1,288 × 91 = 158.1 days; Q4'25 = 2,079 / 1,403 × 91 = 134.8 days. Deck statement: "Higher inventory days, consistent with current levels, support our NBMs and account for higher component costs" [Q4 FY2026 slides, p.16].
- Receivables rose 1,982 in the quarter and 3,640 in the year [Q4 FY2026 release, l.240]; no explanation is given in the release.

Capital return:
- Buyback authorisation: "$20 billion of buyback authorized since separation, with $4.5 billion spent and $15.5 billion remaining authorization" [Q4 FY2026 slides, p.16]; "additional $14 billion buyback program, bringing total remaining authorization to $15.5 billion" [Q4 FY2026 release, l.18]; the earlier programme was "$6B" [Q3 FY2026 slides, p.3]. Gatherer arithmetic: 6 + 14 = 20; 20 − 4.5 = 15.5.
- Repurchases in Q4'26: "Repurchases of common stock (4,524)" [Q4 FY2026 release, l.263]; deck: "$4.5 billion of stock repurchased" [Q4 FY2026 slides, p.3]. No repurchases in Q3'26 or earlier in FY26 (the FY26 total equals the Q4 figure). Share count retired: not disclosed.
- Dividend: none declared or mentioned in any cached document (searched "dividend": only "dividends received" from investees).
- "Capital allocation priorities: invest in the business and return excess cash to shareholders" [Q4 FY2026 slides, p.16]; Investor Day: "Return 100% Excess Cash to Shareholders"; "Maintain Strong Balance Sheet — Healthy cash balance; No debt; Improve credit rating" [2026 Investor Day slides, p.69].

## 5. Business Outlook — Q1 FY2027 guidance (verbatim)

"Business Outlook for Fiscal First Quarter of 2027" [Q4 FY2026 release, l.83–95; identical table on Q4 FY2026 slides, p.15]:

| (in millions, except per share amounts) | GAAP | Non-GAAP (1) |
|---|---|---|
| Revenue | $10,300 - $10,800 | $10,300 - $10,800 |
| Gross Margin | 83.0% - 84.9% | 83.0% - 85.0% |
| Operating Expenses | $574 - $614 | $520 - $540 |
| Tax Expense (2) | N/A | 15.0% |
| Diluted Net Income Per Share | N/A | $44.00 - $46.00 |
| Diluted Shares Outstanding | ~ 155 | ~ 155 |

Footnotes, verbatim [l.93, l.95]:
- "(1) Non-GAAP gross margin guidance excludes stock-based compensation expense, totaling approximately $5 million to $7 million. The Company's Non-GAAP operating expenses guidance excludes stock-based compensation expense, totaling approximately $54 million to $74 million. Non-GAAP diluted net income per share guidance excludes these items totaling $59 million to $81 million. The timing and amount of these charges excluded from Non-GAAP gross margin, Non-GAAP operating expenses, and Non-GAAP diluted net income per share cannot be further allocated or quantified with certainty. Additionally, the timing and amount of certain other adjustments included in the Company's Non-GAAP diluted net income per share guidance are dependent on the timing and determination of certain actions or events and cannot be reasonably predicted. Accordingly, full reconciliations of Non-GAAP gross margin, Non-GAAP operating expenses, and Non-GAAP diluted net income per share to the most directly comparable GAAP financial measures (gross margin, operating expenses, and diluted net income per share, respectively) are not available without unreasonable effort."
- "(2) Non-GAAP tax expense is determined based on a Non-GAAP pre-tax income or loss. Our estimated Non-GAAP tax expense may differ from our GAAP tax expense (i) due to differences in the tax treatment of items excluded from our Non-GAAP net income or loss; (ii) due to the fact that our GAAP income tax expense or benefit recorded in any interim period is based on an estimated forecasted GAAP tax expense for the full year, excluding loss jurisdictions; and (iii) because our GAAP taxes recorded in any interim period are dependent on the timing and determination of certain GAAP operating expenses."

- Presentation changes versus the Q4 FY2026 guidance given in April (gatherer observation): the Q1 FY2027 table has no "Interest and Other Income (Expense), Net" row (the April table had "$12 - $32" GAAP / "$10 - $30" non-GAAP), and tax is given as a rate ("15.0%") rather than a dollar range ("$775 - $875").
- Gatherer arithmetic: revenue midpoint $10,550 is +$1,585 (+17.7%) over Q4'26's $8,965 (range: +14.9% to +20.5%); non-GAAP EPS midpoint $45.00 is +14.6% over Q4'26's $39.25; implied non-GAAP net income at the midpoint = 45.00 × 155 = 6,975.
- Full-year FY2027 items, verbatim ("Financial Outlook") [Q4 FY2026 slides, p.16]:
  - "Capital spending increases YoY as we ramp BiCS 8 and BiCS 10, consistent with growing supply mid-to-high teens"
  - "Investment relative to revenue comes down to approximately 6% of revenue for the full year"
  - "Higher inventory days, consistent with current levels, support our NBMs and account for higher component costs"
  - "Higher inventory levels reduce sellable bit growth to mid-teens for the full year"
  - "Capital allocation priorities: invest in the business and return excess cash to shareholders"
  - "$20 billion of buyback authorized since separation, with $4.5 billion spent and $15.5 billion remaining authorization"
  - The slide does not name the fiscal year for "the full year" and gives no dollar figure for FY2027 capex or Flash Ventures investment. The release contains no full-year FY2027 guidance of any kind.
- No long-term targets appear in the Q4 FY2026 release or earnings deck; the FY2028–FY2030 model is in the Investor Day materials (§11).

## 6. Prior quarter (Q3 FY2026 release and deck): what management said to expect for Q4 FY2026, and Q3 actuals

Q4 FY2026 guidance as given April 30, 2026, verbatim [Q3 FY2026 release, "Business Outlook for Fiscal Fourth Quarter of 2026", l.63–75; identical on Q3 FY2026 slides, p.9]:

| (in millions, except per share amounts) | GAAP | Non-GAAP (1) |
|---|---|---|
| Revenue | $7,750 - $8,250 | $7,750 - $8,250 |
| Gross Margin | 78.9% - 80.9% | 79.0% - 81.0% |
| Operating Expenses | $523 - $558 | $480 - $500 |
| Interest and Other Income (Expense), Net | $12 - $32 | $10 - $30 |
| Tax Expense (2) | N/A | $775 - $875 |
| Diluted Net Income Per Share | N/A | $30.00 - $33.00 |
| Diluted Shares Outstanding | ~ 158 | ~ 158 |

Footnote (1), verbatim [Q3 FY2026 release, l.73]: "Non-GAAP gross margin guidance excludes stock-based compensation expense, totaling approximately $4 million to $6 million. The Company's Non-GAAP operating expenses guidance excludes stock-based compensation expense, totaling approximately $43 million to $58 million. The Company's Non-GAAP interest and other income (expense), net guidance excludes the accretion of the present value discount on consideration receivable from the sale of an interest in a subsidiary, totaling approximately $2 million. In the aggregate, Non-GAAP diluted net income per share guidance excludes these items totaling $45 million to $62 million. ..." (remainder is the same "cannot be further allocated" language as in §5).

News-summary wording: "Expect fourth quarter revenue to be in the range of $7.75 billion to $8.25 billion, with expected Non-GAAP diluted net income per share to be in the range of $30.00 to $33.00." [Q3 FY2026 release, l.21]

Q4 actual vs Q4 guidance (actuals from [Q4 FY2026 release]; guidance from [Q3 FY2026 release]; differences are gatherer arithmetic):

| Item | Guidance (Apr 30, 2026) | Actual Q4 FY2026 | Gatherer arithmetic |
|---|---|---|---|
| Revenue | $7,750 - $8,250 | $8,965 | +$715 above the top of the range; +$965 (+12.1%) vs midpoint $8,000 |
| Non-GAAP gross margin | 79.0% - 81.0% | 84.6% | +3.6 points above the top; +4.6 vs midpoint |
| GAAP gross margin | 78.9% - 80.9% | 84.6% | +3.7 points above the top |
| Non-GAAP operating expenses | $480 - $500 | $484 | inside the range |
| GAAP operating expenses | $523 - $558 | $545 | inside the range |
| Non-GAAP interest and other income (expense), net | $10 - $30 | $8 | $2 below the bottom of the range |
| Non-GAAP tax expense | $775 - $875 | $950 | $75 above the top |
| Non-GAAP diluted EPS | $30.00 - $33.00 | $39.25 | +$6.25 above the top; +$7.75 (+24.6%) vs midpoint $31.50 |
| Diluted shares | ~158 | 157 | 1 million fewer |

Q3 FY2026 headline actuals [Q3 FY2026 release, l.31–47]:
- GAAP: revenue $5,950 (up 97% Q/Q, up 251% Y/Y); gross margin 78.4% (Q2'26 50.9%; Q3'25 22.5%); operating expenses $551; operating income $4,111; net income $3,615; diluted EPS $23.03.
- Non-GAAP: gross margin 78.4% (Q2'26 51.1%; Q3'25 22.7%); operating expenses $448 (Q2'26 $413); operating income $4,218 (Q2'26 $1,133; Q3'25 $2); net income $3,675 (Q2'26 $967; Q3'25 $(43)); diluted EPS $23.41 (Q2'26 $6.20; Q3'25 $(0.30)).
- Q3'26 news summary: "Third quarter revenue was $5.95 billion, up 97% sequentially and above the guidance range, with GAAP net income reported at $3,615 million ($23.03 diluted net income per share). Revenue outperformance was driven by both our mix shift toward higher-value customers, with Datacenter up 233%, and higher pricing. Third quarter Non-GAAP diluted net income per share was $23.41." [Q3 FY2026 release, l.17]
- CEO quote at Q3: "This quarter marks a fundamental inflection point for Sandisk — where our technology leadership is enabling a deliberate shift in our mix toward the highest-value end markets, led by Datacenter," said David Goeckeler, CEO of Sandisk. "We are also advancing to a new business model built on multi-year customer engagements backed by firm financial commitments. Together, this transformation is driving structurally higher and more durable earnings power." [Q3 FY2026 release, l.25]
- Q3'26 end markets: Datacenter $1,467 (Q2'26 $440, up 233%; Q3'25 $197, up 645%); Edge $3,663 (Q2'26 $1,678, up 118%; Q3'25 $927, up 295%); Consumer $820 (Q2'26 $907, down 10%; Q3'25 $571, up 44%) [Q3 FY2026 release, l.53–57].
- Q3'26 cash and balance sheet: OCF $3,038; PP&E (45); free cash flow 2,993; adjusted FCF $2,955 (as then defined); cash $3,735; inventories 2,238; receivables 2,726; long-term debt — (repaid 650 in the quarter) [Q3 FY2026 release, l.111–149, l.226–249, l.321–325].
- Q3'26 deck statements, verbatim [Q3 FY2026 slides]: "Further expansion into the large, fast-growing Datacenter end market with our leading technology" (p.3); "Revenue reached $1.5B, up 233% sequentially — reflecting years of innovation to shift toward this attractive market"; "Fiscal third quarter revenue was enhanced by strong demand for our TLC-based enterprise SSD portfolio, which powers performance intensive compute workloads where speed and latency are paramount"; "In the fiscal fourth quarter, we expect to begin shipping our QLC Stargate solutions for revenue, adding another layer of revenue growth" (p.4); Edge "Revenue reached $3.7B, up 118% sequentially as demand continued to shift toward premium devices across both PC and smartphone markets"; Consumer "Revenue reached $0.8B, down 10% sequentially, in line with historical seasonality. Year-over-year revenue growth was broad based"; "The February launch of our next-generation Portable SSD portfolio ..."; "Introduced our 'Space to Hold More' campaign" (p.5).
- Q3'26 claims a writer can grade against Q4: (a) Q4 revenue $7.75–8.25B → actual $8,965 (above); (b) QLC Stargate to begin shipping for revenue in Q4 → "This quarter we began shipping our QLC Stargate platform for revenue" [Q4 FY2026 slides, p.5]; (c) two additional NBMs signed in Q4 → five more agreements announced in the Q4 release (three new customers, two expansions; "three closed pre-quarter-end and two after quarter-end").

## 7. Year-ago quarter (Q4 FY2025 release): Q1 FY2026 guidance style and FY2025 reference

- Title: "Sandisk Reports Fiscal Fourth Quarter 2025 Financial Results" [Q4 FY2025 release, l.13]. News summary: "Fiscal fourth quarter revenue was $1.90 billion, up 12% sequentially and above the guidance range."; "Fiscal fourth quarter GAAP loss was $23 million ($0.16 diluted loss per share), and fourth quarter Non-GAAP diluted earnings per share (EPS) was $0.29." [l.17–19]
- Q4 2025 highlights [l.34–50]: revenue $1,901 (Q3 2025 $1,695, up 12%; Q4 2024 $1,760, up 8%); GAAP gross margin 26.2% (Q4 2024 36.1%); non-GAAP gross margin 26.4% (Q3 2025 22.7%; Q4 2024 36.4%); non-GAAP operating expenses $402 (Q4 2024 $386); non-GAAP operating income $100 (Q4 2024 $255); non-GAAP net income $42 (Q4 2024 $180); non-GAAP EPS $0.29 (Q4 2024 $1.24).
- FY2025 vs FY2024 [l.52–60]: revenue $7,355 vs $6,663 (up 10%); GAAP gross margin 30.1% vs 16.1%; non-GAAP gross margin 30.3% vs 15.8%; GAAP operating expenses $3,589 vs $1,540; non-GAAP operating expenses $1,539 vs $1,365; GAAP operating loss $(1,377) vs $(468); non-GAAP operating income $689 vs $(309); GAAP net loss $(1,641) vs $(672); non-GAAP net income $440 vs $(502); non-GAAP EPS $2.99 vs $(3.46).
- End markets [l.62–69]: Cloud $213 / $197 / $170 (Q4 2025 / Q3 2025 / Q4 2024), FY2025 $960 vs FY2024 $325 (up 195%); Client 1,103 / 927 / 1,067, FY 4,127 vs 4,069 (up 1%); Consumer 585 / 571 / 523, FY 2,268 vs 2,269 ("—"); total FY 7,355 vs 6,663.
- Q1 FY2026 guidance given August 14, 2025 [l.75–88]: Revenue ($B) $2.10 - $2.20; gross margin 28.3% - 29.2% GAAP / 28.5% - 29.5% non-GAAP; operating expenses ($M) $475 - $490 / $415 - $430; interest and other expense, net ($M) $38 - $43 / $40 - $45; tax expense ($M) N/A / $35 - $40; non-GAAP diluted EPS $0.70 - $0.90; diluted shares ~148. (Q1 FY2026 actual revenue was $2,308 and non-GAAP EPS $1.22 per [2026 Investor Day slides, p.72, p.74].)
- Adjusted free cash flow definition at that time: free cash flow "plus the activity related to Flash Ventures, net" only (no NBM line) [Q4 FY2025 release, l.361–365].

## 8. Non-GAAP reconciliations (adjustment items and sizes)

Operating lines [Q4 FY2026 release, l.296–319; same on Q4 FY2026 slides, p.19–20]:

| (in millions) | Q4'26 | Q3'26 | Q4'25 | FY26 | FY25 |
|---|---|---|---|---|---|
| GAAP gross profit | $7,582 | $4,662 | $498 | $14,472 | $2,212 |
| + Stock-based compensation expense | 6 | 4 | 4 | 19 | 16 |
| Non-GAAP gross profit | $7,588 | $4,666 | $502 | $14,491 | $2,228 |
| GAAP operating expenses | $545 | $551 | $480 | $2,083 | $3,589 |
| − Goodwill impairment | — | — | — | — | (1,830) |
| − Stock-based compensation expense | (61) | (50) | (45) | (213) | (166) |
| − Business separation costs | — | (7) | (17) | (25) | (67) |
| − Employee termination and other | — | — | (16) | 2 | (21) |
| − (Loss) gain on business divestiture | — | — | — | (10) | 34 |
| − Loss on debt extinguishment | — | (46) | — | (46) | — |
| Non-GAAP operating expenses | $484 | $448 | $402 | $1,791 | $1,539 |
| GAAP operating income (loss) | $7,037 | $4,111 | $18 | $12,389 | $(1,377) |
| + Gross profit adjustments | 6 | 4 | 4 | 19 | 16 |
| + Operating expense adjustments | 61 | 103 | 78 | 292 | 2,050 |
| Non-GAAP operating income | $7,104 | $4,218 | $100 | $12,700 | $689 |
| GAAP interest and other income (expense), net | $812 | $(4) | $(36) | $628 | $(102) |
| (Gain) loss on equity securities, net | (804) | — | 1 | (808) | 2 |
| Other, net | — | 1 | (2) | 111 | (9) |
| Non-GAAP interest and other income (expense), net | $8 | $(3) | $(37) | $(69) | $(109) |
| GAAP income tax expense | $946 | $492 | $5 | $1,584 | $162 |
| Income tax adjustments | 4 | 48 | 16 | 60 | (22) |
| Non-GAAP income tax expense | $950 | $540 | $21 | $1,644 | $140 |

Net income and EPS [Q4 FY2026 release, l.329–347; same on Q4 FY2026 slides, p.21]:

| (in millions, except per share) | Q4'26 | Q3'26 | Q4'25 | FY26 | FY25 |
|---|---|---|---|---|---|
| GAAP net income (loss) | $6,903 | $3,615 | $(23) | $11,433 | $(1,641) |
| + Goodwill impairment | — | — | — | — | 1,830 |
| + Stock-based compensation expense | 67 | 54 | 49 | 232 | 182 |
| + Business separation costs | — | 7 | 17 | 25 | 67 |
| + Employee termination and other | — | — | 16 | (2) | 21 |
| + (Gain) loss on business divestiture | — | — | — | 10 | (34) |
| + Loss on debt extinguishment | — | 46 | — | 46 | — |
| + (Gain) loss on equity securities, net | (804) | — | 1 | (808) | 2 |
| + Other, net | — | 1 | (2) | 111 | (9) |
| + Income tax adjustments | (4) | (48) | (16) | (60) | 22 |
| Non-GAAP net income | $6,162 | $3,675 | $42 | $10,987 | $440 |
| Diluted EPS, GAAP | $43.97 | $23.03 | $(0.16) | $73.76 | $(11.32) |
| Diluted EPS, non-GAAP | $39.25 | $23.41 | $0.29 | $70.88 | $2.99 |
| Diluted shares, GAAP | 157 | 157 | 145 | 155 | 145 |
| Diluted shares, non-GAAP | 157 | 157 | 147 | 155 | 147 |

- Q4'26 is the cleanest quarter in the series: the only adjustments are stock-based compensation (67 in total: 6 in cost of revenue, 61 in operating expenses), the (804) equity-securities gain, and a (4) tax adjustment. There is no restructuring, impairment, separation, or amortization-of-intangibles adjustment in Q4'26 (the company does not adjust for intangible amortization at all).
- FY26 "Other, net" 111: "For the year ended July 3, 2026, Other adjustments include charges for the settlement of certain previously existing legal matters." [Q4 FY2026 release, l.378]. The Q3 release described the nine-month "Other" as "charges for the settlement of certain previously existing legal matters and the impairment of an investment, partially offset by a gain upon sale of a..." [Q3 FY2026 release, l.347]. By quarter [2026 Investor Day slides, p.74]: Q1'26 10; Q2'26 100; Q3'26 1; Q4'26 —.
- The company's stated exclusion list [Q4 FY2026 release, l.360–380; Q4 FY2026 slides, p.23–24]: goodwill impairment ($1.8 billion in Q3 FY2025, tied to "the trading price of the Company's common stock and resulting market capitalization"); stock-based compensation; business separation costs (WDC separation, completed February 21, 2025); employee termination and other; (gain) loss on business divestiture ("on September 28, 2024, the Company completed the sale of 80% of its equity interest in one of its manufacturing subsidiaries"; a $10 million working-capital provision in Q1 FY2026); loss on debt extinguishment; (gain) loss on equity securities, net ("ongoing mark-to-market adjustments on the Company's investments in marketable equity securities"); other adjustments; income tax adjustments.
- Q2'26 and Q1'26 columns [Q3 FY2026 release, l.270–319; 2026 Investor Day slides, p.72–74]: Q2'26 GAAP operating expenses $476, SBC (53), separation (9), employee termination (1), non-GAAP $413; GAAP interest and other $(128), Other, net 94 (Investor Day deck: equity securities (4), Other 100), non-GAAP $(34) (Investor Day deck: $(32)). Q1'26 GAAP operating expenses $511, SBC (49), separation (9), employee termination 3, divestiture (10), non-GAAP $446; GAAP interest and other $(52), non-GAAP $(42); GAAP tax $12, non-GAAP $22.

## 9. Slides: page-by-page key numbers and claims (Q4 FY2026 deck, 25 PDF pages)

Deck: "FINANCIAL RESULTS — FISCAL FOURTH QUARTER 2026", "AUGUST 5, 2026 | QUARTER ENDED 07.03.26", marked "[PUBLIC]" (p.1). PDF metadata: created 2026-08-05 05:08 UTC, author "Susan Oak". Printed footer "00.0N" equals PDF page N.

- p.2 Disclaimers: forward-looking statements and non-GAAP notice. Risk list includes "our reliance on strategic relationships with key partners, including Kioxia Corporation; risks related to our long-term agreements"; "risks related to our share repurchase program". Notes results are preliminary until the 10-K.
- p.3 Overview: five bullets quoted in §1 ("fundamental inflection point"; "BiCS leadership across TLC and QLC, advanced HBF"; "New business models ("NBMs"), a more resilient supply chain, and a strengthened balance sheet support growing, durable free cash flow"; "record revenue, gross margin, and EPS, each above the high end of guidance, with $4.5 billion of stock repurchased"; "structurally higher and more durable earnings power").
- p.4 The Era of Inference: quoted in §2.
- p.5 Technology and Product Leadership: quoted in §2. Also: "Future generations extend performance and cost leadership through continued innovation across multiple dimensions of scaling".
- p.6 Financial Highlights: ~$9.0B revenue (+51% QoQ, +372% YoY); $39.25 non-GAAP EPS; 84.6% non-GAAP gross margin; $5.0B adjusted FCF (excludes $1,938 million NBM prepayments and deposits); one-third volume / two-thirds pricing sentence.
- p.7 Performance by End-market: chart (five quarters, unlabelled bars; gross-margin line 26%, 30%, 51%, 78%, 85%) plus text tiles quoted in §2.
- p.8 Datacenter; p.9 Edge; p.10 Consumer: quoted in §2. p.8 source line: "Sandisk Internal Market Model".
- p.11 NBMs: §3.
- p.12 Market Outlook: §2 (NAND market >$300B CY2026, $500B CY2027; allocation beyond CY2027).
- p.13 Non-GAAP Financial Results: three-quarter table (§1) with footnote "Excludes $0 million, $538 million and $1,938 million, respectively, for the periods presented related to NBM prepayments and deposits."
- p.14 Gross and Cash CapEx: §4 table.
- p.15 Fiscal First Quarter Guidance: identical to the release table (§5).
- p.16 Financial Outlook: six bullets (§5).
- p.17 Appendix divider. p.18 Joint Venture Operational Framework (§4). p.19–22 GAAP to non-GAAP reconciliations, three-quarter columns Q4'25 / Q3'26 / Q4'26 (p.19 also has a five-quarter gross-profit strip: Q4'25 $502, Q1'26 $691, Q2'26 $1,546, Q3'26 $4,666, Q4'26 $7,588). p.23–24 non-GAAP footnotes (same text as release). p.25 blank.
- Layout notes: p.7 chart values are not in the text layer (see §2); p.23–24 headings are duplicated by the extractor ("GAAP / GAAP to Non-GAAP Reconciliations / to Non-GAAP (cont'd)"); a few words carry stray spaces ("opera ting", "accountin g", "fore casted") from `pdftotext -layout`. Numbers were cross-checked against the release and match.

Q3 FY2026 deck (18 PDF pages, "SNDK Q3-26 Earnings Deck Final.pdf"; PDF title metadata reads "SNDK Q3-26 Earnings Deck Structure DRAFT WIP"; every page's text layer carries a stray template string "START" "REPEAT" "1988/2025" at top right, which is not content):
- p.3 Executive Summary: "Further expansion into the large, fast-growing Datacenter end market with our leading technology"; "Secured three New Business Model ("NBM") partnerships backed by firm financial guarantees, with an additional two NBMs in the current fiscal fourth quarter"; "Announced a $6B share repurchase program following full debt repayment"; financial results tiles "Revenue of $5.95B", "Non-GAAP Diluted Net Income per Share of $23.41", "Non-GAAP Gross Margin of 78.4%", "Adjusted Free Cash Flow of $2,955 million", "Cash and Cash Equivalents of $3.74 billion".
- p.4–5 Business Highlights (§6). p.6 Revenue Trends by End Market (text tiles only; bars unlabelled). p.7 Non-GAAP Financial Results Q3'25 / Q2'26 / Q3'26 (revenue $1,695 / $3,025 / $5,950; non-GAAP GM 22.7% / 51.1% / 78.4%; non-GAAP opex $383 / $413 / $448; non-GAAP operating income $2 / $1,133 / $4,218; non-GAAP interest and other $(22) / $(34) / $(3); non-GAAP EPS $(0.30) / $6.20 / $23.41; OCF $26 / $1,019 / $3,038; adjusted FCF $220 / $843 / $2,955). p.8 CapEx (§4). p.9 Q4 guidance (§6). p.10 JV framework. p.11 blank. p.12 Appendix. p.13–16 reconciliations (§8). p.17–18 footnotes.

## 10. Other statements in the release worth having

- "Additional details can be found within the Company's earnings presentation, which is accessible online at investor.sandisk.com." [Q4 FY2026 release, l.79]
- Basis of presentation: "On February 21, 2025, Sandisk Corporation (the "Company") completed its separation from Western Digital Corporation ("WDC") and became a standalone publicly traded company." Pre-separation periods "were prepared on a carve-out basis and were derived from WDC's consolidated financial statements". [l.101–103]
- "About Sandisk": "Sandisk is a leading global semiconductor memory company with more than 30 years of innovation in NAND flash technology. We are a vertically integrated solutions provider with ownership of chip-level design and IP, front and back-end manufacturing, as well as systems engineering and design. ... our broad and ever-expanding portfolio delivers powerful flash storage solutions for artificial intelligence workloads in datacenters, edge devices, and consumer applications. Our technologies enab[le] ... removable cards, universal serial bus drives, and wafers and components." [l.111]. The Q3 release's version described the company as "a leading developer, manufacturer and provider of data storage devices and solutions based on NAND flash technology ... for everyone from students, gamers and home offices, to the largest enterprises and public clouds" [Q3 FY2026 release, l.91] — the self-description changed between April and August (gatherer observation).
- Forward-looking statements list "the market leadership of the Company's technology; the contribution of the Company's datacenter business to growth generation and the expected benefits of its customer partnerships; and the Company's ability to create value for its customers through technology and generate growing and durable free cash flow" [l.117].
- Investor contact: Ivan Donaldson, ivan.donaldson@sandisk.com / investors@sandisk.com [l.388–393].

## 11. 2026 Investor Day (August 13, 2026; inside the as-of window)

Sources: `investor-day-2026-slides.txt` (98 PDF pages; sections: CEO David Goeckeler p.4–15; CTO Alper Ilkbahar "NAND Flash Technology Leadership" p.16–30; VP Market Intelligence Eric Cherrstrom "NAND Market Update" p.31–37; Chief Product Officer Khurram Ismail "AI Infrastructure Outlook" p.38–56; CFO Luis Visoso "Sustainable Value Creation" p.57–70; appendix reconciliations p.71–77; CTO "Next Wave of Technology Innovation" p.78–96; closing p.97) and `press-release-investor-day-2026.txt`. Chart-heavy pages (p.18–21, 32–36, 41, 50–51) extract with scrambled axis labels; numbers below are taken only where the text layer is unambiguous.

Long-term financial model, verbatim [2026 Investor Day slides, p.68] — "LONG-TERM SUSTAINABLE MODEL — FY 2028 Through FY 2030, Average Performance":

| Metric | Target |
|---|---|
| Revenue Growth Rate | Mid-to-High Teens |
| Non-GAAP Gross Margin | ~80% |
| Non-GAAP Operating Margin | ~75% |
| Adjusted Free Cash Flow Margin | ~50% |
| Capital Intensity (% of Revenue) | Mid-Single Digits % |

Note on the slide: "These target financial metrics are based on a variety of estimates and assumptions, are subject to risks and uncertainties and should not be relied upon as necessarily indicative of future results."

Release wording of the model [2026 Investor Day release, l.32]: "At the In Focus 2026 event, Sandisk introduced a comprehensive multi-year financial framework for fiscal year 2028 through fiscal year 2030. During this period, the Company expects revenue to grow mid-to-high teens, consistent with bit growth, and expects non-GAAP gross margins to sustain at approximately 80 percent with non-GAAP operating margins at approximately 75 percent. This assumes operating expenses as a percentage of revenue to be around five percent with no meaningful impact from other income and expense. Sandisk expects to deliver adjusted free cash flow margin at approximately 50 percent after accounting for taxes, capital expenses, and working capital to support growth."

CFO quote [2026 Investor Day release, l.34]: "As we unveil our new financial model for FY2028 through FY2030, we believe that we have a unique opportunity as we play in a large and fast-growing market with favorable tailwinds and that we are well positioned to capture the opportunity. We are optimizing for growth, sustainability and returns. As we do that, we expect to return 100 percent of excess cash to our shareholders after investing in the business. Our confidence in the sustainability of the model comes from our multi-year NBMs that are based on intimate relationships with our customers and grounded in innovation and collaboration."

CEO quote [2026 Investor Day release, l.18]: "Our strong performance today is the direct result of disciplined execution against the strategy we outlined 18 months ago," said David Goeckeler, Chairman and CEO, Sandisk. "We have built a differentiated position through decades of NAND flash innovation, deep systems-level expertise, a diversified portfolio, capital-efficient operations and management of the full technology stack. ..."

Other Investor Day KPIs and claims, verbatim unless noted:
- FY'26 summary (p.58): "TAM >3X Y/Y in CY'26, approaching $500B in CY'27"; "Datacenter becomes half of the market in CY'26, driven by AI"; "Sandisk full-year revenue of $20B, up 175% Y/Y"; "Annualized Q4 revenue of $36B, Datacenter end market at $12B"; "Full-year Non-GAAP gross margin of 71.6%, up from 30.3% in the prior year"; "Q4 Non-GAAP gross margin of 84.6%, Non-GAAP EPS $39.25, up from $0.29 in the prior year"; "Full-year Adjusted free cash flow of $8.7B, which excludes $2.5B of NBM pre-payments / deposits"; "Annualized Q4 Adjusted free cash flow of $20B".
- Three imperatives (p.8): "Increase Profitability", "Reduce Cyclicality", "Consistent Revenue Growth"; "MAXIMIZE RETURN ACROSS ALL TIME HORIZONS". p.9: "WE HOLD THE WHOLE STACK, WITH MINIMAL PROFITABILITY LEAKAGE — NAND IP → FRONT-END MANUFACTURING → SYSTEMS EXPERTISE → BACK-END MANUFACTURING → GTM"; "Proactive Supply Management". p.10 (Consumer): "Consumer Business as the Foundation — Inherently Less Cyclical"; "351K Points of Sale with a Global Customer Base"; "2.1B Products Sold Since 2017" (footnote: "Consumer products sold WW via Sandisk CY17-26 internal units sold"). p.13: "INVESTING TO GROW VOLUME MID-TO-HIGH TEENS PER YEAR". p.14: "27% CAGR" bit growth, "54% BiCS Gen-to-Gen Average Bit Growth Per Wafer" over "5 Nodes Over 9 Years" (BiCS5 → BiCS11); "GROWTH PRIMARILY DRIVEN BY INTELLECTUAL CAPITAL, NOT FINANCIAL CAPITAL".
- Invest in the business (p.6): "BiCS 9, 10, 11, 12, 13"; "High Bandwidth Flash (HBF)"; "3D Matrix Memory"; "CASH POSITIVE BALANCE SHEET — No Debt — Significant Cash Reserves". p.7 "NANYA INVESTMENT" (two-column layout; extracted bullets, order ambiguous): "JV Extended through 2034"; "Secure DRAM for eSSD Portfolio"; "~4% Equity Stake"; "R&D Scale (BiCS) Delivers Technology & Cost Leadership"; "JV is the Largest Producer of NAND Wafers in the World (33%)" (source: TechInsights NAND Market Report Q2 2026); "Foundational for NBMs".
- Technology (CTO): "19 GENERATIONS OF NAND FLASH" (p.18); BiCS8 = "218-Layer TLC & QLC, CBA Technology", improvements over BiCS6 TLC ">50% memory density, +60% interface bandwidth, +35% write bandwidth, +42% transfer power efficiency" (p.23); BiCS8 write "+62%" and read "+21%" performance per watt against peer average (p.24–25, "Sandisk estimates"); BiCS9 2Tb QLC = "Mature BiCS8 Cell Array" + "BiCS10-like CMOS", "Minimal CAPEX", write bandwidth "+150%", read "+75%", power efficiency write "+85%", read "+40%" vs BiCS8 2Tb QLC (p.26); BiCS10 "332-Layer 1Tb TLC, CBA Technology, Sampling in August 2026, Development Moving Ahead of Expectations", improvements over BiCS8 "+59% memory density, +33% interface bandwidth, +23% write & read bandwidth, +38% interface power efficiency" (p.27); BiCS10 "332-Layer 2Tb QLC ... World's Highest Density Memory Chip" (footnote: "As of August 13, 2026; based on QLC NAND"), "+60% memory density, +100% write & read bandwidth, +33% interface speed, +75% power efficiency" over BiCS8 (p.28); "+65% MORE DIE PER WAFER" BiCS10 332-layer 2Tb QLC vs BiCS8 218-layer 2Tb QLC (p.29). Capital intensity charts (p.20–21, source TrendForce 2026) compare Sandisk + Kioxia flash capex per incremental petabyte with the industry; the extracted labels cannot be attributed to series reliably.
- Market (p.32–37, "Sandisk Internal estimates" unless noted): "FLASH MARKET TO REACH 1.2ZB IN 2026"; "IN 2026 DATA CENTER OVERTAKES EDGE AS THE LARGEST FLASH SWIMLANE"; "HISTORICAL ~$60B AVERAGE +/- $20B CYCLES WITH CY26-27 DRIVEN BY DATA CENTER GROWTH"; "$300B+" CY26 and "Approaching $500B" CY27 industry revenue; "Flash was priced as a commodity: falling ASPs offset rising volumes, holding revenue growth to ~4%"; wafer capacity "Peaked in CY22 ... ~1,830 kwpm", "~70% Utilization Trough; ~500 kwpm Idle", "~560 kwpm Retired; now ~100% Utilized", "RE-ESTABLISHING CAPACITY ~30% BELOW PEAK" (p.34, with TechInsights); "U.S. DATA CENTER CAPEX KEEPS CLIMBING: 2026 TO $842B AND 2027 TO $1,097B" (p.35, Evercore ISI, "15 consecutive quarters of upward revisions"); Edge: "OEMs ARE SELLING FEWER UNITS AT HIGHER ASPs", "Low-end Mobile reduced by > 200Mu in CY 26", "Gartner posits sub-$500 PCs could be eliminated by 2028" (p.36); summary (p.37): "The revenue TAM inflects from a ~$60B historical average to >$300B+, approaching $500B by CY 27".
- AI infrastructure (p.40–56): "AI DC TAM 1.2ZB 2030 SHIPMENT EST." (TechInsights) split by workload (Fast Data Lakes / Staging / KV Cache; percentages 25% / 40% / 35% appear on the page but the extractor does not bind them to labels reliably) and by technology "34% TLC / 66% QLC" (Sandisk internal splits) (p.41, p.51); "Storage Was Necessary Commodity → Storage Is Strategic Component" (p.42); eSSD portfolio: TLC eSSD "PCIe Gen 5.0, NVMe 2.0", "E1.S, U.2, E3.S", "4TB, 8TB, 16TB, 32TB"; QLC eSSD "U.2, E3", "16TB, 32TB, 64TB, 128TB, 256TB"; "PCIe GEN6 DEMO @ FMS"; "UltraQLC Roadmap • up to 1PB" (p.53); lab claims "~75% Less Energy with SSD", "~3× Higher Throughput with SSD" ("Based on internal testing", p.54); "SSD is a Token Battery" (p.55).
- Next wave (p.78–96): 3D Matrix Memory "Delivered 300mm Wafers and Packaged Parts", "Demonstrated Multi-Gb Functional Memory Arrays", "Achieved Performance Approaching Product Specs" (p.81); HBF "Same read bandwidth as HBM with up to 8-16x capacity", "Architecture developed with inputs from major cloud/AI customers" (p.83); simulation "HBF Only vs HBM Only": "8× CAPEX EFFICIENCY for minimum configuration required to run model: 1 HBF GPU vs 8 HBM GPUs"; "2× GPU EFFICIENCY ... 4 HBF GPUs = 8 HBM GPUs" ("Based on internal testing"; model Qwen3-480B-A35B) (p.87–88); "2ND-GEN HBF TECHNOLOGY FOR THE EDGE ... Enabling 100B+ Models on Your Edge Device ... Actively being co-developed with multiple customers" (p.89); consortium milestones "AUG 2025 Sandisk & SK hynix Announcement; FEB 2026 HBF Technology Consortium Formed (under OCP); AUG 2026 First HBF Spec Released; 2027 Generational Spec Updates" (p.90); HBF Technical Advisory Board: David Patterson, Raja Koduri, and new member Jim Keller (CEO, Tenstorrent) (p.91–92); roadmap "FIRST HBF MEMORY DIE TAPED OUT" and "FIRST HBF INFERENCE PRODUCT SAMPLES ... 2027" (p.96).
- Closing (p.97): "NBMs have structurally reset our margin profile higher while reducing cyclicality"; "Structurally higher margins, combined with our industry-low capital intensity, drives tremendous free cash flow"; "Committed to a strong balance sheet and returning 100% of our excess cash back to shareholders"; "Compounding value for long-term investors by converting bit growth to free cash flow".
- The Investor Day release also states: "the total available market for enterprise data center flash growing to 1.2 zettabytes by 2030" [l.24]; "the new BiCS10 QLC node which achieves 60% increase in bit density compared to BiCS8" [l.22]; "Sandisk's new BiCS9 QLC technology ... combines a proven BiCS8 array with a BiCS10-based CMOS wafer" [l.22].
- No 8-K was filed for the Investor Day (SEC submissions JSON lists no 8-K between 2026-08-05 and the 10-K of 2026-08-17), so the release and deck exist only on the IR site.

## 12. Known gaps (items looked for and not found in the IR documents)

- Exabytes or petabytes shipped, bit growth % by quarter, and ASP per gigabyte: not disclosed (only the "one-third volumes / two-thirds pricing" sentence and the Datacenter bit-share 12% → 38%).
- End-market gross margin or operating income: not disclosed (only company-level margins).
- Q1 FY2026 revenue by end market: not in any cached IR document (derived in §2 as gatherer arithmetic).
- Datacenter revenue split (enterprise SSD vs other), share of datacenter revenue under NBMs, and enterprise SSD exabytes: not disclosed.
- Names of NBM customers; the $93.9B TCV by year or by customer; RPO by end market; the RPO at quarter-end excluding post-quarter deals is $59.8B but its composition is not given.
- Full-year FY2027 capex, cash capex, or Flash Ventures investment in dollars: not disclosed (only "approximately 6% of revenue for the full year" and "capital spending increases YoY", fiscal year unnamed).
- FY2027 full-year revenue, margin or EPS guidance: none (only Q1 FY2027).
- Q1 FY2027 GAAP EPS and GAAP tax: "N/A" in the guidance table.
- Q1 FY2027 interest and other income guidance: row dropped from the table.
- Shares repurchased (count) and average price paid in Q4'26: not disclosed; quarter-end shares outstanding printed as 149 million (see the anomaly in §4).
- Dividend: none exists or is discussed.
- Net cash, liquidity, or credit facility figures: not printed (gatherer arithmetic: cash 4,762, debt zero).
- Inventory days, receivable days: not printed.
- Explanation of the $1,777 marketable equity security, the $804 gain, or the counterparty: not in the release; the Investor Day "Nanya investment ~4% equity stake" page is the only candidate and is not linked to the balance-sheet line by any document.
- Explanation of the 32% sequential Consumer revenue decline: none in release or deck.
- Explanation of "Equity loss in investees, net of dividends received" of 102 in Q4'26 (12 in Q3'26): none.
- Reconciliation between the NBM Payments adjustment (1,938 / 2,476) and the refund-liability and contract-liability cash-flow lines (2,091 / 2,591): none.
- Why the printed shares outstanding rose from 148 to 149 million while $4.5 billion of stock was repurchased: not explained.
- The Q2'26 non-GAAP net income/EPS restatement ($967/$6.20 → $969/$6.21) and the split of "Other, net" into an equity-securities line: not explained.
- Whether Q1 FY2027 is a 13-week quarter, and any statement that FY2026 had 53 weeks: neither release says (searched "week", "53"). The runner's fixed facts state FY2026 was 53 weeks with a 14-week Q1.
- Headcount, geography of revenue, top-customer concentration, Kioxia JV financials (Flash Ventures revenue, capex in total): not in the IR documents; filings gatherer's scope.
- Transcript: not this gatherer's scope; `transcript.txt` and `transcript-FY2026-Q3.txt` exist in the folder from the transcript gatherer and were not read.
