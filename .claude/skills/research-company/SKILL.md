---
name: research-company
description: Build a plain-English company research report from scratch (business.md + outlook.md) as of a given quarter, following AGENTS.md. Use when the user asks to research, analyze, or write up a company for the first time, e.g. "/research-company GOOGL as of Q1 2026".
---

# research-company

Arguments: `<TICKER> [as of <QLABEL>] [--transcript <local file>]`

If no as-of quarter is given, use the most recently reported quarter that has both an earnings call and a 10-Q/10-K on EDGAR.

## Procedure

Read `AGENTS.md` in the repo root before anything else. It defines the philosophy, style rules, file layout, skeletons, source rules, and orchestration. This skill only sequences the work.

1. **Resolve the company.** Ticker → CIK via `https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=<TICKER>&type=10-K&output=atom` or the EDGAR company tickers JSON (`https://www.sec.gov/files/company_tickers.json`). Determine the fiscal calendar from the 10-K. Fix the as-of quarter label per AGENTS.md §5 and the as-of cutoff date (the later of the call date and the 10-Q filing date).

2. **Refuse to overwrite.** If `companies/<TICKER>/business.md` exists, stop and tell the user to use `refresh-company` instead, unless they explicitly ask to rebuild.

3. **Create the folder** `companies/<TICKER>/` with `sources/<QLABEL>/`, `quarters/`, `review/`.

4. **Gather** (AGENTS.md §13). Launch three subagents in parallel, one per type: `filings`, `transcript`, `ir`. Give each: the ticker, CIK, fiscal calendar, as-of quarter and cutoff date, the exact fetch paths from AGENTS.md §12 (including the transcript tier order and any `--transcript` file), the SEC User-Agent requirement, and the instruction to cache extracted text and write `notes-<type>.md` and a `MANIFEST.md` entry. Each gatherer must respect as-of discipline (§12.5): fetch nothing published after the cutoff.

5. **Write** (AGENTS.md §13). Launch one writer subagent. It reads AGENTS.md, all `notes-*.md`, and cached sources as needed, and writes `business.md` (§6) and `outlook.md` (§7, omitting the Tone shift section on a first run). It proposes indicators in `business.md` §8 and marks them `_Proposed — owner to review and lock._` It runs the §14 self-check before returning.

6. **Review** (AGENTS.md §13). Launch one reviewer subagent. It writes `review/<QLABEL>-review.md` and either fixes minor issues directly or returns REVISE with a list. On REVISE, re-launch the writer with the list. Maximum two cycles.

7. **Commit.** `research(<TICKER>): initial report as of <QLABEL>`.

8. **Report to the user** in a few lines: where the files are, the transcript source tier used, the reviewer verdict, the proposed indicators (so they can lock them), and any FLAGs or gaps ("not disclosed" items that mattered).
