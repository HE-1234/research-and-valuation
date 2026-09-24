# Micron — source guide

Company-specific fetch and disclosure notes, migrated from the source-path catalog labelled verified 2026-09-07. Read alongside the [shared sourcing rules](../../docs/sources.md). Preserve source dates and recheck a hint when a fetch fails or disclosures change; quarter evidence belongs in the dated source cache and manifest.

**Micron (MU, CIK 0000723125)**
- `investors.micron.com` HTML returns 403; the Q4 feeds work with a browser-like UA ([shared feed pattern](../../docs/sources.md#section-12-3)). PDFs on `s25.q4cdn.com/621799436/files/doc_financials/<YYYY>/q<N>/`, e.g. `Q<N>-FY<YY>-Prepared-Remarks.pdf` and the deck. The `PressRelease.svc` feed returns empty; use the 8-K Exhibit 99.1 for the release.
- Transcript: tier 1 prepared remarks only (CEO and CFO script, no Q&A, no printed page numbers). Motley Fool did not carry Q3 FY2026, so Q&A was unavailable at every tier; expect this to recur.
- Remarks and deck are non-GAAP by default; GAAP guidance appears only in the release's Business Outlook table. Business units were reorganized in FY2025 (Cloud Memory, Core Data Center, Mobile and Client, Automotive and Embedded); the FY2025 10-K recasts FY2023–FY2025 only, so DRAM / NAND revenue is the only consistent five-year series.
- Fiscal year ends the Thursday closest to August 31; FY2026 is a 53-week year with a 14-week Q4. Q4 is reported in late September with the 10-K in early October.
