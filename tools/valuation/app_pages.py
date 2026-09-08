"""The pages of the valuation walk, one function each (AGENTS.md section 18.10).

Every factor page has the same layout, top to bottom: (a) a short explanation for the
16-year-old and a one-line instruction, (b) the company's own history where the YAML carries
it, (c) one bordered block per case with the analyst's reason in full, its working notes in a
fold-out when the cell has them, the source tags and the prefilled inputs, (d) the live readout
line and (e) Back / Next.  The readout and the buttons are drawn by ``app.py`` after the page
function returns, so the page functions here only draw (a) to (c).

Prose rules: plain words, no LaTeX, no ``$`` (Streamlit reads it as a formula), no Unicode
math symbols, no YAML keys, dotted paths or spec citations; percentages one decimal (market-style
rates two), money in USD millions with separators, per share to the cent.  Text from the YAML
goes through :func:`valuation.app_core.md`; engine messages through :func:`plain_message`.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pandas as pd
import streamlit as st

from valuation import MarketInputs
from valuation.app_core import (
    _WIDE, CASE_LABELS, METHOD_HELP, METHOD_WORDS, NA, STALE_BANNER, TERMINAL_METHOD_HELP, TERMINAL_METHOD_WORDS,
    _commit_cb, _restart_cb, _save_cb, _write_cb, changes_table, fade_clause, fade_line, file_changed_on_disk, heatmap,
    horizon_control, market_boxes, md, money, num, path_list, pct, pct2, pending_commit, per_share, plain_message,
    ranking_for, ranking_table, reason_block, result_notes, results_table, shares, static_table, stop_sentence,
    unsaved_changes, value_chart, w_bool, w_choice, w_line, w_number, w_pct, w_text, w_terminal_growth,
    warning_sentence, working_notes, year_boxes,
)
from valuation.engine import ValuationResult
from valuation.schema import EXPLICIT_YEARS, WEIGHTED_SCENARIOS, get_path, is_riskfree, large_premium_ceiling


@dataclass
class Ctx:
    """Everything a page needs, resolved once per rerun by ``app.py``."""
    root: Path
    ticker: str
    path: Path
    doc: dict[str, Any]
    market: MarketInputs | None
    result: ValuationResult | None
    error: str | None
    T: int                    # the model horizon: 10 by default, 5 when the file says so
    explicit: int             # the years the owner sets: 5 at a ten-year horizon unless the file has ten-entry lists


# --------------------------------------------------------------------------- #
# The explanations (the product; written for a smart 16-year-old)
# --------------------------------------------------------------------------- #

EXPLANATIONS = {
    "revenue_growth": (
        "Revenue is the money customers pay the company in a year, and revenue growth is how fast that number "
        "rises. Almost everything else in the model is a share of revenue, so a faster path means bigger profits "
        "and bigger cash flows in every later year, which is why this factor usually moves the value most. "
        "Damodaran asks three questions of any growth path: is it possible (does year-5 revenue fit inside the "
        "market the company sells into), is it plausible (can this company really win that much), and is it "
        "probable (has management delivered growth like this before)? Each box below is the growth over the year "
        "before, so 20 means revenue ends the year a fifth higher than it started. You set the first five years; "
        "years 6 to 10 are built by rule, easing in equal steps from your year-5 number to the growth the economy "
        "manages forever, and they are shown under the boxes."
    ),
    "operating_margin": (
        "Operating margin is the share of each dollar of revenue left as profit after the costs of running the "
        "business, before interest and taxes. It matters because the model turns revenue into cash by multiplying "
        "by the margin: a company that keeps 30 cents of every dollar is worth far more than one that keeps 15 "
        "cents on the same sales. Damodaran starts from the margin the company reports today and asks where it "
        "settles as the business matures, checked against the industry and the company's own history. Stock-based "
        "pay counts as a real cost here and the amortization of past acquisitions stays deducted, so these are "
        "GAAP margins, not the adjusted ones management likes to quote. You set the first five years; the margin "
        "then holds at your year-5 level through year 10, which is shown under the boxes."
    ),
    "reinvestment": (
        "Growth is not free: to sell more, a company has to spend first, on factories, machines, software and the "
        "working capital that sits in inventory and unpaid bills. The model captures this with sales-to-capital, "
        "the dollars of extra yearly revenue that one dollar of reinvestment buys; a higher ratio means growth "
        "costs less, so more cash is left for the people who fund the company. Damodaran sizes each year's "
        "reinvestment as the coming year's revenue increase divided by this ratio, unless a specific spending "
        "figure (a capital-spending plan management has announced) overrides it for that year. How far ahead the "
        "spending is credited is a setting on the Facts check page: one year by default, which is what his own "
        "template does, and up to three for a business whose factories take that long to earn anything. Watch the "
        "pairing with the growth page: fast growth at a low ratio eats most of the cash it creates."
    ),
    "cost_of_capital": (
        "The cost of capital is the yearly return that the people funding the company, lenders and shareholders "
        "together, could expect from other investments of similar risk. The model uses it as the discount rate: a "
        "dollar expected five years from now is worth less than a dollar today, and the higher this rate, the "
        "less every future cash flow counts, so a higher cost of capital lowers the value. Damodaran builds it "
        "from parts: the risk-free rate (what a government bond pays), plus a premium for owning a risky business "
        "scaled by beta (how much this industry swings with the market), blended with the after-tax cost of the "
        "company's debt. The same rate is used for every case, because the cases differ in what the business "
        "does, not in the market's price of risk."
    ),
    "terminal": (
        "The forecast stops after the forecast years, but the company does not, so the terminal value is what "
        "all the cash flows after that are worth, treated as a business growing at one steady rate forever. It "
        "is usually the largest part of the value, which is why its rules are strict: Damodaran caps growth at "
        "the risk-free rate (no company outgrows the economy forever) and by default assumes the return on "
        "capital drops to the cost of capital, meaning the company's advantage has faded and growth adds nothing "
        "extra. A return-on-capital premium above zero says part of the moat lasts forever, so it needs a reason, "
        "it has to be zero in the bear case, and it should leave the terminal return below the return the company "
        "earns today. Above 8 points in the base case, or 12 in the bull, it also needs the switch ticked: "
        "Damodaran's own choices for wide moats were 4 points for Alphabet in 2018 (a 12% return against an 8% cost "
        "of capital) and 11.5 for Nvidia in 2023 (20% against 8.85%). The terminal cost of capital moves to the rate "
        "a mature company pays, and the share of value that comes from the terminal value is shown on the Results "
        "page as a check on how much rests on this page."
    ),
    "taxes_weights": (
        "Taxes take a slice of operating profit before it becomes cash for the people who fund the company. The "
        "model uses the rate the company actually pays today for the forecast years and moves to the full "
        "statutory rate for the terminal value, since tax breaks tend not to last forever. Weights are "
        "different: they are not about the business but about you, the probability you give the bear, base and "
        "bull cases; they must add up to 100%, and the management case is never weighted because it is what the "
        "company says, not an independent view. Damodaran treats the weighted value as the expected value, the "
        "number to compare with the price."
    ),
}

INSTRUCTIONS = {
    "revenue_growth": "Check each case's growth path below, change the years you disagree with, then press Next.",
    "operating_margin": "Check each case's margin path below, change the years you disagree with, then press Next.",
    "reinvestment": "Check the sales-to-capital ratios and any per-year spending figures below, change what you "
                    "disagree with, then press Next.",
    "cost_of_capital": "Check the parts the rate is built from below, change what you disagree with, then press Next.",
    "terminal": "Check each case's terminal growth and return-on-capital premium below, change what you disagree with, "
                "then press Next.",
    "taxes_weights": "Check the tax rates and set the weight you give each case below, then press Next.",
}

PAGE_TITLES = {
    "start": "Start", "stories": "The stories", "revenue_growth": "Revenue growth",
    "operating_margin": "Operating margin", "reinvestment": "Reinvestment", "cost_of_capital": "Cost of capital",
    "terminal": "Terminal value", "taxes_weights": "Taxes and weights", "facts": "Facts check", "results": "Results",
}

START_TEXT = (
    "This walk takes you through the assumptions behind the valuation, one factor per page, in the order of how "
    "much each one moves the value for this company. On every page you read a short explanation, see the "
    "analyst's proposal and reasons for each case, and either accept the number or type your own. The value is "
    "recomputed after every change and appears in full on the last page, where you can save your edits back to "
    "the assumptions file."
)
HORIZON_TEXT = {
    10: ("The forecast runs ten years: five you set year by year, and five that ease toward the economy by rule, "
         "with growth sliding to the rate a mature business manages forever and the margin holding at your year-5 "
         "level. Next to every case you will also see what the same numbers are worth if the forecast stops at "
         "year 5 instead."),
    5: ("This company's forecast stops at year 5 and takes the terminal value there. Next to every case you will "
        "also see what the same numbers are worth over ten years, with growth easing to the terminal rate over "
        "years 6 to 10."),
}

STORIES_TEXT = (
    "Read the three stories first and decide whether the shape of each case makes sense to you: what has to be "
    "true for the bear, the base and the bull. Each story is headed by the two paths that define it, revenue "
    "growth and operating margin, year by year. You can rewrite a story here; the numbers come on the following "
    "pages. Agree with the shape before you touch a number."
)

FACTS_TEXT = (
    "These are the numbers the model starts from: the last twelve months of revenue and operating profit, the "
    "cash and debt that turn the value of the business into the value of the shares, and the parts of the cost "
    "of capital. They come from the filings, with a source for each. No judgment is asked here; only switch on "
    "Edit facts if a number is wrong against its source."
)

GLOSSARY = [
    ("Operating assets", "what the business itself is worth today: the forecast cash flows and the terminal value, "
                         "discounted back, before adding cash or subtracting debt."),
    ("Enterprise value", "what the market pays for the same thing today: the share price times the shares, plus debt "
                         "and other claims, minus cash."),
    ("Cost of capital", "the yearly return lenders and shareholders together could expect elsewhere for similar risk; "
                        "the rate future cash is discounted at."),
    ("Beta", "how much a business swings with the stock market; unlevered means before the effect of its debt, levered "
             "means after."),
    ("Reinvestment and sales-to-capital", "the spending needed to grow, sized as next year's revenue increase divided "
                                          "by sales-to-capital, the dollars of extra yearly revenue one dollar of "
                                          "spending buys."),
    ("Terminal value", "the value of every year after the forecast, treated as a business growing at one steady rate "
                       "forever; its share of operating assets shows how much rests on that assumption."),
    ("Return on capital", "after-tax operating profit divided by the capital invested in the business; the terminal "
                          "premium is how far above the cost of capital it stays forever."),
    ("Reference value", "a second value computed alongside each case with the other forecast length: a ten-year "
                        "forecast is shown against what it would be worth stopping at year 5, and a five-year "
                        "forecast against what it would be worth over ten years with growth easing to the terminal "
                        "rate. It shows what the choice of length is worth."),
    ("Weighted expected value", "the bear, base and bull values weighted by the probabilities you give them; the "
                                "number to compare with the price."),
]


# --------------------------------------------------------------------------- #
# Shared pieces
# --------------------------------------------------------------------------- #

def cases_in(doc: dict[str, Any]) -> list[str]:
    """bear, base, bull, then management when the YAML has it (computable or not)."""
    sc = doc.get("scenarios") or {}
    return [n for n in ("bear", "base", "bull", "management") if isinstance(sc.get(n), dict)]


def management_computable(doc: dict[str, Any]) -> bool:
    return bool(get_path(doc, "scenarios.management.computable"))


def case_header(doc: dict[str, Any], name: str) -> str:
    if name == "management":
        return "Management case (never weighted)"
    return f"{CASE_LABELS[name]} case, weight {pct(get_path(doc, f'scenarios.{name}.weight'), 0)}"


def guidance_table(doc: dict[str, Any]) -> None:
    guidance = get_path(doc, "scenarios.management.guidance") or []
    if guidance:
        static_table(pd.DataFrame([{"Item": g.get("item"), "Quote": g.get("quote"), "Source": g.get("source"),
                                    "Used as": g.get("used_as")} for g in guidance if isinstance(g, dict)]))
    else:
        st.caption("None recorded.")


def management_note(doc: dict[str, Any], *, with_guidance: bool) -> None:
    """The one-line note when the management case is not computed, with the guidance on record."""
    reason = get_path(doc, "scenarios.management.reason") or "no reason recorded"
    with st.container(border=True):
        st.markdown(f"**Management case: not computed.** {md(reason)}")
        if with_guidance:
            n = len(get_path(doc, "scenarios.management.guidance") or [])
            with st.expander(f"What management has said on record ({n} items)"):
                guidance_table(doc)


def explanation(page: str) -> None:
    with st.container(border=True):
        st.markdown(EXPLANATIONS[page])
    st.caption(INSTRUCTIONS[page])


def history_line(doc: dict[str, Any], cell: str, sentence: str) -> None:
    """One line from ``diagnostics.<cell>`` when it exists; nothing otherwise."""
    node = get_path(doc, f"diagnostics.{cell}")
    if not isinstance(node, dict) or node.get("value") is None:
        return
    source = node.get("source")
    st.markdown(f"**History:** {sentence.format(value=pct(node['value']))}" + (f" {md(source)}" if source else ""))
    if node.get("reason"):
        st.caption(md(node["reason"]))


def case_stop_note(ctx: Ctx, name: str) -> None:
    """Inside a case block: the engine's message, in plain words, when this case stops on the current inputs
    (a merely skipped management case is announced by its own note, not here)."""
    if ctx.result is None or name in ctx.result.scenarios:
        return
    why = "; ".join(ctx.result.stopped.get(name, []))
    if why:
        st.warning(md(stop_sentence(name, why, "not computed with the current inputs")))


def paths_table(doc: dict[str, Any], name: str, T: int) -> pd.DataFrame:
    """The two defining paths of a case as a small table: one row per year, columns revenue growth and
    operating margin (three columns, so it fits a third of the page)."""
    growth = get_path(doc, f"scenarios.{name}.revenue_growth.values") or []
    margin = get_path(doc, f"scenarios.{name}.operating_margin.values") or []

    def at(values: list[Any], t: int) -> str:
        return pct(values[t]) if t < len(values) and values[t] is not None else NA

    return pd.DataFrame([{"Year": f"Y{t + 1}", "Revenue growth": at(growth, t), "Operating margin": at(margin, t)}
                         for t in range(T)])


# --------------------------------------------------------------------------- #
# 1. Start
# --------------------------------------------------------------------------- #

def page_start(ctx: Ctx, tickers: list[str], on_company_change) -> None:
    doc = ctx.doc
    left, right = st.columns([1, 2])
    with left:
        st.selectbox("Company", tickers, index=tickers.index(ctx.ticker), key="company_pick", on_change=on_company_change)
    with right:
        st.markdown(f"**{md(doc.get('company') or ctx.ticker)}**, as of {md(doc.get('as_of_quarter'))} "
                    f"(cutoff {md(doc.get('as_of_date'))}); drafted {md(doc.get('drafted'))}"
                    + (f"; owner edited {md(doc.get('owner_edited'))}" if doc.get("owner_edited") else "") + ".")
        try:
            shown = ctx.path.relative_to(ctx.root)
        except ValueError:
            shown = ctx.path
        st.caption(f"Assumptions file: {shown}")
    st.markdown(START_TEXT + " " + HORIZON_TEXT.get(ctx.T, ""))
    st.subheader("Market inputs")
    market_boxes(doc, ctx.ticker)
    with st.expander("Length of the forecast (advanced; ten years is the default)"):
        horizon_control(doc)
    st.subheader("What moves the value for this company")
    ranking, error = ranking_for(doc, ctx.market)
    if ranking:
        base = ranking[0].base_per_share
        st.markdown("Each factor was nudged once, in the base case, and the change in value per share recorded. "
                    f"The base case as loaded is worth {per_share(base)} per share. The pages that follow come in "
                    "this order, except that revenue growth and operating margin are always first.")
        static_table(ranking_table(ranking))
        st.caption("Each term is explained on its own page.")
    else:
        st.info("The ranking is not available: " + (error or "the market inputs are incomplete")
                + ". The factor pages follow the default order.")
    with st.expander("Words used in this walk"):
        for term, meaning in GLOSSARY:
            st.markdown(f"**{term}**: {meaning}")


# --------------------------------------------------------------------------- #
# 2. The stories
# --------------------------------------------------------------------------- #

def _story_height(text: str, chars_per_line: int = 42) -> int:
    """A text area tall enough for its text: about ``chars_per_line`` per line at the column's width."""
    lines = sum(max(1, len(par) // chars_per_line + 1) for par in (text or "").splitlines()) + 1
    return int(min(720, max(120, 26 * lines + 40)))


def page_stories(ctx: Ctx) -> None:
    doc = ctx.doc
    st.markdown(STORIES_TEXT)
    stories = {name: get_path(doc, f"scenarios.{name}.story") or "" for name in WEIGHTED_SCENARIOS}
    height = max(_story_height(s) for s in stories.values())          # equal heights, so the columns end together
    cols = st.columns(3)
    for name, c in zip(WEIGHTED_SCENARIOS, cols):
        p = f"scenarios.{name}"
        with c, st.container(border=True):
            st.markdown(f"#### {CASE_LABELS[name]} case, {pct(get_path(doc, f'{p}.weight'), 0)}")
            static_table(paths_table(doc, name, ctx.explicit))
            clause = fade_clause(doc, name, ctx.T, ctx.market)
            if clause:
                st.caption(clause)
            w_text(doc, f"{p}.story", "Story (three to five plain sentences)", height=height,
                   convert=lambda x: (x or "").rstrip() + "\n" if (x or "").strip() else "")
    tail = (f" Years {ctx.explicit + 1} to {ctx.T} follow the rule quoted under each table."
            if ctx.explicit < ctx.T else "")
    st.caption(f"Y1 to Y{ctx.explicit} are the forecast years 1 to {ctx.explicit}.{tail}")
    with st.container(border=True):
        computable = management_computable(doc)
        status = ("computed as a fourth, unweighted case" if computable else "not computed, recorded only")
        st.markdown(f"#### Management case ({status})")
        if get_path(doc, "scenarios.management.story") is not None:
            text = get_path(doc, "scenarios.management.story") or ""
            w_text(doc, "scenarios.management.story", "What management has said, in a few sentences",
                   height=_story_height(text, 150),
                   convert=lambda x: (x or "").rstrip() + "\n" if (x or "").strip() else "")
        text = get_path(doc, "scenarios.management.reason") or ""
        label = "Why the management case is computed" if computable else "Why the management case is not computed"
        w_text(doc, "scenarios.management.reason", label, height=_story_height(text, 150))
        if computable:
            static_table(paths_table(doc, "management", ctx.explicit))
            clause = fade_clause(doc, "management", ctx.T, ctx.market)
            if clause:
                st.caption(clause)


# --------------------------------------------------------------------------- #
# 3. Revenue growth   4. Operating margin
# --------------------------------------------------------------------------- #

def _per_year_page(ctx: Ctx, page: str, cell: str, label: str) -> None:
    doc = ctx.doc
    explanation(page)
    if page == "revenue_growth":
        history_line(doc, "historical_revenue_cagr", "the company's own revenue grew {value} a year over the last five years.")
        if ctx.result is not None:
            st.markdown(f"**Base year:** revenue {money(ctx.result.base_year.revenue)} USD millions.")
    else:
        history_line(doc, "historical_operating_margin", "the company's own operating margin averaged {value} over the last five years.")
        if ctx.result is not None:
            st.markdown(f"**Base year:** adjusted operating margin {pct(ctx.result.base_year.margin)} on revenue of "
                        f"{money(ctx.result.base_year.revenue)} USD millions.")
    for name in cases_in(doc):
        if name == "management" and not management_computable(doc):
            management_note(doc, with_guidance=True)
            continue
        with st.container(border=True):
            st.markdown(f"#### {case_header(doc, name)}")
            reason_block(doc, f"scenarios.{name}.{cell}")
            st.markdown(f"**{label}**")
            year_boxes(doc, f"scenarios.{name}.{cell}", ctx.T)
            line = fade_line(doc, name, cell, ctx.T, ctx.market)
            if line:
                st.caption(line)
            case_stop_note(ctx, name)


def page_revenue_growth(ctx: Ctx) -> None:
    _per_year_page(ctx, "revenue_growth", "revenue_growth", "Revenue growth by year, in percent (20 means 20%)")


def page_operating_margin(ctx: Ctx) -> None:
    _per_year_page(ctx, "operating_margin", "operating_margin", "Operating margin by year, in percent of revenue")


# --------------------------------------------------------------------------- #
# Reinvestment
# --------------------------------------------------------------------------- #

def _override_echo(values: list[Any] | None, T: int) -> str:
    """'Year 1 173,970; Year 2 187,000; years 3-5 by the sales-to-capital rule'."""
    values = list(values or []) + [None] * T
    given = [(t, v) for t, v in enumerate(values[:T]) if v is not None]
    if not given:
        return "Every year follows the sales-to-capital rule."
    parts = [f"Year {t + 1} {money(v)}" for t, v in given]
    rule = [t + 1 for t, v in enumerate(values[:T]) if v is None]
    if rule:
        span = f"year {rule[0]}" if len(rule) == 1 else (f"years {rule[0]}-{rule[-1]}" if rule == list(range(rule[0], rule[-1] + 1))
                                                           else "years " + ", ".join(str(r) for r in rule))
        parts.append(f"{span} by the sales-to-capital rule")
    return "; ".join(parts) + "."


def page_reinvestment(ctx: Ctx) -> None:
    doc = ctx.doc
    explanation("reinvestment")
    for name in cases_in(doc):
        if name == "management" and not management_computable(doc):
            management_note(doc, with_guidance=True)
            continue
        p = f"scenarios.{name}"
        with st.container(border=True):
            st.markdown(f"#### {case_header(doc, name)}")
            reason_block(doc, f"{p}.sales_to_capital", title="Sales-to-capital")
            c1, c2, _c3, _c4 = st.columns(4)
            w_number(doc, f"{p}.sales_to_capital.value", "Years 1-5", container=c1, step=0.1,
                     help="Dollars of extra yearly revenue that one dollar of reinvestment buys, in the forecast years.")
            w_number(doc, f"{p}.sales_to_capital.value_late", "Years 6-10", container=c2, step=0.1,
                     help=("The same ratio for years 6 to 10." if ctx.T > EXPLICIT_YEARS else
                           "The same ratio for years 6 to 10 of the ten-year reference value."))
            reason_block(doc, f"{p}.reinvestment_override", title="Per-year spending figures")
            st.markdown("**Net reinvestment by year, USD millions (empty = use the sales-to-capital rule)**")
            year_boxes(doc, f"{p}.reinvestment_override", ctx.T, percent=False, fmt="%.0f", step=1000.0,
                       placeholder="rule")
            st.caption(_override_echo(get_path(doc, f"{p}.reinvestment_override.values"), ctx.T))
            case_stop_note(ctx, name)


# --------------------------------------------------------------------------- #
# Cost of capital
# --------------------------------------------------------------------------- #

COC_INPUTS = [("cost_of_capital.build.unlevered_beta", "Unlevered beta", "%.3f", 0.01),
              ("cost_of_capital.build.debt_to_equity_market", "Debt to equity (market values)", "%.4f", 0.005),
              ("cost_of_capital.build.pretax_cost_of_debt", "Pre-tax cost of debt (%)", "pct", 0.1)]


def coc_derived_rows(result: ValuationResult) -> list[tuple[str, str]]:
    c = result.cost_of_capital
    rows = [("Risk-free rate", pct2(c.risk_free)), ("Equity risk premium", pct2(c.equity_risk_premium))]
    if c.method == "build":
        rows += [("Unlevered beta" + (" (from the cached dataset)" if c.unlevered_beta_note else ""), num(c.unlevered_beta, 3)),
                 ("Debt to equity" + (" (derived from the bridge and the price)" if c.debt_to_equity_note else ""),
                  num(c.debt_to_equity, 4)),
                 ("Levered beta", num(c.levered_beta, 3)), ("Cost of equity", pct2(c.cost_of_equity)),
                 ("After-tax cost of debt", pct2(c.after_tax_cost_of_debt)),
                 ("Weights: equity / debt", f"{pct2(c.weight_equity)} / {pct2(c.weight_debt)}")]
    rows += [("Cost of capital", pct2(c.wacc)),
             (f"Terminal cost of capital ({TERMINAL_METHOD_WORDS.get(c.terminal_method, c.terminal_method).lower()})",
              pct2(c.terminal_wacc))]
    return rows


def page_cost_of_capital(ctx: Ctx) -> None:
    doc = ctx.doc
    explanation("cost_of_capital")
    with st.container(border=True):
        st.markdown("#### How the rate is built (shared by every case)")
        method = get_path(doc, "cost_of_capital.method") or "build"
        c1, c2, c3, c4 = st.columns(4)
        w_choice(doc, "cost_of_capital.method", "Method", ["build", "pinned"], words=METHOD_WORDS, container=c1,
                 help=METHOD_HELP)
        if ctx.market is not None:
            c3.metric("Risk-free rate", pct2(ctx.market.risk_free_rate), help="From the Start page.")
            c4.metric("Equity risk premium", pct2(ctx.market.equity_risk_premium), help="From the Start page.")
        if method == "pinned":
            w_pct(doc, "cost_of_capital.pinned_value", "Cost of capital (%)", container=c2, step=0.25)
        else:
            ind = get_path(doc, "cost_of_capital.build.damodaran_industry") or {}
            st.markdown(f"**Damodaran industry:** {md(ind.get('value') or NA)}. {md(ind.get('reason') or '')}")
            for path, label, fmt, step in COC_INPUTS:
                left, right = st.columns([1, 3])
                if fmt == "pct":
                    w_pct(doc, f"{path}.value", label, container=left, step=step)
                else:
                    w_number(doc, f"{path}.value", label, fmt=fmt, step=step, container=left)
                reason_block(doc, path, container=right)
        if ctx.result is not None:
            st.markdown("**Resulting rates**")
            static_table(pd.DataFrame(coc_derived_rows(ctx.result), columns=["Item", "Value"]))
            for w in ctx.result.cost_of_capital.warnings:
                st.caption(plain_message(w))
    with st.container(border=True):
        st.markdown("#### Per-case override (rare)")
        st.markdown("Cases share one cost of capital unless one has a reason for its own rate. Leave a box empty to use "
                    "the shared rate.")
        cols = st.columns(4)
        for name, c in zip(WEIGHTED_SCENARIOS, cols):
            w_pct(doc, f"scenarios.{name}.cost_of_capital_override", f"{CASE_LABELS[name]} (%)", container=c, step=0.25,
                  placeholder="shared")
        if management_computable(doc):
            w_pct(doc, "scenarios.management.cost_of_capital_override", "Management (%)", container=cols[3], step=0.25,
                  placeholder="shared")
        if ctx.result is not None:
            rates = [f"{CASE_LABELS[n]} {pct2(sc.inputs.wacc)}" for n, sc in ctx.result.scenarios.items()]
            st.caption("Each case discounts at: " + "; ".join(rates) + ".")
        for name in cases_in(doc):
            case_stop_note(ctx, name)


# --------------------------------------------------------------------------- #
# Terminal value
# --------------------------------------------------------------------------- #

def page_terminal(ctx: Ctx) -> None:
    doc = ctx.doc
    explanation("terminal")
    rf = ctx.market.risk_free_rate if ctx.market is not None else 0.0
    with st.container(border=True):
        st.markdown("#### Terminal cost of capital (shared by every case)")
        term = get_path(doc, "cost_of_capital.terminal") or {}
        st.markdown(md(term.get("reason")) if term.get("reason") else "*No reason given.*")
        c1, c2, _c3 = st.columns([3, 2, 1])
        w_choice(doc, "cost_of_capital.terminal.method", "Method", ["mature", "hold", "value"],
                 words=TERMINAL_METHOD_WORDS, container=c1, help=TERMINAL_METHOD_HELP)
        if term.get("method") == "value":
            w_pct(doc, "cost_of_capital.terminal.value", "Rate (%)", container=c2, step=0.25)
        elif term.get("method", "mature") == "mature":
            w_pct(doc, "market.mature_market_erp", "Mature premium (%)", container=c2, step=0.25,
                  help="The premium a mature company pays over the risk-free rate; Damodaran's default is 4.5%.")
        if ctx.result is not None:
            c = ctx.result.cost_of_capital
            st.markdown(f"**Resulting terminal cost of capital:** {pct2(c.terminal_wacc)} "
                        f"(company cost of capital {pct2(c.wacc)}; risk-free rate {pct2(c.risk_free)}).")
    for name in cases_in(doc):
        if name == "management" and not management_computable(doc):
            continue
        p = f"scenarios.{name}"
        with st.container(border=True):
            st.markdown(f"#### {case_header(doc, name)}")
            left, right = st.columns(2)
            with left:
                reason_block(doc, f"{p}.terminal.growth", title="Terminal growth")
                w_terminal_growth(doc, f"{p}.terminal.growth.value", rf)
                if not is_riskfree(get_path(doc, f"{p}.terminal.growth.value")):
                    w_bool(doc, f"{p}.terminal.growth.allow_above_riskfree", "Allow growth above the risk-free rate",
                           help="Needs a reason in the file; the engine then computes and warns.")
            with right:
                reason_block(doc, f"{p}.terminal.roic_premium", title="Terminal return on capital")
                w_pct(doc, f"{p}.terminal.roic_premium.value",
                      "Points above the terminal cost of capital (%; 0 = the moat is gone)", step=0.5,
                      help=("Zero in the bear case, where the advantage is gone." if name == "bear" else
                            f"Above {large_premium_ceiling(name) * 100:g} points this case needs the switch below "
                            "and a reason. Damodaran used 4 points for Alphabet in 2018 and 11.5 for Nvidia in 2023."))
                w_bool(doc, f"{p}.terminal.roic_premium.allow_large_premium", "Allow a large premium",
                       help=(f"Needed above {large_premium_ceiling(name) * 100:g} points in this case, with a reason "
                             "in the file; the engine then computes and warns."))
            if ctx.result is not None and name in ctx.result.scenarios:
                sc = ctx.result.scenarios[name]
                t = sc.terminal
                st.caption(f"This case: terminal growth {pct2(t.growth)}, terminal return on capital {pct2(t.roic)}, "
                           f"terminal cost of capital {pct2(t.wacc)}; the terminal value is {pct(sc.terminal_share)} "
                           "of operating assets.")
            case_stop_note(ctx, name)


# --------------------------------------------------------------------------- #
# Taxes and weights
# --------------------------------------------------------------------------- #

def page_taxes_weights(ctx: Ctx) -> None:
    doc = ctx.doc
    explanation("taxes_weights")
    if ctx.result is not None:
        st.markdown(f"**Base year:** effective tax rate {pct(ctx.result.base_year.effective_tax_rate)}; "
                    f"marginal (statutory) rate {pct(get_path(doc, 'market.marginal_tax_rate'))}.")
    for name in cases_in(doc):
        if name == "management" and not management_computable(doc):
            management_note(doc, with_guidance=True)
            continue
        p = f"scenarios.{name}"
        with st.container(border=True):
            st.markdown(f"#### {case_header(doc, name)}")
            reason_block(doc, f"{p}.tax_rate", title="Tax rate")
            c1, c2, c3, _c4 = st.columns(4)
            w_pct(doc, f"{p}.tax_rate.start", "Tax rate, forecast years (%)", container=c1, step=0.5)
            w_pct(doc, f"{p}.tax_rate.terminal", "Tax rate, terminal (%)", container=c2, step=0.5)
            if name != "management":
                w_pct(doc, f"{p}.weight", "Weight (%)", container=c3, step=5.0,
                      help="Your probability for this case; bear + base + bull must add up to 100%.")
            case_stop_note(ctx, name)
    weights = [get_path(doc, f"scenarios.{n}.weight") for n in WEIGHTED_SCENARIOS]
    if all(isinstance(w, (int, float)) for w in weights):
        total = sum(float(w) for w in weights)
        line = f"Weights add up to {pct(total, 0)}."
        if abs(total - 1.0) > 1e-6:
            st.error(line + " They must add up to 100% before the model computes.")
        else:
            st.markdown(f"**{line}**")


# --------------------------------------------------------------------------- #
# Facts check
# --------------------------------------------------------------------------- #

BASE_FACTS = [("base_year.revenue", "Revenue, trailing twelve months (USD millions)", "money"),
              ("base_year.operating_income_gaap", "Operating income, GAAP (USD millions)", "money"),
              ("base_year.amortization_of_acquired_intangibles", "Amortization of acquired intangibles (memo)", "money"),
              ("base_year.stock_based_compensation", "Stock-based compensation (memo)", "money"),
              ("base_year.rnd_expense", "Research and development expense (memo)", "money"),
              ("base_year.effective_tax_rate", "Effective tax rate", "pct"),
              ("base_year.invested_capital", "Invested capital (book equity + debt + leases - cash)", "money")]
BRIDGE_FACTS = [("bridge.cash_and_marketable_securities", "Cash and marketable securities (added)", "money"),
                ("bridge.debt", "Debt (subtracted)", "money"),
                ("bridge.operating_lease_liabilities", "Operating lease liabilities (subtracted)", "money"),
                ("bridge.minority_interests", "Minority interests (subtracted)", "money"),
                ("bridge.probability_of_failure", "Probability of failure", "pct"),
                ("bridge.distress_proceeds", "What the assets would fetch in a failure", "money"),
                ("bridge.diluted_shares", "Diluted shares (millions)", "shares")]
FORMATTERS = {"money": money, "pct": pct, "shares": shares}


def facts_table(doc: dict[str, Any], facts: list[tuple[str, str, str]], items: list[tuple[str, str]] | None = None,
                *, with_reasons: bool) -> None:
    rows = []

    def add(label: str, value: str, node: dict[str, Any]) -> None:
        row = {"Item": label, "Value": value}
        if with_reasons:
            row["Reason"] = node.get("reason") or ""
        row["Source"] = node.get("source") or ""
        rows.append(row)

    for path, label, kind in facts:
        node = get_path(doc, path)
        node = node if isinstance(node, dict) else {}
        add(label, FORMATTERS[kind](node.get("value")), node)
    for list_path, prefix in items or []:
        for item in get_path(doc, list_path) or []:
            if isinstance(item, dict):
                add(f"{prefix}: {item.get('name', '')}", money(item.get("value")), item)
    static_table(pd.DataFrame(rows))
    if with_reasons:
        details = [(label, get_path(doc, f"{path}.detail")) for path, label, _k in facts if get_path(doc, f"{path}.detail")]
        for label, detail in details:
            with st.expander(f"Working notes: {label}"):
                working_notes(detail)


def facts_editor(doc: dict[str, Any], facts: list[tuple[str, str, str]], items: list[tuple[str, str]] | None = None) -> None:
    for path, label, kind in facts:
        left, right = st.columns([1, 3])
        if kind == "pct":
            w_pct(doc, f"{path}.value", label, container=left, step=0.5)
        elif kind == "shares":
            w_number(doc, f"{path}.value", label, fmt="%.1f", step=1.0, container=left)
        else:
            w_number(doc, f"{path}.value", label, fmt="%.0f", step=10.0, container=left)
        reason_block(doc, path, container=right)
    for list_path, prefix in items or []:
        for i, item in enumerate(get_path(doc, list_path) or []):
            if not isinstance(item, dict):
                continue
            left, right = st.columns([1, 3])
            w_number(doc, f"{list_path}.{i}.value", f"{prefix}: {item.get('name', '')}", fmt="%.0f", step=10.0,
                     container=left)
            reason_block(doc, f"{list_path}.{i}", container=right)


def _on_off(x: Any) -> str:
    return "on" if x else "off"


def _lag_words(lag: Any) -> str:
    """The reinvestment-lag switch in words: how far ahead a year's spending buys growth."""
    try:
        n = int(lag)
    except (TypeError, ValueError):
        n = 1
    if n == 0:
        return "buys the same year's growth."
    if n == 1:
        return "buys the next year's growth."
    return f"buys the growth of {n} years later."


def page_facts(ctx: Ctx) -> None:
    doc = ctx.doc
    st.markdown(FACTS_TEXT)
    c1, c2, _c3, _c4 = st.columns(4)
    edit = c1.toggle("Edit facts", key="edit_facts",
                     help="Sourced numbers are read-only until this is on. Every edit is recorded in the change log on Save.")
    with_reasons = c2.toggle("Show reasons", key="show_reasons", value=False,
                             help="Adds the analyst's reason next to every number.") if not edit else True
    st.subheader("Base year: " + (get_path(doc, "base_year.period") or "period not given"))
    one_time = [("base_year.one_time_items", "One-time item")]
    if edit:
        facts_editor(doc, BASE_FACTS, one_time)
        st.markdown("**Switches** (they stay off unless the owner turns them on for a specific company)")
        c = st.columns(3)
        w_bool(doc, "switches.addback_acquired_amortization", "Add back amortization of acquired intangibles", container=c[0])
        w_bool(doc, "switches.capitalize_rnd", "Treat research spending as an investment", container=c[1])
        w_number(doc, "switches.rnd_amortization_years", "Years to write research spending off", fmt="%d", container=c[2])
        c2 = st.columns(3)
        w_number(doc, "switches.reinvestment_lag", "Years ahead that spending buys growth (0 to 3)", fmt="%d",
                 container=c2[0],
                 help="One year is the default, as in Damodaran's own template: this year's spending buys next "
                      "year's revenue increase. Zero credits the same year; two or three push it further out.")
    else:
        facts_table(doc, BASE_FACTS, one_time, with_reasons=with_reasons)
        sw = doc.get("switches") or {}
        lag = sw.get("reinvestment_lag", 1)
        st.caption(f"Switches: add back acquired amortization {_on_off(sw.get('addback_acquired_amortization'))}; "
                   f"treat research spending as an investment {_on_off(sw.get('capitalize_rnd'))} "
                   f"(written off over {sw.get('rnd_amortization_years', 5)} years); reinvestment "
                   + _lag_words(lag))
    if ctx.result is not None:
        by = ctx.result.base_year
        rows = [("Adjusted operating income (USD millions)", money(by.adjusted_operating_income)),
                ("Adjusted operating margin", pct(by.margin)),
                ("Invested capital used (USD millions)", money(by.invested_capital)),
                ("Base-year return on capital", pct(by.roic))]
        st.markdown("**Derived from the base year**")
        static_table(pd.DataFrame(rows, columns=["Item", "Value"]))

    st.subheader("Bridge from operating assets to equity")
    lists = [("bridge.non_operating_assets", "Non-operating asset (added)"), ("bridge.other_claims", "Other claim (subtracted)")]
    if edit:
        facts_editor(doc, BRIDGE_FACTS, lists)
        w_text(doc, "bridge.dilution_note", "Dilution note", height=90)
    else:
        facts_table(doc, BRIDGE_FACTS, lists, with_reasons=with_reasons)
        note = get_path(doc, "bridge.dilution_note")
        if note:
            st.caption("Dilution note: " + md(note))
    if ctx.result is not None and "base" in ctx.result.scenarios:
        sc, b = ctx.result.scenarios["base"], ctx.result.bridge
        st.markdown("**The bridge for the base case, USD millions**")
        rows = [("Operating assets", money(sc.operating_assets)),
                ("plus cash and marketable securities", money(b.cash)),
                ("plus non-operating assets", money(b.non_operating_assets)),
                ("minus debt", money(b.debt)), ("minus operating lease liabilities", money(b.leases)),
                ("minus minority interests", money(b.minority_interests)), ("minus other claims", money(b.other_claims)),
                ("equals equity value", money(sc.equity)), ("divided by diluted shares (millions)", shares(b.diluted_shares)),
                ("equals value per share (USD)", per_share(sc.per_share)),
                ("Enterprise value today (price x shares + claims - cash)", money(sc.enterprise_value))]
        static_table(pd.DataFrame(rows, columns=["Step", "Value"]))

    st.subheader("Cost of capital build")
    coc = doc.get("cost_of_capital") or {}
    if edit:
        c1, c2, _c3, _c4 = st.columns(4)
        w_choice(doc, "cost_of_capital.method", "Method", ["build", "pinned"], words=METHOD_WORDS, container=c1,
                 help=METHOD_HELP)
        w_pct(doc, "cost_of_capital.pinned_value", "Cost of capital (%; when the method is One number)", container=c2,
              step=0.25)
        left, right = st.columns([1, 3])
        w_line(doc, "cost_of_capital.build.damodaran_industry.value", "Damodaran industry", container=left)
        w_text(doc, "cost_of_capital.build.damodaran_industry.reason", "Reason", height=80, container=right)
        for path, label, fmt, step in COC_INPUTS:
            left, right = st.columns([1, 3])
            if fmt == "pct":
                w_pct(doc, f"{path}.value", label, container=left, step=step)
            else:
                w_number(doc, f"{path}.value", label, fmt=fmt, step=step, container=left)
            reason_block(doc, path, container=right)
        c1, c2, _c3, _c4 = st.columns(4)
        w_pct(doc, "market.mature_market_erp", "Mature-market equity risk premium (%)", container=c1, step=0.25)
        w_pct(doc, "market.marginal_tax_rate", "Marginal tax rate (%)", container=c2, step=0.5)
    else:
        rows = [{"Item": "Method", "Value": METHOD_WORDS.get(coc.get("method"), coc.get("method") or NA), "Reason": "", "Source": ""}]
        if coc.get("pinned_value") is not None:
            rows.append({"Item": "Cost of capital (one number)", "Value": pct2(coc.get("pinned_value")), "Reason": "", "Source": ""})
        ind = get_path(doc, "cost_of_capital.build.damodaran_industry") or {}
        rows.append({"Item": "Damodaran industry", "Value": ind.get("value") or NA, "Reason": ind.get("reason") or "", "Source": ""})
        for path, label, fmt, _step in COC_INPUTS:
            node = get_path(doc, path) or {}
            shown = pct2(node.get("value")) if fmt == "pct" else (NA if node.get("value") is None else fmt % float(node["value"]))
            rows.append({"Item": label, "Value": shown, "Reason": node.get("reason") or "", "Source": node.get("source") or ""})
        term = coc.get("terminal") or {}
        rows.append({"Item": "Terminal cost of capital method",
                     "Value": TERMINAL_METHOD_WORDS.get(term.get("method", "mature"), term.get("method", "mature")),
                     "Reason": term.get("reason") or "", "Source": ""})
        m = doc.get("market") or {}
        rows.append({"Item": "Mature-market equity risk premium", "Value": pct2(m.get("mature_market_erp")), "Reason": "",
                     "Source": "assumptions file, market section"})
        rows.append({"Item": "Marginal tax rate", "Value": pct(m.get("marginal_tax_rate")), "Reason": "",
                     "Source": "assumptions file, market section"})
        df = pd.DataFrame(rows)
        static_table(df if with_reasons else df.drop(columns=["Reason"]))
    if ctx.result is not None:
        st.markdown("**Derived: levered beta, cost of equity, cost of capital, terminal cost of capital**")
        static_table(pd.DataFrame(coc_derived_rows(ctx.result), columns=["Item", "Value"]))
        for w in ctx.result.cost_of_capital.warnings:
            st.caption(plain_message(w))
    sources_table(doc)


def sources_table(doc: dict[str, Any]) -> None:
    """The file's tag-to-cached-file list, when it has one: what every source tag on the pages points to."""
    entries = [e for e in (doc.get("sources") or []) if isinstance(e, dict)] if isinstance(doc.get("sources"), list) else []
    if not entries:
        return
    with st.expander(f"Where the numbers come from ({len(entries)} sources)"):
        st.markdown("Every source tag shown on these pages, the cached file it points to (inside the company's "
                    "folder) and the document date.")
        static_table(pd.DataFrame([{"Tag": e.get("tag") or "", "Cached file": e.get("file") or "",
                                    "Date": e.get("date") or "", "Note": e.get("note") or ""} for e in entries]))


# --------------------------------------------------------------------------- #
# Results
# --------------------------------------------------------------------------- #

def _year_by_year(result: ValuationResult) -> None:
    names = list(result.scenarios)
    name = st.selectbox("Case", names, index=names.index("base") if "base" in names else 0, key="yby_case",
                        format_func=lambda n: CASE_LABELS.get(n, n))
    sc = result.scenarios[name]
    explicit = sc.inputs.explicit_years or sc.inputs.horizon
    rows = []
    for r in sc.rows:
        rows.append({"Year": str(r.year) + (" (by rule)" if r.year > explicit else ""),
                     "Revenue": money(r.revenue), "Growth": pct(r.growth), "Margin": pct(r.margin),
                     "After-tax profit": money(r.ebit_after_tax),
                     "Reinvestment": money(r.reinvestment) + (" (given)" if r.reinvestment_source == "override" else ""),
                     "Free cash flow": money(r.fcff), "Present value": money(r.pv),
                     "Return on capital": pct(r.roic)})
    t = sc.terminal
    rows.append({"Year": "Terminal", "Revenue": money(t.revenue), "Growth": pct(t.growth), "Margin": pct(t.margin),
                 "After-tax profit": money(t.ebit_after_tax), "Reinvestment": money(t.reinvestment),
                 "Free cash flow": money(t.fcff), "Present value": money(t.pv), "Return on capital": pct(t.roic)})
    static_table(pd.DataFrame(rows))
    waccs = sorted({pct2(r.wacc) for r in sc.rows})
    marked = (f" Years 1 to {explicit} come from the assumptions; years {explicit + 1} to {sc.inputs.horizon} are "
              "marked 'by rule' and are built from the year-" + str(explicit) + " numbers."
              if explicit < sc.inputs.horizon else "")
    st.caption("All money in USD millions. The forecast years are discounted at " + " to ".join(waccs)
               + f" and the terminal year at {pct2(t.wacc)}.{marked} Terminal value {money(t.value)}; "
               f"present value {money(t.pv)}; share of operating assets {pct(sc.terminal_share)}.")


def _reverse(result: ValuationResult) -> None:
    a, r = result.analysis, result.analysis.reverse
    case = CASE_LABELS.get(a.scenario, a.scenario)
    rows = [("Enterprise value today (target, USD millions)", money(r.target_enterprise_value)),
            (f"Operating assets in the {case} case (USD millions)", money(r.base_operating_assets)),
            (f"Average revenue growth in the {case} case (years 1-5)", pct(r.base_average_growth)),
            ("Constant yearly growth that matches the price",
             pct(r.implied_growth) if r.implied_growth is not None else f"not found: {r.implied_growth_note}"),
            (f"Year-5 margin in the {case} case", pct(r.base_year5_margin)),
            ("Year-5 margin that matches the price",
             pct(r.implied_year5_margin) if r.implied_year5_margin is not None else f"not found: {r.implied_margin_note}")]
    static_table(pd.DataFrame(rows, columns=["Item", "Value"]))
    st.caption(f"The first solve keeps the {case} case's margins, reinvestment rule, cost of capital and terminal "
               "settings and asks what constant yearly revenue growth makes operating assets equal today's enterprise "
               "value. The second keeps the growth path and solves for the year-5 margin.")


def _diagnostics(result: ValuationResult) -> None:
    a = result.analysis
    if a.industry:
        f = a.industry
        st.markdown(f"**Industry figures** for '{md(f.industry)}' from the cached Damodaran datasets")

        def cell(v, fmt) -> str:
            if v.value is None:
                return md(v.note) if getattr(v, "note", None) else "not found"
            return fmt(v.value)

        rows = [("Unlevered beta corrected for cash", cell(f.unlevered_beta_cash_corrected, lambda x: num(x, 3)), f.unlevered_beta_cash_corrected.dataset_date or ""),
                ("Cost of capital", cell(f.cost_of_capital, pct2), f.cost_of_capital.dataset_date or ""),
                ("Sales to invested capital", cell(f.sales_to_capital, num), f.sales_to_capital.dataset_date or ""),
                ("Pre-tax operating margin", cell(f.pretax_operating_margin, pct), f.pretax_operating_margin.dataset_date or ""),
                ("Revenue growth, last 5 years", cell(f.revenue_cagr_5y, pct), f.revenue_cagr_5y.dataset_date or ""),
                ("Effective tax rate (money-making companies)", cell(f.effective_tax_rate, pct), f.effective_tax_rate.dataset_date or "")]
        static_table(pd.DataFrame(rows, columns=["Figure", "Value", "Dataset date"]))
    for d in a.diagnostics:
        st.markdown(f"**{md(d.title)}**" + ("  :red[flag]" if d.flag else ""))
        static_table(pd.DataFrame([(k, plain_message(v)) for k, v in d.rows], columns=["Item", "Value"]))
        if d.note:
            st.caption(md(d.note))


def _warnings(result: ValuationResult | None, error: str | None) -> None:
    if error:
        st.error(error[:1].upper() + error[1:])
    if result is None:
        return
    items = list(result.warnings)
    if result.analysis:
        items += [w for w in result.analysis.warnings if w not in items]
    items = [w for w in items if "(ignored)" not in w]              # validator notes about unknown keys are not the owner's business
    if not items:
        st.success("None.")
    for w in items:
        st.markdown(f"- {md(warning_sentence(w))}")


def _confirm_restart() -> None:
    st.session_state["confirm_restart"] = True


def _cancel_restart() -> None:
    st.session_state.pop("confirm_restart", None)


def page_results(ctx: Ctx) -> None:
    doc, result = ctx.doc, ctx.result
    if result is None:
        st.error("Not computed: " + (ctx.error or "the model has no result") + ".")
    else:
        static_table(results_table(result))
        for note in result_notes(result):
            st.caption(md(note))
        st.caption("Money in USD millions; value per share and price in USD. Operating assets is what the forecast "
                   "cash flows are worth today; enterprise value is what the market pays for the same thing.")
        chart = value_chart(result)
        if chart is not None:
            st.altair_chart(chart, **_WIDE)
            st.caption("The number on each bar is the value per share. The lighter label at the foot is the "
                       + (result.reference_label or "reference") + " reference: the same case with the other "
                       "forecast length, shown so the cost of the choice is visible.")
    stale = file_changed_on_disk(ctx.path)
    diff = [] if stale else unsaved_changes(doc, ctx.path)
    if stale:
        st.warning(STALE_BANNER)
    with st.expander("Sensitivity"):
        if result is None or result.analysis is None:
            st.info("Sensitivity grids appear once the model computes.")
        else:
            case = CASE_LABELS.get(result.analysis.scenario, result.analysis.scenario)
            st.caption(f"Both grids move the {case} case. The outlined cell is the case as entered.")
            for grid in result.analysis.grids:
                st.altair_chart(heatmap(grid), **_WIDE)
                st.caption(grid.note)
    with st.expander("Year by year"):
        if result is None or not result.scenarios:
            st.info("The year-by-year table appears once the model computes.")
        else:
            _year_by_year(result)
    with st.expander("Reverse DCF"):
        if result is None or result.analysis is None or result.analysis.reverse is None:
            st.info("The reverse DCF appears once the model computes.")
        else:
            _reverse(result)
    with st.expander("Diagnostics"):
        if result is None or result.analysis is None:
            st.info("Diagnostics appear once the model computes.")
        else:
            _diagnostics(result)
    with st.expander("Warnings", expanded=bool(result and result.warnings)):
        _warnings(result, ctx.error)
    with st.expander("Unsaved changes" if stale else f"Unsaved changes ({len(diff)})", expanded=bool(diff)):
        if stale:
            st.caption("Not listed: the file on disk is newer than the copy you loaded. Start over to reload it.")
        elif diff:
            static_table(changes_table(diff))
        else:
            st.caption("None. The working copy matches the file.")

    st.subheader("What to do now")
    st.markdown("**Save** keeps your numbers in the assumptions file, with a note in its change log. **Write the "
                "report** produces valuation.md from the saved file. **Record in the repository** commits both files "
                "so the history keeps them.")
    note_key = f"save_note:{ctx.ticker}"
    st.text_input("Note for the change log (one line, optional; saved with every changed cell)", key=note_key,
                  placeholder="why you changed these cells")
    c1, c2, c3, _c4 = st.columns(4)
    c1.button("Save to the assumptions file", key="save_btn", type="primary", disabled=stale or not diff,
              on_click=_save_cb, args=(ctx.root, ctx.ticker, ctx.path, note_key), **_WIDE)
    c2.button("Write the report (valuation.md)", key="write_btn", disabled=stale or bool(diff), on_click=_write_cb,
              args=(ctx.path,), **_WIDE)
    files, message = pending_commit(ctx.root, ctx.ticker)
    c3.button("Record in the repository", key="commit_btn", on_click=_commit_cb, args=(ctx.root, ctx.ticker), **_WIDE)
    if stale:
        c1.caption("Disabled: the file changed on disk. Start over to reload it.")
        c2.caption("Disabled until the file is reloaded.")
    elif diff:
        c1.caption(f"{len(diff)} change(s) waiting to be saved.")
        c2.caption("Disabled until you save, so the report always matches the file.")
    else:
        c1.caption("Nothing to save; the file matches what you see.")
        c2.caption("Archives the previous report and writes a new one from the saved file.")
    if message:
        names = ", ".join(sorted({Path(f).name for f in files}))
        c3.caption(f"Will commit {names} with the message '{message}'. Never pushes.")
    else:
        c3.caption("Nothing to record yet; everything under this company's valuation folder is already committed.")
    if st.session_state.get("last_output"):
        with st.expander("Output of the last report write"):
            st.code(st.session_state["last_output"])
    if st.session_state.get("git_output"):
        with st.expander("Output of the last commit", expanded=True):
            st.code(st.session_state["git_output"])
    with st.expander("Start over", expanded=stale):
        if stale:
            st.markdown("The assumptions file changed on disk. Start over reloads it and returns to Start; edits made in "
                        "this session are dropped.")
            st.button("Start over and reload the file", key="restart_btn", type="primary", on_click=_restart_cb,
                      args=(ctx.root, ctx.ticker))
        elif diff:
            st.markdown(f"Start over reloads the assumptions file from disk, drops your {len(diff)} unsaved change(s), and "
                        "returns to Start.")
            if st.session_state.get("confirm_restart"):
                st.warning("Are you sure? The unsaved changes listed above will be lost.")
                y, n, _a, _b = st.columns(4)
                y.button("Yes, discard and start over", key="restart_yes", type="primary", on_click=_restart_cb,
                         args=(ctx.root, ctx.ticker), **_WIDE)
                n.button("Cancel", key="restart_no", on_click=_cancel_restart, **_WIDE)
            else:
                st.button("Start over", key="restart_btn", on_click=_confirm_restart)
        else:
            st.markdown("Start over reloads the assumptions file from disk and returns to Start. Nothing is unsaved.")
            st.button("Start over", key="restart_btn", on_click=_restart_cb, args=(ctx.root, ctx.ticker))
