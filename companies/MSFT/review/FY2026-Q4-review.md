# Microsoft Corporation (MSFT) — Reviewer report, Q4 FY2026 (quarter ended June 30, 2026)

_Review cycle 1 of 2 (first research run; no blind re-grade applies). Reviewed 2026-09-08 against `companies/MSFT/sources/FY2026-Q4/` only (cutoff 2026-07-29: call and 10-K both that day). Every number and quotation at stake was checked against the cached source TEXT (five 10-Ks, the Q3 10-Q, the 2025 proxy, five 8-Ks, both transcripts, both releases, the slides, both outlook decks, the IR workbook), not the gatherers' notes. Greps were `grep -F` on full lines (host grep is ugrep; filings use curly apostrophes). Line numbers below refer to the cached `.txt` files. Word counts by `python3 -P /tmp/msft-orch/wc_prose.py`: business.md 2,498 before fixes / 2,634 after; outlook.md 992 before / 1,004 after (targets 2,000–3,000 and 800–1,200)._

**Cycle 1 verdict: REVISE** (four small factual items, all in business.md; nothing structural). **Final verdict after cycle 2: PASS** (see the "Cycle 2" section at the end). Citation spot-check: 131 items (every cell of the §2 product-line and segment tables, the §3 economics and segment-margin tables, the §4 cash table, the §7 capital-allocation table, every cell of outlook §1, all 21 guidance items in outlook §4 word for word, all 11 claim quotes in §5, and 39 prose sentences or quote blocks), 127 PASS, 4 FAIL, 1 FAIL withdrawn with evidence (§3d, FY2024 debt). Every computed ratio re-derives. Every transcript quote is character for character and attributed to the right speaker and section. Nothing after 2026-07-29 is used. Jargon was fixed directly (20 edits, logged in "Direct fixes").

---

## 1. Rubric result (§14)

| # | Question | Answer | Reasoning |
|---|---|---|---|
| 1 | Can I explain what this company does, and who pays it, in two sentences? | **Yes** | §1 opens with "sells the software that offices run on and rents out the computers that run it", then names each payer: companies per employee for Microsoft 365, by usage for Azure, PC makers per Windows licence, consumers for Xbox and subscriptions, advertisers on Bing, Edge, Copilot and LinkedIn. |
| 2 | Do I know exactly what would kill it, and what the early warning sign is? | **Yes** | §6 ranks six scenarios. Each of 1–4 and 6 names an early warning tied to a recurring line (Azure constant-currency growth vs capex, Microsoft Cloud gross margin vs the 64% guided, Intelligent Cloud margin, the related-party revenue and receivable lines, RPO ex-OpenAI vs total, Copilot seat adds vs the 6% seat growth, a named case in the contingencies note). #5 (breach) honestly names only "another 8-K". |
| 3 | Do I know why the margins are what they are, and whether cost scales with usage? | **Yes** | §3 states it plainly: licences cost nothing extra per copy, cloud users consume servers and power, AI answers consume far more; the three economies of scale from the 10-K; the two useful-life changes; two-thirds of capex in short-lived chips; Microsoft Cloud gross margin 72% → 66% "driven by continued investments in AI infrastructure". After the direct fixes, gross margin and operating margin are glossed at first prose use. |
| 4 | Could I predict what the scorecard will check next quarter, from §5 of the outlook alone? | **Yes** | Eleven claims, each with a number or an observable event, the four sharpenings labelled, the one multi-quarter claim (Xbox FY2027) labelled with its horizon. Only claim 4 is headline revenue; no EPS claim. |
| 5 | Did nothing in the report require knowledge I don't have? | **Yes, after fixes** | Before fixes: on-premises, seats, gross margin, operating margin, free cash flow, non-GAAP, recapitalization, net property and equipment, AAA, unearned revenue, AI agents, bookings, impairment, receivable, transfer pricing, pay ratio, MAI and "frontier model companies" were used without a plain gloss; the glossary defined Goodwill, a term never used. All fixed directly (see "Direct fixes"). |

## 2. Skeleton and rules check

**business.md**

| Requirement | Result |
|---|---|
| `# <Company> — The Business`; `_As of <QLABEL>. Written <date>._` with calendar parenthetical | OK: "Q4 FY2026 (quarter ended June 30, 2026). Written 2026-09-08." |
| §1–§8 headings present, in order, none skipped | OK (lines 4, 12, 49, 85, 110, 120, 138, 160). §1 has the history paragraph; §6 carries customer concentration; §8 has name / why / where for each indicator |
| `_Proposed — owner to review and lock._` under §8 | OK (line 162) |
| §2 segment table, five fiscal years | OK: FY2022 (original basis) + FY2023 (recast) + FY2024 (recast) + FY2025 + FY2026, with the mixed-basis note and the old-basis FY2024 figures stated; plus a four-year product-line table on the recast basis with FY2022 explicitly left out |
| §3 table: revenue, gross margin, operating margin, capex, capex/revenue, five years | OK, plus finance-lease additions, the company's own capex figure, depreciation and Microsoft Cloud gross margin; second table gives segment operating income and margins |
| §4 table, five years | OK (12 rows FY2022–FY2026) |
| §7 capital-allocation table | OK, five years |
| Glossary, Sources | Both present. Glossary now 11 entries, one sentence each, all used in the text. Sources maps all 18 tag prefixes to cached files, states the tier, and says the call tags name section and speaker because the transcripts have no page numbers |
| Length 2,000–3,000 | 2,634 after fixes; in range |
| Indicators 5–8, anchored to recurring disclosures (§8) | 8 indicators. #1, #2, #4, #5, #6, #7 are release, slide, workbook or statement lines that appear every quarter. #3 and #8 each carry an "excluding OpenAI" component that so far comes only from the call and the business-highlights slide (two quarters in the sources); the core of each (the RPO balance, the bookings growth rate) is a recurring slide line. Acceptable; if the ex-OpenAI figure disappears, treat that as a 🔇 signal on that half, not a failure of the indicator |

**outlook.md**

| Requirement | Result |
|---|---|
| `# <Company> — Outlook as of <QLABEL>` with calendar parenthetical | OK |
| `_Transcript source tier: … Written <date>._` | OK: "company-published", matching MANIFEST tier 1 |
| §1 table, one row per proposed indicator, three columns | OK, 8 rows, all cells filled; each cell tagged; PBP/IC/MPC abbreviations expanded beneath |
| §2, §3, §4 (verbatim guidance), §5 | OK |
| §6 Tone shift omitted on first run | OK |
| Sources | OK, 9 tag prefixes mapped |
| Length 800–1,200 | 1,004 after fixes |
| Claims 6–12; single direction; one thing to check; verbatim quote and tag under each | OK: 11 claims. None is either/or. Sharpenings labelled in claims 1, 3, 5, 6 ("Our sharpening of …"). Claim 5's 48.9% base is labelled computed and re-derives (37,961 / 77,673). Claim 11 states its horizon (FY2027 10-K) and that it carries. No disclosure checks are used, so the quarter-vs-year-to-date rule does not arise. Claim 7 has two parts (a count is disclosed, and it is above 30 million); both are observable on the same call, so it can still be graded mechanically. Headline revenue is one claim of eleven; EPS none |

## 3. Citation spot-check

Legend: PASS / FAIL. Every "(computed)" cell was re-derived from the cited source figures.

