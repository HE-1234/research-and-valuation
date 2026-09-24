# Research report requirements

Read for initial research and refresh. Valuation writers also read §3 for the shared reader and style rules. These are the authoritative report requirements; [AGENTS.md](../AGENTS.md) owns shared boundaries and routing. Section numbers are retained for existing citations. Source collection lives in [sources.md](sources.md); independent review and completion rules live in [review.md](review.md).

<a id="section-1"></a>

## 1. Purpose

Produce and maintain a library of plain-English company research reports, one folder per company,
that let the owner **understand the business** the way Charlie Munger and Warren Buffett would want to:
what it does, how it makes money, what the economics look like, what protects it, and what could kill it.

Then, each quarter, keep a **receipt**: what management said would happen, and whether it did.

Valuation (price, multiples, "is it cheap") is **out of scope for business research**. Valuation requests follow the separate layer in [§18](../.claude/skills/draft-valuation/references/model-spec.md#section-18).

<a id="section-2"></a>

## 2. Philosophy

Every report must leave the reader able to answer, in their own words:

1. **What do they actually do?** Who is the customer, what do they get, why do they pay.
2. **How profitable is the current business?** Not just margins, but how much real cash it throws off and what it takes to keep it going.
3. **What are the economics?** Does cost rise with every extra unit sold (linear, like a factory) or does it flatten (scale economics, like software)? Where does the money go? How capital-hungry is it?
4. **Why do customers stay?** The moat, its actual source, and the sign that would tell you it is weakening.
5. **How could it be disrupted, and in what scenario?** Ranked by plausibility, each with an early warning sign.
6. **Who runs it and what do they do with the cash?**

The owner's general preference is growth at a reasonable price; that belongs to the separate valuation layer in [§18](../.claude/skills/draft-valuation/references/model-spec.md#section-18).
The understanding layer must stand on its own without it.

<a id="section-3"></a>

## 3. Reader and style rules

**Reader:** the owner, assumed to be a smart 16-year-old. No prior finance or industry knowledge is assumed.
This does not mean baby talk or a pile of analogies. It means the core ideas require no background to follow.

**Rules, in priority order:**

1. **Never invent a number.** If a source does not give it, write "not disclosed" and say so. If you infer something, label it as an inference ("this suggests", "our inference:"). No estimates presented as facts.
2. **Every factual sentence gets a source tag** in square brackets at the end: `[10-K FY2025, Item 7]`, `[Q1 2026 call]`, `[Q1 2026 slides, p.4]`. Each file ends with a **Sources** list mapping tags to the cached file in `sources/`. If a transcript PDF has no printed page numbers, page tags refer to PDF pages and the Sources list must say so. For third-party machine transcripts, take numbers from the press release or slides and quote the transcript only for wording.
3. **Jargon:** avoid unless the term is genuinely important to understanding the business. If a term can be replaced by a plain phrase, replace it. If a term's meaning is inferable from its name (e.g., "data center", "cloud storage"), use it without explanation.
4. **Glossary:** each `business.md` ends with a short **Glossary** containing only the very important terms that cannot be avoided (examples: TPU, CPO, SRAM, ASIC). One sentence each: what it is and what it is used for. Nothing else goes in the glossary.
5. **Numbers live in small tables, meaning lives in prose.** Never write a paragraph that is mostly numbers. Tables cover five fiscal years where history is relevant.
6. **Quote management verbatim** where the exact wording matters (guidance, commitments, vision statements). Paraphrase everywhere else.
7. **Length targets:** `business.md` 2,000–3,000 words. `outlook.md` 800–1,200 words. Over the target is a sign of padding, not thoroughness. **Counting method:** prose words only, excluding tables, headings, the glossary, the Sources list, and the bracketed source tags. Writers and reviewers must both use this definition. Aim for the lower half of the range on a first draft; first drafts in the pilot ran 30–40% over.
8. **Language:** English.

<a id="section-4"></a>

## 4. File layout

```
finance/
├── AGENTS.md                 ← shared rules and workflow routing
├── README.md                 ← how to use the repo and find skills/teachings; the detailed rules live in focused guides
├── CLAUDE.md                 ← two-line pointer to AGENTS.md
├── docs/                     ← research, sourcing, review, and instruction map
├── .claude/skills/
│   ├── research-company/SKILL.md
│   ├── refresh-company/SKILL.md
│   ├── draft-valuation/
│   │   ├── SKILL.md                  ← §18: write assumptions.yaml, stop for owner review
│   │   └── references/              ← playbook, topical guides, reviewer checklist, forecast-learning procedure
│   └── compute-valuation/SKILL.md    ← §18: run the engine, write valuation.md
├── pyproject.toml / uv.lock          ← uv project for the valuation engine (§18.9)
├── tools/
│   └── valuation/                    ← the DCF engine, its tests, cached Damodaran datasets (data/), UI audit reports (ui-audit/), and the indexed teaching library with cached primary text (damodaran-notes/)
└── companies/
    └── <TICKER>/
        ├── source-guide.md   ← company-specific fetch paths and disclosure quirks
        ├── business.md       ← Section A: the stable understanding of the business
        ├── outlook.md        ← Section B: the current quarter's management outlook and claims
        ├── scorecard.md      ← the growing receipt: claims graded quarter by quarter
        ├── quarters/
        │   └── <QLABEL>-outlook.md   ← every past outlook.md, kept in full
        ├── sources/
        │   └── <QLABEL>/
        │       ├── MANIFEST.md       ← what was fetched, from where, which source tier, when
        │       ├── 10-K-FY<YYYY>.txt / 10-Q-<QLABEL>.txt
        │       ├── transcript.txt
        │       ├── press-release.txt
        │       ├── slides.txt
        │       └── notes-*.md        ← gatherer notes (structured, cited)
        ├── review/
        │   ├── <QLABEL>-review.md    ← reviewer's rubric check and citation spot-check
        │   └── <QLABEL>-valuation-draft-review.md   ← §18 reviewer's check of assumptions.yaml
        └── valuation/                ← §18
            ├── historical-roic.yaml   ← sourced annual evidence for read-only app comparison (optional)
            ├── assumptions.yaml      ← the single source of valuation inputs (agents write it; the owner edits through the app)
            ├── assumptions.md        ← read-only rendering of the YAML as tables with reasons; regenerated on every save/compute
            ├── valuation.md          ← rendered by the engine: stories, tables, results
            ├── history/<date>/       ← previous assumptions.yaml + valuation.md pairs
            ├── forecasts/<id>/       ← frozen inputs + dated forecast.md, separate analyst/owner origins
            ├── forecast-reviews/     ← sourced actuals versus original forecasts by quarter
            └── lessons.md            ← company-specific forecast lessons for future authorized redrafts
```

Ticker is the folder name, uppercase. Only extracted text is cached, never PDFs or HTML binaries.

<a id="section-5"></a>

## 5. Quarter labels

Use the **company's own fiscal labels** as they appear in its filings and calls, because that is what the transcripts and 10-Qs say.
When the fiscal calendar differs from the calendar year, add the calendar period in parentheses on first use in each file.

- Alphabet: `Q1 2026` (fiscal = calendar; no parenthetical needed).
- Marvell: `Q1 FY2027 (quarter ended early May 2026)`; fiscal year ends around the end of January.

File and folder names use a compact form with no spaces: `2026-Q1`, `FY2027-Q1`.

<a id="section-6"></a>

## 6. Section A — `business.md` skeleton

Fixed skeleton. Every heading is required. The writer may add a company-specific subsection under any heading but may not skip one.
Section A is written once and thereafter **frozen**: the refresh skill may not edit it (see §11).

```
# <Company> — The Business
_As of <QLABEL>. Written <date>._

## 1. What they do
   Two or three paragraphs a 16-year-old follows. Include a short paragraph of history: how they got here.
## 2. How the money comes in
   Each revenue stream: who pays, why they pay, roughly how big. A small table of segment revenue, 5 fiscal years.
## 3. The economics
   Does cost rise with usage or flatten? Gross margin, operating margin, where the money goes.
   Capital intensity: how much they must spend just to stay in place vs. to grow. Table: revenue, gross margin, operating margin, capex, capex/revenue, 5 fiscal years.
## 4. How profitable, really
   Operating cash flow, free cash flow, cash conversion, return on capital in plain words. Table, 5 fiscal years.
## 5. Why customers don't leave
   The moat, its actual source (switching costs, network effects, scale, brand, IP, distribution), and the specific sign you'd watch to know it is weakening.
## 6. What could break it
   Disruption scenarios ranked by plausibility. For each: what would have to happen, the early warning sign, and how exposed the current profit pool is.
   Customer concentration goes here when material.
## 7. Who runs it and what they do with the cash
   Management track record, capital allocation (buybacks, dividends, M&A, capex), incentives, ownership.
## 8. Indicators worth tracking
   The 5–8 company-specific signals that, if you could see only these each quarter, would tell you whether the thesis in §1–§7 is holding.
   Not just revenue and EPS. Each indicator: name, why it matters, where in the filings it comes from.
   These are proposed by the agent on the first run and LOCKED after the owner reviews them (see §8 below).

## Glossary
## Sources
```

<a id="section-7"></a>

## 7. Section B — `outlook.md` skeleton

Rewritten every quarter. The previous version is archived in full to `quarters/`.

```
# <Company> — Outlook as of <QLABEL>
_Transcript source tier: <company-published | 8-K exhibit | third-party (name) | owner-supplied | none>. Written <date>._

## 1. This quarter in the indicators
   Table: one row per locked indicator from business.md §8. Columns: this quarter, last quarter, what management had said to expect (or "no guidance").
## 2. What management says about the core business
   Their stated direction and long-term vision, in plain words. Quote where wording matters.
## 3. Growth engines
   One short block per engine: what it is, how big now, what management claims, what would tell you it is working or not.
## 4. Guidance
   Next quarter and full year. Revenue, margins, capex, anything else they commit to. Quoted verbatim, not paraphrased.
## 5. Claims to verify next quarter
   The explicit list. See §9 for the rules.
## 6. Tone shift  (refresh runs only; omit on first run)
   What management stopped saying, started saying, or said differently vs. last quarter. This is often the most important section.

## Sources
```

<a id="section-8"></a>

## 8. Indicators

- Proposed by the research skill in `business.md` §8 on the first run.
- The owner reviews and edits them. After that they are **locked**.
- If they are still proposed, research and refresh continue using the existing set unchanged and report its status. Only the owner locks or changes the set; locking is not a prerequisite for completing either report.
- The refresh skill must use exactly the existing set (locked or still proposed) in `outlook.md` §1 so quarters are comparable.
- If the refresh skill believes an indicator should be added or replaced, it writes a **flag** (see §11) and continues using the locked set.
- Anchor each indicator to a disclosure that recurs every quarter (a balance-sheet or income-statement line, a segment table row, a KPI the company has reported for several quarters). Indicators that depend on a number management happened to give on one call (a dollar target, a growth percentage) tend to go undisclosed the next quarter; in the pilot Marvell dropped three such figures in one quarter. Prefer the recurring line, and track the one-off target as a claim instead.

<a id="section-9"></a>

## 9. Claims and verdicts

A **claim** is one testable sentence derived from what management said, written at outlook time so that next quarter's check is mechanical.

Rules for writing a claim (`outlook.md` §5):

- One sentence, one thing to check. Tie it to a metric, a date, or an observable event wherever possible.
- Under each claim, the verbatim quote it came from, with source tag.
- Prefer claims about the **fundamental signals** (the locked indicators, product milestones, margin structure, customer wins, capacity) over headline revenue and EPS. Include headline guidance too, but it should not dominate the list.
- Target 6–12 claims per quarter. Fewer, sharper claims beat a long vague list.
- Vague management statements ("we see strong momentum") are not claims. Either sharpen them into something checkable or leave them out.
- **Single direction, no either/or.** A claim must be able to fail. "Management reaffirms or raises X" is fine; "management reaffirms X or explains why not" can never be missed and is not a claim.
- **Label sharpenings.** If the claim turns a soft phrase ("modest margin pressure") into a number, say so in the claim: "our sharpening of ..., not management's number".
- **Disclosure checks** (e.g., "the 10-Q shows Distributor A at or above 45%") are allowed but must be labelled as disclosure checks, not management claims, and must state whether the threshold refers to the quarter or the year-to-date column.

Verdict scale, used by the refresh skill when grading last quarter's claims:

| Verdict | Meaning |
|---|---|
| ✅ Met | The claim happened as stated, per this quarter's sources. |
| ❌ Missed | The claim did not happen, per this quarter's sources. |
| 🟡 Partial | Directionally happened but short of the stated level, or only part of it happened. |
| ⏳ Not yet verifiable | The claim's horizon has not arrived, or the data needed is not yet disclosed. Carries forward. |
| 🔇 Dropped | Management stopped talking about it and disclosed nothing that lets you check. This is a signal in itself. |

Every verdict gets a one-line reason with a source tag.

<a id="section-10"></a>

## 10. Scorecard — `scorecard.md` format

```
# <Company> — Scorecard

## Running tally
Table: quarter graded | met | missed | partial | not yet | dropped

## Indicator time series
Table: one row per locked indicator, one column per quarter, newest on the right.

## <QLABEL of the quarter that GRADED the claims>  (grading claims made in <previous QLABEL>)
Table: claim | verdict | evidence (one line, with source tag)

## <older quarter>
...
```

Newest section at the top. Claims that are ⏳ carry forward into the next grading section until resolved.

<a id="section-11"></a>

## 11. Freeze-and-flag rule

During a refresh, the **body and indicator definitions** in `business.md` are read-only. Prepending sourced FLAG blocks is authorized and requires no separate confirmation.

If the refresh finds evidence that a statement in `business.md` is now wrong or materially incomplete (a pivot, a broken moat, a management change, a new segment, a customer concentration change), it does **not** edit the text. It prepends a flag block to the top of `business.md`:

```
> **⚠️ FLAG (<QLABEL>):** <one or two sentences: what changed, which section it affects, source tag>. Owner to decide whether to update §N.
```

Flags stay until the owner resolves them by editing the section and deleting the flag. Indicator-set change proposals use the same block.

<a id="section-14"></a>

## 14. Rubric (self-check and reviewer check)

After reading `business.md` + `outlook.md`, the owner should be able to say yes to all five:

1. Can I explain what this company does, and who pays it, in two sentences?
2. Do I know exactly what would kill it, and what the early warning sign is?
3. Do I know why the margins are what they are, and whether cost scales with usage?
4. Could I predict what the scorecard will check next quarter, from §5 of the outlook alone?
5. Did nothing in the report require knowledge I don't have?

<a id="section-15"></a>

## 15. Refresh procedure (`refresh-company`)

Given a ticker with an existing report and a new quarter:

1. Read `business.md` (for the locked indicators and thesis), the current `outlook.md`, and `scorecard.md`.
2. Run gatherers for the new quarter ([§13](review.md#section-13)), respecting as-of discipline for the new quarter.
3. Archive: copy the current `outlook.md` to `quarters/<old QLABEL>-outlook.md` unchanged.
4. Grade: for every claim in the old `outlook.md` §5 (and every ⏳ claim carried in `scorecard.md`), assign a verdict per §9 with one line of evidence. Write the new grading section at the top of `scorecard.md`, update the running tally and the indicator time series.
5. Write the new `outlook.md` per §7, including §6 Tone shift, comparing against the archived outlook and the new transcript.
6. Check `business.md` against the new sources. If anything is now wrong or materially incomplete, prepend a flag per §11. Do not edit the body. When prior valuation forecast records exist, compare due outcomes under [§18.12](../.claude/skills/draft-valuation/references/forecasts-and-learning.md#section-18-12) and update the separate forecast review/lessons; never change active valuation assumptions or compute a new value during refresh.
7. Reviewer pass per [§13](review.md#section-13).
8. Commit only after PASS ([§13](review.md#section-13)).
