# MANIFEST — META sources/2026-Q2

_Merged from the three gatherer manifests (filings, transcript, ir) on 2026-09-07. As-of quarter Q2 2026; cutoff 2026-07-30 (call 2026-07-29, 10-Q filed 2026-07-30). Transcript source tier: 1, company-published (Meta IR via Q4 Inc. CDN). Only extracted text is cached._

## filings.md

# MANIFEST — filings gatherer, Meta Platforms, Inc. (META, CIK 0001326801), Q2 2026

_As-of cutoff 2026-07-30 (10-Q filing date; earnings call 2026-07-29). All fetches performed 2026-09-07 from SEC EDGAR. Only extracted text is cached; no HTML or PDF saved in this folder._

Format: filename | origin URL | fetch date | word count | what it is

- 10-K-FY2025.txt | https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm | 2026-09-07 | 82456 words | Form 10-K for fiscal year ended 2025-12-31, filed 2026-01-29, accession 0001628280-26-003942
- 10-Q-2026-Q2.txt | https://www.sec.gov/Archives/edgar/data/1326801/000162828026050705/meta-20260630.htm | 2026-09-07 | 64128 words | Form 10-Q for quarter ended 2026-06-30, filed 2026-07-30, accession 0001628280-26-050705 (the as-of filing)
- 10-Q-2026-Q1.txt | https://www.sec.gov/Archives/edgar/data/1326801/000162828026028526/meta-20260331.htm | 2026-09-07 | 61420 words | Form 10-Q for quarter ended 2026-03-31, filed 2026-04-30, accession 0001628280-26-028526 (prior-quarter values for indicators)
- DEF14A-2026.txt | https://www.sec.gov/Archives/edgar/data/1326801/000162828026025532/meta-20260416.htm | 2026-09-07 | 48685 words | Definitive proxy statement (DEF 14A), filed 2026-04-16, accession 0001628280-26-025532; record date 2026-04-01
- 10-K-FY2023.txt | https://www.sec.gov/Archives/edgar/data/1326801/000132680124000012/meta-20231231.htm | 2026-09-07 | 78378 words | Form 10-K for fiscal year ended 2023-12-31, filed 2024-02-02, accession 0001326801-24-000012 (used for FY2021–FY2022 history)
- notes-filings.md | (written by filings gatherer from the five files above) | 2026-09-07 | 20309 words | structured bullet facts with source tags

## Fetch log

- User-Agent on every request: `company-research-skill owner@example.com`. Requests were sequential with a 1.2-second sleep between them. No requests were made to data.sec.gov (all five URLs were supplied by the orchestrator, so the submissions index was not needed).
- HTTP results (all first attempt, no retries needed):
  - 05:39:34 UTC 10-K-FY2025 → HTTP 200, 2,371,750 bytes
  - 05:39:35 UTC 10-Q-2026-Q2 → HTTP 200, 1,783,894 bytes
  - 05:39:37 UTC 10-Q-2026-Q1 → HTTP 200, 1,485,906 bytes
  - 05:39:38 UTC DEF14A-2026 → HTTP 200, 1,296,778 bytes
  - 05:39:40 UTC 10-K-FY2023 → HTTP 200, 2,465,661 bytes
