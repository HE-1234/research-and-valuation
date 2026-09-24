# Broadcom — source guide

Company-specific fetch and disclosure notes, migrated from the source-path catalog labelled verified 2026-09-07. Read alongside the [shared sourcing rules](../../docs/sources.md). Preserve source dates and recheck a hint when a fetch fails or disclosures change; quarter evidence belongs in the dated source cache and manifest.

**Broadcom (AVGO, CIK 0001730168)**
- `investors.broadcom.com` (every path, including the Q4 `/feed/*.svc` URLs) returns 403 from the Akamai edge even with a browser UA; `www.broadcom.com/company/news` is JS-rendered and empty. Press release only via 8-K Exhibit 99.1 (`avgo-<MMDDYYYY>x8kxex99.htm`). No earnings slides exist.
- Transcript: tier 3 (Motley Fool) only.
- Guidance is given as single "approximately" points, never ranges; claims must be single-direction or labelled sharpenings. The release carries five columns (current, prior quarter, year-ago, two half-years), so most last-quarter comparisons come from it. Filings use curly apostrophes, which defeat ASCII greps. The FY2023 10-K is pre-split (10-for-1 in 2024) and the FY2025 10-K restates; the split itself is not stated in any fetched filing.
- Fiscal year ends the Sunday closest to October 31, named for the calendar year in which it ends; FY2026 ≈ Nov 2025 – Oct 2026.
