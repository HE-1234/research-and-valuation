# Amazon.com, Inc. (AMZN) — Reviewer report, 2026-Q2 (cycle 1 of 2)

_Reviewed 2026-09-08 against `companies/AMZN/sources/2026-Q2/` only: the cached full texts, not the gatherers' notes (the notes were not needed, because no failure below is a wrong number). Line numbers (`l.N`) refer to the cached `.txt` files. Proxy pages are the printed footers (`2026 Proxy Statement N` on odd pages, a bare number on even pages); letter pages are PDF pages (`\f` count); the transcript has no pages, so transcript checks cite its line numbers (one paragraph per line). Apostrophes and whitespace were normalised before any quote was ruled wrong; every full line was printed before any fact was ruled unsourced (AGENTS.md §17). Word counts use `/tmp/amzn-orch/wc_prose.py` only._

**Verdict: REVISE (light).** No number in either file is wrong and every verbatim quote matches its source. Four items need the writer because they change table cells or claims, which the reviewer may not touch: one indicator cell on a different basis from its neighbour when the like-for-like figure is in a cached filing, one claim that cannot be graded because the metric has never been disclosed, one claim that needs a rule for silence, and one table cell whose period does not match its column header. Everything else found (five tag gaps, three unlabelled inferences, one over-reaching attribution, fourteen jargon glosses) was fixed directly and is listed under "Fixed by reviewer".

---

## 1. Skeleton compliance

**business.md**

| Requirement (§6) | Status |
|---|---|
| `# <Company> — The Business` | OK (`# Amazon.com, Inc. — The Business`) |
| `_As of <QLABEL>. Written <date>._` | OK (`_As of Q2 2026. Written 2026-09-08._`; fiscal = calendar, no parenthetical needed) |
| §1 What they do, with a short history paragraph | OK; history at l.10 (1994, May 1996–July 2021, May 1997 IPO, Netflix 2008, Whole Foods 2017, Graviton 2018, Leo seven years) |
| §2 How the money comes in, 5-year segment table | OK; two tables (segments; product/service lines), FY2021–FY2025 plus 1H 2026 |
| §3 The economics (revenue, gross margin, operating margin, capex, capex/revenue, 5 years) | OK; plus depreciation row, an operating-expense-mix table and a segment-margin table. Gross margin labelled computed and explained as flattering |
| §4 How profitable, really (table, 5 years) | OK; segment operating income table, cash-flow table with all three of Amazon's historical free-cash-flow measures, return-on-capital paragraph |
| §5 Why customers don't leave (moat, source, sign of weakening) | OK; four customer groups, each with a source and a sign |
| §6 What could break it (ranked; concentration) | OK; six scenarios ranked, each with trigger, early warning and exposure; concentration paragraph present |
| §7 Who runs it and what they do with the cash | OK; people, pay, cash, and a twelve-row capital table |
| §8 Indicators (5–8, name / why / where) | OK; eight, each anchored to a recurring disclosure (see §6 below) |
| `_Proposed — owner to review and lock._` | OK (l.168) |
| Glossary | OK; six one-sentence entries (AWS, Trainium and Graviton, Fulfillment, Depreciation, Free cash flow, Backlog) |
| Sources | OK; all 14 tag families used in the body map to a cached file (checked by script: 155 tags, 14 families, 14/14 present) |
| Heading order | OK |
| Length 2,000–3,000 prose words | OK: 2,792 before review, 2,888 after the reviewer's glosses |

**outlook.md**

| Requirement (§7) | Status |
|---|---|
| `# <Company> — Outlook as of <QLABEL>` | OK |
| `_Transcript source tier: ... Written <date>._` | OK: `third-party (The Motley Fool)`, matching MANIFEST (tier 3; call 2026-07-30, posted 2026-08-07) |
| §1 one row per indicator; this quarter / last quarter / what management had said | OK; eight rows matching business.md §8 one for one; three data columns; basis differences stated in-cell (see REVISE item 1) |
| §2 What management says | OK; quotes verbatim, argument labelled as management's |
| §3 Growth engines (what / how big / claim / working-or-not) | OK; five engines |
| §4 Guidance, verbatim | OK; the three release bullets word for word (checked below); call figures labelled as spoken from a machine transcript, with the filed figure alongside |
| §5 Claims | OK; ten claims (target 6–12); two headline, eight fundamentals |
| §6 Tone shift | Correctly omitted (first run) |
| Sources | OK; all 6 tag families used in the body map to a cached file (59 tags, 6/6 present); the transcript entry states tier, both dates, and the numbers-from-release rule |
| Length 800–1,200 prose words | OK: 1,093 before review, 1,097 after |

---

## 2. Rubric (§14)

1. **What the company does and who pays it, in two sentences?** Yes. §1 l.6–8: the store (shoppers, sellers, advertisers pay) and AWS (companies and governments pay to rent computing), with the 82% / 57% split of sales and profit.
2. **What would kill it and the early warning sign?** Yes. §6 ranks six scenarios; each names the trigger, the early warning (backlog stalling while capex rises and the term loan being drawn; AWS growth slowing two quarters; an order changing offer ranking or Prime bundling; online-store growth turning negative; fulfillment-plus-shipping cost outgrowing units; Leo slipping past 2026) and the exposed profit pool.
3. **Why the margins are what they are and whether cost scales with usage?** Yes. §3 answers it in two halves (store linear, AWS fixed-asset-heavy), explains why Amazon reports no gross margin and why the computed row flatters, and shows the mix shift in the operating-expense table.
4. **Could I predict the scorecard from §5 alone?** Mostly. Eight of ten claims name the document and the number or sentence to look for. Claim 9 depends on a robotic-arm count Amazon has never published; claim 10 does not say how to grade a silent 10-Q. Both are on the REVISE list.
5. **Nothing required knowledge I don't have?** Yes after this pass. Fourteen terms were glossed (weighted-average remaining life, expensed, provision, marketable securities, structural relief, omnichannel, customer concentration, independent-chair proposal, finance leases, stock-based compensation, facility, carrying value, trailing twelve months, ad inventory); nothing open remains.

---

## 3. Citation spot-check

Legend: PASS = number or quote found at the tagged location; PASS (tag) = right number, tag repaired by the reviewer; FAIL = wrong or unsupported. Every "(computed)" cell was re-derived from its sourced inputs.

### 3(a) business.md §2 segment table (l.14–19), every cell

Inputs: `10-K-FY2023.txt` Note 10 l.2285–2297 (2021–2023); `10-K-FY2025.txt` Note 10 l.2297–2309 (2023–2025); `10-Q-2026-Q2.txt` Note 8 l.824–836 (six months 2026).

| Row | FY21 | FY22 | FY23 | FY24 | FY25 | 1H26 | Source values (USD m) | Result |
|---|---|---|---|---|---|---|---|---|
| North America | 279.8 | 315.9 | 352.8 | 387.5 | 426.3 | 220.3 | 279,833 / 315,880 / 352,828 / 387,497 / 426,305 / 220,320 | PASS ×6 |
| International | 127.8 | 118.0 | 131.2 | 142.9 | 161.9 | 82.0 | 127,787 / 118,007 / 131,200 / 142,906 / 161,894 / 81,986 | PASS ×6 |
| AWS | 62.2 | 80.1 | 90.8 | 107.6 | 128.7 | 79.8 | 62,202 / 80,096 / 90,757 / 107,556 / 128,725 / 79,819 | PASS ×6 |
| Total | 469.8 | 514.0 | 574.8 | 638.0 | 716.9 | 382.1 | 469,822 / 513,983 / 574,785 / 637,959 / 716,924 / 382,125 | PASS ×6 |

24/24 PASS. The 2023 column is identical in both 10-Ks (no restatement).

### 3(b) business.md §2 product-line table (l.21–30), every cell

Inputs: `10-K-FY2023.txt` l.2314–2321; `10-K-FY2025.txt` l.2326–2333; `10-Q-2026-Q2.txt` l.853–860 (six-month column).

