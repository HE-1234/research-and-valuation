# MRVL valuation assumptions as of FY2027-Q2

This file is a read-only view of the valuation inputs for Marvell Technology, Inc. (MRVL), held in `assumptions.yaml`. Every number and every sentence below comes from that file; nothing is computed here. To change a number, use the app (`uv run --extra app valuation-app`), which saves into the YAML, records the change, and rewrites this file. A dash (—) marks a cell that is empty in the file: the analyst had nothing defensible to put there, or the item is not given. Rates are stored as decimals and shown here as percentages; money is in USD millions.

| Item | Value |
|---|---|
| Ticker | MRVL |
| Company | Marvell Technology, Inc. |
| As-of quarter | FY2027-Q2 |
| As-of date (quarter cutoff) | 2026-08-28 |
| Drafted | 2026-09-09 |
| Horizon | 10 forecast years, then a terminal value: years 1-5 are set below and years 6-10 are built by rule |
| Currency and units | USD, millions |

## 1. The stories

Each story is copied word for word from `assumptions.yaml`.

### Bear (weight 25.0%)

The AI building boom cools once the years management has already put numbers on are behind it,
and Marvell turns out to be a parts supplier rather than a partner: the cloud giants keep the chip
designs that matter in-house, the flagship custom processor is not renewed for its next generation,
and the Google agreement vests only its early slices, so custom silicon shrinks back to the smaller
companion chips. Optics stays a good business, but a rival is first to the next speed step, so it
grows with cloud spending rather than faster than it; the factory deposits already promised are
paid up front, and then sales fall for a stretch in the middle of the decade. Marvell at the end of
the forecast is a merchant chip company, one that sells standard parts to anyone rather than designs
made for one customer, about twice today's size and earning about a quarter of sales as profit,
because the design bill and share-based pay stay fixed while sales do not, and it pays tax at the
low rate management guides until it is taxed like any mature company. To refill its roadmap it
goes back to buying small companies, so each new dollar of sales costs about as much capital as it
does for an average chip company, and nothing above the cost of capital survives into the long run.

How the story becomes numbers:

| What the story says | Which input it sets | The number | Source |
|---|---|---|---|
| The AI building boom cools once the years management has already put numbers on are behind it | revenue growth, years 1 and 2 (the guided quarter and the two guided years taken at the bottom of their ranges) | 0.43, 0.21 | [Q2 FY2027 release; Q2 FY2027 call] |
| the flagship custom processor is not renewed for its next generation, and the Google agreement vests only its early slices, so custom silicon shrinks back to the smaller companion chips | revenue growth, years 3 and 4 (the custom line of the segment build falls from fiscal 2030) | -0.04, -0.10 | [10-K FY2026, Item 1A; 8-K 2026-08-19] |
| a rival is first to the next speed step, so it grows with cloud spending rather than faster than it | revenue growth, year 5 and the fade years (interconnect at a normal chip-industry pace) | 0.05 | [Q1 FY2027 call] |
| Marvell at the end of the forecast is a merchant chip company, one that sells standard parts to anyone rather than designs made for one customer, about twice today's size | the end state the growth path is backed out from (year-10 revenue against the market size and the sector) | about 18,800 of revenue in year 10 against a custom market of about 126,100 | [Q1 FY2027 call; Damodaran capex.xls, Semiconductor, 2026-01-05] |
| earning about a quarter of sales as profit, because the design bill and share-based pay stay fixed while sales do not | operating margin, years 1 to 5 | 0.23, 0.26, 0.24, 0.23, 0.25 | [Q2 FY2027 release; Q2 FY2027 supplemental, p.5; 10-Q Q2 FY2027, Note 5] |
| it pays tax at the low rate management guides until it is taxed like any mature company | tax rate, start and terminal | 0.13, 0.25 | [Q2 FY2027 call] |
| the factory deposits already promised are paid up front, and then sales fall for a stretch in the middle of the decade | reinvestment override, years 1 to 3 (the guided capacity prepayments plus working capital in year 1; no capital handed back in the falling years) | 2200, 200, 150 | [Q2 FY2027 call; 10-Q Q2 FY2027, Note 9; 10-K FY2024, Item 8] |
| To refill its roadmap it goes back to buying small companies, so each new dollar of sales costs about as much capital as it does for an average chip company | sales to capital, years 1 to 5 and years 6 to 10 | 1.5, 1.2 | [Damodaran capex.xls, Semiconductor, 2026-01-05; 10-K FY2024, Item 8] |
| nothing above the cost of capital survives into the long run | terminal return-on-capital premium, and terminal growth at the bond rate | 0.0; riskfree | [business.md section 5; 10-K FY2026, Item 1A] |

### Base (weight 50.0%)

Marvell delivers the two years management has put numbers on, about 18 billion of sales next fiscal
year, and then its custom chips for cloud companies pass the target management set for the year
after as the Google programs behind the summer warrant begin to ship, while its optics and switches
keep growing with AI data-center spending and the new market for optics inside the rack. Growth
slows each year after that as the first wave of programs reaches full volume and customers build to
their capacity plans rather than in a rush, so that by the end of the forecast Marvell is a chip
company about seven times today's size, holding a leading share of the custom silicon market and a
leading place in the optics that connect AI computers. Profit margins roughly double, because the
write-down of old acquisitions runs off and costs grow far more slowly than sales, while the shift
toward lower-margin custom chips gives part of that back; tax starts at the low rate management
guides and rises to a mature company's. Most of the money growth needs is tied up in inventory and
unpaid customer bills rather than in factories, so growth is cheap to fund in the ramp years and
dearer later, when Marvell returns to buying small technology companies to refill its roadmap. Its
custom designs lock a customer in for a chip generation and its optics have led each speed step,
but its customers are a handful of giants who design chips themselves and press on price, so in the
long run its return on capital settles at about half the level it reaches at the end of the
forecast: well above its cost of capital, below what its designs earn today.

How the story becomes numbers:

| What the story says | Which input it sets | The number | Source |
|---|---|---|---|
| Marvell delivers the two years management has put numbers on, about 18 billion of sales next fiscal year | revenue growth, years 1 and 2 | 0.58, 0.47 | [Q2 FY2027 call; Q2 FY2027 release] |
| its custom chips for cloud companies pass the target management set for the year after as the Google programs behind the summer warrant begin to ship | revenue growth, year 3 (the custom line of the segment build in fiscal 2029) | 0.39 | [Q1 FY2027 call; Q2 FY2027 call; 8-K 2026-08-19] |
| Growth slows each year after that as the first wave of programs reaches full volume and customers build to their capacity plans rather than in a rush | revenue growth, years 4 and 5, then the fade to the bond rate by year 10 | 0.20, 0.15 | [Q1 FY2027 call; Q2 FY2027 call] |
| by the end of the forecast Marvell is a chip company about seven times today's size, holding a leading share of the custom silicon market | the end state the growth path is backed out from (year-10 revenue against the market size and the sector) | about 64,300 of revenue in year 10, of which custom about 31,400, a 25% share of a custom market of about 126,100 | [Q1 FY2027 call; Damodaran histgr.xls and capex.xls, Semiconductor, 2026-01-05] |
| Profit margins roughly double, because the write-down of old acquisitions runs off and costs grow far more slowly than sales | operating margin, years 1 to 5 | 0.27, 0.32, 0.34, 0.35, 0.35 | [10-Q Q2 FY2027, Note 5; Q2 FY2027 call] |
| while the shift toward lower-margin custom chips gives part of that back | operating margin, years 3 to 5 (gross margin carried from 58.9% to 55.5% inside the bridge, so the path flattens) | 0.35 | [Q2 FY2027 call; DEF 14A 2026, CD&A] |
| tax starts at the low rate management guides and rises to a mature company's | tax rate, start and terminal | 0.13, 0.25 | [Q2 FY2027 call] |
| Most of the money growth needs is tied up in inventory and unpaid customer bills rather than in factories | reinvestment override, year 1 (working capital on next year's growth plus the guided capacity prepayments, net of depreciation) | 3700 | [Q2 FY2027 call; 10-Q Q2 FY2027, Note 14; 10-K FY2026, Item 8] |
| so growth is cheap to fund in the ramp years | sales to capital, years 1 to 5 (the forward component build: 35 cents of working capital per new dollar plus capital spending at 4.5% of revenue) | 2.2 | [10-K FY2026, Item 8; 10-Q Q2 FY2027, Item 1] |
| and dearer later, when Marvell returns to buying small technology companies to refill its roadmap | sales to capital, years 6 to 10 (the acquisitions take the organic fade-year figure down to about 1.3; 1.1 is set with the eight-point terminal premium as a pair so that year 10 earns about twice the perpetual return, as the last sentence says) | 1.1 | [10-K FY2024, Item 8; 10-Q Q2 FY2027, Note 4; Damodaran capex.xls, Semiconductor, 2026-01-05] |
| in the long run its return on capital settles at about half the level it reaches at the end of the forecast: well above its cost of capital, below what its designs earn today | terminal return-on-capital premium (set with the late sales-to-capital ratio as a pair so that year 10 earns about twice the perpetual return), and terminal growth at the bond rate | 0.08; riskfree | [10-Q Q2 FY2027, Item 1; business.md section 5] |

### Bull (weight 25.0%)

Marvell becomes the design house the cloud giants turn to when they build their own AI chips: the
Google agreement runs close to the pace its warrant implies, with most of its revenue slices vesting
before it expires, and the new top-tier processor program becomes a franchise that renews generation
after generation. Optics moves inside the rack, so the light-emitting parts placed next to the
processor and the switches that go with them grow into a second business as large as all of Marvell
today. By the end of the forecast Marvell is one of the largest chip companies in the world, more
than ten times today's size, with a profit margin above its industry's average during the build-out
that drifts back toward that average as growth slows and its giant customers press on price; tax
starts at the low rate management guides and rises to a mature company's. Growth is paid for out of
cash flow, since the factory capacity is already reserved and most of the investment is inventory
and unpaid bills, with no large acquisitions needed, and as growth slows its returns settle to what
the chip industry earns today. Because Marvell then owns both ends of the optical link, the switch
and the customer's own chip design, the advantage proves durable and it keeps earning a return of
around twenty percent on its capital for the long run, still below what its designs earn today.

How the story becomes numbers:

| What the story says | Which input it sets | The number | Source |
|---|---|---|---|
| the Google agreement runs close to the pace its warrant implies, with most of its revenue slices vesting before it expires, and the new top-tier processor program becomes a franchise that renews generation after generation | revenue growth, years 1 to 3 (the custom line of the segment build) | 0.68, 0.56, 0.55 | [8-K 2026-08-19; Q2 FY2027 call; Q1 FY2027 call] |
| Optics moves inside the rack, so the light-emitting parts placed next to the processor and the switches that go with them grow into a second business as large as all of Marvell today | revenue growth, years 4 and 5 (the interconnect and switching lines of the segment build) | 0.34, 0.20 | [Q2 FY2027 call; Q1 FY2027 call] |
| By the end of the forecast Marvell is one of the largest chip companies in the world, more than ten times today's size | the end state the growth path is backed out from (year-10 revenue against the sector and the market size) | about 103,000 of revenue in year 10 against a sector selling 460,000 to 510,000 today and a custom market of about 126,100 | [Damodaran capex.xls and margin.xls, Semiconductor, 2026-01-05; Q1 FY2027 call] |
| with a profit margin above its industry's average during the build-out | operating margin, years 1 to 5 | 0.29, 0.34, 0.38, 0.40, 0.40 | [Q2 FY2027 call; Damodaran margin.xls, Semiconductor, 2026-01-05] |
| that drifts back toward that average as growth slows and its giant customers press on price | operating margin, years 6 to 10 (the fade years, written out because the story moves them) | 0.39, 0.38, 0.38, 0.37, 0.36 | [10-K FY2026, Item 1A; Damodaran margin.xls, Semiconductor, 2026-01-05] |
| tax starts at the low rate management guides and rises to a mature company's | tax rate, start and terminal | 0.13, 0.25 | [Q2 FY2027 call] |
| Growth is paid for out of cash flow, since the factory capacity is already reserved and most of the investment is inventory and unpaid bills, with no large acquisitions needed | sales to capital, years 1 to 5, and the reinvestment override for year 1 (working capital plus the guided prepayments, net of depreciation) | 2.2; 4400 | [10-Q Q2 FY2027, Note 9; Note 14; Q2 FY2027 call] |
| as growth slows its returns settle to what the chip industry earns today | sales to capital, years 6 to 10 (set where the year-10 implied return meets the industry's) | 1.3 | [Damodaran capex.xls and margin.xls, Semiconductor, 2026-01-05] |
| it keeps earning a return of around twenty percent on its capital for the long run | terminal return-on-capital premium, and terminal growth at the bond rate | 0.11; riskfree | [10-Q Q2 FY2027, Item 1; business.md section 5] |

### Management (not weighted; not computed)

Management's numbers on record: roughly 12 billion of revenue this fiscal year and approximately
18 billion next, data center up about 60% this year and more than 60% next, custom more than
doubling in fiscal 2028 and over 10 billion in fiscal 2029, operating expenses growing at half the
rate of revenue next year, an adjusted operating margin entering 38% to 40% this quarter and reaching
the upper end of that range through fiscal 2028, gross margin holding in a 57.5% to 58.5% range,
about 1 billion of capacity prepayments this year and a tax rate of about 13% next year. Nothing
numeric reaches beyond fiscal 2029, so the case cannot be computed; the October 6, 2026 Investor Day
promises revenue 'out until the end of the decade' and a reset of the margin model. The base case
tracks these figures for two years and then judges the rest; the bull takes them at the top of their
ranges and the bear at the bottom.

Why this case is not computed: Management has met the requirement of at least one multi-year revenue or margin target, giving revenue figures for two years and a margin target, but it has given nothing numeric beyond FY2028, which is only model year 2, except a custom target for FY2029 that covers one product line. Years 3 to 5 would therefore be guesswork rather than filling in between guided points, so this case is left uncomputable. Dollar signs inside the quotations below are written as USD because the app reads a dollar sign as a formula.

## 2. Scenario inputs

Rows are inputs and columns are cases. Per-year cells read year 1 / year 2 / ... in order. The reasons and sources behind each cell follow the table.

| Input | Bear | Base | Bull | Management |
|---|---|---|---|---|
| Weight | 25.0% | 50.0% | 25.0% | not weighted |
| Computable | always | always | always | no |
| Revenue growth, years 1-5 (years 6-10 by rule) | 43.0% / 21.0% / -4.0% / -10.0% / 5.0% | 58.0% / 47.0% / 39.0% / 20.0% / 15.0% | 68.0% / 56.0% / 55.0% / 34.0% / 20.0% | 58.7% / 20.0% / — / — / — |
| Operating margin, years 1-10 | 23.0% / 26.0% / 24.0% / 23.0% / 25.0% / — / — / — / — / — | 27.0% / 32.0% / 34.0% / 35.0% / 35.0% / — / — / — / — / — | 29.0% / 34.0% / 38.0% / 40.0% / 40.0% / 39.0% / 38.0% / 38.0% / 37.0% / 36.0% | 21.2% / — / — / — / — / — / — / — / — / — |
| Sales-to-capital, years 1-5 | 1.50 | 2.20 | 2.20 | — |
| Sales-to-capital, years 6-10 | 1.20 | 1.10 | 1.30 | — |
| Reinvestment override, years 1-5 (USD millions; later years by rule) | 2,200 / 200 / 150 / — / — | 3,700 / — / — / — / — | 4,400 / — / — / — / — | — / — / — / — / — |
| Tax rate, forecast years | 13.0% | 13.0% | 13.0% | 13.0% |
| Tax rate, terminal year onwards | 25.0% | 25.0% | 25.0% | 25.0% |
| Cost of capital override | — | — | — | — |
| Terminal growth | the run's risk-free rate | the run's risk-free rate | the run's risk-free rate | — |
| Terminal growth may exceed the risk-free rate | no | no | no | no |
| Terminal return on capital: points above the cost of capital | 0.00% | 8.00% | 11.00% | — |
| A large premium is allowed (above base 8, bull 12 points) | no | no | no | no |

Years 6-10 are not written in the file; the engine builds them from the last year set above: growth moves in equal steps to terminal growth, the margin holds, per-year reinvestment figures stop, and sales-to-capital switches to the years 6-10 ratio.

- Bear, years 6-10 by rule: growth moving from 5.00% to the risk-free rate; margin held at 25.0% through year 10.
- Base, years 6-10 by rule: growth moving from 15.0% to the risk-free rate; margin held at 35.0% through year 10.
- Bull, years 6-10 by rule: growth moving from 20.0% to the risk-free rate; margin held at 40.0% through year 10.

### Bear: reasons

- **Revenue growth** — Year 1 is above the 37% just reported only because the guided quarter and the two guided years are named items, taken here at the bottom of their ranges rather than the middle (outlook.md section 4). Growth then slows sharply as cloud customers digest what they have bought, and revenue falls in years 3 and 4 because the flagship custom program is not renewed and the Google programs vest only their early slices, the risk business.md section 6 ranks second. [Q2 FY2027 release; Q2 FY2027 call; Q1 FY2027 call; 10-K FY2026, Item 1A; 8-K 2026-08-19]

    The run-rate the path starts from: the latest quarter is up 37% (2,739.3 against 2,006.1) and the
    trailing twelve months up 31% (9,450.3 against 7,234.9) [Q2 FY2027 supplemental, p.5]. What moves
    year 1 off it: the third quarter is guided to 3,150 plus or minus 5%, the fourth to accelerate
    again, fiscal 2027 to roughly 12 billion and fiscal 2028 to approximately 18 billion
    [Q2 FY2027 release; Q2 FY2027 call]. This case takes the third quarter at the bottom of its range
    (2,993), a fourth quarter of 3,400 that grows 14% on the quarter instead of the 17% the full-year
    figure needs, so fiscal 2027 is 11,550, and a fiscal 2028 of 15,450 in which custom grows 80%
    rather than 'more than double' because the second large processor program slips (computed)
    [Q2 FY2027 call].
    
    How the year windows are built. Each model year is a twelve-month window ending in early August,
    so it holds the second half of one fiscal year and the first half of the next. Each line's
    first-half share of a fiscal year is set by its own growth pace (steady quarter-on-quarter growth
    gives a first half of 1 divided by 1 plus the square root of 1 plus the year's growth); the
    reported halves of fiscal 2026 and fiscal 2027 are used where they exist [Q2 FY2027 supplemental,
    p.5; p.10].
    
    The fiscal-year build under the current two-segment definition. Marvell reports only data center
    and communications and other [10-Q Q2 FY2027, Note 3]. Inside data center, two lines have a
    sourced anchor and a growth engine of their own, so they are carried separately and labelled as
    our inference: custom (program wins at a few customers, sized top-down from management's target
    and market) and switching (share gain in an established market plus the new scale-up switch
    market); everything else in data center (optical DSPs, TIAs and drivers, DCI modules, scale-up
    optics, storage, cables and retimers, all merchant parts that follow cloud spending and speed
    transitions) is one residual line. Anchors: custom in fiscal 2026 is set at 2,000 so that the
    'more than 20%' fiscal 2027 growth and the 'more than double' fiscal 2028 land where analysts on
    the calls put the business, 'around 5 billion to 6 billion in calendar 27' and 'a little over 4
    billion' for the processors alone, neither disputed by the chief executive [Q1 FY2027 call;
    Q2 FY2027 call]; switching in fiscal 2026 is 300 because the fiscal 2027 target was 'exceed 600
    million, doubling from fiscal 2026' [Q1 FY2027 call]; the residual is data center's 6,100.3 less
    those two [10-K FY2026, Note 3].
    
    | Fiscal year | Custom | Switching | Interconnect and other data center | Data center | Communications and other | Company | Company growth |
    |---|---|---|---|---|---|---|---|
    | FY2026 actual | 2,000 | 300 | 3,800 | 6,100 | 2,094 | 8,195 | 42% |
    | FY2027 | 2,500 | 600 | 6,250 | 9,350 | 2,200 | 11,550 | 41% |
    | FY2028 | 4,500 | 850 | 7,850 | 13,200 | 2,250 | 15,450 | 34% |
    | FY2029 | 5,000 | 950 | 8,200 | 14,150 | 2,300 | 16,450 | 7% |
    | FY2030 | 3,800 | 850 | 7,500 | 12,150 | 2,250 | 14,400 | minus 12% |
    | FY2031 | 3,500 | 900 | 7,800 | 12,200 | 2,350 | 14,550 | 1% |
    | FY2032 | 3,700 | 1,000 | 8,300 | 13,000 | 2,450 | 15,450 | 6% |
    
    | Part of the business | Trailing revenue | Latest reported growth | Year 1 growth | Year 3 growth | Year 5 growth |
    |---|---|---|---|---|---|
    | Custom (inference) | 2,110 | dollars not disclosed | up 59% | down 8% | flat |
    | Switching (inference) | 413 | dollars not disclosed | up 77% | flat | up 10% |
    | Interconnect and other data center (residual) | 4,651 | dollars not disclosed | up 56% | down 3% | up 7% |
    | Data center, as reported | 7,173 | up 46% in the quarter, up 33% on the year | up 58% | down 5% | up 5% |
    | Communications and other, as reported | 2,277 | up 10% in the quarter, up 24% on the year | down 5% | up 1% | up 5% |
    | Company | 9,450 | up 37% in the quarter, up 31% on the year | up 43% | down 4% | up 5% |
    
    Trailing figures for the two reported segments come from the eight-quarter table; the three
    inferred lines are the fiscal build read over the same window [Q2 FY2027 supplemental, p.10].
    Company revenue in the five windows: 13,514; 16,352; 15,698; 14,128; 14,834 (computed); the build
    sums to within one percent of them, the difference being growth rounded to whole points.
    
    Drivers of each step down of more than three points. Year 1 to year 2, 43% to 21%: fiscal 2027's
    guided surge leaves the window and custom grows 80% rather than doubling [Q2 FY2027 call]. Year
    2 to year 3, 21% to minus 4%: the flagship processor program is not renewed for its next
    generation, which the 10-K says can mean 'foregoing revenues from a given customer's product line
    for the life of that product', and the Google agreement vests only its first slices
    [10-K FY2026, Item 1A; 8-K 2026-08-19]. Year 3 to year 4, minus 4% to minus 10%: cloud customers
    digest what they have bought and data center falls 14% in fiscal 2030, as it fell in fiscal 2024
    when revenue dropped 7% [10-K FY2026, Item 7]. Year 4 to year 5, minus 10% to plus 5%: the next
    optical speed step and scale-up switching restart growth at a normal chip-industry pace, then the
    fade carries it to the bond rate by year 10.
    
    The end state and its tests. Year-10 revenue is about 18,800, twice today's 9,450 and about 4% of
    the 460,000 to 510,000 that the 66 US semiconductor companies in Damodaran's dataset sell today
    (an inference: their net capital spending of 22,421 divided by the row's net capital spending of
    4.4% of sales, or by its 14.5% of after-tax operating profit at a 33.5% after-tax margin)
    [Damodaran capex.xls and margin.xls, Semiconductor, 2026-01-05]. Custom at its year-5 share of
    24% is about 4,500 in year 10, a 3.6% share of the custom market carried forward in the
    diagnostics, against the 20% management targets; size never binds in this case [Q1 FY2027 call].
    Growth agrees with margin: a company losing its custom programs sells more merchant parts at
    merchant margins, so gross margin recovers a little while the total shrinks. Is it plausible:
    Marvell has done this before, revenue falling 7% in fiscal 2024 with data center down as customers
    worked off inventory [10-K FY2026, Item 7]. Is it probable: most sales are on purchase orders
    customers can change 'with relatively short notice', ten customers were 82% of fiscal 2026
    revenue, and this quarter management dropped the numbers from its product-line targets
    (outlook.md section 6) [10-K FY2026, Item 1A].
- **Operating margin** — Margins improve on today's 16.5% even here, because the yearly write-down of past acquisitions runs off whatever happens to sales (business.md section 3). What the bear takes away is the climb: a shrinking business cannot spread a fixed design bill and 1.3 billion a year of share pay, so the reported margin settles near a quarter of sales, between the telecom-equipment and semiconductor-equipment industry averages and well below the semiconductor average. [Q2 FY2027 release; Q2 FY2027 call; 10-Q Q2 FY2027, Note 5; Q2 FY2027 supplemental, p.5; Damodaran margin.xls, Semiconductor, 2026-01-05]

    Where the target sits. Damodaran's US semiconductor row earns a 35.3% operating margin after share
    pay and amortization (40.4% before share pay) on a 59.0% gross margin; the neighbouring rows read
    26.2% for semiconductor equipment, 22.5% for computers and peripherals, 20.7% for telecom
    equipment and 12.8% for the whole market [Damodaran margin.xls, 2026-01-05]. Marvell's own best
    reported year was 16.1% (FY2026) and its worst minus 12.5% (FY2025); its adjusted margin was 35.3%
    in FY2026 and 36.6% in the latest quarter (business.md section 3) [Q2 FY2027 release]. A 25%
    reported margin therefore places the bear between the equipment and telecom rows: a merchant
    chip company without scale advantages, still far above Marvell's own history because the
    amortization is gone. Named comparables from business.md (Broadcom as competitor) carry no margin
    figure in the cached sources, so the industry rows stand in for them.
    
    The bridge, first at fiscal-year level (the company's own adjusted margin), then converted to the
    model's windows and reduced to the reported margin.
    
    | Fiscal year | Adjusted gross margin | Adjusted operating expenses | Expenses over revenue | Adjusted operating margin | Share-based pay | Custom share of revenue |
    |---|---|---|---|---|---|---|
    | FY2027 | 58.3% | 2,550 | 22.1% | 36.2% | 1,164 | 22% |
    | FY2028 | 57.0% | 3,000 | 19.4% | 37.6% | 1,350 | 29% |
    | FY2029 | 56.0% | 3,150 | 19.1% | 36.9% | 1,400 | 30% |
    | FY2030 | 55.0% | 3,000 | 20.8% | 34.2% | 1,350 | 26% |
    | FY2031 | 55.0% | 2,900 | 19.9% | 35.1% | 1,300 | 24% |
    | FY2032 | 55.5% | 2,950 | 19.1% | 36.4% | 1,300 | 24% |
    
    | Model year | Adjusted operating margin | Less share-based pay | Less acquisition write-downs | Less write-down of acquired research | Less restructuring and deal costs | Reported margin | Used |
    |---|---|---|---|---|---|---|---|
    | 1 | 37.2% | 9.3 | 3.9 | 0.2 | 0.3 | 23.4% | 23% |
    | 2 | 37.1% | 8.6 | 1.3 | 0.5 | 0.6 | 26.1% | 26% |
    | 3 | 35.6% | 8.9 | 0.8 | 0.8 | 1.2 | 23.8% | 24% |
    | 4 | 34.6% | 9.1 | 0.6 | 1.0 | 1.2 | 22.6% | 23% |
    | 5 | 35.7% | 8.7 | 0.3 | 1.0 | 0.7 | 25.0% | 25% |
    
    Each row is rounded to the nearest whole point, in whichever direction it falls.
    
    What drags. Gross margin falls to 55.0% by fiscal 2030 against 58.9% today: custom is a bigger
    share of a smaller total through fiscal 2029, the chief financial officer named mix as 'the
    primary driver' of the guided step down this quarter, and after that unused capacity reservations
    and the 'significant pricing pressures' the 10-K expects take over [Q2 FY2027 call; 10-K FY2026,
    Item 1A]. Share-based pay stays near 1,300 to 1,400 a year, because grants already made vest over
    four years and 190.1 of acquired-company awards are still to be charged, so it rises to almost
    nine points of a shrinking revenue; it was 326.2 in the latest quarter alone [Q2 FY2027
    supplemental, p.5; 10-Q Q2 FY2027, Note 10]. Adjusted operating expenses keep rising to 3,150 in
    fiscal 2029 because chip designs already started cannot be stopped, and are cut only afterwards.
    Restructuring returns in the down years, as it has every year since fiscal 2024 [10-K FY2026,
    Note 4].
    
    What offsets. Growth spending inside today's costs: research is 25.8% of revenue against the
    industry's 15.4%, so even a shrinking Marvell can cut design spending on programs that are not
    renewed [Damodaran margin.xls, Semiconductor, 2026-01-05]. The write-down of acquired technology
    falls on the schedule in the accounts, from 9.4 points of revenue to 0.3 by year 5: 385.3 for the
    rest of fiscal 2027, 292.7, 139.6, 117.2, 60.8 and 54.0 after that [10-Q Q2 FY2027, Note 5]. The
    1,297.0 of acquired research not yet in use starts being written off over 6 to 13 years as
    products ship, taken here at 60 in fiscal 2028 rising to 150 a year by fiscal 2031, an inference
    placed inside the 100 to 216 range the useful lives imply [10-Q Q2 FY2027, Note 5]. Depreciation
    is a small offset: it is 443 in year 1, the same as in the other cases because it reflects
    spending already made, and then grows 12% a year rather than the 20% of the growth cases because
    capital spending on a flat revenue base adds less to the asset base, so it runs 443 to 697 a year,
    3.0% to 4.7% of revenue against 3.9% today, and neither helps nor hurts much (computed)
    [10-Q Q2 FY2027, Item 1].
- **Sales-to-capital** — Each dollar of investment supports 1.50 of new sales in this case and 1.20 later, against 2.20 in the base case, because growth has to be bought by acquisition again as it was in fiscal 2022 and fiscal 2027, and 1.20 is exactly what the average US semiconductor company gets (business.md sections 1 and 4). Buying a company is the most expensive way to add revenue Marvell has used. [10-K FY2024, Item 8; 10-K FY2026, Item 8; 10-Q Q2 FY2027, Note 4; Damodaran capex.xls, Semiconductor, 2026-01-05]

    The three candidates, measured the way the model spends (money spent in one year buys the next
    year's growth), are tabled in the base case. In short: Marvell's own lagged record is 2.6 and 3.4
    in the two organic years that can be read and 1.3 over the five years including acquisitions;
    last year's marginal ratio is 3.4 without deals, or about 0.95 if the Celestial and XConn
    purchases in fiscal 2027 are counted against the fiscal 2028 guide; the industry figure is 1.21
    [10-K FY2024, Item 8; 10-K FY2026, Item 8; 10-Q Q2 FY2027, Note 4; Damodaran capex.xls,
    Semiconductor, 2026-01-05]. What differs here is the assumption that deals are needed again:
    fiscal 2022 cost 3,555.0 of cash for Inphi and Innovium, and the first half of fiscal 2027 cost
    1,270.9 of cash plus about 2,500 in shares for Celestial and XConn, whose revenue is still 'not
    material' [10-K FY2024, Item 8; 10-Q Q2 FY2027, Note 4]. Counting those deals, the ratio in an
    acquisition year has been between 0.3 and 1.0, so 1.50 sits between the acquisition years and the
    organic record, and 1.20 in the fade years is the industry figure, the ratio of an average chip
    company. The year-10 implied return on capital from the dry run at these settings is about 13.5%,
    above the 9.28% cost of capital the case ends at and far below the 40.5% the industry earns today
    (after-tax margin 33.5% times sales to capital 1.21), which is what a company that has lost its
    edge should show [Damodaran margin.xls and capex.xls, Semiconductor, 2026-01-05].
- **Reinvestment override** — Year 1 is set in dollars because management has named a spending level the ratio does not cover, about 1 billion of factory prepayments this fiscal year with deposits running into next (outlook.md section 4). Years 2 and 3 are set to small positive amounts because the ratio would hand cash back in the shrinking years, which Marvell's own record says does not happen. All three figures are after subtracting depreciation. [Q2 FY2027 call; 10-Q Q2 FY2027, Note 9; Note 14; 10-Q Q1 FY2027, Note 9; 10-K FY2024, Item 8]

    Year 1 = about 990 of extra working capital on the following year's revenue increase of 2,838 at
    the 35 cents per dollar the base case derives, plus about 1,000 of capacity prepayments falling
    inside the window, plus about 165 of capital spending net of depreciation (608 at 4.5% of revenue
    less 443, the same year-1 depreciation as the other cases because it reflects spending already
    made), which is 2,158, taken as 2,200 (computed) [Q2 FY2027 call; 10-Q Q2 FY2027, Note 14].
    The prepayments: management is 'on pace to make approximately 1 billion of capacity prepayments to
    suppliers in fiscal 2027' (dollar sign written as a word), the balance rose 223.9 in the second
    quarter, and the 870.0 of deposits agreed in May are 'payable in quarterly installments from the
    second quarter of fiscal 2027 through the second quarter of fiscal 2028', so the year-1 window
    holds the roughly 776 left of the fiscal 2027 figure plus two more quarterly installments of about
    174, less an allowance of about 125 for prepayments applied against wafer purchases before the
    window ends: about 1,000 (computed) [Q2 FY2027 call; 10-Q Q2 FY2027, Note 14; 10-Q Q1 FY2027,
    Note 9]. The ratio alone would have charged 1,892.
    Years 2 and 3 are 200 and 150 rather than the minus 436 and minus 1,047 the ratio would produce,
    because unconditional commitments to foundries and test partners stood at 8,518.9 at August 1,
    2026 and cannot be unwound at will, so wafers keep arriving into inventory when demand falls, and
    because when revenue last fell, in fiscal 2024, working capital released only 57.8 on a 411.9
    revenue decline while capital spending ran 36.5 above depreciation [10-Q Q2 FY2027, Note 9;
    10-K FY2024, Item 8]. Years 4 and 5 use the ratio, which is positive because revenue is rising
    again: about 471 and 490 (computed).
- **Tax rate** — Starts at management's own estimate of tax on continuing profits for fiscal 2028, approximately 13%, the figure explained in the base-year tax cell, and rises to the 25% rate the model uses for a mature company. In this case profits are lower, so the low start matters less. [Q2 FY2027 call]
- **Terminal growth** — The ten-year government bond rate fetched for the run, as the method requires: no company outgrows the economy forever.
- **Terminal return on capital premium** — Nothing above the cost of capital: in this case the moat is gone, a customer has taken a program away and the next speed step in optics went to a rival, so Marvell ends up earning exactly what its investors require, which is the method's setting for the pessimistic case.

    Reference points: the perpetual cost of capital is the bond rate plus 4.5 points, about 9.28%
    at today's rates; the return the accounts show today is 6.8% on all capital and 22.6% once
    goodwill is set aside; this case's own year 10 earns about 13.5% (computed; dry run). With no
    premium the perpetual reinvestment the model charges is growth divided by the cost of capital,
    about half of after-tax operating profit at today's rates, against about a fifth in the last
    modelled year, so cash flow steps down by about a third into the terminal year. The step cannot
    be removed without giving this case a premium, which the method forbids here; the engine reports
    it for the bear and does not flag it, because it is a property of assuming the advantage is
    completely gone.

### Base: reasons

- **Revenue growth** — Years 1 and 2 come from the two revenue figures management has given, roughly 12 billion this fiscal year and approximately 18 billion next, and year 3 from its custom target of over 10 billion in fiscal 2029, which the chief executive says now carries 'a lot of upside bias' (outlook.md section 4). Years 4 and 5 slow the custom and optics ramps as the first programs reach full volume, so growth is still three times the economy's in year 5 rather than back to it. [Q2 FY2027 call; Q2 FY2027 release; Q2 FY2027 slides, p.8; Q1 FY2027 call; 8-K 2026-08-19]

    The run-rate the path starts from: the latest quarter is up 37% (2,739.3 against 2,006.1) and the
    trailing twelve months up 31% (9,450.3 against 7,234.9) [Q2 FY2027 supplemental, p.5]. What moves
    year 1 above it, each a named item in the latest filings: the third quarter is guided to 3,150,
    15% above the second and more than 50% above a year earlier; the fourth is expected 'to further
    accelerate'; fiscal 2027 is 'roughly 12 billion', so its second half is 12,000 less the 5,157.1
    already reported, or 6,843; and fiscal 2028 is 'approximately 18 billion', up about 50%
    [Q2 FY2027 release; Q2 FY2027 call]. Year 1 is that second half plus the first half of fiscal
    2028, built line by line below, 14,904, which is 58% above the base year (computed).
    
    How the year windows are built. Each model year is a twelve-month window ending in early August,
    so it holds the second half of one fiscal year and the first half of the next. Each line's
    first-half share of a fiscal year is set by its own growth pace (steady quarter-on-quarter growth
    gives a first half of 1 divided by 1 plus the square root of 1 plus the year's growth, which is
    45% of a year growing 50%); the reported halves of fiscal 2026 and fiscal 2027 are used where they
    exist, and the first half of fiscal 2027 was 43% of its year [Q2 FY2027 supplemental, p.5; p.10].
    
    The end state, set before the path. In year 10 (the twelve months to about August 2036) Marvell
    sells about 64,300, 6.8 times today's revenue. That is 13% to 14% of the 460,000 to 510,000 that
    the 66 US semiconductor companies in Damodaran's dataset sell today (an inference from the row's
    net capital spending of 22,421, its 4.4% net capital spending to sales and its 14.5% of after-tax
    operating profit at a 33.5% after-tax margin); no competitor revenue figure exists in the cached
    reports or sources, so the sector aggregate stands in for the largest companies [Damodaran
    capex.xls and margin.xls, Semiconductor, 2026-01-05]. Of that revenue, custom at its year-5 share
    of 49% is about 31,400, a 25% share of the custom market carried to year 10 in the diagnostics,
    against the 20% management targets for fiscal 2029; at a market growing 15% a year the share
    would be 20% (computed) [Q1 FY2027 call]. Why this company takes that share against this
    competition: it has 'custom engagements across the board at all the US' hyperscalers (the machine transcript
    truncates the last word), the Google agreement
    covers 'a comprehensive range' of chips that attach to that customer's own processor, and
    management says its attach programs have 'all ... sized up significantly since we won them', while the competition
    is Broadcom and the customers' own design teams, which is why the share is a quarter and not a
    half [Q1 FY2027 call; 8-K 2026-08-19; 10-K FY2026, Item 1]. The path below is backed out from
    that end state through the fiscal-year build.
    
    The fiscal-year build under the current two-segment definition. Marvell reports only data center
    and communications and other [10-Q Q2 FY2027, Note 3]. Inside data center, two lines have a
    sourced anchor and a growth engine of their own, so they are carried separately and labelled as
    our inference: custom (program wins at a few customers with two-year development cycles, sized
    top-down from management's target and market) and switching (share gain in an established
    Ethernet market plus the new scale-up switch market); everything else in data center (optical
    DSPs, TIAs and drivers, DCI modules, scale-up optics, storage, cables and retimers, merchant parts
    that follow cloud spending and speed transitions and share one engine) is one residual line, so
    that no line is split without a basis. Anchors: custom in fiscal 2026 is set at 2,000 so that the
    'more than 20%' fiscal 2027 growth and the 'more than double' fiscal 2028 land where analysts on
    the calls put the business, 'around 5 billion to 6 billion in calendar 27' and 'a little over 4
    billion' for the processors alone, neither disputed by the chief executive [Q1 FY2027 call;
    Q2 FY2027 call]; fiscal 2029 custom is 11,500, management's own arithmetic of 20% of a 55 billion
    market ('11 billion. So call it in that range') with the Google programs contributing 'much more
    significantly in fiscal 29' [Q1 FY2027 call; Q2 FY2027 call]; switching in fiscal 2026 is 300
    because the fiscal 2027 target was 'exceed 600 million, doubling from fiscal 2026', tracking to
    'more than 1 billion in annualized revenue in fiscal 2028' [Q1 FY2027 call]; the residual is data
    center's 6,100.3 less those two, and it includes the DCI modules that did 'roughly 500 million' in
    fiscal 2026 with 'line of sight to a 1 billion annualized revenue during fiscal 28' [10-K FY2026,
    Note 3; Q1 FY2027 call].
    
    | Fiscal year | Custom | Switching | Interconnect and other data center | Data center | Data center growth | Communications and other | Company | Company growth |
    |---|---|---|---|---|---|---|---|---|
    | FY2026 actual | 2,000 | 300 | 3,800 | 6,100 | 46% | 2,094 | 8,195 | 42% |
    | FY2027 | 2,700 | 650 | 6,410 | 9,760 | 60% | 2,250 | 12,010 | 47% |
    | FY2028 | 5,700 | 1,000 | 9,000 | 15,700 | 61% | 2,350 | 18,050 | 50% |
    | FY2029 | 11,500 | 1,400 | 11,300 | 24,200 | 54% | 2,450 | 26,650 | 48% |
    | FY2030 | 15,500 | 1,850 | 13,500 | 30,850 | 28% | 2,550 | 33,400 | 25% |
    | FY2031 | 19,000 | 2,300 | 15,500 | 36,800 | 19% | 2,650 | 39,450 | 18% |
    | FY2032 | 22,000 | 2,700 | 17,200 | 41,900 | 14% | 2,750 | 44,650 | 13% |
    
    Checks on that table against what management said: the company grows 47% in fiscal 2027 against
    'approximately 45%' to 'roughly 12 billion', and 50% in fiscal 2028 against 'approximately 50%'
    to 'approximately 18 billion'; data center grows 60% and 61% against 'approximately 60%' and
    'more than 60%'; custom grows 35% then 111% against 'more than 20%' and 'more than double', and
    reaches 11,500 in fiscal 2029 against 'over 10 billion' with 'upside bias'; the residual grows
    69% in fiscal 2027 against the 'more than 70%' interconnect target that was not restated;
    communications and other grows 7% then 4% against a target it expects to 'approach' this year and
    low single digits next [Q2 FY2027 call; Q1 FY2027 call]. The cumulative custom revenue from
    fiscal 2028 to fiscal 2033 in this build is about 98,500 from all customers, against the 120,000
    of purchases from Google alone that would vest every warrant slice, so this case has Google buying
    at roughly half the pace the warrant allows, the middle of the range the chief executive framed
    when he called full performance 'a monster number' (computed) [8-K 2026-08-19; Q2 FY2027 call].
    
    | Part of the business | Trailing revenue | Latest reported growth | Year 1 growth | Year 3 growth | Year 5 growth |
    |---|---|---|---|---|---|
    | Custom (inference) | 2,147 | dollars not disclosed | up 82% | up 71% | up 19% |
    | Switching (inference) | 423 | dollars not disclosed | up 96% | up 36% | up 21% |
    | Interconnect and other data center (residual) | 4,604 | dollars not disclosed | up 72% | up 22% | up 13% |
    | Data center, as reported | 7,173 | up 46% in the quarter, up 33% on the year | up 76% | up 43% | up 16% |
    | Communications and other, as reported | 2,277 | up 10% in the quarter, up 24% on the year | down 1% | up 4% | up 4% |
    | Company | 9,450 | up 37% in the quarter, up 31% on the year | up 58% | up 39% | up 15% |
    
    Trailing figures for the two reported segments come from the eight-quarter table; the three
    inferred lines are the fiscal build read over the same window, scaled so they sum to the 7,173.4
    of data center revenue actually reported [Q2 FY2027 supplemental, p.10]. Company revenue in the
    five windows: 14,904; 21,932; 30,462; 36,553; 42,182, and the rounded path the engine runs gives
    14,931; 21,949; 30,509; 36,611; 42,103, within a quarter of a percent in every year (computed).
    
    Drivers of each step down of more than three points. Year 1 to year 2, 58% to 47%: fiscal 2027's
    guided second-half surge leaves the window and the doubling of custom in fiscal 2028 is a
    one-time step as the second large processor program and the first attach programs reach volume,
    with the 1.6 terabit optical step inside year 1 as well [Q2 FY2027 call; 8-K 2026-08-19]. Year 2
    to year 3, 47% to 39%: fiscal 2029 is the last year with a custom target, its step from 5,700 to
    11,500 is smaller in proportion than the doubling before it, and interconnect moderates to 26%
    as cloud capital spending growth eases into 'the 30%-plus range' management planned for a
    quarter earlier [Q1 FY2027 call; Q2 FY2027 call]. Year 3 to year 4, 39% to 20%: the first wave
    of programs (the flagship processor, the new top-tier processor and the Google attach chips) is
    at full volume by fiscal 2030, so the business grows with its customers' capacity plans rather
    than with a ramp [Q1 FY2027 call]. Year 4 to year 5, 20% to 15%: the 1.6 terabit optical
    generation matures and the shift of scale-up links from copper to light, which management says
    will 'take several years with both technologies coexisting', is by then priced into the base,
    while custom slows to 16% as its share of its market nears a quarter [Q2 FY2027 call]. After year
    5 the engine fades growth in a straight line to the bond rate by year 10.
    
    Growth agrees with margin: half of year-5 revenue is custom silicon, which carries a lower gross
    margin than merchant parts, so the margin path below flattens rather than climbing toward the top
    of the industry; a niche-margin story is not being asked to carry mass-market revenue. Is it
    plausible: the margin and reinvestment paths below are built from the cost structure in
    business.md sections 3 and 4, where the design bill is fixed and most of the investment is
    working capital. Is it probable: the scorecard shows 10 of 12 claims met last quarter and both
    full-year figures raised twice in a row; the fiscal 2029 custom figure dates from June 2025 and
    the April 2024 version of the same target was about 8 billion, so the target has been raised once
    and repeated since, and this quarter the chief executive added that custom numbers for fiscal
    2029 and beyond 'definitely go higher' than anything modelled before the warrant (scorecard.md;
    outlook.md section 6) [Q2 FY2027 call; Q1 FY2027 call].
- **Operating margin** — The reported margin roughly doubles from today's 16.5% to 35%, which is the average operating margin of the US semiconductor industry, and both halves of the climb come out of the accounts: the yearly write-down of past acquisitions falls from 9.4 points of revenue to almost nothing, and operating expenses grow at about half the rate of revenue, which is what management has told investors to expect (business.md section 3; outlook.md section 4). The shift toward lower-margin custom silicon takes about three points off gross margin by year 5, which is why the path flattens at the industry average instead of climbing past it. [Q2 FY2027 call; Q2 FY2027 release; 10-Q Q2 FY2027, Note 5; Q2 FY2027 supplemental, p.5; Damodaran margin.xls, Semiconductor, 2026-01-05]

    Where the target sits. Damodaran's US semiconductor row earns a 35.3% operating margin after
    share pay and amortization, 40.4% before share pay, on a 59.0% gross margin with research at
    15.4% of sales and share pay at 5.0%; the neighbouring rows read 33.0% for system and application
    software, 26.2% for semiconductor equipment and 12.8% for the whole market [Damodaran margin.xls,
    2026-01-05]. Marvell's own best reported year was 16.1% (FY2026) and the latest quarter 16.8%;
    its worst was minus 12.5% (FY2025); its adjusted margin was 35.3% in FY2026 and 36.6% in the
    latest quarter, and management's target is 38% to 40% adjusted, 'likely to enter' that range
    this quarter, at 'the upper end' through fiscal 2028, and about to be 'reset' at the October 6
    Investor Day (business.md section 3) [Q2 FY2027 release; Q2 FY2027 call]. The year-5 reported
    margin of 35% therefore places the base case at the industry average on the reported measure and,
    at 42% adjusted, just above the industry's 40.4% before share pay and above management's current
    38% to 40%: Marvell becomes an average-margin US semiconductor company, not a top-decile one,
    because half its sales are custom chips at thinner gross margins. Named comparables from
    business.md (Broadcom) carry no margin figure in the cached sources, so the industry rows stand
    in for them.
    
    Growth spending inside today's costs, named before the path is set: research is 25.8% of revenue
    against the industry's 15.4%, and new custom chips take 'approximately 2 years' to reach revenue,
    so roughly ten points of today's costs are design work for sales that have not arrived; the path
    below has adjusted operating expenses falling from 21.2% of revenue to 13.4% by fiscal 2032, at
    which point research plus selling costs including share pay are about 20% of revenue against the
    industry's 21.5% [Damodaran margin.xls, Semiconductor, 2026-01-05; Q1 FY2027 call].
    
    The bridge in two steps: first the company's own adjusted margin by fiscal year, then the three
    costs that version leaves out but this model keeps, converted to the model's windows.
    
    | Fiscal year | Adjusted gross margin | Adjusted operating expenses | Expenses over revenue | Adjusted operating margin | Share-based pay | Custom share of revenue |
    |---|---|---|---|---|---|---|
    | FY2027 | 58.5% | 2,550 | 21.2% | 37.3% | 1,164 | 22% |
    | FY2028 | 58.0% | 3,190 | 17.7% | 40.3% | 1,450 | 32% |
    | FY2029 | 57.0% | 4,200 | 15.8% | 41.2% | 1,850 | 43% |
    | FY2030 | 56.5% | 4,900 | 14.7% | 41.8% | 2,200 | 46% |
    | FY2031 | 56.0% | 5,500 | 13.9% | 42.1% | 2,500 | 48% |
    | FY2032 | 55.5% | 6,000 | 13.4% | 42.1% | 2,750 | 49% |
    
    Fiscal 2027 expenses are management's own 'approximately 2.55 billion' and the quarters check
    out: 576.9 reported in the first, 610.8 in the second, 655 guided for the third, leaving about 707
    for the fourth, which puts the fourth-quarter adjusted operating margin near 39%, matching 'likely
    to enter our 38% to 40% long-term target range in Q4' [Q2 FY2027 release; Q2 FY2027 call]. Fiscal
    2028 expenses grow 25%, half the guided 50% revenue growth, exactly as management said they would;
    from fiscal 2029 they grow at about two-thirds of revenue growth, because nothing beyond fiscal
    2028 is guided and design teams have to be added to hold a quarter of the custom market
    [Q2 FY2027 call]. Gross margin: the first half of fiscal 2027 was 59.0%, the third quarter is
    guided to 57.5% to 58.5%, the fourth 'in this range' and fiscal 2028 'in a similar range', so
    58.5% and 58.0%; after that it is carried down half a point a year as custom rises to half of
    revenue, which is what a mix of merchant parts at about 61% and custom at about 50% produces
    (an inference: 22% custom gives 58.6%, 49% gives 55.6%) [Q2 FY2027 release; Q2 FY2027 call].
    
    | Model year | Adjusted operating margin | Less share-based pay | Less acquisition write-downs | Less write-down of acquired research | Less restructuring and deal costs | Reported margin | Used |
    |---|---|---|---|---|---|---|---|
    | 1 | 39.6% | 8.6 | 3.6 | 0.2 | 0.3 | 26.9% | 27% |
    | 2 | 40.9% | 7.4 | 1.0 | 0.4 | 0.3 | 31.8% | 32% |
    | 3 | 41.4% | 6.7 | 0.4 | 0.4 | 0.3 | 33.6% | 34% |
    | 4 | 41.9% | 6.5 | 0.2 | 0.4 | 0.3 | 34.5% | 35% |
    | 5 | 42.1% | 6.2 | 0.1 | 0.4 | 0.3 | 35.0% | 35% |
    
    Each row is rounded to the nearest whole point, in whichever direction it falls; the previous
    draft rounded every row down, which the method treats as a bias rather than caution. The target
    is reached in year 4 and held, so nothing is still moving in year 5, and the engine holds 35%
    through year 10.
    
    What drags. Custom silicon carries a lower gross margin than the standard parts: the chief
    financial officer named mix as 'the primary driver' of the guided step down to 57.5% to 58.5%
    from 58.9%, and the board cut the fiscal 2026 gross-margin bonus target for 'the expected
    near-term product mix shift' to support 'competitive pricing, volume commitments, and start-up
    investments to capture share in the data center AI market' [Q2 FY2027 call; DEF 14A 2026, CD&A].
    Share-based pay is the largest single deduction and it is not guided: it was 326.2 in the latest
    quarter, more than double a year earlier, with 190.1 of acquired-company awards still to be
    charged; this path grows it with operating expenses, from 1,164 in fiscal 2027 to 2,750 in fiscal
    2032, so it falls from 8.8% of revenue today to 6.2%, still above the industry's 5.0%
    [Q2 FY2027 supplemental, p.5; 10-Q Q2 FY2027, Note 10; Damodaran margin.xls, Semiconductor,
    2026-01-05]. Research bought in acquisitions but not yet in use, 1,297.0, starts being written off
    over 6 to 13 years as those products ship, taken at 60 in fiscal 2028 rising to 150 a year by
    fiscal 2031 (an inference inside the 100 to 216 range), and restructuring and deal costs run at
    0.3% of revenue, their trailing rate [10-Q Q2 FY2027, Note 5; Q2 FY2027 supplemental, p.8].
    
    What offsets. Operating leverage is already visible: the adjusted operating margin was 36.6% in
    the latest quarter, up 1.8 points on the year and 1.6 on the quarter on an unchanged gross
    margin, and management expects revenue to keep 'growing substantially faster than operating
    expenses' [Q2 FY2027 call]. The write-down of acquired technology falls on a schedule already in
    the accounts: 385.3 for the rest of fiscal 2027, then 292.7, 139.6, 117.2, 60.8 and 54.0 after
    that, so it drops from 9.4 points of revenue in the base year to 0.1 by year 5 [10-Q Q2 FY2027,
    Note 5]. Depreciation is a tailwind, not a drag: at capital spending of 4.5% of revenue it runs
    443, 531, 637, 765 and 918 over years 1 to 5, falling from 3.9% of revenue today to 2.2%, worth
    about 1.7 points inside the operating-expense line (computed from the reinvestment table)
    [10-Q Q2 FY2027, Item 1]. Mix within the merchant lines helps too: scale-up optics and switching
    are merchant products at merchant margins, and management expects gross margin 'in a similar
    range' next year even as custom doubles [Q2 FY2027 call].
- **Sales-to-capital** — Each dollar Marvell invests supports about 2.20 of new sales through year 5, which is what the forward arithmetic gives when most of the investment is money tied up in stock and unpaid customer bills rather than in factories, and it sits below Marvell's own lagged organic record and above the industry's 1.21 (business.md section 3). The later figure of 1.10 sits a little below the 1.3 the fade-year arithmetic gives once the story's acquisitions are counted, and it is chosen as a pair with the eight-point terminal premium: together they make the year-10 return about twice the perpetual return, which is what the story's last sentence says and what the method's transition test requires, whereas at 1.3 the pair would need a nine-point premium and an exception to the method's ceiling. [10-K FY2024, Item 8; 10-K FY2026, Item 8; 10-Q Q2 FY2027, Item 1; Note 4; Note 14; Damodaran capex.xls, Semiconductor, 2026-01-05]

    Measured the way the model spends the money. This model assumes what is spent in one year buys
    the next year's growth, so the record below divides each year's investment into the following
    year's revenue increase. Investment is capital spending less depreciation, plus the increase in
    working capital (the six operating lines of the cash-flow statement), plus cash paid for
    acquisitions.
    
    | Fiscal year of spending | Capital spending | Depreciation | Working capital increase | Cash for acquisitions | Investment, with deals | Investment, without deals | Next year's revenue increase | Lagged ratio, with deals | Lagged ratio, without deals |
    |---|---|---|---|---|---|---|---|---|---|
    | FY2022 | 169.2 | 265.9 | 662.9 | 3,555.0 | 4,121.2 | 566.2 | 1,457.2 | 0.35 | 2.6 |
    | FY2023 | 206.2 | 304.9 | 649.8 | 112.3 | 663.4 | 551.1 | minus 411.9 | not meaningful | not meaningful |
    | FY2024 | 336.3 | 299.8 | minus 57.8 | 0 | minus 21.3 | minus 21.3 | 259.6 | not meaningful | not meaningful |
    | FY2025 | 284.6 | 304.3 | minus 129.1 | 10.4 | minus 138.4 | minus 148.8 | 2,427.3 | not meaningful | not meaningful |
    | FY2026 | 354.1 | 348.6 | 1,108.3 | 0 | 1,113.8 | 1,113.8 | 3,805.4 | 3.4 | 3.4 |
    | Five years together | 1,350.4 | 1,523.5 | 2,234.1 | 3,677.7 | 5,738.7 | 2,061.0 | 7,537.6 | 1.3 | 3.7 |
    
    Sources for the table: fiscal 2022 and 2023 [10-K FY2024, Item 8]; fiscal 2024 to 2026 [10-K
    FY2026, Item 8]; the fiscal 2027 revenue increase uses the 'roughly 12 billion' guide [Q2 FY2027
    call]. Reading it: in the two years where Marvell invested a positive amount and revenue then
    rose, the lagged ratio was 2.6 and 3.4; two years show investment below zero because capital
    spending was under depreciation and working capital came back, and revenue then rose anyway,
    which is the mark of a company that invested ahead of its growth in fiscal 2022 and 2023; over the
    five years together the ratio is 3.7 without deals and 1.3 with them.
    
    The three candidates and where the numbers land.
    
    | Candidate | Figure | Where it comes from |
    |---|---|---|
    | Marvell's own lagged record | 2.6 and 3.4 organic; 1.3 over five years with acquisitions | the table above |
    | Last year's marginal lagged ratio | 3.4 for fiscal 2026 spending against the fiscal 2027 guide; about 0.95 for fiscal 2027 spending including Celestial and XConn against the fiscal 2028 guide, or 2.35 without those deals | the table above; fiscal 2027 spending estimated as 1,332 of working capital, 220 of capital spending net of depreciation, 1,000 of prepayments, 1,270.9 of deal cash and about 2,500 of deal shares [10-Q Q2 FY2027, Note 4; Q2 FY2027 call] |
    | The industry average | 1.21 | [Damodaran capex.xls, Semiconductor, 'Sales/ Invested Capital (LTM)', 2026-01-05] |
    | Chosen, years 1 to 5 | 2.2 | at the forward component build below; below the organic record, above the industry |
    | Chosen, years 6 to 10 | 1.1 | just below the 1.3 the fade-year arithmetic with acquisitions gives; set as a pair with the eight-point premium so that year 10 earns about twice the perpetual return |
    
    The forward arithmetic that sets 2.2. Each new dollar of revenue has recently taken 31 to 46
    cents of working capital: 34 cents on the balance-sheet measure in fiscal 2026 (working capital
    of 1,101.1 against 274.7 a year earlier on 2,427.3 of added revenue), 31 cents from then to the
    latest quarter (1,487.0 on 1,255.7 of added revenue) and 46 cents on the cash-flow measure in
    fiscal 2026, which also carries non-working-capital items; 35 cents is used [10-K FY2026, Item 8;
    10-Q Q2 FY2027, Item 1]. Capital spending has run 3.5% to 6.1% of revenue over five fiscal years
    and 5.0% in the trailing year (470.2), with 351.6 of commitments mostly due within a year, so 4.5%
    is used; depreciation is 368.8 in the trailing year and is grown 20% a year as that spending
    accumulates [10-K FY2026, Item 8; 10-Q Q2 FY2027, Item 1; Note 9].
    
    | Model year | Revenue | Next year's revenue increase | Working capital at 35 cents | Capital spending at 4.5% | Depreciation | Capital spending net of depreciation | Factory prepayments | Forward investment | Forward ratio |
    |---|---|---|---|---|---|---|---|---|---|
    | 1 | 14,931 | 7,018 | 2,456 | 672 | 443 | 229 | 1,000 | 3,686 | 1.9 |
    | 2 | 21,949 | 8,560 | 2,996 | 988 | 531 | 457 | none guided | 3,453 | 2.5 |
    | 3 | 30,509 | 6,102 | 2,136 | 1,373 | 637 | 736 | none guided | 2,871 | 2.1 |
    | 4 | 36,611 | 5,492 | 1,922 | 1,648 | 765 | 883 | none guided | 2,805 | 2.0 |
    | 5 | 42,103 | 5,455 | 1,909 | 1,895 | 918 | 977 | none guided | 2,886 | 1.9 |
    
    Years 2 to 5 average 2.1, so 2.2 is the forward build, not a discount to the record; year 1 is
    handled by the override below. In the fade years the same arithmetic gives 1.6 to 1.8 organically
    (revenue increases shrink toward the bond rate while capital spending stays at 4.5% of a larger
    base); adding technology acquisitions at Marvell's own pace, about 3.5 billion every five years
    against revenue increases of 3,000 to 5,000 a year, takes about 0.17 more per new dollar and
    brings the ratio to about 1.3 (computed). The late ratio is set at 1.1 rather than 1.3 as a pair
    with the eight-point terminal premium, and that pairing, not convergence to the industry, is what
    drives it: at 1.3 the year-10 return is about 35% and a perpetual return of about 17.3% would fall
    below half of it, which the engine flags as a cliff; at 1.1 the year-10 return is 33.5% and the
    pair holds, with cash flow stepping down about 9% into the terminal year. The alternative, 1.3
    with a nine-point premium (about 18.3%), also holds, with a step of about 10%, but it needs an
    exception to the method's eight-point ceiling for the base case; that choice is left to the owner
    (computed; dry run).
    
    What the chosen ratio implies for capital spending, the test that matters because a ratio can
    quietly demand more equipment than the company has ever bought: charging 3,891, 2,774, 2,496 and
    2,479 in years 2 to 5 and taking off working capital at 35 cents and adding back depreciation
    leaves gross capital spending of 1,426, 1,275, 1,339 and 1,488, or 6.5%, 4.2%, 3.7% and 3.5% of
    revenue, inside the 3.5% to 6.1% record except year 2, which sits at its top because revenue
    growth is slowing while spending is still catching up (computed) [10-K FY2026, Item 8].
    
    The implied return on capital check, from the dry run at these settings. The return on all
    invested capital rises from 17.6% in year 1 to about 39% in year 5 and 40% in year 6, then falls
    to about 33.5% in year 10 as the fade-year investment at 1.1 accumulates, against a cost of
    capital falling from 10.9% to 9.3%. The US semiconductor industry earns about 40.5% today
    (after-tax margin 33.5% times sales to capital 1.21) and Marvell earns 22.6% on its capital
    excluding goodwill, so a year-10 return in the low to mid thirties sits below the industry's
    return at any late ratio between 1.1 and 1.5 (33.5%, 35.1% and 36%); convergence therefore does
    not separate those choices, and the terminal pairing above does (computed; dry run) [Damodaran
    margin.xls and capex.xls, Semiconductor, 2026-01-05].
    
    One caveat for the owner. The model assumes a one-year gap between spending and sales; the
    capacity reservations run 4 to 10 years and unconditional commitments to foundries tripled to
    8,518.9 in one quarter, so some of today's cash is buying revenue two or three years out
    [10-Q Q2 FY2027, Note 9; 10-K FY2026, Note 8]. The record above is measured on the same one-year
    basis as the model, so the two are consistent; a longer gap would raise both.
- **Reinvestment override** — Year 1 is set in dollars because management has named a spending level the ratio does not cover: about 1 billion of factory prepayments this fiscal year, with deposits running in quarterly installments into the first half of next (outlook.md section 4). The figure is after subtracting depreciation, and later years go back to the ratio because no spending beyond this year is guided. [Q2 FY2027 call; 10-Q Q2 FY2027, Note 14; Item 1; 10-Q Q1 FY2027, Note 9]

    Year 1 = extra working capital of about 2,456, being 35 cents on each dollar of the following
    year's revenue increase of 7,018, plus about 1,000 of capacity prepayments falling inside the
    window, plus about 229 of capital spending net of depreciation (672 at 4.5% of revenue less 443),
    which is 3,686, taken as 3,700 (computed) [Q2 FY2027 call; 10-Q Q2 FY2027, Note 14]. The
    prepayments: management is 'on pace to make approximately 1 billion of capacity prepayments to
    suppliers in fiscal 2027' (dollar sign written as a word), the balance rose 223.9 in the second
    quarter to 487.0, and the 870.0 of deposits agreed in May are 'payable in quarterly installments
    from the second quarter of fiscal 2027 through the second quarter of fiscal 2028', so the year-1
    window holds the roughly 776 left of the fiscal 2027 figure plus two more quarterly installments
    of about 174, less an allowance of about 125 for prepayments applied against wafer purchases
    before the window ends: about 1,000, an expected figure rather than the upper bound the previous
    draft used (computed) [Q2 FY2027 call; 10-Q Q2 FY2027, Note 14; 10-Q Q1 FY2027, Note 9]. The
    ratio on its own would have charged 3,190, so the override adds about 500 to year 1; without it
    the model would spend less in the one year management has told us what it is spending. Because
    prepayments are later applied against purchases, part of this cash comes back as lower working
    capital in years 2 and 3; the effect is small next to 6,000 to 8,500 of yearly revenue growth and
    is left inside the ratio.
- **Tax rate** — Starts at management's own estimate of tax on continuing profits for fiscal 2028, approximately 13%, the figure explained in the base-year tax cell, and rises to the 25% rate the model uses once a company is mature. The rise is a real cost in this case, because it lands when profits are largest. [Q2 FY2027 call]
- **Terminal growth** — The ten-year government bond rate fetched for the run, as the method requires: no company outgrows the economy forever.
- **Terminal return on capital premium** — Eight points above the cost of capital, so Marvell keeps earning a return in the high teens forever: custom designs lock a customer in for a whole chip generation, the optical business has been first to each speed step, and the largest custom customer is now tied in by a warrant that only pays off if it keeps buying through 2033 (business.md section 5; outlook.md section 3). That is about half of what the business earns at the end of the forecast, below what it earns today on the capital behind its designs, and a quarter of the way from the cost of capital toward the return the US semiconductor industry earns now, which is where a company with real but shared advantages in a high-return industry belongs.

    Where the number sits. The cost of capital in perpetuity is the bond rate plus the 4.5-point
    mature-market premium, about 9.28% at today's rates, so eight points on top puts the perpetual
    return at the bond rate plus 12.5 points, about 17.3% today. Reference points: the return the
    accounts show today is 6.8%, being after-tax operating profit of 1,358.3 on invested capital of
    19,884.9, but 13,873.9 of that capital is goodwill from past deals and business.md section 4
    makes exactly this point, that the return that matters is on each new design dollar; excluding
    goodwill the same profit is a 22.6% return; this case's own year 10 earns about 33.5% on the
    engine's measure, which includes the goodwill and every dollar reinvested; and the US
    semiconductor industry earns about 40.5% today (after-tax margin 33.5% times sales to capital
    1.21) [10-Q Q2 FY2027, Item 1; Damodaran margin.xls and capex.xls, Semiconductor,
    2026-01-05]. So the perpetual return sits below both returns that describe the operating
    business and above the cost of capital; it sits above the 6.8% the accounts show on all capital,
    the one comparison the method would normally want the other way round, and it is flagged here
    rather than left buried: the judgment is that a balance sheet three-quarters made of past
    acquisition prices is not the right yardstick for the return on tomorrow's designs.
    Why eight and not the seven the previous draft used, or the eleven the bull case carries: Damodaran gave Alphabet, Amazon and Apple seven points in industries that earn
    in the twenties on book capital; semiconductor designers earn twice that on book capital because
    the factories belong to someone else, so an eight-point premium is a modest position in this
    industry's distribution; against it, ten customers were 82% of fiscal 2026 revenue, one
    distributor 44% of the latest quarter, and the 10-K warns that 'some large customers may begin
    developing and making their own semiconductor solutions', which is why it is not the eleven
    the bull case carries [10-K FY2026, Item 1A; 10-Q Q2 FY2027, Item 2]. Seven points would put the
    terminal return below half of year 10's and the engine would flag a cliff; the playbook says
    that is an error, not caution. The late sales-to-capital ratio of 1.1 is chosen with this
    premium as a pair, as that cell explains.
    Transition into perpetuity: the perpetual reinvestment charge is growth divided by that return,
    about 28% of after-tax operating profit, against about 17% in the last modelled year, so cash
    flow steps down about 9% in the terminal year and the terminal return of about 17.3% is just
    above half of year 10's 33.5%, so the engine's cliff test passes on both counts (computed; dry
    run). A step of that size is normal for this method.

### Bull: reasons

- **Revenue growth** — This case takes both guided years at the top of their ranges and then lets the custom business run near the pace the Google warrant implies, with the fiscal 2029 target beaten rather than met and scale-up optics and switching becoming a second business the size of today's company (outlook.md sections 3 and 6). Growth still falls by two-thirds over the five years, because even here the first wave of programs reaches full volume and custom becomes a third of its market. [Q2 FY2027 call; Q2 FY2027 release; 8-K 2026-08-19; Q1 FY2027 call; Q2 FY2027 supplemental, p.10]

    The run-rate the path starts from is the same as in the base case: up 37% in the latest quarter
    and 31% on the trailing twelve months [Q2 FY2027 supplemental, p.5]. What moves year 1: the
    guided third quarter taken near the top of its range (3,308) and a fourth quarter of 3,985, so
    fiscal 2027 is 12,450 against 'roughly 12 billion', and a fiscal 2028 of 19,600 against
    'approximately 18 billion', the case where management under-calls again as it has 'to date'
    [Q2 FY2027 release; Q2 FY2027 call]. Windows and the three inferred data-center lines are built
    exactly as in the base case, whose notes give the anchors and the method; the trailing figures for
    the two reported segments come from the eight-quarter table [10-Q Q2 FY2027, Note 3; Q2 FY2027
    supplemental, p.10].
    
    The end state, set before the path. In year 10 Marvell sells about 103,000, 10.9 times today's
    revenue, which is 20% to 22% of the 460,000 to 510,000 that the 66 US semiconductor companies in
    Damodaran's dataset sell today (the inference explained in the base case): one of the two or three
    largest chip companies in the world by today's yardstick [Damodaran capex.xls and margin.xls,
    Semiconductor, 2026-01-05]. Custom at its year-5 share of 52% is about 53,000, a 42% share of the
    custom market carried forward at the industry rate in the diagnostics, or 34% if that market grows
    15% a year; either way this case only works if the custom market turns out much larger than the
    June 2025 sizing, which is what the chief executive claims when he says 'all of our projections
    to date have been under called' (computed) [Q2 FY2027 call; Q1 FY2027 call]. The cumulative custom
    revenue from fiscal 2028 to fiscal 2033 in this build is about 144,500 from all customers against
    the 120,000 of purchases that would vest every Google warrant slice, so this is the case where
    Google runs near full performance and the other customers add a fifth on top: the 'monster number'
    the chief executive was invited to correct and did not (computed) [8-K 2026-08-19; Q2 FY2027 call].
    
    | Fiscal year | Custom | Switching | Interconnect and other data center | Data center | Data center growth | Communications and other | Company | Company growth |
    |---|---|---|---|---|---|---|---|---|
    | FY2026 actual | 2,000 | 300 | 3,800 | 6,100 | 46% | 2,094 | 8,195 | 42% |
    | FY2027 | 2,800 | 700 | 6,700 | 10,200 | 67% | 2,250 | 12,450 | 52% |
    | FY2028 | 6,200 | 1,250 | 9,750 | 17,200 | 69% | 2,400 | 19,600 | 57% |
    | FY2029 | 13,500 | 2,000 | 13,500 | 29,000 | 69% | 2,550 | 31,550 | 61% |
    | FY2030 | 22,000 | 3,000 | 17,500 | 42,500 | 47% | 2,700 | 45,200 | 43% |
    | FY2031 | 29,000 | 4,000 | 21,000 | 54,000 | 27% | 2,850 | 56,850 | 26% |
    | FY2032 | 34,000 | 5,000 | 24,000 | 63,000 | 17% | 3,000 | 66,000 | 16% |
    
    | Part of the business | Trailing revenue | Latest reported growth | Year 1 growth | Year 3 growth | Year 5 growth |
    |---|---|---|---|---|---|
    | Custom (inference) | 2,138 | dollars not disclosed | up 96% | up 93% | up 23% |
    | Switching (inference) | 431 | dollars not disclosed | up 123% | up 54% | up 28% |
    | Interconnect and other data center (residual) | 4,605 | dollars not disclosed | up 84% | up 34% | up 17% |
    | Data center, as reported | 7,173 | up 46% in the quarter, up 33% on the year | up 90% | up 60% | up 21% |
    | Communications and other, as reported | 2,277 | up 10% in the quarter, up 24% on the year | flat | up 6% | up 5% |
    | Company | 9,450 | up 37% in the quarter, up 31% on the year | up 68% | up 55% | up 20% |
    
    Company revenue in the five windows: 15,920; 24,767; 38,282; 51,458; 61,831, against the rounded
    path's 15,877; 24,767; 38,389; 51,442; 61,730, within a third of a percent in every year
    (computed). The interconnect residual and switching lines together are about 29,000 in
    fiscal 2032 against a whole company of 9,450 today, which is the story's 'second business as large
    as all of Marvell today' (computed).
    
    Drivers of each step down of more than three points. Year 1 to year 2, 68% to 56%: the first
    doubling of custom is inside year 1 and the 1.6 terabit optical step largely is too
    [Q2 FY2027 call]. Year 3 to year 4, 55% to 34%: the fiscal 2029 custom step, the one management
    says will 'accelerate significantly' as the Google programs 'contribute much more significantly
    in fiscal 29', is the largest and cannot repeat, and from fiscal 2030 growth follows the scale-up
    optics and switching ramp rather than a processor ramp [Q2 FY2027 call]. Year 4 to year 5, 34% to
    20%: custom is above 30 billion and about a third of its market, so it can no longer grow much
    faster than that market, and the first generation of scale-up optical links is installed
    [Q1 FY2027 call]. After year 5 the engine fades growth to the bond rate by year 10.
    
    Growth agrees with margin: this case carries mass-market revenue, half of it custom at thinner
    gross margins, and its margin path below peaks above the industry average and then drifts back
    toward it rather than staying at a niche level. Is it plausible: the margin path stays inside the
    cost structure in business.md section 3 and converges to the industry. Is it probable: management
    has raised both full-year figures twice running and 10 of 12 claims were met last quarter, but it
    has never published a number this large, which is why this case carries a quarter of the weight
    (scorecard.md).
- **Operating margin** — Margins pass the 38% to 40% adjusted target management is about to replace, reaching the mid-forties adjusted and 40% reported by year 4, above the US semiconductor industry's 35.3% average, because a design bill that grows at half the rate of sales is spread over a business six times larger (outlook.md sections 2 and 4). The fade years are written out because the story moves them: a margin above the industry average invites entry and price pressure from customers who design their own chips, so it drifts back to 36% by year 10, just above the industry average, and share-based pay and the write-down of old acquisitions shrink to about five points of revenue between them. [Q2 FY2027 call; 10-Q Q2 FY2027, Note 5; Q2 FY2027 supplemental, p.5; 10-K FY2026, Item 1A; Damodaran margin.xls, Semiconductor, 2026-01-05]

    Where the target sits. The industry rows are given in the base case: 35.3% for US semiconductors
    after share pay and amortization, 40.4% before share pay, 33.0% for software, 26.2% for
    semiconductor equipment [Damodaran margin.xls, 2026-01-05]. A 40% reported margin (45.6%
    adjusted) puts this case above the semiconductor average and above management's current target,
    in the upper part of the industry's distribution though far from the leader's, which the cached
    sources do not quantify; Marvell's own best adjusted margin was 36.6% in the latest quarter
    [Q2 FY2027 release]. The business-model argument: a fabless designer's cost of the next chip is
    the factory invoice alone, so once the design bill is spread over ten times the revenue the
    operating margin approaches the gross margin less a shrinking expense ratio; the argument against
    a higher figure is that the customers are a handful of giants who 'may begin developing and making
    their own semiconductor solutions' and press on 'average unit selling prices', which is why the
    margin drifts back after year 5 [10-K FY2026, Item 1A].
    
    | Fiscal year | Adjusted gross margin | Adjusted operating expenses | Expenses over revenue | Adjusted operating margin | Share-based pay | Custom share of revenue |
    |---|---|---|---|---|---|---|
    | FY2027 | 58.5% | 2,550 | 20.5% | 38.0% | 1,164 | 22% |
    | FY2028 | 58.0% | 3,315 | 16.9% | 41.1% | 1,510 | 32% |
    | FY2029 | 57.0% | 4,300 | 13.6% | 43.4% | 1,960 | 43% |
    | FY2030 | 56.5% | 5,200 | 11.5% | 45.0% | 2,370 | 49% |
    | FY2031 | 56.0% | 5,900 | 10.4% | 45.6% | 2,680 | 51% |
    | FY2032 | 55.5% | 6,500 | 9.8% | 45.7% | 2,950 | 52% |
    
    | Model year | Adjusted operating margin | Less share-based pay | Less acquisition write-downs | Less write-down of acquired research | Less restructuring and deal costs | Reported margin | Used |
    |---|---|---|---|---|---|---|---|
    | 1 | 40.5% | 8.2 | 3.3 | 0.2 | 0.3 | 28.6% | 29% |
    | 2 | 42.4% | 6.9 | 0.9 | 0.3 | 0.3 | 34.0% | 34% |
    | 3 | 44.2% | 5.7 | 0.3 | 0.3 | 0.3 | 37.5% | 38% |
    | 4 | 45.3% | 5.0 | 0.2 | 0.3 | 0.3 | 39.6% | 40% |
    | 5 | 45.6% | 4.6 | 0.1 | 0.2 | 0.3 | 40.4% | 40% |
    | 6 to 10 | drifting to about 41% | about 4.5 | none | about 0.2 | 0.3 | 39%, 38%, 38%, 37%, 36% | as listed |
    
    Each explicit year is rounded to the nearest whole point. Operating expenses grow at half the
    rate of revenue in fiscal 2028 as guided and at about half of it afterwards too, because in this
    case the programs are already won and the design teams already hired, which on this revenue path
    takes them from 21% of sales to under 10% [Q2 FY2027 call]. Gross margin follows the same mix
    rule as the base case: custom rises to half of revenue and the merchant scale-up optics and
    switches hold the rest at merchant margins, so 55.5% by fiscal 2032 [Q2 FY2027 call].
    
    What drags. The same custom-mix effect as the base case; share-based pay grows with operating
    expenses from 1,164 to 2,950, falling from 8.8% of revenue to 4.6%, roughly the industry's 5.0%,
    and the 1,297.0 of acquired research not yet in use starts being written off as products ship
    [Q2 FY2027 supplemental, p.5; 10-Q Q2 FY2027, Note 5; Damodaran margin.xls, Semiconductor,
    2026-01-05]. In the fade years the drag is competition: with the reported margin above the
    industry average and growth slowing, customers who design their own chips press on price, so the
    path gives back four points by year 10 [10-K FY2026, Item 1A].
    What offsets. The adjusted operating margin was already 36.6% in the latest quarter, up 1.8
    points on the year, management expects the fourth quarter to enter the target range and the
    upper end of it through fiscal 2028, and the write-down of acquired technology runs off on the
    schedule in the accounts, from 9.4 points of revenue to nothing that matters [Q2 FY2027 call;
    10-Q Q2 FY2027, Note 5]. Depreciation at 4.5% capital spending falls from 3.9% of revenue to 1.5%
    by year 5 on this revenue path, a tailwind of more than two points inside the expense line
    (computed from the reinvestment arithmetic in the base case).
- **Sales-to-capital** — Each dollar of investment supports 2.20 of new sales here as in the base case, because the forward arithmetic is the same (35 cents of working capital and 4.5% of revenue in capital spending) and the growth comes from programs already won on capacity already reserved, paid for out of cash flow rather than by buying companies (business.md section 5). The later figure of 1.30 sits between the organic fade-year arithmetic and the industry's 1.21, and it is the level at which the year-10 implied return meets the 40.5% the US semiconductor industry earns today rather than running past it. [10-K FY2024, Item 8; 10-K FY2026, Item 8; 10-Q Q2 FY2027, Item 1; Note 9; Damodaran capex.xls, Semiconductor, 2026-01-05]

    The three candidates and the measured record are in the base case: organic lagged ratios of 2.6
    and 3.4, 1.3 over five years including deals, a marginal ratio of 3.4 (2.35 for fiscal 2027
    spending without deals), and an industry figure of 1.21. The forward arithmetic on this case's
    revenue path gives 2.5, 2.3, 2.0 and 1.9 in years 2 to 5 (working capital of 4,768, 4,568, 3,601
    and 3,663 at 35 cents, capital spending of 1,115 to 2,778 at 4.5% of revenue, depreciation of 531
    to 918), an average of 2.2, and 1.1 to 1.8 in the fade years as revenue increases shrink toward
    the bond rate, an average of 1.4 (computed). No acquisitions are added because the story does not
    need them: capacity is reserved under commitments of 8,518.9 and agreements of 4 to 10 years
    [10-Q Q2 FY2027, Note 9; 10-K FY2026, Note 8].
    The implied return on capital check, from the dry run at these settings. The return on all
    invested capital climbs to about 52% in years 5 and 6, then falls to about 40% in year 10 as the
    fade-year investment at 1.3 accumulates and the margin drifts back toward the industry average;
    that year-10 figure is the 40.5% the US semiconductor industry earns today (after-tax margin 33.5%
    times sales to capital 1.21), so the bull converges to the industry's return rather than staying
    above it, which is what the playbook asks of the ratio; at a late ratio of 1.9 the year-10 return
    would be about 45%, above the industry's 40.5%, and the terminal step would fail the engine's
    cliff test (computed; dry run) [Damodaran margin.xls and capex.xls, Semiconductor, 2026-01-05].
    The gross capital spending the flat 2.2 ratio implies in years 2 to 5 is 1,955, 2,002, 1,840 and
    2,013 (the ratio's charge of 6,192, 5,933, 4,676 and 4,758 less working capital at 35 cents plus
    depreciation), or 7.9%, 5.2%, 3.6% and 3.3% of revenue: year 2 sits above the 3.5% to 6.1% record
    because a flat ratio over-charges the year with the largest revenue increase, which the forward
    arithmetic puts at 2.5, and under-charges years 4 and 5, which it puts at 2.0 and 1.9; over years 2
    to 5 together the ratio charges about 21,560 against about 21,690 from the component build, so
    the two agree in total and the year-2 excess is timing rather than extra equipment (computed)
    [10-K FY2026, Item 8].
- **Reinvestment override** — Year 1 is set in dollars for the same reason as the base case: management has named about 1 billion of factory prepayments this fiscal year with deposits running into next, and on this faster revenue path working capital takes more as well (outlook.md section 4). The figure is after subtracting depreciation. [Q2 FY2027 call; 10-Q Q2 FY2027, Note 14; Item 1; 10-Q Q1 FY2027, Note 9]

    Year 1 = about 3,112 of extra working capital, being 35 cents on each dollar of the following
    year's revenue increase of 8,891, plus about 1,000 of capacity prepayments falling inside the
    window (the arithmetic is in the base case), plus about 272 of capital spending net of
    depreciation (714 at 4.5% of revenue less 443), which is 4,384, taken as 4,400 (computed)
    [Q2 FY2027 call; 10-Q Q2 FY2027, Note 14; 10-Q Q1 FY2027, Note 9]. The ratio alone would have
    charged 4,041 (8,891 divided by 2.2), so the override adds about 360 to year 1.
- **Tax rate** — Starts at management's own estimate of tax on continuing profits for fiscal 2028, approximately 13%, the figure explained in the base-year tax cell, and rises to the 25% rate the model uses once a company is mature. [Q2 FY2027 call]
- **Terminal growth** — The ten-year government bond rate fetched for the run, as the method requires: no company outgrows the economy forever.
- **Terminal return on capital premium** — Eleven points above the cost of capital, so the perpetual return is around 20% at today's rates: in this case the lock-in described in business.md section 5 proves durable, the warrant keeps the largest custom customer buying into the 2030s, and Marvell holds the leading position in both the optics and the switches that sit next to the processors. It is still below what the business earns today on the capital behind its designs and about half of what it earns in year 10, and it matches the eleven points Damodaran gave Nvidia, the strongest chip franchise he has valued, which is as far as a case that still rests on the customers' own chip designs should go.

    Reference points: the perpetual cost of capital is the bond rate of the day plus 4.5 points, so
    eleven points on top puts the perpetual return at the bond rate plus 15.5 points, around 20.3%
    at today's rates. The comparison that matters is the return on the capital actually behind the
    products, about 22.6% today once the 13,873.9 of goodwill from past deals is set aside, and about
    40% in this case's year 10 on the engine's measure, so the perpetual figure is below both
    [10-Q Q2 FY2027, Item 1; Note 14]. The return the accounts show on all capital including
    goodwill is 6.8%, which this figure is above; the base case cell explains why that comparison
    is not the useful one here. Why eleven: Damodaran's own Nvidia workbooks used 11.2 to 11.5
    points for the strongest chip franchise he has valued, and this case does not claim more than
    that, because even here the customers own the architecture and 'may begin developing and making
    their own semiconductor solutions'; the method's ceiling of twelve was considered and not taken
    for that reason [10-K FY2026, Item 1A].
    Transition into perpetuity: the perpetual reinvestment charge is about 24% of after-tax
    operating profit against about 14% in the last modelled year, so cash flow steps down about 7%
    into the terminal year, and the terminal return of about 20.3% sits just above half of year
    10's 40%, a margin of a quarter of a point that moves with the bond rate; the owner should
    expect the engine's cliff note to appear if the bond rate falls (computed; dry run).

### Management: reasons

- **Computable: no** — Management has met the requirement of at least one multi-year revenue or margin target, giving revenue figures for two years and a margin target, but it has given nothing numeric beyond FY2028, which is only model year 2, except a custom target for FY2029 that covers one product line. Years 3 to 5 would therefore be guesswork rather than filling in between guided points, so this case is left uncomputable. Dollar signs inside the quotations below are written as USD because the app reads a dollar sign as a formula.
- **Revenue growth** — Management's two revenue figures turned into growth rates. Its fiscal years do not line up with the twelve-month windows this model uses, so year 1 takes the midpoint of the two guided years and year 2 takes the later one, both approximations noted below; years 3 to 5 have no company-level guidance of any kind. [Q2 FY2027 call; Q2 FY2027 slides, p.8]

    Year 1 covers the six months after fiscal 2027 ends and the six months before fiscal 2028 ends,
    so the midpoint of 'roughly 12 billion' and 'approximately 18 billion' is used: 15,000 divided
    by 9,450.3 less one is 0.587 (computed) [Q2 FY2027 call; Q2 FY2027 slides, p.8]. Year 2 takes
    fiscal 2028's 18,000 as the nearest guided point: 18,000 over 15,000 less one is 0.20. That
    understates year 2, because the window also holds the first half of fiscal 2029, which
    management says will 'accelerate significantly' in custom without giving a company figure
    [Q2 FY2027 call]. The other guided item that could be turned into a number is the custom target
    of 'over 10 billion in revenue in fiscal 29', but it covers one product line, so it cannot fill
    a company revenue line on its own [Q1 FY2027 call].
- **Operating margin** — One quarter's guidance stretched over a whole year, which is the only official margin management's own numbers support. Years 2 to 5 are left empty because turning the later adjusted target into an official margin needs a share-based-pay figure management does not give. [Q2 FY2027 release]

    Year 1 = the guided third-quarter gross margin midpoint of 53.4% less guided operating expenses
    of 1,015 on revenue of 3,150, which is 32.2% of revenue, giving 21.2% (computed)
    [Q2 FY2027 release]. It understates the window, because the fourth quarter and fiscal 2028 carry
    the 38% to 40% adjusted target and much lower acquisition write-downs [Q2 FY2027 call].
- **Sales-to-capital** — Not guided. The only spending figure management gives is 'approximately 1 billion of capacity prepayments' for this fiscal year, and that is one part of investment; without capital-spending and working-capital guidance it cannot be turned into a ratio. [Q2 FY2027 call]
- **Reinvestment override** — The prepayment figure alone is not a net investment number, and nothing else about spending is guided, so this case has no reinvestment line and cannot be computed. [Q2 FY2027 call]
- **Tax rate** — Management's own estimate of tax on continuing profits for fiscal 2028, approximately 13%, against 11% for this year, with the terminal year at the rate the model uses for a mature company. That estimate is the rate left once one-off items are stripped out. [Q2 FY2027 call]
- **Terminal growth** — Management gives no long-run growth rate.
- **Terminal return on capital premium** — Management gives no return-on-capital target.

## 3. Base year (the twelve months ending August 1, 2026 (Q3 FY2026 to Q2 FY2027))

| Item | USD millions | Reason | Source |
|---|---|---|---|
| Revenue, trailing twelve months | 9,450.3 | The base year is the twelve months to August 1, 2026, so the model starts from the sales Marvell has just made rather than from a fiscal year that ended last January (business.md section 2). It is the last annual report with the newest six months swapped in for the year-earlier six months. | [10-K FY2026, Item 8; 10-Q Q2 FY2027, Item 1] |
| Operating income, GAAP | 1,561.3 | Operating profit for the same twelve months exactly as reported, which is 16.5% of revenue (business.md section 3). Nothing is stripped out as one-off: Marvell has booked restructuring every year since FY2024 and closed acquisitions in four of the last six fiscal years, so the method counts both as recurring. The divestiture gain and the earn-out revaluation sit below operating profit, so they never touch this line. | [10-K FY2026, Item 8; 10-Q Q2 FY2027, Item 1] |
| One-time items | none | — | — |
| Amortization of acquired intangibles (memo) | 892.7 | The yearly write-down of technology and customer relationships bought in past acquisitions, worth 9.4 points of revenue in the base year. It stays as a cost by the method, but it falls away fast on a schedule already in the accounts, and every margin path below builds that roll-off in (business.md section 3). | [10-K FY2026, Item 8; 10-Q Q2 FY2027, Item 1] |
| Stock-based compensation (memo) | 828.9 | Pay handed out as shares, 8.8 points of revenue in the base year and running at roughly double last year's rate. The method keeps it inside operating profit because it is a real cost to existing owners; this cell is only a memo (business.md section 4). | [10-K FY2026, Item 8; 10-Q Q2 FY2027, Item 1] |
| Research and development expense (memo) | 2,441.9 | What Marvell spent on chip design in the base year, 25.8% of revenue: the fixed bill that makes its profits swing so hard with volume, and the biggest piece of spending for future revenue inside today's costs (business.md section 3). Memo row only, since the switch that would treat research as an investment is off. | [10-K FY2026, Item 8; 10-Q Q2 FY2027, Item 1] |
| Effective tax rate | 13.0% | The model starts from management's own estimate of tax on ongoing profits, approximately 13% for FY2028, because the official rates Marvell reports are distorted by a huge divestiture gain in one year and a charge that gets no tax relief in the next (business.md section 4). The FY2028 figure is used rather than FY2027's 11% because model year 1 already runs into FY2028 and the rate rises with earnings. | [Q2 FY2027 call; Q2 FY2027 release] |
| Invested capital | 19,884.9 | The capital the business has been handed: what shareholders and lenders put in, less its cash. It is used only for the return-on-capital check, and it reads low because most of it is the price paid for past acquisitions rather than money behind today's chip designs (business.md section 4). | [10-Q Q2 FY2027, Item 1; Note 14] |

- **Revenue**, working notes:

    Base year = FY2026 (10-K) + six months ended 2026-08-01 minus six months ended 2025-08-02 (10-Q Q2 FY2027): 8,194.6 + 5,157.1 minus 3,901.4 = 9,450.3 [10-K FY2026, Item 8; 10-Q Q2 FY2027, Item 1]. Cross-check: the four quarters Q3 FY2026 to Q2 FY2027 in the eight-quarter table sum to 2,074.5 + 2,218.7 + 2,417.8 + 2,739.3 = 9,450.3 [Q2 FY2027 supplemental, p.5]. The year-earlier twelve months were 1,516.1 + 1,817.4 + 1,895.3 + 2,006.1 = 7,234.9, so the trailing year is up 31% and the latest quarter is up 37% [Q2 FY2027 supplemental, p.5].

- **Operating income gaap**, working notes:

    Trailing twelve months = FY2026 GAAP operating income 1,322.9 + six months FY2027 of 799.1 minus six months FY2026 of 560.7 = 1,561.3 [10-K FY2026, Item 8; 10-Q Q2 FY2027, Item 1]; 1,561.3 / 9,450.3 = 16.5% (computed). The FY2026 figure is the sum of the four quarters 270.6 + 290.1 + 357.8 + 404.4 [Q2 FY2027 supplemental, p.5].
    Left inside operating income, which is why the one-time items list is empty. Restructuring inside the trailing twelve months = 16.0 (FY2026) plus 5.7 (H1 FY2027) plus the 3.6 credit booked in H1 FY2026, which is taken back out, = 25.3; the yearly series FY2024 to FY2026 is 131.1, 711.8, 16.0 [10-K FY2026, Note 4; Q2 FY2027 release]. The 'other' non-GAAP items inside the trailing twelve months (acquisition and divestiture costs, legal matters, investment gains) = cost of goods sold 1.9 + research 22.7 + selling and administrative 62.2 = 86.8 over Q3 FY2026 to Q2 FY2027 [Q2 FY2027 supplemental, p.8].
    Below operating income and therefore untouched: the 1,830.4 divestiture gain and the 433.7 earn-out revaluation [10-K FY2026, Note 1; 10-Q Q2 FY2027, Note 6].

- **Amortization of acquired intangibles**, working notes:

    Cash-flow statement line 'Amortization of acquired intangible assets', trailing twelve months = FY2026 942.0 + H1 FY2027 440.1 minus H1 FY2026 489.4 = 892.7; 892.7 / 9,450.3 = 9.4 points of revenue (computed) [10-K FY2026, Item 8; 10-Q Q2 FY2027, Item 1]. Roll-off schedule as of August 1, 2026: 385.3 for the rest of FY2027, 292.7 for FY2028, 139.6 for FY2029, 117.2 for FY2030, 60.8 for FY2031 and 54.0 after that, total 1,049.6; the 10-K's January schedule read 814.0 / 284.8 / 131.8 / 109.5 [10-Q Q2 FY2027, Note 5; 10-K FY2026, Note 5]. On top of that the balance sheet carries 1,297.0 of acquired research not yet in use (951.0 from Celestial, 46.0 from XConn, 300.0 already on the books at January 31, 2026), which is not amortized until the products ship and then runs over useful lives of 6 to 13 years, a further 100 to 216 a year once all of it is running [10-Q Q2 FY2027, Note 5]. Memo row; stays deducted.

- **Stock based compensation**, working notes:

    Trailing twelve months = FY2026 590.8 + H1 FY2027 533.8 minus H1 FY2026 295.7 = 828.9; 828.9 / 9,450.3 = 8.8 points of revenue (computed) [10-K FY2026, Item 8; 10-Q Q2 FY2027, Item 1]. Run rate: 326.2 in Q2 FY2027 against 153.6 a year earlier, with 190.1 of assumed Celestial awards still to be expensed [Q2 FY2027 supplemental, p.5; 10-Q Q2 FY2027, Note 10]. Five-year history as a share of revenue: 10.3% FY2022, 9.3% FY2023, 11.1% FY2024, 10.4% FY2025, 7.2% FY2026 (computed from business.md section 4). Memo row; never added back.

- **Rnd expense**, working notes:

    Trailing twelve months = FY2026 2,075.2 + H1 FY2027 1,393.4 minus H1 FY2026 1,026.7 = 2,441.9; 2,441.9 / 9,450.3 = 25.8% (computed) [10-K FY2026, Item 8; 10-Q Q2 FY2027, Item 1]. The US semiconductor industry spends 15.4% of sales on research, so about ten points of today's revenue is design spending running ahead of the sales it is meant to produce, which is the first offset in every margin path below [Damodaran margin.xls, Semiconductor, 2026-01-05]. The five-year history in the switches block, oldest first, is FY2022 to FY2026: 1,424.2, 1,784.3, 1,896.2, 1,950.4, 2,075.2 [10-K FY2024, Item 8; 10-K FY2026, Item 8].

- **Effective tax rate**, working notes:

    Why the reported rate is unusable: FY2026 shows 12.4%, but that year's pretax income was dominated by the 1.8 billion divestiture gain; the six months of FY2027 show 25.8% (119.1 on 461.6) because the 433.7 earn-out charge is not tax-deductible [10-K FY2026, Note 12; 10-Q Q2 FY2027, Note 11]. Management guides a non-GAAP tax rate of 11% for FY2027 and 'approximately 13% in fiscal 2028' [Q2 FY2027 call; Q2 FY2027 release]. The US semiconductor industry's average effective rate among profitable companies is 15.8% [Damodaran taxrate.xls, Semiconductor, 2026-01-05].

- **Invested capital**, working notes:

    At August 1, 2026: book equity 18,531.6 + debt 4,962.9 + operating lease liabilities 323.2 (59.3 current + 263.9 non-current) minus cash 3,932.8 = 19,884.9 [10-Q Q2 FY2027, Item 1; Note 14]. Goodwill is 13,873.9 and acquired intangibles 2,346.6 of that [10-Q Q2 FY2027, Item 1]. After-tax operating profit of 1,358.3 (1,561.3 at the 13% rate) is a 6.8% return on the whole figure and a 22.6% return on the 6,011.0 left once goodwill is set aside (computed); both figures are used in the terminal cells below.

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
| Cash and marketable securities (added) | 3,932.8 | The money Marvell can spend at once, added to the value of the business. There is no separate investments line to add: the balance sheet and the management discussion show only cash and cash equivalents. | [10-Q Q2 FY2027, Item 1] |
| Non-operating asset (added): Forward stock purchase contract (cash-settled hedge of the Celestial earn-out) | 131 | A twelve-month contract Marvell bought in April 2026 to hedge the shares it may owe on the Celestial earn-out: it pays out in cash if the share price rises, offsetting the part of the earn-out that is settled in shares. It is an asset, so it is added to the value of the business. | [10-Q Q2 FY2027, Note 6] |
| Non-operating asset (added): Marketable equity investments | 25.5 | Shares in listed companies held among Marvell's longer-term assets and valued at the quoted market price, which accountants call a Level 1 measurement. Added to value separately because they are not part of the chip business. | [10-Q Q2 FY2027, Note 6] |
| Non-operating asset (added): Non-marketable equity investments | 156.2 | Stakes in private companies, added to value separately because they are not part of the chip business. They are carried at what Marvell paid, less any write-down where the value has clearly fallen, so the figure is softer than it looks. | [10-Q Q2 FY2027, Note 14] |
| Debt (subtracted) | 4,962.9 | All of Marvell's borrowing at the value the accounts carry it at, subtracted from the value of the business: eight series of unsecured bonds, with no bank loans left and the revolving credit line untouched (business.md section 7). | [10-Q Q2 FY2027, Note 7] |
| Operating lease liabilities (subtracted) | 323.2 | Rent Marvell has already committed to on the offices and labs it leases, treated as debt-like and subtracted from value. | [10-Q Q2 FY2027, Note 14] |
| Minority interests (subtracted) | 0 | The balance sheet shows no non-controlling interest line. | [10-Q Q2 FY2027, Item 1] |
| Other claim (subtracted): Celestial AI contingent consideration (earn-out) liability | 749.5 | Marvell owes the former owners of Celestial AI extra payments if that business hits revenue targets, and the promise has more than doubled in value since the deal closed. It is subtracted at its carrying value, and the part payable in shares is counted here rather than in the share count, so it is not double-counted. | [10-Q Q2 FY2027, Note 6; Note 14] |
| Probability of failure | 0.0% | Zero, as the method sets it for a large profitable company: Marvell holds 3.9 billion of cash against investment-grade bonds with nothing to repay before FY2029, its operations produced 1.2 billion of cash in six months, and its 1.5 billion credit line is untouched (business.md section 4). Failure risk therefore stays out of the cost of capital as well. | — |
| What the assets would fetch in a failure | 0 | Not needed with the probability of failure at zero. | — |
| Diluted shares (millions) | 921.2 | The share count the per-share value is divided by: the latest quarter's average as the accountants compute it, including shares owed on employee awards and vested customer warrants, and the NVIDIA preferred shares counted as if already swapped for ordinary shares. Management guides the same count for the next quarter. | [10-Q Q2 FY2027, Item 1; Note 12] |

- **Cash and marketable securities**, working notes:

    Cash and cash equivalents 3,932.8 at August 1, 2026; the management discussion describes only 'cash and cash equivalents' of 3.9 billion [10-Q Q2 FY2027, Item 1; Item 2]. Time deposits of 194.0 are already inside cash equivalents [10-Q Q2 FY2027, Note 6].

- **Debt**, working notes:

    Net carrying amount at August 1, 2026 = face value 4,999.9 less 37.0 of unamortized discount and issuance cost = 4,962.9 [10-Q Q2 FY2027, Note 7]. The last term loan was repaid in FY2026 and the 1.5 billion revolver is undrawn [10-Q Q2 FY2027, Note 7]. Left out as operating items: technology-license payment obligations of 220.0 (96.2 + 123.8) [10-Q Q2 FY2027, Note 14].

- **Operating lease liabilities**, working notes:

    Lease liabilities current 59.3 plus non-current 263.9 = 323.2 at August 1, 2026 [10-Q Q2 FY2027, Note 14].

- **Probability of failure**, working notes:

    3,932.8 of cash against 4,999.9 face value of notes with nothing due before FY2029; 1,244.3 of operating cash flow in the six months to August 1, 2026; an undrawn 1.5 billion revolver [10-Q Q2 FY2027, Note 7; Item 1; Item 2].

- **Diluted shares**, working notes:

    Q2 FY2027 diluted weighted-average shares 921.2 = 875.6 basic common + 21.8 NVIDIA convertible preferred counted as if converted + 23.8 from stock awards and vested customer warrants [10-Q Q2 FY2027, Item 1; Note 12]. Management guides 921 million for Q3 [Q2 FY2027 release].

Dilution note: Not in the 921.2: the August 2026 Google warrant for up to 58,970,907 shares at 206.58 USD each (1,360,867 time-based shares vesting quarterly in year one, about 340,217 a quarter, and 57,610,040 performance shares in 240 tranches of about 240,042, one per 500 million USD of custom-product revenue from Q3 FY2027 through FY2033; arithmetic from outlook.md section 5, claim 12), two earlier customer warrants for 4.2 million shares at 87.77 USD (1.2 million vested) and 1.0 million at 87.00 USD, the 22.4 to 24.4 million Celestial earn-out shares already valued in the other claims above, and stock pay running at 326.2 a quarter (190.1 of Celestial awards still to expense), against which management 'intend[s] to continue repurchasing shares to manage dilution' [8-K 2026-08-19; 10-Q Q2 FY2027, Note 3; Note 10; Note 15; Q2 FY2027 supplemental, p.5; Q2 FY2027 call].

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
| Damodaran industry | Semiconductor | Marvell is a fabless chip designer, meaning it designs chips and pays outside factories to make them, and all its revenue is chips sold into data-center and communications equipment (business.md sections 1 and 2). The rate this builds is checked against Damodaran's own semiconductor row and his band of US costs of capital in the terminal cell below. | — |
| Unlevered beta | 1.505 | Damodaran's 66-company US semiconductor group has an unlevered beta, corrected for cash, of 1.5046. A beta above 1 means chip earnings swing more than the market's, which is what Marvell's own history shows (business.md section 3). | [Damodaran betas.xls, Semiconductor, dataset dated 2026-01-05, cached tools/valuation/data/damodaran/betas.csv] |
| Debt to equity (market values) | 0.0255 | Marvell carries very little debt next to what the market says its shares are worth, so borrowing barely moves the cost of capital (business.md section 4). This ratio is what levers the industry beta up; the runner refreshes it with the price of the day. | [10-Q Q2 FY2027, Note 7; Note 14] [Yahoo price 225.41 on 2026-09-08 16:00 EDT; runner re-check 2026-09-09] |
| Pre-tax cost of debt | 5.30% | 5.3% is what ten-year money costs Marvell today, taken from the coupon on its most recent bond sale, which is the rate new borrowing would carry. The average coupon across all eight series is lower because older bonds were sold when rates were lower. | [10-Q Q2 FY2027, Note 7] |
| Terminal cost of capital method | mature | Default: after year 10 the firm is discounted at the risk-free rate plus the mature-market premium of 4.5 points, so no company-specific edge is assumed in perpetuity. The built rate for the explicit years sits in the upper part of Damodaran's US band and next to his semiconductor row, and it carries neither failure risk nor a view on management (both are handled elsewhere in this file). | — |

- **Debt to equity market**, working notes:

    Debt 4,962.9 plus operating leases 323.2 = 5,286.1, divided by market capitalisation of 207,648 (225.41 times 921.2 diluted shares) = 0.0255 [10-Q Q2 FY2027, Note 7; Note 14] [Yahoo price 225.41 on 2026-09-08 16:00 EDT, the price the engine fetched when the runner re-checked this cell on 2026-09-09]. The industry's own market debt-to-equity is 0.026, so Marvell is typical [Damodaran betas.xls, Semiconductor, 2026-01-05].

- **Pretax cost of debt**, working notes:

    The most recent issue is the 5.300% Senior Notes due 2036, sold April 15, 2026, with an effective rate of 5.358% [10-Q Q2 FY2027, Note 7]. The face-weighted average coupon on all eight series is 4.55% (computed). The industry row uses a 5.29% pre-tax cost of debt [Damodaran wacc.xls, Semiconductor, 2026-01-05].

## 7. Inputs for the diagnostics

| Item | Value | Reason | Source |
|---|---|---|---|
| Market size in the final forecast year (USD millions) | 126,100 | An inference, not a management figure: the only market management has sized is a 55 billion custom data-center silicon market for fiscal 2029, and this cell carries it forward seven and a half years to the last model year at the 11.7% a year that analysts expect the US semiconductor industry to grow. It covers only Marvell's custom line, so the engine's share reading overstates the company's true share; each case's growth notes give the custom-only comparison. | [Q1 FY2027 call] [Damodaran histgr.xls, Semiconductor, 2026-01-05] |
| Company's own five-year revenue growth per year | 16.4% | Marvell's own revenue grew about 16.4% a year over the five fiscal years FY2022 to FY2026, shown as context and not as an anchor: data center was 40% of revenue for most of that period and is 79% now, so the old mix tells little about the new one (business.md sections 2 and 3). Almost all of the growth came in the last of those years, when the AI orders arrived. | [10-K FY2024, Item 7; Item 8] [10-K FY2026, Item 7; Item 8] |
| Company's own five-year average operating margin | -2.1% | Averaged over the same five fiscal years, Marvell's reported operating margin was slightly negative, so every case here assumes a business that looks nothing like its own recent history (business.md sections 3 and 4). The red ink came mostly from writing down the price of past acquisitions and from share-based pay rather than from the chips themselves, which is why the margin paths are built from a bridge rather than from this average. | [10-K FY2024, Item 7; Item 8] [10-K FY2026, Item 7; Item 8] |

## 8. Management guidance on record

Everything management has said in numbers or in words, whether or not it was used.

| Item | Quote | Source | Used as |
|---|---|---|---|
| Q3 FY2027 revenue | Net revenue is expected to be USD 3.150 billion +/- 5%. | [Q2 FY2027 release] | revenue growth year 1 (anchors the second half of FY2027 inside the year-1 window) |
| Q3 FY2027 GAAP gross margin | GAAP gross margin is expected to be 52.9% to 53.9%. | [Q2 FY2027 release] | operating margin year 1 (midpoint 53.4%) |
| Q3 FY2027 non-GAAP gross margin | Non-GAAP gross margin is expected to be 57.5% to 58.5%. | [Q2 FY2027 release] | not numeric (non-GAAP; GAAP figure used instead) |
| Q3 FY2027 GAAP operating expenses | GAAP operating expenses are expected to be approximately USD 1.015 billion. | [Q2 FY2027 release] | operating margin year 1 |
| Q3 FY2027 non-GAAP operating expenses | Non-GAAP operating expenses are expected to be approximately USD 655 million. | [Q2 FY2027 release] | not numeric (non-GAAP) |
| Q3 FY2027 share count | Diluted weighted-average shares outstanding are expected to be 921 million. | [Q2 FY2027 release] | not numeric (confirms the diluted share count) |
| Q3 FY2027 GAAP EPS | GAAP diluted net income per share is expected to be USD 0.53 +/- USD 0.05 per share. | [Q2 FY2027 release] | not numeric (below the operating line) |
| Q3 FY2027 non-GAAP EPS | Non-GAAP diluted net income per share is expected to be USD 1.10 +/- USD 0.05 per share. | [Q2 FY2027 release] | not numeric (non-GAAP, below the operating line) |
| Q3 FY2027 data center | data center revenue forecasted to grow more than 20% sequentially and roughly 75% year-over-year. | [Q2 FY2027 call] | not numeric (segment) |
| Q3 FY2027 communications and other | we expect revenue to decline in the low to mid-teens percentage range both sequentially and year-over-year, followed by a solid sequential recovery in the fourth quarter. | [Q2 FY2027 call] | not numeric (segment) |
| Q3 FY2027 non-GAAP tax rate | We expect a non-GAAP tax rate of 11%. | [Q2 FY2027 call] | not numeric (FY2027 rate; superseded by the FY2028 rate used as the starting tax rate) |
| Q3 FY2027 gross-margin driver | the forecasted acceleration of our custom business creating ... the sequential headwind in the fiscal third quarter | [Q2 FY2027 call] | not numeric (the machine transcript first garbles 'headwind' as 'headroom' and then corrects itself; the corrected phrase is quoted, as in outlook.md section 4) |
| Q4 FY2027 gross margin | We currently expect to maintain gross margin in this range in the fourth fiscal quarter. | [Q2 FY2027 call] | not numeric |
| Q4 FY2027 non-GAAP operating margin | non-GAAP operating margin likely to enter our 38% to 40% long-term target range in Q4 of this fiscal year. | [Q2 FY2027 call] | not numeric (non-GAAP; converting to GAAP needs a stock-pay assumption management does not give) |
| FY2027 revenue | we now expect overall Marvell revenue in fiscal 2027 to grow approximately 45% year-over-year to roughly USD 12 billion, up from our prior outlook of approximately USD 11.5 billion just 1 quarter ago. | [Q2 FY2027 call] | revenue growth year 1 (interpolation anchor) |
| FY2027 data center | which we now expect to grow by approximately 60% this fiscal year, up from our prior expectation of approximately 50%. | [Q2 FY2027 call] | not numeric (segment) |
| FY2027 communications and other | we currently expect fiscal 2027 growth to approach our 10% target. | [Q2 FY2027 call] | not numeric (segment) |
| FY2027 non-GAAP operating expenses | For fiscal 2027, we expect non-GAAP operating expenses of approximately USD 2.55 billion, slightly above our prior expectation of USD 2.45 billion | [Q2 FY2027 call] | not numeric (non-GAAP) |
| FY2027 capacity prepayments | We remain on pace to make approximately USD 1 billion of capacity prepayments to suppliers in fiscal 2027. | [Q2 FY2027 call] | not numeric (one component of reinvestment; no capex or working-capital guidance to complete net reinvestment) |
| Capacity deposits schedule | we committed to pay deposits totaling USD 870.0 million, payable in quarterly installments from the second quarter of fiscal 2027 through the second quarter of fiscal 2028. | [10-Q Q1 FY2027, Note 9] | not numeric (timing of the prepayments inside the year-1 window) |
| FY2028 revenue | we now expect fiscal 2028 revenue of approximately USD 18 billion, up USD 1.5 billion from the USD 16.5 billion outlook we provided just 1 quarter ago. | [Q2 FY2027 call] | revenue growth year 1 (interpolation anchor) and year 2 (nearest-year mapping) |
| FY2028 data center | we now expect Marvell's Data Center revenue to grow more than 60% year-over-year in fiscal 2028 | [Q2 FY2027 call] | not numeric (segment) |
| FY2028 custom | We remain confident that this business will more than double year-over-year in fiscal 2028 and accelerate significantly in fiscal 2029. | [Q2 FY2027 call] | not numeric (segment; the FY2029 phrase is qualitative) |
| FY2028 operating expenses | We currently expect non-GAAP operating expenses to grow at roughly half the rate of revenue growth in percentage terms. | [Q2 FY2027 call] | not numeric |
| FY2028 non-GAAP operating margin | to achieve the upper end of our target non-GAAP operating model of 38% to 40% as we progress through the year | [Q2 FY2027 call] | not numeric (non-GAAP; GAAP conversion needs stock pay, not guided) |
| FY2028 non-GAAP tax rate | we expect non-GAAP tax rate of approximately 13% in fiscal 2028. | [Q2 FY2027 call] | the starting tax rate (all cases) |
| FY2028 gross margin | My preliminary view is gross margins next year are going to be in a similar range, same range as we're exiting this year. | [Q2 FY2027 call] | not numeric |
| Long-term model | we're going to reset that long-term target model here in the coming weeks at the Analyst Day. | [Q2 FY2027 call] | not numeric |
| Google warrant arithmetic (FY2029 and beyond) | you should assume starting in FY '29 and beyond whatever you've modeled previously prior to the warrant for custom numbers definitely goes higher | [Q2 FY2027 call] | not numeric |
| Custom FY2029 upside | clearly, there's a lot of upside bias in those numbers in fiscal '29 and beyond in custom. | [Q2 FY2027 call] | not numeric (informs the base-case fiscal 2029 custom figure) |
| Scale-out switching FY2027 | Within scale-out switching, our business remains on track to more than double this year | [Q2 FY2027 call; Q2 FY2027 slides, p.18] | not numeric (segment; Q1 form was 'exceed USD 600 million, doubling from fiscal 2026', tracking to 'more than USD 1 billion in annualized revenue in fiscal 2028' [Q1 FY2027 call]) |
| Interconnect FY2027 (Q1 target, not restated in Q2) | we have increased our fiscal 27 revenue growth expectations for this business to more than 70% year over year | [Q1 FY2027 call; Q1 FY2027 slides, p.7] | not numeric (segment; scorecard.md grades it Partial) |
| Custom FY2027 (Q1 target, not restated in Q2) | Custom revenue remains on track to grow more than 20% year over year in fiscal 27 | [Q1 FY2027 call; Q1 FY2027 slides, p.14] | not numeric (segment) |
| Custom FY2029 target and market | We remain confident in achieving our target model for our custom business to deliver on over USD 10 billion in revenue in fiscal 29. | [Q1 FY2027 call] | not numeric (segment target; the 'USD 55 billion TAM' behind it feeds the final-year market size in the diagnostics) |
| DCI modules | Giving us line of sight to a USD 1 billion annualized revenue during fiscal 28. This would represent approximately double the revenue we achieved in fiscal 26 when the business generated roughly USD 500 million in revenue. | [Q1 FY2027 call] | not numeric (segment anchor inside the interconnect residual) |
| Scale-up optics FY2028 (Q1 figure, superseded) | scale up optics which you know, we are effectively calling at this point to be about USD 300 million | [Q1 FY2027 call] | not numeric (Q2: 'much larger than we thought just a quarter ago', no new figure) |
| Cloud capex planning assumption FY2028 (Q1, dropped in Q2) | we are planning for the rate of cloud CapEx growth to moderate into the 30%-plus range | [Q1 FY2027 call] | not numeric (informs the base-case step down in year 3) |
| Communications FY2028 (Q1) | we continue to expect low single digit percentage revenue growth in fiscal 28, consistent with our prior view. | [Q1 FY2027 call] | not numeric (segment) |

## Sources

Every source tag used above, the cached file it points to (relative to the company folder), and the document date.

| Tag | Cached file | Date | Note |
|---|---|---|---|
| [10-K FY2026, ...] | `sources/FY2027-Q1/10-K-FY2026.txt` | 2026-03-11 | 10-K for the fiscal year ended 2026-01-31; the date is the filing date |
| [10-K FY2024, ...] | `sources/FY2027-Q1/10-K-FY2024.txt` | 2024-03-13 | 10-K for the fiscal year ended 2024-02-03; the date is the filing date |
| [10-Q Q2 FY2027, ...] | `sources/FY2027-Q2/10-Q-FY2027-Q2.txt` | 2026-08-28 | quarter ended 2026-08-01; the date is the filing date |
| [10-Q Q1 FY2027, ...] | `sources/FY2027-Q1/10-Q-FY2027-Q1.txt` | 2026-05-28 | quarter ended 2026-05-02; the date is the filing date |
| [DEF 14A 2026, ...] | `sources/FY2027-Q1/DEF14A-2026.txt` | 2026-05-13 | proxy statement; the bonus-target discussion that supports the custom gross-margin inference |
| [8-K 2026-08-19] | `sources/FY2027-Q2/8-K-2026-08-19.txt` | 2026-08-19 | Google commercial agreement and warrant |
| [Q2 FY2027 release] | `sources/FY2027-Q2/press-release.txt` | 2026-08-27 | 8-K Exhibit 99.1 |
| [Q2 FY2027 supplemental, p.N] | `sources/FY2027-Q2/supplemental.txt` | 2026-08-27 | eight-quarter tables |
| [Q2 FY2027 slides, p.N] | `sources/FY2027-Q2/slides.txt` | 2026-08-27 | — |
| [Q2 FY2027 call] | `sources/FY2027-Q2/transcript.txt` | 2026-08-27 | third-party Motley Fool machine transcript, tier 3; numbers taken from the release where they exist |
| [Q2 FY2027 notes] | `sources/FY2027-Q2/notes-transcript.md` | 2026-09-07 | gatherer's notes on the Q2 call and IR documents; cited only for the absence of market-size figures |
| [Q1 FY2027 call] | `sources/FY2027-Q1/transcript.txt` | 2026-05-27 | Motley Fool machine transcript, tier 3 |
| [Q1 FY2027 slides, p.N] | `sources/FY2027-Q1/slides.txt` | 2026-05-27 | — |
| [Q1 FY2027 release] | `sources/FY2027-Q1/press-release.txt` | 2026-05-27 | 8-K Exhibit 99.1; quarterly non-GAAP operating expenses |
| [Q1 FY2027 supplemental, p.N] | `sources/FY2027-Q1/supplemental.txt` | 2026-05-27 | eight-quarter tables; cited by the historical-margin diagnostic |
| [Damodaran betas.xls, ...] | `tools/valuation/data/damodaran/betas.csv` | 2026-01-05 | engine-cached dataset; Semiconductor row, unlevered beta corrected for cash 1.5046, market debt to equity 0.026 |
| [Damodaran wacc.xls, ...] | `tools/valuation/data/damodaran/wacc.csv` | 2026-01-05 | engine-cached dataset; Semiconductor cost of capital 10.55%, Total Market 6.96% |
| [Damodaran capex.xls, ...] | `tools/valuation/data/damodaran/capex.csv` | 2026-01-05 | engine-cached dataset; Semiconductor sales to invested capital 1.21, capital spending 53,610, depreciation 42,301, acquisitions 5,235, net research 5,877, net capital spending to sales 4.4% and to after-tax operating profit 14.5% |
| [Damodaran margin.xls, ...] | `tools/valuation/data/damodaran/margin.csv` | 2026-01-05 | engine-cached dataset; Semiconductor pre-tax unadjusted operating margin 35.3%, pre-share-pay 40.4%, after-tax 33.5%, gross margin 59.0%, research 15.4% and share pay 5.0% of sales; neighbouring rows as cited |
| [Damodaran histgr.xls, ...] | `tools/valuation/data/damodaran/histgr.csv` | 2026-01-05 | engine-cached dataset; Semiconductor revenue growth 11.2% a year over the last five years, expected 11.7% a year over the next five and 40.9% over the next two |
| [Damodaran taxrate.xls, ...] | `tools/valuation/data/damodaran/taxrate.csv` | 2026-01-05 | engine-cached dataset; Semiconductor average effective tax rate among profitable companies 15.8% |
