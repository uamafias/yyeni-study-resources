# Findings: short check of 8227 repair round 7

Reviewer: Claude Opus 5.5 (cross-vendor, role REVIEWER). Date: 2026-11-23. Commission: `review/opus-5-5-repair-r6/REPAIR-PROMPT.md` and `report.md` §3. Inputs are frozen in `inputs.json` (snapshot `abfc3399…f567e8`).

## Method

- **Fresh-copy rebuild.** I ran `run_repair_r7.py` (a double rebuild) in a separate copy of the workspace, and also ran `freeze_analysis_r7.py --check` on the author checkout.
- **Gap parts (all 22).** Two reviewer agents read every exam part and every selected textbook response on rendered pages, blind to the author's label for the 19 positive parts. They also checked that the 2 held originals really are defective, and searched both books again for 2023 P2 Q2.
- **Disputed pairs (all 28).** I compared every R7 re-decision with my R6 reviewer verdicts and reasons.
- **Rejection labels (B.1–B.5).**
  - Four blind reviewer agents judged 44 pairs on rendered pages, drawn with seed `opus-5-5-r7-reviewer-2026-11-23`:
    - 16 of the 186 converted mixed branches;
    - all 12 nonordered pairs kept rejected;
    - all 4 nonordered pairs made same type;
    - 6 of the 23 new family candidates;
    - 6 batch-rewritten rejections.
  - I tested all 403 rewritten reasons by script.
- **Empty-demand families (C).**
  - I traced all 41 members with examined item-level demands to their current families.
  - One agent read the 10 families that still hold such members, and the 4 families given demands.
- **Named fixes (D.1–D.8).** I checked these against the records myself. The page facts behind them were verified on renders in round 6.
- **My own reading.** I confirmed one kept rejection myself on the pages: YM Try Now 39 Q1(c) (PDF 366) against 2021 P1 Q4(b).
- **Untouched files.** I checked that the author did not change any review folder: the timestamps are unchanged, and Codex's snapshot hashes its `review_files`.

## A. What passed

- **Rebuild and snapshot.**
  - My fresh-copy double rebuild exited 0. Each pass ran 284 commands, and the 244 outputs were byte-identical between passes and equal to the author checkout. All 38 established negatives were rejected; the R7 checks ran inside the same pipeline.
  - `freeze_analysis_r7.py --check` passes on 7,594 files, 436 sources and 29 review files.
- **The gap search (A) is substantially right.** 21 of the 22 dispositions hold.
  - **2024 P2 Q4(a)** "Differentiate (3e²ˣ − 7)⁵" now has a same-type relation to the 28-member chain-rule family, which includes Goldie 4B Q2. The exemplar is YM C11 Example 18(d).
  - **2023 P2 Q3(b)(ii)** now has a same-type relation to Goldie 3A Q2(i)/(iii). Its eight rejections were rewritten to describe (b)(ii), not (b)(iii).
  - **The 19 positive parts:** 18 relations are real. 17 have the same relation kind as my agents, and the one kind difference (2023 P2 Q3(b)(ii): same type against branch) is a margin call.
  - **The two held originals** are genuinely defective:
    - 2022 P1 Q13: the domain x > 0 excludes P(−2, −1).
    - 2023 P1 Q9: sin⁻¹ = 2π/3 lies outside the principal range.

    Both are kept internal, and the textbook items compared are related branches.
  - **2023 P2 Q2** (recover a, b, c from a modulus graph): my agent's own search of Goldie chapter 1 and YM chapter 8 (YM PDF 382–389, 401–405; Goldie 28, 31–37) also found no modulus counterpart. The no-match stands.
- **The 28 disputed pairs.**
  - 26 now follow my reviewers' verdicts, PAIR-024 among them.
  - The two dissents are reasoned margin calls, and I accept them. My own R6 reason for PAIR-045 said it sits at the boundary.
    - PAIR-015 is kept as same type: the inverse is already supplied by (b)(i).
    - PAIR-045 is kept as a mixed branch: s(0) = 0 is implicit, and a numerical distance is required.
- **Converted mixed branches.** 15 of the 16 sampled are related (14 branch, 1 same type). The exception is BP-32, a modulus–line intersection in terms of a, judged not related.
- **Nonordered pairs made same type.** 4 of 4 are related; 2 were judged branches rather than same type.
- **New family candidates.** All 6 agree on related or not related.
- **Batch-rewritten rejections.** As decisions, 5 of the 6 sampled hold; BP-12 is a harder branch. See R7-04 for their text.
- **Neutral labels.** "Relation not established" is used, and the stale "no verified relation recorded yet" wording is gone from the map and the insights.
- **Empty-demand families.**
  - All 61 have dispositions.
  - 27 of the 41 members with examined demands now sit in a family whose assessed demands cover them.
  - For the other 14, the author's reason holds in 8 of the 10 families (R7-03).
  - implicit-given-point-gradient now carries D01, "Differentiate implicit curve".
