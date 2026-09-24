# Scenario judgment controls — independent delivery audit

**Outcome: PASS for delivery, with one nonblocking wording observation below.** All 15 pages opened in a headless Chromium browser at 1440 × 900. Full scroll coverage, screenshots, and rendered text were checked for readable labels, complete reasons and narratives, number formats, navigation, clipping and exceptions. No persistent blank section, horizontal page overflow, truncated control, or app exception was found. This is the independent app audit required by [APP_GUIDE.md](../APP_GUIDE.md), not a financial review or a target-company draft check.

## Final version after the review-only rate fix — PASS

Repeated all **15 pages** on a fresh synthetic server **PID 24506**, started **2026-09-19 11:02:39 America/Los_Angeles**, bound only to **127.0.0.1:8597**. The original synthetic root was reused with `VALUATION_APP_NO_FETCH=1`, the same `.venv/bin/python -m streamlit run tools/valuation/app.py` command and light-theme settings, and browser session `synthetic-scenario-final` at 1440 by 900. The final audit retains **one screenshot per page plus three focused regression screenshots**, together with full rendered-page text and [metadata](../../../output/playwright/scenario-judgment-final/metadata.json). The original detailed scroll audit below supplies the unchanged longer-layout evidence.

**Final app source-manifest SHA-256:** `4a86aa020d3d643855c5680d061621ae8123622cc5a9a8023b00f7b23663572e`. `app_pages.py`: `e11bdab28bb37e92a1d0f28174e6cd3113d78c19aaa2099af3856d1d88e56491`; `app_core.py`: `87e787146c9faed251a11ae827cb54de56d526e70a81c0e39d80ed533a7d588e`. [Full source hashes](../../../output/playwright/scenario-judgment-final/source-sha256.txt) matched at completion. This replaces the initial manifest below as the delivered version. Parent validation reported **316 passed, 1 optional workbook skipped**; the auditor did not rerun that suite.

All pages remained readable with zero app exceptions and no horizontal page overflow. The synthetic fixture's loaded **2.00-point bear premium** was accepted; **9.00** was blocked without its override, accepted with it, and retained the warning. All four case transition rows remained present. Scoped reset restored the loaded 2.00 and override off, and Review showed **Unsaved changes (0)** with Save disabled. The input remained at SHA-256 `9de05669ba095d21191b66c7a9478be317e5d20c6df57af6024e3fe3bc03ba02`; the final-version check performed no Save, report-write or commit.

The missing-rate state was separately simulated **in memory** with the same synthetic fixture and unchanged app source. A [temporary probe wrapper](../../../output/playwright/scenario-judgment-final/missing-rate-probe.py) sets only `market_values.EXMP.rf` to `None` before loading the app, representing unavailable market data. Probe server **PID 26582**, local port **8598**, started **2026-09-19 11:10:52 America/Los_Angeles**. All four controls showed **“Equal to the risk-free rate (unavailable)”**, were disabled, retained their existing checked state and displayed the instruction to set the rate on Overview. No zero rate or input write was introduced. [Missing-rate screenshot](../../../output/playwright/scenario-judgment-final/risk-free-unavailable.png).

The actual META and GOOGL candidates were independently rechecked on fresh review-only server **PID 24483**, local port **8596**, with the same final source hashes. Their known cached 4.75% rate now appears correctly on every terminal sentinel; results remain deferred. Target-specific records: [META](../../../companies/META/review/2026-Q2-valuation-app-check.md), [GOOGL](../../../companies/GOOGL/review/2026-Q2-valuation-app-check.md).

**Cleanup completed after final checks:** the task's temporary browser sessions were closed or already absent. Audit/review servers on ports **8594–8598** were stopped or already exited; a final listener check found none. Only the recorded task processes and named task sessions were addressed. Screenshots, metadata, probe evidence and reports remain available. [Cleanup record](../../../output/playwright/scenario-judgment-final/cleanup.json).

## Initial version and isolated process

- App version 0.1.0; Python 3.12.10; Streamlit 1.63.0. Worktree based on `b4253491dd3a8ba3c0520919982b6acb989a2e2e`; HEAD alone does not identify the uncommitted changes.
- Fresh server PID **2804**, started **2026-09-18 23:28:33 America/Los_Angeles**, bound only to **127.0.0.1:8594**. Audit and final verification: 2026-09-19.
- Exact command: `VALUATION_REPO_ROOT=/private/tmp/scenario-judgment-audit-x5hcb0e8 VALUATION_APP_NO_FETCH=1 .venv/bin/python -m streamlit run tools/valuation/app.py --server.address 127.0.0.1 --server.port 8594 --server.headless true --browser.gatherUsageStats false --theme.base light --theme.primaryColor '#575be7'`.
- SHA-256 of the sorted `tools/valuation/*.py` hash manifest: `8ce45d9f8d7168a62d1c5ba8a2e9c12cbf8b5c34c8621ecec98a84a4de89d33d`. Every recorded source hash still matched at completion. `app.py`: `2695b2a2afaa0410723261e0c4f0c6c2475d67d897075812fe81c7e00394362e`; `app_pages.py`: `1452ff15c3f140a5145e8a522d84d60a5b29cc30633c63e8f9c4e5b80b968b08`.
- Full [metadata](../../../output/playwright/scenario-judgment/metadata.json) and [source hashes](../../../output/playwright/scenario-judgment/source-sha256.txt) are retained with the screenshots. Browser sessions were `scenario-judgment`, then `scenario-judgment-final` after a tooling-session interruption. The same unchanged app process was used; final checks used the installed cached Playwright CLI directly when the `npx` wrapper lost its session/network availability.

