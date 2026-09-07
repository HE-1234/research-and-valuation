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
- 2026-09-07 — (pipeline) Host quirks: a stray `/tmp/inspect.py` shadows a stdlib module and breaks BeautifulSoup for any Python run with cwd `/tmp` (use `python3 -P` or another cwd); `/tmp` is shared across pipelines, so use pipeline-specific file names; host `grep` is ugrep and rejects long regex alternations (use `grep -F`); filings use curly apostrophes that defeat ASCII greps; two-column PDFs need a reading-order `pdftotext` copy; image-only pages need OCR or the release. A large gatherer died on an API error after caching but before writing notes (MU); relaunching against the cache recovered it, hence the fetch-then-notes order in §13.
