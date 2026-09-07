# MANIFEST — GOOGL sources/2026-Q2

## filings.md

# MANIFEST — filings gatherer, Alphabet Inc. (GOOGL, CIK 0001652044), Q2 2026

Source tier: primary (SEC EDGAR). As-of cutoff 2026-07-23. Fetch date 2026-09-07. HTML stripped to text with python3 BeautifulSoup (lxml); inline-XBRL hidden header removed; block line breaks kept. No PDFs or raw HTML saved. Word counts via `wc -w`.

Format: `filename or accession | origin URL | fetch date | word count or classification`

| File / accession | Origin URL | Fetch date | Word count / classification |
|---|---|---|---|
| `10-Q-2026-Q2.txt` (acc 0001652044-26-000071, filed 2026-07-23, period 2026-06-30) | https://www.sec.gov/Archives/edgar/data/1652044/000165204426000071/goog-20260630.htm | 2026-09-07 | 31,712 words. Form 10-Q. Verified prose: `Item 2` MD&A present. |
| `8-K-2026-06-04.txt` (acc 0001193125-26-257724, filed 2026-06-04) | https://www.sec.gov/Archives/edgar/data/1652044/000119312526257724/d83560d8k.htm | 2026-09-07 | 1,893 words. NON-ROUTINE: $40B at-the-market equity distribution agreement; underwritten Class A/Class C common stock offering; $10B Berkshire Hathaway private placement. |
| `8-K-2026-06-05-preferred.txt` (acc 0001193125-26-259830, filed 2026-06-05) | https://www.sec.gov/Archives/edgar/data/1652044/000119312526259830/d36818d8k.htm | 2026-09-07 | 2,925 words. NON-ROUTINE: 6.25% Series A/B Mandatory Convertible Preferred Stock offering (385M depositary shares), capped calls, certificates of designations. |
| `8-K-2026-06-05-officer.txt` (acc 0001652044-26-000059, filed 2026-06-05, event date 2026-06-02) | https://www.sec.gov/Archives/edgar/data/1652044/000165204426000059/goog-20260602.htm | 2026-09-07 | 846 words. NON-ROUTINE: officer change — Marsida Saraci appointed Principal Accounting Officer (Item 5.02(c)). |
| acc 0001193125-26-216986 (8-K filed 2026-05-11) — not saved | https://www.sec.gov/Archives/edgar/data/1652044/000119312526216986/d109021d8k.htm | 2026-09-07 | 1,046 words read; ROUTINE debt offering closing: €9bn euro notes (6 tranches) and Canadian dollar notes (4 tranches; headline says C$9.5bn, tranches sum to C$8.5bn). Item 8.01. |
| acc 0001193125-26-234488 (8-K filed 2026-05-21) — not saved | https://www.sec.gov/Archives/edgar/data/1652044/000119312526234488/d144566d8k.htm | 2026-09-07 | 917 words read; ROUTINE debt offering closing: Japanese yen notes (7 tranches; headline says ¥576.9bn, tranches sum to ¥576.5bn). Item 8.01. |
| acc 0001193125-26-267578 (8-K filed 2026-06-11) — not saved | https://www.sec.gov/Archives/edgar/data/1652044/000119312526267578/d57679d8k.htm | 2026-09-07 | 1,460 words read; ROUTINE annual meeting vote tally (Item 5.07) plus approval of 2021 Stock Plan amendment adding 200,000,000 Class C shares to the reserve (Item 5.02). Key figures recorded in notes-filings.md §12. |
| 8-K filed 2026-07-22 (earnings release) — skipped | — | — | Handled by the ir gatherer per task instructions. |
| `notes-filings.md` | (this gatherer's output) | 2026-09-07 | 7,408 words (gatherer notes; not a fetched source) |

## Notes

- Two 8-Ks were filed on 2026-06-05, so the `8-K-<date>.txt` naming was extended with `-preferred` and `-officer` suffixes to keep both.
- User-Agent: EDGAR returned HTTP 403 "Your Request Originates from an Undeclared Automated Tool" for the prescribed UA `company-research-skill contact: owner@localhost` (retried once, same result). EDGAR accepted the same string with a top-level domain appended: `company-research-skill owner@localhost.com`. That UA was used for all seven fetches. Owner may want to put a real contact address in AGENTS.md §12.1.
- All seven fetches returned HTTP 200 on the first attempt with the accepted UA; no failures.
- Nothing in `sources/2026-Q1/` was read or modified.

## transcript.md

# MANIFEST — transcript gatherer, GOOGL, Q2 2026

_As-of cutoff: 2026-07-23. Call date: 2026-07-22. Only extracted text is cached; the PDF was downloaded to /tmp and not saved in the repo._

| file | origin URL | fetch date | source tier | word count |
|---|---|---|---|---|
| transcript.txt | https://s206.q4cdn.com/479360582/files/doc_events/2026/Jul/22/2026_Q2_Earnings_Transcript.pdf | 2026-09-07 | 1 company-published | 9107 |

Notes:
- Fetched with curl (-L, User-Agent "company-research-skill contact: owner@localhost"); HTTP 200; PDF 8 pages, 317,392 bytes; converted with `pdftotext -layout`.
- Verified: text begins with the operator's introduction ("Welcome, everyone. Thank you for standing by for the Alphabet Second Quarter 2026 Earnings Conference Call.") and contains a question-and-answer session with nine analysts (Morgan Stanley, JP Morgan, Goldman Sachs, Barclays, MoffettNathanson, Bernstein, Citi, Wells Fargo, Wolfe Research).
- Transcript header states: "This transcript is provided for the convenience of investors only, for a full recording please see the Q2 2026 Earnings Call webcast."
- Derived notes: notes-transcript.md (same folder).

## ir.md

# MANIFEST-ir — GOOGL Q2 2026 (IR gatherer: press release and slides)

Fetch method: `curl -L -A "company-research-skill contact: owner@localhost"` to /tmp, then `pdftotext -layout`; PDFs discarded, only text cached. As-of cutoff 2026-07-23; both documents are dated July 22, 2026 (release PDF metadata CreationDate 2026-07-22 19:20 UTC). Fallback (8-K 0001652044-26-000066 Exhibit 99.1) was not needed.

filename | origin URL | fetch date | word count | note on text quality
---|---|---|---|---
press-release.txt | https://s206.q4cdn.com/479360582/files/doc_financials/2026/q2/2026q2-alphabet-earnings-release.pdf | 2026-09-07 | 3,784 | 10 pages, HTTP 200, 140,593-byte PDF (Workiva, title "GOOG Exhibit 99.1 Q2 2026"). Clean layout extraction; all tables (highlights, supplemental revenue/TAC/headcount, segment results, balance sheet, income statement, cash flows, OI&E, FCF reconciliation, revenue by geography YoY and sequential) column-aligned and fully legible. UTF-8 curly quotes/dashes present. Page breaks kept as form feeds.
slides.txt | https://s206.q4cdn.com/479360582/files/doc_financials/2026/q2/2026q2-alphabet-earnings-slides.pdf | 2026-09-07 | 882 | 12 pages, HTTP 200, 2,149,527-byte PDF (title "Alphabet Q2 2026 Earnings Slides"). Sparse but usable: p.1 title, p.2 disclaimer, p.3 product-launch timeline (labels only, no numbers), p.4 six KPI tiles, p.5 income-statement table (clean), p.6–p.10 bar charts where data labels and axis captions extract but are positionally scattered (values still unambiguous: Q2'25 vs Q2'26 two-bar pages for revenue/OI, costs, Services, Cloud; five-quarter capex bars Q2'25–Q2'26 with Y/Y labels), p.11 five-quarter OCF/capex/FCF/TTM-FCF table (clean), p.12 eight-quarter FCF reconciliation table (clean). No depreciation, TPU, or Cloud-margin-trend page.
notes-ir.md | (derived from the two files above) | 2026-09-07 | 5,159 | Structured gatherer notes, every bullet tagged `[Q2 2026 release, p.N]` or `[Q2 2026 slides, p.N]`.

