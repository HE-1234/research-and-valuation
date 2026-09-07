# notes-transcript.md — Applied Optoelectronics, Inc. (AAOI) — Q2 2026 earnings call

Call date: 2026-08-06, 4:30 p.m. Eastern (per the company's event page and press release). Fiscal quarter: Q2 2026 (three months ended 2026-06-30). As-of cutoff: 2026-08-06.
Source file: none. **Transcript source tier: none.** Origin URL: none.
Tag that would have been used: `[Q2 2026 call]`. No sentence in the report may carry this tag, because no transcript text exists in `sources/2026-Q2/`.
Speakers: not verifiable. The press release names Dr. Thompson Lin (Founder, Chairman and CEO) and Dr. Stefan Murry (CFO and Chief Strategy Officer) as call hosts; whether anyone else spoke, and what anyone said, is not documented here.

## 0. What this file is

No transcript of the 2026-08-06 call could be obtained from any permitted source tier (AGENTS.md §12.2) as of the gatherer run on 2026-09-07. This file therefore contains no quotes, no guidance bullets, no analyst questions, and no word counts. Nothing below is drawn from the call itself. Sections 1–6 of the normal notes-transcript layout are omitted rather than filled with material from other documents.

## 1. Every URL attempted, with HTTP status (gatherer run 2026-09-07)

Tier 1 — company-published transcript (investors.ao-inc.com; browser-like User-Agent, 2 s between requests)

| URL | HTTP | Bytes | What was found |
|---|---|---|---|
| https://investors.ao-inc.com/events/event-details/applied-optoelectronics-q2-2026-earnings-call | 200 | 34,353 | Page title "Applied Optoelectronics Q2 2026 Earnings Call", date "August 6, 2026", one link "Listen to webcast" (to https://edge.media-server.com/mmc/p/fdq5dksv) and one attachment `/static-files/ccf74096-279b-47ca-b795-cd9f24cb9278` (anchor text "2Q26 Trended Quarterly Financial Results", `type="application/pdf"`, `title="Q2 2026 Trended Financials 8_6_26 2.20pm.pdf"`, listed size 215.2 KB). Zero occurrences of the string "transcript". |
| https://investors.ao-inc.com/static-files/ccf74096-279b-47ca-b795-cd9f24cb9278 | (HEAD; no headers returned) | — | Identified from the anchor attributes above as a supplemental trended-financials PDF, not a transcript. Not downloaded by this gatherer; left for the IR gatherer. |
| https://investors.ao-inc.com/financial-information/quarterly-results | 200 | 116,940 | Q2 2026 entries: "Applied Optoelectronics Reports Second Quarter 2026 Results" (press release) and "Applied Optoelectronics Q2 2026 Earnings Call" (event link). Zero occurrences of "transcript" anywhere on the page (all quarters 2022–2026). |
| https://investors.ao-inc.com/news-events/events-and-presentations | 200 | 58,669 | Lists the Q2 2026 call dated August 6, 2026. Zero occurrences of "transcript". |
| https://edge.media-server.com/mmc/p/fdq5dksv (the Q2 call's "Listen to webcast" target) | 200 | 3,810 | A JavaScript media-player shell (`MMC` player, `theoplayer2`) with an empty `<title>`, zero text lines after script removal, and no reference to a transcript, caption, .vtt or .srt asset. Audio/video only, not fetchable as text. |
| https://event.choruscall.com/mediaframe/webcast.html?webcastid=Q7Es6HG9 (a webcast link on the events listing page) | 200 | 26,535 | Turned out to be the registration page for the "Applied Optoelectronic OFC Conference and Exhibition Investor Session" of 2026-03-17, not the Q2 call. No transcript. Recorded only because it was fetched. |

Result: no company-published transcript.

Tier 2 — 8-K exhibit (www.sec.gov; User-Agent `company-research-skill owner@example.com`, 1 s after the request)

| URL | HTTP | Bytes | What was found |
|---|---|---|---|
| https://www.sec.gov/Archives/edgar/data/1158114/000168316826006055/ | 200 | 12,841 | Folder for accession 0001683168-26-006055 (Form 8-K, 2026-08-06). Documents: `aaoi_8k.htm`, `aaoi_ex9901.htm`, `image_001.jpg`, XBRL files (`aaoi-20260806.xsd`, `aaoi-20260806_lab.xml`, `aaoi-20260806_pre.xml`, `aaoi_8k_htm.xml`, `FilingSummary.xml`, `MetaLinks.json`, `R1.htm`), the full-submission `.txt`, and the two index pages. Exactly one exhibit (99.1, the press release). No Exhibit 99.2, no "prepared remarks", no "transcript". |

Result: no transcript or prepared remarks in the 8-K.

Tier 3 — The Motley Fool (www.fool.com; browser-like User-Agent, 2 s between requests)

| URL | HTTP | Bytes | What was found |
|---|---|---|---|
| https://www.fool.com/robots.txt | 200 | 2,311 | `User-agent: *` block does not disallow `/earnings/` or `/earnings/call-transcripts/`. Fetching transcript pages is permitted. Sitemaps listed: `/sitemap/`, `/news-sitemap.xml`, others. |
| https://www.fool.com/quote/nasdaq/aaoi/ | 200 | 654,737 | AAOI call-transcript links present: 2021/05/06, 2021/08/06, 2021/11/05, 2022/02/25, 2022/08/05, 2025/08/07 (`applied-optoelectronics-aaoi-earnings-call`), 2026/02/26 (`applied-optoelectronics-aaoi-earnings-call`), 2026/05/07 (`aaoi-q1-2026-earnings-call-transcript`). Zero matches for `call-transcripts/2026/08`. Newest listed transcript is the Q1 2026 call. |
| https://www.fool.com/news-sitemap.xml | 200 | 170,755 | 237 URLs, publication dates 2026-09-05 to 2026-09-07 only (rolling two-day window). No `aaoi` or `applied-optoelectronics` entry. |
| https://www.fool.com/sitemap/ | 200 | 39,493 | Sitemap index of monthly sub-sitemaps `/sitemap/YYYY/MM`, 1995/03 through 2026/09. No separate earnings or transcript sitemap. |
| https://www.fool.com/sitemap/2026/08 | 200 | 998,715 | 6,143 URLs, of which 1,964 are `/earnings/call-transcripts/2026/08/...` (12 dated 08/06, 276 dated 08/07). No `aaoi` slug and no `applied-optoelectronics` transcript slug. The only AAOI-related URL is `https://www.fool.com/investing/2026/08/24/why-applied-optoelectronics-stock-dived-by-almost/`, a stock-move article dated 2026-08-24, after the cutoff; not a transcript; NOT fetched. |
| https://www.fool.com/sitemap/2026/09 | 200 | 147,633 | No `aaoi`, `applied-optoelectronics`, or `opto` entry. |
| https://www.fool.com/earnings/call-transcripts/2026/08/06/aaoi-q2-2026-earnings-call-transcript/ | 404 | 34,994 | "404 - Page Not Found" |
| https://www.fool.com/earnings/call-transcripts/2026/08/07/aaoi-q2-2026-earnings-call-transcript/ | 404 | 34,951 | "404 - Page Not Found" |
| https://www.fool.com/earnings/call-transcripts/2026/08/06/applied-optoelectronics-aaoi-earnings-call/ | 404 | 35,019 | "404 - Page Not Found" |
| https://www.fool.com/earnings/call-transcripts/2026/08/07/applied-optoelectronics-aaoi-earnings-call/ | 404 | 35,019 | "404 - Page Not Found" |
| https://www.fool.com/earnings/call-transcripts/2026/08/06/applied-optoelectronics-aaoi-q2-2026-earnings-call/ | 404 | 35,059 | "404 - Page Not Found" |
| https://www.fool.com/earnings/call-transcripts/2026/08/07/applied-optoelectronics-aaoi-q2-2026-earnings-call/ | 404 | 35,059 | "404 - Page Not Found" |

Result: The Motley Fool had not published a transcript of the AAOI Q2 2026 call as of 2026-09-07. Its quote page and its complete monthly sitemaps for August and September 2026 both omit it, so this is an absence in Fool's catalogue, not a slug-guessing failure.

Tier 4 — owner-supplied file: none was supplied.

Tier 5 — none. This is the tier recorded.

## 2. Consequences for the writer

- The press release (cached by the IR gatherer as `press-release.txt`, from 8-K Exhibit 99.1 `aaoi_ex9901.htm`) is the only as-of source of management's Q3 2026 guidance and of any management quotation. Guidance in `outlook.md` §4 must be quoted from `press-release.txt` and tagged to it, not to `[Q2 2026 call]`.
- There is no as-of record of analyst questions, of anything management declined to answer, of prepared-remarks wording on vision or growth engines, or of tone. `outlook.md` §5 must list which claims could not be sharpened for lack of a transcript (AGENTS.md §12.2, tier 5), and §6 (tone shift) cannot be measured against this quarter's call on a future refresh.
- The event page's "2Q26 Trended Quarterly Financial Results" PDF (`/static-files/ccf74096-279b-47ca-b795-cd9f24cb9278`) is a company document dated to the call day and is within the as-of window; it belongs to the IR gatherer, not this file.
- For context only: a Fool transcript of the prior-quarter call (Q1 2026, 2026-05-07) is listed at `https://www.fool.com/earnings/call-transcripts/2026/05/07/aaoi-q1-2026-earnings-call-transcript/`. It is before the cutoff and could lawfully be fetched, but it documents the Q1 2026 call, not the as-of quarter's call; it was not fetched or read for this run. If the coordinator wants it as background, it would need its own tag (`[Q1 2026 call]`) and its own tier record.

## 3. Sources

- No cached transcript file. Every URL above was fetched on 2026-09-07; HTML and XML were downloaded to /tmp and deleted after inspection. Nothing was saved from them except the facts recorded in this file and in `MANIFEST-transcript.md`.

(End of file. Sections on guidance, vision, analyst questions, deflections, cross-check numbers, and repeated phrases are intentionally absent: no transcript, no extraction.)

- Prior-quarter supplement (added 2026-09-07 at the coordinator's request): the Q1 2026 call of 2026-05-07 (pre-cutoff, tier 3, The Motley Fool) is cached as `transcript-2026-Q1.txt` and extracted in `notes-transcript-2026-Q1.md`, tag `[Q1 2026 call]`. It is the PRIOR quarter's call, not the as-of Q2 2026 call; the tier for the Q2 2026 call remains none.
