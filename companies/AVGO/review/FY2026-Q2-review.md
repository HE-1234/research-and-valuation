# Broadcom Inc. (AVGO) — Reviewer report, Q2 FY2026 (quarter ended May 3, 2026)

_Review cycle 1 of 2. Reviewed 2026-09-07 against `sources/FY2026-Q2/` only (cutoff 2026-06-09: release and call 2026-06-03, 10-Q filed 2026-06-09). Every number at stake was checked against the cached source TEXT (10-K-FY2025.txt, 10-K-FY2023.txt, 10-Q-FY2026-Q2.txt, DEF14A-2026.txt, press-release.txt, press-release-FY2026-Q1.txt, transcript.txt, four 8-K files), not the notes. Word counts by `python3 -P /home/ubuntu/avgo-work/wc_prose.py`: business.md 2,541 before fixes / 2,600 after; outlook.md 1,015 before / 1,018 after._

**Verdict: PASS.** Citation spot-check: 109 items (every cell of the five tables, every guidance quote, every claim quote, 44 prose sentences and quote blocks), 108 PASS, 1 FAIL (a 10-Q quote that paraphrased the source inside quotation marks; corrected directly). Every table number and every computed percentage re-derives exactly. All 35 transcript quotes are character-for-character, none of them sits in a passage flagged as garbled, and the "$56 billion" and "in excess of $100 billion" figures come from the prepared remarks, not the garbled Q&A. Nothing after 2026-06-09 is used. The remaining issues were jargon (fixed directly, listed in "Direct fixes") and a handful of optional notes for the owner or the next refresh.

---

## 1. Rubric result (§14)

| # | Question | Answer | Reasoning |
|---|---|---|---|
| 1 | Can I explain what this company does, and who pays it, in two sentences? | **Yes** | §1 opens with "two businesses under one roof": chips made at TSMC and sold to cloud giants and equipment makers through distributors; VMware and other software sold on multi-year contracts to large enterprises. |
| 2 | Do I know exactly what would kill it, and what the early warning sign is? | **Yes** | §6 ranks eight scenarios; each of 1, 2, 3, 5, 6 has a named early warning tied to a filing line (concentration percentages, inventory and commitments vs RPO, new backstops in 10-Q notes, software growth vs guidance, risk-factor wording). §6 #4 (Taiwan) says honestly that the filings offer no early warning. |
| 3 | Do I know why the margins are what they are, and whether cost scales with usage? | **Yes** | §3 states it plainly: chips need a wafer per unit (cost rises with volume, ~70% gross margin), software costs almost nothing extra per customer (93%), R&D is the fixed cost, and the mix shift toward custom accelerators lowers gross margin while raising operating margin. The two-set-of-margins paragraph explains GAAP vs non-GAAP. |
| 4 | Could I predict what the scorecard will check next quarter, from §5 of the outlook alone? | **Yes** | Eleven claims, each with a number or an observable event, the source column named (release segment table, release reconciliation, 10-Q quarter column), and the one sharpening labelled. |
| 5 | Did nothing in the report require knowledge I don't have? | **Yes, after fixes** | Before fixes, "IP", "proxy", "gross margin", "operating income", "principal", "notes", "EPS", "H1" and "carrying value" were used without a gloss, and the glossary defined "hypervisor" (a term never used in the text) and used "impaired" inside a definition. All fixed directly; see "Direct fixes". |

## 2. Skeleton and rules check

**business.md**

