# Nebius Group — source guide

Company-specific fetch and disclosure notes, migrated from the source-path catalog labelled verified 2026-09-07. Read alongside the [shared sourcing rules](../../docs/sources.md). Preserve source dates and recheck a hint when a fetch fails or disclosures change; quarter evidence belongs in the dated source cache and manifest.

**Nebius Group (NBIS, CIK 0001513845)**
- Foreign private issuer: files 20-F (annual, the 10-K equivalent) and 6-K (quarterly); no 10-K, 10-Q, 8-K or proxy. Management, ownership and pay come from 20-F Items 6–7. The quarterly financial statements arrive in a separate 6-K from the press release (Q1 2026: release 05-13, financials 05-20; Q2 2026: both 08-12). 20-F primary documents are `nbis-<YYYYMMDD>x20f.htm` (older Yandex-era ones `yndx-…`; filer agent changed from 0001558370 to 0001104659).
- IR: `https://nebius.com/investor-hub`, `https://nebius.com/newsroom`, results PDFs on `assets.nebius.com`, all fetchable with a browser-like UA (`group.nebius.com` and `nebius.com/investor-relations` are 404). No slide deck; a two-column CEO letter replaces it and defers numeric guidance to the call, so the transcript gatherer is load-bearing for guidance. Cache a reading-order `pdftotext` copy alongside `-layout` for the letter.
- Transcript: tier 3 (Motley Fool), posted a week after the call. Q&A is IR reading portal questions aloud, so there are no analyst speaker labels.
- No gross profit is reported (cost of revenue excludes D&A); gross margin is a labelled computation. Formerly Yandex N.V. (renamed 2024-08-16); revenue history exists on a continuing basis only from FY2023. Fiscal year = calendar year.
