"""Damodaran's industry datasets: download, cache as CSV, look up by industry name.

Files (AGENTS.md section 18.8), all under ``https://pages.stern.nyu.edu/~adamodar/``:
``pc/implprem/ERPbymonth.xlsx`` and ``pc/datasets/{betas,wacc,capex,margin,taxrate,histgr}.xls``
(``fundgr.xls`` is the fallback if ``histgr.xls`` is missing).  The cache lives in
``tools/valuation/data/damodaran/`` next to a ``MANIFEST.md``; it is refreshed only by
``uv run value --refresh-data``.
"""

from __future__ import annotations

import csv
import json
import re
import urllib.request
from dataclasses import dataclass, field
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

import openpyxl
import xlrd

BASE_URL = "https://pages.stern.nyu.edu/~adamodar/"
DATA_DIR = Path(__file__).resolve().parent / "data" / "damodaran"
USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")


@dataclass(frozen=True)
class DatasetSpec:
    key: str
    remote: str
    sheet: str
    csv_name: str
    columns: dict[str, str]                 # purpose -> exact header text in the sheet
    fallback_remote: str | None = None


SPECS: tuple[DatasetSpec, ...] = (
    DatasetSpec("erp", "pc/implprem/ERPbymonth.xlsx", "Historical ERP", "ERPbymonth.csv",
                {"date": "Start of month", "tbond": "T.Bond Rate", "erp": "ERP (T12m)"}),
    DatasetSpec("betas", "pc/datasets/betas.xls", "Industry Averages", "betas.csv",
                {"unlevered_beta_cash_corrected": "Unlevered beta corrected for cash"}),
    DatasetSpec("wacc", "pc/datasets/wacc.xls", "Industry Averages", "wacc.csv",
                {"cost_of_capital": "Cost of Capital"}),
    DatasetSpec("capex", "pc/datasets/capex.xls", "Industry Averages", "capex.csv",
                {"sales_to_capital": "Sales/ Invested Capital (LTM)"}),
    DatasetSpec("margin", "pc/datasets/margin.xls", "Industry Averages", "margin.csv",
                {"pretax_operating_margin": "Pre-tax Unadjusted Operating Margin"}),
    DatasetSpec("taxrate", "pc/datasets/taxrate.xls", "Industry Averages", "taxrate.csv",
                {"effective_tax_rate": "Aggregate tax rate"}),
    DatasetSpec("histgr", "pc/datasets/histgr.xls", "Industry Averages", "histgr.csv",
                {"revenue_cagr_5y": "CAGR in Revenues- Last 5 years"},
                fallback_remote="pc/datasets/fundgr.xls"),
)
SPEC_BY_KEY = {s.key: s for s in SPECS}


class DatasetError(Exception):
    """A dataset is missing from the cache or could not be parsed."""


@dataclass
class Table:
    headers: list[str]
    rows: list[list[str]]
    meta: dict[str, Any] = field(default_factory=dict)

    def column(self, header: str) -> int:
        want = _norm(header)
        for i, h in enumerate(self.headers):
            if _norm(h) == want:
                return i
        raise DatasetError(f"column {header!r} not found; have {self.headers}")


@dataclass
class IndustryValue:
    value: float | None
    dataset: str
    dataset_date: str | None
    matched_name: str | None
    column: str


@dataclass
class ERPRow:
    date: str
    tbond_rate: float
    erp: float
    dataset_date: str | None
    fetched: str | None


def _norm(text: str) -> str:
    return re.sub(r"\s+", " ", str(text)).strip().lower()


# --------------------------------------------------------------------------- #
# Download and parse
# --------------------------------------------------------------------------- #

