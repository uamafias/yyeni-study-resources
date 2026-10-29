> **Latest targeted repair:** [Prompt, activity and open-item report](TARGETED-LEAK-REPAIRS-6117.md). Named leaks and 8-P03 repaired; all 12 QA runs pass. **236 answer-only note blocks, missing worked methods, MC length bias and broader semantic/visual review remain open.** Recall 390/1,637 (23.82%); publication stays on hold.

> **Latest revision:** [Topic 8, source scope and balance](TOPIC8-SCOPE-REVIEW-6117.md). Recall **390/1,637 (23.82%)** after restoring explicit test knowledge. Full copied-wording scan: 28 paths / 24 distinct contents. All 12 topic checks pass; publication remains **hold**. Older totals below are historical.

> **Current version:** [Recall queue implemented](RECALL-QUEUE-IMPLEMENTED-6117.md). Recall **373/1,637 (22.79%)** after 11 actual queue replacements and the cited card repairs; all 12 topic QA runs pass. Publication remains **hold** for independent review. Earlier totals below are historical.

> **Latest follow-up:** [Wording and visual fixes](WORDING-VISUAL-FOLLOWUP-6117.md). Current recall is **395/1,637 (24.13%)**, above the internal 24% review trigger; publication remains **hold**. All 12 topic QA runs pass. Earlier percentages below are superseded.

> **Current learner-review repair version (29 October 2026):** see [LEARNER-REVIEW-REPAIRS-6117.md](LEARNER-REVIEW-REPAIRS-6117.md). 808 cards + 36 activities; recall 391/1,637 (23.89%). All 12 QA runs have zero failures and remain **hold**. Older counts and rebuild instructions below are historical. Author checks are not independent certification; revised content awaits independent review.

# Chemistry 6117 — October 29 review repairs

## Final rubric repair and independent-review handover

**Author corrections and checks below are not independent approval. Publication remains on hold.**

- Replaced 55 vague rubric entries with specific accepted answers and separate credited elements; repaired 9-038 using comparative wear measurements and a 0.50 mm replacement limit. One mark requires the choice plus the numerical justification.
- Recall remains the author estimate **366/1,557 = 23.51%**. The rule is documented in RECALL-RULE-2026-10-29.md; user/independent acceptance must not be inferred from passing QA. See [the 24-card contingency](RECALL-CONTINGENCY.md) for explicit rewrite priorities, triggers and stop conditions. It is not counted as work already authored.
- planning/round3-numerical-check.json now verifies **26 revised calculation answers plus four additional Ar-only edits** (4-025–028), confirming their unchanged molecular formulae. These four are additional to the 26, not included in that count.
- All twelve topic checks rerun with no blocking failures; all release decisions remain hold. Full-bank accounting, demand freshness, numerical and copied-wording checks are author/tool checks.
- Independent reviewer reports completed: integrity, 55+ calculations, cited repairs, earlier QA freshness and copied-wording review; approximately 45 cards in Topics 5, 7, 8, 9 and 10 scientifically sampled. This is the reviewer's reported scope, not a claim that Codex repeated it independently.
- Still open: twelve topic notes, 67 visuals, at least 20 cards per topic, all 19 misconception cards, and acceptance of the recall interpretation. The reviewer can now continue notes and visuals while checking the explicitly recorded demand rule. Do not mark these gates complete from the author QA results.

Rebuild applies authoring/round4_rubrics.py through apply_round3_repairs.py, so earlier templates do not silently return. Nothing committed, pushed or published.


Ready for independent re-verification, **not publication**. No commit or push was made. This note supersedes the 23.31% recall headline.

| Measure | Current author estimate |
|---|---:|
| Cards / activities | 772 / 36 |
| Activity parts | 236 |
| Total marks | 1,557 |
| Recall | 366 marks, **23.51%** |
| AO A | 754 marks, 48.43% |
| AO B | 489 marks, 31.41% |
| AO C | 314 marks, 20.17% |

## Decision and changes

See [the recall rule](RECALL-RULE-2026-10-29.md). Formula recitation counts as recall; executing numerical operations on supplied data is application. This is grounded in the syllabus's AO B numerical-manipulation description, but remains an author interpretation requiring independent agreement. Familiarity or a command word alone does not settle cognitive demand.

- Rewrote 26 calculation stimuli, including all 19 Topic 1 cards, to add corrections, differences, conversions or successive operations. Topic 1 remains foundation practice, not an examination difficulty model.
- Added recall allocations for 21 thin explanation cards and 20 procedural cards. Rebalanced twenty factual two-mark cards into explicit causal or evidence-based tasks. All 1,008 card/part decisions remain fingerprint-bound and independent of Bloom labels.
- Repaired the cited weak explanations, distinguished 7-003 from 7-004, removed the hydrogen-test giveaway in 7-014, and required evidence for the alloy choice in 9-004. The subtype field is authoritative; stable IDs are retained.
- Replaced generic one-mark card rubrics across the bank with the accepted answer. Tightened the fertiliser rubric and reviewed procedural rubrics. This does not replace independent semantic review of every rubric.
- Retained 273.15 because the syllabus explicitly uses it on PDF page 10. Removed irrelevant atomic-mass values from 4-025–028.
- Updated linked worked examples, claim revisions, rendered notes and content hashes. Earlier MC-key and learner/answer-visual separation fixes remain in place.

The current full-bank decision file builds on the previous author audit plus these corrections. It is **not a fresh independent reading of all 1,008 responses**. Earlier before/after reports describe earlier repair rounds and are historical, not the current totals.

## Verification and remaining gates

All twelve topic checks have been run; zero blocking failures and release **hold**. Whole-bank accounting and demand freshness checks pass. All 26 revised numerical answers were independently recomputed from their supplied values; the calculation check is in planning/round3-numerical-check.json. MC-key and learner-asset regression checks pass. Copied-wording check: 28 source files, zero runs of 12 or more words; the 13 eight-word matches were reviewed as standard definitions/terminology. See review/copied-wording.md, including its final-change note.

C-16 remains honestly not_run where keyword matching cannot assess rubric meaning. No standard/ files were changed. The missing item-budget input has been supplied and no QA report claims publication approval.

Independent review still needs the notes, 67 visuals, at least 20 cards per topic, all 19 misconception cards, and the contested recall/causal-credit allocations. These repairs do not certify those gates. The reviewer may run the QA checks; they regenerate QA files.

Rebuild: original builders/renderers → existing finaliser/full-demand repair stages → **authoring/apply_round3_repairs.py last** → render notes → all twelve topic checks → progress, production, demand, numerical and copied-wording checks. Running an earlier repair stage alone restores superseded text. Preserve planning/demand-audit-before-2026-10-29.json as the baseline.

Carry forward: reword and recompute reused internal examiner-report answers; invent no official allocations for the five commentary-only parts; Paper 1 remains 45 minutes; 2022 and 2023 papers remain proof versions. Nothing is committed or published.
