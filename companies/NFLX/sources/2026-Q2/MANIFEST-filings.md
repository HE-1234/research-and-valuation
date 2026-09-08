# MANIFEST part — filings gatherer (NFLX, as of Q2 2026)

Written 2026-09-08. As-of cutoff 2026-07-17. All fetches on 2026-09-08 with User-Agent `company-research-skill owner@example.com`, at least 2.5 s apart. HTML was converted to text with Python (BeautifulSoup + lxml: script/style/head and `display:none` elements dropped, table cells joined with " | ", line breaks at block elements); binaries were downloaded to `/tmp/nflx-orch/filings/` and deleted after conversion. No HTML or PDF is stored in the repo.

## Files written or verified

| File | Origin URL | Fetch date | Filing date; period | Words | Status |
|---|---|---|---|---|---|
| 10-K-FY2025.txt | https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/nflx-20251231.htm | 2026-09-08 (earlier interrupted run, same day) | 2026-01-23; FY2025 (statements 2023–2025) | 43,893 | reused from cache (verified: Item 1, 1A, 7, 7A, 8 headings present in body; Notes 1–14 headings found; cash flow, balance sheet, equity statement and Exhibit Index present; ends with signature block dated January 23, 2026) |
| 10-K-FY2024.txt | https://www.sec.gov/Archives/edgar/data/1065280/000106528025000044/nflx-20241231.htm | 2026-09-08 (earlier run) | 2025-01-27; FY2024 | 40,938 | reused from cache (verified: Items 1/1A/7/8, Notes to Consolidated Financial Statements, Segment note, Exhibit Index, signatures dated January 27, 2025) |
| 10-K-FY2023.txt | https://www.sec.gov/Archives/edgar/data/1065280/000106528024000030/nflx-20231231.htm | 2026-09-08 (earlier run) | 2024-01-26; FY2023 (statements 2021–2023) | 38,276 | reused from cache (verified as above; signatures dated January 26, 2024) |
| 10-K-FY2022.txt | https://www.sec.gov/Archives/edgar/data/1065280/000106528023000035/nflx-20221231.htm | 2026-09-08 | 2023-01-26; FY2022 (statements 2020–2022) | 35,062 | refetched this run (addition to the brief; verified Items 1/1A/7/8, Notes, Exhibit Index, signatures dated January 26, 2023) |
| 10-Q-2026-Q2.txt | https://www.sec.gov/Archives/edgar/data/1065280/000106528026000212/nflx-20260630.htm | 2026-09-08 (earlier run) | 2026-07-17; quarter ended 2026-06-30 | 21,043 | reused from cache (verified: Part I Items 1–4 incl. Notes 1–12 and Item 2 MD&A, Part II Items 1–6, Exhibit Index, signatures dated July 17, 2026) |
| DEF14A-2026.txt | https://www.sec.gov/Archives/edgar/data/1065280/000119312526159286/d20613ddef14a.htm | 2026-09-08 (earlier run) | 2026-04-16; annual meeting 2026-06-04 | 41,709 | reused from cache (verified: table of contents, Who We Are, CD&A, Summary Compensation Table, Security Ownership, Stockholder Proposals, proxy card at the tail) |
| 8-K-2025-01-21.txt | https://www.sec.gov/Archives/edgar/data/1065280/000106528025000033/nflx-20250121.htm | 2026-09-08 | 2025-01-21; Items 2.02, 8.01 | 790 | refetched this run (Exhibit 99.1 letter not fetched: ir gatherer) |
| 8-K-2025-04-17.txt | https://www.sec.gov/Archives/edgar/data/1065280/000106528025000175/nflx-20250411.htm | 2026-09-08 | 2025-04-17; Items 2.02, 5.02 | 765 | refetched this run |
| 8-K-2025-06-06.txt | https://www.sec.gov/Archives/edgar/data/1065280/000106528025000286/nflx-20250605.htm | 2026-09-08 | 2025-06-06; Item 5.07 | 975 | refetched this run |
| 8-K-2025-06-24.txt | https://www.sec.gov/Archives/edgar/data/1065280/000106528025000287/nflx-20250622.htm | 2026-09-08 | 2025-06-24; Items 5.02, 8.01 | 1,299 | refetched this run |
| 8-K-2025-10-30.txt | https://www.sec.gov/Archives/edgar/data/1065280/000106528025000407/nflx-20251030.htm | 2026-09-08 (earlier run) | 2025-10-30; Item 8.01 | 572 | reused from cache (verified: Item 8.01 text and signature) |
| 8-K-2025-11-04.txt | https://www.sec.gov/Archives/edgar/data/1065280/000106528025000408/nflx-20251030.htm | 2026-09-08 (earlier run) | 2025-11-04; Item 5.02 | 1,722 | reused from cache (verified) |
| 8-K-2025-11-14.txt | https://www.sec.gov/Archives/edgar/data/1065280/000106528025000450/nflx-20251114.htm | 2026-09-08 (earlier run) | 2025-11-14; Item 5.03 | 534 | reused from cache (verified) |
| 8-K-2025-12-05.txt | https://www.sec.gov/Archives/edgar/data/1065280/000119312525308651/d65144d8k.htm | 2026-09-08 (earlier run) | 2025-12-05; Items 1.01, 7.01 | 5,884 | reused from cache (verified: full Item 1.01 through signature) |
| 8-K-2025-12-05-A.txt | https://www.sec.gov/Archives/edgar/data/1065280/000119312525309911/d45027d8ka.htm | 2026-09-08 (earlier run) | 2025-12-05; 8-K/A Item 9.01 | 2,005 | reused from cache (verified) |
| 8-K-2025-12-22.txt | https://www.sec.gov/Archives/edgar/data/1065280/000119312525327462/d82688d8k.htm | 2026-09-08 (earlier run) | 2025-12-22; Items 1.01, 2.03 | 3,267 | reused from cache (verified) |
| 8-K-2026-01-20.txt | https://www.sec.gov/Archives/edgar/data/1065280/000119312526015951/d37713d8k.htm | 2026-09-08 (earlier run) | 2026-01-20; Items 1.01, 7.01 (agent-filed WBD amendment; not the same-day Item 2.02 8-K) | 6,302 | reused from cache (verified) |
| 8-K-2026-02-27.txt | https://www.sec.gov/Archives/edgar/data/1065280/000119312526082247/d120618d8k.htm | 2026-09-08 (earlier run) | 2026-02-27; Item 1.02 | 1,121 | reused from cache (verified) |
| 8-K-2026-04-16.txt | https://www.sec.gov/Archives/edgar/data/1065280/000106528026000137/nflx-20260410.htm | 2026-09-08 (earlier run) | 2026-04-16; Items 2.02, 5.02 | 707 | reused from cache (verified) |
| 8-K-2026-04-23.txt | https://www.sec.gov/Archives/edgar/data/1065280/000106528026000139/nflx-20260422.htm | 2026-09-08 (earlier run) | 2026-04-23; Item 8.01 | 541 | reused from cache (verified) |
| 8-K-2026-06-05.txt | https://www.sec.gov/Archives/edgar/data/1065280/000106528026000189/nflx-20260604.htm | 2026-09-08 (earlier run) | 2026-06-05; Items 5.07, 8.01 | 931 | reused from cache (verified) |
| notes-filings.md | (written by this gatherer) | 2026-09-08 | — | see file | new |
| MANIFEST-filings.md | (this file) | 2026-09-08 | — | — | new |

