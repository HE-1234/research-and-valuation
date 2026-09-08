"""Shared state, widgets and callbacks for the valuation walk (AGENTS.md section 18.10).

The app is split in three: this module (state model, formatting, plain-language translation of
engine messages, bound widgets, market inputs, save / write / commit callbacks, results table
and charts), :mod:`valuation.app_pages` (one function per page) and ``app.py`` (routing).  No
arithmetic lives in any of them; every number comes from :func:`valuation.compute` or
:mod:`valuation.impact`.

State model: the plain dict the engine reads is the *working copy* in
``st.session_state["working"]``; every widget carries an ``on_change`` callback that writes its
value into the working copy before the page reruns.  ``st.session_state["gen"]`` is a counter
folded into every widget key; bumping it (Start over, Save, company switch, horizon change)
makes every widget re-read its value from the working copy.  ``st.session_state["page"]`` is
the index into the page list; Back and Next only change it.

Owner-facing text rules: the owner never sees dotted paths, YAML keys, ``--set``, option tokens
or spec citations.  :func:`plain_message` translates every engine and validator message,
:func:`describe_path` names any cell in words, and :func:`md` escapes text from the YAML (and
maps stray keys and maths symbols in analysts' reasons to words).

Environment: ``VALUATION_REPO_ROOT`` overrides repository-root discovery (used by tests);
``VALUATION_APP_NO_FETCH=1`` disables market fetching (the cached Damodaran T-bond rate is used).
"""

from __future__ import annotations

import inspect
import io
import math
import os
import re
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any, Callable

import altair as alt
import pandas as pd
import streamlit as st

import valuation
from valuation import EngineError, MarketInputs, SchemaError, datasets, yamlio
from valuation import market as market_mod
from valuation.analysis import Grid
from valuation.cli import run_and_write
from valuation.engine import ValuationResult
from valuation.impact import FACTOR_LABELS, Impact, impact_ranking
from valuation.market import MarketError
from valuation.render_assumptions import write_assumptions_md
from valuation.schema import SCENARIO_NAMES, WEIGHTED_SCENARIOS, get_path, is_riskfree, split_path



def no_fetch() -> bool:
    """Read at call time (not import time) so tests and scripts can set it per run."""
    return os.environ.get("VALUATION_APP_NO_FETCH") == "1"


CASE_LABELS = {"bear": "Bear", "base": "Base", "bull": "Bull", "management": "Management"}
BLUE, BLUE_LIGHT, INK, INK_2, SURFACE = "#2a78d6", "#e8f1fb", "#0b0b0b", "#52514e", "#fcfcfb"
# Streamlit >= 1.49 takes width="stretch"; older releases take use_container_width=True.
_WIDE = ({"width": "stretch"} if "width" in inspect.signature(st.dataframe).parameters
         else {"use_container_width": True})
NA = "n/a"
# option tokens in the YAML -> words on screen
METHOD_WORDS = {"build": "Built from parts", "pinned": "One number"}
METHOD_HELP = ("Built from parts: risk-free rate plus beta times the equity risk premium, blended with the after-tax cost "
               "of debt. One number: a cost of capital typed in as is.")
TERMINAL_METHOD_WORDS = {"mature": "Mature company rate", "hold": "Hold the company's rate", "value": "A number I set"}
TERMINAL_METHOD_HELP = ("Mature company rate: the risk-free rate plus the mature-market premium (Damodaran's default). "
                        "Hold the company's rate: keep the cost of capital built above forever. A number I set: a rate "
                        "typed in.")


# --------------------------------------------------------------------------- #
# Formatting (display only).  One rule per kind: growth, margins, taxes, weights and shares of
# value carry one decimal; market-style rates (risk-free, premiums, betas' products, cost of
# capital, terminal growth) carry two; money is USD millions with separators; per share to the cent.
# --------------------------------------------------------------------------- #

def pct(x: Any, digits: int = 1) -> str:
    return NA if x is None else f"{float(x) * 100:.{digits}f}%"


def pct2(x: Any) -> str:
    return pct(x, 2)


def money(x: Any) -> str:
    return NA if x is None else f"{float(x):,.0f}"


def per_share(x: Any) -> str:
    return NA if x is None else f"{float(x):,.2f}"


def num(x: Any, digits: int = 2) -> str:
    return NA if x is None else f"{float(x):.{digits}f}"


def shares(x: Any) -> str:
    return NA if x is None else f"{float(x):,.1f}"


def raw(x: Any) -> str:
    """A value as the YAML holds it (used only where the file itself is the subject)."""
    if x is None:
        return "null"
    if isinstance(x, bool):
        return "true" if x else "false"
    if isinstance(x, float):
        return f"{x:g}"
    if isinstance(x, list):
        return "[" + ", ".join(raw(v) for v in x) + "]"
    return str(x)


_MD_SPECIAL = "\\$*_`#<>~[]|"
# words for keys, citations and maths symbols that analysts' reasons still carry
_JARGON: list[tuple[re.Pattern[str], str]] = [(re.compile(p), r) for p, r in [
    (r"\bby rule[,;]?\s*\(\s*§\s*18\.\d+\s+rule\s+\d+\s*\)", "by rule"),      # the sentence already says so
    (r"\(\s*§\s*18\.\d+\s+rule\s+\d+\s*\)", "(by rule)"),
    (r"§\s*18\.\d+\s+rule\s+\d+", "the rule"),
    (r"§\s*", "section "),
    (r"\bused_as:\s*not numeric\b", "'not numeric'"),
    (r"\bbase_year\.effective_tax_rate\b", "the base-year effective tax rate"),
    (r"\breinvestment_override\b", "the per-year reinvestment overrides"),
    (r"\bcapitalize_rnd\b", "the research-capitalization switch"),
    (r"\baddback_acquired_amortization\b", "the amortization add-back switch"),
    (r"\bone_time_items\b", "one-time items"),
    (r"\bother_claims\b", "other claims"),
    (r"\bnon_operating_assets\b", "non-operating assets"),
    (r"\bfinal_year_market_size\b", "the final-year market size"),
    (r"\bhistorical_revenue_cagr\b", "the company's own five-year revenue growth"),
    (r"\bhistorical_operating_margin\b", "the company's own five-year operating margin"),
    (r"\ballow_above_riskfree\b", "'Allow growth above the risk-free rate'"),
    (r"\ballow_large_premium\b", "'Allow a premium above 5 points'"),
    (r"\bdilution_note\b", "the dilution note"),
    (r"\bsales_to_capital\b", "sales-to-capital"),
    (r"\brevenue_growth\b", "revenue growth"),
    (r"\boperating_margin\b", "operating margin"),
    (r"\broic_premium\b", "the return-on-capital premium"),
    (r"\bdiluted_shares\b", "diluted shares"),
    (r"which the owner can test with --set", "which the owner can test in the app"),
    (r"\s*--set\s+\S+", ""),
    (r"×", " x "), (r"÷", " / "), (r"−", "-"), (r"→", " to "), (r"≤", "<="), (r"≥", ">="), (r"Σ", "sum"),
    (r"Δ\s*", "change in "),
]]


def md(text: Any) -> str:
    """Escape text from the YAML or the engine so Streamlit's markdown shows it literally.

    Streamlit reads ``$...$`` as a formula and ``*``/``_`` as emphasis; the analysts' reasons
    contain dollar amounts and dotted paths, so every character with a markdown meaning is
    backslash-escaped.  Known YAML keys, spec citations and maths symbols become words first.
    Line breaks are kept as line breaks.
    """
    s = "" if text is None else str(text)
    for pattern, replacement in _JARGON:
        s = pattern.sub(replacement, s)
    s = re.sub(r"  +", " ", s)
    out = []
    for ch in s:
        out.append("\\" + ch if ch in _MD_SPECIAL else ch)
    return "".join(out).replace("\n", "  \n")


def path_list(values: list[Any] | None, fmt: Callable[[Any], str] = pct) -> str:
    if not values:
        return NA
    return " / ".join(fmt(v) for v in values)


