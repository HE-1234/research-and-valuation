# Sandisk Corporation (SNDK) — Reviewer report, Q4 FY2026 (quarter ended July 3, 2026)

_Reviewed 2026-09-09 against `sources/FY2026-Q4/` only. As-of cutoff 2026-08-17 (FY2026 10-K filing date; call 2026-08-05; Investor Day 2026-08-13 inside the cutoff). Drafts reviewed: `business.md` and `outlook.md` (first run, review cycle 1). Line references below (`file:LNNN`) are to the cached `.txt` files; `p.N` for the earnings decks is the printed footer page (equal to the PDF page); `p.N` for the Investor Day deck is the PDF page because the deck has no printed numbers. Transcript tags have no page numbers; the transcript is a third-party (Motley Fool) machine transcript, so every number was traced to the release, slides or filings and the transcript was checked for wording only._

**Final verdict (cycle 2): PASS.** Cycle 1 returned REVISE with three factual items (§8); the writer applied all three and each was re-verified against the cached sources (see "Cycle 2" at the end). One cycle-1 finding (the $650M term-loan payment) is withdrawn with evidence: the figure is in the cached Q3 FY2026 release, which the original tag did not name. The cycle-1 findings below are kept as the record. No grading this run (first report).

---

## 1. Skeleton compliance

| Check | Result |
|---|---|
| business.md §6 headings 1–8, Glossary, Sources | All present, in order, exact titles (`business.md` lines 6, 16, 39, 80, 105, 121, 139, 159, 173, 189). |
| outlook.md §7 headings 1–5, Sources; §6 Tone shift omitted | All present in order (lines 6, 22, 30, 42, 61, 76); §6 correctly omitted on a first run. |
| Quarter label with calendar parenthetical on first use | business.md line 2 `Q4 FY2026 (quarter ended July 3, 2026)`; outlook.md title line the same. Both pass. business.md line 4 also explains the 53-week year and 14-week Q1 [10-K FY2026, Item 7; Note 1]. |
| outlook header tier line | `_Transcript source tier: third-party (The Motley Fool). Written 2026-09-09._` — exactly the required text; matches MANIFEST (call 2026-08-05, posted 2026-08-12, both before cutoff). |
| business.md §8 carries `_Proposed — owner to review and lock._` | Present (line 161). outlook.md §1 says "pending owner lock". |
| outlook §1 one row per proposed indicator | Seven indicators in business.md §8, seven rows in outlook §1, same order and same content. |
| Every tag prefix maps to a Sources row | business.md: 16 distinct prefixes (10-K FY2026, 10-K FY2025, Form 10, DEF 14A 2025, S-3ASR 2026-02-17, four 8-Ks, Q4 FY2026 release, Q3 FY2026 release, Q4 FY2025 release, Q4 FY2026 slides, 2026 Investor Day slides, 2026 Investor Day release, Q4 FY2026 call), all mapped. outlook.md: 10 prefixes, all mapped. The tag helper's three "MISSING" hits in business.md and six in outlook.md are compound tags joined with ";" (each component is mapped) plus false hits on bracketed insertions inside quotes ("maintain[s]"; after the reviewer's edits also "[average selling price]" and "[the term loan]"). |
| Sources tables state transcript tags have no page numbers; Investor Day `p.N` are PDF pages | Both files: yes, in bold, in the transcript row and the Investor Day slides row. Both also record that the Q3 transcript is used only for "what management had said to expect". |
| Five-year tables state the basis per column | §2, §3 (both tables) and §4 tables each carry a "Basis" row: carve-out / carve-out / carve-out / carve-out to Feb 21, 2025 then standalone / standalone. The "Reading the five-year tables" paragraph explains carve-out and the FY2022 balance-sheet gap. |

## 2. Rubric (§14)

| # | Question | Answer | Reasoning |
|---|---|---|---|
| 1 | Explain what the company does and who pays, in two sentences? | Yes | §1 paragraph 1 does it (NAND chips and drives; data centers, PC/phone/car makers, consumers), §2 sizes the three markets. |
| 2 | Know what would kill it and the early warning? | Yes | §6 ranks seven scenarios, each with a trigger and a watchable sign (price direction in the release, inventory days past 178, idle-capacity charges in Note 10, YMTC in MD&A, JV disputes, BiCS 10 dates, a 10% customer). |
| 3 | Know why margins are what they are and whether cost scales with usage? | Yes | §3 states the mechanism (price per bit floats, cost per bit barely moves, half of JV fixed costs owed regardless), shows FY2023 against FY2026 with computed cost-of-revenue changes, and explains why capex is tiny (fabs sit in Flash Ventures, "gross capex" on the slides). |
| 4 | Predict what the scorecard will check next quarter from outlook §5 alone? | Yes | Ten numbered claims, each with a threshold, a period and a verbatim quote; sharpenings and disclosure checks labelled with basis. |
| 5 | Nothing required knowledge I don't have? | Yes, after reviewer glosses | A handful of terms leaned on unexplained finance and chip vocabulary (goodwill, revolver, TLB, EPS, PP&E, DRAM, QLC, ASP, sale-leaseback, tape-out, "on allocation", "sequential", shareholders' equity, depreciation, Sections 232/301). All glossed directly; list in §4 below. |

## 3. Citation spot-check

Method: every cell of business.md §2, §3 (both tables) and §4 tables, every cell of outlook.md §1 and §4 tables, every quote under outlook §5, and roughly 120 further source-tagged sentences across both files were grepped in the cited cached `.txt` (full lines printed, `grep -F`, stems for curly-quote text). Every "(computed)" figure was re-derived. "n/d" and "n/a" cells were checked for actual silence in the alternate-basis filing used for that column.

**Totals: about 400 items checked; 3 FAIL (all for the writer, §8 items 1–3); 1 PASS after a reviewer tag-and-rounding fix (allocated costs, §9); everything else PASS.**

### A. business.md §2 — revenue by end market (25 items)

