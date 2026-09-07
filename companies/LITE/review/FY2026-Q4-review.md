# Lumentum Holdings Inc. (LITE) — Reviewer report, Q4 FY2026 (quarter ended June 27, 2026)

_Reviewed 2026-09-07 against `sources/FY2026-Q4/` only (as-of cutoff 2026-08-17). No other folder was opened. Files reviewed: `business.md` (2,865 prose words before fixes, 2,985 after), `outlook.md` (1,163 before and after). Word counts use the §3 rule 7 script (prose only; tables, headings, glossary, Sources and bracketed tags excluded)._

**Verdict: REVISE.** Citation spot-check: 119 items checked, 116 PASS, 2 FAIL, 1 UNVERIFIABLE. Every number in the §2, §3 and §4 tables, in the outlook §1 indicator table (bar one cell) and in the concentration and capital-allocation tables is right; every verbatim quote in outlook §4 and §5 matches the release, slides or transcript character-for-character; every "(computed)" figure re-derives exactly. What fails is one wrong cell in the outlook indicator table ("principal by series not summarized" — the 10-Q does give total principal), one incomplete tag (fixed directly), two inferences written as fact, three paragraphs that are mostly numbers (rule 5), two claims that need a sharper edge, and a length that my glosses pushed to 15 words under the ceiling.

---

## 1. Skeleton compliance

**business.md**

| Requirement (§6) | Result |
|---|---|
| `# <Company> — The Business` | OK |
| `_As of <QLABEL>. Written <date>._` with fiscal parenthetical on first use (§5) | OK: "Q4 FY2026 (quarter ended June 27, 2026)" |
| §1–§8 headings, in order, none skipped | OK. §1 has the history paragraph; §6 carries customer concentration (with a five-year table); §8 has name / why / where |
| §2 segment table, 5 fiscal years | OK (FY2022–FY2026). Two definition changes (OpComms/Lasers → Cloud & Networking/Industrial Tech → single segment with Components/Systems) footnoted per Lessons 2026-09-07 |
| §3 table: revenue, gross margin, operating margin, capex, capex/revenue, 5 years | OK, plus non-GAAP rows, R&D %, employees, and a Q4 FY2026 column |
| §4 table, 5 years | OK (net income, OCF, capex, FCF, SBC, tax on vested shares, amortization, depreciation, buybacks, dividends) |
| §8 marked `_Proposed — owner to review and lock._` | OK |
| Glossary, Sources | Both present. Sources table maps all ten tag prefixes used (10-K FY2026/FY2025/FY2024, 10-Q Q3 FY2026, DEF 14A 2025, both 8-Ks, call, release, slides) to cached files; confirmed by extracting every distinct tag prefix in the file |
| Length 2,000–3,000 | Inside the range: 2,865 before fixes, 2,985 after the reviewer's glosses. Upper half, not lower half as §3 rule 7 asks for first drafts; see REVISE 10 for padding candidates |

**outlook.md**

| Requirement (§7) | Result |
|---|---|
| `# <Company> — Outlook as of <QLABEL>` with fiscal parenthetical | OK |
| `_Transcript source tier: … Written <date>._` | OK: "third-party (The Motley Fool)", matches MANIFEST tier 3 |
| §1 table: one row per §8 indicator; columns this quarter / last quarter / what management said | OK: 8 rows for 8 indicators, in the same order; every cell tagged; a preamble explains that Q4 cash-flow values are FY-minus-nine-months differences |
| §2, §3, §4 (verbatim guidance), §5 | OK. §4 quotes the release and slides verbatim and states what was not guided |
| §6 Tone shift omitted on first run | OK, correctly omitted |
| Sources | OK; five tag prefixes used, all mapped; the call entry states tier 3, no page numbers, and the numbers-from-release rule |
| Length 800–1,200 | OK: 1,163 |

---

## 2. Citation spot-check

Legend: PASS / FAIL / UNVERIFIABLE. Line numbers refer to the cached `.txt` files in `sources/FY2026-Q4/`. Every "(computed)" figure was re-derived.

### 2a. business.md §2 revenue table (every cell) and §2 prose

| # | Cell(s) / sentence | Tag | Found at | Result |
|---|---|---|---|---|
| A1 | Cloud & Networking 1,008.7 / 1,322.5 / 1,084.9 | [10-K FY2024, Note 17] | 10-K-FY2024.txt line 3861 (Note 17 spans 3824–3976) | PASS |
| A2 | Cloud & Networking FY2025 1,410.8 | [10-K FY2025, Note 17; Note 18] | 10-K-FY2025.txt lines 1383, 3908 | PASS |
| A3 | Industrial Tech 703.9 / 444.5 / 274.3 / 234.2 | same | 10-K-FY2024 line 3862; 10-K-FY2025 line 3909 | PASS |
| A4 | Components 822.1 / 1,116.3 / 2,005.6 | [10-K FY2026, Note 18] | 10-K-FY2026.txt line 3939 (Note 18 begins 3928) | PASS |
| A5 | Systems 537.1 / 528.7 / 1,008.4 | same | line 3940 | PASS |
| A6 | Totals 1,712.6 / 1,767.0 / 1,359.2 / 1,645.0 / 3,014.0 | Items 8 | 10-K-FY2024 line 1843; 10-K-FY2026 line 1709 | PASS |
| A7 | Cloud & Networking segment profit 266.9 / 313.2 / 124.5 / 264.5 | Notes 17 | 10-K-FY2024 line 3865; 10-K-FY2025 line 1453 | PASS |
| A8 | Industrial Tech segment profit 373.5 / 152.7 / 25.1 / 12.1 | same | 10-K-FY2024 line 3866; 10-K-FY2025 line 1454 | PASS |
| A9 | Footnote: "OpComms" and "Lasers" through FY2023; segment profit excludes stock pay, acquisition amortization, restructuring, corporate overhead; one segment from Q1 FY2026 | [10-K FY2024, Note 17; 10-K FY2026, Note 17] | 10-K-FY2024 lines 189/3826 and 3867–3880 (reconciliation rows: SG&A, SBC, amortization, restructuring…); 10-K-FY2026 line 3845 | PASS |
| A10 | "higher market competition in the consumer end-market" | [10-K FY2025, Item 7] | 10-K-FY2025 line 1401 | PASS verbatim |
| A11 | "primarily driven by the ramp of laser chip and laser assembly product shipment, which represent 78% of the total growth"; "a slight increase in average selling prices" | [10-K FY2026, Item 7] | line 1343 | PASS verbatim |
| A12 | "cloud transceiver product lines which increased by more than 173%"; "the initial phase of optical circuit switch shipments, which contributed more than $90.0 million" | same | line 1345 | PASS verbatim |
| A13 | "Cloud versus telecom revenue, single product lines and named customers are not disclosed" | [10-K FY2026, Note 18] | line 2133 ("We do not present other levels of disaggregation, such as by customer, markets…") | PASS |

### 2b. business.md §3 economics table (every cell) and footnote

| # | Row | Tag | Found at | Result |
|---|---|---|---|---|
| B1 | Revenue row + Q4 1,006.3 | as A6; [release] | press-release.txt line 31 | PASS |
| B2 | Gross margin GAAP 46.0 / 32.2 / 18.5 / 28.0 / 41.7 / 47.4 | Items 7; release | 10-K-FY2024 line 1387; 10-K-FY2026 line 1299; release line 32 | PASS |
| B3 | Gross margin non-GAAP n/s / n/s / 30.2 / 34.7 / 46.0 / 50.4 | [DEF 14A 2025, CD&A]; [release] | DEF14A-2025.txt line 2236 ("Adjusted Gross Margin (1) 30.2% 34.7%"); release line 206 (34.7%, 46.0%), line 38 (50.4%) | PASS. The proxy's FY2025 figure equals the release's FY2025 column, so the two sources use the same method |
| B4 | R&D % 12.9 / 17.4 / 22.2 / 18.5 / 11.8 / 10.4 | footnote says FY2022–FY2023 and Q4 computed | 10-K-FY2024 line 1389 gives 12.9 / 17.4 / 22.2 directly; 10-K-FY2026 line 1301 (18.5, 11.8); Q4 = 104.4 / 1,006.3 = 10.37 (release line 114) | PASS (FY2022–FY2023 are disclosed, so the "computed" label is unnecessary but harmless; arithmetic 220.7/1,712.6 and 307.8/1,767.0 checks) |
| B5 | Operating margin GAAP 17.7 / (6.5) / (31.9) / (10.9) / 17.4 / 27.8 | Items 7; release | 10-K-FY2024 line 1393; 10-K-FY2026 line 1306; release line 33 | PASS |
| B6 | Operating margin non-GAAP n/s / n/s / (0.6) / 9.7 / 29.8 / 36.6 | [DEF 14A 2025, CD&A]; [release] | DEF14A line 2238; release lines 232, 39 | PASS |
| B7 | Capex 91.2 / 128.5 / 133.0 / 231.0 / 451.3 / 166.8 | Items 8; computed | 10-K-FY2024 line 1975; 10-K-FY2026 line 1851; Q4 = 451.3 − 284.5 (10-Q-FY2026-Q3.txt line 244) = 166.8; CFO "$167 million" transcript.txt line 47 | PASS |
| B8 | Capex / revenue 5.3 / 7.3 / 9.8 / 14.0 / 15.0 / 16.6 (computed) | — | recomputed 5.33 / 7.27 / 9.79 / 14.04 / 14.97 / 16.58 | PASS |
| B9 | Employees 7,257 / 10,562 / 13,757 | Items 1 | 10-K-FY2024 line 351; 10-K-FY2025 line 341; 10-K-FY2026 line 302 | PASS. "n/d" for FY2022–FY2023 means "not in this report's sources", not "not disclosed"; footnote reworded directly |
| B10 | Footnote: FY2024 non-GAAP "recast to the FY2025 method" | [DEF 14A 2025, CD&A] | DEF14A footnote (1) after line 2238: "Fiscal year 2024 non-GAAP financial measures in this table have been recast to conform to this refined methodology" | PASS |

