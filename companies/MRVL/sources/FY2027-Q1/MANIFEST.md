# MANIFEST — MRVL sources/FY2027-Q1

## filings.md

# MANIFEST — filings gatherer, MRVL, Q1 FY2027 (quarter ended 2026-05-02)

As-of cutoff: 2026-05-28 (10-Q filing date). All documents below were published on or before that date. Fetched 2026-09-07 from SEC EDGAR with User-Agent "company-research-skill owner@localhost.local", well under 10 requests/second. HTML was converted to text with Python 3 + BeautifulSoup (html.parser): hidden inline-XBRL header and display:none blocks dropped, table rows kept one per line with cells separated by " | ", whitespace collapsed, block-level line breaks preserved. Only extracted .txt files are stored here; no HTML or PDF binaries.

Format: filename | origin URL | fetch date | word count

10-K-FY2026.txt | https://www.sec.gov/Archives/edgar/data/1835632/000183563226000011/mrvl-20260131.htm | 2026-09-07 | 69571 words (Form 10-K for fiscal year ended 2026-01-31, filed 2026-03-11)
10-Q-FY2027-Q1.txt | https://www.sec.gov/Archives/edgar/data/1835632/000183563226000019/mrvl-20260502.htm | 2026-09-07 | 46056 words (Form 10-Q for quarter ended 2026-05-02, filed 2026-05-28)
DEF14A-2026.txt | https://www.sec.gov/Archives/edgar/data/1835632/000110465926060253/tm261486-1_def14a.htm | 2026-09-07 | 58407 words (proxy statement filed 2026-05-13; annual meeting 2026-06-25)
10-K-FY2024.txt | https://www.sec.gov/Archives/edgar/data/1835632/000183563224000009/mrvl-20240203.htm | 2026-09-07 | 66226 words (Form 10-K for fiscal year ended 2024-02-03, filed 2024-03-13; used for FY2022-FY2023 financials and the five-category end-market history)
notes-filings.md | (written by the filings gatherer from the four files above) | 2026-09-07 | 9409 words

## Fetch log

- The FY2024 10-K was located via https://data.sec.gov/submissions/CIK0001835632.json (filings.recent; accession 0001835632-24-000009, primary document mrvl-20240203.htm). The JSON index itself was not saved to the repo.
- First fetch attempt of all four www.sec.gov documents returned HTTP 403 ("Your Request Originates from an Undeclared Automated Tool") with User-Agent "company-research-skill contact: owner@localhost". Retried once with the SEC-documented "Name contact@domain" User-Agent form plus Accept-Encoding and Host headers; all four returned HTTP 200. No fetch failed after the retry.
- Not fetched (outside scope for this gatherer): earnings press release, slides, transcript (ir and transcript gatherers), and the FY2025 10-K (needed only for the FY2025 four-way split of the "communications and other" end market and FY2025 headcount; both are recorded as gaps in notes-filings.md).

## Verification

- Each .txt was checked to read as prose (first 50 lines) and to contain its MD&A heading: "Item 7. Management's Discussion and Analysis..." at line 1357 (10-K FY2026) and line 1223 (10-K FY2024); "Item 2. Management's Discussion and Analysis..." at line 1371 (10-Q).

## transcript.md

# MANIFEST — transcript gatherer — Marvell Technology (MRVL, CIK 0001835632) — Q1 FY2027

Quarter: Q1 FY2027 (fiscal quarter ended 2026-05-02). Earnings call: 2026-05-27. As-of cutoff: 2026-05-28.
Gatherer run date: 2026-09-07.

## Files

| File | Origin URL | Fetch date | Source tier | Word count |
|---|---|---|---|---|
| transcript.txt | https://www.fool.com/earnings/call-transcripts/2026/05/27/marvell-mrvl-q1-2027-earnings-transcript/ | 2026-09-07 | 3 third-party (Motley Fool) | 9,765 |
| notes-transcript.md | derived from transcript.txt | 2026-09-07 | n/a | see file |

## Tier checks

- Tier 1 (company-published transcript): checked https://investor.marvell.com/financial-information/financial-results on 2026-09-07 (HTTP 200, 191,947 bytes). Zero occurrences of the string "transcript". Result: none available. Consistent with AGENTS.md §12.3.
- Tier 2 (8-K exhibit with prepared remarks/transcript): not fetched. Per task brief, the 2026-05-27 8-K (accession 0001835632-26-000014) contains only the press release; tier 1 check gave no reason to revisit. Result: none.
- Tier 3 (third-party free, Motley Fool): discovered link from https://www.fool.com/quote/nasdaq/mrvl/ (HTTP 200). Quote page listed `/earnings/call-transcripts/2026/05/27/marvell-mrvl-q1-2027-earnings-transcript/`. robots.txt (https://www.fool.com/robots.txt) does not disallow `/earnings/` for `User-agent: *`. Fetched with curl -L and UA "Mozilla/5.0 (compatible; company-research-skill; contact: owner@localhost)"; HTTP 200, 543,960 bytes, no redirect. Page title: "Marvell (MRVL) Q1 2027 Earnings Transcript | The Motley Fool". Page "Date" block: May 27, 2026. Body confirms "first quarter of fiscal 27" and Q2 FY27 guidance. Result: USED.
- Tiers 4/5: not needed.

