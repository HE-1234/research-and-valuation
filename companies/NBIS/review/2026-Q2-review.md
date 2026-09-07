# NBIS — Review of Q2 2026 first-run drafts
_Reviewer pass 1. Written 2026-09-07._

_Reviewed against `sources/2026-Q2/` only (as-of cutoff 2026-08-12; nothing dated later was opened). Files reviewed: `business.md` (2,832 prose words before fixes, 2,976 after), `outlook.md` (1,163 before, 1,187 after; counting method §3 rule 7). Nebius is a Dutch foreign private issuer: 20-F = annual report, 6-K exhibits = quarterly statements, release and CEO letter; both drafts say so in their Sources sections. Transcript is tier 3 (Motley Fool machine transcript); every number checked below was traced to the release, 6-K or 20-F, and the transcript was used for wording only._

**Verdict: REVISE (small list).** Citation spot-check: 92 items, 84 PASS, 6 FAIL, 2 label-only. Every number in the §2, §3, §4 and outlook §1 tables is right except two cells marked "n/d" that the FY2024 20-F does disclose. Every guidance quote and every claim quote is verbatim. The failures are: those two "n/d" cells, one inference presented as fact ($100 exercise price on 6,000,000 options), one over-broad sentence (Microsoft and Meta "appear by name only in the 20-F and the Q1 6-K"; the Q2 letter names both), one wrong explanation of a known conflict ("$2.3 billion ... rounds the release's $2,246.1M"; it does not), and one misleading cell ("No capex figure in the Q1 release or letter"). Nothing structural.

---

## 1. Rubric (§14)

| # | Question | Answer | Reasoning |
|---|---|---|---|
| 1 | Can I explain what the company does and who pays, in two sentences? | **Yes** | §1–§2: it buys NVIDIA GPUs, houses them in data centers it owns or leases, and rents the capacity by the hour or by multi-year reserved contract; AI companies pay because capacity is scarce, and two hyperscalers (Microsoft, Meta) pay take-or-pay for whole clusters. |
| 2 | Do I know what would kill it and the early warning sign? | **Yes** | §6 ranks seven scenarios; each has a concrete early warning (cash vs capex, prepayment coverage below "50-60%", revenue per MW drifting toward the $12M base, Note 4 percentages, connected power vs the 800 MW–1 GW target, Vera Rubin timing, Item 15). Financing risk is correctly ranked first, in the company's own words. |
| 3 | Do I know why the margins are what they are and whether cost scales with usage? | **Yes** | §3: cost is fixed once a cluster is on (five-year GPU depreciation, twelve-year leases, salaried engineers), so margin is utilization × price per MW; the draft shows two labelled computed margins because the company reports none, explains why adjusted EBITDA flatters, and flags both accounting choices (useful-life change, definition change). |
| 4 | Could I predict next quarter's scorecard from outlook §5 alone? | **Yes, with one caveat** | 12 claims, each a single check with a named source (Note 4, Note 15, the letter, the call). Claim 7 uses the net increase in deferred revenue as a proxy for "prepayments received"; it is mechanical but the proxy should be named (REVISE 8). |
| 5 | Did nothing require knowledge I don't have? | **Mostly, after fixes** | Before fixes ~25 terms were bare (treasury, investment-grade, tranche, co-location, amortization, H1, n/m, operating leverage, payback, operating cash flow, carrying value, warrants, options, vest, coupon, impairment, receivables, service credits, material weakness, buybacks, private placement, economic interest, GAAP, contracted/connected power, multi-tenant, asset-backed). All are now glossed inline or in the glossary (see §3 and the edits list). "Exercise price" remains bare in the sentence the writer must rewrite (REVISE 2). |

---

## 2. Citation spot-check

Legend: PASS / FAIL. Line numbers refer to the cached `.txt` files in `sources/2026-Q2/`. Quotes were checked with whitespace collapsed (the letter's two-column layout and the Q1 letter's soft hyphens split words across lines), in `transcript.txt`, `shareholder-letter-reading-order.txt`, `shareholder-letter-2026-Q1.txt` and `press-release*.txt`. "Recomputed" means the arithmetic was redone from the source inputs.

### 2a. business.md §2 segment table (every cell)

| # | Cells | Tag | Found at | Result |
|---|---|---|---|---|
| A1 | FY2023–FY2025: Nebius 9.6 / 68.3 / 480.3; Avride — / 0.3 / 1.3; TripleTen 8.2 / 28.8 / 54.1; Eliminations (8.0) / (5.9) / (5.9); Total 9.8 / 91.5 / 529.8 | [20-F FY2025, Item 5; F-pages, Note 15] | 20-F-FY2025.txt Note 15 table (lines 6720–6730); statements of operations line 3730 | PASS |
| A2 | FY2022: 0.5 / 0.3 / 2.2 / Toloka 10.5 / — / 13.5; footnote "on that basis FY2023 was $20.9M" | [20-F FY2024, Item 5] | 20-F-FY2024.txt lines 1554–1566 (Item 5) and 5753–5765 (Note 15) | PASS |
| A3 | Q1 2026: 389.7 / 0.9 / 11.6 / (3.2) / 399.0 | [6-K Q1 2026 FS, Note 15] | 6-K-2026-Q1-financials.txt Note 15 table (from line 1734) | PASS |
| A4 | Q2 2026: 574.9 / 1.0 / 10.0 / (3.6) / 582.3 | [6-K Q2 2026 FS, Note 15] | 6-K-2026-Q2-financials.txt lines 2090–2100 | PASS |
| A5 | "FY2021 is not disclosed on a comparable basis; the only FY2021 figures are Yandex consolidated ruble totals" | [20-F FY2023, Item 5] | 20-F-FY2023.txt Item 5 (lines 1231–1967) shows 2021 only in Yandex consolidated percent-of-revenue tables; no continuing-operations FY2021 figure exists in any cached filing | PASS |

Basis check (company quirk 3): columns state their basis; FY2022 is footnoted as the Toloka-inclusive FY2024 20-F basis; no Yandex-era consolidated figure is presented as this company's history. PASS.

### 2b. business.md §3 economics table (every cell, all recomputed)

| # | Row | Inputs and source lines | Result |
|---|---|---|---|
| B1 | Revenue 13.5 / 9.8 / 91.5 / 529.8 / 981.3 / 582.3 | 20-F-FY2024.txt 3409; 20-F-FY2025.txt 3730; 6-K-2026-Q2-financials.txt 158; release line 11 | PASS |
| B2 | Cost of revenues (excl. D&A) 210% / 200% / 48% / 31% / 24% / 23% | 28.4 (FY2024 20-F); 19.6 / 43.7 / 166.2 (FY2025 20-F); 237.4 / 133.6 (Q2 FS line 162; release 24–25 prints 24% and 23%) → 210.4 / 200.0 / 47.8 / 31.4 / 24.2 / 22.9 | PASS |
| B3 | "Gross margin" before D&A (computed) (110)% / (100)% / 52% / 69% / 76% / 77% | (rev − cost) / rev → −110.4 / −100.0 / 52.2 / 68.6 / 75.8 / 77.1 | PASS; labelled computed and defined (quirk 1) |
| B4 | "Gross margin" after all D&A (computed) (314)% / (399)% / (32)% / (10)% / 28% / 32% | D&A 27.5 / 29.3 / 77.1 / 417.9 / 471.7 / 259.7 → −314.1 / −398.9 / −32.0 / −10.2 / 27.7 / 32.5 (32.46 rounds to 32) | PASS; footnote says the whole D&A line is deducted |
| B5 | Operating margin (GAAP, computed) (1,170)% / (2,915)% / (437)% / (115)% / (31)% / (30)% | Loss from operations (158.0) / (285.7) / (399.6) / (611.7) / (303.9) / (175.9) → −1,170.4 / −2,915.3 / −436.7 / −115.5 / −31.0 / −30.2 | PASS |
| B6 | Adjusted EBITDA margin (computed) n/m / n/m / (247)% / (12)% / 37% / 41% | Total segment adjusted EBITDA (226.3) / (64.9) [20-F FY2025 Note 15 line ~6740; Item 5 line 1932 confirms "for the group"]; 365.7 / 236.2 [Q2 FS 2102; release 12] → −247.3 / −12.2 / 37.3 / 40.6. FY2022 (−124.5, four segments summed in the FY2024 20-F) and FY2023 (−240.7) marked n/m: a labelling choice, acceptable | PASS (see REVISE 7 on the definition mix) |
| B7 | Capex 14.6 / 82.9 / 807.5 / 4,066.0 / 8,130.3 / 5,657.4; Capex ÷ revenue 1.1x / 8.5x / 8.8x / 7.7x / 8.3x / 9.7x | 20-F-FY2024.txt cash flow line ~3599; 20-F-FY2025.txt ~3920; release lines 42, 211 → 1.08 / 8.46 / 8.83 / 7.67 / 8.29 / 9.72 | PASS |

