# AVGO valuation assumptions as of FY2026-Q2

This file is a read-only view of the valuation inputs for Broadcom Inc. (AVGO), held in `assumptions.yaml`. Every number and every sentence below comes from that file; nothing is computed here. To change a number, use the app (`uv run --extra app valuation-app`), which saves into the YAML, records the change, and rewrites this file. A dash (—) marks a cell that is empty in the file: the analyst had nothing defensible to put there, or the item is not given. Rates are stored as decimals and shown here as percentages; money is in USD millions.

| Item | Value |
|---|---|
| Ticker | AVGO |
| Company | Broadcom Inc. |
| As-of quarter | FY2026-Q2 |
| As-of date (quarter cutoff) | 2026-06-09 |
| Drafted | 2026-09-18 |
| Horizon | 10 forecast years, then a terminal value |
| Currency and units | USD, millions |

## 1. The stories

Each story is copied word for word from `assumptions.yaml`.

### Bear (weight 25.0%)

The announced AI buildout still creates a large first step in sales, but customers then delay projects and move more chip design in house. Software renewals become harder, and price concessions outweigh the benefit of spreading engineering costs over more sales. Broadcom keeps paying for research and inventory while old acquisition charges expire, and cannot recover all working capital when growth stalls. Its competitive advantage eventually disappears, and normal taxes replace today’s unusual tax benefits.

How the story becomes numbers:

| What the story says | Which input it sets | The number | Source |
|---|---|---|---|
| The announced AI buildout still creates a large first step in sales, but customers then delay projects and move more chip design in house. | revenue_growth.values, years1–10 | [0.4311270125, 0.0583333333, -0.0174978128, -0.0080142476, 0.0197486535, 0.0220070423, 0.0215331611, 0.021079258, 0.0206440958, 0.0202265372] | [10-Q Q2 FY2026]; [Q2 FY2026 call] |
| Engineering, stock pay, software mix and expiring acquisition costs produce this GAAP margin path. | operating_margin.values, years1–10 | [0.47075, 0.4484820647, 0.4148975957, 0.3954308797, 0.3928785211, 0.3877906977, 0.3814924115, 0.3750247729, 0.3717799353, 0.3611022998] | [10-Q Q2 FY2026]; [Mature benchmark evidence] |
| The business funds inventory, contracts and equipment before sales, while acquisition amortization is reconciled once. | sales_to_capital.value, value_late; reinvestment_override.values | 1.5, 1.2; [-2609.0, -5456.55, -4564.0, -1946.333, -254.333, 1363.833, 1878.333, 2390.833, 2701.333, 2732.167] | [Valuation base evidence]; [Mature benchmark evidence] |
| Taxes normalize and the mature franchise earns the long-run return specified by this case. | tax_rate.start, terminal; terminal.growth.value; terminal.roic_premium.value; shared cost of capital | 0.20, 0.25; 0.02; 0; shared build | [10-K FY2025]; [Mature benchmark evidence]; [Market inputs] |

### Base (weight 50.0%)

Broadcom supplies several generations of custom AI chips and networking equipment, while established software customers mostly renew. The initial expansion is rapid, then customers gain bargaining power and growth settles as this much larger business matures. Engineering costs grow more slowly than sales at first, but lower software mix and competition later offset much of the benefit from expiring acquisition charges. Research remains an expense, and the company funds inventory, customer contracts and equipment before collecting the next year’s sales. Repeated design wins and the cost of replacing infrastructure software preserve a moderate long-term advantage after taxes normalize.

How the story becomes numbers:

| What the story says | Which input it sets | The number | Source |
|---|---|---|---|
| Broadcom supplies several generations of custom AI chips and networking equipment, while established software customers mostly renew. | revenue_growth.values, years1–10 | [0.6272444179, 0.259771987, 0.1861667744, 0.1264305177, 0.0851475568, 0.0682122158, 0.0538397329, 0.0459405941, 0.0352139341, 0.0299926847] | [10-Q Q2 FY2026]; [Q2 FY2026 call] |
| Engineering, stock pay, software mix and expiring acquisition costs produce this GAAP margin path. | operating_margin.values, years1–10 | [0.5254641694, 0.5521557854, 0.5568228883, 0.5479095307, 0.5399331253, 0.5367579299, 0.5303683168, 0.5228303673, 0.5135588881, 0.5032954545] | [10-Q Q2 FY2026]; [Mature benchmark evidence] |
| The business funds inventory, contracts and equipment before sales, while acquisition amortization is reconciled once. | sales_to_capital.value, value_late; reinvestment_override.values | 2.5, 2.0; [6025.0, 6040.0, 5072.0, 4103.5, 4752.5, 6348.0, 6264.5, 5672.5, 5467.0, 5632.0] | [Valuation base evidence]; [Mature benchmark evidence] |
| Taxes normalize and the mature franchise earns the long-run return specified by this case. | tax_rate.start, terminal; terminal.growth.value; terminal.roic_premium.value; shared cost of capital | 0.20, 0.25; 0.03; 0.0856; shared build | [10-K FY2025]; [Mature benchmark evidence]; [Market inputs] |

### Bull (weight 25.0%)

Custom AI chips win a much larger place in data centers, and Broadcom keeps winning successive designs from several large buyers. Networking leadership and software renewals allow both businesses to expand even after the first deployment wave. Sales initially grow faster than engineering and compensation costs, while later competition takes back part of that gain. Suppliers and customers help fund the ramp, although Broadcom still invests in inventory, equipment and new designs. Those recurring relationships preserve stronger long-term returns after normal taxes, rather than making today’s contracts permanent.

How the story becomes numbers:

| What the story says | Which input it sets | The number | Source |
|---|---|---|---|
| Custom AI chips win a much larger place in data centers, and Broadcom keeps winning successive designs from several large buyers. | revenue_growth.values, years1–10 | [0.8419134698, 0.4064748201, 0.2378516624, 0.1714876033, 0.1065255732, 0.0844756136, 0.0702527925, 0.0530074155, 0.0435576421, 0.0387403149] | [10-Q Q2 FY2026]; [Q2 FY2026 call] |
| Engineering, stock pay, software mix and expiring acquisition costs produce this GAAP margin path. | operating_margin.values, years1–10 | [0.547381295, 0.5746112532, 0.5879938017, 0.5889241623, 0.5844437361, 0.5818412698, 0.5760711343, 0.5672274387, 0.5577793052, 0.5475697786] | [10-Q Q2 FY2026]; [Mature benchmark evidence] |
| The business funds inventory, contracts and equipment before sales, while acquisition amortization is reconciled once. | sales_to_capital.value, value_late; reinvestment_override.values | 3.0, 2.2; [12179.333, 10224.0, 9917.833, 7514.167, 7912.833, 11264.636, 9795.227, 9209.909, 9045.955, 7745.273] | [Valuation base evidence]; [Mature benchmark evidence] |
| Taxes normalize and the mature franchise earns the long-run return specified by this case. | tax_rate.start, terminal; terminal.growth.value; terminal.roic_premium.value; shared cost of capital | 0.20, 0.25; 0.03; 0.1256; shared build | [10-K FY2025]; [Mature benchmark evidence]; [Market inputs] |

### Management (not weighted; computed)

Management’s stated AI revenue targets are achieved at their disclosed floor, with the next fiscal year weighted toward its second half. The analyst fills the periods and businesses for which management gave no annual target using the central operating case. The same central cost and capital assumptions keep research and stock compensation as expenses and fund growth before customers pay. The mature business retains the central case’s moderate advantage after taxes normalize; these later assumptions belong to the analyst, not management.

How the story becomes numbers:

| What the story says | Which input it sets | The number | Source |
|---|---|---|---|
| Management’s stated AI revenue targets are achieved at their disclosed floor, with the next fiscal year weighted toward its second half. | revenue_growth.values, years1–10 | [0.710726827, 0.2881487219, 0.1888153939, 0.1284774911, 0.0860600628, 0.0685101114, 0.0544611819, 0.0465201465, 0.0353517676, 0.0300878972] | [10-Q Q2 FY2026]; [Q2 FY2026 call] |
| Engineering, stock pay, software mix and expiring acquisition costs produce this GAAP margin path. | operating_margin.values, years1–10 | [0.5281603408, 0.5540499098, 0.5578958017, 0.5483850291, 0.5397730087, 0.5361483198, 0.5296190476, 0.5219583479, 0.5125862069, 0.5023055464] | [10-Q Q2 FY2026]; [Mature benchmark evidence] |
| The business funds inventory, contracts and equipment before sales, while acquisition amortization is reconciled once. | sales_to_capital.value, value_late; reinvestment_override.values | 2.5, 2.0; [8176.5, 7138.0, 6023.0, 4825.5, 5362.5, 7044.5, 6917.0, 6180.5, 5929.0, 6094.0] | [Valuation base evidence]; [Mature benchmark evidence] |
| Taxes normalize and the mature franchise earns the long-run return specified by this case. | tax_rate.start, terminal; terminal.growth.value; terminal.roic_premium.value; shared cost of capital | 0.20, 0.25; 0.03; 0.0856; shared build | [10-K FY2025]; [Mature benchmark evidence]; [Market inputs] |

Why this case is computed: Management supplied multi-year AI revenue targets, so a management operating case is conceptually available; shared unresolved bridge claims still prevent a completed valuation. [Q2 FY2026 call]

## 2. Scenario inputs

Rows are inputs and columns are cases. Per-year cells read year 1 / year 2 / ... in order. The reasons and sources behind each cell follow the table.

| Input | Bear | Base | Bull | Management |
|---|---|---|---|---|
| Weight | 25.0% | 50.0% | 25.0% | not weighted |
| Computable | always | always | always | yes |
| Revenue growth, years 1-10 | 43.1% / 5.8% / -1.7% / -0.8% / 2.0% / 2.2% / 2.2% / 2.1% / 2.1% / 2.0% | 62.7% / 26.0% / 18.6% / 12.6% / 8.5% / 6.8% / 5.4% / 4.6% / 3.5% / 3.0% | 84.2% / 40.6% / 23.8% / 17.1% / 10.7% / 8.4% / 7.0% / 5.3% / 4.4% / 3.9% | 71.1% / 28.8% / 18.9% / 12.8% / 8.6% / 6.9% / 5.4% / 4.7% / 3.5% / 3.0% |
| Operating margin, years 1-10 | 47.1% / 44.8% / 41.5% / 39.5% / 39.3% / 38.8% / 38.1% / 37.5% / 37.2% / 36.1% | 52.5% / 55.2% / 55.7% / 54.8% / 54.0% / 53.7% / 53.0% / 52.3% / 51.4% / 50.3% | 54.7% / 57.5% / 58.8% / 58.9% / 58.4% / 58.2% / 57.6% / 56.7% / 55.8% / 54.8% | 52.8% / 55.4% / 55.8% / 54.8% / 54.0% / 53.6% / 53.0% / 52.2% / 51.3% / 50.2% |
| Sales-to-capital, years 1-5 | 1.50 | 2.50 | 3.00 | 2.50 |
| Sales-to-capital, years 6-10 | 1.20 | 2.00 | 2.20 | 2.00 |
| Reinvestment override, years 1-10 (USD millions) | -2,609 / -5,456.6 / -4,564 / -1,946.3 / -254.3 / 1,363.8 / 1,878.3 / 2,390.8 / 2,701.3 / 2,732.2 | 6,025 / 6,040 / 5,072 / 4,103.5 / 4,752.5 / 6,348 / 6,264.5 / 5,672.5 / 5,467 / 5,632 | 12,179.3 / 10,224 / 9,917.8 / 7,514.2 / 7,912.8 / 11,264.6 / 9,795.2 / 9,209.9 / 9,046.0 / 7,745.3 | 8,176.5 / 7,138 / 6,023 / 4,825.5 / 5,362.5 / 7,044.5 / 6,917 / 6,180.5 / 5,929 / 6,094 |
| Tax rate, forecast years | 20.0% | 20.0% | 20.0% | 20.0% |
| Tax rate, terminal year onwards | 25.0% | 25.0% | 25.0% | 25.0% |
| Cost of capital override | — | — | — | — |
| Terminal growth | 2.00% | 3.00% | 3.00% | 3.00% |
| Terminal growth may exceed the risk-free rate | no | no | no | no |
| Terminal return on capital: points above the cost of capital | 0.00% | 8.56% | 12.56% | 8.56% |
| A large premium is allowed (above base 8, bull 12 points) | no | yes | yes | yes |

### Bear: reasons

- **Revenue growth** — Existing commitments still lift the first forward year, but subsequent projects stall and customers do more design themselves; software pricing also loses force. This downside follows the concentration and inventory risks in business.md §6 while preserving the already visible ramp. [10-Q Q2 FY2026; Q2 FY2026 call] [10-Q Q2 FY2026]; [Q2 FY2026 release]; [Q2 FY2026 call]; [WSTS spring 2026]

    Observed starting point: TTM semiconductor47,762 and software27,703 sum to75,465. Q2 revenue22,187 grew47.87% from15,004; Q2 semiconductor15,009 versus8,408 grew78.50%, while software7,178 versus6,596 grew8.82%. The release’s next-quarter revenue29,400 and AI16,000 imply substantial acceleration; the first model year is May2026–May2027, not FY2026. [10-Q Q2 FY2026, Note 9; Q2 FY2026 release]
    
    First-year AI of 60,000 is an analyst assumption of 30,000 in H2 FY2026 and 30,000 in H1 FY2027, below the 36,800 H2 amount implied by management’s fiscal target; older chips add 17,000 and software 31,000. Year-two AI rises only slightly and then contracts for two years; neither a specific lost customer nor an invented unit price is claimed. The defensible downside band is roughly 50,000–70,000 first-year AI and 60,000–90,000 at maturity, with software broadly flat after the initial contract conversion. The chosen middle of that downside range reflects delays and substitution rather than Broadcom failing as a firm. A guide cut, a second supplier replacing a large program, or declining software renewals would support this case; on-time conversion of the disclosed fiscal targets would weaken it.
    
    Annual build in USD millions; AI/other-chip splits after the disclosed starting segment are analyst judgments, not audited subsegments:
    
    | Model year, ends about May | AI judgment | Other chips judgment | Semiconductor total | Software judgment | Company total | Growth |
    | --- | --- | --- | --- | --- | --- | --- |
    | 1 / 2027 | 60,000 | 17,000 | 77,000 | 31,000 | 108,000 | 43.1127% |
    | 2 / 2028 | 65,000 | 17,300 | 82,300 | 32,000 | 114,300 | 5.8333% |
    | 3 / 2029 | 63,000 | 17,300 | 80,300 | 32,000 | 112,300 | -1.7498% |
    | 4 / 2030 | 62,000 | 17,400 | 79,400 | 32,000 | 111,400 | -0.8014% |
    | 5 / 2031 | 64,000 | 17,600 | 81,600 | 32,000 | 113,600 | 1.9749% |
    | 6 / 2032 | 66,000 | 17,800 | 83,800 | 32,300 | 116,100 | 2.2007% |
    | 7 / 2033 | 68,000 | 18,000 | 86,000 | 32,600 | 118,600 | 2.1533% |
    | 8 / 2034 | 70,000 | 18,200 | 88,200 | 32,900 | 121,100 | 2.1079% |
    | 9 / 2035 | 72,000 | 18,400 | 90,400 | 33,200 | 123,600 | 2.0644% |
    | 10 / 2036 | 74,000 | 18,600 | 92,600 | 33,500 | 126,100 | 2.0227% |
    
    Every segment sum is exact; growth ratios are stored to10 decimals solely to reproduce the rounded revenue totals, with less than0.01 of cumulative rounding. Years6–10 are explicit because customer bargaining and the maturing product mix need a slower cost/growth path than holding year-five margins constant. No undisclosed chip quantity, price per gigawatt, new backlog or platform financing is added to sales.
    
    Year-five revenue113,600; final-year revenue126,100, with semiconductor73.4% and software26.6%. Against the broad2036 non-memory ceiling1,438,757, chips would be6.4%; AI alone would be8.4% of a similarly extrapolated logic ceiling883,293. This large-share requirement is a plausibility test, not demonstrated market access. WSTS only forecasts through2027;6% subsequent growth is an analyst assumption, and3–9% alternatives materially change the denominator. [WSTS spring 2026]
    
    Software ends at33,500, compared with Microsoft PBP’s observed FY2025 revenue120,810 and13.10% growth, and Cisco’s total56,654 with5.30% growth including more Splunk. Those broader businesses establish an order of magnitude and mature growth outcomes; they do not prove VMware’s addressable market. The proposed software path requires retention through successive renewals and slows to0.90% in year10. [Mature benchmark evidence; MSFT FY2025 10-K; CSCO FY2025 10-K]
    
    
    Current AI-chip leader scale check: NVIDIA reported FY2026 revenue215,938 and Q1FY2027 revenue81,615 against44,062 a year earlier; reconstructed TTM=215,938+81,615-44,062=253,491. Its latest-quarter Data Center revenue is75,200. These releases were published February25 and May20,2026, before the cutoff. This case’s final Broadcom consolidated revenue126,100 is0.50 times that observed NVIDIA TTM; final semiconductor revenue92,600 is0.37 times it. This is a present-scale comparison against a rapidly growing leader, not a forecast that NVIDIA stops growing or a claim of mature margins/market size. NVIDIA sells compute platforms, networking and systems alongside chips; Broadcom’s call describes its revenue as chips, so supply-chain scope differs. No future share is inferred from this ratio. [NVDA FY2026 release; NVDA Q1 FY2027 release; Q2 FY2026 call]
