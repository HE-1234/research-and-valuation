"""The interactive editor for ``assumptions.yaml`` (AGENTS.md section 18.10).

Start it with ``uv run --extra app valuation-app``.  The page is a view and an editor of
one company's ``assumptions.yaml``: every input is shown with its reason and source, every
change recomputes through :func:`valuation.compute`, and **Save** writes the changed cells
back through :mod:`valuation.yamlio` (comments and key order survive) with a ``changelog``
entry per cell, then regenerates ``assumptions.md``.  No arithmetic lives here.

State model: the plain dict the engine reads is the *working copy* in
``st.session_state["working"]``; every widget carries an ``on_change`` callback that writes
its value into the working copy before the page reruns, so the numbers at the top always
reflect the inputs below.  ``st.session_state["gen"]`` is a counter folded into every widget
key; bumping it (Reset, Save, company switch, horizon change) makes every widget re-read its
value from the working copy.

Environment: ``VALUATION_REPO_ROOT`` overrides repository-root discovery (used by tests);
``VALUATION_APP_NO_FETCH=1`` disables market fetching (the sidebar then asks for values).
"""

from __future__ import annotations

import inspect
import io
import math
import os
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
from valuation.market import MarketError
from valuation.render_assumptions import write_assumptions_md
from valuation.schema import SCENARIO_NAMES, WEIGHTED_SCENARIOS, get_path, is_riskfree, split_path

NO_FETCH = os.environ.get("VALUATION_APP_NO_FETCH") == "1"
SCENARIO_LABELS = {"bear": "Bear", "base": "Base", "bull": "Bull", "management": "Management"}
TAB_NAMES = ["Bear", "Base", "Bull", "Management", "Base year & bridge", "Cost of capital", "Sensitivity",
             "Year by year", "Reverse DCF", "Diagnostics", "Warnings"]
# number kinds: (format, step)
KINDS = {
    "rate": ("%.4f", 0.005), "money": ("%.1f", 10.0), "ratio": ("%.2f", 0.1), "ratio4": ("%.4f", 0.005),
    "shares": ("%.1f", 1.0), "beta": ("%.3f", 0.01), "weight": ("%.2f", 0.05), "int": ("%d", 1),
}
BLUE, BLUE_LIGHT, INK, INK_2, SURFACE = "#2a78d6", "#e8f1fb", "#0b0b0b", "#52514e", "#fcfcfb"
# Streamlit >= 1.49 takes width="stretch"; older releases take use_container_width=True.
_WIDE = ({"width": "stretch"} if "width" in inspect.signature(st.dataframe).parameters
         else {"use_container_width": True})


# --------------------------------------------------------------------------- #
# Formatting (display only)
# --------------------------------------------------------------------------- #

def pct(x: Any, digits: int = 1) -> str:
    return "—" if x is None else f"{float(x) * 100:.{digits}f}%"


def money(x: Any) -> str:
    return "—" if x is None else f"{float(x):,.0f}"


def per_share(x: Any) -> str:
    return "—" if x is None else f"{float(x):,.2f}"


def num(x: Any, digits: int = 2) -> str:
    return "—" if x is None else f"{float(x):.{digits}f}"


def raw(x: Any) -> str:
    """A value as the YAML holds it, for the unsaved-changes list."""
    if x is None:
        return "null"
    if isinstance(x, bool):
        return "true" if x else "false"
    if isinstance(x, float):
        return f"{x:g}"
    if isinstance(x, list):
        return "[" + ", ".join(raw(v) for v in x) + "]"
    return str(x)


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


def load_company(root: Path, ticker: str) -> None:
    path = yaml_path(root, ticker)
    doc = valuation.load(path)
    st.session_state["ticker"] = ticker
    st.session_state["path"] = path
    st.session_state["working"] = doc
    st.session_state["rt"] = yamlio.load_roundtrip(path)
    st.session_state["input_errors"] = {}
    st.session_state.pop("horizon_note", None)
    bump_gen()


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


def _to_growth(x: Any) -> Any:
    text = (x or "").strip()
    if not text:
        return None
    if is_riskfree(text):
        return "riskfree"
    try:
        return float(text)
    except ValueError:
        raise ValueError(f"'{text}' is neither a decimal like 0.04 nor the word riskfree") from None


# --------------------------------------------------------------------------- #
# Bound widgets
# --------------------------------------------------------------------------- #

def w_number(doc: dict[str, Any], path: str, label: str, kind: str = "rate", *, help: str | None = None,
             container=None) -> None:
    c = container or st
    cur = get_path(doc, path)
    fmt, step = KINDS[kind]
    k = key(path)
    if kind == "int":
        c.number_input(label, value=None if cur is None else int(cur), step=1, format=fmt, key=k,
                       on_change=_sync, args=(k, path, _to_int), help=help, placeholder="null")
    else:
        c.number_input(label, value=None if cur is None else float(cur), step=step, format=fmt, key=k,
                       on_change=_sync, args=(k, path, _to_float), help=help, placeholder="null")


def w_text(doc: dict[str, Any], path: str, label: str, *, height: int = 100, container=None,
           convert: Callable[[Any], Any] = _to_text) -> None:
    c = container or st
    k = key(path)
    c.text_area(label, value=get_path(doc, path) or "", key=k, height=height, on_change=_sync,
                args=(k, path, convert))


def w_bool(doc: dict[str, Any], path: str, label: str, *, container=None, help: str | None = None) -> None:
    c = container or st
    k = key(path)
    c.checkbox(label, value=bool(get_path(doc, path)), key=k, on_change=_sync, args=(k, path, bool), help=help)


def w_choice(doc: dict[str, Any], path: str, label: str, options: list[str], *, container=None) -> None:
    c = container or st
    k = key(path)
    cur = get_path(doc, path)
    index = options.index(cur) if cur in options else 0
    c.selectbox(label, options, index=index, key=k, on_change=_sync, args=(k, path, str))


def w_growth(doc: dict[str, Any], path: str, container=None) -> None:
    """Terminal growth: the word ``riskfree`` or a decimal."""
    c = container or st
    k = key(path)
    cur = get_path(doc, path)
    shown = "" if cur is None else ("riskfree" if is_riskfree(cur) else f"{float(cur):g}")
    c.text_input("Terminal growth (decimal, or the word riskfree)", value=shown, key=k, on_change=_sync,
                 args=(k, path, _to_growth), placeholder="null")
    err = st.session_state.get("input_errors", {}).get(path)
    if err:
        c.error(err)


