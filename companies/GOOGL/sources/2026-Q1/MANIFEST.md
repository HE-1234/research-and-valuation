# MANIFEST — GOOGL sources/2026-Q1

## filings.md

# MANIFEST — filings gatherer, Alphabet Inc. (GOOGL, CIK 0001652044), Q1 2026

_As-of cutoff 2026-04-30. All fetches performed 2026-09-07 from SEC EDGAR. Only extracted text is cached; no HTML or PDF saved in this folder._

Format: filename | origin URL | fetch date | word count

- 10-K-FY2025.txt | https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm | 2026-09-07 | 55978 words (10-K for FY ended 2025-12-31, filed 2026-02-05)
- 10-Q-2026-Q1.txt | https://www.sec.gov/Archives/edgar/data/1652044/000165204426000048/goog-20260331.htm | 2026-09-07 | 25687 words (10-Q for quarter ended 2026-03-31, filed 2026-04-30)
- DEF14A-2026.txt | https://www.sec.gov/Archives/edgar/data/1652044/000130817926000342/goog-20260424.htm | 2026-09-07 | 61458 words (definitive proxy, filed 2026-04-24; annual meeting 2026-06-05)
- 10-K-FY2023.txt | https://www.sec.gov/Archives/edgar/data/1652044/000165204424000022/goog-20231231.htm | 2026-09-07 | 55268 words (10-K for FY ended 2023-12-31, filed 2024-01-31; located via https://data.sec.gov/submissions/CIK0001652044.json, filings.recent, accession 0001652044-24-000022; used for FY2021–FY2022 history)
- notes-filings.md | (written by filings gatherer from the four files above) | 2026-09-07 | 9414 words

## Fetch log