### 3a. business.md §2 product-line table (every cell; FY2024–FY2026 from 10-K FY2026 Note 18 lines 3774–3792, FY2023 from 10-K FY2025 Note 18 lines 3713–3731)

| # | Row | FY2023 / FY2024 / FY2025 / FY2026 | Source lines | Result |
|---|---|---|---|---|
| A1 | Server products and cloud services | 65,007 / 79,828 / 98,435 / 129,425 | FY2025 3713; FY2026 3774 | PASS |
| A2 | Microsoft 365 Commercial | 66,949 / 76,969 / 87,767 / 101,997 | 3715; 3776 | PASS |
| A3 | XBOX ("Gaming" through FY2025) | 15,466 / 21,503 / 23,455 / 21,790 | 3717 ("Gaming"); 3778 ("XBOX") | PASS, rename correctly noted |
| A4 | LinkedIn | 14,989 / 16,372 / 17,812 / 19,817 | 3719; 3780 | PASS |
| A5 | Windows and Devices | 17,147 / 17,026 / 17,314 / 17,084 | 3721; 3782 | PASS |
| A6 | Search advertising ("Search and news advertising" through FY2025) | 12,125 / 12,306 / 13,878 / 15,176 | 3723; 3784 | PASS, rename correctly noted |
| A7 | Microsoft 365 Consumer | 6,417 / 6,648 / 7,404 / 9,175 | 3729; 3786 | PASS |
| A8 | Dynamics | 5,796 / 6,831 / 7,827 / 9,006 | 3725; 3788 | PASS |
| A9 | Enterprise and partner services | 7,900 / 7,594 / 7,760 / 8,260 | 3727; 3790 | PASS |
| A10 | Other | 119 / 45 / 72 / 109 | 3731; 3792 | PASS |
| A11 | Total | 211,915 / 245,122 / 281,724 / 331,839 | FY2025 3648 block; FY2026 1754, 3794 | PASS |

### 3b. business.md §2 segment table (every cell)

| # | Row | Cells | Source lines | Result |
|---|---|---|---|---|
| B1 | PBP 63,364 / 94,151 / 106,820 / 120,810 / 139,996 | FY2022 orig; FY2023 recast; FY2024–26 | 10-K FY2024 3951; 10-K FY2025 3648; 10-K FY2026 3709 | PASS |
| B2 | IC 74,965 / 72,944 / 87,464 / 106,265 / 137,791 | same | FY2024 3953; FY2025 3658; FY2026 3719 | PASS |
| B3 | MPC 59,941 / 44,820 / 50,838 / 54,649 / 54,052 | same | FY2024 3955; FY2025 3668; FY2026 3729 | PASS |
| B4 | Total 198,270 / 211,915 / 245,122 / 281,724 / 331,839 | | FY2024 1925; FY2026 1754 | PASS |
| B5 | Note: old-basis FY2024 77,728 / 105,362 / 62,032; totals identical on both bases | | 10-K FY2024 1419–1423 and 3951–3955; recast quote 10-K FY2025 2075 | PASS |

### 3c. business.md §3 economics table (every cell) and segment operating income table

| # | Row | Re-derivation | Result |
|---|---|---|---|
| C1 | Revenue 198,270 / 211,915 / 245,122 / 281,724 / 331,839 | 10-K FY2024 1925; 10-K FY2026 1754 | PASS |
| C2 | Gross margin (computed) 68.4 / 68.9 / 69.8 / 68.8 / 67.9% | Gross margin 135,620 / 146,052 (FY2024 1935); 171,008 / 193,893 / 225,465 (FY2026 1764): 68.40 / 68.92 / 69.76 / 68.82 / 67.94 | PASS |
| C3 | Microsoft Cloud gross margin 70 / 72 / 71 / 69 / 66% | 10-K FY2022 1353 ("decreased slightly to 70%"); FY2023 1417 ("increased 2 points to 72%"); FY2024 1399 ("71%"); FY2025 1239 ("69%"); FY2026 1206 ("66%") | PASS |
| C4 | Operating margin (computed) 42.1 / 41.8 / 44.6 / 45.6 / 46.8% | Operating income 83,383 / 88,523 (FY2024 1943); 109,433 / 128,528 / 155,237 (FY2026 1772): 42.06 / 41.77 / 44.64 / 45.62 / 46.78 | PASS |
| C5 | Capex 23,886 / 28,107 / 44,477 / 64,551 / 115,948 | "Additions to property and equipment" FY2024 2157; FY2026 1984 | PASS |
| C6 | Capex / revenue (computed) 12.0 / 13.3 / 18.1 / 22.9 / 34.9% | 12.05 / 13.26 / 18.14 / 22.91 / 34.94 | PASS |
| C7 | Finance-lease assets added 4,234 / 3,128 / 11,633 / 20,511 / 24,608 | "Finance leases" supplemental lease line: 10-K FY2024 Note 14 line 3562 (11,633 / 3,128 / 4,234); FY2025 Note 13 line 3266 (20,511); FY2026 Note 13 line 3335 (24,608) | PASS |
| C8 | Cash capex plus finance leases (computed) 28,120 / 31,235 / 56,110 / 85,062 / 140,556 | sums re-derive exactly | PASS |
| C9 | … / revenue (computed) 14.2 / 14.7 / 22.9 / 30.2 / 42.4% | 14.18 / 14.74 / 22.89 / 30.19 / 42.36 | PASS |
| C10 | Company capex figure 29.2 / 31.9 / 55.7 / 88.2 / 145.3 | IR workbook CapEx sheet, "Fiscal Year 2022 … 2026" columns (financial-statements line 321) | PASS |
| C11 | Depreciation 12.6 / 11.0 / 15.2 / 22.0 / 34.3 | 10-K FY2023 3005 ("$11.0 billion, $12.6 billion"); 10-K FY2024 Note 7 line 2985; FY2025 Note 6 line 2755; FY2026 Note 6 line 2754 | PASS |
| C12 | Footnote: $26.7 billion received but unpaid at June 30, 2026 | 10-K FY2026 Note 6 line 2756 ("purchases of property and equipment remaining in accounts payable were $26.7 billion"); slide 6 "timing differences between receipt of goods and payment" | PASS |
| C13 | Segment operating income PBP 29,690 / 50,074 / 59,661 / 69,773 / 83,879 | 10-K FY2024 3961; FY2025 3654; FY2026 3715 | PASS |
| C14 | IC 33,203 / 28,411 / 37,813 / 44,589 / 56,972 | FY2024 3963; FY2025 3664; FY2026 3725 | PASS |
| C15 | MPC 20,490 / 10,038 / 11,959 / 14,166 / 14,386 | FY2024 3965; FY2025 3674; FY2026 3735 | PASS |
| C16 | Total 83,383 / 88,523 / 109,433 / 128,528 / 155,237 | FY2024 1943; FY2026 3745 | PASS |
| C17 | Segment margins (computed) 53/39/22; 56/43/24; 58/42/26; 60/41/27 | 53.2/38.9/22.4; 55.9/43.2/23.5; 57.8/42.0/25.9; 59.9/41.3/26.6 | PASS |

### 3d. business.md §4 cash table (every cell)