- **Operating margin** — The margin bridge keeps stock pay and research as costs while acquisition charges expire; scale helps initially, then competition and a smaller software share offset it. Each segment is modeled before reconciling back to GAAP, as business.md §3 requires. [10-Q Q2 FY2026; Mature benchmark evidence] [10-Q Q2 FY2026]; [10-K FY2025]; [Mature benchmark evidence]

    Observed: TTM GAAP margin43.3923%; current-quarter48.6231%. Q2 segment margins are9,281/15,009=61.8362% chips and5,647/7,178=78.6709% software, but exclude SBC2,092, acquired amortization1,967 and restructuring81. The combined segment margin is not GAAP; subtract all excluded costs once. [10-Q Q2 FY2026, Notes 4,7,9]
    
    Analyst arithmetic: GAAP EBIT = semiconductor sales×chip segment margin + software sales×software segment margin - forecast SBC -0.5% of sales for ongoing restructuring/acquisition overhead - disclosed/interpolated acquired amortization. Segment margins retain ordinary R&D, ordinary selling costs, rent and physical depreciation; no additional R&D add-back is made. Future SBC stays above the current TTM dollar expense even where its share of sales falls; the downside permits dollar costs to decline after the initial ramp. Every row below is a future judgment except the sourced amortization schedule’s disclosed fiscal buckets.
    
    | Year | Chip segment margin | Software segment margin | SBC / sales | Other costs / sales | Acquired amortization | GAAP margin | Physical depreciation check |
    | --- | --- | --- | --- | --- | --- | --- | --- |
    | 1 | 60.0% | 77.0% | 10.5% | 0.5% | 7,349.0 | 47.075% | 704.7 |
    | 2 | 56.0% | 75.0% | 10.5% | 0.5% | 6,253.5 | 44.848% | 917.5 |
    | 3 | 50.0% | 73.0% | 10.0% | 0.5% | 5,125.5 | 41.490% | 1,136.8 |
    | 4 | 47.0% | 70.0% | 10.0% | 0.5% | 3,970.0 | 39.543% | 1,351.8 |
    | 5 | 45.0% | 68.0% | 9.5% | 0.5% | 2,489.0 | 39.288% | 1,568.7 |
    | 6 | 43.0% | 66.0% | 9.0% | 0.5% | 1,300.0 | 38.779% | 1,691.0 |
    | 7 | 42.0% | 65.0% | 9.0% | 0.5% | 798.0 | 38.149% | 1,709.6 |
    | 8 | 41.0% | 64.0% | 9.0% | 0.5% | 298.0 | 37.502% | 1,729.2 |
    | 9 | 40.0% | 63.0% | 8.5% | 0.5% | 0.0 | 37.178% | 1,760.7 |
    | 10 | 39.0% | 62.0% | 8.5% | 0.5% | 0.0 | 36.110% | 1,797.8 |
    
    Lower chip prices and weaker software retention reduce segment margins toward mature hardware outcomes, even as noncash acquisition charges expire. The final consolidated margin is above Cisco’s20.76% and Qualcomm’s27.90% because a meaningful software and differentiated-IP business remains; it is below Broadcom’s FY2023 GAAP45.25%. A roughly30–40% final GAAP range supports the rounded operating-cost choices. Lost designs and renewals support the downside; sustained current segment profitability would contradict it. [Mature benchmark evidence]
    
    Both drags and offsets matter: software’s shrinking revenue weight lowers aggregate profitability; custom compute has lower gross margins than networking; research, stock pay and supplier costs continue. Against that, the current chip business already demonstrates operating leverage and the charge for old acquisitions expires. Physical capex/depreciation uses the same cohort check as the investment detail; depreciation rises from the603 TTM anchor to1,798, and is already inside the chosen segment margins. These margins require revenue growth and price/mix to fund that extra depreciation, not its omission. A five-year physical life is an analyst midpoint within the disclosed3–10-year equipment range; new buildings have longer lives and are not separately forecast. [Q2 FY2026 call; 10-K FY2025, Note 2; Valuation base evidence]
    
    Observed: the May 3 intangible schedule is FY2026 remainder 3,940; FY2027 6,818; FY2028 5,689; FY2029 4,562; FY2030 3,378; thereafter 3,196, total 27,583. Purchased technology and customer relationships have weighted remaining lives of five and six years; this is not a schedule for hypothetical future acquisitions. [10-Q Q2 FY2026, Note 4]
    
    Analyst interpolation: spread each named fiscal year evenly across its two half-years. Allocate the otherwise undated thereafter bucket to FY2031/FY2032/FY2033 as 1,600/1,000/596, a declining illustrative schedule, not a disclosed fifth rolling-year amount. This gives rolling model-year amortization of 7,349; 6,253.5; 5,125.5; 3,970; 2,489; 1,300; 798; 298; 0; 0, summing exactly to 27,583. The fifth-year assumption can reasonably vary by about 800 either side without changing the remaining total; a revised filing schedule would replace this allocation. The same annual amount is deducted in margin and subtracted in net investment, so changing the timing does not create a duplicate cash add-back; taxes remain a simplified rate on forecast EBIT.
    
    Future engineering creates replacement products within expensed R&D, and all cases keep a physical-equipment/working-capital budget. The model does not declare the business maintenance-free when acquisition charges expire. A new acquisition or material intangible impairment requires rebuilding both sides of this bridge. [Accounting and reinvestment method]
- **Sales-to-capital** — Use the stated organic-growth funding budget, then reduce capital efficiency as the business matures. The annual overrides reconcile acquisition amortization and prevent a slowdown from creating unsupported cash releases. [Valuation base evidence; Mature benchmark evidence] [Valuation base evidence]; [Mature benchmark evidence]

    Observed lagged history uses investment in year t against sales added in t+1, consistent with the selected one-year lag. The GAAP proxy is capex minus physical depreciation, plus a cash-flow proxy for noncash current operating capital, plus net cash acquisitions/disposals, minus acquired amortization. [Valuation base evidence]
    
    | FY investment | GAAP net proxy | Following FY sales increase | Lag-1 result |
    | --- | --- | --- | --- |
    | 2021 | -5,704 | 5,753 | Unusable negative denominator |
    | 2022 | -3,000 | 2,616 | Unusable negative denominator |
    | 2023 | -2,386 | 15,755 | Unusable; VMware revenue appears next year |
    | 2024 | 15,828 cash-only; 77,616 full-consideration illustration | 12,313 | 0.778x cash-only; 0.159x full-consideration illustration |
    | 2025 | -3,431 | Not yet observable | No FY2026 result at cutoff |
    
    The pre-acquired-amortization cash proxy gives 1.925x for FY2022, 18.298x for FY2023 and 0.491x for FY2024; the latter two are acquisition-distorted. The current-capital proxy includes mixed tax/interest lines; including all long-term cash-flow changes would change FY2025 net investment from -3,431 to +187. No one of these is a clean marginal growth-capital estimate. VMware’s stock-funded consideration is not omitted merely because it was absent from cash investing. [Valuation base evidence; 10-K FY2025; 10-K FY2023]
    
    Mature stock sales/book capital is 0.490x Broadcom, 0.963x Cisco, 1.712x Qualcomm and 0.833x Microsoft consolidated. The screen retains goodwill and R&D expense, treats operating leases as rent, and includes Microsoft finance leases; Microsoft PBP and Qualcomm QCT standalone capital are not disclosed. These are accumulated-capital measures, not next-year incremental sales/investment. The forecast ratios may exceed them because no new large goodwill purchase is assumed and current R&D remains fully expensed; there is no claim that past goodwill can be recovered. [Mature benchmark evidence]
    
    Forecast construction, all explicit years: growth-capital budget=max(next-year sales increase,0)/selected ratio. Add a maintenance allowance of 0.5% of current-year sales, then floor this pre-amortization net budget at gross physical capex less physical depreciation. Net investment equals that budget minus this year’s acquired amortization. Ratios are therefore contextual budget parameters; the displayed annual overrides, not an unadjusted ratio, determine final net investment. A contraction does not mechanically release working capital. The lower bear ratio buys more inventory/contract capital per dollar of future sales, while the bull assumes more supplier/customer support.
    
    Physical check: gross capex is an analyst assumption of 1.5% of sales versus 1.0–1.6% in FY2021–FY2025 and TTM 860. Start physical depreciation at TTM 603, retire that legacy run-rate evenly over five years, and depreciate each new annual capex cohort over five years with a half-year convention. Five years lies within the disclosed 3–10-year equipment lives; 15–40-year buildings are a small but unseparated component, so this is a check, not a reported asset rollforward. Future segment margins below include this depreciation burden. The rest of the budget is working capital, contract assets and supply-chain funding, not capitalized R&D or the separately unvalued customer-lease guarantee. [10-K FY2025, Note 2; Valuation base evidence]
    
    The ordinary investment range is uncertain: sustained net pre-amortization funding around 30–70% of the following sales increment is defensible for these cases against the FY2025 current-capital use of 4,882 and next-year uncertainty; exact ratios are not empirically estimable from acquisition-distorted history. The 128,110 purchase commitments and 164,600 committed contracts support budgeting material funding, but neither is automatically debt nor all cash paid at once. Payment terms, contract-asset disclosures and inventories growing persistently faster than shipments would change these choices. [10-Q Q2 FY2026, Notes 2 and 10]
    
    Case placement: Early1.2–1.8x and late1.0–1.5x;1.5/1.2 sits within that funding-heavy range as customer payments weaken.
    
    
    Broad industry context, kept distinct from the matched peer screen: the January5,2026 Damodaran capex dataset reports LTM sales/invested capital1.2067x for66 US Semiconductor firms and1.5382x for309 Software (System & Application) firms. These are broad aggregated stock ratios, not distributions, marginal growth yields or an AVGO-only rent/GAAP reconciliation; the dataset also reports net R&D within its investment measures. The forecast’s higher organic-growth budget ratio depends on expensing current research and avoiding another large goodwill acquisition, and its annual overrides then subtract acquired amortization consistently. The like-basis company comparisons above therefore carry more weight; do not multiply these aggregated ratios by an unrelated margin and call it observed industry ROIC. [Damodaran capital data]
- **Reinvestment override** — Use the explicit net-investment schedule so retained acquisition amortization is reversed exactly once while real equipment and operating funding are paid for. Management has given no capex target to substitute for this analyst budget. [Valuation base evidence; Q2 FY2026 call] [Valuation base evidence]; [Q2 FY2026 call]

    Observed lagged history uses investment in year t against sales added in t+1, consistent with the selected one-year lag. The GAAP proxy is capex minus physical depreciation, plus a cash-flow proxy for noncash current operating capital, plus net cash acquisitions/disposals, minus acquired amortization. [Valuation base evidence]
    
    | FY investment | GAAP net proxy | Following FY sales increase | Lag-1 result |
    | --- | --- | --- | --- |
    | 2021 | -5,704 | 5,753 | Unusable negative denominator |
    | 2022 | -3,000 | 2,616 | Unusable negative denominator |
    | 2023 | -2,386 | 15,755 | Unusable; VMware revenue appears next year |
    | 2024 | 15,828 cash-only; 77,616 full-consideration illustration | 12,313 | 0.778x cash-only; 0.159x full-consideration illustration |
    | 2025 | -3,431 | Not yet observable | No FY2026 result at cutoff |
    
    The pre-acquired-amortization cash proxy gives 1.925x for FY2022, 18.298x for FY2023 and 0.491x for FY2024; the latter two are acquisition-distorted. The current-capital proxy includes mixed tax/interest lines; including all long-term cash-flow changes would change FY2025 net investment from -3,431 to +187. No one of these is a clean marginal growth-capital estimate. VMware’s stock-funded consideration is not omitted merely because it was absent from cash investing. [Valuation base evidence; 10-K FY2025; 10-K FY2023]
    
    Mature stock sales/book capital is 0.490x Broadcom, 0.963x Cisco, 1.712x Qualcomm and 0.833x Microsoft consolidated. The screen retains goodwill and R&D expense, treats operating leases as rent, and includes Microsoft finance leases; Microsoft PBP and Qualcomm QCT standalone capital are not disclosed. These are accumulated-capital measures, not next-year incremental sales/investment. The forecast ratios may exceed them because no new large goodwill purchase is assumed and current R&D remains fully expensed; there is no claim that past goodwill can be recovered. [Mature benchmark evidence]
    
    Forecast construction, all explicit years: growth-capital budget=max(next-year sales increase,0)/selected ratio. Add a maintenance allowance of 0.5% of current-year sales, then floor this pre-amortization net budget at gross physical capex less physical depreciation. Net investment equals that budget minus this year’s acquired amortization. Ratios are therefore contextual budget parameters; the displayed annual overrides, not an unadjusted ratio, determine final net investment. A contraction does not mechanically release working capital. The lower bear ratio buys more inventory/contract capital per dollar of future sales, while the bull assumes more supplier/customer support.
    
    Physical check: gross capex is an analyst assumption of 1.5% of sales versus 1.0–1.6% in FY2021–FY2025 and TTM 860. Start physical depreciation at TTM 603, retire that legacy run-rate evenly over five years, and depreciate each new annual capex cohort over five years with a half-year convention. Five years lies within the disclosed 3–10-year equipment lives; 15–40-year buildings are a small but unseparated component, so this is a check, not a reported asset rollforward. Future segment margins below include this depreciation burden. The rest of the budget is working capital, contract assets and supply-chain funding, not capitalized R&D or the separately unvalued customer-lease guarantee. [10-K FY2025, Note 2; Valuation base evidence]
    
    The ordinary investment range is uncertain: sustained net pre-amortization funding around 30–70% of the following sales increment is defensible for these cases against the FY2025 current-capital use of 4,882 and next-year uncertainty; exact ratios are not empirically estimable from acquisition-distorted history. The 128,110 purchase commitments and 164,600 committed contracts support budgeting material funding, but neither is automatically debt nor all cash paid at once. Payment terms, contract-asset disclosures and inventories growing persistently faster than shipments would change these choices. [10-Q Q2 FY2026, Notes 2 and 10]
    
    | Year | Next sales increase | Budget before acquired amortization | Gross physical capex | Physical depreciation | Implied other net capital | Acquired amortization subtracted | Net investment override |
    | --- | --- | --- | --- | --- | --- | --- | --- |
    | 1 | 6,300.0 | 4,740.0 | 1,620.0 | 704.7 | 3,824.7 | 7,349.0 | -2,609.000 |
    | 2 | -2,000.0 | 797.0 | 1,714.5 | 917.5 | 0.0 | 6,253.5 | -5,456.550 |
    | 3 | -900.0 | 561.5 | 1,684.5 | 1,136.8 | 13.8 | 5,125.5 | -4,564.000 |
    | 4 | 2,200.0 | 2,023.7 | 1,671.0 | 1,351.8 | 1,704.5 | 3,970.0 | -1,946.333 |
    | 5 | 2,500.0 | 2,234.7 | 1,704.0 | 1,568.7 | 2,099.4 | 2,489.0 | -254.333 |
    | 6 | 2,500.0 | 2,663.8 | 1,741.5 | 1,691.0 | 2,613.3 | 1,300.0 | 1,363.833 |
    | 7 | 2,500.0 | 2,676.3 | 1,779.0 | 1,709.6 | 2,606.9 | 798.0 | 1,878.333 |
    | 8 | 2,500.0 | 2,688.8 | 1,816.5 | 1,729.2 | 2,601.5 | 298.0 | 2,390.833 |
    | 9 | 2,500.0 | 2,701.3 | 1,854.0 | 1,760.7 | 2,608.0 | 0.0 | 2,701.333 |
    | 10 | 2,522.0 | 2,732.2 | 1,891.5 | 1,797.8 | 2,638.4 | 0.0 | 2,732.167 |
    
    Negative net investment where it appears reflects the noncash amortization reversal; it does not assume selling goodwill or recovering inventory at book value. Physical capex is positive in every year. These overrides cover all ten years and supersede the displayed ratio mechanically; the terminal year separately uses growth/terminal return, so the transition requires review rather than automatically extending an unusually light capital budget.
    
    
    Broad industry context, kept distinct from the matched peer screen: the January5,2026 Damodaran capex dataset reports LTM sales/invested capital1.2067x for66 US Semiconductor firms and1.5382x for309 Software (System & Application) firms. These are broad aggregated stock ratios, not distributions, marginal growth yields or an AVGO-only rent/GAAP reconciliation; the dataset also reports net R&D within its investment measures. The forecast’s higher organic-growth budget ratio depends on expensing current research and avoiding another large goodwill acquisition, and its annual overrides then subtract acquired amortization consistently. The like-basis company comparisons above therefore carry more weight; do not multiply these aggregated ratios by an unrelated margin and call it observed industry ROIC. [Damodaran capital data]
- **Tax rate** — Normalize taxes above the reported benefit-heavy rate while allowing for foreign earnings, then reach the house mature rate. The early rate averages the transition rather than treating one quarter’s non-GAAP guidance as permanent. [10-K FY2025; Q2 FY2026 call] [10-K FY2025]; [Q2 FY2026 call]

    Observed TTM GAAP rate3.8125%; H1 FY2026 9.0914%; management guides approximately16% non-GAAP for Q3/FY2026. Singapore incentives expire through2030, Malaysia inFY2028, and minimum taxes already raise the burden. Those definitions differ from operating cash tax. A rounded20% early rate is an analyst normalization within18–23%, balancing geographic incentives against their expiry and the unreliable tax benefits;25% mature is the house marginal-tax assumption within a22–27% operating range. [10-K FY2025, Note12; 10-Q Q2 FY2026, Note8; Q2 FY2026 call]
    
    The engine holds20% in years1–5 and linearly fades21/22/23/24/25% in years6–10. This cannot reproduce the exact expiry years or an explicit tax-loss/credit ledger;20% early is a period-average approximation, so near-term tax can be overstated and midperiod tax understated. No immediate loss tax benefit is required in these profitable cases. The1,662 old uncertain-tax claim is separately deducted and excluded from normal future earnings taxes. A durable reported cash-tax reconciliation, enacted rate change or loss of incentives would change this choice.
- **Terminal growth** — Long-run growth slows below the dollar risk-free ceiling as products mature and some customers substitute their own designs. This is an analyst mature-state assumption. [Analyst judgment]

    Chosen growth2.0% lies within a1–3% bear or2–4% central/upside mature dollar range, not the temporary27% WSTS2027 logic growth. The final explicit growth2.02% transitions to this rate; no endless AI ramp is assumed. A materially shrinking installed base would justify zero or negative growth. [WSTS spring 2026]
