# Marvell Technology, Inc. (MRVL) — Reviewer report, Q2 FY2027 (quarter ended early August 2026)

_Refresh review. As-of cutoff 2026-08-28; nothing after that date was used. Written 2026-09-07._

**Verdict: REVISE** (light). No ✅ or ❌ in the scorecard is wrong. Every number in the scorecard, the outlook §1 table, the §4 guidance table and the seven flags was verified against the cached full texts; every quote checked is verbatim. What must change: outlook.md §6 lists "China" and "any competitor by name" as things management *stopped* saying, but the Q1 call never said them either (0 hits in `sources/FY2027-Q1/transcript.txt`; business.md §6 item 7 says so in as many words); §5 claim 4 uses a 10% decline as the floor for "low to mid-teens", which could produce a wrong ✅ next quarter; §5 claim 12 needs one line of arithmetic to be gradeable if the Q3 10-Q reports only a total vested count. One verdict (claim 6) is a judgment call where I would grade ✅ and the writer graded 🟡; that is not a must-change.

---

## 1. Blind re-grade of the twelve Q1 FY2027 §5 claims

Graded before opening `scorecard.md`, strictly and literally, against `sources/FY2027-Q2/`. One line of evidence each.

| # | Claim (Q1 outlook §5, abridged) | My verdict | Evidence | Writer | Agree? |
|---|---|---|---|---|---|
| 1 | Q2 revenue $2.565B–$2.835B | ✅ | "Net revenue for the second quarter of fiscal 2027 was $2.739 billion" [Q2 FY2027 release] | ✅ | Yes |
| 2 | Q2 non-GAAP GM 58.25%–59.25% | ✅ | "Non-GAAP gross margin \| 58.9%" in the reconciliation table [Q2 FY2027 release] | ✅ | Yes |
| 3 | FY2027 guidance stays "approximately 40%" / "nearly $11.5 billion" or higher | ✅ | "grow approximately 45% year-over-year to roughly $12 billion, up from our prior outlook of approximately $11.5 billion" [Q2 FY2027 call]; slide p.8 same [Q2 FY2027 slides, p.8] | ✅ | Yes |
| 4 | Q3 guidance midpoint ≥ $3.0B | ✅ | "Net revenue is expected to be $3.150 billion +/- 5%." [Q2 FY2027 release] | ✅ | Yes |
| 5 | Interconnect FY2027 target remains ">70%" or is raised | 🟡 | No percentage restated anywhere (call, release, deck p.8/p.18). Asked directly for updated connectivity growth rates (Schneider), the CEO gave direction only: optical DSPs into the scale-out transceiver market are "upsized versus the prior growth rates we talked about" [Q2 FY2027 call]. | 🟡 | Yes |
| 6 | Scale-out switch FY2027 target of >$600M is reiterated | ✅ (judgment call) | "Within scale-out switching, our business remains on track to more than double this year" [Q2 FY2027 call]; "Scale-out switching on track to more than double in FY27" [Q2 FY2027 slides, p.18]. Q1 defined the target as "exceed $600 million, doubling from fiscal 2026" [Q1 FY2027 call], so "remains on track to more than double" reaffirms the same target; only the dollar figure went unspoken. | 🟡 | **No** — see §2 |
| 7 | TIA/driver $1B run rate restated (or reached) | ✅ | "broadband analog TIAs and drivers, scale-across DCI modules and scale-out switching. Each of these 3 businesses is on or ahead of the trajectory towards the $1 billion annualized revenue run rate we highlighted last quarter." [Q2 FY2027 call] | ✅ | Yes |
| 8 | FY2028 ~$16.5B reiterated or raised, not cut | ✅ | "we now expect fiscal 2028 revenue of approximately $18 billion, up $1.5 billion from the $16.5 billion outlook we provided just 1 quarter ago." [Q2 FY2027 call]. Q1 claim wording "reiterated or raised, not cut" is satisfied by a raise. | ✅ | Yes |
| 9 | Tier-1 XPU program again described as on schedule toward volume production | ✅ | Asked about "the other large XPU program that you're planning to start in the next year" (Arya), CEO: "That new program is clearly part of that"; "we continue to make progress every quarter, not only on design execution, but also supply commercials"; "it certainly is tracking, and we feel very good about next year" [Q2 FY2027 call]. "Tracking" = on schedule; "next year" = the FY2028 volume ramp named in Q1 [Q1 FY2027 call]. Sufficient; note the program is identified by the analyst's framing, which the CEO adopted. | ✅ | Yes |
| 10 | Q2 10-Q shows first capacity deposit/prepayment installments paid | ✅ | "Prepayments on supply capacity reservation agreements \| 487.0 \| 278.8" (Aug 1, 2026 vs Jan 31, 2026) [10-Q Q2 FY2027, Note 14]; $263.1M at May 2, 2026 [10-Q Q1 FY2027, Note 14], so +$223.9M in the quarter (computed); "The increase in prepaid expenses and other assets was primarily due to payments made for capacity fees." [10-Q Q2 FY2027, Item 2]; CFO: operating cash flow "down slightly quarter-over-quarter, primarily reflecting the higher capacity prepayments to suppliers" [Q2 FY2027 call]. Both numbers verified; claim satisfied. | ✅ | Yes |
| 11 | Celestial earn-out ≥ $647.6M | ✅ | "Balance at August 1, 2026 \| $ \| 749.5" [10-Q Q2 FY2027, Note 6] | ✅ | Yes |
| 12 | Distributor A ≥ 45% of revenue | ❌ | "Distributor A \| 44% \| 34% \| 45% \| 35%" = three months ended Aug 1, 2026; Aug 2, 2025; six months ended Aug 1, 2026; Aug 2, 2025 [10-Q Q2 FY2027, Item 2]. The Q1 reference row "Distributor A \| 45% \| 36%" was the three-month figure (a Q1 10-Q has only three-month columns), so the claim refers to the quarter: 44% < 45%. The six-month 45% does not rescue it. | ❌ | Yes |

