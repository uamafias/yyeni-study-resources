# Findings — step-3 design review, NSSCAS Mathematics 8227

Reviewer: Claude Opus 5.5 (cross-vendor REVIEWER; Codex is PLANNER). Date: 2026-11-23. Frozen inputs: `inputs.json` (plan manifest `dd0e5cfe…`, content digest `20b77f69…`, analysis snapshot `5aaa3bf2…`, HEAD `fa0a09d4`). Owner decisions taken during this review: `owner-decisions-2026-11-23.md`.

## Method

- **Close-out confirmation.**
  - A fresh-copy rebuild of the R7 close-out, run twice.
  - The seeded negative fixtures.
  - A full hash comparison of the accepted analysis.
  - One agent rendered both pages of all 12 R7-01 pairs and the R7-03 family pages, then recomputed the counts from the ledgers (`check-closeout.json`).
- **Design review.** Six agents read the PLAN, contract, subject rules, app handoff, nine work orders, nine exemplars, coverage plan and part-evidence register.
  - Agent outputs:
    - `check-trig.json`: principal inverse and R-form.
    - `check-calc1.json`: implicit normal and stationary points.
    - `check-calc2.json`: motion and log-linear.
    - `check-visual.json`: modulus and trapezium.
    - `check-vector-contract.json`: vector recipe, contract and rules.
    - `check-coverage.json`: 138 demands and 67 groups.
  - What they did:
    - Recomputed all 45 exemplar cases with sympy or exact fractions.
    - Enumerated every admitted domain with code.
    - Rendered about 100 native pages: questions, NSSCAS examiner-report award tables, Cambridge mark schemes and syllabus pages.
- **My own checks.** I verified the following myself:
  - The examiner-report award tables behind both visual blocking findings: 2023 report PDF 331, "a = −2 www, b = −3 www, c = 2 www"; and 2025 report PDF 358, Q4(b) "B1 F.T. From Their graph".
  - `8227:CONVENTION:076` in `analysis/marking-conventions.json` ("No marks are awarded if only answers are given", 2021 report PDF 236).
  - The answer-only rules in the principal-inverse, R-form and vector work orders.
  - The stationary-inflexion method wording.
  - The 72 inverted close-out reasons.
  - The rebuild.

Severity:
- **Design-blocking:** must be fixed before owner approval.
- **Should-fix:** correct in the same repair.
- **Later-test:** for stage E/F.
- **Note:** an observation.

---

## A. R7 close-out: confirmed, with three residual corrections

| Item | Result |
|---|---|
| R7-01, 12 re-decided pairs | **Confirmed.** All 12 are stored with decision, direction, best member and sub-part, dated 2026-11-23. Both pages were rendered for all 12; the decisions hold. Label consistency: S3-10(c). |
| R7-02, gap records | **Confirmed.** 2023 P2 Q4(c) is a bounded no-match naming Goldie 2B Q10(ii). The 2024 P1 Q9(c) note agrees with its decision. 2023 P2 Q2 keeps the no-match and cites YM PDF 35–37 and Goldie 1B Q7(i). 13 parts with no relation recompute exactly. |
| R7-03, families | **Partly.** Family demands are stored, the candidates are exactly the parts assessing them, the quotient-rule fix is present, and 7 decisions hold on the pages. The 2021 P2 Q4(b) reason fails: S3-10(b). |
| R7-04, templated reasons | **Partly.** 403/403 records carry the template status, the 11 truncations are fixed and the report wording is corrected. The restoration inverted 72 reasons: S3-10(a). |
| R7-05, limits note | **Confirmed.** Present in the objective map (JSON and md), insights, relations and gap-search files. |
| Counts | **Exact.** 2700/207/895/1775 before and 2718/211/910/1777 after recompute from the ledgers, and the deltas reconcile row by row. |
| Rebuild | **Passes.** Two fresh-copy passes in my own copy, 285 commands each; all 275 outputs identical to each other and to the author checkout. The seeded negatives are recorded in `inputs.json`. |
| Analysis during stage D | **Unchanged.** 8,242 of 8,246 snapshot-pinned files match. The 4 that differ are the stage-transition documents (two STATUS.md files, HANDOVER.md, capability-gaps.md), so `freeze_analysis_r7_closeout.py --check` now stops at STATUS.md (S3-11). |

---

## B. Stage-D design: what passed

