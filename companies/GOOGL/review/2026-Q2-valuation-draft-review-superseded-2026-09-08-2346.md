# Alphabet (GOOGL) — Valuation draft review, as of Q2 2026

_This reviews the 2026-09-08 redraft of `valuation/assumptions.yaml` (`drafted: 2026-09-08`, `horizon: 10`, five explicit years per list), which replaced the 2026-09-07 draft that passed review and was then edited by the owner through the app. The archived previous pair is `valuation/history/2026-09-08-0150/`. Written 2026-09-08 per AGENTS.md §18.7 step 4. Nothing was fetched from the internet; every figure below was re-derived from the cached files under `sources/2026-Q2/` and `sources/2026-Q1/` and from the cached Damodaran datasets the engine reads. No value per share, upside or enterprise value is recorded anywhere in this file: the owner meets those in the app._

**Cycle 1 verdict: REVISE** — one numbered item (§6). Everything else re-derived; the wording, source-tag and formatting defects are fixed directly in the YAML and listed in §7. **Cycle 2 verdict: PASS** — see §8, appended 2026-09-08 after the analyst applied item 1.

---

## 1. Base-year and bridge numbers

`diff` of the two files (`diff -u history/2026-09-08-0150/assumptions.yaml assumptions.yaml`) shows the whole of `base_year:` and the whole of `bridge:` byte-identical, and `market:`, `cost_of_capital.build:` byte-identical. **Those cells are unchanged since the passed review of 2026-09-07 and are not re-checked here.** In particular `market.mature_market_erp: 0.04` is the owner's own saved value and the draft preserved it.

Six things did change outside the scenarios, and all six re-check:

| Cell | Draft | Re-derived / rule | Result |
|---|---|---|---|
| `horizon` | 5 to 10 | §18.2 default: five explicit years plus a five-year fade by rule. All `values` lists carry exactly five entries. | OK |
| `switches.reinvestment_lag` | added, 1 | §18.4 default; the sales-to-capital history in every `detail` is measured lagged the same way (§3 below). | OK |
| `cost_of_capital.terminal.reason` | "the 4 per cent mature-market premium the owner set" | Matches `market.mature_market_erp: 0.04`. Engine terminal cost of capital 8.75% = 4.75% + 4.00%. | OK |
| `diagnostics.final_year_market_size.detail` | year-10 revenue: bear about 1,003,000; base about 1,472,000; bull about 1,841,000 | Recomputed by hand from each written five-year path plus the §18.2 linear fade to a 4.75% terminal growth: bear 1,002,714 (2.25x the base year); base 1,472,058 (3.30x); bull 1,841,206 (4.13x). Engine agrees on the base at 1,471,872. | OK |
| `diagnostics.historical_revenue_cagr.reason` | advertising 81% of revenue in 2021, 73% in 2025, 71% in the base year | 2021: (149.0 + 28.8 + 31.7) / 257.6 = 81.3%. 2025: 294,691 / 402,836 = 73.2%. Base year: 315,348 / 445,866 = 70.7%. | OK |
| `diagnostics.historical_operating_margin.reason` | "the base case's 32 to 33%" | Matches the base path 33, 33, 32, 32, 32. | OK |

Every new number inside the scenarios is re-checked in §3. **No base-year or bridge failures.**

## 2. The 3P test on each story

