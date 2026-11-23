# Findings: focused check of 8227 repair round 6

Reviewer: Claude Opus 5.5 (cross-vendor, REVIEWER). Date: 2026-11-23. Inputs are frozen in `inputs.json` (snapshot `13dcf9f7…e818464`, HEAD `11cd03fe`, 301 git status entries before this review). Reviewer seed: `opus-5-5-r6-reviewer-2026-11-23`.

## Method

- **Rebuild.** I copied the workspace to a separate fresh directory and ran `run_repair_r6.py` there: two full rebuilds. I then ran the three round-6 checkers and compared my 137 analysis outputs with the author checkout.
- **Structure, by script.** I recomputed every family–exam-part candidate from `textbook-families.json` and `question-analysis.json` and checked:
  - decisions and read evidence;
  - family summaries against the pair records;
  - member–family demand coverage;
  - text reuse in family prose;
  - stale figure statuses.
- **Blind pair sample (100 pairs).** I drew 100 pairs by stratum:
  - 20 same type and 25 structural branch (main records);
  - 5 same type and 5 branch (member-level exceptions);
  - 30 rejections where the exam part covers all of the family's demands, and 15 other rejections.

  Four agents judged them from rendered pages without seeing the author's labels. Each agent saw the family title and up to three members.
- **Families.** I checked 40 families: the 20 sampled in round 5, mapped to their round-6 successors, plus 20 drawn fresh. Two agents read 140 members on rendered pages (non-blind).
- **Figures.**
  - 40 figures classified blind (graphic or text callout, given or teaching), then compared with the author's labels.
  - 8 positive and 6 negative representation-medium claims.
  - 10 given-figure roles.
  - The nine registered printed errors.
- **Notes and answer pages.** 30 repaired and 10 unrepaired notes; 20 of the 103 answer-page inspections; all 10 locator findings.
- **Insights and map.**
  - 19 "Examination comparison" sections: the 9 named in round 5 and 10 drawn at random.
  - 22 demands in the per-objective map, with the header recomputed.
- **Provenance and recall.** Pair 037 against its record, and recall in the screen record.
- **What I verified myself, beyond the scripts:**
  - PAIR-024 on both rendered pages;
  - 2023 P2 Q3(b)(ii) on its rendered page;
  - the relation records behind every claim below.

The agents' working files are in my scratchpad. The disagreement list and the gap list are saved in this folder.

## A. What passed

- **Rebuild: passed.**
  - Two rebuilds of 281 commands produced 158 byte-identical outputs, and all 38 prior seeded negatives were rejected.
  - The round-6 checkers rejected 12 + 5 + 5 further seeded errors.
  - My 137 analysis outputs match the author checkout file for file.
- **Candidate completeness: passed.**
  - Recomputing from the round-6 families gives exactly 2,675 candidates, and every one has a decision.
  - No decision lacks a candidate, and no family has undecided parts.
  - All 719 positive relations carry a read date and existing renders. Every branch carries a direction.
- **Family summaries: passed.** All 500 equal the summary derived from the pair records, including member-level exceptions.
- **Positive relations: accepted.**
  - 28 of 30 sampled same-type or branch claims were confirmed as related.
  - 23 of 25 same-type claims were confirmed as same type.
- **Named round-5 mislinks: fixed.**
  - elementary-exponential-primitives now links to 2021 P2 Q9(a), not Q2.
  - modulus-quartic-root-count is the same type as 2025 P2 Q12(a).
  - log-derivative-division-integral-chain is the same type as 2021 P2 Q2.
  - mixed-retained-definite-integrals is split.
- **"No exam parts" insight sections: fixed.**
  - None of the 19 sections checked wrongly claims there are no exam parts.
  - Their exam-part, same-type and branch lists match the records exactly.
  - The anchors for stationary classification and identity proof are corrected.
- **Per-objective map: accepted in structure.**
  - All 138 demands are present.
  - The header counts recompute exactly.
  - All 22 sampled demands match `question-analysis.json` and the relation records.