- **Mathematics.** All 45 exemplar cases recompute correctly.
  - The one rounding mismatch is a premature-rounding effect, not a wrong answer: the R-form normal case gives 330.4, or 330.5 if both angles are rounded to 2 dp; see S3-06.
  - Five official exam answers recompute: 2025 P2 Q5 −15/4, 2023 P2 Q8 −4, 2021 P2 Q10(b), 2021 P1 Q11 and 2024 P2 Q10.
- **Domains.** Every claimed capacity reproduces exactly: 24+24; 78 (from 90 raw); 42+42; 540+180; 144/60/27; 30 models (270 presentations)/40; 108; 36; 54.
- **Every admitted instance is mathematically valid.** No instance is degenerate:
  - every implicit point lies on its curve, with a finite nonzero gradient;
  - each two-extrema instance has exactly two extrema;
  - every inflexion is a genuine stationary inflexion;
  - every reversal is a simple root strictly inside the interval;
  - every R-form tuple has two distinct roots inside (0°, 360°);
  - every trapezium interval has one-signed concavity;
  - the modulus graphs have no vertex on an axis and no missing intercepts;
  - the vector instances have no zero or parallel vectors.
- **Coverage accounting.** Every count in the PLAN recomputes from the JSON:
  - 9/15/45/28; 38 of 138 demands; 25 of 60 objectives; 100 later; 12/55 of 67 groups;
  - Bloom 1/11/3, with branch maxima computed per branch;
  - deck totals 14/20/17.

  All 138 demands have a disposition, none is claimed as complete, and the held originals are never learner anchors.
- **Same-type references.** Checked per part on native pages. They are right for:
  - principal inverse (admissible branch: Cambridge 9709/12/F/M/16 Q4(a));
  - R-form roots (2022 P2 Q6(b)(i));
  - implicit gradient (2025 P2 Q5);
  - motion;
  - log-linear;
  - modulus (2023 P2 Q2);
  - trapezium (2023 P2 Q6);
  - vector part (b) (2025 P1 Q3(b)).

  Vector part (a) is withheld for a wrong reason (S3-08). Cambridge is never labelled Namibian.
- **Diagrams.** The six modulus and trapezium paper diagrams and the three log-linear diagrams match their exemplar values. The must-read givens are listed (R3-07).
- **Contract and handoff.**
  - `recipe-contract.md` covers every playbook work-order field without contradiction.
  - The capability documents claim no untested runtime support.
  - Owner decision 6 is respected: all 13 sketch parts are included.
  - The PLAN stops at the owner checkpoint and puts cross-vendor review before release.
- **Selection.** Justified as a framework pilot. 11 of the 15 most-assessed demands (2021–2025, by marks) are touched. Each of the three largest groups left out is visible in the coverage plan: function analysis, numerical roots and constrained optimisation.

---

## C. Findings

### S3-01 (design-blocking, shared). Adapted marking departs from the official schemes without saying so

**Root cause.** `subject-rules.md` does not state the NSSCAS general marking rules:
- "No marks are awarded if only answers are given" (`CONVENTION:076`, `:002`; 2021 report PDF 236, 2025 PDF 355);
- the "hence" rule;
- a misread rule (2025 PDF 345);
- whether a correct 3 s.f. decimal earns A when exactness is not requested;
- units.

Each work order therefore invented its own rule (vector-contract-09/10/11). Owner decision OD-1 now fixes the answer-only rule.

| Kind | Instances (agent IDs) |
|---|---|
| Bare answers earn credit | Principal inverse: a bare x earns 2/2, though the stem says "showing the principal-value step" and no criterion credits that step (trig-01). R-form "Hence": a naked pair of roots earns 2/4, and a non-hence method earns 4/4; the official cap is SC1 (trig-06; 2023 PDF 337, 2022 PDF 301). Implicit: bare gradient 1/5; bare normal 2/7, including an M mark (calc1-01). Stationary points: coordinates alone 2/4 and 1/3 (calc1-02). Motion and log-linear: S3, E5, R3, R6, G-A1/A2, T-A1, U-A1 (calc2-06). R-form (a): R and α alone 3/3 (trig-12). |
| Official qualifier dropped | Modulus: "www" removed from all three B1s, so the examiner-flagged parabola route earns 3/3 in the 36 d = 1 tuples, including the normal exemplar (visual-01). Motion exponential: the official "coefficient not ±V/k" exclusion and "must be an attempted integral" condition are missing (calc2-01). Trapezium (d): no follow-through from the learner's own sketch, so a wrong sketch is penalised twice; the board awards "B1 F.T. From their graph" (2025 PDF 358), and the table and paragraph contradict each other (visual-04). |
| Stricter than the official scheme | Trapezium b:B1 requires both factorising and the log law, where the official mark is for 3 ln(x−2)² alone (visual-05). Log-linear G-M2/G-B1/T-B1 versus the official "state or imply" and DM1 (calc2-07). Vector a:B1 is narrower than the source B1 (vector-contract-06). Principal V-M1 demands an exact ratio, while Cambridge accepts −0.866 at M1 (trig-05). The implicit normal lacks the official DM1 line-construction mark: 2 marks where both official tables give M1, DM1, A1 (calc1-09). |
| Valid method not credited | Stationary inflexion: the first-derivative sign test alone, which the syllabus ("by any method") and the 2025 report (PDF 351) accept, is not credited on its own (calc1-03, design-blocking). Principal: the substitution-contradiction argument (trig-04). Log-linear: the correct ln/lg change-of-base route (calc2-16). |
| Accuracy and form rules missing or contradictory | Vector A1 demands "exact p" though the stem never asks for exact, and 44 of 54 values of p are fractions (vector-contract-01, design-blocking). Motion: accepted forms for recurring answers are not stated (calc2-09), and units are demanded by criteria but never by the stems (calc2-10). |

