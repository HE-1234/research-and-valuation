# AGENTS.md — Company Research System

This is the single source of truth for every agent and skill in this repository.
When the owner says "I don't like X," the fix goes here, not into an individual report.

Skills that implement this spec:

- `.claude/skills/research-company` — builds a company's report from scratch as of a given quarter.
- `.claude/skills/refresh-company` — updates an existing report with a new quarter and grades last quarter's claims.

---

## 1. Purpose

Produce and maintain a library of plain-English company research reports, one folder per company,
that let the owner **understand the business** the way Charlie Munger and Warren Buffett would want to:
what it does, how it makes money, what the economics look like, what protects it, and what could kill it.

Then, each quarter, keep a **receipt**: what management said would happen, and whether it did.

Valuation (price, multiples, "is it cheap") is explicitly **out of scope** for now. The report is about the business, not the stock.

## 2. Philosophy

Every report must leave the reader able to answer, in their own words:

1. **What do they actually do?** Who is the customer, what do they get, why do they pay.
2. **How profitable is the current business?** Not just margins, but how much real cash it throws off and what it takes to keep it going.
3. **What are the economics?** Does cost rise with every extra unit sold (linear, like a factory) or does it flatten (scale economics, like software)? Where does the money go? How capital-hungry is it?
4. **Why do customers stay?** The moat, its actual source, and the sign that would tell you it is weakening.
5. **How could it be disrupted, and in what scenario?** Ranked by plausibility, each with an early warning sign.
6. **Who runs it and what do they do with the cash?**

The owner's general preference is growth at a reasonable price, but that is for a later valuation layer.
The understanding layer must stand on its own without it.

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

## 4. File layout

```
finance/
├── AGENTS.md                 ← this file
├── CLAUDE.md                 ← two-line pointer to AGENTS.md
├── .claude/skills/
│   ├── research-company/SKILL.md
│   └── refresh-company/SKILL.md
└── companies/
    └── <TICKER>/
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
        └── review/
            └── <QLABEL>-review.md    ← reviewer's rubric check and citation spot-check
```

Ticker is the folder name, uppercase. Only extracted text is cached, never PDFs or HTML binaries.

## 5. Quarter labels

Use the **company's own fiscal labels** as they appear in its filings and calls, because that is what the transcripts and 10-Qs say.
When the fiscal calendar differs from the calendar year, add the calendar period in parentheses on first use in each file.

- Alphabet: `Q1 2026` (fiscal = calendar; no parenthetical needed).
- Marvell: `Q1 FY2027 (quarter ended early May 2026)`; fiscal year ends around the end of January.

File and folder names use a compact form with no spaces: `2026-Q1`, `FY2027-Q1`.

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

## 8. Indicators

- Proposed by the research skill in `business.md` §8 on the first run.
- The owner reviews and edits them. After that they are **locked**.
- The refresh skill must use exactly the locked set in `outlook.md` §1 so quarters are comparable.
- If the refresh skill believes an indicator should be added or replaced, it writes a **flag** (see §11) and continues using the locked set.
- Anchor each indicator to a disclosure that recurs every quarter (a balance-sheet or income-statement line, a segment table row, a KPI the company has reported for several quarters). Indicators that depend on a number management happened to give on one call (a dollar target, a growth percentage) tend to go undisclosed the next quarter; in the pilot Marvell dropped three such figures in one quarter. Prefer the recurring line, and track the one-off target as a claim instead.

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

## 11. Freeze-and-flag rule

During a refresh, `business.md` is **read-only**.

If the refresh finds evidence that a statement in `business.md` is now wrong or materially incomplete (a pivot, a broken moat, a management change, a new segment, a customer concentration change), it does **not** edit the text. It prepends a flag block to the top of `business.md`:

```
> **⚠️ FLAG (<QLABEL>):** <one or two sentences: what changed, which section it affects, source tag>. Owner to decide whether to update §N.
```

Flags stay until the owner resolves them by editing the section and deleting the flag. Indicator-set change proposals use the same block.

## 12. Sources: what to fetch, in what order, and how

### 12.1 Primary sources (always)

| Source | Where | Notes |
|---|---|---|
| 10-K, 10-Q, 8-K, proxy (DEF 14A) | SEC EDGAR | `https://data.sec.gov/submissions/CIK<10 digits>.json` lists filings. Documents under `https://www.sec.gov/Archives/edgar/data/<CIK>/<accession-no-dashes>/<filename>`. **SEC requires a User-Agent header** shaped like `AppName email@domain.tld`; SEC rejects anything else as an "Undeclared Automated Tool". Use `-A "company-research-skill owner@example.com"` (owner: replace with your real email). Keep requests under 10/sec. |
| Earnings call transcript | see tiers below | |
| Earnings press release | company IR page or 8-K exhibit 99.1 | The 8-K exhibit is the most reliable path. |
| Earnings slides / investor deck | company IR page | |