### 2c. business.md §4 cash table (every cell)

| # | Row | Found at | Result |
|---|---|---|---|
| C1 | Net income (loss), continuing (180.0) / (299.0) / (352.0) / 9.8 / 430.8 | 20-F-FY2024.txt 3429; 20-F-FY2025.txt 3752; Q2 FS 180 | PASS |
| C2 | ClickHouse paper gains 598.9 / 780.6 | 20-F-FY2025.txt 3744; Q2 FS 172; MD&A line 332 ties the 780.6 to ClickHouse | PASS |
| C3 | Operating cash flow, continuing (139.7) / (222.0) / (269.9) / 401.9 / 4,504.1 | 20-F-FY2024.txt 3591; 20-F-FY2025.txt 3908; Q2 FS 502 | PASS |
| C4 | of which increase in deferred revenue **n/d** / 1.9 / 10.0 / 1,565.8 / 4,395.0 | 1.9 / 10.0 / 1,565.8 at 20-F-FY2025.txt 3902; 4,395.0 at Q2 FS 500 (MD&A 440 confirms). **FY2022 is disclosed:** 20-F-FY2024.txt cash flow line 3583 "Deferred revenue \| 0.8 \| 2.3 \| 9.6" (columns 2022 / 2023 / 2024, header at line 3549) → FY2022 = 0.8 on the same Toloka-inclusive basis as the rest of the column | **FAIL (one cell)** |
| C5 | Capex | as B7 | PASS |
| C6 | Free cash flow (computed) (154.3) / (304.9) / (1,077.4) / (3,664.1) / (3,626.2) | recomputed, all exact | PASS |
| C7 | Share-based compensation **n/d** / 28.8 / 54.5 / 83.2 / 137.8 | 28.8 / 54.5 / 83.2 at 20-F-FY2025.txt 3880; 137.8 at Q2 FS 478 and release 34. **FY2022 is disclosed:** 20-F-FY2024.txt line 3563 "Share-based compensation expense \| 14 \| 9.6 \| 31.4 \| 56.6" → FY2022 = 9.6 | **FAIL (one cell)** |
| C8 | Cash n/d / 116.1 / 2,434.7 / 3,678.1 / 8,042.1 | 20-F-FY2024.txt balance sheet (Dec 31, 2023 column); 20-F-FY2025.txt 3633; Q2 FS 48. No cached filing has a Dec 31, 2022 balance sheet for this perimeter, so n/d is right here | PASS |
| C9 | Debt n/d / 6.8 / 6.1 / 4,127.7 / 8,545.7 | 6.8 = "Debt, current portion" Dec 2023 (no non-current line); 6.1 + 0; 24.5 + 4,103.2; 46.7 + 8,499.0 | PASS |
| C10 | Deferred revenue n/d / 6.9 / 16.3 / 1,577.5 / 5,975.2 | 6.9 (FY2024 20-F); 16.3 + 0; 275.5 + 1,302.0; 979.4 + 4,995.8; Note 4 line 1196 states 1,577.5 and 5,975.2 | PASS |
| C11 | Shares outstanding n/d / 361.5 / 235.8 / 253.0 / 271.9 (millions) | 325,783,607 + 35,698,674 = 361.48M and 200,054,926 + 35,698,674 = 235.75M (FY2024 20-F balance-sheet share line); 219,465,088 + 33,551,883 = 253.02M and 238,400,165 + 33,455,053 = 271,855,218 (Q2 FS balance sheet; release line 45) | PASS |
| C12 | Footnotes: "Debt = current plus non-current (computed)"; FY2022 basis; Dec 31, 2023 balances from the FY2024 20-F | as above | PASS |

### 2d. outlook.md §1 indicator table (every number and quote)

| # | Row | Found at | Result |
|---|---|---|---|
| D1 | 1: $574.9M; $582.3M; $389.7M; $399.0M; "$3.0B–$3.4B revenue" | Q2 FS Note 15; Q1 FS Note 15; Q1 letter p.1 chart "On track to achieve $3.0B–$3.4B revenue in 2026 and $7B–$9B ARR" | PASS |
| D2 | 2: $3.0B; $1.92B; "$7B–$9B ARR" | letter p.9 "Annualized run-rate revenue (ARR) of $3.0 billion as of the end of June"; Q1 letter "ARR ... of $1.92 billion as of the end of March"; Q1 letter chart | PASS |
| D3 | 3: $37,490.6M; $5,975.2M; $33,585.3M; $4,778.1M; "very focused on generating prepayments from our current and future customers" | Q2 FS 1204, 1196; Q1 FS 946, 938; Q1 letter | PASS |
| D4 | 4: 40.6% (236.2 ÷ 582.3 = 40.56); 49.7%; 32.5% (129.5 ÷ 399.0 = 32.46); 45%; "~40% Adj. EBITDA margin" | release 12; letter p.10 (= 285.7 ÷ 574.9); Q1 release 13; Q1 letter (twice); Q1 letter chart | PASS |
| D5 | 5: $5,657.4M; $2,246.1M; $2,472.9M; $2,258.0M; "No capex figure in the Q1 release or letter" | release 42, 207; Q1 release 45, 212. **The cell text is wrong:** both Q1 documents report Q1 capex ($2,472.9M; "approximately $2.5 billion"). What is absent is FY2026 capex *guidance*: the Q1 letter's guidance chart lists revenue, ARR and adjusted EBITDA margin only, and the Q1 release has no guidance; the Q2 call's "We continue to expect ... $20 billion to $25 billion" implies it was given somewhere not in this report's sources (the Q1 call) | numbers PASS; **wording FAIL** |
| D6 | 6: $8,042.1M; $8,545.7M (46.7 + 8,499.0); 271,855,218; $9,298.2M; $8,450.4M (18.4 + 8,432.0); 253,898,194; "mid-single digits billions of dollars in the near term"; "not utilized this program to date" | release 95, 113, 118, 45; Q1 release 99, 117, 122, 48; Q1 letter (both quotes; "rais-ing" soft hyphen handled) | PASS |
| D7 | 7: $12,054.1M; $5,324.1M (computed total); $9,905.2M; "not disclosed in the Q1 6-K"; "more than 4 GW by year-end"; "800MW to 1GW" | Q2 FS 1592; Note 11 line 1692: 81.7 + 541.8 + 542.0 + 540.5 + 535.8 + 3,082.3 = 5,324.1; Q1 FS 1274; Q1 FS Note 11 (line 1356) contains legal and tax contingencies only, no power commitments; Q1 letter (both quotes) | PASS |
| D8 | 8: C 24%, D 21%, E 14%; "Not disclosed (no table in the Q1 6-K)" | Q2 FS 1068–1072; grep "Customer" in Q1 FS Note 4 = 0 hits | PASS |
| D9 | Year-ago line: $105.1M; $93.7M; $(21.0)M; $(167.9)M; $510.6M; "The letter's '$2.3 billion' ... rounds the release's $2,246.1M" | Q2 FS 2090–2102; release cash-flow statement 207 and 42. Note the release's own highlights table (line 41) prints Q2 2025 OCF as (167.7) while its cash-flow statement says (167.9); the draft's (167.9) is the statement figure, the right choice. **"rounds" is wrong:** $2,246.1M rounds to $2.2 billion. The letter p.2 infographic ("Including $2.3 billion in positive operating cash flow") and the call ("Operating cash was $2.3 billion in the quarter") both say 2.3; the release cash-flow statement says 2,246.1. The draft uses the right figure but misdescribes the conflict | numbers PASS; **explanation FAIL** |

### 2e. business.md §8 indicator table (every number)

H1–H8: $574.9M (Note 15); $3.0B (letter p.9); $37,490.6M and $5,975.2M (Note 4); 40.6% (computed) and 49.7% (release; letter p.10); $5,657.4M and $2,246.1M (release); $8,042.1M, $8,545.7M, 271,855,218 (release); $12,054.1M and $5,324.1M (computed) (Notes 8, 11); C 24%, D 21%, E 14% (Note 4). All duplicate 2d and **PASS (8)**.