def reason_and_source(doc: dict[str, Any], cell_path: str, container=None, *, height: int = 100) -> None:
    c = container or st
    node = get_path(doc, cell_path)
    if not isinstance(node, dict):
        return
    w_text(doc, f"{cell_path}.reason", "Reason", height=height, container=c)
    source = node.get("source")
    c.caption(f"Source: {source}" if source else "Source: none given")


# --------------------------------------------------------------------------- #
# Market inputs
# --------------------------------------------------------------------------- #

@st.cache_data(ttl=900, show_spinner="Fetching price, risk-free rate and equity risk premium...")
def fetch_market(ticker: str, price_cell: Any, rf_cell: Any, erp_cell: Any, no_fetch: bool) -> dict[str, Any]:
    """Fetch (or take from the YAML) the three market inputs; never raises."""
    out: dict[str, Any] = {}

    def manual(name: str, cell: Any, label: str) -> bool:
        if isinstance(cell, (int, float)) and not isinstance(cell, bool):
            out[name] = {"value": float(cell), "date": None, "source": f"{label}: written in assumptions.yaml", "error": None}
            return True
        return False

    if not manual("price", price_cell, "price"):
        if no_fetch:
            out["price"] = {"value": None, "date": None, "source": None, "error": "fetching is off (VALUATION_APP_NO_FETCH)"}
        else:
            try:
                p, d = market_mod.fetch_price(ticker)
                out["price"] = {"value": p, "date": d, "source": "Yahoo chart", "error": None}
            except MarketError as exc:
                out["price"] = {"value": None, "date": None, "source": None, "error": str(exc)}
    if not manual("rf", rf_cell, "risk-free rate"):
        if no_fetch:
            out["rf"] = {"value": None, "date": None, "source": None, "error": "fetching is off (VALUATION_APP_NO_FETCH)"}
        else:
            try:
                r, d = market_mod.fetch_risk_free()
                out["rf"] = {"value": r, "date": d, "source": "FRED DGS10", "error": None}
            except MarketError as exc:
                out["rf"] = {"value": None, "date": None, "source": None, "error": str(exc)}
    if not manual("erp", erp_cell, "equity risk premium"):
        try:
            row = datasets.latest_erp()
            out["erp"] = {"value": row.erp, "date": row.date, "source": "Damodaran ERPbymonth.xlsx, cached", "error": None}
        except datasets.DatasetError as exc:
            out["erp"] = {"value": None, "date": None, "source": None, "error": str(exc)}
    return out


def sidebar_market(doc: dict[str, Any], ticker: str) -> MarketInputs | None:
    m = doc.get("market") or {}
    fetched = fetch_market(ticker, m.get("price"), m.get("risk_free_rate"), m.get("equity_risk_premium"), NO_FETCH)
    sb = st.sidebar
    sb.subheader("Market inputs")
    values: dict[str, float | None] = {}
    specs = [("price", "Price (USD per share)", "%.2f", 0.5, per_share),
             ("rf", "Risk-free rate (decimal)", "%.4f", 0.0005, lambda x: pct(x, 2)),
             ("erp", "Equity risk premium (decimal)", "%.4f", 0.0005, lambda x: pct(x, 2))]
    for name, label, fmt, step, show in specs:
        f = fetched[name]
        if f["error"]:
            sb.warning(f"{label} could not be fetched ({f['error']}). Enter a value below.")
        else:
            sb.caption(f"{label}: {show(f['value'])} — {f['date'] or ''} ({f['source']})")
        values[name] = sb.number_input(label, value=f["value"], step=step, format=fmt, key=f"mkt:{ticker}:{name}",
                                       placeholder="enter a value")
    if any(v is None for v in values.values()):
        sb.error("The model needs a price, a risk-free rate and an equity risk premium. Fill in the empty boxes.")
        return None
    warnings = []
    sources, dates = {}, {}
    for name, label, *_ in specs:
        f = fetched[name]
        if f["value"] is not None and abs(f["value"] - values[name]) < 1e-12:
            sources[name], dates[name] = f["source"], f["date"]
        else:
            sources[name], dates[name] = "override typed in the app", datetime.now().strftime("%Y-%m-%d")
            warnings.append(f"{label} is a manual value ({values[name]:g}) typed in the app, not fetched")
    return MarketInputs(price=values["price"], risk_free_rate=values["rf"], equity_risk_premium=values["erp"],
                        price_date=dates["price"], risk_free_date=dates["rf"], erp_date=dates["erp"],
                        price_source=sources["price"] or "", risk_free_source=sources["rf"] or "",
                        erp_source=sources["erp"] or "", warnings=warnings)


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
                "its last value (reinvestment overrides get empty cells). Edit years 6-10 in the scenario tabs.")
    return f"Horizon set to {T} years. Per-year lists were cut to their first {T} entries."


def _horizon_cb(k: str) -> None:
    T = int(st.session_state[k])
    doc = working()
    if T != int(doc.get("horizon", 5)):
        st.session_state["horizon_note"] = resize_horizon(doc, T)
        bump_gen()


def sidebar_horizon(doc: dict[str, Any]) -> None:
    sb = st.sidebar
    sb.subheader("Horizon")
    cur = int(doc.get("horizon", 5))
    k = key("horizon")
    sb.radio("Explicit years before the terminal value", [5, 10], index=[5, 10].index(cur) if cur in (5, 10) else 0,
             horizontal=True, key=k, on_change=_horizon_cb, args=(k,),
             help="Section 18.2: five years is the default; the 10-year-fade reference is always shown next to it.")
    note = st.session_state.get("horizon_note")
    if note:
        sb.info(note)


# --------------------------------------------------------------------------- #
# Sidebar: changes and actions
# --------------------------------------------------------------------------- #

def unsaved_changes(doc: dict[str, Any], path: Path) -> list[yamlio.Change]:
    try:
        return yamlio.diff_against_file(path, doc)
    except OSError as exc:
        st.sidebar.error(f"Cannot read {path}: {exc}")
        return []


