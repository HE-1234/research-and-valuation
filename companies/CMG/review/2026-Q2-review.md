# Chipotle Mexican Grill (CMG) — Reviewer report, 2026-Q2 (cycles 1–2)

_Reviewed 2026-09-08/09 against `companies/CMG/sources/2026-Q2/` only (cached full texts; the `notes-*.md` files were not used as evidence). As-of cutoff 2026-07-31; nothing dated later was consulted except the Motley Fool transcript page (posted 2026-08-07) for call content, as §12.2 allows. Line numbers (l.N) are line numbers of the cached `.txt` files; for the two decks the printed page is also given (Q4 2025 deck page map from the footers: p.7 = l.189–207, p.9 = l.224–257, p.13 = l.304–326, p.14 = l.327–365; Q2 2026 deck p.4 = l.65–101 of non-empty text, footer at l.101, p.6 footer l.135, p.7 footer l.176). Draft line numbers refer to `business.md` (193 lines) and `outlook.md` (92 lines); the direct fixes below were made in place and did not change line counts. Word counts by `python3 -P /tmp/cmg-orch/wc_prose.py` from cwd `/home/ubuntu`; the writer's 2,787 / 1,102 reproduced exactly before edits. Scratch scripts in `/tmp/cmg-orch/reviewer/` (`find.py` normalised full-line search across all cached texts, `quotes.py` quote sweep, `tags.py` tag-prefix extraction, `apply_fixes.py` with a one-occurrence assertion per replacement; originals kept as `business.orig.md` / `outlook.orig.md`)._

**Final verdict (cycle 2, 2026-09-09): PASS.** The writer applied all five cycle-1 REVISE items; each re-verified against the cited source lines, every cycle-1 direct fix is still in place, the quote sweep and tag-prefix check are clean, and both files are within the length limits (business.md 2,950, outlook.md 1,186). Details in the Cycle 2 section at the end of this file. The cycle-1 record follows unchanged.

**Cycle-1 verdict: REVISE** — five factual items for the writer, all cell- or clause-level with the evidence and the exact correction given in §10. Everything else checked out or was fixed directly: 310 table cells verified against the tagged text (every "(computed)" cell re-derived, every "not disclosed" cell searched with full-line output), 3 FAIL, all three being "not disclosed" cells whose number a cached filing or deck does print; 135 quoted strings swept, every substantive quote found verbatim; about 90 prose facts checked with 2 wording slips (both fixed) and 1 factual slip (a date, in REVISE); no invented number; no call-only figure presented as anything but a spoken statement after two tag fixes; 12 claims that all pass §9; 7 indicators anchored to recurring disclosures. Direct fixes: 29 replacements in business.md and 11 in outlook.md (glosses, tag precision, two "(computed)" labels, four wording-precision edits), listed in §9.

---

## 1. Skeleton compliance

**business.md**

| Requirement (§6) | Status |
|---|---|
| `# Chipotle Mexican Grill — The Business` | OK, exact (l.1) |
| `_As of Q2 2026. Written 2026-09-08._` | OK, exact (l.2); fiscal year = calendar year, no parenthetical needed |
| §1 What they do, with a history paragraph | OK (history l.12: Denver 1993, 1998 investment, 2006 IPO, 2015–2018 food safety, 2020 DPA, 2024 CEO change, 2026 strategy) |
| §2 How the money comes in, 5-year table | OK: revenue-stream and segment table FY2021–FY2025 plus H1 2026 (l.16–25); KPI table comps / transactions / check / menu price / AUV / units / openings / Chipotlanes / partner units (l.33–43) |
| §3 The economics: revenue, margins, capex, capex/revenue, 5 years | OK (l.53–65); no gross margin exists, restaurant-level operating margin stands in and l.49 says so; both margins carried, capex and capex/revenue |
| §4 How profitable, really, 5-year table | OK (l.73–83): OCF, capex, OCF less capex, net income, conversion, EPS, buybacks, cash and investments, debt |
| §5 Why customers don't leave | OK: four sources of habit and three weakening signs (l.93–95) |
| §6 What could break it, ranked, concentration | OK: seven ranked scenarios each with early warning and exposure (l.101–113); concentration paragraph l.115 |
| §7 Who runs it and what they do with the cash | OK: people, pay and the 2025 vote, track record, cash, capital-return table (l.119–136) |
| §8 Indicators (5–8; name / why / where) | OK: 7 indicators, each with a recurring location (l.142–150); one-off targets parked as claims (l.152) |
| `_Proposed — owner to review and lock._` | OK (l.140) |
| Glossary, one sentence each | OK: 5 entries (comps, restaurant-level operating margin, Chipotlane, AUV, partner-operated), each one sentence, each unavoidable |
| Sources list maps every tag prefix | OK. `tags.py`: 27 prefixes used, 27 listed (four 10-Ks, two 10-Qs, DEF 14A, thirteen 8-Ks, three releases, two decks, the Mexico release, the call); filing dates match MANIFEST; the call entry states tier 3, the 2026-08-07 posting, the line-number convention and the numbers-from-filings rule. Unchanged after the fixes (the added tags use existing prefixes) |
| Heading order | OK |

**outlook.md**

| Requirement (§7) | Status |
|---|---|
| `# Chipotle Mexican Grill — Outlook as of Q2 2026` | OK, exact (l.1) |
| `_Transcript source tier: third-party (The Motley Fool). Written 2026-09-08._` | OK, exact (l.2); matches MANIFEST tier 3 |
| §1 one row per indicator; this quarter / last quarter / expected | OK: 7 rows in business.md §8 order; header note says the set is proposed and that the Q1 outlook was full-year only (l.6) |
| §2 What management says | OK (l.20–22), quotes where wording matters |
| §3 Growth engines (what / how big / claim / working-if) | OK: seven engines, each with a "Working if" line (l.26–38) |
| §4 Guidance, verbatim | OK: written outlook across three releases (l.44–48) and a spoken table labelled "wording only" (l.50–64); one factual slip on capex, see §10 item 5 |
| §5 Claims | OK: 12 claims (l.68–79) |
| §6 Tone shift | Correctly omitted (first run) |
| Sources | OK: 10 prefixes used, 10 listed; call entry states tier, posting date, l.N convention, and that numbers come from release, decks and filings |

---

## 2. Rubric (§14)

| # | Question | Answer | Reasoning |
|---|---|---|---|
| 1 | Two sentences on what they do and who pays | Yes | l.6–8: 4,186 owned restaurants; "The diner pays at the counter, in the app or through a delivery company, and that is the whole of the revenue"; the owned-versus-franchised contrast is spelt out with the income-statement evidence. |
| 2 | What would kill it and the early warning | Yes | §6 ranks seven scenarios (food safety, unrecovered inflation, value perception, new-unit dilution, competition, delivery/technology dependence, leadership turnover), each with an early-warning line tied to a recurring disclosure and an exposure figure. |
| 3 | Why margins are what they are; does cost scale with usage | Yes | l.49 walks $100 of sales through the four restaurant cost lines to 25.4% and then to 16.2%; l.51 says food is linear, labor and rent are fixed per restaurant, G&A flattens with scale, and menu price is the offsetting lever. |
| 4 | Predict next quarter's scorecard from §5 alone | Yes | 12 claims, each tied to a printed number, a release section, a call statement or a dated event. |
| 5 | Nothing required outside knowledge | Yes, after glosses | Terms a 16-year-old would not know (proxy, MD&A, registration-rights agreement, IPO, mix, working capital, impairment, basis points, cyclospora, class action, say-on-pay, performance shares, retained earnings, treasury stock, HEEP, throughput, lap, cash-on-cash, attachment rate, non-GAAP, EPS, legal accrual) glossed directly (§5). |

Owner's specific asks, one line each:

