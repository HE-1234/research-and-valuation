# Analyst playbook: from the story to the numbers, the way Damodaran does it

Read this in full before writing a single number into `assumptions.yaml`. It is the method behind the rules in AGENTS.md section 18.4; the rules say what a valid file contains, this says how to think your way to the numbers in it. Every claim about his practice here is quoted or cited in two sourced notes, which you consult when you need his exact words or a workbook cell:

- `tools/valuation/damodaran-notes/2026-09-08-story-to-numbers-playbook.md`: his process, each input, his error lists, the Uber 2014 and Nvidia 2023 walkthroughs, with URLs and verbatim quotes.
- `tools/valuation/damodaran-notes/2026-09-08-horizon-terminal-roic-reinvestment.md`: horizon, the ten-year structure of his spreadsheet, terminal return on capital, reinvestment lag, and his Alphabet 2024 and Nvidia 2024-25 inputs read cell by cell.

The reviewer reads this too. The closing section is the list of judgment questions the reviewer must answer, one line each, in the review file.

## 1. The order of work

His five steps, in his order, mapped to our file:

1. **Write the story.** Three to five sentences per case (rule 9): what the company sells, the market it grows into, the competition, the macro setting. His three rules for it: keep it simple, keep it focused, stay grounded in reality. Write the story in the `story` cell before you open any numeric cell.
2. **Test the story.** The 3P test: possible (is there a market that size?), plausible (do the economics in `business.md` sections 3 and 4 allow these margins and this reinvestment?), probable (does `scorecard.md` show management delivering things like this?). The failure modes have names: the runaway story (impossible), the big market delusion (implausible), Willy Wonkitis (improbable). A story that fails a P is rewritten, not patched with numbers.
3. **Turn the story into drivers.** He compresses value to four inputs: revenue growth, a target operating margin, a reinvestment scalar (sales to capital), and a cost of capital plus a failure rate. Fill the `story_to_numbers` table (rule 14) now: one row per sentence that sets an input, the input it sets, the number. If a sentence sets nothing, it is decoration; if an input has no sentence, you do not yet have a reason for it.
4. **Let the arithmetic run.** "With the story in place, and the inputs that come out of it, the valuation, in a sense, does itself." You never see the value in this skill; the engine and the owner do.
5. **Keep the feedback loop open.** New quarters confirm, shift or break stories. When you redraft, say which happened. His bias test: an unbiased analyst raises values as often as lowering them.

His warning about why the story comes first: "every number you have in your valuation, from growth to margins to risk measures, should be backed up by a story about that number, and every story you tell about a company ... has to be reflected in a number in your valuation." And the payoff for us: a story makes the inputs consistent with each other, because you cannot move one number without asking what it does to the story.

## 2. Writing the three stories

- **Bear, base and bull are different stories, not one story with the growth dial moved.** His Uber table had four rows, each a different kind of company (a car service, a logistics company, ...), each with its own market, share, margin, cost of capital and failure odds. "Big differences in valuation almost always result from differing narratives about companies, not disagreements about the small stuff." A bear that keeps the base story and shaves three points off growth is not a bear.
- **The base case is the expected value, not the safe case.** "Much as you will be tempted to use conservative estimates, you should avoid the temptation and make your judgments on expected values." Conservatism is not a virtue in an input; it is a bias with a direction. If you find yourself choosing the lower of two defensible numbers "to be safe", stop and choose the one the story supports.
- **Management's story is tested, not adopted.** "You and I have to develop our own narratives, sometimes in sync with and sometimes at odds with the management story line." The two traps he names: the aggressive analyst, who values what the firm says about itself; the conservative analyst, who refuses to value what is not yet visible. The management case in our file (rule 4) is guidance on record, mapped to the model years, never weighted; use it to see where your stories sit against what management has promised, and say so in the reasons.
- **Weights.** He does not weight discrete cases; he takes the base case as the expected value and runs a Monte Carlo on the two or three inputs that matter most and that he is least sure of. He calls an unweighted best, base, worst display "an almost useless exercise". Our weights (rule 7) are the owner's device for a probability-weighted view and are set by the owner. Your job is to make the three cases genuinely different outcomes with a stated reason for each, so that the weights mean something.
- **Failure is separate.** Failure risk goes into `probability_of_failure`, never into the cost of capital. For a profitable large company he sets it to zero and says so.

## 3. Revenue growth

**Start where the company is (rule 10).** He uses trailing twelve months, never the last annual report, and he moves year one off the current run-rate only for something in the latest filings: "I did lower my revenue growth rate to 1.50%, reflecting the bad news about revenues in the most recent 10Q." A one-year dip that will reverse is smoothed, not modelled, because he showed it barely moves value. An unexplained haircut in year one is the first thing the reviewer will send back.