### 2f. outlook.md §4 guidance quotes (word-for-word)

| # | Quote | Tag | Found at | Result |
|---|---|---|---|---|
| E1 | "We are reaffirming our full-year 2026 guidance across all metrics" | [letter, p.3] | reading-order p.3 (followed by footnote marker "(4)") | PASS |
| E2 | "The company will share a detailed view of guidance on its earnings call and webcast" | [letter, p.11] | p.11 | PASS |
| E3 | "We continue to expect annualized run rate revenue of $7 billion to $9 billion, group revenue of between $3 billion and $3.4 billion, group adjusted EBITDA margin of approximately 40%, and capital expenditures of $20 billion to $25 billion." | [call] | transcript, CFO Dado Alonso prepared remarks | PASS |
| E4 | "We now anticipate ending 2026 with 5 GW of contracted power, up from the +4 GW we indicated last quarter." | [letter, p.5] | p.5; source has a footnote marker "(5)" after "power", omitted in the draft, which is fine | PASS |
| E5 | "we still expect to meet this guidance from 800 megawatts to 1 gigawatt of connected power this year" | [call] | transcript, Andrey Korolenko answer | PASS |
| E6 | "The pace at which we bring capacity to market will accelerate as we plan to deploy more than 1 GW per year, starting in 2027." | [letter, p.5] | p.5 | PASS |
| E7 | "expect capacity deployed late in Q2 to begin contributing to revenue in Q3" | [call] | transcript, CFO | PASS |
| E8 | "We expect to receive over $9 billion in customer prepayments in 2026." | [letter, p.10] | p.10 (p.3 has the shorter "We expect over $9 billion in customer prepayments in 2026"; the draft quotes and tags the p.10 version) | PASS |
| E9 | "We are progressing on additional asset-backed financing and continue to evaluate corporate-level debt and additional financing instruments." | [call] | transcript, CFO | PASS |
| E10 | "we will provide a formal guidance later this year" | [call] | transcript, CFO | PASS |
| E11 | "on track to come online in early 2027" (Meta); "late this year or early next year" (Vera Rubin) | [letter, p.5; call] | p.5; transcript, Korolenko | PASS |

### 2g. outlook.md §5 claim quotes (word-for-word)

All 13 quoted fragments under the 12 claims are verbatim: "group revenue of between $3 billion and $3.4 billion" (call); "expect capacity deployed late in Q2 to begin contributing to revenue in Q3" (call); "group adjusted EBITDA margin of approximately 40%" (call); "capital expenditures of $20 billion to $25 billion" (call); "today we are raising our year-end contracted power target again to 5 GW" (letter p.3); "we still expect to meet this guidance from 800 megawatts to 1 gigawatt of connected power this year" (call); "We expect to receive over $9 billion in customer prepayments in 2026." (p.10) and "$4,397.7" (Note 4 line 1198); "Our pipeline generation stepped up again in Q2 and includes multiple opportunities over $1 billion" (call, Marc Boroditsky) and "$37,490.6" (Note 4 line 1204); "We are progressing on additional asset-backed financing" (call); "To date, we've delivered all capacity tranches to Microsoft under the contract" (p.5); "with capacity on track to come online in early 2027" (p.5); "we will provide a formal guidance later this year" (call). Claim 3's "H1 was 37%" = 365.7 ÷ 981.3 = 37.3%; claim 7's "$2.3 billion" = (9,000 − 4,397.7) ÷ 2 = 2,301. **13 PASS.**

### 2h. Prose sentences (business.md §1–§7, outlook.md §2–§4)