def sidebar_changes(diff: list[yamlio.Change]) -> None:
    sb = st.sidebar
    sb.subheader(f"Unsaved changes ({len(diff)})")
    if not diff:
        sb.caption("None. The working copy matches the file.")
        return
    sb.dataframe(pd.DataFrame([{"path": c.path, "file": raw(c.file_value), "current": raw(c.current_value)} for c in diff]),
                 hide_index=True, **_WIDE)


def _reset_cb(root: Path, ticker: str) -> None:
    load_company(root, ticker)
    st.session_state["flash"] = "Working copy reset to the file on disk."


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
        st.session_state["flash_error"] = f"Save refused: {exc} Use **Reset to file** to reload, then redo your edits."
        return
    except (yamlio.PathError, ValueError, OSError) as exc:
        st.session_state["flash_error"] = f"Could not save: {exc}"
        return
    md = write_assumptions_md(path)
    load_company(root, ticker)
    st.session_state["flash"] = (f"Saved {len(changed)} change(s) to {path.name} with changelog entries"
                                 f"{' (note: ' + note + ')' if note else ''} and rewrote {md.name}.")


def _write_cb(path: Path) -> None:
    doc = working()
    if yamlio.diff_against_file(path, doc):
        st.session_state["flash_error"] = ("Write valuation.md refused: there are unsaved changes. Save them (or reset) "
                                           "first, so valuation.md always matches assumptions.yaml.")
        return
    market = st.session_state.get("market_inputs")
    if market is None:
        st.session_state["flash_error"] = "Write valuation.md refused: the market inputs in the sidebar are incomplete."
        return
    buf = io.StringIO()
    try:
        run_and_write(path, doc, market=market, fetch=False, out=buf)
    except (SchemaError, EngineError, MarketError) as exc:
        st.session_state["flash_error"] = f"Write valuation.md failed: {exc}"
        return
    st.session_state["last_output"] = buf.getvalue()
    st.session_state["flash"] = f"Wrote {path.parent / 'valuation.md'} and assumptions.md (previous pair archived to history/)."


def _git(root: Path, args: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=str(root), capture_output=True, text=True, check=False)


def _commit_cb(root: Path, ticker: str) -> None:
    rel = f"companies/{ticker}/valuation"
    status = _git(root, ["status", "--porcelain", "--", rel])
    if status.returncode != 0:
        st.session_state["git_output"] = status.stdout + status.stderr
        st.session_state["flash_error"] = "git status failed; see the output below."
        return
    files: list[str] = []
    for line in status.stdout.splitlines():
        entry = line[3:].strip()
        if entry.endswith("/"):
            files += [str(p.relative_to(root)) for p in (root / entry).rglob("*") if p.is_file()]
        else:
            files.append(entry)
    if not files:
        st.session_state["flash"] = f"Nothing to commit under {rel}."
        return
    only_yaml = all(Path(f).name in ("assumptions.yaml", "assumptions.md") for f in files)
    if only_yaml:
        message = f"value({ticker}): owner edits to assumptions"
    else:
        history = root / rel / "history"
        n = (sum(1 for p in history.iterdir() if p.is_dir()) if history.exists() else 0) + 1
        message = f"value({ticker}): compute {working().get('as_of_quarter')} rev {n}"
    add = _git(root, ["add", "--", rel])
    commit = _git(root, ["-c", "user.name=company-research", "-c", "user.email=research@localhost",
                         "commit", "-m", message])
    output = "\n".join(x for x in (add.stdout, add.stderr, commit.stdout, commit.stderr) if x.strip())
    st.session_state["git_output"] = f"$ git add -- {rel}\n$ git commit -m \"{message}\"\n{output}"
    if commit.returncode == 0:
        st.session_state["flash"] = f"Committed: {message}"
    else:
        st.session_state["flash_error"] = "git commit failed; see the output below."


def sidebar_actions(root: Path, ticker: str, path: Path, diff: list[yamlio.Change]) -> None:
    sb = st.sidebar
    sb.subheader("Actions")
    note_key = f"save_note:{ticker}"
    sb.text_input("Note for the change log (one line, optional)", key=note_key,
                  placeholder="why you changed these cells")
    c1, c2 = sb.columns(2)
    c1.button("Reset to file", key="reset_btn", on_click=_reset_cb, args=(root, ticker), **_WIDE)
    c2.button("Save to assumptions.yaml", key="save_btn", type="primary", disabled=not diff,
              on_click=_save_cb, args=(root, ticker, path, note_key), **_WIDE)
    c3, c4 = sb.columns(2)
    c3.button("Write valuation.md", key="write_btn", on_click=_write_cb, args=(path,), **_WIDE,
              help="Archives the current pair to history/, computes with the sidebar's market inputs, writes "
                   "valuation.md and assumptions.md. Refuses while there are unsaved changes.")
    c4.button("Commit", key="commit_btn", on_click=_commit_cb, args=(root, ticker), **_WIDE,
              help="git add companies/<T>/valuation and commit as company-research. Never pushes.")
    if diff:
        sb.caption("Write valuation.md is refused while changes are unsaved.")


# --------------------------------------------------------------------------- #
# Compute
# --------------------------------------------------------------------------- #

def compute_result(doc: dict[str, Any], market: MarketInputs | None) -> tuple[ValuationResult | None, str | None]:
    if market is None:
        return None, "Enter the market inputs in the sidebar to compute."
    try:
        return valuation.compute(doc, market=market, fetch=False), None
    except SchemaError as exc:
        return None, "The assumptions do not validate:\n\n" + "\n".join(f"- {line}" for line in str(exc).splitlines())
    except (EngineError, MarketError) as exc:
        return None, str(exc)
    except Exception as exc:                                   # noqa: BLE001 - never show a traceback
        return None, f"The engine could not compute: {type(exc).__name__}: {exc}"


# --------------------------------------------------------------------------- #
# Top of page: results table and chart
# --------------------------------------------------------------------------- #

