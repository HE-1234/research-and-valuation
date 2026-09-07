# Alphabet (GOOGL) — Valuation draft review, as of Q2 2026

_Reviewer pass on `valuation/assumptions.yaml` (drafted 2026-09-07), per AGENTS.md §18.7 step 4. Written 2026-09-07. Nothing fetched from the internet; every figure below was re-derived from the cached filings under `sources/2026-Q2/` and `sources/2026-Q1/`. Line references are to the cached `.txt` files._

**Verdict: REVISE** (one number FAIL, three consistency items; list in §6).

## 1. Number re-check

TTM = FY2025 + six months to June 30, 2026 − six months to June 30, 2025. Sources: `10-K-FY2025.txt` (10-K), `10-Q-2026-Q2.txt` (10-Q), `10-Q-2026-Q1.txt` (Q1 10-Q), `8-K-2026-06-05-preferred.txt` (8-K pref).

| Cell | YAML | Re-derived | Source line(s) | Result |
|---|---|---|---|---|
| base_year.revenue | 445,866 | 402,836 + 229,692 − 186,662 = 445,866 | 10-K l.1591; 10-Q l.376 | OK |
| base_year.operating_income_gaap | 147,628 | 129,039 + 80,466 − 61,877 = 147,628 (33.1%) | 10-K l.1605; 10-Q l.390 | OK |
| one_time_items: EC ad-tech fine | 0 (charge 3,500) | "$3.5 billion in the third quarter of 2025" | 10-Q l.2196; 10-K l.1134 | OK |
| one_time_items: PriceRunner | 0 (charge 1,500) | principal $1.5B in G&A; $581M interest/costs in OI&E | 10-Q l.2833, l.2212 | OK |
| one_time_items: Waymo charge | 0 (charge 2,100) | $2.1B Q4 2025, "based on estimated stock valuation", inside the $4.2B SBC increase | 10-K l.980, l.1110 | OK |
| one_time_items: office impairment | 0 (charge 300) | "$300 million" in Q1 2026 S&M | Q1 10-Q l.2257 | OK |
| base_year.amortization_of_acquired_intangibles | 793 | 6M 2026 545; Q2 2025 124 (6M 2025 246); H2 2025 inferred 2 × 124 = 248; 545 + 248 = 793. Labelled "our inference" in the YAML. The FY2025 10-K has no intangible-assets note: `grep -i amortization` returns only "Amortization of lease assets" (l.2552) and tax text (l.3531); `grep -i intangible` returns only risk-factor, tax and policy text (l.647, 1211, 1782, 1999, 2001, 2009, 3503). Expected 747 / 1,304 / 1,142 / 1,096 / 1,055 confirmed. | 10-Q l.2133, l.2137–2145 | OK |
| base_year.stock_based_compensation | 28,147 | 24,953 + 14,708 − 11,514 = 28,147 (cash-flow line) | 10-K l.1744; 10-Q l.669 | OK |
| base_year.rnd_expense | 68,974 | 61,087 + 35,251 − 27,364 = 68,974 | 10-K l.1597; 10-Q l.378 | OK |
| base_year.effective_tax_rate | 0.168 | 26,656 / 158,826 = 16.78%; TTM (26,656 + 41,394 − 12,986) / (158,826 + 216,165 − 75,722) = 55,064 / 299,269 = 18.4%; 6M 2026 rate 19.1% | 10-K l.1609–1611, l.3527; 10-Q l.2508 | OK |
| base_year.invested_capital | 516,207 | 640,480 + 98,165 + 1,999 + 18,037 − 242,474 = 516,207 | 10-Q l.353, 327, 1826, 1630, 285 | OK |
| bridge.cash_and_marketable_securities | 162,474 | 242,474 − 80,000. Components: cash & equivalents 55,911; government bonds 51,822; corporate debt 26,157; mortgage/asset-backed 21,521; marketable equity 87,063 − 80,000 SpaceX = 7,063. Sum 162,474. | 10-Q l.285; Note 3 table l.1080–1101 | OK (wording clarified, see §5) |
| bridge.debt | 100,164 | 98,165 + 1,999 = 100,164; face 101,085; discount/costs 921; fair value $94.9B; other long-term debt 1,686; no commercial paper; $1.3B drawn on facilities | 10-Q l.1818–1842, l.1729 | OK |
| bridge.operating_lease_liabilities | 18,037 | 3,446 + 14,591 = 18,037; $85.2B not yet commenced | 10-Q l.1626–1630, l.1699 | OK |
| non_operating_assets: SpaceX short-term restricted | 80,000 | footnote (1): "$80.0 billion of ... SpaceX shares subject to short-term restrictions" | 10-Q l.1101 | OK |
| non_operating_assets: marketable equity in other non-current assets | 14,126 | 14,126; footnote (2) $14.1B SpaceX restricted through Q3 2027 | 10-Q l.1097, l.1103 | OK |
| non_operating_assets: non-marketable securities | 131,461 | 124,259 (measurement alternative; $87.9B remeasured in Q2) + 7,202 (equity method and other) = 131,461 | 10-Q l.295, 1114, 1268–1274 | OK |
| bridge.minority_interests | 7,100 | "$7.1 billion", of which 824 redeemable; only given in billions | 10-Q l.1909 | OK (rounded) |
| other_claims: preferred stock | 19,000 | 385 million depositary shares (167.5M + 167.5M + 50M over-allotment) × $50 = **19,250**; equivalently 19.25M preferred shares × $1,000. The 10-Q's "19 million" is rounded; the 8-K gives the exact counts. Cross-check: 19,250 − carried 18,023 = 1,227 = issuance costs (~216) + capped-call premium 1,011; the YAML's 19,000 − 18,023 = 977 is less than the capped-call premium alone, which cannot be. | 10-Q l.2256, 2258, 343–344, 580; 8-K pref l.261; 8-K 06-04 l.269 | **FAIL → 19,250** |
| other_claims: finance leases | 2,590 | 449 + 2,141 = 2,590 | 10-Q l.1640–1644 | OK |
| other_claims: accrued fines and settlements | 17,356 | "Accrued fines and settlements 17,356"; "primarily included EC fines"; $5.2B Android fine paid July 2026 | 10-Q l.1889–1890, 3254, 2186 | OK |
| other_claims: backstop credit derivatives | 815 | liability fair value 815; notional 43,785; $7.6B guarantees "not material"; "$24.1 billion of future backstops" not yet finalized; $20.0B commitment is an equity derivative (liability 457) | 10-Q l.1406, 1375, 2164, 3266, 3268, 1403 | OK |
| bridge.probability_of_failure (reason figures) | 0 | debt proceeds 56,226; equity 30,499 + 19,063 = 49,562 | 10-Q l.723–727 | OK |
| bridge.diluted_shares | 12,309 | basic 12,151 + RSUs 142 + preferred (if-converted) 16 = 12,309; period-end common 12,230 | 10-Q l.2365–2381, l.597 | OK |
| cost_of_capital.build.pretax_cost_of_debt | 0.048 | Q1 2026 USD notes "$20.0 billion ... weighted-average coupon rate of 4.80%"; 2025 USD notes 4.89% and 4.92%; effective rates on 2025/2026 USD notes 4.00–5.79% / 3.93–5.84% | 10-Q l.1737, table l.1740–1835; 10-K l.1281, 1284 (Item 7, not Note 6: tag corrected) | OK |