- **Figures: accepted, with small fixes (R6-07).**
  - The stale "pending" statuses are gone from all 1,758 records.
  - All nine printed errors are registered in three places and match their pages.
  - Blind type labels agree on 38 of 40 figures and role labels on 36 of 40.
  - All 8 positive medium claims hold, and none equates a figure with an exam figure.
- **Provenance: accepted.**
  - Pair 037 (2023 P2 Q4(b) ← 9709/22/M/J/20 Q1) is recorded part-level, with its changes, the duplicate /23, the weaker s17/21 lead and a hidden label.
  - Pair 021 no longer has "(d) 3→3".
  - Recall is recorded as 16 of 32, with the round-5 baseline of 16 of 31.
- **Answer-page findings: accepted.** All 10 round-6 locator findings are confirmed on renders, including Goldie 5B Q11(ii) → PDF 346 and YM C3 Try Now 4 Q3 → PDF 599.

## B. Findings

### R6-01 (medium): the list of exam parts with no textbook practice contains false gaps

**The list.** 31 exam parts have no same-type or branch relation (`no-textbook-relation-parts-r6.json`).
- **9 are expected.** Their only demands are prior-knowledge or modelling abilities.
- **22 are on syllabus demands.** This list is what the planner would use to decide where the Workbench adds most value, so it must be right. It is not.

**Confirmed false gaps:**
- **2024 P2 Q4(a)**, "Differentiate (3e²ˣ − 7)⁵".
  - It had a single candidate family, which was rejected.
  - The books have the same chain-rule task many times. YM C7 Try Now 12 Q2(a) and Q3(a) (PDF 334) differentiate (2x² − 1)⁶ and (x² − 4x + 5)⁶. A blind agent also cites Goldie 4B Q2(viii), (e²ˣ + 1)³ (PDF 108).
- **2023 P2 Q3(b)(ii)**, "Find the exact value of cosec(2π/3) + cot(2π/3)" (render read: a forward exact evaluation, 2 marks).
  - All 8 candidates are rejected.
  - Four rejection reasons describe a different part. special-angle-exact-values says "the target instead solves for unknown angles, differentiates/integrates…", and inverse-angle-squared-ratio-evaluation and advanced-proof-hence-roots say "the exam asks the learner to integrate". That is part (b)(iii).
  - reciprocal-exact-values (Goldie 3A Q2 and others) was never a candidate, because (b)(ii) is not linked to the reciprocal demand M2:T3:O01:D01.
  - The section "Exact special angles and connected geometry" therefore reports no relation, and its step-3 proposal suggests new task structure may be needed. Both are wrong for this part.

**Likely false gaps that need a reading:**
- 2022 P1 Q13: integrate a power of a linear expression, find the constant, recover the curve through a point.
- 2025 P1 Q10(b): sector area.
- 2025 P2 Q6(a) and (b): linearise, then solve an exponential equation.
- 2023 P2 Q4(b) and (c).
- 2022 P1 Q14(a).

**Cause.** Candidates come only from demand-ID overlap. The demand mapping is noisy (R5-03), so a part can end up with one candidate, or none of the right ones.

### R6-02 (medium): rejections under-call real relations

**What the blind sample found** (45 rejections): 31 unrelated, 11 structural branch, 3 same type. Weighted by stratum, roughly 30% of the 1,956 rejections may be related pairs. That estimate is wide, but it is not small.

**Causes:**
1. **The "nonordered" rule.**
   - 202 pairs carry a `nonordered_connection`. They were withdrawn from structural branch because neither side is simply easier or harder.
   - 5 of the 6 sampled were judged related, 2 of them as the same type.
   - My round-6 prompt said "say whether the branch is easier or harder"; the author treated that as a gate. A branch can differ in both directions.
2. **An over-strict same-type test.**
   - **PAIR-024** (I verified the rendered pages):
     - *The pair.* YM C7 Try Now 12 Q2 ("differentiate (2x² − 1)⁶; hence find ∫x(2x² − 1)⁵ dx") against 2024 P2 Q4(b) ("hence find ∫60e²ˣ(3e²ˣ − 7)⁴ dx").
     - *Why it was rejected.* "The target uses an exponential inner derivative, not a rational one."
     - *Why that is wrong.* In both, the learner recognises a multiple of the derivative from part (a) and integrates. The family differentiate-hence-primitive exists exactly for this exam form, and it is recorded as rejected against it.
   - The agents also report PAIR-034 (YM Example 18(d) against 2024 P2 Q4(a)) and PAIR-038 (Goldie 4D Q6(i) against 2023 P2 Q8(a)) as same type. Both are medium confidence; I have not verified them.
