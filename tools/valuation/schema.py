"""Load and validate ``assumptions.yaml`` exactly as AGENTS.md section 18.4 defines it.

Two kinds of findings come out of :func:`validate`:

* **errors** are structural (wrong type, wrong list length, weights that do
  not sum to one, a rate written as a percent).  They stop everything.
* **nulls in required cells** are allowed by the schema but stop only the
  scenario they belong to.  Nulls in shared cells (base year, bridge, cost of
  capital) stop every scenario.  Both are reported with the dotted path.

``management.computable: false`` skips the management scenario without any
error.
"""

from __future__ import annotations

import copy
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

SCENARIO_NAMES = ("bear", "base", "bull", "management")
WEIGHTED_SCENARIOS = ("bear", "base", "bull")
LARGE_PREMIUM = 0.05
WEIGHT_TOLERANCE = 1e-6
HORIZONS = (5, 10)
RISKFREE = "riskfree"          # terminal.growth.value may be this string: "equal to the run's risk-free rate"

TOP_LEVEL_KEYS = {
    "schema", "ticker", "company", "as_of_quarter", "as_of_date", "drafted",
    "currency", "units", "horizon", "base_year", "switches", "bridge", "market",
    "cost_of_capital", "diagnostics", "scenarios",
    "owner_edited", "changelog",   # maintained by the app (section 18.4); never read by the engine
    "sources",                     # optional: [{tag, file, date, note}] mapping source tags to cached files
}
SCENARIO_KEYS = {
    "weight", "story", "revenue_growth", "operating_margin", "sales_to_capital",
    "reinvestment_override", "tax_rate", "cost_of_capital_override", "terminal",
    "computable", "reason", "guidance", "detail",
}
# Any input cell ({value, reason, source}) may also carry `detail`: the working notes behind a short
# reason (section 18.4).  Cells are never checked for unknown keys, so `detail` is accepted silently.
# Optional diagnostics cells beyond section 18.4 (see README): the company's own
# history, which section 18.5 item 9 compares against and nothing else supplies.
DIAGNOSTIC_KEYS = {
    "final_year_market_size", "historical_revenue_cagr", "historical_operating_margin",
}


class SchemaError(Exception):
    """Raised when the assumptions document has structural errors."""


@dataclass
class Validation:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    shared_nulls: list[str] = field(default_factory=list)
    stopped: dict[str, list[str]] = field(default_factory=dict)
    skipped: dict[str, str] = field(default_factory=dict)

    @property
    def ok(self) -> bool:
        return not self.errors

    def stop(self, scenario: str, reason: str) -> None:
        self.stopped.setdefault(scenario, []).append(reason)

    def computable_scenarios(self) -> list[str]:
        """Scenario names that will compute if no engine error occurs."""
        if self.shared_nulls:
            return []
        return [
            n for n in SCENARIO_NAMES
            if n not in self.stopped and n not in self.skipped and n in self._present
        ]

    _present: tuple[str, ...] = ()


# --------------------------------------------------------------------------- #
# Loading and dotted-path access
# --------------------------------------------------------------------------- #

def load_yaml(path: str | Path) -> dict[str, Any]:
    with open(path, encoding="utf-8") as fh:
        doc = yaml.safe_load(fh)
    if not isinstance(doc, dict):
        raise SchemaError(f"{path}: top level must be a mapping")
    return doc


def split_path(path: str) -> list[str | int]:
    parts: list[str | int] = []
    for part in path.split("."):
        parts.append(int(part) if part.isdigit() else part)
    return parts


def get_path(doc: Any, path: str, default: Any = None) -> Any:
    node = doc
    for part in split_path(path):
        try:
            node = node[part]
        except (KeyError, IndexError, TypeError):
            return default
    return node


def coerce_scalar(text: str) -> Any:
    """Turn a ``--set`` value into null, bool, int, float, or string."""
    low = text.strip().lower()
    if low in {"null", "none", "~", ""}:
        return None
    if low == "true":
        return True
    if low == "false":
        return False
    try:
        return int(text)
    except ValueError:
        pass
    try:
        return float(text)
    except ValueError:
        return text.strip()


