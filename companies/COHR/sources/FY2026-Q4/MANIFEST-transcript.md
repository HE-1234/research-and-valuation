# MANIFEST-transcript.md — Coherent Corp. (COHR), Q4 FY2026

| Field | Value |
|---|---|
| Company | Coherent Corp., NYSE: COHR |
| CIK | 0000820318 (EDGAR paths use `820318`) |
| Quarter | Q4 FY2026 (quarter and fiscal year ended June 30, 2026); folder `FY2026-Q4` |
| Call date and time | Wednesday, August 12, 2026, 4:30 p.m. ET (as printed on the transcript page; the IR host says "All our statements are made as of today, August 12, 2026"). The earnings 8-K was accepted by EDGAR at 16:10:13 ET the same day, so the call followed the after-close release. |
| As-of cutoff | 2026-08-14 (10-K FY2026 filing date) |
| Fetch date | 2026-09-09 (UTC) |
| Transcript source tier | 3, third-party free (The Motley Fool) |
| Gatherer | transcript gatherer (AGENTS.md §13) |

## Files

| File | Origin URL | Fetch date | Source tier | Word count |
|---|---|---|---|---|
| `transcript.txt` | https://www.fool.com/earnings/call-transcripts/2026/08/19/coherent-cohr-q4-2026-earnings-call-transcript/ | 2026-09-09 | 3 (Motley Fool machine transcript) | 9,663 total; 9,383 in the call text (54 turns), remainder is the provenance header and section headings |
| `notes-transcript.md` | derived from `transcript.txt` | 2026-09-09 | n/a | 6,558 |
| `MANIFEST-transcript.md` | this file | 2026-09-09 | n/a | n/a |

No `transcript-FY2026-Q3.txt` was cached: a Q4 FY2026 transcript exists, so the tier-none fallback was not needed.

## Tier checks, in order

### Tier 1 — company-published (IR site `ir.coherent.com`, Q4 Inc. on an Akamai edge): CLOSED, nothing found

| URL | UA | Run | HTTP status per attempt | Bytes | Found |
|---|---|---|---|---|---|
| `https://ir.coherent.com/feed/Event.svc/GetEventList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1&eventDateFilter=All` | browser-like (Mozilla/5.0 ... Chrome/124.0) | HTTP/2 | 403, 403, 403, 403 | 413 bytes | Akamai "Access Denied" page (`errors.edgesuite.net` reference) on every attempt, full 10/30/120 s backoff |
| `https://ir.coherent.com/feed/PressRelease.svc/GetPressReleaseList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1` | browser-like (Mozilla/5.0 ... Chrome/124.0) | HTTP/2 | 403, 403, 403, 403 | 427 bytes | Akamai "Access Denied" page (`errors.edgesuite.net` reference) on every attempt, full 10/30/120 s backoff |
| `https://ir.coherent.com/feed/FinancialReport.svc/GetFinancialReportList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1&reportSubType=` | browser-like (Mozilla/5.0 ... Chrome/124.0) | HTTP/2 | 403, 403, 403, 403 | 433 bytes | Akamai "Access Denied" page (`errors.edgesuite.net` reference) on every attempt, full 10/30/120 s backoff |
| `https://www.coherent.com/company/investor-relations/investor-presentations` | browser-like (Mozilla/5.0 ... Chrome/124.0) | `-L` follow | 403, 403, 403, 403 | 382 bytes | Akamai "Access Denied" page (`errors.edgesuite.net` reference) on every attempt, full 10/30/120 s backoff |
| `https://ir.coherent.com/feed/PressRelease.svc/GetPressReleaseList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1` | `company-research-skill owner@example.com` | HTTP/2 | 000 | 0 bytes | connection reset before any response (curl 000), no body |
| `https://www.coherent.com/company/investor-relations/financial-webcasts` | browser-like (Mozilla/5.0 ... Chrome/124.0) | `-L` follow | 403, 403, 403, 403 | 395 bytes | Akamai "Access Denied" page (`errors.edgesuite.net` reference) on every attempt, full 10/30/120 s backoff |
| `https://ir.coherent.com/feed/FinancialReport.svc/GetFinancialReportList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1&reportSubType=` | `company-research-skill owner@example.com` | HTTP/2 | 403, 403, 000 | 433 bytes | Akamai "Access Denied" (`errors.edgesuite.net`) on the 403 attempts; the edge then dropped the connection (curl 000) on retry |
| `https://ir.coherent.com/feed/Event.svc/GetEventList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1&eventDateFilter=All` | `company-research-skill owner@example.com` | HTTP/2 | 403, 000 | 413 bytes | Akamai "Access Denied" (`errors.edgesuite.net`) on the 403 attempts; the edge then dropped the connection (curl 000) on retry |
| `https://ir.coherent.com/feed/FinancialReport.svc/GetFinancialReportList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1&reportSubType=` | `company-research-skill owner@example.com` | HTTP/1.1 retry | 403, 000 | 433 bytes | Akamai "Access Denied" (`errors.edgesuite.net`) on the 403 attempts; the edge then dropped the connection (curl 000) on retry |
| `https://ir.coherent.com/feed/Event.svc/GetEventList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1&eventDateFilter=All` | `company-research-skill owner@example.com` | HTTP/1.1 retry | 403, 000 | 413 bytes | Akamai "Access Denied" (`errors.edgesuite.net`) on the 403 attempts; the edge then dropped the connection (curl 000) on retry |
| `https://ir.coherent.com/feed/PressRelease.svc/GetPressReleaseList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1` | `company-research-skill owner@example.com` | HTTP/1.1 retry | 000 | 0 bytes | connection reset before any response (curl 000), no body |

