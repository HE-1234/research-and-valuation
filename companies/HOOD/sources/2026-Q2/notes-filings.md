# Robinhood Markets, Inc. (HOOD) — Filings notes, as of Q2 2026

_Gatherer: filings (resumed run). As-of quarter Q2 2026 (quarter ended 2026-06-30). As-of cutoff 2026-07-30 (earnings call 2026-07-29 5 p.m. ET; 10-Q filed 2026-07-30). Written 2026-09-09. Structured facts only; no interpretation. Nothing filed after 2026-07-30 was read._
_Dollar figures are USD millions unless a table says otherwise; Robinhood's own statements are presented in millions. Fiscal year = calendar year (FYE 12-31). Items marked "(computed)" are arithmetic on disclosed figures and are not presented as such by the company. "Not in fetched sources" means the cached filings do not contain the figure. Each bullet carries a source tag and, where useful, the line number in the cached .txt file ("L1234") for the reviewer._

**Tag key** (all files in `companies/HOOD/sources/2026-Q2/`)
- `[10-K FY2025, ...]` = Annual report for FY2025 → `10-K-FY2025.txt`. **This cached text is the Form 10-K/A filed 2026-02-20 (accession 0001783879-26-000029), not the original Form 10-K filed 2026-02-18 (accession 0001783879-26-000023).** The Explanatory Note (L89–L91) says the amendment "is being filed solely to address technical issues with formatting portions of the Original Form 10-K that occurred during the electronic transmission of the EDGAR-formatted file", limited to tables on page 3 and heading placement on pages 127–137, "does not change any previously reported financial results", and "includes the Original Form 10-K in its entirety". It is therefore used as the FY2025 10-K throughout and tagged `[10-K FY2025, ...]`.
- `[10-K FY2024, ...]` = Annual report for FY2024, filed 2025-02-18 → `10-K-FY2024.txt` (fetched this run; FY2022–FY2024 statements, KPIs incl. Gold Subscribers 2022–2024)
- `[10-K FY2023, ...]` = Annual report for FY2023, filed 2024-02-27 → `10-K-FY2023.txt` (FY2021–FY2023 statements and KPIs)
- `[10-K FY2022, ...]` = Annual report for FY2022, filed 2023-02-27 → `10-K-FY2022.txt` (fetched this run only for FY2021 Gold subscribers, 12/31/2021 balance sheet and 2022 restructuring headcounts)
- `[10-Q Q2 2026, ...]` = Quarterly report for the quarter ended 2026-06-30, filed 2026-07-30 → `10-Q-2026-Q2.txt`
- `[10-Q Q1 2026, ...]` = Quarterly report for the quarter ended 2026-03-31, filed 2026-04-29 → `10-Q-2026-Q1.txt` (fetched this run so that Q1 2026 revenue lines, KPIs and the 3/31/2026 balance sheet are taken directly rather than computed)
- `[DEF 14A 2026, <section>]` = Proxy statement filed 2026-04-22 (annual meeting 2026-06-02; record date 2026-04-08) → `DEF14A-2026.txt`
- `[8-K YYYY-MM-DD, Item x.xx]` = Current report filed on that date → `8-K-YYYY-MM-DD.txt`; `[8-K/A 2026-03-24]` → `8-KA-2026-03-24.txt`; exhibits `8-K-2026-06-23-ex991.txt` / `-ex992.txt` (convertible-notes launch and pricing releases) and `8-K-2026-01-30-ex991-606-RHF.txt` (Robinhood Financial LLC Rule 606(a) order-routing report, Q4 2025)
- `[40-APP 2026-07-14]` / `[40-6B 2026-07-16]` = Investment Company Act exemptive applications → `40-APP-2026-07-14.txt`, `40-6B-2026-07-16.txt`

**Reading notes on the sources.** (a) Robinhood reports one operating segment and no gross profit or "operating income" line; its income statement goes from total operating expenses to "Other income, net" and "Income before income taxes". (b) The FY2023 10-K presents FY2021–FY2022 operating expenses without a separate "Provision for credit losses" line (folded into "Operations"); the FY2024 10-K re-presents FY2022 with the separate line. (c) From Q1 2026 the 10-Qs break out "Event contracts" as its own transaction-revenue line (previously inside "Other") and net interest paid to users on uninvested cash against segregated-cash interest; prior periods are reclassified ("Certain reclassifications have been made to prior period amounts") [10-Q Q2 2026, Note 1, L667]. (d) Assets Under Custody (AUC) was renamed Total Platform Assets and widened to include TradePMR RIA assets and Bitstamp crypto from 2025 [10-K FY2025, glossary L231]. (e) Text tables are intact in every cached file (no chart-image losses were found for the KPI or revenue tables).

---

## 1. Business description in the company's own words

- "Robinhood was founded in 2013 on the belief that everyone should be welcome to participate in our financial system. We are creating modern financial services platforms for everyone, regardless of their wealth, income, or background." [10-K FY2025, Item 1, L399]
- "Our mission is to democratize finance for all. ... Over the last decade, we have disrupted and changed the industry, becoming the first U.S. retail broker to offer commission-free stock trading with no account minimums, which was subsequently adopted by the rest of the industry. In recent years, we have continued to build relationships with our customers by introducing new products and diversifying our services that further expand access to the financial system, including focusing on products and tools for more seasoned investors." [10-K FY2025, Item 1, L401]
- Note 1 one-liner: "Our platforms enable customers to buy, sell, and trade equities, options, event contracts, and futures, as well as buy, sell, and transfer cryptocurrencies. We are also responsible for the custody of user-held cryptocurrencies. In addition, we offer credit cards with certain rewards offerings, as well as a cash card and spending account that help our customers in investing, saving, and earning rewards." [10-Q Q2 2026, Note 1, L651]
- Values statements: "We know that trust is hard earned and easily lost and that is why we prioritize compliance, approach risk thoughtfully, and never compromise trust for speed." ... "We also strive to do more with less. To that end, constraint drives us to innovate through scalable technology - not excess resources." [10-K FY2025, Item 1, L403–L405]
- Customers: "many of our customers have told us that Robinhood was their first brokerage account ... We are also laser focused on being the top platform for active traders who trade more actively and use more sophisticated products." [10-K FY2025, Item 1, "Our Customers", L521]
- "We refer to our 'users' and our 'customers' interchangeably". [10-K FY2025, Item 7, L2164]

### 1a. Products, as listed in Item 1 (each row is the company's own description, abridged)