def set_path(doc: dict[str, Any], path: str, value: Any) -> dict[str, Any]:
    """Return a deep copy of ``doc`` with ``path`` set to ``value``.

    Intermediate mappings are created when missing; list indices must exist.
    """
    out = copy.deepcopy(doc)
    node: Any = out
    parts = split_path(path)
    for i, part in enumerate(parts[:-1]):
        nxt = parts[i + 1]
        if isinstance(node, list):
            if not isinstance(part, int) or part >= len(node):
                raise SchemaError(f"--set {path}: list index {part!r} out of range")
            node = node[part]
        else:
            if part not in node or node[part] is None:
                node[part] = [] if isinstance(nxt, int) else {}
            node = node[part]
    last = parts[-1]
    if isinstance(node, list):
        if not isinstance(last, int) or last >= len(node):
            raise SchemaError(f"--set {path}: list index {last!r} out of range")
        node[last] = value
    elif isinstance(node, dict):
        node[last] = value
    else:
        raise SchemaError(f"--set {path}: cannot set a key on a scalar")
    return out


# --------------------------------------------------------------------------- #
# Validation helpers
# --------------------------------------------------------------------------- #

def _is_number(x: Any) -> bool:
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def _mapping(v: Validation, doc: Any, path: str) -> dict[str, Any] | None:
    node = get_path(doc, path)
    if node is None:
        v.errors.append(f"{path}: missing")
        return None
    if not isinstance(node, dict):
        v.errors.append(f"{path}: must be a mapping")
        return None
    return node


def _cell_value(v: Validation, doc: Any, path: str, *, key: str = "value") -> Any:
    """Return ``path.value`` (or ``path.values``); errors if the cell is not a mapping."""
    node = get_path(doc, path)
    if node is None:
        v.errors.append(f"{path}: missing")
        return None
    if not isinstance(node, dict):
        v.errors.append(f"{path}: an input cell must be a mapping with `{key}` and `reason`")
        return None
    if key not in node:
        v.errors.append(f"{path}.{key}: missing")
        return None
    return node[key]


def _check_number(v: Validation, path: str, x: Any, *, lo: float | None = None,
                  hi: float | None = None, rate: bool = False) -> float | None:
    """Type-check a number.  Returns the float, or None when null or invalid."""
    if x is None:
        return None
    if not _is_number(x):
        v.errors.append(f"{path}: expected a number, got {x!r}")
        return None
    x = float(x)
    if rate and abs(x) >= 1.0:
        v.errors.append(f"{path}: rates are decimals (0.12, not 12); got {x}")
        return None
    if lo is not None and x < lo:
        v.errors.append(f"{path}: must be >= {lo}, got {x}")
        return None
    if hi is not None and x > hi:
        v.errors.append(f"{path}: must be <= {hi}, got {x}")
        return None
    return x


def _require(v: Validation, path: str, x: Any, scenario: str | None) -> None:
    """Record a null in a required cell as a stop (scenario) or shared null."""
    if x is None:
        if scenario is None:
            v.shared_nulls.append(path)
        else:
            v.stop(scenario, f"{path} is null")


def _check_reason(v: Validation, doc: Any, path: str) -> None:
    node = get_path(doc, path)
    if isinstance(node, dict) and not node.get("reason"):
        v.warnings.append(f"{path}: no reason given")


def _check_list_of_items(v: Validation, doc: Any, path: str) -> float:
    """Named-item lists (one-time items, non-operating assets, other claims). Returns the sum."""
    items = get_path(doc, path)
    if items is None:
        return 0.0
    if not isinstance(items, list):
        v.errors.append(f"{path}: must be a list")
        return 0.0
    total = 0.0
    for i, item in enumerate(items):
        if not isinstance(item, dict):
            v.errors.append(f"{path}.{i}: must be a mapping with name and value")
            continue
        if not item.get("name"):
            v.warnings.append(f"{path}.{i}: no name")
        val = _check_number(v, f"{path}.{i}.value", item.get("value"))
        if val is None and item.get("value") is None:
            v.shared_nulls.append(f"{path}.{i}.value")
        total += val or 0.0
    return total


# --------------------------------------------------------------------------- #
# Section checks
# --------------------------------------------------------------------------- #