- (a) **Owned-and-operated versus franchisor**: l.8 explains what a franchisor is, quotes the 10-K ("Our revenue is derived from sales by our restaurants"), points to the two revenue lines with no royalty or rent line, quotes the proxy ("we own all of our restaurants (except the franchised restaurants in the Middle East)"), and draws the four consequences (large revenue, lower margins that move with food and wages, growth on Chipotle's own capital, direct control of execution). Plain. The 15 partner-operated exceptions follow at l.10.
- (b) **Restaurant-level operating margin and where costs go**: l.49 defines it (revenue less the four restaurant cost lines; excludes head office, depreciation, pre-opening, impairment) and gives the $100 walk: $29.60 food and packaging, $25.10 crews, $5.20 rent, $14.70 other, $25.40 left; then $5.50 head office, $3.00 depreciation, $0.40 pre-opening, $0.20 impairment to a 16.2% operating margin. Every figure verified (§3(c)). Plain.
- (c) **New-unit growth as the main engine**: l.31 uses the 10-K's own bridge: in 2025 comps subtracted $191 million while restaurants opened in 2024–2025 added $809 million, so revenue grew $612 million on a negative comp; l.31 adds that quarterly comps have run between (4.0%) and 2.2% since the start of 2025. §3 l.69 shows two-thirds of the 2026 capex plan buys new restaurants. Plain.
- (d) **The 2024 management change and track record**: §7 l.119 (Niccol out August 2024, Boatwright interim then CEO November 2024, Hartung retirement and Rymer as CFO, COO/brand/legal/digital turnover, independent Chairman Maw), l.121 (retention awards, the 55% say-on-pay vote and the committee's pledge, bonus and PSU design, pay ratio, ownership), l.123 (comps missed 2025 guidance; openings inside every guided range; stock $100 to $134 versus $196 for the S&P 500). Present and plain; one date slip in §1 (REVISE item 1).
- (e) **KPIs anchor the indicators**: §8 indicators 1–5 are exactly comps with the transactions/check split, restaurant-level operating margin with the four cost lines, openings with Chipotlanes and the unit counts, AUV, and digital share; 6–7 add operating margin/G&A and capital return. Outlook §1 reports all seven for Q2 and Q1 from the two releases (§3(f)).

---

## 3. Citation spot-check

Legend: PASS = the tagged source prints the number or text at the line shown. Computed cells re-derived from the sourced inputs. Statements are in USD thousands in the filings; the draft converts to millions.

### 3(a) business.md §2 revenue and segment table (l.16–25), every cell

Inputs: `10-K-FY2023.txt` l.1277 (food and beverage 9,804,124 / 8,558,001 / 7,457,169), l.1279 (delivery 67,525 / 76,651 / 89,892), l.1281 (total 9,871,649 / 8,634,652 / 7,547,061); `10-K-FY2025.txt` l.1263 (11,866,051 / 11,247,384), l.1265 (59,550 / 66,469), l.1267 (11,925,601 / 11,313,853); `10-Q-2026-Q2.txt` l.245 (6,405,522), l.247 (31,282), l.249 (6,436,804). Growth: `10-K-FY2022` l.684 ("Total revenue increased 14.4%"), `10-K-FY2023` l.742 (14.3%), `10-K-FY2024` l.755 (14.6%), `10-K-FY2025` l.749 (5.4%), `10-Q` l.985 (8.4%). Segments: `10-K-FY2025` l.2457 (U.S. segment total revenue 11,679,417 / 11,111,732 / 9,720,369), l.2461 (all other revenue 246,184 / 202,121 / 151,280), l.2499 (definition: Canada, Europe and partner royalties); `10-Q` l.855 (6,289,189). Digital: `10-K-FY2022` l.694 (39.4% in 2022, 45.0% in 2021), `10-K-FY2023` l.255 (37.4%), `10-K-FY2024` l.255 (35.1%), `10-K-FY2025` l.255 (36.7%), `press-release.txt` l.38 (38.3%). Delivery orders: `10-K-FY2022` l.368 ("Approximately 19%"), `10-K-FY2023` l.384 ("Approximately 18%"), `10-K-FY2024` l.407 ("Over 15%"), `10-K-FY2025` l.387 ("Over 16%").

| Row | Result |
|---|---|
| Food and beverage revenue 7,457.2 / 8,558.0 / 9,804.1 / 11,247.4 / 11,866.1 / 6,405.5 | PASS ×6 |
| Delivery service revenue 89.9 / 76.7 / 67.5 / 66.5 / 59.6 / 31.3 | PASS ×6 |
| Total revenue 7,547.1 / 8,634.7 / 9,871.6 / 11,313.9 / 11,925.6 / 6,436.8 | PASS ×6 |
| Revenue growth not disclosed / 14.4 / 14.3 / 14.6 / 5.4 / 8.4% | PASS ×5 on the stated figures. FY2021 "not disclosed": no filing states 2021 growth (the FY2022 10-K's MD&A compares 2022 with 2021 only), so the cell is defensible; but the FY2022 10-K income statement prints FY2020 total revenue 5,984,634 (l.1163), so 26.1% (computed) is available. Recommended in REVISE item 3, owner's call |
| U.S. segment revenue not disclosed / not disclosed / 9,720.4 / 11,111.7 / 11,679.4 / 6,289.2 | PASS ×4 on the stated figures; FY2021 "not disclosed" PASS (the FY2023 10-K has no segment revenue split and no geographic revenue line: `find.py` for "U.S. segment", "All other revenue", "Canada" with "revenue" in `10-K-FY2023.txt` returns nothing). **FY2022 "not disclosed" FAIL**: `10-K-FY2024.txt` l.2409 "U.S. segment total revenue | 11,111,732 | 9,720,369 | 8,516,210" (Note 14, Segment Reporting) |
| All other revenue not disclosed / not disclosed / 151.3 / 202.1 / 246.2 / 147.6 (computed) | PASS ×3 stated; 147.6 = 6,436.8 − 6,289.2 (the 10-Q's Note 14 has no all-other line, l.841–889), PASS; FY2021 PASS as above; **FY2022 "not disclosed" FAIL**: `10-K-FY2024.txt` l.2413 "All other revenue (1) | 202,121 | 151,280 | 118,442" |
| Digital 45.0 / 39.4 / 37.4 / 35.1 / 36.7 / 38.3% (Q2) | PASS ×6 |
| Delivery orders not disclosed / about 19 / about 18 / over 15 / over 16% / not disclosed | PASS ×4 stated; FY2021 "not disclosed" PASS (the FY2022 10-K's only delivery-share sentence, l.368, covers 2022); H1 2026 "not disclosed" PASS (`find.py -i "delivery orders"` in `10-Q-2026-Q2.txt` returns nothing) |

46/48 PASS, 2 FAIL (REVISE item 3).

### 3(b) business.md §2 KPI table (l.33–43), every cell

Inputs: comps `10-K-FY2022` l.746 ("8.0% | 19.3%"), `10-K-FY2023` l.802, `10-K-FY2024` l.827, `10-K-FY2025` l.815 ("(1.7%) | 7.4%"), `10-Q` l.989 (six months 1.4%); transactions / check / menu price `10-K-FY2023` l.804–808 ("5.0% | 0.9%", "2.9% | 7.1%", "5.2% | 12.0%"), `10-K-FY2024` l.829–833, `10-K-FY2025` l.817–821 ("(2.9%)", "1.2%", "2.1%"), `10-Q` l.991–995 (six months 0.8%, 0.6%, 1.3%); AUV `10-K-FY2022` l.744 ("$2.8 | $2.6"), `10-K-FY2023` l.800 ("$3.0 | $2.8"), `10-K-FY2024` l.825 ("$3.213 | $3.018"), `10-K-FY2025` l.813 ("$3.104 | $3.213"), `10-Q` l.987 ("$3.102"); units `10-K-FY2022` l.724 (3,187 / 2,966), `10-K-FY2023` l.780 (3,437), `10-K-FY2024` l.793 (3,726), `10-K-FY2025` l.781 (4,042), `10-Q` l.951 (4,186); openings `10-K-FY2022` l.716 (Chipotle 235 / 215) and l.718 (Pizzeria Locale 1 / -), l.702 ("we opened 236 new restaurants, which included 202 restaurants with a Chipotlane"), `10-K-FY2023` l.770–772 (270 + 1) and l.752 ("opened 271 ... 238 ... with a Chipotlane"), `10-K-FY2024` l.783 (304) and l.763 (257 Chipotlanes), `10-K-FY2025` l.775 (334) and l.757 (257 Chipotlanes), `10-Q` l.945 (149) and l.933 (Q2: 80 Chipotlanes), `press-release-2026-Q1.txt` l.34 (Q1: 42 Chipotlanes); partner units `10-K-FY2024` l.801–805 (beginning "- | -", 3 at end-2024), `10-K-FY2025` l.793 (14), `10-Q` l.963 (15).

| Row | Result |
|---|---|
| Comparable restaurant sales 19.3 / 8.0 / 7.9 / 7.4 / (1.7) / 1.4% | PASS ×6 |
| Transactions not disclosed / 0.9 / 5.0 / 5.3 / (2.9) / 0.8% | PASS ×5; FY2021 "not disclosed" PASS (the FY2022 10-K revenue table l.738–748 has no transactions row and l.690 gives no number) |
| Average check not disclosed / 7.1 / 2.9 / 2.1 / 1.2 / 0.6% | PASS ×6 (same FY2021 check) |
| Menu price not disclosed / 12.0 / 5.2 / 2.9 / 2.1 / 1.3% | PASS ×6 |
| AUV 2.6 / 2.8 / 3.018 / 3.213 / 3.104 / 3.102 | PASS ×6; footnote l.45 ($3.0 in the FY2023 10-K vs $3.018 in the FY2024 10-K) PASS |
| Company-owned restaurants 2,966 / 3,187 / 3,437 / 3,726 / 4,042 / 4,186 | PASS ×6 |
| Openings 215 / 236 / 271 / 304 / 334 / 149 | PASS ×6 (236 = 235 + 1 Pizzeria Locale, 271 = 270 + 1, both as the 10-K text states; footnote l.45 on Pizzeria Locale PASS: `10-K-FY2022` l.718, `10-K-FY2023` l.962 "closing all Pizzeria Locale restaurants") |
| Chipotlanes not disclosed / 202 / 238 / 257 / 257 / 122 | PASS ×4 stated. 122 is not printed anywhere in the 10-Q (`grep -n -F "122"` hits only a cash line, l.455); it is Q1 42 + Q2 80, so "(computed)" and the Q1 release tag added (direct fix 6). **FY2021 "not disclosed" FAIL**: `slides-2025-Q4.txt` l.359 (p.14, "Global Chipotlanes" chart) prints yearly Chipotlane openings "+56 +100 +174 +202 +238 +257 +258" for 2019–2025, so 2021 = 174; the 2022–2024 values agree with the 10-Ks and the deck's 2025 value (258) includes one partner-operated Chipotlane (footnote l.362) |
| Partner-operated 0 / 0 / 0 / 3 / 14 / 15 | PASS ×6 |

53/54 PASS, 1 FAIL (REVISE item 4), 1 label added.

### 3(c) business.md §3 table (l.53–65), every cell

Inputs: cost percentages `10-K-FY2022.txt` l.762 / 780 / 794 / 808 ("30.1% | 30.6%", "25.5% | 25.4%", "5.3% | 5.5%", "15.2% | 15.9%"), l.822 (G&A "6.5% | 8.0%"), l.840 (D&A "3.3% | 3.4%"); `10-K-FY2023` l.844 / 862 / 878 / 892 (29.5 / 24.7 / 5.1 / 14.5), l.906 (6.4), l.946 (3.2); `10-K-FY2024` l.873 / 887 / 901 / 919 (29.8 / 24.7 / 5.0 / 13.9), l.933 (6.2); `10-K-FY2025` l.865 / 881 / 899 / 913 (29.6 / 25.1 / 5.2 / 14.7), l.927 (5.5), l.973 (3.0 / 3.0); `10-Q` l.1033 / 1053 / 1069 / 1083 (six-month columns 29.6 / 25.5 / 5.3 / 15.2), l.1103 (6.1). Stated margins `DEF14A-2026.txt` l.2720–2760 (Appendix A: income from operations 1,935,798 = 16.2% and 1,916,333 = 16.9%; restaurant level operating margin 3,026,207 = 25.4% and 3,017,692 = 26.7%). Income from operations `10-K-FY2023` l.1303 (1,557,813 / 1,160,403 / 804,943), `10-Q` l.269 (922,658). Capex `10-K-FY2023` l.1449 (560,731 / 479,164 / 442,475), `10-K-FY2025` l.1437 (666,336 / 593,603), `10-Q` l.435 (397,601).

| Row | Re-derived | Result |
|---|---|---|
| Revenue | as 3(a) | PASS ×6 |
| Food, beverage and packaging 30.6 / 30.1 / 29.5 / 29.8 / 29.6 / 29.6 | stated | PASS ×6 |
| Labor 25.4 / 25.5 / 24.7 / 24.7 / 25.1 / 25.5 | stated | PASS ×6 |
| Occupancy 5.5 / 5.3 / 5.1 / 5.0 / 5.2 / 5.3 | stated | PASS ×6 |
| Other operating costs 15.9 / 15.2 / 14.5 / 13.9 / 14.7 / 15.2 | stated | PASS ×6 |
| Restaurant-level operating margin 22.6 (c) / 23.9 (c) / 26.2 (c) / 26.7 / 25.4 / 24.3 (c) | 100 − 77.4 = 22.6 and 100 − 76.1 = 23.9 (the FY2022 10-K itself states restaurant operating costs at 77.4% and 76.1%, l.696); 100 − 73.8 = 26.2 (`10-K-FY2023` l.750 states 73.8%); H1 from the 10-Q statement: 6,436,804 − 1,906,919 − 1,641,861 − 344,091 − 980,407 = 1,563,526 = 24.29% | PASS ×6 |
| General and administrative 8.0 / 6.5 / 6.4 / 6.2 / 5.5 / 6.1 | stated | PASS ×6 |
| Depreciation and amortization 3.4 / 3.3 / 3.2 / 3.0 / 3.0 / 3.0 | stated; H1 195,045 / 6,436,804 = 3.03% (the release prints 3.0, `press-release.txt` l.188) | PASS ×6 |
| Operating margin 10.7 (c) / 13.4 (c) / 15.8 (c) / 16.9 / 16.2 / 14.3 (c) | 804,943 / 7,547,061 = 10.67; 1,160,403 / 8,634,652 = 13.44; 1,557,813 / 9,871,649 = 15.78; 922,658 / 6,436,804 = 14.33 | PASS ×6 |
| Capex 442.5 / 479.2 / 560.7 / 593.6 / 666.3 / 397.6 | stated | PASS ×6 |
| Capex / revenue 5.9 / 5.5 / 5.7 / 5.2 / 5.6 / 6.2% | 5.86 / 5.55 / 5.68 / 5.25 / 5.59 / 6.18 | PASS ×6 |

66/66 PASS. Footnote l.67 (Q1 adjusted 23.7% vs 23.3%, $11.9 million legal accrual in labor; Q2 $10.0 million legal reserve in G&A): `press-release-2026-Q1.txt` l.556–560 (718,961 = 23.3%; legal proceedings-labor 11,875; adjusted 730,836 = 23.7%), `press-release.txt` l.480 and l.534 ("Legal proceedings-General and administrative | 10,000"). PASS.

### 3(d) business.md §4 table (l.73–83), every cell

Inputs: OCF `10-K-FY2023` l.1445 (1,783,477 / 1,323,179 / 1,282,081), `10-K-FY2025` l.1433 (2,113,926 / 2,105,076), `10-Q` l.431 (1,332,003); net income `10-K-FY2023` l.1311 (1,228,737 / 899,101 / 652,984), `10-K-FY2025` l.1297 (1,535,761 / 1,534,110), `10-Q` l.275 (706,371); diluted EPS `10-K-FY2023` l.1317 (pre-split 44.34 / 32.04 / 22.90), `10-K-FY2024` l.1305 (1.11 / 0.89 / 0.64), `10-K-FY2025` l.1303 (1.14 / 1.11 / 0.89), `10-Q` l.283 (0.55); repurchases `10-K-FY2023` l.1461 ("Acquisition of treasury stock" 592,349 / 830,140 / 466,462), `10-K-FY2025` l.1449 ("Repurchase of common stock" 2,425,516 / 1,001,559), `10-Q` l.445 (1,354,905); balance sheets `10-K-FY2022` l.1069–1090 (cash 384,000 / 815,374; investments 515,136 / 260,945; long-term investments 388,055 / 274,311), `10-K-FY2023` l.1187–1210 (560,609; 734,838; 564,488), `10-K-FY2025` l.1177–1200 (350,545 / 748,537; 698,591 / 674,378; 197,123 / 868,025), `10-Q` l.157, 167, 173 (228,199; 449,658; 97,079); debt `10-K-FY2025` l.2427 and `10-Q` l.831 ("We had no outstanding borrowings under the credit facility").

| Row | Re-derived | Result |
|---|---|---|
| Operating cash flow 1,282.1 / 1,323.2 / 1,783.5 / 2,105.1 / 2,113.9 / 1,332.0 | stated | PASS ×6 |
| Capex | as 3(c) | PASS ×6 |
| OCF less capex 839.6 / 844.0 / 1,222.7 / 1,511.5 / 1,447.6 / 934.4 (computed) | 839.606 / 844.015 / 1,222.746 / 1,511.473 / 1,447.590 / 934.402 | PASS ×6 |
| Net income 653.0 / 899.1 / 1,228.7 / 1,534.1 / 1,535.8 / 706.4 | stated | PASS ×6 |
| OCF less capex, % of net income 129 / 94 / 100 / 99 / 94 / 132 (computed) | 128.6 / 93.9 / 99.5 / 98.5 / 94.3 / 132.3 | PASS ×6 |
| Diluted EPS 0.46 (computed) / 0.64 / 0.89 / 1.11 / 1.14 / 0.55 | 22.90 / 50 = 0.458; the rest stated post-split | PASS ×6 |
| Cash spent on repurchases 466.5 / 830.1 / 592.3 / 1,001.6 / 2,425.5 / 1,354.9 | stated (cash-flow line) | PASS ×6 |
| Cash and investments 1,350.6 / 1,287.2 / 1,859.9 / 2,290.9 / 1,246.3 / 774.9 (computed) | 815,374 + 260,945 + 274,311 = 1,350,630; 384,000 + 515,136 + 388,055 = 1,287,191; 560,609 + 734,838 + 564,488 = 1,859,935; 748,537 + 674,378 + 868,025 = 2,290,940; 350,545 + 698,591 + 197,123 = 1,246,259; 228,199 + 449,658 + 97,079 = 774,936 | PASS ×6 |
| Debt none ×6 | Note 12 in both filings: $500,000 facility, no borrowings | PASS ×6 |

54/54 PASS.

### 3(e) business.md §7 capital-return table (l.127–134), every cell

Inputs: `10-K-FY2025.txt` l.2145 ("we repurchased $2,417,673, $995,765, and $589,840 of stock at an average price per share of $42.54, $57.21, and $36.55 ... we had $1,710,669 authorized"); `10-Q` l.653 ("$1,331,572 ... at an average price of $34.35 ... $1,679,097 authorized"); equity statements `10-K-FY2024` l.1335 (Dec 31, 2021: 1,856,597 issued, 452,622 treasury), l.1347 (2022: 1,865,992 / 484,651), `10-K-FY2025` l.1345 (2023: 1,874,139 / 502,843), l.1359 (2024: 1,358,751, no treasury), l.1371 (2025: 1,304,360), `10-Q` l.367 (1,267,838); retained earnings `10-K-FY2022` l.1137 (4,828,248 / 3,929,147), `10-K-FY2023` l.1255 (6,056,985), `10-K-FY2025` l.1241 (619,908 / 1,574,232), `10-Q` l.221 ((67,164)); authorizations `10-K-FY2022` l.1959 ($413,947), `10-K-FY2023` l.2105 ($424,107), `10-K-FY2024` l.2089 ($1,028,342); dividends `10-K-FY2025` l.695.

| Row | Result |
|---|---|
| Program repurchases not disclosed / not disclosed / 589.8 / 995.8 / 2,417.7 / 1,331.6 | PASS ×4 stated. FY2021 and FY2022 "not disclosed" PASS: the FY2022, FY2023 and FY2024 Note 7 texts (l.1959, l.2105, l.2089, printed in full) carry only the authorization sentence; the annual dollar-and-price sentence first appears in the FY2025 10-K and covers 2023–2025 |
| Average price not disclosed / not disclosed / 36.55 / 57.21 / 42.54 / 34.35 | PASS ×6 (same reasoning) |
| Shares outstanding 1,404.0 (c) / 1,381.3 (c) / 1,371.3 (c) / 1,358.8 / 1,304.4 / 1,267.8 | 1,856,597 − 452,622 = 1,403,975; 1,865,992 − 484,651 = 1,381,341; 1,874,139 − 502,843 = 1,371,296; rest stated | PASS ×6 |
| Retained earnings 3,929.1 / 4,828.2 / 6,057.0 / 1,574.2 / 619.9 / (67.2) | PASS ×6; footnote l.136 "$5,189.1 million charge for retiring treasury stock": `10-K-FY2024` l.2091 "$5,189,124 in retained earnings" PASS |
| Remaining authorization not disclosed / 413.9 / 424.1 / 1,028.3 / 1,710.7 / 1,679.1 | PASS ×5 stated; FY2021 "not disclosed" PASS (the FY2022 10-K gives the December 31, 2022 figure only, l.1959; its Item 5 table covers Q4 2022 month-ends) |
| Dividends none ×6 | l.695 "have not declared or paid any cash dividends" | PASS ×6 |

36/36 PASS.

### 3(f) outlook.md §1 indicator table (l.10–16), every value

| Row | Source | Result |
|---|---|---|
| 1. Comps Q2 2.2%; +1.0 / +1.2 — Q1 0.5%; +0.6 / (0.1) — "Full year comparable restaurant sales to be about flat" | `press-release.txt` l.38; `press-release-2026-Q1.txt` l.40; Q1 Outlook l.64 | PASS ×7 |
| 2. RLOM Q2 25.2% unadjusted; 29.7 / 25.0 / 5.2 / 14.9 — Q1 23.3%, 23.7% adjusted, $11.9 million; 29.6 / 26.1 / 5.5 / 15.6 — no guidance | `press-release.txt` l.596 (844,565 = 25.2%), l.118–124; Q1 l.556–560, l.412 (11,875), l.120–126; neither Outlook mentions margins | PASS ×12 |
| 3. Openings Q2 100 (80); 4,186 / 15 — Q1 49 (42); 4,090 / 14 — openings bullet | `press-release.txt` l.32, l.416, l.430; Q1 l.34, l.356, l.370; Q1 Outlook l.66 | PASS ×9 |
| 4. AUV 3,102 — 3,094 | `press-release.txt` l.418; Q1 l.358 | PASS ×3 (no guidance: Outlook sections silent) |
| 5. Digital 38.3% — 38.6% | `press-release.txt` l.38; Q1 l.40 | PASS ×3 |
| 6. Operating margin 15.7%; G&A 5.7% ($176.2) — 12.9%; 6.6% ($197.9) — tax-rate bullet | `press-release.txt` l.24, l.126, l.540 (176,200); Q1 l.26, l.128, l.500 (197,948); Q1 Outlook l.68 | PASS ×7 |
| 7. Buybacks $630.7M ($32.55; $1.7B); 1,267.8M shares; $774.9M (c) — $700.8M ($36.14; $1.0B); 1,287.1M shares; $967.8M (c) | `press-release.txt` l.54, l.288, l.232 + 242 + 248 (774,936); Q1 l.56, l.230 (1,287,050), l.174 + 184 + 190 (246,636 + 624,786 + 96,397 = 967,819) | PASS ×11 |

52/52 PASS. Header note l.6 (Q1 Outlook full-year only) PASS: Q1 Outlook l.62–68 has three full-year bullets and nothing on Q2.

### 3(g) Verbatim quotes (programmatic sweep, curly quotes, dashes and whitespace normalised)

`quotes.py`: every double-quoted string of 12 or more characters, paired by quote order (53 in business.md, 82 in outlook.md after the fixes), tested as a substring of any line of the normalised cached texts. Result: every substantive quotation found. The six "misses" are not source quotations: `"Q4/FY 2025 Investor Information"` and `"Non-GAAP tables for IR Site Q226"` (document titles in the Sources lists, taken from MANIFEST; the deck footer prints with spaced letters), `"what management had said"` (the outlook's own column name), `"all other revenue"` and `"average restaurant economic model"` (the source prints "All other revenue" and "AVERAGE RESTAURANT ECONOMIC MODEL", case only), and the 10-Q sentence quoted with an ellipsis, whose two halves are both at `10-Q` l.931. Hand-checked lines behind the sweep:

| Quote (start) | Tag | Found | Result |
|---|---|---|---|
| "real food with wholesome ingredients and without artificial colors, flavors or preservatives" | 10-K FY2025 Item 1 (General) | `10-K-FY2025` l.201 | PASS |
| "Our revenue is derived from sales by our restaurants" | 10-K FY2025 Item 1 | l.203 | PASS |
| "we own all of our restaurants (except the franchised restaurants in the Middle East)" | DEF 14A CEO Pay Ratio | `DEF14A` l.2546 | PASS |
| "among Chipotle Mexican Grill, Inc., McDonald's Corporation and certain shareholders" | 10-K FY2025 Item 15 | l.2691 (January 31, 2006 agreement) | PASS |
| "had a significant negative impact on our sales and profitability" | 10-K FY2022 Item 1A | `10-K-FY2022` l.364 (2015 to 2018) | PASS |
| "lower sales volumes"; "sales leverage" | 10-K FY2025 Labor Costs; added 10-K FY2023 | `10-K-FY2025` l.883; `10-K-FY2023` l.750 and `10-K-FY2022` l.696 | PASS ×2 (tag added) |
| "about $1.5 million in development and construction costs"; "about $1.3 million net of landlord reimbursements"; "around 36 months to ramp up the sales and profitability"; "about $834.1 million in total capital expenditures"; "approximately $531.8 million"; "approximately $266.9 million"; "generally within ten days" | 10-K FY2025 Use of Cash; Item 1A | l.1035; l.511; l.1033 | PASS ×7 |
| "Responsibly Raised"; "a limited list of approved suppliers" | 10-K FY2025 Item 1 | l.221/343; l.251 | PASS ×2 |
| "generous portions, speed and an accessible price point"; "23 million active members" | call l.36; l.35 | exact | PASS ×2 |
| "may have higher risk for food safety incidents than some of our competitors" | 10-K FY2025 Item 1A | l.367 | PASS |
| "a softening, call it about 200 basis points or so right around the issue that's affecting the industry around cyclospora"; "we are impacted from a sales perspective, but we're not involved" | call l.79; l.84 | exact | PASS ×2 |
| "nearly 20%"; "about 15 basis points on an ongoing basis" | 10-K FY2023 Labor Costs; 10-K FY2025 Food costs | `10-K-FY2023` l.866; `10-K-FY2025` l.869 | PASS ×2 |
| "guest perceptions regarding smaller entrée portion sizes"; "under the most pressure" | 10-K FY2025 Item 1A; call l.136 | l.371; exact | PASS ×2 |
| "approximately 100 basis points" | call l.52 | exact | PASS |
| "restaurant formats that claim to serve higher quality ingredients without artificial flavors, colors and preservatives"; "competitor discounting" | 10-K FY2025 Competition; 10-Q Part II Item 1A | l.335; `10-Q` l.1277 | PASS ×2 |
| "may be less than the actual delivery cost"; "Many of these critical systems are provided and managed by third parties" | 10-K FY2025 Item 1A | l.387; l.421 | PASS ×2 |
| "Changes in senior management could result in significant changes in strategic direction and initiatives" | 10-K FY2025 Item 1A | l.415 | PASS |
| "Certain key ingredients are purchased from a small number of suppliers"; "a limited number of suppliers for some of our ingredients, including lemon and lime juice, tomatoes and adobo" | 10-K FY2025 Purchasing; Item 1A | l.225; l.461 | PASS ×2 |
| "limit the use of one-time awards to extraordinary circumstances" | DEF 14A Committee letter | `DEF14A` l.1358 | PASS |
| "low to mid-single digit" | 10-K FY2024 Sales Trends | `10-K-FY2024` l.761 | PASS |
| "subject to market conditions" | 10-Q Item 2 (Cash and Investments) | `10-Q` l.1211 | PASS |
| Outlook §2: pillars (l.25), "that starts with running great restaurants..." (l.26), value (l.68), "building Chipotle into an iconic global brand" (l.47), "at least 7,000 restaurants" (l.52), "7,000 restaurants in the U.S. and Canada" (`10-K-FY2025` l.523), "$4+ MILLION AUVs" / "7,000+ N.A. RESTAURANTS" / "APPROACHING 30%" (`slides-2025-Q4` l.195, l.201, p.7), "8-10% per year" (l.255, p.9), headline (`press-release` l.12), "trends have been softer in recent weeks" (l.50), "toughest lap that we have this year" (l.79), 10-Q sentence (`10-Q` l.931), "not involved in the cyclospora conversation today" (l.84) | as tagged | all exact | PASS ×15 |
| Outlook §3: "approximately 350 restaurants this year with about 80%, including a Chipotlane" (l.43); "New restaurant productivity ... around 60%" (l.52); HEEP "more than 1,000 ... approximately 2,000" (l.28), "sometime in 2027" (l.101), "hundreds of basis points" (l.28 and `slides.txt` l.165–176, p.6); "attachment rate over 25%" (`slides.txt` p.7); "2 additional limited time protein options" (l.38); "only about 20% ... nearly 90%" (l.33); "frictionless in-restaurant Rewards experience beginning in August" (l.34); "represent 2% to 3% of sales today", "a national launch in 2027" (l.40); pricing (l.51, l.143, l.144); Seoul/Singapore (l.45); "high single-digit comp sales growth" (l.44); "rest of the world as partner operated" (l.91) | as tagged | all exact | PASS ×18 |
| Outlook §4 written outlook, nine cells | Q4 2025 release l.120–124; Q1 release l.64–68; Q2 release l.62–66 | exact, "same wording" cells verified identical | PASS ×9 |
| Outlook §4 spoken table, thirteen rows | call l.80, 116, 118, 51, 55, 56, 57, 58, 59, 43, 28, 101, 34, 40, 45 | exact | PASS ×13 |
| Claims 1–12 quotes | call l.80, release l.62, call l.51, l.55, l.56, l.57, l.58, l.28, l.34, l.43, Mexico release, call l.45 | exact | PASS ×12 |

Garbled transcript lines flagged by the gatherer (l.27, l.100, l.122, l.152): none is quoted in either draft (`grep -o "l\.(122|100|27)\b"` returns nothing); the one tag to l.152 (business.md l.103) pointed at the wrong line for the word "rolling", which is at l.143, and was corrected (direct fix 14).

### 3(h) Tagged prose sentences, business.md and outlook.md (52 checked)

| # | Sentence / figure | Tag | Found | Result |
|---|---|---|---|---|
| 1 | 4,186 restaurants, 4,074 U.S. and 112 in Canada, U.K., France, Germany | 10-Q Note 1; Mexico release | `10-Q` l.489 and l.901; `mexico` l.23 (80+ Canada, 20 U.K., six France, two Germany) | PASS |
| 2 | $11.9 billion in 2025; about $3.1 million per restaurant | 10-K FY2025 Item 8; Q2 release Supplemental | l.1267; `press-release` l.418 (3,102) | PASS ×2 |
| 3 | Two revenue lines, no royalty or rent line; four restaurant cost lines named | 10-K FY2025 Item 8 | l.1263–1281 | PASS |
| 4 | About $1.5 million per new restaurant; 125,408 U.S. restaurant employees | Use of Cash; Human Capital | l.1035; l.259 ("125,408 employees worked in our restaurants") | PASS ×2 |
| 5 | 15 partner-operated in the Middle East run by Alshaya; royalties inside "all other revenue" and not split out; Mexico opened July 16, 2026 with Alsea | 10-Q Note 1; Note 14; Mexico release; call l.44 | `10-Q` l.489; `10-K-FY2025` l.2499; `mexico` l.7, l.17 (Alshaya 15 across UAE, Kuwait, Qatar); `transcript` l.44 | PASS ×4; but "Alsea ... never in a filing" FAILS: `DEF14A` l.73 names Alsea (REVISE item 2) |
| 6 | "licensed" renamed "partner-operated" with JV definition | 10-K FY2025 Item 1; 10-K FY2024 Item 7 (Licensing) | `10-K-FY2025` l.203; `10-K-FY2024` l.765 ("Licensing. ... three licensed restaurants") | PASS |
| 7 | Denver 1993; deck timeline 1998 outside investment and 2006 NYSE | 10-K FY2025 Item 1; Q2 slides p.4 | l.201; `slides.txt` l.76, l.108, l.94 | PASS ×3 |
| 8 | Registration-rights agreement January 2006 with McDonald's; proxy on the 2006 IPO | 10-K FY2025 Item 15; DEF 14A Certain Relationships | l.2691; `DEF14A` l.2654–2658 ("Prior to our initial public offering in 2006 ... registration rights agreement") | PASS ×2; the McDonald's-as-1998-investor reading is labelled "our inference" |
| 9 | April 2020 DPA; fine amount not stated; three-year term | 10-K FY2022 Item 1A | l.470 ("Chipotle paid a fine"; term "ends in April 2023") | PASS (wording tightened, direct fix 3) |
| 10 | Niccol left August 31, 2024 for Starbucks; Boatwright interim CEO "that day" | 8-K 2024-08-13 | l.59 (notice August 12, leaving August 31), l.61 (interim CEO "effective immediately"), l.115 (Starbucks) | **FAIL on "that day"**: effective August 12, as §7 l.119 says (REVISE item 1) |
| 11 | Boatwright CEO November 2024; "Recipe for Growth" launched with February 2026 results after a year of falling transactions | 8-K 2024-11-12; Q4 2025 release Headline; 10-K FY2025 | `8-K-2024-11-12` l.59 (November 11, 2024); `press-release-2025-Q4` l.18; transactions (2.9%) l.817 | PASS ×3 |
| 12 | 99.5% food and drink; U.S. 98% of revenue | 10-Q Item 1; Note 14 | 6,405.5 / 6,436.8 = 99.5; 11,679.4 / 11,925.6 = 97.9 | PASS ×2 ("(computed)" added, direct fix 4) |
| 13 | Delivery fee definition; courier keeps the fee on its own app; "third-party service providers" | 10-K FY2025 Note 1 (Delivery) | l.1623 and l.1627 ("Marketplace Sales, we generally recognize revenue, excluding delivery fees collected by the delivery partner") | PASS |
| 14 | Comps definition (13 months); transactions and average check (menu price plus mix) | 10-K FY2025 Sales Trends; revenue table | l.755; l.817–823 | PASS |
| 15 | 2025 bridge: revenue +$612M; openings +$809M; comps −$191M | 10-K FY2025 Item 7 (summary of the change in restaurant sales) | l.835–847: (191.3), 327.0 + 481.8 = 808.8; 11,925.6 − 11,313.9 = 611.7 | PASS ×3 |
| 16 | Quarterly comps between (4.0%) and 2.2% since the start of 2025 | Q2 release Supplemental; Q1 release added | `press-release` l.420 (2.2 / 0.5 / (2.5) / 0.3 / (4.0)); `press-release-2026-Q1` l.360 adds Q1 2025 (0.4) | PASS (tag added, direct fix 5) |
| 17 | RLOM definition and the $100 walk (29.60 / 25.10 / 5.20 / 14.70 → 25.40; 5.50 / 3.00 / 0.40 / 0.20 → 16.2%); other operating costs include marketing, delivery, card fees, utilities | Q2 release Non-GAAP definitions; DEF 14A Appendix A; 10-K FY2025 Note 1 | `press-release` l.225 area; `DEF14A` Appendix A (5.5 / 3.0 / 0.4 / 0.2 / 25.4 / 16.2); `10-K-FY2025` l.1655 | PASS ×10 |
| 18 | Food cost 29.5–30.6% over five years; drivers beef, avocado, dairy, tariffs, portions | 10-K FY2025 and FY2024 Food costs | table; `10-K-FY2025` l.867, l.869; `10-K-FY2024` l.875 ("generous portions ... primarily avocados") | PASS |
| 19 | 2025 labor +0.4 points, 0.7 from lower volumes; G&A 8.0% (2021) to 5.5% (2025) | 10-K FY2025 Labor Costs; G&A | l.883; `10-K-FY2022` l.822, `10-K-FY2025` l.927 | PASS ×3 |
| 20 | Pricing "more in that 1% range" vs inflation "in that low to mid-3%" in H1 2026 | call l.143 | exact | PASS (spoken, quoted) |
| 21 | Owns 17 properties; $5.1 billion lease obligations | Item 2; Note 9 | l.653; l.2357 ("Operating lease liabilities (Current and Long-Term) | $ | 5,075,814") | PASS ×2 |
| 22 | Two-thirds of 2026 capex buys growth | Use of Cash | 531.8 / 834.1 = 64% | PASS (inference from stated figures) |
| 23 | OCF less capex near net income; cash and investments from $2.3B to $0.8B | 10-K FY2025; 10-Q | table 3(d); 2,290.9 → 774.9 | PASS; "Since 2024" tightened to "Since the end of 2024" (2024 buybacks 1,001.6 were below OCF less capex 1,511.5; 2025 and H1 2026 exceed it), direct fix 10 |
| 24 | Return on capital: 1,935.8 / 2,679.4 = 0.72; with 4,463.0 lease assets 0.27 | 10-K FY2025 balance sheet and income statement | l.1289 (1,935,798); balance sheet 2,679,361 and 4,463,010 (`press-release` l.244–250 comparative column agrees) | PASS ×2 |
| 25 | Deck model: $3.1M sales, $787k restaurant cash flow, about 60% of $1.3M | Q4 2025 slides p.13; Use of Cash | `slides-2025-Q4` l.306–322 ($787k, 25.4%); 787 / 1,300 = 60.5% | PASS |
| 26 | 26 regional distribution centers (2024 count) | 10-K FY2024 Purchasing | l.225 ("26 independently owned and operated regional distribution centers"; FY2025 l.225 says "multiple") | PASS |
| 27 | 38% digital; 1,326 Chipotlanes at end-2025; June 2026 total not disclosed | Q2 release; Q4 2025 slides p.14 | l.38; `slides-2025-Q4` l.346 (1,326*, footnote l.362: includes one partner-operated); no Chipotlane total in `press-release.txt`, `slides.txt` or the 10-Q | PASS ×3 |
| 28 | Rewards relaunched April 2026; $80.6 million unredeemed points at June 30, 2026 | call l.32; 10-Q Note 3 | l.32 ("relaunched in mid-April"); `10-Q` l.539 ("Chipotle Rewards liability, ending balance | $ | 80,578") | PASS ×2 |
| 29 | Digital share fell 45.0% (2021) to 35.1% (2024); RLOM below prior year in 2025 and both 2026 quarters | 10-K FY2022/FY2024; DEF 14A Appendix A; Q2 release | l.694; l.255; Appendix A; `press-release` l.26, Q1 l.28 | PASS |
| 30 | Food and labor 54.7% of revenue; one point about $119 million | 10-K FY2025 Item 7 | 29.6 + 25.1; 11,925.6 × 1% = 119.3 | PASS ×2 (labelled computed) |
| 31 | California $20 minimum wage from April 2024, "nearly 20%"; tariffs 15 bps | 10-K FY2023 Labor Costs; 10-K FY2025 | `10-K-FY2023` l.866; `10-K-FY2025` l.869 | PASS ×2 |
| 32 | Stradford class action on portion sizes | 10-Q Note 11 (Shareholder Actions) | l.803 (Note 11), l.817 (heading), l.819 | PASS |
| 33 | AUV $3.213M (end-2024) to $3.102M (June 2026); count +12% | Q2 release Supplemental; 10-K FY2024 | 4,186 / 3,726 = 1.123 | PASS |
| 34 | Build cost about $1.2M in 2022 to $1.5M in 2025 | 10-K FY2022 Liquidity and Capital Resources; 10-K FY2025 Use of Cash | `10-K-FY2022` l.902 (heading at l.899); `10-K-FY2025` l.1035 | PASS ×2 |
| 35 | Impairment $13.8M in Q2 2026 vs $5.5M; about $530M growth capex | 10-Q Item 1; Use of Cash | `10-Q` l.265 (13,808 / 5,467); l.1035 (531.8) | PASS ×2 |
| 36 | Marketing +0.5 points in 2025 | 10-K FY2025 Other Operating Costs | l.915 | PASS |
| 37 | Over 16% delivery; delivery slice about $1.9B; "delivery expense" named in Q1 2026 | 10-K FY2025 Item 1A; 10-Q Q1 Item 2 | l.387; 0.16 × 11,866 = 1,899; `10-Q-2026-Q1` l.1023 | PASS ×3 |
| 38 | CEO, CFO, COO, brand, legal and accounting officers all changed since August 2024 | 8-Ks | 2024-08-13 (CEO), 2024-07-09 / 2024-08-28 (CFO and CAO from October 1, 2024), 2025-05-07 (COO), 2026-01-12 (brand, legal) | PASS |
| 39 | No customer 10%; supplier concentration quotes | 10-K FY2025 Note 14; Purchasing; Item 1A | l.2443; l.225; l.461 | PASS ×3 |
| 40 | Boatwright 53, joined 2017, 18 years at Arby's, interim CEO August 12, 2024, CEO and director November 11, 2024 | DEF 14A; 8-Ks | `DEF14A` l.654; `8-K-2024-08-13` l.61; `8-K-2024-11-12` l.59 | PASS ×5 ("joined in 2017 as Chief Operating Officer" tightened to what the filings state, direct fix 16: the proxy says he "served as Chief Operating Officer and Chief Restaurant Officer prior to his current role" and the August 2024 8-K that he "currently serves as Chipotle's Chief Operating Officer") |
| 41 | Hartung CFO since 2002, retirement announced July 2024, retired March 2026; Rymer 44, since 2009, CFO October 1, 2024 | 8-Ks 2024-07-09, 2024-08-28, 2025-05-07; DEF 14A | `8-K-2024-07-09` l.59 ("since 2002", notified July 8, 2024); `8-K-2024-08-28` l.59 (advanced to October 1, 2024); `8-K-2025-05-07` l.67 ("through early March 2026, when he will retire"); `DEF14A` l.1396 ("until his retirement in March 2026"), l.1296 (Rymer, 44, "joined Chipotle in 2009" per 8-K l.61) | PASS ×6 |
| 42 | Kidd COO May 2025 from Taco Bell; Brandt and Theodoredis out January 2026 with severance; Machado (ex-RBI) June 2026; Sisson (ex-Hyatt) May 2026 | 8-Ks 2025-05-07, 2026-01-12, 2026-04-27 | l.59 (effective May 19, 2025; Taco Bell); `8-K-2026-01-12` l.59–63 (effective January 12, 2026; Executive Officer Severance Plan); `8-K-2026-04-27` l.59 (June 1, 2026), l.61 (May 4, 2026), l.109 (RBI), l.117 (Hyatt) | PASS ×6 |
| 43 | Maw, former Starbucks CFO, independent Chairman when Niccol left; nine of ten directors independent | DEF 14A Board Leadership; Independence; 8-K 2024-08-13 | `DEF14A` l.678, l.916–918; l.225; `8-K` l.65 | PASS ×3 |
| 44 | Retention awards $8M / $8M / $7M / $7M / $3M / $1.5M | 8-K 2024-08-28 | l.61–63 | PASS ×6 ("Right after Niccol's departure" → "was announced": grants dated August 22, 2024, before the August 31 departure; direct fix 17) |
| 45 | 55% say-on-pay 2025 (55.4% of for-plus-against); committee pledge; none granted in 2025; 95.3% in 2026 | 8-K 2025-06-13; DEF 14A l.1358; 8-K 2026-06-17 | 603,124,052 / (603,124,052 + 484,840,689) = 55.44%; l.1358; 973,639,399 / (973,639,399 + 47,598,354) = 95.34% | PASS ×4 |
| 46 | Bonus 75% company (40 comps / 40 RCF margin / 20 site pipeline), food-safety modifier up to −20%, 2025 CPF 40% with comps and margin below threshold; PSUs 90% RCF dollars / 10% openings | DEF 14A CD&A | l.1670 (CPF 75%, IPF 25%), l.1686 (40 / 40 / 20 "Site Assessment Requests"), l.1672 ("as much as -20%"), l.1728–1738 (CRS (1.7)% and RCF margin 25.62% below threshold, "overall CPF of 40%"), l.1888 (90% / 10%) | PASS ×7 |
| 47 | Boatwright 2025 total $15.5M; 886×; median $17,446 part-time crew | DEF 14A Pay Ratio | l.2546 ("$15.46 million", "886 to 1"), l.2544 ("hourly part-time employee ... roughly 24 hours per week ... in Texas") | PASS ×3 |
| 48 | D&O 0.45%; Vanguard 11.25%; Capital World 7.92% | DEF 14A Beneficial Ownership | l.604; l.568; l.570 | PASS ×3 |
| 49 | Comps 2025 vs "low to mid-single digit" guidance; openings inside guided ranges (271 in 255–285, 304 in 285–315, 334 in 315–345); stock $100 → $134 vs S&P $196 | 10-K FY2024 Sales Trends; Restaurant Development sections; 10-K FY2025 Item 5 | `10-K-FY2024` l.761; `10-K-FY2022` l.702, `10-K-FY2023` l.752, `10-K-FY2024` l.763; `10-K-FY2025` l.707–709 | PASS ×5 |
| 50 | Cash order (new restaurants, existing, buybacks "subject to market conditions"); no dividend; $500M revolver to June 2030; $2.4B 2025 and $1.33B H1 at $34.35; accumulated deficit $67.2M, equity $2.2B; $1.8B December 2025, $1.3B June 2026, $1.68B left; split June 26, 2024; venture fund up to $100 million | 10-Q Item 2; 10-K Item 5; 8-K 2025-06-27; Note 7 / Note 6; balance sheet; 8-Ks; 10-K FY2024 | `10-Q` l.1211; `10-K-FY2025` l.695; `8-K-2025-06-27` l.61 ("mature on June 24, 2030"); l.2145 and `10-Q` l.653; `10-Q` l.221, l.223 (2,199,791); `8-K-2025-12-08` l.59; `8-K-2026-07-29` l.59 and `press-release` l.54 (June 11, 2026); `10-K-FY2024` l.1493; `10-K-FY2024` l.767 ("authorized to invest up to $100.0 million") | PASS ×11 (tag on the fund corrected to the "Cultivate Next Fund" heading, direct fix 18) |
| 51 | Outlook §3: 149 openings in H1; working-if "about 200 in H2 (computed)"; Alshaya 15; Monterrey July 16, Mexico City 2027; Seoul this year, Singapore early 2027 | Q2 and Q1 release Headlines; Supplemental; call l.45; Mexico release | 100 + 49; 350 − 149 = 201; `press-release` l.430; `mexico` l.7, l.9; `transcript` l.45 | PASS ×5 |
| 52 | Outlook §4: written outlook raised once; non-GAAP PDF says Q3 forward-looking measures unreconciled; "Not guided anywhere ... capex" | releases; `non-gaap-tables.txt` l.40 ("for our third quarter 2026") | comps: "about flat" → "low single digit"; l.40 exact | PASS ×2; **"capex" FAILS**: `10-K-FY2025` l.1035 guides 2026 capex at about $834.1 million (REVISE item 5) |

Totals across 3(a)–3(h): 310 table cells (3 FAIL, all "not disclosed" cells with a printed source; 1 label added), 135 quoted strings (0 substantive misses), about 90 prose facts in 52 rows (2 FAIL: the August 12 date and "never in a filing"; 4 wording-precision edits made directly). UNVERIFIABLE: 0.

---

## 4. Number-source rule (§3 rule 2)

Every figure whose only support is a call tag, and how it is presented:

| Figure | Where | Status |
|---|---|---|
| "more in that 1% range" pricing vs "low to mid-3%" inflation, H1 2026 | business.md §3 l.51 | Verbatim quotes, call l.143. OK |
| "23 million active members" | §5 l.93 | Quoted, "(spoken; not in a filing)". OK |
| "about 200 basis points" cyclospora softening | §6.1 l.101 | Verbatim CFO quote. OK |
| 1%–2% a year menu-price strategy | §6.2 l.103 | Was a paraphrased number with a call tag only; now 'the CFO says is held to "the 1% to 2% range" a year (spoken)' with the correct line (direct fix 14). OK |
| "approximately 100 basis points" new-unit drag on comps | §6.4 l.107 | Quoted, "(spoken)". OK |
| "at least 7,000 restaurants" | outlook §2 l.20 | "(spoken; the 10-K's goal is ...)" with the 10-K tag alongside. OK |
| "approximately 350 restaurants this year with about 80%"; "80% range"; "around 60%" | outlook §3 l.26 | Verbatim; the unit-economics sentence labelled "spoken only". OK |
| "more than 1,000 restaurants", "approximately 2,000", "sometime in 2027" | outlook §3 l.28 | Verbatim; the 1,000+/~2,000 figures also carry the deck tag (`slides.txt` p.6). OK |
| "2 additional limited time protein options" | l.30 | Verbatim. OK |
| "about 20% ... nearly 90%" scan rates | l.32 | Verbatim, "(spoken)". OK |
| "2% to 3% of sales today" | l.34 | Verbatim, "(spoken)". OK |
| Menu price 1.6% in Q2 | l.36 | Was "about 1.6%" with a call tag only although the 10-Q prints "Menu price increase | 1.6%" (l.995); now tagged to the 10-Q, with the Q3 and full-year figures marked "spoken only" (direct fix, outlook 8). OK |
| "mid-2% range", "high end of the 1% to 2% range", "about 3%", "from Q4 forward" | l.36 | Verbatim, labelled spoken. OK |
| "high single-digit comp sales growth" in Europe | l.38 | Verbatim, "(spoken)". OK |
| Q3 comps "around a plus 1%", "roughly 200 basis point impact", cost of sales "just under 30%", labor "mid-25%", marketing "low 3%", other operating "mid-15%", G&A "around $180 million", D&A "around 3%", tax "24% to 26%" | outlook §4 spoken table l.50–64 | Every cell verbatim under the header "Spoken on the call (wording only; numbers exist only here)"; the tax-rate range is also in the written Outlook, tagged there. OK |
| Claims 1, 3–10, 12 | outlook §5 | Each carries its verbatim quote; sharpenings labelled. OK |

Where a release, deck or filing carries the number (comps, cost lines, margins, openings, Chipotlanes, unit counts, AUV, digital share, G&A, buybacks, the written outlook, HEEP counts on p.6, the Honey Chicken attachment rate on p.7, the 7,000 goal, menu price for Q2), the drafts now tag that source. No violations remain.

---

## 5. Jargon audit

Reader: a smart 16-year-old with no finance background. Terms neither plain, name-inferable nor in the Glossary, and the action taken (all direct fixes):

| Term | Where | Action |
|---|---|---|
| fast-casual | business.md l.6 | "fast-casual (counter-service, made-to-order) restaurants" |
| 10-K; proxy | l.8 | "Its 10-K (annual report)"; "the proxy (its annual shareholder-meeting filing)" |
| registration-rights agreement; IPO | l.12 | "(a contract letting a shareholder sell its stock in a public offering)"; "IPO (initial public offering)" |
| mix | l.31 | "menu price plus mix, meaning what people order" |
| impairment | l.49 (first use) | "impairment (write-downs of restaurants worth less than their cost)" |
| MD&A | l.51 | "the 10-K's management discussion (MD&A)" |
| working capital | l.69 | "(cash tied up in stock and unpaid bills)" |
| restaurant cash flow | l.89 | "(the deck's name for restaurant-level operating profit)" |
| cyclospora; basis points | l.101 (first use) | "(cyclospora is a food-borne parasite; 200 basis points is two percentage points)" |
| class action | l.105 | "(Stradford, a lawsuit brought on behalf of all shareholders)" |
| say-on-pay; performance shares | l.121 | "(the advisory shareholder vote on executive pay; ...)"; "Performance shares (stock that vests only if targets are met)" |
| retained earnings; treasury stock | l.132 (table label), l.136 | "Retained earnings (cumulative profit kept in the business)"; "treasury stock (repurchased shares it had held rather than cancelled)" |
| HEEP | l.152 | "HEEP, the new kitchen equipment package" (outlook §3 l.28 already expands it as "the equipment package (HEEP)") |
| G&A; legal accrual | outlook.md l.15, l.11 (table) | "G&A (head office)"; "legal accrual (money set aside for a case)" |
| throughput; lap; cyclospora | outlook l.20, l.22 | "(throughput: how many orders a line serves in a set time)"; "(the comparison against last year's quarter)"; "(cyclospora is a food-borne parasite behind an industry outbreak)" |
| cash-on-cash returns; basis points; attachment rate | outlook l.26, l.28, l.30 | "(yearly restaurant cash profit as a share of the build cost)"; "(a basis point is a hundredth of a percentage point)"; "(share of orders that included it)" |
| EPS; non-GAAP | outlook l.42, l.56 (table) | "EPS (earnings per share)"; "G&A (non-GAAP: before one-off items)" |

Judged acceptable without change: franchisor and royalties (explained in the same sentence, l.8), comps / restaurant-level operating margin / Chipotlane / AUV / partner-operated (Glossary), G&A in business.md ("the head office", l.49), capex (glossed in the table label, l.64), operating cash flow less capex (plain, no "free cash flow" jargon used), lease assets and lease obligations (explained l.69, l.89), Food with Integrity and Recipe for Growth (explained), Build-Your-Own Chipotle ("a family meal kit"), "sales leverage" and "lower sales volumes" (explained l.51), tariffs and pre-opening costs (name-inferable), Deferred Prosecution Agreement (explained l.12), the 50-for-1 split (name-inferable), "revolving credit line" ("undrawn ... credit line", l.125), "cost of sales" and "underlying effective tax rate ... before discrete items" (verbatim guidance in the spoken table whose row labels are plain), "new restaurant productivity ... 80% range" (a verbatim CFO figure the company does not define in any cached text; left as quoted, see §10 for the owner). Glossary holds five unavoidable terms, one sentence each; nothing else is in it.

---

## 6. Invented-number check

- Every "(computed)" cell in business.md §2, §3, §4, §7 and outlook §1 re-derived from sourced inputs; all correct (details in §3). Two unlabelled computations in prose were labelled: "99.5% of revenue is food and drink" and "The U.S. is 98% of revenue" (both correct). One table cell was a computation presented as a stated figure: H1 2026 Chipotlanes 122 = Q1 42 + Q2 80; now "(computed)" with both release tags.
- Every "not disclosed" cell searched in the filing(s) that should carry it, with full lines printed (§3(a), 3(b), 3(e)). Twelve hold (FY2021 transactions, check, menu price; FY2021 U.S. segment and all other revenue; FY2021 and H1 2026 delivery share; FY2021–FY2022 program repurchases and average prices; FY2021 authorization). Three do not: FY2022 U.S. segment revenue and all other revenue (`10-K-FY2024` l.2409, l.2413) and FY2021 Chipotlane openings (`slides-2025-Q4` l.359). A fourth, FY2021 revenue growth, is not stated anywhere but is computable from the FY2022 10-K's income statement (`10-K-FY2022` l.1163). All in REVISE items 3–4.
- Wrong-period or wrong-basis checks: quarter vs year-to-date (outlook §1 cost lines are the quarter columns of the Statements of Income, l.118–124; business.md H1 column uses the six-month columns, `10-Q` l.1033–1083); adjusted vs unadjusted (Q1 23.3% unadjusted and 23.7% adjusted both shown and explained; Q2 25.2% correctly called unadjusted since the legal reserve sits in G&A); pre-split vs post-split (FY2021 EPS 22.90 / 50 labelled computed; FY2022–FY2023 EPS taken from the post-split FY2024 10-K, not the pre-split FY2023 one; 2021–2023 share counts from the post-split equity statements); thousands vs millions (the Sources notes say statements print thousands and the report converts; every conversion checked). No failure.
- Figures with no tag: none found. Tags that did not support the figure: the "rolling" strategy tag (call l.152 → l.143), the "sales leverage" phrase (FY2025 10-K → FY2023 added), the Cultivate Next fund heading, the Q1 2025 comp behind "since the start of 2025" (Q1 release added), menu price 1.6% (10-Q added). All fixed directly.

---

## 7. Claims check (§9), outlook.md §5, and indicators (§8)

| # | One sentence, one thing | Single direction, can fail | Verbatim quote + tag | Labelling | Gradeable from §5 alone |
|---|---|---|---|---|---|
| 1 | Yes (Q3 comps > 0 and ≤ 2.0%) | Yes | call l.80 | Sharpening labelled "our sharpening ... not management's number" | Yes (Q3 release Results) |
| 2 | Yes (FY comps outlook kept at "low single digit" or raised) | "Reaffirms or raises" form, allowed; fails if cut or dropped | release Outlook l.62 | Management claim | Yes (Q3 release Outlook) |
| 3 | Yes (Q3 average check > 1.2%) | Yes | call l.51 | Sharpening labelled | Yes (Q3 release Results); note for the owner: check includes mix, see §10 |
| 4 | Yes (food costs < 30.0%) | Yes | call l.55 | Management's "just under 30%" | Yes (Q3 Statements of Income) |
| 5 | Yes (labor 25.3–25.7%) | Yes | call l.56 | Sharpening labelled | Yes |
| 6 | Yes (other operating 15.3–15.7%) | Yes | call l.57 | Sharpening labelled | Yes |
| 7 | Yes (adjusted G&A $175–185M) | Yes | call l.58 | Sharpening labelled; names the reconciliation table | Yes |
| 8 | Yes (HEEP ~2,000 by year-end reaffirmed or raised) | Allowed form | call l.28 | Management claim | Yes (Q3 call or deck) |
| 9 | Yes (frictionless Rewards pilot said to be running) | Yes (silence grades 🔇) | call l.34 | Management claim; the mechanism is spelt out | Yes |
| 10 | Yes (9-month company-owned openings ≥ 230) | Yes | call l.43 | Sharpening labelled, with the H1 base (149) stated | Yes (Q3 release Headline / unit table) |
| 11 | Yes (partner-operated count at Sept 30 > 15) | Yes | Mexico release (July 16 opening) | Labelled "Disclosure check, quarter-end count" | Yes (Q3 release unit table) |
| 12 | Yes (Seoul opens before Dec 31, 2026) | Yes; horizon stated, carries forward | call l.45 | Management claim, dated event | Yes |

Count 12 (within 6–12). Headline revenue/EPS: none; two comps claims, four cost-line claims, one G&A, and five on the growth engines (HEEP, Rewards, openings, partners, Korea). No either/or construction; no vague statement passed off as a claim; every quote verified in §3(g).

Indicators: seven in business.md §8, each named with a why and a recurring location, each verified present in both the Q1 and Q2 releases: (1) comps with transactions/check split, Results narrative (`press-release` l.38; Q1 l.40) and 10-Q Sales Trends; (2) restaurant-level operating margin and the four cost lines, reconciliation and Statements of Income (l.596, l.118–124; Q1 l.556–560, l.120–126); (3) openings, Chipotlanes and unit counts, Headline and unit tables (l.32, l.410–430; Q1 l.34, l.350–370) plus 10-Q Note 1; (4) AUV, unit table (l.418; Q1 l.358); (5) digital share, Results (l.38; Q1 l.40); (6) operating margin, G&A and adjusted G&A (l.24, l.126, l.540; Q1 l.26, l.128, l.500); (7) buybacks, shares, cash plus investments (l.54, l.288, l.232–248; Q1 l.56, l.230, l.174–190). None depends on a one-off call number; HEEP, the 350 openings, 7,000 restaurants and the $4 million AUV goal are explicitly parked as claims (l.152). `_Proposed — owner to review and lock._` present (l.140). Outlook §1 has one row per indicator in order, "No guidance" where the Q1 Outlook was silent, and every value verified (§3(f)).

---

## 8. As-of discipline

Every source is dated on or before 2026-07-31 (10-Q filed 2026-07-31; release, 8-K, deck, non-GAAP tables and call 2026-07-29; Mexico release 2026-07-13; Q1 materials 2026-04-28/29; proxy 2026-04-28; Q4 2025 materials 2026-02-03; older 10-Ks and 8-Ks). The transcript was posted 2026-08-07, admitted under §12.2 for call content only, with both dates in MANIFEST and both Sources lists. Future events appear only as plans stated before the cutoff (the August Rewards pilot, Seoul "this year", Monterrey follow-on openings, HEEP by year-end). No later-quarter figure, event or wording appears in either draft; nothing in the drafts requires knowledge of anything after July 31, 2026.

---

## 9. Direct fixes made by the reviewer (before → after) and word counts

business.md (29 replacements, grouped)

1. l.6: "fast-casual restaurants" → "fast-casual (counter-service, made-to-order) restaurants".
2. l.8: "Its 10-K says" → "Its 10-K (annual report) says"; "the proxy states" → "the proxy (its annual shareholder-meeting filing) states".
3. l.12: "registration-rights agreement" → "registration-rights agreement (a contract letting a shareholder sell its stock in a public offering)"; "the 2006 IPO" → "the 2006 IPO (initial public offering)"; "paid an undisclosed fine" → "paid a fine whose amount the filing does not state" (`10-K-FY2022` l.470: "Chipotle paid a fine", no amount).
4. l.29: "99.5% of revenue is food and drink" → "... (computed)"; "The U.S. is 98% of revenue" → "... (computed)".
5. l.31: "menu price plus mix" → "menu price plus mix, meaning what people order"; added `[Q1 2026 release, Supplemental Financial and Other Data]` to the "since the start of 2025" sentence (Q1 2025's (0.4%) is only in the Q1 release's five-quarter table, l.360).
6. l.42 table: "122" → "122 (computed)"; l.45 footnote: added ", H1 Chipotlanes being Q1's 42 plus Q2's 80 [Q1 2026 release, Headline] [Q2 2026 release, Headline]".
7. l.49: "pre-opening costs and impairment" → "pre-opening costs and impairment (write-downs of restaurants worth less than their cost)".
8. l.51: "which the MD&A calls" → "which the 10-K's management discussion (MD&A) calls"; added `[10-K FY2023, Item 7 (Restaurant Operating Costs)]` for "sales leverage" (`10-K-FY2023` l.750, `10-K-FY2022` l.696; the phrase is not in the FY2025 10-K).
9. l.69: "so growth needs no working capital" → "... working capital (cash tied up in stock and unpaid bills)".
10. l.87: "Since 2024 buybacks have exceeded that cash" → "Since the end of 2024 buybacks have exceeded that cash" (2024: 1,001.6 vs 1,511.5; 2025: 2,425.5 vs 1,447.6; H1 2026: 1,354.9 vs 934.4).
11. l.89: "$787 thousand of restaurant cash flow" → "... restaurant cash flow (the deck's name for restaurant-level operating profit)".
12. l.93: "(the June 2026 total is not disclosed)" → "(one of them partner-operated; the June 2026 total is not disclosed)" (`slides-2025-Q4` l.362 footnote).
13. l.101: after the cyclospora quote, added "(cyclospora is a food-borne parasite; 200 basis points is two percentage points)".
14. l.103: 'a "rolling" menu-price strategy deliberately held to 1%–2% a year ... [Q2 2026 call, l.51] [Q2 2026 call, l.152]. Early warning: restaurant-level operating margin below the prior year while average check rises, as in every quarter since Q4 2025.' → 'a "rolling" menu-price strategy that the CFO says is held to "the 1% to 2% range" a year (spoken) ... [Q2 2026 call, l.51] [Q2 2026 call, l.143]. Early warning: restaurant-level operating margin below the prior year (as in every quarter since Q4 2025) while average check rises.' ("rolling strategy" is at l.143, not l.152; average check fell (0.1%) in Q1 2026, so the "every quarter" clause could only attach to the margin, which was below prior year in Q4 2025, Q1 and Q2 2026: 23.4 vs 24.8, 23.3 vs 26.2, 25.2 vs 27.4.)
15. l.105: "a pending shareholder class action (Stradford)" → "... (Stradford, a lawsuit brought on behalf of all shareholders)".
16. l.119: "joined in 2017 as Chief Operating Officer after 18 years at Arby's, became interim CEO" → "joined in 2017 after 18 years at Arby's, was Chief Operating Officer when Niccol left, became interim CEO" (`DEF14A` l.654; `8-K-2024-08-13` l.61).
17. l.121: "Right after Niccol's departure the board granted" → "Right after Niccol's departure was announced, the board granted" (grants August 22, 2024, `8-K-2024-08-28` l.59; departure effective August 31); "say-on-pay vote (55.4%" → "say-on-pay vote (the advisory shareholder vote on executive pay; 55.4%"; "Performance shares are judged" → "Performance shares (stock that vests only if targets are met) are judged".
18. l.125: `[10-K FY2024, Item 7 (Overview)]` → `[10-K FY2024, Item 7 (Cultivate Next Fund)]` (heading at `10-K-FY2024` l.767).
19. l.132 table label: "Retained earnings / (accumulated deficit)" → "Retained earnings (cumulative profit kept in the business) / (accumulated deficit)".
20. l.136: "charge for retiring treasury stock" → "... treasury stock (repurchased shares it had held rather than cancelled)".
21. l.152: "HEEP in about 2,000 restaurants" → "HEEP, the new kitchen equipment package, in about 2,000 restaurants".

outlook.md (11 replacements)

22. l.15 table: "G&A % of revenue" → "G&A (head office) % of revenue".
23. l.11 table: "legal accrual in labor" → "legal accrual (money set aside for a case) in labor".
24. l.20: after "exceptional hospitality" quote, added "(throughput: how many orders a line serves in a set time)".
25. l.22: after "toughest lap" quote, added "(the comparison against last year's quarter)"; after the cyclospora quote, added "(cyclospora is a food-borne parasite behind an industry outbreak)".
26. l.26: after "around 60%" quote, added "(yearly restaurant cash profit as a share of the build cost)".
27. l.28: after "hundreds of basis points" quote, added "(a basis point is a hundredth of a percentage point)".
28. l.30: after "attachment rate over 25%", added "(share of orders that included it)".
29. l.36: "Menu price added about 1.6% in Q2 and rises to ... (all spoken) [Q2 2026 call, l.51] ..." → "Menu price added 1.6% in Q2 [10-Q Q2 2026, Item 2 (Revenue table)] and rises to ... (the Q3 and full-year figures spoken only) [Q2 2026 call, l.51] ..." (`10-Q` l.995).
30. l.42: "EPS" → "EPS (earnings per share)".
31. l.56 table label: "G&A" → "G&A (non-GAAP: before one-off items)".

No table value, claim or quotation was changed except the two "(computed)" labels and the added tags. Fixes applied by `apply_fixes.py` with a one-occurrence assertion per replacement; the quote sweep (53 + 82 strings, same six non-source misses) and the tag-prefix check (27 + 10 prefixes, all listed) were re-run afterwards.

| File | Before review | After direct fixes | Target | Status |
|---|---|---|---|---|
| business.md | 2,787 | 2,925 | 2,000–3,000 | OK (75 words of headroom for the REVISE pass) |
| outlook.md | 1,102 | 1,162 | 800–1,200 | OK |

### Withdrawals recorded (§17: print full lines before ruling)

Eight first-pass searches returned nothing and were resolved as PASS after printing the full line or block; none was ruled a FAIL:

- "real food with wholesome ingredients ..." in the FY2025 10-K: `grep -F` returned nothing (curly characters on the line); the normalising `find.py` found it at l.201.
- "$80.6 million" unredeemed Rewards: searches for "80,6" and "unredeemed" found nothing; the 10-Q prints "Chipotle Rewards liability, ending balance | $ | 80,578" (l.539).
- Diluted EPS rows in the 10-Ks: a cell-pattern grep missed them; printing the "Earnings per share" block gave `10-K-FY2023` l.1317 (22.90), `10-K-FY2024` l.1305, `10-K-FY2025` l.1303.
- "sales leverage" absent from the FY2025 10-K: present in the FY2022 (l.696) and FY2023 (l.750) 10-Ks; tag added rather than FAIL.
- "not yet in the comparable base" absent from the FY2025 10-K: the bridge table (l.837–847) prints "Restaurants not yet in comparable base opened in 2025 | 327.0" and "... opened in 2024 | 481.8".
- "Total lease liabilities" absent: Note 9 prints "Operating lease liabilities (Current and Long-Term) | $ | 5,075,814" (l.2357).
- "100 million" absent from the FY2024 10-K: printed as "$100.0 million" (l.767).
- Boatwright's 2025 Summary Compensation Table row did not surface by name-grep; the pay-ratio section (l.2546) states "$15.46 million ... as reported in the 2025 Summary Compensation Table".

---

## 10. Verdict: REVISE

Five items for the writer, each mechanical, with the evidence. Nothing structural.

1. **business.md §1, l.12 — interim-CEO date.** "CEO Brian Niccol left on August 31, 2024 to run Starbucks; Scott Boatwright, the operations chief, became interim CEO that day and CEO in November 2024" is wrong on "that day". `8-K-2024-08-13.txt` l.59: "On August 12, 2024, Brian Niccol notified Chipotle ... of his decision to leave Chipotle on August 31, 2024"; l.61: the Board "has appointed Scott Boatwright, 51, as Interim Chief Executive Officer, effective immediately". §7 l.119 already says August 12. Suggested: "... left on August 31, 2024 to run Starbucks; Scott Boatwright, the operations chief, became interim CEO on August 12, the day the departure was announced, and CEO in November 2024".
2. **business.md §1, l.10 — "Alsea (named only in a press release and on the call, never in a filing)".** The 2026 proxy names Alsea: `DEF14A-2026.txt` l.73 (shareholder letter): "we signed an agreement with SPC Group to open restaurants in South Korea and Singapore and with Alsea to open Chipotle locations in Mexico beginning in 2026." Delete the parenthetical, or reword to "(named in the proxy's shareholder letter, the Mexico release and the call, not in the 10-K or 10-Q)" and add `[DEF 14A 2026, Letter to Shareholders]`. Alshaya is likewise named at `DEF14A` l.73 and in the Mexico release (l.17), which the sentence already tags.
3. **business.md §2 revenue table, l.22–23 — FY2022 segment cells.** "not disclosed" for FY2022 U.S. segment revenue and all other revenue is wrong: `10-K-FY2024.txt` l.2409 "U.S. segment total revenue | 11,111,732 | 9,720,369 | 8,516,210" and l.2413 "All other revenue (1) | 202,121 | 151,280 | 118,442" (Note 14, Segment Reporting). Replace with 8,516.2 and 118.4 and add `[10-K FY2024, Item 8, Note 14 (Segment Reporting)]` to the segments tag group in l.27. FY2021 stays "not disclosed" (the FY2023 10-K has no segment revenue). Recommended in the same pass: FY2021 revenue growth "not disclosed" → "26.1% (computed)" from FY2020 total revenue 5,984,634 (`10-K-FY2022.txt` l.1163) and FY2021 7,547,061, adding `[10-K FY2022, Item 8 (Consolidated Statements of Income and Comprehensive Income)]` to the growth tag group; no filing states the figure, so "not disclosed" is defensible, and the owner may prefer it.
4. **business.md §2 KPI table, l.42 — FY2021 Chipotlane openings.** "not disclosed" is wrong: the Q4/FY2025 deck's "Global Chipotlanes" chart (`slides-2025-Q4.txt` l.346–365, printed p.14) prints yearly Chipotlane openings "+56 +100 +174 +202 +238 +257 +258" at l.359 for 2019–2025, so 2021 = 174 (the 2022–2024 values match the 10-Ks). Replace with 174, add `[Q4 2025 slides, p.14]` to the FY2021 tag group in l.45, and footnote that the deck's 2025 figure (258) includes one partner-operated Chipotlane (l.362) while the table keeps the 10-K's company-owned 257.
5. **outlook.md §4, l.42 — "Not guided anywhere: restaurant-level operating margin, operating margin, EPS (earnings per share), revenue, capex, average unit volume."** Capex is guided in the FY2025 10-K: `10-K-FY2025.txt` l.1035 "In 2026, we expect to incur about $834.1 million in total capital expenditures. We expect approximately $531.8 million in capital expenditures related to our construction of new restaurants ...", which business.md §3 l.69 quotes. Remove "capex" from the list and add either a sentence or a row to the written-outlook table with the verbatim 10-K figure and `[10-K FY2025, Item 7 (Use of Cash)]` (the prefix is already in the outlook Sources); say that neither 2026 release nor the call repeated it, if the writer wants to keep the point that it is absent from the quarterly materials.

After the pass: re-run `python3 -P /tmp/cmg-orch/wc_prose.py` from `/home/ubuntu` (business.md has 75 words of headroom; item 5 adds a sentence to outlook.md, which has 38), and re-run the quote sweep if any quotation is added.

### For the owner (judgement calls, not blocking)

1. **FY2021 revenue growth cell**: the report's "not disclosed" is literally true; a computed 26.1% is available from the FY2022 10-K (item 3 above). Your call on which convention the tables should follow when a figure is derivable but never stated.
2. **Claim 3** grades average check (menu price plus mix) against the CFO's menu-price guidance; a negative mix could fail the claim even if pricing lands where he said. The 10-Q's "Menu price increase" row (l.995) would test the statement more directly; the writer's version tests the indicator the report actually tracks.
3. **"New restaurant productivity ... in the 80% range"** (outlook §3 l.26) is quoted as spoken but the company defines it nowhere in the cached text; consider asking the writer to drop it or to say the definition is not disclosed.
4. **Indicator 7** bundles five values (buyback dollars, average price, remaining authorization, shares, cash plus investments); comparable across quarters, but you may prefer to split it or drop the average price.
5. **Q4/FY2025 deck p.14** carries Chipotlane openings and totals back to 2019 (66 → 1,326); a "Chipotlanes at year-end" row could join the KPI table if you want the convenience layer tracked as a stock as well as a flow.
6. **Delivery-share row** (§2) uses the 10-K's "about 19% / about 18% / over 15% / over 16%" wording; no consistent series exists in the filings, so the row is approximate by construction.
7. **Glossary**: five entries, all essential; nothing to trim. Sources list is long (27 entries) because thirteen 8-Ks are cited individually; accurate, if heavy.

---

# Cycle 2 (2026-09-09) — re-verification and final verdict

_Method: the on-disk drafts were diffed against a rebuilt cycle-1 end state (`/tmp/cmg-orch/reviewer/business.c1.md`, `outlook.c1.md`, produced by applying `apply_fixes.py` to the `.orig.md` copies). The diff shows exactly the writer's five REVISE edits, the two word trims, and one Sources note; every one of the 40 cycle-1 direct fixes is still present (the glosses on the edited lines 6, 12 and 51 survive alongside the writer's changes). Quote sweep, tag-prefix check and the canonical word count were re-run from cwd `/home/ubuntu`._

## Per-item verification

| # | REVISE item | Draft now reads | Source check | Result |
|---|---|---|---|---|
| 1 | Interim-CEO date (business.md §1, l.12) | "Scott Boatwright, the operations chief, became interim CEO on August 12, the day the departure was announced, and CEO in November 2024" | `8-K-2024-08-13.txt` l.59 "On August 12, 2024, Brian Niccol notified Chipotle ... of his decision to leave Chipotle on August 31, 2024"; l.61 "appointed Scott Boatwright, 51, as Interim Chief Executive Officer, effective immediately"; `8-K-2024-11-12.txt` l.59 "On November 11, 2024 ... appointed Scott Boatwright, age 52, as Chief Executive Officer and as a member of the Board" | PASS; consistent with §7 l.119 |
| 2 | Alsea "never in a filing" (l.10) | "run by Alsea (named in the proxy's shareholder letter and the Mexico release, not in the 10-K or 10-Q)" with `[DEF 14A 2026, Letter to Shareholders]` added | `grep -n -i -F "alsea"` over the four 10-Ks and two 10-Qs, full lines: no hits. `DEF14A-2026.txt` l.73 (under the heading "DEAR SHAREHOLDERS," at l.72) names Alsea; `press-release-2026-07-13-mexico.txt` l.7 names Alsea; the call (l.44) also does, and the sentence keeps its call tag | PASS; the section heading is literally "Dear Shareholders", so "Letter to Shareholders" is a fair descriptor (the DEF 14A prefix is in the Sources list) |
| 3 | FY2022 segment cells and FY2021 growth (l.21–23, l.27) | U.S. segment revenue FY2022 8,516.2; all other revenue FY2022 118.4; revenue growth FY2021 "26.1% (computed)"; footnote adds `[10-K FY2024, Item 8, Note 14 (Segment Reporting)]` to segments and "FY2021 computed from FY2020 revenue [10-K FY2022, Item 8 (Consolidated Statements of Income and Comprehensive Income)]" to growth | `10-K-FY2024.txt` l.2409 "U.S. segment total revenue | 11,111,732 | 9,720,369 | 8,516,210"; l.2413 "All other revenue (1) | 202,121 | 151,280 | 118,442" (Note 14 heading at l.2380s, "14. Segment Reporting"); `10-K-FY2022.txt` l.1163 "Total revenue | 8,634,652 | 7,547,061 | 5,984,634"; 7,547,061 / 5,984,634 − 1 = 26.11% | PASS ×3; 8,516.2 + 118.4 = 8,634.6 against total revenue 8,634.7 (rounding), consistent |
| 4 | FY2021 Chipotlane openings (l.42, l.45) | 174, with `[Q4 2025 slides, p.14]` and the footnote "(the deck's 2025 figure, 258, includes one partner-operated Chipotlane; the table keeps the 10-K's 257)" | `slides-2025-Q4.txt` l.359 (p.14 chart, Chipotlane openings by year) "+56 +100 +174 +202 +238 +257 +258"; l.362 "* Includes 1 partner-operated Chipotlane in 2025"; `10-K-FY2025.txt` l.757 "opened 334 company-owned restaurants, which included 257 restaurants with a Chipotlane" | PASS; the deck's 2022–2024 values (202 / 238 / 257) match the 10-Ks, so the 2021 reading is on the same basis |
| 5 | Capex "not guided anywhere" (outlook.md §4, l.42) | "Not guided anywhere: restaurant-level operating margin, operating margin, EPS (earnings per share), revenue, average unit volume. Capex is guided only in the 10-K ("about $834.1 million in total capital expenditures" for 2026), not in the 2026 releases or on the call [10-K FY2025, Item 7 (Use of Cash)]."; outlook Sources entry for the 10-K now notes "the 2026 capex plan" | `10-K-FY2025.txt` l.1035 "In 2026, we expect to incur about $834.1 million in total capital expenditures" (verbatim); `grep -F "834"` over the three releases, three decks, transcript and both 10-Qs finds no capex figure (only unrelated cash-flow and investment cells); the only "CapEx" on the call is an analyst's question at l.87, answered "I have nothing to report today" (l.90); no "expect to incur" or capex expectation in either 2026 10-Q or release | PASS |

Trims: l.6 "serving made-to-order burritos" → "serving burritos" (the gloss "fast-casual (counter-service, made-to-order)" earlier in the sentence still carries the point); l.51 "for five years" dropped (the table shows the years). Wording only; no fact changed.

## Re-runs

- **Quote sweep** (`quotes.py`): business.md 53 strings, outlook.md 83 (one new: "about $834.1 million in total capital expenditures", found at `10-K-FY2025` l.1035); the same six non-source misses as cycle 1 (two document titles, a column name, two case-only differences, and nothing else). 0 substantive misses.
- **Tag prefixes** (`tags.py`): business.md 256 tags over 27 prefixes, all 27 listed in Sources (the new `[10-K FY2024, Item 8, Note 14 ...]`, `[10-K FY2022, Item 8 ...]`, `[DEF 14A 2026, Letter to Shareholders]` and `[Q4 2025 slides, p.14]` use existing prefixes); outlook.md 111 tags over 10 prefixes, all listed.
- **§2 tables re-checked cell by cell** (the only tables that changed): 48 + 54 cells; the 44 + 53 cells not touched by the writer are byte-identical to the cycle-1 state verified in §3(a)–(b); the 4 changed cells verified above. No other table, claim or quotation moved (diff shows no other lines).
- **Skeleton**: header lines exact in both files; `_Proposed — owner to review and lock._` at business.md l.140; no §6 in outlook.md; heading order unchanged.
- **Word counts** (`python3 -P /tmp/cmg-orch/wc_prose.py`, cwd `/home/ubuntu`): business.md 2,950 (limit 2,000–3,000), outlook.md 1,186 (limit 800–1,200). Both within limits; the writer's reported counts reproduced exactly.

## Further direct fixes

None needed.

## Final verdict: PASS

All five REVISE items are resolved with correct figures and tags; nothing from cycle 1 was undone; no new issue found. The "For the owner" list in §10 above still applies (indicator lock, claim 3's check-versus-price basis, the undefined "new restaurant productivity" figure, the optional Chipotlane-total row); the FY2021 growth cell now shows the computed 26.1%, which the owner may revert to "not disclosed" if the tables should carry only stated figures.
