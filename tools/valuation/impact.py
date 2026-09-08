"""Which factor moves the value most (AGENTS.md section 18.10, the Start page ranking).

For one scenario (the base case by default) every factor gets one plausible nudge and the
change in value per share is recorded.  The app shows the list on its Start page and walks
the owner through the factor pages in this order (revenue growth and operating margin are
always pages 3 and 4 regardless).  Nothing here touches the YAML; every nudge is applied to
a copy of the resolved :class:`~valuation.engine.ScenarioInputs`.

The nudges:

* revenue growth: +1 point in every forecast year;
* operating margin: +1 point in every forecast year;
* reinvestment: sales-to-capital +10% of its value (both the early and the late ratio), and
  every given per-year override +10%;
* cost of capital: +0.5 point on the company's rate (the terminal rate follows only when the
  terminal method is ``hold``);
* terminal value: terminal growth +0.25 point, capped at the risk-free rate; when the growth
  is already at the cap the nudge is -0.25 point;
* terminal return on capital: premium +1 point;
* taxes: start rate +1 point.

Weights are excluded: they change no case's value.
"""

from __future__ import annotations

from dataclasses import dataclass, replace

from .engine import (
    EngineError, MarketInputs, ScenarioInputs, build_base_year, build_bridge, build_cost_of_capital,
    run_scenario, scenario_inputs,
)
from .schema import SchemaError, validate

# page id -> label shown in the app; the order here is the fallback when the ranking is unavailable
FACTOR_LABELS = {
    "revenue_growth": "Revenue growth",
    "operating_margin": "Operating margin",
    "reinvestment": "Reinvestment",
    "cost_of_capital": "Cost of capital",
    "terminal": "Terminal value",
    "taxes_weights": "Taxes and weights",
}
FIXED_FIRST = ("revenue_growth", "operating_margin")


@dataclass
class Impact:
    factor: str                 # page id, a key of FACTOR_LABELS
    label: str                  # "Revenue growth"
    nudge: str                  # the nudge in words
    base_per_share: float       # value per share before the nudge
    nudged_per_share: float | None
    change: float | None        # nudged - base; None when the nudged case could not be computed
    note: str | None = None     # the engine's message when the nudge stops the case


def _nudges(inp: ScenarioInputs, risk_free: float) -> list[tuple[str, str, ScenarioInputs]]:
    out: list[tuple[str, str, ScenarioInputs]] = []
    out.append(("revenue_growth", "+1 point of growth in every forecast year",
                replace(inp, growth=[g + 0.01 for g in inp.growth])))
    out.append(("operating_margin", "+1 point of margin in every forecast year",
                replace(inp, margin=[m + 0.01 for m in inp.margin])))
    overrides = [None if x is None else x * 1.10 for x in inp.reinvestment_override]
    has_override = any(x is not None for x in inp.reinvestment_override)
    words = "sales-to-capital +10% of its value" + ("; per-year reinvestment overrides +10%" if has_override else "")
    out.append(("reinvestment", words,
                replace(inp, sales_to_capital=inp.sales_to_capital * 1.10,
                        sales_to_capital_late=inp.sales_to_capital_late * 1.10, reinvestment_override=overrides)))
    hold = abs(inp.terminal_wacc - inp.wacc) < 1e-12
    out.append(("cost_of_capital", "+0.5 point on the cost of capital" + (" (terminal rate follows)" if hold else ""),
                replace(inp, wacc=inp.wacc + 0.005,
                        terminal_wacc=inp.terminal_wacc + 0.005 if hold else inp.terminal_wacc)))
    if inp.terminal_growth + 0.0025 <= risk_free + 1e-12:
        out.append(("terminal", "terminal growth +0.25 point", replace(inp, terminal_growth=inp.terminal_growth + 0.0025)))
    else:
        out.append(("terminal", "terminal growth -0.25 point (already at the risk-free cap)",
                    replace(inp, terminal_growth=inp.terminal_growth - 0.0025)))
    out.append(("terminal_roic", "terminal return-on-capital premium +1 point",
                replace(inp, roic_premium=inp.roic_premium + 0.01)))
    out.append(("taxes_weights", "tax rate in the forecast years +1 point (weights change no case's value)",
                replace(inp, tax_start=inp.tax_start + 0.01)))
    return out


def impact_ranking(doc: dict, market: MarketInputs, scenario: str = "base") -> list[Impact]:
    """One :class:`Impact` per nudge, sorted by absolute change in value per share, largest first.

    Raises :class:`~valuation.schema.SchemaError` when the document does not validate and
    :class:`~valuation.engine.EngineError` when the scenario itself cannot be computed.
    """
    doc = {k: v for k, v in doc.items() if k != "_path"}
    val = validate(doc)
    if val.errors:
        raise SchemaError("\n".join(val.errors))
    reasons = list(val.shared_nulls) + list(val.stopped.get(scenario, []))
    if scenario in val.skipped or scenario not in (doc.get("scenarios") or {}):
        raise EngineError(f"{scenario} scenario is not computed")
    if reasons:
        raise EngineError(f"{scenario} scenario cannot be computed: " + "; ".join(reasons))
    base = build_base_year(doc)
    bridge = build_bridge(doc)
    coc = build_cost_of_capital(doc, market)
    inp = scenario_inputs(doc, scenario, coc)
    before = run_scenario(inp, base, bridge, market.price).per_share
    out: list[Impact] = []
    for factor, words, nudged in _nudges(inp, market.risk_free_rate):
        label = FACTOR_LABELS.get(factor, "Terminal value" if factor == "terminal_roic" else factor)
        try:
            after = run_scenario(nudged, base, bridge, market.price).per_share
            out.append(Impact(factor, label, words, before, after, after - before))
        except EngineError as exc:
            out.append(Impact(factor, label, words, before, None, None, note=str(exc)))
    out.sort(key=lambda i: (-abs(i.change) if i.change is not None else 1.0, i.label))
    return out


def page_order(ranking: list[Impact] | None) -> list[str]:
    """Factor page ids in walk order: revenue growth, operating margin, then the rest by impact.

    The two terminal nudges (growth and return-on-capital premium) both belong to the
    Terminal value page; the page takes the larger of the two.
    """
    rest = [f for f in FACTOR_LABELS if f not in FIXED_FIRST]
    if not ranking:
        return list(FIXED_FIRST) + rest
    best: dict[str, float] = {}
    for imp in ranking:
        page = "terminal" if imp.factor == "terminal_roic" else imp.factor
        if page in FIXED_FIRST:
            continue
        size = abs(imp.change) if imp.change is not None else -1.0
        best[page] = max(best.get(page, -1.0), size)
    ordered = sorted(rest, key=lambda p: (-best.get(p, -1.0), rest.index(p)))
    return list(FIXED_FIRST) + ordered
