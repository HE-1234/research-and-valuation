# MANIFEST — MRVL sources/FY2027-Q2

## filings.md

# MANIFEST — filings gatherer — Marvell Technology (MRVL, CIK 0001835632) — Q2 FY2027 (quarter ended 2026-08-01)

As-of cutoff: 2026-08-28 (10-Q filing date). Nothing published after that date was fetched or used.
Fetch method: `curl -sS -A "company-research-skill owner@example.com"` from www.sec.gov/Archives; HTML stripped to text with python3 + BeautifulSoup 4.13.5 (table cells joined with ` | `, block line breaks kept, whitespace collapsed). Only .txt saved; raw HTML left in /tmp.
Format: `filename or accession | origin URL | fetch date | word count or classification`

## Files saved in this folder

- `10-Q-FY2027-Q2.txt` | https://www.sec.gov/Archives/edgar/data/1835632/000183563226000025/mrvl-20260801.htm | fetched 2026-09-07 | 48,556 words (10-Q for quarter ended 2026-08-01, filed 2026-08-28, acc 0001835632-26-000025; MD&A "Item 2" verified present as prose)
- `8-K-2026-06-11.txt` | https://www.sec.gov/Archives/edgar/data/1835632/000119312526267688/d151562d8k.htm (8-K body) and https://www.sec.gov/Archives/edgar/data/1835632/000119312526267688/d151562dex991.htm (Exhibit 99.1 press release, same accession, appended after a separator line) | fetched 2026-09-07 | 2,415 words combined (body 1,419 + exhibit 983 + separator) | NON-ROUTINE: Item 5.02 officer change — CFO Willem Meintjes resigned effective 2026-06-15; director Daniel Durn appointed CFO effective 2026-06-15; Item 7.01 reaffirmed Q2 FY2027 outlook as given 2026-05-27
- `8-K-2026-08-19.txt` | https://www.sec.gov/Archives/edgar/data/1835632/000119312526356217/d412696d8k.htm | fetched 2026-09-07 | 816 words | NON-ROUTINE: Item 1.01 commercial agreement with Google LLC (dated 2026-07-29) for custom semiconductor products attached to the TPU ecosystem; Item 3.02 warrant to Google for up to 58,970,907 shares at $206.58 issued 2026-08-18. Exhibit 4.1 (warrant agreement) not fetched.
- `notes-filings.md` | written by this gatherer 2026-09-07 | structured bullet facts from the above
- `MANIFEST-filings.md` | this file

## Filings fetched, read, and classified only (not saved; routine)

- acc 0001628280-26-045564 (mrvl-20260625.htm, 8-K filed 2026-06-25) | https://www.sec.gov/Archives/edgar/data/1835632/000162828026045564/mrvl-20260625.htm | fetched 2026-09-07 | 863 words | ROUTINE: Item 5.07 annual-meeting vote results (2026-06-25) plus Item 8.01 declaration of the regular $0.06/share quarterly dividend (record 2026-07-10, payable 2026-07-30). Not saved per run rules; a few vote figures are quoted in notes-filings.md from this text.
- acc 0001193125-26-299843 (d82462d8k.htm, 8-K filed 2026-07-09) | https://www.sec.gov/Archives/edgar/data/1835632/000119312526299843/d82462d8k.htm | fetched 2026-09-07 | 469 words | ROUTINE: Item 8.01 filed solely to attach a Wilson Sonsini Exhibit 5.1 legality opinion for a prospectus supplement (filed 2026-07-09) to the automatic shelf S-3 No. 333-285742. The 8-K body does not state what securities the supplement covers; the 10-Q debt table shows no new notes after the 2026-04-15 2036 Senior Notes.
- Filing index for acc 0001193125-26-267688 | https://www.sec.gov/Archives/edgar/data/1835632/000119312526267688/ | fetched 2026-09-07 | used only to locate the Exhibit 99.1 filename.

## Not fetched (by instruction)