| # | Sentence / figure | Tag | Found at | Result |
|---|---|---|---|---|
| G1 | §1 customer list quote; "full-stack AI cloud"; Token Factory "token-based model"; "two large hyperscalers, Microsoft and Meta" | [20-F FY2025, Item 4] | 20-F-FY2025.txt Item 4 (lines 1104–1476) | PASS |
| G2 | §1 "approximately 98% of total group revenue"; "our non-core businesses"; ClickHouse "spun off from the group in September 2021"; Toloka "spun off ... May 2025" | [letter p.9; p.8; Item 4] | reading-order p.9, p.8; Item 4 | PASS |
| G3 | §1 history: 1997, May 2011, February 28, 2022 halt, ~1,300 people, 1.8 billion rubles | [20-F FY2023, Item 4] | 20-F-FY2023.txt Item 4 | PASS |
| G4 | §1 "Consortium First", "JSC Solid Management", RUB 475 billion, "a 50% discount to fair value" | [20-F FY2024, Item 10] | 20-F-FY2024.txt Item 10 | PASS |
| G5 | §1 "more than 95% of the Group's consolidated revenues in 2023"; May 17 and July 12, 2024; $2.6 billion; 162.5 million shares; name change August 2024; "resumed on October 21, 2024" | [20-F FY2025, Note 1; 20-F FY2024, Item 4] | Note 1 (line ~4160); 20-F-FY2024.txt Item 4 | PASS |
| G6 | §1 "over $5 billion", "more than $6 billion"; $2.8B ATM; July 2026 loan | [Item 5; Q2 FS Note 14; Note 16] | Item 5 line ~2020; Note 14 line 2052 (gross 2,846.7 at cash flow 538); Note 16 line 2222 | PASS |
| G7 | §2 "pay-as-you-go" / "reserved capacity" recognized evenly; three deal types (quotes); "$20-25 million per megawatt"; "$40-50 million per MW range"; "$12M 2026 base" chart label; "Roughly 70% ..."; "50-60% of the associated capex" | [MD&A; Note 1; letter p.2–4] | MD&A 50; 20-F Note 1 line ~4320; reading-order p.3, p.3, p.2, p.4, p.3 | PASS |
| G8 | §2 Microsoft: September 8, 2025; Vineland, New Jersey; five-year; "nine tranches"; $17,392.9; "irrespective of actual utilization"; $6,958.1. Meta: November 1, 2025; five-year; $2,880.7 | [20-F FY2025, Note 1] | lines 4294–4296 and the following Meta paragraph | PASS |
| G9 | §2 Second Meta Agreement: March 2026; "$12 billion"; "with deployments in tranches starting early 2027"; Meta must buy unsold capacity; "up to $15 billion" | [6-K Q1 2026 FS, Note 1] | 6-K-2026-Q1-financials.txt line 526 (March 13, 2026; "total contract value of $12 billion"; "up to $15 billion") | PASS |
| G10 | §2 RPO $37,490.6M, 36% within 24 months; "Revenue by contract type, customer or product is not disclosed" | [Q2 FS Note 4; 20-F Note 15] | Note 4 line 1204; Note 15 gives segment and geography only; no disaggregation by contract type anywhere in the 20-F (grep "disaggregat" hits only ASU boilerplate) | PASS |
| G11 | §2 Avride $1.0M, outside investors (SAFE, SMB Holding); TripleTen boot camps, revenue −19% | [Note 15; Note 6; MD&A Revenues] | Q2 FS 2092, 1394; MD&A 52, 190 | PASS |
| G12 | §3 five-year GPU life; leases "up to twelve years"; CFO quote "capacity added in Q1, higher utilization and high-margin revenue" | [Note 1; Note 8; call] | Q2 FS 662, 1592; transcript, Dado Alonso | PASS |
| G13 | §3 cost-of-revenues definition quote; D&A $259.7M = 45% of revenue; "from four to five years", $43.0M; "our estimates of the useful lives of such assets may be subject to change" | [MD&A 62; release 30–31; Note 1 662; 20-F Item 3 line 972] | as listed | PASS |
| G14 | §3 adjusted EBITDA definitions: "certain SBC", "one-off restructuring and other expenses" vs "acquisition and other corporate transaction-related costs" | [20-F Item 5; MD&A] | 20-F-FY2025.txt 1906; MD&A 376 | PASS (quirk 2 satisfied) |
| G15 | §3 "29% ... 23% ... 'primarily reflecting operating leverage as we scaled capacity'"; 49.7%; operating loss $175.9M; 7.7x / 8.3x; "1 year and 10 months", "from our historical two-to-three-year range" | [letter p.10; release; p.4] | reading-order p.10 (line 1045), p.10 (1147), p.4 (379); release 148 | PASS |
| G16 | §4 "advance payments received from customers"; $4.4B; "one to five calendar years"; interest charge on prepayments (significant financing component) | [MD&A Cash Flows; Note 4; 20-F Note 1] | MD&A 440; Q2 FS 1198; 20-F-FY2025.txt 4324 (inside Note 1, which spans 4150–4632) | PASS |
| G17 | §4 Q1 2026 net income $621.2M; $780.6M; "at a reported valuation of approximately $15 billion"; adjusted net loss $33.2M | [Q1 release; MD&A; release] | Q1 release 162; MD&A 332; release 14 | PASS |
| G18 | §4 convertibles $8.5B original → $10.0B at maturity; 235.8M → 271.9M shares in eighteen months; 21.1M warrant shares; "approximately 66 million"; 13.0M options + unvested RSUs; $7.8B of $14.1B "not yet in use" | [Note 12; Note 13; Note 14; Item 3; Note 7] | Note 12 lines 1758 (4.16B), 1710 (4.34B), 1798 (10,041.8); Note 14 2040; Item 3 line 998; Note 13 lines 1904 (6,740,600 options) + 1932 (6,234,091 RSUs) = 12,974,691; Note 7 lines 1486–1488 (7,836.4 of 14,149.5) | PASS on numbers; **13.0M not labelled computed** |
| G19 | §5 "non-cancelable"; Boroditsky quote on auctions; "more than 30%"; "excess industry capacity"; "pricing pressure in respect of capacity for older generations of GPUs"; "one of the first-to-deploy the latest generation of NVIDIA GPU chips"; "already had an existing supplier, in some cases, hyperscaler"; CoreWeave, Crusoe, Lambda; "relatively short-term"; "limited experience in delivering large customer contracts" | [Note 4; call; p.4; Item 3; Item 4; call; Item 3] | Note 4 1202; transcript (source starts "In a market..."); p.4; Item 3 (line 478 for the competitor list, which is in Item 3 as tagged); Item 4; transcript (Volozh); Item 3 | PASS |
| G20 | §6#1 "our core business is capital-intensive and currently not profitable ..."; $8.0B cash; $8.5B debt; "over $9 billion" | [Item 3; release; p.10] | as listed | PASS |
| G21 | §6#2 "AI models that require less computation power than earlier models" | [Item 3] | Item 3 | PASS |
| G22 | §6#3 59% (24 + 21 + 14); $17.4B ≈ 46% of RPO (17,392.9 ÷ 37,490.6 = 46.4%, labelled computed); "terminate individual tranches ..."; concentration table (FY2024 A 27%, C 11%, receivables A 59%; FY2025 A 25%, B 15%, receivables D 83%; Q2 2025 A 39%, B 15%; Q2 2026 C 24%, D 21%, E 14%, receivables E 29%, D 16%; H1 2026 C 26%, D 21%); "D" in the 20-F vs "C" in the Q2 6-K for the 83% customer | [Note 4; 20-F Note 1] | 20-F-FY2025.txt Note 1 concentration table and receivables sentence; Q2 FS 1064–1076 | PASS |
| G23 | §6#3 "Microsoft and Meta appear by name only in the 20-F and the Q1 6-K" | [20-F Note 1; Q2 FS Note 4; Q1 FS Note 1] | True of the financial statements and the call (grep "Microsoft" in transcript.txt = 0; "Meta" = 0, only "bare-metal"). **Not true as written:** the Q2 shareholder letter p.5 names both ("delivered all capacity tranches to Microsoft"; "our second Meta agreement") and the letter is itself a 6-K exhibit | **FAIL (over-broad)** |
| G24 | §6#4 $12.1B leases; $5.3B power commitments (computed); "without a vote"; "obtaining reliable power with sufficient capacity and on acceptable terms, will limit the growth of our revenues" | [Note 8; Note 11; call; Item 3] | Q2 FS 1592, 1692; transcript (question relayed from Morgan Stanley); Item 3 | PASS |
| G25 | §6#5 "We currently rely on Nvidia for the GPU chips we use"; three suppliers; $2B NVIDIA; Vera Rubin timing | [Item 3; Note 4; Note 14; call] | Item 3; Q2 FS 1080; 2040; transcript (Korolenko) | PASS |
| G26 | §6#6 two material weaknesses, "depreciation start dates" | [Item 15] | 20-F-FY2025.txt 3138, 3170 (Item 15 spans 3084–3216) | PASS |
| G27 | §6#7 "could create challenges for our businesses, including more protracted client on-boarding"; "may challenge our assessment"; 185 of 1,543 in Israel | [20-F FY2025, Item 3; Item 6; 20-F FY2024, Item 3] | Item 3 line 1056; the tax quote is **not** in the FY2025 20-F (its Item 5 line 2084 says "Different interpretations ... could have resulted in a materially different outcome") but is verbatim in 20-F-FY2024.txt line 978 (Item 3), which the tag list includes; Item 6 employee table line 2310 | PASS |
| G28 | §7 Volozh 62, "the principal founder", 2000–2022, CEO August 2024; Chernin (Token Factory); Korolenko (Head of Infrastructure at Yandex); CFO since June 2025; Boroditsky since May 2025, Cloudflare; Boynton director since 2000, "a founding shareholder of Yandex" | [Item 6] | lines 2122, 2142, 2190, 2192, 2186, 2188, 2146 (source capitalises "A founding shareholder") | PASS |
| G29 | §7 "no purchases of equity securities"; "no present plan to pay cash dividends"; $251.6M; ~3.8M shares for Tavily, ClarifAI, Eigen AI; ">$15 billion (computed)" | [Item 16E; Item 8; cash flow; Note 3; several] | 3266 (Item 16E); 2504 (Item 8); Q2 FS 518; Note 3 Eigen AI: "approximately 1.4 million Class A ordinary shares" as consideration + "approximately 2.4 million" to employees = 3.8M (Tavily and ClarifAI paid in cash, options and RSUs, not shares); 700 + 1,000 + 3,162.5 + 1,150 + 2,000 + 4,340 + 2,846.7 = 15,199 | PASS on numbers; **3.8M not labelled computed** |
| G30 | §7 capital table, every row: 33,333,334 @ $21.00, $700.0M; $1,000M 2.00% / 3.00%, ~$51.45; $3,162.5M 1.00% / 2.75%, ~$138.75; 12,432,432 @ $92.50, $1.15B; 21,065,936, $2,000.0M; $4.34B 1.25% / 2.625%, ~$183 / ~$180; 12,729,493 @ $223.60, $2,846.7M, 12,270,507 remaining; ~$775M SOFR + 2.50%, October 31, 2030, GPU and investment-grade-contract collateral; $10,041.8M; "approximately 66 million" | as tagged | 20-F-FY2024 Note 13; 20-F-FY2025 Note 12 (19.4363 → $51.45; 7.2072 → $138.75), Note 13; Q2 FS 2040, 1718–1722 ($183.22 / $180.31), 2052–2054, 2222, 1798; Item 3 | PASS |
| G31 | §7 pay: $5.9M cash for eight persons; 6,350,000 options; 226,312 RSUs; "6,000,000 of those options carry a $100.00 exercise price"; COO, Chernin, Korolenko each 625,000 vested "premium priced" options | [Item 6; Note 14; Item 7] | Item 6 line ~2340 ($5.9 million, eight persons, 6,350,000, 226,312); Item 7 footnotes (3) Ophir Nave, (11) Chernin, (12) Korolenko: 625,000 "premium priced" options "at an exercise price of $100 per share". **The $100 for all 6,000,000 is not stated anywhere:** Note 14 (lines 6376, 6506) says only that 6,000,000 options were granted to "certain executives with exercise prices that were considered to be deeply out of the money" and "with market conditions". The weighted-average grant price of $96.69 across 6,350,000 options implies ~$100 for the 6,000,000, but that is a computation, not a disclosure | **FAIL (inference stated as fact)** |
| G32 | §7 control: Class B ten votes, Class A one; 28,655,509 Class B held for Volozh's family; 51.62% / 11.33%; "Controlled Company"; nominating committee "does not consist entirely of independent directors"; directors and officers 52.34% / 12.91% | [Q2 FS Note 14; Item 7; Item 3; Item 6] | Q2 FS 2000–2002; Item 7 line 2430 footnote (2) "held by Highvern Cayman Limited, as Trustee of the LASTAR Trust, the beneficiaries of which include Mr. Volozh or members of his family"; line 2380; Item 3; Item 6 line 2214; line 2414 (extracted as "52. 34%") | PASS |
| G33 | outlook §2: CEO business-model quote; "cannot build all of it" / "somebody needs to build the rest of the market, and that will be us"; "We could sell our entire 2027 capacity ..."; asset-light / "even higher margins"; "our trajectory toward 20-30% EBIT margins" | [call; p.3; call; Q1 letter] | transcript (Volozh; Volozh; Alonso); reading-order p.3; Q1 letter | PASS (speakers as attributed) |
| G34 | outlook §3: all quotes (landmark deals, Reflection/Cohere, "in late 2026 ...", "priced at a significant premium", "$40-50 million per MW range", "15% above the highest price we ever charged before", "in Q4", "finance, build and operate the facilities", "the full-stack platform and the demand", "still in very early stage", "dozens of inquiries", Token Factory tripled, Tavily 2.5 million, "Owned capacity now accounts for more than 75%", CFO "second half of next year", "Both are still early stage companies"); $49.5M = 40.1 + 9.4 | [letter p.3–6; call; Q1 letter; Note 15] | all found; "the first was signed in early Q3" paraphrases p.3 "One such deal has been signed in Q3" / "we signed our first one this week"; source has lowercase "both are still early stage companies" (Alonso) | PASS |
| G35 | outlook §4 "The Q2 release contains no guidance ... no Q3 2026 guidance was given anywhere" | [release; letter; call] | release has no outlook section; letter p.11 defers to the call; transcript gives no Q3 number, only "begin contributing to revenue in Q3" | PASS |
| G36 | Known conflicts (quirks 4): draft uses 2,246.1 (release) not "$2.3 billion"; uses 285.7 / 49.7% (letter p.10; Note 15) not the transcript's "(sic) [ $236 million ]" | — | release 207; letter p.10; Q2 FS 2102; transcript "Our Nebius AI business generated adjusted EBITDA of $286 million (sic) [ $236 million ] at a margin of 50%" | PASS (right figures chosen; see D9 for the explanation wording) |

