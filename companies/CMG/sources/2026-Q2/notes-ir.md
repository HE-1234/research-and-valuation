# Chipotle Mexican Grill (CMG) — Q2 2026 IR gatherer notes: earnings releases (Q2 2026, Q1 2026, Q4/FY2025), supplemental investor decks (Q2 2026, Q1 2026, Q4/FY2025), Q2 2026 non-GAAP tables PDF, 2026-07-13 Mexico release

- Quarter: Q2 2026 (quarter ended June 30, 2026). Fiscal year = calendar year. Company: Chipotle Mexican Grill, Inc., NYSE: CMG, CIK 0001058090. The company reports in USD thousands except per-share data.
- As-of cutoff: 2026-07-31 (10-Q filed 2026-07-31; earnings release and call 2026-07-29, call at 4:30 PM Eastern). The Q2 2026 release is datelined "NEWPORT BEACH, Calif. – July 29, 2026" and was filed as Exhibit 99.1 to the 8-K accepted by EDGAR on 2026-07-29 (accession 0001058090-26-000063, Items 2.02, 8.01, 9.01). The Q1 2026 release is datelined April 29, 2026 (8-K accession 0001058090-26-000027). The Q4/FY2025 release is datelined February 3, 2026 (8-K accession 0001058090-26-000007, accepted 2026-02-03 16:10:45, Items 2.02 and 9.01). The Q2 2026 deck PDF was created 2026-07-29 15:26 UTC, the Q1 2026 deck 2026-04-28 21:16 UTC, the Q4/FY2025 deck 2026-02-03 01:23 UTC, the Q2 2026 non-GAAP tables PDF 2026-07-29 16:09 UTC. Nothing published after 2026-07-31 was fetched, read or used.
- Cached text and how each was produced (origin URLs, fetch log and verification in `MANIFEST-ir.md`):
  - `press-release.txt` — Q2 2026 earnings release, EDGAR HTML (8-K EX-99.1) stripped to text with table cells joined by " | ".
  - `press-release-2026-Q1.txt` — Q1 2026 earnings release, same conversion.
  - `press-release-2025-Q4.txt` — Q4 and full-year 2025 earnings release, same conversion (fetched this run).
  - `slides.txt` — Q2 2026 "Investor Information" deck, `pdftotext -layout` of the 15-page PDF.
  - `slides-2026-Q1.txt` — Q1 2026 deck, same conversion, 15 pages.
  - `slides-2025-Q4.txt` — Q4/FY2025 deck, same conversion, 20 pages (fetched this run; cached because it carries the 2019–2025 series and FY2025 unit economics that the 2026 decks do not).
  - `non-gaap-tables.txt` — "Non-GAAP tables for IR Site Q226", `pdftotext -layout` of the 5-page PDF; the text version of the reconciliations that are images in the Q2 2026 deck.
  - `press-release-2026-07-13-mexico.txt` — IR news release of 2026-07-13, body text only.
- Tags. The EDGAR HTML releases have no printed page numbers, so release tags cite the section heading: `[Q2 2026 release, <section>]` = press-release.txt; `[Q1 2026 release, <section>]` = press-release-2026-Q1.txt; `[Q4 2025 release, <section>]` = press-release-2025-Q4.txt. Section names used: Headline (the bullets under "Second quarter highlights" etc.), CEO quote, Results (the narrative paragraphs), Outlook, Definitions, About Chipotle, Forward-Looking Statements, Statements of Income, Balance Sheets, Statements of Cash Flows, Supplemental Financial and Other Data (unit table), Non-GAAP definitions, Adjusted Net Income reconciliation, Adjusted Labor reconciliation (Q1 only), Adjusted G&A reconciliation, Adjusted Effective Income Tax Rate reconciliation, Restaurant Level Operating Margin reconciliation. Deck tags use the printed page number (bottom-right of each slide): `[Q2 2026 slides, p.N]` = slides.txt; `[Q1 2026 slides, p.N]` = slides-2026-Q1.txt; `[Q4 2025 slides, p.N]` = slides-2025-Q4.txt (cover pages and section dividers carry no printed number; they are pages 1, 8 and 11 of the 2026 decks and 1, 11 and 17 of the Q4 deck). `[Q2 2026 non-GAAP tables, p.N]` = non-gaap-tables.txt, PDF page. `[IR release 2026-07-13 (Mexico)]` = press-release-2026-07-13-mexico.txt.
- Units: dollars in thousands in every statement and reconciliation table (the releases print "(in thousands, except per share data)"); the narrative rounds to millions or billions and those roundings are quoted as printed; shares in thousands; percentages as printed. All figures unaudited. Every number is copied verbatim; anything derived by the gatherer is labelled "(computed)"; anything read from a slide image rather than the text layer is labelled "(from slide image p.N, visual read)" or "... OCR".
- Table-shape note: in the EDGAR HTML the "$" sign and the "%" sign sit in their own cells, so rows read e.g. `Food and beverage revenue | $ | 3,332,792 | 99.5 | % | $ | 3,047,754 | 99.5 | %`, and negative comps print as `(2.5 | %)`. Column order is preserved in every table. In the income statements the "Percent of total revenue" column is printed only for the first and last rows with a "%" cell; the other rows carry the percentage without a sign.
- Source text quirks left as-is in the cache: curly apostrophes and quotes throughout the releases ("Chipotle’s", “Recipe for Growth”); the Q2 deck's forward-looking page says "expended levels of comparable restaurant sales" (source typo for "expected"); the Q4 deck's footer text extracts with spaced letters ("Q4/ FY 202 5 Investor Information", "MEXIC AN GRILL"); "1000+ restaurants" (no comma) on Q2 slide p.6; "Adjusted diluted earnings1 per share" (footnote marker mid-phrase) in the Q4 release headline bullets.
- What the three decks are: 15 or 20 landscape slides, mostly text and photographs. Neither 2026 deck contains any KPI chart (no comps, AUV, margin, unit-count or digital-mix chart); their only data pages are the one-page "Highlights" table (p.9) and the three image-only reconciliation pages (pp.13–15), whose numbers equal the release tables (verified by OCR, see §8). The Q4/FY2025 deck has the series pages (p.5 track record 2019–2025, p.13 unit economics, p.14 restaurant and Chipotlane counts by year, p.15 capital allocation) and its chart data labels are in the PDF text layer. Page-by-page map in `MANIFEST-ir.md`.

## 1. Headline results

### 1.1 Q2 2026 (three months ended June 30, 2026) vs Q2 2025

- Release title and sub-heads, verbatim: "CHIPOTLE RAISES FULL YEAR COMPARABLE SALES GUIDANCE ON STRONG Q2 MOMENTUM"; "\"RECIPE FOR GROWTH\" STRATEGY YIELDS COMPARABLE RESTAURANT SALES OF 2.2% ON SECOND CONSECUTIVE QUARTER OF IMPROVING TRANSACTION COMP". [Q2 2026 release, Headline]
- "Second quarter highlights, year over year", verbatim: "Total revenue increased 9.3% to $3.3 billion"; "Comparable restaurant sales increased 2.2%"; "Operating margin was 15.7%, a decrease from 18.2%"; "Restaurant level operating margin1 was 25.2%, a decrease from 27.4%"; "Diluted earnings per share remained flat at $0.32"; "Adjusted diluted earnings per share1 remained flat at $0.33"; "Opened 100 company-owned restaurants, with 80 locations including a Chipotlane. We also opened one international partner-operated restaurant." [Q2 2026 release, Headline]
- CEO quote, verbatim: "“Our positive results reflect the momentum we're building as our Recipe for Growth strategy continues to take shape,” said Scott Boatwright, Chief Executive Officer, Chipotle. “We're seeing encouraging progress because we're focused on the right growth drivers—bringing meaningful menu innovation to our guests, deepening engagement through Chipotle Rewards, elevating hospitality in every restaurant, and expanding opportunities to serve more group occasions. These efforts are building a stronger business and reinforcing our confidence in Chipotle's ability to deliver sustainable long-term growth and shareholder value.”" [Q2 2026 release, CEO quote]
- Revenue and comps narrative, verbatim: "Total revenue in the second quarter of 2026 was $3.3 billion, an increase of 9.3% compared to the second quarter of 2025. The increase was driven by new restaurant openings and, to a lesser extent, comparable restaurant sales. Comparable restaurant sales increased 2.2%, consisting of a 1.2% increase in average check and a 1.0% increase in transactions. Digital sales represented 38.3% of total food and beverage revenue for the three months ended June 30, 2026, an increase from 35.5% for the three months ended June 30, 2025." [Q2 2026 release, Results]
- Openings, verbatim: "During the second quarter we opened 100 company-owned restaurants, of which 80 included a Chipotlane, and one international partner-operated restaurant. Chipotlanes continue to perform well and are helping enhance guest access and convenience, as well as increase new restaurant sales, margins and returns." [Q2 2026 release, Results] Chipotlane share of company-owned openings = 80 / 100 = 80% (computed).
- Net income and adjusted net income, verbatim: "Net income for the second quarter of 2026 was $403.5 million, or $0.32 per diluted share, compared to $436.1 million, or $0.32 per diluted share, in the second quarter of 2025. Adjusted net income1 for the second quarter of 2026 was $418.9 million, or $0.33 per adjusted diluted share, compared to $450.4 million, or $0.33 per adjusted diluted share, in the second quarter of 2025." [Q2 2026 release, Results]
- Buybacks, verbatim: "During the second quarter of 2026 we repurchased $630.7 million of stock at an average price per share of $32.55. As of June 30, 2026, $1.7 billion remained available under share repurchase authorizations from our Board of Directors, including an additional $1.3 billion in authorizations approved by our Board of Directors on June 11, 2026. The repurchase authorization may be modified, suspended or discontinued at any time." [Q2 2026 release, Results] The number of shares repurchased is not stated in the release (see §7).
- Restaurant count at quarter end: the unit table gives 4,186 company-owned restaurants and 15 partner-operated restaurants at Jun. 30, 2026 [Q2 2026 release, Supplemental Financial and Other Data]; total 4,201 (computed). "About Chipotle", verbatim: "There are over 4,200 restaurants as of June 30, 2026, in the United States, Canada, the United Kingdom, France, Germany, and the Middle East and it is the only restaurant company of its size that owns and operates all its restaurants in the United States, Canada and Europe. With nearly 140,000 employees passionate about providing a great guest experience, Chipotle is a longtime leader and innovator in the food industry." [Q2 2026 release, About Chipotle] (The Q1 2026 and Q4 2025 releases worded the ownership claim "all its restaurants in North America and Europe"; the Q2 2026 release changed it to "in the United States, Canada and Europe". [Q1 2026 release, About Chipotle] [Q4 2025 release, About Chipotle])
- Restaurant level operating margin in Q2 2026 is NOT labelled "adjusted" and has no adjustment line: income from operations 525,595 (15.7%) plus G&A 190,471, D&A 98,327, pre-opening 16,364 and impairment/closure/disposals 13,808 = restaurant level operating margin 844,565, 25.2% (Q2 2025: 838,230, 27.4%). [Q2 2026 release, Restaurant Level Operating Margin reconciliation] The Q2 legal reserve ($10,000 thousand) was recognized in general and administrative expenses [Q2 2026 release, Adjusted Net Income reconciliation, footnote 4], and G&A is outside restaurant level operating margin by definition ("revenues generated by our restaurants less direct restaurant operating costs, which consist of food, beverage and packaging, labor, occupancy and other operating costs") [Q2 2026 release, Non-GAAP definitions].

Q2 2026 deck highlights table (matches the release). [Q2 2026 slides, p.9]

| Line | Q2 2026 |
|---|---|
| Revenue | $3.3B |
| Sales Growth | 9.3% |
| Comparable Restaurant Sales | 2.2% |
| New Restaurant Openings (Company-Owned) | 100 |
| Restaurant Level Operating Margin (non-GAAP) | 25.2% |
| Operating Margin | 15.7% |
| Share Repurchases | $631M |
| Non-GAAP Diluted EPS | $0.33 |

- Deck narrative, verbatim: "Recipe for Growth Gaining Traction". "Delivered Strong Q2 Results — Delivered revenue growth of 9.3%, comparable sales growth of 2.2%, and another quarter of positive transaction growth, supported by marketing, menu innovation, Rewards engagement, and hospitality initiatives." "Executing “Recipe for Growth” — Strategy continues to gain traction, with progress across restaurant execution, digital engagement, menu innovation, new occasions, people development, and global expansion." "Improving Restaurant Performance — HEEP is improving food quality, throughput, and guest satisfaction, translating into hundreds of basis points of comparable sales improvement. Deployed in more than 1,000 restaurants today, with approximately 2,000 planned by year-end." "Deepening Digital & Rewards Engagement — Rewards relaunch, Summer of Extras, and new in-restaurant enrollment tools are increasing engagement, with in-store loyalty comp sales outpacing order-ahead loyalty comp sales since mid-April." "Increasing FY26 Outlook — Although the industry and consumer backdrop remains mixed, we are confident we can build on our momentum and are increasing our full-year comparable sales outlook to the low-single-digit range." [Q2 2026 slides, p.9] (HEEP = High Efficiency Equipment Package, spelled out on [Q2 2026 slides, p.6].)

