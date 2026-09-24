# Source collection and cutoff rules

Read whenever gathering research or valuation evidence. Read source guides only for companies whose evidence you are gathering, including peers when relevant; there is no need to read the full company library. Section numbers are retained for existing citations.

<a id="section-12"></a>

## 12. Sources: what to fetch, in what order, and how

<a id="section-12-1"></a>

### 12.1 Primary sources (always)

| Source | Where | Notes |
|---|---|---|
| 10-K, 10-Q, 8-K, proxy (DEF 14A) | SEC EDGAR | `https://data.sec.gov/submissions/CIK<10 digits>.json` lists filings. Documents under `https://www.sec.gov/Archives/edgar/data/<CIK>/<accession-no-dashes>/<filename>`. **SEC requires a User-Agent header** shaped like `AppName email@domain.tld`; SEC rejects anything else as an "Undeclared Automated Tool". Use `-A "company-research-skill owner@example.com"` (owner: replace with your real email). Keep requests under 10/sec. |
| Earnings call transcript | see tiers below | |
| Earnings press release | company IR page or 8-K exhibit 99.1 | The 8-K exhibit is the most reliable path. |
| Earnings slides / investor deck | company IR page | |

<a id="section-12-2"></a>

### 12.2 Transcript source tiers (ordered fallback)

1. **Company-published** transcript (IR site). Alphabet publishes a PDF per quarter, linked from its event feed; see [its source guide](../companies/GOOGL/source-guide.md).
2. **8-K exhibit** containing prepared remarks or transcript. (Neither pilot company does this, but some companies do.)
3. **Third-party free** transcript: The Motley Fool (`fool.com/earnings/call-transcripts/...`). URL slugs are inconsistent; discover the link from `https://www.fool.com/quote/<exchange>/<ticker>/` rather than guessing. Check robots.txt permits the path (the `Disallow: /` lines apply to named bots, not `*`). The quote page hides transcript links inside embedded JSON, so grep loosely for `call-transcripts` rather than for `href=`. The monthly sitemap `https://www.fool.com/sitemap/<YYYY>/<MM>` settles whether a transcript exists at all; coverage is patchy (none for AAOI Q2 2026 or MU Q3 FY2026). Fool posts up to a week after the call: a transcript of a pre-cutoff call is admissible even if posted after the cutoff, provided only call content is used and MANIFEST records both the call date and the posting date. Machine transcripts garble numbers and their "(sic)" corrections can themselves be wrong; take numbers from the release.
4. **Owner-supplied** local file, if given as an argument.
5. **None**: proceed with press release, slides, and 10-Q. Mark the outlook header `Transcript source tier: none`, and in §5 list which claims could not be sharpened for lack of a transcript. If the prior quarter's call is pre-cutoff and available, fetch it as a labelled supplement (`transcript-<prev QLABEL>.txt`, tagged `[<prev QLABEL> call]`) for business.md wording and for the "what management had said to expect" column; never use it for current-quarter guidance. When a company publishes prepared remarks but no Q&A (Micron), the header reads `company-published (prepared remarks); Q&A: none`.

Always record the tier used in `outlook.md`'s header and in `sources/<QLABEL>/MANIFEST.md`.

<a id="section-12-3"></a>

### 12.3 Shared fetch patterns and company guides

**General pattern.** Most IR sites that block plain HTML fetches (Cloudflare or Akamai 403s) are hosted by Q4 Inc. and expose open JSON feeds:
`https://<ir-host>/feed/FinancialReport.svc/GetFinancialReportList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=<YYYY>&excludeSelection=1&reportSubType=` and
`https://<ir-host>/feed/Event.svc/GetEventList?LanguageId=1&pageSize=-1&pageNumber=0&includeTags=true&year=<YYYY>&excludeSelection=1&eventDateFilter=All`.
Documents live on `s<NNN>.q4cdn.com`. Try the feeds before falling back to 8-K exhibits (works for GOOGL, META, PINS, MU; Broadcom blocks even the feeds). For any filer, list a filing's exhibits via `https://www.sec.gov/Archives/edgar/data/<CIK>/<accession-no-dashes>/<accession-with-dashes>-index.htm`; the bare directory URL returns a landing page with no useful links. Material 8-Ks are sometimes filed by a filing agent under a different accession prefix than the company's own (Broadcom: DFIN's `0001193125`), so scan every 8-K in the submissions JSON up to the cutoff, not just the company-prefixed ones.

Before fetching for a company, read `companies/<TICKER>/source-guide.md` if present. It holds that company's fiscal calendar, verified paths and disclosure quirks. These are dated fetch hints, not substitutes for current source evidence. Update that guide when a durable company-specific discovery changes future work; record quarter-specific URLs and fetch results in the quarter manifest. If no guide exists, use the shared source order here.

<a id="section-12-4"></a>

### 12.4 Caching

Everything the agents read is saved as extracted text under `companies/<TICKER>/sources/<QLABEL>/`. PDFs are converted with `pdftotext -layout`; HTML is stripped to text. `MANIFEST.md` lists every file with its origin URL, fetch date, and (for transcripts) the source tier. Re-runs read from cache before fetching.

<a id="section-12-5"></a>

### 12.5 As-of discipline

A report "as of Q1" must not use information that became available after its cutoff. The default cutoff is the later of the quarter's earnings call (or earnings announcement if no call was held) and the corresponding financial filing. Use the company's own fiscal labels and applicable filings: 10-Q/10-K for domestic issuers, or the financial-statements 6-K/20-F for foreign issuers. Respect an explicitly supplied cutoff; do not silently advance it to include a later filing or amendment.

Gatherers use documents published on or before the cutoff, with the transcript-posting exception in [§12.2](#section-12-2): a later-posted transcript may supply only content spoken during a pre-cutoff call. Record both dates and exclude subsequent editorial material. Writers must not use knowledge of later events. Missing transcripts or calls use the documented fallback; they are not reasons to wait indefinitely or choose an older otherwise eligible quarter.