# --------------------------------------------------------------------------- #
# Naming cells and translating engine messages into screen language
# --------------------------------------------------------------------------- #

# scenario cell suffix -> (words, kind)
_FIELDS: dict[str, tuple[str, str]] = {
    "weight": ("weight", "pct"), "story": ("story", "text"), "reason": ("reason", "text"),
    "computable": ("computable", "bool"), "detail": ("working notes", "text"),
    "revenue_growth.values": ("revenue growth", "pct"), "operating_margin.values": ("operating margin", "pct"),
    "reinvestment_override.values": ("reinvestment override", "money"),
    "sales_to_capital.value": ("sales-to-capital, years 1-5", "ratio"),
    "sales_to_capital.value_late": ("sales-to-capital, years 6-10", "ratio"),
    "tax_rate.start": ("tax rate, forecast years", "pct"), "tax_rate.terminal": ("tax rate, terminal", "pct"),
    "terminal.growth.value": ("terminal growth", "growth"),
    "terminal.growth.allow_above_riskfree": ("'Allow growth above the risk-free rate'", "bool"),
    "terminal.roic_premium.value": ("terminal return-on-capital premium", "pct2"),
    "terminal.roic_premium.allow_large_premium": ("'Allow a premium above 5 points'", "bool"),
    "cost_of_capital_override": ("cost of capital override", "pct2"),
}
# top-level cell prefix -> (words, kind); longest prefix wins
_TOP: dict[str, tuple[str, str]] = {
    "horizon": ("Forecast years", "int"),
    "base_year.period": ("Base year: period", "text"),
    "base_year.revenue": ("Base year: revenue", "money"),
    "base_year.operating_income_gaap": ("Base year: operating income", "money"),
    "base_year.one_time_items": ("Base year: one-time item", "money"),
    "base_year.amortization_of_acquired_intangibles": ("Base year: amortization of acquired intangibles", "money"),
    "base_year.stock_based_compensation": ("Base year: stock-based compensation", "money"),
    "base_year.rnd_expense": ("Base year: research and development expense", "money"),
    "base_year.effective_tax_rate": ("Base year: effective tax rate", "pct"),
    "base_year.invested_capital": ("Base year: invested capital", "money"),
    "switches.addback_acquired_amortization": ("Switch: add back acquired amortization", "bool"),
    "switches.capitalize_rnd": ("Switch: treat research spending as an investment", "bool"),
    "switches.rnd_amortization_years": ("Switch: years to write research spending off", "int"),
    "switches.rnd_history": ("Switch: research spending history", "list"),
    "switches.reinvestment_lag": ("Switch: reinvestment lag", "int"),
    "bridge.cash_and_marketable_securities": ("Bridge: cash and marketable securities", "money"),
    "bridge.debt": ("Bridge: debt", "money"),
    "bridge.operating_lease_liabilities": ("Bridge: operating lease liabilities", "money"),
    "bridge.non_operating_assets": ("Bridge: non-operating asset", "money"),
    "bridge.minority_interests": ("Bridge: minority interests", "money"),
    "bridge.other_claims": ("Bridge: other claim", "money"),
    "bridge.probability_of_failure": ("Bridge: probability of failure", "pct"),
    "bridge.distress_proceeds": ("Bridge: what the assets would fetch in a failure", "money"),
    "bridge.diluted_shares": ("Bridge: diluted shares (millions)", "shares"),
    "bridge.dilution_note": ("Bridge: dilution note", "text"),
    "market.price": ("Market: price", "per_share"),
    "market.risk_free_rate": ("Market: risk-free rate", "pct2"),
    "market.equity_risk_premium": ("Market: equity risk premium", "pct2"),
    "market.mature_market_erp": ("Market: mature-market equity risk premium", "pct2"),
    "market.marginal_tax_rate": ("Market: marginal tax rate", "pct"),
    "cost_of_capital.method": ("Cost of capital: method", "method"),
    "cost_of_capital.pinned_value": ("Cost of capital: typed rate", "pct2"),
    "cost_of_capital.build.damodaran_industry": ("Cost of capital: Damodaran industry", "text"),
    "cost_of_capital.build.unlevered_beta": ("Cost of capital: unlevered beta", "beta"),
    "cost_of_capital.build.debt_to_equity_market": ("Cost of capital: debt to equity", "ratio4"),
    "cost_of_capital.build.pretax_cost_of_debt": ("Cost of capital: pre-tax cost of debt", "pct2"),
    "cost_of_capital.terminal.method": ("Terminal cost of capital: method", "terminal_method"),
    "cost_of_capital.terminal.value": ("Terminal cost of capital: typed rate", "pct2"),
    "cost_of_capital.terminal.reason": ("Terminal cost of capital: reason", "text"),
    "diagnostics.final_year_market_size": ("Diagnostics: final-year market size", "money"),
    "diagnostics.historical_revenue_cagr": ("Diagnostics: the company's own five-year revenue growth", "pct"),
    "diagnostics.historical_operating_margin": ("Diagnostics: the company's own five-year operating margin", "pct"),
}
_SUFFIX_WORDS = {"reason": "reason", "source": "source", "detail": "working notes", "name": "name"}


def _humanize(path: str) -> str:
    return " ".join(str(p).replace("_", " ") for p in split_path(path)).capitalize()


def describe_path(path: str) -> tuple[str, str]:
    """A cell's dotted path as words the owner recognises, and the kind of value it holds."""
    parts = split_path(path)
    if not parts:
        return path, "text"
    if parts[0] == "scenarios" and len(parts) >= 2:
        case = CASE_LABELS.get(str(parts[1]), str(parts[1]).capitalize()) + " case"
        rest = [str(p) for p in parts[2:]]
        if not rest:
            return case, "text"
        if rest[0] == "guidance":
            n = f" {int(rest[1]) + 1}" if len(rest) > 1 and rest[1].isdigit() else ""
            return f"{case}, guidance item{n}" + (f" {rest[2]}" if len(rest) > 2 else ""), "text"
        for n in (3, 2, 1):
            key = ".".join(rest[:n])
            if key in _FIELDS:
                words, kind = _FIELDS[key]
                tail = rest[n:]
                if tail and tail[0].isdigit():
                    return f"{case}, {words}, Year {int(tail[0]) + 1}", kind
                if tail and tail[0] in _SUFFIX_WORDS:
                    return f"{case}, {words} {_SUFFIX_WORDS[tail[0]]}", "text"
                return f"{case}, {words}", kind
        head = rest[0]
        if head in ("revenue_growth", "operating_margin", "reinvestment_override", "sales_to_capital", "tax_rate"):
            words = _FIELDS.get(f"{head}.values", _FIELDS.get(f"{head}.value", (head.replace("_", " "), "text")))[0]
            suffix = _SUFFIX_WORDS.get(rest[-1], rest[-1]) if len(rest) > 1 else ""
            return f"{case}, {words}" + (f" {suffix}" if suffix else ""), "text"
        if head == "terminal" and len(rest) > 1:
            words = "terminal growth" if rest[1] == "growth" else "terminal return-on-capital premium"
            suffix = _SUFFIX_WORDS.get(rest[-1], rest[-1]) if len(rest) > 2 else ""
            return f"{case}, {words}" + (f" {suffix}" if suffix else ""), "text"
        return f"{case}, {' '.join(rest).replace('_', ' ')}", "text"
    for n in range(len(parts), 0, -1):
        key = ".".join(str(p) for p in parts[:n])
        if key in _TOP:
            words, kind = _TOP[key]
            tail = [str(p) for p in parts[n:]]
            if tail and tail[0].isdigit():                       # a named item in a list
                words = f"{words} {int(tail[0]) + 1}"
                tail = tail[1:]
            if tail and tail[0] in _SUFFIX_WORDS:
                return f"{words} {_SUFFIX_WORDS[tail[0]]}", "text"
            if tail and tail[0] != "value":
                return f"{words} {' '.join(tail).replace('_', ' ')}", "text"
            return words, kind
    return _humanize(path), "text"