| Product family | What the 10-K says |
|---|---|
| Brokerage | Commission-free U.S.-listed stocks, ETFs, options and ADRs; options approval Levels 2 and 3; index options (all customers from 2025); fractional trading from $1; recurring investments; margin ("tiered margin structure where customers receive a single low interest rate based on their total margin balance"); Fully-Paid Securities Lending; Cash Sweep to partner banks (FDIC-eligible); instant withdrawals for a fee; Robinhood Retirement (IRA match, five-year hold); 24 Hour Market ("first U.S. broker to offer around-the-clock trading of individual stocks, 24 hours a day, 5 days a week"); joint accounts; Prediction Markets Hub (event contracts "on a regulated exchange ... for which we charge a commission for each contract traded", offered through RHD's FCM licence); futures (commissions per contract); short selling (launched Q4 2025). Robinhood Legend is a "browser-based desktop trading platform ... available at no additional cost to all U.S. and U.K. customers". [10-K FY2025, Item 1, L419–L435] |
| U.K. brokerage (RHUK) | Since 2024, "most of our brokerage services" via a dedicated app; multi-currency wallets (GBP); stocks and shares ISAs "recently launched". [10-K FY2025, Item 1, L437] |
| Stock Tokens (EU) | "A stock token is a derivative contract that tracks the price of a U.S. stock or ETP, giving eligible EU customers exposure to U.S. equities without owning the underlying shares"; 24/5, zero commissions or added spreads. [10-K FY2025, Item 1, L439] |
| Robinhood Crypto (RHC, U.S.) | Trading in every U.S. state; "Customers trading in the Robinhood app can choose to have orders routed to market makers commission-free or through partner exchanges via smart exchange routing for a fee. Orders placed on Robinhood Legend are all routed to the partner exchanges via smart exchange routing." 58 supported cryptocurrencies. "As an agent, we route all cryptocurrency transactions initiated by customers to third-party market makers or exchange liquidity providers. We never act as a counterparty to our users' buy or sell transactions." Also Crypto Transfers, Robinhood Connect (fiat-to-crypto on-ramp for dApps, fee), Crypto Trading API, staking. [10-K FY2025, Item 1, L447] |
| Robinhood Crypto (RHEU, EU) | Commission per trade; 74 cryptocurrencies; staking; perpetual futures ("This new asset class gives advanced traders more ways to trade ... with leverage available"); "During 2025, we acquired Bitstamp, a globally-scaled cryptocurrency exchange with retail and institutional customers. This acquisition accelerates our expansion across Europe." [10-K FY2025, Item 1, L449] |
| Crypto custody | Hot and cold wallets; "With the exception of Bitstamp ... we do not utilize third-party custodians for settled cryptocurrencies"; "the overwhelming majority of cryptocurrency coins on our platforms are held in cold storage, in facilities located in the United States and in the EU"; omnibus wallets; "We currently do not hold significant amounts of cryptocurrency for our own account ... We do not engage in lending transactions with cryptocurrencies held on behalf of customers. We do not seek to profit from proprietary trading and only facilitate customer transactions." [10-K FY2025, Item 1, L454] |
| Robinhood Wallet | Self-custody web3 wallet in over 150 countries via Cayman subsidiary Robinhood Non-Custodial Ltd.; no share of network fees. [10-K FY2025, Item 1, L456] |
| Robinhood Gold | Subscription ("After an initial 30-day free trial, subscribers pay a flat recurring rate"): higher Cash Sweep rate, 3% IRA match, bigger instant deposits, no interest on first $1,000 of margin, lower index-option/futures fees and a cap on Strategies fees, exclusive mortgage rates (Sage Home Loans), Morningstar research, Nasdaq Level II data. [10-K FY2025, Item 1, L461] |
| Robinhood Gold Card | Issued by Coastal Bank under a Program Agreement; no annual or foreign transaction fees; "exclusively for qualified Gold Subscribers"; "now in the hands of over 600 thousand customers". [10-K FY2025, Item 1, L462] |
| Robinhood Banking (RHY) | "brings a private banking experience exclusively to Gold Subscribers. Banking services are provided by Coastal Bank"; high-yield checking and savings, on-demand cash delivery, 24/7 support; "invite-only launch" (Regulation section). [10-K FY2025, Item 1, L463; L697] |
| Wealth management | Robinhood Strategies: "0.25% annual management fee, capped at $250 per year for Gold Subscribers"; TradePMR: "a custodial and portfolio management platform for RIAs". [10-K FY2025, Item 1, L469] |
| Robinhood Cortex | AI investment tool (stock and portfolio digests). [10-K FY2025, Item 1, L470] |
| Robinhood Ventures Fund I (RVI) | "In September 2025, we filed our initial prospectus to launch RVI, a listed closed-end fund that aims to offer retail investors exposure to private companies". [10-K FY2025, Item 1, L471] RVI IPO'd on the NYSE 2026-03-06 and was deconsolidated in June 2026 (section 19). [10-Q Q2 2026, Note 1, L655] |
| Media / education | Robinhood Learn, in-app education, newsfeeds (Barron's, Reuters, Dow Jones), Sherwood Media and Robinhood Snacks (advertising revenue), Crypto Learn and Earn. [10-K FY2025, Item 1, L477–L491] |

### 1b. History and acquisitions (as stated in the filings)

- Founded 2013 by Vladimir Tenev and Baiju Bhatt; Class A listed on Nasdaq under "HOOD" since July 29, 2021 (IPO closing price used in the performance graph: $34.82); IPO closed August 2, 2021. [10-K FY2025, Item 5, L2105, L2152; DEF 14A 2026, "Corporate Governance", L1147]
- Self-clearing since November 2018 (previously a third-party clearing firm). [10-K FY2023, Item 1A, L1548]
- Early 2021 Trading Restrictions: from January 28, 2021 RHS "temporarily restricted or limited its customers' purchase of certain securities, including GameStop Corp. and AMC Entertainment Holdings, Inc." because of NSCC deposit requirements; capital raised at the time included February 2021 convertible notes ($2,532.0 million Tranche I plus warrants) [10-K FY2025, Note 15, L4578; DEF 14A 2026, "Transactions with Related Persons", L2594]. The FY2021 income statement carries a $2,045 million "Change in fair value of convertible notes and warrant liability". [10-K FY2023, Item 8, L2601]
- Say Technologies: "On August 13, 2021, we acquired all outstanding stock of Say Technologies. New York-based Say Technologies, founded in 2017, is an investor communications and shareholder engagement platform." Consideration: "The acquisition date fair value of the consideration transferred for Say Technologies was $133 million". [10-K FY2022, Note 3, L3098–L3104] Proxy services later "transitioning ... to Say Technologies, our wholly-owned subsidiary, from a third-party proxy service company" drove FY2023 proxy revenue growth. [10-K FY2023, Item 7, L2128] The FY2021 cash-flow statement shows "Acquisitions of a business, net of cash and cash equivalents acquired $(125) million". [10-K FY2023, Item 8, L2661]
- X1 / Robinhood Credit: "On July 3, 2023, we acquired all of the outstanding equity of X1 Inc. ('X1'), a U.S.-based company that offers a no-fee credit card with rewards on each purchase ... In August 2023, X1 was renamed Robinhood Credit." Consideration "$104 million, which was entirely paid in cash". [10-K FY2023, Note 3, L3213–L3215]
- Ziglu: "in April 2022 we signed a definitive agreement to acquire Ziglu Limited ('Ziglu'), a U.K.-based electronic money institution and crypto-asset firm. However, as a result of prolonged regulatory uncertainty ... we notified Ziglu of the termination of the agreement in February 2023"; $12 million of advances to Ziglu were impaired to zero. [10-K FY2022, Item 1A, L833; Item 7, L1691, L1777] Pluto: not named in any fetched filing text that was read.
- TradePMR: acquired February 26, 2025; consideration ~$175 million cash (finalised to $169 million in Q1 2026) plus 2,049,711 unvested Class A shares (~$100 million) vesting over four years as post-close compensation; goodwill $111 million preliminary / $105 million final; intangibles $81 million (customer relationships $49 million/13 years, developed technology $31 million/5 years). [10-K FY2025, Note 3, L3609–L3648; 10-Q Q2 2026, Note 3, L720–L750]
- Bitstamp: acquired June 2, 2025 for ~$224 million cash; balance sheet acquired included $1,103 million segregated cash/securities and $1,115 million payables to users; goodwill $93 million; intangibles $70 million (developed technology $39 million, licences $21 million). Bitstamp "currently has entities operating internationally in the U.K., EU, Singapore, and the British Virgin Islands". [10-K FY2025, Note 3, L3650–L3700; Item 1A, L1125]
- MIAXdx: joint venture Rothera with SIG (Susquehanna) formed November 2025 acquired 90% of MIAXdx on January 20, 2026 for ~$79 million cash (SIG contributed $41 million); renamed Rothera E&C; intangibles $47 million of licences; Rothera "has the ability to purchase half of the outstanding 10%" held by Miami International Holdings within three years. Robinhood consolidates Rothera but "We do not wholly own or operationally control Rothera". [10-Q Q2 2026, Note 3, L783–L809; 10-K FY2025, Item 1A, L1109–L1121]
- WonderFi (Canada): agreement May 12, 2025 at C$0.36 per share (~$180 million equity value); closed June 1, 2026 for ~$178 million cash; goodwill $120 million; intangibles $50 million; its subsidiary CCML is a CIRO-registered investment dealer. [10-K FY2025, Item 7, L2212; 10-Q Q2 2026, Note 3, L811–L845; Item 1A, L2669]
- Indonesia: agreements in December 2025 to acquire PT Buana Capital Sekuritas (brokerage) and PT Pedagang Aset Kripto (digital asset trader), pending regulatory approval at the 10-K date; not mentioned as closed in the Q2 2026 10-Q text read. [10-K FY2025, Item 7, L2214]
- Trump Accounts: "In April 2026, we announced that Robinhood will serve as broker and sole initial trustee for Trump Accounts on behalf of the U.S. Department of the Treasury. Robinhood will work with BNY ... for which Robinhood will earn revenue"; launched July 4, 2026. [10-Q Q2 2026, Note 1, L655]
- Robinhood Chain: "In July 2026, we launched the Robinhood Chain, a permissionless, Ethereum-compatible Layer 2 blockchain built for financial services and tokenized real-world assets." [10-Q Q2 2026, Item 1A, L3317]

### 1c. Legal entities and licences (glossary and Regulation section)

- RHM = Robinhood Markets, Inc. (parent). RHF = Robinhood Financial LLC (introducing broker-dealer). RHS = Robinhood Securities, LLC (clearing broker-dealer). RHC = Robinhood Crypto, LLC (state money transmitter; FinCEN-registered). RHY = Robinhood Money, LLC (money transmitter; Robinhood Banking/spending). RHD = Robinhood Derivatives, LLC (CFTC-registered FCM, NFA member, registered swap firm). RHUK (FCA-authorised). RHEU = Robinhood Europe, UAB (Bank of Lithuania; MiCA and MiFID licences). RAM = Robinhood Asset Management, LLC and RHV (SEC-registered investment advisers). RHSG = Robinhood Singapore Pte. Ltd. TradePMR = Trade-PMR, Inc. (broker-dealer). Robinhood Credit (credit card programme with Coastal Bank). Bitstamp Ltd. [10-K FY2025, glossary L150–L220; Regulation L679–L775]
- "We are a licensed introducing broker-dealer, a licensed clearing broker-dealer, a licensed money-transmitter, and a registered futures commission merchant." [10-K FY2025, Item 1, L619]
- RHSG "is currently applying for its Capital Markets Services license with the MAS" at the 10-K date [10-K FY2025, L739]; "was granted a capital markets service license on July 1, 2026". [10-Q Q2 2026, Item 1A, L2669]
- Regulators named: SEC, FINRA, CFTC, NFA, CFPB, FDIC, OFAC, FinCEN, state regulators (MSD, CAGO, NYDFS), FCA (U.K.), Bank of Lithuania, MAS, Luxembourg CSSF, Slovenia ATVP. [10-K FY2025, Item 1A, L1225]

### 1d. Growth strategy (verbatim headings and priorities)

- Three "key focus areas": "Establishing Ourselves as the Number One Platform for Active Traders" (Cortex; "expansion of asset classes and capabilities such as event contracts and short selling"; "improving our tools, latency, and charting ... particularly on Robinhood Legend"); "Becoming the Number One in Wallet Share for the Next Generation" ("build new products that cover the next generation's remaining core financial needs, such as Robinhood Banking and advisory"; "innovate on incentives, particularly through Robinhood Gold"; "reduce withdrawals and increase deposits"); "Building the Number One Global Financial Ecosystem" ("launch new products and features that further our tokenization efforts, such as Robinhood Chain, a permissionless Layer 2 blockchain optimized for real-world assets"; multi-currency accounts, staking and stock tokens in the EU; ISAs in the U.K.). [10-K FY2025, Item 1, L531–L567]
- "This drove our decision to open an office in Singapore as our APAC headquarters." [10-K FY2025, Item 1, L569]
- Two platform shifts: "we believe we are strategically positioned at the center of two major platform shifts—AI and cryptocurrency and blockchain technology". AI "in three phases: by augmenting internal operations, by enhancing customer-facing products, and by developing sophisticated autonomous financial agents ... expect to introduce significantly more in the coming year, including our first AI-native advisory products." Crypto: "We anticipate that blockchain technology will increasingly integrate with the traditional financial system, ultimately serving as the new infrastructure for financial services. We expect that this will be driven by tokenization". [10-K FY2025, Item 1, L513–L517]
- Order routing: "We built a proprietary order routing system that uses statistical models to evaluate past orders and execution quality data, and automatically routes customer orders to the market makers that have historically given customers the best prices. This competition-based system creates an incentive for market makers to provide better prices for our customers, in order to receive more orders in the future." Core infrastructure "built on Amazon Web Services". [10-K FY2025, Item 1, L499–L507]
- Competition: "large legacy financial institutions, large technology companies, and smaller, new financial technology entrants"; key factors listed as product innovation, operating efficiency, engineering talent, brand recognition, security and trust, cloud-based architecture, regulatory licenses, vertical integration; "we have developed a business model that is difficult to replicate." [10-K FY2025, Item 1, L571–L593]
- Seasonality: "retail interest in investing and cryptocurrency trading ... varying numbers of trading days ... proxy and investor communications activity during proxy season. Seasonal trends may be superseded by market or macroeconomic events". [10-K FY2025, Item 1, L629]

### 1e. Headcount, offices, international footprint

| Date | Full-time employees | Source |
|---|---|---|
| 12/31/2021 | not in fetched sources (FY2021 10-K not fetched) | — |
| 12/31/2022 | ~2,300 | [10-K FY2022, Item 1, L445] |
| 12/31/2023 | ~2,200 | [10-K FY2023, Item 1, L478] |
| 12/31/2024 | ~2,300 | [10-K FY2024, Item 1, L575] |
| 12/31/2025 | ~2,900 (proxy: 2,958 persons, "all of whom were regular full-time employees"; 2,606 in North America, 337 in Europe, 15 in Asia) | [10-K FY2025, Item 1, L643; DEF 14A 2026, "CEO Pay Ratio", L2216] |
| June 2026 | Reduction in force of "approximately 10% of the Company's full-time employees" announced June 16, 2026 | [8-K 2026-06-16, Item 2.05] |

- 2022 restructurings: April 26, 2022, ~330 employees (~9% of full-time employees at the time); August 2, 2022, ~780 employees (~23%), closure of two offices. [10-K FY2022, Item 7, L1683–L1685]
- Headquarters: Menlo Park, California, "lease commitments for multiple facilities with various expiration dates through 2036"; other leased offices "throughout the United States and other countries". [10-K FY2025, Item 2, L2083]
- Where it operates: "We currently only offer select services to the public outside the U.S. in certain jurisdictions, including brokerage and futures services in the U.K. through RHUK, crypto and brokerage services in the EU, through RHEU, and our Robinhood Wallet, which is available in over 150 countries ... In addition, Bitstamp ... currently has entities operating internationally in the U.K., EU, Singapore, and the British Virgin Islands, and also offers services in other countries globally." [10-K FY2025, Item 1A, L1125] "Substantially all of our revenues and assets are attributed to or located in the United States." [10-K FY2025, Note 1, L3243]
- "This has led to our international customer base growing to over 750,000." [DEF 14A 2026, CD&A "2025 Business Highlights", L1629]
- Subject to laws in "the U.S., the U.K., the EU, the United Arab Emirates, Singapore, the British Virgin Islands, and in other countries and regions". [10-K FY2025, Item 1A, L1187]

---

## 2. Segment and key performance metrics

- One operating segment: "Our CODM is our CEO and President, Vladimir Tenev. We operate and report financial information in one operating segment. This is because our CODM utilizes consolidated net income (loss) and company-wide key performance metrics ... to allocate resources and determine performance." The company is "organized in a GM structure" but "GM level financial information is not currently shared with and used by the CODM". [10-K FY2025, Note 1, L3243–L3245]

### 2a. KPI definitions (current)

- Funded Customers: "a unique person who has at least one account with a Robinhood entity and, within the past 45 calendar days (a) had an account balance that was greater than zero ... or (b) completed a transaction"; joint-account holders each count; TradePMR RIA clients from Q1 2025 and Bitstamp customers from June 2025 are included. Before Q4 2023 the metric was called Net Cumulative Funded Accounts (same calculation). [10-K FY2025, glossary L229; 10-K FY2023, Item 7, L1764]
- Total Platform Assets: fair value of equities, options, crypto, futures/event contracts and customer cash, net of receivables from users, "(previously reported as Assets Under Custody)", plus RIA assets on TradePMR's platform not custodied by Robinhood; includes Bitstamp crypto from June 2025. [10-K FY2025, glossary L231]
- Net Deposits: cash deposits and asset transfers in plus dividends, interest, staking rewards and promotion credits, net of reversals, withdrawals, margin and lending interest, Gold fees and assets transferred out; includes Bitstamp from June 2025; excludes TradePMR ("Due to data limitations"). Growth rate = 12-month Net Deposits ÷ Total Platform Assets at the start of the period (annualized for quarters). [10-K FY2025, glossary L230; 10-K FY2023, Item 7, L1778]
- ARPU: total revenue ÷ average of Funded Customers at the start and end of the period (annualized for quarters). [10-K FY2025, glossary L228]
- Robinhood Gold Subscribers: unique person subscribed at period end who "has made at least one Robinhood Gold subscription fee payment". [10-K FY2025, glossary L232]
- Investment Accounts (new in 2025): funded individual brokerage, joint, IRA or TradePMR RIA accounts; excludes Bitstamp. [10-K FY2025, glossary L239]
- Cash Sweep: off-balance-sheet balance of customer cash swept to program banks; Robinhood earns the spread. [10-K FY2025, glossary L236]
- MAU was reported through FY2023 (17.3 million FY2021, 11.4 million FY2022, 10.9 million FY2023) and does not appear in the FY2024 or FY2025 KPI tables. [10-K FY2023, Item 7, L1844; 10-K FY2024, Item 7, L2000–L2010]

### 2b. Annual KPIs, FY2021–FY2025

| KPI | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| Funded Customers (millions, year-end) | 22.7 | 23.0 | 23.4 | 25.2 | 27.0 |
| Investment Accounts (millions) | n/d | n/d | n/d | 26.2 | 28.4 |
| AUC / Total Platform Assets ($ billions) | 98.0 | 62.2 | 102.6 | 192.9 | 322.1 |
| Net Deposits ($ billions) | 27.1 | 18.4 | 17.1 | 50.5 | 68.1 |
| Net Deposits growth rate | 43% | 19% | 27% | 49% | 35% |
| ARPU ($) | 103 | 60 | 80 | 122 | 171 |
| Gold Subscribers (millions) | ~1.3 (prose) | 1.14 | 1.42 | 2.64 | 4.18 |
| MAU (millions) | 17.3 | 11.4 | 10.9 | n/d | n/d |

- Sources: FY2021–FY2023 [10-K FY2023, Item 7, L1844–L1848]; FY2022–FY2024 incl. Gold [10-K FY2024, Item 7, L2004–L2009]; FY2024–FY2025 incl. Investment Accounts [10-K FY2025, Item 7, L2180–L2231]. FY2021 Gold: "a decrease in paid subscribers to Robinhood Gold from 1.3 million to 1.1 million" (2021 to 2022) [10-K FY2022, Item 7, L2027]. n/d = not disclosed in that year's KPI table. Note the 2025 TPA figure "were revised to reflect final crypto pricing data" after the February 10, 2026 release. [10-K FY2025, L2266]
- Funded Customer roll-forward (millions): FY2021 begin 12.5 / new 12.2 / resurrected 0.5 / churned (2.5) / end 22.7; FY2022 22.7 / 1.3 / 0.2 / (1.2) / 23.0; FY2023 23.0 / 1.1 / 0.2 / (0.9) / 23.4; FY2024 23.4 / 2.2 / 0.5 / (0.9) / 25.2; FY2025 25.2 / 2.5 / 0.4 / acquired 0.6 / (1.7) / 27.0. [10-K FY2023, L1857–L1861; 10-K FY2025, L2235–L2242]
- Total Platform Assets by asset ($ billions): FY2021 equities 72.1 / crypto 22.1 / options 1.5 / cash 8.8 / receivables (6.5); FY2022 45.8 / 8.4 / 0.3 / 10.8 / (3.1); FY2023 69.4 / 14.7 / 0.6 / 21.3 / (3.4); FY2024 130.6 / 35.2 / options and futures 1.8 / RIA — / 33.3 / (8.0); FY2025 212.0 / 38.2 / 2.8 / RIA 42.5 / 43.4 / (16.8). Change in FY2025: begin 192.9 + acquired 51.8 + Net Deposits 68.1 + net market gains 9.3 = 322.1. [10-K FY2023, L1866–L1885; 10-K FY2025, L2246–L2264]

### 2c. Quarterly KPIs

| KPI | Q1 2025 | Q2 2025 | Q1 2026 | Q2 2026 |
|---|---|---|---|---|
| Funded Customers (millions) | 25.8 | 26.5 | 27.4 | 28.4 |
| Investment Accounts (millions) | n/d | 27.4 | n/d | 29.9 |
| Total Platform Assets ($ billions) | 220.6 | 278.6 | 307.3 | 368.7 |
| Net Deposits ($ billions) | 18.0 | 13.8 | 17.7 | 21.7 |
| Annualized Net Deposits growth rate | 37% | 25% | 22% | 28% |
| ARPU ($, annualized) | 145 | 151 | 157 | 187 |
| Gold Subscribers (millions) | 3.19 | 3.48 | 4.34 | 4.84 |

- Sources: [10-Q Q1 2026, Item 2, L1481–L1495]; [10-Q Q2 2026, Item 2, L1611–L1690]. Trailing-twelve-month Net Deposits to Q2 2026: $75.7 billion, "a growth rate of 27% relative to Total Platform Assets at the end of the second quarter of 2025". [10-Q Q2 2026, L1621]
- Q2 2026 Funded Customer roll-forward (millions): begin 27.4, new 0.9, resurrected 0.2, acquired 0.3, churned (0.4), end 28.4 (Q2 2025: 25.8 / 0.6 / 0.1 / 0.5 / (0.5) / 26.5). [10-Q Q2 2026, L1657–L1664]
- Q2 2026 Total Platform Assets ($ billions): equities 265.5, crypto 26.3 (down 36% y/y from 41.1), options and futures 2.9, RIA assets 50.0, cash 45.6, receivables (21.6); change in quarter: begin 307.3 + acquired 0.7 + Net Deposits 21.7 + net market gains 39.0. Q1 2026: 207.5 / 30.5 / 2.0 / 42.6 / 41.6 / (16.9); Q1 change: 322.1 + 17.7 − 32.5 market losses = 307.3. [10-Q Q2 2026, L1668–L1690; 10-Q Q1 2026, L1508–L1528]
- Proxy highlight: "customers traded over 12 billion event contracts in 2025"; "At the end of 2025, more than 40% of our Total Platform Assets were across ETFs, Advisory, Retirement, and Cash"; Gold Card "over 5 times to over 600,000 cardholders"; Bitstamp "volumes more than doubling since the acquisition closed in June 2025". [DEF 14A 2026, CD&A, L1623–L1629]

---

## 3. Revenue by line

### 3a. How each revenue line is earned (company wording)

- Transaction-based revenues: "consist of amounts earned from routing customer orders for options, cryptocurrencies, and equities to market makers. When customers place orders for options, cryptocurrencies, or equities on our platform, we route these orders to market makers and we receive consideration from those market makers. With respect to options and equities trading, such fees are known as PFOF. With respect to cryptocurrencies trading, we receive 'Transaction Rebates' when routing to market makers. In the case of options, our fee is on a per contract basis based on the underlying security. For equities, the fees we receive are typically based on the size of the publicly quoted bid-ask spread for the security being traded; that is, we receive a fixed percentage of the difference between the publicly quoted bid and ask at the time the trade is executed. In the case of cryptocurrencies, our rebate is a fixed percentage of the notional order value." [10-K FY2025, Item 7, L2314]
- "Within each asset class, whether options, cryptocurrencies, or equities, the transaction-based revenue we earn is calculated in an identical manner among all participating market makers. We route option and equity orders in priority to participating market makers that we believe are most likely to give our customers the best execution, based on historical performance ... For cryptocurrency orders, we route to market makers based on price and availability of the cryptocurrency from the market maker." [10-K FY2025, Item 7, L2316] "For each trade type, all market makers pay the same transaction price. Payments are collected monthly in arrears from each market maker." [10-K FY2025, Note 1, L3261]
- "We also earn transaction-based revenues from commissions. Acting as an agent, we facilitate purchases and sales of event contracts and futures on behalf of users. Commissions are recognized on a trade-date basis". [10-K FY2025, Item 7, L2318]
- Net interest revenues: "interest revenues less interest expenses. We earn interest revenues on margin loans to users, segregated cash, cash equivalents, and securities, deposits with clearing organizations, corporate cash and investments, Cash Sweep, and carried customer credit card balances. We also earn and incur interest revenues and expenses on securities lending transactions. We incur interest expenses in connection with our revolving credit facilities and borrowings by the Credit Card Funding Trust." [10-K FY2025, Item 7, L2322]
- Other revenues: "primarily consists of Robinhood Gold subscription fees, proxy revenues, digital asset listing fees, selling concession revenues, advertising revenues, and ACATS fees". Proxy revenue is earned "directly from issuers through Say Technologies"; selling concessions come "from IPO activities"; advertising from Sherwood Media. [10-K FY2025, Item 7, L2326; Note 1, L3269–L3271]
- Robinhood Match Incentives (IRA match, transfer matches): "recognized as a reduction to revenue when earned. The matches are allocated to certain revenue categories on a proportional basis." FY2025 match incentives reduced options revenue by $55 million more than in FY2024, crypto by $18 million and equities by $14 million (year-over-year increases in the deduction). [10-K FY2025, Item 7, L2330; L2430–L2434]
- The auditor's critical audit matter: of FY2025 transaction-based revenues of $2,628 million, "$2,326 million is comprised of revenues earned from routing user orders to market makers" (the balance is commissions on event contracts/futures and other). [10-K FY2025, Item 8, EY report, L2881]

### 3b. Transaction-based revenues by asset class, FY2021–FY2025 ($ millions)

| | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| Options | 690 | 488 | 505 | 760 | 1,123 |
| Cryptocurrencies | 420 | 202 | 135 | 626 | 901 |
| Equities | 287 | 117 | 104 | 177 | 302 |
| Other (incl. event contracts, futures, instant withdrawals) | 5 | 7 | 41 | 84 | 302 |
| Total transaction-based | 1,402 | 814 | 785 | 1,647 | 2,628 |
| Transaction-based as % of total net revenues | 77% | 60% | 42% | 56% | 59% |

- Sources: FY2021–FY2023 [10-K FY2023, Item 7, L2030–L2036]; FY2024–FY2025 [10-K FY2025, Item 7, L2422–L2426; Note 5, L3772–L3776].
- FY2025 drivers: options +$363 million "primarily due to higher option rebate rates due to the mix of ticker symbols traded ... a 12% increase in Options Contracts Traded per trader and a 16% increase in the number of users placing option trades"; crypto +$275 million "primarily due to higher cryptocurrency rebate rates from crypto market makers and a 6% increase in the number of users placing cryptocurrency trades, partially offset by 9% decrease in the average Notional Trading Volume traded per trader ... benefited from our acquisition of Bitstamp"; equities +$125 million "a 65% increase in the average Notional Trading Volume traded per trader and a 12% increase in the number of users placing equity trades ... partially offset by lower equity rebate rates"; other +$218 million "primarily driven by increased user activities in Prediction Markets and instant withdrawals". [10-K FY2025, Item 7, L2428–L2434]
- FY2024 drivers: crypto +$491 million (+77% notional per trader, +72% users, "a rebate increase was effective in May 2024"); options +$255 million (+29% users, +43% contracts); equities +$73 million. [10-K FY2024, Item 7, L2222–L2228]
- FY2023 vs FY2022: crypto −$67 million (−29% users, −15% notional per trader, "partially offset by a higher rebate rate"); equities −$13 million ("lower equity rebate rates due to reduced spreads in securities pricing"); options +$17 million; other +$34 million "primarily driven by increasing user activities in Instant Withdrawals". [10-K FY2023, Item 7, L2038–L2046]

### 3c. Net interest revenues by component, FY2021–FY2025 ($ millions)

| | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| Margin interest | 132 | 177 | 243 | 319 | 573 |
| Interest on segregated cash, cash equivalents, securities and deposits | 4 | 57 | 210 | 261 | 319 |
| Interest on corporate cash and investments | 1 | 103 | 288 | 256 | 167 |
| Cash Sweep | 3 | 22 | 123 | 179 | 229 |
| Securities lending, net | 136 | 89 | 79 | 94 | 190 |
| Credit card, net | — | — | 9 | 24 | 64 |
| Interest expenses related to credit facilities | (20) | (24) | (23) | (24) | (32) |
| Other | — | — | — | — | 4 |
| Total net interest revenues | 256 | 424 | 929 | 1,109 | 1,514 |
| Net interest as % of total net revenues | 14% | 31% | 50% | 38% | 34% |

- Sources: FY2021–FY2023 [10-K FY2023, Item 7, L2056–L2066]; FY2023–FY2025 [10-K FY2025, Note 5, L3778–L3788]. Securities lending gross: interest revenue $184 / $321 / $604 million and interest expense $(105) / $(227) / $(414) million for FY2023 / FY2024 / FY2025. [10-K FY2025, Note 5, L3803–L3805]
- FY2025 comment: "Net interest revenues increased by $405 million, primarily driven by growth in our interest-earning asset balances and securities lending activities. The increase was partially offset by a decrease in interest revenue on corporate cash and investments primarily driven by a lower short-term interest rate environment. We anticipate any potential future rate cuts by the Federal Reserve will negatively impact our net interest revenues and adversely affect our customers' returns on cash deposits." [10-K FY2025, Item 7, L2455]
- FY2024 comment: "Between September 2024 and the end of 2024, the Federal Reserve lowered interest rates by a total of 100 basis points, which negatively impacted our net interest revenues". [10-K FY2024, Item 7, L2257]
- FY2023 comment: "primarily driven by growth in interest-earning assets balances and the higher short-term interest rate environment due to the rise in the federal funds rate". [10-K FY2023, Item 7, L2068]

### 3d. Interest-earning assets and yields (period-end balances, $ millions; yields as stated)

| | Margin book | Cash and deposits | Cash Sweep (off-B/S) | Credit card, net | Total interest-earning assets | Yield: margin | Yield: cash | Yield: sweep | Yield: credit card | Yield: total IEA | Total NII yield |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 12/31/2021 | 6,467 | 10,600 | 2,095 | n/a | 19,162 | 2.43% | 0.05% | 0.14% | n/a | 0.79% | 1.45% |
| 12/31/2022 | 3,089 | 9,530 | 5,837 | n/a | 18,456 | 3.92% | 1.61% | 0.75% | n/a | 2.07% | 2.44% |
| 12/31/2023 | 3,458 | 10,107 | 16,352 | 205 | 30,122 | 7.36% | 4.99% | 1.08% | n/a | 3.52% | 3.74% |
| 12/31/2024 | 7,909 | 9,943 | 26,064 | 391 | 44,307 | 6.28% | 5.04% | 0.84% | 9.20% | 2.81% | 3.00% |
| 12/31/2025 | 16,823 | 10,995 | 32,786 | 1,040 | 61,644 | 5.01% | 3.98% | 0.74% | 10.14% | 2.45% | 2.74% |
| 6/30/2025 | 9,457 | 14,045 | 32,719 | 562 | 56,783 | 5.12% (Q2) | 4.16% | 0.80% | 10.14% | 2.41% | 2.78% |
| 3/31/2026 | 16,953 | 16,669 | 26,023 | 1,132 | 60,777 | 4.45% (Q1) | 2.63% | 0.62% | 11.81% | 2.36% | 2.34% |
| 6/30/2026 | 21,641 | 18,687 | 29,707 | 1,457 | 71,492 | 4.52% (Q2) | 2.02% | 0.59% | 11.88% | 2.33% | 2.34% |

- Yields are the company's "annual yield" (revenue ÷ simple average of month-end balances) for the year ending on that date, or annualized quarterly yield for the quarter ending on that date. Sources: [10-K FY2023, Item 7, L2074–L2100]; [10-K FY2025, Item 7, L2460–L2472]; [10-Q Q2 2026, Item 2, L1845–L1880]. Credit card, net at 12/31/2025: $200 million off-balance-sheet (Coastal Bank Program Agreement) and $840 million on-balance-sheet (Credit Card Funding Trust); at 6/30/2026: $214 million and $1,243 million. [10-K FY2025, L2476; 10-Q Q2 2026, L1874]
- Cash Sweep spread: "we earn a net interest spread on Cash Sweep balances based on the interest rate offered by the partner banks less the interest rate given to users ... For the vast majority of the Cash Sweep program, we have the ability to manage our net interest spread by adjusting the rate given to users". [10-K FY2025, Item 7A, L2794]

### 3e. Other revenues, FY2022–FY2025 ($ millions)

| | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| Gold subscription revenues | n/d | 68 | 75 | 109 | 179 |
| Proxy revenues | n/d | 44 | 61 | 60 | 63 |
| Other (listing fees, selling concessions, advertising, ACATS, Trump Accounts from 2026) | n/d | 8 | 15 | 26 | 89 |
| Total other revenues | 157 | 120 | 151 | 195 | 331 |

- Sources: FY2021 total only [10-K FY2023, Item 7, L2125]; FY2022–FY2024 [10-K FY2024, Item 7, L2306–L2309]; FY2025 [10-K FY2025, Item 7, L2498–L2501]. FY2025 other revenues "increased $136 million primarily driven by increased Gold subscription revenues of $70 million ... Additionally, other revenues increased $63 million primarily driven by higher revenues from an increased number of digital assets listed, revenues derived from acquired business during the year, and increased IPO offerings." [10-K FY2025, L2503] FY2024 included "$11 million due to advertising revenue from Sherwood Media, which was launched during the second quarter of 2023." [10-K FY2024, L2311]

### 3f. Quarterly revenue by line ($ millions)

| | Q1 2025 | Q2 2025 | H1 2025 | Q1 2026 | Q2 2026 | H1 2026 |
|---|---|---|---|---|---|---|
| Options | 240 | 265 | 505 | 260 | 342 | 602 |
| Event contracts | 3 | 10 | 13 | 104 | 156 | 260 |
| Cryptocurrencies | 252 | 160 | 412 | 134 | 100 | 234 |
| Equities | 56 | 66 | 122 | 82 | 129 | 211 |
| Other transaction-based | 32 | 38 | 70 | 43 | 49 | 92 |
| **Total transaction-based** | 583 | 539 | 1,122 | 623 | 776 | 1,399 |
| Margin interest | 110 | 114 | 224 | 193 | 215 | 408 |
| Interest on segregated cash, cash equivalents, securities and deposits, net | 56 | 77 | 133 | 58 | 60 | 118 |
| Cash Sweep | 48 | 60 | 108 | 45 | 41 | 86 |
| Credit card, net | 10 | 13 | 23 | 32 | 40 | 72 |
| Interest on corporate cash and investments | 49 | 46 | 95 | 34 | 31 | 65 |
| Securities lending, net | 23 | 54 | 77 | 4 | 10 | 14 |
| Interest expenses related to credit facilities | (6) | (8) | (14) | (8) | (10) | (18) |
| Other interest | — | 1 | 1 | 1 | 2 | 3 |
| **Total net interest revenues** | 290 | 357 | 647 | 359 | 389 | 748 |
| Gold subscription revenues | 38 | 44 | 82 | 50 | 54 | 104 |
| Proxy revenues | 9 | 36 | 45 | 8 | 42 | 50 |
| Other | 7 | 13 | 20 | 27 | 47 | 74 |
| **Total other revenues** | 54 | 93 | 147 | 85 | 143 | 228 |
| **Total net revenues** | 927 | 989 | 1,916 | 1,067 | 1,308 | 2,375 |

- Sources: Q1 columns [10-Q Q1 2026, Note 6, L806–L838]; Q2 and H1 columns [10-Q Q2 2026, Note 6, L905–L935]. Shares of total net revenues Q2 2026: options 26%, event contracts 12%, crypto 8%, equities 10%, other 3%, transaction-based 59%; net interest 30%; other revenues 11%. [10-Q Q2 2026, Item 2, L1776–L1782, L1824–L1832, L1892]
- Q2 2026 drivers: transaction-based +$237 million y/y "primarily driven by increases of $146 million ... in event contracts, $77 million ... in options, and $63 million ... in equities, partially offset by decreases of $60 million ... in cryptocurrencies." Options: "a 43% ... increase in Options Contracts Traded per trader ... partially offset by lower option rebate rates". Event contracts: "an acceleration in our prediction markets business". Crypto: "lower cryptocurrency rebate rates from crypto market makers, a 16% ... decrease in the number of users placing cryptocurrency trades, and a 20% ... decrease in the average Notional Trading Volume traded per trader, partially offset by ... Bitstamp." Equities: "a 56% ... increase in the average Notional Trading Volume traded per trader and a 13% ... increase in the number of users placing equity trades ... higher equity rebate rates due to the mix of ticker symbols". (Six-month figures: +32% options contracts per trader; −24% crypto users; −21% crypto notional per trader; +51% equity notional per trader; +6% equity users.) [10-Q Q2 2026, Item 2, L1784–L1792]
- Q2 2026 net interest +$32 million y/y "primarily driven by higher margin interest and net credit card interest ... as well as higher accretion income on investments. The increase was partially offset by a decrease in interest revenue from securities lending activities driven by a relatively unfavorable average rate on higher stock loan balances, as well as a decrease in interest revenue on Cash Sweep, corporate cash and investments driven by a lower short-term interest rate environment." Securities lending gross Q2 2026: revenue $112 million, expense $(102) million (Q2 2025: $153 million / $(99) million). [10-Q Q2 2026, Item 2, L1834; Note 6, L941–L946]
- New netting in 2026: "Interest on segregated cash, cash equivalents, securities, and deposits, net" = interest revenue $117 million less "interest expense paid to users on uninvested cash and option deposits" $(57) million in Q2 2026 ($199 million less $(81) million for H1 2026); the expense line was zero in 2025. [10-Q Q2 2026, Note 6, L953–L956]
- Q2 2026 other revenues +$50 million y/y "primarily driven by increases in Robinhood Gold subscription revenues due to growth in Robinhood Gold Subscribers, service revenues earned from Trump Accounts, and revenues earned from coin listings." [10-Q Q2 2026, Item 2, L1910]
- Q1 2026 (from the Q1 10-Q statements): total net revenues $1,067 million; net income $346 million; net income attributable to Robinhood $350 million; diluted EPS $0.38 (Q1 2025: $927 million; $336 million; $0.37). [10-Q Q1 2026, Item 1, L392–L428]

### 3g. Definitional and presentation changes to record

- Event contracts became a separate transaction-revenue line in the 2026 10-Qs; in the FY2025 10-K they sit inside "Other" transaction-based revenue ($302 million for FY2025, driven by "Prediction Markets and instant withdrawals"). [10-K FY2025, L2428; 10-Q Q1 2026, L813–L818]
- Interest paid to users on uninvested cash and option deposits is netted within segregated-cash interest from 2026 (3f above).
- Bitstamp is included in crypto Notional Volume, Funded Customers, Net Deposits and Total Platform Assets from June 2025; TradePMR RIA clients in Funded Customers from Q1 2025 and RIA assets in Total Platform Assets but not in Net Deposits. [10-K FY2025, glossary L229–L242]
- "Assets Under Custody" was renamed "Total Platform Assets"; "Net Cumulative Funded Accounts" was renamed "Funded Customers" in Q4 2023; Robinhood Credit users were added to MAU from Q4 2023. [10-K FY2025, glossary L231; 10-K FY2023, L1764]
- Net Deposits definition changed in January 2024 to include dividend and interest inflows and to deduct Gold fees and margin interest. [10-K FY2023, L1770]
- Adjusted EBITDA definition changed in 2026 to start from "net income attributable to Robinhood" and exclude non-controlling interests and "interest expenses related to debt obligations" (previously "credit facilities"). [10-Q Q2 2026, Item 2, L1696]
- SAB 122: "In January 2025, the staff of the SEC issued SAB 122 which rescinded the SAB 121 requirement ... to recognize both a safeguarding liability and asset on the balance sheet ... we early adopted SAB 122 as part of the consolidated financial statements for the year ended December 31, 2024, with retrospective application"; the FY2022/FY2023 balance sheets therefore carried an "Asset related to user cryptocurrencies safeguarding obligation" of $8,431 million / $14,708 million and an equal liability, which the FY2024 and later balance sheets no longer show. [10-K FY2024, Note 1, L3429; 10-K FY2023, Item 8, L2545–L2580]

---

## 4. Income statement

### 4a. Fiscal years FY2021–FY2025 ($ millions except per share)

| | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| Total net revenues | 1,815 | 1,358 | 1,865 | 2,951 | 4,473 |
| Brokerage and transaction | 158 | 179 | 146 | 164 | 211 |
| Technology and development | 1,234 | 878 | 805 | 818 | 897 |
| Operations | 368 (incl. credit losses) | 249 | 116 | 112 | 130 |
| Provision for credit losses | (in Operations; CF statement shows 78) | 36 | 43 | 76 | 114 |
| Marketing | 325 | 103 | 122 | 272 | 399 |
| General and administrative | 1,371 | 924 | 1,169 | 455 | 628 |
| Total operating expenses | 3,456 | 2,369 | 2,401 | 1,897 | 2,379 |
| Operating income (loss) = revenues − opex (computed) | (1,641) | (1,011) | (536) | 1,054 | 2,094 |
| Change in fair value of convertible notes and warrant liability | (2,045) | — | — | — | — |
| Other income (expense), net | 1 | (16) | 3 | 10 | 14 |
| Income (loss) before income taxes | (3,685) | (1,027) | (533) | 1,064 | 2,108 |
| Provision for (benefit from) income taxes | 2 | 1 | 8 | (347) | 225 |
| Net income (loss) | (3,687) | (1,028) | (541) | 1,411 | 1,883 |
| Diluted EPS ($) | (7.49) | (1.17) | (0.61) | 1.56 | 2.05 |
| Basic EPS ($) | (7.49) | (1.17) | (0.61) | 1.60 | 2.12 |
| Weighted-average diluted shares (millions, rounded from the reported share counts) | 492.4 | 878.6 | 890.9 | 906.2 | 918.8 |

- Sources: FY2021–FY2023 [10-K FY2023, Item 8, L2601–L2632] (FY2021 operating expense lines as presented there; FY2022 Operations split per [10-K FY2024, Item 7, L2160–L2176]); FY2023–FY2025 [10-K FY2025, Item 8, L2993–L3025]. Robinhood presents no gross profit and no "operating income" line; the "computed" row is total net revenues less total operating expenses. The closest cost-of-revenue proxy is "Brokerage and transaction" (5% of revenues in FY2024 and FY2025; "A large portion of our brokerage and transaction costs are variable and tied to trading and transaction volumes"), so any "gross margin" is a computed figure. [10-K FY2025, Item 7, L2342, L2513]
- FY2021 SBC included "$1.01 billion of SBC expense" recognised on the IPO; FY2023 G&A includes $485 million from the "2021 Founders Award Cancellation". [10-K FY2023, Item 7, L2013]
- FY2024 tax: benefit of $347 million reflects "a $369 million deferred tax benefit, primarily from the valuation allowance release on the U.S. federal and certain state deferred tax assets"; "having demonstrated sustained profitability which is objective and verifiable ... we concluded it is more likely than not that our U.S. federal, and certain U.S. states net deferred tax assets will be realizable." Valuation allowance roll-forward: $607 million (end 2022) → $574 million (2023) → $88 million (2024) → $105 million (2025); California and certain other state and foreign DTAs remain reserved. [10-K FY2024, Item 7, L2439; Note 9, L3958; 10-K FY2025, Note 8, L4150–L4158]
- FY2025 effective tax rate 10.7% ($225 million on $2,108 million pre-tax): statutory 21.0%, share-based compensation −8.7 points, R&D credits −3.1 points, state +1.6 points. Cash taxes paid $95 million. NOLs at 12/31/2025: $44 million federal, $297 million state, $11 million non-U.S.; federal tax credit carryforwards $191 million. Unrecognized tax benefits $134 million. [10-K FY2025, Note 8, L4076–L4098, L4161–L4171]
- FY2025 G&A rose $173 million, including "$78 million in employee compensation, benefits, and overhead driven by increased average headcount, payroll taxes related to the vesting of Market-Based RSUs, and expenses recognized for shares granted in connection with acquisitions" and "a $55 million reversal of an accrual as part of a regulatory settlement in the prior year" (i.e., FY2024 G&A was reduced by that reversal). [10-K FY2025, Item 7, L2592]
- FY2025 operating-expense detail ($ millions): Brokerage and transaction 211 = employee costs 60 + market data 34 + instant withdrawals 33 + other 84; Technology and development 897 = employee 485 + cloud infrastructure 211 + software and tools 156 + other 45 (20% of revenue vs 28% in FY2024); Operations 130 = employee 83 + customer experience 23 + other 24; Provision for credit losses 114 = credit-card 86 + brokerage 28; Marketing 399 = digital 177 + brand 78 + employee 50 + other 94 (9% of revenue); G&A 628 = employee 401 + legal 76 + other professional fees 64 + other 87 (14% of revenue). [10-K FY2025, Item 7, L2513–L2592]

### 4b. Quarters and half-years ($ millions except per share)

| | Q1 2025 | Q2 2025 | H1 2025 | Q1 2026 | Q2 2026 | H1 2026 |
|---|---|---|---|---|---|---|
| Total net revenues | 927 | 989 | 1,916 | 1,067 | 1,308 | 2,375 |
| Brokerage and transaction | 50 | 48 | 98 | 60 | 62 | 122 |
| Technology and development | 214 | 214 | 428 | 241 | 256 | 497 |
| Operations | 31 | 29 | 60 | 38 | 57 | 95 |
| Provision for credit losses | 24 | 28 | 52 | 36 | 56 | 92 |
| Marketing | 105 | 99 | 204 | 107 | 104 | 211 |
| General and administrative | 133 | 132 | 265 | 174 | 199 | 373 |
| Total operating expenses | 557 | 550 | 1,107 | 656 | 734 | 1,390 |
| Operating income = revenues − opex (computed) | 370 | 439 | 809 | 411 | 574 | 985 |
| Other income, net | 1 | 3 | 4 | — | 135 | 135 |
| Income before income taxes | 371 | 442 | 813 | 411 | 709 | 1,120 |
| Provision for income taxes | 35 | 56 | 91 | 65 | 136 | 201 |
| Net income | 336 | 386 | 722 | 346 | 573 | 919 |
| Net income attributable to non-controlling interests | — | — | — | (4) | 12 | 8 |
| Net income attributable to Robinhood | 336 | 386 | 722 | 350 | 561 | 911 |
| Diluted EPS ($) | 0.37 | 0.42 | 0.79 | 0.38 | 0.62 | 1.00 |
| Weighted-average diluted shares (millions; Q1 columns rounded from reported share counts, Q2 and H1 as reported) | 909.2 | 909 | 911 | 915.0 | 912 | 913 |
| Effective tax rate | n/d | 12.7% | 11.2% | n/d | 19.2% | 17.9% |

- Sources: [10-Q Q1 2026, Item 1, L392–L428]; [10-Q Q2 2026, Item 1, L402–L430; Note 9, L1146–L1156]. Q2 2026 other income of $135 million is "a $106 million gain recognized as a result of the deconsolidation of RVI and a $23 million gain from equity securities primarily related to investments held by RVI". [10-Q Q2 2026, Item 2, L1996]
- Q2 2026 expense drivers: Operations +$28 million y/y "primarily due to a $13 million ... increase in customer experience costs to support Trump Accounts"; G&A +$67 million "primarily due to a $29 million ... increase in employee compensation, benefits, and overhead expenses driven by increased SBC related to the modification of executive awards related to senior leadership transitions and the growth and expansion of our business. Additionally, other general and administrative expenses increased $22 million ... and legal expenses increased $7 million ... in relation to new product offerings and reserves for legal matters"; provision for credit losses +$28 million, "$32 million ... increase in credit card-related provision ... partially offset by a decrease in reserve rates"; brokerage-related provision fell $4 million "due to decreased fraud activity"; marketing brand spend fell to $7 million from $23 million. Tax: Q2 2026 ETR 19.2% "lower than the U.S. federal statutory rate primarily due to the excess tax benefits from SBC and the release of the valuation allowance on certain California deferred tax assets". [10-Q Q2 2026, Item 2, L1946–L2010; Note 9, L1156]

### 4c. Share-based compensation by line ($ millions)

| | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | Q2 2025 | Q2 2026 | H1 2025 | H1 2026 |
|---|---|---|---|---|---|---|---|---|---|
| Brokerage and transaction | 7 | 5 | 7 | 9 | 10 | 3 | 2 | 5 | 5 |
| Technology and development | 610 | 212 | 211 | 192 | 159 | 39 | 48 | 83 | 88 |
| Operations | 20 | 8 | 8 | 7 | 6 | 2 | 1 | 3 | 2 |
| Marketing | 50 | 4 | 5 | 8 | 8 | 2 | 3 | 4 | 5 |
| General and administrative | 885 | 425 | 640 | 88 | 122 | 32 | 51 | 56 | 97 |
| Total SBC | 1,572 | 654 | 871 | 304 | 305 | 78 | 105 | 151 | 197 |

- Sources: [10-K FY2023, Item 7, L1997–L2011]; [10-K FY2025, Note 12, L4423–L4433]; [10-Q Q2 2026, Note 12, L1372–L1382]. FY2023 SBC included $567 million for Market-Based RSUs (of which the $485 million cancellation charge); FY2024 included negative $8 million on Market-Based RSUs after "a reversal of $11 million ... upon the resignation of our co-founder and former Chief Creative Officer during the first quarter of 2024"; FY2025 "primarily consisted of $293 million related to Time-Based RSUs". Capitalised SBC (software): $17 / $26 / $23 million in FY2023 / FY2024 / FY2025; $10 million in H1 2026. Unrecognised SBC $277 million at 12/31/2025 and $520 million at 6/30/2026, each over a weighted-average 1.13 years. [10-K FY2025, Note 12, L4435–L4441; 10-Q Q2 2026, Note 12, L1384]

### 4d. Adjusted EBITDA (company non-GAAP) ($ millions)

| | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | Q2 2025 | Q2 2026 | H1 2025 | H1 2026 |
|---|---|---|---|---|---|---|---|---|---|
| Adjusted EBITDA | 33 | (94) | 536 | 1,429 | 2,522 | 549 | 741 | 1,019 | 1,275 |

- Sources: FY2021–FY2023 from the proxy's pay-versus-performance table [DEF 14A 2026, L2248–L2252]; FY2024–FY2025 reconciliation [10-K FY2025, Item 7, L2282–L2300]: FY2025 net income 1,883 + interest on credit facilities 32 + taxes 225 + D&A 86 = EBITDA 2,226; + SBC 305 − unrealized gains on non-marketable securities (RVI) 9 = 2,522. FY2024: 1,411 + 24 − 347 + 77 = 1,165; + 304 − 40 (a $55 million accrual reversal within "significant legal and tax settlements and reserves") = 1,429. Q2 2026 [10-Q Q2 2026, Item 2, L1704–L1722]: net income 573 + interest 10 + taxes 136 + D&A 23 = 742; + SBC 105 + restructuring charges 23 − RVI deconsolidation gain 106 − equity-securities gains 23 = 741.
- Adjusted EBITDA margin (computed: Adjusted EBITDA ÷ total net revenues): FY2023 29%, FY2024 48%, FY2025 56%, Q2 2025 56%, Q2 2026 57%, H1 2026 54%.

---

## 5. Cash flow, capex, free cash flow

### 5a. Fiscal years ($ millions)

| | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| Net cash from operating activities | (885) | (852) | 1,181 | (157) | 1,638 |
| Purchases of property, software and equipment | (63) | (28) | (2) | (13) | (15) |
| Capitalization of internally developed software | (20) | (29) | (19) | (37) | (39) |
| Capex incl. capitalised software (computed) | (83) | (57) | (21) | (50) | (54) |
| Free cash flow = OCF − capex (computed) | (968) | (909) | 1,160 | (207) | 1,584 |
| Depreciation and amortization | 26 | 61 | 71 | 77 | 86 |
| Net cash from investing activities | (238) | (60) | (582) | (148) | 141 |
| Net cash from financing activities | 5,203 | — | (610) | (345) | (590) |
| Repurchase of Class A common stock | — | — | (608) | (257) | (653) |
| Taxes paid on net share settlement of equity awards | (422) | (12) | (12) | (244) | (437) |
| Cash paid for income taxes, net | 6 | 4 | 9 | 18 | 95 |
| Cash, cash equivalents, segregated and restricted cash, end of period | 10,270 | 9,357 | 9,346 | 8,695 | 9,893 |

- Sources: FY2021–FY2023 [10-K FY2023, Item 8, L2661–L2722]; FY2022–FY2024 [10-K FY2024, Item 8, L2892–L2960]; FY2023–FY2025 [10-K FY2025, Item 8, L3057–L3105].
- Why operating cash flow swings: the 10-K attributes the FY2024-to-FY2025 change of +$1,795 million to "Increase in net income after adjusting for non-cash items $1,073 [million]; Increase in securities borrowed due to increased customer activities 2,462; Increase in securities segregated under federal and other regulations 594; Increase in securities loaned due to continued growth of our securities lending program, as well as market conditions, variable lending and funding activities 247; Decrease in working capital primarily driven by the timing of collection of receivables from users and payment of current liabilities (2,581)". The operating section itself moves with customer balances: FY2025 receivables from users (9,106), payables to users +3,423, securities loaned +4,163, securities borrowed +828. [10-K FY2025, Item 7, L2695–L2704; Item 8, L3070–L3084]
- FY2025 investing included $1,193 million of "Cash, cash equivalents, and segregated cash acquired in business acquisitions" (mostly Bitstamp customer cash) against $(399) million consideration, $(244) million purchases of non-marketable securities "primarily related to Robinhood Ventures Fund I", and gross credit-card receivable purchases of $(5,195) million with collections of $4,440 million. Financing included $4,752 million of draws and equal repayments on credit facilities (intra-year) and $468 million of Credit Card Funding Trust borrowings. [10-K FY2025, Item 8, L3086–L3100; Item 7, L2708–L2722]

### 5b. Half-years ($ millions)

| | H1 2025 | H1 2026 |
|---|---|---|
| Net cash from operating activities | 4,151 | 2,758 |
| Purchases of property, software and equipment | (10) | (21) |
| Capitalization of internally developed software | (19) | (21) |
| Free cash flow = OCF − capex (computed) | 4,122 | 2,716 |
| Net cash from investing activities | 841 | (1,054) |
| Net cash from financing activities | (703) | 2,086 |
| Repurchase of Class A common stock | (446) | (664) |
| Proceeds from convertible senior notes | — | 2,200 |
| Purchase of Capped Calls | — | (123) |
| Proceeds from RVI IPO, net (non-controlling interest) | — | 312 |
| Cash derecognized on RVI deconsolidation | — | (220) |
| Cash paid for income taxes, net | 82 | 171 |
| Cash, cash equivalents, segregated and restricted cash, end of period | 12,992 | 13,674 |

- Sources: [10-Q Q2 2026, Item 1, L467–L520]. H1 2026 operating drivers listed by the company: securities loaned +$3,733 million change, payables to users +$3,248 million ("higher customer free credit balance"), receivables from users (3,176) ("higher customer margin receivables"), securities segregated (3,772). [10-Q Q2 2026, Item 2, L2108–L2118]

---

## 6. Balance sheet

### 6a. Year-ends and 2026 quarters ($ millions)

| | 12/31/2021 | 12/31/2022 | 12/31/2023 | 12/31/2024 | 12/31/2025 | 3/31/2026 | 6/30/2026 |
|---|---|---|---|---|---|---|---|
| Cash and cash equivalents | 6,253 | 6,339 | 4,835 | 4,332 | 4,261 | 5,012 | 5,362 |
| Cash, cash equivalents and securities segregated under federal and other regulations | 3,992 | 2,995 | 4,448 | 4,724 | 5,749 | 10,874 | 12,023 |
| Receivables from users, net (margin loans, credit-card receivables, other) | 6,639 | 3,218 | 3,495 | 8,239 | 17,994 | 18,115 | 22,799 |
| Securities borrowed | — | 517 | 1,602 | 3,236 | 2,408 | 3,355 | 6,036 |
| Deposits with clearing organizations | 328 | 186 | 338 | 489 | 702 | 694 | 1,240 |
| Held-to-maturity investments (current + non-current) | — | — | 486 | 398 | — | — | — |
| Goodwill | 101 | 100 | 175 | 179 | 385 | 401 | 516 |
| Total assets | 19,769 | 23,337 | 32,332 | 26,187 | 38,137 | 45,474 | 56,550 |
| Payables to users | 6,476 | 4,701 | 5,097 | 7,448 | 11,986 | 16,780 | 17,243 |
| Securities loaned | 3,651 | 1,834 | 3,547 | 7,463 | 11,626 | 13,387 | 20,536 |
| Other current liabilities (incl. Trust borrowings) | 134 | 105 | 217 | 266 | 914 | 1,046 | 1,387 |
| Long-term borrowings (convertible notes, net) | — | — | — | — | — | — | 2,170 |
| Total liabilities | 12,476 | 16,381 | 25,636 | 18,215 | 28,986 | 35,786 | 47,009 |
| Total stockholders' equity | 7,293 | 6,956 | 6,696 | 7,972 | 9,151 | 9,688 | 9,541 |
| of which non-controlling interests | — | — | — | — | 11 | 369 | 61 |
| Accumulated deficit | (3,877) | (4,905) | (5,446) | (4,035) | (2,152) | (1,802) | (1,241) |

- Sources: [10-K FY2022, Item 8, L2485–L2535]; [10-K FY2023, Item 8, L2545–L2598]; [10-K FY2025, Item 8, L2939–L2990]; [10-Q Q1 2026, Item 1, L337–L390]; [10-Q Q2 2026, Item 1, L346–L400]. The 12/31/2022 and 12/31/2023 totals include the SAB 121 safeguarding asset/liability ($8,431 million / $14,708 million) later removed (section 3g). User-held fractional shares ($4,764 million at 6/30/2026) are offset by an equal "Fractional shares repurchase obligation".
- Corporate vs customer cash: cash and cash equivalents ($4.3 billion at 12/31/2025; $5.4 billion at 6/30/2026) plus stablecoin ($152 million; $155 million) are the company's stated "Liquid Assets"; segregated cash/securities ($5,749 million; $12,023 million) is customer money held under the customer protection rule; customers' swept cash ($32.8 billion; $29.7 billion) and custodied crypto ($38.2 billion; $26.3 billion at fair value) are off-balance-sheet. [10-K FY2025, Item 7, L2613; Note 11, L4294; 10-Q Q2 2026, Item 2, L2040; Note 11, L1303]
- Off-balance-sheet credit-card receivables funded by Coastal Bank: $200 million (12/31/2025), $214 million (6/30/2026); Coastal may fund up to $500 million after a March 2026 amendment (previously $300 million) at fed funds + 2.65% on the first $300 million and 1.15% above. [10-K FY2025, Note 11, L4286–L4290; 10-Q Q2 2026, Note 11, L1287–L1291]

### 6b. Debt and committed facilities

- Convertible notes: $2.2 billion 0.00% convertible senior notes due October 1, 2029, issued June 25, 2026 (144A), initial conversion rate 5.7332 shares per $1,000 (conversion price ~$174.42, a 65% premium to the $105.71 close on June 22, 2026); cash settlement of principal, excess in cash or shares at company election; redeemable from July 1, 2028 if the stock is ≥120% of conversion price; net carrying amount $2.17 billion; debt issuance costs ~$30.6 million; effective interest rate 0.43%; potentially convertible into 12.6 million shares (maximum 20,811,560). Capped calls bought for $123.2 million: strike $174.4227, cap $237.8475, ~12,613,040 shares. [8-K 2026-06-25, Items 1.01/2.03/3.02; 10-Q Q2 2026, Note 11, L1201–L1230]
- Use of proceeds language: "Opportunistic capital raise with proceeds used to enhance strategic flexibility to invest for future growth"; ~$290 million used to repurchase 2,743,000 shares at $105.71 concurrently. [8-K-2026-06-23-ex991.txt; 8-K 2026-06-25, Item 8.01]
- RHM (parent) unsecured revolver: $1.0 billion commitment maturing March 21, 2028, accordion up to $500 million (total $1.5 billion), SOFR + 1.50%, 0.25% commitment fee (RHM March 2026 Credit Agreement, March 9, 2026; the 2025 version was $1.125 billion after an accordion draw). [10-Q Q2 2026, Note 11, L1236; 10-K FY2025, Note 11, L4238]
- RHS (clearing broker) 364-day senior secured revolver with JPMorgan as agent: $3.25 billion committed from March 20, 2026 (up from $2.65 billion in March 2025 and $2.25 billion in March 2024), accordion to $4.875 billion; three tranches secured by different RHS assets; SOFR/fed funds/OBFR + 1.25% (Tranche A) or 2.50% (B and C); 0.45% commitment fee; covenants on minimum tangible net worth and excess net capital. No borrowings outstanding at 12/31/2025 or 6/30/2026. [8-K 2026-03-24, Item 1.01; 10-Q Q2 2026, Note 11, L1244–L1252]
- Total committed revolving capacity: $3.775 billion at 12/31/2025; "up to $4.875 billion" at 6/30/2026 (the company's phrasing counts accordion). [10-K FY2025, Item 7, L2617; 10-Q Q2 2026, Item 2, L2044]
- Credit Card Funding Trust (consolidated VIE): borrowing arrangements with Barclays ($200 million), SVB ($150 million), Wells Fargo ($300 million) and Truist ($300 million) at 12/31/2025 (weighted average rate 6.16% in 2025); six arrangements (adding Goldman Sachs and Mizuho) with aggregate commitment $1.55 billion at 6/30/2026, margins 1.30%–1.50% over CP/SOFR, weighted-average rate 5.06%. Purchased receivables not yet collected, net: $786 million (12/31/2025), $1.1 billion (6/30/2026); borrowings outstanding $602 million and $959 million. Trust net interest revenue: $45 million FY2025; $34 million Q2 2026. On July 23, 2026 the Trust "completed an inaugural issuance of $500 million of Series 2026-1 asset-backed notes", weighted average coupon ~4.86%, revolving to June 2029, final maturity July 2031. [10-K FY2025, Note 11, L4254–L4280; 10-Q Q2 2026, Note 11, L1262–L1283]
- Contractual commitments at 6/30/2026 ($ millions): convertible notes 2,200 (2029–2030); purchase commitments 1,287 (cloud, data, insurance); Trust principal and interest 959; operating leases 336; match incentives 9; total 4,791. At 12/31/2025 the total was 1,487. Two committed securities-financing agreements: daily minimum commitments of $25 million (30-day term) and $35 million (21-day term). [10-Q Q2 2026, Item 2, L2052–L2068; 10-K FY2025, Item 7, L2621–L2633]
- Warrants: 8.74 million Class A shares at $26.60, expiring February 12, 2031 (issued with the February 2021 convertible notes); 4.13 million warrants were net-exercised in 2025 for 2.82 million shares; none exercised in H1 2026. [10-K FY2025, Note 12, L4338; 10-Q Q2 2026, Note 12, L1315]

---

## 7. Regulatory capital

| ($ millions) | Net capital | Required | Excess |
|---|---|---|---|
| RHS 12/31/2022 | 2,503 | 66 | 2,437 |
| RHS 12/31/2023 | 2,277 | 75 | 2,202 |
| RHS 12/31/2024 | 2,540 | 178 | 2,362 |
| RHS 12/31/2025 | 3,532 | 373 | 3,159 |
| RHS 6/30/2026 | 3,947 | 504 | 3,443 |
| RHF 12/31/2025 / 6/30/2026 | 210 / 196 | 0.25 / 0.25 | 210 / 196 |
| RHD (FCM) 12/31/2024 / 12/31/2025 / 6/30/2026 | 40 / 180 / 435 | 1 / 10 / 9 | 39 / 170 / 426 |
| TradePMR 12/31/2025 / 6/30/2026 | 13 / 13 | 0.25 / 0.25 | 13 / 13 |

- Sources: [10-K FY2022, L2216]; [10-K FY2023, L2295]; [10-K FY2024, L2499]; [10-K FY2025, Item 7, L2677–L2680]; [10-Q Q2 2026, Item 2, L2085–L2088]. "RHS and RHF compute net capital under the alternative method"; RHD is subject to CFTC Regulation 1.17. All subsidiaries "were in compliance". [10-K FY2025, L2665–L2669]
- Deposits with clearing organizations (DTC, NSCC, OCC, CFTC clearing): $702 million at 12/31/2025; $1,240 million at 6/30/2026 (section 6a). The SEC's December 2024 amendment to Rule 15c3-3 requires daily (rather than weekly) customer reserve computations "by June 2026", which "will increase the operational complexity and burden". [10-K FY2025, Item 1A, L995]

---

## 8. Share count, buybacks, dilution

### 8a. Shares outstanding

| Date | Class A | Class B | Source |
|---|---|---|---|
| 12/31/2021 | 735,957,367 | 127,955,246 | [10-K FY2022, Item 8, L2520] |
| 12/31/2022 | 764,888,917 | 127,862,654 | [10-K FY2023, Item 8, L2582] |
| 12/31/2023 | 745,401,862 | 126,760,802 | [10-K FY2023, Item 8, L2582] |
| 12/31/2024 | 764,903,997 | 119,588,986 | [10-K FY2025, Item 8, L2975] |
| 12/31/2025 | 790,331,696 | 110,996,736 | [10-K FY2025, Item 8, L2975] |
| 2/11/2026 (10-K cover) | 790,054,654 | 110,253,736 | [10-K FY2025, cover, L83] |
| 3/31/2026 | 791,097,939 | 110,120,620 | [10-Q Q1 2026, Item 1, L379] |
| 4/8/2026 (proxy record date) | 791,086,666 | 109,745,620 | [DEF 14A 2026, L2452] |
| 6/30/2026 | ~790 million | ~109 million | [10-Q Q2 2026, Item 1, L384–L385] |
| 7/23/2026 (10-Q cover) | 790,630,234 | 108,452,039 | [10-Q Q2 2026, cover, L67] |

- Combined shares in the equity statements (rounded from the reported counts): 892.8 million (12/31/2022), 872.2 million (2023), 884.5 million (2024), 901.3 million (2025), 899 million (6/30/2026). [10-K FY2025, Item 8, L3110–L3208; 10-Q Q2 2026, L590]
- Class B falls as founders convert/sell: 127,955,246 (12/31/2021) → 108,452,039 (July 23, 2026). Holders of record 2/11/2026: 89 (Class A), nine (Class B), zero Class C. [10-K FY2025, Item 5, L2111]
- Weighted-average diluted shares: 906,171,504 (FY2024), 918,781,846 (FY2025), 912 million (Q2 2026), 913 million (H1 2026). Dilutive effect of options, warrants and unvested shares: 30.3 million (FY2025), 13 million (Q2 2026). The 12.6 million shares under the convertible notes (13 million rounded) were anti-dilutive in Q2 2026; capped calls excluded. [10-K FY2025, Note 13, L4457–L4470; 10-Q Q2 2026, Note 13, L1420–L1436]

### 8b. Repurchase programs

- 2023: on August 30, 2023 Robinhood agreed with the United States Marshals Service to repurchase 55,273,469 Class A shares at $10.96 per share (closed August 31, 2023), $608 million including $2 million costs; shares retired. [10-K FY2023, Note, L3840]
- Prior Repurchase Program: announced May 28, 2024, $1 billion; increased by $500 million on April 30, 2025 to $1.5 billion; "we expect to execute over the next roughly two years with flexibility to accelerate if market conditions warrant." Repurchases: $257 million (10,356,110 shares) in FY2024; $653 million (~12 million shares; equity statement 12,018,462) in FY2025; Q4 2025: 831,629 shares at an average $119.86; $590 million remained at 12/31/2025. [10-K FY2025, Item 5, L2129–L2140; Item 7, L2647; Note 12, L4342–L4346; 10-K FY2024, Item 7, L2481]
- Current Repurchase Program: approved by the board and announced March 24, 2026, "up to $1.5 billion", replacing the prior program and "inclusive of amounts that remained available ... which were rolled over ... and represents more than $1.1 billion of incremental capacity. While the Repurchase Program does not have an expiration date, the Company's management currently expects to conduct the Repurchase Program over a period of approximately three years, beginning in the first quarter of 2026." [8-K 2026-03-24, Item 7.01; 10-Q Q2 2026, Note 12, L1321–L1327]
- 2026 activity: Q1 2026 ~3.1 million shares for ~$250 million (computed as H1 less Q2); Q2 2026 1,687,374 shares for $124 million under the program (April 877,383 at $70.01; May 719,081 at $75.90; June 90,910) plus 2,743,000 shares at $105.71 ($290 million) bought with note proceeds outside the program; H1 2026 program total 4.8 million shares / $374 million; $1,373 million remaining under the program at 6/30/2026. [10-Q Q2 2026, Note 12, L1329; Part II Item 2, L3601–L3620]
- Cumulative cash spent on repurchases FY2023–H1 2026 (computed from cash-flow statements): 608 + 257 + 653 + 664 = $2,182 million.

### 8c. Equity plans and dilution

- 2021 Omnibus Incentive Plan with an annual evergreen: 307 million shares available for new grants at 12/31/2025 plus 45 million added January 1, 2026; 347 million available at 6/30/2026 (aggregate authorized 537 million, 179 million issued). ESPP: 44.9 million shares available at 12/31/2025 plus 9.0 million added; 0.8 million shares bought in 2025 at $29.85 weighted average. [10-K FY2025, Note 12, L4354, L4406–L4411; 10-Q Q2 2026, Note 12, L1339]
- Time-based RSUs unvested: 18.2 million (12/31/2024, fair value $15.20) → 7.6 million (12/31/2025, $29.92) → 9 million (6/30/2026, $60.92) after 7 million granted in H1 2026 at $76.32. Fair value of RSUs vested: $490 million (2023), $439 million (2024), $1.1 billion (2025). PSUs: 0.3 million granted in H1 2026 at $82.07 (maximum). Options outstanding 3,033,979 at $6.12 weighted exercise price (12/31/2025); no options granted since at least 2023. [10-K FY2025, Note 12, L4363–L4387; 10-Q Q2 2026, Note 12, L1343–L1352]
- Market-Based RSUs (founders' 2019 and 2021 awards): "In February 2023, we cancelled the 2021 Market-Based RSUs of 35.5 million unvested shares. We recognized $485 million SBC expense related to the cancellation ... No other payments, replacement equity awards or benefits were granted in connection with the cancellation." "As of December 31, 2024, SBC expense related to the Market-Based RSUs was fully recognized and as of December 31, 2025, all Market-Based RSUs were fully vested." Fair value of Market-Based RSUs vested in 2025: $1.1 billion. [10-K FY2025, Note 12, L4389–L4395]
- TradePMR post-close shares: 2,049,711 unvested Class A shares ($100 million) vesting over four years; ~1 million vested by 6/30/2026. [10-K FY2025, Note 12, L4415; 10-Q Q2 2026, L1360–L1367]
- Dividends: "We have never declared or paid cash dividends ... we do not anticipate declaring or paying any cash dividends in the foreseeable future ... the terms of our current credit facilities contain restrictions on our ability to pay cash dividends." [10-K FY2025, Item 5, L2115]

---

## 9. Payment for order flow (PFOF): mechanics, concentration, regulation

### 9a. Market-maker concentration (share of total net revenues from any single market maker or exchange above 10%)

| | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | Q2 2025 | Q2 2026 | H1 2025 | H1 2026 |
|---|---|---|---|---|---|---|---|---|---|
| Citadel Securities, LLC | 22% | 16% | 12% | 12% | 13% | 13% | 16% | 12% | 16% |
| Entities affiliated with Wolverine Holdings, L.P. | 10% | 8% | 6% | n/d | n/d | n/d | n/d | n/d | n/d |
| Entities affiliated with Susquehanna International Group, LLP | 12% | 8% | 2% | n/d | n/d | n/d | n/d | n/d | n/d |
| Tai Mo Shan Limited | 15% | 3% | 1% | n/d | n/d | n/d | n/d | n/d | n/d |
| Wintermute Trading Ltd | n/d | —% | 2% | 10% | 6% | n/d | n/d | n/d | n/d |
| All others individually less than 10% | 18% | 24% | 19% (FY2023 10-K) / 26% (FY2025 10-K) | 34% | 36% | 39% | 31% | 47% | 32% |
| Total transaction-based revenue from market makers and exchanges as % of total net revenues | 77% | 59% | 40% | 56% | 55% | 52% | 47% | 59% | 48% |

- Sources: [10-K FY2023, Note 1, L2870–L2880] (footnotes: Wolverine = Wolverine Execution Services, LLC and Wolverine Securities, LLC); [10-K FY2024, Note 1, L3119–L3128]; [10-K FY2025, Note 1, L3291–L3300]; [10-Q Q2 2026, Note 1, L683–L690]. The FY2023 "all others" row differs between the FY2023 10-K (19%, when Wolverine, Susquehanna and Tai Mo Shan were still listed separately) and the FY2025 10-K (26%, after those names dropped below the disclosure threshold); the totals agree (40%). From FY2025 the caption reads "market makers and exchanges" (crypto exchanges are now counterparties for fee-based routing).
- Named liquidity providers elsewhere in the 10-K: overnight (24 Hour Market) brokerage trades "primarily are routed through one Liquidity Provider - Virtu"; USDC orders "are fulfilled directly from Circle". [10-K FY2025, Item 1A, L945, L1781]

### 9b. Rule 606 routing report (Robinhood Financial LLC, Q4 2025) — furnished, not filed

- Robinhood furnishes its broker-dealers' Rule 606(a) reports quarterly on Form 8-K (Items 2.02 and 7.01): "these 606-Reports present some (but not necessarily all) of the payment for order flow ('PFOF') received from venues to which orders were routed. (As disclosed on the 606-Reports, RHS shares the PFOF it receives with RHF pursuant to a revenue and cost allocation agreement.)" [8-K 2025-10-31 and 8-K 2026-01-30, Item 7.01] The RHF report states "RHS passes 80% of such revenue to RHF. The amounts above accordingly represent 80% of the payments received by RHS". [8-K-2026-01-30-ex991-606-RHF.txt]
- October 2025, S&P 500 stocks (RHF non-directed order flow): Virtu Americas 46.32%, G1 Execution Services 14.62%, Jane Street Capital 13.47%, Citadel Securities 10.30%, Hudson River Trading 9.28%, Two Sigma Securities 6.01%. Net payment received for market orders, cents per hundred shares (rounded to one decimal): Virtu 73.1, G1 83.2, Jane Street 101.3, Citadel 42.8, HRT 66.8, Two Sigma 75.4. October 2025, non-S&P 500 stocks: Virtu 34.57%, Jane Street 25.87%, Citadel 18.52%, HRT 9.14%, Two Sigma 6.22%, G1 5.67%; market-order payments 9.5–15.9 cents per hundred shares. October 2025, options: Citadel 39.84%, Dash/IMC Financial Markets 26.74%, Jane Street 18.12%, Global Execution Brokers, LP 8.46%, with Wolverine also listed; net payments for marketable limit orders 37.4–45.8 cents per contract-hundred as printed. Non-directed orders were 100% of all orders; in October 2025 42.65% of S&P 500 stock orders were market orders. [8-K-2026-01-30-ex991-606-RHF.txt, "October 2025" sections]
- The report also says RHS may execute fractional-share portions "in a principal capacity"; "RHF does not receive payments or pay transaction fees for any portion of such an order executed in a principal capacity." [8-K-2026-01-30-ex991-606-RHF.txt]

### 9c. PFOF risk factors (key sentences verbatim)

- Summary line: "Factors that affect transaction-based revenue - such as reduced spreads in securities pricing, reduced levels of trading activity generally, changes in our business relationships with or disruption in the services provided by Liquidity Providers ... and any new regulation of, or any bans on, PFOF and similar practices - might result in reduced profitability, increased compliance costs, and negative publicity." [10-K FY2025, Item 1A, L809, L935]
- "A large portion of our revenue is transaction-based, in that we receive consideration in exchange for routing our users' equity, option, and cryptocurrency trade orders to market makers, wholesalers and other liquidity providers (together, the 'Liquidity Providers') for execution. ... Our transaction-based revenue is sensitive to and dependent on trading volumes and therefore tends to decline during periods in which we experience decreased levels of trading generally. Computer-generated buy/sell programs and other technological advances and regulatory changes in the marketplace might continue to tighten spreads on transactions, which could also lead to a decrease in our PFOF earned from Liquidity Providers." [10-K FY2025, Item 1A, L941]
- SEC market-structure rules: "the SEC adopted final rules in 2024 (the 'September 2024 Final Rules') to, among other things, adopt an additional minimum pricing increment, or 'tick size,' ... reduce the access fee caps ... and enhance the transparency of better priced orders. On September 30, 2025 and October 31, 2025, the SEC granted temporary exemptive relief from certain compliance dates ... which extended the effective dates to February, August, and November of 2026 respectively. The quote transparency rules will make the information about smaller-sized orders publicly available and result in the contraction of spreads across several securities, which we expect could lead to a decrease in the PFOF earned from such orders once the securities information processors ('SIPs') begin dissemination of information incorporating the new round lot and odd-lot definitions (starting on May 1, 2026), followed by an August 1, 2026 compliance date for the Rule 605 execution quality report amendments." [10-K FY2025, Item 1A, L941]
- No contracts: "Our PFOF and Transaction Rebate arrangements with Liquidity Providers are a matter of practice and business understanding and are often not documented under binding contracts (as is generally the case with Liquidity Providers in equities and options). If any Liquidity Providers were unwilling to continue to receive orders from us or to pay us for those orders ... we might have little to no recourse ... With respect to cryptocurrencies, for instance, fewer Liquidity Providers are currently able to execute cryptocurrency trades. For instance, in May 2023, two prominent Liquidity Providers announced their respective decisions to limit their offerings in cryptocurrency trading within the U.S." [10-K FY2025, Item 1A, L945]
- Regulation of PFOF: "In recent years, PFOF practices have drawn heightened scrutiny from the U.S. Congress, the SEC, state regulators, and other regulatory and legislative authorities. For example, in December 2020, we settled an SEC investigation into our best execution and PFOF practices and are defending a consolidated putative class action in federal district court relating to the same factual allegations. Additionally, since July 2023, we have been cooperating with an investigation being conducted by the New York Attorney General concerning brokerage execution quality. ... in March 2024, the SEC adopted amendments to enhance order execution disclosures under Rule 605 of Regulation NMS (the 'Order Execution Disclosure Rules'), which will apply for the first time to RHF and RHS beginning in August 2026." "Depending on how our order execution quality compares to other brokers, we could be subject to negative press or critical academic studies". "Because some of our competitors either do not engage in PFOF or derive a lower percentage of their revenues from PFOF than we do, any legal or regulatory change that impacts PFOF could have an outsized impact on our results of operations." [10-K FY2025, Item 1A, L955–L961]
- Negative publicity and the crypto fee model: "if our customers perceive our PFOF practices to create a conflict of interest between us and them ... they might come to have an adverse view of our business model". "RHC has started to allow customers to choose a fee-based model in lieu of a liquidity provider rebate-based model (under which RHC receives Transaction Rebates from Liquidity Providers) for cryptocurrency orders routed to cryptocurrency exchanges for execution. This shift may lead to negative publicity due to potential differences in total costs for customers under the two models." [10-K FY2025, Item 1A, L965–L975]
- Best execution: "As registered broker-dealers, we are subject to 'best execution' requirements under SEC guidelines and FINRA rules ... We have in the past and continue to be subject to investigations related to our best execution practices. ... the SEC previously proposed rules relating to best execution requirements in December 2022 but formally withdrew them in June 2025." The Q2 2026 10-Q reframes the heading as best execution "under common law agency principles, fiduciary obligations, and FINRA rules". [10-K FY2025, Item 1A, L989–L991; 10-Q Q2 2026, Item 1A, L2253]
- Cautionary-statement list in 8-Ks: "our reliance on transaction-based revenue, including payment for order flow ('PFOF'), the risk of new regulation or bans on PFOF and similar practices, and the addition of our new fee-based model for cryptocurrency". [8-K 2026-03-24, cautionary note]
- UK/EU PFOF bans: no sentence in the fetched 10-K or 10-Q text explicitly discusses PFOF bans in the U.K. or EU; the EU offering is described as commission-based ("We charge users a commission each time a user decides to buy or sell certain cryptocurrencies in the EU") and MiFID "best execution standards" apply to RHEU and Bitstamp. [10-K FY2025, Item 1, L449; L743] Treat as "not disclosed" beyond that.
- FINRA closed its best-execution investigation into RHS and RHF in December 2025; the New York Attorney General's execution-quality/collaring investigation remains open. [10-K FY2025, Note 15, L4574–L4576; 10-Q Q2 2026, Note 15, L1483]

---

## 10. Interest-rate sensitivity (Item 7A / Item 3)

- Method: "a net interest sensitivity analysis, which applies hypothetical 50, 100 or 150 basis point increases or decreases in interest rates to the period end balances of our interest-earning assets and liabilities, including interest rate sensitive off-balance sheet amounts related to our Coastal Bank Program Agreement ... over the next 12 months." Cash Sweep is excluded: "we do not consider the Cash Sweep balance to be subject to short-term interest rate risk and the sensitivity analysis excludes Cash Sweep balances." [10-K FY2025, Item 7A, L2792–L2794]

| Impact on total net revenues, net income and cash flows, pre-tax ($ millions, 12 months) | 12/31/2024 | 12/31/2025 | 6/30/2025 | 6/30/2026 |
|---|---|---|---|---|
| 50 basis points | 94 | 152 | 123 | 175 |
| 100 basis points | 188 | 304 | 247 | 350 |
| 150 basis points | 282 | 457 | 370 | 525 |

- "The impact related to the change in interest rates is positively correlated, linear, and proportional. The change in the sensitivity analysis from prior year is in line with the change in interest-earning asset balances." [10-K FY2025, Item 7A, L2796–L2804; 10-Q Q2 2026, Item 3, L2177–L2190]
- Balances behind it: margin book $21.6 billion, cash and deposits $18.7 billion, off-balance-sheet Cash Sweep $29.7 billion, net credit-card receivables $1.5 billion at 6/30/2026 (section 3d).
- Risk-factor wording: "Reductions in interest rates have negatively impacted, and a return to a low interest rate environment would negatively impact our total net revenues, net income (loss), and cash flows ... Changes to the level or mix of interest earning balances could also negatively impact our total net revenues ... if customers react to the rising interest rate environment by moving cash that would have otherwise been spent on services or products with higher revenue potential for Robinhood into Robinhood accounts that offer customers high interest rates." [10-K FY2025, Item 1A, L979]
- Investment portfolio: "highly-rated debt securities that were considered held-to-maturity investments with average duration in the portfolio less than a year and the maximum maturity of two years"; no borrowings under the revolvers, so "limited financial exposure" there. "Interest rate instruments will be used for hedging purposes only and not for speculation." [10-K FY2025, Item 7A, L2806–L2814]
- Market-related credit risk: margin and securities lending collateral monitored daily; participation in "a risk-sharing program offered through the OCC". [10-K FY2025, Item 7A, L2820]

---

## 11. Cryptocurrency

### 11a. Revenue and asset trend

- Crypto transaction revenue: $420 million (FY2021), $202 million (FY2022), $135 million (FY2023), $626 million (FY2024), $901 million (FY2025); Q1 2026 $134 million and Q2 2026 $100 million versus $252 million and $160 million a year earlier (−43% for H1). Crypto's share of total net revenues: 23% (FY2021), 7% (FY2023), 21% (FY2024), 20% (FY2025), 8% (Q2 2026). [sections 3b, 3f]
- Customer crypto held in custody (off-balance-sheet, fair value): $35.2 billion (12/31/2024), $38.2 billion (12/31/2025), $26.3 billion (6/30/2026); "these assets were not recorded on our consolidated balance sheets ... we did not record a liability". [10-K FY2025, Note 11, L4294; 10-Q Q2 2026, Note 11, L1303] Crypto within Total Platform Assets: $22.1 billion (2021), $8.4 billion (2022), $14.7 billion (2023), $35.2 billion (2024), $38.2 billion (2025), $26.3 billion (Q2 2026). [section 2]
- Bitstamp's scale in the ICFR exclusion: "Bitstamp constituted four percent of total assets as of December 31, 2025 and one percent of consolidated total net revenues for the year then ended"; TradePMR less than one percent of each. [10-K FY2025, Item 8, EY ICFR report, L2905]
- Company-owned stablecoin: $361 million (12/31/2024), $152 million (12/31/2025), $155 million (6/30/2026), counted in "Liquid Assets"; RHC supports USDC (fulfilled by Circle) and USDG (Paxos) for Robinhood Earn. [10-K FY2024, L2453; 10-K FY2025, L2613, L1781; 10-Q Q2 2026, L2040, L2659]

### 11b. Crypto-specific risk factors (one line each; verbatim where quoted)

- Price volatility: "The prices of most cryptocurrencies are extremely volatile. Fluctuations in the price of various cryptocurrencies might cause uncertainty in the market and could negatively impact trading volumes of cryptocurrencies". "Volatility in the values of cryptocurrencies ... might impact our regulatory net worth requirements as well as the demand for our services". [10-K FY2025, Item 1A, L1607, L1649]
- Security status: "any particular cryptocurrency's status as a 'security' and cryptocurrency transaction's status as an 'investment contract' is subject to a high degree of uncertainty"; SEC history: investigative subpoenas since December 2022 on RHC's listings, custody and operations; Q4 2023 Staff view that certain supported cryptocurrencies may be securities; Q2 2024 Wells Notice recommending an action under Exchange Act Sections 15(a) and 17A; "On February 21, 2025, the SEC Division of Enforcement closed the investigation ... and did not intend to move forward with recommending an enforcement action." [10-Q Q2 2026, Item 1A, L2297; 10-K FY2025, Item 1A, L1675]
- Staking and onchain lending: launched in the U.S. in June 2025; risk that the SEC, a state regulator or a private litigant alleges "unregistered offers and sales of securities or unregistered securities broker-dealer activity", which could force Robinhood to "cease our staking or onchain lending activities". [10-Q Q2 2026, Item 1A, L2299, L3207]
- Counterparty risk in crypto: "cryptocurrency trades do not settle through any central clearinghouses but rather are conducted under bilateral agreements between us and each crypto Liquidity Provider (the risk of the Liquidity Provider's default therefore falls upon us rather than being distributed among a clearinghouse's members)". [10-K FY2025, Item 1A, L1521]
- Stock tokens: "In June 2025, we launched Robinhood Stock Tokens for eligible customers in certain EEA jurisdictions ... without conveying legal ownership or shareholder rights"; a "Private Company Stock Token Promotion" referenced privately-held U.S. companies; "there remains considerable regulatory uncertainty regarding how transactions ... involving tokenized real-world assets ... are or should be regulated"; SEC Commissioner Peirce's July 2025 statement that "tokenized securities are still securities" is cited. The Q2 2026 10-Q refers to "Classic Stock Tokens (formerly 'Robinhood Stock Tokens')" and perpetual futures in the EEA. [10-K FY2025, Item 1A, L1787–L1793; 10-Q Q2 2026, cautionary note, L328]
- Robinhood Chain (launched July 2026): "permissionless and developer-friendly ... much of the activity that occurs on Robinhood Chain is conducted by independent third parties ... and may be difficult or impossible for us to monitor, influence, prevent, or reverse. Nevertheless, we may bear reputational, legal, financial, and regulatory consequences"; "Our ability to generate revenue from Robinhood Chain depends significantly on the level of adoption and developer activity on the network"; software vulnerability and impairment risks. [10-Q Q2 2026, Item 1A, L3317–L3323]
- Legislation: GENIUS Act signed July 18, 2025 (payment stablecoins; effective January 18, 2027); CLARITY Act pending; California DFAL licensing effective July 1, 2026 ("prohibit any person or entity engaging in digital financial asset business activity ... unless ... holds a license ... has submitted an application ... or is exempt"). [10-Q Q2 2026, Item 1A, L2659; 10-K FY2025, Item 1A, L1705]
- Forks, network upgrades and custody-feature liabilities: "A temporary or permanent blockchain 'fork' could adversely affect our business"; Crypto Transfers, staking, Robinhood Wallet, Connect and Earn "could result in loss of customer assets, customer disputes, and other liabilities". [10-K FY2025, Item 1A, L1753, L1783; 10-Q Q2 2026, L3253]
- Regulatory settlements specific to crypto: NYDFS August 2022 ($30 million, AML and cybersecurity; independent consultant); California Attorney General August 2024 ($3.9 million, disclosures and delivery of customers' crypto assets); the Florida Attorney General closed its crypto fee-disclosure investigation in December 2025. [10-K FY2025, Item 1A, L1283, L1231; Note 15, L4572]

---

## 12. Prediction markets (event contracts), futures and the Rothera joint venture

- Revenue: event contracts $3 million (Q1 2025), $10 million (Q2 2025), $104 million (Q1 2026), $156 million (Q2 2026), $260 million (H1 2026, 11% of total net revenues). FY2025 event contracts are inside "Other" transaction revenue ($302 million). Proxy: "customers traded over 12 billion event contracts in 2025". [sections 3b, 3f; DEF 14A 2026, L1623]
- Offered through RHD, "our FCM license regulated by the CFTC"; "we charge a commission for each contract traded"; contracts trade on third-party exchanges (KalshiEx, ForecastEx and Kalshi Klear rulebooks are cited for RHD deposit requirements). Rothera (JV with SIG) bought 90% of MIAXdx in January 2026 "to advance the build out of an independent, CFTC-licensed exchange and clearinghouse". [10-K FY2025, Item 1, L431; Item 1A, L999; Note 3, L3702]
- Risk summary: "Our ability to offer event contracts is subject to the outcome of currently ongoing and potential future regulatory enforcement actions and litigation, as well as potential changes in federal or state law, that could immediately or subsequently prevent us from offering, or continuing to offer, event contracts." Specifics in the Q2 2026 10-Q: state cease-and-desist letters to DCMs and FCMs "including RHD"; state civil enforcement actions; Arizona criminal charges against KalshiEx (March 2026) with a CFTC preliminary injunction on appeal; CFTC preemption suits against states from April 2026 (RHD intervening); tribal RICO suits; "Statute of Anne" recovery suits; consumer class actions; the CFTC withdrew a proposed event-contract rule on February 4, 2026 and proposed new amendments; Illinois enacted a tax effective July 1, 2026 of 1.75% of the value of the first five million contracts traded annually by Illinois individuals and 3.5% above. [10-Q Q2 2026, Item 1A, L2761–L2795]
- Nevada: "Robinhood has agreed to cease offering new sports-related event contracts in Nevada as of December 1, 2025" pending its Ninth Circuit appeal (argued April 16, 2026). Wisconsin (April 23, 2026) and Kentucky (June 17, 2026) sued Robinhood entities with Kalshi and Coinbase; RHS and RHM were dismissed from the Wisconsin action on June 1 and July 8, 2026. [10-Q Q2 2026, Note 15, L1553–L1569]
- Rothera governance risk: "Robinhood is entitled to designate a majority of the members of the board of directors of Rothera and one representative to serve on the board of directors of Rothera E&C ... we will not have decision-making authority over all operational, strategic, or commercial decisions". [10-K FY2025, Item 1A, L1113]

---

## 13. Legal proceedings and regulatory matters (with amounts)

- Aggregate accruals for contingencies: $128 million (12/31/2024), $71 million (12/31/2025), $89 million (6/30/2026). "In our opinion, an adequate accrual had been made". [10-K FY2025, Note 15, L4550; 10-Q Q2 2026, Note 15, L1461]
- Settled regulatory matters with amounts (all from the FY2025 10-K Item 1A unless noted): December 2020 SEC settlement of the best-execution/PFOF investigation (amount not stated in the fetched text) [L957]; August 2022 NYDFS crypto AML/cybersecurity settlement, $30 million penalty plus independent consultant [L1283]; January 2024 Massachusetts Securities Division settlement, $7.5 million fine (product features, March 2020 outages, options approvals, November 2021 data incident) [L1229]; August 2024 California Attorney General crypto settlement, $3.9 million [L1231]; December 2024 fines and consent orders with the Nebraska Department of Banking and Finance and the Massachusetts Division of Banks for prior unlicensed activity (amounts not stated) [L1247]; January 2025 SEC settlement of multiple matters (Regulation SHO, SAR timeliness, EBS, recordkeeping, the November 2021 data incident, Regulation S-ID), penalties totaling $45 million, of which $13 million related to SAR filings, $8 million to off-channel communications, and $33.5 million paid by RHS [L1233, L1283, L1497–L1505]; March 2025 FINRA settlement of multiple matters, penalty $26 million plus ~$3.76 million restitution and undertakings [L1235]; FY2024 G&A benefited from "a $55 million reversal of an accrual as part of a regulatory settlement" [L2592]. SEC Enforcement closed its Early 2021 Trading Restrictions investigation on January 10, 2025 [L1227].
- Open regulatory matters (6/30/2026): New York Attorney General investigation into "brokerage execution quality and collaring the prices of certain trade orders"; Massachusetts Securities Division examination of complaint supervision, the August 4–5, 2024 BOATS overnight-trading disruption and election/sports event contracts; FINRA investigation into the BOATS disruption; FDIC investigation of EFTA compliance. Closed in December 2025: FINRA's best-execution investigation and the Florida Attorney General's crypto-fee investigation. [10-Q Q2 2026, Note 15, L1483–L1487; 10-K FY2025, Note 15, L4572–L4576]
- Civil litigation status at 6/30/2026 [10-Q Q2 2026, Note 15, L1477–L1580]:
  - Best Execution/PFOF securities class action (N.D. Cal., filed from December 2020): settlement in principle June 2025; "The settlement was approved by the court in June 2026" (amount not stated).
  - Early 2021 Trading Restrictions: federal antitrust and state-law tranches dismissed with prejudice and affirmed; securities tranche lead plaintiffs dismissed August 2024; remaining individual claims in arbitration; "We have not otherwise received requests related to the Early 2021 Trading Restrictions in over two years."
  - IPO litigation (Golubowski, Sections 11/12(a)): Ninth Circuit reversed in part August 29, 2025; Robinhood's petition for certiorari filed February 2026 "remains pending". Zito derivative suit stayed. A 2022 shareholder demand is partly rejected, remainder under a Demand Review Committee.
  - Pay transparency class action (Washington Equal Pay and Opportunity Act): in discovery.
  - Cash Sweep class actions (Dey/Deeney, N.D. Cal.: alleged failure "to pay a reasonable rate of interest to non-Robinhood Gold brokerage account holders"): "Robinhood has reached a settlement in principle" (amount not stated).
  - Event-contract suits: six Statute of Anne suits by "Gambling Recovery LLC" plaintiffs (RHD voluntarily dismissed in Georgia, Massachusetts, Ohio, South Carolina; Kentucky stayed six months); tribal RICO suits (Blue Lake plaintiffs, on appeal; Ho-Chunk RICO claim dismissed May 2026); RHD's own preemption suits in Nevada, New Jersey (Third Circuit ruled for Kalshi April 2026), Massachusetts (dismissed as unripe, on appeal to the First Circuit), Michigan (PI denied June 2026, on appeal), Washington (non-enforcement agreed); consumer class actions filed April–June 2026 (consolidated in N.D. Cal.; motion to compel arbitration); State of Wisconsin (April 23, 2026) and Commonwealth of Kentucky (June 17, 2026) enforcement suits.
  - Google tracking privacy class action (filed May 8, 2026, N.D. Cal.): alleges account data transmitted to Google without consent.
  - StubHub IPO litigation (filed June 29, 2026, S.D.N.Y.): RHF named as a "Selling Group Defendant" under Section 12(a)(2) only.
- Item 3 of the 10-K and Part II Item 1 of the 10-Q simply cross-refer to Note 15. [10-K FY2025, L2087; 10-Q Q2 2026, L2227]

---

## 14. Specific (non-boilerplate) risk factors — one line each

1. Transaction-revenue dependence on PFOF and Liquidity Providers, including undocumented arrangements and single-provider reliance (Virtu) for overnight trading; SEC tick-size/round-lot and Rule 605 changes in 2026 may compress PFOF. [10-K FY2025, Item 1A, L941–L961]
2. Rate sensitivity: net interest revenue falls with Fed cuts; $304 million per 100 bp at 12/31/2025, $350 million at 6/30/2026. [10-K FY2025, L2800; 10-Q Q2 2026, L2181]
3. Event contracts may be curtailed state by state (Nevada already), with tax (Illinois) and litigation exposure. [10-Q Q2 2026, L2761–L2795]
4. Crypto: extreme price volatility, security-status uncertainty for listed tokens, staking/onchain lending exposure, bilateral counterparty risk with crypto Liquidity Providers, and evolving licensing (DFAL, MiCA, GENIUS). [10-K FY2025, L1521, L1607, L1675; 10-Q Q2 2026, L2297–L2299]
5. Net capital, clearinghouse deposits and liquidity: Early 2021 precedent; daily 15c3-3 computations from June 2026; MiCA capital rules for RHEU and Bitstamp Europe. [10-K FY2025, L993–L999]
6. Regulatory history and pipeline: settlements with SEC ($45 million), FINRA ($26 million + restitution), NYDFS ($30 million), MSD ($7.5 million), CAGO ($3.9 million); open NYAG, MSD, FINRA and FDIC matters; "we expect to continue to be subject to such proceedings in the future". [10-K FY2025, L1225–L1249]
7. Rothera/MIAXdx: consolidated but not wholly owned or operationally controlled exchange and clearinghouse. [10-K FY2025, L1109–L1121]
8. Overnight trading depends on BOATS (Blue Oceans ATS), which failed to open on August 5, 2024, and on Virtu. [10-K FY2025, L1507]
9. Credit card and banking: Coastal Bank dependency (issuer and BaaS partner), CFPB jurisdiction, off-balance-sheet credit exposure, provision for credit losses rising with balances ($86 million card-related in FY2025; $51 million in Q2 2026 alone). [10-K FY2025, L695, L721; L2559]
10. New-product risks named in the cautionary note: Robinhood Chain, Stock Tokens, Classic Stock Tokens and perpetual futures in the EEA, Robinhood Wallet updates, staking and onchain lending in the U.S. [10-Q Q2 2026, cautionary note, L328]
11. Concentrated voting power: "The multi-class structure of our common stock has the effect of concentrating voting power with our founders ... In addition, the Founders' Voting Agreement ... and any future issuances of our Class C common stock could prolong the duration of our founders' voting control." [10-K FY2025, L865]
12. Internal metrics not independently validated ("Funded Customers, AUC, and MAU ... have not been validated by any independent third party"). [10-K FY2023, Item 1A, L1548]
- The FY2025 10-K's own "Summary of Risk Factors" (L799–L866) and the Q2 2026 10-Q's (L2239–L2300) list 27–28 bullets; the first is "We might not grow in line with historical rates."

---

## 15. Management, board, ownership and compensation (DEF 14A 2026 unless noted)

### 15a. Executive officers (ages as of April 22, 2026)

| Name | Age | Position | Since |
|---|---|---|---|
| Vladimir Tenev | 39 | Chair of the Board and Chief Executive Officer (CEO and President since November 2020; Chair since March 2021; co-CEO 2013–2020); also "executive chairman and co-founder of Harmonic, an AI company" | 2013 |
| Shiv Verma | 41 | Chief Financial Officer (principal financial officer); previously SVP Finance and Strategy and Treasurer since 2018; earlier Oportun, PIMCO, Franklin Templeton, Symphony, JPMorgan, Oakland A's | February 6, 2026 |
| Steven Quirk | 61 | Chief Brokerage Officer (ex-TD Ameritrade, Thinkorswim) | January 2022 |
| Daniel Gallagher | 53 | Chief Legal, Compliance, and Corporate Affairs Officer (Chief Legal Officer since May 2020; former SEC Commissioner 2011–2015) | January 2022 |
| Jeffrey Pinner | 41 | Chief Technology Officer (ex-Cruise, Lyft CTO) — separated May 7, 2026 (see 16) | August 2024 |
| Dara Bazzano | 58 | Chief Accounting Officer since April 2026; principal accounting officer from June 25, 2026 (ex-T-Mobile, CBRE, Gap CAO) | 2026 |

- Sources: [DEF 14A 2026, "Executive Officers", L1569–L1590; Tenev biography L705]; [8-K 2026-05-08, Item 5.02]; [8-K 2026-06-26, Item 5.02]. Jason Warnick (former CFO) "ceased to serve as Chief Financial Officer effective February 6, 2026, and transitioned to an advisory role" through September 1, 2026 with continued vesting. [DEF 14A 2026, L1612, L1969]

### 15b. Board (ten directors, all elected annually; classified board sunset at the 2024 meeting)

| Director | Age | Since | Independent | Role / committees |
|---|---|---|---|---|
| Vladimir Tenev | 39 | 2013 | No | Chair |
| Baiju Bhatt | 41 | 2013 | No (former Chief Creative Officer to March 2024; founder/CEO of Aetherflux) | — |
| John Hegeman | 41 | March 2025 | Yes | Audit member; Co-CEO Ithaca Holdings, ex-Meta Chief Revenue Officer |
| Paula Loop | 64 | 2021 | Yes | Audit Committee chair; retired PwC partner |
| Meyer Malka | 51 | 2022 | Yes (Ribbit Capital relationship reviewed) | People and Compensation; Ribbit Capital founder |
| Christopher Payne | 57 | 2024 | Yes | NomGov chair; ex-DoorDash President/COO |
| Jonathan Rubinstein | 69 | 2021 | Yes | Lead Independent Director; Safety, Risk and Regulatory chair; Amazon director |
| Susan Segal | 73 | 2024 | Yes | People and Compensation chair; CEO Americas Society/Council of the Americas |
| Dara Treseder | 37 | 2021 | Yes | Autodesk CMO |
| Robert Zoellick | 72 | 2021 | Yes | Chair, Americas, Temasek |

- Sources: [DEF 14A 2026, "Director Nominees", L269–L285; independence L667; biographies L700–L1090]. Committees: Audit, Nominating and Corporate Governance ("NomGov"), People and Compensation, and Safety, Risk and Regulatory. Director pay 2025 (total, mostly RSUs): from $314,802 (Bhatt) to $595,261 (Hegeman, including his initial grant); Rubinstein $381,784, Loop $358,466, Zoellick $350,727, Segal $345,864, Payne $332,155, Treseder $328,466, Malka $324,457. [DEF 14A 2026, L1454–L1466]

### 15c. Dual-class structure and founders' voting power

- "Our Charter provides for two classes of voting common stock: Class A with one vote per share and Class B with ten votes per share. Class A is publicly traded on Nasdaq; Class B is privately held by our Co-Founders and their related entities ... all Class B shares will automatically convert into Class A shares on August 2, 2036, which is the fifteenth anniversary of our IPO closing date." A third class, Class C (non-voting, 7 billion authorized, none issued), exists. [DEF 14A 2026, "Stockholder Structure", L1151; 10-K FY2025, Note 12, L4306]
- Other sunset triggers: 80% of Class B holders vote to convert; Class B falls below 5% of Class A plus B outstanding; each founder ceases to be an officer/employee/consultant and is not a director (61–180 days later); nine months after the death or total disability of both founders (extendable up to 18 months by independent directors). Transfers convert Class B to Class A except permitted transfers. [10-K FY2025, Note 12, L4310–L4314]
- Voting power at the April 8, 2026 record date (791,086,666 Class A; 109,745,620 Class B): Vladimir Tenev 49,234,651 Class B (44.9% of Class B) and 6,907 Class A = 26.1% of voting power; Baiju Bhatt 61,076,048 Class B (55.7%) and 3,579 Class A = 32.0% of voting power; all current executive officers and directors as a group 11,689,215 Class A (1.5%) and 109,745,620 Class B (100.0%) = 58.6% of voting power. "As of April 8, 2026, parties to this agreement [the Founders' Voting Agreement] control approximately 58% of the total outstanding voting power of our common stock. Therefore, the Co-Founders will be able to determine the outcome of the election of directors and, if the Co-Founders vote together on other matters, to determine the outcome of all other matters". [DEF 14A 2026, ownership table L2421–L2442; L1157]
- Some Class B counted for both founders: 565,079 Class B shares held by the Bhatt Family LLC are voted by Tenev under an irrevocable proxy; Bhatt has sole voting power over 6,230,731 Class B shares held by The Tenev 2017 Irrevocable Trust and over Butterfly Management LLC (1,408,450) and Surfboard Management LLC (1,574,375). Bhatt's own holdings include 47,131,060 Class B in his living trust and three GRATs (938,167; 1,228,186; 2,000,000). Tenev holds 48,669,572 Class B directly. [DEF 14A 2026, footnotes 4 and 10, L2456, L2468]
- Founders' Voting Agreement: the founders and their affiliates vote "in favor of the election of each Co-Founder to, and against the removal of each Co-Founder from, our Board" and "together in the election of other directors generally"; each founder grants the other a voting proxy on death or disability; right of first offer on Class B transfers beyond the first 20 million shares per founder ("Through April 8, 2026, Mr. Bhatt and his related Founder Affiliates had so converted or transferred approximately 13.2 million shares, and Mr. Tenev and his related Founder Affiliates had so converted or transferred approximately 13.4 million shares"); remains in effect until all Class B has converted. [DEF 14A 2026, "Voting Agreements", L2531–L2545]
- Class B Exchange Agreements: each founder may exchange Class A received from pre-IPO RSUs into Class B; "To date, Mr. Tenev has utilized his Equity Exchange Rights to exchange 5,434,198 shares of Class A common stock ... for shares of Class B common stock; Mr. Bhatt has not utilized any Equity Exchange Rights, and there are no outstanding shares held by the Co-Founders subject to the Equity Exchange Right." [DEF 14A 2026, L1161]
- Other holders: BlackRock, Inc. 55,763,578 Class A (7.0% of Class A; 3% of voting power; as of September 30, 2025); "certain subsidiaries or business divisions of subsidiaries of The Vanguard Group collectively own approximately 94,436,459 Class A shares (11.9%)" (reported on a disaggregated basis after a March 2026 realignment); Meyer Malka 10,153,086 Class A (1.3%; includes 2,828,430 warrant shares held by Ribbit vehicles) with a variable prepaid forward on 1,000,000 shares (initial price $97.15, cap $149.51, maturing November 2027, up to ~$89.3 million cash). Ribbit Capital fell to 5% or less by December 31, 2024. [DEF 14A 2026, L2441–L2494; L671]
- Trading plans: Bhatt's living trust adopted a Rule 10b5-1 plan on November 13, 2025 to sell up to 3,000,000 Class A shares by February 10, 2027; Steven Quirk, Jonathan Rubinstein, Paula Loop and Dara Treseder adopted smaller plans in November–December 2025. [10-K FY2025, Item 9B, L4668–L4676]

### 15d. Executive compensation (2025 program)

- CEO: "Since our IPO in 2021, our CEO's compensation has been limited to a modest base salary. He does not participate in the annual cash incentive program and has not received new equity awards. The Board is evaluating potential future compensation arrangements for Mr. Tenev following the vesting of his remaining equity incentive compensation in 2025." Salary $34,248; 2025 total compensation $3,004,978, of which personal security $1,722,904 and personal use of private aircraft $1,247,826. No offer letter or employment agreement. [DEF 14A 2026, L1663, L1682, L1907, L1927, L1965]
- The 2019/2021 founder awards: market-based RSUs with share-price hurdles; the 2021 award (35.5 million unvested shares) was cancelled in February 2023 with a $485 million charge and no replacement; all remaining Market-Based RSUs were fully vested by December 31, 2025 (10-K, section 8c). The proxy's pay-versus-performance table shows "compensation actually paid" to the CEO of $1,020,806,245 for 2025, driven by a $1,017,801,267 change in value of prior-year awards that vested in 2025 (versus $91,877,214 for 2024 and negative $6,729,202 for 2023); the CEO's Summary Compensation Table total for 2021 was $796,124,647 (the IPO-year grant value). [DEF 14A 2026, L2248–L2266]
- Other NEOs (2025 total compensation): Steven Quirk $12,868,647; Daniel Gallagher $10,951,157; Jeffrey Pinner $6,617,148 (includes $1,000,000 second half of sign-on bonus); Jason Warnick $12,852,985. Salaries $550,000 each, unchanged; target bonus 75% of salary; 2025 bonus paid at 177.3% of target ($731,528 each) on measures of total net revenues (25%), adjusted net income (25%), Net Deposits (20%), Gold Subscriber growth (20%) and International Net Funded Accounts (10%, new; paid at 54%). 2025 refresh RSU grants (four-year quarterly vesting): Quirk $12 million, Gallagher $10 million, Pinner $4.5 million, Warnick $12 million (grant-date fair values $11,524,232 / $9,603,541 / $4,321,598 / $11,524,232). "In 2025, 94% of our non-CEO NEOs' compensation, on average, was tied to performance." [DEF 14A 2026, L1682–L1760, L1907–L1920]
- New CFO terms: Verma's initial CFO compensation was salary $500,000, target bonus 60%, annual equity target $2,350,000; on March 18–19, 2026 the committee set salary $600,000, bonus target 75% and "a promotion grant of restricted stock units with a grant date target value equal to approximately $18 million ... vesting over a four year period". [8-K 2026-02-10, Item 5.02; 8-K/A 2026-03-24, Item 5.02] Bazzano: salary $425,000, 40% bonus target, $1,540,000 annual equity target, $3,300,000 sign-on RSUs over two years, $400,000 sign-on bonus. [8-K 2026-06-26, Item 5.02]
- Peer group (2025): Affirm, Block, Coinbase, DoorDash, Duolingo, Etsy, Interactive Brokers, Lyft, Maplebear, Pinterest, Rocket Companies, Snap, SoFi, Zillow. Independent consultant Pay Governance. Clawback policies (Nasdaq-required and a detrimental-conduct policy). Stock ownership guidelines met by all executives at end-2025. [DEF 14A 2026, L1808–L1840, L1856–L1880]
- CEO pay ratio: $3,004,978 vs median employee $194,162 = "approximately 15.5 times". [DEF 14A 2026, L2226–L2230]
- Say-on-pay: 2025 meeting 98.5% in favour of 2024 pay; annual frequency. 2026 meeting (June 2, 2026): For 1,512,304,895 / Against 21,260,133 / Abstain 911,177 / broker non-votes 142,176,341 — 98.6% of votes cast for and against (computed). [DEF 14A 2026, L1844; 8-K 2026-06-03, Item 5.07]
- Severance: "Change in Control and Severance Plan for Key Employees" (change in control defined as a transfer of 50% or more of voting power, among other events); Pinner is eligible for termination-without-cause benefits under it. [DEF 14A 2026, L2065–L2124; 8-K 2026-05-08]

### 15e. 2026 annual meeting (June 2, 2026; record date April 8, 2026) — vote results

- Proposal 1 (elect ten directors), votes for / against / abstain (broker non-votes 142,176,341 for each): Tenev 1,516,032,205 / 16,283,549 / 2,160,452; Bhatt 1,529,875,425 / 3,988,937 / 611,844; Hegeman 1,529,736,300 / 4,002,045; Loop 1,528,306,597 / 5,412,651; Malka 1,528,741,308 / 4,972,387; Payne 1,528,763,693 / 4,922,966; Rubinstein 1,391,197,660 / 142,524,705 / 753,841; Segal 1,519,556,629 / 14,145,426; Treseder 1,457,188,310 / 76,500,640; Zoellick 1,457,398,884 / 76,317,163. All elected to serve until the 2027 meeting. [8-K 2026-06-03, Item 5.07]
- Proposal 2 (say-on-pay): approved (15d). Proposal 3 (ratify Ernst & Young for FY2026): 1,673,927,030 for / 1,836,483 against / 889,034 abstain. Class B carried ten votes per share; Class A and B voted together. No shareholder proposals were on the ballot. [8-K 2026-06-03, Item 5.07; DEF 14A 2026, proxy card L2774–L2790]
- Auditor: Ernst & Young LLP, San Francisco, "served as the Company's auditor since 2017". [10-K FY2025, Item 8, L2887]

---

## 16. Officer changes and the 8-K record inside the window (2025-07-01 to 2026-07-30)

| Filed | Form | Items | Substance |
|---|---|---|---|
| 2025-07-30 | 8-K | 2.02, 9.01 | Q2 2025 earnings release (not cached; IR gatherer's scope). |
| 2025-10-31 | 8-K | 2.02, 7.01, 9.01 | Rule 606(a) order-routing reports for Q3 2025 for RHF and RHS furnished as Exhibits 99.1/99.2 (see 9b). Signed by CFO Jason Warnick. |
| 2025-11-05 | 8-K | 2.02, 5.02, 9.01 | Q3 2025 earnings release; **CFO transition**: "On October 30, 2025, Jason Warnick ... informed the Company of his decision to retire ... he will transition from CFO ... to an advisory role in the first quarter of 2026 and will remain employed with the Company until September 1, 2026"; Shiv Verma (SVP Finance and Strategy, Treasurer) "will take over the role of CFO ... subject to his appointment by the Company's Board". |
| 2026-01-30 | 8-K | 2.02, 7.01, 9.01 | Rule 606(a) reports for Q4 2025 (Exhibit 99.1 cached as `8-K-2026-01-30-ex991-606-RHF.txt`). Signed by Warnick. |
| 2026-02-10 | 8-K | 2.02, 5.02, 9.01 | Q4/FY2025 earnings release; **Shiv Verma appointed CFO effective close of business February 6, 2026** (age 40; principal financial and accounting officer); initial pay $500,000 salary, 60% bonus target, $2.35 million annual equity target. |
| 2026-02-18 / 02-20 | 10-K / 10-K/A | — | FY2025 annual report and formatting-only amendment (see tag key). |
| 2026-03-24 | 8-K | 1.01, 2.03, 7.01, 9.01 | RHS Fifth Amended and Restated Credit Agreement (March 20, 2026): $3.25 billion 364-day secured revolver, accordion to $4.875 billion, JPMorgan agent, 0.45% commitment fee; **new $1.5 billion repurchase program** (Item 7.01) replacing the prior one, ">$1.1 billion of incremental capacity", roughly three years. |
| 2026-03-24 | 8-K/A | 5.02 | Verma's CFO pay set: $600,000 salary, 75% bonus target, ~$18 million promotion RSU grant vesting over four years. Signed by Tenev. |
| 2026-04-22 | DEF 14A, DEFA14A, ARS | — | Proxy for the June 2, 2026 meeting; DEFA14A (agent prefix 0001193125) is the notice of internet availability (read, not cached: no content beyond the meeting date, record date and three proposals); ARS is the annual report to shareholders as a PDF (not fetched). |
| 2026-04-28 | 8-K | 2.02, 9.01 | Q1 2026 earnings release (body cached; exhibit is the IR gatherer's `press-release-2026-Q1.txt`). |
| 2026-04-29 | 10-Q | — | Q1 2026 quarterly report (cached). |
| 2026-05-08 | 8-K | 5.02 | "On May 7, 2026, Robinhood Markets, Inc. determined that Jeffrey Pinner, Chief Technology Officer, would be separating from his position, effective the same day", eligible for termination-without-cause benefits under the CIC and Severance Plan. No successor named. |
| 2026-06-03 | 8-K | 5.07 | Annual meeting results (15e). |
| 2026-06-16 | 8-K | 2.05 | **Workforce reduction**: ~10% of full-time employees plus closure of open roles; ~$20 million cash severance and benefits and ~$8 million share-based compensation, accrued in Q2 2026; "taking this action from a position of business strength, including June month-to-date average daily trading volumes at record levels across equities, options, and prediction markets." |
| 2026-06-23 | 8-K | 8.01, 9.01 | Launch and pricing (June 22, 2026) of $2.0 billion 0.00% convertible senior notes due 2029 (exhibits cached). Launch release: ~$300 million of proceeds for repurchases; capped calls "intended to offset any share dilution until at least a targeted 125% premium". |
| 2026-06-25 | 8-K | 1.01, 2.03, 3.02, 7.01, 8.01, 9.01 | Closing of $2.2 billion notes (option exercised in full June 23), indenture with U.S. Bank Trust Company, conversion rate 5.7332 (~$174.42), capped calls (strike $174.4227, cap $237.8475, ~12,613,040 shares), maximum 20,811,560 shares issuable; **Item 8.01: ~$290 million of proceeds used to repurchase 2,743,000 shares at $105.71**. |
| 2026-06-26 | 8-K | 5.02 | Dara Bazzano appointed principal accounting officer effective June 25, 2026; Verma remains CFO and principal financial officer. |
| 2026-07-14 | 40-APP | — | Exemptive application (agent prefix 0000950103, Davis Polk) by Robinhood Ventures Fund I–IV, Robinhood Ventures DE, LLC, Robinhood Asset Management, RHM, RHEU and Robinhood Assets (Jersey) Limited for an SEC order under Sections 17(d) and 57(i) of the Investment Company Act and Rule 17d-1 "permitting certain joint transactions otherwise prohibited" (co-investment among the Robinhood-advised funds and affiliates); dated July 13, 2026; fund board resolutions adopted June 24, 2026. RVI is "a non-diversified, closed-end management investment company registered under the 1940 Act"; RVII intends to elect BDC status. Context for the Ventures/asset-management growth engine, not core. |
| 2026-07-16 | 40-6B | — | Application by RHM and Robinhood Employee Fund, LP under Sections 6(b) and 6(e) of the Investment Company Act for an order exempting an "employees' securities company" (a fund through which eligible Robinhood employees can invest) from certain provisions of the Act; 24 pages; signed by Shiv Verma July 16, 2026. Context only. |
| 2026-07-29 | 8-K | 2.02, 9.01 | Q2 2026 earnings release (body cached; exhibit is the IR gatherer's `press-release.txt`). |
| 2026-07-30 | 10-Q | — | Q2 2026 quarterly report (cached). |

- Also in the window and ignored per instructions: 167 Forms 4, one Form 4/A, three Forms 3, 63 Forms 144, one S-8; nine Schedule 13G/13G-A filings (2025-07-17, 10-06, 10-17, 10-31, 11-05; 2026-03-27, 04-30, 05-18, 07-23). The 10-Qs of 2025-07-31 (Q2 2025) and 2025-11-06 (Q3 2025) were not cached because the Q2 2026 10-Q carries the year-ago comparatives. [submissions JSON]
- Officer changes summarised: CFO Warnick → Verma (announced November 5, 2025; effective February 6, 2026; Warnick advisory role to September 1, 2026); CTO Pinner separated May 7, 2026; CAO Bazzano joined April 2026 and became principal accounting officer June 25, 2026; co-founder Bhatt resigned as Chief Creative Officer in March 2024 (remains a director). [8-Ks above; 10-K FY2025, Note 12, L4435]

---

## 17. Capital allocation: what the filings say

- "Our liquidity needs are primarily to support and invest in our core business, including investing in new ways to serve our customers, potentially seeking strategic acquisitions to leverage existing capabilities and further build our business, and for general capital needs (including capital requirements imposed by regulators and SROs and cash deposit and collateral requirements under the rules of the DTC, NSCC, OCC, and CFTC)." "We seek potential acquisitions to leverage existing capabilities and further build out our business." [10-K FY2025, Item 7, L2609, L2649]
- Buybacks: $1.5 billion program from March 2026 over "approximately three years"; prior program "over the next roughly two years with flexibility to accelerate if market conditions warrant"; $290 million bought concurrently with the notes. [8-K 2026-03-24; 10-K FY2025, Note 12, L4344; 8-K 2026-06-25]
- Debt: the June 2026 notes were an "Opportunistic capital raise with proceeds used to enhance strategic flexibility to invest for future growth". [8-K-2026-06-23-ex991.txt; -ex992.txt]
- No dividends, by policy and credit-facility restriction (section 8c). Cash acquisitions FY2025: TradePMR ($175 million), Bitstamp ($224 million); 2026: MIAXdx (Rothera, $79 million incl. SIG's $41 million), WonderFi ($178 million). Purchases of non-marketable securities for RVI $244 million (FY2025) and $228 million (H1 2026). [sections 1b, 5]
- Equity issuance: none for cash since the IPO other than the RVI IPO ($312 million to non-controlling interests, since deconsolidated); acquisition shares only for TradePMR (2,049,711 unvested). [10-Q Q2 2026, L512; 10-K FY2025, Item 5, L2117]

---

## 18. Other items the writer may need

- RVI (Robinhood Ventures Fund I): launched September 2025; IPO on the NYSE March 6, 2026 ($312 million net to non-controlling interests); on June 25, 2026 Robinhood "sold a portion of our ownership interest in RVI, resulting in the loss of a controlling financial interest" for $22 million cash, derecognised $673 million of net assets and $322 million of non-controlling interest, remeasured its retained interest at $435 million (fair value $437 million at 6/30/2026, in other current assets), recognised a $106 million gain, and RHV "remains the advisor to RVI and charges a management fee of 2% of RVI's net asset value". [10-Q Q2 2026, Note 4, L847–L855]
- Goodwill $516 million and intangibles $246 million at 6/30/2026 ($101 million indefinite-lived licences); amortisation $7 million per quarter; no impairment. [10-Q Q2 2026, Note 5, L859–L900]
- Internal control: management's FY2025 ICFR assessment excluded TradePMR and Bitstamp; WonderFi will be excluded for 2026. [10-K FY2025, L2905; 10-Q Q2 2026, Item 4, L2219]
- Subsequent events disclosed in the Q2 2026 10-Q (all before the 2026-07-30 cutoff): Robinhood Chain launched July 2026; Trump Accounts launched July 4, 2026; Singapore CMS licence granted July 1, 2026; $500 million credit-card ABS issued July 23, 2026; Wisconsin dismissed RHM on July 8, 2026. [10-Q Q2 2026, L655, L1281, L1567, L2669, L3317]
- Contract liabilities: unearned Gold subscription revenue $39 million (12/31/2025) and $59 million (6/30/2026); TradePMR performance obligations $17 million → $13 million. Contract receivables from market makers etc. $185 million → $325 million. [10-K FY2025, Note 5, L3817; 10-Q Q2 2026, Note 6, L961–L969]
- Deferred customer match incentives (IRA/transfer matches, amortised over holding periods): $185 million current + $428 million non-current at 12/31/2025; $220 million + $579 million at 6/30/2026. [10-K FY2025, L2953; 10-Q Q2 2026, L361]
- Performance graph base: $34.82 closing price on July 29, 2021; aggregate market value of non-affiliate stock at June 30, 2025 ~$71.3 billion. [10-K FY2025, L2152; cover L81]

---

## 19. Gaps / not disclosed in the fetched filings

- FY2021 Gold Subscribers precisely (only "1.3 million" in prose), FY2021 split of other revenues, FY2021 headcount (FY2021 10-K not fetched), and Investment Accounts before FY2024.
- MAU after FY2023 (dropped from the KPI tables).
- Payment-for-order-flow revenue by market maker in dollars, rebate rates per contract or per share, and total PFOF as a dollar figure (only percentages of total net revenues by counterparty, and the partial Rule 606 venue amounts for RHF).
- The amount of the December 2020 SEC best-execution settlement, the June 2025/June 2026 class-action settlement, the cash-sweep settlement in principle, and the Nebraska/Massachusetts Division of Banks fines.
- Revenue or profit by geography beyond "Substantially all of our revenues and assets are attributed to or located in the United States"; Bitstamp's revenue beyond "one percent of consolidated total net revenues" for FY2025; U.K./EU customer counts beyond "over 750,000" international customers.
- Robinhood Gold pricing (the "flat recurring rate" is not stated), Gold Card balances outstanding by delinquency, and the credit-card portfolio's charge-off rate.
- Cash Sweep program bank list and the rate paid to Gold vs non-Gold customers; margin interest rate tiers.
- Prediction-market volumes or contracts by quarter (only "over 12 billion event contracts in 2025"); futures revenue separately (inside "Other").
- The reason the Q2 2026 balance sheet shows Class A "790 million" (rounded) rather than an exact count; exact counts exist only on the covers and in the proxy.
- Any explicit forward guidance (the filings give none beyond the rate-sensitivity table and the statement that Fed cuts "will negatively impact our net interest revenues").
- The Pluto acquisition (not named in any fetched filing text that was read).
- Indonesian acquisitions' closing status as of the Q2 2026 10-Q.