### 1.2 Q1 2026 (three months ended March 31, 2026) vs Q1 2025

- Release title and sub-head, verbatim: "CHIPOTLE ANNOUNCES FIRST QUARTER 2026 RESULTS"; "RETURN TO POSITIVE TRANSACTIONS DRIVES 0.5% COMPARABLE RESTAURANT SALES GROWTH; REVENUE INCREASES 7.4% TO $3.1 BILLION". [Q1 2026 release, Headline]
- "First quarter highlights, year over year", verbatim: "Total revenue increased 7.4% to $3.1 billion"; "Comparable restaurant sales increased 0.5%"; "Operating margin was 12.9%, a decrease from 16.7%"; "Adjusted restaurant level operating margin1 was 23.7%, a decrease from 26.2%"; "Diluted earnings per share was $0.23, a 17.9% decrease from $0.28"; "Adjusted diluted earnings per share1 was $0.24, a 17.2% decrease from $0.29"; "Opened 49 company-owned restaurants, with 42 locations including a Chipotlane." [Q1 2026 release, Headline]
- CEO quote, verbatim: "“Our first quarter exceeded expectations as we advanced our Recipe for Growth strategy, delivering tangible progress across operations, digital, menu innovation, people, and development,” said Scott Boatwright, Chief Executive Officer, Chipotle. “We are excited to welcome a new Chief Brand Officer and a new Chief Digital Officer to further strengthen our value proposition, sharpen our brand messaging, and accelerate innovation—positioning Chipotle for sustained, long-term growth as we advance on our path to becoming a global iconic brand.”" [Q1 2026 release, CEO quote]
- Revenue and comps narrative, verbatim: "Total revenue in the first quarter of 2026 was $3.1 billion, an increase of 7.4% compared to the first quarter of 2025. The increase was driven by new restaurant openings and, to a lesser extent, a 0.5% increase in comparable restaurant sales due to higher transactions of 0.6%, partially offset by a 0.1% decrease in average check. Digital sales represented 38.6% of total food and beverage revenue." [Q1 2026 release, Results] The Q1 2026 release gives no prior-year digital-sales percentage.
- Openings, verbatim: "During the first quarter we opened 49 company-owned restaurants, of which 42 included a Chipotlane." No partner-operated openings in the quarter (unit table shows "-" for Opened, total 14). [Q1 2026 release, Results] [Q1 2026 release, Supplemental Financial and Other Data]
- Net income, verbatim: "Net income for the first quarter of 2026 was $302.8 million, or $0.23 per diluted share, compared to $386.6 million, or $0.28 per diluted share, in the first quarter of 2025. Adjusted net income1 for the first quarter of 2026 was $316.2 million, or $0.24 per adjusted diluted share, compared to $396.8 million, or $0.29 per adjusted diluted share, in the first quarter of 2025." [Q1 2026 release, Results]
- Buybacks, verbatim: "During the first quarter of 2026 we repurchased $700.8 million of stock at an average price per share of $36.14. As of March 31, 2026, $1.0 billion remained available under share repurchase authorizations from our Board of Directors." [Q1 2026 release, Results]
- Restaurant count: 4,090 company-owned and 14 partner-operated at Mar. 31, 2026 [Q1 2026 release, Supplemental Financial and Other Data]; total 4,104 (computed). "There are over 4,100 restaurants as of March 31, 2026 ... With over 135,000 employees". [Q1 2026 release, About Chipotle]
- Why Q1's restaurant level operating margin is "adjusted", verbatim: "Excluding a 40 basis point impact from costs related to certain legal proceedings, adjusted labor costs1 were 25.7% of total revenue, compared to 25.0% in the first quarter of 2025." [Q1 2026 release, Results] "Adjusted restaurant level operating margin is equal to the restaurant level operating margin excluding certain legal proceedings, expressed as a percent of total revenue." [Q1 2026 release, Non-GAAP definitions] The adjustment is "Legal proceedings-Labor (1) | 11,875 | 0.4", footnote "(1)Estimated liability recognized in labor on the condensed consolidated statements of income for legal matters that we expect to exceed typical costs for legal proceedings." Unadjusted restaurant level operating margin was 718,961, 23.3%; adjusted 730,836, 23.7%; Q1 2025 753,622, 26.2% (no adjustment). [Q1 2026 release, Restaurant Level Operating Margin reconciliation]

Q1 2026 deck highlights table. [Q1 2026 slides, p.9]

| Line | Q1 2026 |
|---|---|
| Revenue | $3.1B |
| Sales Growth | 7.4% |
| Comparable Restaurant Sales | 0.5% |
| New Restaurant Openings (Company-Owned) | 49 |
| Adjusted Restaurant Level Operating Margin | 23.7%* ("* Adjusted for legal proceedings") |
| Operating Margin | 12.9% |
| Share Repurchases | $700M |
| Non-GAAP Diluted EPS | $0.24 |

- Deck narrative, verbatim: "Accelerating Momentum & Delivering Results". "Q1 Performance Shows Early Traction, Exceeding Expectations — Delivered a double beat on comps and margins, with a return to positive transaction growth — early proof “Recipe for Growth” is working." "Executing “Recipe for Growth” — Strategy is firmly in execution mode, with progress across operations, digital, menu innovation, and people — boosting engagement and re-engaging younger and value-focused guests." "Driving Productivity & Engagement through Innovation — HEEP is improving prep and the guest experience, delivering meaningful throughput gains and comp outperformance. Deployed in over 600 U.S. restaurants today, with 2,000 planned by year-end." "Launching Rewards on Repeat — Entering the next phase of digital growth with a redesigned rewards experience that gives customers more flexibility while driving deeper engagement." "Maintaining FY26 Outlook — Maintaining a prudent outlook amid macro uncertainty, while managing costs transparently. Confident in our ability to execute and adapt." [Q1 2026 slides, p.9]

### 1.3 Q4 2025 and full-year 2025 (from the Q4 2025 release)

- Release title and sub-heads, verbatim: "CHIPOTLE ANNOUNCES FOURTH QUARTER AND FULL YEAR 2025 RESULTS"; "LAUNCHES “RECIPE FOR GROWTH” STRATEGY TO GROW TRANSACTIONS AND DRIVE ACCURACY, EFFICIENCY AND SPEED"; "FULL YEAR TOTAL REVENUE INCREASED 5.4% TO $11.9 BILLION". [Q4 2025 release, Headline]
- "Fourth quarter highlights, year over year", verbatim: "Total revenue increased 4.9% to $3.0 billion"; "Comparable restaurant sales decreased 2.5%"; "Operating margin was 14.1%, a decrease from 14.6%"; "Restaurant level operating margin1 was 23.4%, a decrease from 24.8%"; "Diluted earnings per share was $0.25, a 4.2% increase from $0.24"; "Adjusted diluted earnings per share1 remained flat at $0.25"; "Opened 132 company-owned restaurants, with 97 locations including a Chipotlane, and seven international partner-operated restaurants". [Q4 2025 release, Headline]
- "Full year 2025 highlights, year over year", verbatim: "Total revenue increased 5.4% to $11.9 billion"; "Comparable restaurant sales decreased 1.7%"; "Operating margin was 16.2%, a decrease from 16.9%"; "Restaurant level operating margin1 was 25.4%, a decrease from 26.7%"; "Diluted earnings per share was $1.14, a 2.7% increase from $1.11"; "Adjusted diluted earnings1 per share was $1.17, a 4.5% increase from $1.12"; "Opened 334 company-owned restaurants, with 257 locations including a Chipotlane, and 11 international partner-operated restaurants". [Q4 2025 release, Headline]
- CEO quote, verbatim: ""Through our proven business model, prudent investments in operational excellence and the support of a strong balance sheet, 2025 was a year of progress and resilience for Chipotle. Against a dynamic consumer backdrop, we opened a record number of restaurants globally and grew Q4 and full year revenue," said Scott Boatwright, Chief Executive Officer, Chipotle. "This momentum will fuel our next phase of growth, driven by our 'Recipe for Growth' strategy which leans into what uniquely differentiates our brand to accelerate transactions and expand our footprint globally."" [Q4 2025 release, CEO quote]
- Second CEO quote (strategy section), verbatim: "“Our 'Recipe for Growth' strategy should position us for success over the long-term by growing transactions and driving accuracy, efficiency and speed. We are deploying these initiatives and beginning to see results, including the early success of our high-protein menu and benefits from our high-efficiency equipment package," said Boatwright. "At the center of our strategy is the strength and relevance of our brand and our unwavering commitment to sourcing the best ingredients. We are confident in the opportunity ahead and our ability to delight guests and deliver value for shareholders.”" [Q4 2025 release, "Recipe for Growth" Strategy]
- Q4 revenue and comps, verbatim: "Total revenue in the fourth quarter of 2025 was $3.0 billion, an increase of 4.9% compared to the fourth quarter of 2024. The increase in total revenue was driven by new restaurant openings and gift card breakage revenue of $27.0 million, which represented a $19.1 million increase compared to the fourth quarter of 2024. Gift card breakage revenue does not impact comparable restaurant sales. These increases were partially offset by a 2.5% decrease in comparable restaurant sales due to lower transactions of 3.2%, partially offset by a 0.7% increase in average check. Digital sales represented 37.2% of total food and beverage revenue." [Q4 2025 release, Results (Q4)]
- FY2025 revenue and comps, verbatim: "Total revenue for 2025 was $11.9 billion, an increase of 5.4% compared to 2024. The increase in total revenue was primarily driven by new restaurant openings. The increase was partially offset by a 1.7% decrease in comparable restaurant sales due to lower transactions of 2.9%, partially offset by a 1.2% increase in average check. Digital sales represented 36.7% of total food and beverage revenue." [Q4 2025 release, Results (full year)]
- Year-end count, verbatim: "As of December 31, 2025, there were a total of 4,056 Chipotle restaurants including 14 international partner-operated restaurants. During 2025, we opened 334 company-owned restaurants, of which 257 included a Chipotlane, and 11 international partner-operated restaurants." [Q4 2025 release, Results (full year)] Company-owned at Dec. 31, 2025 = 4,042 [Q4 2025 release, Supplemental Financial and Other Data]. "There are over 4,000 restaurants as of December 31, 2025 ... With over 130,000 employees". [Q4 2025 release, About Chipotle]
- Q4 net income, verbatim: "Net income for the fourth quarter of 2025 was $330.9 million, or $0.25 per diluted share, compared to $331.8 million, or $0.24 per diluted share, in the fourth quarter of 2024. Adjusted net income1 for the fourth quarter of 2025 was $331.3 million, or $0.25 per adjusted diluted share, compared to $340.0 million, or $0.25 per adjusted diluted share, in the fourth quarter of 2024." [Q4 2025 release, Results (Q4)]
- FY2025 net income, verbatim: "Net income for 2025 was $1.54 billion, or $1.14 per diluted share, compared to $1.53 billion, or $1.11 per diluted share, in 2024. Adjusted net income1 for 2025 was $1.57 billion, or $1.17 per adjusted diluted share, compared to $1.54 billion, or $1.12 per adjusted diluted share, in 2024." [Q4 2025 release, Results (full year)]
- Buybacks, verbatim: "During the fourth quarter of 2025 we repurchased $741.6 million of stock at an average price per share of $34.14. As of December 31, 2025, $1.7 billion remained available under share repurchase authorizations from our Board of Directors." "During 2025, we repurchased $2.4 billion of stock at an average price per share of $42.54." [Q4 2025 release, Results]

Q4/FY2025 deck highlights table. [Q4 2025 slides, p.12]

| Line | Q4 2025 | FY 2025 |
|---|---|---|
| Revenue | $3.0B | $11.9B |
| Sales Growth | 4.9% | 5.4% |
| Comparable Restaurant Sales | (2.5%) | (1.7%) |
| New Restaurant Openings (Company-Owned) | 132 | 334 |
| Restaurant Level Operating Margin | 23.4% | 25.4% |
| Adjusted Diluted EPS | $0.25 | $1.17 |

### 1.4 Seven-quarter KPI series from the three releases' unit tables

Company-owned restaurant unit data, "(dollars in thousands)". Columns are quarters ended on the date shown. Dec. 31, 2024 through Dec. 31, 2025 from [Q4 2025 release, Supplemental Financial and Other Data]; Mar. 31, 2026 from [Q1 2026 release, Supplemental Financial and Other Data]; Jun. 30, 2026 from [Q2 2026 release, Supplemental Financial and Other Data]. Overlapping quarters print identical values in all three releases.

| | Dec. 31, 2024 | Mar. 31, 2025 | Jun. 30, 2025 | Sep. 30, 2025 | Dec. 31, 2025 | Mar. 31, 2026 | Jun. 30, 2026 |
|---|---|---|---|---|---|---|---|
| Opened | 119 | 57 | 61 | 84 | 132 | 49 | 100 |
| Permanent closures | (2) | (2) | (2) | (4) | (5) | (1) | (3) |
| Relocations | (6) | - | (1) | (3) | (1) | - | (1) |
| Total (company-owned, end of quarter) | 3,726 | 3,781 | 3,839 | 3,916 | 4,042 | 4,090 | 4,186 |
| Average restaurant sales ($ thousands, trailing 12 months) | 3,213 | 3,186 | 3,142 | 3,132 | 3,104 | 3,094 | 3,102 |
| Comparable restaurant sales increase/(decrease) | 5.4% | (0.4%) | (4.0%) | 0.3% | (2.5%) | 0.5% | 2.2% |