## As-of discipline

- The Fool quote page also listed a Q2 FY2027 transcript dated 2026-08-31. It is after the as-of cutoff and was NOT fetched or read.
- No other post-cutoff material was used.

## Processing notes

- HTML stripped with python3 + BeautifulSoup 4.13.5 (lxml parser). Kept from `div.article-body.transcript-content`: the "Date" and "Call participants" blocks and everything under the h2 "Full Conference Call Transcript". Dropped: Fool's editorial "Takeaways", "Summary", "Industry glossary" blocks, the image caption, the "Need a quote from a Motley Fool analyst" line, and promo/ad divs (`article-body-promobox`, empty `my-8` divs).
- Coverage caveat: Fool's text begins with the CEO's first sentence ("Yes. Thanks Ashish and good afternoon everyone."). The operator's opening and the investor-relations safe-harbor introduction (Ashish Saran) are not present in this source. The text runs through the full Q&A and the operator's closing line.
- Transcript quality caveat: this is a machine/third-party transcription. It contains obvious mis-transcriptions (e.g., "TSC" for what is presumably TSMC; "CO-OP" for what is presumably COUPE; analyst name "Serene E with RBC Capital Markets"; numbers occasionally garbled such as "Reaching approximately 50% by Q4"). Notes quote the source verbatim and flag suspected transcription errors as inferences; they do not correct them silently.
- Speaker labels as they appear in the source: "Matthew J. Murphy", "Willem A. Meintjes", "Christopher Koopmans", "Operator", "Analyst" / "Analyst (Name)". Five analyst turns are labeled only "Analyst:"; their name and firm are taken from the operator's immediately preceding hand-off line.

## ir.md

# MANIFEST-ir — Marvell Technology, Inc. (MRVL) — Q1 FY2027 (quarter ended May 2, 2026)

IR gatherer (press release and slides). As-of cutoff 2026-05-28; every document below was published 2026-05-27. Fetch date 2026-09-07. Only extracted text is cached; PDFs and HTML were downloaded to /tmp and discarded.

Format: filename | origin URL | fetch date | word count | note on text quality

press-release.txt | https://www.sec.gov/Archives/edgar/data/1835632/000183563226000014/q127_8kx522026ex-991.htm (8-K Exhibit 99.1, accession 0001835632-26-000014, filed 2026-05-27; folder index https://www.sec.gov/Archives/edgar/data/1835632/000183563226000014/) | 2026-09-07 | 4613 | Good. HTML stripped with python3/BeautifulSoup; inline tags unwrapped so sentences stay on one line; each table row rendered on one line with " | " cell separators between [TABLE]/[/TABLE] markers. Verified readable: headline bullets, CEO quote, Q2 FY27 outlook bullets, statements of operations, balance sheet, cash flow, all GAAP-to-non-GAAP reconciliations, outlook reconciliation, end-market definitions and revenue-by-end-market tables. Note: SEC blocked User-Agent "company-research-skill contact: owner@localhost" as an "Undeclared Automated Tool"; "company-research-skill owner@example.com" was accepted.
slides.txt | https://d1io3yog0oux5.cloudfront.net/_eac9f0b88f7114d6778a284aa60d5990/marvell/db/3734/35382/presentation/2026_05_27_Marvell_Q1_FY27_financial_business_results_FINAL.pdf (linked from https://investor.marvell.com/financial-information/financial-results as "Financial and Business Results PDF" for Q1 FY2027) | 2026-09-07 | 3605 | Good for a slide deck. 33 pages, pdftotext -layout, pages separated by form feeds. All summary P&L tables (p.11-13, p.16-17) and appendix reconciliations (p.21-32) extracted cleanly with aligned columns. Bar-chart pages (p.8-10, p.14-15) yield values but with chart labels interleaved, so read the tables on p.11-12 and p.16 for the same numbers. Executive summary (p.7) and end-market highlight bullets (p.14-15) fully legible. Page 33 has no extractable text (closing slide).
supplemental.txt | https://d1io3yog0oux5.cloudfront.net/_eac9f0b88f7114d6778a284aa60d5990/marvell/db/3734/35382/additional_earnings_information/MRVL+Q1%2727+Additional+Information_FINAL.pdf (linked from the same IR page as "Additional Earnings Information PDF" for Q1 FY2027) | 2026-09-07 | 3069 | Good. 11 pages, pdftotext -layout. Eight-quarter tables (Q2 FY2025 through Q1 FY2027) for balance sheet (p.4), statement of operations with stock-based compensation by line (p.5), cash flows (p.6-7), GAAP-to-non-GAAP operating income and net income reconciliations (p.8-9), and revenue by end market with % of total (p.10). Columns aligned; "$" signs sit in their own column. Page 11 has no extractable text.
notes-ir.md | (derived from the three files above) | 2026-09-07 | 4909 | Structured bullets, every figure verbatim with period and source tag; §8 lists what the documents do not disclose.
MANIFEST-ir.md | (this file) | 2026-09-07 | 383 | —

Transcript: not in scope for this gatherer (see notes-transcript.md / MANIFEST for the transcript tier).

