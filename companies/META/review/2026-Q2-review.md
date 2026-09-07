# Meta Platforms, Inc. (META) — Reviewer report, 2026-Q2

_Reviewed 2026-09-07 against `companies/META/sources/2026-Q2/` only (cached full texts; gatherer notes consulted only to see how the slide-chart labels were re-associated). As-of cutoff 2026-07-30. Line numbers below refer to the cached `.txt` files. Page numbers for `transcript.txt`, `transcript-followup.txt`, `press-release.txt`, `press-release-2026-Q1.txt` and `slides.txt` are the printed page numbers, which equal the PDF pages (form-feed markers in the text; main transcript p.N starts at lines 1 / 54 / 106 / 157 / 210 / 263 / 316 / 369 / 422 / 474 / 526 / 578 / 630 / 681 / 733 / 785 / 838 / 890 / 941 / 993 / 1045; follow-up p.N at 1 / 53 / 105 / 156 / 208 / 260 / 312 / 364 / 416 / 469 / 521; Q2 release p.N at 1 / 51 / 75 / 111 / 171 / 204 / 247 / 307 / 337; slides p.N at 1 / 8 / 52 / 95 / 130 / 160 / 189 / 221 / 252 / 281 / 307 / 328 / 368 / 405 / 406 / 436 / 470 / 509)._

**Final verdict (after cycle 2): PASS.** Cycle 1 returned REVISE with 12 items; all 12 were resolved in the writer's second pass and re-verified against the cached sources (see "Cycle 2" at the end of this file). The cycle-1 verdict paragraph is kept below for the record.

**Cycle-1 verdict: REVISE** (light second pass). Every number in every table reconciles to the filings and releases, every quote is verbatim, both files are inside their length targets, and no post-cutoff information was found. What needs the writer: one litigation figure is placed under the wrong case type (§6 scenario 2), one sentence about Nvidia is false as written (§6 scenario 5), the capex footnote misdescribes how FY2021–FY2022 were computed, one indicator bundles a one-off statement and another bundles four figures, one claim sharpens "soon" into a date without saying so, and a handful of precision items.

---

## 1. Rubric (§14)

Read as the owner would: a smart 16-year-old with no finance background.

