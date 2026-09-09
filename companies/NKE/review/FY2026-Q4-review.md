# NIKE, Inc. (NKE) — Reviewer report, Q4 FY2026 (quarter ended May 31, 2026)

_Review cycle 1 of 2 (first research run; no blind re-grade applies; no scorecard exists yet). Reviewed 2026-09-08 against `companies/NKE/sources/FY2026-Q4/` only (cutoff 2026-07-15: 10-K and proxy filing date; call 2026-06-30). Every number and quotation at stake was checked against the cached source TEXT (five 10-Ks, the Q3 10-Q, the 2026 proxy, the nine 8-Ks, both transcripts, both releases, the schedules), not the gatherers' notes. Greps were `grep -n -F` on full lines (host grep is ugrep; Nike's filings and transcripts use ASCII apostrophes); transcript quotes were additionally checked with a whitespace-normalising, hyphenation-rejoining matcher (`/tmp/nke-orch/reviewer/qcheck.py`) because the layout transcripts break lines mid-phrase ("mid-\nsingle", "fixed cost\nbase"). Line numbers below refer to the cached `.txt` files; transcript attributions were mapped from the bracketed speaker labels (Q4: Hill prepared remarks lines 53–264, Friend 265–463, Hill close 464–504, then Yih 511, Drbul 571, Boss 637, Hutchinson 702, Binetti 785, Sherman 830, Boruchow 912; Q3: Hill 45–249, Friend 250–455). Word counts by `cd /home/ubuntu && python3 -P /tmp/nke-orch/wc_prose.py`: business.md 2,475 before fixes / 2,561 after; outlook.md 963 before / 993 after (targets 2,000–3,000 and 800–1,200)._

**Cycle 1 verdict: REVISE** (four small factual items, all in business.md: one unlabelled computation presented as a disclosed figure, one wording not supported by its source, two unlabelled arithmetic sums; nothing structural). **Final verdict after cycle 2: PASS** (see the "Cycle 2" section at the end; the cycle-1 FAIL on the currency figure is withdrawn there with evidence, and two cycle-2 direct fixes are logged). Citation spot-check: 168 items (every cell of the §2 segment, channel and product tables, the §3 economics table, the §4 cash table and the §7 capital-allocation table; every cell of outlook §1; all 16 guidance items in outlook §4 word for word; all 12 claim quotes in §5; 75 transcript and release quotations across both files; and 52 prose sentences or facts), 164 PASS, 4 FAIL, 1 FAIL withdrawn with evidence (the "3.1% average coupon", §3j P17). Every "(computed)" ratio re-derives from the cited inputs. Every transcript quote is character for character and attributed to the right speaker and section. Nothing after 2026-07-15 is used. Jargon, tags and two wording slips were fixed directly (24 edits, logged in "Direct fixes").

---

## 1. Rubric result (§14)

| # | Question | Answer | Reasoning |
|---|---|---|---|
| 1 | Can I explain what this company does, and who pays it, in two sentences? | **Yes** | §1: designs and markets sports shoes, clothing and equipment made by contractors; sells to retailers (wholesale, who order five to six months ahead and pay within 90 days) and to shoppers directly (about 980 stores plus apps). §2 gives the split (61% / 39% of NIKE Brand) and the geographies. |
| 2 | Do I know exactly what would kill it, and what the early warning sign is? | **Yes** | §6 ranks six scenarios, each with what must happen, an early warning tied to a recurring line (Digital and Direct declines and the sales-related reserve; running growth vs "5 consecutive quarters"; the product-costs line of the gross-margin bridge; Greater China revenue and EBIT; receivables vs wholesale revenue; overhead dollars vs revenue), and the exposed profit pool. |
| 3 | Do I know why the margins are what they are, and whether cost scales with usage? | **Yes** | §3 says it plainly: cost rises with every pair sold, so gross margin is about how much of the list price survives discounting; below it sit two large mostly fixed lines (demand creation, operating overhead); a 10% revenue fall cut the EBIT margin from 12.7% to 8.2%; capital sits in stock and unpaid invoices, not plant. The year-by-year gross-margin explanation and the tariff refund are separated and labelled. |
| 4 | Could I predict what the scorecard will check next quarter, from §5 of the outlook alone? | **Yes** | Eleven claims, each with a number, a date or an observable event; four sharpenings labelled as the writer's; one disclosure check labelled with its column; one multi-quarter claim (Investor Day) with its horizon. Headline revenue is one claim of eleven; no EPS claim. |
| 5 | Did nothing in the report require knowledge I don't have? | **Yes, after fixes** | Before fixes: "gross-margin bridges", "capex" (first prose use), "write-down reserves", "turns", "diluted EPS", "free cash flow", "receivable", "coupon", "ratings", "proxy", "recast", "wholesale equivalent", "SG&A", "sell-in", "tough compare", "off-price" and "full price realization" were used without a plain gloss; the glossary defined "Futures ordering program", a term never used in prose. All fixed directly (see "Direct fixes"). |

## 2. Skeleton and rules check

**business.md**

| Requirement | Result |
|---|---|
| `# <Company> — The Business`; `_As of <QLABEL>. Written <date>._` with calendar parenthetical | OK: "# Nike — The Business" / "_As of Q4 FY2026 (quarter ended May 31, 2026). Written 2026-09-08._" |
| §1–§8 headings present, in order, none skipped | OK (lines 4, 12, 58, 84, 106, 116, 134, 159). §1 has the history paragraph; §6 carries customer concentration and the Belgian customs claim; §8 has name / why / where for each indicator |
| `_Proposed — owner to review and lock._` under §8 | OK (line 161) |
| §2 segment table, five fiscal years | OK: seven segments plus NIKE Brand and NIKE, Inc. totals and a reported / currency-neutral growth row, FY2022–FY2026, with the note that segment definitions are unchanged. Plus a channel table (wholesale / Direct / Digital / stores / share / growth) and a product table (footwear / apparel / equipment / Jordan), each five years |
| Five-year gaps footnoted, not filled | OK: Jordan Brand FY2022 is "n/d" on the reported basis (the FY2024 10-K gives only a wholesale-equivalent figure, 5,122, a different basis); the FY2026 10-K carries no Men's/Women's/Kids' split (0 hits for "Men's" in `10-K-FY2026.txt`) and the prose says so; the FY2023 Digital restatement (12.6 → 12.4) is shown in the cell and footnoted; NIKE-owned store dollars before FY2025 are labelled computed |
| §3 table: revenue, gross margin, operating margin, capex, capex/revenue, five years | OK, plus gross margin and EBIT margin excluding the IEEPA refund (both labelled computed, FY2026 only, dashes elsewhere), demand creation and overhead as shares of revenue, depreciation and amortization, inventories |
| §4 table, five years | OK (11 rows FY2022–FY2026) |
| §7 capital-allocation table | OK, five years (repurchases in dollars and shares, average price, dividends per share and in cash, capex, debt repaid, share count, employees) |
| Glossary, Sources | Both present. Glossary now 11 entries, one sentence each (the "U.S." in the IEEPA entry is an abbreviation, not a sentence break), all used in business.md or outlook.md. Sources maps all 13 tag prefixes to cached files and states that the transcripts and release PDFs have no printed page numbers, so call tags name section and speaker |
| Length 2,000–3,000 | 2,561 after fixes; in range |
| Indicators 5–8, anchored to recurring disclosures (§8) | 8 indicators. #1, #6, #7 are release Divisional Revenues / EBIT table rows; #3, #5 are release income-statement lines; #2 is the release's wholesale / Direct / Digital text bullets (present in both cached releases, rounded to $0.1 billion); #4 is the release balance sheet plus the Balance Sheet Review sentence (present in both releases); #8 is the 10-Q/10-K cash flow statement (the release has none, as the table says). None depends on a one-off number from a call. The "excluding named one-time items" half of #3 is conditional by construction and reads as "none" in a clean quarter |
| Fixed facts from the brief | Refund: §3 table labels both ex-refund rows "(computed)", the prose and outlook §1 give the $986 million, about 900 basis points of Q4 gross margin and $0.52 of $0.72 diluted EPS, all sourced. CFO: §7 says Friend is due to leave September 4, 2026 and states the August 16 (8-K body) versus August 17 (release, 10-K, proxy) discrepancy rather than picking one. Hill: "since 2024" with the September 19, 2024 offer letter; no bare "October 2024" anywhere (0 hits). Wholesale equivalent and the Men's/Women's/Kids' gap are footnoted, not filled |

**outlook.md**

| Requirement | Result |
|---|---|
| `# <Company> — Outlook as of <QLABEL>` with calendar parenthetical | OK: "# Nike — Outlook as of Q4 FY2026 (quarter ended May 31, 2026)" |
| `_Transcript source tier: company-published. Written 2026-09-08._` | OK, exact; matches MANIFEST tier 1 |
| §1 table, one row per proposed indicator, three columns | OK, 8 rows, all cells filled and tagged. The lead sentence says the indicators are proposed, not locked, names the prior quarter with its calendar dates, and states the basis of the "expected" column (Friend on the March 31, 2026 call, currency-neutral unless he said otherwise). Row 1 quotes the Q3 guide "down 2% to 4%" together with the separate "2-point benefit from foreign exchange" and reads the −4% currency-neutral / −1% reported result against it, as the brief required |
| §2, §3, §4 (verbatim guidance), §5 | OK |
| §6 Tone shift absent on first run | OK (no §6; headings are 1–5 then Sources) |
| Sources | OK, 7 tag prefixes mapped; states no printed page numbers |
| Length 800–1,200 | 993 after fixes |
| Claims 6–12; one sentence; single direction; verbatim quote and tag under each | OK: 11 claims. None is either/or; none can never be missed. Sharpenings labelled as the writer's in claims 1, 3, 5, 6 ("Our sharpening of …, not management's number(s)"). Claim 10 is labelled "Disclosure check (quarter column)" and "Not a management claim". Claim 11 states its horizon (Q2 FY2027) and that it carries. Claim 7 (Denton signs the Q1 FY2027 10-Q) and claim 9 (management states Sportswear and Jordan Streetwear declined) are observable events. Headline revenue is claim 1 only; no EPS claim |
| §4 guidance verbatim | OK: 14 table rows, every quote character for character (§3h); the "Not guided" list is confirmed by grep (§3j P38) |

