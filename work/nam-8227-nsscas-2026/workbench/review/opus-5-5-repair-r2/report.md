# Re-review report: 8227 analysis repair round 2

Reviewer: Claude Opus 5.5 (cross-vendor, role REVIEWER). Date: 2026-11-17. Inputs are frozen in `inputs.json`: HEAD `11cd03fe` with the repair uncommitted, current snapshot `85b782f9…74ee`, and the round-1 snapshot `1afe99d5…561f` preserved. Findings are in `findings.md`.

## 1. Verdict: accept named analysis scope

The repair resolves the round-1 blocker. Coverage now comes from direct part→demand links that I read part by part, not from family membership. The mapping is settled enough to turn groups into recipes, provided that:

- the two diagram crops in R2-01 are fixed before their branches are planned; and
- the recipe contract makes the R2-02 decision.

The other new findings are small corrections for the next author pass.

### Accepted

- **Integrity.** Source and snapshot integrity, and the deterministic rebuild: reproduced in a disposable copy, byte-identical, with both seeded errors rejected.
- **Mapping.** The 250 part annotations, with direct, prior-knowledge and model links kept separate. Corrections: R2-03.
- **Coverage.** The coverage computation and the 138 demand statuses: 126 NSSCAS-observed, 8 Cambridge-comparable, 4 syllabus-derived. Also the exact 12-demand gap list and the inflexion facet.
- **Dependencies.** The 76 typed dependency edges. Additions: R2-04.
- **Groups.** The 67 analysis groups as analysis groups: their decision boundaries, splits and merges, the `identity-extrema` departure, and the two grade-floor exceptions. This is not a recipe count.
- **Grade calibration.** The 46 grade descriptors, complete for pp19–24, and the per-group easiest/hardest grade bounds.
- **Syllabus and source records.** Qualifiers, limits and normalised objective text (spot-checked); the per-year assessment conditions (spot-checked); and the source-defect register, with owner decisions 1–3 applied.
- **Cambridge items.** All 30 Cambridge items. Each verbatim text matches its rendered page; printed pages, selected/omitted parts, scope checks and attribution labels are correct. One relabel: R2-06.
- **References and visuals.**
  - The examination-reference data model, and all 250 part-level "original" references with correct labels.
  - The per-part representation and response records.
  - 37 of the 39 crops.

### Not accepted, or outside this review

- The 2024 P1 Q9 and 2025 P1 Q12 crops (R2-01).
- Learner-facing "Same type as …" labelling, which is so far available for only 12 of 67 groups (R2-02).
- Recipe count and recipe economy, Bloom levels, criterion-level marking rules (R13-22), and textbook breadth (R13-23).
- Runtime sketch marking, diagram generation and app display. These are untested.

## 2. What the repair got right

- **Real decisions.** Every part's demands were judged independently of family membership. The judgements are conservative and correct in the cases that matter:
  - prior-knowledge "show that" models are no longer counted as calculus coverage;
  - quadratic inequalities are now counted where they carry marks;
  - held exemplars are kept out of coverage.
- **Honest evidence statuses.** Comparable Cambridge evidence never fills an NSSCAS count, and four demands remain openly syllabus-derived.
- **Good Cambridge selection.** The pre-2020 Paper 1s supply four unit-vector items and both segment items that 2020+ cannot. Tangency, division by a quadratic and monotonicity each have three items.
- **Two corrections to my round-1 material, both right:**
  - the iteration candidate is Q6(c), not Q9(c);
  - the single `comparable` status for principal values is consistent with owner decision 1.

## 3. Remaining-work list, in the agreed sequence

### Step 2: finish the outstanding source analysis (author)

These must be done before the PLAN is signed off.

1. **Fix R2-01.**
   - Re-crop 2024 P1 Q9 so it includes "B (90, −3)" and "f(x) = a sin x".
   - Re-crop 2025 P1 Q12 so it includes vertex D and the axis label.
   - Trim the text bleed in five crops.
   - Add the automatic crop-containment check.
2. **Apply R2-03 to R2-07.**
   - Special-angle links (1.6.3.1) in eight parts.
   - The 2023 P2 Q7(a) mis-tag.
   - Four secondary links.
   - Three dependency edges.
   - Split diagram parameters into `fixed`, `variable` and `relations`.
   - Relabel the s15/11 Q8(iii) Cambridge item.
   - Add a `learner_display: false` flag to held parts.
3. **R13-22: build the examiner marking-convention register.** Systematically extract from the 2021–2025 reports:
   - answer-format rules (single inequality, exact form, precision, radians);
   - method requirements ("hence", "showing all working");
   - follow-through behaviour;
   - accepted alternatives, and anomalies (keep the R13-06 anomaly).

   The marking and feedback parts of the recipe contract depend on this register.
4. **R13-23: complete the textbook inventory** using `textbook-completion-method.md`. It must cover:
   - exercise items by demand;
   - diagram and visual items;
   - answer-key availability;
   - exam-style items.

   This is the breadth evidence needed before deciding how many branches and variations each group warrants.
5. **R2-08: NSSCAS→Cambridge provenance pass (recommended).** Find which NSSCAS questions are adapted from specific 9709 questions. Record them as `derived-from` references, and use the Cambridge originals when diagnosing source defects.

### Step 3: recipe contract and pilot PLAN

The PLAN must decide the following.

- **References (R2-02):** compute same-type references per branch, apply the display rules for held parts, and use the `derived-from` relation.
- **Diagram spec:** fixed, variable and relations; must-read givens; label set; and an acceptance check that the generated image agrees with the instance values. This is what the owner's image-generation loop needs.
- **Sketch marking:** credited features per sketch branch, taken from the award tables where they exist.
- **Bloom:** per branch, under BLOOM-CLASSIFICATION's highest-genuinely-assessed rule.
- **Grade bounds:** how the descriptor bounds become parameter domains.
- **Shared modules:** whether shared modules (`bounded-trig`, `elementary-differentiation`, the function and numerical chains) are standalone recipes or embedded modules.
- **Thin demands:** 44 demands with two or fewer NSSCAS parts, of which 13 gained Cambridge items. Set the target for further Cambridge variety, especially diagram items, and set the three-item target for sparse demands.

### Steps 4–5: unchanged from the agreed sequence

Author a first batch that exercises symbolic work, connected parts, proof, diagram input and sketch response. Then validate generation, marking, feedback, solution reveal and fresh instances, including visual responses, in YYeni locally.

## 4. Limits

- I did not solve every part or every Cambridge item, and I did not re-read every mark-scheme page.
- The qualifiers, normalised objectives and assessment-condition years were spot-checked, not read in full.
- The textbook and OCR were not re-examined beyond the author's derivative verification.
- No app code was run.
- The repair is uncommitted, and this verdict applies to the hashed state in `inputs.json`. Later edits need their own check.
