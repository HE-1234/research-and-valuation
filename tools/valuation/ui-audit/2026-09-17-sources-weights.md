# Clickable sources and scenario weights — independent audit

Status: PASS for reviewed code, targeted tests, and supplied desktop captures — root browser verification plus independent capture review. The auditor did not independently execute the browser interactions.

## Execution scope

The independent reviewer inspected `app_sources.py`, its `md()` integration and source-view entry route, the scenario weight controls, and targeted tests. Its CUA browser inventory returned `browsers: []`; it did not retry native Chrome or use a terminal browser. The reviewer independently inspected exported root-browser captures, with browser navigation and interactions attributed to the root.

## Code review

- Evidence paths are resolved and restricted to permitted research/method/data locations. Source-view requests must match the selected company's recorded index. Symlink escape and unknown sources are rejected.
- Public document URLs come from an explicit cached-file header or an unambiguous manifest row. Ambiguous provenance falls back to the cached text; no SEC URL is guessed.
- Source markdown escapes ordinary text. The initial alias search could incorrectly resolve `[COHR 10-K FY2025]` to AAOI's filing by matching its inner generic alias. The reviewer reproduced this using AAOI's actual index and requested a citation-context correction. The builder added citation-context protection and unknown-identity regression checks. The final targeted retest passed, resolving this finding.
- Weight edits use the shared working document and bound input widgets. The default reset changes only bear/base/bull weights and requires an explicit button click. The management case is omitted. The new tests cover cross-page synchronization, invalid totals, save/change-log behavior, saved non-default weights, and preserving unrelated edits on reset.

## Checks so far

The first targeted reviewer test run produced 31 passes and one failure: the new unbracketed `UNKNOWN 10-K FY2025` regression exceeded the implementation's six-character uppercase-prefix guard. The builder corrected it. After the final Source facts copy and missing-cache label changes, an independent run of `tests/test_app_sources.py` and `tests/test_app.py` passed all 33 tests using `.venv/bin/python -m pytest -q`. The equivalent `uv run` invocation could not access the sandboxed uv cache; this is a tool-environment limit, not a test failure. The builder reports the final full suite at 240 passed, one skipped, and `git diff --check` clean; these two broader checks were not independently rerun by this reviewer. No production assumptions were edited by the reviewer.

## Visual review

Inspected `output/playwright/sources-weights-2026-09-17/page-01.png` through `page-15.png`, `scenarios-weights.png`, `source-viewer.png`, `weights-edited.png`, `weights-invalid-total.png`, and `source-index.png` with image tools. The 15 main page captures are 1280 × 720; the source-viewer capture uses a narrower window.

- Scenarios: bear/base/bull input labels explicitly identify percent units, the three controls align evenly, the 100.0% total is clear, and the weighted-value readout is visible. The default reset is visibly disabled for 25/50/25. Management exclusion and save behavior are explained in the card.
- Source facts: source tags are visibly underlined links in their own table column. Names remain legible and separated from values. The inline method/source link visible on Terminal value fits the prose without overlap or escaping artefacts.
- Edited/invalid weights: the 30/45/25 capture clearly shows saved-versus-unsaved labels, a 100.0% total, and USD 71.81 weighted value. The 30/50/25 capture shows a readable 105.0% error and suppresses the weighted-value readout. The enabled reset is visible in both states.
- Expanded source index: linked citation tags and cached filenames occupy distinct columns; notes wrap within their cells and source identity remains legible. Dates wrap onto two lines but remain unambiguous.
- Final source-index capture: `source-index-final.png` visibly shows the revised explanation of original-document links, cached copies, and separate tabs. Its 1280 × 720 viewport shows the top of the index; the new `(not cached)` label lies outside this capture and was verified from the rendering code and focused AppTest assertion. No overlap or clipping appears in the captured rows.
- Source viewer: company/tag/file identity, explanatory note, download control, and wrapped cached text are readable. The captured notes are clearly a research copy; the explanatory caption tells the reader their edits remain in the original tab. No raw HTML or markdown-link syntax leaks into normal app prose.
- All 15 captured page viewports retain consistent headings, selected navigation, live-value strips where applicable, and readable primary content. No blocking overlap, horizontal clipping, or error overlay is visible. Existing diagnostic raw-decimal warnings are outside this change.

Scope limitations: this was independent screenshot inspection, not independent browser execution. The root reports navigating all 15 pages without a traceback, opening cached evidence in a separate tab with the original app unaffected, and resetting the edited weights to 25/50/25 and USD 74.36. The captures are viewport samples, not every scroll position or mobile width; source URL reachability on third-party sites is not independently tested. Weight synchronization/save/reset behavior is supported by the independent AppTest run above.

## Version checked (SHA-256)

- `app_sources.py`: `19696f274960e27acc46924f71ea6dfa5fcce6fc1c2a4eeecc87f815d0726376`
- `app_core.py`: `921e8b6b5b35524dda699fd2079a0fdf5e020d62ac4d9e20cb10ad24fe8c6626`
- `app_scenarios.py`: `1cdab2dd576eb789caf44c4593085dca5eb7b2ac3e1834d87ec439174fe8bef1`
- `app_pages.py`: `a398cb0a7e7330c23108f81219f5dd6da191df287434419f775fd32950c594be`
- `app.py`: `bd3b482afaa44236a6bde7521cf7aef077ab9dc11fabb273a34162be096edf8a`
- `tests/test_app.py`: `eb8967e9e7ccf44db0195fb0bb1c73958bee4893ae5ae01babf8ab8191f8f660`
- `source-index-final.png`: `c9467133f0f3f5d614f898373efb69bfea3d424e88e21e442570ae693d8b68b8`
