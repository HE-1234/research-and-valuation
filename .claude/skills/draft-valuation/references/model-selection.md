# Choose a model that fits the business

Read before a new draft or redraft. Record the decision in `sources/<QLABEL>/notes-valuation-evidence.md`; the reviewer checks it before judging numerical inputs. [§18.11](model-spec.md#section-18-11) governs the capability boundary.

## Primary teachings

Financial companies often require direct equity valuation because debt is part of operations and ordinary definitions of reinvestment are difficult to apply. Regulatory capital can be the investment needed to grow. See [financial-firms.txt](../../../../tools/valuation/damodaran-notes/sources/financial-firms.txt), sections “Debt and Equity” and “Equity versus Firm Valuation”.

Cyclical and commodity businesses require a view of normalized economics across a cycle; current earnings may be an unsuitable long-run anchor. Normalization must also account for changes in company size and operations. See [cyclical-companies.txt](../../../../tools/valuation/damodaran-notes/sources/cyclical-companies.txt), “Normalized Earnings” and discussion of commodity-price assumptions.

Declining businesses need not return to growth, and distressed firms may not survive to earn a terminal value. Going-concern and failure outcomes must be distinguished. See [decline-and-distress.txt](../../../../tools/valuation/damodaran-notes/sources/decline-and-distress.txt), sections on negative growth, divestitures and distress. These are 2009 papers; their numerical examples are historical.

## Apply to this repository

| Business or condition | Decision to make | Current engine boundary |
|---|---|---|
| Operating company with identifiable revenue, operating profit and reinvestment | Explain why FCFF represents its economics and which parts differ. | Standard FCFF is supported. |
| Bank, insurer, broker or mixed financial platform | Determine whether funding is an operating input and what regulatory capital buys growth; do not classify solely by ticker or industry label. | No dedicated FCFE, dividend or excess-equity-return model. A material need for one blocks the dependent standard-engine valuation. |
| Cyclical business | Show reported TTM, a sourced through-cycle comparator and an explicit transition. Separate cycle recovery from a structural change. | Explicit growth/margin paths are supported; the engine does not discover normalized earnings. Keep reported base facts intact. |
| Young or distressed business | Explain cash runway, external funding assumptions, failure horizon and recoveries by claimholder. | The existing failure probability and asset-proceeds adjustment are limited; no funding-round simulator or full creditor waterfall. |
| Shrinking business | Assess capacity release, asset-sale recoveries and remaining economic life. | Negative growth is allowed, but the ratio mechanically releases capital. Verify realizable proceeds; do not assume every lost dollar of sales recovers book capital. |
| Mixed businesses or currencies | Check whether one margin, capital ratio and risk build obscure material differences. | No native sum-of-parts or multi-currency engine. Use a defensible consolidated treatment only when the evidence supports it. |

The evidence note records: classification; suitable valuation approach; why this engine can or cannot express it; allowed input/override treatment; material unresolved limitation. A successful schema validation does not answer model suitability. Inspect the current engine when a capability matters; the table is a guide, not a promise about future versions.

If unsupported, complete the source research and explain the required method and missing capability. Do not shoehorn values into unrelated fields, implement a new valuation engine implicitly, or ask for approval to perform routine supported work. Report only the dependent valuation as blocked; research can remain useful.
