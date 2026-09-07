"""The Streamlit app, driven headlessly with ``streamlit.testing.v1.AppTest``.

Skipped when streamlit is not installed (``uv run pytest``); runs under
``uv run --extra app pytest``.  The app is pointed at a temporary repository copy that
holds the fixture company, with market cells written as numbers so nothing is fetched.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

streamlit = pytest.importorskip("streamlit")
from streamlit.testing.v1 import AppTest  # noqa: E402

HERE = Path(__file__).resolve().parent
FIXTURE = HERE / "fixtures" / "example_assumptions.yaml"
APP = HERE.parent / "app.py"


@pytest.fixture
def repo(tmp_path: Path, monkeypatch) -> Path:
    root = tmp_path / "repo"
    root.mkdir()
    (root / "AGENTS.md").write_text("# stub\n", encoding="utf-8")
    vdir = root / "companies" / "EXMP" / "valuation"
    vdir.mkdir(parents=True)
    text = FIXTURE.read_text(encoding="utf-8")
    text = text.replace("price: auto", "price: 70").replace("risk_free_rate: auto", "risk_free_rate: 0.0425")
    text = text.replace("equity_risk_premium: auto", "equity_risk_premium: 0.045")
    (vdir / "assumptions.yaml").write_text(text, encoding="utf-8")
    monkeypatch.setenv("VALUATION_REPO_ROOT", str(root))
    monkeypatch.setenv("VALUATION_APP_NO_FETCH", "1")
    return root


def run_app() -> AppTest:
    at = AppTest.from_file(str(APP), default_timeout=60)
    at.run()
    return at


def assert_clean(at: AppTest) -> None:
    assert not at.exception, [e.value for e in at.exception]


def test_app_loads_edits_recomputes_and_saves(repo: Path):
    yaml_path = repo / "companies" / "EXMP" / "valuation" / "assumptions.yaml"
    at = run_app()
    assert_clean(at)
    assert at.session_state["ticker"] == "EXMP"
    result = at.session_state["last_result"]
    assert result is not None and "base" in result.scenarios
    # the results table is the first dataframe on the page and lists every case
    assert at.dataframe, "no dataframe rendered"
    table = at.dataframe[0].value
    assert list(table["Case"]) == ["bear", "base", "bull", "management", "weighted expected"]
    assert table.loc[table["Case"] == "base", "Price"].iloc[0] == "70.00"
    before = result.scenarios["base"].per_share
    # the sidebar reports no unsaved changes
    assert at.session_state["working"]["scenarios"]["base"]["sales_to_capital"]["value"] == 1.5

    # change one number through its widget; the value recomputes
    gen = at.session_state["gen"]
    widget = at.number_input(key=f"w{gen}:scenarios.base.sales_to_capital.value")
    assert widget.value == 1.5
    widget.set_value(2.5).run()
    assert_clean(at)
    after = at.session_state["last_result"].scenarios["base"].per_share
    assert after > before
    assert at.session_state["working"]["scenarios"]["base"]["sales_to_capital"]["value"] == 2.5
    # the file is untouched so far
    assert yaml.safe_load(yaml_path.read_text(encoding="utf-8"))["scenarios"]["base"]["sales_to_capital"]["value"] == 1.5

    # save with a note
    at.text_input(key="save_note:EXMP").input("owner: fabless peers reinvest less").run()
    at.button(key="save_btn").click().run()
    assert_clean(at)
    text = yaml_path.read_text(encoding="utf-8")
    plain = yaml.safe_load(text)
    assert plain["scenarios"]["base"]["sales_to_capital"]["value"] == 2.5
    assert plain["changelog"] == [{
        "at": plain["owner_edited"], "path": "scenarios.base.sales_to_capital.value", "old": 1.5, "new": 2.5,
        "note": "owner: fabless peers reinvest less"}]
    assert "# Example assumptions.yaml following AGENTS.md section 18.4." in text     # comments survive
    md = yaml_path.parent / "assumptions.md"
    assert md.exists()
    md_text = md.read_text(encoding="utf-8")
    assert "## 9. Change log" in md_text and "owner: fabless peers reinvest less" in md_text
    assert "| Sales-to-capital, years 1-5 | 1.20 | 2.50 | 1.80 | 1.50 |" in md_text
    # after the save the working copy matches the file again and the value stays
    assert at.session_state["working"]["scenarios"]["base"]["sales_to_capital"]["value"] == 2.5
    assert at.session_state["last_result"].scenarios["base"].per_share == pytest.approx(after)
    assert any("Saved 1 change" in s.value for s in at.success)
    # nothing else was written
    assert sorted(p.name for p in yaml_path.parent.iterdir()) == ["assumptions.md", "assumptions.yaml"]


def test_a_null_stops_one_scenario_without_a_traceback(repo: Path):
    yaml_path = repo / "companies" / "EXMP" / "valuation" / "assumptions.yaml"
    text = yaml_path.read_text(encoding="utf-8")
    assert text.count("value_late: 1.5") == 1                     # the bull case
    yaml_path.write_text(text.replace("value_late: 1.5", "value_late: null"), encoding="utf-8")
    at = run_app()
    assert_clean(at)
    result = at.session_state["last_result"]
    assert result is not None and "bull" not in result.scenarios and "bull" in result.stopped
    assert any("scenarios.bull.sales_to_capital.value_late is null" in w.value for w in at.warning)
    table = at.dataframe[0].value
    assert table.loc[table["Case"] == "bull", "Value per share"].iloc[0] == "not computed"


def test_write_valuation_refuses_with_unsaved_changes_and_works_when_clean(repo: Path):
    vdir = repo / "companies" / "EXMP" / "valuation"
    at = run_app()
    gen = at.session_state["gen"]
    at.number_input(key=f"w{gen}:scenarios.base.weight").set_value(0.5).run()   # same value: no change
    at.number_input(key=f"w{gen}:scenarios.base.sales_to_capital.value").set_value(2.0).run()
    at.button(key="write_btn").click().run()
    assert_clean(at)
    assert any("unsaved changes" in e.value for e in at.error)
    assert not (vdir / "valuation.md").exists()
    at.button(key="reset_btn").click().run()
    assert_clean(at)
    assert at.session_state["working"]["scenarios"]["base"]["sales_to_capital"]["value"] == 1.5
    at.button(key="write_btn").click().run()
    assert_clean(at)
    assert (vdir / "valuation.md").exists() and (vdir / "assumptions.md").exists()
    assert "## 1. Results" in (vdir / "valuation.md").read_text(encoding="utf-8")


def test_horizon_switch_pads_lists_and_recomputes(repo: Path):
    at = run_app()
    gen = at.session_state["gen"]
    at.radio(key=f"w{gen}:horizon").set_value(10).run()
    assert_clean(at)
    doc = at.session_state["working"]
    assert doc["horizon"] == 10
    assert doc["scenarios"]["base"]["revenue_growth"]["values"] == [0.20] * 10
    assert doc["scenarios"]["bull"]["reinvestment_override"]["values"] == [400, None, None, None, None] + [None] * 5
    assert at.session_state["last_result"].horizon == 10
    assert any("Horizon set to 10" in i.value for i in at.info)


def test_commit_messages_follow_section_18_7(repo: Path):
    """Owner edits alone commit as 'owner edits'; a written valuation.md commits as 'compute <QLABEL> rev N'."""
    import subprocess

    def git(*args: str) -> str:
        return subprocess.run(["git", *args], cwd=str(repo), capture_output=True, text=True, check=True).stdout

    git("init", "-q")
    git("-c", "user.name=t", "-c", "user.email=t@localhost", "add", ".")
    git("-c", "user.name=t", "-c", "user.email=t@localhost", "commit", "-q", "-m", "start")
    at = run_app()
    gen = at.session_state["gen"]
    at.number_input(key=f"w{gen}:scenarios.base.sales_to_capital.value").set_value(2.0).run()
    at.button(key="save_btn").click().run()
    at.button(key="commit_btn").click().run()
    assert_clean(at)
    assert git("log", "-1", "--format=%s%n%an").splitlines() == ["value(EXMP): owner edits to assumptions", "company-research"]
    assert any("Committed" in s.value for s in at.success)
    at.button(key="write_btn").click().run()
    at.button(key="commit_btn").click().run()
    assert_clean(at)
    assert git("log", "-1", "--format=%s") .strip() == "value(EXMP): compute FY2027-Q2 rev 1"
    assert not git("status", "--porcelain").strip()
    at.button(key="commit_btn").click().run()
    assert any("Nothing to commit" in s.value for s in at.success)