Notes: the two `www.coherent.com/company/investor-relations/...` URLs were fetched with `-L`; both redirect to `https://ir.coherent.com/news-events/events`, which returns the same Akamai 403. Backoff of 10 s / 30 s / 120 s was applied after each 403 (four attempts, about 160 s per URL) wherever the edge kept answering; on the standard-UA runs the edge answered 403 once and then reset the connection on the retry, over both HTTP/2 and HTTP/1.1, and the `PressRelease.svc` feed reset immediately with no body. The fetch helper stops on a connection error, so those runs have fewer than four attempts. No q4cdn.com document path could be discovered. Not attempted: `investors.coherent.com` (the orchestrator reports it 301s to the corporate homepage, not the IR site) and `https://ir.coherent.com/` itself (the orchestrator reports 403).

### Tier 2 — 8-K exhibit: CLOSED, no transcript or prepared-remarks exhibit

| URL | UA | HTTP status | Bytes | Found |
|---|---|---|---|---|
| `https://www.sec.gov/Archives/edgar/data/820318/000119312526346860/0001193125-26-346860-index.htm` | `company-research-skill owner@example.com` | 200 | 15919 bytes | Accession 0001193125-26-346860, filed 2026-08-12, accepted 2026-08-12 16:10:13, period 2026-08-12. Exhibits: `d128030d8k.htm` (8-K body), EX-99.1 `d128030dex991.htm` (press release, 356,427 bytes), EX-99.2 `d128030dex992.htm` (investor presentation, 102,281 bytes), 17 GRAPHIC .jpg files (presentation slide images), XBRL files. No EX-99.3, no prepared remarks, no transcript. |

The release and presentation were not cached here (the ir gatherer owns them). Only one SEC request was made.

### Tier 3 — third-party free (The Motley Fool): USED

| URL | UA | HTTP status | Bytes | Found |
|---|---|---|---|---|
| `https://www.fool.com/robots.txt` | browser-like | 200 | 2311 bytes | `urllib.robotparser`: `can_fetch("*", quote page)`, `can_fetch("*", /earnings/call-transcripts/...)` and `can_fetch("*", /sitemap/2026/08)` all True. The two `Disallow: /` blocks apply to named bots (MauiBot, Bytespider), not `*`. |
| `https://www.fool.com/quote/nyse/cohr/` | browser-like | 200 | 647000 bytes | Embedded JSON lists eight COHR transcript slugs, including `/earnings/call-transcripts/2026/08/19/coherent-cohr-q4-2026-earnings-call-transcript/` (Q4 FY2026) and `/earnings/call-transcripts/2026/05/06/coherent-cohr-q3-2026-earnings-transcript/` (Q3 FY2026, the fallback that was not needed). |
| `https://www.fool.com/earnings/call-transcripts/2026/08/19/coherent-cohr-q4-2026-earnings-call-transcript/` | browser-like | 200 | 528875 bytes | Article "Coherent (COHR) Q4 2026 Earnings Call Transcript"; `article:published_time` 2026-08-19T23:11:19Z, `article:modified_time` 2026-08-19T23:11:19Z; DATE section "Wednesday, Aug. 12, 2026 at 4:30 p.m. ET"; operator opens "welcome to the Coherent Fourth Quarter and Fiscal Year 26 Earnings Call"; IR host dates the statements "today, August 12, 2026". Confirmed to be the Q4 FY2026 call. |

