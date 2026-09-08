# Uber Technologies, Inc. (UBER) — Reviewer report, 2026-Q2

_Reviewed 2026-09-08 (cycle 1 of 2) against `companies/UBER/sources/2026-Q2/` only (cached full texts; gatherer notes not used for any ruling). As-of cutoff 2026-08-05. Line numbers below refer to the cached `.txt` files ("L") and to the drafts as they stood before my edits ("b:" business.md, "o:" outlook.md). Page numbers for the transcripts, prepared remarks, press releases and the supplemental deck are printed page numbers, which equal PDF pages (form-feed markers in the text; Q2 transcript p.N starts at L1 / 16 / 70 / 126 / 182 / 241 / 298 / 356 / 413 / 469 / 525 / 583 / 641 / 699 / 759 / 810; Q2 remarks at L1 / 46 / 91 / 136 / 181 / 226 / 271 / 316 / 361; Q2 release at L1 / 45 / 102 / 126 / 181 / 195 / 248 / 290 / 344 / 401 / 448 / 490 / 538; Q1 release at L1 / 44 / 101 / 125 / 180 / 194 / 246 / 284 / 338 / 393 / 447 / 500; deck p.16 at L349, p.17 at L389, p.31 at L1087). The Delivery Hero release and the AV spotlight are tagged by PDF page, as MANIFEST and both Sources lists say. Scratch scripts: `/tmp/uber-orch/reviewer/pg.py` (page-aware grep) and `quotes.py` (verbatim-quote search); the canonical word counter `/tmp/uber-orch/wc_prose.py` was used for length._

**Final verdict (after cycle 2): PASS.** Cycle 1 returned REVISE with 4 required and 3 optional items; the writer resolved all 7 in its second pass and every change was re-verified against the cached sources (see "Cycle 2" at the end of this file). One tag was added directly in cycle 2. The cycle-1 verdict paragraph is kept below for the record.

**Cycle-1 verdict: REVISE** (light second pass). Every number in every table reconciles to the filings, releases and deck, every quoted string is verbatim, both files are inside their length targets, the Delivery Hero deal is treated as pending throughout, and nothing after 2026-08-05 appears. What needs the writer is small and precise: one growth figure is attached to three products when the source gives it for one (§2), one sentence says Delivery Hero is marked to market when the 10-Q says the stake moved to the equity method in Q2 (§4), one table label says "equals" where the figures differ slightly (§2), two paraphrases overstate what management said ("declined to size", "names three pillars"), and a handful of optional precision items. Six tag imprecisions and about thirty jargon glosses were fixed directly and are listed at the end.

---

## 1. Rubric (§14)

Read as the owner would: a smart 16-year-old with no finance background.

1. **Can I explain what this company does, and who pays it, in two sentences?** **Yes.** §1 does it in two: an app that matches riders, eaters and shippers with independent drivers, couriers and carriers; the drivers and merchants pay Uber a fee, and Uber keeps about a quarter of the $58 billion that flows through it each quarter.
2. **Do I know exactly what would kill it, and what the early warning sign is?** **Yes.** §6 ranks five scenarios (robotaxi owners going direct, driver reclassification, insurance outrunning fares, fee caps and price wars, overpaying and over-borrowing for Delivery Hero), each with what would have to happen, a concrete early warning (Waymo not renewing Austin/Atlanta; the legal-reserve add-back; reserve additions outgrowing Mobility bookings and prior-year adjustments turning positive; promotions outgrowing bookings; the bridge not refinanced in Q3) and a stated exposure.
3. **Do I know why the margins are what they are, and whether cost scales with usage?** **Yes.** §3 separates the half of cost that rises with every trip (insurance, card fees, driver pay where Uber is the legal provider) from the four operating lines that fell from $1.71 to $1.06 per trip, explains why gross margin is an accounting artefact here, shows capex below 2% of revenue, and gives insurance its own table.
4. **Could I predict what the scorecard will check next quarter, from §5 of the outlook alone?** **Yes.** All 11 claims are single-direction and mechanical; every sharpening is labelled; both disclosure checks name their column or event.
5. **Did nothing in the report require knowledge I don't have?** **Now yes.** Before review about thirty terms were unexplained (D&A, captive insurer, actuarial, GAAP, marked to market, collateral, arbitration, mass tort, bridge loan, synergies, leverage, VAT, receivable, investment grade, revolver, commercial paper, intangibles/amortized, total return swap, diluted shares, cc, YoY, bps, operating leverage, lapping, organic, run-rate, ETR, accretive). All are now glossed inline (see "Fixed directly"). Nothing remains that the glossary or the text does not carry.

---

## 2. Skeleton and format compliance

**business.md**

| Requirement (§6) | Status |
|---|---|
| `# <Company> — The Business` | OK (`# Uber Technologies, Inc. — The Business`) |
| `_As of <QLABEL>. Written <date>._` | OK (`_As of Q2 2026. Written 2026-09-08._`) |
| §1 What they do (incl. short history) | OK; history at b:8 (2009, NYSE May 2019, CEO since 2017, losses to profit) |
| §2 How the money comes in (5-year segment table) | OK; revenue table FY2021–FY2025 + Q2 2026, plus a Gross Bookings / Revenue Margin table |
| §3 The economics (revenue, GM, OM, capex, capex/revenue) | OK; plus per-trip cost, an insurance-reserve table and two segment-profit tables kept apart across the measure break |
| §4 How profitable, really (5-year table) | OK |
| §5 Why customers don't leave (source + weakening sign) | OK; liquidity and cross-platform habit; three signs |
| §6 What could break it (ranked; early warning; exposure; concentration) | OK; five ranked scenarios, "Other exposures", "Concentration: none" with source |
| §7 Who runs it and what they do with the cash | OK; people, ownership and pay, cash priorities, cash table |
| §8 Indicators (5–8; name / why / where) | OK; 7 indicators, each with source location |
| `_Proposed — owner to review and lock._` | OK (b:163) |
| Glossary (only unavoidable terms, one sentence each) | OK; 6 entries, each one sentence, each used repeatedly |
| Sources (every tag mapped; page basis stated) | OK; 23 tag families used, 23 mapped, none unused (checked programmatically); PDF-page exceptions for the Delivery Hero release and AV spotlight match MANIFEST |
| Heading order | OK |
| Length 2,000–3,000 prose words | **PASS**: 2,579 before review, 2,661 after my glosses (`/tmp/uber-orch/wc_prose.py`) |

**outlook.md**

