"""The free-cash-flow-to-the-firm engine: AGENTS.md section 18.3, implemented literally.

Conventions where section 18 is silent follow Damodaran's ``fcffsimpleginzu.xlsx``
and are listed in the README:

* after-tax operating income is ``EBIT * (1 - tax)`` only when EBIT is positive;
  a loss carries no tax benefit (sheet row 7, no NOL);
* terminal reinvestment ``g / ROIC`` applies only when terminal growth is
  positive (sheet cell M8);
* implied ROIC divides the year's after-tax operating income by the invested
  capital at the start of that year (sheet row 40);
* the "10-year fade" structure for ``horizon: 10`` holds the start tax rate and
  the company cost of capital for years 1-5 and fades both linearly to their
  terminal values over years 6-10 (sheet rows 6 and 12).
"""

from __future__ import annotations

from dataclasses import dataclass, field, replace
from datetime import datetime, timezone
from typing import Any

from . import __version__
from .schema import (
    SCENARIO_NAMES, WEIGHTED_SCENARIOS, SchemaError, Validation, get_path, is_riskfree,
    terminal_growth_rule, validate,
)


class EngineError(Exception):
    """A scenario cannot be computed (for example terminal growth >= terminal cost of capital)."""


# --------------------------------------------------------------------------- #
# Inputs resolved from the YAML
# --------------------------------------------------------------------------- #

@dataclass
class MarketInputs:
    """What the engine needs from the market: price, risk-free rate, ERP, and their dates."""
    price: float
    risk_free_rate: float
    equity_risk_premium: float
    price_date: str | None = None
    risk_free_date: str | None = None
    erp_date: str | None = None
    price_source: str = "assumptions.yaml"
    risk_free_source: str = "assumptions.yaml"
    erp_source: str = "assumptions.yaml"
    warnings: list[str] = field(default_factory=list)


@dataclass
class BaseYear:
    revenue: float
    operating_income_gaap: float
    one_time_items: float
    amortization_memo: float
    amortization_addback: float
    stock_based_compensation_memo: float
    rnd_expense_memo: float
    rnd_adjustment: float
    rnd_asset: float
    rnd_amortization: float
    adjusted_operating_income: float
    margin: float
    effective_tax_rate: float
    invested_capital_reported: float | None
    invested_capital: float | None
    roic: float | None


@dataclass
class Bridge:
    cash: float
    debt: float
    leases: float
    minority_interests: float
    non_operating_assets: float
    other_claims: float
    probability_of_failure: float
    distress_proceeds: float
    diluted_shares: float


@dataclass
class CostOfCapital:
    method: str
    risk_free: float
    equity_risk_premium: float
    marginal_tax: float
    mature_market_erp: float
    wacc: float
    terminal_method: str
    terminal_wacc: float
    unlevered_beta: float | None = None
    debt_to_equity: float | None = None
    pretax_cost_of_debt: float | None = None
    levered_beta: float | None = None
    cost_of_equity: float | None = None
    after_tax_cost_of_debt: float | None = None
    weight_equity: float | None = None
    weight_debt: float | None = None
    industry: str | None = None
    unlevered_beta_note: str | None = None     # set when the beta came from the cached dataset
    debt_to_equity_note: str | None = None     # set when D/E was derived from the bridge and the price
    warnings: list[str] = field(default_factory=list)


@dataclass
class ScenarioInputs:
    """Everything one scenario run needs, already resolved to numbers."""
    name: str
    horizon: int
    growth: list[float]
    margin: list[float]
    sales_to_capital: float
    sales_to_capital_late: float
    reinvestment_override: list[float | None]
    tax_start: float
    tax_terminal: float
    wacc: float
    terminal_wacc: float
    terminal_growth: float
    roic_premium: float
    reinvestment_lag: int = 1
    weight: float | None = None
    terminal_growth_is_riskfree: bool = False   # the YAML said "riskfree"; the number is the run's rate


# --------------------------------------------------------------------------- #
# Outputs
# --------------------------------------------------------------------------- #

@dataclass
class YearRow:
    year: int
    revenue: float
    growth: float
    margin: float
    ebit: float
    tax_rate: float
    ebit_after_tax: float
    reinvestment: float
    reinvestment_source: str
    sales_to_capital: float
    fcff: float
    wacc: float
    discount_factor: float
    pv: float
    invested_capital_start: float | None
    invested_capital_end: float | None
    roic: float | None


