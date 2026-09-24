# Citation passage highlights — independent audit

Status: PASS for the reviewed code, focused tests, and supplied desktop captures. Browser interactions were run by the root agent; capture inspection and focused tests were independent.

## Scope and method

The independent reviewer inspected the citation renderer, read-only source view, passage matcher, source-table integration, and focused tests. The root agent runs the browser and supplies captures; this reviewer independently inspects those files and does not attribute browser interactions to itself. No company assumptions or implementation code were edited by this reviewer.

## Code findings

- Source requests still require an exact recorded path in the chosen company's source index. Peer files and method notes are available only when recorded; unknown and escaped paths are rejected. Citation query arguments are URL-encoded and capped, and bare cached-file links omit a quote or locator.
- Exact quote previews use literal wording with normalized whitespace. The preview carries offsets into the original cached text. The renderer escapes every source-text character before adding fixed highlight markup; an HTML-in-source regression covers this boundary.
- Item, Note, section, PDF-page and speaker-turn locators produce bounded previews only when recognizable structure survives extraction. Ambiguous body headings are presented as candidates. A bare `p.N` does not assume a PDF-page number unless the recorded source note explicitly defines that convention. Captions identify a broad locator as a location, not proof of a claim, and warn when a quote occurs outside its cited location.
- The source viewer offers manual exact-phrase search, the original-document link when recorded, cached-text download, and the full cached document. A citation without a usable quote or locator gets a clear search/full-text fallback. It does not claim to locate every bare citation in ordinary reason prose.

## Independent checks

- `.venv/bin/python -m pytest -q tools/valuation/tests/test_source_passages.py tools/valuation/tests/test_app_sources.py tools/valuation/tests/test_app.py`: 46 passed on the latest matcher revision.
- Following the generated links for all 26 real AAOI management guidance rows into the recorded cache yielded 12 exact-quote previews and 14 broader locator previews. No row was unlinked or unavailable. A separate real AAOI Item 8 citation resolved to a body marker, speaker paragraphs 4/11 produced two markers, and a bare release citation returned the explicit unavailable/search fallback.
- An independent Streamlit AppTest opened a real AAOI source view, entered an exact phrase in the manual search box, and observed a highlighted result with no app error. The focused test also checks that the source view contains no number inputs and leaves the assumptions file unchanged.
- The root agent reports the final full suite at 253 passed, one optional test skipped. This broader suite was not rerun by the independent reviewer. The reviewer separately ran `git diff --check` successfully.

## Visual review

The reviewer inspected `output/playwright/passage-highlights-2026-09-17/page-01.png` through `page-15.png` at 1280 × 720. All 15 destinations show a clear selected navigation item, heading, primary action/content, and consistent typography. No new overlap, horizontal clipping, raw markdown, or traceback is visible. The raw-decimal model warnings visible on Model checks predate this citation change.

- `quote-viewer.png`: a direct guidance citation opens the recorded release with the exact USD 255–290 million text highlighted within the opening viewport. The card is readable, and original-document/download controls remain available.
- `multiple-passages.png` and `second-passage.png`: an actual AAOI call citation with speaker paragraphs 4 and 11 shows both separate preview cards and highlights the speaker labels. The caption says these broader locations do not verify the particular claim. The second card and full-document disclosure remain readable when scrolled.
- `manual-search.png`: the entered exact phrase and its highlighted search result are visible together. `document-only.png`: a bare citation clearly explains the lack of an exact passage and offers search plus the full cached source.

The screenshots are viewport samples, not every scroll position or mobile width. The reviewer did not independently operate the browser or test third-party original-document reachability. Unknown or ambiguous passage identity is handled with labelled candidates or an explicit fallback; only a recorded quote or manually entered exact phrase yields an exact-text finding.

## Version checked (SHA-256)

- `app_sources.py`: `c03f90de56e744e66827c94de36b52ab82d4d36869b79cb5cad8018ce1104a1f`
- `source_passages.py`: `2bd80b1b104b0d42954ae6ae063e1099fe9a602474b481cd1b59fa0eb8f0ee9b`
- `app_core.py`: `9674ed083d3279beefbf6928409f7d3da5efa102f470289a80bc0d5843c09913`
- `app_pages.py`: `1ebf8c2778b04e5ccced8b675682f79429f04fcc0f0c5dee78cc1c3a04a34693`
- `app.py`: `bd3b482afaa44236a6bde7521cf7aef077ab9dc11fabb273a34162be096edf8a`
- `tests/test_source_passages.py`: `9bf002dffd8a6e132c6a559ea027895ec2d0f2d869e811e0c91193e917d66991`
- `tests/test_app_sources.py`: `db8d008d5b74b3b1c6af815dc8a6d6e92f7af758661831a449e92df134bed7a6`
- `tests/test_app.py`: `1b071ab83c394dde87e4eff2b7cc95352741fef3a901ee54374d0301b45a7777`
- `quote-viewer.png`: `35e4d39ca0a762690d7d9e5971b54e12335143c83bc73a1a873228e44c2c81b5`
- `multiple-passages.png`: `4929817a20932bf1dfd8062ed45b12e5153a82077f201030692bcfc2fa78b7bd`
- `manual-search.png`: `e3b4ebc217d56b57171ef5d3553835e27746cf648917e0535cd54dacf5fc01f3`
- `document-only.png`: `582324a48c80966ee2406b8bc80f0476e989dab1b594aab57ea89a8fe221e43a`
