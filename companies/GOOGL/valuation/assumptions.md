# GOOGL valuation assumptions as of 2026-Q2

This file is a read-only view of the valuation inputs for Alphabet Inc. (GOOGL), held in `assumptions.yaml`. Every number and every sentence below comes from that file; nothing is computed here. To change a number, use the app (`uv run --extra app valuation-app`), which saves into the YAML, records the change, and rewrites this file. A dash (—) marks a cell that is empty in the file: the analyst had nothing defensible to put there, or the item is not given. Rates are stored as decimals and shown here as percentages; money is in USD millions.

| Item | Value |
|---|---|
| Ticker | GOOGL |
| Company | Alphabet Inc. |
| As-of quarter | 2026-Q2 |
| As-of date (quarter cutoff) | 2026-07-23 |
| Drafted | 2026-09-07 |
| Horizon | 5 explicit years, then a terminal value |
| Currency and units | USD, millions |

## 1. The stories

Each story is copied word for word from `assumptions.yaml`.

### Bear (weight 25.0%)

People increasingly ask chat assistants instead of searching, and the ads next to those answers pay less, so Search growth slides into the low single digits within a few years. Alphabet keeps spending on the data centers it has already ordered, so capital spending still rises in 2027 as management promised, and the machines arrive and depreciate just as Cloud demand cools once customers have built their first AI systems; the heavy spending never earns its keep and is cut back only afterwards. Operating margins fall below the 2022–2023 lows, this time with far more machinery to pay for. At the end of the five years the moat is assumed gone and the business earns only its cost of capital.

### Base (weight 50.0%)

AI makes Search bigger rather than smaller, but growth slows from today's pace as it is measured against last year's strong growth and pays more for computing per answer. Cloud keeps converting its half-trillion-dollar backlog and the TPU hardware sales arrive in 2027, so revenue grows about 20% in the first year before easing toward single digits. Capital spending rises again in 2027 as management has promised and then eases back as depreciation catches up. Depreciation from the build-out eats a few points of margin, only partly offset by Cloud becoming as profitable as the older businesses. The habit, distribution and data advantages described in business.md §5 let Alphabet keep earning a modest premium over its cost of capital in the long run.

### Bull (weight 25.0%)

Alphabet turns out to own the whole AI stack, from its own chips to its own models to the products billions of people already use, and that lets it take a large share of both AI advertising and AI cloud computing. Search grows faster than before because AI answers create more questions and richer ads, Cloud approaches the profitability of the older businesses, and TPU systems become a real hardware business. Capital spending rises further in 2027 to meet the demand, and revenue more than doubles in five years while margins hold near today's level despite the heavier machinery. The moat is strong enough to earn a five-point premium over its cost of capital indefinitely.

### Management (not weighted; not computed)

Management gives no revenue, margin or profit targets. It has committed to a capital-spending range for 2026, says 2027 will be significantly higher, expects free cash flow to stay under pressure, and expects Search growth to slow when measured against last year's strong quarters. Everything else is qualitative, so this case records what was said and computes nothing.

Why this case is not computed: Management gives no revenue, margin or earnings targets for 2026 or later; the only numeric guidance is the 2026 capital-spending range, which is used as year-1 reinvestment. Everything else is qualitative and is marked 'not numeric' in the guidance table's 'used as' column below.

## 2. Scenario inputs

Rows are inputs and columns are cases. Per-year cells read year 1 / year 2 / ... in order. The reasons and sources behind each cell follow the table.

| Input | Bear | Base | Bull | Management |
|---|---|---|---|---|
| Weight | 25.0% | 50.0% | 25.0% | not weighted |
| Computable | always | always | always | no |
| Revenue growth, years 1-5 | 15.0% / 9.0% / 6.0% / 4.0% / 3.0% | 20.0% / 16.0% / 13.0% / 10.0% / 8.0% | 24.0% / 21.0% / 17.0% / 13.0% / 10.0% | — / — / — / — / — |
| Operating margin, years 1-5 | 31.0% / 28.0% / 26.0% / 24.0% / 23.0% | 33.0% / 32.0% / 31.0% / 30.0% / 30.0% | 34.0% / 35.0% / 35.0% / 35.0% / 35.0% | — / — / — / — / — |
| Sales-to-capital, years 1-5 | 0.60 | 0.90 | 1.30 | — |
| Sales-to-capital, years 6-10 of the 10-year reference | 0.90 | 1.20 | 1.60 | — |
| Reinvestment override, years 1-5 (USD millions) | 173,970 / 187,000 / — / — / — | 173,970 / 187,000 / — / — / — | 173,970 / 208,000 / — / — / — | 173,970 / — / — / — / — |
| Tax rate, explicit years | 16.8% | 16.8% | 16.8% | — |
| Tax rate, terminal year onwards | 25.0% | 25.0% | 25.0% | 25.0% |
| Cost of capital override | — | — | — | — |
| Terminal growth | the run's risk-free rate | the run's risk-free rate | the run's risk-free rate | — |
| Terminal growth may exceed the risk-free rate | no | no | no | no |
| Terminal return on capital: points above the cost of capital | 0.00% | 3.00% | 5.00% | — |
| A premium above 5 points is allowed | no | no | no | no |

### Bear: reasons

- **Revenue growth** — Year 1 still grows 15%, because the cloud orders already signed and the chip-system sales due in 2027 are largely locked in (outlook.md sections 3 and 4). Growth then drops below even the 2022–2023 lows: AI answers eat into searches, cloud demand cools once customers have built their first AI systems, and the cost of Alphabet's search defaults creeps up (business.md section 6, risks 1 and 5). [10-Q Q2 2026, Note 2] [Q2 2026 call, p.12–13] [10-K FY2025, Item 7] [10-K FY2023, Item 8]

    History as in the base case. Year 1 leans on the Cloud backlog of 513,900, just over half of it due within 24 months and largely contracted, plus TPU system sales landing in 2027 [10-Q Q2 2026, Note 2] [Q2 2026 call, p.12–13]. Search & other is assumed to slow sharply from 17%. Years 2–5 sit below the 2022–2023 troughs of 9.8% and 8.7% as the backlog is worked through, Cloud demand normalizes and the TAC rate rises [10-K FY2023, Item 8] [10-K FY2025, Item 7].
