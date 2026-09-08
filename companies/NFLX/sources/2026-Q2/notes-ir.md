# Netflix (NFLX) — Q2 2026 IR gatherer notes: shareholder letter + "Website Financials" workbook (+ Q1 2026 and Q4 2025 letters for the guidance history and FY2025 actuals)

- Quarter: Q2 2026 (quarter ended June 30, 2026). Fiscal year = calendar year. Company: Netflix, Inc., Nasdaq NFLX, CIK 0001065280.
- As-of cutoff: 2026-07-17. Q2 2026 letter is dated "July 16, 2026" (pdfinfo CreationDate 2026-07-16 17:40 UTC); Q1 2026 letter "April 16, 2026" (CreationDate 2026-04-16); Q4 2025 letter "January 20, 2026" (CreationDate 2026-01-20). Nothing published after 2026-07-17 was fetched, read, or used.
- Netflix publishes **no earnings press release and no slide deck**. The quarterly shareholder letter is the release (also filed as Exhibit 99.1 to the Item 2.02 8-K), and a "Website Financials" Excel workbook carries the statements and supplementary schedules. `shareholder-letter.txt` therefore stands in for `press-release.txt`; there is no `slides.txt`.
- Cached text: `shareholder-letter.txt` (Q2 2026 letter, 14 PDF pages), `shareholder-letter-2026-Q1.txt` (Q1 2026 letter, 14 PDF pages), `shareholder-letter-2025-Q4.txt` (Q4 2025 letter, 17 PDF pages), `financials-xlsx.txt` (openpyxl dump of `Q2-26-Website-Financials.xlsx`, five sheets). See `MANIFEST-ir.md`.
- Tags: `[Q2 2026 letter, p.N]` = shareholder-letter.txt; `[Q1 2026 letter, p.N]` = shareholder-letter-2026-Q1.txt; `[Q4 2025 letter, p.N]` = shareholder-letter-2025-Q4.txt; `[Q2 2026 financials xlsx, <sheet>]` = financials-xlsx.txt.
- Page-number convention: **p.N = PDF page number.** The narrative pages (Q2 and Q1 letters pp.1–8; Q4 2025 letter pp.1–11) carry no printed page number (the lone digits on those pages are footnote markers). The financial-statement pages (Q2/Q1 pp.9–14; Q4 pp.12–17) carry printed page numbers that equal the PDF page numbers, so the two conventions coincide wherever a printed number exists.
- Charts and images: the Q2 2026 and Q1 2026 letters contain **no charts**; the only raster images are the Netflix logo (footer of every page). The summary-results table (p.1) and the Regional Breakdown table (p.7) are text tables and every figure survived `pdftotext -layout`. The Q4 2025 letter has one large raster image on p.5 (a screenshot of the TV UI "Holiday Magic" collection row; no data) and text tables on p.7 (stock performance) and p.8 (Regional Breakdown). No OCR was needed. No page is a two-column narrative layout (the IR/PR contact block sits side by side and extracted cleanly), so no reading-order copy was made.
- Units: letter summary tables and regional tables are USD millions (EPS in dollars; shares in millions); the statements in the letters and the workbook are USD thousands. Percentages in the workbook are stored as fractions (e.g., 0.1 {10.0%}). All figures unaudited. Every number below is copied verbatim; anything derived is labelled "computed".
- Text quirks: the letters use curly apostrophes and contain U+200B zero-width spaces after bullet glyphs and in the footer lines; the cached text is byte-identical to the `pdftotext -layout` output. In the Q2 letter's Q2'26 regional and constant-currency tables, the totals row appears only on p.13.

## 1. Headline results Q2 2026 (with Q2 2025 and Q1 2026 comparatives)

Letter headline bullets, verbatim: "Q2 revenue grew 13% year over year (+12% on a FX-neutral basis) to $12.6B, and operating margin was 33%. Both were in-line with our guidance." "For 2026, we've narrowed our forecasted revenue range to $51.0-$51.4B and continue to forecast an operating margin of 31.5%, both consistent with our prior guidance." [Q2 2026 letter, p.1]

Summary results table (USD millions except per share; "Shares (FD)" = diluted weighted-average shares, millions). [Q2 2026 letter, p.1] Q1'25 column from [Q1 2026 letter, p.1]; Q4'24 column from [Q4 2025 letter, p.1].

| | Q4'24 | Q1'25 | Q2'25 | Q3'25 | Q4'25 | Q1'26 | Q2'26 | Q3'26 forecast |
|---|---|---|---|---|---|---|---|---|
| Revenue | $10,247 | $10,543 | $11,079 | $11,510 | $12,051 | $12,250 | $12,560 | $12,860 |
| Y/Y % growth | 16.0% | 12.5% | 15.9% | 17.2% | 17.6% | 16.2% | 13.4% | 11.7% |
| Operating income | $2,273 | $3,347 | $3,775 | $3,248 | $2,957 | $3,957 | $4,193 | $4,268 |
| Operating margin | 22.2% | 31.7% | 34.1% | 28.2% | 24.5% | 32.3% | 33.4% | 33.2% |
| Net income | $1,869 | $2,890 | $3,125 | $2,547 | $2,419 | $5,283 | $3,401 | $3,452 |
| Diluted EPS | $0.43 | $0.66 | $0.72 | $0.59 | $0.56 | $1.23 | $0.80 | $0.82 |
| Net cash provided by operating activities | $1,537 | $2,789 | $2,423 | $2,825 | $2,112 | $5,290 | $1,744 | — |
| Free cash flow | $1,378 | $2,661 | $2,267 | $2,660 | $1,872 | $5,094 | $1,525 | — |
| Shares (FD) | 4,378 | 4,370 | 4,349 | 4,340 | 4,317 | 4,298 | 4,261 | — |

