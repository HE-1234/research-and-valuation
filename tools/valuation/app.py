"""A Mercury-inspired valuation workspace with fifteen focused pages.

Start with ``uv run --extra app valuation-app``. Grouped sidebar navigation and Back/Next
share the same session state. Assumptions precede dedicated valuation, analysis, forecast,
simulation, checks and review pages. Every calculated value comes from the existing engine.
This module only routes; state/widgets live in app_core and content in app_pages.
"""

from __future__ import annotations

from html import escape

import streamlit as st

from valuation.app_core import (
    _WIDE, STALE_BANNER, apply_style, baseline_values, company_tickers, compute_result, explicit_years, file_changed_on_disk,
    horizon, load_company, market_inputs, ranking_for, readout_line, repo_root, review_only, REVIEW_ONLY_NOTICE, working,
)
from valuation.app_pages import (
    PAGE_TITLES, Ctx, page_cost_of_capital, page_facts, page_operating_margin, page_reinvestment, page_results,
    page_revenue_growth, page_start, page_stories, page_taxes_weights, page_terminal,
    page_analysis, page_forecast, page_simulation, page_checks, page_review,
)
from valuation.impact import page_order
from valuation.app_workspace import live_panel
from valuation.app_sources import source_view

FACTOR_PAGES = {
    "revenue_growth": page_revenue_growth, "operating_margin": page_operating_margin,
    "reinvestment": page_reinvestment, "cost_of_capital": page_cost_of_capital,
    "terminal": page_terminal, "taxes_weights": page_taxes_weights,
}
# Streamlit keeps the scroll offset of its main container across reruns; after a page change the
# owner would otherwise land mid-page.  This runs once per page change and scrolls the parent to the top.
SCROLL_TOP = """<!-- page change NONCE --><script>
(function () {
  function up() {
    try {
      var doc = window.parent.document;
      var main = doc.querySelector('section[data-testid="stMain"]') || doc.querySelector('section.main')
                 || doc.querySelector('[data-testid="stAppViewContainer"]');
      if (main) { main.scrollTo(0, 0); main.scrollTop = 0; }
      window.parent.scrollTo(0, 0);
    } catch (e) {}
  }
  up(); setTimeout(up, 80); setTimeout(up, 250); setTimeout(up, 600);
  // Wait for the end marker: only animate a completed navigation, never an input rerun.
  try {
    var doc = window.parent.document;
    var reduced = window.parent.matchMedia('(prefers-reduced-motion: reduce)');
    if (reduced.matches) return;
    var observer, timeout, animation;
    function finish() {
      if (observer) observer.disconnect();
      clearTimeout(timeout);
    }
    function reveal() {
      var marker = doc.querySelector('[data-page-motion="NONCE"]');
      if (!marker) return;
      var page = marker.closest('.st-key-page_content');
      if (!page || typeof page.animate !== 'function') return;
      finish();
      if (reduced.matches) return;
      animation = page.animate(
        [{ opacity: 0.35, transform: 'translateY(8px)' }, { opacity: 1, transform: 'translateY(0)' }],
        { duration: 240, easing: 'cubic-bezier(0.16, 1, 0.3, 1)' }
      );
      // Changing the OS preference while moving also stops the effect immediately.
      reduced.addEventListener('change', function stop(event) {
        if (event.matches && animation) animation.cancel();
      }, { once: true });
    }
    observer = new MutationObserver(reveal);
    observer.observe(doc.body, { childList: true, subtree: true, attributes: true, attributeFilter: ['data-page-motion'] });
    timeout = setTimeout(finish, 5000);
    window.addEventListener('pagehide', finish, { once: true });
    reveal();
  } catch (e) { /* Motion is optional; navigation never depends on it. */ }
})();
</script>"""


def scroll_to_top(nonce: str) -> None:
    """Run the scroll script once per page change.  The nonce makes the iframe's content differ from the
    previous page's, so Streamlit reloads it instead of reusing the old frame; the retries run after the
    new page's elements have been drawn."""
    html = SCROLL_TOP.replace("NONCE", nonce)
    if hasattr(st, "iframe"):
        st.iframe(html, height=1)
    else:                                                   # pragma: no cover - older Streamlit
        import streamlit.components.v1 as components
        components.html(html, height=1)


def _go(delta: int, n: int) -> None:
    st.session_state["page"] = max(0, min(n - 1, st.session_state.get("page", 0) + delta))


def _jump(i: int) -> None:
    st.session_state["page"] = i


def _company_cb(root) -> None:
    ticker = st.session_state.get("company_pick")
    if ticker and ticker != st.session_state.get("ticker"):
        load_company(root, ticker, reset_walk=True)


FIRST_FACTOR_PAGE = 2          # Start and The stories come before any factor is reviewed


NAV_ICONS = {
    "start": "space_dashboard", "stories": "auto_stories", "revenue_growth": "trending_up",
    "operating_margin": "percent", "reinvestment": "rebase", "cost_of_capital": "account_balance",
    "terminal": "flag", "taxes_weights": "balance", "facts": "description", "results": "bar_chart",
    "analysis": "query_stats", "forecast": "table_chart", "simulation": "scatter_plot",
    "checks": "fact_check", "review": "save",
}


