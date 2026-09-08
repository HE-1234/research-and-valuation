"""The risk-free rate never stalls: FRED timeout and retry, then the cached Damodaran T-bond rate."""

from __future__ import annotations

from pathlib import Path

import pytest

from valuation import datasets
from valuation import market as market_mod
from valuation.market import FRED_FALLBACK_SOURCE, MarketError, fetch_risk_free, resolve, risk_free_with_fallback
from valuation.schema import load_yaml

FIXTURE = Path(__file__).resolve().parent / "fixtures" / "example_assumptions.yaml"
LATEST = datasets.latest_erp()          # the cached ERPbymonth row the fallback must reproduce


class _Timeout:
    """Stands in for urllib.request.urlopen: every call times out, and the calls are counted."""

    def __init__(self) -> None:
        self.calls = 0
        self.timeouts: list[float] = []
        self.requests: list = []

    def __call__(self, req, timeout=None):
        self.calls += 1
        self.timeouts.append(timeout)
        self.requests.append(req)
        raise TimeoutError("The read operation timed out")


@pytest.fixture
def fred_down(monkeypatch):
    stub = _Timeout()
    monkeypatch.setattr(market_mod.urllib.request, "urlopen", stub)
    monkeypatch.setattr(market_mod.time, "sleep", lambda s: None)
    return stub


def test_fetch_risk_free_waits_twenty_seconds_and_retries_once(fred_down):
    with pytest.raises(MarketError, match="timed out"):
        fetch_risk_free()
    assert fred_down.calls == 2 and fred_down.timeouts == [20, 20]


def test_fallback_to_the_cached_tbond_rate_with_its_label_and_date(fred_down):
    got = risk_free_with_fallback()
    assert fred_down.calls == 2
    assert got.rate == LATEST.tbond_rate and got.date == LATEST.date
    assert got.source == FRED_FALLBACK_SOURCE == "Damodaran ERPbymonth T-bond rate (FRED unavailable)"
    assert got.note and "FRED DGS10 unreachable after 2 attempts" in got.note and LATEST.date in got.note


def test_fallback_when_fetching_is_off_does_not_touch_the_network(fred_down):
    got = risk_free_with_fallback(fetch=False)
    assert fred_down.calls == 0
    assert got.rate == LATEST.tbond_rate and got.source == FRED_FALLBACK_SOURCE
    assert got.note and got.note.startswith("risk-free rate: fetching is off")


def test_resolve_uses_the_fallback_and_warns(fred_down):
    doc = load_yaml(FIXTURE)
    doc["market"]["price"] = 70                       # only the risk-free cell is fetched
    market = resolve(doc)
    assert fred_down.calls == 2
    assert market.risk_free_rate == LATEST.tbond_rate and market.risk_free_date == LATEST.date
    assert market.risk_free_source == FRED_FALLBACK_SOURCE
    assert any("FRED DGS10 unreachable" in w and "cached Damodaran ERPbymonth dataset" in w for w in market.warnings)
    offline = resolve(doc, fetch=False)
    assert offline.risk_free_rate == LATEST.tbond_rate and offline.risk_free_source == FRED_FALLBACK_SOURCE


def test_fallback_fails_clearly_when_the_dataset_is_missing(fred_down, tmp_path):
    with pytest.raises(MarketError, match="risk-free fallback"):
        risk_free_with_fallback(data_dir=tmp_path)
    doc = load_yaml(FIXTURE)
    doc["market"]["price"] = 70
    with pytest.raises(MarketError, match="--set market.risk_free_rate"):
        resolve(doc, data_dir=tmp_path)


def test_fred_request_identifies_itself_plainly_and_never_as_a_browser(fred_down):
    """FRED throttles browser-style agents from scripts: the DGS10 request must not carry the Yahoo headers."""
    with pytest.raises(MarketError):
        fetch_risk_free()
    for req in fred_down.requests:
        assert req.full_url == market_mod.FRED_URL
        agent = req.get_header("User-agent") or ""
        assert not agent.startswith("Mozilla") and "AppleWebKit" not in agent
        assert agent.startswith("finance-valuation/") and "python urllib" in agent
        assert "text/csv" in req.get_header("Accept")
    assert market_mod.HEADERS["User-Agent"].startswith("Mozilla/5.0")      # Yahoo keeps the browser agent
