"""Read-only return comparisons. These diagnostics do not change valuation inputs or cash flows.

The ratio used to size new investment is not the turnover of total historical capital.
Its product with an after-tax margin is a constant-margin diagnostic; the engine's
forecast ROIC separately follows operating profit and accumulated opening capital.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
import math
from pathlib import Path
from typing import Any

import yaml

from .engine import ScenarioResult, after_tax


@dataclass(frozen=True)
class ReturnComparison:
    year: int
    margin: float
    tax_rate: float
    sales_to_capital: float
    ratio_implied: float
    forecast_roic: float | None
    cost_of_capital: float
    overridden: bool


def return_comparisons(scenario: ScenarioResult) -> list[ReturnComparison]:
    """Use resolved yearly margins, tax fade and ratios; never substitute this check for engine ROIC."""
    return [ReturnComparison(
        year=row.year, margin=row.margin, tax_rate=row.tax_rate,
        sales_to_capital=row.sales_to_capital,
        ratio_implied=after_tax(row.margin, row.tax_rate) * row.sales_to_capital,
        forecast_roic=(row.roic if row.invested_capital_start is not None and row.invested_capital_start > 0 else None),
        cost_of_capital=row.wacc, overridden=row.reinvestment_source == 'override',
    ) for row in scenario.rows]


@dataclass(frozen=True)
class HistoricalReturn:
    period: str
    operating_income: float | None
    tax_rate: float | None
    opening_capital: float | None
    after_tax_income: float | None
    roic: float | None
    source: str
    source_paths: tuple[str, ...]
    note: str


@dataclass
class ReturnHistory:
    years: list[HistoricalReturn] = field(default_factory=list)
    summary: str = ''
    method: str = ''
    capital_definition: str = ''
    notes: list[str] = field(default_factory=list)
    error: str | None = None


def _number(value: Any) -> float | None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    return float(value) if math.isfinite(value) else None


def _date(value: Any) -> date | None:
    try:
        return date.fromisoformat(str(value))
    except (TypeError, ValueError):
        return None


def load_return_history(company_dir: Path, ticker: str, cutoff: Any) -> ReturnHistory:
    """Load source-backed historical inputs, refusing future evidence and untraceable figures.

    Historical effective taxes may exceed 100% or be negative; retain those observations
    with a warning rather than silently clipping them to forecast assumptions' bounds.
    """
    path = company_dir / 'valuation' / 'historical-roic.yaml'
    if not path.exists():
        return ReturnHistory(error='Historical ROIC has not been recorded for this company.')
    try:
        data = yaml.safe_load(path.read_text(encoding='utf-8'))
    except (OSError, yaml.YAMLError):
        return ReturnHistory(error='The historical ROIC evidence file could not be read.')
    if not isinstance(data, dict) or data.get('schema') != 1 or data.get('ticker') != ticker:
        return ReturnHistory(error='The historical ROIC evidence does not match this company or format.')
    as_of, limit = _date(data.get('as_of_date')), _date(cutoff)
    if as_of is None or limit is None or as_of > limit:
        return ReturnHistory(error='Historical ROIC evidence cannot be used with this valuation’s information cutoff.')
    records = data.get('years')
    if not isinstance(records, list):
        return ReturnHistory(error='The historical ROIC evidence has no usable annual records.')
    history = ReturnHistory(summary=str(data.get('summary') or ''), method=str(data.get('method') or ''), capital_definition=str(data.get('capital_definition') or ''),
                            notes=[str(n) for n in data.get('comparability_notes', [])]
                            if isinstance(data.get('comparability_notes'), list) else [])
    seen = set()
    for record in records:
        if not isinstance(record, dict) or not isinstance(record.get('period'), str):
            history.notes.append('An incomplete historical record was omitted.')
            continue
        period = record['period']
        if period in seen:
            return ReturnHistory(error='The historical ROIC evidence contains duplicate periods.')
        seen.add(period)
        period_end = _date(record.get('period_end'))
        if period_end and period_end > limit:
            continue
        income, tax, capital = (_number(record.get(k)) for k in
                                ('operating_income', 'tax_rate', 'invested_capital_start'))
        source = str(record.get('source') or '')
        paths = record.get('source_paths') or []
        note = str(record.get('note') or '')
        valid_sources = bool(source and isinstance(paths, list) and paths)
        if valid_sources:
            for rel in paths:
                target = (company_dir / str(rel)).resolve()
                if not target.is_relative_to(company_dir.resolve()) or not target.is_file():
                    valid_sources = False
                    break
        nopat = None
        if valid_sources and income is not None and (income <= 0 or tax is not None):
            nopat = after_tax(income, tax if tax is not None else 0.0)
        if nopat is not None and not math.isfinite(nopat):
            nopat = None
            note += ' Historical inputs do not produce a finite after-tax profit.'
        value = nopat / capital if nopat is not None and capital is not None and capital > 0 else None
        if value is not None and not math.isfinite(value):
            value = None
            note += ' Historical inputs do not produce a finite return.' 
        if not valid_sources:
            note += ' Source evidence is missing or cannot be verified in the local source cache.'
        elif income is None:
            note += ' Operating profit is unavailable.'
        elif income > 0 and tax is None:
            note += ' A usable historical tax rate is unavailable.'
        if capital is None:
            note += ' Beginning-of-year invested capital is unavailable.'
        elif capital <= 0:
            note += ' ROIC is not meaningful with zero or negative beginning capital.'
        if income is not None and income < 0:
            note += ' Operating loss: no assumed tax benefit, consistent with the model.'
        elif tax is not None and not 0 <= tax <= 1:
            note += ' Unusual reported tax rate; tax items distort this historical comparison.'
        history.years.append(HistoricalReturn(period, income, tax, capital, nopat, value, source,
                                              tuple(str(p) for p in paths) if isinstance(paths, list) else (), note.strip()))
    return history
