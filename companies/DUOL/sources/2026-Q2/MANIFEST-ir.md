# MANIFEST-ir.md — Duolingo, Inc. (DUOL), Q2 2026 — ir gatherer part

Company: Duolingo, Inc., CIK 0001562088 (EDGAR path `1562088`), Nasdaq: DUOL. Fiscal year = calendar year.
As-of quarter Q2 2026 (ended 2026-06-30); cutoff 2026-08-06. Gatherer run date: 2026-09-08.
Duolingo publishes no slide deck; the shareholder letter (8-K Exhibit 99.2) is the slides-equivalent, so there is no `slides.txt`.

## Files

| File | Origin URL | Fetch date / reuse | Document date | Words |
|---|---|---|---|---|
| `press-release.txt` (Q2 2026 release, 8-K EX-99.1) | https://www.sec.gov/Archives/edgar/data/1562088/000162828026053299/q2fy26duolingo6-30x26xpres.htm | reused (fetched 2026-09-08 20:45:38 by the prior interrupted run, HTTP 200, 9,939 bytes); verified 2026-09-08: starts at the exhibit header and title "Duolingo Reports Second Quarter 2026 Results", ends at Contacts (Deborah Belevan / Michelle Scully) and page footer "2"; two pages complete | 2026-08-05 | 741 |
| `shareholder-letter.txt` (Q2 2026 shareholder letter, 8-K EX-99.2) | https://www.sec.gov/Archives/edgar/data/1562088/000162828026053299/q2fy26duolingo6-30x26share.htm | reused (fetched 2026-09-08 20:45:41, HTTP 200, 265,498 bytes); verified 2026-09-08: title through Contacts (footer "DUOLINGO Q2 2026 23"); page footers 2–23 present except divider pages 7 and 18; highlights table, summary table, Q3/FY guidance table, balance sheet, income statement, six-month cash flow, revenue by product type, Adjusted EBITDA / opex / FCF reconciliations all present with cells joined " \| " | 2026-08-05 | 5,564 |
| `press-release-2026-Q1.txt` (Q1 2026 release, EX-99.1) | https://www.sec.gov/Archives/edgar/data/1562088/000162828026029790/q1fy26duolingo3-31x26xpres.htm | reused (fetched 2026-09-08 20:45:43, HTTP 200, 10,150 bytes); verified 2026-09-08: title "Duolingo Reports First Quarter 2026 Results" through Contacts (Deborah Belevan / Monica Earle), footer "2" | 2026-05-04 | 770 |
| `shareholder-letter-2026-Q1.txt` (Q1 2026 letter, EX-99.2) | https://www.sec.gov/Archives/edgar/data/1562088/000162828026029790/q1fy26duolingo3-31x26share.htm | reused (fetched 2026-09-08 20:45:46, HTTP 200, 270,470 bytes); verified 2026-09-08: title through Contacts (footer "DUOLINGO Q1 / FY 2026 24"); footers 2–24 present except divider pages 7 and 19; highlights, summary, Q2/FY guidance table, three GAAP statements, revenue by type, all reconciliations present | 2026-05-04 | 5,432 |
| `press-release-2025-Q4.txt` (Q4 / FY2025 release, EX-99.1) | https://www.sec.gov/Archives/edgar/data/1562088/000162828026012246/q4fy25duolingo12-31x25pres.htm | fetched 2026-09-08 22:15:10 (HTTP 200, 12,265 bytes); title "Duolingo Reports Fourth Quarter and Full Year 2025 Results / Announces Authorization of $400 Million Share Repurchase Program" through Contacts, footer "2" | 2026-02-26 | 1,007 |
| `shareholder-letter-2025-Q4.txt` (Q4 / FY2025 letter, EX-99.2) | https://www.sec.gov/Archives/edgar/data/1562088/000162828026012246/q4fy25duolingo12-31x25shar.htm | fetched 2026-09-08 22:15:12 (HTTP 200, 296,737 bytes); title through Contacts (footer "DUOLINGO Q4 / FY 2025 23"); footers 2–23 present except divider pages 7 and 19; highlights (Q4 and FY), summary table (Q4 and FY columns), Q1/FY2026 guidance table, condensed balance sheet, income statement (Q4 and FY), FY cash flow, Adjusted EBITDA / opex / FCF reconciliations (Q4 and FY) present. No revenue-by-product-type table exists in this letter. | 2026-02-26 | 6,604 |
| `notes-ir.md` | written by this gatherer | 2026-09-08 | — | 9,723 |
| `MANIFEST-ir.md` | this file | 2026-09-08 | — | — |

Not produced: `slides.txt` (no deck exists); `shareholder-letter-pdf.txt` (no PDF obtained; IR site blocked, see below).

Exhibit indices used to resolve filenames (all fetched by the orchestrator/prior run on 2026-09-08 20:39, cached as `/tmp/duol-orch/idx-<accession>.html`):
- Q2 2026 8-K, accession 0001628280-26-053299, filed 2026-08-05: https://www.sec.gov/Archives/edgar/data/1562088/000162828026053299/0001628280-26-053299-index.htm
- Q1 2026 8-K, accession 0001628280-26-029790, filed 2026-05-04: https://www.sec.gov/Archives/edgar/data/1562088/000162828026029790/0001628280-26-029790-index.htm
- Q4 2025 8-K, accession 0001628280-26-012246, filed 2026-02-26: https://www.sec.gov/Archives/edgar/data/1562088/000162828026012246/0001628280-26-012246-index.htm (EX-99.1 `q4fy25duolingo12-31x25pres.htm`, EX-99.2 `q4fy25duolingo12-31x25shar.htm`; the 8-K body `duol-20260226.htm` belongs to the filings gatherer and was not re-fetched here).

