# D1 short check findings: 8227 Workbench pilot PLAN

**Reviewer:** Claude Opus 5.5, cross-vendor REVIEWER. **Date:** 2026-11-23. This is the OD-3 short check of Codex's D1 repair.

**Inputs.** The inputs are frozen in `inputs.json`:
- plan manifest `c8914cf9…` (content digest `538a3701…`);
- git HEAD `fa0a09d4`.

At the start of the check, all 273 design files, 436 sources and 49 review files matched the manifest. The D0 manifest `dd0e5cfe…` is preserved.

**Owner decisions.** OD-4 and OD-5 were taken during this check; see `owner-decisions-2026-11-23-d1.md`.

## Method

**Seven checking agents (Claude, same vendor as this reviewer).** Each one re-tested its scope using its own code and its own cases, rather than Codex's scripts or reports. Their evidence is in the `check-*.json` files in this folder:
- trig: principal inverse and R-form;
- calc1: implicit normal and stationary points;
- calc2: motion and log-linear;
- visual: modulus and trapezium;
- vector-contract: vector recipe, shared rules D1-MR01..09, and an OD-1 sweep across all 27 parts;
- coverage: counts, coverage and exam weights;
- closeout: S3-10 and S3-11.

**Each agent:**
1. checked every step-3 agent ID in its scope against the current bytes;
2. recomputed every exemplar it covered;
3. enumerated every revised domain;
4. read the cited native pages. Across the agents, 65 page views were recorded.

**What I verified myself:**
- the two points where this check overturns or upholds a step-3 call. I rendered 2022 report PDF 313 (the R-form award table) and 2023 report PDF 331 (the modulus Q2 row).
- the 19 restored-reason over-negations, against HEAD;
- the scope change in the freeze script;
- the two fresh-copy rebuilds, the negatives and the freeze check (§C).

## A. Step-3 dispositions

There are 97 agent IDs (94 from step 3, plus S3-08, S3-09 and S3-11 where agents treated them separately). The results:
- **82 repaired;**
- **8 partly repaired;**
- **7 accepted deferrals** (later-test or note items, deferred with a stated reason).

**All nine step-3 design-blocking items are repaired:**
- trig-01, trig-06;
- calc1-01, calc1-03;
- calc2-01, calc2-02;
- visual-04, which is resolved by OD-5;
- vector-contract-01;
- visual-01, for its www and parabola defect only. The repair introduced the new blocker D1-B01.

| Partly repaired | Remaining gap | Carried as |
|---|---|---|
| calc1-04 | Classification still claims Analyse | OD-4 |
| calc2-03 | Motion still serves the first parts of the exam originals | D1-S09 |
| visual-01 | New list/formula answer-only split | D1-B01 |
| visual-03 | Trapezium (2,8,4,k≠3) reproduces 2023 Q6 (a), (c) and (d) | D1-S16 |
| vector-contract-10 | Misread rule applied inconsistently | D1-S23 |
| vector-contract-13 | Two classification-version strings | D1-S25 |
| coverage-09 | Disposition text overstates the crosslinks | note |
| closeout-01 | 31 reasons still assert the opposite of their decision | D1-S28 |

## B. Corrections to our own step-3 review

| Step-3 item | Correction |
|---|---|
| **trig-06 and REPAIR-PROMPT §1 (R-form "hence" cap)** | I rendered the actual 2022 P2 Q6 award table, report PDF 313 (printed 311). It has B1, M1 A1 / M1 F.T., M1 dep, A1 A1 / B1 F.T. B1 F.T., and no SC row. The SC1 rows we cited are for other task types: PDF 301 is a P1 disguised quadratic, and PDF 337 is a trapezium/log item. The stem says plain "Hence". **Codex's zero for non-hence work is correct; our SC1 analogy was wrong.** |
| **S3-09 exam weight** | Our 720.1 summed 138 per-demand shares that had already been rounded to 1 d.p. The exact total is 2162/3 ≈ 720.67, which reconciles with 750 together with the supplementary 88/3. **Codex's figure is right.** |
| **REPAIR-PROMPT §9** | It cited `check-coverage-demand-frequency.json` in the step-3 folder, but we never placed that file there. The data is now here as `check-coverage-demand-frequency-step3.json`. |
| **REPAIR-PROMPT §4 (motion reversal)** | We prescribed "one interior simple root". That fixed the outcome of the decision for all 108 instances, which undermines the Analyse claim we wanted to keep. OD-4 corrects this. |