| # | Row | Source | Result |
|---|---|---|---|
| D1 | Net cash from operations 89,035 / 87,582 / 118,548 / 136,162 / 182,935 | 10-K FY2024 2135; FY2026 1962 | PASS |
| D2 | Cash capex (as C5) | | PASS |
| D3 | Free cash flow (computed) 65,149 / 59,475 / 74,071 / 71,611 / 66,987 | D1 − D2 re-derives exactly | PASS |
| D4 | FCF / revenue (computed) 32.9 / 28.1 / 30.2 / 25.4 / 20.2% | 32.86 / 28.07 / 30.22 / 25.42 / 20.19 | PASS |
| D5 | Net income 72,738 / 72,361 / 88,136 / 101,832 / 133,749 | FY2024 1951; FY2026 1780 | PASS |
| D6 | OpenAI net gains (losses) n/d / n/d / (1,482) / (4,763) / 6,530 | 10-K FY2026 1472 "Net (gains) losses from investments in OpenAI (6,530) 4,763 1,482". FY2022–FY2023: no OpenAI line exists in the FY2022–FY2024 non-GAAP tables (the FY2022 10-K's adjusted figures exclude tax items only, line 1571), so n/d is correct | PASS |
| D7 | Adjusted net income n/d / n/d / 89,262 / 105,452 / 128,786 | FY2026 1480; earlier years not reported on this definition | PASS |
| D8 | Stock-based compensation 7,502 / 9,611 / 10,734 / 11,974 / 12,405 | FY2024 2109; FY2026 1936 | PASS |
| D9 | Operating income per $1 of net PP&E (computed) 1.12 / 0.93 / 0.81 / 0.63 / 0.50 | Net PP&E 74,398 (FY2022 1975), 95,641 (FY2023 2063), 135,591 (FY2024 2025), 204,966 / 313,076 (FY2026 1854): 1.121 / 0.926 / 0.807 / 0.627 / 0.496 | PASS |
| D10 | Cash and short-term investments 104,757 / 111,262 / 75,543 / 94,565 / 76,843 | FY2022 1965; FY2024 2015; FY2026 1844 | PASS |
| D11 | Debt 49,781 / 47,237 / 51,630 / 43,151 / 40,294 | FY2022: 2,749 + 47,032 (FY2022 1995, 2007). FY2023: 5,247 + 41,990 (FY2024 2047, 2059). FY2024: **first ruled FAIL** because 2,249 + 42,688 = 44,937, not 51,630; **withdrawn** on finding the FY2024 balance sheet's separate line "Short-term debt \| 6,693 \| 0" (FY2024 2045; $6.7 billion of commercial paper, Note 11 line 3211): 6,693 + 2,249 + 42,688 = 51,630. FY2025: 2,999 + 40,152 = 43,151 (Note 10 "Total debt \| 43,151 \| 44,937", FY2025 2971). FY2026: 9,227 + 31,067 = 40,294 (Note 10 line 2954). Numbers correct; the row label "(computed sum of current and long-term)" omitted the short-term line, so it was aligned directly (Direct fix 5) | PASS (label fixed) |
| D12 | Finance-lease liabilities n/d / 17,067 / 27,145 / 46,172 / 66,594 | FY2023–FY2026 PASS (FY2024 3592; FY2025 3302; FY2026 3365). **FY2022 FAIL:** the cached 10-K FY2022 Note 14 line 3479 reads "Total finance lease liabilities \| $ \| 14,902 \| $ \| 12,541" and 10-K FY2023 line 3567 reads "Total finance lease liabilities \| $ \| 17,067 \| $ \| 14,902". The figure is disclosed; "n/d" is wrong. → REVISE item 1 | **FAIL (one cell)** |

### 3e. business.md §7 capital-allocation table (every cell)

| # | Row | Source | Result |
|---|---|---|---|
| E1 | Repurchases under the programs 28,033 / 18,400 / 11,960 / 13,000 / 16,719 | 10-K FY2024 Note 16 table "Total \| 32 \| $ \| 11,960 \| 69 \| $ \| 18,400 \| 95 \| $ \| 28,033" (line 3700); 10-K FY2026 Note 15 table "Total \| 36 \| $ \| 16,719 \| 31 \| $ \| 13,000 \| 32 \| $ \| 11,960" (line 3461) | PASS |
| E2 | Shares bought for employee tax 4,700 / 3,800 / 5,300 / 5,400 / 5,600 | FY2024 3708 ("$5.3 billion, $3.8 billion, and $4.7 billion"); FY2026 3469 ("$5.6 billion, $5.4 billion, and $5.3 billion"); footnote says stated in billions | PASS |
| E3 | Dividends paid 18,135 / 19,800 / 21,771 / 24,082 / 26,445 | FY2024 2149; FY2026 1976 | PASS |
| E4 | Dividends declared per share 2.48 / 2.72 / 3.00 / 3.32 / 3.64 | FY2024 2229; FY2026 2056 | PASS |
| E5 | Cash capex (as C5) | | PASS |
| E6 | Acquisitions 22,038 / 1,670 / 69,132 / 5,978 / 1,743 | FY2024 2159; FY2026 1986 | PASS |
| E7 | Shares outstanding 7,464 / 7,432 / 7,434 / 7,434 / 7,427 | FY2024 3678 "Balance, end of year \| 7,434 \| 7,432 \| 7,464"; FY2026 3439 "7,427 \| 7,434 \| 7,434" | PASS |

### 3f. outlook.md §1 indicator table (every cell)

| # | Row | This quarter / last quarter / expected | Result |
|---|---|---|---|
| F1 | Azure growth | 43% cc (43% reported): release line 204 "Azure and other cloud services revenue \| 43% \| 0% \| 43%". Q3: 39% cc (40% reported): Q3 release line 68. Expected "Growth between 39% to 40% in constant currency": Q4 outlook slide 4 | PASS |
| F2 | Microsoft Cloud | $59.3B +27%, 65%: release line 51; slide 7. Q3 $54.5B +29% (25% cc), 66%: Q3 release line 49; Q3 call line 261. "Roughly 64%": Q4 outlook slide 4 | PASS |
| F3 | Commercial RPO | $678B +84%, +25% ex-OpenAI, ~30%, 2.3 years: transcript line 287; 10-K Note 12 line 3289. Q3 $627B +99%, +26%, ~25%, ~2.5 years: Q3 call line 259 ("approximately two and a half years", "Roughly 25%") | PASS |
| F4 | Capex | $41.0B / $35.8B / $5.6B: slide 6. Q3 $31.9B / $30.9B / $4.7B: Q3 call lines 247–249. "Capital expenditures expected to increase to over $40 billion": Q4 outlook slide 3 | PASS |
| F5 | M365 Commercial cloud | 14% reported, 16% adjusted, seats +6%: slide 9. Q3 15% cc (19% reported): Q3 release line 54; seats 6%: workbook Metrics. Guidance "Growth between 13% to 14% in constant currency" / "15% to 16%": Q4 outlook slide 4 | PASS |
| F6 | Segments | Q4 37,847/21,900; 39,306/15,955; 12,854/2,748: release lines 180–184 and segment table (579 and tail); Q3 35,013/20,973; 34,681/13,753; 13,192/3,672: Q3 release 131–135, 524 and tail; also workbook Segment History lines 235–250. Guidance ranges: Q4 outlook slide 3 verbatim | PASS |
| F7 | OCF / FCF | $55.4B / $19.6B: release 517 (55,441), slide 22 (19,639). Q3 $46.7B: Q3 release 462 (46,679); $15.8B: Q3 call 251 | PASS |
| F8 | Bookings | +10% (+11% cc) / +18%: slide 7; transcript 285. Q3 −4% (−6% cc) / +7%: Q3 call 257. "Healthy growth on a growing expiry base when adjusted for OpenAI contracts in the prior year": Q4 outlook slide 4 | PASS |

### 3g. outlook.md §4 guidance (word for word against transcript.txt and outlook-slide-FY2027-Q1.txt)

| # | Item | Transcript line / slide | Result |
|---|---|---|---|
| G1 | Revenue $89.85–$90.95B, 16–17%; FY "double-digits" | 387; slide 3; FY slide 5 "grow double-digits", transcript 343 | PASS |
| G2 | PBP $36.7–$37.0B, 11–12% | 361 ("$36.7 to $37 billion"); slide 3 "$36.7 to $37.0 billion" | PASS |
| G3 | IC $40.95–$41.25B, 33–34% | 373; slide 3 | PASS |
| G4 | MPC $12.2–$12.7B | 379; slide 3 | PASS |
| G5 | Azure ~45% cc; H1 FY2027 accelerate vs H2 FY2026 | 375; slide 4; slide 5 | PASS |
| G6 | M365 Commercial cloud ~15% reported / 16% adjusted; acceleration through the year | 363; slide 4; slide 5 | PASS |
| G7 | M365 Commercial products mid-single-digit growth (Q1), mid-single-digit decline (FY); Server products low- to mid-single-digit decline (Q1), mid-single-digit decline (FY) | 365, 377, 337; slides 4, 5 | PASS |
| G8 | Windows OEM and Devices: low twenties (Q1), high-teens (FY) | 381, 339; slides 4, 5 | PASS |
| G9 | COGS $29.6–$29.8B, 23–24% | 389; slide 3 | PASS |
| G10 | Opex $16.8–$16.9B, 7–8%; FY mid- to high-single digits | 389, 343; slides 3, 5 | PASS |
| G11 | Operating margin "relatively flat year-over-year"; FY "down less than a point" | 389, 345; slides 3, 5 | PASS |
| G12 | Microsoft Cloud gross margin "relatively stable quarter-over-quarter" | 357; slide 4 | PASS |
| G13 | OI&E ex-OpenAI roughly $(100) million | 391 ("roughly negative $100 million"); slide 3 "$(100) million" | PASS |
| G14 | Tax ~20% Q1 and FY | 393, 347; slides 3, 5 | PASS |
| G15 | Capex "over $50 billion" Q1; FY grows y/y; CY2026 ~$175B | 397, 343, 331; slides 3, 5 | PASS |
| G16 | FCF "remain free cash flow positive" | 345; slide 5 | PASS |
| G17 | Verbatim block: "We expect CapEx spend will be over $50 billion including the lease reclassification impact from the useful life update." | 397, character for character | PASS |
| G18 | Verbatim block: "Outside of this useful life impact … approximately $175 billion." | 331 | PASS |
| G19 | Verbatim block: "At the company level … double-digit revenue and operating income growth." / "Even as we invest … free cash flow positive in FY27." | 343, 345 | PASS |
| G20 | Verbatim block: "In Azure, we expect revenue growth of approximately 45% … we continue to expect H1 growth to accelerate." | 375 | PASS |
| G21 | "Not guided: earnings per share, a FY2027 revenue growth rate, a FY2027 capex dollar figure, headcount"; "the release carries no guidance" | grep of transcript and slides confirms none of these is given; release line 118–120 defers guidance to the call | PASS |

### 3h. outlook.md §5 claim quotes

All eleven quotes are character for character in `transcript.txt` and attributed to the right speaker and section: claim 1 line 375 (Hood); 2 line 397 (Hood); 3 line 357 (Hood); 4 line 387 (Hood); 5 line 389 (Hood) with the 48.9% base re-derived from the workbook Segment History sheet (operating income 37,961 / revenue 77,673, lines 254 and 251; values stored without thousands separators); 6 line 363 (Hood), both fragments; 7 line 143 (Nadella); 8 line 331 (Hood); 9 line 343 (Hood); 10 line 313 (Hood); 11 line 237 (Nadella) with $21,790 million from 10-K Note 18 line 3778. **11 PASS.**

### 3i. Prose sentences and quote blocks, both files

| # | Sentence / quote | Found at | Result |
|---|---|---|---|
| P1 | §1 "Founded in 1975" | 10-K FY2026 line 177 (Item 1) | PASS |
| P2 | §1 Nadella joined 1992, CEO February 2014, Chairman June 2021; Hood CFO May 2013 | 519, 525 (Item 1, executive officers) | PASS |
| P3 | §1 ZeniMax March 2021 $8.1B; Nuance March 2022 $18.8B; Activision October 2023 $75.4B | 10-K FY2023 line 931 (Item 1A, as tagged); 10-K FY2022 line 2917 (Note 8, as tagged); 10-K FY2026 line 2762 (Note 7, as tagged) | PASS |
| P4 | §1 "The cached filings do not date the LinkedIn and GitHub purchases" | **FAIL:** DEF14A-2025 line 1351 (Compensation Discussion and Analysis): "LinkedIn has continued to deliver strong growth and engagement since its acquisition in December 2016." GitHub is indeed undated in every cached filing (no hit for "acquisition of GitHub" / "acquired GitHub" in any 10-K or the proxy). → REVISE item 3 | **FAIL** |
| P5 | §1 OpenAI partnership "was originally established in 2019", extended October 2025 and April 2026 | 1088 (Item 7) | PASS verbatim |
| P6 | §1 recast quote "most notably bringing the commercial components of Microsoft 365 together in the Productivity and Business Processes segment", FY2024 and FY2023 restated | 10-K FY2025 line 2075 (Note 1) | PASS verbatim |
| P7 | §1 first two segments 91% of operating income; 51% US (computed) | (83,879 + 56,972) / 155,237 = 90.7%; 170,794 / 331,839 = 51.5% (Note 18 lines 3745, 3753) | PASS |
| P8 | §2 "is mainly affected by a combination of continued installed base growth and average revenue per user expansion"; cloud +17% on seats +6%; "driven by Microsoft 365 Copilot and Microsoft 365 E5" | 277 (Item 1); 1275 (Item 7) | PASS verbatim |
| P9 | §2 "Azure revenue is mainly affected by infrastructure-as-a-service and platform-as-a-service consumption-based services"; "Azure surpassed $100 billion, up 41%"; server products +1% | 327 (Item 1); transcript 33 (Nadella); 1310 (Item 7) | PASS verbatim |
| P10 | §2 shares 31% / 39% / 11% (computed) | 101,997 / 331,839 = 30.7%; 129,425 / 331,839 = 39.0%; (19,817 + 9,006 + 9,175) / 331,839 = 11.5% | PASS |
| P11 | §2 "XBOX was the one large line to shrink in FY2026, down 7% with hardware down 29%" | 1336 confirms −7% and −29%. **FAIL on "the one large line":** Windows and Devices also fell, 17,314 → 17,084, Item 7 line 1333 "Windows and Devices revenue decreased $230 million or 1%". → REVISE item 4 | **FAIL (wording)** |
| P12 | §2 Microsoft Cloud $214.4B, up 27%, 65% (computed); fourth-quarter seasonality | 3796 (Note 18): $214.4B vs $168.9B = +26.9%; 214.4 / 331.8 = 64.6%; 1112 (Item 7) "Fourth quarter revenue is driven by a higher volume of multi-year contracts". The draft's "most multi-year contracts" overstated "a higher volume"; aligned directly (Direct fix 3) | PASS after fix |
| P13 | §3 licences booked on delivery; "benefits from three economies of scale", "diverse customer, geographic, and application demand patterns" | Note 1 line 2110 ("Revenue from distinct on-premises licenses is recognized at the point in time…"); 191 (Item 1) | PASS verbatim |
| P14 | §3 cost shares 32% / 11% / 8% / 2%; opex +7% vs revenue +18%; Intelligent Cloud cost of revenue +44%; cloud GM 72% → 66% "driven by continued investments in AI infrastructure and growing AI product usage" | 106,374 / 35,562 / 26,710 / 7,956 over 331,839 = 32.1 / 10.7 / 8.0 / 2.4; 1208 ("7%"), 1196 ("18%"); 1240 ("44%"); 1206 | PASS |
| P15 | §3 July 2022 lives "from four years to six years", "$3.7 billion"; FY2027 "from 15 to 25 years", "a minimal benefit to FY27 operating income"; "roughly $190 billion" (April) → "approximately $175 billion" (July); "Investment expectations remain unchanged" | 10-K FY2023 1307 (Item 7); transcript 329, 331 (Hood); Q3 transcript 347 (Hood); Q1 FY2027 outlook slide 5 | PASS verbatim |
| P16 | §3 two-thirds short-lived, "primarily CPUs and GPUs"; leases not commenced $329.1B, FY2027–FY2033; purchase commitments $194.1B, $169.0B in FY2027; Hood COGS quote | slide 6; 10-K 3403 (Note 13); 1564 (Item 7 contractual obligations: "Purchase commitments (d) \| 169,008 \| 25,052 \| 194,060"); transcript 463 (Hood, answering Moerdler/Bernstein) | PASS verbatim |
| P17 | §3 shared costs, "mainly AI infrastructure and marketing", "based on relative gross margin" | 3697 (Note 18): "Operating expenses that are allocated primarily include those relating to our investments in AI infrastructure and training, as well as marketing … generally allocated based on relative gross margin" | PASS |
| P18 | §4 operating cash flow 137% of net income; revenue up 67%; FCF between $59B and $74B | 182,935 / 133,749 = 136.8%; 331,839 / 198,270 = 1.674; D3 row | PASS |
| P19 | §4 "an approximate 25% interest on an as-converted basis"; equity method; net losses $1.5B / $4.8B, gain $6.5B; "dilution gain from the OpenAI Recapitalization"; "exclude net gains and losses from investments in OpenAI"; $17.28 vs $17.95 | 2218 (Note 1); Note 3 (line 2341: "$6.5 billion of net gains, $4.8 billion of net losses, and $1.5 billion of net losses … primarily relate to the dilution gain from the OpenAI Recapitalization"); 1192; 1486, 1786 | PASS verbatim |
| P20 | §4 $1.12 → $0.50; AAA; cash exceeds debt; finance-lease liabilities $66.6B exceed debt | D9; 2586 (Note 5: "our long-term unsecured debt rating was AAA"); 2954 (Note 10 total debt 40,294 vs cash 76,843); 3365 | PASS |
| P21 | §5 "Enterprise Mobility + Security, the cloud portion of Windows Commercial"; unearned revenue $75.7B; RPO $678B, ~30% within twelve months, 2.3 years | 264 (Item 1); 3287 (Note 12: 75,712); 3289 | PASS verbatim |
| P22 | §5 E7 bundles Copilot and E5 with Agent 365, a "control plane" | transcript 175, 137 (Nadella) | PASS |
| P23 | §5 direct / partners / PC makers / volume licensing; 88 datacenters; "roughly double our overall capacity in just two years"; rights "are extended through 2032" | 479 (Item 1), 374, 1524; transcript 39 ("bringing the total to 88 this year"), 43; 8-K 2025-10-28 line 119 | PASS verbatim |
| P24 | §5 "Paid Microsoft 365 Commercial seats have grown 6% in each of the last eight quarters [IR workbook FY26Q4, Metrics]" | **FAIL:** the Metrics sheet (financial-statements line 191) and slide 9 show 6% for five quarters (Q4 FY2025, Q1–Q4 FY2026) plus 6% for FY2025 and FY2026 as whole years; the 10-K FY2025 (line 1304) gives 6% for FY2025 as a year; the 10-K FY2024 (line 2013) gives no percentage. Eight consecutive quarters are not in the cached sources. → REVISE item 2 | **FAIL** |
| P25 | §5 bookings excluding OpenAI up 18%; "licenses running in multi-cloud environments" | transcript 285 (Hood); 10-K 1310 | PASS |
| P26 | §6 #1 depreciation $22.0B → $34.3B; net PP&E $313B; "are in advance of fully developed revenue streams"; "may lead to impairment of assets on our balance sheet"; 64% guided in April; IC operating income $57.0B | 2754; 1854; 626, 634 (Item 1A); Q4 outlook slide 4; 3725 | PASS verbatim |
| P27 | §6 #2 "from commercial arrangements with OpenAI, inclusive of revenue-sharing payments" $24.1B; 7.3% / 17.5% (computed); $6.0B receivable; "has contracted to purchase an incremental $250B of Azure services", "will no longer have a right of first refusal"; RPO +25% ex-OpenAI vs +84%; $11.9B of $13.0B | 2218; 24.1 / 331.8 = 7.26%, 24.1 / 137.8 = 17.5%; 8-K 2025-10-28 line 140; transcript 287; 2218 | PASS verbatim |
| P28 | §6 #3 "every model is substitutable"; "declines as a result of competition, commoditization, or other market forces"; PBP operating income $83.9B | transcript 85 (Nadella prepared remarks); 636 (Item 1A); 3715 | PASS verbatim |
| P29 | §6 #4 no antitrust case named; "Government agencies closely scrutinize us under U.S. and foreign competition laws"; EU AI Act; Irish DPC 2024 decision, appealed, fine not stated; IRS "$28.9 billion plus penalties and interest", "will vigorously contest"; about a fifth of net income; "We derive substantial revenue from government contracts" | Note 14 (3411–3421) names only the IDPC matter and "assessing a fine" with no amount; 809, 812 (Item 1A); 3249 (Note 11); 28.9 / 133.7 = 21.6%; 839 | PASS verbatim |
| P30 | §6 #5 "a nation-state associated threat actor used a password spray attack to compromise a legacy test account and, in turn, gain access to Microsoft email accounts"; source code; "our reputation and customer relationships" | 690 (Item 1A) | PASS verbatim |
| P31 | §6 #6 Windows and Devices 5% (computed); "in the high-teens"; users turning to phones and tablets; MPC $14.4B, 9% (computed) | 17,084 / 331,839 = 5.1%; transcript 339; 592 (Item 1A, "Users continue to turn to these devices"); 14,386 / 155,237 = 9.3% | PASS |
| P32 | §6 concentration: no 10% customer FY2024–FY2026; "There are few qualified suppliers for certain components of our servers and devices" | 3747 (Note 18); 453 (Item 1) | PASS verbatim |
| P33 | §7 Althoff "Chief Executive Officer, Microsoft Commercial Business" October 2025; Coleman CHRO March 2025; 13 directors; Nadella the only non-independent of the 12 nominees; Peterson Lead Independent Director; Rodriguez / Di Sibio / Hoffman | 521, 523; 10-K signature block lines 4284–4332 (Nadella + 12 directors = 13; tag added, Direct fix 16); DEF14A 101, 455, 619; 8-K 2025-09-30 line 56 with the 2025-12-05 meeting (8-K 2025-12-05); 8-K 2026-05-13 line 58 ("effective May 13, 2026"); 8-K 2026-06-02 line 56. The 8-K says Hoffman will not stand for re-election "at the Company's 2026 annual shareholder meeting"; it does not say December, so "leaves in December 2026" was aligned to the source (Direct fix 16) | PASS after fix |
| P34 | §7 pay $96.5M, stock $84.2M; "$50 million, a level unchanged since fiscal year 2022"; FY2025 PSA metrics and weights verbatim; above the 60th percentile; 70% / 30%; security, product and culture categories; 480 to 1; 91.94% | DEF14A 1977 (96,496,790; 84,245,496); 1225; 1569–1575 ("Azure and Other Cloud Services Revenue Growth \| 35%", "Microsoft Cloud Revenue Growth, excluding Azure and Other Cloud Services \| 35%", "Consumer Services Revenue Growth \| 15%", "Xbox Content and Services Revenue Growth \| 15%"); 1475; 1227, 1513; 1677–1685 (Security, Product/Customers & Stakeholders, Culture); 2319; 8-K 2025-12-05 line 118 | PASS verbatim |
| P35 | §7 Nadella 900,572 shares (<1%); 18 people 2,279,620; 0.03% (computed); Vanguard 8.95%, BlackRock 7.30%; trading plan "sell 80% of the net vested shares", vest August 31, 2026 | DEF14A 2507, 2517, 2459, 2461; 2,279,620 / 7,427 million = 0.031%; 10-Q 2810 (Part II Item 5 begins line 2803) | PASS verbatim |
| P36 | §7 FY2022 returns about twice capex; FY2026 capex 2.4× returns; $0.91 quarterly; $40.6B of $60B (September 2024); "will continue to invest in capital expenditures to support growth in our cloud offerings"; "in the form of dividends" | (32,696 + 18,135) / 23,886 = 2.1; 115,948 / (22,271 + 26,445) = 2.38; 3485; 3445; 1596; 1592 | PASS verbatim |
| P37 | outlook §2 seven quotes | release 31 (Nadella); transcript 85 and 427 (Nadella prepared remarks and answer to Keirstead/UBS, as tagged); 179; 313 (Hood); Q3 transcript 349 (Hood); 559 (Hood, answering Borges/Goldman Sachs). Q4 Hood gives no end date for constraints (441: "demand continues to exceed available supply, and that certainly remains true") | PASS verbatim |
| P38 | outlook §3 quotes: gigawatt; double capacity; "100,000 Foundry customers…"; "over 30 million paid…"; "50 million users"; "accelerated over 60% quarter-over-quarter"; "over 11,000 models…"; "5X"; nearly 90% "customers outside of frontier model companies"; "a complete multi-model agentic security system"; "return the business to growth in fiscal 2027"; no Copilot revenue figure; no security revenue in the Zelnick answer | transcript 43, 131, 143, 191, 195, 71, 73 (Nadella); 291 (Hood); 205; 237; only "Copilot revenue accelerated over 60%" exists, no dollar figure; lines 531–543 contain no revenue number | PASS verbatim |
| P39 | outlook §1 lead: "Last quarter" is Q3 FY2026 (quarter ended March 31, 2026); "expected" is the outlook slide of April 29, 2026 | Q3 release header; outlook-slide-FY2026-Q4 slide 1 "April 29, 2026" | PASS |

**Verbatim character-for-character checks (at least three required):** G17–G20 (four guidance blocks), all eleven §5 quotes, P5, P6, P8, P13, P15, P16, P19, P21, P26–P30, P34, P37, P38. All pass.

**Totals:** 131 items checked; 127 PASS; 4 FAIL (D12 one cell, P4, P11, P24); 1 FAIL withdrawn with evidence (D11).

## 4. Jargon audit

Thinking as a 16-year-old, term by term:

| Term | Status before review | Action |
|---|---|---|
| Azure, constant currency, RPO, finance lease, equity method, GPU, token, OEM, capex, depreciation, Copilot | Glossary, one sentence each | OK |
| Goodwill | Glossary entry, but the word never appears in either file | Entry removed (Direct fix 18) |
| E5, E7 | §5: "higher-priced suites, 'Microsoft 365 Copilot and Microsoft 365 E5'"; "The new E7 suite bundles Copilot and E5 with Agent 365" | OK, the reader learns they are the premium plans |
| Agent 365, "control plane" | Glossed "for governing AI agents" | OK; "AI agents" itself now glossed (Direct fix 11) |
| Foundry | outlook: "its platform for building AI applications" | OK |
| MAI | outlook: only inside a quote | Fixed: "(MAI: Microsoft's own models)" |
| "frontier model companies" | outlook: only inside a quote | Fixed: "(the companies that build the leading AI models)" |
| as-converted | "(counting all convertible holdings as shares)" | OK |
| COGS | "COGS being cost of revenue" | OK |
| expiry base | outlook §1: "(expiry base: contracts coming up for renewal)" | OK |
| on-premises | §1, §2, §5 bare | Fixed at first use: "(software run on the customer's own machines)" |
| seats | §2 bare | Fixed: "seats (paid users)" |
| gross margin, operating margin | Tables, then prose in §3 without definition | Fixed at first prose use, one clause each |
| free cash flow | Table row, then prose | Fixed: "(operating cash flow minus capex)" |
| non-GAAP / GAAP | Table row labels | Fixed: one sentence in the §4 table footnote |
| recapitalization | §4 bare | Fixed: "(a reorganisation of who owns what)" |
| net property and equipment | §4 bare | Fixed: "(buildings and machines at book value, after depreciation)" |
| AAA | §4 bare | Fixed: "the credit rating is AAA, the highest grade" |
| unearned revenue | §5 bare | Fixed: "(cash collected for service not yet delivered)" |
| commercial bookings | §5 and indicator 8 bare | Fixed at first prose use: "(the value of new contracts signed in the period)" |
| impairment | §6 #1 inside a quote | Fixed: ", that is, to writing down their value" |
| receivable | §6 #2 bare | Fixed: "(invoiced but not yet paid)" |
| transfer pricing | §6 #4 bare | Fixed: "(how profit is split between its units in different countries)" |
| pay ratio | §7 bare | Fixed: "(CEO pay to the median employee's)" |
| infrastructure-as-a-service, platform-as-a-service, installed base, average revenue per user | Inside verbatim 10-K quotes, immediately followed by the draft's plain restatement ("Azure customers pay for what they use"; "the gap is price per user") | OK, left as quoted |
| moat | Spec vocabulary, used in the §5 sense the whole library uses | OK |
| gigawatt, datacenter, cloud, usage-based pricing, multi-year contracts, buyback, dividend | Name-inferable or plain | OK |
| PBP / IC / MPC | Expanded beneath the outlook §1 table | OK |
| H1 | Only inside a verbatim guidance quote; the table row above it says "first half of FY2027" | OK |

Glossary now holds 11 entries, each one sentence, each used in business.md or outlook.md.

## 5. Invented-number check

| Item | Finding |
|---|---|
| Every "(computed)" cell and percentage in both files | Labelled and re-derived exactly (§3 above) |
| §3 "$26.7 billion was received but unpaid … (our inference)" | The $26.7 billion is a stated fact (Note 6 line 2756); the inference is only the explanation of why the company's capex exceeds the cash line. Correctly tagged; the label is over-cautious, not wrong |
| §3 "AI changes it again, because a Copilot answer needs far more computing than an email (our inference)" | Labelled |
| §4 "Our inference: new datacenters earn less per dollar because they are bought ahead of the revenue meant to fill them" | Labelled; consistent with the 10-K's "in advance of fully developed revenue streams" |
| §5 "On Azure the estate is the customer's own applications and data, costly to move again (our inference)" | Labelled |
| §6 #3 "It also means no model … commands a premium for long (our inference)"; §6 #5 "(our view)" | Labelled |
| §6 #1 early-warning thresholds (two quarters of slowing; Intelligent Cloud margin below 40%) | Analyst-chosen watch levels, not presented as facts; the 64% is sourced to the April outlook slide |
| §7 "Our observation: every stock metric is a revenue growth rate" | Labelled; true of the four FY2025 PSA metrics quoted |
| §7 "13 directors" | Not in the tags cited; confirmed by the 10-K signature block (Nadella plus twelve directors). Tag added (Direct fix 16) |
| §4 FY2022 finance-lease liabilities "n/d" | **Wrong:** $14,902 million is in two cached 10-Ks (REVISE item 1) |
| §5 "each of the last eight quarters" | **Unsupported:** sources show five quarters (REVISE item 2) |
| §1 "The cached filings do not date the LinkedIn … purchase" | **Wrong:** proxy line 1351 gives December 2016 (REVISE item 3) |
| outlook §3 "Nearly 90% of cloud revenue" | Transcript line 291 (full-year figure); the sentence says "cloud revenue" without "for the year", acceptable since the tag points to the annual remark |
| Every other figure in both files | Carries a tag that supports it; no untagged figure found |

## 6. As-of check

- Latest-dated facts used: the July 29, 2026 call, 10-K and outlook deck; Project Perception "earlier this week" (transcript line 205); the June 2026 dividend declaration (payable September 10, 2026, a declared fact as of the 10-K). All within cutoff.
- The transcript, slides and workbook carry CDN posting timestamps of 2026-07-30; they are the company's documents for the 2026-07-29 results and contain nothing dated after July 29 (MANIFEST admissibility note; §12.2). OK.
- Forward references ("From FY2027 it extends … lives", Nadella's plan to sell on the August 31, 2026 vest, Hoffman not standing at the 2026 meeting) are all statements made in pre-cutoff documents about the future, quoted as such, never graded.
- No Q1 FY2027 result, no post-cutoff 8-K (the 2026-09-02 filing was not fetched per MANIFEST and nothing relies on it), no September 2026 material anywhere in either draft.
- Written date 2026-09-08 is the run date, with the as-of label separate. Correct.

## 7. Verdict

**REVISE.** Four factual items in business.md, each one cell or one clause; no structural change. The writer should:

1. **§4 table, "Finance-lease liabilities, June 30", FY2022 column:** replace "n/d" with **14,902** and add the tag. Evidence: `10-K-FY2022.txt` line 3479 "Total finance lease liabilities | $ | 14,902 | $ | 12,541" (Note 14) and `10-K-FY2023.txt` line 3567 "Total finance lease liabilities | $ | 17,067 | $ | 14,902" (Note 14). Extend the table footnote "Leases […]" with `[10-K FY2023, Note 14]` or `[10-K FY2022, Note 14]`. Then re-read the §4 prose sentence on finance leases to see whether the FY2022 figure changes anything (it does not: liabilities went 14,902 → 66,594, which strengthens the point).
2. **§5, first sentence of "The sign of weakening":** "have grown 6% in each of the last eight quarters" is not in the sources. The Metrics sheet (`financial-statements-FY26Q4.txt` line 191) and slide 9 show 6% in each of the five quarters Q4 FY2025 through Q4 FY2026, and 6% for FY2025 and FY2026 as whole years (10-K FY2025 line 1304 also gives 6% for FY2025). Write what the sources show, e.g. "have grown 6% in each of the last five quarters and in both FY2025 and FY2026 as a whole [IR workbook FY26Q4, Metrics] [10-K FY2025, Item 7]".
3. **§1, history paragraph:** "The cached filings do not date the LinkedIn and GitHub purchases" is contradicted for LinkedIn by `DEF14A-2025.txt` line 1351: "LinkedIn has continued to deliver strong growth and engagement since its acquisition in December 2016." Rewrite as: LinkedIn was bought in December 2016 [DEF 14A 2025, Compensation Discussion and Analysis]; the cached filings do not date the GitHub purchase [10-K FY2026, Item 1].
4. **§2, "Windows and Devices, XBOX, Search advertising" paragraph:** "XBOX was the one large line to shrink in FY2026" is not true; Windows and Devices also fell ("Windows and Devices revenue decreased $230 million or 1%", `10-K-FY2026.txt` line 1333; 17,314 → 17,084 in the §2 table). Reword to something like "XBOX was the large line that shrank most in FY2026, down 7% with hardware down 29%; Windows and Devices slipped 1%" and add the line-1333 fact under the existing [10-K FY2026, Item 7] tag.

After these four edits the writer should re-run `python3 -P /tmp/msft-orch/wc_prose.py` on business.md (currently 2,634; the edits add perhaps 25 words) and confirm it stays under 3,000.

Optional notes, not blocking, for the owner or the next refresh:

- Indicators 3 and 8 each carry an "excluding OpenAI" component that management has given on two calls; if it is dropped next quarter, record 🔇 on that half and keep the recurring half (the RPO balance, the bookings growth rate).
- Claim 7 is a two-part claim (a count is disclosed, and it is above 30 million). It grades mechanically, but the refresh grader should treat "no count given" as 🔇 rather than ❌.
- §3's "(our inference)" on the $26.7 billion sentence could move to the clause it actually qualifies ("because it counts equipment when received"), since the $26.7 billion itself is a stated Note 6 fact.

## Direct fixes (recorded per §13)

Word counts: business.md 2,498 → 2,634; outlook.md 992 → 1,004. All edits were in-line; each replacement matched exactly once (script `/tmp/msft-orch/reviewer/apply_fixes.py`; pre-edit copies in `/tmp/msft-orch/reviewer/*.before.md`). No number was changed. No git command was run.

**business.md**

1. §1 line 8: "the on-premises server products and support services" → "the on-premises server products (software run on the customer's own machines) and support services". (jargon)
2. §2 line 39: "on seats up 6%" → "on seats (paid users) up 6%". (jargon)
3. §2 line 47: "when most multi-year contracts are signed" → "when more multi-year contracts are signed", to match 10-K FY2026 line 1112 "a higher volume of multi-year contracts". (one-word alignment to source; tag unchanged)
4. §3 line 69: "so operating margin rose even as gross margin slipped" → "so operating margin (profit after all running costs, before interest and tax, as a share of revenue) rose even as gross margin (revenue left after the direct cost of delivering the product, as a share of revenue) slipped". (jargon)
5. §4 table line 99: row label "Debt, June 30 (computed sum of current and long-term)" → "Debt, June 30 (computed: short-term debt, current portion and long-term debt)", because the FY2024 figure 51,630 includes the balance sheet's "Short-term debt | 6,693" line (10-K FY2024 line 2045). Numbers untouched. (label alignment; see D11 withdrawal)
6. §4 table footnote line 102: "n/d = not disclosed." → "n/d = not disclosed. GAAP is the standard set of accounting rules; the company's non-GAAP figure is its own adjusted number." (jargon)
7. §4 line 104: "The striking row is free cash flow: between" → "The striking row is free cash flow (operating cash flow minus capex): between". (jargon)
8. §4 line 106: "recapitalization diluting the stake" → "recapitalization (a reorganisation of who owns what) diluting the stake". (jargon)
9. §4 line 108: "each dollar of net property and equipment earned" → "each dollar of net property and equipment (buildings and machines at book value, after depreciation) earned"; "the rating is AAA" → "the credit rating is AAA, the highest grade". (jargon)
10. §5 line 112: "unearned revenue was $75.7 billion" → "unearned revenue (cash collected for service not yet delivered) was $75.7 billion". (jargon)
11. §5 line 114: "for governing AI agents" → "for governing AI agents (programs that carry out tasks on their own)". (jargon)
12. §5 line 118: "commercial bookings excluding OpenAI" → "commercial bookings (the value of new contracts signed in the period) excluding OpenAI". (jargon)
13. §6 #1 line 124: after the quote "may lead to impairment of assets on our balance sheet" added ", that is, to writing down their value". (jargon)
14. §6 #2 line 126: "$6.0 billion receivable" → "$6.0 billion receivable (invoiced but not yet paid)". (jargon)
15. §6 #4 line 130: "over transfer pricing," → "over transfer pricing (how profit is split between its units in different countries),". (jargon)
16. §7 line 140: "Reid Hoffman leaves in December 2026 [DEF 14A 2025, Board Leadership] [8-K 2025-09-30] [8-K 2026-05-13] [8-K 2026-06-02]" → "Reid Hoffman is not standing for re-election at the 2026 annual meeting [10-K FY2026, Signatures] [DEF 14A 2025, Board Leadership] [8-K 2025-09-30] [8-K 2025-12-05] [8-K 2026-05-13] [8-K 2026-06-02]". The 8-K (line 56) names the meeting, not a month; the signature block supports "13 directors"; the 2025-12-05 8-K dates Rodriguez's departure. (wording alignment to source; two tags added)
17. §7 line 142: "The pay ratio was 480 to 1" → "The pay ratio (CEO pay to the median employee's) was 480 to 1". (jargon)
18. Glossary: removed the "Goodwill" entry; the term is not used in either file. (unused glossary term)

**outlook.md**

19. §3 line 33: after the quote ending "as well as our own MAI family" added "(MAI: Microsoft's own models)". (jargon)
20. §3 line 33: after "customers outside of frontier model companies" added "(the companies that build the leading AI models)". (jargon)

Nothing else in either file was touched.

---

## Cycle 2 (final): re-check of the four REVISE items

_Reviewed 2026-09-08 against the same `sources/FY2026-Q4/` cache. business.md re-read from disk (copy kept at `/tmp/msft-orch/reviewer/business.cycle2.md`). A `diff` of the current business.md against my reconstructed cycle-1 post-fix state (`/tmp/msft-orch/reviewer/business.recon.md`, produced by re-applying the 18 logged edits to the pre-edit copy) shows exactly four changed lines (10, 45, 100 and 102, 118) and nothing else; outlook.md is byte-identical to my cycle-1 state. None of the 20 direct fixes was reverted. Word counts by `python3 -P /tmp/msft-orch/wc_prose.py`: business.md 2,654 (writer reported 2,654; cycle 1 ended at 2,634); outlook.md 1,004 (unchanged). Both in range._

| # | Item | Draft now reads | Source line(s) | Result |
|---|---|---|---|---|
| R1 | §4 table, Finance-lease liabilities FY2022 (line 100) | "14,902" replaces "n/d"; footnote (line 102) now ends "Leases [10-K FY2026, Note 13] [10-K FY2025, Note 13] [10-K FY2024, Note 14] [10-K FY2022, Note 14]" | `10-K-FY2022.txt` line 3479 "Total finance lease liabilities \| $ \| 14,902 \| $ \| 12,541", inside NOTE 14 — LEASES (heading line 3405); corroborated by `10-K-FY2023.txt` line 3567 "… \| 17,067 \| $ \| 14,902" | PASS |
| R2 | §5 sign of weakening (line 118) | "grew 6% in each of the five quarters from Q4 FY2025 to Q4 FY2026, and 6% in both FY2025 and FY2026 as whole years … [IR workbook FY26Q4, Metrics] [Q4 FY2026 slides, s.9]"; "eight quarters" gone (0 hits) | `financial-statements-FY26Q4.txt` line 191 "Microsoft 365 Commercial seat growth (y/y) \| 6% \| 6% \| 6% \| 6% \| 6% \| 6% \| 6%" under the header (line 182) "Q4'25 \| FY25 \| Q1'26 \| Q2'26 \| Q3'26 \| Q4'26 \| FY26"; `slides.txt` line 159 "Microsoft 365 Commercial seat growth (y/y) \| 6% \| 6% \| 6% \| 6% \| 6%" under "FY25 Q4 \| FY26 Q1 \| FY26 Q2 \| FY26 Q3 \| FY26 Q4" (line 157) | PASS |
| R3 | §1 history (line 10) | "LinkedIn was acquired in December 2016; the cached filings do not date the GitHub purchase [DEF 14A 2025, Compensation Discussion and Analysis] [10-K FY2026, Item 1]." | `DEF14A-2025.txt` line 1351 "LinkedIn has continued to deliver strong growth and engagement since its acquisition in December 2016." (Compensation Discussion and Analysis begins line 1253). GitHub: no dated acquisition sentence in any cached 10-K or the proxy (re-grepped "acquisition of GitHub" / "acquired GitHub", 0 hits) | PASS |
| R4 | §2 (line 45) | "Two lines shrank in FY2026: XBOX by 7%, with hardware down 29%, and Windows and Devices by 1% [10-K FY2026, Item 7] [10-K FY2026, Note 18]." | Item 7 lines 1336 ("XBOX revenue decreased $1.7 billion or 7% … XBOX hardware revenue decreased 29%") and 1333 ("Windows and Devices revenue decreased $230 million or 1%"). Note 18 product-line table (lines 3774–3794), FY2026 vs FY2025, every line re-computed: Server products +31.5%, Microsoft 365 Commercial +16.2%, **XBOX −7.1%**, LinkedIn +11.3%, **Windows and Devices −1.3%**, Search advertising +9.4%, Microsoft 365 Consumer +23.9%, Dynamics +15.1%, Enterprise and partner services +6.4%, Other +51.4%. Exactly two lines fell, as the draft now says | PASS |

**Other checks repeated.** business.md skeleton: §1–§8 headings in order (lines 4, 12, 49, 85, 110, 120, 138, 160), `_Proposed — owner to review and lock._` at line 162, Glossary (11 entries, one sentence each, all used; Goodwill still absent) at 175, Sources at 189 with the `[10-K FY2022, …]` prefix already mapped (line 199), so the new Note 14 tag resolves. outlook.md unchanged: headings §1–§5, no §6, Sources, header `company-published`. As-of scan of both files: nothing dated after 2026-07-29 (only the two "Written 2026-09-08" run-date lines match a post-cutoff pattern). No direct fixes were needed in cycle 2; no file other than this review was written.

**Final verdict: PASS.** Nothing open. The three optional notes from cycle 1 (the "excluding OpenAI" halves of indicators 3 and 8; the two-part claim 7; the placement of "(our inference)" in §3) stand as notes for the owner and the next refresh, not as conditions.