def results_table(result: ValuationResult) -> pd.DataFrame:
    doc = result.assumptions
    rows = []
    for name in SCENARIO_NAMES:
        if name not in (doc.get("scenarios") or {}):
            continue
        weight = get_path(doc, f"scenarios.{name}.weight")
        wtxt = "not weighted" if name == "management" else pct(weight, 0)
        sc = result.scenarios.get(name)
        if sc is None:
            why = "; ".join(result.stopped.get(name, [])) or result.skipped.get(name, "not computed")
            rows.append({"Case": name, "Weight": wtxt, "Operating assets": "", "Enterprise value": "",
                         "Equity value": "", "Value per share": "not computed", "Price": "", "Upside / downside": "",
                         "Terminal-value share": "", "10-year-fade per share": "", "Note": why})
            continue
        fade = sc.fade_reference.per_share if sc.fade_reference else None
        rows.append({"Case": name, "Weight": wtxt, "Operating assets": money(sc.operating_assets),
                     "Enterprise value": money(sc.enterprise_value), "Equity value": money(sc.equity),
                     "Value per share": per_share(sc.per_share), "Price": per_share(sc.price),
                     "Upside / downside": pct(sc.upside), "Terminal-value share": pct(sc.terminal_share),
                     "10-year-fade per share": per_share(fade), "Note": "; ".join(sc.warnings)})
    if result.weighted:
        w = result.weighted
        rows.append({"Case": "weighted expected", "Weight": "100%", "Operating assets": money(w.operating_assets),
                     "Enterprise value": money(w.enterprise_value), "Equity value": money(w.equity),
                     "Value per share": per_share(w.per_share), "Price": per_share(result.market.price),
                     "Upside / downside": pct(w.upside), "Terminal-value share": pct(w.terminal_share),
                     "10-year-fade per share": per_share(w.fade_per_share), "Note": ""})
    else:
        rows.append({"Case": "weighted expected", "Weight": "", "Value per share": "not computed",
                     "Note": "a weighted scenario is missing"})
    return pd.DataFrame(rows).fillna("")


def value_chart(result: ValuationResult) -> alt.LayerChart | None:
    data = []
    for name in WEIGHTED_SCENARIOS:
        sc = result.scenarios.get(name)
        if sc is not None:
            fade = sc.fade_reference.per_share if sc.fade_reference else None
            data.append({"case": name, "value": sc.per_share, "fade": fade,
                         "label": f"10-yr {per_share(fade)}" if fade is not None else ""})
    if result.weighted:
        w = result.weighted
        data.append({"case": "weighted", "value": w.per_share, "fade": w.fade_per_share,
                     "label": f"10-yr {per_share(w.fade_per_share)}"})
    if not data:
        return None
    df = pd.DataFrame(data)
    order = [d["case"] for d in data]
    price = result.market.price
    base = alt.Chart(df).encode(x=alt.X("case:N", sort=order, title=None, axis=alt.Axis(labelAngle=0)))
    bars = base.mark_bar(color=BLUE, cornerRadiusTopLeft=4, cornerRadiusTopRight=4, size=56).encode(
        y=alt.Y("value:Q", title="Value per share (USD)"),
        tooltip=[alt.Tooltip("case:N", title="Case"), alt.Tooltip("value:Q", title="Value per share", format=",.2f"),
                 alt.Tooltip("fade:Q", title="10-year-fade reference", format=",.2f")])
    labels = base.mark_text(dy=-8, color=INK_2, fontSize=12).encode(y="value:Q", text="label:N")
    rule_df = pd.DataFrame({"price": [price], "text": [f"price {per_share(price)}"]})
    rule = alt.Chart(rule_df).mark_rule(color=INK, strokeDash=[6, 4], size=2).encode(y="price:Q")
    rule_text = alt.Chart(rule_df).mark_text(align="left", baseline="bottom", dx=4, dy=-4, color=INK, fontSize=12).encode(
        y="price:Q", text="text:N", x=alt.value(0))
    return (bars + labels + rule + rule_text).properties(height=320, title="Value per share by case, against the price")


def top_section(result: ValuationResult) -> None:
    st.dataframe(results_table(result), hide_index=True, **_WIDE)
    chart = value_chart(result)
    if chart is not None:
        st.altair_chart(chart, **_WIDE)


# --------------------------------------------------------------------------- #
# Scenario tabs
# --------------------------------------------------------------------------- #

YEAR_ROWS = [("revenue_growth", "Revenue growth (decimal)"),
             ("operating_margin", "Operating margin (decimal)"),
             ("reinvestment_override", "Reinvestment override (USD millions; empty = sales-to-capital rule)")]


def _years_cb(k: str, name: str, T: int) -> None:
    """Apply data_editor edits (``edited_rows``) to the scenario's per-year lists."""
    state = st.session_state.get(k) or {}
    doc = working()
    for row_str, cols in (state.get("edited_rows") or {}).items():
        row = int(row_str)
        if row >= len(YEAR_ROWS):
            continue
        input_key = YEAR_ROWS[row][0]
        node = doc["scenarios"][name].setdefault(input_key, {})
        values = list(node.get("values") or [None] * T)
        values += [None] * (T - len(values))
        for col, val in cols.items():
            if not col.startswith("Y"):
                continue
            t = int(col[1:]) - 1
            if 0 <= t < T:
                values[t] = _to_float(val)
        node["values"] = values[:T]


def year_editor(doc: dict[str, Any], name: str, T: int) -> None:
    sc = doc["scenarios"][name]
    table: dict[str, Any] = {"Input": [label for _, label in YEAR_ROWS]}
    for t in range(T):
        col = []
        for k, _ in YEAR_ROWS:
            values = (sc.get(k) or {}).get("values") or []
            v = values[t] if t < len(values) else None
            col.append(float("nan") if v is None else float(v))
        table[f"Y{t + 1}"] = pd.Series(col, dtype="float64")
    df = pd.DataFrame(table)
    k = key(f"scenarios.{name}.years")
    config = {"Input": st.column_config.TextColumn("Input", width="large")}
    for t in range(T):
        config[f"Y{t + 1}"] = st.column_config.NumberColumn(f"Y{t + 1}", format="%.4g")
    st.data_editor(df, key=k, hide_index=True, disabled=["Input"], column_config=config, on_change=_years_cb,
                   args=(k, name, T), **_WIDE)
    st.caption("Rates are decimals: 0.12 means 12%. The reinvestment override is in USD millions; leave a cell "
               "empty to use the sales-to-capital rule for that year. Double-click a cell to edit it.")
    with st.expander("Reasons and sources for the per-year inputs"):
        cols = st.columns(3)
        for (k2, label), c in zip(YEAR_ROWS, cols):
            c.markdown(f"**{label.split(' (')[0]}**")
            reason_and_source(doc, f"scenarios.{name}.{k2}", c, height=140)


