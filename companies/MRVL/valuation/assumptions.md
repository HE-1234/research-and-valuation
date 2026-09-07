# MRVL valuation assumptions as of FY2027-Q2

This file is a read-only view of the valuation inputs for Marvell Technology, Inc. (MRVL), held in `assumptions.yaml`. Every number and every sentence below comes from that file; nothing is computed here. To change a number, use the app (`uv run --extra app valuation-app`), which saves into the YAML, records the change, and rewrites this file. A dash (—) marks a cell that is empty in the file: the analyst had nothing defensible to put there, or the item is not given. Rates are stored as decimals and shown here as percentages; money is in USD millions.

| Item | Value |
|---|---|
| Ticker | MRVL |
| Company | Marvell Technology, Inc. |
| As-of quarter | FY2027-Q2 |
| As-of date (quarter cutoff) | 2026-08-28 |
| Drafted | 2026-09-07 |
| Horizon | 5 explicit years, then a terminal value |
| Currency and units | USD, millions |

## 1. The stories

Each story is copied word for word from `assumptions.yaml`.

### Bear (weight 25.0%)

The AI building boom cools within two years, and the handful of cloud giants that make up most of Marvell's sales cut orders at short notice, as they did in 2023. One of them moves a custom chip program in-house or to a rival, and a competitor beats Marvell to the next speed step in interconnect. Revenue stops growing after the first year, slips a little in year two and falls by about a tenth in year three, while the fixed research bill and the doubled stock pay stay, so margins fall back toward where they were before the AI boom. Marvell keeps buying companies to fill the gap, so each dollar of new sales costs more capital than it has recently.

### Base (weight 50.0%)

Marvell delivers roughly what it has promised for the next two years: the custom chip ramp-up for its big cloud customers arrives, interconnect keeps leading, and revenue about doubles from the last twelve months' level within two years. After that the AI spending cycle matures, growth slows toward that of a normal chip company, and pricing pressure on custom chips keeps gross margins from rising. Operating margins improve sharply anyway, partly because the business grows over a fixed research bill and partly because the amortization from old acquisitions runs off; stock pay stays as a real cost. Reinvestment is mostly working capital and factory prepayments, with an acquisition now and then.

### Bull (weight 25.0%)

The Google agreement and the second large custom program make Marvell the default outside designer for cloud companies' own AI chips, and scale-up optics becomes a large new business on top of interconnect. Revenue grows to nearly four times today's level over five years, and operating margins rise above the current long-term target as research spending is spread over a far bigger base. Customers stay locked in for whole chip generations, so the business earns more than its cost of capital for longer than usual. Growth is funded from cash flow without major acquisitions.

### Management (not weighted; not computed)

(no story given)

Why this case is not computed: Management has given multi-year revenue targets (FY2027 roughly 12 billion, FY2028 approximately 18 billion) and a non-GAAP margin target (upper end of 38–40% in FY2028), so rule 4's threshold is met, but nothing numeric exists beyond FY2028 (model year 2), so years 3–5 would be extrapolation rather than interpolation between guided points. GAAP margins beyond the Q3 guide also need a stock-pay assumption management does not give, and sales-to-capital is not guided. The October 6, 2026 Investor Day promises revenue 'out until the end of the decade' and a new margin model, after which the owner can complete this case.

## 2. Scenario inputs

Rows are inputs and columns are cases. Per-year cells read year 1 / year 2 / ... in order. The reasons and sources behind each cell follow the table.

| Input | Bear | Base | Bull | Management |
|---|---|---|---|---|
| Weight | 25.0% | 50.0% | 25.0% | not weighted |
| Computable | always | always | always | no |
| Revenue growth, years 1-5 | 45.0% / -5.0% / -10.0% / 3.0% / 5.0% | 55.0% / 30.0% / 18.0% / 10.0% / 6.0% | 60.0% / 42.0% / 30.0% / 18.0% / 10.0% | 58.7% / 20.0% / — / — / — |
| Operating margin, years 1-5 | 23.0% / 19.0% / 12.0% / 15.0% / 17.0% | 25.0% / 29.0% / 30.0% / 30.0% / 29.0% | 26.0% / 31.0% / 34.0% / 35.0% / 35.0% | 21.2% / — / — / — / — |
| Sales-to-capital, years 1-5 | 1.40 | 1.80 | 2.20 | — |
| Sales-to-capital, years 6-10 of the 10-year reference | 1.00 | 1.20 | 1.50 | — |
| Reinvestment override, years 1-5 (USD millions) | 970 / 100 / — / — / — | — / — / — / — / — | — / — / — / — / — | — / — / — / — / — |
| Tax rate, explicit years | 13.0% | 13.0% | 13.0% | 13.0% |
| Tax rate, terminal year onwards | 25.0% | 25.0% | 25.0% | 25.0% |
| Cost of capital override | — | — | — | — |
| Terminal growth | the run's risk-free rate | the run's risk-free rate | the run's risk-free rate | — |
| Terminal growth may exceed the risk-free rate | no | no | no | no |
| Terminal return on capital: points above the cost of capital | 0.00% | 3.00% | 5.00% | — |
| A premium above 5 points is allowed | no | no | no | no |