**Totals: 92 items checked (A 5, B 7, C 12, D 9, E 11, F 13 as one block, G 36 minus overlaps, H 8): 84 PASS, 6 FAIL (C4, C7, D5, D9, G23, G31), 2 label-only (G18 "13.0 million", G29 "3.8 million").**

---

## 3. Jargon audit

Read as a smart 16-year-old with no finance or cloud background. "Fixed" = glossed directly by the reviewer (see the edits list at the end).

| Term | Where | Status |
|---|---|---|
| treasury (shares) | business §1 | fixed |
| revenue "recognized" | §2 | fixed |
| investment-grade | §2 (also §7 table, where "one investment-grade customer's contracted cash flows" is now readable after the §2 gloss) | fixed |
| tranche | §2 first use (also §6, outlook §4/§5) | fixed at first use |
| co-location | §3 (inside a quote) | fixed after the quote |
| amortization (in D&A) | §3 | fixed |
| H1, n/m | §3 table and footnote; outlook §1 | fixed in both files |
| operating leverage | §3 (inside a quote) | fixed after the quote |
| payback | §3 | fixed |
| operating cash flow | §4 first use | fixed |
| carrying value | §4 table row label | fixed in the footnote |
| warrant shares; options; vest | §4 | fixed |
| high-coupon | §6#1 | fixed |
| impairment charge | §6#2 | fixed |
| receivables | §6#3 table header | fixed |
| service credits | §6#3 | fixed |
| material weaknesses in internal control | §6#6 | fixed |
| buybacks | §7 | fixed |
| private placement | §7 table | fixed |
| economic interest | §7 | fixed |
| exercise price | §7 pay sentence | **not fixed**: the sentence must be rewritten by the writer (REVISE 2); gloss it there ("the price at which the option lets you buy a share") |
| GAAP | §3 table row "Operating margin (GAAP, computed)"; glossary had no entry | fixed: glossary entry added |
| contracted power / connected power | §6#4, §8 indicator 7, outlook §1 row 7, §4, claims 5–6 | fixed: glossary entry added (the terms were used in both files without definition) |
| dilution | glossary "Convertible notes" | fixed (parenthetical) |
| ATM | outlook §1 row 6 | fixed ("at-the-market share sales"); glossary already covered it in business.md |
| multi-tenant | outlook §2 (inside a quote) | fixed after the quote |
| asset-backed financing | outlook §4 (quote), claim 9 | fixed after the §4 quote; claim 9 left untouched |
| Take-or-pay | glossary only; the term never appears in either file's text | **not fixed**: glossary should hold only terms the text cannot avoid; either use it in §5 ("take-or-pay, in the filings' words 'irrespective of actual utilization'") or drop the entry (REVISE 7) |
| RPO, ARR, deferred revenue, adjusted EBITDA, capex, convertible notes, GPU, hyperscaler, neolab, agentic, token, training/inference, MW/GW | throughout | in the glossary and mostly glossed inline at first use; fine |
| utilization; yield per MW; paper gains; segments; Class A / Class B; SOFR; Vera Rubin; EBIT | §3, §2, §4, §1, §7, §7, §6#5, outlook §2 | explained in place ("how full the clusters are"; "of annual revenue"; "revaluation gain"; ten votes vs one; "a floating benchmark interest rate"; "NVIDIA's next GPU generation"; "operating profit, after depreciation"); acceptable |

**Banned-word sweep** (leverage, synergy, headwind, tailwind, monetize, ecosystem, at scale, robust, unlock, TAM): none in either file outside quotations; "operating leverage" appears once inside a management quote and is now glossed.

**Paragraphs that are mostly numbers** (§3 rule 5): business.md §2 hyperscaler paragraph (line 27: seven dollar figures in five sentences) and §4 third paragraph (line 76: seven figures). Both still read as sentences; the first is the better candidate for a four-row table if the writer has words to spare (it does not, see §6).

---

## 4. Invented-number check

No invented numbers. Every figure in both files traces to a cached source or to an arithmetic step, with these exceptions:

1. **business.md §7, line 135:** "6,000,000 of those options carry a $100.00 exercise price". The filing says the 6,000,000 were "deeply out of the money" with "market conditions"; the $100 is disclosed only for three officers' 625,000 options each (1,875,000 in total). The figure is an inference (and arithmetically plausible from the $96.69 weighted-average grant price). See G31.
2. **business.md §4, line 76:** "13.0 million options and unvested RSUs" is 6,740,600 + 6,234,091 (Note 13), unlabelled.
3. **business.md §7, line 121:** "about 3.8 million shares" is 1.4M + 2.4M (Note 3), unlabelled.
4. **business.md §4 table, lines 63 and 66:** two "n/d" cells where the FY2024 20-F does disclose the figure (0.8 and 9.6). Rule 1 cuts both ways: "not disclosed" is itself a factual claim.
5. **outlook.md line 19:** "rounds the release's $2,246.1M" attaches a wrong arithmetic explanation to two correctly sourced numbers.

Inferences correctly labelled: §4 "Our view: the business is a bet ..."; §6#3 "(computed; part has already been earned, so its remaining share is somewhat lower)"; §6#3 "about 46% of RPO (computed ...)"; §7 "more than $15 billion (computed)"; every "(computed)" margin in §3 and outlook §1. Management statements are attributed to the right speakers (CEO Volozh for the business-model and "rest of the market" quotes; CFO Alonso for guidance, margins and financing; Korolenko for connected power and Vera Rubin; Boroditsky for auctions and pipeline).

---

## 5. Skeleton and rules check

**business.md**

