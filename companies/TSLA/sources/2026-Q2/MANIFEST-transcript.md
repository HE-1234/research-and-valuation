# MANIFEST — transcript gatherer — Tesla, Inc. (TSLA, Nasdaq, CIK 0001318605) — Q2 2026

As-of cutoff: 2026-07-23 (10-Q filing date). Call date: 2026-07-22, 4:30 p.m. CT / 5:30 p.m. ET ("Second Quarter 2026 Q&A Webcast"). Gatherer run: 2026-09-08.

| file | origin URL | fetch date | source tier | word count |
|---|---|---|---|---|
| transcript.txt | https://www.fool.com/earnings/call-transcripts/2026/08/05/tesla-tsla-q2-2026-earnings-call-transcript/ | 2026-09-08 | 3, third-party free (The Motley Fool machine transcript) | 9,068 (8,942 words of call text from l.15 on, plus 126 words of header and participant list, l.1–13) |
| notes-transcript.md | derived from transcript.txt by this gatherer; §8c cross-checked against `slides.txt` and `slides-2026-Q1.txt` cached by the ir gatherer | 2026-09-08 | n/a | 10281 |

Word counts are `wc -w` on the files.

## Tier walk (AGENTS.md §12.2, in order)

### Tier 1, company-published transcript (Tesla IR, ir.tesla.com): UNREACHABLE (HTTP 403 on every path)

Eight requests in total, about 1 s apart, all on 2026-09-08 at about 23:42–23:44 UTC. Browser UA = `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36`; standard UA = `company-research-skill owner@example.com`. All with `-sS -L --max-time 30 -H "Accept: text/html"`.

| # | method | URL | UA | result |
|---|---|---|---|---|
| 1 | GET | https://ir.tesla.com/ | browser | 403, 366 bytes, 0.13 s |
| 2 | GET | https://ir.tesla.com/press-release/tesla-second-quarter-2026-financial-results (guessed slug) | browser | 403, 451 bytes, 0.07 s |
| 3 | GET | https://ir.tesla.com/press-releases | browser | 403, 384 bytes, 0.05 s |
| 4 | GET | https://ir.tesla.com/events-and-presentations | browser | 403, 398 bytes, 0.06 s |
| 5 | HEAD | https://ir.tesla.com/ | browser | 403; `Server: AkamaiGHost`; `X-Reference-Error: 18.ac72cd17.1788911016.75ac980`; Content-Length 364 |
| 6 | GET | https://ir.tesla.com/ | standard | 403, 364 bytes, 0.10 s |
| 7 | GET | https://ir.tesla.com/press-release/tesla-second-quarter-2026-financial-results | standard | 403, 449 bytes, 0.05 s |
| 8 | GET | https://ir.tesla.com/events-and-presentations | browser, `--http1.1`, `Accept-Language: en-US,en;q=0.9` | 403, 396 bytes, 0.06 s |

The block is at the Akamai edge and does not depend on UA or HTTP version. `ir.tesla.com` is not a Q4 Inc. host, so the §12.3 feed fallback does not apply and was not tried. No IR page loaded, so whether Tesla posted a transcript of this call could not be confirmed from this host; historically Tesla posts a webcast replay and no transcript, and the Update deck itself says only that the webcast "will also be available for replay for approximately one year thereafter" at ir.tesla.com [Q2 2026 slides, p.32]. Tier 1 is recorded as not obtainable, not as non-existent.

### Tier 2, 8-K exhibits: NO TRANSCRIPT OR PREPARED REMARKS

Two GET requests to https://www.sec.gov/Archives/edgar/data/1318605/000162828026049213/0001628280-26-049213-index.htm with the standard UA (one at 23:42 UTC to list the exhibits; one at 23:58 UTC, after a 2 s sleep, to re-read the primary document's name after the first copy had been deleted). Both HTTP 200, 20,432 bytes, 0.33 s and 0.46 s; no 403 or 429, so no back-off was needed.

