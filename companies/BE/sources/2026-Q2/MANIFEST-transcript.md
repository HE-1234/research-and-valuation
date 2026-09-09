# MANIFEST — transcript gatherer — Bloom Energy Corporation (BE, CIK 0001664703) — Q2 2026

Quarter: Q2 2026 (three months ended 2026-06-30; fiscal year = calendar year). Earnings call: 2026-07-28, 5:00 p.m. ET (company Q4 Inc. event feed, EventId 1025). 10-Q filed 2026-07-28; 10-Q/A filed 2026-07-29. As-of cutoff: 2026-07-29.
Gatherer run date: 2026-09-09. User-Agents: SEC `company-research-skill owner@example.com` with `Accept-Encoding: gzip, deflate` (one request, no back-off needed); all other hosts `Mozilla/5.0 (compatible; company-research-skill; owner@example.com)` with 1.7–2 s spacing (one 10 s back-off per 403 on the IR site). Scratch: /tmp/be-orch/transcript/ (raw HTML/JSON kept there only; nothing binary or HTML is stored in the repo).

**Transcript source tier for the Q2 2026 call: NONE.** No transcript of the 2026-07-28 call exists at tiers 1–3 as of 2026-09-09; no tier-4 file was supplied. Two pre-cutoff calls are cached as labelled supplements (tier 5 procedure, AGENTS.md §12.2).

## Files

| File | Origin URL | Fetch date | Source tier | Word count |
|---|---|---|---|---|
| transcript.txt | — not created: no Q2 2026 transcript exists | — | none | — |
| transcript-2026-Q1.txt | https://www.fool.com/earnings/call-transcripts/2026/04/28/bloom-energy-be-q1-2026-earnings-transcript/ | 2026-09-09 | 3 third-party (Motley Fool), SUPPLEMENT: Q1 2026 call held 2026-04-28, page published 2026-04-29T03:05:28Z; tag `[Q1 2026 call]` | 8,266 total (8,158 in the call body after the 3-line file header and the Date/Call participants block) |
| transcript-2025-Q4.txt | https://www.fool.com/earnings/call-transcripts/2026/02/05/bloom-energy-be-q4-2025-earnings-call-transcript/ | 2026-09-09 | 3 third-party (Motley Fool), SUPPLEMENT: Q4 2025 call held 2026-02-05, page published 2026-02-05T23:32:47Z; tag `[Q4 2025 call]` | 8,216 total (8,090 in the call body) |
| notes-transcript.md | derived from the two supplements and the tier checks | 2026-09-09 | n/a | see file |
| MANIFEST-transcript.md | this file | 2026-09-09 | n/a | see file |

## Tier checks (every request, in order)

### Tier 1 — company-published transcript (investor.bloomenergy.com, Q4 Inc.-hosted) — result: **none**

