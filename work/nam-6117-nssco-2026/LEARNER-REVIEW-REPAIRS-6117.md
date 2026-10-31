> **Current version:** [Recall queue implemented](RECALL-QUEUE-IMPLEMENTED-6117.md). Recall **373/1,637 (22.79%)** after 11 actual queue replacements and the cited card repairs; all 12 topic QA runs pass. Publication remains **hold** for independent review. Earlier totals below are historical.

> **Latest follow-up:** [Wording and visual fixes](WORDING-VISUAL-FOLLOWUP-6117.md). Current recall is **395/1,637 (24.13%)**, above the internal 24% review trigger; publication remains **hold**. All 12 topic QA runs pass. Earlier percentages below are superseded.

# Learner-review repairs — current version, 29 October 2026

**Repaired review draft; publication remains on hold.** This report supersedes the counts and rebuild instructions in earlier repair briefs. Checks and visual inspections below are author checks, not independent certification. Nothing has been committed or published.

## Current accounting

808 cards + 36 activities = **844 items**, with 236 activity parts and 1,637 marks. The credit-level audit covers all 1,044 card/part responses. Recall is **391/1,637 = 23.89%** under the documented execution-versus-reproduction rule. AO marks are A 783 (47.83%), B 536 (32.74%), C 318 (19.43%). These are resource-bank proportions, not an exam blueprint or independent proof of cognitive demand.

The recall interpretation still needs independent agreement/user acceptance. The 24% review trigger occurs at 393 marks; 410 marks breaches 25%. Eighteen additional recall marks fit below the ceiling; nineteen do not. See [recall contingency](RECALL-CONTINGENCY.md).

## Repairs made

| Review concern | Changes and evidence |
|---|---|
| Activity leaks and mismatched stimuli | 12-P01 now uses the blank grid only, with neutral wording and no supplied planning controls; the cooling illustration no longer contains Topic 11 material. 7-P03(b) no longer supplies observations. 10-P03(c) uses the learner's preceding readings with follow-through. 11-P03 learner image contains scales only. 2-P03 uses the correct circuit context, consistently names the ammeter, and includes the relevant content objectives. 6-P02 legend says Chips/Powder without slow/fast. |
| Incoherent response and duplicated credit | 11-P02 is a coherent hard-water treatment response. 7-P02 uses distinct concentration/cooling and separation credit. 7-003 requires both links for its single mark. |
| Visual defects | Metal-lattice electrons are positioned independently of the ions and the column is no longer clipped. Cooling controls are confined to the answer illustration. Added separate Bohr and ionic model answers, plus an energy-profile stimulus. Rendered revised metal, soap-scale, cooling, ionic, Bohr and energy-profile images were inspected. This does not substitute for independent inspection of the complete visual collection. |
| Answer-bearing card prompts | Replaced the cited shape cues and error-correction stems; removed supplied ratios in 4-016/019/040. Reworked 3-013/016/033. Familiar closed-book recognition tasks are counted as recall rather than being described as demanding interpretation. |
| Coverage | Added 36 cards covering ionic/Bohr diagrams, electron properties, chlorine isotope arithmetic, sodium/water equation, mole/particle/concentration calculations, non-1:1 titration, electrolysis definitions and half-equations, extraction redox, energy profiles, solubility exceptions, hydrogen test, metal reactions/oxides, lubricating fraction, isomers/naming/unsaturation, water tests, industrial conditions, NPK, CO2, lime and air. Existing limiting-reactant work is retained. Added practical accuracy/precision, misconception and limitation tasks. The exact additions and objective IDs are in planning/round5-added-coverage.json. |
| Syllabus corrections | Fuel oil follows ships/home heating systems (PDF p.32); desalination follows the Namibia qualification on PDF p.38. Removed the unverified URL. Restored two omitted extracted outcomes: lubricating-fraction uses (p.32) and the chemical water test (p.37). The registry now has 420 assessable outcomes. |
| Card labels and tariffs | ID suffixes now match actual subtypes. Multi-credit examples 2-071/122/157 have explicit two-mark credit. Other one-mark prompts were narrowed. Causal “Describe why” prompts use Explain; the author command extensions are recorded separately without altering quoted syllabus wording. See round5-id-migration.json and round5-command-extensions.json. |
| MC options | Replaced implausible distractors in 78 questions. Keys remain balanced and non-cyclic. The correct option is uniquely longest in 12/132 questions; including ties, 56/132. Semantic quality of each distractor remains independently reviewable. |
| Notes copied from cards | Removed all 772 copied Worked practice blocks and repeated identical long paragraphs. No current card prompt appears verbatim in the structured notes. Twenty-two of 808 answers do, chiefly short factual statements that remain legitimate teaching content. |
| Thin notes | Expanded significant figures/precision, metal properties/reactivity, and a consolidated Annexe B table, plus targeted coverage explanations. Current structured notes total 81,950 words across 64 units. This is below the earlier 96,140-word planning floor after the requested removal of copied practice/padding; no filler was added to meet that obsolete quota. |

## Verification

- All 12 topic QA runs: zero failing checks; **release_decision remains hold**. Semantic/rubric checks that cannot be established automatically remain explicit gates.
- Production accounting, full-demand freshness, MC/learner-asset regressions and round-five regression checks pass. Fifteen new or changed numeric results were independently calculated in the regression script from their supplied quantities.
- Copied-wording check: 28 sources, zero 12-word defects; nine eight-word matches were read as standard definitions/terminology, not copied question scenarios.
- 55 suggested practicals and all 19 examiner-derived misconceptions remain represented; the two new anticipated misconception cards do not falsely claim examiner evidence.
- No standard/ files were changed. Unrelated Biology, harvest and 2025-paper work remains outside this repair scope.

## Review limits and next checkpoint

The broad claim that every near-duplicate, all card demands and every rubric are now semantically excellent is **not established by structural checks**. The named defects were repaired and the bank was searched for mechanical repetitions; a full independent semantic read and learner simulation remain necessary. Previous reviewer approvals do not automatically cover the new cards, revised options, notes or figures.

Independent review should prioritise the changed activities and learner assets, the 36 added cards, the recall classifications, the consolidated test table, metal notes and revised MC distractors. Complete the outstanding 20-cards-per-topic, misconception, notes and visual review before release. Any recalled credit reclassification must trigger a fresh calculation, not merely a Bloom-label change.

Carry-forward: reword and recompute any reused internal examiner-report answers; invent no official allocations for the five commentary-only parts; Paper 1 uses 45 minutes; retain the 2022/2023 proof-version labels. These constraints remain open review checks, not newly certified facts about every record.

## Reproduce

Run authoring/apply_round5_repairs.py as the final content repair stage; it rebuilds from planning/round5-baseline.json. Do not run an older repair stage afterwards. Regenerate relevant visual renderers, render all notes with standard/v0.2.0-draft/build/render_notes.py, then run all twelve planning/check_resource_topic.py checks. Run authoring/update_progress.py, audit_production.py, check_full_demand_repairs.py, check_review_repairs.py and check_round5_repairs.py, followed by the copied-wording check. The standard scripts are used unchanged.
