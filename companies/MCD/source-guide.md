# McDonald's — source guide

Company-specific fetch and disclosure notes, migrated from the source-path catalog labelled verified 2026-09-07. Read alongside the [shared sourcing rules](../../docs/sources.md). Preserve source dates and recheck a hint when a fetch fails or disclosures change; quarter evidence belongs in the dated source cache and manifest.

**McDonald's (MCD, CIK 0000063908)**
- Every path on `corporate.mcdonalds.com` and `www.mcdonalds.com` fails from this host (HTTP/2 INTERNAL_ERROR from the Akamai edge; `--http1.1` times out). Not a Q4 Inc. host, so no feed fallback; tier 1 is effectively unreachable. No slides exist. Both earnings 8-Ks carry EX-99.1 (short release) and EX-99.2 ("Supplemental Information", ~21 pages): comps, systemwide sales, restaurant margins, restaurant counts, and a written Outlook page with the full-year targets. Neither has a cash-flow statement, balance sheet or capex actuals; the 10-Q is the only quarterly cash-flow source.
- Exhibit names are inconsistent (`exhibit991-<MMDDYYYY>.htm`, `exhibit991-33126xq1.htm`); read the accession `-index.htm`. DEF 14A is filed under agent prefix 0001193125. 10-Ks are in annual-report format with no "Item N" headings in the body; tag by section name. Whole-million rounding adopted in Q1 2024 causes $1M differences between 10-Ks.
- Transcript: tier 3 (Motley Fool), posted a week after the call. Fiscal year = calendar year.
