# Alphabet — source guide

Company-specific fetch and disclosure notes, migrated from the source-path catalog labelled verified 2026-09-07. Read alongside the [shared sourcing rules](../../docs/sources.md). Preserve source dates and recheck a hint when a fetch fails or disclosures change; quarter evidence belongs in the dated source cache and manifest.

**Alphabet (GOOGL, CIK 0001652044)**
- IR HTML pages block plain fetches (Cloudflare). Use the open Q4 Inc. JSON feeds instead:
  - Events (calls, transcripts): `https://abc.xyz/feed/Event.svc/GetEventList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=<YYYY>&excludeSelection=1&eventDateFilter=All`
    Each earnings event lists a transcript PDF attachment on `s206.q4cdn.com`, e.g. `.../doc_events/2026/Jul/22/2026_Q2_Earnings_Transcript.pdf`.
  - Financial reports (slides, release): `https://abc.xyz/feed/FinancialReport.svc/GetFinancialReportList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=<YYYY>&excludeSelection=1&reportSubType=`
    Slides pattern is roughly `.../doc_financials/<YYYY>/q<N>/<YYYY>q<N>-alphabet-earnings-slides.pdf` but casing varies, so read the feed.
- Fiscal year = calendar year.
