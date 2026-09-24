# Scenario readability — independent audit status

**Status: PASS for the supplied 1280 × 720 captures — root browser verification + independent capture review.** The independent browser attempt remained blocked; a separate reviewer subsequently inspected exported root-browser screenshots. This is not independent browser execution or verification of every scroll position.

Requested scope: all 15 pages, with focused AAOI Scenarios review at laptop widths, management-case explanation, and edit → return verification using isolated preview `http://127.0.0.1:8520`. Production data was not touched.

## Successfully inspected

Read `tools/valuation/app_scenarios.py` and the relevant scenario rendering references in `app_pages.py`. The implementation provides one variable per table row, at most five annual columns per table, explicit percentage/multiple/USD-million formatting, a calculated-forecast-revenue explanation, case settings in Variable/Chosen value columns, visible narrative/source mappings, and a separate original-annotations expander. These are code observations, not verified browser results.

## Concrete tool failures

- `cua.createBrowserTab("iab", ...)`: browser unavailable.
- `cua.getState()`: no browser surfaces (`browsers: []`).
- `cua.getBrowser({url: ...})`: no browser available.
- Native fallback `cua.getApp("com.google.Chrome")`: hung for 373.5 seconds and was aborted by the user.

No page screenshot, layout, dynamic-edit, or complete navigation check succeeded in this auditor's CUA session. Terminal Playwright was not used because this pass explicitly required CUA for all browser interactions. The parent subsequently reported an available IAB surface and clean Scenarios rendering at 1280 × 720; those parent observations are not represented as independent verification here.

## Root browser verification (reported by the implementing agent)

The root agent reports using its functioning IAB surface to open all 15 app pages and capture 1280 × 720 screenshots in three batches, with additional full-width Scenarios year-matrix and chosen-value captures. It also reports changing Base Year 1 growth from 226.83% to 227.8% in the isolated AAOI preview, returning to Scenarios, and observing 227.8% and forecast revenue of 1,954 in the DOM. Production data was not changed. The root reports 232 tests passed and one skipped. These are root verification results, not independent browser execution or independently inspected images.

## Independent capture review

A separate reviewer initially lacked the inline image content in its inherited context. The root then exported screenshots to `output/playwright/scenarios-2026-09-16/`. The reviewer used image inspection on all 15 `page-01.png` through `page-15.png` captures and the five focused captures; it did not launch or operate a browser.

Concrete findings:

- `base-inputs.png` and `base-late-inputs.png`: one variable occupies each clearly ruled row; the generous label column and five annual columns fit without horizontal clipping. Revenue growth, operating margin, and taxes visibly use percentages. Forecast revenue and net reinvestment explicitly carry USD-million labels; sales-to-capital carries a times label. Year 1 growth 226.8% maps cleanly to its row, and forecast revenue 1,948 maps to the next row. Years 6–10 repeat the same layout and alignment.
- `base-settings.png`: Variable and Chosen value columns have consistent row separators; case weight, terminal growth, terminal return premium, tax rate, and cost-of-capital values each map unambiguously to their labels. The return premium is explicitly expressed in percentage points. The narrative begins below the table with a visible Supports mapping, keeping explanation separate from numbers.
- `page-02.png`: the Bear, Base, and Bull preview cards have aligned year/growth/margin columns. Multi-line headers wrap cleanly within each card, with no overlap.
- `management-explanation.png`: the management-versus-bull distinction and “Why this case is not computed” paragraphs wrap cleanly inside the full-width card. Their body text, source tags, collapsed guidance and edit controls, and Back/Next buttons are readable without overlap. The heading itself is at the upper scroll boundary; the explanation body is fully visible.
- All 15 page captures show legible main headings, consistent sidebar selection, and no visible error overlay, overlapping primary content, or horizontal clipping in the captured viewport. The visible portions of charts and tables remain aligned. The existing raw-decimal model warnings on page 14 are outside this scenario-layout change.

Limitations: these are viewport captures, not full-page or mobile screenshots; content below the captured areas was not independently inspected. Helper captions are pale, although the principal labels and values are readable. The initial `management-guidance.png` showed only the Scenarios header; the subsequent `management-explanation.png` resolves the explanation-body coverage gap. The guidance-details expander remains collapsed and its contents were not independently inspected. Dynamic edit behavior remains the root's reported browser verification, not an independently replayed interaction.

Version hashes recorded by the capture reviewer (SHA-256):

- `tools/valuation/app_scenarios.py`: `b1bdc4a31ea48f1b06490ee857015114cafa9d83fedf58f0a4844ab83e062b38`
- `tools/valuation/app_pages.py`: `fe098655de0c95343c08e66c5589287f1e4acec1806bde96330bde709625f228`

## Delivery scope

The scenario variable/value readability change passes independent inspection of the supplied desktop captures. Root navigation and numeric-edit verification are recorded above. Do not describe this as an independently executed browser audit or a visual inspection of the collapsed guidance details, mobile widths, or all below-fold content. No blocking visual defect was identified within the reviewed captures.