## 3. Citation spot-check

Legend: PASS / FAIL. Every "(computed)" cell was re-derived from the cited source figures. Source line numbers are given for every cell.

### 3a. business.md §2 segment table (every cell)

FY2024–FY2026 from `10-K-FY2026.txt` Item 7 table lines 1088–1096 (identical figures in Note 15, line 2892 and 2806); FY2023 and FY2022 from `10-K-FY2024.txt` Item 7 table lines 1166–1174 (FY2023 also `10-K-FY2025.txt` 1139–1147); growth rates from each year's own 10-K.

| # | Row | FY2022 / FY2023 / FY2024 / FY2025 / FY2026 | Result |
|---|---|---|---|
| A1 | North America 18,353 / 21,608 / 21,396 / 19,572 / 20,511 | FY2024 1166; FY2026 1088 | PASS |
| A2 | EMEA 12,479 / 13,418 / 13,607 / 12,257 / 12,572 | FY2024 1167; FY2026 1089 | PASS |
| A3 | Greater China 7,547 / 7,248 / 7,545 / 6,586 / 5,847 | FY2024 1168; FY2026 1090 | PASS |
| A4 | APLA 5,955 / 6,431 / 6,729 / 6,251 / 6,243 | FY2024 1169; FY2026 1091 | PASS |
| A5 | Global Brand Divisions 102 / 58 / 45 / 48 / 49 | FY2024 1170; FY2026 1092 | PASS |
| A6 | Total NIKE Brand 44,436 / 48,763 / 49,322 / 44,714 / 45,222 | FY2024 1171; FY2026 1093 | PASS |
| A7 | Converse 2,346 / 2,427 / 2,082 / 1,692 / 1,174 | FY2024 1172; FY2026 1094 | PASS |
| A8 | Corporate (72) / 27 / (42) / (97) / 2 | FY2024 1173; FY2026 1095 | PASS |
| A9 | Total NIKE, Inc. 46,710 / 51,217 / 51,362 / 46,309 / 46,398 | FY2024 1174; FY2026 1096 | PASS |
| A10 | Growth reported / currency-neutral +5%/+6%, +10%/+16%, 0%/+1%, −10%/−9%, 0%/−2% | `10-K-FY2022.txt` 925 ("5% \| 6%"); FY2024 1174 ("10% \| 16%" and "0% \| 1%"); FY2026 1096 ("0% \| -2%" and "-10% \| -9%") | PASS |

### 3b. business.md §2 channel table (every cell)

| # | Row | Source | Result |
|---|---|---|---|
| B1 | Wholesale 25,608 / 27,397 / 27,758 / 25,883 / 27,453 | `10-K-FY2024.txt` 1017; `10-K-FY2026.txt` 963 | PASS |
| B2 | NIKE Direct 18,726 / 21,308 / 21,519 / 18,783 / 17,720 | FY2024 1018; FY2026 964 | PASS |
| B3 | Digital 10.7 / 12.6 (12.4 restated) / 12.1 / 9.6 / 8.6 | FY2022 975 and FY2023 1019 ("$12.6 billion for fiscal 2023 compared to $10.7 billion"); FY2024 1066 ("$12.1 billion for fiscal 2024 compared to $12.4 billion for fiscal 2023", with the reclassification sentence); FY2026 1001 ("$8.6 billion … compared to $9.6 billion") | PASS |
| B4 | Stores 8.0 / 8.7 / 9.4 (computed) / 9.2 / 9.1 | 18.726 − 10.7 = 8.03; 21.308 − 12.6 = 8.71; 21.519 − 12.1 = 9.42; FY2026 1001 ("$9.1 billion … compared to $9.2 billion") | PASS |
| B5 | Direct share ~42% / ~44% / ~44% / ~42% / 39% (computed) | FY2022 975 ("approximately 42%"); FY2023 824 ("approximately 44%", so disclosed, not computed: label aligned, Direct fix 3); FY2024 869 ("approximately 44%"); FY2025 850 ("approximately 42%"); 17,720 / 45,222 = 39.2% | PASS (label fixed) |
| B6 | Wholesale growth cn −1% / +14% / +2% / −6% / +4% | FY2022 928; FY2023 970; FY2024 1017; FY2025 996; FY2026 963 | PASS |
| B7 | Direct growth cn +15% / +20% / +1% / −12% / −8% | FY2022 929; FY2023 971; FY2024 1018; FY2025 997; FY2026 964 | PASS |

### 3c. business.md §2 product table (every cell)

| # | Row | Source | Result |
|---|---|---|---|
| C1 | Footwear 29,143 / 33,135 / 33,427 / 29,510 / 29,525 | `10-K-FY2024.txt` 1007; `10-K-FY2026.txt` 953 | PASS |
| C2 | Apparel 13,567 / 13,843 / 13,775 / 12,965 / 13,449 | FY2024 1008; FY2026 954 | PASS |
| C3 | Equipment 1,624 / 1,727 / 2,075 / 2,191 / 2,199 | FY2024 1009; FY2026 955 | PASS |
| C4 | Global Brand Divisions, Total NIKE Brand | as A5, A6 | PASS |
| C5 | Jordan Brand (reported basis) n/d / 8,460 / 8,701 / 7,270 / 7,034 | `10-K-FY2025.txt` 1005 ("Jordan Brand \| 7,270 \| 8,701 \| … \| 8,460"); `10-K-FY2026.txt` 973 (footnote: "$7,034 million, $7,270 million and $8,701 million"). FY2022: the FY2024 10-K's Jordan rows (982, 1029) are on the wholesale-equivalent basis (5,122 / 6,589 / 6,988), a different measure, so "n/d" on the reported basis is correct | PASS |

### 3d. business.md §3 economics table (every cell)

| # | Row | Re-derivation | Result |
|---|---|---|---|
| D1 | Revenue (as A9) | | PASS |
| D2 | Gross margin 46.0 / 43.5 / 44.6 / 42.7 / 42.9% | `10-K-FY2024.txt` 981 ("44.6% \| 43.5% \| 46.0%"); `10-K-FY2026.txt` 931 ("42.9% \| 42.7% \| 44.6%") | PASS |
| D3 | Gross margin ex-refund 40.8% (computed) | (19,911 − 986) / 46,398 = 40.79% (gross profit 930; refund Note 1 line 1973); Friend states 40.8% (transcript 335) | PASS |
| D4 | EBIT margin 14.7 / 12.1 / 12.7 / 8.2 / 8.3% | FY2024 1200; FY2026 885 | PASS |
| D5 | EBIT margin ex-refund 6.2% (computed) | (3,850 − 986) / 46,398 = 6.17% (EBIT 882) | PASS |
| D6 | Demand creation / revenue 8.2 / 7.9 / 8.3 / 10.1 / 10.2% (computed) | 3,850 / 46,710 = 8.24; 4,060 / 51,217 = 7.93; 4,285 / 51,362 = 8.34; 4,689 / 46,309 = 10.13; 4,754 / 46,398 = 10.25 (FY2024 982; FY2026 932) | PASS |
| D7 | Operating overhead / revenue 23.5 / 24.0 / 23.9 / 24.6 / 24.5% (computed) | 10,954 / 46,710 = 23.45; 12,317 / 51,217 = 24.05; 12,291 / 51,362 = 23.93; 11,399 / 46,309 = 24.62; 11,360 / 46,398 = 24.48 (FY2024 983; FY2026 933) | PASS |
| D8 | Capex 758 / 969 / 812 / 430 / 684 | "Additions to property, plant and equipment": FY2024 1868 ("( 812 ) \| ( 969 ) \| ( 758 )"); FY2026 1853 | PASS |
| D9 | Capex / revenue 1.6 / 1.9 / 1.6 / 0.9 / 1.5% (computed) | 1.62 / 1.89 / 1.58 / 0.93 / 1.47 | PASS |
| D10 | D&A 717 / 703 / 796 / 775 / 747 | `10-K-FY2023.txt` 1800 ("Depreciation \| 703 \| 717"); FY2026 1838 ("Depreciation and amortization \| 747 \| 775 \| 796") | PASS |
| D11 | Inventories 8,420 / 8,454 / 7,519 / 7,489 / 7,501 | FY2023 1750; FY2024 1803; FY2026 1789 | PASS |

### 3e. business.md §4 cash table (every cell)