**Repair.**
1. Add the general rules to `subject-rules.md`, with locators, applying OD-1.
2. Then, for every criterion adapted from an official award row, carry over the official qualifiers (www, F.T., DM, exclusions, "state or imply", SC caps), or record a named deviation for owner approval.
3. Credit every valid method the syllabus and the board accept.

### S3-02 (design-blocking). Admitted instances where a named error gives the right answer

A diagnostic bank must be able to tell the targeted error from correct work, yet several domains admit instances where it can't:

- **Motion, exponential branch:** k = 1 in 20 of 60 tuples, including the "changed" exemplar. There, d/dt(Ve^−t) equals the primitive, so differentiating and integrating can't be told apart and there is no chain factor (calc2-02).
- **Log-linear, gradient-target:** in 30 of 40 tuples the wrong rule a = b·m gives the right a. Only (b, m) = (3, 2), the 2025 source itself, separates them (calc2-08).
- **Modulus:** the parabola model fits all four labelled points in 12 tuples, and "b = y-intercept" gives the right b in 8 more (visual-02). The parabola route reaches the right a in all 36 d = 1 tuples (visual-01).
- **Vector:** the reported common error p(OA − OB) gives the correct p = 0 in all 6 p = 0 tuples, and the identity 0 = 0 in 3 more (vector-contract-05).
- **Implicit:** k = 1 in 14 of 42 tuples assesses no chain rule, although O01:D02 is listed as direct (calc1-06; should-fix).

**Repair.**
1. For each branch, list the named errors from the examiner report and the work order.
2. Exclude any admitted instance where a named error yields the canonical answer, or keep it only as a disclosed non-diagnostic practice instance.
3. Recompute the capacities and record the check.

### S3-03 (should-fix). Exam originals sit inside the generated pools

Six cited exam questions are admitted as unattributed generated instances:

| Exam original | Recipe | Agent ID |
|---|---|---|
| 2021 P1 Q4 | Motion | calc2-03 |
| 2023 P2 Q9 | Motion | calc2-03 |
| 2025 P2 Q6 | Log-linear | calc2-03 |
| 2025 P2 Q5 | Implicit | calc1-05 |
| 2023 P2 Q2 | Modulus | visual-03 |
| 2023 P2 Q6 | Trapezium | visual-03 |

The log-linear boundary exemplar's part (a) is 2025 P2 Q6(a) word for word. The motion work order itself says originals never appear as generated variants.

**Repair.** Exclude these tuples from the fresh pools, or serve them only as attributed originals, and replace the log-linear boundary exemplar.

### S3-04 (should-fix). Some branches don't assess the decision they claim, including all three Analyse labels

- **Principal inverse.**
  - The admissible branch never credits the range check.
  - The obstruction branch always has the answer "no", the stem names the method, and k never matters (trig-02, trig-03, trig-04).
- **Stationary inflexion, Analyse 4.**
  - The prompt cues the test, and every one of the 180 instances has the same outcome (calc1-04).
  - Nothing requires telling an extremum from an inflexion. A quartic a(x−h)⁴+c with f''(h) = 0 at a maximum or minimum would make it a real decision.
- **Motion, interior reversal, Analyse 4.**
  - Velocity is linear and triangles earn full credit, so 6/6 needs no integration although the parts are linked to integration demands.
  - The rest-time part cues the split.
  - The rest part's differentiation link does not fit (calc2-04, calc2-05).