- **Terminal return on capital premium** — The mature return comes from the expected franchise and the closest accounting-consistent peers, independently of the transition warning. The bear’s zero premium is the house convention that its advantage disappears. [Mature benchmark evidence]

    Selected independently before diagnostics: the bear uses the house no-moat return equal to WACC. The current terminal WACC is4.94% dollar risk-free plus4.5% mature ERP=9.44%; premium=0.0000%; implied reinvestment fraction=2.0%/9.44%=21.19% of after-tax operating profit. Terminal GAAP margin holds at the final row above; growth is2.0%. [Market inputs; Analyst judgment]
    
    Comparable mature historical returns on opening book capital at a uniform analytical21% tax: Broadcom15.99% GAAP or21.05% before acquired amortization; Cisco15.86% or18.78%; Qualcomm35.35% or36.27%; Microsoft consolidated37.37% or39.11%. These figures retain goodwill, expense R&D and treat ordinary leases as rent; Qualcomm has royalties and Microsoft has cloud finance leases, while PBP standalone capital is undisclosed. None is a marginal project return. [Mature benchmark evidence]
    
    This downside assumes customer substitution ultimately removes excess returns; a final-year book return above WACC may persist because internally developed research assets are missing from capital, but is not evidence for an eternal economic premium.
    
    Average return on the accumulated forecast book-capital balance can exceed this selected marginal return because R&D remains an expense, past acquired capital amortizes, and the explicit expansion uses existing technology. That difference is not permission to raise terminal returns. The runner/reviewer must compare final operating cash flow and book return with the terminal-year reinvestment requirement through restricted diagnostics, investigate the whole margin/capital/tax bridge and retain any economically supported discontinuity visibly. If the capital budget is insufficient on its own evidence, revise the budget rather than tune this premium to a warning threshold. [Business-drivers method]

### Base: reasons

- **Revenue growth** — Several AI programs ship, but delivery timing and customer bargaining keep the central path below management’s near-term trajectory before growth slows. Software renewals and a modest recovery in older chips supply the smaller part of the increase in business.md §2 and outlook.md §3. [10-Q Q2 FY2026; Q2 FY2026 call] [10-Q Q2 FY2026]; [Q2 FY2026 release]; [Q2 FY2026 call]; [WSTS spring 2026]

    Observed starting point: TTM semiconductor47,762 and software27,703 sum to75,465. Q2 revenue22,187 grew47.87% from15,004; Q2 semiconductor15,009 versus8,408 grew78.50%, while software7,178 versus6,596 grew8.82%. The release’s next-quarter revenue29,400 and AI16,000 imply substantial acceleration; the first model year is May2026–May2027, not FY2026. [10-Q Q2 FY2026, Note 9; Q2 FY2026 release]
    
    First-year AI of 72,000 is a rounded judgment: H2 FY2026 34,000 plus H1 FY2027 38,000, below management’s indicated fiscal path; older chips contribute 17,800 and software 33,000. Subsequent AI growth buys several customer generations, then falls as the installed base grows and buyers negotiate. A central first-year AI interval of roughly 65,000–80,000 and mature AI of 180,000–240,000 is more defensible than distinguishing nearby point estimates; the selected path occupies the middle. Annual software growth slows from about 19% to about 2%, rather than compounding the guided one-quarter 31% or Microsoft PBP’s recent 13% forever. Repeated guide delivery, stable software contract economics and continuing networking leadership would support it; customer insourcing, nonrenewal or unfunded deployments would reduce growth.
    
    Annual build in USD millions; AI/other-chip splits after the disclosed starting segment are analyst judgments, not audited subsegments:
    
    | Model year, ends about May | AI judgment | Other chips judgment | Semiconductor total | Software judgment | Company total | Growth |
    | --- | --- | --- | --- | --- | --- | --- |
    | 1 / 2027 | 72,000 | 17,800 | 89,800 | 33,000 | 122,800 | 62.7244% |
    | 2 / 2028 | 100,000 | 18,700 | 118,700 | 36,000 | 154,700 | 25.9772% |
    | 3 / 2029 | 125,000 | 19,500 | 144,500 | 39,000 | 183,500 | 18.6167% |
    | 4 / 2030 | 145,000 | 20,200 | 165,200 | 41,500 | 206,700 | 12.6431% |
    | 5 / 2031 | 160,000 | 20,800 | 180,800 | 43,500 | 224,300 | 8.5148% |
    | 6 / 2032 | 173,000 | 21,400 | 194,400 | 45,200 | 239,600 | 6.8212% |
    | 7 / 2033 | 184,000 | 21,900 | 205,900 | 46,600 | 252,500 | 5.3840% |
    | 8 / 2034 | 194,000 | 22,300 | 216,300 | 47,800 | 264,100 | 4.5941% |
    | 9 / 2035 | 202,000 | 22,600 | 224,600 | 48,800 | 273,400 | 3.5214% |
    | 10 / 2036 | 209,000 | 22,800 | 231,800 | 49,800 | 281,600 | 2.9993% |
    
    Every segment sum is exact; growth ratios are stored to10 decimals solely to reproduce the rounded revenue totals, with less than0.01 of cumulative rounding. Years6–10 are explicit because customer bargaining and the maturing product mix need a slower cost/growth path than holding year-five margins constant. No undisclosed chip quantity, price per gigawatt, new backlog or platform financing is added to sales.
    
    Year-five revenue224,300; final-year revenue281,600, with semiconductor82.3% and software17.7%. Against the broad2036 non-memory ceiling1,438,757, chips would be16.1%; AI alone would be23.7% of a similarly extrapolated logic ceiling883,293. This large-share requirement is a plausibility test, not demonstrated market access. WSTS only forecasts through2027;6% subsequent growth is an analyst assumption, and3–9% alternatives materially change the denominator. [WSTS spring 2026]
    
    Software ends at49,800, compared with Microsoft PBP’s observed FY2025 revenue120,810 and13.10% growth, and Cisco’s total56,654 with5.30% growth including more Splunk. Those broader businesses establish an order of magnitude and mature growth outcomes; they do not prove VMware’s addressable market. The proposed software path requires retention through successive renewals and slows to2.05% in year10. [Mature benchmark evidence; MSFT FY2025 10-K; CSCO FY2025 10-K]
    
    
    Current AI-chip leader scale check: NVIDIA reported FY2026 revenue215,938 and Q1FY2027 revenue81,615 against44,062 a year earlier; reconstructed TTM=215,938+81,615-44,062=253,491. Its latest-quarter Data Center revenue is75,200. These releases were published February25 and May20,2026, before the cutoff. This case’s final Broadcom consolidated revenue281,600 is1.11 times that observed NVIDIA TTM; final semiconductor revenue231,800 is0.91 times it. This is a present-scale comparison against a rapidly growing leader, not a forecast that NVIDIA stops growing or a claim of mature margins/market size. NVIDIA sells compute platforms, networking and systems alongside chips; Broadcom’s call describes its revenue as chips, so supply-chain scope differs. No future share is inferred from this ratio. [NVDA FY2026 release; NVDA Q1 FY2027 release; Q2 FY2026 call]
- **Operating margin** — The margin bridge keeps stock pay and research as costs while acquisition charges expire; scale helps initially, then competition and a smaller software share offset it. Each segment is modeled before reconciling back to GAAP, as business.md §3 requires. [10-Q Q2 FY2026; Mature benchmark evidence] [10-Q Q2 FY2026]; [10-K FY2025]; [Mature benchmark evidence]

    Observed: TTM GAAP margin43.3923%; current-quarter48.6231%. Q2 segment margins are9,281/15,009=61.8362% chips and5,647/7,178=78.6709% software, but exclude SBC2,092, acquired amortization1,967 and restructuring81. The combined segment margin is not GAAP; subtract all excluded costs once. [10-Q Q2 FY2026, Notes 4,7,9]
    
    Analyst arithmetic: GAAP EBIT = semiconductor sales×chip segment margin + software sales×software segment margin - forecast SBC -0.5% of sales for ongoing restructuring/acquisition overhead - disclosed/interpolated acquired amortization. Segment margins retain ordinary R&D, ordinary selling costs, rent and physical depreciation; no additional R&D add-back is made. Future SBC stays above the current TTM dollar expense even where its share of sales falls; the downside permits dollar costs to decline after the initial ramp. Every row below is a future judgment except the sourced amortization schedule’s disclosed fiscal buckets.
    
    | Year | Chip segment margin | Software segment margin | SBC / sales | Other costs / sales | Acquired amortization | GAAP margin | Physical depreciation check |
    | --- | --- | --- | --- | --- | --- | --- | --- |
    | 1 | 64.0% | 79.0% | 9.0% | 0.5% | 7,349.0 | 52.546% | 726.9 |
    | 2 | 65.0% | 79.0% | 8.5% | 0.5% | 6,253.5 | 55.216% | 1,022.5 |
    | 3 | 64.0% | 78.0% | 8.0% | 0.5% | 5,125.5 | 55.682% | 1,409.2 |
    | 4 | 62.0% | 77.0% | 7.8% | 0.5% | 3,970.0 | 54.791% | 1,874.0 |
    | 5 | 60.0% | 76.0% | 7.5% | 0.5% | 2,489.0 | 53.993% | 2,399.9 |
    | 6 | 59.0% | 75.0% | 7.3% | 0.5% | 1,300.0 | 53.676% | 2,851.2 |
    | 7 | 58.0% | 74.0% | 7.1% | 0.5% | 798.0 | 53.037% | 3,173.1 |
    | 8 | 57.0% | 73.0% | 7.0% | 0.5% | 298.0 | 52.283% | 3,440.7 |
    | 9 | 56.0% | 72.0% | 7.0% | 0.5% | 0.0 | 51.356% | 3,661.7 |
    | 10 | 55.0% | 71.0% | 7.0% | 0.5% | 0.0 | 50.330% | 3,847.7 |
    
    The initial chip scale benefit raises segment profit modestly above the latest61.84%, then competition reduces it to55%; software falls from about78.67% to71% before unallocated charges. The final consolidated GAAP margin belongs in an approximate45–53% range: above Qualcomm/Cisco, near Broadcom’s52.51% FY2025 before-acquired-amortization sensitivity, and below Microsoft PBP’s57.75%. Those comparisons retain R&D/SBC except where the segment definitions explicitly exclude them. This premium needs differentiated IP and recurring software; a sustained fall in chip gross margin or renewal economics would move it lower. [Mature benchmark evidence]
    
    Both drags and offsets matter: software’s shrinking revenue weight lowers aggregate profitability; custom compute has lower gross margins than networking; research, stock pay and supplier costs continue. Against that, the current chip business already demonstrates operating leverage and the charge for old acquisitions expires. Physical capex/depreciation uses the same cohort check as the investment detail; depreciation rises from the603 TTM anchor to3,848, and is already inside the chosen segment margins. These margins require revenue growth and price/mix to fund that extra depreciation, not its omission. A five-year physical life is an analyst midpoint within the disclosed3–10-year equipment range; new buildings have longer lives and are not separately forecast. [Q2 FY2026 call; 10-K FY2025, Note 2; Valuation base evidence]
    
    Observed: the May 3 intangible schedule is FY2026 remainder 3,940; FY2027 6,818; FY2028 5,689; FY2029 4,562; FY2030 3,378; thereafter 3,196, total 27,583. Purchased technology and customer relationships have weighted remaining lives of five and six years; this is not a schedule for hypothetical future acquisitions. [10-Q Q2 FY2026, Note 4]
    
    Analyst interpolation: spread each named fiscal year evenly across its two half-years. Allocate the otherwise undated thereafter bucket to FY2031/FY2032/FY2033 as 1,600/1,000/596, a declining illustrative schedule, not a disclosed fifth rolling-year amount. This gives rolling model-year amortization of 7,349; 6,253.5; 5,125.5; 3,970; 2,489; 1,300; 798; 298; 0; 0, summing exactly to 27,583. The fifth-year assumption can reasonably vary by about 800 either side without changing the remaining total; a revised filing schedule would replace this allocation. The same annual amount is deducted in margin and subtracted in net investment, so changing the timing does not create a duplicate cash add-back; taxes remain a simplified rate on forecast EBIT.
    
    Future engineering creates replacement products within expensed R&D, and all cases keep a physical-equipment/working-capital budget. The model does not declare the business maintenance-free when acquisition charges expire. A new acquisition or material intangible impairment requires rebuilding both sides of this bridge. [Accounting and reinvestment method]
- **Sales-to-capital** — Use the stated organic-growth funding budget, then reduce capital efficiency as the business matures. The annual overrides reconcile acquisition amortization and prevent a slowdown from creating unsupported cash releases. [Valuation base evidence; Mature benchmark evidence] [Valuation base evidence]; [Mature benchmark evidence]

    Observed lagged history uses investment in year t against sales added in t+1, consistent with the selected one-year lag. The GAAP proxy is capex minus physical depreciation, plus a cash-flow proxy for noncash current operating capital, plus net cash acquisitions/disposals, minus acquired amortization. [Valuation base evidence]
    
    | FY investment | GAAP net proxy | Following FY sales increase | Lag-1 result |
    | --- | --- | --- | --- |
    | 2021 | -5,704 | 5,753 | Unusable negative denominator |
    | 2022 | -3,000 | 2,616 | Unusable negative denominator |
    | 2023 | -2,386 | 15,755 | Unusable; VMware revenue appears next year |
    | 2024 | 15,828 cash-only; 77,616 full-consideration illustration | 12,313 | 0.778x cash-only; 0.159x full-consideration illustration |
    | 2025 | -3,431 | Not yet observable | No FY2026 result at cutoff |
    
    The pre-acquired-amortization cash proxy gives 1.925x for FY2022, 18.298x for FY2023 and 0.491x for FY2024; the latter two are acquisition-distorted. The current-capital proxy includes mixed tax/interest lines; including all long-term cash-flow changes would change FY2025 net investment from -3,431 to +187. No one of these is a clean marginal growth-capital estimate. VMware’s stock-funded consideration is not omitted merely because it was absent from cash investing. [Valuation base evidence; 10-K FY2025; 10-K FY2023]
    
    Mature stock sales/book capital is 0.490x Broadcom, 0.963x Cisco, 1.712x Qualcomm and 0.833x Microsoft consolidated. The screen retains goodwill and R&D expense, treats operating leases as rent, and includes Microsoft finance leases; Microsoft PBP and Qualcomm QCT standalone capital are not disclosed. These are accumulated-capital measures, not next-year incremental sales/investment. The forecast ratios may exceed them because no new large goodwill purchase is assumed and current R&D remains fully expensed; there is no claim that past goodwill can be recovered. [Mature benchmark evidence]
    
    Forecast construction, all explicit years: growth-capital budget=max(next-year sales increase,0)/selected ratio. Add a maintenance allowance of 0.5% of current-year sales, then floor this pre-amortization net budget at gross physical capex less physical depreciation. Net investment equals that budget minus this year’s acquired amortization. Ratios are therefore contextual budget parameters; the displayed annual overrides, not an unadjusted ratio, determine final net investment. A contraction does not mechanically release working capital. The lower bear ratio buys more inventory/contract capital per dollar of future sales, while the bull assumes more supplier/customer support.
    
    Physical check: gross capex is an analyst assumption of 1.5% of sales versus 1.0–1.6% in FY2021–FY2025 and TTM 860. Start physical depreciation at TTM 603, retire that legacy run-rate evenly over five years, and depreciate each new annual capex cohort over five years with a half-year convention. Five years lies within the disclosed 3–10-year equipment lives; 15–40-year buildings are a small but unseparated component, so this is a check, not a reported asset rollforward. Future segment margins below include this depreciation burden. The rest of the budget is working capital, contract assets and supply-chain funding, not capitalized R&D or the separately unvalued customer-lease guarantee. [10-K FY2025, Note 2; Valuation base evidence]
    
    The ordinary investment range is uncertain: sustained net pre-amortization funding around 30–70% of the following sales increment is defensible for these cases against the FY2025 current-capital use of 4,882 and next-year uncertainty; exact ratios are not empirically estimable from acquisition-distorted history. The 128,110 purchase commitments and 164,600 committed contracts support budgeting material funding, but neither is automatically debt nor all cash paid at once. Payment terms, contract-asset disclosures and inventories growing persistently faster than shipments would change these choices. [10-Q Q2 FY2026, Notes 2 and 10]
    
    Case placement: Early2.0–3.0x and late1.5–2.5x;2.5/2.0 is a central organic-growth budget, better than stock capital turnover but well below the corrupted18x acquisition-period ratio.
    
    
    Broad industry context, kept distinct from the matched peer screen: the January5,2026 Damodaran capex dataset reports LTM sales/invested capital1.2067x for66 US Semiconductor firms and1.5382x for309 Software (System & Application) firms. These are broad aggregated stock ratios, not distributions, marginal growth yields or an AVGO-only rent/GAAP reconciliation; the dataset also reports net R&D within its investment measures. The forecast’s higher organic-growth budget ratio depends on expensing current research and avoiding another large goodwill acquisition, and its annual overrides then subtract acquired amortization consistently. The like-basis company comparisons above therefore carry more weight; do not multiply these aggregated ratios by an unrelated margin and call it observed industry ROIC. [Damodaran capital data]