| Item | Tag | Found at | Result |
|---|---|---|---|
| FY2022 1,264 / 6,038 / 2,452 / 9,754; FY2023 500 / 3,637 / 1,949 / 6,086; FY2024 325 / 4,069 / 2,269 / 6,663 | Form 10, MD&A | Form10:3970–3973 (also 7892–7895) | PASS (12) |
| FY2025 960 / 4,127 / 2,268 / 7,355 | 10-K FY2025, Item 7 | 10-K-FY2025:1228–1231 ("Cloud", "Client") | PASS (4) |
| FY2026 5,153 / 12,160 / 2,935 / 20,248 | 10-K FY2026, Item 7 | 10-K-FY2026:1185–1188 ("Datacenter", "Edge") | PASS (4) |
| FY2024 identical in all three filings ("our check") | — | 325 / 4,069 / 2,269 in Form10:3970, 10-K-FY2025:1228, 10-K-FY2026:1185 | PASS |
| Datacenter share (computed) 13 / 8 / 5 / 13 / 25% | computed | 12.96 / 8.2 / 4.9 / 13.1 / 25.4% | PASS (5) |
| "formerly referred to as 'Cloud'" / "'Client'" | 10-K FY2026, Item 1 | 10-K-FY2026:137 | PASS |
| Datacenter 437%, "almost 120%" bits, "almost 150%" price; Edge "high single-digits", "almost 180%"; Consumer "mid-teens" down, "low-fifties" | 10-K FY2026, Item 7 | 10-K-FY2026:1205, 1207, 1209 | PASS (7) |
| 12% of bits Q4 FY2025 to 38% Q4 FY2026 | Q4 FY2026 slides, p.8 | slides.txt p.8 | PASS |
| "351K Points of Sale" | 2026 Investor Day slides, p.10 | investor-day p.10 | PASS |
| Price protection 11% / 19% / 21% | 10-K FY2026 Item 7; 10-K FY2025 Item 7 | 10-K-FY2026:1213 (11, 19, 19); 10-K-FY2025:1256 (19, 19, 21) | PASS (3) |
| China + Hong Kong 48% (computed) | 10-K FY2026, Note 3 | 10-K-FY2026:2077–2078: 4,503 + 5,126 = 9,629 / 20,248 = 47.6% | PASS |

### B. business.md §3 — economics table (57 items)

| Item | Tag | Found at | Result |
|---|---|---|---|
| Revenue row (as A) | — | as above | PASS (5) |
| Price per GB: FY2022 n/a; (39)%; (8)%; +4%; FY2026 Datacenter ~150 / Edge ~180 / Consumer low-50s | Form 10 MD&A; 10-K FY2025 Item 7; 10-K FY2026 Item 7 | Form 10 MD&A compares only 2024 vs 2023 and 2023 vs 2022 (no FY2022 vs FY2021) — n/a honest; Form10:4002 (39%); Form10:3988 (8%); 10-K-FY2025:1246 (4%); 10-K-FY2026:1205/1207/1209 | PASS (7) |
| Bits: n/a; roughly flat (labelled inference from "substantially all driven by" price, Form10:4002); +21%; +6%; +mid-teens | as above | Form10:3988 (21%); 10-K-FY2025:1246 (6%); 10-K-FY2026:1203 (mid-teens) | PASS (5) |
| Gross margin 33.3 / 7.1 / 16.1 / 30.1 / 71.5% | Item 7 tables | Form10:3945; 10-K-FY2025:1202; 10-K-FY2026:1157 | PASS (5) |
| Operating margin 12.3 / (33.4) / (7.0) / (18.7) / 61.3% | Item 7 tables | Form10:3954; 10-K-FY2025:1211; 10-K-FY2026:1166 | PASS (5) |
| R&D 1,362 / 1,167 / 1,061 / 1,132 / 1,328 | Item 8 | Form10:7348; 10-K-FY2025:1614; 10-K-FY2026:1590 | PASS (5) |
| SG&A 666 / 558 / 455 / 573 / 676 | Item 8 | Form10:7349; 10-K-FY2025:1615; 10-K-FY2026:1591 | PASS (5) |
| Goodwill impairment — / 671 / — / 1,830 / — | Item 8 | Form10:7352; 10-K-FY2025:1617; 10-K-FY2026:1593 | PASS (5) |
| Idle-capacity charges at Flash Ventures n/d / 286 / 249 / 75 / 11 | Form 10 FV note; 10-K Note 10 | Form10:8403 ("$249 million and $286 million" for 2024 and 2023; nothing for 2022); 10-K-FY2026:2544 ("$11 million, $75 million, and $249 million"). Series is consistent (Flash Ventures-related charges from the related-party notes). The MD&A's company-wide totals are different numbers: $296M FY2023 and $252M FY2024 (Form10:4032, 4040; 10-K-FY2026:549), $75M FY2025 (10-K-FY2025:1172, same as the note). Reviewer added a footnote sentence saying so (§9). FY2022: Form 10 FV note names only the $207M contamination charge (Form10:8408) — n/d honest. | PASS (5) |
| Capex 410 / 219 / 166 / 204 / 177 | Item 8 | Form10:7426 (gross line); 10-K-FY2025:1696; 10-K-FY2026:1683 | PASS (5) |
| Capex / revenue 4.2 / 3.6 / 2.5 / 2.8 / 0.9% (computed) | computed | 4.20 / 3.60 / 2.49 / 2.77 / 0.87% | PASS (5) |
| $207M contamination FY2022 | Form 10, Flash Ventures note | Form10:8408; also 4041 | PASS |
| Ex-impairment operating margins (22)% and (6)% (computed) | computed | FY2023: (−2,035 + 671) / 6,086 = −22.4% PASS. **FY2025: (−1,377 + 1,830) / 7,355 = +6.2%, i.e. a profit, not (6)%.** | **1 PASS, 1 FAIL → §8 item 1** |
| FY2023 revenue −38%, cost of revenue −13% (computed), "all but about 4 points" | Form 10, MD&A | Form10:4002; 6,510 → 5,656 = −13.1%; Form10:4042 ("approximately 4% of the decline due to the net charges") | PASS (3) |
| FY2026 revenue +175%, cost of revenue +12% (computed), 71.5% / 84.6% | 10-K FY2026 Item 7; release | 10-K-FY2026:1203; 5,143 → 5,776 = +12.3%; press-release:33, 55 | PASS (4) |
| Net payments $3.6B vs $5.8B cost of revenue; "cost plus a small markup" | Note 10; Item 8; Item 1 | 10-K-FY2026:2518; 1588 (5,776); 229 | PASS (3) |
| R&D + SG&A 10% of FY2026, 28% of FY2023 (computed) | Item 7 | 2,004 / 20,248 = 9.9%; 1,725 / 6,086 = 28.3% | PASS (2) |
| Non-GAAP vs GAAP gross margin 0.1 point apart in FY2026 | Q4 FY2026 release | press-release:55 (71.5% vs 71.6%) | PASS |
| "at cost"; "in excess of Flash Ventures' operating cash flow"; "pay for half of Flash Ventures' fixed costs regardless of the output we choose to purchase"; "approximately 100%" | Item 1; Note 10; slides p.18 | 10-K-FY2026:229 (at cost; half of fixed costs, verbatim with "we"); slides p.18 ("in excess of Flash Ventures' operating cash flow", verbatim; 10-K Item 1 L233 has the same idea in other words); 10-K-FY2026:2544 | PASS (4) |
| Gross capex $562M, 6.3%; cash capex $153M | Q4 FY2026 slides, p.14 | slides p.14 | PASS (3) |
| "54% BiCS Gen-to-Gen" | 2026 Investor Day slides, p.14 | investor-day p.14 ("54% BiCS Gen-to-Gen Average Bit Growth Per Wafer") | PASS |
| Allocated costs "about three-quarters of R&D plus SG&A in FY2023 and FY2024 (computed)" [10-K FY2026, Note 10] | — | FY2024: (723 + 418) / (1,061 + 455) = 75.3% (10-K-FY2026:2675–2676). FY2023: (750 + 452) / (1,167 + 558) = 69.7% — and the FY2023 column is not in the FY2026 10-K at all; it is in 10-K-FY2025:2643–2644 and Form10:8555–8556. | PASS after reviewer fix: now "about 70% in FY2023 and 75% in FY2024" with tag [10-K FY2025, Note 10; 10-K FY2026, Note 10] (§9) |

