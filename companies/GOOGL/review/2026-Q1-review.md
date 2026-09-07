# Alphabet Inc. (GOOGL) — Reviewer report, 2026-Q1

_Reviewed 2026-09-07 against `companies/GOOGL/sources/2026-Q1/` only (cached full texts; notes used only to see whether an error came from a note). `sources/2026-Q2/` was not opened, listed, or grepped. Line numbers below refer to the cached `.txt` files; transcript page numbers are the printed page footers in `transcript.txt` (p.4 = lines 138–182, p.12 = 500–544, p.13 = 545–590, p.19 = 819–864, p.20 = 865–910, p.23 = 1003–1048)._

**Verdict: REVISE** (second pass needed; no factual problem in the tables, but one wrong prose characterization, one altered quote, both files over length, several unlabeled inferences, and five claims that cannot be graded mechanically).

---

## 1. Skeleton compliance

**business.md**

| Requirement (§6) | Status |
|---|---|
| `# <Company> — The Business` | OK (`# Alphabet Inc. — The Business`) |
| `_As of <QLABEL>. Written <date>._` | OK (`_As of Q1 2026. Written 2026-09-07._`) |
| §1 What they do (incl. short history paragraph) | OK, history paragraph present (line 10) |
| §2 How the money comes in (5-year segment table) | OK, FY2021–FY2025 + Q1 2026 |
| §3 The economics (table: revenue, GM, OM, capex, capex/revenue) | OK, plus depreciation and TAC-rate rows and a segment-margin table |
| §4 How profitable, really (table, 5 years) | OK |
| §5 Why customers don't leave | OK |
| §6 What could break it (ranked; concentration) | OK, five scenarios ranked, concentration paragraph present |
| §7 Who runs it and what they do with the cash | OK |
| §8 Indicators worth tracking (5–8, name/why/where) | OK, 8 indicators, each with source location |
| `_Proposed — owner to review and lock._` | OK (line 121) |
| Glossary | OK, 5 one-sentence entries |
| Sources | OK, all 7 tags mapped to cached files |
| Heading order | OK |
| Length 2,000–3,000 words | **DEVIATION**: 4,368 words total; 3,650 excluding table rows and the Sources list. Roughly 25–45% over target. |

**outlook.md**

| Requirement (§7) | Status |
|---|---|
| `# <Company> — Outlook as of <QLABEL>` | OK |
| `_Transcript source tier: ... Written <date>._` | OK (`company-published`, matches MANIFEST tier 1) |
| §1 This quarter in the indicators (one row per indicator; this q / last q / expected) | OK, 8 rows matching business.md §8. "Last quarter" column is labelled "Prior" and mixes Q4 2025, Q1 2025 and FY2025 bases because Q4 2025 figures are not in the cached sources; each cell says which. Acceptable, but see REVISE item 11. |
| §2 What management says | OK |
| §3 Growth engines (what / how big / claim / working-or-not) | OK, five engines |
| §4 Guidance, verbatim | OK, all seven bullets verbatim (checked word for word below) |
| §5 Claims to verify | OK, 11 claims (target 6–12) |
| §6 Tone shift | Correctly omitted (first run) |
| Sources | OK |
| Length 800–1,200 words | **DEVIATION**: 1,803 words total; 1,342 excluding table rows and Sources. |

No missing or misordered headings in either file.

---

## 2. Citation spot-check

Legend: PASS = number/quote found in the tagged source; FAIL = not in the tagged source, or tagged to the wrong source; UNVERIFIABLE = cannot be checked from cached files. Computed cells were re-derived from the sourced inputs.

### 2(a) business.md §2 table (lines 14–24) — every cell

Inputs: FY2021–FY2023 from `10-K-FY2023.txt` Note 2 (lines 2082–2100); FY2024–FY2025 from `10-K-FY2025.txt` Item 7 revenue table (lines 1002–1020); Q1 2026 from `10-Q-2026-Q1.txt` Item 2 (lines 2137–2155). Tags on line 26 match these locations.

| Row | FY21 | FY22 | FY23 | FY24 | FY25 | Q1 26 | Source values (USD m) | Result |
|---|---|---|---|---|---|---|---|---|
| Search & other | 149.0 | 162.5 | 175.0 | 198.1 | 224.5 | 60.4 | 148,951 / 162,450 / 175,033 / 198,084 / 224,532 / 60,399 | PASS ×6 |
| YouTube ads | 28.8 | 29.2 | 31.5 | 36.1 | 40.4 | 9.9 | 28,845 / 29,243 / 31,510 / 36,147 / 40,367 / 9,883 | PASS ×6 |
| Google Network | 31.7 | 32.8 | 31.3 | 30.4 | 29.8 | 7.0 | 31,701 / 32,780 / 31,312 / 30,359 / 29,792 / 6,971 | PASS ×6 |
| Subscriptions, platforms, devices | 28.0 | 29.1 | 34.7 | 40.3 | 48.0 | 12.4 | 28,032 / 29,055 / 34,688 / 40,340 / 48,030 / 12,384 | PASS ×6 |
| Google Services total | 237.5 | 253.5 | 272.5 | 304.9 | 342.7 | 89.6 | 237,529 / 253,528 / 272,543 / 304,930 / 342,721 / 89,637 | PASS ×6 |
| Google Cloud | 19.2 | 26.3 | 33.1 | 43.2 | 58.7 | 20.0 | 19,206 / 26,280 / 33,088 / 43,229 / 58,705 / 20,028 | PASS ×6 |
| Other Bets | 0.8 | 1.1 | 1.5 | 1.6 | 1.5 | 0.4 | 753 / 1,068 / 1,527 / 1,648 / 1,537 / 411 | PASS ×6 |
| Hedging gains (losses) | 0.1 | 2.0 | 0.2 | 0.2 | (0.1) | (0.2) | 149 / 1,960 / 236 / 211 / (127) / (180) | PASS ×6 |
| Total revenue | 257.6 | 282.8 | 307.4 | 350.0 | 402.8 | 109.9 | 257,637 / 282,836 / 307,394 / 350,018 / 402,836 / 109,896 | PASS ×6 |

54/54 PASS.

### 2(a) business.md §3 first table (lines 42–50) — every cell