@dataclass
class Terminal:
    growth: float
    revenue: float
    margin: float
    ebit: float
    tax_rate: float
    ebit_after_tax: float
    wacc: float
    roic: float
    reinvestment_rate: float
    reinvestment: float
    fcff: float
    value: float
    pv: float


@dataclass
class ScenarioResult:
    name: str
    inputs: ScenarioInputs
    rows: list[YearRow]
    terminal: Terminal
    sum_pv_fcff: float
    pv_terminal: float
    going_concern_value: float
    probability_of_failure: float
    distress_proceeds: float
    operating_assets: float
    equity: float
    per_share: float
    enterprise_value: float
    price: float
    upside: float
    terminal_share: float
    fade_reference: "ScenarioResult | None" = None
    warnings: list[str] = field(default_factory=list)


@dataclass
class WeightedResult:
    operating_assets: float
    enterprise_value: float
    equity: float
    per_share: float
    upside: float
    terminal_share: float
    fade_per_share: float
    weights: dict[str, float]


@dataclass
class ValuationResult:
    ticker: str
    company: str
    as_of_quarter: str
    as_of_date: str | None
    computed_at: str
    engine_version: str
    horizon: int
    market: MarketInputs
    base_year: BaseYear
    bridge: Bridge
    cost_of_capital: CostOfCapital
    scenarios: dict[str, ScenarioResult]
    weighted: WeightedResult | None
    stopped: dict[str, list[str]]
    skipped: dict[str, str]
    warnings: list[str]
    assumptions: dict[str, Any]
    analysis: Any = None          # filled by analysis.run_analysis (grids, reverse DCF, diagnostics)
    company_dir: str | None = None  # companies/<TICKER>, used to resolve source tags in valuation.md


# --------------------------------------------------------------------------- #
# Base year, bridge, cost of capital
# --------------------------------------------------------------------------- #

def _num(doc: Any, path: str, default: float = 0.0) -> float:
    x = get_path(doc, path)
    return default if x is None else float(x)


def _sum_items(doc: Any, path: str) -> float:
    items = get_path(doc, path) or []
    return sum(float(i.get("value") or 0.0) for i in items if isinstance(i, dict))


def rnd_capitalization(current: float, history: list[float], years: int) -> tuple[float, float, float]:
    """Damodaran's R&D converter.

    ``history`` is oldest first; the last ``years`` entries are years -years .. -1.
    Each past year's R&D is amortized straight-line over ``years``.  Returns
    ``(adjustment_to_operating_income, research_asset, amortization_this_year)``.
    """
    past = [float(x) for x in history[-years:]]          # oldest first
    amortization = sum(past) / years
    unamortized = 0.0
    for k, spend in enumerate(reversed(past), start=1):  # k = 1 is year -1
        unamortized += spend * (years - k) / years
    asset = current + unamortized
    return current - amortization, asset, amortization


def build_base_year(doc: dict[str, Any]) -> BaseYear:
    revenue = _num(doc, "base_year.revenue.value")
    ebit_gaap = _num(doc, "base_year.operating_income_gaap.value")
    one_time = _sum_items(doc, "base_year.one_time_items")
    amort_memo = _num(doc, "base_year.amortization_of_acquired_intangibles.value")
    sbc_memo = _num(doc, "base_year.stock_based_compensation.value")
    rnd_memo = _num(doc, "base_year.rnd_expense.value")
    switches = doc.get("switches") or {}
    addback = amort_memo if switches.get("addback_acquired_amortization") else 0.0
    rnd_adj = rnd_asset = rnd_amort = 0.0
    if switches.get("capitalize_rnd"):
        years = int(switches.get("rnd_amortization_years", 5))
        rnd_adj, rnd_asset, rnd_amort = rnd_capitalization(rnd_memo, switches.get("rnd_history") or [], years)
    adjusted = ebit_gaap + one_time + addback + rnd_adj
    ic_reported = get_path(doc, "base_year.invested_capital.value")
    ic = None if ic_reported is None else float(ic_reported) + rnd_asset
    tax = _num(doc, "base_year.effective_tax_rate.value")
    roic = None
    if ic:
        roic = after_tax(adjusted, tax) / ic
    return BaseYear(
        revenue=revenue, operating_income_gaap=ebit_gaap, one_time_items=one_time,
        amortization_memo=amort_memo, amortization_addback=addback,
        stock_based_compensation_memo=sbc_memo, rnd_expense_memo=rnd_memo,
        rnd_adjustment=rnd_adj, rnd_asset=rnd_asset, rnd_amortization=rnd_amort,
        adjusted_operating_income=adjusted, margin=adjusted / revenue if revenue else 0.0,
        effective_tax_rate=tax,
        invested_capital_reported=None if ic_reported is None else float(ic_reported),
        invested_capital=ic, roic=roic,
    )


