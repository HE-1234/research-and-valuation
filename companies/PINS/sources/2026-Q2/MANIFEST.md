# MANIFEST — PINS sources/2026-Q2

_Pinterest, Inc. (PINS, CIK 0001506293). As-of quarter Q2 2026 (quarter ended 2026-06-30). As-of cutoff 2026-08-04 (earnings call 2026-08-04 4:30 pm ET; 10-Q filed 2026-08-04). All fetches 2026-09-07. Transcript source tier: 1, company-published (Pinterest IR, Q4 Inc. CDN). Only extracted text is cached. The three sections below are the per-gatherer manifests, merged verbatim._

## filings

# MANIFEST — filings gatherer, Pinterest, Inc. (PINS, CIK 0001506293), Q2 2026

_As-of cutoff 2026-08-04 (10-Q and earnings call both dated 2026-08-04). All fetches performed 2026-09-07 from SEC EDGAR with User-Agent `company-research-skill owner@example.com` and at least 1 second between requests. Only extracted text is cached in this folder; no HTML or PDF was saved here. Nothing filed after 2026-08-04 was fetched or read._

Format: filename | origin URL | fetch date | filing date | word count

## Cached files written by this gatherer

- 10-K-FY2025.txt | https://www.sec.gov/Archives/edgar/data/1506293/000150629326000021/pins-20251231.htm | 2026-09-07 | filed 2026-02-12 (FY ended 2025-12-31) | 52,575 words
- 10-Q-2026-Q2.txt | https://www.sec.gov/Archives/edgar/data/1506293/000150629326000104/pins-20260630.htm | 2026-09-07 | filed 2026-08-04 (quarter ended 2026-06-30) | 45,618 words
- DEF14A-2026.txt | https://www.sec.gov/Archives/edgar/data/1506293/000150629326000058/pins-20260407.htm | 2026-09-07 | filed 2026-04-08 (annual meeting 2026-05-21; record date 2026-03-27) | 36,078 words
- 10-K-FY2023.txt | https://www.sec.gov/Archives/edgar/data/1506293/000150629324000018/pins-20231231.htm | 2026-09-07 | filed 2024-02-08 (FY ended 2023-12-31; FY2021–FY2023 statements) | 50,723 words
- 10-K-FY2024.txt | https://www.sec.gov/Archives/edgar/data/1506293/000150629325000022/pins-20241231.htm | 2026-09-07 | filed 2025-02-06 (FY ended 2024-12-31) | 52,088 words — **added beyond the orchestrator's list**; see fetch log
- 10-K-FY2022.txt | https://www.sec.gov/Archives/edgar/data/1506293/000150629323000023/pins-20221231.htm | 2026-09-07 | filed 2023-02-06 (FY ended 2022-12-31) | 49,406 words — **added beyond the orchestrator's list**; see fetch log
- 8-K-2026-01-20.txt | https://www.sec.gov/Archives/edgar/data/1506293/000150629326000005/pins-20260120.htm | 2026-09-07 | filed 2026-01-20 (Item 7.01: Chief Business Officer appointment) | 483 words
- 8-K-2026-01-27.txt | https://www.sec.gov/Archives/edgar/data/1506293/000150629326000009/pins-20260122.htm | 2026-09-07 | filed 2026-01-27 (Item 2.05: restructuring plan) | 910 words
- 8-K-2026-02-09.txt | https://www.sec.gov/Archives/edgar/data/1506293/000150629326000012/pins-20260209.htm | 2026-09-07 | filed 2026-02-09 (Item 5.02: director appointment) | 720 words
- 8-K-2026-02-18.txt | https://www.sec.gov/Archives/edgar/data/1506293/000150629326000026/pins-20260217.htm | 2026-09-07 | filed 2026-02-18 (Item 7.01: tvScientific closing, Q1 2026 guidance update) | 1,299 words
- 8-K-2026-03-03.txt | https://www.sec.gov/Archives/edgar/data/1506293/000119312526086731/d22903d8k.htm | 2026-09-07 | filed 2026-03-03 (Items 1.01, 2.03, 3.02, 8.01: Elliott convertible notes, ASR, $3.5 billion buyback) | 3,286 words
- 8-K-2026-03-05.txt | https://www.sec.gov/Archives/edgar/data/1506293/000119312526092744/d107385d8k.htm | 2026-09-07 | filed 2026-03-05 (Items 1.01, 2.03, 3.02: notes closing and indenture) | 2,271 words
- 8-K-2026-05-26.txt | https://www.sec.gov/Archives/edgar/data/1506293/000150629326000074/pins-20260521.htm | 2026-09-07 | filed 2026-05-26 (Item 5.07: annual-meeting votes) | 975 words
- notes-filings.md | (written by the filings gatherer from the thirteen files above) | 2026-09-07 | n/a | 16001 words

