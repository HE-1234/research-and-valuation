# Micron Technology (MU) — Reviewer report, Q3 FY2026 (quarter ended May 28, 2026)

_Reviewed 2026-09-07 against `sources/FY2026-Q3/` only. As-of cutoff 2026-06-25. Drafts reviewed: `business.md` and `outlook.md` (first run). Line references below are to the cached `.txt` files; `p.N` for the prepared remarks is the PDF page._

**Final verdict (cycle 2): PASS.** Cycle 1 returned REVISE with 11 items; the writer applied all 11 and each was re-verified against the cached sources (see "Cycle 2" at the end). The cycle-1 findings below are kept as the record.

---

## 1. Skeleton compliance

| Check | Result |
|---|---|
| business.md §6 headings 1–8, Glossary, Sources | All present, in order, correct titles. |
| outlook.md §7 headings 1–5, Sources; §6 Tone shift omitted | All present; §6 correctly omitted (first run). |
| Quarter label with calendar parenthetical on first use | business.md line 2 `Q3 FY2026 (quarter ended May 28, 2026)`; outlook.md title line the same. Both pass. |
| outlook header tier line | `Transcript source tier: company-published (prepared remarks); Q&A: none.` — matches MANIFEST.md's suggested header exactly and the manifest's tier outcome (tier 1 scripted portion, no Q&A at any tier). |
| §8 marked `_Proposed — owner to review and lock._` | Present (business.md line 146). outlook.md §1 also says "pending owner lock". |
| Sources tables map every tag prefix used | Script check: business.md uses 11 prefixes (10-K FY2025, 10-K FY2023, 10-Q Q3 FY2026, DEF 14A 2025, 8-K 2026-01-21/03-25/06-09, Q3 FY2026 remarks/release/slides, Q4 FY2025 release), all mapped; outlook.md uses 7 (remarks, release, slides, Q2 FY2026 release, 10-Q, 10-K FY2025, 8-K 2026-03-25), all mapped. Both tables state that remarks `p.N` tags are PDF pages because the PDF has no printed numbers, and that slide page numbers match PDF pages. |

## 2. Rubric (§14)

| # | Question | Answer | Reasoning |
|---|---|---|---|
| 1 | Explain what the company does and who pays, in two sentences? | Yes | §1 paragraph 1 does it in two sentences (memory chips; device and data-center makers pay), and §2 names the four customer groups with sizes. |
| 2 | Know what would kill it and the early warning? | Yes | §6 ranks seven scenarios; each has a trigger and a watchable sign (price direction in the 10-Q, inventory days, CXMT/YMTC named in MD&A, the 10% customer line, milestone dates, RPO). |
| 3 | Know why margins are what they are and whether cost scales with usage? | Yes | §3 states costs are mostly fixed (quoted), shows the FY2023 vs Q3 FY2026 columns, and says gross margin moves one-for-one with price. |
| 4 | Predict what the scorecard checks next quarter from outlook §5 alone? | Yes | Nine numbered claims, each with a threshold, a date/period and a source quote; sharpenings labelled. Two need tightening (see REVISE 3 and 6) but are already checkable. |
| 5 | Nothing required knowledge I don't have? | Yes, after reviewer glosses | The drafts leaned on unexplained finance and chip terms (gross/operating margin, depreciation, receivables, equity, SSD, yield, qualification, tender offer, 10-K/10-Q, EPS, RPO in the outlook). All glossed directly; list in §4 below. |

## 3. Citation spot-check

Every number in business.md §2, §3, §4 and §7 tables and outlook.md §1 table was grepped in the cited cached file; every figure labelled "(computed)" was re-derived; all quotes in outlook §4 and §5 and 40+ additional source-tagged prose sentences were checked verbatim (a script normalised quotes/dashes/whitespace and searched every cached `.txt`). Grouped rows carry an item count.

**Totals: 377 items checked; 372 PASS (2 of them after a reviewer tag/label fix); 3 FAIL (1 fixed directly by the reviewer, 2 for the writer); 2 UNVERIFIABLE (for the writer).**

### A. business.md §2 — revenue by technology (30 items)

| Item | Tag | Found at (file:line) | Result |
|---|---|---|---|
| DRAM FY2021 20,039; FY2022 22,386 | 10-K FY2023, Item 8 | 10-K-FY2023.txt:2281 | PASS (2) |
| DRAM FY2023 10,978; FY2024 17,603; FY2025 28,578 | 10-K FY2025, Note 21 | 10-K-FY2025.txt:2442 | PASS (3) |
| DRAM Q3 FY2026 31,328 | 10-Q, Note 14 | 10-Q-FY2026-Q3.txt:693 | PASS |
| NAND 7,007; 7,811 / 4,206; 7,227; 8,503 / 9,943 | as above | 10-K-FY2023.txt:2282; 10-K-FY2025.txt:2443; 10-Q:694 | PASS (6) |
| Other 659; 561 / 356; 281; 297 / 185 | as above | 10-K-FY2023.txt:2283; 10-K-FY2025.txt:2444; 10-Q:695 | PASS (6) |
| Totals 27,705; 30,758 / 15,540; 25,111; 37,378 / 41,456 | as above | 10-K-FY2023.txt:2284; 10-K-FY2025.txt:2445; 10-Q:696 | PASS (6) |
| DRAM share (computed) 72 / 73 / 71 / 70 / 76 / 76% | computed | re-derived 72.3 / 72.8 / 70.6 / 70.1 / 76.5 / 75.6% | PASS (6) |

### B. business.md §2 — revenue by business unit (40 items)

| Item | Tag | Found at | Result |
|---|---|---|---|
| CMBU 1,872 / 3,792 / 13,524; CDBU 2,124 / 4,984 / 7,229; MCBU 7,394 / 11,667 / 11,859; AEBU 4,139 / 4,631 / 4,753; All other 11 / 37 / 13; totals | 10-K FY2025, Item 7 | 10-K-FY2025.txt:1334–1339 (also Note 27 at 2639, 2649, 2659) | PASS (18) |
| Q3 FY2026 13,769 / 11,524 / 11,521 / 4,634 / 8 / 41,456 | 10-Q, Item 2 | 10-Q-FY2026-Q3.txt:922–927 (Note 17 at 766) | PASS (6) |
| Two data-center units' share (computed) 26 / 35 / 56 / 61% | computed | re-derived 25.7 / 34.9 / 55.5 / 61.0% | PASS (4) |
| Old basis CNBU 12,280 / 13,693 / 5,710; MBU 7,203 / 7,260 / 3,630; EBU 4,209 / 5,235 / 3,637; SBU 3,973 / 4,553 / 2,553 | 10-K FY2023, Item 7 | 10-K-FY2023.txt:1196–1199 | PASS (12) |