| Requirement (§7) | Status |
|---|---|
| `# <Company> — Outlook as of <QLABEL>` | OK |
| `_Transcript source tier: ... Written <date>._` | OK (`company-published (call transcript and separate prepared remarks)`; MANIFEST: tier 1, FactSet corrected transcript and remarks from Uber's IR CDN) |
| §1 one row per indicator; this q / last q / expected | OK; 7 rows matching business.md §8 in order |
| §2 What management says | OK |
| §3 Growth engines (what / how big / claim / working-or-not) | OK; seven engines, each with a "Tell" |
| §4 Guidance verbatim | OK; eight bullets, all verified word for word (§4 below) |
| §5 Claims (6–12) | OK; 11 claims |
| §6 Tone shift | Correctly omitted (first run) |
| Sources | OK; 9 tag families used, 9 mapped, none unused; page basis stated |
| Length 800–1,200 prose words | **PASS**: 1,127 before review, 1,180 after glosses. **Twenty words of headroom**: the writer's cycle-2 edits to outlook.md must be word-neutral |

**Indicator anchoring (§8 of AGENTS.md)** — each proposed indicator and the recurring disclosure it rests on; "where" checked in both the Q2 and Q1 2026 releases/filings:

| # | Indicator | Recurring disclosure | Anchored? |
|---|---|---|---|
| 1 | MAPCs and Trips, YoY growth | Release p.1 bullet and p.2 table every quarter (Q2 L20–21, L49–50; Q1 L18–19, L49–50); deck p.10 five-quarter series (L184–225); 10-Q Item 2 | Yes |
| 2 | Gross Bookings by segment, cc growth | Release p.2 "Gross Bookings" table (Q2 L70–77; Q1 L69–76); 10-Q Item 2 | Yes |
| 3 | Revenue Margin, Mobility / Delivery | Deck p.16–17 print it (L362–363, L399–401); computable from release p.2 segment revenue ÷ segment bookings | Yes |
| 4 | Segment Operating Income as % of segment Gross Bookings | Release p.3 segment table (Q2 L106–113; Q1 L105–112); deck p.16–17 print the margin | Yes; the measure only exists from Q1 2026, which the report says plainly |
| 5 | Insurance reserves (short + long) and the cash-flow add-back | Release p.6 balance sheet (two lines) and p.8 cash flow "Accrued insurance reserves" (Q2 L245/255, L316; Q1 L209/216, L311) | Yes |
| 6 | Free cash flow, quarter and TTM | Release p.13 / Q1 p.12 reconciliation; deck p.31 TTM table (L1087–1137) | Yes |
| 7 | Diluted weighted-average shares; buybacks; total debt | Release p.7 income statement, p.8 cash flow, p.6 balance sheet; 10-Q Notes 5 and 7 | Yes, but three figures in one cell (see §9 below; owner's call at lock) |

None depends on a dollar target or growth percentage given once on a call. The one-off figures (15 AV cities, $10 billion of AV capital, "hundreds of millions" of insurance savings) are tracked as claims, as §8 asks.

---

## 3. Citation spot-check

Legend: PASS = number or wording found in the tagged source; FAIL = not in the tagged source, wrongly characterized, or tagged to the wrong place. Computed cells were re-derived from the sourced inputs. Full lines were printed before any ruling (§17 lesson).

### 3(a) business.md §2 revenue table (b:16–22) — every cell

Inputs: `10-K-FY2023.txt` Note 2 L3099–3107 (FY2021–FY2023); `10-K-FY2025.txt` Item 7 L1774–1778 and Note 13 (FY2024–FY2025); `10-Q-2026-Q2.txt` Note 10 L1357 and release p.2 L83–87 (Q2 2026).

| Row | Source values (USD m) | Result |
|---|---|---|
| Mobility 6,953 / 14,029 / 19,832 / 25,087 / 29,670 / 7,363 | same | PASS ×6 |
| Delivery 8,362 / 10,901 / 12,204 / 13,750 / 17,248 / 5,245 | same | PASS ×6 |
| Freight 2,132 / 6,947 / 5,245 / 5,141 / 5,099 / 1,583 | same | PASS ×6 |
| Other 8 / — ×5 | "All Other revenue 8 / — / —"; no such line after 2022 | PASS ×6 |
| Total 17,455 / 31,877 / 37,281 / 43,978 / 52,017 / 14,191 | same | PASS ×6 |

30/30 PASS. "The 2022 jumps include UK gross accounting and the Transplace acquisition" (b:24): FY2023 10-K Note 13 footnote L4559 ("In 2022, we modified our arrangements in certain markets and, as a result, present the respective Mobility and Delivery revenue on a gross basis") and Note 2 L3140 (Transplace, Q4 2021). PASS.

### 3(b) business.md §2 Gross Bookings table (b:26–34) — every cell, including the writer's flag (a)

Inputs: quarterly segment Gross Bookings tables in `10-K-FY2023.txt` Item 7 L1834–1838 (eight quarters 2022–2023) and `10-K-FY2025.txt` Item 7 L1842–1846 (eight quarters 2024–2025); annual totals `10-K-FY2023` L1354, `10-K-FY2025` L1358, `DEF14A-2026.txt` Pay Versus Performance table L4047–4059; Q2 2026 release p.2 L70–77; Revenue Margins deck p.16 L362–363 and p.17 L399–401.

| Row | Re-derivation | Result |
|---|---|---|
| Mobility GB 52.7 / 68.9 / 83.0 / 97.5 / 29.0 | 10,723+13,364+13,684+14,894 = 52,665; 14,981+16,728+17,903+19,285 = 68,897; 18,670+20,554+21,002+22,798 = 83,024; 21,182+23,762+25,111+27,442 = 97,497; 28,988 | PASS ×5 |
| Delivery GB 55.8 / 63.7 / 74.6 / 90.9 / 27.5 | 13,903+13,876+13,684+14,315 = 55,778; 15,026+15,595+16,094+17,011 = 63,726; 17,699+18,126+18,663+20,126 = 74,614; 20,377+21,734+23,322+25,431 = 90,864; 27,463 | PASS ×5 |
| Freight GB 7.0 / 5.2 / 5.1 / 5.1 / 1.6 | 1,823+1,838+1,751+1,540 = 6,952; 1,401+1,278+1,284+1,279 = 5,242; 1,282+1,272+1,308+1,273 = 5,135; 1,259+1,260+1,307+1,267 = 5,093; 1,571 | PASS ×5 (label nit, REVISE item 3: 6,952 ≠ 6,947, 5,242 ≠ 5,245, 1,571 ≠ 1,583, so "equals Freight revenue" is not exact) |
| Total GB 90.4 / 115.4 / 137.9 / 162.8 / 193.5 / 58.0 | proxy L4059–4047: 90,415 / 115,395 / 137,865 / 162,773 / 193,454; release 58,022. Segment sums reconcile to the totals exactly: 52,665+55,778+6,952 = 115,395; 68,897+63,726+5,242 = 137,865; 83,024+74,614+5,135 = 162,773; 97,497+90,864+5,093 = 193,454 | PASS ×6 |
| Mobility Revenue Margin 26.6 / 28.8 / 30.2 / 30.4 / 25.4% | 14,029/52,665 = 26.64; 19,832/68,897 = 28.78; 25,087/83,024 = 30.22; 29,670/97,497 = 30.43; deck p.16 prints 25.4% (7,363/28,988 = 25.40) | PASS ×5 |
| Delivery Revenue Margin 19.5 / 19.2 / 18.4 / 19.0 / 19.1% | 10,901/55,778 = 19.54; 12,204/63,726 = 19.15; 13,750/74,614 = 18.43; 17,248/90,864 = 18.98; deck p.17 prints 19.1% | PASS ×5 |
| Total revenue / GB 19.3 / 27.6 / 27.0 / 27.0 / 26.9 / 24.5% | 17,455/90,415 = 19.31; 31,877/115,395 = 27.62; 37,281/137,865 = 27.04; 43,978/162,773 = 27.02; 52,017/193,454 = 26.89; 14,191/58,022 = 24.46 | PASS ×6 |
| "n/d" ×5 (FY2021 segment cells) | The FY2023 10-K quarterly table (L1834–1838) covers 2022–2023 only; no FY2021 segment Gross Bookings anywhere in the cached filings (grep "Mobility Gross Bookings" and the 2021 quarterly figures: none) | PASS ×5 |
| "UK gross accounting inflated Mobility's 2022–2025 ratio by about 4 points" (b:36) | Transcript p.11 L541–542: "about 400 basis points is entirely related to this UK business model change" | PASS |

42/42 PASS. **Writer's flag (a) ruling:** the quarterly-summation method is sound; each year's three segment sums add to the annual total Uber prints, to the million, so the series is internally consistent and correctly labelled "(computed)".

### 3(c) business.md §3 economics table (b:46–54) — every cell

Inputs: income statements `10-K-FY2023.txt` L2333–2360, `10-K-FY2025.txt` L2334–2361, `10-Q-2026-Q2.txt` L293–330; trips `10-K-FY2023` L1352 (7,642 / 9,448), `10-K-FY2025` L1356 (11,273 / 13,567), release p.2 (3,867); capex cash-flow lines `10-K-FY2023` L2616, `10-K-FY2025` L2609, release p.8 L326 and p.13 L577.

| Row | Check | Result |
|---|---|---|
| Revenue 17.5 / 31.9 / 37.3 / 44.0 / 52.0 / 14.2 | as 3(a) | PASS ×6 |
| Gross margin 46.4 / 38.3 / 39.8 / 39.4 / 39.8 / 44.9% | cost of revenue 9,351 / 19,659 / 22,457 / 26,651 / 31,338 / 7,815 → 46.43 / 38.33 / 39.76 / 39.40 / 39.75 / 44.93 | PASS ×6; labelled computed; prose says not reported (true: no gross-profit line in any statement) |
| Four operating-cost lines / revenue 63.2 / 41.1 / 34.6 / 31.4 / 27.7 / 30.3% | O&S + S&M + R&D + G&A = 11,036 / 13,103 / 12,891 / 13,817 / 14,395 / 4,298 → 63.23 / 41.10 / 34.58 / 31.42 / 27.67 / 30.29 | PASS ×6 |
| Per trip n/d / 1.71 / 1.36 / 1.23 / 1.06 / 1.11 | 13,103/7,642 = 1.715; 12,891/9,448 = 1.364; 13,817/11,273 = 1.226; 14,395/13,567 = 1.061; 4,298/3,867 = 1.111. FY2021 trips are not in the cached filings (FY2023 10-K L1352 shows 2022–2023 only) | PASS ×6 |
| Operating margin (22.0) / (5.7) / 3.0 / 6.4 / 10.7 / 13.3% | (3,834)/17,455 = −21.96; (1,832)/31,877 = −5.75; 1,110/37,281 = 2.98; 2,799/43,978 = 6.36; 5,565/52,017 = 10.70; 1,890/14,191 = 13.32 | PASS ×6 |
| Capex 298 / 252 / 223 / 242 / 336 / 70 | cash-flow "Purchases of property and equipment" | PASS ×6 |
| Capex / revenue 1.7 / 0.8 / 0.6 / 0.6 / 0.6 / 0.5% | 1.71 / 0.79 / 0.60 / 0.55 / 0.65 / 0.49 | PASS ×6 |

42/42 PASS. Prose at b:44: "$1.71 per trip in 2022 to $1.06 in 2025, and from 11.4% of Gross Bookings to 7.4%": 13,103/115,395 = 11.35%; 14,395/193,454 = 7.44%. PASS.

### 3(d) business.md §3 insurance table (b:62–66) — every cell, including the writer's flag (c)

Inputs: balance sheets `10-K-FY2023` L2287/2295 (1,692+3,028; 2,016+4,722), `10-K-FY2025` L2288/2296 (2,754+7,042; 3,387+9,076), `10-Q-2026-Q2` L245/255 (3,758+9,528); Schedule II `10-K-FY2023` L5024–5057 and `10-K-FY2025` L4780–4817.

| Row | Check | Result |
|---|---|---|
| Reserves (computed sum) 4,720 / 6,738 / 9,796 / 12,463 / 13,286 | 4,720 / 6,738 / 9,796 / 12,463 / 13,286 | PASS ×5 |
| Additions 2,128 / 3,544 / 4,489 / 4,879 / n/d | FY2023 10-K: 2022 = 2,128, 2023 = 3,544; FY2025 10-K: 2023 = 3,544, 2024 = 4,489, 2025 = 4,879. No Schedule II in a 10-Q | PASS ×5 |
| Deductions 1,396 / 1,526 / 1,696 / 2,421 / n/d | FY2023 10-K: 1,396 / 1,526; FY2025 10-K: 1,526 / 1,696 / 2,421 | PASS ×5 |

15/15 PASS. **Writer's flag (c) ruling:** the two schedules agree on 2023's additions and deductions (3,544 and 1,526 in both), so mixing bases affects only the balance columns, and the table's balance row is on the balance-sheet basis throughout (the FY2025 schedule's 2023 balances, 4,754 → 6,986, are gross of the insurer-recoverable "Other" column, footnote (4) L4817). The footnote at b:68 says this. Acceptable as written. Prior-year adjustments +158 / −78 / −21 (b:132): FY2025 Schedule II footnote (1) L4809. PASS.

### 3(e) business.md §3 segment-profit tables (b:72–89) — every cell, and the measure break

Inputs: `10-K-FY2023` Note 13 L4493–4505 and Item 7 L1845; `10-K-FY2025` Note 13 L4353/4395/4435 and L4357/4399/4439, Item 7 L1366; release p.3 L106–113 (Q2 2025, Q2 2026), Q1 release p.3 L105–112; deck p.16–17.

| Row | Source values | Result |
|---|---|---|
| Mobility Segment Adjusted EBITDA 1,596 / 3,299 / 4,963 / 6,497 / 7,899 | same | PASS ×5 |
| Delivery (348) / 551 / 1,506 / 2,471 / 3,572 | same | PASS ×5 |
| Freight (130) / — / (64) / (74) / (33) | same | PASS ×5 |
| Corporate G&A and Platform R&D (1,881) / (2,137) / (2,353) / (2,410) / (2,708) | same | PASS ×5 |
| Adjusted EBITDA n/d / 1,713 / 4,052 / 6,484 / 8,730 | Item 7 tables; FY2021 company Adjusted EBITDA is not printed in either cached 10-K (FY2023 Item 7 L1362/1782/1845 show 2022–2023 only). It is derivable: Total Segment Adjusted EBITDA 1,107 (L4501) minus 1,881 = −774; optional, see REVISE item 6 | PASS ×5 |
| Adjusted EBITDA / GB n/d / 1.5 / 2.9 / 4.0 / 4.5% | 1,713/115,395 = 1.48; 4,052/137,865 = 2.94; 6,484/162,773 = 3.98; 8,730/193,454 = 4.51 | PASS ×5 |
| New measure: Mobility 1,729 / 2,029 / 2,215; Delivery 766 / 961 / 1,055; Freight (26) / (30) / (24); Corporate (935) / (1,077) / (1,103); Non-GAAP Operating Income 1,534 / 1,883 / 2,143 | release p.3 and Q1 release p.3; 10-Q Note 10 L1343–1362 | PASS ×15 |
| Mobility margin 7.3 / 7.7 / 7.6%; Delivery 3.5 / 3.7 / 3.8% | 1,729/23,762 = 7.28; 2,029/26,394 = 7.69; 2,215/28,988 = 7.64; 766/21,734 = 3.52; 961/25,992 = 3.70; 1,055/27,463 = 3.84; deck p.16–17 print the same | PASS ×6 |

51/51 PASS. **Measure break honoured:** Segment Adjusted EBITDA (FY2021–FY2025) and Segment Operating Income (Q2 2025, Q1–Q2 2026) sit in separate tables with different column sets; the intro sentence (b:70) says they "must never be read across", and the 8-K of 2026-01-12 L77 confirms the new measure includes depreciation and stock-based compensation but excludes acquired-intangible amortization. Indicator 4 repeats the warning. No column mixes the two.

### 3(f) business.md §4 cash table (b:97–106) — every cell

Inputs: cash-flow statements `10-K-FY2023` L2600–2616, `10-K-FY2025` L2594–2609, release p.8 L306–326 and p.13 L575–578; FCF `10-K-FY2023` L1950, `10-K-FY2025` L1949; income statements as 3(c).

| Row | Source values | Result |
|---|---|---|
| Operating cash flow (445) / 642 / 3,585 / 7,137 / 10,099 / 2,862 | same | PASS ×6 |
| Capex (298) / (252) / (223) / (242) / (336) / (70) | same | PASS ×6 |
| Free cash flow (743) computed / 390 / 3,362 / 6,895 / 9,763 / 2,792 | −445−298 = −743; Uber's stated FCF for the other five | PASS ×6 |
| Insurance add-back 516 / 736 / 2,230 / 2,819 / 2,660 / 387 | FY2023 10-K: 516 / 736 / **2,015**; FY2025 10-K: 2,230 / 2,819 / 2,660; release p.8: 387 | PASS ×6; the footnote at b:108 discloses the 2023 basis difference (2,015 vs 2,230) correctly |
| Stock-based compensation 1,168 / 1,793 / 1,935 / 1,796 / 1,826 / 550 | same (release p.8 L307: 550) | PASS ×6 |
| FCF minus stock pay (1,911) / (1,403) / 1,427 / 5,099 / 7,937 / 2,242 | re-derived | PASS ×6 |
| Net income (496) / (9,141) / 1,887 / 9,856 / 10,053 / 2,394 | same | PASS ×6 |
| Buybacks — / — / — / 1,252 / 6,523 / 518 | cash-flow "Repurchases of common stock"; none before 2024 | PASS ×6 |

48/48 PASS.

### 3(g) business.md §7 cash table (b:148–159) — every figure

| Row | Source | Result |
|---|---|---|
| $7.0B (Feb 2024) + $20.0B (Jul 2025); ~$15.7B unused | `10-K-FY2025` Note 10 L3882; `8-K 2025-08-06` L79 ($20,000,000,000, July 28, 2025); `10-Q` Note 7 L1239 | PASS |
| Buybacks $1.2B → $6.5B → $3.0B → $0.5B | Note 10 L3884; Q1 release p.8 (3,011); 10-Q Note 7 L1239 ($510M) / release p.8 (518) | PASS |
| Shares 2,108M → 2,068M → 2,040M | `10-K-FY2025` L2312 (2,107,953; 2,067,905); `10-Q` L271 (2,039,994) | PASS |
| Debt principal $12.6B; €14.2B undrawn bridge | `10-Q` Item 1A L2854; `8-K 2026-07-16` L174 | PASS |
| $1.15B 0% exchangeable (May 2025); $1.0B 4.15% 2031 and $1.25B 4.80% 2035 (Sep 2025); $2.0B term loan (Jun 2026) | `8-K 2025-05-20` L86; `8-K 2025-09-11` L94–96; `10-Q` Note 5 L1037, L1047 | PASS |
| $5.0B revolver; $2.0B commercial paper | `10-Q` Note 5 L1085, L1099; `8-K 2025-06-06` L88 | PASS |
| Drizly Oct 2021; Transplace Nov 2021; Postmates intangibles fully amortized in 2022; Trendyol GO 85% $694M Jun 17 2025; SpotHero $617M Apr 16 2026; Getir ~$465M Jul 1 2026; Careem Technologies control Jul 30 2026 | `10-K-FY2023` Note 17 L4833/L4896, Item 7 L1659; `10-K-FY2025` Note 17 L4707–4709; `10-Q` Note 14 L1642, Note 15 L1666, Note 3 L939 | PASS (wording "by 2022" → "in 2022" fixed directly, see flag (f)) |
| Blacklane ~$550M by end 2026; Delivery Hero H2 2027 | `10-Q` Note 1 L659; Note 3 L929 / DH release p.3 L132 | PASS |
| Self-driving unit to Aurora Jan 2021; Yandex stake $703M Apr 21 2023; Careem non-rides to e& Dec 2023 | `10-K-FY2023` Note 13 L4469; `10-K-FY2025` Note 4 L3352; Note 18 L4755 | PASS |
| DH stake ~$4B for ~37%, incl. $1.6B of total return swaps | remarks p.8 L328–329; `10-Q` Note 2 L881 | PASS (see flag (d)) |

38/38 PASS.

### 3(h) outlook.md §1 indicator table (o:10–16) — every number

| Cell | Source | Result |
|---|---|---|
| 208M +16%; 3,867M +18% / 199M +17%; 3,643M +20% | Q2 release p.2 L49–50; Q1 release p.2 L49–50 | PASS ×8 |
| Mobility 28,988 +20%; Delivery 27,463 +25%; Freight 1,571 +25%; total 58,022 +22% cc (+24%) | Q2 release p.2 L74–77 | PASS ×9 |
| Q1: 26,394 +20%; 25,992 +23%; 1,334 +6%; 53,720 +21% cc (+25%) | Q1 release p.2 L73–76 | PASS ×9 |
| Expected "$56.25 billion to $57.75 billion ... 18% to 22%"; "roughly 2 percentage-point currency tailwind" | Q1 release p.1 L35–36 | PASS ×2 |
| Revenue Margin 25.4 / 19.1; 25.8 / 19.5 | deck p.16 L362–363; p.17 L399–401 | PASS ×4 |
| "roughly 400 bps" | Q1 remarks p.6 L229 | PASS |
| SOI margin 7.6 / 3.8; 7.7 / 3.7 (computed) | deck p.16–17; 2,029/26,394 = 7.69, 961/25,992 = 3.70 | PASS ×4 |
| EBITDA guided $2.70–2.80B, reported $2,819M; EPS guided $0.78–0.82, reported $0.81 | Q1 release p.1 L37–38; Q2 release p.2 L56, L59 | PASS ×4 |
| Reserves $13,286M; $387M; $830M / $12,904M; $443M | 3,758+9,528; release p.8 L316; 3,467+9,437; Q1 release p.8 L311 | PASS ×5 |
| FCF $2,792M / $10,116M; $2,286M / $9,799M | release p.13 L578; deck p.31 L1096–1099; Q1 release p.12 L547 | PASS ×4 |
| 2,050,225K; $518M; $12,723M (1,997 + 10,726) / 2,071,391K; $3,011M; $10,514M | release p.7 L288, p.8 L332, p.6 L249/257; Q1 release p.7 L280, p.8 L328, p.6 L216 | PASS ×8 |
| "$20 billion share repurchase authorization, which has $16 billion remaining" | Q1 remarks p.6 L255 | PASS |

59/59 PASS.

### 3(i) Prose sentences — 62 checks across both files

| # | Sentence / figure | Tag | Found | Result |
|---|---|---|---|---|
| 1 | "provide a vehicle to perform services on our platform" (b:6) | 10-K FY2025, Item 1A | L467 | PASS |
| 2 | "We generate substantially all of our revenue from fees paid by Drivers and Merchants" (b:6) | Item 7 | L1400 | PASS |
| 3 | 208M MAPCs, 3.9B trips, $58.0B, $14.2B (b:6) | release p.1–2 | L20–22, L49–52 | PASS |
| 4 | "a record 10.2 million drivers and couriers earned over $25 billion" (b:6) | remarks p.1 | L14 | PASS |
| 5 | 70 countries, 15,000 cities; founded 2009; NYSE May 2019; CEO since 2017 (b:8) | Item 1; Item 5; DEF 14A | L232/L259, L387; L1275 ("since May 10, 2019"); proxy L1273 | PASS |
| 6 | Operating losses $3.8B (2021), $1.8B (2022); $5.6B profit 2025; accumulated deficit $8.0B (b:8) | 10-K FY2023 Item 1A; 10-K FY2025 Item 8; 10-Q | L541; L2347 (5,565); L277 (7,950) | PASS |
| 7 | "is net of Driver and Merchant earnings and Driver incentives" (b:12) | Item 7 | L1400 | PASS |
| 8 | 'Uber never says "take rate" in its 10-K; its deck and 10-Q call this ratio "Revenue Margin"' (b:12) | deck p.16; 10-Q Item 2 | Byte-level regex `take\W{1,3}rate` over `10-K-FY2025.txt`: **zero hits** (the phrase appears only in the 10-Qs, Q2 L2946, Q1 L2658). "Revenue Margin" in the 10-Q is at L2510, which is **Item 1A**, not Item 2 | PASS on the fact; tag fixed directly (Item 2 → Item 1A). See "Withdrawn" below |
| 9 | "either a fixed percentage of the end-user fare or the difference..."; "a fixed percentage of the meal price" (b:12) | Note 1 | L2881; L2891 | PASS |
| 10 | "market-wide promotions which are recorded as a reduction of revenue" (b:12) | Note 1 | Only at **L2052, Item 7** (single occurrence in the file) | Tag imprecise; `[10-K FY2025, Item 7]` added directly |
| 11 | Advertising revenue and Freight booked gross (b:12) | Note 1 | L2915 ("Revenue is presented on a gross basis in the amount billed to Merchants and brands"); L2907 | PASS |
| 12 | UK gross from March 2022; Jan 2, 2026 change; "payments to drivers are recorded as a reduction of revenue instead of cost of revenue" (b:14) | Item 7; Note 14; 10-Q Item 2 | L2004 / L4584 (March 14, 2022); 10-Q L1742 | PASS |
| 13 | $1.1B off revenue; $808M off cost of revenue; about 8 points; ~21% (computed) (b:14) | 10-Q Item 2; release p.1–2 | L1928; L1942 ("$808 million decrease in Driver payments and incentives, as a result of Mobility business model changes in the UK"); release L22 ("8 percentage points"); (14,191+1,100)/12,651 = 1.209 | PASS |
| 14 | Mobility 57%, Delivery 33%, Freight 10% of 2025 revenue (b:38) | Note 13 | 29,670/52,017 = 57.0; 17,248/52,017 = 33.2; 5,099/52,017 = 9.8 | PASS |
| 15 | 'premium rides (Black, Reserve, Uber for Business, growing "40%+")' (b:38) | remarks p.2 | L50–51: "premium products including Reserve, Black, and Uber for Business (U4B) continued to outgrow the core business. **U4B** Gross Bookings grew 40%+ YoY" | **FAIL (precision)**: 40%+ is U4B alone. REVISE item 1 |
| 16 | Grocery & Retail "$15 billion in annualized Gross Bookings, growing roughly 40% YoY" (b:38, o:28) | remarks p.2 | L79 | PASS |
| 17 | Freight lost money at segment level every year but 2022 (b:38) | Note 13 ×2 | (130) / — / (64) / (74) / (33) | PASS |
| 18 | "certain insurance costs" (b:42); advertising $2.2B, promotions $1.6B in 2025; G&A carries legal accruals (b:42) | Item 7; Note 1 | L1408; L3003 ("Advertising expenses totaled ... $2.2 billion"; "Discounts, loyalty programs, promotions, refunds, and credits ... $1.6 billion"); L3007 | PASS |
| 19 | "we expect to commit over $10 billion of capital"; "we may need to incur additional debt to finance the purchase of autonomous vehicles"; P&E $1.8B (b:58) | remarks p.5; Item 1A; 10-Q Item 1 | L199; L877; L227 (1,809) | PASS |
| 20 | Captive insurer; reserve includes accidents not yet reported; $851M "primarily due to an increase in insurance rate per mile and miles driven"; total insurance cost not disclosed (b:60) | Note 1; Item 7 | L3033; L1810; no total insurance line anywhere in the income statement or notes | PASS |
| 21 | "significant recurring savings beginning in 2027"; reinvesting savings in lower prices (b:60) | remarks p.7; call p.5 | L300; L220–221 ("reinvesting the savings from insurance back into the market") and remarks L40 ("reinvesting insurance savings to improve affordability") | PASS |
| 22 | Segment measure change and 8-K description (b:70) | 8-K 2026-01-12, Item 8.01; 10-Q Note 10 | L77, L83; L1333 | PASS |
| 23 | FCF definition quote (b:95) | Item 7 | L1937 | PASS |
| 24 | "$9.8 billion in 2025 and passed $10 billion ... 'the first time we have exceeded the $10 billion mark'" (b:110) | Item 7; remarks p.7 | L1949 (9,763); L311 | PASS |
| 25 | About a quarter of 2025 OCF was insurance reserves growing ($2.7B of $10.1B) (b:110) | Item 8 | 2,660/10,099 = 26.3% | PASS |
| 26 | $6.4B 2024 release; $5.0B Netherlands 2025; ~$3.5B and ~$5.1B without them (b:112) | Item 7; Note 11 | L1748; L1390/L4187; 9,856−6,400 = 3,456; 10,053−5,000 = 5,053 | PASS |
| 27 | "Stakes in Aurora, Didi, Grab, Delivery Hero and others are marked to market ... each quarter"; $1.5B loss Q1, $1.6B gain Q2, about half of pre-tax profit (b:112) | Q1 release p.2; 10-Q Item 2 | Q1 L62; 10-Q L1732; 1.6/3.277 = 49%. But 10-Q Note 3 L923: Delivery Hero "prospectively transitioned to the equity method of accounting during the period"; the $1.1B Q2 gain was recognized "immediately prior to this transition" | **FAIL (precision)** on Delivery Hero going forward. REVISE item 2 |
| 28 | "GAAP Net Income may continue to see swings from quarter-to-quarter due to equity stakes on our balance sheet" (b:112) | remarks p.7 | L308 | PASS |
| 29 | $5.6B operating profit on $1.9B P&E; $9.5B restricted investments pledged as insurance collateral (b:114) | Item 8; 10-Q Item 1; Note 1 | L2347, L2270 (1,897); 10-Q L221 (9,486); L2823 ("held in trust accounts ... pursuant to certain contracts with insurance providers") | PASS |
| 30 | $5.4B unrestricted cash; "marked at $12.5 billion"; $12.6B debt (b:114) | release p.1; remarks p.8; 10-Q Item 1A | L33; L323; L2854 | PASS |
| 31 | "network scale and liquidity"; "the low switching costs between competitor platforms" (b:118) | Item 1A | L269 is **Item 1**; L537 is Item 1A | Tag imprecise; `[10-K FY2025, Item 1]` added directly |
| 32 | "Only 30% of our US gross bookings and 25% of our profits are coming from the top 20 cities" (b:118) | call p.14 | L722 | PASS |
| 33 | "over three times the Gross Bookings"; "one in five eligible consumers" (b:120) | Item 1 | L269 | PASS |
| 34 | Uber One members "spend three times more" (b:120) | Q1 call p.6 | L250 (p.6); also L162 (p.4) | PASS |
| 35 | MAPC +16%, trips per user +2%; Brazil "the cost of securing that supply has gone up pretty significantly", two points of trips growth (b:122) | release p.1; call p.7; remarks p.6 | L21; L315–316; remarks L245 ("The 2 point moderation in our YoY Trips growth was entirely attributable to Brazil") | PASS |
| 36 | AV risk-factor quotes incl. the elided Waymo sentence (b:128) | Item 1A | L561: "...on its own platform in addition to a fleet of autonomous vehicles that it makes available through our platform" — the ellipsis drops "of autonomous vehicles that it makes"; no meaning changed | PASS (flag (e)) |
| 37 | "the world's leading commercialization platform for autonomous vehicles"; "AVs will change how trips are supplied, but not how demand is aggregated" (b:128) | call p.3; AV spotlight p.7 | L114–115; L197 (PDF p.7) | PASS |
| 38 | SF, LA, Phoenix "Uber's category share ... is higher today than it was a year ago"; robotaxis "less than 0.5% of our overall trip volume" (b:128) | remarks p.6; call p.7 | L231–232; L336 | PASS |
| 39 | Partners "Waymo, Nuro with Lucid, Zoox, Wayve, Rivian, NVIDIA and Waabi"; "approximately 120,000 vehicles"; 7 live, 8 launching (b:128) | call p.4; remarks p.5; deck p.8 | Nuro/Lucid/Zoox/Wayve L150, Rivian/NVIDIA L155–157, Waymo L327; 120,000 remarks L216; deck L168 ("7 live cities \| 8 cities launching by end of 2026"). **Waabi appears in none of the three** (only Q1 remarks p.5 L181 and AV spotlight p.7 L186) | Tag missing for one name; `[Q1 2026 remarks, p.5]` added directly |
| 40 | Waymo Austin/Atlanta "We believe we'll continue to operate next year in those marketplaces"; profit drag "which the CFO declined to size" (b:128) | call p.7; p.10 | L327–328; L495–497: "we will give you more visibility into that as we go. The closer we get to deployment and scale out, there will be a P&L impact and we'll size that for investors clearly" | Quote PASS; "declined to size" overstates (REVISE item 4) |
| 41 | Mobility 68% of segment profit; US & Canada about half of revenue (b:128) | release p.3; Note 13 | 2,215/(2,215+1,055−24) = 68.2%; 26,469/52,017 = 50.9% | PASS (flag (b)) |
| 42 | Driver-classification quotes; Prop 22; AG case "remains ongoing"; "more than 150,000 Drivers"; New Zealand Nov 2025 four drivers; Mexico Dec 2024 bill (b:130) | Item 1A; Note 14; 10-Q Item 1A | L467, L475, L473; L4538; L469; L481 (both facts, same sentence in 10-Q L2466) | PASS |
| 43 | Accruals $1.8B not itemized; legal add-back $1.1B (2024), $141M (Q2 2026) (b:130) | 10-Q Note 11; Note 13; release p.12 | L1516; FY2025 Note 13 L4405 (1,123); release L501 | PASS |
| 44 | Reserves +164%, GB +68% (b:132) | computed | 12,463/4,720 = 2.64; 193,454/115,395 = 1.68 | PASS |
| 45 | "mass tort"; insurance "is higher" in US & Canada (b:132) | 10-Q Note 11; Item 1A | L1584; L1063 | PASS |
| 46 | Fee-cap quote; "blocked, capped, or suspended" in six countries incl. Germany, Italy, Spain; rivals lists (b:134) | 10-Q Item 1A; Item 1A; Item 1 | L2946; L961 (Argentina, Germany, Italy, Japan, South Korea, Spain = six); L285, L287 | PASS |
| 47 | €41.50; $14.8B / $13.7B; ~37% for ~$4B; €14.2B bridge; "Closing is expected in the second half of 2027"; €700M / €200M fees; 50 markets $42B; "over $1.2 billion"; "below two times" (b:136) | DH release p.1, p.3; remarks p.8; 8-K Item 1.01; DH release p.2; DH presentation p.11 | L3–4, L20–21; L132; remarks L328–329; 8-K L174, L149–156 (€700M tied to regulatory-approval conditions); DH release L37; presentation L295–297 ("Annualized synergies of over / $1.2 billion within 18 months"); remarks L336 | PASS |
| 48 | VAT ~$1.8B for 2022–2024, paid, receivable pending appeal; no customer concentration, "highly fragmented" (b:138) | 10-Q Note 11; Note 1; Item 1 | L1576–1578 (March 2022 to September 2024); L281 | PASS |
| 49 | Khosrowshahi 56; Macdonald 41 President & COO June 2025 over Mobility, Delivery, Autonomous as SVP Delivery left; Krishnamurthy 41 CFO Feb 16 2026; Mahendra-Rajah since Nov 2023, quotes; Hazelbaker May 2026 as CPO left; ten directors, chair Sugar; ~34,000 employees (b:142) | 8-Ks; DEF 14A; Item 1 | proxy L2023; 8-K 2025-06-02 L85–86, L101–103; 8-K 2026-02-04 L73, L75, L83; **"joining the Company in November 2023" is at proxy L2972 (CD&A), not "Executive Officers"**; 8-K 2026-05-11 L95–99; proxy L458 ("ten directors"), L1361; L341 | PASS on facts; `[DEF 14A 2026, CD&A]` added directly |
| 50 | One class, one vote; Vanguard 9.34%, BlackRock 6.82%, Capital Research 5.78%, PIF 3.57% with board seat; officers and directors ex-PIF ~0.25% (b:144) | Note 10; Security Ownership | L3874 (only common stock outstanding); **"Each share of Company stock gets one vote" is proxy L4508 (Additional Information)**; L4226, L4222, L4224, L4200 (Alnowaiser, PIF director); (77,878,487 − 72,846,072)/2,036,824,858 = 0.247% | PASS on facts; proxy tag added directly |
| 51 | CEO pay $35.6M, 96% variable; 2025 bonus on GB, Adj. EBITDA, Adj. EBITDA less SBC plus "insurance savings"; 2026 Non-GAAP EPS replaces EBITDA; PRSUs 45/45/10 (b:144) | CD&A; Looking Ahead to 2026 | L4051 ($35,595,826); L2617; L2742, L2829 ("Insurance savings" strategic goal); L2379–2384; L887 (safety 10%) | PASS |
| 52 | Cash priorities quote; "about 50% of our free cash flows towards buybacks"; "durably reducing our share count"; no dividend ever (b:146) | Q1 remarks p.6; call p.12; remarks p.8; Item 5 | L266; L622; L343; L1279 | PASS |
| 53 | o:20 CEO quotes p.3 | call p.3 | L87–89, L100 | PASS ("names three pillars" is the writer's framing; REVISE item 4) |
| 54 | o:22 "about 4 of the 5 points"; "an optical impact"; "deliberate investments ... in our lower-cost offerings" | call p.11 | L540–545 ("nearly 500 basis points ... about 400 basis points") | PASS |
| 55 | o:22 AV vision quotes | remarks p.5 | L182, L191 | PASS |
| 56 | o:26 US trips and bookings "accelerated"; "~1.5x faster than denser markets" | remarks p.1, p.2 | L38; L61 | PASS |
| 57 | o:28 Getir closed in July; Trendyol GO lapping quotes | remarks p.8; call p.15 | L354–356; L786–789 | PASS |
| 58 | o:30 Uber One 50M in April "up 50% YoY"; "more than 70% of Delivery Gross Bookings, up roughly 20 percentage points" | Q1 remarks p.4; remarks p.3 | L142; L127 | PASS |
| 59 | o:32 advertising run-rate quote | remarks p.4 | L139 | PASS |
| 60 | o:36 Freight quotes and $24M loss | remarks p.3; release p.3 | L111; L110 | PASS |
| 61 | o:38 "across all 10 of our largest international markets"; 99 markets | remarks p.2; DH release p.1 | L73; L17 | PASS |
| 62 | o:67 claim 11 source sentence | 10-Q Item 2 | L2272 ("We expect to enter into term loan facilities that will reduce the commitments under the bridge credit agreement in the third quarter of 2026") | PASS |

**Citation tally:** 30 + 42 + 42 + 15 + 51 + 48 + 38 + 59 = 325 table cells, plus 62 prose checks and 109 quoted strings (§4) = **496 checks. 494 PASS on the facts (six of them carried an imprecise tag, fixed directly: items 8, 10, 31, 39, 49, 50), 2 FAIL (precision, items 15 and 27).** No tag points to a wrong document; no number is wrong. Neither FAIL came from a gatherer note: `notes-transcript.md` and `notes-filings.md` were not consulted for either sentence.

---

## 4. Verbatim-quote check

Every string inside double quotes in both files (109 distinct strings of three words or more; 53 in business.md, 56 in outlook.md) was searched in all cached texts after normalizing whitespace, curly/straight quotes, dash variants and zero-width spaces (`/tmp/uber-orch/reviewer/quotes.py`). Ellipsis quotes were split and each fragment required in the same file.

| Where | Strings | Exact match | Notes |
|---|---|---|---|
| business.md (all sections) | 53 | 53 | Includes the two-fragment Waymo quote (10-K FY2025 L561, both fragments in one sentence, order preserved), the two-fragment "Uber's category share ... is higher today" (remarks L231–232) and the fee-cap quote (10-Q L2946) |
| outlook.md §1–§3 | 29 | 29 | |
| outlook.md §4 guidance (8 bullets) | 12 | 12 | The Q3 bullet stitches four release bullets (p.1 L36–39) into one quoted paragraph; every sentence is verbatim and in order, the bullet/sub-bullet marks are dropped. The full-year tax bullet drops the footnote marker "1" after "single digits." (remarks L370). Both acceptable; noted here so the refresh agent is not surprised |
| outlook.md §5 claim quotes (11 claims, 13 strings) | 13 | 13 | Claim 8's "Accrued insurance reserves" is the cash-flow line label (release p.8 L316) |
| Curly vs straight | — | — | The drafts use straight quotes throughout; sources use curly apostrophes in "we've", "Uber's", "we'll" (call L150, L722, L328, L678) and the remarks' "Uber's" (L231). Straight-for-curly only; no word differs |

No altered word found in any quote.

---

## 5. Claims check (outlook.md §5)

Count: **11** (target 6–12). Mix: claims 1–2 are headline guidance; 3–11 are fundamentals (segment growth, Revenue Margin, Delivery margin, AV cities, Zoox launch, insurance add-back, buybacks, share count, bridge refinancing). Balance is right. Every claim carries its verbatim quote and tag on the same line.

| # | Single direction? | Can it fail? | One thing to check? | Quote supports it? | Sharpening / disclosure labels | Tied to indicator | Verdict |
|---|---|---|---|---|---|---|---|
| 1 | Yes (in range) | Yes | Yes | Yes (release p.1) | n/a | 2 | OK |
| 2 | Yes | Yes | Yes | Yes | n/a | — | OK |
| 3 | Yes (≥20% cc) | Yes | Yes | Loosely: management spoke of the US accelerating, the claim is global Mobility cc growth | Labelled "our sharpening, not management's number" | 2 | OK; the label carries the leap from US to global |
| 4 | Yes (24.4–26.4%) | Yes | Yes | Yes ("roughly the same magnitude") | Labelled | 3 | OK; ±1 point around Q2's 25.4% is a reasonable reading of "roughly the same" |
| 5 | Yes (≥3.8%) | Yes | Yes | Yes ("becoming more profitable") | Labelled | 4 | OK |
| 6 | Yes (≥10 cities stated) | Yes | Yes | Yes (7 → "as many as 15") | Labelled | — | OK |
| 7 | Yes | Yes | Yes (Zoox carrying Uber riders in Las Vegas) | Yes (Q1 remarks "starting in Las Vegas in Q3"; Q2 call "Zoox coming in Vegas") | n/a | — | OK |
| 8 | Yes (nine-month add-back below prior year) | Yes | Yes | Yes ("becoming a tailwind this year") | Labelled "Disclosure check, year-to-date column" | 5 | OK; the Q3 10-Q cash-flow statement carries nine-month columns |
| 9 | Yes (> $518M) | Yes | Yes (release p.8 three-month column) | Yes | n/a | 7 | OK; states the basis figure (cash-flow $518M, not Note 7's $510M) |
| 10 | Yes (< 2,050,225K) | Yes | Yes | Yes | n/a | 7 | OK |
| 11 | Yes (term loans reported) | Yes (no term loans, or bridge unchanged, = missed) | Yes | Yes (10-Q L2272) | Labelled "Disclosure check"; an event, so no quarter/YTD column applies | 7 | OK |

No either/or constructions, no double-barreled claims, no vague statements presented as claims. Grading next quarter is mechanical for all 11. Rubric Q4 passes. One optional note: o:55 "Q3 2026 results are due around early November 2026" has no source; label it as the writer's expectation from past timing (REVISE item 7, optional).

---

## 6. Jargon audit

### (a) Terms found that were neither plain, name-inferable, nor in the glossary — and what was done

| File:line (pre-edit) | Term | Status |
|---|---|---|
| business.md:19 | "Uber Direct" | FIXED: "(deliveries run for merchants' own orders)" — 10-K Item 1 L246 calls it "our white-label Delivery-as-a-Service offering to retailers and restaurants" |
| business.md:49 | "D&A" in a table label | FIXED: "depreciation and amortization" |
| business.md:60 | "captive insurer"; "actuarial estimate" | FIXED: "(an insurance company it owns)"; "actuarial (statistical) estimate" |
| business.md:77 | "Corporate G&A and Platform R&D" | FIXED (first table): "(head-office and shared engineering costs)" |
| business.md:112 | "GAAP"; "marked to market" | FIXED: "(official accounting rules)"; "(revalued at the current share price)" |
| business.md:114 | "collateral" | FIXED: "(security for future claims)" |
| business.md:130 | "arbitration claims" | FIXED: "(private hearings instead of court)" |
| business.md:132 | "mass tort" (quote) | FIXED: gloss outside the quote |
| business.md:136 | "bridge loan"; "synergies"; "leverage" | FIXED: "(short-term borrowing to be replaced by longer-term debt)"; "(savings and extra sales from combining)"; "(debt relative to yearly earnings)" |
| business.md:138 | "VAT"; "receivable" | FIXED: "(sales tax)"; "(money Uber expects back)" |
| business.md:144 | "Non-GAAP EPS" | FIXED: "(Uber's adjusted earnings per share)" |
| business.md:146 | "investment grade" | FIXED: "(keep a credit rating lenders trust)" |
| business.md:155 | "revolver"; "commercial paper program" | FIXED: "(standing credit line)"; "(short-term borrowing notes)" |
| business.md:156 | "intangibles fully amortized" | FIXED: "acquired intangibles, the value assigned to its brand and customer lists, fully written off" |
| business.md:159 | "total return swaps" | FIXED: "(bank contracts paying Uber the gains or losses on Delivery Hero shares it does not own)" |
| business.md:171 | "Diluted weighted-average shares" | FIXED: one sentence added to indicator 7 |
| outlook.md:6 | "constant currency (cc)"; "YoY" | FIXED: "(cc; exchange-rate moves stripped out). YoY means year over year." |
| outlook.md:11 | "tailwind" (quote) | FIXED: "(a boost)" |
| outlook.md:12 | "400 bps" (quote) | FIXED: "(4 points)" |
| outlook.md:13 | "Non-GAAP EPS" | FIXED: "(adjusted earnings per share)" |
| outlook.md:20 | "operating leverage" (quote) | FIXED: "(profit growing faster than sales)" |
| outlook.md:28 | "lapping"; "organic" (quote) | FIXED: "(comparing against a year-ago quarter that already included it)"; "(organic: excluding acquisitions)" |
| outlook.md:32 | "run-rate" (quote) | FIXED: "(run-rate: the quarter's pace times four)" |
| outlook.md:45 | "ETR" (quote) | FIXED: "(ETR: effective tax rate)" |
| outlook.md:51 | "gross leverage"; "accretive"; "synergies" (quote) | FIXED: one bracket after the tag |

Already plain or glossed by the writer, no action: Gross Bookings, MAPCs, Revenue Margin, principal/agent, Adjusted EBITDA, Segment/Non-GAAP Operating Income (glossary); take rate (b:12, explained as the same ratio); gross margin and operating margin (b:42, b:44); cost of revenue (b:14, b:42); capex (table label); free cash flow (b:95); stock-based compensation (b:103 "pay in shares"); valuation allowance (b:112, explained inline); accumulated deficit (b:8); restricted investments (b:114); Proposition 22 (b:130, explained); liquidity (b:118, explained by the next sentence); "moat" (owner's own framework word). "Tender offer", "irrevocable" and "equity method" do not appear in either draft.

### (b) Glossary entries

Six entries (Gross Bookings, MAPCs, Revenue Margin, Principal vs agent accounting, Adjusted EBITDA, Segment Operating Income and Non-GAAP Operating Income). Each is one sentence, each is used repeatedly, none is avoidable given the measure break and the UK accounting flip. **None should be cut; none needs adding** after the inline glosses above.

### (c) Banned-word scan outside quotes

Scanned for leverage, synergy, headwind, tailwind, monetize, ecosystem, at scale, robust, unlock. "leverage" (b:136) and "synergies" (b:136) occur once each outside quotes, now glossed; "headwind"/"tailwind" occur only inside quotes (o:11, o:28, o:44, o:46, o:64); the others do not occur. Acceptable.

### (d) Paragraphs that are mostly numbers

b:14 (UK flip) carries five figures but each is explained; b:112 (GAAP swings) carries six; b:136 (Delivery Hero) carries eight, all in a deal paragraph. None is a wall; the §7 cash items are already a table.

---

## 7. Invented-number check

No figure was found without a source tag, and no tag fails to contain its figure. Specific checks:

| Item | Finding |
|---|---|
| Annual segment Gross Bookings FY2022–FY2025 | Computed by summing quarterly MD&A tables; labelled "(computed)"; every year reconciles to Uber's printed annual total. Correct (§3(b)). |
| Revenue Margins FY2022–FY2025 | Labelled computed; inputs sourced; re-derived. Correct. |
| Gross margin, four-line ratios, per-trip cost, operating margin, capex/revenue | All labelled computed; re-derived (§3(c)). |
| "Mobility is 68% of segment profit" | Labelled computed; base is the three segments' combined Segment Operating Income before corporate costs (2,215 / 3,246, 10-Q Note 10 L1362). Correct; the base could be named in the sentence (optional). |
| "US and Canada about half of revenue" | Labelled computed; 26,469 / 52,017 = 50.9% (Note 13 L4479). Correct. |
| Insurance reserves (computed sum) | Labelled; two balance-sheet lines, all five dates. Correct. |
| Reserves +164%, Gross Bookings +68% | Labelled computed; re-derived. Correct. |
| ~$3.5B and ~$5.1B net income without allowance releases | Labelled computed; re-derived. Correct. |
| ~21% revenue growth without the UK change | Labelled computed; (14,191 + 1,100)/12,651 = 20.9%. Correct. |
| Officers and directors ~0.25% | Labelled computed; re-derived from the proxy's group total less the PIF director's shares over the record-date share count. Correct. |
| 57% / 33% / 10% revenue mix | 57% labelled computed; 33% and 10% follow from the same table (Note 13). Acceptable. |
| Free cash flow FY2021 (743) | Labelled computed (Uber prints FCF from 2022). Correct. |
| "n/d" cells | FY2021 segment Gross Bookings and trips: absent from the cached filings (verified). FY2021 company Adjusted EBITDA: not printed but derivable as −774 from FY2023 Note 13 (REVISE item 6, optional). Jun 2026 Schedule II: no such schedule in a 10-Q. All defensible. |
| Unlabelled inferences | b:44 "Half does" (which costs scale per trip) is the writer's reading of the cost-of-revenue description; acceptable as analysis. b:38 "the filings give the mechanics but no reason for the gap" is a fair statement. o:55 "early November 2026" (REVISE item 7, optional). |
| Estimates presented as fact | None. "not disclosed" used correctly for total insurance cost (b:60) and itemized accruals (b:130). |

---

## 8. Company-specific coverage

- **(a) Marketplace-that-takes-a-cut vs operator:** §1 says Uber "does not own the cars and, in most places, does not employ the drivers"; §2 "The cut" walks a $20 fare; the glossary's principal/agent entry explains why revenue can move without profit moving. Yes.
- **(b) Take rate / Revenue Margin, and why revenue lagged Gross Bookings in 2026:** §2 defines Revenue Margin, gives the five-year series, and the "Why revenue grew 12% when Gross Bookings grew 24%" paragraph explains the UK gross-to-net flip with the $1.1B / $808M / 8-point figures; outlook §2 adds management's "about 4 of the 5 points" and "optical impact". Yes, and clear.
- **(c) Insurance, driver classification, AVs, each with an early warning:** §3 has an insurance paragraph and table; §6 scenarios 3, 2 and 1 respectively give what would have to happen, an early warning (reserve additions vs Mobility bookings and prior-year adjustments; the legal add-back and the $1.8B accrual; Waymo not renewing Austin/Atlanta and the first sized AV profit drag), and the exposure. Yes.
- **(d) Delivery Hero as pending only:** "has offered", "Closing is expected in the second half of 2027", "Pending" row in the §7 table, "the pending Delivery Hero offer" in outlook §3, break fees and bridge described as commitments not draws. Nothing treats the deal as done. Yes.

---

## 9. Writer's flagged uncertainties — rulings

| Flag | Ruling |
|---|---|
| (a) Annual segment Gross Bookings FY2022–FY2025 by summing quarterly MD&A tables | **Verified and correct.** Sums reconcile to Uber's printed annual totals to the million in all four years (§3(b)). Keep the "(computed)" label. |
| (b) "Mobility is 68% of segment profit" base (2,215 / 3,246) | **Verified.** 3,246 is the three segments' combined Segment Operating Income before corporate costs (10-Q Note 10 L1362; release p.3 prints the three components). Optional: say "of the three segments' combined operating income, before corporate costs". |
| (c) Schedule II roll-forward mixing FY2023 and FY2025 10-K bases | **Acceptable.** Additions and deductions for 2023 are identical in both filings (3,544; 1,526); only the balances differ, because the FY2025 schedule adds an "Other" column for reserves with a matching insurer recoverable (footnote (4) L4817). The table's balance row uses the balance-sheet sums throughout, so it is on one basis; the footnote at b:68 says so. No change needed. |
| (d) Delivery Hero stake: "~$4 billion for ~37% economic interest" (remarks) vs 24.99% + total return swaps (10-Q) | **Consistent.** 10-Q Note 3 L923: $2.3B in Q2 took direct ownership to 24.99%; Note 2 L881: $1.6B of total return swaps on Delivery Hero stock; DH release p.3 L128–129: 24.77% directly plus 11.74% "through equity derivatives" = 36.5% ≈ "roughly 37%". $2.3B + $1.6B ≈ $4B. Optional one-clause reconciliation (REVISE item 5). |
| (e) §6 item 1 Waymo quotes with an ellipsis; the untagged framing sentence | **Verified.** The ellipsis drops "of autonomous vehicles that it makes" (L561), meaning unchanged. The untagged sentence "What would have to happen: a maker of self-driving cars reaches scale..." is the writer's scenario statement, not a fact, and needs no tag under §3 rule 2. |
| (f) Postmates intangibles statement | **Verified**: FY2023 10-K Item 7 L1659, "acquired Postmates intangible assets being fully amortized in 2022". The table said "by 2022"; changed to "in 2022" and de-jargoned (see "Fixed directly"). |

---

## 10. Verdict: REVISE

Items 1–2 are factual precision; 3–4 are wording that overstates the source; 5–7 are optional.

1. **business.md:38 (§2)** — "premium rides (Black, Reserve, Uber for Business, growing '40%+')" attaches the growth figure to three products. Remarks p.2 L50–51 give "40%+" for U4B (Uber for Business) alone; the three together "continued to outgrow the core business". Reword so only Uber for Business carries the 40%+.
2. **business.md:112 (§4)** — "Stakes in Aurora, Didi, Grab, Delivery Hero and others are marked to market through the income statement each quarter." From Q2 2026 the Delivery Hero shares are on the equity method (10-Q Note 3 L923: "prospectively transitioned to the equity method of accounting during the period"; the $1.1B Q2 gain was booked "immediately prior to this transition"), so only the $1.6B of total return swaps (Note 2 L881) will keep swinging. Add a clause, because the reader will otherwise expect a Delivery Hero mark every quarter and the refresh agent will look for one.
3. **business.md:30 (§2 table)** — row label "Freight Gross Bookings ($B; equals Freight revenue)": the summed quarterly bookings differ from Freight revenue by a few million in every period shown (6,952 vs 6,947; 5,242 vs 5,245; 5,135 vs 5,141; 5,093 vs 5,099; 1,571 vs 1,583). Say "roughly equals" or drop the clause.
4. **business.md:128 (§6 item 1) and outlook.md:20 (§2)** — "which the CFO declined to size": transcript p.10 L495–497 has the CFO saying "we will give you more visibility into that as we go ... we'll size that for investors clearly as we've historically done"; "has not yet sized" is what was said. "The CEO names three pillars": the CEO did not enumerate pillars (call p.3 L87–115); "The CEO's opening covers three things" or similar.
5. *(optional)* **business.md:136 or :159** — one clause reconciling the 37% to the 10-Q: about 25% held directly (24.99%, 10-Q Note 3) plus about 12% through swaps (11.74%, Delivery Hero release p.3). The numbers are verified above; the writer chooses where.
6. *(optional)* **business.md:78 (§3 old-measure table)** — FY2021 company Adjusted EBITDA is "n/d". It is not printed, but the FY2023 10-K Note 13 (L4501, L4505) gives Total Segment Adjusted EBITDA 1,107 and Corporate G&A and Platform R&D (1,881), which by Uber's own reconciliation is −774. Either compute it with a "(computed)" label or keep n/d; the writer's choice.
7. *(optional)* **outlook.md:55** — "Q3 2026 results are due around early November 2026" has no source; label as the writer's expectation from past reporting dates.

Length constraint for cycle 2: outlook.md is at 1,180 prose words; items 4 and 7 must be word-neutral or shorter. business.md is at 2,661 and has room.

---

## Fixed directly

Tags (source unambiguous, verified; no number or quote changed):
- business.md:12 — `[10-Q Q2 2026, Item 2]` → `[10-Q Q2 2026, Item 1A]` for "Revenue Margin" (10-Q L2510 is in Part II Item 1A, L2378–3186).
- business.md:12 — added `[10-K FY2025, Item 7]` after "advertising and Freight are booked gross" (the "market-wide promotions" quote is at L2052, Item 7; Note 1 does not contain it).
- business.md:118 — added `[10-K FY2025, Item 1]` alongside Item 1A ("network scale and liquidity" is at L269, Item 1).
- business.md:128 — added `[Q1 2026 remarks, p.5]` to the AV-partners sentence (Waabi appears at Q1 remarks L181, p.5, and nowhere in the three tags given).
- business.md:142 — added `[DEF 14A 2026, CD&A]` (Mahendra-Rajah "joining the Company in November 2023", proxy L2972).
- business.md:144 — added `[DEF 14A 2026, Additional Information]` ("Each share of Company stock gets one vote", proxy L4508; Note 10 supports "one class" only).

Wording (jargon glosses, meaning unchanged; no numbers, quotes, claims, indicators or structure touched) — the full list is in §6(a) above. Before/after for the three that touch a fact's phrasing:
- business.md:156 — "Postmates (intangibles fully amortized by 2022)" → "Postmates (acquired intangibles, the value assigned to its brand and customer lists, fully written off in 2022)" (FY2023 10-K L1659: "fully amortized in 2022").
- business.md:189 (Sources) — "CD&A = Compensation Discussion and Analysis" → "CD&A = Compensation Discussion & Analysis" (the printed heading, proxy L121).
- outlook.md:6 — "Growth rates are reported unless marked constant currency (cc)." → "Growth rates are reported unless marked constant currency (cc; exchange-rate moves stripped out). YoY means year over year."

No typos found. All 109 quoted strings re-verified after the edits (106 exact by script; the stitched Q3 guidance bullet, the tax bullet without its footnote marker, and one string adjacent to another quote were re-read by hand and are exact).

Word counts after fixes (`/tmp/uber-orch/wc_prose.py`, §3 rule 7 basis): **business.md 2,661** (target 2,000–3,000), **outlook.md 1,180** (target 800–1,200; 20 words of headroom).

**As-of check:** no information dated after 2026-08-05 found. Dates that appear (Getir closed July 1, Careem control July 30, the Delivery Hero agreement July 16, closing "second half of 2027", integration in 2028–2029, insurance savings "beginning in 2027", Blacklane "by the end of 2026") are all in the cached 10-Q, 8-K, remarks or call. "Early November 2026" is the writer's expectation (REVISE item 7).

**Withdrawn findings (with evidence):**
- *"Uber never says 'take rate' in its 10-K" looked false* because my quote checker listed `10-K-FY2025.txt L969` beside the fee-cap quote. That hit was for the first fragment ("have proposed delivery network fee caps") only; the second fragment ("and caps on take rate or surge pricing") was found only in `10-Q-2026-Q1.txt` L2658 and `10-Q-2026-Q2.txt` L2946. A byte-level regex `take\W{1,3}rate` over `10-K-FY2025.txt` returns zero matches. The sentence stands; the writer correctly tagged the quote to the 10-Q.
- *DH presentation p.11 tag for "over $1.2 billion" looked wrong* (the only same-line hit was p.3 L56). Reading p.11 (L295–297): "Annualized synergies of over / $1.2 billion within 18 months / of closing" — the phrase spans a line break. Tag correct.
- *"spend three times more" [Q1 2026 call, p.6] looked mis-paged* (first hit L162, p.4). A second occurrence is at L250, p.6 ("where they spend three times more than others"). Tag correct.
- *Two guidance quotes failed the script* (Q3 outlook; full-year tax). Manual read: the first stitches four verbatim bullets from release p.1 L36–39; the second is verbatim except the dropped footnote marker "1" (remarks L370). Both accepted.


---

## Cycle 2 (re-check of the writer's second pass, 2026-09-08)

_Same as-of rule observed: nothing outside `sources/2026-Q2/` was opened. Line numbers refer to the revised drafts and the cached `.txt` files. This is the second and last review cycle allowed by AGENTS.md §13._

### 1. REVISE list — resolution

| # | Item | Writer's change | Verified against | Status |
|---|---|---|---|---|
| 1 | 40%+ attached to three products | b:38 now: 'premium rides (Reserve, Black and Uber for Business, which together "continued to outgrow the core business", Uber for Business alone growing "40%+")' | Remarks p.2 L49–51: "higher-value products including Reserve, Black, and Uber for Business (U4B) continued to outgrow the core business. U4B Gross Bookings grew 40%+ YoY" — both quotes verbatim | Resolved |
| 2 | Delivery Hero "marked to market each quarter" | b:112: Delivery Hero removed from the marked-to-market list; new sentence: the Q2 gain "included $1.1 billion on the Delivery Hero shares, booked just before the stake 'prospectively transitioned to the equity method of accounting' (Uber now records its share of Delivery Hero's profit or loss, not the share price); only the $1.6 billion of total return swaps on Delivery Hero stock still move with the price" [Note 3] [Note 2] | 10-Q Note 3 L923 (quote verbatim; "$1.1 billion ... immediately prior to this transition"); Note 2 L881 ("TRS agreements for $1.6 billion ... accounted for the TRS at fair value, with changes in fair value recognized in other income (expense), net"). The gloss is a correct plain statement of the equity method | Resolved |
| 3 | "equals Freight revenue" | b:30: "roughly equals Freight revenue" | Figures as in §3(b) above | Resolved |
| 4 | "declined to size"; "names three pillars" | b:128: 'which the CFO has not yet sized ("we'll size that for investors clearly as we've historically done")' [Q2 2026 call, p.10]; o:20: "The CEO covers three things:" | Transcript p.10 L496–497, verbatim (source has curly apostrophes, draft straight) | Resolved |
| 5 (optional) | 37% vs 24.99% reconciliation | b:159: "about 25% owned directly (24.99% at June 30) plus about 12% of exposure (11.74%) through $1.6B of total return swaps" with tags [Q2 2026 remarks, p.8] [10-Q Q2 2026, Note 3] [10-Q Q2 2026, Note 2] [Delivery Hero release, p.3] | Note 3 L923 (24.99%); DH release p.3 L128–129 ("approximately 11.74% through equity derivatives"); Note 2 L881 ($1.6B); 24.99 + 11.74 = 36.73 ≈ "roughly 37%" (remarks L329). The 11.74% is as of the 2026-07-16 announcement and the $1.6B as of June 30; both pre-cutoff, difference immaterial | Resolved |
| 6 (optional) | FY2021 company Adjusted EBITDA "n/d" | b:78–79: "(774) (computed)" and "(0.9)%"; caption b:91 explains the subtraction and that it reproduces the printed 2022 and 2023 figures [10-K FY2023, Note 13] | FY2023 10-K Note 13 L4501 "Total Segment Adjusted EBITDA \| 1,107 \| 3,850 \| 6,405" and L4505 "Corporate G&A and Platform R&D (2) \| ( 1,881 ) \| ( 2,137 ) \| ( 2,353 )". 1,107 − 1,881 = −774; 3,850 − 2,137 = 1,713 and 6,405 − 2,353 = 4,052 match Item 7 L1845. −774 / 90,415 = −0.856% → (0.9)%. The 90,415 denominator is sourced in the §2 table (b:31, b:36 [DEF 14A 2026, Pay Versus Performance], proxy L4059); I added the same tag to the §3 caption so the ratio row is self-contained | Resolved (one tag added directly) |
| 7 (optional) | Unsourced "early November 2026" | o:55: "We expect Q3 2026 results in early November, judging by past report dates." | Labelled as the writer's expectation; no year, no source needed | Resolved |

The writer also made three trims in outlook §1–§3 ("not yet locked" → "not locked"; "comes from" → "is from"; "The frame is scale turning into cash" → "Scale turning into cash"; "the live-city count, and whether" → "the live-city count; whether"). No fact, number or quote was removed: the verbatim-quote scan finds the same 56 outlook strings as in cycle 1, all matched.

### 2. Re-checks

- **Verbatim quotes:** 109 → 112 distinct strings (three new: "continued to outgrow the core business" remarks L50; "prospectively transitioned to the equity method of accounting" 10-Q L923; "we'll size that for investors clearly as we've historically done" transcript L496–497). All matched by `quotes.py` except the same three script artifacts as cycle 1 (stitched Q3 guidance bullets, dropped footnote marker, one string adjacent to another quote), re-read by hand and exact.
- **Cycle-1 direct edits:** all 36 spot-checked by exact string (22 in business.md, 10 in outlook.md, plus the two Sources-line and table-label edits): every one present exactly once.
- **Tags vs Sources lists:** every tag family used is mapped and none is unused, both files (programmatic check). No new tag family was introduced.
- **Skeleton:** all §6/§7 headings present in order; `_Proposed — owner to review and lock._` present; no §6 Tone shift in outlook; glossary unchanged (six one-sentence entries).
- **Measure break:** the old-measure table still stops at FY2025 and the new-measure table still starts at Q2 2025 / Q1 2026; nothing crosses.
- **As-of:** no date after 2026-08-05 appears; the new §5 intro carries no year.
- **Length** (`/tmp/uber-orch/wc_prose.py`): **business.md 2,768** (writer reported 2,760 before my one-tag caption addition; target 2,000–3,000), **outlook.md 1,179** (target 800–1,200).

### 3. Rubric (§14), re-run briefly

1. What they do and who pays — **Yes** (§1 unchanged).
2. What would kill it and the early warning — **Yes**; §6 item 1's early warning now reads accurately ("has not yet sized").
3. Why the margins are what they are and whether cost scales — **Yes**; the FY2021 Adjusted EBITDA cell now completes the five-year margin series.
4. Predict next quarter's scorecard from §5 alone — **Yes**; the 11 claims are unchanged.
5. Nothing requiring knowledge the reader lacks — **Yes**; the new equity-method sentence carries its own plain gloss.

### 4. Fixed directly in cycle 2

- business.md:91 (§3 old-measure caption) — added "; the Gross Bookings denominators are the §2 totals [DEF 14A 2026, Pay Versus Performance]" so the (0.9)% ratio's FY2021 denominator is tagged where it is used.

### 5. Open items for the owner

None that block PASS. For the indicator lock: indicator 7 bundles three figures (diluted shares, buybacks, total debt) in one cell; consider splitting into share count/buybacks and total debt when locking, as the scorecard time series will be easier to read. The six proposed glossary terms and seven indicators await the owner's review per §8.

**Verdict after cycle 2: PASS.**
