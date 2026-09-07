# Marvell (MRVL) — Review of the valuation draft, as of Q2 FY2027

_Reviewer pass on `companies/MRVL/valuation/assumptions.yaml` (drafted 2026-09-07). Method: every base-year, bridge, cost-of-debt and market-size cell re-derived from the cached filings with `grep -n -F` on full lines; TTM cells rebuilt as FY2026 (10-K) + six months ended 2026-08-01 − six months ended 2025-08-02 (Q2 10-Q comparative columns) and cross-checked against the eight-quarter supplemental. Line numbers below refer to the cached text files in `sources/FY2027-Q2/` and `sources/FY2027-Q1/`. Nothing was fetched from the internet._

**Verdict: REVISE** (one substantive item in the bear case, one question, three minor items; every number in the base year and bridge checks out).

---

## 1. Number re-check

TTM arithmetic components (all in $M):

| Component | FY2026 (10-K Item 8) | H1 FY2027 (10-Q Item 1) | H1 FY2026 (10-Q comparative) | TTM = FY2026 + H1 FY2027 − H1 FY2026 | Four-quarter sum, supplemental |
|---|---|---|---|---|---|
| Net revenue | 8,194.6 (10-K l.1915) | 5,157.1 (10-Q l.127) | 3,901.4 (10-Q l.127) | **9,450.3** | 2,074.5 + 2,218.7 + 2,417.8 + 2,739.3 = 9,450.3 (supp. l.106) |
| Operating income | 1,322.9 (l.1931) | 799.1 (l.135) | 560.7 (l.135) | **1,561.3** | 357.8 + 404.4 + 339.4 + 459.7 = 1,561.3 (supp. l.114) |
| Amortization of acquired intangibles | 942.0 (l.2077) | 440.1 (l.237) | 489.4 (l.237) | **892.7** | 229.0 + 223.6 + 225.2 + 214.9 = 892.7 (supp. l.150) |
| Stock-based compensation | 590.8 (l.1705) | 533.8 (l.1024) | 295.7 (l.1025) | **828.9** | 152.1 + 143.0 + 207.6 + 326.2 = 828.9 (supp. l.149) |
| R&D expense | 2,075.2 (l.1923) | 1,393.4 (l.131) | 1,026.7 (l.131) | **2,441.9** | not in supplemental |
| Restructuring (COGS + opex) | 16.0 (l.2437) | 5.7 (l.709; = 7.9 opex l.133 − 2.2 COGS gains supp. l.207) | (3.6) (l.133) | **25.3** | opex 9.6 + 9.5 + 10.7 − 2.8 = 27.0 plus COGS 0.5 + 0 − 2.0 − 0.2 = −1.7 → 25.3 (supp. l.207, l.219) |
| "Other" non-GAAP items in operating income | — | — | — | — | COGS 0.3 + 1.6 + 0 + 0 = 1.9; R&D 0.3 + 0.1 + 22.4 − 0.1 = 22.7; SG&A 3.5 + 9.6 + 43.6 + 5.5 = 62.2 → **86.8** (supp. l.208, 212, 217) |

Cell-by-cell:

| Cell | YAML value | Reviewer value | Source line reference | Result |
|---|---|---|---|---|
| base_year.revenue | 9,450.3 | 9,450.3 | table above | OK |
| base_year.operating_income_gaap | 1,561.3 | 1,561.3 (16.5% of revenue) | table above | OK |
| … restructuring left inside, 25.3 | 25.3 | 25.3; FY2024–FY2026 series 131.1 / 711.8 / 16.0 | 10-K l.3559; table above | OK |
| … other costs left inside, 86.8; Celestial fees 30.1 | 86.8; 30.1 | 86.8; 30.1 ("acquisition-related transaction costs … six months") | supp. l.208/212/217; 10-Q l.386 | OK |
| … divestiture gain and earn-out charge below operating income | 1,830.4; 433.7 | 1,830.4 "Gain on sale of business" in cash-flow statement; gain "included in interest income and other, net"; 433.7 earn-out charge in "Interest and other loss, net" | 10-K l.2083, l.1371; 10-Q l.985 | OK |
| base_year.one_time_items | [] | nothing removable found (see §2, rule 1) | — | OK |
| base_year.amortization_of_acquired_intangibles | 892.7 | 892.7 (9.4% of revenue); 10-K schedule FY2027 814.0 / FY2028 284.8 / FY2029 131.8 / FY2030 109.5 / FY2031 50.4 | table above; 10-K l.2593–2601 | OK (see REVISE 3 for the newer 10-Q schedule) |
| base_year.stock_based_compensation | 828.9 | 828.9 (8.8%); Q2 326.2 vs 153.6; 190.1 of Celestial awards unrecognized | table above; supp. l.149; 10-Q l.630 | OK |
| base_year.rnd_expense | 2,441.9 | 2,441.9 (25.8%) | table above | OK |
| switches.rnd_history | [1424.2, 1784.3, 1896.2, 1950.4, 2075.2] | FY2022 1,424.2, FY2023 1,784.3, FY2024 1,896.2 (10-K FY2024 l.1785); FY2025 1,950.4, FY2026 2,075.2 (10-K FY2026 l.1923) | as listed | OK |
| base_year.effective_tax_rate | 0.13 | FY2026 GAAP 12.4% (l.3315, l.3357); H1 FY2027 119.1 / 461.6 = 25.8% (10-Q l.139–140); call: "non-GAAP tax rate of 11%" and "approximately 13% in fiscal 2028" (transcript l.77); release confirms 11.0% applied (l.51) | as listed | OK (judgment discussed in §2) |
| base_year.invested_capital | 19,884.9 | 18,531.6 + 4,962.9 + 59.3 + 263.9 − 3,932.8 = 19,884.9; goodwill 13,873.9, intangibles 2,346.6 | 10-Q balance sheet l.83–107; Note 14 | OK |
| bridge.cash_and_marketable_securities | 3,932.8 | 3,932.8; time deposits 194.0 listed under "Cash equivalents"; no marketable-securities line | 10-Q l.83; l.472–473 | OK |
| bridge.debt | 4,962.9 | face 4,999.9 (499.9 + 750 + 500 + 500 + 750 + 500 + 500 + 1,000) − 37.0 = 4,962.9; term loan repaid in full Q2 FY2026; revolver 1.5B undrawn; license obligations 96.2 + 123.8 = 220.0 excluded | 10-Q Note 7 l.518–546; 10-K l.2745; 10-Q l.552; Note 14 l.763, l.777 | OK |
| bridge.operating_lease_liabilities | 323.2 | 59.3 current + 263.9 non-current | 10-Q Note 14 | OK |
| bridge.non_operating_assets: forward contract | 131.0 | 131.0, Level 3, in "Prepaid expenses and other current assets"; notional 300.0, twelve months | 10-Q l.474–475, l.510 | OK |
| bridge.non_operating_assets: marketable equity | 25.5 | 25.5, Level 1, other non-current assets | 10-Q l.477, l.502 | OK |
| bridge.non_operating_assets: non-marketable equity | 156.2 | 156.2 | 10-Q l.515, l.754 | OK |
| bridge.minority_interests | 0 | no non-controlling interest line on the balance sheet | 10-Q l.78–108 | OK |
| bridge.other_claims: Celestial earn-out | 749.5 | 749.5; 315.8 at closing; max 233.0 cash + ~22.4M shares (Note 6) or 24.4M (Item 1A) | 10-Q l.485, l.503, l.509, l.1253 | OK |
| bridge.probability_of_failure | 0.0 | cash 3.9B vs notes 5.0B, nothing due before FY2029 (2028 notes mature in FY2029), operating cash flow 1,244.3 in six months | 10-Q l.250, Note 7 | OK |
| bridge.diluted_shares | 921.2 | 875.6 + 21.8 + 23.8 = 921.2; guidance "921 million" | 10-Q l.675–679; release l.35 | OK |
| bridge.dilution_note figures | as listed | 58,970,907 at $206.58; 1,360,867 time-based; 240 tranches per $500M → 57,610,040 / 240 = 240,042; 4.2M at $87.77 (1.2M vested); 1.0M at $87.00; 876.9M outstanding | 8-K l.48–49; 10-Q l.350–351, l.35 | OK |
| cost_of_capital.build.debt_to_equity_market numerator | 5,286.1 | 4,962.9 + 323.2 = 5,286.1 | as above | OK |
| cost_of_capital.build.pretax_cost_of_debt | 0.053 | 5.300% coupon, 5.358% effective, issued 2026-04-15, ten-year; face-weighted coupon = 227.4 / 4,999.9 = 4.55% | 10-Q l.542–543, l.561–562 | OK |
| diagnostics.final_year_market_size | 55,000 | "It was a $55 billion TAM. 20% on that is $11 billion" for fiscal 2029, data-center custom silicon only | Q1 transcript l.106 | OK |