The only company loaded was **EXMP, Synthetic audit — Example Semiconductor, Inc., FY2027-Q2**, adapted from the documented example fixture, with horizon 10 and explicit offline inputs: price USD 45.00, risk-free rate 4.00%, ERP 4.50%. Source text was explicitly labelled synthetic. Loaded input: `/private/tmp/scenario-judgment-audit-x5hcb0e8/companies/EXMP/valuation/assumptions.yaml`; initial SHA-256 `817320db1a9e0557a6cfa9185be552923e97d54f5936ecf3e457ddda559cd5fb`. No real company inputs were edited, saved, or computed. No report-write or commit action was invoked.

## Page coverage

Screenshot prefixes below are under [output/playwright/scenario-judgment](../../../output/playwright/scenario-judgment/). Numbered images cover successive scroll positions; contact sheets support the visual review. A few early captures caught transient redraws; the final Analysis, management-guidance and simulation captures replace those views.

| Page | Evidence prefix | Result |
|---|---|---|
| Overview | `01-overview` | Offline inputs, dates, orientation and impact ranking readable. |
| Scenarios | `02-scenarios` | Three path comparisons; all full stories and mappings; two five-year matrices; management separate and unweighted. |
| Revenue growth | `03-revenue` | Five annual controls, live fade, history and complete reasons. |
| Operating margin | `04-margin` | Annual controls, ROIC comparisons and explicit missing historical-ROIC state. |
| Terminal value | `05-terminal`, `bear-premium-*` | Bear positive premium, warning threshold and override exercised below. |
| Cost of capital | `06-capital` | Shared build, derived rates and per-case overrides readable. |
| Reinvestment | `07-reinvestment` | Ratios, spending overrides, ROIC comparisons and full reasons. |
| Taxes and weights | `08-taxes` | Tax inputs, weights, totals and unweighted management clear. |
| Source facts | `09-facts` | Source-linked base year, bridge, and capital build readable. |
| Valuation | `10-valuation` | Case chart/table and five-year reference labels readable. |
| Analysis | `11-analysis`, `analysis-reverse-final` | Both sensitivity grids and complete reverse-DCF table. |
| Cash flow forecast | `12-forecast` | Two readable tables, fade-year and terminal labels. |
| Simulation | `simulation-final` | Settings and results checked; 2,000 valid default draws reproduce USD 54.58; transition warning remains. |
| Model checks | `14-checks`, `bear-premium-9-warning` | All four case transitions present; flagged rows and economic-review wording coherent. |
| Review & save | `15-review`, `reset-no-unsaved-changes`, `synthetic-save-final` | Comparison, note, disabled-action explanations, reset and synthetic Save checked. |

Sidebar navigation, Back/Next, the case selector, and disclosures worked. Selecting Bear remained selected after sidebar navigation, with its value and market price visible. The [management guidance disclosure](../../../output/playwright/scenario-judgment/management-guidance-final.png) preserves quote text, source labels and the nonnumeric guidance classification. Its [source popup](../../../output/playwright/scenario-judgment/source-transcript.png) opens separately, highlights the exact cached quote and leaves the editing tab intact.

## Changed behavior exercised

1. **Bear 2.00 points:** accepted with the override off; terminal ROIC became 10.50% against terminal WACC of 8.50%. The current bear value updated from USD 12.57 to USD 13.97.
2. **Bear 9.00 points, override off:** calculation stopped with the explicit message that the bear premium is above 8 points and requires “Allow a large premium” or a lower value. The full explanation was readable at the factor footer and on Model checks; no stack trace appeared.
3. **Bear 9.00 points, override on:** accepted; terminal ROIC became 17.50%. Model checks retained the large-premium warning and the saved reason. The control was also operable by keyboard.
4. **Scoped reset:** restored premium 0.00 and override off. Review showed **Unsaved changes (0)**, Save was disabled with “Nothing to save”; the input hash still matched the initial hash.
5. **Temporary-fixture Save:** a new 2.00-point edit saved one changed cell and rewrote `assumptions.md`. Parsed before/after comparison found only `scenarios.bear.terminal.roic_premium.value`, `owner_edited`, and `changelog` changed. Reasons, stories and source metadata remained intact. The one changelog row recorded 0.00 to 0.02 with the test note. Final synthetic input SHA-256: `9de05669ba095d21191b66c7a9478be317e5d20c6df57af6024e3fe3bc03ba02`.

The restored zero-premium case displayed a flagged bear cash-flow transition alongside base, bull and management. The explanation says the same checks apply to every case and that thresholds prompt economic review; it does not instruct the owner to tune inputs merely to remove flags.

## Nonblocking observation

When the unapproved 9-point bear premium prevents the shared compute, the live strip can say **“Base case needs attention”** while Base is selected, even though Bear caused the validation failure. The correct bear-specific explanation is present at the factor footer and Model checks. Showing the shared error directly in the strip would make recovery clearer. Reported to the builder; this does not prevent entry, diagnosis, override, reset or saving.

Browser console output contained Streamlit's repeated empty sidebar `textColor` warning, with no browser errors or visible color defect. No app-code changes were made by this audit, and no commit was created.
