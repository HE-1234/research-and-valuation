"""Render ``assumptions.md``: a read-only view of ``assumptions.yaml`` (AGENTS.md section 18.9).

No market data, no computing.  The file shows the header, the stories, one table of
scenario inputs, the reason and source behind every scenario cell, then the base year,
switches, bridge, market block, cost of capital, diagnostics inputs, management guidance
and the change log, in the order of section 18.4.  Percentages have one decimal, money
is USD millions with separators, and an empty cell is shown as a dash.
"""

from __future__ import annotations

from datetime import date, datetime
from pathlib import Path
from typing import Any

from .render import _esc, table
from .schema import SCENARIO_NAMES as CASE_ORDER_ALL, get_path, is_riskfree

DASH = "—"          # an empty cell: nothing defensible, or not given
SCENARIO_LABELS = {"bear": "Bear", "base": "Base", "bull": "Bull", "management": "Management"}


# --------------------------------------------------------------------------- #
# Formatting
# --------------------------------------------------------------------------- #

def _pct(x: Any, digits: int = 1) -> str:
    if x is None:
        return DASH
    try:
        return f"{float(x) * 100:.{digits}f}%"
    except (TypeError, ValueError):
        return str(x)


def _money(x: Any) -> str:
    if x is None:
        return DASH
    try:
        v = float(x)
    except (TypeError, ValueError):
        return str(x)
    return f"{v:,.0f}" if abs(v - round(v)) < 1e-9 else f"{v:,.1f}"


def _num(x: Any, digits: int = 2) -> str:
    if x is None:
        return DASH
    try:
        return f"{float(x):.{digits}f}"
    except (TypeError, ValueError):
        return str(x)


def _yes(x: Any) -> str:
    if x is None:
        return DASH
    return "yes" if x else "no"


def _text(x: Any) -> str:
    if x is None or (isinstance(x, str) and not x.strip()):
        return DASH
    if isinstance(x, (datetime, date)):
        return x.isoformat(sep=" ") if isinstance(x, datetime) else x.isoformat()
    return str(x)


def _raw(x: Any) -> str:
    """A value exactly as the file holds it, lightly formatted (used in the change log)."""
    if x is None:
        return DASH
    if isinstance(x, bool):
        return "yes" if x else "no"
    if isinstance(x, (list, tuple)):
        return " / ".join(_raw(v) for v in x) if x else "(empty list)"
    if isinstance(x, dict):
        return ", ".join(f"{k}: {_raw(v)}" for k, v in x.items())
    if isinstance(x, float):
        text = f"{x:,.6f}".rstrip("0").rstrip(".")
        return text if text not in ("", "-") else "0"
    if isinstance(x, int):
        return f"{x:,}"
    return str(x)


def _years(values: Any, fmt, horizon: int) -> str:
    if not isinstance(values, list):
        return DASH
    cells = [fmt(v) for v in values]
    cells += [DASH] * max(0, horizon - len(cells))
    return " / ".join(cells)


def _cell(doc: dict[str, Any], path: str, key: str = "value") -> Any:
    node = get_path(doc, path)
    return node.get(key) if isinstance(node, dict) else None


def _reason(doc: dict[str, Any], path: str) -> str:
    node = get_path(doc, path)
    return _text(node.get("reason")) if isinstance(node, dict) else DASH


def _source(doc: dict[str, Any], path: str) -> str:
    node = get_path(doc, path)
    return _text(node.get("source")) if isinstance(node, dict) else DASH


def _cases(doc: dict[str, Any]) -> list[str]:
    present = doc.get("scenarios") or {}
    return [n for n in CASE_ORDER_ALL if n in present]


def _horizon(doc: dict[str, Any]) -> int:
    h = doc.get("horizon", 5)
    return int(h) if isinstance(h, int) and not isinstance(h, bool) else 5


# --------------------------------------------------------------------------- #
# Sections
# --------------------------------------------------------------------------- #