| Row | Check | Result |
|---|---|---|
| Revenue ($B) | Same as §2 total row; income statements `10-K-FY2023.txt` l.1641, `10-K-FY2025.txt` l.1591, `10-Q` l.291 | PASS ×6 |
| Gross margin (computed) 56.9 / 55.4 / 56.6 / 58.2 / 59.7 / 62.4% | (Revenue − cost of revenues) / revenue. Cost of revenues 110,939 / 126,203 / 133,332 (`10-K-FY2023` l.1645); 146,306 / 162,535 (`10-K-FY2025` l.1595); 41,271 (`10-Q` l.295). Re-derived: 56.94 / 55.38 / 56.63 / 58.20 / 59.65 / 62.45% | PASS ×6, labelled "(computed)", inputs sourced, arithmetic right |
| Operating margin 31 / 26 / 27 / 32 / 32 / 36% | 26% and 27% stated `10-K-FY2023` l.977; 32%/32% stated `10-K-FY2025` l.948; 36% stated `10-Q` l.2085. FY2021 31% is not stated in the FY2023 10-K (its Item 7 only covers 2022–2023); computed 78,714 / 257,637 = 30.55% → 31% | PASS ×6, but the FY2021 cell should carry "(computed)" (REVISE item 10) |
| Capex ($B) 24.6 / 31.5 / 32.3 / 52.5 / 91.4 / 35.7 | Purchases of property and equipment 24,640 / 31,485 / 32,251 (`10-K-FY2023` l.1818); 52,535 / 91,447 (`10-K-FY2025` l.1772); 35,674 (`10-Q` l.468) | PASS ×6 |
| Capex / revenue (computed) 9.6 / 11.1 / 10.5 / 15.0 / 22.7 / 32.5% | Re-derived 9.56 / 11.13 / 10.49 / 15.01 / 22.70 / 32.46% | PASS ×6 |
| Depreciation of P&E ($B) 10.3 / 13.5 / 11.9 / 15.3 / 21.1 / 6.5 | 10,273 / 13,475 / 11,946 (`10-K-FY2023` l.1788); 15,311 / 21,136 (`10-K-FY2025` l.1742); 6,482 (`10-Q` l.440) | PASS ×6 |
| TAC rate 21.7% (computed) / 21.8 / 21.4 / 20.7 / 20.3 / 19.7% | FY2021: TAC 45,566 (`10-K-FY2023` l.1150) / Google advertising 209,497 (Note 2 l.2088) = 21.75%. 21.8%→21.4% stated l.1159; 20.7%→20.3% stated `10-K-FY2025` l.1097; 20.6%→19.7% stated `10-Q` l.2226 | PASS ×6 |
| Footnote: FY2023 depreciation cut $3.9B by six-year server life | `10-K-FY2023` l.1002 | PASS |

42/42 PASS (one labelling nit).

### 2(a) business.md §3 segment-margin table (lines 54–57) — every cell

Segment operating income / segment revenue. Inputs: `10-K-FY2023` Note 15 l.3565–3585 (Services 88,132 / 82,699 / 95,858 on 237,529 / 253,528 / 272,543; Cloud (2,282) / (1,922) / 1,716 on 19,206 / 26,280 / 33,088); `10-K-FY2025` Note 15 l.3705–3725 (Services 121,263 / 139,404 on 304,930 / 342,721; Cloud 6,112 / 13,910 on 43,229 / 58,705); Q1 2026 as reported `slides.txt` l.201 (45.3%) and l.241 (32.9%), also `10-Q` Note 15 l.1884–1898.

| Row | Re-derived | Result |
|---|---|---|
| Google Services 37.1 / 32.6 / 35.2 / 39.8 / 40.7 / 45.3% | 37.10 / 32.62 / 35.17 / 39.77 / 40.68 / 45.28% | PASS ×6 |
| Google Cloud (11.9) / (7.3) / 5.2 / 14.1 / 23.7 / 32.9% | −11.88 / −7.31 / 5.19 / 14.14 / 23.70 / 32.94% | PASS ×6 |

12/12 PASS.

### 2(a) business.md §4 table (lines 69–77) — every cell

| Row | Source values | Result |
|---|---|---|
| Operating cash flow 91.7 / 91.5 / 101.7 / 125.3 / 164.7 / 45.8 | 91,652 / 91,495 / 101,746 (`10-K-FY2023` l.1814); 125,299 / 164,713 (`10-K-FY2025` l.1768); 45,790 (`10-Q` l.464) | PASS ×6 |
| Capex | as §3 | PASS ×6 |
| Free cash flow (computed) 67.0 / 60.0 / 69.5 / 72.8 / 73.3 / 10.1 | 67,012 / 60,010 / 69,495 / 72,764 / 73,266 / 10,116; Q1 and FY2025 also match `slides.txt` l.297–299 | PASS ×6 |
| FCF / revenue (computed) 26.0 / 21.2 / 22.6 / 20.8 / 18.2 / 9.2% | 26.01 / 21.22 / 22.61 / 20.79 / 18.19 / 9.21% | PASS ×6 |
| Net income 76.0 / 60.0 / 73.8 / 100.1 / 132.2 / 62.6 | 76,033 / 59,972 / 73,795 (`10-K-FY2023` l.1663); 100,118 / 132,170 (`10-K-FY2025` l.1613); 62,578 (`10-Q` l.313) | PASS ×6 |
| Share buybacks 50.3 / 59.3 / 62.2 / 62.0 / 45.4 / 0 | `10-K-FY2023` Note 11 l.3087–3092 ($50.3B / $59.3B / $62.2B); `10-K-FY2025` Note 11 l.3168 and equity statement l.1693, 1711 (62,047 / 45,398); `10-Q` Note 11 l.1691–1693 (none). Note: these are the Note 11 / equity-statement basis (includes unsettled repurchases); the cash-flow lines read 61.5 / 62.2 / 45.7. Basis is consistent across all five years and the tag names Note 11, so acceptable. | PASS ×6 |
| Dividends paid 0 / 0 / 0 / 7.4 / 10.0 / 2.5 | No dividend line in FY2021–2023 cash flow; 7,363 / 10,049 (`10-K-FY2025` l.1794); 2,542 (`10-Q` l.490) | PASS ×6 |

42/42 PASS.

### 2(b) outlook.md §1 indicators table (lines 10–17) — every number

| Cell | Tag | Found | Result |
|---|---|---|---|
| Search & other +19% | Q1 2026 release | `press-release.txt` l.6 | PASS |
| FY2025 +13% (computed) | 10-K FY2025, Item 7 | 224,532 / 198,084 = 1.1335 (l.1002) | PASS |
| Cloud margin 32.9%; Q1 2025 17.8% | slides p.8 | `slides.txt` l.241 | PASS ×2 |
| FY2025 Cloud 23.7% (computed) | 10-K FY2025, Note 15 | 13,910 / 58,705 (l.3707, 3719) | PASS |
| Wiz "a low single digit percentage point" | call p.12–13 | `transcript.txt` l.540 | PASS |
| $462.3B Cloud ($467.6B total); "just over 50%" | 10-Q Note 2 | l.609–616 | PASS ×3 |
| 12/31/2025 $242.8B; "just over 50%" | 10-K FY2025, Note 2 | l.2073–2078 | PASS ×2 |
| "just over 50% ... over the next 24 months" | call p.12 | l.506–507 | PASS |
| Capex $35.7B; 32.5%; depreciation $6.5B | 10-Q Item 1 / Item 2 | l.468, 440; l.2389 | PASS ×3 |
| Q4 2025 capex $27.9B; 24.5% (computed) | slides p.9; release | `slides.txt` l.261 (27,851); Q4 2025 revenue 113,828 `press-release.txt` l.429 → 24.47% | PASS ×2 |
| Q1 2025 depreciation $4.5B | 10-Q Item 2 | l.2389 | PASS |
| FY2026 capex $180–190B; 2027 "significantly increase" | call p.13 | l.547–558 | PASS ×2 |
| FCF $10.1B; TTM $64.4B | slides p.10 | l.297, 299 | PASS ×2 |
| Q4 2025 FCF $24.6B; TTM $73.3B | slides p.10 | l.297 (24,551), l.299 (73,266) | PASS ×2 |
| TAC rate 19.7%; Q1 2025 20.6% | 10-Q Item 2 | l.2226 | PASS ×2 |
| FY2025 TAC 20.3%; "to increase as our advertising revenues grow" | 10-K FY2025, Item 7 | l.1097; l.794 | PASS ×2 |
| ~350 million | release | l.23 | PASS |
| "more than a dozen new countries in Q2" | call p.9 | l.389 | PASS |
| 12,116M shares; $0; $69.5B | 10-Q Item 1 / Note 11 | l.266, 417; l.1691–1699 | PASS ×3 |
| 12,088M; FY2025 buybacks $45.4B | 10-K FY2025, Item 8 | l.1721; equity statement l.1711 (45,398) | PASS ×2 |
| Q1 2025 buybacks $15.1B; dividend +5% to $0.22 | release | l.279 (15,068); l.17 | PASS ×2 |

