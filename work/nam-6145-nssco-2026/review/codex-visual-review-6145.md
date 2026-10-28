# Codex visual review — 6145 NSSCO Economics, revision 01

28 October 2026. **Verdict: publish the visual subset when the full subject is complete.** All 12 visual cards and their 24 images are accepted after the repairs below. This is not a declaration that the 625-item subject is complete or ready for classroom import.

## Scope read

Read Claude’s visual-authoring report; all 12 prompts, model answers and four-mark rubrics; all 16 new claims; all new/moved diagram teaching paragraphs and image references; the declarative models; and the rendering, SVG-verification, manifest and publication code. Inspected every question/answer PNG at full size and as its 390-pixel preview. Also inspected greyscale versions of the two elasticity comparisons, the demand shift and the wage floor. These visual checks are separate from Claude’s self-review.

Two learner-reconstruction checks were explicitly followed through: the PPC’s J/K classifications and C→D sacrifice, and the binding price ceiling’s original equilibrium, controlled quantities and shortage. Both can be answered fully from the reviewed notes, worked image and supplied task data. The other ten answers/rubrics were read for consistency and feasibility. This is a focused review of the visual changes, not another whole-bank review of unchanged cards.

## Findings and repairs

| ID | Severity | Finding | Resolution |
|---|---|---|---|
| V01 | high, planning | Eleven activated contracts had a correct item_budget but stale required_outputs.learning_items. Example: 3.2 was 34 rather than the approved 29. | Fixed in live and candidate contracts from work-order counts; scope/IDs/labels unchanged. Fixed the revision wrapper so both counts are always reconciled. The original activation hashes are preserved as historical evidence; contract-count-correction.json records the 22 before/after file hashes and unchanged work-order hashes. |
| V02 | medium, accuracy | PES case says a workshop at full capacity expands output by 20% without explaining a capacity change. | Changed to near capacity in the card, notes, source packet, figure spec and verifier text invariant; regenerated the affected images. All quantities and geometry unchanged. |
| V03 | medium, analysis | Demand/supply curves were interpolated from two points without an explicit straight-line assumption. The PED answer also asserted product-specific substitute facts absent from the prompt. | Both prompts now state straight-line and unchanged-other-conditions assumptions. PED classification rests on the provided numbers; the notes retain substitution as a general possible determinant. |
| V04 | low, clarity | PPC maximum-output assumptions were implicit in the task; wage-floor answer inferred particular people losing jobs from a net employment change and loosely extrapolated outside its model. | PPC prompt explicitly states full, efficient use of fixed resources. Wage answer says 100 fewer jobs and explains that the diagram alone does not establish the response outside the competitive model. |
| V05 | medium, publication | The helper checked for missing IDs but could still let the standard publisher silently skip a failing topic once all IDs existed. | Added a preflight requiring exact unique slot coverage, PUBLISH and matching QA counts for every topic, plus post-export exact coverage. Six focused guard scenarios pass; the real publication remains unchanged. |

No claim meaning was changed by these wording repairs, so no claim revision was raised. Changed canonical items/blocks were restamped and notes rendered. The authoring packets were kept aligned, without replaying their broad apply script. Do not replay apply_card_text.py after review: its fresh-authoring stamp behaviour can remove repair history.

## Calculations and pictures

| Card | Numerical/semantic result |
|---|---|
| 1.1-011 PPC | Opportunity costs 5, 15, 25, 35 cattle for successive 50-tonne increases; J inside and K outside; C→D costs 25 cattle. |
| 3.3-019 PED | Initial-value coefficients −0.5 and −1.5; common axes and starting point; movements along demand, not shifts. |
| 3.3-020 PES | Initial-value coefficients 1.6 and 0.4; common axes and starting point; near-capacity premise repaired. |
| 4.2-025 labour | Equilibrium changes from N$25 / 150 workers to N$30 / 200; demand shifts by 100; supply stays fixed. |
| 5.4-031 LRAC | Average costs 8.50, 6, 4.50, 4, 4.50, 6; optimum 40,000 litres; total cost and average cost kept distinct. |
| 6.3-017 ceiling | Equilibrium N$14 / 500; ceiling N$12; Qs 400, Qd 600, shortage 200. |
| 6.3-018 floor | Equilibrium N$200 / 300; floor N$250; Qd 200, Qs 400, surplus 200; offered output distinguished from sales. |
| 6.3-019 wage floor | Equilibrium N$25 / 400; floor N$30; demand 300, supply 500, excess supply 200, employment change −100 in competitive model. |
| 3.2-002 movements | At N$8→16, Qd 80→40 and Qs 40→80; arrow directions correct and neither curve shifts. |
| 3.2-006 equilibrium | Equilibrium N$20 / 60; at N$10 shortage 60 and adjustment moves towards equilibrium. |
| 3.2-010 demand shift | Original equilibrium (60,20); new (75,25); demand shifts right, supply fixed. |
| 3.2-017 supply shift | Original equilibrium (60,20); new (75,15); supply shifts right, demand fixed. |

