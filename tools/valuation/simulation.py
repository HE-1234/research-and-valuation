"""Conditional operating uncertainty, using the existing FCFF engine unchanged.

This is a judgment model, not fitted company probabilities. See
``damodaran-notes/2026-09-10-monte-carlo.md`` for primary sources and design choices.
Rates are decimals; growth/margin shocks are additive, capital efficiency multiplicative.
One rank per driver is drawn for the entire path. Failed draws are retained, never refilled.
"""

from __future__ import annotations

from collections import Counter
from bisect import bisect_right
from copy import deepcopy
from dataclasses import asdict, dataclass, field, replace
from datetime import datetime, timezone
import hashlib
import json
import math
import random
import statistics
import sys
from typing import Any

from .analysis import shift_margin, transition_flag
from .engine import EngineError, ScenarioInputs, ValuationResult, faded_growth, run_scenario
from .schema import EXPLICIT_YEARS, GROWTH_BOUNDS, MARGIN_BOUNDS

MODEL_VERSION = "operating-paths-v1"
MAX_DRAWS = 20_000
DEPENDENCIES = ("independent", "same_rank", "opposite_rank")


class SimulationError(ValueError):
    """Settings or the starting valuation cannot support this experiment."""


@dataclass(frozen=True)
class Triangle:
    """Hard minimum, most likely value (mode), hard maximum; all equal means fixed."""

    minimum: float = 0.0
    mode: float = 0.0
    maximum: float = 0.0
    reason: str = ""

    def validate(self, label: str) -> None:
        numbers = (self.minimum, self.mode, self.maximum)
        if any(isinstance(x, bool) or not isinstance(x, (int, float)) or not math.isfinite(x)
               for x in numbers):
            raise SimulationError(f"{label}: minimum, most likely and maximum must be finite numbers.")
        if not self.minimum <= self.mode <= self.maximum:
            raise SimulationError(f"{label}: minimum must be at or below most likely, then maximum.")
        if not math.isfinite(self.maximum - self.minimum):
            raise SimulationError(f"{label}: the range is too wide for numerical simulation.")

    def quantile(self, rank: float) -> float:
        """Inverse triangular CDF, including endpoint modes and degenerate ranges."""
        if not 0 <= rank <= 1:
            raise SimulationError("A sampling rank must be between zero and one.")
        lo, mode, hi = self.minimum, self.mode, self.maximum
        if lo == hi or rank == 0:
            return lo
        if rank == 1:
            return hi
        width = hi - lo
        split = (mode - lo) / width
        # Scale before multiplying, avoiding products of two large bounds.
        if rank < split:
            return lo + width * math.sqrt(rank * split)
        return hi - width * math.sqrt((1 - rank) * (1 - split))


@dataclass(frozen=True)
class SimulationSettings:
    scenario: str = "base"
    draws: int = 2_000
    seed: int = 42
    growth_shift: Triangle = field(default_factory=Triangle)
    margin_shift: Triangle = field(default_factory=Triangle)
    capital_multiplier: Triangle = field(default_factory=lambda: Triangle(1.0, 1.0, 1.0))
    margin_dependency: str = "independent"
    capital_dependency: str = "independent"
    dependence_reason: str = ""

    def validate(self) -> None:
        if type(self.draws) is not int or not 1 <= self.draws <= MAX_DRAWS:
            raise SimulationError(f"Number of draws must be an integer from 1 to {MAX_DRAWS:,}.")
        if type(self.seed) is not int or not 0 <= self.seed <= 2**32 - 1:
            raise SimulationError("Seed must be an integer from 0 to 4,294,967,295.")
        for label, triangle in (("Growth shift", self.growth_shift), ("Margin shift", self.margin_shift),
                                ("Capital-efficiency multiplier", self.capital_multiplier)):
            triangle.validate(label)
        if self.capital_multiplier.minimum <= 0:
            raise SimulationError("Capital-efficiency multiplier: the entire range must be positive.")
        if self.margin_dependency not in DEPENDENCIES or self.capital_dependency not in DEPENDENCIES:
            raise SimulationError("Choose independent, same-rank or opposite-rank dependencies.")
        linked = self.margin_dependency != "independent" or self.capital_dependency != "independent"
        if linked and self.growth_shift.minimum == self.growth_shift.maximum:
            raise SimulationError("Rank links need a varying growth range. Use independent draws or vary growth.")


@dataclass
class SimulationDraw:
    index: int
    ranks: tuple[float, float, float]
    growth_shift: float
    margin_shift: float
    capital_multiplier: float
    inputs: ScenarioInputs
    per_share: float | None = None
    error: str | None = None
    transition_flagged: bool = False


@dataclass(frozen=True)
class SimulationSummary:
    attempted: int
    valid: int
    invalid: int
    mean: float | None
    median: float | None
    p10: float | None
    p90: float | None
    standard_deviation: float | None
    minimum: float | None
    maximum: float | None
    above_price: int
    fraction_above_price: float | None
    negative_values: int
    transition_flags: int


