"""Market data: FRED DGS10, Yahoo chart price, Damodaran's implied ERP (AGENTS.md section 18.8).

Numbers written in ``assumptions.yaml`` are used as given, with a warning that they are
manual.  ``auto`` cells are fetched; a failed price fetch stops with a message that names the
``--set`` override.  The risk-free rate never stalls: FRED gets a 20 s timeout and one retry,
and if it is still unreachable the T-bond rate on the latest row of the cached Damodaran ERP
dataset is used and labelled as such (a warning says so).  This module never writes into
``assumptions.yaml``.
"""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from . import datasets
from .engine import MarketInputs
from .schema import get_path

FRED_URL = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10"
YAHOO_URLS = (
    "https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?range=1d&interval=1d",
    "https://query2.finance.yahoo.com/v8/finance/chart/{ticker}?range=1d&interval=1d",
)
USER_AGENT = datasets.USER_AGENT
HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept": "application/json,text/csv,text/plain,*/*",
    "Accept-Language": "en-US,en;q=0.9",
}


FRED_TIMEOUT = 20            # seconds per attempt; FRED is intermittently slow
FRED_ATTEMPTS = 2            # one retry
FRED_FALLBACK_SOURCE = "Damodaran ERPbymonth T-bond rate (FRED unavailable)"


class MarketError(Exception):
    """A required market value could not be obtained."""


@dataclass
class RiskFree:
    """A risk-free rate with where it came from; ``note`` explains a fallback, else None."""
    rate: float
    date: str
    source: str
    note: str | None = None


def _get(url: str, timeout: int = 20, attempts: int = 2, headers: dict[str, str] | None = None) -> bytes:
    """GET with the given headers (browser-like for Yahoo by default), ``attempts`` tries ``timeout``
    seconds each, 1.5 s apart."""
    last: Exception | None = None
    for i in range(attempts):
        try:
            req = urllib.request.Request(url, headers=headers or HEADERS)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError) as exc:
            last = exc
            if i + 1 < attempts:
                time.sleep(1.5)
    raise MarketError(f"{url}: {last}")


# FRED throttles browser-style agents coming from scripts (a browser User-Agent times out after 20 s while
# a plain one answers in well under a second), so the FRED request identifies itself plainly and never
# reuses the Yahoo headers.
FRED_HEADERS = {"User-Agent": f"finance-valuation/{__import__('valuation').__version__} (python urllib)",
                "Accept": "text/csv,text/plain,*/*"}


def fetch_risk_free(timeout: int = FRED_TIMEOUT, attempts: int = FRED_ATTEMPTS) -> tuple[float, str]:
    """Latest non-empty DGS10 observation as (decimal rate, ISO date); ``attempts`` tries, 1.5 s apart,
    with a plain identifying User-Agent (never the browser-like one Yahoo needs)."""
    text = _get(FRED_URL, timeout, attempts, FRED_HEADERS).decode("utf-8", "replace")
    latest: tuple[float, str] | None = None
    for line in text.splitlines()[1:]:
        parts = line.strip().split(",")
        if len(parts) < 2 or parts[1] in ("", "."):
            continue
        try:
            latest = (float(parts[1]) / 100.0, parts[0])
        except ValueError:
            continue
    if latest is None:
        raise MarketError("FRED DGS10: no non-empty observation in the CSV")
    return latest


def fallback_risk_free(data_dir: Path | None = None) -> tuple[float, str]:
    """The T-bond rate on the latest row of the cached Damodaran ERP dataset, as (decimal rate, row date)."""
    try:
        row = datasets.latest_erp(data_dir or datasets.DATA_DIR)
    except datasets.DatasetError as exc:
        raise MarketError(f"cached ERPbymonth dataset unusable as a risk-free fallback: {exc}") from exc
    return row.tbond_rate, row.date


def risk_free_with_fallback(timeout: int = FRED_TIMEOUT, attempts: int = FRED_ATTEMPTS, *, fetch: bool = True,
                            data_dir: Path | None = None) -> RiskFree:
    """FRED DGS10 first (``attempts`` tries); if FRED cannot be reached, or fetching is off, the T-bond
    rate on the latest row of the cached Damodaran ERP dataset, labelled as such.  Never stalls on FRED;
    raises :class:`MarketError` only when the cached dataset is unusable too."""
    why = "fetching is off"
    if fetch:
        try:
            rate, when = fetch_risk_free(timeout, attempts)
            return RiskFree(rate, when, "FRED DGS10")
        except MarketError as exc:
            why = f"FRED DGS10 unreachable after {attempts} attempts ({exc})"
    rate, when = fallback_risk_free(data_dir)
    note = (f"risk-free rate: {why}; using the T-bond rate {rate * 100:.2f}% on the latest row ({when}) of the "
            "cached Damodaran ERPbymonth dataset")
    return RiskFree(rate, when, FRED_FALLBACK_SOURCE, note)