Five-year segment story: correctly handled. The only five-year series presented is by technology, which matches both 10-Ks; the business-unit table is FY2023–FY2025 plus Q3 only, with the FY2021–FY2023 old-basis units given separately and an explicit sentence that they do not map onto the new ones (10-K FY2025 Note 27 L2618–2620 confirms recast "effective in the fourth quarter of 2025" with prior periods "retrospectively adjusted", i.e. FY2023–FY2025 only).

### C. business.md §3 — economics table (42 items; revenue row is the same cells as A)

| Item | Tag | Found at | Result |
|---|---|---|---|
| DRAM price: FY2021 n/a (not in cached sources) | — | none of the cached filings discusses FY2021 vs FY2020 | PASS (honest "n/a") |
| DRAM price FY2022 n/s | 10-K FY2023, Item 7 | 10-K-FY2023.txt:1174 ("increases in bit shipments of slightly over 10%"; no price figure) | PASS |
| DRAM price FY2023 down high-40s% | footnote said 10-K FY2025 | 10-K-FY2023.txt:1168 (not in the FY2025 10-K: zero hits for "high-40") | PASS after reviewer tag fix (footnote now cites 10-K FY2023, Item 7 for FY2023 price changes) |
| DRAM price FY2024 up low-teens%; FY2025 up low-40s% | 10-K FY2025, Item 7 | 10-K-FY2025.txt:1313; 1307 | PASS (2) |
| DRAM price Q3 up low-60s% | 10-Q, Item 2 | 10-Q-FY2026-Q3.txt:894 | PASS |
| NAND price FY2021 n/a; FY2022 up low-single-digit%; FY2023 down low-50s%; FY2024 up low-30s%; FY2025 n/s; Q3 up mid-80s% | as above | 10-K-FY2023.txt:1176; 1170 (tag fixed as above); 10-K-FY2025.txt:1315; 1309 (high-teen bit shipments, no price); 10-Q:896 | PASS (6) |
| Gross margin 38 / 45 / (9) / 22 / 40 / 84.6% | 10-K FY2023 & FY2025, Item 7; release | 10-K-FY2023.txt:1154; 10-K-FY2025.txt:1291; press-release.txt:35 (GAAP column) | PASS (6) — row is GAAP throughout and the prose says so |
| Operating margin 23 / 32 / (37) / 5 / 26 / 80.4% | as above | 10-K-FY2023.txt:1159; 10-K-FY2025.txt:1296; press-release.txt:38 (GAAP) | PASS (6) |
| R&D 2,663 / 3,116 / 3,114 / 3,430 / 3,798 / 1,316 | Item 8; 10-Q | 10-K-FY2023.txt:1155; 10-K-FY2025.txt:1292; 10-Q:125 and press-release.txt:135 | PASS (6) |
| Capex 10,030 / 12,067 / 7,676 / 8,386 / 15,857 / 7,826 | Item 8; release | 10-K-FY2023.txt:1610; 10-K-FY2025.txt:1767; press-release.txt:284 | PASS (6) |
| Capex/revenue (computed) 36 / 39 / 49 / 33 / 42 / 19% | computed | re-derived 36.2 / 39.2 / 49.4 / 33.4 / 42.4 / 18.9% | PASS (6) |

### D. business.md §3 — prose figures (13 items)

| Item | Tag | Found at | Result |
|---|---|---|---|
| COGS up 5% (computed, 6,105 → 6,400) | 10-Q Item 1 | 10-Q-FY2026-Q3.txt:123; press-release.txt:133; re-derived 4.8% | PASS |
| Five-year capex $54.0B vs revenue $136.5B ≈ 40% (computed) | Item 8 both 10-Ks | sums 54,016 and 136,492; 39.6% | PASS |
| FY2023: $1,831M write-down; $382M underutilization; $5,745M operating loss; revenue −49% | 10-K FY2023, Item 7 | 10-K-FY2023.txt:1187 (and 1598); 1121; 1159; 1166 | PASS (4) |
| Depreciation $8.28B FY2025 | 10-K FY2025, Note 8 | 10-K-FY2025.txt:1980 | PASS |
| 84.9% non-GAAP vs 84.6% GAAP | release | press-release.txt:35 | PASS |
| CHIPS up to $6.4B; milestone quote; ITC 25%→35% July 2025; Japan ¥500B ≈ $3.4B; Gujarat 70% | 10-K FY2025, Note 20 | 10-K-FY2025.txt:2417; 2419; 2429 ("On July 4, 2025 … increased the investment tax credit from 25% to 35%"); 2435; 2435 (50% central + 20% state) | PASS (5) — 70% is a sum; "(computed)" label added by reviewer |

### E. business.md §4 — cash table (56 items)

| Item | Tag | Found at | Result |
|---|---|---|---|
| Net income 5,861 / 8,687 / (5,833) / 778 / 8,539 / 47,268 | Item 8; 10-Q Item 1 | 10-K-FY2023.txt:1463; 10-K-FY2025.txt:1624; 10-Q-FY2026-Q3.txt:135 | PASS (6) |
| Operating cash flow 12,468 / 15,181 / 1,559 / 8,507 / 17,525 / 45,702 | as above | 10-K-FY2023.txt:1608; 10-K-FY2025.txt:1765; 10-Q:319 | PASS (6) |
| Capex (10,030) … (15,857) / (19,602) | as above | 10-K-FY2023.txt:1610; 10-K-FY2025.txt:1767; 10-Q:321 | PASS (6) |
| Government incentive proceeds 495 / 115 / 710 / 315 / 2,005 / 2,989 | as above | 10-K-FY2023.txt:1613; 10-K-FY2025.txt:1769; 10-Q:323 | PASS (6) |
| Free cash flow (computed) 2,933 / 3,229 / (5,407) / 436 / 3,673 / 29,089 | computed | re-derived exactly from the three rows above | PASS (6) |
| Stock-based compensation 378 / 514 / 596 / 833 / 972 / 954 | as above | 10-K-FY2023.txt:1599; 10-K-FY2025.txt:1756; 10-Q:311 | PASS (6) |
| Dividends — / 461 / 504 / 513 / 522 / 437 | as above | 10-K-FY2023.txt:1621; 10-K-FY2025.txt:1775; 10-Q:331 | PASS (6) |
| Buybacks 1,200 / 2,432 / 425 / 300 / — / 650 | as above | 10-K-FY2023.txt:1622; 10-K-FY2025.txt:1776; 10-Q:330 | PASS (6) |
| Debt repaid 1,520 / 2,032 / 761 / 1,897 / 4,619 / 9,380 | as above | 10-K-FY2023.txt:1620; 10-K-FY2025.txt:1774; 10-Q:328 | PASS (6) |
| Adjusted FCF $3.72B FY2025; $18.3B Q3 FY2026 | Q4 FY2025 release; Q3 release | press-release-Q4-FY2025.txt:68 and 301 (3,721); press-release.txt:42 and 288 (18,304) | PASS (2) |

