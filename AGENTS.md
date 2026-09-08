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
│   ├── refresh-company/SKILL.md
│   ├── draft-valuation/SKILL.md      ← §18: write assumptions.yaml, stop for owner review
│   └── compute-valuation/SKILL.md    ← §18: run the engine, write valuation.md
├── pyproject.toml / uv.lock          ← uv project for the valuation engine (§18.9)
├── tools/
│   └── valuation/                    ← the DCF engine, its tests, and cached Damodaran datasets
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
        ├── review/
        │   ├── <QLABEL>-review.md    ← reviewer's rubric check and citation spot-check
        │   └── <QLABEL>-valuation-draft-review.md   ← §18 reviewer's check of assumptions.yaml
        └── valuation/                ← §18
            ├── assumptions.yaml      ← the single source of valuation inputs (agents write it; the owner edits through the app)
            ├── assumptions.md        ← read-only rendering of the YAML as tables with reasons; regenerated on every save/compute
            ├── valuation.md          ← rendered by the engine: stories, tables, results
            └── history/<date>/       ← previous assumptions.yaml + valuation.md pairs
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
3. **Third-party free** transcript: The Motley Fool (`fool.com/earnings/call-transcripts/...`). URL slugs are inconsistent; discover the link from `https://www.fool.com/quote/<exchange>/<ticker>/` rather than guessing. Check robots.txt permits the path (the `Disallow: /` lines apply to named bots, not `*`). The quote page hides transcript links inside embedded JSON, so grep loosely for `call-transcripts` rather than for `href=`. The monthly sitemap `https://www.fool.com/sitemap/<YYYY>/<MM>` settles whether a transcript exists at all; coverage is patchy (none for AAOI Q2 2026 or MU Q3 FY2026). Fool posts up to a week after the call: a transcript of a pre-cutoff call is admissible even if posted after the cutoff, provided only call content is used and MANIFEST records both the call date and the posting date. Machine transcripts garble numbers and their "(sic)" corrections can themselves be wrong; take numbers from the release.
4. **Owner-supplied** local file, if given as an argument.
5. **None**: proceed with press release, slides, and 10-Q. Mark the outlook header `Transcript source tier: none`, and in §5 list which claims could not be sharpened for lack of a transcript. If the prior quarter's call is pre-cutoff and available, fetch it as a labelled supplement (`transcript-<prev QLABEL>.txt`, tagged `[<prev QLABEL> call]`) for business.md wording and for the "what management had said to expect" column; never use it for current-quarter guidance. When a company publishes prepared remarks but no Q&A (Micron), the header reads `company-published (prepared remarks); Q&A: none`.

Always record the tier used in `outlook.md`'s header and in `sources/<QLABEL>/MANIFEST.md`.

### 12.3 Known company-specific fetch paths (verified 2026-09-07)