### Bear: reasons

- **Revenue growth** — Year 1 is mostly locked by guidance: FY2027 at roughly 12 billion implies a second half of about 6,843 (Q3 guided at 3,150), and a flat first half of FY2028 at that level gives a TTM of about 13,700, 45% above the 9,450 base (computed; outlook.md §4). Orders then slip 5% in year 2 and 10% in year 3 as the custom ramp stalls and cloud spending pauses, a repeat of FY2024 (revenue −7%, with data-center revenue also down that year; business.md §2 table, §6 risks 1–3), followed by a slow recovery. Year-5 revenue about 12.7 billion, 1.34× the base (computed). [Q2 FY2027 release; Q2 FY2027 call; 10-K FY2026, Item 7]
- **Operating margin** — Year 1: the second half of FY2027 at the guided cost lines (Q3: 53.4% gross margin less 1,015 of operating expenses on 3,150 = 21%; Q4 about 25% on higher revenue) plus a flat first half of FY2028 gives about 23% (computed) [Q2 FY2027 release]. Acquired amortization falls from 9.4 points of revenue to about 1 point by year 3 under the 10-Q schedule (385.3 for the rest of FY2027, 292.7 in FY2028, 139.6 in FY2029, plus 77–166 a year once the 997.0 of Celestial and XConn in-process R&D ships and amortizes over 6–13 years), which props margins up even here [10-Q Q2 FY2027, Note 5]. But stock pay of about 1.3 billion a year is 11 points on a 12 billion base and R&D is fixed, so the 12% in year 3 assumes, beyond that fixed-cost arithmetic (which alone gives about 17%), that custom-heavy mix and price cuts push GAAP gross margin toward 50% (it was 41% in FY2025) while operating expenses are not cut (business.md §3–§4) [Q2 FY2027 supplemental, p.5; 10-K FY2026, Item 7]. [Q2 FY2027 release; 10-Q Q2 FY2027, Note 5; 10-K FY2026, Item 7; Q2 FY2027 supplemental, p.5]
- **Sales-to-capital** — On the formula revenue change / (capex − depreciation + acquisitions) Marvell's history is meaningless (FY2023 about 107, FY2026 about 441, FY2024–FY2025 negative) because net capex is near zero; adding the working-capital outflows the 10-Ks report gives 2.2 in FY2023, 2.2 in FY2026 and 1.7 in H1 FY2027, and counting the Celestial and XConn price (1,271 cash plus 2.5 billion in stock) drops FY2027 below 0.6 (year-by-year arithmetic in the comment above; business.md §3–§4). Bear assumes growth has to be bought with deals again, as in FY2022 (3,555 cash for Inphi and Innovium) and FY2027, so 1.4 early and 1.0 late [10-K FY2024, Item 7; Item 8; 10-K FY2026, Item 7; Item 8; 10-Q Q2 FY2027, Item 1; Item 2]. [10-K FY2024, Item 8; 10-K FY2026, Item 7; Item 8; 10-Q Q2 FY2027, Item 1; Note 14]
- **Reinvestment override** — Years 1 and 2 precede revenue declines, so the sales-to-capital rule would book cash releases of about 490 and 930, far beyond the 58 of working capital Marvell released on a 412 revenue fall in FY2024. Year 1 is therefore set to what is already committed: roughly 780 of the guided 1 billion of FY2027 capacity prepayments still to be paid after the first half (the prepayment balance rose 223.9 to 487.0 in Q2) plus net capex of about 190 at the first-half run rate (282.4 capex less 188.5 depreciation, doubled), about 970 in all (computed). Year 2 is set to 100, net capex partly offset by a small working-capital release, and years 3–5 revert to sales-to-capital. [Q2 FY2027 call; 10-Q Q2 FY2027, Note 14; Item 1; 10-Q Q1 FY2027, Note 14; 10-K FY2024, Item 7]
- **Tax rate** — Starts at management's FY2028 non-GAAP tax rate (see base_year.effective_tax_rate) and moves to the 25% marginal rate in the terminal year.
- **Terminal growth** — Equals the fetched ten-year Treasury rate by rule (§18.4 rule 5); no company grows faster than the economy forever.
- **Terminal return on capital premium** — Bear: the moat is assumed gone, so terminal return on capital equals terminal cost of capital.

### Base: reasons

