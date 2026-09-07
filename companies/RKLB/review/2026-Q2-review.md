# Rocket Lab Corporation (RKLB) — Reviewer report, Q2 2026 (three months ended 2026-06-30)

_Reviewed 2026-09-07 against `sources/2026-Q2/` only (cutoff 2026-08-10). No other folder exists and no outside knowledge was used. Files reviewed: `business.md` (2,965 prose words before fixes), `outlook.md` (1,197 prose words before fixes). First run: no scorecard, no blind re-grade. Line numbers below refer to the drafts (unchanged by the reviewer's edits; both files kept their line count) and to the cached `.txt` files._

**Verdict: REVISE.** Citation spot-check: 96 items checked, 92 PASS, 4 FAIL, 0 UNVERIFIABLE. Every number in the §2, §3 and §4 tables and the outlook §1 table is right, every quote in outlook §4 and §5 is verbatim, and the Iridium deal is consistently described as pending. What fails is one "not disclosed" that is disclosed (government-revenue share for 2021–2022 is in the FY2023 10-K), one set of program figures attributed to two programs when the source gives them for one (SDA Tranche 3), one inference written as fact (revenue lost "waiting for FAA clearance"), and one indicator anchored to the wrong 10-Q note. A handful of wording imprecisions and two files slightly over length (after the reviewer's glosses) round out the list.

---

## 1. Skeleton compliance

**business.md**

| Requirement (§6) | Result |
|---|---|
| `# <Company> — The Business` | OK |
| `_As of <QLABEL>. Written <date>._` | OK: "As of Q2 2026. Written 2026-09-07." Fiscal year = calendar year, so no parenthetical is needed (§5) |
| §1–§8 headings, in order, none skipped | OK. §1 has the history paragraph; §3 adds a permitted company-specific subsection ("### Neutron"); §6 carries customer concentration (#2); §8 has name / why / where |
| §2 segment table, 5 fiscal years | OK: FY2021–FY2025 plus Q2 2026 and 6M 2026, with the FY2021–FY2022 columns from `10-K-FY2023.txt` and FY2023–FY2025 from `10-K-FY2025.txt`, as the footnote states |
| §3 table: revenue, gross margin, operating margin, capex, capex/revenue, 5 years | OK, plus segment gross margins, R&D and SG&A |
| §4 table, 5 years | OK (plus 6M 2026) |
| §8 marked `_Proposed — owner to review and lock._` | OK (line 131) |
| Glossary | OK: 11 one-sentence entries, all used in the text |
| Sources table maps every tag prefix used | OK. Tags used: 10-K FY2025, 10-Q Q2 2026, 10-K FY2023, Q2 2026 call, DEF 14A 2026, Q2 2026 release, Q2 2026 slides, Iridium deck 2026-06-29, 8-K 2026-06-29, 8-K 2026-03-30, Q1 2026 release (11). Table rows: the same 11. No orphan tag, no unused row. (The two `[s]` hits from a grep are the bracketed letters inside the quote "design[s] and manufacture[s]" at line 84, not tags.) |
| Length 2,000–3,000 prose words | 2,965 before fixes (in range, upper edge); **3,069 after the reviewer's glosses** (see §9) |

**outlook.md**

| Requirement (§7) | Result |
|---|---|
| `# <Company> — Outlook as of <QLABEL>` | OK |
| `_Transcript source tier: … Written <date>._` | OK: "third-party (The Motley Fool)"; matches MANIFEST tier 3. The Sources row discloses the page-publication date (2026-08-17) and the garble list |
| §1 table: one row per proposed indicator; columns this quarter / last quarter / what management said | OK: 8 rows matching business.md §8; one comparison value per cell; year-ago figures kept in a sentence under the table |
| §2, §3, §4 (verbatim guidance), §5 | OK. §4 quotes the release's eight guidance bullets word for word and notes the transcript garble ("second quarter") |
| §6 Tone shift omitted on first run | OK, omitted |
| Sources table maps every tag prefix used | OK: Q2 2026 call, Q2 2026 release, Q1 2026 release, Q2 2026 slides, Iridium deck 2026-06-29, 10-Q Q2 2026, 10-K FY2025 (7 used, 7 mapped) |
| Length 800–1,200 prose words | 1,197 before fixes; **1,226 after glosses** (see §9) |

---

## 2. Citation spot-check

Legend: PASS / FAIL / UNVERIFIABLE. Source figures are in $ thousands unless shown otherwise; the draft converts to $ millions. Every "(computed)" cell was recomputed. Line numbers refer to the cached `.txt` files.

### 2a. business.md §2 segment table (every cell, lines 16–24)

| # | Cell(s) | Tag | Found at | Result |
|---|---|---|---|---|
| A1 | Launch FY2021 39.0 / FY2022 60.7 | [10-K FY2023, Note 20] | 10-K-FY2023.txt line 4626: 38,971 / 60,686 | PASS |
| A2 | Space Systems FY2021 23.3 / FY2022 150.3 | same | line 4626: 23,266 / 150,310 | PASS |
| A3 | Total FY2021 62.2 / FY2022 211.0 | same | line 2471 (income statement): 62,237 / 210,996 | PASS |
| A4 | Launch FY2023–25 71.9 / 125.4 / 199.0 | [10-K FY2025, Note 20] | 10-K-FY2025.txt line 4341: 71,894 / 125,376 / 199,042 | PASS |
| A5 | Space Systems FY2023–25 172.7 / 310.8 / 402.8 | same | line 4341: 172,698 / 310,838 / 402,757 | PASS |
| A6 | Total FY2023–25 244.6 / 436.2 / 601.8 | same | line 2325: 244,592 / 436,214 / 601,799 | PASS |
| A7 | Q2 2026 44.6 / 189.5 / 234.1; 6M 2026 108.2 / 326.2 / 434.4 | [10-Q Q2 2026, Note 18] | 10-Q-2026-Q2.txt lines 1649, 1661, 321: 44,586 / 189,480 / 234,066; 108,249 / 326,165 / 434,414 | PASS |
| A8 | Launch share (computed) 63 / 29 / 29 / 29 / 33 / 19 / 25 and complements | — | recomputed 62.6 / 28.8 / 29.4 / 28.7 / 33.1 / 19.0 / 24.9 | PASS |
| A9 | Footnote: FY2021–22 from 10-K FY2023 Note 20, FY2023–25 from 10-K FY2025 Note 20, Q2 from 10-Q Note 18 | — | note headings at 10-K-FY2023 line 4615, 10-K-FY2025 line 4331, 10-Q line 1639 | PASS |

### 2b. business.md §3 economics table (lines 32–44)

| # | Row | Tag | Found at | Result |
|---|---|---|---|---|
| B1 | Revenue | as A3/A6/A7 | | PASS |
| B2 | Gross margin GAAP (3.0) / 9.0 / 21.0 / 26.6 / 34.4 / 36.1 | Items 7/8 | 10-K-FY2023 line 1601: (3.0)%, 9.0%, 21.0%; 10-K-FY2025 line 1443: 21.0%, 26.6%, 34.4%; 10-Q line 1901: 36.1% | PASS |
| B3 | Launch gross margin (computed) (38.1) / (11.5) / 11.2 / 27.6 / 40.8 / 42.9 | Notes 20/18 | −14,856/38,971 = −38.12; −6,954/60,686 = −11.46; 8,067/71,894 = 11.22; 34,590/125,376 = 27.59; 81,270/199,042 = 40.83; 19,110/44,586 = 42.86 (10-K-FY2023 line 4630; 10-K-FY2025 line 4345; 10-Q line 1653) | PASS |
| B4 | Space Systems gross margin (computed) 55.7 / 17.3 / 25.1 / 26.2 / 31.3 / 34.6 | same | 12,963/23,266 = 55.72; 25,944/150,310 = 17.26; 43,342/172,698 = 25.10; 81,559/310,838 = 26.24; 125,911/402,757 = 31.26; 65,466/189,480 = 34.55 | PASS |
| B5 | R&D 41.8 / 65.2 / 119.1 / 174.4 / 270.7 / 82.4 | Items 8 / Item 1 | 10-K-FY2023 line 2479: 41,765; 65,168. 10-K-FY2025 line 2341: 119,054; 174,394; 270,716. 10-Q line 335: 82,429 | PASS |
| B6 | SG&A 58.4 / 89.0 / 110.3 / 131.6 / 165.3 / 59.7 | same | 10-K-FY2023 line 2481: 58,395; 89,026. 10-K-FY2025 line 2343: 110,273; 131,556; 165,303. 10-Q line 337: 59,661 | PASS |
| B7 | Operating margin GAAP (164.0) / (64.1) / (72.8) / (43.6) / (38.1) / (24.6) | FY2021–22 computed; FY2023–25 [10-K FY2025, Item 7] | FY2021: −102,053/62,237 = −163.98; FY2022: −135,204/210,996 = −64.08. FY2023–25 match the 10-K's own percentage table (10-K-FY2025 line 1455: (72.8)%, (43.6)%, (38.1)%). Q2: −57,514/234,066 = −24.57 | PASS. Note: direct division gives 72.7 / 43.5 / 38.0 for FY2023–25 (the 10-K's table rounds component lines), and the FY2023 10-K's own table (line 1611) shows (163.9)% for FY2021 where the draft computes (164.0)%. The row mixes two methods; a footnote would settle it (REVISE 13, optional) |
| B8 | Capex 25.7 / 42.4 / 54.7 / 67.1 / 156.3 / 26.0 | Items 8; Q2 computed | 10-K-FY2023 line 2671: 25,699; 42,412; 54,707. 10-K-FY2025 line 2523: 54,707; 67,093; 156,285. Q2 = 53,112 (10-Q line 535) − 27,065 (press-release-2026-Q1.txt line 200) = 26,047 | PASS |
| B9 | Capex / revenue (computed) 41 / 20 / 22 / 15 / 26 / 11 | — | recomputed 41.3 / 20.1 / 22.4 / 15.4 / 26.0 / 11.1 | PASS |

### 2c. business.md §4 cash table (lines 62–74)

| # | Row | Tag | Found at | Result |
|---|---|---|---|---|
| C1 | Net loss (117.3) / (135.9) / (182.6) / (190.2) / (198.2) / (94.3) | Items 8; Item 1 | 10-K-FY2023 line 2497; 10-K-FY2025 line 2359; 10-Q line 355 | PASS |
| C2 | Operating cash flow (71.8) / (106.5) / (98.9) / (48.9) / (165.5) / (134.4) | same | 10-K-FY2023 line 2667; 10-K-FY2025 line 2519; 10-Q line 531 | PASS |
| C3 | Capex row (incl. 6M 2026 53.1) | same | as B8; 10-Q line 535: 53,112 | PASS |
| C4 | Free cash flow (computed) (97.5) / (149.0) / (153.6) / (116.0) / (321.8) / (187.5) | — | −97,490 / −148,950 / −153,574 / −115,983 / −321,806 / −187,519 | PASS |
| C5 | Stock-based compensation 32.6 / 55.6 / 53.5 / 56.8 / 71.1 / 47.7 | same | 10-K-FY2023 line 2623; 10-K-FY2025 line 2477; 10-Q line 489 | PASS |
| C6 | Cash paid for acquisitions (66.4) / (65.8) / (19.0) / — / (132.4) / (44.3) | same | 10-K-FY2023 line 2675: 66,435; 65,824; 18,966. 10-K-FY2025 line 2527: 18,966; —; 132,441. 10-Q line 539: 44,271 | PASS |
| C7 | Gross ATM proceeds — / — / — / — / 1,146.1 / 1,529.6 | Item 8; Note 13; Note 12 | 10-K-FY2025 line 2539: 1,146,057; 10-Q line 551: 1,529,639 | PASS |
| C8 | Cash and marketable securities 692.1* / 481.0 / 324.0 / 479.7 / 1,098.8 / 2,387.6 | Items 8; Note 5 | FY2021: 10-K-FY2023 line 2723 (cash + restricted cash 692,075; "Purchases of marketable securities" for 2021 is "—" at line 2677, supporting the footnote). FY2022: 242,515 + 229,276 + 9,193 = 480,984 (lines 2369, 2371, 2397). FY2023: 162,518 + 82,255 + 79,247 = 324,020. FY2024: 271,042 + 147,948 + 60,686 = 479,676 (10-K-FY2025 lines 2211–2237). FY2025: 828,660 + 187,917 + 82,247 = 1,098,824. 6M 2026: 2,129,485 + 172,700 + 85,405 = 2,387,590 (10-Q lines 209–235) | PASS |
| C9 | Shares outstanding 450.2 / 475.4 / 488.9 / 504.5 / 543.6 + 46.0 / 598.2 + 41.0 | Items 8; Item 1 | 10-K-FY2023 line 2567: 450,180,479; line 2443: 475,356,517 and 488,923,055. 10-K-FY2025 lines 2285–2287: 504,453,785; 543,574,552; preferred 45,951,250. 10-Q lines 281–283: 598,180,438; preferred 40,951,250 | PASS |
| C10 | Footnote: preferred "convert one-for-one and count as common for per-share figures" | [10-Q Q2 2026, Note 17] | 10-Q line 1607: "for the purposes of the calculation of earnings per share, the Preferred Stock is treated as common stock" | PASS |

### 2d. outlook.md §1 indicator table (every cell, lines 10–19)

| # | Cell | Tag | Found at | Result |
|---|---|---|---|---|
| D1 | Backlog $2,355.9M; about 45% | [10-Q Item 2] | 10-Q line 761 (Note 3: $2,355,949; "approximately 45%") and line 1841 (Item 2) | PASS |
| D1' | Q1: $2.2B, "up 20.2% QoQ"; 12-month share not disclosed | [Q1 2026 release] | press-release-2026-Q1.txt line 17; no conversion share anywhere in that release | PASS |
| D2 | Q2 Launch $44.6M 42.9%; Space Systems $189.5M 34.6% | [Note 18] | as B3/B4 | PASS |
| D2' | Q1 Launch $63.7M 44.3%; Space Systems $136.7M 35.3% (computed) | [Note 18] | 108,249 − 44,586 = 63,663; 326,165 − 189,480 = 136,685; (47,333 − 19,110)/63,663 = 44.33%; (113,736 − 65,466)/136,685 = 35.31% | PASS |
| D3 | 6 Electron missions, 2 HASTE; $9.1M and $4.4M per launch | [Item 2] | 10-Q lines 1813, 1825 | PASS |
| D3' | Q1: 6 (12 in six months less 6); six-month $9.2M / $4.9M | [Item 2] | 10-Q lines 1807, 1829 | PASS |
| D4 | "Government customer" 42% of six-month revenue | [Note 3] | 10-Q line 773 | PASS |
| D4' | FY2025: 28% and 47% | [10-K Note 21; Item 1A] | 10-K-FY2025 line 4411 ("Government Customer | 28 % | 11 % | *"); line 705 (47%) | PASS |
| D5 | 41.5%; $(8.8)M | [Q2 2026 release] | press-release.txt lines 266, 251 (−8,833) | PASS |
| D5' | 43.0%; $(11.8)M; guided "38% and 40%" / "$20 million and $26 million" | [Q1 2026 release] | press-release-2026-Q1.txt lines 260, 247 (−11,751), 33, 37 | PASS, quotes verbatim |
| D6 | $(110.1)M = $(84.1)M OCF less $26.0M capex; $2,387.6M | [slides p.32; releases] | OCF −134,407 − (−50,332) = −84,075; capex 53,112 − 27,065 = 26,047; sum −110,122. slides.txt line 859 (p.32 visual read) shows −84.1 / −26.0 / −110.1. Cash as C8 | PASS |
| D6' | Q1 $(77.4)M; $1,476.8M (computed) | [slides p.32; Q1 release] | −50,332 − 27,065 = −77,397 (Q1 release lines 198, 200); 1,205,499 + 177,852 + 93,494 = 1,476,845 (lines 118, 119, 131) | PASS |
| D7 | 598.2M + 41.0M at June 30; 598.4M at Aug 5; ATM gross $1,079.3M in Q2 (computed) | [10-Q cover; Item 1; releases] | 10-Q lines 283, 281; cover line 71 (598,350,482); 1,529,639 − 450,347 (Q1 release line 207) = 1,079,292; CFO L90 "$1.08 billion" agrees | PASS |
| D7' | 575.8M + 46.0M; ATM gross $450.3M; guided "629 million, including approximately 46 million of Series A"; actual 629.7M | [Q1 release; Q2 release] | Q1 release lines 155, 154, 207, 38; Q2 release line 104 (629,681,803) | PASS |
| D8 | Neutron quotes (Q2 and Q1) | [releases] | press-release.txt line 20; press-release-2026-Q1.txt line 28 | PASS, verbatim |
| D9 | Line 19 year-ago: $144.5M; Launch $46.6M / Space $97.9M; 36.9%; $27.6M loss; five launches; backlog +137% | [Q2 release; 10-Q Note 18; Item 2] | release lines 81, 266, 251 (27,584), 16; 10-Q line 1649 (46,646 / 97,852); line 1813 ("five Electron launch missions") | PASS |

### 2e. outlook.md §4 guidance quotes (word for word)

| # | Quote | Tag | Found at | Result |
|---|---|---|---|---|
| E1 | Eight guidance bullets, "For the third quarter of 2026, Rocket Lab expects: Revenue between $250 million and $265 million. … approximately 41 million of Series A Convertible Participating Preferred Shares." | [Q2 2026 release] | press-release.txt lines 30–38 (bullets joined into one paragraph; every word matches) | PASS |
| E2 | "Stock-based compensation is currently expected to range from $18 million to $20 million in Q3 2026." | [Q2 2026 release] | line 39 | PASS |
| E3 | "driven by weaker mix within several of our product lines" | [Q2 2026 slides, p.33] | slides.txt line 924 (p.33 gatherer visual read; p.33 spans lines 863–928) | PASS |
| E4 | "are accounting for a shift in mix within our Space Systems business, and we expect a beneficial remixing impact on gross margins as we look beyond Q3" | [Q2 2026 call] | transcript.txt line 94 | PASS |
| E5 | "consistent with prior quarters, we expect negative non-GAAP free cash flow in the third quarter to remain at elevated levels. Driven by ongoing investments in Neutron development and scaling production" | [Q2 2026 call] | line 96 (the odd sentence break after "levels." is the transcript's) | PASS |
| E6 | "below Q2's actual 36.1% GAAP and 41.5% non-GAAP"; transcript "second quarter" misread | [release; call] | release line 266; 10-Q line 1901; transcript line 92 | PASS |
| E7 | "Full year 2026: none" | [release; call] | no "full year", "full-year" or FY2026 figure in transcript.txt, press-release.txt or slides.txt (grep); slides line 923 is the Q3 outlook | PASS |

### 2f. outlook.md §5 claim quotes (word for word)

| # | Quote under claim | Found at | Result |
|---|---|---|---|
| F1–F3 | "Revenue between $250 million and $265 million." / "Non-GAAP Gross Margins between 35% and 37%." / "Adjusted EBITDA loss of between $17 million and $23 million." | press-release.txt lines 31, 33, 37 | PASS |
| F4 | "Basic Weighted Average Common Shares Outstanding of 641 million" | line 38 (fragment) | PASS |
| F5 | "we expect negative non-GAAP free cash flow in the third quarter to remain at elevated levels." | transcript line 96 | PASS |
| F6 | "we expect a beneficial remixing impact on gross margins as we look beyond Q3." | line 94 | PASS |
| F7 | "Production of the Stage 1 tank is currently aligned with the target delivery of Neutron to the launch pad in Q4 2026." | release line 20 (also 10-Q line 1759) | PASS |
| F8 | "that will be the real turning point where we go to adjusted EBITDA positivity in the quarter after that, that event happens." | line 228 | PASS |
| F9 | "We're at 13 launches this year with 100% mission success and on track to beat last year's launch Tally2."; 21 launches in 2025 | line 48 (garble "Tally2" reproduced as written, correctly); 10-K-FY2025 line 1361 | PASS |
| F10 | "we signed a significant volume of contracts ... which will be reflected in our Q3 backlog." | line 80 (ellipsis drops "within Space Systems and launch across all vehicles") | PASS |
| F11 | "Government customer | 42%" | 10-Q line 773 | PASS |
| F12 | "The transaction is expected to be completed in mid-2027" | line 36 | PASS |

### 2g. Prose sentences, both files

| # | Sentence / figures | Tag | Found at | Result |
|---|---|---|---|---|
| G1 | §1 l.6: 300 kg; 87 successful missions by June 30, 2026; component list; Mynaric 2026 / GEOST 2025 | [10-K Item 1; 10-Q Item 2] | 10-K-FY2025 line 317; 10-Q lines 1787, 1751; 10-Q Note 4 | PASS |
| G2 | §1 l.8: DoW quote; "Planet and BlackSky"; "diverse mix …" quote; 47%; "Launch has never been so constrained" | [10-K Item 1; Item 1A; call] | 10-K-FY2025 line 273 (verbatim); line 237 ("Blacksky Holdings … Planet"); line 275 (verbatim); line 705; transcript line 68 | PASS |
| G3 | §1 l.10 history: founded 2006; first launch 2017; U.S.–NZ treaty; listed Aug 25, 2021 via Vector; ASI/PSC/SolAero within six months; Sinclair 2020; May 2025 reorganization; GEOST/Mynaric/Motiv dates; Iridium June 28, 2026, $54, ~$8.0B, "expected to close in 2027"; 66 satellites; $871M | as tagged | DEF14A lines 445, 463; 10-K-FY2025 lines 237, 239, 275; 10-K-FY2023 Note 4 (lines 3316, 3376, 3460); 10-Q Note 1 lines 627–641 and Note 4; deck line 124 | PASS. "voice-and-data" is from the 8-K press release (8-K-2026-06-29.txt line 450); tag added by reviewer |
| G4 | §2 l.14: point-in-time deposits, over-time by cost, PO components; HASTE over time | [10-K Item 7; Note 2; 10-Q Item 2] | 10-Q lines 1841–1843, 1813 | PASS |
| G5 | §2 l.26: 21 launches at $8.5M (2025); 6 at $8.1M (2021); 31% / 33% / 47%; **"(earlier years not disclosed)"**; 79% U.S.; backlog $2,355.9M / $940.2M / 45%; options excluded | [10-K Item 7; 10-K FY2023 Item 7; Item 1A; Note 21; 10-Q Item 2; Note 3; release] | 10-K-FY2025 lines 1361, 1371; 10-K-FY2023 lines 1523, 1537; 10-K-FY2025 line 705; line 4429; 10-Q lines 1841, 761, 1837; release line 23 | **FAIL on one clause:** 10-K-FY2023.txt line 813 reads "During 2023, 2022 and 2021, approximately 31%, 33% and 8%, respectively, of our total annual revenues were derived from contracts with the U.S. government …". The 2022 and 2021 shares are disclosed. Everything else PASS |
| G6 | §3 l.30: "absorption" quote; $9.2M → $4.8M; $8.1M → $8.5M; "north of 70 points"; "mid-30s" | [10-K Item 7; FY2023 Item 7; call] | 10-K-FY2025 line 1395 (verbatim), 1371; 10-K-FY2023 line 1537; transcript line 238 | PASS |
| G7 | §3 l.46: FY2025 gross profit 207.2, R&D 270.7, SG&A 165.3, operating loss 228.8; Q2 84.6 / 82.4 / 59.7; adj. EBITDA −8.8 with D&A 20.9 (computed), SBC 19.6, deal costs 8.6; "primarily due to Neutron development progress"; CFO turning-point and 18–24-month quotes; "next 12 months" | as tagged | 10-K-FY2025 lines 2335–2347; 10-Q lines 331–337; release lines 238–251 (10,172 + 10,771 = 20,943); 10-K line 1507; transcript line 228; 10-K line 679 | PASS |
| G8 | §3 l.48: capex 26% of revenue; CFO "remain elevated …" | [10-K Item 8; call] | 156,285 / 601,799 = 26.0%; transcript line 86 | PASS |
| G9 | §3 l.52 Neutron: 43 m, two-stage, 13,000 kg, return to site or ocean platform, Archimedes, LC-3 quote; "significantly higher revenue per launch"; ASP and no-discount quotes; FY2023 15,000 kg expendable | [10-K Item 1; call; 10-K FY2023 Item 7] | 10-K-FY2025 lines 325–327, 449 (verbatim), 287; transcript line 112; 10-K-FY2023 line 1489 | PASS |
| G10 | §3 l.54: Jan 21, 2026 tank "ruptured"; "Neutron's first launch is now targeted for Q4 2026"; 10-Q wording | [10-K Item 1A; Item 7; 10-Q Item 2] | 10-K-FY2025 lines 693, 1331 (verbatim); 10-Q line 1759 (verbatim) | PASS |
| G11 | §3 l.56: no Neutron program cost breakout; R&D 41.8 → 270.7; construction in progress 27.3 → 138.9; inference labelled; Flatellite "to launch on Neutron"; Kepler NET 2028; "7x confidential customer launches"; Neutron backlog not disclosed | as tagged | no program-level figure in 10-K Note 2/Note 10 or 10-Q (grep for Neutron in the notes: none with a dollar amount); 10-K-FY2025 line 3485 (27,285); 10-Q line 1285 (138,908); release line 21; slides.txt line 675 (p.26), line 693/698 (p.27) | PASS on all figures. Nuance: no dollar backlog is disclosed, but slide p.27 lists the slots (1 Kepler, 7 confidential, SB-AMTI, NSSL, a USAF experiment) and the Q1 release said "five new dedicated Neutron launches signed" (REVISE 14) |
| G12 | §4 l.60: FCF FY2025 −321.8 (computed) | [10-K Item 8] | as C4 | PASS |
| G13 | §4 l.76: non-GAAP FCF −77.4 / −110.1; ATM net $1,119.3M FY2025; $1,512.8M 6M 2026; programs $500M / $750M / $1B / $3B; 639.1M shares; "about 30% less"; 3–6% / 17% / 8%; 66.7M conversion shares; "$13.4 million of debt" | as tagged | slides line 859; 10-K-FY2025 line 2437 (1,119,329); 10-Q lines 403 + 417 (444,922 + 1,067,832 = 1,512,754); 10-Q lines 1475–1487; 598,180,438 + 40,951,250 = 639,131,688; 1 − 450.2/639.1 = 29.6%; 5.6 / 2.8 / 3.2 / 16.9 / 8.4%; (355,000 − 13,366) × 0.1951029 = 66,653 (10-Q lines 1445–1451); 10-Q line 1451 ($13,366) | PASS. Two notes: (i) the 10-Q's MD&A (line 2251) gives net ATM proceeds as "$1,512.9 million" (cash-flow 1,529,639 − 16,722), the equity statement 1,512,754; the draft's figure is the equity statement's, so the reviewer added "Item 1" to the tag (REVISE 6 asks the writer to pick and footnote); (ii) "only $13.4 million of debt remains" is the convertible notes; the balance sheet also carries $1.7M long-term borrowings and $14.5M finance-lease liabilities (10-Q lines 291–297) (REVISE 9) |
| G14 | §4 l.78: adj. EBITDA −27.6 / −11.8 / −8.8; equity $3.5B; "about $50 million a quarter"; Iridium $495M / $871M | [releases; 10-Q Item 1; deck p.6] | release lines 251, Q1 release 247; 10-Q line 289 (3,492,153); net loss 49,258; deck lines 124–130 | PASS on numbers. Wording: the deck calls the $495M "2025 OEBITDA" (operational EBITDA, defined at deck line 147), not "adjusted earnings" (REVISE 5) |
| G15 | §5 l.82: 87 successes; three failures (2020, 2021, 2023); "second most frequently launched orbital rocket"; "locking in Neutron slots early"; **"after September 2023 the company lost revenue waiting for FAA clearance"** | [10-K Item 1; Item 1A; 10-Q Item 2; call] | 10-Q line 1787; 10-K-FY2025 line 775 ("three failed customer launches, which occurred in July 2020, May 2021 and September 2023"); line 237/315 (verbatim); transcript line 70 | **FAIL on the last clause:** 10-K-FY2025 line 793 says only that the launch rate "will be negatively impacted if we are not able to operate Electron for any reason, including not being granted appropriate government clearance after a launch failure such as occurred in … September 2023". No revenue loss is stated and the sentence says "government clearance", not FAA. The rest PASS |
| G16 | §5 l.84: "design[s] and manufacture[s] many components and subsystems …"; 1,000 reaction wheels quote; "eliminate margin stacking" | [10-K Item 1; call] | 10-K-FY2025 line 403; transcript lines 168, 172 | PASS, verbatim |
| G17 | §5 l.86: "call it, 4 years"; termination-rights quote; MDA liquidated-damages quote; "contract termination and study revenue" | [call; 10-K Item 7; Note 3; 10-Q Item 2; Note 3] | transcript line 162; 10-K-FY2025 line 1375 (verbatim); 10-Q line 757 (verbatim); 10-Q lines 1813/1943 (Item 2) | PASS |
| G18 | §5 l.88: facility security clearances; Government Security Committee | [10-K Item 1A; DEF 14A] | 10-K-FY2025 line 1137; DEF14A lines 433, 521 | PASS ("personnel" clearances are implied by line 897's "loss of security clearances", not stated) |
| G19 | §5 l.90: "at their convenience"; competitor list | [10-K Item 1] | 10-K-FY2025 lines 525, 463 | PASS |
| G20 | §6#1 l.96: two Neutron risk quotes; "substantially greater resources"; "already spoken for, for their own internal programs" | [10-Q Item 2; 10-K Item 1A; call] | 10-Q line 1783 (both verbatim); 10-K line 737; transcript line 248 | PASS |
| G21 | §6#2 l.98: 11% / 28% / 42%; 47% / 49% / 77%; "terminated or suspended … at any time"; "we bear the risk of loss if costs increase"; October 2025 shutdown effects | [10-K Note 21; 10-Q Note 3; 10-K Item 1A] | 10-K-FY2025 line 4411; 10-Q line 773; 10-K lines 705, 715, 703, 705, 719–721 | PASS |
| G22 | §6#3 l.100: MDA Feb 2022, 17 buses, "not possible to determine with certainty" quote; $12.8M downward adjustment | [10-Q Note 3; 10-K Note 3] | 10-Q line 757; 10-K-FY2025 line 3053 (12,818) | PASS |
| G23 | §6#4 l.102: "currently dependent on Electron"; "will not protect us against our own losses"; 33% of revenue; 40% of backlog | [10-K Item 1A; Note 20; 10-Q Item 2] | 10-K lines 793, 859; 940.2 / 2,355.9 = 39.9% | PASS |
| G24 | §6#5 l.104: "might not be available on company favorable terms, if at all, or may be available only by diluting existing stockholders"; "more than five years" (computed) | [10-K Item 1A; 10-Q Note 5] | 10-K-FY2025 line 947 (verbatim); 2,387.6 / 110.1 = 21.7 quarters | PASS |
| G25 | §6#6 l.106: "over $3.0 billion"; "approximately $1.8 billion"; $3.6B 364-day bridge; "to seek permanent debt or equity financing to replace"; "not conditioned on our obtaining any financing"; Neutron funds; $223.62M fee; no reverse fee; combined debt/shares/synergy targets not disclosed | [10-Q Item 2; Note 1; Part II Item 1A; 8-K; deck p.11] | 10-Q lines 2181, 2183, 2327 (both quotes), 2331 ("including Neutron"); 8-K-2026-06-29.txt line 196 (fee), lines 180–205 (no Rocket Lab-payable fee described); deck lines 218–232 (p.11 has no leverage or synergy figure) | PASS |
| G26 | §6#7 l.108: built in Auckland; ITAR; licence delays late 2025; ~15% foreign-currency spend, unhedged | [10-K Item 1; Item 1A; Item 7A] | 10-K-FY2025 lines 409, 1111, 721, 941 ("approximately 15% of our expenditures, or $126.8 million … We do not currently … use hedging strategies") | PASS |
| G27 | §6#8 l.110: Beck quotes; no key-person insurance | [10-K Item 1A] | line 921 (verbatim) | PASS |
| G28 | §7 l.114: age 48; CEO since July 2013; chairman Aug 2021; only non-independent of seven; 40.95M preferred, one-for-one, votes as-converted, one director, auto-convert; 7.5%; $800,000 → "$1.00 or the statutory minimum …"; 392,155 RSUs; "redirected …" quote; $11.2M charge; $6.8M 2025 pay mostly RSUs | [DEF 14A; 10-K Note 13; 10-Q Note 12; Note 13; 8-K 2026-03-30] | DEF14A lines 421, 445, 517, 369, 1621; 10-Q lines 1455–1467; 8-K-2026-03-30.txt lines 77–86 (verbatim); 10-Q line 1477 (11,180); DEF14A line 1107 (800,000 + 6,030,680 = 6,830,680) | PASS. Two notes: the $800,000 salary is in the proxy, not the 8-K (tag added by reviewer); the preferred also converts if he leaves for any board-approved executive role, on death or disability, or if his stake falls below 5% (10-Q line 1461) (REVISE 7) |
| G29 | §7 l.116: Spice start date not in sources; $86.1M options exercised; pay = salary + time-based RSUs + discretionary bonus, "no formula", no performance-vesting equity; "No base salary increases" / "No discretionary cash bonuses"; Khosla 6.1%; BlackRock 5.2% | [DEF 14A] | no Spice biography in DEF14A (earliest grant 8/3/2018 at line 1171); line 1213 (86,072,891); lines 713, 741, 717, 719, 1645, 1647 | PASS with a note: DEF14A line 955 records a "Senior Executive Cash Incentive Bonus Plan" adopted August 25, 2025 with committee-set performance targets (no payout for 2025); line 1247 says the Company "did not have a formal bonus program". "No formula" is defensible but should mention the plan (REVISE 8) |
| G30 | §7 table: dividends never paid; buybacks restricted under Department of Commerce agreement; SolAero $76.2M; GEOST $292.1M about half in stock; Mynaric $155.3M, 2.28M shares; Motiv $44.5M; goodwill $299.1M "substantially all" Space Systems | as tagged | 10-K-FY2025 line 1279; 10-K-FY2023 line 3464 (76,181); 10-Q line 963 (292,089; stock 137,653 = 47%); 10-Q line 863 ("aggregate consideration value of $155,300 … 2,277,002 shares"; accounting fair value $160,802 at line 873); 10-Q line 803 (44,539); 10-Q line 1313 | PASS |
| G31 | §7 l.127: "We streamline it, introduce efficiencies …" | [call] | transcript line 44 | PASS |
| G32 | outlook §2 l.23: "three key verticals"; "space applications, the entire reason …"; "self-launching Tier 1 space power …"; "decade or more"; "not the endpoint … starting point"; "there will be a constellation …" | [call; release] | transcript lines 28, 28, 28 (verbatim; the release's line 13 wording differs slightly, the call is the verbatim source), 30, 268 (ellipsis drops "I think"), 158 | PASS |
| G33 | outlook §3 l.27: ASP; "narrowing"; "1, 3, 5 ramp"; "quarter after" | [call] | lines 112, 58, 108, 228 | PASS |
| G34 | outlook §3 l.29: $44.6M, down 30% on a similar launch count; two of six HASTE, revenue "largely" booked earlier; "13 launches …"; $266M, 12 launches + 6 options; Kodiak two pads; "90+ launches" | [10-Q Item 2; call; release] | transcript line 74; 63.7 → 44.6 = −30.0%; 10-Q line 1813; transcript line 48; 10-Q line 1769; transcript line 52 and release line 19; release line 18 | PASS on facts. Wording: the 10-Q says HASTE revenue "was partially recognized in prior quarters" and the CFO "a significant portion"; "largely" overstates (REVISE 10) |
| G35 | outlook §3 l.31: $189.5M, +94%, quote; **"SDA Tranche 2 and Tranche 3 ($816 million, 18 satellites, delivery 2029)"**; $397M July 30; ">$160 million" three GEO satellites; late MDA; "10, 40, 40, 10"; "beyond Q3" | [10-K Item 7; 10-Q Item 2; Note 3; release; call] | 10-Q line 1943 (verbatim); 10-K-FY2025 line 1325; 10-Q line 1773; release line 22; transcript lines 162, 94 | **FAIL on attribution:** 10-K-FY2025 line 1325 gives $816 million (base $806M + $10M options), 18 satellites and 2029 delivery for the Tranche 3 award signed December 17, 2025 alone. Tranche 2 is a separate program named only on the call (line 238); no Tranche 2 size is in the sources. The sentence reads as if both tranches total $816M |
| G36 | outlook §3 l.33: "a big moat"; Mynaric $13.2M revenue, $13.2M operating loss; "insolvency process"; "few quarters"; components not disclosed separately | [call; 10-Q Note 4; Note 18] | transcript lines 168, 194, 196; 10-Q line 939 (13,195 / 13,245); Note 18 splits products vs services only | PASS |
| G37 | outlook §3 l.35: $54; ~$8.0B; "expected to close in 2027" (10-Q) vs "mid-2027" (call, deck); "table gets reset"; "significant free cash flow" | [10-Q Item 2; call; deck p.11] | 10-Q line 2181; transcript line 36; deck line 222; transcript line 230 | PASS |
| G38 | business.md §8 cells: $2,355.9M / 45%; 42.9% / 34.6%; 6, $9.1M, $4.4M; 42% / 47%; 41.5% and $(8.8)M vs 38–40% and $(20)–(26)M; $(110.1)M / $2,387.6M; 598.4M + 41.0M; $1,529.6M; Neutron wording | as tagged | as above | PASS on every number |
| G39 | business.md §8 indicator 1 anchor: "10-Q Note 3 for the segment split" | — | the space systems / launch split ($1,415.8M / $940.2M) is in Item 2 (10-Q line 1841); Note 3 (line 761) gives only the total and the 12-month share | **FAIL (wrong anchor)** |
| G40 | Both Sources tables | — | every prefix used maps to a cached file; every row is used | PASS |

**Totals: 96 checked; 92 PASS; 4 FAIL (G5 "earlier years not disclosed", G15 "lost revenue waiting for FAA clearance", G35 Tranche attribution, G39 indicator anchor); 0 UNVERIFIABLE.**

Special attention items requested by the coordinator, all confirmed: unit conversions ($ thousands → $ millions) in every table; five-year segment table sources (FY2021–FY2022 from 10-K-FY2023.txt, FY2023–FY2025 from 10-K-FY2025.txt); segment gross margins; backlog $2,355.9M and 45%; concentration 28% / 42% / 47% / 77% (and 49% top five, 11% FY2024); ATM proceeds and share counts; Iridium terms ($54, ~$8.0B, $3.6B bridge, "over $3.0 billion", "approximately $1.8 billion", $223.62M fee, 2027 / mid-2027); Beck's 40.95M preferred and its description; the Q3 2026 guidance lines; every Q1 2026 value in outlook §1.

---

## 3. Jargon audit

Read as a smart 16-year-old with no finance or space-industry background. Items marked *fixed* were glossed directly (see "Fixed directly").

| Term | First use | Status |
|---|---|---|
| hypersonic | business §1 l.6, glossary l.151 | *fixed* (over five times the speed of sound), both places |
| suborbital | §1 l.6, glossary | *fixed* in the glossary HASTE entry; §1 points to it |
| prime contractors | §1 l.8 | *fixed* |
| gross margin | §3 l.30 (prose), l.35 (table) | *fixed* at l.30; the table header still comes first, acceptable since the definition is on the same screen |
| GAAP / non-GAAP | §3 table l.35 before any prose use | glossary entry exists; *fixed* by adding a one-sentence definition to the table footnote (l.44) |
| operating margin | §3 table l.40 | *fixed* in the same footnote |
| capex | §3 table l.41, prose l.48 | glossary entry exists; *fixed* inline at l.48 |
| "fleet of tails" (in quote) | §3 l.46 | *fixed* (tails: individual rockets) |
| ATM | §4 table l.70 before the l.76 explanation | *fixed* table label "(at-the-market, see below)"; l.76 already explains it in plain words |
| marketable securities, restricted cash | §4 table l.71, footnote l.74 | *fixed* (short-term investments that can be sold quickly); "restricted cash" left, inferable |
| convertible notes | §4 l.76 | *fixed* |
| FAA | §5 l.82, §6 l.102 | *fixed* at first use |
| MDA (program / contract) | §5 l.86 (first use, no explanation) | *fixed*: "the program for MDA Corporation, a satellite-maker customer" |
| liquidated damages | §5 l.86 (in quote) | glossary entry exists; *fixed* with "(a pre-agreed penalty)" after the quote |
| bridge loan | §6#6 l.106 | not in glossary, not inferable; *fixed* |
| reverse fee | §6#6 l.106 | *fixed* |
| term loans | §6#6 l.106 | left; plain enough ("loans") |
| unhedged | §6#7 l.108 | *fixed* |
| goodwill | §7 table l.125 | *fixed* in the row label |
| QoQ (in quote) | outlook §1 l.10 | *fixed* (quarter on quarter) |
| Tier 1 (in quote) | outlook §2 l.23 | *fixed* (top-rank) |
| constellation (in quote) | outlook §2 l.23 | *fixed* |
| geostationary | outlook §3 l.31 | *fixed* |
| insolvency process (in quote) | outlook §3 l.33 | *fixed* (bankruptcy) |
| mix | outlook §4 l.41 | *fixed*; business.md §3 l.30 already uses "depend on mix: some … while …", which explains itself |
| basic weighted-average shares | outlook claim 4 | untouched (claims are off-limits to the reviewer); fine for a claim, but "average share count over the quarter" would be plainer |
| enterprise value | business §1 l.10 ("share price plus debt"), outlook l.35 | glossed in business.md; left bare in outlook (reader has business.md first) |
| backlog, adjusted EBITDA, free cash flow, dilution, over-time revenue, ASP, S-4, ITAR, RSUs, Series A preferred, buses, star trackers, reaction wheels, absorption | various | already explained at or before first use; good |
| Flatellite, HASTE, Archimedes, Electron, Neutron | various | product names; HASTE in glossary |
| low Earth orbit, launch pad, satellite platform | | name-inferable |

Glossary: 11 entries, each one sentence, each used in the text. None superfluous. "Gross margin" and "bridge loan" could be added at the writer's discretion; the inline glosses make it optional.

Banned words (leverage, synergy, headwind, tailwind, monetize, ecosystem, at scale, robust, unlock, TAM): a case-insensitive sweep of both files found **none**, inside or outside quotes. (The writer avoided the CFO's "robust" and the CEO's "unblock".)

Paragraphs that are mostly numbers: business.md l.76 (§4 dilution paragraph: eleven figures) and l.106 (§6#6: six dollar figures) are dense but each figure carries a plain clause; l.114 (§7) is borderline. None is a wall.

---

## 4. Invented-number check

Every figure in both files traces to a cached source or a labelled computation, with the exceptions in §2 above. Specific sweeps:

- **Neutron cost.** The draft states plainly that "No filing breaks out Neutron's program cost" and labels the R&D / construction-in-progress attribution "Our inference, not a disclosed figure" (l.56). Correct: no program-level Neutron dollar figure exists in the 10-K notes, the 10-Q notes, the release or the slides. The 15,000 kg → 13,000 kg spec change is sourced (10-K-FY2023 line 1489; 10-K-FY2025 line 325).
- **Launch counts.** 87 successful (10-Q line 1787), 75 through 2025 (10-K line 323), 21 in 2025 / 16 in 2024 / 10 in 2023 (10-K line 1361), 6 / 9 / 10 for 2021–2023 (10-K-FY2023 line 1523), 12 in six months and 6 in Q2 (10-Q lines 1807, 1813), five in Q2 2025 (line 1813), three failures July 2020 / May 2021 / September 2023 (10-K line 775). All sourced. "13 launches this year" is quoted from the call, not asserted.
- **Iridium leverage / synergies.** None asserted. "Combined debt after the deal, shares to be issued and cost-saving targets are not disclosed" (l.106) is correct: deck p.11 and the 8-K give price, EV, bridge size, timing and funding intent only. The 8-K's "significantly accretive to Rocket Lab's cash flow generation and profitability" (line 445) and the CFO's "pretty significant free cash flow" are qualitative and the draft quotes only the latter.
- **Inferences presented as fact:** (i) §5 l.82 "lost revenue waiting for FAA clearance" (G15, FAIL); (ii) §1 l.6 and glossary "hypersonic-weapon development" — the 10-K (line 321) says "hypersonic and suborbital system technology development" and the 10-Q (line 1769) "missile defense programs"; "weapon" is the writer's word (REVISE 11); (iii) §4 l.78 "$495 million of its own adjusted earnings" for what the deck calls OEBITDA (REVISE 5); (iv) §1 l.10 "founded the company in New Zealand" — the proxy says founded 2006 and launched Atea-1 "from the Southern Hemisphere" (line 455); acceptable.
- **Labelled computations** all re-done: segment shares, segment margins, FY2021–22 operating margins, capex/revenue, FCF, Q2 capex and OCF by subtraction, Q2 ATM gross, Q1 segment figures, Q1 cash, 639.1M shares, 30% dilution, share-count growth rates, 66.7M conversion shares, D&A 20.9, runway "more than five years", "about half in stock" for GEOST. All correct.

---

## 5. Claims quality (outlook.md §5)

Count: 12 (within 6–12). Headline guidance: claims 1–4 (4 of 12); the rest are fundamental signals (cash burn, margin direction, Neutron dates, launch cadence, backlog, concentration, Iridium). Good balance.

| # | Single sentence? | Single direction (can fail)? | Tied to metric / date / event | Quote verbatim? | Sharpening / disclosure label | Notes |
|---|---|---|---|---|---|---|
| 1 | Yes | Yes | Q3 revenue $250–265M | Yes | n/a | |
| 2 | Yes | Yes | Q3 non-GAAP GM 35–37% | Yes | n/a | |
| 3 | Yes | Yes | Q3 adj. EBITDA loss $17–23M | Yes | n/a | |
| 4 | Yes | Yes | Q3 basic shares ≤ 645M | Yes | Labelled ("our ceiling … not management's number") | Release wording "including approximately 41 million of Series A" is reflected |
| 5 | Yes | Yes (fails if outflow < $77.4M or positive) | Q3 non-GAAP FCF outflow ≥ $77.4M | Yes | Labelled sharpening of "elevated levels" | Threshold is the Q1 level; fine |
| 6 | Yes | Yes | Q4 non-GAAP GM guide midpoint > 36%, given on Q3 call | Yes | Labelled | Dropped if no Q4 guide is given; gradeable |
| 7 | Yes | Yes ("a later target is a miss") | Neutron pad delivery still Q4 2026 on Q3 call and 10-Q | Yes | n/a | Two sources, one fact; fine |
| 8 | Yes | Yes | Repeats adj.-EBITDA-positive-quarter-after-first-launch | Yes | n/a | Met if repeated, Missed if changed, Dropped if silent |
| 9 | Yes | Yes | ≥ 17 missions in nine months to Sept 30 (10-Q Item 2) | Yes, including the transcript's garble "Tally2" (correctly reproduced; consider "[sic]") | Labelled sharpening | 12 through June 30 + 13th by Aug 10 makes 17 by Sept 30 a real test |
| 10 | Yes | Yes | Backlog at Sept 30 > $2,355.9M | Yes | Labelled disclosure check; states it is a quarter-end balance | |
| 11 | Yes | Yes | Government customer ≥ 40% in nine-month YTD column | Table row quoted | Labelled disclosure check; column stated | Note: if the customer drops below 10% the row disappears from Note 3, which grades as Missed; fine |
| 12 | Yes | **Two conditions** ("still 'mid-2027'" AND "not been terminated") | Q3 call + merger agreement | Yes | n/a | Both halves are observable, so it can fail, but it is double-barreled and the "mid-2027" wording is fragile: the 10-Q already says "expected to close in 2027" (line 1765), so a Q3 call that says "2027" without "mid" would be an unclear grade. Reduce to one condition and guard the wording (REVISE 12) |

No either/or constructions. No vague statement passed off as a claim.

---

## 6. Indicators (business.md §8)

Eight proposed (within 5–8). Anchors checked against the cached 10-Q and release:

| # | Indicator | Recurring disclosure | Anchor as written | Assessment |
|---|---|---|---|---|
| 1 | Backlog; 12-month share | 10-Q Item 2 "Backlog" paragraph (total, segment split); Note 3 "Backlog" (total, 12-month share) | "10-Q Item 2 ('Backlog'); 10-Q Note 3 for the segment split" | **Anchor wrong:** the split is in Item 2, Note 3 has the 12-month share (REVISE 4) |
| 2 | Segment revenue and gross margin | 10-Q Note 18 / 10-K Note 20 segment table | correct | OK |
| 3 | Launches; revenue and cost per launch | 10-Q Item 2, "Key Metrics and Select Financial Data" → "Revenue and Cost Per Launch" (line 1819); launch counts under the same heading (line 1807) | "results discussion and 'Key Factors'" | Minor: the heading is "Key Metrics and Select Financial Data" (line 1797), not "Key Factors Affecting Our Performance" (line 1779) (REVISE 4) |
| 4 | Largest customer share (YTD); U.S. government-related share (annual) | 10-Q Note 3 concentration table (six-month column); 10-K Item 1A (annual) | correct | OK. Note the 10-Q table lists only customers at ≥10%, so a fall below 10% shows as disappearance |
| 5 | Non-GAAP GM and adj. EBITDA vs guided ranges | Release reconciliation tables and outlook bullets | correct | OK. Depends on management continuing to guide both, which it has for at least Q1 and Q2 |
| 6 | FCF; cash + marketable securities | Release cash-flow statement (year-to-date, so the quarter is a subtraction) and balance sheet; 10-Q Note 5 | correct | OK; the writer already notes the subtraction in outlook §1 |
| 7 | Shares outstanding; ATM proceeds | 10-Q cover; Note 12; cash-flow financing lines | correct | OK. If the ATM is not renewed the line reads zero, which is itself the signal |
| 8 | Neutron milestone language | Release highlights; 10-Q MD&A "Neutron Update"; call | correct | OK; qualitative by design, tracked as claims (§8 of AGENTS.md says to track one-off targets as claims, which the writer did in claims 7–8) |

None rests on a one-off number. The one-call figures (45.5% conversion, $50–55M ASP, "1, 3, 5", 400+ hot fires, headcount) are correctly kept out of the indicator list.

Jargon inside the indicator list (owner to reword at lock; reviewer did not touch): indicator 5 "vs the guided ranges" → "vs the ranges management forecast"; indicator 2 "absorbs its fixed cost" is fine after §3.

---

## 7. Rubric (§14), from the reader's chair

1. **What the company does and who pays, in two sentences?** Yes. §1–§2: it launches small rockets and builds satellites and their parts; U.S. government agencies and their prime contractors (47% of 2025 revenue) plus commercial satellite operators pay per launch, per satellite build or per component.
2. **What would kill it and the early warning?** Yes. §6 is ranked, each scenario has a sign, and the two that matter most (Neutron slipping; one government customer at 42%) have concrete, recurring signals.
3. **Why the margins are what they are and whether cost scales with usage?** Yes. §3's fixed-cost "absorption" story is sourced and shown with the cost-per-launch series; the mix explanation (70-point components vs mid-30s satellite builds) explains the Q3 guide-down.
4. **Could I predict next quarter's scorecard from §5 alone?** Yes for 11 of 12; claim 12 needs a judgment call on "mid-2027" vs "2027".
5. **Did nothing require knowledge I don't have?** Before fixes, no: bridge loan, reverse fee, prime contractors, gross margin, GAAP, convertible notes, unhedged, tails, MDA, QoQ, geostationary and Tier 1 all stopped the reader. After the reviewer's glosses, yes.

---

## 8. As-of check

- Grep of both drafts for dates after 2026-08-10 and for post-cutoff events (Q3 results, September/October 2026, S-4 filing, shareholder vote, Neutron pad arrival, launch 14+): none used as fact. The only post-cutoff date is the transcript page's publication date (2026-08-17), disclosed in both Sources tables and treated as a record of the 2026-08-10 call, consistent with MANIFEST.
- Every event cited is dated on or before 2026-08-10: Iridium agreement June 28 and 8-K June 29; Motiv May 26; Mynaric April 14; $266M contract July 21; Flatellite July 30; 10-Q and release August 10.
- **Iridium is described as pending throughout:** "the deal is pending, needs Iridium shareholder and regulatory approvals, and 'is expected to close in 2027'" (business l.10); "if it closes" (l.78); "Iridium pending" (§7 table l.123); "**Iridium (pending).**" (outlook l.35); claim 12 checks the closing expectation. No sentence treats Iridium's revenue, satellites or cash flow as Rocket Lab's.
- The writer correctly did not use the two 8-Ks filed 2026-08-13 (not in the cache) and did not fill the Q1 2026 10-Q gap with outside numbers (Q1 segment figures are computed by subtraction and labelled).

---

## 9. Length (§3 rule 7 method, `/tmp/wc_prose.py`)

| File | Before reviewer fixes | After reviewer fixes | Target |
|---|---|---|---|
| business.md | 2,965 prose words (tables 1,008; glossary + sources 457) | **3,069** (tables 1,023; glossary + sources 474) | 2,000–3,000 |
| outlook.md | 1,197 prose words (tables 433) | **1,226** (tables 436) | 800–1,200 |

Both drafts were inside the range on submission (upper edge). The reviewer's 25 glosses added 104 and 29 prose words, so both are now slightly over; REVISE 15 asks the writer to trim while making the other changes.

---

## 10. Verdict: REVISE

Numbered list for the writer. Numbers, quotes, claims, indicators and structure were not touched by the reviewer and must be changed by the writer.

1. **business.md §2, line 26.** "(earlier years not disclosed)" is wrong. 10-K-FY2023.txt line 813 (Item 1A) gives 33% for 2022 and 8% for 2021. Replace with: "U.S. government-related work was 8% of revenue in 2021, 33% in 2022, 31% in 2023, 33% in 2024 and 47% in 2025 [10-K FY2023, Item 1A; 10-K FY2025, Item 1A]". Optionally add it as a row of the §2 table (all five years are now available). Add `10-K FY2023, Item 1A` to the tag.
2. **outlook.md §3, line 31.** The $816 million / 18 satellites / 2029 figures belong to the Tranche 3 award alone (10-K-FY2025.txt line 1325: base $806M plus $10M options, signed December 17, 2025). Rewrite: "Space Development Agency (SDA) Tranche 2 and Tranche 3 (the Tranche 3 award alone is $816 million for 18 satellites, delivery 2029; Tranche 2's size is not in the sources)".
3. **business.md §5, line 82.** "after September 2023 the company lost revenue waiting for FAA clearance" is an inference. The source (10-K-FY2025.txt line 793) says the launch rate "will be negatively impacted if … not being granted appropriate government clearance after a launch failure such as occurred in … September 2023". Rewrite to the source: "after the September 2023 failure, launches could not resume until government clearance was granted [10-K FY2025, Item 1A]", or keep the revenue point and label it "our inference". Make §6#4 (line 102, "until the FAA cleared a return") consistent: the 10-K says "government clearance"; the FAA's licensing role is at line 711, which can be cited.
4. **business.md §8, indicators 1 and 3 (anchors).** Indicator 1: "10-Q Note 3 for the segment split" → "10-Q Item 2 'Backlog' paragraph for the total and the launch / space systems split; Note 3 'Backlog' for the total and the share expected within 12 months". Indicator 3: "'Key Factors'" → "'Key Metrics and Select Financial Data', sub-heading 'Revenue and Cost Per Launch'".
5. **business.md §4, line 78.** "$495 million of its own adjusted earnings" → "$495 million of what Iridium calls OEBITDA (operating profit before interest, tax, depreciation and some other items) on $871 million of 2025 revenue [Iridium deck 2026-06-29, p.6]". OEBITDA is not earnings.
6. **business.md §4 line 76 and §7 table line 122.** Net ATM proceeds for 6M 2026: the equity statement gives $1,512.8M (444,922 + 1,067,832), the 10-Q MD&A (line 2251) "$1,512.9 million". Keep one figure and say which statement it comes from, e.g. "(the 10-Q's MD&A rounds to $1,512.9 million)". The reviewer has already added "Item 1" to both tags.
7. **business.md §7, line 114.** "they convert automatically if he stops being CEO" is narrower than the certificate. 10-Q Note 12 (line 1461): conversion is triggered when he no longer serves as CEO "or such other executive officer position of the Company as approved by the Board", on death or permanent disability, on transfer, or if the preferred no longer represents 5% beneficial ownership. Suggested: "they convert automatically if he leaves the CEO job (or another board-approved executive role), dies or is disabled, or if his stake falls below 5%".
8. **business.md §7, line 116.** "a discretionary cash bonus, with no formula" — the proxy (DEF14A-2026.txt line 955) records a "Senior Executive Cash Incentive Bonus Plan" adopted August 25, 2025 with committee-set performance targets; no bonus was paid for 2025, and line 1247 says the Company "did not have a formal bonus program". Suggested: "a discretionary cash bonus (a bonus plan with committee-set targets was adopted in August 2025; nothing was paid for 2025)".
9. **business.md §4, line 76.** "only $13.4 million of debt remains" → "only $13.4 million of the convertible notes remains"; the balance sheet also carries $1.7 million of long-term borrowings and $14.5 million of finance-lease liabilities [10-Q Q2 2026, Item 1].
10. **outlook.md §3, line 29.** "whose revenue had largely been booked earlier" → "whose revenue had partly been booked in earlier quarters" (10-Q line 1813: "partially recognized in prior quarters"; CFO: "a significant portion").
11. **business.md §1 line 6 and glossary line 151.** "hypersonic-weapon development": the 10-K (line 321) says HASTE serves "hypersonic and suborbital system technology development"; the 10-Q (line 1769) says the Space Force contract supports "missile defense programs". Either use the sources' words ("hypersonic test flights for U.S. defence programs") or keep "weapon" and mark it as the writer's reading.
12. **outlook.md §5, claim 12.** Reduce to one condition and guard the wording. Suggested: "On the Q3 call, management's stated Iridium closing expectation is still mid-2027 or earlier; a later or vaguer date (for example '2027' alone) is a miss." Note the 10-Q already says "expected to close in 2027" (line 1765), so the Q3 10-Q's wording alone would not settle the grade.
13. **business.md §3 table footnote, line 44 (optional).** State that the FY2023–FY2025 operating-margin cells are the 10-K's own rounded percentages ((72.8)%, (43.6)%, (38.1)%; line 1455), which differ by 0.1 point from direct division (72.7 / 43.5 / 38.0), while FY2021–FY2022 and Q2 2026 are computed; or compute all six the same way.
14. **business.md §3, line 56.** "Neutron backlog in dollars or launches is not disclosed" → "No dollar figure for Neutron backlog is disclosed; the slides list about ten launch slots (one for Kepler, seven confidential, the Space Force Flatellite launch, NSSL, a U.S. Air Force experiment) [Q2 2026 slides, p.27], and the Q1 release counted 'five new dedicated Neutron launches signed' in Q1 [Q1 2026 release]".
15. **Length.** After the reviewer's glosses business.md is 3,069 prose words (target ≤ 3,000) and outlook.md 1,226 (≤ 1,200). Trim about 80 and 30 words. Candidates: business.md §6#7 and §6#8 (one sentence each), the §1 history paragraph (shell-company detail), the §5 closing caveat; outlook.md line 19 (year-ago comparisons) and the repeated "See business.md §3" framing in §3.
16. **Indicator list wording (owner at lock; not a writer item).** Indicator 5 "vs the guided ranges" → "vs the ranges management forecast".

---

## Fixed directly (jargon glosses and tag corrections only; no number, quote, claim, indicator, structure or factual sentence changed)

Line numbers unchanged (both files kept their line count). Backups of the pre-fix drafts: `/tmp/rklb-business.md.bak`, `/tmp/rklb-outlook.md.bak`. A before/after inventory of every numeric token in both files is identical.

business.md
- Line 6: after "hypersonic-weapon development" added "(hypersonic: over five times the speed of sound; suborbital: see Glossary)".
- Line 8: "prime contractors" → "prime contractors (lead contractors that hire subcontractors)".
- Line 10: tag `[10-Q Q2 2026, Note 1; Item 2]` → `[10-Q Q2 2026, Note 1; Item 2; 8-K 2026-06-29]`; the "voice-and-data" description of Iridium's network is from the 8-K press release (8-K-2026-06-29.txt line 450, "global voice, data, and positioning, navigation, and timing (PNT) satellite services").
- Line 30: "about a 41% gross margin" → "about a 41% gross margin (revenue left after direct costs, as a share of revenue)".
- Line 44 (table footnote): appended "GAAP is the standard U.S. accounting rulebook; operating margin is revenue left after all running costs, including R&D and SG&A."
- Line 46: after the CFO quote ending "to build out for Neutrons" added "(tails: individual rockets)".
- Line 48: "capex" → "capex (cash spent on equipment, buildings and launch sites)".
- Line 70 (§4 table label): "Gross proceeds from ATM share sales" → "Gross proceeds from ATM share sales (at-the-market, see below)".
- Line 74 (footnote): "no marketable securities" → "no marketable securities (short-term investments that can be sold quickly)".
- Line 76: tag `[10-K FY2025, Item 8; Note 13; 10-Q Q2 2026, Item 2; Note 12]` → `[… 10-Q Q2 2026, Item 1; Item 2; Note 12]` (the $1,512.8M is the equity statement's figure); "2029 convertible notes" → "2029 convertible notes (bonds that holders may swap for shares)".
- Line 82: "FAA clearance" → "FAA (the U.S. launch-licensing regulator) clearance".
- Line 86: "on the MDA program the customer 'is potentially entitled to claim liquidated damages' for late delivery" → "on the program for MDA Corporation, a satellite-maker customer, MDA 'is potentially entitled to claim liquidated damages' (a pre-agreed penalty) for late delivery".
- Line 106: "bridge loan" → "bridge loan (a short-term loan to be refinanced later)"; "no reverse fee is described" → "no reverse fee (a fee Rocket Lab would owe if it walked away) is described".
- Line 108: "unhedged" → "unhedged (not insured against currency swings)".
- Line 114: tag `[8-K 2026-03-30; 10-Q Q2 2026, Note 13]` → `[8-K 2026-03-30; 10-Q Q2 2026, Note 13; DEF 14A 2026, Summary Compensation Table]`; the $800,000 salary is at DEF14A-2026.txt line 1107, not in the 8-K.
- Line 122 (§7 table): tag `[10-K FY2025, Item 8; 10-Q Q2 2026, Item 2]` → `[10-K FY2025, Item 8; 10-Q Q2 2026, Item 1; Item 2]`.
- Line 125 (§7 table label): "Goodwill" → "Goodwill (the premium paid over the book value of acquired businesses)".
- Line 151 (glossary, HASTE): "on suborbital arcs for hypersonic-weapon development" → "on suborbital arcs (up and back down without completing an orbit) for hypersonic-weapon development (hypersonic: more than five times the speed of sound)".

outlook.md
- Line 10 (§1 table): after "up 20.2% QoQ" added "(quarter on quarter)".
- Line 23: after the "self-launching Tier 1 space power …" quote added "(Tier 1: top-rank)"; after the "constellation from scratch" quote added "(constellation: a fleet of satellites working as one network)".
- Line 31: "three geostationary satellites" → "three geostationary satellites (satellites that hover over one spot on Earth)".
- Line 33: after "an insolvency process" added "(bankruptcy)".
- Line 41: after the slides quote added "(mix: which products make up the quarter's sales)".

Not fixed (outside the reviewer's remit): everything in §10; the "hypersonic-weapon" wording itself (a factual choice, REVISE 11); claim 4's "basic weighted-average shares".

---

## Cycle 2 (re-check of the writer's second pass; review cycle 2 of 2)

_Re-checked 2026-09-07 against `sources/2026-Q2/` only. Method: the reviewer's cycle-1 glosses were re-applied to the pre-fix backups to rebuild the post-cycle-1 drafts (`/tmp/rklb-business.postgloss.md`, `/tmp/rklb-outlook.postgloss.md`), and the current drafts were diffed against those at line and word level, so every change below is the writer's. Line numbers are the current drafts' (business.md 173 lines, outlook.md 70 lines)._

### 1. Status of the 15 REVISE items

| # | Item | Status | Where | Note (source verified) |
|---|---|---|---|---|
| 1 | "(earlier years not disclosed)" for government-revenue share | **Resolved** | business.md §2 table l.23, footnote l.25, prose l.27 | New table row "U.S. government-related share of revenue: 8% / 33% / 31% / 33% / 47% / n/d / n/d". 10-K-FY2023.txt line 813: "31%, 33% and 8%" for 2023, 2022, 2021; 10-K-FY2025.txt line 705: "47%, 33%, and 31%" for 2025, 2024, 2023. Tags `[10-K FY2023, Item 1A; 10-K FY2025, Item 1A]` added; "n/d = not disclosed for interim periods" is correct (the 10-Q gives only the single "Government customer" 42%) |
| 2 | Tranche 3 figures attributed to Tranche 2 and 3 | **Resolved** | outlook.md §3 l.31 | "the Tranche 3 award alone is $816 million for 18 satellites, delivery 2029; Tranche 2's size is not in the sources". 10-K-FY2025.txt line 1325 |
| 3 | "lost revenue waiting for FAA clearance" (inference as fact) | **Resolved** | business.md §5 l.83; §6#4 l.103 | Now "each past failure stopped launches until the cause was found and the FAA, the U.S. launch-licensing regulator, authorized a return". 10-K-FY2025.txt line 775: "prevented us from conducting future launches until we had investigated the cause of the failures and obtained authorization from the Federal Aviation Administration to resume launches". §6#4 changed "cleared" to "authorized" for consistency |
| 4 | Indicator 1 and 3 anchors | **Resolved** | business.md §8 l.136, l.138 | Indicator 1: Item 2 "Backlog" paragraph for total and split; Note 3 for total and 12-month share (10-Q lines 1841, 761). Indicator 3: "Key Metrics and Select Financial Data", sub-heading "Revenue and Cost Per Launch" (10-Q lines 1797, 1819) |
| 5 | "$495 million of adjusted earnings" | **Resolved** | business.md §4 l.79 | "$495 million of what Iridium calls OEBITDA (operating profit before interest, tax, depreciation and some other items)". Deck lines 124–130 ($495M, "2025 OEBITDA"), definition at line 147 |
| 6 | $1,512.8M vs $1,512.9M net ATM proceeds | **Resolved** | business.md §4 l.77; §7 table l.123 | Now $1,512.9M, labelled as the 10-Q's management-discussion figure. 10-Q line 2251: "$1,512.9 million of net proceeds from the issuance of common stock under the ATM Equity Offerings". Tags keep Item 1 and Item 2 |
| 7 | Preferred auto-conversion triggers | **Resolved** | business.md §7 l.115 | "if he leaves the CEO job (or another board-approved executive role), dies or is disabled, or if his stake through them falls below 5%". 10-Q line 1459 (b)–(d). The transfer trigger (a) is omitted; immaterial for the reader |
| 8 | "with no formula" bonus | **Resolved** | business.md §7 l.117 | "a bonus plan with committee-set targets was adopted in August 2025, but for 2025 there were 'No base salary increases' and 'No discretionary cash bonuses'". DEF14A-2026.txt line 955 (Bonus Plan adopted August 25, 2025; performance targets set by the Compensation Committee; no 2025 payout), lines 717, 719 |
| 9 | "only $13.4 million of debt remains" | **Resolved** | business.md §4 l.77 | "only $13.4 million of the convertible notes remains, beside $1.7 million of other borrowings and $14.5 million of finance-lease liabilities". 10-Q Note 11 line 1451 ($13,366 principal); balance sheet lines 265 (1,716), 269 (14,468) |
| 10 | "largely been booked earlier" | **Resolved** | outlook.md §3 l.29 | "partly been booked in earlier quarters" matches 10-Q line 1813 "partially recognized in prior quarters" |
| 11 | "hypersonic-weapon development" | **Resolved** | business.md §1 l.6; glossary l.152 | Now quotes the 10-K: "hypersonic and suborbital system technology development" (10-K-FY2025.txt line 321, verbatim), "including missile-defence testing for the Space Force" (10-Q line 1769: "12 suborbital launches supporting missile defense programs" for the U.S. Space Force) |
| 12 | Claim 12 double-barreled; "mid-2027" fragile | **Resolved** | outlook.md §5 l.58 | Single condition ("still mid-2027 or earlier"), explicit fail rule ("a later or vaguer date … is a miss"), both quotes verbatim: transcript line 36; 10-Q line 2181 "expected to close in 2027" |
| 13 | Operating-margin method mixed across columns | **Resolved** | business.md §3 table l.41, footnote l.45 | Row relabelled "(computed)"; FY2023–25 now (72.7)% / (43.5)% / (38.0)%, which match direct division (−177,918/244,592 = −72.74; −189,801/436,214 = −43.51; −228,838/601,799 = −38.03). Footnote: "the 10-K's own rounding gives (72.8)%, (43.6)% and (38.1)%" (10-K-FY2025.txt line 1453) |
| 14 | "Neutron backlog in dollars or launches is not disclosed" | **Resolved** | business.md §3 l.57 | "no dollar figure for Neutron backlog is disclosed, but a slide (gatherer visual read) lists ten launches …". slides.txt line 698 (p.27 visual read): 1 Kepler + 7 confidential + SB-AMTI + U.S. Air Force experiment = 10, plus NSSL provider status; line 675 (p.26): Kepler "Launching NET 2028"; press-release-2026-Q1.txt line 19: "five new dedicated Neutron launches signed" (verbatim). The chart-read flag is present |
| 15 | Length | **Resolved** | both files | 2,917 / 1,164 prose words as submitted (reviewer count agrees); 2,928 / 1,164 after the two cycle-2 glosses below. Both inside 2,000–3,000 and 800–1,200 |
| 16 | Indicator 5 wording (owner item, not a writer item) | Unchanged, as expected | business.md §8 l.140 | "vs the guided ranges" stands for the owner to reword at lock |

**15 of 15 resolved.**

### 2. New and changed numbers and quotes (every changed sentence, from the word-level diff)

| Item | Draft value | Source (file, line) | Result |
|---|---|---|---|
| §2 table row: government-related share 8 / 33 / 31 / 33 / 47 | as tagged | 10-K-FY2023.txt 813; 10-K-FY2025.txt 705 | PASS |
| §2 l.27 "rose from 8% of revenue in 2021 to 47% in 2025" | 8% → 47% | same | PASS |
| §1 l.6 HASTE quote and "missile-defence testing for the Space Force" | quote | 10-K-FY2025.txt 321 (verbatim); 10-Q 1769 | PASS |
| §1 l.10 "bought four component makers in 2020–2022 (Sinclair Interplanetary, Advanced Solutions, Planetary Systems, SolAero)" | four; 2020–2022 | 10-K-FY2025.txt 275 (April 2020, October 2021, November 2021, January 2022) | PASS |
| §1 l.10 "reorganized under a new parent … in May 2025 … GEOST (2025), Mynaric and Motiv (2026)" | dates | 10-Q Note 1 line 631; Note 4 lines 785, 861, 943 | PASS |
| §3 l.31 "launches rose from 6 in 2021 to 21 in 2025" | 6; 21 | 10-K-FY2023.txt 1523; 10-K-FY2025.txt 1361 | PASS |
| §3 table l.41 operating margins (72.7) / (43.5) / (38.0) (computed) | recomputed | income statements (10-K-FY2025.txt 2325, 2347) | PASS |
| §3 footnote l.45 "the 10-K's own rounding gives (72.8)%, (43.6)% and (38.1)%" | as stated | 10-K-FY2025.txt 1453 | PASS |
| §3 l.49 CFO "to remain elevated" | fragment | transcript.txt 86 | PASS |
| §3 l.53 Neutron "two-stage, 43-meter … about 13,000 kg … Archimedes … Launch Complex 3 … licensed for two launches a year" | specs | 10-K-FY2025.txt 325, 327, 449 | PASS |
| §3 l.55 10-Q quote now ends at "… ready for full-scale production" | truncated quote | 10-Q 1759 (verbatim up to the cut; the source sentence continues "and high-cadence launch beyond flight one") | PASS; a trailing ellipsis would be more exact (owner note) |
| §3 l.57 "ten launches" on slide; Kepler "no earlier than 2028"; "7x confidential customer launches"; Flatellite "to launch on Neutron"; "five new dedicated Neutron launches signed" | counts and quotes | slides.txt 698 (p.27), 675 (p.26); press-release.txt 21; press-release-2026-Q1.txt 19 | PASS |
| §4 l.77 "$1,512.9 million net … four successive programs, the latest $3 billion" | $1,512.9M; four; $3B | 10-Q 2251; Note 12 lines 1475–1487 (March 2025, September 2025, March 2026, May 2026) | PASS |
| §4 l.77 "$13.4 million of the convertible notes … $1.7 million of other borrowings … $14.5 million of finance-lease liabilities" | 13.4 / 1.7 / 14.5 | 10-Q 1451 (13,366), 265 (1,716), 269 (14,468) | PASS |
| §4 l.79 "Adjusted EBITDA losses have narrowed from $27.6 million … to $11.8 million … and $8.8 million" | same numbers, new framing | press-release.txt 251; press-release-2026-Q1.txt 247 | PASS |
| §4 l.79 "$495 million of what Iridium calls OEBITDA … on $871 million" | 495; 871 | supplemental-iridium-deck.txt 124–130, 147 | PASS |
| §5 l.83 FAA authorization wording | paraphrase | 10-K-FY2025.txt 775 | PASS |
| §5 l.85 "makes 'many components and subsystems for our launch vehicles and family of spacecraft'" | fragment | 10-K-FY2025.txt 403 | PASS |
| §5 l.91 competitor list rephrased | names | 10-K-FY2025.txt 463 | PASS |
| §6#2 l.99 "top five customers were 49% of FY2025 revenue, and the top five backlog customers 77% of year-end backlog" | 49; 77 | 10-K-FY2025.txt 715 | PASS |
| §6#4 l.103 "until the FAA authorized a return" | paraphrase | 10-K-FY2025.txt 775 | PASS |
| §6#6 l.107 "plus up to 'approximately $1.8 billion' to refinance Iridium's loans"; bridge gloss "(a short-term loan to be replaced by permanent debt or equity)"; "If Iridium walks away in specified cases it owes a $223.62 million fee; no such fee is described for Rocket Lab" | as stated | 10-Q 2181 ("if necessary"), 2327, 2331; 8-K-2026-06-29.txt 196, 180–205 | PASS |
| §6#7 l.109 "built and mainly launched in New Zealand"; "15% of FY2025 spending" | as stated | 10-K-FY2025.txt 409, 239; 941 ("approximately 15%") | PASS on the numbers; the source's "approximately" was dropped (owner note) |
| §6#8 l.111 key-person quote trimmed | fragment | 10-K-FY2025.txt 921 | PASS |
| §7 l.115 preferred conversion triggers | paraphrase | 10-Q 1459 | PASS |
| §7 l.117 "a bonus plan with committee-set targets was adopted in August 2025" | paraphrase | DEF14A-2026.txt 955 | PASS |
| §7 table l.123 "$1,512.9M in 6M 2026" | 1,512.9 | 10-Q 2251 | PASS |
| §8 l.136, l.138 anchors | headings | 10-Q 1841, 761, 1797, 1819 | PASS |
| Glossary l.152 HASTE | quote | 10-K-FY2025.txt 321 | PASS |
| outlook l.19 year-ago line (trimmed) | $144.5M; $46.6M; $97.9M; 36.9%; $27.6M; five; 137% | press-release.txt 81, 266, 251, 16; 10-Q 1649, 1813 | PASS |
| outlook l.23 trimmed quotes ("space applications"; "not the endpoint … starting point") | fragments | transcript.txt 28, 268 | PASS |
| outlook l.29 "partly been booked in earlier quarters"; Kodiak clause removed | wording | 10-Q 1813 | PASS |
| outlook l.31 Tranche 3 sentence; "(July 30)" | $816M; 18; 2029; July 30 | 10-K-FY2025.txt 1325; 10-Q 1773 | PASS |
| outlook l.41 cash quote now ends at "elevated levels" | fragment | transcript.txt 96 | PASS |
| outlook l.43 "Full year 2026: none in the release, slides or call" | absence | grep of all three files: no full-year figure | PASS |
| outlook claims 7, 10, 12 | quotes | press-release.txt 20; transcript.txt 80 (leading ellipsis, verbatim fragment), 36; 10-Q 2181 | PASS |

No new number or quote fails. Deleted content checked: the 15,000-kg spec change and LC-3 "potential for an increased number of missions" quote (§3), the $12.8M FY2025 revenue adjustment (§6#3), the CEO's hobbies quote (§6#8), the "We streamline it" quote (§7), the "diverse mix" quote (§1), "Component revenue is not disclosed separately" (outlook §3) and the second Iridium quote in outlook §2. None was required skeleton content; §6#3 keeps its early-warning sign.

### 3. Skeleton, tags and trimming

- All §6 headings present in order (§1–§8, Glossary, Sources; "### Neutron" retained as a permitted subsection); §1 history paragraph intact; §2 table now six rows over five fiscal years; §3 and §4 tables intact; `_Proposed — owner to review and lock._` at line 132. All §7 headings present in outlook.md; §6 Tone shift still omitted.
- Tags: business.md uses 11 prefixes (10-K FY2025, 10-Q Q2 2026, 10-K FY2023, Q2 2026 call, DEF 14A 2026, Q2 2026 release, Q1 2026 release, Q2 2026 slides, Iridium deck 2026-06-29, 8-K 2026-06-29, 8-K 2026-03-30); the Sources table has the same 11 rows. outlook.md uses 7; Sources has 7. No orphan tag, no unused row.
- Every factual sentence on a changed line still ends in a tag; the only untagged sentences are the writer's own "Weakening sign" and "Early warning" judgments, as before. Where sentences were merged, the tags were merged (e.g., §1 l.10 now carries `[10-K FY2025, Item 1; Note 4; 10-K FY2023, Note 4; 10-Q Q2 2026, Note 4]`).
- Banned-word sweep: none. As-of sweep: no post-cutoff fact; Iridium still "pending" at l.10, l.79, l.107, l.124 and outlook l.35.

### 4. Cycle-1 direct edits

Intact (18 of 20 in business.md, 6 of 6 in outlook.md): hypersonic/suborbital gloss (l.6); 8-K tag (l.10); gross-margin gloss (l.31); GAAP / operating-margin footnote (l.45); "tails" (l.47); capex (l.49); ATM table label (l.71); marketable securities (l.75); Item 1 tag and convertible-notes gloss (l.77); MDA and liquidated-damages glosses (l.87); unhedged (l.109); DEF 14A tag (l.115); Item 1 tag (l.123); goodwill label (l.126); glossary HASTE definitions (l.152); outlook QoQ, Tier 1, constellation, geostationary, bankruptcy, mix.

Not surviving verbatim, replacement acceptable:
- "prime contractors (lead contractors that hire subcontractors)" (old §1 l.8): the sentence was rewritten and the term now appears only in the §2 footnote (l.25). Re-glossed there in cycle 2 (see below).
- "reverse fee (a fee Rocket Lab would owe if it walked away)" (§6#6): replaced by "no such fee is described for Rocket Lab", which says the same thing without the term. Acceptable.
- "bridge loan (a short-term loan to be refinanced later)": reworded to "(a short-term loan to be replaced by permanent debt or equity)". Acceptable, closer to 10-Q line 2327.
- "FAA (the U.S. launch-licensing regulator)": reworded to "the FAA, the U.S. launch-licensing regulator". Same gloss.

### 5. Claims (outlook §5)

- 12 (rewritten): one condition, tied to the Q3 call, explicit fail rule, two verbatim quotes. Met if "mid-2027" or earlier is restated; Missed if a later or vaguer date is given; Dropped if silent. Passes §9.
- 7 (tightened): "Management, on the Q3 call and in the Q3 10-Q, still targets Neutron pad delivery in Q4 2026; a later target is a miss." Single direction; gradeable from either document.
- 10 (quote trimmed): "... which will be reflected in our Q3 backlog." is a verbatim fragment of transcript line 80 with a leading ellipsis; disclosure-check label and quarter-end wording unchanged.
- 1–6, 8, 9, 11: unchanged. Count 12; four headline, eight fundamental. None flagged.

### 6. Word counts (`/tmp/wc_prose.py`)

- business.md: 2,917 as submitted (matches the writer's figure); **2,928** after the two cycle-2 glosses. Target 2,000–3,000.
- outlook.md: **1,164** (matches). Target 800–1,200.

### Fixed directly in cycle 2 (glosses only; numbers, quotes, claims, indicators and structure untouched; numeric-token inventory before/after identical; line counts unchanged)

- business.md l.25 (§2 footnote): "its prime contractors" → "its prime contractors, the lead contractors that hire subcontractors" (restores the cycle-1 gloss at the term's new location).
- business.md l.77: "(the 10-Q's MD&A figure)" → "(the figure in the 10-Q's management discussion, or MD&A)".
- business.md l.123 (§7 table): "(10-Q MD&A figure)" → "(10-Q management-discussion figure)".

Pre-fix copies of the cycle-2 drafts: `/tmp/rklb-business.cycle2-prefix.md`, `/tmp/rklb-outlook.cycle2-prefix.md`.

### Notes for the owner (not failures; no third cycle)

1. business.md l.109: the 10-K says "approximately 15%" of 2025 expenditures were in foreign currencies (line 941); the draft now says "15%".
2. business.md l.55: the 10-Q quote is cut at "full-scale production" without an ellipsis; the source sentence continues "and high-cadence launch beyond flight one".
3. business.md §8 indicator 5: "vs the guided ranges" → "vs the ranges management forecast" at lock.
4. business.md l.115 omits the preferred stock's transfer-to-a-non-permitted-holder conversion trigger (10-Q line 1459 (a)); immaterial.

### Final verdict: **PASS**

All four cycle-1 FAILs are resolved with correct sources, the eleven wording items are resolved, no new number or quote fails, both files are inside the length targets, and the claims list is mechanically gradeable.