### F. business.md §4 — prose figures (15 items)

| Item | Tag | Found at | Result |
|---|---|---|---|
| Five-year OCF $55.2B; five-year FCF $4.9B; 9M FCF $29.1B is "six times" | computed | sums 55,240; 4,864; 29,089 ÷ 4,864 = 5.98 | PASS (3) |
| FY2025 OCF $17.5B double NI $8.5B; FY2023 OCF $1.6B vs capex $7.7B; borrowed $6.7B | Item 8 | 10-K-FY2025.txt:1765, 1624; 10-K-FY2023.txt:1608, 1610, 1619 (proceeds from issuance of debt 6,716) | PASS (3) |
| Return on capital ~16%; five-year NI $18.0B; equity $44–54B; ~8%/yr | computed | 8,539 ÷ 54,165 = 15.8%; NI sum 18,032; equity 43,933 (10-K-FY2023.txt:1564, FY2021) to 54,165 (10-K-FY2025.txt:1698); 3,606 ÷ ~47,000 ≈ 7.7% | PASS (4) |
| Q3 net income $28.2B exceeds five-year total | release | press-release.txt:39 (28,243 > 18,032) | PASS |
| Receivables $31.0B "due to higher revenue"; trade receivables 59 days vs 58 at year-end | 10-Q Note 5; Item 2; Q4 FY2025 release | 10-Q:427 (26,894; 7,163); 10-Q:1085 (quote); press-release-Q4-FY2025.txt:45 (Q4 revenue 11,315); 26,894 ÷ 41,456 × 91 = 59.0; 7,163 ÷ 11,315 × 91 = 57.6 | PASS (3) |
| $5.79B noncurrent income taxes payable; 15% minimum tax offsets Singapore incentive | 10-Q Note 15 | 10-Q:725; 721 | PASS |

### G. business.md §7 — capital allocation table (15 items)

| Item | Tag | Found at | Result |
|---|---|---|---|
| $8,511M principal for $8,985M cash; $4,320M April tender (computed sum); total debt $14,577M → $5,722M; $323M loss | 10-Q Note 9 | 10-Q-FY2026-Q3.txt:520; 514–519 (738+429+574+685+864+1,030 = 4,320, all dated April 3, 2026); 494; 522 | PASS (5) |
| $325M in the release reconciliation | Q3 release | press-release.txt:266 | PASS — the 323 vs 325 conflict is stated and each figure tied to its own source |
| Six note series tendered March 25, 2026 | 8-K 2026-03-25 | 8-K-2026-03-25.txt:89–92 | PASS |
| Buybacks $650M in 9M; none in Q3; $7.84B of $10B used | 10-Q Note 11; Part II Item 2 | 10-Q:598; 1811 ($2.16B remaining) | PASS (3) |
| Dividend $0.115 → $0.15 (+30%, computed); $0.46/yr FY2023–FY2025 | 10-Q Note 11; 10-K FY2025 Item 8 | 10-Q:602; 0.15 ÷ 0.115 = 1.30; 10-K-FY2025.txt:1722, 1730, 1737 | PASS (3) |
| Capex "approximately $27 billion" net | 10-Q Item 2 | 10-Q:1034 | PASS |
| Tongluo $1.8B, March 2026, Powerchip | 10-Q Note 7 | 10-Q:458 | PASS |
| Cash and investments $30.13B; net cash $24.4B | 10-Q Item 2; slides p.42 | 10-Q:1024; slides.txt:805 (24,433) | PASS — but the two figures are on different bases (see REVISE 7) |

### H. outlook.md §1 — indicator table and line 20 (46 items)

| Item | Tag | Found at | Result |
|---|---|---|---|
| Row 1: DRAM $31,328M, bits up low-single-digit, prices up low-60s; NAND $9,943M, bits mid-single-digit, prices mid-80s | 10-Q Item 2; Note 14 | 10-Q:693–694; 894; 896 | PASS (6) |
| Row 1: Q2 DRAM $18,768M; NAND $4,997M | slides p.33 | slides.txt:621; 624 | PASS (2) |
| Row 1: "$33.5 billion ± $750 million" | Q2 release | press-release-Q2-FY2026.txt:69 | PASS |
| Row 2: 84.9%; 74.9%; "Approximately 81%" | Q3 release; Q2 release | press-release.txt:35 (non-GAAP columns); press-release-Q2-FY2026.txt:70 | PASS (3) — non-GAAP labelled |
| Row 3: BU Q3 and Q2 revenues; 61% / 56% (computed) | 10-Q Item 2; release | 10-Q:922–925; press-release.txt:49, 53, 57, 61; re-derived 61.0 / 56.3% | PASS (10) |
| Row 4: $8,567M; 122 days (computed); "days of inventory at 120"; DRAM "below 120 days"; Q2 $8,267M; 123 days (computed) | 10-Q Note 6; remarks p.9; Q2 release | 10-Q:439 (and 186); 8,567 ÷ 6,400 × 91 = 121.8; prepared-remarks.txt:424–425 (p.9); press-release-Q2-FY2026.txt:146, 111 (COGS 6,105); 8,267 ÷ 6,105 × 91 = 123.2 | PASS (6) — 120 vs 122 conflict shown with both sources |
| Row 5: gross $7,826M / net $7,084M; ~$27B; Q2 $6,387M / $5,004M; $4.5B "a reasonable quarterly baseline" | release; 10-Q; 10-K Item 7 | press-release.txt:284, 287; 10-Q:1034; 10-K-FY2025.txt:1452 | PASS (6) |
| Row 6: RPO "approximately $5 billion"; $422M; "not material" at Aug 28, 2025 | 10-Q Note 14 | 10-Q:704 | PASS (3) — quarter-end figures correctly separated from the $100B post-quarter figure |
| Row 7: $5,722M; $30.13B; $24,433M; Q2 $10,142M (585 + 9,557); $16.65B; $6,511M; tender offers | 10-Q Note 9, Item 2; slides p.42; Q2 release; 8-K | 10-Q:494; 1024; slides.txt:799–805 (net cash 24,433 / 6,511; components sum to 16,653 incl. $26M restricted cash, also slides.txt:574); press-release-Q2-FY2026.txt:159, 162; 8-K-2026-03-25.txt:89–92 | PASS (7) — basis note, see REVISE 7 |
| Line 20: $25.11 vs guidance $19.15 ± $0.40 | release; Q2 release | press-release.txt:40; press-release-Q2-FY2026.txt:72 | PASS (2) |

