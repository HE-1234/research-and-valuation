"""Economic identities, sampling semantics, invalid draws, and summary reconciliation."""

from copy import deepcopy
from dataclasses import asdict, replace
import json
import math
from pathlib import Path
import random
import statistics

import pytest

from valuation import MarketInputs, SimulationError, SimulationSettings, Triangle, simulate
from valuation.analysis import transition_flag
from valuation.engine import compute, faded_growth, run_scenario
from valuation.schema import GROWTH_BOUNDS, MARGIN_BOUNDS, load_yaml
from valuation.simulation import empirical_quantile, histogram, simulation_fingerprint


@pytest.fixture
def doc():
    return load_yaml(Path(__file__).parent / "fixtures" / "example_assumptions.yaml")


def value(doc):
    return compute(doc, MarketInputs(70, 0.0425, 0.045))


def uncertain(**kwargs):
    return replace(SimulationSettings(draws=120, seed=1729,
                                     growth_shift=Triangle(-0.05, 0.0, 0.07),
                                     margin_shift=Triangle(-0.03, 0.0, 0.05),
                                     capital_multiplier=Triangle(0.8, 1.0, 1.3)), **kwargs)


@pytest.mark.parametrize("horizon", [5, 10])
@pytest.mark.parametrize("case", ["bear", "base", "bull", "management"])
def test_zero_uncertainty_equals_deterministic_cash_flows_terminal_and_value(doc, horizon, case):
    doc["horizon"] = horizon
    result = value(doc)
    expected = result.scenarios[case]
    run = simulate(result, SimulationSettings(scenario=case, draws=5))
    for draw in run.draws:
        assert draw.inputs == expected.inputs
        assert draw.per_share == expected.per_share
        actual = run_scenario(draw.inputs, result.base_year, result.bridge, result.market.price)
        assert actual.rows == expected.rows
        assert actual.terminal == expected.terminal
    assert run.summary.mean == run.summary.median == run.summary.p10 == run.summary.p90 == expected.per_share
    assert run.summary.standard_deviation == 0
    assert run.summary.invalid == 0
    bins = histogram(run)
    assert len(bins) == 1 and bins[0]["count"] == 5


@pytest.mark.parametrize("lag", range(4))
def test_linked_paths_preserve_growth_reinvestment_and_terminal_identities(doc, lag):
    doc["horizon"] = 10
    doc["switches"]["reinvestment_lag"] = lag
    case = doc["scenarios"]["base"]
    # The mixed path lengths in MRVL bull: rebuilding growth must not flatten margins.
    case["operating_margin"]["values"] = [0.18, 0.21, 0.24, 0.26, 0.3, 0.29, 0.28, 0.27, 0.26, 0.25]
    case["reinvestment_override"] = {"values": [100, 120, None, None, None]}
    doc["bridge"]["probability_of_failure"] = {"value": 0.12, "reason": "test"}
    doc["bridge"]["distress_proceeds"] = {"value": 200, "reason": "test"}
    result = value(doc)
    original = result.scenarios["base"].inputs
    run = simulate(result, uncertain(margin_dependency="same_rank", capital_dependency="opposite_rank"))
    for draw in run.draws:
        inp = draw.inputs
        assert inp.growth[:5] == [g + draw.growth_shift for g in original.growth[:5]]
        assert inp.growth[5:] == faded_growth(inp.growth[4], original.terminal_growth)
        assert inp.growth[-1] == original.terminal_growth
        assert inp.margin == [m + draw.margin_shift * min(t, 5) / 5
                              for t, m in enumerate(original.margin, 1)]
        assert inp.sales_to_capital_late / inp.sales_to_capital == pytest.approx(
            original.sales_to_capital_late / original.sales_to_capital)
        for field in ("tax_start", "tax_terminal", "wacc", "terminal_wacc", "terminal_growth", "roic_premium",
                      "reinvestment_lag", "reinvestment_override"):
            assert getattr(inp, field) == getattr(original, field)
        assert draw.ranks[1] == draw.ranks[0] and draw.ranks[2] == 1 - draw.ranks[0]
        assert run.settings.margin_shift.quantile(draw.ranks[0]) == draw.margin_shift
        assert run.settings.capital_multiplier.quantile(1 - draw.ranks[0]) == draw.capital_multiplier
        actual = run_scenario(inp, result.base_year, result.bridge, result.market.price)
        revenues = [result.base_year.revenue] + [row.revenue for row in actual.rows]
        for _ in range(max(1, lag)):
            revenues.append(revenues[-1] * (1 + inp.terminal_growth))
        for row in actual.rows:
            if row.year <= 2:
                assert row.reinvestment == [100, 120][row.year - 1]
            else:
                t = row.year
                assert row.reinvestment == pytest.approx((revenues[t + lag] - revenues[t + lag - 1]) /
                                                         row.sales_to_capital)
            assert GROWTH_BOUNDS[0] <= row.growth <= GROWTH_BOUNDS[1]
            assert MARGIN_BOUNDS[0] <= row.margin <= MARGIN_BOUNDS[1]
        terminal = actual.terminal
        assert terminal.roic == inp.terminal_wacc + inp.roic_premium
        assert terminal.reinvestment_rate == inp.terminal_growth / terminal.roic
        assert terminal.fcff == pytest.approx(terminal.ebit_after_tax * (1 - terminal.reinvestment_rate))
        assert actual.operating_assets == pytest.approx(actual.going_concern_value * .88 + 200 * .12)