### C. business.md §3 — Flash Ventures table (40 cells) and footnote

| Item | Tag | Found at | Result |
|---|---|---|---|
| Net payments 4,700 / 4,200 / 3,400 / 3,400 / 3,600 | Form 10 FV note; 10-K Note 10 | Form10:8361–8362 ("$3.35 billion, $4.20 billion, $4.70 billion"); 10-K-FY2025:2498 ($3.4B, $3.4B, $4.2B); 10-K-FY2026:2518 ($3.6B, $3.4B, $3.4B). The FY2024 3,350-vs-3,400 discrepancy the writer flagged is real and is footnoted in the draft exactly as the sources read. | PASS (5) |
| Loans issued (809) / (627) / (243) / (333) / (462) | cash flow statements | Form10:7429; 10-K-FY2025:1699; 10-K-FY2026:1686 | PASS (5) |
| Loans repaid 718 / 641 / 482 / 515 / 187 | cash flow statements | Form10:7430; 10-K-FY2025:1700; 10-K-FY2026:1687 | PASS (5) |
| Distributions — / — / — / 176 / 107 | Note 10 | 10-K-FY2025:2498 ("$176 million, $0 and $0"); 10-K-FY2026:2518 ($107M, classified in operating activities) | PASS (5) |
| Notes receivable and equity n/d / 1,411 / 1,001 / 654 / 679 | balance sheets; Note 10 | Form 10 has no FY2022 balance sheet (Form10:7204) — n/d honest; Form10:7305 (1,001; 1,411); 10-K-FY2025:1569 (654); 10-K-FY2026 Note 10 table total $679 (line 2511). The FY2026 balance sheet line prints 678 (10-K-FY2026:1540), a $1M rounding inside the filing; the draft cites Note 10, so 679 stands. | PASS (5) |
| Lease guarantees n/d / n/d / 1,299 / 1,404 / 923 | FV notes | Form 10 guarantee table gives June 28, 2024 only (Form10:8436–8441) — FY2022/FY2023 n/d honest; Form10:8388; 10-K-FY2025:2510; 10-K-FY2026:2530, 2556 | PASS (5) |
| Prepayments n/d / n/d / 523 / 946 / 840 | FV notes | Form10:8333 (June 28, 2024 balance only); 10-K-FY2025:2472; 10-K-FY2026:2486 | PASS (5) |
| Maximum loss exposure n/d / n/d / 3,369 / 3,384 / 2,897 | FV notes | Form10:8390 (June 28, 2024 only); 10-K-FY2025:2512; 10-K-FY2026:2532 | PASS (5) |
| $6,559M commitments, $2,627M due FY2027; $1.2B to Kioxia "over the years 2026 through 2029"; extension to December 31, 2034; three-month binding orders | Item 7; Note 10 | 10-K-FY2026:1350; 241; 2488–2490; 2546 | PASS (5) |

### D. business.md §4 — cash table (60 cells) and prose

| Item | Tag | Found at | Result |
|---|---|---|---|
| Net income 1,064 / (2,143) / (672) / (1,641) / 11,433 | Item 8 | Form10:7363; 10-K-FY2025:1631; 10-K-FY2026:1606 | PASS (5) |
| Operating cash flow 1,151 / (713) / (309) / 84 / 11,671 | Item 8 | Form10:7424; 10-K-FY2025:1694; 10-K-FY2026:1680 | PASS (5) |
| Capex row (as B) | — | as above | PASS (5) |
| Free cash flow 741 / (932) / (475) / (120) / 11,494 (computed) | computed | re-derived; FY2025 and FY2026 also printed in press-release:351 | PASS (5) |
| Activity related to Flash Ventures, net (91) / 14 / 239 / 358 / (275) | Form 10 MD&A; releases | Form10:4378; press-release-FY2025-Q4:364 (358); press-release:352 ((275)) | PASS (5) |
| NBM prepayments and deposits — ×4 / (2,476) | Q4 FY2026 release | press-release:353 | PASS (5) |
| Adjusted free cash flow 650 / (918) / (99) / 238 / 8,743 | Form 10 MD&A; releases | Form10:4379; press-release-FY2025-Q4:365 and press-release:354 (238); press-release:354 (8,743) | PASS (5) |
| Stock-based compensation 171 / 165 / 149 / 182 / 232 | Item 8 | Form10:7405; 10-K-FY2025:1673; 10-K-FY2026:1657 | PASS (5) |
| Buybacks — ×4 / 4,524 | Item 8 | 10-K-FY2026:1694 | PASS (5) |
| Net transfers from (to) WDC (933) / 676 / 394 / (1,887) / — | cash flow statements | Form10:8594; 10-K-FY2025:2680; 10-K-FY2026:2706 | PASS (5) |
| Cash 335 / 292 / 328 / 1,481 / 4,762 | Item 8 | Form10:7443; 10-K-FY2025:1719; 10-K-FY2026:1707 | PASS (5) |
| Form 10 FY2024 FCF $(338)M "because it nets $137M of sale-leaseback proceeds against capex" | Form 10, MD&A | Form10:897 ((338)); Form10:896 net purchases (29) vs Form10:7426 gross (166): difference 137 PASS. **But the Form 10 attributes $134M, not $137M, to the Milpitas sale-and-leaseback (Form10:3726, 10019); the other $3M is other property proceeds.** | **FAIL (wording) → §8 item 2** |
| FY2022–FY2025 OCF total $213M; loss $3.4B; goodwill $2.5B (computed) | Item 8 | 1,151 − 713 − 309 + 84 = 213; 1,064 − 2,143 − 672 − 1,641 = −3,392; 671 + 1,830 = 2,501 | PASS (3) |
| Adjusted FCF definition; Q3 $2,955M restated to $2,417M | releases | press-release:384 (definition, "not indicative of the core underlying cash flows"); press-release-FY2026-Q3:325 (2,955); press-release:354 (2,417) | PASS (3) |
| Contract liabilities $1,242M; refund liabilities $1,500M "must be refunded at the end of the contract term"; $2.7B | Note 4; Item 8 | 10-K-FY2026:2128, 2130, 1552 | PASS (3) |
| Cash taxes $146M; expense $1,584M; payable $1,286M; receivables +$3.6B | Note 14; Item 8 | 10-K-FY2026:1711; 1605; 1554; 1670 ((3,640)) | PASS (4) |
| Opening equity $9.2B; FY2025 lost 15% of opening equity (computed) | Item 8 | 10-K-FY2026:1596 (9,216; 11,082); 1,641 / 11,082 = 14.8% | PASS (2) |