- **Named fixes, all verified in the records:**
  - **D.1:** every named misfit moved, or limited to the right parts:
    - Try Now 35(e)/37(b) → identity-fraction-cancellation;
    - Goldie Worked illustration 1 → its own support family;
    - 5A Q8(i) → tangent-normal-at-point;
    - 9B Q1(iii) reason corrected and the "square" progression removed;
    - Examples 5.2–5.4 and 8H Q2(ii) → affine-reciprocal-proper-definite-integral;
    - YM Revision 5 Q3 and Goldie 10F Q11(i) moved out of vector-division-position.

    quadratic-exponential-recovery is merged as a retired alias. modulus-quartic-root-count now names the "show two roots by sketching" task.
  - **D.2:** the doubled prefix count is 0. The two precision contradictions are fixed, and the `limits` note is present.
  - **D.3:**
    - YM C12 Try Now 17 Q1(b) is tan²x with √3/3 − π/6.
    - Example 12(c) (PDF 174) and Example 12 (PDF 122) are registered.
    - Goldie 3D Q9(ii)/(iv) now carry the smallest positive angles.
    - Eight completed-square results are in completed form.
  - **D.4:** answer pages 612 and 653 are fixed, and the four page observations corrected.
  - **D.5:** Goldie C10 Teaching-figure 22 is a worked-solution panel and YM C4 Teaching-figure 13 a given. One long-division rule now covers both books. 19 vector-grid figures count as diagrams. Three own-sketch readbacks are counted.
  - **D.6:** the 2021 P1 Q5(a) branch now reads as a cosine quadratic. In the principal-inverse section, the held 2023 P1 Q9 is excluded from design anchors and four Cambridge comparators are named.
  - **D.7:** all 3,940 note fields are marked damaged, and the R6 report statement is corrected.
  - **D.8:** the map's input hashes match the final inventory and families.
- **The per-objective map** recomputes: by demand, 73 have same-type practice (69 in R6), 64 have only variant or other practice, and 1 has none.

## B. Findings

### R7-01 (medium): all 12 nonordered pairs kept rejected are related

- **What was found.** Under B.1, R7 kept 12 nonordered pairs rejected because "more than two substantive differences remain". Blind reviewer agents judged all 12 related: 4 same type and 8 structural branches. This is the whole set, not a sample.
- **The cause.** Each pair was judged against one member or a whole multi-part example, not against the best member's matching sub-part. The author's own reason says "any isolated subpart counterpart must be separately selected", but none was selected.
- **Verified on the pages.** The motion-vertical-events family was rejected against 2021 P1 Q4(a), 2021 P1 Q4(b) and 2023 P2 Q9(b), and every reason discusses only Example 39. But the same family contains YM C7 Try Now 39 Q1 (PDF 366), whose part (c) says "(i) Find an expression for s in terms of t. (ii) After 4 seconds the ball hit the bottom of the shaft. How deep was the shaft?" Exam 2021 P1 Q4(b) asks "How far is the object from O after 3 seconds?" after v has been found in (a). That is the same task.
- **Map impact.** All 12 exam parts already have other relations, so the impact is small. Some parts gain their first same-type counterpart, for example 2023 P2 Q9(b) and 2021 P1 Q4(b).
- **Evidence.** `kept-rejections-r7.json` lists all 12, with the agents' best members and sub-parts.

### R7-02 (low–medium): one gap relation does not hold, and two gap records need small fixes

- **2023 P2 Q4(c)** asks to solve log y / log 5 = 4 log 5 / log y, giving y = 25 or 1/25.
  - It is recorded as a mixed branch of Goldie 2B Q10(ii), 5²ˣ + 5ˣ − 2 = 0.
  - The agent found four substantive differences: the set-up, a pure square rather than a factorised three-term quadratic, keeping both roots rather than rejecting one, and the direction of back-substitution. The textbook item trains the opposite habit, discarding a root.
  - The author's own note says no rational-log reciprocal equation was located. The part should be a bounded no-match search, with Goldie 2B Q10(ii) named as the closest rejected item, unless a closer item is found (for example, an equation in log_a x and log_x a).
