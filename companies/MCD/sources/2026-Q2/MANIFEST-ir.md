# MANIFEST-ir — McDonald's Corporation (MCD, CIK 0000063908) Q2 2026 — IR gatherer (earnings release EX-99.1, supplemental information EX-99.2, prior-quarter release and supplement, leadership release)

As-of cutoff 2026-08-07 (10-Q filed 2026-08-07; earnings release and call 2026-08-04). Every document below is dated on or before 2026-08-04: the Q2 2026 release masthead reads "8/4/2026" and its 8-K (accession 0000063908-26-000067) was accepted by EDGAR 2026-08-04 07:01:40; the leadership release is datelined "CHICAGO, August 4, 2026" and its 8-K (accession 0000063908-26-000069, period of report 2026-08-03) was accepted 2026-08-04 07:44:19; the Q1 2026 release masthead reads "5/7/2026" and its 8-K (accession 0000063908-26-000048) was accepted 2026-05-07 07:01:19. Nothing published after 2026-08-07 was fetched, read or used. HTML was downloaded to /tmp/mcd-orch/ir/ and deleted after conversion; only extracted text is cached here. Conversion: Python (BeautifulSoup + lxml), script /tmp/mcd-orch/ir/html2txt.py — script/style/head and display:none elements dropped, table cells joined with " | ", one table row per line, non-breaking spaces normalised. User-Agent on every www.sec.gov request: `company-research-skill owner@example.com`; requests spaced at least 2 s apart. No 403 or 429 was received.

## Files

filename | origin URL | fetch date | document date | word count | note on text quality
---|---|---|---|---|---
press-release.txt | https://www.sec.gov/Archives/edgar/data/63908/000006390826000067/exhibit991-6302026.htm (8-K EX-99.1) | 2026-09-08 (fetched by the interrupted earlier run the same day; **reused** after verification, see below) | 2026-08-04 (masthead "8/4/2026"; "McDONALD'S REPORTS SECOND QUARTER 2026 RESULTS") | 2323 | Complete and clean: printed pages 1–6 all present (p.1 headline bullets, CEO quote, financial-performance bullets; p.2 comparable sales table and key financial metrics for quarter and six months; p.3 net income / EPS GAAP-to-non-GAAP reconciliation; p.4 definitions, webcast, forward-looking statements; p.5 quarter income statement; p.6 six-month income statement). Every table row extracted with column order preserved; "$" and "%" signs occupy their own cells. Source typo "quarter.While" kept. No images with data.
press-release-supplement.txt | https://www.sec.gov/Archives/edgar/data/63908/000006390826000067/exhibit992-6302026.htm (8-K EX-99.2) | 2026-09-08 (earlier run; **reused** after verification) | 2026-08-04 (Supplemental Information (Unaudited), Quarter and Six Months Ended June 30, 2026) | 11560 | Complete: all 16 sections of its own contents list are present in order (FX impact p.1–2, net income and EPS p.2–3, revenues p.4–5, comparable sales p.5, Systemwide and franchised sales p.6, restaurant margins p.7, SG&A and other operating p.8, operating income p.9, interest / nonoperating / income taxes p.10, Outlook p.11, restaurant information p.12–13, cautionary statement and risk factors p.14–21) and the text ends at printed page 21 with the last risk factor paragraph. One flattening artifact: the two-row header of the Restaurant Margins tables prints "Inc/ (Dec) Excluding Currency Translation" on the line above the period header; column order is intact. Cells that are blank in the source (growth-rate cells on "(Gains)/Charges" rows) are dropped. Source typo "approximately95%" kept.
press-release-2026-Q1.txt | https://www.sec.gov/Archives/edgar/data/63908/000006390826000048/exhibit991-33126xq1.htm (8-K EX-99.1) | 2026-09-08 (earlier run; **reused** after verification) | 2026-05-07 (masthead "5/7/2026"; "McDONALD'S REPORTS FIRST QUARTER 2026 RESULTS") | 1720 | Complete, printed pages 1–4 (p.1 headline bullets and CEO quote; p.2 comparable sales, key metrics, reconciliation; p.3 definitions and boilerplate; p.4 income statement). Same structure and quality as the Q2 release. Used for the prior-quarter comparison column and for what management had said to expect.
press-release-supplement-2026-Q1.txt | https://www.sec.gov/Archives/edgar/data/63908/000006390826000048/exhibit992-33126xq1.htm (8-K EX-99.2) | 2026-09-08 (earlier run; **reused** after verification) | 2026-05-07 (Supplemental Information (Unaudited), Quarter Ended March 31, 2026) | 10157 | Complete, printed pages 1–18, all 16 contents-list sections present through Risk Factors. Same quality as the Q2 supplement. Used for Q1 segment revenues, Systemwide and franchised sales, margins, operating income, tax rate, capital return, Outlook (p.8) and restaurant counts at 2026-03-31.
press-release-2026-08-03-leadership.txt | https://www.sec.gov/Archives/edgar/data/63908/000006390826000069/exhibitpressrelease.htm (8-K EX-99.1; exhibit name verified on the filing index) | 2026-09-08 (**fetched this run**, HTTP 200, 10,780 bytes) | 2026-08-04 (dateline "CHICAGO, August 4, 2026"; 8-K period of report 2026-08-03) | 762 | Complete two-page release, "McDonald's Appoints Skye Anderson as President of McDonald's USA"; prose only, no tables, no page numbers (the page-2 header "Exhibit 99.1" appears mid-text). Source typo "intranslating" kept. The 8-K body itself is cached by the filings gatherer as 8-K-2026-08-04-officer.txt and was not rewritten.
notes-ir.md | derived from the five files above | 2026-09-08 | — | 12012 | Structured bullets and small tables, every number verbatim with unit and period, tagged [Q2 2026 release, p.N], [Q2 2026 supplement, <section> p.N], [Q1 2026 release, p.N], [Q1 2026 supplement, <section> p.N] or [8-K 2026-08-03 leadership release]; gatherer-derived values labelled "(computed)". Numeric check below.

