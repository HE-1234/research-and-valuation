"""The factor ranking behind the Start page and the page order (AGENTS.md section 18.10)."""

from __future__ import annotations

import copy
import math
from pathlib import Path

import pytest

from valuation.engine import EngineError, MarketInputs
from valuation.impact import FACTOR_LABELS, impact_ranking, page_order
from valuation.schema import load_yaml

FIXTURE = Path(__file__).resolve().parent / "fixtures" / "example_assumptions.yaml"
MARKET = MarketInputs(price=70.0, risk_free_rate=0.0425, equity_risk_premium=0.045)


@pytest.fixture
def doc():
    return load_yaml(FIXTURE)


def test_ranking_is_sorted_by_absolute_impact_and_excludes_weights(doc):
    ranking = impact_ranking(doc, MARKET)
    assert len(ranking) == 7                                   # six pages, the terminal page nudged twice
    changes = [abs(i.change) for i in ranking]
    assert all(c is not None for c in changes)
    assert changes == sorted(changes, reverse=True)
    assert {i.factor for i in ranking} == set(FACTOR_LABELS) | {"terminal_roic"}
    assert not any(i.factor == "weights" for i in ranking)
    assert "weights change no case's value" in next(i.nudge for i in ranking if i.factor == "taxes_weights")
    assert all(i.nudge for i in ranking)
    assert len({i.base_per_share for i in ranking}) == 1       # every nudge starts from the same base value


def test_revenue_growth_nudge_raises_the_value(doc):
    by = {i.factor: i for i in impact_ranking(doc, MARKET)}
    g = by["revenue_growth"]
    assert g.change is not None and g.change > 0
    assert math.isclose(g.nudged_per_share - g.base_per_share, g.change)
    assert "1 point" in g.nudge
    assert by["operating_margin"].change > 0
    assert by["cost_of_capital"].change < 0
    assert by["taxes_weights"].change < 0
    assert by["terminal_roic"].change > 0


def test_terminal_growth_nudge_respects_the_riskfree_cap(doc):
    by = {i.factor: i for i in impact_ranking(doc, MARKET)}          # base terminal growth is 'riskfree'
    assert "-0.25" in by["terminal"].nudge and by["terminal"].change < 0
    bull = {i.factor: i for i in impact_ranking(doc, MARKET, scenario="bull")}   # bull is 0.04 with rf 0.0425
    assert bull["terminal"].nudge == "terminal growth +0.25 point" and bull["terminal"].change > 0


def test_override_nudge_is_described_only_when_an_override_exists(doc):
    base = {i.factor: i for i in impact_ranking(doc, MARKET)}["reinvestment"]
    bull = {i.factor: i for i in impact_ranking(doc, MARKET, scenario="bull")}["reinvestment"]
    assert "overrides" not in base.nudge and "overrides +10%" in bull.nudge


def test_page_order_keeps_revenue_and_margin_first_and_ranks_the_rest(doc):
    ranking = impact_ranking(doc, MARKET)
    order = page_order(ranking)
    assert order[:2] == ["revenue_growth", "operating_margin"]
    assert sorted(order[2:]) == ["cost_of_capital", "reinvestment", "taxes_weights", "terminal"]
    sizes = {}
    for i in ranking:
        page = "terminal" if i.factor == "terminal_roic" else i.factor
        sizes[page] = max(sizes.get(page, 0.0), abs(i.change))
    assert [sizes[p] for p in order[2:]] == sorted((sizes[p] for p in order[2:]), reverse=True)
    assert page_order(None) == list(FACTOR_LABELS)              # the fallback order
    assert page_order([]) == list(FACTOR_LABELS)


def test_ranking_refuses_when_the_scenario_cannot_compute(doc):
    broken = copy.deepcopy(doc)
    broken["scenarios"]["base"]["sales_to_capital"]["value"] = None
    with pytest.raises(EngineError, match="base scenario cannot be computed"):
        impact_ranking(broken, MARKET)
    with pytest.raises(EngineError):
        impact_ranking({**doc, "scenarios": {**doc["scenarios"], "management": {**doc["scenarios"]["management"],
                                                                                "computable": False}}},
                       MARKET, scenario="management")


def test_a_nudge_that_stops_the_case_is_reported_not_raised(doc):
    tight = copy.deepcopy(doc)
    # terminal growth 0.0425 with a fixed terminal cost of capital just above it: the +0.25 nudge is
    # blocked by the cap, so the -0.25 branch runs; a premium nudge is fine; the ROIC nudge is fine too.
    tight["cost_of_capital"]["terminal"] = {"method": "value", "value": 0.0440, "reason": "test"}
    ranking = impact_ranking(tight, MARKET)
    assert all(i.change is not None for i in ranking)
    # now make the terminal cost of capital equal to the cap so the base itself fails
    tight["cost_of_capital"]["terminal"] = {"method": "value", "value": 0.0425, "reason": "test"}
    with pytest.raises(EngineError):
        impact_ranking(tight, MARKET)