def scenario_status(name: str, result: ValuationResult | None, error: str | None) -> None:
    if result is None:
        if error:
            st.error(error)
        return
    sc = result.scenarios.get(name)
    if sc is not None:
        c = st.columns(4)
        c[0].metric("Value per share", per_share(sc.per_share))
        c[1].metric("Against the price", pct(sc.upside), help=f"price {per_share(sc.price)}")
        c[2].metric("Terminal-value share", pct(sc.terminal_share))
        c[3].metric("10-year-fade reference", per_share(sc.fade_reference.per_share if sc.fade_reference else None))
        for w in sc.warnings:
            st.warning(w)
    elif name in result.stopped:
        st.warning("Not computed: " + "; ".join(result.stopped[name]))
    elif name in result.skipped:
        st.info(f"Not computed: {result.skipped[name]}")


def scenario_tab(doc: dict[str, Any], name: str, result: ValuationResult | None, error: str | None) -> None:
    sc = (doc.get("scenarios") or {}).get(name)
    if not isinstance(sc, dict):
        st.info(f"The YAML has no `{name}` scenario.")
        return
    T = int(doc.get("horizon", 5)) if doc.get("horizon") in (5, 10) else 5
    p = f"scenarios.{name}"
    scenario_status(name, result, error)
    if name == "management":
        left, right = st.columns([1, 3])
        w_bool(doc, f"{p}.computable", "Computable (management gave at least one multi-year revenue or margin target)",
               container=left)
        w_text(doc, f"{p}.reason", "Why this case is or is not computable", height=120, container=right)
        guidance = sc.get("guidance") or []
        st.markdown("**Guidance on record** (read-only; every quantitative or qualitative item management has given)")
        if guidance:
            st.dataframe(pd.DataFrame([{"Item": g.get("item"), "Quote": g.get("quote"), "Source": g.get("source"),
                                        "Used as": g.get("used_as")} for g in guidance if isinstance(g, dict)]),
                         hide_index=True, **_WIDE)
        else:
            st.caption("None recorded.")
    else:
        w_text(doc, f"{p}.story", "Story (three to five plain sentences; what has to be true for this case)",
               height=140, convert=_to_story)
        w_number(doc, f"{p}.weight", "Weight (bear + base + bull must sum to 1)", "weight")
    st.markdown("#### Inputs by year")
    year_editor(doc, name, T)
    st.markdown("#### Single-value inputs")
    left, right = st.columns([2, 3])
    w_number(doc, f"{p}.sales_to_capital.value", "Sales-to-capital, years 1-5", "ratio", container=left,
             help="Dollars of extra yearly revenue that one dollar of reinvestment buys.")
    w_number(doc, f"{p}.sales_to_capital.value_late", "Sales-to-capital, years 6-10 (10-year reference)", "ratio",
             container=left)
    reason_and_source(doc, f"{p}.sales_to_capital", right, height=130)
    left, right = st.columns([2, 3])
    w_number(doc, f"{p}.tax_rate.start", "Tax rate, explicit years (decimal)", "rate", container=left)
    w_number(doc, f"{p}.tax_rate.terminal", "Tax rate, terminal (decimal)", "rate", container=left)
    reason_and_source(doc, f"{p}.tax_rate", right, height=130)
    left, right = st.columns([2, 3])
    w_growth(doc, f"{p}.terminal.growth.value", container=left)
    w_bool(doc, f"{p}.terminal.growth.allow_above_riskfree", "Allow terminal growth above the risk-free rate",
           container=left, help="Section 18.4 rule 5: needs a reason; the engine prints a warning.")
    reason_and_source(doc, f"{p}.terminal.growth", right, height=130)
    left, right = st.columns([2, 3])
    w_number(doc, f"{p}.terminal.roic_premium.value", "Terminal return on capital: points above the cost of capital (decimal)",
             "rate", container=left)
    w_bool(doc, f"{p}.terminal.roic_premium.allow_large_premium", "Allow a premium above 0.05",
           container=left, help="Section 18.4 rule 5: needs a reason; the engine prints a warning.")
    reason_and_source(doc, f"{p}.terminal.roic_premium", right, height=130)
    left, right = st.columns([2, 3])
    w_number(doc, f"{p}.cost_of_capital_override", "Cost of capital override (decimal; empty = shared)", "rate",
             container=left, help="Section 18.4 rule 6: scenarios share the cost of capital unless a reason is given.")
    if result is not None and name in result.scenarios:
        t = result.scenarios[name].terminal
        right.caption(f"Live: cost of capital {pct(result.scenarios[name].inputs.wacc, 2)}, terminal cost of capital "
                      f"{pct(t.wacc, 2)}, terminal growth {pct(t.growth, 2)}, terminal return on capital {pct(t.roic, 2)}.")


# --------------------------------------------------------------------------- #
# Base year & bridge, cost of capital
# --------------------------------------------------------------------------- #

BASE_FACTS = [("base_year.revenue", "Revenue, trailing twelve months", "money"),
              ("base_year.operating_income_gaap", "Operating income, GAAP", "money"),
              ("base_year.amortization_of_acquired_intangibles", "Amortization of acquired intangibles (memo)", "money"),
              ("base_year.stock_based_compensation", "Stock-based compensation (memo)", "money"),
              ("base_year.rnd_expense", "Research and development expense (memo)", "money"),
              ("base_year.effective_tax_rate", "Effective tax rate", "rate"),
              ("base_year.invested_capital", "Invested capital (book equity + debt + leases - cash)", "money")]
BRIDGE_FACTS = [("bridge.cash_and_marketable_securities", "Cash and marketable securities (added)", "money"),
                ("bridge.debt", "Debt (subtracted)", "money"),
                ("bridge.operating_lease_liabilities", "Operating lease liabilities (subtracted)", "money"),
                ("bridge.minority_interests", "Minority interests (subtracted)", "money"),
                ("bridge.probability_of_failure", "Probability of failure", "rate"),
                ("bridge.distress_proceeds", "What the assets would fetch in a failure", "money"),
                ("bridge.diluted_shares", "Diluted shares (millions)", "shares")]