### E. business.md §1, §5, §6, §7 — prose (about 95 items)

| Item | Tag | Found at | Result |
|---|---|---|---|
| "All of our flash-based memory is obtained from our joint ventures with Kioxia"; "largely interchangeable with competitors' products"; 49.9%; Penang; may not make flash elsewhere | Item 1; 1A; 2; Note 10 | 10-K-FY2026:225; 617; 2460; 972; 231 | PASS (5) |
| JVs 2004 / 2006 / 2010, originally Toshiba | Note 10; Item 15 | 10-K-FY2026:2462, 2464, 2466; exhibits 3328–3346 | PASS (4) |
| Two officers at "the prior SanDisk Corporation" until 2016 | DEF 14A, Executive Officers | DEF14A:921 (Ilkbahar 2006–2016), 923 (Shek 2011–2016) | PASS |
| "operating segment of WDC" since 2016 | Form 10, Note 1 | Form10:7515 says so for the periods covered (FY2022–FY2024); the 2016 start is bridged from the bios. Reviewer labelled the inference (§9). | PASS after label |
| October 30, 2023; February 21, 2025; 19.9% | Item 7; 8-K 2025-02-03 | 10-K-FY2026:1092, 1094 | PASS (3) |
| Carve-out basis; FY2022 has no balance sheet | Form 10 Note 1; Combined Balance Sheets | Form10:7515; 7204 | PASS (2) |
| "we do not generally require firm order commitments"; no >10% customer FY2024–FY2026 | Item 1A; Item 1 | 10-K-FY2026:617; 265, 2110 | PASS (2) |
| "Demand from our customers is growing faster than our supply, and we expect bits to remain on allocation beyond calendar 2027" | Q4 FY2026 slides, p.12 | slides p.12, verbatim | PASS |
| "We must also qualify our products with customers through potentially lengthy testing processes with uncertain results" | Item 1A | 10-K-FY2026:579 | PASS |
| "industry leading consumer brand awareness and global retail distribution presence"; NBMs "are not related to the consumer business" | Item 1; call Q&A BNP Paribas | 10-K-FY2026:197; transcript:131 (Karl Ackerman, BNP Paribas, section opens transcript:118) | PASS (2) |
| NBM: "fixed and variable components"; "subject to floors and ceilings"; eight customers; $93.9B "at floor pricing"; RPO $59.8B / $91.1B; over half FY2027 bits, about two-thirds FY2028 | Item 7; Note 4; Note 17; slides p.11; call CFO | 10-K-FY2026:1130 (fixed and variable); slides p.11 and transcript:34 (floors and ceilings; $93.9B); 10-K-FY2026:2144 ($59.8B); slides p.11 ($91.1B; 8 customers; 1/2 and ~2/3); 10-K-FY2026 Note 17 line 3223 ($31.3B for the two later deals; 59.8 + 31.3 = 91.1 reproduces) | PASS (7) |
| "$16.5 billion"; $5.0B collateral; "does not reconcile" | slides p.11; Note 4 | slides p.11 and transcript:35 ($16.5B); 10-K-FY2026:2142 ($5.0B); the 10-K nowhere mentions $16.5B (grep). Reviewer relabelled as the writer's observation with the likely timing reason (§9). | PASS after label |
| "may not fully offset such lost revenue"; "Largest Producer of NAND Wafers in the World (33%)"; ~8,000 patents | Item 1A; Investor Day p.7; Item 1 | 10-K-FY2026:667; investor-day p.7; 10-K-FY2026:141, 207 | PASS (3) |
| FY2023: 39% price fall, 7% margin, $2.1B loss | Form 10 MD&A | Form10:4002; 3945; 7363 | PASS (3) |
| "attractive margins even at floor pricing"; uncontracted bits "will fluctuate with the market" | call CFO | transcript:34 | PASS (2) |
| YMTC named with Kioxia, Micron, Samsung, SK hynix; "aggressive expansion of their output capacities" | Item 1; 1A | 10-K-FY2026:171 (written "Yangtze Memory Technologies Co., Ltd."; reviewer glossed the abbreviation); 579 | PASS (2) |
| "cannot unilaterally direct most of Flash Ventures' activities"; "Kioxia's management changes, ownership and capital structure could lead to delays in decision-making, disputes or changes in strategic direction" | Item 1A | 10-K-FY2026:551 (both, verbatim) | PASS (2) |
| "advances in NAND technology, including higher-capacity and higher-layer architectures ... may increase the complexity"; BiCS 8 majority of bits; "Sampling in August 2026" | Item 1A; slides p.5; Investor Day p.27 | 10-K-FY2026:585; slides p.5; investor-day p.27 | PASS (3) |
| Eight fabs, Yokkaichi and Kitakami; "limited insurance coverage and, in some cases, no coverage at all, for natural disasters" | Item 1/2; Item 1A | 10-K-FY2026:227, 985; 495 | PASS (2) |
| Top ten 44%; three customers 19% + 12% + 10% = 41% of receivables (computed); "Fewer companies now hold greater market share ... increased leverage in negotiating prices" | Item 1; Note 3; Item 1A | 10-K-FY2026:653, 2110; 2112; 657 | PASS (3) |
| Sections 232 / 301 "may impact tariff rates for Sandisk products"; "the majority of our products sold in the U.S. are currently exempt"; DRAM "which has experienced supply constraints" | Item 1A | 10-K-FY2026:473; 479 | PASS (3) |
| Nanya: ~139M shares, 3.9%, $970M, 15% discount, three-year lock-up, April 2026, DRAM supply arrangement; worth $1,777M; $807M gain; "$1.0B" in 8-K | 8-K 2026-03-25; Note 6; Note 11 | 8-K-2026-03-25:63, 69 ($1.0 billion; 139M; 3.9%; 15%); 10-K-FY2026:2784 ($970M; "statutory lock-up period of three years"; remitted April 8, 2026); 1538 (1,777); 2347 (807) | PASS (9) |
| Goeckeler 63, WDC CEO March 2020, Cisco; Visoso 56, WDC July 2024, Unity / Palo Alto Networks / AWS; Ilkbahar 58, Intel | DEF 14A | DEF14A:916, 316; 918, 919; 920, 921 | PASS (9) |
| Board eight: two WDC transition directors not renominated (Nov 2025), Bradley Dec 2025; TSMC Arizona, GlobalFoundries, AMD | DEF 14A; 8-Ks | DEF14A:58 (Massengill and Alexy "will not be nominated"); 8-K-2025-11-20 (seven elected); 8-K-2026-01-02:52 (Bradley, December 30, 2025); DEF14A:203, 298, 306, 325 | PASS (5) |
| Insiders 341,824 at Feb 6, 2026; FMR 13.9%; Vanguard 11.2%; BlackRock 6.0% | S-3ASR | S-3ASR:1038, 993; 1026; 1027; 1028 | PASS (5) |
| WDC 14.6% exchanged June 2025; 5.8M shares February 2026; "expects to monetize all remaining shares of Sandisk common stock held by it by the end of 2026" | Item 7; S-3ASR | 10-K-FY2026:1100 (all three; the sentence sits at the end of a long line and was only found on printing the full line) | PASS (3) |
| Bonus 50% profit / 25% adjusted FCF / 25% "Corporate Strategy: Equally weighted across Net Debt, Consumer Net Revenue, and Data Center Market Share"; three-year PSUs on revenue and EPS | DEF 14A, CD&A | DEF14A:1390–1394; 1398 ("Revenue and Earnings Per Share metrics, each weighted at 50%"; three consecutive one-year periods) | PASS (4) |
| Launch grants $47.07 base, 100% at $70.61, 300% at $105.91, to February 2028; $626.56 on Feb 13, 2026; CEO $22.9M, $18.8M stock; "appreciated materially", vest 2028 | DEF 14A; S-3ASR; Item 1A | DEF14A:1335, 1349, 1352, 1339 (Feb 24, 2028); S-3ASR:111; DEF14A:1480 (22,919,536; 18,845,786); 10-K-FY2026:503 | PASS (8) |
| $1.5B net distribution to WDC; $2.0B seven-year term loan; $100M repaid FY2025; final settlement March 4, 2026; $46M write-off; debt zero; $1.5B revolver undrawn | Item 7; Note 8 | 10-K-FY2026:1114, 1112; 10-K-FY2025:2372 ($100M); 10-K-FY2026:2412 (March 4, 2026, $46M); 1359 (revolver undrawn); 10-Q:178 (debt —) | PASS (7) |
| **"the final $650M"** | Note 8 | **Not in any cached source.** 10-K-FY2026:1116, 2412 and 10-Q-FY2026-Q3:837, 1423 say "settled in full the remaining outstanding principal amounts" with no dollar figure; FY2026 repayments total $1,900M (10-K-FY2026:1696; 10-Q:316, 1677); balance at June 27, 2025 was about $1.9B (10-K-FY2025:1488). No "650" anywhere in the 10-K or 10-Q. | **FAIL → §8 item 3** |
| Buybacks $6.0B April 30, 2026; $14.0B August 5, 2026; $15.5B remaining; 2,836,275 shares at $1,600.00; $4.5B | Item 5; Item 7; release | 10-K-FY2026:1031, 1399; press-release:18; 10-K-FY2026:1027; 1330 | PASS (6) |
| Dividend quote; $2,879M outside the U.S.; 146,419,001 shares at August 7, 2026 | Item 5; Item 7; cover | 10-K-FY2026:1017; 1302; 66 | PASS (3) |
| Priorities quote ("first continue to invest ... Priority #2 ... TLB ... share buybacks"); "very consistent in our execution"; "more tax efficient" | call Q&A Goldman Sachs; Melius | transcript:90–91 (Goldman section opens 77); 55 (Melius section opens 50); 92 (Goldman) | PASS (3) |
| 2H FY2025 bonus cut to 90% "with the fact that our company did not generate a profit" | DEF 14A, CD&A | DEF14A:1243 | PASS |
| "Excess cash" undefined; "100 percent of excess cash" | 2026 Investor Day release | press-release-investor-day:13, 34; the release does not define it (grep) | PASS |

