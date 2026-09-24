# Notes reader — independent visual audit

Status: **PASS**, after the fixes below. Audited September 18, 2026 Pacific (September 19 UTC).

## Method and scope

The separate audit agent independently operated headless Chromium through the Playwright CLI, captured the screens, and inspected them. The app ran on local port 8531 with market fetching disabled. An unsaved USD 100 price was entered only to make the existing main pages computable; no Save, Write report, or repository action was used. The reviewer made no app or company-artifact edits.

All 15 main destinations were opened and captured at 1280 × 800: Overview, Scenarios, Revenue growth, Operating margin, Reinvestment, Cost of capital, Terminal value, Taxes and weights, Source facts, Valuation, Analysis, Cash flow forecast, Simulation, Model checks, and Review & save. All have readable headings, consistent navigation, clear page purpose, and no new overlap, truncation, raw Markdown or exception. The existing long raw-decimal warnings on Model checks predate this change and remain outside this notes-reader update.

The reader audit used the real indexed AAOI benchmark note, the MU peer operating-scale note, the AAOI business-drivers methodology reference, and an AAOI FY2019 10-K text source reached from a note citation. Notes were reviewed at 1280-pixel laptop width; the long AAOI tables were also checked at 900 × 800. Initial top captures are 1280 × 720; later focused captures are 1280 × 800. These are viewport samples plus focused scroll positions, not every pixel of every document or a full mobile/accessibility audit.

## Findings and verified fixes

1. **Wide tables:** the first version hid the last columns of nine-column tables at laptop width. The final reader splits them into groups of no more than five columns, repeats row labels, and identifies continued tables. The reviewer inspected both groups, including depreciation and capex. All 11 resulting AAOI tables have equal client and scroll widths at 1280 and 900 pixels. The final CSS also fills the available table width without an empty area inside the border.
2. **Search while reading:** initially, results appeared above the reader's current scroll position with no visible response. The final sidebar shows the match count beside the search field and a same-tab jump to results. Searching `22.7%` returned three highlighted passages; the jump placed the result region below the header while retaining company/source query parameters. A phrase with no match showed an explicit no-match message.
3. **Relative Markdown links:** initially, methodology links such as `worked-examples.md` opened a new Overview at an unrelated URL. The final renderer links only an exact indexed local target and marks other local targets unavailable. The methodology page now identifies unavailable worked examples and retains the recorded `terminal-value.txt` viewer link. External source links remain intact.

## Evidence and reader behavior

- The AAOI and MU pages clearly identify **Research note** and **Agent-written analysis**; the methodology reference identifies **Methodology note**. Heading hierarchy, paragraphs, citations and table text render readably, including literal dollar amounts.
- The table of contents jumps within the current note and preserves its query parameters. Long headings wrap within the sidebar.
- Clicking AAOI's FY2019 10-K citation opens a separate text-source tab with the retained Item 6 locator, labelled candidate passages, and the recorded original SEC document URL. The ordinary text viewer retains its previous layout and controls.
- The raw-text disclosure opens the complete cached Markdown with its recorded tag/path metadata. The reviewer downloaded the note after the final restart and verified it byte-for-byte against the cached source with `cmp`.
- The builder reports 51 passing focused tests for notes, sources, passage matching and app behavior. The independent reviewer did not repeat that suite; browser interaction and screenshot review were independent.

Captures are under `output/playwright/notes-reader-2026-09-19/`: `page-01.png` through `page-15.png`, `aaoi-top.png`, `mu-top.png`, `filing-regression.png`, and the final focused captures `final-tables-1280.png`, `final-tables-900.png`, `final-table-continuation.png`, `final-search-sidebar.png`, `final-search-result.png`, `final-method-top.png`, and `final-raw.png`. Earlier captures document the issues above. Main-page captures remain valid after the isolated note fixes because those modules were unchanged. The audit server was restarted before checking the final imported note module.

## Version checked (SHA-256)

| File | SHA-256 |
|---|---|
| `app_notes.py` | `eef9396b6cf897e28e78978eb08bfecc57f93bf67e4d49d419f666f0c4867dce` |
| `app_sources.py` | `85fa53b93c17a67fe771c22778965a33902ec4103c0cb263355bd87a9c27f8cc` |
| `tests/test_app_notes.py` | `b7803cc0509296ee7cf2cfc6fe34a204cd6f9d1928e8acdbd6f36c238c1c8aa6` |
| `app.py` | `bd3b482afaa44236a6bde7521cf7aef077ab9dc11fabb273a34162be096edf8a` |
| `app_core.py` | `9674ed083d3279beefbf6928409f7d3da5efa102f470289a80bc0d5843c09913` |
| `app_pages.py` | `1ebf8c2778b04e5ccced8b675682f79429f04fcc0f0c5dee78cc1c3a04a34693` |
| `app_workspace.py` | `f32331a9a93ed614ba926b4a014e02ac06ae279b5461d13908e69a5d6685d18b` |
