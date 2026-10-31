# Step 6 post-authoring review: Biology 6116

**Post-review update, 2026-10-19:** The findings and verdict below record the independent review at the time it was written. Subsequent author repairs to 3-P02, 4-152 and topic 2 P03, the label decisions, and the exact graph candidates are logged in `STATUS.md` and `review/POST-AUTHORING-LABEL-DECISIONS-2026-10-19.md`. Those repairs passed automated checks but have not had a second independent Step 6 read. The 35 figure items remain held and learner release remains open.

Date: 2026-10-19. Reviewer: Claude (cross-review of Codex's authored draft; Claude also performed the repair rounds, so this is not a clean two-vendor separation, and the report says so). Named-teacher verification was waived by the operator on 2026-10-19; that waiver does not make any claim verified. Nothing was committed, pushed, published to `publish/` or written to YYeni.

**Verdict: publish as a review copy; not releasable to learners.** No plan problem needs Step 4 to be re-opened. Learner release still needs the 35 held figures resolved, a demonstrated YYeni image route, and an operator decision on the label proposals. All 1,102 claims remain `unverified` and `publishable: false`.

## Playbook Step 6 items

1. **Checks.** `run_checks.py` on every topic, read through `what_to_fix.py`: PUBLISH for all five. Warnings: C-18 (AO mix by item count, every topic) and C-20 (topic 3, three cards). C-35, C-41 and C-43 report `not_run` where their inputs do not exist; that is not a substantive pass. Unit budgets: 0 of 50 units outside the operative minimum or maximum.
2. **Completeness.** `topics/audit_authoring.py`: every one of the 886 work-order slots has exactly one item with its subtype, AOs, Bloom level, command word and tariff; no item lacks a slot; every figure-dependent item is held and listed in `authoring_notes.json`. All 27 planned misconception slots have a MISCON item carrying the planned `misconception_entry`.
3. **Copied wording.** `operations/tools/check_copied_wording.py` against the 18 papers and the six examiner reports (the syllabus was not passed): 43 runs of 8 or more words, 7 of 12 or more, all in standard syllabus definitions (absorption, active transport, recessive allele, and the 8 to 11 word definition runs). Allowed under HANDOVER rule 5, which requires definitions in the syllabus's words. No stem, mark scheme or examiner phrasing was found. One non-definition prompt phrase was reworded earlier. Report: `review/copied-wording.md`.
4. **Level and scope.** Read by six reviewers against the registry and exclusions. Findings were small: terms or details above the objective (the triplet code, UV as a mutagen, hypotonic/isotonic wording, the cholera mechanism) were flagged in earlier rounds and mostly removed or simplified; this pass found only missing coverage, not extra scope. Open: "isotonic" remains in the exemplar-derived 3.3.2 notes and P02.
5. **Truth.** Every topic's notes were read in full by a reviewer (topic 3 in two halves) and 212 items were read in this pass (29, 24, 46, 47, 37 and 29 for topics 1, 2, 3 first half, 3 second half, 4 and 5): every performance task, every misconception item and random flashcards. 60 findings: **0 critical, 2 high, 23 medium, 35 low** (the two highs: ITEM-6116-3-258-APP, and the boiled-saliva control that said boiling "destroyed" the enzyme). No inverted mechanism was found.
6. **Numbers and pictures.** Every worked figure, cross and ratio was recomputed by the reviewers: all correct. One worked example failed its own condition (tourism cap, topic 5) and was fixed.
7. **Misconceptions.** 27 of 27 slots have a card. Discrimination: most discriminate; stems that gave the answer away were rewritten (1-106, 3-471, 3-473, 3-481, 3-467, 3-480, 3-472, 2-023, 4-153, 5-108). 4-152 (exemplar, protected) still gives its answer away and stays open.
8. **Learner test.** Top-tariff items written from the notes alone: full or near-full marks in every area (for example 1-041 and 1-P03; 2-005 and 2-022; 3-012 and 3-116; 4-P02, with 4-P03 about 9 of 10 until the untested-temperature point was added; 5-020, 5-105 at about 4 to 5 of 5).

## Findings and fixes

All 58 findings that concerned editable text were repaired in the author scripts and regenerated (the two exemplar-derived ones were not). A second, independent read of the final text then checked all 60 findings: **56 fixed, 1 partial, 2 left open on purpose, 1 repair introduced a new error**.
- Introduced error: the 5.2 forest sentence called the oxygen change "small compared with" the carbon dioxide change (the percentage change is small, not the amount). Fixed.
- Partial: 2-011, practical P03 is mapped to objective 2.2-16 although most marks test sampling and means from 1.2. A cross-reference was added; re-mapping is a work-order change (listed below).
- Open on purpose (protected exemplar items): 3AB-005 (P02 "neither gain nor lose" wording) and 4-015 (item 152 stem gives its answer away).
- A note on the 3.5 lipase method: it now leads in with "For lipase" and states that no buffer is added when pH change is measured.
- Ingested into each topic's QA report (`operations/review/nam-6116-nssco-*-review-r1*.yaml`): 58 resolved (the author's claim, not a verdict), 2 open, 0 blocking. Raw reviewer files and resolution notes: `review/step6-cross-review/raw/`.

## Plan problems (for the operator; none blocks)
- Practical P03 (topic 2) is mapped to the drawing objective 2.2-16 but tests sampling; re-mapping needs a work-order change.
- The 40 AO, Bloom and command-word proposals in `review/AO-BLOOM-LABEL-AUDIT-2026-10-19.md` remain proposals.
- Two protected exemplar items (3-P02, 4-152) carry small faults that can only be changed through the exemplar route.
- Teaching depth of material added to formerly short units, and Namibian examples written from memory, are for a Biology reader when one is available; the waiver does not verify them.

## Held figure items
All 35 stay held and are omitted from the review package. `review/HELD-FIGURE-ITEMS-RESOLUTION-PLAN.md` lists, per item, what figure it needs and the bank state: 5 have a candidate for every need, 15 need variants prepared, 15 have a gap (the model-drawing items and relay-neurone, human-population and organ-diagram needs have none). Resolving them is the next work: select an exact figure, check labels and scale, bind the key, re-check.

## Limits of this review
Samples, not every card (886 items; 212 read in this pass, a different sample from the earlier rounds); notes read in full. One model reviewer per area. No Biology teacher reviewed anything. YYeni display of images and multi-mark guidance is untested. The renderer's note header and the run_checks exit code are framework issues (`review/FRAMEWORK-REPORTS-FOR-VITALIS-2026-10-19.md`).
