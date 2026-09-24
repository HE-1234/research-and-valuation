# Applied Optoelectronics — source guide

Company-specific fetch and disclosure notes, migrated from the source-path catalog labelled verified 2026-09-07. Read alongside the [shared sourcing rules](../../docs/sources.md). Preserve source dates and recheck a hint when a fetch fails or disclosures change; quarter evidence belongs in the dated source cache and manifest.

**Applied Optoelectronics (AAOI, CIK 0001158114)**
- IR site `investors.ao-inc.com` is fetchable with a browser-like UA but drops roughly one connection in three (retry once); the root URL times out, sub-pages work. Each quarter has only a press release, a webcast, and a "Trended Quarterly Financial Results" PDF (`/static-files/<uuid>`, linked from the event page). No slides, no transcript. The release has no cash-flow statement, so the 10-Q is the only cash-flow source. The company's supplemental PDFs contain arithmetic errors; take numbers from the release or 10-Q.
- Transcript: tier 3 (Motley Fool) when it exists; it carried Q1 2026 but not Q2 2026, so Q2 2026 ran at tier none with the Q1 call as a labelled supplement.
- FY2025 10-K contradicts itself on customer concentration (Item 1 vs Item 7) and swaps the CATV / Data Center labels in one Item 7 percentage table; use the notes to the financial statements. "Geographic" revenue is by manufacturing site, not customer location. Fiscal year = calendar year.