- No 403/429 responses, no failures, no 404s (the fallback of listing the accession folder index was not needed).
- Completeness check: every downloaded HTML file contained exactly one closing `</html>` tag and exceeded 500 KB (range 1.3–2.5 MB; all five are inline XBRL).
- Conversion: Python 3 + BeautifulSoup 4.13.5 with the lxml 5.3.0 parser. Dropped `script`, `style`, `ix:header`, and any element with `display:none`; replaced each table with one line per row, cells joined by " | "; inserted line breaks at block elements; collapsed whitespace and runs of blank lines. (BeautifulSoup emitted an XMLParsedAsHTMLWarning because inline-XBRL documents carry an XML declaration; the HTML parser output was verified to be correct.)
- Verification after conversion: "Item 1. Business", "Item 1A. Risk Factors", "Item 7. Management's Discussion..." and "Item 8." headings survive in both 10-Ks; "Item 2. Management's Discussion..." survives in both 10-Qs (line 907 in the Q2 file, line 839 in the Q1 file); segment tables ("Family of Apps | Reality Labs | Total") and the income statement, balance sheet, and cash flow tables are readable line by line in all four financial filings. Charts (DAP by region, ARPP, ad impressions and price by region) are images in the source and did not survive; only their data rows (ARPP) and the surrounding sentences did.
- Raw HTML was written to /tmp/meta-fetch/ and deleted after conversion; nothing other than extracted text is stored in this folder.
- As-of discipline: nothing dated after 2026-07-30 was fetched or read. The latest-dated document is the Q2 2026 10-Q filed 2026-07-30. No 8-Ks, press releases, or transcripts were fetched by this gatherer (see the transcript and IR gatherers' manifests).
- Not fetched (outside the fetch list): the FY2024 10-K and FY2022 10-K. Consequences recorded in notes-filings.md section 13: headcount at 12/31/2021, 12/31/2022, 12/31/2024 is available only as year-over-year percentages; FY2021 ad-impression and price growth, Class A/B split at 12/31/2021, and marketable securities at 12/31/2021 are not in the fetched sources.
- Transcript source tier: not applicable to this gatherer.

## transcript.md

# MANIFEST-transcript — Meta Platforms (META) — Q2 2026 — transcript gatherer

As-of cutoff: 2026-07-30 (10-Q filing date). Call date: 2026-07-29 (main earnings call and same-day follow-up Q&A call). Gatherer run: 2026-09-07.

| file | origin URL | fetch date | source tier | word count |
|---|---|---|---|---|
| transcript.txt | https://s21.q4cdn.com/399680738/files/doc_financials/2026/q2/META-Q2-2026-Earnings-Call-Transcript.pdf | 2026-09-07 | 1 company-published (Meta IR, Q4 Inc. CDN) | 10365 |
| transcript-followup.txt | https://s21.q4cdn.com/399680738/files/doc_financials/2026/q2/META-Q2-2026-Follow-Up-Call-Transcript.pdf | 2026-09-07 | 1 company-published (Meta IR, Q4 Inc. CDN) | 4827 |
| notes-transcript.md | derived from the two files above (this gatherer) | 2026-09-07 | n/a | see file |

Word counts are `wc -w` on the cached text files.

## Fetch and conversion notes

- Both PDFs were listed by Meta's own IR event feed (`https://investor.atmeta.com/feed/Event.svc/GetEventList?...&year=2026...`, "Q2 2026 Earnings Call", 07/29/2026). The IR HTML pages return HTTP 403 (Cloudflare); the JSON feed and the s21.q4cdn.com files are open. No tier 2 (8-K exhibit) or tier 3 (Motley Fool) source was needed or used.
- Fetched with `curl -sS -L -A "company-research-skill owner@example.com"`. Main call: HTTP 200, `application/pdf`, 214,956 bytes, PDF 1.7, 21 pages, metadata title "META Q2 2026 Earnings Call Transcript", created 2026-07-30 01:49 UTC. Follow-up call: HTTP 200, `application/pdf`, 79,256 bytes, PDF 1.7, 11 pages, metadata title "META Q2 2026 Follow Up Call Transcript", created 2026-07-30 02:47 UTC. Both documents are dated "July 29th, 2026" in their text and titled "Second Quarter 2026 Results Conference Call" / "Second Quarter 2026 Results Follow Up Call".
- Converted with `pdftotext -layout`. PDFs were downloaded to /tmp only and deleted after conversion; no PDF or HTML was saved in the repo. Form-feed page breaks are preserved in the cached text.
- **Printed page numbers:** both PDFs have printed page numbers at the foot of every page (main 1–21, follow-up 1–11), and they equal the PDF page numbers. Page references in `notes-transcript.md` are these printed page numbers.
- **Post-processing (the only change to the extracted text):** three U+2010 (Unicode hyphen) characters in the main call's safe-harbor paragraph ("forward‐looking", "non‐GAAP" twice, p.1) were replaced with the ASCII hyphen "-" so that text searches match the rest of the file. Meaning unchanged. No other edits. Checked for and found none of: split first letters, zero-width spaces (U+200B/U+FEFF), or ligature code points (U+FB00–FB04). Curly quotes and apostrophes are left as the PDF has them (the CEO's prepared remarks use straight apostrophes; the CFO's remarks and the Q&A use curly ones).
- **Transcript quality notes:** the main call transcript carries one editorial footnote (p.21): Susan Li's phrase "supply constrained" is marked “Reflects correction of reference to "demand" during the earnings call.”, so the spoken audio said "demand" and the company's corrected text says "supply". The follow-up transcript has two "[Indiscernible]" markers (p.4, in Michael Nathanson's question; p.7, at the start of Susan Li's answer to Rob Sanderson). No numbers are affected by either.
- **Structure verified:** the main call opens with the host's introduction (Chad Heaton, VP Finance: "Thank you. Good afternoon and welcome to Meta Platforms' second quarter 2026 earnings conference call."), followed by prepared remarks from Mark Zuckerberg (p.1–4) and Susan Li (p.4–9), then a Q&A section opened by the operator (p.9–21) with 7 analysts asking 12 distinct questions: Morgan Stanley, Goldman Sachs, Bernstein, JP Morgan, Bank of America, Barclays, Wells Fargo. The follow-up call opens with the operator ("Good afternoon. My name is Krista...") and the host, then is entirely Q&A with Susan Li (p.1–11); 10 analysts asked 18 distinct questions: Citigroup, Truist Securities, Evercore, MoffettNathanson, Deutsche Bank, Wolfe Research, Loop Capital Markets, Cantor Fitzgerald, Rosenblatt, Piper Sandler. An eleventh (Cleveland Research) was called on but no question came through.
- **As-of discipline:** nothing published after 2026-07-30 was fetched or consulted. In particular, the 08/26/2026 "Update on Agreement with Bipartisan Attorneys General" event in the same IR feed and the Motley Fool transcript page dated 2026-08-07 were NOT fetched.
- Fetch failures: none.

## ir.md

# MANIFEST-ir — Meta Platforms, Inc. (META, CIK 1326801) Q2 2026 — IR gatherer (press release + slides + prior-quarter release)

As-of quarter Q2 2026 (quarter ended June 30, 2026); as-of cutoff 2026-07-30 (earnings release and call 2026-07-29; 10-Q filed 2026-07-30). Gatherer run 2026-09-07, behaving as though the date were 2026-07-30.

Discovery: Meta's IR HTML pages return HTTP 403 (Cloudflare), so documents were taken from the open Q4 Inc. JSON feed `https://investor.atmeta.com/feed/FinancialReport.svc/GetFinancialReportList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1&reportSubType=`, which lists the s21.q4cdn.com PDFs below. All three fetches returned HTTP 200 `application/pdf` on the first attempt (166,342 / 239,882 / 154,270 bytes). User-Agent on every request: `company-research-skill owner@example.com`. The SEC 8-K exhibit fallback (accession 0001628280-26-050596) was not needed and was not fetched.

PDFs were downloaded to /tmp only, converted with `pdftotext -layout`, checked page by page, and deleted (`rm` confirmed; /tmp/meta-ir is empty). No PDF or HTML file was saved in the repository. Only the three extracted-text files below plus `notes-ir.md` and this manifest were written by this gatherer.

## Files

filename | origin URL | fetch date | word count | note on text quality
---|---|---|---|---
press-release.txt | https://s21.q4cdn.com/399680738/files/doc_financials/2026/q2/Meta-06-30-2026-Exhibit-99-1-FINAL.pdf | 2026-09-07 | 2,775 | Q2 2026 earnings release (Exhibit 99.1), datelined "MENLO PARK, Calif. – July 29, 2026". pdfinfo: 9 pages, letter, Creator Workiva, title "Meta-06.30.2026 - Exhibit 99.1", CreationDate 2026-07-29 17:51:12 UTC. All 9 pages yielded text (445 / 206 / 197 / 775 / 181 / 172 / 473 / 149 / 177 words). p.1 headline table + operational highlights + CEO quote; p.2 CFO Outlook Commentary; p.3 webcast/disclosure/about/contacts; p.4 forward-looking statements + non-GAAP definitions; p.5 income statement (three and six months); p.6 balance sheet; p.7 cash flow statement + restricted-cash reconciliation + cash taxes paid; p.8 segment results; p.9 GAAP-to-non-GAAP reconciliation (constant currency, FCF). Tables kept column alignment; all figures legible. One layout artefact: on p.7 the printed page number "7" was pulled into the line "Cash paid for income taxes, net   7   $ 1,458 ..." — the "7" is the page number, not a value. Curly quotes and en dashes came through as UTF-8. Printed page numbers = PDF page numbers.
slides.txt | https://s21.q4cdn.com/399680738/files/doc_financials/2026/q2/Earnings-Presentation-Q2-2026.pdf | 2026-09-07 | 3,284 | Q2 2026 earnings presentation. pdfinfo: 18 pages, 1908 x 1080 pt, Creator Workiva, title "Earnings Presentation - Q2 2026", CreationDate 2026-07-24 01:00:08 UTC. Every page yielded text (6 / 123 / 122 / 208 / 64 / 194 / 141 / 141 / 34 / 298 / 57 / 93 / 96 / 1 / 185 / 654 / 861 / 6 words); the near-empty pages are the covers (p.1, p.18) and the "Appendix" divider (p.14). Tables on p.4 (segment results), p.6 (effective tax rate) and p.15 (FCF reconciliation) extracted in column order for nine quarters Q2'24–Q2'26. Chart pages p.2, p.3 (revenue by user geography, stacked), p.5 (expenses % of revenue, stacked), p.7 (net income), p.8 (diluted EPS), p.10 (DAP), p.11 (ARPP), p.12 (ad impressions YoY by geography, 5 panels x 5 quarters), p.13 (price per ad YoY by geography): every data label extracted, but in scrambled visual order. notes-ir.md re-associates each label to its quarter by text column; checks: all 18 stacked bars on p.2/p.3 sum exactly to their printed totals; all nine ARPP values reproduce from the slide's own definition; p.12/p.13 worldwide values match the release bullets; p.5 percentages match the release income statements for the four quarters that can be checked. Residual uncertainty only on p.5 (G&A vs Marketing & Sales split for the five quarters not covered by a cached release; assignment by stack order). Quarter labels use curly apostrophes on table pages (Q2’26) and straight ones on chart pages (Q2'26). p.9 capex slide has only four bars (Q2'25, Q2'26, YTD 2025, YTD 2026). p.16–17 dense prose (metric limitations) extracted cleanly. No guidance slide, no headcount, cash/debt or share-count slide. Printed page numbers (2–17) = PDF page numbers.
press-release-2026-Q1.txt | https://s21.q4cdn.com/399680738/files/doc_financials/2026/q1/Meta-03-31-2026-Exhibit-99-1_final.pdf | 2026-09-07 | 2,591 | Q1 2026 earnings release (Exhibit 99.1), datelined "April 29, 2026" (before the cutoff; fetched so the writer has prior-quarter KPI values and the guidance given last quarter). pdfinfo: 9 pages, letter, Creator Workiva, title "Meta-03.31.2026 - Exhibit 99.1", CreationDate 2026-04-29 18:20:32 UTC. All 9 pages yielded text (501 / 204 / 196 / 777 / 116 / 172 / 372 / 118 / 135 words). Same nine-page layout as the Q2 release (three-month columns only, no six-month columns). Clean tables, no page-number merge artefact, no garbling.
notes-ir.md | derived from the three files above (this gatherer) | 2026-09-07 | 8,591 (wc -w) | Bullet facts only, every number verbatim with unit and period, tagged [Q2 2026 release, p.N], [Q2 2026 slides, p.N], [Q1 2026 release, p.N] with PDF page numbers (= printed page numbers). Sections: 1 headline results; 2 KPIs; 3 segments and geography; 4 cash/debt/capex/FCF/capital return and full statements; 5 CFO Outlook Commentary verbatim from both releases plus guided-vs-reported facts side by side; 6 prior-quarter values from the Q1 2026 release and a Q1→Q2 arrow list; 7 slides page by page with nine-quarter series; 8 non-GAAP and metric definitions verbatim; 9 not-disclosed list; 10 automated check. Automated check: 720 unique numeric tokens, 718 found verbatim in the cached texts; exceptions "99.1" (exhibit number from PDF metadata title) and "38.8%" (the single labelled computed item).

## Confirmations

- Nothing published after 2026-07-30 was fetched, opened, or read. PDF creation dates: 2026-07-29 (Q2 release), 2026-07-24 (Q2 slides), 2026-04-29 (Q1 release) — all on or before the cutoff. The Q2 release text itself states "the date of this press release is July 29, 2026".
- Not fetched, by instruction: the Excel financial tables, the webcast link, the cloudfront 10-Q PDF (the filings gatherer covers the 10-Q from SEC), and anything relating to Q3 2026. No SEC request was made by this gatherer.
- PDFs discarded after conversion; no binary saved in the repo.
- Files in this folder not produced or read by this gatherer: `10-K-FY2023.txt`, `10-K-FY2025.txt`, `10-Q-2026-Q1.txt`, `10-Q-2026-Q2.txt`, `DEF14A-2026.txt`, `transcript.txt`, `transcript-followup.txt`, `notes-filings.md`, `notes-transcript.md`, `MANIFEST-filings.md`, `MANIFEST-transcript.md` (filings and transcript gatherers). notes-ir.md relies solely on the three IR texts above.
- No git command was run by this gatherer.

