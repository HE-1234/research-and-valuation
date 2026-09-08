# McDonald's Corporation (MCD) — Reviewer report, 2026-Q2 (cycle 1)

_Reviewed 2026-09-08 against `companies/MCD/sources/2026-Q2/` only (cached full texts; `notes-*.md` not used as evidence). As-of cutoff 2026-08-07; nothing dated later was consulted. Line numbers (l.N) refer to the cached `.txt` files. Printed-page maps used (a page number on its own line closes that page): `press-release.txt` p.1 = l.1–44, p.2 = 45–83, p.3 = 84–103, p.4 = 104–133, p.5 = 134–166, p.6 = 167–199. `press-release-supplement.txt` p.1 = 1–49, p.2 = 50–92, p.3 = 93–112, p.4 = 113–143, p.5 = 144–178, p.6 = 179–220, p.7 = 221–275, p.8 = 276–303, p.9 = 304–344, p.10 = 345–368, p.11 = 369–388, p.12 = 389–420, p.13 = 421–449. `press-release-2026-Q1.txt` p.1 = 1–44, p.2 = 45–88, p.3 = 89–118, p.4 = 119–151. `press-release-supplement-2026-Q1.txt` p.3 = 87–119, p.4 = 120–162, p.5 = 163–206, p.6 = 207–260, p.8 = 286–305, p.9 = 306–337, p.10 = 338–366. Word counts by `python3 -P /tmp/mcd-orch/wc_prose.py` from cwd `/home/ubuntu`. Scratch scripts in `/tmp/mcd-orch/reviewer/` (`find.py` normalising full-line search, `quotes.py` quote sweep, `tags.py` tag extraction, `apply_fixes.py`)._

**Verdict: PASS.** Every cell of every table in business.md §2, §3 and §4 and in outlook §1 verifies against the cached source text, including the "not disclosed" cell and every "(computed)" cell, which were re-derived. Every verbatim quote in outlook §2, §4 and §5 matches the transcript, supplement or 10-Q word for word (103 quoted strings swept programmatically, 0 misses). No invented number, no call-only number presented as anything but a spoken statement, no claim that cannot fail. What I fixed directly: three tag-precision slips (a by-segment restaurant count tagged to the wrong note; SG&A totals tagged to an income statement that splits them; a segment-total revenue tagged to the MD&A revenues table), one mislabel ("computed" on a figure the 10-K states), one wording slip in outlook §4 about what changed since Q1, a missing 10-Q tag on claim 5, one unlabelled judgement, and eight glosses. Nothing structural or factual remains for the writer; the only open items are judgement calls for the owner (§13).

---

## 1. Skeleton compliance

**business.md**

| Requirement (§6) | Status |
|---|---|
| `# McDonald's Corporation — The Business` | OK, exact (l.1) |
| `_As of Q2 2026. Written 2026-09-08._` | OK, exact (l.2); fiscal = calendar, no parenthetical needed |
| §1 What they do, with a history paragraph | OK (history l.10) |
| §2 How the money comes in, 5-year segment table | OK: revenue-by-stream table FY2021–FY2025 (l.14–24), restaurant-count table (l.32–40), segment revenue and operating income table (l.48–56) |
| §3 The economics: revenue / margin / operating margin / capex / capex-to-revenue, 5 years | OK (l.66–74); no gross margin exists, the two restaurant margins stand in and the text says so (l.64) |
| §4 How profitable, really, 5-year table | OK (l.84–95): OCF, capex, FCF, conversion, net income, dividends, DPS, buybacks, shares, ROIC |
| §5 Why customers don't leave | OK, diners and franchisees separately, each with a weakening sign |
| §6 What could break it, ranked, concentration | OK, six ranked scenarios, each with an early warning; concentration paragraph l.127 |
| §7 Who runs it and what they do with the cash | OK (people, pay, cash) |
| §8 Indicators (5–8; name / why / where) | OK, 7 indicators, each with a recurring location |
| `_Proposed — owner to review and lock._` | OK (l.139) |
| Glossary, one sentence each | OK, 5 entries (Systemwide sales, Comparable sales, Conventional franchise, Developmental licensee, Affiliate), each one sentence, each unavoidable |
| Sources list maps every tag prefix | OK. Prefixes used (from `tags.py`): 10-K FY2025 / FY2024 / FY2023 / FY2022, 10-Q Q2 2026, DEF 14A 2026, 8-K 2026-05-22, 8-K 2026-08-04, Leadership release 2026-08-04, Q2 2026 release, Q2 2026 supplement, Q2 2026 call — all 12 listed with filing dates matching MANIFEST (10-K FY2025 2026-02-24; FY2024 2025-02-25; FY2023 2024-02-22; FY2022 2023-02-24; 10-Q 2026-08-07; DEF 14A 2026-04-07 for the 2026-05-20 meeting; 8-Ks 05-22 and 08-04; release, supplement, call 2026-08-04). The call entry states tier 3, posting date 2026-08-11, and that l.N is the line number of `transcript.txt` |
| Heading order | OK |

**outlook.md**

| Requirement (§7) | Status |
|---|---|
| `# McDonald's Corporation — Outlook as of Q2 2026` | OK, exact |
| `_Transcript source tier: third-party (The Motley Fool). Written 2026-09-08._` | OK, exact; matches MANIFEST tier 3 |
| §1 one row per indicator; this quarter / last quarter / expected | OK, 7 rows in the same order as business.md §8; header note says the set is proposed |
| §2 What management says | OK |
| §3 Growth engines (what / how big / claim / working-if) | OK, seven engines, each with a "Working if" line |
| §4 Guidance, verbatim | OK, two tables (see §10(h) below) |
| §5 Claims | OK, 12 claims |
| §6 Tone shift | Correctly omitted (first run) |
| Sources | OK: Q2 call, Q2 release, Q2 supplement, Q1 release, Q1 supplement, 10-Q Outlook, 10-K FY2025 — all 7 prefixes used are listed; call entry states line-number citation |

---

## 2. Rubric (§14)

| # | Question | Answer | Reasoning |
|---|---|---|---|
| 1 | Two sentences on what they do and who pays | Yes | §1 l.6: 46,028 restaurants, about 95% run by franchisees who pay rent, royalties and fees; "the customer who pays McDonald's is mostly the franchisee, not the diner". |
| 2 | What would kill it and the early warning | Yes | §6 ranks six scenarios (U.S. value/traffic, franchisee economics or legal status, consumers leaving fast food, geopolitics, food safety, tax), each with an early-warning line and an exposure figure. |
| 3 | Why margins are what they are; does cost scale with usage | Yes | §3 l.64: franchised margin is rent plus royalty against property cost that "barely moves when the franchisee sells more" (84%); company-run margin pays food, crew and occupancy per burger (14.7%); franchised restaurants are ~90% of margin dollars. §3 l.80: franchisees fund equipment and remodels, McDonald's capex is mostly new sites. |
| 4 | Predict next quarter's scorecard from §5 alone | Yes | 12 claims, each tied to a number, a printed line or a dated event. |
| 5 | Nothing required outside knowledge | Yes, after glosses | Terms a 16-year-old would not know (royalties, ROIC, consolidated markets, impairment, transfer pricing, unrecognized tax benefits, EPS, TSR modifier, tailwind, adjusted EPS) glossed directly (§5 below). |

