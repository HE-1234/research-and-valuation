"""Sensitivity grids, reverse DCF, and the diagnostics of AGENTS.md section 18.5 items 7-9.

Damodaran's six checks, plus the transition check of section 18.2: the terminal year's free cash
flow and return on capital against the last explicit year's.  A small notch downwards is normal,
because the terminal year reinvests ``g / ROIC`` whatever the last explicit year spent (his own
Alphabet Feb 2024 sheet drops 10.7%, Microsoft 21%), so the check only flags a fall of more than
:data:`TRANSITION_DROP` or a terminal return below half the last year's implied return.

Everything here re-runs :func:`engine.run_scenario` on modified :class:`ScenarioInputs`;
nothing touches the YAML.
"""

from __future__ import annotations

from dataclasses import dataclass, field, replace
from pathlib import Path
from typing import Any, Callable

from . import datasets
from .engine import (
    BaseYear, Bridge, EngineError, ScenarioInputs, ScenarioResult, ValuationResult, run_scenario,
)
from .schema import get_path

HISTORY_GAP = 0.05      # points of growth beyond which the "history is context" note is printed (rule 11)
TRANSITION_DROP = 0.15  # a terminal-year cash flow this far below the last explicit year's is a cliff
TRANSITION_ROIC = 0.5   # a terminal return below this share of the last year's implied return is a cliff
# The bear case gives up the moat by rule (section 18.4 rule 5: its terminal return on capital equals its
# terminal cost of capital), so its step into the terminal year is large by construction and is reported
# without being checked.
EXEMPT_FROM_TRANSITION = "bear"
BEAR_EXPECTED = " (expected: the bear's terminal return equals its cost of capital by rule)"
WACC_STEPS = (-0.02, -0.01, 0.0, 0.01, 0.02)
TERMINAL_GROWTH_STEPS = (-0.01, -0.005, 0.0, 0.005, 0.01)
GROWTH_STEPS = (-0.04, -0.02, 0.0, 0.02, 0.04)
MARGIN_STEPS = (-0.04, -0.02, 0.0, 0.02, 0.04)


@dataclass
class Grid:
    title: str
    row_label: str
    col_label: str
    row_values: list[float]
    col_values: list[float]
    cells: list[list[float | None]]
    base_row: int
    base_col: int
    note: str


@dataclass
class ReverseDCF:
    target_enterprise_value: float
    base_operating_assets: float
    base_average_growth: float
    base_year5_margin: float
    implied_growth: float | None
    implied_growth_note: str
    implied_year5_margin: float | None
    implied_margin_note: str


@dataclass
class Diagnostic:
    title: str
    rows: list[tuple[str, str]]
    flag: bool = False
    note: str | None = None


@dataclass
class Analysis:
    scenario: str
    grids: list[Grid]
    reverse: ReverseDCF | None
    diagnostics: list[Diagnostic]
    industry: datasets.IndustryFigures | None
    warnings: list[str] = field(default_factory=list)


# --------------------------------------------------------------------------- #
# Input shifts
# --------------------------------------------------------------------------- #

def shift_growth(inp: ScenarioInputs, delta: float) -> ScenarioInputs:
    """Move every forecast year's growth by ``delta`` (so the average moves by ``delta``)."""
    return replace(inp, growth=[g + delta for g in inp.growth])


def shift_margin(inp: ScenarioInputs, delta: float) -> ScenarioInputs:
    """Move the year-5 margin by ``delta``, ramping in over years 1-5 (Damodaran's target-margin lever)."""
    margin = [m + delta * min(t, 5) / 5 for t, m in enumerate(inp.margin, start=1)]
    return replace(inp, margin=margin)


def shift_wacc(inp: ScenarioInputs, delta: float) -> ScenarioInputs:
    """Parallel shift of the company and terminal cost of capital."""
    return replace(inp, wacc=inp.wacc + delta, terminal_wacc=inp.terminal_wacc + delta)


def constant_growth(inp: ScenarioInputs, g: float) -> ScenarioInputs:
    return replace(inp, growth=[g] * inp.horizon)


def average_growth(res: ScenarioResult, years: int = 5) -> float:
    """Compound annual growth over the first ``years`` explicit years."""
    rev0 = res.rows[0].revenue / (1.0 + res.rows[0].growth)
    n = min(years, len(res.rows))
    return (res.rows[n - 1].revenue / rev0) ** (1.0 / n) - 1.0


def year5_margin(inp: ScenarioInputs) -> float:
    return inp.margin[min(4, len(inp.margin) - 1)]


# --------------------------------------------------------------------------- #
# Sensitivity grids
# --------------------------------------------------------------------------- #

def _per_share(inp: ScenarioInputs, base: BaseYear, bridge: Bridge, price: float) -> float | None:
    try:
        return run_scenario(inp, base, bridge, price).per_share
    except EngineError:
        return None