1. **Can I explain what this company does, and who pays it, in two sentences?** **Yes.** §1 does it in three sentences: four free apps used by 3.6 billion people a day; businesses pay to show ads (98% of revenue); a marketer pays per impression or per action.
2. **Do I know exactly what would kill it, and what the early warning sign is?** **Yes.** §6 ranks five scenarios, each with a concrete early warning (FCF negative two quarters / depreciation outgrowing revenue / margin near 31%; verdicts that change product design; Europe's ad price growth trailing; DAP flat two quarters; new operating-system privacy rules) and a stated share of the profit pool. Scenario 1 (capex against $43.6B of FCF, $349B of commitments, ~$347B of unstarted leases) is the sharpest part of the report.
3. **Do I know why the margins are what they are, and whether cost scales with usage?** **Yes.** §3 explains the ~80% gross margin (cost of revenue 18–19% of sales), R&D as the big cost, the 2022 dip and the layoffs, and then the mechanism that matters now: capex becomes depreciation, depreciation is fixed, so a growth slowdown hits margin fast. The "Promised but not yet on the balance sheet" paragraph makes the lease/commitment/JV structure followable.
4. **Could I predict what the scorecard will check next quarter, from §5 of the outlook alone?** **Yes.** All 11 claims are single-direction and mechanical; only claim 10 needs its sharpening labelled (see §5 below).
5. **Did nothing in the report require knowledge I don't have?** **Now yes, with one open item.** Before review, about a dozen terms were unexplained (balance sheet, injunction, receivables, stock option / exercise price, income statement, vest, compute, API in a quote, basis point, open-source, Horizon, amortization); all are now glossed directly (see "Fixed directly"). Still open: "proxy" in claim 4 (meaning stand-in, but the report also cites a proxy statement), which is claim wording and therefore the writer's.

---

## 2. Skeleton and format compliance

**business.md**

| Requirement (§6) | Status |
|---|---|
| `# <Company> — The Business` | OK (`# Meta Platforms, Inc. — The Business`) |
| `_As of <QLABEL>. Written <date>._` | OK (`_As of Q2 2026. Written 2026-09-07._`) |
| §1 What they do (incl. short history) | OK; history paragraph at line 10 |
| §2 How the money comes in (5-year segment table) | OK; FY2021–FY2025 + Q2 2026 |
| §3 The economics (revenue, GM, OM, capex, capex/revenue) | OK; plus R&D/revenue and D&A rows, and a second FoA/RL profit table |
| §4 How profitable, really (5-year table) | OK |
| §5 Why customers don't leave (source + weakening sign) | OK; two moats (network, ad performance) and one sign each |
| §6 What could break it (ranked; early warning; exposure; concentration) | OK; five ranked scenarios, "Other exposures", "Concentration" paragraph |
| §7 Who runs it and what they do with the cash | OK; control, people, pay, cash table |
| §8 Indicators (5–8; name / why / where) | OK; 8 indicators, each with source location |
| `_Proposed — owner to review and lock._` | OK (line 140) |
| Glossary (only unavoidable terms, one sentence each) | OK; 5 entries |
| Sources (every tag mapped; page basis stated) | OK; 9 tags mapped; "Release and slide page numbers are PDF pages (they coincide with the printed page numbers); transcript page numbers are the printed page numbers, which equal the PDF pages" — matches MANIFEST |
| Heading order | OK |
| Length 2,000–3,000 prose words, aim lower half | **PASS**: 2,495 before review, 2,533 after my glosses (`/tmp/wc_prose.py`) |

**outlook.md**

| Requirement (§7) | Status |
|---|---|
| `# <Company> — Outlook as of <QLABEL>` | OK |
| `_Transcript source tier: ... Written <date>._` | OK (`company-published`; MANIFEST says tier 1, Meta IR via Q4 Inc. CDN) |
| §1 one row per indicator; this q / last q / expected | OK; 8 rows matching business.md §8 in order |
| §2 What management says | OK |
| §3 Growth engines (what / how big / claim / working-or-not) | OK; six engines, each with a "Working if" test |
| §4 Guidance verbatim | OK; eight bullets, all verified word for word (§4 below) |
| §5 Claims (6–12) | OK; 11 claims |
| §6 Tone shift | Correctly omitted (first run) |
| Sources | OK; 8 tags mapped; page basis stated; the p.21 "demand"→"supply" correction is disclosed |
| Length 800–1,200 prose words | **PASS**: 998 before review, 1,026 after glosses |

**Indicator anchoring (§8 of AGENTS.md)** — each proposed indicator and the recurring disclosure it rests on:

| # | Indicator | Recurring disclosure | Anchored? |
|---|---|---|---|
| 1 | DAP, y/y growth | Release p.1 "Operational Highlights" bullet every quarter; 10-Q Item 2 | Yes |
| 2 | Ad impressions, y/y % | Release p.1 bullet; 10-Q Item 2; slides p.12 by region | Yes |
| 3 | Average price per ad, y/y % | Release p.1 bullet; 10-Q Item 2; slides p.13 by region | Yes |
| 4 | RL operating loss (quarter and YTD) **and the full-year RL loss statement** | Release p.8 segment table; 10-Q segment note — recurring. The "full-year RL loss statement" is a management sentence that appeared in the 10-K and both 10-Qs but is not a disclosure Meta is obliged to repeat | **Partly**: the statement half is exactly the kind of one-off item §8 says to track as a claim (it already is claim 7). REVISE item 4 |
| 5 | Capex incl. finance-lease principal; capex/revenue; leases not yet commenced; non-cancelable contractual commitments | Release p.1 bullet and p.9 reconciliation; 10-Q commitments note (Note 9 in Q2, Note 8 in Q1) — all four recur every quarter | Yes, but four figures in one cell (REVISE item 5) |
| 6 | Free cash flow (quarter and YTD) | Release p.1 bullet and p.9 reconciliation; slides p.15 | Yes |
| 7 | Operating margin, total and FoA (computed) | Release p.1 headline table and p.8 segment table | Yes |
| 8 | Long-term debt; shares outstanding; buybacks | Release p.1 bullet and p.6 balance sheet; 10-Q cover/balance sheet; cash-flow statement | Yes |

None depends on a dollar target or growth percentage given once on a call.

---

## 3. Citation spot-check

Legend: PASS = number or wording found in the tagged source; FAIL = not in the tagged source, wrongly characterized, or tagged to the wrong place. Computed cells were re-derived from the sourced inputs.

### 3(a) business.md §2 segment table (lines 14–20) — every cell

Inputs: `10-K-FY2023.txt` Note 2 l.2557–2561 (FY2021–FY2023); `10-K-FY2025.txt` Note 2 l.2524–2528 (FY2024–FY2025); `10-Q-2026-Q2.txt` Note 2 l.420–424 (Q2 2026). Segment totals also in `10-K-FY2023` Note 16 l.3287–3289 and `10-K-FY2025` Note 15 l.3280–3298.

| Row | Source values (USD m) | Result |
|---|---|---|
| Advertising 114.9 / 113.6 / 131.9 / 160.6 / 196.2 / 59.4 | 114,934 / 113,642 / 131,948 / 160,633 / 196,175 / 59,363 | PASS ×6 |
| Other FoA 0.7 / 0.8 / 1.1 / 1.7 / 2.6 / 1.0 | 721 / 808 / 1,058 / 1,722 / 2,584 / 1,007 | PASS ×6 |
| Family of Apps 115.7 / 114.5 / 133.0 / 162.4 / 198.8 / 60.4 | 115,655 / 114,450 / 133,006 / 162,355 / 198,759 / 60,370 | PASS ×6 |
| Reality Labs 2.3 / 2.2 / 1.9 / 2.1 / 2.2 / 0.4 | 2,274 / 2,159 / 1,896 / 2,146 / 2,207 / 431 | PASS ×6 |
| Total 117.9 / 116.6 / 134.9 / 164.5 / 201.0 / 60.8 | 117,929 / 116,609 / 134,902 / 164,501 / 200,966 / 60,801 | PASS ×6 |

30/30 PASS.

### 3(b) business.md §3 economics table (lines 34–42) — every cell

Inputs: income statements `10-K-FY2023.txt` l.2154–2161, `10-K-FY2025.txt` l.2104–2111, `10-Q-2026-Q2.txt` l.210–217; cash-flow statements `10-K-FY2023` l.2245, 2261, 2272; `10-K-FY2025` l.2204, 2219, 2233; `10-Q` l.310, 324, 337 and release p.7; FCF reconciliations `10-K-FY2023` Item 7 l.1912–1915 and `10-K-FY2025` Item 7 l.1847–1850; Meta's own percentage-of-revenue tables `10-K-FY2023` l.1689–1715 and `10-K-FY2025` l.1612–1640.

| Row | Check | Result |
|---|---|---|
| Revenue | as §2 | PASS ×6 |
| Gross margin (computed) 80.8 / 78.3 / 80.8 / 81.7 / 82.0 / 81.4% | Cost of revenue 22,649 / 25,249 / 25,959 / 30,161 / 36,175 / 11,330. Re-derived 80.79 / 78.35 / 80.76 / 81.67 / 82.00 / 81.37% | PASS ×6; labelled computed; prose says Meta does not report it (true: neither 10-K nor 10-Q has a gross-margin line) |
| R&D / revenue 21 / 30 / 29 / 27 / 29 / 36% | Meta's tables: 21 / 30 / 29 (FY2023 10-K l.1697) and 29 / 27 / 29 (FY2025 10-K l.1620); Q2: 21,656 / 60,801 = 35.6% | PASS ×6 |
| Operating margin 40 / 25 / 35 / 42 / 41 / 31% | Meta's tables: 40 / 25 / 35 and 41 / 42 / 35; Q2 release p.1 "31 %" | PASS ×6 |
| Capex incl. finance-lease principal 19.2 (computed) / 32.0 (computed) / 28.1 / 39.2 (computed) / 72.2 / 31.1 | FY2023 10-K Item 7 FCF table l.1912–1914: "Purchases of property and equipment, net" 18,567 / 31,186 / 27,045 + finance-lease principal 677 / 850 / 1,058 → 19,244 / 32,036 / 28,103. FY2023 stated "$28.10 billion" (l.1409). FY2025 10-K FCF table l.1847–1850: 37,256 + 1,969 = 39,225; 69,691 + 2,524 = 72,215, stated "$72.22 billion" (l.1397). Q2: 30,116 + 962 = 31,078, stated "$31.08 billion" (release p.1 l.32) | PASS ×6 on arithmetic. **Labelling nit (REVISE item 3):** the footnote at line 44 says the computed cells "add the two cash-flow lines". For FY2021–FY2022 they do not: the cash-flow statement's gross purchases are 18,690 and 31,431 (`10-K-FY2023` l.2261), which would give 19.4 and 32.3. The writer correctly used Meta's own FCF reconciliation basis (net purchases), which is how Meta itself reported $32.04B for 2022 and $19.24B for 2021; the footnote should say so. |
| Capex / revenue (computed) 16.3 / 27.5 / 20.8 / 23.8 / 35.9 / 51.1% | 19,244/117,929 = 16.32%; 32,036/116,609 = 27.47%; 28,103/134,902 = 20.83%; 39,225/164,501 = 23.84%; 72,215/200,966 = 35.93%; 31,078/60,801 = 51.11% | PASS ×6 |
| D&A 8.0 / 8.7 / 11.2 / 15.5 / 18.6 / 6.4 | 7,967 / 8,686 / 11,178 / 15,498 / 18,616 / 6,356 | PASS ×6 |

42/42 PASS (one footnote-wording nit).

### 3(c) business.md §3 FoA/RL profit table (lines 48–53) — every cell

Inputs: `10-K-FY2023` Note 16 l.3291–3293; `10-K-FY2025` Note 15 l.3284–3298; `10-Q` Note 12 l.874–887; line 55's Q1 2026 RL loss from `10-Q-2026-Q1` Note 11 l.821 (4,028).

| Row | Source values | Result |
|---|---|---|
| FoA operating income 56.9 / 42.7 / 62.9 / 87.1 / 102.5 / 23.4 | 56,946 / 42,661 / 62,871 / 87,109 / 102,469 / 23,394 | PASS ×6 |
| RL operating loss (10.2) / (13.7) / (16.1) / (17.7) / (19.2) / (4.6) | (10,193) / (13,717) / (16,120) / (17,729) / (19,193) / (4,619) | PASS ×6 |
| RL loss as % of FoA profit (computed) 18 / 32 / 26 / 20 / 19 / 20% | 17.9 / 32.2 / 25.6 / 20.4 / 18.7 / 19.7% | PASS ×6 |
| Total operating income 46.8 / 28.9 / 46.8 / 69.4 / 83.3 / 18.8 | 46,753 / 28,944 / 46,751 / 69,380 / 83,276 / 18,775 | PASS ×6 |
| Q1 2026 RL loss $4.0B | 4,028 | PASS |

25/25 PASS. "RL's operating loss has grown every year" (line 46): 10.2 → 13.7 → 16.1 → 17.7 → 19.2, true.

### 3(d) business.md §4 cash table (lines 71–80) — every cell

| Row | Source values | Result |
|---|---|---|
| Operating cash flow 57.7 / 50.5 / 71.1 / 91.3 / 115.8 / 31.9 | 57,683 / 50,475 / 71,113 (`10-K-FY2023` l.2259); 91,328 / 115,800 (`10-K-FY2025` l.2217); 31,862 (release p.7 l.266) | PASS ×6 |
| Capex | as §3 | PASS ×6 |
| Free cash flow 38.4 / 18.4 / 43.0 / 52.1 / 43.6 / 0.8 | Meta's FCF tables: 38,439 / 18,439 / 43,010 (`10-K-FY2023` l.1915); 52,103 / 43,585 (`10-K-FY2025` l.1850); 784 (release p.9 l.362) | PASS ×6 (these are Meta's stated FCF, not computed; table label "Meta's definition" is right) |
| Net income 39.4 / 23.2 / 39.1 / 62.4 / 60.5 / 15.8 | 39,370 / 23,200 / 39,098; 62,360 / 60,458; 15,848 | PASS ×6 |
| FCF / net income (computed) 98 / 79 / 110 / 84 / 72 / 5% | 97.6 / 79.5 / 110.0 / 83.6 / 72.1 / 4.9% | PASS ×6 |
| Share-based compensation 9.2 / 12.0 / 14.0 / 16.7 / 20.4 / 7.7 | 9,164 / 11,992 / 14,027 / 16,690 / 20,427 / 7,658 | PASS ×6 |
| Buybacks 44.5 / 28.0 / 19.8 / 30.1 / 26.2 / 0 | Cash-flow "Repurchases of Class A common stock" 44,537 / 27,956 / 19,774 / 30,125 / 26,248 / — | PASS ×6 (cash basis, consistent across years, matches row label "(cash)") |
| Dividends 0 / 0 / 0 / 5.1 / 5.3 / 1.4 | No dividend line in FY2021–FY2023 cash flow; 5,072 / 5,324 (`10-K-FY2025` l.2231); 1,353 (release p.7 l.279) | PASS ×6 |