- **Reinvestment override** — Use the explicit net-investment schedule so retained acquisition amortization is reversed exactly once while real equipment and operating funding are paid for. Management has given no capex target to substitute for this analyst budget. [Valuation base evidence; Q2 FY2026 call] [Valuation base evidence]; [Q2 FY2026 call]

    Observed lagged history uses investment in year t against sales added in t+1, consistent with the selected one-year lag. The GAAP proxy is capex minus physical depreciation, plus a cash-flow proxy for noncash current operating capital, plus net cash acquisitions/disposals, minus acquired amortization. [Valuation base evidence]
    
    | FY investment | GAAP net proxy | Following FY sales increase | Lag-1 result |
    | --- | --- | --- | --- |
    | 2021 | -5,704 | 5,753 | Unusable negative denominator |
    | 2022 | -3,000 | 2,616 | Unusable negative denominator |
    | 2023 | -2,386 | 15,755 | Unusable; VMware revenue appears next year |
    | 2024 | 15,828 cash-only; 77,616 full-consideration illustration | 12,313 | 0.778x cash-only; 0.159x full-consideration illustration |
    | 2025 | -3,431 | Not yet observable | No FY2026 result at cutoff |
    
    The pre-acquired-amortization cash proxy gives 1.925x for FY2022, 18.298x for FY2023 and 0.491x for FY2024; the latter two are acquisition-distorted. The current-capital proxy includes mixed tax/interest lines; including all long-term cash-flow changes would change FY2025 net investment from -3,431 to +187. No one of these is a clean marginal growth-capital estimate. VMware’s stock-funded consideration is not omitted merely because it was absent from cash investing. [Valuation base evidence; 10-K FY2025; 10-K FY2023]
    
    Mature stock sales/book capital is 0.490x Broadcom, 0.963x Cisco, 1.712x Qualcomm and 0.833x Microsoft consolidated. The screen retains goodwill and R&D expense, treats operating leases as rent, and includes Microsoft finance leases; Microsoft PBP and Qualcomm QCT standalone capital are not disclosed. These are accumulated-capital measures, not next-year incremental sales/investment. The forecast ratios may exceed them because no new large goodwill purchase is assumed and current R&D remains fully expensed; there is no claim that past goodwill can be recovered. [Mature benchmark evidence]
    
    Forecast construction, all explicit years: growth-capital budget=max(next-year sales increase,0)/selected ratio. Add a maintenance allowance of 0.5% of current-year sales, then floor this pre-amortization net budget at gross physical capex less physical depreciation. Net investment equals that budget minus this year’s acquired amortization. Ratios are therefore contextual budget parameters; the displayed annual overrides, not an unadjusted ratio, determine final net investment. A contraction does not mechanically release working capital. The lower bear ratio buys more inventory/contract capital per dollar of future sales, while the bull assumes more supplier/customer support.
    
    Physical check: gross capex is an analyst assumption of 1.5% of sales versus 1.0–1.6% in FY2021–FY2025 and TTM 860. Start physical depreciation at TTM 603, retire that legacy run-rate evenly over five years, and depreciate each new annual capex cohort over five years with a half-year convention. Five years lies within the disclosed 3–10-year equipment lives; 15–40-year buildings are a small but unseparated component, so this is a check, not a reported asset rollforward. Future segment margins below include this depreciation burden. The rest of the budget is working capital, contract assets and supply-chain funding, not capitalized R&D or the separately unvalued customer-lease guarantee. [10-K FY2025, Note 2; Valuation base evidence]
    
    The ordinary investment range is uncertain: sustained net pre-amortization funding around 30–70% of the following sales increment is defensible for these cases against the FY2025 current-capital use of 4,882 and next-year uncertainty; exact ratios are not empirically estimable from acquisition-distorted history. The 128,110 purchase commitments and 164,600 committed contracts support budgeting material funding, but neither is automatically debt nor all cash paid at once. Payment terms, contract-asset disclosures and inventories growing persistently faster than shipments would change these choices. [10-Q Q2 FY2026, Notes 2 and 10]
    
    | Year | Next sales increase | Budget before acquired amortization | Gross physical capex | Physical depreciation | Implied other net capital | Acquired amortization subtracted | Net investment override |
    | --- | --- | --- | --- | --- | --- | --- | --- |
    | 1 | 31,900.0 | 13,374.0 | 1,842.0 | 726.9 | 12,258.9 | 7,349.0 | 6,025.000 |
    | 2 | 28,800.0 | 12,293.5 | 2,320.5 | 1,022.5 | 10,995.5 | 6,253.5 | 6,040.000 |
    | 3 | 23,200.0 | 10,197.5 | 2,752.5 | 1,409.2 | 8,854.2 | 5,125.5 | 5,072.000 |
    | 4 | 17,600.0 | 8,073.5 | 3,100.5 | 1,874.0 | 6,847.0 | 3,970.0 | 4,103.500 |
    | 5 | 15,300.0 | 7,241.5 | 3,364.5 | 2,399.9 | 6,276.9 | 2,489.0 | 4,752.500 |
    | 6 | 12,900.0 | 7,648.0 | 3,594.0 | 2,851.2 | 6,905.2 | 1,300.0 | 6,348.000 |
    | 7 | 11,600.0 | 7,062.5 | 3,787.5 | 3,173.1 | 6,448.1 | 798.0 | 6,264.500 |
    | 8 | 9,300.0 | 5,970.5 | 3,961.5 | 3,440.7 | 5,449.7 | 298.0 | 5,672.500 |
    | 9 | 8,200.0 | 5,467.0 | 4,101.0 | 3,661.7 | 5,027.6 | 0.0 | 5,467.000 |
    | 10 | 8,448.0 | 5,632.0 | 4,224.0 | 3,847.7 | 5,255.6 | 0.0 | 5,632.000 |
    
    Negative net investment where it appears reflects the noncash amortization reversal; it does not assume selling goodwill or recovering inventory at book value. Physical capex is positive in every year. These overrides cover all ten years and supersede the displayed ratio mechanically; the terminal year separately uses growth/terminal return, so the transition requires review rather than automatically extending an unusually light capital budget.
    
    
    Broad industry context, kept distinct from the matched peer screen: the January5,2026 Damodaran capex dataset reports LTM sales/invested capital1.2067x for66 US Semiconductor firms and1.5382x for309 Software (System & Application) firms. These are broad aggregated stock ratios, not distributions, marginal growth yields or an AVGO-only rent/GAAP reconciliation; the dataset also reports net R&D within its investment measures. The forecast’s higher organic-growth budget ratio depends on expensing current research and avoiding another large goodwill acquisition, and its annual overrides then subtract acquired amortization consistently. The like-basis company comparisons above therefore carry more weight; do not multiply these aggregated ratios by an unrelated margin and call it observed industry ROIC. [Damodaran capital data]
- **Tax rate** — Normalize taxes above the reported benefit-heavy rate while allowing for foreign earnings, then reach the house mature rate. The early rate averages the transition rather than treating one quarter’s non-GAAP guidance as permanent. [10-K FY2025; Q2 FY2026 call] [10-K FY2025]; [Q2 FY2026 call]

    Observed TTM GAAP rate3.8125%; H1 FY2026 9.0914%; management guides approximately16% non-GAAP for Q3/FY2026. Singapore incentives expire through2030, Malaysia inFY2028, and minimum taxes already raise the burden. Those definitions differ from operating cash tax. A rounded20% early rate is an analyst normalization within18–23%, balancing geographic incentives against their expiry and the unreliable tax benefits;25% mature is the house marginal-tax assumption within a22–27% operating range. [10-K FY2025, Note12; 10-Q Q2 FY2026, Note8; Q2 FY2026 call]
    
    The engine holds20% in years1–5 and linearly fades21/22/23/24/25% in years6–10. This cannot reproduce the exact expiry years or an explicit tax-loss/credit ledger;20% early is a period-average approximation, so near-term tax can be overstated and midperiod tax understated. No immediate loss tax benefit is required in these profitable cases. The1,662 old uncertain-tax claim is separately deducted and excluded from normal future earnings taxes. A durable reported cash-tax reconciliation, enacted rate change or loss of incentives would change this choice.
- **Terminal growth** — Long-run nominal growth slows below the dollar risk-free ceiling as a much larger business follows replacement demand and modest market expansion. This is an analyst mature-state assumption. [Analyst judgment]

    Chosen growth3.0% lies within a1–3% bear or2–4% central/upside mature dollar range, not the temporary27% WSTS2027 logic growth. The final explicit growth3.00% transitions to this rate; no endless AI ramp is assumed. A materially shrinking installed base would justify zero or negative growth. [WSTS spring 2026]
- **Terminal return on capital premium** — The mature return is chosen from Broadcom’s normalized history and the peer range, with continued research and renewals needed to sustain it. Its premium exceeds a house warning threshold and is retained for that business reason, not to clear a diagnostic. [Mature benchmark evidence] [Mature benchmark evidence]

    Selected independently before diagnostics: 18% mature return in the central/management case. The current terminal WACC is4.94% dollar risk-free plus4.5% mature ERP=9.44%; premium=8.5600%; implied reinvestment fraction=3.0%/18.00%=16.67% of after-tax operating profit. Terminal GAAP margin holds at the final row above; growth is3.0%. [Market inputs; Analyst judgment]
    
    Comparable mature historical returns on opening book capital at a uniform analytical21% tax: Broadcom15.99% GAAP or21.05% before acquired amortization; Cisco15.86% or18.78%; Qualcomm35.35% or36.27%; Microsoft consolidated37.37% or39.11%. These figures retain goodwill, expense R&D and treat ordinary leases as rent; Qualcomm has royalties and Microsoft has cloud finance leases, while PBP standalone capital is undisclosed. None is a marginal project return. [Mature benchmark evidence]
    
    A15–20% mature return range has the closest direct support from Broadcom and Cisco;18% is central within that interval. Networking IP, repeated co-design and software migration costs must persist beyond the current contracts despite stronger buyers. Competitors and customers cannot capture all of those engineering and switching benefits in this case; sustained customer self-design or failed renewals would reduce the premium.
    
    Average return on the accumulated forecast book-capital balance can exceed this selected marginal return because R&D remains an expense, past acquired capital amortizes, and the explicit expansion uses existing technology. That difference is not permission to raise terminal returns. The runner/reviewer must compare final operating cash flow and book return with the terminal-year reinvestment requirement through restricted diagnostics, investigate the whole margin/capital/tax bridge and retain any economically supported discontinuity visibly. If the capital budget is insufficient on its own evidence, revise the budget rather than tune this premium to a warning threshold. [Business-drivers method]

### Bull: reasons

- **Revenue growth** — Broadcom wins successive AI designs and converts more of the announced deployment pipeline on time, while software and older chips also expand. This is the strong end of the operating range in outlook.md §3, requiring a much larger share of logic demand. [Q2 FY2026 call; WSTS spring 2026] [10-Q Q2 FY2026]; [Q2 FY2026 release]; [Q2 FY2026 call]; [WSTS spring 2026]

    Observed starting point: TTM semiconductor47,762 and software27,703 sum to75,465. Q2 revenue22,187 grew47.87% from15,004; Q2 semiconductor15,009 versus8,408 grew78.50%, while software7,178 versus6,596 grew8.82%. The release’s next-quarter revenue29,400 and AI16,000 imply substantial acceleration; the first model year is May2026–May2027, not FY2026. [10-Q Q2 FY2026, Note 9; Q2 FY2026 release]
    
    First-year AI of 85,000 assumes H2 FY2026 38,000 and H1 FY2027 47,000; this is above the disclosed fiscal trajectory and is explicitly analyst upside. Older chips of 19,000 and software of 35,000 add a cyclical recovery and stronger contract conversion. An upside first-year AI range of 80,000–95,000 and mature AI of 280,000–360,000 requires sustained share gains rather than just a large industry market. The selected 320,000 mature AI demand is near the middle of that range. Multiple on-time customer deployments and renewal strength would support it; sequential design losses or customers capturing substantially more chip economics would invalidate it.
    
    Annual build in USD millions; AI/other-chip splits after the disclosed starting segment are analyst judgments, not audited subsegments:
    
    | Model year, ends about May | AI judgment | Other chips judgment | Semiconductor total | Software judgment | Company total | Growth |
    | --- | --- | --- | --- | --- | --- | --- |
    | 1 / 2027 | 85,000 | 19,000 | 104,000 | 35,000 | 139,000 | 84.1913% |
    | 2 / 2028 | 135,000 | 20,500 | 155,500 | 40,000 | 195,500 | 40.6475% |
    | 3 / 2029 | 175,000 | 22,000 | 197,000 | 45,000 | 242,000 | 23.7852% |
    | 4 / 2030 | 210,000 | 23,500 | 233,500 | 50,000 | 283,500 | 17.1488% |
    | 5 / 2031 | 235,000 | 24,700 | 259,700 | 54,000 | 313,700 | 10.6526% |
    | 6 / 2032 | 257,000 | 25,700 | 282,700 | 57,500 | 340,200 | 8.4476% |
    | 7 / 2033 | 277,000 | 26,600 | 303,600 | 60,500 | 364,100 | 7.0253% |
    | 8 / 2034 | 293,000 | 27,400 | 320,400 | 63,000 | 383,400 | 5.3007% |
    | 9 / 2035 | 307,000 | 28,000 | 335,000 | 65,100 | 400,100 | 4.3558% |
    | 10 / 2036 | 320,000 | 28,600 | 348,600 | 67,000 | 415,600 | 3.8740% |
    
    Every segment sum is exact; growth ratios are stored to10 decimals solely to reproduce the rounded revenue totals, with less than0.01 of cumulative rounding. Years6–10 are explicit because customer bargaining and the maturing product mix need a slower cost/growth path than holding year-five margins constant. No undisclosed chip quantity, price per gigawatt, new backlog or platform financing is added to sales.
    
    Year-five revenue313,700; final-year revenue415,600, with semiconductor83.9% and software16.1%. Against the broad2036 non-memory ceiling1,438,757, chips would be24.2%; AI alone would be36.2% of a similarly extrapolated logic ceiling883,293. This large-share requirement is a plausibility test, not demonstrated market access. WSTS only forecasts through2027;6% subsequent growth is an analyst assumption, and3–9% alternatives materially change the denominator. [WSTS spring 2026]
    
    Software ends at67,000, compared with Microsoft PBP’s observed FY2025 revenue120,810 and13.10% growth, and Cisco’s total56,654 with5.30% growth including more Splunk. Those broader businesses establish an order of magnitude and mature growth outcomes; they do not prove VMware’s addressable market. The proposed software path requires retention through successive renewals and slows to2.92% in year10. [Mature benchmark evidence; MSFT FY2025 10-K; CSCO FY2025 10-K]
    
    
    Current AI-chip leader scale check: NVIDIA reported FY2026 revenue215,938 and Q1FY2027 revenue81,615 against44,062 a year earlier; reconstructed TTM=215,938+81,615-44,062=253,491. Its latest-quarter Data Center revenue is75,200. These releases were published February25 and May20,2026, before the cutoff. This case’s final Broadcom consolidated revenue415,600 is1.64 times that observed NVIDIA TTM; final semiconductor revenue348,600 is1.38 times it. This is a present-scale comparison against a rapidly growing leader, not a forecast that NVIDIA stops growing or a claim of mature margins/market size. NVIDIA sells compute platforms, networking and systems alongside chips; Broadcom’s call describes its revenue as chips, so supply-chain scope differs. No future share is inferred from this ratio. [NVDA FY2026 release; NVDA Q1 FY2027 release; Q2 FY2026 call]
- **Operating margin** — The margin bridge keeps stock pay and research as costs while acquisition charges expire; scale helps initially, then competition and a smaller software share offset it. Each segment is modeled before reconciling back to GAAP, as business.md §3 requires. [10-Q Q2 FY2026; Mature benchmark evidence] [10-Q Q2 FY2026]; [10-K FY2025]; [Mature benchmark evidence]

    Observed: TTM GAAP margin43.3923%; current-quarter48.6231%. Q2 segment margins are9,281/15,009=61.8362% chips and5,647/7,178=78.6709% software, but exclude SBC2,092, acquired amortization1,967 and restructuring81. The combined segment margin is not GAAP; subtract all excluded costs once. [10-Q Q2 FY2026, Notes 4,7,9]
    
    Analyst arithmetic: GAAP EBIT = semiconductor sales×chip segment margin + software sales×software segment margin - forecast SBC -0.5% of sales for ongoing restructuring/acquisition overhead - disclosed/interpolated acquired amortization. Segment margins retain ordinary R&D, ordinary selling costs, rent and physical depreciation; no additional R&D add-back is made. Future SBC stays above the current TTM dollar expense even where its share of sales falls; the downside permits dollar costs to decline after the initial ramp. Every row below is a future judgment except the sourced amortization schedule’s disclosed fiscal buckets.
    
    | Year | Chip segment margin | Software segment margin | SBC / sales | Other costs / sales | Acquired amortization | GAAP margin | Physical depreciation check |
    | --- | --- | --- | --- | --- | --- | --- | --- |
    | 1 | 66.0% | 80.0% | 9.0% | 0.5% | 7,349.0 | 54.738% | 751.2 |
    | 2 | 67.0% | 80.0% | 8.5% | 0.5% | 6,253.5 | 57.461% | 1,132.3 |
    | 3 | 67.0% | 80.0% | 8.0% | 0.5% | 5,125.5 | 58.799% | 1,668.0 |
    | 4 | 66.0% | 79.0% | 7.5% | 0.5% | 3,970.0 | 58.892% | 2,335.7 |
    | 5 | 65.0% | 78.0% | 7.5% | 0.5% | 2,489.0 | 58.444% | 3,110.9 |
    | 6 | 64.0% | 78.0% | 7.3% | 0.5% | 1,300.0 | 58.184% | 3,822.9 |
    | 7 | 63.0% | 77.0% | 7.0% | 0.5% | 798.0 | 57.607% | 4,377.6 |
    | 8 | 62.0% | 76.0% | 7.0% | 0.5% | 298.0 | 56.723% | 4,842.6 |
    | 9 | 61.0% | 75.0% | 7.0% | 0.5% | 0.0 | 55.778% | 5,229.6 |
    | 10 | 60.0% | 74.0% | 7.0% | 0.5% | 0.0 | 54.757% | 5,557.4 |
    
    Early semiconductor scale approaches the observed roughly70% gross margin while cash engineering expense grows more slowly than sales; the forecast never treats stock compensation as free. Mature chip segment profit still falls to60% and software to74% before unallocated charges. The resulting final consolidated margin lies near the high end of a50–58% range, around Microsoft PBP’s57.75% but on a materially more chip-heavy mix, requiring enduring networking IP and repeated profitable designs. A rival closing the performance gap or buyers demanding lower chip economics would cut these assumptions. [Mature benchmark evidence]
    
    Both drags and offsets matter: software’s shrinking revenue weight lowers aggregate profitability; custom compute has lower gross margins than networking; research, stock pay and supplier costs continue. Against that, the current chip business already demonstrates operating leverage and the charge for old acquisitions expires. Physical capex/depreciation uses the same cohort check as the investment detail; depreciation rises from the603 TTM anchor to5,557, and is already inside the chosen segment margins. These margins require revenue growth and price/mix to fund that extra depreciation, not its omission. A five-year physical life is an analyst midpoint within the disclosed3–10-year equipment range; new buildings have longer lives and are not separately forecast. [Q2 FY2026 call; 10-K FY2025, Note 2; Valuation base evidence]
    
    Observed: the May 3 intangible schedule is FY2026 remainder 3,940; FY2027 6,818; FY2028 5,689; FY2029 4,562; FY2030 3,378; thereafter 3,196, total 27,583. Purchased technology and customer relationships have weighted remaining lives of five and six years; this is not a schedule for hypothetical future acquisitions. [10-Q Q2 FY2026, Note 4]
    
    Analyst interpolation: spread each named fiscal year evenly across its two half-years. Allocate the otherwise undated thereafter bucket to FY2031/FY2032/FY2033 as 1,600/1,000/596, a declining illustrative schedule, not a disclosed fifth rolling-year amount. This gives rolling model-year amortization of 7,349; 6,253.5; 5,125.5; 3,970; 2,489; 1,300; 798; 298; 0; 0, summing exactly to 27,583. The fifth-year assumption can reasonably vary by about 800 either side without changing the remaining total; a revised filing schedule would replace this allocation. The same annual amount is deducted in margin and subtracted in net investment, so changing the timing does not create a duplicate cash add-back; taxes remain a simplified rate on forecast EBIT.
    
    Future engineering creates replacement products within expensed R&D, and all cases keep a physical-equipment/working-capital budget. The model does not declare the business maintenance-free when acquisition charges expire. A new acquisition or material intangible impairment requires rebuilding both sides of this bridge. [Accounting and reinvestment method]
