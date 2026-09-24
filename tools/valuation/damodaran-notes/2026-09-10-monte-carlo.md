# Monte Carlo extension of the existing FCFF engine

Written 2026-09-10. Focused method research; no company assumption calibration or redraft. New web sources below were inspected on this date; linked passages, rather than historical company numbers, support the method. The implementation choices below are proposals for this app, not rules attributed to Damodaran.

## Sourced guidance

- Select the few uncertain inputs that materially affect value; distributions can use relevant company history, comparable observations, or explicit judgment when data is insufficient. Structural changes limit historical calibration. Correlated inputs should be linked explicitly or reduced to fewer drivers. Keep an appropriate risk-adjusted discount rate: drawing uncertain cash flows does not itself replace that rate. Distribution and dependence misspecification remain limitations. [D1, printed/PDF pp.22–26, 36–38]
- Damodaran's Apple example starts from a deterministic valuation, selects operating drivers, uses a bounded triangular distribution for target margin, and explicitly relates margin to growth. His illustrative Apple correlation and parameter values are company- and date-specific; they are not calibration for this repository. He reads value percentiles conditional on his assumptions. [D2, Steps 1–6]
- His lecture reports the simulation mean, spread, observed extremes, and frequency below a chosen threshold, together with a plot. It recommends joint distributions for correlated variables. [D3, Monte Carlo Simulations, Steps 3–5]
- Growth requires investment; terminal reinvestment must agree with growth and the return on new investment. Finite-period changes in margin and utilization can temporarily separate observed growth from sustainable growth. [D4, “Paying for Growth” and “Excess Return Effect”]

## Minimal implementation proposal

Simulate one selected, computable case around its current app inputs. Do not treat bear/base/bull as distribution quantiles or mix their house weights into this first version. Resolve market inputs once and reuse the resulting `ScenarioInputs`, `BaseYear`, `Bridge`, and `run_scenario`; the simulation is an analysis layer and does not rewrite `assumptions.yaml`. [Repository: `engine.py`, `analysis.py`, AGENTS.md §18.10]

Use three editable triangular distributions, specified by **minimum, most likely, maximum**. Bounds are hard limits, not percentiles. Degenerate settings are allowed.

| Driver | Proposed transformation | Initial settings |
|---|---|---|
| Revenue growth | One additive shift, in percentage points, to the explicit growth path | 0 / 0 / 0 |
| Operating margin | One shift to the year-5 margin, phased in by `min(year, 5) / 5`, preserving the existing path's shape | 0 / 0 / 0 |
| Capital efficiency | One positive multiplier applied to both early and late sales-to-capital ratios | 1 / 1 / 1 |

The triangular family is a small, comprehensible **judgment model**, not an empirical fit. Initial settings deliberately express no uncertainty. Any nonzero ranges need an editable rationale/source field and an explicit user-assumption label. Do not infer calibrated widths from sensitivity nudges, scenario endpoints, five historical observations, or industry averages. No illustrative numerical preset is necessary.

For later company calibration, choose a relevant business regime, comparable definitions and observation window; examine forecast errors or comparable operating outcomes; explain how observations inform support, likely value, skew, and the chosen dependence. A cross-company margin distribution is not automatically a single company's future uncertainty. Do not choose parameters to obtain a preferred valuation. [D1, pp.23–25, 36–37; repository `uncertainty-and-bias.md`]

A triangular mode is not necessarily its mean: the mean is `(minimum + mode + maximum) / 3`. Thus an asymmetric distribution centered on a zero mode changes expected inputs. The deterministic case, simulation mean and median need not agree; the DCF is nonlinear even for mean-centered input shifts. Exact agreement is required only when all shocks are zero and the S/C multiplier is one.

### Persistence and dependencies

Draw once per driver per complete forecast, not independently each year. This expresses uncertainty about a persistent business outcome, not annual economic noise. The same S/C multiplier preserves the chosen relative early/late capital efficiency.

Offer clearly named dependency choices for margin and S/C relative to the growth draw:

- **Independent:** separate uniform ranks. Explicitly label this as an assumption, not an estimated zero correlation.
- **Same rank:** use the growth draw's uniform percentile in the linked triangular distribution.
- **Opposite rank:** use one minus that percentile.

Same/opposite rank links impose perfect positive/negative rank dependence between nondegenerate shocks; they are stress choices, not fitted Pearson correlation coefficients. Examples of economic mechanisms: stronger demand and utilization can raise both growth and margin; growth won by price cuts can lower margin; a larger capacity bill can require lower S/C. No direction is universally correct. If no relationship is defensible, vary only one material driver or explicitly use independent exploration. [D1, pp.25–26; D2, Step 5]

### Preserve economic relationships

1. For a five-entry growth path with the automatic ten-year fade, shift years 1–5 and rebuild years 6–10 through `faded_growth`. Year 10 must still reach the fixed terminal growth. For a fully explicit ten-entry growth path, preserve its shape and apply the disclosed shift to those ten entries; keep terminal growth fixed. Never substitute an automatic fade for an explicitly authored path.
2. Apply the margin ramp to each **existing resolved** margin. A five-entry growth path may coexist with a ten-entry margin path: MRVL bull does this, falling from 40% in year 5 to 36% in year 10. Rebuilding growth must not flatten this margin path. Terminal margin remains the final forecast margin, as the engine specifies. [Repository: MRVL assumptions, `scenario_inputs`, `fade_years`, `_terminal`]
3. Keep the selected reinvestment lag. Let `run_scenario` recalculate investment from the sampled revenue and S/C paths. Keep absolute reinvestment overrides unchanged and show which years they cover; the S/C multiplier has no effect in those years. GOOGL and MRVL both contain such overrides. The experiment therefore holds those commitments fixed while varying their eventual productivity. [Repository: company assumptions, `run_scenario`]
4. Hold risk-free rate, WACC path, taxes, terminal growth, terminal ROIC premium, cash/debt/shares and distress bridge fixed. Terminal ROIC remains terminal WACC plus premium; positive terminal growth still requires reinvestment at `g / ROIC`. Do not separately sample FCFF, reinvestment, implied ROIC or terminal value. [Repository: AGENTS.md §18.3; D4]
5. Existing transition warnings should remain visible or be counted across draws, not used to select favorable observations. Mechanical constraints alone cannot establish that a sampled outcome fits capacity, competitive dynamics or the written case narrative. [Repository: AGENTS.md §18.2 and `business-drivers.md`]

