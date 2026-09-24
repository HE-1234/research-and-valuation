"""Results-page controls and presentation; all simulation arithmetic is engine-side."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any
import inspect

import altair as alt
import pandas as pd
import streamlit as st

from valuation.app_core import _WIDE, CASE_LABELS, md, pct, pct2, per_share, plain_message, static_table
from valuation.simulation import (
    DEPENDENCIES, MAX_DRAWS, SimulationError, SimulationResult, SimulationSettings, Triangle,
    histogram, simulate, simulation_fingerprint,
)

if TYPE_CHECKING:
    from valuation.app_pages import Ctx


DEPENDENCY_LABELS = {
    "independent": "Independent draws",
    "same_rank": "Same rank as growth",
    "opposite_rank": "Opposite rank to growth",
}


def simulation_expander():
    # New Streamlit versions support stable expander keys. Older supported versions
    # keep their ordinary expander behavior without receiving an unsupported option.
    options = {"key": "monte_carlo_panel"} if "key" in inspect.signature(st.expander).parameters else {}
    return st.expander("Monte Carlo simulation", **options)


def _number(state: dict[str, Any], prefix: str, name: str, label: str, default, *, container=None, **kwargs):
    value = (container or st).number_input(label, value=state.get(name, default), key=prefix + name, **kwargs)
    state[name] = value
    return value


def _text(state: dict[str, Any], prefix: str, name: str, label: str) -> str:
    value = st.text_input(label, value=state.get(name, ""), key=prefix + name)
    state[name] = value
    return value


def _triangle(state: dict[str, Any], prefix: str, name: str, title: str, explanation: str,
              default: float, scale: float) -> Triangle:
    st.markdown(f"**{title}**")
    st.caption(explanation)
    columns = st.columns(3)
    values = [_number(state, prefix, f"{name}_{part}", label, default, container=col,
                      format="%.2f", step=0.1 if scale == 100 else 0.05)
              for part, label, col in zip(("minimum", "mode", "maximum"),
                                          ("Minimum", "Most likely", "Maximum"), columns)]
    reason = _text(state, prefix, f"{name}_reason", f"Reason or evidence for {title.lower()} (optional)")
    return Triangle(*(v / scale for v in values), reason=reason)


def _dependency(state: dict[str, Any], prefix: str, name: str, label: str) -> str:
    value = st.selectbox(label, DEPENDENCIES, index=DEPENDENCIES.index(state.get(name, "independent")),
                         format_func=DEPENDENCY_LABELS.get, key=prefix + name)
    state[name] = value
    return value


def distribution_chart(run: SimulationResult) -> alt.LayerChart:
    bins = pd.DataFrame(histogram(run))
    bars = alt.Chart(bins).mark_bar(color="#187568", opacity=0.8).encode(
        x=alt.X("lower:Q", bin="binned", title="Value per share (USD)", scale=alt.Scale(zero=False)),
        x2="upper:Q", y=alt.Y("count:Q", title="Valid draws", axis=alt.Axis(tickMinStep=1)),
        tooltip=[alt.Tooltip("lower:Q", title="From USD", format=",.2f"),
                 alt.Tooltip("upper:Q", title="To USD", format=",.2f"),
                 alt.Tooltip("count:Q", title="Draws", format=",")],
    )
    markers = pd.DataFrame([
        {"value": run.deterministic_per_share, "Reference": "Selected case"},
        {"value": run.snapshot["market"]["price"], "Reference": "Market price"},
    ])
    lines = alt.Chart(markers).mark_rule(strokeWidth=2, strokeDash=[5, 3]).encode(
        x="value:Q", color=alt.Color("Reference:N", title=None,
                                    scale=alt.Scale(domain=["Selected case", "Market price"],
                                                    range=["#145dc0", "#ab5a21"])),
        tooltip=["Reference:N", alt.Tooltip("value:Q", title="USD", format=",.2f")],
    )
    return (bars + lines).properties(height=290).configure_legend(orient="bottom")


def _show_result(run: SimulationResult, prefix: str, workspace: dict[str, Any]) -> None:
    summary = run.summary
    st.markdown("**Simulation results**")
    st.caption(f"Attempted {summary.attempted:,}; valid {summary.valid:,}; invalid {summary.invalid:,}. "
               f"Seed {run.settings.seed}; {CASE_LABELS.get(run.settings.scenario, run.settings.scenario)} case. "
               "All statistics below are conditional on valid draws and the selected assumptions.")
    if summary.invalid:
        st.warning("Some draws could not be valued. The chart and statistics describe only the valid subset, "
                   "which may be biased. No draws were replaced and no input or value was clipped.")
        static_table(pd.DataFrame([{"Reason": plain_message(reason), "Draws": count}
                                   for reason, count in run.invalid_reasons.items()]))
    if not summary.valid:
        st.error("No valid draws. Revise the ranges or starting case; no distribution statistics are available.")
    else:
        st.altair_chart(distribution_chart(run), **_WIDE)
        rows = [
            ("Selected case before uncertainty", per_share(run.deterministic_per_share)),
            ("Market price", per_share(run.snapshot["market"]["price"])),
            ("Mean", per_share(summary.mean)), ("Median (50th percentile)", per_share(summary.median)),
            ("10th percentile", per_share(summary.p10)), ("90th percentile", per_share(summary.p90)),
            ("Standard deviation", per_share(summary.standard_deviation)),
            ("Lowest observed", per_share(summary.minimum)), ("Highest observed", per_share(summary.maximum)),
        ]
        static_table(pd.DataFrame(rows, columns=["Measure", "USD per share"]))
        st.markdown(f"**{pct(summary.fraction_above_price)} of valid draws exceed the market price** "
                    f"({summary.above_price:,} of {summary.valid:,}). This is a frequency under your assumptions, "
                    "not a probability of earning a return or a forecast of the share price.")
        st.caption("The 10th-to-90th percentile range describes these assumed outcomes; it is not a confidence "
                   "interval. Percentiles interpolate between sorted values; standard deviation describes the "
                   "full simulated sample. More draws reduce sampling noise, not uncertainty about the business.")
        if summary.minimum == summary.maximum:
            st.caption("All valid draws have the same value. The bar has width only to make that point visible.")
        if summary.negative_values:
            st.warning(f"{summary.negative_values:,} valid draws have negative equity value after the existing "
                       "cash-and-debt bridge. These values are retained model residuals, not negative traded "
                       "share prices or simulated default events.")
        if summary.transition_flags:
            st.warning(f"{summary.transition_flags:,} valid draws trigger the existing terminal-transition "
                       "diagnostic. They remain in the distribution; inspect the growth, investment and mature "
                       "return assumptions together. The warning is not a probability of failure.")
        else:
            st.caption("No terminal-transition flags in valid draws. The same checks apply to every case; "
                       "passing this check does not establish economic plausibility.")
    st.download_button("Download simulation and all draws", data=workspace["export"],
                       file_name=f"{run.snapshot['ticker']}-{run.settings.scenario}-simulation.json",
                       mime="application/json", key=prefix + "download")
    st.caption("Download includes settings, your reasons, the input snapshot, every attempted draw, errors and "
               "summary statistics. Settings stay in this app session; Save and Write the report cover the "
               "deterministic valuation. Reloading the company resets the simulation.")


def simulation_panel(ctx: Ctx, *, stale: bool = False) -> None:
    """Render inside the Results expander, running only on an explicit button click."""
    st.markdown("Explore uncertainty around one case using the same valuation model. Each draw varies a full "
                "business path and recomputes the cash flows. Results use the current working inputs, including "
                "unsaved edits, and are conditional on this case and the ranges you choose.")
    if stale:
        st.info("Reload the company before simulating: the assumptions file changed on disk.")
        return
    if ctx.result is None or not ctx.result.scenarios:
        st.info("Simulation becomes available when a case can be computed.")
        return
    workspace = st.session_state.setdefault("simulation_workspace", {"controls": {}})
    state = workspace["controls"]
    prefix = f"mc:{st.session_state.get('load_seq', 0)}:"
    names = list(ctx.result.scenarios)
    previous = state.get("scenario", "base")
    name = st.selectbox("Case to simulate", names, index=names.index(previous) if previous in names else 0,
                        format_func=lambda n: CASE_LABELS.get(n, n), key=prefix + "scenario")
    state["scenario"] = name
    inp = ctx.result.scenarios[name].inputs
    st.caption("User-selected judgment distributions; no company calibration is supplied. The initial zero "
               "shifts and multiplier of one reproduce the selected case without uncertainty.")
    with st.popover("What is a triangular distribution?"):
        st.markdown("A bounded distribution with its highest density at the most likely value and less density "
                    "toward each end; the three numbers are hard bounds and a mode, not percentiles.")
        st.caption("Asymmetric bounds can change the average input. The value of central inputs need not equal "
                   "the simulation mean because valuation is nonlinear.")

    growth = _triangle(state, prefix, "growth", "Revenue-growth shift (percentage points)",
                       "Added to each authored growth year. For an automatic ten-year fade, the last five "
                       "years are rebuilt to reach the existing terminal growth; a written ten-year path keeps "
                       "its shape. A shift of 2 turns 10% into 12%.", 0.0, 100)
    margin = _triangle(state, prefix, "margin", "Year-5 margin shift (percentage points)",
                       "One fifth of the shift in year 1, building to the full shift in year 5 and later. "
                       "The existing late margin shape stays intact, and the final margin also sets terminal profit.",
                       0.0, 100)
    capital = _triangle(state, prefix, "capital", "Capital-efficiency multiplier",
                        "Multiplies both sales-to-capital ratios: 1 leaves them unchanged; 1.2 means 20% more "
                        "revenue per dollar invested. Reinvestment follows the sampled growth and these ratios, "
                        "with the existing lag. Every bound must be positive.", 1.0, 1)
    override_years = [str(i + 1) for i, v in enumerate(inp.reinvestment_override[:inp.horizon]) if v is not None]
    if override_years:
        st.info("Spending overrides stay fixed in years " + ", ".join(override_years) + ". Changing capital "
                "efficiency does not change spending in those years; growth can still change their eventual "
                "productivity. Review whether these commitments fit your range.")

    st.markdown("**Dependencies between inputs**")
    st.caption("Each driver is drawn once for the entire path. Independent draws are an explicit assumption, "
               "not an estimated correlation. Rank links impose perfect positive or negative rank dependence, "
               "not a fitted relationship. If both drivers link to growth, they also link to each other.")
    margin_link = _dependency(state, prefix, "margin_dependency", "Margin relative to growth")
    capital_link = _dependency(state, prefix, "capital_dependency", "Capital efficiency relative to growth")
    dependence_reason = _text(state, prefix, "dependence_reason", "Reason for the dependencies (optional)")
    st.caption("Same rank pairs high growth with high margin or high capital efficiency. Opposite rank pairs "
               "high growth with low margin or low capital efficiency. Choose the business mechanism you mean; "
               "if unsure, explore one uncertain driver at a time.")
    columns = st.columns(2)
    draws = _number(state, prefix, "draws", "Number of draws", 2_000, container=columns[0],
                    min_value=1, max_value=MAX_DRAWS, step=100)
    seed = _number(state, prefix, "seed", "Random seed", 42, container=columns[1],
                   min_value=0, max_value=2**32 - 1, step=1,
                   help="The same seed, settings and input snapshot reproduce the same draws.")
    with st.expander("Starting path and fixed assumptions"):
        static_table(pd.DataFrame({"Year": list(range(1, inp.horizon + 1)),
                                    "Growth": [pct(x) for x in inp.growth],
                                    "Margin": [pct(x) for x in inp.margin]}))
        st.caption(f"Sales-to-capital: {inp.sales_to_capital:.2f} early, {inp.sales_to_capital_late:.2f} late. "
                   f"Reinvestment lag: {inp.reinvestment_lag} year(s). Cost of capital: {pct2(inp.wacc)}, "
                   f"terminal {pct2(inp.terminal_wacc)}. Terminal growth: {pct2(inp.terminal_growth)}; "
                   f"terminal return on capital: {pct2(inp.terminal_wacc + inp.roic_premium)}.")
        st.markdown("Taxes, financing rates, terminal growth and the return premium, cash, debt, shares and the "
                    "existing distress adjustment stay fixed. Terminal reinvestment is still derived from "
                    "growth and return on capital. These ranges do not model every business or market risk.")
        story = ctx.doc["scenarios"][name].get("story")
        if story:
            st.markdown(md(story))
        st.caption("Method: Damodaran's simulation principles; the three drivers, path shifts and rank choices "
                   "are this app's design. Mechanical input bounds do not establish economic plausibility.")
        st.markdown("[Damodaran: simulation steps and limitations]"
                    "(https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/probabilistic.pdf)")

    settings = SimulationSettings(name, draws, seed, growth, margin, capital, margin_link, capital_link,
                                  dependence_reason)
    error = None
    try:
        settings.validate()
    except SimulationError as exc:
        error = str(exc)
        st.error(error)
    if st.button("Run simulation", key=prefix + "run", disabled=bool(error)):
        workspace.pop("result", None)
        workspace.pop("export", None)
        try:
            with st.spinner("Simulating the selected case..."):
                run = simulate(ctx.result, settings)
                workspace["export"] = run.to_json()
                workspace["result"] = run
        except SimulationError as exc:
            st.error(str(exc))
    old_run = workspace.get("result")
    if old_run is not None:
        if error or old_run.fingerprint != simulation_fingerprint(ctx.result, settings):
            st.info("Inputs or simulation settings changed. Run again to see a current distribution.")
        else:
            _show_result(old_run, prefix, workspace)