- **Sales-to-capital** — Use the stated organic-growth funding budget, then reduce capital efficiency as the business matures. The annual overrides reconcile acquisition amortization and prevent a slowdown from creating unsupported cash releases. [Valuation base evidence; Mature benchmark evidence] [Valuation base evidence]; [Mature benchmark evidence]

    Observed lagged history uses investment in year t against sales added in t+1, consistent with the selected one-year lag. The GAAP proxy is capex minus physical depreciation, plus a cash-flow proxy for noncash current operating capital, plus net cash acquisitions/disposals, minus acquired amortization. [Valuation base evidence]
    
    | FY investment | GAAP net proxy | Following FY sales increase | Lag-1 result |
    | --- | --- | --- | --- |
    | 2021 | -5,704 | 5,753 | Unusable negative denominator |
    | 2022 | -3,000 | 2,616 | Unusable negative denominator |
    | 2023 | -2,386 | 15,755 | Unusable; VMware revenue appears next year |
    | 2024 | 15,828 cash-only; 77,616 full-consideration illustration | 12,313 | 0.778x cash-only; 0.159x full-consideration illustration |
    | 2025 | -3,431 | Not yet observable | No FY2026 result at cutoff |
    
    The pre-acquired-amortization cash proxy gives 1.925x for FY2022, 18.298x for FY2023 and 0.491x for FY2024; the latter two are acquisition-distorted. The current-capital proxy includes mixed tax/interest lines; including all long-term cash-flow changes would change FY2025 net investment from -3,431 to +187. No one of these is a clean marginal growth-capital estimate. VMware’s stock-funded consideration is not omitted merely because it was absent from cash investing. [Valuation base evidence; 10-K FY2025; 10-K FY2023]
    
    Mature stock sales/book capital is 0.490x Broadcom, 0.963x Cisco, 1.712x Qualcomm and 0.833x Microsoft consolidated. The screen retains goodwill and R&D expense, treats operating leases as rent, and includes Microsoft finance leases; Microsoft PBP and Qualcomm QCT standalone capital are not disclosed. These are accumulated-capital measures, not next-year incremental sales/investment. The forecast ratios may exceed them because no new large goodwill purchase is assumed and current R&D remains fully expensed; there is no claim that past goodwill can be recovered. [Mature benchmark evidence]
    
    Forecast construction, all explicit years: growth-capital budget=max(next-year sales increase,0)/selected ratio. Add a maintenance allowance of 0.5% of current-year sales, then floor this pre-amortization net budget at gross physical capex less physical depreciation. Net investment equals that budget minus this year’s acquired amortization. Ratios are therefore contextual budget parameters; the displayed annual overrides, not an unadjusted ratio, determine final net investment. A contraction does not mechanically release working capital. The lower bear ratio buys more inventory/contract capital per dollar of future sales, while the bull assumes more supplier/customer support.
    
    Physical check: gross capex is an analyst assumption of 1.5% of sales versus 1.0–1.6% in FY2021–FY2025 and TTM 860. Start physical depreciation at TTM 603, retire that legacy run-rate evenly over five years, and depreciate each new annual capex cohort over five years with a half-year convention. Five years lies within the disclosed 3–10-year equipment lives; 15–40-year buildings are a small but unseparated component, so this is a check, not a reported asset rollforward. Future segment margins below include this depreciation burden. The rest of the budget is working capital, contract assets and supply-chain funding, not capitalized R&D or the separately unvalued customer-lease guarantee. [10-K FY2025, Note 2; Valuation base evidence]
    
    The ordinary investment range is uncertain: sustained net pre-amortization funding around 30–70% of the following sales increment is defensible for these cases against the FY2025 current-capital use of 4,882 and next-year uncertainty; exact ratios are not empirically estimable from acquisition-distorted history. The 128,110 purchase commitments and 164,600 committed contracts support budgeting material funding, but neither is automatically debt nor all cash paid at once. Payment terms, contract-asset disclosures and inventories growing persistently faster than shipments would change these choices. [10-Q Q2 FY2026, Notes 2 and 10]
    
    Case placement: Early2.5–3.5x and late1.8–2.5x;3.0/2.2 assumes better payment support and supply utilization, but less efficiency after the initial ramp.
    
    
    Broad industry context, kept distinct from the matched peer screen: the January5,2026 Damodaran capex dataset reports LTM sales/invested capital1.2067x for66 US Semiconductor firms and1.5382x for309 Software (System & Application) firms. These are broad aggregated stock ratios, not distributions, marginal growth yields or an AVGO-only rent/GAAP reconciliation; the dataset also reports net R&D within its investment measures. The forecast’s higher organic-growth budget ratio depends on expensing current research and avoiding another large goodwill acquisition, and its annual overrides then subtract acquired amortization consistently. The like-basis company comparisons above therefore carry more weight; do not multiply these aggregated ratios by an unrelated margin and call it observed industry ROIC. [Damodaran capital data]
- **Reinvestment override** — Use the explicit net-investment schedule so retained acquisition amortization is reversed exactly once while real equipment and operating funding are paid for. Management has given no capex target to substitute for this analyst budget. [Valuation base evidence; Q2 FY2026 call] [Valuation base evidence]; [Q2 FY2026 call]

    Observed lagged history uses investment in year t against sales added in t+1, consistent with the selected one-year lag. The GAAP proxy is capex minus physical depreciation, plus a cash-flow proxy for noncash current operating capital, plus net cash acquisitions/disposals, minus acquired amortization. [Valuation base evidence]
    
    | FY investment | GAAP net proxy | Following FY sales increase | Lag-1 result |
    | --- | --- | --- | --- |
    | 2021 | -5,704 | 5,753 | Unusable negative denominator |
    | 2022 | -3,000 | 2,616 | Unusable negative denominator |
    | 2023 | -2,386 | 15,755 | Unusable; VMware revenue appears next year |
    | 2024 | 15,828 cash-only; 77,616 full-consideration illustration | 12,313 | 0.778x cash-only; 0.159x full-consideration illustration |
    | 2025 | -3,431 | Not yet observable | No FY2026 result at cutoff |
    
    The pre-acquired-amortization cash proxy gives 1.925x for FY2022, 18.298x for FY2023 and 0.491x for FY2024; the latter two are acquisition-distorted. The current-capital proxy includes mixed tax/interest lines; including all long-term cash-flow changes would change FY2025 net investment from -3,431 to +187. No one of these is a clean marginal growth-capital estimate. VMware’s stock-funded consideration is not omitted merely because it was absent from cash investing. [Valuation base evidence; 10-K FY2025; 10-K FY2023]
    
    Mature stock sales/book capital is 0.490x Broadcom, 0.963x Cisco, 1.712x Qualcomm and 0.833x Microsoft consolidated. The screen retains goodwill and R&D expense, treats operating leases as rent, and includes Microsoft finance leases; Microsoft PBP and Qualcomm QCT standalone capital are not disclosed. These are accumulated-capital measures, not next-year incremental sales/investment. The forecast ratios may exceed them because no new large goodwill purchase is assumed and current R&D remains fully expensed; there is no claim that past goodwill can be recovered. [Mature benchmark evidence]
    
    Forecast construction, all explicit years: growth-capital budget=max(next-year sales increase,0)/selected ratio. Add a maintenance allowance of 0.5% of current-year sales, then floor this pre-amortization net budget at gross physical capex less physical depreciation. Net investment equals that budget minus this year’s acquired amortization. Ratios are therefore contextual budget parameters; the displayed annual overrides, not an unadjusted ratio, determine final net investment. A contraction does not mechanically release working capital. The lower bear ratio buys more inventory/contract capital per dollar of future sales, while the bull assumes more supplier/customer support.
    
    Physical check: gross capex is an analyst assumption of 1.5% of sales versus 1.0–1.6% in FY2021–FY2025 and TTM 860. Start physical depreciation at TTM 603, retire that legacy run-rate evenly over five years, and depreciate each new annual capex cohort over five years with a half-year convention. Five years lies within the disclosed 3–10-year equipment lives; 15–40-year buildings are a small but unseparated component, so this is a check, not a reported asset rollforward. Future segment margins below include this depreciation burden. The rest of the budget is working capital, contract assets and supply-chain funding, not capitalized R&D or the separately unvalued customer-lease guarantee. [10-K FY2025, Note 2; Valuation base evidence]
    
    The ordinary investment range is uncertain: sustained net pre-amortization funding around 30–70% of the following sales increment is defensible for these cases against the FY2025 current-capital use of 4,882 and next-year uncertainty; exact ratios are not empirically estimable from acquisition-distorted history. The 128,110 purchase commitments and 164,600 committed contracts support budgeting material funding, but neither is automatically debt nor all cash paid at once. Payment terms, contract-asset disclosures and inventories growing persistently faster than shipments would change these choices. [10-Q Q2 FY2026, Notes 2 and 10]
    
    | Year | Next sales increase | Budget before acquired amortization | Gross physical capex | Physical depreciation | Implied other net capital | Acquired amortization subtracted | Net investment override |
    | --- | --- | --- | --- | --- | --- | --- | --- |
    | 1 | 56,500.0 | 19,528.3 | 2,085.0 | 751.2 | 18,194.5 | 7,349.0 | 12,179.333 |
    | 2 | 46,500.0 | 16,477.5 | 2,932.5 | 1,132.3 | 14,677.4 | 6,253.5 | 10,224.000 |
    | 3 | 41,500.0 | 15,043.3 | 3,630.0 | 1,668.0 | 13,081.3 | 5,125.5 | 9,917.833 |
    | 4 | 30,200.0 | 11,484.2 | 4,252.5 | 2,335.7 | 9,567.3 | 3,970.0 | 7,514.167 |
    | 5 | 26,500.0 | 10,401.8 | 4,705.5 | 3,110.9 | 8,807.2 | 2,489.0 | 7,912.833 |
    | 6 | 23,900.0 | 12,564.6 | 5,103.0 | 3,822.9 | 11,284.5 | 1,300.0 | 11,264.636 |
    | 7 | 19,300.0 | 10,593.2 | 5,461.5 | 4,377.6 | 9,509.3 | 798.0 | 9,795.227 |
    | 8 | 16,700.0 | 9,507.9 | 5,751.0 | 4,842.6 | 8,599.5 | 298.0 | 9,209.909 |
    | 9 | 15,500.0 | 9,046.0 | 6,001.5 | 5,229.6 | 8,274.1 | 0.0 | 9,045.955 |
    | 10 | 12,468.0 | 7,745.3 | 6,234.0 | 5,557.4 | 7,068.6 | 0.0 | 7,745.273 |
    
    Negative net investment where it appears reflects the noncash amortization reversal; it does not assume selling goodwill or recovering inventory at book value. Physical capex is positive in every year. These overrides cover all ten years and supersede the displayed ratio mechanically; the terminal year separately uses growth/terminal return, so the transition requires review rather than automatically extending an unusually light capital budget.
    
    
    Broad industry context, kept distinct from the matched peer screen: the January5,2026 Damodaran capex dataset reports LTM sales/invested capital1.2067x for66 US Semiconductor firms and1.5382x for309 Software (System & Application) firms. These are broad aggregated stock ratios, not distributions, marginal growth yields or an AVGO-only rent/GAAP reconciliation; the dataset also reports net R&D within its investment measures. The forecast’s higher organic-growth budget ratio depends on expensing current research and avoiding another large goodwill acquisition, and its annual overrides then subtract acquired amortization consistently. The like-basis company comparisons above therefore carry more weight; do not multiply these aggregated ratios by an unrelated margin and call it observed industry ROIC. [Damodaran capital data]
- **Tax rate** — Normalize taxes above the reported benefit-heavy rate while allowing for foreign earnings, then reach the house mature rate. The early rate averages the transition rather than treating one quarter’s non-GAAP guidance as permanent. [10-K FY2025; Q2 FY2026 call] [10-K FY2025]; [Q2 FY2026 call]

    Observed TTM GAAP rate3.8125%; H1 FY2026 9.0914%; management guides approximately16% non-GAAP for Q3/FY2026. Singapore incentives expire through2030, Malaysia inFY2028, and minimum taxes already raise the burden. Those definitions differ from operating cash tax. A rounded20% early rate is an analyst normalization within18–23%, balancing geographic incentives against their expiry and the unreliable tax benefits;25% mature is the house marginal-tax assumption within a22–27% operating range. [10-K FY2025, Note12; 10-Q Q2 FY2026, Note8; Q2 FY2026 call]
    
    The engine holds20% in years1–5 and linearly fades21/22/23/24/25% in years6–10. This cannot reproduce the exact expiry years or an explicit tax-loss/credit ledger;20% early is a period-average approximation, so near-term tax can be overstated and midperiod tax understated. No immediate loss tax benefit is required in these profitable cases. The1,662 old uncertain-tax claim is separately deducted and excluded from normal future earnings taxes. A durable reported cash-tax reconciliation, enacted rate change or loss of incentives would change this choice.
- **Terminal growth** — Long-run nominal growth slows below the dollar risk-free ceiling as a much larger business follows replacement demand and modest market expansion. This is an analyst mature-state assumption. [Analyst judgment]

    Chosen growth3.0% lies within a1–3% bear or2–4% central/upside mature dollar range, not the temporary27% WSTS2027 logic growth. The final explicit growth3.87% transitions to this rate; no endless AI ramp is assumed. A materially shrinking installed base would justify zero or negative growth. [WSTS spring 2026]
- **Terminal return on capital premium** — The mature return is chosen from Broadcom’s normalized history and the peer range, with continued research and renewals needed to sustain it. Its premium exceeds a house warning threshold and is retained for that business reason, not to clear a diagnostic. [Mature benchmark evidence] [Mature benchmark evidence]

    Selected independently before diagnostics: 22% mature return in the bull. The current terminal WACC is4.94% dollar risk-free plus4.5% mature ERP=9.44%; premium=12.5600%; implied reinvestment fraction=3.0%/22.00%=13.64% of after-tax operating profit. Terminal GAAP margin holds at the final row above; growth is3.0%. [Market inputs; Analyst judgment]
    
    Comparable mature historical returns on opening book capital at a uniform analytical21% tax: Broadcom15.99% GAAP or21.05% before acquired amortization; Cisco15.86% or18.78%; Qualcomm35.35% or36.27%; Microsoft consolidated37.37% or39.11%. These figures retain goodwill, expense R&D and treat ordinary leases as rent; Qualcomm has royalties and Microsoft has cloud finance leases, while PBP standalone capital is undisclosed. None is a marginal project return. [Mature benchmark evidence]
    
    A20–25% mature return range puts the bull above the closest own-company/Cisco outcomes, but below research-light book returns at Qualcomm/Microsoft. Repeated design wins, networking leadership and software renewal costs—not a contract ending in2031—must sustain the premium. The22% choice assumes strong continuing research and buyers retaining less of the design surplus; competitors closing the technology lead or customer-owned designs would remove it.
    
    Average return on the accumulated forecast book-capital balance can exceed this selected marginal return because R&D remains an expense, past acquired capital amortizes, and the explicit expansion uses existing technology. That difference is not permission to raise terminal returns. The runner/reviewer must compare final operating cash flow and book return with the terminal-year reinvestment requirement through restricted diagnostics, investigate the whole margin/capital/tax bridge and retain any economically supported discontinuity visibly. If the capital budget is insufficient on its own evidence, revise the budget rather than tune this premium to a warning threshold. [Business-drivers method]

### Management: reasons

