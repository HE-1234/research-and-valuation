"""Display values come from editable inputs, not potentially stale narrative number strings."""
from pathlib import Path
import pytest
pytest.importorskip('streamlit')
import yaml
from valuation.app_scenarios import scenario_input_tables, readable_driver


def test_explicit_ten_year_inputs_have_units_and_no_ambiguous_combined_numbers():
    doc = {'scenarios': {'base': {'revenue_growth': {'values': [.2] * 10},
        'operating_margin': {'values': [.3] * 10}, 'reinvestment_override': {'values': [1250.5, None] * 5},
        'sales_to_capital': {'value': 1.5, 'value_late': 1.25},
        'tax_rate': {'start': .2, 'terminal': .25}, 'weight': .5,
        'terminal': {'growth': {'value': .03}, 'roic_premium': {'value': .04}},
        'story_to_numbers': [{'drives': 'revenue_growth', 'number': '[.99]'}]}}}
    tables, settings = scenario_input_tables(doc, 'base', 10)
    assert [list(t.columns) for _,t in tables] == [
        ['Variable', 'Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5'],
        ['Variable', 'Year 6', 'Year 7', 'Year 8', 'Year 9', 'Year 10']]
    first = tables[0][1].set_index('Variable')
    assert first.loc['Revenue growth', 'Year 1'] == '20.0%'
    assert first.loc['Net reinvestment (USD millions)', 'Year 1'] == '1,250'
    assert first.loc['Net reinvestment (USD millions)', 'Year 2'] == 'Use ratio'
    assert settings.set_index('Variable').loc['Terminal return premium', 'Chosen value'] == '4.0 percentage points'
    doc['scenarios']['base']['revenue_growth']['values'][0] = .35
    assert scenario_input_tables(doc, 'base', 10)[0][0][1].set_index('Variable').loc['Revenue growth', 'Year 1'] == '35.0%'


def test_missing_management_values_stay_missing_and_driver_names_are_readable():
    tables, settings = scenario_input_tables({'scenarios': {'management': {'revenue_growth': {'values': [None]*5}}}}, 'management', 5)
    assert tables[0][1].set_index('Variable').loc['Revenue growth'].tolist() == ['Not supplied']*5
    assert settings.set_index('Variable').loc['Case weight','Chosen value'] == 'Not weighted'
    assert readable_driver('operating_margin.values; tax_rate.start; terminal.roic_premium.value') == 'Operating margin; Tax rate, years 1-5; Terminal return premium'
