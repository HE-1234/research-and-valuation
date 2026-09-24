"""``value <TICKER> [--validate] [--dry-run] [--diagnostics-only] [--set path=value ...] [--json] [--refresh-data] [--no-fetch] [--render-assumptions]``.

The normal run (fetch, compute, archive, write ``valuation.md`` and ``assumptions.md``) lives in
:func:`run_and_write` so the app can call the very same code path.
"""

from __future__ import annotations

import argparse
import dataclasses
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

from . import (
    EngineError, SchemaError, __version__, assumptions_path, company_dir_for, compute, find_repo_root,
    load, render, write_assumptions_md,
)
from . import datasets
from .analysis import transition_check
from .engine import MarketInputs, ValuationResult
from .market import MarketError
from .render import results_text
from .schema import coerce_scalar, set_path, validate


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="value",
        description="Compute a company's free-cash-flow-to-the-firm valuation from "
                    "companies/<TICKER>/valuation/assumptions.yaml (AGENTS.md section 18).",
    )
    p.add_argument("ticker", nargs="?", help="ticker (folder under companies/) or a path to an assumptions.yaml")
    p.add_argument("--validate", action="store_true", help="validate the assumptions file only; exit 0 or 1")
    p.add_argument("--dry-run", action="store_true", help="compute and print, but write nothing")
    p.add_argument("--diagnostics-only", action="store_true",
                   help="print draft-review diagnostics as JSON, without valuation results or file writes")
    p.add_argument("--set", action="append", default=[], metavar="PATH=VALUE",
                   help="override a YAML cell in memory, e.g. scenarios.base.operating_margin.values.4=0.34")
    p.add_argument("--json", action="store_true", help="print the full result as JSON instead of the table")
    p.add_argument("--refresh-data", action="store_true", help="re-download Damodaran's datasets and exit")
    p.add_argument("--no-fetch", action="store_true", help="no network: 'auto' market cells must be --set")
    p.add_argument("--render-assumptions", action="store_true",
                   help="write companies/<TICKER>/valuation/assumptions.md from the YAML and nothing else "
                        "(no market fetch, no compute)")
    p.add_argument("--version", action="version", version=f"valuation {__version__}")
    return p


def apply_sets(doc: dict[str, Any], sets: list[str]) -> dict[str, Any]:
    for item in sets:
        if "=" not in item:
            raise SchemaError(f"--set expects PATH=VALUE, got {item!r}")
        path, raw = item.split("=", 1)
        doc = set_path(doc, path.strip(), coerce_scalar(raw))
    return doc


def _print_validation(v, out) -> None:
    for e in v.errors:
        print(f"error: {e}", file=out)
    for w in v.warnings:
        print(f"warning: {w}", file=out)
    for path in v.shared_nulls:
        print(f"null: {path} (stops every scenario)", file=out)
    for name, reasons in v.stopped.items():
        for r in reasons:
            print(f"null: {name} scenario stopped: {r}", file=out)
    for name, reason in v.skipped.items():
        print(f"skipped: {name} scenario ({reason})", file=out)


def refresh_data(out) -> int:
    manifest = datasets.refresh()
    for key, d in manifest["datasets"].items():
        print(f"{key:8s} {d['file']:16s} rows={d['rows']:<4d} dated {d['date_updated']}  {d['url']}", file=out)
    erp = datasets.latest_erp()
    print(f"latest ERP row: {erp.date}  T-bond {erp.tbond_rate:.4f}  ERP {erp.erp:.4f}", file=out)
    print(f"written to {datasets.DATA_DIR}", file=out)
    return 0


def archive_previous(valuation_dir: Path, out) -> None:
    md = valuation_dir / "valuation.md"
    if not md.exists():
        return
    stamp = datetime.now().strftime("%Y-%m-%d-%H%M")
    target = valuation_dir / "history" / stamp
    target.mkdir(parents=True, exist_ok=True)
    shutil.copy2(md, target / "valuation.md")
    yaml_path = valuation_dir / "assumptions.yaml"
    if yaml_path.exists():
        shutil.copy2(yaml_path, target / "assumptions.yaml")
    print(f"archived previous valuation.md and assumptions.yaml to {target}", file=out)