def header(doc: dict[str, Any]) -> str:
    ticker = _text(doc.get("ticker"))
    company = _text(doc.get("company"))
    quarter = _text(doc.get("as_of_quarter"))
    rows = [
        ["Ticker", ticker],
        ["Company", company],
        ["As-of quarter", quarter],
        ["As-of date (quarter cutoff)", _text(doc.get("as_of_date"))],
        ["Drafted", _text(doc.get("drafted"))],
    ]
    if doc.get("owner_edited"):
        rows.append(["Owner edited (last save from the app)", _text(doc.get("owner_edited"))])
    rows.append(["Horizon", f"{_horizon(doc)} explicit years, then a terminal value"])
    rows.append(["Currency and units", f"{_text(doc.get('currency', 'USD'))}, {_text(doc.get('units', 'millions'))}"])
    log = doc.get("changelog")
    if isinstance(log, list) and log:
        rows.append(["Owner changes on record", f"{len(log)} (see the change log at the end)"])
    lead = (f"This file is a read-only view of the valuation inputs for {company} ({ticker}), held in "
            "`assumptions.yaml`. Every number and every sentence below comes from that file; nothing is computed "
            "here. To change a number, use the app "
            "(`uv run --extra app valuation-app`), which saves into the YAML, records the change, and rewrites "
            f"this file. A dash ({DASH}) marks a cell that is empty in the file: the analyst had nothing "
            "defensible to put there, or the item is not given. Rates are stored as decimals and shown here "
            "as percentages; money is in USD millions.")
    return f"# {ticker} valuation assumptions as of {quarter}\n\n{lead}\n\n" + table(["Item", "Value"], rows)


def stories(doc: dict[str, Any]) -> str:
    parts = ["## 1. The stories", "", "Each story is copied word for word from `assumptions.yaml`."]
    for name in _cases(doc):
        sc = doc["scenarios"][name] or {}
        title = f"### {SCENARIO_LABELS[name]}"
        if name == "management":
            computable = sc.get("computable", False)
            title += " (not weighted; " + ("computed" if computable else "not computed") + ")"
        elif sc.get("weight") is not None:
            title += f" (weight {_pct(sc.get('weight'))})"
        story = (sc.get("story") or "").strip()
        parts += ["", title, "", story or "(no story given)"]
        if name == "management" and sc.get("reason"):
            parts += ["", f"Why this case is {'computed' if sc.get('computable') else 'not computed'}: {sc['reason'].strip()}"]
    return "\n".join(parts)


def _terminal_growth(doc: dict[str, Any], name: str) -> str:
    x = _cell(doc, f"scenarios.{name}.terminal.growth")
    if is_riskfree(x):
        return "the run's risk-free rate"
    return _pct(x, 2)


def scenario_table(doc: dict[str, Any]) -> str:
    cases = _cases(doc)
    T = _horizon(doc)
    late = "years 6-10" if T == 10 else "years 6-10 of the 10-year reference"

    def row(label: str, fn) -> list[str]:
        return [label] + [fn(n) for n in cases]

    def cell(path: str, fmt):
        return lambda n: fmt(_cell(doc, f"scenarios.{n}.{path.rsplit('.', 1)[0]}", path.rsplit(".", 1)[1]))

    rows = [
        row("Weight", lambda n: "not weighted" if n == "management" else _pct(get_path(doc, f"scenarios.{n}.weight"))),
        row(f"Revenue growth, years 1-{T}", lambda n: _years(_cell(doc, f"scenarios.{n}.revenue_growth", "values"), _pct, T)),
        row(f"Operating margin, years 1-{T}", lambda n: _years(_cell(doc, f"scenarios.{n}.operating_margin", "values"), _pct, T)),
        row("Sales-to-capital, years 1-5", cell("sales_to_capital.value", lambda x: _num(x, 2))),
        row(f"Sales-to-capital, {late}", cell("sales_to_capital.value_late", lambda x: _num(x, 2))),
        row(f"Reinvestment override, years 1-{T} (USD millions)",
            lambda n: _years(_cell(doc, f"scenarios.{n}.reinvestment_override", "values"), _money, T)),
        row("Tax rate, explicit years", cell("tax_rate.start", _pct)),
        row("Tax rate, terminal year onwards", cell("tax_rate.terminal", _pct)),
        row("Cost of capital override", lambda n: _pct(get_path(doc, f"scenarios.{n}.cost_of_capital_override"), 2)),
        row("Terminal growth", lambda n: _terminal_growth(doc, n)),
        row("Terminal growth may exceed the risk-free rate", cell("terminal.growth.allow_above_riskfree", _yes)),
        row("Terminal return on capital: points above the cost of capital", cell("terminal.roic_premium.value", lambda x: _pct(x, 2))),
        row("A premium above 5 points is allowed", cell("terminal.roic_premium.allow_large_premium", _yes)),
    ]
    if "management" in cases:
        rows.insert(1, row("Computable", lambda n: _yes(get_path(doc, "scenarios.management.computable")) if n == "management" else "always"))
    lead = ("Rows are inputs and columns are cases. Per-year cells read year 1 / year 2 / ... in order. "
            "The reasons and sources behind each cell follow the table.")
    return "## 2. Scenario inputs\n\n" + lead + "\n\n" + table(["Input"] + [SCENARIO_LABELS[n] for n in cases], rows)