def _download(remote: str, timeout: int = 60) -> bytes:
    req = urllib.request.Request(BASE_URL + remote, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def _excel_date(x: Any) -> str | None:
    if isinstance(x, (int, float)) and x > 20000:
        return xlrd.xldate_as_datetime(float(x), 0).date().isoformat()
    if isinstance(x, datetime):
        return x.date().isoformat()
    return None


def _cell_text(x: Any) -> str:
    if x is None:
        return ""
    if isinstance(x, datetime):
        return x.date().isoformat()
    if isinstance(x, float) and x.is_integer() and abs(x) < 1e15:
        return str(int(x)) if abs(x) >= 1 else repr(x)
    return str(x)


def parse_industry_sheet(raw: bytes, sheet: str) -> Table:
    """Industry sheets: a 'Date updated:' cell, then a header row starting 'Industry Name'."""
    book = xlrd.open_workbook(file_contents=raw)
    sh = book.sheet_by_name(sheet)
    updated = None
    header_row = None
    for r in range(sh.nrows):
        first = _norm(sh.cell_value(r, 0))
        if first.startswith("date updated"):
            updated = _excel_date(sh.cell_value(r, 1))
        if first.startswith("industry name"):
            header_row = r
            break
    if header_row is None:
        raise DatasetError(f"no 'Industry Name' header row in sheet {sheet!r}")
    headers = [str(sh.cell_value(header_row, c)).strip() for c in range(sh.ncols)]
    rows: list[list[str]] = []
    for r in range(header_row + 1, sh.nrows):
        name = str(sh.cell_value(r, 0)).strip()
        if not name:
            break
        rows.append([_cell_text(sh.cell_value(r, c)) for c in range(sh.ncols)])
    return Table(headers, rows, {"date_updated": updated, "header_row": header_row})


def parse_erp_sheet(raw: bytes, sheet: str) -> Table:
    """ERPbymonth 'Historical ERP': header in row 1, one row per month, dates in column A."""
    import io
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        book = openpyxl.load_workbook(io.BytesIO(raw), data_only=True, read_only=True)
    ws = book[sheet]
    rows_iter = ws.iter_rows(values_only=True)
    headers = [str(h).strip() if h is not None else "" for h in next(rows_iter)]
    rows: list[list[str]] = []
    for row in rows_iter:
        if not row or not isinstance(row[0], datetime):
            continue
        rows.append([_cell_text(x) for x in row[:len(headers)]])
    latest = rows[-1][0] if rows else None
    return Table(headers, rows, {"date_updated": latest, "header_row": 0})


def _write_csv(path: Path, table: Table) -> None:
    with open(path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(table.headers)
        writer.writerows(table.rows)


def refresh(data_dir: Path = DATA_DIR, timeout: int = 60) -> dict[str, Any]:
    """Download every dataset, write CSVs and MANIFEST.md, return the manifest mapping."""
    data_dir.mkdir(parents=True, exist_ok=True)
    fetched = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    manifest: dict[str, Any] = {"fetched": fetched, "datasets": {}}
    for spec in SPECS:
        remote = spec.remote
        try:
            raw = _download(remote, timeout)
        except Exception as exc:                       # noqa: BLE001 - report and try fallback
            if not spec.fallback_remote:
                raise DatasetError(f"{spec.remote}: {exc}") from exc
            remote = spec.fallback_remote
            raw = _download(remote, timeout)
        table = parse_erp_sheet(raw, spec.sheet) if spec.key == "erp" else parse_industry_sheet(raw, spec.sheet)
        _write_csv(data_dir / spec.csv_name, table)
        missing = [h for h in spec.columns.values() if _norm(h) not in {_norm(x) for x in table.headers}]
        if missing:
            raise DatasetError(f"{remote}: expected columns missing: {missing}")
        manifest["datasets"][spec.key] = {
            "url": BASE_URL + remote, "file": spec.csv_name, "fetched": fetched,
            "date_updated": table.meta.get("date_updated"), "rows": len(table.rows),
            "header_row": table.meta.get("header_row"), "sheet": spec.sheet,
            "columns_used": dict(spec.columns),
            "note": ("histgr.xls was missing; fundgr.xls used instead" if remote == spec.fallback_remote
                     else None),
        }
    (data_dir / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    (data_dir / "MANIFEST.md").write_text(_manifest_markdown(manifest, data_dir), encoding="utf-8")
    return manifest


def _manifest_markdown(manifest: dict[str, Any], data_dir: Path) -> str:
    lines = [
        "# Damodaran datasets (cached)",
        "",
        f"Fetched {manifest['fetched']} by `uv run value --refresh-data`.  Source: Aswath Damodaran, "
        "NYU Stern, https://pages.stern.nyu.edu/~adamodar/New_Home_Page/data.html.  Each CSV is the "
        "data block of the named sheet, headers kept verbatim.  \"Last updated\" is the file's own "
        "'Date updated:' cell (industry files) or the latest monthly row (ERP file).",
        "",
        "| Dataset | File | URL | Fetched | Last updated in file | Rows | Columns used |",
        "|---|---|---|---|---|---|---|",
    ]
    for key, d in manifest["datasets"].items():
        cols = "; ".join(f"{purpose} = `{header}`" for purpose, header in d["columns_used"].items())
        lines.append(f"| {key} | `{d['file']}` | {d['url']} | {d['fetched']} | {d['date_updated'] or 'n/a'} "
                     f"| {d['rows']} | {cols} |")
    notes = [d["note"] for d in manifest["datasets"].values() if d.get("note")]
    lines += ["", "Notes:", ""]
    lines.append("- `histgr.xls` existed; `fundgr.xls` was not needed." if not notes else "- " + "; ".join(notes))
    lines.append("- Industry lookups are case-insensitive: exact name first, then substring; the matched "
                 "name is printed in valuation.md.")
    lines.append("- `taxrate.csv` has two `Aggregate tax rate` columns (effective, then cash); the first is used.")
    lines.append("- The ERP row used is the last month with a date and a numeric `ERP (T12m)`; `T.Bond Rate` "
                 "is the 10-year Treasury at the start of that month.")
    try:
        erp = latest_erp(data_dir)
        lines.append(f"- Latest ERP row: {erp.date}, T-bond {erp.tbond_rate:.4f}, ERP {erp.erp:.4f}.")
    except DatasetError:
        pass
    return "\n".join(lines) + "\n"


# --------------------------------------------------------------------------- #
# Reading the cache
# --------------------------------------------------------------------------- #

_CACHE: dict[Path, Table] = {}


def load_manifest(data_dir: Path = DATA_DIR) -> dict[str, Any]:
    path = data_dir / "manifest.json"
    if not path.exists():
        return {"fetched": None, "datasets": {}}
    return json.loads(path.read_text(encoding="utf-8"))


def load_table(key: str, data_dir: Path = DATA_DIR) -> Table:
    spec = SPEC_BY_KEY[key]
    path = data_dir / spec.csv_name
    if path in _CACHE:
        return _CACHE[path]
    if not path.exists():
        raise DatasetError(f"{path.name} is not cached; run `uv run value --refresh-data`")
    with open(path, newline="", encoding="utf-8") as fh:
        reader = csv.reader(fh)
        headers = next(reader)
        rows = [r for r in reader]
    info = load_manifest(data_dir)["datasets"].get(key, {})
    table = Table(headers, rows, {"date_updated": info.get("date_updated"), "fetched": info.get("fetched")})
    _CACHE[path] = table
    return table


def find_industry(table: Table, industry: str) -> list[str] | None:
    """Case-insensitive exact match first, then substring (shortest name wins)."""
    want = _norm(industry)
    if not want:
        return None
    for row in table.rows:
        if _norm(row[0]) == want:
            return row
    candidates = [row for row in table.rows if want in _norm(row[0]) or _norm(row[0]) in want]
    if not candidates:
        return None
    return min(candidates, key=lambda r: len(r[0]))


def _to_float(text: str) -> float | None:
    try:
        return float(text)
    except (TypeError, ValueError):
        return None


def lookup(key: str, industry: str, purpose: str, data_dir: Path = DATA_DIR) -> IndustryValue:
    spec = SPEC_BY_KEY[key]
    header = spec.columns[purpose]
    table = load_table(key, data_dir)
    row = find_industry(table, industry)
    if row is None:
        return IndustryValue(None, key, table.meta.get("date_updated"), None, header)
    return IndustryValue(_to_float(row[table.column(header)]), key, table.meta.get("date_updated"),
                         row[0], header)


@dataclass
class IndustryFigures:
    industry: str
    unlevered_beta_cash_corrected: IndustryValue
    cost_of_capital: IndustryValue
    sales_to_capital: IndustryValue
    pretax_operating_margin: IndustryValue
    revenue_cagr_5y: IndustryValue
    effective_tax_rate: IndustryValue


def industry_figures(industry: str, data_dir: Path = DATA_DIR) -> IndustryFigures:
    return IndustryFigures(
        industry=industry,
        unlevered_beta_cash_corrected=lookup("betas", industry, "unlevered_beta_cash_corrected", data_dir),
        cost_of_capital=lookup("wacc", industry, "cost_of_capital", data_dir),
        sales_to_capital=lookup("capex", industry, "sales_to_capital", data_dir),
        pretax_operating_margin=lookup("margin", industry, "pretax_operating_margin", data_dir),
        revenue_cagr_5y=lookup("histgr", industry, "revenue_cagr_5y", data_dir),
        effective_tax_rate=lookup("taxrate", industry, "effective_tax_rate", data_dir),
    )


def latest_erp(data_dir: Path = DATA_DIR) -> ERPRow:
    """The last month with a date, a numeric T-bond rate, and a numeric implied ERP (T12m)."""
    table = load_table("erp", data_dir)
    spec = SPEC_BY_KEY["erp"]
    ci_date, ci_tbond, ci_erp = (table.column(spec.columns[k]) for k in ("date", "tbond", "erp"))
    for row in reversed(table.rows):
        tbond, erp = _to_float(row[ci_tbond]), _to_float(row[ci_erp])
        if row[ci_date] and tbond is not None and erp is not None:
            return ERPRow(row[ci_date], tbond, erp, table.meta.get("date_updated"), table.meta.get("fetched"))
    raise DatasetError("ERPbymonth.csv has no usable row")


def dataset_sources(data_dir: Path = DATA_DIR) -> list[tuple[str, str, str | None, str | None]]:
    """(key, url, fetched, date_updated) for the Sources section."""
    man = load_manifest(data_dir)
    return [(k, d["url"], d.get("fetched"), d.get("date_updated")) for k, d in man["datasets"].items()]


def today() -> str:
    return date.today().isoformat()
