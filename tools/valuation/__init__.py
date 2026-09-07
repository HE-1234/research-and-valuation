"""Free-cash-flow-to-the-firm valuation engine for the research library (AGENTS.md section 18).

Python API::

    import valuation
    doc = valuation.load("MRVL")                    # companies/MRVL/valuation/assumptions.yaml
    result = valuation.compute(doc)                 # fetches 'auto' market cells, runs every case
    text = valuation.render(result)                 # valuation.md as a string
"""

from __future__ import annotations

__version__ = "0.1.0"

import os
from pathlib import Path
from typing import Any

from .schema import SchemaError, load_yaml, validate, validate_or_raise  # noqa: E402
from .engine import EngineError, MarketInputs, ValuationResult  # noqa: E402
from .engine import compute as _compute  # noqa: E402
from .analysis import run_analysis  # noqa: E402
from .render import render as _render  # noqa: E402
from . import market as _market  # noqa: E402

__all__ = [
    "__version__", "load", "compute", "render", "find_repo_root", "assumptions_path",
    "SchemaError", "EngineError", "MarketInputs", "ValuationResult", "validate", "validate_or_raise",
]


def find_repo_root(start: Path | None = None) -> Path:
    """Walk up from ``start`` (default: cwd) to the directory that holds ``AGENTS.md``."""
    candidates = [Path(start or os.getcwd()).resolve(), Path(__file__).resolve()]
    for origin in candidates:
        for node in (origin, *origin.parents):
            if (node / "AGENTS.md").exists():
                return node
    raise FileNotFoundError("could not find the repository root (a directory containing AGENTS.md)")


def assumptions_path(ticker_or_path: str | Path, root: Path | None = None) -> Path:
    """A ticker resolves to ``companies/<TICKER>/valuation/assumptions.yaml``; a path is used as is."""
    text = str(ticker_or_path)
    candidate = Path(text)
    if candidate.suffix in (".yaml", ".yml") or candidate.exists():
        return candidate.resolve()
    root = root or find_repo_root()
    return root / "companies" / text.upper() / "valuation" / "assumptions.yaml"


def company_dir_for(path: Path) -> Path | None:
    """``companies/<TICKER>`` for an assumptions file living in ``companies/<TICKER>/valuation/``."""
    if path.parent.name == "valuation" and path.parent.parent.parent.name == "companies":
        return path.parent.parent
    return None


def load(ticker_or_path: str | Path, root: Path | None = None) -> dict[str, Any]:
    """Load ``assumptions.yaml`` for a ticker (or a path).  Does not validate."""
    path = assumptions_path(ticker_or_path, root)
    if not path.exists():
        raise FileNotFoundError(f"{path} does not exist")
    doc = load_yaml(path)
    doc.setdefault("_path", str(path))
    return doc


def compute(assumptions: dict[str, Any], market: MarketInputs | None = None, *,
            fetch: bool = True, company_dir: str | Path | None = None,
            analysis_scenario: str = "base") -> ValuationResult:
    """Validate, resolve market data (unless given), compute every case, run the analysis."""
    doc = {k: v for k, v in assumptions.items() if k != "_path"}
    validation = validate_or_raise(doc)
    if market is None:
        market = _market.resolve(doc, fetch=fetch)
    result = _compute(doc, market, validation)
    if company_dir is None and assumptions.get("_path"):
        company_dir = company_dir_for(Path(assumptions["_path"]))
    result.company_dir = None if company_dir is None else str(company_dir)
    run_analysis(result, analysis_scenario)
    return result


def render(result: ValuationResult) -> str:
    """Render ``valuation.md`` (section 18.5 order) as a string."""
    return _render(result)