- **Operating margin** — Margins fall below the 2022 low, this time with far more machinery to pay for: depreciation on data centers already ordered keeps climbing while revenue barely grows, and energy, rented capacity and the price of search defaults all push the wrong way (outlook.md section 4; business.md sections 5 and 6). With growth of 3–9% a year there is no extra scale to offset any of it. [10-K FY2025, Item 8] [10-Q Q2 2026, Item 1] [Q2 2026 call, p.11] [Q2 2026 call, p.13–14] [10-K FY2023, Item 8]

    Starting point: trailing-twelve-month GAAP margin 33.1%, against FY2022–2023 margins of 26–27% earned with capex at only 10–11% of revenue (business.md section 3 table) [10-K FY2025, Item 8] [10-Q Q2 2026, Item 1] [10-K FY2023, Item 8]. On this case's capex path (200,000 in 2026 and about 239,000 of committed spending in 2027, cut back only afterwards; see the reinvestment override row) depreciation of property and equipment rises from 5.7% of trailing revenue to about 9% in year 2 and 16% by year 5, because revenue grows slowly: a headwind of roughly 10 points. The depreciation schedule assumes 60% servers over six years and 40% data centers and network over 20 years, management's 60/40 split [Q2 2026 call, p.11] [Q2 2026 call, p.13–14]. Acquired-intangible amortization is 0.2% of revenue and immaterial to the path.
- **Sales-to-capital** — 0.6 rising to 0.9 says each dollar of net new investment buys well under a dollar of new revenue: in this case the machines keep arriving and the revenue does not (business.md section 6, risk 2). Years 1–2 are set in dollars in the reinvestment override row, so this ratio drives years 3–5 only. [10-K FY2023, Item 8] [10-K FY2025, Item 8] [10-Q Q2 2026, Item 1]

    History as in the base case. What differs: the bear's 0.6 sits below even the latest same-year figure of 0.64, and 0.9 late assumes spending finally slows.
- **Reinvestment override** — Years 1 and 2 are set in dollars rather than by ratio, because the spending is already committed: management has guided 2026 capital spending and said 2027 will rise significantly. The bear keeps that spending, so the machines arrive and then under-earn, and cuts back only from year 3 (outlook.md section 4; business.md section 6). [Q2 2026 call, p.11] [Q2 2026 call, p.13] [10-K FY2025, Item 8] [10-Q Q2 2026, Item 1] [10-Q Q2 2026, Item 2] [10-Q Q2 2026, Note 9]

    Working as in the base case. What differs: the bear keeps the committed spending, behind which sit $811.0 billion of purchase commitments and $85.2 billion of signed-but-not-started leases, so the machines arrive and then under-earn [10-Q Q2 2026, Item 2] [10-Q Q2 2026, Note 9]. Years 3–5 fall back to sales-to-capital, which implies gross capex cut to roughly 120–130B a year as demand disappoints; that cut is a scenario assumption, not guidance. Acquisitions and working capital are ignored.
- **Tax rate** — Starts at the FY2025 effective rate of 16.8% and moves to the 25% marginal rate by the terminal year, as the model requires. Two forces point the rate up over time: the OECD agreement that sets a 15% floor on the tax a big company pays in each country, and the shrinking US deduction for income earned from serving customers abroad [10-K FY2025, Item 7].
- **Terminal growth** — Equal to the fetched 10-year Treasury rate, as the method requires.
- **Terminal return on capital premium** — Zero by rule: in the bear case the moat is gone and the business earns only its cost of capital after year 5.

### Base: reasons

- **Revenue growth** — Year 1 grows 20%: Cloud converts a backlog worth more than a year of company-wide revenue, the chip-system sales arrive in 2027, and Search keeps growing but slower than its recent burst (outlook.md sections 2 and 4). Growth then fades year by year toward the single digits of 2022–2023 as the backlog is worked off and Search matures. The scorecard shows management delivering on its capex and Cloud claims, so the backlog is taken at face value. [10-Q Q2 2026, Note 2] [Q2 2026 call, p.12–13] [10-K FY2025, Item 7] [10-K FY2023, Item 8]

    History (business.md section 2 table; outlook.md section 1): 9.8% (2022), 8.7% (2023), 13.9% (2024), 15.1% (2025) and 23.1% in the first half of 2026, the last with a one-point currency tailwind [10-K FY2023, Item 8] [10-K FY2025, Item 7]. Year 1 (July 2026–June 2027) at 20%: the Cloud backlog of 513,900 with just over half due within 24 months means Cloud alone should add over 50,000 a year against trailing-twelve-month Cloud revenue of 77,617; TPU system sales land mostly in 2027; Search & other slows from 17% as it laps a strong 2025 and faces a slight currency headwind [10-Q Q2 2026, Note 2] [Q2 2026 call, p.12–13]. Management met or beat its capex and Cloud claims last quarter (scorecard.md, Q2 2026).