### 2c. business.md §4 cash table (every cell) and Q4 footnote

| # | Row | Tag | Found at | Result |
|---|---|---|---|---|
| C1 | GAAP net income 198.9 / (131.6) / (546.5) / 25.9 / (6,935.1) | Items 8 | 10-K-FY2024 line 1953; 10-K-FY2026 line 1824 | PASS |
| C2 | Operating cash flow 459.3 / 179.8 / 24.7 / 126.3 / 751.4 | same | 10-K-FY2024 line 1973; 10-K-FY2026 line 1849 | PASS |
| C3 | Capex | as B7 | | PASS |
| C4 | Free cash flow (computed) 368.1 / 51.3 / (108.3) / (104.7) / 300.1 | — | all exact | PASS |
| C5 | Stock-based compensation 103.1 / 148.4 / 128.8 / 177.2 / 170.2 | same | 10-K-FY2024 line 1956; 10-K-FY2026 line 1827 | PASS |
| C6 | Cash paid for taxes on vested shares 39.0 / 37.2 / 24.0 / 41.7 / 281.0 | same | 10-K-FY2024 "Payment of withholding taxes related to net share settlement of restricted stock units" (cash-flow financing section); 10-K-FY2026 line 1880 | PASS |
| C7 | Amortization and write-off of acquired intangibles 85.5 / 149.0 / 179.7 / 152.4 / 138.2 | same | 10-K-FY2024 line 1958; 10-K-FY2026 line 1830 | PASS (row label matches the cash-flow caption exactly) |
| C8 | Depreciation 81.6 / 106.6 / 110.6 / 104.3 / 128.8 | same | 10-K-FY2024 line 1955; 10-K-FY2026 line 1826 | PASS |
| C9 | Buybacks 543.9 / 175.6 / — / — / — | same | 10-K-FY2024 line 1988; no repurchase line in the FY2026 statement (lines 1868–1883) | PASS |
| C10 | Dividends — (all years) | [10-K FY2026, Item 5] | line 1092 | PASS |
| C11 | Q4 alone (computed): OCF 363.0, capex 166.8, FCF 196.2 | [10-K Item 8; 10-Q Item 1] | 751.4 − 388.4 (10-Q line 242) = 363.0; 451.3 − 284.5 = 166.8; 363.0 − 166.8 = 196.2 | PASS |

### 2d. outlook.md §1 indicator table (every number)

| # | Cell | Tag | Found at | Result |
|---|---|---|---|---|
| D1 | Row 1: $649.4M (64.5%) / $356.9M (35.5%); Q3 $533.3M (66.0%) / $275.1M (34.0%); "Q4 revenue landed at the high end of the guided range" | [release]; [slides, p.3] | release lines 46–47 (Q4 values and Q4 %; the release gives no Q3 percentages); slides.txt lines 73, 76 (66.0% / 34.0%); slides line 49 | **FAIL (tag only), fixed directly:** the Q3 percentages come from slides p.4, not the release; tag now "[Q4 FY2026 release; Q4 FY2026 slides, p.4]". Values right (533.3/808.4 = 65.97%) |
| D2 | Row 2: 50.4% (47.4%); 47.9% (44.2%); "originally targeted ... at a $2 billion quarterly run rate" | [release]; [call] | release lines 32, 38; transcript line 28 | PASS |
| D3 | Row 3: 36.6%; 32.2%; "above high end of guided ranges" | [release]; [slides, p.3] | release lines 33, 39; slides line 51 | PASS |
| D4 | Row 4: FY2026 26.6% and 15.0%, receivables 30.4%; Q3 26% and 12%, receivables 25% | [10-K Item 1; Note 17]; [10-Q Note 15] | 10-K-FY2026 lines 249–250 and 3894–3895, 3900 ("Customer 1 30.4%"); 10-Q lines 1670, 1684 (Note 15 spans 1621–1700) | PASS |
| D5 | Row 5: $166.8M computed; "$167 million"; $1,159.1M; 9M $284.5M; $964.3M; "helped offset our planned capital expenditures" | as tagged | see B7; release line 153; 10-Q line 244; 10-Q line 172 and slides line 117; transcript line 34 | PASS. "Q3 alone not derivable from cached sources" is correct: the Q2 10-Q is not in the folder |
| D6 | Row 6: 363.0 − 166.8 = 196.2; FY $300.1M; 9M 388.4 − 284.5 = 103.9 | computed | all exact | PASS |
| D7 | Row 7: $2,354.4M; $691.6M; $1,795.6M; $632.8M; "$59 million sequentially to support the expected growth" | [10-K Item 7; release]; [10-Q Item 2; Item 1]; [call] | 10-K-FY2026 line 1539 (Item 7 contractual-obligations table); release line 150; 10-Q lines 2084, 169; transcript line 47 (and 691.6 − 632.8 = 58.8 confirms) | PASS |
| D8 | Row 8, Q4 cell: 88.6M + 2.9M preferred; 89.7M at Aug 14; principal $1,554.3M; book value $1,544.6M | [10-K Item 8; cover; Note 10] | lines 1802, 1953, 80, 3086, 3088 | PASS |
| D8' | Row 8, Q3 cell: "book value $3,183.4M **(principal by series not summarized)**" | [10-Q Note 9] | book value 3,183.4 at 10-Q line 990 is right; but 10-Q line 2087 (Item 2 contractual-obligations table) states "Convertible notes - principal | 3,198.4" as of March 28, 2026 | **FAIL:** total principal is disclosed; the cell says it is not. Replace with "principal $3,198.4M [10-Q Q3 FY2026, Item 2]" (REVISE 1) |
| D8'' | Row 8, guidance cell: ~102.0M diluted shares; $757.8M conversion requests by Aug 14 | [slides, p.7]; [10-K Note 10] | slides line 145; 10-K line 2907 | PASS |
| D9 | Line 19 year-ago: Components $320.4M, Systems $160.3M; 37.8%; 15.0% | [release] | release lines 46–47, 38–39 | PASS |
| D10 | Line 6: FY2027 is a 53-week year ending July 3, 2027, extra week in Q3 | [10-K Note 1] | line 1997 | PASS |
| D11 | Line 6: "Q1 FY2027 ends in late September 2026" | untagged | derivable from Note 1 (Saturday closest to June 30, 13-week Q1) | PASS (derivation) |

### 2e. outlook.md §4 guidance quotes (character-for-character)

| # | Quote | Tag | Found at | Result |
|---|---|---|---|---|
| E1 | "Net revenue in the range of $1.225 billion to $1.275 billion" | [release] | line 81 | PASS |
| E2 | "Non-GAAP operating margin of 39.5% - 40.5%" | [release] | line 82 | PASS |
| E3 | "Non-GAAP diluted net income per share of $4.05 to $4.35" | [release] | line 83 | PASS |
| E4 | "Diluted Shares – M ... 102.0"; "Guidance assumes effective tax rate of 16.5%" | [slides, p.7] | slides lines 145, 149 | PASS (ellipsis spans the table columns) |
| E5 | "approximately half of the sequential growth will stem for our components portfolio ... The other half will be powered by the ongoing ramp of our systems portfolio" | [call] | transcript line 41 | PASS (garble "for" preserved and flagged) |
| E6 | "We expect gross margin expansion to continue driven by product mix and tight operational execution" | [call] | line 28 | PASS |
| E7 | "cannot be provided without unreasonable effort" | [release] | line 84 | PASS |
| E8 | "on track to deliver meaningful revenue exiting CY 2026" | [slides, p.3] | slides line 57 | PASS |
| E9 | "we'll come out with some new financial targets, probably at the next OFC" | [call] | line 61 | PASS |

### 2f. outlook.md §5 claim quotes (character-for-character)

