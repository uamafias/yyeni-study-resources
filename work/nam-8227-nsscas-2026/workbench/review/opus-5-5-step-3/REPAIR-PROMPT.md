# Stage-D design repair (D1): marking, domains and records before owner approval (NSSCAS Mathematics 8227)

You are Codex, the PLANNER for the 8227 Workbench pilot. The workspace is `work/nam-8227-nsscas-2026/`. Vitalis's decisions are final.

## Where the plan stands

Claude's step-3 review (2026-11-23) has two parts.

**It confirms the R7 close-out.** Three residual text corrections remain, in item 10.

**It finds the stage-D design sound** in selection, structure and mathematics:
- all 45 exemplars are correct;
- every capacity reproduces;
- no admitted instance is degenerate;
- coverage accounting is exact.

**The marking is not ready.** Design-blocking defects affect 7 of the 9 recipes.

**Read first,** all in `workbench/review/opus-5-5-step-3/`:
1. `report.md`;
2. `findings.md` (S3-01 to S3-11);
3. `owner-decisions-2026-11-23.md`.

**Agent evidence,** with exact locators, computations and native page references, is in `check-trig.json`, `check-calc1.json`, `check-calc2.json`, `check-visual.json`, `check-vector-contract.json`, `check-coverage.json` and `check-closeout.json`. Each finding lists its agent IDs; read those records before changing a recipe.

**Owner decisions (2026-11-23, binding):**
- **OD-1:** follow the NSSCAS rule. A bare answer earns no marks unless the official scheme for that question type awards it. Practice feedback still tells the learner the answer is right and asks for the working.
- **OD-2:** add one show-that part to the pilot.
- **OD-3:** repair, then Claude makes a short check, then Vitalis approves. **Do not reopen the recipe selection.** Branch changes are allowed only where this prompt names them.

**Before changing anything,** copy `planning/plan-manifest.json` (sha256 `dd0e5cfe8fdb2dbb807f07bf2348c36d6a3824e934e81a1eeb9a989d04d6ba9f`) to `planning/history/plan-manifest-d0.json`, and keep the D0 candidate files recoverable.

## 1. S3-01: shared marking rules, then every adapted criterion

1. In `subject-rules.md`, add the NSSCAS general rules with their locators:
   - answers only (`CONVENTION:076`, `:002`; 2021 report PDF 236, 2025 PDF 355), as decided in OD-1;
   - "Hence": a method that does not use the hence result earns at most the official SC, unless the stem says "hence or otherwise";
   - misread, per 2025 PDF 345;
   - exact versus decimal: when exactness is not requested, a correct 3 s.f. decimal earns the A mark;
   - premature rounding: M marks survive and the A mark is lost;
   - units: required only when the stem asks for them;
   - multiple final answers.
2. In each work order, replace the local answer-only sentence with a reference to these rules and an explicit per-part statement.
3. For every criterion adapted from an official award row, carry over the official qualifiers (www, F.T., DM, exclusions, "state or imply", SC caps), or record a named deviation with its reason for Vitalis.
4. Fix at least these, each traced in `findings.md` S3-01:
   - **Principal inverse.** Fix the stem and criteria mismatch (trig-01). Allow a decimal forward ratio at V-M1 (trig-05). Credit the substitution-contradiction argument (trig-04).
   - **R-form.** Apply the hence cap and the answer-only rule (trig-06, trig-12).
   - **Implicit.** Answer-only credit goes to 0, and N1 is never an M mark without the perpendicular step seen (calc1-01). The normal part becomes M1 perpendicular gradient, DM1 line through the point, A1 (calc1-09).
   - **Stationary points.** Apply the answer-only rule and require the f' = 0 solving step to be seen (calc1-02). I5 and I6 are each earned by any one valid method: the f' sign test alone, or the f'' sign change with f'(h) = 0 (calc1-03; cite 2025 P1 Q9(c), report PDF 351).
   - **Motion.**
     - E2 gets the "coefficient not ±V/k" exclusion, and E4 requires an attempted primitive (calc2-01).
     - Apply the answer-only rule (calc2-06).
     - State the accepted forms for recurring answers (calc2-09) and the unit rule (calc2-10).
   - **Log-linear.** Align G-B1 and T-B1 with "state or imply", and G-M2 with the official DM1, or record the deviation (calc2-07). Credit the correct ln/lg route (calc2-16).
   - **Modulus.** Restore www on all three B1s and add a feedback row for the parabola route (visual-01).
   - **Trapezium.**
     - d:B1 becomes F.T. from the learner's own sketch, citing 2025 P2 Q4(b) (report PDF 358). Shape errors are penalised only in (c). Define the case where no sketch is drawn. Resolve the table/paragraph contradiction (visual-04).
     - b:B1 credits the factorised form alone (visual-05).
     - c:B1 gets an explicit feature checklist (visual-10).
   - **Vector.**
     - Either the stem asks for an exact p, or a 3 s.f. decimal is accepted; exact 60° and 90° earn b:A1 (vector-contract-01).
     - a:B1 accepts the scaled vector minus OB (vector-contract-06).
     - Add a premature-rounding rule and sample (vector-contract-07).
     - Add a misread sample (vector-contract-10).