## Fetch log

**SEC (www.sec.gov)** — User-Agent exactly `company-research-skill owner@example.com`, `Accept-Encoding: identity`, 2.2 s sleep after every request, back-off schedule 10/30/120 s armed for 403/429 (never triggered).
- This gatherer: 2 requests, 2026-09-08 22:15:10 and 22:15:12 UTC-local, both HTTP 200 (12,265 and 296,737 bytes). Script `/tmp/duol-orch/ir-fetch-q4.py`; log `/tmp/duol-orch/ir-fetch-log.txt`.
- Prior interrupted run (reused files): 4 requests 2026-09-08 20:45:38–20:45:46, all HTTP 200, ≥2.2 s apart. Script `/tmp/duol-orch/fetch_sec.py`; log `/tmp/duol-orch/fetch-log-sec.txt`.
- No 403 or 429 from SEC at any point.

**IR site (investors.duolingo.com, Q4 Inc.-hosted, Akamai edge)** — browser UA `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36`, headers `Accept: application/json`, `Referer: https://investors.duolingo.com/`.
- 2026-09-08 22:15:27: `https://investors.duolingo.com/feed/FinancialReport.svc/GetFinancialReportList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1&reportSubType=` → HTTP 403, 440-byte Akamai "Access Denied" page (reference on errors.edgesuite.net).
- back-off 10 s; 22:15:37: same URL → HTTP 403 (same Access Denied page). Stopped per brief (one back-off cycle).
- Context: the orchestrator's probe with the SEC UA (20:39) and the transcript gatherer's probe (22:13) of the FinancialReport feed, the Event feed, `/events-and-presentations/default.aspx`, `/financials/quarterly-results/default.aspx`, `/events-and-presentations/events/default.aspx` and the root all returned the same 403 with the browser UA, with and without Accept/Referer. Duolingo blocks even the Q4 JSON feeds (like Broadcom, unlike GOOGL/META/PINS/MU). No `s<NNN>.q4cdn.com` document URL could be discovered, so no letter PDF was fetched. The 8-K exhibits are the reliable path.

**Conversion** — HTML → text with Python BeautifulSoup (lxml parser): `<script>`, `<style>`, `<head>`, `ix:header` and `display:none` elements dropped; each `<tr>` rendered as one line with non-empty cells joined by " | "; `<br>` and block elements become line breaks; `&nbsp;` → space; runs of blank lines collapsed to one. Raw HTML was written to `/tmp/duol-orch/` and deleted immediately after conversion; only text is cached. No PDFs were involved (no `pdftotext`). The first five lines of every exhibit file ("EX-99.x", sequence number, filename, "EX-99.x", "Document") are the EDGAR exhibit wrapper, not Duolingo content.

**Page numbers** — Duolingo's letters print a footer "DUOLINGO Q2 2026 N" (Q1: "DUOLINGO Q1 / FY 2026 N"; Q4: "DUOLINGO Q4 / FY 2025 N") at the bottom of each page; the HTML preserves it as a standalone line. Because the last footer (23 or 24) follows the Contacts block, the footer closes its page, so all text between footer N−1 and footer N is page N. The cover (p.1) has no footer. Section-divider pages carry no footer (Q2: p.7 "financial performance and outlook", p.18 "appendix"; Q1: p.7, p.19; Q4: p.7, p.19), so a two-page gap between consecutive footers was split with the divider heading on the lower page and the following table on the higher page. `p.N` tags in `notes-ir.md` therefore equal the printed page numbers of the PDF letter, derived from the HTML footers; they were not checked against a PDF because none could be fetched.

**Structure verification** — For each of the six files: head shows the exhibit wrapper plus the document title; tail shows the Contacts block and final page footer; `grep` confirmed the guidance heading and table, the three GAAP statements, the "Reconciliation:" headings (Adjusted EBITDA, opex, R&D, S&M, G&A, FCF), and the footnote block; footers enumerated to confirm no page is missing apart from the dividers. Tables were spot-read (highlights, summary, guidance, revenue by type, reconciliations) and every cell was legible as " | "-joined text. A scan for numeric or short fragments found no chart-label residue: the letters embed no data charts (exhibit indices list only page-2 artwork, one illustration per letter, logos, headshots and signatures).

**As-of** — Only documents dated on or before 2026-08-06 were fetched or read: the 2026-08-05, 2026-05-04 and 2026-02-26 8-K exhibits. The submissions JSON lists 8-Ks filed 2026-08-10 and 2026-08-19; they were not fetched and not read. The Q2 letter itself reports buyback activity "through August 1, 2026", which is pre-cutoff and was recorded.

**No git commands were run.** Files written only inside `/home/ubuntu/finance/companies/DUOL/sources/2026-Q2/` (six source files, `notes-ir.md`, this manifest); scratch only in `/tmp/duol-orch/` (`ir-fetch-q4.py`, `ir-fetch-log.txt`, `ir-q4ne.txt`, `ir-feed-fr-2026.body`, `ir-feed.err`).