48/48 PASS.

### 3(e) business.md §7 cash table (lines 124–134) — every figure

| Row | Source | Result |
|---|---|---|
| Buybacks $30.1B → $26.2B → $0 | cash flow l.2230 (30,125 / 26,248); `10-Q` Note 10 l.796 "did not repurchase any shares ... six months ended June 30, 2026" | PASS |
| Authorization unused $25.03B | `10-Q` Note 10 l.796 | PASS |
| Shares 2,741M → 2,530M → 2,548M | `10-K-FY2023` equity statement l.2213 "Balances at December 31, 2021 \| 2,741"; `10-K-FY2025` balance sheet / `10-Q` l.188 (2,187 + 343 = 2,530; 2,206 + 342 = 2,548) | PASS |
| Dividend $0.50 → $0.525, unchanged since Q1 2025 | `10-K-FY2025` Note 12 l.3031–3041; `10-Q` Note 10 l.800 ($0.525 in Q2 2026) | PASS |
| Long-term debt $29B → $59B → $84B | face amounts `10-K-FY2025` Note 10 l.2871 (29,000 / 59,000); `10-Q` Note 8 l.657 (84,000); row label says "amount borrowed", i.e. face, correct | PASS |
| Notes $30.0B Nov 2025; $25.0B May 2026 | `10-K-FY2025` Note 10 l.2864; `10-Q` Note 8 l.648 | PASS |
| Unrecognized RSU expense $54.8B → $79.8B | `10-K-FY2025` Note 12 l.3079 (54.81); `10-Q` Note 10 l.832 (79.79) | PASS |
| Cash tax on vesting $18.4B; $8.7B | `10-K-FY2025` Item 7 l.1824 (18.40); `10-Q` Item 2 l.1311 (8.70) | PASS |
| Scale AI $13.8B, 2025 | `10-K-FY2025` Note 5 l.2692 (13.80) | PASS |

20/20 PASS.

### 3(f) outlook.md §1 indicator table (lines 10–17) — every number

| Cell | Source | Result |
|---|---|---|
| DAP 3.60B +3% / 3.56B +4% | Q2 release p.1 l.24; Q1 release p.1 l.32 | PASS ×2 |
| Impressions +14% / +19% | Q2 release l.25; Q1 release l.35 | PASS ×2 |
| Price +12% / +12% | Q2 release l.26; Q1 release l.36 | PASS ×2 |
| RL loss $4.62B / $4.03B; expected "to remain similar to 2025" ($19.19B) | Q2 release p.8 l.330 (4,619); Q1 release p.8 l.330 (4,028); `10-K-FY2025` Item 7 l.1451 has both the $19.19B and the sentence; `10-Q-2026-Q1` Item 2 l.926 repeats it (tag added by me) | PASS ×3 |
| Capex $31.08B; 51%; $278.99B; $349.31B | release p.1 l.32; 31,078/60,801 = 51.1%; `10-Q` Note 9 l.682, 684 | PASS ×4 |
| Q1: $19.84B; 35%; $182.88B; $237.67B | Q1 release p.1 l.39; 19,840/56,311 = 35.2%; `10-Q-2026-Q1` Note 8 l.620, 622 | PASS ×4 |
| Expected FY2026 capex "$125-145 billion" | Q1 release p.2 l.64 | PASS |
| FCF $784M / $12.39B | release p.1 l.37; Q1 release p.1 l.43 | PASS ×2 |
| Operating margin 31%; 39% / 41%; 48% | release p.1 l.17 (31%), 23,394/60,370 = 38.75%; Q1 release l.17 (41%), 26,900/55,909 = 48.1% | PASS ×4 |
| Expected "above 2025 operating income"; "$162-169 billion" | Q1 release p.2 l.62, l.60 | PASS ×2 |
| Debt $83.66B; 2,548M; $0 / $58.75B; 2,538M; $0 | release p.1 l.36; `10-Q` l.188; `10-Q` cash flow l.334 (—); Q1 release p.6 l.226 (58,748); `10-Q-2026-Q1` l.188 (2,196 + 342); l.321 (—) | PASS ×6 |

32/32 PASS.

### 3(g) Prose sentences — 58 checks across all sections of both files

