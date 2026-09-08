# MANIFEST-transcript.md — Duolingo, Inc. (DUOL), Q2 2026 (call 2026-08-05)

**Transcript source tier: 3 (third-party free, The Motley Fool).** Duolingo publishes no transcript (tier 1 unreachable; see log) and the earnings 8-K carries no transcript or prepared-remarks exhibit (tier 2 absent).

| file | origin URL | fetch date | source tier | word count |
|---|---|---|---|---|
| `transcript.txt` | https://www.fool.com/earnings/call-transcripts/2026/08/12/duolingo-duol-q2-2026-earnings-call-transcript/ | 2026-09-08 (cached by the earlier interrupted run; verified and reused 2026-09-08, not refetched; a trailing newline was appended) | 3, Motley Fool machine transcript | 7,726 (whole file incl. 7-line header; 116 lines) |
| `notes-transcript.md` | derived from `transcript.txt`, cross-checked against `shareholder-letter.txt`, `press-release.txt`, `shareholder-letter-2026-Q1.txt`, `10-Q-2026-Q2.txt` | 2026-09-08 | — | 7,571 |
| `MANIFEST-transcript.md` | this file | 2026-09-08 | — | — |

## Header facts

- Call: Wednesday 2026-08-05, 5:00 pm ET ("Second Quarter Earnings Webcast"). Company format: a shareholder letter is published the same afternoon; the call has a short scripted section (CEO, CFO) and a long Q&A (ten analysts, nineteen question turns). Pre-cutoff (as-of cutoff 2026-08-06; 10-Q filed 2026-08-06).
- Fool page posted 2026-08-12T23:41:49Z, after the cutoff. Admissible under AGENTS.md §12.2: only call content is used, and both dates are recorded here and in the file header.
- Printed page numbers: none (web page, not a PDF). Tag as `[Q2 2026 call]` without page numbers. `notes-transcript.md` gives `transcript.txt` line numbers (one paragraph per line) so the reviewer can locate each quote; those line numbers are not to appear in report prose.
- Machine transcript: numbers may be garbled. Report numbers come from the letter/release; the transcript supplies wording (AGENTS.md §3 rule 2, §12.2 tier 3).

## Tier search log (all requests 2026-09-08 UTC; >= 2.5 s between requests to the same host)

**Tier 1 — company-published (investors.duolingo.com, Q4 Inc.-hosted).** Result: unreachable; every path returns HTTP 403 from an Akamai edge ("Access Denied", reference to errors.edgesuite.net, header `x-reference-error`), the same pattern AGENTS.md §12.3 records for Broadcom. Browser UA used: `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36`.

| # | URL | headers | HTTP |
|---|---|---|---|
| 1 | `https://investors.duolingo.com/feed/FinancialReport.svc/GetFinancialReportList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1&reportSubType=` | browser UA | 403 (440 B) |
| 2 | `https://investors.duolingo.com/feed/Event.svc/GetEventList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1&eventDateFilter=All` | browser UA | 403 (420 B) |
| 3 | URL 1 | browser UA + `Accept: application/json` + `Referer: https://investors.duolingo.com/` | 403 |
| 4 | URL 2 | browser UA + `Accept: application/json` + `Referer: https://investors.duolingo.com/` | 403 |
| 5 | `https://investors.duolingo.com/events-and-presentations/default.aspx` | browser UA | 403 |
| 6 | `https://investors.duolingo.com/financials/quarterly-results/default.aspx` | browser UA | 403 |
| 7 | `https://investors.duolingo.com/events-and-presentations/events/default.aspx` | browser UA | 403 |
| 8 | `https://investors.duolingo.com/` | browser UA (GET, then HEAD) | 403 |
| 9-10 | URLs 2 and 1 | browser UA + Accept/Referer, after 10 s back-off | 403 / 403 |
| 11-12 | URLs 2 and 1 | browser UA + Accept/Referer, after 30 s back-off | 403 / 403 |
| 13-14 | URLs 2 and 1 | browser UA + Accept/Referer, after 120 s back-off | 403 / 403 |

The orchestrator's earlier probe of URLs 1 and 2 with the SEC UA (`company-research-skill owner@example.com`) also returned 403. Fourteen 403s across three UA/header combinations and the full 10/30/120 s back-off ladder settle tier 1 as unreachable from this host. Consequences: no company transcript could be looked for, and no `s<NNN>.q4cdn.com` document path (including the shareholder-letter PDF) was observed; the shareholder letter in this folder comes from the 8-K exhibit route.