37/37 PASS.

### 2(c) Verbatim quotes, outlook.md §4 and §5 — word for word

| Quote (start) | Tag | Transcript / 10-Q lines | Result |
|---|---|---|---|
| "At current spot rates, we would expect to see an FX tailwind ... in the first quarter." | call p.12 | l.524–526 | PASS |
| "we are updating our full year 2026 CapEx guidance range to $180 to $190 billion ... which closed in March." | call p.13 | l.547–549 | PASS |
| "we expect our 2027 CapEx to significantly increase compared to 2026." | call p.13 | l.557–558 | PASS |
| "The majority of the backlog is related to typical GCP contracts, and we expect to recognize just over 50% ... 24 months." | call p.12 | l.505–507 | PASS |
| "We expect to begin recognizing a small percent of the revenues from these agreements later this year, with the vast majority of revenues to be realized in 2027." | call p.12 | l.529–531 | PASS |
| "First, Wiz will be reporting in the Google Cloud segment. And second, we expect a low single digit percentage point headwind ... related to the acquisition." | call p.12–13 | l.539–545 | PASS |
| "the significant increase in our investments in technical infrastructure will continue to put pressure on the P&L ... to support our AI products." | call p.13 | l.560–564 | PASS |
| Claim 1 quote (capex range fragment) | call p.13 | l.547–548 | PASS |
| Claim 2 quote (2027 capex) | call p.13 | l.557–558 | PASS |
| Claim 3 quote (just over 50%) | call p.12 | l.506–507 | PASS |
| Claim 4 quote (TPU timing) | call p.12 | l.529–531 | PASS |
| Claim 5 quote (Wiz headwind fragment) | call p.12–13 | l.540–541 | PASS |
| Claim 6 "By the end of Q1, YouTube Premium Lite was fully launched in 23 countries and we plan to launch in more than a dozen new countries in Q2." | call p.9 | l.388–389 | PASS |
| Claim 7 quote (FX tailwind fragment) | call p.12 | l.524–525 | PASS |
| Claim 8 "our Cloud revenue would have been higher if we were able to meet the demand." | call p.19 | l.859–860 | PASS |
| Claim 9 "will continue to put pressure on the P&L in the form of higher depreciation expense" | call p.13 | l.561–562 | PASS |
| Claim 10 "We expect to fund $10.0 billion in the second quarter of 2026 in the form of a non-marketable security." | 10-Q Item 2 | l.2424 | PASS |
| Claim 11 "AI continues to drive Search usage, and queries are at an all time high." | call p.4 | l.138–139 | PASS |

18/18 PASS. Other outlook quotes checked incidentally (§2–§3): "driving overall Search growth" l.141–142 p.4; "the expansionary moment we see here for Search" l.902 p.20; "significantly expanded our ability to deliver Ads on longer, more complex searches" l.704–705 p.16; "there is upside in that coverage number" l.702 p.16; "there may be different ways to accomplish that" l.1024 p.23; "across your Google user experience, including in Search" l.1028–1029 p.23; "we're not rushing anything here" l.882 p.20; "we are compute constrained in the near term. And as an example, our Cloud revenue would have been higher if we were able to meet the demand" l.858–860 p.19; "grew nearly 800% year over year" l.167 p.4; "a select group of customers in their own data centers" l.239–240 p.6; "multiple gigawatts" `10-Q` l.2104; "this was our strongest quarter ever for our consumer AI plans, primarily driven by adoption of the Gemini App" l.56–57 p.2; "Direct Offers in AI Mode" l.339–340 p.8. All PASS.

### 2(d) Prose sentences, business.md §5–§7 (plus §1–§4 sentences checked on the way)