- **Trapezium (d), Analyse 4.** The answer is "under-estimate" in all 36 instances, and the official scheme accepts "the curve is concave" (visual-08).

The PLAN's 3 Analyse labels are exactly these three. All three fail as specified.

**Repair.** For each branch, either make the decision live, or relabel the part Apply and recompute the branch maxima and the Bloom counts. Ways to make it live:
- one principal-inverse branch, "solve or explain why there is no real solution", that draws targets from both sets;
- mixing quartic flat extrema into stationary inflexion, without the cue;
- a quadratic velocity with one interior simple root;
- a later branch where the trapezium bias varies.

### S3-05 (should-fix). Capacity counts surface variation as distinct problems

| Recipe | Claimed | Actual variation (agent ID) |
|---|---|---|
| Principal inverse, range-obstruction | 24 | 6 targets, all with the same conclusion (trig-03) |
| R-form, part (a) | 78 | 16 distinct prompts with 11 distinct α (trig-10) |
| Vector | 54 | Part (b) has 18 problems, each repeated three times; A = C in 18 of 54, and then part (a) computes part (b)'s dot product (vector-contract-03/04) |
| Trapezium | 36 | 4 distinct (a) computations, 12 (b) answers, 3 sketches and 1 (d) answer (visual-07) |
| Stationary points, two-extrema | 540 | 60 shapes × 9 vertical shifts, closed under mirroring (calc1-13) |
| Implicit | 42 curves | 36 curves; 42 point-tasks (calc1-07; PLAN.md:50) |
| Motion | 144 / 60 | Numeric rescaling of one decision (calc2-12) |

**Repair.**
1. Report a decision-level (semantic) capacity per part next to the raw count.
2. Key no-repeat on part-level identity.
3. Exclude A = C in the vector recipe.

### S3-06 (should-fix). Rounding knife-edges and accuracy rules