## 2. S3-02: a discrimination invariant for every branch

1. For each branch, list the named errors from the examiner report and the work order.
2. Exclude every admitted instance where a named error gives the canonical answer, or keep it only as a disclosed non-diagnostic practice instance.
3. Write the check as a script, and record per branch the errors tested and the instances removed.

At least:
- **Motion exponential:** remove k = 1, for example by replacing it with another k, and choose a new "changed" exemplar (calc2-02).
- **Log-linear gradient-target:** m ∈ {2, 3}, or another domain where b^m ≠ b·m (calc2-08).
- **Modulus:** the 20 parabola and y-intercept tuples (visual-02), plus the d = 1 parabola cases once www is restored (visual-01).
- **Vector:** p(OA − OB) at p = 0 (vector-contract-05).
- **Implicit:** k ∈ {2, 3} (calc1-06), with a new "changed" exemplar.

## 3. S3-03: exam originals out of the fresh pools

Exclude these tuples from generation, or serve them only as attributed originals outside freshness:
- **2021 P1 Q4:** polynomial motion, (3, 1, 2, 3).
- **2023 P2 Q9:** exponential motion, (30, 1/2, 2).
- **2025 P2 Q6:** log-linear, (3, 2, 2, 4).
- **2025 P2 Q5:** implicit, (2, 3, −5).
- **2023 P2 Q2:** modulus, (−2, −3, 1).
- **2023 P2 Q6:** trapezium, (2, 8, 4, 3).

Then replace the log-linear boundary exemplar, which is 2025 P2 Q6(a) word for word (calc2-03, calc1-05, visual-03).

## 4. S3-04: make each claimed decision live, or relabel it

For each branch, either redesign it so the decision varies and isn't cued, or relabel the part Apply. Then recompute the branch maxima and the PLAN's Bloom counts.

| Branch | Problem | Ways to make the decision live |
|---|---|---|
| Principal inverse (trig-02/03/04) | The admissible branch never credits the range check; the obstruction answer is always "no", the stem names the method, and k never matters | One branch, "Solve … or explain why there is no real solution", drawing targets from both sets: B1 for the range comparison, then M1 A1 or B1 for the conclusion. Report capacity by target |
| Stationary inflexion (calc1-04) | Analyse 4 is cued, and all 180 instances have the same outcome | Remove the cue, and admit a(x−h)⁴+c instances where f''(h) = 0 at a maximum or minimum |
| Motion interior-reversal (calc2-04/05) | Linear velocity needs no integration, and the rest-time part cues the split | A velocity that needs integration, with one interior simple root, and no rest-time cue. Or relabel the integration demands and Bloom |
| Trapezium (d) (visual-08) | Analyse 4, though the answer never varies | Relabel Apply 3 |

The recommended direction is to keep the three Analyse decisions live where the change is small, because this pilot tests the framework's higher-order evidence. Record each choice.

## 5. S3-05: decision-level capacity and no-repeat keys

Next to each raw count, report the part-level semantic capacity and key no-repeat on it:
- principal obstruction, by target;
- R-form (a), by (a, b) and α;
- vector (b), by (r, s);
- trapezium, by (L, n, k), with its collision counts;
- stationary points, the shape and shift structure;
- implicit, "42 point-tasks on 36 curves", correcting PLAN.md:50;
- motion, numeric rescaling.

Also exclude A = C (r = t) from the vector recipe (vector-contract-03/04, trig-03, trig-10, visual-07, calc1-07, calc1-13, calc2-12).

## 6. S3-06: rounding and accuracy

- **R-form.**
  - Exclude (1, 4, ±3) and (4, 1, ±3), and handle the remaining knife-edge tuples by exclusion or the premature-rounding rule.
  - Choose a normal exemplar that is not on a knife edge.
  - Replace the quadrant-class sentence with the three classes and their b-M2 evidence.
  - Define the root cap, so that a coterminal value outside the interval counts as an extra answer (trig-07, trig-08, trig-09).
- **Vector.** Freeze the 15 rounding-sensitive tuples as stage E/F fixtures (vector-contract-07).
- **Trapezium (b).** State "3 significant figures" or cite the default, and give each instance its accepted-answer set (visual-06).

## 7. S3-07: read the missing official sources