def show_value(value: Any, kind: str) -> str:
    """A cell value the way the pages show it."""
    if value is None or value == yamlio.ABSENT:
        return "empty"
    if kind == "growth":
        return "equal to the risk-free rate" if is_riskfree(value) else pct(value, 2)
    if kind == "bool":
        return "on" if value else "off"
    if kind == "method":
        return METHOD_WORDS.get(str(value), str(value))
    if kind == "terminal_method":
        return TERMINAL_METHOD_WORDS.get(str(value), str(value))
    if isinstance(value, list):
        return ", ".join(show_value(v, kind) for v in value)
    if isinstance(value, str):
        text = value.strip().replace("\n", " ")
        return text if len(text) <= 90 else text[:87] + "..."
    try:
        if kind == "pct":
            return pct(value)
        if kind == "pct2":
            return pct(value, 2)
        if kind == "money":
            return money(value)
        if kind == "ratio":
            return num(value, 2)
        if kind == "ratio4":
            return num(value, 4)
        if kind == "beta":
            return num(value, 3)
        if kind == "shares":
            return shares(value)
        if kind == "per_share":
            return per_share(value)
        if kind == "int":
            return str(int(value))
    except (TypeError, ValueError):
        pass
    return str(value)


def _case(name: str) -> str:
    return CASE_LABELS.get(name, name.capitalize()) + " case"


def _rate(text: str, digits: int = 2) -> str:
    try:
        return pct(float(text), digits)
    except ValueError:
        return text


_TICK_ABOVE = "tick 'Allow growth above the risk-free rate' on the Terminal value page or lower the number"
_TICK_PREMIUM = "tick 'Allow a premium above 5 points' on the Terminal value page or lower it"
_RULES: list[tuple[re.Pattern[str], Callable[[re.Match[str]], str]]] = [(re.compile(p), f) for p, f in [
    (r"\s*\((?:section\s*)?§?\s*18\.\d+(?:\s+rule\s+\d+)?\)", lambda m: ""),
    (r";?\s*pass --set \S+(?: or write a (?:number|decimal) in assumptions\.yaml)?", lambda m: "; type a value on the Start page"),
    (r"scenarios\.\*\.weight: bear \+ base \+ bull must sum to 1, got ([\d.]+)",
     lambda m: f"the weights add up to {_rate(m.group(1), 0)}; they must add up to 100% (Taxes and weights page)"),
    (r"scenarios\.(\w+)\.terminal\.growth\.value: ([\d.]+) is above the risk-free rate ([\d.]+); set allow_above_riskfree: true and give a reason",
     lambda m: f"{_case(m.group(1))}: terminal growth {_rate(m.group(2))} is above the risk-free rate {_rate(m.group(3))}; {_TICK_ABOVE}"),
    (r"(\w+): terminal growth ([\d.]+) is above the risk-free rate ([\d.]+) \(allow_above_riskfree is true; reason: (.*?)\)",
     lambda m: f"{_case(m.group(1))}: terminal growth {_rate(m.group(2))} is above the risk-free rate {_rate(m.group(3))}, allowed with the reason: {m.group(4)}"),
    (r"(\w+): terminal cost of capital ([\d.]+) must exceed terminal growth ([\d.]+)",
     lambda m: f"{_case(m.group(1))}: the terminal cost of capital {_rate(m.group(2))} must be above terminal growth {_rate(m.group(3))}; lower the growth or raise the terminal cost of capital"),
    (r"(\w+): terminal ROIC (-?[\d.]+) must be positive",
     lambda m: f"{_case(m.group(1))}: the terminal return on capital ({_rate(m.group(2))}) must be positive; raise the premium"),
    (r"(\w+): terminal ROIC premium ([\d.]+) is above 0\.05 \(allow_large_premium is true; reason: (.*?)\)",
     lambda m: f"{_case(m.group(1))}: the terminal return-on-capital premium {_rate(m.group(2))} is above 5 points, allowed with the reason: {m.group(3)}"),
    (r"(\S+)\.value: ([\d.]+) is above 0\.05; set allow_large_premium: true and give a reason",
     lambda m: f"{describe_path(m.group(1) + '.value')[0]} {_rate(m.group(2))} is above 5 points; {_TICK_PREMIUM}"),
    (r"(\w+): cost of capital pinned to ([\d.]+) by cost_of_capital_override.*",
     lambda m: f"{_case(m.group(1))} discounts at its own rate of {_rate(m.group(2))} instead of the shared cost of capital"),
    (r"(\S+): rates are decimals \(0\.12, not 12\); got (\S+)",
     lambda m: f"{describe_path(m.group(1))[0]}: a rate must be below 100%; got {m.group(2)}"),
    (r"(\S+)\.values: expected (\d+) entries \(horizon \d+\), got (\d+)",
     lambda m: f"{describe_path(m.group(1) + '.values')[0]} needs {m.group(2)} yearly values and has {m.group(3)}"),
    (r"(\S+): expected a number, got (.*)", lambda m: f"{describe_path(m.group(1))[0]}: expected a number, got {m.group(2)}"),
    (r"(\S+): must be >= ([-\d.]+), got ([-\d.]+)",
     lambda m: f"{describe_path(m.group(1))[0]} must be at least {m.group(2)}; it is {m.group(3)}"),
    (r"(\S+): must be <= ([-\d.]+), got ([-\d.]+)",
     lambda m: f"{describe_path(m.group(1))[0]} must be at most {m.group(2)}; it is {m.group(3)}"),
    (r"(\S+): must be positive", lambda m: f"{describe_path(m.group(1))[0]} must be positive"),
    (r"(\S+) is null(?:; the engine .*)?", lambda m: f"{describe_path(m.group(1))[0]} is empty"),
    (r"(\S+): required (?:number|string|decimal).*", lambda m: f"{describe_path(m.group(1))[0]} is missing"),
    (r"(\S+): missing", lambda m: f"{describe_path(m.group(1))[0]} is missing"),
    (r"(\S+): no reason given", lambda m: f"{describe_path(m.group(1))[0]}: no reason given"),
    (r"^(bear|base|bull|management) scenario not computed: ", lambda m: f"{_case(m.group(1))} not computed: "),
    (r"^(bear|base|bull|management) scenario skipped: ", lambda m: f"{_case(m.group(1))} not computed: "),
    (r"^no scenario could be computed: ", lambda m: "No case could be computed: "),
    (r"market\.(price|risk_free_rate|equity_risk_premium) is a manual value \(([-\d.]+)\) from assumptions\.yaml or --set, not fetched",
     lambda m: f"{describe_path('market.' + m.group(1))[0]} is a value written in the assumptions file "
               f"({show_value(float(m.group(2)), describe_path('market.' + m.group(1))[1])}), not fetched"),
    (r"(Price|Risk-free rate|Equity risk premium) \([^)]*\) is a manual value \(([-\d.]+)\) typed in the app, not fetched",
     lambda m: f"{m.group(1)} is a value typed in the app ({per_share(float(m.group(2))) if m.group(1) == 'Price' else pct(float(m.group(2)), 2)}), not fetched"),
    (r"\b(?:scenarios|base_year|bridge|cost_of_capital|market|diagnostics|switches)\.[\w.]*\w",
     lambda m: describe_path(m.group(0))[0]),
    (r"\bset allow_above_riskfree: true\b", lambda m: _TICK_ABOVE),
    (r"\bset allow_large_premium: true\b", lambda m: _TICK_PREMIUM),
    (r"\ballow_above_riskfree\b", lambda m: "'Allow growth above the risk-free rate'"),
    (r"\ballow_large_premium\b", lambda m: "'Allow a premium above 5 points'"),
    (r"§\s*", lambda m: "section "),
]]


