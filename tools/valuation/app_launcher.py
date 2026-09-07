"""``valuation-app``: start the Streamlit editor for ``assumptions.yaml`` (AGENTS.md section 18.10).

Runs ``streamlit run tools/valuation/app.py --server.headless false`` and passes any
extra arguments through to Streamlit, so ``valuation-app --server.port 8502`` works.
Streamlit is an optional dependency: ``uv sync --extra app`` installs it.
"""

from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path

APP_PATH = Path(__file__).resolve().parent / "app.py"
USAGE = """usage: valuation-app [streamlit options]

Starts the local page that shows every valuation input with its reason, recomputes
live through the engine, and saves edits back into companies/<TICKER>/valuation/assumptions.yaml.

Any option is passed through to `streamlit run`, for example:
  valuation-app --server.port 8502
  valuation-app --server.headless true

Run it from the project with `uv run --extra app valuation-app`.
"""


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if any(a in ("-h", "--help") for a in args):
        print(USAGE)
        return 0
    if importlib.util.find_spec("streamlit") is None:
        print("error: streamlit is not installed. Run `uv sync --extra app`, then "
              "`uv run --extra app valuation-app`.", file=sys.stderr)
        return 1
    cmd = [sys.executable, "-m", "streamlit", "run", str(APP_PATH)]
    if not any(a.startswith("--server.headless") for a in args):
        cmd += ["--server.headless", "false"]
    cmd += args
    try:
        return subprocess.run(cmd, check=False).returncode
    except KeyboardInterrupt:
        return 130


if __name__ == "__main__":
    sys.exit(main())
