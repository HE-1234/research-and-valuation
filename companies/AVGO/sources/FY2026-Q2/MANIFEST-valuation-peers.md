# AVGO valuation peer source manifest

_Gatherer run 2026-09-18; valuation cutoff 2026-06-09. Only extracted text is saved. No report or assumption files changed._

| File / reused path | Original URL | Filing date | Fetched / reused | Role and limitations |
|---|---|---|---|---|
| `QCOM-10-K-FY2025.txt` | https://www.sec.gov/Archives/edgar/data/804328/000080432825000085/qcom-20250928.htm | 2025-11-05 | Fetched 2026-09-18 | Mature fabless comparison; full primary filing, HTTP 200, 1,878,948 bytes, 65,209 extracted words. FY2023–FY2025 income/cash flows and FY2024–FY2025 balance sheets. |
| `CSCO-10-K-FY2025.txt` | https://www.sec.gov/Archives/edgar/data/858877/000085887725000111/csco-20250726.htm | 2025-09-03 | Fetched 2026-09-18 | Mature networking/software comparison; full primary filing, HTTP 200, 3,528,914 bytes, 75,426 extracted words. FY2023–FY2025 income/cash flows and FY2024–FY2025 balance sheets. |
| `companies/MSFT/sources/FY2026-Q4/10-K-FY2025.txt` | https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/msft-20250630.htm | 2025-07-30 | Existing 2026-09-08 cache reused 2026-09-18 | Mature software PBP margin comparison; consolidated capital context. Only this eligible FY2025 filing was read, not the FY2026 annual filing or later-period notes in the same folder. |
| `10-K-FY2025.txt` | https://www.sec.gov/Archives/edgar/data/1730168/000173016825000121/avgo-20251102.htm | 2025-12-18 | Existing 2026-09-07 cache reused 2026-09-18 | Own-company historical benchmark and segment-to-GAAP bridge. |
| `8-K-2026-04-06-google-anthropic.txt` | See existing `MANIFEST.md` orchestrator additions for SEC origin | 2026-04-06 | Existing cache reused 2026-09-18 | Finite contract/capacity disclosure; no supported revenue/GW conversion. |
| `notes-valuation-peers.md` | Gatherer calculations and cited primary sources above | Not applicable | Written 2026-09-18 | Peer selection, margins, book-capital calculations, SBC/R&D/goodwill/lease reconciliation and limitations. |

New SEC downloads used User-Agent `company-research-skill owner@example.com`; requests ran sequentially below 10/sec. Initial sandboxed network access could not resolve SEC; authorized escalated read-only download succeeded. HTML was parsed in memory using Python's standard `HTMLParser`; script/style/inline-XBRL header text was excluded, table cells separated with ` | ` and block text split into lines. Raw HTML was not saved. Files contain the full statements, relevant notes and closing schedules/signatures. Search results were used only to discover original pre-cutoff SEC URLs and filing dates; no later operating information was used.

Transcript tier: not applicable; all newly downloaded materials are primary filings.
