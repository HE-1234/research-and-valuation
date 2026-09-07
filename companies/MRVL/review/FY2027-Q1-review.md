# Marvell Technology, Inc. (MRVL) — Reviewer report, Q1 FY2027 (quarter ended early May 2026)

_Reviewed 2026-09-07 against `sources/FY2027-Q1/` only (cutoff 2026-05-28). `sources/FY2027-Q2/` was not opened, listed, or grepped. Files reviewed: `business.md` (4,074 words before fixes), `outlook.md` (1,650 words before fixes)._

**Verdict: REVISE.** Citation spot-check: 80 items checked, 77 PASS, 3 FAIL, 0 UNVERIFIABLE. The numbers in every table are right and every quote is verbatim. What fails is one garbled sentence in §4 ("the gap is $203 million"), one wrong cell in the outlook indicators table ("no deposits disclosed"), one unlabeled computed figure, several interpretations presented as fact, both files well over the length target, and a GAAP/non-GAAP explanation that arrives after the first use.

---

## 1. Skeleton compliance

**business.md**

| Requirement (§6) | Result |
|---|---|
| `# <Company> — The Business` | OK |
| `_As of <QLABEL>. Written <date>._` with fiscal parenthetical on first use (§5) | OK: "Q1 FY2027 (quarter ended early May 2026)" |
| §1–§8 headings, in order, none skipped | OK. §1 has the history paragraph; §6 carries customer concentration; §8 has name / why / where |
| §2 segment table, 5 fiscal years | OK (FY2022–FY2026 + Q1 FY2027), definition change footnoted per Lessons 2026-09-07 |
| §3 table: revenue, gross margin, operating margin, capex, capex/revenue, 5 years | OK, plus R&D % and non-GAAP rows |
| §4 table, 5 years | OK |
| §8 marked `_Proposed — owner to review and lock._` | OK |
| Glossary, Sources | Both present. Sources table maps every tag prefix to a cached file |
| Length 2,000–3,000 words | **Deviation:** 4,074 words (4,188 after the reviewer's glosses). Even allowing ~600 words of tables and tags, the prose is over target |

**outlook.md**

| Requirement (§7) | Result |
|---|---|
| `# <Company> — Outlook as of <QLABEL>` with fiscal parenthetical | OK |
| `_Transcript source tier: … Written <date>._` | OK: "third-party (The Motley Fool)", matches MANIFEST tier 3 |
| §1 table: one row per indicator; columns this quarter / last quarter / what management said | OK on rows. **Minor deviation:** the middle column mixes "Q4 FY2026" and "Q1 FY2026" values in one cell; the skeleton asks for last quarter |
| §2, §3, §4 (verbatim guidance), §5 | OK |
| §6 Tone shift omitted on first run | OK, correctly omitted |
| Sources | OK |
| Length 800–1,200 words | **Deviation:** 1,650 words (1,680 after glosses) |

---

## 2. Citation spot-check

Legend: PASS / FAIL / UNVERIFIABLE. Line numbers refer to the cached `.txt` files. "computed" items were re-derived.

### 2a. business.md §2 end-market table (every cell)

| # | Cell(s) | Tag | Found at | Result |
|---|---|---|---|---|
| A1 | Data center FY22/23/24: 1,784.7 / 2,408.8 / 2,216.7 | [10-K FY2024, Note 3] | 10-K-FY2024.txt line 2189 | PASS |
| A2 | Enterprise networking 907.7 / 1,369.2 / 1,228.4 | same | line 2191 | PASS |
| A3 | Carrier infrastructure 820.4 / 1,084.0 / 1,051.9 | same | line 2193 | PASS |
| A4 | Consumer 700.0 / 701.1 / 622.4 | same | line 2195 | PASS |
| A5 | Automotive/industrial 249.6 / 356.5 / 388.3 | same | line 2197 | PASS |
| A6 | Data center FY24/25/26: 2,216.7 / 4,164.2 / 6,100.3 | [10-K FY2026, Note 3] | 10-K-FY2026.txt line 2361 | PASS (FY2024 value identical across the definition change, as the 10-K states) |
| A7 | Communications and other FY24/25/26: 3,291.0 / 1,603.1 / 2,094.3 | same | line 2363 | PASS; 3,291.0 = 1,228.4+1,051.9+622.4+388.3 (checks) |
| A8 | Totals 4,462.4 / 5,919.6 / 5,507.7 / 5,767.3 / 8,194.6 | Items 7/8 | 10-K-FY2024 line 1777; 10-K-FY2026 line 1915 | PASS |
| A9 | Q1 FY2027: 1,832.7 / 585.1 / 2,417.8 | [10-Q Q1 FY2027, Note 3] | 10-Q line ~503–509 (Note 3 begins line 487); also release | PASS |
| A10 | Share 40% / 41% / 40% / 72% / 74% / 76% | Notes 3 | 10-K-FY2024 line 2189; 10-K-FY2026 line 2361; 10-Q Note 3 | PASS |
| A11 | Footnote quote "the composition of our data center end market remains unchanged" | [10-K FY2026, Note 3] | line 2353 | PASS verbatim |
| A12 | "the FY2025 four-way split is only in the FY2025 10-K, not among this report's sources" | — | MANIFEST confirms FY2025 10-K not fetched | PASS |

### 2b. business.md §3 economics table

| # | Row | Tag | Found at | Result |
|---|---|---|---|---|
| B1 | Revenue row | as A8 | as A8 | PASS |
| B2 | Gross margin GAAP 46.3 / 50.5 / 41.6 / 41.3 / 51.0 / 52.1 | 10-K FY2024 Item 7; 10-K FY2026 Item 7; release | 10-K-FY2024 line 1341 (41.6, 50.5); 10-K-FY2026 line 1497 (51.0, 41.3); release; FY2022 = 2,064.2/4,462.4 = 46.26% labeled computed | PASS |
| B3 | Gross margin non-GAAP FY2026 **59.4% (computed)** from proxy half-years 59.6% / 59.3% | [DEF 14A 2026, CD&A] | DEF14A lines 1909 and 1921 ("59.6 %", "59.3 %") | PASS with caveat. Simple average = 59.45; revenue-weighted (H1 $3,901M, H2 $4,293M, both in the same proxy table) = 59.44 → 59.4%. Direct computation from the supplemental's quarterly COGS reconciliations (p.8) gives non-GAAP gross profit 4,871.8 / 8,194.6 = 59.45% → 59.5%. The figure sits on a rounding boundary; method should be stated (see REVISE 12) |
| B3' | Non-GAAP GM Q1 58.9% | [release] | press-release.txt reconciliation | PASS |
| B4 | R&D % 31.9 / 30.1 / 34.4 / 33.9 / 25.3 / **27.0** | footnote tags | 10-K-FY2024 line 1345 (34.4, 30.1); 10-K-FY2026 line 1501 (25.3, 33.9); FY2022 = 1,424.2/4,462.4 = 31.9 labeled computed; Q1 = 652.3/2,417.8 = 26.98 | **FAIL (label only):** the Q1 FY2027 27.0% is not in the release; it is computed and not labeled "(computed)". Arithmetic is right |
| B5 | Operating margin GAAP (7.8) / 4.0 / (10.3) / (12.5) / 16.1 / 14.0 | same | 10-K-FY2024 line 1355; 10-K-FY2026 line 1509; release; FY2022 = -347.7/4,462.4 = -7.79 computed | PASS |
| B6 | Operating margin non-GAAP FY2026 **35.3% (computed)** = quarterly non-GAAP operating income 647.3+698.8+753.1+791.8 = 2,891.0 / 8,194.6 | [Q1 FY2027 supplemental, p.8] | supplemental.txt p.8 (form-feed count confirmed) "Non-GAAP Operating income" row | PASS (35.28%) |
| B6' | Non-GAAP OM Q1 35.0% | [release] | release | PASS |
| B7 | Capex 169.2 / 206.2 / 336.3 / 284.6 / 354.1 / 155.7 | Items 8; release | 10-K-FY2024 line 1977; 10-K-FY2026 line 2107; release cash flow | PASS |
| B8 | Capex/revenue (computed) 3.8 / 3.5 / 6.1 / 4.9 / 4.3 / 6.4 | — | recomputed 3.79 / 3.48 / 6.11 / 4.93 / 4.32 / 6.44 | PASS |

### 2c. business.md §4 cash table

| # | Row | Tag | Found at | Result |
|---|---|---|---|---|
| C1 | GAAP net income (421.0) / (163.5) / (933.4) / (885.0) / 2,670.1 / 34.5 | Items 8; release | 10-K-FY2024 line 1809; 10-K-FY2026 line 1943; release | PASS |
| C2 | Operating cash flow 819.3 / 1,288.8 / 1,370.5 / 1,681.2 / 1,750.5 / 638.8 | same | 10-K-FY2024 line 1971; 10-K-FY2026 line 2101; release | PASS |
| C3 | Capex | as B7 | | PASS |
| C4 | Free cash flow (computed) 650.1 / 1,082.6 / 1,034.2 / 1,396.6 / 1,396.4 / 483.1 | — | recomputed, all exact | PASS |
| C5 | Stock-based compensation 460.7 / 552.4 / 609.8 / 597.4 / 590.8 / 207.6 | same | 10-K-FY2024 line 1943; 10-K-FY2026 line 2075; release | PASS |
| C6 | Amortization of acquired intangibles 979.4 / 1,087.4 / 1,097.9 / 1,052.6 / 942.0 / 225.2 | same | 10-K-FY2024 line 1945; 10-K-FY2026 line 2077; release | PASS |
| C7 | Buybacks — / 115.0 / 150.0 / 725.0 / 2,040.1 / 200.0 | Item 8; Note 10; release | 10-K-FY2024 line 1987; 10-K-FY2026 lines 2121, 3011; release | PASS |
| C8 | Dividends 191.0 / 204.4 / 206.8 / 207.5 / 205.1 / 53.8 | same | 10-K-FY2024 line 1993; 10-K-FY2026 line 2127; release | PASS |

### 2d. outlook.md §1 indicators table (every number)

| # | Cell | Tag | Found at | Result |
|---|---|---|---|---|
| D1 | DC $1,832.7M 76%; Q4 FY2026 $1,651.3M 74%; Q1 FY2026 $1,440.6M 76%; "$18.0 million above the mid-point" | [release] | release end-market tables and paragraph 2 | PASS |
| D2 | Non-GAAP GM 58.9% / 59.0% / 59.8%; "key determinants" | [release]; [call] | release reconciliation; transcript CFO remarks | PASS |
| D3 | "remains on track to grow more than 20%"; ">20%" | [call] | transcript CEO custom paragraph | PASS |
| D4 | "more than 70%"; prior "50% growth" | [call] | transcript line 20 | PASS |
| D5 | "to exceed $600 million, doubling from fiscal 2026"; "$300M (inference)" | [call] | transcript switching paragraph; inference labeled | PASS |
| D6 | 45% / 16%; Q1 FY2026 36% / 16%; FY2026 37% / 14% | [10-Q Item 2; 10-K Item 1] | 10-Q lines 1473, 1477; 10-K-FY2026 lines 379, 383 | PASS |
| D7 | $2,756.8M; $870.0M after quarter end; $2,665.8M at Jan 31 2026 | [10-Q Note 9]; [10-K Note 8] | 10-Q lines 1013, 1029; 10-K-FY2026 Note 8 | PASS on the three numbers |
| D7' | "**no deposits disclosed**" at Jan 31 2026 | [10-K FY2026, Note 8] | 10-K-FY2026 Note 8: "total fees and refundable deposits payable under these arrangements are $23.1 million in fiscal 2027 through fiscal 2028" (and 10-Q Note 9 line 1029: $11.5M through FY2028 under the prior agreements) | **FAIL:** the 10-K does disclose deposits, just small ones |
| D8 | $647.6M; $315.8M at closing; max ~$233M cash + 22.4M shares | [10-Q Note 6] | 10-Q lines 837–847 | PASS (note: 10-Q Item 1A line 2155 says 24.4M shares; the filing is internally inconsistent; the writer used Note 6, which is the right choice) |

### 2e. outlook.md §4 guidance quotes (word-for-word)

| # | Quote (abridged) | Tag | Found at | Result |
|---|---|---|---|---|
| E1 | Seven Q2 bullets: "$2.700 billion +/- 5%", "52.1% to 53.1%", "58.25% to 59.25%", "$960 million", "$600 million", "$0.37 +/- $0.05", "$0.93 +/- $0.05"; "quarter ending August 1, 2026" | [release] | release outlook bullets; outlook reconciliation header "Three Months Ended August 1, 2026" | PASS, all verbatim |
| E2 | "mid to high teens sequentially on a percentage basis" | [call] | transcript line ~34 | PASS |
| E3 | "approximately 40% year over year to nearly $11.5 billion" | [call] | line 20 | PASS |
| E4 | "we expect Q3 and Q4 revenue to also grow by at least 10% sequentially, as a result, we now expect $3 billion in quarterly revenue in Q3" | [call] | line 18 | PASS |
| E5 | interconnect "more than 70% … prior expectation of 50% growth" | [call] | line 20 | PASS |
| E6 | "We are forecasting approximately $1 billion in prepayments … applied against future material purchases." | [call] | CFO remarks | PASS |
| E7 | "fiscal 28 revenue to reach 16.5 billion roughly $1.5 billion higher …" | [call] | line 24 | PASS |
| E8 | "data center revenue in fiscal 28 to grow approximately 55%"; custom "to more than double year over year" | [call] | lines 22, custom paragraph | PASS |
| E9 | "upper end of our target operating margin model of 38% to 40% as we progress through fiscal 28" | [call] | CFO remarks | PASS |
| E10 | "over $10 billion in revenue in fiscal 29" | [call] | custom paragraph | PASS |

### 2f. outlook.md §5 claim quotes (word-for-word)

All twelve quotes under the claims match the cached release or transcript exactly, including claim 10's 10-Q quote "payable in quarterly installments from the second quarter of fiscal 2027" (10-Q line 1029) and claim 12's table row "Distributor A | 45% | 36%" (10-Q line 1477). Claim 1's computed range $2.565–2.835 billion is correct. **14 PASS.** None of the quotes relied on is a garbled passage; the writer correctly avoided the garbled "Reaching approximately 50% by Q4" fragment and the "$5 billion" raise (outlook line 45).

### 2g. Prose sentences, business.md §5–§7 and elsewhere

| # | Sentence / claim | Tag | Found at | Result |
|---|---|---|---|---|
| G1 | §6#1: distributor 45% (36%), largest direct 16%, ten largest "represented 82% of our total net revenue for fiscal 2026" | [10-Q Item 2; 10-K Item 1A] | 10-Q lines 1473–1477; 10-K-FY2026 line 613 | PASS |
| G2 | §6#1: three customers 75% of gross receivables | [10-Q Item 2] | 10-Q line 1465 | PASS |
| G3 | §6#5: "Most of our products are manufactured by third-party foundries located in Taiwan"; "most of our products are not manufactured at more than one foundry at any given time, and our products typically are designed to be manufactured in a specific process at only one of these foundries" | [10-K Item 1A] | lines 719, 733 | PASS verbatim |
| G4 | §5: "their typical development cycle of approximately 2 years" | [call] | custom paragraph | PASS |
| G5 | §5: "the first to market cadence we have maintained across successive PAM 4 generations"; "to all 5 major US hyperscalers" | [call] | interconnect / DCI paragraphs | PASS verbatim |
| G6 | §5: COO "Everything that touches AI has been constrained basically since the beginning of this"; 4-to-10-year reservations | [call; 10-K Note 8] | transcript Koopmans answer; 10-K Note 8 "ranges from 4 to 10 years" | PASS |
| G7 | §5/§7: NVIDIA $2.0B preferred; converts at ~$91.84 into up to 21.8M shares | [10-Q Item 2; Note 10] | 10-Q lines 1445, 1083 | PASS |
| G8 | §6#2: "for a negotiated period of time"; "there may be no other customers for these products"; new program "about a third" | [10-K Item 1A; call] | line 783; transcript Murphy to Vivek Arya | PASS |
| G9 | §6#3: data center sales "have fluctuated significantly from period to period"; "30%-plus range"; days of inventory 110 and 91 | [10-K Item 1A; call; supplemental p.4] | 10-K line 637 (this is the data-center sentence, not the largest-customers one at line 613); transcript line 22; supplemental p.4 | PASS on numbers; see §3 item 4 for the selective framing |
| G10 | §6#4: "some of our customers have chosen to develop … proliferate"; "some large customers may begin developing and making their own semiconductor solutions"; Broadcom named competitor | [10-K Item 1; Item 1A] | lines 449, 635, 469 | PASS |
| G11 | §6#6: ~$233M cash, 22.4M shares, $315.8M → $647.6M, $331.8M, $2.4B goodwill, "not material" | [10-Q Note 6; Item 2; Note 4] | lines 837–847, 1633, 599–611 (goodwill 2,404.4), 615 | PASS |
| G12 | §6#7: 44% of Q1 revenue to China, "substantial majority" to non-China customers' factories; 15% revenue share "did not impact Marvell", "could erode our gross margins"; "reduced the demand for our products and damaged our business"; call silent on China/tariffs/export | [10-Q Note 3; 10-K Item 1A; call] | 10-Q line 515 + following paragraph; 10-K line 851, 609; transcript grep = 0 hits | PASS |
| G13 | §7: Murphy 53, joined July 2016, Chairman June 2023; Meintjes CFO Jan 2023; FMR 14.95%, Vanguard 9.40%, BlackRock 7.14%; insiders under 1%; Proposal 4 quote; board cites lead independent director | [DEF 14A] | lines 381/1263, 1281, 1325–1329, 1359 ("*" = <1%), 1129, 1233–1251 | PASS |
| G14 | §7: bonus 50/15/35, paid 144.84%; 70% performance-based for CEO; 3-year TSR vs S&P 500; up to 150% non-GAAP EPS multiplier | [DEF 14A, CD&A] | lines 1871ff, 1521, 1951, 1985, 2029 | PASS |
| G15 | §7: $146.58 average; $0.06 quarterly FY2022–Q1 FY2027; 846.7M shares end FY2022; 875.6M at May 2 2026; 26.8M acquisition shares; $5.0B notes, nothing due until FY2029; cash $3.8B | [10-Q Part II Item 2; Items 5; Item 1; Note 7] | 10-Q line 2459 (only month with purchases); 10-K-FY2024 line 1181, 10-K-FY2026 line 1303, 10-Q line 303; 10-K-FY2024 line 1887; 10-Q lines 290, 305; Note 7 maturity table (FY2028 —, FY2029 1,249.9); balance sheet | PASS |
| G16 | §1 history: "only about 9% of our revenue base"; deals quote; oldest stock plan April 1995; Infineon Aug 14 2025 $2.5B cash; auto-Ethernet revenue not disclosed; Celestial $3.5B, XConn $469.0M | [DEF 14A letter; 10-K Note 11; Note 1/Item 7; 10-Q Note 4] | DEF14A lines 99, 103; 10-K lines 3021, 2165, 1371; 10-Q lines 567, 625; no auto-Ethernet revenue figure anywhere in the 10-K (confirmed) | PASS |
| G17 | §2: distributors 51% Q1 FY2027, 26% FY2022; "with relatively short notice" | [10-Q Note 3; 10-K FY2024 Note 3; 10-K Item 1A] | 10-Q customer-type table (line ~536); 10-K-FY2024 line 2239; 10-K-FY2026 line 621 | PASS |
| G18 | §3: R&D $2.1B / 25%; product costs $3.3B of $4.0B COGS; SBC $591M; GM gap 6.3 + 0.6; proxy GM-target quote; Note 5 amortization falls after FY2027 | [10-K Item 7; Note 14; Item 8; release; DEF 14A CD&A; Note 5] | 10-K lines 1561/1501, 3553, 2075; release; DEF14A line 1863 (verbatim); Note 5 schedule 814.0 → 284.8 | PASS. Nit: "the whole gap" — 6.3 + 0.6 = 6.9 pts against a 6.8 pt gap because of a (0.1) restructuring credit |
| G19 | §4: "adjusted operating profit of about $2.89 billion … became $1.75 billion of operating cash flow and $1.40 billion of free cash flow, 17% of revenue (computed); **the gap is $203 million of interest, cash taxes and money tied up in growth**" | [supplemental p.8; 10-K Item 8] | $2,891.0M and 17.0% check. But $2.89B − $1.75B = **$1.14 billion**, not $203 million. $202.6M is FY2026 interest expense alone (10-K line 1933) | **FAIL:** the sentence attaches a sourced number to the wrong quantity |
| G20 | §4: total assets $26.9B, goodwill $13.9B, intangibles $2.6B at May 2 2026 | [release] | release balance sheet (26,944.5 / 13,883.5 / 2,561.5) | PASS |

**Totals: 80 checked; 77 PASS; 3 FAIL (B4 label, D7' "no deposits disclosed", G19 "$203 million"); 0 UNVERIFIABLE.**

---

## 3. Invented-number and inference check

No invented numbers were found: every figure traces to a cached source or a correctly labeled computation, with the exceptions in §2 above. Interpretations presented as fact:

1. **business.md §3, line 53:** "Custom chips for one customer earn less gross margin than standard interconnect parts." No source says this. The proxy (line 1863) says only "expected near-term product mix shift"; the 10-K (line 1551) says "a shift in product mix." The only place in the sources that says custom is lower-margin is the *shareholder proponent's* text in Proposal 4, which is not management. Label as inference or attribute properly.
2. **Customer A is treated as the custom XPU customer** (business.md §5 line 82 "the largest direct customer's share falling"; §6 line 98 "Customer A's share falling"; outlook.md §3 line 27 "tells are … Customer A's share of revenue"). The 10-Q and 10-K never connect Customer A to any product line. This is a plausible inference and should be written as one ("our inference: Customer A is likely the custom-XPU customer, so its share is a proxy"). The report correctly does **not** name Customer A, Distributor A, or the tier 1 XPU customer anywhere, and correctly ignored the proponent's mention of Amazon and Microsoft in Proposal 4.
3. **business.md §6#6, line 106:** "The rise means Marvell expects Celestial to do better." Note 6 (10-Q line 837) lists the valuation inputs as forecasted revenue, probability of achievement, stock-price volatility, and Marvell's stock price. A higher share price alone raises the liability. Change to "suggests" and note the stock-price input. The adjacent "erased most of Q1's GAAP profit" is fair but is also an inference (net of the $81.1M hedge gain the pre-tax hit was $250.7M).
4. **business.md §6#3, line 100:** days of inventory "110 at quarter end, up from 91 two quarters earlier." The supplemental p.4 sequence is 96 → 91 → 117 → 110. The quarter in between (117) is skipped, so a fall is presented as a rise. Give the sequence or compare with the prior quarter.
5. **business.md §4, line 76:** the "$203 million" gap (FAIL G19). The number is real (interest expense) but does not describe the gap the sentence names.
6. **business.md §2, line 14:** distributors "resell to the module makers and system builders serving the cloud companies." The filings say only that half of sales go through distributors. Label or cut.
7. **business.md §4, line 78:** "a modest return on everything ever paid in; the return that matters now is on each new R&D dollar" is the writer's judgment; say so ("our view").
8. **History paragraph (§1, line 10)** checked against the filings: founding date is *not* in the sources; the writer inferred "mid-1990s" from the 1995 Stock Option Plan (10-K Note 11, line 3021) and said so in the same sentence, which is acceptable but should carry "our inference." Murphy's start (July 2016) is in the proxy (line 381). Cavium and Inphi: the writer gave no dates, quoting only the proxy's list, which is correct restraint; the only dates in the sources are merger-agreement dates in exhibit lists (Cavium 2017-11-19, 10-K FY2026 line 4013; Inphi 2020-10-29, line 4011) and the Inphi term loan (Dec 2020, Note 7 line 2739). "The modern company dates from 2016" is framing supported by the proxy letter ("When I became CEO in 2016, Marvell was a very different company").
9. **Glossary "XPU — Marvell's catch-all name":** XPU is industry shorthand, not a Marvell coinage; no source calls it Marvell's name. Reword.

---

## 4. Jargon and readability audit

Read as a smart 16-year-old with no finance or semiconductor background.

**(a) Undefined terms, not in the glossary, not obvious from the name** (before reviewer fixes; items marked *fixed* were glossed directly, see "Fixed directly"):

| Term | Where | Status |
|---|---|---|
| goodwill | business.md §4 line 78, §6 line 106 | *fixed* at line 78; still bare at line 106; belongs in glossary |
| amortization / amortizing | §3 line 51, §4 table line 68, §4 line 74 | *fixed* at line 51 (plain definition); glossary entry recommended |
| capex | §3 table header line 46 (first use), §4 table | *fixed* at line 55 but the table header still comes first; define in the table footnote or glossary |
| convertible preferred stock | §5 line 88, §7 line 116 | *fixed* at line 88 |
| gross receivables | §6 line 96 | *fixed* |
| tier 1 | §6 line 98; outlook §3 lines 27, 31 and claim 9 | *fixed* at business line 98 and outlook line 27; claim 9 untouched (claims are off-limits to the reviewer) |
| days of inventory | §6 line 100 | *fixed* |
| lead independent director | §7 line 112 | *fixed* |
| fixed-rate notes | §7 line 116 | *fixed* |
| "expensed as spent", "sunk cost" | §3 lines 55, 51 | *fixed* (plain phrases) |
| XPU-attach | §8 indicator 3; outlook §3 line 27 (in quote) | not fixed (indicator list is off-limits). Needs a glossary entry: chips that sit beside a custom AI processor (network cards, memory-expansion controllers) |
| scale-out vs scale-up | §8 indicator 5; outlook §1 row 5, §3 line 29 | *fixed* in outlook §3 (scale-out gloss added; scale-up was already defined "links AI processors inside a rack"); business.md never defines either; glossary entry needed |
| PAM 4 | §5 line 84 (inside a quote) | undefined; either gloss after the quote ("the signalling scheme Marvell's optical DSPs use") or cut the quote to the "first to market" part |
| 800G / 1.6T | §5 line 84 | described as "speed generations", acceptable |
| earn-out | §6 line 106 heading | explained by the next clause ("owes … if the business hits revenue milestones"), acceptable |
| contingent consideration, ASR, mandatory convertible, revolver, NPO, DCI, SerDes | — | not used in either file (the writer used plain phrases: "modules linking data centers", "links AI processors with light"). Good |
| hyperscaler | §1 line 6 | defined inline ("enormous cloud companies … the industry calls them hyperscalers"). Good |
| proxy, CD&A | §3 footnote line 49, tags | "proxy" is explained only in the Sources table; add "(the annual shareholder-meeting document that discloses pay)" at line 49 |
| "guided range", "reconciliation" | §8 indicator 2; outlook §1 row 2 | jargon inside the indicator list; owner to reword at lock ("the range management forecast"; "the press-release table that bridges GAAP to non-GAAP") |
| run rate, sequentially | outlook §3 line 25, §4 line 37 | *fixed* |
| "drivers" (TIAs and drivers) | outlook §3 line 25 | undefined; a one-word gloss ("the chip that drives the laser") would do |
| companion chip | §1 line 8 | semi-obvious; fine |

**(b) Glossary entries that are not plain or not essential.** CPO appears only in the glossary; nowhere in either file's text. Remove it. The XPU entry's "Marvell's catch-all name" is inaccurate (see §3 item 9). TIA is used once in outlook §3 and once in claim 7; borderline essential, keep. DSP, ASIC, Foundry, GAAP/non-GAAP are used and plain. Missing essential entries: goodwill, amortization, scale-out/scale-up, XPU-attach, capex.

**(c) Sentences that assume prior knowledge.**
- §3 line 36 "operating profit swings hard with volume" — operating profit/margin is never defined (profit after all running costs including R&D; gross margin is defined). One clause fixes it.
- §4 line 74 "write-downs such as $357.9 million of impairments" — "write-downs" is used to explain "impairments" but is itself jargon; say "charges for assets judged to be worth less than their book value."
- §7 line 114 "measured on three-year total shareholder return against the S&P 500" — a 16-year-old may not know the S&P 500 is an index of 500 large US companies. Add four words.
- outlook §1 row 2 "revenue level and mix are the 'key determinants'" — "mix" is defined in business.md §3 but not here.

**(d) GAAP vs non-GAAP explanation (business.md line 51).** Plain: yes; the paragraph says what GAAP is, what is removed, and — the key part — "uses non-GAAP margins to see the pricing and cost structure … uses GAAP and cash flow to judge what owners keep, because stock pay is real." The reader comes away knowing which number to trust for what. **Placed before first use: no.** The §3 table (lines 38–47) and its footnote (line 49) use "non-GAAP" four times before the explanation at line 51. Move the paragraph above the table or add a one-line pointer before it.

**(e) Banned words** (leverage, synergy, headwind, tailwind, monetize, ecosystem, at scale, robust, unlock, TAM): a case-insensitive sweep of both files found **none** outside verbatim quotes (and none inside quotes either; the writer chose quotes that avoid them).

**Paragraphs that are mostly numbers:** business.md line 76 (§4, "$2.89 billion … $1.75 billion … $1.40 billion, 17% … $203 million"), line 106 (§6#6: six dollar figures in four sentences), line 116 (§7 capital allocation: eleven figures in five sentences; this wants to be a small table). Line 96 (§6#1) is borderline but reads fine.

**Tables that have become walls:** outlook.md §1 — several cells hold two or three numbers plus a quote plus a tag (rows 1, 6, 7, 8). Readable but dense; the "last quarter" column should hold one comparison, not two. business.md §2, §3, §4 tables are fine.

---

## 5. Claims quality (outlook.md §5)

Count: 12 (within 6–12). Headline revenue claims are 4 of 12 (1, 3, 4, 8); no EPS claim; the rest are fundamental signals. Good balance.

| # | Testable sentence? | Tied to metric / date / event? | Quote supports? | Gradeable mechanically? | Notes |
|---|---|---|---|---|---|
| 1 | Yes | Q2 revenue in $2.565–2.835B | Yes | Yes | Range computed correctly |
| 2 | Yes | Q2 non-GAAP GM 58.25–59.25% | Yes | Yes | |
| 3 | Yes | FY2027 guide ≥ ~40% / ~$11.5B on Q2 call | Yes | Yes | |
| 4 | Yes | Q3 guide midpoint ≥ $3.0B | Yes | Yes | |
| 5 | Yes | interconnect target ≥ 70% restated | Yes | Yes; silence = Dropped | |
| 6 | Yes | switch >$600M restated | Yes | Yes; silence = Dropped | |
| 7 | **Vague** | "at or approaching a $1 billion annualized run rate" | Quote says "exceed … in the next few quarters" | **No** — "approaching" is a judgment call, and the horizon is several quarters, so next quarter is likely ⏳ | Sharpen: "By the Q2 call management reiterates the $1B run-rate target for TIAs and drivers" (checkable now) or set a numeric threshold with a Q3/Q4 horizon |
| 8 | Yes | FY2028 ~$16.5B reiterated or raised | Yes | Yes | |
| 9 | **Double-barreled** | "on track" AND "firm FY2028 requirements" | Yes | Partly — two things to check; "on track" is soft | Reduce to one: "Management again describes the new tier 1 XPU program as on track for FY2028 volume production" |
| 10 | Yes | Q2 10-Q shows first deposit/prepayment installment | Yes (call + 10-Q Note 9) | Mostly; depends on the 10-Q disclosing the payment (Note 9 or cash-flow "prepaid" line) | Acceptable |
| 11 | **Double-barreled and partly unsupported** | liability ≥ $647.6M "consistent with the FY2028 scale-up optics outlook" | The quote is about revenue outlook, not the liability | The number is gradeable; the "consistent with" clause is not — the liability also moves with Marvell's share price (Note 6) | Strip the clause; label as a disclosure check like #12 |
| 12 | Yes (labeled disclosure check) | Distributor A ≥ 45% | Table row | Yes | Fine |

Claims 11 and 12 are reviewer-constructed disclosure checks rather than management statements; 12 is labeled as such, 11 is not.

---

## 6. Rubric (§14), from the reader's chair

1. **What the company does and who pays, in two sentences?** Yes. §1–§2 make it clear: it designs the chips that move data inside and between data centers, pays Taiwanese factories to make them, and a handful of giant cloud companies (half of them through distributors) pay per chip.
2. **What would kill it and the early warning?** Yes. §6 is ranked, each scenario has a sign, and it is honest that Taiwan has none. The concentration numbers are the right thing to watch.
3. **Why the margins are what they are and whether cost scales with usage?** Yes, mostly. §3's "fixed R&D bill spread over more or fewer chips" and "mix" are exactly right; the custom-is-lower-margin sentence is asserted, not sourced, and the GAAP/non-GAAP explanation arrives one table too late.
4. **Could I predict next quarter's scorecard from §5 alone?** Mostly. Nine of twelve claims are mechanical; 7, 9 and 11 would need a judgment call.
5. **Did nothing require knowledge I don't have?** No. Before fixes: goodwill, amortization, capex, preferred stock, receivables, tier 1, run rate, sequentially, scale-out, XPU-attach, PAM 4 all stopped the reader. About half are now glossed; goodwill/amortization/scale-out/XPU-attach/capex still need glossary entries and PAM 4 is still bare.

---

## 7. Verdict: REVISE

Numbered list for the writer (numbers, quotes, structure, claims, and the indicator list are untouched by the reviewer and must be changed by the writer):

1. **business.md §4, line 76.** Rewrite the last clause. The gap between $2.89B adjusted operating profit and $1.75B operating cash flow is $1.14B (computed), not $203M. Suggested: "the $1.14 billion gap (computed) is interest of about $203 million [10-K FY2026, Item 8], cash taxes, and the $1.1 billion of cash tied up in growth [10-K FY2026, Item 7]."
2. **outlook.md §1, indicator 7, middle cell.** Replace "no deposits disclosed" with "$23.1 million of capacity fees and refundable deposits payable FY2027–FY2028 under earlier agreements [10-K FY2026, Note 8]."
3. **business.md §3 table footnote, line 49.** Add "(Q1 FY2027 R&D % computed from the release: 652.3 / 2,417.8)" or drop the R&D row's Q1 cell.
4. **business.md §3, line 53.** Either label "Custom chips for one customer earn less gross margin than standard interconnect parts" as "our inference" with the proxy's "product mix shift" as the supporting phrase, or attribute it to the Proposal 4 proponent explicitly (and say that is a shareholder, not management).
5. **Customer A = XPU customer.** In business.md §5 line 82, §6 line 98, and outlook.md §3 line 27, add "our inference:" before using Customer A's share as the custom-program signal; the filings never link Customer A to a product line.
6. **business.md §6#6, line 106.** "The rise means Marvell expects Celestial to do better" → "The rise suggests Marvell expects Celestial to do better, though the liability also rises with Marvell's share price [10-Q Q1 FY2027, Note 6]."
7. **business.md §6#3, line 100.** Replace "up from 91 two quarters earlier" with the four-quarter sequence "96, 91, 117, 110 over the last four quarters [Q1 FY2027 supplemental, p.4]" or compare with the prior quarter (117).
8. **GAAP/non-GAAP placement.** Move the "Two sets of numbers" paragraph (line 51) above the §3 table, or insert one sentence before the table: "Two versions of margin appear below; see the paragraph after the table for which to trust for what."
9. **Glossary.** Add: goodwill, amortization, scale-out vs scale-up, XPU-attach, capex. Remove CPO (unused). Reword XPU: "industry shorthand for a custom AI processor…" Optional: preferred stock, if the inline gloss is cut.
10. **Length.** Cut business.md to ≤3,000 words and outlook.md to ≤1,200. Candidates: turn §7 line 116 into a five-row table; halve §6#6; merge the §5 "Caveats" line into §6; trim §4 line 76; in outlook, remove the FY2028/FY2029 quotes that already appear in §3, and hold one comparison value per cell in §1.
11. **Claims.** #7: sharpen to a checkable statement (see §5 table). #9: single clause. #11: delete "consistent with the FY2028 scale-up optics outlook" and label "(Disclosure check, not a management claim.)" as in #12.
12. **FY2026 non-GAAP gross margin.** Keep 59.4% but state "revenue-weighted average of the proxy's half-years", or recompute from the supplemental p.8 quarterly COGS reconciliations (4,871.8 / 8,194.6 = 59.5%) so both non-GAAP margins come from the same source. Whichever, show the inputs.
13. **business.md §3, line 51.** "the whole gap" → "almost the whole gap" (6.9 pts of items against a 6.8 pt gap; a 0.1 pt restructuring credit closes it).
14. **Indicator list (owner to review at lock; reviewer did not touch).** Indicator 2: "vs the guided range" → "vs the range management forecast"; "Press release reconciliation" → "press-release GAAP-to-non-GAAP table". Indicator 3: gloss "XPU-attach". Indicator 5: gloss "Scale-out".
15. **business.md §2, line 14.** Label "module makers and system builders serving the cloud companies" as inference, or cut to "who hold stock and resell it."
16. **business.md §5, line 84.** Gloss or trim the "PAM 4" quote; **§3 line 36** define operating profit in a clause; **§7 line 114** add "(an index of 500 large US companies)" after S&P 500; **§4 line 74** replace "write-downs" with a plain phrase.
17. **outlook.md §1 header column.** Use one "last quarter" value per cell (Q4 FY2026) and move year-ago comparisons to prose or a footnote, so the table matches the §7 skeleton and stops being a wall.

---

## Fixed directly (jargon glosses, plain phrases, one tag; no numbers, quotes, structure, claims, or indicators changed)

business.md
- Line 51: "amortization of the value of technology and customer relationships bought in past acquisitions" → "amortization, which spreads the price paid for technology and customer relationships in past acquisitions over several years as a yearly expense"; "a sunk cost" → "money already spent"; added "(each existing share owns a smaller slice)" after "dilute every owner".
- Line 55: "capital spending" → "capital spending (capex: money spent on equipment and buildings)"; "expensed as spent" → "counted as a cost in the year it is spent".
- Line 78: added plain glosses for "goodwill" and "acquired intangibles".
- Line 82: tag "[Q1 FY2027 call]" → "[Q1 FY2027 call; 10-K FY2026, Item 1A]" — the "ships for the whole product generation" half of the sentence is supported by the 10-K's "for the life of that product" (line 767), not by the call.
- Line 88: "convertible preferred stock" → "convertible preferred stock (a special class of shares that can later be swapped for common shares)".
- Line 96: "Three customers owed 75% of gross receivables" → "Three customers accounted for 75% of the money customers owed Marvell (gross receivables)".
- Line 98: "a new tier 1 XPU program" → "a new XPU program for a top-tier (\"tier 1\") customer".
- Line 100: "days of inventory" → "days of inventory, meaning how many days of sales the chips on hand would cover".
- Line 112: added "(a board member with no management role who leads the other independent directors)" after "lead independent director".
- Line 116: "fixed-rate notes" → "fixed-rate notes (bonds with a set interest rate)".

outlook.md
- Line 25: added "(run rate: one quarter's revenue multiplied by four)" after the TIA/driver quote.
- Line 27: added "(tier 1: a top-rank customer)" after the quoted phrase.
- Line 29: "Scale-out Ethernet switches" → "Scale-out Ethernet switches (the switches that connect servers and racks across a data center)".
- Line 37: added "(sequentially: compared with the prior quarter)" after the data-center guidance quote.

Backups of the pre-fix drafts were left at `/tmp/business.md.bak` and `/tmp/outlook.md.bak`.

---

## Cycle 2 (re-check of the writer's second pass; review cycle 2 of 2)

_Re-checked 2026-09-07 against `sources/FY2027-Q1/` only. `sources/FY2027-Q2/` not opened._

### 1. Status of the 17 REVISE items

| # | Item | Status | Where |
|---|---|---|---|
| 1 | "$203 million gap" sentence | **Resolved.** Replaced by a nine-row FY2026 cash bridge and "$1.14 billion gap (computed)" | business.md lines 76–90 |
| 2 | Indicator 7 "no deposits disclosed" | **Resolved.** Now "$23.1M of capacity fees and refundable deposits payable FY2027–FY2028 under earlier agreements [10-K FY2026, Note 8]" | outlook.md line 16 |
| 3 | Q1 R&D % unlabeled | **Resolved.** "27.0% (computed)" plus footnote "652.3 / 2,417.8" | business.md lines 45, 51 |
| 4 | Custom-is-lower-margin as fact | **Resolved.** "Our inference is that … no filing says so directly", with the proxy's "reflected the expected near-term product mix shift" quoted | line 53 |
| 5 | Customer A = XPU customer | **Resolved.** Labeled "our inference" in §5, §6#2 and outlook §3 | business 96, 112; outlook 29 |
| 6 | "The rise means Marvell expects Celestial to do better" | **Resolved.** "suggests … though a higher Marvell share price alone also raises it", with Note 6's input list quoted | line 131 |
| 7 | Days of inventory cherry-pick | **Resolved.** "96, 91, 117 and 110 over the last four quarters, so no clear trend yet" | line 114 |
| 8 | GAAP/non-GAAP after first use | **Resolved.** "Two sets of numbers" paragraph (line 38) now precedes the §3 table (line 40) | |
| 9 | Glossary gaps | **Resolved.** XPU-attach, Scale-out / scale-up, Amortization, Goodwill, Capex added; CPO removed; XPU now "industry shorthand" | lines 167–179 |
| 10 | Length | **Resolved by the coordinator's definition; not by raw count.** Prose excluding tables, glossary, sources and tags: business.md 2,858 (target 2,000–3,000), outlook.md 1,173 (target 800–1,200). Raw counts rose to 4,811 and 1,730 because three new tables were added (1,325 and 455 table words). Owner to decide whether tables count | |
| 11 | Claims 7, 9, 11 | **Resolved.** See §5 below | outlook lines 57, 59, 61 |
| 12 | FY2026 non-GAAP gross margin method | **Resolved.** Recomputed from the supplemental as 4,180.7 + 691.1 = 4,871.8 / 8,194.6 = 59.5%, proxy half-years cited as consistent | lines 44, 51 |
| 13 | "the whole gap" | **Resolved.** "almost the whole gap" | line 38 |
| 14 | Indicator-list jargon | **Resolved.** "the range management forecast", "GAAP-to-non-GAAP table", XPU-attach and scale-out glossed in the table | lines 159, 160, 162 |
| 15 | Distributors "module makers and system builders" unsourced | **Resolved.** Now a sourced quote: "four module makers" … "supporting data center sales to hyperscale customers" [10-K FY2024, Item 1] | line 14 |
| 16 | PAM 4 / operating profit / S&P 500 / write-downs | **Resolved.** PAM 4 quote trimmed to "first to market cadence" with a plain paraphrase; operating profit defined; S&P 500 glossed; "charges for assets judged to be worth less than their book value" | lines 98, 36, 139, 74 |
| 17 | Outlook §1 one comparison per cell | **Resolved.** Column is now "Q4 FY2026 (last quarter)"; year-ago values moved to a sentence under the table | outlook lines 8–19 |

**17 of 17 resolved** (item 10 by the coordinator's prose-only definition; raw counts are noted for the owner).

### 2. New and changed numbers and quotes

| Item | Value in draft | Found at | Result |
|---|---|---|---|
| Bridge: adjusted operating profit | 2,891.0 (computed) | supplemental p.8, four FY2026 quarters sum exactly | PASS |
| Bridge: working capital | about (1,100) | 10-K-FY2026.txt line 1705 "Cash outflow from working capital of $1.1 billion" | PASS |
| Bridge: interest paid in cash | (177.7) [Note 15] | line 3811 "Cash paid for interest | 177.7"; Note 15 begins line 3603 | PASS |
| Bridge: income taxes paid in cash | (92.1) [Note 12] | line 3493 "Total cash paid for income taxes, net of refunds received | 92.1"; Note 12 spans lines 3211–3496 | PASS |
| Bridge: depreciation added back | 348.6 [Item 7] | line 1705 "depreciation and amortization of $348.6 million" | PASS on the number; the 10-K's label is "depreciation and amortization" (non-acquisition amortization such as technology licences is included). Row label corrected directly, see below |
| Bridge: other (computed remainder) | about (119) | 2,891.0 − 1,100.0 − 177.7 − 92.1 + 348.6 = 1,869.8; 1,869.8 − 1,750.5 = 119.3 | PASS |
| Bridge: OCF, capex, FCF, FCF % | 1,750.5; (354.1); 1,396.4; 17.0% | 10-K Item 8 lines 2101, 2107; 1,396.4 / 8,194.6 = 17.04% | PASS |
| "$1.14 billion gap (computed)" | 2,891.0 − 1,750.5 = 1,140.5 | — | PASS |
| $23.1M capacity fees/deposits | [10-K FY2026, Note 8] | Note 8: "total fees and refundable deposits payable under these arrangements are $23.1 million in fiscal 2027 through fiscal 2028" | PASS |
| FY2026 non-GAAP gross margin 59.5% | 4,180.7 + 691.1 = 4,871.8 / 8,194.6 | GAAP gross profit 4,180.7 (10-K line 1919; supplemental p.5 quarters 952.4 + 1,010.6 + 1,069.8 + 1,147.9). COGS items from supplemental p.8: SBC 49.2 + amortization 639.0 + restructuring 0.5 + other 2.4 = 691.1. Margin 59.451% → 59.5% | PASS |
| Days of inventory 96, 91, 117, 110 | [supplemental p.4] | supplemental.txt line 103, columns Aug 2 2025 → May 2 2026 | PASS |
| $81.1M hedge gain beside $331.8M charge | [10-Q Note 6] | 10-Q lines 845 (331.8), 849 (81.1) | PASS |
| "four module makers" / "supporting data center sales to hyperscale customers" | [10-K FY2024, Item 1] | 10-K-FY2024.txt line 339 (Item 1 spans lines 207–518): "Net revenue attributable to Distributor A increased due to the four module makers whose business activity increased in fiscal 2024 as they were involved in supporting data center sales to hyperscale customers." | PASS verbatim; the draft's paraphrase ("the largest distributor's growth came from") matches the sentence |
| Proxy "reflected the expected near-term product mix shift" | [DEF 14A, CD&A] | DEF14A-2026.txt line 1863 | PASS verbatim |
| Claim 9 quote "This program continues to progress very well through development" | [call] | transcript.txt line 70 | PASS verbatim |
| §6#6 table: 233.0 cash + 22.4M shares; 315.8; 647.6; 331.8; (81.1); goodwill 2,404.4; "not material"; "doubled in one quarter" | [10-Q Notes 6, 4] | lines 837, 843–849, 599–611, 615; 647.6 / 315.8 = 2.05 | PASS, every row |
| §6#6 Note 6 quote "forecasted revenue, probability of achievement, stock price volatility, the Company's stock price and other relevant assumptions" | [10-Q Note 6] | line 837 | PASS verbatim |
| §7 table: buybacks $2,040.1M / $200.0M / $146.58 / $5.3B left; dividend $0.06; shares 846.7M / 875.6M / 26.8M; debt $5.0B nothing due until FY2029; cash $3.8B; NVIDIA $2.0B / $91.84 / 21.8M | as tagged | 10-K-FY2026 line 3011; 10-Q lines 2459 (5,334.5 remaining), 303, 290, 305; Note 7 maturity table; balance sheet; Note 10 line 1083 | PASS, every row |
| Outlook §1 Q4 FY2026 column: $1,651.3M 74%; 59.0%; "Not disclosed" rows; FY2026 37% / 14%; $2,665.8M + $23.1M; $315.8M | as tagged | release; 10-K-FY2026 lines 379–383; Note 8; 10-Q Note 6 | PASS |
| Outlook line 19 year-ago: $1,440.6M 76%; 59.8%; 36% / 16% | [release; 10-Q Item 2] | release; 10-Q lines 1473–1477 | PASS |
| §5 line 98 "first to market cadence" | [call] | transcript interconnect paragraph | PASS (verbatim fragment) |

No new number or quote fails.

### 3. Cycle-1 direct edits

All 16 intact: business.md amortization definition, "money already spent", dilution gloss (line 38); capex and "counted as a cost" (line 55); goodwill/intangibles glosses (line 92); tag "[Q1 FY2027 call; 10-K FY2026, Item 1A]" (line 96); preferred-stock gloss (line 102); receivables (line 110); tier 1 (line 112); days of inventory (line 114); lead independent director (line 137); fixed-rate notes (now in the §7 table, line 146). outlook.md run rate (line 27), tier 1 (line 29), scale-out (line 31), sequentially (line 39).

### 4. Word counts (coordinator's definition: prose excluding tables, glossary, sources list, and tags)

- business.md: **2,858** prose words (raw 4,811; tables 1,325; glossary + sources ~330; tags the rest). Within 2,000–3,000.
- outlook.md: **1,173** prose words (raw 1,730; tables 455). Within 800–1,200.

### 5. Claims

All 12 are single-direction and gradeable:
- 7 (rewritten): "restates that TIA and driver revenue will exceed a $1 billion annualized run rate within the next few quarters, or reports that it already has" — both branches point the same way (target intact or beaten); Met / Missed (walked back) / Dropped (silent) without judgment.
- 9 (rewritten): one clause, "again describes the new … XPU program as progressing on schedule toward volume production"; Met if reiterated, Missed if a delay is disclosed, Dropped if silent. Note the quote says "progress very well through development"; "on schedule" is a fair reading.
- 11 (rewritten): labeled "(Disclosure check, not a management claim.)", the "consistent with" clause removed; pure number check.
- 1–6, 8, 10, 12: unchanged and already gradeable.
None flagged.

### 6. Structure and glossary

GAAP/non-GAAP paragraph now precedes the §3 table (line 38 before line 40) and opens with "The table below shows two versions of each margin." Glossary contains XPU (corrected to "industry shorthand"), XPU-attach, ASIC, DSP, TIA, Scale-out / scale-up, Foundry, GAAP / non-GAAP, Amortization, Goodwill, Capex; CPO removed. Confirmed.

### Fixed directly in cycle 2

- business.md §4 bridge table row label: "Depreciation added back (a non-cash cost left inside the adjusted profit)" → "Depreciation and other non-acquisition amortization added back (non-cash costs left inside the adjusted profit)". The 10-K (line 1705) calls the $348.6M "depreciation and amortization"; number unchanged.
- business.md glossary, Goodwill: "until judged impaired" → "until judged impaired (worth less than the amount booked)".

### Final verdict: **PASS**

No substantive failure remains. One note for the owner, not a failure: raw word counts including tables are 4,811 (business.md) and 1,730 (outlook.md); the prose-only counts are inside the §3 targets. If the owner counts tables, §7's capital-allocation table and §6#6's earn-out table are the first candidates to trim.