| # | Sentence / figure (file:line) | Tag | Found | Result |
|---|---|---|---|---|
| 1 | "we generate substantially all of our revenue from selling advertising placements on our family of apps to marketers" (b:6) | 10-K FY2025, Item 1 | l.214 | PASS |
| 2 | Advertising 98% of 2025 revenue (computed) (b:6) | Note 2 | 196,175 / 200,966 = 97.6% | PASS |
| 3 | RL "to continue to operate at a loss for the foreseeable future"; "is dependent on generating sufficient profits from other areas of our business" (b:8) | Item 1; Item 7 | l.218; l.224 and l.1451 | PASS |
| 4 | "superintelligence, which we define as AI that surpasses human intelligence"; "personal superintelligence for everyone" (b:8) | Item 1 | l.182; l.178 | PASS |
| 5 | Incorporated Delaware July 2004; IPO May 2012; "the metaverse" 2021 (b:10) | Item 1; Item 1A | l.296; l.558 | PASS |
| 6 | Zuckerberg 41; 60.8% of votes (b:10, b:116) | DEF 14A | l.269 "Age : 41"; l.1485 | PASS |
| 7 | 2022 ads +18%, price −16%; 2025 ads +12%, price +9%; Q2 impressions +14%, price +12%, ad revenue +27% (b:24) | 10-K FY2023 Item 7; 10-K FY2025 Item 7; release; 10-Q Item 2 | l.1733; l.1374; release l.25–26; `10-Q` l.1165 | PASS |
| 8 | "that monetize at lower rates" ... Reels and Asia-Pacific (b:24) | 10-Q Item 2 | l.984, l.1004 | PASS |
| 9 | US & Canada 44%, Europe 24% of Q2 revenue by user geography (computed) (b:24) | slides p.3 | Q2'26 bar: 26,816 and 14,296 of 60,801 (l.75, l.71; the four regional labels sum to the total) → 44.1%, 23.5% | PASS |
| 10 | Other FoA revenue passed $1B, +73% (b:26) | call p.5 | l.210–211 | PASS |
| 11 | RL Q2 +16% on glasses, Quest lower (b:28) | 10-Q Item 2 | l.1173 | PASS |
| 12 | Cost of revenue 18–19% of revenue every year but 2022 (b:32) | Item 7 tables | 19 / 22 / 19 / 18 / 18 | PASS |
| 13 | ~21,000 layoffs 2022–2023 (b:32) | 10-K FY2023, Note 3 | l.2616 (~11,000) + l.2589 (~10,000) | PASS (sum of two stated figures; "about" covers it) |
| 14 | 70% wearables / 30% VR and Horizon (b:57) | Item 1 | l.210 | PASS |
| 15 | "regardless of whether we procure such property or equipment with a finance lease" (b:59) | release p.4 | l.160 | PASS |
| 16 | P&E $121B → $226B; $80B construction in progress; 2026 plan $130–145B (b:59) | 10-K Item 8; 10-Q Note 6; Item 2 | l.2065 (121,346); l.615, 612 (225,724; 80,345); l.1335 | PASS |
| 17 | Useful life 5.5 years Jan 2025, $2.92B less depreciation (b:61) | Note 1 | l.2293 | PASS |
| 18 | Depreciation of P&E $11.0B (2023) → $18.0B (2025); $6.0B Q2 (b:61) | 10-K Note 6; 10-Q Note 6 | l.2732; l.620 | PASS |
| 19 | Cost of revenue +33%, R&D +67%; "third-party AI token costs" new (b:61) | 10-Q Item 2 | l.1193; l.1203; phrase absent from Q1 10-Q and FY2025 10-K (0 hits) | PASS |
| 20 | $2.4B legal, $1.2B severance in Q2 (b:61) | release p.1 | l.29–30 (2.40; 1.18) | PASS |
| 21 | Leases not yet commenced $279B; ~$68B in July; $104B at year-end (b:63) | 10-Q Note 9; 10-K Note 7 | l.682 (278.99; 68); l.2785 (103.77) | PASS |
| 22 | Commitments $349B ($53.5B 2026, $81.7B 2027); $131B year-end (b:63) | 10-Q Note 9; 10-K Note 11 | l.684 (349.31; 53.52; 81.65); l.2897 (131.05) | PASS |
| 23 | Louisiana venture: Oct 2025, 20%, ~$27B, leases from 2029 ~$12.3B, RVG ~$28B, max exposure $46.0B, not consolidated (b:63) | 10-Q Note 5 | l.588–600 (12.31; 28; 46.03) | PASS (see REVISE item 9 on "the partners fund") |
| 24 | El Paso venture with BlackRock, ~$13B RVG (b:63) | 10-Q Note 13; call p.3 | l.899–901; l.141 | PASS |
| 25 | "has underbuilt historically for the wave of AI adoption"; "geared towards maximizing 2026 and 2027 capacity"; "overall industry capacity is going to remain tight for the foreseeable future" (b:65) | call p.8, p.9 | l.393; l.400; l.422 | PASS |
| 26 | CFO "supply constrained" even in core business (b:65) | call p.21 | l.1045–1046 with footnote l.1076 | PASS (corrected wording, accepted) |
| 27 | FCF definition quote (b:69) | 10-K Item 7 | l.1828 | PASS |
| 28 | FCF $784M on $31.9B OCF; buybacks stopped Q4 2025, zero H1 2026; $30B Nov 2025 and $25B May 2026 notes (b:84) | release; 10-K Item 5; 10-Q Notes 8, 10 | l.37; l.1338; l.648; l.796 | PASS |
| 29 | "is really the primary pillar by which we are financing all of our ambitions" (b:84) | follow-up p.3 | l.109 | PASS |
| 30 | Cash tax on vesting $18.4B / $8.7B (b:86) | Item 7; 10-Q Item 2 | l.1824; l.1311 | PASS |
| 31 | 57c / 47c operating profit per $ of P&E (computed) (b:86) | Item 8 | 69,380/121,346 = 0.572; 83,276/176,400 = 0.472 | PASS |
| 32 | $90.3B cash & marketable securities vs $83.7B debt (b:86) | release p.1 | l.34–36 | PASS |
| 33 | Facebook and Instagram "each have more than 2 billion daily users"; WhatsApp 30M messages/second World Cup Final; Threads 500M monthly (b:90) | call p.1 | l.28–32 | **FAIL (precision)**: transcript says "Instagram reached 2 billion daily actives" and "Facebook has reached more than 2 billion". "More than" is true of Facebook only. REVISE item 8 |
| 34 | "we continue to face competition ... in particular younger users" (b:90) | 10-Q Item 2 | l.984 | PASS |
| 35 | Instagram time spent "double digits", "largely driven by improvements to our Feed and Reels recommendations" (b:90) | call p.5 | l.255–256 | PASS |
| 36 | "be like our ad systems where businesses only pay us when we achieve results for them" (b:92) | call p.3 | l.135 | PASS |
| 37 | Advantage+ >$75B run-rate; 9M small businesses (b:92) | call p.7; p.2 | l.338; l.73 (also l.348) | PASS |
| 38 | 2022–2023 price −16%, −9% (b:94) | 10-K FY2023 Item 7 | l.1733 | PASS |
| 39 | $43.6B 2025 FCF; $349B commitments; ~$347B unstarted leases (computed) (b:100) | Item 7; Note 9 | 43,585; 349.31; 278.99 + 68 = 346.99 | PASS |
| 40 | No 2027 capex figure; no timeline for selling compute (b:100) | call p.10; follow-up p.5 | l.517; l.231 "we don't have a more definitive timeline to share right now" | PASS |
| 41 | LA jury $6M first personal-injury trial (b:102) | 10-Q Part II Item 1 | l.1489 (March 25, 2026; 70% to Meta) | PASS |
| 42 | New Mexico jury $375M; state seeks $953M "plus 'extensive changes to the manner in which we provide our services'" (b:102) | same | l.1489 | PASS |
| 43 | "a second New Mexico trial from September 8 seeks 'up to $62.85 billion'" placed under **youth-safety litigation** (b:102) | same | l.1431, in the **"Privacy and Related Matters"** subsection: "Trial in the New Mexico Attorney General's case, which has expanded to include various claims related to content moderation issues, is scheduled to begin on September 8, 2026. The New Mexico Attorney General has indicated that they intend to seek up to $62.85 billion in penalties in this case." | **FAIL (characterization)**: number, date and tag are right; the case is the state's privacy / consumer-protection suit, not a youth-safety case. REVISE item 1 |
| 44 | First multi-state AG trial August 12 (b:102) | same | l.1489 (MDL trial for four states' claims and all 29 AGs' disgorgement claim) | PASS |
| 45 | "could amount to an aggregate of up to hundreds of billions of dollars" (b:102) | same | l.1417 | PASS (note the youth paragraph itself says "in certain cases up to more than a trillion dollars", l.1489; the writer may want to add it) |
| 46 | FTC seeks ban on "our use of minors' data for any commercial purposes" (b:102) | same | l.1433 | PASS |
| 47 | EC €200M April 2025, "subscription for no ads", appeal, "less personalized ads", quoted warning (b:104) | same | l.1465 | PASS |
| 48 | Europe price +10% vs US & Canada +20%, Q2 2026 (b:104) | slides p.13 | chart labels present at l.370–373 but in scrambled order; `notes-ir.md` l.38 re-association (US&C 20%, Europe 10%, Worldwide 12%) checked against the release's worldwide 12% | PASS (via documented re-association) |
| 49 | DAP +7% Dec 2025 → +3% June 2026; Q1 dip from Iran and Russia (b:106) | 10-K Item 7; 10-Q Item 2 | l.1411; l.1026 | PASS |
| 50 | Apple 2021 quote; "a small number of third parties, often with significant operations in a single region such as Asia" (b:108) | 10-K Item 1A; 10-Q Item 1A | l.506; l.1967 | PASS |
| 51 | "The only chip supplier named anywhere is Broadcom, paid about $2.3 billion in 2025; Nvidia is not named" (b:108) | DEF 14A, Related Party Transactions | Broadcom $2.3B at l.647 PASS. "Nvidia is not named": **NVIDIA (NVDA) appears in the proxy at l.816 as a member of the compensation peer group**. Not named as a supplier anywhere (0 hits in all four financial filings, both transcripts, release, slides) | **FAIL (as written)**. REVISE item 2 |
| 52 | IRS $15.89B for 2017–2019, contested in Tax Court (b:110) | 10-Q Note 11 | l.856 ("filed a petition with the Tax Court in December 2025") | PASS |
| 53 | WhatsApp interim measure June 2026, intend to appeal (b:110) | Part II Item 1 | l.1467 | PASS |
| 54 | No customer ≥10% 2023–2025; 37% from US-based marketers; China resellers quote; China $13.7B = 10% of 2023 (b:112) | 10-K Note 1; Item 1A; 10-K FY2023 Note 2 | l.2498; l.2494; l.948; l.2575 (13.69B / 134,902 = 10.1%); no China footnote in FY2025 Note 2 ("undisclosed since" holds) | PASS |
| 55 | Class B ten votes; 99.8% of Class B; 60.8% of votes; ~13.5% of shares (computed); controlled company; "Our CEO has control over key decision making"; board opposed Proposal Five (b:116) | Note 12; DEF 14A; 10-K Item 1A | l.3015; l.1485; (639,347 + 341,823,978) / (2,196,045,588 + 342,377,716) = 13.49%; l.534; l.924; l.1836 "recommends a vote AGAINST" | PASS |
| 56 | Li CFO since 2022, at Meta since 2008; no MSL head among executive officers; headcount 75,472 incl. ~8,000 (b:118) | DEF 14A; release | l.353; officer list l.268–366 (Zuckerberg, Powell McCormick, Olivan, Li, Bosworth, Cox, Mahoney; "Superintelligence Labs" appears only in bonus rationale l.886); l.38–40 | PASS (but see REVISE item 7 on "long-tenured insiders") |
| 57 | $1 salary; $25.1M mostly security and aircraft; $1M salaries; 200% target / 115% payout; RSUs $20–22M; four-year quarterly vesting; 20M options at $2,788 (b:120) | DEF 14A CD&A; 10-Q Note 10 | l.1039 (25,125,904), l.1041; l.862–865; l.879, l.917 (Li 200 \| 115); l.927–930 (20,000,000; 22,000,000 ×3); l.933; `10-Q` l.836 | PASS |
| 58 | outlook §3: Threads global ads expansion complete; Meta AI +60% since Muse Spark; model API and Meta One launched; EssilorLuxottica line; business agents >1M businesses; charging in H2 via Meta One and per-token from Aug 1; other revenue growth on active businesses and marketing messages (o:27–37) | call p.6, p.2, p.8, p.4, p.3; follow-up p.10, p.3 | l.308–310; l.91–92; l.80, l.96, l.379–384; l.160; l.123–124; follow-up l.500–511; follow-up l.138–146 | PASS |