def test_authored_ten_year_growth_and_zero_premium_terminal_identity(doc):
    doc["horizon"] = 10
    case = doc["scenarios"]["bear"]
    case["revenue_growth"]["values"] += [.06, .05, .04, .035, .03]
    case["operating_margin"]["values"] += [.17] * 5
    result = value(doc)
    original = result.scenarios["bear"].inputs
    run = simulate(result, uncertain(scenario="bear"))
    for draw in run.draws:
        assert draw.inputs.growth == [g + draw.growth_shift for g in original.growth]
        actual = run_scenario(draw.inputs, result.base_year, result.bridge, result.market.price)
        term = actual.terminal
        # With no excess returns, terminal value = terminal NOPAT / WACC: growth isn't free value.
        assert term.value == pytest.approx(term.ebit_after_tax / term.wacc)
        last = actual.rows[-1]
        assert draw.transition_flagged == transition_flag(last.fcff, term.fcff, last.roic, term.roic)
    assert any(draw.transition_flagged for draw in run.draws)


def test_reproducible_isolated_rng_no_mutation_and_snapshot(doc):
    result = value(doc)
    before = deepcopy(result)
    rng = random.getstate()
    first = simulate(result, uncertain())
    second = simulate(result, uncertain())
    assert random.getstate() == rng
    assert result == before
    assert first.draws == second.draws and first.summary == second.summary
    assert first.fingerprint == second.fingerprint
    assert first.draws != simulate(result, uncertain(seed=1730)).draws
    original_snapshot = deepcopy(first.snapshot)
    result.assumptions["scenarios"]["base"]["story"] += " Changed."
    assert first.snapshot == original_snapshot
    assert simulation_fingerprint(result, uncertain()) != first.fingerprint
    assert all(d.ranks[0] != d.ranks[1] != d.ranks[2] for d in first.draws)


@pytest.mark.parametrize("mode", [-2., 0., 6.])
def test_triangular_inverse_cdf_endpoints_support_and_shape(mode):
    tri = Triangle(-2., mode, 6.)
    tri.validate("test")
    assert tri.quantile(0) == -2 and tri.quantile(1) == 6
    for rank in [.001, .1, .25, .5, .9, .999]:
        x = tri.quantile(rank)
        assert -2 <= x <= 6
        # Independently evaluate the triangular CDF at the generated point.
        cdf = (x + 2)**2 / (8 * (mode + 2)) if x < mode else 1 - (6 - x)**2 / (8 * (6 - mode))
        assert cdf == pytest.approx(rank)
    assert Triangle(3, 3, 3).quantile(.75) == 3


@pytest.mark.parametrize("bad", [Triangle(1, 0, 2), Triangle(0, 2, 1), Triangle(float("nan")),
                                  Triangle(0, 0, float("inf")), Triangle(True, 1, 2)])
def test_bad_triangles_are_explained(bad):
    with pytest.raises(SimulationError):
        replace(uncertain(), growth_shift=bad).validate()


@pytest.mark.parametrize("override", [dict(draws=0), dict(draws=20001), dict(draws=3.1), dict(draws=True),
                                      dict(seed=-1), dict(seed=2**32), dict(seed=False),
                                      dict(capital_multiplier=Triangle(0, 1, 2)),
                                      dict(margin_dependency="inferred"),
                                      dict(growth_shift=Triangle(), margin_dependency="same_rank")])
def test_bad_settings_are_explained(override):
    with pytest.raises(SimulationError):
        uncertain(**override).validate()