Franchise-model plainness, as asked: most restaurants franchised (l.6, table l.39), rent and royalties collected on franchisee sales (l.6, l.8, l.28), why that makes margins high and capital needs modest (l.64, l.78, l.80), how company-operated restaurants differ and why they exist (l.60, l.64). All present in plain words.

---

## 3. Citation spot-check

Legend: PASS = the tagged source contains the number or text at the line shown. Computed cells re-derived from sourced inputs.

### 3(a) business.md §2 revenue table (l.14–24), every cell

Inputs: `10-K-FY2023.txt` l.2439–2445 (rents 8,381.1 / royalties 4,645.1 / initial fees 59.2 / franchised revenues 13,085.4 for 2021), l.1623 (company-operated sales 9,787.4), l.504 (MD&A: other revenues 351), l.1629 (total 23,222.9); `10-K-FY2024.txt` l.2475–2481 (9,046 / 5,006 / 54 / 14,106), l.1610 (8,748), l.1612 (328), l.1614 (23,183); `10-K-FY2025.txt` l.2399–2405 (9,840 / 10,017 / 10,442; 5,531 / 5,606 / 6,018; 66 / 92 / 88; 15,437 / 15,715 / 16,548), l.1548 (9,742 / 9,782 / 9,690), l.1550 (316 / 423 / 647), l.1552 (25,494 / 25,920 / 26,885). Systemwide sales: `10-K-FY2022` l.376 ($118.2B), `10-K-FY2023` l.384 ($129.5B), `10-K-FY2024` l.363 ($130.7B), `10-K-FY2025` l.357 ($139.4B). Franchised sales: `10-K-FY2023` l.741 (2021 total 102,675; 2022 109,473; 2023 119,750), `10-K-FY2025` l.678 (2024 120,933; 2025 129,675).

| Row | Result |
|---|---|
| Rents 8,381 / 9,046 / 9,840 / 10,017 / 10,442 | PASS ×5 |
| Royalties 4,645 / 5,006 / 5,531 / 5,606 / 6,018 | PASS ×5 |
| Initial fees 59 / 54 / 66 / 92 / 88 | PASS ×5 |
| Franchised revenues 13,085 / 14,106 / 15,437 / 15,715 / 16,548 | PASS ×5 |
| Company-operated sales 9,787 / 8,748 / 9,742 / 9,782 / 9,690 | PASS ×5 |
| Other revenues 351 / 328 / 316 / 423 / 647 | PASS ×5. Note: FY2021 351 is the FY2023 10-K MD&A figure (l.504) as tagged; the statement line (l.1627) reads 350.1. FY2022 328 is the FY2024 statement (l.1612) as tagged; that 10-K's MD&A says 329. Each cell matches its own tag; the footnote at l.26 already warns of $1 million differences |
| Total revenues 23,223 / 23,183 / 25,494 / 25,920 / 26,885 | PASS ×5 |
| Systemwide sales 112.5 (computed) / 118.2 / 129.5 / 130.7 / 139.4 | 102,675 + 9,787 = 112,462 → 112.5; others stated. PASS ×5 |
| Franchised revenues / franchised sales (computed) 12.7 / 12.9 / 12.9 / 13.0 / 12.8% | 13,085/102,675 = 12.74; 14,106/109,473 = 12.89; 15,437/119,750 = 12.89; 15,715/120,933 = 13.00; 16,548/129,675 = 12.76. PASS ×5 |

45/45 PASS.

### 3(b) business.md §2 restaurant-count table (l.32–40), every cell

Inputs: `10-K-FY2023` l.2025–2035 (2021: 21,607 / 7,913 / 7,775 / company-operated 2,736 / 40,031); `10-K-FY2024` l.2012–2022 (2022: 21,720 / 8,229 / 8,220 / 2,106 / 40,275); `10-K-FY2025` l.1944–1954 (2023–2025: 21,818 / 22,077 / 22,570; 8,684 / 9,247 / 9,675; 9,178 / 10,108 / 11,072; 2,142 / 2,045 / 2,039; 41,822 / 43,477 / 45,356); `10-Q` l.650–660 (22,722 / 9,833 / 11,461 / 2,012 / 46,028). Openings and closings: `10-K-FY2022` l.999 (2021: 1,494 / 661; 2022: 1,576 / 1,332; 855 Russia), `10-K-FY2023` l.1004 (2023: 2,067 / 520), `10-K-FY2025` l.907 (2024: 2,116 / 461; 2025: 2,276 / 396).

| Row | Result |
|---|---|
| Five count rows × six periods | PASS ×30 |
| Franchised share (computed) 93.2 / 94.8 / 94.9 / 95.3 / 95.5 / 95.6% | 37,295/40,031 = 93.17; 38,169/40,275 = 94.77; 39,680/41,822 = 94.88; 41,432/43,477 = 95.30; 43,317/45,356 = 95.50; 44,016/46,028 = 95.63. PASS ×6 |
| Opened / closed 1,494/661; 1,576/1,332; 2,067/520; 2,116/461; 2,276/396 | PASS ×10 |
| 6/30/2026 "not disclosed" | The 10-Q Restaurant Information note (l.644–660) and supplement p.12–13 give counts and year-over-year changes only, no openings or closings. PASS |

47/47 PASS.

### 3(c) business.md §2 segment table (l.48–56), every cell

Inputs: `10-K-FY2023` l.2357–2371 (2021: 8,865.0 / 12,219.8 / 2,138.1; 4,754.7 / 5,130.6 / 470.7; 10,356.0); `10-K-FY2024` l.2357–2403 (2022: 9,588 / 11,297 / 2,297; 5,136 / 3,926 / 309; 9,371); `10-K-FY2025` l.2281–2327 (2023–2025: 10,568 / 10,631 / 10,825; 12,382 / 12,628 / 13,633; 2,543 / 2,661 / 2,427; 5,694 / 5,733 / 5,808; 5,831 / 5,946 / 6,382; 121 / 33 / 203; 11,647 / 11,712 / 12,393).

35/35 PASS. Footnote: the $1,281M Russia charge is in `10-K-FY2022` l.557 and l.871; the FY2024 10-K's segment table puts 2022 impairment and other charges of 1,390 in International Operated Markets (l.2391), consistent with the footnote.

### 3(d) business.md §3 table (l.66–74), every cell

Inputs: franchised margins `10-K-FY2023` l.565 (10,750), `10-K-FY2024` l.542 (11,756), `10-K-FY2025` l.512 (12,962 / 13,178 / 13,930); company-operated margins `10-K-FY2023` l.563 (1,740), `10-K-FY2024` l.544 (1,368), `10-K-FY2025` l.514 (1,517 / 1,447 / 1,422); SG&A `10-K-FY2023` l.567 (2,708), `10-K-FY2024` l.546 (2,862), `10-K-FY2025` l.516 (2,817 / 2,858 / 3,039); operating margin `10-K-FY2022` l.891 (44.6 / 40.4), `10-K-FY2025` l.827 (45.7 / 45.2 / 46.1); capex `10-K-FY2023` l.1873 (2,040.0), `10-K-FY2024` l.1858 (1,899), `10-K-FY2025` l.1792 (2,357 / 2,775 / 3,365).