| Row | Source values (USD m), FY21 / FY22 / FY23 / FY24 / FY25 / 1H26 | Result |
|---|---|---|
| Online stores 222.1 / 220.0 / 231.9 / 247.0 / 269.3 / 134.7 | 222,075 / 220,004 / 231,872 / 247,029 / 269,287 / 134,686 | PASS ×6 |
| Physical stores 17.1 / 19.0 / 20.0 / 21.2 / 22.6 / 11.6 | 17,075 / 18,963 / 20,030 / 21,215 / 22,561 / 11,579 | PASS ×6 |
| Third-party seller services 103.4 / 117.7 / 140.1 / 156.1 / 172.2 / 88.4 | 103,366 / 117,716 / 140,053 / 156,146 / 172,162 / 88,358 | PASS ×6 |
| Advertising services 31.2 / 37.7 / 46.9 / 56.2 / 68.6 / 37.1 | 31,160 / 37,739 / 46,906 / 56,214 / 68,635 / 37,052 | PASS ×6 |
| Subscription services 31.8 / 35.2 / 40.2 / 44.4 / 49.6 / 27.2 | 31,768 / 35,218 / 40,209 / 44,374 / 49,619 / 27,157 | PASS ×6 |
| AWS 62.2 / 80.1 / 90.8 / 107.6 / 128.7 / 79.8 | as 3(a) | PASS ×6 |
| Other 2.2 / 4.2 / 5.0 / 5.4 / 5.9 / 3.5 | 2,176 / 4,247 / 4,958 / 5,425 / 5,935 / 3,474 | PASS ×6 |
| Total | as 3(a) | PASS ×6 |

48/48 PASS. Footnote definitions (1)–(6) are word-for-word identical across the three filings apart from the order of examples in footnote (6), so "Definitions were unchanged throughout" holds; the sentence was tagged only to the FY2023 note, which covers 2021–2023 alone (PASS (tag), fixed: `[10-K FY2025, Note 10] [10-Q Q2 2026, Note 8]` added at l.32).

### 3(c) business.md §3 first table (l.50–57), every cell

| Row | Check | Result |
|---|---|---|
| Net sales | as 3(a); income statements `10-K-FY2023` l.1227, `10-K-FY2025` l.1179, `10-Q` l.181 | PASS ×6 |
| Gross margin (computed) 42.0 / 43.8 / 47.0 / 48.9 / 50.3 / 52.0% | (net sales − cost of sales) / net sales. Cost of sales 272,344 / 288,831 / 304,739 (`10-K-FY2023` l.1229); 326,288 / 356,414 (`10-K-FY2025` l.1181); 183,241 (`10-Q` l.183). Re-derived 42.03 / 43.81 / 46.98 / 48.85 / 50.29 / 52.05% | PASS ×6; labelled computed and "Amazon does not report it", per `10-K-FY2025` l.919 |
| Operating margin (computed) 5.3 / 2.4 / 6.4 / 10.8 / 11.2 / 13.4% | Operating income 24,879 / 12,248 / 36,852 (`10-K-FY2023` l.1236); 68,593 / 79,975 (`10-K-FY2025` l.1188); 51,313 (`10-Q` l.190). Re-derived 5.30 / 2.38 / 6.41 / 10.75 / 11.16 / 13.43% | PASS ×6 |
| Cash capex 55.4 (computed) / 58.3 / 48.1 / 77.7 / 128.3 / 96.3 | FY2021 = 61,053 − 5,657 = 55,396 (`10-K-FY2023` l.1192–1193), correctly labelled computed. FY2022–FY2023 stated as 58,321 / 48,133 (`10-K-FY2023` Item 7 l.970); FY2024–FY2025 as 77,658 / 128,320 (`10-K-FY2025` Item 7 l.966); 1H 2026 "$96.3 billion" (`10-Q` Item 2 l.986) and 98,411 − 2,101 (`10-Q` l.145–146) | PASS ×6; the Item 7 / Item 2 locations were missing from the sources line: PASS (tag), fixed at l.59 |
| Capex / net sales (computed) 11.8 / 11.3 / 8.4 / 12.2 / 17.9 / 25.2% | Re-derived 11.79 / 11.35 / 8.37 / 12.17 / 17.90 / 25.20% | PASS ×6 |
| Depreciation of P&E 22.9 / 24.9 / 30.2 / 32.1 / 41.9 / 13.9 (Q2 alone) | 22,909 / 24,924 / 30,225 (`10-K-FY2023` Note 10 l.2403); 32,067 / 41,860 (`10-K-FY2025` Note 10 l.2427; Note 3 l.1762 says $32.1B / $41.9B); Q2 2026 13,869 (`10-Q` Note 8 l.933) | PASS ×6; but the last cell is a quarter under a half-year header (REVISE item 4; the six-month figure 26,703 is on the same line) |

36/36 PASS.

### 3(d) business.md §3 operating-expense table (l.61–67), every cell

| Column | Source | Draft vs source (cost of sales / fulfillment / T&I / S&M / G&A) | Result |
|---|---|---|---|
| FY2021 (computed) | income statement `10-K-FY2023` l.1229–1233 over 469,822 | 57.97→58.0 / 15.99→16.0 / 11.93→11.9 / 6.93→6.9 / 1.88→1.9 | PASS ×5 |
| FY2022 | `10-K-FY2023` Item 7 "Percent of Net Sales" l.881–886 | 56.2 / 16.4 / 14.2 / 8.2 / 2.3 stated | PASS ×5 |
| FY2023 | same table; also `10-K-FY2024` l.853–858 | 53.0 / 15.8 / 14.9 / 7.7 / 2.1 stated in both | PASS ×5 |
| FY2024 | `10-K-FY2024` l.853–858 and `10-K-FY2025` l.851–856 | 51.1 / 15.4 / 13.9 / 6.9 / 1.8 stated in both | PASS ×5 |
| FY2025 | `10-K-FY2025` l.851–856 | 49.7 / 15.2 / 15.1 / 6.6 / 1.6 stated | PASS ×5 |
| 1H 2026 | `10-Q` Item 2 l.1083–1087 (six-month column) | 48.0 / 14.9 / 16.4 / 5.8 / 1.4 stated | PASS ×5 |

30/30 PASS. Prose at l.71: T&I "grew 23% in 2025" is stated at `10-K-FY2025` l.848; "fulfillment fell as a share of sales for the third straight year" follows from 16.4 → 15.8 → 15.4 → 15.2.

### 3(e) business.md §3 segment-margin table (l.75–79), every cell

Segment operating income / segment net sales from the 3(a) and 3(f) inputs.

| Row | Re-derived | Result |
|---|---|---|
| North America 2.6 / (0.9) / 4.2 / 6.4 / 6.9 / 7.9% | 2.60 / −0.90 / 4.22 / 6.44 / 6.95 / 7.89% | PASS ×6 |
| International (0.7) / (6.6) / (2.0) / 2.7 / 2.9 / 3.8% | −0.72 / −6.56 / −2.02 / 2.65 / 2.93 / 3.83% | PASS ×6 |
| AWS 29.8 / 28.5 / 27.1 / 37.0 / 35.4 / 38.6% | 29.79 / 28.52 / 27.14 / 37.04 / 35.43 / 38.56% | PASS ×6 |

18/18 PASS. Footnote (l.81): $2.5B FTC settlement in Q3 2025 in North America, `10-K-FY2025` Note 1 l.1330; $1.4B extra depreciation from the six-to-five-year server-life change, mostly AWS, l.1328. PASS ×2.

### 3(f) business.md §4 segment operating income table (l.85–91), every cell

