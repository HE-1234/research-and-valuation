"""Pull Damodaran's inputs and outputs out of ``AlphabetApr2018.xlsx`` and ``NVIDIA2023.xlsx``.

Cell addresses were read from the workbooks' formulas (openpyxl without ``data_only``);
values come from the cached results (``data_only=True``).  Run as a script to rewrite
``fixtures/damodaran_workbooks.json`` when the workbooks are present in ``/tmp/damo``.
"""

from __future__ import annotations

import json
import sys
import warnings
from pathlib import Path
from typing import Any

WORKBOOK_DIR = Path("/tmp/damo")
FIXTURE = Path(__file__).resolve().parent / "fixtures" / "damodaran_workbooks.json"
YEAR_COLUMNS = "CDEFGHIJKL"          # years 1..10 on the Valuation output sheet; M is the terminal year


def _open(path: Path):
    import openpyxl
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return openpyxl.load_workbook(path, data_only=True)


def _row(ws, row: int, columns: str = YEAR_COLUMNS) -> list[float]:
    return [float(ws[f"{c}{row}"].value) for c in columns]


def extract_alphabet(path: Path) -> dict[str, Any]:
    wb = _open(path)
    inp, out = wb["Input sheet"], wb["Valuation output"]
    lease, rnd = wb["Operating lease converter"], wb["R& D converter"]
    return {
        "workbook": path.name,
        "inputs": {
            "revenue": inp["B8"].value,
            "ebit_reported": inp["B9"].value,
            "ebit_adjusted": out["B5"].value,                  # reported + lease adj (F32) + R&D adj (D39)
            "lease_adjustment_to_ebit": lease["F32"].value,
            "rnd_adjustment_to_ebit": rnd["D39"].value,
            "rnd_asset": rnd["D35"].value,
            "rnd_amortization_years": rnd["F6"].value,
            "rnd_current": rnd["F7"].value,
            "rnd_history_oldest_first": [rnd["B13"].value, rnd["B12"].value, rnd["B11"].value],
            "book_equity": inp["B11"].value,
            "book_debt": inp["B12"].value,
            "lease_debt": lease["C28"].value,
            "invested_capital": out["B39"].value,
            "effective_tax": inp["B20"].value,
            "marginal_tax": inp["B21"].value,
            "year1_growth": out["C2"].value,
            "cagr_years_2_5": out["D2"].value,
            "target_margin": inp["B24"].value,
            "base_margin": out["B4"].value,
            "convergence_year": inp["B25"].value,
            "sales_to_capital_1_5": out["C38"].value,
            "sales_to_capital_6_10": out["H38"].value,
            "risk_free": inp["B28"].value,
            "initial_wacc": inp["B29"].value,
            "stable_wacc": out["M12"].value,
            "terminal_growth": out["M2"].value,
            "stable_roic": out["M40"].value,
            "stable_tax": out["M6"].value,
            "cash_reported": inp["B15"].value,
            "cash_used": out["B27"].value,                     # after the trapped-cash tax haircut
            "trapped_cash": inp["B59"].value,
            "trapped_cash_tax": inp["B60"].value,
            "cross_holdings": out["B28"].value,
            "debt_used": out["B25"].value,                     # book debt + lease debt
            "minority_interests": out["B26"].value,
            "option_value": out["B30"].value,
            "shares": out["B32"].value,
            "price": inp["B19"].value,
            "failure_probability": out["B22"].value,
            "reinvestment_lag": 0,                             # row 8 uses (Rev_t - Rev_{t-1}) / SC
        },
        "paths": {
            "growth": _row(out, 2),
            "margin": _row(out, 4),
            "revenue": _row(out, 3),
            "tax": _row(out, 6),
            "wacc": _row(out, 12),
            "reinvestment": _row(out, 8),
        },
        "outputs": {
            "pv_fcff_10y": out["B20"].value,
            "terminal_value": out["B18"].value,
            "pv_terminal": out["B19"].value,
            "operating_assets": out["B24"].value,
            "equity": out["B31"].value,
            "per_share": out["B33"].value,
        },
    }