## Invalid draws and interpretation

Validate settings before running: finite ordered triangular bounds, positive S/C support, supported integer draw count/seed, valid dependency choices. Use a local seeded RNG. Do not mutate the starting inputs or global random state.

Validate each sampled path against the applicable existing schema bounds and engine conditions, including positive S/C, finite numbers, terminal WACC greater than terminal growth, and positive terminal ROIC. The current schema accepts growth from -99% to 500% and margin from -500% to 99%; these are software bounds, not economically calibrated ranges. Preserve any baseline-authorized terminal override and its warning. [Repository: `schema.py`, `_terminal`]

Attempt exactly the requested number of draws. Record draw index, sampled inputs and a specific failure reason for invalid outcomes. Never clip inputs, repeatedly resample to fill a success quota, or silently discard failures. If any fail, label summaries as **conditional on valid draws**, with attempted/valid/invalid counts next to them; avoid an unqualified probability headline. If all fail, show no distribution statistics. A known model error is an invalid draw; an unexpected programming error should not be disguised as modeling uncertainty.

Keep finite negative per-share outputs, flag them and explain that they are the existing FCFF bridge's residual, not a negative traded share price or a new default model. Do not silently floor equity at zero: that would change the engine and would need an explicit limited-liability/distress model.

On Results, show the conditional value-per-share histogram, deterministic reference and current price, mean, median, P10/P90, standard deviation, observed min/max, and share of valid draws whose value exceeds price. Use a documented empirical quantile convention and expose sampled results/settings for reconciliation. Call the interval an **assumption-based valuation range**, not a statistical confidence interval or future share-price forecast. More draws reduce simulation noise, not model uncertainty. The fixed distress adjustment is already in every draw; a price-threshold frequency is not a failure probability or probability of making money.

## Verification contract

- Zero shifts/unit S/C multiplier reproduces deterministic rows, terminal value and per-share value; same seed/settings/input snapshot yields identical draws and results.
- Inverse triangular sampling handles endpoint modes and degenerate bounds; generated values remain in support. Same/opposite links match the intended ranks.
- Test five-year, automatic ten-year fade, explicit ten-year paths, independently shaped ten-year margins, lag 0–3, overrides and nonzero distress bridge.
- Recompute lagged reinvestment and terminal `g / ROIC` from sampled paths. Verify the zero-premium terminal case separately; growth does not create an unexplained terminal excess-return benefit.
- Independently reconcile mean, standard deviation, quantiles, histogram counts and threshold counts to raw outputs. Verify partial failure, all-invalid and negative-value reporting.
- Exercise the app's current unsaved edits, case changes and seeded reruns. An old simulation must not appear to describe newly edited assumptions; tie the result to its input/settings snapshot. Confirm simulation never saves or recomputes company artifacts implicitly.

## Sources

- **D1:** Aswath Damodaran, [Probabilistic Approaches: Scenario Analysis, Decision Trees and Simulations](https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/probabilistic.pdf), undated chapter, 61 pages. PDF and printed pages coincide. Relevant locators: “Steps in simulation” pp.22–26; “Issues” pp.36–37; “Risk Adjusted Value and Simulations” pp.37–38. New source inspected through web text; no image claims used.
- **D2:** Aswath Damodaran, [DCF Myth 3.2: If you don't look, its not there!](https://aswathdamodaran.blogspot.com/2016/05/dcf-myth-32-if-you-don-look-its-not.html), 2016-05-23, “Simulation in Valuation,” Steps 1–6. New source inspected through web text; numerical illustrations are not app defaults.
- **D3:** Aswath Damodaran, [Dealing with uncertainty / CBuncert lecture](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/lectures/cbuncert.html), undated, “Monte Carlo Simulations,” Steps 1–5. New source inspected through web text; unrelated example cash-flow formulas were not used.
- **D4:** Aswath Damodaran, [Myth 5.3: Growth is good, more growth is better!](https://aswathdamodaran.blogspot.com/2016/11/myth-53-growth-is-good-more-growth-is.html), 2016-11-30; [existing cached text](sources/growth-and-value.txt). Also [cached terminal-value chapter](sources/terminal-value.txt), printed/PDF pp.10–12, “Project Returns” and “Reinvestment and Retention Ratios.”
- **Repository:** [AGENTS.md §18](../../../AGENTS.md#18-valuation-draft-valuation-compute-valuation); [playbook](../../../.claude/skills/draft-valuation/references/analyst-playbook.md); [business drivers](../../../.claude/skills/draft-valuation/references/business-drivers.md); [uncertainty and bias](../../../.claude/skills/draft-valuation/references/uncertainty-and-bias.md); [engine](../engine.py); [schema](../schema.py); [analysis](../analysis.py); [GOOGL assumptions](../../../companies/GOOGL/valuation/assumptions.yaml); [MRVL assumptions](../../../companies/MRVL/valuation/assumptions.yaml).