| Requirement (§6) | Result |
|---|---|
| `# <Company> — The Business`; `_As of <QLABEL>. Written <date>._` | OK; fiscal = calendar, parenthetical "(quarter ended June 30, 2026)" given |
| §1–§8 headings present, in order, exact wording | OK; §1 has the history paragraph; §6 carries customer concentration with its own table; §8 has name / why / where |
| §2 segment table, 5 fiscal years | FY2022–FY2025 plus 2026 quarters; FY2021 explicitly unavailable on any comparable basis with reason and tag. Acceptable (company quirk 3) |
| §3 table: revenue, gross margin, operating margin, capex, capex/revenue | OK; two computed "gross margin" rows, both labelled and defined (quirk 1); adjusted EBITDA definition change stated in the prose above the table (quirk 2) |
| §4 table, 5 years | OK (two n/d cells to fix) |
| §8 marked `_Proposed — owner to review and lock._` | OK |
| §8 indicators anchored to recurring disclosures (§8 of AGENTS.md) | 1, 3, 4, 5, 6, 8: balance-sheet, cash-flow, Note 4 and Note 15 lines, recurring every quarter. 2 (ARR): a KPI the letter has reported for Q4 2025, Q1 2026 and Q2 2026; acceptable. 7: Note 8 leases-not-commenced recurs (Q1 and Q2 6-Ks); the power-commitment half (Note 11) was **absent from the Q1 2026 6-K** and present in Q2 — the owner should decide at lock whether to keep it (note for the owner, not a failure). One-off targets (5 GW, $9B prepayments, $20–25B capex) are correctly tracked as claims, not indicators |
| Glossary: only essential terms, one sentence each | OK after additions (GAAP; contracted/connected power). "Take-or-pay" is unused in the text (REVISE 7) |
| Sources: foreign-filer sentence; every tag prefix used in the body appears in the table | OK. Tag families used: 20-F FY2025 / FY2024 / FY2023 (Item, F-pages Note), 6-K Q2 2026 MD&A, 6-K Q2 2026 FS, 6-K Q1 2026 FS, Q2 2026 release, Q2 2026 letter p.N, Q1 2026 release, Q2 2026 call. All in the table. The table also lists [Q1 2026 letter], which the body never uses (harmless) |
| Company quirks 4–6 | Release figures used for the two known conflicts; no quarterly concentration series built from inconsistent customer letters (the table carries the caveats and a "no table" row for Q1 2026); every sentence naming Microsoft or Meta cites the 20-F, the Q1 6-K or the letters, never the Q2 6-K statements or the call |
| Nothing after the 2026-08-12 cutoff | OK. The July 10, 2026 facility is Note 16 of the August 12 filing; the transcript records the August 12 call (posted August 19; MANIFEST documents the reasoning) |

**outlook.md**

| Requirement (§7) | Result |
|---|---|
| `# <Company> — Outlook as of <QLABEL>`; `_Transcript source tier: ... Written <date>._` | OK: "third-party (The Motley Fool)", matches MANIFEST tier 3 |
| §1 table: one row per proposed indicator; columns this quarter / last quarter / what management said | OK, exactly those three columns, one comparison value per cell |
| §2, §3, §4 (verbatim), §5 | OK; §4 quotes are verbatim (2f); §4 states clearly that the release and letter carry no numbers and the numbers come from the call |
| §6 Tone shift | correctly omitted (first run) |
| Sources: foreign-filer sentence; tag coverage | OK; every tag family used appears in the table (the table also lists the unused 6-K Q2 2026 MD&A row; harmless) |
| Nothing after the cutoff | OK |

**Claims (§9)** — 12 claims (within 6–12); headline guidance is 3 of 12 (1, 3, 4), no EPS claim; the rest are capacity, prepayments, backlog, financing, delivery milestones.

| # | One sentence, one check | Single direction, can fail | Verbatim quote with tag underneath | Labels | Note |
|---|---|---|---|---|---|
| 1 | Yes | Yes ("reaffirms or raises", the permitted form) | Yes | — | headline |
| 2 | Yes | Yes | Yes | sharpening labelled | |
| 3 | Yes | Yes | Yes | sharpening labelled; arithmetic holds (H1 37.3%; ~40% on $3.0–3.4B needs H2 ≈ 41%) | |
| 4 | Yes | Yes | Yes | — | headline |
| 5 | Yes | Yes | Yes | — | |
| 6 | Yes | Yes ("reaffirmed" only) | Yes | — | |
| 7 | Yes | Yes | Yes | disclosure check labelled; "quarter figure, not year-to-date" stated; sharpening labelled with its arithmetic | uses the net increase in deferred revenue as a proxy for "prepayments received"; revenue recognised out of the balance makes the proxy conservative; say so (REVISE 8) |
| 8 | Yes | Yes | Yes | disclosure check labelled; "quarter-end balance" stated | the quote is soft, the check is a number; fine |
| 9 | Yes | Yes | Yes | — | observable event; the July facility is the baseline |
| 10 | Yes | Yes (Met if repeated; Missed if a slipped tranche is disclosed; Dropped if silent) | Yes | — | |
| 11 | Yes | Yes | Yes | — | |
| 12 | Yes | Yes | Yes | two-quarter horizon labelled, ⏳ rule stated | |

No either/or claims, no double-barrelled claims, no unlabelled hardening of soft phrases.

---

## 6. Length

Script output (the binding method), before the reviewer's edits:

```
/home/ubuntu/finance/companies/NBIS/business.md 2832
/home/ubuntu/finance/companies/NBIS/outlook.md 1163
```

After the reviewer's glosses:

```
/home/ubuntu/finance/companies/NBIS/business.md 2976
/home/ubuntu/finance/companies/NBIS/outlook.md 1187
```

Both inside the binding ranges (2,000–3,000 and 800–1,200): **pass**. Both are in the upper half; the writer aimed for 2,100–2,500 and 850–1,000. The first round of reviewer glosses pushed business.md to 3,009; the reviewer shortened its own glosses to bring it back to 2,976. There are about 24 words of headroom in business.md and 13 in outlook.md, so the writer's fixes below must be word-neutral or paired with a cut (candidates: the financing list at the end of §1, line 10, duplicates the §7 table; §6#7 could lose a clause).

---

## 7. Verdict: REVISE

Numbered list for the writer. Numbers, quotes, structure, claims and the indicator list are untouched by the reviewer and must be changed by the writer.

1. **business.md §4 table, line 63 ("of which increase in deferred revenue") and line 66 ("Share-based compensation").** Replace the FY2022 "n/d" with **0.8** and **9.6** respectively, from the FY2024 20-F cash-flow statement (20-F-FY2024.txt lines 3583 and 3563; columns 2022 / 2023 / 2024, Toloka-inclusive basis, the same basis the column already uses). The footnote's "\*FY2022 on the FY2024 20-F basis" already covers them.
2. **business.md §7, line 135.** "6,000,000 of those options carry a $100.00 exercise price" is not in the filings. Suggested: "6,000,000 of those options were granted 'with exercise prices that were considered to be \"deeply out of the money\"' [20-F FY2025, F-pages, Note 14]; the ownership footnotes show the COO, Chernin and Korolenko each holding 625,000 vested 'premium priced' options at 'an exercise price of $100 per share' (the price at which the option lets you buy a share) [20-F FY2025, Item 7]." If you want to keep the ~$100 for all 6,000,000, label it: "(our computation from the $96.69 weighted-average grant price across 6,350,000 options)".
3. **business.md §6#3, line 107.** "Microsoft and Meta appear by name only in the 20-F and the Q1 6-K" is over-broad: the Q2 shareholder letter (p.5) names both. Suggested: "no customer is named in the concentration tables; Microsoft and Meta are named in the 20-F (Note 1), the Q1 6-K (Note 1) and the shareholder letters, but not in the Q2 6-K financial statements or on the Q2 call [20-F FY2025, F-pages, Note 1; 6-K Q1 2026 FS, Note 1; Q2 2026 letter, p.5]".
4. **outlook.md §1, line 19.** "rounds the release's $2,246.1M" is wrong (2,246.1 rounds to $2.2 billion). Suggested: "The letter's infographic and the call both say '$2.3 billion' of Q2 operating cash flow; the release's cash-flow statement shows $2,246.1M; the release figure is used [Q2 2026 letter, p.2; Q2 2026 call; Q2 2026 release]." Optionally add that the release's highlights table prints Q2 2025 operating cash flow as $(167.7)M while its cash-flow statement says $(167.9)M; the statement figure is used.
5. **outlook.md §1, row 5 (line 14), last cell.** "No capex figure in the Q1 release or letter" reads as if Q1 capex was not reported; it was ($2,472.9M; "approximately $2.5 billion"). Suggested: "No FY2026 capex guidance in the Q1 release or letter; the Q2 call's 'We continue to expect ... $20 billion to $25 billion' implies an earlier figure given outside this report's sources [Q1 2026 release; Q1 2026 letter; Q2 2026 call]".
6. **Label two computations.** business.md line 76: "13.0 million (computed) options and unvested RSUs"; line 121: "about 3.8 million shares (computed: 1.4 million as purchase consideration and 2.4 million to Eigen AI employees)". Both from the notes already tagged.
7. **Small consistency items (optional but cheap).** (a) §3 table row "Adjusted EBITDA margin (computed)" (line 44) mixes the FY2025 20-F definition (FY2024–FY2025) with the 2026 6-K definition (H1, Q2); add "definitions differ, see text" to the row label or footnote. (b) §4 table shows the H1 2026 deferred-revenue increase as 4,395.0 (cash-flow line) while outlook claim 7 uses Note 4's 4,397.7; a footnote reconciling the two saves a reader's double-take. (c) Glossary "Take-or-pay" (line 172) is never used in the text: use the term in §5 or delete the entry. (d) business.md Sources table lists [Q1 2026 letter], which the body never cites; harmless, delete or leave.
8. **outlook.md claim 7 (line 61), optional wording.** Add "(the net increase in deferred revenue is the proxy for prepayments received; revenue recognised out of the balance makes the proxy conservative)" so next quarter's grader knows why a smaller balance change than cash received is not a miss.
9. **Length.** Any words added by items 1–8 should be offset. The §1 financing sentence (line 10) repeats what the §7 table shows and can be cut to "Since then it has raised money almost continuously (details in §7)".
10. **For the owner at indicator lock (not for the writer).** Indicator 7's power-commitments half (Note 11) did not appear in the Q1 2026 6-K (line 16 of outlook.md already says so). Either keep only the leases-not-commenced figure (Note 8, present in both 2026 6-Ks) or accept that the second number may be annual-only. Indicator 2 (ARR) is a management KPI, not a financial-statement line; it has appeared in three consecutive letters and is the basis of FY2026 guidance, so it is worth keeping, but it will vanish the day management stops reporting it.