| Case | Possible | Plausible | Probable (against the scorecard) | Verdict |
|---|---|---|---|---|
| Bear | Yes. Year-10 revenue 1,003,000, 2.3 times the base year, and year 5 is 1.71 times. Nothing in the cached sources bounds a market this size, and `final_year_market_size` is honestly left empty; the near years sit *below* the contracted floor of about 257,000 of order book due inside 24 months, so the case cannot be ruled impossible. | Yes. A 27% margin with depreciation at 16.9% of revenue and single-digit growth is arithmetic, not hope, and the bridge shows it. The one strain is year 1 (see §6). | Yes as a downside. The scorecard's Q2 2026 grades show management met its capex and Cloud claims and only *partly* met the Search and capacity claims (claims 8 and 11 both 🟡), which is exactly where this case attacks. | PASS |
| Base | Yes. Year-10 revenue 3.3 times the base year; the first two years' Cloud revenue of 323,275 sits 26% above the contracted 257,000, which the "exceeding their commitments by more than 50%" disclosure and the exclusion of cancellable contracts cover [Q2 2026 call, p.4] [10-Q Q2 2026, Note 2]. | Yes. Revenue economics from `business.md` §3 and the segment margins from §3's table both support the offsets; the margin gives up only a point because two named offsets nearly cover an eight-point depreciation drag. | Yes. Seven of eleven Q2 2026 claims met, the capex range raised rather than trimmed, backlog up more than 50,000 in one quarter. | PASS |
| Bull | Yes, at the edge. Year-10 revenue 4.1 times the base year and Cloud at 41% of the company in year 5; unbounded by any cached market size, which is this case's honest weak point. | Yes, narrowly. A 36% year-5 margin is above anything Alphabet has reported except the March 2026 quarter's 36.1%, and it needs costs other than depreciation to grow three points a year slower than revenue against 1.6 points actually recorded — the case says so. | Yes as an upside. Supported by delivered claims, but it also needs purchase commitments beyond the 610,300 already signed, which the draft states. | PASS |
| Management | n/a — `computable: false`, no revenue, margin or profit target exists. Every quoted item is verbatim and on its cited page (§3 below). | n/a | n/a | PASS |

## 3. Consistency checks (§18.7 step 4(c))

**Rule 10 — year 1 against the latest reported run-rate.** Reported: first half 2026 revenue growth 23.05% (229,692 / 186,662) and the June quarter 24.23% (119,796 / 96,428) [10-Q Q2 2026, Item 1] [Q2 2026 release, p.1]. Base year 1 at 23% is the reported half-year rate, with the one-point gap to the June quarter carried by two sourced items (a one-point currency tailwind becoming "a slight FX headwind", and "lapping an acceleration in Search performance", both [Q2 2026 call, p.13]) — **PASS**. Bull year 1 at 26% runs about two points above, sourced to the order book, above-commitment usage, chip-system revenue with no year-earlier base and the supply constraint [Q2 2026 call, p.4] [p.13] [p.15] — **PASS**. Bear year 1 at 19% is 4.2 points below the June quarter, and the draft's own detail concedes that only part of the gap is sourced ("The rest of the gap is this case's own assumption") — **FAIL**, item 1 in §6.

**Rule 11 — segment build.** Present in all three computed cases with trailing revenue and latest growth per line, sourced to [10-K FY2025, Note 2] [10-Q Q2 2026, Note 2] [Q2 2026 release, p.1]. I re-derived every trailing figure from the two filings: FY2025 Search 224,532, YouTube 40,367, Network 29,792, Subscriptions 48,030, Cloud 58,705, Other Bets 1,537, hedging (127), total 402,836; plus six months to June 2026 less six months to June 2025. All seven trailing figures and the 445,866 total tie exactly. Latest-growth column re-derived from the same table: 16.8%, 12.9%, (0.7)%, 15.2%, 81.8%, 2.4%, company 24.2% — all as stated.

I rebuilt the company path from the line rates myself. **Years 1, 3 and 5 reproduce to the decimal in all three cases:**

| Case | Draft year 1 | Mine | Draft year 3 | Mine | Draft year 5 | Mine | Verdict |
|---|---|---|---|---|---|---|---|
| Bear | 19.2% | 19.16% | 9.8% | 9.78% | 7.1% | 7.12% | OK |
| Base | 23.1% | 23.11% | 17.0% | 16.97% | 12.8% | 12.85% | OK |
| Bull | 25.8% | 25.84% | 21.2% | 21.21% | 17.1% | 17.07% | OK |

Years 2 and 4 are not published per line; they reproduce on readings consistent with the named steps (bear year 2 lands at 13.43% once Search steps 12 to 7 as the draft names; bear year 4 at 8.27% with Cloud at 17%; bull year 2 at 23.19% with Search at 15%; base years 2 and 4 reproduce at 19.82% and 14.71% on straight interpolation). The Cloud revenue used in each order-book check also reproduces exactly (bear 124,187 and 167,653; base 131,949 and 191,326; bull 135,830 and 206,461), as does the base case's 66,000 excess over the contracted amount. Base year-5 revenue shares reproduce (Search 42%, YouTube 7%, Network 3%, Subscriptions 10%, Cloud 38%), as does the advertising share used in every margin bridge (bear 53.5%, base 51.8%, bull 49.3% against 70.7% today). **PASS.**