def build_bridge(doc: dict[str, Any]) -> Bridge:
    return Bridge(
        cash=_num(doc, "bridge.cash_and_marketable_securities.value"),
        debt=_num(doc, "bridge.debt.value"),
        leases=_num(doc, "bridge.operating_lease_liabilities.value"),
        minority_interests=_num(doc, "bridge.minority_interests.value"),
        non_operating_assets=_sum_items(doc, "bridge.non_operating_assets"),
        other_claims=_sum_items(doc, "bridge.other_claims"),
        probability_of_failure=_num(doc, "bridge.probability_of_failure.value"),
        distress_proceeds=_num(doc, "bridge.distress_proceeds.value"),
        diluted_shares=_num(doc, "bridge.diluted_shares.value"),
    )


def _dataset_beta(industry: str) -> tuple[float, str]:
    """Unlevered beta corrected for cash from the cached Damodaran betas dataset."""
    from . import datasets
    found = datasets.lookup("betas", industry, "unlevered_beta_cash_corrected")
    if found.value is None:
        raise EngineError(f"cost_of_capital.build.unlevered_beta.value is null and industry {industry!r} "
                          "was not found in the cached Damodaran betas dataset")
    return found.value, (f"Damodaran betas.xls dated {found.dataset_date}, industry '{found.matched_name}', "
                         f"column '{found.column}'")


def build_cost_of_capital(doc: dict[str, Any], market: MarketInputs) -> CostOfCapital:
    coc = doc["cost_of_capital"]
    rf = market.risk_free_rate
    erp = market.equity_risk_premium
    mt = _num(doc, "market.marginal_tax_rate", 0.25)
    mature = _num(doc, "market.mature_market_erp", 0.045)
    result = CostOfCapital(
        method=coc["method"], risk_free=rf, equity_risk_premium=erp, marginal_tax=mt,
        mature_market_erp=mature, wacc=0.0, terminal_method="mature", terminal_wacc=0.0,
        industry=get_path(doc, "cost_of_capital.build.damodaran_industry.value"),
    )
    if coc["method"] == "pinned":
        result.wacc = float(coc["pinned_value"])
    else:
        ub_cell = get_path(doc, "cost_of_capital.build.unlevered_beta.value")
        if ub_cell is None:
            ub, result.unlevered_beta_note = _dataset_beta(str(result.industry or ""))
            result.warnings.append(f"cost_of_capital.build.unlevered_beta.value is null; using {ub:.3f} from "
                                   f"{result.unlevered_beta_note}")
        else:
            ub = float(ub_cell)
        de_cell = get_path(doc, "cost_of_capital.build.debt_to_equity_market.value")
        if de_cell is None:
            bridge = build_bridge(doc)
            market_cap = market.price * bridge.diluted_shares
            de = (bridge.debt + bridge.leases) / market_cap if market_cap else 0.0
            result.debt_to_equity_note = (f"(debt {bridge.debt:,.0f} + leases {bridge.leases:,.0f}) / "
                                          f"(price {market.price:,.2f} x {bridge.diluted_shares:,.1f} shares)")
            result.warnings.append(f"cost_of_capital.build.debt_to_equity_market.value is null; derived {de:.4f} "
                                   f"as {result.debt_to_equity_note}")
        else:
            de = float(de_cell)
        kd = _num(doc, "cost_of_capital.build.pretax_cost_of_debt.value")
        levered = ub * (1.0 + (1.0 - mt) * de)
        coe = rf + levered * erp
        we = 1.0 / (1.0 + de)
        wd = de / (1.0 + de)
        result.unlevered_beta, result.debt_to_equity, result.pretax_cost_of_debt = ub, de, kd
        result.levered_beta, result.cost_of_equity = levered, coe
        result.after_tax_cost_of_debt = kd * (1.0 - mt)
        result.weight_equity, result.weight_debt = we, wd
        result.wacc = we * coe + wd * kd * (1.0 - mt)
    term = coc.get("terminal") or {}
    method = term.get("method", "mature")
    result.terminal_method = method
    if method == "mature":
        result.terminal_wacc = rf + mature
    elif method == "hold":
        result.terminal_wacc = result.wacc
    else:
        result.terminal_wacc = float(term["value"])
    return result