def _check_top(v: Validation, doc: dict[str, Any]) -> None:
    for key in doc:
        if key not in TOP_LEVEL_KEYS:
            v.warnings.append(f"{key}: unknown top-level key (ignored)")
    if doc.get("schema") != 1:
        v.errors.append(f"schema: expected 1, got {doc.get('schema')!r}")
    for key in ("ticker", "company", "as_of_quarter"):
        if not isinstance(doc.get(key), str) or not doc.get(key):
            v.errors.append(f"{key}: required string")
    if doc.get("currency", "USD") != "USD":
        v.warnings.append(f"currency: engine formats money as USD; got {doc.get('currency')!r}")
    if doc.get("units", "millions") != "millions":
        v.errors.append(f"units: must be 'millions', got {doc.get('units')!r}")
    horizon = doc.get("horizon", 5)
    if horizon not in HORIZONS:
        v.errors.append(f"horizon: must be 5 or 10, got {horizon!r}")


def _check_base_year(v: Validation, doc: dict[str, Any]) -> None:
    if _mapping(v, doc, "base_year") is None:
        return
    for key in ("revenue", "operating_income_gaap"):
        x = _check_number(v, f"base_year.{key}.value", _cell_value(v, doc, f"base_year.{key}"))
        _require(v, f"base_year.{key}.value", x, None)
    tax = _check_number(v, "base_year.effective_tax_rate.value",
                        _cell_value(v, doc, "base_year.effective_tax_rate"), lo=0.0, rate=True)
    _require(v, "base_year.effective_tax_rate.value", tax, None)
    ic = _check_number(v, "base_year.invested_capital.value",
                       _cell_value(v, doc, "base_year.invested_capital"))
    if ic is None and get_path(doc, "base_year.invested_capital.value") is None:
        v.warnings.append("base_year.invested_capital.value is null; the ROIC check will be blank")
    _check_list_of_items(v, doc, "base_year.one_time_items")
    for memo in ("amortization_of_acquired_intangibles", "stock_based_compensation", "rnd_expense"):
        if get_path(doc, f"base_year.{memo}") is not None:
            _check_number(v, f"base_year.{memo}.value", _cell_value(v, doc, f"base_year.{memo}"))


def _check_switches(v: Validation, doc: dict[str, Any]) -> None:
    sw = get_path(doc, "switches")
    if sw is None:
        return
    if not isinstance(sw, dict):
        v.errors.append("switches: must be a mapping")
        return
    for key in ("addback_acquired_amortization", "capitalize_rnd"):
        if key in sw and not isinstance(sw[key], bool):
            v.errors.append(f"switches.{key}: must be true or false")
    if sw.get("addback_acquired_amortization"):
        v.warnings.append("switches.addback_acquired_amortization is on: acquired-intangible "
                          "amortization is added back to operating income (section 18.4 rule 1 default is off)")
        if get_path(doc, "base_year.amortization_of_acquired_intangibles.value") is None:
            v.shared_nulls.append("base_year.amortization_of_acquired_intangibles.value")
    years = sw.get("rnd_amortization_years", 5)
    if not isinstance(years, int) or isinstance(years, bool) or years < 1 or years > 10:
        v.errors.append(f"switches.rnd_amortization_years: integer 1..10, got {years!r}")
    if sw.get("capitalize_rnd"):
        v.warnings.append("switches.capitalize_rnd is on: R&D is capitalized and amortized "
                          f"over {years} years (section 18.4 rule 1 default is off)")
        hist = sw.get("rnd_history")
        if not isinstance(hist, list) or (isinstance(years, int) and len(hist) < years):
            v.errors.append(f"switches.rnd_history: needs at least {years} entries (oldest first)")
        elif not all(_is_number(x) for x in hist):
            v.errors.append("switches.rnd_history: every entry must be a number")
        if get_path(doc, "base_year.rnd_expense.value") is None:
            v.shared_nulls.append("base_year.rnd_expense.value")
    lag = sw.get("reinvestment_lag", 1)
    if lag not in (0, 1):
        v.errors.append(f"switches.reinvestment_lag: must be 0 or 1, got {lag!r}")
    elif lag == 0:
        v.warnings.append("switches.reinvestment_lag is 0: reinvestment funds the same year's "
                          "growth (section 18.3 default is a one-year lag)")