The monthly sitemaps (`/sitemap/2026/08`, `/sitemap/2026/09`) were not fetched because the quote page already yielded the link. No other fool.com page (sidebar, related articles, "Read Next") was opened or read.

### Tier 4 — owner-supplied: none given.

### Tier 5 — none: not reached.

## As-of discipline

- Call date: 2026-08-12 (4:30 p.m. ET), before the 2026-08-14 cutoff.
- Posting date: 2026-08-19T23:11:19Z (published = modified), five days after the cutoff. Admissible under AGENTS.md §12.2 (transcript of a pre-cutoff call, posted later); only call content is used. The provenance header in `transcript.txt` records both dates.
- No document dated after 2026-08-14 other than the transcript page itself was opened. No conference-appearance transcripts, no later filings, no Fool sidebar or editorial blocks were read. The cached text contains no editorial content from Fool.
- The 8-K index page (filed 2026-08-12) was read only to list exhibits; the exhibits themselves were not opened by this gatherer.

## Processing notes

- Kept from the article body (`<div id="article-body-transcript">`): the DATE section, the CALL PARTICIPANTS list, and the "Full Conference Call Transcript" section. Dropped: Fool's TAKEAWAYS, RISKS, SUMMARY and INDUSTRY GLOSSARY sections, the "Image source" caption, the `article-body-promobox` block, everything from "Read Next" onward, and all sidebar/related-article content. A residue grep for "Stock Advisor", "Motley Fool", "foolcdn", "Image source", "TAKEAWAYS", "GLOSSARY" finds nothing outside the provenance header.
- Speaker-label format: the speaker name from Fool's `<strong>Name:</strong>` appears on its own line ending in a colon, followed by that turn's paragraphs (one paragraph per line), with a blank line between turns. Names are exactly as Fool printed them, including the garbled analyst labels "Joe" (Samik Chatterjee), "Given Arya" (Vivek Arya) and "Michael" (Michael Mani); the notes file lists these and the mislabelled "Operator" turns.
- Header: three provenance lines (SOURCE / CALL / POSTED) precede the kept sections.
- Coverage check: 54 turns; first turn is the operator's "Greetings, and welcome to the Coherent Fourth Quarter and Fiscal Year 26 Earnings Call"; last turn is the operator's "This concludes today's teleconference. You may disconnect your lines at this time." Prepared remarks (Silverstein, Anderson, Luther), nine analyst exchanges with follow-ups, CEO closing remarks. Turn counts: Operator 14, Silverstein 1, Anderson 18, Luther 4, analysts 17.
- Numbers: two guidance items are garbled in the transcript (gross margin range "39.541.5%", tax rate "1.82 thousand%"). Per AGENTS.md §3 rule 2, all numbers are to be taken from the press release and presentation; the transcript is quoted for wording only. Suspected transcription errors are listed in `notes-transcript.md` §0 and were not corrected in the cache.
- Cached extracted text only; the HTML source stays in scratch (`/tmp/cohr-orch/transcript/t3_article.html`). No PDF was involved (HTML article, no page numbers).
- SEC etiquette: one request, UA `company-research-skill owner@example.com`. No 403/429 from SEC. IR-site 403s were retried with the 10/30/120 s backoff as recorded below.

## Fetch log (UTC; one line per attempt)

