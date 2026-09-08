# finance

A library of plain-English company research reports, each with a quarterly receipt of what management promised and delivered, and a Damodaran-style discounted-cash-flow valuation you steer yourself. Agents (Claude Code skills) do the reading and the drafting. You check their work, change the assumptions, and read the result.

`AGENTS.md` is the full specification of how every file here is produced, refreshed and reviewed. This README only tells you how to use the repo.

## What you need

- [Claude Code](https://claude.com/claude-code) opened in this folder (the skills live in `.claude/skills/`)
- [uv](https://docs.astral.sh/uv/) and Python 3.12 or newer, for the valuation engine and the app
- git (the skills commit locally; nothing is ever pushed)
- An internet connection for the research skills (SEC filings, transcripts) and for the engine's market data (Treasury rate from FRED, price from Yahoo, Damodaran's datasets). Before the first research run, put your own email in the SEC User-Agent line in `AGENTS.md` §12.1; the SEC rejects requests without one.

First-time setup:

```
cd finance
uv sync --extra app
```

## The four commands

Type these as slash commands in Claude Code.

| Command | What it does |
|---|---|
| `/research-company GOOGL as of Q2 2026` | Builds a new company from scratch: `business.md` (how the business works, the moat, what could break it) and `outlook.md` (this quarter's guidance and testable claims). Several agents gather filings and transcripts, one writes, one reviews. |
| `/refresh-company MRVL with Q2 FY2027` | Adds a quarter to an existing company: archives the old outlook, grades every claim it made into `scorecard.md`, writes the new outlook, and flags anything in `business.md` that no longer holds. Never re-values. |
| `/draft-valuation GOOGL` | Writes the valuation assumptions (`valuation/assumptions.yaml`): bear, base and bull stories, ten-year paths, every number with its reason and source. A reviewer checks it. Computes nothing; it stops so you can review the inputs first. Use `--redraft` to redo an existing draft. |
| `/compute-valuation GOOGL` | Runs the engine on the assumptions, writes `valuation/valuation.md` (results, sensitivities, reverse DCF, diagnostics) and commits. |

Typical order for a new company: research, then draft the valuation, then open the app, then compute.

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
| `sources/` | The cached filings and transcripts every number points to. |

Source tags in square brackets, such as `[10-Q Q2 2026, Note 2]`, name the cached file and place behind a number.

## Companies in the library

AAOI, AVGO, GOOGL, INTC, LITE, META, MRVL, MU, NBIS, PINS, RKLB. GOOGL and MRVL also have valuations.

## The engine on its own

```
uv run value GOOGL --dry-run            # compute and print, write nothing
uv run value GOOGL --validate           # check the assumptions file
uv run value GOOGL --set scenarios.base.sales_to_capital.value=1.5 --dry-run
uv run pytest -q                        # the engine's tests, including exact reproductions of two of Damodaran's workbooks
```

`tools/valuation/README.md` documents the engine's conventions. `tools/valuation/damodaran-notes/` holds the sourced notes on what Damodaran actually does.

## How to give feedback

Say what you do not like about a report, an assumption or the app. The fix goes into `AGENTS.md`, usually as a new rule and a dated line in §17 (the lessons log), so the next run does not repeat the mistake.
