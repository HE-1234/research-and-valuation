# Restricted operating diagnostics — scope

The saved draft retains null values for corporate investments and the customer-lease backstop. The normal validation therefore stops every equity-valuation case; that is intentional evidence handling, not a schema failure to be filled with guesses.

For the independent operating review only, the runner used:

```
uv run value companies/AVGO/valuation/assumptions.yaml --diagnostics-only --set bridge.non_operating_assets.0.value=0 --set bridge.other_claims.0.value=0
```

The zeros are temporary neutral placeholders for bridge items that do not affect operating revenue, profit, reinvestment, capital returns or transition checks. They are not estimates, accepted assumptions, or changes to the saved YAML. The explicit market debt/equity build is unchanged. This diagnostic output contains only the repository's restricted allowlist and cannot establish completed equity values. No full valuation output, ordinary dry run, valuation.md or passing forecast record has been produced.

`FY2026-Q2-diagnostics-initial-operating-only.json` contains this operating review output. Exact final input hash and review status are recorded after final checks. A subsequent numerical revision requires regenerating these diagnostics before they can be treated as current.

## Pass 1 finding

The non-bear transition flags are caused by terminal ROIC being below half of final-year book ROIC, not by a cash-flow drop exceeding 15%. All first-pass cash-flow drops are below that threshold. Independent review nevertheless found the funding change economically unsupported: central net reinvestment jumps from 5,632 to 18,247 with little change in growth, margin or tax. The generic engine warning is not a substitute for this diagnosis. See the preserved pass-1 review and inputs.

## Revised draft: current status

The revised input SHA-256 is `02ed91bdefb6256c38b600829a015ae2ccc686c646724412aeae1442bc77ea6a`. All four late sales-to-capital inputs and reinvestment overrides for years 6–10 are now null, in addition to the two unresolved bridge items. `FY2026-Q2-valuation-validation.txt` and the unmodified restricted run in `FY2026-Q2-diagnostics-current.txt` both exit 1 and stop every case, as intended.

The previous conditional JSON has been renamed `FY2026-Q2-diagnostics-initial-operating-only.json` and is also preserved with the exact rejected inputs in `FY2026-Q2-valuation-pass1/`. It is historical review evidence, not diagnostics for the revised active draft. No temporary values have been filled into the revised late-capital inputs merely to generate a result.
