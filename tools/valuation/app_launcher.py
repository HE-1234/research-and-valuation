"""``valuation-app``: start the Streamlit walk through ``assumptions.yaml`` (AGENTS.md section 18.10).

Runs ``streamlit run tools/valuation/app.py`` bound to ``127.0.0.1`` (local only), with the browser
opened and Streamlit's usage-statistics prompt silenced, and passes any extra arguments through to
Streamlit, so ``valuation-app --server.port 8502`` works.  Any of the defaults can be overridden by
passing the same option (``--server.address 0.0.0.0`` to expose the app on the network, for
instance).  Streamlit is an optional dependency: ``uv sync --extra app`` installs it.
"""

from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path

APP_PATH = Path(__file__).resolve().parent / "app.py"
USAGE = """usage: valuation-app [streamlit options]

Starts the local page that walks through every valuation input with its reason, recomputes
live through the engine, and saves edits back into companies/<TICKER>/valuation/assumptions.yaml.

The app listens on 127.0.0.1 only (it is not reachable from other machines) unless you pass
your own --server.address. Any option is passed through to `streamlit run`, for example:
  valuation-app --server.port 8502
  valuation-app --server.headless true
  valuation-app --server.address 0.0.0.0     # expose on the network (not the default)

Run it from the project with `uv run --extra app valuation-app`.
"""
# Defaults passed to `streamlit run` unless the caller gives the same option.
DEFAULTS = (("--server.address", "127.0.0.1"),        # local only: never bind to every interface by default
            ("--server.headless", "false"),            # open the browser
            ("--browser.gatherUsageStats", "false"),
            ("--theme.base", "light"),
            ("--theme.primaryColor", "#575be7"))   # no usage-statistics prompt or upload


def _given(args: list[str], option: str) -> bool:
    """True when the caller passed ``option`` (as ``--x.y value`` or ``--x.y=value``)."""
    return any(a == option or a.startswith(option + "=") for a in args)


def build_command(args: list[str], python: str | None = None) -> list[str]:
    """The ``streamlit run`` command line: the app path, the defaults the caller did not override, then
    the caller's own arguments verbatim."""
    cmd = [python or sys.executable, "-m", "streamlit", "run", str(APP_PATH)]
    for option, value in DEFAULTS:
        if not _given(args, option):
            cmd += [option, value]
    return cmd + list(args)


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if any(a in ("-h", "--help") for a in args):
        print(USAGE)
        return 0
    if importlib.util.find_spec("streamlit") is None:
        print("error: streamlit is not installed. Run `uv sync --extra app`, then "
              "`uv run --extra app valuation-app`.", file=sys.stderr)
        return 1
    cmd = build_command(args)
    try:
        return subprocess.run(cmd, check=False).returncode
    except KeyboardInterrupt:
        return 130


if __name__ == "__main__":
    sys.exit(main())
