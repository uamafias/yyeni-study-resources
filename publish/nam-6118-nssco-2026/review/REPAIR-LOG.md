# Physics repair build for Lotto/Claude’s verdict — 31 October 2026

Current build: **693 items — 616 flashcards, 26 MC sets (312 questions), 26 structured tasks and 25 practical tasks**. All 666 original IDs remain; the 27 repair supplements comprise the earlier 20 plus seven new coverage cards. All 28 topics have zero failed mechanical checks. Lotto accepted proceeding to Step 7 on 1 November 2026; the approval is recorded in ../step7-approval.json. Claude’s partial-verification limits remain explicit.

## Corrections to the previous log

- The first repair removed the ECB assertion but retained Ruacana as a syllabus-era example. **Ruacana is now removed from the authored topic, generated notes, prompts, answers and rubrics.** No outside-source verification is claimed.
- The first repair missed the I²R wording in the 26-014 rubric. **That rubric now states higher voltage → lower current → less wire heating**, matching the card.
- **203 was the earlier count of changed flashcard answers. The correct earlier total across item types was 255:** 203 flashcards, 26 MC sets, 24 practical tasks and two structured tasks. Against the original baseline, the latest build changes 256 original canonical answers. New supplements are counted separately. These are string-level answer differences, not counts of corrected physics errors.

## Follow-up feedback repaired

| Item | Change and where to inspect |
|---|---|
| 1–2 | Removed the named plant and matched 26-014/26-017 rubrics to the generic transformer pathway. No I²R formula remains in that rubric. |
| 3 | Figure 23-11 now has a small rectangular relay coil with vertical top/bottom leads, a separate movable open-switch arm and dashed mechanical linkage. |
| 4 | Practical 15 now supplies both **black-can and shiny-can** temperature columns. Slopes are −0.08 and −0.05 °C/s. The graph labels both series, places Δx below the construction line, and the conclusion mark explicitly credits the black can’s steeper negative gradient. The five/three/eight total stays 16; graph plotting credit covers all twelve points. |
| 5 | Practical 4 measurement credit explicitly includes repeating each timing at least three times and taking a mean. |
| 6 | Practical 5 analysis credit explicitly links a straight speed-time line of constant gradient to constant acceleration. |
| 7 | Rewrote the two flagged wrong-option explanations to explain their own alternatives. All 312 option-text/reason pairs are checked after shuffling. Exact lettered extracts for 28 Q10 and 19 Q3 are in followup-validation.json. |
| 8 | 21 Q8 now says initially neutral and excludes other charge transfer; 21 Q11 asks for a sequence with sequence alternatives; 24 Q12 states the smallest-listed-rating-above-normal-current criterion; 15 Q2 no longer uses phonons. |
| 9 | Added Newton’s-first-law and friction cards/notes (6-R02/R03); energy forms/examples and named crowbar, bicycle gearing and crane/flagpole pulley practice (10-R01–R04); iris/aperture and retina/film/sensor comparison (18-R01). Card 21-008 now assesses light discharging the drum explicitly. Topic 20 notes now explicitly teach sound transmission through solids, liquids and gases and its absence in a vacuum. |
| 10 | All **87 calculation rubrics are separately written** in calculation-points.txt; the answer-sentence M1/A1 generator was removed. Guidance separates the actual method/result or independent nuclear-number points, specifies units/alternatives, and applies follow-through only where a dependent stage exists. The four named cards have explicit ECF treatment; 23-022 correctly says it has no preceding calculated value to carry forward. Added specific accepted terminology/paraphrases and choices where valid. The irrelevant heading-only PROC closer is removed. Fixed-condition questions still require their stated conditions; “any n” is used only for actual choices. |
| 11 | Rest line moved clear of the axis; duplicated readings legend text removed; ray/diode labels made readable against linework; vector labels offset from arrows; ice and liquid warming sections labelled. Author opened the nine changed figures in followup-figures.jpg. |
| 12 | Topic 12 alternatives balanced in length: the key is uniquely shortest in one of twelve questions. Topic 15 Q3 now has distinct liquid/solid/vacuum alternatives. Topic 8 Q7 now distinguishes brake-pad friction, drag, road support and chain drive, rather than three near-identical low-friction choices. “Couple” removed from its Q4 feedback. |
| 13 | Practical 2 specifies approximately 35 W at 6 V, rather than voltage alone; 0.100 kg water warming at 0.08 °C/s needs 33.6 W before losses/container heating. Practical 15 specifies 0.025 kg water in each light can, giving about 8.4 W water-energy loss for the black-can slope, rather than implying 67 W from 0.20 kg. Topic 13 no longer teaches resolution. 6-018 uses zero net external force. Practical 25 explicitly labels the supplied values uncorrected readings. |
| 14 | The accepted syllabus-derived headings were retained. |

## Validation and evidence

- `repair-validation.json`: all 24 primary practical slopes/units, declared figure data, diode knee, generator periods/amplitudes, distinct affected-topic images, baseline identities and the bounded 12-word canonical-answer comparison with transcribed syllabus quotations.
- `followup-validation.json`: 15 targeted checks for this feedback, exact MC options/feedback, coverage items, data assumptions and scoped answer-change counts.
- `what-to-fix-results.json`: all 28 topics return zero. Existing warnings and not_run checks remain visible.
- `followup-figures.jpg`: nine changed figures inspected by the author. C-35/C-41 still report not_run; the author’s separate checks and visual inspection are not independent review.
- Claims remain unverified/non-publishable; items remain review_required. The approved curriculum/work-order records were retained; only generated contract item counts changed for the seven additional cards.
- No commit, push or platform import was performed. Unrelated working files were preserved.

## Still open

- Operator acceptance for Step 7 was given on 1 November 2026; a teacher’s subject reading remains recommended.
- The 267 marking-evidence gaps, partial 355/622 demand evidence, independent demand-to-syllabus mapping review, and final-print equivalence for the 2022/2023 First Proof papers.
- Markdown image answers must be checked on the platform at import time. No platform rendering claim is made.
- The accepted working syllabus and waived non-major Paper 1 duration conflict remain settled.

Rebuild sequentially with the repository `.venv` Python: `topics/1/authored.py` through `topics/28/authored.py`, then `authoring/verify_repairs.py`, `authoring/verify_followup.py` and `authoring/export_resources.py`. The review repairs run from the authoring engine on every build.

## Final optional tidy-up — 1 November 2026

- 4-P03 now explicitly specifies a 0.49 m pivot-to-bob-centre length for its invented timing table, and the results-table rubric records length for each timing series. The graph uses hollow readings markers above the fitted line and a legend outside the plotting area; the rebuilt image was opened to check title, labels and legend placement.
- Topic 9 now explicitly separates uranium-235 reactor fuel from the controlled fission process supplying the described heat. This does not add nuclide formulas or confuse fission energy with natural radioactive decay.
- The topic 13 authoring input and generated notes contain the sensitivity/range account, with the superseded resolution comparison removed.
- Affected topics 4, 9 and 13 pass mechanical checks. The evidence, mapping, First Proof, C-35/C-41 and platform-rendering caveats are unchanged. Claude’s supplied final feedback confirms no must-fix findings remain; this tidy-up does not claim a new independent review.
