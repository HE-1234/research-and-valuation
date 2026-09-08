# Damodaran on horizon, terminal ROIC, heavy reinvestment, and the transition — primary-source findings

Compiled 2026-09-08. Every claim below is tied to a file/cell reference or a URL.
Where I could not find evidence, the text says **not found** rather than guessing.

## One-page answer summary

| Q | Answer | Confidence |
|---|---|---|
| Q1 horizon rule | Three factors, verbatim from Ch. 12: firm size relative to its (growing) market; current growth rate and current excess returns; magnitude and sustainability of competitive advantages — the third being "perhaps the most critical". P&G gets 5 years, Amgen 10. Blog 2023: "ten years is already at the 90th percentile of growth periods … 20-25 years risks making your company a unicorn." | high |
| Q1 ginzu structure | 10 explicit years + terminal, hard-wired. Growth: separate year-1 input, then constant years 2-5, then **linear** fade to terminal growth (= risk-free rate) reaching it in year 10. Tax: effective flat years 1-5, then **linear** to marginal by year 10. Cost of capital: initial flat years 1-5, then **linear** to stable (risk-free + mature-market ERP) by year 10. Margin: **linear** to target by a user-chosen convergence year, then flat. Sales-to-capital: **two inputs**, years 1-5 and years 6-10. | high |
| Q2 terminal ROIC | Question: "I will assume that your firm will earn a return on capital equal to its cost of capital after year 10…" Default = **ROIC = stable WACC** (no excess return). Acceptable to exceed it when there are durable competitive advantages; his rule of thumb is to move ROIC "to or towards **industry averages**". In practice he overrode it in every moated company: **+6.4 to +11.4 points** for the Mag 7 (Alphabet 15% vs 8%), +4.0 for Alphabet 2018, 0.00 for Intel/Walgreens/Netflix/Instacart. | high |
| Q3 heavy reinvestment | Never gross capex minus depreciation for forecasting — always Δrevenue ÷ sales-to-capital, and g ÷ ROIC in the terminal year. **He does lag reinvestment**: the current model defaults to a **one-year lag**, allows up to three, and he set **three years** for NVIDIA in Sep 2024 and Jan 2025. He does **not** lengthen the horizon. His stated principle: "Companies that have built capacity in advance of growth will be worth more than companies that will have to reinvest contemporaneously to deliver growth." | high |
| Q4 the year-6 cliff | He never writes the sentence "terminal cash flow below the final explicit year" (**not found** in books, spreadsheet or 64 posts) — but the notch is present in **every** DCF he has published, −5% to −38%, caused by the ROIC/reinvestment-rate step. His prescribed remedy for a one-step transition is explicit and repeated: a **transition phase in which growth, reinvestment rate and cost of capital move to stable levels in linear increments** (three-stage / n-stage), which is what years 6-10 of his spreadsheet are. The warning he *does* write is the mirror image: carrying high-growth capex into perpetuity "will understate the true value". | high on the prescription and the computed notch; medium/low on his ever having stated the notch |

## Sources used

| Ref | What it is | Location |
|---|---|---|
| S1 | `fcffsimpleginzu.xlsx`, dated 1 Feb 2026 (cell `Input sheet!B3`), shipped example company "Almarai" | downloaded 2026-09-08 from https://pages.stern.nyu.edu/~adamodar/pc/fcffsimpleginzu.xlsx ; local copy `/tmp/damo/fcffsimpleginzu.xlsx` |
| S2 | His Alphabet valuation workbook, valuation date 1 Mar 2018 (`Input sheet!B1`) | `/tmp/damo/AlphabetApr2018.xlsx` |
| S3 | His NVIDIA valuation workbook, valuation date 1 Jun 2023 (`Input sheet!B3`) | `/tmp/damo/NVIDIA2023.xlsx` |
| S4 | *Investment Valuation*, Ch. 12, "Closure in Valuation: Estimating Terminal Value" | `/tmp/damo/ch12.txt` (from `ch12.pdf`) |
| S5 | *Investment Valuation*, Ch. 14, FCFE models | `/tmp/damo/ch14.txt` |
| S6 | *Investment Valuation*, Ch. 15, FCFF models | `/tmp/damo/ch15.txt` |
| S7 | *Investment Valuation*, Ch. 10, "From Earnings to Cash Flows" | `/tmp/damo/ch10.txt` |
| S8 | **31 valuation workbooks he linked from blog posts, 2023-2026**, harvested from `https://pages.stern.nyu.edu/~adamodar/pc/blog/<name>.xlsx` | local copies in `/tmp/damo/web/` (Google2024, MSFT2024, Meta2024, Amazon2024, Apple2024, NVIDIA2024, Nvidia2024, NvidiaJan2025, TeslaJan2023/2024/2025DIY, Tesla2023OctDIY, CocaCola2024, Nike2024, Starbucks2024, Intel2024, Walgreens2024, Disney2023, Netflix2023, InstacartIPO, BirkenstockIPO2023, SpaceX2026IPO, SpaceX2026IPOUpdated, …) |
| S9 | His blog, all 681 posts enumerated via the Blogger feed API; full text of the 89 posts published 2023-01-01 → 2026-09-02 | `https://aswathdamodaran.blogspot.com`; local copies `/tmp/damo/web/posts/` |

---

## Q1. Horizon — how long is the high-growth period, and what does fcffsimpleginzu actually do?

### 1a. His stated rule for 5 vs 10 years (S4, Ch. 12, section "I. Length of the High Growth Period")

He frames the choice as a joint judgment about growth *and* excess returns, and lists exactly three factors:

> "Thus, when you assume that a firm will experience high growth for the next 5 or 10 years, you are also implicitly assuming that it will earn excess returns (over and above the required return) during that period. In a competitive market, these excess returns will eventually draw in new competitors and the excess returns will disappear.
> You should look at three factors when considering how long a firm will be able to maintain high growth."

**Factor 1 — size of the firm relative to its market:**
> "1. Size of the firm: Smaller firms are much more likely to earn excess returns and maintain these excess returns than otherwise similar larger firms. This is because they have more room to grow and a larger potential market. Small firms in large markets should have the potential for high growth (at least in revenues) over long periods. When looking at the size of the firm, you should look not only at its current market share, but also at the potential growth in the total market for its products or services. A firm may have a large market share of its current market, but it may be able to grow in spite of this because the entire market is growing rapidly"

**Factor 2 — existing growth rate and existing excess returns:**
> "2. Existing growth rate and excess returns: Momentum does matter, when it comes to projecting growth. Firms that have been reporting rapidly growing revenues are more likely to see revenues grow rapidly at least in the near future. Firms that are earnings [sic] high returns on capital and high excess returns in the current period are likely to sustain these excess returns for the next few years."

**Factor 3 — magnitude and sustainability of competitive advantages (he calls this the most important):**
> "3. Magnitude and Sustainability of Competitive Advantages: This is perhaps the most critical determinant of the length of the high growth period. If there are significant barriers to entry and sustainable competitive advantages, firms can maintain high growth for longer periods. If, on the other hand, there are no or minor barriers to entry or if the firm's existing competitive advantages are fading, you should be far more conservative about allowing for long growth periods. The quality of existing management also influences growth."

And the framing sentence at the top of the chapter (S4, Ch. 12 opening):
> "Will the growth rate drop abruptly at a point in time to a stable growth rate or will it occur more gradually over time? To answer these questions, we will look at a firm's size (relative to the market that it serves), its current growth rate and its competitive advantages."