| Row | Source values (USD m) | Result |
|---|---|---|
| North America 7.3 / (2.8) / 14.9 / 25.0 / 29.6 / 17.4 | 7,271 / (2,847) / 14,877 (`10-K-FY2023` l.2287); 24,967 / 29,619 (`10-K-FY2025` l.2299); 17,390 (`10-Q` l.826) | PASS ×6 |
| International (0.9) / (7.7) / (2.7) / 3.8 / 4.8 / 3.1 | (924) / (7,746) / (2,656) (l.2291); 3,792 / 4,750 (l.2303); 3,141 (`10-Q` l.830) | PASS ×6 |
| AWS 18.5 / 22.8 / 24.6 / 39.8 / 45.6 / 30.8 | 18,532 / 22,841 / 24,631 (l.2295); 39,834 / 45,606 (l.2307); 30,782 (`10-Q` l.834) | PASS ×6 |
| Total 24.9 / 12.2 / 36.9 / 68.6 / 80.0 / 51.3 | 24,879 / 12,248 / 36,852 / 68,593 / 79,975 / 51,313 | PASS ×6 |
| AWS share (computed) 74 / 186 / 67 / 58 / 57 / 60% | 74.49 / 186.49 / 66.84 / 58.07 / 57.03 / 59.99% | PASS ×6 |

30/30 PASS. Prose l.95: stores' $34.4B (29,619 + 4,750 = 34,369) and 43% (34,369 / 79,975 = 42.97%) PASS ×2.

### 3(g) business.md §4 cash-flow table (l.97–105), every cell

| Row | Source values | Result |
|---|---|---|
| Operating cash flow 46.3 / 46.8 / 84.9 / 115.9 / 139.5 / 161.4 | 46,327 / 46,752 (`10-K-FY2023` l.1190); 84,946 / 115,877 / 139,514 (`10-K-FY2025` l.1143); TTM 161,403 (`10-Q` l.143; release l.233, l.412) | PASS ×6 |
| Cash capex 55.4 / 58.3 / 48.1 / 77.7 / 128.3 / 169.0 | as 3(c); TTM 173,028 − 4,021 = 169,007, stated at release l.415 and `10-Q` l.1188 | PASS ×6 |
| Free cash flow (9.1) (computed) / (11.6) / 36.8 / 38.2 / 11.2 / (7.6) | 46,327 − 55,396 = −9,069 (computed, labelled); (11,569) / 36,813 (`10-K-FY2023` l.971); 38,219 / 11,194 (`10-K-FY2025` l.967); (7,604) (release l.416; `10-Q` l.1190) | PASS ×6 |
| FCF less finance-lease and financing-obligation repayments (20.4) (computed) / (19.8) / 32.2 / 35.5 / 9.3 (computed) / not presented | −9,069 − 11,163 − 162 = −20,394; (19,758) / 32,158 (`10-K-FY2023` l.990); 35,507 (`10-K-FY2024` l.982); 11,194 − 1,557 − 328 = 9,309 from `10-K-FY2025` l.1156–1157 (measure dropped; correctly labelled computed); not in the 10-Q | PASS ×6 |
| FCF less equipment finance leases etc. not in sources / (12.8) / 35.5 / 36.2 / not disclosed / not presented | FY2021 not in any cached filing (the FY2023 10-K starts at 2022): correct; (12,786) / 35,549 (`10-K-FY2023` l.1006); 36,211 (`10-K-FY2024` l.1002); FY2025 needs the equipment-finance-lease split that the FY2025 10-K no longer gives: correct | PASS ×6 |
| Net income 33.4 / (2.7) / 30.4 / 59.2 / 77.7 / 135.3 | 33,364 / (2,722) / 30,425 (`10-K-FY2023` l.1178); 59,248 / 77,670 (`10-K-FY2025` l.1130); TTM 135,281 (`10-Q` l.128; release l.435) | PASS ×6 |
| FCF / OCF (computed) (20) / (25) / 43 / 33 / 8 / (5)% | −19.6 / −24.7 / 43.3 / 33.0 / 8.0 / −4.7% | PASS ×6 |

42/42 PASS. The sources line's statement that the FY2025 10-K dropped the two lease-adjusted measures is correct: `10-K-FY2025` Item 7 l.957–971 contains one measure only.

### 3(h) business.md §4 prose and §7 table