def test_partial_failures_all_failures_and_summary_arithmetic(doc):
    result = value(doc)
    run = simulate(result, uncertain(draws=200, margin_shift=Triangle(.6, .7, .8)))
    good = [d.per_share for d in run.draws if d.error is None]
    s = run.summary
    assert 0 < s.valid < s.attempted == 200
    assert s.invalid == sum(run.invalid_reasons.values()) == 200 - len(good)
    assert [d.index for d in run.draws] == list(range(1, 201))
    assert all(d.per_share is None for d in run.draws if d.error)
    assert s.mean == pytest.approx(sum(good) / len(good))
    assert s.median == statistics.median(good)
    assert s.standard_deviation == pytest.approx(math.sqrt(sum((x - s.mean)**2 for x in good) / len(good)))
    quantiles = statistics.quantiles(good, n=10, method="inclusive")
    assert s.p10 == pytest.approx(quantiles[0]) and s.p90 == pytest.approx(quantiles[-1])
    assert s.minimum == min(good) and s.maximum == max(good)
    assert s.above_price == sum(x > result.market.price for x in good)
    assert s.fraction_above_price == s.above_price / s.valid
    bins = histogram(run, bins=13)
    assert sum(b["count"] for b in bins) == s.valid
    for i, b in enumerate(bins):
        assert b["count"] == sum(b["lower"] <= v and (v <= b["upper"] if i == 12 else v < b["upper"])
                                 for v in good)
    payload = json.loads(run.to_json())
    assert payload["summary"] == asdict(s) and len(payload["draws"]) == 200
    assert payload["settings"]["seed"] == run.settings.seed
    failed = simulate(result, uncertain(margin_shift=Triangle(1., 1., 1.)))
    assert failed.summary.valid == 0 and failed.summary.invalid == 120
    assert failed.summary.mean is None and failed.summary.fraction_above_price is None
    assert histogram(failed) == []


def test_negative_values_not_clipped_and_price_comparison_strict(doc):
    result = value(doc)
    run = simulate(result, uncertain(margin_shift=Triangle(-1, -1, -1)))
    assert run.summary.negative_values == run.summary.valid == 120
    assert run.summary.maximum < 0
    result.market.price = result.scenarios["base"].per_share
    exact = simulate(result, SimulationSettings(draws=1))
    assert exact.summary.above_price == 0


def test_known_arithmetic_failures_retained_but_programming_errors_propagate(doc, monkeypatch):
    import valuation.simulation as module
    original = module.run_scenario
    calls = 0

    def bad_draw(*args):
        nonlocal calls
        calls += 1
        if calls > 1:
            raise ZeroDivisionError("test numerical failure")
        return original(*args)

    result = value(doc)
    monkeypatch.setattr(module, "run_scenario", bad_draw)
    run = simulate(result, uncertain(draws=3))
    assert run.summary.invalid == 3 and sum(run.invalid_reasons.values()) == 3
    assert calls == 4  # one baseline plus exactly three attempts, never refill
    monkeypatch.setattr(module, "run_scenario", lambda *args: (_ for _ in ()).throw(RuntimeError("bug")))
    with pytest.raises(RuntimeError, match="bug"):
        simulate(result, uncertain())


def test_nonfinite_failed_inputs_have_strict_json_records(doc):
    result = value(doc)
    run = simulate(result, uncertain(capital_multiplier=Triangle(1.7e308, 1.7e308, 1.7e308)))
    assert run.summary.invalid == 120
    encoded = json.loads(run.to_json(), parse_constant=lambda v: pytest.fail("nonstandard JSON number " + v))
    assert any(str(d["inputs"]["sales_to_capital"]).startswith("nonfinite:") for d in encoded["draws"])


def test_quantile_known_small_sample_and_case_unavailable(doc):
    assert empirical_quantile([0., 10., 20., 30.], .1) == pytest.approx(3)
    assert empirical_quantile([0., 10., 20., 30.], .9) == pytest.approx(27)
    assert empirical_quantile([7.], .9) == 7
    with pytest.raises(SimulationError, match="not computable"):
        simulate(value(doc), uncertain(scenario="unavailable"))


@pytest.mark.parametrize("width", [1e-16, 1e-14, 1e-12])
def test_tiny_nonzero_spread_histogram_counts_match_displayed_edges(doc, width):
    run = simulate(value(doc), uncertain(draws=100, growth_shift=Triangle(-width, 0, width),
                                         margin_shift=Triangle(), capital_multiplier=Triangle(1, 1, 1)))
    bins = histogram(run)
    values = [d.per_share for d in run.draws]
    assert sum(b["count"] for b in bins) == len(values)
    for i, b in enumerate(bins):
        assert b["lower"] < b["upper"]
        assert b["count"] == sum(b["lower"] <= v and
                                 (v <= b["upper"] if i == len(bins) - 1 else v < b["upper"]) for v in values)