**Worked examples (S4, Illustration 12.1):** Con Ed → "already a stable growth firm"; Procter & Gamble → "Brand name can sustain excess returns and growth higher than the stable growth rate for a short period – we will assume **five years**"; Amgen (patents + expanding market) → "The patents that Amgen has will protect it from competition and the long lead time to drug approval will ensure that new products will take a while getting to the market. We will allow for **ten years** of high growth and excess returns. There is clearly a strong subjective component to making a judgment on how long high growth will last."

So the 5-vs-10 split in his own examples turns on patent/structural protection and room to grow in an expanding market (10) versus a strong but eroding brand in a mature market (5).

### 1a-bis. His current, published rule of thumb on horizon length (S9, blog, 2 Feb 2023)

The most direct modern statement is in "Disagreements and First Principles: The Pushback on my Tesla Valuation", https://aswathdamodaran.blogspot.com/2023/02/disagreements-and-first-principles.html :

> "Second, as you get past year 5, the revenue growth rate does not drop precipitously to 3.47% in year 6 (more on that in the next bullet), and instead declines, in linear terms, between years 6 and 10 to approach 3.47% in 2032. **In short, the company has ten years of growth, not five, but growth rates have to get smaller as revenues gets bigger.**"

> "You may decide that this is too pessimistic, but if you do so, the response is not to increase the growth rate from 3.47% to a higher value after year 10, but to either use higher growth in the next ten years to reach revenues of $500 or $600 billion in year 10, or lengthen the growth period to 15 or 20 years. If you do the latter, remember that **growth dissipates between 4-6 years for most growth companies, ten years is already at the 90th percentile of growth periods for the companies and using 20-25 years of growth risks making your company a unicorn.**"

And on why terminal growth is the risk-free rate, same post:
> "The second is the question of what the nominal growth in the global economy, in US dollar terms, will be, and **my best answer to that question is the nominal risk free rate**, which was 3.47% at the time of this valuation."

So his practical position: **10 years is his working horizon and is already generous (90th percentile of observed growth durations); five is the short case; 15-20 is reserved for the exceptional; beyond that you are inventing a unicorn.** Note also that he describes the 10 years as "ten years of growth, not five" — the years 6-10 fade counts as growth, not as a terminal appendage.

**Confidence: high.**

### 1b. The default structure of fcffsimpleginzu (S1)

Verified cell by cell on the Feb-2026 file. Columns `C..L` on `Valuation output` are years 1-10; column `M` is the terminal year.

| Item | Mechanic | Cells (S1) |
|---|---|---|
| Explicit forecast length | **10 years**, plus a terminal year (column M). There is no user input for horizon length — 10 years is hard-wired. | `Valuation output!C1:M1` = 1,2,…,10,"Terminal year" |
| Revenue growth, year 1 | Its own input (so you can use guidance/contracts) | `Input sheet!B26` |
| Revenue growth, years 2-5 | A second input, **held constant across years 2,3,4,5** | `Input sheet!B28`; `Valuation output!D2='Input sheet'!B28`, `E2=D2`, `F2=E2`, `G2=F2` |
| Revenue growth, years 6-10 | **Fades linearly** from the year-5 rate to the terminal growth rate in five equal steps, so year 10 growth already equals terminal growth | `H2 = G2-((G2-$M$2)/5)`; `I2 = G2-((G2-$M$2)/5)*2`; … `L2 = G2-((G2-$M$2)/5)*5` (i.e. `L2 = M2`) |
| Terminal growth | Default = the risk-free rate | `M2` → `Input sheet!B34`; on-sheet text `A66`: "I will assume that the growth rate in perpetuity will be equal to the risk free rate. This allows for both valuation consistency and prevents 'impossible' growth rates." |
| **Tax rate** | Effective rate held flat years 1-5, then **fades linearly** to the marginal rate over years 6-10, reaching marginal in year 10 | `C6..G6` = `Input sheet!B23` (effective); `H6=G6+($M$6-$G$6)/5` … `L6=K6+($M$6-$G$6)/5`; `M6` = `Input sheet!B24` (marginal). On-sheet text `A58`: "I will assume that your effective tax rate will adjust to your marginal tax rate by your terminal year." |
| **Cost of capital** | Initial WACC held flat years 1-5, then **fades linearly** to the stable WACC over years 6-10, reaching it in year 10 | `C12..G12` = `Input sheet!B35`; `H12=G12-($G$12-$M$12)/5` … `L12=K12-($G$12-$M$12)/5`; `M12` = stable WACC |
| Stable WACC default | Risk-free rate **+ the current mature-market ERP** (4.23% at 1 Jan 2026), giving 8.81% in the shipped file. Note the on-sheet prose still says "+4.5%" while the formula uses the live mature-market ERP. | `A44`: "In stable growth, I will assume that your firm will have a cost of capital similar to that of typical mature companies (riskfree rate + 4.5%)"; formula `M12` = `Input sheet!B34 + 'Country equity risk premiums'!B1`; `'Country equity risk premiums'!A1:B1` = "Mature Market ERP +", 0.0423, "Updated January 1, 2026" |
| **Operating margin** | **Linear** interpolation from the year-1 margin to the target margin, reaching the target in a **user-chosen convergence year**, then held flat to the terminal year | Target = `Input sheet!B29`; convergence year = `Input sheet!B30` (default 5 in the shipped file); `D4 = IF(D1>B30, B29, B29-((B29-$C$4)/B30)*(B30-D1))` and the same formula across `E4:L4`; `M4=L4`. Comment on `B30`: "This is the forecast year in which your current margin will converge on target." |
| **Sales-to-capital** | **Two separate inputs**: one applied to years 1-5, a second applied to years 6-10 | `Input sheet!B31` → `Valuation output!C38:G38`; `Input sheet!B32` → `H38:L38`. Comment on `B32`: "I give you a second chance to input the sales to invested capital to allow for the fact that as companies scale up they might need to reinvest less (or more) to get the same growth." |
| Reinvestment, years 1-10 | Change in revenue ÷ sales-to-capital, **with a one-year lag by default** (see Q3) | `C8 = IF(B56="No",(D3-C3)/C38, …)` — note it uses *next* year's revenue increment |
| Reinvestment, terminal year | Reinvestment rate = g ÷ stable ROIC | `M8 = IF(M2>0,(M2/M40)*M7,0)` |

So the shape is: **1 + 4 + 5 explicit years + terminal**; growth constant in years 2-5; growth, tax rate and cost of capital all fade **linearly** over years 6-10 and arrive at their stable values in year 10; the operating margin converges **linearly** to target by a year you choose (default 5) and then stays there; sales-to-capital switches once, at year 6.

**Confidence: high** (read directly off the formulas).

Cross-check on the older workbooks: S2 (Alphabet 2018) has the same 10-year + terminal frame with linear fades (`Valuation output!H2..L2` step 12% → 2.75%; `H12..L12` step 8.26% → 8.00%) but its margin convergence year is 10 (`Input sheet!B25` = 10) and it has only **one** sales-to-capital input (`B26`), not two. S3 (NVIDIA 2023) already has the split sales-to-capital (`B30` years 1-5, `B31` years 6-10) and a margin convergence year of 5 (`B29`).

---

## Q2. Terminal return on capital

### 2a. The question the spreadsheet asks, and the default (S1)

The on-sheet prose, verbatim:

> `Input sheet!A47`: "I will assume that your firm will earn a return on capital equal to its cost of capital after year 10. I am assuming that whatever competitive advantages you have today will fade over time."
> `Input sheet!A48`: "Do you want to override this assumption =" → **`B48` default = "No"**
> `Input sheet!A49`: "If yes, enter the return on capital you expect after year 10" (`B49`, placeholder 0.15)
> `Input sheet!C48`: "Mature companies find it difficult to generate returns that exceed the cost of capital"
> `Input sheet!C49`: "But there are significant exceptions among companies with long-lasting competitive advantages."

The formula that implements it: `Valuation output!M40 = IF('Input sheet'!B48="Yes",'Input sheet'!B49,'Valuation output'!L12)` — i.e. **if you do not override, stable ROIC is set equal to the year-10 (= stable) cost of capital.** In the shipped file that is 8.81%.

Cell comment on `B49` (his advice on how far to push it):
> "Even if you believe your firm has significant competitive advantages, you should expect the return on capital for a company to come down over time, at least on new projects. If you don't see long term competitive advantages, you should just leave the cell above at No."

The Diagnostics sheet turns it into a dial: `Diagnostics!A42` "Return on capital in perpetuity (B48, B49)" → `B42` (if your value looks too low) "Increase relative to your cost of capital"; `C42` (if too high) "If higher than your cost of capital, lower towards your cost of capital". `Diagnostics!G22` asks: "Are you comfortable with your return on capital in year 10?" and `Diagnostics!E27` reports "Stable ROC" next to "ROC in year 10" and the "Marginal (1-10)" ROIC.

### 2b. When it is acceptable to let stable ROIC exceed the cost of capital, and by how much (S4, Ch. 12)

His clearest statement, from "II. Characteristics of Stable Growth Firm → b. Project Returns":

> "High growth firms tend to have high returns on capital (and equity) and earn excess returns. In stable growth, it becomes much more difficult to sustain excess returns. There are some who believe that the only assumption consistent with stable growth is to assume no excess returns; the return on capital is set equal to the cost of capital. While, in principle, excess returns in perpetuity are not feasible, it is difficult in practice to assume that firms will suddenly lose the capacity to earn excess returns. Since entire industries often earn excess returns over long periods, assuming a firm's returns on equity and capital will move towards **industry averages** will yield more reasonable estimates of value."

And the explicit acknowledgement that his own examples build in perpetual excess returns (end of Illustration 12.3):

> "For all of the firms, it is worth noting that you are assuming that excess returns continue in perpetuity by setting the return on capital above the cost of capital. While this is potentially troublesome, the competitive advantages that these firms have built up historically or will build up over the high growth phase will not disappear in an instant. The excess returns will fade over time, but moving them to or towards industry averages in stable growth seems like a reasonable compromise."

On magnitude, his rule of thumb is "towards the industry average", and in the P&G case he splits the difference explicitly:
> "We also assume that the return on equity will drop to 15%, about halfway between the cost of equity and the average return on equity earned by brand name companies similar to Procter & Gamble today."

He also flags the consequence: "If the return on capital is higher than the cost of capital in the stable growth period, increasing the stable growth rate will increase value. If the return on capital is equal to the [cost of capital], increasing the stable growth rate will have no effect on value" (S4, Ch. 12) — i.e. the excess-return spread is the only thing that makes terminal growth worth anything.

**Confidence: high.**

### 2c. Table — stable ROIC vs stable cost of capital in his own valuations

Every row below is read from `Valuation output!M12` (terminal cost of capital) and `M40`/`M59` (terminal ROIC) of the actual workbook, and the override flags from `Input sheet`. "Default" means he left the override at "No", so the model set stable ROIC = the year-10 cost of capital.

| Company | Date of valuation | Stable ROIC | Stable WACC | Diff (pts) | Terminal g | Source |
|---|---|---|---|---|---|---|
| **Alphabet** | **1 Feb 2024** | **15.00%** (override) | **8.00%** (override) | **+7.00** | 4.08% | S8 `Google2024.xlsx` `Input sheet!B48`="Yes",`B49`=0.15; `B45`="Yes",`B46`=0.08; verified `Valuation output!M40`=0.15, `M12`=0.08 |
| Microsoft | 1 Feb 2024 | 15.00% (override) | 8.40% (override) | +6.60 | 4.08% | S8 `MSFT2024.xlsx` |
| Meta | 1 Feb 2024 | 15.00% (override) | 8.58% (default) | +6.42 | 4.08% | S8 `Meta2024.xlsx` |
| Amazon | 1 Feb 2024 | 15.00% (override) | 8.00% (override) | +7.00 | 4.08% | S8 `Amazon2024.xlsx` |
| Apple | 1 Feb 2024 | 15.00% (override) | 8.00% (override) | +7.00 | 4.08% | S8 `Apple2024.xlsx` |
| NVIDIA | 1 Feb 2024 | 20.00% (override) | 8.58% (default) | +11.42 | 4.08% | S8 `NVIDIA2024.xlsx` `B59`="Yes",`B60`=0.20; `B56`="No" |
| NVIDIA | 1 Jun 2023 | 20.00% (override) | 8.85% (default) | +11.15 | 3.60% | S3 / S8 `NVIDIA2023.xlsx` |
| NVIDIA | 1 Sep 2024 | 20.00% (override) | 8.49% (override) | +11.51 | 3.73% | S8 `Nvidia2024.xlsx` `B57`=0.0849 |
| NVIDIA | 1 Jan 2025 | 20.00% (override) | 8.50% (override) | +11.50 | 4.70% | S8 `NvidiaJan2025.xlsx` `B57`=0.085 |
| **Alphabet** | **1 Mar 2018** | **12.00%** (override) | **8.00%** (override) | **+4.00** | 2.75% | S2 `AlphabetApr2018.xlsx` `B42`="Yes",`B43`=0.12; `B39`="Yes",`B40`=0.08 |
| Tesla | 1 Jan 2023 | 18.00% | 9.00% | +9.00 | 3.47% | S8 `TeslaJan2023DIY.xlsx` |
| Tesla | 1 Oct 2023 | 15.00% | 9.00% | +6.00 | 5.00% | S8 `Tesla2023OctDIY.xlsx` |
| Tesla | 28 Jan 2024 | 15.00% | 8.68% | +6.32 | 4.08% | S8 `TeslaJan2024DIY.xlsx` |
| Tesla | 14 Mar 2025 | 15.00% | 8.35% | +6.65 | 4.22% | S8 `TeslaJan2025DIY.xlsx` |
| Coca-Cola | 1 Sep 2024 | 21.95% | 7.415% | +14.54 | 3.72% | S8 `CocaCola2024.xlsx` |
| Nike | 1 Sep 2024 | 20.00% | 7.83% (default) | +12.17 | 3.72% | S8 `Nike2024.xlsx` |
| Starbucks | 1 Sep 2024 | 12.00% | 7.83% (default) | +4.17 | 3.72% | S8 `Starbucks2024.xlsx` |
| Disney | 1 Sep 2023 | 12.00% | 9.00% (default) | +3.00 | 4.00% | S8 `Disney2023.xlsx` |
| Birkenstock (IPO) | 1 Sep 2023 | 12.00% | 7.74% (default) | +4.26 | 2.74% | S8 `BirkenstockIPO2023.xlsx` |
| SpaceX (IPO) | 1 Apr 2026 | 15.00% | 8.00% | +7.00 | 4.20% | S8 `SpaceX2026IPO.xlsx` |
| SpaceX (IPO, updated) | 1 Jun 2026 | 15.00% | 8.25% | +6.75 | 4.56% | S8 `SpaceX2026IPOUpdated.xlsx` `B55`="Yes",`B56`=0.15; `B52`="Yes",`B53`=0.0825 |
| **Intel** | **1 Sep 2024** | **7.83% = WACC** (default) | **7.83%** | **0.00** | 3.72% | S8 `Intel2024.xlsx` `B59`="No" |
| **Walgreens** | 1 Sep 2024 | **7.83% = WACC** (default) | 7.83% | **0.00** | 3.00% | S8 `Walgreens2024.xlsx` |
| **Netflix** | 1 Sep 2023 | **9.00% = WACC** (default) | 9.00% | **0.00** | 4.00% | S8 `Netflix2023.xlsx` |
| **Instacart (IPO)** | 1 Sep 2023 | **9.00% = WACC** (default) | 9.00% | **0.00** | 4.00% | S8 `InstacartIPO.xlsx` |
| fcffsimpleginzu shipped default | 1 Feb 2026 | 8.81% = WACC (default) | 8.81% | 0.00 | 4.58% | S1 `B48`="No"; `Valuation output!M40`=`L12`=0.0881 |
| Amgen (book) | 2001 | 20.00% | 8.86% | +11.14 | 5.00% | S4 Table 12.3; S6 Ch. 15 ("Cost of capital = 9.4% (0.9) + 6.15% (1-0.35) (0.1) = 8.86%") |
| Embraer (book) | 2000/01 | 15.00% | 12.74% | +2.26 | 3.00% real | S6 Ch. 15 |
| P&G (book, ROE) | 2000/01 | ROE 15.00% | stable cost of equity **not stated** | not computable | 5.00% | S4 Table 12.1 |
| Coca-Cola (book, ROE) | 2001 | ROE 20.00% | **not stated in Ch. 12** | not computable | 5.50% | S4 Table 12.2 |