Partner-operated restaurant unit data (same sources and columns).

| | Dec. 31, 2024 | Mar. 31, 2025 | Jun. 30, 2025 | Sep. 30, 2025 | Dec. 31, 2025 | Mar. 31, 2026 | Jun. 30, 2026 |
|---|---|---|---|---|---|---|---|
| Opened | 1 | 2 | - | 2 | 7 | - | 1 |
| Total | 3 | 5 | 5 | 7 | 14 | 14 | 15 |

[Q4 2025 release, Supplemental Financial and Other Data] [Q1 2026 release, Supplemental Financial and Other Data] [Q2 2026 release, Supplemental Financial and Other Data]

- Comps split (transactions / average check) as stated in the narratives: Q2 2026 +2.2% = transactions +1.0%, average check +1.2% [Q2 2026 release, Results]; Q1 2026 +0.5% = transactions +0.6%, average check −0.1% [Q1 2026 release, Results]; Q4 2025 −2.5% = transactions −3.2%, average check +0.7% [Q4 2025 release, Results (Q4)]; FY2025 −1.7% = transactions −2.9%, average check +1.2% [Q4 2025 release, Results (full year)].
- Digital sales as % of food and beverage revenue: Q2 2026 38.3% (Q2 2025 35.5%) [Q2 2026 release, Results]; Q1 2026 38.6% (no prior-year figure given) [Q1 2026 release, Results]; Q4 2025 37.2%; FY2025 36.7% [Q4 2025 release, Results].
- Openings and Chipotlanes: Q2 2026 100 company-owned, 80 with Chipotlane, 1 partner-operated [Q2 2026 release, Headline]; Q1 2026 49 company-owned, 42 with Chipotlane [Q1 2026 release, Headline]; Q4 2025 132 company-owned, 97 with Chipotlane, 7 partner-operated; FY2025 334 company-owned, 257 with Chipotlane, 11 partner-operated [Q4 2025 release, Headline]. H1 2026 company-owned openings = 100 + 49 = 149, Chipotlanes 80 + 42 = 122 (computed).
- Employees: "over 130,000" at Dec. 31, 2025 [Q4 2025 release, About Chipotle]; "over 135,000" at Mar. 31, 2026 [Q1 2026 release, About Chipotle]; "nearly 140,000" at Jun. 30, 2026 [Q2 2026 release, About Chipotle]; the decks print "130,000+ employees", "135,000+ employees", "~140,000 employees" on their "At a glance" panels [Q4 2025 slides, p.4] [Q1 2026 slides, p.4] [Q2 2026 slides, p.4].

### 1.5 Cash, investments and buybacks

Cash and investments from the balance sheets ($ thousands). [Q2 2026 release, Balance Sheets] [Q1 2026 release, Balance Sheets] [Q4 2025 release, Balance Sheets]

| Line | Jun. 30, 2026 | Mar. 31, 2026 | Dec. 31, 2025 | Dec. 31, 2024 |
|---|---|---|---|---|
| Cash and cash equivalents | 228,199 | 246,636 | 350,545 | 748,537 |
| Investments (current) | 449,658 | 624,786 | 698,591 | 674,378 |
| Long-term investments | 97,079 | 96,397 | 197,123 | 868,025 |
| Restricted cash | 35,554 | 35,662 | 35,364 | 29,842 |
| Sum of the four lines (computed) | 810,490 | 1,003,481 | 1,281,623 | 2,320,782 |

- The Q4 deck states "Cash, Cash Equivalents, Restricted Cash and Investments of $1.3 BILLION* and no debt", "*As of December 31, 2025." [Q4 2025 slides, p.15] (consistent with the sum of 1,281,623 in the table above (computed)). Neither 2026 deck repeats a cash figure; the 2026 releases give only the balance-sheet lines. No debt line appears on any of the three balance sheets (liabilities are payables, accruals, unearned revenue, operating lease liabilities, deferred taxes and other). [Q2 2026 release, Balance Sheets]

Share repurchases as stated in the releases and decks.

| Period | Dollars | Average price per share | Remaining authorization at period end | Source |
|---|---|---|---|---|
| Q4 2025 | $741.6 million | $34.14 | $1.7 billion at Dec. 31, 2025 | [Q4 2025 release, Results (Q4)]; deck: "$742 MILLION ... $34.14 during Q4’25" [Q4 2025 slides, p.15] |
| FY2025 | $2.4 billion | $42.54 | — | [Q4 2025 release, Results (full year)]; deck: "Totaling a record $2.4 BILLION for the full year 2025" [Q4 2025 slides, p.15] |
| Q1 2026 | $700.8 million | $36.14 | $1.0 billion at Mar. 31, 2026 | [Q1 2026 release, Results]; deck "$700M" [Q1 2026 slides, p.9] |
| Q2 2026 | $630.7 million | $32.55 | $1.7 billion at Jun. 30, 2026, "including an additional $1.3 billion in authorizations approved by our Board of Directors on June 11, 2026" | [Q2 2026 release, Results]; deck "$631M" [Q2 2026 slides, p.9] |

- H1 2026 buybacks = 700.8 + 630.7 = $1,331.5 million (computed); the cash flow statement shows "Repurchase of common stock | (1,354,905)" for the six months (cash basis) [Q2 2026 release, Statements of Cash Flows]. Shares issued fell from 1,304,360 thousand at Dec. 31, 2025 to 1,287,050 thousand at Mar. 31, 2026 and 1,267,838 thousand at Jun. 30, 2026 [Q4 2025 release, Balance Sheets] [Q1 2026 release, Balance Sheets] [Q2 2026 release, Balance Sheets]; the balance-sheet caption reads "Common stock, $0.01 par value, 11,500,000 shares authorized, 1,267,838 and 1,304,360 shares issued as of June 30, 2026 and December 31, 2025, respectively" [Q2 2026 release, Balance Sheets]. Retained earnings went from 619,908 at Dec. 31, 2025 to "Retained earnings/(accumulated deficit) | (67,164)" at Jun. 30, 2026 [Q2 2026 release, Balance Sheets].
- Track record, verbatim: "SHAREHOLDER RETURNS VIA BUYBACKS — Bought back $5.5B Since 2019". [Q4 2025 slides, p.5]

## 2. Income statement and cost lines

### 2.1 Condensed consolidated statements of income ($ thousands, except per share; percent of total revenue as printed)

Q2 2026 vs Q2 2025 and H1 2026 vs H1 2025. [Q2 2026 release, Statements of Income]

| Line | Q2 2026 | % | Q2 2025 | % | H1 2026 | % | H1 2025 | % |
|---|---|---|---|---|---|---|---|---|
| Food and beverage revenue | 3,332,792 | 99.5 | 3,047,754 | 99.5 | 6,405,522 | 99.5 | 5,907,585 | 99.5 |
| Delivery service revenue | 15,770 | 0.5 | 15,639 | 0.5 | 31,282 | 0.5 | 31,061 | 0.5 |
| Total revenue | 3,348,562 | 100.0 | 3,063,393 | 100.0 | 6,436,804 | 100.0 | 5,938,646 | 100.0 |
| Food, beverage and packaging | 993,573 | 29.7 | 885,989 | 28.9 | 1,906,919 | 29.6 | 1,724,392 | 29.0 |
| Labor | 836,450 | 25.0 | 756,261 | 24.7 | 1,641,861 | 25.5 | 1,474,487 | 24.8 |
| Occupancy | 174,210 | 5.2 | 154,250 | 5.0 | 344,091 | 5.3 | 304,091 | 5.1 |
| Other operating costs | 499,764 | 14.9 | 428,663 | 14.0 | 980,407 | 15.2 | 843,824 | 14.2 |
| General and administrative expenses | 190,471 | 5.7 | 172,151 | 5.6 | 394,191 | 6.1 | 344,934 | 5.8 |
| Depreciation and amortization | 98,327 | 2.9 | 90,945 | 3.0 | 195,045 | 3.0 | 178,156 | 3.0 |
| Pre-opening costs | 16,364 | 0.5 | 10,610 | 0.3 | 28,005 | 0.4 | 18,820 | 0.3 |
| Impairment, closure costs, and asset disposals | 13,808 | 0.4 | 5,467 | 0.2 | 23,627 | 0.4 | 11,635 | 0.2 |
| Total operating expenses | 2,822,967 | 84.3 | 2,504,336 | 81.8 | 5,514,146 | 85.7 | 4,900,339 | 82.5 |
| Income from operations | 525,595 | 15.7 | 559,057 | 18.2 | 922,658 | 14.3 | 1,038,307 | 17.5 |
| Interest and other income, net | 7,677 | 0.2 | 18,355 | 0.6 | 16,419 | 0.3 | 40,608 | 0.7 |
| Income before income taxes | 533,272 | 15.9 | 577,412 | 18.8 | 939,077 | 14.6 | 1,078,915 | 18.2 |
| Provision for income taxes | 129,725 | 3.9 | 141,285 | 4.6 | 232,706 | 3.6 | 256,189 | 4.3 |
| Net income | 403,547 | 12.1 | 436,127 | 14.2 | 706,371 | 11.0 | 822,726 | 13.9 |
| EPS basic | $0.32 | | $0.32 | | $0.55 | | $0.61 | |
| EPS diluted | $0.32 | | $0.32 | | $0.55 | | $0.61 | |
| Weighted-average shares, basic (thousands) | 1,277,363 | | 1,344,955 | | 1,287,792 | | 1,349,737 | |
| Weighted-average shares, diluted (thousands) | 1,279,064 | | 1,350,236 | | 1,290,462 | | 1,355,478 | |

Q1 2026 vs Q1 2025. [Q1 2026 release, Statements of Income]

| Line | Q1 2026 | % | Q1 2025 | % |
|---|---|---|---|---|
| Food and beverage revenue | 3,072,730 | 99.5 | 2,859,831 | 99.5 |
| Delivery service revenue | 15,512 | 0.5 | 15,422 | 0.5 |
| Total revenue | 3,088,242 | 100.0 | 2,875,253 | 100.0 |
| Food, beverage and packaging | 913,346 | 29.6 | 838,403 | 29.2 |
| Labor | 805,411 | 26.1 | 718,226 | 25.0 |
| Occupancy | 169,881 | 5.5 | 149,841 | 5.2 |
| Other operating costs | 480,643 | 15.6 | 415,161 | 14.4 |
| General and administrative expenses | 203,720 | 6.6 | 172,783 | 6.0 |
| Depreciation and amortization | 96,718 | 3.1 | 87,211 | 3.0 |
| Pre-opening costs | 11,641 | 0.4 | 8,210 | 0.3 |
| Impairment, closure costs, and asset disposals | 9,819 | 0.3 | 6,168 | 0.2 |
| Total operating expenses | 2,691,179 | 87.1 | 2,396,003 | 83.3 |
| Income from operations | 397,063 | 12.9 | 479,250 | 16.7 |
| Interest and other income, net | 8,742 | 0.3 | 22,253 | 0.8 |
| Income before income taxes | 405,805 | 13.1 | 501,503 | 17.4 |
| Provision for income taxes | 102,981 | 3.3 | 114,904 | 4.0 |
| Net income | 302,824 | 9.8 | 386,599 | 13.4 |
| EPS basic | $0.23 | | $0.29 | |
| EPS diluted | $0.23 | | $0.28 | |
| Weighted-average shares, basic (thousands) | 1,298,220 | | 1,354,518 | |
| Weighted-average shares, diluted (thousands) | 1,301,859 | | 1,360,719 | |

Q4 2025 vs Q4 2024 and FY2025 vs FY2024. [Q4 2025 release, Statements of Income]

