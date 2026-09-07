"""The ``value`` command on the example assumptions file."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

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