FORMATTERS = {"money": money, "rate": pct, "shares": lambda x: num(x, 1), "beta": lambda x: num(x, 3),
              "ratio4": lambda x: num(x, 4), "ratio": num, "text": lambda x: "—" if x is None else str(x)}


def facts_table(doc: dict[str, Any], facts: list[tuple[str, str, str]], items: list[tuple[str, str]] | None = None) -> None:
    rows = []
    for path, label, kind in facts:
        node = get_path(doc, path)
        node = node if isinstance(node, dict) else {}
        rows.append({"Item": label, "Value": FORMATTERS[kind](node.get("value")), "Reason": node.get("reason") or "",
                     "Source": node.get("source") or ""})
    for list_path, prefix in items or []:
        for item in get_path(doc, list_path) or []:
            if isinstance(item, dict):
                rows.append({"Item": f"{prefix}: {item.get('name', '')}", "Value": money(item.get("value")),
                             "Reason": item.get("reason") or "", "Source": item.get("source") or ""})
    st.dataframe(pd.DataFrame(rows), hide_index=True, **_WIDE)


def facts_editor(doc: dict[str, Any], facts: list[tuple[str, str, str]], items: list[tuple[str, str]] | None = None) -> None:
    for path, label, kind in facts:
        left, right = st.columns([2, 3])
        w_number(doc, f"{path}.value", label, kind, container=left)
        reason_and_source(doc, path, right, height=110)
    for list_path, prefix in items or []:
        for i, item in enumerate(get_path(doc, list_path) or []):
            if not isinstance(item, dict):
                continue
            left, right = st.columns([2, 3])
            w_number(doc, f"{list_path}.{i}.value", f"{prefix}: {item.get('name', '')}", "money", container=left)
            w_text(doc, f"{list_path}.{i}.reason", "Reason", height=110, container=right)
            right.caption(f"Source: {item.get('source') or 'none given'}")


def base_bridge_tab(doc: dict[str, Any], result: ValuationResult | None) -> None:
    edit = st.toggle("Edit facts", key=key("edit_facts_base"),
                     help="Sourced numbers are read-only until this is on. Every edit is recorded in the changelog on Save.")
    st.markdown(f"#### Base year ({get_path(doc, 'base_year.period') or 'period not given'})")
    if edit:
        facts_editor(doc, BASE_FACTS, [("base_year.one_time_items", "One-time item")])
        st.markdown("**Switches** (section 18.4 rule 1: the analyst leaves them off)")
        c = st.columns(3)
        w_bool(doc, "switches.addback_acquired_amortization", "Add back amortization of acquired intangibles", container=c[0])
        w_bool(doc, "switches.capitalize_rnd", "Treat research spending as an investment", container=c[1])
        w_number(doc, "switches.rnd_amortization_years", "Years to write research spending off", "int", container=c[2])
    else:
        facts_table(doc, BASE_FACTS, [("base_year.one_time_items", "One-time item")])
        sw = doc.get("switches") or {}
        st.caption(f"Switches: add back acquired amortization = {bool(sw.get('addback_acquired_amortization'))}; "
                   f"treat research spending as an investment = {bool(sw.get('capitalize_rnd'))} "
                   f"({sw.get('rnd_amortization_years', 5)} years); reinvestment lag = {sw.get('reinvestment_lag', 1)}.")
    if result is not None:
        by = result.base_year
        st.markdown("**Derived (live)**")
        c = st.columns(4)
        c[0].metric("Adjusted operating income", money(by.adjusted_operating_income))
        c[1].metric("Adjusted operating margin", pct(by.margin))
        c[2].metric("Invested capital used", money(by.invested_capital))
        c[3].metric("Base-year return on capital", pct(by.roic))
    st.markdown("#### Bridge from operating assets to equity")
    lists = [("bridge.non_operating_assets", "Non-operating asset (added)"), ("bridge.other_claims", "Other claim (subtracted)")]
    if edit:
        facts_editor(doc, BRIDGE_FACTS, lists)
        w_text(doc, "bridge.dilution_note", "Dilution note", height=100)
    else:
        facts_table(doc, BRIDGE_FACTS, lists)
        note = get_path(doc, "bridge.dilution_note")
        if note:
            st.caption(f"Dilution note: {note}")
    if result is not None and "base" in result.scenarios:
        sc, b = result.scenarios["base"], result.bridge
        st.markdown("**Derived for the base case (live)**")
        rows = [("Operating assets", money(sc.operating_assets)),
                ("+ cash and marketable securities", money(b.cash)),
                ("+ non-operating assets", money(b.non_operating_assets)),
                ("- debt", money(b.debt)), ("- operating lease liabilities", money(b.leases)),
                ("- minority interests", money(b.minority_interests)), ("- other claims", money(b.other_claims)),
                ("= equity value", money(sc.equity)), ("/ diluted shares (millions)", num(b.diluted_shares, 1)),
                ("= value per share", per_share(sc.per_share)),
                ("Enterprise value today (price x shares + claims - cash)", money(sc.enterprise_value))]
        st.dataframe(pd.DataFrame(rows, columns=["Step", "USD millions"]), hide_index=True, **_WIDE)


COC_FACTS = [("cost_of_capital.build.unlevered_beta", "Unlevered beta", "beta"),
             ("cost_of_capital.build.debt_to_equity_market", "Debt to equity (market values)", "ratio4"),
             ("cost_of_capital.build.pretax_cost_of_debt", "Pre-tax cost of debt", "rate")]