## C. What passed

**Counts.** Each count was recomputed from the part records, and they agree across the manifest, PLAN, OWNER-CHECKPOINT, the D1 report and the coverage plan:
- 9 recipes, 14 choices, 42 cases, 27 slots, 83 marks;
- 38 unconditional facets plus 1 conditional-only. The conditional one is M1:T6:O03:D01, for principal real-solution instances only; that status is honest.
- 99 demands outside the pilot;
- 138 demands, 67 groups and 8 supplementary entries, all accounted for;
- decks: 3+7+9 = 19, 3+7+10 = 20, 6+6+5 = 17;
- exam weights: all 146 coverage-plan cells match a direct-link scan, and all 15 reviewer rows agree. No coverage is derived from families.

**Exemplars and domains.**
- Every exemplar was recomputed independently. 118 of 125 recomputations agree. Every one of the 7 disagreements is a finding below (D1-S06, S10, S15, S17, S21, S22, S28); none is a wrong exemplar answer.
- Every claimed capacity reproduces:
  - modulus 108 → 44;
  - trapezium 35 / 12 / packing 3;
  - vector 54 → 30, with (a) 30 and (b) 17;
  - implicit 40 → 27 points on 23 curves, with 8 proofs;
  - stationary 540/30 and 256/16;
  - motion 143/36/31, 59/15/3 and 108/18;
  - R-form 112 → 58, with 6/42/10 classes;
  - principal 47/12;
  - log-linear 270/30 and 20/4/2.
- The 54 removed motion "triangle coincidences" are exactly the instances where r equals the tail. None remains.
- All six named NSSCAS original tuples and the Cambridge inverse equation are out of the fresh pools. D1-S09 and D1-S16 cover the part-level reuse that remains.

**Marking.**
- **OD-1 holds across 25 of the 27 parts.** Each of the 27 parts states its answer-only credit explicitly. The exceptions are the modulus, which is blocking (D1-B01), and the trapezium (b), (c) and (d) rows, which correctly cite official awards on 2023 report PDF 337.
- **No leftover D0 "implied method" language.**
- **The convention locators match the native pages:** CONVENTION:076, :002, :003, :004, :005, :006, :096 and :108, checked on 2021 PDF 236 and 2025 PDFs 345 and 355.
- **No same-type reference is a held original.** All 31 same-type references are per part and per branch.

**The show-that part (OD-2)** is marked 4+2+3, and the 2023 P2 Q8 award table matches (report PDF 339). Response tests:
- a copied target earns 0/4;
- an invalid derivation that still reaches the target earns at most 2/4;
- a failed proof followed by correct use of the given derivative earns 5/5 on the later parts.

There is no follow-through into the target and no double credit.

**Rounding.** The R-form knife-edge tuples are gone. Every rounding path at or above the requested precision gives no change to a final root.

**R7 close-out residuals.**
- All 72 step-3 inversions are fixed. However, see D1-S28.
- 2021 P2 Q4(b): the row accepts 34 or 35 (report PDF 238), and the direction judgement is right.
- One integrand rule now covers BP-08, 09, 27, 24 and 31.
- BP-37 = 0.744207.
- The 2024 P1 Q4(b) wording is correct.
- The relation totals recount exactly: 2,898 rows, of which 209 same, 912 branch and 1,777 rejected; the main rows are 2,718.
- `analysis/history/analysis-snapshot-r7-closeout.json` is byte-identical to HEAD's snapshot (`5aaa3bf2…`).

