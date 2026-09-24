"""Simulation in the real Streamlit app: state, edits, failures and no implicit saves."""

from copy import deepcopy
from pathlib import Path

import pytest

pytest.importorskip("streamlit")
from .test_app import PAGES, assert_clean, go_to, repo, run_app  # noqa: F401,E402


def key(at, name):
    return f"mc:{at.session_state['load_seq']}:{name}"


def run(at):
    at.button(key=key(at, "run")).click().run()
    assert_clean(at)
    return at.session_state["simulation_workspace"]["result"]


def test_default_run_matches_current_case_and_writes_nothing(repo: Path):
    path = repo / "companies/EXMP/valuation/assumptions.yaml"
    saved = path.read_bytes()
    at = run_app()
    go_to(at, "simulation")
    assert at.button(key=key(at, "run"))
    assert not any(e.label == "Monte Carlo simulation" for e in at.expander)
    assert "result" not in at.session_state["simulation_workspace"]
    at.number_input(key=key(at, "draws")).set_value(12).run()
    result = run(at)
    assert result.summary.mean == at.session_state["last_result"].scenarios["base"].per_share
    assert result.summary.valid == 12 and result.summary.standard_deviation == 0
    assert any("conditional on valid draws" in c.value for c in at.caption)
    assert any("no company calibration" in c.value for c in at.caption)
    assert any("Standard deviation" in str(t.value) for t in at.table)
    assert path.read_bytes() == saved
    assert not path.with_name("valuation.md").exists()
    assert not path.with_name("assumptions.md").exists()


def test_seeded_run_and_navigation_preserve_controls_but_invalidate_edited_case(repo: Path):
    at = run_app()
    go_to(at, "simulation")
    at.number_input(key=key(at, "draws")).set_value(30).run()
    at.number_input(key=key(at, "growth_minimum")).set_value(-2.).run()
    at.number_input(key=key(at, "growth_maximum")).set_value(3.).run()
    at.text_input(key=key(at, "growth_reason")).input("Exploratory demand range, not calibrated.").run()
    first = deepcopy(run(at))
    assert first.settings.growth_shift.minimum == -.02 and first.settings.growth_shift.maximum == .03
    assert run(at).draws == first.draws
    at.number_input(key=key(at, "seed")).set_value(99).run()
    assert any("Run again" in i.value for i in at.info)
    assert not any("Standard deviation" in str(t.value) for t in at.table)
    assert run(at).draws != first.draws
    at.button(key="step_2").click().run()
    gen = at.session_state["gen"]
    at.number_input(key=f"w{gen}:scenarios.base.revenue_growth.values.0").set_value(25.).run()
    at.button(key=f"step_{PAGES.index('simulation')}").click().run()
    assert_clean(at)
    assert at.number_input(key=key(at, "growth_minimum")).value == -2.
    assert at.text_input(key=key(at, "growth_reason")).value.startswith("Exploratory")
    assert any("Run again" in i.value for i in at.info)
    latest = run(at)
    assert latest.snapshot["inputs"]["growth"][0] == .25
    assert latest.deterministic_per_share == at.session_state["last_result"].scenarios["base"].per_share
    assert latest.fingerprint != first.fingerprint


def test_case_settings_and_reload_are_isolated(repo: Path):
    at = run_app()
    go_to(at, "simulation")
    at.number_input(key=key(at, "draws")).set_value(5).run()
    run(at)
    at.selectbox(key=key(at, "scenario")).set_value("bull").run()
    assert any("Run again" in i.value for i in at.info)
    changed = run(at)
    assert changed.settings.scenario == "bull"
    assert changed.summary.mean == at.session_state["last_result"].scenarios["bull"].per_share
    go_to(at, "review")
    at.button(key="restart_btn").click().run()
    assert_clean(at)
    go_to(at, "simulation")
    assert "result" not in at.session_state["simulation_workspace"]
    assert at.number_input(key=key(at, "draws")).value == 2000


@pytest.mark.parametrize("minimum,mode,maximum,outcome", [(60., 70., 80., "partial"),
                                                        (100., 100., 100., "invalid"),
                                                        (-100., -100., -100., "negative")])
def test_failed_and_negative_draws_are_visible(repo: Path, minimum, mode, maximum, outcome):
    at = run_app()
    go_to(at, "simulation")
    at.number_input(key=key(at, "draws")).set_value(40).run()
    for name, v in (("minimum", minimum), ("mode", mode), ("maximum", maximum)):
        at.number_input(key=key(at, "margin_" + name)).set_value(v).run()
        assert_clean(at)
    result = run(at)
    if outcome == "invalid":
        assert result.summary.valid == 0
        assert any("No valid draws" in e.value for e in at.error)
        assert not any("Standard deviation" in str(t.value) for t in at.table)
    elif outcome == "partial":
        assert 0 < result.summary.valid < 40
        assert any("subset" in w.value and "biased" in w.value for w in at.warning)
        assert any("invalid" in c.value and "Attempted 40" in c.value for c in at.caption)
    else:
        assert result.summary.negative_values == 40
        assert any("negative equity" in w.value for w in at.warning)


def test_invalid_settings_and_stale_file_never_show_old_result(repo: Path):
    at = run_app()
    go_to(at, "simulation")
    at.number_input(key=key(at, "draws")).set_value(3).run()
    run(at)
    at.number_input(key=key(at, "capital_minimum")).set_value(0.).run()
    assert at.button(key=key(at, "run")).disabled
    assert any("must be positive" in e.value for e in at.error)
    assert not any("Standard deviation" in str(t.value) for t in at.table)
    at.number_input(key=key(at, "capital_minimum")).set_value(1.).run()
    at.selectbox(key=key(at, "margin_dependency")).set_value("same_rank").run()
    assert at.button(key=key(at, "run")).disabled
    assert any("varying growth" in e.value for e in at.error)
    path = repo / "companies/EXMP/valuation/assumptions.yaml"
    path.write_text(path.read_text() + "\n# External edit.\n")
    at.run()
    assert_clean(at)
    assert any("Reload the company before simulating" in i.value for i in at.info)
    assert not any(b.label == "Run simulation" for b in at.button)
    assert not any("Standard deviation" in str(t.value) for t in at.table)
