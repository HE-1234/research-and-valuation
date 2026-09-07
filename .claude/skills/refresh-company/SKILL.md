---
name: refresh-company
description: Update an existing company report with a new quarter: archive the old outlook, grade last quarter's claims into scorecard.md, write the new outlook.md with a tone-shift section, and flag (never edit) anything in business.md that no longer holds. Use when the user asks to refresh, update, or re-run a company after new earnings, e.g. "/refresh-company MRVL with Q2 FY2027".
---

# refresh-company

Arguments: `<TICKER> [with <QLABEL>] [--transcript <local file>]`

If no quarter is given, use the most recently reported quarter after the one in the current `outlook.md`.

## Procedure

Read `AGENTS.md` in the repo root before anything else. It defines everything; this skill only sequences the work. The refresh procedure itself is AGENTS.md §15.

1. **Preconditions.** `companies/<TICKER>/business.md` and `outlook.md` must exist. If not, stop and tell the user to run `research-company`. Read `business.md` §8 for the locked indicator set. If indicators are still marked `_Proposed_`, warn the user but proceed using them as-is.

2. **Resolve the new quarter** and its as-of cutoff date (later of call date and 10-Q/10-K filing date). Create `sources/<new QLABEL>/`.

3. **Gather** (AGENTS.md §13). Launch three subagents in parallel: `filings` (the new 10-Q or 10-K only, plus any 8-Ks in the quarter that are not routine), `transcript` (tier order per §12.2, or the `--transcript` file), `ir` (press release and slides). Same caching, manifest, and as-of discipline rules as a research run.

4. **Archive.** Copy `outlook.md` to `quarters/<old QLABEL>-outlook.md` byte-for-byte.

5. **Grade and write.** Launch one writer subagent with: AGENTS.md, `business.md`, the archived old outlook, the current `scorecard.md` (may not exist yet), and all new `notes-*.md`. It must:
   - Grade every claim in old `outlook.md` §5 plus every ⏳ claim carried in `scorecard.md`, per §9, one line of evidence each with source tag.
   - Prepend the new grading section to `scorecard.md` and update the running tally and indicator time series (§10). Create the file if this is the first refresh.
   - Write the new `outlook.md` per §7, using exactly the locked indicators in §1, and including §6 Tone shift compared against the archived outlook and, where useful, the old transcript in `sources/<old QLABEL>/transcript.txt`.
   - Check `business.md` against the new sources and prepend FLAG blocks per §11 where warranted. Never edit the body of `business.md`.
   - Run the §14 self-check.

6. **Review** (AGENTS.md §13). Launch one reviewer subagent covering `outlook.md`, `scorecard.md`, and any flags. In addition to the standard checks, the reviewer must re-verify every verdict in the new scorecard section against the cached sources: a wrong ✅ or ❌ is the worst possible error in this system. Maximum two cycles.

7. **Commit.** `refresh(<TICKER>): <new QLABEL>`.

8. **Report to the user** in a few lines: the running tally change, any ❌ or 🔇 verdicts with one line each, the tone-shift headline, any FLAGs raised, transcript source tier, and reviewer verdict. If `companies/<TICKER>/valuation/` exists, add one line saying the valuation is now as of an older quarter (AGENTS.md §18.7); this skill never re-values.