3. **Batch-worded reasons.** 389 rejection reasons are phrased for several targets at once ("the target instead…", "none of these targets"). 2023 P2 Q3(b)(ii) shows such a reason applied to the wrong part. In the sample, 4 of 12 batch-worded rejections were disputed, against 5 of 27 specific ones.

**Effect.**
- The map shows these families under "other textbook practice" for the right demand, so nothing is lost from a demand's problem set.
- But a rejection is presented as a difference in learner decisions, when it should mean "relation not established".
- The demand count with same-type practice (69 of 138) is a lower bound.

The 28 disagreements between the author's labels and the blind agents' are in `blind-pair-disagreements.json`, with the agents' reasons and best members.

### R6-03 (low; limitation): same type is under-called among branches

**The pattern.** Of 30 sampled branch claims, 18 were confirmed as branches, 10 were judged same type and 2 unrelated.
- **Typical:** polynomial-factor-sketch-chain against 2023 P2 Q1(c), compound-identity-proof against 2022 P2 Q7(a), and compound-bounded-equations against 2024 P2 Q2.
- **The cause** is the same cautious default as round 5 (the author picks the safer label), but much weaker.

**What it means.** The relation is right that the two are related; only the strength is under-stated. I do not ask for a relabel. Step 3 should treat "same type" counts as lower bounds, and treat a branch whose `differing_decision` names only a change of values or function family as a same-type candidate.

### R6-04 (low–medium): 61 families have no assessed demand, so they were never compared

**The gap.** 61 families have empty `assessed_demand_ids`. Most are support or boundary groups, which is reasonable. But 41 of their 236 members carry examined item-level assessed demands, and these families were never compared with the exam. Examples:
- **implicit-dependent-expression:** Goldie Example 15 and 4D Q1 are implicit differentiation, which is examined 3 times.
- **explicit-second-derivative-zero:** Goldie 4B Q10 and YM Try Now 42 Q2.
- **trig-derivation-teaching-support:** M2:T3:O02:D02, examined 5 times.
- **forced-trig-area-substitution-boundary.**

**Related coherence gap.** implicit-given-point-gradient lists only D03 (an implicit derivative in a geometric demand). All six members actually need D01 (differentiate an implicit curve).

### R6-05 (low–medium): the family prose repairs (B.1–B.5) are only partly met

Results on the 40 sampled families:

| Check | Pass | Weak | Fail |
|---|---:|---:|---:|
| Membership coherence | 32 | – | 8 |
| distinction_basis | 13 | 12 | 15 |
| difficulty_progression | 25 | 14 | 1 |
| units_and_precision | 7 | 31 | 2 |

**Membership misfits** (named members, read on renders):
- **modulus-quartic-root-count:** YM Revision 8 Q3 is "show two roots by sketching", but the family claims "Solve modulus equation".
- **identity-common-expression:** YM Try Now 35(e) and 37(b).
- **implicit-given-point-gradient:** demand mismatch, as in R6-04.
- **parametric-point-plot-support:** Goldie Worked illustration 1.
- **log-derivative-division-integral-chain:** Goldie 5A Q8(i).
- **elementary-exponential-primitives:** Goldie 9B Q1(iii) carries part (iv)'s reason.
- **elementary-reciprocal-definite-logform:** Goldie Examples 5.2–5.4 and 8H Q2(ii) ask for no log form.
- **vector-division-position:** YM Revision 5 Q3 and Goldie 10F Q11(i) involve no division.

**distinction_basis:**
- 428 of 500 repeat their "Compared with X:" prefix twice.
- In the failures, the text compares against a family other than the declared sibling, misdescribes the sibling, or is a process note. Examples:
  - derivative-sign-and-monotonicity describes its sibling as computing a derivative at one point;
  - identity-equation-distinction "closes the old missing-textbook-support lead".