**Steps down of more than three points.** Checked every line in every case. Base: the only company-level step above three points is 23.1 to 19.8, named; Cloud's four steps (70/45/33/25/20) each named; no other line steps more than two points. Bear: 19.2 to 13.4 named, plus Cloud 60 to 35 and 35 to 22 and Search 12 to 7, all named; the 13.4 to 9.8 step is 3.6 points at company level and is not named in its own sentence, but both of its drivers (Cloud 35 to 22, Search) are. Bull: 21.2 to 19.2 named plus four Cloud steps. **PASS.**

**Rule 12 — sales-to-capital against the lagged history.** I recomputed the whole ratio history from the filings, on the model's own basis (net investment = purchases of property and equipment minus depreciation of property and equipment; revenue added the following year):

| Money spent in | Capex | Depreciation | Net investment | Revenue added next year | Ratio |
|---|---|---|---|---|---|
| 2021 | 24,640 | 10,273 | 14,367 | 25,199 | 1.75 |
| 2022 | 31,485 | 13,475 | 18,010 | 24,558 | 1.36 |
| 2023 | 32,251 | 11,946 | 20,305 | 42,624 | 2.10 |
| 2024 | 52,535 | 15,311 | 37,224 | 52,818 | 1.42 |
| 2025 | 91,447 | 21,136 | 70,311 | 86,060 (annualised) | 1.22 |

Five-year average 1.57. Same-year ratios 1.40, 1.21, 1.15, 0.75, 0.64 (the last using 80,598 of capex less 13,586 of depreciation in the first half of 2026). Sources: [10-K FY2023, Item 8] l.1788, l.1818; [10-K FY2025, Item 8] l.1742, l.1772; [10-Q Q2 2026, Item 1] l.667, l.697. Every figure in the draft's table matches mine. Base 1.25 is at the bottom of the lagged record, bull 1.40 is its median (1.42) less a little, bear 0.80 is below all of it; each `value_late` steps down from its early value with a stated reason. **PASS.**

**Rule 13 — margin bridge, drag and offsets.** All three bridges show the depreciation drag and the two offsets side by side in one table. The depreciation path re-derives exactly: 25,237 in the base year, then about 11 cents added per dollar spent the year before. Base: 39,801 (25,237 + 11% of the 132,402 spent in the twelve months to June 2026), 65,063, 92,013, 112,421, 135,035 — 7.3%, 9.9%, 12.0%, 12.7% and 13.5% of each year's revenue, exactly the table. Bull: 39,801, 66,053, 95,203, 118,280, 144,699 (7.1% to 12.4%). Bear: 39,801, 65,063, 92,013, 109,503, 128,533 (7.5% to 16.9%). The 11% factor is calibrated on the company's own step (21,136 − 15,311 = 5,825 on 52,535 of 2024 spending, 11.09%) and cross-checks against the lives management gives: servers and network equipment generally six years, data-centre and office buildings seven to 40 years [10-K FY2025, Note 1], with "Approximately 60% of our investment in technical infrastructure this quarter was in servers, and 40% was in data centers and networking equipment" [Q2 2026 call, p.11] — a 60/40 mix on those lives implies about 10 cents, so 11 is the conservative side of both anchors. The schedule adds without retiring, which is a labelled approximation and matters little inside five years. Offsets re-derive: the traffic-payment rate held at 19.9% of advertising revenue (62,880 / 315,348 = 19.94%, with 62,880 = 59,926 + 31,407 − 28,453) falling to 10.3% of revenue in the base case as advertising drops to 52% of the company; and every other cost growing two points a year slower than revenue, easing to one and a half, which reproduces the 46.4 / 45.6 / 44.9 / 44.3 / 43.7 row exactly from 47.1%. The recorded gaps are right: 1.6 points on the like-for-like aggregate in the June quarter (55,743 against 45,454, 22.6% growth against 24.2%) and 4.6 to 4.7 on all costs except depreciation; the bear's 5.5 for the first half also re-derives (23.1% less 17.6%). **PASS.**