**Rebuild.** I ran this myself in two fresh copies of the current tree, each with its 436 sources copied in.
- **Outputs.** Each copy ran 285 commands. The 275 projected outputs are identical across both copies and the author checkout.
- **Seeded-error checks.** `--negative-only` passes, and all 38 established subprocess negatives are rejected. Codex's total of 75 also counts in-checker fixtures, which I did not count separately. The closeout agent separately confirmed that the new lost-negation fixture fails as intended.
- **Freeze check.** `freeze_analysis_r7_closeout.py --check` is read-only. On the author checkout it passes on 2,503 files, which is the narrowed scope in D1-S30. In the copy it stopped only because the repository-root `AGENTS.md` is not copied.

## D. Findings

### Design-blocking

| ID | Locator | Defect | Repair |
|---|---|---|---|
| **D1-B01** | `work-orders/WB8227-modulus-graph-recovery.md:55,57,66-67`; `exemplars/WB8227-modulus-graph-recovery.md:23,66` | **The modulus answer-only split contradicts OD-1 and the official row.** A bare coefficient list scores 0/3, but a bare formula scores 3/3. The official 2023 P2 Q2 row (report PDF 331, printed 329; rendered) reads "a = −2 www B1, b = −3 www B1, c = 2 www B1" plus "Allow all the marks if values are seen in the correct place in the formula". The work order's own criterion table also has B1 www with no method mark. The response format is named numeric fields, so the default correct response scores 0. The split is labelled `D1-MOD-OD1-LIST`, an "owner-binding interpretation", but no owner decision made it. Found independently by two agents (visual-D1-01 and vector-contract-D1-01). | Under OD-1, correct a, b and c with no wrong working earn B1 www each, given either as named values or in the formula. Practice feedback still asks for the vertex or point reasoning. Remove the "owner-binding" label, update the exemplar sample rows, and add the missing `answer_only_*` fields to `visual-design.json` for the three visual recipes (vector-contract-D1-11). |

### Should-fix (correct in D2, before approval)

**Owner decision OD-4: Bloom**

| ID | Locator | Defect | Repair |
|---|---|---|---|
| D1-S01 | `work-orders/WB8227-stationary-inflexion.md:38,40`; `calculus-design.json:1481,1586`; `part-evidence-register.*`; `PLAN.md:28,54` | Classification Analyse 4 is not supported by its own criteria. A routine f′ sign test earns full I4–I6, which is the same evidence the two-extrema part labels Apply. Degree and leading sign predict the type in 256/256 cases (calc1-D1-01). | OD-4: relabel it Apply 3. Keep the uncued mixed outcomes. |
| D1-S02 | `calculus-design.json:4394`; `work-orders/WB8227-motion-integration.md:25-27,40-45` | Every one of the 108 reversal tuples needs a split at one positive root. The 54/54 "decision_outcome_classes" only vary the starting direction (calc2-D1-05). | OD-4: admit a bounded minority with no sign change on [0, T], for example the positive root beyond T, never at T. Add a criterion for the sign-change check. Re-run the named-error and coincidence sweeps on the new instances. Rename the outcome classes honestly. Recompute Bloom from the new criteria and update the PLAN count to 13 Apply / 1 Analyse. |

**Principal inverse and R-form**