REASON_ROWS = [
    ("revenue_growth", "Revenue growth"),
    ("operating_margin", "Operating margin"),
    ("sales_to_capital", "Sales-to-capital"),
    ("reinvestment_override", "Reinvestment override"),
    ("tax_rate", "Tax rate"),
    ("terminal.growth", "Terminal growth"),
    ("terminal.roic_premium", "Terminal return on capital premium"),
]


def reasons(doc: dict[str, Any]) -> str:
    parts: list[str] = []
    for name in _cases(doc):
        parts += ["", f"### {SCENARIO_LABELS[name]}: reasons", ""]
        if name == "management":
            reason = _text(get_path(doc, "scenarios.management.reason"))
            parts.append(f"- **Computable: {_yes(get_path(doc, 'scenarios.management.computable'))}** {DASH} {reason}")
        for path, label in REASON_ROWS:
            node = get_path(doc, f"scenarios.{name}.{path}")
            if not isinstance(node, dict):
                continue
            reason = _text(node.get("reason"))
            source = node.get("source")
            line = f"- **{label}** {DASH} {reason}"
            if source:
                line += f" {_esc(source)}"
            parts.append(line)
            detail = node.get("detail")
            if detail:
                parts += ["", _indented(detail)]
        override = get_path(doc, f"scenarios.{name}.cost_of_capital_override")
        if override is not None:
            parts.append(f"- **Cost of capital override** {DASH} pinned at {_pct(override, 2)} for this case only.")
    return "\n".join(parts).lstrip("\n")


def _indented(detail: Any) -> str:
    """Working notes as an indented paragraph under a list item; line breaks are kept."""
    return "\n".join("    " + line.rstrip() for line in str(detail).strip().splitlines())


def _details(doc: dict[str, Any], block: str) -> str:
    """Working notes (`detail`) of the cells in a block, as indented paragraphs after its table."""
    node = get_path(doc, block)
    if not isinstance(node, dict):
        return ""
    out = []
    for key, cell in node.items():
        if isinstance(cell, dict) and cell.get("detail"):
            out.append(f"- **{key.replace('_', ' ').capitalize()}**, working notes:\n\n" + _indented(cell["detail"]))
    return "\n\n" + "\n\n".join(out) if out else ""


def base_year(doc: dict[str, Any]) -> str:
    period = _text(get_path(doc, "base_year.period"))
    rows: list[list[str]] = []

    def fact(label: str, path: str, fmt=_money) -> None:
        rows.append([label, fmt(_cell(doc, path)), _reason(doc, path), _source(doc, path)])

    fact("Revenue, trailing twelve months", "base_year.revenue")
    fact("Operating income, GAAP", "base_year.operating_income_gaap")
    items = get_path(doc, "base_year.one_time_items") or []
    if not items:
        rows.append(["One-time items", "none", DASH, DASH])
    for item in items:
        if isinstance(item, dict):
            rows.append([f"One-time item: {_text(item.get('name'))}", _money(item.get("value")),
                         _text(item.get("reason")), _text(item.get("source"))])
    fact("Amortization of acquired intangibles (memo)", "base_year.amortization_of_acquired_intangibles")
    fact("Stock-based compensation (memo)", "base_year.stock_based_compensation")
    fact("Research and development expense (memo)", "base_year.rnd_expense")
    fact("Effective tax rate", "base_year.effective_tax_rate", _pct)
    fact("Invested capital", "base_year.invested_capital")
    sw = doc.get("switches") or {}
    hist = sw.get("rnd_history")
    switch_rows = [
        ["Add back amortization of acquired intangibles", _yes(sw.get("addback_acquired_amortization", False))],
        ["Treat research spending as an investment", _yes(sw.get("capitalize_rnd", False))],
        ["Years over which research spending is written off", _text(sw.get("rnd_amortization_years", 5))],
        ["Research spending history, oldest first (USD millions)",
         " / ".join(_money(x) for x in hist) if isinstance(hist, list) and hist else DASH],
        ["Reinvestment lag", f"{sw.get('reinvestment_lag', 1)} year" + ("" if sw.get("reinvestment_lag", 1) == 1 else "s")],
    ]
    return (f"## 3. Base year ({period})\n\n" + table(["Item", "USD millions", "Reason", "Source"], rows)
            + _details(doc, "base_year")
            + "\n\n### Switches\n\nThese stay off unless the owner turns them on for a specific company.\n\n"
            + table(["Switch", "Setting"], switch_rows))