| Line | Q4 2025 | % | Q4 2024 | % | FY2025 | % | FY2024 | % |
|---|---|---|---|---|---|---|---|---|
| Food and beverage revenue | 2,969,211 | 99.5 | 2,829,988 | 99.5 | 11,866,051 | 99.5 | 11,247,384 | 99.4 |
| Delivery service revenue | 14,300 | 0.5 | 15,322 | 0.5 | 59,550 | 0.5 | 66,469 | 0.6 |
| Total revenue | 2,983,511 | 100.0 | 2,845,310 | 100.0 | 11,925,601 | 100.0 | 11,313,853 | 100.0 |
| Food, beverage and packaging | 900,155 | 30.2 | 866,252 | 30.4 | 3,526,992 | 29.6 | 3,374,516 | 29.8 |
| Labor | 760,524 | 25.5 | 716,865 | 25.2 | 2,991,680 | 25.1 | 2,789,789 | 24.7 |
| Occupancy | 162,493 | 5.4 | 146,442 | 5.1 | 624,898 | 5.2 | 563,374 | 5.0 |
| Other operating costs | 461,567 | 15.5 | 411,490 | 14.5 | 1,755,824 | 14.7 | 1,568,482 | 13.9 |
| General and administrative expenses | 160,341 | 5.4 | 191,216 | 6.7 | 652,017 | 5.5 | 697,483 | 6.2 |
| Depreciation and amortization | 92,702 | 3.1 | 83,876 | 2.9 | 361,382 | 3.0 | 335,030 | 3.0 |
| Pre-opening costs | 16,946 | 0.6 | 12,905 | 0.5 | 49,507 | 0.4 | 41,897 | 0.4 |
| Impairment, closure costs, and asset disposals | 8,464 | 0.3 | 532 | - | 27,503 | 0.2 | 26,949 | 0.2 |
| Total operating expenses | 2,563,192 | 85.9 | 2,429,578 | 85.4 | 9,989,803 | 83.8 | 9,397,520 | 83.1 |
| Income from operations | 420,319 | 14.1 | 415,732 | 14.6 | 1,935,798 | 16.2 | 1,916,333 | 16.9 |
| Interest and other income, net | 13,324 | 0.4 | 23,365 | 0.8 | 73,721 | 0.6 | 93,897 | 0.8 |
| Income before income taxes | 433,643 | 14.5 | 439,097 | 15.4 | 2,009,519 | 16.9 | 2,010,230 | 17.8 |
| Provision for income taxes | 102,711 | 3.4 | 107,333 | 3.8 | 473,758 | 4.0 | 476,120 | 4.2 |
| Net income | 330,932 | 11.1 | 331,764 | 11.7 | 1,535,761 | 12.9 | 1,534,110 | 13.6 |
| EPS basic | $0.25 | | $0.24 | | $1.15 | | $1.12 | |
| EPS diluted | $0.25 | | $0.24 | | $1.14 | | $1.11 | |
| Weighted-average shares, basic (thousands) | 1,314,871 | | 1,361,358 | | 1,337,336 | | 1,368,343 | |
| Weighted-average shares, diluted (thousands) | 1,319,988 | | 1,368,923 | | 1,342,616 | | 1,376,555 | |

- Year-over-year revenue growth check (computed): Q2 2026 3,348,562 / 3,063,393 − 1 = 9.3%; Q1 2026 3,088,242 / 2,875,253 − 1 = 7.4%; H1 2026 6,436,804 / 5,938,646 − 1 = 8.4%; Q4 2025 2,983,511 / 2,845,310 − 1 = 4.9%; FY2025 11,925,601 / 11,313,853 − 1 = 5.4%. Sum of the four restaurant operating cost lines as % of revenue (computed): Q2 2026 29.7 + 25.0 + 5.2 + 14.9 = 74.8 (restaurant level operating margin 25.2); Q2 2025 28.9 + 24.7 + 5.0 + 14.0 = 72.6 (27.4).

### 2.2 Stated drivers for each cost line, verbatim

Q2 2026 [Q2 2026 release, Results]:
- Food, beverage and packaging: "Food, beverage and packaging costs in the second quarter of 2026 were 29.7% of total revenue, an increase from 28.9% in the second quarter of 2025. The increase was driven by inflation, primarily from beef and freight, and higher protein and produce usage. These increases were partially offset by the benefit of menu price increases and lower avocado and dairy costs."
- Labor: "Labor costs in the second quarter of 2026 were 25.0% of total revenue, an increase from 24.7% in the second quarter of 2025. The increase was primarily driven by higher employee compensation, including wage inflation and performance-based bonuses, and additional restaurant labor supporting operational execution, including hospitality initiatives. These headwinds were partially offset by the benefit from menu price increases."
- G&A: "General and administrative expenses for the second quarter of 2026 were $190.5 million, compared to $172.2 million in the second quarter of 2025. The increase was driven by legal reserves, performance bonuses, wages, and restructuring costs, partially offset by lower stock-based compensation. Adjusted general and administrative expenses1 for the second quarter of 2026 were $176.2 million, compared to $159.9 million in the second quarter of 2025."
- Tax: "The effective income tax rate for the second quarter of 2026 was 24.3%, a decrease from 24.5% in the second quarter of 2025. The decrease was primarily due to an increase in U.S. federal income tax credits, partially offset by lower tax benefits from stock option exercises and equity vesting."
- Occupancy, other operating costs, depreciation, pre-opening and impairment: no narrative in the Q2 2026 release; only the statement lines above. Nothing in the release mentions tariffs, portion sizes or marketing timing for Q2 2026 (tariffs appear only in the risk-factor boilerplate: "increases in ingredient and other operating costs due to inflation, global conflicts, severe weather, our Food with Integrity philosophy, tariffs, or trade restrictions"). [Q2 2026 release, Forward-Looking Statements]

Q1 2026 [Q1 2026 release, Results]:
- Food, beverage and packaging: "Food, beverage and packaging costs in the first quarter of 2026 were 29.6% of total revenue, an increase from 29.2% in the first quarter of 2025. The increase was driven by inflation, primarily in beef and freight, and higher produce usage. These increases were partially offset by lower dairy and avocado costs, and the benefit of menu price increases."
- Labor: "Labor costs in the first quarter of 2026 were 26.1% of total revenue, an increase from 25.0% in the first quarter of 2025. The increase was primarily driven by wage inflation, lower average restaurant sales volumes, and higher benefits expense, including performance-based bonuses. These headwinds were partially offset by the benefit of menu price increases. Excluding a 40 basis point impact from costs related to certain legal proceedings, adjusted labor costs1 were 25.7% of total revenue, compared to 25.0% in the first quarter of 2025."
- G&A: "General and administrative expenses for the first quarter of 2026 were $203.7 million, compared to $172.8 million in the first quarter of 2025. The increase was driven by our biennial All Managers Conference held in the first quarter of 2026, performance bonuses and wages, and benefited from lower stock-based compensation. Adjusted general and administrative expenses1 for the first quarter of 2026 were $197.9 million, compared to $160.9 million in the first quarter of 2025."
- Tax: "The effective income tax rate for the first quarter of 2026 was 25.4%, an increase from 22.9% in the first quarter of 2025. The increase was driven by a reduction in tax benefits related to option exercises and equity vesting, fewer tax credits, and an increase in other discrete income tax items."

Q4 2025 and FY2025 [Q4 2025 release, Results]:
- Food, beverage and packaging, Q4: "Food, beverage and packaging costs in the fourth quarter of 2025 were 30.2% of total revenue, a decrease from 30.4% in the fourth quarter of 2024. The decrease was primarily due to the benefit of menu price increases, lower dairy costs, and cost of sales efficiencies. These decreases were partially offset by inflation, primarily in beef and chicken, and the impact from tariffs enacted in 2025." FY: "Food, beverage and packaging costs for 2025 were 29.6% of total revenue, a decrease from 29.8% in 2024. The decrease was due to the benefit of menu price increases and, to a lesser extent, cost of sales efficiencies. These decreases were partially offset by inflation, primarily in beef and chicken, and the tariffs enacted in 2025."
- Labor, Q4: "Labor costs in the fourth quarter of 2025 were 25.5% of total revenue, an increase from 25.2% in the fourth quarter of 2024. The increase was primarily due to lower sales volumes and wage inflation, partially offset by the benefit from menu price increases and higher bonuses in the prior year." FY: "Labor costs for 2025 were 25.1% of total revenue, an increase from 24.7% in 2024. The increase was primarily due to lower sales volumes and wage inflation, partially offset by the benefit from menu price increases."
- G&A, Q4: "General and administrative expenses for the fourth quarter of 2025 were $160.3 million, compared to $191.2 million in the fourth quarter of 2024. The decrease was primarily due to lower stock-based compensation, performance bonuses and legal reserves. On a non-GAAP basis, general and administrative expenses1 for the fourth quarter of 2025 were $162.1 million, compared to $174.9 million in the fourth quarter of 2024." FY: "General and administrative expenses for 2025 were $652.0 million, compared to $697.5 million for 2024. The decrease was primarily due to lower performance bonuses and legal reserves. On a non-GAAP basis, general and administrative expenses1 for 2025 were $621.6 million compared to $686.8 million for 2024."
- Tax, Q4: "The effective income tax rate for the fourth quarter of 2025 was 23.7%, a decrease from 24.4% in the fourth quarter of 2024. The decrease was primarily driven by increases in U.S. federal income tax credits." FY: "The effective income tax rate for 2025 was 23.6%, a decrease from 23.7% in 2024. The decrease was primarily due to increases in U.S. federal income tax credits and a reduction in nondeductible expenses. These decreases were partially offset with a reduction in excess tax benefits related to option exercises and equity vesting."
- Gift card breakage (Q4 only): "gift card breakage revenue of $27.0 million, which represented a $19.1 million increase compared to the fourth quarter of 2024. Gift card breakage revenue does not impact comparable restaurant sales." [Q4 2025 release, Results (Q4)]

### 2.3 Cash flow and capex ($ thousands)

| Line | H1 2026 | H1 2025 | Q1 2026 | Q1 2025 | FY2025 | FY2024 |
|---|---|---|---|---|---|---|
| Net cash provided by operating activities | 1,332,003 | 1,118,402 | 651,350 | 557,075 | 2,113,926 | 2,105,076 |
| Purchases of leasehold improvements, property and equipment | (397,601) | (305,395) | (180,332) | (144,810) | (666,336) | (593,603) |
| Purchases of investments | (5,520) | (6,500) | (250) | (4,000) | (28,222) | (986,673) |
| Maturities of investments | 349,766 | 319,962 | 172,509 | 154,889 | 659,476 | 722,637 |
| Repurchase of common stock | (1,354,905) | (997,055) | (701,027) | (553,796) | (2,425,516) | (1,001,559) |
| Tax withholding on stock-based compensation awards | (49,397) | (33,319) | (47,997) | (32,902) | (49,458) | (74,229) |
| Stock-based compensation expense (operating add-back) | 54,518 | 75,150 | 28,000 | 37,601 | 119,543 | 131,730 |
| Depreciation and amortization | 195,045 | 178,156 | 96,718 | 87,211 | 361,382 | 335,030 |
| Income taxes paid | 82,670 | 279,327 | (55,146) refund | 8,754 | 423,481 | 532,862 |
| Cash, cash equivalents, and restricted cash at end of period | 263,753 | 875,228 | 282,298 | 756,123 | 385,909 | 778,379 |

[Q2 2026 release, Statements of Cash Flows] [Q1 2026 release, Statements of Cash Flows] [Q4 2025 release, Statements of Cash Flows]

- Footnote to H1 2026 income taxes paid, verbatim: "(1) Included in the income taxes paid amount is $93,000 related to the purchase of federal transferable energy credits for the 2026 tax year." [Q2 2026 release, Statements of Cash Flows] (The table is in thousands, so $93,000 thousand.)
- Capex accrued but unpaid: "Purchases of leasehold improvements, property and equipment accrued in accounts payable and accrued liabilities | $ | 97,015 | $ | 75,585" (H1 2026 vs H1 2025) [Q2 2026 release, Statements of Cash Flows]; 102,570 vs 76,389 (Q1) [Q1 2026 release, Statements of Cash Flows]; 89,429 vs 82,636 (FY2025 vs FY2024) [Q4 2025 release, Statements of Cash Flows].
- H1 2026 operating cash flow less capex = 1,332,003 − 397,601 = 934,402 (computed); FY2025 = 2,113,926 − 666,336 = 1,447,590 (computed).

## 3. Outlook sections, verbatim, in order

Q4 2025 release (2026-02-03), original 2026 outlook [Q4 2025 release, Outlook]:
> Outlook
> For 2026, management is anticipating the following:
> •Full year comparable restaurant sales to be about flat
> •350 to 370 new restaurant openings, which includes 10 to 15 international partner-operated restaurants. Around 80% of company-owned restaurants will have a Chipotlane
> •An estimated underlying effective full year tax rate between 24% and 26% before discrete items

Q1 2026 release (2026-04-29), unchanged [Q1 2026 release, Outlook]:
> Outlook
> For 2026, management is anticipating the following:
> •Full year comparable restaurant sales to be about flat
> •350 to 370 new restaurant openings, which includes 10 to 15 international partner-operated restaurants. Around 80% of company-owned restaurants will have a Chipotlane
> •An estimated underlying effective full year tax rate between 24% and 26% before discrete items

Q2 2026 release (2026-07-29), comps raised [Q2 2026 release, Outlook]:
> Outlook
> For 2026, management is anticipating the following:
> •Full year comparable restaurant sales growth in the low single digit range
> •350 to 370 new restaurant openings, which includes 10 to 15 international partner-operated restaurants. Around 80% of new company-owned restaurants will have a Chipotlane
> •An estimated underlying full year effective tax rate between 24% and 26% before discrete items