### I. Prose sentences and quotes (120 items; includes every quote in outlook §4 and §5)

| Item | Tag | Found at | Result |
|---|---|---|---|
| Outlook §4 release quotes: "$50.0 billion ± $1.0 billion"; "Approximately 86%"; "Approximately $1.86 billion"; "Approximately $1.65 billion"; "$30.73 ± $1.00"; "$31.00 ± $1.00"; "based on approximately 1.15 billion diluted shares" | Q3 release | press-release.txt:69, 70, 71, 71, 72, 72, 323 | PASS (7) — character-exact, GAAP and non-GAAP each labelled |
| Outlook §4 remarks quotes: tax "around 15.0%"; capex "around $10 billion … approximately $27 billion"; "free cash flow to increase substantially again"; "trade or geopolitical developments"; FY2027 opex "approximately $1 billion"; FY2027 quarterly capex "above fiscal Q4 levels …"; "From Dec. 9, 2026 … 100% of our excess cash" | remarks p.10 | prepared-remarks.txt:460; 463–464; 469; 473; 456; 465–466; 469–471 | PASS (7) — character-exact |
| Outlook §5 quotes under claims 1–9 | remarks p.10, p.10, p.10, p.10, p.10, p.7, p.7, p.1, p.6 | prepared-remarks.txt:450; 450–451; 454; 463–464; 469; 323; 312–313; 40–41; 268–269 | PASS (9) — all exact including punctuation; page tags correct |
| Outlook §2–§3 quotes (structurally transformed; strategic asset; architecturally dependent; tight beyond calendar 2027; improve gradually in 2028 …; rising bit costs; blended DRAM cost per bit; $25B / $100B run rate; HBM4 12-high / $1B; SSD $5B doubling; AI context memory storage and HDD displacement; balance sheet more in FQ4; financing-related cash flows; Tongluo "about a quarter earlier") | remarks p.2, p.2, p.2, p.1, p.2, p.4, p.4, p.1, p.4, p.1, p.5, p.7, p.7, p.6 | prepared-remarks.txt:55; 82; 79–80; 38–39; 63–64; 176; 177; 36–37; 166–168; 37–38; 203–204; 323; 324; 273–275 | PASS (14) |
| Outlook §3: PC and smartphone revenue "is expected to grow despite unit volume declines" | remarks p.5 | prepared-remarks.txt:208: "PC and smartphone **industry** revenue is expected to grow …" | **FAIL** — the quoted fragment is exact but the lead-in drops "industry", turning an industry forecast into a Micron revenue forecast (REVISE 3) |
| Business §1 quotes: "reluctant to enter into long-term, fixed-price purchase contracts"; "periodically negotiated to reflect market conditions"; "from plus low 40% to a minus high 40% range" (with "past five years"); "at a rate greater than our ability and the industry's ability to increase supply"; "critical information infrastructure" | 10-K FY2025 Item 1, Item 1, Item 1A; 10-Q Item 2; 10-K Item 7 | 10-K-FY2025.txt:265; 265; 533 ("In the past five years …"); 10-Q:857; 10-K-FY2025.txt:1278 (Item 7 runs 1264–1586) | PASS (5) |
| Business §1: "DRAM was 76% of revenue in FY2025 and NAND 23%" | 10-K FY2025 Note 21 | 10-K-FY2025.txt:2442–2445; the 10-K never prints "76%", so this is 28,578 ÷ 37,378 and 8,503 ÷ 37,378 | PASS after reviewer fix ("(computed …)" label added) |
| Business line 4: "FY2026 ends September 3, 2026" | 10-K FY2025 Item 7; 10-Q Note 1 | not in the 10-K (L111, 1266: "Fiscal 2025, 2024, and 2023 each contained 52 weeks"); date is at 8-K-2026-01-21.txt:140 and DEF14A-2025.txt:40; "contains 14 weeks" at 10-Q:366 | PASS after reviewer fix (8-K 2026-01-21 added to the tag) |
| Business §1 history: CEO May 2017; Lehi to TI $893M (2022); 3D XPoint $435M (2021); ~15% headcount; CHIPS agreements Dec 9, 2024; reorganisation in FY2025 | 10-K FY2025 Item 1; 10-K FY2023 Item 7; 10-K FY2025 Note 22, Note 20, Note 27 | 10-K-FY2025.txt:420; 10-K-FY2023.txt:1141; 1139; 10-K-FY2025.txt:2469; 2417; 2618 | PASS (6) |
| Business §2: distributors sell "our competitors' products"; ~half from top ten; one customer 17% (CMBU); ~half data center | 10-K FY2025 Item 1; Note 28; Item 1A | 10-K-FY2025.txt:263; 267; 2720; 797 | PASS (4) |
| Business §2/§5 SCA figures: 16 SCAs; 2026–2030; "take-or-pay agreements, with binding commitments to purchase specific volumes"; "roughly 20% of our DRAM volume and a third of our NAND volume"; "approximately half or more of our company revenue"; 14 of 16 ≈ $100B; "$22 billion"; "approximately $18 billion"; "In a period of significant shortage …"; "This cash will be returned to customers …" | remarks p.1, p.3, p.3, p.3, p.3, p.3, p.3, p.7, p.3, p.7 | prepared-remarks.txt:40–41; 105; 115–116; 106–107; 111; 130–131; 134; 319–320; 139–140; 324–325 (slides p.9–10 carry the same text) | PASS (10) — each figure on the right page; see REVISE 2 for the quarter-end framing |
| Business §3: fixed-cost quote; "tool replacements and upgrades to improve productivity"; "supply in 2030 and beyond"; Idaho mid-2027 / late 2028; Tongluo mid-2027 | 10-K FY2025 Item 1A; remarks p.6; 10-Q Item 2 | 10-K-FY2025.txt:565; prepared-remarks.txt:261–262; 10-Q:1040; 1038; 1060 | PASS (5) |
| Business §5: over 60,000 patents; six named competitors | 10-K FY2025 Item 1 | 10-K-FY2025.txt:323; 271 (Samsung, SK hynix, Kioxia, Sandisk, CXMT, YMTC) | PASS (2) |
| Business §5: CXMT and YMTC "added to the list only in FY2025" | 10-K FY2025 Item 1; 10-K FY2023 Item 1 | 10-K-FY2023.txt:236 lists Kioxia, Samsung, SK hynix, Western Digital (CXMT/YMTC appear only at L238 as state-backed entities); the FY2024 10-K is not cached | **UNVERIFIABLE** — "only in FY2025" cannot be shown (REVISE 5) |
| Business §5 and glossary: "fabs costing tens of billions" / "a leading-edge one costs tens of billions of dollars" | none | no cached file contains a fab cost figure ("tens of billions": 0 hits in all sources) | **UNVERIFIABLE** — unsourced figure (REVISE 4) |
| Business §5: "If we do not meet their product design schedules …"; "maintaining stable bit share" | 10-K FY2025 Item 1A; Item 2 | 10-K-FY2025.txt:671; 1176 (Item 2) and 1458 (Item 7) | PASS (2) |
| Business §6: "reduce memory and storage content"; "suppliers shift capacity from HBM to conventional DRAM"; "oversupply … including by the Chinese government"; "achieving acceptable yields and quality"; Taiwan majority of DRAM output; $19.0B of $47.3B long-lived assets; ~80% shipped outside US; "may not prohibit our competitors …"; Section 232 "may result in industry-wide additional tariffs and trade restrictions"; "up to all of certain incentives being clawed back"; Idaho "early calendar 2026"; China + Hong Kong ≈16% (FY2022–FY2024) → 10% (FY2025) | 10-Q Part II 1A; 10-K FY2025 Item 1A ×6; Note 29; 10-K FY2023 Item 7; Notes 29 / FY2023 Item 8 | 10-Q:1277; 10-K-FY2025.txt:669; 273 and 653; 661; 643; 2746 and 2754; 595; 641; 1009; 741; 10-K-FY2023.txt:1319 (Item 7; also 1037 in Item 2); 10-K-FY2025.txt:2736 + 2738 and 10-K-FY2023.txt:2535 + 2539 → 16.2 / 16.2 / 16.4 / 10.1% | PASS (12) — Note 29 revenue is by customer headquarters, matching the draft's wording |
| Business §6 item 6: "the agreements restrict buybacks and special dividends for five years from December 9, 2024" | 10-K FY2025 Item 1A; Note 20 | 10-K-FY2025.txt:2421: special/one-time dividends restricted for five years; share repurchases permitted in the first two years up to specified amounts and "not restricted during the final three years … if certain financial and other conditions are satisfied" | **FAIL** — buyback restriction overstated (REVISE 1) |
| Business §6 item 7: "could constrain our available supply and limit our flexibility …" | 10-Q Part II 1A | 10-Q:1487 reads "could **also** constrain …" | **FAIL** (verbatim) — fixed by reviewer: quote now begins at "constrain" |
| Business §6 item 7: "if customers fail to meet their purchase commitments …" quote; ceiling at calendar-Q2-2026 prices | 10-Q Part II 1A; Item 2 | 10-Q:1487; 863 | PASS (2) |
| Business §7: Mehrotra quote; SanDisk 1988–2016; age 67; Murphy April 2022 / Qorvo six years; "Seven of eight … independent"; Liu TSMC Executive Chairman; Swan Intel CEO; Dugle lead independent; Björlin (ex-NVIDIA) June 2026; Vanguard 8.4%, BlackRock 7.6%, Capital World 6.3%; insiders < 1% | DEF 14A; 10-K Item 1; 8-K 2026-06-09 | DEF14A-2025.txt:223; 224; 222; 10-K-FY2025.txt:423 (June 2016–April 2022); DEF14A:153; 212; 242; 423; 8-K-2026-06-09.txt:13–19; DEF14A:2197–2199; 2214–2216 | PASS (12) |
| Business §7 pay: $30.9M total; $25.4M stock; 50% profitability goals; HBM3E yield; "Days of inventory outstanding"; PRSUs on HBM / data-center SSD share and rTSR vs SOX; bonus "suspended in February 2023 …" | DEF 14A SCT; CD&A | DEF14A-2025.txt:1510 ($30,940,146; $25,360,029); 1134; 1171; 1172; 1076 and 919; 1550 | PASS (7) |
| Business §7: capex cut 36% (computed) | 10-K FY2023 | 12,067 → 7,676 = −36.4% | PASS |
| Business §8 figures: 61%; FY2023 180 days (computed); ~$27B; RPO ~$5B / $422M; $5.7B debt / $30.1B cash | 10-K FY2023; 10-Q | 10-K-FY2023.txt:1509 (8,387), 1153 (16,956): 8,387 ÷ (16,956 ÷ 364) = 180.0; 10-Q:1034; 704; 494; 1024 | PASS (6) |
| Business §8 indicator 6: "management said RPO will be disclosed each quarter" | (untagged table cell) | prepared-remarks.txt:310–311: "we are disclosing remaining performance obligations (RPO) starting this May quarter" | PASS as paraphrase; suggest quoting "starting this May quarter" (minor, REVISE 9) |
| "contains 14 weeks" (both files) | 10-Q Note 1 | 10-Q:366 | PASS |

