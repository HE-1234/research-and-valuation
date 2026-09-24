"""Return identities and honest historical gaps, independently hand-calculated."""
from copy import deepcopy
from pathlib import Path

import pytest
import yaml

from valuation import MarketInputs, compute
from valuation.roic import load_return_history, return_comparisons

FIXTURE = Path(__file__).parent / 'fixtures' / 'example_assumptions.yaml'


def result(**changes):
    doc = yaml.safe_load(FIXTURE.read_text())
    doc.update(changes)
    return doc, compute(doc, MarketInputs(price=70, risk_free_rate=.0425, equity_risk_premium=.045), fetch=False)


def test_after_tax_identity_uses_each_years_margin_tax_and_ratio():
    doc, value = result(horizon=10)
    doc['scenarios']['base']['sales_to_capital']['value_late'] = 3
    doc['scenarios']['base']['operating_margin']['values'] = [.18, .20, .22, .24, .26, .28, .30, .32, .34, .40]
    value = compute(doc, value.market, fetch=False)
    rows = return_comparisons(value.scenarios['base'])
    assert rows[0].ratio_implied == pytest.approx(.18 * .92 * 1.5)
    assert rows[4].ratio_implied == pytest.approx(.26 * .92 * 1.5)
    assert rows[9].ratio_implied == pytest.approx(.40 * .75 * 3)
    # Total-capital ROIC is a different denominator; its year-1 value is profit / opening 16,000.
    assert rows[0].forecast_roic == pytest.approx(8000 * 1.2 * .18 * .92 / 16000)
    assert rows[0].forecast_roic != rows[0].ratio_implied


def test_spending_override_changes_accumulated_return_not_ratio_identity():
    doc, baseline = result()
    original = return_comparisons(baseline.scenarios['base'])
    doc['scenarios']['base']['reinvestment_override']['values'][0] = 10000
    changed = return_comparisons(compute(doc, baseline.market, fetch=False).scenarios['base'])
    assert changed[0].overridden
    assert changed[0].forecast_roic == original[0].forecast_roic
    assert changed[1].forecast_roic < original[1].forecast_roic
    assert [r.ratio_implied for r in changed] == [r.ratio_implied for r in original]


def test_loss_has_no_assumed_tax_refund_and_nonpositive_capital_is_unavailable():
    doc, value = result()
    doc['scenarios']['base']['operating_margin']['values'][0] = -.1
    changed = compute(doc, value.market, fetch=False).scenarios['base']
    assert return_comparisons(changed)[0].ratio_implied == pytest.approx(-.15)
    changed.rows[0].invested_capital_start = -1
    assert return_comparisons(changed)[0].forecast_roic is None


def history_file(tmp_path, records):
    directory = tmp_path / 'EXMP'
    (directory / 'valuation').mkdir(parents=True)
    (directory / 'sources').mkdir()
    (directory / 'sources' / 'annual.txt').write_text('Illustrative test source')
    data = dict(schema=1, ticker='EXMP', as_of_date='2026-08-01', method='Reported accounting',
                capital_definition='Opening equity plus debt less cash', years=records)
    path = directory / 'valuation' / 'historical-roic.yaml'
    path.write_text(yaml.safe_dump(data))
    return directory, path


def observation(**changes):
    row = dict(period='FY2025', period_end='2025-12-31', operating_income=100, tax_rate=.2,
               invested_capital_start=500, source='[FY2025 filing]', source_paths=['sources/annual.txt'])
    row.update(changes)
    return row


def test_historical_return_keeps_losses_tax_anomalies_and_missing_values_distinct(tmp_path):
    records = [observation(period='positive'), observation(period='loss', operating_income=-100, tax_rate=None),
               observation(period='tax anomaly', tax_rate=1.5), observation(period='missing', tax_rate=None),
               observation(period='zero capital', invested_capital_start=0),
               observation(period='negative capital', invested_capital_start=-100)]
    directory, path = history_file(tmp_path, records)
    before = path.read_bytes()
    loaded = load_return_history(directory, 'EXMP', '2026-09-01')
    assert [r.roic for r in loaded.years] == [.16, -.2, -.1, None, None, None]
    assert 'Unusual reported tax rate' in loaded.years[2].note
    assert path.read_bytes() == before


def test_missing_sources_future_evidence_and_invalid_files_do_not_fabricate_history(tmp_path):
    directory, path = history_file(tmp_path, [observation(source_paths=['sources/missing.txt'])])
    assert load_return_history(directory, 'EXMP', '2026-09-01').years[0].roic is None
    assert load_return_history(directory, 'EXMP', '2026-07-01').error
    assert load_return_history(directory, 'WRONG', '2026-09-01').error
    path.write_text('not: [valid')
    assert load_return_history(directory, 'EXMP', '2026-09-01').error
    path.unlink()
    assert load_return_history(directory, 'EXMP', '2026-09-01').error