def sidebar(pages: list[str], idx: int, readout: str, ctx: Ctx, tickers: list[str]) -> None:
    sb = st.sidebar
    sb.markdown('<div class="workspace-brand"><span>V</span> Valuation</div>', unsafe_allow_html=True)
    sb.selectbox("Company", tickers, index=tickers.index(ctx.ticker), key="company_pick",
                 on_change=_company_cb, args=(ctx.root,))
    groups = [("Company", ["start", "stories"]), ("Assumptions", list(FACTOR_PAGES)),
              ("Evidence", ["facts"]), ("Explore", ["results", "analysis", "forecast", "simulation", "checks"]),
              ("Workspace", ["review"])]
    for title, members in groups:
        sb.markdown(f'<div class="nav-group">{title}</div>', unsafe_allow_html=True)
        for i, page in enumerate(pages):
            if page not in members:
                continue
            sb.button(PAGE_TITLES[page], key=f"step_{i}", type="primary" if i == idx else "secondary",
                      icon=f":material/{NAV_ICONS[page]}:", on_click=_jump, args=(i,), **_WIDE)
    sb.divider()
    sb.caption("Your changes stay in this session until you save.")
    if idx < FIRST_FACTOR_PAGE:
        sb.caption("The value per share appears here once the factor pages begin.")


def main() -> None:
    st.set_page_config(layout="wide", page_title="Valuation workspace", page_icon="◈")
    apply_style()
    root = repo_root()
    tickers = company_tickers(root)
    if source_view(root, tickers):
        return
    if not tickers:
        st.error(f"No companies/<TICKER>/valuation/assumptions.yaml found under {root}.")
        st.stop()
    if st.session_state.get("ticker") not in tickers:
        load_company(root, tickers[0], reset_walk=True)
    ticker = st.session_state["ticker"]
    doc, path = working(), st.session_state["path"]

    market = market_inputs(doc, ticker)
    st.session_state["market_inputs"] = market
    result, error = compute_result(doc, market)
    st.session_state["last_result"] = result
    baseline_values(result)
    ranking, _ranking_error = ranking_for(doc, market)
    pages = ["start", "stories", *page_order(ranking), "facts", "results",
             "analysis", "forecast", "simulation", "checks", "review"]
    n = len(pages)
    idx = max(0, min(n - 1, int(st.session_state.get("page", 0))))
    st.session_state["page"] = idx
    st.session_state.setdefault("visited", {0}).add(idx)
    page = pages[idx]
    T = horizon(doc)
    ctx = Ctx(root=root, ticker=ticker, path=path, doc=doc, market=market, result=result, error=error, T=T,
              explicit=explicit_years(doc, T))
    readout = readout_line(result, error, market)

    if st.session_state.get("last_page_rendered") != idx:
        st.session_state["last_page_rendered"] = idx
        st.session_state["scroll_seq"] = st.session_state.get("scroll_seq", 0) + 1
        scroll_to_top(f"{idx}-{st.session_state['scroll_seq']}")
    else:
        # Keep the same layout slot on reruns: removing the iframe shifted unkeyed
        # expanders and collapsed the simulation controls after their first edit.
        st.empty()

    sidebar(pages, idx, readout, ctx, tickers)
    st.markdown('<div class="workspace-context">' + escape(ticker) + ' / ' +
                escape(str(doc.get("company") or "")) + '</div>', unsafe_allow_html=True)
    st.header(PAGE_TITLES[page])
    if review_only():
        st.info(REVIEW_ONLY_NOTICE)
    if idx >= FIRST_FACTOR_PAGE:
        live_panel(ctx)
    st.progress((idx + 1) / n, text=f"Step {idx + 1} of {n}: {PAGE_TITLES[page]}")
    for kind, k in (("success", "flash"), ("error", "flash_error")):
        msg = st.session_state.pop(k, None)
        if msg:
            getattr(st, kind)(msg)
    if error and page == "start" and market is not None and not review_only():
        st.error("The model cannot compute yet: " + error + ".")
    if page != "review" and file_changed_on_disk(path):
        st.warning(STALE_BANNER)

    with st.container(key="page_content"):
        if page == "start":
            page_start(ctx, tickers, lambda: _company_cb(root))
        elif page == "stories":
            page_stories(ctx)
        elif page == "facts":
            page_facts(ctx)
        elif page == "results":
            page_results(ctx)
        elif page in {"analysis", "forecast", "simulation", "checks", "review"}:
            {"analysis": page_analysis, "forecast": page_forecast, "simulation": page_simulation,
             "checks": page_checks, "review": page_review}[page](ctx)
        else:
            FACTOR_PAGES[page](ctx)
            with st.container(border=True):
                st.markdown(readout)
        nonce = f"{idx}-{st.session_state['scroll_seq']}"
        st.markdown(f'<span data-page-motion="{nonce}" hidden></span>', unsafe_allow_html=True)

    st.divider()
    back, _gap, nxt = st.columns([1, 2, 1])
    back.button("Back", key="back_btn", disabled=idx == 0, on_click=_go, args=(-1, n), **_WIDE)
    nxt.button("Next" if idx == n - 1 else f"Next: {PAGE_TITLES[pages[idx + 1]]}", key="next_btn", type="primary", disabled=idx == n - 1, on_click=_go, args=(1, n), **_WIDE)


main()
