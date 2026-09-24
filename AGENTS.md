# AGENTS.md — Company Research System

This file owns the shared boundaries and routes each task to its authoritative guide. Read the applicable guides before acting; details are loaded by workflow, not all at startup. Paths in backticks are relative to the repository root unless stated otherwise. Current guides govern; dated reviews and lessons are evidence of past decisions.

## Scope and autonomy

The library helps the owner understand what a company does, its economics, competitive advantages, risks, management, and whether management delivered on earlier claims. Business research and valuation are separate layers. Write in English for a smart 16-year-old with no assumed finance background; use plain language and sourced evidence.

Research-report rules govern research artifacts; valuation rules govern valuation, and app rules govern app work. They do not require report-style citations, company pipelines, or app audits for unrelated repository maintenance. Within the requested workflow, complete routine investigation, source fallbacks, implementation, and verification without repeated confirmation. Use stated defaults for nonmaterial choices. Ask when missing information materially changes the task or an explicit owner gate applies. Existing authorization persists; current task-specific restrictions, including review-before-edit requests, remain binding. A blocker stops only dependent work: finish and report unaffected work without presenting an incomplete result as complete.

When the request clearly covers another workflow, route to it and explain the choice without requiring the owner to repeat the request. Do not infer permission to rebuild an existing report, redraft owner assumptions, compute valuation results before the draft has been presented for owner review, extend the two-pass review limit, or push commits. An explicit rebuild/redraft request is sufficient authorization for that action (`--redraft` is one way to express it). A missing prerequisite outside the requested scope needs a concise explanation and question, not an automatically expanded task. Refresh never re-values; a separately requested valuation follows its own workflow.

Select and run the applicable repository skills without asking the owner to choose them. An initial company-valuation request includes creating missing initial business research, so automatically chain research into drafting when `business.md` or `outlook.md` is absent. This does not authorize rebuilding existing research, replacing existing owner assumptions, or crossing the draft-review boundary before a subsequent compute request.

## Choose the workflow

| Requested work | Read and follow |
|---|---|
| Initial company research | [Research skill](.claude/skills/research-company/SKILL.md); it loads report, source, and review requirements. |
| New quarter for an existing company | [Refresh skill](.claude/skills/refresh-company/SKILL.md); preserve the business report and existing indicators. |
| Initial valuation or authorized redraft | [Draft skill](.claude/skills/draft-valuation/SKILL.md); it loads model, assumptions, evidence, review, and draft app-check requirements. |
| Compute after draft review | [Compute skill](.claude/skills/compute-valuation/SKILL.md); apply the existing inputs and requested overrides without redrafting. |
| Valuation engine or schema work | [Engine README](tools/valuation/README.md), [model specification](.claude/skills/draft-valuation/references/model-spec.md), and the relevant [assumptions](.claude/skills/draft-valuation/references/assumptions-spec.md) or [output](.claude/skills/draft-valuation/references/valuation-output.md) contract. |
| App work | [App guide](tools/valuation/APP_GUIDE.md) and [engine README](tools/valuation/README.md); consult model/input contracts when behavior depends on them. |
| Instruction or repository maintenance | This file and the affected guides and their callers; no company pipeline or app audit unless the work actually changes those artifacts or app behavior. |

The skills explicitly name their required reads. If delegating within a workflow, pass the shared boundaries and the references needed for that role. A pointer is not a substitute for reading its requirements before the dependent action.

<a id="18-valuation-draft-valuation-compute-valuation"></a>

## Where information belongs

| Information | Authoritative home |
|---|---|
| Report purpose, style, skeletons, indicators, claims, flags, and refresh requirements | [Research guide](docs/research.md) |
| Source priority, transcript fallback, caching, and information cutoff | [Sourcing guide](docs/sources.md) |
| Gathering roles, independent review, correction permissions, two-pass limit, and completion | [Review guide](docs/review.md) |
| Valuation method and input requirements | The focused specifications linked above, including [assumptions rule 10](.claude/skills/draft-valuation/references/assumptions-spec.md#section-18-4) for consensus-led near-term drafting and [consensus collection](docs/sources.md#section-12-6); the [analyst playbook](.claude/skills/draft-valuation/references/analyst-playbook.md) routes practical teaching references. |
| Redraft protection, draft-review boundary, owner editing, and computation contracts | [Valuation workflow contracts](.claude/skills/draft-valuation/references/workflow-contracts.md) |
| Company-specific fetch paths, fiscal-calendar and disclosure quirks | `companies/<TICKER>/source-guide.md`; read it before fetching for that company, if present. |
| Quarter evidence and provenance | `companies/<TICKER>/sources/<QLABEL>/`, including its manifest |
| Forecast evidence and company-specific learning | Company's `valuation/forecasts/`, `forecast-reviews/`, and `lessons.md`, under [forecast requirements](.claude/skills/draft-valuation/references/forecasts-and-learning.md) |

Never invent numbers or present a judgment as a reported fact. Apply the detailed source and reader rules to their artifacts. Preserve owner assumptions and frozen research under the workflow's editing rules. A passing validator alone does not establish supported assumptions or completed review.

Use explicit reading routes even when working from the repository root; do not assume a company folder's notes are automatically loaded. If its source guide is absent, use the shared sourcing rules. Read only the relevant company notes and method references. The [instruction map](docs/instruction-map.md) resolves legacy section citations; preserved [historical lessons](docs/history/2026-09-18-lessons.md) are optional context, not a required reading list.

<a id="section-16"></a>

## Git

- The repo root is the directory containing this file. Commit after each completed research run or refresh that passed review: `research(GOOGL): initial report as of 2026-Q1`, `refresh(MRVL): FY2027-Q2`.
- Valuation: `value(GOOGL): draft assumptions as of 2026-Q2` after a passing draft; `value(GOOGL): compute 2026-Q2 rev N` after each successful, checked normal compute (N counts computes for that as-of quarter, starting at 1). Owner edits to `assumptions.yaml` may ride along with the compute commit that follows them.
- Owner edits to `business.md` (indicator lock, flag resolution) are their own commits.
- Do not commit binaries. Never push. Stage only the requested workflow's files; unrelated owner changes stay out of its commit.

## Maintaining instructions and lessons

Apply specific feedback to the requested artifact within its editing rules. When feedback changes future practice, update the one authoritative instruction at the narrowest useful scope: company note, workflow reference, app guide, or shared rule. Link to that instruction from callers instead of duplicating its full text. Keep this root file short; move substantial task-specific detail to a focused guide and give its callers an explicit read trigger.

A separate lesson is optional. Record one when the cause or tradeoff will help a future decision: usually two to four lines stating the date, takeaway, affected rule, and a link to evidence. Put general decisions in [decision notes](docs/decisions.md), company-specific lessons with the company, and detailed incident evidence in the existing review/audit record. Do not add an incident narrative for every fix or retain superseded instructions as active rules. Preserve detailed forecast evidence and methodology reasoning where future analysis needs them; the concise lesson points to that evidence.

When moving instructions, update active callers and check links, section targets, and workflow reading routes. Preserve historical records and use the instruction map for their old section references. Mechanical relocation does not authorize changing research conclusions, owner inputs, model behavior, or approval boundaries.