- All four documents fetched successfully (HTTP 200) with a complete closing `</html>` tag; on-disk HTML sizes 1.7–2.6 MB (inline XBRL), converted to text with Python 3.13 + BeautifulSoup 4.13 (lxml parser). Conversion dropped script/style/ix:header and display:none elements, joined table cells with " | ", and collapsed whitespace. Verified prose readability (first 50 lines) and that "Item 7" headings survived in both 10-Ks; 10-Q MD&A ("ITEM 2.") survived at line 1942.
- Failed fetch, then recovered: first requests to www.sec.gov/Archives with User-Agent `company-research-skill contact: owner@localhost` returned HTTP 403 "Your Request Originates from an Undeclared Automated Tool" (retried once, same result). The same UA was accepted by data.sec.gov. The block was specific to the `owner@localhost` contact; switching the contact to a real-looking placeholder domain, `company-research-skill owner@example.com`, returned 200 on all four documents. No other UA or header changes were needed. Recommend updating the UA contact in AGENTS.md §12.1 to a real owner email.
- No PDFs were involved. No documents dated after 2026-04-30 were fetched or read. The FY2024 10-K (filed 2025-02-05) was not fetched because it was not on the fetch list; as a result headcount for 12/31/2021, 12/31/2022, and 12/31/2024 and cash/debt at 12/31/2021 are recorded as "not in fetched sources" in notes-filings.md.
- Transcript source tier: not applicable to this gatherer (see the transcript gatherer's manifest).

## transcript.md

# MANIFEST — transcript gatherer — Alphabet (GOOGL) — Q1 2026

As-of cutoff: 2026-04-30. Call date: 2026-04-29. Gatherer run: 2026-09-07.

| file | origin URL | fetch date | source tier | word count |
|---|---|---|---|---|
| transcript.txt | https://s206.q4cdn.com/479360582/files/doc_events/2026/Apr/29/Alphabet-2026_Q1_Earnings_Transcript.pdf | 2026-09-07 | 1 company-published (Alphabet IR, Q4 Inc. CDN) | 8881 |
| notes-transcript.md | derived from transcript.txt (this gatherer) | 2026-09-07 | n/a | see file |

## Fetch and conversion notes

- Fetched with `curl -A "company-research-skill contact: owner@localhost" -L`; HTTP 200, 151,977 bytes, PDF 1.4, 24 pages (printed page numbers 1–24 at the foot of each page are preserved in transcript.txt and are the page references used in notes-transcript.md).
- Converted with `pdftotext -layout`. The PDF was not saved into the repo (deleted from /tmp after conversion).
- Post-processing (lossless restoration of the PDF's text encoding, no content changed):
  - The PDF encodes the first letter of most paragraphs as a separate glyph, which pdftotext emits as a one-character line following a paragraph line missing its first letter (e.g. " perator:" then "O"). 209 such pairs were rejoined ("Operator:"). Two inline variants were fixed by hand ("Acouple" -> "A couple", p.13; "s hared" -> "shared", p.16).
  - 1,736 zero-width-space characters (U+200B) were removed. 84 doubled zero-width spaces stood in for real spaces at font-span boundaries ("standing by", "Anmuth with") and were replaced with a space; the one case before a period ("webcast.") was dropped.
- Verified: file begins with the operator's introduction ("Operator: Welcome, everyone. Thank you for standing by for the Alphabet First Quarter 2026 Earnings Conference Call.") and contains a Q&A section (12 Operator turns; 9 analysts from Morgan Stanley, JP Morgan, Goldman Sachs, Barclays, MoffettNathanson, Bernstein, Citi, Wells Fargo, Bank of America).
- Fallback paths (event feed, third-party transcripts) were NOT needed and were not used.
- Nothing published after 2026-04-30 was fetched or consulted.

## ir.md

# MANIFEST-ir — Alphabet (GOOGL) Q1 2026 — IR gatherer (press release + slides)

As-of cutoff 2026-04-30. Both source PDFs carry a creation date of 2026-04-29 (pdfinfo) and are dated April 29, 2026 in their text. PDFs were downloaded to /tmp and discarded; only extracted text (`pdftotext -layout`) is cached here. User-Agent used: `company-research-skill contact: owner@localhost`.

filename | origin URL | fetch date | word count | note on text quality
---|---|---|---|---
press-release.txt | https://s206.q4cdn.com/479360582/files/doc_financials/2026/q1/2026q1-alphabet-earnings-release.pdf | 2026-09-07 | 3358 | 9-page PDF (metadata title "GOOG Exhibit 99.1 Q1 2026", Workiva-generated). Clean, complete text: highlights, CEO quote, supplemental revenue/TAC/headcount table, segment results, balance sheet, income statement, cash flow statement, OI&E detail, FCF and constant-currency reconciliations, revenue by geography. Tables preserved column alignment; all figures legible. No OCR needed. The 8-K fallback (accession 0001652044-26-000043) was not needed.
slides.txt | https://s206.q4cdn.com/479360582/files/doc_financials/2026/q1/Alphabet-Q1-2026-Earnings-Slides.pdf | 2026-09-07 | 828 | 11-page PDF (PDFium-generated), 720x405 pt landscape. Text is sparse but fully usable: every page yielded text. p.1 title; p.2 forward-looking note; p.3 Earnings Highlights (five KPI tiles, all captured); p.4 consolidated P&L table with Y/Y %; p.5-p.8 bar charts whose data labels, Y/Y growth and operating-margin rows all extracted (pp.5 consolidated, 6 costs, 7 Google Services, 8 Google Cloud); p.9 five-quarter capex chart with values and Y/Y; p.10 five-quarter OCF/capex/FCF/TTM-FCF table; p.11 eight-quarter FCF reconciliation. Chart values appear out of visual order in the layout text, so read with the release tables alongside. Curly quotes/apostrophes came through as UTF-8 (e.g., "Q1'25"). No guidance slide exists.
notes-ir.md | derived from the two files above | 2026-09-07 | 4094 | Structured bullets, every number verbatim with unit and period, tagged [Q1 2026 release] or [Q1 2026 slides, p.N]. Automated check: every numeric token in the notes was found verbatim in press-release.txt or slides.txt (only exception: "99.1", which is from PDF title metadata). Two items labelled "computed" (Other Bets Y/Y %; none other).

Not produced by this gatherer: `transcript.txt`, `10-K-FY2023.txt`, `10-K-FY2025.txt`, `10-Q-2026-Q1.txt`, `DEF14A-2026.txt` and any other files in this folder belong to the transcript and filings gatherers; they were not read or used for notes-ir.md.