**Blind tally: 10 met, 1 missed, 1 partial, 0 not yet, 0 dropped. Writer's tally: 9 / 1 / 2 / 0 / 0.** The one-claim difference is claim 6.

## 2. Disagreements (one per line, then the §9 reasoning)

- **Claim 6.** Writer 🟡, reviewer ✅. §9 🟡 is "directionally happened but short of the stated level, or only part of it happened." Nothing fell short and nothing was only partly reaffirmed: management said the business "remains on track to more than double this year", which is the target exactly as management defined it last quarter ("exceed $600 million, doubling from fiscal 2026"), and added that switching is "biasing higher this year." The only thing absent is the words "$600 million." §9 ✅ ("happened as stated") fits better. The writer's reading (the claim names a dollar figure, the dollar figure was not said) is a defensible strictly-literal position and is not in the wrong-✅/❌ class, so this is a recommendation, not a must-change. If changed: tally becomes 10 / 1 / 1 / 0 / 0 and the "Verdict counts" line must follow. Lesson for claim-writing either way: state a target in the form management uses ("more than double") so next quarter's check needs no inference.
- **Claim 5, confirmed 🟡 not 🔇.** 🔇 requires "management stopped talking about it and disclosed nothing that lets you check." Neither holds: the question was asked and answered with a direction ("upsized versus the prior growth rates we talked about"). Not ✅ because the target itself (">70%" for interconnect) was neither restated nor explicitly raised; "upsized" was said of optical DSPs into the scale-out transceiver market, a part of interconnect. The writer's evidence line already cites the Schneider exchange, which is the right evidence.
- **Claims 8, 9, 10, 12.** Agree with the writer; see the table for the wording checks the coordinator asked for. Claim 10: both balance-sheet numbers ($263.1M at May 2, 2026 in the Q1 10-Q Note 14; $487.0M at Aug 1, 2026 in the Q2 10-Q Note 14) and the MD&A attribution are in the full texts. Claim 12: table values confirmed; wording refers to the quarter.

