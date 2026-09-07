# Applied Optoelectronics, Inc. (AAOI) — Reviewer report, Q2 2026 (three months ended June 30, 2026)

_Review cycle 1 of 2. Reviewed 2026-09-07 against `sources/2026-Q2/` only (as-of cutoff 2026-08-06; the 8-Ks of 2026-08-21, 2026-08-24 and 2026-09-01 were not fetched and are not referenced anywhere in the drafts). Files reviewed: `business.md` (2,877 prose words before fixes, 2,987 after), `outlook.md` (1,178 before, 1,183 after). Word counts by `python3 /tmp/aaoi_wc_prose.py` (prose only, per AGENTS.md §3 rule 7). Line numbers below refer to the cached `.txt` files; the host grep is ugrep, so every quote was checked with `grep -F`._

**Verdict: REVISE.** Citation spot-check: 111 items checked, 108 PASS, 3 FAIL (one tag pointing at the wrong note, fixed directly; two interpretive phrases presented as sourced fact, for the writer), 0 UNVERIFIABLE. Every number in every table is right, every $-thousand to $-million conversion is right, every guidance and claim quote is verbatim, and nothing dated after 2026-08-06 appears. What needs the writer: the Microsoft/Amazon inference needs its basis made explicit and asymmetric (and the outlook §3 heading quietly equates "second hyperscaler" with Amazon); two unlabelled inferences in §2 and §3; two different six-month share-proceeds totals used without explanation; three claims that are either transcript-dependent, nearly unfailable, or loosely sharpened; duplication across outlook §3/§4/§5; and both files now sit within 20 words of their ceilings, so every fix must be paid for with a cut.

---

## 1. Skeleton compliance

**business.md**

| Requirement (§6) | Result |
|---|---|
| `# <Company> — The Business` | OK |
| `_As of <QLABEL>. Written <date>._` | OK: "Q2 2026 (three months ended June 30, 2026). Written 2026-09-07." Fiscal = calendar, parenthetical present anyway |
| §1–§8 headings, in order, none skipped | OK. §1 has the history paragraph; §6 carries concentration with its own table; §8 has name / why / where |
| §1 "two or three paragraphs" plus history | **Deviation (minor):** four paragraphs before History; paragraph 3 (telecom, sites, headcount) is a candidate to fold into §2/§3 |
| §2 segment table, 5 fiscal years | OK (FY2021–FY2025 + Q2 2026); FTTH/"FTTH and other" definition change footnoted |
| §3 table: revenue, GM, OM, capex, capex/revenue, 5 years | OK, plus non-GAAP GM, R&D %, equipment deposits, D&A |
| §4 table, 5 years | OK (9 rows, includes share proceeds and cash incl. restricted cash, labelled) |
| §8 `_Proposed — owner to review and lock._` | OK |
| §8 indicators anchored to recurring disclosures (§8 of AGENTS.md) | OK. All eight anchor to a release table row, a 10-Q note or a cash-flow line. The one-off call targets (650k/month, $325M CATV, $1.1B) are correctly tracked as claims, not indicators. One caution: indicator 6's "equipment prepayments" line changed label between the Q1 10-Q ("Deposits and deferred charges") and the Q2 10-Q ("Prepayment for equipment and others"); see REVISE 8 |
| Glossary, Sources | Both present. Every tag prefix used (10 in business.md) maps to a file that exists in `sources/2026-Q2/`; page conventions stated for the supplemental and the deck |
| Length 2,000–3,000 | OK: 2,877 before fixes; 2,987 after the reviewer's glosses and the two restored figures. 13 words of headroom |

**outlook.md**

| Requirement (§7) | Result |
|---|---|
| `# <Company> — Outlook as of <QLABEL>` | OK |
| `_Transcript source tier: … Written <date>._` | OK: "none", matches MANIFEST; the Q1 2026 call is declared as a labelled supplement in the header and again in the opening paragraph |
| May statements never presented as August statements | OK. Every Q1-call quote is introduced with "in May", "On the May call", or sits under "Standing statements from the Q1 2026 call … All said May 7, 2026"; claims 3, 4, 7, 8 carry the [Q1 2026 call] tag |
| §1 table: one row per proposed indicator; this quarter / last quarter / what management said | OK, 8 rows, columns as specified, "No guidance" used where appropriate |
| §2, §3, §4 (verbatim guidance), §5 | OK |
| §5 tier-none closing list of claims that could not be sharpened | OK, present and specific |
| §6 Tone shift omitted on first run | OK, omitted |
| Sources | OK; all 6 tag prefixes used map to existing files |
| Length 800–1,200 | OK: 1,178 before, 1,183 after. 17 words of headroom |

---

## 2. Citation spot-check

Legend: PASS / FAIL / UNVERIFIABLE. "computed" items were re-derived from the $-thousand source lines. Sources report in $ thousands; every conversion to $ millions was checked.

### 2a. business.md §2 revenue-by-market table (every cell)

