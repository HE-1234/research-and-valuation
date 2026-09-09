# MANIFEST-transcript — Vistra Corp. (VST, CIK 0001692819) — Q2 2026 — transcript gatherer

Quarter: Q2 2026 (calendar quarter ended 2026-06-30). Earnings call: Friday 2026-08-07, 10:00 a.m. ET (9:00 a.m. CT), same morning as the earnings release (8-K accepted 07:00 ET). 10-Q filed 2026-08-10. **As-of cutoff: 2026-08-10.** Gatherer run: 2026-09-09. **Transcript source tier used: 3, third-party (The Motley Fool).**

## Files

| File | Origin URL | Fetch date | Source tier | Call date | Posting date | Word count |
|---|---|---|---|---|---|---|
| transcript.txt | https://www.fool.com/earnings/call-transcripts/2026/08/14/vistra-vst-q2-2026-earnings-call-transcript/ | 2026-09-09 | 3 third-party (The Motley Fool) | 2026-08-07 | 2026-08-14 (page metadata `article:published_time` 2026-08-14T12:54:21Z) | 9,493 total; 9,392 of call text after the one-line gatherer header |
| transcript-2026-Q1.txt (prior-quarter supplement) | https://www.fool.com/earnings/call-transcripts/2026/06/01/vistra-vst-q1-2026-earnings-call-transcript/ | 2026-09-09 | 3 third-party (The Motley Fool) | 2026-05-07 | 2026-06-01 (`article:published_time` 2026-06-01T21:01:52Z) | 9,239 total including the one-line header |
| notes-transcript.md | derived from the two files above (this gatherer) | 2026-09-09 | n/a | — | — | 9475 |
| MANIFEST-transcript.md | this file | 2026-09-09 | n/a | — | — | — |

Word counts are `wc -w` on the cached text files.

## Tier checks (AGENTS.md §12.2), in order

**Tier 1 — company-published (investor.vistracorp.com; WordPress/MediaRoom host behind Cloudflare, not Q4 Inc.). Result: no transcript.**
- Fetched with `curl -sS -L -A "company-research-skill owner@example.com"`; no 403s, no browser-header retry was needed.
- `https://investor.vistracorp.com/events-and-presentations` — HTTP 200, 85,868 bytes. The event list is JavaScript-rendered (`load_events` posts to `index.php` with `ajax`/`direction` args); the static HTML contains 0 occurrences of "transcript" and no event hrefs.
- `https://investor.vistracorp.com/news/events` — HTTP 200, 107,879 bytes. 0 occurrences of "transcript". Links found: the 2026-07-06 "Vistra to Report Second Quarter Results on Aug 7, 2026" notice, the 2026-07-29 dividend release, the 2026-08-07 results release.
- `https://investor.vistracorp.com/2026-08-07-Vistra-Reports-Second-Quarter-2026-Results` — HTTP 200, 287,290 bytes. 0 occurrences of "transcript". Its "Earnings Webcast" paragraph says the webcast is at 10 a.m. ET on Aug. 7, 2026, that "The live webcast and the accompanying slides" are on the IR site, and "A replay of the webcast will be available on Vistra's website for one year following the live event." Dial-in registration via dpregister.com.
- Sitemap `https://investor.vistracorp.com/?pagetemplate=googlesitemap` — HTTP 200, text/xml, 111 `<loc>` entries including `events-and-presentations?item=N` pages up to item=72. `https://investor.vistracorp.com/sitemap.xml` — HTTP 404.
- Event pages fetched: item=72 "Vistra Corp. Q2 2026 Results Call", Friday, August 7, 2026, 9:00am–10:00am CDT (HTTP 200). Links inside: "Listen to the Webcast" → `https://app.webinar.net/wWNgQrE7v2B` (audio/video webcast, not a transcript); slides `image/Q2_2026_Results_Presentation_vFinal.pdf` (left to the IR gatherer); dpregister.com dial-in registration; the release page. 0 occurrences of "transcript" and "replay". item=71 = Q1 2026 Results Call (slides `image/Q1+2026+Results+Presentation+vFINAL+2026-06-12.pdf`), item=70 = Q4 2025 call, item=69 = Q3 2025 call — same pattern, slides plus webcast/dial-in only. Conclusion: Vistra does not publish call transcripts.

**Tier 2 — 8-K exhibit. Result: none.**
- One request to `https://www.sec.gov/Archives/edgar/data/1692819/000169281926000017/0001692819-26-000017-index.htm` (UA `company-research-skill owner@example.com`), HTTP 200, 10,968 bytes, followed by a 2-second sleep; no further SEC requests. Documents listed: `vistra-20260807.htm` (8-K), `vistra-20260630xearningsre.htm` (EX-99.1, press release), two GRAPHIC jpgs, XBRL files (EX-101 schema/def/lab/pre). No EX-99.2, no prepared-remarks or transcript exhibit. Per the orchestrator, no other 8-K was filed 2026-08-07 to 2026-08-10; not re-checked here (no further SEC requests were made).