| Claim | Quote | Found at | Result |
|---|---|---|---|
| 1 | "Net revenue in the range of $1.225 billion to $1.275 billion" | release line 81 | PASS |
| 2 | "Non-GAAP operating margin of 39.5% - 40.5%" | release line 82 | PASS |
| 3 | "We expect gross margin expansion to continue" | transcript line 28 | PASS |
| 4 | "approximately half of the sequential growth will stem for our components portfolio" | line 41 | PASS |
| 5 | "our guidance includes our first triple-digit OCS revenue quarter" | line 39 | PASS |
| 6 | "over 50% EML unit growth by December 2026 quarter compared to the year ago quarter" | line 36 | PASS |
| 7 | "somewhere in the $50 million range by the end of the calendar year" | line 101 | PASS |
| 8 | "we're definitely tracking to the $400 million. I would not say tracking ahead." | line 116 | PASS |
| 9 | "some things to talk about over the next couple of quarters relative to new arrangements in Greensboro" | line 186 | PASS |
| 10 | "new financial targets, probably at the next OFC"; "probably moving up 100 to 200 basis points versus what we showed at OFC" | lines 61, 169 | PASS |
| 11 | "two customers individually accounted for 26% and 12% of our total revenue" | 10-Q line 1670 | PASS |

### 2g. outlook.md §2–§3 quotes and facts