Render and record each source in the reading manifests:
- **2021 P2 Q10 and 2021 P1 Q11.** Relabel the implicit normal facet as examination-observed, and keep 2021 P2 Q10(b) as a related reference (calc1-08).
- **2021 P1 Q11(a), 2023 P2 Q5(a) and 2025 P1 Q9(c)** (stationary points, calc1-12).
- **2025 P2 Q4** (trapezium bias, visual-04).

Correct the grade-c calibration claim: implicit differentiation appears only at grade a, A:14 (calc1-10).

## 8. S3-08: make the records agree

- **Vector part (a).** Put O02:D01 in and take O02:D03 out. Re-decide the (a) same-type label on form, givens and scaffold, then recompute the coverage counts. Write (a)'s own display reason (coverage-01, vector-contract-02, vector-contract-08).
- **Trapezium.** Give (b) and (c) one primary objective each, the same in the work order, the register and `visual-design.json` (coverage-04, visual-09).
- **Part-evidence register.** Write a part-specific Bloom rationale for every slot, citing only that branch's criteria. Add the work-order prerequisites to the JSON (coverage-05, coverage-06, calc1-15).
- **IDs.** Normalise the selection-ID scheme. Each calculus work order lists its accepted selections, its per-part direct and prerequisite IDs, and the classification version (vector-contract-13).
- **Implicit normal label.** Add a part qualifier to the "same type" label (calc1-11).

## 9. S3-09: show-that part and breadth claims (OD-2)

**Add one show-that part.** Suggested: in `WB8227-implicit-normal`, a part "Show that dy/dx = …" before the gradient or normal, on the pattern of 2023 P2 Q8(a). You may choose another placement if you justify it. Specify:
- answer-given marking: all credit for working; no follow-through onto the given answer; the final A mark only if the preceding work is correct and complete;
- its demands and Bloom level;
- its exemplars: normal, changed and boundary;
- its effect on capacity, counts and the deck totals.

**Other breadth claims:**
- **"Modelling" (PLAN.md line 15).** Correct the claim, since no part assesses model construction (`ABILITY:08`).
- **Exam weight.** Add an exam-weight column, with marks and parts for 2021–2025, to `planning/coverage-plan.md` (coverage-02, coverage-07). You may use the review's `check-coverage-demand-frequency.json` as a cross-check.
- **Deck name.** Rename or recompose the "Visual evidence" deck (coverage-08).

## 10. S3-10: R7 close-out residuals

- **Inverted reasons.** Fix the 72 restored reasons whose negation was lost. Write "This exam part does not …", or drop the sentence. Add a negative fixture: a restored R6 reason that loses its negation must fail (closeout-01).
- **2021 P2 Q4(b).** Correct the reason: the official row accepts 34 or 35 (`CONVENTION:009`). Re-judge the direction (closeout-02).
- **Integrand rule.** Apply one rule to polynomial versus exponential integrands: either relabel BP-09 and BP-27 as easier branches and BP-08 as mixed, or record why integrand kind is surface variation here but not in BP-24 or BP-31 (closeout-03).
- **Notes.** Correct BP-37's value (0.744207) and the 2024 P1 Q4(b) "logarithms" wording (closeout-04, closeout-05).

## 11. S3-11 (optional)

Make the freeze check accept stage-transition documents, either by excluding status and handover files from the pinned set or by recording their transition hashes.

## Deliverables

- **Updated design files:** PLAN, contract, subject rules, work orders, exemplars, design JSONs, coverage plan, part-evidence register and reading manifests. Include a new `planning/plan-manifest.json` with the recomputed counts.
- **`checks/plan-repair-d1-report.md`**, containing:
  - a disposition for every S3 finding and for every design-blocking and should-fix agent ID it lists, with file:line of the change or the reason for not changing;
  - before and after counts: capacities (raw and semantic), Bloom counts, part slots, demands and deck totals;
  - the discrimination check results per branch;
  - the exemplar recomputation, by a separately written oracle, for every new or changed exemplar.
- **`planning/OWNER-CHECKPOINT.md`** updated. Approval is still pending: Claude's short check comes first, then Vitalis approves.
- **STATUS.md and HANDOVER.md** updated.

## Checks before handing back

- Recompute all exemplars, including the new show-that part, with an oracle independent of the answer constructor.
- Enumerate every revised domain and report raw and semantic capacities.
- Run the discrimination script for every branch.
- Run the R7 close-out rebuild and fixtures again if any analysis record changed (item 10).

## Constraints

- Do not commit or push; Vitalis commits.
- **Do not modify** any review folder, source PDFs, `standard/`, other subjects, app code or pinned checkouts.
- **Scope:** no stage-E authoring, generators, runtime items, imports or learner assignments. No change to the recipe selection beyond the branch changes named here.
- **Sources:** textbook originals stay internal (`learner_display: false`). NSSCAS and Cambridge originals are shown only with attribution, and never as generated variants.
- **Acquisition:** use only the YYeni Web Harvester. Write no new scraping scripts.