- Revenue: "Q2 revenue of $12.6B was in-line with forecast and grew 13% year over year (+12% on a foreign exchange (F/X) neutral basis), driven primarily by membership growth, pricing and increased ad revenue. We delivered double digit revenue growth in all regions, surpassing the quarterly revenue mark of $4.0B in EMEA and $1.5B in both LATAM and APAC. In UCAN, Q2 revenue growth of 10% reflects only a partial quarter impact from our recent price change, which has gone well and as expected." [Q2 2026 letter, p.2]
- Operating income and margin: "Operating income in Q2 was $4.2B, up 11% year over year, and operating margin was 33.4% versus 34.1% in Q2'25. Q2 operating income and margin were slightly ahead of forecast due to the timing of expenses. As we noted in previous letters, operating income in Q2 grew slower than revenue because our content amortization growth is higher in the first half of the year; we continue to expect content amortization to grow slower in the second half of the year and to increase ~10% for 2026." [Q2 2026 letter, p.2]
- EPS: "Diluted EPS for the quarter amounted to $0.80 vs. $0.72 in Q2'25 (+11% year over year), slightly above our forecast." [Q2 2026 letter, p.2] Split footnote, verbatim: "Share and per share amounts have been retroactively adjusted to reflect the ten-for-one forward stock split which was effected on November 14, 2025." [Q2 2026 letter, p.9]
- Statement of operations, three months ended June 30, 2026 / March 31, 2026 / June 30, 2025 (USD thousands): Revenues 12,559,938 / 12,249,757 / 11,079,166; Cost of revenues 6,036,965 / 5,888,238 / 5,325,311; Sales and marketing 823,838 / 842,217 / 713,265; Technology and development 1,007,675 / 959,696 / 824,683; General and administrative 498,850 / 602,609 / 441,213; Operating income 4,192,610 / 3,956,997 / 3,774,694; Interest expense (175,685) / (262,077) / (182,649); Interest and other income (expense) 51,661 / 2,852,166 / 39,630; Income before income taxes 4,068,586 / 6,547,086 / 3,631,675; Provision for income taxes (667,172) / (1,264,295) / (506,262); Net income 3,401,414 / 5,282,791 / 3,125,413; EPS basic $0.81 / $1.25 / $0.74; diluted $0.80 / $1.23 / $0.72; weighted-average shares basic 4,189,303 / 4,222,787 / 4,252,112; diluted 4,261,300 / 4,298,437 / 4,348,825. [Q2 2026 letter, p.9]
- Six months ended June 30, 2026 vs 2025 (USD thousands): Revenues 24,809,695 vs 21,621,967; Operating income 8,149,607 vs 7,121,693; Net income 8,684,205 vs 6,015,764; diluted EPS $2.03 vs $1.38; diluted shares 4,279,776 vs 4,359,167. [Q2 2026 letter, p.9]
- computed: Q2'26 operating income growth 4,192,610 / 3,774,694 − 1 = +11.1%; net income growth 3,401,414 / 3,125,413 − 1 = +8.8%; effective tax rate 667,172 / 4,068,586 = 16.4% (Q1'26: 1,264,295 / 6,547,086 = 19.3%; Q2'25: 506,262 / 3,631,675 = 13.9%).
- Cash flow: "Net cash generated from operating activities was $1.7B vs $2.4B in the prior year period. Free cash flow (FCF) in Q2'26 totaled $1.5B vs. $2.3B in Q2'25. This included higher cash tax payments due in part to the Warner Bros. termination fee." [Q2 2026 letter, p.6]
- FCF definition, verbatim (footnote 6): "Defined as cash provided by (used in) operating activities less purchases of property and equipment." [Q2 2026 letter, p.6]
- FCF reconciliation (USD thousands; Q2'26 / Q1'26 / Q2'25 / 6M'26 / 6M'25): Net cash provided by operating activities 1,743,812 / 5,290,205 / 2,423,258 / 7,034,017 / 5,212,457; Purchases of property and equipment (218,644) / (196,130) / (155,889) / (414,774) / (284,166); Non-GAAP free cash flow 1,525,168 / 5,094,075 / 2,267,369 / 6,619,243 / 4,928,291. [Q2 2026 letter, p.12]
- Cash and debt: "We ended the quarter with gross debt of $14.4B and cash and cash equivalents of $9.1B. We have $1B of debt maturing later this year, which we plan to refinance." [Q2 2026 letter, p.6] Balance sheet June 30, 2026 vs December 31, 2025 (USD thousands): Cash and cash equivalents 9,099,232 vs 9,033,681; Short-term investments 28,678 vs 28,678; Short-term debt 2,483,758 vs 998,865; Long-term debt 11,825,548 vs 13,463,971. [Q2 2026 letter, p.10] Net debt reconciliation as of June 30, 2026: Total debt 14,309,306; Add: Debt issuance costs and original issue discount 48,985; Add: Fair value hedging adjustment 13,809; Less: Cash and cash equivalents (9,099,232); Less: Short-term investments (28,678); Net debt 5,244,190. [Q2 2026 letter, p.14]
- Buybacks: "In April, our Board of Directors authorized the repurchase of an additional $25B of our stock on top of the $6.8B of capacity we had remaining as of the end of Q1. In Q2, we bought back $4.7B of stock, our largest quarter of share repurchases, and we currently have $27.1B of capacity left in our remaining authorizations." [Q2 2026 letter, p.6] Cash-flow line "Repurchases of common stock": (4,714,403) Q2'26; (1,270,588) Q1'26; (1,654,327) Q2'25; (5,984,991) six months 2026; (5,190,723) six months 2025. [Q2 2026 letter, p.11] Number of shares repurchased in Q2 2026: not disclosed in the Q2 2026 letter or the workbook (the Q1 2026 letter gave 13.5M shares for Q1; see §7).
- Total streaming content obligations (supplemental, USD thousands): 25,106,705 at June 30, 2026 vs 24,039,228 at December 31, 2025. Definition, verbatim: "Total streaming content obligations are comprised of content liabilities included in "Current content liabilities" and "Non-current content liabilities" on the Consolidated Balance Sheets and obligations that are not reflected on the Consolidated Balance Sheets as they did not yet meet the criteria for recognition." [Q2 2026 letter, p.10]
- Shares outstanding at period end: not disclosed in the letter or the workbook (only weighted averages).

## 2. Revenue by region (UCAN, EMEA, LATAM, APAC)

Regional Breakdown tables (USD millions; growth as printed). Q2'25–Q2'26 from [Q2 2026 letter, p.7]; Q1'25 from [Q1 2026 letter, p.7]; Q4'24 from [Q4 2025 letter, p.8]. The workbook's "Regional Information" sheet carries the same quarters in thousands with the full constant-currency bridge (see §8.4).

| Region | | Q4'24 | Q1'25 | Q2'25 | Q3'25 | Q4'25 | Q1'26 | Q2'26 |
|---|---|---|---|---|---|---|---|---|
| UCAN | Revenue | $4,517 | $4,617 | $4,929 | $5,072 | $5,339 | $5,245 | $5,432 |
| | Y/Y % growth | 15% | 9% | 15% | 17% | 18% | 14% | 10% |
| | F/X neutral Y/Y % growth | 15% | 9% | 15% | 17% | 18% | 14% | 10% |
| EMEA | Revenue | $3,288 | $3,405 | $3,538 | $3,699 | $3,873 | $3,998 | $4,034 |
| | Y/Y % growth | 18% | 15% | 18% | 18% | 18% | 17% | 14% |
| | F/X neutral Y/Y % growth | 16% | 16% | 16% | 15% | 15% | 12% | 11% |
| LATAM | Revenue | $1,230 | $1,262 | $1,307 | $1,371 | $1,418 | $1,497 | $1,584 |
| | Y/Y % growth | 6% | 8% | 9% | 10% | 15% | 19% | 21% |
| | F/X neutral Y/Y % growth | 35% | 27% | 23% | 20% | 20% | 18% | 16% |
| APAC | Revenue | $1,212 | $1,259 | $1,305 | $1,369 | $1,421 | $1,509 | $1,510 |
| | Y/Y % growth | 26% | 23% | 24% | 21% | 17% | 20% | 16% |
| | F/X neutral Y/Y % growth | 24% | 26% | 23% | 20% | 19% | 19% | 18% |

- Regional table footnote, verbatim: "F/X Neutral revenue growth excludes the year over year effect of foreign exchange rate movements and the impact of hedging gains/losses realized as revenues. Assumes foreign exchange rates remained constant with foreign exchange rates from each of the corresponding months of the prior-year period." [Q2 2026 letter, p.7]
- Consolidated constant-currency totals (USD thousands; As Reported | Constant Currency Adjustment | Hedging (Gains) Losses Included in Revenues | Constant Currency Revenues | prior-year As Reported | prior-year Hedging | prior-year Revenues Less Hedging Impact | Reported Change | Constant Currency Change): Q2'26 vs Q2'25: 12,559,938 | (174,187) | 47,630 | 12,433,381 | 11,079,166 | 37,385 | 11,116,551 | 13% | 12% [Q2 2026 letter, p.13]. Q1'26 vs Q1'25: 12,249,757 | (540,512) | 132,517 | 11,841,762 | 10,542,801 | (164,796) | 10,378,005 | 16% | 14% [Q1 2026 letter, p.13]. Q4'25 vs Q4'24: 12,050,762 | (167,726) | 89,189 | 11,972,225 | 10,246,513 | (53,767) | 10,192,746 | 18% | 17% [Q4 2025 letter, p.16].
- FY2025 regional revenue (USD thousands, As Reported; Reported Change; Constant Currency Change): UCAN 19,957,152 (15%; 15%); EMEA 14,514,646 (17%; 16%); LATAM 5,357,521 (11%; 23%); APAC 5,353,717 (21%; 22%). FY2024 As Reported: UCAN 17,359,369; EMEA 12,387,035; LATAM 4,839,816; APAC 4,414,746. [Q2 2026 financials xlsx, Regional Information]
- Paid memberships: **not reported** in the Q2 2026 letter, the Q1 2026 letter or the workbook (no membership count, no regional memberships, no net additions). The last count in the three letters is in the Q4 2025 letter: "we crossed the 325M paid memberships milestone during the quarter" [Q4 2025 letter, p.1] and "With over 325M paid memberships, we're now serving an audience approaching one billion people globally" [Q4 2025 letter, p.2]. The Q2 2026 letter describes the audience only as "a massive audience (approaching 1B people)" [Q2 2026 letter, p.3]; the Q1 2026 letter: "we're now entertaining an audience approaching 1 billion people ... we account for an estimated ~5% of TV view share globally, and as of the end of 2025 we penetrated less than 45% of our Total Addressable Market (TAM) of broadband households" [Q1 2026 letter, p.3]. None of the three letters states why membership counts are no longer published; the recurring sentence is "Our primary financial metrics are revenue for growth and operating margin for profitability." [Q2 2026 letter, p.2] [Q1 2026 letter, p.2] [Q4 2025 letter, p.2] Membership growth is still cited qualitatively: "driven primarily by membership growth, pricing and increased ad revenue" [Q2 2026 letter, p.2]; "Japan was the largest contributor to member growth in Q1" [Q1 2026 letter, p.3].
- Average revenue per membership (ARM): not in the Q2 2026 letter or workbook, nor in the Q1 2026 or Q4 2025 letters.

## 3. Guidance, verbatim

### 3.1 Q2 2026 letter (July 16, 2026)

- Q3 2026: "For Q3, we expect revenue growth of 12% (or 11% F/X neutral) driven by growth in memberships, pricing, and ad revenue. We project an operating margin of 33.2% compared with 28.2% in the year ago quarter." [Q2 2026 letter, p.2] Table column "Q3'26 Forecast": Revenue $12,860; Y/Y % growth 11.7%; Operating income $4,268; Operating margin 33.2%; Net income $3,452; Diluted EPS $0.82 (USD millions except per share). [Q2 2026 letter, p.1]
- FY2026: "Our 2026 outlook is consistent with our prior forecast: we are narrowing our revenue forecast to $51.0-$51.4B, which represents 13%-14% growth (~12% F/X neutral), driven by growth in memberships and pricing, and a projected rough doubling of our ads revenue to approximately $3 billion. We continue to anticipate an operating margin of 31.5% for 2026 both on a reported basis and based on F/X rates as of January 1, 2026 vs. 29.5% in 2025. Our forecast implies annual operating income growth of 20%+ for 2026." [Q2 2026 letter, p.2]
- FY2026 FCF and content ratio: "For the full year, we continue to expect FCF of approximately $12.5B, and an annual cash content spend to amortization ratio of ~1.1x." [Q2 2026 letter, p.6]
- Content amortization: "we continue to expect content amortization to grow slower in the second half of the year and to increase ~10% for 2026." [Q2 2026 letter, p.2]
- Ads: "we remain on track to deliver approximately $3 billion in ads revenue in 2026." [Q2 2026 letter, p.5]
- Debt: "We have $1B of debt maturing later this year, which we plan to refinance." [Q2 2026 letter, p.6]
- Live content spend: "in 2026, we expect live programming to account for just over 5% of our content spend but only ~1% of view hours." [Q2 2026 letter, p.3]
- Guidance philosophy, verbatim: "As a reminder, the guidance we provide is our actual internal forecast at the time we report and we strive for accuracy. Our primary financial metrics are revenue for growth and operating margin for profitability. Our goal is to sustain healthy revenue growth, expand operating profit and margin, and deliver growing free cash flow." [Q2 2026 letter, p.2]
- Not given in the Q2 2026 letter: tax rate, capex, interest expense, cash content spend in dollars, Q3 cash flow or FCF, membership or ARM guidance.

### 3.2 Q1 2026 letter (April 16, 2026) — guidance in force for Q2 2026 before this quarter

- Q2 2026: "For Q2, we expect revenue growth of 13% (or 12% F/X neutral). As we noted in last quarter's letter, growth in content amortization will be first-half weighted due to the timing of title launches. We expect Q2 to have the highest year-over-year content amortization growth rate in 2026, before decelerating to mid-to-high single digit growth in the second half of the year. As a result, we forecast Q2 operating margin of 32.6% compared with 34.1% in the year ago quarter. We expect year-over-year operating margin growth in Q3 and Q4 in order to deliver our 2026 margin target." [Q1 2026 letter, p.2] Table column "Q2'26 Forecast": Revenue $12,574; Y/Y % growth 13.5%; Operating income $4,105; Operating margin 32.6%; Net income $3,327; Diluted EPS $0.78. [Q1 2026 letter, p.1]
- FY2026: "Our full year 2026 guidance is unchanged: we forecast 2026 revenue of $50.7B-$51.7B, which represents 12%-14% growth (11%-13% F/X neutral), driven by continued healthy membership growth, pricing and a projected rough doubling of our ads revenue. Similarly, we're still targeting an operating margin of 31.5% for 2026 based on F/X rates as of January 1, 2026 vs. 29.5% in 2025." [Q1 2026 letter, p.2]
- FY2026 FCF: "We now expect 2026 FCF of approximately $12.5B, an increase from our previous projection of $11B due primarily to the after-tax impact of the Warner Bros.-related termination fee. We continue to expect an annual cash content spend to amortization ratio of ~1.1x." [Q1 2026 letter, p.5]
- Ads: "our advertising revenue remains on track to reach $3B in 2026, up 2x year-over-year." [Q1 2026 letter, p.1] "we continue to expect ~$3B in ad revenue this year, up 2x from 2025." [Q1 2026 letter, p.5]
- Q1 2026 actual vs the Q4 letter's Q1 forecast: "Revenue was slightly above our forecast due to higher than forecasted membership growth and favorable F/X movements net of hedging." "Both operating income and margin were slightly above our forecast owing to higher-than-forecasted revenue." "Diluted EPS for the quarter amounted to $1.23 vs. $0.66 in Q1'25 (+86% year over year), above our forecast of $0.76, driven by higher-than-projected operating income and the $2.8B termination fee related to the Warner Bros. transaction, which was recognized in "interest and other income."" [Q1 2026 letter, p.2]

### 3.3 Q4 2025 letter (January 20, 2026) — initial FY2026 guidance and FY2025 actuals

- Q1 2026 forecast (table only; no prose sentence): Revenue $12,157; Y/Y % growth 15.3%; Operating income $3,906; Operating margin 32.1%; Net income $3,264; Diluted EPS $0.76. [Q4 2025 letter, p.1]
- FY2026 revenue: "For 2026, based on F/X rates as of 1/1/2026, we forecast revenue of $50.7B-$51.7B. This represents 12%-14% year over year growth (or 11%-13% F/X neutral growth), driven by increases in membership and pricing plus a projected rough doubling of ad revenue in 2026 vs. 2025." [Q4 2025 letter, p.2]
- FY2026 operating margin: "We're targeting a 2026 operating margin of 31.5% (based on 1/1/26 F/X rates), up from 29.5% in 2025, which includes approximately $275M of acquisition-related expenses. Our margin forecast also reflects content amortization growth of ~10% in 2026, with higher growth in the first half than the second half due to the timing of title launches. As a result, we expect higher operating income growth in the second half of 2026 than in the first half. We still see plenty of room to increase our margins and our intent is to grow our operating margin each year, although the magnitude of margin expansion will vary year-to-year as we balance reinvesting in our business with improving profitability." [Q4 2025 letter, p.2]
- FY2026 FCF: "For 2026, assuming no material swings in F/X, we expect to generate free cash flow of roughly $11B, which assumes a cash content spend to content amortization ratio of ~1.1x." [Q4 2025 letter, p.6]
- Buybacks: "Consistent with that framework, we'll pause our share buybacks to accumulate cash to help fund the pending acquisition of Warner Bros. We remain committed to maintaining a solid investment grade rating." [Q4 2025 letter, p.7]
- FY2025 actuals, verbatim: "For the year, we delivered $45.2B of revenue (+16% year over year, or 17% on a FX-neutral basis) and operating margin of 29.5% (+3 points). Ad revenue rose more than 2.5x to over $1.5B." [Q4 2025 letter, p.1] "We grew revenue 16% to $45B (+17% on a F/X neutral basis) and we increased our operating margin to 29.5% for the year, up from 26.7% in 2024." [Q4 2025 letter, p.2] "For the full year 2025, we produced $10.1B of net cash generated from operating activities and $9.5B of FCF, up from $7.4B and $6.9B, respectively in 2024. FCF was higher than our forecast of $9B (+/- a few hundred million dollars) as the timing of an expected deposit of ~$700M related to our ongoing dispute with the Brazilian tax authorities shifted from 2025 to 2026." [Q4 2025 letter, p.6] "During the quarter we repurchased 18.9M shares for $2.1B, leaving $8.0B remaining under our existing share repurchase authorization. We ended the quarter with gross debt of $14.5B and cash and cash equivalents of $9.0B." [Q4 2025 letter, p.6]
- Q4 2025 results vs forecast: "Despite unfavorable F/X movements during the quarter, revenue was 1% above our guidance due to stronger-than-forecasted membership growth and ad sales." "Operating income in Q4 was $3.0B, up 30% year over year, and operating margin expanded two percentage points year over year to 25% - both slightly ahead of our forecast due primarily to the revenue upside. Diluted EPS amounted to $0.56 vs $0.43 in Q4'24 (+31% year over year), slightly above our forecast (adjusted for our 10-for-1 stock split). Net income included ~$60M of costs (booked in interest expense) related to our recent Warner Bros.-related bridge loan and associated bridge reduction financings (which was not included in our guidance)." [Q4 2025 letter, p.2]
- FY2025 and FY2024 statement figures (USD thousands, twelve months ended December 31): Revenues 45,183,036 vs 39,000,966; Cost of revenues 23,275,329 vs 21,038,464; Sales and marketing 3,301,306 vs 2,917,554; Technology and development 3,391,390 vs 2,925,295; General and administrative 1,888,408 vs 1,702,039; Operating income 13,326,603 vs 10,417,614; Interest expense (776,510) vs (718,733); Interest and other income 172,459 vs 266,776; Provision for income taxes (1,741,351) vs (1,254,026); Net income 10,981,201 vs 8,711,631; EPS basic $2.58 vs $2.03, diluted $2.53 vs $1.98; diluted weighted-average shares 4,343,863 vs 4,392,608. [Q4 2025 letter, p.12] Cash flow FY2025 vs FY2024: Additions to content assets (17,096,617) vs (16,223,617); Amortization of content assets 16,422,166 vs 15,301,517; Net cash provided by operating activities 10,149,273 vs 7,361,364; Purchases of property and equipment (688,220) vs (439,538); Proceeds from issuance of debt — vs 1,794,460; Repayments of debt (1,833,450) vs (400,000); Repurchases of common stock (9,127,167) vs (6,263,746). [Q4 2025 letter, p.14] Non-GAAP free cash flow 9,461,053 vs 6,921,826. [Q4 2025 letter, p.15] Balance sheet December 31, 2025 vs 2024: Cash and cash equivalents 9,033,681 vs 7,804,733; Short-term investments 28,678 vs 1,779,006; Content assets, net 32,778,392 vs 32,452,462; Short-term debt 998,865 vs 1,784,453; Long-term debt 13,463,971 vs 13,798,351; Total stockholders' equity 26,615,488 vs 24,743,567; Total streaming content obligations 24,039,228 vs 23,248,931. [Q4 2025 letter, p.13] Net debt December 31, 2025: Total debt 14,462,836; Add: Debt issuance costs and original issue discount 56,139; Less: Cash (9,033,681); Less: Short-term investments (28,678); Net debt 5,456,616. [Q4 2025 letter, p.17]
- FY2025 cash content spend in dollars: not stated in the letter; the cash-flow line "Additions to content assets" (17,096,617) is the closest disclosed figure. computed: 17,096,617 / 16,422,166 = 1.04x additions-to-amortization for 2025 (the company's "~1.1x" is a 2026 forecast, not a 2025 actual).

### 3.4 Guidance history table

| Guidance item | Q4 2025 letter (Jan 20, 2026) | Q1 2026 letter (Apr 16, 2026) | Q2 2026 letter (Jul 16, 2026) |
|---|---|---|---|
| Next quarter guided | Q1'26 | Q2'26 | Q3'26 |
| Next-quarter revenue (USD M; y/y) | $12,157; 15.3% | $12,574; 13.5% ("13% (or 12% F/X neutral)") | $12,860; 11.7% ("12% (or 11% F/X neutral)") |
| Next-quarter operating income (USD M) | $3,906 | $4,105 | $4,268 |
| Next-quarter operating margin | 32.1% | 32.6% | 33.2% |
| Next-quarter net income (USD M) | $3,264 | $3,327 | $3,452 |
| Next-quarter diluted EPS | $0.76 | $0.78 | $0.82 |
| FY2026 revenue | $50.7B-$51.7B (12%-14%; 11%-13% F/X neutral) | $50.7B-$51.7B (12%-14%; 11%-13% F/X neutral), "unchanged" | $51.0-$51.4B (13%-14%; ~12% F/X neutral), "narrowing" |
| FY2026 operating margin | 31.5% "based on 1/1/26 F/X rates", incl. ~$275M acquisition-related expenses | 31.5% "based on F/X rates as of January 1, 2026" | 31.5% "both on a reported basis and based on F/X rates as of January 1, 2026" |
| FY2026 free cash flow | "roughly $11B" | "approximately $12.5B" (raised for after-tax termination fee) | "approximately $12.5B" |
| Cash content spend to amortization | ~1.1x | ~1.1x | ~1.1x |
| Content amortization growth 2026 | ~10%, first half higher than second | Q2 highest y/y growth, then mid-to-high single digit in H2 | "increase ~10% for 2026", slower in H2 |
| Ad revenue 2026 | "roughly double" (from over $1.5B in 2025) | "~$3B ... up 2x from 2025" | "approximately $3 billion" |
| F/X basis | "F/X rates as of 1/1/2026" | "F/X rates as of January 1, 2026" | "F/X rates as of January 1, 2026" |
| Share repurchases | paused to fund Warner Bros. | resumed; $6.8B remaining | +$25B authorized in April; $27.1B remaining |
| Tax rate, capex, interest, memberships, ARM | not given | not given | not given |

## 4. Content economics as the letter and workbook state them

- Cash content spend: no dollar figure for the quarter, half or year in any of the three letters; the only company statement is the ratio "annual cash content spend to amortization ratio of ~1.1x" for 2026 [Q2 2026 letter, p.6] [Q1 2026 letter, p.5] [Q4 2025 letter, p.6]. The cash-flow statement line "Additions to content assets" is the nearest disclosed series (USD thousands): Q1'25 (3,549,657); Q2'25 (3,835,813); Q3'25 (4,653,935); Q4'25 (5,057,212); FY2025 (17,096,617); Q1'26 (4,846,917); Q2'26 (4,927,523); six months 2026 (9,774,440). [Q2 2026 financials xlsx, Cashflow] FY2024 (16,223,617). [Q4 2025 letter, p.14]
- Content amortization ("Amortization of content assets", USD thousands): Q1'25 3,823,112; Q2'25 3,832,074; Q3'25 4,002,744; Q4'25 4,764,236; FY2025 16,422,166; Q1'26 4,217,900; Q2'26 4,311,309; six months 2026 8,529,209. [Q2 2026 financials xlsx, Cashflow] Six months 2025 7,655,186 [Q2 2026 letter, p.11]; Q4'24 4,161,501; FY2024 15,301,517 [Q4 2025 letter, p.14]. There is no separate content-amortization schedule in the workbook; the cash-flow line is the only source.
- computed: amortization y/y growth Q1'26 4,217,900 / 3,823,112 − 1 = +10.3%; Q2'26 4,311,309 / 3,832,074 − 1 = +12.5%; six months 2026 8,529,209 / 7,655,186 − 1 = +11.4%; Q4'25 4,764,236 / 4,161,501 − 1 = +14.5%; FY2025 16,422,166 / 15,301,517 − 1 = +7.3%.
- computed: additions to content assets ÷ amortization: Q1'25 0.93x; Q2'25 1.00x; Q3'25 1.16x; Q4'25 1.06x; FY2025 1.04x; FY2024 1.06x; Q1'26 1.15x; Q2'26 1.14x; six months 2026 1.15x.
- computed: cost of revenues y/y Q2'26 6,036,965 / 5,325,311 − 1 = +13.4%, the same as revenue growth 12,559,938 / 11,079,166 − 1 = +13.4%.
- Change in content liabilities (USD thousands): Q1'25 (411,253); Q2'25 (214,052); Q3'25 24,262; Q4'25 (9,795); FY2025 (610,838); Q1'26 45,216; Q2'26 (181,794); six months 2026 (136,578). [Q2 2026 financials xlsx, Cashflow]
- Content assets, net (balance sheet, USD thousands): 3/31/25 32,040,839; 6/30/25 32,089,394; 9/30/25 32,639,879; 12/31/25 32,778,392; 3/31/26 33,376,295; 6/30/26 33,837,573. [Q2 2026 financials xlsx, Balance Sheet]
- Content liabilities (current / non-current, USD thousands): 3/31/25 4,128,905 / 1,696,662; 6/30/25 4,091,770 / 1,606,404; 9/30/25 4,102,640 / 1,591,973; 12/31/25 4,084,854 / 1,579,476; 3/31/26 4,052,278 / 1,626,498; 6/30/26 3,866,522 / 1,625,600. [Q2 2026 financials xlsx, Balance Sheet]
- Total streaming content obligations (USD thousands): 12/31/24 23,248,931 [Q4 2025 letter, p.13]; 12/31/25 24,039,228; 3/31/26 24,139,431 [Q1 2026 letter, p.10]; 6/30/26 25,106,705 [Q2 2026 letter, p.10].
- Live programming share of spend: "in 2026, we expect live programming to account for just over 5% of our content spend but only ~1% of view hours. Yet, live event programming accounted for six of the top 10 new member sign-up days over the last five years (and we've only been doing live events since 2023)." [Q2 2026 letter, p.3]
- Where the budget goes: "We continue to focus the vast majority of our content budget on core series and films." [Q1 2026 letter, p.3] "our single largest area of spend—content" [Q1 2026 letter, p.4]
- Why margins expand, in the company's words: "Our goal is to sustain healthy revenue growth, expand operating profit and margin, and deliver growing free cash flow." [Q2 2026 letter, p.2] "We still see plenty of room to increase our margins and our intent is to grow our operating margin each year, although the magnitude of margin expansion will vary year-to-year as we balance reinvesting in our business with improving profitability." [Q4 2025 letter, p.2] "Better monetization enables us to invest more in content and the product experience, which increases member value and engagement, and in turn supports long-term revenue and profit growth and our ability to reinvest to further improve Netflix – driving a virtuous cycle." [Q1 2026 letter, p.4] The seasonal explanation: "operating income in Q2 grew slower than revenue because our content amortization growth is higher in the first half of the year" [Q2 2026 letter, p.2]; "Our forecast implies annual operating income growth of 20%+ for 2026." [Q2 2026 letter, p.2] The letters do not use the phrases "operating leverage" or "grow revenue faster than costs".
- Licensing (Q4 2025 letter): "Starting this month, members will be able to enjoy new release live action films from our new US licensing partnership with Universal. This deal complements our existing licensing deal for animated films from Universal's animation studios, Illumination and DreamWorks Animation. We've also licensed ~20 shows from Paramount including Matlock and King of Queens for international territories and Seal Team, Watson and Mayor of Kingstown for US and international territories. Additionally, we recently announced we expanded our pay 1 film pact with Sony Pictures Entertainment from a US to a global deal ... with full global availability in early 2029." [Q4 2025 letter, p.4] Non-branded viewing decline: "This decrease primarily reflected a lower volume of licensed, second-run content across most regions following an elevated period of licensing during 2023-2024 as a result of the WGA strike, which temporarily shut down new production." [Q4 2025 letter, p.3]

## 5. Advertising

- Q2 2026 letter, everything it says: "driven primarily by membership growth, pricing and increased ad revenue" [p.2]; "a projected rough doubling of our ads revenue to approximately $3 billion" [p.2]; "enhance ads capabilities for brands" [p.1]. Ads paragraph, verbatim: "In our ads business, we continue to invest in developing a premium ad experience which delivers highly engaged and attentive audiences to advertisers. In Q2, we expanded our AI-powered tools across the full advertising lifecycle, from planning and creative production to campaign management, optimization, and reporting. We're also automating more of the workflow around how advertisers transact with us by extending programmatic access to Pause Ads and live inventory this summer. This reduces the manual effort that has historically limited access for smaller buyers, opening Netflix to a broader range of advertisers over time. These investments enhance the value of our existing inventory and lay the groundwork for the next phase of growth in our ads business." [Q2 2026 letter, p.5] Monetization paragraph, verbatim: "Building out our ads business continues to be a top priority and we remain on track to deliver approximately $3 billion in ads revenue in 2026. Our US upfront negotiations are in advanced stages, and we expect commitments to close in the next few weeks. We are seeing strong interest in our Live events lineup — Women's World Cup, an expanded NFL slate, WWE, MLB events and more — alongside continued demand for our unparalleled breadth of entertainment titles. The growth in our ads business is being fueled by the strength and variety of our slate combined with our investments in AI powered tools and workflows, the Netflix Ads Suite and broader programmatic capabilities." [Q2 2026 letter, p.5]
- Not in the Q2 2026 letter or workbook: quarterly ad revenue in dollars, ad revenue as a percent of revenue, ad-tier share of sign-ups, ad-tier price, advertiser count, upfront dollar results (negotiations described as still open), named programmatic partners, named measurement partners.
- Q1 2026 letter: "Our ads plan (priced at $8.99 in the US) remains very popular, representing over 60% of all Q1 sign ups within our ads countries. We'll launch new products throughout 2026 to help advertisers assess the incrementality of their buys on Netflix, all verified by Netflix's trusted first-party data. Our improved capabilities are attracting many new advertising clients — we now work with over 4,000, up 70% year over year — and we continue to expect ~$3B in ad revenue this year, up 2x from 2025." [Q1 2026 letter, p.5]
- Q4 2025 letter: "Ad revenue rose more than 2.5x to over $1.5B." [p.1] "In 2025, which was only our third year selling advertising, ad revenue grew by more than 2.5x vs. 2024 to over $1.5 billion." [p.2] Q4 revenue "1% above our guidance due to stronger-than-forecasted membership growth and ad sales" [p.2]. AI in ads: "In 2025, we began testing new AI tools to help advertisers create custom ads based on Netflix's intellectual property, and we plan to build on this progress in 2026. We also introduced automated workflows for ad concepts and used advanced AI models to streamline campaign planning, significantly speeding up these processes." [Q4 2025 letter, p.5]

## 6. Engagement and product

### 6.1 View hours and share of TV time
- "View hours grew +2% in H1'26 vs. +1.5% growth in 2025, despite the competitive impact of the Winter Olympics and the World Cup this year." [Q2 2026 letter, p.1] "as detailed in our bi-annual What We Watched report, in the first half of 2026, our members watched more than 97 billion hours, up 2% year over year. This was slightly faster than the 1.5% growth in 2025, despite the competitive impact of the Winter Olympics and the World Cup this year. Non-English content again drove more than a third of all viewing this half, with standout titles from Korea, Japan, Spain, and India." [Q2 2026 letter, p.3]
- Q4 2025 letter: "In the second half of 2025, view hours increased 2% year over year, driven by a 9% rise in viewing of branded originals." [p.1] "in the second half of 2025, our members watched 96 billion hours on Netflix, up 2% (+1.5 billion hours) year over year vs. a 1% increase in the first half of the year. This growth was driven by viewing of our originals, which was up 9% year over year in the second half of 2025" [pp.2–3] "Our overall engagement growth in the second half of 2025, however, was partially offset by a year-over-year decline in viewing of non-branded view hours." [p.3]
- Share of TV time (Nielsen), only in the Q4 2025 letter: "Despite our success over the years, our share of TV time remains below 10% in the major markets in which we operate. For example, according to Nielsen, in December, our share of US TV time reached an all-time high of 9.0% (+0.5 points year over year), yet linear TV still comprises over 40% of US TV screen time." [Q4 2025 letter, p.6] Q1 2026 letter: "we account for an estimated ~5% of TV view share globally" [Q1 2026 letter, p.3]. Q2 2026 letter: no Nielsen or share-of-TV figure.
- Q1 2026 letter: "Our primary internal quality engagement metric hit an all time high in Q1" [p.1]; "In Q1, we made good progress as our primary internal quality metric reached an all-time high." [p.3]
- Engagement disclosure change, verbatim: "After today's What We Watched report, which covers the first half of 2026, we will shift to publishing this report annually in the first quarter, beginning in 2027. The goal of separating the publication of the report from our earnings results is to keep the focus on our primary financial metrics – revenue and operating profit. With this change, we will still report industry-leading title-by-title and total view hours data (including our weekly Top 10 lists for movies and series in more than 90 countries)." [Q2 2026 letter, p.5] Framing: "engagement is not just the quantity of view hours, but also refers to the quality and variety of our offering." [Q2 2026 letter, p.5] "Time spent is just one aspect of strong engagement - quality and variety also matter." [Q2 2026 letter, p.2]

### 6.2 Titles and views (Q2 2026 letter)
- Views definition (footnote 2): "A view is defined as hours viewed divided by runtime for each title. Views for a title are based on the first 91 days since the release of each episode (less than 91 days denoted with an asterisk and data is from launch date through July 12, 2026)." [Q2 2026 letter, p.3]
- Series: Harlan Coben's I Will Find You 87M views ("our biggest new original series debut in 2026 so far"); Legends (UK) 20M; Teach You a Lesson (Korea) 55M ("on track to become our second-most viewed Korean show globally", footnote: "behind Squid Game"); Berlin and The Lady with an Ermine (Spain) 28M; The Polygamist (South Africa) 24M; Flunked (France) 11M; Rosario Tijeras S5 (Mexico) 6M. Films: Apex 131M; Office Romance 63M; Voicemails for Isabelle 71M; Remarkably Bright Creatures 53M; Maternal Instinct 54M; The Crash 67M; Swapped 137M ("on its way to becoming our second most viewed original animated film ever"). [Q2 2026 letter, p.3] "KPop Demon Hunters. It became our first title to surpass over 52 consecutive weeks in the Global Top 10." [Q2 2026 letter, p.2]
- Q3 slate named: films 72 HOURS, The Last House, The Whisper Man, Call My Agent!; series The Hawk, Outer Banks (fifth and final season), Little House on the Prairie, Monster: The Lizzie Borden Story, The Gentlemen S2, The East Palace, The Doll, Lovesick. [Q2 2026 letter, p.4]

### 6.3 Live events and sports
- Q2 2026 letter: "we have two Major League Baseball events (Home Run Derby and Field of Dreams game) in Q3, as well as the Tyson Fury vs. Anthony Joshua fight later this year. We also recently announced an expanded agreement with the NFL, securing a premium slate of games that includes a week-one matchup in Q3, as well as a Thanksgiving Eve game and NFL Christmas Gameday in Q4, and a final week contest in Q1 of next year." [p.4] Ads paragraph names "Women's World Cup, an expanded NFL slate, WWE, MLB events and more" [p.5]. Live share of spend and sign-up days: see §4.
- Q1 2026 letter: "In Q1, we aired more than 70 live events, including our first regional live event with the World Baseball Classic, exclusively for our members in Japan. This massive event delivered 31.4M viewers, becoming our most-watched program ever on Netflix in Japan, and sparked our largest day of sign ups in the country. As a result, among the 190+ countries in which we operate, Japan was the largest contributor to member growth in Q1. Additionally, our March 21st live airing of BTS The Comeback Live delivered 18.4M global viewers, reached the weekly Top 10 in 80 countries and secured the #1 spot in 24 countries." [Q1 2026 letter, p.3] (footnotes: WBC figure "Based on estimated data from Video Research Ltd."; BTS "derived from first-party data (Live+1)".)
- Q4 2025 letter: "big live events like Anthony Joshua's sixth round knockout of Jake Paul (33M average minute audience (Live+1)) and NFL Christmas Day drive disproportionate excitement and signups." "Netflix will stream all 47 games of the 2026 WBC live and on demand for viewers in Japan" "our new show Star Search, with live fan voting, Skyscraper Live, and three Major League Baseball events including an exclusive Opening Night game and the Home Run Derby." [Q4 2025 letter, p.5]

### 6.4 Video podcasts, creators, partnerships
- "approximately half of our viewing occurs in the evening, but our recently launched video podcasts over-index on viewing during the day and on mobile devices, an indicator that this engagement is incremental. We recently added Jay Shetty's On Purpose and Allegedly, as well as announced podcasts featuring Kate Hudson and Oliver Hudson, Lele Pons and Martha Stewart through our partnership with iHeartMedia." [Q2 2026 letter, p.3]
- Creators: "We've had success with creators including Danny Go!, Ms. Rachel, Mark Rober, and Salish & Jordan Matter, and recently announced collaborations with the Stokes Twins, Alan Chikin Chow, Nick DiGiovanni, and Mythical. Ms. Rachel has spent 27 weeks in the Global Top 10 since debuting on Netflix last year and, more recently, Salish & Jordan Matter and Danny Go! have spent eight and seven weeks, respectively, in the Global Top 10 since coming to Netflix in April. We also announced partnerships with leading publishers including Condé Nast, Hearst, and People, to bring their lifestyle content to members in the US and several other countries beginning in August." [Q2 2026 letter, pp.3–4]
- TF1 (France): "last month we launched a partnership with leading local French broadcaster TF1. Netflix members in France are now able to experience TF1 programming as part of their subscription at no additional cost. This fully integrated experience includes TF1's linear channels as well as TF1+'s on-demand content ... a TF1 title, Secret Story has already reached our Top 10 list in France" [Q2 2026 letter, p.4]
- Q4 2025 letter: "in H2, Ms. Rachel S1 was our 9th most-watched show with 47M views globally, while Mark Rober's CrunchLabs had 12M views." Podcast partners "Spotify/The Ringer, iHeartMedia and Barstool Sports", new originals with Pete Davidson and Michael Irvin. Tudum "23.4M visits in December and 232M total visits in 2025 (up 18% from the prior year)"; Netflix Houses in Dallas, TX and King of Prussia, PA. [Q4 2025 letter, p.4]

### 6.5 Games
- "Our cloud-based TV games are gaining traction. In June, we had our two most successful cloud game debuts, with the releases of FIFA World Cup: Launch Edition and Unhinged. And Netflix Playground, our app for kids games, has experienced 3x growth in daily players since its launch in April, and has fueled growth in our kids mobile games engagement, which is up 600% year over year. While off a small base, these early signals give us increasing confidence that we are building a foundation with exciting future growth potential." [Q2 2026 letter, p.4] (footnote 5: "Game play hours are not included in our What We Watched report.")
- Q1 2026 letter: "we're focusing on four categories: narrative, party & puzzle, mainstream, and kids games. Earlier this month we launched Netflix Playground, our new standalone gaming app for kids ... About 10% of kids' profiles have played Netflix games and almost half of kids' profiles view content on mobile devices and tablets ... Based on our data, we believe game play can have a positive impact on member retention." [Q1 2026 letter, p.4] (footnote 5: "Launched in the US, Canada, UK, Australia, the Philippines and New Zealand, with full global launch on 4/28.")
- Q4 2025 letter: "cloud-delivered TV-based party games, including Boggle, Pictionary, Lego Party and Tetris, to roughly one-third of our members." [Q4 2025 letter, p.4]

### 6.6 Pricing, plans, membership tests
- "We offer a wide range of plans and feature sets at accessible price points to provide the best value for members. As we expand and improve our entertainment offering, we occasionally adjust prices so that we can reinvest in our service. Our first half price changes, in markets like the US, Mexico and Spain, have gone well with the impact consistent with prior price changes and our expectations." [Q2 2026 letter, p.5] "The results of our recent price changes are consistent with prior changes and our expectations." [Q2 2026 letter, p.1] UCAN: "only a partial quarter impact from our recent price change" [Q2 2026 letter, p.2]. Price amounts and dates: not disclosed in the letters (the Q1 letter gives only the US ads plan price, $8.99).
- Tests: "We've tested a variety of methods, including a low cost first month in Japan to coincide with the WBC, and an "upgrade on us" offer in various countries around the world. As part of this test and learn strategy, last week we began re-testing free trials for non-rejoining new members in a number of markets around the world (excluding the US and UK)." [Q2 2026 letter, p.5]
- Q1 2026 letter: "Recent price changes have gone well, reflecting the strong and increasing value we provide, and today we announced price adjustments in Spain." [p.5] Distribution: "We've recently found success with new types of partners like Mercado Libre in Mexico and Brazil, where bundling Netflix with their e-commerce loyalty program deepened our penetration" [p.5].

### 6.7 Product, UI and AI
- "We are leveraging LLMs to improve title discovery and to better understand member preferences. We're also enhancing search for our members with new voice search functionality and AI-powered natural language search." [Q2 2026 letter, p.4] "In 2026, GenAI workflows have been used in roughly 300 of our titles, with the largest concentration of work in post-production. We are increasingly leveraging these tools to deliver higher quality output more quickly and at a lower cost than traditional methods. In some cases, productions would have had to leave out key shots and sequences in the absence of GenAI technology." Examples: Glory (India), Brasil 70: A Saga do Tri (Brazil), The American Experiment (US). [Q2 2026 letter, pp.4–5]
- Q1 2026 letter: mobile redesign "launching an updated mobile experience at the end of the month that includes a vertical video discovery feed" [p.4]; "in March we announced our acquisition of InterPositive, the filmmaking technology company founded by Ben Affleck that develops AI-powered tools built by and for filmmakers." [p.4]; GenAI for recommendations, "conversational discovery experiences", promotional assets [p.4].
- Q4 2025 letter: redesigned TV experience rolled out in 2025; 2026 features "live voting and Moments", phone-as-controller for TV games, "thematic title collections" and "vertical video experiences on mobile"; AI for subtitle localization and merchandising. [Q4 2025 letter, p.5]
- The Netflix Effect: "producing TV series and films in more than 50 countries, and contributing more than $325 billion in gross value to the global economy." [Q2 2026 letter, p.6]

## 7. Capital allocation

- Framework, verbatim: "Our capital allocation approach is unchanged. We prioritize reinvestment in the business, both organically and through selective M&A, while maintaining a healthy balance sheet and ample liquidity, and then returning excess cash to shareholders via share repurchases." [Q2 2026 letter, p.6] No numeric leverage target or minimum-cash figure appears in any of the three letters; the Q4 2025 letter adds "We remain committed to maintaining a solid investment grade rating." [Q4 2025 letter, p.7]
- Dividend: no dividend is mentioned in any of the three letters.
- Buybacks by quarter: Q4'25 "repurchased 18.9M shares for $2.1B, leaving $8.0B remaining" [Q4 2025 letter, p.6]; Q1'26 "we repurchased 13.5M shares for $1.3B, leaving $6.8B remaining on our existing share repurchase authorization" [Q1 2026 letter, p.6]; Q2'26 "$4.7B of stock, our largest quarter of share repurchases", new $25B authorization in April, "$27.1B of capacity left" [Q2 2026 letter, p.6]. Cash paid (USD thousands): Q1'25 (3,536,396); Q2'25 (1,654,327); Q3'25 (1,856,885); Q4'25 (2,079,559); FY2025 (9,127,167); Q1'26 (1,270,588); Q2'26 (4,714,403); six months 2026 (5,984,991). [Q2 2026 financials xlsx, Cashflow]
- Debt: gross debt "$14.4B" at both March 31 and June 30, 2026 [Q1 2026 letter, p.5] [Q2 2026 letter, p.6]; "$14.5B" at December 31, 2025 [Q4 2025 letter, p.6]. Repayments of debt: (800,000) Q1'25; (1,033,450) Q2'25; none in Q3'25, Q4'25, Q1'26 or Q2'26; no issuance in 2025 or the first half of 2026. [Q2 2026 financials xlsx, Cashflow] Short-term debt rose from 999,185 (3/31/26) to 2,483,758 (6/30/26) while long-term debt fell from 13,361,331 to 11,825,548 [Q2 2026 financials xlsx, Balance Sheet]; the letter: "$1B of debt maturing later this year, which we plan to refinance." [Q2 2026 letter, p.6]
- Net debt (USD thousands): 5,456,616 at 12/31/25 [Q4 2025 letter, p.17]; 2,124,540 at 3/31/26 (total debt 14,360,516 + issuance costs 52,474 − cash 12,259,772 − short-term investments 28,678) [Q1 2026 letter, p.14]; 5,244,190 at 6/30/26 [Q2 2026 letter, p.14].
- Revolving credit facility: the Q4 2025 letter records "On December 19, we entered a $5B senior unsecured revolving credit facility and a $20B senior unsecured delayed draw term loan facility, and reduced our outstanding bridge facility commitments by a corresponding amount to $34B. On January 19, 2026, we obtained an increase to our bridge facility commitments of $8.2B to support our change to an all-cash transaction, increasing our aggregate bridge facility commitments to $42.2B." (bridge: "On December 4, we obtained commitments for a $59B senior unsecured bridge facility") [Q4 2025 letter, p.6]. The Q1 2026 and Q2 2026 letters say nothing about the status of the revolver, term loan or bridge after the deal ended.
- Warner Bros. Discovery transaction, Q4 2025 letter: "we and WBD amended our merger agreement, which now provides for an all-cash transaction valued at $27.75 per WBD share, replacing the previous mix of cash and Netflix stock." [Q4 2025 letter, p.7] Costs: "~$60M of costs (booked in interest expense) related to our recent Warner Bros.-related bridge loan and associated bridge reduction financings" in Q4'25 [Q4 2025 letter, p.2]; 2026 margin target "includes approximately $275M of acquisition-related expenses" [Q4 2025 letter, p.2].
- Termination, Q1 2026 letter: "Warner Bros. would have been a nice accelerant for our strategy, but only at the right price. We have multiple ways to achieve our goals (including producing, licensing, and partnering)" [p.2]; "the $2.8B termination fee related to the Warner Bros. transaction, which was recognized in "interest and other income."" [p.2]; "This increase was driven in part by a $2.8B cash receipt from the Warner Bros.-related termination fee." [p.5]; "Our cash position is more elevated than normal due to the pause in our share repurchase program during the Warner Bros. transaction and the subsequent receipt of the deal termination fee. As we indicated after declining to raise our offer for Warner Bros., we resumed our share repurchase program." [pp.5–6]; FCF forecast raised to ~$12.5B "due primarily to the after-tax impact of the Warner Bros.-related termination fee" [p.5]. Interest and other income (expense) Q1'26 2,852,166 vs 50,899 in Q1'25 [Q2 2026 financials xlsx, Income Statement]. Interest expense Q1'26 262,077 vs 184,172 Q1'25 and 175,685 Q2'26 [Q2 2026 financials xlsx, Income Statement]; the letters do not itemize deal-related financing costs in Q1'26.
- Q2 2026 letter on Warner Bros.: only "higher cash tax payments due in part to the Warner Bros. termination fee" [p.6]; capital use is the $25B additional authorization and the $4.7B Q2 repurchase [p.6].
- Acquisitions line (USD thousands): (585,744) in Q1'26; (17,194) in Q4'25; none in Q2'26. [Q2 2026 financials xlsx, Cashflow] The Q1 letter names only InterPositive as acquired in Q1 (price not disclosed).
- Governance: "Reed Hastings has informed us that he will not stand for re-election to our Board when his current term expires at the Annual Meeting in June" [Q1 2026 letter, p.6].
- Earnings interview participants: "Co-CEOs Greg Peters and Ted Sarandos, CFO Spence Neumann and VP of Finance & Capital Markets, Spencer Wang" [Q2 2026 letter, p.7]; IR contact Lowell Singer, VP Investor Relations [Q2 2026 letter, p.7].

## 8. The workbook (`Q2-26-Website-Financials.xlsx`, five sheets)

Sheets and contents [Q2 2026 financials xlsx]:
- "Income Statement" (dims A1:L28): Consolidated Statements of Operations, USD thousands except per share; columns Q1'25, Q2'25, Q3'25, Q4'25, FY2025, Q1'26, Q2'26, six months 2026.
- "Balance Sheet" (dims A1:L59): Consolidated Balance Sheets at 3/31/25, 6/30/25, 9/30/25, 12/31/25, 3/31/26, 6/30/26. No supplemental content-obligations line (that is in the letter only).
- "Cashflow" (dims A1:O50): Consolidated Statements of Cash Flows with the same eight columns as the income statement, plus the non-GAAP free cash flow reconciliation.
- "Regional Information" (dims A1:W83): Revenue Information by Region, the full constant-currency bridge for Q1'25, Q2'25, Q3'25, Q4'25, FY2025, Q1'26, Q2'26 and six months 2026, each against its prior-year period. No consolidated total row (the letter has it).
- "FX Neutral" (dims A1:G58): F/X Neutral Operating Margin, YTD 2026 (through June 30, 2026) only.
- Not in the workbook: memberships, ARM, ad revenue, cash content spend as a named line, shares outstanding, share repurchase counts, net debt, content obligations, segment operating results.

### 8.1 Income statement (USD thousands except per share) [Q2 2026 financials xlsx, Income Statement]

| Line | Q1'25 | Q2'25 | Q3'25 | Q4'25 | FY2025 | Q1'26 | Q2'26 | 6M'26 |
|---|---|---|---|---|---|---|---|---|
| Revenues | 10,542,801 | 11,079,166 | 11,510,307 | 12,050,762 | 45,183,036 | 12,249,757 | 12,559,938 | 24,809,695 |
| Cost of revenues | 5,263,147 | 5,325,311 | 6,164,250 | 6,522,621 | 23,275,329 | 5,888,238 | 6,036,965 | 11,925,203 |
| Sales and marketing | 688,370 | 713,265 | 786,295 | 1,113,376 | 3,301,306 | 842,217 | 823,838 | 1,666,055 |
| Technology and development | 822,823 | 824,683 | 853,584 | 890,300 | 3,391,390 | 959,696 | 1,007,675 | 1,967,371 |
| General and administrative | 421,462 | 441,213 | 457,931 | 567,802 | 1,888,408 | 602,609 | 498,850 | 1,101,459 |
| Operating income | 3,346,999 | 3,774,694 | 3,248,247 | 2,956,663 | 13,326,603 | 3,956,997 | 4,192,610 | 8,149,607 |
| Interest expense | (184,172) | (182,649) | (175,294) | (234,395) | (776,510) | (262,077) | (175,685) | (437,762) |
| Interest and other income (expense) | 50,899 | 39,630 | 36,457 | 45,473 | 172,459 | 2,852,166 | 51,661 | 2,903,827 |
| Income before income taxes | 3,213,726 | 3,631,675 | 3,109,410 | 2,767,741 | 12,722,552 | 6,547,086 | 4,068,586 | 10,615,672 |
| Provision for income taxes | (323,375) | (506,262) | (562,494) | (349,220) | (1,741,351) | (1,264,295) | (667,172) | (1,931,467) |
| Net income | 2,890,351 | 3,125,413 | 2,546,916 | 2,418,521 | 10,981,201 | 5,282,791 | 3,401,414 | 8,684,205 |
| EPS basic | 0.68 | 0.74 | 0.60 | 0.57 | 2.58 | 1.25 | 0.81 | 2.06 |
| EPS diluted | 0.66 | 0.72 | 0.59 | 0.56 | 2.53 | 1.23 | 0.80 | 2.03 |
| Weighted-average shares basic | 4,272,695 | 4,252,112 | 4,244,553 | 4,229,221 | 4,249,512 | 4,222,787 | 4,189,303 | 4,205,952 |
| Weighted-average shares diluted | 4,369,623 | 4,348,825 | 4,340,392 | 4,317,144 | 4,343,863 | 4,298,437 | 4,261,300 | 4,279,776 |

- computed: operating margin Q1'25 31.7%; Q2'25 34.1%; Q3'25 28.2%; Q4'25 24.5%; FY2025 29.5%; Q1'26 32.3%; Q2'26 33.4%; 6M'26 32.8% (matches the letter tables and the FX Neutral sheet).

### 8.2 Balance sheet (USD thousands) [Q2 2026 financials xlsx, Balance Sheet]

| Line | 3/31/25 | 6/30/25 | 9/30/25 | 12/31/25 | 3/31/26 | 6/30/26 |
|---|---|---|---|---|---|---|
| Cash and cash equivalents | 7,199,848 | 8,177,405 | 9,287,287 | 9,033,681 | 12,259,772 | 9,099,232 |
| Short-term investments | 1,171,142 | 213,115 | 37,105 | 28,678 | 28,678 | 28,678 |
| Other current assets | 3,326,642 | 3,602,586 | 3,638,543 | 3,957,832 | 4,782,532 | 4,725,393 |
| Total current assets | 11,697,632 | 11,993,106 | 12,962,935 | 13,020,191 | 17,070,982 | 13,853,303 |
| Content assets, net | 32,040,839 | 32,089,394 | 32,639,879 | 32,778,392 | 33,376,295 | 33,837,573 |
| Property and equipment, net | 1,644,346 | 1,743,566 | 1,837,889 | 2,004,350 | 2,147,829 | 2,398,848 |
| Other non-current assets | 6,704,827 | 7,273,598 | 7,494,132 | 7,794,060 | 8,420,808 | 8,360,717 |
| Total assets | 52,087,644 | 53,099,664 | 54,934,835 | 55,596,993 | 61,015,914 | 58,450,441 |
| Current content liabilities | 4,128,905 | 4,091,770 | 4,102,640 | 4,084,854 | 4,052,278 | 3,866,522 |
| Accounts payable | 614,489 | 632,718 | 793,233 | 900,612 | 894,681 | 814,551 |
| Accrued expenses and other liabilities | 2,359,518 | 2,489,486 | 3,111,311 | 3,220,869 | 4,441,986 | 3,172,611 |
| Deferred revenue | 1,609,726 | 1,728,361 | 1,724,675 | 1,775,730 | 1,743,448 | 1,797,456 |
| Short-term debt | 1,005,881 | 0 | 0 | 998,865 | 999,185 | 2,483,758 |
| Total current liabilities | 9,718,519 | 8,942,335 | 9,731,859 | 10,980,930 | 12,131,578 | 12,134,898 |
| Non-current content liabilities | 1,696,662 | 1,606,404 | 1,591,973 | 1,579,476 | 1,626,498 | 1,625,600 |
| Long-term debt | 14,011,037 | 14,453,206 | 14,463,020 | 13,463,971 | 13,361,331 | 11,825,548 |
| Other non-current liabilities | 2,633,353 | 3,145,820 | 3,193,948 | 2,957,128 | 2,770,108 | 2,712,343 |
| Total liabilities | 28,059,571 | 28,147,765 | 28,980,800 | 28,981,505 | 29,889,515 | 28,298,389 |
| Common stock | 6,677,469 | 6,932,828 | 7,080,325 | 7,286,410 | 7,478,495 | 7,670,503 |
| Treasury stock at cost | (16,754,929) | (18,392,942) | (20,270,631) | (22,372,658) | (23,681,974) | (28,387,657) |
| Accumulated other comprehensive income (loss) | (85,735) | (904,668) | (719,256) | (580,382) | (235,031) | (97,117) |
| Retained earnings | 34,191,268 | 37,316,681 | 39,863,597 | 42,282,118 | 47,564,909 | 50,966,323 |
| Total stockholders' equity | 24,028,073 | 24,951,899 | 25,954,035 | 26,615,488 | 31,126,399 | 30,152,052 |

- computed: gross debt (short-term + long-term) 3/31/25 15,016,918; 6/30/25 14,453,206; 9/30/25 14,463,020; 12/31/25 14,462,836; 3/31/26 14,360,516; 6/30/26 14,309,306 (the last three match the letters' net-debt "Total debt" lines).

### 8.3 Cash-flow statement (USD thousands) [Q2 2026 financials xlsx, Cashflow]

| Line | Q1'25 | Q2'25 | Q3'25 | Q4'25 | FY2025 | Q1'26 | Q2'26 | 6M'26 |
|---|---|---|---|---|---|---|---|---|
| Net income | 2,890,351 | 3,125,413 | 2,546,916 | 2,418,521 | 10,981,201 | 5,282,791 | 3,401,414 | 8,684,205 |
| Additions to content assets | (3,549,657) | (3,835,813) | (4,653,935) | (5,057,212) | (17,096,617) | (4,846,917) | (4,927,523) | (9,774,440) |
| Change in content liabilities | (411,253) | (214,052) | 24,262 | (9,795) | (610,838) | 45,216 | (181,794) | (136,578) |
| Amortization of content assets | 3,823,112 | 3,832,074 | 4,002,744 | 4,764,236 | 16,422,166 | 4,217,900 | 4,311,309 | 8,529,209 |
| Depreciation and amortization of property, equipment and intangibles | 80,067 | 80,013 | 87,326 | 85,983 | 333,389 | 98,575 | 100,530 | 199,105 |
| Stock-based compensation expense | 71,977 | 80,862 | 80,986 | 134,624 | 368,449 | 140,405 | 131,312 | 271,717 |
| Foreign currency remeasurement loss (gain) on debt | 28,547 | 55,238 | (1,707) | (9,730) | 72,348 | (10,110) | (8,813) | (18,923) |
| Other non-cash items | 114,730 | 120,139 | 142,293 | 200,289 | 577,451 | 198,227 | 141,356 | 339,583 |
| Deferred income taxes | (163,928) | (135,755) | 20,539 | (162,912) | (442,056) | 58,819 | 81,260 | 140,079 |
| Other current assets | (131,367) | (176,683) | (169,597) | (313,014) | (790,661) | (704,640) | 111,713 | (592,927) |
| Accounts payable | (276,426) | 11,046 | 139,451 | 117,890 | (8,039) | 154 | (157,397) | (157,243) |
| Accrued expenses and other liabilities | 306,413 | (267,235) | 707,151 | 134,889 | 881,218 | 1,295,904 | (1,249,793) | 46,111 |
| Deferred revenue | 88,913 | 118,635 | (3,686) | 51,055 | 254,917 | (32,282) | 54,008 | 21,726 |
| Other non-current assets and liabilities | (82,280) | (370,624) | (97,569) | (243,182) | (793,655) | (453,837) | (63,770) | (517,607) |
| Net cash provided by operating activities | 2,789,199 | 2,423,258 | 2,825,174 | 2,111,642 | 10,149,273 | 5,290,205 | 1,743,812 | 7,034,017 |
| Purchases of property and equipment | (128,277) | (155,889) | (164,719) | (239,335) | (688,220) | (196,130) | (218,644) | (414,774) |
| Acquisitions | 0 | 0 | 0 | (17,194) | (17,194) | (585,744) | 0 | (585,744) |
| Purchases of investments | (156,015) | (1,650) | (3,850) | (8,450) | (169,965) | 0 | 0 | 0 |
| Proceeds from maturities and sales of investments | 769,954 | 962,413 | 176,250 | 8,450 | 1,917,067 | 0 | 0 | 0 |
| Other investing activities | 0 | (36,190) | 36,190 | 0 | 0 | 0 | 0 | 0 |
| Net cash provided by (used in) investing activities | 485,662 | 768,684 | 43,871 | (256,529) | 1,041,688 | (781,874) | (218,644) | (1,000,518) |
| Repayments of debt | (800,000) | (1,033,450) | 0 | 0 | (1,833,450) | 0 | 0 | 0 |
| Proceeds from issuance of common stock | 351,602 | 169,066 | 70,215 | 76,082 | 666,965 | 49,310 | 59,980 | 109,290 |
| Repurchases of common stock | (3,536,396) | (1,654,327) | (1,856,885) | (2,079,559) | (9,127,167) | (1,270,588) | (4,714,403) | (5,984,991) |
| Taxes paid related to net share settlement of equity awards | (27,870) | (6,114) | (6,196) | (5,985) | (46,165) | (29,230) | (6,631) | (35,861) |
| Other financing activities | (15,652) | 21,957 | 55,837 | (67,948) | (5,806) | 19,694 | (8,573) | 11,121 |
| Net cash used in financing activities | (4,028,316) | (2,502,868) | (1,737,029) | (2,077,410) | (10,345,623) | (1,230,814) | (4,669,627) | (5,900,441) |
| Effect of exchange rate changes on cash | 150,146 | 287,471 | (21,721) | (29,377) | 386,519 | (49,838) | (19,628) | (69,466) |
| Net increase (decrease) in cash, cash equivalents, and restricted cash | (603,309) | 976,545 | 1,110,295 | (251,674) | 1,231,857 | 3,227,679 | (3,164,087) | 63,592 |
| Cash, cash equivalents, and restricted cash end of period | 7,204,028 | 8,180,573 | 9,290,868 | 9,039,194 | 9,039,194 | 12,266,873 | 9,102,786 | 9,102,786 |
| Non-GAAP free cash flow | 2,660,922 | 2,267,369 | 2,660,455 | 1,872,307 | 9,461,053 | 5,094,075 | 1,525,168 | 6,619,243 |

### 8.4 Regional revenue with the constant-currency bridge (USD thousands) [Q2 2026 financials xlsx, Regional Information]

Columns: As Reported | Constant Currency Adjustment | Hedging (Gains) Losses Included in Revenues | Constant Currency Revenues | prior-year As Reported | prior-year Hedging (Gains) Losses | prior-year Revenues Less Hedging Impact | Reported Change | Constant Currency Change.

| Period | Region | As Reported | CC Adj. | Hedging | CC Revenues | PY As Reported | PY Hedging | PY Less Hedging | Reported | CC |
|---|---|---|---|---|---|---|---|---|---|---|
| Q1'25 vs Q1'24 | UCAN | 4,617,098 | 23,338 | (14,552) | 4,625,884 | 4,224,315 | 831 | 4,225,146 | 9% | 9% |
| | EMEA | 3,404,676 | 146,975 | (105,225) | 3,446,426 | 2,958,193 | 4,687 | 2,962,880 | 15% | 16% |
| | LATAM | 1,261,934 | 243,068 | (13,936) | 1,491,066 | 1,165,008 | 6,266 | 1,171,274 | 8% | 27% |
| | APAC | 1,259,093 | 62,243 | (31,083) | 1,290,253 | 1,022,924 | (543) | 1,022,381 | 23% | 26% |
| Q2'25 vs Q2'24 | UCAN | 4,929,003 | 8,036 | (6,431) | 4,930,608 | 4,295,560 | (3,183) | 4,292,377 | 15% | 15% |
| | EMEA | 3,538,175 | (122,664) | 42,049 | 3,457,560 | 3,007,772 | (15,344) | 2,992,428 | 18% | 16% |
| | LATAM | 1,306,735 | 161,306 | 14,033 | 1,482,074 | 1,204,145 | (1,759) | 1,202,386 | 9% | 23% |
| | APAC | 1,305,253 | (16,166) | (12,266) | 1,276,821 | 1,051,833 | (13,015) | 1,038,818 | 24% | 23% |
| Q3'25 vs Q3'24 | UCAN | 5,071,781 | 1,816 | (2,196) | 5,071,401 | 4,322,476 | (3,265) | 4,319,211 | 17% | 17% |
| | EMEA | 3,699,052 | (199,597) | 113,580 | 3,613,035 | 3,133,466 | (1,857) | 3,131,609 | 18% | 15% |
| | LATAM | 1,370,913 | 53,678 | 26,300 | 1,450,891 | 1,240,892 | (34,654) | 1,206,238 | 10% | 20% |
| | APAC | 1,368,561 | (14,750) | (8,319) | 1,345,492 | 1,127,869 | (8,408) | 1,119,461 | 21% | 20% |
| Q4'25 vs Q4'24 | UCAN | 5,339,270 | 3,801 | (6,612) | 5,336,459 | 4,517,018 | (5,564) | 4,511,454 | 18% | 18% |
| | EMEA | 3,872,743 | (198,888) | 87,364 | 3,761,219 | 3,287,604 | (12,789) | 3,274,815 | 18% | 15% |
| | LATAM | 1,417,939 | (1,052) | 27,711 | 1,444,598 | 1,229,771 | (28,307) | 1,201,464 | 15% | 20% |
| | APAC | 1,420,810 | 28,413 | (19,274) | 1,429,949 | 1,212,120 | (7,107) | 1,205,013 | 17% | 19% |
| FY2025 vs FY2024 | UCAN | 19,957,152 | 36,991 | (29,791) | 19,964,352 | 17,359,369 | (11,181) | 17,348,188 | 15% | 15% |
| | EMEA | 14,514,646 | (374,174) | 137,768 | 14,278,240 | 12,387,035 | (25,303) | 12,361,732 | 17% | 16% |
| | LATAM | 5,357,521 | 457,000 | 54,108 | 5,868,629 | 4,839,816 | (58,454) | 4,781,362 | 11% | 23% |
| | APAC | 5,353,717 | 59,740 | (70,942) | 5,342,515 | 4,414,746 | (29,073) | 4,385,673 | 21% | 22% |
| Q1'26 vs Q1'25 | UCAN | 5,245,298 | (20,306) | (463) | 5,224,529 | 4,617,098 | (14,552) | 4,602,546 | 14% | 14% |
| | EMEA | 3,998,419 | (418,871) | 113,651 | 3,693,199 | 3,404,676 | (105,225) | 3,299,451 | 17% | 12% |
| | LATAM | 1,497,058 | (60,512) | 31,286 | 1,467,832 | 1,261,934 | (13,936) | 1,247,998 | 19% | 18% |
| | APAC | 1,508,982 | (40,823) | (11,957) | 1,456,202 | 1,259,093 | (31,083) | 1,228,010 | 20% | 19% |
| Q2'26 vs Q2'25 | UCAN | 5,431,667 | (4,883) | (3,284) | 5,423,500 | 4,929,003 | (6,431) | 4,922,572 | 10% | 10% |
| | EMEA | 4,033,515 | (130,725) | 58,490 | 3,961,280 | 3,538,175 | 42,049 | 3,580,224 | 14% | 11% |
| | LATAM | 1,584,290 | (67,459) | 11,494 | 1,528,325 | 1,306,735 | 14,033 | 1,320,768 | 21% | 16% |
| | APAC | 1,510,466 | 28,880 | (19,070) | 1,520,276 | 1,305,253 | (12,266) | 1,292,987 | 16% | 18% |
| 6M'26 vs 6M'25 | UCAN | 10,676,965 | (25,189) | (3,747) | 10,648,029 | 9,546,101 | (20,983) | 9,525,118 | 12% | 12% |
| | EMEA | 8,031,934 | (549,596) | 172,141 | 7,654,479 | 6,942,851 | (63,176) | 6,879,675 | 16% | 11% |
| | LATAM | 3,081,348 | (127,971) | 42,780 | 2,996,157 | 2,568,669 | 97 | 2,568,766 | 20% | 17% |
| | APAC | 3,019,448 | (11,943) | (31,027) | 2,976,478 | 2,564,346 | (43,349) | 2,520,997 | 18% | 18% |

- computed: regional sum Q2'26 5,431,667 + 4,033,515 + 1,584,290 + 1,510,466 = 12,559,938 = consolidated revenue. Regional mix Q2'26: UCAN 43.2%, EMEA 32.1%, LATAM 12.6%, APAC 12.0%.
- Constant-currency footnote, verbatim: "The Company believes the non-GAAP financial measure of constant currency revenue is useful in analyzing period-to-period comparisons in revenues absent foreign currency fluctuations. However, this non-GAAP financial measure should be considered in addition to, not as a substitute for, or superior to other financial measures prepared in accordance with GAAP. In order to exclude the effect of foreign currency rate fluctuations on revenue, we calculate current period revenue assuming foreign exchange rates had remained constant with foreign exchange rates from each of the corresponding months of the prior-year period and exclude the impact of hedging gains or losses realized as revenues. Constant currency percentage change in revenues is calculated as the percentage change between current period constant currency revenue and the prior comparative period revenue. The impact of hedging gains or losses is excluded from both the current and prior periods." [Q2 2026 financials xlsx, Regional Information]

### 8.5 F/X neutral operating margin (USD thousands) [Q2 2026 financials xlsx, FX Neutral]

| | YTD 2026 (through June 30, 2026) |
|---|---|
| As Reported: Revenue | 24,809,695 |
| As Reported: Operating Expenses | 16,660,088 |
| As Reported: Operating Profit | 8,149,607 |
| As Reported: Operating Margin | 32.8% |
| F/X Impact: Revenue | 87,127 |
| F/X Impact: Operating Expenses | 20,139 |
| F/X Impact: Operating Profit | 66,988 |
| Adjusted: Revenue | 24,722,568 |
| Adjusted: Operating Expenses | 16,639,949 |
| Adjusted: Operating Profit | 8,082,619 |
| Adjusted: Operating Margin | 32.7% |

Footnote, verbatim: "*Based on F/X rates at the beginning of each year including our F/X hedges at that time. Note: Excludes F/X impact on content amortization, as titles are amortized at a historical blended rate based on timing of spend. YTD 2026 through June 30, 2026." [Q2 2026 financials xlsx, FX Neutral]

## 9. Non-GAAP reconciliations and definitions in the letters

- Measures named: "F/X neutral revenue and adjusted operating profit and margin, free cash flow and net debt." Rationale, verbatim: "Management believes that free cash flow is an important liquidity metric because it measures, during a given period, the amount of cash generated that is available to repay debt obligations, make strategic acquisitions and investments and for certain other activities like stock repurchases. Management believes that F/X neutral revenue and adjusted operating profit and margin allow investors to compare our projected results to our actual results absent year-over-year and intra-year currency fluctuations. Management believes net debt is a useful measure of the company's liquidity, capital structure, and leverage." [Q2 2026 letter, pp.7–8] "We are not able to reconcile forward-looking non-GAAP financial measures because we are unable to predict without unreasonable effort the exact amount or timing of the reconciling items, including property and equipment, and the impact of changes in currency exchange rates." [Q2 2026 letter, p.8]
- Free cash flow: "Defined as cash provided by (used in) operating activities less purchases of property and equipment." [Q2 2026 letter, p.6] Reconciliation in §1 (Q2 2026) and §3.3 (FY2025).
- F/X neutral revenue growth (footnote 1): "Excluding the year over year effect of foreign exchange rate movements and the impact of hedging gains/losses realized as revenues. Assumes foreign exchange rates remained constant with foreign exchange rates from each of the corresponding months of the prior-year period." [Q2 2026 letter, p.1] Regional bridges in §8.4; consolidated totals in §2.
- F/X neutral operating margin method, verbatim: "To provide additional transparency around our operating margin, we disclose each quarter our year-to-date (YTD) operating margin based on F/X rates at the beginning of each year. This will allow investors to see how our operating margin is tracking against our target (which was set in January of 2026 based on F/X rates at that time), absent intra-year fluctuations in F/X." [Q2 2026 letter, p.14] YTD 2026 (through June 30): as reported 32.8%, adjusted 32.7% (table in §8.5) [Q2 2026 letter, p.14]. YTD through March 31, 2026: As Reported revenue 12,249,757, operating expenses 8,292,760, operating profit 3,956,997, margin 32.3%; F/X impact revenue 39,766, operating expenses 15,625, operating profit 24,141; Adjusted revenue 12,209,991, operating expenses 8,277,135, operating profit 3,932,856, margin 32.2%. [Q1 2026 letter, p.14] Full year 2025: As Reported revenue 45,183,036, operating expenses 31,856,433, operating profit 13,326,603, margin 29.5%; F/X impact revenue 540,673, operating expenses 317,482, operating profit 223,191; Adjusted revenue 44,642,363, operating expenses 31,538,951, operating profit 13,103,412, margin 29.4%. [Q4 2025 letter, p.17]
- Net debt: total debt plus debt issuance costs and original issue discount (and, at June 30, 2026, a fair value hedging adjustment) less cash and cash equivalents and short-term investments; figures in §1 and §7.

## 10. Gaps: what the letters and workbook do not report

- Paid memberships: no count, net additions or regional split in the Q2 2026 letter, Q1 2026 letter or workbook; the last figure in these sources is "over 325M" at the end of 2025 [Q4 2025 letter, p.2]. No source states the reason.
- Average revenue per membership (ARM): not in any of the three letters or the workbook.
- Advertising: no quarterly or half-year ad revenue in dollars; no ad revenue as a percent of total; no ad-tier sign-up share in the Q2 2026 letter (Q1 2026 letter: "over 60%"); no advertiser count in the Q2 2026 letter (Q1 2026 letter: "over 4,000"); no upfront dollar total; no ad-supported plan membership figure.
- Cash content spend: no dollar figure for any period (only the "~1.1x" 2026 ratio); the cash-flow line "Additions to content assets" is the nearest series. No content-amortization schedule beyond the cash-flow line; no split between originals and licensed.
- Share count: number of shares repurchased in Q2 2026 not given (Q1 2026: 13.5M; Q4 2025: 18.9M); shares outstanding at period end not given.
- Guidance: no tax rate, capex, interest expense, share count, Q3 2026 cash flow or FCF, or membership guidance; no 2027 statements.
- Debt: no maturity schedule beyond "$1B of debt maturing later this year"; no coupon or facility status; revolver and term loan mentioned only in the Q4 2025 letter.
- Share of TV time (Nielsen): only the December 2025 US figure in the Q4 2025 letter; nothing for 2026.
- Price changes: countries only (US, Mexico, Spain in the first half of 2026); no amounts, dates or plan-by-plan detail.
- Headcount, churn, retention rates, hours per member, regional margins, segment operating results: not disclosed.
