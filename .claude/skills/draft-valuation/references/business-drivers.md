# Business drivers: connect the operating story to the forecast

Read when drafting or reviewing growth, margins, reinvestment, risk and terminal inputs. [§18.4](assumptions-spec.md#section-18-4) is authoritative. The [teaching library](../../../../tools/valuation/damodaran-notes/README.md) links original sources; [worked examples](worked-examples.md) are dated illustrations, not current benchmarks. Put company-specific evidence and calculations in input `detail`, with the essential judgment visible in `reason`.

## Revenue: define the destination and explain the path

Start with the current TTM revenue and the latest comparable growth rate. Identify the units that genuinely drive the business: customers and spending, volume and price, market and share, or capacity and utilization. Segment only where growth engines differ and evidence supports the split. Extra unsupported line items create apparent precision without better information.

Describe what the company has become at year 5 and the final forecast year: total revenue, business mix, relevant market and share, and scale relative to mature comparables. Then connect the near-term path to that destination. A large market establishes opportunity, not the company's ability to win it. A backlog establishes some contracted demand, not perpetual market share. Distinguish cancellations, conversion timing, remaining orders and new business; do not count an existing order twice.

Reconcile each explicit year's segment amounts to company revenue and growth, showing rounding differences. Explain changes from current growth and material steps in the path with sourced drivers and labelled judgments. Show the implied unit/share or capacity requirement where possible. When only the direction is observable, give a supported range and explain the rounded choice; the source need not predict the exact rate. Do not invent a unit-price decomposition the company does not disclose.

The current run-rate is a starting observation, not an instruction to extrapolate a peak indefinitely. Apply the model-selection guide for cycles, temporary effects and mix changes. Historical company growth and industry forecasts provide context on a comparable basis; neither automatically determines the mature rate. If market size is unavailable, use a documented sourced demand bound or alternative operating check and identify its limits. Required support cannot be replaced by optimism about management's spending.

Source connection: [narrative-and-numbers.txt](../../../../tools/valuation/damodaran-notes/sources/narrative-and-numbers.txt), the process connecting narrative, drivers and checks. Quantitative peer-research and reconciliation requirements are our implementation in rules 11, 15 and 16.

## Margins: explain both costs and offsets

Show the reported starting margin and any reconciled economic adjustments. Explain the target using comparable observed economics: customer pricing power, incremental production costs, business mix, mature competitors and the company's normalized history. Keep segment and consolidated margins distinct and reconcile GAAP versus adjusted measures. Industry means and historical analyst forecasts are not observed peer distributions.

Bridge the margin path through material costs and offsets: price/mix, supplier/customer bargaining, utilization, operating expenses relative to revenue, depreciation from capital spending, and acquired-amortization roll-off. Scale only reduces relative costs where the cost structure supports it. Spending on growth cannot both disappear from operating expense and be omitted from reinvestment. Apply [accounting-and-reinvestment.md](accounting-and-reinvestment.md).

The path's timing must agree with hiring, capacity, depreciation and pricing assumptions. Flat margins during a large cost increase require an offset just as expanding margins do. Faster growth bought through lower prices may reduce margins; high growth and high margins together require evidence. A premium over mature peers needs a specific advantage and a reason it survives competition.

Assess year five and years 6–10 explicitly. Identify whether investment pressure, scarce supply, restructuring or unusual pricing is still affecting year-five economics. Choose the timing and extent of recovery or deterioration from evidence; show ten annual inputs when the default fade or flat margin would freeze a temporary condition. Keeping margins flat may be defensible, but must follow the expected economics rather than the length of the input list.

## Reinvestment: pay for the growth being forecast

Compare three distinct pieces of evidence: the company's multi-year incremental record, its latest incremental ratio, and a relevant industry's or mature peer's stock sales-to-invested-capital ratio. Name definitions, dates and differences rather than treating these as identical statistics. Show net capex, acquisitions, noncash working capital and any capitalized growth spending; match the lag between spending and the resulting revenue.

Choose early and late capital efficiency according to capacity already installed, utilization, asset lives, incremental capital requirements and the mature business mix. Existing spare capacity can support growth with little immediate spending; it does not justify free growth forever. Convert the chosen ratio or override back into actual net investment and, where guidance exists, reconcile to gross capex. A lower ratio means more capital is needed per dollar of added sales.

Review the resulting returns on capital alongside operating profit and investment. The engine rolls historical capital forward; its implied average ROIC is not a direct observation of marginal project returns. A high final-year return can reflect a durable advantage, a distorted capital denominator or insufficient reinvestment. Investigate all three. Do not force a ratio or terminal return merely to clear a diagnostic.

### Investment-payoff check

For a material build-out, connect the spending schedule to its operating payoff in the existing margin/reinvestment working notes: committed versus discretionary spending, capacity commissioning and utilization, the revenue or cost savings it can support, depreciation and replacement needs, and the timing of margin and cash-flow recovery. Use disclosed quantities where available and labelled ranges where they are not; no invented capacity decomposition is required. Explain what management can defer, cancel, sell or redirect when demand disappoints, including commitment limits and exit costs. High spending does not guarantee a payoff, and weak demand does not imply every discretionary budget continues unchanged.

Compare the selected path with the nearest credible alternative that changes the spending duration or payoff. Explain why the evidence favors the selected combination of revenue, margin and investment. Avoid counting capacity already funded twice, giving unsupported free growth, or choosing late investment efficiency just to match a predetermined terminal return. Put missing material evidence in the evidence note and apply the existing evidence-gap rules.

Source connection: [growth-and-value.txt](../../../../tools/valuation/damodaran-notes/sources/growth-and-value.txt), “Paying for Growth” and “Excess Return Effect”: investment and the return it earns determine whether growth adds value. Formula and lag choices are specified in [§18.3](model-spec.md#section-18-3).

## Risk: use the appropriate discount rate

Explain the supported build's business exposure, debt weights, currency and operating-country risk. A listing location does not establish operating risk; one industry label may poorly represent a mixed business. Compare with relevant dated data, not fixed bands lifted from old valuations. Use a supported override with a reason or disclose a capability limitation when the required treatment exceeds the build.

Cross-check the classification against economically similar businesses already in the library and the closest relevant dataset alternatives. Explain material differences in beta, financing treatment and mature discount rate using operating exposure and consistent dates/definitions. Similar companies need not have identical rates, and a previous company's choice is not itself evidence; correct or qualify an inconsistent comparison rather than copy the lower rate. Record this in the evidence note and shared risk-input detail, without using valuation results to select a rate.

Keep operating outcomes in cash flows, systematic risk in the discount rate and discrete outcomes explicitly identified, applying [uncertainty-and-bias.md](uncertainty-and-bias.md). The rate is not a miscellaneous penalty for concerns already reflected elsewhere. The shared-rate convention does not eliminate the need to justify the risk assumptions.

## Terminal state: a mature business, not a plug

Describe mature business mix, growth, margins, risk and capital efficiency together. Select a supported range for returns on future investment using normalized company and mature-peer evidence before looking at the transition warning. Distinguish that economic judgment from the accounting return on accumulated capital.

If ROIC exceeds the cost of capital after the forecast, identify the advantage that sustains it, why competitors/customers cannot fully capture it, and what could end it. A finite customer contract alone cannot support a perpetual premium. Growth at the risk-free ceiling is a house default, not an obligation. A mature company can grow more slowly or shrink.

Show terminal growth, WACC, ROIC, premium and implied reinvestment together. For illustration, 3% growth at 15% ROIC requires reinvesting 20% of after-tax operating profit; at 9% ROIC it requires about 33%. These describe different capital requirements. They are not company estimates.

The terminal return need not be below a depressed current return; a recovery requires evidence. Nor must it rise just because the explicit forecast produces unusually high ROIC. Apply [§18.2](model-spec.md#section-18-2) to every case: investigate a warning, document its economic disposition, and never tune to its threshold. Bear may earn excess returns when its adverse business outcome retains a defensible advantage; zero is an economic assumption to justify, not a required destination. Existing saved zero premiums remain unchanged outside an authorized edit or redraft.

Source connection: [terminal-value.txt](../../../../tools/valuation/damodaran-notes/sources/terminal-value.txt), “Characteristics of Stable Growth Firm”, “Project Returns” and “Reinvestment and Retention Ratios”; [growth-and-value.txt](../../../../tools/valuation/damodaran-notes/sources/growth-and-value.txt), “Two Dangerous Practices”. Historical excess-return examples illustrate discretion, not a premium to copy.
