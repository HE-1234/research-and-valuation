# Mercury-inspired workspace — independent UI audit

**Result: PASS for delivery.** Audited 2026-09-10 by a separate browser audit agent, using Playwright Chromium at **1180 × 820**. All 15 pages were opened, captured, and visually inspected. No page exceptions or document-level horizontal overflow occurred. The final shared metric-style correction was separately checked after restarting the server; values render at 23.2 px without clipping.

## Scope and version

Local app: `http://127.0.0.1:8514`. Isolated synthetic EXMP fixture: `/private/tmp/valuation-mercury-preview`. No production company files were edited; no report generation or repository commit was invoked. The fixture assumptions were restored byte-for-byte after the save and external-change probes.

Final SHA-256 hashes:

| File | SHA-256 |
|---|---|
| `tools/valuation/app.py` | `186b29a02235e5579a99a954ab5aa369dfde860d0000b0981429a6a8b9bc88d6` |
| `tools/valuation/app_core.py` | `14f6669752d0a7267595697ea8b507c154cf185aabefee87064fc2c87d27b2c4` |
| `tools/valuation/app_pages.py` | `b6585f6ad14d7f63a08a44feee8b64f8add7fe25b9cca0a0956d01b70e797a97` |
| `tools/valuation/app_workspace.py` | `f32331a9a93ed614ba926b4a014e02ac06ae279b5461d13908e69a5d6685d18b` |
| `tools/valuation/app_simulation.py` | `8d148824e7dcbc64f9f7ceba92b41647b7b4db15dda631618998129f99b498da` |

## Visual findings and resolution

- Grouped sidebar provides direct access to all 15 destinations, with a clear selected state. Overview, Scenarios, six assumption pages, Source facts, Valuation, Analysis, Cash flow forecast, Simulation, Model checks, and Review & save each rendered correctly.
- The revised typography, spacing, restrained palette, bordered case sections, readable tables, and dedicated analysis pages support the requested Mercury direction. Five annual inputs fit on one row at laptop width; saved reasoning remains adjacent and visible.
- Initial sidebar group-label overlap and overlapping live-strip captions were fixed by removing inherited negative markdown margins in those areas.
- Initially invisible disabled Save text was fixed. The final Review & save capture shows its readable disabled state and explanation.
- Initially undersized live values were fixed after a CSS-specificity recheck. Final screenshots show prominent current value and market price, with separate baseline and change labels.
- The live strip stays at y=46 after scrolling the main pane by 900 px; all its fields remain readable while factor inputs and reasons are visible below.

## Behavioral evidence

| Check | Result |
|---|---|
| Sidebar navigation | All 15 destinations opened; headings matched; main content returns to the page start. |
| Edit and live recompute | Base first-year growth 20% → 21% changed value from 41.72 to 42.09; displayed change +0.38 reflects underlying precision. |
| Edit persistence | The 21% input and 42.09 live value persisted after visiting Operating margin and returning to Revenue growth. |
| Saved reasoning | Saved-versus-edited values and an explicit unchanged-analyst-reason label appeared beside the edited input. |
| Review | Exactly one changed cell appeared, 20.0% saved versus 21.0% current; report writing was disabled pending Save. |
| Save | A fresh session saved the fixture edit, reported one changelog entry, regenerated assumptions.md, and returned the change count to zero. |
| External file change | Save, Write the report, Record in the repository, and quick Save assumptions were all disabled. Clear reload instructions appeared, and external differences were not attributed to the owner. |
| Simulation | The dedicated page ran 2,000 draws successfully: 2,000 valid, zero invalid; default fixed inputs reproduced the current edited case, mean 42.09 and standard deviation 0.00. |

A development session retained an old YAML document class across source hot reload and failed Save. Retesting from a new browser session passed; the delivered app was restarted with final modules. This is not evidence of a clean-start save failure. Browser console warnings were Streamlit theme/iframe warnings; connection errors during explicit server restarts were excluded from the stable-page checks.

## Screenshot evidence

Directory: `output/playwright/valuation-mercury-audit/`.

- `01-overview.png` through `15-review-save.png`: all 15 pages at 1180 × 820, after layout fixes and before the final metric-font-only adjustment.
- `17-edit-persistence.png`, `18-review-edit.png`, `20-stale-guards.png`: edit, review, and stale-file evidence from the interaction probes.
- `21-final-header.png`, `22-final-sticky.png`: final shared header at the hashes above, including the 23.2 px metrics and scrolled state. These supersede the earlier header appearance in the page captures.

This audit covers the synthetic fixture and laptop viewport; it is not a mobile, screen-reader, or every-company-content certification. Simulation result retention across navigation was not part of the completed verification; the simulation run itself was verified.