| # | Item | Tag | Found at | Result |
|---|---|---|---|---|
| F1 | "As AI compute workloads increase in both speed and bandwidth, data center architects are turning to optical links as a primary means of connectivity" | [release] | line 14 | PASS (the transcript's version says "increased"; the writer correctly tagged the release) |
| F2 | "prove 2 things: Our differentiated technology commands premium value and our operating model delivers outsized leverage"; "a premier laser chip manufacturer" | [call] | lines 29, 31 | PASS |
| F3 | "our $1.25 billion target more than 1 quarter ahead of schedule"; release confirms $1.25 billion | [call; release] | transcript line 29; release line 15 | PASS |
| F4 | "38% to 42%"; "probably moving up 100 to 200 basis points"; labelled transcript figures | [call] | line 169 | PASS |
| F5 | demand "is outpacing our current supply" | [10-K Item 1] | line 165 (also Item 7 line 1142) | PASS |
| F6 | ">25% of total EML revenue"; "80% YoY"; "multiple long-term supply agreements now in place"; ">130% YoY"; "initial shipments of 1.6T transceivers, with a portion utilizing internal CW lasers"; "multi-year, multi-billion-dollar purchase agreement" | [slides, p.3] | slides lines 55, 59, 58, 63, 64 | PASS, all verbatim |
| F7 | "over 50% EML unit growth …"; "50% or more of volume by midyear of 2027"; "shipping behind customer demand" | [call] | lines 36, 162, 124 | PASS |
| F8 | "quite a bit better ... than we expected"; "a significant price premium" | [call] | lines 147, 148 | PASS |
| F9 | "very much further behind relative to our ability to supply"; "by the second half of calendar 2027"; "not quite as good as the lasers" | [call] | lines 124, 30, 137 | PASS |
| F10 | "the $50 million range by the end of the calendar year"; triple-digit quarter in fiscal Q3; labelled | [call] | lines 100–101 | PASS |
| F11 | "a fourfold increase in our pump laser shipments over the next several quarters" | [call] | line 34 | PASS |
| F12 | "1.6T transceiver uptake to intensify starting in fiscal Q1 and sustain through calendar 2027" | [call] | line 38 | PASS |
| F13 | "more than $90.0 million"; shipments doubled Q3 to Q4; "includes our first triple-digit OCS revenue quarter" | [10-K Item 7; call] | 10-K line 1345; transcript line 39 | PASS |
| F14 | "tracking to the $400 million" for 2H CY2026, "(analyst's framing; transcript figure)" | [call] | analyst line 113 ("the $400 million plus OCS guide for the second half of 2026"), CEO line 116 | PASS; see §7 item 3 |
| F15 | Two Japan fabs expanding; Greensboro converting to indium phosphide; "first revenue ... early 2028"; AXT substrate deal | [call] | lines 36, 107, 175/179 | PASS |

### 2h. business.md prose sentences (§1, §3–§7)

| # | Sentence / claim | Tag | Found at | Result |
|---|---|---|---|---|
| G0 | §1: a transceiver "converts electrical signals into laser light and back"; an OCS "redirect[s] light between fibers so a data center can be rewired without converting the light to electricity" | [10-K FY2026, Item 1] | Item 1 names both products (lines 139, 221) but nowhere describes them this way; no "electrical" description anywhere in the 10-K | **UNVERIFIABLE** (writer's plain-English definitions under a filing tag; harmless but the tag over-claims; REVISE 9) |
| G1 | §1: "cloud and network service providers, AI infrastructure providers, and network equipment manufacturers" | [10-K Item 1] | line 185 | PASS verbatim |
| G2 | §1: fabs in "United States, Thailand, China, the United Kingdom, Slovenia and Japan"; contract manufacturers "Thailand, Taiwan, Malaysia and the Philippines" | [10-K Item 1] | lines 290, 294 | PASS |
| G3 | §1: laser chips on indium phosphide in two Japan fabs; "a premier laser chip manufacturer" | [call] | transcript lines 36, 31 | PASS (transcript-only wording; no number; see §7 item 4) |
| G4 | §1 history: spin-off August 2015; Oclaro 2018, NeoPhotonics/IPG 2022, Cloud Light 2023; "advanced optical modules for data center applications" | [10-K Item 1; 10-K FY2024, Note 4] | 10-K-FY2026 lines 149, 151; 10-K-FY2024 line 2439 (Note 4) | PASS verbatim |
| G5 | §1: Huawei "historically our largest networking customer in China"; shipments ended "in early 2024" | [10-K Item 1A] | line 494 ("in the beginning of calendar year 2024") | PASS |
| G6 | §1: CEO change February 2025; revenue +83% to $3.0B; "This demand is outpacing our current supply which has required us to make decisions on supply allocation" | [DEF 14A CD&A]; [10-K Item 1; Item 7] | DEF14A line 2768; 10-K lines 1327 (83.2%), 165, 1142 | PASS verbatim |
| G7 | §2: "under purchase orders or under contracts that do not contain volume or long-term purchase commitments"; Components = laser chips, sub-assemblies, line subsystems; Systems = modules, OCS, industrial lasers | [10-K Item 1A; Item 1] | lines 568, 137, 139 | PASS |
| G8 | §3: "Approximately 54% of the gross margin dollar increase was driven by lower manufacturing costs as a percentage of revenue, primarily due to higher internal factory utilization"; 29% "a mix shift to higher margin products"; 17% amortization; FY2024 revenue −23%; "lower revenue" cost 12.9 points | [10-K FY2026 Item 7; 10-K FY2024 Item 7] | 10-K-FY2026 line 1386; 10-K-FY2024 lines 1422 (23.1%), 1470 | PASS verbatim |
| G9 | §3: "our operating model delivers outsized leverage"; gap 3.0 / 8.8 points (computed) | [call]; [release] | transcript line 29; 50.4 − 47.4, 36.6 − 27.8 | PASS |
| G10 | §3: R&D $356.5M (11.8%), SG&A $363.2M; 87% of employees in manufacturing | [10-K Item 7; Item 1] | lines 1330–1332; 11,916 / 13,757 = 86.6% (line 302) | PASS |
| G11 | §3: capex 3.5× depreciation; $181.4M vs $43.4M unpaid equipment; purchase obligations $837.6M → $2.4B; "we have secured multiple long-term customer agreements that helped offset our planned capital expenditures"; Thailand $218.6M → $450.6M, Japan $144.3M → $232.1M | [10-K Item 8; 10-K FY2025 Note 16; 10-K FY2026 Note 16; call; Note 17] | 451.3/128.8 = 3.50; line 1891; 10-K-FY2025 line 3660, 10-K-FY2026 line 3787; transcript line 34; lines 3916–3917 | PASS |
| G12 | §4: conversion prices $69.54–$187.77; $390.77 on Dec 26, 2025; 10.6M shares for $1,124.9M principal; loss $7,756.6M; APIC +$8,876.9M; "a one-time non-cash GAAP charge"; shares 69.8M → 88.6M + 2.9M preferred; 31% (computed); pre-tax ex-loss ≈ $584M (computed) | [Note 10; cover; Item 7; Item 8; call; Note 14] | lines 2875–2878 (187.77, 69.54, 131.03, 99.29), 78, 1424, 2915, 1933, 1802, 1953; transcript line 45; 91.5/69.8 − 1 = 31.1%; −7,172.8 + 7,756.6 = 583.8 | PASS |
| G13 | §4: non-GAAP operating profit $897.0M; receivables +$270.4M, inventory +$228.4M, payables +$221.6M; $281.0M tax on vested shares; five-year OCF $1,541.5M, capex $1,035.0M, acquisitions $1,600.5M; NVIDIA $2.0B | [release; Item 7; Item 8; 10-K FY2024 Item 8; Note 14] | release line 231; 10-K line 1607; line 1880; sums exact; 861.6 + 700.9 + 38.0 (10-K-FY2024 line 1976; 10-K-FY2026 line 1852); line 3435 | PASS |
| G14 | §4: operating capital ≈ $1.8B (1,159.1 + 691.6 + 520.3 − 567.4 = 1,803.6); goodwill + intangibles $1,396.2M (1,069.3 + 326.9); ≈28% (897.0 / 3,199.8 = 28.0%) | [release] | release lines 153, 150, 149, 162, 155–156 | PASS |
| G15 | §5: "We have a distinctive ability to deliver at scale to a very tight set of specifications, which enables superior yields in transceiver manufacturing"; "we are able to command a nice price premium"; "behind customer demand"; "effectively sold out for the foreseeable future"; "very much further behind"; "commoditization" / "predominantly Asia-based competitors" | [call]; [10-K Item 1A] | transcript lines 35, 91, 124, 33, 124; 10-K line 564 | PASS verbatim |
| G16 | §5: "first to market in many instances ahead of larger competitors, giving us a market share advantage that we should be able to maintain through the cycle"; "somewhere between 70%, 80% share"; "3-year arrangements"; "have pricing built into them"; "in most instances, I think they're take-or-pay"; colleague did not confirm | [call] | lines 39, 219; Wupen Yuen "No, thank you." line 223 | PASS |
| G17 | §5: "we're really the only merchant supplier today of OCS"; "they'll continue to use an internal version"; "#1 supplier" in "early '27" | [call; slides p.3] | lines 206, 117 | PASS |
| G18 | §5: "our competitors may seek to vertically integrate by buying suppliers that also supply products or components to us"; "may also determine to develop and produce products for their own use" | [10-K Item 1A] | line 576 | PASS verbatim |
| G19 | §5: Note 14 discloses no commercial agreement with NVIDIA | [Note 14] | lines 3435–3447 list only the preferred-stock terms | PASS |
| G20 | §6#1: 26.6% / 15.0% / 30.4%; nine-month 24%; ≈32% of Q4 (computed, approximate); "may alter their purchasing behavior with little or no notice" | [10-K Item 1; Note 17; 10-Q Note 15; Item 1A] | lines 249–250, 3900; 10-Q line 1670; re-derivation in §7 item 5; line 568 | PASS |
| G21 | §6 concentration table, every cell (18.9 / 15.4 / 26.6; 12.6 / 15.3 / 11.4 / 16.0 / 15.0; 28.7 / 12.1; 10.5) | [10-K FY2024/FY2025/FY2026, Note 17] | 10-K-FY2024 lines 3944–3947 (Customers A–D); 10-K-FY2025 lines 329–332; 10-K-FY2026 lines 3894–3895 | PASS; chaining by identical percentages is labelled as the gatherer's inference |
| G22 | §6#2: "brought down inventories as supply chain constraints eased"; (31.9)%; "$59 million sequentially" | [10-K Item 7; call] | lines 165/1142, 1306; transcript line 47 (691.6 − 632.8 = 58.8 confirms) | PASS |
| G23 | §6#3: "We obviously haven't seen any impact on our numbers as yet"; "some of these Chinese laser suppliers are not delivering in the market today"; "may cause those customers to seek domestic alternatives to our products, including developing alternatives internally" | [call; 10-K Item 1A] | transcript lines 90, 91; 10-K line 600 | PASS |
| G24 | §6#4: "we may never recover this demand"; subpoenas from BIS and DOJ over Huawei; "We are unable to predict the likely outcome of these matters"; "indium, gallium, germanium"; "China and Thailand" | [10-K Item 1A; Note 16] | lines 498, 496 ("administrative subpoena from BIS … related subpoena from the U.S. Department of Justice … regarding our business with Huawei"), 3823, 598, 372 | PASS |
| G25 | §6#5: Thailand 1.17M sq ft; 39% of net plant; "For some of the components and finished good products, we are the sole manufacturer"; "would be costly and require a long period of time"; Greensboro bought March 2026; "first revenue" in "early 2028" | [10-K Item 2; Note 17; Item 1A; call] | line 1072 (1,173,000); 450.6/1,159.1 = 38.9%; line 660; lines 1074/2402; transcript line 107 | PASS |
| G26 | §6#6: "continues to be viewed as the natural end state"; "$50 million range by the end of the calendar year" (labelled) | [call] | lines 32, 101 | PASS |
| G27 | §6#7: principal settled in cash, excess in shares; $757.8M called by Aug 14; all notes current because convertible at will; 69.8M → 89.7M; 2032 notes $1,265.0M at $187.77 | [Note 10; cover] | lines 2870, 2907, 1802, 80, 2933, 2875 | PASS |
| G28 | §7: Hurlston 58, CEO Feb 7 2025, Synaptics 2019–2025, Finisar 2018–2019; Ali 52, joined Feb 2019, ex-Synaptics CFO; Herscher independent chair since spin-off | [DEF 14A Executive Officers; Director Nominees] | DEF14A lines 2081, 2768, 1145–1147, 2082, 2088–2092, 247, 665, 1113 | PASS |
| G29 | §7: Lowe $3.2M severance and ≈$30M accelerated/modified awards (computed) | [DEF 14A CD&A] | line 3391: $3,200,000 cash; $8,952,478 accelerated + $21,387,742 modification incremental fair value = $30,340,220 | PASS |
| G30 | §7: Retort with the company since 2008; retires Oct 2026, two-year consulting | [DEF 14A; 8-K 2026-07-30] | DEF14A line 2118 (joined JDSU, the predecessor, 2008); 8-K lines 57–59 | PASS |
| G31 | §7: on-target pay $12.1M; $14.0M PSUs vs S&P 500 IT index over 4 years; bonus 60% adjusted operating income / 40% revenue; half PSUs; two-thirds FY2027 revenue; FY2023–25 PSUs 24% "because revenue missed" | [DEF 14A CD&A] | lines 2322, 3021, 2734–2735, 2694, 2955 (67%), 312 and 3075 ("Total Revenue: 0% Payout 70% weight … Total Payout: 24%") | PASS |
| G32 | §7: Vanguard 10.2%, FMR 9.8%, BlackRock 8.8%; directors and officers <1% | [DEF 14A Security Ownership] | lines 3948–3950, 3968–3970 | PASS |
| G33 | §7 table: $1.2B buyback expired May 2025, $569.6M unused, no new authorization; dividends quote; NeoPhotonics $934.4M, IPG $55.9M, Cloud Light $728.5M, Sagamihara $42.2M, Greensboro $38.0M; 2032 notes; principal $2,514.7M → $1,554.3M; NVIDIA 2.9M at $695.31; 68.0M shares Jul 2022; cash $2,738.4M; $400M undrawn | as tagged | 10-K-FY2025 lines 1173, 1168–1171; 10-K-FY2026 Item 5 has no buyback text (grep = 0); line 1092; 10-K-FY2024 lines 2522, 2547, 1803; 10-K-FY2026 lines 2661, 2402, 2933, 2895, 3435; 10-K-FY2024 line 2042; release 2,043.5 + 694.9; lines 3153, 3163 | PASS, every row |
| G34 | §7: "The Company will not receive any cash proceeds" | [8-K 2026-06-01] | line 65 | PASS verbatim |
| G35 | §8 indicator table: $649.4M / $356.9M; 50.4% / 47.4%; 36.6%, 39.5%–40.5%; 26.6% / 15.0% / 30.4%; $451.3M / $1,159.1M; $300.1M; $2,354.4M / $691.6M; 89.7M / $1,554.3M | as tagged | all verified above | PASS |

**Totals: 119 checked; 116 PASS; 2 FAIL (D1 tag, fixed directly; D8' wrong cell, REVISE 1); 1 UNVERIFIABLE (G0 definitional clauses under a filing tag).**

---

## 3. Invented-number and inference check

No invented numbers. Every figure traces to a cached source or a labelled computation; the transcript-only figures ($2 billion run rate, $50 million, $400 million, 38%–42% and 100–200 basis points, "$167 million", "$59 million") are each labelled "transcript figure" or independently confirmed by the release, 10-K or 10-Q. Non-GAAP figures appear only for periods the release covers (Q4 FY2026, Q3 FY2026, Q4 FY2025, FY2026, FY2025) plus FY2024 from the proxy, which the footnote says. Items that need a label or a fix:

1. **outlook.md §1 row 8 (line 17):** "principal by series not summarized" — wrong; the 10-Q's Item 2 contractual-obligations table gives total convertible-note principal of $3,198.4M at March 28, 2026 (line 2087). Factual → REVISE 1.
2. **business.md §6#2 (line 108):** "Revenue is now mostly cloud and AI; the share is not disclosed." "Mostly" is an inference. The 10-K says demand growth comes from "AI and cloud customers" (line 165) and gives no cloud share; the nearest disclosed proxy is Cloud & Networking at 85.8% of FY2025 revenue (10-K-FY2025 line 3908), which also contains telecom. Label as inference or anchor to that figure → REVISE 4.
3. **business.md §3 (line 36):** "Materials rise with every unit, factories do not, and factories are the bigger piece." The last clause is the writer's inference; the 10-K supports it only indirectly (54% of the gross-margin increase came from utilization). Label → REVISE 5.
4. **business.md §6#1 (line 97):** the ≈32% Q4 share assumes the 10-K's "Customer A" is the 10-Q's 24% customer; each filing letters customers afresh. The label "(computed, approximate)" is right; add the assumption → REVISE 6.
5. **business.md §1 (line 6):** transceiver and OCS descriptions carry a 10-K tag the 10-K does not support (G0). Definitions, not facts about the company; move or untag → REVISE 9.
6. **business.md §3 table footnote:** FY2022–FY2023 R&D % labelled "computed" although the FY2024 10-K states them directly (line 1389). Harmless; arithmetic matches.
7. Labelled inferences that are fine as written: the customer-chaining inference in the §6 table note; "our inference is that it traded shares now for the cash the principal would otherwise have cost" (§7); "the FY2024 column shows what the same assets earn when demand turns" (§4, framed as observation of the table); "whether the 28.7% customer of FY2022 was Huawei is not disclosed" (§6, restrained). The report names no customer other than NVIDIA (a disclosed investor) and Huawei (disclosed in the 10-K), which is correct.

---

## 4. Jargon and readability audit

Read as a smart 16-year-old with no finance or optics background.

**(a) Terms used without being plain, name-inferable or in the glossary** (before reviewer fixes; *fixed* = glossed directly, see "Fixed directly"):

| Term | Where | Status |
|---|---|---|
| operating margin | business.md §3 table (line 44) then prose lines 52, 54 | *fixed* at first prose use (line 52); gross margin was already defined at line 36 |
| depreciation | §3 line 56 ("3.5 times depreciation"); §4 table row | *fixed* at line 56 |
| preferred shares | §4 line 75; §7 table "NVIDIA preferred" | *fixed* at line 75 |
| dilution | §4 line 75 | *fixed* ("each existing share now owns a smaller slice") |
| commoditization | §5 line 83 (inside a quote) | *fixed* with a gloss after the quote |
| receivables | §6#1 line 97 (and §8 indicator 4) | *fixed* at line 97; indicator list left for the owner (see REVISE 11) |
| sequentially | §6#2 line 108 (quote, before outlook §4 defines it) | *fixed* ("meaning versus the prior quarter") |
| principal | §6#7 line 118 | *fixed* ("the amount borrowed") |
| on-target pay; performance units | §7 line 122 | *fixed* |
| book value | outlook §1 row 8 | *fixed* ("the balance-sheet amount") |
| "silicon photonics" | glossary CW entry | *fixed* (one-clause gloss) |
| leverage (banned word outside quotes) | §3 line 52 "so the leverage arrived" | *fixed* → "margin lift"; the other three uses (lines 36, 145; outlook line 23) are inside management quotes |
| "guided range", "utilization-and-pricing lever" | §8 indicators 2–3; outlook §1 rows 1–3 | not fixed (indicator list is the owner's to lock); reword at lock (REVISE 11) |
| GAAP / non-GAAP | §3 table rows before the explanation at line 52 | table comes first, explanation after (same finding as the pilot); *fixed* with a one-line pointer before the table; the glossary also carries GAAP / non-GAAP |
| transceiver, wafer fab, hyperscaler, indium phosphide, segment profit, purchase obligations, paid-in capital, conversion price, goodwill and intangibles, merchant supplier, take-or-pay, substrates, run rate, OFC, YoY, basis points, PP&E | various | already glossed inline at first use; good |
| EML, CW laser, OCS, CPO/NPO, ELS, pump laser, 800G/1.6T/200G lane, convertible note, capex | text | in the glossary; each is used in the body |
| tier 1, SerDes, DCI, scale-out/scale-up/scale-across, SiPho, NEMs, ASP, EBITDA, TAM, in-tray | — | not used outside quotes (scale-out/scale-across appear only inside slide quotes in outlook §3 and are not load-bearing). Good restraint |

**(b) Glossary.** Twelve entries; all twelve terms appear in the body; each is one sentence (the CPO / NPO entry was two sentences and was merged directly). Nothing non-essential is in it. "Indium phosphide" is a reasonable inclusion because §1, §6#5 and outlook §3 all turn on it.

**(c) Sentences that assume prior knowledge.** After fixes, none stops the reader. Two residual soft spots for the writer: §4 line 75 "negotiated early conversions" versus the 10-K's "privately negotiated exchange arrangements" (the two mechanisms differ; see REVISE 3); §5 heading "Qualification and long-term agreements" — "qualification" is explained by the next sentence only implicitly.

**(d) Banned-word sweep** (leverage, synergy, headwind, tailwind, monetize, ecosystem, at scale, robust, unlock, TAM, accretive): one prose hit ("the leverage arrived", fixed); all other hits are inside management quotes.

**(e) Paragraphs that are mostly numbers (rule 5):** business.md line 75 (§4 debt explanation: 12 figures), line 77 (§4 cash conversion: 11 figures), line 122 (§7 people and pay: about 20 figures in 9 sentences). These want small tables → REVISE 2–3. Tables that have become walls: outlook §1 rows 5 and 8 hold three or four numbers plus a tag each; readable but dense; the pilot's "one comparison per cell" note applies.

---

## 5. Claims quality (outlook.md §5) and indicator anchoring (§8)

Count: 11 (within 6–12). Headline guidance is 2 of 11 (claims 1–2); claims 3–4 are margin/mix structure; 5–10 are product, capacity and target-model milestones; 11 is a labelled disclosure check. Good balance.

| # | One sentence, one thing? | Metric / date / event | Single direction, can fail? | Quote supports? | Labelled where needed? | Notes |
|---|---|---|---|---|---|---|
| 1 | Yes | Q1 revenue in $1.225–1.275B | Yes | Yes | n/a | |
| 2 | Yes | Q1 non-GAAP OM 39.5–40.5% | Yes | Yes | n/a | |
| 3 | Yes | Q1 non-GAAP GM > 50.4% | Yes | Yes | "our sharpening … not management's number" ✓ | |
| 4 | Yes | each product type 40–60% of the sequential increase | Yes | Yes | sharpening labelled ✓ | Checkable from the release table |
| 5 | Yes | management states Q1 OCS ≥ $100M | Yes; silence = Dropped | Yes | n/a | |
| 6 | Yes | EML units +>50% Dec-26 vs Dec-25, by Q2 call | Yes | Yes | n/a | Horizon two quarters (⏳ next quarter) |
| 7 | Yes | UHP laser revenue "about $50 million" in the Dec-26 quarter | Soft edge: "about" is a judgment | Yes | "transcript figure" ✓ | Sharpen to "$50 million or more" (CEO: "the $50 million mark") → REVISE 7 |
| 8 | Yes | OCS ≥ $400M for Q1+Q2 FY2027 | Yes | Yes | "transcript figure" ✓; period attributed to analyst, number not | Say both number and period were the analyst's framing that the CEO endorsed → REVISE 8; see §7 item 3 |
| 9 | Yes | new Greensboro customer arrangement by Q2 call | Yes | Yes | n/a | |
| 10 | Yes (one test: the new model's OM floor) | new target model with OM range ≥ 39%–43% after OFC | Yes | Yes | "transcript figures" ✓ | Horizon two quarters |
| 11 | Yes | 10-Q quarter column: largest customer ≥ 25% | Yes | Yes | "(Disclosure check, not a management claim.)" and "quarter column (not year-to-date)" ✓ | Exactly as §9 asks |

No either/or constructions; no double-barreled claim with an unobservable half; every sharpening is labelled.

**§8 indicators (anchoring, §8 of AGENTS.md).** All eight anchor to disclosures that recur every quarter: (1) release "Net Revenue by Product Type" table (release line 43) and 10-Q/10-K revenue note; (2) release GAAP-to-non-GAAP reconciliation; (3) release "Business Outlook" (line 79) and slides guidance page; (4) 10-Q/10-K concentration note (present in Q3 10-Q Note 15 and 10-K Note 17); (5) cash-flow and balance-sheet lines; (6) cash-flow lines; (7) 10-Q Item 2 contractual-obligations table (line 2084) and balance sheet; (8) cover page and debt note. None depends on a one-off call target; the one-off targets ($400M OCS, $50M UHP lasers, fourfold pumps, 50% EML units, 38–42% model) are correctly tracked as claims instead. Outlook §1 has one row per indicator with this-quarter / last-quarter / what-management-said cells, all tagged.

---

## 6. As-of check

Every source is dated on or before 2026-08-17 (10-K filed 2026-08-17; release, slides and call 2026-08-11; 10-Q 2026-05-06; proxy 2025-10-07; 8-Ks 2026-06-01 and 2026-07-30). The Motley Fool transcript page is dated 2026-08-18, one day after the cutoff, for the 2026-08-11 call; MANIFEST.md documents this and that only call content was used; acceptable. No statement in either file relies on later information: Retort's October 2026 retirement comes from the 2026-07-30 8-K; the FY2027 calendar (53 weeks, July 3, 2027) from 10-K Note 1; the post-cutoff conference appearances listed in MANIFEST were not used. "Written 2026-09-07" is the drafting date, as the skeleton requires. PASS.

---

## 7. Rulings on the writer-flagged items

1. **FY2024 non-GAAP margins 30.2% / (0.6)% from the proxy.** In the proxy (DEF14A-2025.txt lines 2236, 2238: "Adjusted Gross Margin (1) 30.2% 34.7%", "Adjusted Operating Margin (1) (0.6)% 9.7%"). Footnote (1) says the FY2024 measures "have been recast to conform to this refined methodology" adopted in Q1 FY2025, so the draft's "recast to the FY2025 method" is exactly what the proxy says. The proxy's FY2025 figures equal the release's FY2025 column (34.7%, 9.7%), which confirms the methods line up. **Sound; footnote honest.** Nit: label the row "n/s = only in old releases not among this report's sources" is right for FY2022–FY2023.
2. **"No FY2026 proxy existed by the cutoff" tagged [DEF 14A 2025, cover].** Not defensible: a filing cannot evidence the absence of a later filing. The 2025 proxy's cover supports only the filing date (line 44/159: "October 7, 2025"). **Fixed directly:** the tag now sits on the filing date, and the non-existence is attributed to the filings gatherer's check recorded in `sources/FY2026-Q4/MANIFEST.md` ("The FY2026 proxy had not been filed by the cutoff").
3. **Claim 8 (OCS ≥ $400M for 2H CY2026).** The analyst (Papa Sylla, transcript line 113) asked about "the $400 million plus OCS guide for the second half of 2026", implying a prior company guide; the CEO answered "we're definitely tracking to the $400 million. I would not say tracking ahead" and later "leaves us some room to run in the fourth quarter -- fourth calendar quarter" (line 116). So management endorsed both the number and the period, but neither was stated first by management on this call, and neither appears in the release or slides. The period mapping (July–December 2026 = Q1 + Q2 FY2027) is correct. The claim is honest about the period ("the analyst's 'second half of 2026'") and about the source ("transcript figure, not confirmed elsewhere") but does not say the $400 million was also the analyst's framing. **Acceptable as a claim; wording to tighten** (REVISE 8). §3's "(analyst's framing; transcript figure)" already has it right.
4. **"Indium phosphide" transcript-only.** Confirmed: the phrase appears nowhere in the 10-K (only "indium, gallium, germanium" at line 598 as raw materials); the transcript has it at lines 36 ("our 2 indium phosphide wafer fabs in Japan"), 87 and 107 ("convert it from gallium arsenide indium phosphide"). The three sentences that use it (business.md §1 line 8, §6#5 line 114; outlook §3 line 39) are each tagged [Q4 FY2026 call] and none carries a number, so §3 rule 2 (transcript for wording only) is respected. The glossary entry is untagged, which is the glossary convention. **Tags sound.**
5. **Largest customer ≈32% of Q4 (computed, approximate).** FY2026 revenue 3,014.0 × 26.6% = 801.7; nine-month revenue 3,014.0 − 1,006.3 = 2,007.7 × 24% = 481.8; Q4 = 801.7 − 481.8 = 319.9; 319.9 / 1,006.3 = **31.8%**. Because the 24% is rounded to a whole percent, the band is 30.8%–32.8%. Arithmetic and the "(computed, approximate)" label are sound. One unstated assumption: that the 10-K's Customer A (26.6%) is the same company as the 10-Q's 24% customer; each filing letters customers separately, and the 10-Q's second customer (16% for nine months) is close enough that the label matters. Add "assuming the same customer" (REVISE 6).
6. **Q4 capex / OCF / FCF as FY minus nine months.** Capex 451.3 (10-K line 1851) − 284.5 (10-Q line 244) = 166.8; OCF 751.4 (line 1849) − 388.4 (10-Q line 242) = 363.0; FCF 363.0 − 166.8 = 196.2. All exact; the CFO's "$167 million" (transcript line 47) agrees. **Sound.**
7. **The $7,756.6M loss explanation.** Note 10 (line 2915): the loss "consisted primarily of $7,755.1 million of conversion value in excess of principal amounts, $3.1 million of related transaction costs and $2.9 million of unamortized debt issuance costs … partially offset by $2.9 million of forfeited interest and $1.6 million of negotiated exchange discount." The draft's "the market value of the shares handed over, less the debt removed" is that same quantity in plain words (conversion value = shares × share price; debt removed ≈ principal), and the other side of the entry, $8,876.9M to paid-in capital (equity statement line 1933), is consistent with principal $1,124.9M plus the $7,755.1M excess. The framing (notes swap for shares at $69.54–$187.77 while the stock was $390.77) gets a 16-year-old to "the loss is the size of the gift to noteholders, paid in shares, not cash", and "without it, FY2026 pre-tax income was about $584 million" is right (−7,172.8 + 7,756.6). **Accurate and understandable.** Two nits for the writer: "negotiated early conversions" should be "privately negotiated exchanges" (the 10-K's term; an ordinary conversion pays principal in cash, these exchanges were settled entirely in shares), and the paragraph is number-dense (REVISE 3).
8. **Length and padding.** The writer's counts (2,865 / 1,163) reproduce exactly with the §3 rule 7 script. business.md sits in the upper half of its range and the reviewer's glosses took it to 2,985. The padding is not in extra topics but in three prose paragraphs that carry numbers a table should carry (§4 lines 75 and 77, §7 line 122) and in §5's fourth block ("Breadth across the optical chain"), which restates §6#3's vertical-integration risk. Converting those paragraphs to tables would remove 150–250 prose words (REVISE 2–3, 10).

---

## 8. Rubric (§14), from the reader's chair

1. **What the company does and who pays, in two sentences?** Yes. §1–§2: Lumentum makes the laser chips and finished light-based parts (transceivers, optical circuit switches, telecom subsystems) that carry data as light inside and between data centers and across telecom networks, in its own factories; transceiver makers, the giant cloud companies and telecom equipment makers pay per unit, mostly on cancellable purchase orders.
2. **What would kill it and the early warning?** Yes. §6 is ranked, each scenario names the sign to watch (the 10-Q concentration note, inventory versus revenue, price-premium language fading, a BIS/DOJ outcome, the share count on each cover), and it is honest that a single-site failure has no early warning in the filings.
3. **Why the margins are what they are and whether cost scales with usage?** Yes. §3 states the factory model plainly (fixed plant, materials per unit), quotes the 10-K's own 54 / 29 / 17 decomposition of the gross-margin gain, shows the FY2024 collapse as the reverse case, and explains GAAP versus non-GAAP; after the direct fix the two-margin explanation is signposted before the table.
4. **Could I predict next quarter's scorecard from §5 alone?** Yes. Nine of eleven claims are mechanical; 7 ("about $50 million") and, to a lesser degree, 10 (whether a "new target model" was issued) need a small judgment.
5. **Did nothing require knowledge I don't have?** Before fixes, no: operating margin, depreciation, preferred shares, receivables, principal, commoditization, on-target pay, performance units and book value were bare. After the direct glosses, yes for the body text; the §8 indicator wording ("guided range", "utilization-and-pricing lever", "receivables") is left for the owner to plain-word at lock.

---

## 9. Verdict: REVISE

Numbered list for the writer (numbers, quotes, structure, claims and the indicator list were not touched by the reviewer):

1. **outlook.md §1, row 8, "Q3 FY2026" cell.** Replace "(principal by series not summarized)" with "principal $3,198.4M [10-Q Q3 FY2026, Item 2]" — the contractual-obligations table at 10-Q line 2087 gives it. Keep the book value $3,183.4M [Note 9].
2. **business.md §7, line 122.** The paragraph is mostly numbers (rule 5). Move the people and pay facts into a small table (row per person: role, since, prior; rows for bonus mix, PSU mix, FY2023–25 payout, hire award, top holders) and keep two sentences of meaning.
3. **business.md §4, lines 75 and 77.** Both paragraphs are mostly numbers. Suggest a six-row table for the loss (conversion prices; Dec 26, 2025 close; shares issued; principal exchanged; loss; paid-in capital added) and a four-row bridge for cash conversion (non-GAAP operating profit → working capital → tax on vested shares → capex → FCF), with the prose reduced to what each means. Also change "negotiated early conversions" to "privately negotiated exchanges" [10-K FY2026, Item 7; Note 10].
4. **business.md §6#2, line 108.** "Revenue is now mostly cloud and AI" — label "our inference" or anchor to the last disclosed proxy: Cloud & Networking was 85.8% of FY2025 revenue [10-K FY2025, Note 18], noting it includes telecom.
5. **business.md §3, line 36.** "factories are the bigger piece" — label as inference ("our inference, consistent with the 54% utilization share above") or cut.
6. **business.md §6#1, line 97.** Add "assuming the 10-K's largest customer is the same company as the 10-Q's" to the ≈32% sentence, and optionally the 31%–33% rounding band.
7. **outlook.md §5, claim 7.** Replace "about $50 million" with "$50 million or more" (CEO: "the $50 million mark"; "somewhere in the $50 million range") or a labelled band, so the check is mechanical.
8. **outlook.md §5, claim 8.** Reword the attribution: "the analyst's '$400 million plus OCS guide for the second half of 2026', which the CEO endorsed ('tracking to the $400 million')" — both the figure and the period came from the question.
9. **business.md §1, line 6.** The transceiver and OCS descriptions are definitions the 10-K does not contain. Either drop the [10-K FY2026, Item 1] tag from those two clauses (keep it on "Lumentum makes …") or move the definitions to the glossary (OCS already has one; add "Transceiver").
10. **Length.** 2,985 prose words after glosses. Items 2–3 should recover 150–250 words; also consider merging §5's fourth block ("Breadth across the optical chain") into §6#3, which makes the same point.
11. **Indicator list (owner to review at lock; reviewer did not touch).** Indicator 2: "The utilization-and-pricing lever" → "how full the factories are, plus pricing". Indicator 3: "vs the guided range" → "vs the range management forecast". Indicator 4: gloss "receivables (money customers owe)". Outlook §1 row headers should follow.

---

## Fixed directly (glosses, one banned word, two tags, one typo, footnote wording; no numbers, quotes, claims or indicators changed)

business.md
- Line 36: "from 28.0% in FY2026" → "from 28.0% in FY2025" (typo; 10-K-FY2026 line 1386).
- Line 36 (end): added "The table below shows two versions of each margin; the paragraph after it explains the difference." so GAAP / non-GAAP is signposted before the table that uses it.
- Line 50 (footnote): "Employees [...]" → "Employees [...]; the FY2022–FY2023 counts are only in older 10-Ks not among this report's sources."
- Line 52: "8.8 of operating margin in Q4" → "8.8 of operating margin (profit after R&D and selling and administrative costs too, as a share of revenue) in Q4"; "so the leverage arrived at half the modelled revenue" → "so the margin lift arrived at half the modelled revenue".
- Line 56: "3.5 times depreciation (computed)" → "3.5 times depreciation, the yearly charge for wear on existing plant and equipment (computed)".
- Line 75: "What did happen is dilution:" → "What did happen is dilution (each existing share now owns a smaller slice):"; "2.9 million preferred shares sold to NVIDIA" → "2.9 million preferred shares (a separate class of shares, here convertible one-for-one into common) sold to NVIDIA".
- Line 83: added "(products becoming interchangeable, so only price matters)" after "commoditization".
- Line 97: "30.4% of receivables at year-end" → "30.4% of receivables (money customers owed Lumentum) at year-end".
- Line 108: '(up "$59 million sequentially" in Q4)' → '(up "$59 million sequentially", meaning versus the prior quarter, in Q4)'; tag "[Q4 FY2026 call]" → "[Q4 FY2026 call; Q4 FY2026 release; 10-Q Q3 FY2026, Item 1]" (the $59M is confirmed by 691.6 − 632.8).
- Line 118: "Note principal is settled in cash" → "Note principal (the amount borrowed) is settled in cash".
- Line 122: "from the proxy filed October 7, 2025; no FY2026 proxy existed by the 2026-08-17 cutoff [DEF 14A 2025, cover]." → "from the proxy filed October 7, 2025 [DEF 14A 2025, cover]; no FY2026 proxy is among this report's sources (the filings gatherer found none filed by the 2026-08-17 cutoff; see `sources/FY2026-Q4/MANIFEST.md`)."; "on-target pay" → "on-target pay (what he earns if goals are exactly met)"; "half performance units," → "half performance units (shares that pay out only if targets are hit),".
- Glossary: CPO / NPO entry merged into one sentence; CW laser entry: added "(ones whose light-handling parts are built on a silicon chip)" after "silicon photonics" transceivers.

outlook.md
- Line 10 (row 1, Q3 cell): tag "[Q4 FY2026 release]" → "[Q4 FY2026 release; Q4 FY2026 slides, p.4]" (the 66.0% / 34.0% are on slide 4, not in the release).
- Line 17 (row 8): "(book value $1,544.6M)" → "(book value, the balance-sheet amount, $1,544.6M)".

Word counts (§3 rule 7 script): business.md 2,865 → 2,985; outlook.md 1,163 → 1,163. Backups of the pre-fix drafts: `/tmp/lite-business.md.bak`, `/tmp/lite-outlook.md.bak`. No git command was run.

---

## Cycle 2 (re-check of the writer's second pass; review cycle 2 of 2)

_Re-checked 2026-09-07 against `sources/FY2026-Q4/` only (cutoff 2026-08-17). Both drafts re-read in full; line numbers below are the cycle-2 files. Pre-cycle-2 copies: `/tmp/lite-business-c2.md.bak`, `/tmp/lite-outlook-c2.md.bak`. No git command was run._

### 1. Status of the 11 REVISE items

| # | Item | Status | Where |
|---|---|---|---|
| 1 | Outlook §1 row 8 "principal by series not summarized" | **Resolved.** Now "principal $3,198.4M (book value $3,183.4M) [10-Q Q3 FY2026, Item 1; cover; Note 9; Item 2]"; 10-Q line 2087 (principal), line 990 (book value) | outlook.md line 17 |
| 2 | §7 people/pay paragraph mostly numbers | **Resolved.** Three sentences plus a nine-row table | business.md lines 152–164 |
| 3 | §4 loss and cash-conversion paragraphs mostly numbers; "early conversions" wording | **Resolved.** Mechanism-only prose plus "The FY2026 loss, in pieces" (7 rows), a cash-conversion paragraph plus an "FY2026 cash bridge" (9 rows), and a return-on-capital table (7 rows); "privately negotiated exchanges" adopted | lines 75–111 |
| 4 | "mostly cloud and AI" as fact | **Resolved.** "our inference is that they are now most of revenue; the share is not disclosed, and the nearest proxy is the old Cloud & Networking segment at 85.8% of FY2025 revenue, which also held telecom [10-K FY2026, Item 1; 10-K FY2025, Note 18]" | line 138 |
| 5 | "factories are the bigger piece" as fact | **Resolved.** "that the factories are the bigger piece is our inference, consistent with the 54% utilization share above" | line 36 |
| 6 | ≈32% same-customer assumption | **Resolved.** "about 31%–33% given rounding, assuming the 10-K's largest customer is the same company as the 10-Q's (computed, approximate)" | line 127 |
| 7 | Claim 7 "about $50 million" | **Resolved.** "$50 million or more (our sharpening of "the $50 million range" into a floor; transcript figure, not confirmed elsewhere)" | outlook.md line 55 |
| 8 | Claim 8 attribution | **Resolved.** "figure and period are the analyst's framing, endorsed by the CEO"; both quotes given | line 56 |
| 9 | §1 definitions under a 10-K tag | **Resolved.** "In plain words (ours, not the filing's): …" untagged; the tagged clause is now only "Lumentum makes … laser chips for transceivers, finished transceivers, and optical circuit switches"; "Transceiver" added to the Glossary | business.md lines 6, 196 |
| 10 | Length | **Resolved.** 2,985 → 2,695 (2,696 after the one cycle-2 gloss); §5 block 4 merged into §6#3 | — |
| 11 | Indicator wording | **Resolved.** #2 "How full the factories are, plus pricing"; #3 "vs the range management forecast"; #4 "receivables (money customers owe)"; outlook §1 row headers follow | business.md lines 186–188; outlook.md lines 12–13 |

**11 of 11 resolved.**

### 2. New and changed numbers and quotes (every cell of the four new tables and the changed outlook cell)

| Item | Value in draft | Found at | Result |
|---|---|---|---|
| Loss table: conversion prices $69.54 to $187.77 | [Note 10] | 10-K-FY2026.txt lines 2875–2878 (187.77, 69.54, 131.03, 99.29) | PASS |
| Loss table: $390.77 close, Dec 26, 2025 | [cover] | line 78 | PASS |
| Loss table: $1,124.9M principal, about 10.6M shares | [Item 7] | line 1424 | PASS |
| Loss table: $7,756.6M, of which $7,755.1M "conversion value in excess of principal amounts" | [Note 10] | lines 2915 and 1424, phrase verbatim | PASS |
| Loss table: $8,876.9M to paid-in capital | [Item 8] | line 1933 (statement of stockholders' equity) | PASS |
| Loss table: 69.8M → 88.6M + 2.9M preferred; about 31% (computed) | [Item 8; Note 14] | lines 1802, 1953, 3435; (88.6 + 2.9) / 69.8 − 1 = 31.1% | PASS |
| Loss table: pre-tax income without the loss about $584M (computed) | [Item 8] | −7,172.8 + 7,756.6 = 583.8 (line 1727) | PASS |
| Bridge: non-GAAP operating profit 897.0 | [release] | press-release.txt line 231 | PASS |
| Bridge: receivables +270.4, inventory +228.4, payables +221.6 → (277.2) (computed) | [Item 7] | line 1607 (also cash-flow lines 1840–1845); −270.4 − 228.4 + 221.6 = −277.2 | PASS |
| Bridge: other operating items (computed remainder) 131.6 | — | 751.4 − 897.0 + 277.2 = 131.6; check 897.0 − 277.2 + 131.6 = 751.4 | PASS. Note for the owner: the 10-K's total working-capital outflow is $292.0M (line 1607); the row itemizes the three largest lines and the rest sits in this remainder, which the label ("not itemized") makes clear |
| Bridge: OCF 751.4; capex (451.3); FCF 300.1 | [Item 8] | lines 1849, 1851 | PASS |
| Bridge: Q4 alone 363.0 / 166.8 / 196.2 (computed) | [Item 8; 10-Q Item 1] | 751.4 − 388.4 (10-Q line 242); 451.3 − 284.5 (10-Q line 244) | PASS |
| Bridge: vesting tax (281.0), financing outflow | [Item 8] | line 1880 (financing section) | PASS |
| Bridge: five-year 1,541.5 / 1,035.0 / 1,600.5 (computed) | [10-K FY2024 Item 8; 10-K FY2026 Item 8] | sums of the §4 table rows; acquisitions 861.6 + 700.9 + 38.0 (10-K-FY2024 line 1976; 10-K-FY2026 line 1852) | PASS |
| Return table: 1,159.1 / 691.6 / 520.3 / (567.4) → 1,803.6 | [release] | release lines 153, 150, 149, 162 | PASS |
| Return table: 1,396.2 = 1,069.3 + 326.9 | [release] | lines 155–156 | PASS |
| Return table: 3,199.8; 28.0% | computed | 1,803.6 + 1,396.2; 897.0 / 3,199.8 = 28.03% | PASS |
| §7 table: Hurlston 58, Feb 7 2025, Synaptics 2019–2025, Finisar 2018–2019 | [Executive Officers; Director Nominees] | DEF14A-2025.txt lines 2081, 2768, 1145–1147 | PASS |
| §7 table: Ali 52, since Feb 2019, ex-Synaptics CFO | [Executive Officers] | lines 2082, 2088–2092 | PASS |
| §7 table: Herscher independent chair, director since 2015 | [Director Nominees] | lines 247, 665, 1113 | PASS |
| §7 table: Lowe $3.2M severance; about $30M accelerated/modified (computed) | [CD&A] | line 3391: $3,200,000; $8,952,478 + $21,387,742 = $30,340,220 | PASS |
| §7 table: Retort since 2008; retiring Oct 2026, two-year consulting | [Executive Officers; 8-K 2026-07-30] | DEF14A line 2118 (joined JDSU 2008); 8-K lines 57–59 | PASS |
| §7 table: on-target pay $12.1M; $14.0M hire PSUs vs S&P 500 IT index over four years | [CD&A] | lines 2322, 3021 | PASS |
| §7 table: FY2025 bonus 60% / 40%; **"the FY2026 plan is paid in cash"** (new) | [CD&A] | lines 2734–2735; lines 2881–2882 "Any amounts earned under our fiscal year 2026 AIP will be paid entirely in cash; no PSUs were granted as part of the fiscal year 2026 AIP" | PASS |
| §7 table: half PSUs; two-thirds FY2027 revenue; FY2023–25 paid 24% because revenue missed | [CD&A] | lines 2694, 2955 (67%), 312, 3075 ("Total Revenue: 0% Payout 70% weight … Total Payout: 24%") | PASS |
| §7 table: **ownership as of August 29, 2025** (new date); <1%; Vanguard 10.2%, FMR 9.8%, BlackRock 8.8% | [Security Ownership] | Security Ownership preamble ("owned as of August 29, 2025"); lines 3948–3950, 3968–3970 | PASS |
| §7 prose: CEO new and from outside; CFO and chair predate him | [Executive Officers; Director Nominees] | as above | PASS |
| §6#2: "AI and cloud customers" (verbatim); 85.8% FY2025 Cloud & Networking share | [10-K FY2026 Item 1; 10-K FY2025 Note 18] | 10-K-FY2026 line 165; 10-K-FY2025 line 3908 | PASS |
| §6#3: "our competitors may seek to vertically integrate by buying suppliers that also supply products or components to us" | [Item 1A] | line 576 | PASS verbatim |
| Claim 7 quote "somewhere in the $50 million range by the end of the calendar year" | [call] | transcript.txt line 101 | PASS |
| Claim 8 quotes: analyst "the $400 million plus OCS guide for the second half of 2026"; CEO "we're definitely tracking to the $400 million. I would not say tracking ahead." | [call] | lines 113, 116 | PASS verbatim |
| Outlook §1 row 8 Q3 cell: principal $3,198.4M; book value $3,183.4M | [10-Q Item 2; Note 9] | 10-Q-FY2026-Q3.txt lines 2087, 990 | PASS |
| Glossary "Transceiver" | — | one sentence, plain | PASS |

**Cycle-2 tally: 33 checked; 33 PASS; 0 FAIL.** No new number or quote fails; no new untagged factual sentence; the two new inferences (§3 factories, §6#2 cloud share) are labelled.

### 3. Claims 7 and 8 against §9

- **7:** one sentence, one metric (December-2026-quarter ultra-high-power laser revenue), a floor ("$50 million or more"), single direction, can fail (Missed if below, Dropped if silent), sharpening labelled as ours, transcript figure labelled. Holds.
- **8:** one sentence, one metric (OCS revenue for Q1 + Q2 FY2027 ≥ $400M), single direction, can fail, source of both figure and period stated ("the analyst's framing, endorsed by the CEO"), transcript figure labelled, both quotes verbatim. Holds.
- Claims 1–6, 9–11 unchanged and already gradeable. Count 11.

### 4. Structure and coherence after the merge

All §6 skeleton headings present in order (§1–§8, Glossary, Sources); the §2, §3, §4 and §6 tables and the §8 indicator table are intact; §4 now carries four tables and §7 two. §5 has three moat blocks plus the NVIDIA caveat and reads as a complete argument (scarce laser know-how; qualification and long-term agreements; only merchant OCS supplier). §6#3, retitled "Competitors or customers make their own lasers or parts", absorbs the vertical-integration point with the 10-K quote and its early-warning line still fits. Outlook §1 has one row per indicator; §6 Tone shift still correctly omitted; Sources tables cover every tag prefix in both files (re-extracted). The "New targets come 'probably at the next OFC'" sentence dropped from outlook §2 survives in §4, so nothing is lost.

### 5. Cycle-1 direct edits

All 18 intact (business.md: typo, table pointer, employee footnote, operating-margin and depreciation glosses, "margin lift", dilution and preferred glosses (now in the loss table, line 84), commoditization, receivables, sequentially + tags, principal, proxy-tag sentence, on-target pay and performance-unit glosses (now in the §7 table), CPO/NPO and CW glossary edits; outlook.md: slides p.4 tag, book-value gloss).

### 6. Word counts (§3 rule 7 script)

- business.md: **2,696** (writer reported 2,695; +1 from the cycle-2 gloss below). Within 2,000–3,000, lower half.
- outlook.md: **1,172**. Within 800–1,200.

### 7. Rubric (§14), brief

1. What they do and who pays: yes (§1–§2 unchanged in substance). 2. What would kill it and the early warning: yes (§6 ranked, each with a sign). 3. Why the margins and whether cost scales: yes; the two-margin explanation is signposted before the §3 table and the FY2024 reverse case is shown. 4. Predict next quarter's scorecard from §5: yes; all eleven claims are now mechanical (claim 10 asks only whether a new model's floor is at least 39%). 5. Nothing requiring outside knowledge: yes for the body; the §8 indicator wording is now plain.

### 8. Fixed directly in cycle 2

- business.md line 87: "the first gap between adjusted profit and operating cash flow" → "the first gap between adjusted (non-GAAP) profit and operating cash flow" (the bridge table row says "Non-GAAP operating profit"; the prose now uses the same term).

### 9. Notes for the owner (not failures)

1. §4 cash bridge: the working-capital row itemizes the three largest lines ((277.2)); the 10-K's total working-capital outflow is $292.0M [10-K FY2026, Item 7, line 1607], the difference sitting in the labelled remainder. A relabel to "three largest working-capital items" would make this explicit.
2. Outlook §1 rows 5 and 8 still carry three or four figures per cell; readable but dense.
3. §8 indicators are proposed, not locked; wording is now plain, and the owner's lock is the next step.

### Final verdict: **PASS**

No substantive failure remains: every table cell and quote verifies, every computed figure re-derives, all eleven REVISE items are resolved as the writer described, both files are inside the length range, and the claims list is mechanical.