**The pattern, stated plainly.** He never uses zero excess return for a company he thinks has a moat. He overrode the ROIC = WACC default in **every** growth/quality name (Mag 7, Tesla, Coca-Cola, Nike, Disney, SpaceX) and left it at the default only for the aging, broken or unproven (Intel, Walgreens, Netflix, Instacart). For the entire Magnificent Seven in Feb 2024 he used a **uniform 15% stable ROIC** (20% for NVIDIA) against stable costs of capital of 8.00-8.58% — i.e. **6.4 to 11.4 points of perpetual excess return**. His written justification is `Input sheet!C49`: "But there are significant exceptions among companies with long-lasting competitive advantages", backed by his own 2026 data:

> (S9, "Data Update 6 for 2026: In Search of Profitability!", 16 Feb 2026, https://aswathdamodaran.blogspot.com/2026/02/data-update-6-for-2026-in-search-of.html) "only 29% (28%) of global firms earn returns on equity (capital) that exceed their costs of equity (capital). In fact, if you raise the threshold and look at companies that generate 5% or more as excess returns, the numbers drop off to 19% (17%) … **Most companies have trouble earning their costs of equity and capital**, but if you look at the aggregated values, there are multiple sectors in the US (technology, consumer goods and communication services) that earn double digit excess returns"
> "**The most powerful explainer of excess returns … the capacity to generate excess returns comes from barriers to entry and competitive advantages.** In the language of value investing, it is the width (strength of competitive advantages) and depth (sustainability of competitive advantage) of moats that determine whether a company can earn more than its cost of equity or capital"

**Confidence: high** for every row read from a workbook cell (all rows except the P&G and Coca-Cola book rows, which are **not found / not computable** for the stable discount rate).

---

## Q3. Heavy reinvestment ahead of the revenue

### 3a. How reinvestment is computed: sales-to-capital, not gross capex minus depreciation

In the ginzu spreadsheet reinvestment is **never** built from gross capex and depreciation. It is derived from the revenue increment and a sales-to-capital ratio, and in the terminal year from g ÷ ROIC. His own explanation, on the `Stories to Numbers` sheet (S1, cell `H16`):

> "These are the numbers that come from your assumptions. The revenues over time reflect your revenue growth, the operating margins evolve towards your target margin and your tax rate will change, if you have set it to. **The reinvestment is estimated using the sales to capital ratio for the first 10 years and based on a reinvestment rate in stable growth (g/ ROC).**"

Formulas: `Valuation output!C8:L8` = Δrevenue ÷ sales-to-capital; `M8 = (M2/M40)*M7` = (g ÷ stable ROIC) × terminal EBIT(1−t).

The capex-minus-depreciation definition is his *accounting* definition of reinvestment when you are reading a past income statement, not his forecasting device. S7 (Ch. 10, "Reinvestment Needs"): "Two components go into estimating reinvestment. The first is net capital expenditures, which is the difference between capital expenditures and depreciation. The other is investments in non-cash working capital." He immediately warns it is hard to forecast: "firms often incur capital spending in chunks – a large investment in one year can be followed by small investments in subsequent years", plus the R&D and acquisition problems. And S6 (Ch. 15) tells you to sanity-check it against peers: "If reinvestment is estimated from net capital expenditures and change in working capital, the net capital expenditures should be similar to those other firms in the industry".

**Confidence: high.**

### 3b. Yes — he lags reinvestment, and in the current spreadsheet the lag is the default

This is the single most directly relevant finding for a capex-ahead-of-revenue company, and it is a feature he **added between 2018 and 2023**.

- S2 (Alphabet, 2018): reinvestment is contemporaneous. `Valuation output!C8 = (C3-B3)/C38` — this year's revenue increment. There is no lag option anywhere on the 2018 input sheet.
- S3 (NVIDIA, 2023) and S1 (Feb 2026): a lag option exists. On-sheet text, verbatim (S1 `Input sheet!A55`, identical at S3 `A66`):

> "**I assume that reinvestment in a year translates into growth in the next year, i.e., there is a one year lag between reinvesting and generating growth from that reinvestment.**"
> `A56`/`A67`: "Do you want override this assumption =" → default **"No"**
> `A57`/`A68`: "If yes, enter a different lag (0 = no lag to 3 = lag of 3 years)"

The formula confirms the default is a one-year lag: `Valuation output!C8 = IF('Input sheet'!$B$56="No",(D3-C3)/C38, IF($B$57=0,(C3-B3)/C38, IF($B$57=2,(E3-D3)/C38, IF($B$57=3,(F3-E3)/C38,(D3-C3)/C38))))`. With the default "No", year 1's reinvestment equals the revenue increment from year 1 to **year 2** — money spent now, revenue next year. Allowed lags are 0, 1, 2 or 3 years (`Answer keys!J2:J5` = 0,1,2,3).

His comment on the lag cell (`B56`) explains the motivation, and names factories and R&D:

> "The default in the spreadsheet is to assume that reinvestment in a year creates growth in the same year. That may work in service businesses or for companies that grow through acquisitions, but **in some businesses, there will be a lag between when you invest (in a new factory or R&D) and when you see revenue growth.** Enter yes and the following inputs."

*(Caveat, flagged honestly: the comment's first sentence says the default is contemporaneous, while the on-sheet text at `A55` and the formula both implement a one-year lag as the default. The comment appears to be stale from the pre-2023 version. The formula is the authority. **Confidence: high** on what the formula does, **medium** on which he intends to call "the default".)*

**What he actually set, company by company** (verified in S8 by reading `Input sheet` `B56/B57` or `B67/B68`):

| Valuation | Lag override | Lag used |
|---|---|---|
| Alphabet, Microsoft, Amazon, Meta, Apple — Feb 2024 | "No" | **1 year** (default) |
| NVIDIA — Jun 2023 (S3), Feb 2024 | "No" | **1 year** (default; the cell holds 2 but is inactive) |
| **NVIDIA — Sep 2024** (`Nvidia2024.xlsx`) | **"Yes"** | **3 years** (`B68`=3) |
| **NVIDIA — Jan 2025** (`NvidiaJan2025.xlsx`) | **"Yes"** | **3 years** (`B68`=3) |

The three-year lag is the strongest single piece of evidence on this question: for the company at the centre of the AI capital-spending cycle he moved the lag to its maximum, so that money spent in year 1 buys the revenue increment of **year 4** (arithmetic check in `NvidiaJan2025.xlsx`: year-1 reinvestment 4,386.4 = (Rev4 84,073.0 − Rev3 73,106.9)/2.5).

### 3c. His explicit instruction for a company that has already spent ahead of its growth

Cell comment on `Input sheet!B31`, the years 1-5 sales-to-capital input (S1) — this is him telling you what to do with a firm whose capacity is already built:

> "You are probably wondering what this is but it is how I compute how much you are going to reinvest to keep your business growing in future years. The higher you set this number, the more efficiently you are growing and the higher the value of your growth. Again, look at your company's current number (check on the right). Look at the industry averages as well in the worksheet. **(If your company has already invested for the growth for the next few years, this number can be set to a high value for the first five years, to reflect the fact that you don't have to reinvest as much. (Also check the option at the end of the spreadsheet, to allow for a lag between reinvestment and growth)**"

And the `Diagnostics` sheet, "Step 4: Check how much you are reinvesting", asks exactly this question (S1 `Diagnostics!G16:G18`):

> "1. is the growth that you are forecasting bounce-back growth or new growth?
> 2. **How much excess capacity do you have to service near term growth?**
> 3. Does investment efficiency in this business change as companies get bigger?"

So his two levers for the capex-ahead-of-revenue problem are (i) a **high years-1-5 sales-to-capital** ratio, and (ii) the **reinvestment lag**. Neither of them is "use gross capex minus depreciation".

**Confidence: high.**

### 3c-bis. A leftover artifact inside the shipped spreadsheet

The Feb-2026 `fcffsimpleginzu.xlsx` he distributes still carries his own Amazon story text on the `Stories to Numbers` sheet (S1 `A2`, `A3`), which is a direct statement of how he frames a capital-hungry platform:

> "The Disruption Platform Rolls on"
> "Amazon continues on its transformation from online retailer to disruption platform, willling [sic] to enter any business that it perceives as inefficiently run, and changing it. **Along the way, it will invest large amounts of capital and wait for long periods to attain profitability.**"

The accompanying `G9:G14` story links read: "Disruption platform in multiple businesses" (revenue growth), "Margins improve, aided by cloud business & continued economies of scale" (margin), "Global/US marginal tax rate over time" (tax), "Maintained at Amazon's current level" (sales-to-capital), "**Strong competitive edges**" (return on capital), "Cost of capital close to median company" (WACC). Note in particular that the return-on-capital-in-perpetuity input is justified by "strong competitive edges" — i.e. he overrides the ROIC = WACC default for this kind of company. (Confidence: high that the text is in the file; medium on the vintage of the underlying Amazon valuation, which is undated.)

### 3c-ter. What he actually wrote about the 2024-2026 hyperscaler AI capex

He has written a great deal about the *size* of the AI capex and about whether it will earn its cost of capital, and one passage that speaks directly to how it should enter a valuation. All verified against the cached post text.

**The valuation principle — this is the closest he comes to a direct answer** (S9, "AI's Bar Mitzvah Moment: From Hype & Hope to Business Questions!", 20 Aug 2026, https://aswathdamodaran.blogspot.com/2026/08/ais-bar-mitzvah-moment-from-hype-hope.html), in his list of what separates AI winners from losers:

> "**Investment needed to deliver growth**: While AI companies are more capital intensive than their tech counterparts, the additional reinvestment needed to deliver value can be altered by investments already made by a company. **Companies that have built capacity in advance of growth will be worth more than companies that will have to reinvest contemporaneously to deliver growth**, and companies that find ways to invest more efficiently will also have higher value. It is interesting that starting with Deepseek, China seems to be trying the latter path to AI dominance, using less expensive (and less powerful) AI chips and not investing as much in mega data centers…"

That is the economic content of the two spreadsheet levers in 3b/3c: capacity already built = higher near-term sales-to-capital and/or a longer reinvestment lag = higher value.

**On the scale, and his verdict on it** (S9, "Data Update 7 for 2026: Debt and Taxes", 20 Feb 2026, https://aswathdamodaran.blogspot.com/2026/02/data-update-7-for-2026-debt-and-taxes.html):

> "**The shift at these firms from capital-light to capital-intensive models over this period has been staggering, with the collective investment in 2025 alone hitting $400 billion, with guidance suggesting that they are only getting started.**"
> "Going back to investment first principles, you can debate whether these companies can expect to generate positive net present value from their AI investments, and **I have argued in earlier posts that it is very likely that they are collectively over investing**, with **over confidence and a fear of being left behind driving their both corporate investments and investor pricing**, in keeping what you would expect when there is a big market delusion."
> "For many of the big tech companies, much of that capital has come from their existing businesses which are cash machines, **although the AI cap ex will deplete the free cash flows available to return to shareholders.**"
> "**I am hard pressed to think of too many AI investments that have these near-term payoffs.**"

And (S9, "AI's Bar Mitzvah Moment", 20 Aug 2026):
> "Cumulatively, *the total investment from just these companies amount to $1.7 trillion*, over the last few years, and their guidance suggests that they are not done, with trillions of dollars in AI cap ex commitments in the next three to four years. You can see why I use the analogy of a factory, and argue that **AI has built the most expensive factory in history**…"

**How he converts a capex surge into a DCF input — verbatim** (S9, "Revisiting the SpaceX Valuation: A Post-Prospectus Update!", 4 Jun 2026, https://aswathdamodaran.blogspot.com/2026/06/a-weeks-ago-i-assessed-value-of-spacex.html):

> "Story takeaway: Given that SpaceX is continuing to invest substantial amounts in its space launch and connectivity businesses, **I will increase reinvestment in the near term (years 1-5) by lowering how much they will generate as additional revenues for every additional dollar of capital invested (lower sales to capital ratios).** With AI, where I was already assuming that reinvestment would be large (with a low sales to capital ratio), the tripling of target revenues will result in a surge in reinvestment to generate the higher sales."

Note the direction: a capex surge is expressed as a **lower** sales-to-capital ratio in years 1-5, and he uses the years-1-5 / years-6-10 split to let capital intensity ease as the business scales — in that SpaceX file (S8 `SpaceX2026IPOUpdated.xlsx`) the sales-to-capital inputs are per business: Launch/Space 3.00, Starlink/Connectivity 3.00, **xAI 1.50**, Other 5.00, with margin convergence set to **year 10** (`Input sheet!B34`=10) rather than the usual 5.

**What is NOT there.** He does **not** write a capex-minus-depreciation forecast anywhere; that construct appears only when he measures history (e.g. the chart in the same SpaceX post is titled "SpaceX: Capital expenditures, net of depreciation, by business", and his FCFE definition in "Data Update 8 for 2026" is "adding back depreciation … and then netting out capital expenditures and changes in working capital"). And **not found**: any post in which he discusses Alphabet's, Microsoft's, Amazon's or Meta's capex-versus-depreciation gap as a *valuation input*, or any Alphabet DCF published after 1 Feb 2024.

### 3d. His most recent Alphabet valuation — the actual inputs

**There is exactly one Alphabet DCF on his blog in 2023-2026: `Google2024.xlsx`, valuation date 1 February 2024**, linked from "The Seven Samurai: How Big Tech Rescued the Market in 2023!" (8 Feb 2024, https://aswathdamodaran.blogspot.com/2024/02/the-seven-samurai-how-big-tech-rescued.html). Probes for `Google2025/2026`, `Alphabet2024/2025/2026`, `GoogleJan2025/2026`, `GoogleAntitrust`, `MagSeven2025/2026` all returned HTTP 404. The Oct 2024 antitrust post ("Breaking up Big Tech: Cui Bono?", https://aswathdamodaran.blogspot.com/2024/10/breaking-up-big-tech-cui-bono.html) contains **no DCF**. Every cell below I read myself from `/tmp/damo/web/Google2024.xlsx`.

| Input | Value | Cell |
|---|---|---|
| Valuation date | 1 Feb 2024 | `Input sheet!B3` |
| Base revenues / EBIT (TTM, R&D capitalized) | $307,394m / $88,226m reported → $99,057m adjusted, margin 32.22% | `B11`, `B12`, `B16`="Yes" |
| **Revenue growth, year 1** | **8.00%** | `B26` |
| **Revenue growth, years 2-5 (CAGR)** | **8.00%** | `B28` |
| Growth, years 6-10 | linear glide 7.22% → 6.43% → 5.65% → 4.86% → **4.08%** | `Valuation output!H2:L2` |
| Operating margin, year 1 | 32.00% | `B27` |
| **Target pre-tax operating margin** | **30.00%** | `B29` |
| **Year target margin reached** | **year 5** (32.00 → 31.20 → 30.80 → 30.40 → 30.00) | `B30`=5; `Valuation output!C4:G4` |
| **Sales-to-capital, years 1-5** | **1.20** | `B31` |
| **Sales-to-capital, years 6-10** | **1.20** (no switch) | `B32` |
| Reinvestment lag | **1 year (default, not overridden)** | `B56`="No" |
| Risk-free rate / terminal growth | 4.08% | `B34`; `Valuation output!M2` |
| Initial cost of capital | 8.84% | `B35` |
| **Stable cost of capital** | **8.00%** (override "Yes"; the default would have been 8.58%) | `B45`="Yes", `B46`=0.08 |
| **Stable ROIC** | **15.00%** (override "Yes") | `B48`="Yes", `B49`=0.15 |
| Effective / marginal tax rate | 13.9% → 25.0% by terminal year | `B23`, `B24`, `B59`="No" |
| Failure probability | 0% | `B51`="No" |

Implied: revenues year 10 $618,541m; ROIC year 10 **26.66%** (`Valuation output!L40`); marginal ROIC years 1-10 **20.28%** (`Diagnostics!C27`); terminal reinvestment rate 4.08%/15% = **27.2%**; value/share **$143.07** vs price $145 (`B33`, `B34`). *Caveat: the post's own table shows $138.14 vs $145.00; the currently hosted file does not reproduce the post's number exactly. Both are reported rather than one being chosen.*

For context, the sales-to-capital ratios he used across the Magnificent Seven in Feb 2024 (all with **no** years-1-5 / years-6-10 switch, and margin convergence in year 5): **Alphabet 1.20, Meta 1.50, Amazon 2.00, Microsoft 3.00, Apple 5.00, NVIDIA 1.15** (verified in S8). His published 5-year revenue CAGRs and target margins from the post's table: Alphabet 8.00%/30.00%, Amazon 12.00%/14.00%, Apple 7.50%/36.00%, Microsoft 15.00%/45.00%, Meta 12.00%/40.00%, NVIDIA 32.20%/40.00%, Tesla 31.10%/13.07%.

**Confidence: high** on all cell-level inputs; **high** that no later Alphabet DCF exists on his blog (two independent search methods agreed).

### 3e. Does he lengthen the growth period for such firms?

The horizon in the ginzu spreadsheet is fixed at 10 explicit years, so "lengthening" is not available as an input; what varies is how long growth and excess returns are allowed to persist inside those 10 years (the years 2-5 growth rate, the margin convergence year, and the stable ROIC override). In the book (S4, Ch. 12) his three-factor rule does push toward the long end for a firm with protected, expanding markets — Amgen gets ten years — and his transition guidance says a company with very high operating-income growth needs a **transition phase** rather than an abrupt step (see Q4). **A statement of the specific form "a short horizon undervalues a firm investing heavily now for later payoff" was not found** — not in the cached chapters, not in the spreadsheet, and not in any of the 64 posts from 2024-2026. The horizon in his model is fixed at 10 years and he never varies it; the levers he varies are the margin convergence year (5 for the Mag 7, **10** for SpaceX), the years-1-5 vs years-6-10 sales-to-capital split, and the reinvestment lag. The nearest statement, and it concerns the *investor's* wait rather than the model's horizon (S9, "Trillion Dollar Market Caps: Fairy Tale Pricing or Business Marvels?", 3 Dec 2025, https://aswathdamodaran.blogspot.com/2025/12/trillion-dollar-market-caps-fairy-tale.html):

> "Since Nvidia is still growing and you may need to wait, as equity investors, to get your cash flows, **this breakeven number will get larger, the longer you have to wait** and the lower the cash yield that equity investors receive during the growth period."

His written view on the 15-20 year horizon question is in the 2023 Tesla post quoted in Q1a-bis: "ten years is already at the 90th percentile of growth periods … using 20-25 years of growth risks making your company a unicorn."
 The closest thing is the mirror-image warning in S5 (Ch. 14) discussed in Q4, and the diagnostic in S5: "Growth Period (High growth + transition) is too long → Use a shorter growth period" (given as a cause of an *over*valuation), which implies the reverse but does not state it.

---

## Q4. The "year-6 cliff": does he warn about it, and what is the remedy?

### 4a. The warning he does give, verbatim (S5, Ch. 14, "Calculating the terminal price" + Illustration 14.3)

He warns about a one-step transition producing a **wrong terminal cash flow**, and the direction he emphasises is *understatement* — caused by carrying high-growth-phase capital intensity into perpetuity:

> "In addition, the assumptions made to derive the free cashflow to equity after the terminal year have to be consistent with the assumption of stability. For instance, **while capital spending may be much greater than depreciation in the initial high growth phase, the difference should narrow as the firm enters its stable growth phase.** We can use the two approaches described for the stable growth model – industry average capital expenditure requirements or the fundamental growth equation (equity reinvestment rate = g/ROE) to make this estimate."

Then the worked example (Illustration 14.3: "Capital Expenditure, Depreciation and Growth Rates"), 20% growth for five years then 5%:

> "If we use the infinite growth rate model, but fail to adjust the imbalance between capital expenditures and depreciation, the free cashflow to equity in the terminal year is --
> Free cashflow to equity in year 6 = 3.73 * 1.05 = $3.92
> This free cashflow to equity can then be used to compute the value per share at the end of year 5, **but it will understate the true value. There are two ways in which you can adjust for this:**
> 1. Adjust capital expenditures in year 6 to reflect industry average capital expenditure needs …
> 2. Estimate the equity reinvestment rate in year 6, based upon expected growth and the firm's return on equity. For instance, if we assume that this firm's return on equity will be 15% in stable growth, the equity reinvestment rate would need to be: Equity reinvestment rate = g/ROE = 5%/15% = 33.33%"

His diagnostic checklists (S5, Ch. 14, "What is wrong with this valuation?") name the same failure explicitly:

> "If you get a extremely low value from the 2-stage FCFE, the likely culprits are … **capital expenditures are significantly higher than depreciation in stable growth phase → Reduce the difference for stable growth period** … **the use of the 2-stage model when the 3-stage model is more appropriate → Use a three-stage model**"
> "If you get a extremely low value from the 3-stage FCFE … **capital expenditures are significantly higher than depreciation in stable growth phase → Reduce net cap ex in stable growth; Cap Ex grows slower than depreciation during transition period**"

### 4b. The prescribed remedy: a transition (fade) period (S4, Ch. 12, "III. The Transition to Stable Growth")

> "Once you have decided that a firm will be in stable growth at a point in time in the future, you have to consider how the firm will change as it approaches stable growth. There are three distinct scenarios. In the first, the firm will be maintain its high growth rate for a period of time and then become a stable growth firm abruptly; this is a two-stage model. In the second, the firm will maintain its high growth rate for a period and then have a transition period where its characteristics change gradually towards stable growth levels; this is a three stage model. In the third, the firm's characteristics change each year from the initial period to the stable growth period; this can be considered an n-stage model.
> Which of these three scenarios gets chosen depends upon the firm being valued. **Since the firm goes in one year from high growth to stable growth in the two-stage model, this model is more appropriate for firms with moderate growth rates, where the shift will not be too dramatic. For firms with very high growth rates in operating income, a transition phase (in a 2 stage model) allows for a gradual adjustment not just of growth rates but also of risk characteristics, returns on capital and reinvestment rates towards stable growth levels.** For very young firms or for firms with negative operating margins, allowing for changes in each year (in an n-stage model) is prudent."

And the applied version (Illustration 12.4):
> "For Procter & Gamble, stepping down to stable growth at the end of 5 years is not likely to be as abrupt a change as it is for the other two firms and we will use a two-stage model – growth of 13.58% for 5 years and 5% thereafter. **For both Coca Cola and Amgen, we will allow for a transition phase between years 6 and 10 where the inputs will change gradually from high growth to stable growth levels.**"

The mechanics of that transition are stated as linear (S6, Ch. 15, Amgen and Embraer valuations, identical wording in both):
> "**During the transition period, we adjust growth, reinvestment rate and the cost of capital from high growth levels to stable growth levels in linear increments.**"

That is exactly the years-6-10 fade hard-wired into fcffsimpleginzu (Q1b). He also notes a transition can be needed even when growth is already low: "Consider, for instance, a firm whose operating income is growing at 4% a year but whose current return on capital is 20% and whose beta is 1.5. **You would still need a transition period where the return on capital declined to more sustainable levels (say 12%) and the beta moved towards one.**" (S4, Ch. 12)

### 4c. Does he say the terminal cash flow ends up *below* the last explicit year?

**A verbatim warning in that exact form was not found** — not in the cached book chapters, not in the spreadsheet, and not in any of the 64 blog posts published 2024-01-01 → 2026-09-08 (all enumerated from his sitemap and grepped). He also never uses the phrase "transition period" in those posts. His written warning runs the other way (4a: a one-step transition *understates* value when high capex is carried forward).

However, **it demonstrably happens in his own models**, and it is caused by the one input he does *not* fade — the return on capital, which steps in a single move at the terminal year and therefore steps the reinvestment rate (g ÷ ROIC). Computed from his workbooks:

I computed this for **every** one of his published DCFs I could open. It happens in all of them, without exception. Columns are `L8/L7` (year-10 reinvestment as % of EBIT(1−t)), `M8/M7` (terminal, which always equals g ÷ stable ROIC), `L9` and `M9`.

| His valuation | Year-10 reinvestment rate | Terminal reinvestment rate (= g ÷ stable ROIC) | Year-10 FCFF | Terminal FCFF | Change |
|---|---|---|---|---|---|
| **Alphabet, Feb 2024** | **15.1%** | **27.2%** | 113,510 | 101,317 | **−10.7%** |
| Microsoft, Feb 2024 | 4.0% | 27.2% | 221,956 | 175,238 | **−21.0%** |
| Meta, Feb 2024 | 9.1% | 27.2% | 91,923 | 76,595 | **−16.7%** |
| Amazon, Feb 2024 | 19.4% | 27.2% | 121,461 | 114,224 | **−6.0%** |
| Apple, Feb 2024 | 3.0% | 27.2% | 188,988 | 147,660 | **−21.9%** |
| Alphabet, Mar 2018 (S2) | 6.3% | 22.9% (= 2.75%/12%) | 52,223 | 44,146 | **−15.5%** |
| NVIDIA, Jun 2023 — base / AI / auto segments (S3) | 10.4% | 18.0% (= 3.6%/20%) | 11,197 / 52,396 / 8,061 | 10,621 / 49,697 / 7,646 | **−5.2%** each |
| Coca-Cola, Sep 2024 | 9.5% | 16.9% | 15,741 | 14,978 | −4.9% |
| Nike, Sep 2024 | 10.7% | 18.6% | 9,024 | 8,534 | −5.4% |
| Starbucks, Sep 2024 | 16.4% | 31.0% | 6,629 | 5,672 | −14.4% |
| Disney, Sep 2023 | 20.9% | 33.3% | 20,014 | 17,537 | −12.4% |
| Netflix, Sep 2023 (stable ROIC = WACC) | 8.9% | 44.4% | 13,329 | 8,453 | **−36.6%** |
| Intel, Sep 2024 (stable ROIC = WACC) | 12.5% | 47.5% | 15,182 | 9,442 | **−37.8%** |
| fcffsimpleginzu shipped example (S1) | 25.1% | 52.0% | 2,756 | 1,855 | **−32.7%** |

Two things fall out of this table. First, **the notch is universal in his own work** and runs from −5% to −38%. Second, **its size is governed almost entirely by the stable-ROIC choice**: where he overrode ROIC upward (Mag 7 at 15-20%) the notch is 6-22%; where he left the ROIC = WACC default in place (Intel, Netflix, and the shipped template) the terminal reinvestment rate roughly doubles and the notch is 33-38%.

So the drop is real but small, and it is small *because* of the five-year fade: by year 10 the growth rate, tax rate and cost of capital have all already arrived at their stable values, so only the ROIC/reinvestment step is left to absorb. The cliff is not eliminated — it is spread over five years and reduced to a 5-15% notch.

### 4c-bis. He does label years 6-10 as the transition — in the spreadsheet, not in prose

The `Stories to Numbers` sheet of every version of his model lays the inputs out as **"Base year | Next year | Years 2-5 | Years 6-10 | After year 10"** (S1 `B8:F8`), and the years-6-10 cells for revenue growth, tax rate and cost of capital literally read **"Changes to"**, and the margin cell reads **"Moves to"** (S1 `E9`, `D10`, `E11`). That is his own presentation of years 6-10 as the transition band between high growth and stable growth, matching the Ch. 12 three-stage prescription exactly.

### 4d. Important nuance: in the *book* method he fades the reinvestment rate itself, so there is no step at all

His Amgen FCFF table (S6, Ch. 15, Table 15.6) shows the transition period doing exactly the job of removing the notch — the **reinvestment rate** is one of the things faded in linear increments, so that by year 10 it already equals the stable rate:

| Year | Expected growth | EBIT(1−t) | Reinvestment rate | FCFF | Cost of capital |
|---|---|---|---|---|---|
| 1-5 | 13.08% | $1,644 → $2,688 | 56.27% | $719 → $1,176 | 10.76% |
| 6 | 11.46% | $2,996 | 50.01% | $1,498 | 10.38% |
| 7 | 9.85% | $3,291 | 43.76% | $1,851 | 10.00% |
| 8 | 8.23% | $3,562 | 37.51% | $2,226 | 9.62% |
| 9 | 6.62% | $3,798 | 31.25% | $2,611 | 9.24% |
| 10 | 5.00% | $3,988 | **25.00%** (= stable, = 5%/20%) | $2,991 | **8.86%** (= stable) |
| Terminal (11) | 5.00% | $4,188 | 25.00% | **$3,140** | 8.86% |

Terminal FCFF ($3,140) is *above* year 10 ($2,991) — a smooth 5% step-up, no notch, because growth, reinvestment rate *and* cost of capital all reach their stable values by year 10.

The ginzu spreadsheet does **not** do this: there, years 1-10 reinvestment is driven by the sales-to-capital ratio and only the terminal year uses g ÷ ROIC (Q3a), so the reinvestment rate jumps once at the terminal year — which is precisely why the small notch appears in the Alphabet 2018 and NVIDIA 2023 files. **Confidence: high** (both the book table and the workbook formulas are explicit). If you want to reproduce his book behaviour, you have to choose a years-6-10 sales-to-capital ratio (`Input sheet!B32`) that makes the year-10 reinvestment rate land on g ÷ stable ROIC.

Related quote for Q1 (S6, Ch. 15, Embraer, "Rationale for using Model"):
> "Embraer has done exceptionally well in the last few years though it operates in a mature business with strong competition from giants such as Boeing and Airbus. **We believe that it can sustain growth for a long period (10 years) and that there will be a transition to stable growth in the second half of this growth period.**"

**Confidence: high** on the transition-period prescription (direct quotes) and on the computed table; **medium/low** on the specific claim that he has ever written the sentence "the terminal cash flow will be below the final explicit year" — I did not find it.

---

## What this implies for a 5-year model of a company spending 45% of revenue on capex

On his own evidence, a five-year explicit period with a one-step jump to stable inputs is the structure he reserves for the *opposite* kind of company — Procter & Gamble, "where the shift will not be too dramatic" (S4, Ch. 12). A firm putting 45% of revenue into capex is, in his taxonomy, the firm with "very high growth rates in operating income" for which "a transition phase … allows for a gradual adjustment not just of growth rates but also of risk characteristics, returns on capital and reinvestment rates towards stable growth levels", or even the n-stage case. His own tool gives such a firm **ten** explicit years with a five-year linear fade of growth, tax rate and cost of capital, a margin that converges on a chosen year, a **second** sales-to-capital ratio for years 6-10, and — since 2023 — a **default one-year lag** between reinvestment and the revenue it buys, extendable to three years. None of those five cushions exists in a flat 5-year model.

The arithmetic of why this matters is severe, and — this is the part that inverts the usual worry — it runs in the direction of *over*statement, not the −5% to −38% notch seen in every one of his own 10-year files. The direction of the year-6 step is set by whether the explicit-period reinvestment rate sits above or below g ÷ stable ROIC. In his models growth has already faded to the terminal rate by year 10, so explicit reinvestment is *below* g ÷ ROIC and the terminal cash flow drops. In a flat 5-year model of a 45%-of-revenue-capex firm, explicit reinvestment is far *above* g ÷ ROIC, so the terminal cash flow leaps. Take revenue 100 growing 20%, a 30% EBIT margin, a 20% tax rate, capex at 45% of revenue and depreciation at 15% (net reinvestment 30% of revenue, implying a sales-to-capital ratio of only 0.56). Reinvestment then runs at **125% of EBIT(1−t)** in every one of years 1-5 and free cash flow is negative throughout (−7.2 rising to −14.9 by year 5). Step straight to stable growth of 4.5% with ROIC set equal to a 9% cost of capital and the terminal reinvestment rate collapses to g ÷ ROIC = **50%**: year-6 free cash flow leaps from −14.9 to **+31.2**, a +46 swing with no economic event behind it, and the discounted terminal value (451) is **110% of total value** because the explicit period contributes −40. The entire valuation is then one number — the year-6 reinvestment rate — and it is a number that appears nowhere in the five years you actually forecast. Raise stable ROIC from 9% to 12/15/20% (all within the range he himself has used: +4 pts for Alphabet, +11 pts for NVIDIA and Amgen) and total value goes to 1.27× / 1.44× / 1.60× — so a single unfaded input swings the answer by 60%.

The practical conclusions his own material supports: (1) if the horizon must stay at five years, insert his fade explicitly — carry growth, tax rate, cost of capital *and* the reinvestment rate down to stable levels **by** the last explicit year, exactly as his Amgen table does (year 10 reinvestment rate = g ÷ stable ROIC), so no input steps at the terminal boundary; (2) do not compute forecast reinvestment as gross capex minus depreciation — he uses Δrevenue ÷ sales-to-capital, and for a firm that has already built capacity he says to *raise* the near-term sales-to-capital ratio and/or turn on the reinvestment lag ("If your company has already invested for the growth for the next few years, this number can be set to a high value for the first five years"); (3) treat stable ROIC as the load-bearing input it is, justify any excess over the cost of capital by a durable, nameable advantage ("moving them to or towards industry averages in stable growth seems like a reasonable compromise"), and report the value at ROIC = WACC alongside it, which is what his own spreadsheet default gives you; and (4) run his Diagnostics questions — the market-share implied by year-10 revenue, "How much excess capacity do you have to service near term growth?", and "Are you comfortable with your return on capital in year 10?"

One direct precedent worth naming: the closest analogue in his own published work to a 45%-of-revenue-capex company is NVIDIA in Sep 2024 and Jan 2025, and for those two valuations he (a) kept the horizon at ten years, (b) set sales-to-capital to 2.5 in both the years-1-5 and years-6-10 blocks, (c) let the margin converge to target only in year 5, (d) set stable ROIC at 20% against a stable cost of capital of ~8.5%, and (e) **moved the reinvestment lag to its maximum of three years** so that year-1 spending buys year-4 revenue. His stated reason for caring about exactly this, from the Aug 2026 AI post: "Companies that have built capacity in advance of growth will be worth more than companies that will have to reinvest contemporaneously to deliver growth."

---

## A note on the working tree

I wrote nothing into `/home/ubuntu/finance`; all output went to `/tmp/damo/`. For the record, at the end of this work `git status` showed six modified files under `tools/valuation/` (`analysis.py`, `app_core.py`, `engine.py`, `render.py`, `render_assumptions.py`, `schema.py`, +453/−75). Those are not mine — the tree was clean when I started and the diffs contain comments citing this research ("Damodaran's own choices were 4 points for Alphabet 2018 and 11.5 for Nvidia 2023"), so they appear to come from another worker in the same session. I left them untouched.