Not produced by this gatherer: `press-release.txt`, `press-release-2026-Q1.txt`, `slides.txt`, `transcript.txt` and any `notes-ir.md` / `notes-transcript.md` belong to the IR and transcript gatherers and were not read or used for notes-filings.md.

## Fetch log

- Filings list confirmed first with one request to https://data.sec.gov/submissions/CIK0001506293.json (HTTP 200). Company name "PINTEREST, INC.", exchange NYSE, fiscal year end 1231. The accessions and primary-document names supplied by the orchestrator matched the JSON exactly for all thirteen listed documents. The JSON also shows 8-Ks filed 2026-08-07 (accession 0001506293-26-000107) and 2026-08-28 (0001506293-26-000117); both are after the cutoff and were not fetched.
- HTTP results: every document request returned 200 on the first attempt (no 403 or 429 encountered, so no retry or back-off was needed). Total SEC requests: 1 (submissions JSON) + 4 (10-K FY2025, 10-Q, DEF 14A, 10-K FY2023) + 7 (8-Ks) + 2 (10-K FY2024, 10-K FY2022) = 14, spaced at least 1 second apart. HTML sizes: 10-K FY2025 1,927,070 bytes; 10-Q 1,689,107; DEF 14A 1,407,455; 10-K FY2023 1,884,201; 10-K FY2024 1,939,059; 10-K FY2022 2,286,858; 8-Ks 23,065–49,218. Each HTML ended with a closing `</html>` tag.
- Conversion: Python 3.13 + BeautifulSoup 4.13 (lxml parser). Dropped script, style, ix:header and display:none elements; joined table cells with " | "; inserted line breaks at block elements; collapsed whitespace. HTML was downloaded to /tmp, converted, and deleted; no HTML or PDF binary was placed in this folder.
- Verification: (a) readability of the first 40 lines of each 10-K and the 10-Q (cover page, registrant name, period); (b) headings survived: 10-K FY2025 "Item 1. Business" (line 363), "Item 1A. Risk factors" (545), "Item 7." (1455), "Item 8." (1987); 10-K FY2023 Items 1/1A/7/8 at lines 361/539/1403/1857; 10-K FY2024 at 353/533/1425/1949; 10-K FY2022 at 357/523/1387/1833; 10-Q "Item 1. Financial Statements" (319), "ITEM 2. Management's Discussion" (1311), "PART II" (1863), "Item 1A. Risk Factors" (1875); (c) each file ends with the document's closing part (10-K/10-Q signature blocks ending "Andrea Acosta" / "Chief Financial Officer (Principal Financial Officer and Principal Accounting Officer)"; proxy ends with the investor-relations address; 8-Ks end with the CFO signature).
- Known limitation of these sources: the quarterly MAU, revenue-by-geography and ARPU-by-geography tables in Pinterest's 10-Ks and 10-Q are chart images; only chart titles and footnotes survive extraction. Regional MAUs are therefore not available from filings text for any period (see notes-filings.md, header note and section 18).
- Deviation from the fetch list: two extra 10-Ks (FY2024 and FY2022) were fetched because the five-year user-geography revenue and ARPU series and the headcount series required FY2024 and FY2022 prose that exists nowhere else in text form (each 10-K's MD&A gives the current year's regional dollar amounts only). Both filings predate the cutoff. The FY2021 10-K was not fetched because it predates the U.S. and Canada / Europe / Rest of World presentation (introduced Q1 2022) and would not supply FY2021 regional figures in text.
- 8-Ks: all seven in-window 8-Ks carried substantive items (none was a bare Item 2.02 earnings release), so all seven were cached. No exhibits were fetched: the 8-K bodies of 2026-03-03 and 2026-03-05 already state the note terms (principal, coupon, maturity, conversion rate and price, redemption and put terms, Elliott governance rights), and the 10-Q Note 5 restates them. The earnings 8-Ks of 2026-02-12, 2026-05-04 and 2026-08-04 were skipped per instructions (IR gatherer's scope).
- Automated check on notes-filings.md: every numeric token in the notes (excluding lines marked "computed") was searched verbatim in the cached filing texts; after restating a dozen unit conversions in the filings' own units, the only unmatched tokens are labelled computed totals, "Item 2.02", and trailing-comma artifacts.
- Nothing filed after 2026-08-04 was fetched, read, or used.

## transcript

# MANIFEST — transcript gatherer — Pinterest, Inc. (PINS, CIK 0001506293) — Q2 2026

As-of cutoff: 2026-08-04. Call date: 2026-08-04, 4:30 pm ET. Gatherer run: 2026-09-07.

| file | origin URL | fetch date | source tier | word count |
|---|---|---|---|---|
| transcript.txt | https://s204.q4cdn.com/369458543/files/doc_earnings/2026/q2/transcript/Q2-2026-Transcript.pdf | 2026-09-07 | 1 company-published (Pinterest IR, Q4 Inc. CDN) | 9297 |
| notes-transcript.md | derived from transcript.txt (this gatherer); §4 cross-checked against press-release.txt cached by the IR gatherer | 2026-09-07 | n/a | 10240 |

## Fetch and conversion notes

- Discovery: the transcript is listed in Pinterest's open Q4 Inc. JSON feed `https://investor.pinterestinc.com/feed/FinancialReport.svc/GetFinancialReportList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1&reportSubType=` (HTTP 200, 6,245 bytes) under "Second Quarter 2026" as document "Transcript" (341 KB). The same feed entry lists the press release, earnings presentation, webcast and 10-Q links, which belong to the other gatherers. The IR HTML pages themselves were not fetched.
- Fetch: `curl -L -A "company-research-skill owner@example.com"`; HTTP 200, 348,705 bytes, content-type application/pdf.
- `pdfinfo`: title "Q2 2026 Transcript"; producer "Skia/PDF m153 Google Docs Renderer"; PDF 1.6; 16 pages, letter size; CreationDate and ModDate 2026-08-05 01:49:17 UTC (= 2026-08-04 9:49 pm ET, the evening of the call, so inside the as-of cutoff); not encrypted.
- Converted with `pdftotext -layout` to `transcript.txt` (9,297 words, 60,232 bytes, 902 lines). The PDF was downloaded to /tmp and deleted after conversion; no PDF or HTML was saved into the repo.
- Printed page numbers: YES. Each page carries its number (1–16) at the foot, preserved as a right-aligned digit line in `transcript.txt`. Printed page numbers coincide with PDF page numbers, so `p.N` tags in `notes-transcript.md` are unambiguous.
- Cleanups applied: NONE were needed. Checks run on the raw output: zero U+200B zero-width spaces; zero lines ending in a hyphen (no hyphenation splits); no split first letters (the only single-character lines are the page numbers 1–9); the only non-ASCII characters are typographic apostrophes (123), curly double quotes (6 pairs) and em dashes (6), all left as UTF-8. `transcript.txt` is byte-identical to the raw `pdftotext` output (verified with `cmp`).
- Verified structure: the file begins with the heading "MANAGEMENT DISCUSSION SECTION" followed by the operator's introduction ("Hello, everyone. Thank you for joining us. Welcome to Pinterest's Second Quarter 2026 Earnings Conference Call."), the IR head's safe-harbor remarks (Andrew Somberg), CEO remarks (Bill Ready), CFO remarks and guidance (Julia Donnelly), then a "QUESTION AND ANSWER SECTION" heading at line 320 (printed page 7). The Q&A has 12 Operator turns and 11 analyst questions: Mark Shmulik (Bernstein), Colin Sebastian (Baird), Brian Nowak (Morgan Stanley), Ross Sandler (Barclays), John Blackledge (TD Cowen), Justin Patterson (KeyBanc), Nitin Bansal (Bank of America), Jason Helfstein (Oppenheimer), Eric Sheridan (Goldman Sachs), Michael Morris (Guggenheim Securities), Shweta Khajuria (Wolfe Research). Three of the eleven asked two-part questions (Helfstein, Sheridan, Morris). The call ends with the CEO's closing remarks and the operator's sign-off on page 16.
- The transcript is the company's own edited text (Google Docs-rendered), not a machine transcript; numbers in it may be relied on, and every figure quoted in `notes-transcript.md` §4 was also cross-checked against `press-release.txt` where the release states it. One discrepancy found and recorded in §4: the call says "$58 million toward share repurchases" in Q2 while the release's cash-flow statement shows $78,578K cash paid for repurchases of Class A common stock in the quarter.

## Fallback tiers

- Tier 2 (8-K exhibit): not needed and not fetched; per the orchestrator the 2026-08-04 8-K (accession 0001506293-26-000102) carries only the press-release exhibit.
- Tier 3 (Motley Fool, published 2026-08-11): not needed and not fetched.
- Tiers 4–5: not applicable.

## As-of discipline

- Nothing published after 2026-08-04 was fetched or consulted. The only documents read by this gatherer were the JSON feed listing, the transcript PDF (created 2026-08-04 ET), and, for the §4 cross-check, the already-cached `press-release.txt` (release dated August 4, 2026) plus a keyword grep of the already-cached `slides.txt` to confirm the full-year margin outlook wording.
- Not produced by this gatherer: `press-release.txt`, `press-release-2026-Q1.txt`, `slides.txt`, the 10-K/10-Q/8-K/DEF 14A text files and any other files in this folder; they belong to the IR and filings gatherers.

## ir

# MANIFEST-ir — Pinterest, Inc. (PINS, CIK 0001506293) Q2 2026 — IR gatherer (press release + slides + prior-quarter release)

As-of cutoff 2026-08-04. The Q2 2026 release and slides carry pdfinfo creation dates of 2026-08-04 and state in their text that all information is "as of August 4, 2026". The Q1 2026 release (prior-quarter comparison values) carries a creation date of 2026-05-04 and is datelined May 4, 2026. PDFs were downloaded to /tmp and deleted after conversion; only extracted text (`pdftotext -layout`) is cached here. User-Agent used for all fetches: `company-research-skill owner@example.com`. Fetch date for everything: 2026-09-07.

filename | origin URL | fetch date | document date | pages | word count | note on text quality
---|---|---|---|---|---|---
press-release.txt | https://s204.q4cdn.com/369458543/files/doc_earnings/2026/q2/earnings-result/Q2-2026-Press-Release.pdf | 2026-09-07 | 2026-08-04 (dateline "August 4, 2026"; pdfinfo CreationDate 2026-08-04 14:56 UTC; title "Q2 2026 Press Release"; Workiva) | 11 | 4104 | Clean, complete text; printed page numbers 1–11 match PDF pages. p.1 headline, bullets, CEO quote, financial highlights table; p.2 revenue/MAU/ARPU by geography; p.3 guidance; p.4 webcast + forward-looking statements; p.5 non-GAAP definitions; p.6 key-metric definitions and contacts; p.7 balance sheet; p.8 statement of operations (Q2 and six months); p.9 cash flow statement (Q2 and six months); p.10 SBC/payroll-tax/amortization by function and non-GAAP cost reconciliation; p.11 Adjusted EBITDA, non-GAAP net income and FCF reconciliations. Column alignment preserved; all figures legible. No OCR needed. Fallback URLs (alternate q4cdn spelling; EDGAR 8-K Exhibit 99.1) were not needed.
slides.txt | https://s204.q4cdn.com/369458543/files/doc_earnings/2026/q2/presentation/Q2-2026-Pinterest-Earnings-Presentation.pdf | 2026-09-07 | 2026-08-04 (p.3 "as of August 4, 2026"; pdfinfo CreationDate 2026-08-04 05:12 UTC; title "Q2 2026 Pinterest Earnings Presentation"; PowerPoint) | 23 | 5166 | 960x540 pt landscape, 4.5 MB (image-heavy backgrounds) but every page yielded text and every chart data label was captured; no page is image-only for data. p.6 is mostly product screenshots (three phone mockups) with a short caption; screenshot text is image-only and is not data. Quirks: (a) pdftotext inserted spaces inside some words ("non -GAAP", "ad ver tisers", "log ged") — quotes in notes-ir.md have these removed; (b) chart data labels on pp.5, 8–14 appear out of visual order in the layout text; the quarter mapping in notes-ir.md was fixed with `pdftotext -bbox` word coordinates and a rendered PNG of p.5, and cross-checked against the appendix tables (pp.17–22) and the release; (c) apostrophes are UTF-8 curly (e.g., "Q2'26"). The only guidance page is p.4; it also carries the full-year Adjusted EBITDA margin outlook (~30%, raised from 29%) which is not in the release. No OCR performed (tesseract is installed but was not needed).
press-release-2026-Q1.txt | https://s204.q4cdn.com/369458543/files/doc_earnings/2026/q1/earnings-result/Q126-PressRelease.pdf | 2026-09-07 | 2026-05-04 (dateline "May 4, 2026"; pdfinfo CreationDate 2026-05-04 14:23 UTC; title "Q1-26-PressRelease"; Workiva) | 11 | 3934 | Same structure and quality as the Q2 release (printed pages 1–11 match PDF pages). Used only for prior-quarter comparison values (Q1 2026 revenue/MAU/ARPU by region, Adjusted EBITDA, FCF, share count, buybacks) and for the Q2 2026 guidance given on May 4, 2026. Q1 slides and Q1 transcript were not fetched.
notes-ir.md | derived from the three files above | 2026-09-07 | — | — | 9030 | Structured bullets, every number verbatim with unit and period, tagged [Q2 2026 release, p.N], [Q2 2026 slides, p.N] or [Q1 2026 release, p.N]. Items derived by the gatherer are labelled "(computed)". Automated numeric check (see fetch log): 1,832 numeric tokens checked, 1,811 found verbatim in the three cached texts; all 21 misses are on lines labelled "computed"; zero unlabelled misses.

## Fetch log

- Feed: `https://investor.pinterestinc.com/feed/FinancialReport.svc/GetFinancialReportList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1&reportSubType=` → HTTP 200 (6,245 bytes JSON). It lists, for "Second Quarter 2026": Press Release (92 KB, the primary URL above), Webcast, Earnings Presentation (4.41 MB, the URL above), Transcript (341 KB, `https://s204.q4cdn.com/369458543/files/doc_earnings/2026/q2/transcript/Q2-2026-Transcript.pdf`, not fetched by this gatherer — company-published transcript, i.e. tier 1 is available for PINS), and 10-Q (cloudfront PDF, not fetched). For "First Quarter 2026": Press Release (68 KB, the URL above), Webcast, Earnings Presentation (3.32 MB, not fetched), Transcript (231 KB, not fetched), 10-Q (not fetched).
- Q2-2026-Press-Release.pdf → HTTP 200, 94,463 bytes, application/pdf. pdfinfo: 11 pages, CreationDate Tue Aug 4 14:56:05 2026 UTC, ModDate Aug 4 15:34:46 2026 UTC.
- Q2-2026-Pinterest-Earnings-Presentation.pdf → HTTP 200, 4,511,664 bytes, application/pdf. pdfinfo: 23 pages, CreationDate Tue Aug 4 05:12:05 2026 UTC, ModDate Aug 4 15:34:48 2026 UTC.
- Q126-PressRelease.pdf → HTTP 200, 69,899 bytes, application/pdf. pdfinfo: 11 pages, CreationDate Mon May 4 14:23:43 2026 UTC.
- No fallbacks were needed (the alternate `Q2-2026-PressRelease.pdf` spelling and the EDGAR 8-K Exhibit 99.1 `https://www.sec.gov/Archives/edgar/data/1506293/000150629326000102/q2-26xpressrelease.htm` were not requested). No SEC requests were made by this gatherer.
- Conversion: `pdftotext -layout` for all three; per-page word counts checked (slides: every one of 23 pages non-empty; smallest are p.1 title 10 words, p.15 "Appendix" 8 words, p.23 copyright 6 words). `pdftotext -bbox` was run on slide pages 5, 7–14 to recover chart label positions; `pdftoppm -r 60` rendered pp.5–6 to PNG for visual confirmation. All PDFs, bbox HTML and PNG renders were deleted from /tmp afterwards.
- As-of discipline: nothing published after 2026-08-04 was fetched or read. The Q1 2026 release (May 4, 2026) predates the cutoff. No Q3 2026 material, no later press releases, no transcript and no 10-Q were fetched by this gatherer.
- Numeric check on notes-ir.md: every numeric token (excluding ISO dates, page references, quarter labels, years and section numbers) was tested for a verbatim match in the three cached text files. 1,832 tokens checked; 1,811 matched; the 21 non-matches are all on lines labelled "computed" (sums of share classes and cash lines, implied guidance margins, non-GAAP operating income, six-month FCF, SBC/D&A reconciling differences, implied average buyback price, unrounded margin change, MAU component sum). Zero unlabelled misses.
- Not produced by this gatherer: `10-K-FY2023.txt`, `10-K-FY2025.txt`, `10-Q-2026-Q2.txt`, `DEF14A-2026.txt` (filings gatherer) and any transcript files; they were not read or used for notes-ir.md.