| # | Row | Source | Result |
|---|---|---|---|
| E1 | Cash from operations 5,188 / 5,841 / 7,429 / 3,698 / 2,868 | `10-K-FY2024.txt` 1863 ("Cash provided (used) by operations \| 7,429 \| 5,841 \| 5,188"); `10-K-FY2026.txt` 1848 | PASS |
| E2 | Capex (as D8) | | PASS |
| E3 | Free cash flow (computed) 4,430 / 4,872 / 6,617 / 3,268 / 2,184 | E1 − E2 re-derives exactly | PASS |
| E4 | Net income 6,046 / 5,070 / 5,700 / 3,219 / 3,108 | FY2024 1754; FY2026 1740 | PASS |
| E5 | Cash conversion 86 / 115 / 130 / 115 / 92% (computed) | 85.8 / 115.2 / 130.3 / 114.9 / 92.3 | PASS |
| E6 | Share repurchases (cash) 4,014 / 5,480 / 4,250 / 2,985 / 146 | FY2024 1875; FY2026 1859 | PASS |
| E7 | Dividends paid 1,837 / 2,012 / 2,169 / 2,300 / 2,407 | FY2024 1876; FY2026 1860 | PASS |
| E8 | Cash and short-term investments 12,997 / 10,675 / 11,582 / 9,151 / 9,027 | FY2023 1747–1748 (8,574 + 4,423; 7,441 + 3,234); FY2024 1800–1801 (9,860 + 1,722); FY2026 1786–1787 (7,464 + 1,687; 7,563 + 1,464) | PASS |
| E9 | Total debt (computed) 9,430 / 8,933 / 8,909 / 7,966 / 7,942 | Current portion + long-term + notes payable: FY2023 1761, 1762, 1768 (500 + 8,920 + 10; 0 + 8,927 + 6); FY2024 1814, 1815, 1821 (1,000 + 7,903 + 6); `10-K-FY2025.txt` 1850, 1851, 1857 (0 + 7,961 + 5); FY2026 1800, 1806 (2,000 + 5,942, no notes-payable line, which matches Note 6 "Total \| 7,942") | PASS |
| E10 | ROIC 46.5 / 31.5 / 34.9 / 20.2 / 18.7% | `10-K-FY2022.txt` 833 ("ROIC as of May 31, 2022 was 46.5%"); FY2024 881 ("34.9% … compared to 31.5%"); FY2026 834 ("18.7% … compared to 20.2%") | PASS |
| E11 | Stock-based compensation 638 / 755 / 804 / 709 / 715 | FY2024 1855; FY2026 1840 | PASS |

### 3f. business.md §7 capital-allocation table (every cell)

| # | Row | Source | Result |
|---|---|---|---|
| F1 | Repurchases $ (shares) 3,994 (27.3) / 5,509 (50.0) / 4,254 (41.4) / 2,955 (37.6) / 123 (1.8) | `10-K-FY2022.txt` 1376 ("27.3 million shares … for $3,994 million"); FY2023 1454 ("50.0 million shares … $5.5 billion") and equity statement 1871 ("( 5,509 )"); FY2024 1503 ("41.4 million") and 1925 ("( 4,254 )"); FY2025 1539 ("37.6 million") and 1962 ("( 2,955 )"); FY2026 1495 ("1.8 million shares … $122.4 million") and 1909 ("( 123 )") | PASS |
| F2 | Average price 146.11 / 110.32 / 102.72 / 78.50 / 67.63 | same five Item 7 sentences | PASS |
| F3 | Dividends declared per share 1.190 / 1.325 / 1.450 / 1.57 / 1.63 | FY2023 1864, 1872; FY2024 1926; FY2026 1901, 1910 | PASS |
| F4 | Dividends paid (as E7) | | PASS |
| F5 | Capex (as D8) | | PASS |
| F6 | Debt repaid — / 500 / — / 1,000 / — | "Repayment of borrowings": FY2023 1820 ("( 500 ) \| — \| ( 197 )", the 197 being FY2021); FY2024 1873; FY2026 1857 ("— \| ( 1,000 ) \| —") | PASS |
| F7 | Shares outstanding A + B 1,571 / 1,532 / 1,503 / 1,476 / 1,483 (computed) | equity statements: FY2024 1914 (305 + 1,266), 1922 (305 + 1,227), 1931 (298 + 1,205); FY2026 1906 (290 + 1,186), 1915 (281 + 1,202) | PASS |
| F8 | Employees 79,100 / 83,700 / 79,400 / 77,800 / 73,000 | FY2022 315; FY2023 318; FY2024 319; FY2025 321; FY2026 319 | PASS |

### 3g. outlook.md §1 indicator table (every cell)

| # | Row | This quarter / last quarter / expected | Result |
|---|---|---|---|
| G1 | Revenue | $10,972M, −1% / −4%: `press-release.txt` 214; geographies +3 / −6 / −17 / −1 cn: 198, 203, 208, 213 (Total rows). Q3 $11,279M, 0% / −3%: `press-release-FY2026-Q3.txt` 181; +3 / −7 / −10 / −2: 161, 166, 171, 176. Expected: `transcript-FY2026-Q3.txt` 434–435 and 444 (Friend), both verbatim | PASS |
| G2 | Wholesale / Direct / Digital | $6.6B +1% cn, $4.1B −9% cn, Digital −12%: release 42–44. Q3 $6.5B +1%, $4.5B −7%, Digital −9%: Q3 release 44–46. Expected: Q3 transcript 338–339 (Friend) verbatim | PASS |
| G3 | Gross margin | 49.2%, +890 bps, ~900 bps refund: release 48; 40.2% and −10 bps excluding it: transcript 319 (Friend: "have been 40.2%, down 10 basis points"). Q3 40.2%, −130 bps: Q3 release 48. Expected: Q3 transcript 445–446 verbatim | PASS |
| G4 | Inventories | $7,501M flat, sentence verbatim: release 158, 86. Q3 $7,487M −1%, sentence verbatim: Q3 release 124, 58. Expected: Q3 transcript 355–356 verbatim | PASS |
| G5 | Demand creation | $1,203M −4%: release 128; 1,203 / 10,972 = 10.96% → 11.0%. Q3 $1,090M 0%: Q3 release 94; 1,090 / 11,279 = 9.66% → 9.7%. Expected: Q3 transcript 446–447 verbatim; SG&A −2%: release 50 | PASS |
| G6 | Greater China | $1,297M (−12% / −17%): release 208; EBIT $243M −20%: 235. Q3 $1,615M (−7% / −10%): Q3 release 171; EBIT $467M +11%: 201. Expected: Q3 transcript 436–437 verbatim | PASS |
| G7 | EBIT margin; North America EBIT | 12.0%: release 248; ex-refund (1,321 − 986) / 10,972 = 3.05% → 3.1% (EBIT 241); NA $2,000M: 233; 2,000 − 965 = 1,035 (Note 1 line 1973 for the $965M). Q3 5.6%: Q3 release 215; NA $981M −11%: 199. Expected: Q3 transcript 423 ("We expect earnings to be flattish"), scope Q4 FY2026–Q2 FY2027 confirmed by Q3 405–407 ("through the end of this calendar year") and Q4 423–426 ("the fourth quarter of fiscal '26 through the first 2 quarters of fiscal '27") | PASS |
| G8 | Cash from operations; capex; FCF | FY2026 2,868 / 684: `10-K-FY2026.txt` 1848, 1853; FCF 2,184. Nine months 1,231 / 546: `10-Q-FY2026-Q3.txt` 225, 230 (Item 1); FCF 685. Q4 alone 2,868 − 1,231 = 1,637; 684 − 546 = 138; 1,637 − 138 = 1,499, all labelled computed | PASS |

### 3h. outlook.md §4 guidance (word for word against `transcript.txt`)

| # | Item | Lines (speaker) | Result |
|---|---|---|---|
| H1 | Basis: "These assumptions reflect the macro environment … over the next 6 months." | 419–420 (Friend) | PASS |
| H2 | Q1 revenue: "Specifically for the first quarter … consistent with recent performance." | 440–442 (Friend) | PASS |
| H3 | Q1 gross margin: "We expect gross margin in Q1 to be slightly positive." | 442–443 (Friend) | PASS |
| H4 | Tariff assumption: "Our forecast is based on incremental tariff rates of 10% … as we communicated last quarter." | 443–445 (Friend) | PASS |
| H5 | Q1 SG&A: "We expect Q1 SG&A dollars to be flat … as we invest into the World Cup." | 449–450 (Friend) | PASS |
| H6 | Tax: "We expect our full year tax rate to be in the low 20% range." | 450–451 (Friend) | PASS |
| H7 | Three quarters: "We reiterate our expectation for earnings to be flattish … However, the composition has shifted." and "We now expect revenue to be down low to mid-single digits … earlier beginning in Q1." | 426–428 and 434–438 (Friend); "mid-\nsingle" rejoined | PASS |
| H8 | FY2027 margin: "We expect these actions will deliver positive operating leverage and gross margin in fiscal '27." | 322 (Friend) | PASS |
| H9 | Sportswear and Jordan Streetwear: "We expect Sportswear and Jordan Streetwear to continue to be negative this fiscal year with improvement expected in the back half." | 233–234 (Hill) | PASS |
| H10 | Greater China: "We continue to take actions with partners … in line with recent performance." | 398–399 (Friend) | PASS |
| H11 | Inventory: "Considering the current macro environment … but also higher gross margins." | 432–434 (Friend) | PASS |
| H12 | Stores: "including a plan to elevate 50% of our NIKE Direct owned fleet by the end of the fiscal year" | 245–246 (Hill) | PASS |
| H13 | Win Now: "And we do remain on track to sunset the Win Now actions by the end of this calendar year." | 845–846 (Hill, answering Sherman) | PASS |
| H14 | Investor Day: "Most importantly, we look forward to sharing … on November 16 and 17." | 248–250 (Hill) | PASS |
| H15 | "Not guided: revenue in dollars, EPS, capex, buybacks, other income, share count, a tariff cost in dollars or basis points, and FY2027 revenue or gross margin"; "the release contains none" | grep of `transcript.txt` for "capital expenditure", "capex", "repurchase", "buyback", "share count", "other income", "other expense", "interest income": 0 hits; lines 415–462 contain no EPS or dollar-revenue figure; `press-release.txt` has no "guidance" (0 hits) and its only forward-looking text is the Forward-Looking Statements block (108) | PASS |
| H16 | Q3 sentence "the final quarter where higher tariffs continue to be a material year-over-year headwind to gross margin" was not repeated | `transcript-FY2026-Q3.txt` 416–417 (Friend); `transcript.txt`: 0 hits for "final quarter" and "material year-over-year" | PASS |

