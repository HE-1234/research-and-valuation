# Reddit — source guide

Company-specific fetch and disclosure notes, migrated from the source-path catalog labelled verified 2026-09-07. Read alongside the [shared sourcing rules](../../docs/sources.md). Preserve source dates and recheck a hint when a fetch fails or disclosures change; quarter evidence belongs in the dated source cache and manifest.

**Reddit (RDDT, CIK 0001713445)**
- Q4 Inc. feeds on `investor.redditinc.com` are open with the standard UA ([shared feed pattern](../../docs/sources.md#section-12-3)); documents on `s203.q4cdn.com/380862485/files/doc_financials/<YYYY>/q<N>/` (transcript filename hyphenation varies by quarter). Tier 1 transcript with Q&A, no printed page numbers (PDF-page tags). No slides exist; the shareholder letter is the deck, and its charts need `pdftotext -bbox` to fix quarter order. The 8-K's Exhibit 99.2 letter copy is image-only; use the CDN PDF. IR release HTML pages return 403; use the 8-K Exhibit 99.1.
- KPI tables in the 10-K and 10-Q are chart images; absolute series come from letters and releases. Reddit stops reporting logged-in vs logged-out DAUq from Q3 2026. No FY2021 data exists in any filing (the IPO prospectus has two audited years). IPO-era filings carry agent prefix 0001628280. Fiscal year = calendar year.
