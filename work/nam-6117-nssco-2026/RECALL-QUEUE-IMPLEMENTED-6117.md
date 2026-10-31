> **Latest revision:** [Topic 8, source scope and balance](TOPIC8-SCOPE-REVIEW-6117.md). Recall **390/1,637 (23.82%)** after restoring explicit test knowledge. Full copied-wording scan: 28 paths / 24 distinct contents. All 12 topic checks pass; publication remains **hold**. Older totals below are historical.

# Binary-choice and recall-contingency repairs — 29 October 2026

**The four cited prompts and the burette duplicate are repaired, and the still-factual replacement queue has now been implemented.** All 12 topic QA runs and the accounting/regression checks pass. Publication remains on hold for independent semantic review; this is an author estimate, not certification.

## Changed cards

- 9-007 now asks for an example of a metal that displaces copper, with multiple scientifically valid answers accepted.
- 6-002 asks learners to support a classification using the unchanged molecular identity; naming a classification alone earns no mark.
- 10-032 asks for the reactive structural feature in a single displayed formula. This is now explicitly factual recall, not application.
- 10-076 asks for cotton's fibre class without giving either class name in the prompt. Nylon classification remains elsewhere in the bank.
- 1-051 retains apparatus selection. 12-014 now asks about equal initial/final burette offsets cancelling in the delivered-volume difference, with a specific reason required. It no longer answers “a burette”.

These changes address the four named binary prompts. They are not a claim that every remaining choice in every activity has been eliminated: legitimate MC sets and evidence-based selection remain.

## Queue implemented

The earlier first-batch candidates 7-007, 10-059, 10-078 and 11-001 already contained applied stimuli in the live bank. Their existing zero-recall allocation was not counted again as a saving.

Eleven still-factual two-mark cards were rewritten with fresh observations, references/controls, accepted conclusions and specific credit:

| Cards | New demand |
|---|---|
| 8-015 | Resolve an ambiguous red/brick-red flame record using reference comparisons. |
| 8-017 | Reject a sodium attribution when the wire blank is also yellow; design a usable repeat. |
| 8-019 | Interpret cleaned-wire evidence without treating a masking yellow flame as proof of absence. |
| 8-021 | Correct flame-versus-solution reporting and qualify identification without a blank. |
| 8-023 | Distinguish a supported barium result from a contaminated blank. |
| 8-037 | Separate alkaline splash effects from gas-only ammonia evidence. |
| 8-039 | Distinguish mere bubbling from a positive limewater result relative to a control. |
| 8-041 | Interpret a timed litmus sequence, separating acidity from bleaching. |
| 8-043 | Diagnose an invalid negative hydrogen test and specify a valid supervised repeat. |
| 8-045 | Reject continued burning as equivalent to relighting a glowing splint. |
| 11-020 | Select fertiliser using deficiency and excess-nutrient data. |

The exact prompts, answers, credit and current IDs are in [planning/round7-replacement-checks.json](planning/round7-replacement-checks.json). Factual teaching remains in the notes; objective coverage, item counts and tariffs are preserved. No labels were changed to claim savings without rewriting the tasks.

## Recomputed totals

808 cards + 36 activities = 844 items; 236 activity parts; 1,637 marks.

Recall: **395 − 22 rewritten queue marks − 1 burette-offset mark + 1 factual alkene mark = 373/1,637 (22.79%)**. This is below both the 24% trigger and the contingency's 23% target. The largest whole-number total below the ceiling is 409: 36 further recalled marks fit, while 37 would breach 25%. AO marks: A 765 (46.73%), B 557 (34.03%), C 315 (19.24%).

The rewritten queue's application classifications still require independent acceptance. If the reviewer rejects any classifications or changes the single-step calculation rule, recompute the affected credit before release. Do not use the new percentage as proof that cognitive demand has been independently certified.

## Verification and release

All twelve topic QA runs pass with release **hold**. Production totals, fingerprints, subtype/ID consistency, MC keys/learner assets and round-five, round-six and round-seven regressions pass. The burette offset cancellation was numerically checked across three pairs of readings. The new regression checks that the exact authored replacements exist and reconcile the recall delta.

The copied-wording check was rerun against the 24 unique assessment PDFs cited by the evidence records (18 question papers and six annual reports): zero 12-word defects; nine eight-word matches, all read as standard terminology/definitions. This source set is explicit and is not presented as the older 28-file run.

Run authoring/apply_round5_repairs.py, which imports round6_polish.py and then round7_replacements.py, as the final content repair stage. Render notes, run all topic QA and accounting checks, and run check_round7_replacements.py. Do not run an earlier repair stage afterwards.

No commit, push or publication was performed. Independent review of the revised cards, notes and visuals, and acceptance of the recall rule, remain open. Carry-forward constraints remain: reword/recompute reused internal report answers, no invented official allocations for the five commentary-only parts, Paper 1 at 45 minutes, and proof labels for 2022/2023 sources.