### F. outlook.md §1 — indicator table (54 items) and line 20

| Item | Tag | Found at | Result |
|---|---|---|---|
| Row 1 Q4: $2,977M / $5,432M / $556M; 33% (computed); "approximately one-third from higher volumes and two-thirds from higher pricing" | Q4 FY2026 release | press-release:66–68; 2,977 / 8,965 = 33.2%; press-release:12 | PASS (5) |
| Row 1 Q3: $1,467M / $3,663M / $820M; 25% (computed); no split given; bits "flat year-over-year and down high-teens sequentially" | Q3 release; Q3 call CFO | press-release-FY2026-Q3:54–56; 1,467 / 5,950 = 24.7%; no volume/price sentence in the Q3 release (grep); transcript-FY2026-Q3:29. The year-over-year half is also in 10-Q-FY2026-Q3:1533 ("exabytes sold remained flat"); reviewer added that tag (§9). "Down high-teens sequentially" exists only in the machine transcript; kept as quoted wording. | PASS (5) |
| Row 1 expect: "$7,750 - $8,250"; "from both bits growth and higher pricing" | Q3 release; Q3 call | press-release-FY2026-Q3 Business Outlook table; transcript-FY2026-Q3:33 | PASS (2) |
| Row 2: 84.6%; 78.4%; "79.0% - 81.0%" | releases | press-release:33; press-release-FY2026-Q3:34; Q3 outlook table | PASS (3) |
| Row 3: $2,698M, 178 days; $2,238M, 158 days; "we build higher inventory levels" | release; 10-K Item 7; 10-Q Item 2; Q3 call | press-release:136; 10-K-FY2026:1312; press-release-FY2026-Q3:116; 10-Q:1659; transcript-FY2026-Q3:29 | PASS (5) |
| Row 4: RPO $59.8B ($91.1B); contract liabilities $1,242M; refund liabilities $1,500M; Q3 RPO $41.6B; $511M; refund liabilities not broken out | Note 4; Note 17; release; 10-Q Note 4 | 10-K-FY2026:2144; slides p.11 / transcript:35 ($91.1B); 2128; 2130; 10-Q:585; 10-Q:1743 ($511M); no "Refund liabilities" line in the 10-Q (grep, the only "refund" hit is a tariff sentence at 10-Q:1431) — n/d honest | PASS (7) |
| Row 4 expect: "we expect to increase as we conclude additional agreements over the next few months" | Q3 call CFO | transcript-FY2026-Q3:28 | PASS |
| Row 5: $577M; $923M; $2,897M; $(110)M; Q3 $483M; $993M; $2,967M; $(38)M | Note 10; releases; 10-Q Note 10 | 10-K-FY2026:2528–2532; press-release:352 (Q4 column (110), Q3 column (38)); 10-Q:922–926 | PASS (8) |
| Row 6: $562M (6.3%); $153M (1.7%); $43M; Q3 $240M (4.0%); $83M (1.4%); $45M; Citi quotes | slides p.14; Q3 slides p.8; Q3 call Q&A Citigroup | slides p.14; slides-FY2026-Q3 p.8; transcript-FY2026-Q3:128 (Asiya Merchant, Citigroup, section opens 121) | PASS (10) |
| Row 7: $4,762M; no debt; $4,524M for 2,836,275 shares; Q3 $3,735M; no repurchases; "$6.0B ... effective immediately with no expiration date" | release; Item 5; Q3 release; Q3 call | press-release:134; 10-K-FY2026:1027; press-release-FY2026-Q3:114; no repurchase line in the Q3 release (grep); transcript-FY2026-Q3:35 | PASS (7) |
| Line 20: $8,965M vs $7,750–8,250M; 84.6% vs 79–81%; $39.25 vs $30.00–33.00 | releases | press-release:32, 33, 37; Q3 outlook table | PASS (3) |

