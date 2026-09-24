# finance

A library of plain-English company research reports, each with a quarterly receipt of what management promised and delivered, and a Damodaran-style discounted-cash-flow valuation you steer yourself. Agents (Claude Code skills) do the reading and the drafting. You check their work, change the assumptions, and read the result.

[AGENTS.md](AGENTS.md) contains shared boundaries and workflow routing. Detailed requirements live in [focused guides](docs/instruction-map.md), the workflow skills, and each company's source guide. This README explains how to use the repo.

## What you need

- [Claude Code](https://claude.com/claude-code) opened in this folder (the skills live in `.claude/skills/`)
- [uv](https://docs.astral.sh/uv/) and Python 3.12 or newer, for the valuation engine and the app
- Poppler (`pdftotext` and `pdftoppm`) and Tesseract for PDF text and image-only pages; Pandoc for document transcripts. On macOS: `brew install poppler tesseract pandoc`.
- git (the skills commit locally; nothing is ever pushed)
- An internet connection for the research skills (SEC filings, transcripts) and for the engine's market data (Treasury rate from FRED, price from Yahoo, Damodaran's datasets). Before the first research run, put your own email in the SEC User-Agent line in the [sourcing guide](docs/sources.md#section-12-1); the SEC rejects requests without one.

First-time setup:

```
# Run from the repository root, the directory containing AGENTS.md.
uv sync --locked --extra app
```

## The four commands

Type these as slash commands in Claude Code.

| Command | What it does |
|---|---|
| `/research-company GOOGL as of Q2 2026` | Builds a new company from scratch: `business.md` (how the business works, the moat, what could break it) and `outlook.md` (this quarter's guidance and testable claims). Several agents gather filings and transcripts, one writes, one reviews. |
| `/refresh-company MRVL with Q2 FY2027` | Adds a quarter to an existing company: archives the old outlook, grades every claim it made into `scorecard.md`, writes the new outlook, and flags anything in `business.md` that no longer holds. Never re-values. |
| `/draft-valuation GOOGL` | Writes and reviews the valuation assumptions (`valuation/assumptions.yaml`): bear, base and bull stories, ten-year paths, every number with its reason and source. Runs internal diagnostics, then stops for your review before displaying valuation results. Use `--redraft` to prepare a replacement while keeping the active files intact until the candidate passes. |
| `/compute-valuation GOOGL` | Runs the engine on the assumptions, writes `valuation/valuation.md` (results, sensitivities, reverse DCF, diagnostics) and commits. |

Typical order for a new company: research, then draft the valuation, then open the app, then compute.

## Skills and teaching material

The four workflow entrypoints live under `.claude/skills/`. [AGENTS.md](AGENTS.md) owns shared boundaries; skills sequence the work and explicitly load the authoritative guides and method references they need.

| Location | Contents |
|---|---|
| [Research, sourcing and review guides](docs/instruction-map.md) | Report formats, evidence rules, review requirements and legacy section locations. |
| [Research skill](.claude/skills/research-company/SKILL.md) / [Refresh skill](.claude/skills/refresh-company/SKILL.md) | Initial company understanding, quarterly sources and management's receipt; refresh also assesses due analyst forecasts when records exist. |
| [Draft skill](.claude/skills/draft-valuation/SKILL.md) / [Compute skill](.claude/skills/compute-valuation/SKILL.md) | Evidence and assumptions with independent review, followed by owner-requested calculation. |
| [Valuation playbook](.claude/skills/draft-valuation/references/analyst-playbook.md) | Reading map for model selection, accounting, business drivers, uncertainty, review and learning. |
| [Teaching library](tools/valuation/damodaran-notes/README.md) | Cached Damodaran primary texts, source dates/hashes, earlier research and links to practical guides. |
| [Current industry data](tools/valuation/data/damodaran/MANIFEST.md) | Dataset snapshots, distinct from historical teaching examples. |

A valuation draft records how the applicable teachings affected its model choice and input judgments. Peer evidence belongs in the company's quarter source cache, not in the general teaching notes. The model still has capability limits; reading a paper about financial firms does not give the engine an equity-valuation model.

Future passing drafts freeze an analyst-proposal forecast; successful normal computes through the skill freeze a separate owner-compute version. A later refresh compares due targets with sourced actuals in `valuation/forecast-reviews/` and records lessons in `valuation/lessons.md`. The next authorized redraft reads those lessons before choosing inputs. Original forecasts stay unchanged. App-only saves/computes do not automatically create this new learning record yet; old records are used only when provenance and periods can be verified.

## The app: where you change assumptions

```
uv run --extra app valuation-app
```

This opens a local page (it binds to your own machine only). It walks you through the valuation one factor per page, in the order of how much each factor moves the value:

1. Start: pick the company, see the price, risk-free rate and equity risk premium, and a table ranking the factors.
2. The stories: bear, base and bull side by side.
3. Revenue growth, then operating margin, then terminal value, cost of capital, reinvestment, taxes and weights. Each page explains the factor, shows the analyst's proposal and reason for every case, and asks for your number.
4. Facts check: the base year and the balance-sheet bridge, read-only unless you switch on editing.
5. Results: the value per share for every case against the price, with the details in fold-outs.

You set five years of growth and margin per case; the model runs ten, easing years 6 to 10 toward the economy's growth rate by rule, then adds a terminal value. Save writes your changes into the YAML with a dated change log and refreshes the readable `assumptions.md`. Write the report and Record in the repository do what `/compute-valuation` does. Agents treat values you have saved as yours and never overwrite them silently.

Do not edit `assumptions.yaml` by hand. Read `assumptions.md` instead and change numbers in the app.

## Reading a company

Everything for one company sits under `companies/<TICKER>/`:

| File | Read it for |
|---|---|
| `business.md` | The stable understanding: what it sells, how it makes money, the moat, the risks, the indicators to watch. Changes rarely. |
| `outlook.md` | This quarter: results against what management had said, guidance quoted verbatim, testable claims for next quarter. |
| `scorecard.md` | The receipt: every past claim graded hit, miss or not yet, quarter by quarter. |
| `valuation/assumptions.md` | Every valuation input with its reason and working notes. |
| `valuation/valuation.md` | The computed valuation. |
| `review/` | The reviewers' checks, so you can see what was verified and what was fixed. |
| `source-guide.md` | Company-specific fiscal-calendar, source-fetching and disclosure notes; read before gathering. |
| `sources/` | The cached filings and transcripts every number points to. |

Source tags in square brackets, such as `[10-Q Q2 2026, Note 2]`, name the cached file and place behind a number.

## Companies in the library

AAOI, AVGO, GOOGL, INTC, LITE, META, MRVL, MU, NBIS, PINS, RKLB. GOOGL and MRVL also have valuations.

## The engine on its own

```
uv run value GOOGL --dry-run            # compute and print, write nothing
uv run value GOOGL --validate           # check the assumptions file
uv run value GOOGL --diagnostics-only   # draft-review JSON, no valuation results or file writes
uv run value GOOGL --set scenarios.base.sales_to_capital.value=1.5 --dry-run
uv run pytest -q                        # the engine's tests, including exact reproductions of two of Damodaran's workbooks
```

`tools/valuation/README.md` documents the engine's conventions. `tools/valuation/damodaran-notes/` holds the sourced notes on what Damodaran actually does.

## How to give feedback

Say what you do not like about a report, an assumption or the app. Specific feedback fixes the requested artifact within its editing rules. Feedback that changes future practice updates the relevant guide or company note. A separate short lesson is optional when its reasoning will help future work; it links to detailed evidence. See [instruction maintenance](AGENTS.md#maintaining-instructions-and-lessons). Historical feedback is preserved in the [archive](docs/history/2026-09-18-lessons.md).
