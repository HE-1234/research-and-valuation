# Netflix, Inc. (NFLX) — Review of the Q2 2026 drafts

_Reviewer pass 1. Written 2026-09-08. Drafts reviewed: `business.md` (2,480 prose words before my edits, 2,546 after) and `outlook.md` (981 before, 989 after), counted with `/tmp/nflx-orch/wc_prose.py`. Cutoff 2026-07-17. Every number below was checked against the cached source text in `sources/2026-Q2/` (filings, letters, workbook, transcripts), not only against the notes files._

## 1. Rubric (§14)

| # | Question | Answer | Reasoning |
|---|---|---|---|
| 1 | Can I explain what the company does, and who pays it, in two sentences? | Yes | §1 opens with the two payers (members on plans from $1 to $38 a month; advertisers on the $8.99 ad plan) and how each pays; §2 gives the four regions and the last membership and ARM figures. |
| 2 | Do I know exactly what would kill it, and what the early warning sign is? | Yes | §6 ranks six scenarios, each with the trigger, an early warning tied to a disclosure (UCAN growth at or below 10%, cash content spend above 1.1x amortization for a year, the $3 billion ad line dropped, an 8-K Item 1.01) and the exposed profit pool. |
| 3 | Do I know why the margins are what they are, and whether cost scales with usage? | Yes | §3 separates the fixed content cost (payment terms "not tied to member usage") from the usage-linked "other cost of revenues" (about 15% of revenue) and explains the cash-versus-amortization timing that governs both margin and free cash flow. |
| 4 | Could I predict what the scorecard will check next quarter, from §5 of the outlook alone? | Yes | Ten claims, each with a threshold, a period and the line to read (letter table, cash-flow line, 10-Q "Proceeds from issuance of debt"). |
| 5 | Did nothing in the report require knowledge I don't have? | Yes, after my glosses | Terms that needed a clause (hedging, tranches, net debt, effective tax rate, guild, linear TV, equity value, bridge loans, diluted shares, over-index) now carry one; the rest are plain, name-inferable or in the glossary. |

## 2. Citation spot-check

### 2a. Every number in business.md §3 and §4 tables (and the §2 and §7 tables, which feed them)

All figures in USD thousands in the filings; the report rounds to billions. "Recomputed" means I re-derived the figure from the stated inputs.

**§3 Economics table** (source: FY2025 10-K income statement, FY2023 10-K income statement for 2021–2022, 10-Q Q2 2026 income statement and cash-flow statement; capex from the cash-flow statements):

| Row | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | 6M 2026 | Result |
|---|---|---|---|---|---|---|---|
| Revenue | 29,697,844 | 31,615,550 | 33,723,297 | 39,000,966 | 45,183,036 | 24,809,695 | all 6 match |
| Cost of revenues | 17,332,683 | 19,168,285 | 19,715,368 | 21,038,464 | 23,275,329 | 11,925,203 | all 6 match |
| Gross margin (recomputed) | 41.64% | 39.37% | 41.54% | 46.06% | 48.49% | 51.93% | all 6 match to one decimal |
| Operating margin (as reported) | 21% [10-K FY2023 Item 7] | 18% [10-K FY2023 Item 7] | 20.6% [10-K FY2025 Item 7] | 26.7% | 29.5% | 32.8% [letter p.14; 8,149,607 / 24,809,695 = 32.85%] | all 6 match |
| Capex | 524,585 | 407,729 | 348,552 | 439,538 | 688,220 | 414,774 | all 6 match |
| Capex / revenue (recomputed) | 1.77% | 1.29% | 1.03% | 1.13% | 1.52% | 1.67% | all 6 match |

**§3 Content table** (cash-flow statements; balance sheets; content-obligation notes: FY2022 10-K Note 7, FY2023 10-K Note 8, FY2025 10-K Note 9, 10-Q Note 9):

| Row | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | 6M 2026 | Result |
|---|---|---|---|---|---|---|---|
| Additions to content assets | 17,702,202 | 16,839,038 | 12,554,703 | 16,223,617 | 17,096,617 | 9,774,440 | all match |
| Amortization | 12,230,367 | 14,026,132 | 14,197,437 | 15,301,517 | 16,422,166 | 8,529,209 | all match |
| Ratio (recomputed) | 1.447 | 1.201 | 0.884 | 1.060 | 1.041 | 1.146 | all match (1.45 / 1.20 / 0.88 / 1.06 / 1.04 / 1.15) |
| Content assets, net | 30,919,539 | 32,736,713 | 31,658,056 | 32,452,462 | 32,778,392 | 33,837,573 | all match |
| Total content obligations | 23,161,360 | 21,831,947 | 21,713,349 | 23,248,931 | 24,039,228 | 25,106,705 | all match |
| Not on balance sheet | $15.8B | $14.2B | $14.6B | $17.0B | $18.4B | $19.6B | all match (stated in the notes) |