Supporting reasons also checked: sales-to-capital history inputs (FY2023 revenue +1,457.2, capex 206.2, D&A 304.9, acquisitions 112.3, working-capital outflow 649.8; FY2026 revenue +2,427.3, capex 354.1, D&A 348.6, working-capital outflow 1.1B; H1 FY2027 capex 282.4, D&A 188.5, working-capital outflow 660.3, acquisitions 1.0B + 270.2 cash and 2.5B stock; FY2022 acquisitions 3,555.0) all match 10-K FY2024 l.1573, l.1941, l.1977–1979; 10-K FY2026 l.1705, l.2073, l.2107; 10-Q l.235, l.253, l.1011, l.1024, Note 14. Every management quote in the `guidance` list is verbatim in the transcripts or release (Q2 transcript l.27–83, l.107, l.165–169, l.203–209; Q1 transcript l.20–22, l.40, l.68–72, l.106, l.180; release l.23–39).

**Number-check FAILs: none.**

---

## 2. Rule checks (§18.4)

1. **Base year GAAP, one-time items.** Operating income is as reported. The analyst removes nothing. Restructuring has been booked every year since FY2023 (5.6, 131.1, 711.8, 16.0, 5.7) and acquisition costs appear in four of the last six fiscal years, so treating both as recurring-at-intervals is the reading rule 1 asks for. The two items total 112.1, or 1.2 points of margin; the scenario margins are built from guidance rather than from the base margin, so the choice does not move value. Defensible.
2. **Stock pay expensed.** Yes; 828.9 recorded as a memo row and left inside operating income; `addback_acquired_amortization` and `capitalize_rnd` are off.
3. **Amortization deducted and roll-off addressed.** 892.7 stays deducted. Each scenario's margin reason cites the 10-K schedule (814.0 / 284.8 / 131.8 / 109.5), which is correct as of January 31, 2026. The Q2 10-Q carries an updated schedule as of August 1, 2026 (remainder of FY2027 385.3; FY2028 292.7; FY2029 139.6; FY2030 117.2; FY2031 60.8; total 1,049.6, 10-Q l.451–459) that already includes XConn's 35.0 of amortizable assets; the 997.0 of Celestial and XConn in-process R&D is not amortized until products ship, then over 6–13 years (10-Q l.446–449), so 77–166 a year once it starts. The analyst's "roughly 70 a year" is the low end. See REVISE 3 (wording, no input changes).
4. **Interest income and expense excluded.** Yes. Operating income sits above "Interest income", "Interest expense" and "Other income (expense), net"; the 1,830.4 divestiture gain, the 433.7 earn-out charge and the 131.0 hedge gain are all in that lower block (10-K l.1371; 10-Q l.985).
5. **Management case.** Every item is a recorded quote; ranges are at midpoint (Q3 revenue 3,150; GAAP gross margin 53.4%); qualitative items are `not numeric`; the year-1 mapping (TTM to August 2027 as the midpoint of FY2027 ≈ 12,000 and FY2028 ≈ 18,000) and year-2 mapping (FY2028's 18,000 as nearest guided point) are stated as approximations. `computable: false` is the right call: rule 4's threshold (a multi-year revenue target) is met by FY2028 ≈ 18B, but years 3–5 have no guided number and the engine refuses to compute with nulls, so declaring the case computable would only produce a refusal; the reason explains this and points to the October 6 Investor Day.
6. **Terminal growth.** 0.0475 in all three cases with `allow_above_riskfree: false`. This is the planner's proxy for the ten-year yield; if the fetched DGS10 is below 4.75% at compute time the engine will object. Flagged as a question (REVISE 4), not a rule breach.
7. **ROIC premium.** Bear 0.0; base 0.03; bull 0.05 (at the ceiling, not above it); all `allow_large_premium: false`. Compliant.
8. **Weights** 0.25 + 0.50 + 0.25 = 1.00. **Cost of capital** shared (all `cost_of_capital_override: null`).
9. **Tax rate (13%).** Damodaran's convention is the company's effective rate on operating income in the explicit years, moving to the marginal rate in the terminal year. Marvell's GAAP effective rates are not usable as is: FY2026's 12.4% is on pretax income that includes the 1.8B divestiture gain, and H1 FY2027's 25.8% is on pretax income depressed by the non-deductible 433.7 earn-out charge that the analyst correctly keeps out of operating income. Adding that charge back (net of the 131.0 hedge gain the 10-Q says is netted for tax) gives 119.1 / 764.3 = 15.6% for the half year; the FY2026 figure cannot be cleaned because the tax on the gain is not disclosed separately. So the GAAP evidence points to a low-to-mid-teens rate, and management's forward "approximately 13% in fiscal 2028" is inside that range and is the only forward-looking figure in the sources. Defensible; a sensitivity at 15–16% would be a reasonable owner check. The move to 25% in the terminal year follows §18.2.

---

## 3. Consistency checks

### (a) Growth vs reinvestment

Implied yearly reinvestment from the engine's rule Reinv_t = (Rev_{t+1} − Rev_t) / sales-to-capital, with Rev_6 = Rev_5 × (1 + g_5):

| $M | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 | Five-year total |
|---|---|---|---|---|---|---|
| Bear revenue (S/C 1.4) | 12,474 | 13,098 | 11,788 | 12,142 | 12,749 | — |
| Bear reinvestment | 446 | **−936** | 253 | 434 | 455 | 652 |
| Base revenue (S/C 1.8) | 14,648 | 19,042 | 22,470 | 24,717 | 26,200 | — |
| Base reinvestment | 2,441 | 1,904 | 1,248 | 824 | 873 | 7,290 |
| Bull revenue (S/C 2.2) | 15,120 | 21,471 | 27,912 | 32,937 | 36,230 | — |
| Bull reinvestment | 2,887 | 2,928 | 2,284 | 1,497 | 1,647 | 11,243 |

History from the filings, on the analyst's definition (capex − depreciation + working-capital outflow, acquisitions separately):

| Year | Revenue change | Capex − D&A | Working-capital outflow | Organic reinvestment | Organic S/C | Acquisitions (cash; stock) | All-in S/C |
|---|---|---|---|---|---|---|---|
| FY2023 | +1,457 | −99 | 650 | 551 | 2.6 | 112 | 2.2 |
| FY2024 | −412 | +37 | −58 (inflow) | −21 | n/m | 0 | n/m |
| FY2025 | +260 | −20 | −129 (inflow) | −149 | n/m | 10 | n/m |
| FY2026 | +2,427 | +6 | 1,100 | 1,106 | 2.2 | 0 | 2.2 |
| H1 FY2027 (TTM gain) | +1,256 | +94 | 660 | 754 | 1.7 | 1,271; 2,500 | 0.28 |

The analyst's 2.2 / 2.2 / 1.7 figures reproduce (the FY2023 organic figure is 2.6 before the 112 of acquisitions the analyst folds in). Base at 1.8 sits between the two organic growth years and the prepayment-heavy first half of FY2027; bull at 2.2 equals the organic growth-year ratio; bear at 1.4 early and 1.0 late assumes growth bought with deals. Reinvestment of 2.4B in base year 1 against a 4.4B revenue step is 56% of the increment, versus 45% in FY2026 and 60% in H1 FY2027: plausible. The one problem is the bear: because year 3 revenue falls 10%, the lagged rule makes year-2 reinvestment −936, a cash release that lifts the bear's free cash flow. Marvell's own downturn in FY2024 released only 58 of working capital on a 412 revenue decline (10-K FY2024 l.1569), so the release is far larger than history supports. See REVISE 2.

Excluding Celestial and XConn from the base and bull early ratio is defensible: the 4.0B was spent before the base year ends, sits in invested capital already, and any revenue from it lands inside the growth path.

### (b) Margin path vs the economics (business.md §3–§4)

Bridge from management's non-GAAP operating margin to GAAP: GAAP = non-GAAP − stock pay − acquired amortization − other items. Inputs: stock pay run rate 326.2 × 4 = 1,305 a year (8.8 points of TTM revenue, having doubled); amortization from the 10-Q schedule; "other" about 0.3 points.

| | Revenue | Non-GAAP margin | Stock pay | Amortization | GAAP margin implied | YAML |
|---|---|---|---|---|---|---|
| Base year 1 (H2 FY2027 + H1 FY2028) | 14,648 | Q3 guide 58.0% − 655/3,150 = 37.2%; Q4 entering 38–40; H1 FY2028 ≈ 39 → ≈ 38.4% | 1,305 → 8.9 pts | 385.3 + ½ × 292.7 = 532 → 3.6 pts | 38.4 − 8.9 − 3.6 − 0.3 = **25.6%** | 0.25 |
| Base year 2 (H2 FY2028 + H1 FY2029) | 19,042 | 39.5% (upper end) | 1,305 → 6.9 pts (or 8.8 if it grows with revenue) | ½ × 292.7 + ½ × 139.6 = 216 → 1.1 pts, plus 0.4–0.9 once Celestial IPR&D amortizes | 39.5 − 6.9 − 1.6 − 0.3 = **30.7%** (28.8% if stock pay stays at 8.8 pts) | 0.29 |
| Base year 5 | 26,200 | Management's rule: opex grows at half the rate of revenue. Revenue ×2.18 from FY2027's 12,000 → opex ×1.59 → 4,055 = 15.5%; at 58% gross → 42.5%. At 56% gross (custom mix pressure) → 40.5% | 7.5 pts | ~0.8 pts | **33.9%** at 58% gross; **31.9%** at 56% | 0.29 |
| Bull year 5 | 36,230 | Revenue ×3.02 → opex ×2.01 → 5,126 = 14.1%; at 58% gross → 43.9% | 6 pts (analyst) or 8.8 if unchanged | ~0.5 pts | **37.1%** at 6 pts of stock pay; **34.3%** at 8.8 pts | 0.35 |
| Bear year 1 | 12,474 | H2 FY2027 at guided cost lines: Q3 3,150 × 53.4% − 1,015 = 667; Q4 3,693 × 53.4% − 1,030 = 942; H1 FY2028 5,631 × 53% − 2,030 = 954 | included | included | 2,563 / 12,474 = **20.5%** | 0.21 |
| Bear year 3 | 11,788 | Gross 55%, opex 3,000 (R&D still rising) → 29.6% | 1,300 → 11 pts | 140 → 1.2 pts | **17%**; 12% needs gross near 52% or opex near 3,300 | 0.12 |

Conclusion: the base case's 30% is reachable with room to spare under management's own opex rule; the analyst's choice to hold 30% and trim to 29% is conservative relative to that rule and consistent with the gross-margin pressure the CFO named. The bull's 35% requires stock pay to fall from 8.8 to about 6 points of revenue as well as gross margin holding at 58%; with stock pay unchanged as a share of revenue it lands near 34%, so the bull margin is at the plausible edge, not beyond it. The bear's 12% in year 3 is harsher than the fixed-cost arithmetic alone produces (about 17%); acceptable for a bear case, but the reason should say what extra pain it assumes (the reason currently asserts "about 12%" without the arithmetic).

### (c) Year-5 revenue vs market size and vs delivery

| Scenario | Year-5 revenue | Multiple of base | Share of the 55B FY2029 custom-only market |
|---|---|---|---|
| Bear | 12,749 | 1.35× | 23% |
| Base | 26,200 | 2.77× | 48% |
| Bull | 36,230 | 3.83× | 66% |

All pass the "possible" test, comfortably so because the 55B figure covers one product group in FY2029 and Marvell's revenue also includes interconnect, switching and communications. Against delivery: the scorecard records 10 of 12 Q1 claims met, FY2027 raised from "nearly $11.5 billion" to "roughly $12 billion" and FY2028 from 16.5 to 18 billion. Base year 2 (19.0B for the TTM to August 2028) is a haircut on management's path (FY2028 at 18B plus a first half of FY2029 that "accelerates significantly"); bull year 2 (21.5B) is roughly management's implied path if FY2029 custom reaches the "over $10 billion" target from a little over 4 billion in FY2028 (Q1 transcript l.100–106). The market-size cell should be replaced after the Investor Day, as the analyst says.

### (d) Bear internal consistency (32% then −10%)

The year-1 reason says "even a flat first half of FY2028 puts the TTM near 12.5 billion". That is wrong. FY2027 at roughly 12,000 implies H2 FY2027 ≈ 12,000 − 5,157 = 6,843 (Q3 guided 3,150, Q4 ≈ 3,693). A flat H1 FY2028 at the H2 FY2027 level gives a TTM of 13,686 (+45%); flat at the Q4 run rate gives 14,229 (+51%). The YAML's 12,474 (+32%) requires H1 FY2028 ≈ 5,631, an 18% fall from H2 FY2027 within months of a guided acceleration. That is a legitimate bear event, but it is a cut, not the "stall" the story describes, and the path then zigzags: year 2 at 13,098 implies H2 FY2028 ≈ 7,467 (+33% half-on-half), and year 3 at 11,788 implies H1 FY2029 ≈ 4,321 (−42% half-on-half). A smooth bear reaching the same year-5 endpoint would be roughly [0.45, −0.05, −0.10, 0.03, 0.05] (13,703 → 13,018 → 11,716 → 12,067 → 12,671), with year-1 margin then about 23% by the same cost arithmetic. See REVISE 1.

---

## 4. 3P test

- **Bear.** Possible: 12.7B is a quarter of the FY2029 custom market alone. Plausible: margins of 12–21% with a fixed R&D bill and 11 points of stock pay match the cost structure in business.md §3, and cancellable purchase orders plus 82% of revenue from ten customers make a sudden cut mechanically easy (business.md §6). Probable: the scorecard shows management meeting 10 of 12 claims and raising guidance twice, and Marvell has just committed 8.5B of purchase commitments to foundries (outlook.md §1), so this is the against-the-evidence case; the FY2024 precedent (revenue −7% after FY2023's boom) keeps it at a 25% weight. The path itself needs the fix in REVISE 1.
- **Base.** Possible: 26.2B is under half of a market figure that covers only one product group. Plausible: 30% GAAP is below what management's "opex at half the rate of revenue" rule produces (§3b), and reinvestment at 1.8 sales-to-capital sits between the FY2026 and H1 FY2027 organic ratios. Probable: it tracks guidance for two years, and guidance has been met or raised at every check so far (scorecard, Q2 FY2027 table); the fade thereafter uses management's own "30%-plus" cloud-capex planning assumption.
- **Bull.** Possible: 36.2B is two-thirds of the FY2029 custom market and below the "$120 billion divided by 6.5" the CEO called "not wrong" (Q2 transcript l.161–165). Plausible: 35% requires stock pay to fall to about 6 points of revenue and gross margin to hold at 58% while custom mix rises, which is at the edge (§3b); reinvestment at 2.2 equals the organic growth-year history. Probable: it needs the FY2029 acceleration and the Google warrant to convert to revenue, neither of which is in the scorecard yet; 25% weight is right.
- **Management.** Not computable; the two guided points (FY2027 ≈ 12B, FY2028 ≈ 18B) are exactly what the scorecard shows management delivering against, so filling what exists and stopping is correct.

---

## 5. Reader check

The three stories read cleanly for a 16-year-old: short sentences, one or two defining numbers each, no undefined acronyms. Changes made directly in the YAML (wording only):

1. Base story: "the custom chip ramp" → "the custom chip ramp-up"; "today's trailing level" → "the last twelve months' level" ("trailing" is analyst jargon).
2. Bear story: "the interconnect business loses a speed generation" → "a competitor beats Marvell to the next speed step in interconnect" (plain statement of the same event).
3. Bear `revenue_growth.reason`: "the FY2025 data-center lull" → "with data-center revenue also down that year" attached to FY2024; business.md §2 shows data center fell in FY2024 (2,408.8 → 2,216.7) and rose 88% in FY2025, so "FY2025 lull" was a factual slip.
4. Management guidance item "Q3 FY2027 gross-margin driver": the quote now uses the transcript's self-corrected phrase "the sequential headwind in the fiscal third quarter" instead of the garbled "headroom", matching outlook.md §4.

Not changed: several reasons run four to six sentences against §18.4's "one to three"; they carry sourced arithmetic the owner may want, so trimming is left to the analyst (REVISE 5).

---

## 6. Verdict: REVISE

1. **`scenarios.bear.revenue_growth.values` and `.reason` (and `scenarios.bear.operating_margin.values[0]`, `scenarios.bear.story` to match).** The reason's arithmetic is wrong: a flat first half of FY2028 gives a year-1 TTM of about 13.7B (+45%), not 12.5B; the +32% in the YAML requires an 18% drop in H1 FY2028 versus H2 FY2027, and the path then zigzags half-on-half (+33%, then −42%). Fix: either smooth the path to roughly [0.45, −0.05, −0.10, 0.03, 0.05] (same 12.7B endpoint; year-1 margin then about 0.23 by the analyst's own Q3-guide arithmetic) and keep the story's "stalls, then falls"; or keep 0.32 and rewrite the reason and story to say orders are cut sharply in the first half of FY2028, with year 2 at about 0.0 rather than +0.05 so the halves do not rebound before the year-3 fall.
2. **`scenarios.bear.reinvestment_override.values[1]` (question).** With year 3 at −10%, the lagged rule gives year-2 reinvestment of −936 (a cash release) at sales-to-capital 1.4, lifting bear free cash flow. Marvell's FY2024 downturn released only 58 of working capital on a 412 revenue fall. Either set an override of 0 (or small positive net capex, roughly 100) for the year before the decline, or state in the reason that the Damodaran-convention release is accepted.
3. **`base_year.amortization_of_acquired_intangibles.reason` and the three `operating_margin.reason` cells.** Add the Q2 10-Q's updated schedule as of August 1, 2026 (remainder of FY2027 385.3; FY2028 292.7; FY2029 139.6; FY2030 117.2; FY2031 60.8; 10-Q Note 5) alongside the 10-K figures, and state that the 997.0 of Celestial and XConn in-process R&D is not amortized until products ship, then over 6–13 years (77–166 a year), so "roughly 70 a year" is the low end. No input value changes.
4. **`scenarios.*.terminal.growth.value` = 0.0475 (question for the owner).** This is the planner's risk-free proxy with `allow_above_riskfree: false`; if the fetched ten-year yield is below 4.75% at compute time the engine will flag it. Confirm the proxy or set a lower value.
5. **Reason length (minor).** `base_year.operating_income_gaap.reason`, the three `sales_to_capital.reason` cells, `bridge.dilution_note` and `scenarios.management.reason` exceed §18.4's one-to-three sentences. Optional trim; the content is sourced and correct.
6. **`base_year.revenue.reason` supplemental page tag (minor).** In the text dump the eight-quarter income statement (revenue, operating income) is on the fourth page and the cash-flow lines (stock pay, amortization) on the fifth; the YAML tags both "p.5". Confirm against the PDF page numbering before compute.

Items 1 and 2 change numbers or judgments and are for the analyst; 3–6 are wording or owner questions. Everything in the base year, bridge, cost of debt and market-size cells re-derives exactly; no FAILs.

---

## Cycle 2 — re-check of the changed cells

_Scope: only the cells the analyst changed after the cycle-1 REVISE list. Same method; line numbers refer to the cached text files._

| Changed cell | Claim in the YAML | Reviewer re-derivation | Result |
|---|---|---|---|
| `bear.revenue_growth.values` [0.45, −0.05, −0.10, 0.03, 0.05] and reason | H2 FY2027 ≈ 6,843; flat H1 FY2028 → TTM ≈ 13,700, +45%; year 5 ≈ 12.7B, 1.34× | 12,000 − 5,157.1 = 6,842.9; 2 × 6,842.9 = 13,685.8 / 9,450.3 = 1.448; path 13,702.9 → 13,017.8 → 11,716.0 → 12,067.5 → 12,670.9 = 1.341× | OK |
| `bear.operating_margin.values[0]` 0.23 and reason | H2 FY2027 at guided cost lines plus a flat H1 FY2028 ≈ 23% | Q3 3,150 × 53.4% − 1,015 = 667; Q4 3,693 × 53.4% − 1,030 = 942; H1 FY2028 6,843 × 53% − 2,030 = 1,597; 3,206 / 13,686 = 23.4% (release l.23–29) | OK |
| `bear.operating_margin.reason`, year 3 | fixed-cost arithmetic alone gives ~17%; 12% assumes gross margin toward 50% (41% in FY2025) | matches cycle-1 §3(b); FY2025 GAAP gross margin 41.3% (business.md §3 table; 10-K FY2026, Item 7) | OK |
| `bear.reinvestment_override.values` [970, 100, null, null, null] | S/C rule would release ~490 and ~930; 970 = ~780 of remaining FY2027 prepayments + ~190 net capex | (13,017.8 − 13,702.9)/1.4 = −489; (11,716.0 − 13,017.8)/1.4 = −930. Prepayments: "approximately $1 billion" (Q2 transcript l.83); balance 263.1 at May 2 (Q1 10-Q l.1267) → 487.0 at Aug 1 (Q2 10-Q l.751), +223.9; 1,000 − 223.9 = 776. Net capex (282.4 − 188.5) × 2 = 188 (Q2 10-Q l.235, l.253). 776 + 188 = 964 ≈ 970. FY2024 release 57.8 (10-K FY2024 l.1569) | OK; source tag now includes the Q1 10-Q (reviewer edit) |
| Amortization reasons (base-year memo; bear, base, bull `operating_margin.reason`) | 10-Q schedule 385.3 / 292.7 / 139.6 / 117.2 / 60.8; IPR&D 997.0, 6–13 years, 77–166 a year | 10-Q l.451–459: remainder of 2027 385.3, 2028 292.7, 2029 139.6, 2030 117.2, 2031 60.8, total 1,049.6; IPR&D 951.0 + 46.0 = 997.0, "6 to 13 years" (l.427–429, l.449); 997/13 = 76.7, 997/6 = 166.2 | OK |
| Base `operating_margin.reason` arithmetic | 3.6 pts amortization year 1; 1–2 pts from year 2; stock pay 7–9 pts | 385.3 + 146.4 = 531.7 / 14,648 = 3.6%; 146.4 + 69.8 = 216.2 / 19,042 = 1.1% plus IPR&D; 1,300 / 15,000 = 8.7%, 1,300 / 19,000 = 6.8% | OK |
| `terminal.growth.value: riskfree` (bear, base, bull) | equals the fetched ten-year rate by rule | §18.4 rule 5 default; `allow_above_riskfree: false`; roic premiums unchanged (0.0 / 0.03 / 0.05) | OK, by spec |
| Trimmed reasons (`operating_income_gaap`, three `sales_to_capital`, `dilution_note`, `management.reason`) | arithmetic moved to YAML comments | comment tables re-added: FY2023 13.6 → ~107 and 663 → 2.2; FY2026 5.5 → ~441 and 1,106 → 2.2; H1 FY2027 organic 754 → 1.7, all-in 4,524 → 0.28; restructuring 25.3 and "other" 86.8 with note tags (10-K Note 4 = Restructuring, 10-Q Note 8 = Restructuring, Note 4 = Business Combinations) | OK |
| Supplemental page tag "p.5" kept | analyst checked form-feed pages | Form feeds fall at lines 7, 34, 58, 100, 138, 174, 196, 232, 275, 294, so page 5 = lines 100–137 (income statement, "Net revenue" l.106, with the stock-pay-by-line footnote), page 6 = cash flow, page 8 = lines 196–231 (reconciliation, the "Other" items l.208–217). The IR gatherer's notes tag the balance sheet p.4 and the income statement p.5 the same way. Cycle-1 minor item 6 was wrong and is withdrawn | OK |

Story, values and reasons now agree: the story's "as they did in 2023 … stops growing after the first year, slips a little in year two and falls by about a tenth in year three" matches [+45%, −5%, −10%] and the reason's "orders then slip 5% in year 2 and 10% in year 3". The year-1 override of 970 is also consistent with the bear story: the prepayments are unconditional commitments (Q2 10-Q Note 9), so they are paid even if orders are cut.

Wording-only edits made in this cycle: (1) bear story, "stops growing after the first year and then falls" → "stops growing after the first year, slips a little in year two and falls", so the story matches the −5% in year 2; (2) `bear.reinvestment_override.source` gains "10-Q Q1 FY2027, Note 14", the filing that supplies the May 2 balance of 263.1 behind the 223.9 increase.

YAML parses; weights sum to 1.0; management case remains `computable: false`.

**Cycle 2 verdict: PASS.**
