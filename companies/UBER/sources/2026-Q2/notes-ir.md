# notes-ir — Uber Technologies, Inc. (UBER, CIK 0001543151) — Q2 2026 — IR gatherer

As-of quarter Q2 2026 (quarter ended June 30, 2026). As-of cutoff 2026-08-05 (release and call 2026-08-05). Prior quarter Q1 2026 (release May 6, 2026). Gatherer run 2026-09-08 behaving as though the date were 2026-08-05. Bullet facts only; every number verbatim with unit and period unless labelled "(computed)".

Source files (all in this folder) and tags:

- `press-release.txt` → `[Q2 2026 release, p.N]` — "Uber Announces Results for Second Quarter 2026", datelined "SAN FRANCISCO – August 5, 2026". 13 PDF pages; printed page numbers 1–13 = PDF pages.
- `supplemental-data.txt` → `[Q2 2026 supplemental, p.N]` — "Q2 2026 Earnings Supplemental Data", dated "August 5, 2026" on the cover. 31 PDF pages; printed page numbers 2–31 = PDF pages (cover unnumbered). Uber publishes no separate slide deck; this is the slides equivalent (the release itself calls it the "slide presentation").
- `press-release-2026-Q1.txt` → `[Q1 2026 release, p.N]` — "Uber Announces Results for First Quarter 2026", datelined "SAN FRANCISCO – May 6, 2026". 12 PDF pages; printed page numbers 1–12 = PDF pages.
- `delivery-hero-press-release.txt` → `[Delivery Hero release, p.N]` — "Uber Announces Acquisition Offer for Delivery Hero", datelined "SAN FRANCISCO – July 16, 2026". 7 PDF pages; NO printed page numbers, so page tags are PDF pages.
- `delivery-hero-presentation.txt` → `[Delivery Hero presentation, p.N]` — "Announcement of Uber's Acquisition of Delivery Hero", dated "July 16, 2026" on the cover. 16 PDF pages; printed page numbers 2–14 and 16 = PDF pages; p.1 (cover) unnumbered; p.15 is image-only with no text layer.

All dollar figures are US$; tables in the releases and deck are "In millions" except share counts (thousands) and per-share amounts, unless a bullet says otherwise.

## 0. Supplemental deck, page by page (what yielded text, what is a chart)

Every one of the 31 pages has a text layer (per-page `pdftotext -layout` word yields: 11 / 422 / 318 / 19 / 63 / 60 / 65 / 70 / 19 / 152 / 134 / 103 / 147 / 100 / 19 / 137 / 137 / 82 / 19 / 243 / 111 / 142 / 177 / 266 / 19 / 144 / 141 / 194 / 150 / 176 / 117). Raster images (from `pdfimages -list`) sit only on p.1 (cover photo), p.5–8 (highlight slides: 17 / 59 / 55 / 56 images each, logos and photos) and small legend/icon strips on p.13, 16, 17, 18.

