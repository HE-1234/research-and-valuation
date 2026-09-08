# Reddit (RDDT) — Q2 2026 IR gatherer notes: press release + shareholder letter (+ Q1 2026 release and letter for prior-quarter comparison)

- Company: Reddit, Inc., NYSE: RDDT, CIK 0001713445. Fiscal year = calendar year (no parenthetical needed on quarter labels).
- Quarter: Q2 2026 (quarter ended June 30, 2026). Prior quarter: Q1 2026 (quarter ended March 31, 2026).
- As-of cutoff: 2026-07-31. Q2 release datelined "SAN FRANCISCO, Calif. – July 30, 2026"; furnished as 8-K Exhibit 99.1 accepted by EDGAR 2026-07-30 16:09:38 ET. Q2 letter PDF: Canva, CreationDate 2026-07-22, ModDate 2026-07-29 20:48 UTC, title "Q2 '26 Shareholder Letter". Q1 release datelined "April 30, 2026" (8-K accepted 2026-04-30 16:08:35 ET); Q1 letter ModDate 2026-04-29, title "Q1'26 Shareholder Letter". Nothing published after 2026-07-31 was fetched or read.
- Reddit publishes no earnings slide deck. The shareholder letter (22 pages, 1440x810 pt landscape) plays the deck's role: KPI charts, financial charts, guidance, financial statements and non-GAAP reconciliations are all in it. The Q4 Inc. FinancialReport feeds for 2025 and 2026 list, per quarter, only: Earnings Release, Shareholder Letter, Webcast, Earnings Call Transcript, 10-Q/10-K, r/RDDT AMA post (Q1 2025 also an AMA video and AMA transcript). No "Presentation" or "Slides" item exists in any 2025 or 2026 quarter. The 8-K also furnishes the letter as Exhibit 99.2, but only as 22 JPG images (image-only), so the q4cdn PDF is the text source.
- Cached text (all in this folder; see `MANIFEST-ir.md`): `press-release.txt` (Q2 2026 release; 8-K Exhibit 99.1 HTML stripped to text; 4,931 words), `shareholder-letter.txt` (Q2 2026 letter, `pdftotext -layout`, 22 pages, 6,122 words), `shareholder-letter-reading-order.txt` (same PDF, `pdftotext` without `-layout`, for the two-column prose pages), `press-release-2026-Q1.txt` (Q1 2026 release, 3,996 words), `shareholder-letter-2026-Q1.txt` (Q1 2026 letter, 22 pages, 5,740 words).
- Tags: `[Q2 2026 release, p.N <section>]` = press-release.txt; `[Q2 2026 letter, p.N]` = shareholder-letter.txt; `[Q1 2026 release, p.N <section>]` = press-release-2026-Q1.txt; `[Q1 2026 letter, p.N]` = shareholder-letter-2026-Q1.txt.
- Page numbering. Releases: the HTML exhibits DO carry printed page numbers 1–11 (a bare digit closes each page; the release's own footnote points to "pages 10-11" for the reconciliations), so release tags use those printed pages plus the section name. Letters: printed footers read "Q2 2026 • Letter to Shareholders <n>" and printed page numbers EQUAL PDF page numbers on every page (cover p.1 has no number; p.4 prints a bare "4" without the footer text; p.13 of the Q2 letter misprints its footer as "Q1 2026 • Letter to Shareholders 13" — a company typo, the page is Q2 content).
- Release page map (both quarters identical in structure): p.1 headline bullets, dateline, CEO quote, bullet highlights; p.2 Financial Highlights table, Financial Outlook (guidance), conference-call details; p.3 community Q&A note, Regulation FD channels, Notes, About Reddit, contacts; p.4 Forward-Looking Statements, A Note About Metrics (DAUq/WAUq/ARPU definitions), Use of Non-GAAP Financial Measures (start); p.5 non-GAAP definitions; p.6 Key Operating Metrics by Geography; p.7 Statements of Operations; p.8 Balance Sheets; p.9 Cash Flows; p.10 Adjusted EBITDA reconciliation; p.11 Free Cash Flow reconciliation. The release has NO non-GAAP cost reconciliation and NO SBC-by-function table (those are letter-only, p.22).
- Q2 letter page map: p.1 cover; p.2 financial highlights (text); p.3 business highlights + DAUq and WAUq stacked-bar charts (5 quarters); p.4–5 CEO letter (two columns); p.6 revenue / opex per headcount chart; p.7 consumer product; p.8 advertising & monetization + Wise case study + third-party validation; p.9 P&L charts (revenue by geography, gross margin, opex, net income / Adj. EBITDA); p.10 ARPU, "Rule of 40", revenue vs cost growth, margin trends; p.11 cash, fully diluted shares, operating cash flow, SBC; p.12 Financial outlook (Q3 2026 guidance); p.13 call details; p.14 appendix notes, About Reddit, forward-looking statements, metric definitions; p.15 non-GAAP definitions, IR contacts; p.16 Key Operating Metrics by Geography table; p.17 Statements of Operations; p.18 Balance Sheets; p.19 Cash Flows; p.20 Adj. EBITDA reconciliation; p.21 FCF reconciliation; p.22 non-GAAP costs reconciliation (by function). Q1 letter: same map except p.6 is a "1 of 1 financial model" FactSet comparison page, p.7 is "Consumer product & internationalization", p.8 has Liquid I.V. and Cozey case studies, p.13 adds "Reddit AMA highlights".
- Chart extraction (x-coordinates below are bbox metadata in points, not source figures): every chart page yielded its data labels as text (no page is image-only for data), but `pdftotext -layout` returns the labels in scrambled order. The quarter mapping of every series below was fixed with word x-coordinates from `pdftotext -bbox` on Q2 letter pp.3, 6, 9, 10, 11 (five bar columns at x≈300/380/460/540/620 or ≈985/1065/1145/1225/1300 pt map to Q2'25, Q3'25, Q4'25, Q1'26, Q2'26) and confirmed by a visual read of 72-dpi renders of pp.3, 6, 7, 8, 9, 10, 11 (and Q1 letter pp.7, 8). One catch that the flat text gets wrong: on p.9 the Q4'25 bars are net income $251.6M and Adjusted EBITDA $327.0M (not the reverse). Q1-letter-only values (the Q1'25 column) were mapped by overlap with the Q2 letter (four shared quarters match exactly) and by arithmetic, not by bbox. All stacked-bar components foot to their totals (checked below).
- Units: release Financial Highlights table is USD millions; statements are USD thousands; KPI tables are millions of users and USD for ARPU; letter charts are USD millions (per-headcount chart USD thousands; cash chart USD billions). Every number is copied verbatim; anything derived is labelled "(computed)".

## 1. Headline metrics: Q2 2026 vs Q2 2025 vs Q1 2026

Release Financial Highlights table (USD millions except percentages and per-share; three months ended June 30; 2026 vs 2025; % change) [Q2 2026 release, p.2 Financial Highlights]; Q1 2026 column from the Q1 release table (three months ended March 31, 2026) [Q1 2026 release, p.2 Financial Highlights].

| Metric | Q2 2026 | Q2 2025 | % change (stated) | Q1 2026 |
|---|---|---|---|---|
| Revenue | $805 | $500 | 61% | $663 |
| Revenue: U.S. | $638 | $409 | 56% | $526 |
| Revenue: International | $167 | $91 | 84% | $138 |
| Advertising revenue (bullets, p.1) | $762 | not stated (64% growth) | 64% | $625 |
| Other revenue (bullets, p.1) | $43 | not stated (24% growth) | 24% | $39 |
| GAAP gross margin | 91.3% | 90.8% | +50 bps | 91.5% |
| Net income | $253 | $89 | 183% | $204 |
| Net margin | 31.4% | 17.9% | — | 30.7% |
| EPS basic | $1.31 | $0.48 | 173% | $1.07 |
| EPS diluted | $1.25 | $0.45 | 178% | $1.01 |
| Adjusted EBITDA | $343 | $167 | 106% | $266 |
| Adjusted EBITDA margin | 42.6% | 33.4% | — | 40.1% |
| Net cash provided by operating activities | $262 | $111 | 135% | $312 |
| Free Cash Flow | $261 | $111 | 135% | $311 |
| Cash, cash equivalents and marketable securities (period end) | $2,786 | not shown | — | $2,771 |

- Exact figures (USD thousands) [Q2 2026 letter, p.17] [Q2 2026 release, p.7 Statements of Operations]: revenue 804,905 vs 499,627; cost of revenue 70,308 vs 45,900; R&D 231,276 vs 196,610; S&M 195,897 vs 120,619; G&A 75,708 vs 68,787; total costs and expenses 573,189 vs 431,916; income from operations 231,716 vs 67,711; other income (expense), net 25,119 vs 21,147; income before taxes 256,835 vs 88,858; income tax expense (benefit) 3,987 vs (439); net income 252,848 vs 89,297. Six months: revenue 1,468,316 vs 891,988; income from operations 414,628 vs 71,614; net income 456,829 vs 115,455.
- Q1 2026 exact (USD thousands) [Q1 2026 letter, p.17]: revenue 663,411 vs 392,361; cost of revenue 56,267 vs 37,089; R&D 207,246 vs 191,271; S&M 151,472 vs 90,685; G&A 65,514 vs 69,413; total costs and expenses 480,499 vs 388,458; income from operations 182,912 vs 3,903; other income, net 22,816 vs 20,534; income tax expense (benefit) 1,747 vs (1,721); net income 203,981 vs 26,158.
- Operating margin (computed, not stated anywhere): Q2 2026 231,716 / 804,905 = 28.8%; Q2 2025 67,711 / 499,627 = 13.6%; Q1 2026 182,912 / 663,411 = 27.6%.
- Weighted-average shares: basic 192,345,684 vs 185,437,777; diluted 202,029,721 vs 199,522,433 (Q2). Six months basic 191,932,329 vs 183,730,992; diluted 202,326,864 vs 200,681,458. [Q2 2026 letter, p.17] Q1 2026: basic 191,518,973 vs 182,024,207; diluted 202,524,173 vs 201,275,223. [Q1 2026 letter, p.17]
- Release headline bullets, verbatim [Q2 2026 release, p.1]: "Daily Active Uniques ("DAUq") increased 18% year-over-year to 130.3 million"; "Weekly Active Uniques ("WAUq") increased 24% year-over-year to 514.6 million, crossing half a billion"; "Revenue of $805 million grew 61% year-over-year. 8th consecutive quarter over 60%"; "Net income of $253 million, 31% of revenue, and Diluted EPS of $1.25, both up over 2x year-over-year"; "Adj. EBITDA of $343 million, 43% of revenue, up 106% year-over-year"; "Operating cash flow of $262 million, 33% of revenue, up 135% year-over-year".
- Release bullet highlights, verbatim [Q2 2026 release, p.1]: "Total revenue increased 61% year-over-year to $805 million, Ad revenue increased 64% year-over-year to $762 million, and Other revenue increased 24% year-over-year to $43 million"; "Gross margin was 91.3%, as compared to 90.8% in the prior year, up 50 bps year-over-year"; "Net income was $253 million, an improvement of $164 million from the prior year and more than doubling year-over-year"; "Adjusted EBITDA was $343 million, an improvement of $176 million from the prior year and more than doubling year-over-year"; "Operating cash flow was $262 million, an improvement of $151 million from the prior year and more than doubling year-over-year"; "Free Cash Flow was $261 million, an improvement of $150 million from the prior year and more than doubling year-over-year"; "Basic and diluted earnings per share ("EPS") were $1.31 and $1.25, more than doubling year-over-year"; "Total fully diluted shares outstanding were 207.0 million as of June 30, 2026, up 0.2% from the prior year"; "We repurchased 1.5 million shares of our Class A common stock during the quarter for a total of $235 million at an average price per share of $157.57".
- Letter financial highlights add [Q2 2026 letter, p.2]: "Capital expenditures were $1 million, 0.1% of revenue"; "Cash, cash equivalents, and marketable securities were $2.8 billion as of June 30, 2026"; "Total fully diluted shares outstanding were 207.0 million as of June 30, 2026, up 0.2% from the prior year"; "Share repurchases: 1.5 million shares repurchased during the quarter for a total of $235 million at an average price per share of $157.57"; diluted EPS "up 178% from prior year".
- Cash and marketable securities detail (USD thousands) [Q2 2026 letter, p.18]: cash and cash equivalents 1,486,838 and marketable securities 1,299,519 at June 30, 2026 (sum 2,786,357, computed, = the release's $2,786M) vs 953,569 and 1,523,242 at December 31, 2025. Q1: 1,374,348 and 1,396,284 at March 31, 2026 (sum 2,770,632, computed) [Q1 2026 letter, p.18]. No debt line appears on either balance sheet; total liabilities 350,905 at June 30, 2026 [Q2 2026 letter, p.18].
- Headcount: not disclosed in release or letter. Revenue per employee: the CEO letter says the company "crossed a major milestone we've been chasing: $1 million in revenue per employee" [Q2 2026 letter, p.4]; the chart value is $1,077 thousand (trailing-four-quarter revenue divided by average trailing-four-quarter headcount; see §8) [Q2 2026 letter, p.6]. Implied average headcount (computed, approximate): TTM revenue $2,778.8M (584.9 + 725.6 + 663.4 + 804.9) / $1.077M ≈ 2,580.
- Revenue per employee is a letter-only figure; the release only carries the CEO quote about crossing $1 million [Q2 2026 release, p.1].

## 2. User KPIs

### 2.1 Definitions, verbatim [Q2 2026 release, p.4 A Note About Metrics] (identical wording in [Q2 2026 letter, p.14] and in the Q1 documents)

- "We define a daily active unique ("DAUq") as a user whom we can identify with a unique identifier who has visited a page on the Reddit website, www.reddit.com, or opened a Reddit application at least once during a 24-hour period. Average DAUq for a particular period is calculated by adding the number of DAUq on each day of that period and dividing that sum by the number of days in that period."
- "We define a weekly active unique ("WAUq") as a user whom we can identify with a unique identifier who has visited a page on the Reddit website, www.reddit.com, or opened a Reddit application at least once during a trailing seven-day period. Average quarterly WAUq for a particular period is calculated by adding the number of WAUq on each day of that period and dividing that sum by the number of days in that period."
- "We define average revenue per unique ("ARPU") as quarterly revenue in a given geography divided by the average DAUq in that geography. For the purposes of calculating ARPU, advertising revenue in a given geography is based on the geographic location in which advertising impressions are delivered, as this approximates revenue based on user activity, while other revenue in a given geography is based on the billing address of the customer."
- Logged-in / logged-out: neither the release nor the letter defines these terms; they appear only as row labels ("Logged-in DAUq", "Logged-out DAUq") in the KPI table and as "Logged-in users" / "Logged-out users" in the business highlights. Not defined in the IR documents (the 10-Q/10-K may define them; filings gatherer).

### 2.2 KPI table, Q2 2026 vs Q2 2025 (millions of users; USD for ARPU) [Q2 2026 release, p.6 Key Operating Metrics by Geography] (identical table [Q2 2026 letter, p.16])

| Metric | Q2 2026 | Q2 2025 | % change |
|---|---|---|---|
| DAUq: Global | 130.3 | 110.4 | 18% |
| DAUq: U.S. | 53.2 | 50.3 | 6% |
| DAUq: International | 77.1 | 60.1 | 28% |
| Logged-in DAUq: Global | 52.6 | 49.3 | 7% |
| Logged-in DAUq: U.S. | 23.1 | 22.9 | 1% |
| Logged-in DAUq: International | 29.5 | 26.4 | 12% |
| Logged-out DAUq: Global | 77.7 | 61.1 | 27% |
| Logged-out DAUq: U.S. | 30.1 | 27.4 | 10% |
| Logged-out DAUq: International | 47.6 | 33.7 | 41% |
| WAUq: Global | 514.6 | 416.4 | 24% |
| WAUq: U.S. | 197.2 | 181.0 | 9% |
| WAUq: International | 317.4 | 235.4 | 35% |
| ARPU: Global | $6.18 | $4.53 | 36% |
| ARPU: U.S. | $11.85 | $7.87 | 51% |
| ARPU: International | $2.26 | $1.73 | 31% |

- Footing (computed): logged-in + logged-out = 52.6 + 77.7 = 130.3 Global; 23.1 + 30.1 = 53.2 U.S.; 29.5 + 47.6 = 77.1 International; U.S. + International DAUq = 130.3; WAUq 197.2 + 317.4 = 514.6. All foot.
- Logged-in share of DAUq (computed): Global 40.4% in Q2 2026 vs 44.7% in Q2 2025; U.S. 43.4% vs 45.5%; International 38.3% vs 43.9%.

### 2.3 KPI table, Q1 2026 vs Q1 2025 [Q1 2026 release, p.6 Key Operating Metrics by Geography] (identical [Q1 2026 letter, p.16])

| Metric | Q1 2026 | Q1 2025 | % change |
|---|---|---|---|
| DAUq: Global | 126.8 | 108.1 | 17% |
| DAUq: U.S. | 53.5 | 50.1 | 7% |
| DAUq: International | 73.3 | 58.0 | 26% |
| Logged-in DAUq: Global | 52.0 | 48.7 | 7% |
| Logged-in DAUq: U.S. | 23.2 | 23.0 | 1% |
| Logged-in DAUq: International | 28.8 | 25.8 | 12% |
| Logged-out DAUq: Global | 74.8 | 59.4 | 26% |
| Logged-out DAUq: U.S. | 30.3 | 27.1 | 12% |
| Logged-out DAUq: International | 44.5 | 32.2 | 38% |
| WAUq: Global | 493.1 | 401.3 | 23% |
| WAUq: U.S. | 196.5 | 178.3 | 10% |
| WAUq: International | 296.6 | 223.0 | 33% |
| ARPU: Global | $5.23 | $3.63 | 44% |
| ARPU: U.S. | $9.63 | $6.27 | 54% |
| ARPU: International | $2.02 | $1.34 | 51% |

- Footing (computed): 52.0 + 74.8 = 126.8; 23.2 + 30.3 = 53.5; 28.8 + 44.5 = 73.3; 48.7 + 59.4 = 108.1. All foot.
- Sequential (computed from the two tables): U.S. DAUq fell from 53.5 (Q1 2026) to 53.2 (Q2 2026); U.S. logged-in DAUq 23.2 to 23.1; U.S. logged-out 30.3 to 30.1; International DAUq rose 73.3 to 77.1; Global logged-out rose 74.8 to 77.7; Global logged-in 52.0 to 52.6.

### 2.4 Six-quarter DAUq and WAUq series (millions; stacked-bar labels, quarter mapping bbox-confirmed for Q2'25–Q2'26)

Q2 letter chart "Q2 '26 DAILY ACTIVE UNIQUES" and "Q2 '26 WEEKLY ACTIVE UNIQUES", quarters Q2 '25, Q3 '25, Q4 '25, Q1 '26, Q2 '26 [Q2 2026 letter, p.3]; Q1 '25 column from the Q1 letter's equivalent charts (Q1 '25 – Q1 '26) [Q1 2026 letter, p.3]. Logged-in / logged-out splits are NOT charted; they exist only for the four quarters in the release tables above.

| Quarter | DAUq Global | DAUq U.S. | DAUq Int'l | WAUq Global | WAUq U.S. | WAUq Int'l |
|---|---|---|---|---|---|---|
| Q1 '25 | 108.1 | 50.1 | 58.0 | 401.3 | 178.3 | 223.0 |
| Q2 '25 | 110.4 | 50.3 | 60.1 | 416.4 | 181.0 | 235.4 |
| Q3 '25 | 116.0 | 51.6 | 64.4 | 443.8 | 187.8 | 256.0 |
| Q4 '25 | 121.4 | 52.5 | 68.9 | 471.6 | 193.4 | 278.2 |
| Q1 '26 | 126.8 | 53.5 | 73.3 | 493.1 | 196.5 | 296.6 |
| Q2 '26 | 130.3 | 53.2 | 77.1 | 514.6 | 197.2 | 317.4 |

- Footing (computed): U.S. + Int'l equals the printed total in all six quarters for both DAUq and WAUq.
- Growth rates as stated: "Logged-in users grew 7% and Logged-out users grew 27% year-over-year"; "U.S. DAUq grew 6% year-over-year and international DAUq grew 28% year-over-year" [Q2 2026 letter, p.3]. Q1: "Logged-in users grew 7% and Logged-out users grew 26% year-over-year"; "U.S. DAUq grew 7% year-over-year and International DAUq grew 26% year-over-year" [Q1 2026 letter, p.3].
- DAUq-to-WAUq ratio (computed): Q2 2026 130.3 / 514.6 = 25.3%; Q2 2025 110.4 / 416.4 = 26.5%; U.S. 53.2 / 197.2 = 27.0%; International 77.1 / 317.4 = 24.3%.

### 2.5 Six-quarter ARPU series (USD; bbox-confirmed for Q2'25–Q2'26)

Chart "Q2 '26 AVERAGE REVENUE PER UNIQUE (ARPU)", stacked labels: global total on top, U.S. and Int'l inside [Q2 2026 letter, p.10]; Q1 '25 from [Q1 2026 letter, p.10].

| Quarter | ARPU Global | ARPU U.S. | ARPU Int'l |
|---|---|---|---|
| Q1 '25 | $3.63 | $6.27 | $1.34 |
| Q2 '25 | $4.53 | $7.87 | $1.73 |
| Q3 '25 | $5.04 | $9.04 | $1.84 |
| Q4 '25 | $5.98 | $10.79 | $2.31 |
| Q1 '26 | $5.23 | $9.63 | $2.02 |
| Q2 '26 | $6.18 | $11.85 | $2.26 |

- Caption: "ARPU was $6.18, up 36% year-over-year" [Q2 2026 letter, p.10]; "ARPU was $5.23, up 44% year-over-year" [Q1 2026 letter, p.10].
- Footing note (computed): Global ARPU x Global DAUq reproduces revenue (6.18 x 130.3 = $805.3M vs $804.9M). Regional ARPU x regional DAUq does NOT reproduce the "Revenue: U.S." / "Revenue: International" lines: 11.85 x 53.2 = $630.4M vs U.S. revenue $638.1M; 2.26 x 77.1 = $174.2M vs International revenue $166.8M (the two implied figures sum to $804.6M). Same pattern in Q1 2026 (9.63 x 53.5 = $515.2M vs $525.6M; 2.02 x 73.3 = $148.1M vs $137.8M) and Q2 2025 (7.87 x 50.3 = $395.9M vs $408.8M). The ARPU definition allocates advertising revenue by impression-delivery location; the basis of the revenue-by-geography lines is not stated in the release or letter. Writers should not derive regional revenue from ARPU x DAUq.

## 3. Revenue by type and geography; gross margin

### 3.1 Revenue by type (only the current quarter of each release/letter; the letters do not chart revenue by type)

| Quarter | Advertising | Other | Total | Ad growth (stated) | Other growth (stated) | Source |
|---|---|---|---|---|---|---|
| Q2 2026 | $762M | $43M | $805M | 64% | 24% | [Q2 2026 release, p.1] [Q2 2026 letter, p.3] |
| Q1 2026 | $625M | $39M | $663M | 74% | 15% | [Q1 2026 release, p.1] [Q1 2026 letter, p.3] |

- Year-ago values implied by the stated growth rates (computed, approximate): Q2 2025 advertising ≈ $465M (762 / 1.64) and other ≈ $35M (43 / 1.24), sum ≈ $499M vs reported $499.6M; Q1 2025 advertising ≈ $359M (625 / 1.74) and other ≈ $34M (39 / 1.15), sum ≈ $393M vs reported $392.4M.
- Q1 2026 type split does not foot exactly: $625M + $39M = $664M vs total $663M (rounding of each component; total is $663.4M). Q2 2026 foots ($762M + $43M = $805M).
- Driver statements, verbatim: "Advertising revenue growth was driven by year-over-year growth in pricing and impressions" [Q2 2026 letter, p.3]; Q1: "Advertising revenue growth was driven by year-over-year growth in impressions and pricing" [Q1 2026 letter, p.3] (order of the two words is reversed between quarters). "Broad strength across the full ad funnel and industry verticals" [Q2 2026 letter, p.3]; Q1: "Broad strength across the full ad funnel and our top-15 industry verticals" [Q1 2026 letter, p.3].
- Other revenue commentary: the Q2 letter and release contain no commentary on data-licensing customers, renewals or new agreements; "Other revenue" appears only as the $43M / +24% line. Not disclosed in the IR documents (10-Q may say more; filings gatherer).

### 3.2 Revenue by geography, six quarters (USD millions; Q2'25–Q2'26 bbox-confirmed from the stacked bars on [Q2 2026 letter, p.9]; Q1 '25 from [Q1 2026 letter, p.9]; the Q2'25/Q2'26 and Q1'25/Q1'26 columns also appear in the release tables)

| Quarter | Total | U.S. | International | Revenue Y/Y growth (stated) |
|---|---|---|---|---|
| Q1 '25 | $392.4 | $313.9 | $78.5 | 61% |
| Q2 '25 | $499.6 | $408.8 | $90.8 | 78% |
| Q3 '25 | $584.9 | $479.6 | $105.3 | 68% |
| Q4 '25 | $725.6 | $583.3 | $142.3 | 70% |
| Q1 '26 | $663.4 | $525.6 | $137.8 | 69% |
| Q2 '26 | $804.9 | $638.1 | $166.8 | 61% |

- Growth rates: Q2 2026 U.S. 56%, International 84% [Q2 2026 release, p.6]; six months U.S. $1,163.7M (+61%), International $304.6M (+80%), Global $1,468.3M (+65%) [Q2 2026 release, p.6]. Q1 2026 U.S. 67%, International 76% [Q1 2026 release, p.6]. Revenue Y/Y growth series (Rule-of-40 chart) 78%, 68%, 70%, 69%, 61% for Q2'25–Q2'26 [Q2 2026 letter, p.10]; the Q1 letter's growth-vs-cost chart gives one-decimal values 61.5%, 77.7%, 67.9%, 69.7%, 69.1% for Q1'25–Q1'26 [Q1 2026 letter, p.10].
- International share of revenue (computed): 20.7% in Q2 2026 vs 18.2% in Q2 2025 and 20.8% in Q1 2026.
- Sequential (computed): total revenue +21.3% Q/Q (663.4 to 804.9); U.S. +21.4%; International +21.0%.

### 3.3 Gross margin and cost of revenue, six quarters [Q2 2026 letter, p.9] [Q1 2026 letter, p.9]

| Quarter | Gross margin | Cost of revenue ($M) |
|---|---|---|
| Q1 '25 | 90.5% | $37.1 |
| Q2 '25 | 90.8% | $45.9 |
| Q3 '25 | 91.0% | $52.5 |
| Q4 '25 | 91.9% | $58.7 |
| Q1 '26 | 91.5% | $56.3 |
| Q2 '26 | 91.3% | $70.3 |

- Caption: "Gross margin was 91.3%, an improvement of 50 bps year-over-year" [Q2 2026 letter, p.9]. Check (computed): (804.9 − 70.3) / 804.9 = 91.3%.

## 4. Guidance

### 4.1 Q3 2026 guidance (given July 30, 2026), verbatim

- Release "Financial Outlook", complete [Q2 2026 release, p.2 Financial Outlook]: "The guidance provided below is based on Reddit's current estimates and is not a guarantee of future performance. This guidance is subject to significant risks and uncertainties that could cause actual results to differ materially, including the risk factors discussed in Reddit's reports on file with the Securities and Exchange Commission (the "SEC"). Reddit undertakes no duty to update any forward-looking statements or estimates, except as required by applicable law." "As we look ahead, we will share our internal thoughts on revenue and Adjusted EBITDA for the third quarter." "In the third quarter of 2026, we estimate: • Revenue in the range of $860 million to $870 million • Adjusted EBITDA in the range of $385 million to $395 million".
- Letter "Financial outlook" page repeats the same two sentences and the same ranges, with callouts "Q3 '26 REVENUE $860M-$870M" and "Q3 '26 ADJUSTED EBITDA $385M-$395M" [Q2 2026 letter, p.12].
- Footnote to the Adjusted EBITDA guidance, verbatim [Q2 2026 release, p.3 Notes]: "We have not provided a reconciliation to the forward-looking U.S. GAAP equivalent measures for our non-GAAP guidance due to uncertainty regarding, and the potential variability of, reconciling items. Therefore, a reconciliation of these non-GAAP guidance measures to their corresponding U.S. GAAP guidance measures is not available without unreasonable effort."
- No full-year guidance, no DAUq guidance, no margin guidance, no capex or share-count guidance, no FX statement appears in the release or letter. [Q2 2026 release, p.2] [Q2 2026 letter, p.12]
- Implied by the Q3 2026 ranges (computed): revenue growth vs Q3 2025 ($584.9M) of 47.0% to 48.7%; sequential revenue growth vs Q2 2026 ($804.9M) of 6.8% to 8.1%; Adjusted EBITDA growth vs Q3 2025 ($236.0M) of 63.1% to 67.4%; Adjusted EBITDA margin 44.3% ($385M / $870M) to 45.9% ($395M / $860M), midpoint 45.1% ($390M / $865M).

### 4.2 Q2 2026 guidance as given on April 30, 2026, verbatim (fills "what management had said to expect")

- Release [Q1 2026 release, p.2 Financial Outlook]: "As we look ahead, we will share our internal thoughts on revenue and Adjusted EBITDA for the second quarter." "In the second quarter of 2026, we estimate: • Revenue in the range of $715 million to $725 million • Adjusted EBITDA in the range of $285 million to $295 million". Preceded by the same risk-disclaimer paragraph as above.
- Letter [Q1 2026 letter, p.12]: same sentences and ranges; callouts "Q2 '26 REVENUE $715M-$725M" and "Q2 '26 ADJUSTED EBITDA $285M-$295M".
- The Q1 letter gives no other Q2 expectation (no DAUq, margin, expense or capex outlook for Q2) beyond the two ranges. The CEO letter's forward statements are for "the remainder of 2026" as priorities, not numbers (see §7). [Q1 2026 letter, pp.4–5, 12]

### 4.3 Q2 2026 guidance versus actual (computed)

| Item | Guidance (Apr 30, 2026) | Midpoint | Actual Q2 2026 | vs high end | vs midpoint |
|---|---|---|---|---|---|
| Revenue | $715M–$725M | $720M | $804.9M | +$79.9M (+11.0%) | +$84.9M (+11.8%) (computed) |
| Adjusted EBITDA | $285M–$295M | $290M | $342.8M | +$47.8M (+16.2%) | +$52.8M (+18.2%) (computed) |
| Implied revenue growth Y/Y | 43.1%–45.1% (vs Q2 2025 $499.6M) | 44.1% | 61% | — | — |
| Implied Adj. EBITDA margin | 39.3% ($285M/$725M) – 41.3% ($295M/$715M) | 40.3% | 42.6% | — | — |

- Actuals from [Q2 2026 release, p.6] and [Q2 2026 release, p.10]; guidance from [Q1 2026 release, p.2 Financial Outlook].

## 5. Non-GAAP reconciliations and definitions

### 5.1 Definitions, verbatim

- Adjusted EBITDA [Q2 2026 release, p.5 Use of Non-GAAP Financial Measures]: "Adjusted EBITDA is defined as net income excluding interest (income) expense, net, income tax expense (benefit), depreciation and amortization, stock-based compensation expense and related taxes, other (income) expense, net, and certain other non-recurring or non-cash items impacting net income that we do not consider indicative of our ongoing business performance. Other (income) expense, net consists primarily of realized gains and losses on sales of marketable securities, foreign currency transaction gains and losses, and other income and expense that are not indicative of our core operating performance. Adjusted EBITDA margin is defined as Adjusted EBITDA divided by revenue."
- Free Cash Flow [Q2 2026 release, p.5]: "Free Cash Flow represents net cash provided by (used in) operating activities less purchases of property and equipment. Free Cash Flow margin is defined as Free Cash Flow divided by revenue. We believe that Free Cash Flow is useful to investors as a liquidity measure because it measures our ability to generate or use cash. Once our business needs and obligations are met, cash can be used to maintain a strong balance sheet and invest in future growth. Additionally, we believe that Free Cash Flow is an important measure since we use third-party infrastructure partners to host our services and therefore we do not incur significant capital expenditures to support revenue generating activities."
- Letter-only measures [Q2 2026 letter, p.15]: "Incremental Adjusted EBITDA margin is defined as the change in Adjusted EBITDA divided by the change in revenue over the same period. Rule of 40 is defined as the year-over-year revenue growth rate plus adjusted EBITDA margin over the same period." "Total adjusted costs and expenses represents cost of revenue and operating expenses excluding stock-based compensation and related taxes, depreciation and amortization, and certain other non-recurring or non-cash items impacting cost of revenue and operating expenses that we do not consider indicative of our ongoing business performance. Non-GAAP operating expenses represents operating expenses excluding stock-based compensation and related taxes, depreciation and amortization, and certain other non-recurring or non-cash items impacting operating expenses that we do not consider indicative of our ongoing business performance. Non-GAAP research and development expense, non-GAAP sales and marketing expense, and non-GAAP general and administrative expense represent their respective operating expense line items excluding stock-based compensation and related taxes, depreciation and amortization, and certain other non-recurring or non-cash items."
- The release lists only "Adjusted EBITDA, Adjusted EBITDA margin, Free Cash Flow, and Free Cash Flow margin" as its non-GAAP measures [Q2 2026 release, p.4]; the letter's list adds "total adjusted costs and expenses, non-GAAP operating expense, non-GAAP research and development expense, non-GAAP sales and marketing expense, and non-GAAP general and administrative expense" [Q2 2026 letter, p.15].

### 5.2 Adjusted EBITDA reconciliation (USD thousands) [Q2 2026 release, p.10 Reconciliation of Adjusted EBITDA] (identical [Q2 2026 letter, p.20]); Q1 columns [Q1 2026 release, p.10]

| Line | Q2 2026 | Q2 2025 | 6M 2026 | 6M 2025 | Q1 2026 | Q1 2025 |
|---|---|---|---|---|---|---|
| Net income | 252,848 | 89,297 | 456,829 | 115,455 | 203,981 | 26,158 |
| Interest (income) expense, net | (25,027) | (21,056) | (48,912) | (41,470) | (23,885) | (20,414) |
| Income tax expense (benefit) | 3,987 | (439) | 5,734 | (2,160) | 1,747 | (1,721) |
| Depreciation and amortization | 4,258 | 3,934 | 8,468 | 7,897 | 4,210 | 3,963 |
| Stock-based compensation expense and related taxes | 106,836 | 95,104 | 185,684 | 202,509 | 78,848 | 107,405 |
| Other (income) expense, net | (92) | (91) | 977 | (211) | 1,069 | (120) |
| Adjusted EBITDA | 342,810 | 166,749 | 608,780 | 282,020 | 265,970 | 115,271 |
| Net margin | 31.4% | 17.9% | 31.1% | 12.9% | 30.7% | 6.7% |
| Adjusted EBITDA margin | 42.6% | 33.4% | 41.5% | 31.6% | 40.1% | 29.4% |

- Footing (computed): every column sums to the printed Adjusted EBITDA. Interest (income) of (25,027) plus other (income) of (92) equals the P&L "Other income (expense), net" of 25,119 (Q2 2026); (23,885) + 1,069 = 22,816 (Q1 2026). No "other non-recurring" add-back line appears in any quarter shown.
- Stock-based compensation expense alone (cash flow statement) was 100,952 in Q2 2026 and 89,070 in Q2 2025; 169,288 and 174,484 for six months [Q2 2026 letter, p.19]; 68,336 and 85,414 in Q1 2026 / Q1 2025 [Q1 2026 letter, p.19]. The "related taxes" component is therefore 5,884 in Q2 2026, 6,034 in Q2 2025, 10,512 in Q1 2026 (computed as the difference from the reconciliation line).

### 5.3 Free Cash Flow reconciliation (USD thousands) [Q2 2026 release, p.11 Reconciliation of Free Cash Flow] (identical [Q2 2026 letter, p.21]); Q1 [Q1 2026 release, p.11]

| Line | Q2 2026 | Q2 2025 | 6M 2026 | 6M 2025 | Q1 2026 | Q1 2025 |
|---|---|---|---|---|---|---|
| Net cash provided by (used in) operating activities | 261,876 | 111,331 | 574,129 | 238,909 | 312,253 | 127,578 |
| Less: Purchases of property and equipment | (1,134) | (505) | (2,224) | (1,484) | (1,090) | (979) |
| Free Cash Flow | 260,742 | 110,826 | 571,905 | 237,425 | 311,163 | 126,599 |
| Operating cash flow margin | 32.5% | 22.3% | 39.1% | 26.8% | 47.1% | 32.5% |
| Free Cash Flow margin | 32.4% | 22.2% | 38.9% | 26.6% | 46.9% | 32.3% |

- The only capex line is "Purchases of property and equipment"; there is no capitalized-software or finance-lease line in the cash flow statement [Q2 2026 letter, p.19].
- Working capital: accounts receivable change (127,228) in Q2 2026 vs (81,116) in Q2 2025; Q1 2026 was +67,957 (a source of cash) [Q2 2026 letter, p.19] [Q1 2026 letter, p.19]. Accounts receivable, net 650,098 at June 30, 2026 vs 522,905 at March 31, 2026 and 590,162 at December 31, 2025 [Q2 2026 letter, p.18] [Q1 2026 letter, p.18].

### 5.4 Non-GAAP costs and expenses, SBC and D&A by function (USD thousands) — LETTER-ONLY [Q2 2026 letter, p.22]; Q1 [Q1 2026 letter, p.22]

| Line | Q2 2026 | Q2 2025 | 6M 2026 | 6M 2025 | Q1 2026 | Q1 2025 |
|---|---|---|---|---|---|---|
| Total costs and expenses | 573,189 | 431,916 | 1,053,688 | 820,374 | 480,499 | 388,458 |
| less D&A | 4,258 | 3,934 | 8,468 | 7,897 | 4,210 | 3,963 |
| less SBC and related taxes | 106,836 | 95,104 | 185,684 | 202,509 | 78,848 | 107,405 |
| Total adjusted costs and expenses | 462,095 | 332,878 | 859,536 | 609,968 | 397,441 | 277,090 |
| Total operating expenses | 502,881 | 386,016 | 927,113 | 737,385 | 424,232 | 351,369 |
| less D&A | 4,258 | 3,934 | 8,468 | 7,897 | 4,210 | 3,963 |
| less SBC and related taxes | 106,583 | 94,900 | 185,286 | 202,088 | 78,703 | 107,188 |
| Non-GAAP operating expenses | 392,040 | 287,182 | 733,359 | 527,400 | 341,319 | 240,218 |
| R&D | 231,276 | 196,610 | 438,522 | 387,881 | 207,246 | 191,271 |
| R&D: D&A | 2,645 | 2,510 | 5,284 | 5,050 | 2,639 | 2,540 |
| R&D: SBC and related taxes | 69,098 | 59,629 | 118,770 | 124,816 | 49,672 | 65,187 |
| Non-GAAP R&D | 159,533 | 134,471 | 314,468 | 258,015 | 154,935 | 123,544 |
| S&M | 195,897 | 120,619 | 347,369 | 211,304 | 151,472 | 90,685 |
| S&M: D&A | 1,379 | 1,216 | 2,721 | 2,418 | 1,342 | 1,202 |
| S&M: SBC and related taxes | 13,068 | 11,153 | 20,205 | 25,373 | 7,137 | 14,220 |
| Non-GAAP S&M | 181,450 | 108,250 | 324,443 | 183,513 | 142,993 | 75,263 |
| G&A | 75,708 | 68,787 | 141,222 | 138,200 | 65,514 | 69,413 |
| G&A: D&A | 234 | 208 | 463 | 429 | 229 | 221 |
| G&A: SBC and related taxes | 24,417 | 24,118 | 46,311 | 51,899 | 21,894 | 27,781 |
| Non-GAAP G&A | 51,057 | 44,461 | 94,448 | 85,872 | 43,391 | 41,411 |

- Footing (computed): 69,098 + 13,068 + 24,417 = 106,583 (opex SBC); total SBC and related taxes 106,836 minus opex 106,583 = 253 in cost of revenue (Q2 2026); D&A by function 2,645 + 1,379 + 234 = 4,258 = total D&A, so cost of revenue carries no D&A. All subtotals foot.
- Growth (computed): non-GAAP S&M +67.6% Y/Y (181,450 vs 108,250); non-GAAP R&D +18.6%; non-GAAP G&A +14.8%; non-GAAP opex +36.5% (letter says "up 37%"); total adjusted costs +38.8% (letter chart: 39%).
- Letter captions: "Total GAAP operating expenses were $502.9 million, up 30% year-over-year"; "Total non-GAAP operating expenses were $392.0 million, up 37% year-over-year" [Q2 2026 letter, p.9]. Q1: "Total GAAP operating expenses were $424.2 million, up 21% year-over-year"; "Total non-GAAP operating expenses were $341.3 million, up 42% year-over-year" [Q1 2026 letter, p.9].

### 5.5 Six-quarter expense and profit series from the letter charts (USD millions; Q2'25–Q2'26 bbox-confirmed [Q2 2026 letter, p.9]; Q1 '25 from [Q1 2026 letter, p.9])

| Quarter | GAAP opex | Non-GAAP opex | SBC & related taxes (opex) | D&A | Net income | Adjusted EBITDA |
|---|---|---|---|---|---|---|
| Q1 '25 | $351.4 | $240.2 | $107.2 | $4.0 | $26.2 | $115.3 |
| Q2 '25 | $386.0 | $287.2 | $94.9 | $3.9 | $89.3 | $166.7 |
| Q3 '25 | $393.9 | $296.6 | $93.4 | $3.9 | $162.7 | $236.0 |
| Q4 '25 | $435.1 | $340.1 | $90.8 | $4.2 | $251.6 | $327.0 |
| Q1 '26 | $424.2 | $341.3 | $78.7 | $4.2 | $204.0 | $266.0 |
| Q2 '26 | $502.9 | $392.0 | $106.6 | $4.3 | $252.8 | $342.8 |

- Footing (computed): non-GAAP opex + SBC + D&A = GAAP opex in every quarter (e.g., 392.0 + 106.6 + 4.3 = 502.9; 340.1 + 90.8 + 4.2 = 435.1).
- Q4 '25 mapping note: the flat text places "$327.0" near the net-income labels; bbox x-positions (net income $251.6 at x=1110, Adjusted EBITDA $327.0 at x=1143 in the Q4 '25 column) and the rendered page show net income $251.6M and Adjusted EBITDA $327.0M; consistent with the margin chart (net margin 34.7% = 251.6 / 725.6; Adjusted EBITDA margin 45.1% = 327.0 / 725.6) [Q2 2026 letter, p.10].

### 5.6 Margin, "Rule of 40" and cost-growth series [Q2 2026 letter, p.10] [Q1 2026 letter, p.10]

| Quarter | Revenue Y/Y growth | Adj. EBITDA margin | "Rule of 40" (growth + margin) | Net income margin | Incremental Adj. EBITDA margin Y/Y | Non-GAAP total cost Y/Y growth | Revenue growth / cost growth |
|---|---|---|---|---|---|---|---|
| Q1 '25 | 61% (61.5%) | 29.4% | 91% | 6.7% | 70.4% | 19.0% | 3.2x |
| Q2 '25 | 78% (77.7%) | 33.4% | 111% | 17.9% | 58.3% | 38% (37.7%) | 2.1x |
| Q3 '25 | 68% (67.9%) | 40.3% | 108% | 27.8% | 60.0% | 37% (37.3%) | 1.8x |
| Q4 '25 | 70% (69.7%) | 45.1% | 115% | 34.7% | 58.0% | 46% (45.8%) | 1.5x |
| Q1 '26 | 69% (69.1%) | 40.1% | 109% | 30.7% | 55.6% | 43% (43.4%) | 1.6x |
| Q2 '26 | 61% | 42.6% | 104% | 31.4% | 57.7% | 39% | 1.6x |

- Whole-number values are the Q2 letter's chart labels; one-decimal values in parentheses are the Q1 letter's labels for the same quarters. The Q1 '25 row and the one-decimal growth values were mapped by overlap and arithmetic (61.5 / 19.0 = 3.2; the Q1 letter's "average of 60.5% for the last five quarters" equals the mean of 70.4, 58.3, 60.0, 58.0, 55.6), not by bbox.
- Captions, verbatim: "Revenue growth plus Adjusted EBITDA margin makes us a "Rule of 104" Company, 6,400 bps above "Rule of 40"" ; "Total revenue grew 1.6x times as fast as total adjusted costs and expenses year-over-year"; "57.7% year-over-year incremental Adjusted EBITDA margin" [Q2 2026 letter, p.10]. Q1: ""Rule of 109" Company, 6,900 bps above "Rule of 40""; "55.6% year-over-year incremental Adjusted EBITDA margin, with an average of 60.5% for the last five quarters" [Q1 2026 letter, p.10].
- Check (computed): incremental margin Q2 2026 = (342.8 − 166.7) / (804.9 − 499.6) = 57.7%.

### 5.7 Cash, share count, operating cash flow and SBC series [Q2 2026 letter, p.11] [Q1 2026 letter, p.11]

| Quarter | Cash, equivalents & marketable securities ($B) | Basic shares outstanding (M) | Shares underlying stock-based awards (M) | Fully diluted shares outstanding (M) | Q/Q dilution | Operating cash flow ($M) | OCF % of revenue | SBC & related taxes ($M) | SBC % of revenue |
|---|---|---|---|---|---|---|---|---|---|
| Q1 '25 | $2.0 | 184.3 | 21.7 | 206.0 | (0.1%)* | $127.6 | 32.5% | $107.4 | 27.4% |
| Q2 '25 | $2.1 | 187.1 | 19.5 | 206.6 | 0.3% | $111.3 | 22.3% | $95.1 | 19.0% |
| Q3 '25 | $2.2 | 189.4 | 16.7 | 206.1 | (0.2%) | $185.2 | 31.7% | $93.6 | 16.0% |
| Q4 '25 | $2.5 | 190.9 | 15.2 | 206.1 | 0.0% | $266.8 | 36.8% | $91.1 | 12.6% |
| Q1 '26 | $2.8 | 192.4 | 14.0 | 206.4 | 0.1% | $312.3 | 47.1% | $78.8 | 11.9% |
| Q2 '26 | $2.8 | 192.3 | 14.7 | 207.0 | 0.3% | $261.9 | 32.5% | $106.8 | 13.3% |

- *Q1 '25 dilution value read from the Q1 letter's flat text by elimination (not bbox-verified). Basic + awards = fully diluted in every quarter (computed): 192.3 + 14.7 = 207.0.
- Captions, verbatim [Q2 2026 letter, p.11]: "Cash on balance sheet was $2.8 billion, up 35% from the prior year"; "Fully diluted shares outstanding (FDSO) were 207.0M, up 0.2% y/y and up 0.3% from last quarter"; "Excluding the impact of share repurchases, FDSO were 208.5M, up 0.9% y/y and 1.0% from last quarter"; "Operating cash flow was $262 million, up 135% year-over-year"; "Operating cash flow as % of revenue was 33%, an improvement of 1,020 bps year-over-year"; "Stock-based compensation & related taxes were $106.8 million, up 12% year-over-year"; "SBC as % of revenue was 13%, an improvement of 570 bps year-over-year". Footnote A: "Represents cash and cash equivalents and marketable securities."
- Q1 captions [Q1 2026 letter, p.11]: "Cash on balance sheet was $2.8 billion, up 42% from the prior year"; "Fully diluted shares outstanding were 206.4 million, up 0.2% year-over-year"; "Operating cash flow was $312.3 million, up 145% year-over-year"; "Operating cash flow as % of revenue was 47.1%, an improvement of 1,460 bps year-over-year"; "Stock-based compensation & related taxes taxes were $78.8 million, down 27% year-over-year" (sic, "taxes taxes"); "SBC as % of revenue was 12%, an improvement of 1,550 bps year-over-year".
- Basic shares fell Q/Q for the first time in the series (192.4 to 192.3) while shares underlying awards rose (14.0 to 14.7) (computed observation from the table).

### 5.8 Capital return and balance sheet items

- Repurchases of Class A common stock (cash flow statement): (234,591) in Q2 2026, — in Q2 2025; six months (239,590) vs — [Q2 2026 letter, p.19]; Q1 2026 (4,999) [Q1 2026 letter, p.19]. So Q2 2026 was the first quarter of meaningful buybacks; the release's "$235 million" matches 234,591 (computed check). Average price $157.57 x 1.5M shares ≈ $236M (rounded share count) (computed).
- Remaining authorization: not stated in the Q2 release or letter. (The Q4 2025 results release title in the Q4 Inc. feed reads "Reddit Reports Fourth Quarter and Full Year 2025 Results, Announces $1 Billion Share Repurchase Program", dated 2026-02-05; that document was not fetched by this gatherer; the filings gatherer's `8-K-2026-02-05.txt` covers the announcement.)
- Taxes paid related to net share settlement of RSUs: (14,546) Q2 2026 vs (15,225) Q2 2025; six months (30,742) vs (51,900). Proceeds from option exercises 5,037 vs 4,303. [Q2 2026 letter, p.19]
- Investing: purchases of marketable securities (311,978), maturities 409,247, proceeds from sales — (Q2 2026); net cash from investing 94,714. Financing net (244,100). Net increase in cash 112,490; cash and equivalents end of period 1,486,838. [Q2 2026 letter, p.19]
- Balance sheet (USD thousands, June 30, 2026 vs December 31, 2025) [Q2 2026 letter, p.18]: total current assets 3,541,665 vs 3,135,985; property and equipment, net 11,981 vs 12,710; operating lease ROU assets 18,411 vs 20,788; intangible assets, net 10,565 vs 15,521; goodwill 42,174 vs 42,174; total assets 3,636,605 vs 3,239,173; accounts payable 89,144 vs 62,929; accrued expenses and other current liabilities 240,822 vs 201,331; total current liabilities 337,749 vs 271,283; other noncurrent liabilities 72 vs 22,661; total liabilities 350,905 vs 310,135; additional paid-in capital 3,504,664 vs 3,595,772; accumulated other comprehensive income (loss) (4,695) vs 4,364; accumulated deficit (214,288) vs (671,117); total stockholders' equity 3,285,700 vs 2,929,038.
- Additional paid-in capital fell 91,108 in six months despite 169,288 of SBC (computed), consistent with repurchases and net share settlement being charged to APIC; the release does not say where repurchases are recorded.

## 6. Q2 2026 letter narrative, structured

### 6.1 CEO letter themes (Steve Huffman, Co-Founder & CEO) [Q2 2026 letter, pp.4–5]

- Opening thesis, verbatim: "Q2 reinforced something we believe deeply: as the internet becomes more automated, the value of authentic human conversation continues to rise. We saw that reflected in both our commercial success and early progress of our product roadmap. We delivered our eighth consecutive quarter of over 60% revenue growth, hit an adjusted EBITDA margin of 43%, and crossed a major milestone we've been chasing: $1 million in revenue per employee."
- Advertiser feedback, verbatim: "I heard that clearly at Cannes last month, where we met with many of our customers. Across the board, brands told me they believe in Reddit's distinct ability to connect them with highly engaged, highly intentional audiences. More than that, they are rooting for us to win."
- AI positioning, verbatim: "We are the antidote to an automated web. AI compresses the internet into summaries. Reddit delivers the opposite: deep discussions, passionate debates, and lived experiences. People don't want a summary of Reddit; they want Reddit." "As AI makes information more abundant, the challenge is no longer finding content—it's finding context, personal opinion, and first-hand accounts. ... We've never had more information, but we've never trusted it less. That's why decision-making is shifting from single authorities to groups of real people who have nothing to gain from you purchasing a product. And it's not just purchase decisions—it's health, careers, travel, everything."
- Top priority, verbatim: "Our top priority remains growing our daily active user base by improving the experience for new users so they come back more frequently. Everyone belongs on Reddit because Reddit has content for everyone. We already have a massive base of weekly users, and our focus is on converting them into dailies."
- Product progress, verbatim: "Updated feed models are increasing contribution rates and session frequency, and we're successfully driving more web users to our app, where they are far more engaged. We've made it easier to post on Reddit and find the right community to post in. We've also broadened the product in ways that support growth and engagement—video in comments helps expand our upper funnel, and interactive games on our Developer Platform drive repeat usage and daily habit."
- Retention, verbatim: "On a weekly basis, Reddit now reaches over half a billion people, including more than 130 million daily. In Q2, we improved our user mix and brought more high-quality users to Reddit across the app and site. And new app user retention, an area we've discussed frequently, was up 50% year-over-year on a relative basis this quarter—now, this is coming from a small base, and we have a lot of work ahead of us, but it's an important sign that we're moving in the right direction."
- Search traffic (the explicit statement on Google/search referrals and logged-out volatility), verbatim: "These product efforts, paired with consumer marketing, helped drive daily active users and offset headwinds in users coming from search. Search referrals were choppy in the quarter, and traffic was more volatile later in the quarter, but the bigger picture is unchanged: the commercial business is strong, our revenue growth is differentiated, and we have much to be encouraged by on the product side." And: "While our visibility in referral traffic remains low, we're not building for drive-by traffic. We're building a daily destination." The word "Google" does not appear anywhere in the Q2 letter or release.
- Long-term user goal, verbatim: "Our product work is what will get us to our goal of 1 billion daily users globally and 100 million in the U.S. That work takes time to gain traction, but is what will deepen engagement, strengthen our monetization flywheel, and drive more durable growth."
- Closing, verbatim: "The internet is divided between machines and humans. There is room for both, but we know who we're building for. People will always want to hear from other people: real opinions, expertise, stories, and communities where they can ask, learn, argue, and belong." "Reddit has continued to grow through every major change on the internet because the underlying need has not changed. Human connection is existential, and Reddit is the most human place on the internet. That's why I'm so confident in where we're going."
- Release CEO quote, verbatim [Q2 2026 release, p.1]: ""In an increasingly automated web, the value of real human perspective has never been higher. Reddit's commercial momentum reflects that," said Steve Huffman, Founder and CEO of Reddit. "Crossing $1 million in revenue per employee and maintaining eight consecutive quarters of over 60% revenue growth shows the strength of our community model and the value we deliver to advertisers."" No CFO or COO quote in the release.

### 6.2 Business highlights bullets [Q2 2026 letter, p.3], verbatim where not already quoted

- "Expanded our Shopify integration to general availability, unlocking access for millions of merchants to tap into Reddit's high-intent audiences and drive measurable lower-funnel outcomes"; "Introduced Video in Comments, giving users a new way to connect through richer, more authentic conversations"; "Launched our "People Are the Best" brand marketing campaign, celebrating the people and communities at the heart of Reddit".

### 6.3 Consumer product [Q2 2026 letter, p.7] (page title "Consumer product & experience"; three columns; stats confirmed by visual read)

- Investing in video: "We're investing in video and creating a uniquely Reddit experience that highlights the conversations and communities on Reddit"; "In Q2, we launched video in comments, enabling users to share video replies directly in the comment section, creating richer and more authentic conversations with core video creation tools"; "Looking ahead, we're reimagining how users and communities connect, share, and consume content through a modernized video experience on Reddit". Screenshots captioned "Video in comments".
- Keeping Reddit real, and safe: "Reddit is the most trusted source of authentic human knowledge, built for people and powered by real human perspectives"; "Our "People Are the Best" brand campaign launched in Q2 celebrates the communities that make Reddit unlike anywhere else on the internet"; stat callouts "100k+ Active communites" (sic) and "26B+ Posts & comments"; "We are also investing to keep Reddit human and safe at scale, using AI and community-led moderation to catch and remove spam and coordinated inauthentic behavior"; stat callouts "20% reduction in user exposure to spam" and "23M spam views blocked daily, before they ever reach a human user".
- Converting frequent users into higher-value app Redditors: "We are converting existing, high-intent Reddit users into app users, where we deliver a richer native product experience and monetize more effectively"; "In Q2, we launched app upsells for deep-funnel mobile web users, driving app DAU and downloads"; "We also launched our first desktop login upsell, driving a lift in signups"; callout "Improving conversion efficiency with ML-powered targeting"; screenshots "Mobile web to app download upsell" and "Desktop login upsell".
- Not mentioned in the Q2 letter (present in the Q1 letter): Reddit search / "Reddit Answers", machine translation or a count of translated languages, bot verification tools, the U.K./France country call-outs. The Q2 letter's only search reference is the CEO's referral-traffic paragraph (§6.1). Not disclosed for Q2 in the IR documents.

### 6.4 Advertising and monetization [Q2 2026 letter, p.8] (stats confirmed by visual read)

- Real conversations driving the consumer decision journey: "Real conversations on Reddit are shaping how consumers discover, evaluate, and buy products"; "In Q2, we introduced AI- and Reddit Community Intelligence-powered tools to improve the advertiser experience: Tailored Creative Assets: Identifies high-potential Reddit communities and generates tailored creatives; Free-form Ad Generator: Enables advertisers to append text, GIFs, and videos to ad placements"; "In Q2, we launched Shopping Listing Ads (alpha), our first multi-advertiser ad format that matches products to relevant conversations, helping shoppers discover & compare products in context"; "We also expanded our Shopify integration to general availability, enabling Shopify merchants to start running Reddit Shopping Ad campaigns within minutes". Callouts: "2X+ higher Shopify advertiser activation rate" (footnote A: "Represents % of advertisers spending out of new accounts when compared to standard Ads Manager") and "~50% of US shoppers verify AI recommendations on Reddit before they buy" (footnote B: "Source: Reddit Path to Purchase 2026 Survey, US, n=13,956, A18-65 (Monthly Social Media, LLM, and E-commerce users), Attest Sample, May 2026. All platform rankings statistically significant at a 95% confidence level against Social Platforms (YouTube, Facebook, Instagram, TikTok, Snapchat, X, Pinterest, Discord, LinkedIn) and All Platforms = Social Platforms, LLMs (ChatGPT, Gemini, Claude, Microsoft Copilot) and Amazon.").
- ML-driven performance across the ad stack: "We're investing in machine learning ("ML") across our ads platform to drive performance and deliver more outcomes for advertisers"; "Upper funnel: Enhanced models increased six-second Engaged Video View-through and completion rates by 130% and 71%, respectively"; "Middle funnel: Better models are leading to improvements in CTR and delivering more valuable clicks. Click through rates are up over 40% year-over-year"; "Lower funnel: ML investments and optimizations are driving significant performance gains in our App Install campaigns".
- Lower funnel updates (table): "Reddit Max campaigns — Growing adoption, driving revenue: 60%+ advertiser growth vs. Q1; 150%+ revenue growth vs. Q1". "App Event Optimization — Made generally available: 22% lower Cost Per Action; 100%+ growth in app install volume". (Both comparisons are sequential vs Q1 2026, not year-over-year; no base figures given.)
- Case study: Wise: "Wise launched an App Event Optimization campaign via Reddit Max campaigns to streamline creative generation and Call to Action combinations that would deliver against its most valuable KPIs"; results "8% Lower cost per install" and "7% More app sign up events"; quote: ""The intuitive setup and automated features of Reddit's Max campaigns have really simplified how we manage the platform. We can now focus on broader strategy rather than daily manual tweaks to creative and copy. We're excited to move Max into our permanent US strategy and start testing its impact in other regions."" (speaker not named).
- Third-party validation: "Reddit delivers strong performance and high LTV customers for its advertisers, as validated by third-party research"; "Over 2x incremental ROAS from performance outcomes for retail advertisers" (footnote C: "When compared to the North American media plan average. Transunion (formerly Neustar) MTA findings across 24 brands/112 outcome metrics."); "7x avg. ROAS for retail advertisers in EMEA" (footnote D: "Reddit-commissioned custom Retail MMM Meta Analysis Q1'23-Q4'25 conducted by TransUnion. Date range: January 2023 to December 2025. Sample. Blinded MMMs within the Retail industry that contain Reddit, Other Paid Social Media, Digital Display, TV, Online Video, Paid Search, and other digital and traditional channels."); "Reddit shoppers generate higher post acquisition value across CPG categories" (footnote E: "Based on Attain's Census Balanced Transaction Panel; Customer Lifetime Value metrics conducted in partnership with Attain and Theta. Date: March 2026.").
- Not disclosed in the Q2 release or letter: number of active advertisers, advertiser count growth (other than "60%+ advertiser growth vs. Q1" for Reddit Max campaigns specifically), revenue mix between performance and brand advertising, SMB / mid-market share of revenue, vertical mix, impression and price growth rates (only "growth in pricing and impressions" qualitatively), ad load, Reddit Max share of revenue.

### 6.5 International

- Quantitative only: International DAUq 77.1M (+28%), International WAUq 317.4M (+35%), International revenue $166.8M (+84%), International ARPU $2.26 (+31%), International logged-out DAUq +41% and logged-in +12% [Q2 2026 release, p.6]. No translation-market count, no country call-outs, no international product commentary in the Q2 letter (contrast Q1, §7). Wise is described as testing Max "in other regions" [Q2 2026 letter, p.8].

### 6.6 AI, data licensing and "other revenue"

- AI appears as (a) the CEO's "antidote to an automated web" framing (§6.1), (b) AI-powered advertiser tools and ML across the ad stack (§6.4), (c) "using AI and community-led moderation to catch and remove spam" (§6.3), and (d) the "~50% of US shoppers verify AI recommendations on Reddit before they buy" survey stat (§6.4). [Q2 2026 letter, pp.4, 7, 8]
- Data licensing / AI content agreements: no mention in the Q2 letter or release. "Other revenue" is stated only as $43M, +24% [Q2 2026 release, p.1]. Not disclosed.

### 6.7 Hiring, expenses, efficiency

- Page title, verbatim: "Reddit is scaling efficiently and crossed the $1M Revenue Per Head milestone" [Q2 2026 letter, p.6]. Chart "REVENUE, OPERATING EXPENSES, AND NON-GAAP OPERATING EXPENSES PER HEADCOUNT (IN THOUSANDS)", quarters Q2 '25 – Q2 '26 (bbox- and visually confirmed): Revenue / headcount $735, $808, $904, $986, $1,077; GAAP operating expenses / headcount $611, $626, $643, $654, $681; non-GAAP operating expenses / headcount $436, $452, $478, $504, $531. Footnote A, verbatim: "Revenue / headcount calculated as sum of last four quarters revenue divided by average of last four quarters headcount. GAAP operating expenses / headcount and non-GAAP operating expenses / headcount calculated as sum of last four quarters GAAP and non-GAAP operating expenses, respectively, divided by average of last four quarters headcount."
- No hiring-plan, headcount-growth or expense-outlook statement appears in the Q2 letter or release. Expense facts are the chart captions in §5.4 to §5.7 (GAAP opex +30%, non-GAAP opex +37%, SBC +12%, SBC 13% of revenue).
- Cost of revenue rose 53% Y/Y (70,308 vs 45,900) and 25% Q/Q (vs 56,267) (computed) [Q2 2026 letter, p.17] [Q1 2026 letter, p.17]; no explanation is given in the IR documents.

### 6.8 Corporate / disclosure

- Regulation FD channels, verbatim [Q2 2026 release, p.3]: "Reddit uses the investor relations page on its website https://investor.redditinc.com, user accounts of Reddit's Chief Executive Officer, Steve Huffman (u/spez); Reddit's Chief Operating Officer, Jen Wong (u/adsjunkie); and Reddit's Chief Financial Officer, Drew Vollero (u/TimingandLuck), as well as the subreddits r/RDDT and r/reddit ... as means of disclosing material non-public information".
- Community Q&A: "Reddit will solicit questions from the community in the investor relations subreddit, r/RDDT, ... on Thursday, July 30, 2026, after the market closes, and post responses following the earnings call" [Q2 2026 release, p.3]. The Q4 Inc. feed lists the resulting "r/RDDT AMA Post" and "r/RDDT Numbers Recap Post" on reddit.com; both returned HTTP 403 (Cloudflare) to this gatherer and were not cached.
- Signatories of the letter: Steve Huffman, Co-Founder & Chief Executive Officer; Drew Vollero, Chief Financial Officer [Q2 2026 letter, p.13].
- About Reddit boilerplate now says "With 26+ billion posts and comments and more than 130 million daily active uniques" [Q2 2026 release, p.3]; Q1 said "25+ billion posts and comments and more than 126 million daily active uniques" [Q1 2026 release, p.3].

## 7. Q1 2026 letter (prior quarter), in brief: what management had said

### 7.1 Business highlights [Q1 2026 letter, p.3]

- DAUq averaged 126.8M (+17%); WAUq 493.1M (+23%); logged-in +7%, logged-out +26%; U.S. DAUq +7%, International +26%; U.S. revenue +67%, International +76%; advertising $625M (+74%), other $39M (+15%); "Broad strength across the full ad funnel and our top-15 industry verticals"; "Announced integration with Shopify to scale our advertiser ecosystem and streamline customer onboarding".
- Financial highlights [Q1 2026 letter, p.2]: revenue $663M (+69%); gross margin 91.5% (up 100 bps); net income $204M, 31% margin; Adjusted EBITDA $266M, 40% margin; operating cash flow $312M; FCF $311M; EPS $1.07 basic / $1.01 diluted ("up over 650%"); capex $1M (0.2% of revenue); cash $2.77B; FDSO 206.4M (+0.2%). No repurchase mentioned in the Q1 highlights (cash flow shows $4,999K repurchased) [Q1 2026 letter, p.19].

### 7.2 CEO letter themes [Q1 2026 letter, pp.4–5]

- "Reddit is truly a one-of-one company"; "This marks our seventh consecutive quarter with revenue growth over 60%, with industry-leading gross margins over 90%, an Adjusted EBITDA margin of 40%, and record cash flow of more than $300 million. At the same time, our capital expenditures remained low at just $1 million, underscoring the advantage of Reddit's capital-light model."
- "Around 40% of conversations on Reddit are commercial in nature, where people are actively discussing products, services, and purchase decisions. And these conversations are uniquely influential: 84% of shoppers say they feel more confident in their decisions after researching on Reddit." (Footnote A: Attest survey, U.S., n=1,004, February 2026.)
- AI / data: "Reddit is built on more than two decades of human conversation—over 25 billion posts and comments—and every month our communities generate the equivalent of Wikipedia's entire content library in new content." "As AI becomes more prevalent, people increasingly seek out real human perspectives, and in turn, AI models rely on these perspectives to train and power their products. Scarce assets tend to become more valuable over time, and authentic human conversation at scale is becoming increasingly rare. Reddit's conversations are like oil for the modern internet: a foundational resource powering the next generation of technology."
- Users: "On the user side, we're making steady progress, but we still have work to do to increase frequency and accelerate growth toward the levels we see on leading platforms." "We already have tremendous reach today with nearly 500 million weekly users globally and 200 million in the United States. Now it's about driving both greater reach and greater frequency." "Our goal is to reach 100 million daily U.S. users, and we're actively executing a strategy to get us there."
- Organization: "One thing that has become clear is that product quality leads to growth. I believe our previous ways of working yielded the best results we were capable of, but not the results we aspired to. So to get to the next level, we first had to improve ourselves." "We've strengthened our teams with more people who've successfully grown other major platforms. We've added critical machine learning talent ... And we've improved our processes for data, experiments, and shipping more quickly while still improving quality".
- Forward priorities (the only forward-looking operating statement beyond the guidance table), verbatim: "We made advancements across several product areas this quarter that we're encouraged by, including bot verification, improvements in core user engagement, performance gains across the stack, and continued success with machine translation. Looking ahead to the remainder of 2026, our priorities include broadening the top of the funnel, improving new user retention, and making Reddit faster across the board, which remains a meaningful opportunity and can lead to an outsized impact."
- Release CEO quote [Q1 2026 release, p.1]: ""Reddit is a one-of-one business powered by deeply engaged communities and authentic human conversation," said Steve Huffman, Founder and CEO of Reddit. "That foundation is driving a rare combination of growth, profitability, and efficiency, and giving Reddit a unique advantage in the age of AI.""

### 7.3 "1 of 1 Financial Model" page [Q1 2026 letter, p.6]

- "Out of 300+ Publicly Listed U.S. Tech Companies, including: Alphabet, Meta, Microsoft, Netflix, NVIDIA, etc. only 21 companies have >40% 2025 Revenue Growth; 5 have >30% 2025 Free Cash Flow and Adj. EBITDA Margins; 3 have <$15M 2025 CapEx; 1 has >90% 2025 Gross Margin. Reddit is a 1 of 1 Company." Source: "FactSet, market data as of 01-Apr-2026." This page has no Q2 equivalent (replaced by the revenue-per-headcount page).

### 7.4 Consumer product & internationalization [Q1 2026 letter, p.7] (visual read)

- Modernizing search: "Reddit search enables community discovery, surfaces authentic human perspectives, and informs high-intent decisions"; "AI-powered search results and product integrations improve the search experience, accelerating usage and utility"; screenshot caption "Product placements enable searchers to browse listings and shop directly within the Reddit search results". (The term "Reddit Answers" does not appear in either letter.)
- Scaling internationally: "Reddit's content is translated into over 30 languages and optimized to deliver high-quality and locally relevant content to users across the world"; "Reddit is one of the most visited sites in the U.K. and is especially popular with women, who represent more than half of Reddit's users in the U.K."; "Reddit is gaining influence in France, with brands and media outlets integrating the platform to uncover local trends, topics, and culture"; press quotes: "Three in five Brits now encounter the site while online, up from one-third in 2023." (FC) and "Reddit is undergoing a transformation in France. The conversational platform [...] is influencing brands, media outlets, recruiters and AI engines." (Influencia).
- Authentically human: "With over 25 billion posts and comments, Reddit is the internet's largest collection of community-driven conversation"; "We're leading the industry with verification and bot labeling tools"; captions "Testing fast and secure verification protocols" and "Automated bot labeling"; callout "25B+ Posts and comments on the platform".

### 7.5 Advertising & monetization [Q1 2026 letter, p.8] (visual read)

- Scaling automation with Reddit Max campaigns: "Middle Market and SMBs are increasingly adopting Reddit Max campaigns to optimize their lower funnel objectives"; "Max campaigns unlock performance and deliver AI-powered insights to measure performance across audiences"; "Advertisers see 17% lower costs / CPA* and over 25%* more conversions with Max campaigns" (*"Based on 17 split tests conducted between June and August 2025. Each test compared Max campaigns to standard campaigns over a 21-day period. CPA refers to Cost per Action."); callout "~50% of Max campaign advertisers use AI-powered creative features to unlock greater performance".
- Shopping ads momentum: "84% of Reddit shoppers feel more secure in their purchases after researching products on the platform"; "We have strong adoption with our Dynamic Product Ads (DPA), bringing Reddit-unique content into the shopping journey"; callouts "40% Y/Y increase in high-intent shopping conversations on Reddit" (footnote B: "Reddit Insights powered by Community Intelligence, Global, 2024 vs 2025; posts with CI score >0.8 inside the "shopping" entity") and "91% Y/Y DPA ROAS improvement from signal and ML investments"; "We announced an integration with Shopify to simplify catalog and measurement setup and enable frictionless onboarding for new DPA advertisers".
- Case study Liquid I.V., quote: ""Since launching Reddit DPA in April 2025, we've seen a transformative shift in our lower-funnel efficiency for Liquid I.V." said Karilyn Anderson, VP of Media and Retention at Liquid I.V. "Despite being a newer placement for us, DPA has already generated 33% of our total platform revenue. Most impressively, it is outperforming our other conversion campaigns by 40%, all while maintaining engagement levels on par with our top-tier prospecting efforts.""
- Case study Cozey: "By launching Reddit Max campaigns, Cozey leveraged automated bidding, creative rotation, and audience expansion to scale new customer acquisition with less hands-on management"; results "27-28% Lower costs (CPA and CPM)*" and "35% Higher ROAS*" (*"When compared to Cozey's standard campaigns.").

### 7.6 AMA highlights [Q1 2026 letter, p.13]

- "In Q1, Reddit supported 70+ AMAs across more than 50 communities." Two example AMAs (identified only by images): "Impressions: over 2.5m; Upvotes: over 10k; Comments: over 2.5k" and "Impressions: over 1m; Upvotes: over 5.5k; Comments: over 1.5k". No Q2 equivalent page.

### 7.7 What carried through from Q1 to Q2 (side-by-side, no interpretation)

| Topic | Q1 2026 letter said | Q2 2026 letter says |
|---|---|---|
| Shopify | "Announced integration with Shopify" (p.3, p.8) | "Expanded our Shopify integration to general availability" (p.3, p.8); "2X+ higher Shopify advertiser activation rate" (p.8) |
| Reddit Max campaigns | Middle Market and SMBs "increasingly adopting"; 17% lower CPA, 25%+ more conversions; ~50% use AI creative (p.8) | "60%+ advertiser growth vs. Q1; 150%+ revenue growth vs. Q1" (p.8); Wise case study |
| Shopping ads | DPA momentum; 91% Y/Y DPA ROAS improvement (p.8) | "Shopping Listing Ads (alpha), our first multi-advertiser ad format" (p.8) |
| Search | "AI-powered search results and product integrations improve the search experience" (p.7) | "Search referrals were choppy in the quarter, and traffic was more volatile later in the quarter" (p.5) |
| U.S. daily user goal | "Our goal is to reach 100 million daily U.S. users" (p.5) | "our goal of 1 billion daily users globally and 100 million in the U.S." (p.5) |
| 2026 priorities | "broadening the top of the funnel, improving new user retention, and making Reddit faster" (p.5) | "new app user retention ... was up 50% year-over-year on a relative basis ... coming from a small base" (p.5); "video in comments helps expand our upper funnel" (p.5) |
| Machine translation / international product | "translated into over 30 languages"; U.K. and France (p.7) | no international product commentary |
| Bot verification | "bot verification", "verification and bot labeling tools" (p.5, p.7) | "using AI and community-led moderation to catch and remove spam and coordinated inauthentic behavior"; 20% reduction in spam exposure; 23M spam views blocked daily (p.7) |
| Efficiency framing | "1 of 1" FactSet comparison (p.6) | "$1M Revenue Per Head milestone" (p.6) |
| Capital return | not mentioned in highlights; $5.0M repurchased (p.19) | 1.5M shares, $235M, $157.57 average (p.2); FDSO ex-repurchases 208.5M (p.11) |

## 8. Release/letter-only figures (not expected in the 10-Q; flag for the writer)

- Release/letter-only figure: WAUq (global, U.S., international) and its growth rates [Q2 2026 release, p.6].
- Release/letter-only figure: logged-in vs logged-out DAUq by geography [Q2 2026 release, p.6].
- Release/letter-only figure: ARPU by geography [Q2 2026 release, p.6].
- Letter-only figure: five-quarter chart series for DAUq/WAUq by geography, revenue by geography, gross margin, opex composition, net income / Adjusted EBITDA, ARPU, Rule of 40, cost-growth ratio, margin trends, cash, FDSO, OCF, SBC [Q2 2026 letter, pp.3, 9, 10, 11].
- Letter-only figure: revenue, GAAP opex and non-GAAP opex per headcount (TTM basis) [Q2 2026 letter, p.6].
- Letter-only figure: fully diluted shares outstanding 207.0M; FDSO excluding repurchases 208.5M; shares underlying stock-based awards 14.7M; Q/Q dilution [Q2 2026 letter, pp.2, 11].
- Letter-only figure: non-GAAP cost reconciliation, SBC and D&A by function [Q2 2026 letter, p.22].
- Letter-only figures: Reddit Max "60%+ advertiser growth vs. Q1" and "150%+ revenue growth vs. Q1"; App Event Optimization "22% lower Cost Per Action", "100%+ growth in app install volume"; CTR "up over 40% year-over-year"; six-second video view-through and completion rates "+130% and 71%"; Shopify "2X+" activation; "~50% of US shoppers verify AI recommendations on Reddit before they buy"; "Over 2x incremental ROAS", "7x avg. ROAS ... EMEA"; "20% reduction in user exposure to spam"; "23M spam views blocked daily"; "100k+ Active communities"; "26B+ Posts & comments"; new app user retention "up 50% year-over-year on a relative basis" [Q2 2026 letter, pp.5, 7, 8].
- Letter-only figures (Q1): "over 30 languages"; "Around 40% of conversations on Reddit are commercial in nature"; "84% of shoppers"; Max campaigns 17% lower CPA / 25%+ more conversions / ~50% use AI creative; 40% Y/Y increase in high-intent shopping conversations; 91% Y/Y DPA ROAS improvement; Liquid I.V. 33% / 40%; Cozey 27-28% / 35%; FactSet "1 of 1" counts; 70+ AMAs across 50+ communities [Q1 2026 letter, pp.4, 6, 7, 8, 13].
- Release-only text: Regulation FD disclosure channels (executive Reddit accounts u/spez, u/adsjunkie, u/TimingandLuck) [Q2 2026 release, p.3].

## 9. Data quality notes

- Both letters are Canva-generated landscape PDFs with real text layers; no page is image-only for data. Product/marketing pages (Q2 pp.7–8; Q1 pp.7–8) mix text with screenshots whose embedded text is not extractable and is not data.
- `pdftotext -layout` scrambles chart data labels (e.g., p.9 lists "$342.8 / $327.0 / $266.0 / $251.6 / $252.8 ... $236.0 / $204.0 / $166.7 $162.7 / $89.3" in reading order that does not follow the bars). All quarter mappings above were fixed with `pdftotext -bbox` x-coordinates and a visual read; in particular Q4 '25 net income is $251.6M and Adjusted EBITDA $327.0M.
- Two-column prose pages (pp.4–5 of each letter) interleave columns line-by-line under `-layout`; `shareholder-letter-reading-order.txt` gives p.4 cleanly but p.5 still interleaves paragraph blocks of the two columns. The quotes in §6.1 were assembled from both copies and checked against the rendered page.
- Footnotes on Q2 letter p.8 are set in very small type; the layout text merges footnote fragments with the footer ("Q2 2026 • Letter to Shareholders B. Source: Reddit Path to Purchase 2026 Survey ..."). Footnote text in §6.4 was reassembled from the fragments; the letter order is A, B (bottom-left) and C, D, E (bottom-right).
- Company typos: Q2 letter p.13 footer reads "Q1 2026 • Letter to Shareholders 13"; Q2 letter p.7 "Active communites"; Q1 letter p.11 "related taxes taxes". Q2 letter p.9 axis label "Q3'25" lacks the space used elsewhere.
- Curly quotes (" " ') and en-dashes are used throughout the letters and the release exhibits; ASCII greps for quotes or hyphens will miss them.
- Rounding: release Financial Highlights table shows Q2 2025 revenue as $500 (exact 499,627) and Q2 2025 Free Cash Flow as $111 (exact 110,826); the Q1 2026 ad + other split sums to $664M vs $663M total. The letter's "Net income ... improvement of $164 million" is 252.8 − 89.3 = 163.5 rounded (computed).
- ARPU x DAUq by region does not reproduce the geographic revenue lines (see §2.5); the definitions differ in allocation basis.
- Six-month KPI averages are not given (the KPI table's six-month columns cover revenue only) [Q2 2026 release, p.6].
- Neither release contains a cash-flow-statement-level capex breakdown beyond one line, a headcount figure, a remaining-authorization figure for buybacks, or any FX commentary.
- The Q2 letter's p.16 KPI table and the release p.6 table are identical in every value (checked cell by cell).

## 10. Not disclosed in the release or letter (for the writer)

- Headcount; number of advertisers; performance vs brand revenue mix; impressions and pricing growth rates; ad load; data-licensing revenue, customers or renewals; Reddit Answers / search product metrics; translated-language count for Q2; country-level user or revenue data; remaining buyback authorization; full-year 2026 outlook; DAUq or margin guidance; FX impact; capex guidance; any definition of logged-in vs logged-out.

## 11. Automated numeric check

- Run 2026-09-08 after writing: every numeric token in this file (excluding source tags, page references, quarter labels, years, dates, times, section numbers and file-size/coordinate metadata) was tested for a verbatim match in the five cached text files. Result: tokens checked 1373; matched 1313; misses on computed/implied lines 52; unlabelled misses 8. The remaining unlabelled misses are metadata only (PDF page size 1440x810 pt, exhibit number 99.2, five bbox x-coordinates in the chart-extraction note, HTTP status 403); every derived figure sits on a line labelled "computed" or "implied".