**Citation tally:** 30 + 42 + 25 + 48 + 20 + 32 table/indicator cells = 197 cells, plus 58 prose checks and 73 quoted strings (§4) = **328 checks. 325 PASS, 3 FAIL** (items 33, 43, 51), plus one footnote-wording nit (capex basis). No tag points to a wrong document; item 43's tag is right and its placement is wrong. None of the three failures came from a gatherer note: `notes-filings.md` l.477 correctly says Nvidia is "not named anywhere in the four SEC financial filings" and names Broadcom via the proxy; the writer widened that to "anywhere".

---

## 4. Verbatim-quote check

Every string inside double quotes in both files (73 strings of 12+ characters) was searched in all cached texts after normalizing whitespace, curly quotes and hyphen variants (`/tmp/quotecheck.py`). Results:

| Where | Strings | Exact match | Notes |
|---|---|---|---|
| business.md (all sections) | 37 | 37 | The two-word fragments ("the metaverse", "double digits") also match. "supply constrained" (b:65) matches the follow-up call l.171 and the corrected main-call text |
| outlook.md §2–§3 | 12 | 11 | One is the corrected p.21 quote (below) |
| outlook.md §4 guidance (8 bullets) | 8 | 8 | Release p.2 l.53–68 word for word, including "lower-end" and "$61-64 billion"; 2027 capex "we aren't providing a specific outlook for 2027 CapEx at this time." at call l.517 (curly apostrophe preserved); RL sentence at `10-Q` l.996 |
| outlook.md §5 claim quotes (11) | 11 | 10 | One is the corrected p.21 quote |
| **Corrected quote** (o:23 and o:64; b:65) | "we are today, and expect to be in the sort of foreseeable future, supply constrained, and that really includes our core business, too" | as corrected | Transcript l.1045–1046 reads "...foreseeable future, supply1 constrained, and that really includes our core business, too, where there are --" with footnote l.1076 "Reflects correction of reference to "demand" during the earnings call." The draft uses the company's corrected word and drops the footnote marker; both Sources lists disclose this. **Accepted as PASS** per the review brief. |

No altered word found in any quote. The pilot's failure mode ("is" for "are") does not recur.

---

## 5. Claims check (outlook.md §5)

Count: **11** (target 6–12). Mix: claims 1–4 are headline guidance (revenue, capex ceiling, expense ceiling, operating income); 5–11 are fundamentals (headcount, business-agent pricing, RL loss statement, depreciation, RL revenue, open-source release, supply constraint). Balance is right. Every claim has its verbatim quote and tag beneath it.

| # | Single direction? | Can it fail? | One thing to check? | Quote supports it? | Sharpening / disclosure labels | Verdict |
|---|---|---|---|---|---|---|
| 1 | Yes (in range) | Yes | Yes (Q3 revenue) | Yes | n/a | OK |
| 2 | Yes | Yes (top lowered or raised = not kept) | Yes | Yes | n/a | OK. Note a *raise* of the top would grade as missed under the literal wording; if the writer means "not raised", say "keeps the top of the range at or below $145 billion" |
| 3 | Yes | Yes | Yes | Yes | n/a | OK, same note as 2 |
| 4 | Yes | Yes | Yes (9-month operating income vs $58.5B) | Yes | Labelled: "our year-to-date proxy from the 2025 quarterly figures, not management's number"; states nine months (YTD) | OK; $58.5B re-derived from slides p.4: 17,555 + 20,441 + 20,535 = 58,531. Jargon: "proxy" → "stand-in" (REVISE item 10) |
| 5 | Yes (below 71,500) | Yes | Yes (Q3 release headcount) | Yes | Labelled: "our sharpening: 75,472 minus half of about 8,000, ignoring hiring; not management's number" | OK |
| 6 | Yes | Yes (pricing delayed or reversed = missed; silence = dropped) | Yes | Yes | n/a | OK |
| 7 | Yes | Yes (statement softened or absent) | Yes (10-Q Item 2 wording) | Yes | Labelled "disclosure check, full-year wording" — it checks a sentence, not a quarter/YTD number, so the quarter-vs-YTD requirement is satisfied by "full-year" | OK |
| 8 | Yes (> $6.00B) | Yes | Yes (10-Q Note 6, three-month column) | Loosely ("driven by higher depreciation") | n/a; the threshold is a disclosed number | OK; states the three-month figure explicitly ("Q3 2026 depreciation ... exceeds Q2's $6.00 billion") |
| 9 | Yes (> $470M) | Yes | Yes (segment table) | Yes | n/a | OK |
| 10 | Yes | Yes | Yes | Partly: management said "at some point soon"; the claim fixes the horizon at the Q3 call | **Unlabelled sharpening** | **REVISE item 6**: add "(our sharpening of 'at some point soon', not management's date)" |
| 11 | Yes (says it again) | Yes (says constraint eased) | Yes | Yes | n/a | OK |

No either/or constructions, no double-barreled claims with an unobservable half, no vague statements presented as claims. Rubric Q4 passes.

---

## 6. Jargon audit

### (a) Terms found that were neither plain, name-inferable, nor in the glossary — and what was done

| File:line (pre-edit) | Term | Status |
|---|---|---|
| business.md:40 | "Capex" in the table label, used 19 lines before its definition at line 59 | FIXED: label now "Capex (capital spending) incl. finance-lease principal" |
| business.md:42 | "Depreciation & amortization" (amortization undefined) | FIXED: label now adds "the yearly expense from past capex" |
| business.md:57 | "Horizon" | FIXED: "(Meta's virtual-reality software platform)" |
| business.md:61 | "R&D" | FIXED: spelled out |
| business.md:63 | "balance sheet" (heading and body) | FIXED: heading now "(the list of what Meta owns and owes)" |
| business.md:65 | "supply constrained" (quote) | FIXED: "(short of computing capacity)" outside the quote |
| business.md:86, 120, 133 | "vest / vesting" | FIXED in the RSU glossary entry: 'delivered ("vested") to an employee over time' |
| business.md:100 | "selling compute" | FIXED: "(computing capacity)" |
| business.md:102 | "injunctions" | FIXED: "(court orders)" |
| business.md:112 | "receivables" | FIXED: "(money owed by customers)" |
| business.md:120 | "stock options", "weighted-average exercise price" | FIXED: "(rights to buy a share at a fixed price)", "(that fixed price)" |
| business.md:132 | "income statement" | FIXED: "(the profit-and-loss report)" |
| outlook.md:21 | "APIs", "compute" inside a quote | FIXED: gloss added after the tag |
| outlook.md:23 | "supply constrained" (quote); "open-source" | FIXED: glosses added outside the quote |
| outlook.md:27 | "basis point" (quote) | FIXED: "(a basis point is 0.01%)" |
| outlook.md:57 | "proxy" (= stand-in) in claim 4 | OPEN (claim wording; REVISE item 10) |

Already plain or glossed inline by the writer, no action: impression (b:6), cost of revenue / gross margin / operating margin (b:32), finance lease (glossary), residual value guarantee (glossary and inline), free cash flow (Meta's definition quoted), operating cash flow (table label), share-based compensation (table label), run-rate (o:29), token (o:33), model API (o:35), headwind (o:41), Class A/B votes (b:116), controlled company (b:116, explained by the preceding clause), "moat" (b:92; the owner's own framework word, used in AGENTS.md).

### (b) Glossary entries

Five entries (DAP, Finance lease, Residual value guarantee, RSU, Depreciation). Each is one sentence, each is used repeatedly in the argument, none is avoidable. **None should be cut; none needs adding** after the inline glosses above.

### (c) Banned-word scan outside quotes

Scanned for leverage, synergy, headwind, tailwind, monetize, ecosystem, at scale, robust, unlock. "monetize" occurs once, inside a 10-Q quote (b:24); "headwind" occurs in the release quote (o:43) with the writer's gloss at o:41. **None outside quotes.**

### (d) Paragraphs that are mostly numbers