**§4 Cash table** (cash-flow statements; balance sheets; Q4 2025 letter p.15 and Q2 2026 letter p.12 for the FY2024, FY2025 and 6M 2026 free-cash-flow figures):

| Row | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | 6M 2026 | Result |
|---|---|---|---|---|---|---|---|
| Operating cash flow | 392,610 | 2,026,257 | 7,274,301 | 7,361,364 | 10,149,273 | 7,034,017 | all match |
| Free cash flow (recomputed OCF − capex) | (131,975) | 1,618,528 | 6,925,749 | 6,921,826 (letter: same) | 9,461,053 (letter: same) | 6,619,243 (letter: same) | all match |
| Net income | 5,116,228 | 4,491,924 | 5,407,990 | 8,711,631 | 10,981,201 | 8,684,205 | all match |
| FCF ÷ NI (recomputed) | negative | 0.360 | 1.281 | 0.795 | 0.862 | 0.762 | all match |
| Repurchases (cash) | 600,022 | — | 6,045,347 | 6,263,746 | 9,127,167 | 5,984,991 | all match |
| Cash and cash equivalents | 6,027,804 | 5,147,176 | 7,116,913 | 7,804,733 | 9,033,681 | 9,099,232 | all match |
| Debt (short + long, recomputed) | 699,823 + 14,693,072 = 15,392,895 | 14,353,076 | 399,844 + 14,143,417 = 14,543,261 | 1,784,453 + 13,798,351 = 15,582,804 | 998,865 + 13,463,971 = 14,462,836 | 2,483,758 + 11,825,548 = 14,309,306 | all match |

**§2 Regional revenue table**: all 24 regional cells (FY2021–FY2024 from the FY2023 and FY2025 10-K segment tables and Item 7; 6M 2026 from 10-Q Item 2) match; DVD residuals 182 / 146 / 83 → 0.2 / 0.1 / 0.1 match; reported growth rows match the 10-K Item 7 tables for each year (FY2022: 9% / — / 14% / 9%; FY2023: 6 / 8 / 9 / 5; FY2024: 17 / 17 / 9 / 17; FY2025: 15 / 17 / 11 / 21; 6M 2026: 12 / 16 / 20 / 18); FX-neutral rows match the FY2025 10-K constant-currency table (15 / 16 / 23 / 22) and the 10-Q six-month table (12 / 11 / 17 / 18); totals 6% / 7% / 16% / 16% (17%) / 15% (13%) match. The "—" for FY2022–FY2024 FX-neutral regional growth is correct: neither the FY2023 nor the FY2024 10-K publishes regional constant-currency revenue growth (the FY2024 "constant currency change" rows are ARM, not revenue). **Membership table**: 221,844 / 230,747 / 260,276 / 301,626 and the ten ARM figures all match the FY2023 and FY2024 10-K Item 7 tables; "over 325" matches Q4 2025 letter p.2.

**§7 Buybacks table**: cash rows match the cash-flow statements; shares repurchased 145,137,900 / 98,619,350 / 86,536,215 match the FY2025 10-K equity statement (post-split), 1,182,410 × 10 = 11.8 million is correctly labelled computed, 66,431,786 matches 10-Q Note 10; shares outstanding 443,963,107 × 10 = 4,439.6 (labelled computed), 4,453,467,760 / 4,327,595,840 / 4,277,571,000 / 4,222,162,150 match the FY2025 10-K equity statement (post-split, so not computed), 4,163,939,676 matches the 10-Q cover; authorizations $5B (Mar 2021), $10B (Sep 2023), $15B (Dec 2024), $25B (Apr 2026) match the 10-K notes and 8-Ks; remaining $17.1B (FY2024 10-K Item 7 and 8-K 2025-01-21), $8.0B (FY2025 10-K Item 7), $27.1B (10-Q Part II Item 2: $27,120,118K) match. **Two cells fail**: see Failure 1 below.

### 2b. Outlook §1 table cells