def _check_bridge(v: Validation, doc: dict[str, Any]) -> None:
    if _mapping(v, doc, "bridge") is None:
        return
    for key in ("cash_and_marketable_securities", "debt", "operating_lease_liabilities",
                "minority_interests"):
        x = _check_number(v, f"bridge.{key}.value", _cell_value(v, doc, f"bridge.{key}"))
        _require(v, f"bridge.{key}.value", x, None)
    _check_list_of_items(v, doc, "bridge.non_operating_assets")
    _check_list_of_items(v, doc, "bridge.other_claims")
    p = _check_number(v, "bridge.probability_of_failure.value",
                      _cell_value(v, doc, "bridge.probability_of_failure"), lo=0.0, hi=1.0)
    if p is None and get_path(doc, "bridge.probability_of_failure.value") is None:
        v.warnings.append("bridge.probability_of_failure.value is null; treated as 0")
    dp = _check_number(v, "bridge.distress_proceeds.value",
                       _cell_value(v, doc, "bridge.distress_proceeds"), lo=0.0)
    if p and p > 0 and dp is None:
        v.shared_nulls.append("bridge.distress_proceeds.value")
    shares = _check_number(v, "bridge.diluted_shares.value",
                           _cell_value(v, doc, "bridge.diluted_shares"))
    _require(v, "bridge.diluted_shares.value", shares, None)
    if shares is not None and shares <= 0:
        v.errors.append("bridge.diluted_shares.value: must be positive")


def _check_market(v: Validation, doc: dict[str, Any]) -> None:
    m = _mapping(v, doc, "market")
    if m is None:
        return
    price = m.get("price")
    if price != "auto" and (_check_number(v, "market.price", price) is None):
        v.errors.append("market.price: 'auto' or a positive number")
    elif price != "auto" and float(price) <= 0:
        v.errors.append("market.price: must be positive")
    for key in ("risk_free_rate", "equity_risk_premium"):
        x = m.get(key)
        if x == "auto":
            continue
        if _check_number(v, f"market.{key}", x, lo=0.0, rate=True) is None:
            v.errors.append(f"market.{key}: 'auto' or a decimal rate")
    for key in ("mature_market_erp", "marginal_tax_rate"):
        x = _check_number(v, f"market.{key}", m.get(key), lo=0.0, rate=True)
        if x is None:
            v.errors.append(f"market.{key}: required decimal rate")


def _check_cost_of_capital(v: Validation, doc: dict[str, Any]) -> None:
    coc = _mapping(v, doc, "cost_of_capital")
    if coc is None:
        return
    method = coc.get("method")
    if method not in ("build", "pinned"):
        v.errors.append(f"cost_of_capital.method: 'build' or 'pinned', got {method!r}")
    if method == "pinned":
        x = _check_number(v, "cost_of_capital.pinned_value", coc.get("pinned_value"), lo=0.0, rate=True)
        if x is None:
            v.errors.append("cost_of_capital.pinned_value: required decimal when method is pinned")
    if method == "build":
        if _mapping(v, doc, "cost_of_capital.build") is not None:
            ind = get_path(doc, "cost_of_capital.build.damodaran_industry.value")
            if ind is not None and not isinstance(ind, str):
                v.errors.append("cost_of_capital.build.damodaran_industry.value: must be a string")
            ub = _check_number(v, "cost_of_capital.build.unlevered_beta.value",
                               _cell_value(v, doc, "cost_of_capital.build.unlevered_beta"), lo=0.0)
            if ub is None and get_path(doc, "cost_of_capital.build.unlevered_beta.value") is None:
                if isinstance(ind, str) and ind.strip():
                    v.warnings.append("cost_of_capital.build.unlevered_beta.value is null; the engine takes the "
                                      f"unlevered beta corrected for cash for '{ind}' from the cached Damodaran "
                                      "betas dataset (section 18.4 rule 3: datasets are the engine's job)")
                else:
                    v.shared_nulls.append("cost_of_capital.build.unlevered_beta.value")
            de = _check_number(v, "cost_of_capital.build.debt_to_equity_market.value",
                               _cell_value(v, doc, "cost_of_capital.build.debt_to_equity_market"), lo=0.0)
            if de is None and get_path(doc, "cost_of_capital.build.debt_to_equity_market.value") is None:
                v.warnings.append("cost_of_capital.build.debt_to_equity_market.value is null; the engine derives "
                                  "it as (debt + operating leases) / (price x diluted shares) at compute time")
            kd = _check_number(v, "cost_of_capital.build.pretax_cost_of_debt.value",
                               _cell_value(v, doc, "cost_of_capital.build.pretax_cost_of_debt"),
                               lo=0.0, rate=True)
            _require(v, "cost_of_capital.build.pretax_cost_of_debt.value", kd, None)
    term = _mapping(v, doc, "cost_of_capital.terminal")
    if term is not None:
        tm = term.get("method", "mature")
        if tm not in ("mature", "hold", "value"):
            v.errors.append(f"cost_of_capital.terminal.method: mature | hold | value, got {tm!r}")
        if tm == "value":
            x = _check_number(v, "cost_of_capital.terminal.value", term.get("value"), lo=0.0, rate=True)
            if x is None:
                v.errors.append("cost_of_capital.terminal.value: required decimal when method is value")
        if tm == "hold":
            v.warnings.append("cost_of_capital.terminal.method is 'hold': the company's own cost of "
                              "capital is kept forever (default is the mature-market rate)")


