# MANIFEST — transcript gatherer — McDonald's Corporation (MCD, NYSE, CIK 0000063908) — Q2 2026

As-of cutoff: 2026-08-07 (10-Q filing date). Call date: 2026-08-04, 8:30 am ET. Gatherer run: 2026-09-08.

| file | origin URL | fetch date | source tier | word count |
|---|---|---|---|---|
| transcript.txt | https://www.fool.com/earnings/call-transcripts/2026/08/11/mcdonalds-mcd-q2-2026-earnings-call-transcript/ | 2026-09-08 (cached by the earlier interrupted run on 2026-09-08; page re-fetched and the cache verified word-for-word on 2026-09-08; cached file reused unchanged) | 3, third-party free (The Motley Fool machine transcript) | 9,793 (9,701 words of call text plus 92 words of header and participant list) |
| notes-transcript.md | derived from transcript.txt by this gatherer; §10 cross-checked against press-release.txt and press-release-supplement.txt cached by the IR gatherer | 2026-09-08 | n/a | 13,744 |

## Tier walk (AGENTS.md §12.2, in order)

### Tier 1, company-published transcript (McDonald's IR): UNREACHABLE

The orchestrator's probes on 2026-09-08 found the whole corporate.mcdonalds.com domain failing from this host (curl error 92 "HTTP/2 stream was not closed cleanly: INTERNAL_ERROR" within 0.1 s from the Akamai edge; `--http1.1` timing out with 0 bytes). This gatherer made three further attempts at about 20:58 UTC on 2026-09-08, roughly 60 seconds in total, with `-A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36" -H "Accept: text/html" -sS -L --max-time 30`:

- (a) `--http1.1` https://corporate.mcdonalds.com/corpmcd/investors/events-and-presentations.html : `curl: (28) Operation timed out after 30001 milliseconds with 0 bytes received`; http_code=000, size=0, remote_ip=23.59.88.235.
- (b) `--http2 -H "Accept-Language: en-US"` same URL: `curl: (92) HTTP/2 stream 1 was not closed cleanly: INTERNAL_ERROR (err 2)`; http_code=000, size=0, time 0.118 s, remote_ip=23.59.88.235.
- (c) `--http1.1` https://corporate.mcdonalds.com/corpmcd/en-us/investors.html : `curl: (28) Operation timed out after 30002 milliseconds with 0 bytes received`; http_code=000, size=0.

No page loaded, so no search for "transcript" or "prepared remarks" was possible. Whether McDonald's publishes a transcript of this call is unknown from this host; tier 1 is recorded as not obtainable, not as non-existent.

### Tier 2, 8-K exhibits: NO TRANSCRIPT OR PREPARED REMARKS

Fetched with User-Agent `company-research-skill owner@example.com`, 2.5 s apart; both HTTP 200; no 403 or 429 encountered, so no back-off was needed.

- https://www.sec.gov/Archives/edgar/data/63908/000006390826000067/0000063908-26-000067-index.htm (10,910 bytes): Form 8-K, filed 2026-08-04, accepted 2026-08-04 07:01:40, period of report 2026-08-04, Items 2.02 (Results of Operations and Financial Condition) and 9.01. Documents: 1 `mcd-20260804.htm` 8-K (iXBRL, 33,940 bytes); 2 `exhibit991-6302026.htm` EX-99.1 (176,954 bytes; the earnings release); 3 `exhibit992-6302026.htm` EX-99.2 (498,351 bytes; supplemental information); 7 `archyellowlogoa07.jpg` GRAPHIC; 8 `form8k06302026.pdf` 8-K PDF; XBRL files 4, 5, 6 and 20; complete submission text file. No transcript and no prepared remarks.
- https://www.sec.gov/Archives/edgar/data/63908/000006390826000069/0000063908-26-000069-index.htm (10,378 bytes): Form 8-K, filed 2026-08-04, accepted 2026-08-04 07:44:19, period of report 2026-08-03, Items 5.02 (officer changes), 7.01 (Regulation FD) and 9.01. Documents: 1 `mcd-20260803.htm` 8-K (iXBRL, 31,943 bytes); 2 `exhibitpressrelease.htm` EX-99.1 (10,780 bytes; the officer-change press release); 6 `pdfof8-k.pdf`; XBRL files 3, 4, 5 and 17; complete submission text file. No transcript and no prepared remarks.