## Reuse verification of the four cached texts

The earlier interrupted run (same day) had left the four EDGAR HTML exhibits in /tmp/mcd-orch/ir/ (ex991_q2.htm 176,954 bytes; ex992_q2.htm 498,351 bytes; ex991_q1.htm 106,372 bytes; ex992_q1.htm 366,928 bytes). Each byte count equals the document size listed on the corresponding EDGAR filing index fetched this run, and each file ends with the closing `</html></TEXT></DOCUMENT>` markers, so the downloads were complete. Re-running html2txt.py on each produced text byte-identical (`cmp`) to the four cached .txt files. Content check: the Q2 release reads as prose from the headline bullets through the CEO quote, comparable-sales bullets, key financial metrics table, reconciliation, definitions, forward-looking statements and both income statements to printed page 6; the Q2 supplement contains every section in its contents list through Risk Factors, ending at printed page 21 (the Q1 supplement likewise ends at printed page 18). All four were therefore reused, not refetched.

## Fetch log (this run, 2026-09-08, all with UA `company-research-skill owner@example.com`)

- 2026-09-08T20:59:27Z GET https://www.sec.gov/Archives/edgar/data/63908/000006390826000067/0000063908-26-000067-index.htm -> HTTP 200, 10910 bytes
- 2026-09-08T20:59:29Z GET https://www.sec.gov/Archives/edgar/data/63908/000006390826000048/0000063908-26-000048-index.htm -> HTTP 200, 10913 bytes
- 2026-09-08T20:59:32Z GET https://www.sec.gov/Archives/edgar/data/63908/000006390826000069/0000063908-26-000069-index.htm -> HTTP 200, 10378 bytes
- 2026-09-08T21:00:55Z GET https://www.sec.gov/Archives/edgar/data/63908/000006390826000069/exhibitpressrelease.htm -> HTTP 200, 10780 bytes

Four SEC requests in total; all HTTP 200; no 403/429; no back-off needed. The earlier run's fetches of the four exhibits (URLs in the table above) were also from www.sec.gov on 2026-09-08. No data.sec.gov request was needed (accession numbers were supplied by the orchestrator and confirmed on the filing indexes).

Exhibit lists read from the indexes: Q2 2026 earnings 8-K (0000063908-26-000067, Items 2.02 and 9.01): mcd-20260804.htm (8-K), exhibit991-6302026.htm (EX-99.1), exhibit992-6302026.htm (EX-99.2), archyellowlogoa07.jpg (GRAPHIC), form8k06302026.pdf (PDF copy of the 8-K), XBRL files. Q1 2026 earnings 8-K (0000063908-26-000048, Items 2.02 and 9.01): mcd-20260507.htm, exhibit991-33126xq1.htm, exhibit992-33126xq1.htm, archyellowlogoa07.jpg, form8k03312026.pdf, XBRL files. Leadership 8-K (0000063908-26-000069, Items 5.02, 7.01 and 9.01): mcd-20260803.htm, exhibitpressrelease.htm (EX-99.1), pdfof8-k.pdf, XBRL files. No presentation, slide or prepared-remarks exhibit in any of the three.

