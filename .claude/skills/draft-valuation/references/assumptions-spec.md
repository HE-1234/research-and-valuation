# Valuation assumptions specification

Read before drafting or reviewing assumptions, or changing their schema. This file owns the input format and sixteen analyst rules. Use the [playbook](analyst-playbook.md) for practical method references and [workflow contracts](workflow-contracts.md) for authorization, redrafts and owner review.

<a id="section-18-4"></a>

## 18.4 `assumptions.yaml` — the single source of inputs

**Number units.** Numeric rates in YAML, CLI overrides and formulas use decimal fractions: `0.12` means 12%, and `1.20` means 120%. App percentage fields convert on entry and display; do not put a percent string or a whole-percent number into a decimal input. Return premiums are additive differences: `0.08` means 8 percentage points above the cost of capital. Growth and returns can exceed 100%; size alone does not establish a units error. A finite positive terminal return premium at or above `1.0` is permitted only with the existing `allow_large_premium: true` and a reason under rule 5; its warning remains. This exception does not change tax, probability, discount-rate or terminal-growth bounds. Bear premiums remain nonnegative; a positive premium needs a supported reason under rule 5. Never divide an existing assumption by 100 merely to pass validation.

Every input cell is a mapping with `value`, `reason`, and where the number comes from a document, `source` (a [reader-rule §3](../../../../docs/research.md#section-3) source tag). Per-year inputs use `values`: a list of five numbers for years 1–5 (years 6–10 follow the [§18.2](model-spec.md#section-18-2) rule), or ten when the analyst shapes the fade years explicitly. Any cell may be `null` where the analyst has nothing defensible; the engine refuses to compute a scenario with a `null` in a required cell and says which. Reasons are one to three plain sentences that point at the report (`business.md §3`, `outlook.md §4`) and, where a number is involved, at a source. Any cell may also carry `detail`: the working notes behind the reason (history tables, the arithmetic, the alternatives considered), as long as needed. The app shows `detail` in a fold-out under the reason and `assumptions.md` prints it after the reason; nothing goes into YAML comments, because the owner never sees comments.

```yaml
schema: 1
ticker: MRVL
company: Marvell Technology, Inc.
as_of_quarter: FY2027-Q2         # the library's latest outlook quarter
as_of_date: 2026-08-28           # that quarter's cutoff date
drafted: 2026-09-07
currency: USD
units: millions
horizon: 10                      # five explicit years plus five faded by rule (§18.2); the 5-year-stop reference is always computed too

base_year:                       # trailing twelve months ending at as_of_quarter
  period: "Q3 FY2026 – Q2 FY2027 (TTM)"
  revenue:                      {value: 0, source: "[...]"}
  operating_income_gaap:        {value: 0, source: "[...]"}
  one_time_items:               # each: positive = a charge to add back, negative = a gain to remove
    - {name: "...", value: 0, source: "[...]", reason: "why this is genuinely one-time"}
  amortization_of_acquired_intangibles: {value: 0, source: "[...]"}   # memo row; deducted unless the switch is on
  stock_based_compensation:     {value: 0, source: "[...]"}           # memo row; never added back
  rnd_expense:                  {value: 0, source: "[...]"}           # memo row; used only if capitalize_rnd
  effective_tax_rate:           {value: 0.0, source: "[...]", reason: "..."}
  invested_capital:             {value: 0, source: "[...]", reason: "book equity + debt + leases − cash; for the ROIC check"}
switches:
  addback_acquired_amortization: false
  capitalize_rnd: false
  rnd_amortization_years: 5
  rnd_history: []               # oldest first, at least rnd_amortization_years entries, if capitalize_rnd
  reinvestment_lag: 1           # 0–3 years, as his ginzu allows: 1 = money spent in year t buys growth in t+1 (default); 0 = same-year (his Alphabet 2018 sheet); he used 3 for Nvidia in 2024–25

bridge:                          # firm value → equity; all as of the latest balance sheet
  cash_and_marketable_securities: {value: 0, source: "[...]"}
  debt:                           {value: 0, source: "[...]"}
  operating_lease_liabilities:    {value: 0, source: "[...]"}
  non_operating_assets:           # named, at carrying value
    - {name: "...", value: 0, source: "[...]", reason: "..."}
  minority_interests:             {value: 0, source: "[...]"}
  other_claims:                   # e.g. contingent consideration, earn-outs
    - {name: "...", value: 0, source: "[...]"}
  probability_of_failure:         {value: 0.0, reason: "..."}
  distress_proceeds:              {value: 0, reason: "what the assets would fetch in a failure"}
  diluted_shares:                 {value: 0, source: "[...]", reason: "latest-quarter diluted weighted average"}
  dilution_note: "known future dilution sources, one sentence"

market:
  price: auto                    # 'auto' = fetched at compute time (Yahoo chart endpoint), or a number
  risk_free_rate: auto           # 'auto' = FRED DGS10 latest, or a decimal
  equity_risk_premium: auto      # 'auto' = latest row of Damodaran's ERPbymonth.xlsx (cached), or a decimal
  mature_market_erp: 0.045       # Damodaran's mature-market default
  marginal_tax_rate: 0.25

cost_of_capital:
  method: build                  # build | pinned
  pinned_value: null
  build:
    damodaran_industry:     {value: "Semiconductor", reason: "..."}
    unlevered_beta:         {value: 0.0, source: "[Damodaran betas.xls <date>, <industry>]", reason: "..."}
    debt_to_equity_market:  {value: 0.0, source: "[...]", reason: "debt + leases over market cap"}
    pretax_cost_of_debt:    {value: 0.0, source: "[...]", reason: "actual coupon / synthetic rating"}
  terminal:
    method: mature               # mature | hold | value
    value: null
    reason: "..."

diagnostics:
  final_year_market_size:   {value: null, source: "[...]", reason: "the 'big market' test: total spend the company could address in the final model year (year 10 by default); a sourced nearer-year market carried forward at a stated growth rate is allowed if the reason labels it an inference and gives the arithmetic in detail"}
  historical_revenue_cagr:  {value: null, source: "[...]", reason: "optional: the company's own five-year revenue growth, for the 'vs own history' check"}
  historical_operating_margin: {value: null, source: "[...]", reason: "optional: the company's own five-year average GAAP operating margin"}

scenarios:
  bear:
    weight: 0.25
    story: |
      Three to five plain sentences: what has to be true for this case.
    story_to_numbers:              # rule 14: one row per sentence of the story that sets an input
      - {says: "one sentence of the story", drives: "revenue growth, years 1 to 2", number: "the number as written in that input", source: "[...]"}
    revenue_growth:        {values: [0, 0, 0, 0, 0], reason: "...", source: "[...]"}
    operating_margin:      {values: [0, 0, 0, 0, 0], reason: "...", source: "[...]"}
    sales_to_capital:      {value: 0.0, value_late: 0.0, reason: "...", source: "[...]"}
    reinvestment_override: {values: [null, null, null, null, null], reason: "explicit net reinvestment in USD millions where guidance is specific; null = use sales-to-capital"}
    tax_rate:              {start: 0.0, terminal: 0.25, reason: "..."}
    cost_of_capital_override: null          # a decimal pins this scenario's WACC; null = shared
    terminal:
      growth:              {value: riskfree, allow_above_riskfree: false, reason: "..."}   # 'riskfree' = the run's risk-free rate (Damodaran's default), or a decimal
      roic_premium:        {value: 0.0, allow_large_premium: false, reason: "points above terminal WACC; justify the advantage retained or lost in this outcome"}
  base:  { ... same keys ..., weight: 0.50 }
  bull:  { ... same keys ..., weight: 0.25 }
  management:
    computable: false            # true only when at least one multi-year revenue or margin target exists
    reason: "..."
    guidance:                    # every quantitative or qualitative item management has given, whether used or not
      - {item: "...", quote: "verbatim", source: "[...]", used_as: "revenue_growth year 1 | reinvestment year 1 | not numeric"}
    revenue_growth:        {values: [null, null, null, null, null], reason: "...", source: "[...]"}
    operating_margin:      {values: [null, null, null, null, null], reason: "...", source: "[...]"}
    sales_to_capital:      {value: null, value_late: null, reason: "..."}
    reinvestment_override: {values: [null, null, null, null, null], reason: "..."}
    tax_rate:              {start: null, terminal: 0.25, reason: "..."}
    cost_of_capital_override: null
    terminal:
      growth:              {value: null, allow_above_riskfree: false, reason: "..."}
      roic_premium:        {value: null, allow_large_premium: false, reason: "..."}
```

An optional top-level `sources:` list maps every tag used in the file to its cached text: `- {tag: "10-Q Q2 FY2027", file: "sources/FY2027-Q2/10-Q-FY2027-Q2.txt", date: "2026-08-28", note: "..."}`. `assumptions.md` prints it as its Sources table. Two more optional top-level blocks the engine and the app maintain; analysts never write them:

```yaml
owner_edited: 2026-09-08T10:12:00      # last save from the app
changelog:                              # appended by the app on every save, oldest first
  - {at: "2026-09-08T10:12:00", path: "scenarios.base.operating_margin.values.4", old: 0.30, new: 0.32, note: "owner: depreciation offsets look achievable"}
```

**Rules for the analyst filling it in:**

1. **Base facts are reported; economic adjustments are reconciled.** Preserve reported operating income and record sourced one-time adjustments separately; recurring charges are not one-time. Stock-based pay stays expensed. Acquired amortization is deducted by default, shown as a memo and addressed in the margin path. On an initial or explicitly authorized redraft, the analyst assesses material R&D, acquisition and other accounting differences with the accounting reference ([§18.11](model-spec.md#section-18-11)), and may propose a supported switch with a complete reconciliation across profit, capital, reinvestment and taxes. Do not make only the favorable half of an adjustment or imply that a switch supplies an entire forecast. Explain a material retained simplification; an unsupported material treatment follows [§13](../../../../docs/review.md#section-13). Existing owner choices remain fixed outside an authorized redraft.
2. **Interest income and interest expense are not in operating income.** Cash is valued in the bridge, not in the cash flows.
3. **Sources first, reports second.** Base-year and bridge numbers come from the cached 10-Q/10-K text, tagged. Scenario reasoning points to `business.md` and `outlook.md` sections and their underlying sources. The runner closes valuation-specific evidence gaps under rule 16 before handing the cache to the analyst; the analyst requests specific missing evidence from the runner and fetches nothing itself. This permits targeted peer and market research, not rebuilding the research reports. Market data and Damodaran's datasets follow [§18.8](model-spec.md#section-18-8).
4. **Management case.** Guidance ranges become midpoints. Qualitative guidance ("capex up significantly") is recorded in `guidance` with `used_as: not numeric` and never turned into a number. Long-term targets already captured in the reports count. `computable` is true only when management has given at least one multi-year revenue or margin target; otherwise fill what exists and leave `computable: false`. The management case is never weighted. Guidance is mapped to the nearest model year and the approximation noted, since fiscal years and trailing-twelve-month windows do not line up.
5. **Terminal discipline.** Terminal growth defaults to `value: riskfree`, a house choice using Damodaran's ceiling as a starting point, not a requirement to grow at that ceiling. Explain why the mature company keeps pace with, grows slower than, or shrinks relative to its economy, in the valuation currency. Growth above the run's risk-free rate requires `allow_above_riskfree: true`, a reason and a warning; lower or negative growth needs a reason too. For every case, including bear, choose mature ROIC from the business's expected economics and rule 16 benchmarks before checking the transition. Bear may retain an advantage; a positive premium requires a supported reason, while zero remains allowed when the selected adverse outcome earns no excess return. Do not force moat loss from the scenario label or tune forecast investment to approach a predetermined terminal return. Explain which advantage persists after the forecast, why competitors or customers cannot fully capture it, and how it supports the chosen excess return and its duration. A finite contract or one product generation cannot by itself justify excess returns forever. Show normalized current, final-year and benchmark returns, terminal WACC, the selected ROIC and its implied premium, and terminal reinvestment as growth divided by ROIC. Explain the capital and profit definitions, including goodwill and R&D; show reported and adjusted comparisons together and never discard goodwill solely to obtain a desired bound. Returns on existing capital are context for returns on future investment, not mechanically interchangeable. Terminal ROIC need not be below a depressed current ROIC; a recovery or business-mix change must be justified. Likewise an unusually high final-year ROIC can mean the forecast underpays for growth, rather than that terminal ROIC must rise. Resolve transition warnings under [§18.2](model-spec.md#section-18-2) without calibrating to its thresholds. Bear and base premiums above 0.08 and bull premiums above 0.12 require `allow_large_premium: true` and a reason; these are house warning thresholds, not supported targets. Damodaran's published historical premiums in `tools/valuation/damodaran-notes/` illustrate choices, not present-day company benchmarks.
6. **Cost of capital is shared** across scenarios unless a scenario sets `cost_of_capital_override` with a reason. Scenarios vary the business story, not the market's price of risk. Apply the business-drivers risk comparison to economically similar library companies and plausible dataset classifications; explain material differences in operating exposure, financing and mature rates rather than copying a sector label or the rate that produces a preferred value.
7. **Case definitions and weights.** Apply [uncertainty and bias](uncertainty-and-bias.md#apply-to-this-repository): base is the best-supported central operating outlook; bear and bull are credible adverse and favorable outcomes, with severity, dependencies and management response explained. Define the outcomes before assessing their weights. Weights default 0.25 / 0.50 / 0.25 and must sum to 1. Label these as house probability assumptions, preserve owner values, and explain proposed alternatives on an authorized redraft. Assess the credibility of the combined scenario at its proposed weight, identify provisional odds and material mismatches, and never infer probability from a list of disclosed risks. Base uses no safety haircut; its result is distinct from the probability-weighted expected result. Three scenarios do not imply statistical confidence bounds.
8. **Test possibility, economic plausibility and likelihood separately.** Check feasible demand and scale, consistent margins and reinvestment, and evidence for the combined business outcome. Management's delivery record informs the last check but does not establish a probability. A different case may arise from adoption, pricing or execution within the same business; dramatic structural change is not required. The reviewer compares material choices with credible alternatives under the review checklist, rather than accepting possibility as proof that a path is central or deserves its weight.
9. **Stories are prose for the 16-year-old**, three to five sentences, no numbers except the one or two that define the case.
10. **Year 1 starts where the company is.** Year-1 revenue growth starts from the latest reported run-rate (the most recent half-year or quarter against the year-earlier period, stated with its source) and moves off it only for a specific, sourced reason named in the reason: guidance for the coming year, a comparison-period effect management has called out, a contract won or lost, capacity that is or is not arriving. "Growth slows because the company is big" is not a reason. (GOOGL lesson, 2026-09-08: the first draft wrote 20% against a reported 23%.)
11. **Growth is built from the parts, not from the past.** The revenue-growth `detail` of every computed case carries a segment build: each reported segment or product line with its trailing revenue, its latest growth, and the growth assumed for it in years 1, 3 and 5, summing to the company path. Where the reports hold a backlog, a market size or a capacity plan, the build uses it. Segments that share one growth engine may be carried as one line when the detail says so; Damodaran splits a company only where its parts have different growth engines (Nvidia, Amazon) and warns that line items with no basis for forecasting them create the illusion of precision. The company's own five-year history and the industry figure are context in the diagnostics, not anchors: a company whose mix has changed (a cloud unit that was 10% of revenue and is now 25%) does not fade back to the growth its old mix produced. Every step down of more than three points between one year and the next has one sentence naming the driver (backlog conversion slowing, a market filling up, a product cycle ending). (GOOGL lesson: the first draft faded to 8% by year 5 "toward the single digits of 2022–2023" while Cloud, a quarter of revenue, was growing 82% with a backlog above a year of company revenue.)
12. **Reinvestment history is measured the way the model spends it.** With `switches.reinvestment_lag: 1` (the default: this year's spending buys next year's growth) the sales-to-capital history in `detail` is computed lagged the same way, and the chosen ratio is set against that lagged record. A same-year ratio taken during an investment surge is depressed by construction and is not the comparison. (GOOGL lesson: 0.9 was chosen against same-year figures of 0.64–0.75 while the lagged record read 1.2–2.1.)
13. **Margins carry their own bridge.** A margin path that moves more than two points over the five years shows, in `detail`, both forces side by side: the depreciation the reinvestment path will create (from the capex plan and the asset lives management gives) and the offsets (mix shift toward higher-margin units, costs growing slower than revenue, the operating leverage the reports describe). A path that shows only the drag is incomplete. For material build-outs apply the [investment-payoff check](business-drivers.md#investment-payoff-check), including committed/discretionary spending, commissioning, utilization, management response and recovery timing. Explicitly assess years 6–10; use ten annual inputs when the default fade or fixed year-five margin would preserve a temporary condition.
14. **Every number has a sentence; the initial story is a hypothesis.** The analyst reads `.claude/skills/draft-valuation/references/analyst-playbook.md` and its applicable topical references ([§18.11](model-spec.md#section-18-11)) before writing a number, writes a provisional story before its numbers, revises both when operating evidence or arithmetic contradicts the hypothesis, and then fills that case's `story_to_numbers` table: one row per sentence of the story that sets an input, naming the input (`drives`) and the number as it is written in that input cell (`number`). Every input the case carries (the growth path, the margin path, sales-to-capital, the terminal premium, any reinvestment override) appears in at least one row, and no row names a number the story does not motivate. An input with no sentence is a number without a reason; a sentence with no number is decoration. A polished explanation does not rescue an unsupported number: compare credible alternatives and record material reconsiderations in the relevant working notes. The engine warns when a computed case has no table and stops on a malformed row; the app shows the table on the stories page and `assumptions.md` prints it under each story.
15. **Explain the choice, not just the direction.** Each material judgment's visible `reason` states what must be true and why the selected level is defensible. Its `detail` separates (a) observed facts and management guidance, with dates and sources; (b) the analyst's assumptions about demand, price, competition, costs or capital; (c) arithmetic connecting those assumptions to the input; (d) a defensible range, a materially different credible alternative and why the evidence favors this case's position; and (e) an observable development that would change the judgment. Cover growth, margin, early and late reinvestment, taxes, discount-rate choices, terminal growth and return, failure assumptions, and material switches; shared inputs can carry one explanation referenced by each case. Label house defaults and mechanical interpolation as assumptions too. A citation to a growth driver does not establish the analyst's chosen percentage. Revenue builds reconcile every explicit year (show rounding differences), and give year-5 and final-year revenue, the relevant market/share or a sourced alternative demand bound, and the expected mature business mix. Use disclosed units times price, customers times spending, market times share, or capacity times utilization where useful; do not fabricate undisclosed components. When evidence cannot distinguish nearby percentages, say so and use a rounded judgment within the supported range. A populated `story_to_numbers` table or passing validator does not prove any of this.
16. **Research the mature destination.** Before drafting, the runner prepares `sources/<QLABEL>/notes-valuation-evidence.md`: missing evidence by input; a benchmark table; source definitions and limitations; and unresolved gaps. Reuse eligible cached sources across the library first, then fetch the specific pre-cutoff company filings, market evidence or industry data needed to close material gaps, using [§12](../../../../docs/sources.md#section-12)'s source and caching rules. Record new sources in the manifest and map cited tags to cached text; reuse another company's cache by exact path when appropriate. This targeted research is part of drafting and needs no separate owner approval. Start with two to four named companies or business segments that illuminate the future economics, selecting for business model and maturity rather than a shared sector label. Explain inclusions, exclusions and why today's mature analogue resembles the subject's future mix; do not choose only exceptional survivors. Show observed revenue/scale, growth, operating margin, reinvestment or sales-to-capital, and ROIC where relevant and disclosed, using several years when cyclicality or one-off items matter. Reconcile GAAP versus adjusted profit, R&D, goodwill, leases, capital denominators, fiscal periods and gross versus net revenue; mark an unusable metric rather than forcing comparability. Distinguish observed peer outcomes, broad industry aggregates and another analyst's forecasts: Damodaran's old valuation inputs are examples of judgment, not realized peer performance. An industry mean is not a percentile or a distribution. Do not multiply separately aggregated margin and capital ratios and call the result observed industry ROIC without verifying compatible definitions and populations. Explain why each target should converge to, exceed or fall below its benchmarks. If suitable peers do not exist, document the search and substitute sourced unit economics, industry ranges or a normalized own-company record; peer count alone is not a gate. If neither peer evidence nor a defensible substitute supports a material assumption, keep the dependent input unsupported and mark the required check BLOCKED under [§13](../../../../docs/review.md#section-13). Passing with a caveat is not a substitute for missing evidence.