| ID | Locator | Defect | Repair |
|---|---|---|---|
| D1-S03 | `work-orders/WB8227-principal-inverse.md:50,58`; `trig-model-design.json` P-B1/P-M1 | In the real-solution route, P-B1 is earned by stating the interval without applying it to θ, so "interval + forward + x" scores 3/3. The JSON P-M1 wording also contradicts work order line 58 (trig-D1-01). | P-B1 requires the actual target to be shown inside [−π/2, π/2], or x to be verified by a principal-inverse evaluation. Align the JSON. Keep the 2/3 forward-only outcome. |
| D1-S04 | `work-orders/WB8227-trig-rform-equation.md:46-54,67-68` | b-M2 does not say how follow-through works from a wrong α. After the common inverted-ratio error, the F.T. pair differs from the canonical class in 6 of 58 tuples. In 8 tuples with c = a, the learner's own equation puts a root at the endpoint θ = 0 (trig-D1-02). | Judge b-M2 on their transformed roots inside (their α, 360° + their α). State what happens at the c = a endpoint. Add both cases to the fixtures. |

**Implicit and stationary**

| ID | Locator | Defect | Repair |
|---|---|---|---|
| D1-S05 | `work-orders/WB8227-implicit-normal.md:63,89`; `planning/d1/calculus-design-check.py:26-36` | **The examiner-named e-index error is not caught.** The 2023 report (PDF 339) names "the index of an e does not change". Because P is at x = 0, that error gives the canonical gradient in 27/27 tuples. Codex's error list omits it, and G5 has no www, so this wrong working scores 4/5 (calc1-D1-03). | Add the error to the named list and disclose it. Make G5 "A1 www", meaning a correct derivative, or state a coherent slip rule. |
| D1-S06 | `work-orders/WB8227-implicit-normal.md:90-93,108`; `subject-rules.md` MR09 | A valid alternative proof, such as dividing by y or a log form, has no mapped criteria, so it would score 0/4 (calc1-D1-04). | Add a generic alternative mapping for S1–S4 with the same cap and dependencies. |
| D1-S07 | `work-orders/WB8227-implicit-normal.md:94-95`; `exemplars/WB8227-implicit-normal.md:71` | It is undecided whether H1 accepts substitution into the learner's own wrong derivative (calc1-D1-05). | State the rule, with a named deviation if it is stricter than the official M1. Also settle vector-contract-D1-09 (the N1 wording against sample line 114) and calc1-D1-06 (whether S4 accepts a simplified target). |
| D1-S08 | `work-orders/WB8227-stationary-inflexion.md:27,36,80`; `calculus-design.json:1498` | All 128 quartic instances need an expanded cubic solved for f′ = 0. That uses the factor theorem (M2:T1:O04) or a binomial cube (M1:T2:O01), but the prerequisite is recorded as "NSSCO algebra" (calc1-D1-02). | Record the correct AS prerequisite and the module dependency, or justify the scope. State the factor-theorem route for I2. |

**Motion and log-linear**

| ID | Locator | Defect | Repair |
|---|---|---|---|
| D1-S09 | `work-orders/WB8227-motion-integration.md:19,23` | Exam originals are still served part by part. Admitted (3,1,2,T≠3) has part (a) identical to 2021 P1 Q4(a), and (30,½,T≠2) has part (a) identical to 2023 P2 Q9(a). The log recipe removes the same kind of reuse, so the two recipes are inconsistent (calc2-D1-01). | Exclude (3,1,2,\*) and (30,½,\*), giving capacities 140/56 and contexts 35/14, or serve those parts only as attributed originals outside freshness. |
| D1-S10 | `work-orders/WB8227-motion-integration.md:50` | The endpoint triangles are stated to give 18. The actual value is 17, and Codex's own script also gives 17 (calc2-D1-02). | Correct it to 17. |
| D1-S11 | `work-orders/WB8227-motion-integration.md:43-44`; `calculus-design.json:441…` | R3's F.T. from a miscalculated root can never apply, because R1 requires the correct root. R3 and R4 also do not need an attempted primitive, so calculator legs earn 3/4 (calc2-D1-03, calc2-D1-04). | R1 becomes M1 for solving v = 0 (one slip allowed) plus a sign test about their root. R3 becomes the legs from an attempted primitive with both bounds. R4 depends on R2 and R3. Re-derive this together with D1-S02. |
| D1-S12 | `work-orders/WB8227-motion-integration.md:21,40` | Eleven polynomial tuples (all with A = 3) let a wrong method give the right distance. Three of them use differentiate-instead-with-both-bounds, the error behind the official "k ≠ −15" exclusion. S3 is also not stated to depend on S1 (calc2-D1-06). | Exclude at least the three differentiate-instead tuples and disclose the rest. State that S3 depends on S1 and S2. |
| D1-S13 | `work-orders/WB8227-log-linear-model.md:98` | A learner who dropped the prefactor in part (a) and substitutes consistently into that line gets no U-M1. That is stricter than the official "into their log-equation" F.T. on 2025 report PDF 359 (calc2-D1-08). | Distinguish two cases: the prefactor dropped only in (b), and consistent F.T. from their own (a) line. Otherwise record a named deviation. |