| Time | URL | Status | Bytes | Attempt | Label | UA (prefix) |
|---|---|---|---|---|---|---|
| 2026-09-09T00:17:01Z | `https://ir.coherent.com/feed/Event.svc/GetEventList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1&eventDateFilter=All` | HTTP 403 | 413 bytes | attempt 1 | T1 event feed (browser UA) | Mozilla/5.0 (X11; Linux x86_64 |
| 2026-09-09T00:17:12Z | `https://ir.coherent.com/feed/Event.svc/GetEventList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1&eventDateFilter=All` | HTTP 403 | 413 bytes | attempt 2 | T1 event feed (browser UA) | Mozilla/5.0 (X11; Linux x86_64 |
| 2026-09-09T00:17:42Z | `https://ir.coherent.com/feed/Event.svc/GetEventList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1&eventDateFilter=All` | HTTP 403 | 413 bytes | attempt 3 | T1 event feed (browser UA) | Mozilla/5.0 (X11; Linux x86_64 |
| 2026-09-09T00:19:42Z | `https://ir.coherent.com/feed/Event.svc/GetEventList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1&eventDateFilter=All` | HTTP 403 | 413 bytes | attempt 4 | T1 event feed (browser UA) | Mozilla/5.0 (X11; Linux x86_64 |
| 2026-09-09T00:20:06Z | `https://www.sec.gov/Archives/edgar/data/820318/000119312526346860/0001193125-26-346860-index.htm` | HTTP 200 | 15919 bytes | attempt 1 | T2 SEC 8-K accession index | company-research-skill owner@e |
| 2026-09-09T00:20:06Z | `https://www.fool.com/robots.txt` | HTTP 200 | 2311 bytes | attempt 1 | T3 fool robots.txt | Mozilla/5.0 (X11; Linux x86_64 |
| 2026-09-09T00:20:06Z | `https://ir.coherent.com/feed/PressRelease.svc/GetPressReleaseList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1` | HTTP 403 | 427 bytes | attempt 1 | T1 pressrel feed (browser UA) | Mozilla/5.0 (X11; Linux x86_64 |
| 2026-09-09T00:20:06Z | `https://ir.coherent.com/feed/FinancialReport.svc/GetFinancialReportList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1&reportSubType=` | HTTP 403 | 433 bytes | attempt 1 | T1 finrep feed (browser UA) | Mozilla/5.0 (X11; Linux x86_64 |
| 2026-09-09T00:20:06Z | `https://www.coherent.com/company/investor-relations/investor-presentations` | HTTP 403 | 382 bytes | attempt 1 | T1 www investor-presentations -L (browser UA) | Mozilla/5.0 (X11; Linux x86_64 |
| 2026-09-09T00:20:06Z | `https://ir.coherent.com/feed/PressRelease.svc/GetPressReleaseList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1` | HTTP 000 | 0 bytes | attempt 1 | T1 pressrel feed (standard UA) | company-research-skill owner@e |
| 2026-09-09T00:20:06Z | `https://www.coherent.com/company/investor-relations/financial-webcasts` | HTTP 403 | 395 bytes | attempt 1 | T1 www financial-webcasts -L (browser UA) | Mozilla/5.0 (X11; Linux x86_64 |
| 2026-09-09T00:20:06Z | `https://ir.coherent.com/feed/FinancialReport.svc/GetFinancialReportList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1&reportSubType=` | HTTP 403 | 433 bytes | attempt 1 | T1 finrep feed (standard UA) | company-research-skill owner@e |
| 2026-09-09T00:20:06Z | `https://ir.coherent.com/feed/Event.svc/GetEventList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1&eventDateFilter=All` | HTTP 403 | 413 bytes | attempt 1 | T1 event feed (standard UA) | company-research-skill owner@e |
| 2026-09-09T00:20:07Z | `https://www.fool.com/quote/nyse/cohr/` | HTTP 200 | 647000 bytes | attempt 1 | T3 fool quote page | Mozilla/5.0 (X11; Linux x86_64 |
| 2026-09-09T00:20:16Z | `https://ir.coherent.com/feed/FinancialReport.svc/GetFinancialReportList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1&reportSubType=` | HTTP 403 | 433 bytes | attempt 2 | T1 finrep feed (browser UA) | Mozilla/5.0 (X11; Linux x86_64 |
| 2026-09-09T00:20:16Z | `https://ir.coherent.com/feed/PressRelease.svc/GetPressReleaseList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1` | HTTP 403 | 427 bytes | attempt 2 | T1 pressrel feed (browser UA) | Mozilla/5.0 (X11; Linux x86_64 |
| 2026-09-09T00:20:16Z | `https://www.coherent.com/company/investor-relations/investor-presentations` | HTTP 403 | 382 bytes | attempt 2 | T1 www investor-presentations -L (browser UA) | Mozilla/5.0 (X11; Linux x86_64 |
| 2026-09-09T00:20:16Z | `https://www.coherent.com/company/investor-relations/financial-webcasts` | HTTP 403 | 395 bytes | attempt 2 | T1 www financial-webcasts -L (browser UA) | Mozilla/5.0 (X11; Linux x86_64 |
| 2026-09-09T00:20:16Z | `https://ir.coherent.com/feed/Event.svc/GetEventList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1&eventDateFilter=All` | HTTP 000 | 413 bytes | attempt 2 | T1 event feed (standard UA) | company-research-skill owner@e |
| 2026-09-09T00:20:17Z | `https://ir.coherent.com/feed/FinancialReport.svc/GetFinancialReportList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1&reportSubType=` | HTTP 403 | 433 bytes | attempt 2 | T1 finrep feed (standard UA) | company-research-skill owner@e |
| 2026-09-09T00:20:46Z | `https://ir.coherent.com/feed/FinancialReport.svc/GetFinancialReportList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1&reportSubType=` | HTTP 403 | 433 bytes | attempt 3 | T1 finrep feed (browser UA) | Mozilla/5.0 (X11; Linux x86_64 |
| 2026-09-09T00:20:46Z | `https://ir.coherent.com/feed/PressRelease.svc/GetPressReleaseList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1` | HTTP 403 | 427 bytes | attempt 3 | T1 pressrel feed (browser UA) | Mozilla/5.0 (X11; Linux x86_64 |
| 2026-09-09T00:20:47Z | `https://www.coherent.com/company/investor-relations/financial-webcasts` | HTTP 403 | 395 bytes | attempt 3 | T1 www financial-webcasts -L (browser UA) | Mozilla/5.0 (X11; Linux x86_64 |
| 2026-09-09T00:20:47Z | `https://www.coherent.com/company/investor-relations/investor-presentations` | HTTP 403 | 382 bytes | attempt 3 | T1 www investor-presentations -L (browser UA) | Mozilla/5.0 (X11; Linux x86_64 |
| 2026-09-09T00:20:47Z | `https://ir.coherent.com/feed/FinancialReport.svc/GetFinancialReportList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1&reportSubType=` | HTTP 000 | 433 bytes | attempt 3 | T1 finrep feed (standard UA) | company-research-skill owner@e |
| 2026-09-09T00:22:47Z | `https://ir.coherent.com/feed/PressRelease.svc/GetPressReleaseList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1` | HTTP 403 | 427 bytes | attempt 4 | T1 pressrel feed (browser UA) | Mozilla/5.0 (X11; Linux x86_64 |
| 2026-09-09T00:22:47Z | `https://ir.coherent.com/feed/FinancialReport.svc/GetFinancialReportList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1&reportSubType=` | HTTP 403 | 433 bytes | attempt 4 | T1 finrep feed (browser UA) | Mozilla/5.0 (X11; Linux x86_64 |
| 2026-09-09T00:22:47Z | `https://www.coherent.com/company/investor-relations/financial-webcasts` | HTTP 403 | 395 bytes | attempt 4 | T1 www financial-webcasts -L (browser UA) | Mozilla/5.0 (X11; Linux x86_64 |
| 2026-09-09T00:22:47Z | `https://www.coherent.com/company/investor-relations/investor-presentations` | HTTP 403 | 382 bytes | attempt 4 | T1 www investor-presentations -L (browser UA) | Mozilla/5.0 (X11; Linux x86_64 |
| 2026-09-09T00:31:14Z | `https://ir.coherent.com/feed/FinancialReport.svc/GetFinancialReportList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1&reportSubType=` | HTTP 403 | 433 bytes | attempt 1 | T1 finrep feed (standard UA, http1.1 retry) | company-research-skill owner@e |
| 2026-09-09T00:31:14Z | `https://ir.coherent.com/feed/Event.svc/GetEventList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1&eventDateFilter=All` | HTTP 403 | 413 bytes | attempt 1 | T1 event feed (standard UA, http1.1 retry) | company-research-skill owner@e |
| 2026-09-09T00:31:14Z | `https://www.fool.com/earnings/call-transcripts/2026/08/19/coherent-cohr-q4-2026-earnings-call-transcript/` | HTTP 200 | 528875 bytes | attempt 1 | T3 fool Q4 FY2026 transcript article | Mozilla/5.0 (X11; Linux x86_64 |
| 2026-09-09T00:32:13Z | `https://ir.coherent.com/feed/PressRelease.svc/GetPressReleaseList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1` | HTTP 000 | 0 bytes | attempt 1 | T1 pressrel feed (standard UA, http1.1 retry) | company-research-skill owner@e |
| 2026-09-09T00:32:24Z | `https://ir.coherent.com/feed/FinancialReport.svc/GetFinancialReportList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1&reportSubType=` | HTTP 000 | 433 bytes | attempt 2 | T1 finrep feed (standard UA, http1.1 retry) | company-research-skill owner@e |
| 2026-09-09T00:32:24Z | `https://ir.coherent.com/feed/Event.svc/GetEventList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1&eventDateFilter=All` | HTTP 000 | 413 bytes | attempt 2 | T1 event feed (standard UA, http1.1 retry) | company-research-skill owner@e |

Scratch directory: `/tmp/cohr-orch/transcript/` (fetch.sh, fetch.log, extract.py, manifest.py, raw HTML/JSON responses). Nothing was written outside `companies/COHR/sources/FY2026-Q4/`; no git commands were run.