def cost_of_capital_tab(doc: dict[str, Any], result: ValuationResult | None) -> None:
    edit = st.toggle("Edit facts", key=key("edit_facts_coc"))
    coc = doc.get("cost_of_capital") or {}
    if edit:
        c = st.columns(3)
        w_choice(doc, "cost_of_capital.method", "Method", ["build", "pinned"], container=c[0])
        w_number(doc, "cost_of_capital.pinned_value", "Pinned cost of capital (decimal; used when method is pinned)", "rate",
                 container=c[1])
        left, right = st.columns([2, 3])
        k = key("cost_of_capital.build.damodaran_industry.value")
        left.text_input("Damodaran industry", value=get_path(doc, "cost_of_capital.build.damodaran_industry.value") or "",
                        key=k, on_change=_sync, args=(k, "cost_of_capital.build.damodaran_industry.value", _to_text))
        w_text(doc, "cost_of_capital.build.damodaran_industry.reason", "Reason", height=100, container=right)
        facts_editor(doc, COC_FACTS)
        c = st.columns(3)
        w_choice(doc, "cost_of_capital.terminal.method", "Terminal cost of capital method", ["mature", "hold", "value"],
                 container=c[0])
        w_number(doc, "cost_of_capital.terminal.value", "Terminal cost of capital (decimal; when method is value)", "rate",
                 container=c[1])
        w_text(doc, "cost_of_capital.terminal.reason", "Reason", height=100, container=c[2])
        c = st.columns(2)
        w_number(doc, "market.mature_market_erp", "Mature-market equity risk premium (decimal)", "rate", container=c[0])
        w_number(doc, "market.marginal_tax_rate", "Marginal tax rate (decimal)", "rate", container=c[1])
    else:
        rows = [{"Item": "Method", "Value": coc.get("method") or "—", "Reason": "", "Source": ""}]
        if coc.get("pinned_value") is not None:
            rows.append({"Item": "Pinned cost of capital", "Value": pct(coc.get("pinned_value"), 2), "Reason": "", "Source": ""})
        ind = get_path(doc, "cost_of_capital.build.damodaran_industry") or {}
        rows.append({"Item": "Damodaran industry", "Value": ind.get("value") or "—", "Reason": ind.get("reason") or "", "Source": ""})
        for path, label, kind in COC_FACTS:
            node = get_path(doc, path) or {}
            rows.append({"Item": label, "Value": FORMATTERS[kind](node.get("value")), "Reason": node.get("reason") or "",
                         "Source": node.get("source") or ""})
        term = coc.get("terminal") or {}
        rows.append({"Item": "Terminal cost of capital method", "Value": term.get("method", "mature"),
                     "Reason": term.get("reason") or "", "Source": ""})
        if term.get("value") is not None:
            rows.append({"Item": "Terminal cost of capital, given", "Value": pct(term.get("value"), 2), "Reason": "", "Source": ""})
        m = doc.get("market") or {}
        rows.append({"Item": "Mature-market equity risk premium", "Value": pct(m.get("mature_market_erp"), 2), "Reason": "", "Source": "market.mature_market_erp"})
        rows.append({"Item": "Marginal tax rate", "Value": pct(m.get("marginal_tax_rate")), "Reason": "", "Source": "market.marginal_tax_rate"})
        st.dataframe(pd.DataFrame(rows), hide_index=True, **_WIDE)
    if result is None:
        return
    c = result.cost_of_capital
    st.markdown("**Derived (live)**")
    rows = [("Risk-free rate", pct(c.risk_free, 2)), ("Equity risk premium", pct(c.equity_risk_premium, 2))]
    if c.method == "build":
        rows += [("Unlevered beta" + (" (from the cached dataset)" if c.unlevered_beta_note else ""), num(c.unlevered_beta, 3)),
                 ("Debt to equity" + (" (derived from the bridge and the price)" if c.debt_to_equity_note else ""), num(c.debt_to_equity, 4)),
                 ("Levered beta", num(c.levered_beta, 3)), ("Cost of equity", pct(c.cost_of_equity, 2)),
                 ("After-tax cost of debt", pct(c.after_tax_cost_of_debt, 2)),
                 ("Weights: equity / debt", f"{pct(c.weight_equity)} / {pct(c.weight_debt)}")]
    rows += [("Cost of capital (WACC)", pct(c.wacc, 2)), (f"Terminal cost of capital ({c.terminal_method})", pct(c.terminal_wacc, 2))]
    for name, sc in result.scenarios.items():
        rows.append((f"Terminal return on capital, {name} case", pct(sc.terminal.roic, 2)))
    st.dataframe(pd.DataFrame(rows, columns=["Item", "Value"]), hide_index=True, **_WIDE)
    for w in c.warnings:
        st.caption(w)


# --------------------------------------------------------------------------- #
# Analysis tabs
# --------------------------------------------------------------------------- #

def heatmap(grid: Grid) -> alt.LayerChart:
    rows = []
    for i, rv in enumerate(grid.row_values):
        for j, cv in enumerate(grid.col_values):
            cell = grid.cells[i][j]
            rows.append({"row": pct(rv, 2), "col": pct(cv, 2), "value": cell,
                         "label": per_share(cell) if cell is not None else "n/a",
                         "base": i == grid.base_row and j == grid.base_col})
    df = pd.DataFrame(rows)
    row_order = [pct(v, 2) for v in grid.row_values]
    col_order = [pct(v, 2) for v in grid.col_values]
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
    return (rects + text + marker).properties(height=260, title=grid.title)


def sensitivity_tab(result: ValuationResult | None) -> None:
    if result is None or result.analysis is None:
        st.info("Sensitivity grids appear once the model computes.")
        return
    a = result.analysis
    st.caption(f"Both grids move the {a.scenario} case. The outlined cell is the case as entered.")
    for grid in a.grids:
        st.altair_chart(heatmap(grid), **_WIDE)
        st.caption(grid.note)


def year_by_year_tab(result: ValuationResult | None) -> None:
    if result is None or not result.scenarios:
        st.info("The year-by-year table appears once the model computes.")
        return
    names = list(result.scenarios)
    name = st.selectbox("Case", names, index=names.index("base") if "base" in names else 0, key="yby_case")
    sc = result.scenarios[name]
    rows = []
    for r in sc.rows:
        rows.append({"Year": str(r.year), "Revenue": money(r.revenue), "Growth": pct(r.growth), "Margin": pct(r.margin),
                     "After-tax operating income": money(r.ebit_after_tax),
                     "Reinvestment": money(r.reinvestment) + (" (override)" if r.reinvestment_source == "override" else ""),
                     "Free cash flow": money(r.fcff), "Cost of capital": pct(r.wacc, 2),
                     "Discount factor": num(r.discount_factor, 4), "Present value": money(r.pv),
                     "Implied return on capital": pct(r.roic)})
    t = sc.terminal
    rows.append({"Year": "Terminal (T+1)", "Revenue": money(t.revenue), "Growth": pct(t.growth), "Margin": pct(t.margin),
                 "After-tax operating income": money(t.ebit_after_tax), "Reinvestment": money(t.reinvestment),
                 "Free cash flow": money(t.fcff), "Cost of capital": pct(t.wacc, 2),
                 "Discount factor": num(sc.rows[-1].discount_factor, 4), "Present value": money(t.pv),
                 "Implied return on capital": pct(t.roic)})
    st.dataframe(pd.DataFrame(rows), hide_index=True, **_WIDE)
    st.caption("Reinvestment in a year buys the next year's growth, so the last explicit year's reinvestment is sized "
               "for terminal growth. Terminal value: "
               f"{money(t.value)}; present value {money(t.pv)}; share of operating assets {pct(sc.terminal_share)}.")