- **Operating margin** — Margins slip about three points over five years and then hold: the depreciation management has guided for is the big headwind (outlook.md section 4), and cost discipline, a falling traffic-acquisition rate and Cloud becoming as profitable as the older businesses roughly cover it (business.md section 3; outlook.md section 1). The three points of slippage are the room left for energy, rented capacity and the low-margin chip-system sales described in outlook.md section 3. [10-K FY2025, Item 8] [10-Q Q2 2026, Item 1] [10-Q Q2 2026, Item 2] [Q2 2026 call, p.11] [Q2 2026 call, p.13–14] [Q2 2026 slides, p.9] [10-K FY2025, Note 15]

    Starting point: trailing-twelve-month GAAP margin 33.1%, first half of 2026 35.0%, FY2021–2025 31%, 26%, 27%, 32%, 32% (business.md section 3 table) [10-K FY2025, Item 8] [10-Q Q2 2026, Item 1] [10-Q Q2 2026, Item 2]. Management says the build-out 'will continue to put pressure on the P&L in the form of higher depreciation expense and related data center operations costs, such as energy' (outlook.md section 4) [Q2 2026 call, p.13–14].
    Headwind: depreciation of property and equipment was 25,237 trailing, 5.7% of revenue; 200,000 of capex adds about 24–28B a year of depreciation once in service (60% servers over six years = 20B, 40% data centers and network over about 20 years = 4B, using management's 60/40 split). On this case's capex path (200,000 in 2026, about 239,000 in 2027, then falling back; see the reinvestment override row) depreciation is about 8% of revenue in year 2, 11% in year 3, 12% in year 4 and 13% in year 5, roughly 6–7 points of headwind by year 5 before energy and operations costs [Q2 2026 call, p.11].
    Offsets: operating expenses were 27.8% of trailing revenue (R&D 15.5%, S&M 7.0%, G&A 5.3%), and growing them about 10% a year against 13% revenue growth frees about 4 points; TAC at 19.8% of ad revenue drifting down a point is worth about 0.7; Cloud (35.6% margin in Q2 2026, up from 23.7% in FY2025) growing from 17% toward 30% of revenue adds 1–2 points; about 6–7 points in all [Q2 2026 slides, p.9] [10-K FY2025, Note 15].
    Net: about zero to minus 1 point before energy, third-party capacity and low-margin TPU hardware sales, so the path gives up 3 points to leave room for those. Acquired-intangible amortization, about 1,300 a year at its 2027 peak, is 0.2% of revenue and does not move the path.
- **Sales-to-capital** — 0.9 rising to 1.2 sits between what Alphabet has managed in the last year and its longer record, reflecting that AI capacity costs more per dollar of revenue than the old search machines did (business.md section 3). Years 1–2 are set in dollars in the reinvestment override row, so this ratio drives years 3–5 only. [10-K FY2023, Item 8] [10-K FY2025, Item 8] [10-Q Q2 2026, Item 1]

    Historical sales-to-capital, revenue change / (capex minus depreciation of property and equipment), same year: 2022 1.40 (25,199 / 18,010), 2023 1.21 (24,558 / 20,305), 2024 1.15 (42,624 / 37,224), 2025 0.75 (52,818 / 70,311), first half of 2026 0.64 (43,030 / 67,012) [10-K FY2023, Item 8] [10-K FY2025, Item 8] [10-Q Q2 2026, Item 1]. 2021 cannot be computed: FY2020 revenue is not in the cached filings.
    With the engine's one-year lag, where a year's spending buys the next year's growth: 2021 into 22 gives 1.75, 2022 into 23 gives 1.36, 2023 into 24 gives 2.10, 2024 into 25 gives 1.42, and 2025 into H1 2026 gives roughly 1.2 annualized.
    Base: 0.9 early, between the latest same-year figure and the lagged history, and 1.2 late as depreciation catches up with spending.
- **Reinvestment override** — Years 1 and 2 are set in dollars rather than by ratio, because management has guided 2026 capital spending and said 2027 will rise significantly (outlook.md section 4). From year 3 the model falls back to the sales-to-capital ratio, letting spending ease as depreciation catches up; nothing in the sources speaks to capex beyond 2027, so that fall-back is the input most worth the owner's attention. [Q2 2026 call, p.11] [Q2 2026 call, p.13] [10-K FY2025, Item 8] [10-Q Q2 2026, Item 1] [10-Q Q2 2026, Note 9]

    Year 1: the 2026 capex guidance midpoint of $195–205 billion = 200,000, less trailing depreciation of property and equipment 25,237 and intangible amortization 793 (26,030 together) = 173,970 of net reinvestment; calendar 2026 is mapped to model year 1 (July 2026–June 2027), an approximation [Q2 2026 call, p.11] [10-K FY2025, Item 8] [10-Q Q2 2026, Item 1] [10-Q Q2 2026, Note 9]. Netting trailing depreciation against a year whose depreciation will run about 35–40B overstates net reinvestment by roughly 10B, while the model year will carry more than calendar 2026's 200B given the 80.6B spent in the first half and a rising 2027; the two roughly offset and the result is accepted as conservative.
    Year 2 (2027) is anchored on the only sourced figure behind 'increase significantly in 2027': the second-half 2026 run-rate implied by the guidance midpoint, 200,000 minus 80,598 spent in the first half = 119,402 per half-year, about 239,000 a year, less about 52,000 of 2027 depreciation = about 187,000 net, our inference from guidance [Q2 2026 call, p.13]. The 2027 depreciation figure uses a schedule of 60% servers over six years and 40% data centers and network over 20 years, a one-year lag to in-service, applied to 2021–2026 capex; the 60/40 split is management's.
    Years 3–5 fall back to sales-to-capital, which implies gross capex of roughly 155–185B a year (net 70–78B plus depreciation of 78–110B), so spending falls back from the 2027 peak as depreciation catches up. Acquisitions and working capital are ignored.
- **Tax rate** — Starts at the FY2025 effective rate of 16.8% and moves to the 25% marginal rate by the terminal year, as the model requires. Two forces point the rate up over time: the OECD agreement that sets a 15% floor on the tax a big company pays in each country, and the shrinking US deduction for income earned from serving customers abroad [10-K FY2025, Item 7].
- **Terminal growth** — Equal to the fetched 10-year Treasury rate, as the method requires.
- **Terminal return on capital premium** — Three points over the terminal cost of capital, from business.md section 5: the search habit; the distribution Alphabet buys with traffic acquisition costs, the money it pays phone and browser makers to be their default search engine; the search data that courts treat as the hard-to-copy asset; YouTube's two-sided creator-and-viewer network; and Cloud switching costs from multi-year contracts. Below Damodaran's own four points for Alphabet in 2018, because the owner prefers to err low.

### Bull: reasons

- **Revenue growth** — Growth holds roughly the 23–24% pace of the first half of 2026 for a year and then fades more slowly than in the base case, on the view that AI answers create more questions and richer ads while Cloud and the chip-system business compound (outlook.md sections 2 and 3). Even year 5 at 10% is below what Alphabet did in 2024 and 2025, but the case only works if Search keeps growing in the mid-teens. [10-Q Q2 2026, Note 2] [Q2 2026 call, p.3–4] [Q2 2026 call, p.12] [Q2 2026 release, p.1]

    History as in the base case. What supports the faster path: the Cloud backlog grew by more than 50,000 in one quarter to 513,900 and customers use more than they commit (outlook.md section 3); AI Mode passed one billion monthly users and the Gemini app 950 million (outlook.md section 2); TPU sales become a new revenue line [10-Q Q2 2026, Note 2] [Q2 2026 call, p.3–4] [Q2 2026 call, p.12] [Q2 2026 release, p.1]. Search & other grew in the mid-teens in the first half of 2026, which is what the case leans on (outlook.md section 1).
- **Operating margin** — Margins hold near the level Alphabet reached in the first half of 2026 rather than rising: faster growth spreads the research and sales bills further and Cloud approaches the profitability of the older businesses, but that only covers the extra depreciation from a bigger build-out (business.md sections 3 and 4; outlook.md section 1). [10-Q Q2 2026, Item 1] [10-Q Q2 2026, Item 2] [Q2 2026 slides, p.9] [Q2 2026 call, p.11–12] [10-Q Q1 2026, Item 1] [10-K FY2025, Item 8] [10-K FY2025, Note 15]

    Starting point: Q2 2026 margin 34.0%, which carried a 1.3-point legal charge, and first-half-2026 35.0% [10-Q Q2 2026, Item 1] [10-Q Q2 2026, Item 2] [Q2 2026 slides, p.9]. On this case's capex path (200,000 in 2026, about 260,000 in 2027, then falling back; see the reinvestment override row) depreciation of property and equipment runs about 8% of revenue in year 2 and 10–12% by year 5 against 5.7% trailing, a headwind of 4–6 points plus energy and operations costs [Q2 2026 call, p.11–12].
    Offsets: operating expenses were 27.8% of trailing revenue (R&D 15.5%, S&M 7.0%, G&A 5.3%), and growing them 12–13% a year against 17% revenue growth frees 4–5 points; Cloud (35.6% margin in Q2 2026 against 20.7% a year earlier, approaching Google Services' 41–45%) growing toward 30% of revenue adds 1–2 points; TAC drifting down adds about 0.7; 6–8 points in all [10-K FY2025, Item 8] [10-K FY2025, Note 15].
    Why the path does not rise: Q1 2026's 36.1% was earned with depreciation at 5.9% of revenue, before the wave [10-Q Q1 2026, Item 1]. Acquired-intangible amortization is 0.2% of revenue and immaterial.
- **Sales-to-capital** — 1.3 rising to 1.6 assumes the older pattern returns, in which a year's spending shows up as revenue the year after (business.md section 3). Years 1–2 are set in dollars in the reinvestment override row, so this ratio drives years 3–5 only. [10-K FY2023, Item 8] [10-K FY2025, Item 8] [10-Q Q2 2026, Item 1]

    History as in the base case. What differs: 1.3 assumes the payoff pattern of the lagged series resumes, and 1.6 late is still under that lagged series' average of 1.66.
- **Reinvestment override** — Year 1 is the guided 2026 capital spending and year 2 is a bigger 2027 than in the base case, because demand is stronger; both are set in dollars rather than by ratio (outlook.md section 4). From year 3 the model falls back to the sales-to-capital ratio, and nothing in the sources speaks to capex that far out, so that fall-back is a scenario assumption. [Q2 2026 call, p.11] [Q2 2026 call, p.13] [10-K FY2025, Item 8] [10-Q Q2 2026, Item 1] [10-Q Q2 2026, Note 9]

    Working as in the base case. What differs: year 2 spends about 260,000 of gross capex rather than about 239,000, the same sourced second-half-2026 run-rate (200,000 minus 80,598 = 119,402 per half-year) plus about 9% to match stronger demand, less about 52,000 of 2027 depreciation on the base case's schedule = about 208,000 net, our inference [Q2 2026 call, p.11] [Q2 2026 call, p.13] [10-K FY2025, Item 8] [10-Q Q2 2026, Item 1] [10-Q Q2 2026, Note 9]. Years 3–5 fall back to sales-to-capital, which implies gross capex of roughly 160–190B a year (net 68–78B plus depreciation of 81–113B). Acquisitions and working capital are ignored.
- **Tax rate** — Starts at the FY2025 effective rate of 16.8% and moves to the 25% marginal rate by the terminal year, as the model requires. Two forces point the rate up over time: the OECD agreement that sets a 15% floor on the tax a big company pays in each country, and the shrinking US deduction for income earned from serving customers abroad [10-K FY2025, Item 7].
- **Terminal growth** — Equal to the fetched 10-year Treasury rate, as the method requires.
- **Terminal return on capital premium** — Five points, the ceiling without an override: the full-stack position (own chips, own models, own distribution) that business.md section 5 describes for Cloud, together with the Search moat, is assumed to persist. Damodaran used four points for Alphabet in 2018.

### Management: reasons

- **Computable: no** — Management gives no revenue, margin or earnings targets for 2026 or later; the only numeric guidance is the 2026 capital-spending range, which is used as year-1 reinvestment. Everything else is qualitative and is marked 'not numeric' in the guidance table's 'used as' column below.
- **Revenue growth** — No revenue guidance for any period. [Q2 2026 call, p.13–14]
- **Operating margin** — No margin guidance; only the qualitative depreciation and Cloud-margin comments above. [Q2 2026 call, p.13–14]
- **Sales-to-capital** — Not derivable from guidance.
- **Reinvestment override** — The one number management has given is the 2026 capital-spending range, so year 1 is that midpoint less the depreciation and amortization it replaces, and the later years are left empty. The 2027 remark about spending increasing significantly is not turned into a number here; the bear, base and bull each carry a labelled inference for 2027 instead.

    Year 1: the 2026 capex guidance midpoint 200,000 minus trailing-twelve-month depreciation of property and equipment 25,237 and intangible amortization 793 = 173,970 of net reinvestment [Q2 2026 call, p.13] [10-K FY2025, Item 8] [10-Q Q2 2026, Item 1] [10-Q Q2 2026, Note 9]. Calendar 2026 is mapped to model year 1 (July 2026–June 2027), an approximation.
- **Tax rate** — No tax guidance.
- **Terminal growth** — Not guided.
- **Terminal return on capital premium** — Not guided.

## 3. Base year (the twelve months ending June 30, 2026 (Q3 2025 to Q2 2026))

| Item | USD millions | Reason | Source |
|---|---|---|---|
| Revenue, trailing twelve months | 445,866 | The base year is the twelve months to June 30, 2026, so the model starts from what Alphabet has just earned rather than from a calendar year (business.md section 2). It is the 2025 annual figure with the newest half-year swapped in for the year-earlier half-year. | [10-K FY2025, Item 8] [10-Q Q2 2026, Item 1] |
| Operating income, GAAP | 147,628 | Operating profit for the same twelve months, exactly as reported, which works out at 33.1% of revenue (business.md section 3). The legal charges in the one-time items list below are deliberately left inside it, because charges like them arrive most years. | [10-K FY2025, Item 8] [10-Q Q2 2026, Item 1] |
| One-time item: EC advertising-technology fine, Q3 2025 (recorded, not added back) | 0 | A $3.5 billion fine from the September 2025 European Commission ad-technology decision sits inside the base year's costs and is left there. Brussels has fined Alphabet at intervals since 2017, so the method treats these fines as a recurring cost of running this business rather than a one-off (business.md section 6). | [10-K FY2025, Item 7] [10-Q Q2 2026, Note 10] |
| One-time item: PriceRunner damages award, Q2 2026 (recorded, not added back) | 0 | A Stockholm court ordered Alphabet to pay PriceRunner damages, and the $1.5 billion of principal was charged to Google Services costs in Q2 2026; it is left in the base year. Legal accruals like this recur at Alphabet and the award is under appeal, so it is not treated as one-off (business.md section 6). | [10-Q Q2 2026, Item 2] [10-Q Q2 2026, Note 10] |
| One-time item: Waymo valuation-based compensation charge, Q4 2025 (recorded, not added back) | 0 | A $2.1 billion employee compensation charge for Waymo, based on estimated stock valuation and mostly in R&D, was recognized in Q4 2025. Not added back because it is stock-based pay, which always stays as a cost by rule. | [10-K FY2025, Item 7] |
| One-time item: Office space impairment, Q1 2026 (recorded, not added back) | 0 | $300 million of office space impairment charges in Q1 2026 sales and marketing expense. Not added back: office-exit charges recurred in 2023 ($1.8 billion, business.md section 3) and again here, and the amount is 0.07% of TTM revenue. | [10-Q Q1 2026, Item 2] |
| Amortization of acquired intangibles (memo) | 793 | This is the yearly write-down of technology and customer lists bought in acquisitions. It stays as a cost by rule and is recorded here only as a memo; at 0.2–0.3% of revenue it is far too small to bend the margin paths, whether it runs off or not. | [10-Q Q2 2026, Note 9] |
| Stock-based compensation (memo) | 28,147 | Pay handed out as shares, 6.3% of revenue in the base year. The method keeps it inside operating profit, because it is a real cost to existing owners; this cell is only a memo (business.md section 4). | [10-K FY2025, Item 8] [10-Q Q2 2026, Item 1] |
| Research and development expense (memo) | 68,974 | What Alphabet spent on research and development in the base year, 15.5% of revenue. Memo row only: the switch that would treat research as an investment rather than a cost is off, as the method requires. | [10-K FY2025, Item 8] [10-Q Q2 2026, Item 1] |
| Effective tax rate | 16.8% | The model starts from Alphabet's FY2025 tax rate of 16.8%, the cleanest recent measure of tax on ordinary profits (business.md section 4). Rates computed from the newest quarters look higher only because enormous paper gains on investment stakes carry tax at the full statutory rate, and those gains have nothing to do with the operating business. | [10-K FY2025, Item 7] [10-Q Q2 2026, Note 14] |
| Invested capital | 516,207 | The capital the business has been handed: what shareholders and lenders put in, less the cash it is sitting on. It is used only for the return-on-capital check, and it understates that return, because it still contains large investment stakes that are not operating assets (business.md section 4). | [10-Q Q2 2026, Item 1] [10-Q Q2 2026, Note 4] [10-Q Q2 2026, Note 6] |

- **Revenue**, working notes:

    Trailing twelve months = FY2025 revenue 402,836 + six months to June 30, 2026 of 229,692 minus six months to June 30, 2025 of 186,662 = 445,866. All three figures come from the consolidated statements of income [10-K FY2025, Item 8] [10-Q Q2 2026, Item 1].

- **Operating income gaap**, working notes:

    Income from operations, trailing twelve months = FY2025 129,039 + 6M 2026 80,466 minus 6M 2025 61,877 = 147,628 [10-K FY2025, Item 8] [10-Q Q2 2026, Item 1]. 147,628 / 445,866 = 33.1% (computed).

- **Amortization of acquired intangibles**, working notes:

    Trailing twelve months = 545 for the six months to June 30, 2026 (Wiz and Intersect closed in March 2026) + 248 for the second half of 2025 = 793 [10-Q Q2 2026, Note 9]. The second half of 2025 is not disclosed in the cached filings (the FY2025 10-K carries no intangible-assets table and the Q3 2025 10-Q is not cached), so it is taken at the Q2 2025 quarterly run-rate of 124 times 2 = 248; our inference. Disclosed expected amortization: 747 for the rest of 2026, 1,304 in 2027, then 1,142, 1,096 and 1,055, i.e. about 0.2–0.3% of revenue. Memo row; stays deducted.

- **Stock based compensation**, working notes:

    Cash-flow statement SBC expense, trailing twelve months = FY2025 24,953 + 6M 2026 14,708 minus 6M 2025 11,514 = 28,147 [10-K FY2025, Item 8] [10-Q Q2 2026, Item 1]. 28,147 / 445,866 = 6.3% of revenue (computed). Memo row; never added back.

- **Rnd expense**, working notes:

    Research and development, trailing twelve months = FY2025 61,087 + 6M 2026 35,251 minus 6M 2025 27,364 = 68,974 [10-K FY2025, Item 8] [10-Q Q2 2026, Item 1]. 68,974 / 445,866 = 15.5% of revenue (computed). Used only if the research-capitalisation switch is turned on.

- **Effective tax rate**, working notes:

    FY2025: provision 26,656 on pre-tax income 158,826 = 16.8%, a rate that already includes a non-deductible EC fine [10-K FY2025, Item 7]. Alternatives considered: the trailing-twelve-month rate on the same basis is 18.4% (55,064 / 299,269), and the Q2 and six-month 2026 rates were 19.1%; all of them are pushed up by $99.0 billion of unrealized equity gains carrying deferred tax at the statutory rate [10-Q Q2 2026, Note 14].

- **Invested capital**, working notes:

    At June 30, 2026: total stockholders' equity 640,480 + debt 100,164 (long-term 98,165 plus current portion 1,999) + operating lease liabilities 18,037 minus cash, cash equivalents and marketable securities 242,474 = 516,207 [10-Q Q2 2026, Item 1] [10-Q Q2 2026, Note 4] [10-Q Q2 2026, Note 6]. Excluding the 131,461 of non-marketable securities and the 14,126 of restricted SpaceX shares held in other non-current assets gives 370,620 and a correspondingly higher ROIC.

### Switches

These stay off unless the owner turns them on for a specific company.

| Switch | Setting |
|---|---|
| Add back amortization of acquired intangibles | no |
| Treat research spending as an investment | no |
| Years over which research spending is written off | 5 |
| Research spending history, oldest first (USD millions) | — |
| Reinvestment lag | 1 year |

## 4. Bridge from operating assets to equity

| Item | USD millions | Reason | Source |
|---|---|---|---|
| Cash and marketable securities (added) | 162,474 | The cash and investments Alphabet could turn into money at short notice, which the model adds to the value of the business. The SpaceX shares inside the balance-sheet total are excluded here because they cannot be sold yet; they are listed separately below. | [10-Q Q2 2026, Item 1] [10-Q Q2 2026, Note 3] |
| Non-operating asset (added): SpaceX shares under short-term sale restrictions (inside marketable securities) | 80,000 | Shares in SpaceX that Alphabet holds inside its marketable securities at fair value, meaning the price they would fetch if sold today. They are kept out of the cash line because they cannot be sold yet, so they are added to the value of the business separately. | [10-Q Q2 2026, Note 3] |
| Non-operating asset (added): Marketable equity securities in other non-current assets (includes $14.1B SpaceX shares restricted through Q3 2027) | 14,126 | A second block of SpaceX shares, held among other non-current assets, the accounting label for assets not expected to turn into cash within a year. It is carried at fair value, the price it would fetch today, and it sits outside the balance-sheet cash total, so it is added separately. | [10-Q Q2 2026, Note 3] |
| Non-operating asset (added): Non-marketable securities (private companies, including the unnamed private company; equity-method stakes) | 131,461 | Stakes in private companies, added to value separately because they are not part of the advertising and cloud business (business.md section 7). The figure is what the last funding rounds implied rather than a market price, so the owner may want to mark it down. | [10-Q Q2 2026, Item 1] [10-Q Q2 2026, Note 3] |
| Debt (subtracted) | 100,164 | Every dollar of borrowing on the balance sheet, at the value the accounts carry it at, subtracted from the value of the business. No commercial paper is outstanding (business.md section 4). | [10-Q Q2 2026, Note 6] [10-Q Q2 2026, Item 1] |
| Operating lease liabilities (subtracted) | 18,037 | Rent Alphabet has already committed to on buildings and data centers it leases, treated as debt-like and subtracted from value. Data-center leases that are signed but have not started are not liabilities yet and belong to the reinvestment story instead. | [10-Q Q2 2026, Note 4] |
| Minority interests (subtracted) | 7,100 | The book value of the slices of subsidiaries such as Waymo that outside investors own, subtracted because that share of the profits is not Alphabet's. Accountants call them noncontrolling interests, meaning stakes too small to control the subsidiary; 824 of the total is redeemable, meaning those holders can require Alphabet to buy them out. | [10-Q Q2 2026, Note 7] |
| Other claim (subtracted): 6.25% mandatory convertible preferred stock (liquidation preference) | 19,250 | In June 2026 Alphabet sold preferred shares that get paid before ordinary shareholders and turn into ordinary shares in May 2029. They are subtracted here at the amount their holders are owed first, which is simpler and slightly more conservative than adding the future shares to the share count. | [10-Q Q2 2026, Note 11] [8-K 2026-06-05 (preferred)] |
| Other claim (subtracted): Finance lease liabilities | 2,590 | Equipment and space Alphabet has effectively bought on credit through leases. Debt-like, and not counted in the debt or operating-lease lines above, so it is subtracted here. | [10-Q Q2 2026, Note 4] |
| Other claim (subtracted): Accrued legal and regulatory fines and settlements | 17,356 | Fines already charged against past operating profit but not yet paid, 'primarily' EC fines; $5.2 billion of it (the Android fine plus interest) was paid in July 2026. Cash that will leave without buying anything, so it is treated like debt. Future fines are inside the forecast margins, because the one-time items listed in the base year are left inside operating profit. | [10-Q Q2 2026, Note 7] [10-Q Q2 2026, Item 2] |
| Other claim (subtracted): Data-center backstop credit derivatives, at fair value | 815 | Alphabet has promised to cover other companies' data-center payments if they default, and the liability it records for those promises is subtracted here. The worst case is far bigger than the recorded number, which is why the line is worth the owner's attention (business.md section 6). | [10-Q Q2 2026, Note 3] [10-Q Q2 2026, Note 10] |
| Probability of failure | 0.0% | Zero: Alphabet holds far more spendable cash and securities than debt, earns a large operating profit every quarter, and has just shown it can raise money at will. Failure inside the five-year window is not a realistic case (business.md section 4). | — |
| What the assets would fetch in a failure | 0 | Not needed with probability of failure at zero. | — |
| Diluted shares (millions) | 12309.0 | The share count the per-share value is divided by: the latest quarter's average share count as the accountants compute it, including shares owed on employee awards and the new preferred. Shares sold in June 2026 count only for the part of the quarter they existed, which is why the period-end count is a little higher. | [10-Q Q2 2026, Note 12] |

- **Cash and marketable securities**, working notes:

    Balance-sheet cash, cash equivalents and marketable securities of 242,474 less the 80,000 of SpaceX shares that carry short-term sale restrictions (Note 3, footnote 1) = 162,474 [10-Q Q2 2026, Item 1] [10-Q Q2 2026, Note 3]. What remains is 55,911 of cash and equivalents plus 106,563 of other marketable securities: 99,500 of government bonds, corporate debt and mortgage-backed securities, and 7,063 of other marketable equity, all sellable at short notice.

- **Debt**, working notes:

    Long-term debt 98,165 plus the 1,999 current portion of long-term notes held in accrued expenses = 100,164 [10-Q Q2 2026, Note 6] [10-Q Q2 2026, Item 1]. Face value is 101,085; the 921 difference is unamortized discount and issuance costs, and the notes' estimated fair value was 94,900. The total includes 1,686 of other long-term debt; the 10-Q does not say whether the 1,300 drawn on credit facilities is part of it.

- **Operating lease liabilities**, working notes:

    Current 3,446 (in accrued expenses) + non-current 14,591 = 18,037 [10-Q Q2 2026, Note 4]. The excluded signed-but-not-commenced leases carry 85,200 of future payments.

- **Minority interests**, working notes:

    Total noncontrolling interests in consolidated subsidiaries were $7.1 billion at June 30, 2026, including 824 redeemable [10-Q Q2 2026, Note 7]. The 10-Q states the total in billions, so 7,100 is rounded.

- **Probability of failure**, working notes:

    162,474 of unrestricted cash and securities against 100,164 of debt and 147,628 of trailing-twelve-month operating income; $56 billion of notes and $49.6 billion of equity were raised in the first half of 2026 alone.

- **Diluted shares**, working notes:

    Q2 2026 diluted weighted-average shares, consolidated: 12,309 million = 12,151 basic + 142 RSUs and other contingently issuable shares + 16 from the preferred under the if-converted method [10-Q Q2 2026, Note 12]. Period-end common shares outstanding were 12,230 million. The June sales were roughly 87 million shares: the 10-Q rounds them to 29 + 29 + 14 + 14 million, and the 8-K's 25.46 million per class plus the fully exercised 3.82 million over-allotment option per class and 28.57 million private-placement shares total 87.1 million [8-K 2026-06-04].

Dilution note: A $40.0 billion at-the-market program was set up in June 2026 and was unused at June 30; the CFO said it will run 'for some period of time' to cover tax on stock-based pay [Q2 2026 call, p.18] [10-Q Q2 2026, Item 2]. The preferred converts into about 43–54 million common shares in May 2029, partly offset by capped calls [10-Q Q2 2026, Note 11]. Buybacks that used to absorb employee stock issuance were zero in the first half of 2026 [10-Q Q2 2026, Note 11].

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
| Damodaran industry | Advertising | Advertising is the industry group used for the risk measure, because ads are just over 70% of revenue and their economics drive the profit (business.md section 2). Cloud is the fast-growing minority with different economics, so the owner may want the planner to test a software group as well. | — |
| Unlevered beta | 1.008 | Damodaran's advertising-industry beta of about 1.0 means Alphabet's operating profits are assumed to swing roughly in line with the market's, which is what sets the cost of capital. Treating Alphabet as an internet-software company instead would raise that cost by about two and a half points, a test the owner can run. | [Damodaran betas.xls, Advertising, dataset dated 2026-01-05, cached tools/valuation/data/damodaran/betas.csv] |
| Debt to equity (market values) | 0.0284 | Borrowing is under 3% of what the market says Alphabet's shares are worth, even after the 2025–2026 bond sales, so debt barely moves the cost of capital (business.md section 4). This ratio is what levers the industry beta up. | [10-Q Q2 2026, Note 6] [10-Q Q2 2026, Note 4] [10-Q Q2 2026, Note 12] [Yahoo price 338.46 on 2026-09-04] |
| Pre-tax cost of debt | 4.80% | 4.8% is what long-dated dollar borrowing costs Alphabet today, taken from the coupon on its most recent large dollar bond sale. Dollar coupons are used because the model discounts dollar cash flows. | [10-Q Q2 2026, Note 6] [10-K FY2025, Item 7] |
| Terminal cost of capital method | mature | Default: after the forecast Alphabet is priced like a mature company, cost of capital = risk-free rate + the 4.5% mature-market premium. | — |

- **Damodaran industry**, working notes:

    Advertising was 70.7% of trailing-twelve-month revenue: 315,348 of 445,866, being Search & other, YouTube ads and Network [10-K FY2025, Item 7] [10-Q Q2 2026, Note 2]. Google Cloud is 17.4% of revenue and growing about 80% a year, with economics closer to 'Software (System & Application)' or 'Computer Services'. 'Software (Internet)' is a reasonable whole-company alternative and the planner may compare both betas.

- **Unlevered beta**, working notes:

    1.0080 is the cash-corrected unlevered beta of Damodaran's 52-company US advertising group [Damodaran betas.xls, Advertising, dataset dated 2026-01-05, cached tools/valuation/data/damodaran/betas.csv]. The whole-company alternative 'Software (Internet)' is 1.591, worth about 2.4 points on the cost of capital, and the owner can test this in the app.

- **Debt to equity market**, working notes:

    Debt 100,164 plus operating lease liabilities 18,037 = 118,201 (120,791 if finance leases are added), divided by market capitalisation of 4,166,104 (338.46 times 12,309 million diluted shares) = 0.0284 [10-Q Q2 2026, Note 6] [10-Q Q2 2026, Note 4] [10-Q Q2 2026, Note 12] [Yahoo price 338.46 on 2026-09-04].

- **Pretax cost of debt**, working notes:

    The $20.0 billion of US-dollar notes issued in Q1 2026 carry a weighted-average coupon of 4.80% with a 15-year average maturity [10-Q Q2 2026, Note 6]. For comparison: the 2025 US-dollar notes were issued at 4.89% and 4.92%, and effective interest rates on the 2025–2026 dollar notes run 3.93%–5.84% [10-K FY2025, Item 7]. The euro, sterling, franc, Canadian-dollar and yen notes carry local-currency coupons of 1.06%–5.31% and are not comparable.

## 7. Inputs for the diagnostics

| Item | Value | Reason | Source |
|---|---|---|---|
| Market size in the final forecast year (USD millions) | — | Left empty: no cached filing, release, slide or transcript puts a dollar size on global digital advertising or cloud spending, and the method forbids inventing one. Management said only that the AI shift 'is an expansion of our total addressable market'. | [Q2 2026 call, p.22] |
| Company's own five-year revenue growth per year | 11.8% | Alphabet's own revenue grew about 11.8% a year over the five fiscal years 2021–2025, which is the yardstick the scenario growth paths should be judged against (business.md section 2). | [10-K FY2023, Note 2] [10-K FY2025, Item 7] |
| Company's own five-year average operating margin | 29.6% | Alphabet averaged a 29.6% operating margin over the same five fiscal years, so the base case's 30–33% assumes it holds a little above its own recent average (business.md section 3). | [10-K FY2023, Item 7] [10-K FY2023, Item 8] [10-K FY2025, Item 7] [10-K FY2025, Item 8] |

## 8. Management guidance on record

Everything management has said in numbers or in words, whether or not it was used.

| Item | Quote | Source | Used as |
|---|---|---|---|
| Capex 2026 | we are updating our full year 2026 CapEx guidance range to $195‑205 billion, up from our previous estimate of $180‑190 billion. | [Q2 2026 call, p.13] | reinvestment year 1 (midpoint 200,000 minus TTM depreciation and amortization of 26,030 = 173,970) |
| Capex 2027 | we continue to expect our CapEx to increase significantly in 2027, and we'll provide more details at a later date. | [Q2 2026 call, p.13] | not numeric |
| Backlog | we expect to recognize just over 50% of the total backlog as revenue over the next 24 months. | [Q2 2026 call, p.12] | not numeric (informs analyst revenue growth in years 1–2) |
| TPU revenue timing | We continue to expect to recognize a relatively small portion of the revenues ... this year, ramping as we exit 2026. We anticipate the vast majority of the revenues from these agreements will be realized in 2027. | [Q2 2026 call, p.13] | not numeric |
| Third-party capacity and Cloud margin | we plan to expand the use of third‑party capacity in Q3 as a bridging strategy while we build out more internal capacity. ... it will create modest margin pressure in the near‑term as we utilize this capacity. | [Q2 2026 call, p.13] | not numeric |
| Search comparison | in Q3, we will begin lapping an acceleration in Search performance that began in the third quarter last year. | [Q2 2026 call, p.13] | not numeric |
| FX | we would expect a slight FX headwind to our consolidated revenue in Q3, compared to a one percentage point FX tailwind in Q2. | [Q2 2026 call, p.13] | not numeric |
| Free cash flow | we expect the free cash flow will remain under pressure driven by our investments in technical infrastructure | [Q2 2026 call, p.14] | not numeric |
| Equity markets and ATM program | At this point, we're not planning to go back to the equity markets, with the exception of ... the ATM, or at‑the‑market, offering that we will do to address ... the tax on SBC, which we'll do for some period of time. | [Q2 2026 call, p.18] | the dilution note |
| Depreciation and hiring | will continue to put pressure on the P&L in the form of higher depreciation expense and related data center operations costs, such as energy. We also expect to continue hiring in key investment areas such as AI and cloud | [Q2 2026 call, p.13–14] | not numeric (informs analyst margin paths) |

## Sources

Every source tag used above, the cached file it points to (relative to the company folder), and the document date.

| Tag | Cached file | Date | Note |
|---|---|---|---|
| [10-Q Q2 2026, …] | `sources/2026-Q2/10-Q-2026-Q2.txt` | 2026-07-23 | quarter ended 2026-06-30; the date is the filing date |
| [10-Q Q1 2026, …] | `sources/2026-Q1/10-Q-2026-Q1.txt` | 2026-04-30 | quarter ended 2026-03-31; the date is the filing date |
| [10-K FY2025, …] | `sources/2026-Q1/10-K-FY2025.txt` | 2026-02-05 | 10-K for the year ended 2025-12-31; the date is the filing date |
| [10-K FY2023, …] | `sources/2026-Q1/10-K-FY2023.txt` | 2024-01-31 | 10-K for the year ended 2023-12-31; the date is the filing date; used for the FY2021–FY2022 history |
| [Q2 2026 call, p.N] | `sources/2026-Q2/transcript.txt` | 2026-07-22 | company-published transcript, tier 1; page numbers are the PDF's own |
| [Q2 2026 release, p.N] | `sources/2026-Q2/press-release.txt` | 2026-07-22 | earnings press release, 8-K Exhibit 99.1 |
| [Q2 2026 slides, p.N] | `sources/2026-Q2/slides.txt` | 2026-07-22 | earnings slides |
| [8-K 2026-06-04] | `sources/2026-Q2/8-K-2026-06-04.txt` | 2026-06-04 | at-the-market equity programme, common-stock offering and Berkshire private placement |
| [8-K 2026-06-05 (preferred)] | `sources/2026-Q2/8-K-2026-06-05-preferred.txt` | 2026-06-05 | mandatory convertible preferred offering and capped calls |
| [Damodaran betas.xls, …] | `tools/valuation/data/damodaran/betas.csv` | 2026-01-05 | engine-cached dataset, dated as cited in the source tag; not read by the analyst |
| [Yahoo price 338.46 on 2026-09-04] | `none (fetched)` | 2026-09-04 | spot price fetched by the engine at run time; nothing cached in the repo |