def fetch_price(ticker: str, timeout: int = 20) -> tuple[float, str]:
    """Yahoo chart ``regularMarketPrice`` and the trade date (exchange local time)."""
    errors: list[str] = []
    for template in YAHOO_URLS:
        url = template.format(ticker=ticker)
        try:
            payload = json.loads(_get(url, timeout).decode("utf-8", "replace"))
            meta = payload["chart"]["result"][0]["meta"]
            price = float(meta["regularMarketPrice"])
            stamp = int(meta.get("regularMarketTime", 0))
            offset = int(meta.get("gmtoffset", 0))
            when = (datetime.fromtimestamp(stamp, tz=timezone.utc) + timedelta(seconds=offset)
                    if stamp else datetime.now(timezone.utc))
            return price, when.strftime("%Y-%m-%d %H:%M ") + str(meta.get("timezone", "UTC"))
        except (MarketError, KeyError, IndexError, TypeError, ValueError, json.JSONDecodeError) as exc:
            errors.append(f"{url}: {exc}")
    raise MarketError("Yahoo price: " + " | ".join(errors))


def resolve(doc: dict[str, Any], *, fetch: bool = True, ticker: str | None = None,
            data_dir: Path | None = None, timeout: int = 20) -> MarketInputs:
    """Turn the YAML ``market`` block into numbers with dates and sources."""
    data_dir = data_dir or datasets.DATA_DIR
    ticker = ticker or str(doc.get("ticker"))
    warnings: list[str] = []
    manual_date = str(doc.get("drafted") or doc.get("as_of_date") or "")

    price_cell = get_path(doc, "market.price")
    if price_cell == "auto":
        if not fetch:
            raise MarketError("market.price is 'auto' but fetching is off (--no-fetch); "
                              "pass --set market.price=<number> or write a number in assumptions.yaml")
        try:
            price, price_date = fetch_price(ticker, timeout)
            price_source = "Yahoo chart"
        except MarketError as exc:
            raise MarketError(f"price fetch failed ({exc}); pass --set market.price=<number> "
                              "or write a number in assumptions.yaml") from exc
    else:
        price, price_date, price_source = float(price_cell), manual_date, "assumptions.yaml (manual)"
        warnings.append(f"market.price is a manual value ({price:.2f}) from assumptions.yaml or --set, not fetched")

    rf_cell = get_path(doc, "market.risk_free_rate")
    if rf_cell == "auto":
        try:
            got = risk_free_with_fallback(timeout, fetch=fetch, data_dir=data_dir)
        except MarketError as exc:
            raise MarketError(f"risk-free rate: {exc}; pass --set market.risk_free_rate=<decimal> "
                              "or write a decimal in assumptions.yaml") from exc
        rf, rf_date, rf_source = got.rate, got.date, got.source
        if got.note:
            warnings.append(got.note)
    else:
        rf, rf_date, rf_source = float(rf_cell), manual_date, "assumptions.yaml (manual)"
        warnings.append(f"market.risk_free_rate is a manual value ({rf:.4f}) from assumptions.yaml or --set, not fetched")

    erp_cell = get_path(doc, "market.equity_risk_premium")
    if erp_cell == "auto":
        try:
            row = datasets.latest_erp(data_dir)
        except datasets.DatasetError as exc:
            raise MarketError(f"equity risk premium: {exc}; or pass --set market.equity_risk_premium=<decimal>") from exc
        erp, erp_date, erp_source = row.erp, row.date, "Damodaran ERPbymonth.xlsx, cached"
    else:
        erp, erp_date, erp_source = float(erp_cell), manual_date, "assumptions.yaml (manual)"
        warnings.append(f"market.equity_risk_premium is a manual value ({erp:.4f}) from assumptions.yaml or --set, not fetched")

    return MarketInputs(price=price, risk_free_rate=rf, equity_risk_premium=erp, price_date=price_date,
                        risk_free_date=rf_date, erp_date=erp_date, price_source=price_source,
                        risk_free_source=rf_source, erp_source=erp_source, warnings=warnings)
