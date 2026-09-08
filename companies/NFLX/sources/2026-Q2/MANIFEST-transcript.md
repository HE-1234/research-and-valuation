## transcript

# MANIFEST — transcript gatherer — Netflix, Inc. (NFLX, CIK 0001065280) — Q2 2026

As-of cutoff: 2026-07-17. Event: Netflix Second Quarter 2026 Earnings Interview, 2026-07-16, 1:45 pm PT (4:45 pm ET; S&P header "8:45 PM GMT"). Gatherer run: 2026-09-08.

Transcript source tier: 1, company-published (Netflix IR, Q4 Inc. CDN; S&P Global Market Intelligence transcript of the company's recorded earnings interview).

| file | origin URL | fetch date | source tier | word count |
|---|---|---|---|---|
| transcript.txt | https://s22.q4cdn.com/959853165/files/doc_financials/2026/q2/Netflix-Inc-_Earnings-Call_2026-07-16T00_00_00_English-1.pdf | 2026-09-08 | 1 company-published (Netflix IR, Q4 Inc. CDN; S&P Global Market Intelligence transcript) | 7565 |
| transcript-2026-Q1.txt | https://s22.q4cdn.com/959853165/files/doc_financials/2026/q1/Netflix-Inc-_Earnings-Call_2026-04-16T00_00_00_English-1.pdf | 2026-09-08 | 1 company-published (labelled supplement: Q1 2026 interview, 2026-04-16) | 9073 |
| transcript-2026-03-04-MS-conference.txt | https://s22.q4cdn.com/959853165/files/doc_events/2026/Mar/04/Netflix-Inc-_Company-Conference-Presentation_2026-03-04_English.pdf | 2026-09-08 | 1 company-published (labelled supplement: CFO Q&A, Morgan Stanley TMT Conference, 2026-03-04) | 7670 |
| notes-transcript.md | derived from the three files above (this gatherer); §9 cross-checked against shareholder-letter.txt cached by the IR gatherer; one FY2025 revenue figure from 10-K-FY2025.txt and the termination date from 8-K-2026-02-27.txt (filings gatherer) | 2026-09-08 | n/a | 9687 |

No reading-order copy was made: the S&P transcripts are single-column and the `pdftotext -layout` output reads in order (a plain `pdftotext` run was produced in scratch for comparison and differed only by three words of header spacing; it was not kept).

## Format note

Netflix does not hold a conventional earnings conference call. It publishes a shareholder letter and a pre-recorded video interview (YouTube, youtube/netflixir) in which Spencer Wang (VP Finance, Corporate Development & IR) reads questions submitted in writing by sell-side analysts to co-CEOs Ted Sarandos and Greg Peters and CFO Spencer Neumann. No analyst speaks and there is no operator. The company posts an S&P Global Market Intelligence transcript of that interview on its IR site; that company-posted PDF is treated as tier 1, company-published. Ten analysts' questions were read (Cahall/Wells Fargo, Sanderson/Loop Capital, Joyce/Seaport, Kesavabhotla/Baird, Fishman/MoffettNathanson, Greenfield/LightShed, Hodulik/UBS, Diffley/Morgan Stanley, Reif Ehrlich/Bank of America, Kurnos/StoneX). The only "prepared remarks" are Wang's three-sentence introduction (p.4).

## Discovery path

- Financial-report feed (re-fetched 2026-09-08, HTTP 200, 5,109 bytes): `https://ir.netflix.net/feed/FinancialReport.svc/GetFinancialReportList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1&reportSubType=`. Entry "Second Quarter 2026" (ReportDate 06/30/2026) lists four documents: "Video Interview" (YouTube embed, not fetched), "Letter to Shareholders" (PDF, IR gatherer), "Financial Statements" (XLSX, IR gatherer) and "Transcript" (the PDF URL above). Entry "First Quarter 2026" lists the same four types; its "Transcript" is the Q1 URL above.
- Event feed (re-fetched 2026-09-08, HTTP 200, 9,169 bytes): `https://ir.netflix.net/feed/Event.svc/GetEventList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=2026&excludeSelection=1&eventDateFilter=All`. Entries: "Netflix Fourth Quarter 2025 Earnings Interview" (01/20/2026 13:45), "Netflix CFO to Participate in a Q&A session at the Morgan Stanley Technology, Media & Telecom Conference" (03/04/2026 13:50, webcast link only), "Netflix First Quarter 2026 Earnings Interview" (04/16/2026 13:45), "Annual Meeting of Stockholders" (06/04/2026 15:00), "Netflix Second Quarter 2026 Earnings Interview" (07/16/2026 13:45). The feed labels times "PST"; they are Pacific local time. The event entries carry no transcript attachments; the transcripts are in the financial-report feed, and the MS conference transcript URL (doc_events path above) was supplied by the orchestrator and verified by fetch.
- `ir.netflix.net` HTML pages were not fetched (they return 403). Fallback tiers (8-K exhibits, Motley Fool) were not needed and were not fetched.

## Fetch and conversion

- All three PDFs fetched with `curl -L -A "company-research-skill owner@example.com"` on 2026-09-08, HTTP 200, content-type application/pdf: Q2 interview 382,801 bytes; Q1 interview 389,798 bytes; MS conference 162,485 bytes. Saved to /tmp/nflx-orch/transcript/, converted, and deleted after conversion. No PDF was saved into the repo (verified with `find`).
- `pdfinfo`, Q2 interview: 14 pages, letter size, PDF 1.7, Creator "Aspose Ltd.", Producer "Aspose.Pdf for .NET 7.0", Title/Author empty, CreationDate 2026-07-16 19:07:59 UTC, ModDate 2026-07-16 19:08:00 UTC (= 12:07 pm PT on the interview day, i.e. the transcript file was generated before the 1:45 pm PT posting time; the interview is pre-recorded), not encrypted.
- `pdfinfo`, Q1 interview: 15 pages, same producer, CreationDate = ModDate 2026-04-16 17:48:38 UTC. S&P's running header marks it "PRELIMINARY COPY".
- `pdfinfo`, MS conference: 13 pages, same producer, CreationDate = ModDate 2026-03-04 19:24:50 UTC.
- Converted with `pdftotext -layout`. transcript.txt 7,565 words / 618 lines / 48,740 bytes; transcript-2026-Q1.txt 9,073 words / 694 lines / 56,774 bytes; transcript-2026-03-04-MS-conference.txt 7,670 words / 567 lines / 45,697 bytes. The S&P header block (title, date/time, "S&P Global Market Intelligence Estimates" consensus table on p.1, contents on p.2, participants on p.3) and the legal page at the end are kept in the cached text; the consensus EPS/revenue figures are S&P's, not the company's, and are not used as facts.
- Page-number convention: YES, printed page numbers. Each page carries its number at the foot (right-aligned, after the S&P copyright line). Verified programmatically for all three files that printed page N sits on PDF page N (Q2: 1–14; Q1: 1–15; MS: 1–13), so `p.N` tags in notes-transcript.md are unambiguous under either reading. Q&A text: Q2 p.5–13, Q1 p.5–14, MS p.5–12.
- Text quality: single column; no hyphenation splits; straight apostrophes only (no curly characters in the transcripts); spoken breaks rendered as "--"; S&P editorial marks "[indiscernible]", "(sic) [ ... ]" and bracketed uncertain names ("[ Dan Kurnos ]") left as is.

## Cache reuse (AGENTS.md §12.4)

- `transcript.txt` (7,565 words) and `transcript-2026-03-04-MS-conference.txt` (7,670 words) were already present from an earlier interrupted run. Both PDFs were re-fetched and re-converted; `cmp` and `diff` against the cached files reported byte-identical output. Both cached files were kept unchanged: reused from cache, verified identical to a fresh conversion.
- `transcript-2026-Q1.txt` was not in the cache and was created from the fresh conversion.

## Cross-check and as-of discipline

- Every number spoken in the Q2 interview was checked against `shareholder-letter.txt` (notes §9). No contradiction. One spoken figure not in the letter, "an incremental 1.5 billion hours" for H1 2026 view-hour growth, does not reconcile with the letter's ">97 billion hours, up 2%" (about 1.9B implied) and is flagged; the report should use the letter's figures. Three items that look like management numbers were analyst wording ("0 billion cash content budget", "approximately 330 million subscription households") and are marked as such.
- 117 quotation fragments in notes-transcript.md were machine-checked for verbatim presence in the cached source text (whitespace-normalised); all pass.
- Nothing published after 2026-07-17 was fetched or used. Documents read: the two JSON feed listings (2026 entries only; the feeds list events by date and none after 07/16/2026 was opened), the three PDFs dated 2026-03-04, 2026-04-16 and 2026-07-16, and for cross-checking the already-cached `shareholder-letter.txt` (2026-07-16), `shareholder-letter-2026-Q1.txt` (2026-04-16), `8-K-2026-02-27.txt` and one line of `10-K-FY2025.txt`.
- Not produced by this gatherer: `shareholder-letter.txt`, `shareholder-letter-2026-Q1.txt`, `financials-xlsx.txt`, the 10-K / 10-Q / 8-K / DEF 14A text files and any `notes-ir.md` / `notes-filings.md`; they belong to the IR and filings gatherers.
- Scratch left in /tmp/nflx-orch/transcript/: the two feed JSON files and the six pdftotext outputs (layout and reading-order) used for comparison; no PDFs.