def plain_message(text: str) -> str:
    """One engine or validator message in screen language: cases named, rates as percentages,
    checkbox names quoted, no dotted paths, no ``--set``, no spec citations."""
    s = " ".join(str(text).split())
    for pattern, repl in _RULES:
        s = pattern.sub(repl, s)
    for pattern, replacement in _JARGON:                   # keys and symbols inside free text (skip reasons)
        s = pattern.sub(replacement, s)
    s = " ".join(s.split()).strip().rstrip(";").strip()
    return s[:1].upper() + s[1:] if s else s


def plain_messages(text: str) -> list[str]:
    return [plain_message(line) for line in str(text).splitlines() if line.strip()]


# --------------------------------------------------------------------------- #
# Repository and session state
# --------------------------------------------------------------------------- #

def repo_root() -> Path:
    env = os.environ.get("VALUATION_REPO_ROOT")
    return Path(env).resolve() if env else valuation.find_repo_root()


def company_tickers(root: Path) -> list[str]:
    return sorted(p.parent.parent.name for p in root.glob("companies/*/valuation/assumptions.yaml"))


def yaml_path(root: Path, ticker: str) -> Path:
    return root / "companies" / ticker / "valuation" / "assumptions.yaml"


def working() -> dict[str, Any]:
    return st.session_state["working"]


def key(path: str) -> str:
    return f"w{st.session_state.get('gen', 0)}:{path}"


def bump_gen() -> None:
    st.session_state["gen"] = st.session_state.get("gen", 0) + 1


def load_company(root: Path, ticker: str, *, reset_walk: bool = False) -> None:
    """(Re)load the working copy from disk.  ``reset_walk`` also returns to Start."""
    path = yaml_path(root, ticker)
    doc = valuation.load(path)
    st.session_state["ticker"] = ticker
    st.session_state["path"] = path
    st.session_state["working"] = doc
    st.session_state["rt"] = yamlio.load_roundtrip(path)
    st.session_state["input_errors"] = {}
    st.session_state["load_seq"] = st.session_state.get("load_seq", 0) + 1
    for k in ("horizon_note", "ranking", "ranking_key", "baseline"):
        st.session_state.pop(k, None)
    if reset_walk:
        st.session_state["page"] = 0
        st.session_state["visited"] = {0}
        st.session_state.pop("confirm_restart", None)
    bump_gen()


def horizon(doc: dict[str, Any]) -> int:
    return int(doc.get("horizon", 5)) if doc.get("horizon") in (5, 10) else 5


def set_in(doc: Any, path: str, value: Any) -> None:
    """Set a dotted path in place, creating intermediate mappings; list indices must exist."""
    parts = split_path(path)
    node = doc
    for i, part in enumerate(parts[:-1]):
        nxt = parts[i + 1]
        if isinstance(node, list):
            node = node[part]
        else:
            if node.get(part) is None:
                node[part] = [] if isinstance(nxt, int) else {}
            node = node[part]
    node[parts[-1]] = value


def _sync(k: str, path: str, convert: Callable[[Any], Any]) -> None:
    """on_change callback: copy a widget's value into the working copy (runs before the rerun)."""
    errors = st.session_state.setdefault("input_errors", {})
    try:
        value = convert(st.session_state.get(k))
    except ValueError as exc:
        errors[path] = str(exc)
        return
    errors.pop(path, None)
    set_in(working(), path, value)


def _to_float(x: Any) -> float | None:
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return None
    return float(x)


def _to_int(x: Any) -> int | None:
    return None if x is None else int(x)


def _to_text(x: Any) -> str | None:
    text = (x or "").strip()
    return text or None


def _to_story(x: Any) -> str:
    return (x or "").rstrip() + "\n" if (x or "").strip() else ""


def _pct_to_dec(x: Any) -> float | None:
    """A box showing 12.0 (percent) stores 0.12; rounding removes float noise from the division."""
    f = _to_float(x)
    return None if f is None else round(f / 100.0, 10)


def dec_to_pct(x: Any) -> float | None:
    return None if x is None else round(float(x) * 100.0, 6)


# --------------------------------------------------------------------------- #
# Bound widgets
# --------------------------------------------------------------------------- #

def w_pct(doc: dict[str, Any], path: str, label: str, *, container=None, digits: int = 2, step: float = 1.0,
          help: str | None = None, placeholder: str = "empty") -> None:
    """A rate stored as a decimal, entered as a percentage ("12.0" means 0.12)."""
    c = container or st
    k = key(path)
    c.number_input(label, value=dec_to_pct(get_path(doc, path)), step=step, format=f"%.{digits}f", key=k,
                   on_change=_sync, args=(k, path, _pct_to_dec), help=help, placeholder=placeholder)


def w_number(doc: dict[str, Any], path: str, label: str, *, fmt: str = "%.2f", step: float = 0.1, container=None,
             help: str | None = None, placeholder: str = "empty") -> None:
    c = container or st
    cur = get_path(doc, path)
    k = key(path)
    if fmt == "%d":
        c.number_input(label, value=None if cur is None else int(cur), step=1, format=fmt, key=k,
                       on_change=_sync, args=(k, path, _to_int), help=help, placeholder=placeholder)
    else:
        c.number_input(label, value=None if cur is None else float(cur), step=step, format=fmt, key=k,
                       on_change=_sync, args=(k, path, _to_float), help=help, placeholder=placeholder)


def w_text(doc: dict[str, Any], path: str, label: str, *, height: int = 100, container=None,
           convert: Callable[[Any], Any] = _to_text, label_visibility: str = "visible") -> None:
    c = container or st
    k = key(path)
    c.text_area(label, value=get_path(doc, path) or "", key=k, height=height, on_change=_sync,
                args=(k, path, convert), label_visibility=label_visibility)


def w_line(doc: dict[str, Any], path: str, label: str, *, container=None) -> None:
    c = container or st
    k = key(path)
    c.text_input(label, value=get_path(doc, path) or "", key=k, on_change=_sync, args=(k, path, _to_text))


def w_bool(doc: dict[str, Any], path: str, label: str, *, container=None, help: str | None = None) -> None:
    c = container or st
    k = key(path)
    c.checkbox(label, value=bool(get_path(doc, path)), key=k, on_change=_sync, args=(k, path, bool), help=help)


def w_choice(doc: dict[str, Any], path: str, label: str, options: list[str], *, words: dict[str, str] | None = None,
             container=None, help: str | None = None) -> None:
    """A select box whose options are stored as YAML tokens but shown as words."""
    c = container or st
    k = key(path)
    cur = get_path(doc, path)
    index = options.index(cur) if cur in options else 0
    c.selectbox(label, options, index=index, key=k, on_change=_sync, args=(k, path, str), help=help,
                format_func=lambda o: (words or {}).get(o, o))


def _riskfree_cb(k: str, path: str, rf: float) -> None:
    """The 'equal to the risk-free rate' checkbox: on writes the word, off writes the current rate."""
    if st.session_state.get(k):
        set_in(working(), path, "riskfree")
    else:
        set_in(working(), path, round(rf, 6))
    bump_gen()


def w_terminal_growth(doc: dict[str, Any], path: str, rf: float, *, container=None) -> None:
    """Terminal growth: a checkbox for ``riskfree``; unchecked reveals a percentage box."""
    c = container or st
    cur = get_path(doc, path)
    k = key(path + "#riskfree")
    c.checkbox(f"Equal to the risk-free rate ({pct(rf, 2)})", value=is_riskfree(cur), key=k,
               on_change=_riskfree_cb, args=(k, path, rf),
               help="Damodaran's default: growth forever equals the risk-free rate used in this run.")
    if not is_riskfree(cur):
        w_pct(doc, path, "Terminal growth (%), forever", container=c, step=0.25)