## 3. Scorecard format and tally (§10)

- Title, running-tally table (quarter graded | met | missed | partial | not yet | dropped), indicator time series (one row per indicator, newest column on the right), grading section headed "Q2 FY2027 (grading claims made in Q1 FY2027)" with claim | verdict | evidence: **all present and in §10 order.** Sources list maps every tag.
- Fiscal parenthetical on first use: "Q2 FY2027 (quarter ended early August 2026)" in the tally row. Yes.
- Tally arithmetic: table has ✅ on 1, 2, 3, 4, 7, 8, 9, 10, 11 (9), 🟡 on 5, 6 (2), ❌ on 12 (1). Matches 9 / 1 / 2 / 0 / 0.
- Every ✅ and ❌ has an evidence line whose tag supports it; I checked each quote against the full text (release lines 15, 23, 205–210, 319–327; transcript paragraphs at lines 27, 31, 37, 61, 71, 73, 119–123; 10-Q lines 509, 751, 863, 1024; slides p.8, p.18). No failures.
- Indicator time series numbers: Q4 FY2026 $1,651.3M / 74% [supplemental p.10 ✓]; Q2 $2,171.5M / 79% ✓; 58.9% ✓; 44% / 16% ✓; $8,518.9M ✓; $487.0M / $263.1M ✓; $749.5M ✓; $647.6M ✓; $315.8M (Q1 10-Q) ✓. Row 3 and 4 quotes verbatim ✓.
- Note for the owner: the scorecard states that business.md §8 is still marked "Proposed" and was used as-is. Correct behaviour under §8; the owner should lock the set (or accept the writer's flag 7 proposals) so the time series stays comparable.

## 4. Outlook.md checks

**(a) Skeleton and header.** §1–§6 plus Sources, all present, in §7 order; §6 Tone shift present. Header "# Marvell — Outlook as of Q2 FY2027 (quarter ended early August 2026)" carries the §5 parenthetical; source-tier line and date present. Nit: business.md and the Q1 outlook say "Marvell Technology, Inc."; the new outlook and scorecard say "Marvell". Not a §7 violation.

**(b) §1 indicators table.** Same eight indicators as business.md §8, same order. Every number verified: $2,171.5M / 79% / +18% [release]; $1,832.7M / 76% [release, May 2 column]; 58.9% / 58.9% [release]; "58.25% to 59.25%" [Q1 release]; 44% / 16% and 45% / 16% [10-Q Q2 Item 2; 10-Q Q1 Item 2]; $8,518.9M, $487.0M [10-Q Q2 Note 9; Note 14]; $2,756.8M, $870.0M, $263.1M [10-Q Q1 Note 9; Note 14]; $749.5M / $647.6M [Note 6 each]. "Mid to high teens sequentially" [Q1 call] ✓. Row 4's Q2 cell omits the "upsized versus the prior growth rates" quote that the scorecard uses; consistency suggestion, not an error.

**(c) §4 quotes, word for word.** All 26 quoted fragments checked against `press-release.txt` (lines 23–39) and `transcript.txt` (lines 27, 29, 31, 35, 57, 75, 77, 79, 81, 83, 205–209). All verbatim. The writer's note that the Q3 figures come from the release because the transcript garbles the share count ("$900 million") and the gross-margin sentence is accurate: the transcript reads "creating the sequential headroom in the fiscal third quarter -- the sequential headwind in the fiscal third quarter"; the writer's ellipsis quote keeps only the corrected phrase, which is the right treatment. Release wording confirmed for every Q3 figure.

**(d) §5 claims.** Twelve claims, each one sentence, one observable, single direction. Arithmetic: 3.150 × 0.95 / 1.05 = $2.9925B / $3.3075B ✓; 2,171.5 × 1.20 = $2,605.8M ✓; 567.8 × 0.90 = $511.0M ✓ (but see below). Quotes verbatim ✓. Two need sharpening:
- Claim 4: management said "decline in the low to mid-teens percentage range"; 10% is not teens. As written, a 10.5% decline would be graded ✅ against words management missed. Use 13% (below $494.0M; 567.8 × 0.87 = 493.99) or at minimum 11% (below $505.3M).
- Claim 12: the Q2 10-Q reports vested warrant shares as a total (Note 3: "A total of 1.2 million Fiscal 2025 Warrant Shares were vested"), not split between time-based and performance vesting. Add the arithmetic from the 8-K so the Q3 grader can do it without judgment: time-based 1,360,867 shares vest "in equal quarterly installments during the first year" ≈ 340,217 per quarter; the remaining 57,610,040 shares vest in 240 equal tranches ≈ 240,042 shares each; a disclosed vested count above ≈340,000 implies at least one performance tranche [8-K 2026-08-19].
- Claim 10 (Investor Day replaces the 38%–40% target) is gradeable only if the Q3 refresh fetches the October 6, 2026 Investor Day materials; note that for the gatherer.

**(e) §6 Tone shift.** Table rows: interconnect (Q1 slides p.7 "led by interconnect revenue, which is expected to grow >70% y/y" ✓; Q2 deck p.8 has no percentage ✓); scale-out switching (Q1 slides p.14 ✓; Q2 slides p.18 ✓); custom (Q1 p.14 ✓; Q2 p.18 "Expect custom business to grow >2x y/y in FY28" ✓, FY2027 percentage absent ✓); TIAs/DCI (Q1 call line 52 "line of sight to a $1 billion annualized revenue during fiscal 28" ✓); buybacks (Q1 call line 94 "we plan to continue to repurchase shares to manage dilution" ✓; Q2 "we intend to continue repurchasing shares to manage dilution" ✓; 10-Q Part II Item 2 monthly table: 1.1M at $176.24 May 3–30, none May 31–Aug 1 ✓); gross-margin driver (Q1 line 86 ✓; Q2 Durn ✓); capacity (Q1 Koopmans line 168 ✓; Q2 Koopmans listed but silent ✓). Scale-up optics row: the Q1 transcript has the figure directly (line 180: "we are effectively calling at this point to be about $300 million"), so the Q1-side tag has been corrected to [Q1 FY2027 call] (see Fixed directly).
"Your math is not wrong": quoted accurately (transcript line 165) and correctly attributed to the CEO answering the Melius analyst, who supplied the "$120 billion ... divided by 6.5" arithmetic (JPMorgan had earlier supplied "$120 billion in cumulative revs over 6 years"). The writer frames it as "analysts' arithmetic", which is right; the $120B in §3 is the writer's own computation from the 8-K (240 × $500M), correctly labelled computed. Optional: name the analyst so no reader thinks management said $120B.
"Stopped saying": "moderate into the 30%-plus range" ✓ (Q1 line 22, absent in Q2) and "CapEx" ✓ (Q1 lines 22 ×2 by the CEO; zero in Q2) are genuine. **"China" and "any competitor by name" are not shifts**: the Q1 transcript has zero occurrences of China, tariff, export, Broadcom or competitor (management), and business.md §6 item 7 already records that "The Q1 call did not mention export controls, China or tariffs." On the Q2 call the only "competitors" is an analyst's word (line 115) and NVIDIA is named as a partner (line 47). This is interpretation dressed as observation and must be removed or reworded ("still unmentioned on either call, yet 42% of Q2 revenue shipped to China…"). The 42% / 29% figures themselves are correct [10-Q Q2 FY2027, Note 3, line 324].
"Changed cash": $326.2M / $207.6M / $153.6M [supplemental p.5 line 137 ✓]; $190.1M [10-Q Note 10 line 630 ✓]; $8,518.9M − $2,756.8M = $5,762.1M ✓.

**(f) Jargon and banned words.** Warrant explained in plain words ("a contract giving its holder the right to buy shares at a fixed price for a set period"), vesting glossed ("becoming usable"), tranche glossed ("slices"), TPU glossed, DCI glossed, run rate glossed, NPO/CPO glossed. "Hyperscaler" is not glossed in outlook.md but is in business.md §1. Banned-word sweep outside quotes (leverage, synergy, headwind, tailwind, monetize, ecosystem, at scale, robust, unlock, TAM): none. "Headwind" and "ecosystem" appear only inside verbatim quotes. Paragraph density: §3 custom paragraph carries nine figures in three sentences (58,970,907; $206.58; Aug 18, 2033; 240; $500M; $120B; 6.7%; 876.9M; FY2033); rule 5 suggests a four-row table.

**(g) Word count** (prose excluding tables, headings, sources list, tags). Script result: 1,196 words excluding the italic header line; 1,205 including it. Writer reported 1,204. At the ceiling either way; any additions from the REVISE list must be offset by trims.

## 5. Flags (seven blocks prepended to business.md)

`git diff HEAD -- companies/MRVL/business.md`: 14 added lines at the top, 0 deletions; body byte-identical to the committed version. Archive check: `quarters/FY2027-Q1-outlook.md` is identical to `HEAD:companies/MRVL/outlook.md`.

| Flag | Supported by cited source? | Right section? | Notes |
|---|---|---|---|
| 1 Google agreement and warrant | Yes: 8-K 2026-08-19 (July 29, 2026 agreement; Aug 18, 2026 warrant; 58,970,907 at $206.58; one tranche per $500M through FY2033); 10-Q cover 876.9M; Note 15 Subsequent Event; 6.7% computed ✓ | §5, §6, §7 ✓ | The only place the counterparty is named is the 8-K; the 10-Q says "a customer". Correctly stated. |
| 2 CFO change | Yes: 8-K 2026-06-11 Item 5.02 (effective June 15, 2026; "not the result of any disagreement"; Adobe, Applied Materials, NXP, GlobalFoundries) ✓; Saran retiring April 2027 [Q2 call] ✓ | §7 ✓ | business.md §7 says Meintjes is CFO; flag warranted. |
| 3 Foundry commitments $8,518.9M; deposits no longer itemized; prepayments $487.0M | Yes: Note 9 table and "supply capacity reservation payment commitments" wording ✓; 0 hits for "870.0" in Q2 10-Q ✓; Note 14 ✓; Q1 Note 9/Note 14 ✓ | §3, §8 ✓ | Indicator-7 redefinition proposal is sensible. |
| 4 SBC $326.2M | Yes: supplemental p.5; Note 13 line 710; Note 10 $190.1M ✓; $590.8M FY2026 matches business.md §4 table ✓ | §3, §4 ✓ | |
| 5 Buybacks | Yes: Part II Item 2 table (1.1M at $176.24 May 3–30; none after); $5.1B remaining; "we intend to continue repurchasing shares to manage dilution" ✓ | §7 ✓ | Flag states facts, not the word "pause". Warranted. |
| 6 Celestial earn-out $749.5M | Yes: Note 6 ($647.6M → $749.5M; 22.4M shares); cash-flow statement $101.9M and $(49.9)M; Item 1A "24.4 million additional shares" (line 1253) ✓ | §6 ✓ | The 22.4M vs 24.4M discrepancy is real and worth the owner's attention. |
| 7 Indicator proposals | Yes: 8-K; Note 3 vested-count precedent; targets not restated [Q2 call; slides p.18] ✓ | §8 ✓ | |

Missing flags: none material. **China 42%**: the writer's reasoning holds. business.md §6 item 7 already gives a Q1 ship-to figure (44%); 42% neither contradicts it nor changes the picture, and the Q2 call again said nothing about China, exactly as §6 item 7 describes. A flag is for statements now wrong or materially incomplete; this is neither. FYI only: the Q2 10-Q risk factors add one new sentence ("In July 2026, bipartisan AI oversight legislation was introduced…", line 1091); §6 item 7 lists risk-factor wording changes as an early warning, but this one concerns AI oversight, not export controls, so no flag. Also checked and found not flag-worthy: receivables concentration (three customers 75% → four customers 72%), distributor share (51% → 50%), shares outstanding (875.6M → 876.9M, covered by flag 1). No flag is unwarranted.

## 6. Rubric (§14), outlook.md read with business.md

1. What it does and who pays: **Yes.** §2–§3 plus business.md §1; the Google agreement now gives the custom buyer a name.
2. What would kill it and the early warning: **Yes.** §3 tells (warrant tranches, FY2028 "more than double", Q3 gross margin) and §6 gross-margin cause map onto business.md §6 items 1–3.
3. Why margins are what they are: **Yes.** §6 "Gross margin now has a stated cause" (custom mix, Q3 range below Q2) confirms business.md §3's inference, and says so.
4. Predict next quarter's scorecard from §5 alone: **Yes**, for 10 of 12 mechanically; claims 4 and 12 need the sharpening in §4(d) to be judgment-free.
5. Nothing requiring knowledge the reader lacks: **Yes**, with "hyperscaler" relying on business.md §1.

## 7. Verdict: REVISE — what must change

1. **outlook.md §6 "Stopped saying".** Delete "China" and "any competitor by name" as stopped-saying items, or reword them as things neither call mentioned. Evidence: 0 occurrences of China/tariff/export/Broadcom/competitor in `sources/FY2027-Q1/transcript.txt`; business.md §6 item 7. Keep "30%-plus" and "CapEx", which are genuine Q1-only statements. The 42% / 29% China sentence may stay if reframed.
2. **outlook.md §5 claim 4.** Replace the 10% floor with 13% ("below $494.0 million, computed: 13% below $567.8 million") or at minimum 11% ($505.3M), so the claim cannot be ✅ when management's "low to mid-teens" was missed.
3. **outlook.md §5 claim 12.** Add the one-line arithmetic (≈340,217 time-based shares per quarter; ≈240,042 shares per performance tranche; therefore a vested count above ≈340,000 implies a performance tranche) with the [8-K 2026-08-19] tag, so the Q3 grader does not need judgment if the 10-Q reports only a total.
4. **Word count.** After items 1–3, keep prose at or under 1,200 by the AGENTS.md definition (now 1,196 / 1,205 depending on the header line); item 1 removes words, items 2–3 add a few.

Recommended, not required (writer's call; note the decision in the second pass):
- Scorecard claim 6: 🟡 → ✅ per §2 above; if changed, tally to 10 / 1 / 1 / 0 / 0 and the "Verdict counts" line. If kept at 🟡, no other change needed; the evidence line already explains the reasoning.
- §3 custom paragraph: move the warrant terms (shares, price, expiry, tranche size and count) into a small table.
- §1 row 4 and §3 interconnect: add the "upsized versus the prior growth rates we talked about" quote so the outlook and scorecard say the same thing.
- §6 "your math is not wrong": say the Melius analyst did the "$120 billion divided by 6.5" arithmetic.
- Title: "Marvell Technology, Inc." in outlook.md and scorecard.md, matching business.md.
- Gatherer note for Q3: fetch the October 6, 2026 Investor Day materials or claims 6 and 10 cannot be graded.

## Fixed directly (no verdicts, numbers, quotes, claim wording, flags, tally or business.md touched)

1. outlook.md §6 tone table, "Scale-up optics FY2028" row, Q1 column: tag `[Q2 FY2027 call, restating Q1]` → `[Q1 FY2027 call]`. The Q1 transcript (line 180) contains the quoted words "about $300 million" directly, so the correct tag was unambiguous.

No typos found in scorecard.md or outlook.md. No page numbers wrong (Q1 slides p.7, p.14; Q2 slides p.4, p.8, p.18; supplemental p.5, p.10 all confirmed against footer numbers). No missing tags other than the one above.

## Sources checked

`sources/FY2027-Q2/`: `10-Q-FY2027-Q2.txt` (cover l.35; Note 3 l.324, 349–351; Note 6 l.485–509; Note 9 l.595–616; Note 10 l.630, 797–798; Note 13 l.710; Note 14 l.751; Note 15 l.800; Item 2 l.860–863, 1024; Item 1A l.1091, 1253; Part II Item 2 l.1396–1404), `transcript.txt` (full), `press-release.txt` (full), `slides.txt` (full), `supplemental.txt` (l.137, 283, 291), `8-K-2026-06-11.txt` (Item 5.02, Exhibit 99.1), `8-K-2026-08-19.txt` (full). `sources/FY2027-Q1/`: `transcript.txt` (l.20, 22, 52, 58, 70, 86, 94, 168, 180; keyword sweeps), `slides.txt` (p.7, p.14), `10-Q-FY2027-Q1.txt` (Note 9 l.1029; Note 14 l.1267; l.1681).

## Cycle 2 (re-check of the writer's second pass; review cycle 2 of 2)

Focused re-check of `scorecard.md`, `outlook.md` and the business.md flag blocks against the cached sources. As-of cutoff 2026-08-28 respected; no new sources used.

### 1. Status of the must-change items and adopted recommendations

| Item | Status | Check |
|---|---|---|
| Must 1: §6 "Stopped saying" China / competitors | **Resolved** | Competitors removed entirely. China reframed as "Never said on either call: China, which took 42% of Q2 shipments against 29% a year earlier, mostly for non-China customers' factories" — Q1 and Q2 transcripts both have zero China mentions; 42% / 29% match 10-Q Note 3 (line 324: "China \| $ \| 1,161.5 \| 42 % \| ... \| 583.4 \| 29 %"); "non-China customers' factories" matches line 330. "30%-plus" and "CapEx" kept, both genuinely Q1-only. |
| Must 2: §5 claim 4 threshold | **Resolved** | "below $494.0 million (computed: 13% below $567.8 million, the low end of 'low to mid-teens')": 567.8 × 0.87 = 493.99. Quote verbatim. |
| Must 3: §5 claim 12 arithmetic | **Resolved** | Added with [8-K 2026-08-19] tag; figures correct (see §3 below). |
| Must 4: word count ≤ 1,200 | **Resolved** | 1,193 excluding the italic header line (1,202 including it). See §9. |
| Rec: claim 6 🟡 → ✅ | **Adopted** | Tally and "Verdict counts" line updated; see §2. |
| Rec: warrant table | **Adopted** | Five-row table under §3 custom; every cell checked, see §5. |
| Rec: "upsized" quote in §1 row 4 and §3 | **Adopted** | Both now carry "upsized versus the prior growth rates we talked about" (transcript line 193). Outlook and scorecard now agree. |
| Rec: analyst attribution | **Adopted** | See §6. |
| Rec: title "Marvell Technology, Inc." | Not adopted | Cosmetic; no action needed. |

### 2. Tally and claim 6

Running tally reads 10 / 1 / 1 / 0 / 0. Grading table: ✅ on claims 1, 2, 3, 4, 6, 7, 8, 9, 10, 11 (10); 🟡 on 5 (1); ❌ on 12 (1). "Verdict counts" line matches. Claim 6's rewritten evidence: "Within scale-out switching, our business remains on track to more than double this year" is verbatim (transcript line 37); "Scale-out switching on track to more than double in FY27" is verbatim (Q2 slides p.18); the Q1 definition "exceed $600 million, doubling from fiscal 2026" is verbatim (Q1 call, as quoted in the Q1 outlook §5); "biasing higher this year" is verbatim (transcript line 195, "our switching, which is biasing higher this year"). Accurate against both the Q2 call and the Q1 definition.

### 3. Arithmetic

- Claim 4: 567.8 × 0.87 = 493.99 → $494.0M. Correct.
- Claim 12: 1,360,867 / 4 = 340,216.75 → "about 340,217" correct; 58,970,907 − 1,360,867 = 57,610,040 correct; 57,610,040 / 240 = 240,041.83 → "about 240,042" correct. Underlying figures all in the 8-K text: "58,970,907", "1,360,867", "equal quarterly installments during the first year", "240 equal tranches", "$500 million".
- Warrant table: 58,970,907 / 876.9M = 6.72% → "about 6.7%" correct; 240 × $500M = $120B correct.

### 4. §6 "Stopped saying"

No longer lists China or competitors as shifts. The reframed China sentence is accurate against the 10-Q (42% of Q2 net revenue shipped to China vs 29% a year earlier; Note 3 line 324) and against both transcripts (zero mentions). Tags on both sides present.

### 5. §3 warrant table and definition

| Cell | 8-K text | Result |
|---|---|---|
| up to 58,970,907 shares | "up to an aggregate of 58,970,907 shares" | ✓ |
| about 6.7% of 876.9M outstanding (computed) | 10-Q cover: "876.9 million" | ✓ |
| $206.58 | "exercise price of $206.58 per share" | ✓ |
| 1,360,867 time-based, "in equal quarterly installments during the first year" | "1,360,867 of the Warrant Shares ... vest in equal quarterly installments during the first year" | ✓ verbatim fragment |
| 57,610,040 performance shares (computed), 240 equal slices, "one tranche vesting for each $500 million in Custom Products revenue", Q3 FY2027 through FY2033 | "in 240 equal tranches, with one tranche vesting for each $500 million in Custom Products revenue"; "from the Company's third quarter of fiscal 2027 through the end of the Company's fiscal year 2033" | ✓ |
| full vesting = $120 billion (computed) | 240 × $500M | ✓ |
| Exercisable until August 18, 2033 | "exercisable ... until August 18, 2033" | ✓ |

Definition present in the prose: "A warrant is a contract giving its holder the right to buy shares at a fixed price for a set period (terms in the table)." Plain; "vesting (becoming usable)" and "slices" for tranche are glossed in the table. Understandable without finance background. The §3 custom paragraph is no longer number-dense.

### 6. "Your math is not wrong" attribution

Transcript line 159: "Your next question comes from Ben Reitzes with Melius Research." Line 161 (Reitzes): "...that's about $18 billion a year, and at the $120 billion divided by 6.5." Line 165 (Murphy): "when you look at the scale of this, your math is not wrong." Outlook §6 now reads "when Ben Reitzes of Melius Research put full vesting at '$120 billion divided by 6.5', the CEO answered 'your math is not wrong'". Name, firm, both quotes and speaker order are correct; "definitely goes higher" is also verbatim (line 169).

### 7. Cycle-1 direct fix

Intact: §6 tone table, scale-up optics row, Q1 column reads `"about $300 million" [Q1 FY2027 call]` (now line 81 after the table insertions); zero occurrences of the old tag.

### 8. business.md

`git diff HEAD --numstat`: 14 added, 0 deleted. Body from the title line onward compared byte-for-byte against `HEAD:companies/MRVL/business.md`: identical. Flag blocks: 7.

### 9. Word count (AGENTS.md definition: prose excluding tables, headings, sources list, tags)

Reviewer count: **1,193** excluding the italic header line; 1,202 including it. Writer reported 1,193 excluding the header; counts agree. Within the 800–1,200 target on the operative reading; the header line is part of the §7 header block, not prose.

### Other checks on changed text

- §3 communications-and-other quotes ("to decline in the low to mid-teens percentage range", "a solid sequential recovery in the fourth quarter") verbatim (transcript line 59).
- §6 table new rows: stock-based pay $207.6M / $326.2M / $153.6M [supplemental p.5 line 137] ✓; commitments $2,756.8M / $8,518.9M [Q1 Note 9; Q2 Note 9] ✓. "More than doubled year over year" (326.2 / 153.6 = 2.12) and "tripled in one quarter" (8,518.9 / 2,756.8 = 3.09) are fair; $5,762.1M increase correct.
- Banned-word sweep outside quotes: none.
- No new numbers or quotes failed.

### Fixed directly in cycle 2

None required.

### Final verdict: **PASS**

All four must-change items resolved; all adopted recommendations implemented correctly; no verdict, number or quote fails; business.md body untouched; word count within target.