The exhibits themselves were not downloaded by this gatherer; the IR and filings gatherers own them.

### Tier 3, The Motley Fool: USED

- Discovery: the transcript URL appears both in the cached quote page `/tmp/mcd-orch/fool_quote.html` (from https://www.fool.com/quote/nyse/mcd/) and in the cached monthly sitemap `/tmp/mcd-orch/fool_sitemap_202608.xml` (from https://www.fool.com/sitemap/2026/08), both fetched by the orchestrator on 2026-09-08.
- robots.txt: https://www.fool.com/robots.txt returned HTTP 200 (2,311 bytes). The `User-agent: *` block carries about 90 `Disallow` prefixes (for example `/a/`, `/account/`, `/investing/stocks/`, `/premium-reports`, `/quote/failed-lookup/`); none matches `/earnings/call-transcripts/2026/08/11/mcdonalds-mcd-q2-2026-earnings-call-transcript/`. The two bare `Disallow: /` lines sit in named-bot blocks, not under `*`. Path allowed.
- Fetch: HTTP 200, 534,048 bytes, 0.41 s, browser UA. Page title "McDonald's (MCD) Q2 2026 Earnings Call Transcript | The Motley Fool". JSON-LD `datePublished` and `dateModified` both `2026-08-11T16:57:58.000Z`. The page's DATE section reads "Tuesday, Aug. 4, 2026 at 8:30 a.m. ET".
- Admissibility under §12.2: the call (2026-08-04) precedes the as-of cutoff (2026-08-07); the transcript was posted 2026-08-11, after the cutoff. It is admitted because only call content is used. Fool's editorial sections (Takeaways, Risks, Summary, Industry Glossary, promotional blocks, "Read Next") were excluded from the cache and were not read for the notes. Call date and posting date are recorded here and in the headers of `transcript.txt` and `notes-transcript.md`.
- Verification of the cached file against the fresh page (Python, 2026-09-08): the article body was extracted to `/tmp/mcd-orch/transcript/fool_q2_body_fresh.txt` (164 paragraphs, 10,666 words including Fool's editorial sections); the transcript-only portion is 114 paragraphs, 9,701 words. The cached `transcript.txt` call text is also 9,701 words (difference 0.0%). After normalising the one layout difference (Fool renders "Speaker: text" inline; the cache puts each speaker name on its own line), the paragraph sequences are identical except that the cache splits the operator's opening paragraph into three lines (l.14, l.15, l.16; same words). Three-point check: the operator's opening sentence ("Hello, and welcome to McDonald's Second Quarter 2026 Investor Conference Call. At the request of McDonald's Corporation, this conference is being recorded.") is identical; the mid-call exchange (Brian Harbour's question and the CEO's answer, l.101–109) is identical; the closing line ("This concludes McDonald's Corporation Investor Call. You may now disconnect, and have a great day.") is identical. Decision: cached file REUSED unchanged; nothing rewritten; line numbers unchanged.
- Cleanups in the cached file (applied by the earlier run, confirmed now): Fool's editorial sections removed; only DATE (folded into the header), CALL PARTICIPANTS and the full transcript kept; a four-line header added (source URL, tier, call date, posting date, fetch date, note that no page numbers exist and line numbers are cited). The text contains no "(sic)" strings, no bracketed insertions other than "[Operator Instructions]" (l.15 and l.60) and no non-ASCII characters. Nothing else was altered.
- Structure verified: 212 lines (211 plus a trailing newline). l.1–4 header; l.6–9 participants (Dexter Congbalay, Vice President of Investor Relations; Chris Kempczinski, Chairman and Chief Executive Officer; Ian Borden, Chief Financial Officer); l.13–57 prepared remarks (operator, IR head, CEO, CFO, CEO); l.59–60 operator instructions; l.62–205 Q&A with 8 analyst questions in this order: David Palmer (Evercore), Dennis Geiger (UBS), Brian Harbour (Morgan Stanley), John Ivankoe (JPMorgan), Sara Senatore (Bank of America), David Tarantino (Baird), Jon Tower (Citi), Lauren Silberman (Deutsche); six were introduced by the IR head and two (Tarantino, Silberman) by the operator; three asked multi-part questions (Ivankoe, Senatore, Silberman). l.208 IR head's close; l.211 operator's sign-off ("This concludes McDonald's Corporation Investor Call.").

### Tiers 4 and 5: not applicable (no owner-supplied file; a transcript exists). The prior-quarter (Q1 2026, 2026-05-07) Fool transcript was not fetched, per the orchestrator's instruction.

## Release cross-check summary (notes §10)

20 figures spoken on the call could be checked against `press-release.txt` or `press-release-supplement.txt`; all 20 match, two of them via arithmetic (Q2 G&A at 2.2% of systemwide sales from SG&A $817 million over about $37 billion; "international more than half of systemwide sales and operating profit" from the segment tables). Two references to prior guidance ($0.20 to $0.30 FX tailwind; 50,000 restaurants by the end of 2027) do not appear in the cached Q1 or Q2 release texts and are recorded as unverifiable. No numeric discrepancy was found. One caution recorded for the writer: the call's "$40 billion" (systemwide-sales growth under Accelerating the Arches) and the release's "$40 billion" (trailing-twelve-month systemwide sales to loyalty members) are different metrics. Release items not spoken on the call (dividend, buybacks, capex, tax rate, operating-margin range, free-cash-flow conversion, net additions, restructuring charges, effective tax rate) are listed in notes §2 and §10.

## Citation check

Script `/tmp/mcd-orch/transcript/check_quotes.py`, run 2026-09-08 on the final `notes-transcript.md`: every double-quoted string of 15 or more characters on a line carrying an `l.N` tag was tested as a substring of the cited transcript line(s) after whitespace and quote-mark normalisation. 348 quotations checked; 0 problems (not found or mis-cited); 13 quotations on tagged lines are from the release or supplement and were verified against those files instead. Quoted strings on untagged lines are the header's term names and the release's outlook wording (checked against the supplement by hand).

## As-of discipline

Nothing published after 2026-08-07 was used except the Fool transcript page (posted 2026-08-11) of the 2026-08-04 call, from which only call content was taken. Other documents read by this gatherer: the two SEC filing indexes (filings of 2026-08-04), fool.com's robots.txt, and the already-cached `press-release.txt`, `press-release-supplement.txt` and, only to test the two prior-guidance references, `press-release-supplement-2026-Q1.txt` (release of 2026-05-07). All pre-cutoff. No 10-K, 10-Q, 8-K or DEF 14A text was read by this gatherer.

## Scratch and hygiene

Scripts and downloads were kept under `/tmp/mcd-orch/transcript/` only: `fool_q2_body_fresh.txt` (extracted text), `fool_q2_body_raw.txt` (stale, from the earlier run), `fool_robots.txt`, `check_quotes.py`. The downloaded HTML (`fool_q2_page.html`, `tier1_a.html`, `tier1_b.html`, `tier1_c.html`, the two SEC index pages) was deleted after use; no HTML was cached in the repository. No git commands were run.

## Not produced by this gatherer

`press-release.txt`, `press-release-supplement.txt`, `press-release-2026-Q1.txt`, `press-release-supplement-2026-Q1.txt`, `10-K-FY2022.txt`, `10-K-FY2023.txt`, `10-K-FY2024.txt`, `10-K-FY2025.txt`, `10-Q-2026-Q2.txt`, `DEF14A-2026.txt`, every `8-K-*.txt` file (including `8-K-2026-08-04-officer.txt`) and `MANIFEST.md` (merged by the orchestrator). This gatherer wrote only `notes-transcript.md` and `MANIFEST-transcript.md`; `transcript.txt` was left exactly as cached.