business.md:63 ("Promised but not yet on the balance sheet") carries nine figures but each is explained in words and the paragraph is the report's most important; acceptable. business.md:102 (scenario 2) carries seven figures; acceptable for a litigation scenario. Neither is a wall. The §7 cash items are already a table.

---

## 7. Invented-number check

No figure was found without a source tag, and no tag fails to contain its figure. Specific checks requested:

| Item | Finding |
|---|---|
| Gross margin | Labelled "(computed)" in the table and explained in prose as computed because Meta does not report it. Inputs (revenue, cost of revenue) sourced. Correct. |
| Capex incl. finance-lease principal | FY2021, FY2022, FY2024 labelled "(computed)"; FY2023 ($28.10B), FY2025 ($72.22B) and Q2 2026 ($31.08B) are stated by Meta and correctly unlabelled. Arithmetic verified (§3(b)). Footnote basis wording needs one fix (REVISE item 3). |
| Zuckerberg voting % | 60.8% and 99.8% match DEF 14A l.1485 exactly. |
| Zuckerberg economic stake ~13.5% | Labelled "(computed)"; re-derived 13.49% from the proxy's share counts (l.1470, l.1485). Correct. "(computed)" is the report's standard label and suffices; no separate "our computation" wording needed. |
| RL loss figures | All from Note 16 / Note 15 / Note 12 / Q1 Note 11; verified. "about $19 billion a year", "about a fifth of the apps' profit" match. |
| FCF | Meta's stated FCF for all six periods (not computed); Q2 $784M matches release. |
| Commitments and leases (10-Q Note 9 / Note 5) | $278.99B, ~$68B, $349.31B, $53.52B, $81.65B, $12.31B, ~$28B, $46.03B, 20%, ~$27B, 2029 all verified; "$347 billion (computed)" = 278.99 + 68 labelled. |
| Litigation figures (Part II Item 1) | $6M, $375M, $953M, $62.85B, Aug 12, Sept 8, €200M all present; one mis-placed (item 43 above). |
| Shares and buybacks | 2,741M / 2,530M / 2,548M / 2,538M; $44.5B ... $0; $25.03B authorization; all verified. |
| Other computed cells | 98% advertising, 44%/24% geography, RL % of FoA, FCF/net income, capex/revenue, 57c/47c return on P&E, 10% China: all labelled and re-derived. |
| Unlabelled inferences | b:6 "almost none paying" (fair reading of $1.0B other revenue vs 3.6B users; acceptable). b:61 "Our inference: these costs are fixed..." labelled. b:136 "Our inference: ... raises the share count" labelled. o:23 "open-source releases are paused" is the writer's reading of "we expect that we will get back to releasing" (REVISE item 11, minor). b:118 "long-tenured insiders" (REVISE item 7). |
| Estimates presented as fact | None found. "not disclosed" used correctly for advertiser count (b:112). |

---

## 8. Company-specific coverage