**Modulus and trapezium**

| ID | Locator | Defect | Repair |
|---|---|---|---|
| D1-S14 | `work-orders/WB8227-trapezium-sketch-estimate.md:76-79,97`; `exemplars/…` | D1-TRAP-FT-BRIDGE is mislabelled as a departure, and two cases are undefined (visual-D1-07). | OD-5: accept the bridge, reworded. The 2023 Q6(d) row is kept in full ("must be correct from their graph" is read as own-graph F.T. for B1). The only extension is DB1 judged on the learner's own curve, supported by 2025 Q4(b). Define a drawn chord with a brief statement, and more than one graph in (c). |
| D1-S15 | `work-orders/WB8227-trapezium-sketch-estimate.md:39`; `planning/d1/visual-domain-checks.py` | For (L,n,k) = (4,4,2), T² = 15.86 rounds to the canonical 15.9. Codex's check compares unrounded values, so it misses this. The packing witness (2,4,4,2) is one of these tuples (visual-D1-02). | Compare wrong methods at the marked precision. Then either exclude (4,4,2), giving 32/11 and packing 3, or disclose it, and correct the count. |
| D1-S16 | `work-orders/WB8227-trapezium-sketch-estimate.md:30`; `visual-design.json:263-329` | (2,8,4,1) and (2,8,4,2) remain admitted and reproduce 2023 P2 Q6 (a), (c) and (d) verbatim (visual-D1-05). | Exclude (h,L,n) = (2,8,4) for every k, giving 33 presentations, or serve those parts as attributed originals. Update the part keys. |
| D1-S17 | `work-orders/WB8227-trapezium-sketch-estimate.md:72,83-91` | The closed accepted list conflicts with F.T. It takes 15.24 but rejects 15.23. With ordinates given to 2 d.p., the values 43.4, 46.1 and 69.1 are rejected even though (a) stays correct (visual-D1-03). | State b:B2 as a rule judged against the learner's own (a) value. Keep the list only as canonical-path fixtures. |
| D1-S18 | `work-orders/WB8227-trapezium-sketch-estimate.md:73-75` | c:B1 ties the shape mark to x = h. A correct shape with the wrong shift scores 0/3, against the official 1/3 (visual-D1-04). | Judge c:B1 relative to the learner's own asymptote. Credit x = h only in c:B2 and (h+1, 0) only in c:B3. |
| D1-S19 | `visual-design.json:357-361` | The c → d dependency is recorded as "cue" only (visual-D1-06). | Add a follow-through edge to d:B1. Note that DB1 is judged on the same own curve. |
| D1-S20 | `work-orders/WB8227-trapezium-sketch-estimate.md:71` | It is ambiguous whether a direct 2k ln(x−h) earns b:B1 (visual-D1-09). | State that a correct 2k ln(x−h) implies the square and earns b:B1, and add a sample row. |
| D1-S21 | `work-orders/WB8227-modulus-graph-recovery.md:39`; D1 report; dispositions | The crowded-label fixtures are stated as 4, but the JSON and the enumeration give 8 (visual-D1-08). The varied-asset note also says the leader avoids the y-axis, which it does not (visual-D1-10). | Correct the count to 8 and fix the asset note. |