def extract_nvidia(path: Path) -> dict[str, Any]:
    wb = _open(path)
    inp, out, rnd = wb["Input sheet"], wb["Valuation output"], wb["R& D converter"]
    rest_rev, ai_rev, auto_rev = _row(out, 3), _row(out, 14), _row(out, 23)
    rest_ebit, ai_ebit, auto_ebit = _row(out, 5), _row(out, 16), _row(out, 25)
    return {
        "workbook": path.name,
        "inputs": {
            "revenue": inp["B10"].value,                        # total; split into rest / AI / auto below
            "ebit_reported": inp["B11"].value,
            "rnd_adjustment_to_ebit": rnd["D39"].value,
            "rnd_asset": rnd["D35"].value,
            "rnd_amortization_years": rnd["F6"].value,
            "rnd_current": rnd["F7"].value,
            "rnd_history_oldest_first": [rnd[f"B{r}"].value for r in (15, 14, 13, 12, 11)],
            "ebit_adjusted": out["B5"].value + out["B16"].value + out["B25"].value,
            "book_equity": inp["B13"].value,
            "book_debt": inp["B14"].value,
            "invested_capital": out["B58"].value,
            "effective_tax": inp["B22"].value,
            "marginal_tax": inp["B23"].value,
            "year1_growth": inp["B25"].value,                   # rest-of-business segment
            "year1_margin": inp["B26"].value,
            "cagr_years_2_5": inp["B27"].value,
            "target_margin": inp["B28"].value,
            "convergence_year": inp["B29"].value,
            "sales_to_capital_1_5": inp["B30"].value,
            "sales_to_capital_6_10": inp["B31"].value,
            "risk_free": inp["B33"].value,
            "initial_wacc": inp["B34"].value,
            "mature_market_erp": wb["Country equity risk premiums"]["B1"].value,
            "stable_wacc": out["M30"].value,
            "terminal_growth": out["M2"].value,
            "stable_roic": out["M59"].value,
            "stable_tax": out["M6"].value,
            "cash_used": out["B46"].value,
            "cross_holdings": out["B47"].value,
            "debt_used": out["B44"].value,
            "minority_interests": out["B45"].value,
            "option_value": out["B49"].value,
            "shares": out["B51"].value,
            "price": inp["B21"].value,
            "failure_probability": out["B41"].value,
            "reinvestment_lag": 1,
            "segments": {
                "ai": {"market_now": inp["B44"].value, "market_year10": inp["C44"].value,
                       "share_now": inp["B45"].value, "share_year10": inp["C45"].value,
                       "margin_now": inp["B46"].value, "margin_target": inp["C46"].value,
                       "revenue_base": out["B14"].value, "ebit_base": out["B16"].value},
                "auto": {"market_now": inp["B50"].value, "market_year10": inp["C50"].value,
                         "share_now": inp["B51"].value, "share_year10": inp["C51"].value,
                         "margin_now": inp["B52"].value, "margin_target": inp["C52"].value,
                         "revenue_base": out["B23"].value, "ebit_base": out["B25"].value},
                "rest": {"revenue_base": out["B3"].value, "ebit_base": out["B5"].value},
            },
        },
        "paths": {
            "revenue_rest": rest_rev, "revenue_ai": ai_rev, "revenue_auto": auto_rev,
            "ebit_rest": rest_ebit, "ebit_ai": ai_ebit, "ebit_auto": auto_ebit,
            "tax": _row(out, 6), "wacc": _row(out, 30),
        },
        "outputs": {
            "value_rest": out["B37"].value,
            "value_ai": out["B38"].value,
            "value_auto": out["B39"].value,
            "operating_assets": out["B43"].value,
            "equity": out["B50"].value,
            "per_share": out["B52"].value,
        },
    }


def extract_all(directory: Path = WORKBOOK_DIR) -> dict[str, Any]:
    return {
        "alphabet_2018": extract_alphabet(directory / "AlphabetApr2018.xlsx"),
        "nvidia_2023": extract_nvidia(directory / "NVIDIA2023.xlsx"),
    }


def main() -> int:
    data = extract_all()
    FIXTURE.write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(f"wrote {FIXTURE}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
