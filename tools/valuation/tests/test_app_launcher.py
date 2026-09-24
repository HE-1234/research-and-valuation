"""The ``valuation-app`` launcher assembles a local-only ``streamlit run`` command and passes options through."""

from __future__ import annotations

from valuation.app_launcher import APP_PATH, build_command, main


def test_defaults_bind_to_localhost_open_the_browser_and_silence_usage_stats():
    cmd = build_command([], python="py")
    assert cmd[:5] == ["py", "-m", "streamlit", "run", str(APP_PATH)]
    assert APP_PATH.name == "app.py"
    tail = cmd[5:]
    assert tail == ["--server.address", "127.0.0.1", "--server.headless", "false", "--browser.gatherUsageStats", "false",
                    "--theme.base", "light", "--theme.primaryColor", "#575be7"]


def test_callers_own_options_replace_the_defaults_and_pass_through():
    cmd = build_command(["--server.address", "0.0.0.0", "--server.port", "8502"], python="py")
    tail = cmd[5:]
    assert "127.0.0.1" not in tail and tail.count("--server.address") == 1
    assert tail[-4:] == ["--server.address", "0.0.0.0", "--server.port", "8502"]
    assert "--server.headless" in tail and "--browser.gatherUsageStats" in tail
    cmd = build_command(["--server.headless=true", "--browser.gatherUsageStats=true"], python="py")
    tail = cmd[5:]
    assert tail == ["--server.address", "127.0.0.1", "--theme.base", "light", "--theme.primaryColor", "#575be7",
                    "--server.headless=true", "--browser.gatherUsageStats=true"]


def test_help_prints_usage_and_exits_zero(capsys):
    assert main(["--help"]) == 0
    out = capsys.readouterr().out
    assert "127.0.0.1" in out and "--server.address" in out