- **Computable: yes** — Management supplied multi-year AI revenue targets, so a management operating case is conceptually available; shared unresolved bridge claims still prevent a completed valuation. [Q2 FY2026 call]
- **Revenue growth** — The first forward year blends the recorded fiscal AI target with a disclosed-floor interpretation of the following year’s target, using an explicit timing assumption. Later periods and businesses without annual guidance use labelled analyst completion rather than turning qualitative optimism into guidance. [Q2 FY2026 call] [10-Q Q2 FY2026]; [Q2 FY2026 release]; [Q2 FY2026 call]; [WSTS spring 2026]

    Observed starting point: TTM semiconductor47,762 and software27,703 sum to75,465. Q2 revenue22,187 grew47.87% from15,004; Q2 semiconductor15,009 versus8,408 grew78.50%, while software7,178 versus6,596 grew8.82%. The release’s next-quarter revenue29,400 and AI16,000 imply substantial acceleration; the first model year is May2026–May2027, not FY2026. [10-Q Q2 FY2026, Note 9; Q2 FY2026 release]
    
    Recorded wording gives AI revenue of 56,000 in FY2026 and “in excess of” 100,000 in FY2027. The 100,000 figure is a conservative boundary of an open-ended target, not its midpoint or exact promise. H1 FY2026 reported AI is 8,400+10,800=19,200, so the fiscal target implies H2 36,800. Assume 40% of the 100,000 FY2027 floor arrives in H1, consistent with the back-half-loaded wording; model year one is therefore 36,800+40,000=76,800. At a 35–45% H1 fraction the same arithmetic gives 71,800–81,800. [Q2 FY2026 call; Q1 FY2026 release; Q2 FY2026 release]
    
    For model year two, FY2027 H2 is 60,000; an analyst completion assumes 25% fiscal AI growth in FY2028 and the same 40% first-half share, giving FY2028 H1 50,000 and total 110,000. The qualitative “substantial growth” statement is only recorded in guidance, not converted into that 25%; this is the independently chosen central AI growth assumption. Thereafter use the base AI growth rates from year two onward, applied to 110,000, with amounts rounded to the nearest 100. Software starts at 34,500, slightly below four times the 8,900 next-quarter guide, then follows central fading growth; older chips equal the base case. No annual total-company revenue guidance exists. Every year extends from May to May, roughly six months away from the fiscal-year labels; quarterly conversion remains a material approximation. [Q2 FY2026 call]
    
    The first-year timing range above is not a management range. A change to the published fiscal target or its back-half timing changes the mapped path; exact year-two-and-later numbers should be replaced when management gives actual annual targets.
    
    Annual build in USD millions; AI/other-chip splits after the disclosed starting segment are analyst judgments, not audited subsegments:
    
    | Model year, ends about May | AI judgment | Other chips judgment | Semiconductor total | Software judgment | Company total | Growth |
    | --- | --- | --- | --- | --- | --- | --- |
    | 1 / 2027 | 76,800 | 17,800 | 94,600 | 34,500 | 129,100 | 71.0727% |
    | 2 / 2028 | 110,000 | 18,700 | 128,700 | 37,600 | 166,300 | 28.8149% |
    | 3 / 2029 | 137,500 | 19,500 | 157,000 | 40,700 | 197,700 | 18.8815% |
    | 4 / 2030 | 159,500 | 20,200 | 179,700 | 43,400 | 223,100 | 12.8477% |
    | 5 / 2031 | 176,000 | 20,800 | 196,800 | 45,500 | 242,300 | 8.6060% |
    | 6 / 2032 | 190,300 | 21,400 | 211,700 | 47,200 | 258,900 | 6.8510% |
    | 7 / 2033 | 202,400 | 21,900 | 224,300 | 48,700 | 273,000 | 5.4461% |
    | 8 / 2034 | 213,400 | 22,300 | 235,700 | 50,000 | 285,700 | 4.6520% |
    | 9 / 2035 | 222,200 | 22,600 | 244,800 | 51,000 | 295,800 | 3.5352% |
    | 10 / 2036 | 229,900 | 22,800 | 252,700 | 52,000 | 304,700 | 3.0088% |
    
    Every segment sum is exact; growth ratios are stored to10 decimals solely to reproduce the rounded revenue totals, with less than0.01 of cumulative rounding. Years6–10 are explicit because customer bargaining and the maturing product mix need a slower cost/growth path than holding year-five margins constant. No undisclosed chip quantity, price per gigawatt, new backlog or platform financing is added to sales.
    
    Year-five revenue242,300; final-year revenue304,700, with semiconductor82.9% and software17.1%. Against the broad2036 non-memory ceiling1,438,757, chips would be17.6%; AI alone would be26.0% of a similarly extrapolated logic ceiling883,293. This large-share requirement is a plausibility test, not demonstrated market access. WSTS only forecasts through2027;6% subsequent growth is an analyst assumption, and3–9% alternatives materially change the denominator. [WSTS spring 2026]
    
    Software ends at52,000, compared with Microsoft PBP’s observed FY2025 revenue120,810 and13.10% growth, and Cisco’s total56,654 with5.30% growth including more Splunk. Those broader businesses establish an order of magnitude and mature growth outcomes; they do not prove VMware’s addressable market. The proposed software path requires retention through successive renewals and slows to1.96% in year10. [Mature benchmark evidence; MSFT FY2025 10-K; CSCO FY2025 10-K]
    
    
    Current AI-chip leader scale check: NVIDIA reported FY2026 revenue215,938 and Q1FY2027 revenue81,615 against44,062 a year earlier; reconstructed TTM=215,938+81,615-44,062=253,491. Its latest-quarter Data Center revenue is75,200. These releases were published February25 and May20,2026, before the cutoff. This case’s final Broadcom consolidated revenue304,700 is1.20 times that observed NVIDIA TTM; final semiconductor revenue252,700 is1.00 times it. This is a present-scale comparison against a rapidly growing leader, not a forecast that NVIDIA stops growing or a claim of mature margins/market size. NVIDIA sells compute platforms, networking and systems alongside chips; Broadcom’s call describes its revenue as chips, so supply-chain scope differs. No future share is inferred from this ratio. [NVDA FY2026 release; NVDA Q1 FY2027 release; Q2 FY2026 call]
- **Operating margin** — The margin bridge keeps stock pay and research as costs while acquisition charges expire; scale helps initially, then competition and a smaller software share offset it. Each segment is modeled before reconciling back to GAAP, as business.md §3 requires. [10-Q Q2 FY2026; Mature benchmark evidence] [10-Q Q2 FY2026]; [10-K FY2025]; [Mature benchmark evidence]

    Observed: TTM GAAP margin43.3923%; current-quarter48.6231%. Q2 segment margins are9,281/15,009=61.8362% chips and5,647/7,178=78.6709% software, but exclude SBC2,092, acquired amortization1,967 and restructuring81. The combined segment margin is not GAAP; subtract all excluded costs once. [10-Q Q2 FY2026, Notes 4,7,9]
    
    Analyst arithmetic: GAAP EBIT = semiconductor sales×chip segment margin + software sales×software segment margin - forecast SBC -0.5% of sales for ongoing restructuring/acquisition overhead - disclosed/interpolated acquired amortization. Segment margins retain ordinary R&D, ordinary selling costs, rent and physical depreciation; no additional R&D add-back is made. Future SBC stays above the current TTM dollar expense even where its share of sales falls; the downside permits dollar costs to decline after the initial ramp. Every row below is a future judgment except the sourced amortization schedule’s disclosed fiscal buckets.
    
    | Year | Chip segment margin | Software segment margin | SBC / sales | Other costs / sales | Acquired amortization | GAAP margin | Physical depreciation check |
    | --- | --- | --- | --- | --- | --- | --- | --- |
    | 1 | 64.0% | 79.0% | 9.0% | 0.5% | 7,349.0 | 52.816% | 736.4 |
    | 2 | 65.0% | 79.0% | 8.5% | 0.5% | 6,253.5 | 55.405% | 1,058.8 |
    | 3 | 64.0% | 78.0% | 8.0% | 0.5% | 5,125.5 | 55.790% | 1,484.2 |
    | 4 | 62.0% | 77.0% | 7.8% | 0.5% | 3,970.0 | 54.839% | 1,994.9 |
    | 5 | 60.0% | 76.0% | 7.5% | 0.5% | 2,489.0 | 53.977% | 2,572.4 |
    | 6 | 59.0% | 75.0% | 7.3% | 0.5% | 1,300.0 | 53.615% | 3,070.2 |
    | 7 | 58.0% | 74.0% | 7.1% | 0.5% | 798.0 | 52.962% | 3,425.0 |
    | 8 | 57.0% | 73.0% | 7.0% | 0.5% | 298.0 | 52.196% | 3,717.0 |
    | 9 | 56.0% | 72.0% | 7.0% | 0.5% | 0.0 | 51.259% | 3,958.1 |
    | 10 | 55.0% | 71.0% | 7.0% | 0.5% | 0.0 | 50.231% | 4,160.7 |
    
    The initial chip scale benefit raises segment profit modestly above the latest61.84%, then competition reduces it to55%; software falls from about78.67% to71% before unallocated charges. The final consolidated GAAP margin belongs in an approximate45–53% range: above Qualcomm/Cisco, near Broadcom’s52.51% FY2025 before-acquired-amortization sensitivity, and below Microsoft PBP’s57.75%. Those comparisons retain R&D/SBC except where the segment definitions explicitly exclude them. This premium needs differentiated IP and recurring software; a sustained fall in chip gross margin or renewal economics would move it lower. [Mature benchmark evidence]
    
    Both drags and offsets matter: software’s shrinking revenue weight lowers aggregate profitability; custom compute has lower gross margins than networking; research, stock pay and supplier costs continue. Against that, the current chip business already demonstrates operating leverage and the charge for old acquisitions expires. Physical capex/depreciation uses the same cohort check as the investment detail; depreciation rises from the603 TTM anchor to4,161, and is already inside the chosen segment margins. These margins require revenue growth and price/mix to fund that extra depreciation, not its omission. A five-year physical life is an analyst midpoint within the disclosed3–10-year equipment range; new buildings have longer lives and are not separately forecast. [Q2 FY2026 call; 10-K FY2025, Note 2; Valuation base evidence]
    
    Observed: the May 3 intangible schedule is FY2026 remainder 3,940; FY2027 6,818; FY2028 5,689; FY2029 4,562; FY2030 3,378; thereafter 3,196, total 27,583. Purchased technology and customer relationships have weighted remaining lives of five and six years; this is not a schedule for hypothetical future acquisitions. [10-Q Q2 FY2026, Note 4]
    
    Analyst interpolation: spread each named fiscal year evenly across its two half-years. Allocate the otherwise undated thereafter bucket to FY2031/FY2032/FY2033 as 1,600/1,000/596, a declining illustrative schedule, not a disclosed fifth rolling-year amount. This gives rolling model-year amortization of 7,349; 6,253.5; 5,125.5; 3,970; 2,489; 1,300; 798; 298; 0; 0, summing exactly to 27,583. The fifth-year assumption can reasonably vary by about 800 either side without changing the remaining total; a revised filing schedule would replace this allocation. The same annual amount is deducted in margin and subtracted in net investment, so changing the timing does not create a duplicate cash add-back; taxes remain a simplified rate on forecast EBIT.
    
    Future engineering creates replacement products within expensed R&D, and all cases keep a physical-equipment/working-capital budget. The model does not declare the business maintenance-free when acquisition charges expire. A new acquisition or material intangible impairment requires rebuilding both sides of this bridge. [Accounting and reinvestment method]
- **Sales-to-capital** — Use the stated organic-growth funding budget, then reduce capital efficiency as the business matures. The annual overrides reconcile acquisition amortization and prevent a slowdown from creating unsupported cash releases. [Valuation base evidence; Mature benchmark evidence] [Valuation base evidence]; [Mature benchmark evidence]

    Observed lagged history uses investment in year t against sales added in t+1, consistent with the selected one-year lag. The GAAP proxy is capex minus physical depreciation, plus a cash-flow proxy for noncash current operating capital, plus net cash acquisitions/disposals, minus acquired amortization. [Valuation base evidence]
    
    | FY investment | GAAP net proxy | Following FY sales increase | Lag-1 result |
    | --- | --- | --- | --- |
    | 2021 | -5,704 | 5,753 | Unusable negative denominator |
    | 2022 | -3,000 | 2,616 | Unusable negative denominator |
    | 2023 | -2,386 | 15,755 | Unusable; VMware revenue appears next year |
    | 2024 | 15,828 cash-only; 77,616 full-consideration illustration | 12,313 | 0.778x cash-only; 0.159x full-consideration illustration |
    | 2025 | -3,431 | Not yet observable | No FY2026 result at cutoff |
    
    The pre-acquired-amortization cash proxy gives 1.925x for FY2022, 18.298x for FY2023 and 0.491x for FY2024; the latter two are acquisition-distorted. The current-capital proxy includes mixed tax/interest lines; including all long-term cash-flow changes would change FY2025 net investment from -3,431 to +187. No one of these is a clean marginal growth-capital estimate. VMware’s stock-funded consideration is not omitted merely because it was absent from cash investing. [Valuation base evidence; 10-K FY2025; 10-K FY2023]
    
    Mature stock sales/book capital is 0.490x Broadcom, 0.963x Cisco, 1.712x Qualcomm and 0.833x Microsoft consolidated. The screen retains goodwill and R&D expense, treats operating leases as rent, and includes Microsoft finance leases; Microsoft PBP and Qualcomm QCT standalone capital are not disclosed. These are accumulated-capital measures, not next-year incremental sales/investment. The forecast ratios may exceed them because no new large goodwill purchase is assumed and current R&D remains fully expensed; there is no claim that past goodwill can be recovered. [Mature benchmark evidence]
    
    Forecast construction, all explicit years: growth-capital budget=max(next-year sales increase,0)/selected ratio. Add a maintenance allowance of 0.5% of current-year sales, then floor this pre-amortization net budget at gross physical capex less physical depreciation. Net investment equals that budget minus this year’s acquired amortization. Ratios are therefore contextual budget parameters; the displayed annual overrides, not an unadjusted ratio, determine final net investment. A contraction does not mechanically release working capital. The lower bear ratio buys more inventory/contract capital per dollar of future sales, while the bull assumes more supplier/customer support.
    
    Physical check: gross capex is an analyst assumption of 1.5% of sales versus 1.0–1.6% in FY2021–FY2025 and TTM 860. Start physical depreciation at TTM 603, retire that legacy run-rate evenly over five years, and depreciate each new annual capex cohort over five years with a half-year convention. Five years lies within the disclosed 3–10-year equipment lives; 15–40-year buildings are a small but unseparated component, so this is a check, not a reported asset rollforward. Future segment margins below include this depreciation burden. The rest of the budget is working capital, contract assets and supply-chain funding, not capitalized R&D or the separately unvalued customer-lease guarantee. [10-K FY2025, Note 2; Valuation base evidence]
    
    The ordinary investment range is uncertain: sustained net pre-amortization funding around 30–70% of the following sales increment is defensible for these cases against the FY2025 current-capital use of 4,882 and next-year uncertainty; exact ratios are not empirically estimable from acquisition-distorted history. The 128,110 purchase commitments and 164,600 committed contracts support budgeting material funding, but neither is automatically debt nor all cash paid at once. Payment terms, contract-asset disclosures and inventories growing persistently faster than shipments would change these choices. [10-Q Q2 FY2026, Notes 2 and 10]
    
    Case placement: Use the central early2.5x/late2.0x budget and its2.0–3.0x/1.5–2.5x working ranges; management gave no numerical investment target.
    
    
    Broad industry context, kept distinct from the matched peer screen: the January5,2026 Damodaran capex dataset reports LTM sales/invested capital1.2067x for66 US Semiconductor firms and1.5382x for309 Software (System & Application) firms. These are broad aggregated stock ratios, not distributions, marginal growth yields or an AVGO-only rent/GAAP reconciliation; the dataset also reports net R&D within its investment measures. The forecast’s higher organic-growth budget ratio depends on expensing current research and avoiding another large goodwill acquisition, and its annual overrides then subtract acquired amortization consistently. The like-basis company comparisons above therefore carry more weight; do not multiply these aggregated ratios by an unrelated margin and call it observed industry ROIC. [Damodaran capital data]