### G. outlook.md §2, §3, §4 — quotes and guidance (about 35 items)

| Item | Tag | Found at | Result |
|---|---|---|---|
| "Underlying our performance is the most important force in our market, the Era of Inference. AI is fundamentally a memory-centric storage-intensive problem. And it is reshaping the demand equation for NAND" | call CEO | transcript:23, verbatim | PASS |
| "we grow supply primarily through nodal transitions rather than wafer additions ... This is a structural advantage and what makes this franchise such a powerful cash generator" | call CEO | transcript:29 (ellipsis honest) | PASS |
| "We want to get this kind of boom and bust out of it. It doesn't work for anybody"; "I think mid-80s gross margin, I would characterize as a fair return"; "about 80% gross margin. And then the rest of the portfolio floats" | call Q&A Cantor | transcript:98, 99 (C.J. Muse, Cantor, section opens 94) | PASS (3) |
| Investor Day FY2028–FY2030 framework quote; "at approximately 50 percent"; "we expect to return 100 percent of excess cash to our shareholders after investing in the business"; "more tax efficient" | Investor Day release; call Q&A Goldman | press-release-investor-day:32 (verbatim), 34; transcript:92 | PASS (4) |
| Datacenter $2,977M, a third of revenue, 38% of bits from 12%; "This quarter we began shipping our QLC Stargate platform for revenue" | release; slides p.8; slides p.5 | press-release:66; slides p.8; slides p.5 | PASS (4) |
| Eight customers; $59.8B / $91.1B; "more than 50% of our bits in fiscal year 2027, and approximately 2/3 of our bits in fiscal year 2028"; "still in deep conversations with additional customers"; "highly selective" | slides p.11; call CFO; Q&A Goldman | slides p.11; transcript:34; 86; 36 | PASS (5) |
| BiCS 10 "Sampling in August 2026"; "as we ramp BiCS 8 and BiCS 10"; "the higher inventory levels reduce sellable bits to mid-teens for the full year fiscal year 2027" | Investor Day p.27; call CFO | investor-day p.27; transcript:43, 44 | PASS (3) |
| "working through a period of adjustment"; "We expect these markets to return to growth in calendar year '27" | call CEO | transcript:27 | PASS (2) |
| "FIRST HBF MEMORY DIE TAPED OUT"; "FIRST HBF INFERENCE PRODUCT SAMPLES"; 2027 | Investor Day p.96 | investor-day p.96 | PASS (3) |
| §4 Q1 FY2027 table: revenue $10,300 - $10,800; gross margin 83.0% - 84.9% / 83.0% - 85.0%; opex $574 - $614 / $520 - $540; tax N/A / 15.0%; EPS N/A / $44.00 - $46.00; shares ~155 / ~155 | Q4 FY2026 release | press-release:83–91 "Business Outlook for Fiscal First Quarter of 2027", cell for cell | PASS (12) |
| CFO revenue sentence; two April items absent ($10–30M interest; $775–875M tax) | call CFO; Q3 release | transcript:42; Q3 outlook table (rows present in April, absent in August) | PASS (3) |
| FY2027 capex and inventory quotes; "$14 billion ... $15.5 billion"; "very consistent" | call CFO; Q&A Melius | transcript:43, 44 (verbatim, including "to support our NBMs and account for higher component costs"); 44; 55 | PASS (4) |

### H. outlook.md §5 — the ten claim quotes (10 items)

All ten quotes verbatim: 1 press-release:20; 2 press-release:86; 3 transcript:42; 4 slides p.8; 5 transcript:35; 6 transcript:86; 7 transcript:36; 8 transcript:43; 9 transcript:43; 10 transcript:55. Claim 7's $2,742M reproduces (1,242 + 1,500). PASS (10).

### Withdrawals (suspected failures dropped after printing the full line)

| Suspicion | Why withdrawn |
|---|---|
| FY2026 "notes receivable and equity" 679 vs balance sheet 678 | Note 10 table (10-K-FY2026:2511) totals $679; the balance sheet (1540) rounds to 678; the draft cites Note 10. |
| "in excess of Flash Ventures' operating cash flow" not in the 10-K | Verbatim on slides p.18, which the tag names; 10-K Item 1 L233 says the same in other words. |
| "floors and ceilings", "$91.1B", "$93.9B", "eight customers" not in the 10-K | All on slides p.11 (and transcript:34–35), which the tags name; 10-K Note 17's $31.3B for the two later deals reproduces $91.1B. |
| "expects to monetize" not found | Sits at the end of the 500-character 10-K-FY2026:1100; found on printing the full line. |
| "YMTC" not in the 10-K | The 10-K writes "Yangtze Memory Technologies Co., Ltd." (10-K-FY2026:171); reviewer glossed the abbreviation. |
| "three-year lock-up" not in the Nanya 8-K | In 10-K Note 11 (10-K-FY2026:2784, "statutory lock-up period of three years"), which the tag names. |
| "aggressive expansion of their output capacities" not visible | Hidden by a 500-character cut of 10-K-FY2026:579; verbatim on the full line. |
| "the prior SanDisk Corporation", two officers | Hidden by cuts of DEF14A:921 and 923; both bios say it on the full lines. |

## 4. Jargon audit

Terms found that were neither plain, name-inferable nor in the Glossary, and what was done (all direct reviewer edits; see §9 for wording):

| Term | Where | Fix |
|---|---|---|
| goodwill / goodwill impairment | §3 table row, §4 prose | Glossary entry added |
| revolver | §7 table | "revolving credit line" |
| TLB (inside a quote) | §7 prose | bracketed "[the term loan]" |
| EPS | §7 prose; outlook line 20 and §4 | spelled out once in each file |
| PP&E | §3/§4 table rows, §8, outlook §1 | added to the Glossary's Capex entry |
| DRAM | §6 item 7, §7 table | inline gloss at first use |
| QLC | outlook §1, §3 | inline gloss at first prose use |
| ASP (inside a quote) | §3 | bracketed "[average selling price]" |
| sale-leaseback | §4 footnote | gloss included in the §8 item 2 wording for the writer |
| "TAPED OUT" (inside a quote) | outlook §3 | inline gloss |
| "on allocation" (inside a quote) | §5 | inline gloss "(rationed among customers)" |
| sequential | outlook §1, §4, §5 | one-line gloss in the outlook preamble |
| shareholders' equity | §4 | inline gloss |
| depreciation | §3 | inline gloss at first use |
| Sections 232 and 301 | §6 item 7 | "US tariff investigations under Sections 232 and 301 of trade law" |
| price protection (quoted) | §2 | inline gloss |
| AI inference | outlook §2 | inline gloss |
| 8-K | Sources only | added to the Glossary's 10-K / 10-Q entry |

