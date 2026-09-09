# NIKE, Inc. (NKE) — Q4 FY2026 IR gatherer notes: press release, financial schedules, prior-quarter press release

- Quarter: Q4 FY2026 (quarter ended May 31, 2026); fiscal year FY2026 ended May 31, 2026 (June 1, 2025 – May 31, 2026). Prior quarter: Q3 FY2026 (quarter ended February 28, 2026).
- As-of cutoff: 2026-07-15 (10-K filing date). Release and call 2026-06-30. Nothing published after 2026-07-15 was fetched or read.
- Cached text files (all in this folder; see `MANIFEST-ir.md`): `press-release.txt` (Q4 FY2026 release, 8-K Exhibit 99.1, four tables included), `supplemental.txt` (the IR site's "Q4FY26 Financial Schedules & Key Financial Metrics" PDF in `pdftotext -layout` form; it contains the same four tables as the release and nothing else), `press-release-FY2026-Q3.txt` (Q3 FY2026 release, 8-K Exhibit 99.1, four tables included; the IR site's separate Q3 "schedules only" PDF is a strict subset of it, so no separate `supplemental-FY2026-Q3.txt` was cached).
- Tags: `[Q4 FY2026 release, <section or table>]` = press-release.txt; `[Q4 FY2026 schedules, <table>]` = supplemental.txt (same numbers as the release tables; cited where the layout form is the cleaner grep target); `[Q3 FY2026 release, <section or table>]` = press-release-FY2026-Q3.txt.
- Page numbering: neither the Q4 nor the Q3 release PDF has printed page numbers, and the 8-K exhibit HTML has no pages at all, so every tag names the section heading or table title instead of a page. For anyone opening the PDFs: Q4 release PDF (8 pages) p.1 header and headline bullets, p.2 rest of the Fourth Quarter review and the Fiscal 2026 review, p.3 balance-sheet review, shareholder returns, conference call, p.4 about, forward-looking statements, "(Tables Follow)", p.5 Consolidated Statements of Income, p.6 Consolidated Balance Sheets, p.7 Divisional Revenues, p.8 EBIT. Q3 release PDF (6 pages): p.1–2 text, p.3 income statement, p.4 balance sheet, p.5 Divisional Revenues, p.6 EBIT. The Combined Tables PDF (4 pages) and the Q3 schedules PDF (4 pages) are those last four pages alone.
- Text quality: no page of any PDF is an image; `pdftotext -layout` keeps every table's columns aligned; the plain reading-order `pdftotext` copies scramble the tables (one cell per line, "$" split from its number), so the layout copies and the 8-K exhibit conversions are the authoritative text. No slides or earnings presentation exist for Q4 FY2026 (feed evidence in MANIFEST-ir.md).
- What the release does NOT contain (both quarters): a cash flow statement, a channel (Wholesale / NIKE Direct) table in dollars, a geography-by-channel split, store counts, an order-book or futures figure, share-count at period end, remaining buyback authorization, any guidance or outlook table. Wholesale and NIKE Direct revenue appear only in the text bullets, rounded to $0.1 billion.
- Units: USD millions unless written "billion" or per share; percentages as printed. "c-n" = currency-neutral (Nike's phrase: "excluding currency changes"), Nike's non-GAAP measure (definition in §8). "bp" = basis points. Every number is copied verbatim; the few items marked "(computed)" are the gatherer's own arithmetic on release figures.
- Release sections, in order (Q4): header; six headline bullets; CEO and CFO quotes; "Fourth Quarter Income Statement Review"; "Fiscal 2026 Income Statement Review"; "May 31, 2026 Balance Sheet Review"; "Shareholder Returns"; "Conference Call"; "About NIKE, Inc."; "Forward-Looking Statements"; footnote "* Non-GAAP financial measure. See additional information in the accompanying Divisional Revenues table."; "(Tables Follow)"; CONSOLIDATED STATEMENTS OF INCOME; CONSOLIDATED BALANCE SHEETS; DIVISIONAL REVENUES (with footnotes 1–4); EARNINGS BEFORE INTEREST AND TAXES ("EBIT") (with footnotes 1–4).

## 1. Headline results, Q4 FY2026 (three months ended May 31, 2026) and FY2026 (twelve months ended May 31, 2026)

- Release title: "NIKE, INC. REPORTS FISCAL 2026 FOURTH QUARTER AND FULL YEAR RESULTS"; dateline "BEAVERTON, Ore., June 30, 2026". Investor contact Paul Trussell; media contact Sandra Carreon-John. [Q4 FY2026 release, header]
- Headline bullets, verbatim: "Full year revenues were $46.4 billion, flat on a reported basis and down 2 percent on a currency-neutral basis*"; "Fourth quarter revenues were $11.0 billion, down 1 percent on a reported basis and down 4 percent on a currency-neutral basis"; "Wholesale revenues for the fourth quarter were $6.6 billion, up 4 percent on a reported basis and up 1 percent on a currency-neutral basis"; "NIKE Direct revenues for the fourth quarter were $4.1 billion, down 7 percent on a reported basis and down 9 percent on a currency-neutral basis"; "Gross margin for the fourth quarter increased 890 basis points to 49.2 percent, including an approximately 900 basis point benefit due to the expected recovery of the International Emergency Economic Powers Act ("IEEPA") tariffs"; "Diluted earnings per share was $0.72 for the fourth quarter, including a $0.52 benefit related to the expected recovery of the IEEPA tariffs". [Q4 FY2026 release, headline bullets]
- CEO quote, verbatim: "In fiscal 2026, we took decisive actions to strengthen the foundation of NIKE, Inc. and reposition our business for long-term growth," said Elliott Hill, President and Chief Executive Officer, NIKE, Inc. "We made meaningful structural improvements to lay the groundwork for our Sport Offense across our team culture, innovative product, brand strength, and how we serve consumers in our countries and cities. While we continue to face top-line headwinds, we're encouraged by progress in performance product and are focused on consistent execution, improved profitability and scaling our wins to realize our full potential." [Q4 FY2026 release, CEO quote]
- CFO quote, verbatim: "We delivered fourth quarter results in line with our expectations, demonstrating financial discipline in an increasingly challenging operating environment, where sell-through remains challenged," said Matthew Friend, Executive Vice President and Chief Financial Officer, NIKE, Inc. "We are improving the health of our business, managing our product portfolio and investing in marketplace elevation, while adjusting our operating costs for greater efficiency over time." [Q4 FY2026 release, CFO quote]

### 1a. Income statement, Q4 FY2026 and FY2026 [Q4 FY2026 release, Consolidated Statements of Income]

Line (USD millions except per share) | Q4 FY2026 | Q4 FY2025 | % change | FY2026 | FY2025 | % change
---|---|---|---|---|---|---
Revenues | 10,972 | 11,097 | -1% | 46,398 | 46,309 | 0%
Cost of sales | 5,579 | 6,628 | -16% | 26,487 | 26,519 | 0%
Gross profit | 5,393 | 4,469 | 21% | 19,911 | 19,790 | 1%
Gross margin | 49.2% | 40.3% | (+890 bp, computed from the two margins; release text says "increased 890 basis points") | 42.9% | 42.7% | (+20 bp; release text says "increased 20 basis points")
Demand creation expense | 1,203 | 1,253 | -4% | 4,754 | 4,689 | 1%
Operating overhead expense | 2,879 | 2,895 | -1% | 11,360 | 11,399 | 0%
Total selling and administrative expense | 4,082 | 4,148 | -2% | 16,114 | 16,088 | 0%
% of revenues | 37.2% | 37.4% | | 34.7% | 34.7% |
Interest (income) expense, net | (8) | (22) | — | (50) | (107) | —
Other (income) expense, net | (10) | 25 | — | (53) | (76) | —
Income before income taxes | 1,329 | 318 | 318% | 3,900 | 3,885 | 0%
Income tax expense | 260 | 107 | 143% | 792 | 666 | 19%
Effective tax rate | 19.6% | 33.6% | | 20.3% | 17.1% |
NET INCOME | 1,069 | 211 | 407% | 3,108 | 3,219 | -3%
EPS, basic | $0.72 | $0.14 | 414% | $2.10 | $2.17 | -3%
EPS, diluted | $0.72 | $0.14 | 414% | $2.10 | $2.16 | -3%
Weighted average shares, basic (millions) | 1,482.6 | 1,476.7 | | 1,479.8 | 1,484.9 |
Weighted average shares, diluted (millions) | 1,482.9 | 1,477.7 | | 1,481.0 | 1,487.6 |
Dividends declared per common share | $0.410 | $0.400 | | $1.630 | $1.570 |

- EBIT and EBIT margin (Nike's non-GAAP, from the EBIT table, not computed): Total NIKE, Inc. EBIT 1,321 in Q4 FY2026 vs 296 (+346%); FY2026 3,850 vs 3,778 (+2%). EBIT margin 12.0% vs 2.7% (Q4); 8.3% vs 8.2% (FY). Net income margin 9.7% vs 1.9% (Q4); 6.7% vs 7.0% (FY). [Q4 FY2026 release, EBIT table]
- Currency-neutral growth: total revenues -4% (Q4) and -2% (FY); NIKE Brand -3% (Q4) and -1% (FY); reported 0% for the NIKE Brand in Q4 and +1% for FY. [Q4 FY2026 release, Divisional Revenues]

### 1b. Drivers the release gives (verbatim or near-verbatim)

- Q4 revenues: "Revenues for NIKE, Inc. were $11.0 billion, down 1 percent on a reported basis and down 4 percent on a currency-neutral basis." "Revenues for the NIKE Brand were $10.7 billion, flat on a reported basis and down 3 percent on a currency-neutral basis, primarily due to declines in Greater China and EMEA, partially offset by growth in North America." [Q4 FY2026 release, Fourth Quarter Income Statement Review]
- Q4 wholesale: "Wholesale revenues were $6.6 billion, up 4 percent on a reported basis and up 1 percent on a currency-neutral basis, primarily due to growth in North America, partially offset by declines in Greater China." [Q4 FY2026 release, Fourth Quarter Income Statement Review]
- Q4 NIKE Direct: "NIKE Direct revenues were $4.1 billion, down 7 percent on a reported basis and down 9 percent on a currency-neutral basis, due to a 12 percent decrease in NIKE Brand Digital and a 7 percent decrease in NIKE-owned stores." (The basis, reported or currency-neutral, of the 12 percent and 7 percent is not stated.) [Q4 FY2026 release, Fourth Quarter Income Statement Review]
- Q4 Converse: "Revenues for Converse were $244 million, down 32 percent on a reported basis and down 34 percent on a currency-neutral basis, due to declines across all territories." [Q4 FY2026 release, Fourth Quarter Income Statement Review]
- Q4 gross margin: "Gross margin increased 890 basis points to 49.2 percent, primarily due to the expected recovery of the IEEPA tariffs. The expected recovery of the IEEPA tariffs of $986 million increased gross margin by approximately 900 basis points." No other gross-margin driver (markdowns, channel mix, FX, product costs) is named for Q4 in the release. [Q4 FY2026 release, Fourth Quarter Income Statement Review]
- Q4 SG&A: "Selling and administrative expense decreased 2 percent to $4.1 billion." "Demand creation expense was $1.2 billion, down 4 percent, primarily due to lower brand marketing expense, partially offset by unfavorable changes in foreign currency exchange rates." "Operating overhead expense was $2.9 billion, down 1 percent, due to lower other administrative costs, partially offset by unfavorable changes in foreign currency exchange rates and higher wage-related expense." [Q4 FY2026 release, Fourth Quarter Income Statement Review]
- Q4 tax: "The effective tax rate was 19.6 percent, compared to 33.6 percent for the same period last year, primarily due to stock-based compensation and prior year one-time items that had an outsized impact on the tax rate because of lower pre-tax income in the prior year." [Q4 FY2026 release, Fourth Quarter Income Statement Review]
- Q4 net income: "Net income was $1.1 billion, up 407 percent, and Diluted earnings per share was $0.72, including a $0.52 benefit related to the expected recovery of the IEEPA tariffs." [Q4 FY2026 release, Fourth Quarter Income Statement Review]
- FY2026 revenues: "Revenues for NIKE, Inc. were $46.4 billion, flat on a reported basis and down 2 percent on a currency-neutral basis." "Revenues for the NIKE Brand were $45.2 billion, up 1 percent on a reported basis and down 1 percent on a currency-neutral basis, primarily due to declines in Greater China and EMEA, partially offset by growth in North America." "Wholesale revenues were $27.5 billion, up 6 percent on a reported basis and up 4 percent on a currency-neutral basis." "NIKE Direct revenues were $17.7 billion, down 6 percent on a reported basis and down 8 percent on a currency-neutral basis, due to a 12 percent decrease in NIKE Brand Digital and a 4 percent decrease in NIKE-owned stores." "Revenues for Converse were $1.2 billion, down 31 percent on a reported basis and down 32 percent on a currency-neutral basis, due to declines across all territories." [Q4 FY2026 release, Fiscal 2026 Income Statement Review]
- FY2026 gross margin: "Gross margin increased 20 basis points to 42.9 percent." No driver sentence is given for the full year. [Q4 FY2026 release, Fiscal 2026 Income Statement Review]
- FY2026 SG&A: "Selling and administrative expense was flat compared to the prior year at $16.1 billion." "Demand creation expense was $4.8 billion, up 1 percent, due to higher sports marketing expense and unfavorable changes in foreign currency exchange rates, partially offset by lower brand marketing expense, reflecting higher investment in key sports events in the prior year." "Operating overhead expense was $11.4 billion, flat compared to the prior year as lower other administrative costs were offset by higher wage-related expense, driven by employee severance costs, and unfavorable changes in foreign currency exchange rates." [Q4 FY2026 release, Fiscal 2026 Income Statement Review]
- FY2026 tax: "The effective tax rate was 20.3 percent, compared to 17.1 percent for the same period last year, primarily due to a prior year one-time, non-cash deferred tax benefit provided by U.S. tax regulations related to foreign currency gains and losses." [Q4 FY2026 release, Fiscal 2026 Income Statement Review]
- FY2026 net income: "Net income was $3.1 billion, down 3 percent, and Diluted earnings per share was $2.10, a decrease of 3 percent." [Q4 FY2026 release, Fiscal 2026 Income Statement Review]

### 1c. IEEPA tariff recovery: what the release states, and gatherer arithmetic

- EBIT-table footnote 2, verbatim: "On February 20, 2026, the U.S. Supreme Court ruled that U.S. tariffs imposed under the International Emergency Economic Powers Act ("IEEPA") on goods imported into the U.S. were unauthorized. During the fourth quarter of fiscal 2026, the Company deemed the recovery of IEEPA tariffs paid to be probable. For the three and twelve months ended May 31, 2026, North America and Converse include a $965 million and $21 million benefit, respectively, for the expected recovery of the IEEPA tariffs paid on goods imported into the U.S. For the twelve months ended May 31, 2026, the benefit largely offsets the impact of the IEEPA tariffs recognized during fiscal 2026." [Q4 FY2026 release, EBIT table footnote 2]
- Stated benefit amounts: $986 million to gross margin (approximately 900 bp in Q4); $965 million in North America EBIT and $21 million in Converse EBIT (965 + 21 = 986, computed); $0.52 of Q4 diluted EPS; approximately $0.3 billion of cash received from IEEPA tariff recoveries inside FY2026 cash generated from operations. [Q4 FY2026 release, headline bullets; EBIT table footnote 2; May 31, 2026 Balance Sheet Review]
- (computed) Q4 FY2026 figures with only the $986 million recovery removed (the tariff expense itself stays in): gross profit 5,393 − 986 = 4,407, i.e. 40.2% of revenues (vs 40.3% in Q4 FY2025); Total NIKE, Inc. EBIT 1,321 − 986 = 335, i.e. 3.1% EBIT margin (vs 2.7%); North America EBIT 2,000 − 965 = 1,035 (vs 1,045); Converse EBIT 23 − 21 = 2 (vs 27); diluted EPS 0.72 − 0.52 = $0.20 (vs $0.14). For FY2026: EBIT 3,850 − 986 = 2,864 (vs 3,778); North America EBIT 5,376 − 965 = 4,411 (vs 4,735); Converse EBIT 18 − 21 = (3) (vs 240). The release itself gives none of these ex-benefit figures except the EPS benefit and the "approximately 900 basis point" gross-margin effect.
- The FY2026 tariff cost that the benefit "largely offsets" is not quantified in the release. Not disclosed.

## 2. Revenue tables (as printed; reported % change, then "% change excluding currency changes")

### 2a. NIKE, Inc. revenues by segment and by product [Q4 FY2026 release, Divisional Revenues] [Q4 FY2026 schedules, Divisional Revenues]

Three months ended 5/31 (USD millions) | Q4 FY2026 | Q4 FY2025 | % change | % change c-n
---|---|---|---|---
North America — Footwear | 3,230 | 3,104 | 4% | 4%
North America — Apparel | 1,310 | 1,303 | 1% | 0%
North America — Equipment | 292 | 296 | -1% | -2%
North America — Total | 4,832 | 4,703 | 3% | 3%
Europe, Middle East & Africa — Footwear | 1,821 | 1,893 | -4% | -9%
EMEA — Apparel | 982 | 929 | 6% | 0%
EMEA — Equipment | 172 | 178 | -3% | -9%
EMEA — Total | 2,975 | 3,000 | -1% | -6%
Greater China — Footwear | 938 | 1,074 | -13% | -17%
Greater China — Apparel | 334 | 372 | -10% | -15%
Greater China — Equipment | 25 | 30 | -17% | -21%
Greater China — Total | 1,297 | 1,476 | -12% | -17%
Asia Pacific & Latin America — Footwear | 1,114 | 1,114 | 0% | -2%
APLA — Apparel | 420 | 398 | 6% | 4%
APLA — Equipment | 62 | 63 | -2% | -3%
APLA — Total | 1,596 | 1,575 | 1% | -1%
Global Brand Divisions (fn 2) | 24 | 9 | 167% | 150%
TOTAL NIKE BRAND (fn 3) | 10,724 | 10,763 | 0% | -3%
Converse | 244 | 357 | -32% | -34%
Corporate (fn 4) | 4 | (23) | — | —
TOTAL NIKE, INC. REVENUES | 10,972 | 11,097 | -1% | -4%
NIKE Brand — Footwear | 7,103 | 7,185 | -1% | -4%
NIKE Brand — Apparel | 3,046 | 3,002 | 1% | -1%
NIKE Brand — Equipment | 551 | 567 | -3% | -5%
NIKE Brand — Global Brand Divisions | 24 | 9 | 167% | 150%
TOTAL NIKE BRAND REVENUES | 10,724 | 10,763 | 0% | -3%

Twelve months ended 5/31 (USD millions) | FY2026 | FY2025 | % change | % change c-n
---|---|---|---|---
North America — Footwear | 13,317 | 12,684 | 5% | 5%
North America — Apparel | 6,075 | 5,837 | 4% | 4%
North America — Equipment | 1,119 | 1,051 | 6% | 6%
North America — Total | 20,511 | 19,572 | 5% | 5%
EMEA — Footwear | 7,643 | 7,569 | 1% | -5%
EMEA — Apparel | 4,210 | 3,971 | 6% | 0%
EMEA — Equipment | 719 | 717 | 0% | -6%
EMEA — Total | 12,572 | 12,257 | 3% | -3%
Greater China — Footwear | 4,188 | 4,805 | -13% | -15%
Greater China — Apparel | 1,535 | 1,616 | -5% | -7%
Greater China — Equipment | 124 | 165 | -25% | -26%
Greater China — Total | 5,847 | 6,586 | -11% | -13%
APLA — Footwear | 4,377 | 4,452 | -2% | -3%
APLA — Apparel | 1,629 | 1,541 | 6% | 5%
APLA — Equipment | 237 | 258 | -8% | -9%
APLA — Total | 6,243 | 6,251 | 0% | -1%
Global Brand Divisions (fn 2) | 49 | 48 | 2% | 2%
TOTAL NIKE BRAND (fn 3) | 45,222 | 44,714 | 1% | -1%
Converse | 1,174 | 1,692 | -31% | -32%
Corporate (fn 4) | 2 | (97) | — | —
TOTAL NIKE, INC. REVENUES | 46,398 | 46,309 | 0% | -2%
NIKE Brand — Footwear | 29,525 | 29,510 | 0% | -2%
NIKE Brand — Apparel | 13,449 | 12,965 | 4% | 2%
NIKE Brand — Equipment | 2,199 | 2,191 | 0% | -2%
NIKE Brand — Global Brand Divisions | 49 | 48 | 2% | 2%
TOTAL NIKE BRAND REVENUES | 45,222 | 44,714 | 1% | -1%

- Jordan Brand (Divisional Revenues footnote 3, verbatim): "Included in NIKE Brand revenues are sales of Jordan Brand products which were $7,034 million in fiscal 2026 compared to $7,270 million in fiscal 2025, down 3% on a reported basis and down 5% on a currency-neutral basis." Quarterly Jordan Brand revenue: not disclosed. [Q4 FY2026 release, Divisional Revenues footnote 3]

### 2b. NIKE Brand by channel (text bullets only; no channel table exists in the release or schedules)

Channel | Q4 FY2026 | reported | c-n | FY2026 | reported | c-n
---|---|---|---|---|---|---
Wholesale revenues | $6.6 billion | up 4 percent | up 1 percent | $27.5 billion | up 6 percent | up 4 percent
NIKE Direct revenues | $4.1 billion | down 7 percent | down 9 percent | $17.7 billion | down 6 percent | down 8 percent
NIKE Brand Digital | not given in dollars | "12 percent decrease" (basis not stated) | | not given in dollars | "12 percent decrease" (basis not stated) |
NIKE-owned stores | not given in dollars | "7 percent decrease" (basis not stated) | | not given in dollars | "4 percent decrease" (basis not stated) |

[Q4 FY2026 release, headline bullets; Fourth Quarter Income Statement Review; Fiscal 2026 Income Statement Review]

- (computed) 6.6 + 4.1 = 10.7 ≈ NIKE Brand revenue of $10.7 billion (10,724) for Q4; 27.5 + 17.7 = 45.2 = NIKE Brand FY revenue $45.2 billion (45,222); so Wholesale + NIKE Direct = NIKE Brand revenue excluding the small Global Brand Divisions line, within rounding.
- Each geography's Wholesale / NIKE Direct split: not disclosed in the release or schedules (the 10-K has it).
- NIKE Direct in dollars by quarter for Q3: see §9.

## 3. EBIT by segment [Q4 FY2026 release, EBIT table] [Q4 FY2026 schedules, EBIT table]

Segment (USD millions) | Q4 FY2026 | Q4 FY2025 | % change | FY2026 | FY2025 | % change
---|---|---|---|---|---|---
North America (fn 2: includes a $965 million IEEPA benefit in both Q4 FY2026 and FY2026) | 2,000 | 1,045 | 91% | 5,376 | 4,735 | 14%
Europe, Middle East & Africa | 434 | 472 | -8% | 2,417 | 2,575 | -6%
Greater China | 243 | 304 | -20% | 1,278 | 1,602 | -20%
Asia Pacific & Latin America | 316 | 319 | -1% | 1,387 | 1,527 | -9%
Global Brand Divisions (fn 3) | (1,130) | (1,246) | 9% | (4,603) | (4,699) | 2%
TOTAL NIKE BRAND EBIT | 1,863 | 894 | 108% | 5,855 | 5,740 | 2%
Converse (fn 2: includes a $21 million IEEPA benefit in both Q4 FY2026 and FY2026) | 23 | 27 | -15% | 18 | 240 | -93%
Corporate (fn 4) | (565) | (625) | 10% | (2,023) | (2,202) | 8%
TOTAL NIKE, INC. EBIT | 1,321 | 296 | 346% | 3,850 | 3,778 | 2%
Interest (income) expense, net | (8) | (22) | — | (50) | (107) | —
Income tax expense | 260 | 107 | 143% | 792 | 666 | 19%
NET INCOME | 1,069 | 211 | 407% | 3,108 | 3,219 | -3%
Total NIKE, Inc. Revenues | 10,972 | 11,097 | -1% | 46,398 | 46,309 | 0%
Net income margin | 9.7% | 1.9% | | 6.7% | 7.0% |
EBIT margin | 12.0% | 2.7% | | 8.3% | 8.2% |

- Note on the EBIT table: "Other (income) expense, net" does not appear as a separate line; EBIT is Net income plus Interest (income) expense, net plus Income tax expense, so the table's EBIT already includes Other (income) expense, net. (computed check: 1,069 + (8) + 260 = 1,321 for Q4; 3,108 + (50) + 792 = 3,850 for FY.) [Q4 FY2026 release, EBIT table footnote 1]
- Segment EBIT margins are not printed; (computed) Q4 FY2026: North America 2,000 / 4,832 = 41.4% (1,035 / 4,832 = 21.4% ex-IEEPA benefit); EMEA 434 / 2,975 = 14.6%; Greater China 243 / 1,297 = 18.7%; APLA 316 / 1,596 = 19.8%; Converse 23 / 244 = 9.4%. FY2026: North America 5,376 / 20,511 = 26.2% (4,411 / 20,511 = 21.5% ex-benefit); EMEA 2,417 / 12,572 = 19.2%; Greater China 1,278 / 5,847 = 21.9%; APLA 1,387 / 6,243 = 22.2%; Converse 18 / 1,174 = 1.5%.

## 4. Balance sheet, May 31, 2026 vs May 31, 2025 [Q4 FY2026 release, Consolidated Balance Sheets] [Q4 FY2026 schedules, Consolidated Balance Sheets]

Line (USD millions) | May 31, 2026 | May 31, 2025 | % change
---|---|---|---
Cash and equivalents | 7,563 | 7,464 | 1%
Short-term investments | 1,464 | 1,687 | -13%
Accounts receivable, net | 5,931 | 4,717 | 26%
Inventories | 7,501 | 7,489 | 0%
Prepaid expenses and other current assets | 2,144 | 2,005 | 7%
Total current assets | 24,603 | 23,362 | 5%
Property, plant and equipment, net | 4,796 | 4,828 | -1%
Operating lease right-of-use assets, net | 2,838 | 2,712 | 5%
Identifiable intangible assets, net | 259 | 259 | 0%
Goodwill | 240 | 240 | 0%
Deferred income taxes and other assets | 5,674 | 5,178 | 10%
TOTAL ASSETS | 38,410 | 36,579 | 5%
Current portion of long-term debt | 2,000 | — | 100%
Accounts payable | 3,600 | 3,479 | 3%
Current portion of operating lease liabilities | 478 | 502 | -5%
Accrued liabilities | 6,092 | 5,916 | 3%
Income taxes payable | 377 | 669 | -44%
Total current liabilities | 12,547 | 10,566 | 19%
Long-term debt | 5,942 | 7,961 | -25%
Operating lease liabilities | 2,613 | 2,550 | 2%
Deferred income taxes and other liabilities | 2,443 | 2,289 | 7%
Redeemable preferred stock | — | — | —
Shareholders' equity | 14,865 | 13,213 | 13%
TOTAL LIABILITIES AND SHAREHOLDERS' EQUITY | 38,410 | 36,579 | 5%

- Notes payable: no such line appears on the May 31, 2026 balance sheet in the release (the February 28, 2026 balance sheet in the Q3 release carried a "Notes payable" line of — vs 4; see §9). Not disclosed for May 31, 2026 in the release.
- (computed) Cash and equivalents plus short-term investments: 7,563 + 1,464 = 9,027 at May 31, 2026 vs 7,464 + 1,687 = 9,151 at May 31, 2025, down 124 (release: "$9.0 billion, down approximately $0.1 billion"). Total debt (current portion of long-term debt plus long-term debt): 2,000 + 5,942 = 7,942 vs 0 + 7,961 = 7,961.
- Inventory statement, verbatim: "Inventories for NIKE, Inc. were $7.5 billion, flat compared to the prior year, primarily reflecting an increase in units, offset by shifts in product mix." [Q4 FY2026 release, May 31, 2026 Balance Sheet Review]
- Cash statement, verbatim: "Cash and equivalents and short-term investments were $9.0 billion, down approximately $0.1 billion from last year, as cash generated from operations, which includes approximately $0.3 billion of cash received from IEEPA tariff recoveries, was more than offset by cash dividends and capital expenditures." [Q4 FY2026 release, May 31, 2026 Balance Sheet Review]
- Accounts receivable rose 26% (5,931 vs 4,717) with no explanation in the release. Not explained.
- Period-end shares outstanding: not disclosed in the release (weighted averages only, §1a).

## 5. Cash flow

- Neither the Q4 FY2026 release, the Combined Tables PDF, nor the Q3 FY2026 release contains a cash flow statement. Cash from operations, additions to property, plant and equipment, depreciation and amortization, and cash paid for repurchases and dividends are not disclosed as line items in the release; the 10-K (filings gatherer) is the only source. Not disclosed.
- The only cash-flow statements in the release are the two sentences quoted in §4 (FY2026 cash generated from operations "includes approximately $0.3 billion of cash received from IEEPA tariff recoveries" and was "more than offset by cash dividends and capital expenditures") and the Shareholder Returns figures in §6. [Q4 FY2026 release, May 31, 2026 Balance Sheet Review; Shareholder Returns]

## 6. Shareholder returns [Q4 FY2026 release, Shareholder Returns; Consolidated Statements of Income]

- Verbatim: "NIKE has a strong track record of returns to shareholders. In the fourth quarter, the Company returned approximately $609 million to shareholders through dividends, up 3 percent from the prior year." "In fiscal 2026, the Company returned approximately $2.5 billion to shareholders, including:" "Dividends of $2.4 billion, up 5 percent from the prior year." "Share repurchases of $123 million, reflecting 1.8 million shares retired as part of the Company's four-year, $18 billion program approved by the Board of Directors."

Item | Q4 FY2026 | FY2026
---|---|---
Dividends paid (approx.) | $609 million, up 3 percent | $2.4 billion, up 5 percent
Share repurchases | not stated for the quarter alone (the Q4 sentence mentions dividends only) | $123 million; 1.8 million shares retired
Total returned (approx.) | $609 million (dividends) | $2.5 billion
Dividends declared per common share | $0.410 (vs $0.400) | $1.630 (vs $1.570)
Buyback program | "four-year, $18 billion program approved by the Board of Directors" | same
Remaining authorization | not disclosed in the release | not disclosed in the release

- (computed) $123 million / 1.8 million shares ≈ $68 per share average repurchase price. (computed) 2.4 + 0.123 ≈ 2.5 billion, consistent with the "$2.5 billion" total.
- The Q3 FY2026 release adds "24 consecutive years of increasing dividend payouts" (see §9). The Q4 release does not repeat that phrase.

## 7. Guidance or outlook in the release

- No guidance in the release. The Q4 FY2026 release contains no guidance table, no outlook section and no forward-looking numbers; the only forward-looking sentences are the CEO's "we're encouraged by progress in performance product and are focused on consistent execution, improved profitability and scaling our wins to realize our full potential" and the CFO's "adjusting our operating costs for greater efficiency over time" (both quoted in full in §1), plus the boilerplate "Forward-Looking Statements" paragraph. Guidance, if any, was given on the call (transcript gatherer). [Q4 FY2026 release, CEO quote; CFO quote; Forward-Looking Statements]
- Conference call sentence, verbatim: "NIKE, Inc. management will host a conference call beginning at approximately 2:00 p.m. PT on June 30, 2026, to review fiscal fourth quarter and full year results. The conference call will be broadcast live via the Internet and can be accessed at http://investors.nike.com. For those unable to listen to the live broadcast, an archived version will be available at the same location through approximately 9:00 p.m. PT, July 24, 2026." [Q4 FY2026 release, Conference Call]
- The Q3 FY2026 release likewise has no guidance; its only forward-looking line is in the CFO quote: "Win Now actions will continue to impact results over the balance of the calendar year, and we remain confident in our ability to position the Company for profitable growth long-term." [Q3 FY2026 release, CFO quote]

## 8. Non-GAAP measures and definitions

- Nike presents exactly two non-GAAP items in the release: (1) revenue "% Change Excluding Currency Changes" (currency-neutral), marked with "*" in the headline bullets and footnote 1 of the Divisional Revenues table; (2) EBIT, Total NIKE Brand EBIT and EBIT margin, footnote 1 of the EBIT table. There is no adjusted EPS, adjusted operating income, free cash flow or "excluding IEEPA" measure; the IEEPA effects are disclosed as amounts inside GAAP lines (§1c). [Q4 FY2026 release, Divisional Revenues footnote 1; EBIT table footnote 1]
- Currency-neutral definition, verbatim (Divisional Revenues footnote 1): "The percent change has been calculated using actual exchange rates in use during the comparative prior year period and is provided to enhance the visibility of the underlying business trends by excluding the impact of translation arising from foreign currency exchange rate fluctuations, which is considered a non-GAAP financial measure. Management uses this non-GAAP financial measure when evaluating the Company's performance, including when making financial and operating decisions. Additionally, management believes this non-GAAP financial measure provides investors with additional financial information that should be considered when assessing the Company's underlying business performance and trends. References to this measure should not be considered in isolation or as a substitute for other financial measures calculated and presented in accordance with U.S. GAAP and may not be comparable to similarly titled non-GAAP measures used by other companies." [Q4 FY2026 release, Divisional Revenues footnote 1]
- Currency-neutral "reconciliation": the release gives only the two growth-rate columns side by side (reported % change and % change excluding currency changes) for every revenue line (§2a); it does not give the dollar amount of the translation effect. The spread between the two columns for total revenues is 3 points in Q4 (-1% reported vs -4% c-n) and 2 points for FY2026 (0% vs -2%); EMEA shows the widest spread (Q4: -1% vs -6%; FY: 3% vs -3%). (computed spreads.) [Q4 FY2026 release, Divisional Revenues]
- EBIT definition, verbatim (EBIT table footnote 1): "Total NIKE Brand EBIT, Total NIKE, Inc. EBIT and EBIT margin are considered non-GAAP financial measures. EBIT is calculated as Net income before Interest (income) expense, net and Income tax expense. EBIT margin is calculated as total NIKE, Inc. EBIT divided by total NIKE, Inc. Revenues. References to EBIT and EBIT margin should not be considered in isolation or as a substitute for other financial measures calculated and presented in accordance with U.S. GAAP and may not be comparable to similarly titled non-GAAP measures used by other companies. Management uses these non-GAAP financial measures when evaluating the Company's performance, including segment performance, when making financial and operating decisions. Additionally, management believes these non-GAAP financial measures provide investors with additional financial information that should be considered when assessing the Company's underlying business performance and trends." [Q4 FY2026 release, EBIT table footnote 1]
- EBIT reconciliation is the EBIT table itself: TOTAL NIKE, INC. EBIT 1,321 less Interest (income) expense, net (8) less Income tax expense 260 = NET INCOME 1,069 (Q4); 3,850, (50), 792, 3,108 (FY). [Q4 FY2026 release, EBIT table]

## 9. Prior quarter: Q3 FY2026 release (March 31, 2026), and Q4-vs-Q3 side-by-side

### 9a. Q3 FY2026 headline and quotes [Q3 FY2026 release]

- Title "NIKE, INC. REPORTS FISCAL 2026 THIRD QUARTER RESULTS"; dateline "BEAVERTON, Ore., Mar. 31, 2026"; "today reported fiscal 2026 financial results for its third quarter ended February 28, 2026." [Q3 FY2026 release, header]
- Headline bullets, verbatim: "Third quarter revenues were $11.3 billion, flat on a reported basis and down 3 percent on a currency-neutral basis*"; "Wholesale revenues were $6.5 billion, up 5 percent on a reported basis and up 1 percent on a currency-neutral basis"; "NIKE Direct revenues were $4.5 billion, down 4 percent on a reported basis and down 7 percent on a currency-neutral basis"; "Gross margin decreased 130 basis points to 40.2 percent"; "Diluted earnings per share was $0.35". [Q3 FY2026 release, headline bullets]
- CEO quote, verbatim: "This quarter we took meaningful actions to improve the health and quality of our business. The pace of progress is different across the portfolio and the areas we prioritized first continue to drive momentum," said Elliott Hill, President and Chief Executive Officer, NIKE, Inc. "The work is not finished, but the direction is clear, our teams are moving with focus and urgency, and our foundation is getting even stronger to build the future of NIKE." [Q3 FY2026 release, CEO quote]
- CFO quote, verbatim: "We delivered third quarter results in line with our expectations, and our teams continue to execute with discipline," said Matthew Friend, Executive Vice President and Chief Financial Officer, NIKE, Inc. "Win Now actions will continue to impact results over the balance of the calendar year, and we remain confident in our ability to position the Company for profitable growth long-term." [Q3 FY2026 release, CFO quote]
- Q3 drivers, verbatim: "NIKE Brand revenues were $11.0 billion, up 1 percent on a reported basis and down 2 percent on a currency-neutral basis, primarily due to declines in EMEA and Greater China, partially offset by growth in North America." "Wholesale revenues were $6.5 billion, up 5 percent on a reported basis and up 1 percent on a currency-neutral basis, primarily due to growth in North America." "NIKE Direct revenues were $4.5 billion, down 4 percent on a reported basis and down 7 percent on a currency-neutral basis, due to a 9 percent decrease in NIKE Brand Digital and a 5 percent decrease in NIKE-owned stores." "Revenues for Converse were $264 million, down 35 percent on a reported basis and down 37 percent on a currency-neutral basis, due to declines across all territories." "Gross margin decreased 130 basis points to 40.2 percent, primarily due to higher tariffs in North America." "Selling and administrative expense increased 2 percent to $4.0 billion." "Demand creation expense was $1.1 billion, flat compared to the prior year, as higher sports marketing expense and unfavorable changes in foreign currency exchange rates were offset by lower brand marketing expense." "Operating overhead expense was $2.9 billion, up 3 percent, due to employee severance costs and unfavorable changes in foreign currency exchange rates, partially offset by lower other administrative costs." "The effective tax rate was 20.0 percent compared to 5.9 percent for the same period last year, primarily due to a prior period one-time, non-cash deferred tax benefit provided by U.S. tax regulations related to foreign currency gains and losses." "Net income was $0.5 billion, down 35 percent, and Diluted earnings per share was $0.35, a decrease of 35 percent." [Q3 FY2026 release, Third Quarter Income Statement Review]
- Q3 inventory and cash statements, verbatim: "Inventories for NIKE, Inc. were $7.5 billion, down 1 percent, primarily reflecting a decrease in units and product mix shifts, partially offset by increased product costs, primarily due to higher tariffs in North America." "Cash and equivalents and short-term investments were $8.1 billion, down approximately $2.3 billion, as cash generated by operations was more than offset by cash dividends, bond repayment, capital expenditures and share repurchases." [Q3 FY2026 release, February 28, 2026 Balance Sheet Review]
- Q3 shareholder returns, verbatim: "NIKE has a strong track record of returns to shareholders, including 24 consecutive years of increasing dividend payouts. In the third quarter, the Company returned approximately $609 million to shareholders through dividends, up 3 percent from the prior year." No repurchase figure is given for Q3 or the nine months (the balance-sheet sentence says repurchases occurred). [Q3 FY2026 release, Shareholder Returns]
- Q3 release tariff language: the only tariff statements are the gross-margin driver ("primarily due to higher tariffs in North America") and the inventory sentence ("increased product costs, primarily due to higher tariffs in North America"); the IEEPA ruling of February 20, 2026 is not mentioned in the Q3 release. [Q3 FY2026 release, Third Quarter Income Statement Review; February 28, 2026 Balance Sheet Review]
- Q3 call archive: "an archived version will be available at the same location through approximately 9:00 p.m. PT, April 23, 2026." [Q3 FY2026 release, Conference Call]

### 9b. Q3 FY2026 income statement [Q3 FY2026 release, Consolidated Statements of Income]

Line (USD millions except per share) | Q3 FY2026 | Q3 FY2025 | % change | 9M FY2026 | 9M FY2025 | % change
---|---|---|---|---|---|---
Revenues | 11,279 | 11,269 | 0% | 35,426 | 35,212 | 1%
Cost of sales | 6,749 | 6,594 | 2% | 20,908 | 19,891 | 5%
Gross profit | 4,530 | 4,675 | -3% | 14,518 | 15,321 | -5%
Gross margin | 40.2% | 41.5% | (-130 bp per text) | 41.0% | 43.5% |
Demand creation expense | 1,090 | 1,088 | 0% | 3,551 | 3,436 | 3%
Operating overhead expense | 2,887 | 2,799 | 3% | 8,481 | 8,504 | 0%
Total selling and administrative expense | 3,977 | 3,887 | 2% | 12,032 | 11,940 | 1%
% of revenues | 35.3% | 34.5% | | 34.0% | 33.9% |
Interest (income) expense, net | (15) | (18) | — | (42) | (85) | —
Other (income) expense, net | (82) | (38) | — | (43) | (101) | —
Income before income taxes | 650 | 844 | -23% | 2,571 | 3,567 | -28%
Income tax expense | 130 | 50 | 160% | 532 | 559 | -5%
Effective tax rate | 20.0% | 5.9% | | 20.7% | 15.7% |
NET INCOME | 520 | 794 | -35% | 2,039 | 3,008 | -32%
EPS, basic | $0.35 | $0.54 | -35% | $1.38 | $2.02 | -32%
EPS, diluted | $0.35 | $0.54 | -35% | $1.38 | $2.02 | -32%
Weighted average shares, basic | 1,480.5 | 1,478.1 | | 1,478.9 | 1,487.6 |
Weighted average shares, diluted | 1,481.6 | 1,480.6 | | 1,480.4 | 1,491.0 |
Dividends declared per common share | $0.410 | $0.400 | | $1.220 | $1.170 |

- (computed) Nine months FY2026 plus Q4 FY2026 equals FY2026 in the Q4 release for every line checked: revenues 35,426 + 10,972 = 46,398; gross profit 14,518 + 5,393 = 19,911; demand creation 3,551 + 1,203 = 4,754; operating overhead 8,481 + 2,879 = 11,360; net income 2,039 + 1,069 = 3,108; dividends declared per share 1.220 + 0.410 = 1.630. No restatement between the two releases.

### 9c. Q3 FY2026 balance sheet, February 28, 2026 vs February 28, 2025 [Q3 FY2026 release, Consolidated Balance Sheets]

Line (USD millions) | Feb 28, 2026 | Feb 28, 2025 | % change
---|---|---|---
Cash and equivalents | 6,660 | 8,601 | -23%
Short-term investments | 1,397 | 1,792 | -22%
Accounts receivable, net | 5,369 | 4,491 | 20%
Inventories | 7,487 | 7,539 | -1%
Prepaid expenses and other current assets | 2,271 | 2,186 | 4%
Total current assets | 23,184 | 24,609 | -6%
Property, plant and equipment, net | 4,766 | 4,717 | 1%
Operating lease right-of-use assets, net | 2,886 | 2,614 | 10%
Identifiable intangible assets, net | 259 | 259 | 0%
Goodwill | 240 | 239 | 0%
Deferred income taxes and other assets | 5,729 | 5,355 | 7%
TOTAL ASSETS | 37,064 | 37,793 | -2%
Current portion of long-term debt | 999 | 1,000 | 0%
Notes payable | — | 4 | -100%
Accounts payable | 2,888 | 3,106 | -7%
Current portion of operating lease liabilities | 493 | 474 | 4%
Accrued liabilities | 6,183 | 5,905 | 5%
Income taxes payable | 275 | 734 | -63%
Total current liabilities | 10,838 | 11,223 | -3%
Long-term debt | 7,030 | 7,956 | -12%
Operating lease liabilities | 2,656 | 2,477 | 7%
Deferred income taxes and other liabilities | 2,450 | 2,130 | 15%
Redeemable preferred stock | — | — | —
Shareholders' equity | 14,090 | 14,007 | 1%
TOTAL LIABILITIES AND SHAREHOLDERS' EQUITY | 37,064 | 37,793 | -2%

- (computed) Cash and equivalents plus short-term investments 6,660 + 1,397 = 8,057 (release: "$8.1 billion"); total debt 999 + 7,030 = 8,029.

### 9d. Q3 FY2026 Divisional Revenues [Q3 FY2026 release, Divisional Revenues]

Three months ended 2/28 (USD millions) | Q3 FY2026 | Q3 FY2025 | % change | % change c-n
---|---|---|---|---
North America — Footwear | 3,326 | 3,132 | 6% | 6%
North America — Apparel | 1,480 | 1,510 | -2% | -2%
North America — Equipment | 220 | 222 | -1% | -1%
North America — Total | 5,026 | 4,864 | 3% | 3%
EMEA — Footwear | 1,789 | 1,742 | 3% | -7%
EMEA — Apparel | 926 | 913 | 1% | -8%
EMEA — Equipment | 159 | 156 | 2% | -8%
EMEA — Total | 2,874 | 2,811 | 2% | -7%
Greater China — Footwear | 1,187 | 1,282 | -7% | -10%
Greater China — Apparel | 397 | 412 | -4% | -7%
Greater China — Equipment | 31 | 39 | -21% | -22%
Greater China — Total | 1,615 | 1,733 | -7% | -10%
APLA — Footwear | 1,051 | 1,052 | 0% | -3%
APLA — Apparel | 381 | 358 | 6% | 4%
APLA — Equipment | 58 | 60 | -3% | -7%
APLA — Total | 1,490 | 1,470 | 1% | -2%
Global Brand Divisions | 7 | 12 | -42% | -37%
TOTAL NIKE BRAND | 11,012 | 10,890 | 1% | -2%
Converse | 264 | 405 | -35% | -37%
Corporate | 3 | (26) | — | —
TOTAL NIKE, INC. REVENUES | 11,279 | 11,269 | 0% | -3%
NIKE Brand — Footwear | 7,353 | 7,208 | 2% | -1%
NIKE Brand — Apparel | 3,184 | 3,193 | 0% | -4%
NIKE Brand — Equipment | 468 | 477 | -2% | -6%
NIKE Brand — Global Brand Divisions | 7 | 12 | -42% | -37%
TOTAL NIKE BRAND REVENUES | 11,012 | 10,890 | 1% | -2%

Nine months ended 2/28 (USD millions) | 9M FY2026 | 9M FY2025 | % change | % change c-n
---|---|---|---|---
North America — Footwear | 10,087 | 9,580 | 5% | 5%
North America — Apparel | 4,765 | 4,534 | 5% | 5%
North America — Equipment | 827 | 755 | 10% | 10%
North America — Total | 15,679 | 14,869 | 5% | 5%
EMEA — Footwear | 5,822 | 5,676 | 3% | -3%
EMEA — Apparel | 3,228 | 3,042 | 6% | 0%
EMEA — Equipment | 547 | 539 | 1% | -5%
EMEA — Total | 9,597 | 9,257 | 4% | -2%
Greater China — Footwear | 3,250 | 3,731 | -13% | -14%
Greater China — Apparel | 1,201 | 1,244 | -3% | -5%
Greater China — Equipment | 99 | 135 | -27% | -27%
Greater China — Total | 4,550 | 5,110 | -11% | -12%
APLA — Footwear | 3,263 | 3,338 | -2% | -3%
APLA — Apparel | 1,209 | 1,143 | 6% | 5%
APLA — Equipment | 175 | 195 | -10% | -11%
APLA — Total | 4,647 | 4,676 | -1% | -2%
Global Brand Divisions | 25 | 39 | -36% | -34%
TOTAL NIKE BRAND | 34,498 | 33,951 | 2% | 0%
Converse | 930 | 1,335 | -30% | -32%
Corporate | (2) | (74) | — | —
TOTAL NIKE, INC. REVENUES | 35,426 | 35,212 | 1% | -1%
NIKE Brand — Footwear | 22,422 | 22,325 | 0% | -1%
NIKE Brand — Apparel | 10,403 | 9,963 | 4% | 2%
NIKE Brand — Equipment | 1,648 | 1,624 | 1% | -1%
NIKE Brand — Global Brand Divisions | 25 | 39 | -36% | -34%
TOTAL NIKE BRAND REVENUES | 34,498 | 33,951 | 2% | 0%

- The Q3 Divisional Revenues table carries no Jordan Brand footnote (the Q4 table does, for the full year). Jordan Brand revenue for Q3 or the nine months: not disclosed.

### 9e. Q3 FY2026 EBIT by segment [Q3 FY2026 release, EBIT table]

Segment (USD millions) | Q3 FY2026 | Q3 FY2025 | % change | 9M FY2026 | 9M FY2025 | % change
---|---|---|---|---|---|---
North America | 981 | 1,103 | -11% | 3,376 | 3,690 | -9%
Europe, Middle East & Africa | 515 | 480 | 7% | 1,983 | 2,103 | -6%
Greater China | 467 | 421 | 11% | 1,035 | 1,298 | -20%
Asia Pacific & Latin America | 332 | 346 | -4% | 1,071 | 1,208 | -11%
Global Brand Divisions | (1,209) | (1,093) | -11% | (3,473) | (3,453) | -1%
TOTAL NIKE BRAND EBIT | 1,086 | 1,257 | -14% | 3,992 | 4,846 | -18%
Converse | (40) | 39 | -203% | (5) | 213 | -102%
Corporate | (411) | (470) | 13% | (1,458) | (1,577) | 8%
TOTAL NIKE, INC. EBIT | 635 | 826 | -23% | 2,529 | 3,482 | -27%
Interest (income) expense, net | (15) | (18) | — | (42) | (85) | —
Income tax expense | 130 | 50 | 160% | 532 | 559 | -5%
NET INCOME | 520 | 794 | -35% | 2,039 | 3,008 | -32%
Net income margin | 4.6% | 7.0% | | 5.8% | 8.5% |
EBIT margin | 5.6% | 7.3% | | 7.1% | 9.9% |

- (computed) 9M FY2026 EBIT 2,529 + Q4 FY2026 EBIT 1,321 = 3,850 = FY2026 EBIT; North America 3,376 + 2,000 = 5,376; Converse (5) + 23 = 18; Corporate (1,458) + (565) = (2,023).

### 9f. Side-by-side, Q4 FY2026 vs Q3 FY2026 (each quarter's own year-over-year % as the releases print it; no sequential % is computed)

Line (USD millions unless stated) | Q3 FY2026 (quarter ended Feb 28, 2026) | Q3 YoY reported / c-n | Q4 FY2026 (quarter ended May 31, 2026) | Q4 YoY reported / c-n
---|---|---|---|---
Total NIKE, Inc. revenues | 11,279 | 0% / -3% | 10,972 | -1% / -4%
NIKE Brand revenues | 11,012 | 1% / -2% | 10,724 | 0% / -3%
Wholesale revenues (text) | $6.5 billion | up 5 / up 1 percent | $6.6 billion | up 4 / up 1 percent
NIKE Direct revenues (text) | $4.5 billion | down 4 / down 7 percent | $4.1 billion | down 7 / down 9 percent
NIKE Brand Digital (text) | n/a | "9 percent decrease" | n/a | "12 percent decrease"
NIKE-owned stores (text) | n/a | "5 percent decrease" | n/a | "7 percent decrease"
North America revenue | 5,026 | 3% / 3% | 4,832 | 3% / 3%
EMEA revenue | 2,874 | 2% / -7% | 2,975 | -1% / -6%
Greater China revenue | 1,615 | -7% / -10% | 1,297 | -12% / -17%
APLA revenue | 1,490 | 1% / -2% | 1,596 | 1% / -1%
Converse revenue | 264 | -35% / -37% | 244 | -32% / -34%
NIKE Brand Footwear | 7,353 | 2% / -1% | 7,103 | -1% / -4%
NIKE Brand Apparel | 3,184 | 0% / -4% | 3,046 | 1% / -1%
NIKE Brand Equipment | 468 | -2% / -6% | 551 | -3% / -5%
Gross margin | 40.2% | "decreased 130 basis points" | 49.2% | "increased 890 basis points", ~900 bp of it IEEPA recovery
Gross-margin driver named | "higher tariffs in North America" | | "expected recovery of the IEEPA tariffs" ($986 million) |
Demand creation expense | 1,090 | 0% | 1,203 | -4%
Operating overhead expense | 2,887 | 3% | 2,879 | -1%
Total selling and administrative expense | 3,977 | 2% | 4,082 | -2%
SG&A % of revenues | 35.3% | | 37.2% |
North America EBIT | 981 | -11% | 2,000 (incl. 965 IEEPA) | 91%
EMEA EBIT | 515 | 7% | 434 | -8%
Greater China EBIT | 467 | 11% | 243 | -20%
APLA EBIT | 332 | -4% | 316 | -1%
Global Brand Divisions EBIT | (1,209) | -11% | (1,130) | 9%
Converse EBIT | (40) | -203% | 23 (incl. 21 IEEPA) | -15%
Corporate EBIT | (411) | 13% | (565) | 10%
Total NIKE, Inc. EBIT | 635 | -23% | 1,321 | 346%
EBIT margin | 5.6% | | 12.0% |
Effective tax rate | 20.0% | | 19.6% |
Net income | 520 | -35% | 1,069 | 407%
Diluted EPS | $0.35 | -35% | $0.72 (incl. $0.52 IEEPA) | 414%
Diluted shares (millions) | 1,481.6 | | 1,482.9 |
Inventories (period end) | 7,487 | -1% | 7,501 | 0%
Inventory driver named | "decrease in units and product mix shifts, partially offset by increased product costs, primarily due to higher tariffs in North America" | | "an increase in units, offset by shifts in product mix" |
Cash and equivalents (period end) | 6,660 | -23% | 7,563 | 1%
Short-term investments | 1,397 | -22% | 1,464 | -13%
Cash + short-term investments (text) | $8.1 billion, "down approximately $2.3 billion" | | $9.0 billion, "down approximately $0.1 billion" |
Accounts receivable, net | 5,369 | 20% | 5,931 | 26%
Current portion of long-term debt / Long-term debt | 999 / 7,030 | | 2,000 / 5,942 |
Shareholders' equity | 14,090 | 1% | 14,865 | 13%
Dividends paid in the quarter (text) | ~$609 million, up 3 percent | | ~$609 million, up 3 percent |
Dividends declared per share | $0.410 | | $0.410 |
Share repurchases in the quarter | not quantified (repurchases mentioned in the cash sentence) | | not stated for the quarter; FY2026 total $123 million / 1.8 million shares |

[Q3 FY2026 release, all sections] [Q4 FY2026 release, all sections]

## 10. Footnotes and definitions from the schedules

- Global Brand Divisions, revenue side (Divisional Revenues footnote 2, both releases, verbatim): "Global Brand Divisions revenues include NIKE Brand licensing and other miscellaneous revenues that are not part of a geographic operating segment." [Q4 FY2026 release, Divisional Revenues footnote 2] [Q3 FY2026 release, Divisional Revenues footnote 2]
- Global Brand Divisions, cost side (EBIT footnote 3 in Q4, footnote 2 in Q3, verbatim): "Global Brand Divisions primarily represents costs, including product creation and design expenses, that are centrally managed for the NIKE Brand, as well as costs associated with NIKE Direct global digital operations and enterprise technology. Global Brand Divisions revenues include NIKE Brand licensing and other miscellaneous revenues that are not part of a geographic operating segment." [Q4 FY2026 release, EBIT table footnote 3] [Q3 FY2026 release, EBIT table footnote 2]
- Corporate, revenue side (Divisional Revenues footnote 4 in Q4, footnote 3 in Q3, verbatim): "Corporate revenues primarily consist of foreign currency hedge gains and losses related to revenues generated by entities within the NIKE Brand geographic operating segments and Converse, but managed through the Company's central foreign exchange risk management program." [Q4 FY2026 release, Divisional Revenues footnote 4] [Q3 FY2026 release, Divisional Revenues footnote 3]
- Corporate, EBIT side (EBIT footnote 4 in Q4, footnote 3 in Q3, verbatim): "Corporate consists primarily of unallocated general and administrative expenses, including expenses associated with centrally managed departments; depreciation and amortization related to the Company's corporate headquarters; unallocated insurance, benefit and compensation programs, including stock-based compensation; and certain foreign currency gains and losses, including certain hedge gains and losses." [Q4 FY2026 release, EBIT table footnote 4] [Q3 FY2026 release, EBIT table footnote 3]
- NIKE Direct: the release does not define it. The text decomposes NIKE Direct into "NIKE Brand Digital" and "NIKE-owned stores" (§1b, §9a); the formal definition is in the 10-K. Not defined in the release.
- Currency-neutral and EBIT definitions: §8.
- IEEPA footnote: §1c (Q4 only; the Q4 EBIT table attaches footnote 2 to the North America and Converse rows).
- Jordan Brand footnote: §2a (Q4 only, full year only).
- Restatement or reclassification: neither release contains any restatement, recast or reclassification note; the nine-month FY2026 figures in the Q3 release plus Q4 reconcile exactly to the FY2026 figures in the Q4 release (§9b, §9e). Footnote numbering shifts between the two releases only because Q4 adds the IEEPA and Jordan footnotes. The Q3 balance sheet shows a "Notes payable" row (— vs 4) that the Q4 balance sheet omits entirely.
- The headline asterisk: "* Non-GAAP financial measure. See additional information in the accompanying Divisional Revenues table." [Q4 FY2026 release, footnote after Forward-Looking Statements] [Q3 FY2026 release, same]

## 11. Release-only items (not in the 10-K/10-Q financial statements)

- NIKE Brand Digital: "12 percent decrease" in Q4 FY2026 and "12 percent decrease" for FY2026; "9 percent decrease" in Q3 FY2026. NIKE-owned stores: "7 percent decrease" in Q4, "4 percent decrease" for FY2026, "5 percent decrease" in Q3. No dollar amounts, no basis stated. [Q4 FY2026 release, Fourth Quarter Income Statement Review; Fiscal 2026 Income Statement Review] [Q3 FY2026 release, Third Quarter Income Statement Review]
- Wholesale and NIKE Direct quarterly revenue with reported and currency-neutral growth (§2b, §9f).
- IEEPA recovery split by segment ($965 million North America, $21 million Converse), the "approximately 900 basis point" gross-margin effect, the $0.52 EPS effect, and "approximately $0.3 billion of cash received from IEEPA tariff recoveries" (§1c).
- Inventory composition statements: Q4 "an increase in units, offset by shifts in product mix"; Q3 "a decrease in units and product mix shifts, partially offset by increased product costs, primarily due to higher tariffs in North America" (§4, §9a).
- CFO wording on the marketplace: "an increasingly challenging operating environment, where sell-through remains challenged" (Q4); "Win Now actions will continue to impact results over the balance of the calendar year" (Q3) (§1, §9a).
- Dividend track record: "24 consecutive years of increasing dividend payouts" (Q3 release only) (§9a).
- Jordan Brand FY2026 revenue $7,034 million vs $7,270 million (§2a).
- Store counts: not disclosed in either release. Order book / futures / wholesale order comments: not disclosed. Digital revenue in dollars: not disclosed. Headcount: not disclosed. Marketplace or partner names: none in either release.

## Sources

Tag | Cached file (this folder) | Origin
---|---|---
[Q4 FY2026 release, <section or table>] | `press-release.txt` | 8-K Exhibit 99.1, accession 0000320187-26-000076, filed 2026-06-30: https://www.sec.gov/Archives/edgar/data/320187/000032018726000076/q4fy26exhibit991er.htm (same document as the IR PDF https://s1.q4cdn.com/806093406/files/doc_financials/2026/q4/Q4-FY26_Press-Release_FINAL.pdf; no printed page numbers, so tags name sections/tables)
[Q4 FY2026 schedules, <table>] | `supplemental.txt` | https://s1.q4cdn.com/806093406/files/doc_financials/2026/q4/Q4-FY26_Combined-Tables.pdf ("Nike, Inc. Q4FY26 Financial Schedules & Key Financial Metrics"; 4 pages = the release's four tables; `pdftotext -layout`; no printed page numbers)
[Q3 FY2026 release, <section or table>] | `press-release-FY2026-Q3.txt` | 8-K Exhibit 99.1, accession 0000320187-26-000026, filed 2026-03-31: https://www.sec.gov/Archives/edgar/data/320187/000032018726000026/q3fy26exhibit991er.htm (same document as https://s1.q4cdn.com/806093406/files/doc_financials/2026/q3/Q3-26-Press-Release-FINAL-42.pdf; the separate schedules PDF Q3-26-Press-Release-FINAL-schedules-only.pdf is a subset of it and was not cached separately; no printed page numbers)