def reverse_tab(result: ValuationResult | None) -> None:
    if result is None or result.analysis is None or result.analysis.reverse is None:
        st.info("The reverse DCF appears once the model computes.")
        return
    a, r = result.analysis, result.analysis.reverse
    rows = [("Enterprise value today (target)", money(r.target_enterprise_value)),
            (f"Operating assets in the {a.scenario} case", money(r.base_operating_assets)),
            (f"Average revenue growth in the {a.scenario} case (years 1-5)", pct(r.base_average_growth)),
            ("Constant yearly growth that matches the price",
             pct(r.implied_growth) if r.implied_growth is not None else f"not found: {r.implied_growth_note}"),
            (f"Year-5 margin in the {a.scenario} case", pct(r.base_year5_margin)),
            ("Year-5 margin that matches the price",
             pct(r.implied_year5_margin) if r.implied_year5_margin is not None else f"not found: {r.implied_margin_note}")]
    st.dataframe(pd.DataFrame(rows, columns=["Item", "Value"]), hide_index=True, **_WIDE)
    st.caption(f"The first solve keeps the {a.scenario} case's margins, reinvestment rule, cost of capital and terminal "
               "settings and asks what constant yearly revenue growth makes operating assets equal today's enterprise "
               "value. The second keeps the growth path and solves for the year-5 margin.")


def diagnostics_tab(result: ValuationResult | None) -> None:
    if result is None or result.analysis is None:
        st.info("Diagnostics appear once the model computes.")
        return
    a = result.analysis
    if a.industry:
        f = a.industry
        st.markdown(f"**Industry figures** for '{f.industry}' from the cached Damodaran datasets")
        rows = [("Unlevered beta corrected for cash", num(f.unlevered_beta_cash_corrected.value, 3), f.unlevered_beta_cash_corrected.dataset_date or ""),
                ("Cost of capital", pct(f.cost_of_capital.value), f.cost_of_capital.dataset_date or ""),
                ("Sales to invested capital", num(f.sales_to_capital.value), f.sales_to_capital.dataset_date or ""),
                ("Pre-tax operating margin", pct(f.pretax_operating_margin.value), f.pretax_operating_margin.dataset_date or ""),
                ("Revenue growth, last 5 years", pct(f.revenue_cagr_5y.value), f.revenue_cagr_5y.dataset_date or ""),
                ("Effective tax rate", pct(f.effective_tax_rate.value), f.effective_tax_rate.dataset_date or "")]
        st.dataframe(pd.DataFrame(rows, columns=["Figure", "Value", "Dataset date"]), hide_index=True, **_WIDE)
    for d in a.diagnostics:
        st.markdown(f"**{d.title}**" + ("  :red[flag]" if d.flag else ""))
        st.dataframe(pd.DataFrame(d.rows, columns=["Item", "Value"]), hide_index=True, **_WIDE)
        if d.note:
            st.caption(d.note)


def warnings_tab(result: ValuationResult | None, error: str | None) -> None:
    if error:
        st.error(error)
    if result is None:
        return
    items = list(result.warnings)
    if result.analysis:
        items += [w for w in result.analysis.warnings if w not in items]
    if not items:
        st.success("None.")
    for w in items:
        st.markdown(f"- {w}")


# --------------------------------------------------------------------------- #
# Page
# --------------------------------------------------------------------------- #

def main() -> None:
    st.set_page_config(page_title="Valuation assumptions", layout="wide")
    root = repo_root()
    tickers = company_tickers(root)
    if not tickers:
        st.error(f"No companies/<TICKER>/valuation/assumptions.yaml found under {root}.")
        st.stop()
    st.sidebar.title("Valuation")
    ticker = st.sidebar.selectbox("Company", tickers, key="company_pick")
    if st.session_state.get("ticker") != ticker:
        load_company(root, ticker)
    doc, path = working(), st.session_state["path"]

    market = sidebar_market(doc, ticker)
    st.session_state["market_inputs"] = market
    sidebar_horizon(doc)

    result, error = compute_result(doc, market)
    st.session_state["last_result"] = result

    st.title(f"{ticker}: {doc.get('company') or ''}")
    st.caption(f"As of {doc.get('as_of_quarter')} (cutoff {doc.get('as_of_date')}); drafted {doc.get('drafted')}"
               + (f"; owner edited {doc.get('owner_edited')}" if doc.get("owner_edited") else "")
               + f". File: {path}")
    for kind, k in (("success", "flash"), ("error", "flash_error")):
        msg = st.session_state.pop(k, None)
        if msg:
            getattr(st, kind)(msg)
    if error:
        st.error(error)
    tab_error = None if market is None else error          # the tabs repeat engine messages, not the market prompt
    if result is not None:
        top_section(result)
    if st.session_state.get("last_output"):
        with st.expander("Output of the last Write valuation.md"):
            st.code(st.session_state["last_output"])
    if st.session_state.get("git_output"):
        with st.expander("Output of the last Commit", expanded=True):
            st.code(st.session_state["git_output"])

    tabs = st.tabs(TAB_NAMES)
    for i, name in enumerate(("bear", "base", "bull", "management")):
        with tabs[i]:
            scenario_tab(doc, name, result, tab_error)
    with tabs[4]:
        base_bridge_tab(doc, result)
    with tabs[5]:
        cost_of_capital_tab(doc, result)
    with tabs[6]:
        sensitivity_tab(result)
    with tabs[7]:
        year_by_year_tab(result)
    with tabs[8]:
        reverse_tab(result)
    with tabs[9]:
        diagnostics_tab(result)
    with tabs[10]:
        warnings_tab(result, tab_error)

    diff = unsaved_changes(doc, path)
    sidebar_changes(diff)
    sidebar_actions(root, ticker, path, diff)


main()
