# AVGO rendering — independent app audit

**PASS for rendering and review interactions.** Audited September 18, 2026 Pacific / September 19 UTC by a separate audit agent. AVGO's financial draft remains **BLOCKED**; this audit neither changes assumptions nor adds a financial review pass.

## Target and version

The target was Broadcom Inc. (AVGO), FY2026-Q2, information through June 9, 2026, drafted September 18. Original and loaded input were the same active file:

`/Users/erichuang/Documents/Code/research-and-valuation/companies/AVGO/valuation/assumptions.yaml`

SHA-256 before and after the audit: `02ed91bdefb6256c38b600829a015ae2ccc686c646724412aeae1442bc77ea6a`. There was no staging or promotion. The builder confirmed that the fresh processes used this repository as their default root, without a `VALUATION_REPO_ROOT` override. The auditor independently selected AVGO, checked the displayed quarter/date and distinctive inputs, and verified the file hash.

Git HEAD was `06f2662207ea5e50d27a8f8d170e7843534dea16`, with uncommitted app changes. File hashes below identify the actual version; HEAD alone does not.

| File under `tools/valuation/` | SHA-256 |
|---|---|
| `app.py` | `2695b2a2afaa0410723261e0c4f0c6c2475d67d897075812fe81c7e00394362e` |
| `app_core.py` | `70e0701c7951ca1899b41ee61d1060846486b2e067894aa092241e75656bc42b` |
| `app_pages.py` | `6310e059c721f00bed34b921afff0e1128720496c0ceeb0a7c7c3bab37112e14` |
| `app_workspace.py` | `677050f9ece20f875ffed000b8b08faa07e078de0e9e3975701b8de7a8cb7b27` |
| `app_sources.py` | `85fa53b93c17a67fe771c22778965a33902ec4103c0cb263355bd87a9c27f8cc` |
| `app_notes.py` | `eef9396b6cf897e28e78978eb08bfecc57f93bf67e4d49d419f666f0c4867dce` |
| `app_scenarios.py` | `1cdab2dd576eb789caf44c4593085dca5eb7b2ac3e1834d87ec439174fe8bef1` |
| `app_simulation.py` | `8d148824e7dcbc64f9f7ceba92b41647b7b4db15dda631618998129f99b498da` |
| `app_launcher.py` | `7eb4bc2f95ad9e5deede64bf3852b55707fdd2b8f12796a288cec32d0c5ce7b8` |

## Method and coverage

The auditor operated headless Chromium through the Playwright CLI in its own `avgo-final-audit` session at 1280 by 800 pixels. The final full walk used the fresh review-only process on port 8537, started at 23:03:47 Pacific. All fifteen destinations were reopened and captured after that restart:

| Destination | Result and final screenshot |
|---|---|
| Overview | PASS — `page-01-overview.png` |
| Scenarios | PASS — `page-02-scenarios.png` |
| Revenue growth | PASS — `page-03-revenue.png` |
| Operating margin | PASS — `page-04-margin.png` |
| Reinvestment | PASS — `page-05-reinvestment.png` |
| Cost of capital | PASS — `page-06-cost-of-capital.png` |
| Terminal value | PASS — `page-07-terminal.png` |
| Taxes and weights | PASS — `page-08-taxes.png` |
| Source facts | PASS — `page-09-facts.png` |
| Valuation | PASS, explicitly deferred — `page-10-valuation.png` |
| Analysis | PASS, explicitly unavailable — `page-11-analysis.png` |
| Cash flow forecast | PASS, explicitly unavailable — `page-12-forecast.png` |
| Simulation | PASS, explicitly unavailable — `page-13-simulation.png` |
| Model checks | PASS, missing inputs and schema warnings visible — `page-14-checks.png` |
| Review & save | PASS — `page-15-review.png` |

All captures are in `output/playwright/avgo-app-2026-09-19/`. Final page screenshots and focused scroll positions were visually inspected. Headings, paragraphs, inputs, reasons and navigation remain readable at laptop width, without blank pages, Python exceptions, broken Markdown or obstructive layout. This was a targeted desktop audit, not every pixel of every long document or a mobile/accessibility certification.

## Interactions and incomplete-input behavior

- All four full narratives were read in the app. The management guidance disclosure and the base revenue working notes expanded correctly, including long prose and tables. Relevant scenario rendering modules and input bytes remained unchanged through the final restart. Focused captures: `scenarios-bear.png`, `scenarios-base.png`, `scenarios-bull.png`, `scenarios-management.png`, `scenarios-guidance-expanded.png`, and `revenue-notes.png`. Visible scenario tables had matching client/scroll widths at 1280 pixels.
- Source facts displayed both bridge unknowns as unavailable. Reinvestment retained empty years 6–10 and explained the unsupported capital needs beside the inputs; no zero or invented ratio replaced them. Focused captures: `source-bridge.png`, `source-reasons.png`, `reinvestment-base.png`.
- On the final process, the bear weight was changed from 25% to 26% in memory. Taxes and weights showed 26% and a 101% total warning. Review showed exactly one change, 25% to 26%. Reset restored 25/50/25, and the final Review page reported `Unsaved changes (0)`. `weight-edited.png`, `review-unsaved.png`, and `review-controls.png` record the flow. Back and Next were exercised between Scenarios and Revenue growth.
- The recorded `10-K FY2025` citation opened a separate cached-source tab identifying AVGO and `sources/FY2026-Q2/10-K-FY2025.txt`, retaining the original SEC link. It honestly stated that the citation had no exact passage locator. Searching `63,887` produced five highlighted matches; the original app tab remained intact. Captures: `source-10k.png` and `source-search.png`. A first attempt coincided with the planned server shutdown; the same source action succeeded after the final restart.
- Review-only mode displayed deferred-result notices throughout. Model checks showed the two shared bridge gaps, all four late-reinvestment gaps, and the existing terminal-premium warnings. Save was disabled when unchanged with an explanation; Write the report was disabled with a draft-review explanation. No Save, Write the report or Record in the repository action was invoked. No AVGO `valuation.md` was created.

## Normal-mode regression and limitations

The auditor independently checked the fresh regular app on port 8501 after its 23:03:51 Pacific restart. AVGO's Overview, Reinvestment, Model checks and Review & save rendered with the unchanged real draft and the app's fetched market inputs; no replacement market value was entered. The sticky panel now says that three inputs need attention for the selected case, with details on Model checks, rather than repeating every case's errors over the editing area. The panel remains compact while scrolling through the empty late-investment input and its reason. Captures: `normal-reinvestment.png`, `normal-reinvestment-base.png`, `normal-model-checks.png`, and `normal-review.png`.

The final browser sessions reported no console errors. Existing Streamlit theme/iframe feature warnings remained and did not prevent rendering. The builder reported 52 passing focused app tests after the final changes; that suite was not independently rerun by this UI auditor.

The missing corporate-investment balance, customer-lease backstop valuation and later funding assumptions still prevent an AVGO equity valuation. Rendering PASS does not resolve those financial gaps or change the original financial review verdict.
