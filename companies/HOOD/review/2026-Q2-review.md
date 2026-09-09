# Robinhood Markets, Inc. (HOOD) — Reviewer report, 2026-Q2

_Reviewed 2026-09-09 against `companies/HOOD/sources/2026-Q2/` only (cached full texts; `notes-*.md` not opened, since no error traced to a note was needed). As-of cutoff 2026-07-30; nothing dated later was consulted; `transcript-motleyfool.txt` was excluded from every search. Line numbers refer to the cached `.txt` files. Page maps used: `transcript.txt` printed page N ends at l.48, 96, 144, 191, 239, 286, 333, 381, 428, 474, 522, 569, 617, 663, 711, 759, 807, 855, 902, 950, 997, 1045, 1092, 1140, 1188, 1236, 1283, 1330, 1368 for N = 1..29. `press-release.txt` p.1 = l.1–31, p.2 = 32–49, p.3 = 50–60, p.4 = 61–73, p.11 = 290–323, p.12 = 324–339. `press-release-2026-Q1.txt` p.1 = 1–29, p.2 = 30–55, p.3 = 56–68. `slides.txt` (Nth form-feed block) p.3 = 71–123, p.4 = 124–172, p.9 = 369–429, p.10 = 430–464, p.13 = 549–587, p.16 = 674–708, p.18 = 748–785, p.19 = 786–827, p.29 = 1146–1188, p.32 = 1251–1290, p.33 = 1291–1328, p.34 = 1329–1365, p.37 = 1417–1456, p.39 = 1504–1552, p.42 = 1638–1674, p.43 = 1675–1731, p.45 = 1777–1812. Word counts by `python3 -P /tmp/hood-orch/wc_prose.py`._