| # | Sentence / figure | Tag | Found | Result |
|---|---|---|---|---|
| 1 | "other products and services are literally one click away" | 10-K FY2025, Item 1 | l.357 | PASS |
| 2 | TAC $59.9B in 2025 | 10-K FY2025, Item 7 | l.1088 (59,926) | PASS |
| 3 | Search remedy "requires Google to share certain search data with ... competitors" | 10-Q Note 10 | l.1651 | PASS (fact); the clause "a sign regulators regard that data as the hard-to-copy asset" is an unlabeled inference, see §3 |
| 4 | Brand "one of the most recognized in the world" | 10-K FY2025, Item 1 | l.266 | PASS |
| 5 | Ten million channels post Shorts daily; 200M hours/day on TV | call p.6 | l.245–249 | PASS |
| 6 | Led US streaming watch time three straight years | call p.9 | l.365–366 | PASS |
| 7 | American Express "hundreds of production applications" | call p.5 | l.208–210 | PASS |
| 8 | "the only provider to offer first party solutions across the entire Enterprise AI stack" | call p.4 | l.163–164 | PASS |
| 9 | Customers used 45% more than committed | call p.4 | l.174–175 | PASS |
| 10 | "consumers may change how they obtain information online" | 10-K FY2025, Item 1A | l.420 | PASS |
| 11 | "which could affect revenue growth rates and margin trends" | 10-K FY2025, Item 7 | l.781 | PASS |
| 12 | Google Services operating income > total (computed) | 10-K FY2025, Note 15 | 139,404 vs 129,039, l.3717, 3725 | PASS |
| 13 | Debt $77.5B from $10.9B at end-2024 | 10-Q Item 1; 10-K FY2025 Item 8 | l.250; l.1552 | PASS |
| 14 | $75.6B leases not yet commenced | 10-Q Item 2 | l.2392 | PASS |
| 15 | $232.7B commitments, payments through 2047 | 10-Q Note 10 | l.1602–1609 | PASS |
| 16 | "expected technology advancements" | 10-K FY2025, Item 1A | l.401 | PASS (quote); "could shorten" is a paraphrase of "could change the period", see §3 |
| 17 | Search judgment Dec 2025; quoted remedy sentence; appeals Jan/Feb 2026 | 10-Q Note 10 | l.1651 | PASS |
| 18 | Ad-tech: "unfairly excluded rivals"; "structural remedies that could have a material adverse effect on our business" | 10-Q Note 10 | l.1654 | PASS |
| 19 | Ad-tech: the company "is awaiting a final judgment" | 10-Q Note 10 | l.1654 reads "we are awaiting a final judgment" | **FAIL** (quoted words altered: "is" for "are"; either paraphrase without quotation marks or quote "we are awaiting a final judgment") |
| 20 | TAC rate on Search "substantially consistent" | 10-Q Item 2 | l.2226 | PASS |
| 21 | Cloud 63%; "would have been higher if we were able to meet the demand" | release; call p.19 | l.8; l.859–860 | PASS |
| 22 | Cloud 14.6% of revenue, 10.8% of operating income (computed) | 10-K FY2025, Note 15 | 58,705/402,836; 13,910/129,039 | PASS |
| 23 | No customer >10% in 2023–2025 | 10-K FY2025, Note 2 | l.2049–2050 | PASS |
| 24 | "a small number of qualified suppliers" | 10-K FY2025, Item 1A | l.438 | PASS |
| 25 | "may incur additional liabilities, have excess capacity that we cannot easily redeploy" | 10-Q Part II Item 1A | l.2477 | PASS |
| 26 | Pichai 53, joined 2004, CEO Google Oct 2015 / Alphabet Dec 2019 | DEF 14A 2026 | l.520 | PASS |
| 27 | Ashkenazi 53, CFO since July 2024, ex-Eli Lilly; Porat President & CIO | DEF 14A | l.582, 584 | PASS |
| 28 | Hennessy independent chair; Page 27.4%, Brin 25.3%, group 54.3% | DEF 14A | l.526–528; l.838, 840, 866 | PASS |
| 29 | Salaries $2.0M / $1.0M; bonus discontinued Feb 2025 | DEF 14A | l.1097; l.1113, 1295 | PASS |
| 30 | GSUs vest over three years; PSUs 0–200% on TSR vs S&P 100; only measure | DEF 14A | l.1136; l.1137; l.1559 | PASS |
| 31 | CEO award every three years; $84M GSU + two $63M PSU tranches; Waymo ~$130M, Wing ~$45M | DEF 14A | l.1147–1151 | PASS |
| 32 | "the primary use of capital continues to be to invest for the long-term growth of the business" | 10-K FY2025, Item 7 | l.1225 | PASS |
| 33 | Buybacks $62.0B → $45.4B → 0; $69.5B unused | 10-K Note 11; 10-Q Note 11 | l.3168, 3153–3155; l.1691–1699 | PASS |
| 34 | Shares 13,242M (2021) → 12,088M (2025) → 12,116M (3/31/26) | 10-K FY2023 Item 8; 10-K FY2025 Item 8; 10-Q Item 1 | l.1737; l.1721; l.417 | PASS |
| 35 | Dividend raised 5% to $0.22 in April 2026 | 10-Q Note 11 | l.1712–1718 | PASS |
| 36 | Net bond proceeds $37.3B in 2025 | 10-K FY2025, Item 7 | l.976 | PASS |
| 37 | Net bond proceeds $31.1B in Q1 2026 | 10-Q Q1 2026, Note 6 | Note 6 (l.1235–1253) gives face amounts by currency only; the $31.1B net figure is at Item 2 l.2116 (and release l.96) | **FAIL** (right number, wrong note) — fixed directly by adding `[10-Q Q1 2026, Item 2]` |
| 38 | Wiz $29.5B in Google Cloud; Intersect $5.9B | 10-Q Note 8 | l.1475–1477; l.1508–1510 | PASS |
| 39 | $40.0B commitment: $10.0B up front (Q2 2026), $30.0B contingent | 10-Q Item 2 | l.2106, 2424 | PASS |
| 40 | Up to $33.3B backstops; ~$15.3B signed April 2026 | 10-Q Item 2 | l.2423 | PASS |
| 41 | §1: "paid clicks" definition | 10-K FY2025 Item 7 **and** Q1 2026 call p.7 | Item 7 l.836 supports it; transcript p.7 (l.274–318) never mentions paid clicks | **FAIL** (second tag unsupported) — fixed directly by removing the call tag |
| 42 | §1: Google DeepMind builds Gemini; cost not charged to any segment | 10-K FY2025, Note 15 | FY2025 Note 15 l.3686–3688 supports "shared AI R&D not allocated" but never names DeepMind; the name is in `10-K-FY2023` Note 15 l.3553–3554 | **FAIL** (partial) — fixed directly by adding `[10-K FY2023, Note 15]` |
| 43 | §1: 15 half-billion-user products on Gemini; "AI-first" since 2016; 52.7% voting power | 10-K FY2025 Item 1 / 1A | l.255; l.240; l.598–599 | PASS |
| 44 | §1: 73% advertising, 56% Search (computed) | 10-K FY2025, Item 7 | 294,691 and 224,532 / 402,836 | PASS |
| 45 | §2: paid clicks +13%, cost-per-click +5% | 10-Q Item 2 | l.2170–2172 | PASS |
| 46 | §2: 350M subscriptions; subs line +19% | call p.2; release | l.56–59; l.7 | PASS |
| 47 | §2: US 48%, EMEA 29% of 2025 revenue | 10-K FY2025, Item 7 | l.1062–1064 | PASS |
| 48 | §3: revenue +56% 2021–2025 (computed); "relatively fixed and may not correlate to changes in revenue" | 10-K FY2023/FY2025 Item 8; Item 1A | 402,836/257,637 = 1.564; l.423 | PASS |
| 49 | §3: R&D 15%, S&M 7%, G&A 5% of revenue | 10-K FY2025, Item 7 | l.1108, 1120, 1132 | PASS |
| 50 | §3: "depreciation, energy, equipment, and network capacity" ... "are expected to significantly increase as developing and serving AI offerings require more compute power than our historical consumer and enterprise offerings" | 10-K FY2025, Item 7 | l.787 | PASS |
| 51 | §3: Q1 depreciation +44% (computed); AI answer cost down >30% | 10-Q Item 2; call p.4 | 6,482/4,487 = 1.445; l.155–157 | PASS |
| 52 | §4: FCF −47%, TTM $64.4B −14% | slides p.10 | l.297–299 | PASS |
| 53 | §4: equity gains $24.1B (2025) and $36.9B (Q1 2026); July 2025 tax law in operating cash flow | 10-K Item 7; 10-Q Item 2 | l.978, 982; l.2118 | PASS |
| 54 | §4: 66c and 52c operating profit per $ of P&E (computed) | 10-K FY2025, Item 8 | 112,390/171,036 = 0.657; 129,039/246,597 = 0.523 (l.1526, 1605) | PASS |
| 55 | §4: $126.8B cash and marketable securities; $77.5B long-term debt | 10-Q Item 1 | l.210, 250 | PASS |

**Citation tally:** 55 prose checks + 150 business.md table cells + 37 indicator cells + 18 verbatim quotes = 260 checks. **256 PASS, 4 FAIL, 0 UNVERIFIABLE.** Three of the four failures are tag problems with the right number (fixed directly); one is an altered quote (REVISE item 4). None of the four came from a wrong note: `notes-filings.md` l.354 and `notes-ir.md` l.103 tag the $31.1B correctly; the DeepMind and paid-clicks tags were writer errors.

---

## 3. Invented-number and inference check

No figure was found without a source tag, and no figure was found that its tag does not support after the three tag fixes above. The following are interpretations presented as fact, or statements that overstate what the source says:

| File:line | Text | Problem |
|---|---|---|
| business.md:40 | "operating margin held around 31–32%" over 2021–2025 | Wrong as written. The table two lines below shows 31%, 26%, 27%, 32%, 32%. It dipped five points in 2022 and recovered. The sentence should say that (e.g., "operating margin dipped to 26–27% in 2022–2023 and returned to 32%"). This is the one place where prose contradicts the report's own numbers. |
| business.md:65 | "Put simply: a classic search rode almost free on machines already paid for; an AI answer needs far more computing per question, and the company is buying that computing years ahead of the revenue it hopes will follow." | Interpretation stated as fact. Supported in spirit by the Item 7 quote just before it, but should be labelled ("our inference:" or "this suggests"). |
| business.md:81 | "because almost every extra dollar of operating cash went into servers and data centers" | Inference from the table (OCF +$73B, capex +$67B over 2021–2025). Fair, but label it. |
| business.md:85 | "each new dollar of machinery is earning less than the old ones did" | Inference from the two return-on-capital figures; label it. |
| business.md:89 | "a sign regulators regard that data as the hard-to-copy asset" | Inference about a court's reasoning, stated as fact, tagged to Note 10 which says nothing of the kind. Label as inference or cut. |
| business.md:91 | "A rival would need both sides at once." | Inference; label. |
| business.md:93 | "once a data platform ... has moved, as American Express is doing, moving back is slow and expensive" | Inference stated as fact; the transcript only says AmEx is moving to BigQuery. Label. |
| business.md:101 | "'expected technology advancements' could shorten the assumed life of its equipment, raising depreciation further" | Source (Item 1A l.401) says such changes "could change the period over which we expect to benefit from the asset"; it does not say shorten. Rephrase ("could change, most likely shorten, ...") and label the direction as inference. |
| business.md:105 | "no partner is named in any filing" | True for the cached 10-K and 10-Q (no "Apple" or "Samsung" anywhere in either), but "any filing" is broader than what was checked. Say "in the 10-K or 10-Q". |
| business.md:36; outlook.md:12 | Backlog $462.3B vs $242.8B at year end, presented as like-for-like | `10-Q` Note 2 l.618–619: from Q1 2026 the company changed the backlog definition to include contracts of one year or less, worth about $7.3B. Not an invented number, but a comparability caveat that must be stated (same rule as the Marvell end-market lesson in AGENTS.md §17). |
| business.md:6 | "On YouTube, 'brand advertising' is video ads meant to be seen rather than clicked" | Slight narrowing of the source (Item 1 l.281–282: "videos, text, images, and other interactive ads" across properties). Acceptable simplification, but drop "video" or say "mostly video". |
| outlook.md:31 | "first hardware revenue counted in the second half of 2026" | Management said "later this year" (p.12) and the 10-Q says "later in 2026" (l.2007). From an April call that could include Q2. Say "later in 2026". |
| outlook.md:21 | "asked about showing ads on more than the historical roughly 20% of queries" | The 20% is the analyst's figure (l.652), not management's; the sentence attributes it correctly as the question, so PASS, but it would be safer to say "an analyst's figure of about 20%". |

---

## 4. Jargon and readability audit

Read as a smart 16-year-old with no finance or industry background. Items marked FIXED were changed directly (see "Fixed directly"); the rest go to the writer.

### (a) Undefined terms, not in glossary, not obvious from the name