| URL | HTTP | Bytes | Finding |
|---|---|---|---|
| https://investor.bloomenergy.com/feed/Event.svc/GetEventList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1&eventDateFilter=All | 200 | 4,601 | Byte-identical to the orchestrator's /tmp/be-orch/event-2026.json. Three 2026 events: EventId 1004 "Bloom Energy Q4 2025 Earnings Conference Call" 02/05/2026 17:00; 1017 "Q1 2026 Earnings Conference Call" 04/28/2026 17:00; 1025 "Bloom Energy Q2 2026 Earnings Conference Call" 07/28/2026 17:00. Each carries exactly one attachment titled "Supplemental Financial Information" (Q2 2026: https://s29.q4cdn.com/452919417/files/doc_financials/2026/q2/Q226-Supplemental-Financial-Information.pdf) and a webcast link (Q2 2026: https://events.q4inc.com/attendee/949393051). Zero occurrences of "transcript". |
| https://investor.bloomenergy.com/feed/FinancialReport.svc/GetFinancialReportList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1&reportSubType= | 200 | 3,122 | Byte-identical to /tmp/be-orch/finrep-2026.json. "Second Quarter 2026" lists two documents: "Q2 Earnings Release" (Q226-Earnings-release.pdf) and "Q2 Supplemental Financial Information" (Q226-Supplemental-Financial-Information.pdf); "First Quarter 2026" likewise two. Zero occurrences of "transcript". |
| https://investor.bloomenergy.com/feed/PressRelease.svc/GetPressReleaseList?LanguageId=1&pageSize=20&pageNumber=0&includeTags=true&year=2026&excludeSelection=1 | 200 | 32 | `{"GetPressReleaseListResult":[]}` — empty. |
| https://investor.bloomenergy.com/feed/ContentAsset.svc/GetContentAssetList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1 | 200 | 32 | `{"GetContentAssetListResult":[]}` — empty. |
| https://investor.bloomenergy.com/feed/Presentation.svc/GetPresentationList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1 | 403, 403, 403 | 6,136 / 6,136 / 6,221 | Cloudflare "Just a moment..." challenge page on the first try, on a retry after a 10 s back-off, and on a third try with a Chrome desktop UA. Feed not readable. |
| https://investor.bloomenergy.com/events-and-presentations/default.aspx | 403, 403 | 5,675 / 5,675 | Cloudflare "Just a moment..." before and after a 10 s back-off. Expected per brief; moved on. |
| https://investor.bloomenergy.com/financials/quarterly-results/default.aspx | 403, 403 | 5,687 / 5,687 | Same Cloudflare challenge before and after a 10 s back-off. |

The orchestrator's 2025 event feed (/tmp/be-orch/event-2025.json, read from disk) shows the same pattern for every 2025 earnings event: supplemental deck plus webcast, no transcript. The webcast replay was not opened and the audio was not transcribed.

### Tier 2 — 8-K exhibit — result: **none**

