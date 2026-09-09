# Tesla, Inc. (TSLA) — Reviewer report, 2026-Q2

_Reviewed 2026-09-09 against `companies/TSLA/sources/2026-Q2/` only (cached primary texts; the gatherer notes were not used as evidence). As-of cutoff 2026-07-23 (call 2026-07-22; 10-Q filed 2026-07-23). Line numbers below (`l.N`) refer to the cached `.txt` files. Deck pages: `p.N` is the printed deck page, which equals the slide number; in the cached text page N begins at line 3N+1 (marker `=== p.N ===` at line 3N), so Q2 2026 Update p.4 is `slides.txt` l.13, p.5 l.16, p.10 l.31, p.27 l.82, p.30 l.91; Q4 2025 Update p.5 is `slides-2025-Q4.txt` l.16, p.7 l.22, p.32 l.97; Q1 2026 Update p.4 is `slides-2026-Q1.txt` l.13, p.5 l.16, p.9 l.28, p.10 l.31, p.23 l.70, p.28 l.85. The transcript has no pages; `l.N` is the line in `transcript.txt` (Musk prepared remarks l.19–51, Taneja l.55–73, Elluswamy l.77–97, analyst Q&A l.99–231). Filings use curly apostrophes; every search was run with quotes and dashes normalised on both sides, and every NOT FOUND was re-searched on a shorter token and the full line printed before a ruling._

**Final verdict (after cycle 2, 2026-09-09): PASS.** All 7 must-fix and 10 nice-to-have items were resolved in the writer's second pass and re-verified against the cached sources (see "Cycle 2" at the end of this file); both files are inside their length targets (business.md 2,737, outlook.md 1,119). The cycle-1 verdict paragraph is kept below for the record.

**Cycle-1 verdict: REVISE** (light second pass, one cycle expected). Every number in every table reconciles to the filings and decks (199 cells, 0 failures), every management quotation in the outlook is verbatim, no post-cutoff information was found, and the company-specific content the owner asked for is present. What needs the writer: one dollar figure that exists in no cached source (the "$65 million" fee award), one quotation spliced from two sentences of the FY2023 10-K, one unsupported count ("six factories"), one unlabelled inference (which award milestone is "probable"), one mischaracterisation of the debt, a transcript-only number presented without the machine-transcript caveat, and both files over the length target (business.md 3,260 against 2,000–3,000; outlook.md 1,447 against 800–1,200).

---

## 1. Rubric (§14)

Read as the owner would: a smart 16-year-old with no finance background.

1. **Can I explain what this company does, and who pays it, in two sentences?** **Yes.** §1 does it in two paragraphs: cars sold direct to drivers, batteries sold to utilities and homes, software subscriptions, and credits sold to other carmakers; the 2025 split ($69.5B / $12.5B / $12.8B) is stated.
2. **Do I know exactly what would kill it, and what the early warning sign is?** **Yes.** §6 ranks seven scenarios, each with a concrete early warning (automotive margin ex-credits below 15%; the quarterly credit line and the $287M contracted; FCF negative two quarters and cash below $40B; a court order on FSD naming or the metro count stalling; new outside roles or share sales by the CEO; tariffs reappearing in the bridge; production trailing deliveries) and a stated exposure.
3. **Do I know why the margins are what they are, and whether cost scales with usage?** **Yes.** §3 explains fixed-cost absorption, price, mix and ramp costs in plain words with the company's own phrases, then shows the 16.8% to 1.4% operating-margin slide as price, credits and AI spending. The energy table makes the second business's size visible.
4. **Could I predict what the scorecard will check next quarter, from §5 of the outlook alone?** **Yes.** All ten claims are single-direction and mechanical; claim 7 should define "live" (see §5 below).
5. **Did nothing in the report require knowledge I don't have?** **Now yes.** Before review about twenty terms were unexplained (attach rate, ASP, tranche, market cap, adjusted EBITDA, net-settle, grant-date fair value, derivative proceeding, supermajority, beneficially owned, restricted shares, Series E preferred, working-capital facility, compensatory/punitive, securities suit, dilution, days of inventory, valuation allowance, cathode, 4680, EMEA, fab, S-curve, warranty true-up). All are now glossed in place (see "Fixed directly").

---

## 2. Skeleton and format compliance

**business.md**

| Requirement (§6) | Status |
|---|---|
| `# <Company> — The Business` | OK (`# Tesla, Inc. — The Business`) |
| `_As of <QLABEL>. Written <date>._` | OK (`_As of Q2 2026. Written 2026-09-09._`) |
| §1 What they do (incl. short history) | OK; history paragraph at l.12 |
| §2 How the money comes in (5-year segment table) | OK; five revenue lines FY2021–FY2025 + Q2 2026, plus a regulatory-credit table |
| §3 The economics (revenue, GM, OM, capex, capex/revenue, 5 years) | OK; plus automotive margin ex-credits, energy margin, R&D/revenue; second table for energy storage |
| §4 How profitable, really (5-year table) | OK; OCF, capex, FCF, net income, SBC, cash, debt |
| §5 Why customers don't leave (source + weakening sign) | OK; five moats, each with a source and a weakening sign |
| §6 What could break it (ranked; early warning; exposure; concentration) | OK; seven ranked scenarios and a customer-concentration paragraph |
| §7 Who runs it and what they do with the cash | OK; people, board, ownership, pay table, related-party table, capital allocation |
| §8 Indicators (5–8; name / why / where) | OK; 8 indicators, each with why and where |
| `_Proposed — owner to review and lock._` | OK (l.162) |
| Glossary (only unavoidable terms, one sentence each) | OK; 8 entries |
| Sources (every tag mapped; page basis stated) | OK; 17 tag families used, all mapped (checked by script); page basis and 10-K Item 8 / 10-Q Item 1 convention stated; note numbering per filing stated |
| Heading order | OK (l.4, 14, 43, 75, 93, 105, 125, 160, 173, 184) |
| Length 2,000–3,000 prose words, aim lower half | **OVER**: 3,179 at launch, 3,260 after my glosses (`/tmp/tsla-orch/wc_prose.py`). REVISE item 7 |

**outlook.md**

| Requirement (§7) | Status |
|---|---|
| `# <Company> — Outlook as of <QLABEL>` | OK |
| `_Transcript source tier: ... Written <date>._` | OK (`third-party (The Motley Fool)`); MANIFEST.md l.3 records tier 3, call 2026-07-22, posted 2026-08-05; the outlook's l.4 repeats both dates and the numbers-from-deck rule |
| §1 one row per indicator; this q / last q / expected | OK; 8 rows in the same order as business.md §8 |
| §2 What management says | OK |
| §3 Growth engines (what / how big / claim / working-or-not) | OK; six engines, each with "Working if"; opens with "Everything here is management's claim, not fact" |
| §4 Guidance verbatim | OK; the Outlook page is quoted in full (see §4 below for the two extraction artefacts) |
| §5 Claims (6–12) | OK; 10 claims |
| §6 Tone shift | Correctly absent (first run) |
| Sources | OK; 8 tag families used, all mapped; page basis and note numbering stated |
| Length 800–1,200 prose words | **OVER**: 1,417 at launch, 1,447 after glosses. REVISE item 7 |

**Indicator anchoring (AGENTS.md §8)** — each proposed indicator and the recurring disclosure it rests on:

| # | Indicator | Recurring disclosure | Anchored? |
|---|---|---|---|
| 1 | Vehicle deliveries; production (quarter) | Production, Deliveries & Deployments 8-K every quarter (`press-release-deliveries.txt`); deck Operational Summary p.5 every quarter | Yes |
| 2 | Automotive gross margin excl. regulatory credits (non-GAAP) | Deck reconciliation page every quarter (Q2 2026 p.30 l.91; Q1 2026 p.28 l.85; annual Q4 2025 p.32 l.97) | Yes |
| 3 | Regulatory credit revenue (quarter) | 10-Q income statement line (`10-Q-2026-Q2.txt` l.170); deck Statement of Operations p.27 l.82 | Yes |
| 4 | Storage deployed (GWh); energy segment gross profit (margin) | Deck p.5 and the P&D release; 10-Q segment note (Q2: Note 14 l.959; Q1: Note 13 l.922) | Yes (two figures, natural pair) |
| 5 | Active FSD subscriptions | Deck Operational Summary p.5, footnoted "In accordance with our 2025 CEO Performance Award"; present in the Q4 2025, Q1 2026 and Q2 2026 decks, with the Q2 deck back-filling Q2-2025 to Q1-2026 | Yes, but new: three decks so far. The indicator text already says so; the owner should know it could be redefined |
| 6 | Operating margin | Deck Financial Summary p.4 every quarter; 10-Q | Yes |
| 7 | Capex; free cash flow (quarter) | Deck p.4 and p.29/p.31 every quarter; 10-Q cash-flow statement | Yes |
| 8 | Cash and short-term investments; total debt (principal) | Deck p.4 and p.28 footnote; 10-Q debt note | Yes |

None depends on a dollar target or growth percentage given once on a call; the one-off figures ($25B capex, "up to $30B" facilities, "10% a week") are correctly handled as claims or excluded.

---

## 3. Citation spot-check

Legend: PASS = number or wording found in the tagged source; FAIL = not in the tagged source, wrongly characterised, or tagged to the wrong place. Computed cells were re-derived from the sourced inputs.

### 3(a) business.md §2 revenue table (l.16–23) — every cell

Inputs: `10-K-FY2023.txt` l.1353–1359 (FY2021–FY2023); `10-K-FY2025.txt` l.1335–1341 (FY2024–FY2025); `10-Q-2026-Q2.txt` l.169–175 (Q2 2026).

| Row | Source values (USD m) | Result |
|---|---|---|
| Automotive sales 44,125 / 67,210 / 78,509 / 72,480 / 65,821 / 20,006 | as stated | PASS ×6 |
| Regulatory credits 1,465 / 1,776 / 1,790 / 2,763 / 1,993 / 146 | as stated | PASS ×6 |
| Leasing 1,642 / 2,476 / 2,120 / 1,827 / 1,712 / 364 | as stated | PASS ×6 |
| Services and other 3,802 / 6,091 / 8,319 / 10,534 / 12,530 / 4,581 | as stated | PASS ×6 |
| Energy 2,789 / 3,909 / 6,035 / 10,086 / 12,771 / 3,139 | as stated | PASS ×6 |
| Total 53,823 / 81,462 / 96,773 / 97,690 / 94,827 / 28,236 | as stated | PASS ×6 |

