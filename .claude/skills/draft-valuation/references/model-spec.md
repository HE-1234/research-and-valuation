# Valuation model requirements

Read for model selection, valuation drafting, or engine changes. Compute runs need §18.8 for market-data fallbacks; they do not redraft inputs. [Assumptions](assumptions-spec.md), [workflow contracts](workflow-contracts.md), and [output requirements](valuation-output.md) are separate. Section numbers are retained for existing citations.

<a id="section-18"></a>

## 18. Valuation (`draft-valuation`, `compute-valuation`)

Valuation is a separate layer on top of the research library. It never edits `business.md`, `outlook.md`, or `scorecard.md`. It reads them, plus cached filings and targeted valuation evidence under [§18.4](assumptions-spec.md#section-18-4) rule 16, and produces one editable file of assumptions and one rendered document of results. The owner's judgment lives in the assumptions file; the engine only does arithmetic.

<a id="section-18-1"></a>

## 18.1 Method in one paragraph

We follow Aswath Damodaran's free-cash-flow-to-the-firm model as implemented in his public `fcffsimpleginzu.xlsx`. Operating profit after tax, minus the reinvestment needed to grow, gives the cash the whole firm produces each year. Those cash flows are discounted at the firm's cost of capital (the blended return lenders and owners require). A terminal value captures everything after the forecast, under strict rules: growth capped at the risk-free rate, and a mature return on capital supported by the advantage retained in each outcome. A zero excess-return input means no lasting moat; it is allowed in any case and is not imposed on bear. Cash and non-operating assets are added, debt and other claims subtracted, and the result divided by diluted shares. Everything stays firm-side until that last step ([§18.6](#section-18-6)).

Reader rules from [research-guide §3](../../../../docs/research.md#section-3) apply to every prose sentence in `valuation.md`: the scenario stories are written for the 16-year-old, numbers live in tables, and the glossary holds only unavoidable terms (cost of capital, terminal value, reinvestment, enterprise value, and the like), one sentence each.

<a id="section-18-2"></a>

## 18.2 Horizon and structure

- **Default horizon: 10 years, built as five explicit years plus a five-year fade by rule.** This is the structure of Damodaran's own `fcffsimpleginzu.xlsx` and of both workbooks our tests reproduce (Alphabet 2018, Nvidia 2023). The analyst judges years 1–5 (`values` lists of five). The engine builds years 6–10: revenue growth moves linearly from year-5 growth to terminal growth; the operating margin holds at the year-5 level; sales-to-capital uses `value_late`; tax rate and cost of capital move linearly to their terminal values; reinvestment overrides may carry ten entries, otherwise years 6–10 use the ratio; terminal value at year 10. An analyst with a sourced reason to shape years 6–10 differently writes ten-entry lists; the app and `assumptions.md` then show all ten. Every draft must explicitly assess whether year-five conditions are temporary and whether the default fade and flat margin fit the expected investment payoff. If they do not, use ten-entry paths; this requirement does not silently change existing saved inputs or the engine's interpolation.
- **Why the default changed (2026-09-08).** The first version defaulted to five explicit years then terminal value, on the argument that the shorter structure was less likely to overvalue a fast grower. For a company investing far ahead of its revenue (Alphabet in 2026 spends about 45% of revenue on capital equipment) the short structure is not conservative but inconsistent: it charges the whole investment in years 1–2, stops crediting the growth it buys at year 5, and moves growth, return on capital and tax from their year-5 values to their stable values in one step. In the GOOGL draft the terminal-year free cash flow came out 29% below year 5's. Damodaran's rule: the move to stable growth is gradual for firms far from stable, and firms with high growth and strong competitive advantages get the longer growth period. "Choose the structure less likely to overvalue" never meant "choose the lower number"; a structure that contradicts its own inputs is wrong in both directions. See [§17](../../../../docs/history/2026-09-18-lessons.md#section-17).
- **The 5-year-stop reference value is always computed and shown** next to each case (same inputs, terminal value at year 5, terminal settings applied in year 6), so the owner still sees what the shorter structure would give. `horizon: 5` remains allowed for a company already close to stable growth; its reference row then shows the 10-year fade.
- **Transition check.** For every case the engine reports the change in free cash flow from the final explicit year to the terminal year, and terminal return on capital against the final year's implied return. It flags a cash-flow drop greater than 15% or terminal ROIC below half the final-year implied ROIC (including bear; no scenario is exempt by its label). These are house diagnostic thresholds, not Damodaran rules or economic bounds. A flag requires a documented explanation: inspect growth, margin, taxes, reinvestment, capital measurement and the transition together. Revise inputs only for economic reasons; never raise terminal ROIC or tune sales-to-capital merely to clear the warning. A supported economic discontinuity may remain with a reviewer explanation and visible warning; unresolved inconsistency cannot pass. Absence of a flag is not evidence that the terminal assumptions are sound. See [assumptions rule 5](assumptions-spec.md#section-18-4) and the sourced notes under `tools/valuation/damodaran-notes/`.
- End-of-year discounting, as in his sheet.

<a id="section-18-3"></a>

## 18.3 Formulas (the engine implements exactly these; tests reproduce his workbooks)

All money in USD millions. `T` = horizon. For year `t = 1..T`:

```
Rev_t      = Rev_{t-1} × (1 + g_t)                       Rev_0 = base-year TTM revenue
EBIT_t     = Rev_t × m_t                                  m_t = operating margin path
Tax_t      = effective rate (years 1..T in the 5-year model; see §18.2 for the fade)
Reinv_t    = (Rev_{t+L} − Rev_{t+L−1}) / SC   (L = switches.reinvestment_lag, default 1: money spent in t buys growth in t+1; revenue beyond the horizon grows at the terminal rate)
             where Rev_{T+1} = Rev_T × (1 + g_T), and an explicit per-year override replaces the S/C figure when given
FCFF_t     = EBIT_t × (1 − Tax_t) − Reinv_t
DF_t       = Π_{k=1..t} 1 / (1 + WACC_k)                  (cumulative, so a fading rate is handled)

Terminal (year T+1, growing at g_T forever):
EBIT_{T+1}  = Rev_T × (1 + g_T) × m_T
ROIC_T      = WACC_T + premium                            premium defaults to 0
FCFF_{T+1}  = EBIT_{T+1} × (1 − Tax_T) × (1 − g_T / ROIC_T)     (reinvestment = g / ROIC)
TV          = FCFF_{T+1} / (WACC_T − g_T)
PV(TV)      = TV × DF_T

Operating assets  = Σ FCFF_t × DF_t + PV(TV)
                    × (1 − p_fail) + distress_proceeds × p_fail        (p_fail defaults to 0)
Equity            = Operating assets + cash & marketable securities + non-operating assets
                    − debt − operating-lease liabilities − minority interests − other claims
Per share         = Equity / diluted shares
Enterprise value  = price × diluted shares + debt + leases + minorities + other claims
                    − cash − non-operating assets            (the like-for-like comparison to Operating assets)
```

Cost of capital build (when `method: build`):

```
levered beta   = unlevered beta × (1 + (1 − marginal tax) × D/E)
cost of equity = risk-free + levered beta × equity risk premium
WACC           = E/(D+E) × cost of equity + D/(D+E) × pre-tax cost of debt × (1 − marginal tax)
terminal WACC  = risk-free + mature-market ERP   (method `mature`, default)
               | the company's own WACC          (method `hold`)
               | a given number                   (method `value`)
```

Return on invested capital is after-tax EBIT divided by invested capital (book equity + debt + leases − cash), tracked each year by rolling invested capital forward with reinvestment; it is printed as a check, never used as an input.

<a id="section-18-6"></a>

## 18.6 Firm-side consistency

Cash flows are to the firm (before interest), discounted at the cost of capital, never at the cost of equity. Cash and marketable securities are excluded from the cash flows and added in the bridge; Damodaran's reason is that cash earns the riskless rate and discounting it at an operating cost of capital misvalues it. Debt is excluded from the cash flows and subtracted in the bridge; the interest tax shield sits in the after-tax cost of debt, not in the cash flows. The like-for-like market comparison is operating assets against enterprise value; the reverse DCF solves on enterprise value. Return on capital, never return on equity.

<a id="section-18-8"></a>

## 18.8 Market data and Damodaran datasets

- Risk-free rate: FRED series DGS10, `https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10`, latest non-empty row.
- Price: Yahoo chart endpoint `https://query1.finance.yahoo.com/v8/finance/chart/<TICKER>?range=1d&interval=1d` with a browser User-Agent; `regularMarketPrice` and its timestamp.
- Damodaran datasets, cached as CSV under `tools/valuation/data/damodaran/` with a `MANIFEST.md` (URL, fetch date, his "last updated" date), refreshed only by `uv run value --refresh-data`: `pc/implprem/ERPbymonth.xlsx` (implied ERP), `pc/datasets/betas.xls` (industry unlevered betas), `wacc.xls`, `capex.xls` (sales-to-capital), `margin.xls`, `taxrate.xls`, `histgr.xls` (historical revenue growth by industry), all under `https://pages.stern.nyu.edu/~adamodar/`.
- Honor manual inputs and user-supplied `--set` overrides. Automatic fetches use the market module's bounded retries; FRED failure falls back to the cached Damodaran T-bond rate with its date and a warning. If no documented fallback is usable, stop the dependent computation with a clear message and request only the missing input or decision. Do not invent a price or silently substitute another date or source. Fetched values and dates appear in `valuation.md`; the engine never writes into `assumptions.yaml`.

<a id="section-18-9"></a>

## 18.9 Engine

- uv project at the repo root; package `tools/valuation/` (module name `valuation`); Python ≥ 3.12; core dependencies limited to PyYAML, openpyxl, xlrd, and ruamel.yaml; pytest for tests and optional Streamlit for the app. `.venv/` is gitignored. `pyproject.toml` and `uv.lock` define installable versions.
- Console script `value`: `uv run value <TICKER-or-YAML-path> [--validate] [--dry-run] [--diagnostics-only] [--set a.b.c=1.2 ...] [--json] [--refresh-data]`. `--set` takes dotted paths into the YAML (`scenarios.base.sales_to_capital.value=2.0`, `scenarios.base.operating_margin.values.4=0.34`) and applies them in memory only, including during validation. `--diagnostics-only` always prints restricted JSON and writes nothing; it rejects combinations with validation, data refresh, or assumption rendering.
- Python API: `valuation.load(ticker)`, `valuation.compute(assumptions, market=None)`, `valuation.render(result)`.
- Tests: the engine in 10-year mode must reproduce Damodaran's `AlphabetApr2018.xlsx` and `NVIDIA2023.xlsx` values of operating assets and per-share values to within 0.1% from their input sheets; a hand-worked 5-year case; the five-plus-fade rule of [§18.2](#section-18-2) reproducing the ginzu's years 6–10 from five explicit inputs; the reference structure in both directions; the transition check; every validation rule; the reverse DCF round-trips.
- `uv run value <TICKER> --render-assumptions` writes `assumptions.md` only (no market fetch, no compute): the stories, then every input as tables with value, reason, and source, in the [§18.4](assumptions-spec.md#section-18-4) order. The same renderer runs on every app save and every compute.
- Creating or editing YAML goes through the writer built on `ruamel.yaml` round-trip mode so comments and key order survive. Archival copies and promotion of a reviewed candidate preserve bytes; promotion checks for intervening owner edits first. The engine's read path may stay on PyYAML.

<a id="section-18-11"></a>

## 18.11 Teaching references and economic suitability

The four skill entrypoints sequence work; `draft-valuation/references/analyst-playbook.md` routes detailed guidance. `tools/valuation/damodaran-notes/README.md` indexes cached primary texts, manifests and historical examples. Binding requirements stay here; topical references explain how to apply them and hold the reviewer checklist and forecast-record format. Read the playbook before a draft and use its model-selection, accounting, business-driver and uncertainty references at the corresponding steps. Read the learning reference on initial snapshot creation, on redraft and on refresh with forecast records. The reviewer reads the applicable guides and original source passages for material methodological claims. Record reference → decision → affected cell/evidence in the evidence note and review; a link list alone is insufficient.

Before numerical drafting, the evidence note establishes whether this engine represents the business: life-cycle/cycle position, FCFF suitability, material accounting adjustments, currency and risk consistency, and supported treatment of failure/financing/equity claims. A financial-sector label alone neither establishes nor rules out model fit. If a material required method or adjustment is unsupported, complete unaffected research and report the dependent valuation limitation; never force it through unrelated fields or implicitly build a new engine. An uncertain but supported forecast range is not missing evidence merely because no source predicts its precise value.

Methodological teachings are distinct from house conventions and old numerical examples. Do not treat dated cost-of-capital bands, historical forecast inputs, default scenario weights or warning thresholds as universal economic laws. Select economically coherent assumptions before testing diagnostics, and preserve price-independent operating judgments.