| File:line | Term | Status |
|---|---|---|
| business.md:23 | "Hedging gains (losses)" | FIXED (added "(currency-protection contracts)") |
| business.md:45–46 | "Gross margin", "Operating margin" | FIXED (one-line glosses at first prose use, line 40) |
| business.md:47 | "Capex" | FIXED (row label now says capital spending on servers, data centers, buildings) |
| business.md:61 | "Cost of revenues" | FIXED |
| business.md:65 | "guided to" | FIXED ("told investors to expect") |
| business.md:71 | "Operating cash flow" | Open. One phrase needed at first use ("cash the business itself brought in during the year"). |
| business.md:81 | "trailing-twelve-month" | FIXED ("last four quarters combined") |
| business.md:85 | "marketable securities" | FIXED |
| business.md:103 | "syndication services" (inside a verbatim quote) | Open. Add a plain gloss after the quote (letting rivals show Google's results or ads on their own sites), or drop that clause from the quote with an ellipsis. |
| business.md:103 | "publisher tools" | Open. Gloss: the software website owners use to sell ad space. |
| business.md:109 | "counterparties" | FIXED |
| business.md:115 | "S&P 100", "tranches" | FIXED |
| business.md:117 | "backstops" | FIXED |
| business.md:130 | "dilution" | FIXED |
| outlook.md:10 | "Y/Y" | Open. Write "year over year" once. |
| outlook.md:41 | "EPS" | FIXED |
| outlook.md:43, 48 | "FX", "tailwind", "headwind" (inside verbatim quotes) | FIXED with glosses in the bullet labels, outside the quotes |
| outlook.md:59 (claim 7) | "constant-currency growth" | Open (claims may not be reworded by the reviewer). Add a parenthetical: growth with currency swings stripped out, as reported in the press-release reconciliation. |
| outlook.md:62 (claim 10) | "non-marketable security" | Open (claim). Gloss: a stake in a private company that cannot be sold on an exchange. |
| outlook.md:31 | "credit backstops" | Open. Same gloss as business.md:117. |

### (b) Glossary entries

All five entries (TPU, Backlog, TAC, Depreciation, Free cash flow) are one sentence, plain, and each is used repeatedly in the argument. None should be cut. "Backlog" is also defined inline at business.md:36, which is fine. No addition is required if the inline glosses above stay; if the writer prefers, "Gross margin / Operating margin" could move to the glossary instead.

### (c) Sentences assuming prior knowledge

| File:line | Issue | Status |
|---|---|---|
| business.md:89, 103 | What an antitrust remedy is | FIXED (glosses added at both places) |
| business.md:103 | "final judgment", "appealed", "structural remedies" | Partly covered by the new gloss and by "whether it orders a sale of any business"; acceptable. |
| outlook.md:31, 46, 47 | "recognize revenue" / "recognizing ... revenues" | Prose use FIXED ("counted"); the two verbatim quotes still say "recognize". Add "(recognize = count as revenue)" to the Backlog bullet label. |
| outlook.md:49 | "P&L = income statement" assumed the reader knows what an income statement is | FIXED |
| business.md:65 | "compute power" (quote) | Acceptable, meaning obvious in context. |
| business.md:93 | "Enterprise AI stack" (quote) | Explained immediately after the quote. OK. |

### (d) Banned words outside verbatim quotes

Scanned both files for leverage, synergy, headwind, tailwind, monetize, ecosystem, at scale, robust, unlock. **None outside quotes.** "tailwind(s)" (outlook.md:43, 59) and "headwind" (outlook.md:48, 57) occur only inside management's verbatim guidance; glosses now sit outside the quotes.

### Paragraphs that are mostly numbers / tables that have become walls

- business.md:117 ("**Cash.**"): one paragraph carrying buybacks (3 figures), share counts (3), dividend, debt (4), two acquisitions, a $40B/$10B/$30B commitment and two backstop figures. This is a numbers paragraph and should be a small table (item | amount | date | source) with two sentences of meaning. REVISE item 3.
- business.md:101 (scenario 2) is number-heavy but argumentative; acceptable if the $75.6B / $232.7B / $77.5B figures are trimmed to the two that matter.
- outlook.md §1 table: cells carry two or three figures plus two tags each. Readable, but the "Prior" column mixes three different bases. Not a wall; see REVISE item 11.
- business.md §3 first table (7 rows) and §4 table (7 rows) are fine.

---

## 5. Claims quality (outlook.md §5)

Count: 11 (target 6–12). Mix is right: only one claim (7) is headline revenue-adjacent; the rest are capex, backlog, margin, product, depreciation, and management-statement checks. Every quote sits under its claim and is verbatim.

| # | One sentence, one thing? | Tied to metric/date/event? | Quote supports it? | Gradable without judgment? | Verdict |
|---|---|---|---|---|---|
| 1 | No, two things ("consistent with" and "not cut") | Range: yes. "Consistent with" the full-year range: no threshold given | Yes | No. What Q2 figure is "consistent" with $180–190B when Q1 was $35.7B? Needs a number or should be dropped, keeping "range reaffirmed or raised" | **Sharpen** |
| 2 | Yes | Event on Q2 call | Yes | Yes (met / dropped) | OK |
| 3 | Yes | 10-Q Note 2 wording | Yes | Yes | OK |
| 4 | No, two things | First half not observable: TPU hardware revenue is not broken out anywhere in the sources, so "no material TPU hardware revenue" cannot be checked | Second half yes | No for first half | **Sharpen** to the management statement only, or to "10-Q Item 2 still says revenue begins later in 2026 with the majority in 2027" |
| 5 | No, two things; "a few percentage points" is vague | Metric yes | Only partly. The quote says Wiz is a 1–3 point drag on what the margin would otherwise be; it does not say Q2 margin will be within a few points of Q1's 32.9% (margins also move with mix and seasonality) | No | **Rewrite** with a numeric floor stated as a proxy (e.g., "Q2 Cloud operating margin ≥ 29.9%, i.e. Q1 minus three points") or as a statement check ("management again attributes Cloud margin pressure to Wiz") |
| 6 | Yes | 36 countries by end Q2 (23 + at least 13) | Yes | Yes if disclosed; otherwise ⏳ | OK |
| 7 | Yes | Press-release reconciliation, ~1 point | Yes | Yes ("about" = ±0.5 pt is a reasonable convention; state it) | OK, add gloss for "constant-currency" |
| 8 | Either/or: "again describes Cloud as supply-constrained, or says the constraint has eased" | Event | Yes | No: both outcomes are "met", so the claim can never be missed. Only silence would be a verdict (dropped) | **Rewrite** as one direction: "Management again says Q2 Cloud revenue was limited by available capacity." Then met / missed (they say it has eased) / dropped |
| 9 | Yes | Q2 depreciation > $6.5B | Yes | Yes | OK |
| 10 | Yes | $10.0B funded, Q2 10-Q | Yes | Yes | OK, add gloss for "non-marketable security" |
| 11 | Either/or again ("again says ... all-time high, or gives a query-growth figure") | Event | Yes | Mostly. "Dropped" is the real signal here and it is gradable, but the "or" makes "missed" impossible | **Tighten** to "Management again says Search queries are at an all-time high" |

Predictability (rubric Q4): from claims 2, 3, 6, 7, 9, 10 a refresh agent knows exactly what to look up. Claims 1, 4, 5, 8, 11 need rewording before they are mechanical.

---

## 6. Rubric (§14)

1. **Can I explain what this company does, and who pays it, in two sentences?** Yes. §1 says it in three sentences: free products, advertisers pay per click, and companies pay Cloud by usage.
2. **Do I know exactly what would kill it, and what the early warning sign is?** Yes. §6 ranks five scenarios and gives a concrete early warning for each (Search growth slowing for two quarters with more subscription talk; backlog flattening while capex rises; the search appeal and ad-tech remedy rulings; TAC rate jump; backlog stalling).
3. **Do I know why the margins are what they are, and whether cost scales with usage?** Yes, with one blemish. §3 explains the fixed-cost search engine, TAC as the price of distribution, and the shift to heavy depreciation clearly; but line 40's "held around 31–32%" contradicts the table beneath it and must be fixed before this is a clean yes.
4. **Could I predict what the scorecard will check next quarter, from §5 alone?** Partly. Six of eleven claims are mechanical; five need a threshold or a single direction.
5. **Did nothing in the report require knowledge I don't have?** Not yet. Before this review roughly fifteen terms were unexplained (FX, tailwind, hedging, gross/operating margin, trailing twelve months, marketable securities, counterparties, tranches, dilution, backstop, antitrust remedy, EPS, capex, recognized revenue, income statement). Most are now glossed; still open: syndication services, publisher tools, constant-currency, non-marketable security, operating cash flow, Y/Y.

---

## 7. Verdict: REVISE

1. **business.md:40** — Replace "operating margin held around 31–32%" with wording that matches the table: dipped to 26% in 2022 and 27% in 2023, back to 32% in 2024–2025. Keep the tags.
2. **Length** — Cut business.md to 3,000 words or fewer (currently 4,368; 3,650 excluding tables) and outlook.md to 1,200 or fewer (currently 1,803; 1,342 excluding tables). Candidates: the second and third sentences of each §6 scenario, the §5 "sign it is weakening" lists (keep one or two signs each), the §7 "Cash." paragraph once it is a table, outlook §2's third paragraph, and outlook §3 Waymo block.
3. **business.md:117** — Turn the "Cash." paragraph into a small table (item | amount | date | tag): buybacks 2024/2025/Q1, share count 2021/2025/3-31-26, dividend, long-term debt 12-31-24/3-31-26, bond proceeds 2025/Q1 2026, Wiz, Intersect, $40B commitment, $33.3B backstops. Keep two sentences of prose on what it means.
4. **business.md:103** — Fix the altered quote: either quote exactly ("we are awaiting a final judgment") or paraphrase without quotation marks.
5. **business.md:36 and outlook.md:12** — Add the backlog definition change: from Q1 2026 backlog includes contracts of one year or less (about $7.3B at 3/31/26) [10-Q Q1 2026, Note 2], so the $242.8B → $462.3B comparison is not exactly like-for-like.
6. **Label inferences** at business.md:65 ("Put simply..."), :81 ("because almost every extra dollar..."), :85 ("each new dollar of machinery..."), :89 ("a sign regulators regard..."), :91 ("A rival would need both sides"), :93 ("moving back is slow and expensive"), :101 ("could shorten" → "could change, most likely shorten"). Use "our inference:" or "this suggests". Change :105 "any filing" to "the 10-K or 10-Q".
7. **outlook.md:31** — "second half of 2026" → "later in 2026" (management's words).
8. **Claims** (outlook.md §5): rewrite 1 (drop "consistent with" or give a Q2 dollar threshold; keep "range reaffirmed or raised"), 4 (management-statement check only; TPU hardware revenue is not disclosed separately), 5 (numeric floor stated as a proxy, or a statement check), 8 (one direction: "again says Cloud revenue was limited by capacity"), 11 (drop the "or gives a query-growth figure"). Add glosses to 7 ("constant-currency" = growth with currency swings removed, from the press-release reconciliation) and 10 ("non-marketable security" = a stake in a private company).
9. **Remaining jargon**: gloss "syndication services" and "publisher tools" (business.md:103), "operating cash flow" (business.md:71, first use), "credit backstops" (outlook.md:31), "Y/Y" (outlook.md:10), and add "(recognize = count as revenue)" to the outlook §4 Backlog bullet label.
10. **business.md:46** — Mark the FY2021 operating-margin cell "31% (computed)"; the FY2023 10-K states only 2022 and 2023.
11. **outlook.md §1 "Prior" column** — Either relabel the column "Prior (basis varies, see cell)" or add a one-line note that Q4 2025 segment figures are not in the cached sources so the year-ago quarter or full year is used. Optional but helps the refresh agent build the time series.
12. **business.md:6** — "video ads meant to be seen rather than clicked" → "ads (mostly video) meant to be seen rather than clicked", per Item 1 l.281–282.

Items 1, 4 and 5 are factual and must change. Items 2, 3, 6, 7, 8 make the report usable by the refresh agent. Items 9–12 are polish.

---

## Fixed directly

Tags (correct tag unambiguous from the cached source):
- business.md:6 — removed `[Q1 2026 call, p.7]` from the paid-clicks sentence; the transcript page does not mention paid clicks; `[10-K FY2025, Item 7]` (l.836) remains.
- business.md:8 — added `[10-K FY2023, Note 15]` (l.3553–3554 names Google DeepMind within Alphabet-level activities) alongside `[10-K FY2025, Note 15]`.
- business.md:117 — added `[10-Q Q1 2026, Item 2]` (l.2116) for the $31.1B net note proceeds, which Note 6 does not state.

Jargon replaced or glossed with meaning unchanged (no numbers, quotes, claims, indicators or structure touched):
- business.md:23 table label "Hedging gains (losses)" → added "(currency-protection contracts)".
- business.md:40 glosses for gross margin and operating margin.
- business.md:47 table label "Capex ($B)" → "Capex (capital spending on servers, data centers, buildings) ($B)".
- business.md:61 "Cost of revenues" → added "(the direct cost of delivering the service)".
- business.md:65 "has guided to" → "has told investors to expect".
- business.md:81 "the trailing-twelve-month figure of $64.4 billion" → "the figure for the last four quarters combined, $64.4 billion,".
- business.md:85 "cash and marketable securities" → "cash and quickly sellable investments (marketable securities)".
- business.md:89 "search remedy" → added "(the changes the court ordered after ruling that Google had broken competition law)".
- business.md:103 added a one-sentence gloss of antitrust law and remedy after the scenario heading.
- business.md:109 "if counterparties fail" → "if the other parties to those deals fail".
- business.md:115 "PSU tranches" → "PSU pieces (tranches)"; "S&P 100" → added "(an index of 100 large US companies)".
- business.md:117 "backstops" → added "(promises to cover payments if a project owner cannot)".
- business.md:130 "dilution is paying" → "newly issued shares (each existing share then owns a smaller slice) are paying".
- outlook.md:31 "revenue recognized" → "revenue counted".
- outlook.md:41 "EPS" → "EPS (earnings per share)".
- outlook.md:43 bullet label → "FX (currency swings), Q2; a "tailwind" here is a boost from exchange rates" (quote untouched).
- outlook.md:48 bullet label → "Wiz (a "headwind" is a drag on the margin)" (quote untouched).
- outlook.md:49 bullet label → "P&L = income statement, the profit-and-loss report".

No typos found. Word counts after fixes: business.md 4,368; outlook.md 1,803.

---

## Cycle 2 (focused re-check of the writer's second pass, 2026-09-07)

_Same as-of rule observed: `sources/2026-Q2/` was not opened, listed, or grepped. Line numbers refer to the revised drafts and the cached Q1 `.txt` files._

### 1. REVISE list — resolution

| # | Item | Status |
|---|---|---|
| 1 | business.md:40 operating-margin wording | **Resolved.** Now reads "went from 31% to 32%, with a dip to 26–27% in 2022–2023", matching the table; adds the 2023 severance and office-exit charges (verified below). |
| 2 | Length | **Resolved.** Prose excluding tables, glossary, sources and tags: business.md 2,969 words (target 2,000–3,000); outlook.md 1,189 (target 800–1,200). |
| 3 | §7 "Cash." paragraph → table | **Resolved.** Ten-row table at business.md:119–130 with two sentences of prose before and one labelled inference after. |
| 4 | Altered quote | **Resolved.** business.md:103 now quotes "we are awaiting a final judgment" (10-Q Note 10 l.1654). |
| 5 | Backlog definition change | **Resolved.** business.md:36 and outlook.md:12 both state that from Q1 2026 backlog includes contracts of one year or less, about $7.3B. |
| 6 | Label inferences (:65, :81, :85, :89, :91, :93, :101; "any filing" at :105) | **Resolved.** All seven carry "Our inference" / "This suggests"; :101 now says the useful life "could change" with the shortening labelled as inference; :105 says "in the 10-K or 10-Q". |
| 7 | outlook.md:31 "second half of 2026" | **Resolved.** Sentence rewritten; the timing now lives only in claim 4 with management's own words. |
| 8 | Claims 1, 4, 5, 8, 11 rewritten; glosses on 7 and 10 | **Resolved.** See §5 below. |
| 9 | Remaining jargon (syndication, publisher tools, operating cash flow, credit backstops, Y/Y, recognize) | **Resolved.** Glosses at business.md:103 (two), :71 (table label), outlook.md:31, :10 ("year over year"), :46 ("recognize = count as revenue"). |
| 10 | FY2021 operating margin "(computed)" | **Resolved.** business.md:46. |
| 11 | outlook §1 "Prior" column basis | **Resolved.** Column header now "Prior (basis varies; see cell)" and the intro sentence explains why. |
| 12 | "video ads" → "ads (mostly video)" | **Resolved.** business.md:6. |

12 of 12 resolved.

### 2. New or changed numbers and quotes

| Item (file:line) | Tag | Found in cached source | Result |
|---|---|---|---|
| $2.1B severance and $1.8B office-exit charges, 2023 (business.md:40) | 10-K FY2023, Item 7 | `10-K-FY2023.txt` l.1000: "employee severance and related charges of $2.1 billion ... exit charges recorded during the year ended December 31, 2023, were $1.8 billion" (Item 7 spans l.792–1409) | PASS |
| "$7.3 billion" sub-one-year backlog (business.md:36; outlook.md:12) | 10-Q Q1 2026, Note 2 | `10-Q-2026-Q1.txt` l.618–620: "approximately $7.3 billion" | PASS |
| FY2021 operating margin "31% (computed)" (business.md:46) | 10-K FY2023, Item 8 | 78,714 / 257,637 = 30.55% (l.1655, 1641) | PASS |
| §7 table row 1: buybacks $62.0B → $45.4B → $0 | 10-K FY2025 Note 11; 10-Q Note 11 | l.3168 (62,047 / 45,398); l.1691–1693 (none) | PASS |
| Row 2: $69.5B unused authorization, 3/31/2026 | 10-Q Note 11 | l.1697–1699 | PASS |
| Row 3: shares 13,242M → 12,088M → 12,116M | 10-K FY2023 Item 8; 10-K FY2025 Item 8; 10-Q Item 1 | l.1737; l.1721; l.417 | PASS |
| Row 4: dividend first paid 2024; $0.21 → $0.22 (+5%), April 2026 | 10-K FY2025 Item 8; 10-Q Note 11 | cash-flow l.1794 (0 / 7,363 / 10,049); l.1712–1718 | PASS |
| Row 5: long-term debt $10.9B → $46.5B → $77.5B (the $46.5B is new) | 10-K FY2025 Item 8; 10-Q Item 1 | l.1552 (10,883 / 46,547); l.250 (46,547 / 77,501) | PASS |
| Row 6: net bond proceeds $37.3B (2025); $31.1B (Q1 2026) | 10-K FY2025 Item 7; 10-Q Item 2 | l.976; l.2116 | PASS |
| Row 7: Wiz $29.5B, closed 3/11/2026, inside Google Cloud | 10-Q Note 8 | l.1475–1477 | PASS |
| Row 8: Intersect $5.9B, closed 3/10/2026 | 10-Q Note 8 | l.1508–1510 | PASS |
| Row 9: $40.0B = $10.0B up front (Q2 2026) + $30.0B on milestones, March 2026 | 10-Q Item 2 | l.2106, 2424 | PASS |
| Row 10: backstops up to $33.3B, ~$15.3B signed April 2026 | 10-Q Item 2 | l.2423 | PASS |
| business.md:132 inference: share count rose because employee stock issuance was no longer offset by buybacks | 10-Q Item 1 | equity statement l.403 "Stock issued 28", no repurchase line; 12,088 → 12,116 | PASS (labelled inference, supported) |
| business.md:36 "The United States supplied 48% of 2025 revenue" | 10-K FY2025, Item 7 | l.1062 | PASS |
| Claim 4 quote "We expect to begin recognizing revenues from these agreements later in 2026, with the significant majority to be recognized in 2027." | 10-Q Item 2 | l.2007 (also l.2104), word for word | PASS |
| Claim 5 "at least 29.9%" = 32.9% − 3 points | slides p.8; call p.12–13 | 32.9% at `slides.txt` l.241; "low single digit percentage point headwind" l.540–541; 32.9 − 3.0 = 29.9 | PASS (derivation stated in the claim; three-point ceiling is a stated convention) |
| "we are awaiting a final judgment" (business.md:103) | 10-Q Note 10 | l.1654 | PASS |
| Q1 2026 depreciation $6.5B (outlook.md:13; business.md:49) | 10-Q Item 1 / Item 2 | l.440 (6,482); l.2389 | PASS, unchanged |
| outlook.md:21 "an analyst's figure of about 20%" | call p.16 | l.652 (Doug Anmuth's question) | PASS |

21/21 PASS. No unsourced figure introduced. The one untagged factual sentence added is business.md:117 ("buybacks stopped, debt rose, and cash went into servers, acquisitions, and stakes in other companies"), which summarizes the fully tagged table directly beneath it; acceptable.

### 3. Cycle-1 direct edits

All 22 intact. Two were carried into the writer's restructuring rather than sitting at their original line: the $31.1B `[10-Q Q1 2026, Item 2]` tag and the backstop gloss now live in the §7 table (rows 6 and 10); the outlook.md:31 "counted" wording was superseded because the writer rewrote that sentence and it no longer uses "recognized". The remaining 19 are unchanged in place (business.md:6, :8, :23, :40, :47, :61, :65, :81, :85, :89, :103, :109, :115 ×2, :145; outlook.md:41, :43, :48, :49).

### 4. Word counts (AGENTS.md §3.7 basis: prose excluding table rows, Glossary, Sources list, and source tags)

- business.md: **2,969** (target 2,000–3,000). Whole file including tables: 3,713.
- outlook.md: **1,189** (target 800–1,200). Whole file including tables: 1,689.

### 5. Claims — single-direction and gradeable

| # | Claim (short) | Single direction? | Gradeable next quarter? |
|---|---|---|---|
| 1 | Management reaffirms or raises $180–190B 2026 capex range on Q2 call | Yes (cut = missed; silence = dropped) | Yes |
| 2 | Management again says 2027 capex significantly above 2026 | Yes | Yes |
| 3 | Q2 10-Q again says just over 50% of backlog within 24 months | Yes | Yes |
| 4 | Q2 10-Q still says TPU hardware revenue begins later in 2026, majority 2027 | Yes | Yes (10-Q Item 2 wording) |
| 5 | Q2 Cloud operating margin ≥ 29.9% (32.9% − 3 pts, stated as proxy) | Yes | Yes (slides p.8 equivalent) |
| 6 | Premium Lite in ≥ 36 countries by end Q2 | Yes | Yes if disclosed; else ⏳ |
| 7 | Reported growth exceeds constant-currency growth by ~1 pt, ±0.5 | Yes | Yes (press-release reconciliation) |
| 8 | Management again says Cloud revenue was limited by capacity | Yes | Yes |
| 9 | Q2 depreciation of P&E > $6.5B | Yes | Yes (cash-flow statement) |
| 10 | Q2 10-Q shows $10.0B funded as non-marketable security | Yes | Yes |
| 11 | Management again says Search queries at an all-time high | Yes | Yes |

11/11 single-direction and gradeable. Count 11, within 6–12; one headline-adjacent claim (7), the rest fundamentals.

### 6. Jargon and banned words, re-scan

Banned-word hits (tailwind ×4, headwind ×4) are all inside management's verbatim quotes or refer to the quoted word in a gloss label; none in the writer's own prose. "Y/Y" is gone. One leftover inconsistency, not fixed because it touches an indicator row: outlook.md:14 row label still says "trailing 12 months" while business.md §8 indicator 5 now says "last four quarters combined". Owner may align the wording when locking the indicators.

### 7. Rubric, cycle 2

1. What they do / who pays: **Yes.**
2. What would kill it / early warning: **Yes.**
3. Why margins are what they are / cost scaling: **Yes.** The line-40 contradiction is gone and the 2022–2023 dip is explained.
4. Predict the scorecard from §5 alone: **Yes.** All eleven claims name the document and the number or sentence to look for.
5. Nothing required knowledge I don't have: **Yes**, with the minor "trailing 12 months" label noted above.

### Fixed directly, cycle 2

- outlook.md:43 bullet label: added "and "spot rates" are today's exchange rates" outside the verbatim quote (the quote itself is unchanged).

No typos found in either revised file.

### Final verdict: **PASS**

All twelve REVISE items are resolved, all 21 new or changed figures and quotes verify against the cached Q1 sources, the 22 cycle-1 edits are intact or carried into the restructured table, both files are within the word-count targets, and all eleven claims are single-direction and mechanically gradeable. Nothing substantive fails. One cosmetic note for the owner at indicator lock: align the outlook §1 free-cash-flow row label ("trailing 12 months") with business.md §8 ("last four quarters combined").