- p.1 cover; p.2 non-GAAP disclosure; p.3 forward-looking statements; p.4, 9, 15, 19, 25 section dividers (same five section titles repeated).
- p.5–8 "Platform and Business Highlights": text headlines and a few numeric callouts; partner names/brands are logos (images) and did not survive. Details in §7.
- p.10–14 "Financial and Operational Highlights": vector bar charts, five quarters Q2 2025 … Q2 2026. All data labels are real text but come out in scrambled visual order in `-layout` mode. **Re-association method:** `pdftotext -bbox` word coordinates; the five quarter columns sit at x ≈ 105–360 (Q2 2025), 320–550 (Q3 2025), 540–720 (Q4 2025), 750–890 (Q1 2026), 965–1075 (Q2 2026) on the 1920-pt-wide page, and each label was assigned to the column whose x-range contains it. Growth-rate rows under each chart are already in left-to-right order in the text. **Cross-check:** every re-associated dollar value on p.10–14 and p.16–18 also appears in the tabular pages p.20–31 for the same quarter, and every re-associated margin label equals the value computed from those tables rounded to one decimal (listed in §3d). Where a chart page carries a number that no table confirms (Q3 2025 and Q4 2025 Freight margins), the bullet says "x-position only".
- p.16–18 "Segment Details": same chart style, same method, same x-columns (Mobility, Delivery, Freight).
- p.20–24 condensed consolidated statements (income statement, balance sheet in two pages, cash flow in two pages): clean tables, but on p.20, 21 and 23 a few rows were split so that the four values print on separate lines under the row label (e.g. "Depreciation and amortization / Total costs and expenses" then "175 / $11,201 / 188 / $12,301 / 346 / $21,506 / 372 / $23,581"). Values are identical to the release; the release's version is used in §2.
- p.26–31 non-GAAP reconciliations: clean five-quarter tables (Jun 30 '25, Sept 30 '25, Dec 31 '25, Mar 31 '26, Jun 30 '26). These are the only source for Q3 2025 and Q4 2025 figures in these notes. One layout artefact: p.24 prints "(3529)" without the thousands comma for six-month repurchases (release: "(3,529)").
- No chart page's labels were guessed. Nothing on any page is a scanned image of a table.

## 1. Headline results, Q2 2026 (release wording)

- Headline lines: "Gross Bookings grew 22% year-over-year on a constant currency basis; Trips grew 18% year-over-year"; "GAAP Income from operations of $1.9 billion; Non-GAAP Operating Income of $2.1 billion, up 40% year-over-year"; "GAAP Diluted EPS of $1.17; Non-GAAP EPS of $0.81, up 35% year-over-year". [Q2 2026 release, p.1]
- Trips: "Trips during the quarter grew 18% year-over-year ("YoY") to 3.9 billion, driven by Monthly Active Platform Consumers ("MAPCs") growth of 16% YoY and monthly Trips per MAPC growth of 2% YoY." Table: Trips 3,268 (Q2 2025) → 3,867 (Q2 2026), 18%. [Q2 2026 release, p.1–2]
- MAPCs: 180 (Q2 2025) → 208 (Q2 2026), 16%. [Q2 2026 release, p.2]
- Monthly Trips per MAPC: 6.2 (Q2 2026), +2% YoY; 6.1 (Q2 2025). [Q2 2026 supplemental, p.10; re-associated by x-position]
- Gross Bookings: "Gross Bookings grew 24% YoY to $58.0 billion, and 22% on a constant currency basis." Table: $46,756 → $58,022, 24%, 22% constant currency. [Q2 2026 release, p.1–2]
- Gross Bookings by segment, Q2 2025 → Q2 2026, % change, constant-currency % change: Mobility $23,762 → $28,988, 22%, 20%; Delivery 21,734 → 27,463, 26%, 25%; Freight 1,260 → 1,571, 25%, 25%; Total $46,756 → $58,022, 24%, 22%. [Q2 2026 release, p.2]
- Revenue: "Revenue grew 12% YoY to $14.2 billion, or 11% on a constant currency basis. Business model changes negatively impacted total revenue YoY growth by 8 percentage points on a reported and constant currency basis." Table: $12,651 → $14,191, 12%, 11%. [Q2 2026 release, p.1–2]
- Revenue by segment, Q2 2025 → Q2 2026, % change, constant-currency % change: Mobility $7,288 → $7,363, 1%, 0%; Delivery 4,102 → 5,245, 28%, 26%; Freight 1,261 → 1,583, 26%, 25%; Total $12,651 → $14,191, 12%, 11%. [Q2 2026 release, p.2]
- GAAP Income from operations: "grew 30% YoY to $1.9 billion"; table $1,450 → $1,890, 30%. [Q2 2026 release, p.1–2]
- GAAP Net income: "GAAP Net income attributable to Uber Technologies, Inc. was $2.4 billion, which includes a $1.6 billion net benefit (pre-tax) from revaluations of Uber's equity investments. GAAP Diluted earnings per share ("EPS") was $1.17." Table: $1,355 → $2,394, 77%; GAAP Diluted EPS $0.63 → $1.17, 85%. Footnote (2): "Q2 2025 net income includes a $17 million net headwind (pre-tax) from revaluations of Uber's equity investments. Q2 2026 net income includes a $1.6 billion net benefit (pre-tax) from revaluations of Uber's equity investments." [Q2 2026 release, p.1–2]
- Adjusted EBITDA: "Adjusted EBITDA grew 33% YoY to $2.8 billion. Adjusted EBITDA margin as a percentage of Gross Bookings was 4.9%, up from 4.5% in Q2 2025." Table: $2,119 → $2,819, 33%. [Q2 2026 release, p.1–2]
- Adjusted EBITDA by segment: NOT disclosed in the Q2 2026 release or deck. The release presents "Segment Operating Income (Loss)" instead (see §3) and states "Adjusted EBITDA is no longer a key measure used by management; we include a disclosure on Adjusted EBITDA to assist during the transition to our new non-GAAP measures." [Q2 2026 release, p.9]
- Non-GAAP Operating Income: "Non-GAAP Operating Income grew 40% YoY to $2.1 billion. Non-GAAP Operating Income as a percentage of Gross Bookings was 3.7%, up from 3.3% in Q2 2025." Table: $1,534 → $2,143, 40%. [Q2 2026 release, p.1–2]
- Non-GAAP Net Income and EPS: "Non-GAAP Net Income grew 29% YoY to $1.7 billion and Non-GAAP EPS grew 35% YoY to $0.81." Table: Non-GAAP Net Income $1,280 → $1,652, 29%; Non-GAAP EPS $0.60 → $0.81, 35%. [Q2 2026 release, p.1–2]
- Cash flow: "Net cash provided by operating activities was $2.9 billion and free cash flow, defined as net cash flows from operating activities less capital expenditures, was $2.8 billion." Table: operating cash flow $2,564 → $2,862, 12%; free cash flow $2,475 → $2,792, 13%. Capex ("Purchases of property and equipment") (89) → (70). [Q2 2026 release, p.1–2, p.13]
- Trailing-twelve-month free cash flow: CFO quote "trailing twelve-month free cash flow exceeded $10 billion for the first time in Uber's history" [Q2 2026 release, p.1]; TTM ended Jun 30 '26: net cash provided by operating activities 10,424, purchases of property and equipment (308), Free Cash Flow $10,116 [Q2 2026 supplemental, p.31].
- Cash: "Unrestricted cash, cash equivalents, and short-term investments were $5.4 billion at the end of the second quarter." [Q2 2026 release, p.1] Balance sheet at June 30, 2026: Cash and cash equivalents $4,870; Short-term investments 521. [Q2 2026 release, p.6]
- Debt at June 30, 2026: Short-term debt 1,997 (December 31, 2025: —); Long-term debt, net of current portion 10,726 (December 31, 2025: 10,521). [Q2 2026 release, p.6] Cash-flow lines, three months ended June 30, 2026: "Proceeds from term loan, notes, and credit facility, net of issuance costs" 3,997; "Principal repayment on term loan, notes, and credit facility" (2,000). [Q2 2026 release, p.8] No narrative on the borrowing appears in the release or deck.
- Share repurchases: "Repurchases of common stock" (518) for the three months and (3,529) for the six months ended June 30, 2026 (Q2 2025: (1,363); six months 2025: (3,148)). [Q2 2026 release, p.8] Remaining repurchase authorization: not stated in the release or deck.
- Diluted weighted-average shares (thousands): 2,125,628 (Q2 2025) → 2,050,225 (Q2 2026); six months 2,124,181 → 2,060,763. Basic: 2,091,106 → 2,036,458; six months 2,091,781 → 2,044,279. [Q2 2026 release, p.7] YoY change in diluted shares (computed): −75,403 thousand, −3.5%; six-month (computed): −63,418 thousand, −3.0%.
- CEO quote: "Uber's platform advantage continues to compound: record consumers and engagement, and profitable growth across our business … In fact, we've added more first-time users over the past twelve months than in any period over the past five years. We're investing from a position of strength, as we accelerate our cross-platform strategy at a global scale and build the world's largest platform for autonomous vehicles." [Q2 2026 release, p.1]
- CFO quote: "We continue to convert strong top-line growth into faster earnings and significant cash generation … Gross Bookings grew 22%, Non-GAAP EPS grew 35%, and trailing twelve-month free cash flow exceeded $10 billion for the first time in Uber's history—giving us the flexibility to both invest for the future and pursue strategic opportunities, while continuing to reduce our share count." [Q2 2026 release, p.1]
- Tax rates, three months ended June 30 (2025, 2026): GAAP effective tax rate 9%, 26%; Total adjustments to GAAP provision for income taxes 12%, (2)%; Non-GAAP effective tax rate 21%, 24%. Six months: GAAP (9)%, 27%; adjustments 31%, (3)%; Non-GAAP 22%, 24%. [Q2 2026 release, p.10]
- "About Uber": "More than 79 billion trips later" (Q1 2026 release: "More than 75 billion trips later"). [Q2 2026 release, p.4; Q1 2026 release, p.4]

## 2. Full financial statements printed in the release

### 2a. Condensed consolidated statements of operations (In millions, except share amounts in thousands, and per share amounts; unaudited) — columns: 3M Jun 30 2025 | 3M Jun 30 2026 | 6M Jun 30 2025 | 6M Jun 30 2026 [Q2 2026 release, p.7]

| Line | Q2 2025 | Q2 2026 | 6M 2025 | 6M 2026 |
|---|---|---|---|---|
| Revenue | 12,651 | 14,191 | 24,184 | 27,394 |
| Cost of revenue, exclusive of depreciation and amortization shown separately below | 7,611 | 7,815 | 14,548 | 15,073 |
| Operations and support | 696 | 805 | 1,364 | 1,568 |
| Sales and marketing | 1,210 | 1,515 | 2,267 | 2,841 |
| Research and development | 840 | 1,043 | 1,655 | 1,994 |
| General and administrative | 669 | 935 | 1,326 | 1,733 |
| Depreciation and amortization | 175 | 188 | 346 | 372 |
| Total costs and expenses | 11,201 | 12,301 | 21,506 | 23,581 |
| Income from operations | 1,450 | 1,890 | 2,678 | 3,813 |
| Interest expense | (108) | (127) | (213) | (235) |
| Interest income | 181 | 172 | 350 | 347 |
| Other income (expense), net | (19) | 1,342 | 74 | (152) |
| Income before income taxes and loss from equity method investments | 1,504 | 3,277 | 2,889 | 3,773 |
| Provision for (benefit from) income taxes | 142 | 840 | (260) | 1,034 |
| Loss from equity method investments | (12) | (21) | (25) | (41) |
| Net income including non-controlling interests | 1,350 | 2,416 | 3,124 | 2,698 |
| Less: net income (loss) attributable to non-controlling interests, net of tax | (5) | 22 | (7) | 41 |
| Net income attributable to Uber Technologies, Inc. | 1,355 | 2,394 | 3,131 | 2,657 |
| Net income per share, basic ($) | 0.65 | 1.18 | 1.50 | 1.30 |
| Net income per share, diluted ($) | 0.63 | 1.17 | 1.46 | 1.29 |
| Weighted-average shares, basic (thousands) | 2,091,106 | 2,036,458 | 2,091,781 | 2,044,279 |
| Weighted-average shares, diluted (thousands) | 2,125,628 | 2,050,225 | 2,124,181 | 2,060,763 |

### 2b. Condensed consolidated balance sheets (In millions; unaudited) — As of December 31, 2025 | As of June 30, 2026 [Q2 2026 release, p.6]

| Line | Dec 31, 2025 | Jun 30, 2026 |
|---|---|---|
| Cash and cash equivalents | 7,105 | 4,870 |
| Short-term investments | 528 | 521 |
| Restricted cash and cash equivalents (current) | 631 | 661 |
| Accounts receivable, net | 3,827 | 4,298 |
| Prepaid expenses and other current assets | 1,902 | 2,179 |
| Total current assets | 13,993 | 12,529 |
| Restricted cash and cash equivalents (non-current) | 1,911 | 1,646 |
| Restricted investments | 8,874 | 9,486 |
| Investments | 9,178 | 8,759 |
| Equity method investments | 287 | 3,773 |
| Property and equipment, net | 1,897 | 1,809 |
| Operating lease right-of-use assets | 1,114 | 1,558 |
| Intangible assets, net | 1,048 | 1,132 |
| Goodwill | 8,931 | 9,472 |
| Deferred tax assets | 10,951 | 10,162 |
| Other non-current assets | 3,618 | 5,475 |
| Total assets | 61,802 | 65,801 |
| Accounts payable | 1,013 | 1,366 |
| Short-term insurance reserves | 3,387 | 3,758 |
| Operating lease liabilities, current | 169 | 178 |
| Short-term debt | — | 1,997 |
| Accrued and other current liabilities | 7,751 | 7,572 |
| Total current liabilities | 12,320 | 14,871 |
| Long-term insurance reserves | 9,076 | 9,528 |
| Long-term debt, net of current portion | 10,521 | 10,726 |
| Operating lease liabilities, non-current | 1,390 | 1,830 |
| Other non-current liabilities | 412 | 447 |
| Total liabilities | 33,719 | 37,402 |
| Redeemable non-controlling interests | 165 | 180 |
| Common stock | — | — |
| Additional paid-in capital | 38,101 | 35,698 |
| Accumulated other comprehensive loss | (432) | (432) |
| Accumulated deficit | (10,628) | (7,950) |
| Total Uber Technologies, Inc. stockholders' equity | 27,041 | 27,316 |
| Non-redeemable non-controlling interests | 877 | 903 |
| Total equity | 27,918 | 28,219 |
| Total liabilities, redeemable non-controlling interests and equity | 61,802 | 65,801 |

- Equity method investments rose from 287 to 3,773 and "Purchase of total return swaps" (1,640) appears as a new investing line (see 2c); the release gives no narrative for either. [Q2 2026 release, p.6, p.8]

### 2c. Condensed consolidated statements of cash flows (In millions; unaudited) — 3M 2025 | 3M 2026 | 6M 2025 | 6M 2026 [Q2 2026 release, p.8–9]

| Line | Q2 2025 | Q2 2026 | 6M 2025 | 6M 2026 |
|---|---|---|---|---|
| Net income including non-controlling interests | 1,350 | 2,416 | 3,124 | 2,698 |
| Depreciation and amortization | 181 | 195 | 359 | 386 |
| Stock-based compensation | 475 | 550 | 910 | 1,023 |
| Deferred income taxes | 87 | 665 | (325) | 771 |
| (Gains) losses on debt and equity securities, net | 17 | (1,612) | (34) | (138) |
| (Gains) losses on foreign currency transactions, net | (101) | (58) | (152) | (53) |
| Other | 106 | 296 | 79 | 316 |
| Accounts receivable | (212) | (425) | (335) | (499) |
| Prepaid expenses and other assets | (251) | (163) | (748) | (375) |
| Operating lease right-of-use assets | 46 | 38 | 89 | 100 |
| Accounts payable | 125 | 161 | 131 | 345 |
| Accrued insurance reserves | 812 | 387 | 1,487 | 830 |
| Accrued expenses and other liabilities | (20) | 447 | 410 | (94) |
| Operating lease liabilities | (51) | (35) | (107) | (97) |
| Net cash provided by operating activities | 2,564 | 2,862 | 4,888 | 5,213 |
| Purchases of property and equipment | (89) | (70) | (163) | (135) |
| Purchases of non-marketable equity securities | (12) | (175) | (191) | (507) |
| Purchases of marketable securities | (5,095) | (10,887) | (7,635) | (17,646) |
| Purchases of notes receivable | — | (111) | — | (298) |
| Proceeds from maturities and sales of marketable securities | 4,636 | 8,119 | 7,033 | 14,665 |
| Acquisition of businesses, net of cash acquired | (804) | (647) | (804) | (653) |
| Purchase of total return swaps | — | (1,640) | — | (1,640) |
| Other investing activities | (97) | 22 | (243) | 52 |
| Net cash used in investing activities | (1,461) | (5,389) | (2,003) | (6,162) |
| Proceeds from term loan, notes, and credit facility, net of issuance costs | 1,127 | 3,997 | 1,127 | 3,997 |
| Principal repayment on term loan, notes, and credit facility | — | (2,000) | — | (2,000) |
| Principal payments on finance leases | (28) | (42) | (75) | (82) |
| Proceeds from the issuance of common stock under the Employee Stock Purchase Plan | 120 | 136 | 120 | 136 |
| Repurchases of common stock | (1,363) | (518) | (3,148) | (3,529) |
| Other financing activities | (51) | (33) | (81) | (73) |
| Net cash provided by (used in) financing activities | (195) | 1,540 | (2,057) | (1,551) |
| Effect of exchange rate changes on cash and cash equivalents, and restricted cash and cash equivalents | 159 | 54 | 229 | 30 |
| Net increase (decrease) in cash and cash equivalents, and restricted cash and cash equivalents | 1,067 | (933) | 1,057 | (2,470) |
| Cash and cash equivalents, and restricted cash and cash equivalents, beginning of period | 8,600 | 8,110 | 8,610 | 9,647 |
| Cash and cash equivalents, and restricted cash and cash equivalents, end of period | 9,667 | 7,177 | 9,667 | 7,177 |

## 3. Segment tables (five quarters where available)

### 3a. Gross Bookings by segment ($ millions)

| Segment | Q2 2025 | Q3 2025 | Q4 2025 | Q1 2026 | Q2 2026 | Source |
|---|---|---|---|---|---|---|
| Mobility | 23,762 | 25,111 | 27,442 | 26,394 | 28,988 | Q2 2025/Q2 2026: [Q2 2026 release, p.2]; Q1 2026: [Q1 2026 release, p.2]; Q3/Q4 2025: [Q2 2026 supplemental, p.16], re-associated by x-position |
| Delivery | 21,734 | 23,322 | 25,431 | 25,992 | 27,463 | same pattern; Q3/Q4 2025: [Q2 2026 supplemental, p.17] |
| Freight | 1,260 | not disclosed | not disclosed | 1,334 | 1,571 | [Q2 2026 release, p.2]; [Q1 2026 release, p.2]; the Freight deck page (p.18) shows revenue and operating income only |
| Total | 46,756 | 49,740 | 54,140 | 53,720 | 58,022 | [Q2 2026 release, p.2]; [Q1 2026 release, p.2]; Q3/Q4 2025: [Q2 2026 supplemental, p.11], re-associated by x-position |

- Total Gross Bookings % growth YoY, Q2 2025 … Q2 2026: 17%, 21%, 22%, 25%, 24%; constant-currency: 18%, 21%, 22%, 21%, 22%. [Q2 2026 supplemental, p.11; rows in left-to-right order]
- Mobility Gross Bookings constant-currency growth YoY, Q2 2025 … Q2 2026: 18%, 19%, 19%, 20%, 20%. [Q2 2026 supplemental, p.16]
- Delivery Gross Bookings constant-currency growth YoY: 20%, 24%, 26%, 23%, 25%. [Q2 2026 supplemental, p.17]

### 3b. Revenue by segment ($ millions)

| Segment | Q2 2025 | Q3 2025 | Q4 2025 | Q1 2026 | Q2 2026 |
|---|---|---|---|---|---|
| Mobility | 7,288 | 7,682 | 8,204 | 6,798 | 7,363 |
| Delivery | 4,102 | 4,477 | 4,892 | 5,068 | 5,245 |
| Freight | 1,261 | 1,308 | 1,270 | 1,337 | 1,583 |
| Total | 12,651 | 13,467 | 14,366 | 13,203 | 14,191 |

Sources: Q2 2025 and Q2 2026 [Q2 2026 release, p.2]; Q1 2026 [Q1 2026 release, p.2]; totals for all five quarters [Q2 2026 supplemental, p.29, table]; Q3 2025 and Q4 2025 segment values [Q2 2026 supplemental, p.16–18, re-associated by x-position; segment values sum to the p.29 totals: 7,682+4,477+1,308 = 13,467 and 8,204+4,892+1,270 = 14,366 (computed check)].

- Revenue % growth YoY (total), Q2 2025 … Q2 2026: 18%, 20%, 20%, 14%, 12%; constant currency 18%, 19%, 19%, 10%, 11%. [Q2 2026 supplemental, p.12] Note 2 on that page: "Business model changes negatively impacted Q2 2026 revenue YoY growth by 8 percentage points on a reported and constant currency basis."
- Mobility revenue constant-currency growth YoY: 18%, 18%, 18%, 1%, 0%. Delivery: 23%, 27%, 29%, 28%, 26%. Freight: (1%), 0%, (1%), 6%, 25%. [Q2 2026 supplemental, p.16, 17, 18]
- Q1 2026 release wording on the same effect: "Business model changes negatively impacted total revenue YoY growth by 9 percentage points, or 8 percentage points on a constant currency basis." [Q1 2026 release, p.1]

### 3c. Segment Operating Income (Loss) and Non-GAAP Operating Income ($ millions) [Q2 2026 supplemental, p.26, table; Q2 2025/Q2 2026 also Q2 2026 release, p.3; Q1 2026 also Q1 2026 release, p.3]

| Line | Jun 30 '25 | Sept 30 '25 | Dec 31 '25 | Mar 31 '26 | Jun 30 '26 |
|---|---|---|---|---|---|
| Mobility | 1,729 | 1,864 | 2,027 | 2,029 | 2,215 |
| Delivery | 766 | 811 | 905 | 961 | 1,055 |
| Freight | (26) | (40) | (18) | (30) | (24) |
| Corporate G&A and Platform R&D | (935) | (960) | (996) | (1,077) | (1,103) |
| Non-GAAP Operating Income | 1,534 | 1,675 | 1,918 | 1,883 | 2,143 |

- Release % change Q2 2025 → Q2 2026: Mobility 28%; Delivery 38%; Freight 8%; Corporate G&A and Platform R&D (18)%; Non-GAAP Operating Income 40%. [Q2 2026 release, p.3]
- Release footnote (1): "Includes costs that are not directly attributable to our reportable segments. Corporate G&A also includes certain shared costs such as finance, accounting, tax, human resources, information technology and legal costs. Platform R&D also includes mapping and payment technologies and support and development of the internal technology infrastructure. Our allocation methodology is periodically evaluated and may change." [Q2 2026 release, p.3]
- Segment Operating Income % reported growth YoY, Q2 2025 … Q2 2026: Mobility 24%, 23%, 26%, 28%, 28%; Delivery 49%, 49%, 42%, 43%, 38%. [Q2 2026 supplemental, p.16–17]

### 3d. Revenue Margin and margins as % of Gross Bookings (deck chart labels, re-associated by x-position; each checked against the tables)

- Definition: "Revenue Margin is defined as Revenue as a percentage of Gross Bookings." [Q2 2026 supplemental, p.16–17, Note 1] "We define Non-GAAP Operating Income margin as a percentage of Gross Bookings as Non-GAAP Operating Income divided by Gross Bookings." [Q2 2026 supplemental, p.13, Note 2] The release and deck never use the phrase "take rate".

| Metric (% of segment or total Gross Bookings) | Q2 2025 | Q3 2025 | Q4 2025 | Q1 2026 | Q2 2026 | Source page |
|---|---|---|---|---|---|---|
| Mobility Revenue Margin | 30.7% | 30.6% | 29.9% | 25.8% | 25.4% | p.16 |
| Delivery Revenue Margin | 18.9% | 19.2% | 19.2% | 19.5% | 19.1% | p.17 |
| Mobility Segment Operating Income margin | 7.3% | 7.4% | 7.4% | 7.7% | 7.6% | p.16 |
| Delivery Segment Operating Income margin | 3.5% | 3.5% | 3.6% | 3.7% | 3.8% | p.17 |
| Freight Segment Operating Income margin | (2.1%) | (3.1%) | (1.4%) | (2.2%) | (1.5%) | p.18 |
| Non-GAAP Operating Income as % of Gross Bookings | 3.3% | 3.4% | 3.5% | 3.5% | 3.7% | p.13 |

- Cross-check (computed from §3a–3c): Mobility revenue/GB 30.67%, 30.59%, 29.90%, 25.76%, 25.40%; Delivery 18.87%, 19.20%, 19.24%, 19.50%, 19.10%; Mobility SOI/GB 7.28%, 7.42%, 7.39%, 7.69%, 7.64%; Delivery SOI/GB 3.52%, 3.48%, 3.56%, 3.70%, 3.84%; Non-GAAP OI/GB 3.28%, 3.37%, 3.54%, 3.51%, 3.69%; Freight SOI/GB (2.06%) Q2 2025, (2.25%) Q1 2026, (1.53%) Q2 2026. All round to the labels above. Freight Q3 2025 (3.1%) and Q4 2025 (1.4%) rest on x-position only (no Freight Gross Bookings for those quarters in these sources).
- Adjusted EBITDA margin as % of Gross Bookings, stated by the releases: 4.9% (Q2 2026), 4.5% (Q2 2025) [Q2 2026 release, p.1]; 4.6% (Q1 2026), 4.4% (Q1 2025) [Q1 2026 release, p.1]. Not charted in the deck.
- Non-GAAP Operating Income as % of Gross Bookings, stated by the releases: 3.7% (Q2 2026), 3.3% (Q2 2025) [Q2 2026 release, p.1]; 3.5% (Q1 2026), 3.1% (Q1 2025) [Q1 2026 release, p.1].

### 3e. Operating metrics, five quarters [Q2 2026 supplemental, p.10; values re-associated by x-position; growth rows in order]

| Metric | Q2 2025 | Q3 2025 | Q4 2025 | Q1 2026 | Q2 2026 |
|---|---|---|---|---|---|
| MAPCs (millions) | 180 | 189 | 202 | 199 | 208 |
| MAPCs growth YoY | 15% | 17% | 18% | 17% | 16% |
| Monthly Trips / MAPC | 6.1 | 6.2 | 6.2 | 6.1 | 6.2 |
| Frequency growth YoY | 2% | 4% | 3% | 3% | 2% |
| Trips (millions) | 3,268 | 3,512 | 3,751 | 3,643 | 3,867 |
| Trips growth YoY | 18% | 22% | 22% | 20% | 18% |

- Check: Q2 2025 180 and 3,268, Q1 2026 199 and 3,643, Q2 2026 208 and 3,867 match the releases [Q2 2026 release, p.2; Q1 2026 release, p.2]. Monthly Trips/MAPC computed as Trips ÷ 3 ÷ MAPCs: 6.05, 6.10, 6.20 for Q2 2025, Q1 2026, Q2 2026 (computed; consistent with labels).
- Deck Note 3: "We define Frequency as Monthly Trips divided by MAPCs for a given period." [Q2 2026 supplemental, p.10]

### 3f. Non-GAAP EPS, five quarters [Q2 2026 supplemental, p.14 chart and p.27 table]

- Non-GAAP EPS: $0.60, $0.65, $0.71, $0.72, $0.81 (Q2 2025 … Q2 2026); % growth YoY 48%, 28%, 27%, 44%, 35%. GAAP Diluted EPS: $0.63, $3.11, $0.14, $0.13, $1.17. Non-GAAP Operating Income % growth YoY: 50%, 46%, 46%, 42%, 40% [p.13].

## 4. Definitions, verbatim [Q2 2026 release, p.9–11; identical wording in Q1 2026 release, p.8–11]

- Driver(s): "The term Driver collectively refers to independent providers of ride or delivery services who use our platform to provide Mobility or Delivery services, or both."
- Gross Bookings: "We define Gross Bookings as the total dollar value, including any applicable taxes, tolls, and fees, of: Mobility rides, Delivery orders (in each case without any adjustment for consumer discounts and refunds, Driver and Merchant earnings, and Driver incentives) and Freight revenue. Gross Bookings do not include tips earned by Drivers. Gross Bookings are an indication of the scale of our current platform, which ultimately impacts revenue."
- MAPCs: "We define MAPCs as the number of unique consumers who completed a Mobility ride or received a Delivery order on our platform at least once in a given month, averaged over each month in the quarter. While a unique consumer can use multiple product offerings on our platform in a given month, that unique consumer is counted as only one MAPC."
- Segment Operating Income (Loss): "We define each segment's Operating Income (Loss) as segment revenue less direct costs and expenses of that segment as well as any applicable exclusions from Non-GAAP Operating Income."
- Trips: "We define Trips as the number of completed consumer Mobility rides and Delivery orders in a given period. For example, an UberX Share ride with three paying consumers represents three unique Trips, whereas an UberX ride with three passengers represents one Trip. We believe that Trips are a useful metric to measure the scale and usage of our platform."
- Status of Adjusted EBITDA: "In addition to revenue, net income (loss), income (loss) from operations, and other results under GAAP, we use: Non-GAAP Operating Income; Non-GAAP Net Income; Non-GAAP EPS; Free cash flow; as well as, revenue growth rates in constant currency, which are described below, to evaluate our business. Adjusted EBITDA is no longer a key measure used by management; we include a disclosure on Adjusted EBITDA to assist during the transition to our new non-GAAP measures." [Q2 2026 release, p.9]
- Non-GAAP Operating Income: "We define Non-GAAP Operating Income as income from operations, excluding (i) amortization of acquired intangible assets, (ii) certain legal, non-income tax, and regulatory reserve changes and settlements, (iii) goodwill and asset impairments/loss on sale of assets, (iv) acquisition, financing and divestitures related expenses, (v) restructuring and related charges, and (vi) other items not indicative of our ongoing operating performance." [p.9]
- Non-GAAP Net Income: "Our Non-GAAP Net Income excludes the adjustments that are excluded from Non-GAAP Operating Income, as well as certain components below income from operations, such as certain items that are not indicative of our recurring core business operating results and certain income tax effects." Sub-items: Other income (expense), net ("Primarily includes items not indicative of our ongoing operating performance … These items include, but are not limited to: foreign currency exchange gain (losses), net, and unrealized (gain) loss on debt and equity securities, net."); Income tax effects; Adjustment to redeemable non-controlling interests ("Primarily reflects changes in the carrying value of redeemable non-controlling interests that are subject to put or call arrangements not solely within our control, which are remeasured to their estimated redemption value on a quarterly basis. These adjustments are non-cash in nature and are not indicative of our ongoing operating performance."). [p.10]
- Non-GAAP EPS: "We define Non-GAAP EPS as Non-GAAP Net Income attributable to common stockholders divided by Non-GAAP weighted-average shares outstanding. Adjustments to GAAP diluted weighted-average shares outstanding are for any potentially dilutive outstanding securities in periods where Non-GAAP Net Income is positive, but GAAP Net income was in a loss position." [p.10]
- Adjusted EBITDA: "We define Adjusted EBITDA as net income (loss), excluding (i) income (loss) from discontinued operations, net of income taxes, (ii) net income (loss) attributable to non-controlling interests, net of tax, (iii) provision for (benefit from) income taxes, (iv) income (loss) from equity method investments, (v) interest expense, (vi) interest income, (vii) other income (expense), net, (viii) depreciation and amortization, (ix) stock-based compensation expense, (x) certain legal, non-income tax, and regulatory reserve changes and settlements, (xi) goodwill and asset impairments/loss on sale of assets, (xii) acquisition, financing and divestitures related expenses, (xiii) restructuring and related charges and (xiv) other items not indicative of our ongoing operating performance." [p.11]
- Legal, non-income tax, and regulatory reserve changes and settlements (excluded from both measures): "primarily related to certain significant legal proceedings or governmental investigations related to worker classification definitions, or tax agencies challenging our non-income tax positions. These matters have limited precedent, cover extended historical periods and are unpredictable in both magnitude and timing, therefore are distinct from normal, recurring legal, non-income tax and regulatory matters and related expenses incurred in our ongoing operating performance." [p.9–10, p.11]
- Constant Currency: "We compare the percent change in our current period results from the corresponding prior period using constant currency disclosure. We present constant currency growth rate information to provide a framework for assessing how our underlying revenue performed excluding the effect of foreign currency rate fluctuations. We calculate constant currency by translating our current period financial results using the corresponding prior period's monthly exchange rates for our transacted currencies other than the U.S. dollar." [p.11]
- Free Cash Flow: "We define free cash flow as net cash flows from operating activities less capital expenditures." [p.11]
- Guidance reconciliation caveat: "In regards to forward looking non-GAAP guidance, we are not able to reconcile the forward-looking Non-GAAP EPS and Adjusted EBITDA measures to the closest corresponding GAAP measures without unreasonable efforts because we are unable to predict the ultimate outcome of certain significant items. These items include, but are not limited to, significant legal settlements, unrealized gains and losses on equity investments, tax and regulatory reserve changes, restructuring costs and acquisition and financing related impacts." [p.5]

## 5. Outlook, verbatim

### 5a. Q2 2026 release — "Outlook for Q3 2026" [Q2 2026 release, p.1] (the complete section)

> For Q3 2026, we anticipate:
> • Gross Bookings of $58.25 billion to $60.25 billion, representing growth of 18% to 22% YoY on a constant-currency basis.
>   ◦ Our outlook assumes a roughly 1 percentage-point currency headwind to total reported YoY growth.
> • Non-GAAP EPS of $0.84 to $0.88, representing growth of 28% to 35% YoY.
>   ◦ Our outlook translates to Adjusted EBITDA of $2.86 billion to $2.96 billion.

- Nothing else is guided in the release or deck (no revenue, capex, share-count, tax-rate, or full-year figure). Range midpoints (computed): Gross Bookings $59.25 billion; Non-GAAP EPS $0.86; Adjusted EBITDA $2.91 billion.

### 5b. Q1 2026 release — "Outlook for Q2 2026" [Q1 2026 release, p.1] (the complete section; what management said last quarter to expect)

> For Q2 2026, we anticipate:
> • Gross Bookings of $56.25 billion to $57.75 billion, representing growth of 18% to 22% YoY on a constant-currency basis.
>   ◦ Our outlook assumes a roughly 2 percentage-point currency tailwind to total reported YoY growth.
> • Non-GAAP EPS of $0.78 to $0.82, representing growth of 31% to 38% YoY.
>   ◦ Our outlook translates to Adjusted EBITDA of $2.70 billion to $2.80 billion.

### 5c. Guided (May 6, 2026) vs reported (August 5, 2026) for Q2 2026 — comparison only, no verdicts

| Item | Guided in Q1 2026 release | Reported in Q2 2026 release | Gap (computed) |
|---|---|---|---|
| Gross Bookings | $56.25 billion to $57.75 billion | $58,022 million ($58.0 billion) | $272 million above the top of the range |
| Gross Bookings growth, constant currency | 18% to 22% YoY | 22% | at the top of the range |
| Currency effect on reported growth | "roughly 2 percentage-point currency tailwind" | reported 24% vs constant currency 22% | 2 points (computed as 24 − 22) |
| Non-GAAP EPS | $0.78 to $0.82 (growth 31% to 38%) | $0.81 (growth 35%) | inside the range |
| Adjusted EBITDA | $2.70 billion to $2.80 billion | $2,819 million ($2.8 billion) | $19 million above the top of the range |

## 6. Non-GAAP reconciliations, with item amounts

### 6a. GAAP Income from operations → Non-GAAP Operating Income [Q2 2026 release, p.12] — 3M 2025 | 3M 2026 | 6M 2025 | 6M 2026

| Line | Q2 2025 | Q2 2026 | 6M 2025 | 6M 2026 |
|---|---|---|---|---|
| GAAP Income from operations | 1,450 | 1,890 | 2,678 | 3,813 |
| Amortization of acquired intangible assets | 65 | 61 | 129 | 120 |
| Legal, non-income tax, and regulatory reserve changes and settlements | — | 141 | 28 | 12 |
| Goodwill and asset impairments/loss on sale of assets | — | 4 | — | 4 |
| Acquisition, financing and divestitures related expenses | 19 | 31 | 22 | 56 |
| Loss on lease arrangement, net | — | — | 2 | 5 |
| Restructuring and related charges | — | 16 | 1 | 16 |
| Total adjustments excluded from Non-GAAP Operating Income | 84 | 253 | 182 | 213 |
| Non-GAAP Operating Income | 1,534 | 2,143 | 2,860 | 4,026 |

### 6b. GAAP Net income → Non-GAAP Net Income → Non-GAAP EPS [Q2 2026 release, p.12]

| Line | Q2 2025 | Q2 2026 | 6M 2025 | 6M 2026 |
|---|---|---|---|---|
| GAAP Net income attributable to Uber Technologies, Inc. | 1,355 | 2,394 | 3,131 | 2,657 |
| Adjustments excluded from Non-GAAP Operating Income (see above) | 84 | 253 | 182 | 213 |
| Other (income) expense, net | 19 | (1,342) | (74) | 152 |
| Income tax effects (1) | (190) | 315 | (912) | 61 |
| Loss from equity method investments | 12 | 21 | 25 | 41 |
| Adjustment to redeemable non-controlling interests | — | 11 | — | 21 |
| Non-GAAP Net Income | 1,280 | 1,652 | 2,352 | 3,145 |
| Assumed net loss attributable to Freight Holding contingently issuable shares | (14) | — | (27) | — |
| Non-GAAP Net Income attributable to common stockholders | 1,266 | 1,652 | 2,325 | 3,145 |
| Diluted weighted-average shares outstanding (thousands) | 2,125,628 | 2,050,225 | 2,124,181 | 2,060,763 |
| GAAP Diluted EPS (2) ($) | 0.63 | 1.17 | 1.46 | 1.29 |
| Non-GAAP EPS (2) ($) | 0.60 | 0.81 | 1.09 | 1.53 |

- Footnotes: "(1) Income tax effects include the impact of a stock loss and capitalized research and development expenses through Q2 2025 and the deferred U.S. tax impact related to our equity securities through Q2 2026. (2) Per share amounts are calculated using unrounded numbers and therefore may not recalculate." [Q2 2026 release, p.12]

### 6c. Adjusted EBITDA reconciliation [Q2 2026 release, p.13]

| Line | Q2 2025 | Q2 2026 | 6M 2025 | 6M 2026 |
|---|---|---|---|---|
| Net income attributable to Uber Technologies, Inc. | 1,355 | 2,394 | 3,131 | 2,657 |
| Net income (loss) attributable to non-controlling interests, net of tax | (5) | 22 | (7) | 41 |
| Loss from equity method investments | 12 | 21 | 25 | 41 |
| Provision for (benefit from) income taxes | 142 | 840 | (260) | 1,034 |
| Other (income) expense, net | 19 | (1,342) | (74) | 152 |
| Interest expense | 108 | 127 | 213 | 235 |
| Interest income | (181) | (172) | (350) | (347) |
| Income from operations | 1,450 | 1,890 | 2,678 | 3,813 |
| Depreciation and amortization | 175 | 188 | 346 | 372 |
| Stock-based compensation expense | 475 | 549 | 910 | 1,022 |
| Legal, non-income tax, and regulatory reserve changes and settlements | — | 141 | 28 | 12 |
| Goodwill and asset impairments/loss on sale of assets, net | — | 4 | — | 4 |
| Acquisition, financing and divestitures related expenses | 19 | 31 | 22 | 56 |
| Loss on lease arrangement, net | — | — | 2 | 5 |
| Restructuring and related charges | — | 16 | 1 | 16 |
| Adjusted EBITDA | 2,119 | 2,819 | 3,987 | 5,300 |

- Note: stock-based compensation is 549 in the Adjusted EBITDA bridge but 550 in the cash-flow statement for the same quarter (six months 1,022 vs 1,023); both are as printed. [Q2 2026 release, p.8, p.13]

### 6d. Free cash flow reconciliation [Q2 2026 release, p.13; TTM from Q2 2026 supplemental, p.31]

| Line | Q2 2025 | Q2 2026 | 6M 2025 | 6M 2026 |
|---|---|---|---|---|
| Net cash provided by operating activities | 2,564 | 2,862 | 4,888 | 5,213 |
| Purchases of property and equipment | (89) | (70) | (163) | (135) |
| Free cash flow | 2,475 | 2,792 | 4,725 | 5,078 |

- Five quarters (Jun 30 '25, Sept 30 '25, Dec 31 '25, Mar 31 '26, Jun 30 '26): operating cash flow 2,564, 2,328, 2,883, 2,351, 2,862; purchases of property and equipment (89), (98), (75), (65), (70); Free Cash Flow $2,475, $2,230, $2,808, $2,286, $2,792. [Q2 2026 supplemental, p.31]
- Trailing twelve months ended the same five dates: operating cash flow 8,789, 8,966, 10,099, 10,126, 10,424; purchases of property and equipment (249), (305), (336), (327), (308); Free Cash Flow $8,540, $8,661, $9,763, $9,799, $10,116. [Q2 2026 supplemental, p.31]

### 6e. Five-quarter Non-GAAP Operating Income and Adjusted EBITDA bridges (deck tables; signs as printed, i.e. deductions from the non-GAAP figure down to GAAP) [Q2 2026 supplemental, p.26, p.28]

| Line | Jun 30 '25 | Sept 30 '25 | Dec 31 '25 | Mar 31 '26 | Jun 30 '26 |
|---|---|---|---|---|---|
| Non-GAAP Operating Income | 1,534 | 1,675 | 1,918 | 1,883 | 2,143 |
| Amortization of acquired intangible assets | (65) | (72) | (67) | (59) | (61) |
| Legal, non-income tax, and regulatory reserve changes and settlements | — | (479) | (57) | 129 | (141) |
| Goodwill and asset impairment/loss on sale of assets | — | (2) | — | — | (4) |
| Acquisition, financing, and divestitures related expenses | (19) | (6) | (15) | (25) | (31) |
| Loss on lease arrangements, net | — | — | — | (5) | — |
| Restructuring and related charges | — | (3) | (5) | — | (16) |
| GAAP Income from operations | 1,450 | 1,113 | 1,774 | 1,923 | 1,890 |
| Adjusted EBITDA | 2,119 | 2,256 | 2,487 | 2,481 | 2,819 |
| Depreciation and amortization | (175) | (188) | (185) | (184) | (188) |
| Stock-based compensation expense | (475) | (465) | (451) | (473) | (549) |
| Other income (expense), net | (19) | 1,426 | (1,568) | (1,494) | 1,342 |
| Interest expense | (108) | (112) | (115) | (108) | (127) |
| Interest income | 181 | 193 | 200 | 175 | 172 |
| Loss from equity method investments | (12) | (14) | (14) | (20) | (21) |
| (Provision for) benefit from income taxes | (142) | 4,046 | 40 | (194) | (840) |
| Net (income) loss attributable to non-controlling interests, net of tax | 5 | (26) | (21) | (19) | (22) |
| Net income attributable to Uber Technologies, Inc. | 1,355 | 6,626 | 296 | 263 | 2,394 |

- Non-GAAP Net Income five quarters: $1,280, $1,389, $1,496, $1,493, $1,652; income tax effects 190, 4,387, 526, 254, (315); diluted weighted-average shares (thousands) 2,125,628, 2,124,391, 2,106,011, 2,071,391, 2,050,225. [Q2 2026 supplemental, p.27]

### 6f. Non-GAAP costs and operating expenses, five quarters ($ millions) [Q2 2026 supplemental, p.29–30]

| Line | Jun 30 '25 | Sept 30 '25 | Dec 31 '25 | Mar 31 '26 | Jun 30 '26 |
|---|---|---|---|---|---|
| Revenue | 12,651 | 13,467 | 14,366 | 13,203 | 14,191 |
| GAAP Cost of Revenue, excluding D&A | 7,611 | 8,109 | 8,681 | 7,258 | 7,815 |
| Non-GAAP Cost of Revenue | 7,611 | 8,109 | 8,681 | 7,423 | 7,810 |
| GAAP Operations and support | 696 | 735 | 755 | 763 | 805 |
| Non-GAAP Operations and support | 696 | 735 | 753 | 760 | 802 |
| GAAP = Non-GAAP Sales and marketing | 1,210 | 1,277 | 1,354 | 1,326 | 1,515 |
| GAAP Research and development | 840 | 862 | 885 | 951 | 1,043 |
| Non-GAAP Research and development | 840 | 860 | 884 | 950 | 1,042 |
| GAAP General and administrative | 669 | 1,183 | 732 | 798 | 935 |
| Non-GAAP General and administrative | 650 | 697 | 715 | 772 | 781 |
| GAAP Depreciation and amortization | 175 | 188 | 185 | 184 | 188 |
| Non-GAAP Depreciation & Amortization | 110 | 116 | 118 | 125 | 127 |

- Q2 2026 adjustments inside those lines: Cost of revenue restructuring (5); Operations and support acquisition-related (3); G&A legal/regulatory (114), goodwill/asset impairment (4), restructuring (9), acquisition-related (27); R&D acquisition-related (1); D&A amortization of acquired intangibles (61). Q1 2026: cost of revenue legal/regulatory 165 (a credit, adding to cost), G&A acquisition-related (23), loss on lease (3) in G&A and (2) in operations and support. [Q2 2026 supplemental, p.29–30]

## 7. Business highlights (the Q2 2026 release has no highlights section; these are from the deck's four highlight slides and the two CEO/CFO quotes in §1)

- Deck p.5 headline: "Delivery Hero expands Uber's local commerce platform while accelerating cross-platform engagement". Labels on the page: Gross Bookings pie charts "2019 (IPO)" with "$65B" and "22%" and "2025¹" with "$236B" and "56%" (legend: Delivery, Mobility, Freight; which slice the percentages label is not stated in text); "Cross-Platform Markets / Total Markets: Pre Deal 34 / 79; Post Deal 58 / 99"; "50M+ new eligible cross-platform users". Footnote 1: "Reflects pro forma 2025 Gross Bookings for Uber and Delivery Hero assets within acquisition scope." [Q2 2026 supplemental, p.5]
- Deck p.6: "World Cup showcased the power of Uber's platform across Mobility and Delivery"; "8M+ tourists took rides in host cities | ~$300M of World Cup savings¹"; product names "Travel Pass, International Benefits, Specialized Pickup, Deal Drops, Cross-Platform Offers" under "Travel & Venue Experience" and "Game Day Offers". Footnote 1: "Includes savings from Travel Pass, Uber One International Benefits, and Game Day Offers." [Q2 2026 supplemental, p.6]
- Deck p.7: "Uber One continues to deepen platform engagement"; "400K Participating merchants, ~50% increase YoY"; "35+ Partners" (Global Reach); "Member Days": "~70% increase in merchant funded offers YoY" (Delivery), "~110% increase in non UberX Trips YoY" (Mobility); "~40% of eligible¹ members are active across both Mobility and Delivery". Footnote 1: "Eligible members defined as active members in markets with Mobility and Delivery operations." No Uber One member count is given for Q2 2026 (the Q1 2026 release said "Reaching 50 million Uber One members … with members now driving half of our Gross Bookings across Mobility and Delivery" [Q1 2026 release, p.1]). [Q2 2026 supplemental, p.7]
- Deck p.8: "Uber is building the infrastructure to commercialize autonomous mobility at global scale"; "2026 Deployment Partners" grouped as Hardware Platform, Self-Driving Technology, Fleet Management (partner names are logos and did not survive extraction); city list (text): London, UK; Munich, DE; Las Vegas, NV; Zagreb, HR; Bay Area, CA; Atlanta, GA; Zurich, CH; Tokyo, JP; Dallas, TX; Madrid, ES; Dubai, UAE; Los Angeles, CA; Abu Dhabi, UAE; Austin, TX; Riyadh, KSA (15 cities); "7 live cities | 8 cities launching by end of 2026". Which seven are live is shown by colour only and is not recoverable from the text. No AV trip counts. [Q2 2026 supplemental, p.8]
- Release: "we've added more first-time users over the past twelve months than in any period over the past five years" (CEO); "build the world's largest platform for autonomous vehicles" (CEO). [Q2 2026 release, p.1]
- Nothing in the release or deck on advertising revenue, grocery/retail Gross Bookings, Freight operations beyond the segment tables, or specific new markets other than the Delivery Hero slide.

## 8. Delivery Hero documents (July 16, 2026)

Status wording, verbatim: "Uber Announces Acquisition Offer for Delivery Hero"; "Uber Technologies, Inc. (NYSE: UBER) has entered into a business combination agreement with Delivery Hero"; "Under the terms of the voluntary takeover offer, Uber will offer Delivery Hero shareholders cash consideration"; Delivery Hero boards "unanimously welcome and support the Takeover Offer and intend to recommend Delivery Hero shareholders to tender into the offer, subject to their review of the Offer Document"; "Closing is expected in the second half of 2027." The forward-looking statements refer to "the pending transaction" and "the proposed transaction". The deck: "Proposed transaction summary"; "closing expected in H2'27". [Delivery Hero release, p.1, p.3, p.5; Delivery Hero presentation, p.3] The Q2 2026 release (August 5, 2026) does not mention Delivery Hero at all; the Q2 deck's p.5 uses "Pre Deal / Post Deal" and "acquisition scope" wording only.

- Offer price and value: "Cash consideration of €41.50 per share offered to all Delivery Hero shareholders, representing an Equity Value of $14.8 billion, or $13.7 billion adjusted for Uber's prior stake purchases"; Equity Value "implied for 100% of the company"; footnote "Based on Delivery Hero's fully diluted shares outstanding of 314 million." [Delivery Hero release, p.1] Deck: "Transaction values translated from EUR to USD at 1.14 spot conversion rate." [Delivery Hero presentation, p.3]
- Multiple: "Uber's multiple paid implies ~8x EV / 2027E Adj. EBITDA (incl. Uber's existing economic ownership and over $1.2 billion of run-rate synergies)²"; footnote 2: "Uber purchased a ~37% economic stake in Delivery Hero at prices below the Offer Price, reducing Uber's all-in equity purchase price. Net debt and other equity-to-enterprise bridge items (including non-controlling interests) of $4.2 billion and other adjustments. Consensus as per Delivery Hero company compiled consensus. Adjusted EBITDA presented here is adjusted based on Uber's reporting standards (U.S. GAAP) and also reflects the pro-forma group to be acquired." [Delivery Hero presentation, p.3]
- Uber's prior stake and resulting interest: "Prior to the announcement of the Takeover Offer, Uber held approximately 24.77% of Delivery Hero's issued voting share capital directly, and held additional economic exposure of approximately 11.74% through equity derivatives. Prosus has entered into an irrevocable undertaking agreement to tender all of their Delivery Hero shares (~17% of shares outstanding) into the offer, bringing Uber's total economic interest to ~53%." [Delivery Hero release, p.3] Deck: "including Uber's existing ~37% economic ownership". [Delivery Hero presentation, p.3] (24.77 + 11.74 = 36.51, computed.)
- Minimum acceptance and conditions: "The Takeover Offer will be subject to a minimum acceptance threshold of 50% plus one share of Delivery Hero's outstanding share capital (inclusive of shares owned by Uber) and certain further conditions, including receipt of certain merger control and financial regulatory clearances, which will be set out in full in the Offer Document." "Uber has committed to not entering into a Domination and Profit Transfer Agreement (DPLTA) for a period of three years." "The Offer Document will be submitted to BaFin for approval and published in accordance with the German Securities Acquisition and Takeover Act (WpÜG). The acceptance period for the Takeover Offer will commence upon publication of the Offer Document." Offer website: www.delivering-value.com. Bidder entity: "Uber International Technologies II Corporation (the "Bidder")". [Delivery Hero release, p.3–5]
- Financing: "Uber will fund the Takeover Offer through existing cash on its balance sheet and new debt financing. Uber has executed a committed bridge facility of approximately €14 billion. The transaction is structured to maintain Uber's strong investment grade credit rating, with gross leverage to remain below 2x, supported by Uber's strong free cash flow generation. Uber's existing capital allocation framework remains unchanged, including its commitment to return excess capital to shareholders through share buybacks." [Delivery Hero release, p.3] Deck: bridge facility "~€14 billion for cash confirmation purposes; to be refinanced prior to closing"; "Affiliates of Morgan Stanley & Co. LLC, Bank of America and Deutsche Bank are providing the committed bridge facility to Uber." [Delivery Hero presentation, p.12; Delivery Hero release, p.4]
- SSW Partners carve-out: "Delivery Hero has entered into a separate agreement with SSW Partners, a New York-based investment firm … SSW will acquire Delivery Hero's businesses in a total of 14 markets, particularly where Uber Eats and Delivery Hero already overlap, subject to completion of the Uber Takeover Offer and other customary conditions, for a consideration of approximately $1.6 billion. Uber will not acquire control over the businesses transferred to SSW, and SSW will independently lead the process to find strategic partners that best position those businesses for long-term success." The 14 markets: "foodora (Austria, Czechia, Norway, Sweden); efood (Greece); Foody (Cyprus); Glovo (Moldova, Poland, Portugal, Romania, Spain); PedidosYa (Chile, Ecuador); Yemeksepeti (Türkiye)" — "14 markets generating $11B of Gross Bookings in 2025". [Delivery Hero release, p.1–2] Deck footnote: "Uber has agreed to lend SSW funds to finance the majority of the SSW transaction. SSW will repay Uber such funds over time, including in the event of a future sale of these assets." [Delivery Hero presentation, p.12]
- Businesses Uber acquires: "50 markets generating $42B of Gross Bookings² in 2025" (footnote 2: "Gross Merchandise Value (GMV) used as a proxy for Gross Bookings."): Baedal Minjok (Republic of Korea); foodpanda (Bangladesh, Cambodia, Hong Kong, Laos, Malaysia, Myanmar, Pakistan, Philippines, Singapore); Glovo (Armenia, Bosnia and Herzegovina, Bulgaria, Cote d'Ivoire, Croatia, Georgia, Italy, Kazakhstan, Kenya, Kyrgyzstan, Montenegro, Morocco, Nigeria, Serbia, Tunisia, Uganda, Ukraine); Hungerstation (Saudi Arabia); PedidosYa (Argentina, Bolivia, Costa Rica, Dominican Republic, El Salvador, Guatemala, Honduras, Nicaragua, Panama, Paraguay, Peru, Uruguay, Venezuela); talabat (Bahrain, Egypt, Iraq, Jordan, Kuwait, Oman, Qatar, United Arab Emirates). [Delivery Hero release, p.2]
- Delivery Hero scale (2025, in-scope assets, IFRS, "translated from EUR to USD at 1.12 average conversion rate"): 49M MAPCs¹ (footnote: "Monthly active users used as a proxy for MAPCs"); 900K Earners; 1.1M Merchants; $42B Gross Bookings² (GMV proxy; "Delivery Hero defines GMV as the total value paid by customers (including VAT, delivery fees, other fees and subsidies but excluding subscription fees, tips and delivery-as-a-service fees)"); 2.9B Trips; $1.1B Adj. EBITDA. Markets / #1 positions: EMEA 27 / 20; LatAm 13 / 11; APAC 10 / 7. [Delivery Hero presentation, p.4; numeric labels re-associated by x-position: the three numbers in each row sit above their captions] "About Delivery Hero": "operating its service in around 65 countries across Asia, Europe, Latin America, the Middle East and Africa … listed on the Frankfurt Stock Exchange since 2017 and is part of the MDAX stock market index." [Delivery Hero release, p.4] Delivery Hero revenue: not stated in either document.
- Combined scale: "extending the world's largest mobility and delivery platform to a total of 99 markets, with combined pro-forma Gross Bookings of $236 billion in 2025." [Delivery Hero release, p.1] Deck p.5 stacked bar "2025 Gross Bookings ($B)": $236 total; Uber Mobility $97; Freight $5; Uber Delivery $91; Delivery Hero $42; "$133" printed beside the Delivery + Delivery Hero portion. "2025 Adj. EBITDA ($B)": $9.8 total = Uber $8.7 + Delivery Hero $1.1; "Rest of Operational Peers" $6.0¹; "~1.5x". "Total markets" row: 1, 11, 8, 18, 2, 15, 41, 7, 99 (peer names are logos; 99 is Uber + Delivery Hero). Footnote 1: "Represents combined 2025 Adj. EBITDA for peer set consisting of Eternal, Lyft, Grab, Prosus, Instacart, Didi, and DoorDash. Excludes Meituan due to lack of broker estimates for segment-level profitability." [Delivery Hero presentation, p.5; labels re-associated by x/y position; Uber's FY2025 Adjusted EBITDA $8,730 million is on p.16]
- Cross-platform: "The transaction nearly doubles the number of markets where Uber will offer both mobility and delivery services, from 34 to 58 markets … cross-platform users generating roughly 3x the Gross Bookings and profits compared to single-product users." [Delivery Hero release, p.3] Deck: "Total Markets 79 → 99"; "50M+ new eligible cross-platform users¹" (footnote: "Calculated as sum of Uber MAPCs and Delivery Hero monthly active customers in new cross-platform markets, assuming no existing customer overlap."); "35M+ Delivery Hero users in new cross-platform markets"; "15M+ Uber Mobility users in new cross-platform markets"; ">50% lower cost of incremental consumer acquisition compared to paid channels"; "Cross-platform users generate 3x more Gross Bookings vs. single business users". [Delivery Hero presentation, p.8–9]
- Middle East case study (Uber Mobility vs Talabat): both "#1" category position; 2025 Gross Bookings constant-currency growth "+34%" (Uber Mobility) and "+28%" (Talabat); "~8M MAUs" each; "~7% Adj. EBITDA Margin" each (Talabat's "in line with Delivery Hero's reporting standards (IFRS)"); "Uber's top cross-platform markets are 3-4x larger than #2 player across Mobility and Delivery, on average"; cross-platform coverage labels "~28%" and "20%" (defined as "percentage of MAPCs in markets with active Mobility and Delivery businesses who use both offerings"; which label is which market is not recoverable from the text). [Delivery Hero presentation, p.10]
- Accretion and synergies: "The transaction is expected to be accretive to Non-GAAP EPS upon close; high-single-digit percentage accretion by year three." [Delivery Hero release, p.1, p.3] "Annualized synergies of over $1.2 billion within 18 months of closing". [Delivery Hero presentation, p.11]
- Commitments: "pledged to retain Delivery Hero's headquarters and make no changes to its workforce in Berlin until at least 2029. Additionally, Uber has committed to invest €2 billion in Germany over the next 5 years, with a focus on developing its local corporate workforce, growing its nationwide business, and launching autonomous vehicle deployments and partnerships with the German automotive industry." [Delivery Hero release, p.3]
- Advisors: "Morgan Stanley & Co. LLC and Deutsche Bank are serving as lead financial advisors to Uber. Bank of America and Goldman Sachs are also serving as financial advisors to Uber. Freshfields and Wachtell, Lipton, Rosen & Katz are serving as legal counsel to Uber and Cooley LLP is serving as legal counsel to Uber in connection with the financing … Evercore is serving as financial advisor to SSW." [Delivery Hero release, p.4]
- Uber FY2025 Adjusted EBITDA reconciliation (deck appendix, "Fiscal Year Ended December 31, 2025", $ in millions): Adjusted EBITDA $8,730; Legal, non-income tax, and regulatory reserve changes and settlements (564); Goodwill and asset impairments / loss on sale of assets (2); Restructuring and related charges (9); Loss on lease arrangements, net (2); Acquisition, financing and divestitures related expenses (43); Depreciation and amortization (719); Stock-based compensation expense (1,826); Income from operations $5,565; Other income (expense), net (68); Interest expense (440); Interest income 743; Loss from equity method investments (53); (Provision for) benefit from income taxes 4,346; Net (income) loss attributable to non-controlling interests, net of tax (40); Net income attributable to Uber Technologies, Inc. $10,053. [Delivery Hero presentation, p.16]
- Q2 2026 balance-sheet lines that the writer may want to read alongside (no link is stated in the sources): Equity method investments 3,773 at June 30, 2026 vs 287 at December 31, 2025; "Purchase of total return swaps" (1,640) in Q2 2026 investing cash flows; "Purchases of notes receivable" (111) in Q2 2026. [Q2 2026 release, p.6, p.8]

## 9. Prior-quarter values (Q1 2026 release) and Q1 → Q2 changes

### 9a. Q1 2026 headline table [Q1 2026 release, p.2] — Q1 2025 | Q1 2026 | % change | constant currency

- MAPCs 170 | 199 | 17%. Trips 3,036 | 3,643 | 20%. Gross Bookings $42,818 | $53,720 | 25% | 21%. Revenue $11,533 | $13,203 | 14% | 10%. GAAP Income from operations $1,228 | $1,923 | 57%. GAAP Net income attributable to Uber $1,776 | $263 | (85)%. GAAP Diluted EPS $0.83 | $0.13 | (85)%. Adjusted EBITDA $1,868 | $2,481 | 33%. Non-GAAP Operating Income $1,326 | $1,883 | 42%. Non-GAAP Net Income $1,072 | $1,493 | 39%. Non-GAAP EPS $0.50 | $0.72 | 44%. Net cash provided by operating activities $2,324 | $2,351 | 1%. Free cash flow $2,250 | $2,286 | 2%.
- Footnote: "Q1 2025 net income includes a $51 million net benefit (pre-tax) from revaluations of Uber's equity investments. Q1 2026 net income includes a $1.5 billion net headwind (pre-tax) from revaluations of Uber's equity investments."
- Q1 2026 prose bullets: Trips "grew 20% year-over-year ("YoY") to 3.6 billion, driven by … MAPCs growth of 17% YoY and monthly Trips per MAPC growth of 3% YoY"; Gross Bookings "grew 25% YoY to $53.7 billion, and 21% on a constant currency basis"; Revenue "grew 14% YoY to $13.2 billion, or 10% on a constant currency basis"; Adjusted EBITDA "grew 33% YoY to $2.5 billion. Adjusted EBITDA margin as a percentage of Gross Bookings was 4.6%, up from 4.4% in Q1 2025"; Non-GAAP Operating Income "grew 42% YoY to $1.9 billion … as a percentage of Gross Bookings was 3.5%, up from 3.1% in Q1 2025"; "Unrestricted cash, cash equivalents, and short-term investments were $6.1 billion at the end of the first quarter." [Q1 2026 release, p.1]
- Q1 2026 segment tables [Q1 2026 release, p.2–3]: Gross Bookings Mobility $21,182 → $26,394 (25%; 20% cc), Delivery 20,377 → 25,992 (28%; 23%), Freight 1,259 → 1,334 (6%; 6%), Total $42,818 → $53,720 (25%; 21%). Revenue Mobility $6,496 → $6,798 (5%; 1%), Delivery 3,777 → 5,068 (34%; 28%), Freight 1,260 → 1,337 (6%; 6%), Total $11,533 → $13,203 (14%; 10%). Segment Operating Income (Loss) Mobility $1,587 → $2,029 (28%), Delivery 671 → 961 (43%), Freight (25) → (30) ((20)%), Corporate G&A and Platform R&D (907) → (1,077) ((19)%), Non-GAAP Operating Income $1,326 → $1,883 (42%).
- Q1 2026 balance sheet (As of March 31, 2026) [Q1 2026 release, p.6]: Cash and cash equivalents 5,558; Short-term investments 533; Restricted cash and cash equivalents 680 (current) and 1,872 (non-current); Accounts receivable, net 3,895; Prepaid expenses and other current assets 2,157; Total current assets 12,823; Restricted investments 9,026; Investments 8,109; Equity method investments 268; Property and equipment, net 1,842; Operating lease right-of-use assets 1,458; Intangible assets, net 990; Goodwill 8,919; Deferred tax assets 10,844; Other assets 3,734; Total assets 59,885; Accounts payable 1,189; Short-term insurance reserves 3,467; Operating lease liabilities, current 195; Accrued and other current liabilities 7,142; Total current liabilities 11,993; Long-term insurance reserves 9,437; Long-term debt, net of current portion 10,514; Operating lease liabilities, non-current 1,710; Other long-term liabilities 419; Total liabilities 34,073; Redeemable non-controlling interests 171; Additional paid-in capital 35,527; Accumulated other comprehensive loss (421); Accumulated deficit (10,355); Total Uber stockholders' equity 24,751; Non-redeemable non-controlling interests 890; Total equity 25,641. No short-term debt line at March 31, 2026.
- Q1 2026 income statement (three months ended March 31; 2025 | 2026) [Q1 2026 release, p.7]: Revenue 11,533 | 13,203; Cost of revenue 6,937 | 7,258; Operations and support 668 | 763; Sales and marketing 1,057 | 1,326; R&D 815 | 951; G&A 657 | 798; D&A 171 | 184; Total costs and expenses 10,305 | 11,280; Income from operations 1,228 | 1,923; Interest expense (105) | (108); Interest income 169 | 175; Other income (expense), net 93 | (1,494); Income before taxes and equity method 1,385 | 496; Provision for (benefit from) income taxes (402) | 194; Loss from equity method investments (13) | (20); Net income incl. NCI 1,774 | 282; NCI (2) | 19; Net income attributable to Uber 1,776 | 263; EPS basic $0.85 | $0.13, diluted $0.83 | $0.13; shares basic 2,092,464 | 2,052,187, diluted 2,122,618 | 2,071,391 (thousands).
- Q1 2026 cash flow (three months; 2025 | 2026) [Q1 2026 release, p.8]: Net cash provided by operating activities 2,324 | 2,351; Stock-based compensation 435 | 473; Deferred income taxes (412) | 106; Unrealized (gain) loss on debt and equity securities, net (51) | 1,474; Accrued insurance reserves 675 | 443; Purchases of property and equipment (74) | (65); Purchases of non-marketable equity securities (179) | (332); Purchases of marketable securities (2,540) | (6,759); Purchases of notes receivable (40) | (187); Proceeds from maturities and sales of marketable securities 2,397 | 6,546; Acquisition of businesses, net of cash acquired — | (6); Net cash used in investing activities (542) | (773); Repurchases of common stock (1,785) | (3,011); Net cash used in financing activities (1,862) | (3,091); Net increase (decrease) in cash, cash equivalents and restricted cash (10) | (1,537); end of period 8,600 | 8,110.
- Q1 2026 reconciliations [Q1 2026 release, p.11–12] (2025 | 2026): Non-GAAP Operating Income bridge — Amortization of acquired intangible assets 64 | 59; Legal, non-income tax, and regulatory reserve changes and settlements 28 | (129); Acquisition, financing and divestitures related expenses 3 | 25; Loss on lease arrangement, net 2 | 5; Restructuring and related charges 1 | —; Total adjustments 98 | (40); Non-GAAP Operating Income 1,326 | 1,883. Net income bridge — Other (income) expense, net (93) | 1,494; Income tax effects (722) | (254); Loss from equity method investments 13 | 20; Adjustment to redeemable non-controlling interests — | 10; Non-GAAP Net Income 1,072 | 1,493; Assumed net loss attributable to Freight Holding contingently issuable shares (13) | —; Non-GAAP Net Income attributable to common stockholders 1,059 | 1,493; Non-GAAP EPS $0.50 | $0.72. Adjusted EBITDA bridge — D&A 171 | 184; Stock-based compensation expense 435 | 473; Adjusted EBITDA 1,868 | 2,481. FCF — operating cash flow 2,324 | 2,351; capex (74) | (65); free cash flow 2,250 | 2,286. Tax rates: GAAP effective tax rate (29)% | 39%; Total adjustments 52% | (16)%; Non-GAAP effective tax rate 23% | 23% [Q1 2026 release, p.10]. Footnote (1): "Income tax effects include the impact of a stock loss and capitalized research and development expenses in Q1 2025 and the deferred U.S. tax impact related to our equity securities in Q1 2026."
- Q1 2026 CEO quote: "As we highlighted at GO-GET, from innovative travel integrations to new ways to shop, we're continuing to deepen the role Uber plays in daily life … Reaching 50 million Uber One members is an exciting milestone as we execute against our platform strategy, with members now driving half of our Gross Bookings across Mobility and Delivery." CFO: "We are off to an exceptional start to 2026, with Gross Bookings growth exceeding 21% for the third consecutive quarter and earnings scaling at more than twice our topline … while taking a capital-efficient approach to AVs and embracing AI to drive growth and productivity." [Q1 2026 release, p.1]

### 9b. Q1 2026 → Q2 2026, side by side (verbatim values; "change" column computed)

| Item | Q1 2026 | Q2 2026 | Change (computed) |
|---|---|---|---|
| MAPCs (millions) | 199 | 208 | +9; +4.5% |
| Trips (millions) | 3,643 | 3,867 | +224; +6.1% |
| Monthly Trips / MAPC | 6.1 | 6.2 | +0.1 |
| Gross Bookings ($M) | 53,720 | 58,022 | +4,302; +8.0% |
| Gross Bookings growth YoY (reported / cc) | 25% / 21% | 24% / 22% | −1 pt / +1 pt |
| Mobility Gross Bookings | 26,394 | 28,988 | +2,594; +9.8% |
| Delivery Gross Bookings | 25,992 | 27,463 | +1,471; +5.7% |
| Freight Gross Bookings | 1,334 | 1,571 | +237; +17.8% |
| Revenue ($M) | 13,203 | 14,191 | +988; +7.5% |
| Revenue growth YoY (reported / cc) | 14% / 10% | 12% / 11% | −2 pts / +1 pt |
| Business-model-change drag on revenue growth | 9 pts reported / 8 pts cc | 8 pts reported and cc | −1 pt / 0 |
| Mobility revenue | 6,798 | 7,363 | +565; +8.3% |
| Delivery revenue | 5,068 | 5,245 | +177; +3.5% |
| Freight revenue | 1,337 | 1,583 | +246; +18.4% |
| Mobility Revenue Margin (deck) | 25.8% | 25.4% | −0.4 pt |
| Delivery Revenue Margin (deck) | 19.5% | 19.1% | −0.4 pt |
| GAAP Income from operations | 1,923 | 1,890 | −33; −1.7% |
| Non-GAAP Operating Income | 1,883 | 2,143 | +260; +13.8% |
| Non-GAAP OI as % of Gross Bookings | 3.5% | 3.7% | +0.2 pt |
| Mobility Segment Operating Income | 2,029 | 2,215 | +186; +9.2% |
| Delivery Segment Operating Income | 961 | 1,055 | +94; +9.8% |
| Freight Segment Operating Income (Loss) | (30) | (24) | +6 |
| Corporate G&A and Platform R&D | (1,077) | (1,103) | −26 |
| Adjusted EBITDA | 2,481 | 2,819 | +338; +13.6% |
| Adjusted EBITDA margin (% of Gross Bookings) | 4.6% | 4.9% | +0.3 pt |
| GAAP Net income attributable to Uber | 263 | 2,394 | +2,131 |
| Equity-investment revaluation effect (pre-tax) | $1.5 billion net headwind | $1.6 billion net benefit | — |
| GAAP Diluted EPS ($) | 0.13 | 1.17 | +1.04 |
| Non-GAAP Net Income | 1,493 | 1,652 | +159; +10.6% |
| Non-GAAP EPS ($) | 0.72 | 0.81 | +0.09; +12.5% |
| Non-GAAP EPS growth YoY | 44% | 35% | −9 pts |
| Net cash provided by operating activities | 2,351 | 2,862 | +511; +21.7% |
| Purchases of property and equipment | (65) | (70) | +5 |
| Free cash flow | 2,286 | 2,792 | +506; +22.1% |
| TTM free cash flow (deck) | 9,799 | 10,116 | +317 |
| Stock-based compensation (cash-flow statement) | 473 | 550 | +77; +16.3% |
| Repurchases of common stock (cash flow) | (3,011) | (518) | −2,493 |
| Unrestricted cash, cash equivalents and short-term investments | $6.1 billion | $5.4 billion | −$0.7 billion |
| Cash and cash equivalents (balance sheet) | 5,558 | 4,870 | −688 |
| Short-term debt | — (no line) | 1,997 | +1,997 |
| Long-term debt, net of current portion | 10,514 | 10,726 | +212 |
| Equity method investments | 268 | 3,773 | +3,505 |
| Total assets | 59,885 | 65,801 | +5,916 |
| Diluted weighted-average shares (thousands) | 2,071,391 | 2,050,225 | −21,166; −1.0% |
| Non-GAAP effective tax rate | 23% | 24% | +1 pt |
| Legal, non-income tax, and regulatory reserve changes and settlements (Non-GAAP OI bridge) | (129) | 141 | — |

## 10. Not disclosed (looked for in all five files, not found) and as-of confirmation

Not disclosed in the Q2 2026 release, Q2 2026 deck, or Q1 2026 release:
- Adjusted EBITDA by segment (replaced by Segment Operating Income; see §3c) and any segment Adjusted EBITDA margin.
- "Take rate" by segment as a phrase; the deck's "Revenue Margin" (revenue ÷ Gross Bookings) is the only such measure, and it is given for Mobility and Delivery only (not Freight, not total).
- Freight Gross Bookings for Q3 2025 and Q4 2025 (the Freight deck page omits them).
- Insurance costs or insurance expense trend (only the balance-sheet reserve lines and the "Accrued insurance reserves" cash-flow line appear).
- Driver or courier counts; driver earnings; supply-side metrics of any kind.
- Autonomous-vehicle trip counts, AV Gross Bookings, or names of AV partners in text (logos only on deck p.8).
- Uber One member count as of Q2 2026 (last stated: "50 million" in the Q1 2026 release); Uber One share of Gross Bookings as of Q2 2026 (Q1 2026 release: "half").
- Advertising revenue or run-rate; grocery and retail Gross Bookings; Uber for Business; new-market launches.
- Remaining share-repurchase authorization; any new authorization; average repurchase price.
- Headcount.
- Capital expenditure guidance, revenue guidance, full-year guidance, tax-rate guidance, share-count guidance.
- Terms of the Q2 2026 borrowing (the 3,997 proceeds and 2,000 repayment), or what the 1,997 short-term debt is.
- Any explanation of the "Purchase of total return swaps" (1,640) or of the rise in equity method investments to 3,773.
- Constant-currency growth for Non-GAAP Operating Income or Adjusted EBITDA.
- MAPCs, Trips or Gross Bookings by geography.
Not disclosed in the Delivery Hero documents: Delivery Hero revenue; Delivery Hero net debt as a stand-alone figure (only "$4.2 billion" of net debt and other bridge items combined); expected transaction costs; expected timing of regulatory filings; the identity of the "Rest of Operational Peers" numbers per peer (logos only).

As-of confirmation:
- Nothing dated after 2026-08-05 was fetched or read. The FinancialReport feed for 2026 lists only "First Quarter 2026" (03/31/2026) and "Second Quarter 2026" (06/30/2026) items; the Event feed for 2026 ends with "Uber Q2 2026 Earnings Conference Call" (08/05/2026). No 2026 feed item is dated after the cutoff, so nothing had to be skipped for as-of reasons.
- Feed items dated on or before the cutoff that this gatherer did not open (out of scope for the IR gatherer): the Q2 2026 "Prepared Remarks" PDF and "Transcript" PDF (transcript gatherer), the Q2 2026 webcast, the Q1 2026 "Prepared Remarks" and "Transcript" PDFs, the Q1 2026 Supplemental Data PDF (optional; not needed because the Q2 deck carries five-quarter series for every indicator), the 02/04/2026 Q4 2025 earnings call, the 03/02/2026 Morgan Stanley fireside chat, the 05/04/2026 annual meeting, the 05/28/2026 Bernstein fireside chat, and the Delivery Hero "Investor Video" webcast link.
- PDF creation dates: Q2 2026 release 2026-08-04 22:33 UTC; Q2 2026 supplemental 2026-08-04 23:01 UTC; Q1 2026 release 2026-05-05 22:03 UTC; Delivery Hero release 2026-07-16 04:07 UTC; Delivery Hero presentation carries no creation date in its metadata (Creator "Google"), but its cover is dated "July 16, 2026" and the feed lists it under the 07/15/2026 21:45 PT event.

## 11. Automated numeric check

- Method: every numeric token in this file (integers, decimals, comma-grouped amounts, percentages, parenthesised negatives, after stripping "$", "€", "%", "B", "M", "K", "x", "+", "~", ">" and parentheses) was searched verbatim in `press-release.txt`, `supplemental-data.txt`, `press-release-2026-Q1.txt`, `delivery-hero-press-release.txt` and `delivery-hero-presentation.txt`. Tokens that are part of source tags, ISO dates, file/page references, section numbers, PDF metadata (page counts, word yields, image counts, x-coordinates, timestamps) and quarter labels were excluded.
- Result: see the line appended below by the check script after the file was written.

- Result (run 2026-09-08 after the file was written; script `/tmp/uber-orch/ir/verify/numcheck.py`, scratch only): 755 unique numeric tokens checked; 682 found verbatim in at least one of the five cached texts; 73 not found. Of the 73: three are bbox x-coordinates quoted in the method description in §0 (750, 965, 1075; the other coordinates happen to coincide with source numbers), and 70 are items labelled "(computed)": the year-over-year and six-month diluted-share changes (75,403; 63,418; 3.0%) in §1; the 26 margin cross-checks and the three Trips/MAPC checks (6.05, 6.10, 6.20) in §3d–3e; the guidance midpoints (59.25, 0.86, 2.91) and the $272 million gap in §5; 36.51 in §8; and the "Change (computed)" column of table 9b (224; 4,302; 2,594; 1,471; 237; 246; 186; 338; 2,131; 1.04; 0.09; 511; 317; 2,493; 688; 3,505; 5,916; 21,166 and the percentage changes 5.7, 17.8, 7.5, 8.3, 18.4, 13.8, 13.6, 10.6, 12.5, 21.7, 22.1, 16.3 and the 0.4 / 0.3 point deltas). No unlabelled number failed the check. Caveat: small computed values (for example "+9", "+6", "$19 million", "−26", "2 points", "−33") are trivially present somewhere in the sources and so pass the check without proving anything; every computed value is labelled where it appears, and no other computed items exist in this file.