**Verdict: REVISE** (one pass expected). Every number in the business.md §2, §3 and §4 tables, the concentration table and the §7 table verifies, as does every number in outlook §1 and every verbatim quote in outlook §4 and §5. What fails: one mis-sourced and mis-described outage date (August 2024), one over-attributed gain ($129M "from deconsolidating"), one superseded acquisition price (TradePMR), one unlabelled computation that disagrees with the slides ($799M vs ~$761M), one overstated co-defendant sentence, one risk over-extended to Robinhood Chain, one restructuring charge that omits its stock-pay half, one "not stated" that the slides do state (Gold's $5 a month), one double-barreled claim, and indicator row labels that do not match §8 verbatim. Both files are inside the length ranges after my glosses (outlook.md is 58 words under its ceiling).

---

## 1. Skeleton compliance

**business.md**

| Requirement (§6) | Status |
|---|---|
| `# <Company> — The Business` | OK (`# Robinhood Markets, Inc. — The Business`) |
| `_As of <QLABEL>. Written <date>._` | OK (`_As of Q2 2026. Written 2026-09-09._`; fiscal = calendar, no parenthetical needed) |
| §1 What they do, with a short history paragraph | OK (history at l.10) |
| §2 How the money comes in, 5-year segment table | OK. One segment; a revenue-by-line table FY2021–FY2025 + Q2 2026 (l.16–33) plus a market-maker concentration table (l.41–45); definition changes footnoted (event contracts line from 2026; segregated-cash line net of user interest from 2026; Bitstamp/WonderFi inclusion) |
| §3 The economics, table with revenue / GM / OM / capex / capex-to-revenue | OK; gross margin given as a labelled proxy (no gross profit reported), operating margin labelled computed, plus Adjusted EBITDA margin and SBC/revenue rows |
| §4 How profitable, really, 5-year table | OK (OCF, capex, FCF, net income, Adjusted EBITDA, cash taxes, buybacks, tax withholding) |
| §5 Why customers don't leave | OK; inference labelled at l.96; each source of stickiness has a weakening sign |
| §6 What could break it, ranked, concentration | OK; seven scenarios ranked, each with early warning; concentration paragraph at l.126 |
| §7 Who runs it and what they do with the cash | OK, with a capital-allocation table (l.138–147); dual-class control at l.132 |
| §8 Indicators (5–8; name / why / where) | OK, 8 indicators, each with a source location |
| `_Proposed — owner to review and lock._` | OK (l.162) |
| Glossary (one sentence each) | OK, 11 entries, each one sentence. Judgment call for the owner: "Adjusted EBITDA", "Adjusted Operating Expenses and SBC" and "Convertible notes and capped call" are finance terms rather than business terms; §3 rule 4 says only the very important ones belong here |
| Sources list maps every tag family used | OK. Families used (18): 10-K FY2025, 10-K FY2024, 10-K FY2023, 10-K FY2022, 10-Q Q2 2026, DEF 14A 2026, 8-K 2025-11-05, 8-K 2026-02-10, 8-K 2026-03-24, 8-K/A 2026-03-24, 8-K 2026-06-16, 8-K 2026-06-23, 8-K 2026-06-25, Q2 2026 release, Q2 2026 slides, Q2 2026 supplement, June 2026 metrics, Q2 2026 call. All 18 listed with dates that match MANIFEST (10-K/A 2026-02-20 standing in for the 10-K of 2026-02-18, stated; FY2024 2025-02-18; FY2023 2024-02-27; FY2022 2023-02-27; 10-Q 2026-07-30; DEF 14A 2026-04-22 for the 2026-06-02 meeting; 8-K dates; release/slides/supplement/metrics 2026-07-29; transcript tier 1, printed pages = PDF pages) |
| Heading order | OK |

**outlook.md**

| Requirement (§7) | Status |
|---|---|
| `# <Company> — Outlook as of <QLABEL>` | OK |
| `_Transcript source tier: ... Written <date>._` | OK (`company-published`, matches MANIFEST tier 1) |
| §1 one row per indicator; this quarter / last quarter / expected | OK on structure: 8 rows in the same order as business.md §8, columns Q2 2026 / Q1 2026 / what management had said; header says the set is proposed, not yet locked. Row labels are not the §8 names verbatim (REVISE item 10) |
| §2 What management says | OK |
| §3 Growth engines (what / how big / claim / working-or-not) | OK, seven engines, each with a "Working if" line |
| §4 Guidance, verbatim | OK, four bullets, all verbatim (checked below); the p.17–18 speaker-label problem is stated |
| §5 Claims to verify | OK, 11 claims (target 6–12) |
| §6 Tone shift | Correctly omitted (first run) |
| Sources | OK, all 8 families used (Q2 call, Q2 release, Q2 slides, Q2 supplement, Q1 release, 10-Q Q2, 10-Q Q1, 10-K FY2025) are listed with dates |
| Valuation, price, multiples | None anywhere in either file (the $300, $174.42, $237.85, $105.71 figures are the terms of the convertible notes, not a valuation) |

---

## 2. Rubric (§14)

| # | Question | Answer | Reasoning |
|---|---|---|---|
| 1 | Two sentences on what they do and who pays | Yes | §1 l.6–8: an app where retail investors trade and bank; market makers pay for orders, customers pay interest, Gold fees and commissions, banks pay a spread on swept cash. |
| 2 | What would kill it and the early warning | Yes | §6 ranks seven scenarios (PFOF ban, rate cuts, crypto, prediction-market restrictions, a 2022-style downturn, operational/regulatory failure, competition), each with an early-warning line; interest-rate and crypto exposure are quantified from filings. |
| 3 | Why margins are what they are; does cost scale with usage | Yes | §3: only "Brokerage and transaction" (5% of revenue) moves with volume; the rest is people and cloud; 2022 loss vs 60% incremental margin in Q2 2026; capex 1–2% of revenue but large regulatory and customer-funding balances must be held. |
| 4 | Predict next quarter's scorecard from §5 alone | Yes, with one fix | 11 claims, each tied to a number, date or event; claim 4 bundles two metrics (REVISE item 9). |
| 5 | Nothing required outside knowledge | Yes, after glosses | Options, futures, clearinghouse, collateral, segregated cash, short sellers, IRA, proxy, selling concessions, incremental margin, capex, unamortised, tick size, Rule 605, basis point, FINRA, contingency accrual, accordion, deconsolidated, ARR, run-rate, trailing, DCM, DEX, stock tokens, Earn, Arbitrum, Legend, Strategies, Agentic Trading, notional, SBC, H1 were glossed directly (see §9). |

---

## 3. Citation spot-check

Legend: PASS = found in the tagged source at the line shown; FAIL = not there, or tag points elsewhere. Computed cells re-derived from sourced inputs.

### 3(a) business.md §2 revenue-by-line table (l.16–33), every cell

Inputs: `10-K-FY2023.txt` l.2030–2034 (transaction lines FY2021–FY2023), l.2059–2066 (net interest lines), l.1984–1986 (totals); `10-K-FY2025.txt` l.2422–2426 (transaction FY2024–FY2025), l.2445–2453 (net interest), l.2376–2378 (totals); `10-Q-2026-Q2.txt` l.905–930 (Note 6, three months ended June 30, 2026).

| Row | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | Q2 2026 | Result |
|---|---|---|---|---|---|---|---|
| Options | 690 | 488 | 505 | 760 | 1,123 | 342 | PASS ×6 |
| Cryptocurrencies | 420 | 202 | 135 | 626 | 901 | 100 | PASS ×6 |
| Equities | 287 | 117 | 104 | 177 | 302 | 129 | PASS ×6 |
| Event contracts | in Other ×5 | | | | | 156 | PASS (Q2 l.914; "in Other" consistent with `10-K-FY2025` l.2428: other transaction revenue "primarily driven by increased user activities in Prediction Markets and instant withdrawals") |
| Other transaction-based | 5 | 7 | 41 | 84 | 302 | 49 | PASS ×6 |
| Transaction-based revenues | 1,402 | 814 | 785 | 1,647 | 2,628 | 776 | PASS ×6 |
| Margin interest | 132 | 177 | 243 | 319 | 573 | 215 | PASS ×6 |
| Cash Sweep | 3 | 22 | 123 | 179 | 229 | 41 | PASS ×6 |
| Interest on segregated cash and deposits | 4 | 57 | 210 | 261 | 319 | 60 | PASS ×6; footnote ² ($57M interest paid to users, net from 2026) at `10-Q` l.940 |
| Interest on corporate cash | 1 | 103 | 288 | 256 | 167 | 31 | PASS ×6 |
| Securities lending, net | 136 | 89 | 79 | 94 | 190 | 10 | PASS ×6 |
| Credit card, net | — | — | 9 | 24 | 64 | 40 | PASS ×6 |
| Credit-facility interest and other | (20) | (24) | (23) | (24) | (28) | (8) | PASS ×6: (20)/(24)/(23) l.2065; (24) l.2451; FY2025 (32) + 4 other = (28); Q2 (10) + 2 = (8) |
| Net interest revenues | 256 | 424 | 929 | 1,109 | 1,514 | 389 | PASS ×6 |
| Other revenues | 157 | 120 | 151 | 195 | 331 | 143 | PASS ×6 |
| Total net revenues | 1,815 | 1,358 | 1,865 | 2,951 | 4,473 | 1,308 | PASS ×6 |

96/96 PASS. Footnote: Bitstamp from June 2025 and WonderFi from June 2026, `earnings-supplement-2026-Q2.txt` l.129, l.170–172. PASS.

### 3(b) business.md §2 concentration table (l.41–45), every cell

| Row | Source | Result |
|---|---|---|
| Citadel 22% / 16% / 12% / 12% / 13% / 16% | `10-K-FY2023` l.2875; `10-K-FY2025` l.3298; `10-Q` l.686 (three months ended June 30, 2026) | PASS ×6 |
| Other names above 10%: FY2021 Tai Mo Shan 15%, Susquehanna 12%, Wolverine 10%; FY2022 none; FY2023 none; FY2024 Wintermute 10%; FY2025 none; Q2 2026 none | `10-K-FY2023` l.2876–2878 (Wolverine 10/8/6, Susquehanna 12/8/2, Tai Mo Shan 15/3/1); `10-K-FY2025` l.3299 (Wintermute 2/10/6); `10-Q` l.686–688 (only Citadel) | PASS ×6 |
| All market makers and exchanges 77% / 59% / 40% / 56% / 55% / 47% | `10-K-FY2023` l.2880; `10-K-FY2025` l.3301; `10-Q` l.688 | PASS ×6 |

18/18 PASS. Header wording: the FY2023 10-K says "market makers" and "total revenues", the FY2025 10-K and 10-Q say "market makers and exchanges" and "total net revenues"; the draft's header uses the current wording. Acceptable.

### 3(c) business.md §3 table (l.57–65), every cell

Inputs: `10-K-FY2023.txt` l.1988–1993 (expenses FY2021–FY2023), l.1912 (Adjusted EBITDA 33 / (94) / 536), l.2671 (SBC 1,572 / 654 / 871), l.2688–2689 (capex 63+20 / 28+29 / 2+19); `10-K-FY2025.txt` l.2380–2386 (expenses FY2024–FY2025), l.2296 (Adjusted EBITDA 1,429 / 2,522), l.3067 (SBC 304 / 305), l.3084–3085 (capex 13+37 / 15+39); `10-Q-2026-Q2.txt` l.414–420 (H1 expenses), l.479 (SBC 197), l.498–499 (capex 21+21), l.1722 (Adjusted EBITDA 1,275); `press-release.txt` l.309 (1,275); `DEF14A-2026.txt` l.2248–2252 (Adjusted EBITDA 33 / (94) / 536 / 1,429 / 2,522 in Pay Versus Performance).

| Row | Re-derived | Result |
|---|---|---|
| Revenue 1,815 / 1,358 / 1,865 / 2,951 / 4,473 / 2,375 | as 3(a); H1 `10-Q` l.930 | PASS ×6 |
| Gross-margin proxy 91 / 87 / 92 / 94 / 95 / 95% | 1 − 158/1,815 = 91.3; 1 − 179/1,358 = 86.8; 1 − 146/1,865 = 92.2; 1 − 164/2,951 = 94.4; 1 − 211/4,473 = 95.3; 1 − 122/2,375 = 94.9 | PASS ×6 |
| Operating margin (90) / (74) / (29) / 36 / 47 / 41% | (1,815−3,456)/1,815 = −90.4; (1,358−2,369)/1,358 = −74.4; (1,865−2,401)/1,865 = −28.7; (2,951−1,897)/2,951 = 35.7; (4,473−2,379)/4,473 = 46.8; (2,375−1,390)/2,375 = 41.5 | PASS ×6 |
| Adjusted EBITDA margin 2 / (7) / 29 / 48 / 56 / 54% | 33/1,815 = 1.8; −94/1,358 = −6.9; 536/1,865 = 28.7; 1,429/2,951 = 48.4; 2,522/4,473 = 56.4; 1,275/2,375 = 53.7 | PASS ×6 |
| SBC / revenue 87 / 48 / 47 / 10 / 7 / 8% | 1,572/1,815 = 86.6; 654/1,358 = 48.2; 871/1,865 = 46.7; 304/2,951 = 10.3; 305/4,473 = 6.8; 197/2,375 = 8.3 | PASS ×6 |
| Capex 83 / 57 / 21 / 50 / 54 / 42 | 63+20; 28+29; 2+19; 13+37; 15+39; 21+21 | PASS ×6 |
| Capex / revenue 4.6 / 4.2 / 1.1 / 1.7 / 1.2 / 1.8% | 4.57; 4.20; 1.13; 1.69; 1.21; 1.77 | PASS ×6 |
| Footnote ³ $1.01 billion IPO SBC; ⁴ $485 million founders' award cancellation | `10-K-FY2023` l.2013 (Item 7: "Upon our IPO in 2021, we recognized $1.01 billion of SBC expense. In 2023, we recognized $485 million ...") | PASS ×2 |

44/44 PASS. Prose l.55: brokerage and transaction 5% of FY2025 revenue (`10-K-FY2025` l.2525), technology and development 20% (l.2541), operations 3% (l.2552), credit losses 3% (l.2562), marketing 9% (l.2578), G&A 14% (l.2590): PASS ×6, all stated in the 10-K. "a large portion ... are variable and tied to trading and transaction volumes" l.2342: PASS. Revenue fell 25% in 2022 (computed): (1,358−1,815)/1,815 = −25.2%: PASS. Incremental Adjusted EBITDA margin 60%: `slides` p.45 l.1803: PASS.

### 3(d) business.md §4 table (l.75–84), every cell

Inputs: `10-K-FY2023.txt` l.2686 (OCF (885) / (852) / 1,181), l.1899 (net loss), l.2721 (cash taxes 6 / 4 / 9), l.2707 (repurchase 608), l.2700 (tax withholding 422 / 12 / 12); `10-K-FY2025.txt` l.3082 (OCF (157) / 1,638), l.3013 (net income 1,411 / 1,883), l.3129 (taxes 18 / 95), l.3099 (repurchases 257 / 653), l.3098 (withholding 244 / 437); `10-Q-2026-Q2.txt` l.496 (OCF 2,758), l.424 (net income 919), l.548 (taxes 171), l.515 (repurchases 664), l.514 (withholding 23).

| Row | Re-derived | Result |
|---|---|---|
| OCF (885) / (852) / 1,181 / (157) / 1,638 / 2,758 | direct | PASS ×6 |
| Capex (83) / (57) / (21) / (50) / (54) / (42) | as 3(c) | PASS ×6 |
| FCF (968) / (909) / 1,160 / (207) / 1,584 / 2,716 | −885−83; −852−57; 1,181−21; −157−50; 1,638−54; 2,758−42 | PASS ×6 |
| Net income (3,687) / (1,028) / (541) / 1,411 / 1,883 / 919 | direct | PASS ×6 |
| Adjusted EBITDA 33 / (94) / 536 / 1,429 / 2,522 / 1,275 | as 3(c) | PASS ×6 |
| Cash paid for income taxes 6 / 4 / 9 / 18 / 95 / 171 | direct | PASS ×6 |
| Share repurchases — / — / 608 / 257 / 653 / 664 | direct | PASS ×6 |
| Taxes paid on vesting shares 422 / 12 / 12 / 244 / 437 / 23 | direct | PASS ×6 |
| Footnote ⁵ $2,045M convertible-note charge; $1.01B IPO SBC | `10-K-FY2023` l.1911 (change in fair value of convertible notes and warrant liability 2,045), l.2013 | PASS ×2 |
| Footnote ⁶ $485M | `10-K-FY2025` Note 12 l.4391 | PASS |
| Footnote ⁷ $347M tax benefit | `10-K-FY2025` l.3012 (benefit from income taxes (347) for 2024) | PASS |
| Footnote ⁸ "$129 million of gains from deconsolidating Robinhood Ventures Fund I" | `press-release` l.16: "$129 million of gains **primarily related to** the deconsolidation of RVI"; p.11 l.307–312: $106M deconsolidation gain + $23M "unrealized and realized gains in equity securities ... primarily related to investments held by RVI" | Number PASS, description overstated — REVISE item 2 |

50/50 numbers PASS; one description flagged. Prose l.88: receivables from users grew $4,592M in FY2024 (`10-K-FY2025` l.3072); H1 2025 OCF $4,151M (`10-Q` l.496); Adjusted EBITDA less SBC 2,522 − 305 = 2,217 ≈ $2.2B (labelled computed): PASS ×3. l.90: valuation allowance release and "sustained profitability" (`10-K-FY2024` l.2439, l.3958; total benefit $347M l.2437): PASS; 35.5 million shares, "No other payments, replacement equity awards or benefits were granted" (`10-K-FY2025` l.4391): PASS ×2. l.92: equity $9,541M, cash $5,362M, total assets $56,550M (`10-Q` l.391, l.354, l.369); ROE 1,883/((7,972+9,151)/2) = 22.0% (`10-K-FY2025` l.2982): PASS ×4.

### 3(e) business.md §7 table (l.138–147)

| Cell | Source | Result |
|---|---|---|
| Say Technologies $133M, Aug 2021 | `10-K-FY2022` Note 3 l.3094 ff. ("$133 million ... Cash $132 ... Total consideration $133"; August 13, 2021) | PASS |
| X1 $104M, Jul 2023 | `10-K-FY2023` Note 3 l.3213–3215 | PASS |
| U.S. Marshals 55.3M shares at $10.96, $608M, Aug 2023 | `10-K-FY2023` Note 14 (heading l.3792; text l.3840: 55,273,469 shares, $10.96, $608 million, closed August 31, 2023) | PASS ×3; the `[10-K FY2023, Note 14]` tag the writer flagged is correct |
| $1.0B (May 2024) → $1.5B (Apr 2025) → new $1.5B (Mar 2026, "approximately three years"); $1,373M left | `10-K-FY2025` l.1983 / l.2142 (Item 5); `8-K-2026-03-24` l.71; `10-Q` Part II Item 2 l.3607–3608 ($1,373) | PASS ×4; the $1,373M is in Part II Item 2, not Note 12 — tag corrected (direct fix) |
| Cash on buybacks $257M → $653M → $664M (incl. $290M outside the program) | as 3(d); `8-K-2026-06-25` l.111 ($290 million, 2,743,000 shares at $105.71) | PASS ×4 |
| TradePMR ~$175M | `10-K-FY2025` l.2119 / l.3613 ("approximately $175 million"); but `10-Q` Note 3 l.724: "approximately $169 million following customary purchase price adjustments", allocation finalised in Q1 2026 | FAIL (superseded) — REVISE item 3 |
| Bitstamp ~$224M (Jun 2025); MIAXdx ~$79M (Jan 2026); WonderFi ~$178M (Jun 2026) | `10-Q` l.751; l.~790 ("approximately $79 million in cash", closed January 20, 2026); l.~820 ("approximately $178 million ... entirely paid in cash", June 1, 2026) | PASS ×3 |
| Convertible notes $2.2B, 0%, due Oct 2029; ~$174.42 (65% premium); capped calls $123M; cap $237.85 | `10-Q` Note 11 l.1203, l.1225, l.1239 ($123.2 million), l.1243 ($237.8475); `8-K-2026-06-25` l.59–67, l.83 | PASS ×5 |
| Credit lines $3.25B RHS 364-day, expandable to $4.875B; $1.0B parent to Mar 2028 | `8-K-2026-03-24` l.59; `10-Q` l.1253 (maturity March 21, 2028), l.1259 | PASS ×3 |
| Shares outstanding 863.9M → 892.8M → 872.2M → 884.5M → 901.3M → 899.0M | `10-K-FY2022` l.2521–2522 (735,957,367 + 127,955,246; 764,888,917 + 127,862,654); `10-K-FY2023` l.2584–2585 (745,401,862 + 126,760,802); `10-K-FY2025` l.2975–2976 (764,903,997 + 119,588,986; 790,331,696 + 110,996,736); `slides` p.42 l.1652 (899.0) | PASS ×6; end-2023 figure needed the FY2023 10-K — tag added (direct fix) |

Prose l.149: "roughly flat" `slides` p.19 l.788–789; "$300" `transcript` l.203–204 (p.5); $106M `10-Q` Note 4 l.853: PASS ×3.

### 3(f) outlook.md §1 indicator table (l.10–17), every number

| Cell | Source | Result |
|---|---|---|
| Net Deposits $21.7B; 28% — Q1 $17.7B; 22% | `press-release` l.25; `press-release-2026-Q1` l.23 | PASS ×4 |
| "even with tax season, net deposits are approximately $5 billion month-to-date" | Q1 release l.9 (p.1) | PASS |
| Funded Customers 28.4M; +0.9 / +0.2 / +0.3 / (0.4) — Q1 27.4M; +0.7 / +0.1 / — / (0.4) | `press-release` l.22; Q1 l.20; `slides` p.29 l.1156–1162 | PASS ×10 |
| "we said last quarter we were making a concerted effort to regrow top of funnel" | `transcript` l.489 (p.11, CFO) | PASS |
| Total Platform Assets $368.7B — Q1 $307B | release l.24 says "$369 billion"; the decimal is at `slides` p.29 l.1182 and `earnings-supplement` l.98; Q1 l.22 | PASS ×2; slides tag added (direct fix) |
| Gold 4.84M; 17.0% — Q1 4.34M; 15.8% | `slides` p.9 l.383 (4.84M), l.386–387 (15.8%, 17.0%), p.9 chart l.378 (4.34); release l.26 (4.8 million), l.43 (17 percent); Q1 l.24 (4.3 million) | PASS ×4 |
| Transaction revenue $342M / $129M / $100M / $156M — Q1 $260M / $82M / $134M / $104M | release l.12; Q1 l.12; supplement l.11 (Event Contracts Q1'26 = 104) | PASS ×8 |
| "equity and option trading volumes are on track to be the highest month of the year" | Q1 l.9 | PASS |
| NII $389M; Margin Book $21.6B; Cash Sweep $29.7B — Q1 $359M; $17.0B; $26.0B | release l.13, l.52, l.54 (p.3); Q1 l.13, l.47, l.49 (p.2) | PASS ×6 |
| Adj OpEx and SBC $641M (H1 $1,248M); "$2.675 to $2.775 billion" — Q1 $607M; "$2.7 billion to $2.825 billion" | release l.20, l.338 (p.12: $522 / $641 / $607 / $1,055 / $1,248), l.65; Q1 l.18, l.60 | PASS ×5; the H1 sum is on p.12, not p.11 — tag corrected (direct fix) |
| "did not include costs related to Rothera and WonderFi" | release l.65 | PASS |
| Citadel 16%; 47% — Q1 15%; 48% | `10-Q` l.686–688; `10-Q-2026-Q1` l.623, l.630 | PASS ×4 |

46/46 PASS.

### 3(g) Verbatim quotes, outlook.md §4 and §5, word for word (curly quotes and whitespace normalised; also run programmatically against every cached text)

| Quote (start) | Tag | Lines | Result |
|---|---|---|---|
| "we are lowering and tightening our 2026 outlook for Adjusted Operating Expenses and SBC to a range of $2.675 to $2.775 billion to reflect efficiencies we have captured, part of which were used to fund costs related to two new businesses, Rothera and WonderFi." | release p.4 | l.65 | PASS |
| "$2.7 billion to $2.825 billion"; "did not include costs related to Rothera and WonderFi" | release p.4 | l.65 | PASS ×2 |
| "an additional $70 million of costs for two new businesses" | slides p.18 | l.765 | PASS (the $110M of efficiencies is the chart label at l.760) |
| "we anticipate diluted share count will be roughly flat in 2026 as well" | slides p.19 | l.788–789 | PASS |
| "July average daily volumes, compared to a record Q2, are in a similar area for equities, options, and event contracts. And July Net Deposits are tracking towards the $4 billion area - and this does not yet include deposits into the Trump Accounts." | call p.5 | l.208–211 | PASS |
| "In terms of crypto, it's probably a little bit slower than what we saw in Q2"; "in a similar area to what we saw for the Q2 average." | call p.26 | l.1211–1212; l.1214 | PASS ×2 |
| "our goal, as we've said, is 20% on an annualized basis ... If you look at year-to-date, including July, we're still well north of that 20%" | call p.17–18 | l.800–801, l.807 (spans the p.17 footer; labelled "Vladimir Tenev" at l.798 although l.821 "As I shared, July, the average daily volumes..." continues the CFO's prepared remarks; the draft says so) | PASS |
| Claim 1 "a range of $2.675 billion to $2.775 billion" | call p.5 | l.191–192 | PASS |
| Claim 2 "over the fullness of a year or even longer, we should be growing at about 20%" | call p.18 | l.813–814 | PASS |
| Claim 3 "July Net Deposits are tracking towards the $4 billion area" | call p.5 | l.210 | PASS |
| Claim 4 "July average daily volumes, compared to a record Q2, are in a similar area" | call p.5 | l.208–209 | PASS |
| Claim 5 "In terms of crypto, it's probably a little bit slower than what we saw in Q2" | call p.26 | l.1211–1212 | PASS |
| Claim 6 "you should expect that more and more of it will start to go through there" | call p.25 | l.1152–1153 | PASS |
| Claim 7 "The goal is to get it out to everyone by the end of the quarter." | call p.9 | l.390 | PASS |
| Claim 8 "Crypto is coming soon as well." | call p.13 | l.610 | PASS |
| Claim 9 "So, on deck soon, making it so that employers can fund the Trump Accounts of their employees" | call p.10 | l.458–459 | PASS |
| Claim 10 "diluted share count will be roughly flat in 2026" | slides p.19 | l.788–789 | PASS |

22/22 PASS. Outlook §2–§3 quotes checked incidentally, all PASS: "Robinhood exists to make everyone an owner" l.75 (p.2); three arcs l.86–88; "at over a 20% growth rates" l.218–219; "has made us more than a Rule of 80 company for the past few years" l.222–223; "$100 million ARR businesses" l.227; "over $5 billion of annual revenue" l.225; "financial North Star remains the same - maximize earnings per share and free cash flow per share for shareholders over time" l.233–234; "we believe we can 10x the business over the next 10 years" l.890–891 (p.19); "has rapidly become a top three DCM" l.100–101 (p.3); "in the near- to medium-term more than the majority or a good portion will flow through Rothera" l.1150–1151 (p.25); "not yet fully integrated into the main app or the ecosystem" l.829–830 (p.18); "over 7M account sign ups with nearly $1.5 billion deposited" release l.40; "contracted on a cost plus basis with a small margin" Q1 release l.60 (p.3); "tens of millions [of children]" l.453 (p.10, brackets in the transcript itself); "a good, durable, consistent source of Net Deposits" l.831–832; "getting close" l.1065 (p.23); "over $12 billion in DEX volume" l.125; "more than 120 countries" l.136 and release l.46; "over $200 million" l.130; "a few basis points" l.1105 (p.24); "when we start to get larger and it goes through a couple of quarters" l.1108; "nearly 100 thousand customers have opened Agentic Trading accounts" release l.36; "over 100,000" l.617 (p.14).

### 3(h) Prose sentences, business.md

| # | Sentence / figure | Tag | Found | Result |
|---|---|---|---|---|
| 1 | 28.4 million Funded Customers; $369 billion | release p.1 | l.22, l.24 | PASS |
| 2 | "many of our customers have told us that Robinhood was their first brokerage account" | 10-K Item 1 | l.521 | PASS |
| 3 | "in 2013 on the belief that everyone should be welcome to participate in our financial system"; "the first U.S. retail broker to offer commission-free stock trading with no account minimums" | 10-K Item 1 | l.399; l.401 / l.2170 | PASS ×2 |
| 4 | Self-clearing since November 2018 | 10-K FY2023 Item 1A | l.1548 ("prior to our becoming self-clearing in November 2018") | PASS |
| 5 | Nasdaq listing July 29, 2021 | 10-K Item 5 | l.2105 | PASS |
| 6 | "temporarily restricted or limited its customers' purchase of certain securities, including GameStop Corp. and AMC Entertainment Holdings, Inc." (January 2021) | 10-K Note 15 | l.4584 (Note 15 begins l.4548) | PASS |
| 7 | Trump Accounts launched July 4; Robinhood Chain launched July 2026 | 10-Q Note 1; Item 1A | l.655; l.3317 | PASS ×2 |
| 8 | "route[s] these orders to market makers and we receive consideration from those market makers"; "known as PFOF"; "a fixed percentage of the difference between the publicly quoted bid and ask"; crypto rebate a fixed percentage of notional | 10-K Item 7 | l.2314 | PASS ×4 |
| 9 | "have historically given customers the best prices"; "incentive for market makers to provide better prices for our customers, in order to receive more orders in the future" | 10-K Item 1 (also tagged Note 1) | l.507 | PASS ×2 |
| 10 | $2,326M of FY2025 transaction revenue from routing to market makers | 10-K Item 8 | l.2882 (auditor's critical audit matter) | PASS |
| 11 | "perceive our PFOF practices to create a conflict of interest between us and them"; December 2020 SEC settlement; NYAG since July 2023; "outsized impact"; "are often not documented under binding contracts" | 10-K Item 1A | l.973; l.957; l.957; l.961; l.945 | PASS ×5 |
| 12 | "(amount not in the cached filings)" for the December 2020 SEC settlement | — | no dollar figure for that settlement in any cached 10-K or 10-Q (grep "65 million", "December 17, 2020" context `10-K-FY2022` l.741) | PASS (correctly stated as not in cache) |
| 13 | "The cached filings do not discuss U.K. or EU treatment of PFOF" | 10-K Item 1A | no PFOF line mentions the U.K., EU or Europe | PASS |
| 14 | Margin $21.6B at 4.52%; Cash Sweep $29.7B at 0.59%; cash and deposits $18.7B at 2.02%; card $1.5B at 11.88% | slides p.39 | l.1517, l.1525 | PASS ×8 |
| 15 | Gold "a flat recurring rate"; 3% IRA match; first $1,000 of margin interest-free; lower fees; Gold subscription revenue $179M FY2025 | 10-K Item 1; Note 5 | l.461; l.3793 | PASS ×5 |
| 16 | Gold "(price not stated in the filings)" | — | true of the 10-K/10-Q, but `slides` p.9 l.373–374: "meaningful value for $5 per month" | Disclosed in the cache — REVISE item 8 |
| 17 | $25M Trump Accounts service revenue; $63M promotional matches deducted | slides p.13; p.37 | l.584; l.1419, l.1450 | PASS ×2 |
| 18 | Net capital $3,947M vs $504M required; clearinghouse deposits $1,240M; segregated cash $12,023M; payables to users $17.2B; securities loaned $20.5B; card trust $1.55B of bank lines; $4.25B undrawn lines (computed 3.25 + 1.0) | 10-Q Item 2; Item 1; Note 11 | l.2085; l.359; l.355; l.373; l.374; l.1277; l.1253 + l.1259 | PASS ×7 |
| 19 | $2.2B 0% notes "to enhance strategic flexibility to invest for future growth" | 8-K 2026-06-23 Exhibit 99.1 | l.8 | PASS |
| 20 | Thirteen business lines at $100M+ | slides p.16 | l.687, l.704 (footnote: measured when a line crossed ~$100M in quarterly annualized revenue) | PASS; wording "each earn over $100 million a year" slightly overstates the footnote (optional item 12) |
| 21 | Flywheel quote "We get a customer in, they become a Gold Subscriber ... And then a decent chunk of their earnings - if we get the direct deposit - go into Robinhood" | call p.21 | l.958–962 | PASS |
| 22 | Gold Subscriber holds ~4.2× the assets of the average customer; Banking $3.1B from 245 thousand; Gold Card 1 million; "approximately 40 percent" of new customers sign up for Gold | slides p.9; p.34; release p.2 | l.414; l.1340, l.1362; l.39; l.43 | PASS ×5 |
| 23 | $799M unamortised matches over about four years | slides p.37; 10-Q Item 1 | 220 + 579 = 799 (`10-Q` l.361, l.367), not labelled computed; `slides` l.1435–1437 say "~$761M of unamortized matches remaining with a weighted average amortization of approximately 4 years" | Unlabelled computation and source disagreement — REVISE item 4 |
| 24 | ACATS in ~$5.2B, out ~$2.4B | slides p.10 | l.458 | PASS ×2 |
| 25 | "tend to be younger"; "use some of these drawdowns as ways to buy"; Net Deposits $75.7B over twelve months, 27% | call p.18; release p.1 | l.817–818; l.25 | PASS ×3 |
| 26 | Churned 0.4–0.6 million a quarter 2025–2026 | slides p.29 | l.1162 ((0.4) (0.5) (0.5) (0.6) (0.4) (0.4)) | PASS |
| 27 | TradePMR $50B; "a good, durable, consistent source of Net Deposits" | release p.2; call p.18 | l.42; l.831–832 | PASS ×2 |
| 28 | Options + equities 36% of Q2 revenue (computed); "lower option rebate rates"; Rule 605 reports from August 2026; 2026 tick-size rules | 10-Q Item 2; 10-K Item 1A | (342+129)/1,308 = 36.0%; `10-Q` l.1802; `10-K` l.941 ("August 1, 2026 compliance date for the Rule 605 execution quality report amendments"), l.961 | PASS ×4 |
| 29 | Net interest 30% of Q2 revenue; 100 bp = $350M; 8% of FY2025 revenue (computed); Cash Sweep excluded from the sensitivity | 10-Q Item 3; 10-K Item 7A | 389/1,308 = 29.7% (unlabelled computation, item 11); `10-Q` l.2182; 350/4,473 = 7.8%; `10-K` l.2794 (Item 7A begins l.2786) | PASS ×4 |
| 30 | Blended yield 3.74% (2023) → 2.34% (Q2 2026) | 10-K FY2023 Item 7; slides p.39 | `10-K-FY2023` l.2091 (3.74% = total net interest revenues 929 / average interest-earning assets 24,826); `slides` l.1525 (last value 2.34% = annualised 389 / 66,383). Same definition both ends (the 2.33% beside it is the interest-earning-asset yield). I first suspected a definition mismatch; the arithmetic shows there is none | PASS (concern withdrawn) |
| 31 | Crypto 23% / 7% / 20% / 8% of revenue; app crypto volume −35% y/y | 10-K FY2023 Item 7; 10-K FY2025 Item 7; release p.3 | l.2037; l.2423; 100/1,308 = 7.6% (unlabelled computation, item 11); l.58 | PASS ×4 |
| 32 | Staking, stock tokens and Robinhood Chain "each risk being called unregistered securities activity" | 10-Q Item 1A | staking/onchain lending l.2299, l.3203; Classic Stock Tokens l.3201 (SEC "could assert jurisdiction"); Robinhood Chain l.3315–3329 covers adoption, technical failure and illicit use only | Over-extended to Chain — REVISE item 6 |
| 33 | Event contracts $10M → $156M; 12% of the total; Nevada from December 1, 2025; Wisconsin and Kentucky suits 2026; Illinois tax from July 1, 2026; "immediately or subsequently prevent us from offering" | 10-Q Note 6; Note 15; Item 1A | l.914; l.1547; l.1567 (April 23, 2026), l.1569 (June 17, 2026); l.2795; l.2275 | PASS ×6 (12% unlabelled computation, item 11) |
| 34 | FY2022 revenue −25%, transaction −42%, loss $1,028M; "A really strong market backdrop"; "the SpaceX IPO" | 10-K FY2023 Item 7 / Item 8; call p.11 | l.1986, l.2034, l.1899; l.492, l.494 | PASS ×5 |
| 35 | Outages (March 2020; August 2024) | 10-K Item 1A | l.1411 names the "March 2020 Outages" and the "April-May 2021 Disruptions" (crypto platform). "August 4-5, 2024" appears only in Note 15 (`10-K` l.4574; `10-Q` l.1485, l.1489) as "the disruptions experienced by BOATS during the Robinhood 24 Hour Market overnight trading session", a third-party venue, under MSD/FINRA examination | FAIL — REVISE item 1 |
| 36 | January 2021 collateral squeeze; November 2021 data breach; $45M SEC (January 2025); $26M FINRA (March 2025); NYAG, Massachusetts, FDIC inquiries; $89M accrual | 10-K Item 1A; 10-Q Note 15 | l.4584; l.1229 ("November 2021 Data Security Incident"); l.1233; l.1241; `10-Q` l.1485, l.1495; l.1461 | PASS ×7 |
| 37 | "large legacy financial institutions, large technology companies, and smaller, new financial technology entrants"; "might choose to forgo PFOF"; the 10-K names no rival | 10-K Item 1; Item 1A | l.573; l.1331; no Schwab / Fidelity / Interactive Brokers / SoFi / Webull anywhere in the 10-K (Coinbase, Binance, Kraken appear only as SEC-enforcement examples, l.1667) | PASS ×3 |
| 38 | "Coinbase and Webull appear only as co-defendants in the Kentucky suit"; Kalshi both a venue and a rival | 10-Q Note 15; call p.27 | Kentucky l.1569 names Webull and Coinbase; but Wisconsin l.1567 also names Coinbase Global and Coinbase Financial Markets; Kalshi as venue l.1240 | Overstated ("only ... Kentucky") — REVISE item 5 |
| 39 | Tenev 39, sole CEO since November 2020, chair since March 2021; Bhatt 41, Chief Creative Officer until March 2024, still a director | DEF 14A | l.685, l.691–695; l.712, l.722 | PASS ×5 |
| 40 | Warnick retirement announced October 30, 2025; Verma CFO February 6, 2026, SVP Finance and Strategy since 2018; Warnick advising until September 1, 2026 | 8-K 2025-11-05; 8-K 2026-02-10 | l.67–69; l.67 | PASS ×4 |
| 41 | ~10% of staff cut June 16, 2026, "a $23 million charge" | 8-K 2026-06-16; slides p.43 | 8-K l.61 estimates ~$20M severance + ~$8M SBC; `slides` p.43 l.1707 and `release` l.305 show $23M restructuring charges, plus $7M "SBC attributable to restructuring" (release l.319) | Number PASS for the restructuring line, but it omits the stock-pay half — REVISE item 7 |
| 42 | Ten directors, eight independent, elected annually | DEF 14A | l.568; l.288; l.288 | PASS ×3 |
| 43 | Class B ten votes, held only by founders and their vehicles; Tenev 26.1%, Bhatt 32.0%; "control approximately 58% of the total outstanding voting power"; "will be able to determine the outcome of the election of directors" | DEF 14A | l.403, l.1153; l.2425, l.2430; l.1157 | PASS ×5 |
| 44 | Class B converts August 2, 2036, or earlier on an 80% Class B vote, if Class B falls below 5%, or after both founders leave or die | DEF 14A; 10-K Note 12 | l.1153 ("August 2, 2036, which is the fifteenth anniversary of our IPO closing date"); `10-K` l.4312 (80%; less than 5%; founders no longer officers/employees/consultants and not directors; death or total disability of both) | PASS ×4 |
| 45 | Class B 128.0M (end 2021) → 108.5M | 10-K FY2022 Item 8; 10-Q cover | l.2522 (127,955,246); `10-Q` l.67 (108,452,039 as of July 23, 2026) | PASS ×2; "as the founders sell" is an unlabelled inference (optional item 13) |
| 46 | Vanguard ~11.9%; BlackRock 7.0% | DEF 14A | l.2494; l.2441 | PASS ×2 |
| 47 | Salary $34,248; no new equity since 2021; 2021 award valued at $794 million; 2021 tranche cancelled February 2023 ($485M); "compensation actually paid" 2025 $1,020.8 million | DEF 14A; 10-K Note 12 | l.1682, l.1907–1909 (no stock awards 2023–2025); l.2263 (Reported Value of Equity Awards 2021 $794,011,732); l.4391; l.2248 ($1,020,806,245) | PASS ×5. The writer's flag: the sentence says "the 2021 award valued at $794 million", which is the equity-award value in the Pay Versus Performance table, not the $796.1M Summary Compensation Table total (l.2252); wording and figure agree |
| 48 | Bonus measures: revenue, adjusted net income, Net Deposits, Gold growth, international accounts; Verma ~$18M promotion grant | DEF 14A; 8-K/A 2026-03-24 | l.304 / l.1637; l.63 | PASS ×2 |
| 49 | Never paid a dividend | 10-K Item 5 | l.2115 | PASS |

Totals across 3(a)–3(h): 283 numbers, quotes and sentences checked. FAIL: 2 (August 2024 outage mis-sourced/mis-described; TradePMR price superseded). Overstated or mis-described but numerically correct: 4 ($129M "from deconsolidating"; "only ... Kentucky"; Robinhood Chain as unregistered-securities risk; $23M restructuring omitting $7M stock pay). Disclosed-in-cache "not stated": 1 (Gold $5 a month). Unlabelled computations: 4 (item 11) plus the $799M sum. Concern raised and withdrawn: 1 (yield definitions, row 30). Tag corrections made directly: 5 (see §9).

---

## 4. Jargon audit

Reader: a smart 16-year-old with no finance background. Terms found that were neither plain, name-inferable nor in the Glossary, and the fix applied (all direct fixes, logged in §9):

| Term | Where | Action |
|---|---|---|
| options; futures | business.md §1 l.6 | Glossed "(contracts giving the right to buy or sell a stock at a set price)" and "(contracts to buy or sell something at a set price on a future date)" |
| clearinghouse; collateral | business.md §1 l.10 | Glossed "(the central body that settles trades)" and "(cash as security)" |
| segregated customer cash; short sellers | business.md §2 l.49 | Glossed "(customer money kept apart from the firm's own by law)" and "(traders betting a price will fall)" |
| IRA; proxy-voting; IPO selling concessions | business.md §2 l.51 | Glossed "(retirement account)", "(shareholder-vote)", "(fees for distributing new share offerings)" |
| incremental Adjusted EBITDA margin | business.md §3 l.55 | Glossed "(the share of each extra revenue dollar that became Adjusted EBITDA)" |
| H1 | business.md §3 l.67; outlook.md §1 l.16 | "(H1 = first half)" / "(H1, first half: ...)" |
| Capex | business.md §3 l.71 | "Capex (capital spending)" |
| unamortised | business.md §5 l.102 | "(not yet charged against revenue)" |
| tick-size; Rule 605 execution reports | business.md §6 l.112 | "(minimum price step)"; "execution-quality reports (the SEC's standard broker scorecards)" |
| basis point | business.md §6 l.114; outlook.md §3 l.35 | "(one percentage point)" for 100 bp; "(hundredths of a percent)" |
| FINRA; contingency accrual | business.md §6 l.122 | "(FINRA, the brokers' self-regulator)"; "(money set aside for expected legal losses)" |
| accordion | business.md §7 l.146 | Replaced with "expandable to" |
| deconsolidated | business.md §7 l.149 | "(dropped from Robinhood's own accounts once it lost control)" |
| SBC | outlook.md §1 l.16 (first use; outlook has no glossary) | "(SBC: stock-based compensation)" |
| ARR; run-rate; trailing | outlook.md §2 l.21 | "(ARR: annualized revenue)"; "(latest quarter times four)"; "trailing (last twelve months)" |
| DCM | outlook.md §3 l.25 | "(designated contract market, a regulated futures exchange)" |
| Strategies | outlook.md §3 l.31 | "Robinhood Strategies (its managed-portfolio service)" per `10-Q` Note 1 l.653 |
| DEX volume; stock tokens; Earn; Arbitrum | outlook.md §3 l.35 | "(trading on decentralized exchanges)"; "(blockchain tokens tracking U.S. stocks)"; "(its stablecoin lending product)" per `transcript` l.130–131; "(the network the chain is built on)" per l.1107 |
| Legend; Agentic Trading | outlook.md §3 l.37 | "(its desktop platform for active traders)" per `10-K-FY2025` l.419; "(trading through AI agents)" per release l.36 |
| notional volume | outlook.md §5 claim 5 | "notional (dollar) volume" |

Judged acceptable without change: PFOF, market maker, margin loan, Cash Sweep, securities lending, event contract, net capital, Adjusted EBITDA, Adjusted Operating Expenses and SBC, convertible notes and capped call, RIA (all in the Glossary); "spread" (covered by the Cash Sweep entry); valuation allowance (explained at l.90); Say Technologies, X1, TradePMR, Bitstamp, MIAXdx/Rothera, WonderFi (each explained at l.10); Gold and the Gold Card (l.51, l.100); Rule of 40 (explained in the sentence); Total Platform Assets, Funded Customers, Net Deposits (company KPI names used with their meaning evident); SEC, IPO, Nasdaq, blockchain, stablecoin (widely known or name-inferable). Glossary: 11 entries, each one sentence, each a term that recurs in the text.

---

## 5. Invented-number / unsupported-inference check

- **"August 2024" outage** (business.md §6 l.122): not an outage in Item 1A; see 3(h) row 35. REVISE item 1.
- **"$129 million of gains from deconsolidating RVI"** (§4 footnote ⁸ l.86): the release says "primarily related to"; the reconciliation splits $106M + $23M. REVISE item 2.
- **TradePMR "~$175M"** (§7 l.144): superseded by the 10-Q's final ~$169M. REVISE item 3.
- **"$799 million was unamortised ... over about four years"** (§5 l.102): $799M is 220 + 579 from the balance sheet, not labelled computed; the slides state ~$761M for the same concept. REVISE item 4.
- **"(price not stated in the filings)"** for Gold (§2 l.51): slides p.9 give "$5 per month". REVISE item 8.
- **"(amount not in the cached filings)"** for the December 2020 SEC settlement (§2 l.39): correct; no amount appears in any cached filing.
- **Unlabelled computations that are correct**: "Net interest was 30% of Q2 2026 revenue" (389/1,308 = 29.7%, l.114); "8% in Q2 2026" crypto share (100/1,308 = 7.6%, l.116); "12% of the total" event contracts (156/1,308 = 11.9%, l.118); outlook l.25 "12% of revenue". REVISE item 11 (add "(computed)").
- **Unlabelled inference**: "as the founders sell" (§7 l.132) explains the Class B decline; the filings show the count, not the reason (Class B converts on transfer). Optional item 13.
- **Slight overstatement**: "Thirteen business lines each earn over $100 million a year" (§5 l.98) vs the slides' footnote (crossed ~$100M quarterly annualized at some point). Optional item 12.
- Every "(computed)" cell in §3, §4 and §7 and every computed figure in outlook §5 (claim 1's $764M = (2,775 − 1,248)/2 = 763.5; claim 5's $6.1B = 18.3/3; claim 10's 918–923M range from slides p.42 l.1660: 917.7 / 921.9 / 920.6 / 923.0 / 918.5) re-derives correctly.
- **"$300" no-dilution threshold**: correctly labelled as the CFO's unfiled statement (l.149), with the filed $174.42 conversion price and $237.85 cap beside it. The MANIFEST notes that ~$300 follows only when the $290M concurrent repurchase is netted; the draft does not attempt that arithmetic. Compliant.
- **"over $5 billion of annual revenue"**: labelled a run-rate; trailing $4.9B from slides p.4 l.140. Compliant.
- **Post-cutoff information**: none found. Every fact traces to a document dated on or before 2026-07-30; the July 23, 2026 ABS issuance in 10-Q Note 11 is not used.
- **Statement about the call** (outlook l.21, "Nobody on the call mentioned interest rates, payment for order flow, credit losses or the June layoffs"): verified by search of `transcript.txt` for "interest rate", "PFOF", "order flow", "credit loss", "layoff", "reduction in force", "restructuring", "Federal Reserve", "rate cut": no hits ("interest" appears only in "interest earning assets", "compound interest" and non-financial senses). PASS; tag added (direct fix).

---

## 6. Claims check (§9), outlook.md §5

| # | One sentence, one thing | Single direction, can fail | Verbatim quote + tag | Labelling | Gradeable from §5 alone |
|---|---|---|---|---|---|
| 1 | Yes | Yes (fails if Q3 > $764M) | Yes | Sharpening labelled ("half the second half implied by the top of the range, not management's number"); arithmetic verified | Yes (Q3 release reconciliation) |
| 2 | Yes | Yes | Yes | — | Yes (Q3 release p.1 trailing-twelve-month rate) |
| 3 | Yes | Yes | Yes | Sharpening labelled | Yes (July monthly metrics) |
| 4 | **No: two metrics** (equity ADV within 10% of $15.4B and options ADV within 10% of 12.5M) | Each half can fail | Yes | Sharpening labelled; Q2 averages verified (`supplement` l.111–112) | Partly — REVISE item 9 |
| 5 | Yes | Yes | Yes | "(computed from $18.3 billion)" stated; source `slides` p.33 l.1301 | Yes (July monthly metrics) |
| 6 | Yes | Yes | Yes | — ; Q2 figure 2.1B at `slides` l.1287 | Yes (Q3 slides) |
| 7 | Yes | Yes | Yes | — | Yes (Q3 release or call) |
| 8 | Yes | Yes | Yes | — | Yes (Q3 call) |
| 9 | Yes | Yes | Yes | — | Yes (Q3 call) |
| 10 | Yes | Yes | Yes | Sharpening labelled; range stated | Yes (Q3 slides share-count page) |
| 11 | Yes | Yes | n/a (disclosure check) | Labelled "Disclosure check (quarter column)"; "Not a management claim"; series 13% / 15% / 16% verified (`10-K-FY2025` l.3298; `10-Q-2026-Q1` l.623; `10-Q` l.686) | Yes (Q3 10-Q Note 1) |

Count 11 (within 6–12). Headline revenue/EPS: none; the only guidance-type claim is the expense range (claim 1). The rest are fundamental signals: Net Deposit growth, July volumes, crypto volume, Rothera share, product milestones (Social, agentic crypto, employer funding of Trump Accounts), share count, market-maker concentration. No either/or constructions. No vague statements passed off as claims.

---

## 7. Indicator check (§8)

Eight indicators in business.md §8, each named, with a why and a source location, each anchored to a disclosure that recurs every quarter:

1. Net Deposits and annualized growth rate — release p.1 bullet every quarter; monthly metrics. Recurring.
2. Funded Customers with new / resurrected / churned — release p.1; slides roll-forward (p.29 this quarter, nine quarters shown). Recurring.
3. Total Platform Assets — release p.1; monthly metrics. Recurring.
4. Robinhood Gold Subscribers and adoption rate — release p.1 and p.2; slides. Recurring.
5. Transaction-based revenue by line — release income statement and 10-Q Note 6 (event contracts now a separate line, footnoted in §2). Recurring.
6. Net interest revenue, Margin Book, Cash Sweep — release "Additional [quarter] Operating Data"; slides net-interest table (p.39). Recurring.
7. Adjusted Operating Expenses and SBC against the full-year outlook — release reconciliation and "Financial Outlook" section, both present in every release. Recurring.
8. Largest market maker's share of total net revenues — 10-Q Note 1 "Concentrations of Revenue". Recurring.

None depends on a one-off number from a single call (the "$300" threshold, "over $5 billion" run-rate, "13 businesses" and "Rule of 80" are handled in prose or as claims, not as indicators). Outlook §1 has exactly one row per indicator, in the same order, with Q2 2026 / Q1 2026 / expectation columns, "No guidance" where none was given, and the header says the set is proposed. The row labels paraphrase the §8 names rather than repeat them (REVISE item 10).

---

## 8. Length (§3 rule 7 method, `python3 -P /tmp/hood-orch/wc_prose.py`)

| File | Before review | After direct fixes (glosses, tags) | Range | Status |
|---|---|---|---|---|
| business.md | 2,558 | 2,671 | 2,000–3,000 | OK |
| outlook.md | 1,086 | 1,142 | 800–1,200 | OK, 58 words under the ceiling; the writer's revisions (items 9–11) should not add net words |

---

## 9. Direct fixes made by the reviewer (logged per §13)

1. business.md §3 sources line l.67: `[Q2 2026 release, p.11]` → `[Q2 2026 release, p.12]` (the Adjusted Operating Expenses and SBC totals row, including H1 $1,248M, is `press-release.txt` l.338, on printed page 12; p.11 ends at l.323). Also added "(H1 = first half)".
2. business.md §3 l.69: `[Q2 2026 release, p.11]` → `[Q2 2026 release, p.1]` for the $641M (release l.20; the p.11 table stops at Adjusted Operating Expenses $550M).
3. business.md §7 table l.142: `[10-Q Q2 2026, Note 12]` → `[10-Q Q2 2026, Part II Item 2]` for "$1,373M left" (`10-Q` l.3607–3608; Note 12 l.1325–1329 does not state the remaining authorization).
4. business.md §7 table l.147: added `[10-K FY2023, Item 8]` (end-2023 share count 745,401,862 + 126,760,802 is only in the FY2023 10-K, l.2584–2585).
5. business.md §8 indicator 6 l.158: press release "Additional Operating Data" → "Additional [quarter] Operating Data" (the heading is "Additional Q2 2026 Operating Data", release l.50).
6. outlook.md §1 l.12: added `[Q2 2026 slides, p.29]` beside the release tag for Total Platform Assets $368.7B (the release rounds to $369 billion; the decimal is slides l.1182).
7. outlook.md §1 l.16: `[Q2 2026 release, p.11]` → `[Q2 2026 release, p.12]` for the H1 $1,248M (release l.338).
8. outlook.md §2 l.21: added `[Q2 2026 call, p.1–29]` to the untagged sentence "Nobody on the call mentioned interest rates, payment for order flow, credit losses or the June layoffs."
9. Jargon glosses listed in §4 (fourteen in business.md at l.6, 10, 49, 51, 55, 67, 71, 102, 112, 114, 122, 146, 149; nine in outlook.md at l.16, 21, 25, 31, 35, 37, 54). No prose, numbers or claims were rewritten; every edit is an inserted parenthetical, a replaced single word ("accordion" → "expandable to"), or a tag.
10. Housekeeping: during the check I suspected the 3.74% (2023) vs 2.34% (Q2 2026) yield comparison mixed two definitions (the slides' 2.33% is the interest-earning-asset yield). Re-deriving both ends showed 3.74% = 929/24,826 and 2.34% = 4 × 389/66,383, both total-net-interest-revenue yields on average interest-earning assets. No change made; the concern is withdrawn and recorded here.

---

## 10. Verdict: REVISE

Numbered list for the writer (file:line, what is wrong, what would fix it). Items 1–9 are factual or structural; 10–11 are minor; 12–13 optional.

1. **business.md:122 (§6 #6)** — "Outages (March 2020; August 2024)" tagged `[10-K FY2025, Item 1A]`. Item 1A (`10-K-FY2025.txt` l.1411) names the "March 2020 Outages" and the "April-May 2021 Disruptions" on the crypto platform. "August 4-5, 2024" appears only in the legal note (`10-K` l.4574; `10-Q` l.1485, l.1489) as "the disruptions experienced by BOATS during the Robinhood 24 Hour Market overnight trading session", a third-party overnight venue, which the Massachusetts Securities Division and FINRA are examining. Fix: "Outages (March 2020; the April–May 2021 crypto disruptions) [10-K FY2025, Item 1A]" and, if wanted, add "a third-party overnight-venue disruption in August 2024 still under regulatory examination [10-Q Q2 2026, Note 15]".
2. **business.md:86 (§4 footnote ⁸)** — "Includes $129 million of gains from deconsolidating Robinhood Ventures Fund I". The release (l.16) says "$129 million of gains primarily related to the deconsolidation of RVI"; the reconciliation (release p.11 l.307–312) splits it into a $106M deconsolidation gain and $23M of gains on equity securities "primarily related to investments held by RVI". Fix: "Includes $129 million of gains, $106 million of it from deconsolidating Robinhood Ventures Fund I [Q2 2026 release, p.1] [Q2 2026 release, p.11]". This also makes the footnote consistent with the $106M at l.149.
3. **business.md:144 (§7 table)** — TradePMR "~$175M". The FY2025 10-K's $175M (l.2119) was preliminary; the Q2 2026 10-Q Note 3 (l.724) gives the final consideration as "approximately $169 million following customary purchase price adjustments" after the allocation was finalised in Q1 2026. Fix: "~$169M (final; $175M preliminary)" keeping both tags.
4. **business.md:102 (§5)** — "$799 million was unamortised at June 30, 2026 over about four years [Q2 2026 slides, p.37] [10-Q Q2 2026, Item 1]". $799M is the sum of two balance-sheet lines (deferred customer match incentives 220 current + 579 non-current, `10-Q` l.361, l.367) and is not labelled computed; the slides (p.37 l.1435–1437) say "~$761M of unamortized matches remaining with a weighted average amortization of approximately 4 years". Fix: either "$799 million of deferred match incentives sat on the balance sheet (computed from two lines) and the slides put unamortised matches at about $761 million with roughly four years to run", or use the slides' figure alone with the p.37 tag.
5. **business.md:124 (§6 #7)** — "Coinbase and Webull appear only as co-defendants in the Kentucky suit". Coinbase Global and Coinbase Financial Markets are also co-defendants in Wisconsin's April 23, 2026 suit (`10-Q` l.1567); Webull is only in Kentucky (l.1569). Fix: "Coinbase and Webull appear only as co-defendants in the Wisconsin and Kentucky suits".
6. **business.md:116 (§6 #3)** — "Staking, stock tokens and Robinhood Chain each risk being called unregistered securities activity [10-Q Q2 2026, Item 1A]". True for staking and onchain lending (`10-Q` l.2299, l.3203) and for Classic Stock Tokens (l.3201, the SEC "could assert jurisdiction"); the Robinhood Chain risk factors (l.3315–3329) are about adoption, technical failure and illicit use, not securities status. Fix: drop Robinhood Chain from that sentence, or say "Robinhood Chain carries its own adoption, technical and illicit-use risks".
7. **business.md:130 (§7)** — "cut about 10% of staff, a $23 million charge [8-K 2026-06-16, Item 2.05] [Q2 2026 slides, p.43]". The 8-K (l.61) estimated about $20M of cash severance plus about $8M of stock pay; the Q2 release (p.11 l.305, l.319) recorded $23M of restructuring charges plus $7M of "SBC attributable to restructuring". Fix: "a $23 million restructuring charge plus $7 million of stock pay [Q2 2026 release, p.11]" (or "about $30 million in total").
8. **business.md:51 (§2 c)** — "(price not stated in the filings)" for Gold. Literally true of the 10-K and 10-Q, but the cached slides state it: "meaningful value for $5 per month" (`slides` p.9 l.373–374). Fix: "($5 a month per the slides [Q2 2026 slides, p.9])".
9. **outlook.md:53 (§5 claim 4)** — two checks in one claim (equity ADV and options ADV each within 10% of the Q2 average). §9: one sentence, one thing. Fix: keep one metric, or split into two claims (count would become 12, still within range).
10. **outlook.md:10–17 (§1 row labels) vs business.md:153–160 (§8 names)** — the rows correspond one-to-one and in order, but the labels are paraphrases ("Net Deposits; annualized growth rate" vs "Net Deposits and annualized growth rate"; row 2 adds "acquired"; row 8 adds "all market makers and exchanges"; row 7 "full-year outlook" vs "against the full-year outlook"). §8 says the locked set must be used exactly so quarters are comparable. Fix: make the §1 labels the §8 names verbatim (or edit §8 to the labels you want locked; adding "acquired" to indicator 2 and "and all market makers" to indicator 8 is sensible).
11. **Unlabelled computations (minor)** — business.md:114 "Net interest was 30% of Q2 2026 revenue" (389/1,308); :116 "8% in Q2 2026" (100/1,308); :118 "12% of the total" (156/1,308); outlook.md:25 "12% of revenue". Add "(computed)" to each, as §3 rule 1 requires; all four re-derive correctly.
12. **business.md:98 (§5), optional** — "Thirteen business lines each earn over $100 million a year" reads as a current run-rate for all thirteen; the slides' footnote (p.16 l.704) measures when each line crossed ~$100M of quarterly annualized revenue. Consider "Thirteen business lines have each reached a $100 million annual revenue run-rate".
13. **business.md:132 (§7), optional** — "as the founders sell" is an inference (Class B converts to Class A on transfer; the filings give the count, not the reason). Label it "our inference" or write "as Class B is converted".

---

## 11. Points the writer flagged, checked

- **Tenev's 2021 award "$794 million"**: matches the Pay Versus Performance "Reported Value of Equity Awards" for 2021 (`DEF14A-2026.txt` l.2263, $794,011,732); the sentence says "the 2021 award valued at $794 million", so wording and figure agree. The $796.1M Summary Compensation Table total (l.2252) is not used. PASS.
- **Q1 2026 Citadel 15%, all market makers 48%**: `10-Q-2026-Q1.txt` l.623, l.630. PASS.
- **"$300" no-dilution threshold**: `transcript` l.203–204 (CFO, p.5), labelled unfiled at business.md l.149; filed $174.42 and $237.8475 at `8-K-2026-06-25` l.67, l.83 and `10-Q` l.1225, l.1243. PASS. **"Over $5B"** labelled run-rate, trailing $4.9B at `slides` l.140. PASS. **Agentic accounts**: release l.36 "nearly 100 thousand" and call l.617 "over 100,000", both shown. PASS. **Transcript p.17–18 label**: l.798 reads "Vladimir Tenev" but l.821 ("As I shared, July, the average daily volumes are very similar to the Q2 average") continues the CFO's l.208–211 remarks; the outlook says so in §4 and in its Sources entry. PASS.
- **Outages "March 2020; August 2024"**: FAIL, REVISE item 1.
- **`[10-K FY2023, Note 14]`** for the 2023 U.S. Marshals repurchase: Note 14 heading at l.3792, text at l.3840. PASS. **DEF 14A section-title tags**: "Executive Officers" (l.1560), "Director Nominees" (l.583), "Director Independence" (l.663), "Stockholder Structure" (l.1149), "Executive Compensation" (l.1592), "Pay Versus Performance" (l.2239) all exist; "Beneficial Ownership" is a shortened form of "Beneficial Ownership of Principal Stockholders and Management" (l.2415). Acceptable.
- **Definition changes**: event contracts as a separate line from 2026 is footnoted in the §2 table (¹) and the segregated-cash line's netting (²); Bitstamp/WonderFi inclusion is footnoted; the drafts show no pre-2024 balance sheets (only share counts), so the SAB 122 comparability point does not arise; "Assets Under Custody" and "DARTs"/"DATs" are not used in either file. Nothing missing.
- **PFOF plain-English explanation and why regulators care**: business.md §2(a) l.37–39 (routing, per-contract and spread-based payments, best-execution conflict, December 2020 settlement, NYAG inquiry, outsized-impact and no-binding-contract quotes), all sourced. Present. **Interest-rate dependence quantified**: §6 #2 l.114, 100 bp = $350M over twelve months (`10-Q` Item 3 l.2182), Cash Sweep exclusion (`10-K` Item 7A l.2794). Present. **Crypto dependence by year**: §6 #3 l.116, 23% / 7% / 20% / 8%. Present. **Dual-class control**: §7 l.132, Tenev 26.1% and Bhatt 32.0% of votes, ~58% under the voting agreement, sunset August 2, 2036 and earlier triggers. Present and sourced.

---

## 12. As-of discipline

Every source read is dated on or before 2026-07-30 (10-Q filed 2026-07-30; call, release, slides, supplement and June metrics 2026-07-29). MANIFEST records that later filings and the July 2026 monthly metrics were seen in listings but not opened, and that the Motley Fool copy (posted 2026-08-07) was used by the gatherer only for wording cross-checks; it is not tagged anywhere in the drafts and was excluded from this review's searches. Neither draft refers to any event after the Q2 call. No concern.

---

## Cycle 2 (final)

_Re-read both drafts from disk on 2026-09-09 after the writer's second pass; verified against the cached sources only (full lines). Word counts as received 2,670 / 1,141; after this cycle's one tag addition 2,670 / 1,141 (ranges 2,000–3,000 / 800–1,200). Every cycle-1 direct fix is still in place._

**Final verdict: PASS.**

### Per-item verification of the writer's changes

| # | Change (as now in the draft) | Verified against | Status |
|---|---|---|---|
| 1 | business.md §6 #6 l.122: "Outages (March 2020; crypto, April–May 2021), a third-party overnight venue's disruption in August 2024 still under regulatory examination, ..." [10-K FY2025, Item 1A] [10-Q Q2 2026, Note 15] | `10-K-FY2025.txt` l.1411 ("the March 2020 Outages ... the partial service outages and degraded service on our RHC cryptocurrency platform ... in mid-April and early May 2021"); `10-Q-2026-Q2.txt` l.1485 (MSD examining "the disruptions experienced by BOATS during the Robinhood 24 Hour Market overnight trading session on August 4-5, 2024"), l.1489–1495 (FINRA investigating the same) | Resolved |
| 2 | §4 footnote ⁸ l.86: "Includes $129 million of gains, $106 million of it from deconsolidating Robinhood Ventures Fund I" [release p.1] [release p.11] | `press-release.txt` l.16 ($129 million "primarily related to"); l.307 (Gain on deconsolidation of RVI (106)), l.311 | Resolved; consistent with the $106M at l.149 |
| 3 | §7 table l.144: TradePMR "~$169M (final; $175M preliminary)" | `10-Q` Note 3 l.724 ("approximately $169 million following customary purchase price adjustments"; allocation finalised Q1 2026); `10-K-FY2025` l.2119 ($175 million) | Resolved |
| 4 | §5 l.102: "about $761 million was unamortised ... at June 30, 2026 over about four years" [Q2 2026 slides, p.37]; the $799M sum dropped | `slides.txt` l.1435–1437 ("~$761M of unamortized matches remaining with a weighted average amortization of approximately 4 years") | Resolved |
| 5 | §6 #7 l.124: "Coinbase and Webull appear only as co-defendants in the Wisconsin and Kentucky suits" | `10-Q` l.1567 (Wisconsin, April 23, 2026: Coinbase Global and Coinbase Financial Markets), l.1569 (Kentucky, June 17, 2026: Webull Corporation and Coinbase Financial Markets) | Resolved (read collectively; Webull is in Kentucky only, which the sentence does not contradict) |
| 6 | §6 #3 l.116: "Staking, onchain lending and stock tokens each risk being called unregistered securities activity; Robinhood Chain carries its own adoption, technical and illicit-use risks" [10-Q Q2 2026, Item 1A] | `10-Q` l.2299 and l.3203 (staking / onchain lending "unregistered offers and sales of securities or unregistered securities broker-dealer activity"); l.3201 (Classic Stock Tokens: "the SEC could assert jurisdiction ... and claim that transactions ... must be conducted in compliance with applicable federal laws and regulations", a fair plain rendering); l.3315–3329 (Chain: adoption, technical vulnerabilities, illicit activity) | Resolved |
| 7 | §7 l.130: "$23 million of restructuring charges plus $7 million of related stock pay, against the 8-K's estimate of about $20 million plus $8 million" [8-K 2026-06-16, Item 2.05] [Q2 2026 release, p.11] | `press-release.txt` l.305 (Restructuring charges 23), l.319 (SBC attributable to restructuring 7), both on p.11 (l.290–323); `8-K-2026-06-16.txt` l.61 ("approximately $20 million related to employee severance and benefits costs as well as approximately $8 million related to share-based compensation") | Resolved |
| 8 | §2(c) l.51: Gold "a $5-a-month subscription" [Q2 2026 slides, p.9] | `slides.txt` l.373–374 ("meaningful value for $5 / per month") | Resolved |
| 9 | outlook §5: claim 4 (equity ADV within 10% of $15.4B) and claim 5 (options ADV within 10% of 12.5M, "same sharpening"); claims renumbered 1–12 | `transcript.txt` l.208–209 (claim 4 quote), l.209 ("in a similar area for equities, options, and event contracts", claim 5 quote); `earnings-supplement-2026-Q2.txt` l.111 (Equity ADV Q2'26 15.4), l.112 (Options Contracts 12.5) | Resolved; each claim is one metric, single direction, fails if the July monthly metrics land outside the band |
| 10 | outlook §1 row labels vs business §8 names; §8 indicator 2 renamed "Funded Customers, with new, resurrected, acquired and churned" | Programmatic comparison of the eight §8 bold names with the eight §1 first-column labels: 8/8 identical strings, same order. Row 8 keeps the extra "all market makers and exchanges 47%" inside the value cell, not the label. The "SBC = stock-based compensation" gloss moved to the header note (l.6) | Resolved |
| 11 | Writer disagreed with adding "(computed)" to 30% / 8% / 12% and added [10-Q Q2 2026, Item 2] tags instead | `10-Q-2026-Q2.txt` l.1792–1797 ("Transaction-based revenues as a % of total net revenues:" three months ended June 30, 2026 column: Options 26%, Event contracts 12%, Cryptocurrencies 8%, Equities 10%); l.1837 ("Total net interest revenues \| 36% \| 30% \| 34% \| 31%", i.e. 30% for the three months ended June 30, 2026). Tags now present at business.md l.114, l.116, l.118 and outlook.md l.25 | **Ruling: the writer is right and cycle-1 item 11 is withdrawn.** The 30%, 8% and 12% shares are printed in the 10-Q's percent-of-revenue tables, so they are sourced figures, not computations; the Item 2 tag is the correct label. (The 36% at l.112 remains "(computed)", correctly, because it sums the 10-Q's 26% and 10%.) |
| 12 | §5 l.98: "Thirteen business lines have each reached a $100 million annual revenue run-rate (a quarter's revenue times four)" [Q2 2026 slides, p.16] | `slides.txt` l.704 ("Measured based on when a given business crossed ~$100 million in quarterly annualized revenues (revenues in a given quarter times 4)") | Resolved |
| 13 | §7 l.132: "as the founders convert or transfer shares" [DEF 14A 2026, "Voting Agreements"] | `DEF14A-2026.txt` l.2543 (Bhatt "converted or transferred approximately 13.2 million shares", Tenev "approximately 13.4 million shares" through April 8, 2026); section heading "Voting Agreements" at l.2527 | Resolved; the inference is now a sourced fact |

### Offsetting trims, checked

- "(now a family of apps)" dropped from l.6; the §3 convertible sentence shortened to "In June 2026 the parent added $2.2 billion of 0% convertible notes (§7)"; the H1 2025 operating-cash-flow example dropped from l.88; the Verma $18M promotion-grant clause dropped from l.134 and the `8-K/A 2026-03-24` Sources entry removed; "IPO selling concessions" dropped from l.51; §8 indicator 3 shortened to "The asset base behind every revenue line."; outlook §4 no longer repeats the prior range (it remains in §1 row 7 with its tag); two "Working if" lines tightened. None of these removes a fact that another sentence relies on.
- **One consequence caught:** the shortened §3 sentence (l.71) kept only the launch-release tag `[8-K 2026-06-23, Exhibit 99.1]`, which announces a "$2.0 Billion" offering with an option for "up to an additional $200 million" (`8-K-2026-06-23-ex991.txt` l.8) and so does not state $2.2 billion. The $2.2 billion and the 0.00% coupon are in `8-K-2026-06-25.txt` l.59–61 and `10-Q` Note 11 l.1203. Added `[8-K 2026-06-25, Item 1.01]` beside the existing tag (direct fix 1 below).

### Other checks requested

- **(a) Changed and new sentences:** all thirteen items and the trims above verified against full source lines; the programmatic quote check was re-run over both files: 109 quoted strings, all found in the cache (the three "misses" are the known artefacts: the p.17–18 quote spanning the transcript's page footer at l.801/807, the writer's connective ", where growth plus margin" between two quotes, and the reviewer's own "[quarter]" placeholder in indicator 6). Every number in the §2, §3, §4 and §7 tables and in outlook §1 is unchanged from cycle 1 except TradePMR (item 3) and re-verifies.
- **(b) Sources lists:** business.md uses 17 tag families (10-K FY2025 / FY2024 / FY2023 / FY2022, 10-Q Q2 2026, DEF 14A 2026, 8-K 2025-11-05, 8-K 2026-02-10, 8-K 2026-03-24, 8-K 2026-06-16, 8-K 2026-06-23, 8-K 2026-06-25, Q2 2026 release / slides / supplement / call, June 2026 metrics); all 17 are listed and no other family is used. No `8-K/A` or `8-KA` string remains in either draft. The new `"Voting Agreements"` section title exists in the proxy (l.2527). outlook.md uses 8 families, all listed.
- **(c) Indicators and claims:** §1 labels equal §8 names exactly (8/8, verified by string comparison). Claims: 12 (within 6–12), each one sentence, one metric or event, single direction, able to fail; sharpenings labelled (claims 1, 3, 4, 5, 6, 11); the disclosure check (claim 12) labelled with "quarter column". Headline guidance is still only claim 1.
- **(d) Length:** `python3 -P /tmp/hood-orch/wc_prose.py` → business.md 2,670, outlook.md 1,141 (writer's counts confirmed); unchanged after this cycle's tag addition.
- **(e) Rubric (§14):** 1 Yes (§1 l.6–8); 2 Yes (§6, seven ranked scenarios with early warnings, rates and crypto quantified); 3 Yes (§3, 5% variable cost line, 60% incremental margin, 1–2% capex against large held balances); 4 Yes (12 single-metric claims, no double-barreled claim remains); 5 Yes (every cycle-1 gloss retained; no new jargon introduced by the revisions; "onchain lending" is name-inferable next to "staking").
- **(f) Jargon / untagged figures in the changed sentences:** none new. The new "$5-a-month" carries the slides tag; "$761 million" the slides tag; "$169M" the 10-Q tag; "$7 million" the release tag; "13.2/13.4 million" are not quoted, only the conclusion, which is tagged.
- **As-of discipline:** unchanged; nothing dated after 2026-07-30 is used.

### Direct fixes this cycle

1. business.md §3 l.71: added `[8-K 2026-06-25, Item 1.01]` after `[8-K 2026-06-23, Exhibit 99.1]` on "In June 2026 the parent added $2.2 billion of 0% convertible notes (§7)". Reason: the launch release states $2.0 billion plus a $200 million option; the $2.2 billion aggregate and 0.00% coupon are stated in the closing 8-K (l.59–61). No other edits.

### Left open for the owner

No factual item remains open. Judgment calls only: (i) the Glossary carries three finance terms (Adjusted EBITDA, Adjusted Operating Expenses and SBC, Convertible notes and capped call) that §3 rule 4 might exclude; (ii) the §8 indicator set is proposed and awaits the owner's lock (indicator 2 now includes "acquired"); (iii) outlook.md sits 59 words under its ceiling, so the first refresh should aim to trim rather than add.