def _check_sources(v: Validation, doc: dict[str, Any]) -> None:
    """Optional top-level ``sources``: a list of mappings, each with at least ``tag`` and ``file``."""
    src = doc.get("sources")
    if src is None:
        return
    if not isinstance(src, list):
        v.errors.append("sources: must be a list of {tag, file, date, note} entries")
        return
    for i, entry in enumerate(src):
        if not isinstance(entry, dict):
            v.errors.append(f"sources.{i}: must be a mapping with tag and file")
            continue
        for key in ("tag", "file"):
            if not isinstance(entry.get(key), str) or not entry.get(key).strip():
                v.errors.append(f"sources.{i}.{key}: required string")


def _check_diagnostics(v: Validation, doc: dict[str, Any]) -> None:
    diag = get_path(doc, "diagnostics")
    if diag is None:
        return
    if not isinstance(diag, dict):
        v.errors.append("diagnostics: must be a mapping")
        return
    for key in diag:
        if key not in DIAGNOSTIC_KEYS:
            v.warnings.append(f"diagnostics.{key}: unknown key (ignored)")
    if "final_year_market_size" in diag:
        _check_number(v, "diagnostics.final_year_market_size.value",
                      _cell_value(v, doc, "diagnostics.final_year_market_size"), lo=0.0)
    for key in ("historical_revenue_cagr", "historical_operating_margin"):
        if key in diag:
            _check_number(v, f"diagnostics.{key}.value", _cell_value(v, doc, f"diagnostics.{key}"),
                          lo=-5.0, hi=5.0)


def _check_year_list(v: Validation, doc: Any, path: str, horizon: int, scenario: str, *,
                     required: bool, lo: float, hi: float, warn_hi: float | None = None) -> None:
    values = _cell_value(v, doc, path, key="values")
    if values is None:
        if get_path(doc, path) is not None and isinstance(get_path(doc, path), dict):
            return  # error already recorded (missing `values`)
        return
    if not isinstance(values, list):
        v.errors.append(f"{path}.values: must be a list of {horizon} numbers")
        return
    if len(values) != horizon:
        v.errors.append(f"{path}.values: expected {horizon} entries (horizon {horizon}), got {len(values)}")
        return
    for i, x in enumerate(values):
        p = f"{path}.values.{i}"
        if x is None:
            if required:
                v.stop(scenario, f"{p} is null")
            continue
        val = _check_number(v, p, x, lo=lo, hi=hi)
        if val is not None and warn_hi is not None and val >= warn_hi:
            v.warnings.append(f"{p}: {val} is very large for a decimal rate; check it is not a percent")


def is_riskfree(x: Any) -> bool:
    """True when a terminal growth cell says "riskfree" (any letter case)."""
    return isinstance(x, str) and x.strip().lower() == RISKFREE