36/36 PASS.

### 3(b) business.md §2 regulatory-credit table (l.31–35) — every cell

Inputs: credits as above plus `10-Q-2026-Q2.txt` l.170 (Q2 2025: 439); income from operations `10-K-FY2023.txt` l.1373 (6,523 / 13,656 / 8,891), `10-K-FY2025.txt` l.1355 (7,076 / 4,355), `10-Q-2026-Q2.txt` l.189 (398; Q2 2025: 923).

| Row | Check | Result |
|---|---|---|
| Credits 1,465 / 1,776 / 1,790 / 2,763 / 1,993 / 439 / 146 | as stated | PASS ×7 |
| Income from operations 6,523 / 13,656 / 8,891 / 7,076 / 4,355 / 923 / 398 | as stated | PASS ×7 |
| Credits % of operating income (computed) 22 / 13 / 20 / 39 / 46 / 48 / 37% | 22.5 / 13.0 / 20.1 / 39.0 / 45.8 / 47.6 / 36.7% | PASS ×7 |

21/21 PASS.

### 3(c) business.md §3 economics table (l.47–56) — every cell

Inputs: `slides-2025-Q4.txt` p.5 l.16 (revenue, gross margin, operating margin, capex FY2021–FY2025); `slides.txt` p.4 l.13 (Q2 2026); automotive margin ex-credits `slides-2025-Q4.txt` p.32 l.97 and `slides.txt` p.30 l.91; energy margin `10-K-FY2023.txt` l.1049 "(4.6) | % ... 7.4 | % ... 18.9 | %", `10-K-FY2025.txt` l.1027 "29.8 | % | 26.2 | %", `10-Q-2026-Q2.txt` l.1112 "20.4 | %"; R&D `10-K-FY2023.txt` l.1369 (2,593 / 3,075 / 3,969), `10-K-FY2025.txt` l.1351 (4,540 / 6,411), `10-Q-2026-Q2.txt` l.185 (2,371).

| Row | Check | Result |
|---|---|---|
| Revenue | as §2 | PASS ×6 |
| Gross margin 25.3 / 25.6 / 18.2 / 17.9 / 18.0 / 16.8% | deck rows "Total GAAP gross margin" | PASS ×6 |
| Auto GM ex credits 27.0 / 26.7 / 17.7 / 15.4 / 15.4 / 16.3% | deck reconciliation rows | PASS ×6 |
| Energy GM (4.6) / 7.4 / 18.9 / 26.2 / 29.8 / 20.4% | 10-K/10-Q Item 7 / Item 2 tables | PASS ×6 |
| R&D / revenue (computed) 4.8 / 3.8 / 4.1 / 4.6 / 6.8 / 8.4% | 2,593/53,823 = 4.82; 3,075/81,462 = 3.77; 3,969/96,773 = 4.10; 4,540/97,690 = 4.65; 6,411/94,827 = 6.76; 2,371/28,236 = 8.40 | PASS ×6 |
| Operating margin 12.1 / 16.8 / 9.2 / 7.2 / 4.6 / 1.4% | deck rows | PASS ×6 |
| Capex 6,514 / 7,163 / 8,899 / 11,342 / 8,527 / 5,789 | deck rows (Tesla definition incl. energy systems, footnote (3) on Q4 p.5 and (1) on Q2 p.31) | PASS ×6 |
| Capex / revenue (computed) 12.1 / 8.8 / 9.2 / 11.6 / 9.0 / 20.5% | 12.10 / 8.79 / 9.20 / 11.61 / 8.99 / 20.50 | PASS ×6 |

48/48 PASS.

### 3(d) business.md §3 energy storage table (l.64–69) — every cell

Inputs: energy revenue as §2; GWh `slides-2025-Q4.txt` p.7 l.22 (4.0 / 6.5 / 14.7 / 31.4 / 46.7) and `slides.txt` p.5 l.16 (13.5); gross profit `10-K-FY2023.txt` Note 18 l.2649 "1,141 | $ | 288 | $ | ( 129 )", `10-K-FY2025.txt` Note 16 l.2694 "3,802 | $ | 2,640 | $ | 1,141", `10-Q-2026-Q2.txt` Note 14 l.959 "640".

| Row | Check | Result |
|---|---|---|
| Energy revenue | as §2 | PASS ×6 |
| Storage deployed 4.0 / 6.5 / 14.7 / 31.4 / 46.7 / 13.5 | deck rows | PASS ×6 |
| Energy gross profit (129) / 288 / 1,141 / 2,640 / 3,802 / 640 | segment notes; Q2 also = 3,139 − 2,499 (deck p.27) | PASS ×6 |
| Energy gross margin | re-derived: −4.63 / 7.37 / 18.91 / 26.17 / 29.77 / 20.39% | PASS ×6 |

24/24 PASS. Prose l.73 "more than a fifth of the company's total (computed)": 3,802 / 17,094 = 22.2% (`10-K-FY2025.txt` l.1349) PASS.

### 3(e) business.md §4 cash table (l.79–87) — every cell

Inputs: OCF, capex, FCF, cash `slides-2025-Q4.txt` p.5 l.16 and `slides.txt` p.4 l.13 (Q1: 3,937 / 2,493 / 1,444 / 44,743; Q2: 4,697 / 5,789 / (1,092) / 43,524); net income `10-K-FY2023.txt` l.1381, `10-K-FY2025.txt` l.1363, `10-Q-2026-Q2.txt` l.197 (six months 1,591); SBC cash-flow lines `10-K-FY2023.txt` l.1466 (1,812 / 1,560 / 2,121), `10-K-FY2025.txt` l.1446 (2,825 / 1,999 / 1,812), `10-Q-2026-Q2.txt` l.321 (2,181); debt principal `10-K-FY2023.txt` Note 11 l.2134 (2,061) and l.2113 (4,683), `10-K-FY2025.txt` Note 9 l.2086 (7,907) and l.2068 (8,177), `10-Q-2026-Q2.txt` Note 8 l.707 (9,080).

| Row | Check | Result |
|---|---|---|
| Operating cash flow 11,497 / 14,724 / 13,256 / 14,923 / 14,747 / 8,634 | H1 = 3,937 + 4,697 = 8,634 | PASS ×6 |
| Capex 6,514 / 7,163 / 8,899 / 11,342 / 8,527 / 8,282 | H1 = 2,493 + 5,789 = 8,282 | PASS ×6 |
| Free cash flow 4,983 / 7,561 / 4,357 / 3,581 / 6,220 / 352 | H1 = 1,444 − 1,092 = 352 | PASS ×6 |
| Net income 5,519 / 12,556 / 14,997 / 7,091 / 3,794 / 1,591 | 10-Q six-month column 1,591 (= 477 + 1,114) | PASS ×6 |
| SBC 2,121 / 1,560 / 1,812 / 1,999 / 2,825 / 2,181 | cash-flow statements; H1 2026 = 1,030 + 1,151 (deck p.29) | PASS ×6 on the numbers. **Tag nit** (nice-to-have 14): the totals sit on the cash-flow statement (Item 8 / Item 1), not in the equity-plan notes the row is tagged to |
| Cash and ST investments 17,707 / 22,185 / 29,094 / 36,563 / 44,059 / 43,524 | deck rows | PASS ×6 |
| Total debt, principal n/d / 2,061 / 4,683 / 7,907 / 8,177 / 9,080 | "Total debt ... Unpaid Principal Balance" columns; FY2023 10-K shows only 2023 and 2022, so 2021 is genuinely not in the fetched filings | PASS ×6 (n/d confirmed) |

42/42 PASS. Footnote l.89 ("releasing $6.54 billion of our valuation allowance"): `10-K-FY2024.txt` l.919 PASS.

### 3(f) business.md §4 return-on-capital sentence (l.91) — computed cells

Income from operations over year-end net PP&E: 13,656 / 23,548 = 58.0% (`10-K-FY2023.txt` l.1308); 8,891 / 29,725 = 29.9%; 7,076 / 35,836 = 19.7% (`10-K-FY2025.txt` l.1292); 4,355 / 40,643 = 10.7%. Stated 58 / 30 / 20 / 11 cents: PASS ×4. "$47.3 billion at June 30, 2026" = 47,255 (`10-Q-2026-Q2.txt` l.122) PASS; "$10.8 billion (gross) of 'AI infrastructure'" = 10,823 (Note 5 l.645) PASS.

### 3(g) outlook.md §1 indicator table (l.10–19) — every number

| Row | This quarter | Last quarter | Result |
|---|---|---|---|
| 1 Deliveries; production | 480,126; 451,758 (`press-release-deliveries.txt` table) | 358,023; 408,386 (`press-release-deliveries-2026-Q1.txt`) | PASS ×4 |
| 2 Auto GM ex credits | 16.3% (`slides.txt` p.30 l.91) | 19.2% (`slides-2026-Q1.txt` p.28 l.85) | PASS ×2 |
| 3 Regulatory credits | $146M (`10-Q-2026-Q2.txt` l.170) | $380M (`10-Q-2026-Q1.txt` l.170) | PASS ×2 |
| 4 GWh; energy GP (margin) | 13.5; $640M (20.4%) (`slides.txt` l.16; `10-Q-2026-Q2.txt` l.959; 640/3,139 = 20.39%) | 8.8; $952M (39.5%) (`slides-2026-Q1.txt` l.16; `10-Q-2026-Q1.txt` l.922; 952/2,408 = 39.53%) | PASS ×6 |
| 5 Active FSD subscriptions | 1.48M (`slides.txt` l.16) | 1.28M (`slides-2026-Q1.txt` l.16) | PASS ×2 |
| 6 Operating margin | 1.4% (`slides.txt` l.13) | 4.2% (`slides-2026-Q1.txt` l.13) | PASS ×2 |
| 7 Capex; FCF | $5,789M; $(1,092)M | $2,493M; $1,444M | PASS ×4 |
| 8 Cash; debt principal | $43,524M; $9,080M (`slides.txt` l.13; `10-Q-2026-Q2.txt` l.707) | $44,743M; $9,039M (`slides-2026-Q1.txt` l.13; `10-Q-2026-Q1.txt` l.654) | PASS ×4 |

