# Monte Carlo implementation review and app audit

Date: 2026-09-10. Reviewer: independent `monte_carlo_review` agent. **PASS — first review pass.** No unresolved substantive findings in the feature. This review covers the Monte Carlo implementation and necessary app integration, not unrelated owner changes already present in the checkout. No implementation or production company files were edited by the reviewer.

## Mathematical and economic review

The reviewer inspected `simulation.py`, `app_simulation.py`, the existing FCFF engine and sensitivity/transition helpers, shared schema bounds, app integration/reset paths, both simulation test files, and the Monte Carlo documentation directly.

| Check | Evidence and conclusion |
|---|---|
| Existing deterministic engine is reused | `simulate` takes a resolved valuation and calls `engine.run_scenario`. It does not introduce a second cash-flow calculation, fetch market data, mix scenarios, or write company files. |
| Zero uncertainty | Tests cover bear/base/bull/management at both horizons, comparing exact sampled inputs, operating rows, terminal calculation, and per-share output. Browser base-case result was exactly 41.71599543636716 for all 100 draws, equal to its deterministic value, with zero standard deviation. |
| Sampling and reproducibility | Inverse triangular CDF is checked against an independently evaluated CDF, including endpoint modes and fixed ranges. A local seeded RNG preserves global state. Repeated browser downloads have identical draws, summary and fingerprint. |
| Dependencies | Same/opposite rank uses the same uniform rank or its complement. Those choices preserve triangular marginals and impose the stated perfect rank dependence; independence is explicitly a modeling assumption. Linking to fixed growth is rejected. No company correlation is claimed or fitted. |
| Growth, margins and investment | Growth shifts rebuild only an automatic five-plus-five growth fade. The resolved margin path is shifted in place, preserving separately authored late margins such as MRVL bull. Sales-to-capital changes both periods together. Tests independently recompute lagged revenue changes for lags 0–3, preserve spending overrides, and check the distress bridge. |
| Terminal consistency | Terminal growth, financing and return premium stay fixed; the engine still derives reinvestment from growth divided by terminal return. Tests check terminal cash flow and the zero-excess-return identity. Shifted final margins feed the same engine terminal calculation. |
| Failures and warnings | Exactly the requested attempts are retained. Bounds/arithmetic/nonfinite failures retain inputs and reasons; no replacement sampling or clipping. Finite negative equity remains with a warning. Transition warnings are counted without excluding draws, retaining the existing bear exemption. |
| Summaries, histogram and export | Mean, median, inclusive P10/P90, population standard deviation and strict price-threshold counts reconcile to independently read browser JSON. Histogram bins use their actual numerical edges. The export records settings, reasons, resolved inputs, every attempt, errors and version metadata. |
| App state and workflow | Controls remain in the session across navigation and are cleared on company reload. A fingerprint hides old results after assumption, market, case or setting edits. A changed file on disk disables simulation until reload. Save/report actions remain separate from simulation; focused app tests verify no implicit file writes. |

The builder identified a very-small-spread histogram rounding discrepancy while this review was underway. The final implementation merges duplicate floating-point edges and counts against the displayed edges with `bisect_right`. The reviewer inspected that correction and ran its three regression cases as part of the final focused suite; it is resolved. This remained within the same first review pass.

## Primary-source checks and implementation decisions

The reviewer read original material directly, rather than relying only on the feature's research note:

| Original reference | Checked guidance and affected design |
|---|---|
| [Damodaran, DCF Myth 3.2, 2016-05-23](https://aswathdamodaran.blogspot.com/2016/05/dcf-myth-32-if-you-don-look-its-not.html), simulation Steps 3–6 | Relevant history and judgment inform distributions; bounded target margins and explicit relationships are useful; resulting percentiles depend on the assumptions. Supports editable triangular judgments and explicit dependency controls, without borrowing Apple's historical calibration. |
| [Damodaran, Capital Budgeting Under Uncertainty](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/lectures/cbuncert.html), Monte Carlo Steps 1–5 | Develop input distributions, draw and value outcomes, account for related variables, and report distributions plus summary statistics. Supports the reusable engine wrapper, dependency choices, histogram and summaries. |
| [Cached original growth-and-value article](../damodaran-notes/sources/growth-and-value.txt), “Paying for Growth” and “Excess Return Effect” | Growth requires reinvestment; value effects depend on returns relative to the cost of capital. Supports deriving investment/cash flow from sampled operating inputs and retaining the terminal growth/return identity. |
| [Cached original terminal-value chapter](../damodaran-notes/sources/terminal-value.txt), “Project Returns” and “Reinvestment and Retention Ratios,” PDF pp.10–13 | Mature returns and growth-compatible reinvestment must be assessed together. Supports keeping selected terminal assumptions explicit and letting the existing engine derive terminal reinvestment. |
| [Repository uncertainty guide](../../../.claude/skills/draft-valuation/references/uncertainty-and-bias.md) | Connected business assumptions, price-independent judgments and honest probability labels support single-case conditional experiments, explanatory warnings and no inferred bear/base/bull quantiles. |

The three drivers, additive path shifts, common capital multiplier, triangular family and extreme rank choices are app modeling decisions, not claimed universal Damodaran rules. Fixed initial ranges avoid silently supplying calibration. The original probabilistic chapter endpoint timed out twice through web retrieval; a direct network attempt failed DNS in the sandbox and its pending escalation was canceled. No claim is made that this reviewer retrieved that PDF. The independently read original article/lecture and cached primary chapters establish the reviewed principles without it.

## Verification results

- Reviewer command: `.venv/bin/python -m pytest tools/valuation/tests/test_simulation.py tools/valuation/tests/test_app_simulation.py -q` — **47 passed in 8.21s** on the final code, including histogram regressions.
- `git diff --check` — passed.
- Builder separately reported the complete final suite: **220 passed, 1 skipped**. The skip is the optional direct-original-workbook check whose `/tmp/damo` downloads are absent; cached workbook-fixture checks passed. This full-suite run is builder evidence, not represented as independently rerun by the reviewer.
- Actual browser JSON files `mc-zero.json`, `mc-uncertain-a.json`, and `mc-uncertain-b.json` were independently loaded with Python. Zero uncertainty matched exactly. Both seeded nonzero runs matched exactly. Mean, median, P10/P90, population standard deviation and frequency numerator matched raw draws. Nonzero example: 100 valid draws, mean 42.470138402207155, median 42.30611770233638, P10 40.27741344906318, P90 44.798852666425645, standard deviation 1.7082799626930074.

## Headless app audit

The reviewer used a separate Playwright CLI session, `valuation-mc-review`, at **1180 × 820**, against `http://127.0.0.1:8512`. The server used isolated temporary company files under `/private/tmp/valuation-monte-carlo-preview`, with illustrative manual market inputs and fetching disabled. Production assumptions/reports were not changed. No Save, Write the report or repository-commit button was used.

Every page was opened, captured and visually inspected at laptop width. All retained readable controls, complete labels, consistent formatting and clear page navigation. No clipping, overlapping content, rendering exception or JavaScript error was observed. The console contains transient Vega extent warnings during chart rerenders; the completed charts rendered correctly in the inspected captures.

| Page | Screenshot | Result |
|---|---|---|
| Start | `page-01.png` | PASS |
| The stories | `page-02.png` | PASS |
| Revenue growth | `page-03.png` | PASS |
| Operating margin | `page-04.png` | PASS |
| Terminal value | `page-05.png` | PASS |
| Cost of capital | `page-06.png` | PASS |
| Reinvestment | `page-07.png` | PASS |
| Taxes and weights | `page-08.png` | PASS |
| Facts check | `page-09.png` | PASS |
| Results | `page-10.png` | PASS |

Feature interactions additionally verified in the browser:

- Zero-uncertainty run: 100 valid attempts, one point-distribution bar and correct deterministic reference (`mc-zero.png`).
- Nonzero range entry and persistent expanded panel (`mc-controls.png`); stale settings message appeared and prior statistics were hidden before rerun.
- Seeded nonzero results and actual downloadable output (`mc-uncertain.png`, the two JSON files above).
- Partly invalid margin range: **83 valid, 17 invalid** out of 100; a visible warning explains valid-subset bias and the failure reason count (`mc-partial.png`).
- All-invalid margin range: **0 valid, 100 invalid**; no distribution statistics, explicit error and export still available (`mc-all-invalid.png`).

Screenshot/export artifacts are under [`output/playwright/valuation-mc-review/`](../../../output/playwright/valuation-mc-review/). The focused Streamlit tests additionally cover unsaved valuation edits, case changes, company reload, external file changes, malformed settings, negative values, and absence of implicit saves.

## Reviewed version

SHA-256 values of feature and integration files after the final histogram correction:

| File under `tools/valuation/` | SHA-256 |
|---|---|
| `simulation.py` | `39faedf5a1ef9247e513ce9f79f97a927f5b571c6b15bc1dab9d0173c4786c60` |
| `app_simulation.py` | `8d148824e7dcbc64f9f7ceba92b41647b7b4db15dda631618998129f99b498da` |
| `app.py` | `c4c1b7e3fc4b7d722f52575305cbbeedb54ecb6343b5052df0af78b1bdec36c8` |
| `app_pages.py` | `60c1d4115e981d1fd17042aa77dca4bb2c5241aa1ee096763607ea8aedf4d690` |
| `app_core.py` | `85c7e71b29bd3418c36f8cc48b364252c6b8ee82daffd8de871ba5de63276e33` |
| `schema.py` | `3dd5f6cb347a6e36d66e5fc5058a322fbf715d89ad92b540aaf24abc81674ec8` |
| `__init__.py` | `492667bba3b9471c660d4abffc85572ea3af3de77778c9cb3dd483415b19fb8d` |
| `tests/test_simulation.py` | `9cb6ac422e0f665277b9326cb36f93a8eea11866ba4f151cee9c21ab58c898ea` |
| `tests/test_app_simulation.py` | `468fd44dbfdd1f8147c83c5a11019bf77127b599fd051dd90bfc3f4444e995a5` |
| `README.md` | `5dc81332f164a1524e4d0d5ba209fc2f4623ff9a272df10c90fe62a3996a923e` |
| `damodaran-notes/2026-09-10-monte-carlo.md` | `7374f57f55c5effc0cc0518e46c47c5e905bb0f591e108226d7766fe8a098242` |

Remaining modeling limitations are disclosed rather than defects: conditional single-case uncertainty; user-judgment distributions; fixed financing/terminal/bridge inputs; whole-path shocks; optional perfect rank dependence rather than estimated partial correlations; and no new capacity, default, limited-liability or annual-shock model. Mechanical bounds and transition checks cannot prove business plausibility. Valid-only statistics can be biased when failures occur. Session settings are exported but are not saved in company assumptions or the deterministic report.