Other figures quoted in reasons, spot-checked: TTM advertising 294,691 + 158,882 − 138,225 = 315,348 (70.7%) OK [10-K l.1008; 10-Q l.918]; TTM Cloud 58,705 + 44,796 − 25,884 = 77,617 OK; Cloud margin Q2 35.6% vs 20.7% OK [slides l.256; 10-Q l.2551]; Q1 2026 margin 39,696 / 109,896 = 36.1% OK; Google Services FY2025 40.7%, Q2 2026 41.8% OK; sales-to-capital history (same-year 1.40 / 1.21 / 1.15 / 0.75 / 0.64; lagged 1.75 / 1.36 / 2.10 / 1.42) all reproduce from 10-K FY2023 l.1641, 1788, 1818 and 10-K FY2025 l.1591, 1742, 1772; D/E numerator 118,201 and the 0.027 illustration OK; transcript page numbers p.11–14, p.18, p.22 confirmed by counting form feeds. Minor: "86 million shares sold in June" follows the 10-Q's rounded counts (29 + 29 + 14 + 14); the 8-K's exact counts sum to 87.1 million.

## 2. Rule checks (§18.4)

1. **Base year GAAP, only sourced one-time items removed.** Operating income is the reported 147,628 with nothing removed. The four candidates are set to 0 with reasons: EC fine (fourth EC fine since 2017, recurring at intervals: defensible, and the rule's own wording), PriceRunner (third legal accrual above $1B in twelve months: defensible), Waymo charge (stock-based pay: rule 1 forbids the add-back, correct), office impairment ($300M after $1.8B in 2023, 0.07% of revenue: defensible). Damodaran's recurring-at-intervals guidance would *average* such charges rather than count the TTM amount in full; TTM legal charges of ~5.0B run roughly 2–3B above a ten-year EC-fine average, so the base margin is understated by about 0.5–0.7 points. Conservative and within rule 1; a note, not a fix.
2. **Stock pay expensed.** Yes; memo row 28,147 recorded, never added back.
3. **Amortization deducted and its role addressed.** Yes; memo row 793 (inference labelled), roll-off addressed in every margin reason (0.2–0.3% of revenue, peak 1,304 in 2027).
4. **Interest income and the $99B equity gains excluded.** Yes: both sit in OI&E (10-Q l.392, 2831), below the "Income from operations" line used.
5. **Management case only from recorded guidance; `computable: false`.** Correct: no multi-year revenue or margin target exists (outlook.md §4). All ten guidance items are verbatim and match `outlook.md` §4 and the transcript (p.12–14, p.18). Year-1 override 200,000 − (25,237 + 793) = 173,970: arithmetic correct; midpoint of "$195‑205 billion" [call p.13, l.482]; D&A components confirmed. Two approximations are noted in the reason (calendar 2026 mapped to July 2026–June 2027; TTM rather than year-1 depreciation); they pull in opposite directions (see §3a).
6. **`other_claims` are claims on existing value.** Preferred: yes, with a one-line justification, and liquidation preference is the right measure *within the conversion band*: at a May 2029 price between about $355 and $444 the holders receive exactly $1,000 of stock per preferred share; above $444 they receive 2.252 shares each (more than $1,000), below $355 2.816 shares (less). Omitted: three years of 6.25% dividends on 19,250 (~1,200 a year, ~3,300 present value, ~$0.27 a share). Accrued fines: yes, justified ("cash that will leave without buying anything"); already expensed in TTM operating income, so subtracting the unpaid stock does not double-count, and the July $5.2B payment reduces cash and the claim equally. Finance leases and the 815 backstop liability: debt-like, fine. The $20.0B milestone commitment is correctly excluded (buys more shares).
7. **Terminal growth ≤ 0.0475, flags false.** Yes in all three cases. Risk: the reason says the engine "caps it at the fetched risk-free rate", but §18.4 rule 5 says going above the risk-free rate requires `allow_above_riskfree: true`; if the fetched DGS10 is below 4.75% the run may stop. See §6 item 4.
8. **`roic_premium`.** Bear 0, base 0.03, bull 0.05; none above 0.05; flags false. OK.
9. **Weights.** 0.25 + 0.50 + 0.25 = 1. OK.
10. **Cost of capital shared.** All `cost_of_capital_override: null`. OK.
11. **Tax rate 0.168.** Defensible: FY2025 rate, already burdened by a non-deductible EC fine (10-K l.1211); the 18.4% TTM and 19.1% H1 2026 rates are inflated by deferred tax at the statutory rate on $99B of unrealized equity gains (10-Q l.3121), which are not operating income. Terminal 0.25 as the model requires.

## 3. Consistency checks

### (a) Growth vs reinvestment

Engine formula: Reinv_t = (Rev_{t+1} − Rev_t) / S·C, year 1 overridden at 173,970. Rev_0 = 445,866.

| USD millions | Yr 1 | Yr 2 | Yr 3 | Yr 4 | Yr 5 |
|---|---|---|---|---|---|
| Bear revenue | 512,746 | 558,893 | 592,427 | 616,124 | 634,607 |
| Bear net reinvestment (S·C 0.6) | 173,970* | 55,889 | 39,495 | 30,806 | 31,730 |
| Base revenue | 535,039 | 620,645 | 701,329 | 771,462 | 833,179 |
| Base net reinvestment (S·C 0.9) | 173,970* | 89,649 | 77,925 | 68,574 | 74,060 |
| Bull revenue | 552,874 | 668,977 | 782,703 | 884,455 | 972,900 |
| Bull net reinvestment (S·C 1.3) | 173,970* | 87,482 | 78,270 | 68,035 | 74,838 |

\*override. Gross capex ≈ net reinvestment + depreciation. Depreciation of property and equipment was 25,237 TTM and 7,104 in Q2 2026 alone (28.4B run-rate); a simple schedule (60% servers over 6 years, 40% data centers and network over 20 years, per the call's 60/40 split [call p.11, l.398–400], one-year lag to in-service) reproduces the 2026 run-rate (27.9B) and puts 2027 depreciation near 52B from 2021–2026 capex alone. So the model's year-2 gross capex is roughly 108B (bear), 142B (base), 140B (bull), all **below 2026's 200B**, while the recorded guidance is "we continue to expect our CapEx to increase significantly in 2027" [call p.13, l.486]. History for scale: capex 24.6 / 31.5 / 32.3 / 52.5 / 91.4B for 2021–2025, 80.6B in H1 2026 alone [business.md §3 table; 10-Q l.697].

A **year-2 override is needed** in every scenario, or the reasons must say the scenario assumes capex falls back in 2027 against guidance. The only sourced anchor for "significantly" is the H2 2026 run-rate implied by guidance: 200,000 − 80,598 = 119,402 for the half-year, about 239B annualized; less ~52B of depreciation gives ~187B of net reinvestment for year 2, against the 90B the base case now spends. At a 9% discount rate for illustration, the ~97B gap is worth about 82B of present value, or about $6.6 a share. The bear is the most inconsistent: its story says the ordered data centers "still arrive", and $811B of purchase commitments and $85.2B of signed-but-not-started leases back that up [business.md FLAG (Q2 2026); 10-Q l.1699], yet the S·C mechanism halves its spending as soon as growth slows.

The ratios 0.6 / 0.9 / 1.3 are below the lagged history of 1.2–2.1 (average 1.66) and bracket the latest same-year figures (0.75 in 2025, 0.64 in H1 2026). They are plausible: AI capacity buys less revenue per dollar than search servers did, and the bull's 1.3 assumes a return toward the lagged pattern rather than beyond it. The direction of error is conservative except where the override gap above dominates.

### (b) Margin path vs the economics (business.md §3–§4)

TTM GAAP margin 33.1%; FY2022–2023 26–27% when capex was 10–11% of revenue; depreciation of property and equipment 5.7% of TTM revenue.

Depreciation wave, same schedule as above, two capex paths (USD billions, as % of base-case revenue):

| | 2027 (yr 2) | 2028 (yr 3) | 2029 (yr 4) | 2030 (yr 5) |
|---|---|---|---|---|
| Capex flat at 200B from 2026 | 52 (8.4%) | 73 (10.4%) | 94 (12.2%) | 115 (13.8%) |
| Capex 250B in 2027, 300B after | 52 (8.4%) | 79 (11.3%) | 112 (14.5%) | 145 (17.4%) |
| Capex falls to ~140B in 2027 (the model's own base path) | 52 (8.4%) | ~65 (9.3%) | ~80 (10.4%) | ~95 (11.4%) |

Headwind against 5.7% today: 2.7 points in year 2 in every path, then 4–12 points by year 5 depending on capex, plus the energy and data-center operating costs management warns of [call p.13–14]. Offsets available: operating expenses fell from 21.5% of TTM revenue only slowly (R&D 15.5%, S&M 3.6%, G&A 2.4%); with 13–20% revenue growth, holding opex dollar growth near 10% yields about 3–4 points by year 5; TAC at 19.8% of ad revenue drifting down one point is worth about 0.7 points of consolidated margin; Cloud at 35.6% is already near Services' 41.8%, so the mix shift adds at most 1–2 points as Cloud grows from 17% toward 30% of revenue. Total plausible offsets: about 5–6 points.

- **Base 30% (−3 points):** reachable only on the model's own falling-capex path (headwind ~5.7 points by year 5, offsets ~5–6). On any path consistent with "increase significantly in 2027", the year-5 margin lands nearer 26–28%. The base margin and base reinvestment are each defensible alone but not together: the owner must pick one capex path and make both cells follow it.
- **Bull 37% (+4 points):** requires 8–10 points of offsets against a depreciation share of 10–14% of even the bull's larger revenue (972,900). Q1 2026's 36.1%, the anchor cited, was earned with depreciation at 5.9% of revenue, before the wave. "Margins rise despite the heavier machinery" is asserted, not shown; 34–35% in years 4–5 is the most the arithmetic supports.
- **Bear 23%:** below the 2022 low, consistent with 8–14% depreciation on slow-growing revenue; plausible as written, though its spending path (see a) contradicts its story.
- Amortization roll-off: addressed, correctly immaterial (0.2–0.3% of revenue).

### (c) Year-5 revenue vs history

| | Year-5 revenue | × TTM | 5-year CAGR |
|---|---|---|---|
| Bear | 634,607 | 1.42 | 7.3% |
| Base | 833,179 | 1.87 | 13.3% |
| Bull | 972,900 | 2.18 | 16.9% |

Alphabet's own history in the cached filings: 257.6B (2021) to 402.8B (2025), +56% in four years, 11.8% a year; yearly 9.8 / 8.7 / 13.9 / 15.1%; H1 2026 +23.1% [business.md §2 table; outlook.md §1]. Base runs 1.5 points above the four-year average from a base twice as large; bull runs 5 points above it. No cached source gives a market size for digital advertising or cloud infrastructure, so `final_year_market_size` is correctly null and the "possible" test can only be done by comparison, which is a gap the owner should know about.

### (d) Backlog and TPU timing in the base case

Confirmed: Cloud backlog $513.9B of $519.5B total, "just over 50%" within 24 months [10-Q Note 2, l.972; outlook.md §1, §3]; TPU revenue "a relatively small portion ... this year, ramping as we exit 2026 ... the vast majority ... in 2027" [call p.13, l.470–473; outlook.md §4]; the 10-Q's own wording is "significant majority to be recognized in 2027" [scorecard.md claim 4]. The base story's "half-trillion-dollar backlog" and "TPU hardware sales arrive in 2027" are accurate. Caveat: no dollar size for TPU sales exists anywhere in the sources; the reasons do not invent one.

## 4. 3P test

- **Bear.** Possible: yes (634,607 is 1.42× TTM). Plausible: half; the 23% margin fits the depreciation arithmetic, but net reinvestment of 56B in year 2 (gross ~108B) contradicts the story's own "data centers ... still arrive" and the $811B of purchase commitments [business.md FLAG]. Probable: not today, and it need not be: Search & other grew 17–19% and the scorecard is 7 met / 0 missed [scorecard.md].
- **Base.** Possible: yes by comparison (1.87× TTM, 13.3% a year vs 11.8% history); no market-size figure exists to complete the test. Plausible: margin and reinvestment are individually defensible but rest on opposite capex paths (§3a–b). Probable: supported; backlog rose "by more than $50 billion sequentially" and every capex and Cloud claim was met [outlook.md §3; scorecard.md].
- **Bull.** Possible: unverifiable without a market size; 2.18× in five years against 1.56× over 2021–2025. Plausible: the 37% margin is the weak link (needs 8–10 points of offsets against depreciation at 10%+ of revenue). Probable: year 1 at 24% matches H1 2026's 23–24% [outlook.md §1]; years 2–3 at 21% and 17% exceed every full year in the tables.
- **Management.** Correctly not computable; the story states exactly what was and was not guided.

## 5. Reader check

The four stories are readable by a smart 16-year-old. Retained terms: "moat" (the owner's lens, used in AGENTS.md §18.1), "cost of capital" (valuation glossary, unavoidable), "depreciate", "backlog", "TPU" (business.md glossary), "AI stack" (explained inline: chips, models, products). Direct edits made to `assumptions.yaml`, wording only:

1. Base story: "as the company laps a strong year" → "as it is measured against last year's strong growth" ("laps" is trade jargon).
2. Management story: "as it laps a strong year" → "when measured against last year's strong quarters".
3. `bridge.cash_and_marketable_securities.reason`: the sentence read as 55,911 + 106,563 + 7,063; rewritten so 7,063 is shown inside the 106,563 (99,500 debt securities + 7,063 other marketable equity).
4. `cost_of_capital.build.pretax_cost_of_debt.reason`: "lower local-currency coupons (1.06%–5.31%)" → "local-currency coupons (1.06%–5.31%)"; the sterling notes at 5.31% are not lower than 4.80%.
5. `cost_of_capital.build.pretax_cost_of_debt.source`: `[10-K FY2025, Note 6]` → `[10-K FY2025, Item 7]`; the 4.89% and 4.92% weighted-average coupons appear only in Item 7 (l.1281, 1284), not in the debt note.

Not fixed, noted: the `reason` fields for `sales_to_capital` and several others run five or more sentences dense with numbers, against §18.4's "one to three plain sentences" and §3 rule 5; the engine renders them into `valuation.md`. Trimming is the analyst's call.

## 6. Verdict: REVISE

1. **`bridge.other_claims[0].value` (preferred stock).** 19,000 is wrong: 385 million depositary shares × $50 = 19.25 million preferred shares × $1,000 liquidation preference = **19,250** [10-Q Note 11, l.2256–2258; 8-K 2026-06-05 (preferred), l.261 and 8-K 2026-06-04, l.269]. Fix the value and the reason's "19 million preferred shares ... = 19,000" (the dilution range 43–54 million shares still holds: 19.25M × 2.2520–2.8160). Optionally mention the ~3,300 present value of three years of 6.25% dividends the bridge omits.
2. **`scenarios.{bear,base,bull}.reinvestment_override.values[1]` (year 2).** Sales-to-capital gives net reinvestment of 55,889 / 89,649 / 87,482, i.e. gross 2027 capex of roughly 108–142B, below 2026's 200B, while recorded guidance is "increase significantly in 2027" [Q2 2026 call, p.13]. Either (a) set a year-2 override anchored on the only sourced figure, the H2 2026 run-rate implied by guidance (200,000 − 80,598 = 119,402 per half-year, ~239B a year, less ~52B depreciation ≈ 187,000 net, our inference; the bear at least as much since its spending is committed), or (b) state in each `sales_to_capital.reason` that the scenario assumes capex falls back in 2027 against guidance. Decision for the owner; the arithmetic is in §3a.
3. **`scenarios.base.operating_margin.values` and `scenarios.bull.operating_margin.values`.** Must follow the same capex path as item 2. If capex stays at or above 200B, depreciation reaches 8% of revenue in year 2 and 12–17% by year 5 against 5.7% today, and the base's 30% needs 5–7 points of offsets (about the maximum available) while the bull's 37% needs 8–10 (not available). Question: keep 30% only if item 2 takes option (b); lower bull years 4–5 to about 0.34–0.35, or add the offset arithmetic to the bull reason. Also the base reason's "adds well over 30,000 a year of expense" overstates: 200B at 60% servers over six years plus 40% over longer lives is about 24–28B a year.
4. **`scenarios.*.terminal.growth.value` = 0.0475.** The reason says the engine "caps it at the fetched risk-free rate"; §18.4 rule 5 instead requires `allow_above_riskfree: true` above the risk-free rate. If the fetched DGS10 is below 4.75% the run will warn or stop. Fix: set the value at or below the rate expected at compute time (or confirm the engine caps), or set the flag with a reason.
5. **Minor, `reinvestment_override.values[0]` reasons.** Note that 173,970 nets TTM depreciation (26,030) while year-1 depreciation will be roughly 35–40B, and that the model year (July 2026–June 2027) will carry more than calendar 2026's 200B given H1 2026's 80.6B and a rising 2027; the two errors roughly offset. One sentence in the reason suffices.
6. **Minor, `bridge.diluted_shares.reason`.** "86 million shares sold in June" is the 10-Q's rounded count; the 8-K totals 87.1 million. Say "about 86–87 million".

Everything else in §1 and §2 passes. One more cycle is allowed under §18.7 step 4.

## Cycle 2 (re-check of changed cells only)

**Verdict: PASS.**

| Changed cell | Check | Result |
|---|---|---|
| `bridge.other_claims[0]` preferred = 19,250 | 385M depositary shares (167.5M + 167.5M + 50M over-allotment, 25M per series) × $50 = 19.25M × $1,000 = 19,250 [10-Q Note 11 l.2256–2258; 8-K pref l.261; 8-K 06-04 l.269]. Dividends 6.25% × 19,250 = 1,203 a year; three-year PV ≈ 3,070 at 8.5%; "about 1,200 ... roughly 3,000", noted not valued. | OK |
| Year-2 `reinvestment_override` bear/base 187,000, bull 208,000 | H1 2026 capex 80,598 [10-Q l.697]; 200,000 − 80,598 = 119,402; × 2 = 238,804 ≈ 239,000. 2027 depreciation from 2021–2026 capex on the stated schedule (60/40 split [call p.11, l.398–400]; 6 and 20 years; one-year lag) = 51,883 ≈ 52,000. 239,000 − 52,000 = 187,000; bull 260,000 (239,000 × 1.089, "about 9%") − 52,000 = 208,000. All labelled "our inference". Bear's committed-spending anchor $811.0B / $200.7B short-term confirmed [10-Q Item 2 l.3262]. | OK |
| Depreciation-share arithmetic in reasons (iterating years 3–5 gross capex = net reinvestment + that year's depreciation) | Base: dep/revenue 8.4 / 11.1 / 12.1 / 13.2% in years 2–5 (reason: 8 / 11 / 12 / 13%); gross capex 156 / 162 / 184B (reason: 155–185B); depreciation 78–110B (reason: 78–110B). Bear: 9.3% year 2, 15.8% year 5 (reason: 9%, 16%); gross capex 118–132B (reason: 120–130B). Bull: 7.8% year 2, 11.6% year 5 (reason: 8%, 10–12%); gross 159–188B (reason: 160–190B). | OK |
| Offset arithmetic in base and bull margin reasons | TTM opex 27.8% of revenue (R&D 15.5%, S&M 31,429 = 7.0%, G&A 23,486 = 5.3%) reproduces; opex +10%/yr against 13.3% revenue CAGR → 24.0%, frees 3.8 points (reason "about 4"); bull +12.5% vs 16.9% → 22.9%, frees 4.9 (reason "4–5"). Correction to Cycle 1 §3b of this review: I wrote S&M 3.6% and G&A 2.4%; the analyst's 7.0% and 5.3% are right, and the offset total of 6–7 points stands. "About 24–28B a year" per 200B of capex correct. | OK |
| `bull.operating_margin` [0.34, 0.35, 0.35, 0.35, 0.35] | Matches story "margins hold near today's level" (TTM 33.1%, H1 2026 35.0%) and the reason's "covers the headwind but does not fund a rise". | OK |
| `terminal.growth.value: riskfree` (all three) | Coordinator confirms the string is by spec (§18.4 rule 5, default = risk-free rate); `allow_above_riskfree: false`. Management case null, correct. | OK |
| `bridge.diluted_shares.reason` "roughly 87 million" | 25.46M × 2 + 3.82M × 2 + 28.57M = 87.1M [8-K 06-04 l.267–277]; 10-Q rounding 29 + 29 + 14 + 14 noted. | OK |
| Stories vs values vs reasons | Bear: "keeps spending ... cut back only afterwards" = 187,000 then S/C fall-back; margin below 2022 low = 23%. Bull: "rises further in 2027" = 260B; "hold near today's level" = 35%. Base: story said capex "levels off" while the reason has it falling from 239B to ~156B; **wording edited** to "then eases back as depreciation catches up". Management story and override unchanged and consistent. | OK after edit |

Direct edit this cycle: base story, "then levels off" → "then eases back" (wording only). YAML re-parsed; weights still sum to 1. No numbers changed by the reviewer. Ready for `uv run value GOOGL --validate` and owner review; the owner's attention is best spent on the years 3–5 capex fall-back (a scenario assumption, unsourced by design) and the non-marketable securities carried at 131,461.