def bridge(doc: dict[str, Any]) -> str:
    rows: list[list[str]] = []

    def fact(label: str, path: str, fmt=_money) -> None:
        rows.append([label, fmt(_cell(doc, path)), _reason(doc, path), _source(doc, path)])

    fact("Cash and marketable securities (added)", "bridge.cash_and_marketable_securities")
    for item in get_path(doc, "bridge.non_operating_assets") or []:
        if isinstance(item, dict):
            rows.append([f"Non-operating asset (added): {_text(item.get('name'))}", _money(item.get("value")),
                         _text(item.get("reason")), _text(item.get("source"))])
    fact("Debt (subtracted)", "bridge.debt")
    fact("Operating lease liabilities (subtracted)", "bridge.operating_lease_liabilities")
    fact("Minority interests (subtracted)", "bridge.minority_interests")
    for item in get_path(doc, "bridge.other_claims") or []:
        if isinstance(item, dict):
            rows.append([f"Other claim (subtracted): {_text(item.get('name'))}", _money(item.get("value")),
                         _text(item.get("reason")), _text(item.get("source"))])
    fact("Probability of failure", "bridge.probability_of_failure", _pct)
    fact("What the assets would fetch in a failure", "bridge.distress_proceeds")
    rows.append(["Diluted shares (millions)", _num(_cell(doc, "bridge.diluted_shares"), 1),
                 _reason(doc, "bridge.diluted_shares"), _source(doc, "bridge.diluted_shares")])
    out = ("## 4. Bridge from operating assets to equity\n\n" + table(["Item", "USD millions", "Reason", "Source"], rows)
           + _details(doc, "bridge"))
    note = get_path(doc, "bridge.dilution_note")
    if note:
        out += f"\n\nDilution note: {_esc(note)}"
    return out


def market(doc: dict[str, Any]) -> str:
    m = doc.get("market") or {}
    meanings = {
        "price": ("Price (USD per share)", "fetched from Yahoo at compute time", lambda x: _num(x, 2)),
        "risk_free_rate": ("Risk-free rate", "latest ten-year Treasury yield from FRED at compute time", lambda x: _pct(x, 2)),
        "equity_risk_premium": ("Equity risk premium", "latest row of Damodaran's cached monthly dataset", lambda x: _pct(x, 2)),
    }
    rows = []
    for key, (label, auto_text, fmt) in meanings.items():
        x = m.get(key)
        if x == "auto":
            rows.append([label, "auto", auto_text])
        else:
            rows.append([label, fmt(x), "written in the file; used as given"])
    rows.append(["Mature-market equity risk premium", _pct(m.get("mature_market_erp"), 2), "used for the terminal cost of capital"])
    rows.append(["Marginal tax rate", _pct(m.get("marginal_tax_rate")), "used in the cost of capital build"])
    return "## 5. Market inputs\n\n" + table(["Item", "Value in the file", "Meaning"], rows)