**Reinvestment overrides for years 1 to 2, net of the depreciation those years carry.** Arithmetic re-done, all exact. Gross spending: second half of 2026 = 200,000 (midpoint of the guided range) less 80,598 already spent = 119,402; first half 2027 = 45% of 245,000 = 110,250; model year 1 = 229,652; second half 2027 = 134,750; first half 2028 = 110,250; model year 2 = 245,000. Amortisation from the disclosed schedule (747 for the rest of 2026, 1,304 in 2027, 1,142 in 2028 [10-Q Q2 2026, Note 9] l.2137): 747 + 652 = 1,399 for year 1, 652 + 571 = 1,223 for year 2. So 229,652 − 39,801 − 1,399 = **188,452** and 245,000 − 65,063 − 1,223 = **178,714**; bull 238,652 − 39,801 − 1,399 = **197,452** and 265,000 − 66,053 − 1,223 = **197,724**; management 200,000 − 39,801 − 1,399 = **158,800**. The bear reuses the base figures, which is right because the spending is contracted either way. The implied ratios for those two years (0.58 and 0.62) also re-derive. **PASS.** One note: the management cell pairs a calendar-2026 gross number with a July-to-June depreciation figure, so 158,800 is a few thousand low; the cell says the mapping is an approximation and the case is not computed, so nothing turns on it.

**Gross capex the years 3 to 5 fall-back implies.** Stated in a table in every case, and it re-derives from the ratio and the written revenue path. Base: 185,529 / 205,586 / 226,938 (24%, 23%, 23% of revenue), summing to 618,053. Bull: 209,795 / 240,174 / 266,734 (25%, 24%, 23%), summing to 716,703. Bear: about 159,000 / 173,000 / 192,000 (24% to 25%). Plausibility against what management has said: the two guided years are set in money and honour the 195,000 to 205,000 range and the "increase significantly in 2027" quote; years 3 to 5 sit beyond all guidance, and the draft says so and names this as the input most worth the owner's attention. The base case's 610,300 comparison is the right order of magnitude but loose — purchase commitments run to 2054 and include energy take-or-pay and content licences, not only equipment [10-Q Q2 2026, Note 10]. The one shape worth the owner's eye is the 24% fall in gross spending from model year 2 to model year 3 (245,000 to 185,529) in the year straight after the guided peak; it is disclosed, it is what a 1.25 ratio forces, and the margin bridge is built on the same number, so it is consistent rather than hidden. **PASS with that note.**

**Amortisation roll-off.** Addressed. The memo row carries the full disclosed schedule (747 / 1,304 / 1,142 / 1,096 / 1,055), states that it stays deducted, and every margin `detail` says it runs about 0.2% of revenue and does not move the path. The step from 793 in the base year to 1,399 in year 1 is about 0.08 points of margin, inside the bridges' rounding. **PASS.**

**Management case built only from recorded guidance.** `computable: false` with a stated reason; the only number used is the capex midpoint. I checked all eleven quoted items word for word against the cached transcript with whitespace and dash normalisation: every one is verbatim and on the page cited (capex 2026, capex 2027, chip-system timing, rented capacity, Search comparison, currency, depreciation and hiring all p.13; order book p.12; free cash flow p.14; equity markets p.18). Ranges are taken at the midpoint; nine of eleven items are marked "not numeric". **PASS.**

**Terminal rules.** Bear premium 0 with the moat-is-gone reason ✓. Base 0.07, at or below the 0.08 soft ceiling, `allow_large_premium: false`, no warning printed ✓. Bull 0.10, below the 0.12 ceiling ✓. Terminal growth `riskfree` in all three with `allow_above_riskfree: false` ✓. Cost of capital shared, no overrides ✓. Weights 0.25 + 0.50 + 0.25 = 1.00 ✓.

The draft's two return-on-capital figures both check out. Reported: 147,628 × (1 − 0.168) / 516,207 = 122,827 / 516,207 = **23.79%**, so "23.8%" is right. Excluding the investment stakes: 516,207 − 131,461 − 14,126 = 370,620, and 122,827 / 370,620 = **33.14%**, so "about 33 per cent" is right, and the 145,600 of stakes named in the reason is 131,461 + 14,126 = 145,587. Terminal cost of capital 8.75%, so the terminal returns are 8.75% (bear), 15.75% (base) and 18.75% (bull) — each below today's 23.8% and far below the 33% on operating capital, and each below its own final-year implied return (below). **PASS.**