| Row | Re-derived | Result |
|---|---|---|
| Total revenues | as 3(a) | PASS ×5 |
| Franchised margin $ / % 10,750 / 82.2; 11,756 / 83.3; 12,962 / 84.0; 13,178 / 83.9; 13,930 / 84.2 | 82.15 / 83.34 / 83.97 / 83.86 / 84.18% | PASS ×10 |
| Company-operated margin $ / % 1,740 / 17.8; 1,368 / 15.6; 1,517 / 15.6; 1,447 / 14.8; 1,422 / 14.7 | 17.78 / 15.64 / 15.57 / 14.79 / 14.67% | PASS ×10 (FY2023 10-K prints 2023 as 1,518; the draft uses the FY2025 10-K's 1,517 and tags it there) |
| SG&A 2,708 / 2,862 / 2,817 / 2,858 / 3,039 | stated in each MD&A table | PASS ×5. Tag precision: the income statements split SG&A into depreciation and other (FY2025 l.1570–1572: 457 + 2,583 = 3,040; 447 + 2,412 = 2,859; FY2024 l.1634–1636: 370 + 2,492 = 2,862), so the exact totals live in MD&A (Consolidated Operating Results). Tags corrected (direct fix 3) |
| Operating margin 44.6 / 40.4 / 45.7 / 45.2 / 46.1% | stated | PASS ×5 |
| Capex 2,040 / 1,899 / 2,357 / 2,775 / 3,365 | stated | PASS ×5 |
| Capex / revenue (computed) 8.8 / 8.2 / 9.2 / 10.7 / 12.5% | 8.78 / 8.19 / 9.25 / 10.71 / 12.52% | PASS ×5 |

45/45 PASS (one tag group corrected).

### 3(e) business.md §4 table (l.84–95), every cell

Inputs: `10-K-FY2023` l.1869 (OCF 9,141.5), l.1841 (net income 7,545.2), l.1895 (dividends 3,918.6), l.1893 (buybacks 845.5), l.1048 (DPS 5.25), l.1046 (shares 745); `10-K-FY2024` l.1854 (7,387), l.1826 (6,177), l.1882 (4,168), l.1880 (3,896), l.1003 (5.66), l.1001 (731); `10-K-FY2025` l.1788 (9,612 / 9,447 / 10,551), l.1760 (8,469 / 8,223 / 8,563), l.1816 (4,533 / 4,870 / 5,115), l.1814 (3,054 / 2,824 / 2,056), l.949 (6.23 / 6.78 / 7.17), l.947 (723 / 715 / 711); conversion `10-K-FY2022` l.987 (94% 2021, 89% 2022), `10-K-FY2024` l.949 (86% 2023), `10-K-FY2025` l.895 (81% 2024, 84% 2025); ROIC `10-K-FY2022` l.1064 (21.5 / 22.6), `10-K-FY2025` l.970 (25.2 / 21.8 / 20.3).

| Row | Result |
|---|---|
| Cash provided by operations 9,142 / 7,387 / 9,612 / 9,447 / 10,551 | PASS ×5 |
| Capex | PASS ×5 |
| FCF (computed) 7,102 / 5,488 / 7,255 / 6,672 / 7,186 | 9,142−2,040; 7,387−1,899; 9,612−2,357; 9,447−2,775; 10,551−3,365. PASS ×5 |
| Conversion (as stated) 94 / 89 / 86 / 81 / 84% | PASS ×5 |
| Net income 7,545 / 6,177 / 8,469 / 8,223 / 8,563 | PASS ×5 |
| Dividends paid 3,919 / 4,168 / 4,533 / 4,870 / 5,115 | PASS ×5 |
| DPS 5.25 / 5.66 / 6.23 / 6.78 / 7.17 | PASS ×5 |
| Buybacks 846 / 3,896 / 3,054 / 2,824 / 2,056 | PASS ×5 |
| Shares 745 / 731 / 723 / 715 / 711 | PASS ×5 |
| ROIC 21.5 / 22.6 / 25.2 / 21.8 / 20.3% | PASS ×5; the footnote's "formula sits in an exhibit that was not fetched" matches l.970 ("Refer to the reconciliation in Exhibit 99.1") and MANIFEST |

50/50 PASS.

### 3(f) business.md §7

No table in §7; its figures are checked as prose in 3(h) (#34–#43).

### 3(g) outlook.md §1 indicator table (l.10–16), every cell

| Row | Source | Result |
|---|---|---|
| 1. Comps Q2 1.3%; 0.8 / 1.5 / 1.9 — Q1 3.8%; 3.9 / 3.9 / 3.4 | `press-release` l.51–54 (p.2); `press-release-2026-Q1` l.51–54 (p.2) | PASS ×8. "No guidance" correct: Q1 Outlook (Q1 supplement l.286–304, p.8) has no comps line. CFO recollection of April "slightly negative" at `transcript` l.34, and the cell labels it as said on the Q2 call |
| 2. Systemwide constant-currency Q2 4%; 2 / 4 / 7; reported 5% — Q1 6%; 5 / 6 / 8; 11% | `press-release-supplement` l.188–191 (p.6); Q1 supplement l.140–143 (p.4) | PASS ×10; guidance quote at Q1 supplement l.290 (p.8) |
| 3. Restaurants 46,028; +329; 2,012 — 45,699; +343; 2,027 | Q2 supplement l.446–449 (p.13); Q1 supplement l.334 (p.9), l.363 (p.10); `10-K-FY2025` l.1954 (45,356). 46,028−45,699 = 329; 45,699−45,356 = 343 | PASS ×6; guidance quotes at Q1 supplement l.300 |
| 4. Franchised margin 3,713; 84.5% — 3,331; 83.1% | Q2 supplement l.238 (p.7), l.129 (4,393): 84.52%; Q1 supplement l.184 (p.5), l.101 (4,007): 83.13% | PASS ×4 |
| 5. Company-operated 387; 15.3%; U.S. 11.6% — 285; 12.3%; U.S. 8.1% | Q2 l.243, l.134 (2,525): 15.33%; l.240, l.131 (91/784): 11.61%; Q1 l.189, l.108 (2,317): 12.30%; l.186, l.103 (59/729): 8.09% | PASS ×6 |
| 6. Operating margin 47.0% (computed); SG&A 2.2% — 45.3%; 2.2% | `press-release` l.145, l.155 (p.5): 3,338/7,099 = 47.02%; Q2 supplement l.281 (p.8); Q1 supplement l.239 (p.6), l.199 (p.5) | PASS ×4; guidance quotes Q1 supplement l.292, l.294 |
| 7. Loyalty $40B, up over 20%; nearly 220M, up 13% — over $38B; users not given | `press-release` l.14 (p.1); Q1 release l.16 (p.1: trailing "over $38 billion", no user count) | PASS ×5; 250 million and $45.0 billion by end-2027 at `10-K-FY2025` l.391 |

43/43 PASS.

### 3(h) Verbatim quotes, outlook §2, §4, §5 (curly quotes normalised)

Programmatic sweep (`quotes.py`): every double-quoted string of 12+ characters in outlook.md (63 captures, of which 5 are regex artefacts between adjacent fragments) and business.md (45) tested as a substring of the normalised cached texts. Result: 58/58 real outlook quotes and 45/45 business quotes found. Hand-checked lines:

| Quote (start) | Tag | Found | Result |
|---|---|---|---|
| "We've grown systemwide sales roughly $40 billion and operating income by over $3 billion" | call l.24 | l.24 | PASS |
| "The McDonald's brand remains one of one in our industry" | call l.25 | l.25 | PASS |
| "We don't have a strategy problem. We simply didn't execute" | call l.29 | l.29 (sentence continues "at the level we needed to in the second quarter"; the draft stops mid-sentence without an ellipsis) | PASS on wording; cosmetic |
| "3 buckets"; "overwhelmed by too many deployments"; "didn't deliver against expectations" | call l.29, l.30 | l.29, l.29, l.30 | PASS ×3 |
| "We have been consistent. We will not get beaten on value" | call l.36 | l.36 | PASS |
| "earn the right to be more customers' first choice"; "meaningfully self-funded"; "not a remodel program" | call l.57, l.49, l.173 | exact | PASS ×3 |
| §4 table 1, seven Outlook bullets | 10-Q Outlook | `10-Q` l.1793–1805; identical text at supplement l.374–386 (p.11) | PASS ×7, complete bullets |
| Currency "$0.15 ... $0.20 to $0.30 tailwind" | call l.42 | l.42 | PASS |
| G&A two sentences | call l.43 | l.43 | PASS ×2 |
| "comps in the U.S. were slightly negative in July." | call l.94 | l.94 | PASS |
| "we certainly expect in both segments ... 1.5% and 1.9% comps in Q2, respectively." | call l.95 | l.95 | PASS |
| Marketing "nothing in Q3 ... 2027." | call l.87 | l.87 | PASS |
| U.S. actions, five fragments | call l.35, l.36, l.88, l.51 | l.35, l.36, l.36, l.88, l.51 | PASS ×5 |
| Beverages "Australia who has launched in mid-July"; "Red Bull Energizers in the U.S. in the coming weeks" | call l.203, l.51 | exact | PASS ×2 |
| Development "50,000 restaurants globally in 2028"; "about 2,600 gross restaurants by the end of this year" | call l.44, l.45 | exact | PASS ×2 |
| Investor Day September 23 | call l.57 | l.57 | PASS |
| Claims 1–12 quotes | as tagged | l.95; l.95; l.94; `10-Q` l.1803; l.44; l.43; l.42; `press-release` l.14; l.51; l.57; l.44; l.44 | PASS ×12 |

### 3(i) Tagged prose sentences, business.md (43 checked)

| # | Sentence / figure | Tag | Found | Result |
|---|---|---|---|---|
| 1 | 46,028 restaurants in 114 countries | Q2 supplement p.12; 10-K Products | supplement l.418–419; `10-K-FY2025` l.289–295 | PASS |
| 2 | About 95% franchised; franchisees control employment, pricing | 10-Q MD&A; 10-K Description of the Business | `10-Q` l.1007; `10-K-FY2025` l.193 | PASS |
| 3 | "The Company is primarily a franchisor" | 10-K Description of the Business | l.193 | PASS |
| 4 | Systemwide sales $139.4B; revenue $26.9B; comps definition; growth = comps + units | 10-K MD&A | l.357, l.355, l.323–331 (thirteen months), l.331 | PASS ×4 |
| 5 | 70th anniversary 2025; Founder's Day Oct 5 | DEF 14A Chairman's Letter; call l.52 | `DEF14A` l.57; `transcript` l.52 | PASS ×2 |
| 6 | Accelerating the Arches 2020, refreshed 2023; NEXT June 2026 "to be more customers' first choice" | 10-Q MD&A | l.1043, l.1045, l.1065 | PASS ×3 |
| 7 | Russia: 855 restaurants, $1,281M | 10-K FY2023 MD&A; FY2022 MD&A | `10-K-FY2023` l.1004, l.587; `10-K-FY2022` l.999, l.557 | PASS ×2 |
| 8 | Conventional franchise quotes; 20 years; "maintains control of the underlying real estate" | 10-K Description (Conventional Franchise); Note: Franchise Arrangements | l.201, l.207; l.2389 | PASS ×4 |
| 9 | Rent rate, royalty rate, initial fee "not disclosed in any filing" | 10-K Note: Franchise Arrangements | l.2387–2427 give no rates; regex search of the FY2025 10-K for a royalty or rent percentage found none | PASS (not-disclosed claim holds) |
| 10 | Rents 63% of franchised revenues (computed) | Note: Franchise Arrangements | 10,442/16,548 = 63.1% | PASS |
| 11 | Developmental license quotes; affiliates "primarily China and Japan" (48% and 35%) | Description (Developmental License or Affiliate); Note: Equity Method Investments | l.211, l.213; l.2621–2623 (Grand Foods Holding 48%, McDonald's Japan 35%) | PASS ×3 |
| 12 | "over 75 countries"; licensed segment 99% franchised; IOM markets list | Note: Segment and Geographic Information; Description of the Business | l.2271 (99%), l.2269 (Australia, Canada, France, Germany, Italy, Poland, Spain, U.K.); l.189 | PASS ×3 |
| 13 | U.S. 13,128 conventional / 641 company-run; licensed 9,642 / 11,461 / 238; China 8,114; Japan 3,038 | Q2 supplement p.12, p.13 | l.406–407, l.425–426, l.435–438 | PASS ×6 |
| 14 | Take by structure 14.2% / 17.2% / 5.4% (computed) | MD&A (Revenues), (Franchised Sales) | 7,371/51,946 = 14.19; 7,279/42,440 = 17.15; 1,898/35,289 = 5.38 (l.592–596, l.672–676) | PASS ×3 |
| 15 | Licensed markets 46% of restaurants, 11.5% of franchised revenues | (as tagged: Note: Summary of Significant Accounting Policies) | 20,805/45,356 = 45.9% but the by-segment count is at MD&A l.917 ("Systemwide restaurants at year end"), not in the note (which is by type, l.1944–1954); 1,898/16,548 = 11.47% | PASS on numbers; tag corrected (direct fix 2) |
| 16 | IOM 90% franchised; licensed segment carries Corporate | 10-Q Note: Segment Information | l.897, l.899, l.903 | PASS ×2 |
| 17 | Company-run restaurants for a "credible franchisor" | 10-K Description | l.195 | PASS |
| 18 | Other revenues: technology fees "not designed to generate margins", brand licensing; +53% / +66% | Note: Summary of Significant Accounting Policies; MD&A (Consolidated Operating Results) | l.2000; l.457 (53), l.467 (66) | PASS ×3 |
| 19 | Franchised margin 84% (computed); occupancy = lease expense and depreciation; "approximately 90% of restaurant margin dollars" | MD&A (Restaurant Margins) | 13,930/16,548 = 84.2%; l.692; l.736 | PASS ×3 |
| 20 | Food & paper $3.0B, payroll $2.9B, occupancy $2.4B against $9.7B; 14.7%; "ongoing inflationary cost pressures" | Consolidated Statement of Income; MD&A (Restaurant Margins) | l.1560–1564 (3,006 / 2,905 / 2,358); l.1548; l.738 | PASS ×5 |
| 21 | Where the money goes: $8.3B / $2.6B / $0.6B / $3.0B / $12.4B / 46.1%; overhead 2.2% of Systemwide sales 2025 (computed) and H1 2026 (stated) | Statement of Income; MD&A (Operating Income); 10-Q MD&A | 3,006+2,905+2,358 = 8,269; l.1556 (2,618); l.1566 (564); l.516 (3,039); l.1578; l.827; 3,039/139,365 = 2.18%; `10-Q` l.1641 | PASS ×7 |
| 22 | Franchisees "responsible for reinvesting capital"; remodels "every 10 years" | Description (Conventional Franchise); call l.174 | l.203; `transcript` l.174 | PASS ×2 |
| 23 | Capex $3.4B "mainly allocated to new restaurant openings ..."; 2022–2023 "approximately 50% to each"; dollar split not disclosed (chart is an image) | MD&A (Restaurant Development and Capital Expenditures); 10-K FY2023 same | `10-K-FY2025` l.367 (highlights bullet) and l.927–929 (section; chart title only); `10-K-FY2023` l.394, l.1024–1028 | PASS ×3; consistent with MANIFEST's image note |
| 24 | 56% of land, 80% of buildings; $28.2B net P&E; $14.8B lease liabilities | MD&A (Restaurant Development); Note: Property and Equipment; Note: Leasing Arrangements | l.935; l.2383 (28,241); l.2508 (present value of lease liability 14,840) | PASS ×3 |
| 25 | FCF $7.2B, 84%; "a decrease of $510 million or 8%" vs "an 8% increase"; statements 7,186 vs 6,672 | MD&A (Cash Flows); MD&A (2025 Financial Performance) | l.895; l.369; 10,551−3,365 and 9,447−2,775 | PASS ×4 (see §10(d)) |
| 26 | Debt $40.0B, 97% fixed-rate, BBB+ / Baa1, interest $1,582M ≈ 13% of operating income | MD&A (Financing and Market Risk); Statement of Income | l.974; l.980–981 ("Fixed-rate debt as a percent of total debt" / "97 %"); l.1001; l.481; 1,582/12,393 = 12.8% | PASS ×5 |
| 27 | Equity deficit $1,791M; $79.3B treasury stock | Consolidated Balance Sheet | l.1744; l.1741–1742 (79,316) | PASS ×2 |
| 28 | "most drive thru locations worldwide, with nearly 29,000"; delivery from nearly 41,000; loyalty in 70 markets, nearly 220M users, $40B trailing | MD&A (Growth Pillars); Q2 release p.1 | l.395; l.393; `press-release` l.14 | PASS ×5 |
| 29 | "seventeen unique billion-dollar brands" | MD&A (Growth Pillars) | l.387 | PASS |
| 30 | Comparable guest counts negative in U.S. 2024 and Q2 2026 | 10-K FY2024 MD&A; 10-Q MD&A | `10-K-FY2024` l.349; `10-Q` l.1089 | PASS ×2 |
| 31 | "generally does not work with passive investors"; ~$4M sales per U.S. franchised restaurant (computed); advertising pool by percent of sales | Note: Franchise Arrangements; Description; MD&A (Franchised Sales); supplement p.13; Note: Summary of Significant Accounting Policies | l.207; 51,946/13,128 = $3.96M; l.2057–2059 | PASS ×3 |
| 32 | "royalty relief and/or deferral of cash collection" 2023 and 2024; a third of franchisees off pricing guidance | 10-K FY2024 MD&A (Revenues); call l.104; 10-K FY2023 | `10-K-FY2024` l.610; `10-K-FY2023` l.637; `transcript` l.104 ("1/3 of the system that did not execute") | PASS ×3 |
| 33 | U.S. company-operated margin 19.5% (2021) → 11.6% (Q2 2026) | 10-K FY2023 MD&A (Restaurant Margins), (Revenues); Q2 supplement p.7 | 511/2,617 = 19.53% (l.779, l.649); 91/784 = 11.61% (l.240, l.131) | PASS ×2 (see §10(e)) |
| 34 | U.S. 40% of revenue, 47% of segment operating income (computed); $7.4B U.S. franchised revenues | Note: Segment; MD&A (Revenues) | 10,825/26,885 = 40.3%; 5,808/12,393 = 46.9%; l.592 (7,371) | PASS ×3 |
| 35 | Risk-factor quotes (franchisee success, funding, legal distinction, weight-loss, anti-American, geographic areas, food tampering) | 10-K Risk Factors | l.1252, l.1254, l.1304, l.1210, l.1242, l.1242, l.1276 | PASS ×7 |
| 36 | "informal eating out"; "are we taking share in each of the markets" | Competition; call l.156 | l.311; `transcript` l.156 | PASS ×2 |
| 37 | 68% of operating income outside the U.S.; China negative comps; $1.9B licensed royalties; $13.6B IOM | MD&A (Liquidity and Uses of Cash); 10-Q MD&A; MD&A (Revenues) | l.1037; `10-Q` l.1093; l.596 (1,898); 13,633 is the segment note (l.2283), the MD&A revenues table shows 13,410 excluding Other revenues | PASS on numbers; segment-note tag added (direct fix 7b) |
| 38 | IRS audits 2011–2012 and 2016–2021; transfer pricing; $537M France; $414M unrecognized tax benefits | Note: Income Taxes; 10-K FY2022 MD&A | l.2828, l.2830; `10-K-FY2022` l.561; l.2805 | PASS ×4 |
| 39 | Affiliates' revenue $579M = 2.2% (computed) | Note: Equity Method Investments; Statement of Income | l.2631; 579/26,885 = 2.15% | PASS ×2 |
| 40 | Kempczinski 57, CEO Nov 2019, Chairman May 2024, ran the U.S.; Borden 57, CFO Sept 2022, 30+ years, ran licensed markets | Information About Our Executive Officers | l.1478; l.1468 | PASS ×2 |
| 41 | Anderson 26 years, COO since April, replaced Erlinger Aug 4; adviser to early 2027; no reason given | 8-K 2026-08-04; Leadership release; call l.54 | 8-K Items 5.02 and 7.01 ("effective August 4, 2026"; "more than 26 years"; "advisory role until early 2027"; notice of "intention to leave", no reason); release para 1–3, 9; `transcript` l.54 ("Since April, as the Chief Operating Officer") | PASS ×5 (see §10(i)) |
| 42 | Twelve directors, eleven independent; Miles White Lead Independent Director | DEF 14A Overview of Director Nominees; Board Leadership | 8-K 05-22 lists 12 nominees; `DEF14A` l.2409 (eleven named independent), l.6680 ("All but one"); l.507, l.559 | PASS ×3 |
| 43 | Pay: 40/30/15/15; 76.4%; 50% PRSUs / 50% options; 75% EPS / 25% ROIC with relative TSR modifier; 82.2%; $20.6M; 1,082:1; Poland $19,020; 95.1% approval (computed); insiders <1%; Vanguard 10.03%, BlackRock 7.3%, State Street 5.1% | DEF 14A CD&A, Summary Compensation Table, Pay Ratio, Security Ownership; 8-K 2026-05-22 | l.4728; l.979; l.3911; l.3965; l.979; l.4720 (20,618) and l.5757 ($20,574,525); l.5757; l.5761; 478,236,845/(478,236,845+24,626,761) = 95.10%; l.6810; l.6985–7001 | PASS ×13 |
| 44 | Cash order quote "(i) invest ... (ii) prioritize our dividend and (iii) repurchase shares with remaining free cash flow over time"; 50 consecutive years; $1.86 Q4; $5.1B dividends; $2.0B buybacks 2025; $1.3B H1 2026; $11.7B left of $15.0B; $7.1B returned; AtO $795M and ~$250M; stock $100 → $160 vs $196 | MD&A (Foundation and Platforms), (Share Repurchases and Dividends), (Cash Flows); 10-Q Part II Item 2, Note: Accelerating the Organization; Stock Performance Graph | l.413; l.960; l.1816; l.1814; `10-Q` l.1297; `10-Q` l.2107 ($11,731,806,872), l.2117; l.373 and l.939 ("$7.1 billion"); `10-Q` l.718; l.1107, l.1109 | PASS ×11; "(computed)" on the $7.1B removed since the 10-K states it (direct fix 10) |

Totals across 3(a)–3(i): 265 table cells, 103 quoted strings and about 150 prose facts checked. FAIL: 0. Tag corrections: 3. Mislabels: 1. UNVERIFIABLE: 0 (the ROIC formula and the capex-by-type dollar split are correctly described as not in the cached text).

---

## 4. Number-source rule (§3 rule 2)

Every number whose only support is a call tag was checked for being a verbatim spoken statement presented as such:

| Figure | Where | Status |
|---|---|---|
| "$40 billion" systemwide sales added, "over $3 billion" operating income | outlook §2 l.20 | Quoted, labelled "spoken figures, not in the release" and distinguished from the release's $40B. OK |
| "more than $20 billion" delivery sales | outlook §3 l.28 | Quoted, "(spoken, not in the release)". OK |
| "up about 50%" beverage check; "ahead of plan" | outlook §3 l.32 | Quoted, "(spoken; no beverage sales are disclosed)". OK |
| "60% to 65%", "15% discount or better", "$5 Meal Deals", "10 items for under $3" | outlook §3 l.36 | Verbatim quotes. OK |
| "$0.15", "$0.20 to $0.30" currency | outlook §4 l.54, claim 7 | Verbatim guidance; release carries no currency guidance. OK |
| "2.2%" G&A | outlook §4 l.55, claim 6 | Verbatim; the written Outlook figure is separately tagged to the 10-Q in table 1. OK |
| "1.5% and 1.9%" inside the acceleration quote | l.57, claims 1–2 | Same figures as release p.2, presented as the CFO's words. OK |
| "2,600 gross restaurants" | l.61 | Verbatim in a table headed "Spoken on the call ... wording only"; the written figure is in table 1 with the 10-Q tag. OK |
| "every 10 years" remodel; "a third" of franchisees; "slightly negative" July; "since April" (Anderson) | business.md l.80, l.109, l.115, l.131 | Each attributed to the speaker ("the CEO says", "as the CEO said", "the CFO said"). OK |

No violations. Where the release, supplement or a filing carries the number (comps, systemwide growth, margins, counts, loyalty users, outlook bullets), the draft tags that source, not the call.

---

## 5. Jargon audit

Reader: a smart 16-year-old with no finance background. Terms neither plain, name-inferable nor in the Glossary, and the action taken:

| Term | Where | Action |
|---|---|---|
| royalties (never defined) | business.md §1 l.8 | Glossed "(a percentage of each restaurant's sales)" — direct fix |
| consolidated markets | business.md §3 l.80 | Glossed "(the markets it accounts for directly, mainly the U.S. and the owned international markets)" — direct fix |
| After-tax return on invested capital | business.md §4 table l.95 | Row label extended: "the company's measure of profit earned per dollar tied up in the business" — direct fix |
| impairment | business.md §6 l.121 | "an impairment (write-down) of an affiliate stake" — direct fix |
| transfer pricing | business.md §6 l.125 | Glossed "(how profit is split between the countries inside the company)" — direct fix |
| unrecognized tax benefits | business.md §6 l.125 | Glossed "(tax the company might owe if audits go against it)" — direct fix |
| EPS | business.md §7 l.133 | "EPS (earnings per share)" — direct fix |
| relative-shareholder-return modifier | business.md §7 l.133 | Rewritten "with a modifier for the stock's return against the S&P 500" (per `DEF14A` l.3965) — direct fix |
| tailwind; adjusted EPS | outlook.md claim 7 l.72 | "tailwind (boost)"; "adjusted EPS (earnings per share before one-off charges)" — direct fix |

Judged acceptable without change: franchisee/franchisor (explained l.6), Systemwide sales, Comparable sales, conventional franchise, developmental licensee, affiliate (Glossary), constant currency ("at last year's exchange rates", l.8 and outlook l.11), check ("average spend per order", l.115), G&A and SG&A ("overhead", outlook l.20, business l.148), refranchising (glossed l.145 and outlook l.20), capex (glossed l.73), free cash flow and conversion (defined l.88–89, l.99), investment grade ("a few notches above junk", l.101), comparable guest counts ("fewer people paid more", l.107), restaurant margins (defined l.64), trailing-twelve-month (plain), Founder's Day, McValue, EDAP-free wording ("10 items for under $3"), 2-year stack (not used), QSR (not used). Glossary holds five unavoidable terms, one sentence each; nothing else is in it.

---

## 6. Invented-number check

- Every "(computed)" cell in business.md §2, §3, §4 and outlook §1 re-derived; all correct (details in §3).
- Every "not disclosed" statement checked against the filing that should carry it: openings/closings at 6/30/2026 (10-Q note and supplement give none); rent and royalty rates (Franchise Arrangements note gives none; no percentage found by regex); capex dollar split by type (chart image, titles only at l.929); ROIC formula (Exhibit 99.1, not fetched, per MANIFEST). All hold.
- Mislabel found and fixed: "$7.1 billion ... (computed)" (business.md l.135); the 10-K states $7.1 billion (l.373, l.939). Note for the owner: the two cash-flow lines the table shows sum to $7,171M, which rounds to $7.2 billion; the draft now says "(as stated)".
- Unlabelled computations that are correct and harmless: "about 13% of operating income" for interest (1,582/12,393, labelled computed already); "roughly $4 million a year" (labelled).
- No figure without a tag; no tag that fails to support its figure after the three tag corrections in §12.

---

## 7. Claims check (§9), outlook.md §5

| # | One sentence, one thing | Single direction, can fail | Verbatim quote + tag | Labelling | Gradeable from §5 alone |
|---|---|---|---|---|---|
| 1 | Yes (IOM Q3 comps > 1.5%) | Yes | Yes, l.95 | Management claim | Yes (Q3 release p.2) |
| 2 | Yes (IDL Q3 comps > 1.9%) | Yes | Yes, l.95 | Management claim | Yes |
| 3 | Yes (U.S. Q3 comps < 0.8%) | Yes | Yes, l.94 | Sharpening labelled "our sharpening ... not management's number" | Yes |
| 4 | Yes (Outlook still "approximately 2,100") | "Reaffirms" form, allowed | Yes, 10-Q Outlook | Management claim | Yes (Q3 supplement Outlook) |
| 5 | Yes (Outlook still "50,000 ... in 2028") | Allowed | Yes, call l.44; 10-Q tag added to the in-claim phrase (direct fix) | Management claim | Yes |
| 6 | Yes (9-month SG&A ≤ 2.3%) | Yes | Yes, l.43 | Sharpening labelled; "year-to-date figure" stated | Yes (Q3 supplement SG&A page) |
| 7 | Yes (positive FY currency tailwind still estimated) | Yes (headwind or silence fails or drops it) | Yes, l.42 | Management claim | Yes (Q3 call) |
| 8 | Yes (users > 220M) | Yes | Yes, release p.1 | Sharpening labelled; "a missing figure counts as dropped" | Yes (Q3 release p.1) |
| 9 | Yes (Red Bull on sale in U.S.) | Yes | Yes, l.51 | Management claim | Yes (Q3 call or release) |
| 10 | Yes (Investor Day held Sept 23) | Yes | Yes, l.57 | Event | Yes |
| 11 | Yes (G&A outlook beyond 2026 given at Investor Day) | Yes; the parenthetical defines what counts, not an either/or outcome | Yes, l.44 | Management claim | Yes, provided the refresh gatherer fetches the Investor Day materials (8-K or IR deck); noted for the owner |
| 12 | Yes (company-operated count < 2,012) | Yes | Yes, l.44; supplement p.13 | Labelled "Disclosure check (quarter-end count)" | Yes (Q3 supplement p.13) |

Count 12 (within 6–12). Headline EPS/revenue: none; claim 7 is about a currency effect on EPS, the rest are fundamentals (comps by segment, units, overhead, loyalty, beverages, refranchising). No either/or constructions. No vague statement passed off as a claim.

---

## 8. Indicator check (§8)

Seven indicators in business.md §8, each named, with a why and a recurring location, each verified to exist in both the Q1 and Q2 materials:

1. Comparable sales by segment — release p.2 table; supplement "Comparable Sales" (Q2 l.170–176; Q1 l.126–133); 10-Q MD&A. Recurring.
2. Systemwide sales growth in constant currency by segment — supplement "Systemwide Sales and Franchised Sales" (Q2 l.184–191; Q1 l.141–148). Recurring.
3. Restaurants by ownership type, net additions computed — supplement "Restaurant Information" (Q2 p.12–13; Q1 p.9–10); 10-Q Restaurant Information note. Recurring.
4. Franchised margin $ and % — supplement "Restaurant Margins" (Q2 p.7; Q1 p.5); revenues page for the denominator. Recurring.
5. Company-operated margin $ and %, total and U.S. — same pages. Recurring.
6. Operating margin for the quarter (computed from the release income statement) and SG&A as % of Systemwide sales (year-to-date, as printed on the supplement's SG&A page). Recurring; the draft correctly marks the SG&A figure as year-to-date (see §10(b)).
7. Trailing-twelve-month Systemwide sales to loyalty members, with the 90-day user count "when given" — release p.1 headline bullets; both releases carry the trailing figure (Q1 "over $38 billion", Q2 "$40 billion"), only Q2 the user count. Anchored to the recurring form, with the intermittent one flagged as such.

None depends on a one-off call number; free cash flow conversion is explicitly parked as a claim, not an indicator (l.151). `_Proposed — owner to review and lock._` present (l.139). Outlook §1 has exactly one row per indicator, in order, with this quarter / last quarter / expectation columns; "No guidance" where none was given; every value verified in §3(g).

---

## 9. As-of discipline

Every source read is dated on or before 2026-08-07 (10-Q filed 2026-08-07; release, supplement, leadership 8-K and call 2026-08-04; Q1 materials 2026-05-07; proxy 2026-04-07). The transcript was posted 2026-08-11, admitted under §12.2 for call content only, with both dates in MANIFEST and both Sources lists. The September 23, 2026 Investor Day appears only as an announced future event ("which had not happened at this report's cutoff", outlook l.20; claims 10–11 are written to be checked after it). No later-quarter figure, event or wording appears in either draft.

---

## 10. Specific points requested by the orchestrator

- **(a) Two "$40 billion" figures.** Kept distinct. Outlook §2 l.20 quotes the CEO's "$40 billion" of systemwide sales added under Accelerating the Arches and says in the same sentence it is "a different $40 billion from the release's trailing loyalty sales"; outlook §1 row 7, §3 l.26 and business.md §5 l.107 use the release's $40 billion (trailing-twelve-month sales to loyalty members, `press-release` l.14) with the release tag. PASS.
- **(b) 46.2% / 46.9% are six-month figures.** Neither number appears in either draft. The only quarter operating margin given is outlook §1 row 6, "47.0% (computed) [Q2 2026 release, p.5]" = 3,338/7,099 = 47.02% (release l.145, l.155). Q1's 45.3% is a single-quarter figure as printed (Q1 supplement l.239). The SG&A 2.2% is labelled year-to-date and comes from the supplement's six-month sentence (l.281). PASS.
- **(c) 50,000 target date.** Outlook §3 l.24: moved from "end of 2027" [10-K FY2025] to "in 2028" [10-Q Outlook] with the CFO's reason quoted; verified at `10-K-FY2025` l.397 and l.433 ("by the end of 2027") and `10-Q` l.1803 / supplement l.384 ("in 2028"); call l.44–45 and l.153 agree. Both tags present. One wording slip fixed: outlook §4 said the written Outlook was "unchanged from Q1 except for the 50,000-unit date", but the Q1 Outlook (Q1 supplement l.300) did not mention the 50,000 target at all; the Q2 version adds it with 2028. Reworded (direct fix 11). PASS.
- **(d) FY2025 10-K free-cash-flow contradiction.** business.md §4 l.99 quotes both the "decrease of $510 million or 8%" (l.895) and the "8% increase" (l.369), points to the statement figures 7,186 vs 6,672 (both re-derived) and labels the resolution computed. PASS.
- **(e) FY2021 U.S. company-operated margin 19.5%.** `10-K-FY2023` l.779: U.S. company-operated margin 2021 = 511; l.649: U.S. company-operated sales 2021 = 2,617; 511/2,617 = 19.53%. Q2 2026: 91/784 = 11.61% (supplement l.240, l.131). Both tags point to the right sections. PASS.
- **(f) "Other revenues" explanation.** business.md l.60 says they are "mainly fees franchisees pay back for technology platforms, which 'are not designed to generate margins for the Company', plus brand licensing". The 10-K: "fees paid by franchisees to recover a portion of costs incurred by the Company for various technology and digital platforms and revenues from brand licensing arrangements" (supplement l.116, same words in the 10-Q l.1341) and "the various technology platform fees are not designed to generate margins for the Company" (`10-K-FY2025` l.2000, in the revenue-recognition part of the Summary of Significant Accounting Policies note, as tagged). Matches. PASS.
- **(g) Loyalty indicator anchoring.** Anchored to the release p.1 headline bullet on trailing-twelve-month Systemwide sales to loyalty members, which both the Q1 (l.16) and Q2 (l.14) releases carry; the 90-day user count is marked "when given" and its absence in Q1 is stated in outlook §1. PASS.
- **(h) Tables instead of bullets in outlook §4.** Judged acceptable: the first table reproduces all seven written Outlook bullets complete and verbatim with one tag; the second table gives the spoken items as verbatim fragments, each with its line tag, under a header that says "wording only". It reads well and is easier to scan than fourteen bullets would be. No REVISE item; no length consequence.
- **(i) Anderson / Erlinger.** business.md l.131: 8-K Item 5.02 (Erlinger gave notice August 3, 2026, effective August 4, 2026; advisory role "until early 2027"; "no change to his compensation"; no reason stated) and Item 7.01 (Anderson appointed EVP and President, McDonald's USA, effective August 4, 2026; "more than 26 years"; most recently COO of McDonald's USA); leadership release para 1–3 and 9 agree; call l.54 gives "Since April" for the COO role. The draft's facts and dates match. PASS.

---

## 11. Length (§3 rule 7)

| File | Before review | After direct fixes | Target | Status |
|---|---|---|---|---|
| business.md | 2,524 | 2,593 | 2,000–3,000 | OK |
| outlook.md | 1,020 | 1,044 | 800–1,200 | OK |

Counter: `python3 -P /tmp/mcd-orch/wc_prose.py` from cwd `/home/ubuntu`; the writer's reported 2,524 / 1,020 reproduced exactly before edits.

---

## 12. Direct fixes made by the reviewer (before → after)

business.md

1. §1 l.8: "only the rent, royalties and fees it collects on them are" → "only the rent, royalties (a percentage of each restaurant's sales) and fees it collects on them are".
2. §2 l.44: tag on "Licensed markets hold 46% of the restaurants" `[10-K FY2025, Note: Summary of Significant Accounting Policies]` → `[10-K FY2025, MD&A (Restaurant Development and Capital Expenditures)]`. The by-segment count 20,805 is at `10-K-FY2025` l.917 in that MD&A section; the note (l.1944–1954) counts by ownership type only.
3. §3 l.76 footnote: "Revenues and SG&A: FY2021 [...]; FY2022 [10-K FY2024, Consolidated Statement of Income]; FY2023–FY2025 [10-K FY2025, Consolidated Statement of Income]." → revenues keep those tags; SG&A totals now tagged `MD&A (Consolidated Operating Results)` in the FY2023, FY2024 and FY2025 10-Ks (l.567, l.546, l.516), with the note that the income statement splits SG&A into depreciation and other.
4. §3 l.80: "in its consolidated markets," → "in its consolidated markets (the markets it accounts for directly, mainly the U.S. and the owned international markets),".
5. §4 table l.95: row label "After-tax return on invested capital (as stated)" → "... (as stated; the company's measure of profit earned per dollar tied up in the business)".
6. §5 l.109: "the best public proxy for what a franchisee earns" → "in our view the best public proxy for what a franchisee earns" (labels a judgement).
7. §6 l.121: (a) "an impairment on an affiliate." → "an impairment (write-down) of an affiliate stake."; (b) "$13.6 billion [10-K FY2025, MD&A (Revenues)]" → added `[10-K FY2025, Note: Segment and Geographic Information]` (13,633 is the segment-note total, l.2283; the MD&A revenues table shows 13,410 excluding Other revenues).
8. §6 l.125: (a) "transfer pricing," → "transfer pricing (how profit is split between the countries inside the company),"; (b) "unrecognized tax benefits ($414 million at end-2025)" → "unrecognized tax benefits (tax the company might owe if audits go against it; $414 million at end-2025)".
9. §7 l.133: "three-year EPS growth and 25% on return on invested capital with a relative-shareholder-return modifier," → "three-year EPS (earnings per share) growth and 25% on return on invested capital, with a modifier for the stock's return against the S&P 500," (`DEF14A` l.3965).
10. §7 l.135: "$7.1 billion, almost exactly the $7.2 billion of free cash flow (computed)" → "$7.1 billion (as stated), almost exactly the $7.2 billion of free cash flow" (`10-K-FY2025` l.373, l.939 state $7.1 billion).

outlook.md

11. §4 l.40: "unchanged from Q1 except for the 50,000-unit date" → "unchanged in substance from Q1, except that the Q2 version adds the 50,000-unit target with a 2028 date, which the Q1 outlook did not mention" (Q1 supplement l.300 vs Q2 supplement l.384).
12. §5 claim 5 l.70: added `[10-Q Q2 2026, Outlook]` after the in-claim phrase "50,000 global units in 2028", which is the written Outlook's wording; the call quote and tag remain.
13. §5 claim 7 l.72: "currency tailwind on adjusted EPS." → "currency tailwind (boost) on adjusted EPS (earnings per share before one-off charges)."

No number, table cell, claim or quotation was changed. Fixes applied by `/tmp/mcd-orch/reviewer/apply_fixes.py` with a one-occurrence assertion per replacement; the quote sweep and tag-prefix check were re-run afterwards (unchanged results).

### Withdrawals recorded (§17: print full lines before ruling)

Six searches returned zero hits on first pass and were resolved as PASS after printing the surrounding table or full line; none was ruled a FAIL:

- "97% fixed-rate": `grep '97%'` found nothing because the 10-K prints the label and value on separate lines (`10-K-FY2025` l.980 "Fixed-rate debt as a percent of total debt", l.981 "97 | %").
- "$11.7 billion" remaining buyback authorization: the 10-Q prints "$ | 11,731,806,872" (l.2107).
- "48% and 35%": the Equity Method Investments table prints "48 | %" and "35 | %" (l.2621, l.2623).
- "$579 million" affiliate revenue: table cell "Revenue | $ | 579" (l.2631).
- "$28.2 billion" / "$14.8 billion": stated as 28,241 (l.2383) and 14,840 (l.2508).
- "Information About Our Executive Officers": heading is upper-case at l.1460; case-sensitive search missed it.

---

## 13. Verdict: PASS

No REVISE items. Everything that needed changing was cell-level or wording-level and has been fixed directly (§12). Judgement calls left for the owner, none blocking:

1. **Indicator 7's second half (90-day active users)** is not carried every quarter (absent in Q1 2026). The draft says "when given"; the owner may prefer to drop the user count from the indicator and keep it as a claim (claim 8 already does this).
2. **Claims 10 and 11** are checked against the September 23 Investor Day, so the Q3 refresh gatherers should fetch the Investor Day 8-K or IR materials; otherwise both would grade ⏳ or 🔇.
3. **§2 revenue table, FY2021 "Other revenues" 351** is the FY2023 10-K's MD&A figure (as tagged); the statement line is 350.1 and the FY2022 column uses the statement basis (328). Each cell matches its tag and the footnote explains the rounding change; a purist might align all five to one basis.
4. **"$7.1 billion returned in 2025"**: the 10-K states it, but the table's dividends (5,115) and buybacks (2,056) sum to 7,171; the draft now says "(as stated)".
5. **Glossary**: five entries, all essential. Nothing to trim.