def sensitivity_wacc_growth(inp: ScenarioInputs, base: BaseYear, bridge: Bridge, price: float) -> Grid:
    rows = [inp.wacc + d for d in WACC_STEPS]
    cols = [inp.terminal_growth + d for d in TERMINAL_GROWTH_STEPS]
    cells = [[_per_share(replace(shift_wacc(inp, dw), terminal_growth=inp.terminal_growth + dg), base, bridge, price)
              for dg in TERMINAL_GROWTH_STEPS] for dw in WACC_STEPS]
    return Grid(
        title="Cost of capital and terminal growth", row_label="Cost of capital",
        col_label="Terminal growth", row_values=rows, col_values=cols, cells=cells,
        base_row=WACC_STEPS.index(0.0), base_col=TERMINAL_GROWTH_STEPS.index(0.0),
        note="Each row moves the company's cost of capital and the terminal cost of capital together by the "
             "same amount. Each column moves terminal growth. Cells are value per share in USD.",
    )


def sensitivity_growth_margin(inp: ScenarioInputs, base: BaseYear, bridge: Bridge, price: float) -> Grid:
    probe = run_scenario(inp, base, bridge, price)
    avg = average_growth(probe)
    rows = [avg + d for d in GROWTH_STEPS]
    cols = [year5_margin(inp) + d for d in MARGIN_STEPS]
    cells = [[_per_share(shift_margin(shift_growth(inp, dg), dm), base, bridge, price) for dm in MARGIN_STEPS]
             for dg in GROWTH_STEPS]
    return Grid(
        title="Average five-year revenue growth and year-5 operating margin",
        row_label="Average revenue growth (years 1-5)", col_label="Year-5 operating margin",
        row_values=rows, col_values=cols, cells=cells,
        base_row=GROWTH_STEPS.index(0.0), base_col=MARGIN_STEPS.index(0.0),
        note="Each row moves every year's revenue growth by the same amount. Each column moves the year-5 "
             "margin, with earlier years moving proportionally (one fifth per year). Cells are value per "
             "share in USD.",
    )


# --------------------------------------------------------------------------- #
# Reverse DCF
# --------------------------------------------------------------------------- #

def _bisect(f: Callable[[float], float | None], lo: float, hi: float, *, tol: float = 1e-9,
            max_iter: int = 200) -> tuple[float | None, str]:
    """Find x in [lo, hi] with f(x) = 0 for an increasing f.  Returns (x, note)."""
    flo, fhi = f(lo), f(hi)
    if flo is None or fhi is None:
        return None, "the cash-flow model could not be evaluated at the search bounds"
    if flo > 0:
        return None, f"even at the lower bound ({lo * 100:.1f}%) the value stays above the target"
    if fhi < 0:
        return None, f"even at the upper bound ({hi * 100:.1f}%) the value stays below the target"
    for _ in range(max_iter):
        mid = (lo + hi) / 2.0
        fm = f(mid)
        if fm is None:
            return None, "the cash-flow model failed during the search"
        if abs(fm) < 1e-9 or (hi - lo) < tol:
            return mid, "converged"
        if fm < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0, "stopped at the iteration limit"


def _operating_assets(inp: ScenarioInputs, base: BaseYear, bridge: Bridge, price: float) -> float | None:
    try:
        return run_scenario(inp, base, bridge, price).operating_assets
    except EngineError:
        return None


def reverse_dcf(inp: ScenarioInputs, base: BaseYear, bridge: Bridge, price: float,
                target_ev: float | None = None) -> ReverseDCF:
    """Constant growth, and separately the year-5 margin, that make operating assets equal EV."""
    probe = run_scenario(inp, base, bridge, price)
    target = probe.enterprise_value if target_ev is None else target_ev

    def f_growth(g: float) -> float | None:
        oa = _operating_assets(constant_growth(inp, g), base, bridge, price)
        return None if oa is None else oa - target

    def f_margin(m5: float) -> float | None:
        oa = _operating_assets(shift_margin(inp, m5 - year5_margin(inp)), base, bridge, price)
        return None if oa is None else oa - target

    g, g_note = _bisect(f_growth, -0.9, 3.0)
    m, m_note = _bisect(f_margin, -0.95, 0.95)
    return ReverseDCF(
        target_enterprise_value=target, base_operating_assets=probe.operating_assets,
        base_average_growth=average_growth(probe), base_year5_margin=year5_margin(inp),
        implied_growth=g, implied_growth_note=g_note, implied_year5_margin=m, implied_margin_note=m_note,
    )


# --------------------------------------------------------------------------- #
# Diagnostics
# --------------------------------------------------------------------------- #

def _pct(x: float | None) -> str:
    return "n/a" if x is None else f"{x * 100:.1f}%"