def scenario_inputs(doc: dict[str, Any], name: str, coc: CostOfCapital) -> ScenarioInputs:
    s = doc["scenarios"][name]
    horizon = int(doc.get("horizon", 5))
    override = (s.get("reinvestment_override") or {}).get("values") or [None] * horizon
    pinned = s.get("cost_of_capital_override")
    wacc = coc.wacc if pinned is None else float(pinned)
    terminal_wacc = wacc if coc.terminal_method == "hold" else coc.terminal_wacc
    lag = int((doc.get("switches") or {}).get("reinvestment_lag", 1))
    raw_growth = s["terminal"]["growth"]["value"]
    riskfree = is_riskfree(raw_growth)
    return ScenarioInputs(
        name=name, horizon=horizon,
        growth=[float(x) for x in s["revenue_growth"]["values"]],
        margin=[float(x) for x in s["operating_margin"]["values"]],
        sales_to_capital=float(s["sales_to_capital"]["value"]),
        sales_to_capital_late=float(s["sales_to_capital"]["value_late"]),
        reinvestment_override=[None if x is None else float(x) for x in override],
        tax_start=float(s["tax_rate"]["start"]),
        tax_terminal=float(s["tax_rate"]["terminal"]),
        wacc=wacc, terminal_wacc=terminal_wacc,
        terminal_growth=coc.risk_free if riskfree else float(raw_growth),
        roic_premium=float(s["terminal"]["roic_premium"]["value"]),
        reinvestment_lag=lag,
        weight=None if s.get("weight") is None else float(s["weight"]),
        terminal_growth_is_riskfree=riskfree,
    )


# --------------------------------------------------------------------------- #
# Paths and the scenario run
# --------------------------------------------------------------------------- #

def _fade(start: float, end: float, horizon: int) -> list[float]:
    """Years 1-5 at ``start``; years 6-10 move linearly to ``end`` (Damodaran rows 6 and 12)."""
    if horizon == 5:
        return [start] * 5
    return [start] * 5 + [start + (end - start) * k / 5 for k in range(1, 6)]


def tax_path(inp: ScenarioInputs) -> list[float]:
    return _fade(inp.tax_start, inp.tax_terminal, inp.horizon)


def wacc_path(inp: ScenarioInputs) -> list[float]:
    return _fade(inp.wacc, inp.terminal_wacc, inp.horizon)


def sales_to_capital_path(inp: ScenarioInputs) -> list[float]:
    if inp.horizon == 5:
        return [inp.sales_to_capital] * 5
    return [inp.sales_to_capital] * 5 + [inp.sales_to_capital_late] * 5


def after_tax(ebit: float, tax: float) -> float:
    """Operating income after tax; a loss carries no tax benefit (ginzu row 7)."""
    return ebit * (1.0 - tax) if ebit > 0 else ebit


def fade_inputs(inp: ScenarioInputs) -> ScenarioInputs:
    """The 10-year-fade reference of section 18.2 built from the first five explicit years."""
    g5, gt = inp.growth[4], inp.terminal_growth
    growth = inp.growth[:5] + [g5 - (g5 - gt) * k / 5 for k in range(1, 6)]
    margin = inp.margin[:5] + [inp.margin[4]] * 5
    override = list(inp.reinvestment_override[:5]) + [None] * 5
    return replace(inp, name=f"{inp.name} (10-year fade)", horizon=10, growth=growth,
                   margin=margin, reinvestment_override=override)