def terminal_growth_rule(scenario: str, growth: float, risk_free: float,
                         node: dict[str, Any]) -> tuple[str | None, str | None]:
    """Section 18.4 rule 5.  Returns ``(error, warning)``: growth above the risk-free rate is an
    error for that scenario unless ``allow_above_riskfree`` is true, in which case it is a warning."""
    if growth <= risk_free + 1e-12:
        return None, None
    if node.get("allow_above_riskfree"):
        return None, (f"{scenario}: terminal growth {growth:.4f} is above the risk-free rate {risk_free:.4f} "
                      f"(allow_above_riskfree is true; reason: {node.get('reason', '')})")
    return (f"scenarios.{scenario}.terminal.growth.value: {growth:.4f} is above the risk-free rate "
            f"{risk_free:.4f}; set allow_above_riskfree: true and give a reason (section 18.4 rule 5)"), None


def _check_terminal(v: Validation, doc: Any, sp: str, scenario: str) -> None:
    if _mapping(v, doc, f"{sp}.terminal") is None:
        return
    g_path = f"{sp}.terminal.growth"
    raw = _cell_value(v, doc, g_path)
    if is_riskfree(raw):
        g = None
    else:
        g = _check_number(v, f"{g_path}.value", raw, rate=True)
        _require(v, f"{g_path}.value", g, scenario)
    gnode = get_path(doc, g_path) or {}
    if isinstance(gnode, dict):
        flag = gnode.get("allow_above_riskfree", False)
        if not isinstance(flag, bool):
            v.errors.append(f"{g_path}.allow_above_riskfree: must be true or false")
        elif flag and not gnode.get("reason"):
            v.errors.append(f"{g_path}.allow_above_riskfree is true but no reason is given")
        rf = get_path(doc, "market.risk_free_rate")
        if g is not None and _is_number(rf) and isinstance(flag, bool):
            error, warning = terminal_growth_rule(scenario, g, float(rf), gnode)
            if error:
                v.errors.append(error)
            if warning:
                v.warnings.append(warning)
    p_path = f"{sp}.terminal.roic_premium"
    prem = _check_number(v, f"{p_path}.value", _cell_value(v, doc, p_path), rate=True)
    _require(v, f"{p_path}.value", prem, scenario)
    pnode = get_path(doc, p_path) or {}
    if isinstance(pnode, dict) and prem is not None:
        flag = pnode.get("allow_large_premium", False)
        if not isinstance(flag, bool):
            v.errors.append(f"{p_path}.allow_large_premium: must be true or false")
        elif prem > LARGE_PREMIUM and not flag:
            v.errors.append(f"{p_path}.value: {prem} is above {LARGE_PREMIUM}; set allow_large_premium: "
                            "true and give a reason (section 18.4 rule 5)")
        elif prem > LARGE_PREMIUM and flag:
            if not pnode.get("reason"):
                v.errors.append(f"{p_path}.allow_large_premium is true but no reason is given")
            v.warnings.append(f"{scenario}: terminal ROIC premium {prem:.3f} is above {LARGE_PREMIUM} "
                              f"(allow_large_premium is true; reason: {pnode.get('reason', '')})")
        if prem < 0:
            v.warnings.append(f"{p_path}.value: negative premium means terminal ROIC below cost of capital")


