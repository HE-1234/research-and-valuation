"""The valuation walk: a guided, page-by-page editor for ``assumptions.yaml`` (AGENTS.md section 18.10).

Start it with ``uv run --extra app valuation-app``.  Ten pages: Start, The stories, Revenue
growth, Operating margin, then Reinvestment / Cost of capital / Terminal value / Taxes and
weights in the order of how much each moves this company's value (:mod:`valuation.impact`),
then Facts check and Results.  Back and Next at the bottom of every page, a clickable step
list in the sidebar, a progress line at the top.  Every change recomputes through
:func:`valuation.compute`; results appear in full only on the last page, where Save writes the
changed cells back through :mod:`valuation.yamlio`.

This file only routes.  State, widgets and callbacks live in :mod:`valuation.app_core`; the
pages in :mod:`valuation.app_pages`.
"""

from __future__ import annotations

import streamlit as st

from valuation.app_core import (
    _WIDE, STALE_BANNER, baseline_values, company_tickers, compute_result, explicit_years, file_changed_on_disk,
    horizon, load_company, market_inputs, ranking_for, readout_line, repo_root, working,
)
from valuation.app_pages import (
    PAGE_TITLES, Ctx, page_cost_of_capital, page_facts, page_operating_margin, page_reinvestment, page_results,
    page_revenue_growth, page_start, page_stories, page_taxes_weights, page_terminal,
)
from valuation.impact import page_order

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


def sidebar(pages: list[str], idx: int, readout: str) -> None:
    sb = st.sidebar
    sb.title("Valuation walk")
    sb.caption(f"{st.session_state['ticker']}: {working().get('company') or ''}")
    visited = st.session_state.setdefault("visited", {0})
    for i, page in enumerate(pages):
        label = f"{i + 1}. {PAGE_TITLES[page]}"
        if i == idx:
            sb.button(label, key=f"step_{i}", type="primary", icon=":material/arrow_forward:", **_WIDE)
        else:
            icon = ":material/check_circle:" if i in visited else ":material/radio_button_unchecked:"
            sb.button(label, key=f"step_{i}", icon=icon, on_click=_jump, args=(i,), **_WIDE)
    sb.divider()
    # results only when the assumptions have been walked through: no values before the factor pages
    if idx >= FIRST_FACTOR_PAGE:
        sb.caption(readout)
    else:
        sb.caption("The value per share appears here once the factor pages begin.")


def main() -> None:
    st.set_page_config(layout="wide", page_title="Valuation walk")
    root = repo_root()
    tickers = company_tickers(root)
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
    pages = ["start", "stories", *page_order(ranking), "facts", "results"]
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

    sidebar(pages, idx, readout)
    st.progress((idx + 1) / n, text=f"Step {idx + 1} of {n}: {PAGE_TITLES[page]}")
    st.header(PAGE_TITLES[page] if page != "start" else f"{ticker}: {doc.get('company') or ''}")
    for kind, k in (("success", "flash"), ("error", "flash_error")):
        msg = st.session_state.pop(k, None)
        if msg:
            getattr(st, kind)(msg)
    if error and page == "start" and market is not None:
        st.error("The model cannot compute yet: " + error + ".")
    if page != "results" and file_changed_on_disk(path):
        st.warning(STALE_BANNER)

    if page == "start":
        page_start(ctx, tickers, lambda: _company_cb(root))
    elif page == "stories":
        page_stories(ctx)
    elif page == "facts":
        page_facts(ctx)
    elif page == "results":
        page_results(ctx)
    else:
        FACTOR_PAGES[page](ctx)
        with st.container(border=True):
            st.markdown(readout)

    st.divider()
    back, _gap, nxt = st.columns([1, 4, 1])
    back.button("Back", key="back_btn", disabled=idx == 0, on_click=_go, args=(-1, n), **_WIDE)
    nxt.button("Next", key="next_btn", type="primary", disabled=idx == n - 1, on_click=_go, args=(1, n), **_WIDE)


main()
