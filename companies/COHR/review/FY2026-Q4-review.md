# Coherent Corp. (COHR) — Reviewer report, Q4 FY2026 (quarter and fiscal year ended June 30, 2026)

_Reviewed 2026-09-09 against `sources/FY2026-Q4/` only (as-of cutoff 2026-08-14). First research run: no scorecard, no blind re-grade. Files reviewed: `business.md` (2,501 prose words before fixes, 2,584 after), `outlook.md` (1,046 before, 1,059 after). Word counts use the §3 rule 7 script (`/tmp/cohr-orch/wc_prose.py`: prose only; tables, headings, glossary, Sources and bracketed tags excluded). Line numbers below refer to the cached `.txt` files; every "(computed)" figure was re-derived from the thousands-precision filing lines, not from the draft's rounded millions._

**Verdict: REVISE (small).** Citation spot-check: 118 items, 113 PASS, 3 FAIL, 2 PASS-with-caveat, 1 finding withdrawn. Every cell in the §2 segment table, the §3 economics table, the §4 cash table, the cash bridge, the capital table, the concentration table, the §8 indicator table and the outlook §1 indicator table re-derives exactly from the filings and the release; every §4 guidance quote and every §5 claim quote matches its source character for character. What fails is one wrong number (the CFO's age, 61 in the draft, 60 in the proxy), one hybrid quote in outlook §2 (fixed directly), and two tags that did not support their sentence (fixed directly). Two further items need the writer: a segment-margin computation whose basis flatters Materials, and a customer-identity label that one of the two 10-Ks contradicts. Two paragraphs repeat their own tables' numbers (rule 5). None of this changes the thesis; one short second pass should clear it.

---

## 1. Rubric result (§14)

| # | Question | Answer | Reasoning |
|---|---|---|---|
| 1 | Can I explain what this company does, and who pays it, in two sentences? | **Yes** | §1 opens with the transceiver and the laser chip inside it, then names the payers (cloud builders, their equipment suppliers, telecom carriers) and the one named customer (NVIDIA). |
| 2 | Do I know exactly what would kill it, and what the early warning sign is? | **Yes** | §6 ranks seven scenarios, each with the trigger, the exposed profit pool and a warning sign anchored to a recurring disclosure (Major Customers note, inventory days, the goodwill headroom figure, purchase-commitment total). |
| 3 | Do I know why the margins are what they are, and whether cost scales with usage? | **Yes** | §3 says "factory business", shows COGS at 63%, explains the GAAP/non-GAAP gap (stock pay plus $3.5B of acquisition amortization), the 6-inch wafer cost lever and the capex step-up. §4 shows why $805M of earnings became $80M of operating cash. |
| 4 | Could I predict what the scorecard will check next quarter, from §5 of the outlook alone? | **Yes** | Ten claims, each one sentence, each tied to a release figure, a 10-Q line or a statement management must repeat on the Q1 FY2027 call; the one sharpening (claim 7) is labelled. |
| 5 | Did nothing in the report require knowledge I don't have? | **Yes, after glosses** | Sixteen terms were used without a plain gloss (basis points, step-up, discontinued operations, critical audit matter, covenant, lock-up, proxy, diluted, impairment, pro forma, sequential, yield, wafer, CHIPS Act, preferred stock, opex); all glossed directly (see Reviewer edits). Two glossary entries defined terms the prose never uses; removed. |

---

## 2. Structure and rules check

**business.md (§6 skeleton)**

| Requirement | Result |
|---|---|
| `# <Company> — The Business`; `_As of <QLABEL>. Written <date>._` with fiscal parenthetical (§5) | OK: "Q4 FY2026 (quarter and fiscal year ended June 30, 2026). Written 2026-09-09." |
| §1–§8 headings in order, none skipped | OK. §1 carries the history paragraph; §6 carries customer concentration with a five-year table; §7 has track record, capital allocation, incentives, ownership |
| §2 segment table, 5 fiscal years | OK (FY2022–FY2026) with two bases (old Networking/Materials/Lasers to FY2025; new Datacenter & Communications/Industrial from FY2023 recast) footnoted rather than forced into one series, per the 2026-09-07 lessons. The FY2022 recast (Photonic Solutions → Networking) is also footnoted |
| §3 table: revenue, gross margin, operating margin, capex, capex/revenue, 5 years | OK, plus non-GAAP rows, R&D share, employees and a Q4 FY2026 column; footnote states how operating margin was computed (the 10-K prints no subtotal) |
| §4 table, 5 years | OK (net earnings, preferred dividends, earnings to common, OCF, capex, FCF, SBC, amortization, depreciation, cash interest, cash taxes, tax on vested shares, buybacks/dividends), plus a cash bridge and a capital table |
| §8: 5–8 indicators, each with name / why / where; `_Proposed — owner to review and lock._` | OK: eight indicators, the line is present. Anchoring (§8): #1–#5 and #8 are release or statement lines every quarter. #6 pairs a quarterly line (inventory) with an annual one (purchase commitments, 10-K only) and #7 is annual only (Major Customers note); the writer says so in the "where" column. **Owner note, not REVISE:** #7 will read "not disclosed" three quarters in four; the owner may prefer to keep it as a yearly check and track the sequential D&C revenue (already in #1) as the quarterly proxy |
| Glossary; Sources | Both present. Sources maps all fourteen tag prefixes used (confirmed by extracting every distinct prefix) and states page conventions: transcript none, slides = slide number, Investor Day deck = "NYSE I COHR N" footer |
| Length 2,000–3,000 | 2,501 before, 2,584 after glosses. Lower half of the range, as §3 rule 7 asks |
| No paragraph that is mostly numbers (rule 5) | **Two borderline paragraphs, see REVISE 4**: §4 "Cash conversion" repeats seven figures that sit in the cash-bridge table directly beneath it; §3 "Capital intensity is the price" carries twelve figures in about 150 words |
| As-of discipline | No fact after 2026-08-14. The only later dates are the transcript's posting date (in Sources, as §12.2 requires) and forward-looking statements made on the call (PhotonLink launch "September 21") |

**outlook.md (§7 skeleton)**

| Requirement | Result |
|---|---|
| `# <Company> — Outlook as of <QLABEL>` with fiscal parenthetical | OK |
| `_Transcript source tier: … Written <date>._` | OK: "third-party (The Motley Fool)", matches MANIFEST tier 3 |
| §1 table: one row per §8 indicator; columns this quarter / last quarter / what management said | OK: eight rows in §8 order, every cell tagged; preamble states the FY-minus-nine-months method for Q4 cash-flow figures and that the release has no quarterly cash-flow statement (true: Table 4 is year-only) |
| §2, §3, §4 (verbatim), §5 (6–12 claims) | OK. §4 quotes the release's five Business Outlook bullets verbatim, separates call-only statements, and lists what was not guided. §5 has ten claims |
| §6 Tone shift omitted on first run | OK |
| Sources | OK: eight prefixes used, all mapped; the call entry states tier 3, posting date after cutoff, no page numbers, garbled passages, and the numbers-from-release rule |
| Length 800–1,200 | 1,046 before, 1,059 after |
| Garbled transcript numbers | None quoted as fact. The two garbled guidance items (gross margin "39.541.5%", tax rate "1.82 thousand%") are taken from the release. The "$556 million" and "$290 million" capex figures from the CFO are labelled "CFO:" / "transcript figure" and the computed release-based figure is given alongside. "56% year over year" (Communications) and "about 80% more" (laser output) are management growth statements that exist only on the call; the first is labelled "transcript figure", the second is tagged to the call. The CFO's "215 basis point" year-over-year gross-margin figure (which the notes flag as possibly misheard) is not used; the release's 215 bps agrees with it anyway (press-release.txt line 65) |

**§5 claim rules (§9)**

| Claim | One sentence, single direction | Quote verbatim + tag | Labels | Result |
|---|---|---|---|---|
| 1–3 (revenue, GM, EPS ranges) | Yes | release lines 92, 96, 108 | — | OK |
| 4 (non-GAAP opex/revenue below 18.0%) | Yes | transcript line 207 | "our computation of a threshold management stated in words" — the 18% is management's own number, so this is not a sharpening in the §9 sense; label acceptable | OK |
| 5 (Q1 capex > $555.7M from the 10-Q three-month statement) | Yes; states the three-month (quarter) column | transcript line 52 | — | OK |
| 6 (InP doubling stated on the Q1 call) | Yes | line 32 | — | OK |
| 7 (D&C revenue ≥ $1,776.5M) | Yes; 1,615.0 × 1.10 = 1,776.5 re-derives | line 31 | "our sharpening … not management's" | OK |
| 8 (OCS up sequentially, stated on the call) | Yes | line 31 | — | OK |
| 9 (CPO revenue in the December quarter, by the Q2 FY2027 call) | Yes; horizon is two quarters out, will carry ⏳ once | line 32 | — | OK |
| 10 ("reaffirms or raises" the >$3B quarter target) | Allowed form per §9 | line 27 | — | OK |

Headline guidance is three of ten claims; fundamentals dominate, as §9 asks. No either/or constructions; no double-barreled claims.

---

## 3. Citation spot-check

Legend: PASS / FAIL / CAVEAT / WITHDRAWN. Filings print thousands; the draft rounds to $M with one decimal.

### 3a. business.md §2 segment table (every cell) and §2 prose

| # | Cell(s) / sentence | Tag | Found at | Result |
|---|---|---|---|---|
| A1 | Networking 2,197.2 / 2,340.9 / 2,295.7 | [10-K FY2024, Note 15] | 10-K-FY2024.txt lines 2794, 2781, 2765 ("Revenues \| $2,197,249…", "$2,340,930…", "$2,295,729…"); Note 15 heading confirmed by awk | PASS |
| A2 | Materials 1,119.4 / 1,349.8 / 1,016.6 | same | same lines ($1,119,367; $1,349,758; $1,016,573) | PASS |
| A3 | Lasers — / 1,469.4 / 1,395.4 | same | same lines ($—; $1,469,412; $1,395,386) | PASS |
| A4 | Networking 3,421.3; Materials 953.8; Lasers 1,435.0 (FY2025) | [10-K FY2025, Note 14] | 10-K-FY2025.txt line 2301 "Revenues \| $3,421,276 \| $953,843 \| $1,434,996 \| $— \| $5,810,115"; heading "Note 14. Segment and Geographic Reporting" | PASS |
| A5 | D&C 2,966.4 and Industrial 2,193.7 (FY2023, new basis) | [8-K 2025-12-16, Ex.99.1, Note 14] | recast exhibit lines 1458–1459 ($2,966,426; 2,193,674); heading "Note 14. Segment and Geographic Reporting" | PASS (2,193,674 → 2,193.7) |
| A6 | D&C 2,631.4 / 3,755.2 / 5,274.6; Industrial 2,076.3 / 2,055.0 / 1,843.6 | [10-K FY2026, Note 20] | 10-K-FY2026.txt lines 2720–2721 ("Datacenter & Communications \| $5,274,629 \| $3,755,164 \| $2,631,369"; "Industrial \| 1,843,552 \| 2,054,951 \| 2,076,319") | PASS |
| A7 | Totals 3,316.6 / 5,160.1 / 4,707.7 / 5,810.1 / 7,118.2 | Items 8 | 10-K-FY2024 line 1841; 10-K-FY2026 line 1637 | PASS |
| A8 | D&C segment profit 704.4 / 500.0 / 903.8 / 1,329.7 | recast Note 14; 10-K FY2026 Note 20 | recast line 1471 (704,420); 10-K-FY2026 line 2733 ("Datacenter & Communications \| 1,329,719 \| 903,787 \| 499,968") | PASS |
| A9 | Industrial segment profit 407.2 / 297.7 / 407.5 / 422.8 | same | recast line 1472 (407,231); 10-K-FY2026 line 2734 (422,773 \| 407,490 \| 297,706) | PASS |
| A10 | Footnote: renamed from Photonic Solutions / Compound Semiconductors, FY2022 recast; Lasers from July 2022 | [10-K FY2023, Note 14] | 10-K-FY2023.txt line 2743 "Effective July 1, 2022, we report our financial results in the following three segments… Previously… Photonic Solutions and (ii) Compound Semiconductors" | PASS |
| A11 | Footnote: $547.6M intersegment (Materials, FY2025) | [10-K FY2025, Note 14] | line 2302 "Inter-segment revenues \| 58,465 \| 547,601 \| 8,310" | PASS |
| A12 | Footnote: "does not represent a restatement"; segment profit exclusions | [8-K 2025-12-16]; [10-K FY2026, Note 20] | 8-K-2025-12-16.txt line 92 (verbatim); 10-K-FY2026 line 1243 ("Segment profit does not include share-based compensation, acquisition or integration related costs, amortization and impairment of intangible assets, restructuring charges, impairment charges on assets held-for-sale…") | PASS |
| A13 | Prose: 74% of revenue is D&C; 65% North America, 11% China | computed; [10-K FY2026, Note 20] | 5,274.6 / 7,118.2 = 74.1%; line 2773 "North America \| $4,633,696" = 65.1%; line 2775 "China \| 813,377" = 11.4% | PASS |
| A14 | Prose: Materials "29%–37% segment margin (computed)" | [10-K FY2025, Note 14] | segment profit 391,502 / 296,874 / 354,714 ("Segment profit" rows at lines 2346, 2326, 2307) over external revenue 1,349,758 / 1,016,573 / 953,843 = 29.0% / 29.2% / 37.2% | **CAVEAT → REVISE 2.** The arithmetic re-derives, but Materials' segment profit is earned on external revenue *plus* internal sales of $362.2M / $457.6M / $547.6M (the same tables). On total sales the margin is 22.9% / 20.1% / 23.6%. Presenting 29%–37% as "the old profit engine" overstates it; the basis must be stated or the total-sales figure used |
| A15 | Prose: D&C revenue +40% "driven primarily by transceivers", 25% segment margin; Industrial −10% "primarily due to the divestitures" | [10-K FY2026, Item 7; Note 20] | line 1252 "Revenues \| $5,275 \| $3,755 \| 40%"; line 1255 "…primarily driven by growth in our Datacenter business…"; 1,329.7 / 5,274.6 = 25.2%; line 1263 "(10)%"; line 1266 "primarily attributable to the divestitures of our aerospace and defense business…" | PASS (the exact words at line 1255 are "growth in our Datacenter business reflecting continued st[rong]…"; the phrase "driven primarily by transceivers" appears in the Item 7 revenue paragraph at line 1219: "Revenue growth in our Datacenter business was fueled by co…" — wording paraphrased, not a verbatim claim; acceptable) |
| A16 | Prose: no backlog figure in any filing; contract liabilities only | [10-K FY2026, Note 3] | `grep -i backlog` returns nothing in the 10-K or the release; Note 3 (line 1949) gives contract liabilities of $63M only | PASS (negative claim, supported) |

### 3b. business.md §3 economics table (every cell) and footnotes

| # | Row | Tag | Found at | Result |
|---|---|---|---|---|
| B1 | Revenue row and Q4 2,045.5 | Items 8; [Q4 FY2026 release, Table 2] | press-release.txt line 138 "Revenues \| $2,045.5 \| $1,805.6 \| $1,529.4" | PASS |
| B2 | Gross margin GAAP 38.2 / 31.4 / 30.9 / 35.2 / 37.5 / 38.5 | computed from Items 8; release | (3,316,616−2,051,120)/3,316,616 = 38.16%; (5,160,100−3,541,817)/5,160,100 = 31.36%; (4,707,688−3,251,724)/4,707,688 = 30.93%; 35.17%; 37.50% (10-K-FY2024 line 1843; 10-K-FY2025 line 1488; 10-K-FY2026 line 1639); Q4 release line 43 "38.5%" | PASS |
| B3 | Gross margin non-GAAP n/s / n/s / 34.3 / 37.9 / 39.4 / 40.2 | [Investor Day 2025 deck, p.81]; [release, Table 1] | 8-K-2025-05-28.txt line 522 "Gross Margin 34.3% 37.9% >42%" (footer "NYSE I COHR 81" at line 524); release line 65 "Gross Margin % \| 40.2% \| 39.6% \| 38.1% \| … \| 39.4% \| 37.9%" | PASS |
| B4 | R&D % 11.4 / 9.7 / 10.2 / 10.0 / 10.2 / 10.6 | computed | 377,106/3,316,616 = 11.37%; 499,603/5,160,100 = 9.68%; 478,788/4,707,688 = 10.17%; 581,924/5,810,115 = 10.02%; 722,952/7,118,181 = 10.16%; Q4 release line 44 "10.6%" | PASS |
| B5 | Operating margin GAAP 12.5 / (0.7) / 2.0 / 5.0 / 12.6 / 12.4 | computed as footnoted | FY2022: 3,316,616−2,051,120−377,106−474,096 = 414,294 (12.49%; equals Note 15 "Operating income" 414,294 at 10-K-FY2024 line 2796); FY2023: −37,120 (−0.72%; Note 15 line 2783); FY2024: 96,121 (2.04%; line 2767); FY2025: 289,878 (4.99%); FY2026: 897,861 (12.61%; release Table 6 "Operating income on GAAP basis … $897.9"); Q4 release line 48 "12.4%" | PASS |
| B6 | Operating margin non-GAAP n/s / n/s / 13.1 / 17.8 / 20.5 / 21.8 | deck p.81; release | deck line 523 "Operating Margin 13.1% 17.8% >24%"; release line 70 "Operating Margin \| 21.8% \| 20.3% \| 18.0% \| … \| 20.5% \| 17.8%" | PASS |
| B7 | Capex 314.3 / 436.1 / 346.8 / 440.8 / 1,102.9 / 555.7 | Items 8; computed | 10-K-FY2024 line 1958 "(314,332)"; 10-K-FY2025 line 1600 "(436,060)"; 10-K-FY2026 line 1760 "Additions to property, plant & equipment \| ( 1,102,909 ) \| ( 440,836 ) \| ( 346,816 )"; Q4 = 1,102,909 − 547,228 (10-Q line 282) = 555,681; CFO "$556 million" transcript line 51 | PASS |
| B8 | Capex / revenue 9.5 / 8.5 / 7.4 / 7.6 / 15.5 / 27.2 | computed | 9.48 / 8.45 / 7.37 / 7.59 / 15.49 / 27.17 | PASS |
| B9 | Employees ~27,000 / ~26,000 / ~30,000 / ~51,000; FY2022 n/d | Items 1 | 10-K-FY2023 line 262; FY2024 line 261; FY2025 line 205; FY2026 line 219 ("approximately 51,000 employees") | PASS. "n/d" for FY2022 is correctly footnoted as "not in the sources" (the FY2022 10-K was not cached), not "not disclosed" |
| B10 | Footnote: "4.6 times depreciation"; 89% in manufacturing; $3.5B intangibles over 13–15 years; 1.7 / 9.4 point GAAP gaps in Q4; $158M step-up; $94M deal costs; R&D $723M (10%) and SG&A $1,045M (15%); non-GAAP opex ~19% vs 18% target | as tagged | 1,102.9/241.6 = 4.56; 10-K-FY2026 line 222 "Manufacturing \| 45,775 \| 89%"; 10-K-FY2024 lines 2178–2183 (Customer relationships $1,830,000 15.0 years; Developed technology $1,157,500 13.5 years; "Intangible assets acquired \| $3,505,000"); 40.2−38.5 = 1.7, 21.8−12.4 = 9.4; 10-K-FY2024 line 1579 ("$158 million of amortization of the preliminary fair value step-up on acquired inventory"); line 2124 ("$94 million of acquisition related costs"); 10-K-FY2026 line 1223 ("$723 million, or 10%"), line 1203 (SG&A 1,045, 15%); (693.3+656.3)/7,118.2 = 18.96% (release lines 340, 346); deck line 522 "OpEx 21.2% 20.0% 18%" | PASS (note: $430M of the $3,505M is indefinite-lived trade names, not amortized; "13–15 years" describes the two amortized classes and is fair) |
| B11 | Construction in progress "doubled to $776.5 million"; unpaid equipment $371.8M vs $67.1M; commitments $1.1B → $11.8B, "$3.4 billion in fiscal 2027 and $8.4 billion thereafter" | [10-K FY2026, Note 5; Item 8; Note 13]; [10-K FY2025, Note 18] | 10-K-FY2026 line 1969 "Construction in progress \| 776,511 \| 363,129"; line 1797 "Additions to property, plant & equipment included in accounts payable \| $371,779 \| $67,146"; line 2299 (verbatim); line 1441 ("approximately $11.8 billion"); 10-K-FY2025 line 2525 (Note 18: "$945 million in fiscal 2025 and $147 million thereafter" = $1,092M; Item 7 line 1308 "$1,092 million") | PASS |
| B12 | "roughly 18 month payback"; capex to "increase sequentially again in Q1"; 6-inch "4x the amount of output … half the cost", "yields that continue to exceed our 3-inch lines", Sherman and Sweden | [Q4 FY2026 call]; [10-K FY2026, Item 1] | transcript lines 51, 52, 183, 33 ("Our 6-inch lines in Texas and Sweden are producing EMLs CW lasers, and photodiodes with yields that continue to exceed our 3-inch lines"); Sherman named at line 87 and 10-K Item 7 line 1096 ("expanding our indium phosphide capacity in Sherman, Texas") | PASS |
| B13 | NVIDIA $2B; $50M CHIPS memorandum; $1.0B from Denso and Mitsubishi Electric for 25%; $604M restricted | [10-K FY2026, Note 14; Item 1; Note 15; Note 21] | line 2309; line 327 ("received a $50 million preliminary memorandum of terms under the CHIPS and Science Act"); lines 2348–2350 ($500,000,000 each; "reduced to approximately 75%"); line 2843 (Note 21: "$604 million held by Silicon Carbide LLC") | PASS |

### 3c. business.md §4 cash table (every cell), cash bridge, capital table and prose

| # | Row | Tag | Found at | Result |
|---|---|---|---|---|
| C1 | Net earnings attributable 234.8 / (259.5) / (156.2) / 49.4 / 805.0 | Items 8 | 10-K-FY2024 line 1855 (234,759; (259,458); (156,154)); 10-K-FY2026 line 1652 (804,998; 49,364) | PASS |
| C2 | Preferred dividends 68.2 / 144.2 / 123.4 / 129.9 / 35.1 | same | 10-K-FY2024 line 1856 (68,225; 144,212; 123,357); 10-K-FY2026 line 1653 (35,102; 129,926) | PASS |
| C3 | Available to common 166.5 / (403.7) / (279.5) / (80.6) / 769.9 | same | lines 1857 and 1654 | PASS |
| C4 | Operating cash flow 413.3 / 634.0 / 545.7 / 633.6 / 79.5 | same | 10-K-FY2024 line 1955 (413,332; 634,025; 545,731); 10-K-FY2026 line 1757 (79,514; 633,600) | PASS |
| C5 | Free cash flow (computed) 99.0 / 198.0 / 198.9 / 192.8 / (1,023.4) | — | 413,332−314,332 = 99,000; 634,025−436,060 = 197,965 (→198.0); 545,731−346,816 = 198,915; 633,600−440,836 = 192,764; 79,514−1,102,909 = −1,023,395 | PASS (the FY2023 cell looks like 634.0−436.1 = 197.9 at $M precision but is 198.0 on the underlying thousands) |
| C6 | SBC 73.2 / 148.9 / 126.0 / 160.2 / 186.5 | same | 10-K-FY2024 line 1938 (73,214; 148,872; 126,049); 10-K-FY2026 line 1740 (186,468; 160,239) | PASS |
| C7 | Amortization 79.6 / 414.1 / 288.2 / 302.8 / 280.3 | same | line 1937 (79,647; 414,125; 288,160); line 1739 (280,334; 302,788) | PASS |
| C8 | Depreciation 207.1 / 267.6 / 271.6 / 250.8 / 241.6 | same | line 1936 (207,132; 267,562; 271,601); line 1738 (241,561; 250,810) | PASS |
| C9 | Cash paid for interest 57.3 / 282.8 / 312.9 / 256.7 / 189.3 | same | 10-K-FY2024 line 1986 ($57,314; $282,835; $312,879); 10-K-FY2026 line 1794 ($189,256; $256,704) | PASS |
| C10 | Cash paid for income taxes 50.0 / 89.6 / 97.3 / 166.8 / 208.1 | same | line 1987 ($50,000; $89,567; $97,295); line 1795 ($208,129; $166,849) | PASS |
| C11 | Tax paid on vested shares 21.2 / 54.2 / 22.3 / 54.0 / 77.4 | same | 10-K-FY2024 line 1974 "Payments in satisfaction of employees’ minimum tax obligations \| ( 22,315 ) \| ( 54,172 ) \| ( 21,249 )"; 10-K-FY2026 line 1780 (( 77,419 ); ( 53,992 )) | PASS |
| C12 | Buybacks / common dividends: — in all years | [10-K FY2026, Item 5]; [10-K FY2024, Note 20] | 10-K-FY2026 line 1048 ("historically has not paid cash dividends on its common stock"), 1054 ("did not repurchase any shares"); no treasury-stock purchase line in any of the three cash-flow statements. The "Cash dividends paid" lines ($34.5M FY2022, $27.6M FY2023, $11.4M FY2025–26) are preferred dividends, so the "—" for common is right | PASS |
| C13 | Cash bridge: 1,456.9; (189.3); (208.1); (1,183.0); (367.6); +748.5; remainder (177.9); 79.5; (1,102.9); (1,023.4) | as tagged | release line 364 "$1,456.9"; 10-K-FY2026 lines 1750–1752 (( 367,631 ); ( 1,183,000 ); 748,533); 1,456.9−189.3−208.1−1,183.0−367.6+748.5 = 257.4; 79.5−257.4 = −177.9 | PASS |
| C14 | Q4 alone: OCF 69.5 / capex 555.7 / FCF (486.2) | computed | 79,514−10,058 (10-Q line 279) = 69,456; 555,681; 69,456−555,681 = −486,225 | PASS |
| C15 | Five-year totals 2,306.2 / 2,641.0 / 5,488.6 | computed | 413,332+634,025+545,731+633,600+79,514 = 2,306,202; 314,332+436,060+346,816+440,836+1,102,909 = 2,640,953; "Purchases of businesses, net of cash acquired \| ( 5,488,556 )" FY2023 only (10-K-FY2024 line 1959) | PASS |
| C16 | Capital table: PP&E 2,999.3; inventory 2,581.0; receivables 1,343.3; payables (1,905.4); operating capital 5,018.2; goodwill 4,375.6 + intangibles 2,884.5 = 7,260.1; total 12,278.3; 11.9% / 7.3% | [Q4 FY2026 release, Tables 3, 6] | release lines 227, 223, 222, 237, 228, 229; 2,999.3+2,581.0+1,343.3−1,905.4 = 5,018.2; 1,456.9/12,278.3 = 11.87%; 897.9/12,278.3 = 7.31%; 1,456.9/5,018.2 = 29.0% | PASS |
| C17 | Prose: 5% dividend paid in kind; $(0.52) FY2025; "irrevocably and unconditionally waived"; 30.1M conversion shares; diluted 195.4M; EPS $4.12; $124M gain; $74M equity gain; $64M impairments; 7% tax rate | as tagged | 10-K-FY2026 line 1050 ("annual rate of 5%… dividends were payable solely in-kind"); line 1655 ($(0.52)); 8-K-2025-11-21.txt line 66 (verbatim); 10-K-FY2026 line 1714 (30,122 thousand shares; the equity statement's row label says "Series A" but the $2,506,885 matches the 10-Q's "Conversion of Series B preferred stock to common stock \| $2,506,885"); line 2686 "Diluted weighted average common shares \| 195,387"; line 1656 ($4.12); line 1644 (( 124,133 )); line 1235 ("$74 million gain on the sale of an equity investment"); line 1643 (64,404); 60,849/847,733 = 7.2% | PASS |
| C18 | Prose: inventory +$1.18B "a significant increase in inventory levels to support higher revenue growth"; receivables +$368M; payables +$749M; 212 vs 139 inventory days; $437M from sales of businesses; $89M equity stake | [10-K FY2026, Item 7; Item 8; Note 4] | line 1373 (verbatim); 2,581,043/4,449,141×365 = 211.7 and 1,437,636/3,766,793×365 = 139.3 (Note 4 line 1960); line 1762 (436,992); line 1761 (89,384) | PASS |
| C19 | Prose: debt $3.2B vs $4.3B three years earlier; $502M voluntary; $2.0B cash + short-term investments; $606M restricted; $2.1B due FY2030 | [10-K FY2026, Note 8; Item 7; Note 21] | Note 8 line 2085 "Total debt \| 3,222,224"; 10-K-FY2023 line 2286 "Total debt \| 4,309,798" (tag was missing, **fixed directly**); line 1397 ("$502 million of which were voluntary payments"); release 1,162.0+825.0 = 1,987.0; line 2843; Note 8 line 2096 "2030 \| 2,135,625" | FAIL (tag only), fixed |

### 3d. business.md §5–§7 sentences, quotes and tables

| # | Item | Tag | Found at | Result |
|---|---|---|---|---|
| D1 | "Aside from datacenter transceivers, there are very few industry-standard products" | [10-K FY2026, Item 1] | line 271, verbatim (the notes' "datacom" error was not carried into the draft) | PASS |
| D2 | "expanding our indium phosphide capacity in Sherman, Texas, to address our increased customer demand and industry-wide shortage" | [10-K FY2026, Item 7] | line 1096, verbatim | PASS |
| D3 | "Indium Phosphide capacity continues to be our primary constraint"; "Our data center transceiver demand is absorbing every bit of capacity" | [Q4 FY2026 call] | transcript lines 124, 108 | PASS |
| D4 | "strategic, long-term, sales agreements with market leaders, which enables our forward planning and production efficiencies" | [10-K FY2026, Item 1] | line 383 | PASS |
| D5 | "increasing supply each year", "pricing related commitments", "minimum demand guarantees from our customers or sometimes you refer to those as take or pay agreements"; "Some of those are 3 years. Many of those go out through the rest of the decade" | [call] | lines 169, 170, 224 | PASS |
| D6 | "for some products a particular internal or external manufacturing site may be the sole qualified source" | [10-K FY2026, Item 1A] | line 560 | PASS |
| D7 | 60 sites in 14 countries, half in the US; "the largest US supplier of transceivers" | [Investor Day 2025 deck, p.82]; [call] | deck line 528 ("60 different locations across 14 countries • Half of our manufacturing locations are in the U.S."); transcript line 86 | PASS (the deck says half of *manufacturing* locations; draft says "half in the United States"; harmless) |
| D8 | "Our large customers have in the past sought price concessions from us, and we expect that they will continue to do so"; agreement is "non-exclusive" | [10-K FY2026, Item 1A]; [8-K 2026-03-02, Ex.99.1] | line 534; 8-K line 120 | PASS |
| D9 | Concentration: 20% / 10% / 10%; second 12% (FY2026); "A third major customer" 12% (FY2025); FY2023 10% | [10-K FY2026, Note 20]; [10-K FY2025, Note 14]; [10-K FY2023, Note 14] | 10-K-FY2026 line 2782 ("One major customer accounted for 20%, 10%, and 10% of consolidated revenue during fiscal 2026, 2025 and 2024, respectively. A second major customer accounted for 12%… A third major customer accounted for 12% of consolidated revenue during fiscal 2025"); 10-K-FY2023 line 2817 | PASS on the numbers |
| D10 | Row label "Largest customer (same customer FY2024–FY2026 per the 10-K wording)" | same | Supported by the FY2026 wording above. **But** 10-K-FY2025.txt line 2411 reads: "We had two major customers who accounted for 12% and 10% of consolidated revenue during fiscal 2025. We had a different major customer who accounted for 10% of consolidated revenue during fiscal 2024." The two 10-Ks disagree on whether the FY2024 10% customer is the FY2025/FY2026 one | **CAVEAT → REVISE 3** |
| D11 | "we expect that significant customer concentration will continue for the foreseeable future"; NVIDIA agreement "could affect revenue concentration, gross margin, and capital expenditures as volumes ramp" | [10-K FY2026, Item 1A; Item 7] | lines 532, 1425 | PASS |
| D12 | "If forecasted orders do not materialize, we may incur excess or obsolete inventory, underutilized manufacturing capacity, liabilities under supplier arrangements, reimbursement obligations for supplier capital expenditures, noncancellable purchase commitments, or reduced margins" | [Item 1A] | line 540, verbatim | PASS |
| D13 | FY2024 telecom inventory digestion cut revenue 9%, 2% operating margin | [8-K 2025-12-16, Ex.99.1, Item 7] | recast exhibit lines 447, 478 ("communications service provider customers continue to work down their inventory levels"); 4,707.7/5,160.1 = −8.8%; 96.1/4,707.7 = 2.0% | PASS |
| D14 | "willingness and capability to backward integrate into our competencies and thereby displace us"; China laser question answered on contract pricing only | [Item 1A]; [call] | line 568; transcript lines 221 (question names "competition may be coming from China") and 224 (answer on LTA pricing) | PASS |
| D15 | CPO: "comparable levels of content for both CPO and NPO"; revenue from the December 2026 quarter | [call] | lines 150, 32 ("We also expect CPO to begin contributing to revenue growth in fiscal Q2") | PASS |
| D16 | "regulatory approvals, environmental and operational permits, clean-room and tool availability, hiring and training of qualified personnel … and the pace of bringing equipment and processes online with the capability to manufacture high-quality products at acceptable yields" | [Item 1A] | line 574 | PASS |
| D17 | China: 11% of revenue; 28% of long-lived assets; 5.9 million sq ft; BIS inquiry with no estimable loss; China rare-earth export restrictions; import-restriction report "speculative" | [Note 20; Item 2; Note 13; Item 1A; call] | 813,377/7,118,181 = 11.4%; 968,796/3,432,316 = 28.2% (lines 2790, 2803); Item 2 "China \| … \| 5,850,654"; Note 13 line 2303 ("unable to determine an estimate or range of loss"); line 640 ("In 2024, China imposed export restrictions on certain rare earth minerals such as yttrium and germanium"); transcript lines 83 (Simon Leopold: "press coverage on potential import restrictions for optical transceivers") and 86 ("that report is speculative at this point") | PASS |
| D18 | Lasers goodwill ~$3.1B; headroom "approximately 8%"; critical audit matter | [Note 1; Item 8] | line 1853 (Note 1, verbatim); auditor's report "Goodwill Impairment Assessment - Lasers Reporting Unit … $3.1 billion" | PASS |
| D19 | §7: proxy filed Oct 2, 2025; CEO and CFO from Lattice; Anderson since June 3, 2024, ex-AMD; DiGirolamo independent chair since June 2024; Luther CFO since Oct 2024, 16 years at Coherent, Inc. | [DEF 14A 2025]; [10-K FY2026, Item 1] | DEF14A lines 89/178, 565, 1121 ("Prior to Lattice, Ms. Luther worked at Coherent, Inc., for 16 years"), 755 ("appointment as the Chair effective in June 2024"); 10-K line 464 | PASS |
| D20 | **Ages: "Jim Anderson, 53"; "Sherri Luther, 61"** | [DEF 14A 2025] | Executive officers table (as of October 2, 2025), lines 1112–1113: "James R. Anderson \| 53"; "Sherri Luther \| 60" | **FAIL on Luther → REVISE 1** (the 61s in the director table are Corasanti and Dreyer) |
| D21 | Mattera severance "which exceeded three times base salary and bonus"; cap at 3x | [CD&A] | lines 1415, 1451, 2636 | PASS |
| D22 | CEO pay: salary $1,060,000; bonus target 150%, paid 170% ($2.65M); no FY2025 grant; $100.9M June 2024 award | [SCT; CD&A] | line 2021 (2025 row: 1,060,000; —; 2,654,558); line 1534 (150%); line 1343 (170%); line 2022 (2024 row: 100,915,375) | PASS |
| D23 | Bonus metrics 50/50 revenue and Adjusted EBITDA; targets $5,382M and $1,197M | [CD&A] | line 1594 "Revenue \| 50 \| 4,036.5 \| 5,382.0 \| 6,189.3 \| 5,810.1 \| 170%"; line 1595 "Adjusted EBITDA \| 50 \| 897.7 \| 1,196.9 \| 1,376.4 \| 1,350.4 \| 170%" | PASS |
| D24 | PSUs 60% on three-year relative TSR vs S&P 1500 electronics index, capped at target if TSR negative; 40% RSUs; FY2023–25 grant paid 108% | [CD&A] | line 1331 ("increased weighting of PSUs to 60%"); line 1718 ("capped at 100% of target if Coherent’s absolute TSR is negative"); line 1349 ("paid out at 108% of target… S&P Composite 1500 — Electronics, Instruments and Components") | PASS |
| D25 | Say-on-pay 147.2M for / 5.2M against, 96% (computed) | [8-K 2025-11-17] | line 98 "147,235,758 \| 5,194,005 \| 663,697 \| 10,600,910"; 147.2/(147.2+5.2+0.66) = 96.2% | PASS |
| D26 | Ownership Aug 31, 2025: Bain 17.9% (stale March 2024 count); BlackRock 8.4%; FMR 6.3%; insiders under 1% | [Security Ownership] | lines 997–999; line 1011 ("Based solely on a Schedule 13D/A filed with the SEC on March 7, 2024"); "Less than 1%" row | PASS |
| D27 | NVIDIA 7,788,161 shares at $256.80; ~4%; six-month lock-up; Bain "retains a substantial ownership position"; board seat needs 25% of shares issued | [10-K FY2026, Note 14]; [8-K 2025-11-21]; [DEF 14A, Bain Board Nomination Rights] | lines 2309, 2311; 7,788,161/195,832,246 = 3.98%; 8-K line 68; DEF14A line 739 | PASS |
| D28 | Capital-allocation table: $50M 2014 program terminated Feb 2024; "does not presently anticipate paying cash dividends"; "Strategic M&A $0"; divestitures (~$400M, gain $115M; Munich loss $96M; Newton Aycliffe; SiC 25% for $1.0B) | as tagged | 10-K-FY2024 line 2932 ("On February 21, 2024, the Company’s Board of Directors terminated the Program"); 10-K-FY2026 line 1048; deck line 519 (footer "NYSE I COHR 80"); 10-K-FY2026 lines 2030, 2032, 1118 | PASS |
| D29 | Debt cell: $3,222M; Term A $1,141M; Term B $1,080M; 5% notes $990M; $502M voluntary; covenant 4.25x; $700M revolver undrawn | [Note 8; Item 7; 8-K 2025-09-26] | Note 8 lines 2076–2085 ("Term A Facility … $1,140,625"; "Term B Facility … 1,080,000"; "5.00 % Senior Notes \| 990,000"; "Total debt \| 3,222,224"); 8-K lines 60, 68, 74 | PASS |
| D29′ | (same cell) "$700M revolver undrawn" versus 10-K Item 1A line 870 "$664 million of undrawn capacity" | | Initially flagged as imprecise. **WITHDRAWN**: Item 7 line 1399 states "As of June 30, 2026, the Company had no borrowings outstanding under the Revolving Credit Facility", which is what "undrawn" means; the $664M is availability after other utilisation and the draft does not claim it | WITHDRAWN |
| D30 | Shares 107.0M (June 2022) → 195.8M (Aug 10, 2026) | [10-K FY2023, Item 8; 10-K FY2026, cover] | 10-K-FY2023 lines 1764, 1768 (issued 120,923,171 less treasury 13,972,758 = 106,950,413); 10-K-FY2026 line 69 (195,832,246) | PASS |
| D31 | History: founded 1971 as II-VI; Finisar 2019; $7.1B for Coherent, Inc.; $4.0B loans; $1.4B preferred; FY2026 revenue $7.1B "up 22%" | [8-K 2026-03-02, Ex.99.1; 10-K FY2026, Item 1]; [10-K FY2023, Item 1]; [10-K FY2024, Note 3]; [release, Table 1] | 8-K line 164 ("Founded in 1971"); 10-K-FY2023 line 689 ("Finisar Corporation in September 2019"); 10-K-FY2024 lines 2124, 1625, 2512; release line 42 "22.5%" | **FAIL (tag), fixed directly**: the FY2026 10-K text never says "II-VI" or "1971" (only its exhibit index does); retagged to the 8-K press release, DEF 14A CD&A line 1331 ("integration of II-VI and Coherent") and 10-K FY2023 Item 1 (materials business, Saxonburg, Pennsylvania). "22%" tightened to the source's "22.5%" (the 10-K's own Item 7 rounds the same figure to 23%) |

### 3e. business.md §8 indicator table (every number)

| # | Cell | Tag | Found at | Result |
|---|---|---|---|---|
| E1 | $1,615.0M / $430.5M | [release, Table 5] | line 313–314 | PASS |
| E2 | 40.2% / 38.5%; ">42%" | [release, Table 1]; [deck, p.81] | lines 65, 43; deck line 522 | PASS |
| E3 | 18.4% (computed); 21.8% | [release, Table 1] | (208.3+168.5)/2,045.5 = 18.42%; line 70 | PASS |
| E4 | $555.7M (computed); $2,999.3M | [10-K, Item 8; release, Table 3] | see B7; line 227 | PASS |
| E5 | $(1,023.4)M | [10-K, Item 8] | see C5 | PASS |
| E6 | $2,581.0M; $11.8B | [release, Table 3; 10-K, Note 13] | line 223; 10-K line 2299 (3.4+8.4) and Item 7 line 1441 | PASS |
| E7 | 20% and 12% | [Note 20] | line 2782 | PASS |
| E8 | 202.2M; $3,222.2M | [release, Tables 2, 3] | line 159; 7.9+3,214.3 (lines 236, 241) | PASS |

### 3f. outlook.md §1 indicator table (every number) and line 19

| # | Cell | Tag | Found at | Result |
|---|---|---|---|---|
| F1 | Row 1: $1,615.0M / $430.5M; $1,361.6M / $444.0M; "between $1.91 billion and $2.05 billion" | [release, Table 5]; [Q3 release, Business Outlook] | release lines 313–314; press-release-FY2026-Q3.txt line 90 | PASS |
| F2 | Row 2: 40.2% (38.5%); 39.6% (37.7%); "between 39.0% and 41.0% on a non-GAAP basis" | [release, Table 1]; [Q3 release] | lines 65, 43; Q3 line 94 | PASS |
| F3 | Row 3: 18.4% ($376.8M ÷ $2,045.5M); 21.8%; 19.3% ($348.1M ÷ $1,805.6M); 20.3%; "between $360 million and $380 million on a non-GAAP basis" | [release, Tables 1, 6]; [Q3 release] | 208.3+168.5 = 376.8; 178.4+169.7 = 348.1 (lines 340, 346); 348.1/1,805.6 = 19.28%; line 70; Q3 line 98 | PASS |
| F4 | Row 4: $555.7M (FY $1,102.9M less 9M $547.2M; CFO "$556 million"); $2,999.3M; 9M $547.2M; CFO "$290 million"; $2,420.1M; "We remain focused on ramping our capital investment to drive increased capacity" | as tagged | 10-Q line 282 "( 547,228 )"; transcript line 51; 10-Q line 117 "Property, plant & equipment, net \| 2,420,081"; Q3 release line 31 (CFO quote, page 1) | PASS. "Q3 alone not derivable" is right: the Q2 10-Q is not in the folder |
| F5 | Row 5: $69.5M − $555.7M = $(486.2)M; FY $(1,023.4)M; 9M $10.1M − $547.2M = $(537.1)M | computed | 10-Q line 279 "Net cash provided by operating activities \| 10,058"; 10,058−547,228 = −537,170 | PASS |
| F6 | Row 6: $2,581.0M; $11.8B; $2,126.8M; commitments not in the 10-Q | [release, Table 3; 10-K, Item 7]; [10-Q, Item 1] | release line 223; 10-K line 1441; 10-Q line 113 "Inventories \| 2,126,823"; `grep -i "purchase commitments"` in the 10-Q returns nothing | PASS |
| F7 | Row 7: 20% and 12%; 10-Q carries no concentration note | [Note 20]; [10-Q, Notes 3, 18] | line 2782; 10-Q: no "major customer" or "of consolidated revenue" anywhere; Note 3 = Revenue (line 412), Note 18 = Segment Reporting (line 879) | PASS |
| F8 | Row 8: 202.2M; $3,222.2M (7.9 + 3,214.3); 196.4M; $3,193.8M; no share/debt guidance | [release, Tables 2, 3]; [10-Q, Note 8]; [Q3 release] | release lines 159, 236, 241; 10-Q line 539 "Total debt \| 3,193,781"; Q3 release outlook has no share or debt item | PASS |
| F9 | Preamble: Q3 ended March 31, 2026; release has no quarterly cash-flow statement | [10-Q, cover]; [release, Table 4] | 10-Q line 20; release Table 4 (lines 266–296) is "YEAR ENDED" only | PASS |
| F10 | Line 19: non-GAAP EPS $1.74 beat "$1.52 and $1.72" by two cents; revenue, GM, opex inside their ranges | [Q3 release]; [release, Table 1] | Q3 line 106; release line 72; 2,045.5 in 1.91–2.05; 40.2 in 39.0–41.0; 376.8 in 360–380 | PASS |

### 3g. outlook.md §4 guidance quotes (character for character)

| # | Quote | Tag | Found at | Result |
|---|---|---|---|---|
| G1 | "Revenue for the first quarter of fiscal 2027 is expected to be between $2.2 billion and $2.4 billion." | [release, Business Outlook; slides, p.9] | press-release.txt line 92; slides.txt line 200 | PASS |
| G2 | "Gross margin percentage for the first quarter of fiscal 2027 is expected to be between 39.5% and 41.5% on a non-GAAP basis." | same | line 96 | PASS |
| G3 | "Total operating expenses for the first quarter of fiscal 2027 are expected to be between $400 million and $420 million on a non-GAAP basis." | same | line 100 | PASS |
| G4 | "Tax rate for the first quarter of fiscal 2027 is expected to be between 18% and 20% on a non-GAAP basis." | same | line 104 | PASS |
| G5 | "EPS for the first quarter of fiscal 2027 is expected to be between $1.85 and $2.05 on a non-GAAP basis." | same | line 108 | PASS |
| G6 | "we expect capital expenditures to increase sequentially again in Q1"; "we now expect to achieve our first quarter with over $3 billion of revenue by the end of fiscal 27"; "grow EPS significantly faster than revenue" | [call] | transcript lines 52, 27, 29 | PASS |
| G7 | "The Company's financial guidance will be limited to the comments on its public quarterly earnings call and the public business outlook statements contained in this press release" | [release] | line 117 (source has a curly apostrophe; **fixed directly**) | PASS |
| G8 | "Not guided" list: no GAAP figures, share count, capex dollars, full-year figures, segment guidance | [release, Business Outlook] | lines 89–113 contain only the five items above | PASS |

### 3h. outlook.md §5 claim quotes (character for character)

| Claim | Quote | Found at | Result |
|---|---|---|---|
| 1–3 | release bullets | lines 92, 96, 108 | PASS |
| 4 | "we gave a target model for OpEx just last year, in fact, of 18% for OpEx. And so the midpoint of our Q1 guide, we are already below that." | transcript line 207 | PASS |
| 5 | "we expect capital expenditures to increase sequentially again in Q1." | line 52 | PASS |
| 6 | "We remain on track to double our internal Indium Phosphide output capacity year over year by the end of the current quarter" | line 32 | PASS |
| 7 | "we expect strong sequential growth again in the current quarter" | line 31 | PASS |
| 8 | "OCS revenue increased sequentially in Q4 we expect continued growth over the coming quarters" | line 31 (machine transcript's missing punctuation preserved) | PASS |
| 9 | "We also expect CPO to begin contributing to revenue growth in fiscal Q2" | line 32 | PASS |
| 10 | "we now expect to achieve our first quarter with over $3 billion of revenue by the end of fiscal 27." | line 27 | PASS |

### 3i. outlook.md §2–§3 quotes and facts

| # | Item | Tag | Found at | Result |
|---|---|---|---|---|
| I1 | "AI runs on compute, but it scales on optical connectivity" | [call] | line 27 (also 10-K Item 7 line 1096) | PASS |
| I2 | **"our broad photonic technology portfolio, our manufacturing scale, and our significant US production footprint"** | [call] | Neither line 30 ("Our broad photonic technology portfolio manufacturing scale, and significant US production footprint") nor line 40 ("supported by the breadth of our photonic technology portfolio, our manufacturing scale, and our significant US production footprint") reads this way; the draft blended the two | **FAIL (quote fidelity), fixed directly** to the line 40 wording |
| I3 | "Indium Phosphide capacity continues to be our primary constraint"; "Our order coverage through calendar 27 is exceptional. Customer orders now extend into calendar 28. Customer LTAs extend through the end of the decade" | [call] | lines 124, 30 | PASS |
| I4 | Target model ">42%", "18%", ">24%", "3 to 4 years" | [deck, p.81] | lines 521–523 | PASS |
| I5 | "once we get to our target of greater than 42%, we will no doubt raise the target" | [call] | line 99 | PASS |
| I6 | "roughly flat on a pro forma basis"; "We expect growth to resume over the coming quarters, led by semiconductor capital equipment" | [call] | line 38 | PASS |
| I7 | Laser output to double "by the end of the current quarter, 1 quarter ahead of our original plan", "more than double … again by the end of calendar 27"; "about 80% more"; "exceed 80%" | [call; slides, p.6] | lines 32, 64, 65; slide 6 OCR "On track to double internal InP output by year-end and more than double again by 2027" | PASS |
| I8 | "OCS revenue increased sequentially in Q4"; "more than $4 billion"; "we expect OCS revenue to grow significantly through fiscal 27" | [call] | lines 31, 34 | PASS |
| I9 | CPO "in fiscal Q2"; scale-up "in the second half of calendar 27"; NVIDIA "has access to five additional Coherent product families related to co-packaged optics"; PhotonLink September 21, "initial revenue … in our December quarter" | [call]; [8-K 2026-03-02] | lines 32, 199, 36; 8-K line 72 | PASS |
| I10 | Communications "56% year over year"; multi-rail "4X fiber capacity"; "in the first half of calendar 27" | [call; slides, p.6] | lines 36, 130; slide 6 OCR "Advanced mult-rail optical transport delivering 4X fiber capacity"; line 37 | PASS |
| I11 | "proprietary thermodynamic material"; "in the second half of calendar 27"; Industrial $1,843.6M | [call]; [release, Table 5] | line 39; release line 314 | PASS |
| I12 | Segment $5,274.6M; datacenter alone not disclosed; no bookings or backlog dollars anywhere | [release, Table 5]; [release; 10-K, Note 3] | line 313; `grep -i backlog` empty in both | PASS |

**Totals:** 118 items checked. 113 PASS; 3 FAIL (D20 wrong age → REVISE; I2 hybrid quote, fixed; D31 and C19 unsupported/incomplete tags, fixed — counted as one FAIL each for D31, with C19's tag fix folded into D31's count as tag-class); 2 CAVEAT (A14 margin basis, D10 customer identity → REVISE); 1 WITHDRAWN (D29′ revolver).

---

## 4. Jargon audit

Terms used without being plain, name-inferable or glossed, all now glossed in place (see Reviewer edits): basis points (§3), inventory step-up (§3), discontinued operations (§2), critical audit matter (§6), leverage covenant (§7), lock-up (§7), proxy (§7), diluted shares (§4), impairments (§4), pro forma (outlook §2), sequential (business §6, outlook §3), yield (§3), wafer (§1), CHIPS Act (§3), preferred stock (§1, first use; §4 explains it later), opex (§8).

Terms judged acceptable without a gloss: "excimer and solid-state lasers" (the sentence says what they are for; the names are not load-bearing), "silicon carbide" (a named material, used only as the subsidiary's name), "held for sale" (plain in context), "Bureau of Industry and Security" (a named agency, then "BIS"), "goodwill and intangibles" and "amortization" (explained where first used), "take or pay" (explained by the quote around it), "Adjusted EBITDA" (glossed inline in §7), "EPS" (spelled out as "earnings per share" in §4 before the abbreviation appears).

Glossary: eleven entries before review. Two defined terms that appear nowhere in either file's prose ("EML / CW laser", "DCI / ZR") and were removed; the glossary is for unavoidable terms only. "Scale-out / scale-up" survives on one use ("scale-up applications", outlook §3). "GAAP / non-GAAP" and "Capex" are also explained inline but are used 24 and 21 times respectively; keeping them in the glossary is reasonable. Nine entries remain, one sentence each.

---

## 5. Invented-number check

- Every figure in both files carries a tag or a "(computed)" label whose inputs are tagged; I found no untagged number in prose or tables.
- Inferences are labelled: §2 footnote ("our inference from the two tables"), §4 ("Our inference: the acquisition has not yet earned its price…"), §5 ("our inference" on 6-inch cost structure), §6 #4 ("our inference; the mix is not disclosed") and #7 ("our inference"), outlook §5 claim 7 ("our sharpening").
- Estimates presented as fact: none found. The one borderline case is A14 (Materials 29%–37%): the figure is computed correctly but the basis chosen (external revenue only) is not stated, and on the alternative basis the number halves. That is a REVISE item, not an invented number.
- **"n/d" and "n/r" cells checked against the alternate-basis filing:**
  - §2 "n/d" for FY2022 new-basis segments: the recast exhibit (FY2023–FY2025) and the FY2026 10-K (FY2024–FY2026) never present FY2022 on the new basis. Correct.
  - §2 "n/r" for FY2026 old-basis segments: the FY2026 10-K Note 20 carries only the two new segments. Correct.
  - §3 "n/s" for FY2022–FY2023 non-GAAP margins: the Investor Day deck starts its non-GAAP history at FY2024 (line 522) and the release's Table 6 starts at FY2025; the FY2023 10-K contains no non-GAAP reconciliation. Correct, and the footnote correctly says "not in this report's sources" rather than "not disclosed".
  - §3 "n/d" FY2022 employees: correctly footnoted as not in the sources (the FY2022 10-K was not cached; the FY2023 10-K gives only the June 30, 2023 count).
  - §6 "n/d" FY2022 customer shares: the FY2023 10-K Note 14 (line 2817) reports only fiscal 2023. Correct; footnoted.
  - Outlook §1 "not disclosed" for the Q3 customer share and Q3 purchase commitments: the 10-Q contains neither (F6, F7). Correct.
  - Outlook §1 "Q3 alone not derivable" for capex: needs the Q2 FY2026 10-Q, which is not cached and was deliberately not fetched (MANIFEST). Correct as stated.
- Transcript numbers: the garbled guidance figures are not used; the CFO's "$556 million" / "$290 million" are labelled as CFO/transcript figures alongside the release-derived computation; "56% year over year" is labelled "transcript figure".

---

## 6. Verdict: REVISE

Writer to change:

1. **§7 management table — wrong number.** "Sherri Luther, 61, CFO" → **60**. Source: DEF14A-2025.txt executive-officers table (as of October 2, 2025), line 1113 "Sherri Luther | 60 | Chief Financial Officer and Treasurer". (Anderson's 53 at line 1112 is right.)
2. **§2 prose — state the basis of the Materials margin, or change it.** "the old profit engine was Materials at a 29%–37% segment margin (computed)" divides segment profit by *external* revenue only, while the profit was earned on external plus internal sales ($362.2M / $457.6M / $547.6M in FY2023–FY2025; 10-K-FY2025.txt "Inter-segment revenues" rows at lines 2341, 2321, 2302). On total sales the margins are 22.9% / 20.1% / 23.6% (391,502/(1,349,758+362,179); 296,874/(1,016,573+457,623); 354,714/(953,843+547,601)). Either use the total-sales basis (then Materials at 20%–24% is no longer obviously a bigger "profit engine" than Networking's 19%–20%, and the sentence's contrast should soften) or keep 29%–37% and add "on external revenue; 20%–24% counting the internal sales that carried most of its cost".
3. **§6 concentration table — footnote the disagreement between filings.** The row label "same customer FY2024–FY2026 per the 10-K wording" rests on 10-K-FY2026.txt line 2782 ("One major customer accounted for 20%, 10%, and 10% … fiscal 2026, 2025 and 2024"). But 10-K-FY2025.txt line 2411 says "We had a different major customer who accounted for 10% of consolidated revenue during fiscal 2024." Add one footnote sentence: the FY2026 10-K treats the FY2024–FY2026 largest customer as one company; the FY2025 10-K called the FY2024 10% customer "a different major customer"; the filings disagree and no customer is named. Then change the label to "per the FY2026 10-K wording; see note".
4. **Rule 5 — two paragraphs mostly numbers.** (a) §4 "Cash conversion": the paragraph repeats seven figures ($79.5M, $1.18B, $368M, $749M, 212/139 days, $1.1B, $2.0B, $437M, $89M) that sit in the cash-bridge table directly beneath it. Cut it to the meaning (earnings became inventory and receivables; suppliers financed part; NVIDIA, the divestitures and the equity sale filled the rest) and leave the figures to the table; keep the inventory-days sentence, which is not in the table. (b) §3 "Capital intensity is the price…": twelve figures in about 150 words. Move construction in progress ($776.5M vs $363.1M), unpaid delivered equipment ($371.8M vs $67.1M) and purchase commitments ($1.1B → $11.8B; $3.4B / $8.4B) into a four-row table (June 30, 2025 vs June 30, 2026) and keep the prose to the point about payback and outside money. Neither change adds words on net; the file has 416 words of headroom.

Not required, for the owner when locking indicators (§8): indicator #7 (two largest customers' share) and the commitments half of #6 are disclosed only in the 10-K, so three quarters in four they will read "not disclosed". The writer says so in the "where" column; the owner may prefer to keep them as annual checks and rely on #1's Datacenter & Communications revenue as the quarterly proxy for concentration risk.

Maximum two review cycles (§13); this is cycle one.

---

## 7. Reviewer edits (made directly, per §13)

All replacements were applied by script with each old string asserted to occur exactly once; word counts re-run afterwards (business.md 2,501 → 2,584; outlook.md 1,046 → 1,059; both inside their ranges).

**business.md**

| # | Where | Edit | Reason |
|---|---|---|---|
| 1 | §1 history | "$1.4 billion of preferred stock sold to Bain Capital" → "…preferred stock (shares that earn a fixed dividend ahead of common shareholders) sold to Bain Capital" | jargon gloss at first use |
| 2 | §1 history | "up 22%" → "up 22.5%" | the tagged source (release Table 1, line 42) prints 22.5%; the 10-K's Item 7 rounds the same figure to 23%, so "22%" invited a false discrepancy |
| 3 | §1 history | tag "[8-K 2026-03-02, Ex.99.1; 10-K FY2026, Item 1]" → "[8-K 2026-03-02, Ex.99.1; DEF 14A 2025, CD&A; 10-K FY2023, Item 1]" | the FY2026 10-K text never says "II-VI" or "1971"; the 8-K press release gives 1971 (line 164), DEF 14A line 1331 names II-VI, 10-K FY2023 Item 1 (lines 210, 248) gives the materials business and Saxonburg, Pennsylvania |
| 4 | §1 | "grown on wafers of indium phosphide" → "grown on wafers (thin discs) of indium phosphide" | gloss |
| 5 | §2 prose | "not treated as discontinued operations" → "…(the accounting treatment that would have removed the sold units from both years' figures)" | gloss |
| 6 | §3 prose | "233 basis points" → "233 basis points (2.33 percentage points)" | gloss |
| 7 | §3 prose | after "yields that continue to exceed our 3-inch lines" added "(yield: the share of chips on a wafer that come out working)" | gloss |
| 8 | §3 prose | "$158 million inventory step-up" → "…step-up (acquired inventory marked up to market value and then expensed as it sold)" | gloss; matches 10-K-FY2024 line 1579 "amortization of the preliminary fair value step-up on acquired inventory" |
| 9 | §3 prose | "CHIPS Act" → "CHIPS Act (the US chip-factory subsidy law)" | gloss |
| 10 | §4 prose | "diluted shares jumped" → "diluted shares (the count including convertible securities) jumped" | gloss |
| 11 | §4 prose | "$64 million of impairments" → "$64 million of impairments (write-downs)" | gloss |
| 12 | §4 prose | debt sentence tag → adds "10-K FY2023, Item 8" | the $4.3B "three years earlier" comes from the FY2023 balance sheet (10-K-FY2023.txt lines 1748, 1755; total 4,309,798 at line 2286), which the tag omitted |
| 13 | §6 #1 | "a sequential drop" → "a quarter-on-quarter drop" | plain phrase instead of jargon |
| 14 | §6 #7 | "the auditor's critical audit matter" → "…(the judgement it singled out as hardest to audit)" | gloss |
| 15 | §7 intro | "from the proxy filed October 2, 2025" → "from the proxy (the annual shareholder-meeting filing that discloses pay and ownership) filed…" | gloss |
| 16 | §7 table | "six-month lock-up" → "six-month lock-up (no sales allowed)" | gloss; 10-K line 2311 |
| 17 | §7 table | "leverage covenant 4.25x" → "leverage covenant (lenders' cap on net debt relative to earnings) 4.25x" | gloss; 8-K-2025-09-26 line 68 "total net leverage ratio financial covenant… 4.25 to 1.00" |
| 18 | §8 row 3 | "18% opex model" → "18% operating-expense model" | plain phrase |
| 19 | Glossary | removed "EML / CW laser" and "DCI / ZR" | neither term appears in either file's prose; glossary is for unavoidable terms only (§3 rule 4) |

**outlook.md**

| # | Where | Edit | Reason |
|---|---|---|---|
| 20 | §2 | "our broad photonic technology portfolio, our manufacturing scale, and our significant US production footprint" → "the breadth of our photonic technology portfolio, our manufacturing scale, and our significant US production footprint" | the draft's wording blended transcript lines 30 and 40; the corrected text is line 40 verbatim |
| 21 | §2 | after "roughly flat on a pro forma basis" added "(as if the sold businesses were excluded from both periods)" | gloss |
| 22 | §3 | "Tell: sequential growth in Q1" → "Tell: sequential (quarter-on-quarter) growth in Q1" | gloss at first prose use; later uses are inside quotes |
| 23 | §4 | "The Company's financial guidance" → "The Company’s financial guidance" | verbatim quote; the release (line 117) uses the curly apostrophe |

**Withdrawn finding (kept per the §17 lesson):** D29′, "$700M revolver undrawn" in the §7 debt cell. I first read 10-K-FY2026.txt line 870 ("we have $664 million of undrawn capacity under our senior secured revolving credit facility") as contradicting "undrawn". Item 7 line 1399 then settled it: "As of June 30, 2026, the Company had no borrowings outstanding under the Revolving Credit Facility." The cell is correct as written; the $664M is availability after other utilisation, which the draft does not claim. No edit made.

---

## Cycle 2 (final; no third cycle runs)

_Re-reviewed 2026-09-09 from disk after the writer's second pass. outlook.md unchanged since the cycle-1 edits (all four cycle-1 edits still present; file timestamp earlier than business.md's). All nineteen cycle-1 glosses and tag fixes in business.md survived the rewrite (checked string by string). Word counts after this cycle: business.md 2,652 (writer reported 2,639; +13 from two reviewer wording fixes below), outlook.md 1,059. Both inside range._

**Verdict: PASS.** Nothing remains open for the owner.

| REVISE item | Result | Evidence |
|---|---|---|
| 1. §7 Luther age 61 → 60 | **PASS** | business.md line 154 now "Sherri Luther, 60, CFO"; DEF14A-2025.txt line 1113 "Sherri Luther \| 60 \| Chief Financial Officer and Treasurer". No stray "61" remains. |
| 2. §2 Materials margin basis | **PASS (arithmetic re-derived)**, one wording fix made directly | New text gives both bases. External: 391,502/1,349,758 = 29.0%; 296,874/1,016,573 = 29.2%; 354,714/953,843 = 37.2% ("Segment profit" rows 10-K-FY2025.txt lines 2346, 2326, 2307). Total sales: 391,502/(1,349,758+362,179) = 391,502/1,711,937 = 22.9%; 296,874/(1,016,573+457,623) = 296,874/1,474,196 = 20.1%; 354,714/(953,843+547,601) = 354,714/1,501,444 = 23.6% ("Inter-segment revenues" rows lines 2341, 2321, 2302: 362,179; 457,623; 547,601). "20%–24%" and "$362.2M, $457.6M and $547.6M" are right. **Direct fix:** the draft said the internal sales went "to Networking"; the FY2025 10-K names no buyer (Note 14 gives only each segment's intersegment total; Item 1 lines 179, 255, 2288 and Item 7 line 1013 do not link Materials' internal sales to Networking). Changed to "to the other segments" in the §2 prose and in the table footnote, with "the filing does not say which segment bought them" added to the footnote. |
| 3. §6 concentration label and note | **PASS** | Label now "Largest customer (per the FY2026 10-K wording; see note)". Note quotes 10-K-FY2026.txt line 2782 ("One major customer accounted for 20%, 10%, and 10% of consolidated revenue during fiscal 2026, 2025 and 2024") and 10-K-FY2025.txt line 2411 ("We had a different major customer who accounted for 10% of consolidated revenue during fiscal 2024") verbatim, states the disagreement, tags both notes, keeps "No customer is named." |
| 4a. §4 "Cash conversion" (rule 5) | **PASS**, one tag added directly | Paragraph is now meaning-only: three sentences, two figures (212 and 139 days), with the cash-bridge table carrying the dollars. 2,581,043/4,449,141 × 365 = 211.7 → 212; 1,437,636/3,766,793 × 365 = 139.3 → 139 (10-K-FY2026.txt Note 4 line 1960; COGS line 1639). The quote "a significant increase in inventory levels to support higher revenue growth" is Item 7 line 1373 verbatim. "Capex then swallowed many times what operations produced": 1,102.9 / 79.5 = 13.9×. **Direct fix:** "a year of record adjusted profit" rests on non-GAAP operating income $1,456.9M vs $1,036.9M (press-release.txt line 364), which the 10-K does not carry; added "Q4 FY2026 release, Table 6" to that sentence's tag. |
| 4b. §3 capital-intensity prose and new table | **PASS** | Prose now runs wafer cost lever → "Capital intensity is the price, and the table below shows how fast the bet grew" → payback and Q1 capex direction → outside money; no longer mostly numbers (the outside-money sentence keeps its five figures, the rest is words). New table "The capacity bet, $M", every cell verified: capex/depreciation 1.8x = 440,836/250,810 = 1.758 and 4.6x = 1,102,909/241,561 = 4.565 (10-K-FY2026.txt lines 1760, 1738); construction in progress 363,129 → 776,511 (Note 5 line 1969); capex in accounts payable 67,146 → 371,779 (line 1797); purchase commitments "about 1,092" with the Note 18 sentence quoted as printed ("$945 million in fiscal 2025 and $147 million thereafter", 10-K-FY2025.txt line 2525; Item 7 line 1308 gives the $1,092 million total) → 11,800 with "$3.4 billion in fiscal 2027 and $8.4 billion thereafter" (10-K-FY2026.txt line 2299; Item 7 line 1441 "approximately $11.8 billion"). Tags [10-K FY2026, Item 8], [10-K FY2026, Note 5], [10-K FY2025, Note 18; 10-K FY2026, Note 13] all use prefixes already in the Sources table (re-extracted: 10-K FY2023/FY2024/FY2025/FY2026, 10-Q Q3 FY2026, DEF 14A 2025, five 8-Ks, Investor Day 2025 deck, Q4 FY2026 release, Q4 FY2026 call; nothing new). The two glosses in the row labels ("plant not yet in service", "capex sitting in accounts payable") are plain. |

Rule 5 sweep of the whole file after the rewrite: no paragraph is now mostly numbers. The two remaining number-dense passages ("Why earnings per share were negative for three years" and "Return on capital") each carry an argument the numbers serve and were judged acceptable in cycle 1.

**Reviewer edits this cycle (both in business.md, logged above):** (24) §2 prose and footnote: "internal sales to Networking" → "internal sales to the other segments", footnote gains "the filing does not say which segment bought them" — the buyer is not stated in the FY2025 10-K. (25) §4 "Cash conversion": tag extended with "Q4 FY2026 release, Table 6" for "record adjusted profit".

**Final word counts:** business.md 2,652; outlook.md 1,059.