---

## Edits made by reviewer

Jargon glosses, two glossary entries, one tag. No number, quote, table cell value, claim or indicator was changed. Backups of the pre-edit drafts: `/tmp/nbis-business.md.bak`, `/tmp/nbis-outlook.md.bak`.

business.md
- Line 10: "went into treasury" → "went into treasury (shares the company holds itself)".
- Line 25: "revenue is recognized evenly" → "revenue is recognized (counted) evenly"; "investment-grade customers" → "investment-grade customers (customers with top credit ratings)".
- Line 27: after "in nine tranches during 2025 and 2026" added "(tranche: a batch delivered on its own schedule)".
- Line 35: after the cost-of-revenues quote added "(co-location: renting space and power in someone else's data center)"; "(D&A)" → "(D&A; amortization is the same spreading of cost for purchased software and similar assets)".
- Line 48 (§3 table footnote): appended "H1 = first half (January–June); n/m = not meaningful (revenue too small for a percentage)."
- Line 50: after "operating leverage as we scaled capacity" added "(operating leverage: fixed costs spread over more revenue)".
- Line 52: "payback" → "payback (time to earn back the money spent)".
- Line 56: "Operating cash flow" → "Operating cash flow (cash from running the business, before investment)".
- Line 72 (§4 table footnote): appended "carrying value = the balance-sheet amount, below the sum due at maturity."
- Line 76: "NVIDIA warrant shares" → "NVIDIA warrant shares (rights to shares, already paid for)"; "options" → "options (rights to buy shares at a set price)"; "that vest over time" → "that vest, meaning become theirs, over time".
- Line 92: "high-coupon" → "high-coupon (high-interest)".
- Line 94: "impairment charge" → "impairment charge (a write-off of equipment judged worth less than its book value)".
- Line 98 (§6 table header): "Largest shares of receivables" → "Largest shares of receivables (money owed by customers)".
- Line 107: "service credits" → "service credits (refunds owed when service falls short)".
- Line 113: "material weaknesses in internal control" → "... (serious gaps in the checks behind the accounts)".
- Line 121: "no buybacks" → "no buybacks (buying back its own shares)".
- Line 125 (§7 table): "Dec 2024 private placement" → "Dec 2024 private placement (shares sold directly to chosen investors)".
- Line 135: tag "[Q2 2026 release; 6-K Q2 2026 FS, Note 3]" → "[Q2 2026 release; 6-K Q2 2026 MD&A, Share-based compensation; 6-K Q2 2026 FS, Note 3]" — the "$74.9 million ... in connection with the acquisition of ... Eigen AI" figure that makes "mostly" true (54% of $137.8M) is in the MD&A (line 312), not in Note 3 or the release.
- Line 137: "11.33% economic interest" → "11.33% economic interest (share of the company's value)".
- Line 170 (glossary, Convertible notes): "dilution later" → "dilution later (each existing share owns a smaller slice)".
- Lines 173–174 (glossary): added entries **Contracted / connected power** and **GAAP**.

outlook.md
- Line 6: added "H1 2026 is the first half (January–June 2026)."
- Line 15 (row 6): "ATM" → "ATM (at-the-market share sales)".
- Line 23: after the CEO quote added "(multi-tenant: many customers share the same machines)".
- Line 49: after the financing quote and its tag added "(asset-backed: loans secured on specific GPUs or customer contracts.)".


---

## Reviewer pass 2 (re-check of the writer's second pass; review cycle 2 of 2)

_Re-checked 2026-09-07 against `sources/2026-Q2/` only. Pass 1 above is left as written; corrections to it are recorded in §2.6 below._

### 2.1 Status of the REVISE items

| # | Item | Status | Evidence in the revised file (fragment grepped) and source check |
|---|---|---|---|
| 1 | §4 table FY2022 "n/d" cells | **Resolved** | business.md line 63 `\| of which increase in deferred revenue \| 0.8 \| 1.9 \|`; line 66 `\| Share-based compensation \| 9.6 \| 28.8 \|`. Footnote (line 72) now tags "[20-F FY2024, F-pages, statements of cash flows and balance sheet]" and redefines n/d as "no Dec 31, 2022 balance sheet in this report's sources". Source: 20-F-FY2024.txt line 3583 "Deferred revenue \| 0.8 \| 2.3 \| 9.6", line 3563 "Share-based compensation expense \| 14 \| 9.6 \| 31.4 \| 56.6" |
| 2 | §7 "$100.00 exercise price" | **Resolved; pass-1 finding G31 withdrawn** | line 135: `6,000,000 of those options, "granted with market conditions", are listed in the awards table at a $100.00 exercise price (the price at which an option lets you buy a share), and the ownership footnotes show the COO, Chernin and Korolenko each holding 625,000 vested "premium priced" options "at an exercise price of $100 per share" [20-F FY2025, Item 6; F-pages, Note 14; Item 7]`. The writer is right: 20-F-FY2025.txt line 6532, Note 14 awards-outstanding table, reads `$ 100.00 \| Option \| 6,000,000 \| 9.3 \| 16.3 \| 1,500,000 \| 9.3 \| 16.3`; footnote line 6506 "Includes 6,000,000 options granted with market conditions"; Item 7 lines 2434, 2466, 2470 "at an exercise price of $100 per share". The pass-1 grep for "100.00" was piped through `head -8` and dropped the line-6532 hit; the reviewer's error, not the writer's |
| 3 | §6#3 "appear by name only in the 20-F and the Q1 6-K" | **Resolved** | line 107: "no customer is named in the tables; Microsoft and Meta are named in the 20-F, the Q1 6-K and the shareholder letters, but not in the Q2 6-K statements or on the Q2 call [20-F FY2025, F-pages, Note 1; 6-K Q2 2026 FS, Note 4; 6-K Q1 2026 FS, Note 1; Q2 2026 letter, p.5; Q2 2026 call]". Letter p.5 names both ("delivered all capacity tranches to Microsoft"; "our second Meta agreement"); transcript.txt: 0 hits for "microsoft" (case-insensitive), 0 for "Meta" as a word |
| 4 | outlook §1 "rounds the release's $2,246.1M" | **Resolved** | outlook.md line 19: `The letter's infographic and the call both say "$2.3 billion" of Q2 operating cash flow; the release's cash-flow statement shows $2,246.1M, which is used here [Q2 2026 letter, p.2; Q2 2026 call; Q2 2026 release]`. Letter p.2 "Including $2.3 billion in positive operating cash flow"; transcript line 44 "Operating cash was $2.3 billion in the quarter"; release line 207 "2,246.1". The writer removed the year-ago comparison sentence, so the optional (167.7)/(167.9) note no longer has a home; nothing depends on it |
| 5 | outlook §1 row 5 "No capex figure" | **Resolved** | line 14: `No FY2026 capex guidance in the Q1 release or letter; the Q2 call's "We continue to expect ... capital expenditures of $20 billion to $25 billion" implies an earlier figure given outside this report's sources [Q1 2026 release; Q1 2026 letter; Q2 2026 call]`. Both fragments around the ellipsis are verbatim in transcript.txt (1 hit each) |
| 6 | Label two computations | **Resolved** | line 76 "13.0 million (computed) options"; line 121 "about 3.8 million shares, computed as 1.4 million of purchase consideration and 2.4 million to Eigen AI employees". 6-K-2026-Q2-financials.txt lines 966 "approximately 1.4 million Class A ordinary shares", 968 "approximately 2.4 million Class A ordinary shares" |
| 7a | §3 row mixes two adjusted-EBITDA definitions | **Resolved** | line 44 row label "Adjusted EBITDA margin (computed; definitions differ, see text)" |
| 7b | 4,395.0 vs 4,397.7 | **Resolved** | line 72: "Note 4 gives the H1 2026 increase as 4,397.7 (used in outlook claim 7); the $2.7M gap is not explained [6-K Q2 2026 FS, Note 4]". Note 4 line 1198 "increased by $1,197.1 and $4,397.7"; 4,397.7 − 4,395.0 = 2.7 |
| 7c | Glossary "Take-or-pay" unused | **Resolved** | §5 line 80 now reads `Microsoft and Meta pay take-or-pay, "irrespective of actual utilization"`; 20-F-FY2025.txt Note 1 lines 4296 and 4312 carry the phrase; glossary entry (line 172) retained |
| 7d | Unused Sources rows | **Resolved** | [Q1 2026 letter] row removed from business.md Sources; grep "Q1 2026 letter" in business.md = 0. [6-K Q2 2026 MD&A] row removed from outlook.md Sources; grep in outlook.md = 0 |
| 8 | Claim 7 proxy | **Resolved** | outlook.md line 61 adds "the net increase in deferred revenue is the proxy for prepayments received, and revenue recognised out of the balance makes it conservative". Still one sentence, one check, labelled disclosure check with the quarter stated |
| 9 | Length offset | **Resolved** | line 10 now "Since then it has raised money almost continuously (details in §7) [20-F FY2025, Item 5]" (Item 5 line ~2020 supports it). Counts 2,794 / 1,095 (see §2.5) |
| 10 | Owner note (indicator 7) | n/a | Not for the writer; unchanged, as intended |