### 12.2 Transcript source tiers (ordered fallback)

1. **Company-published** transcript (IR site). Alphabet publishes a PDF per quarter, linked from its event feed; see 12.3.
2. **8-K exhibit** containing prepared remarks or transcript. (Neither pilot company does this, but some companies do.)
3. **Third-party free** transcript: The Motley Fool (`fool.com/earnings/call-transcripts/...`). URL slugs are inconsistent; discover the link from `https://www.fool.com/quote/<exchange>/<ticker>/` rather than guessing. Check robots.txt permits the path.
4. **Owner-supplied** local file, if given as an argument.
5. **None**: proceed with press release, slides, and 10-Q. Mark the outlook header `Transcript source tier: none`, and in §5 list which claims could not be sharpened for lack of a transcript.

Always record the tier used in `outlook.md`'s header and in `sources/<QLABEL>/MANIFEST.md`.

### 12.3 Known company-specific fetch paths (verified 2026-09-07)

**Alphabet (GOOGL, CIK 0001652044)**
- IR HTML pages block plain fetches (Cloudflare). Use the open Q4 Inc. JSON feeds instead:
  - Events (calls, transcripts): `https://abc.xyz/feed/Event.svc/GetEventList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=<YYYY>&excludeSelection=1&eventDateFilter=All`
    Each earnings event lists a transcript PDF attachment on `s206.q4cdn.com`, e.g. `.../doc_events/2026/Jul/22/2026_Q2_Earnings_Transcript.pdf`.
  - Financial reports (slides, release): `https://abc.xyz/feed/FinancialReport.svc/GetFinancialReportList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=<YYYY>&excludeSelection=1&reportSubType=`
    Slides pattern is roughly `.../doc_financials/<YYYY>/q<N>/<YYYY>q<N>-alphabet-earnings-slides.pdf` but casing varies, so read the feed.
- Fiscal year = calendar year.

**Marvell (MRVL, CIK 0001835632)**
- IR site is fetchable: `https://investor.marvell.com/financial-information/financial-results` lists press release, slides ("financial business results" PDF on cloudfront), and webcast per quarter. No transcript anywhere on the company site or 8-K.
- Transcript: tier 3 (Motley Fool). Verified fetchable as of 2026-09-07.
- Fiscal year ends around the end of January. FY2027 = roughly Feb 2026 – Jan 2027.

### 12.4 Caching

Everything the agents read is saved as extracted text under `companies/<TICKER>/sources/<QLABEL>/`. PDFs are converted with `pdftotext -layout`; HTML is stripped to text. `MANIFEST.md` lists every file with its origin URL, fetch date, and (for transcripts) the source tier. Re-runs read from cache before fetching.

### 12.5 As-of discipline

A report "as of Q1" must not use any information published after that quarter's earnings call and 10-Q. Gatherers fetch only documents dated on or before the as-of cutoff. Writers must not use knowledge of later events. This is what makes the scorecard honest.

## 13. Orchestration: gather → write → review

Each company runs as an independent pipeline; multiple companies run in parallel.

### Gatherers (parallel, one per source type)

Each gatherer fetches its sources, caches extracted text (§12.4), and writes a structured notes file `sources/<QLABEL>/notes-<type>.md`. Notes are bullet facts, each with a source tag and page/section reference. Gatherers do not write prose for the report and do not interpret beyond what the source says.

- **filings** gatherer: latest 10-K and the as-of 10-Q. Extracts: business description, segments, revenue by segment (5 years, from current and prior 10-Ks as needed), margins, cash flow, capex, share count, buybacks, customer concentration, risk factors that are specific (not boilerplate), management and ownership, compensation structure from the proxy if easily available.
- **transcript** gatherer: the as-of quarter's call. Extracts: every forward-looking statement and guidance item verbatim; management's description of vision and growth engines; every question analysts asked and the substance of the answer; anything management declined to answer.
- **ir** gatherer: press release and slides for the as-of quarter. Extracts: reported metrics, any KPIs the company highlights that are not in the 10-Q, guidance table, non-GAAP reconciliations.

### Writer (one per company)

Reads AGENTS.md and all notes files. Writes `business.md` (research run only) and `outlook.md` following §6 and §7 exactly. Reads the cached source text directly when a note is insufficient. Runs the self-check in §14 before finishing.