The independent Codex numeric audit restates these calculations from the learner prompts using exact fractions rather than importing the author’s expected-value functions. Claude’s geometry verifier was separately rerun: **542 pass, zero failures**. It reads curve coordinates from SVG paths; it does not, by itself, establish PNG fidelity or economic truth.

All **48 source/rendered files (24 SVG + 24 PNG)** reproduced byte-for-byte in a complete rerender on this machine, following the capacity-label repair. This establishes that the inspected PNGs correspond to their current generated sources. It does not promise byte identity across different fonts or browser versions on another machine.

Question sides contain the required given data, starter axes or initial curves, rather than the requested labelled solution. Showing the initial curves for a reading/annotation task is appropriate. The four existing 3.2 question images remain table-only because their rubrics award labelled axes. Their question/answer/guidance text still matches the authored checkpoint byte-for-byte. Curves, axes, marked values, arrows and change directions are consistent. No independent numerical, geometry, rubric or legibility defect remains open in this visual subset.

## Asset and build reconciliation

- 12 visual IDs, 12 question PNGs and 12 answer PNGs, all paired with SVG masters and correct manifest hashes. Every worked answer image is referenced by the appropriate canonical notes. Managed YYeni asset IDs remain null.
- All 588 present items have unique approved IDs and the labels explicitly specified by their work orders. The only missing IDs are exactly the 37 assigned Codex nonvisual additions. All 625 planned contract counts now match the approved work orders.
- All 28 topic check suites rerun: **13 PUBLISH, 15 incomplete/reject**. PUBLISH topics: 1.1, 1.2, 1.3, 2.1, 3.1, 3.2, 3.4, 3.5, 4.3, 5.2, 6.3, 7.2 and 7.3. Remaining failures are C-42 actual-versus-planned item counts and C-05/C-06/C-15/C-27 coverage for unfilled nonvisual slots. They are not marked waived or passed.
- C-18 warns in all topics. C-26 warns in eight topics, affecting the earlier ten-unit budget work order. C-35/C-41/C-43 remain not_run; they do not certify these visuals. Current main-unit headroom: 3.3 = 1,132/1,135 words; 4.2 = 1,408/1,412; 6.3 = 2,009/2,010.
- Copied wording: 40 cached subject-only assessment extracts; zero runs of eight or more words. Syllabus excluded.
- Six publication-guard scenarios pass, covering duplicate IDs, failed QA with complete IDs, stale QA counts, a valid fixture and both current incomplete-publication refusals. No actual subject publication was written.

Acceptance is recorded in diagrams/CODEX-REVIEW-6145.json, bound to the reviewed image hashes and learner-text/label fingerprints. The manifest builder now reports independent review only when those still match; changed files/text revert to needing review. No cloud upload, classroom write, commit or push occurred. The existing 580-item published package remains unchanged.

## Next work

Proceed with the already-approved 37 nonvisual cards and ten focused budget repairs, preserving these diagrams and prior review fixes. Use existing teaching text for gross/net pay and time/piece rates; new objectives/claims/mappings do not require repeating that prose. Claude then cross-reviews Codex’s nonvisual changes. Once all 625 slots are complete and all required checks pass, use the guarded publication helper and reconcile the image sidecar. Live YYeni attachment/display and learner drawing/grading acceptance remain later import-stage checks.

No new scope decision is needed for the count correction: it makes derived fields agree with the existing approved slots.