def year_boxes(doc: dict[str, Any], path: str, T: int, *, percent: bool = True, fmt: str = "%.1f",
               step: float = 10.0, placeholder: str = "empty") -> None:
    """Number boxes labelled Year 1..Year T bound to ``path.values.<i>``: rows of five for percentages, rows
    of three for money (six-digit figures need the width at laptop sizes)."""
    values = get_path(doc, f"{path}.values")
    if not isinstance(values, list) or len(values) != T:
        values = (list(values) if isinstance(values, list) else []) + [None] * T
        set_in(doc, f"{path}.values", values[:T])
    per_row = 5 if percent else 3
    for start in range(0, T, per_row):
        cols = st.columns(per_row)
        for t, c in zip(range(start, min(start + per_row, T)), cols):
            p = f"{path}.values.{t}"
            label = f"Year {t + 1}" + (" (%)" if percent else "")
            if percent:
                w_pct(doc, p, label, container=c, placeholder=placeholder)
            else:
                w_number(doc, p, label, fmt=fmt, step=step, container=c, placeholder=placeholder)


def reason_block(doc: dict[str, Any], cell_path: str, *, container=None, title: str | None = None) -> None:
    """The analyst's reason in full as normal text, the working notes (``detail``) in a fold-out, the
    source tags in small text (only when the cell has a source)."""
    c = container or st
    node = get_path(doc, cell_path)
    if not isinstance(node, dict):
        return
    reason = node.get("reason")
    if title:
        c.markdown(f"**{title}**")
    c.markdown(md(reason) if reason else "*No reason given.*")
    detail = node.get("detail")
    if detail:
        with c.expander("Working notes"):
            working_notes(detail)
    source = node.get("source")
    if source:
        c.caption("Source: " + md(source))


def detail_blocks(text: str) -> list[tuple[str, Any]]:
    """Split working notes into blocks: ("table", DataFrame) for pipe tables, ("code", text) for
    whitespace-aligned columns, ("text", text) otherwise.  Markdown would collapse the spacing of a
    table typed with spaces, so those are shown preformatted."""
    out: list[tuple[str, Any]] = []
    for block in re.split(r"\n\s*\n", str(text).strip()):
        lines = [ln.rstrip() for ln in block.splitlines() if ln.strip()]
        if not lines:
            continue
        piped = [ln for ln in lines if ln.count("|") >= 2]
        if len(piped) >= 2 and len(piped) >= len(lines) - 1:
            rows = []
            for ln in piped:
                cells = [c.strip() for c in ln.strip().strip("|").split("|")]
                if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                    continue                                     # the markdown separator line
                rows.append(cells)
            if len(rows) >= 2:
                width = max(len(r) for r in rows)
                rows = [(r + [""] * width)[:width] for r in rows]           # ragged rows padded to the widest
                header = dedupe_columns([h or f"col {i + 1}" for i, h in enumerate(rows[0])])
                out.append(("table", pd.DataFrame(rows[1:], columns=header)))
                continue
        aligned = [ln for ln in lines if re.search(r"\S {2,}\S", ln)]
        if len(lines) >= 2 and len(aligned) * 2 >= len(lines):
            out.append(("code", "\n".join(lines)))
            continue
        out.append(("text", block))
    return out


def working_notes(text: str) -> None:
    """Render a cell's ``detail``: tables as tables, aligned columns preformatted, prose as prose.  Whatever the
    analyst typed, the page keeps rendering: any block that cannot be shown its intended way falls back to a
    preformatted copy of the raw text."""
    try:
        blocks = detail_blocks(text)
    except Exception:                                          # noqa: BLE001
        st.code(str(text), language=None)
        return
    for kind, payload in blocks:
        try:
            if kind == "table":
                static_table(payload)
            elif kind == "code":
                st.code(payload, language=None)
            else:
                st.markdown(md(payload))
        except Exception:                                      # noqa: BLE001
            st.code(payload if isinstance(payload, str) else payload.to_string(index=False), language=None)


# --------------------------------------------------------------------------- #
# Market inputs
# --------------------------------------------------------------------------- #

@st.cache_data(ttl=900, show_spinner="Fetching the price, the risk-free rate and the equity risk premium...")
def fetch_market(ticker: str, price_cell: Any, rf_cell: Any, erp_cell: Any, no_fetch: bool) -> dict[str, Any]:
    """Fetch (or take from the YAML) the three market inputs; never raises."""
    out: dict[str, Any] = {}

    def manual(name: str, cell: Any, label: str) -> bool:
        if isinstance(cell, (int, float)) and not isinstance(cell, bool):
            out[name] = {"value": float(cell), "date": None, "source": f"{label} written in the assumptions file",
                         "error": None, "note": None}
            return True
        return False

    if not manual("price", price_cell, "price"):
        if no_fetch:
            out["price"] = {"value": None, "date": None, "source": None, "error": "fetching is off", "note": None}
        else:
            try:
                p, d = market_mod.fetch_price(ticker)
                out["price"] = {"value": p, "date": d, "source": "Yahoo Finance, latest trade", "error": None, "note": None}
            except MarketError as exc:
                out["price"] = {"value": None, "date": None, "source": None, "error": str(exc), "note": None}
    if not manual("rf", rf_cell, "risk-free rate"):
        # FRED with a 20 s timeout and one retry; if unreachable (or fetching is off) the cached Damodaran
        # T-bond rate, labelled as such, so the walk never waits for a typed rate
        try:
            got = market_mod.risk_free_with_fallback(fetch=not no_fetch)
            source = "FRED, ten-year Treasury yield" if got.source == "FRED DGS10" else got.source
            out["rf"] = {"value": got.rate, "date": got.date, "source": source, "error": None, "note": got.note}
        except MarketError as exc:
            out["rf"] = {"value": None, "date": None, "source": None, "error": str(exc), "note": None}
    if not manual("erp", erp_cell, "equity risk premium"):
        try:
            row = datasets.latest_erp()
            out["erp"] = {"value": row.erp, "date": row.date, "source": "Damodaran's monthly premium dataset (cached)",
                          "error": None, "note": None}
        except datasets.DatasetError as exc:
            out["erp"] = {"value": None, "date": None, "source": None, "error": str(exc), "note": None}
    return out


MARKET_SPECS = [("price", "Price (USD per share)", "%.2f", 0.5, per_share),
                ("rf", "Risk-free rate (%)", "%.2f", 0.05, pct2),
                ("erp", "Equity risk premium (%)", "%.2f", 0.05, pct2)]


def _market_values(ticker: str) -> dict[str, float | None]:
    """The owner's market values for this company (fetched value unless overridden), kept in session state
    so they survive pages on which the boxes are not drawn."""
    store = st.session_state.setdefault("market_values", {})
    return store.setdefault(ticker, {})


def _market_cb(ticker: str, name: str, k: str) -> None:
    v = st.session_state.get(k)
    if v is None:
        _market_values(ticker)[name] = None
    else:
        _market_values(ticker)[name] = float(v) if name == "price" else round(float(v) / 100.0, 10)


def market_inputs(doc: dict[str, Any], ticker: str) -> MarketInputs | None:
    """The three market inputs as the engine needs them, without drawing anything."""
    m = doc.get("market") or {}
    fetched = fetch_market(ticker, m.get("price"), m.get("risk_free_rate"), m.get("equity_risk_premium"), no_fetch())
    values = _market_values(ticker)
    for name, *_ in MARKET_SPECS:
        if name not in values:
            values[name] = fetched[name]["value"]
    if any(values[name] is None for name, *_ in MARKET_SPECS):
        return None
    warnings, sources, dates = [], {}, {}
    for name, label, _fmt, _step, show in MARKET_SPECS:
        f = fetched[name]
        if f["value"] is not None and abs(f["value"] - values[name]) < 1e-9:
            sources[name], dates[name] = f["source"], f["date"]
            if f.get("note"):
                warnings.append(f["note"])
        else:
            sources[name], dates[name] = "typed in the app", datetime.now().strftime("%Y-%m-%d")
            warnings.append(f"{label.split(' (')[0]} is a value typed in the app ({show(values[name])}), not fetched")
    return MarketInputs(price=values["price"], risk_free_rate=values["rf"], equity_risk_premium=values["erp"],
                        price_date=dates["price"], risk_free_date=dates["rf"], erp_date=dates["erp"],
                        price_source=sources["price"] or "", risk_free_source=sources["rf"] or "",
                        erp_source=sources["erp"] or "", warnings=warnings)


