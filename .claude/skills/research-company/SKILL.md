---
name: research-company
description: Build a plain-English company research report from scratch (business.md + outlook.md) as of a given quarter, following AGENTS.md. Use when the user asks to research, analyze, or write up a company for the first time, e.g. "/research-company GOOGL as of Q1 2026".
---

# research-company

Arguments: `<TICKER> [as of <QLABEL>] [--transcript <local file>]`

If no as-of quarter is given, use the most recently reported quarter with an earnings announcement and the corresponding financial filing on EDGAR, including 6-K/20-F equivalents. A missing call or transcript does not disqualify a quarter; use [§12.2](../../../docs/sources.md#section-12-2) and [§12.5](../../../docs/sources.md#section-12-5).

## Procedure

Read the [root instructions](../../../AGENTS.md), [research guide](../../../docs/research.md), [sourcing guide](../../../docs/sources.md), and [review guide](../../../docs/review.md) before the dependent work. Before fetching, read `companies/<TICKER>/source-guide.md` if present. These guides own the requirements; this skill sequences them. Give each delegated role the applicable guides.

1. **Resolve the company.** Ticker → CIK via the EDGAR company tickers JSON (`https://www.sec.gov/files/company_tickers.json`) or company submissions. Determine the fiscal calendar from the annual filing. Fix the quarter label per [§5](../../../docs/research.md#section-5) and the cutoff per [§12.5](../../../docs/sources.md#section-12-5), including equivalent foreign-issuer filings and the transcript-posting exception.

2. **Protect existing work.** If `companies/<TICKER>/business.md` exists and the owner requested an update, route to `refresh-company` under AGENTS.md's opening routing rule. Rebuilding requires an explicit rebuild request; without one, preserve the report and explain the appropriate options. Do not treat a routing choice as permission to overwrite.

3. **Create the folder** `companies/<TICKER>/` with `sources/<QLABEL>/`, `quarters/`, `review/`.

4. **Gather** per [§13](../../../docs/review.md#section-13): one subagent per type (`filings`, `transcript`, `ir`), scheduled to fit current capacity. Give each the ticker, CIK, fiscal calendar, quarter, cutoff, applicable [§12](../../../docs/sources.md#section-12) fetch paths and transcript tiers, any `--transcript` file, and SEC User-Agent requirement. Follow [§13](../../../docs/review.md#section-13)'s cache reuse, prior-period comparison sources, and separate `MANIFEST-<type>.md` parts merged by the runner. Apply [§12.5](../../../docs/sources.md#section-12-5)'s information cutoff and explicit transcript-posting exception.

5. **Write** ([§13](../../../docs/review.md#section-13)). Launch one writer subagent. It reads the [research guide](../../../docs/research.md), shared boundaries, all `notes-*.md`, and cached sources as needed, and writes `business.md` ([§6](../../../docs/research.md#section-6)) and `outlook.md` ([§7](../../../docs/research.md#section-7), omitting the Tone shift section on a first run). It proposes indicators in `business.md` §8 and marks them `_Proposed — owner to review and lock._` It runs the [§14](../../../docs/research.md#section-14) self-check before returning.

6. **Review** per [§13](../../../docs/review.md#section-13). Launch an independent reviewer to write `review/<QLABEL>-review.md`. Apply the shared correction permissions, two-pass limit, and PASS/REVISE/BLOCKED handling; address the full first-pass revision list before the second pass.

7. **Commit only after PASS.** `research(<TICKER>): initial report as of <QLABEL>`, following [§16](../../../AGENTS.md#section-16). Otherwise preserve drafts and report incomplete work under [§13](../../../docs/review.md#section-13).

8. **Report to the user** in a few lines: where the files are, the transcript source tier used, the reviewer verdict, the proposed indicators (so they can lock them), and any FLAGs or gaps ("not disclosed" items that mattered).

## Handoff to valuation

Company research stays focused on understanding the business. Preserve sourced accounting definitions, segment changes, capital needs and management's claims so the later analyst can trace them. When valuation is also requested, hand off after the research passes to [draft-valuation](../draft-valuation/SKILL.md); that skill gathers [analyst consensus](../../../docs/sources.md#section-12-6) and targeted peer/market evidence before drafting under the [valuation playbook](../draft-valuation/references/analyst-playbook.md). Standalone research and routine refresh do not require new valuation forecasts. A completed business report is not a claim that every valuation assumption is already supported. Do not insert valuation targets or forecasts into the research reports.