**Transition check, read from `uv run value GOOGL --dry-run --no-fetch --set market.price=338.46 --set market.risk_free=0.0475`.** Diagnostic 7 rows, verbatim:

| Row | Reading |
|---|---|
| bear case, free cash flow (USD millions) | year 10 107,832 to terminal year 97,268, a change of −9.8% (expected: the bear's terminal return equals its cost of capital by rule) |
| bear case, return on capital | year 10 13.9% to terminal year 8.8% |
| base case, free cash flow (USD millions) | year 10 289,691 to terminal year 258,433, a change of −10.8% |
| base case, return on capital | year 10 23.8% to terminal year 15.8% |
| bull case, free cash flow (USD millions) | year 10 427,016 to terminal year 388,688, a change of −9.0% |
| bull case, return on capital | year 10 29.7% to terminal year 18.8% |

**No cliff flag.** Every cash-flow step is inside the 15% threshold and every terminal return is above half its year-10 figure (base 15.8 against 11.9; bull 18.8 against 14.9). This is the defect the 2026-09-08 lesson was written about, and the redraft has cleared it: the previous structure produced a terminal-year cash flow 29% below year 5. Diagnostic 6 (value against price) raises its standard flag; its row is a value-versus-price statement, so it is not reproduced here. The run printed three warnings, all mechanical and none about the assumptions: the price is a manual value from `--set`; fetching is off, so the risk-free rate came from the T-bond row of the cached ERPbymonth dataset dated 2026-09-01; and the management scenario was skipped for the stated reason. No rule-override warning was printed.

## 4. Owner's view

The archived `changelog` records the owner editing six cells: `market.mature_market_erp`, and the year-by-year lists for bear revenue growth, bear operating margin, base revenue growth, base operating margin (year 2 only) and bull revenue growth.

| Owner-edited cell | Owner's saved values | Draft | Says so, with a reason? |
|---|---|---|---|
| `market.mature_market_erp` | 0.04 | 0.04 — kept | Not needed; the terminal cost-of-capital reason credits it to the owner |
| Bear revenue growth | 20, 15, 14, 14, 12 | 19, 13, 10, 8, 7 | Yes — names the owner's path, then argues the build lets the erosion happen from year 3 and that the owner's path leaves the bear only two to five points below the base |
| Bear operating margin | 31, 30, 30, 30, 30 | 33, 31, 29, 28, 27 | Yes — year 1 higher on the reported 35.0% half-year, later years lower because a flat 30% would need offsets this case does not allow |
| Base revenue growth | 23, 19, 17, 14, 13 | 23, 20, 17, 15, 13 | Yes — the two differences are years 2 and 4, both inside one point, both from the build rounding up |
| Base operating margin | 33, 33, 31, 30, 30 | 33, 33, 32, 32, 32 | Yes — years 1 and 2 agree; years 3 to 5 higher because the two offsets keep working after the drag stops growing |
| Bull revenue growth | 26, 23, 20, 19, 17 | 26, 23, 21, 19, 17 | Yes — the single difference is year 3, one point, from the build |

**No owner-edited cell is silently overwritten or silently kept.** Bull operating margin is *not* an owner-edited cell (it appears nowhere in the changelog), and the draft's note described it as "the owner's saved view"; I corrected that wording (§7). Six cells changed materially that the owner never set and that therefore carry no side-by-side note, correctly: `horizon`, all three `sales_to_capital` pairs, all three `reinvestment_override` pairs, and the base and bull terminal return premiums (0.03 to 0.07 and 0.05 to 0.10). The runner's report to the owner should lead with those last two and with the years 3 to 5 spending fall-back.

## 5. Reader check

- **Reasons:** every `reason` in the file is three sentences or fewer (checked mechanically). None is mostly numbers; the working arithmetic, the history tables and the alternatives all sit in `detail`. Nothing substantive is in a YAML comment — the file has none.
- **No spec citations:** no "§" anywhere in the file. Reasons point at `business.md` and `outlook.md` sections, which is what the method asks for.
- **No YAML key names in prose:** checked for every input key; the reasons say "the reinvestment row", "the ratio above", "set in money below".
- **Unicode and dollar signs:** the redrafted scenario cells were clean, but eleven range en-dashes and twenty "$" signs survived in the base-year, bridge and cost-of-capital cells that were carried over unchanged from the 2026-09-07 draft — the app rules that ban them were written on 2026-09-08, after that draft passed. Streamlit reads "$" as the start of a formula and would have mangled the facts page. Both are now fixed (§7); the file contains no "$" and no en-dash.
- **Pipe tables:** twelve tables, all with unique column headers, and every body row has the same number of cells as its header (checked mechanically). This is the defect that killed a page in the UI audit's third cycle.
- **Stories:** bear 4 sentences, base 5, bull 5, management 3 — all inside three to five. Each carries only the one or two numbers that define it (bear "the 2022 low"; base "a point below today's", "low twenties", "low teens"; bull "more than doubles in five years", "about twice its cost of capital"), and I verified those: base year-5 margin 32% against 33.1% today, bull year-5 revenue 2.61 times the base year, bull terminal return 18.75% against a 8.75% cost of capital.

## 6. Verdict: REVISE

1. **Bear year-1 revenue growth: 0.19 breaks rule 10 and sits below the owner's own value. Correction: 0.20, with the Search line raised from 12% to about 14.5%.** The latest reported run-rate is 23.1% for the first half and 24.2% for the June quarter, and reported Search growth is 17% [10-Q Q2 2026, Item 1] [Q2 2026 release, p.1]. Rule 10 allows year 1 to move off that only for a specific sourced reason, and the two sourced items here are the currency flip from a one-point tailwind to "a slight FX headwind" and the "lapping an acceleration in Search performance" comparison, both [Q2 2026 call, p.13]; the draft's own `detail` says the rest of the gap is "this case's own assumption that the shift to assistants starts costing Search straight away", which is not one of the reasons the rule admits. I re-ran the draft's own segment build: raising Search year 1 from 12% to 14.5% and leaving every other line untouched gives a company year-1 growth of 20.5%, and 14.0% gives 20.25% — that is, the sourced FX and lapping effects land the bear almost exactly on the 20% the owner saved. The case loses nothing: its differentiation lives in years 2 to 5 (13, 10, 8, 7 against the owner's 15, 14, 14, 12), which the segment build fully supports, and the draft itself concedes that "years one and two are close either way, because the order book fixes them". Please also re-derive the bear margin bridge's year-1 column and the year-1 depreciation share on the corrected revenue, and re-publish the year-2 and year-4 per-line rates while you are there, so the whole build is checkable without reconstruction.