def _check_scenario(v: Validation, doc: dict[str, Any], name: str, horizon: int) -> None:
    sp = f"scenarios.{name}"
    s = _mapping(v, doc, sp)
    if s is None:
        return
    for key in s:
        if key not in SCENARIO_KEYS:
            v.warnings.append(f"{sp}.{key}: unknown key (ignored)")
    if name == "management":
        computable = s.get("computable", False)
        if not isinstance(computable, bool):
            v.errors.append(f"{sp}.computable: must be true or false")
            return
        if "weight" in s and s["weight"] not in (None, 0):
            v.errors.append(f"{sp}.weight: the management case is never weighted")
        guidance = s.get("guidance")
        if guidance is not None and not isinstance(guidance, list):
            v.errors.append(f"{sp}.guidance: must be a list")
        if not computable:
            v.skipped[name] = s.get("reason") or "computable: false"
            return
    else:
        w = _check_number(v, f"{sp}.weight", s.get("weight"), lo=0.0, hi=1.0)
        if w is None:
            v.errors.append(f"{sp}.weight: required number between 0 and 1")
    if name != "management" and (not isinstance(s.get("story"), str) or not s.get("story", "").strip()):
        v.warnings.append(f"{sp}.story: missing; the stories section will be blank for this case")
    _check_year_list(v, doc, f"{sp}.revenue_growth", horizon, name, required=True, lo=-0.99, hi=5.0, warn_hi=1.0)
    _check_year_list(v, doc, f"{sp}.operating_margin", horizon, name, required=True, lo=-5.0, hi=0.99)
    if get_path(doc, f"{sp}.reinvestment_override") is not None:
        _check_year_list(v, doc, f"{sp}.reinvestment_override", horizon, name, required=False,
                         lo=-1e9, hi=1e9)
    sc_node = _mapping(v, doc, f"{sp}.sales_to_capital")
    if sc_node is not None:
        for key in ("value", "value_late"):
            x = _check_number(v, f"{sp}.sales_to_capital.{key}", sc_node.get(key))
            _require(v, f"{sp}.sales_to_capital.{key}", x, name)
            if x is not None and x <= 0:
                v.errors.append(f"{sp}.sales_to_capital.{key}: must be positive")
    tax_node = _mapping(v, doc, f"{sp}.tax_rate")
    if tax_node is not None:
        for key in ("start", "terminal"):
            x = _check_number(v, f"{sp}.tax_rate.{key}", tax_node.get(key), lo=0.0, rate=True)
            _require(v, f"{sp}.tax_rate.{key}", x, name)
    override = s.get("cost_of_capital_override")
    if override is not None:
        x = _check_number(v, f"{sp}.cost_of_capital_override", override, lo=0.0, rate=True)
        if x is not None:
            v.warnings.append(f"{name}: cost of capital pinned to {x:.4f} by cost_of_capital_override "
                              "(section 18.4 rule 6: cost of capital is shared unless a reason is given)")
    _check_terminal(v, doc, sp, name)
    for key in ("revenue_growth", "operating_margin", "sales_to_capital", "tax_rate"):
        _check_reason(v, doc, f"{sp}.{key}")


def _check_scenarios(v: Validation, doc: dict[str, Any]) -> None:
    sc = _mapping(v, doc, "scenarios")
    if sc is None:
        return
    horizon = doc.get("horizon", 5)
    if horizon not in HORIZONS:
        horizon = 5
    for name in sc:
        if name not in SCENARIO_NAMES:
            v.errors.append(f"scenarios.{name}: unknown scenario; only bear, base, bull, management")
    for name in WEIGHTED_SCENARIOS:
        if name not in sc:
            v.errors.append(f"scenarios.{name}: missing")
    v._present = tuple(n for n in SCENARIO_NAMES if n in sc)
    for name in v._present:
        _check_scenario(v, doc, name, horizon)
    weights = [get_path(doc, f"scenarios.{n}.weight") for n in WEIGHTED_SCENARIOS]
    if all(_is_number(w) for w in weights):
        total = sum(float(w) for w in weights)
        if abs(total - 1.0) > WEIGHT_TOLERANCE:
            v.errors.append(f"scenarios.*.weight: bear + base + bull must sum to 1, got {total:.6f}")


def validate(doc: Any) -> Validation:
    """Validate a loaded assumptions document.  Never raises."""
    v = Validation()
    if not isinstance(doc, dict):
        v.errors.append("top level must be a mapping")
        return v
    _check_top(v, doc)
    _check_base_year(v, doc)
    _check_switches(v, doc)
    _check_bridge(v, doc)
    _check_market(v, doc)
    _check_cost_of_capital(v, doc)
    _check_diagnostics(v, doc)
    _check_sources(v, doc)
    _check_scenarios(v, doc)
    # de-duplicate while keeping order
    v.shared_nulls = list(dict.fromkeys(v.shared_nulls))
    v.warnings = list(dict.fromkeys(v.warnings))
    return v


def validate_or_raise(doc: Any) -> Validation:
    v = validate(doc)
    if v.errors:
        raise SchemaError("\n".join(v.errors))
    return v