Known source conflicts (task list): all five are cited to the right source and labelled — $323M (10-Q Note 9 L522) vs $325M (release L266) in the §7 table; customer deposits "in financing-related cash flows" (remarks p.7 L324) vs the 10-Q cash flow statement with no such line (10-Q:318–334) in outlook §3, with the $422M contract liability tied to Note 14; days of inventory 120 (remarks p.9) vs 122 computed in outlook §1 row 4; Idaho "early calendar 2026" (10-K FY2023 Item 7 L1319) vs "mid-calendar 2027" (10-Q L1038 and remarks p.6) in §1 and §6. The FY2025 10-K's intermediate date, "second half of calendar 2027" (L1170, L1456), is not mentioned; optional. GAAP and non-GAAP are never mixed in one row: the §3 table is GAAP throughout and says so; outlook §1 row 2 and §4 label non-GAAP explicitly.

## 4. Jargon audit

Reader: smart 16-year-old, no finance or chip background. Terms found without a plain phrase, an inferable name, or a glossary entry, and what was done (all fixed directly):

| Term | Where | Fix applied |
|---|---|---|
| gross margin | business §1 first use; used 8× | inline gloss at first use in §1; glossary line "Gross margin / operating margin" added |
| operating margin | business §3 prose | inline gloss ("what is left after research and overhead as well"); glossary line |
| depreciation | business §3, §4 | inline gloss at first use |
| receivables | business §4 | inline gloss |
| equity (return on capital) | business §4 | inline gloss "shareholders' equity, the accounting value of what shareholders own" |
| SSD | business §5, §7; outlook §3 | glossary line added |
| HDD | outlook §3 (inside a quote) | parenthetical after the quote |
| managed NAND | business §5 | inline gloss |
| qualified / qualification | business §5 | "(tested and approved)" |
| yield | business §6 (quote), §7 | parenthetical after the §6 quote |
| tender offer | business §7 table | parenthetical |
| 10-K / 10-Q / SEC | throughout | glossary line added |
| CHIPS Act | business §1 first use | inline gloss (2022 US law subsidising domestic chip factories) |
| bit share | business §5 (quote) | "(market share measured in bits)" |
| cleanrooms | business §3 | inline gloss |
| G9 NAND | business §3 | "Micron's ninth-generation NAND" (10-K FY2025 L175) |
| contingencies note | business §6 | "(the 10-Q's note on lawsuits and disputes)" |
| EPS | outlook line 20 | "(earnings per share)" |
| RPO, SCA | outlook §1 row 6 (first use in the outlook; outlook has no glossary) | both expanded in the row label |
| 12-high | outlook §3 (quote) | parenthetical "twelve DRAM chips stacked in one HBM package" |
| sequentially | outlook §3 (quote) | "(that is, versus the prior quarter)" |
| ID1 / ID2 | outlook §3 | "(the first Idaho fab)", "(the second)" |