**Tier 2 — 8-K exhibit.** `https://www.sec.gov/Archives/edgar/data/1562088/000162828026053299/0001628280-26-053299-index.htm` (SEC UA `company-research-skill owner@example.com`): HTTP 200. Exhibits: primary document `duol-20260805.htm` (8-K, iXBRL); EX-99.1 `q2fy26duolingo6-30x26xpres.htm` (press release); EX-99.2 `q2fy26duolingo6-30x26share.htm` (shareholder letter); EX-101.SCH / LAB / PRE (XBRL). No transcript or prepared-remarks exhibit. Tier 2 absent. (The two 99.x exhibits are the IR gatherer's files; not fetched here.)

**Tier 3 — Motley Fool.** `transcript.txt` was already cached by the earlier interrupted run from the URL in the table above. Verified this run and reused without refetching:
- `https://www.fool.com/robots.txt`: HTTP 200. The `User-agent: *` block has no Disallow covering `/earnings/` or `/earnings/call-transcripts/`; the path is permitted for `*`.
- Structure check of the cached file: 7-line provenance header (tier, URL, call date/time, posting timestamp, fetch date, dropped blocks, quote normalisation); `## DATE` (l.9-10); `## CALL PARTICIPANTS` listing Deborah Belevan (IR), Luis von Ahn Arellano (Co-Founder and CEO), Gillian Munson (CFO) (l.12-16); `## Full Conference Call Transcript` (l.18) with the IR host's opening and safe-harbour statement (l.20-21), CEO remarks (l.22-23), CFO remarks incl. guidance (l.24-28), operator-introduced Q&A with ten analysts in order: Wyatt Swanson (D.A. Davidson), Andrew Boone (Citizens), Nathan Feather (firm not stated), Bryan Smilek (JPMorgan), Ryan MacDonald (Needham), Shweta Khajuria (Wolfe Research), Mark Mahaney (Evercore), Ygal Arounian (Wedbush), Justin Patterson (KeyBanc), Arvind Ramnani (Truist) (l.29-114), operator close "I'm showing no further questions. This concludes the Q&A section of the call." (l.115) and the CEO's sign-off (l.116). No truncation: the final line is a complete closing sentence. 7,726 words (7,700 expected).
- Cleanups already applied by the earlier run and recorded in the header: kept DATE / CALL PARTICIPANTS / Full Conference Call Transcript only; dropped Fool's TAKEAWAYS, RISKS, SUMMARY, INDUSTRY GLOSSARY and footer blocks; curly quotes normalised to straight. Cleanup applied this run: appended the missing trailing newline (no other byte changed; line numbering unaffected).
- Known transcript defects, left as-is (do not silently "fix" the source): CFO's name spelled "Gilian"; FY Adjusted EBITDA margin spoken/transcribed as "roughly 25.5%" at l.26 (26.5% at l.25 and in the letter); "existing user subscribers" at l.46 for "existing Super subscribers"; "make the minimum session length longer" at l.70 where context says shorter; a bracketed "[ as reactive ]" transcriber guess at l.105.

## Cross-check summary against the shareholder letter and release

- Every Q3 2026 guidance number spoken (bookings ~$307M / 9%, revenue $302M / 11%, gross margin 71%, Adjusted EBITDA ~$76M / 25.2%) matches the letter's table (8.9%, 11.1% before rounding).
- Full-year: bookings ~11% and revenue ~16% match the letter's 10.9% / 16.3%; the 10-12% / 15-18% ranges match; Adjusted EBITDA ~$320M matches; the margin is 26.5% in the letter and at l.25 but "roughly 25.5%" at l.26 (one discrepancy; letter governs).
- Call-only guidance not in the letter or release: FY free cash flow "over $375 million"; Q4-exit gross margin "closer to 70%" (letter gives Q3 71.0% and FY 71.6% only; our arithmetic on the letter's figures implies about 70% for Q4, so the statements are consistent); about 0.5 point of FX headwind in FY bookings growth since the May call; the Q4-DAU bonus plan (trigger 25% DAU growth, ~$10M cash, excluded from guidance; also absent from the 10-Q).
- Letter-only guidance not spoken: SBC ~15% of revenue, dilution 3.5-4.0%, tax rate 23-25%, the H2 "above 20%" DAU growth expectation (quoted by an analyst, not restated by management), the $4M-per-1%-FX sensitivity.
- Reported figures spoken (DAU +23%, $1.3B cash and investments, FCF ~$79M vs $78.6M, buyback ~$44M in Q2 and $72M / ~700,000 shares cumulative vs the letter's $71.9M / 708 thousand through 2026-08-01, >15M streak revivals vs 15.4M, CURR up ~1 point, >1B social impressions per quarter, two-thirds of impressions from influencers in China/Indonesia/India) all match the letter within rounding.
- Full detail, including every call-only number (Video Call cost $0.30 to under $0.01; ~350 changes per weekly release; China second-largest DAU market, monetising like France; Math and Music at single-digit millions of DAUs; AI cost in COGS "tens of millions", internal AI ~"$10 million"; open-source models 3-6 months behind frontier; Super Lite at about half Super's price), is in `notes-transcript.md` §2 and §6.

## As-of statement

Everything in `transcript.txt` and `notes-transcript.md` is content of the 2026-08-05 call, which precedes the 2026-08-06 cutoff. The only post-cutoff artefact is the Fool page's posting date (2026-08-12), recorded above; no Fool editorial content (posted 2026-08-12) was kept. No other post-cutoff source was fetched or read. The letter and release used for cross-checking are the 2026-08-05 8-K exhibits already in this folder.

## Fetch lessons for AGENTS.md §12.3 (Duolingo entry)

- `investors.duolingo.com` is Q4 Inc.-hosted behind Akamai and returns 403 on every path tried, including both `/feed/*.svc` JSON feeds, with SEC-style and browser UAs, with and without `Accept: application/json` / `Referer`, and after 10/30/120 s back-off. Treat like Broadcom: press release and shareholder letter via 8-K exhibits 99.1 / 99.2; transcript tier 3 only.
- The company replaces slides with a shareholder letter (EX-99.2) and runs a Q&A-heavy webcast, so the letter is the guidance source and the transcript adds only a few call-only items (FCF guide, Q4 exit gross margin, FX headwind, the DAU bonus plan).
- Motley Fool carried the Q2 2026 call, posted seven days after it (2026-08-12). Its editorial set includes TAKEAWAYS, RISKS, SUMMARY and INDUSTRY GLOSSARY blocks; keep only DATE / CALL PARTICIPANTS / Full Conference Call Transcript.