| # | Figure or quote | Tag | Found | Result |
|---|---|---|---|---|
| 1 | "increase of $66.1 billion in purchases of property and equipment" ... "primarily reflects investments in artificial intelligence" | Q2 2026 release | l.30–32 | PASS |
| 2 | $27.0B of equipment received but not paid in accounts payable at end-2025; $20.6B added in 1H 2026 | 10-K Note 3; 10-Q Note 1 | l.1760 ($16.8B and $27.0B); `10-Q` l.324 (20,620) | PASS ×2 |
| 3 | Q2 net income $62.6B; $53.4B other income; $50.5B Anthropic mark-up "to reflect observable changes in price related to Anthropic's fundings"; $15.9B tax in the six-month provision | release; 10-Q Note 2; Note 7 | release l.24–27, l.285; `10-Q` l.474 (quote word for word), l.226 of Note 7 range (l.789) | PASS ×4 |
| 4 | Q1 2026 gain $16.8B | Q1 2026 release | l.20–21 | PASS |
| 5 | ~$640M tariff refunds in North America cost of sales; $551M unrealized energy gains mostly AWS; CFO "approximately $1.2 billion" | 10-Q Note 1; call | `10-Q` l.305, l.367; transcript l.50–51 | PASS ×3 (the call's two "approximately $600 million" figures are not used; the 10-Q figures are, correctly) |
| 6 | Return on capital 18 / 27 / 22 / 21 cents (computed); $446B P&E | 10-K Item 8, Note 10; 10-Q Item 1; release | 36,852 / 204,177 = 18.05%; 68,593 / 252,665 = 27.15%; 79,975 / 357,025 = 22.40%; TTM operating income 93,712 (release l.430) / 446,046 (`10-Q` l.254) = 21.01% | PASS ×5 |
| 7 | Cash and marketable securities $123.0B; face value of debt $133.0B; $25.0B July notes | 10-Q Note 2, Note 5; 8-K 07-09 | `10-Q` l.441 (122,988); Note 5 face value 132,995; 8-K eight tranches 750 + 3,500 + 4,250 + 3,000 + 4,500 + 2,750 + 4,000 + 2,250 = 25,000 (Item 8.01) | PASS ×3 |
| 8 | §7 table: $6.0B buyback in 2022; none 2023–2025 or 1H 2026; $6.1B of $10.0B left | 10-K FY2023 Note 8; 10-K FY2025 Note 8; 10-Q Note 6 | `10-K-FY2023` l.1199 and l.2067; `10-K-FY2025` l.2034; `10-Q` Note 6 ("no repurchases ... six months ended June 30, 2025 or 2026 ... $6.1 billion remaining") | PASS ×3 |
| 9 | Shares 10,175M → 10,731M → 10,783M | 10-K FY2023 Item 8; 10-K FY2025 Item 8; 10-Q Item 1 | l.1340; l.1266; `10-Q` l.271 | PASS ×3 |
| 10 | Stock-based compensation $19.5B FY2025 | 10-K FY2025 Note 8 | l.2051 (19,467) | PASS |
| 11 | Notes $68.0B → $132.1B; $17.5B term loan, single draw by 9/30/2026, signed 6/2026 | 10-K Note 6; 10-Q Note 5; 8-K 06-10 | `10-K-FY2025` l.1894; `10-Q` Note 5 first paragraph and term-loan paragraph; 8-K Item 1.01 (agreement dated June 8, 2026; commitments expire September 30, 2026) | PASS ×4 |
| 12 | Anthropic: $8.0B convertible notes Q3 2023–Q4 2025; $10.0B preferred in Q2 2026; facility up to $20.0B, $15.0B available | 10-Q Note 2 | l.462; $5.0B Series G + $5.0B Series H; "not to exceed $20.0 billion ... reduced the amount available under the facility to $15.0 billion" | PASS ×3 |
| 13 | OpenAI: $15.0B Q1; $13.7B Q2; $21.3B after quarter end; $50.0B total | 10-Q Note 2; 8-K 02-27 | l.480–484; 8-K Item 1.01 ($35.0B commitment "separate from and in addition to" $15.0B) | PASS ×4 |
| 14 | Carrying value $16.2B → $122.3B | 10-Q Note 2 | l.486 | PASS |
| 15 | Globalstar ~$10.9B including debt, agreed 4/13/2026, close 2027 | 10-Q Note 4 | Note 4 commitments paragraph (April 13, 2026; "approximately $10.9 billion, including its debt"; "expected to close in 2027") | PASS |
| 16 | "approximately $200 billion in capex in 2026" (letter); "approximately $220 billion in cash CapEx in 2026" (call) | letter p.5; call | letter p.5 l.214 ("We're not investing approximately $200 billion in capex in 2026 on a hunch"); transcript l.39 | PASS ×2 |
| 17 | Rural network "over $4 billion" | letter p.2 | p.2 l.56 | PASS |

### 3(i) outlook.md §1 indicator table (l.10–17) and headline (l.19), every cell

| Cell | Tag | Found | Result |
|---|---|---|---|
| AWS +37%; 39.4% | Q2 2026 release | l.17; l.474 (16,621 / 42,232 = 39.36%) | PASS ×2 |
| AWS +28%; 37.7% (Q1) | Q1 2026 release | l.13; l.472 | PASS ×2 |
| Backlog ~$496B; 6.4 years at 6/30/2026 | 10-Q Q2 Note 1 | l.397 | PASS ×2 |
| Backlog ~$364B; 5.5 years at 3/31/2026 | 10-Q Q1 Note 1 | `10-Q-2026-Q1` l.391 | PASS ×2 |
| Cash capex $53.1B; TTM FCF $(7.6)B | 10-Q Item 2; release | `10-Q` l.986; release l.416 | PASS ×2 |
| Q1 capex $43.2B (computed: 44,203 − 969); TTM FCF $1.2B | Q1 2026 release | l.237–238 (three-month column); l.414 (1,232) | PASS ×2 |
| "approximately $200 billion in capex in 2026" | letter p.5 | l.214 | PASS |
| Ads +26% ($19.8B); +24% ($17.2B) | Q2 release; Q1 release | l.490 (19,809; 26%); Q1 l.488 (17,243; 24%) | PASS ×4 |
| Seller services +16%; units +17%; sellers 61% | Q2 release | l.488, l.510, l.511 | PASS ×3 |
| +14%; +15%; 60% (Q1) | Q1 release | l.486, l.508, l.509 | PASS ×3 |
| NA 7.9%; Intl 4.1%; Q1 7.9%; 3.6% | releases | Q2 l.454, l.464; Q1 l.452, l.462 | PASS ×4 |
| "between $20.0 billion and $24.0 billion" | Q1 release | l.170 | PASS |
| T&I 16.5%; Q1 16.3% (computed 29,567 / 181,519) | 10-Q Item 2; Q1 release | `10-Q` l.1085; Q1 l.278 / l.274 = 16.29% | PASS ×2 |
| $133.0B face value; $123.0B; 10,783M at 6/30/2026 | 10-Q Note 5, Note 2, Item 1 | 132,995; l.441; l.271 | PASS ×3 |
| Balance-sheet LTD $119.1B; $143.1B (computed 101,816 + 41,273); 10,754M at 3/31/2026 | Q1 release | l.389; l.372–373; l.416 | PASS ×3 (right numbers; basis point in REVISE item 1) |
| "We expect to undertake additional financing activities in 2026." | 10-Q Item 2 | l.994 | PASS |
| Headline: $200.6B and $27.5B beat "$194.0 billion and $199.0 billion" / "$20.0 billion and $24.0 billion" | Q2 release; Q1 release | Q2 l.12, l.18; Q1 l.167, l.170 | PASS ×4 |

44/44 PASS.

### 3(j) outlook.md §4 guidance, word for word

| Quote | Source | Result |
|---|---|---|
| "Net sales are expected to be between $197.0 billion and $202.0 billion, or to grow between 9% and 12% compared with third quarter 2025. Excluding the impact of Prime Day in both 2025 and 2026, third quarter 2026 year-over-year growth would be nearly 400 basis points higher. This guidance anticipates an unfavorable impact of approximately 80 basis points from foreign exchange rates." | release l.164–167 (also `10-Q` l.1229) | PASS |
| "Operating income is expected to be between $22.5 billion and $26.5 billion, compared with $17.4 billion in third quarter 2025." | release l.168–169 | PASS |
| "This guidance assumes, among other things, no impact from energy derivative contract remeasurements, and that no additional business acquisitions, restructurings, or legal settlements are concluded." | release l.170–171 | PASS |
| "We now believe we will spend approximately $220 billion in cash CapEx in 2026. The higher cost of memory pushing this number up from our prior estimate of about $200 billion." | transcript l.39 | PASS |
| "Even at that amount, we will still not have enough capacity to meet all the demand we have in 2026, and I believe this dynamic will also be true in 2027, too." | transcript l.39 | PASS |
| "we'll spend a lot of CapEx and encounter free cash flow headwinds until these data centers come online, can be monetized, and we get a few years into these servers being utilized." | transcript l.38 | PASS |
| "first-half cash capex was $96.3 billion" (filed figure alongside) | `10-Q` Item 2 l.986 | PASS |

7/7 PASS. The release gave no full-year, segment, margin, capex or free-cash-flow guidance (l.155–171): correct.

### 3(k) outlook.md §5 claim quotes, word for word

| # | Quote | Transcript / release line | Result |
|---|---|---|---|
| 1 | "Net sales are expected to be between $197.0 billion and $202.0 billion" | release l.164 | PASS |
| 2 | "Operating income is expected to be between $22.5 billion and $26.5 billion" | release l.168 | PASS |
| 3 | "We now believe we will spend approximately $220 billion in cash CapEx in 2026." | l.39 | PASS |
| 4 | "Our backlog stands at $496 billion, growing triple digits year-over-year." | l.23 | PASS |
| 5 | "accelerating for the fifth straight quarter" | l.23 | PASS |
| 6 | "I believe this dynamic will also be true in 2027, too." | l.39 | PASS |
| 7 | "double the power capacity by the end of 2027 that we had in 2025, and we continue to be on that track" | l.75 | PASS |
| 8 | "enough to begin initial satellite internet service this year." | l.48 (also release l.146) | PASS |
| 9 | "more than double our fleet of robotic arms, like Cardinal and Sparrow, in 2026." | l.53 | PASS |
| 10 | "represents the significant majority of refunds we expect to receive." | l.50 | PASS |

10/10 PASS.

### 3(l) Other source-tagged sentences (business.md unless noted)

| # | Sentence or figure | Tag | Found | Result |
|---|---|---|---|---|
| 1 | Prime "a membership program that includes fast, free shipping on tens of millions of items, access to award-winning movies and series, live sports, and other benefits" (l.8) | 10-K Item 1 | l.152 | PASS |
| 2 | "We are not the seller of record in these transactions. We earn fixed fees, a percentage of sales, per-unit activity fees, interest, or some combination thereof" (l.8) | 10-K Item 1 | l.158 (source continues ", for our seller programs"; quote closes before the comma) | PASS |
| 3 | 82% of 2025 sales from the stores; AWS 57% of operating profit (computed) (l.8) | 10-K Note 10 | (426,305 + 161,894) / 716,924 = 82.04%; 45,606 / 79,975 = 57.03% | PASS ×2 |
| 4 | Bezos founded 1994, CEO May 1996–July 2021; Jassy led AWS from 2006 (l.10) | 10-K Item 1 | l.217, l.219 (SVP AWS from April 2006) | PASS ×3 |
| 5 | IPO May 1997 (letter p.10); Netflix 2008 (p.1); Whole Foods 2017 (p.3); Graviton 2018 (p.4); Leo "seven years" (p.2) (l.10) | letter | p.10 l.458 "our initial public offering in May 1997"; p.1 l.20; p.3 l.120–121; p.4 l.183–184; p.2 l.65 | PASS ×5 |
| 6 | Sellers 61% of units in Q2 2026 (l.36) | Q2 release | l.511 | PASS |
| 7 | Sponsored Products the largest format; Prime Video and live sports (l.38); CFO "double-digit" membership growth (l.40) | call | l.45–46; l.52 | PASS ×2 |
| 8 | AWS services "as a fixed quantity over a specified term" (l.42) | 10-K Note 1 | l.1390 | PASS |
| 9 | Backlog $496B at 6/30/2026, up from $244B at year end; 6.4 years; twelve-month share not disclosed; 3.3 years of trailing AWS revenue (computed) (l.42) | 10-Q Note 1; 10-K Note 1; release | `10-Q` l.397; `10-K` l.1639 ($244 billion, 4.1 years); no twelve-month split anywhere in the 10-Q; 496 / 148.404 (release l.470) = 3.34 | PASS ×4 |
| 10 | Shipping costs $102.7B in 2025 (l.46); "majority of infrastructure costs" ... "are allocated to the AWS segment based on usage" | 10-K Item 7; Note 10 | l.865; l.2274 | PASS ×2 |
| 11 | "We believe that operating income is a more meaningful measure than gross profit and gross margin" (l.48); service sales 49% → 59% (computed) | 10-K Item 7; Items 8 | l.919; 228,035 / 469,822 = 48.5%, 420,658 / 716,924 = 58.7% | PASS ×2 |
| 12 | Leo costs expensed until the service "achieves commercial viability" (l.71) | 10-K Item 7 | l.885 | PASS |
| 13 | "investments in technology infrastructure (the majority of which is to support AWS business growth)"; "to increase in 2026" (l.73) | 10-K Item 7; 10-Q Item 2 | `10-K` l.761; `10-Q` l.986 | PASS ×2 |
| 14 | $142B total P&E additions in 2025, 68% to AWS (computed) (l.73) | 10-K Note 10 | l.2402–2404: 96,496 / 142,352 = 67.8% | PASS ×2 |
| 15 | "continue offering them indefinitely" (l.117); "over 40% more items same day or overnight"; paid units +17%; "people consider you for a lot more of their total purchases and shopping visits" | 10-Q Item 2; call; release; call | `10-Q` l.1130; transcript l.43; release l.510; transcript l.99 | PASS ×4 |
| 16 | "China-based sellers account for significant portions of our third-party seller services and advertising revenues" (l.119) | 10-K Item 1A | l.321 | PASS |
| 17 | "want their AI inference to reside near their other applications and data, and more of it resides in AWS than anywhere else" (l.121); "contractual obligations related to the performance of AWS chips" | call; 10-Q Note 1 | l.24; `10-Q` l.399–401 (both OpenAI and Anthropic) | PASS ×2; the clause "so both have agreed to run on Trainium" is supported by release l.45–46, not by Note 1: PASS (tag), fixed |
| 18 | Notes $68.0B → $132.1B; "additional financing activities in 2026"; "two years before"; "for 30-plus years"; "a little less than three years"; "at least five to six years"; "contracted for at least five-year terms" (l.129) | 10-K Note 6; 10-Q Note 5; 10-Q Item 2; call | l.1894; Note 5 opening; l.994; transcript l.35–36 | PASS ×7 |
| 19 | "companies that provide information technology services or products"; "a limited group of suppliers for semiconductor products" (l.131) | 10-K Item 1; 1A | l.178; l.453 | PASS ×2 |
| 20 | Antitrust quotes and status (l.133): "abuse of dominance, monopolization, and attempted monopolization"; "pricing policies, selection of the Featured Offers, use of seller data, advertising practices, the structure of Prime, and promotion of our own products"; "structural relief"; "most of Amazon's motions to dismiss were granted in part, but in each case, at least some of the claims survived"; one U.S. class certified, three pre-certification | 10-Q Note 4 | Note 4 legal paragraph (curly apostrophe in "Amazon's" normalised) | PASS ×5 |
| 21 | $2.5B Q3 2025 charge for "a lawsuit with the FTC" not identified by case (l.133) | 10-K Note 1 | l.1330 | PASS |
| 22 | "its fulfillment network and Prime"; "gatekeepers"; "tax and other challenges in Italy" (l.133) | 10-K Item 1A; 10-Q Item 1A | `10-K` l.557; `10-Q` l.1593 | PASS ×3 (attribution wording tightened, see Fixed) |
| 23 | $241B of 2025 seller-services and advertising sales (computed) | 10-K Note 10 | 172,162 + 68,635 = 240,797 | PASS |
| 24 | "physical, e-commerce, and omnichannel retailers"; "tariffs proposed or implemented by the U.S. and other countries" (l.135) | 10-K Item 1; 1A | l.178; l.411 | PASS ×2 |
| 25 | About 1.6 million employees; "if successful, decrease our operational flexibility"; "the characterization of delivery drivers"; "over one million robots" (l.137) | 10-K Item 1; 1A; letter p.2 | l.190 (1,576,000); l.449; l.561; p.2 l.47 | PASS ×4 |
| 26 | "approximately $1 billion of higher year-over-year Amazon Leo costs" (l.139) | 10-K Item 7 | l.1005 | PASS |
| 27 | "no vendor accounted for 10% or more of our purchases" (l.141) | 10-K Note 7 | l.1978 | PASS |
| 28 | Jassy 58, CEO since July 2021; Olsavsky CFO since June 2015; Garman AWS since June 2024; Herrington stores since July 2022 (l.145) | 10-K Item 1 | l.210, l.219, l.225, l.221, l.223 | PASS ×5 |
| 29 | Bezos 62; 950 million shares, 8.8%, February 2026; "is appropriate given Mr. Bezos's role in founding Amazon and his significant ownership stake" (l.145) | DEF 14A p.45, p.16 | age at `10-K` l.209 (tag added); p.45 l.2244 (950,434,581; 8.8%; table "as of February 24, 2026" l.2241); p.16 l.798 | PASS ×3 |
| 30 | Eleven directors after Keith Alexander did not stand; independent-chair proposal 14% (computed) (l.145) | DEF 14A p.2; 8-K 05-22 | p.2 l.597, l.593 (April 7, 2026); 8-K: 1,112,511,990 for / 6,730,245,638 against = 14.2% (14.1% counting abstentions) | PASS ×2 |
| 31 | Blue Origin about $1.8B since the start of 2025 (l.145) | DEF 14A p.69 | l.3086 ("Since the beginning of the last fiscal year ... approximately $1.8 billion is estimated to have been paid to Blue Origin") | PASS |
| 32 | $365,000 salary; "No annual cash bonuses or incentive awards"; "we avoid tying compensation to discrete, short-term performance goals, financial or otherwise" (l.147) | DEF 14A p.51; p.46 | l.2534 (p.51); l.2351 and l.2314 (both p.46) | PASS ×3 |
| 33 | Jassy's 2021 grant vesting 50,000 shares a quarter through February 2031; no named-executive grant in 2025; Bezos "has never received any stock-based compensation" (l.147) | DEF 14A p.56, p.57 | l.2731 (p.57: 50,000 on each quarterly date to February 21, 2031); l.2697 (p.56); l.2685 (p.56); "has not granted our CEO an award since 2021" also at p.28 l.1313 | PASS ×3 |
| 34 | Say-on-pay 78% (2025) → 94% (2026) (computed) (l.147) | DEF 14A p.28; 8-K 05-22 | l.1298; 7,391,737,243 / (7,391,737,243 + 470,466,853) = 94.0% (93.7% counting abstentions) | PASS ×2 |
| 35 | "long-term, sustainable growth in free cash flow" (l.149) | 10-K Item 7 | l.694, l.961 | PASS |
| 36 | outlook l.23–27: "I'll start with AWS, which is booming right now"; "very possibly be a trillion-dollar annual revenue business for us in time"; "growth in one is driving growth in the other"; "85% of the global IT spend is still on premises"; "ROIC equation"; "We've done this before in the first era of cloud computing"; "record delivery speeds"; "the second largest grocer in the U.S." | call | l.23, l.40, l.25, l.73, l.23, l.39, l.42, l.41 | PASS ×8 |
| 37 | outlook l.31–39: fastest in 18 quarters; "a $25 billion annual revenue run rate" for AI and for chips; "largely reserved"; "a real chance"; "all sold out"; "over $150 billion in gross sales in 2025"; "2,300 cities"; Amazon Now nine countries, over 250 cities; nearly 400 satellites | release; call; letter p.3 | release l.6, l.42–44, l.109, l.145–146; transcript l.79, l.83, l.46, l.101; letter p.3 l.134 | PASS ×9 |

**Citation tally.** Table cells: 24 + 48 + 36 + 30 + 18 + 30 + 42 = 228, all PASS. Outlook §1 cells 44, guidance and claim quotes 17, other tagged sentences and figures about 115. **About 404 checks; 0 wrong numbers, 0 altered quotes; 5 tag gaps and 3 unlabelled inferences (listed in §5 and under "Fixed by reviewer"), all repaired directly.** No failure traced to a gatherer note; all were writer-side tagging or labelling.

**Checked and cleared (recorded per §17 so the same worry is not raised again):**
- "No annual cash bonuses or incentive awards" was not on p.51; the full line shows it on p.46 (l.2351), which the sentence also tags. Cleared.
- Letter p.1 l.9 reads "May 1997", but that is Jassy's own start date; the IPO sentence is on p.10 (l.458), which is what the draft tags. Cleared.
- The Q2 release's supplemental table shows Q1 2026 advertising growth of 22% and seller-services growth of 12% (l.491, l.489), against the outlook's 24% and 14%; those release rows are ex-FX, and the Q1 release's reported Y/Y column (l.488, l.486) gives 24% and 14%. The Q2 column's 26% and 16% are the same on both bases. Basis is consistent (reported). Cleared.
- The CFO said "approximately $600 million" for each one-off (transcript l.50–51); the draft uses the 10-Q's $640 million and $551 million and attributes only the $1.2 billion total to the CFO. Correct handling of a machine transcript. Cleared.
- The call says grocery was "over $150 billion in gross merchandise sales" (l.100); the draft's "over $150 billion in gross sales in 2025" is tagged to the letter (p.3 l.134), where that is the exact wording. Cleared.

---

## 4. Jargon audit

Read as a smart 16-year-old with no finance background. FIXED items were glossed inline by the reviewer, meaning unchanged.

| File:line | Term | Status |
|---|---|---|
| business.md:42 | "weighted-average remaining life" | FIXED: "(the typical contract, weighted by size, has 6.4 years left to run)" |
| business.md:71 | "expensed" | FIXED: "(counted as a cost at once, not spread over years)" |
| business.md:102 (table label) | "principal repayments of finance leases and financing obligations" | FIXED: "(long-term equipment and building leases that count like loans)" |
| business.md:111 | "provision" | FIXED: "(the tax charge booked for the half-year)" |
| business.md:113 | "marketable securities" | FIXED: "(investments that can be sold quickly)" |
| business.md:133 | "structural relief" (inside a quote) | FIXED: gloss after the quote, "(court-ordered changes to how the business is built, up to a break-up)" |
| business.md:135 | "omnichannel" (inside a quote) | FIXED: "(omnichannel means selling both online and in stores)" |
| business.md:141 | "customer concentration" | FIXED: "(a single customer large enough to have to be named)" |
| business.md:145 | "independent-chair proposal" | FIXED: "a shareholder proposal to require a board chair from outside management" |
| business.md:156 (table) | "Stock-based compensation expense" | FIXED: "(pay given in shares)" |
| business.md:159 (table) | "facility" | FIXED: "(standing arrangement to lend)" |
| business.md:161 (table) | "Carrying value" | FIXED: "(value on Amazon's books)" |
| outlook.md:12 (row label) | "trailing-twelve-month" | FIXED: "(last four quarters combined)" |
| outlook.md:19 | "the guided" | FIXED: "the April guidance of" |
| outlook.md:33 | "inventory" (advertising sense) | FIXED: "(ad slots)" |

Already plain or glossed by the writer and left alone: segments (l.6), backlog (l.42 and glossary), depreciated (l.46), gross margin and operating income (l.48), capex (l.55), the operating-expense labels (l.63–67), FTC (l.81), operating cash flow (l.99), accounts payable (l.109), preferred stock, deferred, unrealized (l.111), face value (l.113), inference (l.121), notes, ROIC, term loan (l.129), antitrust, class action, certified (l.133), restricted stock units (l.147), convertible notes (l.159); outlook: on premises (l.23), ROIC, headwind (l.25), run rate (l.31), basis points and energy derivative remeasurements (l.49), monetized (l.55). Banned-word scan (leverage, synergy, headwind, tailwind, monetize, ecosystem, at scale, robust, unlock): "headwind(s)" and "monetized" appear only inside management's verbatim words with a gloss outside the quote; nothing in the writer's own prose. Glossary: six entries, one sentence each, all used repeatedly; nothing to add or cut. No paragraph is mostly numbers; the §7 cash paragraph is two sentences above a table.

---

## 5. Invented-number check

No figure lacks a tag; after the five tag repairs no tag fails to support its figure. Special-attention items:

| Item | Finding |
|---|---|
| Shares of operating income "supplied by AWS" | 57% (FY2025) is labelled computed at l.8 and in the §4 table row; l.129 repeated it bare: FIXED, "(computed, §4)". 74 / 186 / 67 / 58 / 57 / 60% all re-derived (3(f)). |
| Return-on-capital figures | 18 / 27 / 22 / 21 cents labelled computed, inputs tagged, arithmetic right (3(h) #6); the "slipping because assets are bought ahead of revenue" sentence is labelled "Our inference". |
| Gross margin | Labelled "(computed; Amazon does not report it)" in the table and explained in prose with the 10-K quote (l.919). The "its climb mostly reflects service sales" reading was an interpretation stated as fact: FIXED, "our inference" inserted. |
| ~$220 billion capex | Labelled a spoken figure from a machine transcript at l.73 and l.163 and in outlook l.51–53, with "No filing gives a 2026 figure" (true: `10-Q` l.986 says only "expect to increase in 2026"). l.129's "the roughly $220 billion of 2026 spending" leans on the label two paragraphs above; acceptable. |
| ~$600 million one-offs | Draft uses the 10-Q figures ($640M, $551M; `10-Q` l.305, l.367) and quotes the CFO only for the $1.2B total. Correct. |
| Backlog figures and dates | $496B / 6.4 years at 6/30/2026 (`10-Q` l.397); $364B / 5.5 years at 3/31/2026 (`10-Q-2026-Q1` l.391); $244B at 12/31/2025 (`10-K` l.1639). All PASS; the outlook table states the dates. |
| Debt and the 07-09 8-K | $68.0B → $132.1B notes; $133.0B face value; $25.0B closed 7/9/2026 (eight tranches sum to $25,000M); $17.5B undrawn term loan. All PASS. The §7 table's "issued 7/9/2026" matches the 8-K's closing date. |
| Buyback authorization | $6.1B of $10.0B remaining at 6/30/2026 (`10-Q` Note 6); no repurchases 2023–1H 2026 (`10-K` l.2034; Note 6); $6.0B in 2022 (`10-K-FY2023` l.1199, l.2067). PASS. |
| Bezos ownership and proxy page | 950,434,581 shares, 8.8%, table as of February 24, 2026, printed page 45 (l.2241–2244; page 44 ends at l.2235, page 45 at l.2304). PASS. |
| Jassy's RSU vesting | 50,000 shares on each quarterly date from May 21, 2026 to February 21, 2031, footnote on printed page 57 (l.2731; page 56 ends at l.2701). "Only award since becoming CEO is the 2021 grant" is supported by p.28 l.1313 ("has not granted our CEO an award since 2021"). PASS. |
| Say-on-pay | 78% of votes cast in 2025 (p.28 l.1298); 2026: 94.0% excluding abstentions, 93.7% including them, both round to 94% (8-K 05-22). PASS, labelled computed. |
| Founding and launch dates | 1994, May 1996, July 2021, April 2006, May 1997, 2008, 2017, 2018, "seven years" all verified (3(l) #4–5). PASS. |
| Other inferences | l.149 "two AI labs that are also AWS's biggest committed customers" was an inference no source states: FIXED to the sourced fact ("have each also signed AWS commitments of $100 billion or more [10-Q Q2 2026, Note 1]", l.399–401). l.133 "Regulators who label Amazon an online gatekeeper": the 10-K (l.557) says regulators characterise technology companies as gatekeepers, not Amazon by name: FIXED to "Regulators who treat large technology companies as online 'gatekeepers'". Remaining labelled inferences (l.46, l.113, l.119, l.121, l.123, l.147) are correctly marked. |
| Dates inferred | §7 table l.160 "$21.3B after quarter end ... to 7/2026": the 10-Q says only "Subsequent to June 30, 2026" (l.484); the month follows from the 07-31 filing date. Acceptable; optional to write "after 6/30/2026". |

---

## 6. Claims check (§9) and indicators (§8)

| # | Claim (short) | One thing? | Single direction? | Label right? | Quote matches? | Gradeable next quarter? |
|---|---|---|---|---|---|---|
| 1 | Q3 net sales $197.0–202.0B | Yes | Yes | Headline guidance | Yes | Yes (Q3 release) |
| 2 | Q3 operating income $22.5–26.5B | Yes | Yes | Headline guidance | Yes | Yes |
| 3 | Management reaffirms or raises ~$220B 2026 capex on the Q3 call | Yes | Yes (a cut = missed; silence = dropped) | Management claim | Yes | Yes |
| 4 | Disclosure check: Q3 10-Q backlog above $496B at 9/30/2026 | Yes | Yes | Labelled disclosure check; point-in-time stated; sharpening labelled | Yes | Yes (10-Q Note 1 sentence) |
| 5 | Q3 AWS growth ≥ 30% | Yes | Yes | Sharpening labelled, "no AWS guidance was given" | Yes | Yes (release segment table) |
| 6 | Management again says capacity short of demand in 2026 and 2027 | Two years, both observable in one sentence on the call | Yes | Management claim | Yes | Yes (met / missed / dropped) |
| 7 | Management again says on track to double power capacity by end-2027 vs 2025 | Yes | Yes | Management claim | Yes | Yes |
| 8 | Leo begins initial service before end-2026 | Yes | Yes | Year-end horizon stated | Yes | Yes when the horizon arrives; ⏳ at Q3 |
| 9 | Robotic-arm fleet more than doubles in 2026 | Yes | Yes | Year-end horizon stated; "needs a disclosed count" | Yes | **No.** No cached source gives a robotic-arm count (the letter gives only "over one million robots", p.2 l.47), so nothing can be compared; as written it can only ever be ⏳ or 🔇. REVISE item 2 |
| 10 | Disclosure check: Q3 tariff refunds (quarter alone) below Q2's ~$640M | Yes | Yes | Labelled disclosure check; "quarter alone" stated | Yes | Only if the Q3 10-Q states a figure; the claim does not say how a silent 10-Q is graded. REVISE item 3 |

Ten claims, within 6–12; two headline, eight fundamentals (capex, backlog, AWS growth, capacity, power, Leo, robotics, tariffs). No either/or constructions, no "or explains why", no unobservable halves. Sharpenings (4, 5) are labelled ours; disclosure checks (4, 10) are labelled and state point-in-time / quarter-alone.

**Indicators (business.md §8).** All eight anchor to disclosures that recur every quarter: (1) AWS growth and margin, release segment table and 10-Q Note 8; (2) backlog and weighted-average remaining life, the Note 1 performance-obligations paragraph, present in every 10-K and 10-Q in the cache (l.1639 / l.391 / l.397); (3) cash capex and TTM free cash flow, release supplemental table and 10-Q Item 2 reconciliation; (4) advertising growth, release product-line table; (5) seller services, paid units and seller unit mix, release product-line table and business metrics; (6) North America and International margins, release segment table; (7) technology-and-infrastructure share of net sales, 10-Q Item 2 percent-of-net-sales table; (8) face value of debt, cash and marketable securities, shares outstanding, 10-Q Note 5, Note 2 and balance sheet. None depends on a one-off call figure; the $220B capex figure is tracked as a claim, not an indicator, as §8 asks. Outlook §1 has one row per indicator and the three required columns, and states the basis of every Q1 cell; the one avoidable basis mismatch is REVISE item 1.

---

## 7. As-of discipline

Every tagged document is dated on or before the 2026-07-31 cutoff: 10-K FY2025 (filed 2026-02-06), 10-K FY2024, 10-K FY2023, 10-Q Q1 2026 (2026-04-30), 10-Q Q2 2026 (2026-07-31), DEF 14A (2026-04-09), 8-Ks of 02-27, 05-22, 06-10 and 07-09, the Q1 release (2026-04-29), the Q2 release (2026-07-30), the letter (April 2026), and the 2026-07-30 call. The transcript was posted 2026-08-07; only call content is used (every transcript citation was located in the call text, none in Fool's editorial sections, which were not cached), and both dates are in MANIFEST and in both Sources lists. Nothing in either file refers to Q3 2026 results, to the Globalstar S-4 (filed 2026-07-31, not cached), or to any event after the call; the "$21.3B after quarter end" OpenAI payment comes from the 10-Q (l.484). No slides were cited, so no slide-page question arises.

---

## 8. Verdict: REVISE (light)

Nothing below is a wrong number or an altered quote. Items 1–4 change table cells or claims and are therefore the writer's.

1. **outlook.md:17, row 8, Q1 2026 column.** The Q2 cell is the face value of long-term debt ($133.0B, 10-Q Note 5) but the Q1 cell is balance-sheet long-term debt ($119.1B) "because face value is not in the release". The face value is in the cached Q1 10-Q: `10-Q-2026-Q1.txt` l.615, "Total face value of long-term debt | 68,836 | 122,632". Replace with "$122.6B face value at 3/31/2026 [10-Q Q1 2026, Note 5]" so the indicator's two columns share the basis business.md §8 indicator 8 names; keep $143.1B and 10,754M as they are.
2. **outlook.md:67, claim 9.** No filing, release or letter gives a robotic-arm count, so "more than doubles during 2026" cannot be graded even at year-end. Rewrite as a management-statement check with the same quote, for example: "By the Q4 2026 call or the 2026 shareholder letter, management says the fleet of robotic arms more than doubled in 2026 (year-end horizon)." Met / missed / dropped are then all possible.
3. **outlook.md:68, claim 10.** Add where it is graded and what silence means, for example: "graded on the tariff-refund sentence in the Q3 10-Q Note 1; a 10-Q that gives no refund figure is graded 🔇 Dropped, not Met." Otherwise a silent filing could be read either way.
4. **business.md:57, depreciation row, last cell.** "13.9 (Q2 alone)" sits under the "1H 2026" header that every other cell in the table uses. Use the six-month figure, 26.7 (`10-Q-2026-Q2.txt` Note 8 l.933: "Consolidated | $9,766 | $13,869 | $18,822 | $26,703"), or change the header for that cell. Cosmetic, but the refresh agent will build a series from this row.

Optional, not required for PASS: business.md:160 "to 7/2026" could read "after 6/30/2026" (the 10-Q gives no month); business.md:8 and l.129 could say "operating income" rather than "operating profit" in one place for consistency with the tables.

### Fixed by reviewer (§13: tags, glosses, labels, small wording; no number, quote, claim, indicator or structure changed)

Tags:
- business.md:32 added `[10-K FY2025, Note 10] [10-Q Q2 2026, Note 8]` to "Definitions were unchanged throughout" (the FY2023 note covers 2021–2023 only).
- business.md:59 added "net capex as stated in the free cash flow reconciliations [10-K FY2023, Item 7] [10-K FY2025, Item 7] [10-Q Q2 2026, Item 2]" (l.970; l.966; l.986), the locations that state the FY2022–1H 2026 net capex figures the table presents as reported.
- business.md:111 added `[Q2 2026 call]` to the Prime Day sentence; the Q1 10-Q (l.1187) only says the Q2 guidance assumed Prime Day in Q2 2026 and the release (l.165) only implies 2025's timing; transcript l.59 states "In 2025, Prime Day was entirely in Q3."
- business.md:121 added `[Q2 2026 release]` (l.45–46 names Trainium) after "so both have agreed to run on Trainium"; Note 1 says only "AWS chips".
- business.md:145 added `[10-K FY2025, Item 1]` (l.209) for Bezos's age.

Labels and wording (meaning preserved or tightened to the source):
- business.md:48 "its climb mostly reflects" → "its climb, our inference, mostly reflects".
- business.md:129 "AWS supplied 57% of 2025 operating income" → "... (computed, §4)".
- business.md:133 "Regulators who label Amazon an online gatekeeper" → "Regulators who treat large technology companies as online "gatekeepers"" (10-K Item 1A l.557 wording).
- business.md:149 "two AI labs that are also AWS's biggest committed customers" → "two AI labs that have each also signed AWS commitments of $100 billion or more [10-Q Q2 2026, Note 1]" (l.399–401).

Glosses: the fifteen items in §4 above (twelve in business.md, three in outlook.md).

No typos found in either file.

### Word counts (canonical script, prose words only)

| File | Before review | After reviewer edits | Target |
|---|---|---|---|
| business.md | 2,792 | 2,888 | 2,000–3,000 |
| outlook.md | 1,093 | 1,097 | 800–1,200 |

Both inside their ceilings; no trim needed. The writer's four REVISE edits add at most a few words.

### Withdrawals

None. Five potential findings were examined and cleared before being written up (listed at the end of §3 with the evidence); no finding was made and then withdrawn.

---

## Cycle 2 (focused re-check of the writer's second pass, 2026-09-08)

_Same rules and sources as cycle 1. Both drafts re-read from disk; line numbers refer to the revised drafts and the cached `.txt` files. Word counts from `/tmp/amzn-orch/wc_prose.py` only._

### 1. REVISE list — resolution

| # | Item | Status |
|---|---|---|
| 1 | outlook.md §1 row 8, Q1 2026 cell on the face-value basis | **Resolved.** Cell now reads "$122.6B; $143.1B (computed: $101,816M + $41,273M); 10,754M at 3/31/2026 [10-Q Q1 2026, Note 5] [Q1 2026 release]" (l.17). Verified: `10-Q-2026-Q1.txt` l.615 "Total face value of long-term debt | 68,836 | 122,632" → $122.6B; Q1 release l.372–373 cash 101,816 + marketable securities 41,273 = 143,089 → $143.1B; shares 10,754 at Q1 release l.416. Both columns of the indicator are now face value, matching business.md §8 indicator 8. The §1 intro (l.6) dropped "and note any basis difference", which is correct now that no cell differs in basis; the two "(computed: ...)" annotations in rows 3 and 7 remain and are right. |
| 2 | outlook.md claim 9 not gradeable | **Resolved.** Now a labelled statement check: "By the Q4 2026 call or the 2026 shareholder letter, management says the fleet of robotic arms more than doubled in 2026 (year-end horizon; a statement check, since no cached source gives an arm count)." One thing to check; single direction (said it doubled = met; said otherwise or gave a smaller multiple = missed; silence = dropped); the "or" concerns the venue, not the outcome; quote unchanged and still matches transcript l.53. |
| 3 | outlook.md claim 10 silence rule | **Resolved.** Now "graded on the tariff-refund sentence in the Q3 2026 10-Q Note 1, and a 10-Q with no refund figure is graded Dropped, not Met." Labelled disclosure check, "the quarter alone" stated, threshold $640 million is the 10-Q figure (`10-Q-2026-Q2.txt` l.305); quote unchanged and matches transcript l.50. |
| 4 | business.md §3 depreciation cell period | **Resolved.** Last cell is 26.7 (`10-Q-2026-Q2.txt` Note 8 l.933: "Consolidated | $9,766 | $13,869 | $18,822 | $26,703", six-month column). The source line (l.59) now says "1H 2026, every cell a six-month figure"; checked cell by cell: net sales 382,125 (l.181), gross margin from cost of sales 183,241 (l.183) = 52.05%, operating margin from operating income 51,313 (l.190) = 13.43%, cash capex 98,411 − 2,101 (l.145–146) = 96,310, capex/net sales 25.20%, depreciation 26,703. All six-month. True as claimed. |
| opt. | business.md §7 OpenAI row date | **Resolved.** "Q1 2026 to after 6/30/2026" (l.160), matching "Subsequent to June 30, 2026" at `10-Q-2026-Q2.txt` l.484. |

5 of 5 resolved (four required, one optional).

### 2. Regression scan

- Headings: business.md §1–§8, Glossary, Sources present and in order (l.4, 12, 44, 83, 115, 125, 143, 166, 179, 188); header line l.2 and `_Proposed — owner to review and lock._` at l.168 unchanged. outlook.md §1–§5 and Sources present and in order (l.4, 21, 29, 41, 57, 70); tier header l.2 unchanged; no §6.
- Sources lists: business.md 11 entries, outlook.md 6 entries, unchanged. Script check: business.md 164 tags in 14 families, outlook.md 60 tags in 6 families, every family mapped (the counts rose from cycle 1's 155 and 59 by exactly the nine tags the reviewer added and the one Note 5 tag the writer added).
- Cycle-1 direct edits: all 24 intact in place (21 in business.md, 3 in outlook.md).
- Claims 1–8 unchanged from cycle 1; ten claims in total, two headline, eight fundamentals; all single-direction and gradeable.
- No other line of either file changed in a way that touches a number, quote, tag or heading (line counts unchanged apart from the edited cells).

### 3. Word counts (canonical script)

| File | Cycle 1 end | Cycle 2 | Target |
|---|---|---|---|
| business.md | 2,888 | 2,893 | 2,000–3,000 |
| outlook.md | 1,097 | 1,136 | 800–1,200 |

Both inside their ceilings.

### 4. Rubric, cycle 2

1. What they do and who pays: **Yes.**
2. What would kill it and the early warning: **Yes.**
3. Why the margins are what they are and whether cost scales with usage: **Yes.**
4. Predict the scorecard from §5 alone: **Yes.** All ten claims name the document and the number or sentence to look for, and claims 9 and 10 now say how silence is graded.
5. Nothing required knowledge I don't have: **Yes.** The two rewritten claims introduce no new terms ("statement check", "Dropped", "Met" are the scorecard's own words).

### Fixed directly, cycle 2

Nothing. No jargon, tag, typo or wording problem was found in the changed passages, and the rest of both files is as left at the end of cycle 1.

### Withdrawals, cycle 2

None.

### Final verdict: **PASS**

All four REVISE items and the optional wording are resolved and verified against the cached sources; the 24 cycle-1 edits are intact; every tag maps to a cached file; both files are within length; all ten claims are single-direction and mechanically gradeable; nothing substantive fails. One note for the owner at indicator lock: indicator 8 now reports the face value of long-term debt in both quarters ($122.6B at 3/31/2026, $133.0B at 6/30/2026); the balance-sheet carrying amounts ($119.1B, $128.9B) are lower because of unamortised discount and the current portion, and the refresh agent should keep using Note 5's face value.