## IR-site attempts (verbatim results)

    2026-09-08T20:59:37Z GET https://corporate.mcdonalds.com/corpmcd/investors/financial-information.html (curl -sS -L --http1.1 --max-time 30, Chrome UA)
      result: exit 28; curl: (28) Operation timed out after 30002 milliseconds with 0 bytes received
    HTTP 000, 0 bytes, 30.002761s, final URL https://corporate.mcdonalds.com/corpmcd/investors/financial-information.html
    2026-09-08T21:00:07Z GET https://corporate.mcdonalds.com/corpmcd/investors/events-and-presentations.html (curl -sS -L --http1.1 --max-time 30, Chrome UA)
      result: exit 28; curl: (28) Operation timed out after 30002 milliseconds with 0 bytes received
    HTTP 000, 0 bytes, 30.002303s, final URL https://corporate.mcdonalds.com/corpmcd/investors/events-and-presentations.html

Both attempts (HTTP/1.1, Chrome-like User-Agent, 30 s limit) timed out with 0 bytes received, matching the orchestrator's 2026-09-08 probe (HTTP/2 stream INTERNAL_ERROR from the Akamai edge; HTTP/1.1 timeout). Total time spent on the IR site: about 60 s. No further attempts were made.

## Slides finding

No slides found: IR site unreachable, 8-K carries only EX-99.1 and EX-99.2. McDonald's earnings materials for Q2 2026 consist of the release (Exhibit 99.1) and the Supplemental Information (Exhibit 99.2); the Q1 2026 8-K has the same two exhibits. No slides.txt was created.

## As-of discipline

Only documents dated on or before 2026-08-04 (release, supplement, leadership release) and 2026-05-07 (Q1 release and supplement) were read. The 8-K filing indexes fetched this run are metadata pages for those same filings. No later 8-K, no post-cutoff IR page and no third-party source was consulted. The Q2 2026 call transcript is the transcript gatherer's file and was not read by this gatherer.

## Numeric check (run 2026-09-08)

Method: every numeric token in notes-ir.md (regex `\d[\d,]*(\.\d+)?`, after removing structural tokens — ISO dates, EDGAR timestamps, accession numbers, CIK, page references "p.N"/"pp.N–N", section references "§N", form names 8-K/10-Q/10-K/EX-99.N, quarter labels Q1–Q4 and years 2022–2026, "6M", markdown heading numbers) was searched verbatim in the concatenation of the five cached texts.
- Lines not labelled "computed": 1,395 tokens checked, 1,395 found, 0 misses.
- Lines labelled "computed" (29 lines): 276 tokens checked, 215 found, 61 not found; all 61 are the gatherer's derived values (margin percentages such as 84.5 / 15.3 / 11.6, quarter operating margins 47.0 / 47.2 / 47.8 / 47.9, Systemwide-sales dollar sums 36,976 / 35,218 / 71,210 / 66,154 / 34,234 / 30,936, the SG&A sum 701, the buyback sums 4.3 / 1,251, the tax-rate check 19.6, the D&A sums 565 / 531, the franchised-share ratios 90.6 / 92.1 / 95.6, and the net-additions-by-type figure 161).
- Zero unlabelled misses.

## Files in this folder NOT produced by the ir gatherer (owned by other gatherers; not read or modified except the two lines of 8-K-2026-08-04-officer.txt quoted in notes-ir.md §11 for the notice and effective dates)

- 10-K-FY2022.txt
- 10-K-FY2023.txt
- 10-K-FY2024.txt
- 10-K-FY2025.txt
- 10-Q-2026-Q2.txt
- 8-K-2025-01-17.txt
- 8-K-2025-02-14.txt
- 8-K-2025-03-04.txt
- 8-K-2025-03-11.txt
- 8-K-2025-05-23.txt
- 8-K-2025-08-27.txt
- 8-K-2026-02-10.txt
- 8-K-2026-05-22.txt
- 8-K-2026-08-04-officer.txt
- 8-K-A-2026-04-02.txt
- DEF14A-2026.txt
- transcript.txt