Every cell checked against the Q2 2026 letter (pp.1, 3, 5, 6, 7, 10, 12, 14), the Q1 2026 letter (pp.1, 2, 3, 5, 6, 7, 10, 14), the Q1 2026 interview p.6, the 10-Q Note 10 and the workbook Cashflow sheet. All match, including: Q2 regional 10/10, 14/11, 21/16, 16/18 and total 13/12 on $12,560M; Q1 regional 14/14, 17/12, 19/18, 20/19 and total 16/14 on $12,250M; guidance "13% (or 12% F/X neutral)" and $12,574M; margins 33.4% and 32.8% / 32.7% (letter p.14), 32.3% and 32.3% / 32.2% (Q1 letter p.14), guide 32.6% and 31.5%; additions 4,927,523 / amortization 4,311,309 = 1.143 and 4,846,917 / 4,217,900 = 1.149; amortization growth 4,311,309 / 3,832,074 = +12.5% and 4,217,900 / 3,823,112 = +10.3%; FCF $1,525,168K and $6,619,243K, Q1 $5,094,075K; ad statements verbatim; hours "more than 97 billion hours, up 2% year over year"; buybacks $4.7B / 52,934,688 / $27.1B / 4,261,300 and $1.3B / 13.5M / $6.8B / 4,298,437; obligations $25,106,705K and $24,139,431K.

### 2c. Outlook §4 guidance quotes

All seven quotations were compared character by character with `shareholder-letter.txt` pp.2, 5 and 6: Q3 revenue and margin sentence, FY2026 revenue/margin paragraph, content amortization sentence, FCF and 1.1x sentence, the $3 billion ads sentence and the $1B refinancing sentence. All verbatim. The Q3 table figures ($12,860M, $4,268M, $3,452M, $0.82) match letter p.1.

### 2d. Tagged sentences checked (beyond the tables), 61 in all

Verified verbatim or numerically against the cited page or section: the §1 Item 1 and Note 1 quotations, the $1–$38 and $2–$10 price ranges (10-Q Item 2), the FY2022 "recently introduced" ad plan (Item 1A), the $8.99 US price (interview p.10), "over 325M" and "approaching one billion people" (Q4 2025 letter p.2), the discontinued-reporting sentence (10-K FY2025 Item 7), incorporation 1997 (Note 1: August 29, 1997), DVD end September 29, 2023 (10-K FY2023 Item 7), streaming 2007 / animation 2018 / live 2023 (Q2 letter pp.2–3), the 2022–2024 net-addition figures, the split date (8-K 2025-11-14), the region attribution ("geographic location used at time of sign-up", 10-K FY2024 Item 7), the 10-Q revenue drivers sentence, the ARM-gap quotation (interview p.10), "rose more than 2.5x to over $1.5B" (Q4 letter p.1), "about a 25% contributor" (MS conference p.9), 56% / 31% (Item 7A), the amortization-policy quotations (Note 1: ten years, accelerated, over 90% within four years), the "paid as the content is created" quotation (Item 7), the WGA-strike quotation (Q4 letter p.3), "~10%" and "~1.1x" and "$20 billion" (letter pp.2, 6; MS p.5), "not tied to member usage" (Item 1A), 16% vs 7% (recomputed 16,422,166 / 15,301,517 = 7.3%), "We grow the content spend slower than revenue" (interview p.6), "a little over 2 percentage points ... per year" over the last five years and "no ceiling" (MS pp.5–6), other cost of revenues about 15% (recomputed 6,853,163 / 45,183,036 = 15.2%), the 52 / 36 / 7 / 8 / 4 cents split (recomputed), $2.0B property and equipment, the FCF definition (letter p.6 footnote), the $2.8B fee in interest and other income (10-Q Item 1 footnote; Q1 letter p.2), first-half net income 8,684,205 vs 6,015,764, operating income +14.4%, "roughly $11B" to "approximately $12.5B" and "due primarily to the after-tax impact" (Q4 letter p.6; Q1 letter p.5), "$85 million" and "$729 million" (10-Q Item 2), "twelve tranches" and "$1B ... refinance", net debt $5,244,190K, "ample liquidity" and "solid investment grade rating", the 13.7% effective rate (Note 11) and the return-on-capital arithmetic (13,326,603 × 0.863 = 11.5B; 26,615 + 14,463 − 9,062 = 32.0B; 36%), "can change their plans at any time" (Item 1), the programming-ROI quotation (interview p.11), "more than a third of all viewing" (letter p.3), $3.4B technology and development, the SVOD quotation (interview p.10), "first place people go ... last they cancel" (Q1 letter p.3), "industry-leading retention" (interview p.6), UCAN 18% to 10% (letter p.7), hours 1.5% / 2% and the Japan remark (MS p.7), free-trial re-testing (letter p.5), 9.0% and "over 40%" (Q4 letter p.6), 76% and 32% shares (recomputed), the six §6 risk-factor quotations (Items 1 and 1A), "less than 45%" (Q1 letter p.3), EMEA 16% / 11%, the NFL agreement (letter p.4), $619 million (Note 9), "open content platform providers" (Item 1) and "YouTube is a key competitor" (MS p.7), the supplier quotation (MS p.8), the AWS dependency (Item 1A), the officer ages and tenures (proxy pp. Who We Are and Executive Officers: Sarandos 61, co-CEO since 2020, CCO 2000–2023; Peters 55, co-CEO since January 2023, at Netflix since 2008; Neumann 56, CFO since January 2019), the Hastings sentences (proxy line "the co-founder and former co-CEO and President of the Company"; April 17, 2025 transition; 8-K 2026-04-16; 8-K 2026-06-05 Item 8.01), the bonus design (35% / 65%, 117.57%; 50% RSU / 50% PSU), the pay totals (53,905,972 / 53,187,307 / 20,834,050), the say-on-pay arithmetic (2,660,768,297 / (2,660,768,297 + 517,268,246) = 83.7%), "two times the sum of" and retirement vesting (8-K 2025-11-04), 1.24% and 37,759,062 shares, Vanguard 8.65% / BlackRock 7.34% / FMR 5.29% on 2023 holdings with the "0.0%" March 2026 caveat, the capital-allocation quotation (letter p.6), no dividend (Item 5), the 6.5% share-count fall (4,163.9 / 4,453.5), "our largest quarter of share repurchases", the WBD terms ($23.25 cash and $4.50 stock collar, 8-K 2025-12-05; "$72.0 billion" equity value, 10-K FY2025 Item 7 and Note 9; "$59,000,000,000"; $2.8B and $5.8B fees; "$27.75 ... entirely in cash", 8-K 2026-01-20; the pause, Q4 letter p.7; "would not seek to make any revisions" and "on behalf of WBD, paid the $2,800,000,000", 8-K 2026-02-27), "all about price" (MS p.8), the $587 million unnamed acquisition (10-Q Note 6) and InterPositive (Q1 letter p.4), and every quotation in outlook §2, §3 and §5.