**Tier 3 — The Motley Fool. Result: USED.**
- `https://www.fool.com/robots.txt` — HTTP 200. The `User-agent: *` block contains no rule mentioning `/earnings/` or `/call-transcripts/` (it disallows `/a/`, `/account/`, `/admin`, `/feeds`, etc.); the path is permitted for `*`.
- Discovery: `https://www.fool.com/quote/nyse/vst/` — HTTP 200, 666,034 bytes; loose grep for `call-transcripts` found eight Vistra transcript slugs (2020–2021 and 2026), including `/earnings/call-transcripts/2026/08/14/vistra-vst-q2-2026-earnings-call-transcript/` and `/earnings/call-transcripts/2026/06/01/vistra-vst-q1-2026-earnings-call-transcript/`. Confirmed in the monthly sitemap `https://www.fool.com/sitemap/2026/08` (HTTP 200) which lists the Q2 2026 transcript URL (the `/2026/09` sitemap was not needed and not fetched).
- Transcript pages fetched with a browser-like UA (`Mozilla/5.0 (X11; Linux x86_64) ... Chrome/126.0.0.0 Safari/537.36`) plus Accept and Accept-Language headers: Q2 page HTTP 200, 544,221 bytes, no redirect; Q1 page HTTP 200, 516,751 bytes, no redirect. Page titles: "Vistra (VST) Q2 2026 Earnings Call Transcript | The Motley Fool" and "Vistra (VST) Q1 2026 Earnings Call Transcript | The Motley Fool".

**Tiers 4/5** — not applicable (no owner file; a transcript was found at tier 3).

## Call identity confirmation (Q2)
- Source DATE block: "Friday, Aug. 7, 2026 at 10:00 a.m. ET". Operator opening: "Good day, welcome to the Vistra Corp second quarter 2026 results conference call." IR host: "thank you for joining Vistra's investor webcast discussing our second quarter 2026 results." CFO: "we are reaffirming our 2026 Adjusted EBITDA guidance range of $6.8 billion-$7.6 billion".
- Matches the IR event item=72 (Q2 2026 Results Call, August 7, 2026, 9:00am CDT) and the release page's webcast paragraph.

## How the Fool pages were cleaned
- Script `/tmp/vst-orch/transcript/clean_fool.py` (python3 -P, BeautifulSoup 4 with lxml). Container `div#article-body-transcript`.
- **Kept:** the `DATE` paragraph, the `CALL PARTICIPANTS` list, and every `<p>` after the `<h2 id="full-conference-call-transcript">` heading (Q2: 145 paragraphs, operator opening through operator close; Q1: 110 paragraphs).
- **Dropped:** the "Image source: The Motley Fool." caption, the "Need a quote from a Motley Fool analyst?" line, empty `div.my-8` spacers, `div.article-body-promobox` (one inside the transcript section), and Fool's own editorial blocks under the headings TAKEAWAYS, RISKS, SUMMARY, INDUSTRY GLOSSARY (Q1 page had TAKEAWAYS, SUMMARY, INDUSTRY GLOSSARY). These are Fool-written and are not call content.
- Whitespace collapsed to single spaces; space-before-punctuation artefacts removed; non-breaking spaces normalised. No words changed. A one-line gatherer header (source, dates, caveat) was prepended to each cached file.
- **Page markers:** none. The cached text has no page numbers; notes cite `transcript.txt` line numbers (`l.N`), one paragraph per line with blank lines between.
- Raw HTML downloads (IR pages, SEC index, sitemaps, Fool pages) were kept only in `/tmp/vst-orch/transcript/` and deleted after extraction. No PDF was fetched by this gatherer.

## Transcript quality and garbling observed (Q2)
- Machine transcript; no "(sic)", "[inaudible]" or "[indiscernible]" markers in the source.
- Suspected garbles flagged in notes-transcript.md §7: "the PJM nuclear operate supported by power purchase agreements with Meta" (l.53; the Q1 call says "PJM nuclear uprate"); "ERCOT took an approach to do a BAS sort of slow things down" (l.109); sentence fragment "As a behind the meter or island is." (l.81); "3 of the 5%-6%" (l.219); "555" without units on first mention (l.77; "$555 a megawatt day" at l.123); July 22 prices "$57", "$400 or $500" without units (l.223–225).
- Name spellings: "Sean Stucki" (l.219, in Burke's speech) vs speaker label "Shawn Stuckey" (l.223); operator "Rini Singh" vs label "Rinny Singh" (l.273/275); the Wells Fargo questioner is labelled only "Constantine" (l.61) speaking "for Char" (Shahriar Pourreza). Stacey Doré's title is not stated on the Q2 call; the Q1 participant block gives "Executive Vice President and Chief Legal Officer".
- Q1 supplement coverage caveat: the Q1 text starts mid-way through the IR introduction (l.14, unlabelled); the operator opening and first sentences are missing. The Wells Fargo questioner is labelled "Unknown Analyst".

## As-of discipline
- Q2 call 2026-08-07 and 10-Q 2026-08-10 are both at or before the cutoff. The Fool Q2 page was posted 2026-08-14, after the cutoff; only call content was extracted, and Fool's post-call editorial blocks were dropped, so no post-cutoff information entered the cache. Both the call date and posting date are recorded above and in the file header.
- Nothing about Q3 2026 was opened. The Fool quote page and August sitemap were used only to locate the two URLs above; the three post-cutoff Fool opinion articles about Vistra listed in the August sitemap were not fetched. IR event item=72 was the newest event in the sitemap; nothing dated after 2026-08-10 was read on the IR site.
- The Q1 2026 transcript (call 2026-05-07, posted 2026-06-01) is pre-cutoff and cached as a labelled supplement only.

## Fetch failures and backoffs
- None. Every request returned HTTP 200 on the first attempt except `https://investor.vistracorp.com/sitemap.xml` (404; the `?pagetemplate=googlesitemap` alternative worked). No Cloudflare 403 was encountered; no browser-header retry was needed on the IR site.

## Scope
- Files written by this gatherer: `transcript.txt`, `transcript-2026-Q1.txt`, `notes-transcript.md`, `MANIFEST-transcript.md`, all in `companies/VST/sources/2026-Q2/`. `MANIFEST.md` was not written (runner merges). No other file in the folder was touched. No git command was run.
