# Intel Corporation (INTC) — Reviewer report, Q2 2026 (quarter ended June 27, 2026)

_Reviewed 2026-09-07 against `sources/2026-Q2/` only (as-of cutoff 2026-07-24). Files reviewed: `business.md` (2,771 prose words before fixes, 2,929 after), `outlook.md` (1,200 before, 1,199 after). Line numbers below refer to the cached `.txt` files; `p.N` on the two transcripts and the slides means PDF page N (the Nth form-feed block), as both drafts' Sources lists state._

**Final verdict (after cycle 2): PASS.** All 11 REVISE items were applied and re-verified against the cached text; see "## Cycle 2" at the end. One minor wording imprecision the reviewer missed in cycle 1 (§4 "until Q2 2026, earned no operating profit on them") is recorded there as an open note for the owner; it does not change any number.

**Cycle 1 verdict: REVISE (one cycle; small list).** Citation spot-check: 114 items checked, 110 PASS, 2 FAIL, 2 UNVERIFIABLE. Every number in the §2, §3 and §4 tables, every cell of the outlook indicator table, every guidance quote and every claim quote traces to the cached text; every "(computed)" cell re-derives. What needs the writer: one overstated sentence in §1 ("most of the world's PCs"), one factory-count slip in §3, two unlabelled inferences in the segment-table footnotes (IMS move, NAND), one claim (#6) that hardens "roughly" into a ceiling without saying so, one misleading "Not guided" item, and a handful of label and wording nits. Jargon was fixed directly (list at the end).

---

## 1. Skeleton compliance

**business.md**

| Requirement (§6) | Result |
|---|---|
| `# <Company> — The Business` | OK: "# Intel Corporation — The Business" |
| `_As of <QLABEL>. Written <date>._` with period parenthetical on first use (§5) | OK: "_As of Q2 2026 (quarter ended June 27, 2026). Written 2026-09-07._" |
| §1–§8 headings present, in order, none skipped | OK. §1 has the history paragraph; §6 carries customer concentration (#4); §8 has name / why / where |
| §2 segment table, 5 fiscal years | OK: FY2021–FY2025 plus Q2 2026, three bases kept separate with footnotes (see §5c below for the footnote wording) |
| §3 table: revenue, gross margin, operating margin, capex, capex/revenue, 5 years | OK, plus non-GAAP gross margin and R&D % rows |
| §4 table, 5 years | OK (cash-flow bridge to Intel's adjusted free cash flow, plus SBC, depreciation, amortization, dividends, buybacks) |
| §8 marked `_Proposed — owner to review and lock._` | OK, exact |
| Glossary | OK (10 entries after the reviewer added "Amortization") |
| Sources | OK. Every tag prefix used in the body maps to a cached file; the transcript and slides rows state the PDF-page convention. Nit: the `[Q2 2026 slides, p.N]` row is listed but no slides tag is used anywhere in the body |
| Length 2,000–3,000 prose words | OK: 2,929 after fixes (upper half of range; the writer's REVISE fixes should be word-neutral) |

**outlook.md**

| Requirement (§7) | Result |
|---|---|
| `# <Company> — Outlook as of <QLABEL>` | OK: "# Intel Corporation — Outlook as of Q2 2026 (quarter ended June 27, 2026)" |
| `_Transcript source tier: … Written <date>._` | OK: "company-published (prepared remarks only; Q&A not available)", matches MANIFEST tier 1 wording |
| §1 table: one row per §8 indicator; columns this quarter / last quarter / what management had said | OK: 8 rows matching §8 exactly, one comparison value per cell, "No guidance" where none |
| §2, §3, §4 (verbatim guidance), §5 | OK |
| §6 Tone shift omitted on first run | OK, correctly omitted |
| Sources with PDF-page convention | OK (transcripts and slides). Same unused-slides-row nit as above |
| Length 800–1,200 prose words | OK: 1,199 after fixes (1,200 before) |

---

## 2. Length (§3 rule 7 method, shared counter `/tmp/intc-orch/wc_prose.py`)

| File | Before reviewer fixes | After reviewer fixes | Target |
|---|---|---|---|
| business.md | 2,771 | 2,929 | 2,000–3,000 |
| outlook.md | 1,200 | 1,199 | 800–1,200 |

The outlook glosses (+24 words) were offset by removing two items from "Not sharpenable" that already sit in §4 "Not guided" (−14) and by tightening five phrases without changing meaning (−11). Details under "Fixed directly".

---

## 3. Rubric (§14), from the reader's chair

1. **What the company does and who pays, in two sentences?** Yes. §1–§2: Intel designs the CPUs in PCs and servers and, unlike rivals, owns the factories; PC makers, distributors, cloud companies and server makers pay per chip, and the factory business is almost entirely Intel paying itself.
2. **What would kill it and the early warning?** Yes. §6 is ranked, each scenario has a named warning sign anchored to a filing line (Foundry loss, outside revenue, 14A dates, server prices, client volume, region table, litigation note).
3. **Why the margins are what they are and whether cost scales with usage?** Yes. §3 explains two fixed-cost structures, the node cost curve, and idle-capacity depreciation, all with 10-K quotes; the reviewer added a one-sentence definition of gross vs operating margin that was missing.
4. **Could I predict next quarter's scorecard from §5 alone?** Yes, for 10 of 11 claims. Claim 6 is gradeable but hardens "roughly $16.5 billion" into "$16.5 billion or lower" without saying so (see §6).
5. **Did nothing require knowledge I don't have?** Before fixes, no: GPUs, TSMC, Arm, goodwill, write-downs, receivables, dilution, CHIPS Act, say-on-pay, vesting, S&P 500, bridge loan, notes, maturities, inference, edge, backlog, sequentially and basis points were all bare. After the direct fixes below, yes.

---

## 4. Citation spot-check

Legend: PASS / FAIL / UNVERIFIABLE. Every "(computed)" cell was re-derived from the cited inputs.

### 4a. business.md §2 revenue table and its footnotes

| # | Cell(s) | Tag | Found at | Result |
|---|---|---|---|---|
| A1 | CCG/CCPG 32,305 / 33,346 / 32,228 | [10-K FY2025, Note 3] | 10-K-FY2025.txt L2225, L2218, L2211 | PASS |
| A2 | DCAI 15,980 / 16,125 / 16,919 | same | same lines | PASS |
| A3 | Intel Products 48,285 / 49,471 / 49,147 | same | same lines | PASS |
| A4 | Intel Foundry 18,504 / 17,317 / 17,826 | same | same lines | PASS |
| A5 | Foundry from outside customers 547 / 159 / 307 | same | L2170: "totaled $307 million in 2025, $159 million in 2024 and $547 million in 2023" | PASS |
| A6 | All other 5,463 / 3,601 / 3,563 | same | L2225, L2218, L2211 | PASS |
| A7 | Eliminations (18,024) / (17,288) / (17,683) | same | same lines | PASS |
| A8 | Q2 2026 column 8,877 / 6,262 / 15,139 / 5,765 / 293 / 701 / (5,477) / 16,128 | [10-Q Q2 2026, Note 2; Item 2] | 10-Q-2026-Q2.txt L515 (segments), L1244 ("External revenue was $293 million"); release L395 agrees | PASS |
| A9 | FY2024 basis CCG 31,773 / 29,258 / 30,290; DCAI 16,856 / 12,635 / 12,817; NEX 8,409 / 5,774 / 5,842 | [10-K FY2024, Note 3] | 10-K-FY2024.txt L2317, L2308, L2299 | PASS |
| A10 | FY2024 basis Foundry 27,491 / 18,910 / 17,543; outside 474 / 953 / 385 | same | same lines; L2256: "$385 million in 2024, $953 million in 2023, and $474 million in 2022" | PASS |
| A11 | FY2024 basis All other 5,530 / 5,608 / 3,824; eliminations (27,005) / (17,957) / (17,215) | same | same lines | PASS |
| A12 | FY2023 basis CCG 41,081 / 31,773 / 29,258; DCAI 22,774 / 19,445 / 15,521; NEX 7,665 / 8,409 / 5,774; Mobileye 1,386 / 1,869 / 2,079; IFS 347 / 469 / 952; All other 5,771 / 1,089 / 644 | [10-K FY2023, Note 3] | 10-K-FY2023.txt L2443–L2448 | PASS |
| A13 | Totals 79,024 / 63,054 / 54,228 / 53,101 / 52,853 / 16,128 | Items 8 | 10-K-FY2023 L2449; 10-K-FY2025 L1750; 10-Q L215 | PASS |
| A14 | Footnote ¹ "NEX folded into CCG and DCAI from Q1 2025, prior years recast" | [10-K FY2025, Note 3] | L2140: "In the first quarter of 2025, we made an organizational change to integrate our NEX business into CCG and DCAI … All prior period segment data have been retrospectively adjusted" | PASS |
| A14' | Footnote ¹ "IMS moved from Foundry to All other" | [10-K FY2025, Note 3] | Not stated. FY2025 Note 3 lists "our IMS business" inside All other (L2178) and mentions only "certain other business reorganizations" (L2140); the FY2024 Note 3 All other names Altera and Mobileye, not IMS (L2262); the FY2023 10-K books mask-writer tool sales in IFS (L991). A move is the natural reading but no filing says it | **UNVERIFIABLE (inference, unlabelled)** |
| A15 | Footnote ² "Foundry model from Q1 2024, earlier years recast; NEX still a segment" | [10-K FY2024, Note 3] | L2240, L2244 | PASS |
| A16 | Footnote ³ "FY2021 All other includes the NAND business later sold" | [10-K FY2023, Note 3] | L2417–L2427 say All other includes "historical results of operations from divested businesses"; NAND is named as divested elsewhere (L133, L431) but the note does not name it | **UNVERIFIABLE (inference, unlabelled)** |
| A17 | "$953 million versus $547 million for 2023 … do not reconcile them" | [10-K FY2024, Note 3; 10-K FY2025, Note 3] | L2256 vs L2170; neither text reconciles | PASS (stated, not resolved, as required) |
| A18 | "Intel redrew its segments in 2023, 2024 and 2025" | three Notes 3 | 10-K-FY2023 L2397 (AXG folded into CCG/DCAI in Q1 2023); FY2024 L2240; FY2025 L2140 | PASS |

### 4b. business.md §2 segment operating income table

| # | Row | Tag | Found at | Result |
|---|---|---|---|---|
| B1 | CCG/CCPG 10,128 / 11,594 / 9,317 / 2,343 | [10-K FY2025, Note 3]; [10-Q Q2 2026, Note 2] | L2227, L2220, L2213; 10-Q L517 | PASS |
| B2 | DCAI 945 / 1,414 / 3,422 / 2,474 | same | same | PASS |
| B3 | Intel Foundry (7,083) / (13,291) / (10,318) / (2,089) | same | same | PASS |
| B4 | All other 1,507 / (57) / 264 / 230 | same | same | PASS |
| B5 | Corporate unallocated (5,199) / (11,177) / (5,518) / (1,416) | same | same | PASS |
| B6 | Eliminations (205) / (161) / 619 / 254 | same | same | PASS |
| B7 | Total 93 / (11,678) / (2,214) / 1,796 | same | same | PASS |

### 4c. business.md §3 economics table and prose

| # | Row / sentence | Tag | Found at | Result |
|---|---|---|---|---|
| C1 | Revenue row | as A13 | as A13 | PASS |
| C2 | Gross margin GAAP 55.4 / 42.6 / 40.0 / 32.7 / 34.8 / 39.9 | Items 7 | 10-K-FY2023 L1295; 10-K-FY2024 L915; 10-K-FY2025 L869; 10-Q L1302 | PASS |
| C3 | Gross margin non-GAAP 58.1 / 47.3 / 43.6 / n/s / 36.7 / 41.0 & 41.8 | 10-K FY2023 Item 7; DEF 14A; releases | 10-K-FY2023 L1301; FY2024 figure genuinely absent from the sources; DEF14A L1296 "non-GAAP gross margin percentage (36.7%)"; Q1 release L433; Q2 release L460 | PASS |
| C4 | R&D % 19.2 (computed) / 27.8 (computed) / 29.6 / 31.2 / 26.1 / 22.7 (computed) | Items 7 | 10-K-FY2023 L1006 prints 19.2% and 27.8%; 10-K-FY2025 L870; 10-Q L1303 prints 22.7% | PASS on numbers. **Label nit:** the three "(computed)" cells are printed in the filings, so the label is unnecessary (harmless) |
| C5 | Operating margin GAAP 24.6 (computed) / 3.7 (computed) / 0.2 / (22.0) / (4.2) / (4.5) | Items 7 | 19,456 / 79,024 = 24.62 (10-K-FY2023 L2457, L2449); 2,334 / 63,054 = 3.70 (also printed, 10-K-FY2024 L919); 10-K-FY2025 L873; 10-Q L1306 | PASS |
| C6 | Gross capex 18,733 / 24,844 / 25,750 / 25,122 / 17,672 / 7,615 | Items 8; footnote "sums computed" | 10-K-FY2023 L2126 (no financing-additions line in that 10-K); 25,122 = 23,944 + 1,178 (10-K-FY2025 L1860 + L1873; FY2024 10-K L527 confirms "$25.1 billion"); 17,672 = 14,646 + 3,026 (same lines); 7,615 = 6,192 + 1,423 (10-Q L330 + L345) | PASS |
| C7 | Capex / revenue 23.7 / 39.4 / 47.5 / 47.3 / 33.4 / 25.6 (computed) | — | recomputed 23.71 / 39.40 / 47.48 / 47.31 / 33.44 / 25.64 | PASS |
| C8 | Prose: R&D $13.8B, 26% of revenue; "high fixed cost structure …"; "higher depreciation costs and lower yields"; "increased mix of higher-cost wafers manufactured on our Intel 18A process node"; $34.5B construction in progress; "unfavorably affected"; "higher yields, improved cycle times and increased factory scale" | [10-K FY2025, Item 7; Item 1A; 10-Q Item 2; Q2 call p.4] | L870; L1241; L1235; 10-Q L1250 (Foundry operating loss summary); L909; L909; transcript p.4 L218 | PASS, all verbatim |
| C9 | "39% to 48% … then fell to 33%"; "shell ahead"; "a more disciplined capital deployment strategy"; $6.7B of capital-related incentives in 2025; "more than $20 billion"; "significantly above the 2026 levels" | [10-K FY2025, Item 1; Note 6; Q2 call p.5] | C7; L506; L506; L2435 (Note 6 spans L2384–L2477); transcript p.5 L257, L260 | PASS |
| C10 | "most of Intel's depreciation sits in Foundry" | [10-K FY2025, Note 3] | L2190 region: "the substantial majority of our consolidated depreciation expense was incurred by Intel Foundry in 2025, 2024 and 2023" | PASS |
| C11 | "Brookfield in Arizona and Apollo in Ireland, paid for 49% of two factories" | [10-K FY2025, Note 4] | 10-Q Note 3 L564–565 (49% each) but Arizona SCIP is "two new chip factories" (10-Q L600) plus Fab 34 in Ireland = three factories, or two projects | **FAIL (wording):** "two factories" undercounts; say "two factory projects (Fab 34 in Ireland; two new fabs in Arizona)" |

### 4d. business.md §4 cash table and prose

| # | Row / sentence | Tag | Found at | Result |
|---|---|---|---|---|
| D1 | Net income attributable 19,868 / 8,014 / 1,689 / (18,756) / (267) / (14,761) | Items 8 | 10-K-FY2023 L2170, L2178, L2186; 10-K-FY2025 L1764; 10-Q L229 | PASS |
| D2 | Operating cash flow 29,456 / 15,433 / 11,471 / 8,288 / 9,697 / 8,102 | same | 10-K-FY2023 L1316; 10-K-FY2025 L1858; 10-Q L328 | PASS |
| D3 | Gross capex | as C6 | | PASS |
| D4 | Government capital incentives 166 / 246 / 1,011 / 1,936 / 1,577 / 167 | same | 10-K-FY2023 L2128; 10-K-FY2025 L1861; 10-Q L331 | PASS |
| D5 | Partner contributions net — / 874 / 1,511 / 12,671 / 4,891 / (10,257) (computed) | same; [10-K FY2025, Note 4]; [10-Q, Note 3] | 10-K-FY2023 L2140 (874; 1,511; no distributions in those years, confirmed 10-K-FY2025 L2275); 12,714 − 43 (L1871, L2280); 5,108 − 217 (L1871, L2285); 4,082 − 14,339 (10-Q L343–L344) | PASS |
| D6 | Payments on finance leases — / (345) / (96) / (1) / (105) / (832) | same | 10-K-FY2023 L2139; 10-K-FY2025 L1027; 10-Q L342 | PASS |
| D7 | Adjusted free cash flow 10,889 / (4,075)* / (11,853) / (2,228) / (1,612) / (10,435) | Items 7; releases | 10-K-FY2023 L1320; 10-K-FY2025 L1028; (2,016) + (8,419) (Q1 release L483; Q2 release L510); cross-check 8,102 − 7,615 + 167 − 10,257 − 832 = −10,435 | PASS |
| D8 | Stock-based compensation 2,036 / 3,128 / 3,229 / 3,410 / 2,434 / 1,307 | same | 10-K-FY2023 L2110; 10-K-FY2025 L1842; 10-Q L313 | PASS |
| D9 | Depreciation 9,953 / 11,128 / 7,847 / 9,951 / 10,757 / 5,891 | same | 10-K-FY2023 L2109; 10-K-FY2025 L1841; 10-Q L312 | PASS |
| D10 | Amortization of acquired intangibles 1,839 / 1,907 / 1,755 / 1,428 / 949 / 469 | same | 10-K-FY2023 L2112; 10-K-FY2025 L1844; 10-Q L315 | PASS |
| D11 | Dividends paid (5,644) / (5,997) / (3,088) / (1,599) / — / — | same | 10-K-FY2023 L2146; 10-K-FY2025 L1879 | PASS |
| D12 | Share buybacks (2,415) then none | same; Item 5; 10-Q Part II Item 2 | 10-K-FY2023 L2145; 10-K-FY2025 L1598 ("last share repurchase … Q1 2021"); 10-Q L1568 | PASS |
| D13 | Footnote: FY2022 adds back $4,561M McAfee sale | [10-K FY2023, Item 7] | L1319 "Sale of equity investment | — | 4,561" | PASS |
| D14 | Prose: Apollo $11.0B; "added $12.7 billion"; "$10.3 billion outflow (computed)"; "$8.1 billion roughly covered gross capex of $7.6 billion (computed)" | [10-K FY2025, Note 4; 10-Q Note 3; Q2 release] | L2294 (Note 4); D5; 4,082 − 14,339 = −10,257; release L354, L356 + L371 | PASS |
| D15 | Escrow paragraph: $1.8B operating income, $(11.0)B net loss, $(2.16); 159M shares at $20.00; liability $2.7B → $15.6B; $12.5B loss "driven by an increase in our stock price"; 143M remaining; SEC staff, December 2025; non-GAAP $2.2B / $0.42 | [Q2 release; 10-K FY2025, Item 7; Note 5; 10-Q Q1 Note 4; 10-Q Q2 Note 4; Item 2] | release L256, L263, L265; 10-K L662; 10-Q Q1 L585 ($2.7B), 10-Q Q2 L631 ($15.6B), L1133 (quote, Item 2); L633 (143M); 10-K L2370 (Note 5 spans L2320–L2383: "In December 2025, the staff completed its review … objected"); release L487, L504 | PASS |
| D16 | "$105.7 billion of factories and equipment" | [10-Q Q2 2026, Item 1] | L273 (105,741) | PASS |

### 4e. outlook.md §1 indicator table (every number)

| # | Cell(s) | Tag | Found at | Result |
|---|---|---|---|---|
| E1 | Row 1: $(2,089)M; $(2,437)M; "we expect Intel Foundry's operating loss to improve through the year as 18A continues to ramp into volume and yields improve further" | [10-Q Q2, Note 2]; [10-Q Q1, Note 2]; [Q1 call, p.4] | 10-Q Q2 L517; 10-Q Q1 L478; transcript-Q1 p.4 L205–L206 | PASS |
| E2 | Row 2: $293M; $174M | Items 2 | 10-Q Q2 L1244; 10-Q Q1 L1182 | PASS |
| E3 | Row 3: $6,262M; 40%; $5,052M; 31%; "sequential revenue growth in both CCG and DCAI on improved supply and a full quarter of pricing actions, with DCAI up double digits" | Notes 2; Items 2; [Q1 call, p.5] | 10-Q Q2 L1178, L1181 ("Operating margin % | 26% | 40%"); 10-Q Q1 L1125, L1128 ("33% | 31%"); transcript-Q1 p.5 L238–L240 | PASS |
| E4 | Row 4: $8,877M; 26%; $7,727M; 33% (reported as CCG) | same | same tables | PASS |
| E5 | Row 5: 41.8% vs 39.0% guided; 41.0%, "approximately 650 basis points ahead of guidance"; "Gross margin … 39.0%" | releases; [Q1 call, p.3] | Q2 release L460; Q1 release L96 ("Gross margin | 37.5% | 39.0%"); Q1 release L433; transcript-Q1 p.3 L138–L139 | PASS |
| E6 | Row 6: $2,652M; $(8,419)M; $4,963M; $(2,016)M; "flat to last year"; "roughly equal across the year"; "excluding the buyout of the Fab 34 joint investment, we still expect positive adjusted free cash flow for the full year" | releases; [Q1 call, p.5; p.6] | Q2 release L506, L510; Q1 release L479, L483; transcript-Q1 p.5 L265, L267–L268; p.6 L281–L282 | PASS |
| E7 | Row 7: $29,727M; $50,537M (computed); $32,789M; $45,031M (computed); "approximately $7.7 billion in cash and $6.5 billion in new debt"; "retiring all $2.5 billion of maturities as they come due this year" | Items 1; [Q1 call, p.6] | 12,874 + 16,853 (10-Q Q2 L267–L268); 1,988 + 48,549 (L283, L286); 17,247 + 15,542 (10-Q Q1 L267–L268); 2,004 + 43,027 (L283, L286); transcript-Q1 p.6 L282–L284 | PASS, all four sums exact |
| E8 | Row 8: 143M; $15.6B; 149M; $3.6B | Notes 4 | 10-Q Q2 L631, L633; 10-Q Q1 L585, L587 | PASS |
| E9 | Note under table: $14.2B; "Partner contributions, net" $(12,216)M | [Q2 release; 10-Q Note 3] | 10-Q L594; release L508 | PASS |

### 4f. outlook.md §4 guidance quotes (word-for-word, curly quotes and line breaks normalised)

| # | Quote (abridged) | Tag | Found at | Result |
|---|---|---|---|---|
| F1 | "Revenue | $15.8-16.8 billion"; "Gross margin | 41.0% | 42.0%"; "Tax Rate | 1% | 11%"; "Earnings (Loss) Per Share Attributable to Intel—Diluted | $0.31 | $0.38"; "based on the midpoint of the revenue range" | [Q2 release] | L114–L117; L120 | PASS |
| F2 | "we are guiding Q3 revenue to a range of $15.8 to $16.8 billion. At the midpoint of $16.3 billion, we forecast gross margin of 42 percent, a tax rate of 11 percent, and EPS of $0.38 cents, all on a non-GAAP basis" | [Q2 call, p.5] | L248–L250 (p.5 = L220–L273) | PASS |
| F3 | "We continue to tightly manage non-gaap operating expenses to roughly $16.5 billion for the year" | [Q2 call, p.5] | L252 | PASS |
| F4 | "now expect our cap ex to be more than $20 billion, which is up significantly versus our expectations entering the year" | [Q2 call, p.5] | L257–L258 | PASS |
| F5 | "we expect non-controlling interest, or NCI, to net to approximately $250 million in each of Q3 and Q4 of this year and be approximately $1.1 billion for 2027 and 2028, on a GAAP basis" | [Q2 call, p.5] | L253–L254 | PASS |
| F6 | "we are forecasting 2027 capital expenditures to be significantly above the 2026 levels with the vast majority spent across our US network" | [Q2 call, p.5] | L260–L261 | PASS |
| F7 | "we remain on track for 14A risk production for our internal products in the second half of 2027 and we made the decision in Q2 to fully commit to high volume ramps in 2028" | [Q2 call, p.2] | L79–L80 (p.2 = L56–L110) | PASS |
| F8 | 18A-P entered risk production in June 2026 | [10-Q Q2, Item 2] | L1143 | PASS |
| F9 | "Not guided": April's "positive … for the full year" not repeated | [Q1 call, p.6; Q2 call] | transcript-Q1 L281–L282; no "free cash flow" in transcript.txt | PASS on the fact. **Wording nit:** "GAAP margin or EPS in the remarks" reads as if GAAP were not guided, but the release guides both (41.0%, $0.31) and §4 quotes them |

### 4g. outlook.md §5 claim quotes

| # | Quote | Tag | Found at | Result |
|---|---|---|---|---|
| G1 | "Revenue | $15.8-16.8 billion" | [Q2 release] | L114 | PASS |
| G2 | "Gross margin | 41.0% | 42.0%" | [Q2 release] | L115 | PASS |
| G3 | "NCI, to net to approximately $250 million in each of Q3 and Q4 of this year" | [Q2 call, p.5] | L253–L254 | PASS |
| G4 | "now expect our cap ex to be more than $20 billion" | [Q2 call, p.5] | L257 | PASS |
| G5 | "we are meaningfully increasing our investments in equipment, clean room space, and substrates"; first-half gross capex $7.6B | [Q2 release] | L30; 4,963 + 2,652 = 7,615 | PASS |
| G6 | "We continue to tightly manage non-gaap operating expenses to roughly $16.5 billion for the year" | [Q2 call, p.5] | L252 | PASS (quote); see §6 for the unlabelled sharpening |
| G7 | "we expect Intel Foundry's operating loss to improve through the year" | [Q1 call, p.4] | transcript-Q1 L205 | PASS |
| G8 | 14A quote | [Q2 call, p.2] | L79–L80 | PASS |
| G9 | "PDK 0.9 is on track for October" | [Q2 call, p.2] | L73–L74 | PASS |
| G10 | "on track for an additional 20 percent this year" | [Q2 call, p.4–5] | L223–L224; the sentence starts on p.4 L219 ("Intel Foundry has driven down the cost") and ends on p.5, so the p.4–5 tag is right | PASS |
| G11 | "the near-term linearity of our supply growth is more skewed towards the end of Q3 and into Q4, especially for servers" | [Q2 call, p.5] | L237–L238 | PASS |
| G12 | "Not sharpenable": April's "early design commitments" window (late 2026 into early 2027) | [Q1 call, p.2] | transcript-Q1 L94–L95 (p.2 = L55–L109) | PASS |

### 4h. outlook.md §2–§3 quotes and page tags

| # | Quote / fact | Tag | Found at | Result |
|---|---|---|---|---|
| H1 | "Our core message is simple: … tangible results" | [Q2 call, p.1] | L27–L29 | PASS |
| H2 | "the seventh consecutive quarter of exceeding our financial expectations" | p.1 | L24–L25 | PASS |
| H3 | "The industry is facing one of the most severe supply constraints in its history"; "will persist for the foreseeable future" | p.1 | L40–L41 | PASS |
| H4 | "leverage our X86 computing franchise to strengthen our product leadership and establish Intel Foundry as a world-class wafer and packaging foundry business" | p.3 | L125–L126 (p.3 = L111–L165) | PASS |
| H5 | factory output as top priority; "AI-first" | p.2; p.1 | L104–L105; L35 | PASS |
| H6 | "The remarks never mention the US government stake, Altera, Mobileye, dividends, buybacks, tariffs or China" | [Q2 call] | case-insensitive grep of transcript.txt for government / Altera / Mobileye / dividend / buyback / repurchase / tariff / China: 0 hits | PASS |
| H7 | "our core server CPU franchise is growing faster than ever"; "strong double-digit"; "momentum extending into 2028" | p.1; p.5 | L48–L49; L245; L245–L246 | PASS |
| H8 | "two thirds of our client revenue mix"; "roughly 10 percent of CCPG revenue"; "the Edge and Physical AI opportunity is likely to at least match the client TAM overtime"; "We still have work to do" | p.4; p.2 | L172–L174; L195–L196; L95 | PASS |
| H9 | "increasing momentum on customer engagements for Intel 14A"; "high volume ramps in 2028"; "on track for October"; Altera $181M | p.2; [10-Q Item 2] | L76; L80; L73–L74; 10-Q L1161 (also L797) | PASS |
| H10 | "a growing EMIB-T backlog, yield and reliability are hitting targets"; "customer ramps in 2027" | p.2 | L84–L86 | PASS |
| H11 | "up roughly 20 percent sequentially and nearly tripling year-over year"; Fortinet; "other DCAI revenue" $951M | p.4; p.3; [10-Q Item 2] | L202; L121; 10-Q L1201 | PASS |

### 4i. business.md prose sentences (§1, §2, §5–§7)

| # | Sentence / fact | Tag | Found at | Result |
|---|---|---|---|---|
| I1 | §1 "cancel, change or delay product purchase commitments with little or no notice to us and without penalty" | [10-K FY2025, Item 1] | L524 | PASS |
| I2 | §1 "substantially all" (Foundry work for Intel Products); "a strategically important company from both a national economic and national security perspective"; only US company doing leading-edge R&D and HVM | [10-Q Item 2]; [10-K Item 1] | 10-Q L1227; 10-K L232; L342 | PASS |
| I3 | §1 "a foundational computing platform for over four decades"; "leading manufacturing competitor"; "where we have been unsuccessful to date in becoming a meaningful participant"; $79.0B → $52.9B; CEO March 18, 2025; "our strongest revenue growth in more than fifteen years"; 25% growth | as tagged | L270; L506; L1225; A13; DEF14A L1007; release L28, L20 | PASS |
| I4 | §1 "Intel designs the central processing units (CPUs) … in most of the world's PCs and a large share of its servers" | [10-K FY2025, Item 1] | L318 says x86 (Intel **and** AMD) "remain the foundational computing platform for the majority of PCs"; L1225 says Intel has "lost market share … in both client and data center markets". No source says Intel alone is in most PCs | **FAIL (overstates):** attribute "most PCs" to x86, or drop "most" |
| I5 | §2 CCPG: "distributors and OEMs"; $32.2B / $9.3B; 8% fewer units, 27% higher prices, "market demand exceeded our available product supply" | [10-K Item 1; Note 3]; [10-Q Item 2] | L310; L2211, L2213; 10-Q L1199 | PASS |
| I6 | §2 DCAI: hyperscalers and OEMs; $16.9B; $6.3B, +59%, ASP +48%, volume +9% | same | L324; L2211; 10-Q L1201 | PASS |
| I7 | §2 Foundry: $17.8B / $5.8B; $307M / $293M; "at prices that are intended to approximate market pricing"; "are meant to reflect separate fabless semiconductor and foundry companies"; Altera $181M | [10-K Note 3]; [10-Q Item 2] | L2211, L2170; 10-Q L1233, L1244; L2170; L2202 (also 10-Q L504); 10-Q L1161 | PASS |
| I8 | §2 All other and Corporate unallocated composition | [10-K Note 3] | L2178; L2231 ("restructuring and other charges, share-based compensation and certain acquisition-related costs") | PASS |
| I9 | §5 "established software ecosystem continues to provide interoperability and performance across diverse workloads"; "we have lost market share in recent years, including in both client and data center markets"; Apple 2020; $1.7B deposits; "We have been unsuccessful to date in securing any significant external foundry customers for any of our nodes" | [10-K Item 1; Item 1A]; [10-Q Item 2] | L270; L1225; L1221; 10-Q L1506; L1245 | PASS |
| I10 | §6#1 "a significant external foundry customer for Intel 14A"; "may pause or discontinue"; "become dependent on third-party foundries, particularly TSMC"; "over $100 billion"; "committed to completing development of Intel 14A"; "will ultimately be dictated by the amount of committed demand" | [10-K Item 1A]; [10-Q Item 2] | L1243; L1243; L1251; L1253; 10-Q L1143; L1143 | PASS |
| I11 | §6#2 $633M → $2.5B; NVIDIA "GPU systems have experienced the highest demand in the market"; hyperscalers designing own chips; DCAI 51% of Products' Q2 operating income (computed) | [10-Q Note 2; Item 2]; [10-K Item 1] | 10-Q L525, L517; L336; 2,474 / 4,817 = 51.4% | PASS |
| I12 | §6#3 CCPG 73% of Products' FY2025 operating income (computed); "down low double digits percent for all of 2026"; competitors AMD, Apple, Qualcomm, MediaTek | [10-K Note 3]; [Q2 call p.5]; [10-K Item 1] | 9,317 / 12,739 = 73.1%; L241; L318 | PASS |
| I13 | §6#4 Customer A 19% × 3; 40% / 45% / 43%; Dell, Lenovo, HP named in FY2023; 47% of receivables; not in 10-Qs | [10-K FY2023 Note 3; 10-K FY2025 Note 3; Note 2]; [10-Q Item 2] | 10-K-FY2025 L2247–L2250 (A 19/19/19, B 12/14/11, C 12/12/10, totals 43/45/40); 10-K-FY2023 L2464–L2466 (Dell 19%, Lenovo 11%, HP 10% for 2023); L2068 (Note 2); 10-Q: no customer-percentage table | PASS |
| I14 | §6#5 "A significant portion" of revenue from Intel 7 made in Israel; "not insured" against war; Iran list "with Intel being near the top of that list"; helium "essential to the semiconductor manufacturing process"; Intel 7 "almost half" of 2026 production | [10-Q Item 2]; [10-K Item 1] | 10-Q L1155; L1155; L1155; L1153; 10-K L480 | PASS |
| I15 | §6#6 China 24% of FY2025 revenue; "led to additional sales reductions"; "exclusively manufactured by TSMC"; "no long-term contract"; March 2026 suit calling the agreement "unlawful"; "unauthorized, void or voidable" | [10-K Item 1A; 10-Q Note 14] | 12,694 / 52,853 = 24.0% (L2258; computed, label added by reviewer); L1329; L1391; L1251; 10-Q L1014 (Note 14, filed March 2026, "the agreement was unlawful"); 10-K L1279 (the "void or voidable" words are the 10-K's risk factor, not the 10-Q's, and the tag covers both) | PASS |
| I16 | §7 Tan 66, CEO since March 18, 2025, 12 years at Cadence, two years on the board; $25M purchase held for vesting; Zinsner CFO since January 2022, PAO from April 24, 2026; CLO out June 1, 2026; Barratt (director since Nov 2025) succeeds Yeary as chair after the May 13, 2026 meeting; "CEO transitions in 2025, 2024, 2021 and 2019" | [10-K Item 10; DEF 14A; 8-Ks] | 10-K L1562; DEF14A L1007, L443 (12 years), L1015 (Sept 2022–Aug 2024); L1082, L1093; 10-K L1568; 8-K-2026-04-24; 8-K-2026-04-03; 8-K-2026-03-03-ex991 + DEF14A L249, L351; 10-K L1471 | PASS |
| I17 | §7 track record: $18.8B FY2024 loss with $9.9B tax charge and $3.3B Intel 7 write-downs; 108,900 → 85,100; $12.7B raised; Altera $4.3B net, $5.6B gain; Mobileye $3.9B goodwill write-down; $14.2B Apollo, $13.5B to equity | [10-K Items 1, 7, 8; Note 10]; [10-Q Q1 Note 10]; [10-Q Q2 Note 3] | L1764; L702; L698; FY2024 10-K L443, FY2025 L570; L1877 (see §5e); L676, L2474; 10-Q Q1 L760 ("substantially all of which related to our Mobileye reporting unit"); 10-Q Q2 L594 | PASS |
| I18 | §7 pay: four metrics 25% each for CEO, 20% each incl. individual goals for others; 123.4% → 118.7%; three-year TSR vs S&P 500; hiring awards need absolute stock-price growth; $93.0M total, $42M hiring awards; 72% say-on-pay in 2025; 86.9% in 2026 (computed) | [DEF 14A CD&A; 8-K 2026-05-15] | L1104; L1362; L1090; L1093; L1648 ($92,990,900), L1068; L1128; 2,795,303,255 / (2,795,303,255 + 422,008,632) = 86.88% | PASS on arithmetic. **Nit:** the denominator excludes 12,839,978 abstentions; with them it is 86.5%. State "for ÷ (for + against)" |
| I19 | §7 ownership: US government 433.3M / 8.4% counting escrowed shares; "has agreed to vote its shares of common stock as recommended by our board of directors"; Vanguard 8.1%; BlackRock 6.8%; directors and officers together "under 1%" | [DEF 14A Security Ownership; 10-K Item 1A] | L700 (footnote: "assumes full release of 149,438,785 shares held in escrow"); 10-K L1285; L701; L702; L693 says "not more than 1%" | PASS (wording nit: "not more than 1%") |
| I20 | §7 table: $7.2B authorization unused; dividends $1.39 / $1.46 / $0.74 / $0.38, suspended from Q4 2024; CHIPS "prohibited … for the next two years" quote; amendment "substantially all other requirements under the agreement other than those required by law"; 4,070M → 5,043M shares; 580M issued in 2025 (computed); $5.7B, 275M, 159M, 241M, $20.00, 51%; SoftBank 87M @ $23.00 = $2.0B; NVIDIA 215M @ $23.28 = $5.0B; NVLink; Altera 51% to Silver Lake $4.3B; Mobileye $921M, 80%; Apollo $14.2B Apr 8, $6.5B bridge; $6.5B notes 4.65–6.20% due 2031–2066 Apr 30, bridge repaid; $3.8B due 2027; cash $29.7B vs $37.4B; headcount 124,800 / 108,900 / 85,100 / 82.3K; Brookfield unfunded $5.2B | as tagged | 10-K L1598, 10-Q L1568; 10-K-FY2023 L2176/L2184/L2192, 10-K-FY2025 L1913, 10-K-FY2024 L1057; L1057; 10-K-FY2025 L656; 10-K-FY2023 L2177, 10-Q L317; 275 + 87 + 215 = 577, = 580 only if the 3M escrowed shares released in 2025 (10-K L662) are counted; L658–L662; L670; L672; DEF14A L1033; L676 (SLP); L2312, L362; 8-K-2026-04-08; 8-K-2026-04-30 + 10-Q L833, L837 ("On April 30, 2026, we repaid the term loan facility in full"); 10-K L2951 ("2027 | $3,826"; Note 13); 10-Q L267–L268 (14,265 + 23,151 = 37,416); FY2023 L515, FY2024 L443, FY2025 L570, release L277; 10-K L3326 (Note 19) | PASS. **Nit:** say what the 580M is made of |

**Totals: 114 checked; 110 PASS; 2 FAIL (C11 "two factories", I4 "most of the world's PCs"); 2 UNVERIFIABLE (A14' IMS move, A16 NAND in FY2021 All other).** No quote is misattributed, no page tag is wrong, and no number in any table is wrong.

---

## 5. Company-specific accuracy checks

**a. Products vs Foundry, intersegment revenue, eliminations, corporate unallocated.** Faithful. The draft quotes the FY2025 Note 3 wording for transfer pricing ("at prices that are intended to approximate market pricing", L2170) and purpose ("are meant to reflect separate fabless semiconductor and foundry companies", L2202), describes eliminations as removing the internal sale from consolidated revenue (matches L2202 and the eliminations column), and describes corporate unallocated as "restructuring, stock pay and acquisition costs" (L2231). Foundry external revenue $293M in Q2 2026 (10-Q L1244) and operating loss $(2,089)M (10-Q L517) are right. The FY2024-vs-FY2025 10-K discrepancy for 2023 external revenue ($953M at 10-K-FY2024 L2256 vs $547M at 10-K-FY2025 L2170) is stated and explicitly left unreconciled ("do not reconcile them"), as required. One caution: footnote ¹'s "IMS moved from Foundry to All other" is the likely explanation for that gap but is an inference, not a disclosure (A14'); label it.

**b. Escrowed shares / derivative liability.** Matches the notes: liability $2.7B at Dec 27, 2025 (10-Q Q1 L585) → $3.6B at Mar 28, 2026 (L585, in the outlook) → $15.6B at Jun 27, 2026 (10-Q Q2 L631); $12.5B Q2 loss (L631; Item 2 L1133 adds "driven by an increase in our stock price"); releases 3M in 2025 (10-K L662), 6M in Q1 (10-Q Q1 L583), 7M in Q2 (10-Q Q2 L629); 143M remaining (L633); $20.00 release price (10-K L662); warrant 241M shares conditional on 51% Foundry ownership (10-K L660; 10-Q L635); government voting agreement (10-K L1285); 8.4% per proxy (DEF14A L700). The draft explains it as a non-cash mark-to-market effect of the share price, which is what Note 4 and the release's non-GAAP explanation (L439) say. One overstatement: "dilution, fixed the day the deal was signed". The share count is capped at 159M and depends on Secure Enclave disbursements, and if disbursements stop "half of any remaining Escrowed Shares will be released" (10-K L2366), so the dilution is capped, not fixed. The draft does not list the per-period releases, which is fine.

**c. Segment-table footnotes.** ¹ NEX folded into CCG/DCAI in Q1 2025 with prior years recast: stated and sourced (10-K-FY2025 L2140). CCG renamed CCPG in Q2 2026 without restatement: stated in §1 and in the row label "CCG / CCPG" (10-Q L1070; release L69). Altera deconsolidated September 2025: not in the footnote but in the §2 prose ("half-sold in September 2025"; "Altera's results through September 11, 2025", 10-K L2178). IMS moved to All other: stated but not sourced (A14'). ² Foundry model from Q1 2024, NEX still a segment: sourced (10-K-FY2024 L2240, L2244). ³ No Foundry segment before 2024: sourced (10-K-FY2023 L2413); the NAND remark is an inference (A16).

**d. Customer concentration.** Correct in every particular: Dell / Lenovo / HP named only in the FY2023 10-K (L2464–L2466: 19% / 11% / 10% for 2023 = 40%); Customer A / B / C thereafter (10-K-FY2025 L2247–L2250: 19 / 12 / 12 = 43% for 2025, 19 / 14 / 12 = 45% for 2024); 47% of receivables at Dec 27, 2025 (L2068, Note 2); the 10-Qs carry no customer-percentage table, so "updates once a year" is right, and §8 correctly keeps concentration out of the quarterly indicator list for that reason.

**e. Capital allocation.** Dividend suspended from Q4 2024 (10-K-FY2024 L1057) and no buybacks since Q1 2021 (10-K-FY2025 L1598): right. Apollo Fab 34 buyback $14.2B on April 8, 2026 (8-K-2026-04-08), $6.5B notes April 30 in five tranches 4.65%–6.20% due 2031–2066 (8-K-2026-04-30) repaying the term loan the same day (10-Q L837), $13.5B "as a reduction to our capital in excess of par value" (10-Q L594): right. SoftBank $2.0B, NVIDIA $5.0B (10-K L670, L672), NVLink (DEF14A L1033), Altera 51% to an SLP affiliate for $4.3B net with a $5.6B gain (L676, L2474), Mobileye $921M with 80% retained (L2312, L362): right. The "$12.7 billion raised by selling shares" sentence rests on the FY2025 cash-flow line "Net proceeds attributed to common stock and warrants issued, and Escrowed Shares | 12,706" (L1877). That line is the sum of the government's $5.7B and the SoftBank and NVIDIA placements ($2.0B + $5.0B), all of which were share deals, so the sentence is faithful to a single disclosed line and needs no "(computed)" label. Optional precision: "by selling shares and related rights to the US government, SoftBank and NVIDIA".

**f. Management facts.** Lip-Bu Tan CEO effective March 18, 2025 (DEF14A L1007), 12 years as Cadence CEO (L443; 10-K L1562 gives 2009–Dec 2021), age 66 (10-K L1562): right. Zinsner CFO since January 2022 (10-K L1568) and principal accounting officer from April 24, 2026 after Gawel resigned (8-K-2026-04-24): right. Yeary → Barratt as independent chair "effective following the company's Annual Stockholders' Meeting on May 13, 2026" (8-K-2026-03-03-ex991; DEF14A L351): right. CLO April Miller Boise separating June 1, 2026 (8-K-2026-04-03): right. Pay metrics and weights (DEF14A L1104: CEO four metrics 25% each; others five at 20% each), 123.4% formulaic → 118.7% (L1362), total $92,990,900 (L1648), $42M new-hire awards (L1068), 72% say-on-pay in 2025 (L1128): right. Ownership table (L700–L702, L693): right, with the "under 1%" vs "not more than 1%" wording nit.

**g. Outlook §1 non-GAAP gross-margin row.** The Q2 expectation columns use only the Q1 2026 release's own Q2 guidance (revenue $13.8–14.8B, GM 37.5% GAAP / 39.0% non-GAAP, tax 4% / 11%, EPS $0.08 / $0.20; press-release-Q1-2026.txt L94–L98), quoting "Gross margin … 39.0%". The Q1 cell uses 41.0% (Q1 release L433) plus the remarks' "approximately 650 basis points ahead of guidance" (transcript-Q1 p.3 L138–L139) and does not back out an implied Q1 guide, correctly, because the Q4 2025 release is not in the sources. Nothing is invented.

---

## 6. Claims audit (§9), outlook §5

Count 11 (target 6–12). Headline guidance is 4 of 11 (1, 2, 3, 6); the rest are fundamentals (capex, Foundry loss, 14A dates, PDK, Panther Lake cost, Q4 guide shape). All quotes verbatim and tagged (G1–G11).

| # | One sentence, one thing? | Single direction (can fail)? | Verbatim quote + tag | Sharpening / disclosure labelled? | Notes |
|---|---|---|---|---|---|
| 1 | Yes | Yes (either side of the range misses) | Yes | n/a | Headline revenue |
| 2 | Yes | Yes | Yes | n/a | |
| 3 | Yes | Yes | Yes | Yes: "our sharpening of 'approximately $250 million'"; quarter stated (Q3) | Gradeable from the income statement's NCI line |
| 4 | Yes | Yes ("keeps or raises", allowed by §9) | Yes | n/a | Fails if cut or dropped |
| 5 | Yes | Yes | Yes | Yes: "our sharpening from first-half gross capex of $7.6 billion"; quarter stated; the release reconciliation is a recurring table | $7.6B re-derives (4,963 + 2,652) |
| 6 | Yes | Yes | Yes | **No.** "roughly $16.5 billion" is turned into "$16.5 billion or lower" without a sharpening label; a $16.6B figure would fail the claim while matching "roughly" | The Full-Year 2026 opex table appears in both the Q1 (L526–L532) and Q2 releases, so the source recurs. Add "(our sharpening of 'roughly')" or restate as "keeps the full-year figure at roughly $16.5 billion, not raised" |
| 7 | Yes | Yes | Yes (April call, p.4) | Yes: "our sharpening of the April statement, which July did not repeat" | **Keep.** The April statement is a full-year statement ("improve through the year") that management has not withdrawn; the July remarks add that Q2 "stepped up investments … for Intel 14A" (p.5 L228) but say nothing about the Foundry loss trajectory. The Q3 segment table will make this Met or Missed mechanically; the label already tells the grader its provenance. Optional: add "despite the Q2 step-up in 14A spending" so the grader knows the countervailing remark |
| 8 | Two dates, one schedule | Yes ("reaffirms … with neither date pushed out") | Yes | n/a | Acceptable; both dates come from one sentence of management. If either slips the claim is Missed, which is the intended reading |
| 9 | Yes | Yes | Yes | n/a | If the Q3 call falls before month-end the grader may need the 10-Q or a ⏳; the claim allows both |
| 10 | Yes | Yes | Yes | No sharpening: "roughly 20%" is management's "20 percent" | Horizon Q4 call, so ⏳ at Q3 |
| 11 | Yes | Yes (midpoint ≤ Q3 actual fails) | Yes | Yes: "our sharpening of the supply-timing statement" | Legitimate single-direction reading of "supply growth is more skewed towards the end of Q3 and into Q4"; the PC "sub-seasonal" remark (p.5 L240) cuts the other way, which is exactly why this is a claim and not a fact |

No either/or constructions. No disclosure checks are used, so the quarter-vs-year-to-date rule does not arise beyond claims 3 and 5, which both name the quarter.

---

## 7. Indicator audit (§8)

| # | Indicator | Recurring anchor? | Name / why / where present? |
|---|---|---|---|
| 1 | Intel Foundry operating income (loss) | Yes: 10-Q Note 2 segment table; release "Supplemental Operating Segment Results" | Yes |
| 2 | Intel Foundry revenue from outside customers | Yes: stated every quarter in 10-Q Item 2 Foundry section (Q1 L1182, Q2 L1244) and in the CFO remarks | Yes |
| 3 | DCAI revenue and operating margin | Yes: segment table; Item 2 "Operating margin %" row | Yes |
| 4 | CCPG revenue and operating margin | Yes: same | Yes |
| 5 | Non-GAAP gross margin vs guided | Yes: release summary table and prior release's outlook table, every quarter | Yes |
| 6 | Gross capex and adjusted free cash flow, quarterly | Yes: release adjusted-free-cash-flow reconciliation, every quarter | Yes |
| 7 | Cash plus short-term investments; total debt | Yes: balance sheet lines | Yes |
| 8 | Escrowed shares not yet released; derivative liability | Yes while escrow lasts: 10-Q Note 4 and Note 5 each quarter (the row will naturally retire when the 143M shares are released) | Yes |

No indicator depends on a one-off target; the one-off targets (capex >$20B, opex $16.5B, NCI $250M, PDK October, Panther Lake cost) are tracked as claims, as §8 asks. Customer concentration is correctly excluded as annual-only.

---

## 8. Jargon audit (smart 16-year-old, no finance or chip background)

**Fixed directly (see list at the end):** GPUs, TSMC, Arm, consolidated revenue, Mobileye / IMS / Altera one-word descriptions, restructuring, gross vs operating margin, CHIPS Act, dilution, write-downs, risk production (business.md first use), receivables, goodwill, principal accounting officer, vest, S&P 500, say-on-pay, bridge loan, notes, maturities, finance leases, NAND, x86 glossary wording, amortization (glossary entry), proxy statement (Sources); in the outlook: inference, edge, backlog, purpose-built silicon, sequentially, basis points.

**Already plain or defined in the drafts:** node, hyperscalers, fabless, yield, depreciation, non-controlling interests, derivative liability, escrow, PDK, TAM, EMIB, wafer, capex, GAAP / non-GAAP (glossary plus table footnote), adjusted free cash flow (Intel's definition explained in §4).

**Left as is, judged acceptable:** "leading-edge" (name-inferable), "AI PCs", company and product names, "18A / 14A / Intel 3 / Intel 7" (covered by the glossary's "Process node"), "midpoint", "tax rate".

**Banned-word sweep** (leverage, synergy, headwind, tailwind, monetize, ecosystem, at scale, robust, unlock, TAM): none in the writer's own prose. "leverage", "tailwind", "ecosystem" and "TAM" appear only inside management quotes, and TAM is glossed.

**Paragraphs that are mostly numbers:** business.md §7 "Track record" (nine figures in two sentences) is borderline; the §7 table absorbs most of the rest. Tables are dense but readable; outlook §1 holds one comparison per cell.

---

## 9. Invented-number and inference check

No invented numbers. Every figure traces to a cached source or a labelled computation, with these labelling gaps:

1. **business.md §2 footnote ¹ "IMS moved from Foundry to All other"** — inference, not disclosed (A14'). Label "our inference".
2. **business.md §2 footnote ³ "FY2021 All other includes the NAND business later sold"** — inference from "historical results of operations from divested businesses" (A16). Label.
3. **business.md §1 "in most of the world's PCs"** — overstates the 10-K, which says x86 (Intel and AMD) is the majority platform and that Intel has lost share (I4).
4. **business.md §4 "dilution, fixed the day the deal was signed"** — capped, not fixed (§5b).
5. **business.md §7 "86.9% of votes cast (computed)"** — arithmetic right; denominator (abstentions excluded) unstated (I18).
6. **business.md §7 table "580M issued in 2025 … (computed)"** — reconciles only if the 3M escrowed shares released in 2025 are included with the 275M + 87M + 215M placements; say so (I20).
7. **business.md §3 table R&D % "(computed)" on FY2021, FY2022 and 6M 2026** — these are printed in the filings; the label is unnecessary rather than wrong (C4).
8. **business.md §6#6 China 24%** — computed from the region table; the reviewer added the "(computed)" label.
9. **business.md §3 "which is why gross margin slid from 55.4% … to 32.7%"** — the causal "which is why" is the writer's reading; the 10-K's fixed-cost quote supports it, and the FY2024 figure also carries $3.3B of Intel 7 impairments (10-K-FY2025 L698). Acceptable, but "a big reason why" would be more careful.

Interpretations correctly labelled as such: §5 "our inference" on why the government bought in; §6#1 "Exposure: the whole profit pool" (reasoning, not a number); outlook claims 3, 5, 7, 11 labelled as sharpenings.

---

## 10. As-of check (cutoff 2026-07-24)

Grep of both drafts for any date, event or figure after 2026-07-24: none, other than forward-looking references inside quotes and claims (Q3 2026, Q4 2026, "October", late 2027, 2028) and the "Written 2026-09-07" header lines. The 10-Q used was filed 2026-07-24 (on the cutoff); the latest 8-K used is 2026-05-15; the transcript and release are 2026-07-23. The MANIFEST confirms the 2026-08-12 8-K and later items were not fetched. No later knowledge appears in either draft.

---

## 11. Verdict: REVISE

Numbered list for the writer (numbers, quotes, structure and claims are otherwise correct; keep both files word-neutral: business.md is at 2,929 of 3,000 and outlook.md at 1,199 of 1,200):

1. **business.md §1, first sentence.** "in most of the world's PCs" is not supported; the 10-K (L318) says x86, made by Intel *and* AMD, is "the foundational computing platform for the majority of PCs", and Intel has "lost market share". Reword, e.g. "the x86 chips that, with AMD's, run most of the world's PCs and a large share of its servers".
2. **business.md §2 footnote ¹.** "IMS moved from Foundry to All other" is not stated in any cached 10-K. Write "our inference: IMS, whose tool sales sat in IFS in the FY2023 10-K, is listed in All other from the FY2025 10-K; the 10-K cites only 'certain other business reorganizations'". Optionally add that this is also the likely, unconfirmed reason for the $953M vs $547M gap in the prose above (keep "do not reconcile them").
3. **business.md §2 footnote ³.** Label "FY2021 All other includes the NAND (memory-chip) business later sold" as inference ("our inference; the note says only 'historical results of operations from divested businesses'").
4. **business.md §3, capital-intensity paragraph.** "paid for 49% of two factories" → "49% of two factory projects (Fab 34 in Ireland; two new fabs in Arizona)" [10-Q Q2 2026, Note 3].
5. **business.md §4, escrow paragraph.** "dilution … fixed the day the deal was signed" → "capped the day the deal was signed (at most 159 million shares, released as Secure Enclave money arrives)" [10-K FY2025, Note 5].
6. **business.md §7.** State the say-on-pay denominator: "86.9% of votes for and against (computed; 86.5% counting abstentions)". Change "under 1%" to "not more than 1%" (the proxy's words). In the table, "580M issued in 2025 … (computed)" → "580M (computed: 275M plus 3M escrowed shares released to the government, 87M SoftBank, 215M NVIDIA)".
7. **business.md §3 table.** Either drop the "(computed)" label on the FY2021, FY2022 and 6M 2026 R&D % cells (all printed in the filings) or leave it; not a correctness issue.
8. **outlook.md §5 claim 6.** Label the sharpening: "… is $16.5 billion or lower (our sharpening of 'roughly $16.5 billion')", or restate as "The Q3 2026 release keeps the full-year 2026 non-GAAP operating expense figure at roughly $16.5 billion (not raised)". Net word change zero or negative, please.
9. **outlook.md §4 "Not guided".** Delete "GAAP margin or EPS in the remarks;" (the release guides both and §4 quotes them) or change to "the remarks give only non-GAAP figures". Deleting frees seven words for item 8.
10. **Both Sources tables.** Remove the `[Q2 2026 slides, p.N]` row, or use the tag somewhere; nothing in either body cites the slides.
11. **Optional, business.md §3.** "which is why gross margin slid" → "a large part of why gross margin slid", since FY2024 also carried $3.3 billion of Intel 7 impairments.

Items 1–6 and 8 are the substantive ones; the rest are tidy-ups. One cycle should suffice.

---

## Fixed directly (jargon glosses, plain phrases, one "(computed)" label, one glossary entry, one Sources gloss; no numbers, quotes, structure, claims or indicators changed)

business.md
- §1 history: "TSMC" → "TSMC (the Taiwanese contract chipmaker)"; "GPUs" → "GPUs (graphics processing units, the chips NVIDIA sells for AI)".
- §2 Foundry paragraph: "consolidated revenue" → "consolidated (company-wide) revenue".
- §2 All other paragraph: added "(driver-assistance chips)" after Mobileye, "(machines that make the masks used to print chips)" after IMS, "(programmable chips)" after Altera, "(layoff and shutdown costs)" after restructuring; reordered the Altera clause so the date reads cleanly.
- §2 footnote ³: "NAND business" → "NAND (memory-chip) business".
- §3 first paragraph: inserted "(Gross margin is the share of revenue left after the direct cost of making the chips; operating margin is what is left after R&D and overhead too.)" after the opening sentence.
- §4 escrow paragraph: "Secure Enclave, a CHIPS Act program" → "Secure Enclave, a program under the CHIPS Act (the 2022 US law that pays grants for chip factories)"; "dilution" → "dilution (each existing share owning a smaller slice of the company)".
- §4 table: "Payments on finance leases" → "Payments on finance leases (equipment bought in installments)".
- §5: "Arm-based chips" → "Arm-based chips (a rival chip design used by Apple and Qualcomm)".
- §6#1: "write-downs" → "write-downs (charges booked when assets are judged worth less than their recorded cost)"; "risk production in late 2027" → "risk production, the first small runs before full volume, in late 2027".
- §6#4: "owed 47% of receivables" → "owed 47% of the money customers owed Intel (receivables)".
- §6#6: "China billings were 24% of FY2025 revenue" → "Sales billed to China were 24% of FY2025 revenue (computed)".
- §7: "principal accounting officer" → "… (the executive who signs off on the books)"; "to vest" → "to vest (become his to keep)"; "Mobileye goodwill" → "Mobileye goodwill (the premium paid over a bought company's asset value, carried on the balance sheet)"; "S&P 500" → "S&P 500 (an index of 500 large US companies)"; "say-on-pay support was 72%" → "support in the say-on-pay vote (shareholders' advisory vote on executive pay) was 72%".
- §7 table: "bridge loan" → "bridge loan (a short-term loan)"; "new notes (4.65%–6.20% …)" → "new notes (bonds; 4.65%–6.20% …)"; "2027 maturities $3.8B" → "$3.8B of debt comes due in 2027".
- Glossary: x86 entry reworded ("the set of basic instructions (the 'language') that Intel's and AMD's CPUs understand"); added "Amortization" entry.
- Sources: DEF 14A row now says "proxy statement, the annual shareholder-meeting document that discloses pay and ownership".

outlook.md
- §1 intro line tightened: "Indicators as proposed in business.md §8, pending owner lock; Q1 2026 ended March 28, 2026."
- §1 row 5: added "(6.5 percentage points)" after the 650-basis-points quote.
- §1 note: "The Q2 adjusted free cash flow includes the $14.2 billion paid to buy out Apollo's stake in Fab 34" → "Q2 adjusted free cash flow includes the $14.2 billion Apollo buyout of Fab 34".
- §2: "The CEO's frame:" → "The CEO:"; "The two stated priorities:" → "Stated priorities:"; "and a deeper Google Cloud collaboration is framed as helping Intel adopt an 'AI-first' way of running itself" → "; a deeper Google Cloud collaboration is meant to make Intel 'AI-first' in how it runs itself".
- §3 DCAI: "AI inference" → "AI inference (running trained AI models)".
- §3 CCPG: "edge deployments" → "edge deployments (chips in factories and devices, not data centers)"; "being restated and rising" → "restated and rising".
- §3 EMIB-T: added "(backlog: orders not yet delivered)"; "showing up in" → "appearing in".
- §3 Design Services: heading → "Purpose-built silicon (custom chips for one customer) and Design Services"; added "(sequentially: versus the prior quarter)" after the quote.
- §5 "Not sharpenable": removed "whether the '$20 billion' capex is gross or net; 2026 adjusted free cash flow;" (both already listed under §4 "Not guided").

Backups of the pre-fix drafts: `/tmp/intc-business.md.bak`, `/tmp/intc-outlook.md.bak`.

---

## Cycle 2 (re-check of the writer's second pass; review cycle 2 of 2)

_Re-checked 2026-09-07 against `sources/2026-Q2/` only. Both drafts re-read in full; every changed sentence compared with the cited line._

### 1. Status of the 11 REVISE items

| # | Item | Applied? | Faithful to source? | Note |
|---|---|---|---|---|
| 1 | §1 "most of the world's PCs" | Yes | Yes | Now "x86 CPUs, Intel's and AMD's, run most of the world's PCs and a large share of its servers" — matches 10-K-FY2025.txt L318 ("Client CPUs utilizing the x86 architecture remain the foundational computing platform for the majority of PCs") and L270 (x86 supports "client and data center applications"). "A large share of its servers" is unquantified in the source and stays soft, which is right |
| 2 | §2 footnote ¹ IMS move | Yes | Yes | Labelled "Our inference"; "certain other business reorganizations" is verbatim at L2140; IMS listed in All other at L2178; FY2023 10-K L991 puts mask-writer tool sales in IFS. The gap is described as "likely, unconfirmed" and the prose still says "do not reconcile them" |
| 3 | §2 footnote ³ NAND | Yes | Yes | Labelled "Our inference"; "historical results of operations from divested businesses" is verbatim at 10-K-FY2023.txt L2421 |
| 4 | §3 "two factories" | Yes | Yes | Now "49% of two factory projects (Apollo: Fab 34 in Ireland; Brookfield: two new fabs in Arizona)" with [10-Q Q2 2026, Note 3] added; 10-Q L564–L565 (49% each), L592 (Fab 34), L600 ("two new chip factories") |
| 5 | §4 "dilution … fixed" | Yes | Yes | Now "capped the day the deal was signed at 159 million shares [10-K FY2025, Note 5]"; L2350 ("159 million would be issued into escrow", inside Note 5 L2320–L2383). The half-release clause at L2366 means the eventual count can be lower than 159M; "capped" states a ceiling, not a fixed count, so the writer's reading is accepted |
| 6 | §7 say-on-pay denominator; "under 1%"; 580M composition | Yes | Yes | 2,795,303,255 ÷ (2,795,303,255 + 422,008,632) = 86.88% → 86.9%; ÷ (… + 12,839,978 abstentions) = 86.54% → 86.5% (8-K-2026-05-15.txt L537). "not more than 1%" is the proxy's phrase (DEF14A L693). 275M + 3M + 87M + 215M = 580M (10-K L660, L662, L670, L672) |
| 7 | §3 table R&D "(computed)" labels | Yes | Yes | Labels dropped; 19.2% / 27.8% printed at 10-K-FY2023.txt L1006, 22.7% at 10-Q L1303 |
| 8 | Outlook claim 6 | Yes | Yes | Now "The Q3 2026 release keeps the full-year 2026 non-GAAP operating expense figure at roughly $16.5 billion, not raised." Single direction under §9: Missed if the Full-Year 2026 table (present in both the Q1 release L526–L532 and the Q2 release L552–L558, so recurring) shows a higher figure; Dropped if the table disappears; Met if roughly $16.5B. A lowered figure would be graded on the "not raised" clause; acceptable. Quote unchanged and verbatim (transcript.txt L252) |
| 9 | Outlook §4 "GAAP margin or EPS in the remarks" | Yes | Yes | Removed; the remaining "Not guided" items (2026 adjusted FCF, segments, gross-vs-net capex, 2027 opex, 2027 debt retirement) are all genuinely absent from transcript.txt |
| 10 | Unused `[Q2 2026 slides, p.N]` Sources rows | Yes | n/a | Removed from both files. Tag prefixes used now map one-to-one to Sources rows: business.md 15 prefixes / 15 rows; outlook.md 6 / 6 |
| 11 | §3 "which is why gross margin slid" (optional) | Yes | Yes | Now "a large part of why gross margin slid …"; the $3.3B Intel 7 impairment context is at 10-K-FY2025.txt L698 |

**11 of 11 applied and faithful.**

### 2. Reviewer's cycle-1 direct fixes

All survived: business.md TSMC, GPUs, consolidated (company-wide), Mobileye / IMS / Altera / restructuring glosses, NAND, gross-vs-operating-margin sentence, CHIPS Act, dilution, finance leases, Arm, write-downs, risk production, receivables, China "(computed)", principal accounting officer, vest, goodwill, S&P 500, say-on-pay, bridge loan, notes (bonds), "$3.8B of debt comes due in 2027", x86 glossary wording, Amortization entry, proxy gloss in Sources. outlook.md: intro line, "(6.5 percentage points)", Apollo-buyout note, "The CEO:", "Stated priorities:", Google Cloud rewording, inference, edge, backlog, purpose-built silicon, sequentially, trimmed "Not sharpenable".

### 3. Other writer changes in the second pass

Word-trimming only (about 40 sentences tightened: "has been two businesses in one company", "without restating numbers", "Adding up the segments removes that internal sale", "unassigned costs", "recovered to 40.4%", "Without the buyout", "Return on capital, plainly", "Pay tracks this report's numbers", etc.). Each was read against its tag; no number, quote, tag, claim or indicator changed. The §4 opening sentence "In cash, from FY2022 through FY2025, not at all" was dropped; the paragraph still makes the point with the sourced figures. §1 "the only US company doing both leading-edge chip research and high-volume manufacturing" matches 10-K L342 ("in the U.S., where we are the only company conducting both leading-edge logic R&D and high-volume manufacturing").

### 4. Word counts (shared counter `/tmp/intc-orch/wc_prose.py`)

- business.md: **2,905** prose words (2,929 after cycle-1 fixes; 2,771 original). Within 2,000–3,000.
- outlook.md: **1,195** prose words (1,199; 1,200 original). Within 800–1,200.

### 5. As-of re-check

Grep of both drafts for dates after 2026-07-24: only the "Written 2026-09-07" header lines and forward-looking "Q3 2026 call / release", "Q4 2026", "October 2026" inside claims. Nothing post-cutoff is used as fact.

### 6. Open note for the owner (not a REVISE item; cycle limit reached)

- **business.md §4, last prose paragraph:** "Intel carries $105.7 billion of factories and equipment and, until Q2 2026, earned no operating profit on them". True on an annual basis for FY2024 and FY2025 (operating losses of $(11,678)M and $(2,214)M, 10-K-FY2025.txt L1757) but imprecise at finer grain: FY2023 operating income was $93M (L1757) and GAAP operating income was positive in Q3 2025 ($0.7B) and Q4 2025 ($0.6B) (slides.txt p.6 footnote 2, L108). The sentence was in the original draft and the reviewer did not flag it in cycle 1. Suggested owner edit, no new sources needed: "…and earned an operating loss on them in FY2024 and FY2025; whether Q2's $1.8 billion …". No number in the report is affected.

### 7. Direct fixes in cycle 2

None. No typo, tag or page-number error was found in the revised drafts.

### Final verdict: **PASS**

Both files meet the §6/§7 skeletons, all figures and quotes verify against the cached sources, all 11 claims meet §9, all 8 indicators anchor to recurring disclosures, both files are inside the §3 length targets, and nothing post-cutoff appears. The single open note above is a wording precision point for the owner, not a failing item.

## Orchestrator note (after cycle 2)

The one open item from cycle 2 was applied by the orchestrator rather than left to the owner, because it is a one-line wording correction verified against the cached source and business.md is frozen after this run: §4 "until Q2 2026, earned no operating profit on them" → "earned an operating loss on them in FY2024 and FY2025" (FY2023 operating income was +$93M [10-K FY2025, Item 8, line 1757 of the cached text]; FY2024 and FY2025 were losses of $(11,678)M and $(2,214)M). Existing tags on the sentence already support the new wording. No number, quote, claim or indicator changed. Word count after the fix is recorded below by the orchestrator.
2906	business.md
1195	outlook.md