- **2024 P1 Q9(c)** contradicts itself. It selects YM Example 16(f) as a mixed branch, but its search note says "Closest rejected: YM Example16(f) … bounded search leaves a visible gap". Make the note and the decision agree. My agent judged the pair an easier branch.
- **2023 P2 Q2 search note.** It should name the nearest related practice the agent found: reconstructing a quadratic from its graph (YM Examples 26–27 and Try Now 27, PDF 35–37; Goldie 1B Q7(i)). These are mixed branches, not modulus counterparts.

### R7-03 (low–medium): two empty-demand families do contain examined practice

- **trig-point-value-parameter-support.** All three members (YM C4 Example 58 and its Try Now items, PDF 226) need exact special-angle values, M1:T6:O03:D01. The Try Now items use cos(π/3), cos π, sin(π/6) and sin(π/2). Assign that demand and decide the family's candidates.
- **exponential-scale-context-support.** No single demand covers all six members, but four are posed, exam-style items in two groups:
  - the doubling geometric-progression items, Goldie C2 Prompt 1 and Exercise 2A Q6, are close to 2024 P1 Q4(a)/(b);
  - the exponential/log model-solving items, Exercise 2B Q13 and Q14(iii), are close to 2021 P2 Q4(b).

  Split the family, or record member-level relations, and decide the candidates.
- **explicit-second-derivative-zero** (assigned D02).
  - Both members (y = x e^(−x/2)) mainly test the product rule and the exponential chain rule.
  - 2022 P2 Q5(a) (y = 6x e^(x/3)) is a near-identical exam part.
  - Add the product-rule demand at family level, so this pair is compared.
- **Smaller points:**
  - differentiation-conceptual-proof-support's reason says "product rule" where the recorded demand is the quotient rule.
  - One rule is needed for unposed prompts: the same-gradient family's unposed "?" prompt is treated as directly assessed, while Goldie C3 Prompt 3 stays support only.

### R7-04 (low): the 403 rewritten rejection reasons are templates, not part-specific reasons

- **The template.** B.4 asked for a reason that names the part's actual task. Every rewrite follows the same pattern: `<part id> asks: <raw extracted exam text> Source comparison: <first sentence of the R6 reason> Relation not established for the selected textbook response; no absence-of-practice claim follows.`
- **Script results** (`tools/textbook-relation-decisions-r7.json` → `batch_rejection_rewrites`):
  - The source sentence repeats: 88 distinct sentences across 403 records, one used 12 times.
  - 346 of the R6 reasons had a part-specific closing sentence, and the rewrite dropped it. For example, 2022 P2 Q1(b) lost "the target instead asks the learner to reuse that algebraic modulus result with a positive exponential input and use logarithms".
  - 11 are cut off mid-sentence, e.g. "it does not perform Relation not established".
  - At least 46 paste garbled extraction text, e.g. "∫ 6 π (6 sin2 x + tan2 2x)dx = 1 3 π − 3 4".
- **Impact is limited.** The rejection decisions themselves mostly hold (5 of 6 sampled), and step 3 treats a rejection as "relation not established". The R7 report's "part-specific batch rejection rewrites" overstates the work.
- **Fix: do not rewrite all 403 again.**
  - Mark them with a status that says what they are.
  - Restore the R6 closing sentence where it was specific, dropping only the batch phrase.
  - Fix the 11 truncations.
  - Correct the report.

### R7-05 (low; limitation for step 3): rejections in general under-call relations

- In R6 about a quarter of the sampled non-nonordered rejections were related, and in this check 1 of 6 batch rejections was.
- R7-01 shows the mechanism: judging a family through one member.
- About 1,750 main rejections remain. Treat "rejected" as "relation not established" and the same-type and branch counts as lower bounds; this extends R6-03.
- When step 3 builds a recipe, it should search the family's members and item-level demand links (union links, R5-03), not only the recorded relations.

### R7-06 (cosmetic): new author prose still loses spaces

The new text loses spaces in places:
- correction entries, e.g. "Question(c) asks3cosx+2; worked graph is3cos2x−1";
- insight headings, e.g. "Injectivity,restricted inverse rules";
- method strings.

This is readable but sloppy. Fix it where convenient; it is not a blocker.

## C. Not findings

- **Answers stored as rational forms of rounded decimals** (e.g. 64/5 for 12.8 km, where the exact value is √164) are this record's convention for requested rounded answers. They were accepted in R5 and are not an error.
- **Three selected labels are not printed labels:** "line-sketch", "b" and "a-intercepts". They are descriptive sub-part names for printed parts and were found unambiguously.