- **Reality Labs losses**: §1 states the loss, §3 gives a five-year FoA/RL table with the loss as a share of FoA profit, quotes the 10-K on why RL exists and how long it may take, and the 2026 spending split. Clear and plain. Yes.
- **Capex program**: §3 explains what capex buys, why finance-lease principal is included (Meta's own words), the P&E build-up including construction in progress, the useful-life change, how capex turns into depreciation and then into the Q2 margin drop. Yes.
- **Finance leases, joint venture / residual value guarantees, leases not yet commenced**: all three in one paragraph (b:63) with plain-word explanations ("if Meta walks away it pays any shortfall against a guaranteed value"; "kept off Meta's balance sheet because Meta does not control the venture"), plus glossary entries for finance lease and RVG. Yes; the best treatment of off-balance-sheet exposure in the three reports so far.
- **Dual-class control in §7**: Class B ten votes, 99.8% / 60.8% / 13.5%, controlled-company status, the 10-K's own risk-factor sentence, and the board's rejection of Proposal Five. Yes.
- **Customer concentration per the filings**: no customer ≥10% (Note 1), 37% from US-based marketers (Note 1), the China-reseller risk factor, the last disclosed China figure (FY2023) and the fact that it has not been disclosed since. Yes; also notes "The number of advertisers is not disclosed."
- **Disruption scenarios**: five, ranked, each with what must happen, an early warning, and profit-pool exposure with a number. Yes.

---

## 9. Writer's flagged uncertainties — rulings

| Flag | Ruling |
|---|---|
| Proxy tag short forms "CD&A", "Security Ownership" | **Acceptable.** Both are expanded in the Sources list (b:167) and both headings exist in the cached proxy (l.726 "COMPENSATION DISCUSSION AND ANALYSIS"; l.1461 "Security Ownership of Certain Beneficial Owners and Management"). The other section tags used (Director Nominees and Executive Officers l.259, Corporate Governance l.400, Related Party Transactions l.639, Proposal Five l.1748) are printed headings. |
| FY2021 / FY2022 / FY2024 capex computed from two cash-flow lines | **Arithmetic verified, description wrong for two of three years.** FY2024 = 37,256 + 1,969 (cash-flow lines) = 39.2. FY2021 and FY2022 = 18,567 + 677 and 31,186 + 850, where 18,567 and 31,186 are the *net* purchases in the FY2023 10-K's Item 7 FCF reconciliation (l.1913), not the cash-flow statement's 18,690 and 31,431 (l.2261). The net basis is the right one (it is what Meta itself reported as capex in those years and what its FCF used), so keep the numbers and fix the footnote (REVISE item 3). |
| Zuckerberg ~13.5% economic stake computed from proxy share counts | **Verified**: 342,463,325 / 2,538,423,304 = 13.49%. The "(computed)" label is sufficient. |
| Indicator 5 bundles four figures | **Split it.** Leases-not-commenced and non-cancelable commitments are the primary early-warning numbers for scenario 1 and deserve their own row in the scorecard time series; a four-figure cell will be hard to read across eight quarters. To stay within 5–8 indicators, merge indicators 2 and 3 (impressions and price per ad are two halves of one identity, always reported together on release p.1). Net count stays 8. The owner decides at lock; the writer should implement so that outlook §1 keeps one row per indicator (REVISE item 5). |
| Outlook §1 RL "expected" cell cites the 10-K rather than the Q1 10-Q | **Both are valid**; the 10-K (Item 7 l.1451) is the original statement and gives the $19.19B, the Q1 10-Q (Item 2 l.926) repeats the sentence. Because the table's intro says "Expected" comes from Q1 2026 sources, I added `[10-Q Q1 2026, Item 2]` alongside the 10-K tag (verified). No writer action needed. |

---

## 10. Verdict: REVISE

Items 1–3 are factual; 4–6 make the indicator set and one claim usable by the refresh agent; 7–12 are precision.

1. **business.md:102 (scenario 2)** — The "second New Mexico trial from September 8" seeking "up to $62.85 billion" is the New Mexico Attorney General's **privacy / consumer-protection** case ("which has expanded to include various claims related to content moderation issues"), disclosed under "Privacy and Related Matters" (`10-Q-2026-Q2.txt` l.1431), not a youth-safety case. Either move it to "Other exposures" or keep it in scenario 2 but say what it is. Optionally add the youth paragraph's own ceiling: plaintiffs "could seek ... in certain cases up to more than a trillion dollars" (l.1489).
2. **business.md:108 (scenario 5)** — "Nvidia is not named" is false as written: NVIDIA appears in the proxy's compensation peer group (DEF 14A l.816). Reword to "Nvidia is not named as a supplier in any cached filing or call" (true: zero hits in the four financial filings, both transcripts, release and slides).
3. **business.md:44 footnote** — Replace "computed cells add the two cash-flow lines" with wording that matches what was done: FY2021 and FY2022 add the *net* purchases of property and equipment from the 10-K's FCF reconciliation (Item 7) to finance-lease principal; FY2024 adds the two cash-flow-statement lines. Tag the FY2023 10-K Item 7 for the former.
4. **business.md §8 indicator 4** — Drop "and the full-year RL loss statement". It is a management sentence, not a recurring disclosure, and it is already tracked as claim 7 (§8 of AGENTS.md).
5. **business.md §8 indicator 5 and outlook.md §1** — Split indicator 5 into (a) capex incl. finance-lease principal and capex/revenue, and (b) forward commitments: leases not yet commenced and non-cancelable contractual commitments (10-Q commitments note). Merge indicators 2 and 3 into "Ad impressions and average price per ad, y/y % change" to keep the count at 8. Rebuild the outlook §1 table with one row per resulting indicator. (Proposed set; owner locks.)
6. **outlook.md:63 claim 10** — Label the sharpening: "By the Q3 2026 call (our sharpening of 'at some point soon', not management's date), Meta has released at least one open-source model."
7. **business.md:118** — "the other named officers are long-tenured insiders" is true of the four other named executive officers in the pay tables (Li 2008, Cox 2005, Olivan 2007, Bosworth 2006) but two of the seven executive officers listed in the proxy joined in 2025–2026 (Dina Powell McCormick, President and Vice Chairman, l.342; C.J. Mahoney, Chief Legal Officer, l.366). Say which group is meant, or note the two newcomers.
8. **business.md:90** — "Facebook and Instagram each have more than 2 billion daily users" → "at least 2 billion" (transcript l.28–30: Instagram "reached 2 billion daily actives", Facebook "more than 2 billion").
9. **business.md:63** — "the partners fund about $27 billion of construction" → the venture's owners, Meta included at 20%, fund their pro-rata shares of about $27 billion (Note 5 l.590: "The parties have committed to fund their respective pro rata share of approximately $27 billion").
10. **outlook.md:57 claim 4** — "our year-to-date proxy" → "our year-to-date stand-in" (a reader who has just met the proxy statement in §7 will trip on the word).
11. **outlook.md:23** — "open-source releases are paused" is an inference from "we expect that we will get back to releasing some open source models"; either label it ("our reading:") or say "no open-source model has been released since Meta Superintelligence Labs was formed" only if a source states it, otherwise use management's own words.
12. **business.md:32** — "about 21,000 layoffs" is the sum of two disclosed figures (≈11,000 in 2022, ≈10,000 in 2023; Note 3 l.2616, l.2589). Add "(computed)" or give both figures.

Not required but worth considering: claims 2 and 3 grade a *raise* of the ceiling as "missed"; if the intent is capex discipline, "at or below $145 billion" says so.

---

## Fixed directly

Tags (source unambiguous, verified):
- outlook.md:13 — added `[10-Q Q1 2026, Item 2]` (l.926) to the RL "expected" cell alongside the existing 10-K tag, so the column's stated Q1-2026 basis holds.

Jargon replaced or glossed, meaning unchanged (no numbers, quotes, claims, indicators or structure touched):
- business.md:40 — table label "Capex incl. finance-lease principal ($B)" → "Capex (capital spending) incl. finance-lease principal ($B)".
- business.md:42 — table label "Depreciation & amortization ($B)" → "Depreciation & amortization ($B; the yearly expense from past capex)".
- business.md:57 — "VR and Horizon" → "VR and Horizon (Meta's virtual-reality software platform)".
- business.md:61 — "R&D 67%" → "research and development 67%".
- business.md:63 — heading "Promised but not yet on the balance sheet." → "... on the balance sheet (the list of what Meta owns and owes)."
- business.md:65 — added "(short of computing capacity)" after the "supply constrained" quote.
- business.md:100 — "selling compute" → "selling compute (computing capacity)".
- business.md:102 — "verdicts or injunctions" → "verdicts or injunctions (court orders)".
- business.md:112 — "revenue or receivables" → "revenue or receivables (money owed by customers)".
- business.md:120 — "20 million stock options to executives and employees at a weighted-average exercise price of $2,788" → "20 million stock options (rights to buy a share at a fixed price) to executives and employees at a weighted-average exercise price (that fixed price) of $2,788".
- business.md:132 — table label "... still to hit the income statement" → "... still to hit the income statement (the profit-and-loss report)".
- business.md:156 (Glossary, RSU) — "delivered to an employee over time" → 'delivered ("vested") to an employee over time'.
- outlook.md:21 — added "(an API lets other companies' software use Meta's models; compute is computing capacity)" after the tag.
- outlook.md:23 — added "(supply constrained: short of computing capacity)" after the tag; "open-source releases are paused" → "open-source releases (models published for anyone to use) are paused".
- outlook.md:27 — added "(a basis point is 0.01%)" after the quote.

No typos found. All 73 quoted strings re-verified after the edits (68 exact, 5 short fragments exact, 2 accepted corrected-wording quotes).

Word counts after fixes (`/tmp/wc_prose.py`, §3 rule 7 basis): **business.md 2,533** (target 2,000–3,000; lower half), **outlook.md 1,026** (target 800–1,200; lower half).

As-of check: no information dated after 2026-07-30 found. The dates that appear (August 1 per-token pricing, August 12 and September 8 trial dates, September 30 claim horizon) are all forward-looking statements made in the cached call and 10-Q.


---

## Cycle 2 (re-check of the writer's second pass, 2026-09-07)

_Same as-of rule observed: nothing outside `sources/2026-Q2/` was opened. Line numbers refer to the revised drafts and the cached `.txt` files. This is the second and last review cycle allowed by AGENTS.md §13._

### 1. REVISE list — resolution

| # | Item | Status |
|---|---|---|
| 1 | $62.85B New Mexico trial mis-placed under youth-safety | **Resolved.** Removed from scenario 2 (business.md:102) and now a separate sentence under "Other exposures" (business.md:110): "A separate New Mexico Attorney General case over privacy and consumer protection, since widened to content-moderation claims, goes to trial on September 8, 2026, with the state seeking 'up to $62.85 billion in penalties' [10-Q Q2 2026, Part II Item 1]." Verified against `10-Q-2026-Q2.txt` l.1431 (the "Privacy and Related Matters" paragraph, which frames the state-AG cases as arising from "platform and user data practices" and cites a consumer-protection settlement with California; "which has expanded to include various claims related to content moderation issues"; "intend to seek up to $62.85 billion in penalties in this case"). Characterization and quote fragment both PASS. |
| 2 | "Nvidia is not named" false | **Resolved.** business.md:108 now: "The only chip supplier named in any cached filing or call is Broadcom, paid about $2.3 billion in 2025; Nvidia is not named as a supplier anywhere and appears only in the proxy's pay peer group [DEF 14A 2026, Related Party Transactions] [DEF 14A 2026, CD&A]." Re-checked: Broadcom $2.3B at DEF 14A l.647; NVIDIA only at l.816 ("Peer Group ... NVIDIA (NVDA)"), which sits inside the CD&A (heading l.726; next top-level heading after the peer-group section is "PERQUISITES AND OTHER BENEFITS" l.936), so the new CD&A tag is right; zero hits for Nvidia in the four financial filings, both transcripts, release and slides; also zero hits for Qualcomm, AMD, TSMC, Intel, Arm, Samsung, Micron, so "only chip supplier named" holds. PASS. |
| 3 | Capex footnote basis | **Resolved.** business.md:44 now: "Computed cells: FY2021 and FY2022 add the net purchases of property and equipment shown in the 10-K's free-cash-flow reconciliation to finance-lease principal [10-K FY2023, Item 7]; FY2024 adds the two cash-flow-statement lines [10-K FY2025, Item 8]." Matches `10-K-FY2023.txt` l.1913 (18,567; 31,186) and `10-K-FY2025.txt` l.2219/l.2233 (37,256; 1,969). PASS. |
| 4 | Indicator 4 bundled a one-off statement | **Resolved.** New indicator 3 (business.md:144) is "Reality Labs operating loss (quarter and year-to-date)" only; the full-year statement remains claim 7. |
| 5 | Indicator 5 four-figure bundle; keep count at 8 | **Resolved.** business.md:142–149: 1 DAP; 2 impressions and price per ad (two figures); 3 RL loss (quarter and YTD); 4 capex incl. finance-lease principal and capex/revenue; 5 forward commitments (leases not yet commenced; non-cancelable contractual commitments), sourced to the 10-Q "Leases and Contractual Commitments" note; 6 FCF (quarter and YTD); 7 operating margin total and FoA; 8 debt, shares, buybacks. Eight indicators, each anchored to a recurring disclosure. outlook.md:10–17 rebuilt with eight numbered rows in the same order (verified below). |
| 6 | Claim 10 unlabelled sharpening | **Resolved.** outlook.md:63: "By the Q3 2026 call (our sharpening of "at some point soon", not management's date), Meta has released at least one open-source model." |
| 7 | "long-tenured insiders" | **Resolved.** business.md:118: "the three other named executive officers (COO, CTO, Chief Product Officer) joined between 2005 and 2007, while two of the seven listed executive officers, the President and Vice Chairman and the Chief Legal Officer, arrived in 2025–2026". Verified against DEF 14A: Cox "Various other positions (2005-2009)" l.361; Bosworth "(2006-2017)" l.357; Olivan "Head of International Growth (2007-2011)" l.346; Powell McCormick "Advisor (2025-2026)", "President and Vice Chairman (2026-present)" l.342; Mahoney "Chief Legal Officer (2026-present)" l.366; seven executive officers listed l.268–366. PASS. |
| 8 | "more than 2 billion" for Instagram | **Resolved.** business.md:90 "each have at least 2 billion daily users" (transcript l.28–30). |
| 9 | JV funding wording | **Resolved.** business.md:63 "the owners, Meta included, fund about $27 billion of construction in proportion to their stakes" — matches Note 5 l.590 "The parties have committed to fund their respective pro rata share of approximately $27 billion in total estimated development costs". PASS. |
| 10 | "proxy" in claim 4 | **Resolved.** outlook.md:57 "our year-to-date stand-in". |
| 11 | "open-source releases are paused" inference | **Resolved.** outlook.md:23 now quotes management instead: "We plan to do a combination of open and closed models." and "we expect that we will get back to releasing some open source models at some point soon" [Q2 2026 call, p.16] [Q2 2026 call, p.18]. New quote verified word for word at `transcript.txt` l.923–924 (p.18 = l.890–940). PASS. |
| 12 | "about 21,000 layoffs" | **Resolved.** business.md:32 "layoffs of about 11,000 people announced in 2022 and about 10,000 in 2023" — `10-K-FY2023.txt` Note 3 l.2616 ("a layoff of approximately 11,000 employees") and l.2589 ("approximately 10,000 employees"). PASS. |

12 of 12 resolved. The optional suggestion on claims 2 and 3 was also taken: outlook.md:55–56 now read "keeps the top of the 2026 capex range at or below $145 billion" / "at or below $169 billion" — single direction (a raise is missed, silence is dropped), gradeable.

### 2. Cycle-1 direct edits — all intact

All 16 glosses and the added tag survived the rewrite: business.md:40 (capex label), :42 (D&A label), :57 (Horizon), :61 (research and development spelled out), :63 (balance sheet), :65 (supply constrained), :100 (compute), :102 (injunctions), :112 (receivables), :120 (stock options / exercise price), :132 (income statement), :156 ("vested"); outlook.md:21 (API / compute), :23 (supply constrained; the open-source gloss now reads "on open-source models (models published for anyone to use)"), :27 (basis point); outlook.md:12 carries `[10-Q Q1 2026, Item 2]` on the RL "expected" cell (moved from row 4 to row 3 with the re-ordering).

### 3. New or changed numbers and quotes

| Item (file:line) | Tag | Found | Result |
|---|---|---|---|
| "in certain cases up to more than a trillion dollars" (business.md:102) | 10-Q Part II Item 1 | `10-Q-2026-Q2.txt` l.1489 "including in certain cases up to more than a trillion dollars" | PASS |
| "up to $62.85 billion in penalties"; September 8, 2026; content-moderation claims (business.md:110) | 10-Q Part II Item 1 | l.1431 | PASS |
| Nvidia / peer group / Broadcom $2.3B (business.md:108) | DEF 14A Related Party Transactions; CD&A | l.647; l.816 | PASS |
| Capex footnote figures (business.md:44) | 10-K FY2023 Item 7; 10-K FY2025 Item 8 | l.1913; l.2219, 2233 | PASS |
| Officer tenures (business.md:118) | DEF 14A Director Nominees and Executive Officers | l.342, 346, 353, 357, 361, 366 | PASS |
| JV pro-rata funding (business.md:63) | 10-Q Note 5 | l.590 | PASS |
| Layoffs ~11,000 (2022) and ~10,000 (2023) (business.md:32) | 10-K FY2023 Note 3 | l.2616; l.2589 | PASS |
| "We plan to do a combination of open and closed models." (outlook.md:23) | call p.18 | l.923–924 | PASS |
| Trimmed sentence business.md:61 ("Q2's 31% previews it") | release p.1 | l.17 | PASS (the dropped legal/severance parenthetical is still covered at l.102 and in the §4 table context) |
| Trimmed outlook.md:31 (other revenue $1.0B, +73%) | call p.5; follow-up p.3 | l.210–211; l.138 | PASS |
| Trimmed outlook.md:35 (API gloss moved to :21) | call p.2, p.8 | l.80, 96; l.379–384 | PASS |

**Rebuilt outlook §1 table (lines 10–17) — every cell:**

| Row | Q2 2026 cell | Q1 2026 cell | Expected | Result |
|---|---|---|---|---|
| 1 DAP | 3.60B, +3% (release l.24) | 3.56B, +4% (Q1 release l.32) | No guidance | PASS |
| 2 Impressions; price | +14%; +12% (release l.25–26) | +19%; +12% (Q1 release l.35–36) | No guidance | PASS |
| 3 RL loss quarter; YTD | $4.62B; $8.65B (release p.8 l.330: 4,619; 8,647) | $4.03B; $4.03B (Q1 release p.8 l.330: 4,028) | "to remain similar to 2025" ($19.19B) — 10-K Item 7 l.1451; 10-Q Q1 Item 2 l.926 | PASS |
| 4 Capex; capex/revenue | $31.08B; 51% (release l.32; 31,078/60,801 = 51.1%) | $19.84B; 35% (Q1 release l.39; 19,840/56,311 = 35.2%) | "$125-145 billion" (Q1 release l.64) | PASS |
| 5 Leases not commenced; commitments | $278.99B; $349.31B (10-Q Note 9 l.682, 684) | $182.88B; $237.67B (10-Q Q1 Note 8 l.620, 622) | No guidance | PASS |
| 6 FCF quarter; YTD | $784M; $13.17B (release l.37; p.9 l.362: 13,170) | $12.39B; $12.39B (Q1 release l.43; p.9: 12,386) | No guidance | PASS |
| 7 Operating margin total; FoA | 31%; 39% (release l.17; 23,394/60,370 = 38.8%) | 41%; 48% (Q1 release l.17; 26,900/55,909 = 48.1%) | "above 2025 operating income"; "$162-169 billion" (Q1 release l.62, 60) | PASS |
| 8 Debt; shares; buybacks | $83.66B; 2,548M; $0 (release l.36; 10-Q l.188, 334) | $58.75B; 2,538M; $0 (Q1 release l.226; 10-Q Q1 l.188, 321) | No guidance | PASS |

36/36 cells PASS; row order matches business.md §8; each row's disclosure recurs every quarter.

### 4. Claims — §9 rules, final wording

Eleven claims. Claims 2 and 3 now single-direction "at or below" ceilings; claim 4 says "stand-in" and keeps its label; claim 5 keeps its label; claim 7 is labelled a disclosure check with "full-year wording"; claim 10 now carries "(our sharpening of "at some point soon", not management's date)". No either/or constructions, no double-barreled claims, every quote verbatim and tagged. Rubric Q4: yes.

### 5. Verbatim-quote check, word counts, as-of

- Quoted strings in both files re-searched across all cached texts: **74 strings, 72 exact matches**, plus the two "supply constrained" quotes that correctly use the company's p.21 corrected wording (accepted). No altered word.
- Word counts (`/tmp/wc_prose.py`, §3 rule 7 basis): **business.md 2,607** (target 2,000–3,000), **outlook.md 1,035** (target 800–1,200). Both pass; both in the lower half or at the midpoint.
- As-of: no information dated after 2026-07-30. Dates present (October 2025 venture; August 1 per-token pricing; August 12 and September 8 trial dates; September 30 claim horizon) are all from the cached call, 10-Q and follow-up call as forward-looking statements.
- Skeleton: all headings present and in order in both files; `_Proposed — owner to review and lock._` at business.md:140; Tone shift omitted; 8 indicators, 8 outlook rows; every tag family used maps to a Sources entry (business.md 9, outlook.md 8).
- Jargon: no new unglossed term introduced by the rewrite ("content-moderation claims", "pay peer group", "pro rata" avoided in favour of "in proportion to their stakes"). Rubric Q5 now a clean yes.
- Typos: none found (doubled-word and double-space scan clean).

### 6. Fixed directly, cycle 2

None needed.

### Final verdict: **PASS**

Nothing remains open for the writer. For the owner, two notes rather than defects: (a) the proposed indicator set changed between cycles (impressions and price merged; capex and forward commitments split) and is ready for the lock review; (b) the 10-Q itself states both an aggregate ceiling of "hundreds of billions of dollars" (l.1417) and, for the youth cases alone, "in certain cases up to more than a trillion dollars" (l.1489); business.md:102 now quotes both, which is the honest thing to do with an internally inconsistent source.
