# Duolingo, Inc. (DUOL) — Review of business.md and outlook.md, as of Q2 2026

_Reviewer pass, 2026-09-08. Drafts: `companies/DUOL/business.md`, `companies/DUOL/outlook.md`. Sources: `companies/DUOL/sources/2026-Q2/` (cached filings, letters, release, transcript; the `notes-*.md` files were not used as evidence). Source line numbers below are line numbers in the cached `.txt` files; letter `p.N` is the printed footer page (text between footer N−1 and footer N). Filings give dollars in thousands; the drafts round to millions._

## Verdict: REVISE (one pass). Cycle 2 below: final verdict PASS

_Cycle 1 (2026-09-08): REVISE, seven items. Cycle 2 (2026-09-08, after the writer's second pass): all seven verified against the sources; PASS. The cycle-1 text is kept unchanged below; the cycle-2 results are in §13._

Everything in the two §3/§4 tables, the outlook §1 table, the guidance quotes and the claim quotes verified against the cached sources. The revise items are: one invented range built from "tens of millions" (business §3), one unsupported date ("flat since 2021"), one internal contradiction (2021 buyback), one double-barreled claim, three unlabelled floors in the claims list, and two small wording fixes where the text says more than the source does. The list is in §10.

## 1. Rubric (§14)

| # | Question | Answer | Reasoning |
|---|---|---|---|
| 1 | Explain what the company does and who pays it, in two sentences? | Yes | §1 and §2 give it directly: a free language app where about 9% of monthly users pay for Super/Max subscriptions (84% of revenue), advertisers pay to reach the rest, and test-takers pay for the Duolingo English Test. |
| 2 | Know what would kill it and the early warning sign? | Yes | §6 ranks eight scenarios, each with a warning sign; the top one (general-purpose AI) is tied to DAU growth below 20% with CURR falling, and the app-store scenario to the processor shares in the quarterly revenue note. |
| 3 | Know why margins are what they are and whether cost scales with usage? | Yes | §3 separates the app-store fee (scales with paid revenue) from hosting and AI (scale with usage), shows gross margin at 72–73% for five years with the stated driver each year, and splits the 2025 revenue dollar 28/30/12/18/13. |
| 4 | Predict what the scorecard will check next quarter from §5 alone? | Yes, with one fix | Eleven claims, each tied to a metric, date or event; claim 9 checks two things at once and must be split (item 4 in §10). |
| 5 | Nothing required knowledge I don't have? | Yes, after edits | Eleven-entry glossary covers the unavoidable terms; the reviewer glossed the remaining jargon directly (see §11). |

## 2. Citation spot-check

Convention: PASS = the tagged source contains the number or wording; for "(computed)" cells the arithmetic is redone from the source numbers and shown. Curly quotes in the filings were normalised for comparison.

### 2a. business.md §2, revenue-by-type table (every cell)

Sources printed in full: `10-K-FY2023.txt` l.2816–2826 (Note 4, FY2023/2022/2021 columns), `10-K-FY2025.txt` l.2851–2871 (Note 5, Subscription plus the "Other revenue is comprised of" table), `10-Q-2026-Q2.txt` l.662–672 (Note 4).

| Row | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | Q2 2026 | Result |
|---|---|---|---|---|---|---|---|
| Subscription | 180,698 | 273,507 | 404,684 | 607,531 | 873,442 | 258,035 | PASS (all six) |
| Advertising | 38,501 | 44,731 | 49,858 | 54,907 | 79,725 | 21,052 | PASS |
| DET | 24,658 | 32,718 | 41,212 | 45,640 | 42,006 | 10,109 | PASS |
| In-app purchases | 6,836 | 17,914 | 34,673 | 38,653 | 40,479 ("IAPs") | 8,002 | PASS |
| Other | 79 | 625 | 682 | 1,293 | 1,937 | 1,256 | PASS (0.1 = 79/1000) |
| Total | 250,772 | 369,495 | 531,109 | 748,024 | 1,037,589 | 298,454 | PASS |
| Growth (computed) | n/a | 369,495/250,772 = +47.3% | +43.7% | +40.8% | +38.7% | 298,454/252,265 = +18.3% | PASS |
| Subscription share (computed) | 72.1% | 74.0% | 76.2% | 81.2% | 84.2% | 86.5% | PASS |

Text percentages in §2: advertising 79,725/1,037,589 = 7.68% → "7.7%" PASS; DET 42,006/1,037,589 = 4.05% → "4.0%" PASS (also stated as "approximately 4.0%" at `10-K-FY2025.txt` l.754); DET 2024 45,640/748,024 = 6.10% → "6.1%" PASS (also stated at `10-K-FY2024.txt` l.744); in-app 40,479/1,037,589 = 3.90% PASS. The note that the FY2025 10-K's MD&A shows only "Subscription" and "Other (1)" PASS (`10-K-FY2025.txt` l.1812–1814).

### 2b. business.md §2, users-and-bookings table (every cell)

| Row | Source lines | Result |
|---|---|---|
| DAUs 10.1 / 16.3 / 26.9 / 40.5 / 52.7 / 58.7 | `10-K-FY2021.txt` l.1420; `10-K-FY2022.txt` l.1394; `10-K-FY2023.txt` l.1514; `10-K-FY2024.txt` l.1458; `10-K-FY2025.txt` l.1430; `10-Q-2026-Q2.txt` l.936 | PASS |
| DAU growth 20% / 62% / 65% / 51% / 30% / 23% | stated in each 10-K's Item 2/7 text: FY2021 l.1456 ("increase of 20%"), FY2022 l.1430 ("62%"), FY2023 l.1550 ("65%"), FY2024 l.1494 ("51%"), FY2025 l.1472 ("30%"), 10-Q l.972 ("23%") | PASS (62% is management's figure; 16.3/10.1 rounds to 61%, so the stated number is the right one to use) |
| MAUs 42.4 / 60.7 / 88.4 / 116.7 / 133.1 / 140.6 | same KPI tables (l.1418, 1392, 1512, 1456, 1428) and 10-Q l.962 | PASS |
| Paid subscribers 2.5 / 4.2 / 6.6 / 9.5 / 12.2 / 12.7 | l.1422, 1396, 1516, 1460, 1432; 10-Q l.938 | PASS |
| Paid-subscriber growth 56% / 67% / 57% / 43% / 28% / 17% | FY2021 l.1460, FY2022 l.1438, FY2023 l.1554, FY2024 l.1498, FY2025 l.1476, 10-Q l.976 | PASS (all are management's stated figures) |
| Paid / MAUs (computed) 5.9 / 6.9 / 7.5 / 8.1 / 9.2 / 9.0% | 2.5/42.4 = 5.90; 4.2/60.7 = 6.92; 6.6/88.4 = 7.47; 9.5/116.7 = 8.14; 12.2/133.1 = 9.17; 12.7/140.6 = 9.03 | PASS |
| Subscription bookings 224.5 / 331.8 / 495.5 / 730.7 / 996.3 / 250.3 | l.1434 (224,520), 1408 (331,803), 1528 (495,497), 1468 (730,737), 1440 (996,268); 10-Q l.946 (250,316) | PASS |
| Total bookings 294.2 / 428.6 / 622.2 / 870.6 / 1,158.4 / 289.1 | l.1436 (294,247), 1410 (428,647), 1530 (622,181), 1470 (870,601), 1442 (1,158,425); 10-Q l.948 (289,054) | PASS |

### 2c. business.md §3 table (every cell)

| Row | Source and arithmetic | Result |
|---|---|---|
| Revenue 250.8 / 369.5 / 531.1 / 748.0 / 1,037.6 / 590.4 | as 2a; six months 590,421 (`10-Q-2026-Q2.txt` l.267) | PASS |
| Gross margin 72.4 / 73.1 / 73.2 / 72.8 / 72.2 / 72.8% | gross profit ÷ revenue: 181,586/250,772 = 72.41 (`10-K-FY2021.txt` l.1644); 270,064/369,495 = 73.09 (`10-K-FY2023.txt` l.2383); 389,004/531,109 = 73.24; 544,379/748,024 = 72.78; 749,457/1,037,589 = 72.23 (`10-K-FY2025.txt` l.2301); 429,836/590,421 = 72.80 (10-Q l.271). Management states the same one-decimal figures in each Item 7 gross-margin paragraph (FY2021 l.1754, FY2022 l.1780, FY2023 l.1894, FY2024 l.1824, FY2025 l.1822; 10-Q l.1290 "72.8%") | PASS |
| Operating margin (24) / (18) / (2) / 8 / 13 / 13% | percent-of-revenue tables: `10-K-FY2022.txt` l.1734 "(18) | (24)"; `10-K-FY2023.txt` l.1844 "(2) | (18)"; `10-K-FY2025.txt` l.1780 "13 | 8"; 10-Q l.1242 six-month column "13" | PASS |
| Adjusted EBITDA margin (computed) (0.4) / 4.2 / 17.6 / 25.7 / 29.5 / 27.2% | −1,066/250,772 = −0.43 (`10-K-FY2021.txt` l.1442); 15,457/369,495 = 4.18 (`10-K-FY2022.txt` l.1416); 93,678/531,109 = 17.64 (`10-K-FY2023.txt` l.1536); 191,942/748,024 = 25.66 (`10-K-FY2024.txt` l.1476); 305,878/1,037,589 = 29.48 (`10-K-FY2025.txt` l.1448); 160,747/590,421 = 27.23 (10-Q l.954) | PASS |
| Stock-based compensation / revenue (computed) 16.3 / 20.0 / 17.9 / 14.8 / 13.2 / 12.3% | 40,804 / 73,820 / 95,221 (`10-K-FY2023.txt` l.2438, 2454, 2476); 110,477 / 137,437 (`10-K-FY2025.txt` l.2367, 2383); 72,857 (10-Q l.1028 "$72.9 million"; letter p.17 cash-flow line). 40,804/250,772 = 16.27; 73,820/369,495 = 19.98; 95,221/531,109 = 17.93; 110,477/748,024 = 14.77; 137,437/1,037,589 = 13.25; 72,857/590,421 = 12.34 | PASS |
| Purchases of property and equipment 3.6 / 5.6 / 3.2 / 12.1 / 18.1 / 7.0 | 3,586 (`10-K-FY2021.txt` l.1556); 5,562 (`10-K-FY2022.txt` l.1546); 3,191 (`10-K-FY2023.txt` l.1654); 12,116 (`10-K-FY2024.txt` l.1596); 18,096 (`10-K-FY2025.txt` l.1588); 7,028 (10-Q l.1066) | PASS |
| Capitalised software and intangibles 2.6 / 4.6 / 10.5 / 9.0 / 9.3 / 5.6 | 2,620 (l.1554); 4,562 (l.1544); 10,493 (l.1652); 9,024 (l.1594); 9,303 (l.1586); 5,587 (10-Q l.1064) | PASS |
| Both together / revenue (computed) 2.5 / 2.7 / 2.6 / 2.8 / 2.6 / 2.1% | 6,206/250,772 = 2.47; 10,124/369,495 = 2.74; 13,684/531,109 = 2.58; 21,140/748,024 = 2.83; 27,399/1,037,589 = 2.64; 12,615/590,421 = 2.14 | PASS |

Footnote "Adjusted EBITDA was redefined in Q3 2025 (acquisition integration costs added back)": `10-K-FY2025.txt` l.1542 "Integration costs began in the third quarter of 2025 in connection with the July 2025 acquisition" PASS.

### 2d. business.md §4 table (every cell)

| Row | Source and arithmetic | Result |
|---|---|---|
| Operating cash flow 9.2 / 53.7 / 153.6 / 285.5 / 387.8 / 239.0 | 9,170 (`10-K-FY2021.txt` l.2245); 53,656 and 153,614 (`10-K-FY2023.txt` l.2534); 285,513 and 387,823 (`10-K-FY2025.txt` l.2443); 239,031 (10-Q l.436) | PASS |
| Free cash flow, current definition 3.0 (computed) / 43.5 (computed) / 139.9 (computed) / 264.4 (recast) / 360.4 / 226.4 | OCF − PP&E − capitalised software: 9,170−3,586−2,620 = 2,964; 53,656−5,562−4,562 = 43,532; 153,614−3,191−10,493 = 139,930; 2024 recast 264,373 stated (`10-K-FY2025.txt` l.1590, footnote l.1592 "prior period has been recast"); 360,424 stated (l.1590); 226,416 stated (10-Q l.1068) | PASS |
| Free cash flow as originally reported 12.7 / 46.2 / 144.3 / 274.9 | 12,746 (`10-K-FY2021.txt` l.1564); 46,170 (`10-K-FY2022.txt` l.1558); 144,273 (`10-K-FY2023.txt` l.1664); 274,937 (`10-K-FY2024.txt` l.1604) | PASS |
| FCF / revenue (computed) 1.2 / 11.8 / 26.3 / 35.3 / 34.7 / 38.3% | 2,964/250,772 = 1.18; 43,532/369,495 = 11.78; 139,930/531,109 = 26.35; 264,373/748,024 = 35.34; 360,424/1,037,589 = 34.74; 226,416/590,421 = 38.35 | PASS |
| Change in deferred revenue inside OCF 43.5 / 59.3 / 91.6 / 123.7 / 123.3 / 8.9 | cash-flow "Deferred revenue" lines: 43,475 (`10-K-FY2021.txt` l.2231); 91,642 / 59,283 / 43,475 (`10-K-FY2023.txt` l.2520); 123,321 / 123,692 / 91,642 (`10-K-FY2025.txt` l.2429); 8,897 vs 58,293 (10-Q l.422) | PASS |
| Stock-based compensation 40.8 / 73.8 / 95.2 / 110.5 / 137.4 / 72.9 | as in 2c | PASS |
| Net income (60.1) / (59.6) / 16.1 / 88.6 / 414.1 / 76.6 | −60,135 and −59,574 (`10-K-FY2023.txt` l.2506); 16,067 / 88,574 / 414,065 (`10-K-FY2025.txt` l.2361–2393); 76,618 (10-Q l.368, letter p.17) | PASS |
| Cash paid for employees' taxes on vesting shares — / — / 11.5 / 49.4 / 41.6 / 18.8 | "Taxes paid related to net-share settlement": none in 2021–2022 (`10-K-FY2023.txt` l.2560 "( 11,482 ) | — | —"); 41,617 / 49,358 / 11,482 (`10-K-FY2025.txt` l.2465); 18,799 (10-Q l.456) | PASS |
| Share buybacks (cash) 0.9 / — / — / — / — / 69.6 | "Repurchase of common stock ( 868 )" 2021 (`10-K-FY2021.txt` l.2265; `10-K-FY2023.txt` l.2558 shows — for 2023 and 2022); no repurchase line in `10-K-FY2025.txt` cash flow, Item 5 "Issuer Purchases of Equity Securities: None." (l.1352–1354); 69,603 (10-Q l.454) | PASS as numbers; see §10 item 3 for the sentence that contradicts the 2021 cell |
| Footnote ¹ recast definition and ² $256.7M one-time benefit | `10-K-FY2025.txt` l.1578 ("Prior to the first quarter of 2025, free cash flow added back taxes paid related to stock-based compensation equity awards, acquisition transaction costs, and acquisition earn-out payments"), l.1456 and l.3239 ($256,728) | PASS |

### 2e. outlook.md §1 table (every cell) and the guided-versus-actual table

| Cell | Source | Result |
|---|---|---|
| 1. 58.7M, +23% [Q2 letter p.8]; CURR 84%, "up by about 1%" [p.4]; Q1 56.5M, +21% [Q1 letter p.8]; "CURR not disclosed"; FY2026 DAU "about 20%" [Q4 letter p.4] | `shareholder-letter.txt` l.124 (p.8 table "47.7 | 58.7 | 23%"), l.82 (p.4: "our CURR is at an all-time high of 84%, up by about 1% from last year"); `shareholder-letter-2026-Q1.txt` l.128 ("46.6 | 56.5 | 21%"); grep "CURR" in the Q1 and Q4 letters returns nothing; `shareholder-letter-2025-Q4.txt` l.72 ("we expect 2026 DAU growth to be about 20%") | PASS |
| 2. 12.7M, +17%; Q1 12.5M, +21% | Q2 letter l.126 ("10.9 | 12.7 | 17%"); Q1 letter l.130 ("10.3 | 12.5 | 21%") | PASS |
| 3. $289.1M, +8% / +6%; $250.3M, +10% / +9%; Q1 $308.5M, +14% / +9%; $268.1M, +15%; guided $283.5M, "+5.8%" (+4.1% cc), "Q2 faces a challenging bookings growth comparable" | Q2 letter l.130–132 (table) and l.174 (p.9: "increased 8% ... or 6% on a constant-currency basis, to $289.1 million"); subscription constant-currency 9%: `10-Q-2026-Q2.txt` l.1092 ("250,316 | 227,259 | 10% | 9%"); Q1 letter l.134–136 and l.174 ("grew 14% year over year, or 9% on a constant currency basis, to $308.5 million"); Q1 letter l.194–204 and footnote l.206 ("4.1%"), l.210 (the "challenging bookings growth comparable" sentence) | PASS |
| 4. $258.0M, +22% (86%); $21.1M, +2%; $10.1M, flat; $8.0M, −23%; Q1 $250.9M, +31% (86%); $20.6M, +15%; $11.3M, −6%; $8.4M, −11%; guided revenue $295.5M, "+17.1%" | Q2 letter l.450–462 (p.19 table; 258,035/298,454 = 86.5%); Q1 letter l.458–470 (p.20 table; 250,908/291,967 = 85.9%); Q1 letter l.194–204 | PASS |
| 5. 72.6%; Q1 73.0%; "approximately 71.0% in Q2", "to approximately 69.0% by Q4" | Q2 letter l.140; Q1 letter l.144, l.214 ("We expect gross margin of approximately 71.0% in Q2. We believe gross margin will trend down to approximately 69.0% by Q4") | PASS |
| 6. $505.1M; −$8.2M (computed); Q1 $513.3M; +$17.1M (computed) | Q2 letter l.328 ("Deferred revenues | $496,205 | $505,102"); Q1 letter l.338 ("$496,205 | $513,256"). 505,102 − 513,256 = −8,154; 513,256 − 496,205 = +17,051 | PASS |
| 7. 13.4% ($40.0M); 12.7% ($37.8M); Q1 13.4% ($39.2M); 12.8% ($37.3M); Q4 guidance quote | 40,007/298,454 = 13.40 (Q2 letter l.378); 37,821/298,454 = 12.67 (l.538); 39,249/291,967 = 13.44 (Q1 letter l.388); 37,276/291,967 = 12.77 (l.540); `shareholder-letter-2025-Q4.txt` l.234 ("expect non-GAAP operating expenses to grow faster year over year than revenue in all categories, with the exception of G&A") | PASS |
| 8. 50.7M; $44.4M, 432K; $329.7M; 12.8% ($38.2M); Q1 49.7M; about $25.8M, 262K (computed); 11.9% ($34.6M); guidance "approximately 3.5-4%", "nearly 15% of revenue" | Q2 letter l.180 (p.9: "approximately 50.7 million ... approximately $44.4 million, or approximately 432 thousand shares"), l.234 (p.11 table 50.7); `10-Q-2026-Q2.txt` l.1444 ($329,722), l.854 (Note 8: 432 and 695 thousand shares, $44,448 and $70,278), l.1342 (694,630 shares); 38.2/298.454 = 12.80 (l.576 footnote "$38.2 million"); Q1 letter l.182 (49.7 million); 70,278 − 44,448 = 25,830 → $25.8M and 694,630 − 432,306 = 262,324 → 262K (10-Q l.1436–1448 for 432,306); 34.647/291.967 = 11.87 (Q1 letter l.432 cash-flow line 34,647); Q1 letter l.218–222 ("nearly 15% of revenue" on p.10; "approximately 3.5-4% in 2026. This does not include the impact of any buyback activity" on p.11) | PASS. Tag corrected by reviewer: the Q1 buyback computation now also cites 10-Q Note 8 (the half-year figures are there, not in Part II Item 2); the guidance tag now reads p.10–11 |
| Guided vs actual: $283.5M→$289.1M (+5.6); $295.5M→$298.5M (+3.0); $71.0M/24.0%→$77.3M/25.9% (+6.3; +1.9 pts); ~71.0%→72.6% (+1.6 pts) | Q1 letter l.194–204; Q2 letter l.130–140 | PASS |

Revision-path table (outlook §4): Q4 letter $1,274–1,298M (10–12%), $1,197–1,221M (15–18%), $299–305M, 25.0%, "roughly 69% for the rest of the year", "over $350 million", "almost 15%", "effective tax benefit of approximately 6%" — `shareholder-letter-2025-Q4.txt` l.200–212, l.222, l.232–238 PASS. Q1 letter $1,280M (10.5%), $1,205M (16.1%), $310M, 25.7%, "approximately 69.0% by Q4", no FCF restatement (grep "free cash flow" in the guidance pages returns none), "nearly 15%", "approximately 18-20%" — l.194–224 PASS. Q2 letter column matches the p.10 table PASS.

### 2f. outlook.md §4 quotes, word for word

| Quote (start) | Source | Result |
|---|---|---|
| Guidance table Bookings $307 / $1,285; 8.9% / 10.9%; $302 / $1,207; 11.1% / 16.3%; $76 / $320; 25.2% / 26.5% | Q2 letter l.190–202 (p.10) | PASS |
| "We continue to manage the business to the full-year targets ... stronger-than-expected gross margin performance." | l.186 | PASS, verbatim |
| "over half of our bookings come from outside the US, and we estimate ... impact on our H2 bookings." | l.208 | PASS, verbatim |
| "We expect a gross margin of approximately 71.0% in Q3 and approximately 71.6% for the full year, better than the trajectory we outlined on our Q1 call based on AI cost trends." | l.210 | PASS, verbatim |
| "We expect stock-based compensation to be around 15.0% of revenue in 2026 ... approximately 23-25% for the year." | l.214 | PASS, verbatim |
| Call-only: "we expect to generate over $375 million of free cash flow this year"; "to end the year closer to 70% as compared to the 69% we initially expected"; "a bonus plan that will trigger if Q4 DAU growth is 25% or higher and would be paid out during Q1 ... roughly $10 million in cash"; "roughly 25.5%" | `transcript.txt` l.25–26 (CFO prepared remarks) | PASS, verbatim fragments; the ellipsis skips one sentence |

### 2g. outlook.md §5 claim quotes, word for word

| Claim | Quote | Source | Result |
|---|---|---|---|
| 1 | "we expect bookings of approximately $307 million or growth of 9%." | transcript l.27 | PASS |
| 2 | "Revenue of $302 million, representing growth of 11%." | transcript l.27 | PASS |
| 3 | "We expect a gross margin of approximately 71.0% in Q3" | Q2 letter l.210 | PASS |
| 4 | "For Q3, we expect Adjusted EBITDA of approximately $76.0 million, or a 25.2% margin." | l.212 | PASS |
| 5 | "we expect DAU year-over-year growth throughout the rest of the year to remain above the 20% we had previously guided to." | l.74 (p.4) | PASS |
| 6 | "our CURR is at an all-time high of 84%, up by about 1% from last year." | l.82 (p.4) | PASS |
| 7 | "over the next few quarters ... you're going to see some improvements in our ads business." | transcript l.83 ("I would expect that over the next few quarters, that there -- that you're going to see some improvements in our ads business.") | PASS; the ellipsis removes the transcription stutter |
| 8 | "with absolute expense increasing through the year." | l.214 | PASS |
| 9 | "we expect Adjusted EBITDA of approximately $320.0 million, or a 26.5% margin." / "approximately 71.6% for the full year" | l.212, l.210 | PASS |
| 10 | "we expect to extend that access to existing Super subscribers later this year." | l.84 (p.4) | PASS |
| 11 | "we're going to have an answer to this in the next couple of quarters." | transcript l.48 | PASS |

### 2h. Other tagged sentences (18 chosen across both files)

| # | File, line | Sentence or fragment | Tag | Source | Result |
|---|---|---|---|---|---|
| 1 | business L6 | "a freemium business model: the app and the website are accessible free of charge, although Duolingo also offers premium services for a subscription fee" | 10-K FY2025, Note 1 | l.2519 | PASS |
| 2 | business L8 | "We intentionally do not put our learning content behind a paywall"; "an ad at the end of each lesson"; "an ad-free experience and access to additional features"; about 9% of MAUs pay | 10-K FY2025, Item 1 | l.290 | PASS |
| 3 | business L10 | formed August 18, 2011; app launched June 19, 2012; Carnegie Mellon professor and Ph.D. student | Item 1 / Note 1 | l.266, l.2517 | PASS |
| 4 | business L10 | "decelerated throughout 2025"; "our increased focus on monetization in recent years"; "prioritize teaching better and user growth" | Q4 2025 letter, p.4 | `shareholder-letter-2025-Q4.txt` l.72 | PASS |
| 5 | business L52 | "the initial rollout of Energy, a price increase, and advertising outperformance" | Q2 2026 letter, p.9 | l.174; "Energy" appears in no cached filing (grep of 10-K FY2025 and 10-Q returns nothing) | PASS |
| 6 | business L56 | "paid Apple and Google, as applicable, a meaningful share (generally 15-30%) of the payments we receive from transactions processed through in-app payment systems" | 10-K FY2025, Item 1A | l.662 | PASS |
| 7 | business L56 | "is the principal in the transaction with the end user" | 10-K FY2025, Note 2 | l.2551 | PASS |
| 8 | business L58 | 2025 driver "increased AI costs used in features like Video Call, and a shift in revenue mix toward advertising"; 2026 "continued reductions in per-unit third-party AI costs"; Video Call "like $0.30 per call" to "under $0.01", "mainly a move towards open source models" | 10-K FY2025 Item 7; 10-Q Item 2; Q2 call | l.1822; 10-Q l.1290; transcript l.44–45 | PASS |
| 9 | business L75 | 20,500 course units in Q1 2026, "up from 7,100 per quarter in 2025 and 1,800 per quarter in 2024" | Q1 2026 letter, p.5 | `shareholder-letter-2026-Q1.txt` l.94 | PASS |
| 10 | business L93 | valuation allowance release, "resulting in a one-time income-tax benefit ... of $256.7 million"; net income without it about $157 million (414.1 − 256.7 = 157.4) | 10-K FY2025, Note 9 | l.3239 ($256,728) and l.1456 ($256.7 million) | PASS |
| 11 | business L93 | tax 26.9% of pre-tax income in Q2 2026 vs 3.6% a year earlier "(computed)" | 10-Q, Item 1 / Item 2 | 12,208/45,366 = 26.91%; 1,669/46,450 = 3.59%; the 10-Q also states "Effective tax rate 26.9% / 3.6%" directly at l.770 (Note 7) | PASS; the "(computed)" label is unnecessary (see §10, optional) |
| 12 | business L99 | about 43 million DAUs with a 7-day streak, about 15 million with a 365-day streak; 15.4 million revived streaks "including nearly 8 million users who had no active streak" | Item 1; Q2 letter p.5 | l.312; letter l.100 | PASS |
| 13 | business L115 | "we derived 62% of our revenue and 61% of our total bookings from the Apple App Store, and 20% of our revenue and 21% of our total bookings from the Google Play Store"; Note 5 processed shares 61.6% and 23.4%; "generally terminable by Apple or Google without cause with 30 days prior written notice" | Item 1A; Note 5 | l.662, l.664; l.2875 | PASS (both figures shown and marked unreconciled; they are different measures, revenue derived vs revenue processed) |
| 14 | business L125 | China "our second largest market in terms of daily active users", largest "in a year or 2", Chinese models "by law", "I don't know what the government will decide at any point"; U.S. 38% of revenue | Q2 call; Note 5 | transcript l.107–108; l.2893 | PASS |
| 15 | business L131 | Skaruppa resigned January 8, 2026 after "nearly six years"; Munson CFO February 23, 2026, $14 million starting RSU grant; "Neither Mr. Skaruppa nor Ms. Munson resigned because of any disagreements" | 8-K 2026-01-12; DEF 14A | 8-K l.69, l.73, l.89, l.132; DEF 14A l.801 | PASS (the $14 million is in the 8-K, l.89; the sentence carries that tag) |
| 16 | business L133 | von Ahn 55.2% of Class B and 40.0% of votes; Hacker 47.7% and 35.8%; group 76.0% of votes with 1.3% of Class A; as of April 7, 2026 | DEF 14A, Security Ownership | l.1899, l.1901, l.1925, l.1865 | PASS |
| 17 | business L135 | 1,200,000 and 600,000 PSUs, hurdles $127.50 to $816, eight tranches earned; "modified the service condition applicable to the final two tranches of the Founder Awards held by one of its founders", $8.2M reversed, $7.0M Q2 benefit; 1.94M RSUs at $111.19 vs 0.60M at $391.09; $412.0M unrecognised | DEF 14A; 10-Q Note 8; 10-K Note 10 | DEF 14A l.1275, l.1283–1301, footnotes (1)–(7) l.1307–1319 cover tranches 1–8; 10-Q l.822, l.828, l.806, l.814; 10-K l.3317 | PASS |
| 18 | outlook L30 | "Our ambition is to teach a billion people, and every step we take toward a better product brings us closer to that goal" | Q2 2026 release | `press-release.txt` l.14 | PASS |
| 19 | outlook L36–46 | "we may actually sunset Max"; "1-month free trial"; Super Lite "about half the price"; "single-digit millions of DAUs"; "Asia is still the fastest growing" | Q2 call | transcript l.48, l.35, l.51, l.71, l.39 | PASS |
| 20 | business L150 | von Ahn 10b5-1 plan June 2, 2026, up to 626,000 shares plus 54,000 foundation shares, through September 15, 2027 | 10-Q, Part II Item 5 | l.1474 | PASS |

Spot-checks run: 20 sentence checks, 8 table blocks cell by cell (about 190 cells), 6 guidance quotes, 11 claim quotes. Failures: 0 on numbers or quotes. Tag corrections made by the reviewer: 4 (listed in §11). Fact-level problems for the writer: 7 (§10).

## 3. Jargon audit

Terms used and how each is handled (after the reviewer's edits):

| Term | Where | Status |
|---|---|---|
| DAU, MAU, bookings, deferred revenue, Adjusted EBITDA, free cash flow, CURR, valuation allowance, capitalised software, RSU, GAAP/non-GAAP, constant currency | throughout | In the glossary; each entry one sentence |
| freemium | §1 | Explained by the quoted 10-K sentence |
| programmatic advertising networks | §2 | Glossed "(automated ad exchanges)" by the writer |
| goodwill | §4 | Glossed inline by the writer |
| Rule 10b5-1 plan; 8-K Item 5.02 | §7, §6 | Glossed inline by the writer |
| hosting | §3 | Reviewer added "(servers)" |
| proctoring | §3 | Reviewer added "(test-supervision)" |
| amortised | §3 | Reviewer replaced with "expensed", matching the glossary entry |
| earn-outs | §4 footnote | Reviewer glossed |
| vest | §4, §7 | Reviewer glossed at first use |
| receivables | §6 | Reviewer glossed |
| CTO | §7 | Reviewer spelled out |
| tranches | §7 | Reviewer replaced with "portions" |
| fully diluted shares | §7 table, §8 | Reviewer glossed in the table cell |
| opex | outlook §1 | Reviewer replaced with "operating expenses" |
| top-of-funnel; performance marketing | outlook §3 | Reviewer glossed |
| H2 | outlook §4 (inside a verbatim quote) | Reviewer added a one-line gloss after the quote |
| G&A, YoY | outlook §1 and §4, inside verbatim management wording | Left as quoted; business.md spells both out where it uses them |
| gross margin, operating margin, operating cash flow, stock-based compensation | throughout | Name-inferable and explained by the §3 "where the money goes" paragraph; no glossary entry needed |

Glossary entries not strictly needed: "RSU / PSU" (the text never says "PSU"; it says "performance shares", which the entry explains, so it can stay); "Valuation allowance" is used once with a partial inline explanation and could be dropped if the owner wants the glossary shorter. No entry exceeds one sentence. No term in either file remains unexplained.

## 4. Invented-number check

| Item | Finding |
|---|---|
| (a) business §3: "roughly 7–17% of the $288.1 million 2025 cost of revenues (computed on $20–50 million)" | **FAIL (invented range).** The CFO said only "Our expenses on AI and cost of goods sold are tens of millions of dollars" (transcript l.110). The $20–50 million bounds are the writer's, not a source's; "tens of millions" spans $10–99 million, and the CFO did not say which year. Labelling it "(computed)" presents an assumption as arithmetic. Rule 1 requires the assumption to be dropped or stated as an assumption; dropping it is cleaner. |
| (b) Q2 2026 effective tax rates 26.9% and 3.6% "(computed)" | PASS. The arithmetic is right and the 10-Q states both rates directly (l.770). The label can go. |
| (c) Q1 2026 buyback "about $25.8M, 262K (computed: half-year less Q2 in the 10-Q)" | PASS. 70,278 − 44,448 = 25,830; 694,630 − 432,306 = 262,324. Labelled. The Q1 letter's "$50.6 million, or roughly 514,000 shares, through May 1, 2026" is a different window, so the difference is expected. Tag corrected to include Note 8. |
| (d) non-GAAP S&M percentages 12.7% and 12.8% "(computed)" | PASS. 37,821/298,454 and 37,276/291,967, from the letters' reconciliations. |
| (e) claim 1 "at least $307 million (our floor on a point estimate)" | PASS as a labelled sharpening. But claims 2–4 apply the same floor to "approximately" figures without the label; see §10 item 5. |
| (f) IPO date | PASS. The draft says "the Nasdaq listing in July 2021" and never picks a day, so the DEF 14A ("July 27, 2021", l.1279) vs 10-K ("July 30, 2021", l.3329; Item 5 "July 28, 2021" first trading day, l.1358) discrepancy is avoided rather than resolved. Acceptable. |
| (g) Google Play 20% vs 23.4% | PASS. Both shown, labelled "unreconciled". They are different measures (Item 1A: revenue derived from the store; Note 5: revenue processed by Google). |
| "flat since 2021" (von Ahn's salary, business §7) | **FAIL (unsupported).** The proxy's pay table shows $750,000 for 2023, 2024 and 2025 only (DEF 14A l.1397–1401, l.1229). No cached source gives 2021 or 2022. |
| "no buybacks before 2026" (business §7) | **FAIL (contradicts the draft's own table).** The §4 table shows $0.9 million of buybacks in FY2021 (`10-K-FY2021.txt` l.2265 "Repurchase of common stock ( 868 )", a pre-IPO repurchase). Item 5 of the FY2025 10-K says "Issuer Purchases of Equity Securities: None." for 2025 only. |
| "since the Q2 2026 10-Q 'We primarily evaluate user engagement using DAUs...'" (business §2) | **Minor FAIL (says more than the source).** The identical footnote is already in the Q1 2026 letter (`shareholder-letter-2026-Q1.txt` l.160, dated 2026-05-04) and absent from the Q4 2025 letter, so the change predates the Q2 10-Q; the Q1 10-Q is not cached. |
| "with no lead independent director" (business §7) | **Minor FAIL (inference from silence).** The proxy says the guidelines permit the independent directors to appoint one (l.813) and then describes von Ahn as chairman without naming a lead director (l.815). It does not say there is none. |
| "no debt" tagged [10-K FY2025, Item 7] (business §4 and §7 table) | Tag did not support the statement: no such sentence exists in the FY2025 10-K (grep of "debt", "borrow", "credit facility" finds only investment-related uses). The Q4 2025 letter p.10 says "no debt" (`shareholder-letter-2025-Q4.txt` l.222) and the 10-Q balance sheet carries no borrowings. **Reviewer retagged to [Q4 2025 letter, p.10]; not sent back.** |
| Everything else with a "(computed)" label | Redone above; all agree. No untagged factual sentence found outside the §8 indicator list, whose "Source:" pointers are the §6-required "where in the filings it comes from". |

## 5. Claims check (§9), outlook §5

Eleven claims (target 6–12). Each row: one sentence? one thing? single direction (can fail)? tied to metric/date/event? quote verbatim? sharpening labelled? disclosure check labelled with quarter vs year-to-date?

| # | One sentence | One thing | Can fail | Anchor | Quote | Labels | Notes |
|---|---|---|---|---|---|---|---|
| 1 | yes | yes | yes | Q3 bookings ≥ $307M | verbatim | "our floor on a point estimate" | OK |
| 2 | yes | yes | yes | Q3 revenue ≥ $302M | verbatim | none | floor on a point estimate, unlabelled (§10 item 5) |
| 3 | yes | yes | yes | Q3 gross margin ≥ 71.0% | verbatim | none | "approximately 71.0%" read as a floor, unlabelled (item 5) |
| 4 | yes | yes | yes | Q3 Adj. EBITDA ≥ $76.0M | verbatim | none | same (item 5) |
| 5 | yes | yes | yes | Q3 DAU growth > 20% | verbatim | not needed | OK; management's own words |
| 6 | yes | yes | yes | Q3 letter reports CURR ≥ 84% | verbatim | labelled disclosure check; "no figure counts as dropped" | OK; CURR is a letter metric with no quarter/YTD column, so that qualifier does not apply |
| 7 | yes | yes | yes | Q3 ad revenue growth > 2%, quarter column | verbatim | "our sharpening of 'some improvements'"; quarter stated | OK |
| 8 | yes | yes | yes | Q3 SBC (quarter) > $38.2M | verbatim | quarter stated | OK; direct reading of "increasing through the year" |
| 9 | yes | **no** | yes | reaffirm/raise FY Adj. EBITDA ~$320M **and** FY gross margin ~71.6% | verbatim (two) | — | two checks in one claim; split (§10 item 4). "reaffirms or raises" is the permitted form. |
| 10 | yes | yes | yes | Video Call to existing Super subscribers by the Q4 letter | verbatim | not needed | OK |
| 11 | yes | yes | yes | Max decision announced by the Q4 call | verbatim | not needed | OK; the "whether ... or ..." describes possible content, not an either/or verdict |

Mix: four headline-guidance claims (1–4, plus 9 on the full year), six fundamental-signal claims (5–8, 10–11). Acceptable balance; headline items do not dominate.

## 6. Indicators check (§8)

Section marked `_Proposed — owner to review and lock._`: yes (business.md L154). Outlook §1 carries exactly eight rows for the eight indicators: yes.

| # | Indicator | Recurring anchor | Comment |
|---|---|---|---|
| 1 | DAUs, quarterly average and growth (+ CURR as companion) | KPI table in every 10-Q/10-K Item 2 and letter p.3/p.8: recurring | CURR is a one-off so far: it appears only in the Q2 2026 letter (zero hits in the Q1 2026 and Q4 2025 letters). The writer says so ("given once so far") and also tracks it as claim 6. §8 prefers tracking one-offs as claims rather than indicators; recommend the owner drop CURR from the indicator row at lock time so outlook §1 does not carry a "not disclosed" cell most quarters. Not a rule failure. |
| 2 | Paid subscribers | KPI table: recurring | OK |
| 3 | Subscription and total bookings, reported and constant currency | KPI table; letter p.3, p.9: recurring | OK |
| 4 | Revenue by type | 10-Q Note 4 / 10-K Note 5; letter p.19: recurring | OK; note the FY2025 10-K MD&A collapsed the split to Subscription/Other, but the note kept it |
| 5 | Gross margin and stated driver | Item 2 paragraph; letter p.8–9: recurring | OK |
| 6 | Deferred revenue and its cash-flow change | balance sheet and cash-flow statement: recurring | OK |
| 7 | S&M as a share of revenue, GAAP and non-GAAP | income statement; letter reconciliation p.21: recurring | OK |
| 8 | Fully diluted shares, buyback cash and remaining authorisation, SBC/revenue | letter dilutive-securities table (p.11), 10-Q Part II Item 2, cash-flow statement: recurring | OK |

None is built on a one-off dollar target or growth percentage; the one-offs (20% DAU guide, 100M DAUs in 2028, $375M FCF) are handled as guidance or claims.

## 7. Skeleton check

business.md: header `_As of Q2 2026. Written 2026-09-08._` exact; headings 1–8 present and in order; §2 has a five-fiscal-year segment table (plus a Q2 2026 column) and a five-year KPI table; §3 table has revenue, gross margin, operating margin, capex (two lines) and capex/revenue for five years plus 6M 2026; §4 table five years plus 6M 2026; Glossary and Sources present; every tag prefix used (13) is mapped to a cached file in Sources (checked by script); the Sources note states the letter page convention and that the transcript has no page numbers.

outlook.md: header `_Transcript source tier: third-party (The Motley Fool machine transcript of the 2026-08-05 call, posted 2026-08-12). Written 2026-09-08._` — tier 3, name, call date and posting date all present as required; headings 1–5 present and in order; §6 Tone shift correctly omitted on a first run; Sources maps all six tag prefixes used; §1 has one row per indicator; §4 guidance quoted verbatim.

## 8. As-of check

Cutoff 2026-08-06. The transcript was posted 2026-08-12 but the call was 2026-08-05; both dates are in the header, only call content is used (§12.2). The Q2 letter's buyback figure "through August 1, 2026" is pre-cutoff. The MANIFEST lists two post-cutoff 8-Ks (2026-08-10, Items 5.02/7.01; 2026-08-19) that were not fetched; nothing in either draft depends on them. The §6 early-warning "an officer-change filing (8-K Item 5.02)" is generic and supportable without post-cutoff knowledge; the writer should confirm no post-cutoff information informed it. No sentence in either file reads as knowledge from after 2026-08-06.

## 9. Length (§3 rule 7, `wc_prose.py`)

| File | Before reviewer edits | After | Ceiling |
|---|---|---|---|
| business.md | 2,755 | 2,775 | 3,000 |
| outlook.md | 1,119 | 1,134 | 1,200 |

The writer's reported counts (2,755 / 1,119) were reproduced exactly with the same script. The REVISE items below remove more words than they add.

## 10. Verdict: REVISE — list for the writer

Rule failures (fix all):

1. **business §3, L56 — invented range.** Delete "roughly 7–17% of the $288.1 million 2025 cost of revenues (computed on $20–50 million)". The CFO said "tens of millions of dollars" (transcript l.110) and nothing narrower; the $20–50 million bounds are yours. Keep the quote. If you want scale, write: 'against $288.1 million of 2025 cost of revenues [10-K FY2025, Item 8]' with no percentage.
2. **business §7, L135 — unsupported date.** "Von Ahn's salary is $750,000, flat since 2021" → the proxy pay table shows $750,000 for 2023, 2024 and 2025 only (DEF 14A l.1397–1401). Write "flat since at least 2023 (the earliest year in the proxy's pay table)".
3. **business §7, L137 — contradicts the §4 table.** "No dividend, ever, and no buybacks before 2026" conflicts with the FY2021 "Share buybacks (cash) 0.9" cell (10-K FY2021 cash flow, "Repurchase of common stock (868)"). Write "no buyback programme before 2026 (the $0.9 million in 2021 was a repurchase before the listing)", or footnote the table cell the same way.
4. **outlook §5, claim 9 — two things in one claim.** Split into "management reaffirms or raises full-year Adjusted EBITDA of approximately $320 million" and "management reaffirms or raises full-year gross margin of approximately 71.6%", each with its own quote, or drop the gross-margin half (claim 3 already covers Q3 gross margin). Either way the count stays within 6–12.
5. **outlook §5, claims 2–4 — unlabelled floors.** Claims 2, 3 and 4 read "approximately"/point estimates as "at least" without the label claim 1 carries. Add one sentence above the list: "Claims 1–4 read management's point estimates as floors; that is our convention, not management's wording", and then either drop the parenthesis in claim 1 or repeat it in 2–4.
6. **business §2, L50 — says more than the source.** "since the Q2 2026 10-Q 'We primarily evaluate user engagement using DAUs...'" → the same footnote is in the Q1 2026 letter (May 2026), so the change did not start with the Q2 10-Q. Write "and, per the Q2 2026 10-Q, ..." or "since 2026 (first in the Q1 2026 letter) ...", adding [Q1 2026 letter, p.8] if you use the second form.
7. **business §7, L131 — inference stated as fact.** "with no lead independent director" → the proxy says the guidelines permit one and names none (DEF 14A l.813–815). Write "and the proxy names no lead independent director".

Optional, not rule failures (owner's or writer's taste):

- business §5, L105: "DAU growth (23%) below the 20% guided for 2026" reads as if 23 were below 20; "DAU growth (now 23%) falling below the 20% guided for 2026" is clearer.
- business §4, L93: the 10-Q states the 26.9% and 3.6% effective tax rates directly (Note 7, l.770); "(computed)" can be dropped and the tag pointed at [10-Q Q2 2026, Note 7].
- business §8 / outlook §1 row 1: consider dropping CURR from indicator 1 (it is already claim 6); see §6 above.
- Glossary: "RSU / PSU" could become "RSU" alone, since the text says "performance shares"; harmless as is.

## 11. Direct edits made by the reviewer (tags, jargon, typos only)

Tag corrections (4):

| File, line | Before | After | Reason |
|---|---|---|---|
| business L95 (end of the return-on-capital paragraph) | `[10-Q Q2 2026, Item 1] [10-K FY2025, Item 7]` | `[10-Q Q2 2026, Item 1] [Q4 2025 letter, p.10]` | "no debt" is not stated in the FY2025 10-K; it is stated at Q4 2025 letter p.10 (l.222) and shown by the 10-Q balance sheet |
| business L148 (cash-and-debt table row) | `[10-Q Q2 2026, Item 1] [10-K FY2025, Item 7]` | `[10-Q Q2 2026, Item 1] [Q4 2025 letter, p.10]` | same |
| business L142 (shares-bought table row) | `[10-Q Q2 2026, Part II Item 2]` | `[10-Q Q2 2026, Note 8] [10-Q Q2 2026, Part II Item 2]` | Part II Item 2 has only the Q2 monthly table and the $329,722 remaining; 695K shares / $101.15 / $70,278 are in Note 8 (l.854) and 694,630 in Item 2 (l.1342) |
| outlook L17 (indicator 8, Q1 cell and guidance cell) | `[10-Q Q2 2026, Part II Item 2]`; `[Q1 2026 letter, p.11]` | `[10-Q Q2 2026, Note 8] [10-Q Q2 2026, Part II Item 2]`; `[Q1 2026 letter, p.10–11]` | half-year buyback figures are in Note 8; "nearly 15% of revenue" is on p.10 and "3.5-4%" on p.11 |
| outlook L78 (revision-path table, DAU row) | three untagged cells | added `[Q4 2025 letter, p.4]`, `[Q1 2026 letter, p.4]`, `[Q2 2026 letter, p.4]` | the column-header tags (p.10–11) did not cover these p.4 statements |

Jargon glosses (13; before → after):

- business L56: "Hosting and AI scale with usage" → "Hosting (servers) and AI scale with usage"
- business L58: "DET proctoring costs" → "DET proctoring (test-supervision) costs"
- business L75: "amortised over three years" → "expensed over three years"
- business L91: "acquisition costs and earn-outs;" → "acquisition costs and earn-outs (later payments owed to sellers of acquired businesses);"
- business L93: "when shares vest the company pays" → "when shares vest (become the employee's) the company pays"
- business L127: "of receivables at June 30, 2026" → "of receivables (money owed to Duolingo) at June 30, 2026"
- business L131: "is CTO, co-founder" → "is CTO (chief technology officer), co-founder"
- business L135: "vesting in ten tranches" → "vesting in ten portions"
- business L145: "Fully diluted shares (company estimate)" → "Fully diluted shares (company estimate: shares outstanding plus options and unvested grants)"
- outlook L16: "Non-GAAP opex" → "Non-GAAP operating expenses"
- outlook L34: "Performance marketing is ... showing 'up in top-of-funnel growth'" → "Performance marketing (paid advertising) is ... showing 'up in top-of-funnel growth' (more people trying the app)"
- outlook L62: added "(H2 is the second half of the year.)" after the verbatim FX-sensitivity quote

Typos: none found (scanned for doubled words, doubled spaces, stray punctuation, the transcript's "Gilian" misspelling).

## 12. Withdrawn or near-miss findings (recorded per §17)

- **"no debt" [10-K FY2025, Item 7]** — first ruling: unsourced (no "debt" sentence in the 10-K). Printed the Q4 2025 letter p.10 in full: "We are entering 2026 from a position of financial strength, with healthy profitability, a strong cash position, no debt, and the expectation of generating over $350 million of free cash flow this year." Retagged rather than failed.
- **FY2025 in-app purchases 40.5** — a grep for "In-App Purchases |" found nothing in the FY2025 10-K; printing Note 5 in full showed the row is labelled "IAPs | 40,479 | 38,653 | 34,673" (l.2869). PASS.
- **FY2021 Other 0.1** — grep for "Other |" missed the FY2023 10-K row because it is labelled "Other (1) | 682 | 625 | 79" (l.2824). PASS.
- **Change in deferred revenue (cash-flow row)** — grep for "Deferred revenues |" matched only balance-sheet lines; the cash-flow line is singular, "Deferred revenue | 123,321 | 123,692 | 91,642" (`10-K-FY2025.txt` l.2429). PASS.
- **Munson's $14 million grant tagged [DEF 14A 2026, Executive Transition]** — not in the proxy's Executive Transition paragraph; found in the 8-K 2026-01-12 exhibit (l.89), which the same sentence also cites. PASS.
- **"eight are earned"** — the proxy's tranche footnotes run (1)–(7), but tranches 1 and 2 share footnote (1), so tranches 1–8 are marked achieved (l.1283–1319). PASS.

## 13. Cycle 2 (2026-09-08) — re-verification from disk and final verdict

Both files were re-read from disk. Word counts after the writer's second pass (`wc_prose.py`): business.md 2,774 (ceiling 3,000), outlook.md 1,135 (ceiling 1,200).

### 13a. The seven REVISE items

| # | Item | What the file now says | Source check | Result |
|---|---|---|---|---|
| 1 | business §3 L56, invented 7–17% range | Range deleted; the CFO quote stands and is followed by "the dollar figure is not disclosed [Q2 2026 call]" | `transcript.txt` l.110 gives only "tens of millions of dollars"; no figure anywhere else | PASS |
| 2 | business §7 L135, "flat since 2021" | "Von Ahn's salary is $750,000, flat across the three years the proxy shows" | `DEF14A-2026.txt` l.1397–1401: 750,000 for 2025, 2024, 2023 | PASS |
| 3 | business §7 L137 vs §4 table | "no buyback programme before 2026 [10-K FY2025, Item 5]"; §4 table cell now "0.9³" with footnote ³ "A pre-IPO repurchase tied to a February 2021 tender offer, not a buyback programme [10-K FY2021, Item 8]" | `10-K-FY2021.txt` l.2881 (Note 9, inside Item 8, which begins at l.1994): "In February 2021, the Company initiated a tender offer which allowed employees to sell up to 10% of their vested options or shares back to the Company ... 23 shares were retired with an $868 decrease to Additional paid-in capital"; cash-flow l.2265 "Repurchase of common stock ( 868 )"; IPO July 2021 (`10-K-FY2025.txt` l.3329), so the repurchase was pre-IPO; `10-K-FY2025.txt` l.1352–1354 "Issuer Purchases of Equity Securities: None." | PASS |
| 4 | outlook §5 claim 9, two things | Now "management reaffirms or raises full-year Adjusted EBITDA of approximately $320 million" only, with its single quote | `shareholder-letter.txt` l.212 | PASS; 11 claims remain |
| 5 | outlook §5 claims 2–4, unlabelled floors | New sentence above the list: 'Where management gave an "approximately" point estimate (claims 1–4), we treat the figure as a floor; this is our sharpening, not management's number.' Claim 1's parenthetical removed | Methodological note; no tag needed | PASS |
| 6 | business §2 L50, "since the Q2 2026 10-Q" | Now "and per the Q2 2026 10-Q" | `10-Q-2026-Q2.txt` l.962 | PASS |
| 7 | business §7 L131, lead director | Now "the proxy names no lead independent director [DEF 14A 2026, Board Leadership Structure]" | Heading exists at `DEF14A-2026.txt` l.811; text l.813–815 permits a Lead Director and names none | PASS |

### 13b. Optional suggestions the writer took

- business §5 L105: "DAU growth (23% now) falling below the 20% guided for 2026" — clear now.
- business §4 L93: tax rates 26.9% / 3.6% retagged to [10-Q Q2 2026, Note 7], "(computed)" dropped — `10-Q-2026-Q2.txt` l.770 states both rates in Note 7. PASS.
- business §8 indicator 1: CURR now "Companion: CURR (84%), letter-only and may not recur" — accurate (one letter so far). The owner still decides at lock time whether to keep it in the row.
- Glossary: "RSU (restricted stock unit): a share grant that vests with time; the founders' awards instead vest when share-price targets are met." One sentence; PSU dropped. PASS.

### 13c. Trims and survival of cycle-1 edits

- Trims checked: the dropped §4 sentence repeated the $8.9 million half-year deferred-revenue change, which remains in §2 L52 (tagged) and in the §4 table; the §8 closing line, the §6.2 "(§2)" cross-reference, outlook §2 "The target:" and the shortened China "Working if" removed no tag-bearing fact that a table or later sentence depends on.
- All cycle-1 reviewer edits are present: "(servers)", "(test-supervision)", "expensed over three years", the earn-out gloss, "(become the employee's)", "(money owed to Duolingo)", "CTO (chief technology officer)", "ten portions", the fully-diluted-shares gloss, the [Q4 2025 letter, p.10] retags (L95, L148), the [10-Q Q2 2026, Note 8] tags (business L142, outlook L17), [Q1 2026 letter, p.10–11], "Non-GAAP operating expenses", the top-of-funnel and performance-marketing glosses, the H2 gloss, and the three p.4 tags in the revision-path DAU row.
- Tag sweep: every tag prefix in both files maps to a cached file in Sources (13 prefixes in business.md, 6 in outlook.md). The only untagged prose sentence is the new §5 convention note, which is not a factual claim.

### 13d. Claims re-check

Eleven claims (target 6–12). Each is one sentence, one thing, single-direction and anchored to a metric, date or event; every quote re-matched the source word for word (claims 1, 2, 7, 11 to `transcript.txt` l.27, l.27, l.83, l.48; claims 3, 4, 8, 9 to `shareholder-letter.txt` l.210, l.212, l.214, l.212; claims 5, 6, 10 to l.74, l.82, l.84). Claim 7's sharpening and claim 6's disclosure-check label are intact; the new convention sentence covers claims 1–4.

### 13e. Direct edits in cycle 2

None needed. Typo scan (doubled words, doubled spaces, stray punctuation) clean.

### 13f. Final verdict: PASS

Nothing remains open. Two notes for the owner at indicator-lock time, not defects: whether CURR stays as a companion in indicator 1 (it has appeared in one letter), and whether the eleven-entry glossary should lose "Valuation allowance" (used once, partly explained inline).