Form 8-K, filed 2026-07-22, accepted 2026-07-22 16:35:52, period of report 2026-07-22, Items 2.02 (Results of Operations and Financial Condition) and 9.01 (Financial Statements and Exhibits). The index header counts 45 documents; the document table lists 39: sequence 1 `tsla-20260722.htm` (8-K, iXBRL, 27,495 bytes); sequence 2 `exhibit991.htm` EX-99.1 (52,312 bytes; the Q2 2026 Update deck, owned by the ir gatherer as `slides.txt`); sequences 3–5 XBRL schema, label and presentation files (`tsla-20260722.xsd`, `_lab.xml`, `_pre.xml`); sequences 6–38 thirty-three GRAPHIC files `exhibit991001.jpg` … `exhibit991033.jpg` (the deck's images); and the complete submission text file; the remaining entries are XBRL-derived data files. No exhibit is a transcript or prepared remarks. No exhibit was downloaded by this gatherer.

### Tier 3, The Motley Fool: USED

- **robots.txt:** https://www.fool.com/robots.txt, browser UA, HTTP 200, 2,311 bytes. Three user-agent blocks: `MauiBot` and `Bytespider` each carry the bare `Disallow: /`; the `User-agent: *` block carries 83 `Disallow` prefixes (for example `/a/`, `/account/`, `/investing/stocks/`, `/premium-reports`, `/quote/failed-lookup/`) and none matches `/earnings/call-transcripts/2026/08/05/tesla-tsla-q2-2026-earnings-call-transcript/`. Path allowed for a generic agent.
- **Discovery:** https://www.fool.com/quote/nasdaq/tsla/ (browser UA, HTTP 200, 758,603 bytes) contains 16 occurrences of `call-transcripts` inside embedded JSON, resolving to 8 distinct Tesla transcript URLs from Q2 2024 to Q2 2026, including the Q2 2026 one above. One of the eight is oddly slugged (`/2026/04/22/tesla-tsla-q3-2024-earnings-call-transcript/`, presumably the Q1 2026 call); it was not fetched. Monthly sitemaps: https://www.fool.com/sitemap/2026/07 (HTTP 200, 707,910 bytes, 4,515 `<loc>` entries, 0 Tesla transcripts) and https://www.fool.com/sitemap/2026/08 (HTTP 200, 995,365 bytes, 6,121 entries, exactly 1 Tesla transcript: the Q2 2026 URL). So Fool carried the call, but posted it in August.
- **Fetch:** HTTP 200, 511,830 bytes, 0.40 s, browser UA. Page title "Tesla (TSLA) Q2 2026 Earnings Call Transcript | The Motley Fool". JSON-LD `datePublished` and `dateModified` both `2026-08-05T14:54:12.000Z`. The page's DATE section reads "Wednesday, July 22, 2026 at 5:30 p.m. ET", which equals the deck's 4:30 p.m. CT.
- **Call date vs posting date:** call 2026-07-22; posted 2026-08-05, fourteen days after the call and thirteen days after the 2026-07-23 cutoff. Admitted under §12.2 because the call is pre-cutoff and only call content is used. Both dates are recorded here, in l.2 of `transcript.txt`, and in the header of `notes-transcript.md`.
- **Conversion:** `/tmp/tsla-orch/transcript/convert_fool.py` (BeautifulSoup 4.13.5 with lxml) on the container `div.article-body.transcript-content`. Kept, in order: the DATE paragraph (folded into the header), the CALL PARTICIPANTS list (7 entries), and every `<p>` under the "Full Conference Call Transcript" heading (111 paragraphs). Dropped: the "Image source" block, TAKEAWAYS, RISKS, SUMMARY, INDUSTRY GLOSSARY, the two in-body promotional `div`s, Read Next, Stocks Mentioned, Stock Advisor and Premium Investing Services blocks, and everything outside the container. Speaker labels are kept inline exactly as Fool renders them ("Travis Axelrod: …"), with the `<strong>` wrapper removed; one blank line between paragraphs; a 13-line header added (source URL, dates, tier, citation rule, participant list). Fool's editorial blocks were only glimpsed as 140-character previews while mapping the page structure; nothing from them was read for or used in the notes. HTML entities unescaped; no other alteration.
- **Hygiene of the cached text:** 235 lines (234 plus a trailing newline); 0 non-ASCII characters; 0 "(sic)" strings; 0 bracketed insertions; 0 double-quote characters (so every quotation in the notes is unambiguous). Speaker turns: Travis Axelrod 17, Elon Musk 16, Vaibhav Taneja 5, Ashok Elluswamy 3, Lars Moravy 3, William Stein 3, Andrew Percoco 3, Walter Piecyk 2, Dan Levy 2, Colin Langan 2, Karn Budhiraj 1, Brandon Ehrhart 1, Alexander Perry 1.
- **Structure:** l.1–2 source and dates; l.4–11 participants; l.13 section marker; l.15–17 Axelrod opening; l.19–51 Musk prepared remarks; l.53 Axelrod; l.55–73 Taneja prepared remarks; l.75 Axelrod (say.com questions already covered); l.77–87 Elluswamy on robotaxi (say.com block); l.89 Axelrod; l.91–97 Elluswamy on Optimus training data (say.com block); l.99–231 analyst Q&A (seven analysts called: Tom of RBC never heard, then Andrew Percoco, Alexander Perry of Bank of America, Colin Langan of Wells Fargo, Walter Piecyk of LightShed, William Stein of Truist, Dan Levy of Barclays; eleven questions in all); l.233 Axelrod close; l.235 Musk sign-off.
- **Page numbers:** none exist. Citations use `l.N` (line in `transcript.txt`) plus speaker and section, e.g. `[Q2 2026 call, Taneja prepared remarks, l.69]`, `[Q2 2026 call, Q&A, Stein, l.191]`.

### Tiers 4 and 5: not applicable (no owner-supplied file; a transcript exists). The prior quarter's call (Q1 2026, 2026-04-22) was not fetched because the supplement rule in §12.2 applies only when the current call is unavailable; the "what management had said to expect" material in notes §7 comes from the Q2 call's own "as previously guided" references and from the cached Q1 2026 Update deck.

## Deck cross-check summary (notes §8c)

27 spoken figures or status claims were tested against the Q2 2026 Update deck (`slides.txt`, ir gatherer). 13 match numerically (record Q2 deliveries; ~55% North America FSD attach; ~1.5 million paid FSD customers = 1.48 million Active FSD Subscriptions; automotive gross margin ex credits 19.2% to 16.3%; 13.5 GWh storage, +53%; energy gross margin 39.5% to 20.4% and services margin 9.2% to 14.1%, both reproduced from the Statement of Operations; opex up mainly on R&D; $1 billion SpaceX gain = 1,005; ~$300 million FX loss = 312; ~$100 million Bitcoin loss = 112; negative FCF with capex 2.3x; seven robotaxi metros). 5 are consistent in words (Cybercab production began; Megapack 3 soon; lithium and cathode refineries in early ramp; Optimus production soon; fab equipment procurement). 2 are call-only guidance absent from the deck (FY2026 capex "more than $25 billion"; debt facilities "up to $30 billion"). 6 cannot be checked against the deck (regional sequential growth 60%/27%/12%; 55/45 upfront/subscription split; the $230 million Q1 automotive benefit; the ~$240 million energy warranty true-up and the >$200 million Q1 energy tariff benefit as amounts; 380,000 unsupervised miles; 7 GW at superchargers). 1 is inconsistent: the CEO's "We have started production with the Tesla semi-truck" (l.23) against the deck's "Tesla Semi remains on track for production this year" and a "Commissioning" status (p.3, p.6); the writer should take Semi status from the deck.

Transcript garbles flagged for the writer (notes §8b): "appreciation" for depreciation (l.67), "amazing awareness" for Amazing Abundance (l.73), "writes it" / "rights" for rides (l.87, l.145), "braking battles" for pedals (l.159), "AI will initially go into Optimus" for AI5 (l.199), "March 9" for March of 9s (l.131), and four unclear fragments (l.31, l.165, l.209, l.225). Numbers in the notes are quoted for wording only; the writer takes figures from the deck or the 10-Q.

## Citation check

Script `/tmp/tsla-orch/transcript/check_quotes.py`, run 2026-09-08 on the final `notes-transcript.md`: every double-quoted string of 15 or more characters on a line carrying an `l.N` tag was tested, after whitespace normalisation and case-sensitively, as a substring of the cited transcript line(s) and of the whole transcript; strings on lines tagged `slides` were tested against `slides.txt` and `slides-2026-Q1.txt`. Final result: 266 transcript-tagged quotations, 266 verbatim (235 on the cited lines; 31 deck quotations on mixed lines, verified against the decks); 5 deck-tagged quotations, 5 verbatim; 0 mis-cited; 0 not found; 3 quoted strings on untagged lines outside the check (two header strings that appear at l.15 and one section label). The first run had found 3 mis-cites (analyst introductions cited to the question line rather than the introduction line) and 4 genuine wording slips (two of this gatherer's reconstructions placed in double quotes, one elided quotation, one case mismatch against the deck); all were corrected in the notes before the final run.

## As-of discipline

Nothing published after 2026-07-23 was used except the Motley Fool transcript page (posted 2026-08-05) of the 2026-07-22 call, from which only call content was taken. Other documents touched by this gatherer: the SEC filing index for the 2026-07-22 8-K; fool.com's robots.txt, the TSLA quote page and the 2026/07 and 2026/08 sitemaps (used only to locate the transcript URL; no other content read); the already-cached `slides.txt` (deck filed 2026-07-22) and `slides-2026-Q1.txt` (deck filed 2026-04-22). No 10-K, 10-Q, 8-K body, DEF 14A or press-release text was read by this gatherer. No information from any event after the call (Terafab announcements, later robotaxi launches, later deliveries reports) appears in the notes.

## Scratch and hygiene

Scratch kept under `/tmp/tsla-orch/transcript/` only: `convert_fool.py`, `check_quotes.py`, `fool_robots.txt`, `fool_sitemap_202607.xml`, `fool_sitemap_202608.xml` (all text). Downloaded HTML (`fool_q2_page.html`, `fool_quote.html`, `sec_8k_index.htm` twice, four `tier1_*.html` 403 bodies) was deleted after use. No HTML, PDF or other binary was cached in the repository. Python was run as `python3 -P` with cwd `/home/ubuntu`. No git command was run by this gatherer.

## Not produced by this gatherer

`slides.txt`, `slides-2026-Q1.txt`, `slides-2025-Q4.txt`, `press-release-deliveries.txt`, `press-release-deliveries-2026-Q1.txt`, `10-K-FY2023.txt`, `10-K-FY2025.txt`, `10-KA-FY2025.txt`, `10-Q-2026-Q1.txt`, `10-Q-2026-Q2.txt`, `DEF14A-2025.txt`, `8-K-2025-11-07-annual-meeting.txt`, `notes-filings.md`, `notes-ir.md`, `MANIFEST-filings.md`, `MANIFEST-ir.md`, and `MANIFEST.md` (merged by the orchestrator). This gatherer wrote only `transcript.txt`, `notes-transcript.md` and `MANIFEST-transcript.md`. No `transcript-2026-Q1.txt` was written (supplement rule not triggered).