def market_boxes(doc: dict[str, Any], ticker: str) -> None:
    """The Start page's market block: three aligned columns, each a label, a box, then the fetched value
    with its date and source in small text (and a note when a fallback was used)."""
    m = doc.get("market") or {}
    fetched = fetch_market(ticker, m.get("price"), m.get("risk_free_rate"), m.get("equity_risk_premium"), no_fetch())
    values = _market_values(ticker)
    cols = st.columns(3)
    for (name, label, fmt, step, show), c in zip(MARKET_SPECS, cols):
        f = fetched[name]
        with c:
            cur = values.get(name, f["value"])
            shown = None if cur is None else (cur if name == "price" else dec_to_pct(cur))
            k = f"mkt:{ticker}:{name}"
            st.number_input(label, value=shown, step=step, format=fmt, key=k, on_change=_market_cb,
                            args=(ticker, name, k), placeholder="type a value")
            if f["error"]:
                st.caption(f"Could not be fetched ({md(f['error'])}). Type a value above.")
            else:
                when = f" on {f['date']}" if f["date"] else ""
                st.caption(f"Fetched: {show(f['value'])}{when}. Source: {md(f['source'])}.")
                if f.get("note"):
                    st.caption("Note: FRED was unreachable, so this is the T-bond rate on the latest row of the cached "
                               "Damodaran dataset. Type a rate above to override it." if "FRED" in f["note"]
                               else "Note: fetching is off, so this is the T-bond rate on the latest row of the cached "
                                    "Damodaran dataset. Type a rate above to override it.")
    if any(values.get(name, fetched[name]["value"]) is None for name, *_ in MARKET_SPECS):
        st.error("The model needs a price, a risk-free rate and an equity risk premium. Fill in the empty boxes.")


# --------------------------------------------------------------------------- #
# Horizon
# --------------------------------------------------------------------------- #

def resize_horizon(doc: dict[str, Any], T: int) -> str:
    """Set ``horizon`` and pad or cut every per-year list; returns a note for the owner."""
    old = int(doc.get("horizon", 5))
    doc["horizon"] = T
    for name, sc in (doc.get("scenarios") or {}).items():
        if not isinstance(sc, dict):
            continue
        for k in ("revenue_growth", "operating_margin", "reinvestment_override"):
            node = sc.get(k)
            if not isinstance(node, dict) or not isinstance(node.get("values"), list):
                continue
            values = list(node["values"])
            if len(values) < T:
                filler = None if k == "reinvestment_override" or not values else values[-1]
                values += [filler] * (T - len(values))
            node["values"] = values[:T]
    if T > old:
        return (f"Horizon set to {T} years. Every per-year list was extended from {old} to {T} entries by repeating "
                "its last value (reinvestment overrides get empty cells). Edit years 6-10 on the factor pages.")
    return f"Horizon set to {T} years. Per-year lists were cut to their first {T} entries."


def _horizon_cb(k: str) -> None:
    T = int(st.session_state[k])
    doc = working()
    if T != int(doc.get("horizon", 5)):
        st.session_state["horizon_note"] = resize_horizon(doc, T)
        bump_gen()


def horizon_control(doc: dict[str, Any]) -> None:
    cur = horizon(doc)
    k = key("horizon")
    st.radio("Forecast years before the terminal value", [5, 10], index=[5, 10].index(cur), horizontal=True, key=k,
             on_change=_horizon_cb, args=(k,),
             help="Five years is the default; the 10-year-fade reference is always shown next to it.")
    note = st.session_state.get("horizon_note")
    if note:
        st.info(note)


# --------------------------------------------------------------------------- #
# Compute and ranking
# --------------------------------------------------------------------------- #

def compute_result(doc: dict[str, Any], market: MarketInputs | None) -> tuple[ValuationResult | None, str | None]:
    """The engine's result, or a plain-language sentence saying why there is none."""
    if market is None:
        return None, "the market inputs on the Start page are incomplete"
    try:
        return valuation.compute(doc, market=market, fetch=False), None
    except SchemaError as exc:
        return None, "; ".join(plain_messages(str(exc)))
    except (EngineError, MarketError) as exc:
        return None, plain_message(str(exc))
    except Exception as exc:                                   # noqa: BLE001 - never show a traceback
        return None, f"the engine could not compute ({type(exc).__name__}: {plain_message(str(exc))})"


def ranking_for(doc: dict[str, Any], market: MarketInputs | None) -> tuple[list[Impact] | None, str | None]:
    """The factor ranking, computed once per load (and per market change) and kept in session state."""
    if market is None:
        return None, "the market inputs above are incomplete"
    k = (st.session_state.get("ticker"), st.session_state.get("load_seq"), market.price, market.risk_free_rate,
         market.equity_risk_premium)
    if st.session_state.get("ranking_key") == k:
        return st.session_state.get("ranking"), st.session_state.get("ranking_error")
    ranking, error = None, None
    try:
        ranking = impact_ranking(doc, market)
    except (SchemaError, EngineError) as exc:
        error = "; ".join(plain_messages(str(exc)))
    except Exception as exc:                                   # noqa: BLE001
        error = f"{type(exc).__name__}: {plain_message(str(exc))}"
    st.session_state["ranking"], st.session_state["ranking_error"], st.session_state["ranking_key"] = ranking, error, k
    return ranking, error


def ranking_table(ranking: list[Impact]) -> pd.DataFrame:
    """One row per factor page (the larger of a page's nudges), largest impact first."""
    best: dict[str, Impact] = {}
    for i in ranking:
        page = "terminal" if i.factor == "terminal_roic" else i.factor
        size = abs(i.change) if i.change is not None else -1.0
        cur = best.get(page)
        cur_size = abs(cur.change) if cur is not None and cur.change is not None else -1.0
        if cur is None or size > cur_size:
            best[page] = i
    rows = []
    for page, i in sorted(best.items(), key=lambda kv: -(abs(kv[1].change) if kv[1].change is not None else -1.0)):
        change = f"{i.change:+,.2f}" if i.change is not None else f"not computed: {plain_message(i.note or '')}"
        rows.append({"Factor": FACTOR_LABELS.get(page, i.label), "What we nudged": i.nudge,
                     "Change in base value per share (USD)": change})
    return pd.DataFrame(rows)


# --------------------------------------------------------------------------- #
# Save, write, commit
# --------------------------------------------------------------------------- #

def file_changed_on_disk(path: Path) -> bool:
    """True when the assumptions file no longer matches the snapshot taken at load (an agent redraft, a save
    from another session); the working copy must then be reloaded before anything is saved."""
    rt = st.session_state.get("rt")
    return rt is not None and not rt.snapshot.matches(Path(path))


STALE_BANNER = ("The assumptions file changed on disk since you loaded it. Start over to reload; Save is disabled "
                "until then, and the differences below are not listed because they are not your changes.")


def unsaved_changes(doc: dict[str, Any], path: Path) -> list[yamlio.Change]:
    try:
        return yamlio.diff_against_file(path, doc)
    except OSError as exc:
        st.error(f"Cannot read {path}: {md(str(exc))}")
        return []


def changes_table(diff: list[yamlio.Change]) -> pd.DataFrame:
    """Unsaved changes labelled in words, values as the pages show them."""
    rows = []
    for c in diff:
        label, kind = describe_path(c.path)
        rows.append({"Input": label, "In the file": show_value(c.file_value, kind), "Now": show_value(c.current_value, kind)})
    return pd.DataFrame(rows, columns=["Input", "In the file", "Now"])


