# Pinterest, Inc. (PINS) — Filings notes, as of Q2 2026

_Gatherer: filings. As-of cutoff 2026-08-04 (10-Q and call both dated 2026-08-04). Written 2026-09-07. Structured facts only; no interpretation._
_Dollar figures are USD thousands where taken from financial statements and notes (the company's own unit), and USD millions where the company states them that way in MD&A prose; each table says which. Fiscal year = calendar year. Numbers marked "(computed)" are arithmetic on disclosed figures, not disclosed as such. "Not in fetched sources" means the fetched filings do not contain the figure in text form._

**Tag key**
- `[10-K FY2025, ...]` = Annual report for FY2025, filed 2026-02-12 → `10-K-FY2025.txt`
- `[10-K FY2024, ...]` = Annual report for FY2024, filed 2025-02-06 → `10-K-FY2024.txt` (fetched in addition to the orchestrator's list, to fill FY2024 user-geography revenue, ARPU, MAUs and headcount)
- `[10-K FY2023, ...]` = Annual report for FY2023, filed 2024-02-08 → `10-K-FY2023.txt` (FY2021–FY2023 statements)
- `[10-K FY2022, ...]` = Annual report for FY2022, filed 2023-02-06 → `10-K-FY2022.txt` (fetched in addition, for FY2022 user-geography revenue, ARPU, MAUs, headcount and the 12/31/2021 balance sheet)
- `[10-Q Q2 2026, ...]` = Quarterly report for the quarter ended 2026-06-30, filed 2026-08-04 → `10-Q-2026-Q2.txt`
- `[DEF 14A 2026, <section>]` = Proxy statement filed 2026-04-08 (annual meeting 2026-05-21) → `DEF14A-2026.txt`
- `[8-K YYYY-MM-DD]` = Current report filed on that date → `8-K-YYYY-MM-DD.txt`

**Important limitation of the text sources.** In every Pinterest 10-K and 10-Q the quarterly tables of MAUs, revenue and ARPU by geography (U.S. and Canada / Europe / Rest of World) are embedded as chart images. The text extraction keeps only the chart titles and footnotes, not the numbers. What survives in text is: (a) year-end global MAUs and annual ARPU by region in the MD&A prose, (b) annual revenue by user geography in the MD&A "Revenue" paragraph, (c) the quarter and six-month figures for the same in the 10-Q prose, and (d) revenue by customer billing address in the geography note. Regional MAUs for any period are therefore "not in fetched sources"; the IR gatherer's press release tables are the place to get them.

---

## 1. Business description in the company's own words

- "Pinterest is an AI-powered visual search and discovery platform, positioned at the intersection of search, social, and commerce. We offer a unique and differentiated experience that enables people to go from inspiration to action all on one consumer internet property. Pinterest can be accessed through our mobile application or the web." [10-K FY2025, Item 1]
- "People use Pinterest to find useful, relevant ideas—and then bring them to life. People don't always have the words to describe what they're looking for, but often know it when they see it. As they browse Pinterest content (called "Pins"), they fine-tune their tastes and find the perfect idea... This happens at a massive scale, with billions of searches and saves per month, with the vast majority of queries being visual." [10-K FY2025, Item 1]
- Mission: "our mission of bringing everyone the inspiration to create a life they love". [10-K FY2025, Item 1 (Talent management)] Also stated as "Our mission—to bring everyone the inspiration to create a life they love—and company values are integral to everything we do." [10-K FY2025, Item 1A]
- Users: "619 million monthly active users from around the world come to Pinterest to find new ideas, curate and refine their tastes, and turn those ideas into reality. Our platform particularly resonates with women, who comprise roughly two-thirds of our total user base. In addition, our platform also resonates with the younger generation, as Gen Z users represent over 50% of our user base. Geographically, we have a diverse user set, representing over 100 countries globally." [10-K FY2025, Item 1] The filings use the word "users" (not "Pinners"); "Pinners" does not appear in the 10-K or 10-Q. [10-K FY2025; 10-Q Q2 2026]
- Content sources: "retailers, brands, creators, publishers and users"; formats "images... videos... collages... and products that brands and merchants upload from catalogs." [10-K FY2025, Item 1]
- Surfaces: Home Feed, Search Page ("over 90% of our searches are unbranded"), Related Pins, Boards. Data asset: "This curation activity generates signals across a network of many billions of associations between Pins, searches, boards, products and users on our platform. Together, these connections comprise our valuable Taste Graph". [10-K FY2025, Item 1]
- Flywheel: "We believe that in-market consumers on Pinterest tend to be early in their journey toward a purchase decision and do not yet know exactly what they want to purchase. Accordingly, we believe that they are open to discovering new products and brands on Pinterest rather than merely navigating to brands they already know, as is common on traditional search engines and e-commerce platforms. This creates a unique flywheel where relevant ads can not only enhance the user experience but also drive more value for advertisers". [10-K FY2025, Item 1]
- How advertisers are described: "AI also plays a central role in how we drive value for our advertisers, who come to Pinterest to reach our users with high commercial intent. The inspiration-to-action journey on Pinterest aligns with the advertiser marketing funnel, allowing us to help brands reach customers at every stage, from discovery to purchase, through digital ads." [10-K FY2025, Item 1]
- Ad formats listed: Standard ad, Video ad, Shopping ad ("promote specific products in their catalogs"), Carousel ad, Collection ad, Interactive ad, Premier Spotlight ad ("exclusive placements on the Pinterest Home Feed and search page"), Idea ad. Many formats carry "mobile deep links and/or direct link capabilities for a seamless, one-click handoff from an ad to the advertiser's mobile app or webpage, and increasingly, in-app purchase experiences." [10-K FY2025, Item 1]
- Auction and objectives: "The vast majority of our advertisers buy ads through an auction-based system... Upper funnel "brand" revenue is billed when an advertiser optimizes an ad campaign around "brand" objectives like impressions ("CPM") or video views ("CPV"). Lower funnel revenue is billed when an advertiser optimizes an ad campaign around "performance" objectives like clicks ("CPC"), actions ("CPA") or conversion events ("oCPM"), such as a checkout or add-to-cart. Our auction system selects the best ad for each available ad impression, based on the likelihood of a desired action occurring and how much that action is worth to advertisers." [10-K FY2025, Item 1]
- Campaign tools: Ads Manager, Pinterest API, "our AI-enabled campaign solution, Pinterest Performance+, which streamlines setup and drives performance through automated features such as targeting, bidding and creative optimization." Measurement: "Our first-party measurement solutions, including our Conversions API and clean rooms". [10-K FY2025, Item 1]
- Go-to-market: "advertisers across multiple verticals including retail, consumer packaged goods, financial services, technology and entertainment, travel and auto... The majority of our advertisers utilize our Ads Manager platform to initiate and manage their campaigns. We also have a global sales force presence who work directly with advertisers and ad agencies... In some geographies, we work with other third parties to support our sales efforts." [10-K FY2025, Item 1] International: "we are working to partner with local third-party sales organizations, which we refer to as resellers." [10-K FY2025, Item 1A]
- User acquisition: "We grow our global user base organically through the strength of our global brand, the utility of our service and unpaid traffic from search engines. In addition, we use paid marketing to grow and retain our user base". [10-K FY2025, Item 1]
- Third-party ad demand partnerships: the filings do not name any partner. Wording used: "a portion of our revenue is derived from partnerships with third-party advertising platforms. We may be unable to maintain these partnerships or identify and secure new partnerships on commercially reasonable terms. In addition, we may be exposed to reputational and other risks arising from our business association with these partners." [10-K FY2025, Item 1A] Risk list item: "if our partnerships for third-party advertisement demand do not yield expected business impact". [10-K FY2025, Item 1A] Accounting: "For revenue generated from arrangements that involve third parties, we evaluate whether it is appropriate to recognize revenue on a gross or net basis based upon which party obtains control of the specified goods or services before they are transferred to the customer." [10-K FY2025, Note 1] Cost of revenue includes "payments associated with partner arrangements". [10-K FY2025, Item 7] Amazon and Google appear in the 10-K only as competitors, as search/login/browser platforms, and (Amazon Web Services) as the cloud host. [10-K FY2025, Item 1; Item 1A]
- Connected TV (new in 2026): "We generate revenue by delivering ads on our website, mobile application and connected TV platforms." [10-Q Q2 2026, Note 1] The tvScientific acquisition "will extend our AI-powered performance advertising from mobile to connected TV." [10-Q Q2 2026, Note 3]
- Segment: "We operate as a single operating segment. Our chief operating decision maker is our Chief Executive Officer ("CEO"), who reviews financial information presented on a consolidated basis, accompanied by disaggregated information about our revenue". [10-K FY2025, Note 1; same wording 10-Q Q2 2026, Note 1]
- Competition: "We primarily compete with consumer internet companies that are either tools (search, ecommerce) or media (newsfeeds, video, social networks), particularly ones focused on advertising. Competitors such as Amazon, Meta (including Facebook, Instagram, Threads and MetaAI), Google (including Gemini, Lens and YouTube), OpenAI (including ChatGPT), Snap, Reddit, TikTok and X, many of which are larger and have significantly greater financial and human resources, offer users engaging content and commerce opportunities through similar technology or products to ours." [10-K FY2025, Item 1]
- Technology: "We believe we have one of the largest image-rich data sets ever assembled." Patents: "approximately 400 issued patents and pending patent applications"; "over 660 registered trademarks and trademark applications" as of 12/31/2025. [10-K FY2025, Item 1]
- Seasonality: "We have historically experienced seasonality in monthly active user growth, monetization on our platform and free cash flow. Historically, we have had lower sequential user growth in the second quarter. Industry advertising spend tends to be strongest in the fourth quarter resulting in higher revenue in the fourth quarter, and free cash flow is historically higher in the first quarter as we collect on the fourth quarter's higher revenue. We expect this seasonality to continue." [10-K FY2025, Item 1]
- History markers in filings: incorporated in Delaware 2008; IPO trading began April 18, 2019; Silbermann CEO 2008–June 2022; Ready CEO since 2022. [10-K FY2025, Note 1; Item 5; DEF 14A 2026, Our board of directors]
- Properties: HQ San Francisco ~120,000 sq ft leased; total offices ~604,000 sq ft as of 12/31/2025. [10-K FY2025, Item 2]

## 2. Revenue by geography

Pinterest reports geography two ways. (a) MD&A "revenue by user geography" (where the user was when the revenue-generating activity happened) is the basis for ARPU; it appears in text only as annual/quarterly totals in prose (USD millions). (b) The notes disaggregate revenue by customer billing address (USD thousands). The two do not match by design. [10-K FY2025, Item 7 (Trends in monetization metrics, footnote to chart); Note 11]

### 2a. Revenue by user geography, fiscal years (USD millions, as stated in MD&A prose)

| Region | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| U.S. and Canada | not in fetched sources | 2,309.3 | 2,447.3 | 2,884.0 | 3,173.1 |
| Europe | not in fetched sources | 397.9 | 483.4 | 593.2 | 775.0 |
| Rest of World | not in fetched sources | 95.3 | 124.4 | 168.9 | 273.6 |
| Total revenue (statements, converted to millions; computed) | 2,578.0 | 2,802.6 | 3,055.1 | 3,646.2 | 4,221.8 |
| Growth: US&C / Europe / RoW | n/a | +8% / +4% / +52% | +6% / +21% / +31% | +18% / +23% / +36% | +10% / +31% / +62% |

- FY2022: [10-K FY2022, Item 7 (Revenue)]. FY2023: [10-K FY2023, Item 7 (Revenue)]. FY2024: [10-K FY2024, Item 7 (Revenue)]. FY2025: [10-K FY2025, Item 7 (Revenue)]. Regions sum to within $0.1 million of the reported totals (computed), consistent with the company's rounding note.
- FY2021 by-region figures exist only as a chart image in the FY2022 10-K (the region split was introduced in Q1 2022: "Beginning in the first quarter of 2022, we updated the presentation of our key metrics by presenting U.S. and Canada, Europe and Rest of World separately... For comparability, we provided revenue, MAUs and ARPU data from the fourth quarter of 2020 to the fourth quarter of 2021 on the same basis."). [10-K FY2022, Item 7]
- FY2025: "Revenue based on our estimate of the geographic location of our users increased by 10% in the U.S. and Canada to $3,173.1 million, Europe revenue increased by 31% to $775.0 million and Rest of World revenue increased by 62% to $273.6 million". [10-K FY2025, Item 7]
- Note on Europe: "Europe includes Russia and Turkey for our reporting of Revenue, MAUs and ARPU by geographic region." [10-K FY2025, Item 7]

### 2b. Revenue by user geography, Q2 and six months (USD millions)

| Region | Q2 2025 | Q2 2026 | Q2 growth | 6M 2025 | 6M 2026 | 6M growth |
|---|---|---|---|---|---|---|
| U.S. and Canada | not stated | 879.9 | +18% | not stated | 1,630.3 | +16% |
| Europe | not stated | 212.7 | +12% | not stated | 398.3 | +18% |
| Rest of World | not stated | 87.0 | +38% | not stated | 158.5 | +47% |
| Total revenue (statements, converted to millions; computed) | 998.2 | 1,179.7 | +18% | 1,853.2 | 2,187.2 | +18% |

- "Revenue based on our estimate of the geographic location of our users increased by 18% and 16% in U.S. and Canada to $879.9 million and $1,630.3 million, Europe revenue increased by 12% and 18% to $212.7 million and $398.3 million, and Rest of World revenue increased by 38% and 47% to $87.0 million and $158.5 million for the three and six months ended June 30, 2026 compared to the three and six months ended June 30, 2025, respectively." [10-Q Q2 2026, Item 2] Prior-year regional dollar amounts are not stated in the 10-Q text (chart only).
- Constant currency: Q2 2026 revenue +18% reported, +17% constant currency ($1,169.3 million; $10.4 million favorable FX); 6M +18% reported, +16% constant currency ($2,153.6 million; $33.6 million favorable FX). FY2025 +16% reported, +15% constant currency ($4,205.3 million; $16.5 million favorable). [10-Q Q2 2026, Item 2; 10-K FY2025, Item 7]

### 2c. Revenue by customer billing address (USD thousands, from the geography notes)

| Region | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | Q2 2025 | Q2 2026 | 6M 2025 | 6M 2026 |
|---|---|---|---|---|---|---|---|---|---|
| U.S. and Canada | 2,109,089 | 2,264,640 | 2,350,188 | 2,739,887 | 3,052,639 | 721,801 | 842,607 | 1,353,935 | 1,560,055 |
| of which United States (USD millions, as stated in the footnote) | 2,003.6 | 2,144.3 | 2,226.3 | 2,612.1 | 2,912.0 | 689.4 | 800.5 | 1,293.9 | 1,484.5 |
| Europe | 384,657 | 410,516 | 501,290 | 601,187 | 779,092 | 189,620 | 223,428 | 336,796 | 415,524 |
| Rest of World | 84,281 | 127,418 | 203,593 | 305,092 | 390,036 | 86,806 | 113,619 | 162,484 | 211,589 |
| Total | 2,578,027 | 2,802,574 | 3,055,071 | 3,646,166 | 4,221,767 | 998,227 | 1,179,654 | 1,853,215 | 2,187,168 |

- FY2021–FY2023: [10-K FY2023, Note 12]. FY2023–FY2025: [10-K FY2025, Note 11]. Quarters: [10-Q Q2 2026, Note 10]. United States amounts are given in the footnotes in millions ("$2,912.0 million, $2,612.1 million and $2,226.3 million"; "$800.5 million and $689.4 million... $1,484.5 million and $1,293.9 million"); FY2021–FY2022 U.S. amounts "$2,144.3 million and $2,003.6 million" are from [10-K FY2023, Note 12]. "No individual country other than the United States exceeded 10% of our total revenue for any period presented." [10-K FY2025, Note 11; 10-Q Q2 2026, Note 10]
- Revenue by channel or customer type (e.g., managed vs. self-serve, large vs. SMB): not disclosed in any fetched filing. The only split given is by objective in prose: FY2025 growth "primarily due to growth in demand from our conversion and awareness objectives"; FY2024 "consideration and conversion objectives"; FY2023 "awareness and conversion objectives"; Q2 2026 "conversion and consideration objectives". [10-K FY2025, Item 7; 10-K FY2024, Item 7; 10-K FY2023, Item 7; 10-Q Q2 2026, Item 2]
- Volume and price: ads served vs. price of ads, year over year: FY2022 +17% / −7%; FY2023 +31% / −17%; FY2024 +39% / −14%; FY2025 +49% / −22%; Q2 2026 +16% / +1%; 6M 2026 +20% / −2%. [10-K FY2022, Item 7; 10-K FY2023, Item 7; 10-K FY2024, Item 7; 10-K FY2025, Item 7; 10-Q Q2 2026, Item 2]
- Deferred revenue: $23.4 million (12/31/2024), $47.5 million (12/31/2025), $93.5 million (6/30/2026); "We expect materially all of our deferred revenue to be recognized in the subsequent quarter." [10-K FY2025, Note 1; 10-Q Q2 2026, Note 1]

## 3. Monthly Active Users (MAUs)

- Definition (verbatim, unchanged across FY2022–FY2025 10-Ks and the 10-Q): "We define an MAU as an authenticated Pinterest user who visits our website, opens our mobile application or interacts with Pinterest through one of our browser or site extensions, such as the Save button, at least once during the 30-day period ending on the date of measurement. The number of MAUs does not include Shuffles users unless they would otherwise qualify as MAUs. We present MAUs based on the number of MAUs measured on the last day of the current period. We calculate average MAUs based on the average of the number of MAUs measured on the last day of the current period and the last day prior to the beginning of the current period. MAUs are the primary metric by which we measure the scale of our active user base." [10-K FY2025, Item 7; 10-Q Q2 2026, Item 2]
- Counting caveats (verbatim): "Our MAU metrics may also be impacted by our information quality efforts, which are our overall efforts to reduce malicious activity on our platform, including false, spam and malicious automation accounts in existence on our platform. We make efforts to regularly deactivate false, spam and malicious automation accounts that violate our terms of service and exclude these users from the calculation of our MAU metrics; however, we will not succeed in identifying and removing all false, spam and malicious accounts from our platform... In addition, users are not prohibited from having more than one account on our platform, and we treat multiple accounts held by a single person as multiple users for purposes of calculating our active users." "These metrics are calculated using internal company data and have not been validated by an independent third party." "We have in the past implemented, and may from time to time in the future implement, new methodologies for calculating these metrics". Geography is estimated: "our data regarding the geographic location of users and revenue by user geography is estimated based on a number of factors, which may not always accurately reflect the actual location". [10-K FY2025, Item 1A]
- Daily users: "Our growth efforts are not currently focused on increasing the number of daily active users, and we do not anticipate that most of our users will become daily active users." [10-K FY2025, Item 1A]

| Date | Global MAUs (millions) | YoY | WAU/MAU ratio |
|---|---|---|---|
| 12/31/2021 | not in fetched sources (FY2022 10-K gives only "+4%" for 2022) | n/a | not in fetched sources |
| 12/31/2022 | 450 | +4% | 61% |
| 12/31/2023 | 498 | +11% | 61% |
| 12/31/2024 | 553 | +11% | 62% |
| 12/31/2025 | 619 | +12% | 62% |
| 6/30/2025 | not stated in text (10-Q gives only "+11%" for 6/30/2026) | n/a | not stated |
| 6/30/2026 | 640 | +11% | not stated |

- [10-K FY2022, Item 7]; [10-K FY2023, Item 7]; [10-K FY2024, Item 7]; [10-K FY2025, Item 7]; [10-Q Q2 2026, Item 2]. WAU definition: "an authenticated Pinterest user who visits our website, opens our mobile application or interacts with Pinterest through one of our browser or site extensions, such as the Save button, at least once during the seven-day period ending on the date of measurement." [10-K FY2025, Item 7]
- Regional MAUs (U.S. and Canada, Europe, Rest of World) for every period: **not in fetched sources** (chart images only). Average-MAU growth used in the revenue bridge: FY2022 −1%; FY2023 +8%; FY2024 +11%; FY2025 +11%; Q2 2026 +11%; 6M 2026 +11%. FY2022 also states "a 6% decrease in average U.S. and Canada MAUs". [10-K FY2022, Item 7; 10-K FY2023, Item 7; 10-K FY2024, Item 7; 10-K FY2025, Item 7; 10-Q Q2 2026, Item 2]
- Drivers as stated: 12/31/2025 and 12/31/2024 "increased... primarily due to our ongoing investments in relevance and personalization"; 12/31/2023 "primarily due to our investments in relevance and personalization beginning in the second quarter of 2022"; 12/31/2022 increased "as the negative impacts on user growth from the COVID-19 pandemic unwind and the November 2021 changes in search engine algorithms have subsided." [10-K FY2025; 10-K FY2024; 10-K FY2023; 10-K FY2022, Item 7]

## 4. ARPU (average revenue per user)

- Definition (verbatim): "We define ARPU as our total revenue in a given geography during a period divided by average MAUs in that geography during the period. We calculate ARPU by geography based on our estimate of the geography in which revenue‑generating activities occur. We present ARPU on a U.S. and Canada, Europe and Rest of World basis because we currently monetize users in different geographies at different average rates. Our ARPU in U.S. and Canada and, to a lesser extent, Europe is higher primarily due to the relative size and maturity of the digital advertising markets in these geographies." [10-K FY2025, Item 7; 10-Q Q2 2026, Item 2]

| Period | Global | U.S. and Canada | Europe | Rest of World |
|---|---|---|---|---|
| FY2021 | not in fetched sources | not in fetched sources | not in fetched sources | not in fetched sources |
| FY2022 | $6.36 (+10%) | $24.38 (+16%) | $3.23 (+7%) | $0.43 (+49%) |
| FY2023 | $6.44 (+1%) | $25.52 (+5%) | $3.73 (+15%) | $0.50 (+17%) |
| FY2024 | $6.94 (+8%) | $29.15 (+14%) | $4.24 (+14%) | $0.59 (+18%) |
| FY2025 | $7.21 (+4%) | $30.84 (+6%) | $5.12 (+21%) | $0.83 (+40%) |
| Q2 2026 (three months) | $1.86 (+7%) | $8.30 (+14%) | $1.35 (+4%) | $0.23 (+21%) |

- [10-K FY2022, Item 7]; [10-K FY2023, Item 7]; [10-K FY2024, Item 7]; [10-K FY2025, Item 7]; [10-Q Q2 2026, Item 2]. Percentages are year over year as stated by the company. Q2 2025 and six-month ARPU values are not stated in the 10-Q text (chart only). FY2021 values could be derived from the FY2022 growth rates but that would be an estimate, so they are left blank.
- FY2025 verbatim: "For the year ended December 31, 2025, global ARPU was $7.21, which represents an increase of 4% compared to the year ended December 31, 2024. For the year ended December 31, 2025, U.S. and Canada ARPU was $30.84, an increase of 6%, Europe ARPU was $5.12, an increase of 21%, and Rest of World ARPU was $0.83, an increase of 40%". [10-K FY2025, Item 7]
- Q2 2026 verbatim: "For the three months ended June 30, 2026, global ARPU was $1.86, which represents an increase of 7% compared to the three months ended June 30, 2025. For the three months ended June 30, 2026, U.S. and Canada ARPU was $8.30, an increase of 14%, Europe ARPU was $1.35, an increase of 4%, and Rest of World ARPU was $0.23, an increase of 21%". [10-Q Q2 2026, Item 2]
- "We use MAUs and ARPU to assess the growth and health of the overall business and believe that these metrics best reflect our ability to attract, retain, engage and monetize our users, and thereby drive revenue." [10-K FY2025, Item 7]

## 5. Income statement (USD thousands except per share and %)

### 5a. Fiscal years

| Line | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| Revenue | 2,578,027 | 2,802,574 | 3,055,071 | 3,646,166 | 4,221,767 |
| Cost of revenue | 529,320 | 678,597 | 688,760 | 750,355 | 841,521 |
| Gross profit (computed) | 2,048,707 | 2,123,977 | 2,366,311 | 2,895,811 | 3,380,246 |
| Gross margin (computed) | 79.5% | 75.8% | 77.5% | 79.4% | 80.1% |
| Research and development | 780,264 | 948,980 | 1,068,416 | 1,240,564 | 1,427,447 |
| Sales and marketing | 641,279 | 933,133 | 911,166 | 1,011,772 | 1,166,705 |
| General and administrative | 300,977 | 343,541 | 512,407 | 463,658 | 466,211 |
| Total costs and expenses | 2,251,840 | 2,904,251 | 3,180,749 | 3,466,349 | 3,901,884 |
| Income (loss) from operations | 326,187 | (101,677) | (125,678) | 179,817 | 319,883 |
| Operating margin (company: FY2023–FY2025; computed: FY2021–FY2022) | 12.7% | (3.6%) | (4)% | 5% | 8% |
| Interest income (expense), net | 3,075 | 30,235 | 105,439 | 127,003 | 110,493 |
| Other income (expense), net | (8,291) | (14,502) | 3,799 | (19,215) | 15,514 |
| Income (loss) before taxes | 320,971 | (85,944) | (16,440) | 287,605 | 445,890 |
| Provision for (benefit from) income taxes | 4,533 | 10,103 | 19,170 | (1,574,501) | 29,035 |
| Net income (loss) | 316,438 | (96,047) | (35,610) | 1,862,106 | 416,855 |
| Diluted EPS ($) | 0.46 | (0.14) | (0.05) | 2.67 | 0.61 |
| Weighted-average shares, basic (thousands) | 640,030 | 665,732 | 674,641 | 678,831 | 674,706 |
| Weighted-average shares, diluted (thousands) | 691,651 | 665,732 | 674,641 | 698,376 | 687,771 |
| Depreciation and amortization (cash flow statement) | 27,500 | 46,489 | 21,509 | 21,266 | 25,151 |
| Adjusted EBITDA (current definition) | not restated in fetched sources | 461,423 | 707,594 | 1,032,315 | 1,269,976 |
| Adjusted EBITDA (definition in force at the time) | 814,369 | 441,935 | 683,463 | — | — |

- FY2021–FY2023 statement lines: [10-K FY2023, Item 8 (Consolidated statements of operations)]. FY2023–FY2025: [10-K FY2025, Item 8]. Percent-of-revenue rows as stated: FY2023 (4)%, FY2024 5%, FY2025 8% operating margin; cost of revenue 23% / 21% / 20%; R&D 35% / 34% / 34%; S&M 30% / 28% / 28%; G&A 17% / 13% / 11%. [10-K FY2025, Item 7] FY2021–FY2022 as stated: cost of revenue 21% / 24%; R&D 30% / 34%; S&M 25% / 33%; G&A 12% / 12%; operating margin 13% / (4)%. [10-K FY2023, Item 7]
- Adjusted EBITDA definitions: the current definition (in force since Q4 2024) excludes payroll tax on share-based compensation; FY2022 and FY2023 restated values 461,423 and 707,594 are from [10-K FY2024, Item 7] and [10-K FY2025, Item 7]. The older figures 814,369 (FY2021), 441,935 (FY2022) and 683,463 (FY2023) are under the prior definition. [10-K FY2023, Item 7] FY2021 was not restated in any fetched filing.
- FY2024 tax benefit: "The tax benefit during the year ended December 31, 2024 was primarily due to the release of our valuation allowance on our U.S. federal and state, excluding California, deferred tax assets." Amount: "Provision for (benefit from) income taxes includes $1,597.0 million related to the release of our valuation allowance on our U.S. federal and state, excluding California, deferred tax assets during the fourth quarter of 2024." Rate reconciliation line "Change in valuation allowance (1,421,323)" for FY2024 vs +111,497 for FY2023; deferred federal benefit (1,434,298) and state (162,684). [10-K FY2025, Item 7; Note 10] FY2024 10-K wording: "The primary difference between our benefit from income taxes and the expected tax at the US federal statutory rate is the release of our valuation allowance on our U.S. federal and state, excluding California, deferred tax assets for the year ended December 31, 2024." [10-K FY2024, Note 10]
- FY2025 effective tax rate 7%: tax at 21% statutory 93,637; state +13,203 (3 pts); R&D credit (76,612) (−17 pts); share-based compensation (4,606). "The primary difference between our effective tax rate and the U.S. federal statutory rate is the research and development credit partially offset by state tax expense". [10-K FY2025, Note 10]
- FY2023 one-offs: restructuring charges $126.9 million (office-space impairment/abandonment $117.3 million in G&A, severance $9.6 million across lines); workforce reduction ~4% (March 2023 plan, completed Q3 2023). [10-K FY2023, Item 7; Note 13]
- FY2024 one-off: "On November 1, 2024, we reached a settlement to resolve pending litigation relating to allegations concerning the early development of Pinterest. We recorded legal settlement expense of $34.7 million, net of insurance proceeds". [10-K FY2025, Item 7]
- FY2025 cost commentary: cost of revenue +$91.2 million "primarily due to increased users and engagement"; R&D +$186.9 million "primarily due to an 18% increase in personnel expenses due to higher headcount, a $70.1 million increase in share-based compensation expense and a $10.8 million increase in allocated facilities costs"; S&M +$154.9 million ("19% increase in personnel expenses... $27.4 million increase in share-based compensation... $23.9 million increase in outsourced services costs, a $12.6 million increase in marketing expenses"); G&A +$2.6 million ("$13.5 million in non-cash charitable contributions and a $12.4 million increase in share-based compensation expense, offset by a $34.7 million legal settlement... in 2024"). [10-K FY2025, Item 7]
- FY2023 cost of revenue commentary: "+$10.2 million... primarily due to higher absolute hosting costs due to higher compute utilization offset by infrastructure efficiency initiatives." [10-K FY2023, Item 7]
- Non-cash charitable contributions (stock donated): FY2021 45,300; FY2022 0; FY2023 12,890; FY2024 0; FY2025 13,495; 6M 2026 12,198. [10-K FY2023, Item 8; 10-K FY2025, Item 8; 10-Q Q2 2026, Item 1]
- Advertising expense (in S&M): $145.6 million (FY2023), $161.5 million (FY2024), $168.8 million (FY2025). [10-K FY2025, Note 1]

### 5b. Share-based compensation by line (USD thousands)

| Line | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | Q2 2025 | Q2 2026 | 6M 2025 | 6M 2026 |
|---|---|---|---|---|---|---|---|---|---|
| Cost of revenue | 7,438 | 7,629 | 11,117 | 14,836 | 19,541 | 4,983 | 8,484 | 9,055 | 13,046 |
| Research and development | 309,715 | 324,161 | 422,964 | 497,442 | 567,571 | 145,939 | 212,537 | 265,421 | 353,213 |
| Sales and marketing | 52,691 | 99,467 | 96,798 | 122,149 | 149,565 | 38,715 | 52,155 | 69,046 | 91,099 |
| General and administrative | 45,538 | 65,866 | 116,981 | 131,368 | 143,786 | 37,597 | 46,553 | 71,138 | 84,492 |
| Restructuring | — | — | — | — | — | — | 4,788 | — | 14,113 |
| Total | 415,382 | 497,123 | 647,860 | 765,795 | 880,463 | 227,234 | 324,517 | 414,660 | 555,963 |
| SBC / revenue (computed) | 16.1% | 17.7% | 21.2% | 21.0% | 20.9% | 22.8% | 27.5% | 22.4% | 25.4% |

- FY2021–FY2023: [10-K FY2023, Item 7]. FY2023–FY2025: [10-K FY2025, Note 8]. Quarters: [10-Q Q2 2026, Note 7].
- Unrecognized share-based compensation: $1,128.1 million over 2.2 years (12/31/2023); $1,080.6 million over 1.9 years (12/31/2025); $1,443.8 million over 2.1 years (6/30/2026). [10-K FY2023, Note 9; 10-K FY2025, Note 8; 10-Q Q2 2026, Note 7]
- Q2 2026 R&D commentary: "$66.6 million and $87.8 million respective increases in share-based compensation expense and 15% increases in personnel expenses primarily due to higher headcount". [10-Q Q2 2026, Item 2]

### 5c. Q2 2026 vs Q2 2025 and six months (USD thousands)

| Line | Q2 2025 | Q2 2026 | 6M 2025 | 6M 2026 |
|---|---|---|---|---|
| Revenue | 998,227 | 1,179,654 | 1,853,215 | 2,187,168 |
| Cost of revenue | 203,009 | 257,354 | 402,279 | 495,906 |
| Gross profit (computed) | 795,218 | 922,300 | 1,450,936 | 1,691,262 |
| Gross margin (computed) | 79.7% | 78.2% | 78.3% | 77.3% |
| Research and development | 359,624 | 451,010 | 691,289 | 831,799 |
| Sales and marketing | 313,075 | 374,273 | 566,995 | 692,124 |
| General and administrative | 126,849 | 137,880 | 232,459 | 241,397 |
| Restructuring | — | 14,335 | — | 61,432 |
| Total costs and expenses | 1,002,557 | 1,234,852 | 1,893,022 | 2,322,658 |
| Loss from operations | (4,330) | (55,198) | (39,807) | (135,490) |
| Operating margin (company) | —% | (5)% | (2)% | (6)% |
| Interest income (expense), net | 28,022 | 7,334 | 55,315 | 25,120 |
| Other income (expense), net | 10,960 | (1,295) | 15,479 | (2,289) |
| Income (loss) before taxes | 34,652 | (49,159) | 30,987 | (112,659) |
| Provision for (benefit from) income taxes | (4,103) | (2,490) | (16,690) | 7,597 |
| Net income (loss) | 38,755 | (46,669) | 47,677 | (120,256) |
| Diluted EPS ($) | 0.06 | (0.08) | 0.07 | (0.20) |
| Weighted-average shares, basic / diluted (thousands) | 676,852 / 689,837 | 562,913 / 562,913 | 676,688 / 689,598 | 599,629 / 599,629 |
| Depreciation and amortization (Adj. EBITDA reconciliation) | 6,090 | 10,216 | 11,938 | 17,668 |
| Adjusted EBITDA | 250,776 | 311,307 | 422,425 | 517,817 |

- [10-Q Q2 2026, Item 1 (Condensed consolidated statements of operations); Item 2 (Results of operations)]. Percent-of-revenue rows as stated: cost of revenue 20% → 22% (Q2), 22% → 23% (6M); R&D 36% → 38%, 37% → 38%; S&M 31% → 32% both; G&A 13% → 12%, 13% → 11%; restructuring 1% (Q2), 3% (6M). [10-Q Q2 2026, Item 2]
- Six-month D&A per cash flow statement is 20,611 (2026) vs 11,938 (2025); the Adjusted EBITDA reconciliation's 17,668 "Excludes... amortization expense of $1.6 million and $2.9 million for the three and six months ended June 30, 2026, respectively included in restructuring charges." [10-Q Q2 2026, Item 1; Item 2]
- Cost of revenue Q2 2026 +$54.3 million, 6M +$93.6 million, "primarily due to increased users and engagement." [10-Q Q2 2026, Item 2]
- S&M Q2 2026 +$61.2 million: "$18.3 million and $34.4 million respective increases in marketing expenses, 14% and 17% increases in personnel expenses primarily due to higher headcount, $13.4 million and $22.1 million increases in share-based compensation expense and, for the six months ended June 30, 2026, a $22.3 million increase in outsourced services costs." [10-Q Q2 2026, Item 2]
- G&A: 6M 2026 includes "a $15.4 million decrease in non-income based tax benefit related to the repeal of Canada's digital services tax." [10-Q Q2 2026, Item 2]
- Interest and other income fell $32.9 million (Q2) "primarily due to lower invested balances and returns on our cash equivalents and marketable securities as well as lower foreign currency exchange gains." Interest expense on the convertible notes "was not material". [10-Q Q2 2026, Item 2; Note 5]
- Taxes: Q2 2026 benefit "primarily due to tax benefits from our net loss"; 6M 2026 provision "primarily due to tax deficiencies from shared-based compensation"; 2025 benefits "primarily due to excess tax benefits from share-based compensation." [10-Q Q2 2026, Item 2]

## 6. Cash flow, capex, free cash flow, cash and debt

### 6a. Cash flow (USD thousands)

| Item | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | 6M 2025 | 6M 2026 |
|---|---|---|---|---|---|---|---|
| Net cash provided by operating activities | 752,907 | 469,202 | 612,961 | 964,594 | 1,284,264 | 571,399 | 620,908 |
| Purchases of property and equipment (capex) | (9,031)* | (28,984)* | (8,063) | (24,606) | (32,375) | (18,299) | (39,293) |
| Free cash flow (company-defined: OCF − capex) | 743,876 (computed) | 440,218 (computed) | 604,898 | 939,988 | 1,251,889 | 553,100 | 581,615 |
| Capex / revenue (computed) | 0.35% | 1.03% | 0.26% | 0.67% | 0.77% | 0.99% | 1.80% |
| Acquisition of business, net of cash acquired | (36,914) | (86,059) | — | — | — | — | (446,954) |
| Net cash used in / provided by investing activities | (25,858) | (128,245) | (36,993) | (221,017) | (134,482) | (74,120) | 158,770 |
| Repurchases of Class A common stock | — | — | (500,000) | (600,198) | (927,013) | (227,626) | (2,024,886) |
| Shares repurchased for tax withholding on RSU/RSA release | — | (161,809) | (335,019) | (390,254) | (398,982) | (199,468) | (180,532) |
| Proceeds from exercise of stock options, net | 23,912 | 12,882 | 8,256 | 22,133 | 8,053 | 8,053 | — |
| Proceeds from convertible notes, net of issuance costs | — | — | — | — | — | — | 979,894 |
| Purchase of capped calls | — | — | — | — | — | — | (99,187) |
| Net cash used in / provided by financing activities | 22,162 | (148,927) | (826,763) | (968,319) | (1,317,942) | (419,041) | (1,326,601) |
| Cash paid for income taxes, net | 1,494 | 10,008 | 19,173 | 25,018 | 22,376 | 14,079 | 11,600 |

- *FY2021 and FY2022 capex line is labelled "Purchases of property and equipment and intangible assets" in the FY2023 10-K; later years are labelled "Purchases of property and equipment". FY2021–FY2023: [10-K FY2023, Item 8 (Consolidated statements of cash flows)]. FY2023–FY2025: [10-K FY2025, Item 8]. Six months: [10-Q Q2 2026, Item 1]. Company-reported FCF for FY2023–FY2025 and six months: [10-K FY2025, Item 7 (Free cash flow reconciliation); 10-Q Q2 2026, Item 2]. FY2021–FY2022 FCF computed by this gatherer using the same formula; the company did not present FCF in the FY2022 or FY2023 10-K.
- FCF definition (verbatim): "We define free cash flow as net cash provided by operating activities less purchases of property and equipment. Free cash flow is not intended to represent our residual cash flow available for discretionary expenditures." [10-K FY2025, Item 7; 10-Q Q2 2026, Item 2]
- What capex is: "Cash flows from investing activities consist of capital expenditures for improvements to new and existing office spaces and acquisitions of businesses." [10-Q Q2 2026, Item 2] "Website development costs... development costs meeting our capitalization criteria were not material during the periods presented." i.e., no capitalized internal-use software shown separately. [10-K FY2025, Note 1]
- Depreciation of property and equipment: $14.1 million (FY2023), $13.9 million (FY2024), $19.4 million (FY2025). Property and equipment, gross 152,153 thousand at 12/31/2025 (leasehold improvements 95,309; computer and network equipment 33,092; furniture 23,752), net 66,451; construction in progress 19,810. [10-K FY2025, Note 4]
- Cash uses: "Our primary uses of cash are personnel-related costs and the cost of hosting our website and mobile application, as well as our stock repurchase program". [10-Q Q2 2026, Item 2]
- Six-month 2026 OCF commentary: "+$49.5 million... primarily due to an increase in accrued expenses and other liabilities due to timing of payments to vendors offset by the impact of higher revenue on our accounts receivable balance." Investing: "+$232.9 million... primarily due to an increase in net purchases and sales of marketable securities offset by a decrease in maturities of marketable securities and the acquisition of tvScientific." Financing: "+$907.6 million [more used]... primarily due to an increase in repurchases of our Class A common stock and the purchase of the Capped Calls offset by net proceeds from the issuance of the Notes." [10-Q Q2 2026, Item 2]
- FY2024 OCF included "the release of our valuation allowance" among non-cash items and "an increase in our accrued expenses and other liabilities due to timing of payments to vendors". [10-K FY2024, Item 7]
- Tax law: OBBBA enacted July 4, 2025 allows immediate expensing of domestic R&D; "The changes effective in 2025 are included in our provision for income taxes for the year ended December 31, 2025 and were not material." [10-K FY2025, Item 7]

### 6b. Cash, marketable securities and debt (USD thousands)

| Date | Cash and cash equivalents | Marketable securities | Cash + marketable securities (computed) | Debt (principal) |
|---|---|---|---|---|
| 12/31/2021 | 1,419,630 | 1,060,488 | 2,480,118 | none (revolver undrawn) |
| 12/31/2022 | 1,611,063 | 1,087,164 | 2,698,227 | none |
| 12/31/2023 | 1,361,936 | 1,149,148 | 2,511,084 | none |
| 12/31/2024 | 1,136,460 | 1,376,409 | 2,512,869 | none |
| 12/31/2025 | 969,342 | 1,497,811 | 2,467,153 | none |
| 6/30/2026 | 422,484 | 852,417 | 1,274,901 | 1,000,000 convertible notes |

- 12/31/2021: [10-K FY2022, Item 8]. 12/31/2022–12/31/2023: [10-K FY2023, Item 8]. 12/31/2024–12/31/2025: [10-K FY2025, Item 8]. 6/30/2026: [10-Q Q2 2026, Item 1]. Company statements of the combined figure: "$2,698.2 million" (2022), "$2,511.1 million" (2023), "$2,512.9 million" (2024), "$2,467.2 million" (2025), "$1,274.9 million" (6/30/2026). [10-K FY2022; FY2023; FY2024; FY2025, Item 7; 10-Q Q2 2026, Item 2]
- Net cash at 6/30/2026 = cash and marketable securities minus notes principal = $274.9 million (computed).
- Held abroad: "$216.2 million of our cash and cash equivalents was held by our foreign subsidiaries" (12/31/2025); "$169.5 million" (6/30/2026). [10-K FY2025, Item 7; 10-Q Q2 2026, Item 2]
- Investments: "primarily invested in short-duration fixed income securities, including government and investment-grade corporate debt securities and money market funds." 6/30/2026 marketable securities: corporate bonds 402,917; commercial paper 188,620; certificates of deposit 117,502; U.S. treasuries 139,255; non-U.S. government 4,123; 574,232 thousand due within one year. A 100 bp rate rise would cut market value by $5.0 million (6/30/2026) vs $8.5 million (12/31/2025). [10-Q Q2 2026, Note 2; Item 3]
- Revolving credit facility: $500.0 million, five-year, amended October 2023 (accordion $305.0 million); interest at adjusted term SOFR + 0.10% + 1.50% margin or base rate + 0.50%; commitment fee 0.15%; covenant "maximum net leverage ratio of consolidated debt to consolidated EBITDA no greater than 3.50 to 1.00, subject to an increase up to 4.00 to 1.00 for a certain period following an acquisition"; "secured by liens on substantially all of our domestic assets, including certain domestic intellectual property assets"; undrawn and in compliance at 12/31/2025 and 6/30/2026. It "place[s] certain limitations on the amount of dividends we can pay". [10-K FY2025, Note 6; Item 5; 10-Q Q2 2026, Item 2]

### 6c. Convertible notes (issued March 2026)

- "On March 5, 2026, we issued $1,000.0 million in aggregate principal amount of 1.75% convertible senior notes due in 2031 (the "Notes") and entered into an investment agreement... with Elliott Associates, L.P. and Elliott International, L.P. (collectively, "Elliott")... The net proceeds were $979.9 million after deducting issuance costs of $20.1 million." [10-Q Q2 2026, Note 5]
- Terms: "senior, unsecured obligations"; 1.75% paid semi-annually March 1 and September 1 from September 1, 2026; mature March 1, 2031. "Each $1,000 principal amount of the Notes is convertible at an initial conversion rate of 44.0063, which is equivalent to a conversion price of approximately $22.72 per share, and a maximum conversion rate of 57.2082... Upon conversion, we will pay cash up to the aggregate principal amount of the Notes being converted and deliver shares of our Class A common stock for any conversion value in excess of the principal amount." Shares underlying: 44,006,300 (computed from 44.0063 × 1,000,000; also stated in the capped-call paragraph). [10-Q Q2 2026, Note 5]
- Conversion conditions before December 1, 2030: stock above 150% of conversion price for 20 of 30 trading days in a quarter (falls to 130% "if Elliott and its affiliates no longer own a majority of the then-outstanding aggregate principal amount"), redemption call, trading-price test, specified corporate events; freely convertible on or after December 1, 2030. Company may redeem for cash on or after March 5, 2029 if the stock is at least 130% of conversion price for 20 of 30 trading days. Fundamental change put at 100%. "As of June 30, 2026, the Notes are not eligible for optional conversion." [10-Q Q2 2026, Note 5; Item 2]
- Carrying amount 6/30/2026: principal 1,000,000 less unamortized issuance costs 18,872 = 981,128; effective interest rate 2.20%; fair value $1,087.9 million (Level 3, binomial lattice). [10-Q Q2 2026, Note 5; Note 2]
- Use of proceeds: "In March 2026, we used the proceeds of the Notes to repurchase shares of our Class A common stock". [10-Q Q2 2026, Item 2]
- Capped calls (June 2026): cost $99.2 million; cover 44,006,300 shares; strike ~$22.72; cap $30.59; mature March 1, 2031; recorded as a reduction of APIC offset by $23.3 million deferred tax; "we expect the Capped Calls to reduce the potential dilution to our Class A common stock for any conversion value in excess of the principal amount of the Notes, subject to a cap based on the cap price." [10-Q Q2 2026, Note 5]
- Related party: "Marc Steinberg is a Partner at Elliott Investment Management L.P. and remains on our board of directors pursuant to the Investment Agreement." [10-Q Q2 2026, Note 12]
- 8-K terms not repeated in the 10-Q: Elliott lock-up on the Notes and conversion shares "for a period ending on the second anniversary of the Closing"; registration rights; Steinberg to be nominated as a Class I director through 2029; the company's board-seat obligations "automatically terminate... if Elliott ceases to beneficially own a net long position of at least 4.3% of the then-outstanding shares of the Company's Class A common stock"; Elliott standstill and voting commitments "until the later of (i) 20 days after such time as Mr. Steinberg (or any replacement director) has ceased to serve on the Board and (ii) the two-year anniversary of the Closing." Trustee: U.S. Bank Trust Company. [8-K 2026-03-03, Item 1.01; 8-K 2026-03-05, Item 1.01]
- Diluted EPS treatment: "We use the if‑converted method for the Notes"; "the Notes will only impact diluted net income (loss) per share when the average market price of our Class A common stock exceeds the initial conversion price of approximately $22.72 per share". [10-Q Q2 2026, Note 8]

## 7. Balance sheet basics (USD thousands)

| Item | 12/31/2024 | 12/31/2025 | 6/30/2026 |
|---|---|---|---|
| Cash and cash equivalents | 1,136,460 | 969,342 | 422,484 |
| Marketable securities | 1,376,409 | 1,497,811 | 852,417 |
| Accounts receivable, net | 893,403 | 997,849 | 932,000 |
| Total current assets | 3,484,707 | 3,555,737 | 2,323,347 |
| Property and equipment, net | 45,624 | 66,451 | 97,447 |
| Operating lease right-of-use assets | 85,867 | 150,399 | 143,050 |
| Goodwill | (combined 110,103) | 100,227 | 475,290 |
| Intangible assets, net | (combined with goodwill) | 6,083 | 83,037 |
| Deferred tax assets | 1,602,539 | 1,592,153 | 1,616,367 |
| Total assets | 5,342,660 | 5,492,132 | 4,759,378 |
| Accounts payable | 84,026 | 129,810 | 145,148 |
| Accrued expenses and other current liabilities | 314,107 | 335,663 | 464,663 |
| Total current liabilities | 398,133 | 465,473 | 609,811 |
| Convertible notes, net | — | — | 981,128 |
| Operating lease liabilities (non-current) | 151,364 | 220,581 | 215,507 |
| Total liabilities | 591,506 | 746,894 | 1,865,480 |
| Additional paid-in capital | 5,039,439 | 4,612,205 | 2,886,635 |
| Retained earnings (accumulated deficit) | (288,162) | 128,693 | 8,437 |
| Total stockholders' equity | 4,751,154 | 4,745,238 | 2,893,898 |

- [10-K FY2025, Item 8 (Consolidated balance sheets)]; [10-Q Q2 2026, Item 1]. Earlier year-ends: total assets 3,537,238 / liabilities 498,495 / equity 3,038,743 (12/31/2021); 3,862,730 / 581,076 / 3,281,654 (12/31/2022); 3,594,405 / 503,725 / 3,090,680 (12/31/2023). [10-K FY2022, Item 8; 10-K FY2023, Item 8]
- Accrued expenses detail 12/31/2025 (12/31/2024): accrued hosting expenses 67,964 (56,946); accrued compensation 57,089 (52,717); accrued legal expenses 11,440 (47,599); operating lease liabilities 41,437 (34,425); deferred revenue 47,467 (23,387); other 110,266 (99,033). [10-K FY2025, Note 4]
- Deferred tax assets, gross 1,957,045 at 12/31/2025 (NOLs 569,975; research credits 786,586; research capitalization 486,379) less valuation allowance (346,095) (California and Ireland). "Our valuation allowance increased by $24.0 million for the year ended December 31, 2025, primarily due to California tax credits generated during the year." NOL carryforwards: federal $2,160.6 million (do not expire), California $554.3 million, other state $956.4 million, Irish $198.2 million; R&D credit carryforwards federal $711.4 million, California $490.0 million. Gross unrecognized tax benefits $370.2 million. [10-K FY2025, Note 10]
- Ireland valuation allowance: "we believe that there is a reasonable possibility that sufficient positive evidence may become available to allow us to determine that the valuation allowance recorded against our Ireland deferred tax assets could be released within the next twelve months. The reversal would result in the recognition of Ireland deferred tax assets and a corresponding income tax benefit in the period the release is recorded." [10-K FY2025, Note 10; repeated 10-Q Q2 2026, Note 9]
- Goodwill and intangibles after tvScientific: goodwill 100,227 → 475,290 (+375,063); intangibles: developed technology gross 88,151 (net 56,075, 4.6 years), customer relationships 42,700 (net 24,183, 5.4 years), patents and other 12,721 (net 2,779). Future amortization: remainder of 2026 9,208; 2027 15,794; 2028 15,752; 2029 15,396; 2030 15,023. Amortization expense $4.8 million (Q2 2026) vs $1.7 million (Q2 2025). [10-Q Q2 2026, Note 4]
- Operating leases: obligations $323.5 million at 12/31/2025 ($50.0 million due within 12 months); leases expire through 2036. Schedule: 2026 49,969; 2027 46,958; 2028 41,077; 2029 36,232; 2030 32,453; thereafter 116,811. [10-K FY2025, Item 7; Note 6; Note 1]

## 8. Share count, buybacks, dilution

### 8a. Shares outstanding

| Date | Class A | Class B | Total (computed) | Source |
|---|---|---|---|---|
| 12/31/2020 (equity statement) | — | — | 626,372 thousand | [10-K FY2023, Item 8] |
| 12/31/2021 (equity statement) | — | — | 656,872 thousand | [10-K FY2023, Item 8] |
| 12/31/2022 (balance sheet) | 593,918 thousand | 89,284 thousand | 683,202 thousand | [10-K FY2023, Item 8] |
| January 31, 2023 (cover) | 594,519,329 | 89,348,474 | 683,867,803 | [10-K FY2022, cover] |
| 12/31/2023 (balance sheet) | 591,663 thousand | 86,355 thousand | 678,018 thousand | [10-K FY2023, Item 8] |
| February 2, 2024 (cover) | 595,211,750 | 83,771,609 | 678,983,359 | [10-K FY2023, cover] |
| 12/31/2024 (balance sheet) | 593,462 thousand | 82,471 thousand | 675,933 thousand | [10-K FY2025, Item 8] |
| January 31, 2025 (cover) | 595,091,038 | 83,146,379 | 678,237,417 | [10-K FY2024, cover] |
| 12/31/2025 (balance sheet) | 584,866 thousand | 79,680 thousand | 664,546 thousand | [10-K FY2025, Item 8] |
| February 6, 2026 (cover) | 585,458,698 | 79,679,925 | 665,138,623 | [10-K FY2025, cover] |
| March 27, 2026 (proxy record date) | 496,121,510 | 79,679,925 | 575,801,435 | [DEF 14A 2026, Security ownership] |
| 3/31/2026 (equity statement) | — | — | 573,671 thousand | [10-Q Q2 2026, Item 1] |
| 6/30/2026 (balance sheet) | 490,712 thousand | 74,785 thousand | 565,497 thousand | [10-Q Q2 2026, Item 1] |
| July 29, 2026 (cover) | 492,198,008 | 74,115,019 | 566,313,027 | [10-Q Q2 2026, cover] |

- Authorized: Class A 6,666,667 thousand; Class B 1,333,333 thousand. [10-K FY2025, Item 8] "As of June 30, 2026, we had 5,921,462,168 shares of authorized but unissued Class A common stock that are currently not reserved for issuance". [10-Q Q2 2026, Part II Item 1A]
- Class B as a share of all shares: 11.99% at 12/31/2025; 13.22% at 6/30/2026 (computed). Class B conversion: "in April 2026, pursuant to the requirements of our charter, 1.3 million shares of Class B common stock were automatically converted into 1.3 million shares of Class A common stock due to the holders thereof no longer owning 50% of their pre-IPO Class B common stock on the 7th anniversary of the completion of our IPO." [10-Q Q2 2026, Part II Item 1A]

### 8b. Repurchase programs and activity

| Program | Authorized | Activity | Status |
|---|---|---|---|
| February 2, 2023 | $500.0 million | 21,215,663 shares for $500.0 million at avg $23.57, completed Q2 2023 | completed |
| September 16, 2023 | $1.0 billion | FY2024: 15,894,701 shares for $500.0 million at avg $31.46 | canceled Nov 2024 with $500.0 million remaining |
| November 5, 2024 | $2.0 billion | FY2024 total repurchases (all programs) 19,125,363 shares, $600.2 million; $1,899.8 million remained at 12/31/2024. FY2025: 30,108,015 shares for $927.0 million at avg $30.79 (incl. $3.3 million excise tax); $972.8 million remained at 12/31/2025. 6M 2026: 27,664,663 shares for $472.9 million at avg $17.09 | canceled March 2, 2026 with $499.9 million remaining |
| March 2, 2026 | $3.5 billion | 6M 2026 open market: 28,950,481 shares for $551.0 million at avg $19.03; ASR: 54,796,613 shares for $1,000.0 million at avg $18.25 (41,279,670 delivered March 2026, 13,516,943 April 2026) | $1,948.0 million remained at 6/30/2026 |

- [10-K FY2023, Note 9]; [10-K FY2024, Note 8]; [10-K FY2025, Note 8; Item 5]; [10-Q Q2 2026, Note 7; Part II Item 2]; [8-K 2026-03-03, Item 8.01].
- Yearly totals (equity statements): FY2023 21,216 thousand shares / $500,000 thousand; FY2024 19,125 thousand / $600,198 thousand; FY2025 30,108 thousand / $930,263 thousand (includes accrued excise tax; cash paid $927,013 thousand); 6M 2026 111,412 thousand / $2,039,826 thousand (includes $14.9 million excise tax; cash paid $2,024,886 thousand). No repurchases in FY2021 or FY2022. [10-K FY2023, Item 8; 10-K FY2025, Item 8; 10-Q Q2 2026, Item 1]
- Q2 2026 monthly: April 380,624 shares at $18.32 (348,568 under the program) plus ASR final delivery 13,516,943; May none; June 2,381,000 at $21.43; total 16,278,567 shares (16,246,511 under programs). Q4 2025 monthly: October 3,172,749 at $31.85; November 14,786,360 at $27.05; December none. [10-Q Q2 2026, Part II Item 2; 10-K FY2025, Item 5]
- ASR mechanics per 8-K: counterparty Goldman Sachs & Co. LLC; $1 billion paid March 5, 2026 with initial delivery of ~80% of expected shares; final settlement "no later than May 1, 2026"; the Nov 2024 program was canceled after "$473 million of share repurchases year to date"; "After giving effect to the ASR, the aggregate remaining authorization under the 2026 Share Repurchase Program is approximately $2.5 billion." [8-K 2026-03-03, Item 1.01; Item 8.01]
- Risk-factor caveat: "We cannot guarantee that the program will be fully consummated, renewed or exhausted or that it will enhance long-term stockholder value... In addition, any purchases made under this program would diminish our cash reserves." New in 10-Q: "We may also enter into derivative share repurchase agreements from time to time that impose potential liabilities on the company." [10-K FY2025, Item 1A; 10-Q Q2 2026, Part II Item 1A]

### 8c. Dilution from equity awards

- RSUs/RSAs outstanding: 37,217 thousand (12/31/2024) → 39,119 thousand at weighted grant-date fair value $30.25 (12/31/2025; granted 37,305 thousand at $29.70, released 29,047 thousand, forfeited 6,356 thousand) → 69,085 thousand at $22.97 (6/30/2026; granted 59,190 thousand at $19.19, released 20,947 thousand, forfeited 8,277 thousand). [10-K FY2025, Note 8; 10-Q Q2 2026, Note 7]
- Stock options: 8,554 thousand outstanding at weighted exercise price $19.96 at both 12/31/2025 and 6/30/2026 (8,019 thousand exercisable at 6/30/2026); intrinsic value $50.7 million → $9.2 million. No options exercised in 6M 2026. [10-K FY2025, Note 8; 10-Q Q2 2026, Note 7]
- Market-condition RSUs: 798,034 granted in 2025 and 1,004,022 in Q1 2026, vesting 0%–200% on total stockholder return relative to the Nasdaq CTA Internet Index over two- to three-year periods. [10-K FY2025, Note 8; 10-Q Q2 2026, Note 7]
- 2019 Plan evergreen: reserve "will automatically increase on the first day of each fiscal year through and including January 1, 2029, in an amount equal to 5% of the total number of shares of our Class A common stock and our Class B common stock outstanding"; 186,410,561 shares reserved at 12/31/2025; 176,814,803 at 6/30/2026. [10-K FY2025, Note 8; 10-Q Q2 2026, Note 7]
- Equity plan table at 12/31/2025: 47,672,428 securities to be issued (37,859,546 RSUs, 1,084,476 PSUs, 175,234 RSAs, 8,553,172 options). [DEF 14A 2026, Equity compensation plan information]
- Anti-dilutive shares excluded from diluted EPS, Q2 2026: options 8,554 thousand; unvested RSUs/RSAs 77,844 thousand; ASR 1,931 thousand. [10-Q Q2 2026, Note 8]
- Tax withholding on vesting is settled in cash by the company ("net settling"), USD thousands: 335,019 (FY2023), 390,254 (FY2024), 398,982 (FY2025), 180,532 (6M 2026). "fluctuations, caused by stock price volatility, in the amount we spend to fund tax withholding and remittance obligations related to the vesting and settlement of restricted stock units ("RSUs") as we continue to net settle such RSUs" is listed as a results driver. [10-K FY2025, Item 8; Item 1A; 10-Q Q2 2026, Item 1]

## 9. Cost structure, hosting commitments, headcount

- Cost of revenue composition (verbatim): "Cost of revenue consists primarily of expenses associated with the delivery of our service, including the cost of hosting our website and mobile application. Cost of revenue also includes personnel-related expense, including salaries, benefits and share-based compensation for employees on our operations teams, payments associated with partner arrangements, credit card and other transaction processing fees, amortization of acquired intangible assets and allocated facilities and other supporting overhead costs." [10-K FY2025, Item 7]
- R&D: "personnel-related expense... for our engineers and other employees engaged in the research and development of our products, and allocated facilities and other supporting overhead costs." S&M: personnel including commissions, "advertising and promotional expenditures, services provided by third-party resellers, professional services, amortization of acquired intangible assets". G&A: finance, legal, HR personnel, "professional services, including outside legal and accounting services, charitable contributions, non income-based taxes". [10-K FY2025, Item 7; 10-Q Q2 2026, Item 2]
- Fixed vs variable: "Certain of our costs..." is not stated; the closest statements are "we have entered into certain non-cancelable commitments that limit our ability to reduce our cost and expenses in the future" and "As our user, content and advertiser base, number of actionable consumer products, sophistication of our machine learning models and the volume and types of information shared on our service continue to grow, we will need an increasing amount of technology infrastructure, including network capacity and computing power, to continue to satisfy the needs of users, content creators and advertisers, which could increase our costs." [10-K FY2025, Item 1A]
- Cloud concentration: "We have an agreement with Amazon Web Services ("AWS") to provide the cloud computing infrastructure we use to host our website, mobile application and many of the internal tools we use to operate our business. We are currently required to maintain a substantial majority of our monthly usage of certain compute, storage, data transfer and other services on AWS. Any transition of the cloud services currently provided by AWS to another cloud services provider would be difficult to implement and would cause us to incur significant time and expense." [10-K FY2025, Note 1] "We are particularly vulnerable to these types of events because our cloud computing infrastructure is currently located in one geographic region." "we have implemented a limited disaster recovery program which does not allow us to serve network traffic from back-up data center services." [10-K FY2025, Item 1A]

| AWS commitment | Terms | Remaining commitment |
|---|---|---|
| April 2021 addendum | "at least $3,250.0 million of cloud services from AWS through April 2029"; "not subject to annual purchase commitments" | $2,357.1 million (12/31/2022); $1,754.6 million (12/31/2023); $1,110.2 million (12/31/2024); $312.3 million (12/31/2025), all shown as due in 2029 |
| May 2026 addendum | "at least $4,000.0 million of cloud services from AWS through May 2031. If we fail to do so, we are required to pay the difference between the amount we spend and the required commitment amount." | $3,927.9 million (6/30/2026); "We expect to meet our remaining commitment." |

- [10-K FY2022, Note (Commitments)]; [10-K FY2023, Note 7]; [10-K FY2024, Note (Commitments)]; [10-K FY2025, Note 6; Item 7]; [10-Q Q2 2026, Note 6; Item 2]. Implied AWS spend counted against the 2021 commitment (computed from the decline in remaining commitment): $1,495.4 million April 2021–December 2023; $644.4 million in 2024; $797.9 million in 2025. This is an inference about minimum qualifying spend, not a disclosed cost figure.
- Accrued hosting expenses (USD thousands): 56,946 (12/31/2024), 67,964 (12/31/2025). [10-K FY2025, Note 4]
- New risk wording in 10-Q: "Industry-wide shortages of, or constraints on access to, cloud infrastructure capacity, including GPUs (graphics processing units), could increase our costs, limit the availability of AWS services to us and adversely affect our business". [10-Q Q2 2026, Part II Item 1A]

| Date | Full-time employees |
|---|---|
| 12/31/2021 | not in fetched sources |
| 12/31/2022 | 3,987 |
| 12/31/2023 | 4,014 |
| 12/31/2024 | 4,666 |
| 12/31/2025 | 5,265 |
| 6/30/2026 | 5,116 |

- [10-K FY2022, Item 1]; [10-K FY2023, Item 1]; [10-K FY2024, Item 1]; [10-K FY2025, Item 1]; [10-Q Q2 2026, Item 2 ("Headcount was 5,116")]. Restructurings: March 2023 plan, "workforce reduction of approximately 4%", completed Q3 2023, $126.9 million charges; January 2026 plan, "reduction in force that is expected to affect less than 15% of the Company's workforce as well as office space reductions", initial estimate "$35 million to $45 million" of pre-tax charges, expected completion by end of Q3 2026. [10-K FY2023, Note 13; 8-K 2026-01-27, Item 2.05]
- 2026 restructuring cost to date (USD thousands): Q2 2026 14,335 (severance 7,975; SBC 4,788; office 1,572); 6M 2026 61,432 (severance 44,147; SBC 14,113; office 3,172). "We expect to incur total charges of up to $69.6 million under the Restructuring Plan through the end of the third quarter of 2026." Stated purpose: "(i) reallocating resources to AI-focused roles and teams that drive AI adoption and execution, (ii) prioritizing AI‑powered products and capabilities, and (iii) accelerating the transformation of our sales and go-to-market approach." [10-Q Q2 2026, Note 11]
- Flexible work: "We utilize a flexible work model and, as a result, a majority of our employees work remotely." "the substantial majority of our employees are located in California". [10-K FY2025, Item 1A]

## 10. Customer concentration

- "No customer accounted for more than 10% of our revenue for the years ended December 31, 2025, 2024 and 2023." [10-K FY2025, Note 1]
- Concentration described qualitatively: "A substantial portion of our revenue is derived from a small number of advertisers and is currently concentrated in certain verticals, particularly retail and CPG. We either contract directly with advertisers or with advertising agencies on behalf of advertisers, many of which are owned by large media corporations that exercise varying degrees of control over the agencies. Our business, revenue and financial results could be harmed by the loss of, or a deterioration in our relationship with, any of our largest advertisers or with any advertising agencies or the large media corporations that control them." [10-K FY2025, Item 1A]
- "As is common in our industry, most of our advertisers do not have long-term advertising commitments with us. Many of our advertisers spend a relatively small portion of their overall advertising budget with us." [10-K FY2025, Item 1A]
- Share of revenue from large advertisers vs SMB, from third-party demand partners, or from agencies: not disclosed. Tariff effect (new in 10-Q): "For example, we have seen reduced spending from certain advertisers due to the impact of tariffs and related retaliatory actions." [10-Q Q2 2026, Part II Item 1A]
- Geographic concentration: "since the majority of our revenue is derived from advertisers within the U.S., economic conditions in the U.S. have a greater impact on us." [10-K FY2025, Item 1A]
- Credit: "Our accounts receivable are generally unsecured... Bad debt expense was not material". [10-K FY2025, Note 1]

## 11. Pinterest-specific risk factors (key sentences, verbatim)

- Search-engine dependence: "We depend in part on internet search engines, such as Google, Bing and Yahoo!, to direct a significant amount of traffic to our platform... Search engines, such as Google, have and may continue to modify their search algorithms (including what content they index and the format in which content is indexed) and policies or enforce those policies in ways that are detrimental to us... We have experienced declines in traffic and user growth as a result of these changes in the past, and anticipate fluctuations as a result of such actions in the future." "Traditional search engines compete with new methods of search, particularly those powered by AI, and as a result traditional search engines may provide less traffic to our platform". "Further, some of these search engines are owned by companies that compete with various aspects of our business." [10-K FY2025, Item 1A]
- App stores and logins: "we also rely on certain major online stores for distribution of our application." "A significant number of users access their accounts on our platform using a third-party login provider such as Facebook, Apple or Google." [10-K FY2025, Item 1A]
- Apple/ATT and measurement: "web and mobile browser developers, such as Apple, Microsoft or Google, have implemented and may continue to implement changes... that impair our ability to measure and improve the effectiveness of advertising on our platform... Apple implemented certain changes, including an AppTrackingTransparency framework that limits the ability of mobile applications to obtain access to an iOS device's advertising identifier and affects our ability to track user actions off our platform". "All of this may result in advertisers spending less or not at all, on our platform and prefer larger platforms like Facebook and Google that have more capabilities to help advertisers measure their conversions." "Many existing advertiser tools that measure the effectiveness of advertising do not account for the role of advertising early in a user's decision-making process, which is when many users come to our platform." [10-K FY2025, Item 1A]
- Generative AI competition: "consumers may increasingly search for products using chatbots, virtual assistants or other generative AI technologies powered by large language models." "Barriers to entry in our industry are low and may be further lowered by commercial AI tools". "we face significant potential disruption from other companies, particularly as internet companies utilize AI to introduce new methods of search and discovery for consumers and AI reduces barriers to entry to compete with our products and services". [10-K FY2025, Item 1A]
- AI-generated content and liability: "AI technologies, including generative AI, may create content that is factually inaccurate or flawed, or otherwise unlawful, harmful or policy-violating. Such content may expose us to brand or reputational harm and/or legal liability." EU AI Act "Penalties for non-compliance... include fines as high as 7% of a company's global annual revenue." "Our AI initiatives also depend on our access to data to effectively train our models." [10-K FY2025, Item 1A]
- Regulation (DSA, teens, age verification): "various laws to restrict or govern the use of commercial websites, applications, online services, or other interactive platforms by teens have passed or have been proposed, including laws: prohibiting offering services to teens, prohibiting showing teens advertising, requiring age verification or assurance, limiting the use of teens' personal data, and requiring parental consent... These new laws may result in restrictions on the use of certain of our products or services by teens, the inability to offer certain products and services to teens, decrease users or user engagement in those jurisdictions, require changes to our products and services to achieve compliance, decrease our advertising and subscription revenue". "laws that allow users to opt out of the use of personal data or restrict the use of personal data of teens, which may limit or prohibit us and our customers from targeting advertising to users, including teens". GDPR fines "up to 4% of global annual turnover". Brazil: "in June 2025, the Brazilian Supreme Court partially invalidated the country's limitation on platform liability for third-party content." [10-K FY2025, Item 1A]
- Data scale disadvantage: "the impact of these developments may disproportionately affect our business in comparison to certain peers in the technology sector that, by virtue of the scope and breadth of their operations or user base, have greater access to user data." [10-K FY2025, Item 1A]
- User growth: "We anticipate that our active user growth rate will decline over time if the size of our active user base increases or we achieve higher market penetration rates. As a result, our financial performance will increasingly depend on our ability to increase user engagement and our monetization efforts... We may not be able to further increase the number of users in these demographics and may need to increase the number of users in other demographics, such as men and international users, in order to grow our users." [10-K FY2025, Item 1A]
- Content choices that cost engagement: "We endeavor to keep divisive, disturbing or unsafe content off our platform by deactivating or limiting the distribution of certain types of content, even if this content would be permitted on other platforms, which could result in a decrease in user growth, retention or engagement." [10-K FY2025, Item 1A]
- Lower-funnel strategy: "as we execute on our business strategy of transitioning to provide full funnel advertising solutions there is no guarantee that the lower funnel performance advertising solutions that we have developed and that we may develop in the future will be attractive to or effective for advertisers". [10-K FY2025, Item 1A]
- AWS: "We depend on Amazon Web Services for the vast majority of our compute, storage, data transfer and other services." (10-Q wording: "for the majority of"). "Under our long-term agreement with AWS, in return for negotiated concessions, we currently are required to maintain a substantial majority of our monthly usage... A material breach of this agreement by us, or early termination of the agreement, could carry substantial penalties, including liquidated damages." [10-K FY2025, Item 1A; 10-Q Q2 2026, Part II Item 1A]
- Dual class: "Our Class B common stock has twenty votes per share, and our Class A common stock has one vote per share. Because of the 20-to-1 voting ratio between our Class B and Class A common stock, the holders of our outstanding Class B hold approximately 73.2% of the voting power of our outstanding capital stock as of December 31, 2025." (75.3% as of June 30, 2026.) "The holders of Class B common stock will no longer hold in the aggregate over 50% of the voting power of our outstanding capital stock once the Class B common stock represents in the aggregate less than approximately 4.76% of our outstanding capital stock." "Despite no longer being employed by us, Paul Sciarra and Benjamin Silbermann, two of our co-founders, remain able to exercise significant voting power." [10-K FY2025, Item 1A; 10-Q Q2 2026, Part II Item 1A]
- Profitability: "We have incurred significant net losses in the past and generated net income only recently... We have achieved profitability only recently and may not realize sufficient revenue to maintain profitability in future periods." 10-Q version: "and may continue to generate operating losses in the future. We generated net loss of $120.3 million and net income of $47.7 million for the six months ended June 30, 2026 and 2025, respectively. As of June 30, 2026, we had retained earnings of $8.4 million." [10-K FY2025, Item 1A; 10-Q Q2 2026, Part II Item 1A]
- Seasonality in risk list: "seasonal fluctuations in engagement on our platform, including our historical experience of lower engagement in our second quarter". [10-K FY2025, Item 1A]
- Macro: "the macroeconomic conditions and the status of the advertising industry, such as fear of recession, inflation, the impact of tariffs and related retaliatory actions and other trade protection measures... which could cause businesses to spend less on advertising and/or direct their advertising spend to larger companies". [10-K FY2025, Item 1A]
- Ad blocking, third-party software, mobile OS interoperability (Android, Chrome, iOS, Safari), international resellers, and derivative-suit settlement costs ("our ongoing efforts to implement terms of the settlement agreement with respect to certain derivative lawsuits... have resulted in, and will continue to result in, increased costs") are also listed. [10-K FY2025, Item 1A]
- New risk factors in the 10-Q vs the 10-K (paragraph-level comparison by this gatherer): indebtedness and the Notes ("We have incurred a significant amount of indebtedness and may in the future incur additional indebtedness... We may be required to use a substantial portion of our cash flows from operations to pay interest and principal on our indebtedness"; possible reclassification of the Notes as current if conversion conditions are met); capped-call counterparty risk ("we will be subject to the risk that one or more of the counterparties may default"); derivative share repurchase agreements; tariff-driven advertiser spending reductions; GPU/cloud capacity shortages; tvScientific closing; measurement-tool cost increases; Class B conversions in April 2026. [10-Q Q2 2026, Part II Item 1A]

## 12. Legal proceedings

- 10-K Item 3 incorporates Note 6 by reference and states: "we do not believe that there is a reasonable possibility that the final outcome of these matters will have a material adverse effect on our business or financial results." Note 6 "Legal matters": "We are involved in various lawsuits, claims and proceedings that arise in the ordinary course of business. While the results of legal matters are inherently uncertain, we do not believe there is a reasonable possibility that the ultimate resolution of these matters, either individually or in aggregate, will have a material adverse effect". No specific case, regulator or amount is named. [10-K FY2025, Item 3; Note 6]
- 10-Q Part II Item 1 repeats the same language and points to Note 6, which is identical in substance. No specific matter is named. [10-Q Q2 2026, Part II Item 1; Note 6]
- The only quantified legal item in the window: the November 1, 2024 settlement "to resolve pending litigation relating to allegations concerning the early development of Pinterest", $34.7 million net of insurance proceeds, expensed in FY2024. [10-K FY2025, Item 7] Accrued legal expenses fell from 47,599 thousand (12/31/2024) to 11,440 thousand (12/31/2025). [10-K FY2025, Note 4]
- Types of exposure listed: "intellectual property, data privacy and data protection, privacy and other torts, illegal or objectionable content, consumer protection, securities, corporate governance, employment, workplace culture, contractual rights, civil rights infringement, false or misleading advertising". "We are presently involved in intellectual property litigation and expect to continue to face allegations from third parties, including our competitors and "non-practicing entities"". [10-K FY2025, Item 3; Item 1]
- Auditor fees for "services rendered in connection with the Digital Services Act and business metrics" were $1.6 million (2025). [DEF 14A 2026, Principal accountant fees]

## 13. Management, board, ownership, compensation

### 13a. Executive officers (as of the proxy, plus 2026 changes)

| Name | Age | Title | Since / background |
|---|---|---|---|
| Bill Ready | 46 | Chief Executive Officer and director | CEO since 2022 (June 2022); previously "president of commerce, payments & next billion users at Alphabet, Inc. (Google)... from January 2020 until June 2022"; PayPal EVP and COO Oct 2016–Jul 2019; CEO of Braintree/Venmo |
| Julia Brau Donnelly | 43 | Chief Financial Officer | since June 2023; previously VP, Global Head of Finance and Accounting at Wayfair (Sept 2019–June 2023) |
| Matthew Madrigal | 50 | Chief Technology Officer | since September 2024; previously VP and GM of Merchant Shopping at Google (2020–2024); Fanatics CTO/CPO (2014–2020); serves on Tapestry, Inc. board |
| Wanji Walcott | 55 | Chief Legal & Business Affairs Officer and Corporate Secretary | since November 2022; previously CLO Discover Financial (2019–2022), GC PayPal (2017–2019) |
| Claude (Lee) Brown | not stated | Chief Business Officer | appointed effective January 20, 2026; "will oversee the Company's global sales, content, customer-facing operations and advertising product marketing"; previously Chief Revenue Officer of DoorDash; six years as Spotify's VP, Global Head of Advertising |
| Malik Ducard | not stated | Chief Content Officer (no longer an executive officer) | "in February 2026, the board determined that his role no longer met the threshold to qualify him as an executive officer" |

- [DEF 14A 2026, Executive officers; Our board of directors; Compensation discussion and analysis]; [8-K 2026-01-20, Item 7.01]. The 10-K signature block lists Andrea Acosta as Chief Accounting Officer (Principal Accounting Officer) at February 12, 2026; the 10-Q is signed by Donnelly as "Principal Financial Officer and Principal Accounting Officer". [10-K FY2025, Signatures; 10-Q Q2 2026, Signatures]
- CEO at-will: "We currently depend on the continued services and performance of our key personnel, including William Ready and others. Mr. Ready's employment... is at will". [10-K FY2025, Item 1A]

### 13b. Board

- "Our board is comprised of twelve members"; three staggered classes; "A substantial majority of our board—ten out of twelve directors—is independent" (all except Ready and Silbermann). Chair and CEO separate: "Since 2022, Bill Ready has served as our CEO, and Benjamin Silbermann has served as our chair." Silbermann is Non-Executive Chair (age 43, co-founder, "previously served as our Chief Executive Officer from 2008 and as President from 2012 until June 2022"). Lead independent director: Andrea Wishom. Board met 8 times in 2025. Committees: Audit and Risk (Schenkel chair; 11 meetings), Talent Development and Compensation (Kilgore chair; 5), Nominating and Corporate Governance (Bergh chair; 4). [DEF 14A 2026, Proxy summary; Director independence; Board leadership structure; Board committees]
- Directors (age, since): Chip Bergh 68 (2024), Gokul Rajaram 51 (2020), Emily Reuter 42 (2025), Marc Steinberg 36 (2022, Partner at Elliott Investment Management), Leslie Kilgore 60 (2019), Bill Ready 46 (2022), Benjamin Silbermann 43 (2008), Salaam Coleman Smith 56 (2020), Fredric Reynolds 75 (2017), Scott Schenkel 58 (2023), Kecia Steelman 55 (2026; appointed effective February 16, 2026), Andrea Wishom 56 (2020). [DEF 14A 2026, Proxy summary; 8-K 2026-02-09, Item 5.02]
- Elliott seat: "Mr. Steinberg continues to serve on our board pursuant to the investment agreement entered into by and among the company, Elliott Associates, L.P., and Elliott International L.P. in March 2026." [DEF 14A 2026, Our board of directors]
- 2026 annual meeting (May 21, 2026) results: Class I directors elected (Bergh 1,795,684,711 for / 152,462,358 against; Rajaram 1,906,257,236 / 41,887,444; Reuter 1,945,691,087 / 2,451,265; Steinberg 1,939,563,390 / 8,587,510); say-on-pay approved 1,872,585,095 for / 75,176,625 against / 731,895 abstain (96.1% of for-plus-against votes, computed); say-on-frequency: one year 1,940,750,588; EY ratified 1,980,724,813 / 14,669,424. Broker non-votes 47,220,520. [8-K 2026-05-26, Item 5.07]
- Director pay: annual cash retainer $50,000; non-executive chair +$40,000; lead independent director +$75,000; annual RSU grant $260,000 (raised to $270,000 in February 2026); initial grant $400,000. 2025 totals: Wishom $394,993; Silbermann $349,993; Steinberg $322,993. [DEF 14A 2026, Director compensation]

### 13c. Dual-class structure and ownership

- Votes: "Our Class A common stock has one vote per share and our Class B common stock has twenty votes per share." Class B converts to Class A on transfer (with exceptions for certain trusts/charities) and "upon the death or permanent incapacity of each holder of Class B common stock who is a natural person", except Silbermann's shares convert "between 90 and 540 days after his death or permanent incapacity, as determined by the board." Sunset: "all shares of Class B common stock will automatically convert into shares of Class A common stock on (i) April 23, 2026, the seven-year anniversary of our IPO, except with respect to shares of Class B common stock held by any holder that continues to beneficially own at least 50% of the number of shares of Class B common stock that such holder beneficially owned immediately prior to completion of our IPO". [DEF 14A 2026, Voting information; Equity compensation plan information]
- Record-date shares (March 27, 2026): 496,121,510 Class A and 79,679,925 Class B. [DEF 14A 2026, Security ownership]

| Holder | Class A shares (% of class) | Class B shares (% of class) | % of total voting power |
|---|---|---|---|
| Benjamin Silbermann (co-founder, chair) | 8,414 (*) | 36,911,603 (46.32%) | 35.33% |
| Paul Sciarra (co-founder, not an officer or director) | — | 32,589,537 (40.90%) | 31.19% |
| Bill Ready (CEO) | 8,719,450 (1.73%; includes 7,484,023 exercisable option shares plus 534,573 vesting within 60 days) | — | * |
| Fredric Reynolds | 105,223 | 100,000 | * |
| Leslie Kilgore | 78,898 | 6,838 | * |
| All directors and executive officers as a group | 9,591,705 (1.90%) | 37,018,441 (46.46%) | 35.75% |
| BlackRock, Inc. | 59,584,440 (12.01%) | — | 2.85% |
| The Vanguard Group | 60,147,395 (12.12%) | — | 2.88% |

- [DEF 14A 2026, Security ownership of certain beneficial owners and management]. Silbermann's figure excludes "8,762,530 shares of Class B common stock held by an LLC that is owned by a trust, the beneficiaries of which include certain of Mr. Silbermann's immediate family members" over which he has no voting or dispositive power. BlackRock per 13G/A of January 8, 2026 (as of 12/31/2025). Vanguard per 13G/A of December 6, 2024; Vanguard "reported on March 27, 2026, that due to an internal realignment it no longer has, or is deemed to have, beneficial ownership" and its units will report separately. Elliott does not appear as a 5% holder. Silbermann and Sciarra together hold 87.22% of Class B and 66.52% of total voting power (computed from the table).
- Holders of Class B in aggregate: 73.2% of voting power at 12/31/2025; 75.3% at 6/30/2026. [10-K FY2025, Item 1A; 10-Q Q2 2026, Part II Item 1A]
- Anti-takeover: classified board, removal only for cause, 66⅔% vote for charter/bylaw amendments, no action by written consent, no cumulative voting, undesignated preferred stock, Delaware exclusive forum. [10-K FY2025, Item 1A]
- Governance policies: proxy access (3%/3 years, up to 20 holders, greater of two directors or 20% of board); director resignation policy; stock ownership guideline 5x cash retainer for directors, 6x salary for CEO, 3x for other executives; hedging and pledging prohibited; clawback policy covering restatements and "cause". [DEF 14A 2026, Corporate governance; Other compensation policies]
- Related-party transactions since January 1, 2025: only the Elliott Investment Agreement. [DEF 14A 2026, Related party transactions]

### 13d. Executive compensation (2025 program and pay)

- Elements: base salary; annual cash bonus (introduced 2025); RSUs and PSUs. Base salaries "adjusted to $625,000 from $600,000" for all NEOs for 2025. [DEF 14A 2026, CD&A]
- Bonus metrics: "the compensation committee selected revenue and adjusted EBITDA (each weighted 50%) as the financial metrics for the 2025 bonus plan". Goals (USD millions): revenue threshold $4,108 / target $4,190 / maximum $4,356, actual $4,222 → 110% payout; Adjusted EBITDA threshold $1,168 / target $1,213 / maximum $1,303, actual $1,270 → 132%; overall payout 121%. Targets: CEO 100% of salary ($625,000 → paid $756,250); other NEOs 80% ($500,000 → paid $605,000 each). Payout range 75%–150% between threshold and maximum, 0% below threshold. [DEF 14A 2026, CD&A (Short-term incentive compensation)]
- Equity design: CEO 2025 award 60% PSUs / 40% RSUs; PSUs "based on the company's rTSR compared to the companies in the Nasdaq CTA Internet Index" over January 1, 2025–December 31, 2027, payout 0% (<25th percentile), 50% (25th), 100% (50th), 200% (≥75th). Other NEOs: 2025 annual awards 85% RSUs / 15% PSUs plus one-time "bridge" and "overlay" awards; 2026: "All NEOs were granted PSUs with a three-year performance period (2026 - 2028) as well as RSUs with back-loaded vesting over the third year following grant". No revenue, EBITDA or margin metric is used in PSUs; those metrics live in the cash bonus. [DEF 14A 2026, CD&A]
- CEO 2025 grants: 572,884 PSUs (target value $18 million; grant-date fair value $28.6 million) in January 2025; 354,192 RSUs (target $12 million; fair value $9.3 million) in April 2025 vesting quarterly in 2027. [DEF 14A 2026, CD&A (Long-term incentive compensation)]
- 2025 Summary Compensation Table totals: Bill Ready $39,312,010 (salary $620,833; stock awards $37,928,927; non-equity incentive $756,250; other $6,000); Julia Brau Donnelly $16,902,716; Malik Ducard $11,718,913; Matthew Madrigal $22,380,913; Wanji Walcott $12,462,079. Ready's 2024 total $18,143,031; 2023 $522,667 (no grant). "Compensation actually paid" to Ready 2025: $22,037,070 (2024: $(24,338,934); 2023: $74,249,630; 2022: $153,878,150). [DEF 14A 2026, Summary compensation table; Pay versus performance]
- CEO pay ratio: 126.2 to 1; median employee total compensation $311,466. [DEF 14A 2026, CEO pay ratio]
- Ready's 2022 hire grants: stock option for 8,553,172 shares at $19.96 (6,949,452 exercisable at 12/31/2025) vesting quarterly to July 20, 2026; RSA of 175,234 unvested shares conditioned on his purchase of "$5 million" of stock in the open market. [DEF 14A 2026, Outstanding equity awards]
- Severance: without cause, up to 24 months' salary (reduced one month per month of service, max reduction 12) and 12 months' equity acceleration; double-trigger change-in-control full acceleration; no 280G gross-ups. Estimated CIC value for Ready at 12/31/2025: $51,778,076. [DEF 14A 2026, Potential payments upon termination or change in control]
- Say-on-pay history: 2025 meeting 97% in favor; 2026 meeting approved (see 13b). Consultant: Compensia. Peer group of 21 companies including Snap, Reddit, Roku, The Trade Desk, Spotify, Etsy, Match Group, Zillow, DoorDash, Airbnb. [DEF 14A 2026, CD&A]
- Pay-versus-performance TSR: $100 invested 12/31/2020 was worth $55 (2021), $37 (2022), $56 (2023), $44 (2024), $39 (2025) vs Nasdaq CTA Internet Index $95, $50, $80, $104, $120. [DEF 14A 2026, Pay versus performance]
- Insider trading plans adopted Q2 2026: Lee Brown (sell up to 50% of net shares from 1,089,740 RSUs, Aug 11, 2026–Apr 30, 2027); Julia Brau Donnelly (29,548 shares plus net shares from 341,090 RSUs, Aug 7, 2026–Jun 30, 2027); Matthew Madrigal (up to 121,000 shares, Sep 16, 2026–Jan 15, 2027). Gokul Rajaram plan (Nov 2025) to sell up to 21,000 shares. [10-Q Q2 2026, Part II Item 5; 10-K FY2025, Item 9B]

## 14. Management statements about what will happen (verbatim, 10-Q and in-window 8-Ks)

- Restructuring: "We expect to incur total charges of up to $69.6 million under the Restructuring Plan through the end of the third quarter of 2026. We will record additional charges under the Restructuring Plan as incurred, and the timing and magnitude of such charges are subject to change." [10-Q Q2 2026, Note 11] Original estimate: "approximately $35 million to $45 million, which are expected to be primarily cash-related expenditures... The Company intends to exclude the restructuring charges from its non-GAAP financial measures, including Adjusted EBITDA... Although the Company is reducing its overall staffing levels with these actions in the near term, the Company plans to reinvest in key development areas and strategic opportunities. The Company expects to complete the Plan by the end of its third quarter ending September 30, 2026". [8-K 2026-01-27, Item 2.05]
- AWS: "we are required to purchase at least $4,000.0 million of cloud services from AWS through May 2031... We expect to meet our remaining commitment." [10-Q Q2 2026, Item 2]
- Liquidity: "We believe our existing cash, cash equivalents and marketable securities and amounts available under the 2022 revolving credit facility will be sufficient to meet our working capital and capital expenditure needs over at least the next 12 months, though we may require additional capital resources in the future. We may elect to raise additional capital through the sale of additional equity to fund our future needs beyond the next 12 months." "There have been no other material changes to our material cash requirements or non-cancelable contractual commitments since December 31, 2025." [10-Q Q2 2026, Item 2]
- Taxes: Ireland valuation-allowance release "could be released in the next twelve months... However, the exact timing and amount of the valuation allowance release are subject to change based on our actual operating results." OBBBA: "We are currently evaluating the impact of the legislation on our consolidated financial statements for future periods." [10-Q Q2 2026, Item 2; 10-K FY2025, Item 7]
- Deferred revenue: "We expect materially all of our deferred revenue to be recognized in the subsequent quarter." [10-Q Q2 2026, Note 1]
- Q1 2026 guidance update at the tvScientific closing: "the Company is updating its first quarter 2026 guidance to $958 million to $978 million in revenue and $163 million to $183 million in Adjusted EBITDA to include, in each case, the expected partial-quarter contribution of tvScientific". [8-K 2026-02-18, Item 7.01] (Q1 guidance is historical by the as-of date; recorded for the scorecard.)
- Capex and headcount expectations: no dollar or count outlook is given in the 10-K or 10-Q. Tax-rate expectation: none beyond the Ireland statement. [10-K FY2025; 10-Q Q2 2026]
- User trends: "As of June 30, 2026, global MAUs increased compared to June 30, 2025 primarily due to our ongoing investments in relevance and personalization." [10-Q Q2 2026, Item 2]
- Seasonality expectation: "We expect this seasonality to continue." [10-K FY2025, Item 1]
- Purpose of the Elliott financing/buyback per the 8-K: proceeds of the Notes funded the $1 billion ASR "as part of a new share repurchase program of $3.5 billion". [8-K 2026-03-03, Item 1.01; 10-Q Q2 2026, Item 2]

## 15. Item 5: dividends, splits, market

- "We have never declared or paid dividends on our capital stock and do not intend to pay any dividends in the foreseeable future... In addition, the terms of our revolving credit facility place certain limitations on the amount of dividends we can pay, even if no amounts are currently outstanding." [10-K FY2025, Item 5]
- Stock splits: none mentioned in any fetched filing. IPO: Class A "began trading on April 18, 2019"; "There is no public trading market for our Class B common stock." Holders of record at February 6, 2026: 100 (Class A), 38 (Class B). Aggregate market value of common equity held by non-affiliates at June 30, 2025: "approximately $18.7 billion". Closing price 12/31/2025: $25.89. [10-K FY2025, Item 5; cover; DEF 14A 2026, Outstanding equity awards]

## 16. Non-GAAP measures and subsequent events

- Adjusted EBITDA definition (verbatim): "We define Adjusted EBITDA as net income (loss) adjusted to exclude depreciation and amortization expense, share-based compensation expense, payroll tax expense related to share-based compensation, interest income (expense), net, other income (expense), net, provision for (benefit from) income taxes and certain other non-recurring or non-cash items impacting net income (loss) that we do not consider indicative of our ongoing business performance." Definition change: "We began excluding payroll tax expense related to share-based compensation from Adjusted EBITDA in the fourth quarter of 2024... Prior period amounts have been restated to conform to this presentation." [10-K FY2025, Item 7; 10-Q Q2 2026, Item 2]

| Reconciliation (USD thousands) | FY2023 | FY2024 | FY2025 | Q2 2025 | Q2 2026 | 6M 2025 | 6M 2026 |
|---|---|---|---|---|---|---|---|
| Net income (loss) | (35,610) | 1,862,106 | 416,855 | 38,755 | (46,669) | 47,677 | (120,256) |
| Depreciation and amortization | 21,509 | 21,266 | 25,151 | 6,090 | 10,216 | 11,938 | 17,668 |
| Share-based compensation | 647,860 | 765,795 | 880,463 | 227,234 | 319,729 | 414,660 | 541,850 |
| Payroll tax on share-based compensation | 24,131 | 30,787 | 30,984 | 8,287 | 10,027 | 22,139 | 20,159 |
| Interest (income) expense, net | (105,439) | (127,003) | (110,493) | (28,022) | (7,334) | (55,315) | (25,120) |
| Other (income) expense, net | (3,799) | 19,215 | (15,514) | (10,960) | 1,295 | (15,479) | 2,289 |
| Provision for (benefit from) income taxes | 19,170 | (1,574,501) | 29,035 | (4,103) | (2,490) | (16,690) | 7,597 |
| Legal settlement | — | 34,650 | — | — | — | — | — |
| Restructuring charges | 126,882 | — | — | — | 14,335 | — | 61,432 |
| Non-cash charitable contributions | 12,890 | — | 13,495 | 13,495 | 12,198 | 13,495 | 12,198 |
| Adjusted EBITDA | 707,594 | 1,032,315 | 1,269,976 | 250,776 | 311,307 | 422,425 | 517,817 |
| Adjusted EBITDA margin (company: FY; computed: quarters) | 23% | 28% | 30% | 25.1% | 26.4% | 22.8% | 23.7% |

- [10-K FY2025, Item 7]; [10-Q Q2 2026, Item 2]; margins FY2023–FY2025 as stated in [DEF 14A 2026, Appendix A]. In 6M 2026 the SBC and D&A rows exclude amounts included in restructuring (SBC $4.8 million / $14.1 million; amortization $1.6 million / $2.9 million for Q2 / 6M). [10-Q Q2 2026, Item 2]
- Constant-currency revenue and free cash flow definitions: see sections 2b and 6a.
- Subsequent events in the 10-K (Note 12): the January 26, 2026 restructuring announcement and the December 2025 agreement "to acquire tvScientific, a connected TV performance advertising platform, for $450.0 million in cash, subject to certain adjustments. The transaction is expected to close in the first half of 2026". [10-K FY2025, Note 12] The 10-Q has no subsequent-events note (notes run 1–12, ending with "Related Party"). [10-Q Q2 2026, Item 1]
- tvScientific as closed: February 17, 2026; "The total purchase consideration was $465.1 million, which was primarily in cash. We also issued replacement share-based awards with a grant date fair value of $24.1 million"; allocation "$59.0 million to developed technology, $25.0 million to customer relationships, $375.1 million to goodwill"; "The acquisition did not have a material impact on our condensed consolidated financial statements so we have not presented historical and pro forma disclosures." Cash paid, net of cash acquired: 446,954 thousand. [10-Q Q2 2026, Note 3; Item 1]

## 17. 8-K events inside the as-of window (filed after the 10-K, before 2026-08-04)

| Filed | Items | Substance |
|---|---|---|
| 2026-01-20 | 7.01 | Claude (Lee) Brown appointed Chief Business Officer effective January 20, 2026 (ex-DoorDash CRO, ex-Spotify). |
| 2026-01-27 | 2.05 | Board-approved global restructuring: "reduction in force that is expected to affect less than 15% of the Company's workforce as well as office space reductions"; $35–45 million pre-tax charges expected; completion by end of Q3 2026; charges to be excluded from Adjusted EBITDA. |
| 2026-02-09 | 5.02, 7.01, 9.01 | Kecia Steelman (President and CEO, Ulta Beauty) appointed independent Class II director effective February 16, 2026; joins compensation committee. |
| 2026-02-18 | 7.01 | tvScientific acquisition closed February 17, 2026; Q1 2026 guidance updated to revenue $958–978 million and Adjusted EBITDA $163–183 million including tvScientific's partial quarter. |
| 2026-03-03 | 1.01, 2.03, 3.02, 8.01, 9.01 | Investment Agreement with Elliott for $1 billion of 1.75% convertible senior notes due 2031 (conversion price ~$22.72); $1 billion ASR with Goldman Sachs; new $3.5 billion repurchase program approved March 2, 2026, replacing the November 2024 program ($473 million repurchased year to date); Elliott governance rights (Steinberg seat), two-year lock-up, standstill. |
| 2026-03-05 | 1.01, 2.03, 3.02, 9.01 | Closing of the Notes issuance; indenture with U.S. Bank Trust Company dated March 5, 2026. |
| 2026-05-26 | 5.07 | Annual meeting results (May 21, 2026): four Class I directors elected; say-on-pay approved; annual say-on-pay frequency; EY ratified. Class B voted 20 votes per share. |

- Earnings 8-Ks of 2026-02-12, 2026-05-04 and 2026-08-04 (Item 2.02) were not fetched (IR gatherer's scope). 8-Ks filed 2026-08-07 and 2026-08-28 are after the cutoff and were not fetched.

## 18. Data gaps (not in fetched sources)

- MAUs by region (U.S. and Canada / Europe / Rest of World) for every period, and quarterly MAUs, revenue and ARPU: chart images only in every 10-K and 10-Q. Only global year-end MAUs, annual ARPU by region, and the current-period regional revenue prose survive in text.
- FY2021 revenue by user geography, FY2021 ARPU by region, and 12/31/2021 global MAU count (the FY2022 10-K gives only growth rates: MAUs +4%, global ARPU +10%, US&C ARPU +16%, Europe +7%, RoW +49%).
- Q2 2025 and six-month ARPU by region; Q2 2025 and 6M 2025 revenue by user geography in dollars.
- Headcount at 12/31/2021.
- FY2021 Adjusted EBITDA under the current (payroll-tax-excluding) definition.
- Revenue split by advertiser size, by agency vs direct, by objective (dollar terms), by ad format, or from third-party demand partners; identity of third-party ad demand partners.
- Hosting cost as a dollar figure (only the AWS commitment schedule and accrued hosting expenses are disclosed).
- Any capex, headcount, tax-rate or margin outlook in dollar or percentage terms.
- Lee Brown's age; Elliott's share ownership.