- **Reinvestment override** — Use the explicit net-investment schedule so retained acquisition amortization is reversed exactly once while real equipment and operating funding are paid for. Management has given no capex target to substitute for this analyst budget. [Valuation base evidence; Q2 FY2026 call] [Valuation base evidence]; [Q2 FY2026 call]

    Observed lagged history uses investment in year t against sales added in t+1, consistent with the selected one-year lag. The GAAP proxy is capex minus physical depreciation, plus a cash-flow proxy for noncash current operating capital, plus net cash acquisitions/disposals, minus acquired amortization. [Valuation base evidence]
    
    | FY investment | GAAP net proxy | Following FY sales increase | Lag-1 result |
    | --- | --- | --- | --- |
    | 2021 | -5,704 | 5,753 | Unusable negative denominator |
    | 2022 | -3,000 | 2,616 | Unusable negative denominator |
    | 2023 | -2,386 | 15,755 | Unusable; VMware revenue appears next year |
    | 2024 | 15,828 cash-only; 77,616 full-consideration illustration | 12,313 | 0.778x cash-only; 0.159x full-consideration illustration |
    | 2025 | -3,431 | Not yet observable | No FY2026 result at cutoff |
    
    The pre-acquired-amortization cash proxy gives 1.925x for FY2022, 18.298x for FY2023 and 0.491x for FY2024; the latter two are acquisition-distorted. The current-capital proxy includes mixed tax/interest lines; including all long-term cash-flow changes would change FY2025 net investment from -3,431 to +187. No one of these is a clean marginal growth-capital estimate. VMware’s stock-funded consideration is not omitted merely because it was absent from cash investing. [Valuation base evidence; 10-K FY2025; 10-K FY2023]
    
    Mature stock sales/book capital is 0.490x Broadcom, 0.963x Cisco, 1.712x Qualcomm and 0.833x Microsoft consolidated. The screen retains goodwill and R&D expense, treats operating leases as rent, and includes Microsoft finance leases; Microsoft PBP and Qualcomm QCT standalone capital are not disclosed. These are accumulated-capital measures, not next-year incremental sales/investment. The forecast ratios may exceed them because no new large goodwill purchase is assumed and current R&D remains fully expensed; there is no claim that past goodwill can be recovered. [Mature benchmark evidence]
    
    Forecast construction, all explicit years: growth-capital budget=max(next-year sales increase,0)/selected ratio. Add a maintenance allowance of 0.5% of current-year sales, then floor this pre-amortization net budget at gross physical capex less physical depreciation. Net investment equals that budget minus this year’s acquired amortization. Ratios are therefore contextual budget parameters; the displayed annual overrides, not an unadjusted ratio, determine final net investment. A contraction does not mechanically release working capital. The lower bear ratio buys more inventory/contract capital per dollar of future sales, while the bull assumes more supplier/customer support.
    
    Physical check: gross capex is an analyst assumption of 1.5% of sales versus 1.0–1.6% in FY2021–FY2025 and TTM 860. Start physical depreciation at TTM 603, retire that legacy run-rate evenly over five years, and depreciate each new annual capex cohort over five years with a half-year convention. Five years lies within the disclosed 3–10-year equipment lives; 15–40-year buildings are a small but unseparated component, so this is a check, not a reported asset rollforward. Future segment margins below include this depreciation burden. The rest of the budget is working capital, contract assets and supply-chain funding, not capitalized R&D or the separately unvalued customer-lease guarantee. [10-K FY2025, Note 2; Valuation base evidence]
    
    The ordinary investment range is uncertain: sustained net pre-amortization funding around 30–70% of the following sales increment is defensible for these cases against the FY2025 current-capital use of 4,882 and next-year uncertainty; exact ratios are not empirically estimable from acquisition-distorted history. The 128,110 purchase commitments and 164,600 committed contracts support budgeting material funding, but neither is automatically debt nor all cash paid at once. Payment terms, contract-asset disclosures and inventories growing persistently faster than shipments would change these choices. [10-Q Q2 FY2026, Notes 2 and 10]
    
    | Year | Next sales increase | Budget before acquired amortization | Gross physical capex | Physical depreciation | Implied other net capital | Acquired amortization subtracted | Net investment override |
    | --- | --- | --- | --- | --- | --- | --- | --- |
    | 1 | 37,200.0 | 15,525.5 | 1,936.5 | 736.4 | 14,325.4 | 7,349.0 | 8,176.500 |
    | 2 | 31,400.0 | 13,391.5 | 2,494.5 | 1,058.8 | 11,955.9 | 6,253.5 | 7,138.000 |
    | 3 | 25,400.0 | 11,148.5 | 2,965.5 | 1,484.2 | 9,667.2 | 5,125.5 | 6,023.000 |
    | 4 | 19,200.0 | 8,795.5 | 3,346.5 | 1,994.9 | 7,443.9 | 3,970.0 | 4,825.500 |
    | 5 | 16,600.0 | 7,851.5 | 3,634.5 | 2,572.4 | 6,789.4 | 2,489.0 | 5,362.500 |
    | 6 | 14,100.0 | 8,344.5 | 3,883.5 | 3,070.2 | 7,531.2 | 1,300.0 | 7,044.500 |
    | 7 | 12,700.0 | 7,715.0 | 4,095.0 | 3,425.0 | 7,045.0 | 798.0 | 6,917.000 |
    | 8 | 10,100.0 | 6,478.5 | 4,285.5 | 3,717.0 | 5,910.0 | 298.0 | 6,180.500 |
    | 9 | 8,900.0 | 5,929.0 | 4,437.0 | 3,958.1 | 5,450.1 | 0.0 | 5,929.000 |
    | 10 | 9,141.0 | 6,094.0 | 4,570.5 | 4,160.7 | 5,684.2 | 0.0 | 6,094.000 |
    
    Negative net investment where it appears reflects the noncash amortization reversal; it does not assume selling goodwill or recovering inventory at book value. Physical capex is positive in every year. These overrides cover all ten years and supersede the displayed ratio mechanically; the terminal year separately uses growth/terminal return, so the transition requires review rather than automatically extending an unusually light capital budget.
    
    
    Broad industry context, kept distinct from the matched peer screen: the January5,2026 Damodaran capex dataset reports LTM sales/invested capital1.2067x for66 US Semiconductor firms and1.5382x for309 Software (System & Application) firms. These are broad aggregated stock ratios, not distributions, marginal growth yields or an AVGO-only rent/GAAP reconciliation; the dataset also reports net R&D within its investment measures. The forecast’s higher organic-growth budget ratio depends on expensing current research and avoiding another large goodwill acquisition, and its annual overrides then subtract acquired amortization consistently. The like-basis company comparisons above therefore carry more weight; do not multiply these aggregated ratios by an unrelated margin and call it observed industry ROIC. [Damodaran capital data]
- **Tax rate** — Normalize taxes above the reported benefit-heavy rate while allowing for foreign earnings, then reach the house mature rate. The early rate averages the transition rather than treating one quarter’s non-GAAP guidance as permanent. [10-K FY2025; Q2 FY2026 call] [10-K FY2025]; [Q2 FY2026 call]

    Observed TTM GAAP rate3.8125%; H1 FY2026 9.0914%; management guides approximately16% non-GAAP for Q3/FY2026. Singapore incentives expire through2030, Malaysia inFY2028, and minimum taxes already raise the burden. Those definitions differ from operating cash tax. A rounded20% early rate is an analyst normalization within18–23%, balancing geographic incentives against their expiry and the unreliable tax benefits;25% mature is the house marginal-tax assumption within a22–27% operating range. [10-K FY2025, Note12; 10-Q Q2 FY2026, Note8; Q2 FY2026 call]
    
    The engine holds20% in years1–5 and linearly fades21/22/23/24/25% in years6–10. This cannot reproduce the exact expiry years or an explicit tax-loss/credit ledger;20% early is a period-average approximation, so near-term tax can be overstated and midperiod tax understated. No immediate loss tax benefit is required in these profitable cases. The1,662 old uncertain-tax claim is separately deducted and excluded from normal future earnings taxes. A durable reported cash-tax reconciliation, enacted rate change or loss of incentives would change this choice.
- **Terminal growth** — Long-run nominal growth slows below the dollar risk-free ceiling as a much larger business follows replacement demand and modest market expansion. This is an analyst mature-state assumption. [Analyst judgment]

    Chosen growth3.0% lies within a1–3% bear or2–4% central/upside mature dollar range, not the temporary27% WSTS2027 logic growth. The final explicit growth3.01% transitions to this rate; no endless AI ramp is assumed. A materially shrinking installed base would justify zero or negative growth. [WSTS spring 2026]
- **Terminal return on capital premium** — The mature return is chosen from Broadcom’s normalized history and the peer range, with continued research and renewals needed to sustain it. Its premium exceeds a house warning threshold and is retained for that business reason, not to clear a diagnostic. [Mature benchmark evidence] [Mature benchmark evidence]

    Selected independently before diagnostics: 18% mature return in the central/management case. The current terminal WACC is4.94% dollar risk-free plus4.5% mature ERP=9.44%; premium=8.5600%; implied reinvestment fraction=3.0%/18.00%=16.67% of after-tax operating profit. Terminal GAAP margin holds at the final row above; growth is3.0%. [Market inputs; Analyst judgment]
    
    Comparable mature historical returns on opening book capital at a uniform analytical21% tax: Broadcom15.99% GAAP or21.05% before acquired amortization; Cisco15.86% or18.78%; Qualcomm35.35% or36.27%; Microsoft consolidated37.37% or39.11%. These figures retain goodwill, expense R&D and treat ordinary leases as rent; Qualcomm has royalties and Microsoft has cloud finance leases, while PBP standalone capital is undisclosed. None is a marginal project return. [Mature benchmark evidence]
    
    A15–20% mature return range has the closest direct support from Broadcom and Cisco;18% is central within that interval. Networking IP, repeated co-design and software migration costs must persist beyond the current contracts despite stronger buyers. Competitors and customers cannot capture all of those engineering and switching benefits in this case; sustained customer self-design or failed renewals would reduce the premium.
    
    Average return on the accumulated forecast book-capital balance can exceed this selected marginal return because R&D remains an expense, past acquired capital amortizes, and the explicit expansion uses existing technology. That difference is not permission to raise terminal returns. The runner/reviewer must compare final operating cash flow and book return with the terminal-year reinvestment requirement through restricted diagnostics, investigate the whole margin/capital/tax bridge and retain any economically supported discontinuity visibly. If the capital budget is insufficient on its own evidence, revise the budget rather than tune this premium to a warning threshold. [Business-drivers method]

## 3. Base year (Q3 FY2025–Q2 FY2026, TTM ended May 3, 2026; model year 1 ends around May 2027)

| Item | USD millions | Reason | Source |
|---|---|---|---|
| Revenue, trailing twelve months | 75,465 | Reported trailing revenue is the fiscal year plus the latest first half less the previous first half. [10-K FY2025; 10-Q Q2 FY2026] | [10-K FY2025]; [10-Q Q2 FY2026] |
| Operating income, GAAP | 32,746 | Keep reported operating profit, including research, stock pay and acquisition amortization. [10-K FY2025; 10-Q Q2 FY2026] | [10-K FY2025]; [10-Q Q2 FY2026] |
| One-time items | none | — | — |
| Amortization of acquired intangibles (memo) | 8,014 | Keep the historical acquisition charge and show its future expiry on both profit and investment. [10-K FY2025; 10-Q Q2 FY2026] | [10-K FY2025]; [10-Q Q2 FY2026] |
| Stock-based compensation (memo) | 8,785 | Stock compensation remains a cost of employing people; it is never added back as free cash. [10-K FY2025; 10-Q Q2 FY2026] | [10-K FY2025]; [10-Q Q2 FY2026] |
| Research and development expense (memo) | 11,991 | Research remains an expense because a complete matched-period capitalization is not available for this mixed chip and software business. [10-K FY2025; 10-Q Q2 FY2026] | [10-K FY2025]; [10-Q Q2 FY2026] |
| Effective tax rate | 3.8% | This is the reported tax rate, including unusual benefits, rather than the forecast’s normal tax assumption. [10-K FY2025; 10-Q Q2 FY2026] | [10-K FY2025]; [10-Q Q2 FY2026] |
| Invested capital | 132,970 | Book capital retains goodwill and treats ordinary leases as rent, matching the peer comparison. Unidentified investment holdings make this a conservative capital-denominator proxy rather than an exact operating-asset valuation. [10-Q Q2 FY2026; Mature benchmark evidence] | [10-Q Q2 FY2026]; [Mature benchmark evidence] |

- **Revenue**, working notes:

    63,887 + 41,498 - 29,920 = 75,465. Semiconductor: 36,858 + 27,524 - 16,620 = 47,762; software: 27,029 + 13,974 - 13,300 = 27,703. The two segments sum exactly. [10-K FY2025, Note 13; 10-Q Q2 FY2026, Note 9]

- **Operating income gaap**, working notes:

    25,484 + 19,351 - 12,089 = 32,746; divided by 75,465 revenue gives 43.3923%. Accounting basis: reported GAAP EBIT is retained, including all SBC and R&D; no one-time adjustment is proposed. The repeated restructuring charge is not a one-off, and the H1 FY2026 excise-tax reversal sits in other income, outside EBIT. Goodwill stays in book capital. Operating leases remain rent expense and are excluded from debt-like bridge claims; this is the same rental basis used in the peer screen. [10-K FY2025; 10-Q Q2 FY2026; Mature benchmark evidence]
    
    The acquired-amortization switch remains off: the forecast margin deducts each year’s amortization and the net-investment override subtracts the same amount once, so the noncash charge is reversed through net investment rather than added twice. R&D stays in operating costs and is not counted again in capital spending. Its missing internally generated asset makes book ROIC a limited measure; a full capitalization would require matched rolling cohorts, defensible chip/software lives and an additional future tax/investment schedule that the switch does not supply. [Valuation base evidence; Accounting and reinvestment method]
    
    No large future acquisition is assumed in the operating cases. This is a conditional organic-growth forecast, not a claim that future acquisitions cost nothing: a new material purchase must be added at full cash-plus-stock consideration, with the associated sales, amortization and capital. VMware’s net consideration was 79,648 including 53,398 of shares; the illustrative full-consideration correction also includes 7,518 assumed debt and 600 Seagate assets. [10-K FY2025; Valuation base evidence]
    
    No prior valuation, owner-edited input or eligible frozen forecast exists for this initial draft; there is no company forecast lesson to adopt or reject. House scenario weights are assumptions of 25%/50%/25%, not measured likelihoods or confidence intervals. Current market price was not used to set an operating path. [Valuation evidence overview]

- **Amortization of acquired intangibles**, working notes:

    8,062 + 3,936 - 3,984 = 8,014, or 10.6195% of TTM sales.
    
    Observed: the May 3 intangible schedule is FY2026 remainder 3,940; FY2027 6,818; FY2028 5,689; FY2029 4,562; FY2030 3,378; thereafter 3,196, total 27,583. Purchased technology and customer relationships have weighted remaining lives of five and six years; this is not a schedule for hypothetical future acquisitions. [10-Q Q2 FY2026, Note 4]
    
    Analyst interpolation: spread each named fiscal year evenly across its two half-years. Allocate the otherwise undated thereafter bucket to FY2031/FY2032/FY2033 as 1,600/1,000/596, a declining illustrative schedule, not a disclosed fifth rolling-year amount. This gives rolling model-year amortization of 7,349; 6,253.5; 5,125.5; 3,970; 2,489; 1,300; 798; 298; 0; 0, summing exactly to 27,583. The fifth-year assumption can reasonably vary by about 800 either side without changing the remaining total; a revised filing schedule would replace this allocation. The same annual amount is deducted in margin and subtracted in net investment, so changing the timing does not create a duplicate cash add-back; taxes remain a simplified rate on forecast EBIT.
    
    Future engineering creates replacement products within expensed R&D, and all cases keep a physical-equipment/working-capital budget. The model does not declare the business maintenance-free when acquisition charges expire. A new acquisition or material intangible impairment requires rebuilding both sides of this bridge. [Accounting and reinvestment method]

- **Stock based compensation**, working notes:

    7,568 + 4,268 - 3,051 = 8,785; forecast margins retain a separately shown stock-pay allowance. The latest quarter’s diluted denominator already includes 129 million award shares. [10-Q Q2 FY2026, Notes 5 and 7]

- **Rnd expense**, working notes:

    10,977 + 5,960 - 4,946 = 11,991, or 15.8895% of sales. Accounting basis: reported GAAP EBIT is retained, including all SBC and R&D; no one-time adjustment is proposed. The repeated restructuring charge is not a one-off, and the H1 FY2026 excise-tax reversal sits in other income, outside EBIT. Goodwill stays in book capital. Operating leases remain rent expense and are excluded from debt-like bridge claims; this is the same rental basis used in the peer screen. [10-K FY2025; 10-Q Q2 FY2026; Mature benchmark evidence]
    
    The acquired-amortization switch remains off: the forecast margin deducts each year’s amortization and the net-investment override subtracts the same amount once, so the noncash charge is reversed through net investment rather than added twice. R&D stays in operating costs and is not counted again in capital spending. Its missing internally generated asset makes book ROIC a limited measure; a full capitalization would require matched rolling cohorts, defensible chip/software lives and an additional future tax/investment schedule that the switch does not supply. [Valuation base evidence; Accounting and reinvestment method]
    
    No large future acquisition is assumed in the operating cases. This is a conditional organic-growth forecast, not a claim that future acquisitions cost nothing: a new material purchase must be added at full cash-plus-stock consideration, with the associated sales, amortization and capital. VMware’s net consideration was 79,648 including 53,398 of shares; the illustrative full-consideration correction also includes 7,518 assumed debt and 600 Seagate assets. [10-K FY2025; Valuation base evidence]
    
    No prior valuation, owner-edited input or eligible frozen forecast exists for this initial draft; there is no company forecast lesson to adopt or reject. House scenario weights are assumptions of 25%/50%/25%, not measured likelihoods or confidence intervals. Current market price was not used to set an operating path. [Valuation evidence overview]

- **Effective tax rate**, working notes:

    Tax provision = -397+1,666-107=1,162; pretax earnings=22,729+18,325-10,575=30,479; rate=3.812462%. FY2025 benefited from releases/settlements and stock-pay deductions. The forward tax choice is separately explained in each scenario. [10-K FY2025, Note 12; 10-Q Q2 FY2026, Note 8]

- **Invested capital**, working notes:

    87,691 equity +64,907 book debt -19,628 cash =132,970. No operating-lease liability is added because rent remains in EBIT; no R&D asset is invented. Reported-tax TTM return on this ending-capital proxy is 23.6877%; at an analytical 21% tax rate it is 19.4550%, or 24.2163% before acquired amortization, a supplementary sensitivity only. These are not returns on future capital. Nonoperating investments are not separately removed because their stock value is unresolved. [10-Q Q2 FY2026; Valuation base evidence]

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
| Cash and marketable securities (added) | 19,628 | Use disclosed cash and equivalents once, with investment income excluded from operating profit. [10-Q Q2 FY2026] | [10-Q Q2 FY2026] |
| Non-operating asset (added): Corporate investments outside reported cash equivalents — carrying value unresolved | — | Investment purchases and sales establish that holdings exist but do not establish their current carrying balance. Keep this claim on assets unresolved until a dated stock amount or a supported immateriality bound is available. [10-Q Q2 FY2026] | [10-Q Q2 FY2026] |
| Debt (subtracted) | 64,907 | Use the reported book carrying amount consistently with the invested-capital screen. [10-Q Q2 FY2026] | [10-Q Q2 FY2026] |
| Operating lease liabilities (subtracted) | 0 | Ordinary leases stay as rent in operating costs, so no separate lease-debt deduction is made. This is an accounting-treatment zero, not a claim that no leases exist. [10-K FY2025] | [10-K FY2025] |
| Minority interests (subtracted) | 0 | No separate minority-interest balance is reported in the latest balance sheet. [10-Q Q2 FY2026] | [10-Q Q2 FY2026] |
| Other claim (subtracted): June 8 customer-lease backstop — present claim value unsupported | — | The contractual maximum is not the present value of this contingent claim, and the necessary deployment, default and recovery evidence is missing. This material gap blocks a completed equity valuation while the operating forecast remains reviewable. [10-Q Q2 FY2026] | [10-Q Q2 FY2026]; [Apollo platform release June 9]; [Apollo financing release June 9] |
| Other claim (subtracted): Existing uncertain-tax claim, undiscounted carrying amount | 1,662 | Deduct the separately disclosed unsettled tax claim once rather than folding old disputes into future normal operating taxes. Its payment timing remains uncertain. [10-Q Q2 FY2026] | [10-Q Q2 FY2026] |
| Other claim (subtracted): Underfunded pension plans, gross deficit carry-forward | 96 | Carry forward the last disclosed gross pension deficit without using inaccessible surpluses elsewhere to cancel it. This is a small dated proxy requiring replacement when the next plan disclosure arrives. [10-K FY2025] | [10-K FY2025] |
| Probability of failure | 0.0% | Model Broadcom as a going concern without a separate whole-company failure overlay. Customer nonpayment belongs in the unresolved backstop claim and operating downside, rather than being mislabeled as failure of Broadcom. [10-Q Q2 FY2026] | [10-Q Q2 FY2026] |
| What the assets would fetch in a failure | 0 | Unused while the whole-company failure probability is zero; this is not an estimate of liquidation proceeds. | [Analyst judgment] |
| Diluted shares (millions) | 4876.0 | Use the latest quarter’s diluted weighted-average shares, which already include disclosed award dilution. [10-Q Q2 FY2026] | [10-Q Q2 FY2026] |

