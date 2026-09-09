# American Electric Power Company, Inc. (AEP) — Reviewer report, 2026-Q2

_Reviewed 2026-09-09 (cycle 1 of 2) against `companies/AEP/sources/2026-Q2/` only: the cached `.txt` files; the `notes-*.md` files were not used as evidence. As-of cutoff 2026-07-30; nothing dated later was consulted (the Motley Fool page of the 2026-07-30 call, posted 2026-07-30 evening, was used for call wording only; the August 2026 investor handout was correctly not fetched and is cited nowhere). Line numbers (l.N) refer to the cached `.txt` files. Deck and release page numbers are the printed footers, which equal PDF pages; page maps from the form feeds: Q2 deck p.5 = l.100–135, p.8 = l.158–188, p.12 = l.276–325, p.14 = l.377–421, p.15 = l.421–454, p.18 = l.481–521, p.21 = l.615–671, p.22 = l.671–705, p.24 = l.745–774, p.25 = l.774–807, p.28 = l.837–873, p.31 = l.905–936, p.32 = l.936–969; Q1 deck p.5 = l.103–140, p.7 = l.148–195, p.8 = l.195–240, p.16 = l.499–542, p.19 = l.633–663, p.28 = l.873–911, p.30 = l.941–976, p.32 = l.983–1013, p.33 = l.1013–1046; Q2 release p.1 = l.1–47, p.2 = l.47–95, p.3 = l.95–145, p.4 = l.145–202, p.7 = l.297–369, p.8 = l.369–411, p.9 = l.411–492; Q1 release p.2 = l.46–96, p.3 = l.96–148, p.8 = l.374–414; Q4 2025 release (PDF pages) p.1 = l.1–45, p.3 = l.93–108, p.4 = l.108–160. Draft line numbers refer to the drafts as handed off (business.md 179 lines, outlook.md 76 lines); the direct fixes did not change line counts. Word counts by `python3 -P /tmp/aep-orch/wc_prose.py` from cwd `/home/ubuntu`; the writer's 2,802 / 1,103 reproduced exactly before edits. Scratch in `/tmp/aep-orch/reviewer/` (`find.py` normalised full-line search, `pages.py` page maps, `quotes.py` quote sweep, `apply_fixes.py` with a one-occurrence assertion per replacement; originals kept as `business.orig.md` / `outlook.orig.md`)._

**Cycle-1 verdict: REVISE** — two factual items for the writer (one wrong pair of numbers, one quote tagged to the wrong filing and mis-dated) plus one §3 rule 5 trim, all with the evidence and the exact correction in §12. Everything else checked out or was fixed directly: 207 table and indicator cells verified against the tagged text (every "(computed)" cell re-derived, every "not reported" / "not disclosed" / "—" cell searched with full-line output), 1 cell mischaracterised (fixed directly); 98 quoted strings swept, every substantive quote found verbatim; 66 prose facts checked with 4 failures (2 fixed directly, 2 on the REVISE list); no invented number; no transcript figure presented as a number; 11 claims that all pass §9 after the writer's own labelling; 8 indicators each anchored to a disclosure present in both the Q1 and Q2 documents. Direct fixes: 20 replacements in business.md and 8 in outlook.md (glosses, tag precision, two "(computed)" labels, five wording-precision edits), listed in §13.

---

## 1. Rubric (§14)

Read as the owner would: a smart 16-year-old with no finance background.

1. **Can I explain what this company does, and who pays it, in two sentences?** **Yes.** §1 l.6–8 does it: regulated monopoly utilities in eleven states that generate, transmit and deliver electricity; customers must buy from them and state commissions or FERC set the price. §2 l.14 names who pays ($16.0B retail, $1.6B transmission, $1.2B wholesale, $2.4B AEP Energy).
2. **Do I know exactly what would kill it, and what the early warning sign is?** **Yes.** §6 ranks six scenarios, each with what must happen, an early warning and the exposure (data-center load not arriving → contracted GW falling / ERCOT rejecting projects / commercial kWh growth fading; regulators refusing recovery → approved ROEs below 9.5%, earned ROE below 9%; balance sheet → FFO/debt below 14%, negative outlook; FERC changing the transmission deal; PJM cost shifts; coal and storms). Scenario 1's point that 45 of the 69 GW rest on letters of agreement in a market whose peak is about 8 GW is the sharpest part of the report.
3. **Do I know why the margins are what they are, and whether cost scales with usage?** **Yes.** §3 l.45 explains that the largest cost (fuel and purchased power, 32% of revenue) is passed through so revenue moves with fuel while profit does not, that the rest is fixed, and that operating margin therefore tracks approved investment; §2 l.39–41 explains rate base, allowed return, regulatory lag and formula rates in plain words with the 10-K's own sentences; §4 l.66 explains why free cash flow is negative by design.
4. **Could I predict what the scorecard will check next quarter, from §5 of the outlook alone?** **Yes.** All 11 claims are single-direction and mechanical; the three sharpenings and two disclosure checks are labelled (see §5 below).
5. **Did nothing in the report require knowledge I don't have?** **Now yes.** Before review about fifteen terms were unexplained (FERC, rate case, depreciation, gross and operating margin, GAAP, EPS, tariff, disallowance, loss contingency, say-on-pay, investment grade, SWEPCo, PSO, I&M, WVPSC, ATM, TSR); all are now glossed at first use (§13).

---

## 2. Skeleton and format compliance

**business.md**

| Requirement (§6) | Status |
|---|---|
| `# <Company> — The Business` | OK |
| `_As of Q2 2026. Written 2026-09-09._` | OK (l.2) |
| §1 What they do (incl. short history) | OK; history paragraph l.10 |
| §2 How the money comes in (5-year segment table) | OK; two tables (revenue, earnings), FY2021–FY2025 + 6M 2026; segment names as filed |
| §3 The economics (revenue, GM, OM, capex, capex/revenue) | OK; gross margin row reads "not reported" (verified: no gross-margin line in any statement) |
| §4 How profitable, really (5-year table) | OK; 10 rows |
| §5 Why customers don't leave (source + weakening sign) | OK; legal moat, contract lock-in, three weakening signs |
| §6 What could break it (ranked; early warning; exposure; concentration) | OK; six ranked scenarios + Concentration paragraph |
| §7 Who runs it and what they do with the cash | OK; people, pay, cash, table |
| §8 Indicators (5–8; name / why / where) | OK; 8 indicators |
| `_Proposed — owner to review and lock._` | OK (l.135) |
| Glossary (only unavoidable terms, one sentence each) | OK; 6 entries, each one sentence, each used repeatedly |
| Sources (every tag mapped; page basis stated; note-number map) | OK; 21 tags mapped; the eight-registrant caveat and the note-number differences are stated |
| Length 2,000–3,000 prose words | **PASS**: 2,802 before review, 2,913 after glosses (ceiling 3,000; REVISE item 3 frees words) |

**outlook.md**

| Requirement (§7) | Status |
|---|---|
| `# <Company> — Outlook as of Q2 2026` | OK |
| `_Transcript source tier: third-party (The Motley Fool). Written 2026-09-09._` | OK (l.2); MANIFEST says tier 3, posted 2026-07-30 20:42 ET |
| §1 one row per indicator; this q / last q / expected | OK; 8 rows in business.md §8 order |
| §2 What management says | OK |
| §3 Growth engines (what / how big / claim / working-or-not) | OK; four engines, each with a "Working if" test |
| §4 Guidance verbatim | OK; eight bullets, all verified word for word (§4 below) |
| §5 Claims (6–12) | OK; 11 claims |
| §6 Tone shift | Correctly absent (first run) |
| Sources | OK; 10 tags mapped; transcript conventions stated (numbers from release/slides; speaker labels unreliable; doubtful lines to "management") |
| Length 800–1,200 prose words | **PASS**: 1,103 before, 1,128 after glosses |

**Indicator anchoring (§8 of AGENTS.md)** — each proposed indicator, the recurring disclosure it rests on, and whether that disclosure appears in both the Q1 2026 and Q2 2026 documents:

| # | Indicator | Recurring disclosure | Q1 | Q2 | Anchored? |
|---|---|---|---|---|---|
| 1 | Construction expenditures vs the year's forecast | 10-Q cash-flow line "Construction Expenditures"; Item 2 "Management forecasts approximately $N billion" | l.1893; l.1468 | l.2258; l.1892 | Yes |
| 2 | Operating earnings by segment | Release p.3 "Operating Earnings (non-GAAP)" table | l.129–135 | l.125–131 | Yes |
| 3 | Retail kWh by class, y/y, both utility segments | Release p.8 "Summary of Selected Sales Data" | l.374–404 | l.369–401 | Yes |
| 4 | Incremental contracted load by 2030, ERCOT/PJM/SPP | Deck "2026-2030 Load Growth" page | p.16 | p.14 | Yes, but a deck KPI, not a filing line. It has appeared three quarters running (Q4 2025 release 56 GW, Q1 deck 63, Q2 deck 69), which meets §8's "KPI the company has reported for several quarters"; the owner should know it can vanish from a deck without notice, in which case the refresh records 🔇. The one-off level (69 GW) is correctly a claim (claim 5), not the indicator. |
| 5 | Regulated earned ROE, TTM, total and by company | Deck "Regulated Earned Returns" page | p.28 | p.28 | Yes |
| 6 | Completed base rate cases | 10-Q Item 2 "Completed Base Rate Case Proceedings" table | l.616–623 | l.700–711 | Yes |
| 7 | FFO/debt (S&P, Moody's) and total debt | Deck credit-metrics and FFO reconciliation pages | p.32–34 | p.31–33 | Yes |
| 8 | Shares outstanding, forwards remaining, stock issued | 10-Q cover; Note 12 forward table; cash-flow "Issuance of Common Stock" | l.66; l.6667–6673; l.1906 | l.66; l.7993–7999; l.2271 | Yes |

None of the one-off targets the brief warned about (69 GW, $78B, 9.5% ROE by 2030) is an indicator; 69 GW is claim 5, $78B is the baseline of claim 8, and 9.5% by 2030 sits in the "expected" column and §4.

---

## 3. Citation spot-check

Legend: PASS = number or wording found in the tagged source at the line given; FAIL = not there, wrongly characterised, or tagged to the wrong place. Every "(computed)" cell was re-derived from the sourced inputs (Python, `/tmp/aep-orch/reviewer/`). All AEP-column figures were taken from the statements headed "AMERICAN ELECTRIC POWER COMPANY, INC. AND SUBSIDIARY COMPANIES" (10-K FY2025 l.3528–3874; 10-K FY2023 l.3404–3745; 10-Q Q2 l.1929–2292; 10-Q Q1 l.1588–1926), not from a subsidiary registrant's.

### 3(a) business.md §2 segment revenue table (l.16–24) — every cell

Inputs: `10-K-FY2023.txt` Note 9 l.9600 (2021), l.9572 (2022); `10-K-FY2025.txt` Note 9 l.9945 (2023), l.9916 (2024), l.9885 (2025); `10-Q-2026-Q2.txt` Note 8 l.6739 (6M 2026). Consolidated totals also on the income statements (l.3417, l.3541, l.1946).

| Row | Source values (USD m) | Result |
|---|---|---|
| Vertically Integrated Utilities 9,998.5 / 11,477.5 / 11,450 / 11,597 / 12,819 / 6,560 | as stated | PASS ×6 |
| Transmission and Distribution Utilities 4,492.9 / 5,512.0 / 5,713 / 5,908 / 6,147 / 3,192 | as stated | PASS ×6 |
| AEP Transmission Holdco 1,526.2 / 1,677.0 / 1,729 / 1,951 / 2,377 / 1,208 | as stated | PASS ×6 |
| Generation & Marketing 2,163.7 / 2,466.9 / 1,632 / 2,045 / 2,762 / 1,661 | as stated | PASS ×6 |
| Corporate and Other 72.2 / 109.9 / 168 / 183 / 144 / 61 | as stated | PASS ×6 |
| Less: sales between segments (1,461.5) / (1,603.8) / (1,710) / (1,963) / (2,373) / (1,217) | as stated | PASS ×6 |
| Consolidated 16,792.0 / 19,639.5 / 18,982 / 19,721 / 21,876 / 11,465 | as stated (FY2023 prints 18,982.3; the table uses the FY2025 10-K's whole-million figure, consistent with its column source) | PASS ×6 |

42/42 PASS. l.26 "Holdco revenue is mostly billed to AEP's own utilities and eliminated": 1,884 of 2,377 (79%) is intersegment (l.9884–9885). PASS.

### 3(b) business.md §2 segment earnings table (l.28–35) and footnote — every cell

Inputs: `10-K-FY2023.txt` l.9608 (2021 Net Income), l.9584 (2022); `10-K-FY2025.txt` l.9958 (2023), l.9930 (2024), l.9903 (2025) Earnings Attributable to AEP Common Shareholders; `10-Q-2026-Q2.txt` l.6751 (6M 2026).

| Row | Result |
|---|---|
| VIU 1,116.7 / 1,296.2 / 1,090 / 1,453 / 1,605 / 746 | PASS ×6 |
| T&D 543.4 / 595.7 / 699 / 726 / 816 / 459 | PASS ×6 |
| Holdco 682.0 / 676.8 / 703 / 790 / 1,161 / 434 | PASS ×6 |
| G&M 210.2 / 274.5 / (26) / 289 / 287 / 172 | PASS ×6 |
| Corporate and Other (64.2) / (537.6) / (258) / (291) / (289) / (224) | PASS ×6 |
| Total 2,488.1 / 2,305.6 / 2,208 / 2,967 / 3,580 / 1,587 | PASS ×6 |
| Footnote: measure change Net Income (FY2023 10-K l.9535 "AEP measures segment profit or loss based on net income (loss)") vs Earnings Attributable to AEP Common Shareholders (FY2025 10-K l.9848); FY2023 2,212.6 (l.9558) vs 2,208 (l.9958); $363M Kentucky loss in Corporate and Other 2022 (l.9574); $354M FERC NOLC in Holdco (release p.7 l.352) | PASS ×4; the owner's ask (segment-measure change footnoted) is met |

40/40 PASS.

### 3(c) business.md §3 economics table (l.47–56) — every cell

Inputs: income statements `10-K-FY2023` l.3417–3441, `10-K-FY2025` l.3541–3563, `10-Q` l.1946–1968; cash-flow "Construction Expenditures" `10-K-FY2023` l.3717, `10-K-FY2025` l.3838, `10-Q` l.2258.

| Row | Check | Result |
|---|---|---|
| Revenue | as 3(a) | PASS ×6 |
| Purchased power and fuel / revenue (computed) 32.6 / 36.1 / 34.7 / 30.1 / 32.1 / 32.5% | 5,466.3 / 7,097.9 / 6,578 / 5,936 / 7,031 / 3,721 over revenue → 32.55 / 36.14 / 34.65 / 30.10 / 32.14 / 32.46% | PASS ×6 |
| Gross margin "not reported" ×6 | No gross-margin or cost-of-sales subtotal on any AEP income statement (l.3536–3555; l.3412–3433; l.1941–1960) | PASS ×6 |
| Operating margin (computed) 20.3 / 17.7 / 18.7 / 21.8 / 24.3 / 22.7% | Operating income 3,411.3 / 3,482.7 / 3,556 / 4,304 / 5,319 / 2,607 → 20.32 / 17.73 / 18.73 / 21.82 / 24.31 / 22.74% | PASS ×6 |
| D&A 2,825.7 / 3,202.8 / 3,090 / 3,290 / 3,380 / 1,817 | l.3429; l.3551; l.1956 | PASS ×6 |
| Interest expense 1,199.1 / 1,396.1 / 1,807 / 1,863 / 2,026 / 1,137 | l.3441; l.3563; l.1968 | PASS ×6 |
| Construction expenditures 5,659.6 / 6,671.7 / 7,378 / 7,631 / 8,453 / 5,606 | l.3717; l.3838; l.2258 | PASS ×6 |
| Capex / revenue (computed) 33.7 / 34.0 / 38.9 / 38.7 / 38.6 / 48.9% | 33.70 / 33.97 / 38.87 / 38.69 / 38.64 / 48.90% | PASS ×6 |

48/48 PASS. l.45 prose: $7.0B and 32% (7,031 / 21,876 = 32.1%) PASS; other O&M $4.4B (2,950 + 1,499 = 4,449) PASS; depreciation $3.4B, taxes $1.6B (1,631), interest $2.0B PASS; "19% in 2023, 24% in 2025" are the computed margins (18.7%, 24.3%) but were tagged Item 7 without a "(computed)" label — fixed directly (tag → Item 8, label added).

### 3(d) business.md §4 cash table (l.68–79) — every cell

| Row | Source | Result |
|---|---|---|
| Net income 2,488.1 / 2,305.6 / 2,213 / 2,976 / 3,696 / 1,650 | `10-K-FY2023` l.3448; `10-K-FY2025` l.3570; `10-Q` l.1975 | PASS ×6 |
| Operating cash flow 3,839.9 / 5,288.0 / 5,012 / 6,804 / 6,944 / 3,421 | l.3714; l.3835; l.2255 | PASS ×6 |
| Construction expenditures | as 3(c) | PASS ×6 |
| Free cash flow (computed) (1,819.7) / (1,383.7) / (2,366) / (827) / (1,509) / (2,185) | OCF less construction, re-derived exactly | PASS ×6 |
| Plant acquisitions (767.2) / (1,207.3) / (155) / (399) / (3,453) / (1,315) | "Acquisitions of Renewable Energy Facilities" l.3723 (2021–2022); "Acquisitions of Generation Facilities" l.3844, l.2262 | PASS ×6 |
| Dividends paid on common stock (1,507.7) / (1,628.7) / (1,752) / (1,898) / (2,008) / (1,039) | FY2021–FY2022 from the FY2023 10-K statement of changes in equity "Common Stock Dividends" l.3511, l.3520 (its cash-flow line, l.3738, bundles minority-holder dividends: 1,519.5 / 1,645.2); FY2023–FY2025 cash-flow l.3862; 6M l.2280. The equity-statement basis matches the cash-flow basis where both exist (2023: 1,752.3 vs 1,752) | PASS ×6; Sources note l.160 discloses the basis |
| Net debt raised 3,631.7 / 3,802.5 / 1,985 / 2,126 / 3,596 / 3,987 | Issuance of LTD + ST >90d + change in ST <90d − retirements − redemptions: 6,486.3+1,393.3−487.3−2,989.3−771.3; 4,649.7+833.9+1,650.4−2,345.4−986.1; 5,463+1,070−1,223−2,196−1,129; 5,117+724−159−2,685−871; 8,261+320−658−3,649−678; 5,045+520−1,578 (l.3731–3735; l.3854–3858; l.2272–2277) | PASS ×6 on arithmetic; only the 6M cell carried "(computed)" although every cell is computed — label moved to the row (direct fix) |
| Common stock issued, net 600.5 / 826.5 / 1,000 / 552 / 775 / 405 | l.3730; l.3853; l.2271 | PASS ×6 |
| Minority-stake sale proceeds — / — / — / — / 2,783 / — | l.3861 (2025 only); no such line in other years or 6M 2026 (l.2279 shows 2,783 in the 2025 comparative only) | PASS ×6 |
| Share buybacks 0 ×6 | No repurchase line on any cash-flow statement; treasury shares 1,186,815 at 12/31/2024, 12/31/2025 and 6/30/2026 (`10-K-FY2025` l.3779; `10-Q` l.2200); the 10-K's only "repurchase" hits are repurchase agreements (financing) | PASS ×6 |

60/60 PASS. l.81 "treasury shares were unchanged" PASS (above).

### 3(e) business.md §7 table (l.123–131) — every figure

| Row | Source | Result |
|---|---|---|
| Dividends $3.00 → $3.74; $0.95 per quarter | `10-K-FY2023` l.3536 ($3.00 for 2021); `10-K-FY2025` l.3663 ($3.74 for 2025); `10-Q` l.2080 and l.1783 ($0.95) | PASS ×3 |
| Shares 504.2M → 540.9M → 544.4M | `10-K-FY2022` l.4220–4221 (524,416,175 − 20,204,160 = 504,212,015); `10-K-FY2025` l.3778–3779 (542,048,288 − 1,186,815 = 540,861,473); `10-Q` cover l.66 (544,397,352) | PASS ×3 |
| Forwards 45M for about $5.0B | `10-Q` Note 12 l.7997–7999: 18 + 3 + 24 = 45M shares; 1,728 + 374 + 2,932 = $5,034M | PASS ×2 |
| Total debt $36.1B → $48.8B → $52.8B | `10-K-FY2022` l.4183+4184+4196 (2,614.0 + 2,153.8 + 31,300.7 = 36,068.5); `10-K-FY2025` l.3745+3746+3757 (48,830); `10-Q` l.2166+2167+2178 (52,836; also deck p.32 l.945) | PASS ×3 |
| Minority stake 19.9%, $2.82B, June 2025 | `10-K-FY2025` Note 7 l.9146 (KKR and PSP funds; $2.82B; closed June 2025; $2.78B net) | PASS ×3 |
| Plan $72B → $78B, "over $10 billion" | `10-K-FY2025` l.2890 (October 2025, $72B); `10-Q` l.574 ($78B); release p.1 l.24 | PASS ×3 |
| Icahn signed Dec 22, 2025; ended Apr 28, 2026 | `8-K-2025-12-29` l.52; `DEF14A` l.797 ("terminating the Board Observer Agreement effective April 28, 2026") | PASS ×2 |

19/19 PASS.

### 3(f) outlook.md §1 indicator table (l.10–17) — every number

| Cell | Source | Result |
|---|---|---|
| Row 1: $2,776M (computed 5,606 − 2,830); $5,606M; $2,830M; "approximately $12.8 billion"; "$13B 2026 Capital Investment" | `10-Q` l.2258; `10-Q-Q1` l.1893; `10-Q-Q1` l.1468; Q1 deck p.5 l.115–119 (label split over three lines) | PASS ×5 |
| Row 2: 302; 239; 225; 91; (115); 742 / 464; 237; 209; 90; (109); 891 | Q2 release p.3 l.126–131; Q1 release p.3 l.130–135 | PASS ×12; both Q1-call quotes at `transcript-2026-Q1` l.67 (Mihalik) PASS ×2 |
| Row 3: +4.6 / +14.9; +11.4 / +17.4 / +1.2 / +15.8; +12.0 / +33.3 | Q2 release p.8 l.380–396; Q1 release p.8 l.385–400; "7 GW Incremental Contracted Load in 2026" Q1 deck p.5 l.131–133 | PASS ×9 |
| Row 4: 69 (45/18/6); 63 (41/16/6) | Q2 deck p.14 l.382–402; Q1 deck p.16 l.504–522; quote `transcript-2026-Q1` l.83 (Mihalik) | PASS ×9 |
| Row 5: 9.2% (I&M 12.7%, KPCo 4.1%); 9.3% (12.6%, 4.2%); 2026E 9.2%; "approximately 9.5% by 2030" | Q2 deck p.28 l.841, 845, 861; Q1 deck p.28 l.877, 881, 898; trend series l.891–899 (8.8 → 9.05 → 9.1 → 9.2 → 9.5, re-associated by the gatherer, monotonic); l.874 | PASS ×8 |
| Row 6 Q2 cell: "Completed: Ohio $11M at 9.84% (April 2026)" | `10-Q` l.711 has the row, but so does the **Q1** 10-Q's completed table (`10-Q-Q1` l.623: "OPCo \| Ohio \| 11 \| 9.7% \| 9.84% \| April 2026"); the Q2 table (l.708–711) is identical to Q1's, so nothing was completed in the quarter | **FAIL (characterisation)** — fixed directly: cell now says "none new; the 10-Q's completed-case table is unchanged from Q1 (Ohio ... was already listed there)", and Ohio was added to the Q1 cell |
| Row 6 pending: SWEPCo Texas settlement in principle; PSO 9.375%; Virginia filed May 2026 | `10-Q` l.6307 (April 2026 settlement in principle; order expected Q4 2026); l.6297 (9.375%); l.729 ("APCo \| Virginia \| May 2026 \| 61 \| 10.5%") | PASS ×3 |
| Row 6 Q1 cell: WV $91M 9.75%; Arkansas $85M 9.65%; Kentucky $55M 9.75% | `10-Q-Q1` l.620–622 | PASS ×6 |
| Row 6 expected: PSO order Q3 2026; SWEPCo Texas order Q4 2026 | Q1 deck p.30 l.967, l.962 | PASS ×2 |
| Row 7: 14.6%; 14.0%; $52,836M / 14.7%; 13.9%; $51,109M; "Maintaining FFO/Debt targeted range of 14%-15% for 2026-2030" | Q2 deck p.31 l.912, p.32 l.945; Q1 deck p.32 l.990, p.33 l.1022; Q1 deck p.7 l.188–190 (split over three lines, "2026-" / "2030") | PASS ×7 |
| Row 8: 544,397,352; 45M; $5.0B; $405M / 544,104,955; 21M; $2.1B (computed); $358M; "$1 billion of ATM ... $665 million"; "Growth Equity" $3,000M 2028–2030 | `10-Q` l.66, l.7997–7999, l.2271; `10-Q-Q1` l.66, l.6671–6672 (18 + 3 = 21; 1,749 + 373 = 2,122), l.1906; `transcript-2026-Q1` l.147 (Mihalik, answering David Arcaro, Morgan Stanley, l.143); Q1 deck p.19 l.650 | PASS ×11 |

75/75 numbers PASS; 1 cell characterisation FAIL (fixed).

### 3(g) Prose sentences — 66 checks across both files

| # | Sentence / figure (file:line) | Tag | Found | Result |
|---|---|---|---|---|
| 1 | "more than five million retail customers"; eleven states (b:6) | 10-K FY2025 Item 7 | l.1669 | PASS |
| 2 | ~25,000 MW; 38,000 circuit miles; ~2,000 miles 765-kV; 252,000 miles distribution (b:6) | Item 7 | l.1673–1677 | PASS ×4 |
| 3 | "backbone" of the eastern grid (b:6) | 10-K FY2023 Item 7 | l.1716 ("the backbone of the electric interconnection grid in the eastern United States"; that filing says 40,000 miles and 2,200 miles of 765 kV — the draft correctly takes the FY2025 counts) | PASS |
| 4 | "effectively grant the exclusive ability to provide electric service"; state commissions or FERC set prices (b:8) | Item 1 | l.841 | PASS |
| 5 | Ohio and Texas T&D: customers buy electricity from competing suppliers (b:8) | Item 1 / Note 9 | l.871 (AEP Texas serves REPs), l.342 ("REP \| Texas Retail Electric Provider"), l.230 (Ohio CRES providers) | PASS |
| 6 | VIU "in ten states" (b:8) | Note 9 | l.9854 companies → AR, IN, KY, LA, MI, OK, TN, TX, VA, WV | PASS |
| 7 | "to be a pure play, regulated, electric utility" (b:8) | DEF 14A Corporate Governance | l.556 (under "Linking Business Strategy with Key Skills", as the Sources list says) | PASS |
| 8 | Incorporated New York 1906 (b:10) | Item 1 | l.461 | PASS |
| 9 | Kentucky: agreed 2021, $363M loss 2022, FERC denial December 2022, cancelled 2023; renewables sold 2023 at $93M loss (b:10) | 10-K FY2023 Note 7; 10-K FY2025 Note 7 | l.1802–1808 (October 2021 SPA; $363M; "In December 2022, the FERC issued an order denying"; April 2023 termination); income statement l.3428 (92.7) | PASS ×5 |
| 10 | HB 6: "Management does not believe..."; shareholder suits dismissed; SEC $19M loss contingency 2024 (b:10) | 10-K FY2023 Note 6; 10-K FY2025 Item 7 | l.1968; l.1970 (securities class action dismissed with prejudice Dec 2021), l.1972 (consolidated derivative actions dismissed with prejudice March 2023; one notice of appeal April 2023); `10-K-FY2025` l.2844 ("$19 million loss contingency recorded in 2024 associated with the SEC investigation") | PASS ×3 (wording tightened to note the pending appeal, direct fix) |
| 11 | Fehrman ex-BHE CEO, CEO August 2024 (b:10, b:117); age 65; Chair since August 2025; BHE 2018–2023 (b:117) | Item 1 | l.964–970 | PASS ×5 |
| 12 | Icahn observer Dec 2025 in place of two nominated directors; ended April 28, 2026 (b:10) | 8-K 2025-12-29; DEF 14A | l.52, l.62; `DEF14A` l.797 | PASS ×2 |
| 13 | Revenue by class: $16.0B retail (7.8 / 4.7 / 3.3); $1.6B transmission; $1.2B wholesale; $2.4B AEP Energy (b:14) | Note 20 | l.12779–12792 (7,754; 4,694; 3,250; 16,000; 1,603; 1,220; 2,397) | PASS ×7 |
| 14 | Cost-of-service quote; "found to be a prudent investment..." (b:39) | Item 1 | l.777; l.779 | PASS ×2 |
| 15 | "have long timelines..."; "earning less than the allowed returns" (b:41) | Item 1A | l.1068 | PASS ×2 |
| 16 | Formula-rate quotes; rate base $13.3B for 2025; FERC ROEs 9.85%–10.50% (b:41) | Item 1 | l.928; l.932; l.524–527 (OHTCo 9.85%, APTCo etc. 10.35%, OKTCo/SWTCo 10.50%) | PASS ×5 |
| 17 | "such that the revenues and expenses ... do not affect Earnings" (b:45) | Item 7 | l.2328 | PASS |
| 18 | Net plant $66.0B end-2021 → $96.7B 6/30/2026; $8.5B + $3.5B vs $3.4B depreciation (b:60) | 10-K FY2022 Item 8; 10-Q Item 1; 10-K FY2025 Item 8 | `10-K-FY2022` l.4148 (66,001.3); `10-Q` l.2129 (96,673); l.3838, l.3844, l.3809 | PASS ×5 |
| 19 | $12.2B 2026 and $59.7B 2027–2030, "$72 billion capital plan" of October 2025; 10-Qs $12.8B and $65.1B, "$78 billion, five-year capital plan" (b:60) | 10-K Item 7; 10-Q Item 2 | l.3116, l.2890; `10-Q` l.1892, l.574 (and `10-Q-Q1` l.1468, l.499) | PASS ×6 |
| 20 | Transmission $33B / generation $24B / distribution $17B; rate base $80B → $134B (b:60) | Q2 slides p.21 | l.659–663; l.649, l.640 | PASS ×5 |
| 21 | Retail kWh +5% 2024, +7% 2025 (computed); T&D commercial +28% 2025; quoted driver (b:62) | Item 7 | VIU table l.2356–2366 and T&D table l.2524–2534: (91,956+91,039)/(90,148+83,834) = +5.2%; (93,967+102,372)/182,995 = +7.3%; 46,187/36,147 = +27.8%; quote l.1869 | PASS ×4 ("(computed)" added to the 28%, direct fix) |
| 22 | 2.2 GW bought in 2025; 765-kV awards in PJM, SPP, MISO (b:62) | Item 7; Q1 release p.2 | l.1857; l.63–70 | PASS ×2 |
| 23 | OCF $4–7B a year has not covered construction (b:66) | Item 8 | 3(d): OCF 3.8–6.9 vs capex 5.7–8.5 every year | PASS (wording tightened, direct fix) |
| 24 | Debt $36.1B → $52.8B; shares 504M → 544M (b:83) | 10-K FY2022; 10-Q | as 3(e) | PASS ×4 |
| 25 | $3B junior subordinated debentures at 5.80%–6.05%; agencies count half as equity (b:83) | 8-K 2025-09-25; Q2 slides p.32 | `8-K-2025-09-25` l.52 ($1.1B 5.800% + $0.9B 6.050%), `8-K-2025-12-05` l.52 ($0.4B + $0.6B add-on); deck p.32 l.947 and p.33 l.981 "Junior Subordinated Debentures (50%)" deducted from debt | PASS ×3 |
| 26 | 19.9% of Ohio and I&M transmission companies to KKR and PSP funds for $2.82B (b:83) | 10-K Note 7 | l.9146 | PASS |
| 27 | $3.5B ATM program (b:83) | 8-K 2025-11-25 | l.52; `10-Q` l.1777 | PASS |
| 28 | Forward sale 23,543,308 shares at $124.968, settle by May 2028 (b:83) | 8-K 2026-05-14 | l.54–60 (20,472,442 + 3,070,866; $124.968; "on or prior to May 31, 2028") | PASS ×3 |
| 29 | 45M shares, ~8% (computed), still to deliver (b:83) | 10-Q Note 12 | l.7997–7999; 45 / 544.4 = 8.3% | PASS ×2 |
| 30 | Plan: $47.1B OCF; $77.9B capital; $11.1B dividends; $45.5B debt; ~$9.7B equity (computed) (b:83) | Q2 slides p.24 | l.749–762; 900 + 4,000 + 4,800 = 9,700 | PASS ×5 |
| 31 | 5.8c / 5.2c operating profit per $ of net plant (computed) (b:85) | Item 8 | 5,319 / 92,374 = 5.76%; 4,304 / 82,416 = 5.22% | PASS ×2 |
| 32 | Earned ROE 9.2% TTM to June 2026; authorized 9.25%–10.5% (b:85) | Q2 slides p.28; Item 1 | l.841; l.522–541 (min 9.25% SWEPCo-Texas/WV, max 10.50% FERC OKTCo/SWTCo) | PASS ×2 |
| 33 | Plan ROE target 9.375%, actual 9.060%, score zero (b:85) | DEF 14A CD&A | l.1385 | PASS ×3 |
| 34 | FFO/debt target 14%–15%; 14.6% S&P; 14.0% Moody's; 13% downgrade threshold; filings state neither ratings nor a target (b:85) | Q2 slides p.31; 10-K Item 7 | l.912–918; "Moody" 0 hits, "BBB" 0 hits, "FFO" 0 hits in `10-K-FY2025.txt`; l.1200 and l.2983 discuss ratings only generically | PASS ×5 |
| 35 | June 2025 FERC NOLC order; $480M (~$0.90/share) excluded from operating earnings (b:87) | Q2 release p.7 | l.352 and l.474 ("FERC NOLC Order ... (480) ... (0.90)"); `10-Q` l.422 ("June 2025 FERC NOLC order") | PASS ×3, but **imprecise**: the 10-K (l.2043) says the orders added $499M to Q2 2025 earnings (years 2021–2025); the $480M is the 2021–2024 portion excluded from operating earnings. Fixed directly (see §13); this also settles the brief's "$480–499M" question |
| 36 | GAAP $1,226M → $713M; operating $766M → $742M; FY2025 GAAP EPS $6.70 vs operating $5.97 (b:87) | Q2 release p.3; Q4 2025 release p.1 | l.102–103; l.3 | PASS ×6 |
| 37 | Only named competition "self-generation" (b:91) | Item 1 | l.843 | PASS |
| 38 | WV ROE 9.25% → 9.75% on reconsideration; Kentucky settlement cut $22M; Oklahoma staff as low as 8.3% (b:91) | 10-Q Item 2; Note 4 | l.713; l.6261; l.6295 | PASS ×3 |
| 39 | Take-or-pay quote "as much as 80-90%"; five of eight jurisdictions approved (b:93) | 10-Q Item 2 | l.576 (four approved at March 31 + Virginia in Q2 = five; three pending) | PASS ×2 |
| 40 | "growth helps pay for growth"; "up to $16 billion in expected cost offsets for residential customers" (b:93) | Q2 release p.2; p.1 | l.62; l.36–37 | PASS ×2 |
| 41 | Pirkey $31M; Texas tracker $22M; 9.5% target (b:95) | Q2 release p.9; Q2 slides p.28 | l.428, l.431; l.838 | PASS ×3 (the 10-Q's $23M pretax added, direct fix) |
| 42 | "depend, in part, on the continued growth and viability of data centers and large load customers" (b:101) | Item 1A | l.1038 | PASS |
| 43 | 69 GW; 90% data centers; 45 GW Texas; LOAs only; Batch Zero decides 2026–2027; AEP Texas peak ~8 GW (b:101) | Q2 slides p.14, p.15; 10-Q Item 2 | l.382–420; l.422–449 ("current peak demand of approximately 8 GW"; August 2026 / April 2027); `10-Q` l.692 ("one-time transitional interconnection process") | PASS ×6 |
| 44 | $72B plan set when AEP Texas signed load was 13 GW; 13 GW of turbines secured (b:101) | Q4 2025 release p.1; Q2 release p.2 | l.38–39 ("increased from 13 GW to 36 GW"), l.45–52 (28 GW "not included in the current capital plan"); l.80–81 | PASS ×2 |
| 45 | "The increase in spending could trigger..."; "Customer affordability considerations..." (b:103) | Item 1A; 10-Q Forward-Looking Information | l.1060; `10-Q` l.384 | PASS ×2 |
| 46 | Kentucky $47M reclassified; Texas staff 9.6% vs SWEPCo 10.75% (b:103) | 10-Q Note 4 | l.6261; l.6305, l.6303 | PASS ×3 |
| 47 | Debt 61.4% of capital (b:105) | 10-Q Item 2 | l.1734 | PASS |
| 48 | "have approached, and may in the future approach, thresholds..." (b:105) | Item 1A | l.1200 | PASS |
| 49 | $45.5B planned borrowing; $1B a year ATM (b:105) | Q2 slides p.24 | l.762; l.760 | PASS ×2 |
| 50 | More than half of 2026 operating earnings from transmission (b:107) | Q2 slides p.5 | l.120–122 (">50% 2026 Operating Earnings from High-Growth Transmission Business") | PASS |
| 51 | "If the FERC were to adopt a different policy..."; "have been challenged, which could result in lowered rates and/or refunds" (b:107) | Item 1A | l.1076; l.1078 | PASS ×2 |
| 52 | $480M ruling under appeal (b:107) | 10-Q Note 4 | l.6343 ("petitions for review ... United States Court of Appeals for the District of Columbia Circuit") | PASS |
| 53 | PJM's July 2026 reforms "have the potential to materially impact AEP's competitive retail operations and could materially alter OPCo's cost allocations to retail customers" (b:109) | **10-Q Q2 2026, Item 2** | The sentence is in **`10-K-FY2025.txt` l.1901** (Item 7, "PJM Capacity Market Reform"), where it refers to the January 2026 Statement of Principles and a PJM Board decision letter. The 10-Q's July 2026 passage ("PJM Proposed Reforms", l.590–596) describes a Reliability Backstop Procurement, an Interim Resource Adequacy Service from June 1, 2027, a Large Load Registry and withdrawal provisions, and does not contain the quoted sentence (0 hits for "competitive retail operations" in the 10-Q) | **FAIL (wrong filing, wrong date)** — REVISE item 2 |
| 54 | CEO tone: "does not give me great confidence" (Q1) → "very optimistic" (Q2) (b:109) | Q1 call, Fehrman; Q2 call, Q&A, Truist | `transcript-2026-Q1` l.41 (Fehrman prepared remarks, speaker at l.13); `transcript` l.205 (Fehrman answering Richard Sunderland, Truist, l.199–201) | PASS ×2 |
| 55 | ~10,200 MW coal of 26,500 MW; coal-closure quote; storm costs "may not be recoverable"; $300M storm costs not earning a return (b:111) | 10-Q Item 2; 10-K Item 1A; 10-Q Note 4 | `10-Q` l.837; `10-K` l.2239; l.1254; `10-Q` l.5956–5957 ("Regulatory Assets Currently Not Earning a Return / Storm-Related Costs (a) \| 300 \| 191") | PASS ×5 |
| 56 | NRG and Vistra 38% of AEP Texas 2025 revenue; ~4% of consolidated (computed); no other registrant utility >10% (b:113) | 10-K Note 1 | l.7296–7302; AEP Texas revenue 2,199 (l.4067 area, AEP Texas income statement) × 38% / 21,876 = 3.8% | PASS ×3 (wording tightened to "the other five registrant utilities", which is what l.7296 says) |
| 57 | "hyperscale customers"; "AEP load data are not publicly disclosed for most projects" (b:113) | Q1 slides p.8; Q2 slides p.18 | l.221–223; l.518–520 (the sentence is interleaved with the "New data centers announced in 2026" label in the layout text) | PASS ×2 |
| 58 | Third CEO since 2022 after Sloat and Fowke; Mihalik from Sempra January 2025; team arrived 2025, several from BHE (b:117) | DEF 14A Pay Versus Performance; Item 1 | `DEF14A` l.2297; `10-K` l.1012–1015 (CFO since January 2025; Sempra 2018–2025); l.972–1005 (Berntsen Jul 2025 ex-BHE, Cannon Jun 2025 ex-NV Energy, Eckert Jul 2025, Knapp Sep 2025 ex-BHE Renewables) | PASS ×3 |
| 59 | Board twelve → ten in April 2026; two added July incl. Equinix's Charles Meyers (b:117) | DEF 14A Item 1; 8-K 2026-07-21 | l.179 ("consists of 12 members"), l.181 ("Ten directors are to be elected"); `8-K-2026-07-21` l.52, l.56 | PASS ×3 |
| 60 | Six equally weighted principles; every measure except Plan ROE above target; 162.5%; EPS $5.97 vs $5.90 target (b:119) | DEF 14A CD&A | l.1238; l.1377–1393 (scores 157.3%–200% on all but Plan ROE); l.1393; l.1392 | PASS ×4 ("at or near maximum" softened to "above target": DART 166.7% and TRIR 157.3% are not near the 200% maximum) |
| 61 | Fehrman pay $36.6M; $15M retention vesting Dec 31, 2030 (b:119) | DEF 14A SCT; 8-K 2025-12-19 | l.1655 (36,601,524); l.54–56 ($10M performance shares + $5M RSUs, December 31, 2030) | PASS ×2 |
| 62 | Say-on-pay ~96% (2025) → 82% (2026, computed); insiders under 1% (b:119) | DEF 14A CD&A; 8-K 2026-04-29; DEF 14A Share Ownership | l.1204; `8-K` l.106 (332,608,628 for / 70,774,562 against → 82.5%); `DEF14A` footnote (c) after l.2524 ("less than 1.0%") | PASS ×3 |
| 63 | Dividend $3.00 (2021) → $3.74 (2025); "462nd consecutive quarterly dividend" October 2025; payout target 50%–60% (b:121) | 10-K FY2023 Item 8; 10-K FY2025 Item 8; DEF 14A Executive Summary; Q2 slides p.24 | l.3536; l.3663; l.1159; l.772 | PASS ×4 |
| 64 | "$125 million for 12.5% of Gigawatt AI" (b:121) | 10-Q Note 13 | l.8380: "$100 million for a 10% ownership interest ... In January and April 2026, AEP made two additional $25 million investments, each for an incremental 2.5% interest ... as of June 30, 2026, AEP holds 15% of GWAI's common stock with a cumulative investment of $150 million" | **FAIL (wrong numbers)** — REVISE item 1 |
| 65 | $2.65B fuel-cell purchase; unnamed "high investment grade third party customer"; 20-year contract (b:121) | 8-K 2026-01-08 | l.54 ("approximately $2.65 billion, and (ii) a 20 year offtake arrangement with a high investment grade third party customer") | PASS ×3 |
| 66 | outlook §2–§3 quotes and figures: "Our future is all about growth..." (l.57, Fehrman); "One of the most important drivers..." (l.69, Mihalik); "As new large load comes online..." (l.43, Fehrman); UTM / SB 998 / test year and "9.5% by 2030" (l.67, Mihalik); "scarce resource" (l.233, Fehrman answering David Arcaro, Morgan Stanley, l.223–229); "clearly looking into the GenCo structure" (l.101, answering Shar Pourreza, Wells Fargo, l.93–99); 27 GW resource needs (deck p.25 l.798: 27,235 MW); "roughly about half" (l.213, Mihalik answering Richard Sunderland, Truist); Sycamore order December 2026 and Rockport Energy Center Q1 2027 (`10-Q` l.634, l.636); Holdco rate base $15B → $26B and Piketon $4.2B (deck p.21 l.664/663, p.22 l.688–690, l.628); five of eight states and "by end of 2026" (deck p.8 l.182–183) | as tagged | PASS ×12 |

**Prose tally: 66 checks (about 190 individual figures and quotes), 62 PASS, 4 FAIL** — items 35 and the outlook row-6 cell fixed directly; items 53 and 64 on the REVISE list. No tag points to a document dated after the cutoff. Neither gatherer note is at fault for item 64 (I did not consult the notes); the writer appears to have read the January 2026 increment and stopped before the April one.

**Citation tally overall:** 42 + 40 + 48 + 60 + 19 + 75 = **284 table and indicator cells, 283 PASS, 1 characterisation FAIL (fixed)**, plus 66 prose checks (62 PASS, 4 FAIL) and 98 quoted strings (all found, §4).

---

## 4. Verbatim-quote check

Every string inside double quotes of 10 or more characters in both files was normalised (curly quotes, dashes, whitespace) and searched across all cached texts joined line by line (`quotes.py`); short quotes (under 10 characters: "~95% ESAs", "~55% ESAs", "205 gigs") were checked by hand.

| Where | Strings | Exact match | Notes |
|---|---|---|---|
| business.md | 46 | 46 | "AEP load data are not publicly disclosed for most projects" is split by an interleaved chart label in `slides.txt` l.518–520 and was confirmed on the page dump; "not earning a return" is the 10-Q Note 4 table heading (l.5956) as well as 10-K text |
| outlook.md §1–§3 | 22 | 22 | Four deck labels are line-broken in the layout text ("$13B / 2026 Capital / Investment" Q1 p.5 l.115–119; "7 GW / Incremental Contracted / Load in 2026" l.131–133; "Maintaining FFO/Debt targeted / range of 14%-15% for 2026- / 2030" Q1 p.7 l.188–190; "targeting to obtain / approval of remaining tariffs by end of 2026" Q2 p.8 l.182–183); each confirmed on the page dump |
| outlook.md §4 guidance (8 bullets, 11 quotes) | 11 | 11 | Release p.1 l.19–26 and p.4 l.154–176 word for word, including the six reconciliation items 0.03 / (0.07) / 0.06 / 0.04 / 0.04 / (0.01); deck p.12 l.278–279; deck p.28 l.838; deck p.8 l.182–183; transcript l.41, l.27, l.83 |
| outlook.md §5 claim quotes | 14 | 14 | transcript l.265 (Mihalik, answering "Aidan" of JPMorgan, l.251–263), l.63, l.77, l.211, l.191, l.27, l.45; deck p.12; release p.1–2; `10-Q` l.6297, l.783 |
| outlook.md l.62 unsharpened figures | 5 | 5 | l.101 ("about 1.2 gigs", Wells Fargo exchange), l.155 ("205 gigs", Wolfe), l.133 ("100 gigawatts", Wolfe), l.189 ("10%-13%", Jefferies) |

No altered word in any quote. Speaker attributions: every prepared-remarks quote sits inside the right speaker's block (Fehrman l.27–61, Mihalik l.63–91 in the Q2 file; Fehrman from l.13, Mihalik from l.63 in the Q1 file); every Q&A tag names the analyst's firm as introduced by the operator (l.93 Wells Fargo, l.125 Wolfe, l.169 Jefferies, l.199 Truist, l.223 Morgan Stanley, l.251 JPMorgan). The Sources note's example of a wrong label is real: l.109 is labelled "Trevor Mihalik" and says "I'll let Trevor hop in here", answering Shar Pourreza (Wells Fargo).

---

## 5. Claims check (outlook.md §5)

Count: **11** (target 6–12). Mix: claims 1–2 are headline EPS; 3–4 segment earnings; 5–6 load and ERCOT; 7–8 capital; 9 credit; 10–11 rate-case disclosure checks. Headline EPS does not dominate. Every claim has its verbatim quote and tag beneath it.

| # | Single direction? | Can it fail? | One thing to check? | Quote supports? | Labels | Verdict |
|---|---|---|---|---|---|---|
| 1 | Yes (bottom ≥ $6.25) | Yes | Yes | Yes | n/a | OK |
| 2 | Yes (> $1.80) | Yes | Yes | Loosely ("Q3 has typically been our strongest quarter"); the claim is the writer's | Labelled "our sharpening, not management's number"; arithmetic shown | OK. Re-derived: FY2025 operating EPS $5.97 (Q4 2025 release l.3, l.105) − 6M 2025 $2.98 (Q2 release l.107) − Q4 2025 $1.19 (Q4 release l.13, l.105) = $1.80. Caveat for the grader: quarterly EPS figures do not sum exactly to the annual figure because share counts differ, so treat $1.80 as approximate to a cent |
| 3 | Yes (> $200M) | Yes | Yes | Yes ("favorable year-over-year by end of 2026" is a full-year statement; testing Q3 alone is a sharpening) | Labelled; arithmetic shown | OK. Re-derived: FY2025 Holdco operating earnings $807M (Q4 release l.122) − 6M 2025 $459M (Q2 release l.128) − Q4 2025 $148M (Q4 release l.122) = $200M. Dollar figures sum exactly, unlike EPS |
| 4 | Yes (loss < $115M) | Yes | Yes | Yes | Labelled sharpening | OK |
| 5 | Yes (≥ 69 GW) | Yes (or 🔇 if the deck drops it) | Yes | Yes | n/a | OK |
| 6 | Yes | Yes | Yes | Yes | Labelled sharpening; "40 GW is the 10-Q's figure" verified at `10-Q` l.692 ("approximately 40 gigawatts of prospective load seeking consideration under ERCOT's Batch Zero process"); ERCOT's eligibility list is due August 2026 (deck p.15 l.428) | OK |
| 7 | Yes | Yes | Yes | Yes (l.211: "we anticipate that we would have executed docs in the third quarter") | n/a | OK |
| 8 | Yes (> $78B) | Yes | Yes | Yes | n/a | OK |
| 9 | Yes (≥ 14.0%) | Yes | Yes | Yes | n/a | OK |
| 10 | Yes | Yes | Yes | Yes (`10-Q` l.6297) | Labelled disclosure check; "quarter" stated | OK |
| 11 | Yes | Yes | Yes | Yes (l.45 call; `10-Q` l.783) | Labelled disclosure check; "quarter" stated | OK. Precision note for the writer (optional): the 10-Q calls the filing "an Indiana MYRP" (multi-year rate plan) with a notice of intent to file "no later than September 1, 2026"; the claim's "base-rate case seeking a rate decrease" is the CEO's description ("base rate reduction filing") and is fine, but naming the MYRP would make the check unambiguous |

No either/or, no double-barreled claim with an unobservable half, no vague statement presented as a claim. The writer's flagged Q3 2025 baselines (claims 2–3) are correct and the claims say how they were computed. Rubric Q4 passes.

---

## 6. Jargon audit

Reader: a smart 16-year-old with no finance background. Terms found that were neither plain, name-inferable nor in the Glossary, and the action taken (all direct fixes; before → after in §13):

| File:line | Term | Action |
|---|---|---|
| business.md:8 | FERC (never expanded) | glossed "the federal energy regulator" |
| business.md:10 | "loss contingency" | glossed "an expected settlement cost" |
| business.md:39 | depreciation | glossed at first use |
| business.md:41 | "rate cases"; "PJM and SPP" (first use, before l.62's "grid operators") | glossed |
| business.md:45 | gross margin; operating margin | glossed |
| business.md:87 | GAAP; EPS | glossed |
| business.md:93 | tariffs (a reader may think of trade tariffs) | glossed "approved price schedules" |
| business.md:95 | disallowances | glossed |
| business.md:103 | SWEPCo | expanded |
| business.md:119 | say-on-pay | glossed |
| business.md:121 | "high investment grade" (inside a quote) | glossed outside the quote |
| business.md:129 | I&M | expanded |
| outlook.md:13 | ERCOT / PJM / SPP | "the three grid operators" |
| outlook.md:14 | I&M | expanded |
| outlook.md:15 | PSO | expanded |
| outlook.md:17 | ATM (inside a quote) | glossed outside the quote |
| outlook.md:39 | EPS | expanded |
| outlook.md:40 | WVPSC | "West Virginia commission" |
| outlook.md:62 | TSR | "total shareholder return" |

Already plain or glossed by the writer, no action: rate base, authorized/earned ROE, regulatory lag, rider/tracker/formula rate, FFO/debt, take-or-pay (all Glossary); holding company, franchise, kilowatt-hour, circuit miles, kV, MW/GW (name-inferable); junior subordinated debentures, at-the-market program, forward sale, hyperscale, letter of agreement, ESA, Batch Zero, UTM, SB 998, test year, GenCo, mark-to-market (glossed inline by the writer); "moat" (the owner's own framework word). OPCo appears only inside the PJM quote at business.md:109, which the writer is reworking (REVISE item 2); add "(AEP Ohio)" after the quote when doing so.

**Glossary (6 entries):** rate base, authorized ROE, regulatory lag, rider/tracker/formula rate, FFO/debt, take-or-pay minimum. Each one sentence, each unavoidable and used repeatedly. None should be cut; none needs adding after the inline glosses above.

**Analogy pile-up:** none; the report uses almost no analogies. **Banned-word scan** outside quotes (leverage, synergy, headwind, tailwind, ecosystem, robust, unlock): none; "robust" and "leveraging" occur only inside release quotes.

---

## 7. Invented-number check

No figure was found without a source tag or with a tag that does not contain it, except the two REVISE items. Specific checks:

| Item | Finding |
|---|---|
| Every "(computed)" cell and ratio | Re-derived: purchased power/revenue ×6, operating margin ×6, capex/revenue ×6, FCF ×6, net debt raised ×6, Q2 construction 2,776, Q1 forwards $2.1B, 5.8c/5.2c per $ of plant, 8% of shares, ~$9.7B equity, 82% say-on-pay, ~4% concentration, +5%/+7% kWh, 28% commercial, 32% fuel share. All correct |
| Numbers taken from the machine transcript | None presented as numbers. The four spoken figures the writer chose not to use (1.2 GW, 205 GW, ~100 GW, 10%–13% TSR) are quoted as wording in outlook l.62 and labelled as such; the TSR figure is in fact on deck p.5 (l.105), so the sentence's "absent from the release and slides" was wrong for that item — fixed directly |
| Numbers from documents after the cutoff | None. Every tag maps to a file dated on or before 2026-07-30; the June 2026 handout is not cited |
| "not reported" / "not disclosed" cells | Gross margin ×6 (verified absent); "no buyback program is disclosed" (verified: no repurchase line, treasury unchanged); "the filings state neither ratings nor a target" (verified: no Moody's/S&P/FFO figure in the 10-K); "the filings name no customer, give no MW per customer and no contracted total outside Texas" (verified: the 10-Q's only MW-by-customer figure is the 40 GW / 45 GW Texas aggregate at l.692; the deck says "AEP load data are not publicly disclosed for most projects") |
| Unlabelled inferences | b:101 "so most Texas load is upside not yet in the plan" rests on the Q4 2025 release's own sentence (l.51–52: the 28 GW "are not included in the current capital plan"), so it is sourced, not inferred. b:66 "For a growing regulated utility that is normal" is framing, not a fact. No estimate presented as fact |
| The $480M / $499M FERC NOLC item | Both are real: $499M is the total Q2 2025 earnings effect (10-K l.2043, years 2021–2025); $480M is the 2021–2024 portion excluded from operating earnings (release l.352, l.474; 10-Q l.501). The draft used $480M as if it were the whole GAAP effect; fixed directly and explained once, as the brief asked |
| The $22M / $23M Texas UTM disallowance | Release reconciliation shows 22 pretax with tax effect separate (l.314, l.431); 10-Q Item 2 l.735 says "an unfavorable pretax impact of $23 million". The draft used $22M with the release tag; the 10-Q figure is now shown beside it (direct fix) |

---

## 8. Owner's asks — coverage

| Ask | Where | Verdict |
|---|---|---|
| How a regulated utility earns money (rate base, allowed return, regulatory lag, formula rates) | business.md §2 l.39–41, with the 10-K's own sentences and the FERC formula-rate mechanics; Glossary | Yes, plain and correct |
| Why capex exceeds operating cash flow and is funded with debt and equity | §3 l.60 ("spends far more than it depreciates"), §4 l.66 and table, §4 l.83 (instruments), §6 scenario 3 | Yes |
| $72B (FY2025 10-K) vs $78B (2026 10-Qs/decks) | §3 l.60 gives both with dates and the per-period splits ($12.2B + $59.7B; $12.8B + $65.1B); §7 table repeats the move | Yes |
| The one-time ~$480–499M FERC NOLC benefit explained once | §4 l.87 "One-off item to read past" (now with both figures); §2 footnote points to it | Yes |
| Segment profit-measure change footnoted | §2 l.37 | Yes |
| Guidance quoted verbatim and treated as claims | outlook §4 (eight verbatim bullets) and §5 claims 1, 3, 5, 8, 9 | Yes |
| Data-center load and rate cases as the things to watch | §8 indicators 3, 4, 6; §6 scenarios 1–2; outlook §3 engines 1 and 4 | Yes |
| "Not disclosed" where sources are silent | §3 gross margin; §4 buybacks; §4 ratings/target; §6 concentration (no customer named, no MW per customer) | Yes |

---

## 9. Source conflicts the writer reported — rulings

| Conflict | Ruling |
|---|---|
| (a) UTM disallowance $23M pretax (10-Q) vs $22M (release) | **Both verified** (`10-Q` l.735; release l.314/l.431). Using the release figure with the release tag was honest but silent; the 10-Q figure is now shown beside it (direct fix). The 10-Q figure is in Item 2, not Note 4 as the brief assumed |
| (b) FY2022 balance sheet differs between the FY2022 and FY2023 10-Ks; FY2022 10-K used only for 2021-12-31 | **Acceptable.** The draft takes 2021-12-31 net plant (66,001.3), debt (36,068.5) and shares (504.2M) from the FY2022 10-K (l.4148, l.4183–4196, l.4220–4221) and says so in Sources l.161. No FY2022 figure in the tables comes from the FY2022 10-K, so the reclassification does not touch the tables |
| (c) Take-or-pay "as much as 90%" (10-K l.1877) vs "80-90%" (10-Q l.576) | **Both verified.** The draft quotes the later filing with its tag. Honest as written |
| (d) Transmission mileage 38,000 (10-K FY2025 l.1675) vs 40,000 (proxy l.556, release l.210, 10-K FY2023 l.1716) | **Both verified.** The draft uses the 10-K FY2025 count with its tag and does not mention 40,000; acceptable, since the proxy and release count "line miles" and the 10-K "circuit miles" |
| (e) "13 GW to 36 GW" Texas baseline anchored to the Q4 2025 release | **Verified** (l.38–39); the transcript (l.133) has the CFO saying the plan "was based on a 13 gigs of interconnection in Texas", consistent |
| (f) Wells Fargo Q&A answer attributed to "management" | **Correct.** l.109 is labelled Mihalik and says "I'll let Trevor hop in here"; the draft's "(speaker label unreliable)" and the Sources note are right |

---

## 10. Readability

- **Paragraphs that are mostly numbers (§3 rule 5):** business.md l.83 ("Where the money came from") carries 14 figures in five sentences, most of them repeated in the §7 table eight lines later (debt, shares, forwards, minority stake, plan). This is the one wall of numbers in the report and the writer's own cut candidate — REVISE item 3. l.85 (return on capital) and l.87 (the one-off item) are number-dense but each figure is explained and they are short; acceptable. l.14 ("Who pays") is one sentence with eight figures doing the job of a table; acceptable because it is the revenue split the owner asked for.
- **Sentences needing finance background:** none remain after the glosses. The hardest idea in the report (a forward sale fixes the price now and delivers shares later) is explained in the sentence that introduces it.
- **Analogies:** none to pile up.

---

## 11. As-of check

Both drafts were scanned for every month-year and quarter label. Everything after July 2026 is a forward-looking statement quoted from a pre-cutoff source: August 2026 and April 2027 (ERCOT Batch Zero timeline, deck p.15), September 1 and September 30, 2026 (10-Q l.783, l.6297), December 2026 (Sycamore order, 10-Q l.634), Q1 2027 (Rockport Energy Center, l.636), Q3/Q4 2026 (expected rate orders, Q1 deck p.30), May 2028 (forward settlement, 8-K), 2030–2035 targets. "July 2026" at business.md l.109 refers to the PJM Board action disclosed in the 10-Q (l.592), which is pre-cutoff, although the sentence it is attached to is mis-sourced (REVISE item 2). Nothing is sourced to the August 2026 handout or to any Q3 2026 material; the June 2026 handout is cached but uncited.

---

## 12. Verdict: REVISE

Items 1–2 are factual; item 3 is the §3 rule 5 trim; item 4 is optional precision.

1. **business.md l.121 — Gigawatt AI stake.** "$125 million for 12.5% of Gigawatt AI" → "$150 million for 15% of Gigawatt AI". `10-Q-2026-Q2.txt` l.8380 (Note 13): $100M for 10% in August 2025, then two $25M investments (January and April 2026) for 2.5% each, "as of June 30, 2026, AEP holds 15% of GWAI's common stock with a cumulative investment of $150 million"; two further milestones were confirmed in July 2026. Keep the tag.
2. **business.md l.109 — PJM quote.** The sentence "have the potential to materially impact AEP's competitive retail operations and could materially alter OPCo's cost allocations to retail customers" is `10-K-FY2025.txt` l.1901 (Item 7, "PJM Capacity Market Reform"), where it refers to the January 2026 Statement of Principles and the PJM Board's decision letter, not to "PJM's July 2026 reforms". The 10-Q's July 2026 passage ("PJM Proposed Reforms", l.590–596) does not contain it. Either (a) retag to `[10-K FY2025, Item 7]` and describe the reforms as the capacity-market changes under way since January 2026, or (b) keep "July 2026" and quote the 10-Q's own words (Reliability Backstop Procurement; an Interim Resource Adequacy Service that AEP's distribution utilities "would be required to administer" from June 1, 2027; provisions on a transmission owner's withdrawal from PJM, l.596, which also supports the scenario's early warning "AEP proposing to leave PJM"). Add "(AEP Ohio)" after "OPCo" if the quote stays.
3. **business.md l.83 — "Where the money came from".** Fourteen figures in five sentences, most duplicated in the §7 table (l.123–131). Cut to the instruments and what each means in plain words (debentures counted half as equity; the 19.9% stake sale; the at-the-market programme; the forward sale that fixes the price now and delivers shares by May 2028) and drop the duplicated totals, or move the remaining figures into the table. This is the writer's own cut candidate and also restores headroom: the file is at 2,913 after my glosses against a 3,000 ceiling.
4. **outlook.md l.60 claim 11 (optional).** The 10-Q (l.783) calls the filing "an Indiana MYRP" (multi-year rate plan) with a notice of intent to file "no later than September 1, 2026"; consider "I&M files its Indiana multi-year rate plan (which the CEO calls a 'base rate reduction filing') by September 1, 2026" so the grader knows what document to look for.

Not required: consider whether indicator 4 (contracted GW from the deck) should carry a note in §8 that it is a deck KPI, not a filing line, so the owner locks it knowingly.

---

## 13. Direct fixes made by the reviewer (before → after) and word counts

Applied with `/tmp/aep-orch/reviewer/apply_fixes.py` (each old string asserted to occur exactly once). No number was changed except where the source was verified and is cited beside it; no claim, indicator, table value or structure was altered.

**business.md**

1. l.8: "state commissions (or FERC, for transmission) set their prices" → "state commissions (or FERC, the federal energy regulator, for transmission) set their prices".
2. l.10: "shareholder suits were dismissed, and an SEC investigation ended in a $19 million loss contingency in 2024, with nothing further disclosed" → "shareholder suits were dismissed (one appeal was pending when last disclosed), and an SEC investigation led AEP to book a $19 million loss contingency (an expected settlement cost) in 2024, with nothing further disclosed" (`10-K-FY2023` l.1972: consolidated derivative actions dismissed with prejudice March 2023, one notice of appeal April 2023; `10-K-FY2025` l.2844).
3. l.39: "depreciation, taxes, interest" → "depreciation (the yearly charge that spreads a plant's cost over its life), taxes, interest".
4. l.41: "rate cases "have long timelines" → "rate cases (the formal proceedings in which a commission resets prices) "have long timelines"; ""PJM and SPP pay the transmission owners" that amount" → ""PJM and SPP pay the transmission owners" (the regional grid operators) that amount".
5. l.45: "AEP reports no gross margin." → "AEP reports no gross margin (revenue less direct costs)."; "Operating margin therefore tracks approved investment, not efficiency: 19% in 2023, 24% in 2025 as rate cases and transmission additions came through [10-K FY2025, Item 7]." → "Operating margin (operating profit as a share of revenue) therefore tracks approved investment, not efficiency: 19% in 2023, 24% in 2025 (computed) as rate cases and transmission additions came through [10-K FY2025, Item 8]." (the percentages are computed from the Item 8 statements; 18.7% and 24.3%).
6. l.62: "grew 28% in 2025 on" → "grew 28% in 2025 (computed) on" (46,187 / 36,147 from the Item 7 KWh table, l.2530).
7. l.66: "has never covered construction" → "has not covered construction in any of the last five years" (the table covers five years; "never" was unsupported).
8. l.76 table row: "Net debt raised (issued less repaid, incl. short-term) | ... | 3,987 (computed)" → "Net debt raised (computed: issued less repaid, incl. short-term) | ... | 3,987" (every cell in the row is computed).
9. l.87: "adding $480 million (about $0.90 a share) to Q2 2025 GAAP earnings, which management excludes from "operating earnings", its non-GAAP measure [Q2 2026 release, p.7]." → "adding $499 million to Q2 2025 GAAP earnings (GAAP: the official accounting rules); management excludes the $480 million (about $0.90 a share) that relates to 2021–2024 from "operating earnings", its non-GAAP measure [10-K FY2025, Item 7] [Q2 2026 release, p.7]." (`10-K-FY2025` l.2043; release l.352, l.363); "FY2025 GAAP EPS of $6.70" → "FY2025 GAAP EPS (earnings per share) of $6.70".
10. l.93: "New data-center tariffs carry" → "New data-center tariffs (approved price schedules) carry".
11. l.95: "disallowances growing beyond 2026's small ones (Pirkey plant $31 million, Texas tracker $22 million); FERC reopening transmission ROEs [Q2 2026 slides, p.28] [Q2 2026 release, p.9] [10-K FY2025, Item 1]." → "disallowances (costs regulators refuse to put into rates) growing beyond 2026's small ones (Pirkey plant $31 million; Texas tracker $22 million in the release, $23 million pretax in the 10-Q); FERC reopening transmission ROEs [Q2 2026 slides, p.28] [Q2 2026 release, p.9] [10-Q Q2 2026, Item 2] [10-K FY2025, Item 1]." (`10-Q` l.735).
12. l.103: "against SWEPCo's 10.75% request" → "against SWEPCo's (Southwestern Electric Power's) 10.75% request".
13. l.113: "no other AEP utility has a customer above 10%" → "none of the other five registrant utilities has a customer above 10%" (`10-K-FY2025` l.7296 covers APCo, I&M, OPCo, PSO and SWEPCo only).
14. l.119: "every measure except "Plan ROE" scored at or near maximum" → "every measure except "Plan ROE" scored above target" (DART 166.7%, TRIR 157.3% against a 200% maximum, `DEF14A` l.1380–1383); "Say-on-pay support fell" → "Say-on-pay (the advisory shareholder vote on executive pay) support fell".
15. l.121: ""high investment grade third party customer" under a 20-year contract" → ""high investment grade third party customer" (one with a strong credit rating) under a 20-year contract".
16. l.129 table: "(19.9% of Ohio and I&M transmission companies)" → "(19.9% of the Ohio and Indiana Michigan transmission companies)".

**outlook.md**

1. l.13: "(ERCOT / PJM / SPP)" → "(ERCOT / PJM / SPP, the three grid operators)".
2. l.14: "(I&M 12.7% to Kentucky Power 4.1%)" → "(I&M, i.e. Indiana Michigan Power, 12.7% to Kentucky Power 4.1%)".
3. l.15 Q2 cell: "Completed: Ohio $11M at 9.84% (April 2026). Pending: Texas settlement in principle; PSO partial settlement at 9.375%; Virginia case filed May 2026" → "Completed: none new; the 10-Q's completed-case table is unchanged from Q1 (Ohio $11M at 9.84%, effective April 2026, was already listed there). Pending: SWEPCo Texas settlement in principle; PSO (Public Service Company of Oklahoma) partial settlement at 9.375%; Virginia case filed May 2026" (`10-Q-2026-Q1` l.623 already lists the Ohio row; `10-Q-2026-Q2` l.708–711 is identical).
4. l.15 Q1 cell: "West Virginia $91M at 9.75%; Arkansas $85M at 9.65%; Kentucky $55M at 9.75%" → "...; Kentucky $55M at 9.75%; Ohio $11M at 9.84%" (`10-Q-2026-Q1` l.620–623).
5. l.17: ""$1 billion of ATM in 2026, of which $665 million is already issued"; "Growth Equity"" → ""$1 billion of ATM in 2026, of which $665 million is already issued" (ATM: at-the-market share sales); "Growth Equity"".
6. l.39: "**2026 operating EPS:**" → "**2026 operating EPS (earnings per share):**".
7. l.40: "WVPSC order $(0.07)" → "WVPSC (West Virginia commission) order $(0.07)".
8. l.62: "Not sharpened (machine-transcript figures absent from the release and slides): a West Virginia project of "about 1.2 gigs", "205 gigs" of ERCOT-eligible load, "almost 100 gigawatts in Texas" behind the 45 GW, and a "TSR of 10%-13%" [Q2 2026 call, Q&A, Wells Fargo] [Q2 2026 call, Q&A, Wolfe Research] [Q2 2026 call, Q&A, Jefferies]." → "Not sharpened (machine-transcript figures absent from the release and slides): a West Virginia project of "about 1.2 gigs", "205 gigs" of ERCOT-eligible load and "almost 100 gigawatts in Texas" behind the 45 GW [Q2 2026 call, Q&A, Wells Fargo] [Q2 2026 call, Q&A, Wolfe Research]. The "TSR of 10%-13%" (total shareholder return) is also on the deck, as a 2026–2030 expectation that cannot be checked next quarter [Q2 2026 call, Q&A, Jefferies] [Q2 2026 slides, p.5]." (deck p.5 l.105–107 "~10%-13% Total Annual Expected Shareholder Return (TSR)").

No typos found. All 98 quoted strings re-verified after the edits (93 by the sweep, 5 line-broken deck labels by hand).

**Withdrawals:** none. Two provisional failures were withdrawn before being recorded as such: "not earning a return" (business.md l.111) looked absent from the 10-Q because the sweep printed only the first three matching files; it is the 10-Q Note 4 table heading at l.5956 with "Storm-Related Costs (a) | 300 | 191" beneath it. "AEP load data are not publicly disclosed for most projects" (l.113) looked absent from `slides.txt` because a chart label is interleaved between "publicly" and "disclosed" at l.518–520; the page dump shows the full sentence.

**Word counts** (`python3 -P /tmp/aep-orch/wc_prose.py`, §3 rule 7 basis): business.md **2,802 → 2,913** (ceiling 3,000; REVISE item 3 should bring it back toward 2,800), outlook.md **1,103 → 1,128** (ceiling 1,200).


---

## Cycle 2 (re-check of the writer's second pass, 2026-09-09)

_Same as-of rule observed: nothing outside `sources/2026-Q2/` was opened. Line numbers refer to the cached `.txt` files and to the drafts as they now stand (business.md 179 lines, outlook.md 76 lines; no line was added or removed by either pass). Method: the post-cycle-1 versions were rebuilt in scratch from `business.orig.md` / `outlook.orig.md` plus `apply_fixes.py`, and diffed against the files on disk; the diff shows exactly four changed lines (business.md l.83, l.109, l.121; outlook.md l.60) and nothing else, so every cycle-1 direct fix is still in place. This is the second and last review cycle allowed by AGENTS.md §13._

**Final verdict: PASS.** All four REVISE items were resolved and each re-verified against the cited source lines; the new quotes are verbatim; the new computed sentence re-derives from figures that are on the cited deck page; the quote sweep, tag-prefix check and as-of scan are clean; both files are inside their ceilings. Three small precision edits were made directly (below).

### 1. REVISE list — resolution

| # | Item | Now reads | Re-check | Result |
|---|---|---|---|---|
| 1 | b:121 Gigawatt AI stake | "$150 million for 15% of Gigawatt AI ... [10-Q Q2 2026, Note 13]" | `10-Q-2026-Q2.txt` l.8380: $100M/10% (Aug 2025) + $25M/2.5% (Jan 2026) + $25M/2.5% (Apr 2026) = "15% ... cumulative investment of $150 million" as of June 30, 2026; l.8380 lies inside Note 13 (l.8298–8391) | **Resolved** |
| 2 | b:109 PJM quote | 10-K sentence now attributed to "capacity-market reforms launched by a January 2026 Statement of Principles" with `[10-K FY2025, Item 7]` and "(OPCo is AEP Ohio)"; a new sentence gives the 10-Q's July 2026 reforms with `[10-Q Q2 2026, Item 2]` | `10-K-FY2025.txt` l.1899 ("In January 2026 ... jointly released a Statement of Principles"), l.1901 (quote, verbatim). `10-Q-2026-Q2.txt` l.592 ("In July 2026, the PJM Board approved near-term resource adequacy reforms ... Reliability Backstop Procurement mechanism and an Interim Resource Adequacy Service"), l.594 ("beginning June 1, 2027, electric distribution utilities would be required to administer an Interim Resource Adequacy Service"), l.596 ("provisions intended to mitigate impacts associated with a transmission owner's withdrawal from PJM"). All three quoted fragments verbatim; OPCo = AEP Ohio per Note 8 l.6665 and release p.3 footnote (b). The early warning "AEP proposing to leave PJM" now has the l.596 passage behind it | **Resolved** |
| 3 | b:83 "Where the money came from" (§3 rule 5) | Rewritten as instruments in plain words; two computed ratios replace fourteen figures; totals live in the §7 table | Instruments: debentures "due 2056" (`8-K-2025-09-25` l.52) with the 50% equity credit on deck p.32 l.947 / p.33 l.981; 19.9% stake (`10-K-FY2025` l.9146); ATM (`8-K-2025-11-25` l.52); forward at $124.968 by May 2028 (`8-K-2026-05-14` l.54–60); 45M shares / 8% (`10-Q` l.7997–7999; 45/544.4). "Share count has risen every year": year-end shares outstanding 504,212,015 (2021, `10-K-FY2022` l.4220–4221) → 513,866,081 (2022, `10-K-FY2023` l.3654–3655: 525,099,321 − 11,233,240) → 526,184,585 (2023: 527,369,157 − 1,184,572) → 532,907,715 (2024, `10-K-FY2025` l.3778–3779) → 540,861,473 (2025) → 544,362,629 (6/30/2026, `10-Q` l.2199–2200); true, but the 2022–2023 counts are in the FY2023 10-K, which the sentence did not tag (direct fix 1). Plan ratios from deck p.24 l.749–762: 47,100 / (77,900 + 11,100) = 52.9% ("about half", correct); net new debt 45,500 − 11,000 maturities − 1,200 securitization amortization = 33,300 against equity 900 + 4,000 + 4,800 = 9,700, and 33,300 + 9,700 = 43,000 = the deck's "Required Capital", so the basis is right; the ratio is 3.43, which the draft rounded to "about three" (direct fix 3 makes it "about three and a half"). The "so" linking the May 2026 forward to the 45M shares overstated: 24M of the 45M are the May 2026 sale, 18M the March 2025 forward and 3M ATM forwards (l.7997–7999; direct fix 2). The paragraph is now three sentences with four figures; §3 rule 5 satisfied | **Resolved** (with two wording fixes) |
| 4 | o:60 claim 11 (optional) | "I&M files its Indiana multi-year rate plan (MYRP), which the CEO calls a "base rate reduction filing", by September 1, 2026 (disclosure check, Q3 10-Q; quarter)." with the 10-Q quote extended and IURC glossed | `10-Q-2026-Q2.txt` l.783: "In July 2026, I&M submitted a notice of intent to file an Indiana MYRP with the IURC no later than September 1, 2026." — verbatim; `transcript.txt` l.45 for the CEO's wording. Still one sentence, single direction, labelled disclosure check, "quarter" stated | **Resolved** |

### 2. Re-checks

- **Cycle-1 direct fixes:** all 28 present (diff of the rebuilt post-cycle-1 files against disk shows only the writer's four lines).
- **Quote sweep** (`quotes.py`): 97 strings found verbatim; the only non-hits are the same five line-broken deck labels confirmed by hand in cycle 1 (Q1 p.5 l.115–119 and l.131–133, Q1 p.7 l.188–190, Q2 p.8 l.182–183, Q2 p.18 l.518–520). New strings checked individually: "Reliability Backstop Procurement mechanism" (l.592), "Interim Resource Adequacy Service" (l.592, l.594), "would be required to administer" (l.594), "notice of intent to file an Indiana MYRP with the IURC no later than September 1, 2026" (l.783), "Statement of Principles" (`10-K` l.1899).
- **Tag prefixes:** every tag in both files maps to a Sources entry (including the new `[10-K FY2025, Item 7]` use at l.109 and the `[10-K FY2023, Item 8]` I added at l.83).
- **As-of:** month-year and quarter labels in both files re-scanned. New mentions: "January 2026" (the Statement of Principles, `10-K-FY2025` filed 2026-02-12) and "June 1, 2027" (a proposed start date quoted from the 10-Q). Everything after July 2026 remains a forward-looking statement from a pre-cutoff source; the handout is still uncited.
- **Headers:** `_As of Q2 2026. Written 2026-09-09._`, `_Transcript source tier: third-party (The Motley Fool). Written 2026-09-09._`, `_Proposed — owner to review and lock._` (l.135) all present; outlook §6 absent.
- **Claims and indicators:** unchanged apart from claim 11's wording; still 11 claims, 8 indicators, one row per indicator in outlook §1.

### 3. Direct fixes made in cycle 2 (before → after)

business.md l.83 only:
1. Tag: "plus a share count that has risen every year (§7 table) [10-K FY2022, Item 8] [10-K FY2025, Item 8] [10-Q Q2 2026, Item 1]." → "... [10-K FY2022, Item 8] [10-K FY2023, Item 8] [10-K FY2025, Item 8] [10-Q Q2 2026, Item 1]." (the 2022 and 2023 year-end counts are only in the FY2023 10-K, l.3654–3655).
2. Precision: "shares delivered for cash by May 2028, so 45 million shares (about 8% of the count, computed) were still to be issued at June 30, 2026" → "shares delivered for cash by May 2028; with the 2025 forwards, 45 million shares (about 8% of the count, computed) were still to be issued at June 30, 2026" (`10-Q` l.7997–7999: 18M March 2025 forward + 3M ATM forwards + 24M May 2026 forward).
3. Precision: "about three dollars per dollar of new shares" → "about three and a half dollars per dollar of new shares" (33,300 / 9,700 = 3.43, deck p.24 l.756–762).

No trim was needed. No numbers, quotes, claims, indicators or structure were changed.

### 4. Final word counts

`python3 -P /tmp/aep-orch/wc_prose.py` (§3 rule 7 basis): **business.md 2942** (writer's second pass 2,936; ceiling 3,000), **outlook.md 1150** (ceiling 1,200). History: business.md 2,802 (hand-off) → 2,913 (cycle-1 glosses) → 2,936 (writer's second pass) → 2942; outlook.md 1,103 → 1,128 → 1,150 → 1150.

**Verdict: PASS.** Ready for the owner to review and lock the §8 indicators.