Already adequate before review: EUV ("the newest chip-patterning machines"), MD&A (glossed in the §3 footnote, before its §5 use), non-GAAP, take-or-pay, RPO, node, wafer, bit, fab, HBM, DRAM, NAND, capex (all in the glossary); "SOX chip index"; "15% global minimum tax" (Pillar Two avoided); "hyperscale" avoided ("largest cloud companies"); Section 232 explained by its consequence.

## 5. Invented-number check

| Finding | Status |
|---|---|
| "fabs costing tens of billions" (§5) and glossary "costs tens of billions of dollars" — no source in the cache gives a fab cost | **For the writer** (REVISE 4). |
| "DRAM was 76% of revenue in FY2025 and NAND 23%" — the 10-K does not print these percentages; they are computed from Note 21 | Fixed: "(computed …)" label added. |
| "70% of the Gujarat plant's cost from India" — Note 20 says 50% central + 20% state | Fixed: label added. |
| "FY2026 ends September 3, 2026" tagged only to 10-K Item 7 and 10-Q Note 1, neither of which states the date | Fixed: 8-K 2026-01-21 added to the tag. |
| §3 table footnote attributed FY2023 price changes to the FY2025 10-K; they are only in the FY2023 10-K | Fixed: footnote amended. |
| §3 "Nothing about the factories changed between those columns except the price of what came out of them." — an unlabelled inference, and an overstatement (nodes moved to 1-gamma/G9, mix shifted to HBM and data center, cost per bit changed) | For the writer (REVISE 8): label as the writer's reading or soften. |
| §8 indicator 6 "management said RPO will be disclosed each quarter" — a paraphrase of "starting this May quarter" | Acceptable inference; suggest quoting (REVISE 9, minor). |
| Outlook §1 row 7 / business §7 table: "$30.13B" (cash and marketable investments, 10-Q Item 2) paired with "net cash $24,433M" (slides p.42, which includes $27M restricted cash); 30,128 − 5,722 = 24,406 | For the writer (REVISE 7, minor): make the basis consistent or round to "$24.4B". |
| All "(computed)" figures in §2, §3, §4, §7, §8 and outlook §1 | Re-derived; all correct (see §3 above). |
| Any figure with no tag | None found outside table cells whose source is given in the table footnote or "Where it comes from" column. |

## 6. Claims check (§9) and indicators (§8)

**Claims (outlook §5).** Nine claims (target 6–12). Each is one sentence, single direction, can fail, tied to a metric or event and a period, and carries its verbatim quote and page tag (all nine quotes verified exact). Headline guidance is 4 of 9 (revenue, gross margin, capex, free cash flow); the other five are fundamentals (price-increase moderation, SCA deposits, RPO, SCA count, Idaho date). Sharpenings are labelled in claims 2, 4 and 7. No claim is attributed to analysts or answers; "Not sharpenable without Q&A" is present and lists five specific gaps. Notes:

- Claim 3 checks two metrics (DRAM and NAND) in one sentence; both are observable in the same source and the claim fails if either does not moderate, so it is acceptable.
- Claim 5 turns "increase substantially" into "exceeds $18.3 billion" — a loosening, not a sharpening. Fine, but say so in the claim so a 1% rise is not silently graded ✅ (REVISE 10, minor).
- Claim 6 says the 10-K "balance sheet … shows contract liabilities or customer deposits". Contract liabilities are disclosed in the revenue note and sit inside "other noncurrent liabilities" (10-Q Note 14 L704), so a grader looking at the balance sheet face will find nothing; and "or" reads as either/or. REVISE 6.
- No disclosure checks are labelled as such; none are needed (claims 6 and 7 are management statements verified through the 10-K; both specify year-end).

