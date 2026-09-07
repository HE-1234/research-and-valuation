# MANIFEST — filings gatherer, RKLB (Rocket Lab Corporation, CIK 0001819994), Q2 2026 (quarter ended 2026-06-30)

As-of cutoff: 2026-08-10 (10-Q filing date; earnings call 2026-08-10). Every document below was published on or before that date; nothing after it was fetched or read (the two 8-Ks filed 2026-08-13 were deliberately not touched). Fetched 2026-09-07 from SEC EDGAR (www.sec.gov) with User-Agent "company-research-skill owner@example.com", Accept-Encoding gzip/deflate, and a 1.2-second sleep between requests (11 document requests plus 4 folder-index requests, all HTTP 200 on first attempt). HTML was converted to text with Python 3 + BeautifulSoup 4.13.5 (lxml parser): script/style blocks, the hidden inline-XBRL ix:header, and display:none blocks were dropped; table rows kept one per line with cells separated by " | "; block-level line breaks preserved; whitespace collapsed. Only extracted .txt files are stored here; the HTML was deleted from /tmp after conversion. No PDFs were involved.

Format: filename | origin URL | fetch date | word count (description, filing date)

10-K-FY2025.txt | https://www.sec.gov/Archives/edgar/data/1819994/000181999426000013/rklb-20251231.htm | 2026-09-07 | 66483 words (Form 10-K for fiscal year ended 2025-12-31, filed 2026-02-26; accession 0001819994-26-000013)
10-Q-2026-Q2.txt | https://www.sec.gov/Archives/edgar/data/1819994/000181999426000062/rklb-20260630.htm | 2026-09-07 | 30093 words (Form 10-Q for quarter ended 2026-06-30, filed 2026-08-10; accession 0001819994-26-000062)
DEF14A-2026.txt | https://www.sec.gov/Archives/edgar/data/1819994/000162828026023922/rklb-20260406.htm | 2026-09-07 | 36292 words (definitive proxy statement filed 2026-04-06; annual meeting 2026-05-20; accession 0001628280-26-023922)
10-K-FY2023.txt | https://www.sec.gov/Archives/edgar/data/1819994/000095017024022160/rklb-20231231.htm | 2026-09-07 | 68670 words (Form 10-K of Rocket Lab USA, Inc. for fiscal year ended 2023-12-31, filed 2024-02-28; accession 0000950170-24-022160; used for FY2021–FY2022 financials, segment history, 2021–2022 acquisitions)
8-K-2026-06-29.txt | https://www.sec.gov/Archives/edgar/data/1819994/000175392626001085/g085783_8k.htm + g085783_ex99-1.htm + g085783_ex99-2.htm | 2026-09-07 | 10153 words (Form 8-K filed 2026-06-29, Items 1.01/7.01/9.01: Iridium merger agreement, joint press release, investor presentation; accession 0001753926-26-001085; Exhibits 2.1 and 10.1 not fetched)
8-K-2026-06-05.txt | https://www.sec.gov/Archives/edgar/data/1819994/000181999426000056/rklb-20260603.htm | 2026-09-07 | 860 words (Form 8-K filed 2026-06-05, Item 5.02: appointment of Chief Accounting Officer; accession 0001819994-26-000056)
8-K-2026-04-14.txt | https://www.sec.gov/Archives/edgar/data/1819994/000175392626000654/g085683_8k.htm + g085683_ex99-1.htm | 2026-09-07 | 1746 words (Form 8-K filed 2026-04-14, Items 3.02/7.01/8.01: Mynaric acquisition closing and press release; accession 0001753926-26-000654)
8-K-2026-03-30.txt | https://www.sec.gov/Archives/edgar/data/1819994/000175392626000568/g085462_8k-rocket.htm | 2026-09-07 | 698 words (Form 8-K filed 2026-03-30, Item 5.02: CEO salary reduction to $1 and RSU cancellation; accession 0001753926-26-000568)
notes-filings.md | (written by the filings gatherer from the eight files above) | 2026-09-07 | 16380 words

## Fetch log

- All URLs were supplied by the coordinator; no data.sec.gov submissions index was needed or fetched.
- Four required documents: first attempt returned HTTP 200 for all four (sizes 2.4 MB, 1.7 MB, 0.8 MB, 4.2 MB of HTML). No 403/429, no retries.
- Optional 8-Ks: the four folder indexes (https://www.sec.gov/Archives/edgar/data/1819994/<accession>/) were fetched first to identify the primary document and Exhibit 99 files; then seven documents (four primaries, three Exhibit 99s) were fetched. All HTTP 200 on first attempt. For each 8-K the primary document and its Exhibit 99(s) were concatenated into one dated .txt with "### PRIMARY DOCUMENT" / "### EXHIBIT 99.x" separators.
- Not fetched: 8-K 2026-06-29 Exhibit 2.1 (merger agreement) and Exhibit 10.1 (form of support agreement) — long legal exhibits outside the brief; the Item 1.01 summary was used instead. The two 8-Ks filed 2026-08-13 (post-cutoff). FY2022 and FY2024 10-Ks (not requested; their absence leaves the 12/31/2022 backlog and the 12/31/2024 backlog segment split as gaps, recorded in notes-filings.md §14). Earnings press release, slides and transcript belong to the ir and transcript gatherers.
- Conversion note: BeautifulSoup emitted an XMLParsedAsHTMLWarning for the inline-XBRL documents; harmless, output verified.

## Verification

- Each .txt was checked to read as prose (first 50 lines are the SEC cover page: registrant name, fiscal period, file number, address).
- MD&A heading present: "Item 7. Management's Discussion and Analysis..." at line 1297 of 10-K-FY2025.txt and line 1471 of 10-K-FY2023.txt; "Item 2. Management's Discussion and Analysis..." at line 1729 of 10-Q-2026-Q2.txt. DEF14A-2026.txt has no MD&A (checked instead for "COMPENSATION DISCUSSION AND ANALYSIS" at line 679 and "SECURITY OWNERSHIP OF CERTAIN BENEFICIAL OWNERS AND MANAGEMENT" at line 1605). The 8-K files were checked for their Item headings (Item 1.01 / 5.02 / 8.01 present).
- Financial-statement tables render one row per line with " | " separators (e.g., "Total revenues | 601,799 | 436,214 | 244,592" in 10-K-FY2025.txt).