### 2e. Failures

Four items failed (two table cells, two sentences); one further sentence is unsupported by its tag. All are listed in §9 as REVISE items.

1. **business.md §7, buybacks table, row "Authorization remaining, period end", cells FY2022 and FY2023 read "n/d".** The sources are not silent. 10-K FY2022, Item 5 and Item 7: "As of December 31, 2022, $4.4 billion remains available for repurchases." 10-K FY2023, Item 7 (line 861): "As of December 31, 2023, $8.4 billion remains available for repurchases." (FY2021 is genuinely not stated in a cached filing; the FY2022 10-K's "There were no repurchases during the year ended December 31, 2022" implies $4.4 billion at end-2021 as well, which may be shown as an inference or left n/d.)
2. **business.md §4: "since 2023 it has run at roughly 80–90% of net income [10-K FY2025, Note 11]".** The table two lines above shows 2023 at 1.28 (free cash flow above net income); only 2024 (0.79), 2025 (0.86) and the first half of 2026 (0.76) fit "roughly 80–90%". The tag does not support the sentence either: Note 11 is Income Taxes. The figure is a computation from the table.
3. **business.md §7: "the financing ended and Netflix paid nothing [8-K 2026-02-27, Item 1.02]".** The 8-K says the bridge, revolver and term-loan commitments "were each automatically terminated"; it says nothing about what Netflix paid. The report itself records "approximately $85 million" of financing costs written off in Q1 2026 interest expense (10-Q Item 2) and the Q4 2025 letter (p.2) records "~$60M of costs (booked in interest expense) related to our recent Warner Bros.-related bridge loan". What the sources support is that no termination fee was owed by Netflix (the $5.8 billion reverse fee applied only to a regulatory block, 8-K 2025-12-05).
4. **business.md §7: the severance change was made "citing only market practice" [8-K 2025-11-04, Item 5.02] [DEF 14A 2026, Compensation Discussion and Analysis].** Neither document gives a rationale for the October 2025 amendments. The 8-K describes the terms only; the proxy's "Amended and Restated Executive Officer Severance Plan" section lists the changes without a reason; the gatherer's notes (notes-filings.md, "not found" list) record this explicitly. The only competitiveness language in the proxy is the general pay-philosophy paragraph ("pay employees at their personal top of market"), which is not about this amendment.

Withdrawn after checking the full line (recorded per §17): "$72.0 billion" is not in the 8-K 2025-12-05 text, but it is in 10-K FY2025 Item 7 (line 877: "for a total equity value of approximately $72.0 billion ... as of December 4, 2025") and Note 9; the sentence carries both tags, so it passes. "Where the member signed up" (§2) is supported by 10-K FY2024 Item 7's footnote "assigned to territories based on the geographic location used at time of sign-up". "Expired in 2026" for the guild contracts is what 10-K FY2025 Item 1A says ("each expire in 2026", May 1 and June 30); I aligned the wording to the quotation (see §8) rather than fail it.

## 3. Jargon audit

Checked against the three tests (plain, name-inferable, or in the glossary). Glossary entries present: content amortization, FX-neutral (constant currency), free cash flow, ARM, the four region acronyms.

| Term | Where | Status |
|---|---|---|
| amortization | §3, §8, glossary | in glossary |
| FX-neutral / constant currency | §2, §5, §6, outlook | in glossary; also explained inline in §2 |
| ARM | §2, §5, §6, outlook §4 | in glossary; explained on first use |
| SVOD | §5 | glossed inline by the writer ("other subscription video services") |
| upfront | outlook §3 | glossed by the writer ("the annual advance sale of ad slots") |
| programmatic | outlook §3 | glossed by the writer ("automated") |
| CPM, churn, paid sharing, delayed-draw term loan, 13G, PSU/RSU, operating leverage, cash conversion | — | not used (the writer wrote "sharing crackdown", "performance shares, half time-vesting shares", "Free cash flow ÷ net income") |
| hedging | §2 | **fixed**: "(currency contracts that offset exchange-rate moves)" |
| Open Connect network | §3 | **fixed**: "Open Connect server network" |
| tranches | §4 (inside a quotation) | **fixed**: "(twelve separate bond issues)" |
| net debt | §4 | **fixed**: "(debt less cash)" |
| effective rate | §4 | **fixed**: "(tax actually charged as a share of pre-tax profit)" |
| guild | §6 | **fixed**: "(writers', actors' and directors' union)" |
| linear TV | §6 | **fixed**: "linear (traditional scheduled) TV" |
| equity value; bridge loans | §7 | **fixed**: "(the price for all the shares)"; "(short-term bank loans meant to be replaced by bonds)" |
| accelerated financing costs | §4 | **fixed**: "loan-arrangement fees written off ... when the Warner Bros. financing ended" |
| diluted weighted-average shares | §8 | **fixed**: "(the share count used for earnings per share)" |
| over-index | outlook §3 (inside a quotation) | **fixed**: "(take a bigger share of viewing than average)" |
| capital employed | §4 | defined inline by the writer |
| 8-K Item 1.01, investment grade rating, Nielsen, World Baseball Classic, TF1 | various | name-inferable or explained by context; left |

## 4. Invented-number check

- **$2.8B termination fee**: correctly placed in "interest and other income" in Q1 2026 (10-Q Item 1 footnote; Q1 letter p.2), explicitly excluded from operating income, and its tax and cash effects described with the right tags. Pass.
- **"$72.0 billion"**: supported by 10-K FY2025 Item 7 and Note 9 (the sentence carries the 10-K tag alongside the 8-K tag). Pass.
- **"~1.1x" and computed ratios**: guide quoted verbatim (letter p.6); every ratio in the §3 table and outlook §1 recomputed and matching; the 10.3% and 12.5% amortization growth figures recomputed from the workbook. Pass.
- **Buyback dollars per year and the $27.1B remaining**: cash figures match the cash-flow statements; $27.1B matches 10-Q Part II Item 2 and letter p.6. Pass. **Fail** on the FY2022 and FY2023 "n/d" cells (Failure 1).
- **2025 pay figures**: $53.9M / $53.2M / $20.8M match the Summary Compensation Table; 117.57%, 35% / 65%, 50/50 RSU/PSU match the CD&A. Pass.
- **Ownership**: 1.24%, 37.8 million, 8.65% / 7.34% / 5.29%, the 2023 dates and the "0.0%" March 2026 note all match the proxy's Security Ownership table and footnotes. Pass.
- **History dates**: 1997 (Note 1), September 29, 2023 (10-K FY2023 Item 7), 2007 / 2018 / 2023 (Q2 letter pp.2–3), November 14, 2025 (8-K), December 4, 2025 / January 19, 2026 / February 27, 2026 (8-Ks), April 17, 2025 (proxy), June 2026 (8-K 2026-06-05). All in cached sources. Pass.
- **Regional revenue table FY2021–FY2025**: every cell traced to the 10-K segment notes or Item 7 tables. Pass.
- **Pre-split vs post-split**: the two computed ×10 cells are labelled; FY2022–FY2025 share counts are taken from the post-split FY2025 10-K equity statement; per-share figures are not used in prose. Pass.
- **Quarter vs year-to-date**: outlook §1 labels quarter and YTD margins and FCF separately; the $729 million and $85 million are correctly attributed to the six-month and first-quarter periods. Pass.
- **Untagged figures**: none found; every computed figure is labelled "(computed)" or "(our inference)" (two inference labels added by me, §8).
- **Unsupported by tag**: Failures 2, 3 and 4 above.

## 5. Claims check (§9), outlook §5

Ten claims (within 6–12). Each is one sentence with one checkable thing and a single direction; every quotation was verified verbatim against the tagged page.

| # | Checkable thing | Direction | Quote verbatim | Notes |
|---|---|---|---|---|
| 1 | Q3 revenue ≥ $12.86B | single | yes (p.2, p.1) | headline |
| 2 | Q3 operating margin ≥ 33.2% | single | yes (p.2) | headline |
| 3 | Q3 UCAN growth ≥ 10% | single | yes (p.2) | labelled as the writer's sharpening |
| 4 | Q3 amortization growth < 10%, i.e. below $4.40B vs $4.00B (workbook: 4,002,744) | single | yes (Q1 letter p.2, reaffirmed in Q2 letter p.2) | labelled sharpening; names the cash-flow line and the quarter |
| 5 | FY revenue low end ≥ $51.0B in the Q3 letter | single | yes (p.2) | headline |
| 6 | 31.5% margin reaffirmed or raised | single | yes (p.2) | headline |
| 7 | FCF ~$12.5B reaffirmed or raised | single | yes (p.6) | fundamental (cash) |
| 8 | ~$3B ads reaffirmed or raised | single | yes (p.5) | fundamental (growth engine) |
| 9 | Upfront reported closed | single (silence = miss) | yes (p.5) | fundamental |
| 10 | New debt issued to refinance the $1B notes by the Q3 report | single | yes (p.6) | fundamental; names the 10-Q line |

No either/or constructions; no claim that cannot fail; no disclosure checks are used, so no quarter/YTD label is needed there. Four of ten are headline revenue or margin claims and none is EPS, so the list is not dominated by headlines. Claim 4 rests on a Q1-letter phrase ("mid-to-high single digit") that the Q2 letter softened to "grow slower in the second half"; the claim tags both letters and labels the number as the writer's, which is acceptable.

## 6. Indicators check (§8)

Eight indicators in business.md §8 (within 5–8); the section is marked `_Proposed — owner to review and lock._`; outlook §1 has exactly eight rows in the same order. Each names its source. Anchoring to a recurring disclosure: indicators 1, 2, 3, 4, 7 and 8 are lines that appear in every letter, workbook or 10-Q. Indicator 5 (the annual ad-revenue statement) is commentary, as the writer says; it has appeared in every letter since 2025 but is not a reported line. Indicator 6 (view hours) will be published annually from 2027 (letter p.5), so most quarters will read "no update", which the writer discloses. Both are honest and useful, but the owner should decide at lock time whether to keep 6 as an indicator or move it to an annual claim, per §8's preference for quarterly-recurring lines.

## 7. Skeleton and as-of check

- business.md headings: 1–8, Glossary, Sources, all present and in order; header lines `# Netflix, Inc. — The Business` and `_As of Q2 2026. Written 2026-09-08._` exact.
- outlook.md headings: 1–5 and Sources, in order; no Tone shift section (correct for a first run); header `_Transcript source tier: company-published (...). Written 2026-09-08._` follows the §7 form.
- Tags: 158 tag instances in business.md across 20 tag families and 76 in outlook.md across 7; every family appears in the file's Sources list and maps to an existing file in `sources/2026-Q2/`. One Sources entry in business.md (`[Q2 2026 financials xlsx, <sheet>]`) is listed but not used as a tag; harmless, and §8 names the workbook by sheet.
- As-of: no information dated after 2026-07-17. The only later dates are forward-looking references from the sources themselves (the $1B maturity in November 2026; "by the Q3 2026 report" as a claim horizon). The Hastings and Hoag items are dated June 4–5, 2026.
- Emojis: none in either file.
- Length after my edits: business.md 2,546 (target 2,000–3,000); outlook.md 989 (target 800–1,200).

## 8. Direct fixes made (before → after)

business.md:
1. §4: `"was recognized in "interest and other income"" in Q1` → `"was recognized in 'interest and other income'" in Q1` (nested double quotes).
2. §2: `and strips out hedging, as with LATAM` → `and strips out hedging (currency contracts that offset exchange-rate moves), as with LATAM`.
3. §3: `Netflix's own Open Connect network,` → `Netflix's own Open Connect server network,`.
4. §4: `... due between 2026 and 2054", with $1 billion` → `... due between 2026 and 2054" (twelve separate bond issues), with $1 billion`.
5. §4: `net debt was $5.2 billion` → `net debt (debt less cash) was $5.2 billion`.
6. §4: `less tax at the 13.7% effective rate is` → `less tax at the 13.7% effective rate (tax actually charged as a share of pre-tax profit) is`.
7. §4: `so the true figure is lower.` → `so the true figure is lower (our inference).`
8. §3: `roughly the $16 billion a year it amortizes.` → `roughly the $16 billion a year it amortizes (our inference).`
9. §6: `US guild contracts expired in 2026;` → `the US guild (writers', actors' and directors' union) contracts "each expire in 2026";` (gloss, and wording aligned to the 10-K quotation).
10. §6: `compares with linear TV's "over 40%"` → `compares with linear (traditional scheduled) TV's "over 40%"`.
11. §7: `"approximately $72.0 billion" of equity value, with "up to $59,000,000,000" of bridge loans;` → `"approximately $72.0 billion" of equity value (the price for all the shares), with "up to $59,000,000,000" of bridge loans (short-term bank loans meant to be replaced by bonds);`.
12. §4: `"approximately $85 million" of accelerated financing costs in Q1 interest expense` → `"approximately $85 million" of loan-arrangement fees written off in Q1 interest expense when the Warner Bros. financing ended`.
13. §8: `remaining authorization, diluted weighted-average shares.**` → `remaining authorization, diluted weighted-average shares (the share count used for earnings per share).**`.

outlook.md:
14. §3: `"over-index on viewing during the day and on mobile", so "incremental"` → `"over-index on viewing during the day and on mobile" (take a bigger share of viewing than average), so "incremental"`.

Word counts after the fixes: 2,546 and 989.

## 9. Verdict: REVISE

The report is well built: every table number in §2, §3, §4 and §7 and every outlook §1 cell reconciles to the filing, letter or workbook text; every guidance quotation is verbatim; the skeleton, tags and as-of discipline are clean; the claims are sharp and single-direction; the prose is readable. Four factual items must go back to the writer; each is a one-line change.

1. **§7 buybacks table, "Authorization remaining, period end":** replace "n/d" for FY2022 with **4.4** [10-K FY2022, Item 7] ("As of December 31, 2022, $4.4 billion remains available for repurchases") and for FY2023 with **8.4** [10-K FY2023, Item 7] ("As of December 31, 2023, $8.4 billion remains available for repurchases"). For FY2021 either keep "n/d" or write "4.4 (inferred: no 2022 repurchases)" citing the same FY2022 sentence. Add the two tags to the table's Sources line.
2. **§4, sentence "It was far below net income in 2021–2022, when cash content spend ran at 1.2–1.45 times amortization (§3); since 2023 it has run at roughly 80–90% of net income [10-K FY2025, Note 11]."** 2023 was 1.28 times net income, not 80–90%. Change "since 2023 it has run at roughly 80–90% of net income" to "in 2024 and 2025 it ran at roughly 80–90% of net income (computed from the table above)" (or equivalent) and drop the Note 11 tag, which is the income-tax note and does not support the sentence.
3. **§7, sentence ending "... the financing ended and Netflix paid nothing [8-K 2026-02-27, Item 1.02]."** The 8-K says only that the financing commitments "were each automatically terminated". Replace "Netflix paid nothing" with what the sources support, for example: "the financing commitments were terminated and no fee was owed by Netflix (its $5.8 billion fee applied only to a regulatory block) [8-K 2026-02-27, Item 1.02] [8-K 2025-12-05, Item 1.01]". Note the report's own §4 records ~$85 million of financing costs written off, so "paid nothing" also contradicts §4.
4. **§7, sentence "In October 2025 the board doubled cash severance outside a change in control to "two times the sum of" salary and target bonus and added retirement vesting, citing only market practice [8-K 2025-11-04, Item 5.02] [DEF 14A 2026, Compensation Discussion and Analysis]."** Neither source gives a rationale. Replace "citing only market practice" with "without giving a reason" (or delete the clause).

Owner note (not a REVISE item): at lock time, decide whether indicator 6 (view hours, now annual from 2027) stays an indicator or becomes an annual claim (§8).

---

# Cycle 2 (2026-09-08): verification of the four REVISE items

The writer edited `business.md` only; `outlook.md` is byte-identical to the cycle-1 file after my glosses (md5 4a32ff82…). Each edit was checked against the cached source text with full lines printed.

## Per-item results

| # | Item | Result | Evidence |
|---|---|---|---|
| 1 | §7 buybacks table, "Authorization remaining, period end" now `4.4 (inference: no 2022 repurchases) \| 4.4 \| 8.4 \| 17.1 \| 8.0 \| 27.1`; tags [10-K FY2022, Item 7] [10-K FY2023, Item 7] added to the table's Sources line | **Pass** | 10-K FY2022 line 938 (inside Item 7, which runs lines 715–1059): "As of December 31, 2022, $4.4 billion remains available for repurchases." 10-K FY2023 line 861 (inside Item 7, lines 649–960): "As of December 31, 2023, $8.4 billion remains available for repurchases." The FY2021 cell is labelled as an inference and rests on 10-K FY2022's "There were no repurchases during the year ended December 31, 2022" (Item 5 line 697; Note line 2136). FY2024–6M 2026 cells unchanged and previously verified. |
| 2 | §4: "...and above it in the 2023 strike year (§3); in 2024, 2025 and the first half of 2026 it ran at roughly 75–90% of net income (computed from the table)." Note 11 tag dropped | **Pass** | Recomputed from the §4 table inputs: 2023 6,925,749 / 5,407,990 = 1.28 (above); 2024 6,921,826 / 8,711,631 = 0.795; 2025 9,461,053 / 10,981,201 = 0.862; 6M 2026 6,619,243 / 8,684,205 = 0.762. "Roughly 75–90%" covers 76–86%. The computation label replaces the unsupported tag. |
| 3 | §7 WBD: Paramount Skydance "on behalf of WBD, paid the $2,800,000,000 termination fee" and the financing commitments "were each automatically terminated" [8-K 2026-02-27, Item 1.02]. "Netflix owed no termination fee, because its $5.8 billion fee applied only to a regulatory block [8-K 2025-12-05, Item 1.01]; its only cost was the financing expense already booked (§4) [10-Q Q2 2026, Item 2] [Q4 2025 letter, p.2]." | **Pass** | Both fragments occur verbatim in 8-K 2026-02-27 (lines 42–43). 8-K 2025-12-05 line 125, the only Netflix-payable fee in the filing: "Netflix will pay WBD a termination fee of $5,800,000,000 if the Merger Agreement is not consummated under certain circumstances relating to the failure to obtain approvals, or there is a final, non-appealable order preventing the transaction, in each case, relating to antitrust laws or foreign regulatory laws." Lines 103 and 123 describe only WBD's $2.8B fee. Supports for "financing expense already booked": 10-Q Item 2 "approximately $85 million recognized in connection with the termination of financing arrangements associated with the WBD transaction in the first quarter of 2026"; Q4 2025 letter p.2 "Net income included ~$60M of costs (booked in interest expense) related to our recent Warner Bros.-related bridge loan". |
| 4 | §7 severance: "without giving a reason" replaces "citing only market practice" | **Pass** | Consistent with 8-K 2025-11-04 Item 5.02 (terms only) and the proxy's "Amended and Restated Executive Officer Severance Plan" section (no rationale); gatherer notes list the rationale as not found. |

## Other checks repeated

- No other sentence changed: §4 (lines 86–94) and §7 (lines 120–146) re-read; the cycle-1 glosses and all other text are intact; file remains 191 lines. The only additions are the four edits above.
- Tags: 162 tag instances in business.md (was 158); every tag family maps to a listed Sources entry and an existing cached file. Changes match the edits exactly: 10-K FY2025 48 → 47 (Note 11 tag dropped), 8-K 2025-12-05 1 → 2, 10-K FY2022 6 → 7, 10-K FY2023 11 → 12, 10-Q Q2 2026 19 → 20, Q4 2025 letter 10 → 11. outlook.md unchanged (76 instances, all mapped).
- Skeleton, header lines, `_Proposed — owner to review and lock._` marker, no Tone shift, no emojis, no post-cutoff information: all unchanged and passing.
- Length (`python3 -P /tmp/nflx-orch/wc_prose.py`): business.md **2,592** (target 2,000–3,000); outlook.md **989** (800–1,200). Both inside range.
- No direct fixes were needed in cycle 2.

## Final verdict: PASS

All four cycle-1 failures are resolved with sourced wording; no new failures; numbers, tags, skeleton, claims and length all pass. The report is ready to commit. Owner note carried forward from cycle 1: at lock time, decide whether indicator 6 (view hours, annual from 2027) stays an indicator or becomes an annual claim.