**Vector and shared rules**

| ID | Locator | Defect | Repair |
|---|---|---|---|
| D1-S22 | `work-orders/WB8227-vector-geometry.md:20,30,63,69,86` | Two answer forms are unstated. Three non-exact angles round to 80.0 or 63.0, and it is not said whether "80" or "63" earns b:A1. It is also not said whether the undistributed p(1,r,1) − (s,1,−1) earns a:B1 (vector-contract-D1-02, vector-contract-D1-03). | Non-exact angles need the 1 d.p. form, and those three tuples are frozen as fixtures. The undistributed form earns B0 unless the scaled components are shown, per the official wording. Correct line 20. |
| D1-S23 | `subject-rules.md:67`; `work-orders/WB8227-motion-integration.md:48`; `work-orders/WB8227-vector-geometry.md:90`; principal, modulus and trapezium work orders | The misread rule is applied inconsistently. Motion keeps value-bearing E3 but drops E1, vector drops its value-bearing B marks, and three work orders are silent (vector-contract-D1-04). | Decide once whether value-bearing B marks follow coherently misread data. Apply that to motion and vector, and add a misread line to the three silent work orders. |
| D1-S24 | `planning/OWNER-CHECKPOINT.md:14` | The work orders contain 16 named deviations, but the checkpoint lists 2 (vector-contract-D1-05). | Add a consolidated deviation register (ID, recipe/part, official row, departure, rationale), so that Vitalis's approval records exactly what he accepts. |
| D1-S25 | Lines 3 of the principal, R-form and log work orders; `trig-model-design.json`; `pilot-design.json` | Two classification-version strings coexist: `8227-stage-d-d1-0.1.1` and `8227-pilot-design-0.1.1` (vector-contract-D1-06, calc2-D1-12). | Normalise to `8227-pilot-design-0.1.1`. |

**Coverage records**

| ID | Locator | Defect | Repair |
|---|---|---|---|
| D1-S26 | `PLAN.md:24`; `OWNER-CHECKPOINT.md:13`; `coverage-plan.md:7`; D1 report `:134` | "26 objectives" is not split into unconditional and conditional (coverage-D1-01). | Write "26 / 60: 25 unconditional, 1 conditional-only (M1:T6:O03)". Name the new M1:T8:O01:D01 facet (coverage-D1-08). Attribute the 14 → 19 deck change correctly (coverage-D1-07). |
| D1-S27 | D1 report `:109-117`; dispositions | The report cites a missing `planning/d1/visual-coverage-check.json`, and claims a given-diagram gap that no gap row records (coverage-D1-02, coverage-D1-03). | Cite the script, or persist and pin its output. Add a gap row for given geometric diagrams, or drop the claim. Update coverage-plan.md:17 now that the 0.6 difference is explained (coverage-D1-04). Fix the stale audit hash (coverage-D1-09). |

**R7 close-out (analysis layer)**