| # | Cell(s) | Tag | Found at | Result |
|---|---|---|---|---|
| A1 | Data Center 97.5 / 77.1 / 141.2 / 148.5 / 195.7 / 107.7 | 10-K FY2023 Note C; 10-K FY2025 Note C; 10-Q Note 3 | 10-K-FY2023 line 2624 (97,461; 77,094; 141,213); 10-K-FY2025 line 2799 (141,213; 148,525; 195,651); 10-Q line 693 (107,662) | PASS |
| A2 | CATV 94.3 / 118.2 / 59.9 / 87.7 / 245.1 / 80.6 | same | lines 2622; 2797; 695 | PASS |
| A3 | Telecom 16.2 / 24.7 / 13.8 / 11.0 / 13.7 / 3.4 | same | lines 2626; 2801; 697 | PASS |
| A4 | FTTH 1.0 / 0.1 / 0.1 | 10-K FY2023 Note C | line 2628 (957; 129; 56) | PASS |
| A5 | Other 2.6 / 2.7 / 2.6; "FTTH and other" 2.1 / 1.2; Other 0.3 | Notes C; Note 3 | FY2021–23 remainders 211,565−…=2,634; 2,699; 2,604 (FY2025 10-K's own 2023 "FTTH and other" 2,660 = 56+2,604, line 2803); 2,147; 1,211; 271 (line 699) | PASS |
| A6 | Total 211.6 / 222.8 / 217.6 / 249.4 / 455.7 / 191.9 | same | lines 2632; 2805; 10-Q 693–701 sum 191,922 | PASS |
| A7 | Percentages 46/35/65/60/43/56; 45/53/28/35/54/42; 8/11/6/4/3/2 | same | company figures 46.1/34.6/64.9/59.5/42.9/56.1; 44.6/53.0/27.5/35.2/53.8/42.0; 7.7/11.1/6.4/4.4/3.0/1.8 | PASS. Nit: the footnote says Q2 2026 percentages are "computed"; the 10-Q states them (line 693–699) |
| A8 | Footnote: 10-Q says "Other"; FY2025 10-K folds FTTH into "FTTH and other" | Note 3; Note C | 10-Q line 699; 10-K-FY2025 line 2803 | PASS |

### 2b. business.md §3 economics table

| # | Row | Tag | Found at | Result |
|---|---|---|---|---|
| B1 | Revenue (as A6); 6M 2026 343.1 | Item 7/8; 10-Q Item 1 | 10-Q line 1451 total 343,066 | PASS |
| B2 | Gross margin GAAP 17.8 / 15.1 / 27.1 / 24.8 / 30.0 / 28.3 | Items 7; 10-Q Item 2 | 10-K-FY2023 line 1142; 10-K-FY2025 line 1357; 10-Q line 1553 | PASS |
| B3 | Gross margin non-GAAP n/s / n/s / n/s / 25.1 / 30.9 / 29.5 (computed) | supplemental p.5; release | supplemental.txt p.5 line 265 (25.1%, 30.9%); release line 149 non-GAAP gross profit 101,341 / 343,066 = 29.54% | PASS |
| B4 | R&D % 19.5 / 16.3 / 16.5 / 22.0 / 18.8 / 17.6 | same | lines 1146; 1361; 1557 | PASS |
| B5 | Operating margin (26.8) / (26.5) / (19.0) / (28.4) / (12.0) / (11.0) | same | lines 1154; 1369; 1565 | PASS |
| B6 | Capex 8.0 / 3.2 / 9.1 / 43.4 / 179.1 / 335.1 | Items 8; 10-Q Item 1 | 10-K-FY2023 line 2310 (7,981; 3,210; 9,079); 10-K-FY2025 line 2476 (43,406; 179,148); 10-Q line 509 (335,132) | PASS |
| B7 | Equipment deposits and prepayments 2.2 / 0.5 / 5.2 / 6.8 / 31.1 / 289.7 | same | line 2314 "Deposits and prepaid for equipment" (2,222; 529; 5,229); line 2480 "Deposits and prepayment for equipment" (6,792; 31,082); 10-Q line 513 "Prepayment for equipment and others" (289,744) | PASS on numbers; the line label differs by filing, see REVISE 8 |
| B8 | Capex / revenue (computed) 3.8 / 1.4 / 4.2 / 17.4 / 39.3 / 97.7 | — | recomputed 3.77 / 1.44 / 4.17 / 17.41 / 39.31 / 97.69 | PASS |
| B9 | D&A 25.4 / 23.2 / 20.4 / 20.6 / 27.7 / 19.7 | same | lines 2268; 2438; 10-Q 475 | PASS |

### 2c. business.md §4 cash table

| # | Row | Tag | Found at | Result |
|---|---|---|---|---|
| C1 | GAAP net loss (54.2) / (66.4) / (56.0) / (186.7) / (38.2) / (37.1) | Items 8; 10-Q Item 1 | lines 2140; 2308; 10-Q 289 | PASS |
| C2 | Operating cash flow (11.6) / (14.0) / (7.9) / (69.5) / (174.4) / (73.8) | same | lines 2306; 2472; 10-Q 505 | PASS |
| C3 | Capex | as B6 | | PASS |
| C4 | Free cash flow (computed) (19.6) / (17.2) / (17.0) / (112.9) / (353.6) / (408.9) | — | 19,625; 17,232; 17,008; 112,932; 353,576; 408,913 | PASS |
| C5 | Equipment deposits | as B7 | | PASS |
| C6 | Net proceeds from selling new shares 15.4 / 1.2 / 69.0 / 146.3 / 518.9 / 1,028.2 | same | line 2340 (15,397; 1,238; 68,984); line 2506 (146,293; 518,914); 10-Q line 539 (1,028,207) | PASS |
| C7 | Stock-based compensation 12.1 / 9.6 / 11.9 / 14.8 / 11.7 / 9.3 | same | lines 2274; 2444; 10-Q 483 | PASS |
| C8 | Weighted-average shares 26.9 / 27.8 / 31.9 / 41.5 / 60.2 / 78.8 | same | line 2150 (26,912,141; 27,846,387; 31,944,259); line 2318 (41,538,551; 60,183,987); 10-Q line 299 six-month basic 78,789 thousand | PASS |
| C9 | Cash, equivalents and restricted cash 41.1 / 35.6 / 55.1 / 79.1 / 216.0 / 508.8 | same | lines 2350; 2518; 10-Q 549 | PASS. Row label says restricted cash is included, and the figure is the cash-flow-statement line, which includes it (worry-list item 6 confirmed) |
| C10 | Footnote: FY2024 loss includes $112.0M non-cash loss on exchanging notes | 10-K Note L | line 1565; 10-Q line 1141 "debt extinguishment loss of $112.0 million" | PASS |

### 2d. business.md §6 concentration table

| # | Row | Tag | Found at | Result |
|---|---|---|---|---|
| D1 | Digicomm 0% / 0% / 11.3% / 34.1%* / 53.1% / 42% (41.8% computed) | 10-K FY2023 Item 1; 10-K FY2025 Item 1, Note B; 10-Q Note 2, Item 2 | 10-K-FY2023 line 984; 10-K-FY2025 line 191 (Item 1: 34.1%) and 2614 (Note B: 35.1%); 10-Q line 1027 (top customer 42%), line 2001 (six-month Digicomm $147.0M, 42.8%); Q1 10-Q line 1735 ($66.7M) → (147.0−66.7)/191.9 = 41.84% | PASS. "42% = Digicomm" is an arithmetic inference the 10-Q does not state; sound, see §3 item 3 |
| D2 | Microsoft 14.1% / 18.4% / 46.6% / 43.7% / 28.8% / n/d | same | line 984; line 191; line 2614 | PASS. Correctly taken from Item 1 / Note B, not the self-contradictory Item 7 (line 1209) |
| D3 | ATX 25.6% / 47.3% / 15.6% / below 10% n/d | same | line 984; FY2024 ">10%" customers are Microsoft, Digicomm, Oracle only (line 2614) | PASS (inference sound) |
| D4 | Oracle 12.4% FY2024 | same | lines 191, 2614 | PASS |
| D5 | Unnamed second and third 26%, 24% | 10-Q Note 2 | line 1027 | PASS |
| D6 | Top five 67% / 78.2% / 85.6% / 92.9% / 95.2% | Notes B | 10-K-FY2023 line 2435; 10-K-FY2025 line 2614 | PASS |
| D7 | Top ten 84.7% / 87.2% / 92.7% / 95.0% / 96.6% / 99% | Items 1A/7; 10-Q | line 475; lines 621, 1281; 10-Q 1027 | PASS |
| D8 | Footnote: Item 7 misprints Microsoft (repeats 2023/2022) and swaps CATV/Data Center labels | 10-K FY2025 Item 7 | line 1209 ("28.8%, 46.6% and 18.4%"); lines 1271–1273 ("Data Center 53.8%", "CATV 42.9%") | PASS, and the writer correctly did not use Item 7 for concentration or mix (coordinator's instruction met) |

### 2e. business.md §7 capital-allocation table

| # | Row | Tag | Found at | Result |
|---|---|---|---|---|
| E1 | Buybacks and dividends: none ever | 10-K Item 5 | line 1181 "never declared or paid any cash dividends" | PASS (no buyback line exists in any cash-flow statement) |
| E2 | Capex + prepayments $210.2M FY2025; $624.8M 6M 2026 (computed) | Item 7; 10-Q Item 1 | 179,148+31,082 = 210,230; 335,132+289,744 = 624,876 | PASS |
| E3 | Share sales $69.0M / $146.3M / $518.9M / $1,028.2M | as C6 | | PASS |
| E4 | Shares outstanding 49.4M Dec 2024; 75.0M Dec 2025; 84.6M Aug 3, 2026 | 10-K Item 8; 10-Q cover | line 2248 (49,393; 74,998 thousand); 10-Q line 91 (84,569,237) | PASS |
| E5 | Convertible $125.0M, 2.75%, due January 2030, ~$43.31 | 10-K Note L | lines 1565, 3266; 10-Q line 2025 "mature on January 15, 2030" | PASS |
| E6 | Bank loans $58.9M drawn; $106.5M unused; one US, three Taiwan, six China lenders | 10-Q Note 11; Item 2 | line 1063 (Total $58,915); lines 1127, 1927 ($106.5M); line 2023 | PASS |
| E7 | Warrant 7,945,399 at $23.6956; 1,324,233 vested; $4B over 10 years | 10-Q Note 3 | line 721 | PASS |
| E8 | Cash and equivalents $499.7M | 10-Q Item 1 | line 171 (499,737) | PASS |

### 2f. outlook.md §1 indicators table (every number and quote)

| # | Cell | Tag | Found at | Result |
|---|---|---|---|---|
| F1 | DC $107.7M, 56.1%; Q1 $81.4M, 53.9% (computed); two Q1-call quotes | release; Q1 release; call | release line 8, 10-Q 693; Q1 release table "Datacenter 81,404" / 151,144 = 53.86%; transcript lines 84 and 40 (both Murry) | PASS |
| F2 | CATV $80.6M; $66.8M; "$75 million and $80 million" | same | 10-Q 695; Q1 release "CATV 66,841"; transcript line 68 | PASS |
| F3 | Non-GAAP GM 29.8%; 29.2%; "29% to 30%." | releases | release line 9; Q1 release line 27 | PASS |
| F4 | Digicomm 42% (41.8%) / 67.2%; 44.1% / 74.5%; "to decline" | 10-Q Note 2, Item 2; Q1 10-Q | lines 1027, 1997, 2001; Q1 10-Q 1731, 1735 | PASS |
| F5 | Warrant-linked $46.8M (84.8−38.0); 1,324,233; ~$38.0M; "return this customer as a 10%-plus customer" | Notes 3, 6; Q1 Note 3; call | 10-Q 737, 857; Q1 10-Q 651; transcript line 42 | PASS (worry-list item 5: arithmetic and label correct) |
| F6 | OCF +$11.6M vs $276.9M + $280.0M (computed); Q1 ($85.4M) vs $58.2M + $9.7M; capex "above the total that we spent in Q1" | 10-Q Item 1; Q1 10-Q Item 1; call | −73,781 − (−85,353) = +11,572; 335,132 − 58,225 = 276,907; 289,744 − 9,744 = 280,000; Q1 lines 447, 451, 453; transcript line 80 | PASS. Caveat: the Q1 line subtracted is labelled "Deposits and deferred charges", the Q2 six-month line "Prepayment for equipment and others"; the subtraction assumes they are the same line (REVISE 8) |
| F7 | Inventory $278.8M; $206.2M | releases | release line 68; Q1 release line 73 | PASS |
| F8 | 84,569,237 at Aug 3; $645.8M (computed); 80,242,767 at May 5; $382.4M; two quotes | covers; Items 1; call; Q1 release | covers line 91 each; 1,028,207 − 382,448 = 645,759; Q1 10-Q 477; transcript line 82; Q1 release line 28 | PASS |
| F9 | Year-ago: DC $44.8M 43.5%; CATV $56.0M; non-GAAP GM 30.4%; top customer 54%; inventory $138.9M | release; Note 2; supplemental p.2 | 10-Q 693–695; release line 9; 10-Q 1027; supplemental p.2 line 51, sixth column (2Q25) 138,867 | PASS |

### 2g. outlook.md §4 guidance quotes (word-for-word, `grep -F`)

| # | Quote (abridged) | Tag | Found at | Result |
|---|---|---|---|---|
| G1 | "For third quarter of 2026, the company currently expects:" | release | line 18 | PASS |
| G2 | "Revenue in the range of $255 million to $290 million." | release | line 20 | PASS |
| G3 | "Non-GAAP gross margin in the range of 29% to 30.5%." | release | line 21 | PASS |
| G4 | "Non-GAAP net income in the range of $10.1 million to $24.0 million, … approximately 92.8 million shares." | release | line 22 | PASS |
| G5 | "we continue to anticipate steady sequential revenue growth this year" (CFO) | release | line 5, Murry | PASS |
| G6 | "we now believe our 2026 revenue will exceed $1.1 billion, and we now expect to generate more than $140 million in non-GAAP operating income this year." | call | line 32 (Lin) | PASS |
| G7 | "we expect by the end of this year we will be capable of producing over 650 thousand pieces … bring new production online." | call | line 50 (Murry) | PASS |
| G8 | "By the end of next year, 2027, … over 930 thousand pieces … over half of that output coming from Texas." | call | line 50 | PASS |
| G9 | "we now currently expect to generate over $325 million annually in CATV." | call | line 68 | PASS |
| G10 | By mid-2027, "about $471 million per month of data center transceiver revenue, with about 40% of this capacity in the U.S." | call | line 84; the "by mid-2027" framing is Murry's own at line 82 (90 + 217 + 164 = 471) | PASS |
| G11 | CEO: "I would say we go to 35% gross margin by end of this year." | call | line 174 (Lin) | PASS. The writer correctly avoided the garbled "by Q3, the whole company … more than 40%" that follows |
| G12 | Q2 guided vs delivered: "$180 million to $198 million"; "29% to 30%"; "a loss of $2.5 million to income of $2.8 million"; $191.9M / 29.8% / $5.5M; CATV $75–80M | Q1 release; release; call | Q1 release lines 26–28; release lines 8, 9, 11; transcript line 68 | PASS |

### 2h. outlook.md §5 claim quotes (word-for-word)

| # | Claim quote | Tag | Found at | Result |
|---|---|---|---|---|
| H1–H2 | Claims 1–2 (G2, G3) | release | lines 20, 21 | PASS |
| H3–H4 | Claims 3–4 (G6 split) | call | line 32 | PASS |
| H5 | "continue to expect by the end of this year that we will be capable of producing around 650,000 pieces of 800G and 1.6 Tb products per month." | release | line 5 | PASS |
| H6 | "We expect the first of these new facilities to begin production later in 2026." | 10-Q Item 2 | line 1519 | PASS |
| H7 | "the 1.6T order as early as Q3" | call | line 40 (Murry): "we expect to begin delivering these 800G orders in Q2, the 1.6T order as early as Q3, and to complete all of the deliveries by the end of this year" | PASS verbatim; on the sharpening see §5 |
| H8 | "over $325 million annually in CATV" | call | line 68 | PASS |
| H9 | "our top three customers represented 42%, 26% and 24% of our revenue" | 10-Q Note 2 | line 1027 | PASS |
| H10 | "Should additional liquidity be needed, our Board may authorize issuance of additional common stock under an at-the-market offering in the future" | 10-Q Item 2 | line 2039 | PASS |
| H11 | Closing list: "complete all of the deliveries by the end of this year" (line 40); three-year agreements (line 118, Lin: "three-year long-term agreements with several customers—around three"); "35% gross margin by end of this year" (174); "approaching 200,000 units per month" (release line 5); $3.6M discontinued-products charge (release line 147: "Expenses associated with discontinued products 3,594"; 10-Q line 919) | call; release | as listed | PASS |

### 2i. Prose sentences (36 checked across business.md §1, §5, §6, §7 and outlook §2–§3)

| # | Sentence / fact | Tag | Found at | Result |
|---|---|---|---|---|
| P1 | §1: "large internet-based ("hyperscale") data center operators" and the equipment makers that supply them | 10-K Item 1 | line 177 | PASS |
| P2 | §1: "most established business"; direct sales to MSOs since 2023 under Quantum Bandwidth | Item 1 | line 175 | PASS |
| P3 | §1: amplifiers "contain no optics" but rely on RF electronics and in-house software | Item 1 | line 289 ("do not incorporate optics, but do rely on advanced mixed-signal RF and digital electronic design as well as software and firmware which we develop in house") | PASS |
| P4 | §1: Comcast and Charter upgrading to DOCSIS 4.0 | Item 1 | line 201 | PASS |
| P5 | §1: one segment | Note R | line 3759 "one reportable segment" | PASS |
| P6 | §1: 2,881 of 4,691 employees in China at end-2025 | Item 1 | line 409 | PASS |
| P7 | §1 history: Feb 1997 founding; former University of Houston research scientist; Ningbo (Global) bought 2006; Nasdaq Sept 26, 2013 | DEF 14A; 10-K Item 1; Item 5 | DEF14A line 615 ("senior research scientist from 1994 to 1998 at the University of Houston"); 10-K line 467 ("acquired by Prime World on March 30, 2006"); line 1155 | PASS |
| P8 | §1: Microsoft 46.6% (2023); ATX 47.3% (2022); Digicomm 0% → 53.1% | 10-K FY2023 Item 1; 10-K FY2025 Item 1 | lines 984; 191 | PASS |
| P9 | §1: warrant March 2025, $4B; 2025 revenue +83% | Note C; Item 7 | 10-Q 721 / 10-K 2825; line 1399 (82.8%) | PASS |
| P10 | §2: "subject to rescheduling, revision or cancellation on short notice"; no commitments longer than a year | Items 1, 7 | 1 hit; line 1217 "We do not have any long-term purchase commitments (in excess of one year)" | PASS |
| P11 | §2: "In 2025 sales were still mostly 100G and 400G, with 800G expected to overtake 400G 'later in 2026'" | Item 7 | quote at line 1213; the first half is not in the source (the 10-K gives no 2025 speed mix; the only support is the May call's "800G revenue in the first quarter was $4.6 million, or 5.6% of our total data center revenue", line 38) | **FAIL (label only):** inference presented as sourced fact |
| P12 | §2: "only minimally differentiated"; "strong pricing pressure" | Item 7 | 1 hit each | PASS |
| P13 | §2: Digicomm "to quickly provide products to customers when needed for their network builds"; "the vast majority" amplifiers (CFO); $80.3M / 41.8% computed | 10-Q Item 2; call | line 1997; transcript line 68 (Murry); 147.0 − 66.7 = 80.3 | PASS |
| P14 | §3: COGS 70%; "increased direct material, direct labor and other manufacturing costs associated with increased production volumes"; "high fixed cost base…"; "greatly affected by our sales volume" | Item 8; 10-Q Item 2; Item 1A | line 1355; 10-Q 1713; 1 hit each | PASS |
| P15 | §3: "increased costs associated with certain data center products" **as new lines ramped** cost about $5.0M; $3.6M charge took 1.9 points | 10-Q Item 2; release | line 1719 ($5.0M); release line 147 (3,594); 3,594/191,922 = 1.87% | **FAIL (label only):** the numbers and quote pass; "as new lines ramped" is the writer's explanation, not the 10-Q's, which gives no cause |
| P16 | §3: R&D 18.8%, +55.6%, "customer testing and qualification"; S&M 6.6%, G&A 16.6%; SBC $11.7M; non-GAAP operating loss $10.3M vs GAAP $24.7M | Items 7; Note P; supplemental p.4; release | lines 1441, 1451, 1363–1365; Note P heading line 3584 and line 2444; supplemental p.4 line 196 (10,302); 10-Q 273 | PASS |
| P17 | §3 capital intensity: $335.1M + $289.7M + $8.6M = $633.4M, 185%; $169.0M US capex; 210,000 sq ft; "begin production later in 2026"; four Houston buildings; Pearland; ~400,000 sq ft New Taipei; "through at least the end of 2027"; PP&E 376.1 → 697.1; other assets 50.9 → 324.0 | 10-Q Items 1, 2; Note 4; Note 8; Q1 10-Q Note 19 | 633,457; 184.6%; line 2007; Note 4 line 753 (209,665); 1519; Blue Ridge (755) + three Hightower (757); Q1 10-Q line 1355; 346,212 + 54,086 = 400,298 (751); 2011; 183; 193/965 | PASS. The depreciation proxy ($20–25M) is labelled "our rough proxy" and matches the D&A row for FY2021–FY2023 (worry-list item 3 confirmed); the row is "Depreciation and amortization", see REVISE 12 |
| P18 | §4: receivables +$127.6M, inventory +$100.7M (FY2025); inventory +$94.1M "due to production ramp and build to support anticipated demand"; $314.0M = 1.6 quarters; $211.0M Digicomm, "longer than typical payment terms"; +$11.6M Q2 OCF; AP +$142.2M | 10-K Item 7; 10-Q Items 1, 2; Note 2 | line 1589; 10-Q 1989; 314.0/191.9 = 1.64; 1027, 1997; computed as F6; 1991 | PASS |
| P19 | §4: $750.8M FY2021–25 share proceeds; ~$1.78B total; $83.7M convertible 2023; $125M due 2030; $58.9M loans; 84.6M ≈ 3× 26.9M; deficit $527.1M; equity $1,668.0M | 10-K FY2023 Item 8; 10-K Note L; 10-Q Note 11; cover; Item 1 | 15,397+1,238+68,984+146,293+518,914 = 750,826; +1,028,207 = 1,779,033; line 2330 (83,661); 10-Q 1063; 84.57/26.91 = 3.14; 10-Q 233, 235 | PASS |
| P20 | §5: customers "qualify" with sampling, reliability testing, audits; life-cycle quote; design wins 6, 8, 9; Microsoft 46.6% → 28.8% | Item 1A; Item 7; Item 1 | line 635; line 1217 (verbatim except the source's curly apostrophe and the trailing "or substituting an alternative solution", cut at a clause boundary); line 1219 ("9, 8 and 6"); 191 | PASS |
| P21 | §5: "the majority of the laser chips and optical components…"; "unique in our industry"; "difficult and time-consuming for other vendors to replicate"; CFO "allowed us to avoid some of the shortages…"; "by around 350% by 2027" | Item 1; call | line 183; 1 hit; transcript line 56 (Murry, both) | PASS |
| P22 | §5: "Largely Location-Agnostic"; "a competitive advantage"; US 0.7% of Q2 revenue | deck p.18; Item 1; Note 17 | investor-presentation p.18 line 395 (form-feed count confirmed); 10-K 183, 199; 1,339/191,922 = 0.70% | PASS |
| P23 | §5: "less downward price pressure than many of our competitors in this market"; vendors outsource design and manufacturing; early DOCSIS 4.0 developer | Items 7, 1 | 1 hit; line 175; line 201 "As one of the early developers of DOCSIS 4.0 equipment" | PASS |
| P24 | §5: warrant terms; $84.8M; 24.7% | 10-Q Note 3 | 721; 737; 84.8/343.1 = 24.7% | PASS |
| P25 | §6#1: 42/26/24, top ten 99%; "may increase, decrease, cancel or delay purchase orders already in place without significant penalty" | 10-Q Note 2; 10-K Item 1A | 1027; 1 hit | PASS |
| P26 | §6#2: "If AI adoption slows…negative operating leverage"; "to impair long-lived assets, including construction-in-progress"; inventory $278.8M from $183.1M; $697M plant, $324M prepayments | Item 1A; 10-Q Notes 7, 8 | 1 hit each; 913; 183, 193 | PASS |
| P27 | §6#3: Coherent, Eoptolink, InnoLight, Lumentum, Source Photonics; "may decide to manufacture the optical subsystems incorporated into their network systems in-house" | Item 1 | 1 hit each; line 379 | PASS |
| P28 | §6#4: CATV $118.2M → $59.9M; Comcast and Charter "have announced plans to spend billions of dollars over the next few years" | 10-K FY2023 Note C; Item 1 | 2622; line 201 | PASS |
| P29 | §6#5: 7.8M shares for $1,028.8M net; $101.72 to $197.26; "Should additional liquidity be needed…"; $106.5M unused; $499.7M cash | 10-Q Item 2; Item 1 | ATM table lines 1945–1953 (7,775,523; $1,028,817; the four monthly prices are 104.03, 101.72, 181.24, 197.26, so min/max correct); 2039; 1927; 171 | PASS |
| P30 | §6#6: 57.5% FY2025 and 44.2% 6M 2026 made in China; tariffs struck down February 2026; ~$5.9M refunded; "not always establish the country of origin for these products as China for U.S. tariff purposes" | 10-K Item 7; 10-Q Note 17; **Note 19**; Item 2 | 973/1283; 151,486/343,066 = 44.16%; the February 20, 2026 Supreme Court ruling is at line 1479, inside **Note 18** (Commitments and Contingencies, begins 1463); the $5.9M aggregate is in Note 19 (1485); quote at 1519 | **FAIL (tag):** Note 18 missing from the tag. **Fixed directly.** Also see REVISE 11 on "on Chinese-origin goods" |
| P31 | §6#7: "If our MBE or MOCVD fabrication facility in Sugar Land, Texas were to be damaged or destroyed for any reason, our manufacturing process would be severely disrupted" | Item 1A | 1 hit | PASS |
| P32 | §7: Lin 63, founded Feb 1997, CEO since inception, Chairman since Jan 2014; Murry 53, joined Feb 1997 as engineer, CFO since Aug 2014; seven directors in three classes; Yeh lead independent director since 2000; Black 92, since 2001; officers and directors 3.8%, Lin 1.8%; Jane Street and Vanguard 5.1% each, the only 5% holders; Lin's May 2026 plans for 80,000 and 144,000 shares | DEF 14A; 10-Q Part II Item 5 | DEF14A 615, 489, 1157 ("Age: 53"), 1165 ("Senior Engineer of Device Packaging from February 1997"), 529 ("two Class I … two Class II … three Class III"), 483, 657, 2209, 491, 2885, 2861, 2855–2857 (two entries under "5% or Greater Stockholders"); 10-Q 2115–2121 | PASS |
| P33 | §7 pay: 25% revenue / 25% non-GAAP operating income / 50% design wins; 104.8%; revenue and design wins at maximum, profit short ($11.17M loss); 50/50 RSU/PSU; three-year relative TSR vs peers plus price hurdles; 2022 PSUs at 200%; $4.77M; 469:1; 84.5%; 97.45% | DEF 14A CD&A; SCT; Pay-Ratio | 1439–1443; 1451; 1441; 1231, 1485; 1545–1549; 1649 (4,769,014); 2039; 2043; 1113 | PASS |
| P34 | §7: dividends never, loan agreements restrict; "Warrants contra revenue" $2.1M; fully vested ≈ 9% of August share count | 10-K Item 5; 10-Q Note 3, Item 1 | 1181; 485 (2,130); 7,945,399 / 84,569,237 = 9.4% | PASS |
| P35 | outlook §2: CEO release quote; CFO "is limited by our production capacity and supply chain, not market demand, which we believe is much larger" | release; call | release line 4 verbatim; transcript line 86 (Murry) | PASS |
| P36 | outlook §3: $4.6M 800G in Q1; "approaching 200,000 units per month"; CFO "on track to begin to contribute to our overall revenue later this year"; CFO "initial production in this facility in the third quarter", "about 30%"; US $1.3M; "high-volume adoption of our 1.8 GHz CATV products"; "another long-term major hyperscale customer" / "return this customer as a 10%-plus customer" | call; release; 10-Q Note 17 | lines 38, 52, 46, 50 (all Murry); release 5, 4; 10-Q 1441; lines 32 (Lin), 42 (Murry) | PASS |

**Totals: 111 checked; 108 PASS; 3 FAIL (P11 label, P15 label, P30 tag — the tag fixed directly); 0 UNVERIFIABLE.**

---

## 3. Invented-number and inference check

No invented numbers. Every figure traces to a cached source line or to a labelled computation whose arithmetic re-derives. Every $-thousand figure was converted correctly. Items where interpretation is presented as, or shades into, fact:

1. **§6#1 Microsoft and Amazon (worry-list item 2).** The sentence is labelled ("our inference from the FY2025 10-K and the warrant disclosure is Microsoft and Amazon, but the 10-Q does not say"), which is the right form. It should stay, but the basis is stronger for one name than the other and the text should say so. Amazon ≈ the 24% customer is close to arithmetic: 10-Q Note 3 (line 721) says the warrant's value is recognized "as a reduction of revenue from Amazon", the only warrant-linked customer, and warrant-linked revenue of $46.8M (computed) is 24.4% of Q2 revenue. Microsoft ≈ the 26% customer rests only on Microsoft being the sole other named data-center customer (28.8% of FY2025). The sources offer a third candidate the reader should hear about: Oracle was a 12.4% customer in FY2024 (10-K FY2025 line 2614), and the May call described the second hyperscaler as one whose orders would "return this customer as a 10%-plus customer" (transcript line 42). Verdict: keep as an inference, state the two different bases, and mention that the filings never link the 26% and 24% to names.
2. **outlook §3 heading "A second hyperscaler and the Amazon warrant."** The paragraph itself is careful (it juxtaposes without asserting), but the heading joins the two with "and" and a reader will take them as the same customer. Nothing in the sources identifies the "another long-term major hyperscale customer" (line 32) as Amazon. Reword the heading or add "our inference: the sources do not say whether this is Amazon".
3. **§6#1 and table: "the 42% is Digicomm".** Not stated by the 10-Q, which ranks without naming in the quarter column. Supported by two matches: six-month Digicomm 42.8% (line 2001) against six-month top customer 43% (line 1027), and the computed Q2 41.8% against 42%. Acceptable; a six-word clause giving the basis would make it airtight.
4. **§2 line 18: "In 2025 sales were still mostly 100G and 400G".** Inference (P11). Basis available: the 10-K's "sales of 800 Gbps products will likely exceed sales of 400 Gbps products later in 2026" (line 1213) and the May call's "800G revenue in the first quarter was $4.6 million, or 5.6% of our total data center revenue" (line 38). Label it and cite the second.
5. **§3 line 41: "as new lines ramped".** Inference (P15). The 10-Q attributes the $5.0M only to "increased costs associated with certain data center products" (line 1719); the ramp explanation is the writer's. Label ("our reading") or cut. The same framing recurs in §6#3 ("persisting past the ramp").
6. **§3 line 45, depreciation as "the cost of standing still" (worry-list item 3).** Labelled "our rough proxy … (the filings do not split maintenance from growth spending)". The $20–25M range matches the D&A row for FY2021–FY2023 (25.4, 23.2, 20.4; FY2024 20.6). Fine as labelled. Nit: the cash-flow line is "Depreciation and amortization"; amortization is small (intangible purchases run $0.4–0.6M a year, 10-K cash-flow statements) but the word should match the row.
7. **Two six-month share-proceeds totals.** $1,028.2M (cash-flow statement, 10-Q line 539; used in the §4 table, §7 table and outlook §1 row 8's computation) and $1,028.8M (Item 2 ATM table, line 1953; used in §6#5 and §8 indicator 8). Both are sourced and both are real, but the report never says why they differ, and a reader will think one is a typo. One footnote, and one figure for the indicator.
8. **§6#6: "Tariffs on Chinese-origin goods imposed in 2025 were partly struck down in February 2026".** The 10-Q says the Supreme Court invalidated "certain tariffs previously imposed under the International Emergency Economic Powers Act" (line 1479). The China-specific framing is the writer's; the source does not limit the ruling to Chinese-origin goods. Reword toward the source.
9. **Worry-list item 4 (Hightower option, Pearland price).** Both figures are in the cached filings in full dollars, not thousands: "aggregate purchase price of $102,250,000" (10-Q Q2 2026 Note 4, line 757) and "a total purchase price of approximately $58.4 million" (10-Q Q1 2026 Note 19, line 1355; the Q2 10-Q does not mention Pearland, so whether the purchase closed by June 30 is not disclosed). **Restored directly** in §3 with those exact figures; the sentence's existing tags already cover both notes.
10. **Worry-list item 5 (outlook §1 rows 6 and 8).** Arithmetic verified exactly (F6, F8); labels "(all computed, six-month less Q1)" and "(computed)" present. One caveat in REVISE 8.
11. **Worry-list item 7 (claim 7).** See §5 below: a fair labelled sharpening, but its gradeability depends on a disclosure management does not make routinely.
12. **Paragraphs that are mostly numbers (§3 rule 5).** §3 line 45 (capital intensity) carries fifteen figures after the reviewer's two restorations; §4 line 81 carries eight; §6#5 six. The §3 paragraph duplicates the table beneath it for capex and deposits; the facilities and balance-sheet figures want a four-row table ("Expansion footprint") rather than prose.

---

## 4. Jargon and readability audit

Read as a smart 16-year-old with no finance or optics background.

**(a) Terms used without being plain, name-inferable, or in the glossary** (items marked *fixed* were glossed directly; see "Fixed directly"):

| Term | Where | Status |
|---|---|---|
| segment ("reports one segment") | business §1 line 10 | *fixed* |
| fab ("the laser fab") | §3 line 39; §5 line 87 | *fixed* at first use |
| depreciation | §3 line 45 (first use; the table row follows) | *fixed* |
| restricted cash | §4 table row; §4 footnote | *fixed* (footnote gloss) |
| tranches / vesting | §5 line 93; outlook §3 line 35 | *fixed* both |
| operating leverage (inside a 10-K quote) | §6#2 | *fixed* (gloss after the quote) |
| impairment / write-down | §6#2 | *fixed* (plain phrase replaces "write-down") |
| gross-profit bridge | §6#3 | *fixed* (plain phrase) |
| three classes (board) | §7 line 129 | *fixed* |
| lead independent director | §7 line 129 | *fixed* |
| weighted basic (share count) | outlook §1 row 8 | *fixed* (plain phrase; no value changed) |
| "vs the guided range" | business §8 indicator 3; outlook §1 row 3 | **not fixed** (indicator list is the owner's to lock); suggest "vs the range management forecast" |
| dilution ("Dilution is the cost of the funding") | §8 indicator 8 | **not fixed** (indicator list); suggest "(each existing share owns a smaller slice)" |
| ramp / ramped | §3, outlook §2–§3 | borderline; understood as "scale up" from context; left |
| "Tells:" (poker idiom for a signal) | outlook §3, four times | left; "Signs to watch:" would be plainer (REVISE 14) |
| construction-in-progress, utilization rates | inside 10-K quotes, §6#2 | plain enough from the words; left |
| purchase orders, receivables, accounts payable, accumulated deficit, operating cash flow, free cash flow, gross margin, operating margin, contra revenue | various | all defined inline at first use by the writer. Good |
| hyperscale / hyperscaler, CATV / MSO, DOCSIS 4.0 / 1.8 GHz, 800G / 1.6T, qualification / design win, GAAP / non-GAAP, ATM program, convertible notes, warrant, capex, free cash flow, optical transceiver, laser chip (MBE/MOCVD) | glossary | all present and all used in the text |

**(b) Glossary contents (§3 rule 4).** Thirteen entries; every one is used in the body and none is avoidable jargon except arguably "Capex" and "Free cash flow", which the writer also defines inline; keeping both is harmless. Nothing unused (CPO-style dead entries: none). No additions needed after the inline glosses above.

**(c) Sentences that assume prior knowledge.** §4 "stockholders' equity of $1,668.0 million is almost entirely money shareholders paid in" explains itself; §7 "performance units judged on three-year shareholder return against peers and share-price hurdles" is followable. outlook §1 row 3 "guided range" is the only remaining stopper, and it is the owner's at lock.

**(d) GAAP vs non-GAAP.** Explained at first use in §3 ("non-GAAP gross margin, which strips out that charge and stock pay") and again in the glossary; the §3 table's non-GAAP row comes after that sentence. Good; the pilot's ordering problem does not recur here.

**(e) Banned-word sweep** (leverage, synergy, headwind, tailwind, monetize, ecosystem, at scale, robust, unlock, TAM): the only hit is "negative operating leverage" inside a verbatim 10-K risk-factor quote in §6#2, now glossed. The writer trimmed the release's "robust" out of the CEO quote in outlook §2. Good.

**(f) Tables that have become walls.** outlook §1 rows 1, 5, 6 and 8 each hold two or three values plus a quote plus tags; readable but dense. business.md tables are clean.

---

## 5. Claims quality (outlook.md §5)

Count: 10 (target 6–12). Headline revenue/profit claims: 1, 2, 3, 4 (four of ten); the rest are capacity, facility, product, customer-concentration and funding signals. Balance is right. No either/or construction that cannot fail (claim 5's "restates … or raises it" is the permitted form; claim 6's "release or 10-Q" is about where to look, not about direction). Every claim has its verbatim quote and tag. Sharpenings (7, 8) are labelled "Our sharpening". Disclosure checks (9, 10) are labelled and 9 states the quarter column. Tier-none closing list present and specific.

| # | Testable? | Metric / date / event | Quote supports? | Gradeable mechanically next quarter? | Notes |
|---|---|---|---|---|---|
| 1 | Yes | Q3 revenue $255–290M | Yes | Yes | |
| 2 | Yes | Q3 non-GAAP GM 29–30.5% | Yes | Yes | |
| 3 | Yes | FY2026 revenue > $1.1B reaffirmed | Yes (May, CEO) | Yes; silence = Dropped | The Q2 release did not repeat it; the claim correctly makes that the test |
| 4 | Yes | FY2026 non-GAAP operating income > $140M reaffirmed | Yes | Yes; silence = Dropped | H1 non-GAAP operating loss was $17.6M (supplemental p.4: 7,286 + 10,302), so this is a live test, not a formality |
| 5 | Yes | ~650k/month year-end capacity restated or raised | Yes (release) | Yes | |
| 6 | Yes | Sugar Land facility began production, per release or 10-Q | Yes | Yes | |
| 7 | Yes, labelled sharpening | 1.6T revenue reported for Q3, any amount | "as early as Q3" (line 40) is the CFO's earliest case, hedged; the firmer statement is "on track to begin to contribute to our overall revenue later this year" (line 52) | **Partly.** Depends on management disclosing a 1.6T figure. The 800G dollar figure was given only on the Q1 call (line 38), not in the Q2 release; with tier none for Q2 and possibly Q3, this claim may be ungradeable | Fair as a labelled sharpening (worry-list item 7); add "if no 1.6T figure or statement is disclosed, grade Dropped, not Missed", or reword to "the Q3 release or call states that 1.6T products shipped or contributed revenue in Q3" |
| 8 | Yes, labelled sharpening | Q3 CATV ≥ $81.25M | "over $325 million annually" (line 68), said "Looking further ahead" | Yes | Two readings: a 2026 total (then H1's $147.4M implies about $88.8M a quarter in H2, computed) or a run-rate (then $81.25M). The label covers it, but say which reading you took |
| 9 | Yes, disclosure check | Three customers >10% in the Q3 quarter column | Yes | Yes | Labelled; column stated |
| 10 | Technically, but nearly unfailable | Cover share count > 84,569,237 | Yes | Yes, but RSU vesting alone raises the count every quarter, so this cannot realistically fail | Replace with management's own number: the Q3 guide uses "approximately 92.8 million shares" [Q2 2026 release line 22] against 84.6M outstanding on Aug 3, which implies roughly 8M more shares to be sold in Q3 (computed). Claim: "Q3 2026 weighted-average basic shares are approximately 92.8 million or more, management's own assumption" — or "the Q3 10-Q's ATM table shows shares sold in July–September 2026" |

---

## 6. Rubric (§14), from the reader's chair

1. **What the company does and who pays, in two sentences?** Yes. It makes the plug-in light modules that link machines inside AI data centers and the amplifiers cable companies need for their DOCSIS 4.0 upgrade; a handful of giant customers (Digicomm for cable, two unnamed hyperscalers for data center, together about 92% of revenue) pay per unit on cancellable purchase orders.
2. **What would kill it and the early warning sign?** Yes. §6 is ranked, each scenario has a sign, the concentration table is exactly the right thing to watch, and #7 is honest that the single laser fab has no early warning.
3. **Why the margins are what they are and whether cost scales with usage?** Yes. §3 is the strongest section: cost rises with every unit, the margin depends on how full the fixed-cost factory is, new products start low by design, and the "capex versus depreciation" framing shows the reader the scale of the bet without needing finance.
4. **Could I predict next quarter's scorecard from §5 alone?** Mostly. Eight of ten claims are mechanical; claim 7 depends on a disclosure management may not make, and claim 10 will almost certainly be ✅ regardless of anything that matters.
5. **Did nothing require knowledge I don't have?** Before fixes, no: segment, fab, depreciation, tranches, vesting, operating leverage, impairment, bridge, board classes, lead independent director and "weighted basic" each stopped the reader. All are now glossed inline. "Guided range" and "dilution" remain in the indicator list for the owner.

---

## 7. Verdict: REVISE

Numbered list for the writer (numbers, quotes, table values, claims and the indicator list are untouched by the reviewer and must be changed by the writer). Both files are within 20 words of their ceilings after the reviewer's glosses, so items 9 and 10 (cuts) should be done first.

1. **business.md §6#1 and outlook §3 heading.** Split the Microsoft/Amazon inference by strength: "Amazon is very likely the 24% customer, because 10-Q Note 3 recognizes the warrant as a 'reduction of revenue from Amazon' and warrant-linked revenue of $46.8M (computed) is 24.4% of the quarter; Microsoft is our guess for the 26% only because it is the one other data-center customer the FY2025 10-K names (28.8%); Oracle, 12.4% in FY2024, is the other candidate and the May call's second hyperscaler was one that would 'return … as a 10%-plus customer' [10-Q Q2 2026, Note 3; 10-K FY2025, Item 1; Note B; Q1 2026 call]." Retitle outlook §3's fourth block (e.g., "A second hyperscaler; the Amazon warrant") or add "our inference: the sources do not say whether this customer is Amazon".
2. **business.md §3 line 41.** Label or cut "as new lines ramped"; the 10-Q gives no cause for the $5.0M beyond "increased costs associated with certain data center products". Same for "persisting past the ramp" in §6#3.
3. **business.md §2 line 18.** Label "In 2025 sales were still mostly 100G and 400G" as inference and give its basis: 800G to exceed 400G "later in 2026" [10-K FY2025, Item 7]; Q1 2026 800G revenue "$4.6 million, or 5.6% of our total data center revenue" [Q1 2026 call].
4. **Share-proceeds totals.** Add one footnote (to the §4 table or §6#5): "The 10-Q's cash-flow statement shows $1,028.2M of net proceeds [Item 1]; its ATM table shows $1,028.8M [Item 2]; the report uses the cash-flow figure in tables and the ATM figure where the share count and prices come from that table." Then use one figure in §8 indicator 8 and outlook §1 row 8.
5. **Claim 7.** Keep the labelled sharpening but add the grading rule: "If neither the Q3 release nor any Q3 call statement mentions 1.6T shipments or revenue, grade Dropped, not Missed." Or reword to the observable: "The Q3 2026 release or call states that 1.6T products shipped or contributed revenue in Q3 (our sharpening of 'as early as Q3')."
6. **Claim 10.** Replace with the guidance-anchored version: "Q3 2026 weighted-average basic shares are approximately 92.8 million or more, management's own guidance assumption. 'using approximately 92.8 million shares' [Q2 2026 release]." (84,569,237 on Aug 3 → 92.8M implies roughly 8M more shares in Q3, computed.) Or a disclosure check on the Q3 10-Q's ATM table showing July–September sales.
7. **Claim 8.** State which reading of "over $325 million annually" the $81.25M threshold takes (run-rate). If the 2026-total reading is intended, the H1 figure of $147.4M [10-Q Q2 2026, Note 3] implies about $88.8M a quarter in H2 (computed).
8. **outlook §1 row 6 and business §8 indicator 6.** Footnote that the Q1 10-Q's line is "Deposits and deferred charges" (9,744) while the Q2 10-Q's six-month line is "Prepayment for equipment and others" (289,744), so the Q2 figure of $280.0M assumes the two are the same line; and name the cash-flow line in indicator 6's "where it comes from" so the refresh finds it.
9. **outlook.md duplication.** The 650k/month capacity, "about 30%" from Texas, "$325 million annually" and 1.6T "later this year" each appear in two or three of §3, §4 and §5. Cut the §4 "Standing statements" bullets already quoted in §3 (bullets 2, 4), or move the §3 quotes into §4 and leave §3 with the plain-words summary. This pays for items 1, 5–8.
10. **business.md §1.** Fold paragraph 3 (telecom, three sites, headcount) into §2 "Telecom and other" and §3's capital-intensity paragraph, or cut it to one sentence, so §1 is two or three paragraphs plus history (skeleton) and the file has room for items 1–4. Consider turning §3 line 45's facilities and balance-sheet figures into a four-row "Expansion footprint" table (§3 rule 5).
11. **business.md §6#6.** "Tariffs on Chinese-origin goods imposed in 2025 were partly struck down in February 2026" → "In February 2026 the Supreme Court invalidated 'certain tariffs previously imposed under the International Emergency Economic Powers Act'; AOI has since recovered about $5.9 million [10-Q Q2 2026, Note 18; Note 19]." The source does not limit the ruling to Chinese-origin goods.
12. **business.md §3 line 45.** "below depreciation of $20–25 million a year" → "below depreciation and amortization of $20–25 million a year" to match the table row, or note that amortization is small.
13. **Indicator list (owner to review at lock; reviewer did not touch).** #3: "vs the guided range" → "vs the range management forecast" (also outlook §1 row 3 header). #8: gloss "dilution" ("each existing share owns a smaller slice"). #6: name the cash-flow lines as they appear.
14. **Optional wording.** outlook §3 "Tells:" → "Signs to watch:". §2 table footnote: Q2 2026 percentages are the company's (10-Q Note 3), not computed. §6#1: add the one-clause basis for "the 42% is Digicomm" (six-month 42.8% vs 43%; computed Q2 41.8%).

---

## Fixed directly (jargon glosses, one tag, two restored figures; no table value, quote, claim or indicator changed)

business.md
- Line 10: "the company reports one segment" → "the company reports one segment (it does not split profit by business line)".
- Line 39: "owns the laser fab" → "owns the laser fab (the factory that makes the laser chips)".
- Line 45: "below depreciation of $20–25 million" → "below depreciation (the yearly charge spreading equipment cost over its useful life) of $20–25 million".
- Line 45: restored the two dropped figures inside the existing sentence and tags: "four Houston buildings and a Pearland site have been leased or contracted (the three Hightower buildings in Houston carry an option to buy them for an aggregate $102,250,000; the Pearland property was contracted in April 2026 for approximately $58.4 million)" — sources 10-Q Q2 2026 Note 4 line 757 and 10-Q Q1 2026 Note 19 line 1355, both already in the sentence's tag.
- Line 77 (§4 table footnote): appended "Restricted cash is cash set aside that the company cannot freely spend."
- Line 93: "Sign: no further tranches vesting." → "Sign: no further tranches (portions of the warrant) vesting, that is, becoming exercisable."
- Line 115: added "(operating leverage: fixed costs magnifying profit swings)" after the 10-K quote; "impairment (write-down) language" → "impairment language (a charge admitting that plant is worth less than its book value)".
- Line 117: "the 10-Q gross-profit bridge" → "the 10-Q's list of what moved gross profit".
- Line 123: tag "[10-K FY2025, Item 1A; 10-Q Q2 2026, Note 19; Item 2]" → "[…; 10-Q Q2 2026, Note 18; Note 19; Item 2]" (the February 2026 ruling is in Note 18, line 1479; the $5.9M is in Note 19, line 1485).
- Line 129: "seven members in three classes; lead independent director William Yeh" → "seven members in three classes (a third stand for election each year); lead independent director (the non-management director who leads the independent directors) William Yeh".

outlook.md
- Line 19 (§1 row 8, text only): '"approximately 80.7 million shares" weighted basic for Q2' → '"approximately 80.7 million shares" as the average share count behind Q2 per-share guidance'.
- Line 35: "warrant tranches vesting" → "further warrant tranches (portions of the warrant) vesting".

Backups of the pre-fix drafts: `/tmp/aaoi_business.md.bak`, `/tmp/aaoi_outlook.md.bak`.

---

## Word counts (`python3 /tmp/aaoi_wc_prose.py`, prose only per §3 rule 7)

| File | Before reviewer fixes | After | Target | Status |
|---|---|---|---|---|
| business.md | 2,877 | 2,987 | 2,000–3,000 | In range, 13 words of headroom; upper half. Padding candidates: §1 paragraph 3; §3 line 45 (prose repeating the table); §5 "honest caveat" overlaps §2 and §6#1 |
| outlook.md | 1,178 | 1,183 | 800–1,200 | In range, 17 words of headroom. Padding: §4 "Standing statements" bullets 2 and 4 repeat §3; the §1 year-ago line could be a footnote |

Raw `wc -w` (including tables, tags, glossary, sources) is 5,239 and 1,861 before fixes, for reference only.

---

## Cycle 2 (re-check of the writer's second pass; review cycle 2 of 2)

_Re-checked 2026-09-07 against `sources/2026-Q2/` only (cutoff 2026-08-06; source-file timestamps unchanged since the gather, so nothing was re-fetched or edited). The writer's reported counts were verified, not taken on trust: `python3 /tmp/aaoi_wc_prose.py` gave business.md 2,839 and outlook.md 1,118 before the reviewer's cycle-2 glosses (2,839 and 1,139 after)._

**Final verdict: PASS.** All 14 REVISE items resolved. Every new or changed number and quote verifies against the cached filings and releases; all 13 cycle-1 direct edits are intact (two relocated by the writer's restructuring); no post-cutoff item; skeleton, header lines, `_Proposed — owner to review and lock._` and both Sources tables complete. Three cosmetic glosses fixed directly in this cycle (below). Nothing factual or structural remains open. Two notes are left for the owner at indicator lock, neither blocking.

### 1. Status of the 14 REVISE items

| # | Item | Status | Where (current line numbers) |
|---|---|---|---|
| 1 | Microsoft/Amazon inference split by strength; Oracle named; outlook §3 heading | **Resolved.** "Our inference, with unequal confidence: the 24% is very likely Amazon, because the 10-Q books the warrant 'as a reduction of revenue from Amazon' and warrant-linked revenue of $46.8 million (computed) is 24.4% of the quarter; the 26% is only a guess at Microsoft … Oracle (12.4% in FY2024) is also a candidate". Heading now "A second hyperscaler; the Amazon warrant" with "the sources do not say whether this is Amazon" | business.md 111; outlook.md 33 |
| 2 | "as new lines ramped" unlabelled | **Resolved.** "(the 10-Q gives no cause; our reading is start-up cost on new lines)"; §6#3 "persisting beyond the next two quarters (our threshold; the 10-Q gives no cause)" | business 39, 127 |
| 3 | "mostly 100G and 400G" unlabelled | **Resolved.** "(our inference: the 10-K expected 800G to overtake 400G only 'later in 2026', and on the May call 800G was put at '5.6% of our total data center revenue' for Q1 2026) [10-K FY2025, Item 7; Q1 2026 call]" | business 16 |
| 4 | Two share-proceeds totals | **Resolved.** Footnote under the §4 table names both figures and says which sections use which; §7 table keeps the cash-flow $1,028.2M, §6#5 and §8 indicator 8 the ATM-table $1,028.8M; outlook §1 row 8 now states "(ATM table)" and uses ATM-row figures for both quarters | business 87, 131, 149, 171; outlook 19 |
| 5 | Claim 7 transcript-dependent | **Resolved.** Reworded to the observable "The Q3 2026 release or call states that 1.6T products shipped or contributed revenue in Q3", sharpening labelled, "if 1.6T goes unmentioned, grade Dropped, not Missed" | outlook 56 |
| 6 | Claim 10 nearly unfailable | **Resolved.** Replaced by "The share count used for Q3 2026 non-GAAP per-share results is approximately 92.8 million or more, management's own guidance assumption", with the release quote | outlook 59 |
| 7 | Claim 8 reading of "$325 million annually" | **Resolved.** States the run-rate reading and the alternative: "as a 2026 total it would imply about $88.8 million a quarter in H2 after $147.4 million in H1 (computed)" | outlook 57 |
| 8 | Cash-flow line label change (row 6 / indicator 6) | **Resolved.** Both name "Deposits and deferred charges" (Q1 10-Q) and "Prepayment for equipment and others" (Q2 10-Q) and say the subtraction assumes the same line | outlook 17; business 169 |
| 9 | Outlook duplication | **Resolved.** §4 bullets on 650k/month and $325M cut (four bullets remain); "beat the May range" clause cut from §3; year-ago sentence folded into a table column. 1,178 → 1,118 | outlook 39–44 |
| 10 | business §1 fold; §3 number-heavy paragraph | **Resolved.** §1 is two paragraphs plus History; the sites/headcount sentence moved into a new nine-row "Footprint and expansion" table; the capital-intensity paragraph now carries four figures instead of fifteen. 2,987 → 2,839 | business 4–10, 43–55 |
| 11 | §6#6 tariff wording | **Resolved.** "In February 2026 the Supreme Court invalidated 'certain tariffs previously imposed under the International Emergency Economic Powers Act', AOI has since recovered about $5.9 million … [10-Q Q2 2026, Note 18; Note 19; Item 2]" | business 133 |
| 12 | "depreciation" vs the D&A row | **Resolved.** "depreciation and amortization (the yearly charge spreading equipment and similar costs over their useful lives)" | business 43 |
| 13 | Indicator-list wording | **Resolved** (pre-lock, so the writer could edit). #3 "vs the range management forecast" (mirrored in outlook §1 row 3); #6 names the three cash-flow lines; #8 "Dilution (each existing share owns a smaller slice)" and "per the ATM table" | business 166, 169, 171; outlook 14 |
| 14 | Optional wording | **Resolved.** "Signs to watch" replaces "Tells" (four places); §2 footnote "Percentages are the company's, rounded"; §6#1 gives the Digicomm basis "(its six-month share is 42.8% against a 43% six-month top customer, and Q2 computes to 41.8%)" | outlook 27–33; business 31, 111 |

**14 of 14 resolved.**

### 2. New and changed numbers and quotes

| Item | Value in draft | Found at | Result |
|---|---|---|---|
| Footprint row 1: Sugar Land makes laser chips and, since 2026, data center transceivers | — | 10-Q line 1519 ("laser chips … transceivers for the internet data center market"); FY2025 10-K line 337 lists no transceivers at Sugar Land, so "since 2026" is a fair reading | PASS |
| Footprint row 2: Taipei transceivers and CATV amplifiers; ~400,000 sq ft New Taipei City | — | 10-Q 1519; Note 4 line 751: 346,212 sq ft (Sept 1, 2025 lease) + 54,086 sq ft (Oct 28, 2025 lease) = 400,298 | PASS on the number; "under a September 2025 agreement" omitted the October lease — **fixed directly** to "September and October 2025 agreements" |
| Footprint row 3: Ningbo; 2,881 of 4,691 employees | — | 10-K line 409 | PASS |
| Footprint row 4: 209,665 sq ft; lease from March 31, 2026; "begin production later in 2026" | — | Note 4 line 753 ("approximately 209,665 square feet … commencing on March 31, 2026"); 1519 | PASS |
| Footprint row 5: one Houston building leased February 2026; three Hightower buildings May 2026; option $102,250,000 | — | Note 4 lines 755 ("On February 23, 2026 … Blue Ridge … Houston"), 757 ("On May 8, 2026 … three industrial buildings … aggregate purchase price of $102,250,000") | PASS |
| Footprint row 6: Pearland, April 2026, ~$58.4M; closing not disclosed in Q2 10-Q | — | 10-Q Q1 2026 Note 19 line 1355 ("On April 7, 2026 … total purchase price of approximately $58.4 million"); `grep -F Pearland` in 10-Q-2026-Q2.txt = 0 hits | PASS |
| Footprint row 7: 6M 2026 capex by location US 169.0 / Taiwan 62.8 / China 103.3 | [10-Q Item 2] | line 2007, verbatim; sums to 335.1 | PASS |
| Footprint row 8: 335.1 + 289.7 + 8.6 = 633.4 (computed) | [10-Q Item 1] | 335,132 + 289,744 + 8,581 = 633,457 | PASS |
| Footprint row 9: PP&E 376.1 → 697.1; other assets 50.9 → 324.0 | [10-Q Item 1; Note 8] | lines 183, 193, 965 | PASS |
| §3 line 43: $633.4M, 185% (computed) | — | 633,457 / 343,066 = 184.6% | PASS |
| §2 line 16 quotes: "later in 2026"; "5.6% of our total data center revenue" | [10-K Item 7; Q1 2026 call] | 10-K line 1213; transcript line 38 (Murry) | PASS, verbatim |
| §6#1: "as a reduction of revenue from Amazon"; 24.4%; 42.8% / 43% / 41.8%; 28.8%; 12.4% | [10-Q Note 3; 10-K Item 1; Note B; call] | 10-Q line 721 verbatim; 46,800 / 191,922 = 24.38%; 10-Q lines 2001, 1027, (147.0−66.7)/191.9; 10-K lines 191, 2614; transcript line 42 | PASS |
| §6#6: "certain tariffs previously imposed under the International Emergency Economic Powers Act"; ~$5.9M | [Note 18; Note 19] | 10-Q lines 1479 (Note 18), 1485 (Note 19) | PASS, verbatim |
| §4 footnote: $1,028.2M (cash flow) vs $1,028.8M (ATM table) | [Item 1; Item 2] | lines 539 (1,028,207), 1953 (1,028,817) | PASS |
| §4 line 91: convertible $125M due 2030; bank loans $58.9M | [Note L; Note 11] | 10-K 1565; 10-Q 1063 | PASS |
| outlook §1 year-ago column: DC $44.8M 43.5%; CATV $56.0M; non-GAAP GM 30.4%; top customer 54%; inventory $138.9M; 6M 2025 OCF ($116.4M) vs $53.9M + $21.2M; 6M 2025 proceeds $195.8M | [10-Q Note 3; release; Note 2; supplemental p.2; 10-Q Item 1] | 10-Q 693, 695 (release also carries 44,791 and 56,019); release line 9; 10-Q 1027; supplemental p.2 line 51 sixth column; 10-Q 505 (116,389), 509 (53,868), 513 (21,181), 539 (195,770) | PASS. Row 6's year-ago cell is honestly labelled "6M 2025" because the Q2 10-Q gives only six-month cash flows |
| outlook §1 row 8: $646.2M Q2 (computed from April–June ATM rows); $382.6M Q1 | [10-Q Q2 Item 2; 10-Q Q1 Item 2] | 107,372 + 345,249 + 193,568 = 646,189 (lines 1947–1951); Q1 10-Q line 1685 net proceeds $382,628 | PASS |
| Claim 8: $147.4M H1 CATV; ~$88.8M/quarter | [10-Q Note 3] | 147,419 (line 711); (325 − 147.4) / 2 = 88.8 | PASS |
| Claim 10: "using approximately 92.8 million shares"; Q2 diluted count 88.2M; ~4.6M more | [Q2 2026 release] | release line 22 verbatim; reconciliation "Shares used to compute diluted earnings per share | 88,152"; 92.8 − 88.2 = 4.6 | PASS |
| outlook §3: "24.4% of the quarter" | [Note 3] | as above | PASS |

All previously verified table cells (business §2, §3, §4, §6, §7; outlook §1 current and prior-quarter columns) are unchanged and were spot-re-read; no value moved.

### 3. Cycle-1 direct edits: all 13 intact

Segment gloss (relocated by the writer into §2 line 14 as "it reports one segment, so profit is not split by business line"); fab gloss (37); depreciation gloss (43, adapted to "depreciation and amortization"); Hightower $102,250,000 and Pearland $58.4M (relocated into Footprint rows 5–6); restricted-cash footnote (87); tranches gloss (103); operating-leverage gloss and impairment plain phrase (125); "list of what moved gross profit" (127); Note 18 tag (133); board-classes and lead-independent-director glosses (139); outlook "average share count behind Q2 per-share guidance" (19); outlook tranches gloss (33).

### 4. Claims (§9)

Ten claims. 1–6 and 10 are management statements (10 is management's own guidance share count); 7 and 8 are labelled sharpenings; 9 is a labelled disclosure check stating the quarter column. Each has a verbatim quote and tag (all re-checked with `grep -F`). Single direction throughout (5's "restates … or raises" is the permitted form; 6's and 7's "release or 10-Q/call" is about where to look). Each can fail: 7 fails if management says 1.6T slipped, and its "unmentioned = Dropped" rule is stated; 10 fails if the Q3 share count is materially below 92.8M. Headline claims are four of ten. Tier-none closing list present. All ten are gradeable mechanically next quarter.

### 5. Structure, header lines, glossary, sources, as-of

- business.md: `# … — The Business`; `_As of Q2 2026 (three months ended June 30, 2026). Written 2026-09-07._`; §1–§8 in order; §1 now two paragraphs plus History; `_Proposed — owner to review and lock._` present; Glossary 13 entries, all used; Sources table maps all 10 tag prefixes used (compound tags split) to existing files, page conventions stated.
- outlook.md: `# … — Outlook as of Q2 2026`; `_Transcript source tier: none. …_`; §1–§5, §6 omitted, Sources maps all 6 prefixes. §1 table now has a fourth column "Q2 2025 (year ago)" in addition to the three the §7 skeleton names; the required columns are all present and the extra column replaces the dense year-ago sentence, so this is accepted as a company-specific addition (owner may drop it at lock).
- As-of: `grep` for August 2x, September 2026, Q3 results, later 8-Ks: zero hits in either file. The only "August 2026" is the Aug 3, 2026 cover share count from the 10-Q filed Aug 6.
- Banned words: only "negative operating leverage" inside the glossed 10-K quote.
- Number-dense paragraphs: §6#1 (line 111) now carries the inference arithmetic and is dense but purposeful; the table beneath holds the data. Acceptable.

### 6. Fixed directly in cycle 2 (jargon and one precision fix; no value, quote, claim wording or indicator changed)

- business.md line 48: "leased under a September 2025 agreement" → "leased under September and October 2025 agreements" (10-Q Q2 2026 Note 4 line 751: the 54,086 sq ft came under the October 28, 2025 lease).
- outlook.md line 57 (claim 8 explanatory sentence): "as a run-rate divided by four" → "as a run-rate (a yearly pace, not a calendar-year total) divided by four".
- outlook.md line 59 (claim 10 parenthetical): "Q2's diluted count was 88.2 million" → "Q2's diluted count, which adds the shares that stock awards, the warrant and convertible notes could create, was 88.2 million".

### 7. Word counts (`python3 /tmp/aaoi_wc_prose.py`)

| File | Cycle 1 start | Cycle 1 end | Writer's pass | After cycle-2 glosses | Target |
|---|---|---|---|---|---|
| business.md | 2,877 | 2,987 | 2,839 | 2,839 | 2,000–3,000 |
| outlook.md | 1,178 | 1,183 | 1,118 | 1,139 | 800–1,200 |

### 8. Notes for the owner at indicator lock (not blocking)

1. Indicator 8 now draws its dollar figure from the 10-Q Item 2 ATM table rather than the cash-flow statement; the two differ by about $0.6M over six months (footnoted in §4). Pick one basis and the refresh will follow it.
2. Indicator 6's "prepayment" line has carried two labels in two consecutive 10-Qs; if the label changes again, the refresh should flag rather than silently subtract.

**PASS.** Ready to commit.