def run_scenario(inp: ScenarioInputs, base: BaseYear, bridge: Bridge, price: float) -> ScenarioResult:
    """Section 18.3, year by year, then terminal, failure adjustment, bridge, per share."""
    T = inp.horizon
    if len(inp.growth) != T or len(inp.margin) != T:
        raise EngineError(f"{inp.name}: growth and margin lists must have {T} entries")
    revenues = [base.revenue]
    for g in inp.growth:
        revenues.append(revenues[-1] * (1.0 + g))
    revenues.append(revenues[T] * (1.0 + inp.terminal_growth))      # Rev_{T+1}
    taxes, waccs, scs = tax_path(inp), wacc_path(inp), sales_to_capital_path(inp)
    rows: list[YearRow] = []
    df = 1.0
    ic = base.invested_capital
    for t in range(1, T + 1):
        ebit = revenues[t] * inp.margin[t - 1]
        eat = after_tax(ebit, taxes[t - 1])
        override = inp.reinvestment_override[t - 1] if t - 1 < len(inp.reinvestment_override) else None
        if override is not None:
            reinvestment, source = override, "override"
        else:
            delta = revenues[t + 1] - revenues[t] if inp.reinvestment_lag == 1 else revenues[t] - revenues[t - 1]
            reinvestment, source = delta / scs[t - 1], "sales_to_capital"
        fcff = eat - reinvestment
        df *= 1.0 / (1.0 + waccs[t - 1])
        roic = eat / ic if ic else None
        ic_end = None if ic is None else ic + reinvestment
        rows.append(YearRow(
            year=t, revenue=revenues[t], growth=inp.growth[t - 1], margin=inp.margin[t - 1],
            ebit=ebit, tax_rate=taxes[t - 1], ebit_after_tax=eat, reinvestment=reinvestment,
            reinvestment_source=source, sales_to_capital=scs[t - 1], fcff=fcff, wacc=waccs[t - 1],
            discount_factor=df, pv=fcff * df, invested_capital_start=ic, invested_capital_end=ic_end,
            roic=roic,
        ))
        ic = ic_end
    terminal = _terminal(inp, revenues[T + 1], df)
    sum_pv = sum(r.pv for r in rows)
    going_concern = sum_pv + terminal.pv
    p_fail = bridge.probability_of_failure
    operating_assets = going_concern * (1.0 - p_fail) + bridge.distress_proceeds * p_fail
    equity = (operating_assets + bridge.cash + bridge.non_operating_assets
              - bridge.debt - bridge.leases - bridge.minority_interests - bridge.other_claims)
    per_share = equity / bridge.diluted_shares
    ev = (price * bridge.diluted_shares + bridge.debt + bridge.leases + bridge.minority_interests
          + bridge.other_claims - bridge.cash - bridge.non_operating_assets)
    return ScenarioResult(
        name=inp.name, inputs=inp, rows=rows, terminal=terminal, sum_pv_fcff=sum_pv,
        pv_terminal=terminal.pv, going_concern_value=going_concern, probability_of_failure=p_fail,
        distress_proceeds=bridge.distress_proceeds, operating_assets=operating_assets, equity=equity,
        per_share=per_share, enterprise_value=ev, price=price,
        upside=per_share / price - 1.0 if price else 0.0,
        terminal_share=terminal.pv / going_concern if going_concern else 0.0,
    )


def _terminal(inp: ScenarioInputs, revenue_next: float, df_T: float) -> Terminal:
    g = inp.terminal_growth
    margin = inp.margin[-1]
    ebit = revenue_next * margin
    eat = ebit * (1.0 - inp.tax_terminal)
    roic = inp.terminal_wacc + inp.roic_premium
    if roic <= 0:
        raise EngineError(f"{inp.name}: terminal ROIC {roic:.4f} must be positive")
    if inp.terminal_wacc <= g:
        raise EngineError(f"{inp.name}: terminal cost of capital {inp.terminal_wacc:.4f} must exceed "
                          f"terminal growth {g:.4f}")
    rate = g / roic if g > 0 else 0.0
    reinvestment = eat * rate
    fcff = eat - reinvestment
    value = fcff / (inp.terminal_wacc - g)
    return Terminal(growth=g, revenue=revenue_next, margin=margin, ebit=ebit, tax_rate=inp.tax_terminal,
                    ebit_after_tax=eat, wacc=inp.terminal_wacc, roic=roic, reinvestment_rate=rate,
                    reinvestment=reinvestment, fcff=fcff, value=value, pv=value * df_T)


# --------------------------------------------------------------------------- #
# The whole document
# --------------------------------------------------------------------------- #