Glossary check: 13 entries, all unavoidable (NAND, bit, wafer, fab, node/BiCS, SSD, NBM, RPO, gross/operating margin, capex, GAAP/non-GAAP, carve-out, 10-K/10-Q), one sentence each. Reviewer added one entry (goodwill impairment) and extended two. Terms explained inline and correctly kept out of the Glossary: OEM, qualification, contract and refund liabilities, price protection, controller, Stargate, HBF.

## 5. Invented-number check

- **$650M** final term-loan payment (business.md §7 table): no cached source carries this figure; see §3E and §8 item 3.
- Every other figure carries a tag that supports it (§3 above). Computed figures are labelled "(computed)" or "our check" and reproduce, except the FY2025 ex-impairment margin sign (§8 item 1) and the $137M/$134M attribution (§8 item 2).
- Inferences: "Our inference" (§3, chips/fabs/people vs price), "roughly flat" bits FY2023 (footnoted as derived from "substantially all driven by" price), "Our read" (outlook §2) are labelled. Two more were labelled by the reviewer: the 2016 "operating segment" bridge (§1) and the $16.5B-vs-$7.7B non-reconciliation (§5).
- Transcript numbers: the drafts take every number from the release, slides or filings and quote the transcript for wording; the known garble (86.5% gross margin, transcript:160) does not appear in either draft. The one soft figure that exists only in a transcript, Q3 bits "down high-teens sequentially", is presented as a quote and now also carries the 10-Q tag for its year-over-year half.

## 6. Claims check (outlook §5)

Ten claims (target 6–12). Each is one sentence, one thing, single direction, able to fail; no either/or; verbatim quote with tag under each.

| # | Type | Check |
|---|---|---|
| 1 | Headline guidance (revenue range) | Range from the release; can fail either side. OK. |
| 2 | Headline guidance (gross margin floor) | "at least 83.0%", the guided low end. OK. |
| 3 | Management statement (both bit growth and price positive) | Checkable in the Q1 release's volume/price sentence; if the sentence is absent next quarter it grades Dropped, which is the right outcome. OK. |
| 4 | Sharpening of "fastest-growing end market" into Datacenter > $2,977M | Labelled "our sharpening ... not management's number". OK. |
| 5 | Disclosure check, RPO > $59.8B | Labelled disclosure check, "quarter-end balance" stated. OK. |
| 6 | Management statement (more than eight NBM customers by the call) | Single direction, observable. OK. |
| 7 | Disclosure check, contract + refund liabilities > $2,742M | Labelled, "quarter-end balances", "(computed)". The quote is a loose fit (it is about guarantees releasing late), but the claim itself is mechanical. Acceptable. |
| 8 | Sharpening: days in inventory >= 160 | Labelled "our sharpening of 'consistent with current levels', which were 178 days, not management's number". OK. |
| 9 | Sharpening: Q1 gross capex > Q4's $562M | Labelled; note that management's sentence was about FY2027 vs FY2026, and the claim narrows it to Q1 vs Q4, which the label covers. OK. |
| 10 | Sharpening: buybacks >= $3.0B in Q1 | Labelled "our sharpening of 'very consistent' against $4.5B in Q4". OK. |

Fundamentals dominate (claims 3–10 are volume/price mix, end-market, RPO, deposits, customers, inventory, capex, buybacks); headline EPS is not a claim. The "Not sharpenable from this call" line is useful; its tag [Q4 FY2026 call, Q&A, Bernstein] fits only the pricing item (transcript:61–65), not the whole list, but the line makes no factual assertion, so it is left as is.

## 7. As-of discipline

Nothing relies on information published after 2026-08-17. Latest-dated items used: the FY2026 10-K (filed 2026-08-17, the cutoff itself), the Investor Day deck and release (2026-08-13), the Motley Fool transcript (call 2026-08-05, posted 2026-08-12), the cover-page share count "as of August 7, 2026". The WDC "monetize by the end of 2026" statement is quoted from the 10-K as an announced intention, not as an event. No later filing, price or news is referenced.

## 8. Verdict: REVISE — items for the writer