- quadratic-exponential-recovery and exponential-positive-substitution appear to be the same family, split only by demand ID.

**units_and_precision.**
- Every family's text is distinct as a string, but 446 of 500 contain a sentence shared by 7–39 families.
- Two are contradictory:
  - photo-density-estimation-support carries integration text ("integration variable, differential, bounds");
  - trig-derivative-hence-integrals carries trapezium-rule text.

**Membership reasons.** 56 of the 140 read run words together or drop "=" signs, e.g. "givesA+C5,A+B−1,B+2C0". A few are false: completed-square-interpretation's "selected result" is the original polynomial, never the completed form.

**Record errors found in passing:**
- **YM Try Now 17 Q1(b)** (PDF 543): the page prints ∫₀^{π/6} tan²x dx. The record uses tan²(2x) and gives √3/2 − π/6; the printed integrand gives √3/3 − π/6.
- **YM Example 12(c)** (PDF 174): the question says y = 3cos x + 2, but the printed solution sketches 3cos 2x − 1. The record follows the question without noting this.
- **YM Example 12 (PDF 122)**, from a blind agent: domain x ≠ 3 should be x ≠ −3, and the range of √(x − 5) is printed as all reals.
- **Goldie 3D Q9(ii) and (iv):** the smallest positive θ is asked for, but the selected results give only the extreme values.
- **trig-formula-restricted-sketch:** selected-result keys are truncated ("window_m…").

### R6-06 (low): notes are not repaired

The report says 1,034 notes were repaired, but the repair added spaces only. Many notes also lost "=" signs in extraction, which a spacing repair cannot restore. Examples:
- "y−x+π" for y = −x + π;
- "Tanx−2gives" for tan x = −2;
- "p1.35, K7.12to2dp".

Of 30 repaired notes read, 4 read normally, 24 partly and 2 not at all. Of 10 unrepaired notes, none reads normally. The note-spacing input files still say "working; … remaining proposals unreviewed".

The planner documents (`objective-problem-map.md`, `textbook-insights.md`) do not carry the notes and read cleanly, so this is a limitation, not a blocker. But the report's claim should be corrected, and the notes marked as damaged text.

### R6-07 (low): small record fixes

- **Answer locators** (both introduced in round 5; the earlier locator was right):
  - YM C4 Try Now 50 Q1(b): the key is on PDF 612, not 613;
  - YM C13 Try Now 4 Q3(a): the key starts on PDF 653.
- **Answer-page observations that name the wrong item:**
  - YM 623: Try Now 32, not 33;
  - YM 634: Try Now 11, not 10;
  - Goldie 352: Activity 8.2, not 8F;
  - Goldie 354: Chapter 9 marked out of scope, contradicting the inventory.
- **Figure roles:**
  - Goldie C10 Teaching-figure 22 (Figure 10.12, PDF 257) is a worked-solution panel, not given;
  - YM C4 Teaching-figure 13 (PDF 158) is the given diagram for Try Now 4.
  - Long divisions are graphics in Goldie but text callouts in YM; choose one rule.
- **Figure medium:**
  - Vector diagrams drawn on squared paper are tagged "graph" and so come out negative; 2022 P1 Q11(a) and 2024 P1 Q10 use vector diagrams.
  - Parts where the learner reads back their own sketch are not counted (2023 P2 Q6(d)).
- **Insights:**
  - The transform-equations branch for 2021 P1 Q5(a) says "quadratic in sec θ"; it is a quadratic in cos θ.
  - The principal-inverse proposal treats the held 2023 P1 Q9 as design evidence and omits the Cambridge comparators the map links to (w15/11 Q3 and others).
  - Both documents still say "no verified relation recorded yet" in places.
- **Map:** its recorded input hash for `textbook-inventory.json` is from before the figure step. The rebuild reproduces the map exactly, so this is ordering hygiene only.
- **Status strings:**
  - `textbook-exam-relations-r6.json` still says "working; first rendered comparisons";
  - two note-spacing inputs say "working".
- **Provenance 037 text:** the fields have lost their spaces ("Bases2^y=9^(3x) become3^y…").
