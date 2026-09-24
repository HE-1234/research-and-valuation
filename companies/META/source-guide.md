# Meta Platforms — source guide

Company-specific fetch and disclosure notes, migrated from the source-path catalog labelled verified 2026-09-07. Read alongside the [shared sourcing rules](../../docs/sources.md). Preserve source dates and recheck a hint when a fetch fails or disclosures change; quarter evidence belongs in the dated source cache and manifest.

**Meta Platforms (META, CIK 0001326801)**
- IR HTML (`investor.atmeta.com`, `investor.fb.com`) returns 403. The Q4 feeds work ([shared feed pattern](../../docs/sources.md#section-12-3), host `investor.atmeta.com`). Documents on `https://s21.q4cdn.com/399680738/files/doc_financials/<YYYY>/q<N>/`: `META-Q<N>-<YYYY>-Earnings-Call-Transcript.pdf`, `META-Q<N>-<YYYY>-Follow-Up-Call-Transcript.pdf`, `Earnings-Presentation-Q<N>-<YYYY>.pdf`, and the release `Meta-<MM>-<DD>-<YYYY>-Exhibit-99-1-FINAL.pdf` (casing and suffix vary; read the feed).
- Transcript: tier 1. Meta publishes two company transcripts per quarter, the main call and a same-day CFO follow-up call; cache both (`transcript.txt`, `transcript-followup.txt`). Printed page numbers equal PDF pages. The company transcript footnotes corrections to spoken words; third-party transcripts show the uncorrected word.
- The CFO Outlook Commentary is printed inside the press release. KPI charts (regional DAP, impressions, price per ad) in the 10-Q and 10-K MD&A are images and do not survive text extraction; slides give nine quarters of series but chart pages extract data labels in scrambled order. Meta does not report gross margin. Fiscal year = calendar year.