Scanned in the submissions JSON but deliberately not cached (bare Item 2.02 earnings 8-Ks whose Exhibit 99.1 letters belong to the ir gatherer): 8-K 2025-07-17 (0001065280-25-000322), 8-K 2025-10-21 (0001065280-25-000404), 8-K 2026-01-20 (0001065280-26-000033), 8-K 2026-07-16 (0001065280-26-000211). Every 8-K and 8-K/A filed 2025-01-01 through 2026-07-17, including those under the filing-agent prefix 0001193125, was reviewed.

## Fetch log (this run)

- Requests to SEC: 6. (1) `https://data.sec.gov/submissions/CIK0001065280-submissions-001.json` (older submissions index, needed to locate the FY2022 10-K accession) → HTTP 200; (2) FY2022 10-K → 200; (3) 8-K 2025-06-24 → 200; (4) 8-K 2025-06-06 → 200; (5) 8-K 2025-04-17 → 200; (6) 8-K 2025-01-21 → 200. No 403 or 429; no backoff needed. Per-request log at `/tmp/nflx-orch/filings/fetch_log.txt`. The main submissions JSON was read from `/tmp/nflx-orch/submissions.json` (fetched by the orchestrator), not re-requested.
- The 16 pre-existing cache files came from an earlier interrupted run on 2026-09-08 (its log at `/tmp/nflx-orch/filings/fetchlog.txt` shows HTTP 200 and "html complete=True" for each, converted with bs4+lxml). Each was verified as described in the table before reuse.
- Verification of headings: every 10-K contains body occurrences of "Item 1.Business", "Item 1A.Risk Factors", "Item 7.", "Item 8." and "NOTES TO CONSOLIDATED FINANCIAL STATEMENTS" with the segment note and the Exhibit Index, and ends with the director signature block; the 10-Q contains "Notes to Consolidated Financial Statements (unaudited)" with Notes 1–12, Item 2 MD&A, Part II and the July 17, 2026 signatures.
- Deviations from the brief: (a) the FY2022 10-K was fetched in addition to the listed filings, to fill the 12/31/2021 balance sheet, 2021 content obligations and 2022 headcount (FY2021 regional revenue and memberships were already in the FY2023 10-K, so it was not required for that table); (b) the four 2025 8-Ks with non-earnings items were cached as primary documents only (no exhibits). Nothing else was fetched.
- Nothing filed after 2026-07-17 was fetched, read, or used.
- No git state was changed; nothing outside `companies/NFLX/sources/2026-Q2/` and `/tmp/nflx-orch/filings/` was written. The ir and transcript gatherers' files in the folder were not opened or modified.