- Progression in one line: comps "about flat" (Feb) → "about flat" (Apr) → "growth in the low single digit range" (Jul); openings 350 to 370 including 10 to 15 partner-operated and around 80% Chipotlanes, unchanged all three times; tax rate 24% to 26% before discrete items, unchanged. The Q1 deck's own words were "Maintaining FY26 Outlook" [Q1 2026 slides, p.9] and the Q2 deck's "Increasing FY26 Outlook ... increasing our full-year comparable sales outlook to the low-single-digit range" [Q2 2026 slides, p.9]. Minor wording differences between releases: "Around 80% of company-owned restaurants" (Feb, Apr) vs "Around 80% of new company-owned restaurants" (Jul); "underlying effective full year tax rate" (Feb, Apr) vs "underlying full year effective tax rate" (Jul).
- Longer-term goals (not time-bound), verbatim from the Q4 deck: "Recipe for Growth Longer-Term Goals: $4+ MILLION AUVs | 7,000+ N.A. RESTAURANTS | RESTAURANT LEVEL OPERATING MARGIN APPROACHING 30% | GROW INTERNATIONAL PARTNERSHIPS". "“Recipe for Growth” is expected to position us for success in any environment. WE INTEND TO: Grow transactions; Drive accuracy, efficiency and speed; Deliver long-term, sustainable growth for our people, our guests and our shareholders". [Q4 2025 slides, p.7] Unit-growth rate: "we remain confident in our ability to reach 7,000+ North America restaurants, and by scaling with intention through trusted partner-operated markets and strategic new regions, we will continue to expand our global reach and grow new restaurant openings by 8-10% per year." [Q4 2025 slides, p.9] The Mexico release restates "a target of operating 7,000 locations in the U.S. and Canada". [IR release 2026-07-13 (Mexico)]
- Middle East 2026 expectation, verbatim: "Expect to nearly double footprint and sales in 2026"; "New Markets: Expect to open 3 new partner-operated markets this year in Mexico, Singapore, and South Korea". [Q4 2025 slides, p.9]
- HEEP rollout target, verbatim: "350 restaurants have equipment today, ~ 2,000 by year-end" [Q4 2025 slides, p.8]; "Over 600 restaurants have equipment today, ~ 2,000 by year-end" [Q1 2026 slides, p.6]; "1000+ restaurants with equipment today, ~ 2,000 by year-end" [Q2 2026 slides, p.6].
- What the call will cover, verbatim: "Chipotle will host a conference call on Wednesday, July 29, 2026, at 4:30 PM Eastern time to discuss second quarter 2026 financial results and provide a business update for the third quarter to date." [Q2 2026 release, Conference Call Details and Supplemental Slides] The non-GAAP tables PDF adds, verbatim: "Certain non-GAAP measures presented on a forward-looking basis during our investor conference call, such as adjusted general and administrative expenses or restaurant level operating margin for our third quarter 2026, were not reconciled to the comparable GAAP financial measures because the reconciliation could not be performed without unreasonable efforts. The GAAP measures are not accessible on a forward-looking basis because we are currently unable to predict with a reasonable degree of certainty the type and extent of certain items that would be expected to impact GAAP measures for these periods but would not impact the non-GAAP measures. Such items may include corporate initiatives, litigation expense, impairments on long lived assets, and other items. The unavailable information could have a significant impact on our GAAP financial results." [Q2 2026 non-GAAP tables, p.1] (So any Q3 2026 restaurant-level-margin or G&A guidance was given on the call, not in the release; see the transcript gatherer's notes.)
- Forward-looking statement scope in the Q2 release lists what the guidance covers, verbatim: "statements under “Outlook,” and about our anticipated full year 2026 comparable restaurant sales growth, the number of new company-owned and international partner-operated restaurant openings in 2026, expected number of restaurants with Chipotlanes, and estimated underlying effective 2026 full year tax rate, as well as statements about the expected success of our “Recipe for Growth” strategy, our future food, beverage, packaging, labor, general and administrative and other costs, future estimated tax rates and future long-term prospects." [Q2 2026 release, Forward-Looking Statements]

## 4. Non-GAAP reconciliations

### 4.1 Definitions, verbatim [Q2 2026 release, Non-GAAP definitions]

- "Adjusted net income is net income excluding restaurant asset impairment, corporate asset impairment and gains, restructuring expenses, certain legal proceedings, stock-based compensation retention and loss on investments."
- "Adjusted diluted earnings per share is calculated by dividing adjusted net income by the diluted weighted-average number of common shares outstanding."
- "Adjusted general and administrative expenses are general and administrative expenses excluding expenses related to restructuring, certain legal proceedings and stock-based compensation retention."
- "The adjusted effective income tax rate is the effective income tax rate adjusted to reflect the after-tax impact of non-GAAP adjustments."
- "Restaurant level operating margin is equal to the revenues generated by our restaurants less direct restaurant operating costs, which consist of food, beverage and packaging, labor, occupancy and other operating costs, expressed as a percent of total revenue. This performance measure primarily includes the costs that restaurant level managers can directly control and excludes other costs that are essential to conduct our business. Management uses restaurant level operating margin as a measure of restaurant performance. Management believes restaurant level operating margin is useful because it highlights trends in our core business that may not otherwise be apparent when relying solely on GAAP financial measures."
- The Q1 2026 release adds: "Adjusted labor is labor expense excluding expenses related to certain legal proceedings." and "Adjusted restaurant level operating margin is equal to the restaurant level operating margin excluding certain legal proceedings, expressed as a percent of total revenue." [Q1 2026 release, Non-GAAP definitions]
- The Q4 2025 release's definition, verbatim (older list of items): "Adjusted net income is net income excluding restaurant asset impairment and gains, corporate asset impairment and gains, expenses/(reductions) related to certain legal proceedings, stock-based compensation forfeiture, stock-based compensation retention grants, and loss on investments. Adjusted general and administrative expense is general and administrative expense excluding expenses related to certain legal proceedings, stock-based compensation forfeiture and stock-based compensation retention grants." [Q4 2025 release, Non-GAAP definitions]

### 4.2 Adjusted net income and adjusted diluted EPS ($ thousands, except per share)

Q2 2026 vs Q2 2025. [Q2 2026 release, Adjusted Net Income reconciliation] (identical table at [Q2 2026 non-GAAP tables, p.2] and as an image at [Q2 2026 slides, p.13])

| Line | Q2 2026 | Q2 2025 |
|---|---|---|
| Net income | 403,547 | 436,127 |
| Restaurant asset impairment (1) | 3,933 | - |
| Corporate asset impairment and other corporate (gains)/costs (2) | - | (1,484) |
| Recipe for Growth restructuring (3) | 3,346 | - |
| Legal proceedings-General and administrative (4) | 10,000 | - |
| Stock-based compensation (5) | 925 | 12,213 |
| Investment unrealized loss (6) | - | 6,168 |
| Total non-GAAP adjustments | 18,204 | 16,897 |
| Tax effect of non-GAAP adjustments above (7) | (2,845) | (2,619) |
| After tax impact of non-GAAP adjustments | 15,359 | 14,278 |
| Adjusted net income | 418,906 | 450,405 |
| Diluted weighted-average number of common shares outstanding | 1,279,064 | 1,350,236 |
| Diluted earnings per share | $0.32 | $0.32 |
| Adjusted diluted earnings per share | $0.33 | $0.33 |

Footnotes, verbatim: "(1)Operating lease asset and leasehold improvements, property, plant and equipment impairment charges and other expenses for restaurants due to closures, relocations, or underperformance. (2)Lease remeasurement gain for vacated office space. (3)Cost related to restructuring, including employee severance, recruitment, other third-party restructuring costs, and stock-based compensation, net of forfeitures. (4)Estimated liability recognized in general and administrative expenses on the condensed consolidated statements of income for legal matters that we expect to exceed typical costs for legal proceedings. (5)Stock-based compensation for retention equity awards granted to certain executives in connection with the former CEO's departure. (6)Charges for an unrealized loss in a long-term investment. (7)Adjustments related to the tax effect of non-GAAP adjustments, which were determined based on the nature of the underlying non-GAAP adjustments and their relevant jurisdictional tax rates." [Q2 2026 release, Adjusted Net Income reconciliation]

Q1 2026 vs Q1 2025. [Q1 2026 release, Adjusted Net Income reconciliation] (image at [Q1 2026 slides, p.13])

| Line | Q1 2026 | Q1 2025 |
|---|---|---|
| Net income | 302,824 | 386,599 |
| Legal proceedings-Labor (1) | 11,875 | - |
| Recipe for Growth restructuring (2) | 2,140 | - |
| Legal proceedings-General and administrative (3) | 625 | - |
| Stock-based compensation (4) | 3,007 | 11,877 |
| Total non-GAAP adjustments | 17,647 | 11,877 |
| Tax effect of non-GAAP adjustments above (5) | (4,249) | (1,676) |
| After tax impact of non-GAAP adjustments | 13,398 | 10,201 |
| Adjusted net income | 316,222 | 396,800 |
| Diluted weighted-average number of common shares outstanding | 1,301,859 | 1,360,719 |
| Diluted earnings per share | $0.23 | $0.28 |
| Adjusted diluted earnings per share | $0.24 | $0.29 |

Footnotes, verbatim: "(1)Estimated liability recognized in labor on the condensed consolidated statements of income for legal matters that we expect to exceed typical costs for legal proceedings. (2)Cost for restructuring including employee severance, recruitment, other third-party restructuring costs, and stock-based compensation, net of forfeitures. (3)Estimated liability recognized in general and administrative expenses on the condensed consolidated statements of income for legal matters that we expect to exceed typical costs for legal proceedings. (4)Stock-based compensation for retention equity awards granted to certain executives in connection with the former CEO's departure. (5)Adjustments related to the tax effect of non-GAAP adjustments, which were determined based on the nature of the underlying non-GAAP adjustments and their relevant jurisdictional tax rates." [Q1 2026 release, Adjusted Net Income reconciliation]

Q4 2025 vs Q4 2024 and FY2025 vs FY2024. [Q4 2025 release, Adjusted Net Income reconciliation] (image at [Q4 2025 slides, p.19])

| Line | Q4 2025 | Q4 2024 | FY2025 | FY2024 |
|---|---|---|---|---|
| Net income | 330,932 | 331,764 | 1,535,761 | 1,534,110 |
| Restaurant asset impairment (1) | 2,466 | 2,634 | 2,466 | 2,634 |
| Gain on restaurant lease termination (2) | (1,518) | - | (1,518) | - |
| Corporate asset impairment and other corporate (gains)/costs (3) | - | (7,392) | (1,484) | (7,392) |
| Software asset impairment (4) | - | - | - | 6,249 |
| Legal proceedings (5) | (4,387) | 4,387 | (4,387) | 21,437 |
| Stock-based compensation forfeiture (6) | - | - | - | (27,863) |
| Stock-based compensation retention grants (7) | 2,611 | 11,945 | 34,759 | 17,079 |
| Investment unrealized loss (8) | - | - | 6,168 | 1,381 |
| Total non-GAAP adjustments | (828) | 11,574 | 36,004 | 13,525 |
| Tax effect of non-GAAP adjustments above (9) | 1,235 | (3,386) | (3,358) | (8,804) |
| After tax impact of non-GAAP adjustments | 407 | 8,188 | 32,646 | 4,721 |
| Adjusted net income | 331,339 | 339,952 | 1,568,407 | 1,538,831 |
| Diluted weighted-average number of common shares outstanding | 1,319,988 | 1,368,923 | 1,342,616 | 1,376,555 |
| Diluted earnings per share | $0.25 | $0.24 | $1.14 | $1.11 |
| Adjusted diluted earnings per share | $0.25 | $0.25 | $1.17 | $1.12 |

Footnotes, verbatim: "(1)Operating lease asset and leasehold improvements, property, plant and equipment impairment charges and other expenses for restaurants due to closures, relocations, or underperformance. (2)Lease remeasurement gain at termination of restaurant lease. (3)Other gains for offices or other corporate assets. (4)Property and equipment impairment charges related to a software asset. (5)(Reduction)/charges for estimated settlements for distinct legal matters that exceeded or are expected to exceed typical costs for these types of legal proceedings. (6)Stock-based compensation expense reversal for equity awards forfeited by our former CEO. (7)Stock-based compensation expense for retention equity awards granted to key executives in connection with the CEO transition. (8)Charges for unrealized losses in long-term investments. (9)Adjustments related to the tax effect of non-GAAP adjustments, which were determined based on the nature of the underlying non-GAAP adjustments and their relevant jurisdictional tax rates." [Q4 2025 release, Adjusted Net Income reconciliation] Note the row "Stock-based compensation forfeiture (6) | - | - | (27,863)" prints only three values in the source (the FY2024 column is the (27,863); the Q4 columns and FY2025 are dashes).

### 4.3 Adjusted labor (Q1 2026 only) [Q1 2026 release, Adjusted Labor reconciliation] (image at [Q1 2026 slides, p.14])

| Line | Q1 2026 | Q1 2025 |
|---|---|---|
| Labor | 805,411 | 718,226 |
| Legal proceedings-Labor (1) | (11,875) | - |
| Adjusted labor | 793,536 | 718,226 |
| Adjusted labor as a percent of total revenue | 25.7% | 25.0% |

### 4.4 Adjusted general and administrative expenses ($ thousands)

| Line | Q2 2026 | Q2 2025 | Q1 2026 | Q1 2025 | Q4 2025 | Q4 2024 | FY2025 | FY2024 |
|---|---|---|---|---|---|---|---|---|
| General and administrative expenses | 190,471 | 172,151 | 203,720 | 172,783 | 160,341 | 191,216 | 652,017 | 697,483 |
| Recipe for Growth restructuring | (3,346) | - | (2,140) | - | | | | |
| Legal proceedings-General and administrative | (10,000) | - | (625) | - | | | | |
| Legal proceedings (Q4 release row) | | | | | 4,387 | (4,387) | 4,387 | (21,437) |
| Stock-based compensation forfeiture | | | | | - | - | - | 27,863 |
| Stock-based compensation (retention) | (925) | (12,213) | (3,007) | (11,877) | (2,611) | (11,945) | (34,759) | (17,079) |
| Total non-GAAP adjustments | (14,271) | (12,213) | (5,772) | (11,877) | 1,776 | (16,332) | (30,372) | (10,653) |
| Adjusted general and administrative expenses | 176,200 | 159,938 | 197,948 | 160,906 | 162,117 | 174,884 | 621,645 | 686,830 |

[Q2 2026 release, Adjusted G&A reconciliation] (also [Q2 2026 non-GAAP tables, p.3], image [Q2 2026 slides, p.14]); [Q1 2026 release, Adjusted G&A reconciliation] (image [Q1 2026 slides, p.14]); [Q4 2025 release, Adjusted G&A reconciliation]. The Q4 release's legal row footnote reads "(1)Reductions/(charges) for estimated settlements for distinct legal matters that exceeded or are expected to exceed typical costs for these types of legal proceedings." and its stock-comp rows are labelled "Stock-based compensation forfeiture (2)" and "Stock-based compensation retention grants (3)". [Q4 2025 release, Adjusted G&A reconciliation]

### 4.5 Adjusted effective income tax rate

| Line | Q2 2026 | Q2 2025 | Q1 2026 | Q1 2025 | Q4 2025 | Q4 2024 | FY2025 | FY2024 |
|---|---|---|---|---|---|---|---|---|
| Effective income tax rate | 24.3% | 24.5% | 25.4% | 22.9% | 23.7% | 24.4% | 23.6% | 23.7% |
| Tax impact of non-GAAP adjustments | (0.3) | (0.3) | (0.1) | (0.2) | (0.3) | 0.2 | (0.3) | 0.3 |
| Adjusted effective income tax rate | 24.0% | 24.2% | 25.3% | 22.7% | 23.4% | 24.6% | 23.3% | 24.0% |

[Q2 2026 release, Adjusted Effective Income Tax Rate reconciliation] (also [Q2 2026 non-GAAP tables, p.4], image [Q2 2026 slides, p.14]); [Q1 2026 release, Adjusted Effective Income Tax Rate reconciliation]; [Q4 2025 release, Adjusted Effective Income Tax Rate reconciliation]

### 4.6 Restaurant level operating margin ($ thousands; % of total revenue)

| Line | Q2 2026 | % | Q2 2025 | % | Q1 2026 | % | Q1 2025 | % |
|---|---|---|---|---|---|---|---|---|
| Income from operations | 525,595 | 15.7 | 559,057 | 18.2 | 397,063 | 12.9 | 479,250 | 16.7 |
| General and administrative expenses | 190,471 | 5.7 | 172,151 | 5.6 | 203,720 | 6.6 | 172,783 | 6.0 |
| Depreciation and amortization | 98,327 | 2.9 | 90,945 | 3.0 | 96,718 | 3.1 | 87,211 | 3.0 |
| Pre-opening costs | 16,364 | 0.5 | 10,610 | 0.3 | 11,641 | 0.4 | 8,210 | 0.3 |
| Impairment, closure costs, and asset disposals | 13,808 | 0.4 | 5,467 | 0.2 | 9,819 | 0.3 | 6,168 | 0.2 |
| Total non-GAAP Adjustments | 318,970 | 9.5 | 279,173 | 9.1 | 321,898 | 10.4 | 274,372 | 9.5 |
| Restaurant level operating margin | 844,565 | 25.2 | 838,230 | 27.4 | 718,961 | 23.3 | 753,622 | 26.2 |
| Legal proceedings-Labor (Q1 only) | | | | | 11,875 | 0.4 | - | - |
| Adjusted restaurant level operating margin (Q1 only) | | | | | 730,836 | 23.7 | 753,622 | 26.2 |

[Q2 2026 release, Restaurant Level Operating Margin reconciliation] (also [Q2 2026 non-GAAP tables, p.5], image [Q2 2026 slides, p.15]); [Q1 2026 release, Restaurant Level Operating Margin reconciliation] (image [Q1 2026 slides, p.15])

| Line | Q4 2025 | % | Q4 2024 | % | FY2025 | % | FY2024 | % |
|---|---|---|---|---|---|---|---|---|
| Income from operations | 420,319 | 14.1 | 415,732 | 14.6 | 1,935,798 | 16.2 | 1,916,333 | 16.9 |
| General and administrative expenses | 160,341 | 5.4 | 191,216 | 6.7 | 652,017 | 5.5 | 697,483 | 6.2 |
| Depreciation and amortization | 92,702 | 3.1 | 83,876 | 2.9 | 361,382 | 3.0 | 335,030 | 3.0 |
| Pre-opening costs | 16,946 | 0.6 | 12,905 | 0.5 | 49,507 | 0.4 | 41,897 | 0.4 |
| Impairment, closure costs, and asset disposals | 8,464 | 0.3 | 532 | - | 27,503 | 0.2 | 26,949 | 0.2 |
| Total non-GAAP Adjustments | 278,453 | 9.3 | 288,529 | 10.1 | 1,090,409 | 9.1 | 1,101,359 | 9.7 |
| Restaurant level operating margin | 698,772 | 23.4 | 704,261 | 24.8 | 3,026,207 | 25.4 | 3,017,692 | 26.7 |

[Q4 2025 release, Restaurant Level Operating Margin reconciliation] (image at [Q4 2025 slides, p.20], whose title reads "Restaurant Level Operating Margin and Cash Flow" (from slide image p.20, visual read))

- Restaurant level operating margin series in one row (all from the reconciliations above): Q4 2024 24.8%; FY2024 26.7%; Q1 2025 26.2%; Q2 2025 27.4%; Q4 2025 23.4%; FY2025 25.4%; Q1 2026 23.3% (23.7% adjusted); Q2 2026 25.2%. Q3 2025 is not in any of the three releases (see §7).

## 5. Slide-deck content

### 5.1 Q2 2026 deck (15 pages; footer "Q2 2026 Investor Information · PROPRIETARY INFORMATION · ALL RIGHTS RESERVED. CHIPOTLE MEXICAN GRILL")

- p.1 (cover, unnumbered): "RECIPE FOR GROWTH" badge; "Q2 2026 EARNINGS INVESTOR INFORMATION". Photograph. [Q2 2026 slides, p.1]
- p.2 Forward-looking statements: two columns of text; lists as forward-looking "our anticipated full year 2026 comparable restaurant sales growth, future margins, the number of new company-owned and international partner-operated restaurant openings in 2026, as well as statements about the expected success of our “Recipe for Growth” strategy, our future food, beverage, packaging, labor, general and administrative and other costs, future estimated tax rates and future long-term prospects." Risk list includes "the expected costs and risks related to our international expansion, including through partner-operated restaurants in the Middle East, Asia, and Mexico". [Q2 2026 slides, p.2]
- p.3 "OUR INVESTMENT THESIS — WE ARE AN INDUSTRY LEADER BUILT ON:", verbatim, five items: "Extraordinary Value Proposition Anchored By Brand Strength and Customer Loyalty"; "Food with Integrity Due to High Quality, Delicious and Real Ingredients Served Quickly at Accessible Price Points"; "Distinct, Competitive Advantages, Grounded in Best-in-Class Operations and Innovation"; "Strong Balance Sheet and Track Record of Returning Capital to Shareholders"; "Top-Tier Management Team with Deep Expertise to Realize “Recipe For Growth” Strategy". [Q2 2026 slides, p.3] (Identical on [Q1 2026 slides, p.3] and [Q4 2025 slides, p.3].)
- p.4 "CONTINUOUSLY INNOVATING" timeline with an "AT A GLANCE" panel, "Note: As of June 30, 2026": "HEADQUARTERS Newport Beach, CA"; "OUR PEOPLE ~140,000 employees"; "LOCATIONS 4,200+ restaurants across North America, Europe and the Middle East". Timeline, verbatim: "1993 First restaurant opens in Denver as a private company"; "1998 Outside investment accelerates openings"; "2006 Go public on NYSE"; "2011 Established “Chipotle Cultivate Foundation”"; "2019 Launch of Chipotle “Rewards” program"; "2024 Scott Boatwright named CEO"; "2024 1st Middle East partnership"; "2025 Accelerate Menu Innovation (“Build Your Own Chipotle”)"; "2025 Record restaurant openings — 334 COMPANY-OWNED GLOBALLY; MIDDLE EAST 11 IN 2025, 14 TOTAL"; "2026 Deploying “Recipe For Growth” strategy to drive value". [Q2 2026 slides, p.4] (The Q1 deck's panel reads "135,000+ employees", "4,100+ restaurants", "As of March 31, 2026" [Q1 2026 slides, p.4]; the Q4 deck's reads "130,000+ employees", "4,000+ restaurants", "As of December 31, 2025" [Q4 2025 slides, p.4]; the timeline entries are the same in all three, so the Middle East "14 TOTAL" on the Q2 deck is the year-end 2025 figure, not the June 2026 count of 15 [Q2 2026 release, Supplemental Financial and Other Data].)
- p.5 "OUR RECIPE FOR SUSTAINABLE GROWTH… THE NEXT PHASE OF OUR GROWTH WILL BE SUPPORTED BY FIVE KEY STRATEGIES", verbatim: "Drive Operational and Culinary Excellence — Protect and strengthen the core to deliver exceptional value"; "Evolve Brand Messaging and Accelerate Menu Innovation & New Occasions — Drive demand to restaurants"; "Modernize Our Model through Industry-Leading Technology — Leverage AI and relaunch Rewards Program to elevate guest and team experience"; "Expand Global Reach — Scale with intention via proven, company-owned and partner-operated markets and strategic new regions"; "Cultivate the Best Talent in the Industry — Prioritize energy, speed and agility". Banner: "DOUBLING DOWN ON WHAT UNIQUELY DIFFERENTIATES OUR BRAND TO POSITION CHIPOTLE FOR THE NEXT PHASE OF GROWTH". [Q2 2026 slides, p.5] (Identical on [Q1 2026 slides, p.5] and [Q4 2025 slides, p.6].) The Q4 release's numbered version of the same five: "1.Protect and strengthen the core by driving operational and culinary excellence to deliver exceptional value for our guests; 2.Evolve the brand messaging and accelerate menu innovation and new occasions that drive demand into our restaurants; 3.Modernize our business model with industry-leading technology, including leveraging AI and relaunching our Rewards Program, to elevate the experience for our guests and teams; 4.Expand our global reach by scaling with intention through proven, company-owned and partner-operated markets, as well as strategic new regions; and 5.Cultivate the best talent in the industry that is energized and focused on speed and agility." [Q4 2025 release, "Recipe for Growth" Strategy]
- p.6 "INNOVATION IS DRIVING STRONGER PERFORMANCE", verbatim. Left: "CHIPOTLE KITCHEN IS: ENHANCING DIGITAL ORDER ACCURACY, SPEED AND CONSISTENCY; CREATING IMPROVEMENTS IN ON-TIME FULFILLMENT AND OVERALL GUEST SATISFACTION" (two screenshots of a kitchen display showing a burrito order with its ingredients; no numbers). Right: "HIGH EFFICIENCY EQUIPMENT PACKAGE IS: EASING REPETITIVE PREP; IMPROVING CONSISTENCY; SIMPLIFYING PROCESSES; ENABLING READINESS FOR PEAK; … ALL WHILE MAINTAINING OR IMPROVING OUR CULINARY STANDARDS". "RESULTING IN: Higher food quality, throughput and guest satisfaction scores; Hundreds of basis points of improvement in comparable sales; 1000+ restaurants with equipment today, ~ 2,000 by year-end". [Q2 2026 slides, p.6]
- p.7 "CHIPOTLE IS DEEPENING GUEST ENGAGEMENT THROUGH…", verbatim. "SUMMER OF EXTRAS CAMPAIGN, WHICH IS… Built on momentum of Rewards relaunch; Designed to reward frequency and deepen engagement; Resulting in more frequency and more members engaging … with the highest gains amongst our lowest frequency guests". "MENU INNOVATION, INCLUDING… Return of Chipotle Honey Chicken — Outperformed last year’s launch with attachment rate over 25%; Success of Cilantro Lime Sauce — Attachment rates above Red Chimichurri and Adobo Ranch … reinforcing demand for flavor-forward profiles". "UNDERSCORING COMMITMENT TO COMPELLING INNOVATION WHILE STAYING TRUE TO CULINARY PRINCIPLES". [Q2 2026 slides, p.7]
- p.8 (divider, unnumbered): "FINANCIAL RESULTS". [Q2 2026 slides, p.8]
- p.9 "Q2 2026 Highlights": see §1.1 table and narrative. Footnote: "1 Non-GAAP measure. See Appendix for additional information, including reconciliations to most comparable GAAP measures". [Q2 2026 slides, p.9]
- p.10 "OUR INVESTMENT THESIS" repeated with a left-hand bullet list, verbatim: "Committed to “Food with Integrity”; Continue to deliver exceptional value; Pursue new growth vectors; Modernize our business; Scale with intention; Invest in the development and growth of our world-class people". [Q2 2026 slides, p.10]
- p.11 (divider, unnumbered): "APPENDIX". [Q2 2026 slides, p.11]
- p.12 "DEFINITIONS", verbatim: "Restaurant Level Operating Margin — Restaurant level operating margin is a non-GAAP financial measure and represents total revenue less direct restaurant operating costs, expressed as a percent of total revenue." "Restaurant Cash Flow — Restaurant cash flow is a non-GAAP financial measure and represents total revenue less direct restaurant operating costs." "Adjusted Diluted EPS — Adjusted diluted EPS is a non-GAAP financial measure and represents adjusted net income divided by the diluted weighted-average number of common shares outstanding." "Average Unit Volume (“AUV”) — Average Unit Volume represents the average trailing 12-month food and beverage revenue for company-owned restaurants in operation for at least 12 full calendar months." "Comparable Restaurant Sales — Represents the change in period-over-period total revenue for company-owned restaurants in operation for at least 13 full calendar months." [Q2 2026 slides, p.12] The releases' matching definitions add "Digital sales represent food and beverage revenue for company-owned restaurants generated through the Chipotle website, Chipotle app or third-party delivery aggregators. Digital sales include revenue deferrals associated with Chipotle Rewards." and "Partner-operated restaurants represent Chipotle restaurants over which Chipotle does not have a controlling financial interest and for which Chipotle does not directly manage day-to-day operations. This includes restaurants operated by third parties pursuant to license or franchise agreements and restaurants in which Chipotle holds a minority, non‑controlling ownership interest." [Q2 2026 release, Definitions] No deck or release defines "Chipotlane"; the term is used without definition ("Opened 100 company-owned restaurants, with 80 locations including a Chipotlane") [Q2 2026 release, Headline].
- pp.13–15 "RECONCILIATION OF NON-GAAP FINANCIAL MEASURES": image-only tables (the text layer holds only the titles). p.13 = adjusted net income and adjusted diluted EPS; p.14 = adjusted G&A and adjusted effective income tax rate; p.15 = restaurant level operating margin. Every number on the three images equals the corresponding release table in §4 (verified by OCR at 300 dpi, 54 of 54 numbers; see §8), so the release values are used throughout. [Q2 2026 slides, pp.13–15]

### 5.2 Q1 2026 deck (15 pages) — pages that differ from the Q2 deck

- p.2 Forward-looking statements: the Q1 (and Q4) wording lists "future AUV and margins, the number of company owned and partner-operated restaurants we will open, and the future success of our Recipe for Growth initiatives" [Q1 2026 slides, p.2]; the Q2 deck replaced this with the release's list (§5.1 p.2).
- p.6 "INNOVATION IS DRIVING PRODUCTIVITY & PERFORMANCE — Our High Efficiency Equipment Package is simplifying prep and enhancing the guest experience", verbatim. Left panel: "EASING REPETITIVE PREP; IMPROVING CONSISTENCY; SIMPLIFYING PROCESSES; ENABLING READINESS FOR PEAK; … ALL WHILE MAINTAINING OR IMPROVING OUR CULINARY STANDARDS." "RESULTS IN: Higher “Taste of Food” and “Overall Guest Satisfaction” scores; Better throughput and meaningful comp sales outperformance; Over 600 restaurants have equipment today, ~ 2,000 by year-end". Right panel, the three pieces of equipment: "DUAL-SIDED PLANCHA — Cooks chicken and steak faster than a traditional plancha and improves consistency and increases capacity. Simplifies one of the most complex roles in the kitchen to make it easier for teams to execute." "THREE-PAN RICE COOKER — By cooking rice directly in line pans, we deliver it fresh and streamline the process. This enables smaller batches, less waste and the ability to cook white and brown rice simultaneously." "HIGH-CAPACITY FRYER — Increases chip-frying capacity, improves consistency and keeps restaurants stocked during peak periods." [Q1 2026 slides, p.6]
- p.7 "REWARDS ARE CREATING REPEAT ENGAGEMENT — Chipotle is entering its next phase of digital growth with a scaled platform", verbatim. "CUSTOMERS WIN WITH MORE FLEXIBILITY: Birthday optionality — Choose your reward with a 30-day redemption window; More ways to redeem — Lower point thresholds and new offers (e.g., 50% off entrée, group options); Extended point life — Points do not expire with one qualifying purchase per year". "CHIPOTLE WINS WITH DEEPER ENGAGEMENT: “Double Protein” promotion drove highest digital sales day; Loyalty comps outpacing non-loyalty comps through increased engagement (“Summer Of Extras” Campaign); Incremental sales through expanding new occasions (“Build Your Own Chipotle” and Catering)". "A ONE STOP SHOP FOR REWARDS: Rewards experience redesigned with all content in one easy-to-navigate hub; Always on with Gamification and Points Tracker; Prioritizes intuitive experience for users; Ongoing rewards available (Monthly “Freepotle” and bonus drops); Enables personalized interactions at scale". "Goal: Growing Rewards Participation Beyond 1 in 5 In-Restaurant Customers — LAUNCHING COMPREHENSIVE CAMPAIGN: Menu panels, table tents, cups, receipts and “cashwrap” messaging; LEVERAGING OUR CREWS: Incentives, training and communications to drive sign-ups; RECURRING OPPORTUNITIES FOR ENGAGEMENT: Turning visits into opportunities to enroll in Chipotle Rewards". [Q1 2026 slides, p.7]
- p.9 "Q1 2026 Highlights": see §1.2. [Q1 2026 slides, p.9]
- p.12 "DEFINITIONS": the first entry is "Adjusted Restaurant Level Operating Margin — Restaurant level operating margin is a non-GAAP financial measure and represents total revenue less direct restaurant operating costs, expressed as a percent of total revenue. Reconciliations to GAAP financial measures are set forth in a table at the end of this presentation. Adjusted to exclude certain legal proceedings." Other definitions as in the Q2 deck. [Q1 2026 slides, p.12]
- pp.13–15 image-only reconciliations: p.13 adjusted net income; p.14 adjusted labor and adjusted G&A; p.15 restaurant level operating margin with the "Legal proceedings-Labor" line and adjusted margin. All 55 numbers checked equal the Q1 release tables (OCR at 300 dpi). [Q1 2026 slides, pp.13–15]
- Pages 1, 3, 4 (except the "At a glance" figures), 5, 8, 10, 11 are the same as the Q2 deck. [Q1 2026 slides]

### 5.3 Q4/FY2025 deck (20 pages, "Q4/FY 2025 EARNINGS INVESTOR INFORMATION") — the series pages

- p.5 "PROVEN TRACK RECORD OF ACHIEVING GROWTH AND CREATING VALUE 2019-2025", verbatim tiles: "COMPARABLE RESTAURANT SALES INCREASE* +66% Since 2019"; "NEW RESTAURANT OPENINGS +1,675 Since 2019"; "REVENUES +113% Since 2019"; "RESTAURANT LEVEL OPERATING MARGIN +490 BPS expansion since 2019"; "ADJUSTED DILUTED EPS +27% CAGR Since 2019"; "SHAREHOLDER RETURNS VIA BUYBACKS Bought back $5.5B Since 2019". Footnote: "*Represents the geometric growth of comparable restaurant sales between December 31, 2018, and December 31, 2025." Banner: "WE EXPECT OUR STRONG FOUNDATION TO DRIVE THE NEXT WAVE OF GROWTH OVER THE LONG-TERM DUE TO "RECIPE FOR GROWTH" STRATEGY". [Q4 2025 slides, p.5]

"NET REVENUE" stacked bar chart on the same page, In-Store vs Digital, data labels in the PDF text layer (bar totals and both segment percentages; column assignment confirmed against the image (from slide image p.5, visual read)). [Q4 2025 slides, p.5]

| Year | Net revenue | In-Store % | Digital % |
|---|---|---|---|
| 2019 | $5.6B | 82% | 18% |
| 2020 | $6.0B | 54% | 46% |
| 2021 | $7.5B | 54% | 46% |
| 2022 | $8.6B | 61% | 39% |
| 2023 | $9.9B | 63% | 37% |
| 2024 | $11.3B | 65% | 35% |
| 2025 | $11.9B | 63% | 37% |

- p.7 longer-term goals: see §3. [Q4 2025 slides, p.7]
- p.8 "OUR MARKETING, TECHNOLOGY AND INNOVATION DRIVE RESULTS", verbatim. "High Efficiency Equipment Package Rollout — RESULTS IN: Higher “Taste of Food” and “Overall Guest Satisfaction” scores; Better throughput and meaningful comp sales outperformance; 350 restaurants have equipment today, ~ 2,000 by year-end". "Marketing and Rewards Program Evolution — RESULTS IN: “Double Protein” promotion drove highest digital sales day; Loyalty comps outpacing non-loyalty comps through increased engagement like our “Summer Of Extras” Campaign; Incremental sales through expanding new occasions like “Build Your Own Chipotle” and Catering". [Q4 2025 slides, p.8]
- p.9 "OUR GLOBAL PRESENCE UNDERSCORES OUR STRENGTH — Record 345 openings and 9%+ new restaurant growth in 2025", verbatim. "COMPANY – OWNED: 334 new restaurants (21 in Canada); Surpassed 4,000 total restaurants; 38% growth YoY in Canada; 9% growth YoY in North America; Central London and Frankfurt cash on cash returns unlocking growth in the region". "PARTNER – OPERATED MARKETS (MIDDLE EAST, MEXICO, SINGAPORE AND SOUTH KOREA): Middle East: Opened 11 new restaurants in 2025, 14 total in the region; Expect to nearly double footprint and sales in 2026. New Markets: Expect to open 3 new partner-operated markets this year in Mexico, Singapore, and South Korea". Photo captions: "TORONTO, ON", "HIXSON, TN", "CANARY WHARF, LONDON", "JUMEIRAH BEACH RESIDENCE, DUBAI". Banner: "By ramping up growth in proven, company-owned markets, we remain confident in our ability to reach 7,000+ North America restaurants, and by scaling with intention through trusted partner-operated markets and strategic new regions, we will continue to expand our global reach and grow new restaurant openings by 8-10% per year." [Q4 2025 slides, p.9] 345 = 334 company-owned + 11 partner-operated (computed; consistent with [Q4 2025 release, Headline]).
- p.10 "OUR PEOPLE MAKE OUR SUCCESS POSSIBLE", verbatim: "To continue Cultivating a Better World, we need efficient, dedicated and effective team members!" "In 2025, 23,000 internal promotions, including 100% of Regional VP roles, over 83% of Field Leader positions and nearly 90% of restaurant management". "YEAR OVER YEAR CUSTOMER SATISFACTION IMPROVEMENT — WHICH MEANS… OUR CULTURE OF SPEED, AGILITY AND PURPOSE IS WORKING". Banner: "WITH TRUE OPERATORS AT THE HELM, OUR SYSTEMS, TOOLS, PROCESSES AND PEOPLE WILL DEFINE THE NEXT CHAPTER FOR OUR RESTAURANTS". [Q4 2025 slides, p.10]
- p.12 "Q4 AND FY 2025 FINANCIAL HIGHLIGHTS — ACHIEVED RESULTS IN DYNAMIC CONSUMER BACKDROP": see §1.3 table. [Q4 2025 slides, p.12]

p.13 "OUR DIFFERENTIATED UNIT ECONOMIC MODEL DRIVES INDUSTRY LEADING ROI — AVERAGE RESTAURANT ECONOMIC MODEL USING FY 2025 RESULTS" (text layer). [Q4 2025 slides, p.13]

| Line | Per restaurant | % |
|---|---|---|
| Average Unit Volume | $3.1 million | |
| Food Costs | $918k | 29.6% |
| Labor Costs | $778k | 25.1% |
| Other Operating Costs | $456k | 14.7% |
| Occupancy Costs | $161k | 5.2% |
| Restaurant Cash Flow | $787k | 25.4% |

(The percentages equal the FY2025 income-statement cost ratios and the FY2025 restaurant level operating margin in §2.1 and §4.6; "Restaurant Cash Flow" is defined on p.18 as "total revenue less direct restaurant operating costs".) [Q4 2025 slides, p.13] [Q4 2025 slides, p.18]

p.14 "GLOBAL NEW RESTAURANT GROWTH", two bar charts with data labels in the text layer; the "+N" row under each year is labelled "NRO’s:" (new restaurant openings). [Q4 2025 slides, p.14]

| Year-end | Global Restaurants | NRO's | Global Chipotlanes | NRO's |
|---|---|---|---|---|
| 2019 | 2,622 | +140 | 66 | +56 |
| 2020 | 2,768 | +161 | 170 | +100 |
| 2021 | 2,966 | +215 | 355 | +174 |
| 2022 | 3,187 | +236 | 571 | +202 |
| 2023 | 3,437 | +271 | 811 | +238 |
| 2024 | 3,729* | +307 | 1,068 | +257 |
| 2025 | 4,056* | +345 | 1,326* | +258 |

Footnotes, verbatim: "* Includes 3 partner-operated restaurants in 2024 and 14 partner-operated restaurants in 2025" (restaurants chart); "* Includes 1 partner-operated Chipotlane in 2025" (Chipotlanes chart). [Q4 2025 slides, p.14] Cross-check: 4,056 − 14 = 4,042 company-owned, matching the Q4 release unit table; 3,729 − 3 = 3,726, matching the Dec. 31, 2024 column (computed). The 2025 Chipotlane NRO of +258 vs the release's "257 locations including a Chipotlane" among company-owned openings differs by the 1 partner-operated Chipotlane in the footnote (computed).

- p.15 "CAPITAL ALLOCATION PRIORITIES — Dynamic strategy to further track record of returning capital to shareholders", verbatim: "Cash, Cash Equivalents, Restricted Cash and Investments of $1.3 BILLION* and no debt"; "Bought back $742 MILLION worth of stock at an average price of $34.14 during Q4’25"; "Totaling a record $2.4 BILLION for the full year 2025"; "*As of December 31, 2025." [Q4 2025 slides, p.15]
- p.18 "DEFINITIONS": as the Q2 deck's p.12 but each non-GAAP entry adds "Reconciliations to GAAP financial measures are set forth in a table at the end of this presentation." [Q4 2025 slides, p.18]
- pp.19–20 image-only reconciliations: p.19 adjusted net income Q4 and FY (2025 vs 2024); p.20 restaurant level operating margin Q4 and FY. All 97 numbers checked equal the Q4 release tables (OCR at 300 dpi). The Q4 deck has no adjusted G&A or adjusted tax-rate page; those are in the release only. [Q4 2025 slides, pp.19–20]
- Pages 1 (cover), 2, 3, 4, 6, 11 (divider "FINANCIAL RESULTS"), 16 (investment thesis with bullets), 17 (divider "APPENDIX") match the 2026 decks' equivalents. [Q4 2025 slides]

## 6. Mexico release, 2026-07-13 [IR release 2026-07-13 (Mexico)]

- Title on the IR site: "CHIPOTLE ENTERS MEXICO WITH FIRST RESTAURANT IN NUEVO LEON" (from the page URL and title); sub-head, verbatim: "Chipotle and Alsea plan additional openings in Nuevo León this year and expansion into Mexico City in 2027". Dateline "NEWPORT BEACH, Calif., July 13, 2026 /PRNewswire/".
- Opening, verbatim: "Chipotle Mexican Grill (NYSE: CMG) today announced that the first Chipotle restaurant in Mexico will open on Thursday, July 16 in San Pedro Garza García, Nuevo León, part of the Monterrey metropolitan area, in partnership with Alsea (BMV: ALSEA*), a leading restaurant operator in Latin America and Europe. The opening marks a significant milestone in Chipotle's international growth strategy and introduces the company's menu of freshly prepared, customizable burritos, bowls, salads, tacos and quesadillas to guests in Mexico."
- Agreement and plans, verbatim: "This restaurant is the first location to open under the development agreement Chipotle and Alsea announced in April 2025. Building on this market entry, Chipotle and Alsea plan to open additional restaurants in Nuevo León later this year and expand into Mexico City in 2027."
- CEO quote, verbatim: ""We are entering Mexico with deep respect for the country's culinary heritage and a commitment to delivering the Chipotle experience with excellence," said Scott Boatwright, Chief Executive Officer of Chipotle. "Our research has reinforced our belief that there is strong interest in high-quality, freshly prepared food served with the customization and convenience that Chipotle offers. Nuevo León is an ideal place to begin this journey, and with Alsea's operational expertise and deep local market knowledge, we look forward to serving new guests and earning a place in Mexico's vibrant dining culture.""
- Chief Business Development Officer quote, verbatim: ""We've spent years evaluating opportunities to bring Chipotle to Mexico, and this week's opening reinforces our confidence in the market," said Nate Lawton, Chief Business Development Officer of Chipotle. "Our initial focus is on opening one great restaurant and learning alongside our guests and our partners at Alsea. This first location will serve as an important proof-of-concept, giving us the opportunity to better understand local consumer preferences as we thoughtfully grow in Mexico.""
- How the restaurant is run and sourced, verbatim: "The new restaurant features Chipotle's signature menu prepared fresh throughout the day with the same chef-led standards and classic cooking techniques that have shaped the brand since its founding. The company sources many of its ingredients from suppliers throughout the region and remains committed to serving real food made with wholesome ingredients and without artificial colors, flavors, or preservatives." Site choice: "The Monterrey metropolitan area was selected as Chipotle's first location in Mexico due to its strong economy, growing population, and status as one of the country's leading business and innovation hubs. The restaurant represents the first step in Chipotle and Alsea's broader expansion strategy as the companies evaluate opportunities across Mexico's largest metropolitan markets."
- Alsea CEO quote, verbatim: ""Bringing Chipotle to Mexico is an important step in our growth and portfolio diversification strategy. We are introducing an iconic brand with a differentiated value proposition that has resonated with millions of guests around the world, and we are confident it will be warmly welcomed by Mexican consumers. This week's opening reflects our confidence in Mexico's growth potential and our commitment to continuing to drive investment, job creation, and economic development in the communities where we operate," said Christian Gurría, Chief Executive Officer of Alsea."
- International footprint, verbatim: "Chipotle signed its first international development agreement in July 2023 with Alshaya Group to open restaurants in the Middle East. Alshaya Group currently operates 15 restaurants across the UAE, Kuwait and Qatar. In September 2025, Chipotle announced a joint venture with SPC Group, a leading South Korean food and bakery company, to expand the brand into Asia for the first time, with plans to open its first restaurant in South Korea later this year and in Singapore early next year." "Chipotle's existing international portfolio of owned and operated restaurants includes more than 80 locations in Canada, 20 in the U.K., six in France, and two in Germany. The company currently operates more than 4,100 restaurants worldwide and expects to open between 350 and 370 new restaurants in 2026 as it continues to execute its "Recipe for Growth" strategy, including a target of operating 7,000 locations in the U.S. and Canada." "Chipotle's business development group, led by Chief Business Development Officer Nate Lawton, continues to evaluate strategic opportunities to accelerate the company's global growth through partnerships, joint ventures, and development agreements."
- About Alsea, verbatim: "Alsea is the leading restaurant operator in Latin America and Europe of global brands in the quick service, coffee shop and fast casual dining segments. It has a diversified portfolio, with brands such as Domino's Pizza, Starbucks, Burger King, Chili's, P.F. Chang's, Italianni's, The Cheesecake Factory, Vips, Archies, Foster's Hollywood, Gino's and Chipotle. The company operates more than 4,800 units in Mexico, Spain, Argentina, Chile, Colombia, France, Portugal, Netherlands, Belgium, Luxembourg, Uruguay and Paraguay." "*Alsea shares are traded on the Mexican Stock Exchange under the ticker symbol ALSEA".
- Consistency note: the Mexico release's "About Chipotle" repeats the Q1 2026 boilerplate ("over 4,100 restaurants as of March 31, 2026", "over 135,000 employees"), and its "15 restaurants" for Alshaya (as of July 13) agrees with the 15 partner-operated restaurants at Jun. 30, 2026 in the Q2 release unit table, whose one Q2 partner opening therefore predates the Mexico opening of July 16. [IR release 2026-07-13 (Mexico)] [Q2 2026 release, Supplemental Financial and Other Data] The Mexico restaurant is partner-operated (Alsea) and so falls under "Partner-operated restaurants" as defined in [Q2 2026 release, Definitions]; the release does not use the words "franchise" or "license" for the Alsea arrangement, only "development agreement" and "in partnership with".

## 7. What the releases and decks do NOT disclose (writer's checklist)

- Average unit volume for the quarter as a standalone figure: the releases give "Average restaurant sales" (trailing 12 months, $ thousands) in the unit table — 3,102 at Jun. 30, 2026 — but no quarterly AUV, no AUV by cohort or by Chipotlane vs non-Chipotlane, and no AUV in either 2026 deck; the only deck AUV is the FY2025 "$3.1 million" model. [Q2 2026 release, Supplemental Financial and Other Data] [Q4 2025 slides, p.13]
- Number of shares repurchased in the quarter (dollars and average price only); the 10-Q carries the share count (filings gatherer).
- Comparable transactions and check are given only as the two components of the comp; no traffic by daypart, by channel (in-store vs digital) or by region; no menu price increase percentage for any period (the releases say only "the benefit of menu price increases").
- Digital sales split between order-ahead, delivery and third-party aggregators; Rewards member count; the deck says only "Goal: Growing Rewards Participation Beyond 1 in 5 In-Restaurant Customers" and "in-store loyalty comp sales outpacing order-ahead loyalty comp sales since mid-April". [Q1 2026 slides, p.7] [Q2 2026 slides, p.9]
- Q3 2026 guidance of any kind in the releases (comps, margin, G&A, tax): none. The non-GAAP tables PDF says forward-looking adjusted G&A and restaurant level operating margin "for our third quarter 2026" were presented on the call and not reconciled. [Q2 2026 non-GAAP tables, p.1] Full-year revenue, margin, EPS, capex, pre-opening, D&A, interest income, share count and stock-based compensation guidance: none in any of the three releases; the Outlook covers only comps, openings and tax rate. [Q2 2026 release, Outlook]
- Q3 2025 figures: the three releases cover Q4 2025, Q1 2026 and Q2 2026 (with prior-year comparatives), so Q3 2025's income statement and reconciliations are absent; only its unit-table column (84 opened, 3,916 total, ARS 3,132, comps 0.3%) is present. [Q4 2025 release, Supplemental Financial and Other Data]
- Restaurant counts by country or region at Jun. 30, 2026 (the 10-Q has U.S. vs international; filings gatherer). The Mexico release gives approximate counts as of July 13: "more than 80 locations in Canada, 20 in the U.K., six in France, and two in Germany"; Alshaya "15 restaurants across the UAE, Kuwait and Qatar". [IR release 2026-07-13 (Mexico)]
- Chipotlane count at Jun. 30, 2026 (only openings with a Chipotlane per quarter; the last total is 1,326 at year-end 2025). [Q4 2025 slides, p.14]
- Capex guidance, new-restaurant investment cost per unit, cash-on-cash returns (the Q4 deck says only "Central London and Frankfurt cash on cash returns unlocking growth in the region" without numbers). [Q4 2025 slides, p.9]
- Marketing and promotional expense as a line or percentage (inside "Other operating costs"); delivery fees; food-cost inflation percentages (only qualitative: "inflation, primarily from beef and freight"); tariff cost in dollars or basis points (mentioned as a driver only in the Q4 2025 release: "the impact from tariffs enacted in 2025"). [Q2 2026 release, Results] [Q4 2025 release, Results]
- Legal proceedings: the nature of the matters behind the $11,875 thousand Q1 labor accrual and the $10,000 thousand Q2 G&A accrual is not described beyond "legal matters that we expect to exceed typical costs for legal proceedings". [Q1 2026 release, Adjusted Net Income reconciliation] [Q2 2026 release, Adjusted Net Income reconciliation]
- Recipe for Growth restructuring: total expected cost or headcount is not given (only the quarterly amounts, 2,140 in Q1 and 3,346 in Q2, $ thousands). [Q1 2026 release, Adjusted Net Income reconciliation] [Q2 2026 release, Adjusted Net Income reconciliation]
- Employee count is rounded ("nearly 140,000"); no turnover or wage-rate figures beyond "23,000 internal promotions" in 2025. [Q2 2026 release, About Chipotle] [Q4 2025 slides, p.10]
- The HEEP "hundreds of basis points of improvement in comparable sales" is not quantified further, and the slide does not say over what period or against what control group. [Q2 2026 slides, p.6]
- Guidance for the Middle East beyond "nearly double footprint and sales in 2026", and no opening dates for South Korea or Singapore beyond "later this year" and "early next year" (Mexico release, July 2026). [Q4 2025 slides, p.9] [IR release 2026-07-13 (Mexico)]

## 8. Numeric self-check (run 2026-09-08)

- Method: script /tmp/cmg-orch/ir/numcheck.py. Every numeric token in this file (regex `\d[\d,]*(\.\d+)?`) was searched verbatim (as a substring) in the concatenation of the eight cached texts cited above, after removing structural tokens: ISO dates, "Month D, YYYY" and "D Month YYYY" dates, EDGAR accession numbers and timestamps, CIK, page and PDF-page references (p.N, pp.N–N), form names (8-K, 10-Q, 10-K, EX-99.1), quarter and half labels (Q1–Q4, H1, FY2024–FY2026), stand-alone years 1993–2027, markdown heading numbers and the section numbers used in tags (§N.N).
- Lines carrying "(computed)" or "(from slide image" were checked separately; misses on those lines are the gatherer's derived values and are listed in `MANIFEST-ir.md`.
- Result: unlabelled lines 1418 tokens checked, 1418 found, 0 misses. Lines labelled "(computed)" or "(from slide image": 116 tokens checked, 103 found, 13 not found; the 13 are the gatherer's own derived values: 8.4, 72.6, 74.8, 4,104, 4,201, 1,331.5, 810,490, 934,402, 1,003,481, 1,281,623, 1,447,590, 2,320,782. (computed)
- Image-page verification: tesseract OCR at 300 dpi of the six image-only reconciliation pages (Q2 deck pp.13–15, Q1 deck pp.13–15) and the Q4 deck's pp.19–20, digits compared after stripping punctuation: 54 of 54, 55 of 55 and 97 of 97 numbers matched the corresponding release tables. Q4 deck chart pages 5, 13 and 14 are text-layer pages (every data label is in `slides-2025-Q4.txt`); OCR of the same pages confirmed 21 of 30, 8 of 11 and 27 of 28 labels (the OCR misses are tesseract failures on small chart labels, not discrepancies; the text layer is authoritative). (computed)