def _terminal_growth_check(doc: dict[str, Any], name: str, inp: ScenarioInputs,
                           rf: float) -> tuple[str | None, str | None]:
    """Rule 5 against the run's risk-free rate.  Returns (stop, warning); "riskfree" never trips it."""
    if inp.terminal_growth_is_riskfree:
        return None, None
    node = get_path(doc, f"scenarios.{name}.terminal.growth") or {}
    return terminal_growth_rule(name, inp.terminal_growth, rf, node if isinstance(node, dict) else {})


def _weighted(results: dict[str, ScenarioResult]) -> WeightedResult | None:
    if any(n not in results for n in WEIGHTED_SCENARIOS):
        return None
    weights = {n: results[n].inputs.weight or 0.0 for n in WEIGHTED_SCENARIOS}

    def w(attr: str) -> float:
        return sum(weights[n] * getattr(results[n], attr) for n in WEIGHTED_SCENARIOS)

    pv_tv = sum(weights[n] * results[n].pv_terminal for n in WEIGHTED_SCENARIOS)
    gc = sum(weights[n] * results[n].going_concern_value for n in WEIGHTED_SCENARIOS)
    per_share = w("per_share")
    price = results["base"].price
    fade = sum(weights[n] * results[n].fade_reference.per_share for n in WEIGHTED_SCENARIOS
               if results[n].fade_reference is not None)
    return WeightedResult(
        operating_assets=w("operating_assets"), enterprise_value=results["base"].enterprise_value,
        equity=w("equity"), per_share=per_share, upside=per_share / price - 1.0 if price else 0.0,
        terminal_share=pv_tv / gc if gc else 0.0, fade_per_share=fade, weights=weights,
    )


def compute(doc: dict[str, Any], market: MarketInputs, validation: Validation | None = None) -> ValuationResult:
    """Compute every scenario.  ``market`` must already be resolved (see market.resolve)."""
    val = validation or validate(doc)
    if val.errors:
        raise SchemaError("\n".join(val.errors))
    base = build_base_year(doc)
    bridge = build_bridge(doc)
    coc = build_cost_of_capital(doc, market)
    # The validator's generic "is null; the engine takes/derives" notes are superseded by the
    # engine's lines that carry the actual numbers.
    generic = [w for w in val.warnings if coc.warnings and "is null; the engine" in w]
    warnings = [w for w in val.warnings if w not in generic] + list(market.warnings) + list(coc.warnings)
    results: dict[str, ScenarioResult] = {}
    stopped: dict[str, list[str]] = {}
    skipped = dict(val.skipped)
    for name in SCENARIO_NAMES:
        if name not in (doc.get("scenarios") or {}) or name in skipped:
            continue
        reasons = list(val.shared_nulls) + list(val.stopped.get(name, []))
        if reasons:
            stopped[name] = reasons
            continue
        inp = scenario_inputs(doc, name, coc)
        stop, warn = _terminal_growth_check(doc, name, inp, market.risk_free_rate)
        if stop:
            stopped[name] = [stop]
            continue
        try:
            res = run_scenario(inp, base, bridge, market.price)
            res.fade_reference = run_scenario(fade_inputs(inp), base, bridge, market.price)
        except EngineError as exc:
            stopped[name] = [str(exc)]
            continue
        if warn:
            res.warnings.append(warn)
            warnings.append(warn)
        results[name] = res
    for name, reasons in stopped.items():
        warnings.append(f"{name} scenario not computed: " + "; ".join(reasons))
    for name, reason in skipped.items():
        warnings.append(f"{name} scenario skipped: {reason}")
    if not results:
        raise EngineError("no scenario could be computed: " + "; ".join(
            f"{n}: {'; '.join(r)}" for n, r in stopped.items()) if stopped else "no scenarios")
    return ValuationResult(
        ticker=str(doc.get("ticker")), company=str(doc.get("company")),
        as_of_quarter=str(doc.get("as_of_quarter")), as_of_date=_text(doc.get("as_of_date")),
        computed_at=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        engine_version=__version__, horizon=int(doc.get("horizon", 5)), market=market, base_year=base,
        bridge=bridge, cost_of_capital=coc, scenarios=results, weighted=_weighted(results),
        stopped=stopped, skipped=skipped, warnings=list(dict.fromkeys(warnings)), assumptions=doc,
    )


def _text(x: Any) -> str | None:
    return None if x is None else str(x)