- **R-form.**
  - 6 tuples flip with 2 dp intermediates, including the normal exemplar (330.45 → 330.5 against the memo's 330.4).
  - Two tuples sit within 0.0001° of a boundary (trig-09).
  - The quadrant-class sentence is wrong: positive c keeps the anchor's pattern in only 7 of 78 tuples (trig-07).
  - The rule capping answers at two roots is ambiguous for coterminal values such as −29.6 (trig-08).
- **Vector:** 3 s.f. intermediates change the 1 dp angle in 15 of 54 tuples, including both the normal and changed exemplars (vector-contract-07).
- **Trapezium (b):** in 18 of 36 tuples, 2k × (3 s.f. a) differs from the canonical value, and the stem states no precision (visual-06).

**Repair.** Exclude knife-edge tuples, or state the premature-rounding rule (M marks survive, A0 with "premature rounding" feedback). Give each instance an accepted-answer set, and correct the quadrant sentence and the cap rule.

### S3-07 (should-fix). Official sources the planner didn't read

- **Implicit.** The normal facet is called "textbook-derived" and "no normal awards official", but 2021 P2 Q10(b) (with its normal award table) and 2021 P1 Q11 belong to the implicit exam family (calc1-08). The grade-c calibration claim cites C:13, which doesn't mention implicit differentiation; that skill appears only at grade a, A:14 (calc1-10).
- **Stationary points.** 2021 P1 Q11(a) and 2023 P2 Q5(a) were not read. The decisive dual-method wording in 2025 P1 Q9(c) (report PDF 351) is not cited (calc1-12).
- **Trapezium.** 2025 P2 Q4, the board's bias-from-their-graph award, was not read (visual-04).

**Repair.** Read and record these sources, relabel the normal facet as examination-observed, and correct the grade claim.

### S3-08 (should-fix). Record inconsistencies

- **Vector part (a)** claims O02:D03, which no criterion assesses, and omits O02:D01 (add and subtract vectors), which a:B1 assesses. The PLAN (line 60) uses this mistake to withhold the part (a) same-type label (coverage-01, vector-contract-02). With D01 in, the demand set equals the source part's, so decide the label again on form, givens and scaffold. Part (a)'s display reason is copied from part (b) (vector-contract-08).
- **Trapezium** primary objectives for (b) and (c) differ between the work order, the register and the JSON (coverage-04, visual-09).
- **Part-evidence register:** 14 of 28 slots reuse a recipe-level rationale, and two cite criteria from the sibling branch (coverage-05, calc1-15). Work-order prerequisites are missing from the JSON (coverage-06).
- **IDs:** three selection-ID schemes are in use. The three calculus work orders defer their selections and per-part demand IDs to `calculus-design.json`, and six work orders omit the classification version (vector-contract-13).
- **Implicit normal label:** the "same type" label has no part qualifier (calc1-11; later-test).

**Repair.** Make the work orders, register and JSON agree, and normalise the ID scheme.

### S3-09 (should-fix; owner decided). Pilot breadth claims

- **No show-that part.** No part is "show that", against 44 exam parts and 131 of 750 marks (coverage-03). OD-2: add one show-that part. Its answer-given marking: all credit for working, no follow-through to the given answer, and the final mark only if the preceding work is correct.
- **"Modelling" claim.** PLAN line 15 claims "modelling", but no part assesses model construction (`ABILITY:08`: 10 exam parts, 26 marks; coverage-02). Correct the claim, or add a part.
- **Exam weight.** `coverage-plan.md` has no exam-weight column, so the owner can't see what the later batches weigh (coverage-07).
- **Deck label.** The "Visual evidence" deck includes the vector branch, whose givens are text only (coverage-08).

### S3-10 (should-fix). R7 close-out residuals

- **(a) Inverted reasons.** In all 72 records whose R6 reason said "None of these targets asks / requires / requests / credits / uses X", the restored text now says "this exam part asks X". That reverses the meaning: 2021 P1 Q8(b) is now said to ask for an AP term position (closeout-01; I verified the count). The decisions are unaffected, but the objective map shows this text to planners. Codex's check only tested that the text was present.
- **(b) Wrong rounding claim.** The 2021 P2 Q4(b) reason says the exam "requires floor rather than nearest rounding" and uses that to make the branch mixed. The official row (2021 report PDF 238) gives t = 34 and "Accept: 35", which is the conflict recorded in `CONVENTION:009` (closeout-02). Re-judge the direction (likely harder).
- **(c) Two rules in use.** BP-09 and BP-27 (same type) and BP-08 (harder) compare polynomial textbook integration with 2023 P2 Q9(b), whose direct demands include exponential integration. In the same close-out, BP-24 and BP-31 count a missing exponential derivative as making the textbook easier (closeout-03). Apply one rule.
- **Notes.** BP-37's stored check value is 0.744018; it should be 0.744207 (closeout-04). The 2024 P1 Q4(b) reason says the Goldie prompt uses logarithms, but the page says powers of 2 (closeout-05). Lost spaces recur (closeout-06).

### S3-11 (note). The freeze check now fails on stage-transition documents

The R7 snapshot pins STATUS.md, HANDOVER.md and capability-gaps.md, so `--check` stops at the first status edit. The analysis itself is unchanged (section A). Either exclude status and handover documents from the next snapshot, or record their transition hashes in a check that accepts them.

---

## D. Later tests and notes (no repair needed now)

- **Later tests (stage E/F).**
  - Label placement in the log and modulus diagrams (calc2-13, visual-11); the trapezium asymptote rendered solid instead of dashed (visual-12).
  - α values that sit near a 2 dp rounding boundary (trig-16).
  - Vertical tangents near the supplied point (calc1-14).
  - Vector and LaTeX input acceptance (vector-contract-14).
- **Notes.**
  - The accepted surd forms in R-form (a) (trig-11), and the out-of-range c in an exclusion example (trig-13).
  - The anchor's quadrant scope disclosure (trig-14), and the extent of the principal-range diagram (trig-15).
  - Instances with x = 0 by inspection, and the mostly negative answers (calc2-11); every reversal starts in the negative direction, and 9 of 27 have zero displacement (calc2-12).
  - A = e^integer (calc2-14), and "Hence" and positivity givens not kept consistently across the stems (calc2-15).
  - The trapezium (b) demand double counts (visual-13), its extra scaffolds (visual-14) and premature rounding (visual-15). The 2023 "First Proof" paper is corroborated by the report (visual-16).
  - A rule for multiple submitted answers (vector-contract-12), the review gate wording (vector-contract-15) and the owner-decision locator (vector-contract-16).
  - The 12/55 group split undercounts partly exercised groups (coverage-09).

## E. Not checked

- App runtime, rendering, MCP delivery and generators: none exist yet.
- Grade-descriptor pages beyond those cited.
- Textbook pages beyond the members named in the work orders.
- Cambridge searches for further same-type references.
- Whether the accepted question→demand links are correct; they were accepted in earlier rounds.