**Choose the engine for each part of the business.** With stable margins, growth comes from reinvestment times return on capital. With changing margins, or a young business, work top down: the total market, the share the company earns, and the revenue those two imply, keeping "track of absolute revenues to make sure that the growth is feasible". Most companies in this library have both kinds of part (Alphabet's Search and Cloud; Amazon's retail and AWS). He splits only where the parts have different growth engines and says that splitting line items with no basis for forecasting them "creates the illusion of precision". So the segment build (rule 11) is a consistency check on the company path built from the parts that genuinely differ; parts sharing one engine may be one line, and the detail says so.

**Set the end state before the path.** "The revenue growth rate is a means to an end, not an end in itself." Decide what the company is in year ten: its revenue in dollars, its share of the market it will then be in, and how it compares with the largest companies in that sector today. Then back out the growth path. His two ways: work backwards from an end-state share (market size grown forward times share gives year-ten revenue and the compound rate), or extrapolate the first few years and hand off to the growth rate of firms that size today. Either way, the path falls as revenue scales, and every step of more than three points has a named driver (rule 11).

**Tests you run and record in `detail`:**

- Year-ten revenue against the largest companies in the sector today (he compared Commerce One with EDS, Tesla with Audi and then with "only five companies in the world" above 400 billion in revenue). Write the comparison down.
- Year-ten revenue against `diagnostics.final_year_market_size` and the implied share. A share near dominance in a competitive market is a signal to reassess.
- Growth against margin: "firms can post higher growth rates in revenues by adopting more aggressive pricing strategies but the higher revenue growth will then be accompanied by lower margins." A niche-margin story cannot carry mass-market revenue.
- No fade toward the company's own five-year average after a mix change. His words on mean reversion: "If there are structural changes that alter the underlying distribution, there is no quicker way to ruin [a valuation] than trusting in mean reversion." The five-year history in `diagnostics` is context, not an anchor.
- The big-market check in reverse: if the story rests on a large market, the reason must say why this company, against this competition, takes the share assumed. "The market is huge" is not a reason.

## 4. Operating margin

**The starting margin is the trailing twelve months, GAAP, as rule 1 says,** with one-time items removed and acquired amortization kept as a memo row. He goes further and reclassifies growth spending (research, customer acquisition) as capital; our switches exist for the owner to do that, and the analyst leaves them off. What you must do instead is say, in the margin detail, how much of today's operating expense is spending for future revenue, because it is the first offset you will use. He also picks the quarter he thinks representative rather than the annual average when the year was volatile, and says so.

**The target margin is placed inside a named distribution, not asserted.** Every target he publishes comes with its position: "40%, towards the top decile of technology companies" (Uber), "7.36%, the overall retail business" with a bull at "the 75th percentile" and a bear at "the 25th percentile" (Amazon), "25%, lower than Booking.com's 35.48% but higher than Expedia or the hotel business" (Airbnb), "40%, it is worth remembering that the company delivered 42.5% in 2020 and 38.4% in 2021" (Nvidia). Three anchors, in this order:

1. The true competitor set, defined by what the company actually does, not by what it calls itself. The cached `margin.csv` (column "Pre-tax Unadjusted Operating Margin") gives the industry average; name the industry row you used and its date. We do not cache firm-level percentiles, so where he would cite a percentile you bracket the target with named comparables from `business.md` and neighbouring industry rows, and label it as such.
2. The company's own best and worst recent years, from the five-year table in `business.md` section 3.
3. The business model: unit economics ("the companies that deliver the highest margins incur very low costs in producing the next units that they sell"), pricing power, and whether the company controls its own cost of production (Nvidia's margin gains had to come from price because TSMC makes its chips).

**The path: biggest gains early, target reached inside the horizon.** His mechanical default is to close half the gap to the target each year; in practice he names the year the target is reached, usually year five. A margin that is still moving in year five needs a sentence saying why.

**Drag and offsets together (rule 13).** He never shows a drag alone. When he assumes expansion he names the offset and tests it: economies of scale count "only if a company has significant operating expenses (SG&A, marketing) that grow at a rate lower than revenues"; the gap between gross and operating margin is his rough measure of that potential. When he sees a drag (Meta's Reality Labs, Amazon's build-out) he asks what the spending buys and when. For a company spending heavily on assets, the depreciation those assets will carry is arithmetic from the capex plan and the asset lives in the 10-K; the offsets are mix shift, costs growing slower than revenue, and the revenue the assets produce. Both columns, side by side, in `detail`.

**Margin convergence.** Margins far above the competitor set invite entry; a target above the industry needs a moat argument from `business.md` section 5, and the terminal premium (rule 5) must tell the same story.

## 5. Reinvestment

**Sales to capital is chosen among three candidates, and the reason says where you landed and why.** His worked table lists the firm's own ratio, last year's marginal ratio, and the industry average, then picks: "approximately midway through their marginal sales to capital ratio from last year and the industry average" for one firm; "well below the industry average and the firm's marginal ratio ... as competition increases, [it] will have to invest increasing amounts" for another. Build the same table in `detail`:

| Candidate | Where it comes from |
|---|---|
| The company's own record, lagged the way the engine spends (rule 12) | capex less depreciation, acquisitions, working capital, per year, against the revenue added the following year |
| Last year's marginal ratio | the same, latest year only |
| The industry average | cached `capex.csv`, column "Sales/ Invested Capital (LTM)", industry row and date named |

Then state the chosen `value` and `value_late` against those three. Reinvestment in his definition is broad: capital spending net of depreciation, plus acquisitions, plus working capital, plus capitalized research where that switch is on.

**A company that has invested ahead of its growth is not penalised for it.** Nvidia in 2023 had generated "only 65 cents in revenues for every dollar of capital invested" during its build-out; he read that as a depressed marginal figure and let the forward ratio "approach the global industry median". Tesla with idle capacity got a high early ratio "since Tesla contends ... to have capacity online ... enough to cover growth for the next year or two", then a lower one. Our tools for the same judgment: the lagged history (rule 12), `value` above `value_late` when capacity is already built, `reinvestment_override` where guidance names a spending level (and then the gross capex the ratio implies in every explicit year is checked against that guidance), and `switches.reinvestment_lag` when assets take more than a year to earn (he used three years for Nvidia in 2024-25).

**Run the implied return on capital check.** This is the check he insists on and the one most often skipped: "If the sales-to-capital ratio is set too high, the return on capital in the later years will be too high, while if it is set too low, it will be too low." Compare the year-ten implied return (the engine prints it, and `uv run value <TICKER> --dry-run` shows it without a value per share) with the industry's return and with the cost of capital. A year-ten return of 40% against a 10% cost of capital in a sector earning 15% means the company is being asked to grow without paying for it; lower the ratio until the return converges. The reverse holds too.

**How much it matters.** For a company whose story is about market size and share, the ratio moves value less than growth and margin do; for a heavy investor it is a first-order input. Spend your effort accordingly, but never leave the check unrun.

## 6. Cost of capital

The engine builds it (rule 6, section 18.3): bottom-up beta from his industry table, his implied equity risk premium, the company's own debt weights. Your part is the industry choice and the sanity check, and his rule is not to fine-tune: "analysts spend too much time finessing and tweaking the cost of capital and not enough on the cash flows"; "costs of capital of 15% or 6% are just off the table". Check the built rate against his distribution (the cached `wacc.csv` gives industry rates; his published US band runs from about 6% at the tenth percentile to about 12% at the ninetieth, with the median near 8%). A young, unprofitable company starts near the top of the band and drifts to the median as it matures; a large profitable one sits near the median already. Two things the rate must never carry: failure risk (a separate probability) and management quality (a story input, expressed through growth and margin). The cost of capital is shared across the three cases; scenarios vary the business, not the market's price of risk.

## 7. Terminal value

One paragraph, because the companion note covers it. Growth forever is capped at the risk-free rate, his proxy for nominal growth of the economy (`value: riskfree`). The terminal cost of capital is the mature firm's. Excess returns "move towards zero in stable growth", with discretion: zero for a firm with no durable advantage, positive for a firm with a strong one, and he used a positive premium for every moated firm he published. The premium must agree with the moat sentence in the story, sit below today's return and below the year-ten implied return (rule 5), and the transition check must not flag a cliff. His two banned practices: growing the last explicit year's cash flow as if it were the terminal one, and letting a stable-growth firm stop reinvesting.

## 8. Three of his valuations, compressed

Full quotes and URLs are in the sourced notes. The pattern in all three: each number sits inside a named distribution and the company is placed within it by an argument about its business, not by its own historical average.

**Uber, June 2014.** Story: a matchmaker between drivers and riders, an urban car service with local network benefits and a low-capital model, keeping its 20% slice of fares. Inputs: total market 100 billion USD growing 6% a year (built city by city from Tokyo, London and US taxi revenue, plus a judgment for the rest of the world); share 10% ("at the optimistic end", because regulation and me-too competitors); target margin 40% ("towards the top decile of technology companies", because the cost of a city network falls relative to revenue once built); sales to capital 5.0 (technology median about 2.5, all-US median about 2.0, "a really high number would be about 10"); cost of capital 12% falling to 8% (top decile of US companies, then the median, because it will not carry a transport company's debt); failure 10%, liquidation value zero. Result about 6 billion against a 17 billion price. He then published the counter-story's inputs and showed they gave 54 billion, to make the point that the disagreement was about story, not arithmetic; a year later he conceded the margin was too high.

**Nvidia, June 2023.** Story: the customers of the last decade (gaming, crypto) are maturing; AI chips (a 15 billion market in 2022, 80% share, estimates of 200 to 300 billion by 2030) and automotive step in; still less than half the revenue of Intel or TSMC, so room to grow. Inputs: revenue by segment because the engines diverge, reaching 267 billion in 2033; margin 35% next year and 40% by 2027 on a research-adjusted basis, held ("the company delivered 42.5% in 2020 and 38.4% in 2021"; gains must come from price because TSMC makes the chips); sales to capital 0.65 (the depressed 2022 figure after a decade of heavy investment) moving to 1.15, the global industry median; cost of capital 12.21% (the US semiconductor industry average, chosen over his own 13.13% build) drifting to 8.85%; no failure risk. Result about 240 a share against 409; the price sat near the 95th percentile of his simulation.

**Alphabet, February 2024** (his last published Alphabet workbook; before the 2025-26 spending surge, so a reference for method, not for today's numbers). Trailing revenue 307 billion, research capitalized, adjusted margin 32.2%. Inputs: growth 8% for five years fading to the 4.08% risk-free rate by year ten; target margin 30% reached in year five; sales to capital 1.20 throughout; cost of capital 8.84% to a stable 8.00%; stable return on capital 15% against that 8% (a seven-point premium); tax 13.9% to 25%; no failure risk. His Magnificent Seven sales-to-capital choices the same month: Alphabet 1.20, Meta 1.50, Amazon 2.00, Microsoft 3.00, Apple 5.00, Nvidia 1.15.

## 9. Your self-check before you hand the file to the reviewer

Each of these is a mistake a previous draft in this library made and he would not have:

1. Year-one growth sits at the trailing run-rate unless a named item in the latest filings moves it.
2. The path fades toward the end state the story implies, never toward the company's own five-year average after its mix has changed.
3. Sales to capital is chosen among the three candidates, against the lagged record, with the position stated; an investment surge is read as a depressed marginal figure, not as the future ratio.
4. Every drag on margin has its offsets beside it, and growth spending inside operating expense is named before the path is set.
5. The terminal return on capital matches the story's moat claim and the year-ten implied return; no cliff.
6. Every number is placed in a named distribution: industry row and date, named comparables, the company's own best years.
7. Year-ten revenue is compared with the largest firms in the sector and with the market size, and growth agrees with margin.
8. The cost of capital is inside the plausible band, shared across cases, and carries neither failure nor management quality.
9. The three cases are three stories; the base case is the expected value; management's numbers are tested, not averaged in.
10. The `story_to_numbers` table is complete in both directions: every input has a sentence, every sentence that sets an input has a row.

## 10. What the reviewer asks

The reviewer answers each question in one line in the review file, with the cell or the quote that settles it. A "no" is a REVISE item.

1. Are the bear, base and bull stories three different business outcomes, or one story with dials moved? Name the sentence that makes each different.
2. Does year-one growth start at the latest reported run-rate, and if not, which sourced item in the latest filings moves it?
3. Is the year-ten revenue compared with the largest companies in the sector today and with a market size, and is the implied share plausible for the competition the story describes?
4. Is the target margin placed inside a named distribution (industry row and date, named comparables, the company's own best years), and does the business-model argument for its position hold?
5. Do growth and margin agree, or does a niche-margin story carry mass-market revenue?
6. Is sales to capital chosen among the firm's lagged record, its latest marginal ratio and the industry figure, with the position explained; and does the year-ten implied return on capital in the dry run sit within the band the industry and the cost of capital allow?
7. Where the company has invested ahead of growth, is that handled (early ratio, override, lag) rather than penalised?
8. Is the cost of capital inside the plausible band, shared across cases, free of failure risk and management quality?
9. Does the terminal premium match the moat claim in the story and the year-ten implied return, with no cliff in the transition check?
10. Is the `story_to_numbers` table complete in both directions, and does each row's number match its cell?
11. Is the base case an expected value? Point to any input chosen as the lower of two defensible numbers "for safety" and ask for the one the story supports.
12. Against the previous draft (if any), did the analyst's numbers move in both directions, or only one way?
