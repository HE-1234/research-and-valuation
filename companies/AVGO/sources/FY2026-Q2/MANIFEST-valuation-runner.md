# AVGO valuation source additions — runner

Operating cutoff remains June 9, 2026; Q2 FY2026 ended May 3. Retrieved September 18, 2026. Text only is retained.

| File | Origin | Published / observation | Handling |
|---|---|---|---|
| apollo-platform-release-2026-06-09.txt | https://ir.apollo.com/news-events/press-releases/detail/630/broadcom-apollo-and-blackstone-establish-landmark | 2026-06-09 | HTML parsed to visible text with Python HTMLParser; navigation retained; platform release only is evidence. |
| apollo-financing-release-2026-06-09.txt | https://www.apollo.com/insights-news/pressreleases/2026/06/apollo-leads-35-billion-capital-solution-for-broadcom-ai-xpv-platform-in-partnership-with-blackstone-and-leading-global-banks-3308896 | 2026-06-09 | Same text extraction. |
| wsts-spring-2026.txt | https://www.wsts.org/esraCMS/extension/media/f/WST/7618/WSTS_FC-Release-2026-May.pdf | 2026-06-02 06:00 UTC, stated on p.1 | pdftotext -layout; original PDF used temporarily then removed. Industry forecast, not realized results or AVGO's addressable share. |
| sec-bridge-facts-precutoff.txt | https://data.sec.gov/api/xbrl/companyfacts/CIK0001730168.json | Only observations ending 2026-05-03 and filed by 2026-06-09 retained | Filtered standard-GAAP lease, investment, pension and minority tags; no relevant May 3 stock balance found. Cash-flow movements are not investment balances. |
| valuation-market-inputs.txt | Yahoo chart; FRED DGS10; cached Damodaran datasets, exact URLs in record | Price 2026-09-18; DGS10 2026-09-17; ERP 2026-09-01; industry 2026-01-05 | Current market inputs are separately dated under §18.8. |

Targeted transaction search: primary Apollo June 9 releases and the already-cached AVGO June 9 10-Q were inspected. They do not disclose a backstop fair value, exposure-by-year schedule, fee or recoveries. Search results also surfaced post-cutoff filings; those results were excluded from all model assumptions and no post-cutoff filing was cached. An unknown pre-cutoff term cannot be repaired with hindsight.

## Targeted analyst requests

| File | Original URL | Publication / observation | Purpose |
|---|---|---|---|
| fred-treasury-debt-proxy.txt | https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10 | Jan 6 and Jan 13, 2026: 4.18%; Sep 17, 2026: 4.94%; fetched Sep 18 | Same-tenor January 2036 coupon spread proxy: 4.95%-4.18%=0.77 percentage points, then current Treasury plus retained spread. This is a borrowing-cost estimate, not an observed current bond yield. |
| NVDA-release-FY2027-Q1.txt | https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2027 | Published 2026-05-20, quarter ended 2026-04-26; fetched Sep 18 | Current large AI-chip supplier scale only; not a mature-return benchmark. HTMLParser visible-text extraction. |
| NVDA-release-FY2026-Q4.txt | https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026 | Published 2026-02-25, year ended 2026-01-25; fetched Sep 18 | Annual scale and TTM reconstruction using current-quarter release; same text extraction. |

Rating-agency search results were inspected only to discover potential pre-cutoff borrowing evidence; no rating was used in the model. The selected spread proxy uses the existing January 2026 debt issue and the dated FRED observations above.
