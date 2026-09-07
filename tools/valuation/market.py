"""Market data: FRED DGS10, Yahoo chart price, Damodaran's implied ERP (AGENTS.md section 18.8).

Numbers written in ``assumptions.yaml`` are used as given, with a warning that they are
manual.  ``auto`` cells are fetched; a failed fetch stops with a message that names the
``--set`` override.  This module never writes into ``assumptions.yaml``.
"""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.request
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


class MarketError(Exception):
    """A required market value could not be obtained."""


def _get(url: str, timeout: int = 20, attempts: int = 2) -> bytes:
    last: Exception | None = None
    for i in range(attempts):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError) as exc:
            last = exc
            if i + 1 < attempts:
                time.sleep(1.5)
    raise MarketError(f"{url}: {last}")


def fetch_risk_free(timeout: int = 20) -> tuple[float, str]:
    """Latest non-empty DGS10 observation as (decimal rate, ISO date)."""
    text = _get(FRED_URL, timeout).decode("utf-8", "replace")
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
        if not fetch:
            raise MarketError("market.risk_free_rate is 'auto' but fetching is off (--no-fetch); "
                              "pass --set market.risk_free_rate=<decimal> or write a decimal in assumptions.yaml")
        try:
            rf, rf_date = fetch_risk_free(timeout)
            rf_source = "FRED DGS10"
        except MarketError as exc:
            raise MarketError(f"risk-free fetch failed ({exc}); pass --set market.risk_free_rate=<decimal> "
                              "or write a decimal in assumptions.yaml") from exc
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