def _dated(v: datasets.IndustryValue) -> str:
    if v.value is None and v.note:
        return f"{v.note} ({v.dataset} dataset {v.dataset_date or 'undated'}, industry '{v.matched_name}')"
    if v.value is None:
        return f"not found in {v.dataset} dataset ({v.dataset_date or 'undated'})"
    return f"{_pct(v.value)} ({v.dataset} dataset {v.dataset_date or 'undated'}, industry '{v.matched_name}')"


def _optional_cell(doc: dict[str, Any], path: str) -> float | None:
    x = get_path(doc, f"{path}.value")
    return None if x is None else float(x)


def diagnostics(result: ValuationResult, res: ScenarioResult,
                figures: datasets.IndustryFigures | None,
                warnings: list[str] | None = None) -> list[Diagnostic]:
    doc = result.assumptions
    out: list[Diagnostic] = []
    avg = average_growth(res)
    rows = [(f"{res.name} case, average annual growth years 1-5", _pct(avg))]
    if figures:
        rows.append(("Industry, revenue growth last 5 years", _dated(figures.revenue_cagr_5y)))
    own = _optional_cell(doc, "diagnostics.historical_revenue_cagr")
    rows.append(("Company's own five-year history", _pct(own) if own is not None
                 else "not recorded in the assumptions"))
    note = None
    if own is not None and abs(avg - own) > HISTORY_GAP:
        note = ("The company's own history is context, not an anchor: a business whose mix has changed does not "
                "grow at the rate its old mix produced.")
    out.append(Diagnostic("1. Revenue growth against the industry and the company's own history", rows, note=note))

    last = res.rows[-1]
    size = _optional_cell(doc, "diagnostics.final_year_market_size")
    rows = [(f"Revenue in year {last.year} (USD millions)", f"{last.revenue:,.0f}")]
    if size is None:
        rows.append(("Market size in year " + str(last.year), "not given"))
        flag = False
    else:
        rows.append((f"Market size in year {last.year} (USD millions)", f"{size:,.0f}"))
        rows.append(("Implied share of that market", _pct(last.revenue / size if size else None)))
        flag = last.revenue > size
    out.append(Diagnostic("2. Year-T revenue against the market it could address", rows, flag=flag,
                          note="Flagged when revenue exceeds the market size." if flag else None))

    m5 = year5_margin(res.inputs)
    rows = [(f"{res.name} case, year-5 operating margin", _pct(m5)),
            ("Base-year adjusted operating margin", _pct(result.base_year.margin))]
    if figures:
        rows.append(("Industry, pre-tax operating margin", _dated(figures.pretax_operating_margin)))
    own_m = _optional_cell(doc, "diagnostics.historical_operating_margin")
    rows.append(("Company's own five-year average margin", _pct(own_m) if own_m is not None
                 else "not recorded in the assumptions"))
    out.append(Diagnostic("3. Year-5 margin against the industry and the company's own history", rows))

    rows = []
    for r in res.rows:
        rows.append((f"Year {r.year}", f"ROIC {_pct(r.roic)} against cost of capital {_pct(r.wacc)}"))
    rows.append(("Terminal", f"ROIC {_pct(res.terminal.roic)} against terminal cost of capital "
                             f"{_pct(res.terminal.wacc)}"))
    note = None
    if result.base_year.invested_capital is None:
        note = "Base-year invested capital is null, so the yearly ROIC could not be computed."
    out.append(Diagnostic("4. Implied return on invested capital against the cost of capital", rows, note=note))

    rows = [(f"{name} case", _pct(sc.terminal_share)) for name, sc in result.scenarios.items()]
    out.append(Diagnostic("5. Share of operating assets that comes from the terminal value", rows))

    rows, flag = [], False
    for name, sc in result.scenarios.items():
        ratio = sc.per_share / sc.price if sc.price else None
        hit = ratio is not None and (ratio > 2.0 or ratio < 0.5)
        flag = flag or hit
        rows.append((f"{name} case", f"value per share is {ratio:.2f}x the price" + (" (flag)" if hit else "")
                     if ratio is not None else "no price"))
    out.append(Diagnostic("6. Value against price", rows, flag=flag,
                          note="Flagged when value per share is above 2x or below 0.5x the price." if flag else None))
    out.append(transition_check(result, warnings))
    return out


