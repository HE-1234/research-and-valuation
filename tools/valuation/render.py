"""Render ``valuation.md`` in the order AGENTS.md section 18.5 prescribes.

Prose is kept to short plain sentences; numbers live in tables.  Percentages have one
decimal, money is USD millions with thousands separators and no decimals, per-share
values have two decimals.  The renderer reports numbers and never interprets them.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Iterable

from . import datasets
from .analysis import Analysis, Grid
from .engine import ScenarioResult, ValuationResult
from .market import FRED_URL, YAHOO_URLS
from .schema import EXPLICIT_YEARS, SCENARIO_NAMES, get_path, is_riskfree

CASE_ORDER = ("bear", "base", "bull", "management")
GLOSSARY = [
    ("Cost of capital", "The blended yearly return that the company's lenders and owners require; "
                        "the engine uses it to shrink future cash to today's value."),
    ("Terminal value", "One number standing for all the cash the business produces after the last forecast "
                       "year, assuming it grows at a fixed slow rate forever."),
    ("Reinvestment", "The money the company must put back into the business each year (equipment, working "
                     "capital, acquisitions) to make its revenue grow."),
    ("Sales-to-capital", "How many dollars of extra yearly revenue one dollar of reinvestment buys; the "
                         "engine divides the revenue increase by this number to get reinvestment."),
    ("Enterprise value", "What the market says the whole operating business is worth today: share price "
                         "times shares, plus debt and other claims, minus cash and non-operating assets."),
    ("Return on invested capital", "After-tax operating income divided by the capital tied up in the business; "
                                   "it shows how much profit each dollar of capital earns."),
    ("Reference value", "The same case run with the other forecast length: a ten-year forecast is shown against the "
                        "value it would have if it stopped at year 5, and a five-year forecast against the value it "
                        "would have with five more years in which growth eases to the terminal rate."),
]


# --------------------------------------------------------------------------- #
# Formatting
# --------------------------------------------------------------------------- #

def pct(x: float | None, digits: int = 1) -> str:
    return "n/a" if x is None else f"{x * 100:.{digits}f}%"


def money(x: float | None) -> str:
    return "n/a" if x is None else f"{x:,.0f}"


def per_share(x: float | None) -> str:
    return "n/a" if x is None else f"{x:,.2f}"


def num(x: float | None, digits: int = 2) -> str:
    return "n/a" if x is None else f"{x:.{digits}f}"


def _esc(text: Any) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ").strip()


def table(headers: Iterable[str], rows: Iterable[Iterable[Any]]) -> str:
    hs = [_esc(h) for h in headers]
    lines = ["| " + " | ".join(hs) + " |", "|" + "|".join("---" for _ in hs) + "|"]
    for row in rows:
        lines.append("| " + " | ".join(_esc(c) for c in row) + " |")
    return "\n".join(lines)


def _cases(result: ValuationResult) -> list[str]:
    present = result.assumptions.get("scenarios") or {}
    return [n for n in CASE_ORDER if n in present]


def _cell_source(doc: dict[str, Any], path: str) -> str:
    node = get_path(doc, path)
    if isinstance(node, dict):
        return str(node.get("source") or "")
    return ""


def _cell_reason(doc: dict[str, Any], path: str) -> str:
    node = get_path(doc, path)
    if isinstance(node, dict):
        return str(node.get("reason") or "")
    return ""


# --------------------------------------------------------------------------- #
# Sections
# --------------------------------------------------------------------------- #

def _explicit_years(result: ValuationResult) -> int:
    """The years the analyst set: five when the file carries five-entry lists at a ten-year horizon."""
    for sc in result.scenarios.values():
        if sc.inputs.explicit_years:
            return int(sc.inputs.explicit_years)
    return result.horizon


def _horizon_words(result: ValuationResult) -> str:
    n = _explicit_years(result)
    if n < result.horizon:
        return f"horizon {result.horizon} years ({n} set in the assumptions, the rest by rule)"
    return f"horizon {result.horizon} years"


def header(result: ValuationResult) -> str:
    m = result.market
    rows = [
        ("Ticker", result.ticker, result.company),
        ("As-of quarter", result.as_of_quarter, f"cutoff {result.as_of_date}" if result.as_of_date else ""),
        ("Price (USD per share)", per_share(m.price), f"{m.price_date or ''} ({m.price_source})"),
        ("Risk-free rate (10-year Treasury)", pct(m.risk_free_rate, 2), f"{m.risk_free_date or ''} ({m.risk_free_source})"),
        ("Equity risk premium", pct(m.equity_risk_premium, 2), f"{m.erp_date or ''} ({m.erp_source})"),
        ("Computed", result.computed_at, ""),
        ("Engine", f"valuation {result.engine_version}", f"{_horizon_words(result)}; money in USD millions"),
    ]
    lead = (f"This file is produced by the valuation engine from `assumptions.yaml` for {result.company}. "
            "The owner's judgment lives in that file; this file only shows the arithmetic and the market "
            "data it used.")
    return f"# {result.ticker} valuation as of {result.as_of_quarter}\n\n{lead}\n\n" + table(
        ["Item", "Value", "Date / source"], rows)


def results_table(result: ValuationResult) -> str:
    label = result.reference_label or "reference"
    headers = ["Case", "Weight", "Operating assets", "Enterprise value today", "Equity value",
               "Value per share", "Price", "Upside / downside", "Terminal share of operating assets",
               f"{label} value per share"]
    rows: list[list[str]] = []
    for name in _cases(result):
        sc = result.scenarios.get(name)
        weight = get_path(result.assumptions, f"scenarios.{name}.weight")
        wtxt = pct(float(weight), 0) if weight is not None and name != "management" else "not weighted"
        if sc is None:
            why = "; ".join(result.stopped.get(name, [])) or result.skipped.get(name, "not computed")
            rows.append([name, wtxt, f"not computed: {why}"] + [""] * 7)
            continue
        ref = sc.reference.per_share if sc.reference else None
        rows.append([name, wtxt, money(sc.operating_assets), money(sc.enterprise_value), money(sc.equity),
                     per_share(sc.per_share), per_share(sc.price), pct(sc.upside), pct(sc.terminal_share),
                     per_share(ref)])
    if result.weighted:
        w = result.weighted
        rows.append(["weighted expected", "100%", money(w.operating_assets), money(w.enterprise_value),
                     money(w.equity), per_share(w.per_share), per_share(result.market.price), pct(w.upside),
                     pct(w.terminal_share), per_share(w.reference_per_share)])
    else:
        rows.append(["weighted expected", "", "not computed: a weighted scenario is missing"] + [""] * 7)
    if result.horizon > EXPLICIT_YEARS:
        last = ("the last column stops the same forecast at year 5 and takes the terminal value there, so the cost "
                "of the shorter structure is visible")
    else:
        last = ("the last column stretches the same forecast to ten years, with growth easing to the terminal rate "
                "over years 6 to 10, so the cost of stopping at year 5 is visible")
    lead = ("One row per case. Operating assets is what the forecast cash flows are worth today; enterprise "
            f"value is what the market pays for the same thing; {last}.")
    return "## 1. Results\n\n" + lead + "\n\n" + table(headers, rows)


def stories(result: ValuationResult) -> str:
    parts = ["## 2. The stories", "", "Each story is copied word for word from `assumptions.yaml`."]
    for name in _cases(result):
        weight = get_path(result.assumptions, f"scenarios.{name}.weight")
        title = f"### {name.capitalize()}" + (f" (weight {pct(float(weight), 0)})" if weight is not None
                                               and name != "management" else "")
        story = (get_path(result.assumptions, f"scenarios.{name}.story") or "").strip()
        if name == "management" and name in result.skipped:
            story = (story + "\n\n" if story else "") + f"Not computed: {result.skipped[name]}"
        parts += ["", title, "", story or "(no story given)"]
    return "\n".join(parts)


def _scalar_rows(result: ValuationResult, cases: list[str]) -> list[list[str]]:
    doc = result.assumptions
    coc = result.cost_of_capital

    def col(name: str, fn) -> str:
        try:
            return fn(name)
        except (TypeError, KeyError, ValueError):
            return "null"

    def cell(path: str, fmt) -> list[str]:
        out = []
        for n in cases:
            x = get_path(doc, f"scenarios.{n}.{path}")
            out.append("null" if x is None else fmt(float(x)))
        return out

    def scen_wacc(n: str) -> str:
        x = get_path(doc, f"scenarios.{n}.cost_of_capital_override")
        return pct(coc.wacc, 2) + " (shared)" if x is None else pct(float(x), 2) + " (override)"

    def term_wacc(n: str) -> str:
        sc = result.scenarios.get(n)
        return pct(sc.terminal.wacc, 2) if sc else pct(coc.terminal_wacc, 2)

    def term_roic(n: str) -> str:
        sc = result.scenarios.get(n)
        return pct(sc.terminal.roic, 2) if sc else "n/a"

    def term_growth(n: str) -> str:
        x = get_path(doc, f"scenarios.{n}.terminal.growth.value")
        if is_riskfree(x):
            return pct(result.market.risk_free_rate, 2) + " (= risk-free rate)"
        return "null" if x is None else pct(float(x), 2)

    return [
        ["Weight"] + [("not weighted" if n == "management" else pct(float(get_path(doc, f"scenarios.{n}.weight") or 0), 0))
                      for n in cases],
        ["Sales-to-capital, years 1-5"] + cell("sales_to_capital.value", lambda x: num(x, 2)),
        [("Sales-to-capital, years 6-10" if result.horizon > EXPLICIT_YEARS
          else "Sales-to-capital, years 6-10 (10-year-fade reference only)")]
        + cell("sales_to_capital.value_late", lambda x: num(x, 2)),
        ["Tax rate, explicit years"] + cell("tax_rate.start", pct),
        ["Tax rate, terminal"] + cell("tax_rate.terminal", pct),
        ["Cost of capital, explicit years"] + [col(n, scen_wacc) for n in cases],
        ["Terminal cost of capital"] + [col(n, term_wacc) for n in cases],
        ["Terminal growth"] + [col(n, term_growth) for n in cases],
        ["Terminal ROIC premium over cost of capital"] + cell("terminal.roic_premium.value", lambda x: pct(x, 2)),
        ["Terminal ROIC"] + [col(n, term_roic) for n in cases],
    ]


def _year_columns(result: ValuationResult, cases: list[str], key: str) -> int:
    """How many year columns a per-year input needs: the longest list the cases carry."""
    lengths = [len(get_path(result.assumptions, f"scenarios.{n}.{key}.values") or []) for n in cases]
    return max([n for n in lengths if n] or [result.horizon])


def _year_table(result: ValuationResult, cases: list[str], key: str, fmt, null_text: str) -> str:
    doc = result.assumptions
    T = _year_columns(result, cases, key)
    rows = []
    for n in cases:
        values = (get_path(doc, f"scenarios.{n}.{key}.values") or [None] * T)[:T]
        rows.append([n] + [null_text if x is None else fmt(float(x)) for x in values] + [""] * (T - len(values)))
    return table(["Case"] + [f"Year {t}" for t in range(1, T + 1)], rows)


def fade_sentence(year5_growth: float | None, last_growth: float | None, year5_margin: float | None,
                  *, terminal_words: str | None = None) -> str:
    """"growth eases from 20.0% to 4.2%; margin holds at 26.0%" - the rule of section 18.2 in words."""
    falling = (year5_growth is not None and last_growth is not None and last_growth < year5_growth)
    to = terminal_words or pct(last_growth)
    return (f"growth {'eases' if falling else 'moves'} from {pct(year5_growth)} to {to}; "
            f"margin holds at {pct(year5_margin)}")


def _by_rule_note(result: ValuationResult) -> str:
    """One line per case under the per-year tables when years 6-10 come from the rule of section 18.2."""
    n = _explicit_years(result)
    if n >= result.horizon:
        return ""
    lines = [f"- {name}: " + fade_sentence(sc.inputs.growth[n - 1], sc.inputs.growth[-1], sc.inputs.margin[n - 1])
             + f" through year {result.horizon}."
             for name, sc in result.scenarios.items()]
    return (f"\nYears {n + 1}-{result.horizon} are built by rule from year {n}, not written in the assumptions: "
            "growth moves in equal steps to terminal growth, the margin holds at its year-"
            f"{n} level, per-year reinvestment figures stop, and sales-to-capital switches to the "
            f"years {n + 1}-{result.horizon} ratio.\n\n" + "\n".join(lines) + "\n")


def assumptions_section(result: ValuationResult) -> str:
    cases = _cases(result)
    doc = result.assumptions
    parts = ["## 3. Assumptions", "",
             "Rows are inputs and columns are cases. Rates are shown as percentages; the YAML holds decimals.",
             "", table(["Input"] + cases, _scalar_rows(result, cases)),
             "", "### Revenue growth by year", "", _year_table(result, cases, "revenue_growth", pct, "null"),
             "", "### Operating margin by year", "", _year_table(result, cases, "operating_margin", pct, "null"),
             "", "### Reinvestment override by year (USD millions; blank means sales-to-capital is used)", "",
             _year_table(result, cases, "reinvestment_override", money, ""), _by_rule_note(result)]
    parts += ["", "### Reasoning", ""]
    cell_paths = [
        ("revenue_growth", "Revenue growth"), ("operating_margin", "Operating margin"),
        ("sales_to_capital", "Sales-to-capital"), ("reinvestment_override", "Reinvestment override"),
        ("tax_rate", "Tax rate"), ("terminal.growth", "Terminal growth"),
        ("terminal.roic_premium", "Terminal ROIC premium"),
    ]
    for n in cases:
        parts.append(f"**{n.capitalize()}**")
        parts.append("")
        for path, label in cell_paths:
            reason = _cell_reason(doc, f"scenarios.{n}.{path}")
            source = _cell_source(doc, f"scenarios.{n}.{path}")
            if not reason and not source:
                continue
            line = f"- {label}: {reason}".rstrip()
            if source:
                line += f" Source: {source}"
            parts.append(line)
        override = get_path(doc, f"scenarios.{n}.cost_of_capital_override")
        if override is not None:
            parts.append(f"- Cost of capital override: {pct(float(override), 2)}")
        if n == "management":
            guidance = get_path(doc, "scenarios.management.guidance") or []
            if guidance:
                parts += ["", "Management guidance on record:", ""]
                parts.append(table(["Item", "Quote", "Source", "Used as"],
                                   [[g.get("item", ""), g.get("quote", ""), g.get("source", ""), g.get("used_as", "")]
                                    for g in guidance if isinstance(g, dict)]))
        parts.append("")
    return "\n".join(parts).rstrip()


def base_year_section(result: ValuationResult) -> str:
    doc, by = result.assumptions, result.base_year
    switches = doc.get("switches") or {}
    rows: list[list[str]] = [
        ["Revenue (TTM)", money(by.revenue), _cell_source(doc, "base_year.revenue")],
        ["Operating income, GAAP", money(by.operating_income_gaap), _cell_source(doc, "base_year.operating_income_gaap")],
    ]
    for item in get_path(doc, "base_year.one_time_items") or []:
        if isinstance(item, dict):
            rows.append([f"One-time item: {item.get('name', '')}", money(float(item.get("value") or 0)),
                         f"{item.get('source', '')} {item.get('reason', '')}".strip()])
    amort_text = "added back (switch on)" if switches.get("addback_acquired_amortization") else "memo; stays deducted"
    rows.append([f"Amortization of acquired intangibles ({amort_text})", money(by.amortization_memo),
                 _cell_source(doc, "base_year.amortization_of_acquired_intangibles")])
    rows.append(["Stock-based compensation (memo; stays expensed)", money(by.stock_based_compensation_memo),
                 _cell_source(doc, "base_year.stock_based_compensation")])
    if switches.get("capitalize_rnd"):
        rows.append(["R&D expense (capitalized, switch on)", money(by.rnd_expense_memo), _cell_source(doc, "base_year.rnd_expense")])
        rows.append([f"R&D amortization this year ({switches.get('rnd_amortization_years', 5)}-year life)",
                     money(by.rnd_amortization), "derived"])
        rows.append(["R&D adjustment to operating income", money(by.rnd_adjustment), "derived"])
        rows.append(["R&D asset added to invested capital", money(by.rnd_asset), "derived"])
    else:
        rows.append(["R&D expense (memo; stays expensed)", money(by.rnd_expense_memo), _cell_source(doc, "base_year.rnd_expense")])
    rows.append(["Adjusted operating income", money(by.adjusted_operating_income), "derived"])
    rows.append(["Adjusted operating margin", pct(by.margin), "derived"])
    rows.append(["Effective tax rate", pct(by.effective_tax_rate), _cell_source(doc, "base_year.effective_tax_rate")])
    rows.append(["Invested capital (book equity + debt + leases - cash)", money(by.invested_capital_reported),
                 _cell_source(doc, "base_year.invested_capital")])
    if by.rnd_asset:
        rows.append(["Invested capital including R&D asset", money(by.invested_capital), "derived"])
    rows.append(["Base-year return on invested capital", pct(by.roic), "derived; a check, not an input"])
    period = get_path(doc, "base_year.period") or ""
    return f"### Base year ({period})\n\n" + table(["Item", "USD millions", "Source"], rows)


def bridge_section(result: ValuationResult) -> str:
    doc, b = result.assumptions, result.bridge
    rows: list[list[str]] = [
        ["Cash and marketable securities (added)", money(b.cash), _cell_source(doc, "bridge.cash_and_marketable_securities")],
    ]
    for item in get_path(doc, "bridge.non_operating_assets") or []:
        if isinstance(item, dict):
            rows.append([f"Non-operating asset (added): {item.get('name', '')}", money(float(item.get("value") or 0)),
                         f"{item.get('source', '')} {item.get('reason', '')}".strip()])
    rows.append(["Debt (subtracted)", money(b.debt), _cell_source(doc, "bridge.debt")])
    rows.append(["Operating lease liabilities (subtracted)", money(b.leases), _cell_source(doc, "bridge.operating_lease_liabilities")])
    rows.append(["Minority interests (subtracted)", money(b.minority_interests), _cell_source(doc, "bridge.minority_interests")])
    for item in get_path(doc, "bridge.other_claims") or []:
        if isinstance(item, dict):
            rows.append([f"Other claim (subtracted): {item.get('name', '')}", money(float(item.get("value") or 0)),
                         item.get("source", "")])
    rows.append(["Probability of failure", pct(b.probability_of_failure), _cell_reason(doc, "bridge.probability_of_failure")])
    rows.append(["Distress proceeds if the firm fails", money(b.distress_proceeds), _cell_reason(doc, "bridge.distress_proceeds")])
    rows.append(["Diluted shares (millions)", f"{b.diluted_shares:,.1f}", _cell_source(doc, "bridge.diluted_shares")])
    note = get_path(doc, "bridge.dilution_note") or ""
    out = "### Bridge from operating assets to equity\n\n" + table(["Item", "USD millions", "Source / reason"], rows)
    if note:
        out += f"\n\nDilution note: {note}"
    return out


def cost_of_capital_section(result: ValuationResult) -> str:
    doc, c, m = result.assumptions, result.cost_of_capital, result.market
    rows: list[list[str]] = [
        ["Method", c.method, ""],
        ["Risk-free rate", pct(c.risk_free, 2), f"{m.risk_free_date or ''} ({m.risk_free_source})"],
        ["Equity risk premium", pct(c.equity_risk_premium, 2), f"{m.erp_date or ''} ({m.erp_source})"],
        ["Marginal tax rate", pct(c.marginal_tax), "market.marginal_tax_rate"],
    ]
    if c.method == "build":
        rows += [
            ["Damodaran industry", c.industry or "", _cell_reason(doc, "cost_of_capital.build.damodaran_industry")],
            ["Unlevered beta", num(c.unlevered_beta, 3),
             c.unlevered_beta_note or _cell_source(doc, "cost_of_capital.build.unlevered_beta")],
            ["Debt to equity (market)", num(c.debt_to_equity, 3),
             ("derived: " + c.debt_to_equity_note) if c.debt_to_equity_note
             else _cell_source(doc, "cost_of_capital.build.debt_to_equity_market")],
            ["Levered beta", num(c.levered_beta, 3), "derived"],
            ["Cost of equity", pct(c.cost_of_equity, 2), "derived"],
            ["Pre-tax cost of debt", pct(c.pretax_cost_of_debt, 2), _cell_source(doc, "cost_of_capital.build.pretax_cost_of_debt")],
            ["After-tax cost of debt", pct(c.after_tax_cost_of_debt, 2), "derived"],
            ["Weights: equity / debt", f"{pct(c.weight_equity)} / {pct(c.weight_debt)}", "derived"],
        ]
    else:
        rows.append(["Pinned value", pct(c.wacc, 2), _cell_reason(doc, "cost_of_capital") or "cost_of_capital.pinned_value"])
    rows.append(["Cost of capital (WACC)", pct(c.wacc, 2), "derived"])
    rows.append(["Terminal method", c.terminal_method, _cell_reason(doc, "cost_of_capital.terminal")])
    if c.terminal_method == "mature":
        rows.append(["Mature-market equity risk premium", pct(c.mature_market_erp, 2), "market.mature_market_erp"])
    rows.append(["Terminal cost of capital", pct(c.terminal_wacc, 2), "derived"])
    return "### Cost of capital\n\n" + table(["Item", "Value", "Source"], rows)


def terminal_section(result: ValuationResult) -> str:
    rows = []
    for name, sc in result.scenarios.items():
        t = sc.terminal
        rows.append([name, pct(t.growth, 2), pct(t.wacc, 2), pct(t.roic, 2), pct(t.reinvestment_rate),
                     money(t.ebit_after_tax), money(t.fcff), money(t.value), money(t.pv), pct(sc.terminal_share)])
    return "### Terminal values by case\n\n" + table(
        ["Case", "Growth", "Cost of capital", "ROIC", "Reinvestment rate (g / ROIC)",
         "After-tax operating income, year T+1", "Free cash flow, year T+1", "Terminal value",
         "Present value", "Share of operating assets"], rows)


def tables_section(result: ValuationResult) -> str:
    return "\n\n".join(["## 4. Base year, bridge, cost of capital, terminal", base_year_section(result),
                        bridge_section(result), cost_of_capital_section(result), terminal_section(result)])


def year_by_year(result: ValuationResult, name: str = "base") -> str:
    sc = result.scenarios.get(name) or next(iter(result.scenarios.values()))
    explicit = sc.inputs.explicit_years or sc.inputs.horizon
    rows = []
    for r in sc.rows:
        reinv = money(r.reinvestment) + (" (override)" if r.reinvestment_source == "override" else "")
        rows.append([str(r.year), "by rule" if r.year > explicit else "from the assumptions",
                     money(r.revenue), pct(r.growth),
                     pct(r.margin), money(r.ebit_after_tax), reinv, money(r.fcff), num(r.discount_factor, 4),
                     money(r.pv), pct(r.roic)])
    t = sc.terminal
    rows.append(["Terminal (year T+1)", "terminal settings", money(t.revenue), pct(t.growth), pct(t.margin),
                 money(t.ebit_after_tax), money(t.reinvestment), money(t.fcff),
                 num(sc.rows[-1].discount_factor, 4), money(t.pv), pct(t.roic)])
    extra = ""
    if explicit < sc.inputs.horizon:
        extra = (f" Years 1-{explicit} come from the assumptions; years {explicit + 1}-{sc.inputs.horizon} are marked "
                 "\"by rule\": growth eases to terminal growth, the margin holds, and the tax rate and cost of "
                 "capital move to their terminal values.")
    lead = (f"The {sc.name} case, year by year. Reinvestment in a year buys the next year's growth, so the "
            f"last forecast year's reinvestment is sized for terminal growth.{extra}")
    return f"## 5. {sc.name.capitalize()} case, year by year\n\n{lead}\n\n" + table(
        ["Year", "How the year is set", "Revenue", "Growth", "Margin", "After-tax operating income", "Reinvestment",
         "Free cash flow", "Discount factor", "Present value", "Implied ROIC"], rows)


def grid_table(grid: Grid) -> str:
    headers = [f"{grid.row_label} \\ {grid.col_label}"] + [pct(c) for c in grid.col_values]
    rows = []
    for i, rv in enumerate(grid.row_values):
        cells = []
        for j, cell in enumerate(grid.cells[i]):
            text = per_share(cell) if cell is not None else "n/a"
            cells.append(f"**{text}**" if i == grid.base_row and j == grid.base_col else text)
        rows.append([pct(rv)] + cells)
    return f"### {grid.title}\n\n{grid.note} The base case is in bold.\n\n" + table(headers, rows)


def sensitivity_section(analysis: Analysis) -> str:
    return "\n\n".join([f"## 6. Sensitivity ({analysis.scenario} case)"] + [grid_table(g) for g in analysis.grids])


def reverse_section(analysis: Analysis) -> str:
    r = analysis.reverse
    if r is None:
        return "## 7. Reverse DCF\n\nNot computed."
    rows = [
        ["Enterprise value today (target)", money(r.target_enterprise_value)],
        [f"Operating assets in the {analysis.scenario} case", money(r.base_operating_assets)],
        [f"Average revenue growth in the {analysis.scenario} case (years 1-5)", pct(r.base_average_growth)],
        ["Constant annual growth that matches the price", pct(r.implied_growth) if r.implied_growth is not None
         else f"not found: {r.implied_growth_note}"],
        [f"Year-5 margin in the {analysis.scenario} case", pct(r.base_year5_margin)],
        ["Year-5 margin that matches the price", pct(r.implied_year5_margin) if r.implied_year5_margin is not None
         else f"not found: {r.implied_margin_note}"],
    ]
    lead = (f"The first solve keeps the {analysis.scenario} case's margins, reinvestment rule, cost of capital "
            "and terminal settings, and asks what constant yearly revenue growth would make operating assets "
            "equal today's enterprise value. The second keeps the growth path and solves for the year-5 margin.")
    return f"## 7. Reverse DCF ({analysis.scenario} case)\n\n{lead}\n\n" + table(["Item", "Value"], rows)


def diagnostics_section(analysis: Analysis) -> str:
    parts = ["## 8. Diagnostics", "",
             "Damodaran's six checks and the step into the terminal year. Industry figures come from the cached "
             "datasets and carry the dataset date."]
    if analysis.industry:
        f = analysis.industry
        names = {v.matched_name for v in (f.unlevered_beta_cash_corrected, f.cost_of_capital, f.sales_to_capital,
                                          f.pretax_operating_margin, f.revenue_cagr_5y) if v.matched_name}
        parts[-1] += f" Industry looked up: '{f.industry}'" + (f" (matched '{', '.join(sorted(names))}')" if names else "") + "."
        rows = [
            ["Unlevered beta corrected for cash", num(f.unlevered_beta_cash_corrected.value, 3), f.unlevered_beta_cash_corrected.dataset_date or ""],
            ["Cost of capital", pct(f.cost_of_capital.value), f.cost_of_capital.dataset_date or ""],
            ["Sales to invested capital", num(f.sales_to_capital.value, 2), f.sales_to_capital.dataset_date or ""],
            ["Pre-tax operating margin", pct(f.pretax_operating_margin.value), f.pretax_operating_margin.dataset_date or ""],
            ["Revenue growth, last 5 years (CAGR)", pct(f.revenue_cagr_5y.value), f.revenue_cagr_5y.dataset_date or ""],
            ["Effective tax rate (money-making companies)", pct(f.effective_tax_rate.value), f.effective_tax_rate.dataset_date or ""],
        ]
        parts += ["", table(["Industry figure", "Value", "Dataset date"], rows)]
    for d in analysis.diagnostics:
        parts += ["", f"### {d.title}" + (" (flag)" if d.flag else ""), ""]
        parts.append(table(["Item", "Value"], d.rows))
        if d.note:
            parts += ["", d.note]
    return "\n".join(parts)


def warnings_section(result: ValuationResult) -> str:
    items = list(result.warnings)
    if result.analysis:
        items += [w for w in result.analysis.warnings if w not in items]
    body = "\n".join(f"- {w}" for w in items) if items else "None."
    return "## 9. Warnings\n\n" + body


def glossary_section() -> str:
    return "## 10. Glossary\n\n" + "\n".join(f"- **{term}**: {text}" for term, text in GLOSSARY)


# --------------------------------------------------------------------------- #
# Sources
# --------------------------------------------------------------------------- #

def collect_source_tags(doc: Any) -> list[str]:
    """Every bracketed tag inside any ``source`` string in the document, in order, unique."""
    tags: list[str] = []

    def walk(node: Any) -> None:
        if isinstance(node, dict):
            for key, val in node.items():
                if key == "source" and isinstance(val, str):
                    found = re.findall(r"\[([^\[\]]+)\]", val)
                    tags.extend(found or [val.strip()])
                else:
                    walk(val)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(doc)
    return [t for t in dict.fromkeys(t.strip() for t in tags) if t]


def _sources_tables(company_dir: Path) -> list[tuple[str, str]]:
    """(prefix, path) pairs from the Sources tables of business.md and outlook.md."""
    pairs: list[tuple[str, str]] = []
    for name in ("business.md", "outlook.md"):
        path = company_dir / name
        if not path.exists():
            continue
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            m = re.match(r"^\|\s*\[([^\]]+)\]\s*\|\s*`([^`]+)`", line)
            if m:
                pairs.append((m.group(1).strip(), m.group(2).strip()))
    return pairs


def _head(tag: str) -> str:
    head = tag.split(",")[0]
    head = re.sub(r"\b(p\.?\s*\S+|pp\.?\s*\S+|…|\.\.\.)$", "", head).strip()
    return re.sub(r"\s+", " ", head).lower()


def _quarter_dir_candidates(tag: str) -> list[str]:
    """'Q2 FY2027' -> ['FY2027-Q2']; 'Q2 2026' -> ['2026-Q2']; 'FY2027-Q2' passes through."""
    out = []
    for m in re.finditer(r"\b(Q[1-4])\s+(FY\d{4}|\d{4})\b", tag, re.I):
        out.append(f"{m.group(2).upper()}-{m.group(1).upper()}")
    for m in re.finditer(r"\b((?:FY)?\d{4}-Q[1-4])\b", tag, re.I):
        out.append(m.group(1).upper())
    return out


def _heuristic_file(tag: str, company_dir: Path) -> str | None:
    sources = company_dir / "sources"
    if not sources.exists():
        return None
    low = tag.lower()
    candidates: list[str] = []
    if "10-k" in low:
        m = re.search(r"FY\s?(\d{4})", tag, re.I)
        if m:
            candidates.append(f"10-K-FY{m.group(1)}.txt")
    if "10-q" in low:
        candidates += [f"10-Q-{q}.txt" for q in _quarter_dir_candidates(tag)]
    if "8-k" in low:
        m = re.search(r"(\d{4}-\d{2}-\d{2})", tag)
        if m:
            candidates.append(f"8-K-{m.group(1)}.txt")
    if "def 14a" in low or "def14a" in low:
        m = re.search(r"(\d{4})", tag)
        if m:
            candidates += [f"DEF14A-{m.group(1)}.txt", f"DEF-14A-{m.group(1)}.txt"]
    kind = None
    for word, fname in (("call", "transcript.txt"), ("transcript", "transcript.txt"), ("release", "press-release.txt"),
                        ("slides", "slides.txt"), ("supplemental", "supplemental.txt")):
        if re.search(rf"\b{word}\b", low):
            kind = fname
            break
    if kind:
        for q in _quarter_dir_candidates(tag):
            p = sources / q / kind
            if p.exists():
                return str(p.relative_to(company_dir))
    for qdir in sorted(sources.iterdir(), reverse=True):
        if not qdir.is_dir():
            continue
        for fname in candidates:
            if (qdir / fname).exists():
                return str((qdir / fname).relative_to(company_dir))
    return None


def resolve_tag(tag: str, company_dir: Path | None, pairs: list[tuple[str, str]]) -> str:
    low = tag.lower()
    if "damodaran" in low:
        for key in ("betas", "wacc", "capex", "margin", "taxrate", "histgr", "erp"):
            if key in low or (key == "erp" and "erpbymonth" in low):
                return datasets.BASE_URL + datasets.SPEC_BY_KEY[key].remote
        return datasets.BASE_URL + "New_Home_Page/data.html"
    if company_dir is None:
        return "not resolved (no company directory)"
    head = _head(tag)
    best: tuple[int, str] | None = None
    for prefix, path in pairs:
        ph = _head(prefix)
        if head == ph or head.startswith(ph) or low.startswith(prefix.lower()):
            if best is None or len(ph) > best[0]:
                best = (len(ph), path)
    if best:
        return f"`{_existing_path(best[1], company_dir)}`"
    found = _heuristic_file(tag, company_dir)
    return f"`{found}`" if found else "not resolved in sources/"


def _existing_path(path: str, company_dir: Path) -> str:
    """Sources tables sometimes give a bare file name; find it under sources/<QLABEL>/."""
    if (company_dir / path).exists():
        return path
    sources = company_dir / "sources"
    if sources.exists():
        for qdir in sorted(sources.iterdir(), reverse=True):
            if qdir.is_dir() and (qdir / Path(path).name).exists():
                return str((qdir / Path(path).name).relative_to(company_dir))
    return path


def sources_section(result: ValuationResult) -> str:
    doc = result.assumptions
    company_dir = Path(result.company_dir) if result.company_dir else None
    pairs = _sources_tables(company_dir) if company_dir else []
    tags = collect_source_tags(doc)
    rows = [[f"[{t}]", resolve_tag(t, company_dir, pairs)] for t in tags]
    m = result.market
    feed_rows = [
        ["Price", YAHOO_URLS[0].format(ticker=result.ticker), f"{m.price_date or ''} ({m.price_source})"],
        ["Risk-free rate", FRED_URL, f"{m.risk_free_date or ''} ({m.risk_free_source})"],
    ]
    for key, url, fetched, updated in datasets.dataset_sources():
        feed_rows.append([f"Damodaran {key}", url, f"fetched {fetched or 'n/a'}; file dated {updated or 'n/a'}"])
    parts = ["## 11. Sources", "",
             "Source tags used in `assumptions.yaml`, mapped to the cached files where the tag prefix could be "
             "matched against the Sources tables of `business.md` and `outlook.md` or the file names under "
             "`sources/`. Paths are relative to the company folder."]
    parts += ["", table(["Tag", "Cached file"], rows) if rows else "No source tags found in assumptions.yaml.",
              "", "Feeds and datasets:", "", table(["Feed", "URL", "Fetched / dated"], feed_rows)]
    return "\n".join(parts)


# --------------------------------------------------------------------------- #
# Entry point
# --------------------------------------------------------------------------- #

def render(result: ValuationResult) -> str:
    analysis = result.analysis
    if analysis is None:
        from .analysis import run_analysis
        analysis = run_analysis(result)
    parts = [header(result), results_table(result), stories(result), assumptions_section(result),
             tables_section(result), year_by_year(result, analysis.scenario), sensitivity_section(analysis),
             reverse_section(analysis), diagnostics_section(analysis), warnings_section(result),
             glossary_section(), sources_section(result)]
    return "\n\n".join(parts).rstrip() + "\n"


def results_text(result: ValuationResult) -> str:
    """The results table plus warnings, for stdout."""
    return results_table(result) + "\n\n" + warnings_section(result) + "\n"