26/26 PASS. The "expected" column's seven quotations are all verbatim (Q1 deck p.10, p.3, p.23, p.6, p.9; 10-K FY2025 Note 2 l.1912; transcript l.69, l.71; 10-Q Q1 Item 2 l.1018).

### 3(h) Prose sentences — 62 checks across both files

business.md

1. l.6 "sells them straight to drivers ... with no dealers" — `10-K-FY2025.txt` l.131 "We generally sell our products directly to customers". PASS.
2. l.6 "delivered about 1.64 million vehicles in 2025" — l.867 "delivered approximately 1.64 million consumer vehicles". PASS.
3. l.6 "46.7 GWh were deployed in 2025" — l.869. PASS.
4. l.6 "six factories in the United States, China and Germany" — **FAIL.** Item 2 (l.799–807) lists eight primary manufacturing facilities (Texas, Fremont, Nevada, Berlin, Shanghai, Megafactory Shanghai, Gigafactory New York, Megafactory Lathrop); the deck's automotive capacity table (`slides.txt` p.6 l.19) shows cars built in four (California, Shanghai, Berlin, Texas) with Nevada "Commissioning" for Semi. No source gives "six". REVISE item 3.
5. l.8 "1.48 million active subscriptions" — `slides.txt` l.16. PASS.
6. l.8 "$94.8 billion: $69.5 billion ... $12.5 billion ... $12.8 billion" — `10-K-FY2025.txt` l.1338–1341. PASS.
7. l.10 mission quotes — `10-K-FY2025.txt` l.131, l.133; `10-K-FY2024.txt` l.133. PASS ×3.
8. l.10 "launched in Austin in June 2025" — `10-K-FY2025.txt` l.147 gives June 2025 but not Austin; `transcript.txt` l.79 "We started the robotaxi program roughly a year ago in Austin". PASS after adding the call tag (fixed directly).
9. l.12 history: Delaware July 1, 2003 and Texas June 13, 2024 (`10-K-FY2025.txt` l.1497); listed June 29, 2010 (l.827); CEO since October 2008 (`10-KA-FY2025.txt` l.189); SolarCity acquired November 2016 (l.192); Austin HQ (l.797); 134,785 employees (l.421). PASS ×6.
10. l.12 deliveries 936,222 → 1,808,581 then two falls — `slides-2025-Q4.txt` l.22 (1,789,226; 1,636,129). PASS.
11. l.27 "deliveries down 1% then 9%" — 1,789,226/1,808,581 = −1.1%; deck YoY −9%. PASS. Quotes "overall price reductions and attractive financing options" (`10-K-FY2024.txt` l.1037) and "higher customer incentives" (`10-K-FY2025.txt` l.994). PASS ×2.
12. l.27 "deliveries up 25% to 480,126, automotive sales revenue up 27%" — `slides.txt` l.16; `10-Q-2026-Q2.txt` l.1079. PASS ×2.
13. l.27 "over 55% of new deliveries" and "$4.05 billion" deferred revenue — `slides.txt` p.9 l.28; `10-Q-2026-Q2.txt` l.403. PASS ×2. "subscription-only" — `slides-2026-Q1.txt` l.28. PASS.
14. l.29 tradable-credits quote and "negligible incremental costs" — `10-K-FY2025.txt` l.323, l.1564. PASS ×2.
15. l.39 OBBBA quotes — l.1912; "July 2025" enacted July 4, 2025 (l.319). PASS ×3. "fell 67%, from $439 million ... to $146 million" — 146/439 = −66.7%; l.1083. PASS. "$841 million to $287 million" — `10-K-FY2025.txt` l.1564 and `10-Q-2026-Q2.txt` l.419 (both tagged). PASS.
16. l.41 "growing about 20% a year" — 2025 growth 19% (l.1000), but 2024 was 27% and 2023 37% (computed from §2). Loose; nice-to-have 10. "record 14% gross margin" — `slides.txt` p.9 l.28. PASS.
17. l.41 geography $47.6B / $21.0B / $26.2B — `10-K-FY2025.txt` l.2704–2706 (47,627 / 20,962 / 26,238). PASS ×3.
18. l.45 "depreciation costs of tooling and machinery" (l.1033), "lower manufacturing costs from better fixed cost absorption" (`10-K-FY2023.txt` l.1065), "lower fixed cost absorption" (`10-K-FY2025.txt` l.1043), "Cybertruck ramp" (`10-K-FY2024.txt` l.1094), "preproduction ramp costs ..." (`transcript.txt` l.69), "relatively larger" (l.865), $565 million and $1.12 billion (l.1624, l.1638). PASS ×7.
19. l.45 quotation "primarily due to a lower average selling price on our vehicles driven by overall price reductions year over year" — **FAIL (spliced).** `10-K-FY2023.txt` l.1071 reads "The decrease was primarily due to a lower average selling price on our vehicles partially offset by the favorable change in our average combined cost per unit"; the words "driven by overall price reductions year over year" come from the revenue paragraph at l.1014. Two sentences joined as one quotation. REVISE item 2.
20. l.57 "$3.1 billion in 2022 to $6.4 billion in 2025" (3,075 → 6,411), "primarily due to increases in costs related to AI and other programs" (l.1072), "R&D rose another 49% and administrative costs 45%" (`10-Q-2026-Q2.txt` l.1145, l.1156), "$283 million increase in stock-based compensation" (l.1156), "energy warranty-related charges due to vendor cell issue" (`slides.txt` p.25 l.76), "investing heavily in research and development ..." (l.1006). PASS ×6.
21. l.73 Lathrop 40 GWh, Shanghai 20 GWh, Texas "Commissioning" — `slides.txt` p.6 l.19 (the deck says "California" and "Texas"; Lathrop and "near Houston" are in `10-K-FY2025.txt` l.807 and l.899). PASS (add the Item 2 / Item 7 tag when trimming). Q1 39.5% and "one-time benefits related to tariffs" — `10-Q-2026-Q1.txt` l.1082, l.1098. PASS ×2. "can vary meaningfully quarter to quarter" — l.899. PASS. CFO quote — `transcript.txt` l.65. PASS. "$10.05 billion" — `10-Q-2026-Q2.txt` l.445. PASS.
22. l.77 FCF definition — `slides.txt` p.32 l.97. PASS.
23. l.91 "capex of $5.8 billion, more than double Q1, made free cash flow negative $1.1 billion" — `slides.txt` p.25 l.76; 5,789 vs 2,493. PASS. "in excess of $25 billion" (`10-Q-2026-Q2.txt` l.1046), "will grow for the next two to three years" (`transcript.txt` l.71). PASS ×2.
24. l.91 "Debt of $9.1 billion is almost all owed by subsidiaries against specific assets" — **FAIL (mischaracterised).** `10-Q-2026-Q2.txt` l.733 (corrected in cycle 2 from l.729, which is the table's footnote (1)): "Non-recourse debt refers to debt that is recourse to only assets of our subsidiaries"; the largest piece, the China Working Capital Facility (5,888, l.703), is "an unsecured revolving facility" (`10-K-FY2025.txt` l.2118). Non-recourse is right; "against specific assets" is wrong for the unsecured $5.9B. REVISE item 5.
25. l.91 "securing certain debt facilities that will give us the capacity to borrow up to $30 billion" — `transcript.txt` l.71, verbatim. PASS as wording; the amount has no deck or 10-Q counterpart (`10-Q-2026-Q2.txt` l.1008 says only "may include additional funding"). REVISE item 6.
26. l.95 Superchargers 8,704 / 82,357 and 3,476 / 31,498 — `slides.txt` l.16; `slides-2025-Q4.txt` l.22. PASS ×4. "all major automakers" — `10-K-FY2025.txt` l.239. PASS. "17% in Q2 2026" — `slides.txt` p.7 l.22. PASS.
27. l.97 "up 56% in a year" — deck YoY column. PASS.
28. l.99 "over 2.3 million cars a year (computed)" — 550 + 950 + 375 + 250 + 125 + 125 = 2,375k (`slides.txt` l.19). PASS. "best-selling vehicle, of any kind, globally" (`10-KA-FY2025.txt` l.484); "less than $35,000" (`DEF14A-2025.txt` l.4179). PASS ×2.
29. l.101 "relatively low marketing costs" (l.223); protest quotes (l.559 ×3); "days of vehicle inventory ... 27" (`slides.txt` l.16). PASS ×5.
30. l.103 4680 ">40 GWh" and "limiting factor" — `slides.txt` p.7 l.22. PASS ×2.
31. l.109 competition quote (l.519); 26.7% → 15.4%; "China supplied 22% (computed)" = 20,962/94,827 = 22.1%; Shanghai >950,000 the largest (`slides.txt` l.19); "about three quarters" = 69,526/94,827 = 73.3%. PASS ×5.
32. l.111 "46% of 2025 operating income"; tax-credit quote (l.685); $287 million. PASS ×3.
33. l.113 "increase further in the second half of 2026" (`transcript.txt` l.71); "slow the pace ..." and "raise additional capital ..." (`10-Q-2026-Q2.txt` l.1201); $43.5 billion. PASS ×4.
34. l.115 FSD risk quotes (l.449, l.699); Florida jury August 1, 2025, $129 million, 33%, $200 million, on appeal (`10-Q-2026-Q2.txt` l.897: Eleventh Circuit brief filed July 2, 2026); "cease using the term" (`10-K-FY2025.txt` l.2608); securities suit (`10-Q-2026-Q2.txt` l.889); NHTSA/SEC/DOJ (l.903, NHTSA spelled out); "if we injure even one person" (`transcript.txt` l.25). PASS ×10.
35. l.117 Musk dependency quote (l.591); "About 207 million" = 207,498,721 (`10-KA-FY2025.txt` l.1526). PASS ×2.
36. l.119 tariff quotes (l.461, l.541 ×2); energy "relatively larger" (l.865). PASS ×4.
37. l.121 battery quotes (`slides.txt` l.22; `10-K-FY2025.txt` l.487 Panasonic, CATL, "a very limited number"); 451,758 / 480,126. PASS ×5.
38. l.123 concentration quote (`10-Q-2026-Q2.txt` l.515); xAI $430 million (`10-K-FY2025.txt` l.2673); SpaceX $318 million (`10-Q-2026-Q2.txt` l.938); "about 10%" = 318/3,139 = 10.1%. PASS ×4.
39. l.127 ages 54 / 48 / 46 (`10-KA-FY2025.txt` l.398–400); CFO since August 2023 (l.407); Zhu quote and role (l.412–414); "had no other executive officers" (l.467); SpaceX CEO, CTO, Chairman (l.190–191); xAI to SpaceX February 2, 2026 (l.1580). PASS ×7. "CEO of Neuralink and The Boring Company" — l.198–199 says founder of TBC and Neuralink "where he serves as the Chief Executive Officer" (Neuralink); nice-to-have 8.
40. l.129 nine directors and expiry classes (l.178–186); Denholm chair since November 2018 (l.211); Hartung effective June 1, 2025 (`8-K-2025-05-16-hartung...` l.60); Straubel CEO of Redwood (l.1617); independence of all but the two Musks (l.1648); no cash or equity pay for the eight outside directors in 2025 (director compensation table l.1302–1309, all dashes); Special Committee of Denholm and Wilson-Thompson (l.545–547); 63% Texas vote (`8-K-2024-06-14...` l.111); bylaw quotes (`8-K-2025-05-16-bylaws-amendment.txt` l.72, l.74); November 2025 votes: Proposal 10 not approved (l.190), Proposal 12 approved 1,328,135,664 to 1,118,920,427 (l.205–209), Proposal 6 "not approved" (l.154–155). PASS ×12.
41. l.131 ownership 717,112,739 / 20.3% / 303,960,630 options counted / 423,743,904 excluded and voted proportionately / 207,498,721 pledgeable (l.1505, l.1526); Vanguard 6.1%, BlackRock 5.0% (l.1506–1507). PASS ×7.
42. l.133 "Musk takes no salary" — l.639 "he has never accepted his salary". PASS.
43. Pay table l.137–142: 2018 grant January 2018, 303,960,630 options, 12 tranches of 1%, $100B rising $50B, "specified operational milestones relating to profitability" (`10-KA-FY2025.txt` l.918–922, line-wrapped); $23.34 (`8-K-2025-08-04...` l.94 "equal to the exercise price per share of the 2018 CEO Award"); rescission January 30, 2024, 72% ratification, reversal December 19, 2025 (`10-K-FY2025.txt` l.2572); 304.0 million exercised, 17.5 million net-settled, January 19, 2028, five-year holding (`10-Q-2026-Q2.txt` l.757, l.759); ratification votes (`8-K-2024-06-14...` l.162); interim award 96,000,000 at $23.34, second-anniversary vesting, "No Double Dip", August 3, 2025 (`8-K-2025-08-04...` l.90–98, l.261); forfeited April 21, 2026 as a "Tornetta Decision Event", no expense (`10-Q-2026-Q2.txt` l.753); $26.06 billion (`10-K-FY2025.txt` l.2299); 2025 award September 3 / November 6, 2025, 423,743,904, 12 × 35,311,992, $2.0T to $8.5T, milestone list incl. $400B three times (`10-K-FY2025.txt` l.2305–2325; `10-KA-FY2025.txt` l.849–861); $267 million, $9.82 billion, $105.82–120.37 billion, $334.09, 7.5 or 10 years, succession framework for tranches 11–12 (`10-Q-2026-Q2.txt` l.816, l.826; `10-K-FY2025.txt` l.2326); $87.75 billion (`DEF14A-2025.txt` l.2020); vote 1,892,235,822 / 564,940,908 / 12,227,846 (`8-K-2025-11-07...` l.140). PASS ×30.
44. l.140 "plaintiff's counsel awarded about $65 million" — **FAIL (no source).** `10-K-FY2025.txt` l.2572: Chancery "awarded Plaintiff's counsel fees in the amount of $345 million"; on December 19, 2025 the Supreme Court "significantly reduced the attorney fee award" with no figure. `10-Q-2026-Q2.txt` Note 9 (l.753–759) and Note 11 (l.863–911) give no fee figure. Not in any cached file. REVISE item 1.
45. l.140 "the 20-million-vehicle goal deemed probable" — **FAIL (unlabelled inference).** `10-Q-2026-Q2.txt` l.826 and `10-K-FY2025.txt` l.2362 say only "the operational milestone that was considered probable of achievement"; neither names it. REVISE item 4.
46. l.137 "(shares issued August 15)" — `10-K-FY2025.txt` l.2299 calls August 15, 2025 the accounting grant date, "the date the issuance of the shares of restricted stock was no longer subject to conditionality"; the 8-K (l.79) says shares are issued after the HSR waiting period. Near enough, but say "accounting grant date". Nice-to-have 9.
47. l.144 "$158.4 billion" = 158,359,009,867 (l.1085); "2,522,203 to 1" and "0.00:1" (l.1256); product-goals risk quotes (`10-K-FY2025.txt` l.747, l.749); "no bonus" (l.625 "we currently do not provide cash bonuses to our executive officers"). PASS ×5.
48. Related-party table l.148–156: xAI investment terms (`10-K-FY2025.txt` l.2774–2776; `10-Q-2026-Q2.txt` l.940 "less than 1%"; `10-KA-FY2025.txt` l.1588 March 12, 2026); $3,007 million and "$1.00 billion net gain" and December 2026 restriction (l.572, l.578); call quotes (`transcript.txt` l.139 Ehrhart, l.137 Musk); xAI proposal votes and "not approved under the bylaw standard" (`8-K-2025-11-07...` l.164–168) and "NONE" recommendation (`DEF14A-2025.txt` l.257); Megapack $430M / $318M / $405M; AI hardware acquisition quote (l.617); derivative suits dismissed April 13, 2026, appealed May 2026 (l.873); Redwood $3.3M and $12.9M scrap, X $3.3M, TBC $0.9M, security $4.8M (`10-KA-FY2025.txt` l.1600–1620). PASS ×16.
49. l.158 "None" buybacks and no dividends (`10-K-FY2025.txt` l.849, l.835); capex quote (l.1046); $5 billion revolver (Note 9 l.2100; unused 5,000 at `10-Q-2026-Q2.txt` l.707); 11,509 bitcoin (l.580) worth $674 million (balance sheet l.124 "Digital assets | 674"); diluted shares 3,386 → 3,540 (`10-K-FY2023.txt` l.1387; `10-Q-2026-Q2.txt` l.203); "until the shares have been deemed to be earned" (`10-K-FY2025.txt` l.1698). PASS ×8.

outlook.md

50. l.8 "Tesla gives no numeric guidance" — the Outlook page (`slides.txt` p.10 l.31) contains no number; the 10-Q's only figure is capex. PASS.
51. l.23–25 §2 quotes — `slides.txt` l.10 (p.3) ×2, l.31 (p.10); `transcript.txt` l.55, l.57, l.19, l.21. PASS ×7. "Nothing was said about the fall in regulatory credits, pricing plans or the CEO award" — checked the whole transcript: "regulatory credits" appears only in the automotive-margin definition (l.59); no pricing plan; the award is not mentioned. PASS.
52. l.31 "$3.1 billion revenue and 13.5 GWh" — `slides.txt` l.13, l.16. PASS ×2.
53. l.35 "live in seven US metros, six without a safety driver" — `slides.txt` p.9 l.28: SF Bay Area "Safety Driver"; Austin, Dallas, Houston, Miami, Orlando, Tampa "Ramping Unsupervised"; Phoenix and Las Vegas "Preparations Underway"; p.3 "live in seven major metros". PASS.
54. l.37 "lines being installed at Fremont" — `slides.txt` p.6 l.19. PASS. Optimus quotes — `transcript.txt` l.23, l.33, l.191. PASS ×3.
55. l.39 "construction and equipment procurement" (`slides.txt` p.8 l.25); Terafab and AI5 quotes (`transcript.txt` l.37, l.199). PASS ×3.
56. l.41 Semi and Megapack quotes — `slides.txt` l.31, l.10, l.19; `transcript.txt` l.23; Q1 wording `slides-2026-Q1.txt` l.31 ("volume production"; Optimus "in anticipation of volume production"). PASS ×5. The two source disagreements are real and correctly described.
57. l.54–59 guidance bullets — `10-Q-2026-Q2.txt` l.1046; `transcript.txt` l.71 ×3, l.69, l.65, l.57, l.69, l.199. PASS ×9.
58. l.71 claim 9 "$417 million" Q3 2025 — `slides.txt` p.27 l.82. PASS. Quote — `10-Q-2026-Q2.txt` l.419 and l.1083. PASS.
59. l.72 claim 10 "451,758" — deliveries release. PASS.
60. l.74 "more than 10% a week" (`transcript.txt` l.31), "up to $30 billion" (l.71), the Q1 benefits and Q2 warranty amounts spoken only (l.61, l.65). PASS; correctly excluded.
61. l.4 dates (call 2026-07-22; posted 2026-08-05) — `transcript.txt` l.2; MANIFEST.md l.3. PASS.
62. l.15 Q1 energy GP $952M (39.5%) — `10-Q-2026-Q1.txt` l.922, l.1082. PASS.

**Citation tally:** 36 + 21 + 48 + 24 + 42 + 4 + 26 = **201 table and computed cells, 201 PASS**; 62 prose groups covering about 230 individual facts, of which **5 FAIL** (items 4, 19, 24, 44, 45) and 4 are precision nits (16, 39, 46, and the SBC tag in 3(e)); 82 quoted strings (§4 below), all verbatim except two extraction artefacts. No tag points to a document that does not contain the fact except the "$65 million" figure, which is in no document.

---

## 4. Verbatim-quote check

Script (`/tmp/tsla-orch/reviewer/quotes.py`): every double-quoted string of 12+ characters in outlook.md, whitespace and quote characters normalised, tested as a substring of the cached decks, transcript, 10-Qs and 10-K; elided quotes ("...") tested fragment by fragment. 62 quoted strings, 62 found. Business.md's transcript quotations (eight tags) were checked by hand: `transcript.txt` l.69 (preproduction ramp costs), l.65 (ASPs / mid- to low 20%), l.71 (two to three years; up to $30 billion; second half), l.25 (injure one person), l.139 (Ehrhart), l.137 (Musk on combining companies). All verbatim. The twelve 10-K/10-Q/8-K quotations sampled in §3(h) are verbatim except the spliced one at business.md l.45.

**outlook.md §4, the Outlook page in full (l.47–50) against `slides.txt` p.10 (l.31):** Volume, Cash and Profit paragraphs match character for character (the draft keeps the deck's "hardware- related" with its stray space). The Product paragraph matches except that the cached deck text reads "via se rvices powered", a line-break artefact of the exhibit conversion (MANIFEST-ir notes "se rvices" on p.10), which the draft normalises to "services". Both are extraction artefacts, not misquotations. §2 (l.23) quotes the same Profit sentence as "hardware-related" while §4 keeps "hardware- related": pick one and say so in Sources (nice-to-have 12).

**outlook.md §5, the quotation under each claim:** 1 `transcript.txt` l.71; 2 l.71; 3 l.65 (two fragments, elided); 4 l.23; 5 `slides.txt` l.31; 6 l.31; 7 `transcript.txt` l.69; 8 l.59; 9 `10-Q-2026-Q2.txt` l.419 (also l.1083); 10 l.55. All verbatim.

---

## 5. Claims check (outlook.md §5, AGENTS.md §9)

| # | One sentence, one check | Single direction | Sharpening labelled | Verbatim quote + tag | Note |
|---|---|---|---|---|---|
| 1 | Q3 capex > $5,789M | Yes | Yes ("our sharpening ... not management's number") | Yes | Mechanical from deck p.4 |
| 2 | FY2026 capex > $25B | Yes | Management's number, so labelled | Yes | Carries forward to Q4; says so |
| 3 | Q3 energy GM > 20.4% | Yes | Yes | Yes | Source of the check named (10-Q segment note) |
| 4 | Megapack 3 production started by Q3 Update | Yes | Yes ("soon" to one quarter; management's date 2026) | Yes | Checkable on deck p.6 status |
| 5 | Semi production starts in 2026 | Yes | Management's date | Yes | Says how it can be checked early |
| 6 | Optimus production starts at Fremont in 2026 | Yes | Management's date | Yes | |
| 7 | Q3 coverage table shows > 7 live metros | Yes | Yes | Yes | "Live" is undefined; the deck has three statuses. Define it as "any status other than Preparations Underway" (nice-to-have 13) |
| 8 | Active FSD subscriptions > 1.48M | Yes | Yes | Yes | |
| 9 | Q3 credit revenue < Q3 2025's $417M | Yes | Labelled disclosure check; quarter column stated | Yes | |
| 10 | Q3 production > 451,758 | Yes | Yes | Yes | |

Ten claims, inside 6–12. No either/or constructions, no double-barrelled claims, fundamentals dominate (no revenue or EPS claim at all, which is right for a company that gives no numeric guidance). The closing paragraph correctly lists what could not be sharpened and why. Every robotaxi, Cybercab, Optimus and chip statement in §3 is framed as a claim with a "Working if" test, and claims 4–8 give the checkable milestones.

---

## 6. Jargon audit

### (a) Terms neither plain, name-inferable nor in the glossary — and what was done

All glossed in place by the reviewer (see "Fixed directly"): attach rate (business §5, outlook §3), ASPs (§3 CFO quote), capex (§3 table label), net income attributable to common stockholders and total debt principal (§4 table labels), valuation allowance (§4 footnote), working-capital facility (§4), 4680 line and cathode plant (§5), days of vehicle inventory (§5), dilution / equity raised (§6), compensatory and punitive damages, securities suit (§6), derivative proceeding and supermajority (§7), beneficially owned and restricted shares (§7), tranches, market cap, adjusted EBITDA, exercised options, net-settled, grant-date fair value (§7 pay table), Series E preferred stock (§7 related-party table); outlook: EMEA (§1), S-curve and fab (§3), warranty true-up (§5 claim 3).

Left as is (plain or inferable): Supercharger, Megapack, Megafactory, Gigafactory, over-the-air, subscription, backlog, revolving credit line, class action, advisory proposal, pay ratio, bitcoin, data centers, humanoid robot, chip, fab (after gloss), FSD (glossary), GWh (glossary), regulatory credits (glossary), gross/operating margin (glossary), free cash flow (glossary), non-GAAP (glossary), deferred revenue (glossed inline at §2), fixed-cost absorption (explained in §3), return on capital (explained in §4).

### (b) Glossary

Eight entries, one sentence each, all used in the text. "Gross margin", "Operating margin", "Free cash flow" and "Non-GAAP" are generic finance terms; for this reader they are unavoidable and the META report set the same precedent. OK.

### (c) Paragraphs that are mostly numbers

business.md l.57 ("Why operating margin fell") and l.131 ("Ownership") are dense with figures already in the neighbouring tables; see the length guidance in §8.

---

## 7. Invented-number check

| Where | Figure | Finding |
|---|---|---|
| business.md l.140 (pay table, 2018 award status) | "plaintiff's counsel awarded about $65 million" | **Not in any cached source.** The 10-K (l.2572) gives $345 million at Chancery and says the Supreme Court "significantly reduced" it, no figure; the 10-Q has none. Must fix |
| business.md l.140 (2025 award status) | "the 20-million-vehicle goal deemed probable" | The filings do not name the probable milestone (`10-Q-2026-Q2.txt` l.826; `10-K-FY2025.txt` l.2362). An inference presented as fact. Must fix |
| business.md l.6 | "six factories" | No source gives six (Item 2 lists eight facilities; four build cars today). Must fix |
| business.md l.91, l.158; outlook.md l.74 | "up to $30 billion" (debt facilities) | Transcript-only (`transcript.txt` l.71); the 10-Q (l.1008, l.1201) gives no amount. Quoted as the CFO's words, which §3 rule 2 allows, but as a machine-transcript number it needs the caveat the outlook already gives at l.74. Must fix in business.md (label) |
| business.md l.45 | spliced quotation | Two sentences from `10-K-FY2023.txt` l.1071 and l.1014 presented as one. Must fix |
| business.md l.41 | "about 20% a year" | Only 2025 (19%) fits; 2024 was 27%, 2023 37%. Nice-to-have |
| business.md l.91 | "'AI infrastructure', meaning data centers" | Gloss is the writer's; the 10-Q's own words are "compute infrastructure and data centers" (l.1046). Nice-to-have |

Every other figure in both files traces to a tagged source; every "computed" cell re-derives; every "n/d" (2021 debt) is genuinely absent from the fetched filings. No number tagged to the transcript is used as a fact except as noted; the deck-or-10-Q rule is otherwise respected (the writer's l.74 note lists the excluded spoken figures).

---

## 8. Length check (§3 rule 7, canonical counter)

`cd /home/ubuntu && python3 -P /tmp/tsla-orch/wc_prose.py business.md outlook.md`

| File | At launch | After reviewer glosses | Target | Status |
|---|---|---|---|---|
| business.md | 3,179 | **3,260** | 2,000–3,000 (aim lower half) | OVER by 260; cut at least 500, ideally 700 |
| outlook.md | 1,417 | **1,447** | 800–1,200 | OVER by 247; cut at least 300 |

Per-section prose words after glosses (`/tmp/tsla-orch/writer/wc_sections.py`, same method):

business.md: §1 321 · §2 329 · §3 522 · §4 257 · §5 293 · §6 755 · §7 599 · §8 178. outlook.md: header 34 · §1 28 · §2 161 · §3 391 · §4 353 · §5 480.

Where the words are and what looks cuttable (the writer decides; do not lose a commitment or a sourced fact that appears nowhere else):

- **business.md §6 (755).** Scenario 5's risk factor is quoted in full (about 70 words); the second sentence is the point. Scenario 4's litigation list duplicates the related-party table's derivative-suit row and §7's securities-suit mention; keep the Florida verdict and the FSD-naming injunction, drop the rest to a clause. The "Customer concentration" paragraph (l.123) repeats the xAI $430M and SpaceX $318M already in the §7 table (l.153); keep one.
- **business.md §7 (599 + three tables).** The board paragraph (l.129) carries the bylaw quotes and three 2025 vote results; the 3% threshold and the annual-election vote could go to a clause each. "Capital allocation" (l.158) re-quotes the "in excess of $25 billion" capex sentence that already appears in §4 and §6.3 (three times in the file) and the "$30 billion" facilities that appear in §4; state each once. The bitcoin sentence is colour.
- **business.md §3 (522).** "Why operating margin fell" (l.57) restates numbers that sit in the two tables above it (credits 2.76B / 1.99B / 146M; margin 26.7% to 15.4%) and again in §6.1; keep the causes, drop the repeated figures. The Megafactory sentence (l.73) duplicates indicator 4 and the outlook.
- **business.md §1 (321).** The history sentence carries five tags and details (Texas move, SolarCity) repeated in §7; one clause each.
- **business.md §2 (329).** "The line is vanishing" (l.39) repeats $439M and $146M from the table directly above.
- **outlook.md §4 (353).** The verbatim Outlook page must stay (§7 skeleton). But the "numbers and dates that exist" bullets re-quote the same CFO sentences that appear under claims 1–4 and in §3 (the energy-margin sentence appears three times: §3, §4, claim 3); keep the §4 bullet list to items not quoted again in §5, or shorten each bullet to the operative words.
- **outlook.md §3 (391).** "New models" (about 100 words) partly duplicates claims 5–6 and §4; the Optimus block carries three quotes where one plus "no dates" would do.
- **outlook.md §5 (480).** Claims 1 and 2 quote the same passage (l.71): one quote can serve both. Claim 3's quotation can be cut to the "normalize" sentence. The closing "Not sharpened" paragraph can be halved without losing the list.

---

## 9. As-of discipline (§12.5)

Every date in both drafts was scanned. The latest events relied on are the 2026-07-22 deck and call and the 2026-07-23 10-Q. Forward-looking mentions (December 2026 SpaceX sale restriction, May 2026 appeal, Q3/Q4 2026 claim horizons) are statements made in the cached 10-Q or call. "Launched Robotaxi in three cities in Florida in July", the Model YL launch and the Cybercab employee rides are in the 2026-07-22 deck (`slides.txt` l.10, l.19, l.28). The transcript's posting date (2026-08-05) is disclosed at the top of outlook.md and in Sources, and only call content is used. No information published after 2026-07-23 was found in either draft, and none was used in this review.

---

## 10. Company-specific content checks (owner's list)

| Ask | Where | Verdict |
|---|---|---|
| (a) how a carmaker's margins work | business.md §3 first paragraph: fixed cost that "does not fall when fewer cars are made", volume sharing the fixed cost, price cuts, ramp costs, mix and tariffs, each with the company's own phrase and tag | Present and plain. One spliced quote to repair (REVISE 2) |
| (b) regulatory credits: what, why near-pure profit, five-year series | §2: plain explanation, the 10-K's own definition, "negligible incremental costs", a table FY2021–FY2025 plus Q2 2025 / Q2 2026 with credits as % of operating income, and the OBBBA-driven decline with the $841M to $287M backlog | Present; all 21 cells verified |
| (c) how big energy storage is (GWh, revenue, gross profit) | §3 second table: GWh, revenue, gross profit, margin, five years plus Q2; prose on Lathrop / Shanghai / Houston capacity, margin swings and the $10.05B backlog | Present; all 24 cells verified |
| (d) robotaxi, Cybercab, Optimus, AI chips strictly as management claims; checkable milestones in outlook §5 | business.md §1 "what the company says it is building; none has disclosed revenue"; §6.4 "robotaxi revenue is not disclosed"; outlook §3 opens "Everything here is management's claim, not fact" and each block has a "Working if" test; claims 4–8 carry the milestones (Megapack 3, Semi, Optimus, robotaxi metros, FSD count); AI5 timing is quoted in §4 but, correctly, not made a claim because it is a spoken "hopefully" with no deck counterpart | Present and correctly framed |
| (e) two reportable segments and the quarterly KPIs | §2 table uses the five income-statement revenue lines and names the two reporting segments through the segment notes (Note 16 / Note 14); §8 indicators 1, 3, 4 are deliveries/production, credit revenue and storage deployed; the P&D release is cited as the KPI source. The sentence "Its second business is large batteries" (§1) and "**Energy** is covered in §3" (§2) make the segment split clear | Present. Suggest one explicit sentence in §2 that the two reportable segments are Automotive (which includes services) and Energy Generation and Storage, per Note 16 |

---

## 11. Verdict: REVISE

Items 1–6 are factual or rule-2 matters; item 7 is length. Each states file and line, the problem, the evidence, and the fix.

### Must fix

1. **business.md l.140 (pay table, "Status at Q2 2026", 2018 award column)** — "plaintiff's counsel awarded about $65 million" exists in no cached source. Evidence: `10-K-FY2025.txt` l.2572 says the Chancery court "awarded Plaintiff's counsel fees in the amount of $345 million" (December 2, 2024) and that on December 19, 2025 the Delaware Supreme Court "significantly reduced the attorney fee award", giving no figure; `10-Q-2026-Q2.txt` Note 9 (l.753–759) and Note 11 (l.863–911) carry no fee figure. Fix: replace with "the Chancery court's $345 million fee award to plaintiff's counsel was 'significantly reduced' by the Supreme Court, amount not stated [10-K FY2025, Note 13]", or delete the fee clause.
2. **business.md l.45 (§3, "How a carmaker's margin works")** — the quotation "primarily due to a lower average selling price on our vehicles driven by overall price reductions year over year" splices two sentences. Evidence: `10-K-FY2023.txt` l.1071 (gross margin paragraph) reads "The decrease was primarily due to a lower average selling price on our vehicles partially offset by the favorable change in our average combined cost per unit of our vehicles and IRA manufacturing credits earned"; "driven by overall price reductions year over year" is from the revenue paragraph at l.1014. Fix: 'in 2023 automotive gross margin fell from 28.5% to 19.4% "primarily due to a lower average selling price on our vehicles", a price the same report ties to "overall price reductions year over year" [10-K FY2023, Item 7]'.
3. **business.md l.6 (§1)** — "in six factories in the United States, China and Germany" is unsupported. Evidence: `10-K-FY2025.txt` Item 2 l.799–807 lists eight primary manufacturing facilities (Gigafactory Texas, Fremont, Nevada, Berlin-Brandenburg, Shanghai, Megafactory Shanghai, Gigafactory New York, Megafactory Lathrop); `slides.txt` p.6 l.19 shows cars in production at California, Shanghai, Berlin and Texas, with Nevada "Commissioning" for Semi. Fix: "in four car factories (Fremont and Austin in the United States, Shanghai, and Berlin), with the Semi to come from Nevada [10-K FY2025, Item 2] [Q2 2026 Update, p.6]".
4. **business.md l.140 (pay table, 2025 award column)** — "the 20-million-vehicle goal deemed probable ($9.82 billion still to expense)" names a milestone the filings do not name. Evidence: `10-Q-2026-Q2.txt` l.826 and `10-K-FY2025.txt` l.2362 say only "the operational milestone that was considered probable of achievement". Fix: "one of the twelve operational goals, not named in the filing, deemed probable ($9.82 billion still to expense)"; or keep the guess and label it "our inference from the size of the amount, not stated by Tesla".
5. **business.md l.91 (§4)** — "Debt of $9.1 billion is almost all owed by subsidiaries against specific assets" mischaracterises the largest loan. Evidence: `10-Q-2026-Q2.txt` l.733 (corrected in cycle 2 from l.729) "Non-recourse debt refers to debt that is recourse to only assets of our subsidiaries"; the China Working Capital Facility (5,888 of 9,080 principal, l.703) is "an unsecured revolving facility of up to RMB 20.00 billion" (`10-K-FY2025.txt` l.2118); the Automotive Asset-backed Notes (2,366, l.702) are the part backed by specific vehicles (l.2106). Fix: 'Debt of $9.1 billion is almost all "non-recourse", meaning lenders can claim only the borrowing subsidiary's assets, not Tesla's; the largest piece is a $5.9 billion unsecured Chinese working-capital facility (a revolving loan for day-to-day needs), and most of the rest is notes backed by leased or financed cars [10-Q Q2 2026, Note 8] [10-K FY2025, Note 9]'.
6. **business.md l.91 (§4) and l.158 (§7)** — the CFO's "up to $30 billion" of debt facilities is a machine-transcript number with no deck or 10-Q counterpart. Evidence: `transcript.txt` l.71; `10-Q-2026-Q2.txt` l.1008 says only "may include additional funding" and l.1201 "drawdowns on existing or new" facilities, no amount. §3 rule 2 allows the quotation as wording but not as a fact. Fix: at both places add, after the quotation, "(a spoken figure; the 10-Q gives no amount)", and keep it out of any table; or drop the amount and keep "securing certain debt facilities". outlook.md l.74 already carries the right caveat.
7. **Length, both files** — business.md 3,260 prose words (target 2,000–3,000, aim lower half); outlook.md 1,447 (target 800–1,200). Cut at least 500 and 300 respectively, using the per-section map in §8 above: dedupe the capex quote (three times), the $30B facilities (twice), the xAI/SpaceX Megapack sales (twice), the credit figures (table plus prose), the energy-margin CFO sentence in the outlook (three times); shorten the Musk risk-factor quote and the §6.4 litigation list; trim the outlook §4 bullet list to items not re-quoted in §5. Re-run `python3 -P /tmp/tsla-orch/wc_prose.py` and record the counts in the self-check.

### Nice to have

8. **business.md l.127** — "CEO of Neuralink and The Boring Company": `10-KA-FY2025.txt` l.198–199 makes him "founder of The Boring Company ... and Neuralink Corp. ... where he serves as the Chief Executive Officer". Write "founder of The Boring Company and CEO of Neuralink".
9. **business.md l.137** — "(shares issued August 15)" → "(accounting grant date August 15, 2025)" per `10-K-FY2025.txt` l.2299.
10. **business.md l.41** — "growing about 20% a year" → "up 19% in 2025 and 50% year on year in Q2 2026" (`10-K-FY2025.txt` l.1000; `slides.txt` p.4 l.13).
11. **business.md l.91** — "'AI infrastructure', meaning data centers" → "'AI infrastructure' (the 10-Q's capex language is 'compute infrastructure and data centers')" (`10-Q-2026-Q2.txt` l.1046), so the gloss is Tesla's, not ours.
12. **outlook.md l.23 vs l.49–50** — the cached deck text carries two line-break artefacts on p.10 ("hardware- related", "se rvices"). Normalise both quotations to "hardware-related" and "services" and add one clause to Sources: "two line-break artefacts in the cached p.10 text were normalised".
13. **outlook.md l.69 (claim 7)** — define "live" so the check is mechanical: "shows more than seven metros with a status other than 'Preparations Underway'".
14. **business.md l.89 (§4 table sources)** — the stock-based compensation totals sit on the cash-flow statements (`10-K-FY2023.txt` l.1466; `10-K-FY2025.txt` l.1446; `10-Q-2026-Q2.txt` l.321), i.e. Item 8 / Item 1, not in the equity-plan notes; retag or add those tags.
15. **business.md l.73** — Lathrop and "near Houston" are not on deck p.6 (which says "California" and "Texas"); add `[10-K FY2025, Item 2]` (l.807) and `[10-K FY2025, Item 7]` (l.899) when trimming.
16. **business.md §2** — add one sentence naming the two reportable segments (Automotive, which includes services and other; Energy Generation and Storage) with the Note 16 tag, so the owner's ask (e) is explicit rather than implied.
17. **business.md §8 indicator 5** — one more clause that the metric is defined by the 2025 award footnote and has appeared in three decks, so the owner locks it knowing it is young.

---

## Withdrawals (first marked NOT FOUND, then found; kept per §17)

- "operational milestones relating to profitability" — first NOT FOUND in the 10-K/A; the phrase is line-wrapped across `10-KA-FY2025.txt` l.921–922. PASS.
- "$841 million" — NOT FOUND in the 10-Q; it is in `10-K-FY2025.txt` l.1564, which the sentence also tags. PASS.
- "1,636,129" — not in the 10-K; the draft says "about 1.64 million", which is at l.867. PASS.
- "cease using the term 'Full Self-Driving Capability'" — not in the 10-Q; it is in `10-K-FY2025.txt` l.2608 (Note 13), the tagged source. PASS.
- "NHTSA" — the 10-Q spells out "National Highway Traffic Safety Administration" (l.903). PASS.
- "207.5 million", "$158.4 billion", "1,119 million" — rounded forms of 207,498,721 (l.1526), 158,359,009,867 (l.1085), 1,118,920,427 (`8-K-2025-11-07...` l.209). PASS.
- "March 12, 2026" — not in the 10-Q; it is in `10-KA-FY2025.txt` l.1588 (Item 13), which the table row also tags. PASS.
- "$674 million" bitcoin — the 10-Q shows "Digital assets | 674" (l.124, l.574). PASS.
- "SolarCity" — not in the FY2025 10-K body; it is in `10-KA-FY2025.txt` l.192 (Item 10), a tag on the sentence. PASS.
- "staggered" three-year terms — not stated in words; the director table's expiry years (2026 / 2027 / 2028, l.178–186) establish three classes. PASS as a description of the table.
- "no cash or equity pay" for outside directors — the 2025 Director Compensation Table (l.1302–1309) shows dashes in every column. PASS.
- "Two years' service" — the 8-K says "vest upon the second anniversary of August 3, 2025 ... subject to Mr. Musk remaining in continuous service" (l.90). PASS.
- "all 12 vested" — the 10-Q says the final order allowed the CEO "to exercise the 2018 CEO Performance Award in full" (l.753). PASS.
- "$23.34" as the 2018 exercise price — `8-K-2025-08-04...` l.94 "equal to the exercise price per share of the 2018 CEO Award". PASS.

---

## Fixed directly

Tag (source unambiguous, verified):
- business.md l.10 — added `[Q2 2026 call, Elluswamy remarks]` after `[10-K FY2025, Item 1]`, because the 10-K sentence (l.147) gives June 2025 but not Austin; `transcript.txt` l.79 gives Austin. The Sources entry for the call now names "Elluswamy remarks" (l.77–87).

Jargon glossed in place, meaning unchanged (no numbers, quotes, claims, indicators or structure touched):
- business.md l.55 (§3 table) — "Capex ($M)" → "Capex (capital spending, $M)".
- business.md l.73 — after the CFO quote, added "(ASPs: average selling prices)".
- business.md l.84, l.87 (§4 table) — "Net income attributable to common stockholders" → "... (profit belonging to shareholders)"; "Total debt, principal" → "... (amount borrowed)".
- business.md l.89 — "valuation allowance" quote → added "(a tax-accounting reserve)".
- business.md l.91 — "a $5.9 billion Chinese working-capital facility" → "... (a revolving loan for day-to-day needs)".
- business.md l.97 — "the North American attach rate below 55%" → "the North American attach rate (the share of new deliveries sold with an FSD subscription) below 55%".
- business.md l.103 — "a 4680 line" → "a 4680 battery-cell line"; "a cathode plant" → "a cathode (battery-material) plant".
- business.md l.101 — "days of vehicle inventory" → "days of vehicle inventory (unsold cars measured in days of sales)".
- business.md l.113 — "and dilution if equity is raised" → "and dilution (each existing share owning a smaller slice) if new shares are sold to raise money".
- business.md l.115 — "$129 million compensatory and $200 million punitive damages" → "$129 million compensatory (to cover losses) and $200 million punitive (to punish) damages"; "a securities suit over" → "a securities suit (shareholders suing over statements made to investors) over".
- business.md l.129 — after the bylaw quote, added "(a suit a shareholder brings on the company's behalf)"; "supermajority voting" → "supermajority voting (rules needing more than a simple majority)".
- business.md l.131 — "beneficially owned" → "beneficially owned (owned or controlled)"; "restricted shares of the 2025 award" → "restricted shares (shares forfeited if conditions are not met) of the 2025 award".
- business.md l.138 (pay table) — "in 12 tranches each equal to 1%" → "in 12 tranches (slices) each equal to 1%".
- business.md l.139 — "Market cap milestones" → "Market cap (stock-market value) milestones"; "adjusted EBITDA of $50 billion" → "adjusted EBITDA (a profit measure before interest, tax, depreciation and share-based pay) of $50 billion".
- business.md l.140 — "exercised about 304.0 million options and net-settled the exercise price" → "exercised (used) about 304.0 million options and net-settled the exercise price (paid the option price by giving up shares rather than cash)"; "grant-date fair value $26.06 billion" → "grant-date fair value (the accounting value of the award when granted) $26.06 billion".
- business.md l.150 — "xAI Series E preferred stock" → "xAI Series E preferred stock (a class of investor shares)".
- outlook.md l.12 — after the EMEA quote, added "(EMEA: Europe, Middle East and Africa)".
- outlook.md l.33 — "the attach rate rise" → "the attach rate (share of new deliveries taking FSD) rise".
- outlook.md l.37 — after the S-curve quote, added "(an S-curve: slow start, steep middle, flat end)".
- outlook.md l.39 — "an Austin fab at" → "an Austin fab (chip factory) at".
- outlook.md l.65 — after claim 3's tags, added "(A warranty true-up is a catch-up charge to the estimate of future repair costs.)".

No typos found. All 62 outlook quotations re-verified after the edits (same result: 62 found, two deck artefacts as described in §4).

Word counts after fixes (`/tmp/tsla-orch/wc_prose.py`, §3 rule 7 basis): **business.md 3,260** (was 3,179), **outlook.md 1,447** (was 1,417). Both remain over target; the glosses cost about 110 words, which the writer's cuts must absorb.

Scratch scripts: `/tmp/tsla-orch/reviewer/find.py`, `quotes.py`, `tags.py`, `apply_fixes.py`. No network access; no git command of any kind; nothing written outside `companies/TSLA/`.


---

## Cycle 2 (re-check of the writer's second pass, 2026-09-09)

_Re-reviewed against the cached primary texts only, with the same tools as cycle 1 (`find.py`, `quotes2.py`, `tags2.py` in `/tmp/tsla-orch/reviewer/`). Line numbers for the drafts refer to the revised files (business.md 201 lines, outlook.md 82 lines before my cycle-2 edits)._

### 1. REVISE list — resolution, item by item

| # | Item | Result | Evidence |
|---|---|---|---|
| 1 | "$65 million" fee award | **PASS** | business.md l.138 now reads "the Chancery court's $345 million fee award to plaintiff's counsel was 'significantly reduced' by the Supreme Court, amount not stated"; `10-K-FY2025.txt` l.2572 "awarded Plaintiff's counsel fees in the amount of $345 million" and "The Court also significantly reduced the attorney fee award". Tag [10-K FY2025, Note 13] in the column's Sources row |
| 2 | Spliced FY2023 margin quote | **PASS** | business.md l.45: "primarily due to a lower average selling price on our vehicles" (`10-K-FY2023.txt` l.1071) and "overall price reductions year over year" (l.1014) are now two quotations, each verbatim |
| 3 | "six factories" | **PASS** | l.6: "Model 3, Model Y, Model S, Model X and Cybertruck in four car factories (Fremont and Austin in the United States, Shanghai, and Berlin), with the Semi to come from Nevada". `10-K-FY2025.txt` l.145 "We currently manufacture five different consumer vehicles - the Model 3, Y, S, X and Cybertruck"; Item 2 l.799–807; `slides.txt` l.19 (p.6 capacity table) and l.10 (p.3 "Tesla Semi remains on track for production this year at our new factory in Nevada") |
| 4 | Named "probable" milestone | **PASS** | l.138: "one of the twelve operational goals, not named in the filing, deemed probable ($9.82 billion still to expense)"; `10-Q-2026-Q2.txt` l.826 |
| 5 | Debt "against specific assets" | **PASS** | l.89 now: almost all "non-recourse", lenders can claim only the borrowing subsidiary's assets; $5.9 billion unsecured Chinese working-capital facility; most of the rest notes backed by leased or financed cars. `10-Q-2026-Q2.txt` l.733 (definition; the writer is right that l.729 is footnote (1); corrected above), l.702–707 (China 5,888; Automotive ABS 2,366 of 3,190 non-China non-recourse = 74%); `10-K-FY2025.txt` l.2118 "unsecured revolving facility", l.2104 "backed by these automotive assets" |
| 6 | Transcript-only "$30 billion" | **PASS** | Kept once, l.89, with "(a spoken figure; the 10-Q gives no amount)" and tags [Q2 2026 call] [10-Q Q2 2026, Item 2] (`transcript.txt` l.71; `10-Q-2026-Q2.txt` l.1008). Dropped from §7 (l.156 now "Funding: the cash and debt in §4, plus an undrawn $5 billion revolving credit line"). outlook.md l.69 caveat unchanged |
| 7 | Length | **PASS** | business.md 2,726 and outlook.md 1,112 as received; 2,737 and 1,119 after my cycle-2 edits (canonical `wc_prose.py`). Both inside target; business.md in the lower half |
| 8 | Neuralink / Boring | **PASS** | l.125 "founder of The Boring Company and CEO of Neuralink, and led xAI Holdings, a SpaceX subsidiary since February 2026"; `10-KA-FY2025.txt` l.196–199 |
| 9 | "shares issued August 15" | **PASS** | l.135 "accounting grant date August 15, 2025"; `10-K-FY2025.txt` l.2299 |
| 10 | "about 20% a year" | **PASS** | l.41 "up 19% in 2025 and 50% year on year in Q2 2026"; `10-K-FY2025.txt` l.1000; `slides.txt` l.13 (Services YoY 50%); tag [Q2 2026 Update, p.4] added |
| 11 | "meaning data centers" | **PASS** | l.89 quotes the 10-Q's "driven by our AI initiatives, including investments in compute infrastructure and data centers" (l.1046) and "AI infrastructure" (Note 5 l.645) with no reviewer gloss |
| 12 | Deck artefacts | **PASS** | outlook.md l.49 "hardware-related", l.50 "services"; Sources l.73 names both artefacts and the normalisation. `slides.txt` l.31 confirms "hardware- related" and "se rvices" are the only differences (quotes2.py: l.49 and l.50 match once the two artefacts are restored) |
| 13 | Claim 7 "live" | **PASS** | l.64: "more than seven metros with a status other than 'Preparations Underway'"; `slides.txt` l.28 has exactly seven such metros today |
| 14 | SBC tags | **PASS** | l.87 "stock-based compensation (cash-flow statements) [10-K FY2023, Item 8] [10-K FY2025, Item 8] [10-Q Q2 2026, Item 1]"; `10-K-FY2023.txt` l.1466, `10-K-FY2025.txt` l.1446, `10-Q-2026-Q2.txt` l.321 |
| 15 | Lathrop / Houston tags | **PASS** | l.73 adds [10-K FY2025, Item 2] [10-K FY2025, Item 7]; `10-K-FY2025.txt` l.807 "Megafactory Lathrop", l.899 "new Megafactory near Houston, Texas" |
| 16 | Two segments named | **PASS** | l.41 "Tesla reports two segments, automotive (including services and other) and energy generation and storage [10-K FY2025, Note 16]"; `10-K-FY2025.txt` l.2681 "two operating and reportable segments: (i) automotive and (ii) energy generation and storage. ... the automotive segment also includes services and other" (also l.137) |
| 17 | Indicator 5 newness | **PASS** | l.166 "defined by the 2025 CEO Performance Award footnote and shown in only three decks so far (Q4 2025 to Q2 2026)"; `slides.txt` l.16 footnote (2) |

Other writer changes, verified: l.60 "led by a '$283 million increase in stock-based compensation'" (`10-Q-2026-Q2.txt` l.1156 "driven by a $283 million increase ... a $134 million increase in employee and labor costs"), PASS; l.156 '"None" under "Purchases of Equity Securities by the Issuer and Affiliated Purchasers"' (`10-K-FY2025.txt` l.849–851), PASS; l.10 shortened AI quote (l.131), PASS; l.29 plain explanation kept with "negligible incremental costs" (l.1564), PASS; l.39 "eliminates 'certain penalties for violations of certain regulatory credit programs'" (l.1912), PASS; l.113 "our future business depends on development of our driver assistance systems and autonomous driving solutions" (l.449, mid-sentence lower case), PASS; l.115 elided Musk quote (l.591), PASS; l.127 Straubel "co-founder ... CEO of Redwood Materials" (`10-KA-FY2025.txt` l.329–333), Denholm "since 2018" (l.212), PASS; l.142 "product goals", "directionally consistent with Mr. Musk's vision", "misaligned with current or future consumer demand" (l.747, l.749), PASS; l.125 Zhu "who built Gigafactory Shanghai" paraphrases "led the construction and operations of Gigafactory Shanghai" (l.414), accepted.

### 2. Skeleton and format

business.md: title and as-of line unchanged; §1–§8 headings at l.4, 14, 43, 75, 91, 103, 123, 158, Glossary l.171, Sources l.182, all in order; `_Proposed — owner to review and lock._` at l.160; 8 indicators; 8 glossary entries. outlook.md: header with tier at l.2; §1–§5 at l.6, 21, 27, 43, 56; Sources l.71; no Tone shift; §1 has 8 rows in the same order as §8. Tag mapping (tags2.py): business.md 16 tag families used, all mapped, none unused (the `[8-K 2025-05-16 Hartung]` entry was correctly deleted with its last use); outlook.md 8 used, all mapped, none unused; after my cycle-2 tag addition, 9 used and 9 mapped.

### 3. Quotations (shortened or split)

quotes2.py over every double-quoted string of 10+ characters in both files against all 24 cached texts: business.md 77 strings, 75 found; the two misses at l.142 are the regex spanning the gap between two quotations, and the three real quotations on that line are found individually (`10-K-FY2025.txt` l.747, l.749; `10-KA-FY2025.txt` l.1256 "0.00:1"). outlook.md 51 strings, 48 found; the misses are the two normalised deck artefacts (l.49, l.50; verified equal to `slides.txt` l.31 with the artefacts restored) and a bold claim label the regex caught at l.61. So every quotation in both files is verbatim. Specifically re-read word for word: business §1 l.10 (`10-K-FY2025.txt` l.131, l.133; `10-K-FY2024.txt` l.133), §2 l.27–41, §3 l.45–73 (`10-K-FY2023.txt` l.1065, l.1071, l.1014; `10-K-FY2024.txt` l.1094; `transcript.txt` l.65, l.69), §6.4 l.113 (l.449; `10-Q-2026-Q2.txt` l.897; `10-K-FY2025.txt` l.2608; `transcript.txt` l.25), §6.5 l.115 (l.591; `10-KA-FY2025.txt` l.1526), §7 l.125–156; outlook §2 l.23–25 (`slides.txt` l.10; `transcript.txt` l.55, l.57, l.19, l.21), §3 l.31–41 (l.67, l.23, l.37, l.199; `slides.txt` l.10, l.19, l.25; `slides-2026-Q1.txt` l.31), §4 l.47–54 (`slides.txt` l.31; `10-Q-2026-Q2.txt` l.1046; `transcript.txt` l.71, l.69), claims 3, 7, 10 (l.65, l.69, l.55).

### 4. Claims (§9), as now worded

All ten remain one sentence, one check, single direction, no either/or. Sharpenings labelled: 1, 3, 4, 7, 8, 10 ("our sharpening"); management's number or date: 2, 5, 6; disclosure check labelled with the quarter column: 9. Claim 3's label now says what was sharpened ("the CFO gave only a long-run range and listed a warranty charge among the Q2 causes"); claim 5 states the early check (Nevada Semi "Production" on the Q3 deck); claim 7 defines "live". Verbatim quote and tag under each. Ten claims, fundamentals only.

### 5. Indicator anchoring

Unchanged set of eight; the cycle-1 table stands. Indicator 5 now carries the newness note.

### 6. Required content after the cuts

Carmaker margin mechanics (l.45: fixed cost, absorption, price, ramp, mix, tariffs, tax credits), present. Regulatory credits: plain explanation, "negligible incremental costs", five-year table with Q2 2025 / Q2 2026 and the share of operating income, the OBBBA decline and the $841M to $287M backlog (l.29–39), present. Energy storage size table (l.64–69) with GWh, revenue, gross profit, margin, plus capacity and backlog (l.73), present. Robotaxi, Cybercab, Optimus and chips framed as "what the company says it is building; none has disclosed revenue" (l.10), "Everything here is management's claim, not fact" (outlook l.29), milestones in claims 4–8, present. Two segments named (l.41). Quarterly KPIs: deliveries, production, storage deployed and credit revenue are indicators 1, 3, 4 with the P&D release and deck named as sources; §1 rows 1, 3, 4. Each §6 scenario still has what would happen, an early warning and an exposure (l.107–119); each §5 moat still has its source and weakening sign (l.93–101). Nothing the skeleton or the owner's list requires was lost.

### 7. New findings in cycle 2 (all fixed directly; none structural)

- outlook.md l.25 read "Nothing was said about regulatory credits, pricing or the CEO award". The CFO did say "Automotive margins, excluding regulatory credits, declined" (`transcript.txt` l.59) and "the effective pricing and cost management" (l.61); no fee, award or compensation word appears anywhere in the transcript. Reworded to "Nothing was said about the fall in regulatory credit revenue, about pricing plans, or about the CEO award" (the cycle-1 meaning, which was accurate).
- outlook.md l.23 "the profit sentence in §4 is unchanged since January" was tagged only to the Q2 deck. The identical sentence is on the Q4 2025 Update p.13 (`slides-2025-Q4.txt` l.40). Added `[Q4 2025 Update, p.13]` and a Sources entry for `slides-2025-Q4.txt`.
- business.md l.107 "the deck's bridge" — jargon; glossed "(its list of what moved revenue and profit year over year)".
- business.md l.109 "Exposure: up to $2 billion a year of nearly pure profit" understated 2024 (2,763; `10-K-FY2025.txt` l.1336); changed to "about $2 billion a year (2025) of nearly pure profit".
- Review file: the cycle-1 evidence line for item 5 cited `10-Q-2026-Q2.txt` l.729; the recourse definition is at l.733 (l.729 is footnote (1) of the debt table). Corrected in place with a note.

### 8. Word counts after cycle-2 edits (canonical `wc_prose.py`, §3 rule 7)

business.md **2,737** (received 2,726; target 2,000–3,000, lower half); outlook.md **1,119** (received 1,112; target 800–1,200).

### 9. As-of, constraints

No new dates; nothing after 2026-07-23 relied on. No git command; writes confined to `companies/TSLA/` (the two drafts, small edits listed above, and this file); no network; scratch in `/tmp/tsla-orch/reviewer/`.

### Final verdict: **PASS**

Nothing remains open. Two accepted judgement calls for the owner's information: (1) business.md l.8 "about three quarters of it from vehicles and credits (§2)" is arithmetic from the §2 table (69,526 / 94,827 = 73%) pointed to rather than marked "(computed)"; l.107 marks the same figure "(computed)". (2) Indicator 5 (Active FSD subscriptions) is a metric Tesla has published for three quarters under an award-linked definition; it is anchored to a recurring deck row today but is the indicator most likely to be redefined.
