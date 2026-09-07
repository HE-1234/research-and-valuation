# Alphabet Inc. (GOOGL) — Reviewer report, 2026-Q2 refresh

_Reviewed 2026-09-07 against the cached full texts in `companies/GOOGL/sources/2026-Q2/` (10-Q, transcript, press release, slides, three 8-Ks) and, for the Q1 side of claims and tone shift, `sources/2026-Q1/`. Notes files were not used as evidence. As-of cutoff 2026-07-23 respected; nothing later was consulted._

_Page conventions used below. Q2 transcript has no printed page numbers; pages are counted by form feeds, and the form feed opens a new page, so p.2 = lines 40–76, p.3 = 77–115, p.4 = 116–151, p.5 = 152–189, p.6 = 190–227, p.10 = 341–379, p.11 = 380–417, p.12 = 418–453, p.13 = 454–491, p.14 = 492–530, p.15 = 531–568, p.16 = 569–604, p.17 = 605–643, p.18 = 644–681, p.19 = 682–718, p.20 = 719–755, p.22 = 795–830, p.25 = 907–945 (27 pages in total; the MANIFEST's "8 pages" is wrong). Release: p.1 = 1–55, p.2 = 56–109, p.5 = 182–236, p.7 = 269–320, p.8 = 321–366, p.9 = 367–421, p.10 = 422–479. Slides: p.9 = 218–256, p.11 = 296–321. Q1 transcript uses its printed footers (p.2 = 47–91, p.3 = 92–137, p.4 = 138–182, p.5 = 183–227, p.6 = 228–273, p.7 = 274–318, p.10 = 410–454, p.11 = 455–499, p.13 = 545–590, p.19 = 819–864)._

**Verdict: REVISE.** One verdict is a wrong ✅ (claim 8 should be 🟡, which also changes the running tally), one §6 sentence states an attribution the 10-Q does not make ("mostly SpaceX"), one material change to business.md §7/§6 (backstop exposure) is not flagged, and the outlook is over the length ceiling. Everything else — every other verdict, every number in §1 and the time series, every §4 quote, every page tag checked — holds.

---

## 1. Blind re-grade of the 11 Q1 claims

Graded from `quarters/2026-Q1-outlook.md` §5 against the Q2 full texts before opening `scorecard.md`.

| # | Claim (short) | My verdict | My evidence (one line) | Writer | Agree? |
|---|---|---|---|---|---|
| 1 | Q2 call reaffirms or raises $180–190B 2026 capex | ✅ | Raised to "$195‑205 billion, up from our previous estimate of $180‑190 billion" [Q2 2026 call, p.13] (lines 481–482) | ✅ | Yes |
| 2 | Q2 call again says 2027 capex significantly above 2026 | ✅ | "we continue to expect our CapEx to increase significantly in 2027" [Q2 2026 call, p.13] (486–487) | ✅ | Yes |
| 3 | Q2 10-Q again says just over 50% of backlog within 24 months | ✅ | "We expect to recognize just over 50 % of the revenue backlog as revenues over the next 24 months" [10-Q Q2 2026, Note 2] (line 972) | ✅ | Yes |
| 4 | Q2 10-Q still says TPU revenue begins later in 2026, significant majority 2027 | ✅ | "In the second quarter of 2026, we began recognizing revenues from these agreements, with the significant majority to be recognized in 2027." [10-Q Q2 2026, Item 2] (line 2710). Start moved from "expect to begin later in 2026" to "began in Q2 2026", i.e. within 2026 and earlier than implied; the 2027 clause is word-for-word. Nothing fell short, so ✅, not 🟡. | ✅ | Yes |
| 5 | Q2 Cloud operating margin ≥ 29.9% | ✅ | 35.6% [Q2 2026 slides, p.9] (line 256); 8,814/24,768 = 35.6% [Q2 2026 release, p.2] | ✅ | Yes |
| 6 | YouTube Premium Lite in ≥ 36 countries by end of Q2 | 🔇 | "Premium Lite" does not appear in the Q2 transcript, release, slides, or 10-Q (grep, case-insensitive, excluding "Flash-Lite"); horizon has passed; nothing disclosed to check → Dropped, not ⏳ | 🔇 | Yes |
| 7 | Reported growth exceeds constant-currency growth by ~1 pt (±0.5) | ✅ | 24% reported, "Less FX Effect" 1%, 23% constant currency [Q2 2026 release, p.10] (lines 436–438); $740M FX on $96,540M base = 0.77 pt, inside the band | ✅ | Yes |
| 8 | Q2 call again says Cloud revenue was limited by available computing capacity | 🟡 | Management said "we continue to be supply constrained" (about model/token demand, line 69, p.2), "given the supply constraint environment" (Cloud outlook, 475, p.13), and "very strong demand, both from external Cloud customers ... the demand still outpaces that investment" (553–562, p.15). No statement that Cloud revenue was limited or "would have been higher"; the CFO's Cloud framing was that growth "accelerated meaningfully" (440–441, p.12). Directionally repeated, specific statement not made → 🟡 | ✅ | **No** |
| 9 | Q2 depreciation of P&E exceeds Q1's $6.5B | ✅ | $7,104M [Q2 2026 release, p.7] (line 277); six-month $13,586M − 7,104 = $6,482M for Q1 [10-Q Q2 2026, Item 2] | ✅ | Yes |
| 10 | Q2 10-Q shows $10.0B funded to the private company as a non-marketable security | 🟡 | 10-Q never itemizes a $10.0B funding. Consistent evidence: purchases of non-marketable securities $21,145M in Q2 [Q2 2026 release, p.7] (295); contingent commitment now "$20.0 billion" [10-Q Q2 2026, Item 2] (3268) vs $30.0B contingent + $10.0B upfront in Q1 [10-Q Q1 2026, Item 2] (2424); holdings "primarily consist of our investment in a private company" [10-Q Q2 2026, Note 3] (1276). Horizon passed and the 10-Q will not itemize later, so ⏳ is wrong; funding evidently happened but is not "shown" → 🟡 | 🟡 | Yes |
| 11 | Q2 call again says Search queries are at an all-time high | ✅ | "Search usage hit an all‑time high during the World Cup this year" [Q2 2026 call, p.3] (98–99); queries "driving growth in queries" (97). I read usage ≈ queries (Q1's own sentence used both) and a peak inside the quarter as satisfying "are at". | 🟡 | **No** (minor) |

**My blind tally:** Met 8, Missed 0, Partial 2 (claims 8, 10), Not yet 0, Dropped 1 (claim 6).
**Writer's tally:** Met 8, Missed 0, Partial 2 (claims 10, 11), Not yet 0, Dropped 1 (claim 6).
Same totals, different composition. The two disagreements:

**Claim 8 — writer ✅, reviewer 🟡. §9 supports 🟡.** The claim's checkable content is a management *statement* with a specific subject and predicate: Cloud revenue was limited by capacity. In Q1 that statement existed verbatim ("our Cloud revenue would have been higher if we were able to meet the demand"). In Q2 management said (a) "we continue to be supply constrained" in the paragraph about model/token demand; (b) "given the supply constraint environment" in the Cloud outlook, as the reason for buying third-party capacity "to keep growing our customer base"; (c) in Q&A, that demand "from external Cloud customers as well as across the business ... still outpaces that investment". None of these says Cloud revenue was held back; getting there needs one inference step (Cloud demand > capacity ⇒ Cloud revenue capped), and the CFO's actual Cloud framing was acceleration. The writer's own §6 row "Capacity" and "Said differently" paragraph record exactly this softening ("compute constrained" → "supply constrained ... just like the rest of the industry"), which is the tone shift a 🟡 preserves and a ✅ erases. §9: 🟡 = "directionally happened but ... only part of it happened" — the supply-constraint part was repeated, the Cloud-revenue part was not. **Must change to 🟡; running tally becomes Met 7 / Partial 3.**

**Claim 11 — writer 🟡, reviewer ✅. Both are defensible under §9; no change required.** The writer's 🟡 rests on two literal gaps: "usage" rather than "queries", and a peak "during the World Cup" rather than a standing "are at". My ✅ treats those as immaterial because Pichai's Q1 sentence itself equated the two ("AI continues to drive Search usage, and queries are at an all time high") and the World Cup peak fell inside the quarter being reported. Under the instruction to grade strictly and literally, the writer's 🟡 is at least as well supported as my ✅, the evidence line quotes the exact wording so the reader sees the narrowing, and it is not a ✅/❌ error in either direction. Leave as 🟡.

**Claims 4 and 10 (flagged for attention):** both agree with the writer, reasoning in the table. On 10, the writer correctly hedged ("consistent with one") rather than asserting the funding; note the arithmetic ($30.0B contingent → $20.0B) actually implies about $20B went to the company in Q2, not just the $10.0B upfront, which is another reason the 10-Q cannot be said to "show $10.0B".

**Evidence-line audit (every ✅ and ❌):** each quoted fragment in claims 1, 2, 3, 4, 5, 7, 9 was found word-for-word at the tagged page/line above. Tags are correct. Claim 8's quotes and pages are accurate; only the verdict is wrong. No ❌ verdicts exist.

---

## 2. Scorecard format and tally (§10)

| Check | Result |
|---|---|
| `# <Company> — Scorecard` | OK ("Alphabet", while business.md says "Alphabet Inc."; cosmetic) |
| Running tally row (quarter graded / met / missed / partial / not yet / dropped) | OK; 8/0/2/0/1 matches the table as written. **Becomes 7/0/3/0/1 after claim 8 is corrected.** |
| Indicator time series, one row per locked indicator, newest on right | OK; 8 rows, labels identical to business.md §8; three columns (pre-Q1 basis / Q1 / Q2) with the odd first-column basis labelled per cell |
| Q2 column values | All verified: +17% (release p.1); 35.6% (slides p.9); $513.9B/$519.5B, "just over 50%" (10-Q Note 2); $44.9B, 37.5% = 44,924/119,796, $7.1B (release p.7/p.1); −$5,855M, $53,273M (slides p.11); 19.8%, "substantially consistent" (10-Q Item 2 line 2972); paid subscriptions absent from all four sources (grep confirmed); 12,230M common, $0 buybacks, $69.5B left, 19M preferred (release p.5; 10-Q Note 11) |
| Grading section heading `## Q2 2026 (grading claims made in Q1 2026)` at top | OK |
| Table claim / verdict / evidence with tag | OK; evidence one line each; claim numbering matches the archived outlook |
| ⏳ carry-forward | None to carry; stated explicitly in outlook §5 |
| Sources list mapping tags to files | OK; the transcript page convention is documented |

---

## 3. outlook.md checks

**(a) Skeleton (§7).** Title, tier line (company-published; matches MANIFEST tier 1), §1–§6 in order, §6 Tone shift present, Sources list. OK.

**(b) §1 indicators.** Row labels are exactly the eight in business.md §8 (still `_Proposed_`; the writer says so). Every Q2 number verified as in the table above; every Q1 number matches the archived outlook; the "what management had said to expect" column reproduces Q1 §4 quotes at the right pages. OK.

**(c) §4 quotes, word-for-word against `transcript.txt`.** All ten checked; all verbatim, ellipses only where marked, pages correct:
Capex 2026 (481–482, p.13) ✓; Capex 2027 (486–487, p.13) ✓; Backlog (449–450, p.12) ✓; TPU timing (470–473, p.13; ellipsis drops "from our existing TPU system sales agreements") ✓; Third-party capacity (475–479, p.13; ellipsis drops one sentence) ✓; Search comparison (465–466, p.13) ✓; FX (459–461, p.13) ✓; Free cash flow (495–496, p.14) ✓; Equity markets (644–647, p.18; two ellipses drop asides) ✓; Depreciation and hiring (489–492, p.13–14) ✓. §2 and §3 quote fragments (lines 65, 69, 75, 96–99, 107, 114, 118–119, 146–147, 209, 402, 418, 427–428, 435–453, 700–705) also verified at the tagged pages. Q1-side quotes in §2/§3/§6 verified against the Q1 transcript at p.2 (58), p.3 (113–114), p.4 (167), p.5 (190), p.6 (260), p.7 (284), p.10 (436–437), p.11 (455, 458–459, 476). §6's "equity not mentioned [Q1 call, p.11]" and "SpaceX not raised [Q1 call]" confirmed by grep. Q1 10-Q Note 15 wording ("generates revenues primarily from consumption-based fees and subscriptions") confirmed at line 1857.

**(d) §5 claims.** Nine claims (target 6–12; within the 8–12 asked). Each is one sentence, one observable, single direction, with a verbatim quote and tag beneath, and each can be graded next quarter from the 10-Q, slides, release, or call without judgment. Five are on locked indicators (Cloud margin, backlog, Search growth, depreciation, FCF). Two small points: claims 2 ("below Q2's 35.6%", from "modest margin pressure") and 8 ("shares sold under the ATM during Q3", from "which we'll do for some period of time") are the writer's sharpenings, exactly like claim 4, which is labelled as such; they should carry the same label for honesty. Claim 3's supporting quote is vague ("strong demand indicators ...") but the claim itself is mechanical.

**(e) §6 Tone shift.** Every table row has a Q1 tag and a Q2 tag, and each pair is a real wording or fact difference (checked above). "Stopped saying" is factual and confirmed by grep (no "800%", no ride count, no subscription count, no Gemini Enterprise growth rate in Q2). "Said differently" is observation with quotes, and the closing sentence is labelled "Our inference". One sentence in "Started saying" fails: "**mostly SpaceX shares under sale restrictions**" is not in any source. The 10-Q attributes the $99.0B "primarily ... to unrealized gains in our equity securities portfolio from SpaceX and a private company" (Item 2, lines 2831 and 3101) and Note 3 splits the gain as $77.4B on non-marketable (measurement-alternative) securities and $21.4B on marketable and other equity securities (lines 1288–1298), without saying how much is SpaceX. "Mostly SpaceX" is an unlabelled inference presented as fact — interpretation dressed as observation. Nit: the "Inventory" row's Q1 column shows the 12/31/2025 figure from the Q2 release rather than a 3/31/2026 figure; acceptable as labelled.

**(f) Jargon audit.** Banned words: every hit of headwind/tailwind is inside a management quote or inside quotation marks in a gloss label; no leverage, synergy, monetize, ecosystem, at scale, robust, unlock outside quotes in outlook.md, scorecard.md, or the flags. Terms glossed in place: EPS, P&L, OI&E, SBC, tokens, APIs, pre-training, lapping, third-party capacity, paper gain. Terms that were **not** glossed and that a 16-year-old would not know: "mandatory convertible preferred shares" (§1 row 8; also scorecard row 8), "ATM program" outside the quote (§5 claim 8 relies on the §4 quote), "equity gains" (§6), "measurement-alternative holdings" (scorecard claim 10). All four fixed directly (see below). Remaining terms are either glossaried in business.md (TPU, backlog, TAC, depreciation, free cash flow) or name-inferable.

**(g) Word count.** By the AGENTS definition (prose only; tables, headings, Sources list, and `[tags]` excluded): **1,312 words as submitted; 1,329 after my glosses** (the glosses added 17 prose words; the §1 gloss is in a table and does not count). Ceiling 1,200. Breakdown: §1 22 / §2 143 / §3 321 / §4 341 / §5 263 / §6 216 (pre-gloss). Words inside double quotes across the prose: 538, of which §4's mandated verbatim guidance is the bulk. The writer's explanation is fair as far as it goes — without §4 the file would be ~990 words — but §4 is not the only place to cut. Cuts to get under 1,200, in priority order, with word savings:

| # | Cut | Saves | Required content? |
|---|---|---|---|
| 1 | §6 "**Stopped saying.** See the last five rows: four Q1 growth or scale figures were not repeated, and a question about buying computing from SpaceX went unanswered [tags]." — delete; the table already shows it | 26 | No |
| 2 | §6 "New outlook items: free cash flow "under pressure", Search "lapping", "modest margin pressure" from third-party capacity [tag]." — delete; duplicates §4 | 16 | No |
| 3 | §3 "Gemini 4, a bigger model, is in its "most ambitious pre‑training run yet" (pre-training: ...) [tag]." — delete; a roadmap item, not a measurable engine | 22 | No |
| 4 | §6 "Reported profit was dominated by a paper gain: ... mostly SpaceX shares under sale restrictions" → "A $99.0 billion paper gain on stakes in SpaceX and a private company added $77.1 billion to net income and $6.26 to EPS" (also fixes the error in (e)) | 12 | Rewrite is required; the shorter form loses nothing sourced |
| 5 | §2 ""Lapping" means the year-ago quarter was itself strong, so the growth rate gets harder to hold." → "(lapping: the year-ago quarter was itself strong)" appended to the quote | 9 | Gloss is required in spirit; the short form keeps it |
| 6 | §1 footnote → "Indicators: the proposed set in business.md §8; last column from the Q1 2026 outlook §4." | 7 | No |
| 7 | §3 Waymo: "Waymo launched the Ojai vehicle, and" — delete | 6 | No |
| 8 | §4 "We also expect to continue hiring in key investment areas such as AI and cloud" — delete and retitle the bullet "Depreciation" | 15 | Borderline: §4 asks for "anything else they commit to"; a hiring intention with no number is the weakest item in the list, so cut it last |
| 9 | §6 closing "Our inference: ..." sentence | 32 | No, but it is the most useful synthesis in the section; only if 1–8 are not enough |

Cuts 1–7 save 98 words (1,329 → 1,231); adding 8 saves 113 (→ 1,216); adding 9 reaches 1,184. Alternatively the owner may accept ~1,230 on the grounds that §4's verbatim quotes are mandated; that is the owner's call, not the writer's.

---

## 4. Flags on business.md

`git diff HEAD -- companies/GOOGL/business.md`: 14 inserted lines (seven flag blocks, each followed by a blank line), zero deletions; `tail -n +15 business.md` is byte-identical to `HEAD:business.md` (cmp). Freeze respected.

| Flag | Change claimed | Supported by cited Q2 source? | Section named correctly? | Notes |
|---|---|---|---|---|
| 1 Equity raise, Berkshire, preferred, ATM, debt | Yes: $49.6B net (Item 2 line 2825; release p.2), Berkshire $10.0B (Note 11 line 2252; 8-K 06-04), 6.25% preferred converting ~May 15, 2029 (Note 11; 8-K 06-05), $40.0B ATM unused (Note 11 line 2284), face value $101,085M (Note 6 line 1820), no buybacks (Note 11 line 2298) | §7 ✓ (Cash paragraph and table list debt and stopped buybacks only). Should also name §6 scenario 2, which describes the funding as "debt ... and by stopping buybacks", and §4's closing cash-vs-debt sentence. | Two precision points: (i) $49.6B is stated in Item 2 and the release, not Note 11 (Note 11's parts sum to $49.5B); (ii) the flag compares §7's $77.5B (carrying value) with $101.1B *face* value; like-for-like is $98.2B carrying [10-Q Q2 2026, Item 1 / Note 6]. |
| 2 Cloud sells TPU systems; inventory | Yes: Note 1 lines 829, 835, 880; Note 15 line 2518; Item 2 lines 2710, 2926; release p.5 inventory $2,439M → $9,991M; call p.10 "inventory costs, primarily from the sales of TPU systems" | §2 and §3 ✓; §1 ("charges mostly by how much they use, plus subscriptions") is affected too | Warranted |
| 3 Negative FCF | Yes: slides p.11 (−$5,855M; TTM $53,273M, −20%); call p.14 | §4 ("stuck between $60 billion and $73 billion") and §6 scenario 2 ("stuck near Q1 2026's $10.1 billion") ✓ | Warranted |
| 4 Legal status | Yes: Android ECJ denial July 2026, "now final", $5.2B paid (Note 10 line 2186); PriceRunner ~$2.1B accrued, appealed (line 2212); Epic "is complying with the October 2024 remedies decision" (line 2202) | §6 ✓ | Warranted. Precision: Google withdrew its Supreme Court petition in **March 2026** (Q1, already in the Q1 10-Q); the Q2 news is the **July 2026** joint withdrawal of the motion to modify the injunction and compliance. The flag reads as if the petition withdrawal were new. |
| 5 Equity gains; restricted SpaceX shares inside "marketable securities" | Yes: Item 2 line 2831; Note 3 lines 1101–1103 ($80.0B short-term restricted; $14.1B restricted through Q3 2027); release p.9 ($77.1B / $6.26); $55,911 + $186,563 = $242,474 | §4 ("quickly sellable investments") ✓ | Warranted; correctly quotes "SpaceX and a private company" without apportioning |
| 6 Capex raised; leases $85.2B; commitments $811.0B | Yes: call p.13; Note 4 line 1699; Item 2 line 3262 | §3 and §6 ✓ ($180–190B in both; $75.6B leases in §6) | Warranted |
| 7 Indicator 7 proposal | Yes: paid-subscription count absent from all four sources; 950M MAU and 22B tokens/min are in release p.1 | §8 ✓; proposal only, locked set unchanged, as §8 requires | Warranted |

**Missing flag (material):** business.md §7 table row "Backstops ... up to $33.3B, of which ~$15.3B signed | April 2026" and §6 "Concentration" ("guarantees backing other companies' data centers and power plants"). Q2 10-Q: credit-derivative notional (signed backstops) $43,785M at 6/30/2026 vs $16,940M at 12/31/2025 and $28,436M at 3/31/2026 [10-Q Q2 2026, Note 3, line 1375; 10-Q Q1 2026, Note 3]; financial guarantees with maximum future payments $7.6B [Note 10, line 2164]; plus "an estimated $24.1 billion of future backstops ... subject to finalization" [Item 2, line 3266]; credit-derivative liability fair value $815M vs $69M [Note 3, line 1406]. Signed exposure roughly tripled against the figure §7 cites and total potential roughly doubled. This is exactly the "materially incomplete" case §11 describes.

**Optional additions (minor, owner's call):** §7's "Commitment to an unnamed private company: $40.0B ... $10.0B due Q2 2026" row is stale — remaining contingent commitment is $20.0B [Item 2 line 3268] and Q2 purchases of non-marketable securities were $21.1B [release p.7]; could be folded into flag 1 or 5. The Principal Accounting Officer appointment (8-K 2026-06-05, officer) is not a named executive in §7 and does not need a flag.

**Unwarranted flags:** none.

---

## 5. Rubric (§14), after reading business.md + outlook.md

1. **What the company does and who pays, in two sentences?** Yes — business.md §1 does it; outlook §3's TPU block adds the one new payer type (hardware buyers), and flag 2 records that §1–§3 do not yet cover it.
2. **What would kill it and the early warning?** Yes — §6 ranks five scenarios with warnings; flags 3, 4, 6 correctly mark the scenario-2 and -3 numbers that have moved. The missing backstop flag leaves the concentration paragraph understated.
3. **Why margins are what they are and whether cost scales with usage?** Yes for the ad business (§3); the hardware line and third-party capacity are new and only covered in outlook §3/§4 — flag 2 sends the owner there.
4. **Predict next quarter's scorecard from §5 alone?** Yes — nine mechanical claims with the number or event named; two sharpenings should be labelled.
5. **Nothing requiring knowledge I don't have?** Yes after the four glosses added below; before them, "mandatory convertible preferred", "ATM program", "equity gains" and "measurement-alternative" were bare.

---

## 6. Verdict: REVISE

1. **scorecard.md, claim 8: change ✅ Met → 🟡 Partial.** Keep the existing quotes; add the reason: management repeated "supply constrained" and said Cloud-customer demand outpaces capacity, but did not say Cloud revenue was limited (Q1's "would have been higher" statement was not repeated; the CFO's Cloud framing was acceleration). **Update the running tally to Met 7 / Missed 0 / Partial 3 / Not yet 0 / Dropped 1.**
2. **outlook.md §6 "Started saying": remove "mostly SpaceX shares under sale restrictions".** The 10-Q says "SpaceX and a private company" and gives no split. Suggested: "A $99.0 billion paper gain on stakes in SpaceX and a private company added $77.1 billion to net income and $6.26 to EPS [Q2 2026 release, p.9] [10-Q Q2 2026, Item 2]."
3. **business.md: prepend a flag for the backstop exposure** (§7 table row and §6 Concentration): signed credit-derivative backstops $43.8B at 6/30/2026 vs $16.9B at 12/31/2025 and $28.4B at 3/31/2026; $7.6B financial guarantees; $24.1B further backstops agreed but not final [10-Q Q2 2026, Note 3] [10-Q Q2 2026, Note 10] [10-Q Q2 2026, Item 2]. Owner to decide whether to update §6 and §7.
4. **outlook.md length:** apply cuts 1–7 from §3(g) above (98 words, to ~1,231), and cut 8 if the owner wants a hard 1,200; none of 1–7 is required content.
5. **Flag 1 wording:** compare like with like — "$98.2 billion carrying value ($101.1 billion face)" against §7's $77.5B; add `[10-Q Q2 2026, Item 2]` for the $49.6B figure; add §6 scenario 2 and §4 to the affected sections.
6. **Flag 4 wording:** the Supreme Court petition was withdrawn in March 2026 (already Q1); the new Q2 fact is the July 2026 joint withdrawal of the motion to modify and "is complying with the October 2024 remedies decision". Rephrase so the reader does not take the petition withdrawal as new.
7. **outlook.md §5 claims 2 and 8:** append "our sharpening of ..., not management's forecast" as claim 4 already does.
8. (Cosmetic, optional) Title consistency: scorecard and Q2 outlook say "Alphabet"; business.md and the Q1 outlook say "Alphabet Inc."

Nothing else needs to change. Claims 1–7 and 9–11 stand as graded; every number, quote, and page tag checked in scorecard.md and outlook.md is correct; flags 2, 3, 5, 6, 7 are correct as written; the business.md body is untouched.

---

## Fixed directly (jargon glosses only; no verdict, number, quote, claim, flag, or tally touched)

- `outlook.md` §1 row 8: "19M mandatory convertible preferred shares" → added "(preferred shares that must convert into common shares in 2029)".
- `outlook.md` §4 "Equity markets" bullet label: added "an ATM program sells new shares gradually on the open market" to the parenthetical (the quote itself is unchanged).
- `outlook.md` §6 "Started saying": "$99.0 billion of equity gains" → added "(gains on stakes in other companies)". This sentence still needs the REVISE-2 rewrite.
- `scorecard.md` indicator row 8: "19M mandatory convertible preferred shares" → added "(must convert into common shares in 2029)".
- `scorecard.md` claim 10 evidence: "measurement-alternative holdings" → added "(stakes in private companies, carried at cost until a new deal sets a price)".

No typos, missing tags, or wrong page numbers were found to fix.

---

## Cycle 2 (focused re-check after the writer's second pass)

_Re-read `scorecard.md`, `outlook.md`, and the flag blocks atop `business.md` on 2026-09-07; same sources, same cutoff (2026-07-23)._

### REVISE items from cycle 1

| # | Item | Status |
|---|---|---|
| 1 | Claim 8 → 🟡; tally 7/0/3/0/1 | **Resolved.** Verdict is 🟡 Partial; evidence cell quotes "we're still in a supply‑constrained environment" and demand "from external Cloud customers ... still outpaces that investment" (lines 552–562, p.15), "the supply constraint environment" (475, p.13), and "accelerated meaningfully" (440–441, p.12); all at the tagged pages. Tally row reads 7 / 0 / 3 / 0 / 1; table has ✅ on 1,2,3,4,5,7,9, 🟡 on 8,10,11, 🔇 on 6 — matches. |
| 2 | Remove "mostly SpaceX shares under sale restrictions" | **Resolved.** Now "A $99.0 billion paper gain on stakes in SpaceX and a private company added $77.1 billion to net income and $6.26 to EPS [Q2 2026 release, p.9] [10-Q Q2 2026, Item 2]" — matches release lines 381–383 and 10-Q line 2831. |
| 3 | Add backstop flag | **Resolved.** New fourth flag block; every figure verified (see below). |
| 4 | Length under 1,200 | **Resolved.** 1,188 prose words by the AGENTS definition. |
| 5 | Flag 1 like-for-like debt; source for $49.6B; add §6/§4 | **Resolved.** "carrying value of $98.2 billion ($101.1 billion face) against the $77.5 billion §7 cites" — 10-Q Item 2 line 3208 / Note 6 line 1820–1828; $49.6B tagged `[10-Q Q2 2026, Item 2]` (line 2825) and `[Q2 2026 release, p.2]` (line 94), both state it; affected sections now §7, §6 scenario 2, §4. |
| 6 | Flag 4 (legal) Q2-only facts | **Resolved.** States only: ECJ denial, "is now final", $5.2B paid — all July 2026 (Note 10 line 2186); PriceRunner ~$2.1B July 2026, accrued Q2, appealed (line 2212); July 2026 joint withdrawal of the motion to modify and "is complying with the October 2024 remedies decision" (line 2202). The March 2026 petition withdrawal is no longer mentioned. |
| 7 | Label claims 2 and 8 as sharpenings | **Resolved.** Claim 2: "our sharpening of "modest margin pressure", not management's number." Claim 8: "our sharpening of "for some period of time", not a management commitment to Q3." All nine claims remain one sentence, single-direction, and gradeable from a named document (slides, 10-Q, release reconciliation, cash-flow statement, or call). Claim 3's quote was shortened to "strong demand indicators, including long‑term deals" — still verbatim (line 922, p.25). |
| 8 | (Optional) title "Alphabet" vs "Alphabet Inc." | Not changed; cosmetic, not required. |

### New backstop flag — figure-by-figure

| Figure in flag | Source text | Tag in flag | OK |
|---|---|---|---|
| $43.8B notional at 6/30/2026 | Q2 10-Q Note 3, derivatives notional table, line 1375: "Credit derivatives $ 16,940 $ 43,785" | [10-Q Q2 2026, Note 3] | ✓ |
| $28.4B at 3/31/2026 | Q1 10-Q Note 3, line 936: "16,940 \| 28,436" | [10-Q Q1 2026, Note 3] | ✓ |
| $16.9B at year-end 2025 | both tables above | [10-Q Q2 2026, Note 3] | ✓ |
| Liability fair value $69M → $815M | Q2 10-Q Note 3, fair-value table, line 1406: "Credit derivatives 0 69 0 815" | [10-Q Q2 2026, Note 3] | ✓ |
| $7.6B financial guarantees "back power-equipment purchases" | Q2 10-Q Note 10, line 2164: "support counterparty procurement of long-lead time equipment for our future power purchase and energy agreements ... maximum potential amount of future payments under these guarantees was $ 7.6 billion" | [10-Q Q2 2026, Note 10] | ✓ |
| "an estimated $24.1 billion of future backstops" | Q2 10-Q Item 2, line 3266, verbatim | [10-Q Q2 2026, Item 2] | ✓ |
| §7 cites "up to $33.3B, of which ~$15.3B signed"; §6 Concentration "new and unsized" | business.md body lines 130 and 109 | — | ✓ |

The flag also correctly glosses "backstop" in plain English and names §7 and §6.

### Other flags re-checked

Flag 2 now also names §1 (correct: §1 says Cloud "charges mostly by how much they use, plus subscriptions"). Flag 6 (equity gains) absorbed the optional item: "§7's row for the $40.0 billion private-company commitment is also stale: the remaining milestone-based commitment is $20.0 billion and Q2 purchases of non-marketable securities were $21.1 billion" — 10-Q Item 2 line 3268 and release p.7 line 295 ($21,145M). Flags 3, 7, 8 unchanged and still correct. No banned words in any flag.

### Mechanical checks

- `git diff HEAD -- companies/GOOGL/business.md`: one hunk at line 1, 16 insertions, 0 deletions; `tail -n +17 business.md` is byte-identical to `HEAD:business.md` (cmp). **8 flag blocks**, each followed by a blank line.
- **Word count (AGENTS definition: prose only, excluding tables, headings, Sources, and `[tags]`): 1,188** (§1 15 / §2 117 / §3 293 / §4 352 / §5 276 / §6 129). Under the 1,200 ceiling with the verbatim §4 quotes intact.
- Direct glosses from cycle 1: `outlook.md` §1 "preferred shares that must convert into common shares in 2029" — intact; `outlook.md` §4 "an ATM program sells new shares gradually on the open market" — intact; `scorecard.md` row 8 "(must convert into common shares in 2029)" — intact; `scorecard.md` claim 10 "(stakes in private companies, carried at cost until a new deal sets a price)" — intact. The fourth outlook gloss, "(gains on stakes in other companies)", is gone because the writer rewrote that sentence per REVISE-2 into plain English ("paper gain on stakes in SpaceX and a private company"), which removes the jargon it glossed — superseded, not lost.
- Banned words: hits for headwind/tailwind in `outlook.md` lines 11, 47, 79 and `scorecard.md` line 36 are all inside management quotes or inside quotation marks in a gloss label; none elsewhere.
- Nit (not a failure): §3 Waymo still carries `[Q2 2026 call, p.6]` after the Ojai clause was cut; p.6 is where Waymo appears in the Q2 call without a ride count, so the tag still supports "was not repeated".

### Fixed directly in cycle 2

Nothing. No typo, tag, page number, or jargon issue remained in the permitted categories.

### Final verdict: **PASS**

All substantive cycle-1 items are resolved; every verdict, number, quote, and tag re-checked matches the cached sources; the business.md body is untouched; the outlook is within length. Remaining cosmetic point (file titles "Alphabet" vs "Alphabet Inc.") is left to the owner.