1. **business.md §3, footnote under the economics table (line 56), wrong sign.** "Without the impairments, FY2023 and FY2025 operating margins would be (22)% and (6)% (computed)". FY2025: operating loss (1,377) + goodwill impairment 1,830 = +453 on revenue 7,355 = **+6.2%**, a profit (10-K-FY2026:1161–1166). FY2023 reproduces: (−2,035 + 671) / 6,086 = −22.4% (Form10:3951–3954). Fix: "Without the impairments, FY2023's operating margin would still have been (22)% and FY2025's would have been +6% (computed)."
2. **business.md §4, footnote under the cash table (line 99), misattributed amount.** "because it nets $137M of sale-leaseback proceeds against capex". The Form 10 allocates **$134M** of the Milpitas sale-and-leaseback proceeds to the business (Form10:3726, 10019); $137M is the difference between gross purchases of PP&E (166, Form10:7426) and the net line (29, Form10:896), so about $3M is other property proceeds. Fix: "because it nets $137M of proceeds from property sales, mostly the $134M allocated from WDC's Milpitas sale-and-leaseback (a building sold and rented back), against capex [Form 10, MD&A; Combined Statements of Cash Flows]".
3. **business.md §7, capital-allocation table, "Term loan" row (line 150), unsupported figure.** "the final $650M 'settled in full' on March 4, 2026". No cached source gives the amount of the final payment: 10-K FY2026 Note 8 (10-K-FY2026:2412) and Item 7 (1116), and 10-Q Q3 (837, 1423), all say "settled in full the remaining outstanding principal amounts" with no dollar figure; FY2026 repayments total $1,900M (10-K-FY2026:1696; 10-Q:316, 1677) against about $1.9B outstanding at June 27, 2025 (10-K-FY2025:1488). Fix: "$100M repaid in FY2025 and the remaining $1,900M in FY2026, 'settled in full' on March 4, 2026 with a $46M write-off of issuance costs; debt now zero; $1.5B revolving credit line undrawn". If the $650M came from an uncached document (for example the Q2 FY2027 10-Q's balance at January 2, 2026), either cache it and tag it or drop the figure.

After these three edits, re-run the counter; the drafts stand at 2,845 / 1,115 after the reviewer's glosses, so there is room.

## 9. Direct edits made by the reviewer (recorded)

business.md:

1. §1 line 12: labelled the 2016 "operating segment" bridge as an inference and quoted the Form 10 wording ("an operating segment of WDC" for the periods covered, Form10:7515).
2. §1 line 14: allocated costs changed from "about three-quarters ... in FY2023 and FY2024" to "about 70% of R&D plus SG&A in FY2023 and 75% in FY2024 (computed)" and the tag corrected to [10-K FY2025, Note 10; 10-K FY2026, Note 10] (FY2023 column is only in the FY2025 10-K and the Form 10).
3. §2 line 35: gloss on "limited price protection" (credits to resellers when list prices fall on stock they hold).
4. §3 line 56 footnote: added the sentence that the idle-capacity row is the Flash Ventures series from the related-party notes and that the MD&A's company-wide totals were $296M (FY2023) and $252M (FY2024) [Form 10, MD&A; Flash Ventures note; 10-K FY2026, Item 1A].
5. §3 line 60: "[average selling price]" inserted after "ASP" inside the quote.
6. §3 line 64: gloss on depreciation.
7. §4 line 96: gloss on shareholders' equity.
8. §5 line 109: gloss "(that is, rationed among customers)" after the "on allocation" quote.
9. §5 line 115: the $16.5B sentence relabelled as the writer's observation, with the likely timing reason (the slide counts the two deals signed after year-end; the 10-K balances are at July 3, 2026) and Note 17 added to the tag.
10. §6 item 2: "YMTC" expanded to "Yangtze Memory Technologies (YMTC)".
11. §6 item 7: "Section 232 and 301 investigations" reworded to "US tariff investigations under Sections 232 and 301 of trade law"; DRAM glossed; and the DRAM quote corrected to the 10-K's contiguous words "a commodity component that has experienced supply constraints" (10-K-FY2026:479) — the draft had spliced "which has experienced supply constraints" from non-adjacent words.
12. §7 table: "revolver" changed to "revolving credit line"; "three-year lock-up" glossed.
13. §7 line 145: "EPS" spelled out.
14. §7 line 157: "[the term loan]" inserted after "TLB" inside the quote.
15. Glossary: added "Goodwill impairment"; extended "Capex" with the PP&E line name; extended "10-K / 10-Q" with 8-K.

outlook.md:

16. Line 4 preamble: added the sentence defining "sequential" and "EPS".
17. §1 row 1: added [10-Q Q3 FY2026, Item 2] to the tag for the Q3 bits statement (10-Q:1533 confirms "exabytes sold remained flat" year-over-year).
18. §2 line 24: glossed "AI inference".
19. §3 line 32: glossed "QLC".
20. §3 line 40: glossed "taped out".

Word counts after these edits (canonical counter, `/tmp/sndk-orch/wc_prose.py`): business.md 2,845 (range 2,000–3,000; was 2,713); outlook.md 1,115 (range 800–1,200; was 1,065). Tag-coverage helper: every prefix still maps; its remaining "MISSING" hits are compound tags joined with ";" and the bracketed insertions inside quotes ("maintain[s]", "[average selling price]", "[the term loan]"), which it mistakes for tags.

---

## Cycle 2 (final) — re-verification of the three REVISE items

_2026-09-09. The writer changed only the three passages below by exact-string replacement; outlook.md untouched. Reviewer confirmed all 24 cycle-1 direct edits are still present (each grepped, one hit apiece), the ten `##` headings are unchanged, the line count is unchanged (209), and the tag helper shows 108 tags (one more than cycle 1: the added `[Q3 FY2026 release]` tag, which maps to the existing Sources row at business.md line 204); its remaining "MISSING" hits are the same compound tags and bracketed quote insertions as before._

| # | Writer's new passage | Verified against | Result |
|---|---|---|---|
| 1 | §3 footnote (line 58): "Without the impairments, FY2023's operating margin would still have been (22)% and FY2025's would have been +6% (computed) [Form 10, Combined Statements of Operations; 10-K FY2026, Item 7]." | 10-K-FY2026:1167 operating loss (1,377), 1161 goodwill 1,830, 1155 revenue 7,355: (−1,377 + 1,830) / 7,355 = +6.2%. Form10:3951–3953 (and the statements of operations at 7352–7354): goodwill 671, operating loss (2,035), revenue 6,086: (−2,035 + 671) / 6,086 = −22.4%. | PASS |
| 2 | §4 footnote (line 99): "...because it nets $137M of proceeds from property sales, mostly the $134M allocated from WDC's Milpitas sale-and-leaseback (a building sold and rented back), against capex, and its FY2022–FY2024 adjusted figures use an older definition [Form 10, MD&A; Combined Statements of Cash Flows]." | Form10:7427 "Proceeds from the sale of property, plant and equipment \| 137"; Form10:7426 purchases (166); Form10:896 net (29) = −166 + 137; Form10:897 free cash flow (338) = −309 − 29; Form10:3726 and 10019 "$134 million of the net proceeds from the sale-leaseback transaction has been allocated to us". Wording now matches the sources exactly. | PASS |
| 3 | §7 table, Term loan row (line 150): "$100M repaid in FY2025 and the remaining $1,900M in FY2026, of which $650M was repaid in Q3 FY2026 when the loan was \"settled in full\" on March 4, 2026, with a $46M write-off of issuance costs; debt now zero; $1.5B revolving credit line undrawn [10-K FY2026, Note 8; Item 8; Q3 FY2026 release]" | press-release-FY2026-Q3:239 "Repayment of debt \| (650) \| — \| (1,900) \| —" under the header at 197–198 "Three Months Ended \| Nine Months Ended / April 3, 2026 \| March 28, 2025 \| April 3, 2026 \| March 28, 2025": $650M repaid in the quarter ended April 3, 2026, $1,900M in the nine months. 10-K-FY2026:2411 and 1116 (March 4, 2026, "settled in full", $46M); 1696 "Repayment of debt \| ( 1,900 ) \| ( 100 )" ($1,900M FY2026, $100M FY2025; also 10-K-FY2025:2372); 1359 revolver undrawn. March 4 falls inside the quarter ended April 3, so "repaid in Q3 FY2026 when the loan was settled in full" is supported. | PASS |

**Withdrawal recorded (§17 rule).** Cycle-1 finding "the $650M is not in any cached source" was wrong as to the cache and right as to the tag: the figure sits in `press-release-FY2026-Q3.txt` line 239 (condensed cash-flow statement, three-months column), which the reviewer did not grep because the original tag named only [10-K FY2026, Note 8], and neither the 10-K nor the 10-Q prints a quarterly repayment figure. The writer's fix adds the release tag, so the number is now traceable. Lesson for the reviewer: when a figure is missing from the cited filing, grep every cached file before ruling it absent.

Direct edits in cycle 2: none. Word counts after cycle 2 (canonical counter): business.md **2,865** (range 2,000–3,000); outlook.md **1,115** (range 800–1,200).