| ID | Locator | Defect | Repair |
|---|---|---|---|
| D1-S28 | `tools/textbook-relation-decisions-r7.json:5556` (records 157–163), `:9239` (331–335), `:10488` (390–396), `:5136` (137–148); outputs | **31 rejection reasons now assert the opposite of their decision.** The D1 rewrite negated 19 positive "The target instead asks …" sentences that were correct at HEAD. For example, 2021 P2 Q10(b) "Find the equation of the normal" now reads "does not ask the learner to … give the normal equation"; I verified this against HEAD. Separately, 12 "two-sided absolute-exponent preimage" reasons are still inverted and were only capitalised. These are non-evidence text, but they are wrong (closeout-D1-01, closeout-D1-02). | Revert the 19 sentences and negate the 12. Regenerate the ledger, families, map and insights. Re-run the rebuild and negatives. |
| D1-S29 | `tools/check_repair_r7_closeout.py:14-19` | The negation validator only looks for "does not <verb>" in the 72-pattern records. It passes all 403 records, including the 31 above (closeout-D1-03). | Compare each sentence's polarity with R6, cover "None of these other targets" and "The target instead", and add an over-negation fixture. |
| D1-S30 | `tools/freeze_analysis_r7_closeout.py:20-22` | The freeze scope changed from the whole workspace except reviews to an allow-list. That unpins 5,266 historical checks files (r3–r7, repair-r2..r7, fresh-copy r4–r6), not just the 4 stage-transition files (closeout-D1-04). Git still holds them, but the freeze no longer detects edits to them. | Pin the whole workspace except the review folders and the stage-D files the plan manifest pins (`checks/plan-*`, `planning/`, PLAN, status and handover). State the exclusions exactly. Update the stale `checks/r7-closeout/*-reading` manifests (closeout-D1-05). |

## E. Carried to stage E/F (later tests)

- **trig-D1-03:** R-form rounding flips on admitted tuples. With α or β at 1 d.p., 38 of 58 change; with R at 3 s.f., 15 change. These include the changed exemplar (4,3,−2), which goes to 299.5. Add 4 half-up ties, including 299.55, and R at 6 s.f. for (3,1) and (1,3) (trig-16). Accepted-answer generators must round half-up in decimal.
- **trig-D1-04:** hide the conditional exact-angle tags until after submission. Add marker fixtures for the decimal contradiction and for an implicit interval comparison.
- **calc2-D1-09:** exponential premature-rounding flips (14 of 59 at 3 s.f., including the boundary exemplar), and the 116.5 half-boundary.
- **calc2-D1-10:** tidy the stem polynomials. Current stems print forms such as "2t+0", "1t²" and "(0)t".
- **Carried from step 3:** diagram label placement (visual-11, calc1-11), vector notation input (vector-contract-14), and the 31 log zero-ordinate presentations (calc2-13).

## F. Notes (no action required before approval)

- **calc1-D1-07:** the stationary stem says "local evidence", which may exclude a valid global argument.
- **calc2-D1-07:** the log-linear answer a takes only the values 8 and 9, and half the pool shares the 2025 original's a = 9.
- **calc2-D1-11:** adding the signed legs from part (a) is a valid route for R5.
- **visual-D1-11:** a standard-form parabola fit gives the right b in 4 tuples. The www qualifier protects the marks.
- **vector-contract-D1-07:** the held 2023 P1 Q9 record is correctly `learner_display: false`, but its display reason was copied from the Cambridge reference.
- **vector-contract-D1-08:** MR02 describes the SC1 on 2022 PDF 301 loosely.
- **vector-contract-D1-10:** every admitted p terminates within 3 s.f. Dotting the resultant with OA gives the right p at (2,2,1) and (2,2,3).
- **coverage-D1-05:** the templated reasons for later groups undercount.
- **coverage-D1-06:** the trapezium (b) and (c) primaries depart from the 2023 Q6 analysis primaries without a stated reason.
- **closeout-D1-06:** ten records keep batch phrasing, with the negation intact.
- **trig-D1-05:** the trig-13 locator points to the wrong line.

## G. Not checked

- **No runtime work.** No app, generator, renderer, MCP or local-website operation exists or was run.
- **No pedagogical re-review.** Pedagogy was not re-reviewed beyond the repaired scope. Unchanged accepted material was not re-read in depth.
- **Same-vendor agents.** The agents are the same vendor as this reviewer. Each recipe was re-tested by one agent, except the modulus answer-only rule, which two agents found independently. Marking judgements at the margin carry that limit.
- **Frozen state.** This verdict applies only to the hashed state in `inputs.json`.