def transition_check(result: ValuationResult, warnings: list[str] | None = None) -> Diagnostic:
    """Section 18.2: the step from the last explicit year into the terminal year, case by case.

    Reports the terminal year's free cash flow and return on capital against the last explicit
    year's, and flags a cliff when the step is bigger than the normal notch.  A flagged case also
    gets a line in the run's warnings, because the reviewer must resolve it.

    The bear case is reported but never flagged: section 18.4 rule 5 fixes its terminal return on
    capital at its terminal cost of capital, so a large step is what the rule asks for, not a
    disagreement between the inputs.
    """
    rows: list[tuple[str, str]] = []
    flag = False
    last_year = 0
    for name, sc in result.scenarios.items():
        last, term = sc.rows[-1], sc.terminal
        change = fcff_change(last.fcff, term.fcff)
        checked = name != EXEMPT_FROM_TRANSITION
        hit = checked and transition_flag(last.fcff, term.fcff, last.roic, term.roic)
        flag = flag or hit
        last_year = last.year
        rows.append((f"{name} case, free cash flow (USD millions)",
                     f"year {last.year} {last.fcff:,.0f} to terminal year {term.fcff:,.0f}"
                     + ("" if change is None else f", a change of {change * 100:+.1f}%")
                     + (" (flag)" if hit else "")
                     + ("" if checked else BEAR_EXPECTED)))
        rows.append((f"{name} case, return on capital",
                     f"year {last.year} {_pct(last.roic)} to terminal year {_pct(term.roic)}"))
        if hit and warnings is not None:
            warnings.append(
                f"{name}: the terminal year's free cash flow ({term.fcff:,.0f}) is far below the year-{last.year} "
                f"free cash flow ({last.fcff:,.0f}); the terminal settings and the year-{last.year} inputs disagree")
    note = ("A small drop is normal, because the terminal year reinvests g divided by return on capital. "
            f"Flagged when the terminal year's cash flow is more than {TRANSITION_DROP * 100:.0f}% below the year-"
            f"{last_year} figure, or when the terminal return on capital is below half of that year's. The bear "
            "case is shown but not checked, because its terminal return equals its cost of capital by rule.")
    if flag:
        note = ("A small drop is normal, because the terminal year reinvests g divided by return on capital; a drop "
                "this large means the terminal settings and the last explicit year disagree. Revisit the terminal "
                "return on capital or the shape of the last years, rather than accepting the step. The bear case is "
                "shown but not checked, because its terminal return equals its cost of capital by rule.")
    return Diagnostic("7. The step from the last explicit year into the terminal year", rows, flag=flag, note=note)


def fcff_change(last_fcff: float, terminal_fcff: float) -> float | None:
    """The terminal year's free cash flow against the last explicit year's, as a share of the latter."""
    if last_fcff == 0:
        return None
    return (terminal_fcff - last_fcff) / abs(last_fcff)


def transition_flag(last_fcff: float, terminal_fcff: float, last_roic: float | None,
                    terminal_roic: float | None) -> bool:
    """A cliff, not the normal notch: the cash flow falls too far, or the return on capital halves.

    Damodaran's own published sheets carry a small terminal-year notch (Alphabet February 2024 is
    10.7% below year 10, Microsoft 21%) because the terminal year reinvests ``g / ROIC`` whatever the
    last explicit year spent.  Only a bigger step means the two sets of inputs disagree.
    """
    change = fcff_change(last_fcff, terminal_fcff)
    if change is not None and change < -TRANSITION_DROP:
        return True
    if last_roic is not None and terminal_roic is not None and last_roic > 0:
        return terminal_roic < TRANSITION_ROIC * last_roic
    return False


# --------------------------------------------------------------------------- #
# Entry point
# --------------------------------------------------------------------------- #

def run_analysis(result: ValuationResult, scenario: str = "base",
                 data_dir: Path | None = None) -> Analysis:
    """Grids, reverse DCF and diagnostics for one scenario (the base case by default)."""
    data_dir = data_dir or datasets.DATA_DIR
    warnings: list[str] = []
    industry_name = result.cost_of_capital.industry
    figures = None
    if industry_name:
        try:
            figures = datasets.industry_figures(industry_name, data_dir)
        except datasets.DatasetError as exc:
            warnings.append(f"industry diagnostics unavailable: {exc}")
    else:
        warnings.append("no cost_of_capital.build.damodaran_industry given; industry diagnostics skipped")
    if scenario not in result.scenarios:
        fallback = next(iter(result.scenarios))
        warnings.append(f"{scenario} scenario not computed; analysis uses the {fallback} case")
        scenario = fallback
    res = result.scenarios[scenario]
    base, bridge, price = result.base_year, result.bridge, result.market.price
    grids = [sensitivity_wacc_growth(res.inputs, base, bridge, price),
             sensitivity_growth_margin(res.inputs, base, bridge, price)]
    reverse = reverse_dcf(res.inputs, base, bridge, price)
    diags = diagnostics(result, res, figures, warnings)
    analysis = Analysis(scenario=scenario, grids=grids, reverse=reverse, diagnostics=diags,
                        industry=figures, warnings=warnings)
    result.analysis = analysis
    result.warnings.extend(w for w in warnings if w not in result.warnings)
    return analysis