def _save_cb(root: Path, ticker: str, path: Path, note_key: str) -> None:
    doc = working()
    diff = yamlio.diff_against_file(path, doc)
    if not diff:
        st.session_state["flash"] = "Nothing to save: the working copy matches the file."
        return
    note = (st.session_state.get(note_key) or "").strip() or None
    rt = st.session_state["rt"]
    try:
        changed = yamlio.apply_changes(rt, yamlio.changes_from_diff(diff))
        now = datetime.now().replace(microsecond=0).isoformat()
        yamlio.append_changelog(rt, [{"at": now, "path": p, "old": o, "new": n, "note": note} for p, o, n in changed])
        yamlio.set_owner_edited(rt, now)
        yamlio.save(rt)
    except yamlio.StaleFileError as exc:
        st.session_state["flash_error"] = (f"Save refused: {md(str(exc))} Use Start over to reload the file, "
                                           "then redo your edits.")
        return
    except (yamlio.PathError, ValueError, OSError) as exc:
        st.session_state["flash_error"] = f"Could not save: {md(str(exc))}"
        return
    md_path = write_assumptions_md(path)
    load_company(root, ticker)
    st.session_state["flash"] = (f"Saved {len(changed)} change(s) to {path.name} with changelog entries"
                                 f"{' (note: ' + md(note) + ')' if note else ''} and rewrote {md_path.name}.")


def _write_cb(path: Path) -> None:
    doc = working()
    if yamlio.diff_against_file(path, doc):
        st.session_state["flash_error"] = ("Write valuation.md refused: there are unsaved changes. Save them (or start "
                                           "over) first, so the report always matches the assumptions file.")
        return
    market = st.session_state.get("market_inputs")
    if market is None:
        st.session_state["flash_error"] = "Write valuation.md refused: the market inputs on the Start page are incomplete."
        return
    buf = io.StringIO()
    try:
        run_and_write(path, doc, market=market, fetch=False, out=buf)
    except (SchemaError, EngineError, MarketError) as exc:
        st.session_state["flash_error"] = "Write valuation.md failed: " + "; ".join(plain_messages(str(exc)))
        return
    st.session_state["last_output"] = buf.getvalue()
    st.session_state["flash"] = f"Wrote {path.parent / 'valuation.md'} and assumptions.md (previous pair archived to history/)."


def _git(root: Path, args: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=str(root), capture_output=True, text=True, check=False)


def pending_commit(root: Path, ticker: str) -> tuple[list[str], str | None]:
    """Files under companies/<T>/valuation that a Commit would record, and the message it would use."""
    rel = f"companies/{ticker}/valuation"
    status = _git(root, ["status", "--porcelain", "--", rel])
    if status.returncode != 0:
        return [], None
    files: list[str] = []
    for line in status.stdout.splitlines():
        entry = line[3:].strip()
        if entry.endswith("/"):
            files += [str(p.relative_to(root)) for p in (root / entry).rglob("*") if p.is_file()]
        else:
            files.append(entry)
    if not files:
        return [], None
    only_yaml = all(Path(f).name in ("assumptions.yaml", "assumptions.md") for f in files)
    if only_yaml:
        message = f"value({ticker}): owner edits to assumptions"
    else:
        history = root / rel / "history"
        n = (sum(1 for p in history.iterdir() if p.is_dir()) if history.exists() else 0) + 1
        message = f"value({ticker}): compute {working().get('as_of_quarter')} rev {n}"
    return files, message


def _commit_cb(root: Path, ticker: str) -> None:
    rel = f"companies/{ticker}/valuation"
    files, message = pending_commit(root, ticker)
    if message is None:
        status = _git(root, ["status", "--porcelain", "--", rel])
        if status.returncode != 0:
            st.session_state["git_output"] = status.stdout + status.stderr
            st.session_state["flash_error"] = "git status failed; see the output below."
            return
        st.session_state["flash"] = f"Nothing to commit under {rel}."
        return
    add = _git(root, ["add", "--", rel])
    commit = _git(root, ["-c", "user.name=company-research", "-c", "user.email=research@localhost",
                         "commit", "-m", message])
    output = "\n".join(x for x in (add.stdout, add.stderr, commit.stdout, commit.stderr) if x.strip())
    st.session_state["git_output"] = f"$ git add -- {rel}\n$ git commit -m \"{message}\"\n{output}"
    if commit.returncode == 0:
        st.session_state["flash"] = f"Committed: {message}"
    else:
        st.session_state["flash_error"] = "git commit failed; see the output below."


def _restart_cb(root: Path, ticker: str) -> None:
    load_company(root, ticker, reset_walk=True)
    st.session_state["flash"] = "Working copy reloaded from the file on disk. Back at Start."


# --------------------------------------------------------------------------- #
# Results table and charts
# --------------------------------------------------------------------------- #

RESULT_COLUMNS = ["Case", "Weight", "Value per share", "Price", "Upside / downside", "Terminal-value share",
                  "10-year-fade per share", "Operating assets", "Enterprise value", "Equity value"]


def results_table(result: ValuationResult) -> pd.DataFrame:
    """The section 18.5 results table: one row per case plus the weighted row (money in USD millions)."""
    doc = result.assumptions
    rows = []
    for name in SCENARIO_NAMES:
        if name not in (doc.get("scenarios") or {}):
            continue
        weight = get_path(doc, f"scenarios.{name}.weight")
        wtxt = "not weighted" if name == "management" else pct(weight, 0)
        sc = result.scenarios.get(name)
        if sc is None:
            rows.append({"Case": CASE_LABELS[name], "Weight": wtxt, "Value per share": "not computed"})
            continue
        fade = sc.fade_reference.per_share if sc.fade_reference else None
        rows.append({"Case": CASE_LABELS[name], "Weight": wtxt, "Value per share": per_share(sc.per_share),
                     "Price": per_share(sc.price), "Upside / downside": pct(sc.upside),
                     "Terminal-value share": pct(sc.terminal_share), "10-year-fade per share": per_share(fade),
                     "Operating assets": money(sc.operating_assets), "Enterprise value": money(sc.enterprise_value),
                     "Equity value": money(sc.equity)})
    if result.weighted:
        w = result.weighted
        rows.append({"Case": "Weighted expected", "Weight": "100%", "Value per share": per_share(w.per_share),
                     "Price": per_share(result.market.price), "Upside / downside": pct(w.upside),
                     "Terminal-value share": pct(w.terminal_share), "10-year-fade per share": per_share(w.fade_per_share),
                     "Operating assets": money(w.operating_assets), "Enterprise value": money(w.enterprise_value),
                     "Equity value": money(w.equity)})
    else:
        rows.append({"Case": "Weighted expected", "Weight": "", "Value per share": "not computed"})
    return pd.DataFrame(rows, columns=RESULT_COLUMNS).fillna("")


def result_notes(result: ValuationResult) -> list[str]:
    """One plain sentence per case that is not computed (its reason) and per case warning."""
    doc = result.assumptions
    notes = []
    for name in SCENARIO_NAMES:
        if name not in (doc.get("scenarios") or {}):
            continue
        sc = result.scenarios.get(name)
        if sc is None:
            if name in result.stopped:
                notes.append(stop_sentence(name, "; ".join(result.stopped[name])))
            else:
                notes.append(MANAGEMENT_SKIPPED if name == "management" else f"{CASE_LABELS[name]} case not computed.")
        else:
            notes += [plain_message(w) for w in sc.warnings]
    if not result.weighted:
        notes.append("Weighted expected value not computed because a weighted case is missing.")
    return notes


def stop_sentence(name: str, why: str, lead: str = "not computed") -> str:
    """'Bull case not computed: terminal growth ...' without repeating the case name when the engine's message
    already starts with '<Case> case:'; one sentence, ending with a full stop."""
    text = plain_message(why)
    text = re.sub(rf"^{re.escape(CASE_LABELS[name])} case:\s*", "", text).rstrip(".")
    return f"{CASE_LABELS[name]} case {lead}: {text}."


def dedupe_columns(names: list[Any]) -> list[str]:
    """Column names made unique ("Ratio", "Ratio (2)", ...): st.table refuses duplicate names."""
    seen: dict[str, int] = {}
    out: list[str] = []
    for raw_name in names:
        name = str(raw_name).strip() or "column"
        seen[name] = seen.get(name, 0) + 1
        out.append(name if seen[name] == 1 else f"{name} ({seen[name]})")
    return out


