"""The ``value`` command on the example assumptions file."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

import pytest

from valuation.cli import main

FIXTURE = Path(__file__).resolve().parent / "fixtures" / "example_assumptions.yaml"
OFFLINE = ["--no-fetch", "--set", "market.price=70", "--set", "market.risk_free_rate=0.0425"]


def test_validate_ok(capsys):
    assert main([str(FIXTURE), "--validate"]) == 0
    out = capsys.readouterr().out
    assert "validates" in out and "computable scenarios: bear, base, bull, management" in out


def test_validate_reports_errors_with_paths(tmp_path, capsys):
    text = FIXTURE.read_text(encoding="utf-8").replace("weight: 0.50", "weight: 0.60")
    bad = tmp_path / "assumptions.yaml"
    bad.write_text(text, encoding="utf-8")
    assert main([str(bad), "--validate"]) == 1
    assert "scenarios.*.weight" in capsys.readouterr().out


def test_validate_with_set_null_reports_stopped_scenario(capsys):
    assert main([str(FIXTURE), "--validate", "--set", "scenarios.base.sales_to_capital.value=null"]) == 0
    out = capsys.readouterr().out
    assert "base scenario stopped: scenarios.base.sales_to_capital.value is null" in out


def test_dry_run_offline_prints_table_and_writes_nothing(capsys):
    assert main([str(FIXTURE), "--dry-run", *OFFLINE]) == 0
    out = capsys.readouterr().out
    assert "| base |" in out and "| weighted expected |" in out and "dry run: nothing written" in out
    assert "## 9. Warnings" in out
    assert not (FIXTURE.parent / "valuation.md").exists()


def test_no_fetch_without_override_fails_clearly(capsys):
    assert main([str(FIXTURE), "--dry-run", "--no-fetch"]) == 1
    err = capsys.readouterr().err
    assert "--set market.price" in err


def test_set_changes_the_result(capsys):
    assert main([str(FIXTURE), "--json", *OFFLINE]) == 0
    before = json.loads(capsys.readouterr().out)
    assert main([str(FIXTURE), "--json", *OFFLINE, "--set", "scenarios.base.operating_margin.values.4=0.34"]) == 0
    after = json.loads(capsys.readouterr().out)
    assert after["scenarios"]["base"]["per_share"] > before["scenarios"]["base"]["per_share"]
    assert after["scenarios"]["base"]["inputs"]["margin"][4] == 0.34
    assert before["market"]["price"] == 70.0
    assert "assumptions" not in after


def test_normal_run_writes_and_archives(tmp_path, capsys):
    root = tmp_path
    (root / "AGENTS.md").write_text("# stub\n", encoding="utf-8")
    company = root / "companies" / "EXMP"
    (company / "valuation").mkdir(parents=True)
    (company / "sources" / "FY2027-Q2").mkdir(parents=True)
    (company / "sources" / "FY2027-Q2" / "10-Q-FY2027-Q2.txt").write_text("stub", encoding="utf-8")
    (company / "outlook.md").write_text(
        "## Sources\n\n| Tag prefix | Cached file |\n|---|---|\n"
        "| [Q2 FY2027 call] | `sources/FY2027-Q2/transcript.txt` (call) |\n", encoding="utf-8")
    target = company / "valuation" / "assumptions.yaml"
    shutil.copy(FIXTURE, target)
    assert main([str(target), *OFFLINE]) == 0
    md = company / "valuation" / "valuation.md"
    assert md.exists()
    text = md.read_text(encoding="utf-8")
    for heading in ("## 1. Results", "## 2. The stories", "## 3. Assumptions", "## 4. Base year",
                    "## 5. Base case, year by year", "## 6. Sensitivity", "## 7. Reverse DCF",
                    "## 8. Diagnostics", "## 9. Warnings", "## 10. Glossary", "## 11. Sources"):
        assert heading in text, heading
    assert "`sources/FY2027-Q2/10-Q-FY2027-Q2.txt`" in text          # resolved by file name
    assert "`sources/FY2027-Q2/transcript.txt`" in text              # resolved by the Sources table
    assert "not resolved" in text                                      # slides tag has no file
    assert "--set" not in text or "market.price" in text
    # second run archives the first pair
    assert main([str(target), *OFFLINE]) == 0
    history = list((company / "valuation" / "history").iterdir())
    assert len(history) == 1
    assert {p.name for p in history[0].iterdir()} == {"valuation.md", "assumptions.yaml"}
    out = capsys.readouterr().out
    assert "archived previous valuation.md" in out and "written" in out


def test_ticker_resolution_needs_repo_root(tmp_path, capsys):
    root = tmp_path
    (root / "AGENTS.md").write_text("# stub\n", encoding="utf-8")
    company = root / "companies" / "EXMP" / "valuation"
    company.mkdir(parents=True)
    shutil.copy(FIXTURE, company / "assumptions.yaml")
    import os
    cwd = os.getcwd()
    os.chdir(root)
    try:
        assert main(["exmp", "--validate"]) == 0
        assert main(["nope", "--validate"]) == 1
    finally:
        os.chdir(cwd)
    assert "does not exist" in capsys.readouterr().err


def test_horizon_ten_on_a_five_entry_file_marks_the_fade_years_and_names_the_reference(capsys):
    """`--set horizon=10` on a five-entry file is the section 18.2 default structure."""
    assert main([str(FIXTURE), "--dry-run", *OFFLINE, "--set", "horizon=10"]) == 0
    out = capsys.readouterr().out
    assert "| 5-year stop value per share |" in out
    assert "10-year-fade" not in out


def test_valuation_md_marks_the_fade_years_and_the_transition_check(tmp_path, capsys):
    root = tmp_path
    (root / "AGENTS.md").write_text("# stub\n", encoding="utf-8")
    vdir = root / "companies" / "EXMP" / "valuation"
    vdir.mkdir(parents=True)
    target = vdir / "assumptions.yaml"
    shutil.copy(FIXTURE, target)
    assert main([str(target), *OFFLINE, "--set", "horizon=10"]) == 0
    text = (vdir / "valuation.md").read_text(encoding="utf-8")
    assert "| 5-year stop value per share |" in text
    assert "| How the year is set |" in text
    assert "| 6 | by rule |" in text and "| 5 | from the assumptions |" in text
    assert "| 10 | by rule |" in text
    assert "Years 6-10 are built by rule from year 5" in text
    assert "7. The step from the last explicit year into the terminal year" in text
    assert "horizon 10 years (5 set in the assumptions, the rest by rule)" in text
    capsys.readouterr()


def test_five_year_file_keeps_the_ten_year_fade_as_its_reference(capsys):
    assert main([str(FIXTURE), "--dry-run", *OFFLINE, "--set", "horizon=5"]) == 0
    out = capsys.readouterr().out
    assert "| 10-year fade value per share |" in out
    assert "5-year stop" not in out


@pytest.mark.parametrize("extra", [[], ["--json"], ["--dry-run", "--json"]])
def test_draft_diagnostics_match_engine_without_values_or_writes(tmp_path, capsys, monkeypatch, extra):
    target = tmp_path / "assumptions.yaml"
    shutil.copy(FIXTURE, target)
    # A stale report must neither be read as the current result nor archived/overwritten.
    (tmp_path / "valuation.md").write_text("previous valuation", encoding="utf-8")
    (tmp_path / "assumptions.md").write_text("previous readable inputs", encoding="utf-8")
    before = {p.name: p.read_bytes() for p in tmp_path.iterdir()}
    assert main([str(target), "--json", *OFFLINE]) == 0
    full = json.loads(capsys.readouterr().out)

    def no_report(*args, **kwargs):
        pytest.fail("draft diagnostics must not render a valuation report")

    monkeypatch.setattr("valuation.cli.render", no_report)
    assert main([str(target), "--diagnostics-only", *extra, *OFFLINE]) == 0
    captured = capsys.readouterr()
    payload = json.loads(captured.out)
    assert not captured.err
    assert payload["market"] == full["market"]
    assert payload["warnings"] == full["warnings"]
    assert payload["transition_check"]["flag"] is True
    for name, case in payload["scenarios"].items():
        for row, original in zip(case["years"], full["scenarios"][name]["rows"], strict=True):
            assert row["fcff"] == original["fcff"]
            assert row["roic"] == original["roic"]
            assert row["wacc"] == original["wacc"]
        assert case["terminal"]["fcff"] == full["scenarios"][name]["terminal"]["fcff"]
        assert case["terminal"]["roic"] == full["scenarios"][name]["terminal"]["roic"]

    forbidden = {"per_share", "equity", "enterprise_value", "operating_assets", "pv", "pv_terminal",
                 "sum_pv_fcff", "terminal_share", "reference", "reference_per_share", "weighted",
                 "reverse", "grids", "upside", "assumptions"}

    def check_fields(value):
        if isinstance(value, dict):
            assert not forbidden.intersection(value)
            for child in value.values():
                check_fields(child)
        elif isinstance(value, list):
            for child in value:
                check_fields(child)

    check_fields(payload)
    assert set(payload["scenarios"]["base"]["terminal"]) == {
        "year", "revenue", "growth", "margin", "ebit_after_tax", "reinvestment", "fcff", "wacc", "roic"}
    assert {p.name: p.read_bytes() for p in tmp_path.iterdir()} == before


def test_draft_diagnostics_report_stopped_and_skipped_cases(capsys):
    assert main([str(FIXTURE), "--diagnostics-only", *OFFLINE,
                 "--set", "scenarios.base.sales_to_capital.value=null",
                 "--set", "scenarios.management.computable=false"]) == 0
    payload = json.loads(capsys.readouterr().out)
    assert set(payload["scenarios"]) == {"bear", "bull"}
    assert "sales_to_capital.value is null" in payload["stopped"]["base"][0]
    assert "management" in payload["skipped"]
    assert any("base scenario not computed" in warning for warning in payload["warnings"])


@pytest.mark.parametrize("mode", ["--render-assumptions", "--refresh-data", "--validate"])
def test_draft_diagnostics_reject_conflicting_modes_before_side_effects(tmp_path, capsys, monkeypatch, mode):
    def forbidden(*args, **kwargs):
        pytest.fail("a conflicting mode must fail before file access or fetching")

    monkeypatch.setattr("valuation.cli.load", forbidden)
    monkeypatch.setattr("valuation.cli.refresh_data", forbidden)
    with pytest.raises(SystemExit) as exc:
        main([str(tmp_path / "missing.yaml"), "--diagnostics-only", mode])
    assert exc.value.code == 2
    assert "cannot be combined" in capsys.readouterr().err
    assert not list(tmp_path.iterdir())


def test_validation_accepts_user_override_that_repairs_input_without_saving(tmp_path, capsys):
    target = tmp_path / "assumptions.yaml"
    target.write_text(FIXTURE.read_text().replace("weight: 0.50", "weight: 0.60"), encoding="utf-8")
    before = target.read_bytes()
    assert main([str(target), "--validate"]) == 1
    capsys.readouterr()
    assert main([str(target), "--validate", "--set", "scenarios.base.weight=0.50"]) == 0
    assert "validates" in capsys.readouterr().out
    assert target.read_bytes() == before