def run_and_write(path: Path, doc: dict[str, Any], *, market: MarketInputs | None = None,
                  fetch: bool = True, out=None) -> ValuationResult:
    """The normal run: archive the previous pair, compute, write ``valuation.md`` and ``assumptions.md``.

    ``doc`` is the document to compute (it may carry in-memory ``--set`` overrides);
    ``assumptions.md`` is always rendered from the YAML on disk so it mirrors the file.
    The app calls this with the market inputs from its sidebar.
    """
    out = out or sys.stdout
    result = compute(doc, market=market, fetch=fetch, company_dir=company_dir_for(path))
    text = render(result)
    valuation_dir = path.parent
    archive_previous(valuation_dir, out)
    (valuation_dir / "valuation.md").write_text(text, encoding="utf-8")
    md = write_assumptions_md(path)
    print(results_text(result), file=out)
    print(f"written {valuation_dir / 'valuation.md'}", file=out)
    print(f"written {md}", file=out)
    return result


def _json_default(obj: Any) -> Any:
    if dataclasses.is_dataclass(obj):
        return dataclasses.asdict(obj)
    if isinstance(obj, Path):
        return str(obj)
    return str(obj)


def diagnostics_payload(result: ValuationResult) -> dict[str, Any]:
    """Allowlist draft-review fields; never serialize the full valuation result.

    The engine still computes normally. Its asset/equity/per-share values, present
    values, reference valuations, sensitivities and reverse DCF stay internal.
    """
    fields = ("revenue", "growth", "margin", "ebit_after_tax", "reinvestment", "fcff", "wacc", "roic")
    scenarios = {}
    for name, scenario in result.scenarios.items():
        scenarios[name] = {
            "years": [{"year": row.year, **{key: getattr(row, key) for key in fields}}
                      for row in scenario.rows],
            "terminal": {"year": scenario.inputs.horizon + 1,
                         **{key: getattr(scenario.terminal, key) for key in fields}},
        }
    return {
        "ticker": result.ticker,
        "as_of_quarter": result.as_of_quarter,
        "computed_at": result.computed_at,
        "engine_version": result.engine_version,
        "market": dataclasses.asdict(result.market),
        "base_year": dataclasses.asdict(result.base_year),
        "cost_of_capital": dataclasses.asdict(result.cost_of_capital),
        "industry": dataclasses.asdict(result.analysis.industry) if result.analysis.industry else None,
        "scenarios": scenarios,
        "transition_check": dataclasses.asdict(transition_check(result)),
        "stopped": result.stopped,
        "skipped": result.skipped,
        "warnings": result.warnings,
    }


def main(argv: list[str] | None = None) -> int:
    out, err = sys.stdout, sys.stderr
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.diagnostics_only and (args.validate or args.refresh_data or args.render_assumptions):
        parser.error("--diagnostics-only cannot be combined with --validate, --refresh-data or --render-assumptions")
    if args.refresh_data:
        try:
            return refresh_data(out)
        except Exception as exc:                        # noqa: BLE001 - report to the owner
            print(f"error: dataset refresh failed: {exc}", file=err)
            return 1
    if not args.ticker:
        build_parser().print_usage(err)
        print("error: a ticker or a path to assumptions.yaml is required", file=err)
        return 2
    try:
        path = assumptions_path(args.ticker, find_repo_root() if not Path(args.ticker).exists() else None)
        doc = load(path)
        doc = apply_sets(doc, args.set)
    except (FileNotFoundError, SchemaError) as exc:
        print(f"error: {exc}", file=err)
        return 1
    if args.render_assumptions:
        if args.set:
            print("note: --set overrides are ignored by --render-assumptions; assumptions.md mirrors the file", file=err)
        md = write_assumptions_md(path)
        print(f"written {md}", file=out)
        return 0
    validation = validate({k: v for k, v in doc.items() if k != "_path"})
    if args.validate:
        _print_validation(validation, out)
        computable = validation.computable_scenarios()
        if validation.ok and computable:
            print(f"ok: {path} validates; computable scenarios: {', '.join(computable)}", file=out)
            return 0
        if validation.ok:
            print("error: no scenario can be computed (see nulls above)", file=out)
        return 1
    if not validation.ok:
        _print_validation(validation, err)
        return 1
    try:
        if args.json or args.dry_run or args.diagnostics_only:
            result = compute(doc, fetch=not args.no_fetch, company_dir=company_dir_for(path))
        else:
            run_and_write(path, doc, fetch=not args.no_fetch, out=out)
            return 0
    except MarketError as exc:
        print(f"error: {exc}", file=err)
        return 1
    except (SchemaError, EngineError) as exc:
        print(f"error: {exc}", file=err)
        return 1
    if args.diagnostics_only:
        print(json.dumps(diagnostics_payload(result), indent=2, default=_json_default), file=out)
        return 0
    if args.json:
        payload = dataclasses.asdict(result)
        payload.pop("assumptions", None)
        print(json.dumps(payload, indent=2, default=_json_default), file=out)
        return 0
    render(result)                      # the render must succeed even on a dry run
    print(results_text(result), file=out)
    print("dry run: nothing written", file=out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