- **Cash and marketable securities**, working notes:

    Cash at May 3 is 19,628; Treasury bills, deposits and money-market funds disclosed in Note 1 are already within this total. House bridge convention adds reported cash, without a separate invented minimum-cash reserve; operating funding is budgeted in reinvestment. Separate corporate investment balances remain unresolved below. [10-Q Q2 FY2026, balance sheet and Note 1]

- **Debt**, working notes:

    Principal 66,720 less unamortized discounts/issuance costs 1,813 =64,907; disclosed fair value is62,505. These are alternative measures, not additional claims. The book convention differs from principal by1,813 and fair value by2,402; a computation should preserve this explicit convention rather than mix denominators. [10-Q Q2 FY2026, Note 6]

- **Operating lease liabilities**, working notes:

    FY2025 liability1,325 and ROU asset1,318 are reported; a May3 stock update is unavailable. Expense182, cash payments277 and new ROU assets220 establish ongoing operating cash costs. Keeping both rent and rental funding in operations matches the peer basis and avoids subtracting lease debt while retaining the full rent cost. The missing current stock does not require a fabricated carry-forward liability. This treatment applies only to ordinary leases, not the separate 29,000 maximum customer backstop. [10-K FY2025, Note 6; Valuation base evidence]

- **Minority interests**, working notes:

    Total equity including noncontrolling interests and stockholders equity both equal87,691 in the reviewed statements/companyfacts. Zero means no separately reported material claim, not proof that every subsidiary is wholly owned. [10-Q Q2 FY2026; SEC bridge facts precutoff]

- **Probability of failure**, working notes:

    Observed cash19,628, TTM operating cash33,622, unused revolver7,500 and FY2027 principal493 provide financing capacity; no default probability is disclosed. Zero is a modelling choice for this operating forecast, not a measured absence of risk. A liquidity shortfall, covenant breach or inability to refinance would require a separate failure model and recoveries. [10-Q Q2 FY2026, Note 6; Valuation base evidence]

- **Diluted shares**, working notes:

    4,747 basic shares +129 dilutive awards =4,876; period-end4,758 and H1 average4,882 answer different questions. [10-Q Q2 FY2026, Note 5]

Dilution note: The quarter’s denominator already includes129 million award shares;183 million RSUs outstanding and20,106 of unrecognized future compensation overlap those measures and must not simply be added or deducted again; future SBC stays expensed. [10-Q Q2 FY2026, Notes 5 and 7]

## 5. Market inputs

| Item | Value in the file | Meaning |
|---|---|---|
| Price (USD per share) | auto | fetched from Yahoo at compute time |
| Risk-free rate | 4.94% | written in the file; used as given |
| Equity risk premium | 4.09% | written in the file; used as given |
| Mature-market equity risk premium | 4.50% | used for the terminal cost of capital |
| Marginal tax rate | 25.0% | used in the cost of capital build |

## 6. Cost of capital inputs

| Item | Value | Reason | Source |
|---|---|---|---|
| Method | build | — | — |
| Damodaran industry | Semiconductor | Semiconductors dominate the forward revenue mix, so that industry anchors shared business risk. Software is a stabilizing minority rather than a reason to assign separate arbitrary scenario rates. [10-Q Q2 FY2026] | [10-Q Q2 FY2026] |
| Unlevered beta | 1.505 | Use the cached Semiconductor industry beta as the shared risk proxy because chips dominate the forecast mix. It is an industry average, not a company-specific measured beta. [Damodaran betas January 2026, Semiconductor] | [Damodaran betas January 2026, Semiconductor] |
| Debt to equity (market values) | 0.0372 | Reported debt is about 3.7% of current market equity on the draft’s rental basis. The separately dated share price sets financing weights only. [Valuation market inputs September 2026; 10-Q Q2 FY2026] | [Valuation market inputs September 2026; 10-Q Q2 FY2026, balance sheet and Note 5] |
| Pre-tax cost of debt | 5.70% | Use a rounded current borrowing-cost estimate by carrying forward the latest ten-year issuance spread over Treasuries. It is a supported proxy, not an observed current bond yield or an extra penalty for operating risk. [January 2026 debt issue; Treasury debt proxy] | [January 2026 debt issue]; [Treasury debt proxy] |
| Terminal cost of capital method | mature | Use the house mature-company convention of the current dollar risk-free rate plus a4.5-point mature equity premium, shared by all scenarios. This is a normal-risk assumption, not a forecast of future bond yields. [Market inputs] | — |

- **Damodaran industry**, working notes:

    The base grows from47,762/75,465=63.29% semiconductor TTM sales toward more than80% in the final year. The selected industry has a useful fabless/hardware exposure but does not reproduce Broadcom’s software mix. A revenue-weighted software beta would require consistent separately sourced populations; use one clearly identified group here. Country shipment shares do not identify final operating-country risk: China shipment17% is expressly not end-customer exposure, so no invented country-risk surcharge is added. [10-K FY2025; 10-Q Q2 FY2026]

- **Unlevered beta**, working notes:

    Runner dataset fill: cash-corrected unlevered beta 1.5046492754744247; betas.xls dated 2026-01-05, cached 2026-09-07. Exact row Semiconductor. Original URL and cache date: tools/valuation/data/damodaran/MANIFEST.md.

- **Debt to equity market**, working notes:

    Operating leases are excluded on both sides under the rent convention. This market input affects financing weights only; no operational choice was made to achieve a price-relative answer.
    Runner arithmetic: (64907 debt + 0 debt-like lease adjustment) / (357.61 USD per share x 4876 million diluted shares) = 0.037223583907. Yahoo price observed 2026-09-18 16:00 EDT; direct fetch without valuation. Current financing weights are distinct from the June 9 operating cutoff. This uses the draft's disclosed lease/debt accounting basis.

- **Pretax cost of debt**, working notes:

    Observed January2026 ten-year note coupon4.95% and same-tenor DGS10 on January6/pricing and January13/closing4.18% imply a coupon-minus-Treasury proxy of0.77 percentage points. Adding that proxy to the separately dated current DGS10 of4.94% gives5.71%, rounded to a5.7% forecast cost of debt. Coupon differs from yield if issue price/fees matter, and the credit spread may have changed, so this is explicitly a financing judgment. [January 2026 debt issue; Treasury debt proxy]
    
    A roughly0.5–1.25-point current spread would imply5.44–6.19%;5.7% places the estimate near the recent same-tenor observation, consistent with cash generation and an unused revolver while retaining a positive credit spread. The range is an analyst uncertainty band, not a quoted market range. A current traded yield, new debt issue or evidence of changed credit risk should replace it; there is no scenario-specific surcharge for customer losses already in cash flow. [10-Q Q2 FY2026, Note6; Treasury debt proxy]

## 7. Inputs for the diagnostics

| Item | Value | Reason | Source |
|---|---|---|---|
| Market size in the final forecast year (USD millions) | 1,438,757 | Use a broad non-memory semiconductor ceiling as a scale check, with a separate software comparison in each revenue build. It is an extrapolated outer bound, not Broadcom’s addressable market or a forecast of its share. [WSTS spring 2026] | [WSTS spring 2026] |
| Company's own five-year revenue growth per year | 23.5% | This is the four-year compound change across five reported annual observations and includes VMware. It is context rather than an organic forecast. [10-K FY2025; 10-K FY2023] | [10-K FY2025]; [10-K FY2023] |
| Company's own five-year average operating margin | 37.0% | The five-year simple average retains GAAP acquisition costs and the VMware integration trough. [10-K FY2025; 10-K FY2023] | [10-K FY2025]; [10-K FY2023] |

## 8. Management guidance on record

Everything management has said in numbers or in words, whether or not it was used.

| Item | Quote | Source | Used as |
|---|---|---|---|
| Q3 total revenue | Third quarter revenue guidance of approximately $29.4 billion; | [Q2 FY2026 release] | near-term check on revenue_growth year1; not a full-year target |
| Q3 AI revenue | in Q3 we expect semiconductor revenue from AI to grow over 200 percent year-over-year to $16.0 billion. | [Q2 FY2026 release] | near-term check on revenue_growth year1 |
| Q3 operating margin | Third quarter non-GAAP operating income guidance of approximately 67 percent of projected revenue; | [Q2 FY2026 release] | near-term segment-margin check; not GAAP |
| Q3 EBITDA | Third quarter Adjusted EBITDA guidance of approximately 68 percent of projected revenue. | [Q2 FY2026 release] | not numeric: incompatible with GAAP EBIT without reconciliation |
| FY2026 AI target | For the full year 2026, we expect to achieve AI semiconductor revenue of $56 billion, up approximately 180% from fiscal 2025. | [Q2 FY2026 call] | revenue_growth year1 timing bridge |
| FY2027 AI target | we reiterate our AI semiconductor revenue guidance to be in excess of $100 billion. | [Q2 FY2026 call] | revenue_growth years1–2;100,000 is an open-ended floor, not midpoint |
| FY2027 delivery timing | We are planning to ship 10 gigawatts in 2027, and nothing has changed. Back-half loaded | [Q2 FY2026 call] | timing context; no revenue-per-GW conversion |
| FY2028 direction | We expect, in fact, 2028 to be a substantial growth from what we are forecasting in 2027. | [Q2 FY2026 call] | not numeric |
| Q3 chip revenue | We forecast semiconductor revenue of approximately $20.5 billion, up 124% year-on-year. | [Q2 FY2026 call] | near-term segment check, not a full-year target |
| Q3 software revenue | We expect Q3 infrastructure software revenue of approximately $8.9 billion, up 31% year-on-year. | [Q2 FY2026 call] | software year1 check, annual completion is analyst judgment |
| Q3 older-chip revenue | in Q3 we forecast non-AI semiconductor revenue to be approximately $4.5 billion, up 12% year-on-year. | [Q2 FY2026 call] | older-chip year1 check |
| Q3 gross margin | we expect Q3 consolidated gross margin to be down to approximately 74%. | [Q2 FY2026 call] | not numeric: non-GAAP mix check only |
| FY2026 tax | We expect the non-GAAP tax rate for Q3 and fiscal year 2026 to be approximately 16% | [Q2 FY2026 call] | tax normalization context; no permanent16% assumption |
| Q3 diluted shares | We expect the non-GAAP diluted share count in Q3 to be approximately 4.94 billion shares, excluding the impact of potential share repurchases. | [Q2 FY2026 call] | not numeric: latest reported GAAP diluted shares remain denominator |
| OpenAI timing | we are on track for production late 26. | [Q2 FY2026 call] | not numeric |
| Meta delivery | we expect to deploy 3 gigawatts through the end of 2028. | [Q2 FY2026 call] | not numeric |
| Two other customers | we expect shipments to begin in late 2026 and accelerate into 2027. | [Q2 FY2026 call] | not numeric |
| Networking milestone | We will now be taping out our next-generation 200-terabit switch this quarter. | [Q2 FY2026 call] | not numeric |
| AI networking mix | closer to around 30% | [Q2 FY2026 call] | not numeric: direction only; no separate networking revenue build |
| Platform ambition | deploy more than 20 gigawatts of compute capacity through 2028. | [Q2 FY2026 call] | not numeric: financing/platform capacity is not Broadcom chip revenue |
| Software direction | we expect that to continue, I guess, for the next multiple quarters as this demand picks up. | [Q2 FY2026 call] | not numeric |
| Garbled half-year growth | In the second half of 2026, we expect AI semiconductor revenue to double from the first half | [Q2 FY2026 call] | not numeric: inconsistent machine-transcript arithmetic; use explicit fiscal target wording instead |

## Sources

Every source tag used above, the cached file it points to (relative to the company folder), and the document date.

| Tag | Cached file | Date | Note |
|---|---|---|---|
| [10-K FY2025] | `sources/FY2026-Q2/10-K-FY2025.txt` | 2025-12-18 | Fiscal year ended2025-11-02; original statement and note locators in base evidence. |
| [10-K FY2023] | `sources/FY2026-Q2/10-K-FY2023.txt` | 2023-12-14 | Source of FY2021–FY2022 history. |
| [10-Q Q2 FY2026] | `sources/FY2026-Q2/10-Q-FY2026-Q2.txt` | 2026-06-09 | Quarter ended2026-05-03; Note11 includes June8 subsequent event. |
| [Q2 FY2026 release] | `sources/FY2026-Q2/press-release.txt` | 2026-06-03 | 8-K exhibit; reported Q2 numbers and Q3 guidance. |
| [Q1 FY2026 release] | `sources/FY2026-Q2/press-release-FY2026-Q1.txt` | 2026-03-04 | Q1 reported AI revenue8,400. |
| [Q2 FY2026 call] | `sources/FY2026-Q2/transcript.txt` | 2026-06-03 | Motley Fool third-party machine transcript, wording only; known garbles, especially half-year growth and Anthropic GW. Call date shown; posting date in original manifest. |
| [January 2026 debt issue] | `sources/FY2026-Q2/8-K-2026-01-13-notes-offering.txt` | 2026-01-13 | January2026 issuance coupons4.300–5.700%. |
| [Valuation base evidence] | `sources/FY2026-Q2/notes-valuation-base.md` | 2026-09-18 | Sourced calculations and exact original filing line locators; pre-cutoff evidence only. |
| [Mature benchmark evidence] | `sources/FY2026-Q2/notes-valuation-peers.md` | 2026-09-18 | Named comparators, definitions, opening-capital returns and limitations; not a primary filing. |
| [Valuation evidence overview] | `sources/FY2026-Q2/notes-valuation-evidence.md` | 2026-09-18 | Model-fit, evidence-gap and accounting map. |
| [WSTS spring 2026] | `sources/FY2026-Q2/wsts-spring-2026.txt` | 2026-06-02 | WSTS forecast pp1–2, not realized market size;2036 extension is analyst judgment. |
| [Apollo platform release June 9] | `sources/FY2026-Q2/apollo-platform-release-2026-06-09.txt` | 2026-06-09 | Primary platform announcement. |
| [Apollo financing release June 9] | `sources/FY2026-Q2/apollo-financing-release-2026-06-09.txt` | 2026-06-09 | Primary financing announcement; no disclosed guarantee fair value. |
| [SEC bridge facts precutoff] | `sources/FY2026-Q2/sec-bridge-facts-precutoff.txt` | 2026-06-09 | Filtered eligible companyfacts; absent current stock disclosure is not zero. |
| [Market inputs] | `sources/FY2026-Q2/valuation-market-inputs.txt` | 2026-09-18 | DGS10 observation2026-09-17; current ERP2026-09-01; industry data2026-01-05; price financing input only. |
| [QCOM FY2025 10-K] | `sources/FY2026-Q2/QCOM-10-K-FY2025.txt` | 2025-11-05 | Mature fabless/royalty comparator, retained GAAP basis. |
| [CSCO FY2025 10-K] | `sources/FY2026-Q2/CSCO-10-K-FY2025.txt` | 2025-09-03 | Mature hardware/software comparator, retained GAAP basis. |
| [MSFT FY2025 10-K] | `../MSFT/sources/FY2026-Q4/10-K-FY2025.txt` | 2025-07-30 | Only eligible FY2025 source reused despite later-labelled cache; PBP segment margin and consolidated capital are distinct. |
| [Accounting and reinvestment method] | `../../.claude/skills/draft-valuation/references/accounting-and-reinvestment.md` | 2026-09-18 | Local method reference, not company evidence; primary teaching locators within. |
| [Business-drivers method] | `../../.claude/skills/draft-valuation/references/business-drivers.md` | 2026-09-18 | Local method reference, not company evidence; primary teaching locators within. |
| [Uncertainty method] | `../../.claude/skills/draft-valuation/references/uncertainty-and-bias.md` | 2026-09-18 | Local method reference, not company evidence; primary teaching locators within. |
| [Damodaran industry data] | `../../tools/valuation/data/damodaran/MANIFEST.md` | 2026-01-05 | Runner fills actual cached industry beta and date. |
| [Analyst judgment] | `sources/FY2026-Q2/notes-valuation-evidence.md` | 2026-09-18 | Identifies assumptions made in this draft, not source-reported facts. |
| Damodaran betas January 2026, Semiconductor | `../../tools/valuation/data/damodaran/betas.csv` | 2026-01-05 | Cash-corrected unlevered beta; exact industry row. Cache manifest gives original URL and fetch date. |
| Valuation market inputs September 2026 | `sources/FY2026-Q2/valuation-market-inputs.txt` | 2026-09-18 | Direct Yahoo price fetch, FRED DGS10 and current cached ERP, separately dated from operating cutoff. |
| [Treasury debt proxy] | `sources/FY2026-Q2/fred-treasury-debt-proxy.txt` | 2026-09-18 | FRED same-tenor DGS10: January6/13 4.18%, September17 4.94%; current borrowing cost is an analyst proxy, not a traded bond quote. |
| [NVDA FY2026 release] | `sources/FY2026-Q2/NVDA-release-FY2026-Q4.txt` | 2026-02-25 | Primary NVIDIA annual release; only contemporaneous scale context, not a mature peer or TAM. |
| [NVDA Q1 FY2027 release] | `sources/FY2026-Q2/NVDA-release-FY2027-Q1.txt` | 2026-05-20 | Primary NVIDIA quarter release; revenue81,615, prior44,062; Data Center75,200. |
| [Damodaran capital data] | `../../tools/valuation/data/damodaran/capex.csv` | 2026-01-05 | Industry aggregates: Semiconductor66firms1.206668x, Software(System & Application)309firms1.538172x; definitions/populations differ from matched peer screen. |