### 3i. outlook.md §5 claim quotes

All twelve quotes are character for character and attributed to the right speaker and section: claim 1 `transcript.txt` 440–441 (Friend); 2 line 442–443 (Friend); 3 line 449–450 (Friend); 4 line 449 (Friend); 5 line 399 (Friend); 6 line 432–433 (Friend); 7 `8-K-2026-06-16.txt` 244 (EX-99.1 press release, "effective August 17"); 8 line 426–427 (Friend); 9 line 233–234 (Hill); 10 `10-K-FY2026.txt` 784 (Item 5; also 1495 in Item 7); 11 line 248–250 (Hill) and `transcript-FY2026-Q3.txt` 449–450 (Friend). Claim 5's "recent performance" base: Greater China currency-neutral −10% (Q3), −17% (Q4), −13% (FY2026), so a 10% floor is a fair sharpening and is labelled. **12 PASS.**

### 3j. Prose sentences and facts, both files

| # | Sentence / fact | Found at | Result |
|---|---|---|---|
| P1 | §1 "the largest seller of athletic footwear and apparel in the world"; "Nearly all of our products are manufactured by independent contractors. Nearly all footwear, apparel and equipment products are manufactured outside the United States."; 52% / 27% / 16%; 15 contract manufacturers | `10-K-FY2026.txt` 149 (Item 1) verbatim; 237 | PASS |
| P2 | §1 "five to six months ahead of delivery"; "within 90 days or less"; "approximately 980 retail stores … which primarily consist of factory stores"; "over 40 countries" | 438 (Item 1A); 1979 (Note 1); 764 (Item 2); 207 (Item 1) | PASS verbatim |
| P3 | §1 "incorporated in 1967 under the laws of the State of Oregon"; IPO 1980 with two classes; Converse purchase undated in the filings; "Consumer Direct Acceleration" in fiscal 2021; Direct about 44% of NIKE Brand in FY2024 | 147; `DEF14A-2026.txt` 471 (Capital Structure); no dated Converse acquisition sentence in any cached 10-K (0 hits for "Converse" with "acqui"); `10-K-FY2022.txt` 805, 807, 951, 3068; `10-K-FY2024.txt` 869 | PASS |
| P4 | §1 Hill (62) joined 1988, retired 2020, President and CEO "since 2024"; offer letter September 19, 2024; Donahoe as former CEO; "in December of '24, we launched the Win Now actions"; "about 8,000 teammates into vertical sport teams" | 369 (Item 1); 3180 (Item 15); DEF14A 1695–1721 (Pay Versus Performance); `transcript.txt` 844 (Hill, answering Sherman); 66 (Hill prepared) | PASS |
| P5 | §2 shares 45% / 28% / 13% / 14% (computed); U.S. about 44%; Converse 2.5% (computed), −31% "due to declines across all territories" | 20,511 / 12,572 / 5,847 / 6,243 over 45,222 = 45.4 / 27.8 / 12.9 / 13.8; 189 (Item 1); 1,174 / 46,398 = 2.53%; `press-release.txt` 70 | PASS |
| P6 | §2 "A weaker dollar added about $1.0 billion of FY2026 revenue" [10-K FY2026, Item 7] | **FAIL:** no cached source states a dollar effect of currency on FY2026 revenue. `10-K-FY2026.txt` 991 (Item 7) gives only "flat on a reported basis and down 2% on a currency-neutral basis" and attributes points to geographies; the release (20, 62) gives the same two rates; both transcripts give no dollar or point figure for the year (0 hits for currency with "billion" or "point"). The $1.0 billion is the writer's arithmetic (46,398 − 46,309 × 0.98 ≈ 1,015, on a rounded −2%) presented as a disclosed fact without a "(computed)" label. → REVISE item 1 | **FAIL** |
| P7 | §2 three largest U.S. customers "about 29% of U.S. sales in FY2026, up from 21% in FY2024"; "No customer accounted for 10% or more of our consolidated Revenues" | 189; `10-K-FY2024.txt` 189 ("approximately 21%"); 223 verbatim | PASS |
| P8 | §2 "Wholesale grew 4% currency-neutral in FY2026 'led by double-digit growth in North America' after two years of deliberately shipping less [Q4 FY2026 call, prepared remarks, Hill] [10-K FY2025, Item 7]" | Growth and quote: `transcript.txt` 115–116 (Hill) and `10-K-FY2026.txt` 999. **FAIL on "two years":** the draft's own channel table shows wholesale currency-neutral +2% in FY2024 and −6% in FY2025; `10-K-FY2025.txt` 862 and 878 describe the deliberate supply reduction ("our actions to reduce supply of certain footwear products in the marketplace … higher sales returns with our wholesale partners") for fiscal 2025 only, and `10-K-FY2024.txt` has no such statement (0 hits for "franchise" with reduce / supply / manage). One year of deliberately shipping less is supported, two is not. → REVISE item 2 | **FAIL (wording)** |
| P9 | §2 Direct $8.6B digital / $9.1B stores; "primarily due to reduced traffic"; "discounting less on NIKE Digital"; footwear 65% / apparel 30% / equipment 5% / Jordan 16% (computed); Jordan $8.7B → $7.0B; Men's/Women's/Kids' on a wholesale-equivalent basis to FY2024, recast in FY2025, absent in FY2026 | 1001 verbatim; `transcript.txt` 123–124 (Hill); 29,525 / 13,449 / 2,199 / 7,034 over 45,222 = 65.3 / 29.7 / 4.9 / 15.6; 973; `10-K-FY2024.txt` 964 and 1021 (wholesale-equivalent tables), `10-K-FY2025.txt` 1002 and 1017 ("we have removed the non-GAAP financial measure of wholesale equivalent revenues … Prior year amounts have been recast"), `10-K-FY2026.txt` 0 hits for "Men's" | PASS |
| P10 | §3 cost of sales: inventory cost, inbound freight, import duties, warehousing, royalties; "sports marketing expense"; demand creation $4.8B / 10.2%; overhead $11.4B / 24.5% | Note 1 lines 1999 ("Cost of sales consists primarily of inventory costs, as well as warehousing costs …, shipping and handling costs, third-party royalties …") and 2043 ("Inventory costs primarily consist of product cost from the Company's suppliers, as well as inbound freight, import duties …"); 1039 (Item 7); 932–933 | PASS |
| P11 | §3 Friend: "a higher fixed cost base that weighed significantly on our EBIT margins as revenue came down"; EBIT margin 12.7% → 8.2% on a 10% revenue fall | `transcript-FY2026-Q3.txt` 288–289 (Friend prepared; "fixed cost\nbase" split across lines, found after normalising); 885 and 1096 | PASS verbatim |
| P12 | §3 net PP&E $4.8B; inventory $7.5B; receivables $5.9B | 1792 (4,796); 1789 (7,501); 1788 (5,931) | PASS |
| P13 | §3 gross margin, one clause per year: FY2022 +120 bps, "elevated freight and logistics costs"; FY2023 −250, higher input and freight costs, "higher promotional activity to liquidate inventory"; FY2024 +110, pricing about 200 bps, "Lower margin in our NIKE Direct business"; FY2025 −190, about 180 bps "primarily due to higher discounts", about 90 bps other costs including obsolescence reserves; FY2026 +20 reported, about 210 from the refund, 40.8% underlying | `10-K-FY2022.txt` 833; `10-K-FY2023.txt` 826, 1035 ("higher input costs and elevated inbound freight and logistics costs"), 1039; `10-K-FY2024.txt` 873, 1084, 1094; `10-K-FY2025.txt` 1055, 1061, 1063 ("Higher other costs (decreasing gross margin approximately 90 basis points), including higher inventory obsolescence reserves"; the draft's "inventory write-down reserves (about 90)" attributed the whole 90 to reserves, aligned directly, Direct fix 7); `transcript.txt` 333–335 (Friend) | PASS after fix |
| P14 | §3 "at least four to five months in advance of sale"; "excess inventory at discounted prices could significantly impair our brand image"; "intentionally reduced over $4 billion of revenue from the peak levels of classic footwear franchises"; "$2 billion"; turns 3.8 → 3.5 (computed) | 1527 (Item 7); 500 (Item 1A); `transcript-FY2026-Q3.txt` 215–216 (Hill); `transcript.txt` 548 (Hill, answering Yih); cost of sales 28,475 / 7,519 = 3.79 (FY2024: 51,362 − 22,887) and 26,487 / 7,501 = 3.53 (`press-release.txt` 125) | PASS verbatim |
| P15 | §3 tariffs: "approximately $1.0 billion" paid; 270 bps in Q3; Supreme Court February 20, 2026, "were unauthorized"; $986M in Q4 cost of sales; ~900 bps; $0.52 of $0.72; "incremental tariff rates of 10% continuing through the end of July and then increasing to 15% thereafter" | `10-Q-FY2026-Q3.txt` 1030 and 1165 (Item 2); `10-K-FY2026.txt` 1973 (Note 1); `press-release.txt` 48, 30; `transcript.txt` 444–445 (Friend) | PASS verbatim |
| P16 | §4 FY2024 130%; $684M refund receivable at year-end; receivables rose on higher wholesale revenue; $243M severance accrued unpaid; FCF $2.2B vs $2.4B dividend; buybacks paused | E5; 1973; 1483 ("The increase in Accounts receivable was primarily due to the outstanding IEEPA tariff receivable, as well as higher wholesale revenues"); 3054 (Note 18: "remaining severance and other employee costs of $243 million are reflected within Accrued liabilities"); E3, E7; 784 | PASS |
| P17 | §4 ROIC "after-tax operating profit by the capital tied up (debt plus equity minus cash)"; 46.5% → 18.7%; cash exceeds debt by about $1.1B (computed); 3.1% average coupon; $2B due FY2027; $3B credit lines undrawn; ratings cut in 2025 from AA-/A1 to A+/A2 | ROIC table 888–907 (EBIT less tax adjustment over average total debt + equity − cash and short-term investments); E10; 9,027 − 7,942 = 1,085. **3.1%: first suspected an unlabelled computation** (the eight coupons in Note 6, 2288–2295, weight to 25,110 / 8,000 = 3.14%); **withdrawn** on finding Item 7A line 1629 "Average interest rate \| 2.6% \| 0.0% \| 0.0% \| 2.9% \| 0.0% \| 3.5% \| 3.1%" (TOTAL column), a disclosed figure; the tag was Note 6, so [10-K FY2026, Item 7A] was added (Direct fix 12). $2B: Note 6 "scheduled maturity … $2 billion, $0 billion, $0 billion, $1.5 billion and $0 billion". $3B: Note 5 lines 2269–2273 ($1B 364-day plus $2B five-year, "no amounts were outstanding"). Ratings: 1509 and 2269 (A+ and A2); the downgrade grades are not in the FY2026 10-K (696 says only "in 2025, our rating was downgraded by S&P Global Ratings and Moody's Ratings"): AA- → A+ is `10-K-FY2025.txt` 1549 ("In July 2025, Standard and Poor's Corporation downgraded our debt rating from AA- to A+") and A1 → A2 is `10-Q-FY2026-Q3.txt` 1792 ("In November 2025, Moody's Investor Services downgraded our debt rating from A1 to A2"); both tags added (Direct fix 12) | PASS after fix; 1 FAIL withdrawn |
| P18 | §5 brand: "in over 190 jurisdictions worldwide"; "what creates authenticity for NIKE is our sport business. And that creates the halo over both of those brands."; FY2025 about 180 bps to "higher discounts"; "digital is still too promotional. Markdowns across the marketplace remain elevated"; Sportswear "declined double digits" | 289 (Item 1; tag was missing, added, Direct fix 13); `transcript.txt` 522–523 (Hill, answering Yih); `10-K-FY2025.txt` 1061; `transcript-FY2026-Q3.txt` 264–265 (Friend); `transcript.txt` 284 (Friend) | PASS verbatim, tag added |
| P19 | §5 athletes: about $15.5B of endorsement contracts; "the growing influence of athletes' personal brands, the proliferation of athlete-led commercial ventures"; Jordan −16% FY2025, −5% cn FY2026 | 1525 (Item 7); 494 (Item 1A) verbatim; 973 | PASS |
| P20 | §5 scale: $4.8B four times Converse revenue (computed); 15 footwear and 64 apparel manufacturers; own Air cushioning; "5 points of running market share in statement footwear, more than any other top 5 brand" | 4,754 / 1,174 = 4.05; 237, 239; 243 and 762 (Air Manufacturing Innovation); `transcript.txt` 106–108 (Hill: "In FY '26, across Western Europe and North America, we gained 5 points …"); the geographic scope was missing from both drafts and was added (Direct fixes 14, 21) | PASS after fix |
| P21 | §5 distribution: 980 stores, 40 countries, "more than 15,000 spaces in wholesale doors"; "Order books are growing, and we are taking back shelf space"; "reducing the order book in holiday" | 764, 207; `transcript.txt` 117 (Hill); `transcript-FY2026-Q3.txt` 263 (Friend); `transcript.txt` 897 (Friend, answering Sherman) | PASS verbatim |
| P22 | §6 #1 "represent approximately half of our revenue"; "continue to be negative this fiscal year"; $1.6B returns and discount reserve | 235–236, 233–234 (Hill); Note 14 line 2856 ("sales-related reserve balance, which includes returns, post-invoice sales discounts and claims, was $1,589 million") | PASS verbatim |
| P23 | §6 #2 competitor list "adidas, Anta, ASICS, Deckers, Li Ning, lululemon athletica, New Balance, On, Puma, Under Armour and V.F. Corporation"; "5 consecutive quarters"; footwear 65% | 269 (Item 1) verbatim; 105 (Hill); P9 | PASS |
| P24 | §6 #3 95% of footwear from three countries (computed); four manufacturers about 60%; "protectionist measures have resulted in increased costs of our products"; U.S. 44%; North America EBIT $4.4B excluding the refund (computed) | 52 + 27 + 16 = 95 (237); 237 ("approximately 60%"); 259 (Item 1) verbatim; 189; `press-release.txt` 233: 5,376 − 965 = 4,411 | PASS |
| P25 | §6 #4 Greater China revenue $7.5B → $5.8B, EBIT $2.3B → $1.3B; "negative impacts from Greater China and Converse to continue throughout fiscal 2027"; "profitability will bottom before sales"; 13% of NIKE Brand | A3; 1111 ("Greater China \| 1,278 \| 1,602 \| -20% \| 2,309"); 856 (Item 7) verbatim; `transcript.txt` 776–777 (Friend, adding to the Hutchinson answer after the truncated operator line, as the MANIFEST notes; the analyst-based tag is right); 5,847 / 45,222 = 12.9% | PASS |
| P26 | §6 #5 "generally without requiring collateral"; "some customers have experienced financial difficulties up to and including bankruptcies"; 29% / 21%; receivables $5.9B up 26% | 438 (Item 1A) verbatim; P7; 5,931 / 4,717 = +25.7% | PASS |
| P27 | §6 #6 overhead 24.5%; "cut about 10,700 jobs from May 2023 to May 2026"; $443M FY2024 restructuring; $385M FY2026 severance; "positive operating leverage and gross margin in fiscal '27" | D7; 83,700 (`10-K-FY2023.txt` 318) − 73,000 (`10-K-FY2026.txt` 319) = 10,700, correct but **an unlabelled computation** → REVISE item 3; 3058 (Note 18) and `10-K-FY2024.txt` 875; 3052; `transcript.txt` 322 | **FAIL (label only)** |
| P28 | §6 legal: Belgian customs claims "beginning in fiscal 2018"; "unable to estimate the range of loss"; "could have a material adverse effect" | 2998 (Note 16) verbatim | PASS |
| P29 | §7 Hill 62 since 2024; Parker 70, CEO 2006–2020, Executive Chairman; Friend leaves September 4, 2026; Denton, CFO of Pfizer, announced June 23, 2026, start August 17 (8-K body says August 16); $7.25M sign-on; $4M award tied to FY2027 EBIT-margin growth | 369, 368; `8-K-2026-06-16.txt` 75 (Separation Date September 4, 2026), 79 and 250 (Pfizer), 73 ("effective as of August 16, 2026"), 244 (press release: "effective August 17"), `10-K-FY2026.txt` 378 and `DEF14A-2026.txt` 709 (August 17, 2026), 89 ("$7,250,000"), 91 ("$4,000,000 … Adjusted Operating Margin Growth targets (the growth rate of fiscal 2027 EBIT Margin measured in basis points above fiscal 2026 EBIT Margin"). The discrepancy is stated, as the brief required | PASS |
| P30 | §7 December 2025: Alagirisamy COO; Chief Commercial and Chief Technology Officer roles eliminated; four geography heads join the leadership team | `8-K-2025-12-01.txt` 69 (announced December 2, 2025, effective December 8), 73 (CCO role eliminated), 155 (EX-99.1: "eliminated the EVP, Chief Technology Officer role"), 157 (Dong, Grebert, Peddie, Sparks join the SLT) | PASS |
| P31 | §7 track record: revenue $51.4B → $46.4B; EBIT $6.5B → $3.85B; $100 → $36.47 vs $48.36 | A9; 882 ("EBIT \| $3,850 \| $3,778 \| $6,539"); DEF14A 1683 (Pay Versus Performance table, "$ 36.47 \| $ 48.36") | PASS |
| P32 | §7 cash: "bought back $17 billion of stock in FY2022–FY2025"; "paused repurchases under this program during the first quarter of fiscal 2026"; about $5.9B of $18B left; "24 consecutive years"; share count rose; no acquisition line in any cash flow statement | F1 sums to 3,994 + 5,509 + 4,254 + 2,955 = 16,712 (cash basis 16,729), so "$17 billion" is correct rounding but **an unlabelled sum** → REVISE item 4; 784 verbatim; 784 ("approximately $5.9 billion … remains available"; "$18 billion"); `press-release-FY2026-Q3.txt` 64 (Shareholder Returns); F7 (1,476 → 1,483); investing sections of `10-K-FY2026.txt` 1849–1855, `10-K-FY2024.txt` and `10-K-FY2023.txt` have no acquisition row (0 hits for "acqui" with a table separator) | **FAIL (label only)** |
| P33 | §7 incentives: "Adjusted Revenue and Adjusted EBIT", equally weighted; targets revenue +0.5%, EBIT −15%; 101% cut to 74%; FY2025 paid nothing; PSUs 0%, "at the 1st percentile"; $15M Hill retention, half service / half FY2027 EBIT margin growth "measured in basis points above fiscal 2026 EBIT Margin"; $36.3M; 746 to 1; "unanticipated restructurings" | DEF14A 777; 779 ("an increase of approximately 0.5% … a decrease of approximately 15%"); 666 and 783; 1132 ("No amounts were earned for fiscal 2025", Summary Compensation Table footnote; tag added, Direct fix 18); 908; 920, 922; 1113 and 1652 ($36,340,876); 1654; 636 (footnote inside Key Defined Terms, heading 617) | PASS, tag added |
| P34 | §7 ownership: 281M Class A / 1,202M Class B; Swoosh "formed by Mr. Philip Knight, NIKE's co-founder, in 2015"; about 79% of Class A, 16% if converted; Knight 9.8%; Chairman Emeritus; Travis Knight "has a significant role in the management" of the Swoosh shares; eight of eleven directors; 1.1% of Class B; Cook Lead Independent Director; "three-quarters" | DEF14A 2162 and `10-K-FY2026.txt` 1915; DEF14A 481 verbatim; 10-K 692 (Item 1A); DEF14A 1971; DEF14A 385, 2026 and 10-K 692; 10-K 692 ("Travis Knight, his son and a NIKE director, has a significant role in the management of th[e]…"); DEF14A 479 and 2094 (Class B elects three, Class A "the remaining eight"); 1979 ("18 persons … 1.1%"); 174, 381; Class B elects 25% rounded up, Class A the rest (479), so "three-quarters" is the designed split | PASS verbatim |
| P35 | outlook §1 lead: Q3 call on March 31, 2026; currency-neutral convention | `press-release-FY2026-Q3.txt` 68; `transcript-FY2026-Q3.txt` 37–38 and `transcript.txt` 38–40 ("All growth comparisons on the call today are presented on a year-over-year basis and are currency neutral unless otherwise noted") | PASS |
| P36 | outlook §2 ten quotes | `transcript.txt` 547–548 (Hill, answering Yih); 846 (Hill, answering Sherman); 66–67 (Hill prepared); 76–78 (Hill); 113–117 (Hill; "wholesale revenue grew 4%" 115); 123–124 (Hill); 687 (Friend, answering Boss; analyst-based tag); 548–549 (Hill, answering Yih); 283 (Friend prepared); 886–888 (Friend, answering Sherman) | PASS verbatim |
| P37 | outlook §3 quotes and paraphrases: running 105–108; "2.5x the number of kits compared to the same period in World Cup '22" 210 (Hill); "grows high single digits" 450 (Friend); North America wholesale "reported up 10%" and "we didn't sell in up 10% …" 947–950, "tough compare" 956–957 (Friend, answering Boruchow); EMEA "off-price was down over 50%" / "15-point improvement" 376–377 (Friend, EMEA paragraph); Greater China inventory 397–398 (Friend); "locally designed …" 745–746 (Hill, answering Hutchinson); Sportswear 233–236, 241 (Hill); Women's given no figure | all found at the lines stated; the Drbul exchange (571–633) mentions "Women's World Cup" (615) and "NIKE Pro, men's and women's" (624) with no figure, so the sentence is true, though the tag points at the only place women's is mentioned rather than at a women's question (none was asked) | PASS |
| P38 | outlook §4 "Not guided" and the Q3 sentence not repeated | see H15, H16 | PASS |
| P39 | outlook §4 "Q1 FY2027 is the quarter ending August 31, 2026" | fiscal year ends May 31 (MANIFEST; 10-K cover), so Q1 ends August 31 | PASS |
| P40 | outlook §5 claim 5 base: Greater China "recent performance" | G6 (−10% Q3, −17% Q4), A3 (−13% FY2026 cn, `10-K-FY2026.txt` 1090) | PASS |

**Verbatim character-for-character checks (at least three required):** all 16 §4 guidance items, all 12 §5 quotes, and the 47 further quotations in P4, P11, P13–P15, P18–P26, P28, P32, P34–P37 were run through the normalising matcher against the file each tag names: 75 quotations, 75 found exactly once each (two found twice: "more than a dozen new footwear styles" and the Item 5 buyback sentence, both identical repeats). Every speaker attribution matches the bracketed label governing the line.

**Totals:** 168 items checked (53 table rows in 3a–3f covering 257 cells, 24 cells in 3g, 16 in 3h, 12 in 3i, 40 prose entries in 3j, plus the 23 further quotation checks not otherwise listed); 164 PASS; 4 FAIL (P6, P8, P27, P32); 1 FAIL withdrawn with evidence (P17, the 3.1% rate, disclosed at Item 7A line 1629). Five greps that returned nothing on the first try (the Q3 "fixed cost base" quote, the 10-Q "$1.0 billion", "four to five months", "discounted prices", the Q3 "$4 billion") were all found on a shorter-fragment or normalised retry and were never ruled FAIL; they are line-wrap and column-truncation misses of the kind §17 warns about.

## 4. Jargon audit

Thinking as a 16-year-old, term by term:

| Term | Status before review | Action |
|---|---|---|
| Wholesale, NIKE Direct, Demand creation, Operating overhead, Gross margin, EBIT, Currency-neutral, Basis point, IEEPA tariffs, Sell-through, Classics | Glossary, one sentence each; all used in business.md or outlook.md | OK |
| Futures ordering program | Glossary entry, but the phrase never appears in either file's prose (§1 describes the practice without naming it) | Entry removed (Direct fix 19) |
| "gross-margin bridges" (§1), "gross-margin bridge" (§6 #3) | Analyst jargon, no gloss | Replaced with "year-by-year gross-margin explanations" / "gross-margin explanation" (Direct fixes 1, 15) |
| capex | Defined in the §3 table row label, but the prose uses it first | Fixed at first prose use: "capex (spending on buildings, equipment and technology)" (Direct fix 6) |
| "recast" (§2 table, footnote, prose) | Bare | Replaced with "restated" / "as restated" (Direct fixes 2, 4, 5) |
| "wholesale equivalent" basis (§2) | Bare, inside quotation marks | Glossed from `10-K-FY2024.txt` 964: "(NIKE Direct sales counted at wholesale prices, as if sold to a retailer)" (Direct fix 5) |
| "inventory write-down reserves" (§3) | Bare | Now "other costs including reserves for stock expected to sell below cost", which also aligns to the source (Direct fix 7) |
| "turns" (§3) | Bare | Fixed: "inventory turns (cost of sales divided by year-end inventory, roughly how many times a year the stock is sold through)" (Direct fix 8) |
| "diluted EPS" (§3) | Bare | "diluted earnings per share" (Direct fix 9) |
| Free cash flow (§4 table, then prose) | Row label only | Row label now "Free cash flow: cash from operations minus capex (computed)" (Direct fix 10) |
| "receivable" (§4) | Bare | "(owed to Nike but not yet received)" (Direct fix 11); §3 already reads "receivables … unpaid invoices" |
| "coupon", "ratings" (§4) | Bare | "average interest rate"; "credit ratings"; "committed credit lines" (Direct fix 12) |
| "the proxy's chart" (§7) | Bare | "the proxy statement (the document sent to shareholders before the annual meeting)" (Direct fix 17) |
| SG&A (outlook §1 row 5 and §4 quotes) | Bare in the row text | "(selling and administrative expense, demand creation plus operating overhead)" at first use (Direct fix 20) |
| "sell in" / "sell-in" (outlook §3 quote, §4 and §5 quotes) | Inside quotes, no gloss | "(sell-in: Nike's shipments to retailers)" at first use in §3 (Direct fix 22) |
| "tough compare" (outlook §3 quote) | Inside quote | "(a strong year-ago quarter to beat)" (Direct fix 23) |
| "off-price", "full price realization" (outlook §3 quotes) | Inside quotes | "(off-price: sales through discount channels)"; "(the share of sales made at full price)" (Direct fix 24) |
| Win Now, Sport Offense, vertical sport teams | Explained at first use in business.md §1 and outlook §2 | OK |
| Jordan Brand, Converse, Sportswear, Jordan Streetwear, NIKE Brand Digital, factory stores (outlets), order book, markdowns, discounting, endorsement contracts, severance, restructuring, credit lines, share classes | Plain or name-inferable; "factory stores" is glossed "(outlets)" | OK |
| "statement footwear", "halo", "sequential deceleration", "operating leverage", "fleet" | Only inside verbatim management quotes whose surrounding sentence or row label carries the meaning; no source gives a definition to quote, so none was invented | Left as quoted |
| Return on invested capital, cash conversion, EBIT margin, currency-neutral | Defined in row labels or §4 prose ("Nike divides after-tax operating profit by the capital tied up") | OK |
| moat | Spec vocabulary, used in the §5 sense the whole library uses | OK |

Glossary now holds 11 entries, each one sentence, each used in business.md or outlook.md.

## 5. Invented-number check

| Item | Finding |
|---|---|
| Every "(computed)" cell and percentage in both files | Labelled and re-derived exactly (§3 above), including both ex-refund rows of the §3 table, the ex-refund EBIT margin and North America EBIT in outlook §1, the Q4-alone cash flows, and the FY2023 Direct share now shown as disclosed |
| §1 "(our inference from the year-by-year gross-margin explanations in §3)" | Labelled |
| §2 "$1.0 billion" added by a weaker dollar | **Unlabelled computation presented as a disclosed figure**; no source states it (P6). REVISE item 1 |
| §2 "after two years of deliberately shipping less" | **Not supported** for FY2024 by the cited 10-K FY2025 Item 7 or by the draft's own table (P8). REVISE item 2 |
| §3 "about 210" basis points from the refund; "40.8%" | Friend's stated figures (transcript 333–335); the table separately labels the 40.8% computed, and the two agree |
| §3 turns 3.8 → 3.5; §4 cash exceeds debt by $1.1B; §5 four times Converse; §6 95%, 13%, $4.4B; §2 shares | All labelled computed and re-derived |
| §6 #6 "about 10,700 jobs" | Correct difference of two disclosed headcounts, **unlabelled** (P27). REVISE item 3 |
| §7 "$17 billion of stock in FY2022–FY2025" | Correct rounding of a sum of four disclosed figures, **unlabelled** (P32). REVISE item 4 |
| §7 "whether that base includes the $986 million refund is not stated" | A fair negative: DEF14A 922 defines the base as "fiscal 2026 EBIT Margin … as set forth in the audited consolidated financial statements" under a metric named "Adjusted", and the Key Defined Terms footnote (636) lists what is adjusted without naming tariff refunds |
| §7 "Our observation: every yardstick is 'adjusted' …" | Labelled as the writer's observation; the quoted exclusions are at DEF14A 636 |
| §6 #1 "the styles promised for the second half of FY2027 fail at full price" and other "What must happen" lines | Scenario conditions, not presented as facts |
| outlook §3 "Working if …" lines; §5 sharpenings | Analyst tests and labelled sharpenings, not facts |
| outlook §1 "the −4% currency-neutral sits at the bottom of the range, the −1% reported inside it" | Reading of two sourced numbers against a sourced guide (down 2% to 4% currency-neutral plus a 2-point FX benefit implies 0% to −2% reported) |
| Every other figure in both files | Carries a tag that supports it; no untagged figure found. The "3.1% average coupon" first looked unsupported by its Note 6 tag and is disclosed at Item 7A (P17; tag added) |

## 6. As-of check

- Latest-dated facts used: the 2026-07-15 10-K and proxy (the proxy names the 2026-09-08 annual meeting as a scheduled date, quoted as such in Sources), the 2026-06-30 call and release, the 2026-06-23 CFO 8-K. All within cutoff. The MANIFEST records the transcript PDF as posted 2026-07-01, before the cutoff.
- Future events announced before the cutoff are phrased as announced, not as having happened: Denton "was announced on June 23, 2026 to start August 17 (the 8-K body says August 16)"; Friend "is due to leave on September 4, 2026" (was "leaves on", tightened, Direct fix 16, since the run date is after that day); Win Now "are to be sunset"; Investor Day "November 16 and 17" as a plan; claims 7–11 are written as things to check on the Q1 FY2027 call and 10-Q.
- A regex scan of both files for August/September/October 2026 and for Q1 FY2027 results, calls or releases finds only the two "Written 2026-09-08" run-date lines, the claims themselves, and the proxy's meeting date. No Q1 FY2027 result, no post-cutoff 8-K (the 2026-08-10 filing was not fetched per MANIFEST and nothing relies on it), no September 2026 material anywhere in either draft.
- The "Written 2026-09-08" date is the run date, with the as-of label separate. Correct.

## 7. Length

`cd /home/ubuntu && python3 -P /tmp/nke-orch/wc_prose.py companies/NKE/business.md companies/NKE/outlook.md`: business.md 2,475 before / **2,561 after** direct fixes; outlook.md 963 before / **993 after**. Both in range; the glosses added 86 and 30 words. The four REVISE edits below add perhaps 15 words.

## 8. Verdict

**REVISE.** Four small factual items, all in business.md, each one clause; no structural change. The writer should:

1. **§2, third paragraph (line 29):** "A weaker dollar added about $1.0 billion of FY2026 revenue, so flat reported revenue was down 2% 'currency-neutral' (at the prior year's exchange rates) [10-K FY2026, Item 7]." No cached source gives a dollar or point figure for the currency effect on FY2026 revenue (`10-K-FY2026.txt` 991 and `press-release.txt` 20, 62 give only "flat on a reported basis and down 2% on a currency-neutral basis"; both transcripts give none). Either label it: "about $1.0 billion (computed from the reported and currency-neutral growth rates; the 10-K gives only the rates)", or drop the dollar figure: "A weaker dollar added about two points of growth, so flat reported revenue was down 2% 'currency-neutral' …". Keep the tag.
2. **§2, "Wholesale, 61% of NIKE Brand" paragraph (line 43):** "after two years of deliberately shipping less [Q4 FY2026 call, prepared remarks, Hill] [10-K FY2025, Item 7]". The draft's own channel table shows wholesale currency-neutral growth of +2% in FY2024 and −6% in FY2025; `10-K-FY2025.txt` 862 and 878 describe the deliberate supply reduction for fiscal 2025 only, and `10-K-FY2024.txt` carries no such statement. Reword to what the sources show, e.g. "after a year of deliberately shipping less to reduce the supply of classic footwear [10-K FY2025, Item 7]".
3. **§6 #6 (line 130):** "Nike cut about 10,700 jobs from May 2023 to May 2026" is the difference of two disclosed headcounts (83,700, `10-K-FY2023.txt` 318; 73,000, `10-K-FY2026.txt` 319). Add "(computed)" after "10,700 jobs"; the tags already present support the inputs.
4. **§7, "Cash" paragraph (line 153):** "Nike bought back $17 billion of stock in FY2022–FY2025" is a sum of the four disclosed repurchase figures (3,994 + 5,509 + 4,254 + 2,955 = 16,712; the table above it carries all four). Write "about $16.7 billion (computed)" or "$17 billion (computed)" so the reader knows it is the writer's sum.

After these four edits the writer should re-run `cd /home/ubuntu && python3 -P /tmp/nke-orch/wc_prose.py companies/NKE/business.md companies/NKE/outlook.md` (currently 2,561 / 993) and confirm both stay in range.

Optional notes, not blocking, for the owner or the next refresh:

- The §2 channel table computes FY2023 NIKE-owned store dollars (8.7) from the as-first-reported Digital figure (12.6); on the restated 12.4 it would be 8.9. Both bases are visible in the row above, so the reader can see it; a future refresh could pick one basis and say so.
- Indicator 3's "excluding any named one-time item" half will read "none" in most quarters; that is fine, but the refresh grader should not treat its absence as 🔇.
- outlook §3's "Women's was given no separate figure [Q4 FY2026 call, Q&A, Drbul/BTIG]" is true but the tag points at the only place women's product is mentioned (Hill's innovation answer, lines 615 and 624), not at a women's question; no analyst asked one. Consider "No analyst asked about Women's and management gave it no separate figure [Q4 FY2026 call, Q&A]".
- Claim 7 (Denton signs the Q1 FY2027 10-Q) depends on the 10-Q being filed after his start date, which the announced dates make near-certain; if the filing is signed by someone else for a procedural reason the grader should record what the 10-Q shows rather than infer anything about the appointment.

## Direct fixes (recorded per §13)

Word counts: business.md 2,475 → 2,561; outlook.md 963 → 993. All edits were in-line; each replacement matched exactly once (script `/tmp/nke-orch/reviewer/apply_fixes.py`; pre-edit copies in `/tmp/nke-orch/reviewer/business.before.md` and `outlook.before.md`). No number was changed. No git command was run.

**business.md**

1. §1 line 8: "(our inference from the gross-margin bridges in §3)" → "(our inference from the year-by-year gross-margin explanations in §3)". (jargon)
2. §2 channel table line 35: "12.6 (12.4 recast)" → "12.6 (12.4 as restated)". (jargon)
3. §2 channel table line 37: FY2023 "~44% (computed)" → "~44%", because `10-K-FY2023.txt` 824 discloses "approximately 44% of total NIKE Brand revenues for fiscal 2023" and the footnote already carries [10-K FY2023, Item 7]. (label alignment; number unchanged)
4. §2 footnote line 41: "FY2023 Digital was recast to $12.4 billion [10-K FY2024, Item 7]." → "FY2023 Digital was restated to $12.4 billion in the following year's 10-K [10-K FY2024, Item 7]." (jargon; source `10-K-FY2024.txt` 1066)
5. §2 line 56: "reported on a "wholesale equivalent" basis to FY2024 and recast in FY2025," → "reported on a "wholesale equivalent" basis (NIKE Direct sales counted at wholesale prices, as if sold to a retailer) to FY2024 and restated on a reported basis in FY2025,". (jargon; gloss from `10-K-FY2024.txt` 964: internal sales to NIKE Direct "charged at prices comparable to those charged to external wholesale customers")
6. §3 line 60: "capex is 1–2% of revenue" → "capex (spending on buildings, equipment and technology) is 1–2% of revenue". (jargon)
7. §3 line 78: "and inventory write-down reserves (about 90) as Nike cut Classics supply" → "and other costs including reserves for stock expected to sell below cost (about 90) as Nike cut Classics supply", matching `10-K-FY2025.txt` 1063 "Higher other costs (decreasing gross margin approximately 90 basis points), including higher inventory obsolescence reserves". (wording alignment to source plus jargon; tag unchanged)
8. §3 line 80: "so turns slowed from 3.8 in FY2024 to 3.5 in FY2026 (computed)" → "so inventory turns (cost of sales divided by year-end inventory, roughly how many times a year the stock is sold through) slowed from 3.8 in FY2024 to 3.5 in FY2026 (computed)". (jargon)
9. §3 line 82: "$0.52 of the quarter's $0.72 diluted EPS" → "$0.52 of the quarter's $0.72 diluted earnings per share". (jargon)
10. §4 table line 90: row label "Free cash flow (computed)" → "Free cash flow: cash from operations minus capex (computed)". (jargon)
11. §4 line 102: "$684 million of the refund was still a receivable at year-end" → "$684 million of the refund was still a receivable (owed to Nike but not yet received) at year-end". (jargon)
12. §4 line 104: "the bonds carry a 3.1% average coupon with $2 billion due in FY2027, $3 billion of credit lines are undrawn, and the ratings were cut in 2025 from AA-/A1 to A+/A2 [10-K FY2026, Note 6] [10-K FY2026, Note 5] [10-K FY2026, Item 1A]." → "the bonds carry a 3.1% average interest rate with $2 billion due in FY2027, $3 billion of committed credit lines are undrawn, and the credit ratings were cut in 2025 from AA-/A1 to A+/A2 [10-K FY2026, Item 7A] [10-K FY2026, Note 6] [10-K FY2026, Note 5] [10-K FY2026, Item 1A] [10-K FY2025, Item 7] [10-Q Q3 FY2026, Item 2]." The 3.1% is the TOTAL column of the Item 7A rate table (`10-K-FY2026.txt` 1629); "AA- to A+" is `10-K-FY2025.txt` 1549; "A1 to A2" is `10-Q-FY2026-Q3.txt` 1792; the FY2026 10-K (696, Item 1A) says only that both agencies downgraded in 2025. (jargon; three tags added; see P17 withdrawal)
13. §5 line 108: added "[10-K FY2026, Item 1]" before "[Q4 FY2026 call, Q&A, Yih/Barclays]" for "in over 190 jurisdictions worldwide" (`10-K-FY2026.txt` 289). (missing tag)
14. §5 line 112: "In FY2026 it says it gained "5 points of running market share in statement footwear, more than any other top 5 brand"" → "In FY2026 it says it gained, in Western Europe and North America, "5 points …"", restoring the scope Hill stated (`transcript.txt` 106–107: "across Western Europe and North America"). (wording alignment to source; quote and tag unchanged)
15. §6 #3 line 124: "in each quarter's gross-margin bridge" → "in each quarter's gross-margin explanation". (jargon)
16. §7 line 136: "CFO Matthew Friend leaves on September 4, 2026;" → "CFO Matthew Friend is due to leave on September 4, 2026;". (as-of phrasing: an announced future event, `8-K-2026-06-16.txt` 75)
17. §7 line 138: "the proxy's chart shows $100 invested" → "the proxy statement (the document sent to shareholders before the annual meeting) shows $100 invested". (jargon)
18. §7 line 155: "FY2025 paid nothing [DEF 14A 2026, Annual Cash Incentive]." → "FY2025 paid nothing [DEF 14A 2026, Annual Cash Incentive] [DEF 14A 2026, Summary Compensation Table]." (tag added: `DEF14A-2026.txt` 1132 "No amounts were earned for fiscal 2025")
19. Glossary: removed "Futures ordering program"; the phrase is used in neither file's prose. (unused glossary term)

**outlook.md**

20. §1 row 5 line 14: "Total SG&A only:" → "Total SG&A (selling and administrative expense, demand creation plus operating overhead) only:". (jargon)
21. §3 line 29: ""5 points of running market share in statement footwear" [Q4 FY2026 call, prepared remarks, Hill]." → ""5 points of running market share in statement footwear" in Western Europe and North America [Q4 FY2026 call, prepared remarks, Hill]." (wording alignment to source, as Direct fix 14)
22. §3 line 33: after the Boruchow quote ending "lower discount and lower cancellations."" added "(sell-in: Nike's shipments to retailers)" before the tag. (jargon)
23. §3 line 33: "Q2 "has a tough compare in North America"" → "Q2 "has a tough compare in North America" (a strong year-ago quarter to beat)". (jargon)
24. §3 line 35: ""off-price was down over 50%" with a "15-point improvement in full price realization"" → ""off-price was down over 50%" (off-price: sales through discount channels) with a "15-point improvement in full price realization" (the share of sales made at full price)". (jargon)

Nothing else in either file was touched in cycle 1.

---

## Cycle 2 (final): re-check of the four REVISE items

_Reviewed 2026-09-09 against the same `sources/FY2026-Q4/` cache (unchanged: `find -newer` against the cycle-1 pre-edit copy returns nothing). business.md re-read from disk (copy kept at `/tmp/nke-orch/reviewer/business.cycle2.md`). A `diff` of the writer's business.md against my reconstructed cycle-1 post-fix state (`/tmp/nke-orch/reviewer/business.recon.md`, produced by re-applying the 24 logged edits to the pre-edit copy with `apply_fixes_recon.py`) shows exactly four changed lines (29, 43, 130, 153) and nothing else; outlook.md is byte-identical to my cycle-1 state. None of the 24 direct fixes was reverted. Word counts by `cd /home/ubuntu && python3 -P /tmp/nke-orch/wc_prose.py`: business.md 2,578 as received from the writer (writer reported 2,578), 2,584 after the two cycle-2 direct fixes below; outlook.md 993 (unchanged). Both in range._

| # | Item | Draft now reads | Source line(s) | Result |
|---|---|---|---|---|
| R1 | §2 currency sentence (line 29) | 'The 10-K puts the translation benefit from a weaker dollar … at "approximately $1,023 million" of FY2026 revenue, so flat reported revenue was down 2% "currency-neutral" (at the prior year's exchange rates) [10-K FY2026, Item 7].' | `10-K-FY2026.txt` line 1451 (Item 7, which runs 812–1595; subsection "Foreign Currency Exposures and Hedging Practices", heading 1405, "Translational Exposures", heading 1449): "The impact of foreign exchange rate fluctuations on the translation of our consolidated Revenues was a benefit of approximately $1,023 million for the year ended May 31, 2026." The quote is verbatim, the tag is right, and 1,023 / 46,309 = 2.2 points, consistent with the reported 0% versus currency-neutral −2% at line 991. **Cycle-1 FAIL P6 withdrawn with this evidence:** my cycle-1 searches were for "$1.0 billion", "1.0 billion" and "percentage point" near "currency", and for the dollar figure in the transcripts and release; the 10-K states it as "$1,023 million" in the hedging section, which those patterns did not reach. The writer was right that the figure is disclosed; the cycle-1 draft's fault was only that it gave a rounded figure without the quote or the location, which the new sentence fixes. "Translation benefit" was glossed directly (Direct fix 25) | PASS; cycle-1 FAIL withdrawn |
| R2 | §2 wholesale paragraph (line 43) | "after a year of deliberately shipping less to reduce the supply of classic footwear [Q4 FY2026 call, prepared remarks, Hill] [10-K FY2025, Item 7] [Q3 FY2026 call, prepared remarks, Hill]" | "a year": `10-K-FY2025.txt` 862 ("Our results for fiscal 2025 reflected … our actions to reduce supply of certain footwear products in the marketplace") and 878; "two years" is gone (0 hits). "classic footwear": the FY2025 10-K never uses the word "classic" (0 hits in the whole file; it says "certain footwear products"), and Hill's Q4 prepared remarks (lines 53–264) do not either; the phrase is Hill's on the Q3 call, `transcript-FY2026-Q3.txt` 215–216 ("intentionally reduced over $4 billion of revenue from the peak levels of classic footwear franchises"), and Friend's at `transcript.txt` 271 ("reducing classic footwear franchises by more than $2 billion"). The sentence lacked a tag for those two words, so [Q3 FY2026 call, prepared remarks, Hill] was added (Direct fix 26); the prefix is already mapped in Sources | PASS after tag fix |
| R3 | §6 #6 (line 130) | "Nike cut about 10,700 jobs (computed) from May 2023 to May 2026" | 83,700 (`10-K-FY2023.txt` 318) − 73,000 (`10-K-FY2026.txt` 319) = 10,700; label present; tags unchanged | PASS |
| R4 | §7 Cash paragraph (line 153) | "Nike bought back about $16.7 billion of stock (computed) in FY2022–FY2025 at falling prices" | 3,994 + 5,509 + 4,254 + 2,955 = 16,712 (§3f F1: `10-K-FY2022.txt` 1376; `10-K-FY2023.txt` 1871; `10-K-FY2024.txt` 1925; `10-K-FY2025.txt` 1962); "$17 billion" gone (0 hits) | PASS |

**Other checks repeated.** business.md skeleton: §1–§8 headings in order (lines 4, 12, 58, 84, 106, 116, 134, 159), `_Proposed — owner to review and lock._` at line 161, Glossary (11 entries, one sentence each; "Futures ordering program" still absent) at 174, Sources at 188 with every tag prefix used in the file mapped, including the [Q3 FY2026 call, …] prefix the new tag uses. outlook.md unchanged: headings §1–§5, no §6, Sources, header `_Transcript source tier: company-published. Written 2026-09-08._`. As-of scan of both files: nothing dated after 2026-07-15 beyond the two run-date lines, the proxy's meeting date and the forward-looking claims. No source file was touched. No git command was run.

**Cycle-2 direct fixes (both in business.md, recorded per §13):**

25. §2 line 29: "the translation benefit from a weaker dollar at" → "the translation benefit from a weaker dollar (foreign sales converting into more dollars) at". (jargon; the 10-K's own explanation at line 1451: "a weaker U.S. Dollar in relation to foreign functional currencies benefits our consolidated earnings")
26. §2 line 43: appended "[Q3 FY2026 call, prepared remarks, Hill]" after "[10-K FY2025, Item 7]", sourcing the words "classic footwear" to `transcript-FY2026-Q3.txt` 215–216. (missing tag)

Nothing else in either file was touched in cycle 2.

**Final verdict: PASS.** Nothing open. Totals across both cycles: 168 items checked, 165 PASS, 3 FAIL fixed by the writer and re-verified (P8, P27, P32), 2 FAILs withdrawn with evidence (P17 in cycle 1, P6 in cycle 2). The four optional notes from cycle 1 (the FY2023 store-dollar basis; indicator 3's conditional half; the Women's sentence's tag; claim 7's dependence on the 10-Q signing) stand as notes for the owner and the next refresh, not as conditions.
