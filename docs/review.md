# Research and valuation review

Read for research, refresh and valuation drafting. The gathering and report checks below apply to research; valuation uses its skill and review checklist for valuation-specific checks. For valuation, the [draft review checklist](../.claude/skills/draft-valuation/references/review-checklist.md) includes consensus provenance, its use in the base case, and later-year/scenario checks. The independent-review, correction, two-pass, evidence-gap and completion rules apply to both. They do not impose a report pipeline on repository maintenance.

<a id="section-13"></a>

## 13. Orchestration: gather → write → review

Each company runs as an independent pipeline. Schedule against the current host's available agent capacity, counting nested agents and reserving capacity for their work. Parallelize only when capacity allows; otherwise serialize companies or gatherers. Do not occupy every slot with runners waiting to spawn children. On a capacity error, let active work finish and retry with a smaller schedule; do not blindly sleep and retry the same blocked layout. Preserve the writer and independent-review stages. If the host cannot run a required independent reviewer, finish preparatory work, preserve the checkpoint, and report that review is blocked; never label a self-review as independent.

### Gatherers (one per source type, parallel when capacity allows)

Each gatherer fetches its sources, caches extracted text ([§12.4](sources.md#section-12-4)), and writes a structured notes file `sources/<QLABEL>/notes-<type>.md` and its own `MANIFEST-<type>.md` part; the runner merges the parts into `MANIFEST.md` so parallel gatherers never write the same file. Notes are bullet facts, each with a source tag and page/section reference. Gatherers do not write prose for the report and do not interpret beyond what the source says.

- **filings** gatherer: latest 10-K and the as-of 10-Q. Extracts: business description, segments, revenue by segment (5 years, from current and prior 10-Ks as needed), margins, cash flow, capex, share count, buybacks, customer concentration, risk factors that are specific (not boilerplate), management and ownership, compensation structure from the proxy if easily available. Also scan every 8-K filed up to the cutoff (including those under a filing agent's accession prefix) and cache the material ones: officer changes, large customer or financing agreements, vote results. If the brief is large, cache all filings first and write notes second, so a mid-run failure can be resumed from the cache.
- **transcript** gatherer: the as-of quarter's call. Extracts: every forward-looking statement and guidance item verbatim; management's description of vision and growth engines; every question analysts asked and the substance of the answer; anything management declined to answer.
- **ir** gatherer: press release and slides for the as-of quarter, plus the prior quarter's press release (`press-release-<prev QLABEL>.txt`), which fills outlook §1's "what management had said to expect" column directly. Extracts: reported metrics, any KPIs the company highlights that are not in the 10-Q, guidance table, non-GAAP reconciliations. Where KPI or reconciliation pages are images, say so in the notes and take the numbers from the release.

These source and manifest rules also apply on refresh. Reuse the cache first; fetch additional pre-cutoff filings or prior-period guidance materials only when required for comparisons, incorporated disclosures, or calculations. Use equivalent foreign-issuer filings per [§12.5](sources.md#section-12-5). On refresh, scan new material filings since the previous cutoff rather than repeating the full historical scan. Image-only sources use the verified extraction methods in [§12.3](sources.md#section-12-3) when no equivalent text table exists.

### Writer (one per company)

Reads the root instructions, the research guide and all notes files. Writes `business.md` (research run only) and `outlook.md` following [research-guide §6](research.md#section-6) and [§7](research.md#section-7) exactly. Reads the cached source text directly when a note is insufficient. Runs the self-check in [§14](research.md#section-14) before finishing.

### Reviewer (one per company)

Reads the root instructions, this review guide, the applicable research or valuation requirements, the draft(s), and the cached sources. Produces `review/<QLABEL>-review.md` with:

1. Rubric result ([§14](research.md#section-14)), each question answered yes/no with one line of reasoning; use N/A only for a genuinely inapplicable check, and BLOCKED for missing required evidence.
2. Citation spot-check: pick at least 10 source-tagged sentences, including every number in the business report’s §3 and §4 tables, verify each against the cached source. List any that fail.
3. Jargon audit: list any term used without being either plain, name-inferable, or in the glossary.
4. Invented-number check: any figure with no source tag or with a tag that does not support it.
5. Verdict: PASS, REVISE with a specific list of repairable defects, or BLOCKED with the missing evidence or capability and affected checks. Missing required evidence is never PASS.

The reviewer may directly fix jargon, missing tags, and typos. Anything structural or factual goes back to the writer (the analyst for valuation). One review cycle is one complete reviewer pass; two passes maximum. After the first REVISE, address the full list before the second pass without asking for additional permission. After two passes, if still failing, preserve the draft and review findings, stop the dependent workflow, and report the unfinished items. Work beyond the two-pass limit requires owner authorization. Commit a completed research, refresh, or valuation draft only after PASS; a saved draft or successful command alone is not completion.

**Errors and evidence gaps.** Repair agent-authored formatting, schema, arithmetic, and citation errors within the authorized workflow and review budget. Search the permitted cache before declaring evidence missing. Do not repeatedly validate unchanged inputs, invent numbers to satisfy validation, or ask the owner to supply a routine implementation choice. Retain unsupported inputs as `null` or "not disclosed", complete unaffected work, and identify which scenarios and required checks are blocked. A validation exit code of zero may still leave scenarios stopped: inspect the full output. A documented `computable: false` management case is an allowed omission, not a reason to block the other cases. Genuinely inapplicable checks may be N/A with a reason (for example, comparison with a previous draft on the first run).

**On a refresh run, the reviewer must blind re-grade.** Before opening `scorecard.md`, the reviewer reads last quarter's claims and grades each one independently against the new sources, then compares. Every disagreement is written up with both verdicts and the evidence. In the pilot this caught one wrong ✅ that the writer's own checks had missed.