**Indicators (business §8).** Seven (within 5–8). Each anchors to a recurring disclosure: 10-Q Item 2 price/bit direction; release headline non-GAAP gross margin; 10-Q Note 17 segment revenue; balance-sheet inventory (+ computed days); cash-flow-statement capex; Note 14 RPO and contract liabilities (a required recurring disclosure now that SCAs exist; management's "starting this May quarter" supports recurrence); balance-sheet debt and cash. Indicator 5 also tracks "the stated full-year plan", a management figure, but only alongside the recurring cash-flow line. Pass.

## 7. Length (§3 rule 7 method, the prescribed counter)

| File | Before reviewer fixes | After reviewer fixes | Target |
|---|---|---|---|
| business.md | 2,602 | **2,731** | 2,000–3,000 — in range |
| outlook.md | 1,012 | **1,042** | 800–1,200 — in range |

## 8. As-of discipline (cutoff 2026-06-25)

Grep of both drafts for any date after 2026-06-25 and for later-event vocabulary (Q4 FY2026 results, 10-K FY2026, July–September 2026) returns only the "Written 2026-09-07" header lines. Every source cited is dated on or before 2026-06-25 (latest: the 10-Q filed 2026-06-25; the remarks, release and slides dated 2026-06-24; the Björlin 8-K exhibit dated 2026-06-09). Forward-looking dates in the drafts (Dec. 9, 2026; 2027; 2028; 2030) are all management statements from the remarks or 10-Q. No sentence relies on knowledge of later events. Pass.

## 9. Verdict: REVISE

Everything below is local; no section needs restructuring. Items 1–6 are required; 7–10 are minor.

1. **business.md §6 item 6** — "Grants depend on milestones, with "up to all of certain incentives being clawed back" on failure, and the agreements restrict buybacks and special dividends for five years from December 9, 2024 [10-K FY2025, Item 1A; Note 20]." Wrong on buybacks: Note 20 (10-K-FY2025.txt:2421) restricts *special and one-time dividends* for five years, but permits share repurchases in the first two years up to specified amounts (to offset stock-compensation dilution) and does not restrict them in the final three years if financial and other conditions are met. Fix: "…the agreements bar special dividends for five years from December 9, 2024 and cap buybacks for the first two of those years, after which buybacks are free if certain financial conditions are met". This also reconciles with §7's "limited … until December 9, 2026".
2. **business.md §2 and §5, quarter-end vs post-quarter SCA figures** — "A new way of getting paid appeared this quarter: 16 "strategic customer agreements" (SCAs)…" and §5 "The 16 agreements are … Fourteen carry "a cumulative revenue at minimum price per our contracts of approximately $100 billion"…". The count of 16 and the ~$100 billion include agreements signed after May 28 (remarks p.7: "including ones executed after the end of FQ3"; 10-Q Note 14 L700: "including agreements executed subsequent to May 28, 2026"); at quarter end the 10-Q shows RPO of approximately $5 billion and $422 million of deposits (L704). Fix: add one clause in §2 or §5, e.g. "16 agreements as of the June 24 call, some signed after quarter end; the 10-Q's quarter-end RPO was approximately $5 billion [10-Q Q3 FY2026, Note 14]". Outlook §1 row 6 and claim 7 already keep this straight.
3. **outlook.md §3 Edge devices** — "PC and smartphone revenue "is expected to grow despite unit volume declines" [Q3 FY2026 remarks, p.5]." The source (prepared-remarks.txt:208) says "PC and smartphone **industry** revenue"; as written it reads as Micron's own PC/phone revenue. Fix: "PC and smartphone industry revenue "is expected to grow …"".
4. **business.md §5 and Glossary (Fab)** — "Leading-edge memory needs fabs costing tens of billions…" and "a leading-edge one costs tens of billions of dollars and takes years to build". No cached source gives a fab cost (rule 1: never invent a number). Fix: drop the figure, or anchor it to a sourced number, e.g. Micron's "approximately $27 billion" FY2026 capex plan [10-Q Q3 FY2026, Item 2] or the up-to-$6.1 billion CHIPS grant covering three fabs [10-K FY2025, Note 20].
5. **business.md §5** — "two of them (CXMT and YMTC) Chinese state-backed entrants added to the list only in FY2025 [10-K FY2025, Item 1; 10-K FY2023, Item 1]". The FY2023 10-K's competitor list (10-K-FY2023.txt:236) omits them, but the FY2024 10-K is not cached, so "only in FY2025" is unverifiable. Fix: "…entrants that were not on the FY2023 10-K's list".
6. **outlook.md §5 claim 6** — "The FY2026 10-K balance sheet (year-end column) shows contract liabilities or customer deposits under SCAs above the $422 million at May 28, 2026." Contract liabilities are disclosed in the revenue note, not as a balance-sheet line (10-Q Note 14 L704: "primarily included in other noncurrent liabilities"), and "or" reads as either/or. Fix: "The FY2026 10-K's revenue note discloses contract liabilities (customer deposits under SCAs) above $422 million at year-end."
7. *(minor)* **outlook.md §1 row 7 and business.md §7 table** — "$30.13B; net cash $24,433M": $30.13B (10-Q Item 2) excludes $27M restricted cash; the slides' $24,433M includes it (30,128 − 5,722 = 24,406). Fix: use "$30.16B of cash, investments and restricted cash [Q3 FY2026 slides, p.31]" with $24,433M, or write "net cash about $24.4B". Same for Q2 ($16.65B includes $26M restricted cash).
8. *(minor)* **business.md §3** — "Nothing about the factories changed between those columns except the price of what came out of them." Unlabelled inference and an overstatement (node transitions, HBM mix). Fix: "Our reading: the swing is almost entirely price, not cost" or similar.
9. *(minor)* **business.md §8 indicator 6** — "management said RPO will be disclosed each quarter". The remarks say "we are disclosing remaining performance obligations (RPO) starting this May quarter" (p.7). Fix: quote that phrase.
10. *(minor)* **outlook.md §5 claim 5** — "Q4 FY2026 adjusted free cash flow exceeds Q3's $18.3 billion." Management said "increase substantially"; the claim is looser. Fix: add "(any increase counts; management said "substantially")" so the grader knows the bar was lowered deliberately.
11. *(minor, optional)* **business.md §2** — "customers commit to set volumes, mostly within a price floor and ceiling". The 10-Q (L863) says most agreements are *either* fixed-price *or* floor/ceiling. Fix: "mostly at fixed prices or within a price floor and ceiling".

## Reviewer fixes applied (directly in the drafts)

business.md:
1. Line 4: added `8-K 2026-01-21` to the tag supporting "FY2026 ends September 3, 2026" (the date is not in the 10-K or 10-Q).
2. §1: "DRAM was 76% … NAND 23%" now labelled "(computed from the revenue-by-technology table)".
3. §1: inline gloss for "gross margin"; inline gloss for "CHIPS Act".
4. §3: inline glosses for "Depreciation", "operating margin", "G9 NAND", "cleanrooms".
5. §3 table footnote: FY2023 price-change ranges now attributed to [10-K FY2023, Item 7] (they are not in the FY2025 10-K).
6. §3: "70% of the Gujarat plant's cost" now "(50% from the central government plus 20% from the state, computed)".
7. §4: inline glosses for "equity" and "Receivables".
8. §5: inline glosses for "maintaining stable bit share", "managed NAND", "qualified".
9. §6 item 3: gloss for "yields". §6 item 7: quote corrected to begin at "constrain …" (source reads "could also constrain"); gloss for "contingencies note".
10. §7 table: gloss for "tender offers".
11. Glossary: added "Gross margin / operating margin", "SSD", "10-K / 10-Q".

outlook.md:
1. §1 row 6: expanded "RPO" and "SCA" on first use.
2. Line 20: "EPS (earnings per share)".
3. §3: parentheticals for "12-high", "sequentially", "HDD"; "ID1 (the first Idaho fab)", "ID2 (the second)".

No numbers, claims, tags other than the two noted, or section structure were changed. Pre-fix copies are in `/tmp/business.md.bak` and `/tmp/outlook.md.bak` (not in the repo). No git commands were run.

## Summary

- **Verdict:** REVISE — 6 required fixes (1 factual: CHIPS buyback restriction; 1 precision: quarter-end vs post-quarter SCA figures; 1 misattribution: "industry" revenue; 1 unsourced figure: fab cost; 1 unverifiable: "only in FY2025"; 1 claim wording: claim 6) plus 5 minor items.
- **Citation check:** 377 items; 372 pass (2 after reviewer tag/label fixes); 3 fail (1 fixed directly); 2 unverifiable.
- **Quotes:** all 50 quoted strings in outlook.md and 50 of 51 in business.md verbatim; the one mismatch fixed.
- **Skeleton, header, §8 lock marker, Sources tables, as-of discipline:** all pass.
- **Length (prescribed counter):** business.md 2,731; outlook.md 1,042.

---

## Cycle 2 (review cycle 2 of 2) — verification of the 11 REVISE items

_Re-read both drafts from disk on 2026-09-07 after the writer's second pass. Each new wording was checked against the cited cached file and line, not against the writer's description._

| # | Item | New wording verified against file:line | Result |
|---|---|---|---|
| 1 | CHIPS restrictions (business §6 item 6; §7) | §6 now: special and one-time dividends restricted five years from Dec 9, 2024; buybacks capped "at specified amounts during the first two of those years"; freed in the final three only "if certain financial and other conditions are satisfied". 10-K-FY2025.txt:2421 says exactly this (dividends: "five-year period following … December 9, 2024"; repurchases "permitted during the first two years … up to amounts specified"; "not restricted during the final three years … if certain financial and other conditions are satisfied" — quote verbatim). §7 "capped … until December 9, 2026, two years after signing" = Dec 9, 2024 + 2 years. Item 1A tag also holds: 10-K-FY2025.txt:1103 cites "restrictions applicable under our CHIPS Act direct funding agreements" and points to Note 20; clawback quote at 741. | PASS |
| 2 | Quarter-end vs post-quarter SCA figures (business §2, §5) | §2 new sentence: "The 16 signed by the June 24 call include agreements executed after quarter-end; at May 28, 2026 the 10-Q recorded RPO of "approximately $5 billion" and $422 million of deposits [Q3 FY2026 remarks, p.1; 10-Q Q3 FY2026, Note 14]". 16 at prepared-remarks.txt:40–41 (p.1); post-quarter signings at 10-Q-FY2026-Q3.txt:700 ("including agreements executed subsequent to May 28, 2026"); "approximately $5 billion" verbatim at 10-Q:704, which also says "$422 million has been recognized as contract liabilities. Contract liabilities primarily consisted of customer deposits" — so "deposits" (§2), "contract liabilities (customer deposits)" (§8, outlook §1) and "contract liabilities" (outlook §3) are consistent. §5 parenthetical "(a figure that includes agreements signed after May 28, 2026; quarter-end RPO was about $5 billion)" now tagged [remarks p.3; p.7; 10-Q Note 14]; remarks p.7 L312–313 confirms "including ones executed after the end of FQ3". | PASS |
| 3 | outlook §3 industry revenue | "For the industry as a whole, "PC and smartphone industry revenue is expected to grow despite unit volume declines"" — prepared-remarks.txt:208 (p.5), verbatim. | PASS |
| 4 | "tens of billions" removed; §5 moat sentence tag | `grep "tens of billions"` = 0 hits in both drafts (glossary Fab line now "a new one takes years to build"). §5 "fabs that take years to build, over 60,000 granted patents and decades of process know-how [10-K FY2025, Item 1; Item 2; 10-K FY2023, Item 1]": 60,000 patents at 10-K-FY2025.txt:323 (Item 1); years-to-build supported by Item 2 L1170 (ground broken September 2022, construction from October 2023, first output second half of calendar 2027). "decades of process know-how" is a qualitative phrase with no direct source line; it is not a number, so acceptable, but the writer may prefer to drop "decades". | PASS |
| 5 | CXMT / YMTC "were not on the FY2023 10-K's list" | 10-K-FY2023.txt:236 lists Kioxia, Samsung, SK hynix and Western Digital only; CXMT and YMTC appear at L238 in a separate sentence about Chinese state investment, not in the competitor list. FY2025 list at 10-K-FY2025.txt:271 names six including both. The cycle-1 UNVERIFIABLE is resolved. | PASS |
| 6 | outlook claim 6 | "(Disclosure check, not a management claim.) The contract-liabilities figure in the FY2026 10-K's revenue note, year-end column, is above the $422 million reported at May 28, 2026." Labelled as a disclosure check; single direction ("is above"); names the note and the year-end column; the either/or is gone; quote and tag unchanged and verbatim (prepared-remarks.txt:323). | PASS |
| 7 | Net-cash basis | slides.txt:574 (p.31): "Cash, marketable investments, and restricted cash (GAAP)" 30,155 (FQ3) and 16,653 (FQ2). slides.txt:802–805 (p.42): restricted cash 27 / 26; net cash 24,433 / 6,511. 30,155 rounds to $30.16B (business §7 table) and $30.2B (indicator 7); 30,155 − 5,722 = 24,433 ("$24.4B after $5.7B of debt, on the same basis"). Outlook §1 row 7 now "$5,722M; $30,155M; net cash $24,433M" and Q2 "$10,142M (computed: 585 + 9,557, press-release-Q2-FY2026.txt:159, 162); $16,653M; net cash $6,511M", with the basis stated in the row label. | PASS |
| 8 | §3 inference label | "Our inference: the factories, nodes and product mix changed far less between those columns than the price of what came out of them." Labelled and no longer overstated. | PASS |
| 9 | Indicator 6 quote | "disclosing remaining performance obligations (RPO) starting this May quarter" [Q3 FY2026 remarks, p.7] — prepared-remarks.txt:310–311, verbatim across the line break ("we / are disclosing …"). | PASS |
| 10 | Claim 5 label | "(our sharpening of "increase substantially", not management's number)" present; quote unchanged and verbatim (prepared-remarks.txt:469). Strictly it loosens rather than sharpens management's phrase, but the reader is told the threshold is ours, which is what §9 requires. | PASS |
| 11 | §2 SCA pricing | "mostly at fixed prices or within a floor and ceiling" matches 10-Q-FY2026-Q3.txt:700 and 863: "Pricing for most agreements is either fixed, or is subject to minimum and maximum pricing." | PASS |

**Other checks**

- Cycle-1 direct fixes: all 22 business.md edits and all 6 outlook.md edits are still present (each grepped, one occurrence apiece).
- New sentences and numbers: every new sentence carries a tag except the labelled "Our inference" sentence (an inference, not a fact); new figures ($30.16B, $30.2B, $27M, $30,155M, $16,653M, "two years") all verified above. Full change set inspected (diff against the pre-cycle-1 copy); nothing changed beyond the 11 items and the reviewer's cycle-1 fixes.
- Cycle-1 UNVERIFIABLE items: both resolved (item 4 removed the unsourced fab cost; item 5 reworded to what the FY2023 10-K shows).
- Cycle-2 direct fix: business.md §7 table, "restricted cash" glossed as "cash set aside for a specific purpose" (table cell; word count unaffected). Recorded here; no other edits.
- Length (prescribed counter): business.md **2,821**; outlook.md **1,061** — both match the writer's figures and are within 2,000–3,000 and 800–1,200.
- As-of discipline: unchanged; no post-2026-06-25 material introduced.

**Final verdict: PASS.** No open items. Optional polish only: drop "decades of" in §5 if the writer wants every qualifier sourced.