def cost_of_capital(doc: dict[str, Any]) -> str:
    coc = doc.get("cost_of_capital") or {}
    rows: list[list[str]] = [["Method", _text(coc.get("method")), DASH, DASH]]
    if coc.get("method") == "pinned" or coc.get("pinned_value") is not None:
        rows.append(["Pinned cost of capital", _pct(coc.get("pinned_value"), 2), DASH, DASH])
    if isinstance(coc.get("build"), dict):
        for path, label, fmt in (
            ("damodaran_industry", "Damodaran industry", _text),
            ("unlevered_beta", "Unlevered beta", lambda x: _num(x, 3)),
            ("debt_to_equity_market", "Debt to equity (market values)", lambda x: _num(x, 4)),
            ("pretax_cost_of_debt", "Pre-tax cost of debt", lambda x: _pct(x, 2)),
        ):
            p = f"cost_of_capital.build.{path}"
            rows.append([label, fmt(_cell(doc, p)), _reason(doc, p), _source(doc, p)])
    term = coc.get("terminal") or {}
    rows.append(["Terminal cost of capital method", _text(term.get("method", "mature")), _text(term.get("reason")), DASH])
    if term.get("method") == "value" or term.get("value") is not None:
        rows.append(["Terminal cost of capital, given", _pct(term.get("value"), 2), DASH, DASH])
    return ("## 6. Cost of capital inputs\n\n" + table(["Item", "Value", "Reason", "Source"], rows)
            + _details(doc, "cost_of_capital.build"))


def diagnostics(doc: dict[str, Any]) -> str:
    rows = []
    for path, label, fmt in (
        ("final_year_market_size", "Market size in the final forecast year (USD millions)", _money),
        ("historical_revenue_cagr", "Company's own five-year revenue growth per year", _pct),
        ("historical_operating_margin", "Company's own five-year average operating margin", _pct),
    ):
        p = f"diagnostics.{path}"
        rows.append([label, fmt(_cell(doc, p)), _reason(doc, p), _source(doc, p)])
    return "## 7. Inputs for the diagnostics\n\n" + table(["Item", "Value", "Reason", "Source"], rows)


def guidance(doc: dict[str, Any]) -> str:
    items = get_path(doc, "scenarios.management.guidance") or []
    lead = "Everything management has said in numbers or in words, whether or not it was used."
    if not items:
        return "## 8. Management guidance on record\n\n" + lead + "\n\nNone recorded."
    rows = [[_text(g.get("item")), _text(g.get("quote")), _text(g.get("source")), _text(g.get("used_as"))]
            for g in items if isinstance(g, dict)]
    return "## 8. Management guidance on record\n\n" + lead + "\n\n" + table(["Item", "Quote", "Source", "Used as"], rows)


def changelog(doc: dict[str, Any]) -> str | None:
    log = doc.get("changelog")
    if not isinstance(log, list) or not log:
        return None
    rows = [[_text(e.get("at")), f"`{_text(e.get('path'))}`", _raw(e.get("old")), _raw(e.get("new")), _text(e.get("note"))]
            for e in log if isinstance(e, dict)]
    lead = "Every change the owner saved from the app, oldest first. Values are shown as the file holds them."
    return "## 9. Change log\n\n" + lead + "\n\n" + table(["When", "Input", "Before", "After", "Note"], rows)


# --------------------------------------------------------------------------- #
# Entry points
# --------------------------------------------------------------------------- #

def render_assumptions(assumptions: dict[str, Any]) -> str:
    """``assumptions.md`` as a string.  Works on any loaded YAML, valid or not."""
    doc = {k: v for k, v in assumptions.items() if k != "_path"}
    parts = [header(doc), stories(doc), scenario_table(doc), reasons(doc), base_year(doc), bridge(doc),
             market(doc), cost_of_capital(doc), diagnostics(doc), guidance(doc)]
    log = changelog(doc)
    if log:
        parts.append(log)
    return "\n\n".join(p for p in parts if p).rstrip() + "\n"


def write_assumptions_md(yaml_path: str | Path, assumptions: dict[str, Any] | None = None) -> Path:
    """Render the YAML at ``yaml_path`` (or the given dict) to ``assumptions.md`` next to it."""
    yaml_path = Path(yaml_path)
    if assumptions is None:
        from .schema import load_yaml
        assumptions = load_yaml(yaml_path)
    target = yaml_path.parent / "assumptions.md"
    target.write_text(render_assumptions(assumptions), encoding="utf-8")
    return target