MANAGEMENT_SKIPPED = ("Management case not computed; its reason and the guidance on record are on the Revenue growth "
                      "page.")


def warning_sentence(text: str) -> str:
    """A warning line as the owner reads it: stopped cases through stop_sentence, the skipped management case
    through the same pointer sentence the Results notes use, everything else through plain_message."""
    m = re.match(r"^(bear|base|bull|management) scenario not computed: (.*)$", str(text).strip(), re.S)
    if m:
        return stop_sentence(m.group(1), m.group(2))
    m = re.match(r"^(bear|base|bull|management) scenario skipped: ", str(text).strip())
    if m:
        return MANAGEMENT_SKIPPED if m.group(1) == "management" else f"{CASE_LABELS[m.group(1)]} case not computed."
    return plain_message(text)


def static_table(df: pd.DataFrame) -> None:
    """A read-only table that wraps long text and never scrolls; every cell is escaped so markdown shows it
    literally.  Content can never crash the page: duplicate column names are made unique and anything the
    table widget still refuses is shown as a preformatted block instead."""
    try:
        shown = df.copy()
        shown.columns = dedupe_columns(list(shown.columns))
        st.table(shown.astype(str).map(md), hide_index=True)
    except Exception:                                          # noqa: BLE001 - owner content must never raise
        st.code(df.to_string(index=False), language=None)


def value_chart(result: ValuationResult) -> alt.LayerChart | None:
    data = []
    for name in WEIGHTED_SCENARIOS:
        sc = result.scenarios.get(name)
        if sc is not None:
            fade = sc.fade_reference.per_share if sc.fade_reference else None
            data.append({"case": CASE_LABELS[name], "value": sc.per_share, "fade": fade,
                         "value_label": per_share(sc.per_share),
                         "fade_label": f"10-year fade {per_share(fade)}" if fade is not None else ""})
    if result.weighted:
        w = result.weighted
        data.append({"case": "Weighted", "value": w.per_share, "fade": w.fade_per_share, "value_label": per_share(w.per_share),
                     "fade_label": f"10-year fade {per_share(w.fade_per_share)}"})
    if not data:
        return None
    for d in data:
        d["zero"] = 0.0
    df = pd.DataFrame(data)
    order = [d["case"] for d in data]
    price = result.market.price
    base = alt.Chart(df).encode(x=alt.X("case:N", sort=order, title=None, axis=alt.Axis(labelAngle=0, labelFontSize=13)))
    bars = base.mark_bar(color=BLUE, cornerRadiusTopLeft=4, cornerRadiusTopRight=4, size=140).encode(
        y=alt.Y("value:Q", title="Value per share (USD)"),
        tooltip=[alt.Tooltip("case:N", title="Case"), alt.Tooltip("value:Q", title="Value per share", format=",.2f"),
                 alt.Tooltip("fade:Q", title="10-year-fade reference", format=",.2f")])
    # the value per share sits just inside the top of each bar (white on blue, so it never crosses the dashed
    # price line); a bar too short for that carries it above; the 10-year-fade reference is a lighter label
    # inside the foot of a bar tall enough to hold both
    top = max(max(d["value"] for d in data), price)
    tall = alt.datum.value > 0.18 * top
    values_in = base.transform_filter(tall).mark_text(baseline="top", dy=8, color="#ffffff", fontSize=14,
                                                      fontWeight="bold").encode(y="value:Q", text="value_label:N")
    values_out = base.transform_filter(~tall).mark_text(baseline="bottom", dy=-6, color=INK, fontSize=14,
                                                        fontWeight="bold").encode(y="value:Q", text="value_label:N")
    values = values_in + values_out
    fades = base.transform_filter(tall).mark_text(baseline="bottom", dy=-8, color=BLUE_LIGHT, fontSize=12).encode(
        y="zero:Q", text="fade_label:N")
    rule_df = pd.DataFrame({"price": [price], "text": [f"price {per_share(price)}"]})
    rule = alt.Chart(rule_df).mark_rule(color=INK, strokeDash=[6, 4], size=2).encode(y="price:Q")
    rule_text = alt.Chart(rule_df).mark_text(align="right", baseline="bottom", dx=-4, dy=-4, color=INK, fontSize=12).encode(
        y="price:Q", text="text:N", x=alt.value("width"))
    return (bars + values + fades + rule + rule_text).properties(height=340, title="Value per share by case, against the price")


def heatmap(grid: Grid) -> alt.LayerChart:
    # cost of capital and terminal growth axes carry two decimals; growth and margin axes one
    digits = 2 if "capital" in grid.row_label.lower() else 1
    rows = []
    for i, rv in enumerate(grid.row_values):
        for j, cv in enumerate(grid.col_values):
            cell = grid.cells[i][j]
            rows.append({"row": pct(rv, digits), "col": pct(cv, digits), "value": cell,
                         "label": per_share(cell) if cell is not None else NA,
                         "base": i == grid.base_row and j == grid.base_col})
    df = pd.DataFrame(rows)
    row_order = [pct(v, digits) for v in grid.row_values]
    col_order = [pct(v, digits) for v in grid.col_values]
    values = [r["value"] for r in rows if r["value"] is not None]
    mid = (min(values) + max(values)) / 2 if values else 0
    base = alt.Chart(df).encode(x=alt.X("col:N", sort=col_order, title=grid.col_label, axis=alt.Axis(labelAngle=0)),
                                y=alt.Y("row:N", sort=row_order, title=grid.row_label))
    rects = base.mark_rect(stroke=SURFACE, strokeWidth=2).encode(
        color=alt.Color("value:Q", scale=alt.Scale(range=[BLUE_LIGHT, BLUE]), title="USD per share"),
        tooltip=[alt.Tooltip("row:N", title=grid.row_label), alt.Tooltip("col:N", title=grid.col_label),
                 alt.Tooltip("value:Q", title="Value per share", format=",.2f")])
    text = base.mark_text(fontSize=12).encode(
        text="label:N", color=alt.condition(alt.datum.value > mid, alt.value("#ffffff"), alt.value(INK)))
    marker = base.transform_filter(alt.datum.base).mark_rect(fill=None, stroke=INK, strokeWidth=3)
    return (rects + text + marker).properties(height=280, title=grid.title)


# --------------------------------------------------------------------------- #
# The live readout line
# --------------------------------------------------------------------------- #

def baseline_values(result: ValuationResult | None) -> dict[str, float]:
    """Per-share values as loaded, remembered on the first successful compute after a load."""
    if "baseline" not in st.session_state and result is not None:
        base = {n: sc.per_share for n, sc in result.scenarios.items()}
        if result.weighted:
            base["weighted"] = result.weighted.per_share
        st.session_state["baseline"] = base
    return st.session_state.get("baseline", {})


def _with_reference(label: str, value: float, loaded: float | None) -> str:
    if loaded is not None and abs(value - loaded) > 0.005:
        return f"{label} {per_share(value)} (as loaded {per_share(loaded)})"
    return f"{label} {per_share(value)}"


def readout_line(result: ValuationResult | None, error: str | None, market: MarketInputs | None) -> str:
    """One plain sentence: the value per share for every case with the current inputs, or why there is none."""
    if result is None:
        return f"Not computed: {error or 'the model has no result'}."
    loaded = baseline_values(result)
    parts = []
    for name in WEIGHTED_SCENARIOS:
        sc = result.scenarios.get(name)
        if sc is not None:
            parts.append(_with_reference(CASE_LABELS[name], sc.per_share, loaded.get(name)))
        else:
            parts.append(f"{CASE_LABELS[name]} not computed (see its box)")
    if "management" in result.scenarios:
        parts.append(_with_reference("Management", result.scenarios["management"].per_share, loaded.get("management")))
    if result.weighted:
        parts.append(_with_reference("Weighted", result.weighted.per_share, loaded.get("weighted")))
    else:
        parts.append("Weighted not computed")
    price = f", against a price of {per_share(market.price)}" if market is not None else ""
    return "With your current inputs: " + " / ".join(parts) + " per share" + price + "."
