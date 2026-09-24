# AVGO FY2026-Q2 — valuation app check

**App check: PASS. Financial draft: BLOCKED, unchanged.** Checked September 18, 2026 Pacific / September 19 UTC by an independent audit agent.

## Exact target

- Company: Broadcom Inc. / AVGO.
- Quarter and cutoff: FY2026-Q2, information through June 9, 2026; draft dated September 18, 2026. These dates were confirmed in the running app.
- Original input: `/Users/erichuang/Documents/Code/research-and-valuation/companies/AVGO/valuation/assumptions.yaml`.
- Loaded input: the same absolute path, under the default repository root. No staged candidate or promoted path was involved.
- Original and loaded SHA-256, before and after: `02ed91bdefb6256c38b600829a015ae2ccc686c646724412aeae1442bc77ea6a`.
- App revision: working tree based on `06f2662207ea5e50d27a8f8d170e7843534dea16`. Exact final module hashes and screenshots are recorded in the [independent app audit](../../../tools/valuation/ui-audit/2026-09-19-avgo-rendering.md).

## Checks performed

The final full walk used a fresh process on `http://localhost:8537/`, with `VALUATION_APP_REVIEW_ONLY=1`, headless Chromium and a 1280 by 800 viewport. It covered all fifteen destinations: Overview, Scenarios, Revenue growth, Operating margin, Reinvestment, Cost of capital, Terminal value, Taxes and weights, Source facts, Valuation, Analysis, Cash flow forecast, Simulation, Model checks, and Review & save.

The four narratives, scenario tables, reasons and long working notes rendered readably. Management guidance and working-note disclosures opened correctly. Source facts retained the two bridge unknowns as unavailable, and Reinvestment retained empty years 6–10 with the recorded explanation. Model checks displayed these gaps and existing input warnings without an exception. Results and analysis pages showed explicit deferred/unavailable states.

A recorded FY2025 10-K source link opened the correct AVGO cached document in a separate tab, retained its original SEC link, and disclosed the absence of an exact citation locator. Searching `63,887` displayed five highlighted matches. Sidebar navigation and Back/Next worked.

An in-memory bear-weight edit from 25% to 26% propagated to Taxes and weights, showed the 101% total warning, and appeared accurately in Review. The explicit reset restored 25/50/25; Review then showed zero unsaved changes. Save and Write report disabled states had explanations. No Save, Write report or Commit action was used, and the source YAML bytes remained unchanged.

A separate regression check on the freshly restarted normal app at `http://localhost:8501/` confirmed that AVGO's blocked draft still renders. The selected-case warning panel remains compact while scrolling, with the complete input errors accessible on Model checks. No substitute price, bridge amount or reinvestment assumption was entered.

## Outcome

The actual AVGO draft is usable for narrative and input review in the app. This is a rendering and interaction check, not another financial review pass. The [financial review](FY2026-Q2-valuation-draft-review.md) remains BLOCKED by unresolved corporate investments, the customer-lease backstop and later capital needs. No price target or AVGO valuation report was produced by this check.

Evidence: `output/playwright/avgo-app-2026-09-19/`, including `page-01-overview.png` through `page-15-review.png`, focused narrative/source captures, `weight-edited.png`, `review-unsaved.png`, `review-controls.png`, and normal-mode regression captures. See the independent audit for the exact page-to-file mapping and version hashes.