| Requirement | Result |
|---|---|
| `# <Company> — The Business`; `_As of <QLABEL>. Written <date>._` with calendar parenthetical on first use | OK: "Q2 FY2026 (quarter ended May 3, 2026). Written 2026-09-07." |
| §1–§8 headings present, in order, none skipped | OK (lines 4, 14, 32, 63, 88, 96, 116, 134). §1 has the history paragraph; §6 carries customer concentration (#1); §8 has name / why / where for each indicator |
| `_Proposed — owner to review and lock._` under §8 | OK (line 136) |
| §2 segment table, five fiscal years | OK: FY2021–FY2025 plus Q2 FY2026, plus the management "AI semiconductor revenue" row marked n/d where not disclosed |
| §3 table: revenue, gross margin, operating margin, capex, capex/revenue, five years | OK, plus non-GAAP rows and R&D %; second table gives segment operating margins |
| §4 table, five years | OK (12 rows FY2021–FY2025 + H1 FY2026) |
| §7 capital-allocation table | OK, five years + H1 |
| Glossary, Sources | Both present. Sources maps all 11 tag prefixes to cached files and records the transcript tier and garble caveat |
| Length 2,000–3,000 (aim lower half) | 2,600 after fixes: in range, upper half. Not a deviation; noted for the writer |
| Indicators anchored to recurring disclosures (§8) | OK. #1, #3, #4, #5, #6, #7, #8 are income-statement, balance-sheet, segment-note, revenue-note or MD&A lines that appear every quarter. #2 (AI semiconductor revenue) is a management figure, but it has appeared in the CEO quote of every release in the sources (Q1 and Q2 FY2026) and the proxy, and the draft says so explicitly. Acceptable; if management ever drops it, that is itself the signal |

**outlook.md**

| Requirement | Result |
|---|---|
| `# <Company> — Outlook as of <QLABEL>` with calendar parenthetical | OK |
| `_Transcript source tier: … Written <date>._` | OK: "third-party (The Motley Fool)", matches MANIFEST tier 3 |
| §1 table, one row per proposed indicator, columns this quarter / last quarter / what management said | OK, 8 rows, all three columns filled; gaps ("Q1 10-Q not among sources") stated rather than guessed |
| §2, §3, §4 (verbatim guidance), §5 | OK |
| §6 Tone shift omitted on first run | OK, correctly omitted |
| Sources | OK, 6 tag prefixes mapped |
| Length 800–1,200 | 1,018 after fixes |
| Claims 6–12; single direction; one thing to check; verbatim quote and tag under each | OK: 11 claims. None is either/or. Each has a number or event and a quote with tag. Claim 5 labels its 73–75% band as "our sharpening ... not management's number". Claims 10 and 11 are labelled "(Disclosure check, not a management claim.)"; claim 11 states "in the quarter column"; claim 10 is a period-end balance (RPO), so quarter vs YTD does not arise — the writer could say so in three words next time. Six of eleven claims are guidance numbers, but four of those are the segment-level and margin-structure items §9 prefers, and claims 7–11 are targets, a product milestone and two filing checks. Headline revenue and EPS do not dominate |

## 3. Citation spot-check

Legend: PASS / FAIL. Line numbers refer to the cached `.txt` files. Every "(computed)" cell was re-derived from the cited source figures.

### 3a. business.md §2 segment table (every cell)

| # | Row | Source | Found at | Result |
|---|---|---|---|---|
| A1 | Semiconductor 20,383 / 25,818 / 28,182 / 30,096 / 36,858 / 15,009 | 10-K FY2023 Note 12; 10-K FY2025 Note 13; 10-Q Note 9 | 10-K-FY2023 line 3545; 10-K-FY2025 line 3585; 10-Q line 1421 | PASS |
| A2 | Software 7,067 / 7,385 / 7,637 / 21,478 / 27,029 / 7,178 | same | 10-K-FY2023 line 3547; 10-K-FY2025 line 3597; 10-Q line 1423 | PASS |
| A3 | Total 27,450 / 33,203 / 35,819 / 51,574 / 63,887 / 22,187 | same | 10-K-FY2023 line 3549; 10-K-FY2025 line 3609; release line 160 | PASS |
| A4 | Share (computed) 74 / 78 / 79 / 58 / 58 / 68 | — | 74.3 / 77.8 / 78.7 / 58.4 / 57.7 / 67.6 | PASS |
| A5 | AI row 12.2 / 20.2 / 10.8 | DEF 14A Proxy Statement Summary; release | DEF14A line 235 ("from $12.2 billion in fiscal 2024 to $20.2 billion in fiscal 2025"); release line 32 | PASS |

### 3b. business.md §3 economics table

| # | Row | Found at | Result |
|---|---|---|---|
| B1 | Gross margin GAAP (computed) 61.4 / 66.5 / 68.9 / 63.0 / 67.8 / 69.5 | Gross margin 16,844 / 22,095 / 24,690 (10-K-FY2023 line 1917); 32,509 / 43,294 (10-K-FY2025 line 1675); 15,415 (release line 172) | PASS (61.36 / 66.54 / 68.93 / 63.03 / 67.77 / 69.48) |
| B2 | Non-GAAP gross margin Q2 77.1 | release line 236: 17,109 / 22,187 = 77.11 | PASS |
| B3 | Operating margin GAAP (computed) 31.0 / 42.8 / 45.2 / 26.1 / 39.9 / 48.6 | Operating income 8,519 / 14,225 / 16,207 (10-K-FY2023 line 1929); 13,463 / 25,484 (10-K-FY2025 line 1687); 10,788 (release line 184) | PASS (31.03 / 42.84 / 45.25 / 26.10 / 39.89 / 48.62) |
| B4 | Operating margin non-GAAP (computed) 61.8 / 59.6 / 65.7 / 67.3 | DEF14A line 2607: 41,997 / 30,736 / 22,125; release line 274: 14,928 | PASS (61.77 / 59.60 / 65.73 / 67.28) |
| B5 | R&D % (computed) 17.7 / 14.8 / 14.7 / 18.1 / 17.2 / 13.5 | R&D 4,854 / 4,919 / 5,253 (10-K-FY2023 line 1919); 9,310 / 10,977 (10-K-FY2025 line 1677); 2,995 (release line 174) | PASS |
| B6 | Capex 443 / 424 / 452 / 548 / 623 / 231 | 10-K-FY2023 line 2043; 10-K-FY2025 line 1811; release line 360 | PASS |
| B7 | Capex / revenue (computed) 1.6 / 1.3 / 1.3 / 1.1 / 1.0 / 1.0 | recomputed 1.61 / 1.28 / 1.26 / 1.06 / 0.98 / 1.04 | PASS |
| B8 | Segment op. margin (computed): semi 53.8 / 58.4 / 58.5 / 55.7 / 57.6 / 61.8; software 69.8 / 70.7 / 73.8 / 65.1 / 76.8 / 78.7 | Segment operating income 10,976 / 15,075 / 16,486 and 4,936 / 5,219 / 5,639 (10-K-FY2023 lines 3553, 3555); 16,759 / 21,232 and 13,977 / 20,765 (10-K-FY2025 lines 3593, 3605); 9,281 and 5,647 (10-Q lines 1495, 1497) | PASS (all twelve re-derive to the stated decimal) |
| B9 | Unallocated (7,393) / (6,069) / (5,918) / (17,273) / (16,513) / (4,140) | 10-K-FY2023 line 3557; 10-K-FY2025 line 1367; 10-Q line 1499 | PASS |

### 3c. business.md §4 cash table (every cell)

| # | Row | Found at | Result |
|---|---|---|---|
| C1 | Operating cash flow 13,764 / 16,736 / 18,085 / 19,962 / 27,537 / 18,753 | 10-K-FY2023 line 2035; 10-K-FY2025 line 1803; release line 358 | PASS |
| C2 | Free cash flow (computed) 13,321 / 16,312 / 17,633 / 19,414 / 26,914 / 18,272 | OCF minus capex; release line 362 states 18,272 | PASS |
| C3 | FCF / revenue (computed) 48.5 / 49.1 / 49.2 / 37.6 / 42.1 / 44.0 | recomputed 48.53 / 49.13 / 49.23 / 37.64 / 42.13 / 44.03 (H1 revenue 41,498, release line 160) | PASS |
| C4 | Net income 6,736 / 11,495 / 14,082 / 5,895 / 23,126 / 16,659 | 10-K-FY2023 line 1939; 10-K-FY2025 line 1701; release line 194 | PASS |
| C5 | Stock-based compensation 1,704 / 1,533 / 2,171 / 5,741 / 7,568 / 4,268 | 10-K-FY2023 line 2011; 10-K-FY2025 line 1779; release line 458 | PASS |
| C6 | Amortization of acquired intangibles (computed, both lines) 5,403 / 4,359 / 3,247 / 9,267 / 8,062 / 3,936 | 3,427+1,976; 2,847+1,512; 1,853+1,394 (10-K-FY2023 lines 1911, 1923); 6,023+3,244; 6,031+2,031 (10-K-FY2025 lines 1669, 1681); 2,923+1,013 (release lines 166, 178); 10-K-FY2025 line 3619 states 8,062 / 9,267 / 3,247 directly | PASS |
| C7 | Cash interest paid 1,565 / 1,386 / 1,503 / 3,250 / 2,672 / 1,314 | 10-K-FY2023 line 2079; 10-K-FY2025 line 1847; release line 524 | PASS |
| C8 | Dividends paid 6,212 / 7,032 / 7,645 / 9,814 / 11,142 / 6,178 | "Payments of dividends" 10-K-FY2023 line 2059; 10-K-FY2025 line 1827; release line 504. FY2021–FY2022 include preferred dividends (299, 272), which the row label "(common and preferred)" correctly says | PASS |
| C9 | Repurchases, program — / 7,000 / 5,824 / 7,176 / 2,450 / 8,450 | 10-K-FY2023 line 2061; 10-K-FY2025 line 1829; release line 506 | PASS |
| C10 | Shares bought for employee tax 1,299 / 1,455 / 1,861 / 5,216 / 3,860 / — | 10-K-FY2023 line 2063; 10-K-FY2025 line 1831; release line 508 ("—") | PASS |
| C11 | Debt principal n/s / 41,218 / 40,815 / 69,847 / 67,120 / 66,720 | 10-K-FY2023 line 3095; 10-K-FY2025 line 3173; 10-Q line 999. FY2021 not stated in either 10-K | PASS |
| C12 | Table note "Free cash flow = operating cash flow minus capex" | release line 20 | PASS |

### 3d. business.md §7 capital-allocation table

| # | Row | Found at | Result |
|---|---|---|---|
| D1 | Dividends per share 1.44* / 1.64* / 1.840 / 2.105 / 2.360 / 1.30 | 10-K-FY2023 line 3225: 18.40 / 16.40 / 14.40; 10-K-FY2025 line 3263: 2.360 / 2.105 / 1.840; 10-Q line 1075: 1.30 | PASS. The 10-for-1 factor is correctly labelled an inference in the footnote; the 10-K FY2025 says "on a split adjusted basis" (lines 1935, 2181) without stating the ratio, and 18.40 vs 1.840 for FY2023 fixes it |
| D2 | Acquisitions 8 / 246 / 53 / 25,978 / — / — | 10-K-FY2023 line 2039; 10-K-FY2025 line 1807; Q2 release cash flow has no acquisitions line | PASS |
| D3 | Net borrowing (computed) (1,591) / (426) / (403) / 20,346 / (2,812) / (426) | Proceeds 9,904 / 1,935 / — and payments (11,495) / (2,361) / (403) (10-K-FY2023 lines 2055, 2057); 39,954 / 15,666 and (19,608) / (18,478) (10-K-FY2025 lines 1823, 1825); 4,474 and (4,900) (release lines 498, 500) | PASS |
| D4 | Shares outstanding n/s / 4,179 / 4,139 / 4,686 / 4,741 / 4,758 | 10-K-FY2025 lines 1867, 1883, 1901, 1917; 10-Q line 185 | PASS. FY2021 is available pre-split in the FY2023 10-K equity statement; "n/s" is conservative but could read "411 pre-split" next run |
| D5 | Footnote: $14.40 and $16.40 pre-split; FY2023 $18.40 vs $1.840 | 10-K-FY2023 line 3225; 10-K-FY2025 line 3263 | PASS |

### 3e. outlook.md §1 indicator table (every number) and year-ago line

| # | Cell | Found at | Result |
|---|---|---|---|
| E1 | $15,009M / $7,178M; $12,515M / $6,796M; "approximately $22.0 billion" | release line 66–68; Q1 release lines 66–68, 84 | PASS |
| E2 | "$10.8 billion"; "$8.4 billion"; "$10.7 billion in Q2" | release line 32; Q1 release line 32 | PASS |
| E3 | 69.5% / 77.1%; 68.1% / 77.0%; "approximately 68 percent"; actual 68.7% (computed) | release lines 172, 236, 160; Q1 release (13,157 / 19,311 = 68.13; 14,868 / 19,311 = 76.99); Q1 release line 86; 15,244 / 22,187 = 68.71 | PASS |
| E4 | 61.8% / 78.7%; 60.0% / 78.3% (computed as H1 minus Q2) | 10-Q lines 1421–1423, 1495–1497: (16,784 − 9,281) / (27,524 − 15,009) = 7,503 / 12,515 = 59.95; (10,970 − 5,647) / (13,974 − 7,178) = 5,323 / 6,796 = 78.33. The derived Q1 revenues equal the Q1 release segment figures, confirming the subtraction | PASS |
| E5 | $164.6B; $33.3B at Nov 2, 2025 | 10-Q line 609; 10-K-FY2025 line 2175 | PASS |
| E6 | $4,328M / $128,110M; $2,962M; $132M | 10-Q lines 641, 1227; Q1 release line 406; 10-K-FY2025 line 3679 (Purchase Commitments column) | PASS |
| E7 | 42% / ~45% "for each of the fiscal quarter and two fiscal quarters" | 10-Q lines 1403, 1405 | PASS |
| E8 | $10,262M (46%); $66,720M; $8,010M (41%); $66,057M carrying value (computed) | release lines 20, 362; 10-Q line 999; Q1 release line 20 ("41 percent"); Q1 release lines 432, 440: 2,252 + 63,805 = 66,057 | PASS |
| E9 | Year-ago: $15,004M; 68.0% / 79.4%; 57.2% / 75.6%; $6,411M; 29% / 40% | release lines 160, 172, 236 (10,197 / 15,004 = 67.96; 11,911 / 15,004 = 79.39), 362; 10-Q lines 1495–1497 (4,806 / 8,408 = 57.16; 4,987 / 6,596 = 75.61), 1403, 1405 | PASS |

### 3f. outlook.md §4 guidance (word-for-word)

| # | Quote | Found at | Result |
|---|---|---|---|
| F1 | Three release bullets "approximately $29.4 billion;" / "approximately 67 percent of projected revenue;" / "approximately 68 percent of projected revenue."; "ending August 2, 2026" | release lines 82–88 | PASS, verbatim including semicolons |
| F2 | "in Q3 we expect semiconductor revenue from AI to grow over 200 percent year-over-year to $16.0 billion." | release line 32 | PASS |
| F3 | "We forecast semiconductor revenue of approximately $20.5 billion, up 124% year-on-year." | transcript CFO guidance paragraph | PASS |
| F4 | "We expect Q3 infrastructure software revenue of approximately $8.9 billion, up 31% year-on-year." | same | PASS |
| F5 | "in Q3 we forecast non-AI semiconductor revenue to be approximately $4.5 billion, up 12% year-on-year." | transcript CEO non-AI paragraph | PASS |
| F6 | "we expect Q3 consolidated gross margin to be down to approximately 74%." | transcript CFO margins paragraph | PASS |
| F7 | "We expect the non-GAAP tax rate for Q3 and fiscal year 2026 to be approximately 16% ... We expect the non-GAAP diluted share count in Q3 to be approximately 4.94 billion shares, excluding the impact of potential share repurchases." | same; ellipsis covers "due to the impact of the global minimum tax and the geographic mix of income compared to that of fiscal year 2025." | PASS |
| F8 | "For the full year 2026, we expect to achieve AI semiconductor revenue of $56 billion, up approximately 180% from fiscal 2025." | transcript CEO prepared remarks. This is NOT the garbled "Which is fifth around $56 billion" Q&A line listed in notes-transcript §9 | PASS |
| F9 | "we reiterate our AI semiconductor revenue guidance to be in excess of $100 billion." | CEO prepared remarks; not a §9 garble | PASS |
| F10 | "We are planning to ship 10 gigawatts in 2027, and nothing has changed. Back-half loaded" | Rasgon answer | PASS |
| F11 | "We expect, in fact, 2028 to be a substantial growth from what we are forecasting in 2027." | Reitzes answer. The sentence that follows it ("Thank you, Harlan.") is a flagged misattribution; the quoted sentence itself is not flagged | PASS |
| F12 | "Not guided: FY2026 total or software revenue, capex, operating expenses, free cash flow, EPS, buybacks" | grep of release and transcript confirms none of these is guided; matches notes-transcript §10 | PASS |

### 3g. outlook.md §5 claim quotes

All eleven quotes match the release, transcript or 10-Q exactly: "revenue guidance of approximately $29.4 billion" (release line 84); "semiconductor revenue from AI to grow over 200 percent year-over-year to $16.0 billion" (line 32); "Q3 infrastructure software revenue of approximately $8.9 billion" and "non-AI semiconductor revenue to be approximately $4.5 billion" (transcript); "Q3 consolidated gross margin to be down to approximately 74%"; "approximately 67 percent of projected revenue" (line 86); "AI semiconductor revenue of $56 billion"; "in excess of $100 billion"; "taping out our next-generation 200-terabit switch this quarter"; "approximately $164.6 billion" (10-Q line 609); "accounted for 42% of our net revenue for each of the fiscal quarter and two fiscal quarters" (10-Q line 1403). **11 PASS.** The "not sharpened" paragraph correctly avoids the two garbled passages ("double from the first half we shipped last from the ship this year"; "something in the range of $19 billion") and correctly reports the 8-K's "approximately 3.5 gigawatts" (8-K-2026-04-06 line 61) against the call's "another 5 gigawatts".

### 3h. Prose sentences and quote blocks, both files

| # | Sentence / quote | Found at | Result |
|---|---|---|---|
| G1 | §1: ~95% of wafers from TSMC in H1 FY2026; own plants for filters and lasers | 10-Q line 1801; 10-K-FY2025 lines 307, 637 (FBAR filters, InP wafers for lasers at Fort Collins and Breinigsville) | PASS |
| G2 | §1: "enterprise and artificial intelligence ("AI") data centers, servers and networking and connectivity equipment" | 10-K-FY2025 line 163 | PASS verbatim |
| G3 | §1: VCF "a private cloud platform that integrates compute, storage, networking, and management into a single solution" | 10-K-FY2025 line 2325 (Note 4) | PASS verbatim |
| G4 | §1: "large enterprises"; "most of the Fortune 500" | lines 303, 225 | PASS |
| G5 | §1 history: IPO August 2009; LSI 2014; Broadcom Corp February 2016; CA, Inc. and Symantec named; VMware Nov 22, 2023, $86.3B | DEF14A line 1407; 10-K-FY2025 line 383; DEF14A lines 151, 377; 10-K-FY2025 line 153; lines 1109, 2203 ("Total purchase consideration | 86,290") | PASS (tag corrected, see Direct fixes) |
| G6 | §2: "which can cause our quarterly net revenue to fluctuate significantly"; revenue booked on delivery to distributors | 10-K-FY2025 line 1125 ("We recognize revenue upon the delivery of our products to the distributors, which can cause…") | PASS verbatim |
| G7 | §2: distributors 48% FY2025, 56% H1; one distributor 42% (32% FY2025); top five ~45% (~40%) | 10-K-FY2025 lines 551, 1261, 1263; 10-Q lines 1403, 1405, 1781 | PASS; all quoted fragments verbatim |
| G8 | §2: Apple "approximately 20%" in FY2023 10-K; no Apple in FY2025 10-K | 10-K-FY2023 line 1503; grep "Apple" in 10-K-FY2025 = 0 hits | PASS |
| G9 | §2: "Networking represented almost 40% of our Q2 AI revenue" | transcript | PASS verbatim |
| G10 | §2: $7.8B upfront licence revenue; termination-right accounting; $12.4B VMware FY2024 revenue; "strong demand for our VCF product ... and the transition to a subscription license model" | 10-K-FY2025 lines 1257, 1265, 1301 (quote, ellipsis covers "including license revenue recognized on contracts where customers do not have the right to terminate and"), 2261 ("$12,384 million of net revenue attributable to VMware for fiscal year 2024") | PASS |
| G11 | §2/§3 outlook: "ARR growth of 17% year-over-year" | transcript | PASS |
| G12 | §3: $12.1B cost of products on $44.8B products revenue; TSMC "has raised, and may in the future raise, their prices" | 10-K-FY2025 lines 1665, 1657, 579 | PASS |
| G13 | §3: $1.9B software cost of revenue on $27.0B; "93%"; "approximately 70%" | 10-K-FY2025 line 3599 (1,902); transcript CFO segment paragraphs | PASS |
| G14 | §3: R&D $11.0B; reconciliation items 1,967 / 2,092 / 81 | 10-K-FY2025 line 1677 (10,977); release lines 266–270 | PASS |
| G15 | §3: "lower infrastructure software labor costs following our integration of the VMware business"; "our ASICs, TPUs, some of the wireless business has lower margins"; 79.4% → 77.1% | 10-K-FY2025 line 1307; transcript Spears to Seymore; release line 236 | PASS |
| G16 | §3: capex below depreciation until FY2025 | depreciation 539 / 529 / 502 / 593 / 574 (10-K-FY2023 line 2449; 10-K-FY2025 line 2435) vs capex 443 / 424 / 452 / 548 / 623 | PASS |
| G17 | §3: $128,110M commitments, $55,214M FY2027, $72,870M FY2028, "primarily inventory"; $132M six months earlier; inventory $4,328M "primarily to support higher expected shipments for custom AI accelerators" | 10-Q lines 1217–1229, 1541; 10-K-FY2025 lines 3667–3681 | PASS |
| G18 | §4: 37.8% FY2024 rate from IP transfer; FY2025 net benefit | 10-K-FY2025 lines 3467 ((1.7)% / 37.8%), 3473 ("intra-group transfer of certain IP rights to the United States") | PASS |
| G19 | §4: receivables sold $7.4B; tax-withholding purchases $3.9B FY2025, none in FY2026 | 10-K-FY2025 lines 2395 (7,401), 1831 (3,860); release line 508; 10-Q line 1567 (Item 2 describes the change) | PASS |
| G20 | §4: principal $66,720M all fixed-rate; interest $3,210M ≈ 13% of operating income (computed); Jan 2026 $4.5B notes 4.300%–5.700% due 2031–2056 redeeming 2027/2028 notes; $493M due FY2027; $7.5B facility undrawn | 10-Q lines 999, 1027, 1051 (maturity table "2027 | 493"); 10-K-FY2025 lines 1689, 1483; 8-K-2026-01-13 lines 59–65 | PASS (3,210 / 25,484 = 12.6%) |
| G21 | §4: tax incentives $2,709M; global minimum tax from FY2026; "approximately 16%" | 10-K-FY2025 lines 873, 863; transcript | PASS |
| G22 | §4: assets $171.1B, goodwill $97.8B, intangibles $32.3B; 16% (computed) | 10-K-FY2025 lines 1597, 1591; release line 394 (32,273 at Nov 2, 2025); 26,914 / 171,092 = 15.7% | PASS |
| G23 | §5: "to our individual customers' specifications"; "Many of our major customer relationships … collaborative product development" | 10-K-FY2025 lines 171, 301 | PASS verbatim |
| G24 | §5: Google 8-K quote "a Long Term Agreement for Broadcom to develop and supply custom Tensor Processing Units ("TPUs") for Google's future generations of TPUs and a Supply Assurance Agreement ... through up to 2031" | 8-K-2026-04-06 line 59 | PASS verbatim with ellipsis |
| G25 | §5: RPO $33.3B → $164.6B, "including obligations under a long-term contract for custom AI accelerators" | 10-Q line 609 reads "These commitments include obligations under a long-term contract for custom AI accelerators entered in the fiscal quarter ended May 3, 2026" | **FAIL (wording):** "including obligations under" is not in the source. Numbers correct. Corrected directly to "…and these commitments "include obligations under a long-term contract for custom AI accelerators"" |
| G26 | §5: "we fully expect that there will be some diversity of sources" | transcript Tan to Curtis | PASS |
| G27 | §5: "at least one generation of technology and product leadership"; "the industry's only 100 terabit Ethernet switch, the Tomahawk 6, for over one year"; "enabled some of our competitors"; "closer to around 30%" | transcript CEO networking paragraph; 10-K-FY2025 line 333; transcript Tan to Schneider | PASS |
| G28 | §5: "investigations or inquiries ... in Korea, Japan and the European Union into certain of our contracting and business practices"; growth "below the 31% guided" | 10-Q line 1741; transcript | PASS |
| G29 | §6 #1: "with customer-owned tooling"; AI ≈ 49% of Q2 revenue (computed) | 10-Q line 1789; 10.8 / 22.187 = 48.7%; CFO also said "49% of total revenue" | PASS |
| G30 | §6 #2: "may have constrained resources or capital and may be unable to pay for their required AI infrastructure" | 10-K-FY2025 line 547 and 10-Q line 1771 (both cited) | PASS verbatim |
| G31 | §6 #3: Apollo quotes, "June 8, 2026", "maximum exposure of $29 billion", "as the AI racks are deployed"; Note 11 and Part II Item 5 | 10-Q lines 1255 (Note 11, "Subsequent Events" begins line 1253) and 2213 (Item 5 begins line 2211) | PASS verbatim |
| G32 | §6 #3: "AI XPU platform with Apollo and Blackstone and other leading investors to deploy more than 20 gigawatts of compute capacity through 2028"; "valued at $35 billion" | transcript CEO. The draft paraphrases the garbled "first trench" as "first slice (tranche)" rather than quoting it | PASS |
| G33 | §6 #4: "designed to be manufactured in a specific process, typically at one particular fab or foundry"; no long-term capacity contracts | 10-Q line 1797; 10-K-FY2025 line 577 and 10-Q line 1799: "We do not generally have long-term capacity commitments with our CMs" | PASS on the quote. The draft's "there are no long-term capacity contracts" dropped the source's "generally"; aligned directly to the source wording (see Direct fixes) |
| G34 | §6 #5: "shift existing compute workloads off-premises to public cloud providers"; "not accept our subscription licensing model"; $20.8B segment operating income | 10-Q lines 1911–1913; 10-K-FY2025 line 3605 (20,765) | PASS |
| G35 | §6 #6: China incl. Hong Kong 17% of FY2025 revenue; "a substantially smaller percentage"; "have had and may in the future have an adverse effect on our revenue" | 10-K-FY2025 lines 1267–1273, 509 | PASS verbatim |
| G36 | §6 #7: age 74; "None of our senior management is bound by written employment contracts. In addition, we do not currently maintain key person life insurance"; board succession plan names no one | 10-K-FY2025 lines 373, 597; DEF14A lines 385–397 | PASS |
| G37 | §7: CEO since March 2006; no annual cash bonus; 2023 award 10,000,000 shares, price hurdles, October 31, 2027 | 10-K-FY2025 line 381; DEF14A lines 1033, 1899, 1941 | PASS |
| G38 | §7: 2025 award September 3, 2025, "to extend his leadership of Broadcom through fiscal 2030", 610,521 target, 0–300%, best four consecutive quarters FY2028–FY2030, ≤$60B 0% / $90B 100% / $105B 200% / ≥$120B 300% | DEF14A lines 1415, 155, 1473, 1491–1505 | PASS |
| G39 | §7: FY2025 pay $205.3M, almost all the grant; 66% of votes cast (computed); 92% a year earlier | DEF14A line 1759 (205,278,006; stock awards 202,351,080); 8-K-2026-04-21 line 91: 2,433,503,375 / (2,433,503,375 + 1,232,879,962 + 17,517,248) = 66.1% (66.4% excluding abstentions; both round to 66%); DEF14A line 1099 | PASS |
| G40 | §7: CFO retires June 12, 2026; successor "Vice President, Corporate Controller and Chief Accounting Officer of Alphabet Inc. since 2018" | 8-K-2026-04-02 lines 61–65 | PASS verbatim |
| G41 | §7: eight directors, seven independent; Samueli chair, co-founder, 1.8%, 16,175,000 pledged; Vanguard 9.9%, BlackRock 7.3%, insiders 1.9%; Tan 908,474 | DEF14A lines 457, 719, 793, 2349, 363, 2387, 2323, 2329, 2361, 2351 | PASS |
| G42 | §7: $30.4B term loans repaid; $7,850M Q1 / $600M Q2 / $10.1B remaining; 544M shares; dividend +10% to $0.65 | 10-K-FY2025 lines 3219 (30,390; repaid remaining 13,595 in FY2025), 1935; 10-Q lines 417, 1081; DEF14A line 229 | PASS |
| G43 | outlook §2: "we provide chips, technology in the form of chips, whether they be AI compute accelerators we call XPUs or networking chips that cluster them together"; "our six core customers"; "our other two customers"; "simply insatiable"; "bookings for AI semiconductors were over $30 billion against the $10.8 billion we shipped"; "Our visibility runs all the way to 2028 right now"; "Our strategic vision is to bring together … including Anthropic and OpenAI"; "the AI XPU platform with Apollo and Blackstone and other leading investors" | transcript Tan to Muse; CEO prepared remarks; Tan to Moore | PASS, all verbatim |
| G44 | outlook §3: "another 5 gigawatts of next-generation TPU-based compute beginning in 2027"; "on track for production late 26"; "1.3 gigawatts in 2027"; "3 gigawatts through the end of 2028"; "purchase orders totaling $6 billion"; "next-generation 200-terabit switch"; "Q2 revenue of $4.2 billion was up 6% year-on-year. Bookings during the same period exceeded $6 billion, which is a clear indication we are on the path towards a full cyclical recovery"; software $7,178M up 9% | transcript CEO prepared remarks; release line 68 | PASS, all verbatim |

**Verbatim character-for-character checks (at least three required):** F1 (release outlook bullets), F8 ($56 billion sentence), G3 (VCF definition), G24 (Google 8-K), G30 (constrained-resources risk factor), G36 (employment-contract sentence), G43 and G44 (transcript blocks). All pass except G25, corrected.

**Totals:** 109 items checked; 108 PASS; 1 FAIL (G25, wording inside quotation marks, fixed directly).

## 4. Jargon audit

Thinking as a 16-year-old, term by term:

| Term | Status before review | Action |
|---|---|---|
| hypervisor | Only in the glossary, never in the text | Glossary entry replaced by a plain "Private cloud" entry (the term the text actually uses) |
| XPU, TPU, ASIC | Defined in §1 and glossary | OK |
| RPO | "Firmly committed contracts (RPO)" in §5; glossary | OK |
| tape-out | Outlook glosses inline "(design finished and sent to the foundry)"; glossary | OK |
| ARR | Glossary; outlook glosses inline | OK |
| adjusted EBITDA | Glossary; used in outlook only | OK (outlook has no glossary by design; business.md's serves both) |
| PSU | Not used; draft says "performance share awards" | OK |
| tranche | "first slice (tranche)" | OK |
| backstop | Explained in plain words in §6 #3 and glossary | OK |
| wafer, foundry | Glossary; "fab" appears only inside a verbatim quote next to "foundry" | OK |
| hyperscaler | "cloud giants (hyperscalers)" at first use | OK |
| ratable, accretive | Not used | OK |
| IP | Used twice with no expansion | Fixed: "intellectual property (IP)" at first use (§4) |
| proxy | "the proxy and each quarterly release" | Fixed: "the proxy statement (the document sent to shareholders before the annual meeting)" |
| gross margin, operating income/margin | Used from §3 without definition | Fixed: one-line glosses at first prose use in §3 |
| restructuring | Bare | Fixed: "(reorganisation costs)" |
| principal | "Principal was $66,720 million" | Fixed: "(the amount borrowed, before interest)" |
| notes (debt) | "sold $4.5 billion of notes" | Fixed: "notes (bonds)" |
| "bank line is undrawn" | Jargon | Fixed: "bank credit line is unused" |
| receivables | Bare | Fixed: "(unpaid invoices)" |
| "authorization left" | Finance shorthand | Fixed: "board-approved buyback room left" |
| H1 | Abbreviation unexplained at first use in both files | Fixed: "(first half)" at first use in each file |
| carrying value (outlook) | Bare | Fixed: "carrying (balance-sheet) value" |
| EPS (outlook) | Bare | Fixed: "EPS (earnings per share)" |
| "impaired" inside the goodwill glossary entry | Jargon within a definition | Fixed: "until the company decides it is worth less and writes it down" |
| gigawatt, Ethernet switch, perpetual licence vs subscription, GAAP/non-GAAP, amortization, goodwill, capex | Glossary, one sentence each | OK |
| Tomahawk, Jericho, VCF, set-top boxes, mainframe, fibre-channel storage networking, distributor, end customer, bookings | Product names or name-inferable in context | OK |

Glossary now holds 18 entries, each one sentence, each used in business.md or outlook.md. "Tape-out" and "Adjusted EBITDA" appear only in outlook.md; keeping them in the business.md glossary is the only place they can live, so they stay.

## 5. Invented-number check

| Item | Finding |
|---|---|
| Pre-split dividends per share FY2021–FY2022 (1.44*, 1.64*) | Correctly labelled: footnote states the 10-K reports $14.40 / $16.40, that no fetched filing states the split, and that the 10-for-1 factor "is our inference" from $18.40 vs $1.840 for FY2023. PASS |
| Q1 FY2026 segment operating margins 60.0% / 78.3% | Labelled "(computed as H1 minus Q2)"; re-derived exactly; derived Q1 revenues match the Q1 release. PASS |
| Say-on-pay 66% | Labelled "(computed)"; 8-K vote counts give 66.1% (66.4% excluding abstentions). PASS |
| Anthropic gigawatts (call "another 5 gigawatts" vs 8-K "approximately 3.5 gigawatts") | business.md does not use the figure. outlook.md §3 quotes the call verbatim and §5's "Not sharpened" paragraph states the discrepancy and that it is unexplained. PASS |
| "$56 billion" FY2026 and "in excess of $100 billion" FY2027 | Transcript-only, quoted verbatim from the CEO's prepared remarks, tagged [Q2 FY2026 call]; neither is among the §0/§9 garbles (the garbled "$56 billion" is a different Q&A sentence). PASS |
| Apollo backstop | "$29 billion" maximum exposure, "June 8, 2026", 5-year terms, remedies, and "increase over time as the AI racks are deployed" all match 10-Q Note 11 / Part II Item 5. Broadcom's exposure to the wider $35B / 20 GW platform is stated as "not disclosed", which is correct (transcript notes §10 confirm). PASS |
| "about 13% of operating income (computed)", "about 16% of that total (computed)", "about 49% of Q2 revenue (computed)", "Semiconductor share (computed)", "Net borrowing (computed)", "Amortization … (computed, both lines)", outlook "roughly 60% … (computed)", "(actual 68.7%, computed)", "(percentages computed)" | All labelled and all re-derive. PASS |
| Inferences: "a multi-year job (our inference)", "light in practice (our inference)", "(our view)" on incentives, "Alphabet is Google's parent (our observation…)", outlook row 7 "(our inference)" | All labelled. PASS |
| §3 "Broadcom has promised suppliers roughly two years of AI-chip purchases, matched by $164.6 billion of committed customer contracts" | Supported (commitments "primarily inventory" for FY2027–FY2028; inventory build "primarily to support higher expected shipments for custom AI accelerators") but was not labelled. Label "(our inference)" added directly |
| §6 #4 "there are no long-term capacity contracts" | Source says "We do not generally have long-term capacity commitments with our CMs". Aligned directly to the quoted source wording |
| §2 "$12.4 billion of FY2024 revenue" from VMware | 10-K FY2025 Note 4 line 2261: $12,384 million. PASS |
| Every other figure | Carries a tag that supports it (see §3 tables above). No untagged figure found |

## 6. Banned-filler sweep

Grep of both files for leverage (verb), synergy, headwind, tailwind, monetize, ecosystem, at scale, robust, unlock, TAM, poised, landscape: **one hit**, "at scale", inside the verbatim CEO quote in outlook.md §2 ("to deliver at scale sufficient compute capacity"). Allowed. No other hits in either file outside quotes.

## 7. As-of check

- Latest-dated fact used: the Apollo arrangement of June 8, 2026, taken from the 10-Q filed June 9, 2026 (Note 11 subsequent event). Within cutoff.
- No Q3 FY2026 results, no September 2026 material, no post-cutoff 8-K (2026-06-11, 2026-06-18, 2026-07-06, 2026-09-02 were not fetched per MANIFEST and nothing in the drafts relies on them).
- CFO change: business.md §7 says "CFO Kirsten Spears retires June 12, 2026; Amie Thuener … succeeds her [10-K FY2025, Item 1; 8-K 2026-04-02]", i.e., the announced plan with its effective date, no later detail. The transcript's "Amy Teiner" garble is not reproduced; the 8-K spelling is used.
- Guidance is quoted as forward-looking ("we expect", "guidance of"), never graded.
- Written date 2026-09-07 is the run date, with the as-of label separate. Correct.

## 8. Verdict

**PASS.** No structural or factual item remains for the writer. Optional notes for the owner or the next refresh, none of which blocks the report:

1. Indicator #2 (AI semiconductor revenue) depends on management continuing to state the figure. It has appeared in every release in the sources; if it disappears, treat that as a 🔇 signal rather than an indicator failure.
2. §7 table "Shares outstanding" FY2021 is marked n/s; the FY2023 10-K gives the pre-split balance, which could be shown as "411 pre-split (≈4,110 split-adjusted, inferred)" for a complete row.
3. Claim 10 (RPO) could add "a period-end balance, so no quarter/YTD column applies" to close the §9 disclosure-check requirement formally.
4. business.md is 2,600 words, in range but in the upper half; §6 #8 (Debt) and the last sentence of §3's capital-intensity paragraph could be trimmed if the owner wants it shorter.

## Direct fixes (recorded per §13)

Word counts: business.md 2,541 → 2,600; outlook.md 1,015 → 1,018. All edits were in-line; line numbers unchanged.

**business.md**

1. §2 line 28: "the proxy and each quarterly release do" → "the proxy statement (the document sent to shareholders before the annual meeting) and each quarterly release do". (jargon)
2. §3 line 34: added "(revenue left after the direct cost of making the product, as a share of revenue)" after "a gross margin". (jargon)
3. §3 line 49: added "(profit after all running costs, before interest and tax)" after "non-GAAP operating income"; "restructuring $81 million" → "restructuring (reorganisation costs) $81 million". (jargon)
4. §4 line 65 table header: "H1 FY2026" → "H1 FY2026 (first half)". (jargon)
5. §4 line 82: "transfer of IP rights" → "transfer of intellectual property (IP) rights"; "customer receivables to banks" → "customer receivables (unpaid invoices) to banks". (jargon)
6. §4 line 84: "Principal was" → "Principal (the amount borrowed, before interest) was"; "notes due 2031 to 2056" → "notes (bonds) due 2031 to 2056"; "bank line is undrawn" → "bank credit line is unused". (jargon)
7. §5 line 90: quote `"including obligations under a long-term contract for custom AI accelerators"` was not verbatim (10-Q line 609 reads "These commitments include obligations under…"). Rewritten as `…and these commitments "include obligations under a long-term contract for custom AI accelerators"`. (quote wording; tag unchanged)
8. §3 line 61: added "(our inference)" before the tag on "Broadcom has promised suppliers roughly two years of AI-chip purchases … binds whatever demand does". (label on a supported inference)
9. §6 #4 line 106: "and there are no long-term capacity contracts" → "and Broadcom does "not generally have long-term capacity commitments" with its manufacturers" to match 10-K FY2025 Item 1A line 577 / 10-Q Item 1A line 1799. (one-word alignment to source; tags unchanged)
10. §1 line 10: tag "[DEF 14A 2026, Director Nominees; 10-K FY2025, Item 1]" → "[DEF 14A 2026, CD&A; Corporate Governance; 10-K FY2025, Item 1]" because the August 2009 IPO date is in the CD&A (line 1407) and the February 2016 date in Corporate Governance (line 377), not in the nominee bios. (tag precision)
11. §7 line 132: "$10.1 billion of authorization left" → "$10.1 billion of board-approved buyback room left". (jargon)
12. Glossary line 155: "Hypervisor / private cloud" entry replaced by "**Private cloud** — a company's own data center run with software that lets one physical server act as many separate virtual computers, the way a cloud provider's does." (unused term removed; used term kept)
13. Glossary line 165 (Goodwill): "until judged impaired" → "until the company decides it is worth less and writes it down". (jargon inside a definition)

**outlook.md**

14. §1 line 13: "(computed as H1 minus Q2)" → "(computed as first half (H1) minus Q2)". (jargon)
15. §1 line 17: "$66,057M carrying value" → "$66,057M carrying (balance-sheet) value". (jargon)
16. §4 line 47: "EPS" → "EPS (earnings per share)". (jargon)

Nothing else in either file was touched. No git command was run.