### Reviewer (one per company)

Reads AGENTS.md, the draft(s), and the cached sources. Produces `review/<QLABEL>-review.md` with:

1. Rubric result (§14), each question answered yes/no with one line of reasoning.
2. Citation spot-check: pick at least 10 source-tagged sentences, including every number in §3 and §4 tables, verify each against the cached source. List any that fail.
3. Jargon audit: list any term used without being either plain, name-inferable, or in the glossary.
4. Invented-number check: any figure with no source tag or with a tag that does not support it.
5. Verdict: PASS or REVISE with a specific list.

The reviewer may directly fix jargon, missing tags, and typos. Anything structural or factual goes back to the writer for a second pass. Maximum two review cycles; if still failing, stop and report to the owner.

**On a refresh run, the reviewer must blind re-grade.** Before opening `scorecard.md`, the reviewer reads last quarter's claims and grades each one independently against the new sources, then compares. Every disagreement is written up with both verdicts and the evidence. In the pilot this caught one wrong ✅ that the writer's own checks had missed.

## 14. Rubric (self-check and reviewer check)

After reading `business.md` + `outlook.md`, the owner should be able to say yes to all five:

1. Can I explain what this company does, and who pays it, in two sentences?
2. Do I know exactly what would kill it, and what the early warning sign is?
3. Do I know why the margins are what they are, and whether cost scales with usage?
4. Could I predict what the scorecard will check next quarter, from §5 of the outlook alone?
5. Did nothing in the report require knowledge I don't have?

## 15. Refresh procedure (`refresh-company`)

Given a ticker with an existing report and a new quarter:

1. Read `business.md` (for the locked indicators and thesis), the current `outlook.md`, and `scorecard.md`.
2. Run gatherers for the new quarter (§13), respecting as-of discipline for the new quarter.
3. Archive: copy the current `outlook.md` to `quarters/<old QLABEL>-outlook.md` unchanged.
4. Grade: for every claim in the old `outlook.md` §5 (and every ⏳ claim carried in `scorecard.md`), assign a verdict per §9 with one line of evidence. Write the new grading section at the top of `scorecard.md`, update the running tally and the indicator time series.
5. Write the new `outlook.md` per §7, including §6 Tone shift, comparing against the archived outlook and the new transcript.
6. Check `business.md` against the new sources. If anything is now wrong or materially incomplete, prepend a flag per §11. Do not edit the body.
7. Reviewer pass per §13.
8. Commit.

## 16. Git

- The repo root is `finance/`. Commit after each completed research run or refresh: `research(GOOGL): initial report as of 2026-Q1`, `refresh(MRVL): FY2027-Q2`.
- Owner edits to `business.md` (indicator lock, flag resolution) are their own commits.
- Do not commit binaries.

## 17. Lessons (owner feedback log)

Append here whenever the owner gives feedback that changes how reports should be written. Date, what was wrong, what rule changed.

- 2026-09-07 — Initial spec written from the design interview. No feedback yet.
- 2026-09-07 — (pipeline) SEC rejected the User-Agent `company-research-skill contact: owner@localhost` on www.sec.gov/Archives; an email-shaped UA works. §12.1 updated.
- 2026-09-07 — (pipeline) Marvell stopped reporting five end markets in Q4 FY2026; now only "data center" and "communications and other". Five-year end-market tables must note the definition change rather than force old categories.
- 2026-09-07 — (pipeline) Both first drafts ran 30–40% over length and both needed two review cycles. Writers and reviewers had counted words differently; §3 rule 7 now fixes the method and asks first drafts to aim low.
- 2026-09-07 — (pipeline) Common first-draft claim failures: either/or constructions that can never be missed, double-barreled claims with one unobservable half, soft phrases hardened into numbers without saying so. §9 now bans the first two and requires labelling the third.
- 2026-09-07 — (pipeline) Blind re-grade by the refresh reviewer caught one wrong ✅ (GOOGL claim 8: "supply constrained" is not the same as "Cloud revenue was limited"). Made standard in §13.
- 2026-09-07 — (pipeline) Alphabet's Q1 2026 transcript PDF has printed page numbers; the Q2 2026 one does not. Motley Fool machine transcripts for Marvell contain garbled numbers. §3 rule 2 now says how to tag and what to trust.
- 2026-09-07 — (pipeline) Marvell's 10-Q Note 9 changed shape between Q1 and Q2 FY2027 (capacity deposits no longer itemized). §8 now asks that indicators anchor to recurring disclosures.