@dataclass
class SimulationResult:
    settings: SimulationSettings
    snapshot: dict[str, Any]
    fingerprint: str
    deterministic_per_share: float
    draws: list[SimulationDraw]
    summary: SimulationSummary
    invalid_reasons: dict[str, int]
    created_at: str
    model_version: str = MODEL_VERSION
    python_version: str = sys.version.split()[0]

    def to_json(self) -> str:
        """Reproducible settings + resolved starting inputs + every attempted draw.

        Nonfinite numbers in failed inputs are explicit strings, never nonstandard JSON
        numbers or silently missing records. Valid outputs are always finite.
        """
        return json.dumps(_json_safe(asdict(self)), indent=2, sort_keys=True, allow_nan=False)


def _json_safe(value: Any) -> Any:
    if isinstance(value, float) and not math.isfinite(value):
        return f"nonfinite:{value}"
    if isinstance(value, dict):
        return {k: _json_safe(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_safe(v) for v in value]
    if isinstance(value, (datetime,)) or hasattr(value, "isoformat"):
        return value.isoformat()
    return value


def _snapshot(result: ValuationResult, name: str) -> dict[str, Any]:
    if name not in result.scenarios:
        raise SimulationError(f"The {name} case is not computable. Resolve its inputs before simulating it.")
    return {
        "ticker": result.ticker, "company": result.company, "as_of_quarter": result.as_of_quarter,
        "as_of_date": result.as_of_date, "engine_version": result.engine_version,
        "inputs": asdict(result.scenarios[name].inputs), "base_year": asdict(result.base_year),
        "bridge": asdict(result.bridge), "market": asdict(result.market),
        "assumptions": {k: v for k, v in result.assumptions.items() if k != "_path"},
        "baseline_warnings": result.warnings,
    }


def simulation_fingerprint(result: ValuationResult, settings: SimulationSettings) -> str:
    """Ignore compute timestamps; detect edits to assumptions, market data or settings."""
    payload = {"snapshot": _snapshot(result, settings.scenario), "settings": asdict(settings),
               "model_version": MODEL_VERSION}
    return hashlib.sha256(json.dumps(_json_safe(payload), sort_keys=True, allow_nan=False).encode()).hexdigest()


def sample_inputs(inp: ScenarioInputs, growth_shift: float, margin_shift: float,
                  capital_multiplier: float) -> ScenarioInputs:
    """Transform authored paths, then let the FCFF engine derive cash flows and returns.

    Growth's automatic fade is rebuilt independently of margin's path length. This
    matters for cases with five growth entries and ten separately authored margins.
    """
    n = inp.explicit_years or inp.horizon
    growth = [g + growth_shift for g in inp.growth[:n]]
    if n == EXPLICIT_YEARS and inp.horizon == 10:
        growth += faded_growth(growth[-1], inp.terminal_growth)
    # Existing sensitivity convention: one fifth of the margin shift each year to year 5,
    # then the whole shift, including on an explicitly shaped late margin path.
    changed = shift_margin(inp, margin_shift)
    return replace(changed, growth=growth, sales_to_capital=inp.sales_to_capital * capital_multiplier,
                   sales_to_capital_late=inp.sales_to_capital_late * capital_multiplier,
                   reinvestment_override=list(inp.reinvestment_override))


def _has_nonfinite(value: Any) -> bool:
    if isinstance(value, float):
        return not math.isfinite(value)
    if isinstance(value, dict):
        return any(_has_nonfinite(v) for v in value.values())
    if isinstance(value, (tuple, list)):
        return any(_has_nonfinite(v) for v in value)
    return False


def _path_error(inp: ScenarioInputs) -> str | None:
    if _has_nonfinite(asdict(inp)):
        return "Sampled inputs contain a nonfinite number."
    for label, values, bounds in (("Growth", inp.growth, GROWTH_BOUNDS),
                                   ("Margin", inp.margin, MARGIN_BOUNDS)):
        if any(x < bounds[0] or x > bounds[1] for x in values):
            return f"{label} path outside the engine's {bounds[0]:.0%} to {bounds[1]:.0%} input bounds."
    if inp.sales_to_capital <= 0 or inp.sales_to_capital_late <= 0:
        return "Sales-to-capital must be positive in both periods."
    return None


def _linked_rank(growth_rank: float, independent_rank: float, dependency: str) -> float:
    if dependency == "same_rank":
        return growth_rank
    if dependency == "opposite_rank":
        return 1 - growth_rank
    return independent_rank


def empirical_quantile(ordered: list[float], probability: float) -> float:
    """Linear interpolation at (n-1)*p (the usual inclusive/type-7 quantile)."""
    position = (len(ordered) - 1) * probability
    i = int(position)
    if i == len(ordered) - 1:
        return ordered[i]
    if ordered[i] == ordered[i + 1]:
        return ordered[i]
    fraction = position - i
    return ordered[i] * (1 - fraction) + ordered[i + 1] * fraction


def summarize(draws: list[SimulationDraw], price: float) -> SimulationSummary:
    values = sorted(d.per_share for d in draws if d.error is None and d.per_share is not None)
    n = len(values)
    above = sum(v > price for v in values)
    return SimulationSummary(
        attempted=len(draws), valid=n, invalid=len(draws) - n,
        mean=statistics.mean(values) if n else None,
        median=empirical_quantile(values, 0.5) if n else None,
        p10=empirical_quantile(values, 0.1) if n else None,
        p90=empirical_quantile(values, 0.9) if n else None,
        standard_deviation=statistics.pstdev(values) if n else None,
        minimum=values[0] if n else None, maximum=values[-1] if n else None,
        above_price=above, fraction_above_price=above / n if n else None,
        negative_values=sum(v < 0 for v in values),
        transition_flags=sum(d.transition_flagged for d in draws if d.error is None),
    )


def histogram(result: SimulationResult, bins: int = 30) -> list[dict[str, float | int]]:
    """Equal-width bins counted here so the app chart and export can be reconciled.

    A point distribution receives one centered display bin; values themselves never move.
    Bins include their lower edge, exclude the upper edge, except the last includes both.
    Duplicate edges from floating-point rounding are merged before counting.
    """
    if type(bins) is not int or bins < 1:
        raise SimulationError("Histogram bin count must be a positive integer.")
    values = [d.per_share for d in result.draws if d.error is None and d.per_share is not None]
    if not values:
        return []
    lo, hi = min(values), max(values)
    if lo == hi:
        pad = max(abs(lo) * 0.01, 0.01)
        return [{"lower": lo - pad, "upper": hi + pad, "count": len(values)}]
    width = (hi - lo) / bins
    edges = sorted(set([lo + i * width for i in range(bins)] + [hi]))
    counts = [0] * (len(edges) - 1)
    for value in values:
        # Count against the actual displayed edges, including when a narrow range
        # rounds several nominal edges to the same float. The maximum stays in the last bin.
        index = min(bisect_right(edges, value) - 1, len(counts) - 1)
        counts[index] += 1
    return [{"lower": edges[i], "upper": edges[i + 1],
             "count": count} for i, count in enumerate(counts)]


def simulate(result: ValuationResult, settings: SimulationSettings | None = None) -> SimulationResult:
    """Run a seeded selected-case experiment from an already computed valuation.

    No market fetch, file writes, global RNG changes, scenario mixing or rejection
    sampling. Only known arithmetic/model failures become invalid draws; programming
    errors propagate. Terminal and bridge assumptions stay at their resolved values.
    """
    settings = settings or SimulationSettings()
    settings.validate()
    snapshot = deepcopy(_snapshot(result, settings.scenario))
    original = deepcopy(result.scenarios[settings.scenario].inputs)
    base, bridge = deepcopy(result.base_year), deepcopy(result.bridge)
    price = result.market.price
    if _has_nonfinite((asdict(original), asdict(base), asdict(bridge), asdict(result.market))):
        raise SimulationError("The starting valuation contains nonfinite inputs.")
    start_error = _path_error(original)
    if start_error:
        raise SimulationError("The starting valuation is invalid: " + start_error)
    baseline = run_scenario(original, base, bridge, price)
    if _has_nonfinite(asdict(baseline)):
        raise SimulationError("The starting valuation has a nonfinite result.")
    rng = random.Random(settings.seed)
    draws = []
    for i in range(settings.draws):
        # Always consume three ranks: dependence choices do not shift later growth draws.
        ug, um, uc = (rng.random() for _ in range(3))
        um = _linked_rank(ug, um, settings.margin_dependency)
        uc = _linked_rank(ug, uc, settings.capital_dependency)
        dg, dm, multiplier = (settings.growth_shift.quantile(ug), settings.margin_shift.quantile(um),
                              settings.capital_multiplier.quantile(uc))
        inp = sample_inputs(original, dg, dm, multiplier)
        draw = SimulationDraw(i + 1, (ug, um, uc), dg, dm, multiplier, inp)
        draw.error = _path_error(inp)
        if draw.error is None:
            try:
                valued = run_scenario(inp, base, bridge, price)
                if _has_nonfinite(asdict(valued)):
                    draw.error = "The engine produced a nonfinite result."
                else:
                    draw.per_share = valued.per_share
                    last, terminal = valued.rows[-1], valued.terminal
                    draw.transition_flagged = transition_flag(
                        last.fcff, terminal.fcff, last.roic, terminal.roic)
            except (EngineError, ArithmeticError) as exc:
                draw.error = f"{type(exc).__name__}: {exc}"
        draws.append(draw)
    return SimulationResult(
        settings=settings, snapshot=snapshot, fingerprint=simulation_fingerprint(result, settings),
        deterministic_per_share=baseline.per_share, draws=draws, summary=summarize(draws, price),
        invalid_reasons=dict(Counter(d.error for d in draws if d.error)),
        created_at=datetime.now(timezone.utc).isoformat(),
    )