- 8-K filed 2026-08-27 (Q2 FY2027 earnings release) — handled by the ir gatherer.
- Anything in `sources/FY2027-Q1/` — belongs to a different run; not read.

## Failures

- None. All six HTTP fetches returned 200 on the first attempt.

## transcript.md

# MANIFEST — transcript gatherer — Marvell (MRVL, CIK 0001835632) — FY2027-Q2

Quarter: Q2 FY2027 (fiscal quarter ended 2026-08-01; earnings call held 2026-08-27, 4:45 p.m. ET). As-of cutoff: 2026-08-28. Run type: refresh. Gatherer run date: 2026-09-07.

## Files

| File | Origin URL | Fetch date | Source tier | Word count |
|---|---|---|---|---|
| transcript.txt | https://www.fool.com/earnings/call-transcripts/2026/08/31/marvell-mrvl-q2-2027-earnings-call-transcript/ | 2026-09-07 | 3 third-party (Motley Fool) | 8,660 (8,549 in the call text; 111 in the added header and participant list) |
| notes-transcript.md | derived from transcript.txt (no external sources) | written 2026-09-07 | n/a | 10,179 |

## Transcript source tiers checked (AGENTS.md §12.2)

1. Company-published (IR site): checked https://investor.marvell.com/financial-information/financial-results on 2026-09-07 (HTTP 200, 191,947 bytes). Zero occurrences of "transcript" on the page. Result: none available, consistent with AGENTS.md §12.3.
2. 8-K exhibit: skipped per run instructions; the 2026-08-27 8-K (accession 0001835632-26-000022) contains only the press release. Result: not applicable.
3. Third-party free (The Motley Fool): SUCCESS. URL above fetched 2026-09-07 with curl -L and User-Agent "Mozilla/5.0 (compatible; company-research-skill; owner@example.com)"; HTTP 200, 524,471 bytes, no redirect. robots.txt (https://www.fool.com/robots.txt, HTTP 200) has no rule touching /earnings/ for User-agent: *; path allowed. First attempt succeeded; no retry needed.
4. Owner-supplied file: not needed.
5. None: not needed.

## Call identity confirmation

- Page title: "Marvell (MRVL) Q2 2027 Earnings Call Transcript | The Motley Fool".
- Date line in source: "Thursday, Aug. 27, 2026 at 4:45 p.m. ET".
- Operator opening line: "Good afternoon, and welcome to Marvell Technology Inc. Second Quarter of Fiscal Year 2027 Earnings Conference Call."
- CEO: "For the second quarter of fiscal 2027, Marvell delivered record revenue of $2.739 billion".
- The transcript text itself does not state the quarter-end date (2026-08-01); that date comes from the run instructions and should be cross-checked against the press release / 10-Q by the ir and filings gatherers.
- Published on fool.com 2026-08-31 (after the 2026-08-28 cutoff) but records the 2026-08-27 call; permitted per run instructions. No other post-cutoff material was read or used.

## Extraction method

- python3 with BeautifulSoup 4.13.5 (lxml parser). Kept the container `div#article-body-transcript`. From it kept: the DATE paragraph, the CALL PARTICIPANTS list, and every `<p>` after the `<h2>Full Conference Call Transcript</h2>` header (99 paragraphs, Operator opening through Operator closing, 9 analyst questioners).
- Dropped: page navigation, ads, promo boxes (`div.article-body-promobox`, `div.my-8`), the "Image source: The Motley Fool." caption, the "Need a quote from a Motley Fool analyst?" line, and Fool's own editorial sections TAKEAWAYS, RISKS, SUMMARY, INDUSTRY GLOSSARY (these are Fool-written summaries, not call content).
- Whitespace collapsed; space-before-punctuation artifacts removed. No words changed. Transcription artifacts in the source (e.g. "$900 million" for share count, "sequential headroom ... -- the sequential headwind") were left as-is and flagged [sic] in the notes.
- Verified: text begins at the operator's introduction, includes prepared remarks by Murphy and Durn, and includes the full Q&A (Barclays, JPMorgan, BofA, Wells Fargo, Morgan Stanley, Melius, Cantor Fitzgerald, Goldman Sachs, Needham).

## Failures

- None. Tier 1 returned no transcript (expected). Tier 3 succeeded on first attempt.

## ir.md

# MANIFEST-ir — Marvell (MRVL), Q2 FY2027 (quarter ended 2026-08-01; results 2026-08-27)

Gatherer: ir (press release and slides). As-of cutoff 2026-08-28; all documents dated 2026-08-27. Fetched 2026-09-07. Only extracted text is cached; PDFs and HTML were downloaded to /tmp and not saved here.

Format: filename | origin URL | fetch date | word count | note on text quality

press-release.txt | https://www.sec.gov/Archives/edgar/data/1835632/000183563226000022/q227_8kx812026ex-991.htm (8-K Exhibit 99.1, accession 0001835632-26-000022, filed 2026-08-27 16:05:59; folder index https://www.sec.gov/Archives/edgar/data/1835632/000183563226000022/) | 2026-09-07 | 5093 | Good. HTML stripped with python3 BeautifulSoup (html.parser backend), table-aware: each table row emitted as one line with cells joined by " | ". Statement of operations, balance sheet, cash flow, all GAAP-to-non-GAAP reconciliations, Q3 FY2027 outlook reconciliation, and revenue-by-end-market tables all survived as readable rows and were cross-checked against slides and supplemental. No images/logo text lost that matters.

slides.txt | https://d1io3yog0oux5.cloudfront.net/_eac9f0b88f7114d6778a284aa60d5990/marvell/db/3734/35391/presentation/2026_08_27_Marvell_Q2_FY27_financial_business_results_FINAL+%281%29.pdf (linked from https://investor.marvell.com/financial-information/financial-results; PDF title "Financial and Business Results FY27 and Q2 FY27", 36 pages, created 2026-08-27) | 2026-09-07 | 3849 | Good for tables, fair for charts. pdftotext -layout. Footer page numbers 1–35 match p.N tags in notes-ir.md; p.36 blank. Summary P&L, balance sheet, end-market, outlook, and appendix reconciliation tables (p.15–17, 20–21, 24–35) are clean. Chart slides (p.10–14, 18–19) contain bar labels whose quarter assignment is inferred from reading order; on p.14 the capital-return stacked-bar segment labels cannot be reliably attributed (totals are). p.23 non-GAAP boilerplate has letter-spacing artifacts ("excl ude th e") but duplicates release text.

supplemental.txt | https://d1io3yog0oux5.cloudfront.net/_eac9f0b88f7114d6778a284aa60d5990/marvell/db/3734/35391/additional_earnings_information/MRVL+Q2%2727+Additional+Information_FINAL+v2.pdf (linked from https://investor.marvell.com/financial-information/financial-results; PDF title "Marvell Technology, Inc. Second Quarter and Fiscal Year 2027 Additional Information", 11 pages, created 2026-08-26) | 2026-09-07 | 3131 | Good. pdftotext -layout. Eight-quarter tables (balance sheets p.4, statements of operations p.5, cash flows p.6–7, GAAP-to-non-GAAP reconciliations p.8–9, quarterly revenue trend by end market p.10) are column-aligned and fully readable. p.11 blank. Contains no gross-margin-percentage line (gross profit and revenue only).

notes-ir.md | (written by ir gatherer from the three files above) | 2026-09-07 | 5850 | Structured bullets, every bullet tagged [Q2 FY2027 release], [Q2 FY2027 slides, p.N], or [Q2 FY2027 supplemental, p.N]; gatherer arithmetic labeled as such.

MANIFEST-ir.md | (this file) | 2026-09-07 | 393 | —

Not fetched / not available: no earnings-call transcript exists on the IR page or in the 8-K (transcript gatherer handles tier-3 source separately). No other exhibits in the 8-K folder besides the primary document mrvl-20260827.htm and Exhibit 99.1.