### 2.2 New or changed tags introduced by the writer

| Tag / figure | Source check | Result |
|---|---|---|
| [20-F FY2025, F-pages, Note 14] "$100.00" awards row and "granted with market conditions" | 20-F-FY2025.txt lines 6532, 6506 | PASS |
| [20-F FY2025, Item 7] "at an exercise price of $100 per share" | lines 2434, 2466, 2470 (footnotes 3, 11, 12: Nave, Chernin, Korolenko) | PASS |
| [6-K Q2 2026 FS, Note 3] 1.4 million / 2.4 million | lines 966, 968 | PASS |
| [20-F FY2024, F-pages, statements of cash flows and balance sheet] 0.8 and 9.6 | lines 3583, 3563 (2022 column; header line 3549) | PASS |
| [Q2 2026 letter, p.2] "$2.3 billion"; [Q2 2026 letter, p.5] Microsoft, Meta | reading-order p.2, p.5 | PASS |
| [Q2 2026 call] "Operating cash was $2.3 billion in the quarter"; zero Microsoft / Meta hits | transcript.txt line 44; 0 / 0 | PASS |
| [6-K Q2 2026 FS, Note 4] 4,397.7 footnote | line 1198 | PASS |
| [20-F FY2025, F-pages, Note 1] "irrespective of actual utilization" (take-or-pay sentence, §5) | lines 4296, 4312 | PASS |
| §6#3 rephrased quote: "terminate individual tranches" ... "specified delivery delays or repeated failure to meet availability requirements" | Note 1 Microsoft paragraph (line 4296 block; also Item 10 lines 2768, 2792) | PASS (verbatim fragments) |
| outlook row 5 ellipsis quote | transcript.txt, both halves verbatim | PASS |

10 new checks, 10 PASS.

### 2.3 Damage check after the cuts

- **Headings.** business.md: §1–§8, Glossary, Sources present in order (lines 4, 12, 31, 54, 78, 88, 117, 139, 156, 176). outlook.md: §1–§5, Sources (lines 4, 21, 27, 41, 53, 68); §6 Tone shift correctly absent.
- **§8 marker** `_Proposed — owner to review and lock._` present (line 141).
- **Tag coverage.** business.md body: 101 tags in 10 families (20-F FY2025 / FY2024 / FY2023; 6-K Q2 2026 MD&A; 6-K Q2 2026 FS; 6-K Q1 2026 FS; Q2 2026 release; Q2 2026 letter; Q1 2026 release; Q2 2026 call); every family has a Sources row and no row is unused. outlook.md body: 61 tags in 7 families, all in the table, no unused rows. Foreign-filer sentence present in both.
- **Untagged prose.** Only structural sentences carry no tag: business.md line 90 ("Ranked from most to least plausible."), line 154 (pointer to outlook §5); outlook.md line 6 (table note). No factual sentence lacks a tag.
- **Cuts read for damage.** Removed material was restatement (Austin location; "JSC Solid Management" and the 50% discount quote; 1,300 employees / RUB 1.8bn; the "over $5 billion" / "more than $6 billion" list; 7.7x / 8.3x prose duplicating the table; the "$15 billion" ClickHouse valuation quote; "relatively short-term" quote; Israel headcount; ">$15 billion (computed)"; outlook year-ago line; "cannot build all of it"; Reflection / Cohere naming; "Owned capacity ... more than 75%"; the p.11 quote (tag retained, still supports "restates no numbers"); the §4 Q3 timing quote, which survives under claim 2). Every remaining tag still supports its sentence. One dangling pronoun found (§3, "Its estimated payback" after "Management guides") and fixed directly (§2.4).
- **Claims.** 12 present; unchanged except 2 (sharpening label reworded: "our sharpening of the timing statement below") and 7 (proxy named). All single-direction, one check each, quotes verbatim, labels intact.
- **Cutoff.** Date sweep for anything after 2026-08-12 finds nothing.
- **Company quirks 1–7.** All still satisfied (computed margins labelled; definition change now flagged in the table row too; table bases stated; release figures used for both conflicts with the conflict now described correctly; no quarterly concentration series; Microsoft / Meta sentences tagged to the 20-F, Q1 6-K or letter; guidance verbatim).

### 2.4 Direct edit made in pass 2

- business.md line 52: "Its estimated payback (time to earn back the money spent) on Q2 deals is" → "Management's estimated payback (time to earn back the money spent) on Q2 deals is". The writer's cut of the preceding sentence left "Its" pointing at "Management". Word count unchanged.

### 2.5 Word counts (binding script)

```
/home/ubuntu/finance/companies/NBIS/business.md 2794
/home/ubuntu/finance/companies/NBIS/outlook.md 1095
```

Before the pass-2 edit: 2794 / 1095 (the edit swapped one word for one word). Both inside the binding ranges and under the 2,900 / 1,150 ceilings set for this cycle. Both remain in the upper half of their ranges; not a failure.

### 2.6 Corrections to pass 1

- **G31 withdrawn.** The $100.00 exercise price for all 6,000,000 options is disclosed in the Note 14 awards-outstanding table (line 6532). Pass-1 totals become **92 checked, 85 PASS, 5 FAIL (C4, C7, D5, D9, G23), 2 label-only**. REVISE item 2's premise was wrong; the writer's rewrite is nonetheless better than the original because it cites the table row and the footnote and quotes the Item 7 wording.
- §4 invented-number item 1 is likewise withdrawn.

### Final verdict: **PASS**

Nothing factual remains wrong. Open for the owner (notes, not failures):
1. Indicator 7's power-commitments half (Note 11) was not in the Q1 2026 6-K; decide at lock whether to keep it (see pass-1 REVISE 10).
2. Indicator 2 (ARR) is a management KPI, not a statement line; it vanishes the day management stops reporting it.
3. The $2.7M gap between the cash-flow deferred-revenue line (4,395.0) and Note 4's increase (4,397.7) is not reconciled anywhere in the 6-K; the draft says so.
4. The Q2 release prints Q2 2025 operating cash flow as (167.7) in its highlights table and (167.9) in its cash-flow statement; the drafts no longer cite either, but future refreshes should take the statement figure.