- **Revenue growth** — Year 1 (TTM to Aug 2027) lands at about 14.6 billion, a little under the 15 billion midpoint between management's FY2027 'roughly $12 billion' and FY2028 'approximately $18 billion' (outlook.md §4), a haircut for slippage in the custom ramp; year 2 (TTM to Aug 2028) at about 19.0 billion means FY2028 is delivered roughly as guided but the FY2029 acceleration is muted. Years 3–5 fade toward the risk-free rate as cloud spending growth moderates, the assumption management itself used a quarter ago ('30%-plus range' for cloud capex, outlook.md §6), giving year-5 revenue of about 26.2 billion, 2.8× the base (computed). The base tracks guidance for two years rather than discounting it because management has met 10 of 12 graded claims and raised full-year guidance twice (scorecard.md). [Q2 FY2027 call; Q2 FY2027 release; Q1 FY2027 call]
- **Operating margin** — Bridge from management's non-GAAP target to GAAP: non-GAAP operating margin enters 38–40% in Q4 FY2027 and reaches the upper end through FY2028 (outlook.md §4); subtract stock pay of 7–9 points (1.3 billion run rate on 15–19 billion of revenue, kept as a cost) and acquired amortization of about 3.6 points in year 1 (385.3 for the rest of FY2027 plus half of FY2028's 292.7) falling to 1–2 points from year 2 (half of 292.7 plus half of FY2029's 139.6, plus 77–166 a year once the 997.0 of Celestial and XConn in-process R&D ships and amortizes over 6–13 years), which gives about 25% in year 1 and 29–31% from year 2 (computed) [10-Q Q2 FY2027, Note 5; Q2 FY2027 supplemental, p.5]. Year 1 also reconciles bottom-up from the Q3 guide (GAAP margin 21%), Q4 (about 25%) and the first half of FY2028 (about 28%) [Q2 FY2027 release]. Held at 30% and trimmed to 29% in year 5 for the custom-mix gross-margin pressure the CFO named and the 'significant pricing pressures' the 10-K warns of (business.md §3; outlook.md §6) [10-K FY2026, Item 1A]. [Q2 FY2027 call; Q2 FY2027 release; 10-Q Q2 FY2027, Note 5; Q2 FY2027 supplemental, p.5]
- **Sales-to-capital** — Organic history including working capital is 2.2 in the growth years FY2023 and FY2026 and 1.7 in H1 FY2027 once capacity prepayments began (table in the comment above the bear cell; business.md §3–§4). Base uses 1.8 for years 1–5 (working capital about 30% of revenue plus prepayments and net capex) and 1.2 for the fade years, when growth is assumed to be bought partly by acquisition as in FY2022 and FY2027. Celestial and XConn (4.0 billion of consideration, revenue 'not material' so far) are excluded from the early ratio because the spend is already in invested capital and any revenue from it sits in the growth path [10-K FY2024, Item 8; 10-Q Q2 FY2027, Note 4; Item 2]. [10-K FY2024, Item 8; 10-K FY2026, Item 7; Item 8; 10-Q Q2 FY2027, Item 1; Note 4]
- **Reinvestment override** — No specific capex guidance; the FY2027 prepayment figure is only one component of reinvestment, so sales-to-capital is used throughout.
- **Tax rate** — Management's FY2028 non-GAAP tax rate (see base_year.effective_tax_rate), rising to the 25% marginal rate in the terminal year.
- **Terminal growth** — Equals the fetched ten-year Treasury rate by rule (§18.4 rule 5); no company grows faster than the economy forever.
- **Terminal return on capital premium** — Three points above terminal cost of capital: custom programs lock a customer in for a whole chip generation, interconnect wins each speed transition first, and Google is now tied in through a revenue-vesting warrant (business.md §5; Q2 FLAG). Kept below Damodaran's 4 points for Alphabet because ten customers are 82% of revenue and one distributor 44%, and the 10-K says customers 'may begin developing and making their own semiconductor solutions' (business.md §6).

### Bull: reasons

- **Revenue growth** — Year 1 at about 15.1 billion is the midpoint of management's FY2027 and FY2028 targets taken at face value; year 2 at about 21.5 billion reflects FY2028 hit and custom 'accelerate significantly in fiscal 2029' (outlook.md §3–§4). Years 3–5 credit part of the Google warrant arithmetic the CEO did not dispute ($120 billion of custom purchases over 6.5 years for full vesting; 'your math is not wrong', outlook.md §6) while still fading. Year-5 revenue about 36.2 billion, 3.8× the base (computed), below the $55 billion custom market alone for FY2029. [Q2 FY2027 call; 8-K 2026-08-19; Q1 FY2027 call]
- **Operating margin** — Non-GAAP operating margin moves above the 38–40% target to the low-to-mid 40s, the direction the CFO signalled when promising to 'reset that long-term target model' at the October 2026 Investor Day (outlook.md §4), because R&D is fixed (business.md §3). Less stock pay falling toward 6 points of revenue as revenue outgrows headcount, and acquired amortization of about 1 point once the FY2027 roll-off is done (10-Q schedule: 292.7 in FY2028, 139.6 in FY2029, plus 77–166 a year when the 997.0 of Celestial and XConn in-process R&D starts amortizing over 6–13 years) [10-Q Q2 FY2027, Note 5]. [Q2 FY2027 call; 10-Q Q2 FY2027, Note 5]
- **Sales-to-capital** — Matches the organic ratio including working capital achieved in FY2023 and FY2026 (2.2; arithmetic in the bear case), on the view that growth comes from programs already won and needs no further acquisitions; 1.5 late as growth normalises. [10-K FY2024, Item 8; 10-K FY2026, Item 7; Item 8]
- **Reinvestment override** — No specific capex guidance; sales-to-capital is used throughout.
- **Tax rate** — Management's FY2028 non-GAAP tax rate, rising to the 25% marginal rate in the terminal year.
- **Terminal growth** — Equals the fetched ten-year Treasury rate by rule (§18.4 rule 5); no company grows faster than the economy forever.
- **Terminal return on capital premium** — Five points, the ceiling without an override: in this case the customer lock-in in business.md §5 (multi-generation custom programs, first-to-market interconnect, equity ties to NVIDIA and Google) proves durable. Still well under Damodaran's 11 points for Nvidia because Marvell's customers design competing chips themselves.

### Management: reasons

- **Computable: no** — Management has given multi-year revenue targets (FY2027 roughly 12 billion, FY2028 approximately 18 billion) and a non-GAAP margin target (upper end of 38–40% in FY2028), so rule 4's threshold is met, but nothing numeric exists beyond FY2028 (model year 2), so years 3–5 would be extrapolation rather than interpolation between guided points. GAAP margins beyond the Q3 guide also need a stock-pay assumption management does not give, and sales-to-capital is not guided. The October 6, 2026 Investor Day promises revenue 'out until the end of the decade' and a new margin model, after which the owner can complete this case.
- **Revenue growth** — Year 1: the TTM to Aug 2027 ends six months after FY2027 (roughly $12 billion) and six months before FY2028 (approximately $18 billion), so the midpoint 15,000 is used: 15,000 / 9,450.3 − 1 = 0.587 (computed). Year 2: FY2028's 18,000 is the nearest guided point (six months before the TTM to Aug 2028): 18,000 / 15,000 − 1 = 0.20; this understates year 2 because the window also contains the first half of FY2029, which management says will 'accelerate significantly' without a number. Years 3–5: no guidance. [Q2 FY2027 call; Q2 FY2027 slides, p.8]
- **Operating margin** — Year 1 is one quarter's guidance applied to a full year, an explicit approximation: Q3 FY2027 GAAP gross margin midpoint 53.4% less GAAP operating expenses of 1,015 on revenue of 3,150 (32.2%) = 21.2% (computed). It understates the year because Q4 and FY2028 carry the 38–40% non-GAAP target and lower amortization, but the GAAP conversion needs stock pay, which management does not guide; years 2–5 therefore null. [Q2 FY2027 release]
- **Sales-to-capital** — Not guided; the only reinvestment figure is 'approximately $1 billion of capacity prepayments' in FY2027, which cannot be turned into a sales-to-capital ratio without capex and working-capital guidance.
- **Reinvestment override** — No capex guidance; the prepayment figure alone does not make a net reinvestment number.
- **Tax rate** — Management's own FY2028 non-GAAP tax rate of 'approximately 13%' (11% for FY2027); terminal at the marginal rate.
- **Terminal growth** — Management gives no long-run growth rate.
- **Terminal return on capital premium** — Management gives no return-on-capital target.

## 3. Base year (Q3 FY2026 – Q2 FY2027 (TTM ending 2026-08-01))

| Item | USD millions | Reason | Source |
|---|---|---|---|
| Revenue, trailing twelve months | 9,450.3 | FY2026 net revenue 8,194.6 plus six months ended Aug 1, 2026 of 5,157.1 minus six months ended Aug 2, 2025 of 3,901.4 = 9,450.3. Cross-check: the four quarters Q3 FY2026 to Q2 FY2027 in the eight-quarter table sum to 2,074.5 + 2,218.7 + 2,417.8 + 2,739.3 = 9,450.3 [Q2 FY2027 supplemental, p.5]. | [10-K FY2026, Item 8; 10-Q Q2 FY2027, Item 1] |
| Operating income, GAAP | 1,561.3 | FY2026 GAAP operating income 1,322.9 plus six months FY2027 of 799.1 minus six months FY2026 of 560.7 = 1,561.3, a 16.5% margin on TTM revenue (computed). Nothing is removed as one-time: restructuring of 25.3 and 86.8 of acquisition, divestiture and legal costs (30.1 of it Celestial deal fees) stay in, because Marvell has booked restructuring every year since FY2024 and closed acquisitions in four of the last six fiscal years, so both recur at intervals (§18.4 rule 1) [10-K FY2026, Note 4; 10-Q Q2 FY2027, Note 4; Note 8; Q2 FY2027 supplemental, p.8]. The 1,830.4 divestiture gain and the 433.7 earn-out revaluation sit below operating income, so nothing is removed for them either [10-K FY2026, Note 1; 10-Q Q2 FY2027, Note 6]. | [10-K FY2026, Item 8; 10-Q Q2 FY2027, Item 1] |
| One-time items | none | — | — |
| Amortization of acquired intangibles (memo) | 892.7 | Cash-flow statement line 'Amortization of acquired intangible assets': FY2026 942.0 plus H1 FY2027 440.1 minus H1 FY2026 489.4 = 892.7, or 9.4 points of TTM revenue (computed). Memo row, stays deducted; the roll-off is built into the margin paths from the 10-Q schedule as of August 1, 2026: 385.3 for the rest of FY2027, 292.7 for FY2028, 139.6 for FY2029, 117.2 for FY2030 and 60.8 for FY2031 (the 10-K's January schedule read 814.0 / 284.8 / 131.8 / 109.5) [10-Q Q2 FY2027, Note 5; 10-K FY2026, Note 5]. On top of that, 997.0 of Celestial and XConn in-process R&D is not amortized until the products ship, then over 6 to 13 years, so a further 77 to 166 a year once it starts. | [10-K FY2026, Item 8; 10-Q Q2 FY2027, Item 1] |
| Stock-based compensation (memo) | 828.9 | FY2026 590.8 plus H1 FY2027 533.8 minus H1 FY2026 295.7 = 828.9, or 8.8 points of TTM revenue (computed). Memo row, never added back. The run rate has roughly doubled: 326.2 in Q2 FY2027 against 153.6 a year earlier, with 190.1 of assumed Celestial awards still to be expensed [Q2 FY2027 supplemental, p.5; 10-Q Q2 FY2027, Note 10]. | [10-K FY2026, Item 8; 10-Q Q2 FY2027, Item 1] |
| Research and development expense (memo) | 2,441.9 | FY2026 2,075.2 plus H1 FY2027 1,393.4 minus H1 FY2026 1,026.7 = 2,441.9, or 25.8% of TTM revenue (computed). Memo row; used only if the capitalize_rnd switch is turned on. | [10-K FY2026, Item 8; 10-Q Q2 FY2027, Item 1] |
| Effective tax rate | 13.0% | Marvell's GAAP tax line is not usable as a rate: FY2026 shows 12.4% but that year's pretax income was dominated by the 1.8 billion divestiture gain, and the six months of FY2027 show 25.8% (119.1 on 461.6) because the 433.7 earn-out charge is not tax-deductible [10-K FY2026, Note 12; 10-Q Q2 FY2027, Note 11]. We therefore use management's non-GAAP tax rate, its own estimate of tax on ongoing operating profit: 11% for FY2027 and 'approximately 13% in fiscal 2028', taking the higher FY2028 figure because model year 1 already runs into FY2028 and the rate rises with earnings [Q2 FY2027 call]. | [Q2 FY2027 call; Q2 FY2027 release] |
| Invested capital | 19,884.9 | Book equity 18,531.6 + debt 4,962.9 + operating lease liabilities 323.2 (59.3 current + 263.9 non-current) − cash 3,932.8 = 19,884.9 at August 1, 2026. About 13.9 billion of it is goodwill and 2.3 billion acquired intangibles, so the ROIC check will look low; it measures the return on everything ever paid for acquisitions, not on new R&D. | [10-Q Q2 FY2027, Item 1; Note 14] |

### Switches

These stay off unless the owner turns them on for a specific company.

| Switch | Setting |
|---|---|
| Add back amortization of acquired intangibles | no |
| Treat research spending as an investment | no |
| Years over which research spending is written off | 5 |
| Research spending history, oldest first (USD millions) | 1,424.2 / 1,784.3 / 1,896.2 / 1,950.4 / 2,075.2 |
| Reinvestment lag | 1 year |

## 4. Bridge from operating assets to equity

| Item | USD millions | Reason | Source |
|---|---|---|---|
| Cash and marketable securities (added) | 3,932.8 | Cash and cash equivalents at August 1, 2026; there is no marketable-securities line on the balance sheet and the MD&A describes only 'cash and cash equivalents' of 3.9 billion [10-Q Q2 FY2027, Item 2]. Time deposits of 194.0 are already inside cash equivalents [10-Q Q2 FY2027, Note 6]. | [10-Q Q2 FY2027, Item 1] |
| Non-operating asset (added): Forward stock purchase contract (cash-settled hedge of the Celestial earn-out) | 131 | A twelve-month, 300.0 notional contract entered April 2026 to offset the share-settled part of the earn-out; carried at fair value in prepaid expenses. It is a financial asset that partly offsets the earn-out claim below. | [10-Q Q2 FY2027, Note 6] |
| Non-operating asset (added): Marketable equity investments | 25.5 | Level 1 securities held in other non-current assets, at quoted prices. | [10-Q Q2 FY2027, Note 6] |
| Non-operating asset (added): Non-marketable equity investments | 156.2 | Stakes in private companies carried at cost less impairment in other non-current assets; not part of operations. | [10-Q Q2 FY2027, Note 14] |
| Debt (subtracted) | 4,962.9 | Net carrying amount of eight series of unsecured senior notes at August 1, 2026; face value 4,999.9 less 37.0 of unamortized discount and issuance cost. No term loans remain (the last was repaid in FY2026) and the 1.5 billion revolver is undrawn. Technology-license payment obligations of 220.0 (96.2 + 123.8) are left out as operating items [10-Q Q2 FY2027, Note 14]. | [10-Q Q2 FY2027, Note 7] |
| Operating lease liabilities (subtracted) | 323.2 | Lease liabilities current 59.3 plus non-current 263.9 at August 1, 2026. | [10-Q Q2 FY2027, Note 14] |
| Minority interests (subtracted) | 0 | The balance sheet shows no non-controlling interest line. | [10-Q Q2 FY2027, Item 1] |
| Other claim (subtracted): Celestial AI contingent consideration (earn-out) liability | 749.5 | Fair value at August 1, 2026, up from 315.8 at closing; payable in up to 233.0 of cash plus about 22.4 million shares if Celestial hits revenue milestones through FY2029. Treated as a debt-like claim at its carrying value; the share-settled part would otherwise appear as dilution, so it is counted here and not in the share count. | [10-Q Q2 FY2027, Note 6; Note 14] |
| Probability of failure | 0.0% | Marvell holds 3.9 billion of cash against 5.0 billion of investment-grade notes with nothing due before FY2029, generated 1.2 billion of operating cash flow in six months, and has an undrawn 1.5 billion revolver [10-Q Q2 FY2027, Note 7; Item 1; Item 2]. | — |
| What the assets would fetch in a failure | 0 | Not needed with probability of failure at zero. | — |
| Diluted shares (millions) | 921.2 | Q2 FY2027 diluted weighted-average shares: 875.6 basic common + 21.8 NVIDIA convertible preferred counted as if converted + 23.8 from stock awards and vested customer warrants. Management guides the same 921 million for Q3 [Q2 FY2027 release]. | [10-Q Q2 FY2027, Item 1; Note 12] |

Dilution note: Not in the 921.2: the August 2026 Google warrant for up to 58,970,907 shares at $206.58 (1,360,867 time-based shares vesting quarterly in year one, about 340,217 a quarter, and 57,610,040 performance shares in 240 tranches of about 240,042, one per $500 million of custom-product revenue from Q3 FY2027 through FY2033; arithmetic from outlook.md §5, claim 12), two earlier customer warrants for 4.2 million shares at $87.77 (1.2 million vested) and 1.0 million at $87.00, the 22.4–24.4 million Celestial earn-out shares already valued in other_claims, and stock pay running at 326.2 a quarter (190.1 of Celestial awards still to expense), against which management 'intend[s] to continue repurchasing shares to manage dilution' [8-K 2026-08-19; 10-Q Q2 FY2027, Note 3; Note 10; Note 15; Q2 FY2027 supplemental, p.5; Q2 FY2027 call].

## 5. Market inputs

| Item | Value in the file | Meaning |
|---|---|---|
| Price (USD per share) | auto | fetched from Yahoo at compute time |
| Risk-free rate | auto | latest ten-year Treasury yield from FRED at compute time |
| Equity risk premium | auto | latest row of Damodaran's cached monthly dataset |
| Mature-market equity risk premium | 4.50% | used for the terminal cost of capital |
| Marginal tax rate | 25.0% | used in the cost of capital build |

## 6. Cost of capital inputs

| Item | Value | Reason | Source |
|---|---|---|---|
| Method | build | — | — |
| Damodaran industry | Semiconductor | Marvell is a fabless chip designer; all revenue is chips sold into data-center and communications equipment (business.md §1–§2). | — |
| Unlevered beta | 1.505 | Unlevered beta corrected for cash for his 66-company US Semiconductor group (1.5046); a beta above 1 means chip earnings swing more than the market's, which is what Marvell's history shows (business.md §3). | [Damodaran betas.xls, Semiconductor, dataset dated 2026-01-05, cached tools/valuation/data/damodaran/betas.csv] |
| Debt to equity (market values) | 0.0257 | Debt 4,962.9 plus operating leases 323.2 = 5,286.1, divided by market capitalisation of 205,934 (223.55 × 921.2 diluted shares) = 0.0257; Marvell carries very little debt relative to what the market says the company is worth. | [10-Q Q2 FY2027, Note 7; Note 14] [Yahoo price 223.55 on 2026-09-04] |
| Pre-tax cost of debt | 5.30% | Coupon on the most recent issue, the 5.300% Senior Notes due 2036 sold April 15, 2026 (effective rate 5.358%), taken as what ten-year money costs Marvell today. The face-weighted average coupon on all eight series is 4.55% (computed), so 5.3% is the conservative choice. | [10-Q Q2 FY2027, Note 7] |
| Terminal cost of capital method | mature | Default: after year 5 the firm is discounted at the risk-free rate plus the mature-market premium, so no company-specific edge is assumed in perpetuity. | — |

## 7. Inputs for the diagnostics

| Item | Value | Reason | Source |
|---|---|---|---|
| Market size in the final forecast year (USD millions) | 55,000 | The only sized addressable market in the sources: the CEO said the data-center custom silicon market Marvell targets is 'a $55 billion TAM' for fiscal 2029, of which Marvell aims for a 20% share (Q&A with Vivek Arya; third-party machine transcript, wording not corrected). It covers only one of the three data-center product groups (not interconnect or switching) and refers to FY2029, not model year 5 (FY2032), so it understates the year-5 market; management promised a fuller long-range sizing at the October 6, 2026 Investor Day, after which the owner may replace it [Q2 FY2027 call]. | [Q1 FY2027 call] |
| Company's own five-year revenue growth per year | — | — | — |
| Company's own five-year average operating margin | — | — | — |

## 8. Management guidance on record

Everything management has said in numbers or in words, whether or not it was used.

| Item | Quote | Source | Used as |
|---|---|---|---|
| Q3 FY2027 revenue | Net revenue is expected to be $3.150 billion +/- 5%. | [Q2 FY2027 release] | revenue_growth year 1 (anchors the second half of FY2027 inside the year-1 window) |
| Q3 FY2027 GAAP gross margin | GAAP gross margin is expected to be 52.9% to 53.9%. | [Q2 FY2027 release] | operating_margin year 1 (midpoint 53.4%) |
| Q3 FY2027 non-GAAP gross margin | Non-GAAP gross margin is expected to be 57.5% to 58.5%. | [Q2 FY2027 release] | not numeric (non-GAAP; GAAP figure used instead) |
| Q3 FY2027 GAAP operating expenses | GAAP operating expenses are expected to be approximately $1.015 billion. | [Q2 FY2027 release] | operating_margin year 1 |
| Q3 FY2027 non-GAAP operating expenses | Non-GAAP operating expenses are expected to be approximately $655 million. | [Q2 FY2027 release] | not numeric (non-GAAP) |
| Q3 FY2027 share count | Diluted weighted-average shares outstanding are expected to be 921 million. | [Q2 FY2027 release] | not numeric (confirms bridge.diluted_shares) |
| Q3 FY2027 GAAP EPS | GAAP diluted net income per share is expected to be $0.53 +/- $0.05 per share. | [Q2 FY2027 release] | not numeric (below the operating line) |
| Q3 FY2027 non-GAAP EPS | Non-GAAP diluted net income per share is expected to be $1.10 +/- $0.05 per share. | [Q2 FY2027 release] | not numeric (non-GAAP, below the operating line) |
| Q3 FY2027 data center | data center revenue forecasted to grow more than 20% sequentially and roughly 75% year-over-year. | [Q2 FY2027 call] | not numeric (segment) |
| Q3 FY2027 communications and other | we expect revenue to decline in the low to mid-teens percentage range both sequentially and year-over-year, followed by a solid sequential recovery in the fourth quarter. | [Q2 FY2027 call] | not numeric (segment) |
| Q3 FY2027 non-GAAP tax rate | We expect a non-GAAP tax rate of 11%. | [Q2 FY2027 call] | not numeric (FY2027 rate; superseded by the FY2028 rate used as tax_rate.start) |
| Q3 FY2027 gross-margin driver | the forecasted acceleration of our custom business creating ... the sequential headwind in the fiscal third quarter | [Q2 FY2027 call] | not numeric (the machine transcript first garbles 'headwind' as 'headroom' and then corrects itself; the corrected phrase is quoted, as in outlook.md §4) |
| Q4 FY2027 gross margin | We currently expect to maintain gross margin in this range in the fourth fiscal quarter. | [Q2 FY2027 call] | not numeric |
| Q4 FY2027 non-GAAP operating margin | non-GAAP operating margin likely to enter our 38% to 40% long-term target range in Q4 of this fiscal year. | [Q2 FY2027 call] | not numeric (non-GAAP; converting to GAAP needs a stock-pay assumption management does not give) |
| FY2027 revenue | we now expect overall Marvell revenue in fiscal 2027 to grow approximately 45% year-over-year to roughly $12 billion, up from our prior outlook of approximately $11.5 billion just 1 quarter ago. | [Q2 FY2027 call] | revenue_growth year 1 (interpolation anchor) |
| FY2027 data center | which we now expect to grow by approximately 60% this fiscal year, up from our prior expectation of approximately 50%. | [Q2 FY2027 call] | not numeric (segment) |
| FY2027 communications and other | we currently expect fiscal 2027 growth to approach our 10% target. | [Q2 FY2027 call] | not numeric (segment) |
| FY2027 non-GAAP operating expenses | For fiscal 2027, we expect non-GAAP operating expenses of approximately $2.55 billion, slightly above our prior expectation of $2.45 billion | [Q2 FY2027 call] | not numeric (non-GAAP) |
| FY2027 capacity prepayments | We remain on pace to make approximately $1 billion of capacity prepayments to suppliers in fiscal 2027. | [Q2 FY2027 call] | not numeric (one component of reinvestment; no capex or working-capital guidance to complete net reinvestment) |
| FY2028 revenue | we now expect fiscal 2028 revenue of approximately $18 billion, up $1.5 billion from the $16.5 billion outlook we provided just 1 quarter ago. | [Q2 FY2027 call] | revenue_growth year 1 (interpolation anchor) and year 2 (nearest-year mapping) |
| FY2028 data center | we now expect Marvell's Data Center revenue to grow more than 60% year-over-year in fiscal 2028 | [Q2 FY2027 call] | not numeric (segment) |
| FY2028 custom | We remain confident that this business will more than double year-over-year in fiscal 2028 and accelerate significantly in fiscal 2029. | [Q2 FY2027 call] | not numeric (segment; the FY2029 phrase is qualitative) |
| FY2028 operating expenses | We currently expect non-GAAP operating expenses to grow at roughly half the rate of revenue growth in percentage terms. | [Q2 FY2027 call] | not numeric |
| FY2028 non-GAAP operating margin | to achieve the upper end of our target non-GAAP operating model of 38% to 40% as we progress through the year | [Q2 FY2027 call] | not numeric (non-GAAP; GAAP conversion needs stock pay, not guided) |
| FY2028 non-GAAP tax rate | we expect non-GAAP tax rate of approximately 13% in fiscal 2028. | [Q2 FY2027 call] | tax_rate start (all cases) |
| FY2028 gross margin | My preliminary view is gross margins next year are going to be in a similar range, same range as we're exiting this year. | [Q2 FY2027 call] | not numeric |
| Long-term model | we're going to reset that long-term target model here in the coming weeks at the Analyst Day. | [Q2 FY2027 call] | not numeric |
| Google warrant arithmetic (FY2029 and beyond) | you should assume starting in FY '29 and beyond whatever you've modeled previously prior to the warrant for custom numbers definitely goes higher | [Q2 FY2027 call] | not numeric |
| Scale-out switching FY2027 | Within scale-out switching, our business remains on track to more than double this year | [Q2 FY2027 call; Q2 FY2027 slides, p.18] | not numeric (segment; Q1 form was 'exceed $600 million, doubling from fiscal 2026', tracking to 'more than $1 billion in annualized revenue in fiscal 2028' [Q1 FY2027 call]) |
| Interconnect FY2027 (Q1 target, not restated in Q2) | we have increased our fiscal 27 revenue growth expectations for this business to more than 70% year over year | [Q1 FY2027 call; Q1 FY2027 slides, p.7] | not numeric (segment; scorecard.md grades it Partial) |
| Custom FY2027 (Q1 target, not restated in Q2) | Custom revenue remains on track to grow more than 20% year over year in fiscal 27 | [Q1 FY2027 call; Q1 FY2027 slides, p.14] | not numeric (segment) |
| Custom FY2029 target and market | We remain confident in achieving our target model for our custom business to deliver on over $10 billion in revenue in fiscal 29. | [Q1 FY2027 call] | not numeric (segment target; the '$55 billion TAM' behind it feeds diagnostics.final_year_market_size) |
| Scale-up optics FY2028 (Q1 figure, superseded) | scale up optics which you know, we are effectively calling at this point to be about $300 million | [Q1 FY2027 call] | not numeric (Q2: 'much larger than we thought just a quarter ago', no new figure) |
| Cloud capex planning assumption FY2028 (Q1, dropped in Q2) | we are planning for the rate of cloud CapEx growth to moderate into the 30%-plus range | [Q1 FY2027 call] | not numeric (informs the base-case fade) |
