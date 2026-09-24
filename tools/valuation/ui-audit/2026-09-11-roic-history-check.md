# Independent historical ROIC evidence check — 2026-09-11

**Verdict: PASS for the scoped evidence check.** No material numerical errors or unsupported capital components found in MU, AAOI or SNDK. No sidecar or assumption edits were needed. This is a source and arithmetic review, not a visual UI audit.

## Scope and method

Independently reviewed the three historical evidence sidecars against cached original filing passages. Spot-checked each company's latest annual operating income, effective tax treatment, opening balance date, debt, equity, cash and lease components. Recomputed every populated opening-capital total across all three files and exercised `load_return_history` on each file. The historical return is the stated tax-adjusted book-capital proxy, with beginning-of-year capital; it is not a company-reported ROIC or a return on the next investment.

All 15 annual rows load, all source paths exist, all period-end dates precede their evidence cutoff, and all three evidence cutoffs match the corresponding assumption-file cutoff. Each company has three calculable annual returns and two explicitly unavailable opening-capital observations. Loss rows preserve reported operating loss without an assumed tax benefit. These checks do not independently establish complete source support for every older income-statement figure; the original-passage spot-check focused on the latest year and its opening capital.

## Source checks

| Company / latest year | Operating income, USD millions | Tax treatment | Opening capital, USD millions | App-calculated historical return |
|---|---:|---|---:|---:|
| MU FY2025 | 9,770 | Reported 11.6% effective rate | 51,103 at August 29, 2024 | 16.90% |
| AAOI FY2025 | -54.602 | No assumed benefit on operating loss | 333.285 at December 31, 2024 | -16.38% |
| SNDK FY2026 | 12,389 | Reported rounded 12% effective rate | 9,803 at June 27, 2025 | 111.21% |

**MU.** FY2025 operating income 9,770 and effective tax 11.6% match Item 7 and the consolidated income statement. The August 29, 2024 balance-sheet column has equity 45,131, current debt 431, long-term debt 12,966, cash 7,041 and short-term investments 1,065. Note 9 supplies current operating leases 71; the balance sheet supplies noncurrent operating leases 610. Thus opening capital is 45,131 + 431 + 12,966 + 71 + 610 - 7,041 - 1,065 = 51,103. Note 12's debt table already includes finance leases, so the sidecar correctly avoids adding them again. [10-K FY2025, Item 7; Item 8; Notes 9 and 12](../../../companies/MU/sources/FY2026-Q3/10-K-FY2025.txt)

**AAOI.** The statements report USD thousands; the sidecar correctly converts each amount to millions. FY2025 operating loss is 54,602 thousand. The December 31, 2024 balance sheet supplies equity 229,112, current notes/debt 22,370, convertible notes 134,497, long-term debt 4,313, current operating leases 1,380, noncurrent operating leases 9,041 and cash 67,428 thousand. The resulting capital is 333.285 million. The separately reported restricted cash is retained. Note K explicitly identifies vendor bank-acceptance notes as carrying zero interest; their exclusion is consistent with the sidecar's stated interest-bearing-debt definition and is disclosed. The balance-sheet amounts are used consistently despite one-thousand-dollar differences in the debt note. FY2025's reported income-tax benefit of 8,476 thousand does not reduce the operating loss in the comparison, matching the model's no-loss-benefit convention. [10-K FY2025, Item 8; Notes E and K](../../../companies/AAOI/sources/2026-Q2/10-K-FY2025.txt)

**SNDK.** FY2026 operating income 12,389 and the rounded 12% effective rate match the consolidated statements and income-tax note. The June 27, 2025 comparative balance sheet supplies equity 9,216, current debt 20, long-term debt 1,829 and cash 1,481. The lease note supplies 26 current and 193 noncurrent operating leases. Opening capital is therefore 9,216 + 20 + 1,829 + 26 + 193 - 1,481 = 9,803. Goodwill of 4,999 remains in the reported opening assets. The resulting return above 100% is supported by these inputs, not a percent-scaling error. Separation, prior goodwill impairment and the Flash Ventures structure limit its interpretation, as disclosed in the sidecar. [10-K FY2026, Item 8; lease and income-tax notes](../../../companies/SNDK/sources/FY2026-Q4/10-K-FY2026.txt), [10-K FY2025, Notes 1 and 10](../../../companies/SNDK/sources/FY2026-Q4/10-K-FY2025.txt)

## Interpretation limits

Effective corporate income-tax rates apply to total pretax income rather than solely operating profit; applying them to EBIT is a proxy. Operating lease liabilities enter capital while the numerator remains reported operating income. The displayed comparison should retain the root implementation's proxy label and methodology explanation. Missing opening balances must remain unavailable. No normalized taxes, goodwill add-backs, replacement year-end denominators or forecast-assumption changes were introduced by this check.

## Evidence versions checked

SHA-256 of the sidecar bytes checked:

- MU: `8d409f52e6b9433e19f80e12c4f34c586e499e8db1b901acb834413788f495b7`
- AAOI: `43e1e5a541d3da5daceef4672826874a44e0d7c5f95569fa3cb9319d9bf4e6ac`
- SNDK: `b383f68c782931f0407b9e94a04eb4536dcc38a05d03813eb9203fa822270db4`

## Additional root checks: GOOGL and MRVL

The builder independently checked the other agent’s latest-year evidence against original cached filings and reconciled every populated capital-component sum. GOOGL FY2025 operating income 129,039 and effective tax16.8% match the FY2025 10-K income statement and tax table. Opening equity325,084 + notes debt10,883 + current notes999 + commercial paper2,300 + finance leases1,677 + operating leases14,578 − cash/short-term securities95,657 =259,864, giving41.31%. Commercial paper retains the filing’s rounded precision. Source: `companies/GOOGL/sources/2026-Q1/10-K-FY2025.txt`, Item8, Notes4/6 and Income Taxes. MRVL FY2026 operating income1,322.9 and effective tax12.4% match its FY2026 10-K; opening equity13,427.0 + debt129.5+3,934.3 + leases48.3+231.0 − cash948.3 =16,821.8, giving6.89%. Source: `companies/MRVL/sources/FY2027-Q1/10-K-FY2026.txt`, Item8, Notes12/15. Earlier populated capital sums also reconcile. These are builder checks, separate from the independent review above.
