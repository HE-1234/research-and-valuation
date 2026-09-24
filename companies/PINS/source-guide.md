# Pinterest — source guide

Company-specific fetch and disclosure notes, migrated from the source-path catalog labelled verified 2026-09-07. Read alongside the [shared sourcing rules](../../docs/sources.md). Preserve source dates and recheck a hint when a fetch fails or disclosures change; quarter evidence belongs in the dated source cache and manifest.

**Pinterest (PINS, CIK 0001506293)**
- IR HTML is Cloudflare-blocked; the Q4 feeds are open with the standard UA ([shared feed pattern](../../docs/sources.md#section-12-3), host `investor.pinterestinc.com`). The FinancialReport feed lists press release, presentation, the company transcript PDF and the 10-Q per quarter on `s204.q4cdn.com/369458543/files/doc_earnings/<YYYY>/q<N>/`.
- Transcript: tier 1, with printed page numbers equal to PDF pages.
- KPI tables (regional MAU, ARPU) in the 10-K and 10-Q are chart images; use the press release. Each 10-K states regional revenue and ARPU in MD&A prose for its own year only, so five-year regional tables need every 10-K in the window. Slides scramble chart labels under `pdftotext -layout`; `pdftotext -bbox` plus a low-resolution `pdftoppm` render fixes the quarter mapping. Slides also insert spaces inside words ("non -GAAP"). Fiscal year = calendar year.