**General pattern.** Most IR sites that block plain HTML fetches (Cloudflare or Akamai 403s) are hosted by Q4 Inc. and expose open JSON feeds:
`https://<ir-host>/feed/FinancialReport.svc/GetFinancialReportList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=<YYYY>&excludeSelection=1&reportSubType=` and
`https://<ir-host>/feed/Event.svc/GetEventList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=<YYYY>&excludeSelection=1&eventDateFilter=All`.
Documents live on `s<NNN>.q4cdn.com`. Try the feeds before falling back to 8-K exhibits (works for GOOGL, META, PINS, MU; Broadcom blocks even the feeds). For any filer, list a filing's exhibits via `https://www.sec.gov/Archives/edgar/data/<CIK>/<accession-no-dashes>/<accession-with-dashes>-index.htm`; the bare directory URL returns a landing page with no useful links. Material 8-Ks are sometimes filed by a filing agent under a different accession prefix than the company's own (Broadcom: DFIN's `0001193125`), so scan every 8-K in the submissions JSON up to the cutoff, not just the company-prefixed ones.

**Alphabet (GOOGL, CIK 0001652044)**
- IR HTML pages block plain fetches (Cloudflare). Use the open Q4 Inc. JSON feeds instead:
  - Events (calls, transcripts): `https://abc.xyz/feed/Event.svc/GetEventList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=<YYYY>&excludeSelection=1&eventDateFilter=All`
    Each earnings event lists a transcript PDF attachment on `s206.q4cdn.com`, e.g. `.../doc_events/2026/Jul/22/2026_Q2_Earnings_Transcript.pdf`.
  - Financial reports (slides, release): `https://abc.xyz/feed/FinancialReport.svc/GetFinancialReportList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=<YYYY>&excludeSelection=1&reportSubType=`
    Slides pattern is roughly `.../doc_financials/<YYYY>/q<N>/<YYYY>q<N>-alphabet-earnings-slides.pdf` but casing varies, so read the feed.
- Fiscal year = calendar year.

**Applied Optoelectronics (AAOI, CIK 0001158114)**
- IR site `investors.ao-inc.com` is fetchable with a browser-like UA but drops roughly one connection in three (retry once); the root URL times out, sub-pages work. Each quarter has only a press release, a webcast, and a "Trended Quarterly Financial Results" PDF (`/static-files/<uuid>`, linked from the event page). No slides, no transcript. The release has no cash-flow statement, so the 10-Q is the only cash-flow source. The company's supplemental PDFs contain arithmetic errors; take numbers from the release or 10-Q.
- Transcript: tier 3 (Motley Fool) when it exists; it carried Q1 2026 but not Q2 2026, so Q2 2026 ran at tier none with the Q1 call as a labelled supplement.
- FY2025 10-K contradicts itself on customer concentration (Item 1 vs Item 7) and swaps the CATV / Data Center labels in one Item 7 percentage table; use the notes to the financial statements. "Geographic" revenue is by manufacturing site, not customer location. Fiscal year = calendar year.

**Broadcom (AVGO, CIK 0001730168)**
- `investors.broadcom.com` (every path, including the Q4 `/feed/*.svc` URLs) returns 403 from the Akamai edge even with a browser UA; `www.broadcom.com/company/news` is JS-rendered and empty. Press release only via 8-K Exhibit 99.1 (`avgo-<MMDDYYYY>x8kxex99.htm`). No earnings slides exist.
- Transcript: tier 3 (Motley Fool) only.
- Guidance is given as single "approximately" points, never ranges; claims must be single-direction or labelled sharpenings. The release carries five columns (current, prior quarter, year-ago, two half-years), so most last-quarter comparisons come from it. Filings use curly apostrophes, which defeat ASCII greps. The FY2023 10-K is pre-split (10-for-1 in 2024) and the FY2025 10-K restates; the split itself is not stated in any fetched filing.
- Fiscal year ends the Sunday closest to October 31, named for the calendar year in which it ends; FY2026 ≈ Nov 2025 – Oct 2026.

**Intel (INTC, CIK 0000050863)**
- `https://www.intc.com/financial-info/financial-results` is fetchable with a Mozilla-style UA; each quarter's results box links an earnings release PDF, an earnings deck PDF, a "Prepared Remarks" PDF and the webcast, all on `d1io3yog0oux5.cloudfront.net/_88b01b330621eb4afbd070d5caa4f035/intel/db/887/<id>/...`. The 8-K Exhibit 99.1 (`q<Q><YY>earningsrelease.htm`) is the cleanest press-release source. Neither the deck nor the remarks have printed page numbers (use PDF-page tags).
- Transcript: tier 1 prepared remarks only (scripted portion); Intel never publishes Q&A, and Motley Fool did not carry Q2 2026. Header form: `company-published (prepared remarks only; Q&A not available)`. The remarks contain a "$0.38 cents" slip, so guidance numbers come from the release table.
- Three incompatible segment series across the FY2023, FY2024 and FY2025 10-Ks (NEX folded into CCG/DCAI in Q1 2025; CCG renamed "Client Computing and Physical AI Group (CCPG)" in the Q2 2026 release with no restatement). Intel Products = CCPG + DCAI only; Intel Foundry revenue is mostly intersegment, so track external Foundry revenue separately. 10-Ks after FY2023 anonymize customers (Customer A/B/C) and 10-Qs give no concentration; segment gross margin disappears after the FY2024 10-K. The FY2024 and FY2025 10-Ks give different 2023 Foundry external revenue with no reconciliation.
- Fiscal year is 52/53 weeks ending the last Saturday of December (FY2025 ended 2025-12-27).

**Lumentum (LITE, CIK 0001633978)**
- IR site is Q4 Inc.-hosted and fetchable with a browser UA: quarterly results at `https://investor.lumentum.com/quarterly-results/default.aspx` (`/financials/quarterly-results/` is 404); events at `/events-and-presentations/default.aspx`; deck PDFs on `s21.q4cdn.com/377324469/files/doc_financials/<YYYY>/q<N>/`. No transcript, no supplemental data document.
- The deck's GAAP-to-non-GAAP pages are images (pdftotext yields nothing); take reconciliation numbers from the release. The 10-Ks contain no non-GAAP figures; the release has no cash-flow statement, so quarter-alone capex and operating cash flow for Q4 are FY (10-K) minus nine months (Q3 10-Q), labelled computed. The proxy carries recast non-GAAP margins.
- Transcript: tier 3 (Motley Fool), posted about a week after the call.
- Fiscal year ends the Saturday closest to June 30; Q4 is reported in August with a 10-K, not a 10-Q. FY2027 is a 53-week year. Segments: OpComms / Lasers through FY2023, Cloud & Networking / Industrial Tech FY2024–FY2025, a single reportable segment from FY2026 with only a Components / Systems disaggregation.

**Marvell (MRVL, CIK 0001835632)**
- IR site is fetchable: `https://investor.marvell.com/financial-information/financial-results` lists press release, slides ("financial business results" PDF on cloudfront), and webcast per quarter. No transcript anywhere on the company site or 8-K.
- Transcript: tier 3 (Motley Fool). Verified fetchable as of 2026-09-07.
- Fiscal year ends around the end of January. FY2027 = roughly Feb 2026 – Jan 2027.

**Meta Platforms (META, CIK 0001326801)**
- IR HTML (`investor.atmeta.com`, `investor.fb.com`) returns 403. The Q4 feeds work (general pattern above, host `investor.atmeta.com`). Documents on `https://s21.q4cdn.com/399680738/files/doc_financials/<YYYY>/q<N>/`: `META-Q<N>-<YYYY>-Earnings-Call-Transcript.pdf`, `META-Q<N>-<YYYY>-Follow-Up-Call-Transcript.pdf`, `Earnings-Presentation-Q<N>-<YYYY>.pdf`, and the release `Meta-<MM>-<DD>-<YYYY>-Exhibit-99-1-FINAL.pdf` (casing and suffix vary; read the feed).
- Transcript: tier 1. Meta publishes two company transcripts per quarter, the main call and a same-day CFO follow-up call; cache both (`transcript.txt`, `transcript-followup.txt`). Printed page numbers equal PDF pages. The company transcript footnotes corrections to spoken words; third-party transcripts show the uncorrected word.
- The CFO Outlook Commentary is printed inside the press release. KPI charts (regional DAP, impressions, price per ad) in the 10-Q and 10-K MD&A are images and do not survive text extraction; slides give nine quarters of series but chart pages extract data labels in scrambled order. Meta does not report gross margin. Fiscal year = calendar year.

**Micron (MU, CIK 0000723125)**
- `investors.micron.com` HTML returns 403; the Q4 feeds work with a browser-like UA (general pattern above). PDFs on `s25.q4cdn.com/621799436/files/doc_financials/<YYYY>/q<N>/`, e.g. `Q<N>-FY<YY>-Prepared-Remarks.pdf` and the deck. The `PressRelease.svc` feed returns empty; use the 8-K Exhibit 99.1 for the release.
- Transcript: tier 1 prepared remarks only (CEO and CFO script, no Q&A, no printed page numbers). Motley Fool did not carry Q3 FY2026, so Q&A was unavailable at every tier; expect this to recur.
- Remarks and deck are non-GAAP by default; GAAP guidance appears only in the release's Business Outlook table. Business units were reorganized in FY2025 (Cloud Memory, Core Data Center, Mobile and Client, Automotive and Embedded); the FY2025 10-K recasts FY2023–FY2025 only, so DRAM / NAND revenue is the only consistent five-year series.
- Fiscal year ends the Thursday closest to August 31; FY2026 is a 53-week year with a 14-week Q4. Q4 is reported in late September with the 10-K in early October.

**Nebius Group (NBIS, CIK 0001513845)**
- Foreign private issuer: files 20-F (annual, the 10-K equivalent) and 6-K (quarterly); no 10-K, 10-Q, 8-K or proxy. Management, ownership and pay come from 20-F Items 6–7. The quarterly financial statements arrive in a separate 6-K from the press release (Q1 2026: release 05-13, financials 05-20; Q2 2026: both 08-12). 20-F primary documents are `nbis-<YYYYMMDD>x20f.htm` (older Yandex-era ones `yndx-…`; filer agent changed from 0001558370 to 0001104659).
- IR: `https://nebius.com/investor-hub`, `https://nebius.com/newsroom`, results PDFs on `assets.nebius.com`, all fetchable with a browser-like UA (`group.nebius.com` and `nebius.com/investor-relations` are 404). No slide deck; a two-column CEO letter replaces it and defers numeric guidance to the call, so the transcript gatherer is load-bearing for guidance. Cache a reading-order `pdftotext` copy alongside `-layout` for the letter.
- Transcript: tier 3 (Motley Fool), posted a week after the call. Q&A is IR reading portal questions aloud, so there are no analyst speaker labels.
- No gross profit is reported (cost of revenue excludes D&A); gross margin is a labelled computation. Formerly Yandex N.V. (renamed 2024-08-16); revenue history exists on a continuing basis only from FY2023. Fiscal year = calendar year.

**Pinterest (PINS, CIK 0001506293)**
- IR HTML is Cloudflare-blocked; the Q4 feeds are open with the standard UA (general pattern above, host `investor.pinterestinc.com`). The FinancialReport feed lists press release, presentation, the company transcript PDF and the 10-Q per quarter on `s204.q4cdn.com/369458543/files/doc_earnings/<YYYY>/q<N>/`.
- Transcript: tier 1, with printed page numbers equal to PDF pages.
- KPI tables (regional MAU, ARPU) in the 10-K and 10-Q are chart images; use the press release. Each 10-K states regional revenue and ARPU in MD&A prose for its own year only, so five-year regional tables need every 10-K in the window. Slides scramble chart labels under `pdftotext -layout`; `pdftotext -bbox` plus a low-resolution `pdftoppm` render fixes the quarter mapping. Slides also insert spaces inside words ("non -GAAP"). Fiscal year = calendar year.

**Rocket Lab (RKLB, CIK 0001819994)**
- Same registrant throughout the 2025 redomiciling: EDGAR lists "Rocket Lab USA, Inc." as a former name to 2025-05-23, now "Rocket Lab Corp"; there is no successor CIK. IR host is `investors.rocketlabcorp.com`; direct HTTP/2 requests fail intermittently (curl error 92), so go through the `investors.rocketlabusa.com` 301 redirect or use `--http1.1`. Key pages: `/financial-information/quarterly-results`, `/events-presentations/presentations`, `/events/event-details/<quarter>-financial-results-update-and-conference-call`; slide PDFs under `/static-files/<uuid>`.
- Earnings decks are image-only PDFs with no text layer: `pdftoppm` plus `tesseract` OCR, then visually verify chart pages (one OCR misread, "$966M" for $266M, was caught). Segment revenue and backlog live only in the slides and the 10-Q; the press release carries neither table, and launch counts for the quarter are only in the 10-Q.
- Transcript: tier 3 (Motley Fool), posted a week after the call; the company has published exactly one transcript ever (a May 2025 acquisition call). The machine transcript garbled the guidance period ("second quarter" for Q3), so guidance numbers come from the release. Fool's editorial set now includes a "RISKS" block; keep only the Date / Participants / Full transcript sections rather than naming blocks to drop.
- 8-K exhibits are `rklb-MMDDYYYYex991.htm`; resolve them from the accession folder index. 8-Ks filed via agent 0001753926 break "Item" and its number onto separate lines, so grep the item title text. The 10-Q has no subsequent-events note; post-quarter contracts sit in MD&A "Recent Developments". Fiscal year = calendar year.

### 12.4 Caching

Everything the agents read is saved as extracted text under `companies/<TICKER>/sources/<QLABEL>/`. PDFs are converted with `pdftotext -layout`; HTML is stripped to text. `MANIFEST.md` lists every file with its origin URL, fetch date, and (for transcripts) the source tier. Re-runs read from cache before fetching.

### 12.5 As-of discipline

A report "as of Q1" must not use any information published after that quarter's earnings call and 10-Q. Gatherers fetch only documents dated on or before the as-of cutoff. Writers must not use knowledge of later events. This is what makes the scorecard honest.

## 13. Orchestration: gather → write → review

Each company runs as an independent pipeline; multiple companies run in parallel.

### Gatherers (parallel, one per source type)

Each gatherer fetches its sources, caches extracted text (§12.4), and writes a structured notes file `sources/<QLABEL>/notes-<type>.md` and its own `MANIFEST-<type>.md` part; the runner merges the parts into `MANIFEST.md` so parallel gatherers never write the same file. Notes are bullet facts, each with a source tag and page/section reference. Gatherers do not write prose for the report and do not interpret beyond what the source says.

- **filings** gatherer: latest 10-K and the as-of 10-Q. Extracts: business description, segments, revenue by segment (5 years, from current and prior 10-Ks as needed), margins, cash flow, capex, share count, buybacks, customer concentration, risk factors that are specific (not boilerplate), management and ownership, compensation structure from the proxy if easily available. Also scan every 8-K filed up to the cutoff (including those under a filing agent's accession prefix) and cache the material ones: officer changes, large customer or financing agreements, vote results. If the brief is large, cache all filings first and write notes second, so a mid-run failure can be resumed from the cache.
- **transcript** gatherer: the as-of quarter's call. Extracts: every forward-looking statement and guidance item verbatim; management's description of vision and growth engines; every question analysts asked and the substance of the answer; anything management declined to answer.
- **ir** gatherer: press release and slides for the as-of quarter, plus the prior quarter's press release (`press-release-<prev QLABEL>.txt`), which fills outlook §1's "what management had said to expect" column directly. Extracts: reported metrics, any KPIs the company highlights that are not in the 10-Q, guidance table, non-GAAP reconciliations. Where KPI or reconciliation pages are images, say so in the notes and take the numbers from the release.

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
- Valuation (§18): `value(GOOGL): draft assumptions as of 2026-Q2` after `draft-valuation`; `value(GOOGL): compute 2026-Q2 rev N` after each `compute-valuation` (N counts computes for that as-of quarter, starting at 1). Owner edits to `assumptions.yaml` may ride along with the compute commit that follows them.
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
- 2026-09-07 — (pipeline) Second batch, nine companies in parallel (AAOI, AVGO, INTC, LITE, META, MU, NBIS, PINS, RKLB), one runner per company each spawning gatherers → writer → reviewer, planner committing centrally. SEC returned 200 on every request at ≥1 s spacing with the §12.1 UA despite nine pipelines on one IP. Q4 Inc. JSON feeds were the reliable path for blocked IR sites; the general pattern and per-company paths are now in §12.3.
- 2026-09-07 — (pipeline) Motley Fool posts transcripts up to a week after the call (LITE, META, NBIS, PINS) and skips some calls entirely (AAOI Q2 2026, MU Q3 FY2026). §12.2 now says a pre-cutoff call posted after the cutoff is admissible with both dates in MANIFEST, how to check existence via the monthly sitemap, and how to run tier none with the prior quarter's call as a labelled supplement.
- 2026-09-07 — (pipeline) Five of seven pipelines fetched the prior quarter's press release to fill the "what management had said to expect" column; made standard for the ir gatherer in §13. Broadcom's CFO-change 8-K was missed by the filings gatherer because it carried DFIN's accession prefix; §13 filings gatherer now scans all pre-cutoff 8-Ks.
- 2026-09-07 — (pipeline) Segment definitions changed mid-window at LITE (twice), MU (FY2025 reorg) and NBIS (basis changes); as with Marvell, the writers used the consistent series (product or technology line) and footnoted the reorg rather than forcing a five-year table.
- 2026-09-07 — (pipeline) Length: when writer and reviewer ran the same counting script their counts agreed within a few words and no review cycle was length-driven. Reviewer glosses add about 5%, so a draft near 2,800 leaves no room; the one single-cycle PASS (AVGO) came from a hard 2,000–2,500 aim. Pipelines each rewrote a counter in `/tmp` and one was overwritten by another pipeline mid-run; a canonical script committed to the repo (e.g. `tools/wc_prose.py`) would end the re-derivation. Owner to decide.
- 2026-09-07 — (pipeline) Reviewer gotcha in two pipelines (PINS, NBIS): truncating grep output (`| head`, character cut) hid the end of a long proxy line and produced a false FAIL. Print full lines before ruling a fact unsourced. Treat "n/d" cells like any other number and check the alternate-basis filing used for that column. Reviewer withdrawals must be recorded in the review file with the evidence.
- 2026-09-07 — (valuation) §18 designed in a second grill-me interview and built the same day: engine `tools/valuation/` (63 tests; reproduces Damodaran's Alphabet 2018 and Nvidia 2023 workbooks to the dollar), skills `draft-valuation` and `compute-valuation`, drafts for GOOGL and MRVL. Lessons: (1) his Alphabet 2018 sheet has no reinvestment lag while ginzu does; `switches.reinvestment_lag` records the choice, default 1 per §18.3. (2) FRED timed out once for the engine builder and worked before and after; the CLI names the `--set market.risk_free_rate=` fallback. (3) Both drafts needed two review cycles. Reviewers caught a preferred-stock arithmetic slip (19,000 vs 19,250, Alphabet), a bear path whose half-year arithmetic did not match its reason (Marvell), and, most usefully, a capex-versus-margin inconsistency: sales-to-capital alone made Alphabet's 2027 capex fall below 2026's against explicit guidance, so year-2 overrides were added and the bull margin lowered. Rule for future analysts: whenever guidance names a spending level, check what the sales-to-capital path implies for gross capex in every explicit year and override where they disagree. (4) A hard-coded terminal growth goes stale; `value: riskfree` is now the default written into drafts. (5) The engine derives unlevered beta and market debt-to-equity when the analyst leaves them null, with a warning; the runner still fills them explicitly so the owner sees the numbers and dates.
- 2026-09-07 — (valuation) Owner feedback: YAML is too hard to read and edit. Rule: the owner never edits `assumptions.yaml` by hand; `assumptions.md` is the readable view and the app (§18.10) is the editor, saving back into the YAML with a `changelog`. Skills now point the owner at `assumptions.md` and the app, never at the YAML.
- 2026-09-07 — (valuation) Owner feedback on the first app: "not very good": everything crammed into tabs, not intuitive, some math symbols not rendering. Rule: the app is a guided walk, one factor per page in order of impact (stories first, then revenue and margin, then the rest ranked), each page explains the factor and asks for the owner's number, results only at the end; no LaTeX or `$` in markdown; a separate UI audit with screenshots before showing the owner. §18.10 rewritten.
- 2026-09-08 — (valuation) Guided-walk app: two screenshot audits (Playwright, `tools/valuation/ui-audit/`). Cycle 1 found 5 blockers, mostly engine messages and raw YAML paths leaking to the screen and tables clipping their own rows; cycle 2 confirmed all blockers fixed and left a wording punch list. Lessons: (1) every engine or validator message shown to the owner goes through one translation function; nothing raw reaches the page. (2) YAML reasons must not cite the spec ("§18.4 rule 5") or name keys; the owner reads them verbatim. (3) The app must detect the assumptions file changing on disk mid-session and refuse Save rather than list the agent's edits as the owner's. (4) FRED serves the DGS10 CSV instantly to Python's default User-Agent and times out on browser-like agents; the engine sends a plain identifying agent to FRED and the browser agent only to Yahoo. (5) Playwright on this host must run with cwd outside `/tmp` and `python -P`. (6) Cycle 3 found a whole page killed by a working-notes table with two identical column headers; the renderer now de-duplicates, pads, and falls back to raw text, because analyst content must never stop a page from rendering.
- 2026-09-08 — (valuation) Owner feedback on the GOOGL draft: assumptions "very pessimistic"; the price should sit at most between base and bull, year 1 should be about this year's growth, and growth should not collapse within five years. Diagnosis, by size of effect on the base case (220 a share against a price of 338 after the owner's own edits): (1) the 5-year default plus the terminal rules built a cliff at year 6 (return on capital 22% to 11.75%, growth 13% to 4.75%, tax 16.8% to 25%, all in one step; terminal-year cash flow 29% below year 5), and for a company spending 45% of revenue on capex the short structure charges the investment in full and stops crediting the growth it buys; the default is now Damodaran's own ten years as five explicit plus five faded by rule (§18.2), the 5-year stop is the reference row, and a transition check flags cliffs; (2) the terminal return-on-capital ceiling (5 points, "err low") made a 24%-return business earn 11.75% forever in the base case; the soft thresholds are now 8 (base) and 12 (bull) points with Damodaran's own 4 and 11.5 as anchors, and terminal return must sit below today's (§18.4 rule 5); (3) analyst drafting: year 1 at 20% against a reported 23%, a fade to 8% anchored on 2022–23 growth from a different business mix while Cloud grew 82% on a backlog above a year of revenue, and sales-to-capital set against same-year figures while the engine lags spending by a year; rules 10–13 added and the reviewer checklist extended (§18.7). Lesson: "prefer the structure less likely to overvalue" was applied to the wrong object; a structure inconsistent with its inputs is not conservative.
- 2026-09-07 — (pipeline) Host quirks: a stray `/tmp/inspect.py` shadows a stdlib module and breaks BeautifulSoup for any Python run with cwd `/tmp` (use `python3 -P` or another cwd); `/tmp` is shared across pipelines, so use pipeline-specific file names; host `grep` is ugrep and rejects long regex alternations (use `grep -F`); filings use curly apostrophes that defeat ASCII greps; two-column PDFs need a reading-order `pdftotext` copy; image-only pages need OCR or the release. A large gatherer died on an API error after caching but before writing notes (MU); relaunching against the cache recovered it, hence the fetch-then-notes order in §13.

## 18. Valuation (`draft-valuation`, `compute-valuation`)

Valuation is a separate layer on top of the research library. It never edits `business.md`, `outlook.md`, or `scorecard.md`. It reads them, plus the cached filings, and produces one editable file of assumptions and one rendered document of results. The owner's judgment lives in the assumptions file; the engine only does arithmetic.

### 18.1 Method in one paragraph

We follow Aswath Damodaran's free-cash-flow-to-the-firm model as implemented in his public `fcffsimpleginzu.xlsx`. Operating profit after tax, minus the reinvestment needed to grow, gives the cash the whole firm produces each year. Those cash flows are discounted at the firm's cost of capital (the blended return lenders and owners require). A terminal value captures everything after the forecast, under strict rules: growth capped at the risk-free rate, and a return on capital that by default equals the cost of capital, so the moat is assumed gone. Cash and non-operating assets are added, debt and other claims subtracted, and the result divided by diluted shares. Everything stays firm-side until that last step (§18.6).

Reader rules from §3 apply to every prose sentence in `valuation.md`: the scenario stories are written for the 16-year-old, numbers live in tables, and the glossary holds only unavoidable terms (cost of capital, terminal value, reinvestment, enterprise value, and the like), one sentence each.

### 18.2 Horizon and structure

- **Default horizon: 10 years, built as five explicit years plus a five-year fade by rule.** This is the structure of Damodaran's own `fcffsimpleginzu.xlsx` and of both workbooks our tests reproduce (Alphabet 2018, Nvidia 2023). The analyst judges years 1–5 (`values` lists of five). The engine builds years 6–10: revenue growth moves linearly from year-5 growth to terminal growth; the operating margin holds at the year-5 level; sales-to-capital uses `value_late`; tax rate and cost of capital move linearly to their terminal values; reinvestment overrides may carry ten entries, otherwise years 6–10 use the ratio; terminal value at year 10. An analyst with a sourced reason to shape years 6–10 differently writes ten-entry lists; the app and `assumptions.md` then show all ten.
- **Why the default changed (2026-09-08).** The first version defaulted to five explicit years then terminal value, on the argument that the shorter structure was less likely to overvalue a fast grower. For a company investing far ahead of its revenue (Alphabet in 2026 spends about 45% of revenue on capital equipment) the short structure is not conservative but inconsistent: it charges the whole investment in years 1–2, stops crediting the growth it buys at year 5, and moves growth, return on capital and tax from their year-5 values to their stable values in one step. In the GOOGL draft the terminal-year free cash flow came out 29% below year 5's. Damodaran's rule: the move to stable growth is gradual for firms far from stable, and firms with high growth and strong competitive advantages get the longer growth period. "Choose the structure less likely to overvalue" never meant "choose the lower number"; a structure that contradicts its own inputs is wrong in both directions. See §17.
- **The 5-year-stop reference value is always computed and shown** next to each case (same inputs, terminal value at year 5, terminal settings applied in year 6), so the owner still sees what the shorter structure would give. `horizon: 5` remains allowed for a company already close to stable growth; its reference row then shows the 10-year fade.
- **Transition check.** For every case the engine reports the terminal-year free cash flow against the final explicit year's, and the terminal return on capital against the final year's implied return, and flags a cliff when the terminal-year cash flow is below the final year's. A flagged cliff means the terminal settings and the final-year inputs disagree; the reviewer resolves it, usually by revisiting the terminal return on capital or the shape of the fade, and never by accepting it silently.
- End-of-year discounting, as in his sheet.

### 18.3 Formulas (the engine implements exactly these; tests reproduce his workbooks)

All money in USD millions. `T` = horizon. For year `t = 1..T`:

```
Rev_t      = Rev_{t-1} × (1 + g_t)                       Rev_0 = base-year TTM revenue
EBIT_t     = Rev_t × m_t                                  m_t = operating margin path
Tax_t      = effective rate (years 1..T in the 5-year model; see §18.2 for the fade)
Reinv_t    = (Rev_{t+1} − Rev_t) / SC        (one-year lag: money spent in t buys growth in t+1)
             where Rev_{T+1} = Rev_T × (1 + g_T), and an explicit per-year override replaces the S/C figure when given
FCFF_t     = EBIT_t × (1 − Tax_t) − Reinv_t
DF_t       = Π_{k=1..t} 1 / (1 + WACC_k)                  (cumulative, so a fading rate is handled)

Terminal (year T+1, growing at g_T forever):
EBIT_{T+1}  = Rev_T × (1 + g_T) × m_T
ROIC_T      = WACC_T + premium                            premium defaults to 0
FCFF_{T+1}  = EBIT_{T+1} × (1 − Tax_T) × (1 − g_T / ROIC_T)     (reinvestment = g / ROIC)
TV          = FCFF_{T+1} / (WACC_T − g_T)
PV(TV)      = TV × DF_T

Operating assets  = Σ FCFF_t × DF_t + PV(TV)
                    × (1 − p_fail) + distress_proceeds × p_fail        (p_fail defaults to 0)
Equity            = Operating assets + cash & marketable securities + non-operating assets
                    − debt − operating-lease liabilities − minority interests − other claims
Per share         = Equity / diluted shares
Enterprise value  = price × diluted shares + debt + leases + minorities + other claims
                    − cash − non-operating assets            (the like-for-like comparison to Operating assets)
```

Cost of capital build (when `method: build`):

```
levered beta   = unlevered beta × (1 + (1 − marginal tax) × D/E)
cost of equity = risk-free + levered beta × equity risk premium
WACC           = E/(D+E) × cost of equity + D/(D+E) × pre-tax cost of debt × (1 − marginal tax)
terminal WACC  = risk-free + mature-market ERP   (method `mature`, default)
               | the company's own WACC          (method `hold`)
               | a given number                   (method `value`)
```

Return on invested capital is after-tax EBIT divided by invested capital (book equity + debt + leases − cash), tracked each year by rolling invested capital forward with reinvestment; it is printed as a check, never used as an input.

### 18.4 `assumptions.yaml` — the single source of inputs

Every input cell is a mapping with `value`, `reason`, and where the number comes from a document, `source` (a §3-style tag). Per-year inputs use `values`: a list of five numbers for years 1–5 (years 6–10 follow the §18.2 rule), or ten when the analyst shapes the fade years explicitly. Any cell may be `null` where the analyst has nothing defensible; the engine refuses to compute a scenario with a `null` in a required cell and says which. Rates are decimals (`0.12`, not `12%`). Reasons are one to three plain sentences that point at the report (`business.md §3`, `outlook.md §4`) and, where a number is involved, at a source. Any cell may also carry `detail`: the working notes behind the reason (history tables, the arithmetic, the alternatives considered), as long as needed. The app shows `detail` in a fold-out under the reason and `assumptions.md` prints it after the reason; nothing goes into YAML comments, because the owner never sees comments.

```yaml
schema: 1
ticker: MRVL
company: Marvell Technology, Inc.
as_of_quarter: FY2027-Q2         # the library's latest outlook quarter
as_of_date: 2026-08-28           # that quarter's cutoff date
drafted: 2026-09-07
currency: USD
units: millions
horizon: 10                      # five explicit years plus five faded by rule (§18.2); the 5-year-stop reference is always computed too

base_year:                       # trailing twelve months ending at as_of_quarter
  period: "Q3 FY2026 – Q2 FY2027 (TTM)"
  revenue:                      {value: 0, source: "[...]"}
  operating_income_gaap:        {value: 0, source: "[...]"}
  one_time_items:               # each: positive = a charge to add back, negative = a gain to remove
    - {name: "...", value: 0, source: "[...]", reason: "why this is genuinely one-time"}
  amortization_of_acquired_intangibles: {value: 0, source: "[...]"}   # memo row; deducted unless the switch is on
  stock_based_compensation:     {value: 0, source: "[...]"}           # memo row; never added back
  rnd_expense:                  {value: 0, source: "[...]"}           # memo row; used only if capitalize_rnd
  effective_tax_rate:           {value: 0.0, source: "[...]", reason: "..."}
  invested_capital:             {value: 0, source: "[...]", reason: "book equity + debt + leases − cash; for the ROIC check"}
switches:
  addback_acquired_amortization: false
  capitalize_rnd: false
  rnd_amortization_years: 5
  rnd_history: []               # oldest first, at least rnd_amortization_years entries, if capitalize_rnd
  reinvestment_lag: 1           # 1 = money spent in year t buys growth in t+1 (§18.3, his ginzu sheet); 0 = same-year (his Alphabet 2018 sheet)

bridge:                          # firm value → equity; all as of the latest balance sheet
  cash_and_marketable_securities: {value: 0, source: "[...]"}
  debt:                           {value: 0, source: "[...]"}
  operating_lease_liabilities:    {value: 0, source: "[...]"}
  non_operating_assets:           # named, at carrying value
    - {name: "...", value: 0, source: "[...]", reason: "..."}
  minority_interests:             {value: 0, source: "[...]"}
  other_claims:                   # e.g. contingent consideration, earn-outs
    - {name: "...", value: 0, source: "[...]"}
  probability_of_failure:         {value: 0.0, reason: "..."}
  distress_proceeds:              {value: 0, reason: "what the assets would fetch in a failure"}
  diluted_shares:                 {value: 0, source: "[...]", reason: "latest-quarter diluted weighted average"}
  dilution_note: "known future dilution sources, one sentence"

market:
  price: auto                    # 'auto' = fetched at compute time (Yahoo chart endpoint), or a number
  risk_free_rate: auto           # 'auto' = FRED DGS10 latest, or a decimal
  equity_risk_premium: auto      # 'auto' = latest row of Damodaran's ERPbymonth.xlsx (cached), or a decimal
  mature_market_erp: 0.045       # Damodaran's mature-market default
  marginal_tax_rate: 0.25

cost_of_capital:
  method: build                  # build | pinned
  pinned_value: null
  build:
    damodaran_industry:     {value: "Semiconductor", reason: "..."}
    unlevered_beta:         {value: 0.0, source: "[Damodaran betas.xls <date>, <industry>]", reason: "..."}
    debt_to_equity_market:  {value: 0.0, source: "[...]", reason: "debt + leases over market cap"}
    pretax_cost_of_debt:    {value: 0.0, source: "[...]", reason: "actual coupon / synthetic rating"}
  terminal:
    method: mature               # mature | hold | value
    value: null
    reason: "..."

diagnostics:
  final_year_market_size:   {value: null, source: "[...]", reason: "the 'big market' test: total spend the company could address in year T"}
  historical_revenue_cagr:  {value: null, source: "[...]", reason: "optional: the company's own five-year revenue growth, for the 'vs own history' check"}
  historical_operating_margin: {value: null, source: "[...]", reason: "optional: the company's own five-year average GAAP operating margin"}

scenarios:
  bear:
    weight: 0.25
    story: |
      Three to five plain sentences: what has to be true for this case.
    revenue_growth:        {values: [0, 0, 0, 0, 0], reason: "...", source: "[...]"}
    operating_margin:      {values: [0, 0, 0, 0, 0], reason: "...", source: "[...]"}
    sales_to_capital:      {value: 0.0, value_late: 0.0, reason: "...", source: "[...]"}
    reinvestment_override: {values: [null, null, null, null, null], reason: "explicit net reinvestment in USD millions where guidance is specific; null = use sales-to-capital"}
    tax_rate:              {start: 0.0, terminal: 0.25, reason: "..."}
    cost_of_capital_override: null          # a decimal pins this scenario's WACC; null = shared
    terminal:
      growth:              {value: riskfree, allow_above_riskfree: false, reason: "..."}   # 'riskfree' = the run's risk-free rate (Damodaran's default), or a decimal
      roic_premium:        {value: 0.0, allow_large_premium: false, reason: "points above terminal WACC; bear is 0"}
  base:  { ... same keys ..., weight: 0.50 }
  bull:  { ... same keys ..., weight: 0.25 }
  management:
    computable: false            # true only when at least one multi-year revenue or margin target exists
    reason: "..."
    guidance:                    # every quantitative or qualitative item management has given, whether used or not
      - {item: "...", quote: "verbatim", source: "[...]", used_as: "revenue_growth year 1 | reinvestment year 1 | not numeric"}
    revenue_growth:        {values: [null, null, null, null, null], reason: "...", source: "[...]"}
    operating_margin:      {values: [null, null, null, null, null], reason: "...", source: "[...]"}
    sales_to_capital:      {value: null, value_late: null, reason: "..."}
    reinvestment_override: {values: [null, null, null, null, null], reason: "..."}
    tax_rate:              {start: null, terminal: 0.25, reason: "..."}
    cost_of_capital_override: null
    terminal:
      growth:              {value: null, allow_above_riskfree: false, reason: "..."}
      roic_premium:        {value: null, allow_large_premium: false, reason: "..."}
```

An optional top-level `sources:` list maps every tag used in the file to its cached text: `- {tag: "10-Q Q2 FY2027", file: "sources/FY2027-Q2/10-Q-FY2027-Q2.txt", date: "2026-08-28", note: "..."}`. `assumptions.md` prints it as its Sources table. Two more optional top-level blocks the engine and the app maintain; analysts never write them:

```yaml
owner_edited: 2026-09-08T10:12:00      # last save from the app
changelog:                              # appended by the app on every save, oldest first
  - {at: "2026-09-08T10:12:00", path: "scenarios.base.operating_margin.values.4", old: 0.30, new: 0.32, note: "owner: depreciation offsets look achievable"}
```

**Rules for the analyst filling it in:**

1. **Base year is GAAP.** Operating income as reported, minus items the analyst can source as genuinely one-time (a gain on a divestiture, a termination charge). Recurring-at-intervals charges are not one-time. Stock-based pay stays expensed, always. Amortization of acquired intangibles stays deducted; it is recorded as a memo row and its roll-off must be addressed in the margin-path reasoning. The `switches` exist so the owner can change either treatment for a specific company; the analyst leaves them off.
2. **Interest income and interest expense are not in operating income.** Cash is valued in the bridge, not in the cash flows.
3. **Sources first, reports second, nothing new.** Base-year and bridge numbers come from the cached 10-Q/10-K text in `sources/<QLABEL>/`, tagged. Scenario reasoning points to `business.md` and `outlook.md` sections and to the sources they cite. The analyst fetches nothing from the internet. Market data and Damodaran's datasets are the engine's job.
4. **Management case.** Guidance ranges become midpoints. Qualitative guidance ("capex up significantly") is recorded in `guidance` with `used_as: not numeric` and never turned into a number. Long-term targets already captured in the reports count. `computable` is true only when management has given at least one multi-year revenue or margin target; otherwise fill what exists and leave `computable: false`. The management case is never weighted. Guidance is mapped to the nearest model year and the approximation noted, since fiscal years and trailing-twelve-month windows do not line up.
5. **Terminal discipline.** Terminal growth defaults to the risk-free rate: write `value: riskfree` and the engine uses the rate fetched for that run. A number above the run's risk-free rate is a validation error for that scenario unless `allow_above_riskfree: true` is set with a reason, in which case the engine computes and prints a warning. It may be lower or negative with a reason. Terminal return on capital equals terminal cost of capital in the bear case (`roic_premium: 0`): the moat is gone. Base and bull carry a premium justified from `business.md` §5 and anchored on the company's own record: the resulting terminal return on capital must sit below the base-year return on capital and below the final explicit year's implied return, and the reason says where between the cost of capital and today's return the company lands, and why. Damodaran's own choices for firms with strong moats were 4 points (Alphabet 2018: stable return 12% against a stable cost of capital of 8%) and 11.5 points (Nvidia 2023: 20% against 8.85%). A base premium above 0.08 or a bull premium above 0.12 requires `allow_large_premium: true` and a reason, and the engine prints a warning. A premium set so low that the §18.2 transition check flags a cliff for a wide-moat company is an error, not caution (GOOGL lesson, 2026-09-08: 3 points made a 24%-return business earn 11.75% forever and cut the terminal-year cash flow 29% below year 5).
6. **Cost of capital is shared** across scenarios unless a scenario sets `cost_of_capital_override` with a reason. Scenarios vary the business story, not the market's price of risk.
7. **Weights** default 0.25 / 0.50 / 0.25 and must sum to 1.
8. **Every story passes Damodaran's 3P test** in the reviewer's hands: is it possible (year-T revenue below the market size), plausible (margins and reinvestment consistent with the economics in `business.md` §3–§4), probable (consistent with what the scorecard shows management actually delivering)?
9. **Stories are prose for the 16-year-old**, three to five sentences, no numbers except the one or two that define the case.
10. **Year 1 starts where the company is.** Year-1 revenue growth starts from the latest reported run-rate (the most recent half-year or quarter against the year-earlier period, stated with its source) and moves off it only for a specific, sourced reason named in the reason: guidance for the coming year, a comparison-period effect management has called out, a contract won or lost, capacity that is or is not arriving. "Growth slows because the company is big" is not a reason. (GOOGL lesson, 2026-09-08: the first draft wrote 20% against a reported 23%.)
11. **Growth is built from the parts, not from the past.** The revenue-growth `detail` of every computed case carries a segment build: each reported segment or product line with its trailing revenue, its latest growth, and the growth assumed for it in years 1, 3 and 5, summing to the company path. Where the reports hold a backlog, a market size or a capacity plan, the build uses it. The company's own five-year history and the industry figure are context in the diagnostics, not anchors: a company whose mix has changed (a cloud unit that was 10% of revenue and is now 25%) does not fade back to the growth its old mix produced. Every step down of more than three points between one year and the next has one sentence naming the driver (backlog conversion slowing, a market filling up, a product cycle ending). (GOOGL lesson: the first draft faded to 8% by year 5 "toward the single digits of 2022–2023" while Cloud, a quarter of revenue, was growing 82% with a backlog above a year of company revenue.)
12. **Reinvestment history is measured the way the model spends it.** With `switches.reinvestment_lag: 1` (the default: this year's spending buys next year's growth) the sales-to-capital history in `detail` is computed lagged the same way, and the chosen ratio is set against that lagged record. A same-year ratio taken during an investment surge is depressed by construction and is not the comparison. (GOOGL lesson: 0.9 was chosen against same-year figures of 0.64–0.75 while the lagged record read 1.2–2.1.)
13. **Margins carry their own bridge.** A margin path that moves more than two points over the five years shows, in `detail`, both forces side by side: the depreciation the reinvestment path will create (from the capex plan and the asset lives management gives) and the offsets (mix shift toward higher-margin units, costs growing slower than revenue, the operating leverage the reports describe). A path that shows only the drag is incomplete.

### 18.5 Outputs (`valuation.md`, rendered by the engine)

In this order:

1. Header: ticker, as-of quarter, price and its date, risk-free rate and its date, equity risk premium and its date, compute timestamp, engine version.
2. **Results table**, one row per case (bear, base, bull, management if computable, weighted expected): value of operating assets, enterprise value today, equity value, value per share, price, upside or downside, terminal-value share of operating assets, and the reference value per share from the other structure (the 5-year stop when `horizon` is 10; the 10-year fade when it is 5).
3. **The stories**, one short section per scenario, verbatim from the YAML.
4. **Assumptions table**: rows are inputs, columns are cases, per-year lists shown as five columns; followed by a reasoning list per scenario (each cell's `reason` and `source`).
5. **Base year, bridge, cost of capital, and terminal tables** with sources and the derived numbers (adjusted operating income, levered beta, cost of equity, WACC, terminal WACC, terminal ROIC).
6. **Base-case year-by-year table**: one row per model year (ten by default, the fade years marked "by rule"), then the terminal year: revenue, growth, margin, after-tax operating income, reinvestment, free cash flow, discount factor, present value, implied ROIC.
7. **Sensitivity grids** for the base case: cost of capital × terminal growth; average 5-year revenue growth × year-5 margin. Value per share in each cell; the base-case cell marked.
8. **Reverse DCF**: the constant annual revenue growth over the horizon that, with base-case margins, reinvestment, cost of capital, and terminal settings, makes operating assets equal today's enterprise value. Also the year-5 margin that does the same at base-case growth.
9. **Diagnostics** (Damodaran's six plus the transition check): revenue growth vs industry average and the company's own five-year history (labelled as context, not an anchor, per rule 11); year-T revenue vs `final_year_market_size`; year-5 margin vs industry average and own history; implied ROIC path vs cost of capital; terminal-value share; a flag when value per share is above 2× or below 0.5× the price; and the §18.2 transition check (terminal-year free cash flow and return on capital against the final explicit year, flagged on a cliff). Industry figures come from the cached datasets (§18.8) and are labelled with their dataset date.
10. **Warnings**: every rule override, every `null` that stopped a scenario, any fetch that fell back to a manual value.
11. Glossary and Sources (the YAML's source tags mapped to cached files, plus dataset and feed URLs with fetch dates).

### 18.6 Firm-side consistency

Cash flows are to the firm (before interest), discounted at the cost of capital, never at the cost of equity. Cash and marketable securities are excluded from the cash flows and added in the bridge; Damodaran's reason is that cash earns the riskless rate and discounting it at an operating cost of capital misvalues it. Debt is excluded from the cash flows and subtracted in the bridge; the interest tax shield sits in the after-tax cost of debt, not in the cash flows. The like-for-like market comparison is operating assets against enterprise value; the reverse DCF solves on enterprise value. Return on capital, never return on equity.

### 18.7 Procedures

**`draft-valuation <TICKER>`** (stops for owner review; computes nothing):

1. Preconditions: `business.md` and `outlook.md` exist; `valuation/assumptions.yaml` does not (else tell the owner to edit it or pass `--redraft`, which archives the old pair to `history/`). If the archived file carries a `changelog`, the owner-edited cells are handed to the analyst as the owner's own view: the analyst still builds every number from the sources and the rules, and wherever its number differs from the owner's, its `detail` says so and the report to the owner shows the two side by side. The owner's values are never silently overwritten and never silently kept.
2. Launch one **analyst** subagent with AGENTS.md (§3, §18), `business.md`, `outlook.md`, `scorecard.md` if present, and read access to `sources/`. It writes `valuation/assumptions.yaml` per §18.4. Cells that need Damodaran's datasets or the market price (unlevered beta, market debt-to-equity) it leaves `null`, stating the industry or the numerator in the reason.
3. The runner fills those cells from the cached datasets (§18.8) and the fetched price, recording dataset and price dates in each cell's `source`, then runs `uv run value <TICKER> --validate` until it passes.
4. Launch one **reviewer** subagent. It writes `review/<QLABEL>-valuation-draft-review.md` with: (a) every base-year and bridge number re-checked against the cached source, listing failures; (b) the 3P test on each story with one line each; (c) consistency checks: year-1 growth against the latest reported run-rate (rule 10); the segment build present, sourced and summing to the path (rule 11); sales-to-capital set against the lagged history (rule 12); the margin bridge showing both drag and offsets (rule 13); amortization roll-off addressed; management case built only from recorded guidance; terminal rules respected, including terminal return on capital below the base-year and final-year returns; weights sum to 1; and the §18.2 transition check, which the reviewer reads from `uv run value <TICKER> --dry-run` (it records flags and the terminal-versus-final-year cash flows, never values per share, so the owner still meets the values first in the app); (d) reader check on the stories and reasons: every reason is one to three plain sentences, working numbers live in `detail`, nothing substantive sits in YAML comments; (e) PASS or REVISE with a list. Maximum two cycles.
5. Commit `value(<TICKER>): draft assumptions as of <QLABEL>`.
6. Report to the owner: the four stories in one line each, the five inputs most worth their attention, anything the analyst could not source, and the exact command to compute.

**Owner editing (the app, §18.10).** The owner does not edit YAML by hand. `uv run valuation-app` opens a local page that shows every input with its reason, recomputes live through the same engine, and on **Save** writes changed values back into `assumptions.yaml`, preserving reasons, sources, and comments, appending a `changelog` entry per changed cell (with the owner's note if given), and regenerating `assumptions.md`. **Write valuation.md** in the app runs the same code path as `compute-valuation` steps 2–3; **Commit** runs step 4. An agent that later reads a YAML with a `changelog` must treat owner values as fixed unless the owner says otherwise.

**`compute-valuation <TICKER> [--set path=value ...]`**:

1. Preconditions: `valuation/assumptions.yaml` exists and validates.
2. If `valuation.md` exists, copy it and `assumptions.yaml` to `history/<YYYY-MM-DD-HHMM>/`.
3. Run `uv run value <TICKER>`; it fetches market data, computes every case, writes `valuation.md`, prints the results table and warnings.
4. Commit `value(<TICKER>): compute <QLABEL> rev N`.
5. Report to the owner in a few lines: per-share value per case against price, weighted value, terminal-value share, the reverse-DCF growth, and every warning. No interpretation beyond that; the owner reads `valuation.md`.

The refresh skill never re-values. When `refresh-company` runs on a company that has a `valuation/` folder, its report tells the owner the valuation is now as of an older quarter.

### 18.8 Market data and Damodaran datasets

- Risk-free rate: FRED series DGS10, `https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10`, latest non-empty row.
- Price: Yahoo chart endpoint `https://query1.finance.yahoo.com/v8/finance/chart/<TICKER>?range=1d&interval=1d` with a browser User-Agent; `regularMarketPrice` and its timestamp.
- Damodaran datasets, cached as CSV under `tools/valuation/data/damodaran/` with a `MANIFEST.md` (URL, fetch date, his "last updated" date), refreshed only by `uv run value --refresh-data`: `pc/implprem/ERPbymonth.xlsx` (implied ERP), `pc/datasets/betas.xls` (industry unlevered betas), `wacc.xls`, `capex.xls` (sales-to-capital), `margin.xls`, `taxrate.xls`, `histgr.xls` (historical revenue growth by industry), all under `https://pages.stern.nyu.edu/~adamodar/`.
- Any fetch failure falls back to the YAML's manual value if given, else stops with a clear message. Fetched values and dates are printed in the header of `valuation.md`; the engine never writes into `assumptions.yaml`.

### 18.9 Engine

- uv project at the repo root; package `tools/valuation/` (module name `valuation`); Python ≥ 3.12; dependencies limited to PyYAML, openpyxl, xlrd; pytest for tests. `.venv/` is gitignored.
- Console script `value`: `uv run value <TICKER> [--validate] [--dry-run] [--set a.b.c=1.2 ...] [--json] [--refresh-data]`. `--set` takes dotted paths into the YAML (`scenarios.base.sales_to_capital.value=2.0`, `scenarios.base.operating_margin.values.4=0.34`) and applies them in memory only.
- Python API: `valuation.load(ticker)`, `valuation.compute(assumptions, market=None)`, `valuation.render(result)`.
- Tests: the engine in 10-year mode must reproduce Damodaran's `AlphabetApr2018.xlsx` and `NVIDIA2023.xlsx` values of operating assets and per-share values to within 0.1% from their input sheets; a hand-worked 5-year case; the five-plus-fade rule of §18.2 reproducing the ginzu's years 6–10 from five explicit inputs; the reference structure in both directions; the transition check; every validation rule; the reverse DCF round-trips.
- `uv run value <TICKER> --render-assumptions` writes `assumptions.md` only (no market fetch, no compute): the stories, then every input as tables with value, reason, and source, in the §18.4 order. The same renderer runs on every app save and every compute.
- Writing YAML (app save, `--redraft` archiving) goes through one writer built on `ruamel.yaml` round-trip mode so comments and key order survive. The engine's read path may stay on PyYAML.

### 18.10 Interactive app: a guided walk through the assumptions

`uv run --extra app valuation-app` starts a local Streamlit page (optional dependency group `app`; the engine stays on PyYAML/openpyxl/xlrd/ruamel). It is a view and an editor of `assumptions.yaml`; it holds no valuation logic and calls `valuation.compute`, `valuation.render`, and the YAML writer.

**Shape.** The app is a sequence of pages, one factor per page, with Back and Next buttons and a progress indicator ("Step 3 of 9: Operating margin"). The owner is walked through the factors in the order of how much they move the value, reads a plain explanation of each, sees the analyst's proposal and reasons for every case, and types their own number or accepts the proposal. Results appear only on the last page. Owner feedback that produced this shape (2026-09-07): the first version crammed every input into tabs and the owner could not follow it.

**Pages, in order:**

1. **Start.** Company picker; the as-of quarter; price, risk-free rate, and equity risk premium with their dates and an override box each; a one-paragraph description of what the walk will do; the factor ranking for this company (computed at load: for each factor, the change in base-case value per share from a plausible nudge, shown as a small table so the owner sees why the pages come in this order).
2. **The stories.** The bear, base, and bull stories side by side, each headed by its two defining lines: the revenue-growth path and the margin path for years 1–5, each followed by a short clause for the fade years the rule produces ("then easing to 4.8% by year 10"). The management summary below. Stories are editable text; this page asks the owner to read and agree with the shape of each case before touching numbers.
3. **Revenue growth.** 4. **Operating margin.** On both, the inputs are the five explicit years; beneath them a read-only line shows the years 6–10 the §18.2 rule produces from the year-5 number (and, for growth, the terminal growth), updated live. Then the remaining factors in the computed impact order: **Reinvestment** (sales-to-capital and per-year overrides), **Cost of capital** (the build inputs and the resulting rate), **Terminal value** (terminal growth, terminal return-on-capital premium, terminal cost of capital), **Taxes and weights**. Revenue and margin are always pages 3 and 4 regardless of the ranking.
5. **Facts check.** Base year and bridge as read-only tables with sources; an "Edit facts" toggle for corrections. No judgment is asked here.
6. **Results.** The §18.5 results table (the reference column labelled "5-year stop", or "10-year fade" when the file's horizon is 5), the bar chart against price, then expanders for sensitivity grids, year by year (fade years marked), reverse DCF, diagnostics including the transition check, warnings. Buttons: Save to assumptions.yaml (with a note), Write valuation.md, Commit, Start over.

**Every factor page has the same layout, top to bottom:** (a) a short explanation for the 16-year-old: what the factor is, why it matters to the value, how Damodaran treats it, two to four sentences; (b) the company's own history for the factor where the YAML carries it (the analyst's reasons hold the history tables; the `diagnostics.historical_*` cells feed a one-line comparison); (c) one block per case (bear, base, bull, management when computable) with the analyst's proposed values, the reason in full, the source tags, and the input widgets prefilled with the proposal; (d) a live readout line at the bottom: value per share for bear, base, bull, and weighted with the current inputs against the price, so the owner sees what their change did before moving on; (e) Back and Next.

**Rules.**
- One factor per page. No tabs. Per-year inputs are five wide number boxes in a row labelled Year 1–5, not a grid editor, with the read-only fade line for years 6–10 beneath; ten boxes only when the file carries ten-entry lists.
- Plain text only in prose: no LaTeX, no Unicode math symbols (×, Σ, ≤), no `$` sign in markdown (Streamlit reads `$` as a formula; write "USD" or escape it). Percentages one decimal; money in USD millions with separators; per share to the cent.
- Reasons are always visible next to their numbers, never hidden behind a hover.
- A change that stops a scenario shows the engine's message in place of that case's number; never a stack trace.
- Save writes only changed values, preserves reasons, sources, and comments, appends a `changelog` entry per changed cell with the owner's note, regenerates `assumptions.md`, and refuses if the file changed on disk since load. Write valuation.md runs the same code path as `compute-valuation`; Commit runs its git step; never push.
- Before any version of the app is shown to the owner, a separate audit agent opens every page in a headless browser, takes screenshots, and checks: nothing cramped, nothing truncated, no rendering artefacts, one clear action per page, consistent number formats, readable at a laptop width. Findings go back to the builder; the audit report is kept under `tools/valuation/ui-audit/`.