| URL | HTTP | Bytes | Finding |
|---|---|---|---|
| https://www.sec.gov/Archives/edgar/data/1664703/000162828026050150/0001628280-26-050150-index.htm | 200 | 17,576 | 8-K filed 2026-07-28, accepted 16:07:21, period 2026-07-28, Items 2.02, 7.01, 9.01. Document Format Files: seq 1 be-20260728.htm (8-K, iXBRL); seq 2 ex991_q226financialresults.htm (EX-99.1, 559,627 B, press release); seq 3 ex992q226supplementalfin.htm (EX-99.2, 20,890 B, supplemental financial information wrapper) plus 19 GRAPHIC files ex992q226supplementalfin001–019.jpg and two logo JPGs; XBRL schema/label/presentation files. Zero occurrences of "transcript" and "prepared remarks". Identical size to the orchestrator's cached copy (/tmp/be-orch/8k-0728-index.html, 17,576 B). |
| /tmp/be-orch/submissions.json (read from disk; fetched by the orchestrator from https://data.sec.gov/submissions/CIK0001664703.json) | — | 158,232 | Filings dated 2026-07-27..2026-07-30: SCHEDULE 13G/A 2026-07-27 (0002012383-26-002272), 8-K 2026-07-28 (0001628280-26-050150), 10-Q 2026-07-28 (0001628280-26-050247), 10-Q/A 2026-07-29 (0001628280-26-050325). No other 8-K on 07-28 or 07-29. Only filing dates and form types were read; nothing filed after the cutoff was opened. |

### Tier 3 — third-party free (The Motley Fool) — result: **none for Q2 2026; used for supplements**

| URL | HTTP | Bytes | Finding |
|---|---|---|---|
| https://www.fool.com/robots.txt | 200 | 2,311 | `User-agent: *` block: `Allow: /a/feeds/`, `Allow: /ads.txt`, sitemap lines, then Disallow entries (/3910, /a/, /account/, /admin, /amptest/, /art/, /auth/, /betaboards/, /cdn-cgi/, /Common/, /dubs/, /ecap/, /ext-content/, /external/, /feeds, /fool/free-report, /foolpics, /free-report, /help, /includes, /investing/businesswire/, /investing/fiercemarkets/, /investing/stocks/, /investor-alert/, /localize, /login/, /mailemergency, /Marketing/EcapSurvey.aspx, /mms, /news/commentary/, /news/xt, /newsletters/*, /nexus/, /now50/, /offers/, /order-results*, /order/, /p/*, /partners, /pegulator, /premium-reports, /private, /quote/failed-lookup/, /quote/unknown/, /reports, /scripts, /secure/, /server, /shop/, ...). No line contains "earnings" or "transcript"; `/earnings/call-transcripts/` is permitted. |
| https://www.fool.com/quote/nyse/be/ | 200 | 657,131 | Embedded JSON `transcripts` array lists eight BE transcript paths: 2019/11/08 (Q3 2019), 2020/03/17 (Q4 2019), 2020/05/12 (Q1 2020), 2021/11/05 (Q3 2021), 2025/10/28 (Q3 2025), 2026/02/05 (Q4 2025), 2026/04/28 bloom-energy-be-q1-2026-earnings-transcript (headline "Bloom Energy (BE) Q1 2026 Earnings Transcript", publish_at 2026-04-29T03:05:28Z), and 2026/04/28 bloom-energy-be-q2-2025-earnings-transcript. **No Q2 2026 entry.** Consistent with the orchestrator's copy fetched earlier on 2026-09-09. Only the transcript list was read. |
| https://www.fool.com/sitemap/2026/07 | 200 | 707,910 | Byte-identical to /tmp/be-orch/fool-sitemap-2026-07.html. 4,515 `<loc>` entries; 214 under /earnings/call-transcripts/ dated 2026-07-01..07-30 (123 of them dated 07-28..07-30, so Fool was posting transcripts that week). None contains "bloom" or "-be-q". |
| https://www.fool.com/sitemap/2026/08 | 200 | 995,365 | Byte-identical to /tmp/be-orch/fool-sitemap-2026-08.html. 6,121 `<loc>`; 1,964 call-transcript URLs dated 2026-08-03..08-31. The only "bloom" match is bloomin-brands-blmn-q2-2026 (a different company). No Bloom Energy transcript. |
| https://www.fool.com/sitemap/2026/09 | 200 | 191,775 | 1,197 `<loc>`; 46 call-transcript URLs dated 2026-08-31..09-08. No Bloom Energy transcript. |
| https://www.fool.com/earnings/call-transcripts/2026/07/28/bloom-energy-be-q2-2026-earnings-call-transcript/ | 404 | 35,880 | "404 - Page Not Found" |
| https://www.fool.com/earnings/call-transcripts/2026/07/29/bloom-energy-be-q2-2026-earnings-call-transcript/ | 404 | 35,880 | "404 - Page Not Found" |
| https://www.fool.com/earnings/call-transcripts/2026/07/28/bloom-energy-be-q2-2026-earnings-transcript/ | 404 | 35,855 | "404 - Page Not Found" |
| https://www.fool.com/earnings/call-transcripts/2026/07/29/bloom-energy-be-q2-2026-earnings-transcript/ | 404 | 35,855 | "404 - Page Not Found" |
| https://www.fool.com/earnings/call-transcripts/2026/04/28/bloom-energy-be-q1-2026-earnings-transcript/ | 200 | 493,501 | Title "Bloom Energy (BE) Q1 2026 Earnings Transcript"; Date block "April 28, 2026" (no time given); IR intro "Bloom Energy's First Quarter 2026 Earnings Call"; `datePublished` 2026-04-29T03:05:28.000Z. **USED as supplement → transcript-2026-Q1.txt.** |
| https://www.fool.com/earnings/call-transcripts/2026/02/05/bloom-energy-be-q4-2025-earnings-call-transcript/ | 200 | 495,950 | Title "Bloom Energy (BE) Q4 2025 Earnings Call Transcript"; Date block "Thursday, February 5, 2026 at 5 p.m. ET"; IR intro "fourth quarter and full year 2025 earnings call"; `datePublished` 2026-02-05T23:32:47.000Z. **USED as supplement → transcript-2025-Q4.txt.** |
| https://www.fool.com/earnings/call-transcripts/2026/04/28/bloom-energy-be-q2-2025-earnings-transcript/ (the odd quote-page slug) | 200 | 457,001 | Title "Bloom Energy (BE) Q2 2025 Earnings Transcript"; Date block "Thursday, July 31, 2025 at 5 p.m. ET"; IR intro "Second Quarter 2025 Earnings Call"; `datePublished` 2026-04-28T16:15:37.000Z. It is the year-ago (Q2 2025) call, posted nine months late on the day of the Q1 2026 call. Genuine pre-cutoff Bloom call, but outside the supplement scope (prior quarter and initial-guidance call). **Inspected, not cached**; recorded here so the writer knows it exists. Scratch text at /tmp/be-orch/transcript/scratch-oddslug-q2-2025.txt (6,622 words) only. |

### Tiers 4 and 5

- Tier 4 (owner-supplied file): none supplied.
- Tier 5 (none): applies. `outlook.md` header: `Transcript source tier: none`. Supplements fetched per §12.2: the prior-quarter call (Q1 2026, 2026-04-28) and, because it carried the initial FY2026 guidance, the Q4 2025 call (2026-02-05). Both are for business.md wording and outlook §1's "what management had said to expect" column only; never for Q2 2026 guidance.

## As-of discipline

- Q2 2026 call date 2026-07-28; cutoff 2026-07-29. No transcript of that call exists, so nothing post-cutoff about the call was read or used.
- Supplement 1: Q1 2026 call held 2026-04-28; Fool page published 2026-04-29T03:05:28Z (page `datePublished`, matching the quote-page `publish_at`). Both dates precede the cutoff.
- Supplement 2: Q4 2025 call held 2026-02-05; Fool page published 2026-02-05T23:32:47Z. Both dates precede the cutoff.
- The odd-slug page is a transcript of the 2025-07-31 call published 2026-04-28T16:15:37Z; pre-cutoff on both counts; not cached.
- Post-cutoff documents touched: the Fool quote page and the 2026/07, 2026/08 and 2026/09 sitemaps (fetched 2026-09-09) were used solely to establish whether a transcript of the 2026-07-28 call exists; only transcript URL lists were parsed. The 2026/08 and 2026/09 sitemaps contain URL slugs of post-cutoff Bloom news articles; these were not read, recorded or used. The submissions JSON lists filings after the cutoff; only form types and dates in the 07-27..07-30 window were read. No later calls, news or filings were opened.
- Fool editorial blocks written after each call (Takeaways, Summary, Industry glossary, promo box, analyst-quote solicitation, image caption) were stripped from both supplements, so each cached file contains only what was said on its call date.

## Processing notes

- HTML stripped with python3 -P + BeautifulSoup 4.13.5 (lxml 5.3.0), run from /home/ubuntu with the script /tmp/be-orch/transcript/fool2txt.py. Kept from `div.article-body.transcript-content`: the DATE `<p>`, the CALL PARTICIPANTS `<ul>` (one "- " line per `<li>`), and every `<p>` after `<h2 id="full-conference-call-transcript">`. Dropped, in page order (identical list on both pages): the "Image source: The Motley Fool." div, the "Need a quote from a Motley Fool analyst?" line, a `div.my-8` spacer, the TAKEAWAYS heading and list, the SUMMARY heading, paragraph and list, a second `div.my-8` spacer, the INDUSTRY GLOSSARY heading and list, and the trailing `div.article-body-promobox`. No RISKS block was present on these pages. Whitespace collapsed; one blank line between paragraphs; a 3-line header (title, Source, Fetched/notes) prepended to each file.
- Speaker labels: Fool puts the speaker name in `<strong>` at the start of the first paragraph of each turn; kept as "Name: text". Continuation paragraphs of the same speaker carry no label (54 in Q1 2026, 51 in Q4 2025). Labels as they appear: Q1 2026 — "Michael Tierney", "K. Sridhar" (participants list says "K.R. Sridhar"), "Simon Edwards", "Operator", "Mark W. Strouse", "David Arcaro", "Christopher Dendrinos", "Nicholas Amicucci", "Manav Gupta", "Ben Kallo", "Colin Rusch", "Maheep Mandloi", "Vikram Bagri". Q4 2025 — "Michael Tierney", "KR Sridhar", "Maciej Kurzymski", "Desiree" (the operator), "David Arcaro", "Christopher Dendrinos", "Manav Gupta", "David Sandler", "Michael Blum", "Colin Rusch", "Mark Strouse", "Sherif Elmaghrabi", "Noel Parks".
- Verification, transcript-2026-Q1.txt: 202 lines, 8,266 words; first transcript line is IR's welcome to "Bloom Energy's First Quarter 2026 Earnings Call" (L14); "K. Sridhar:" appears as a label 15 times, "Simon Edwards:" once (his prepared remarks, L62), "Operator:" 10 times; 95 transcript paragraphs kept; the raised FY2026 guidance block is present at L54–L56 (CEO) and L76–L80 (CFO); the file ends with the operator's "You may now disconnect." (L202).
- Verification, transcript-2025-Q4.txt: 222 lines, 8,216 words; first transcript line is IR's welcome to the "fourth quarter and full year 2025 earnings call" (L14); "KR Sridhar:" appears 19 times, "Maciej Kurzymski:" once (L46), "Desiree:" 10 times; 105 transcript paragraphs kept; the initial FY2026 guidance block is present at L56–L58; the file ends with the operator's "You may now disconnect." (L222).
- Raw HTML and JSON from every fetch remain only in /tmp/be-orch/transcript/ (t1-*, t2-*, t3-*, t5-* files) and are not stored in the repo. No PDF or binary was downloaded by this gatherer.

## Quality caveats

- Both supplements are machine/edited third-party transcriptions with visible errors; notes-transcript.md §Q1-0 and §Q4-0 list them. Highlights: Q1 2026 L86 is labelled "K. Sridhar" but is evidently CFO Edwards answering; Q1 2026 L68 states revenue "up 13.4% year-over-year" and, in the next sentence, "greater than 100% year-over-year growth" (the Q1 2026 release says 130.4%); Q1 2026 L54 garbles the guidance raise into "$3.1 billion to $3.3 billion to $3.4 billion to $3.8 billion" (CFO L76 states it cleanly); Q4 2025 L56 gives the initial FY2026 non-GAAP operating-income guide as "$125 million to $475 million" (the Q4 2025 release, cached by the IR gatherer as press-release-2025-Q4.txt, says $425M–$475M; the transcript figure is a transcription error); Q4 2025 L20 places the CEO's first sentences inside the IR paragraph; Q4 2025 L172 ends mid-sentence. Names garbled: "Orca" (Oracle), "gloom"/"balloons"/"loan" (Bloom), "ultra cats" (ultracapacitors), "[indiscernible]" for the acting CFO's name (Q1 2026 L58).
- Numbers should be taken from the press releases, decks and filings; the transcripts are for wording only (§3 rule 2).
- Neither supplement mentions Brookfield, SK ecoplant, hydrogen, electrolyzers, tax credits, Equinix, CoreWeave or Conagra; the writer should not expect call wording on those topics from this gatherer.
- The Q1 2026 Date block gives no time of day; the company event feed gives 04/28/2026 17:00 (ET).