## 7. Direct edits I made to `assumptions.yaml`

All wording, source tags and table formatting; no input value and no judgment was changed. `uv run value GOOGL --validate` passes after the edits, `assumptions.md` was regenerated with `--render-assumptions`, and the dry-run diagnostics are byte-identical to those in §3.

1. **Dollar signs removed (all twenty of them).** All in the carried-over base-year, bridge and cost-of-capital cells; each "$X billion" became "X billion USD". In the one verbatim quote that contained one (Note 3's SpaceX footnote) the sign is written "[USD]" and the cell now says so, matching the convention the management case already used.
2. **Range en-dashes removed (11 occurrences).** "0.2–0.3%" became "0.2 to 0.3%", "2025–2026" became "2025 and 2026", "3.93%–5.84%" became "3.93% to 5.84%", "43–54 million" became "43 to 54 million", and so on.
3. **Source tag corrected.** The base case's revenue detail credited the World Cup contribution to YouTube's 13% to [Q2 2026 call, p.12]; page 12 attributes the 13% to direct-response and brand advertising, and the World Cup remark is on page 11 ("experienced strong Ads growth related to the World Cup, particularly in YouTube Ads"). Both pages are now cited and the sentence says management named it.
4. **Base margin detail:** "so two points is the middle of what the company is actually doing" became "so two points sits just above the like-for-like figure and well below the broader one". Two points is not the midpoint of 1.6 and 4.6; it is just above the like-for-like 1.6.
5. **Base terminal premium reason:** "a little under two thirds of the way down" became "a little over half way down". 15.75% is 8.05 points below today's 23.8% out of a 15.05-point range, i.e. 53% of the way down. (It is about two thirds of the way down from the 33% on operating capital, and the `detail` still carries both figures.)
6. **Base terminal premium detail:** "used a seven point premium, four points in 2018, and 11.5 points for Nvidia" read as self-contradictory; it now says "seven points for Alphabet in February 2024, four points for it in 2018, and 11.5 points for Nvidia in 2023", which is what §18.4 rule 5 records from his workbooks.
7. **Bull margin detail:** "The owner's saved view was 34, 35, 35, 35 and 35 per cent" became "The previous draft, which the owner left unchanged, had ...". That cell is absent from the archived changelog, so it is not one of the owner's own values.
8. **Bear story and bear margin reason:** "Margins fall below the 2022 low" became "Margins fall back to the lows of 2022 and 2023". The path ends at 26.8% (written 27%), which is above 2022's 26% and level with 2023's 27%, not below either.
9. **Bear margin detail:** "grows one point a year slower than revenue" now adds "easing to about half a point by year five", which is what the table's 46.7 / 46.3 / 45.9 / 45.7 / 45.5 row actually does.
10. **Margin bridge row label, all three cases:** "Search distribution payments" became "Payments for traffic (distribution deals and partner sites)", and the base case's offsets sentence now says the same. The 62,880 is total traffic acquisition cost, which includes the money passed to partner sites as well as the money paid for search defaults; the modelling (holding the rate at 19.9% of total advertising revenue) was already the right treatment, only the label was wrong. Worth the owner knowing that holding that blended rate flat is conservative: the filings say the rate has been falling precisely because Network revenue, which carries a much higher rate, is shrinking [10-K FY2025, Item 7] [10-Q Q2 2026, Item 2].

## Sources

Cached files only. `[10-Q Q2 2026, ...]` — `sources/2026-Q2/10-Q-2026-Q2.txt`; `[Q2 2026 call, p.N]` — `sources/2026-Q2/transcript.txt` (company transcript, no printed page numbers; N counted by page break, 28 pages); `[Q2 2026 release, p.N]` — `sources/2026-Q2/press-release.txt`; `[10-K FY2025, ...]` — `sources/2026-Q1/10-K-FY2025.txt`; `[10-K FY2023, ...]` — `sources/2026-Q1/10-K-FY2023.txt`; `[10-Q Q1 2026, ...]` — `sources/2026-Q1/10-Q-2026-Q1.txt`. Industry beta, margin, growth and T-bond figures come from the engine's cached Damodaran datasets under `tools/valuation/data/damodaran/`, dataset date 2026-01-05 and ERPbymonth row 2026-09-01.

---

## 8. Cycle 2 (2026-09-08): re-check of what changed

The analyst applied item 1. I re-checked only the changed cells, plus the file-wide reader rules. **Verdict: PASS.**

**Bear revenue growth, years 1 to 5.** The cell is now `[0.20, 0.13, 0.10, 0.08, 0.07]` and the build publishes every line for all five years. I rebuilt it from those rates alone:

| Year | Draft build | Mine | Draft revenue | Mine | Result |
|---|---|---|---|---|---|
| 1 | 20.5% | 20.52% | 537,379 | 537,379 | OK |
| 2 | 13.3% | 13.33% | 609,011 | 609,011 | OK |
| 3 | 9.7% | 9.73% | 668,280 | 668,280 | OK |
| 4 | 8.1% | 8.13% | 722,628 | 722,628 | OK |
| 5 | 7.1% | 7.06% | 773,650 | 773,650 | OK |

Cloud year 1 and year 2 come out at 124,187 and 167,653, so the order-book check against the contracted 257,000 is unchanged and still correct. The year-5 advertising share is 53.8%, which is the figure the margin bridge now uses (it was 53.4%). **OK.**

**Rounding statement.** "The build gives 20.5, 13.3, 9.7, 8.1 and 7.1 per cent; the path is written as 20, 13, 10, 8 and 7, with year one rounded down half a point rather than up, which is the only rounding in the path that is not to the nearest whole point." Verified: 20.52 is within a hundredth of an exact half, so writing 20 is a choice against the round-half-up convention and rounds the case's favour away; 13.33 to 13, 9.73 to 10, 8.13 to 8 and 7.06 to 7 are each the nearest whole point. The statement is true. **OK.**

**Rule 10, re-tested.** Year 1 at 20% sits 3.1 points below the June quarter's 24.23% and 3.05 below the first half's 23.05%, and the whole of the move is now carried by the two sourced items: the currency flip, whose effect the CFO located ("This impact will be seen primarily in Search and YouTube Ads", verbatim, [Q2 2026 call, p.13]), and the "lapping an acceleration in Search performance" comparison [Q2 2026 call, p.13]. Those take the Search line from a reported 17% to 14.5% and the company to 20.5%; the sentence "This case's own view of the business is expressed in years two to five, not in year one" is now accurate against the numbers. The unsourced assumption that cycle 1 failed on is gone, and year 1 lands on the owner's own saved 20%. **PASS.**

**Bear margin bridge, year-1 column and depreciation share.** Re-derived on the corrected revenue of 535,039 (445,866 x 1.20): payments for traffic 70,329 / 535,039 = 13.14% against the stated 13.1; depreciation 39,801 / 535,039 = 7.44% against the stated 7.4; everything else 47.125 x (1.195 / 1.205) = 46.73 against the stated 46.7; operating margin 100 − 13.14 − 7.44 − 46.73 = 32.69 against the stated 32.7. The money figure for year-1 depreciation is correctly left at 39,801, because the lagged schedule sets it from the 132,402 spent in the twelve months to June 2026 and not from this year's revenue, and the cell now says exactly that. Years 2 to 5 also re-derive: 10.76, 13.84, 15.26 and 16.74 per cent of revenue against the stated 10.8, 13.8, 15.3 and 16.7. **OK.**

**Reader rules, re-checked file-wide.** No "$" anywhere; no "§" anywhere; no en-dashes (the only non-ASCII characters left are the five ellipses inside the source-tag names); all twelve pipe tables still have unique column headers and every body row matches its header width; every `reason` is still three sentences or fewer. The base and bull builds now publish years 1 to 5 as well, and both reproduce exactly from the published rates (base 23.11 / 19.82 / 16.97 / 14.67 / 12.85; bull 25.84 / 23.20 / 21.22 / 19.17 / 17.08), with the base year-5 share column and the bull 49% advertising share confirmed. **OK.**

**Engine.** `uv run value GOOGL --validate` passes (computable scenarios bear, base, bull; management skipped for the stated reason). Diagnostic 7 from `uv run value GOOGL --dry-run --no-fetch --set market.price=338.46 --set market.risk_free=0.0475`, **no cliff flag**, only the bear rows moved:

| Row | Reading |
|---|---|
| bear case, free cash flow (USD millions) | year 10 108,738 to terminal year 98,085, a change of −9.8% (expected: the bear's terminal return equals its cost of capital by rule) |
| bear case, return on capital | year 10 14.0% to terminal year 8.8% |
| base case, free cash flow (USD millions) | year 10 289,691 to terminal year 258,433, a change of −10.8% |
| base case, return on capital | year 10 23.8% to terminal year 15.8% |
| bull case, free cash flow (USD millions) | year 10 427,016 to terminal year 388,688, a change of −9.0% |
| bull case, return on capital | year 10 29.7% to terminal year 18.8% |

Diagnostic 6 still raises its standard flag; its row is a value-versus-price statement and is not reproduced. The same three mechanical warnings as in cycle 1, and no rule-override warning.

**Two direct edits in cycle 2** (`--render-assumptions` and `--validate` re-run after both):

1. **Bear margin detail, rounding note added.** On the corrected revenue the bridge gives 28.4% in year 3 while the written path keeps 0.29, a six-tenths round-up away from the nearest whole point that the cell did not mention. The written values are unchanged; the cell now says which two years round up and that year three is "the one place the written margin is more generous than the bridge". Worth the owner's eye, and it cuts in the direction of the owner's own view that the first draft was too pessimistic.
2. **Bear sales-to-capital detail, year-5 implied spending corrected from 197,000 to 193,000, and the range from "24 to 26 per cent" to "24 to 25 per cent".** This is a working note the engine never reads. 197,000 assumes year-6 revenue grows at year 5's 7%; with `horizon: 10` the §18.2 rule fades year 6 to 6.55%, which gives net investment of 62,924, gross spending of 192,632 and 25.1% of revenue. Years 3 and 4 were already right at about 160,000 (24.0%) and 173,000 (24.2%), and I re-derived both.

**Nothing is outstanding.** §18.7 allows two cycles and this was the second; the two items above are recorded rather than sent back, because neither changes an input and both are now stated in the file the owner reads.
