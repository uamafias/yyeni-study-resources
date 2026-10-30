> **30 October 2026 review repair:** [Changed-item re-review packet](REVIEW-DELTA-2026-10-30.md). All latest named defects addressed, including optional items; counts clarified as 20 MISCON-subtype cards, 19 examiner mappings and eight image-bearing activities. Current author recall/AO figures remain unapproved; publication stays on hold. This working-tree repair follows the previously committed snapshot.

> **Current state — 29 October 2026:** [Final editorial repair handover](FINAL-EDITORIAL-HANDOVER-6117.md). Latest reviewer follow-up implemented and checked (132 MC explanations sets, note placement/labels, card commands and repeated fraction advice): 808 cards + 36 activities; recall 392/1,637 (23.95%); all 12 topic QA reports have zero failures and retain **hold**. Independent re-verification and release approval remain open. Older repair summaries below are historical.

# Handover — NSSCO Chemistry 6117

## Final rubric repair and independent-review handover

**Author corrections and checks below are not independent approval. Publication remains on hold.**

- Replaced 55 vague rubric entries with specific accepted answers and separate credited elements; repaired 9-038 using comparative wear measurements and a 0.50 mm replacement limit. One mark requires the choice plus the numerical justification.
- Recall remains the author estimate **366/1,557 = 23.51%**. The rule is documented in RECALL-RULE-2026-10-29.md; user/independent acceptance must not be inferred from passing QA. See [the 24-card contingency](RECALL-CONTINGENCY.md) for explicit rewrite priorities, triggers and stop conditions. It is not counted as work already authored.
- planning/round3-numerical-check.json now verifies **26 revised calculation answers plus four additional Ar-only edits** (4-025–028), confirming their unchanged molecular formulae. These four are additional to the 26, not included in that count.
- All twelve topic checks rerun with no blocking failures; all release decisions remain hold. Full-bank accounting, demand freshness, numerical and copied-wording checks are author/tool checks.
- Independent reviewer reports completed: integrity, 55+ calculations, cited repairs, earlier QA freshness and copied-wording review; approximately 45 cards in Topics 5, 7, 8, 9 and 10 scientifically sampled. This is the reviewer's reported scope, not a claim that Codex repeated it independently.
- Still open: twelve topic notes, 67 visuals, at least 20 cards per topic, all 19 misconception cards, and acceptance of the recall interpretation. The reviewer can now continue notes and visuals while checking the explicitly recorded demand rule. Do not mark these gates complete from the author QA results.

Rebuild applies authoring/round4_rubrics.py through apply_round3_repairs.py, so earlier templates do not silently return. Nothing committed, pushed or published.


Read AGENTS.md and the author role brief. Work only in `work/nam-6117-nssco-2026/` after the user approves Step 4.

## Entry gate

Before Step 5, the human reviewer must sign off all 56 calculation-card specifications, all 36 activities and the scientific/numerical VIS specifications in planning/semantic-review-gate.json, then approve the plan. The gate also covers nine fully authored sample cards (seven specified non-calculation slots and the two calculation exemplars). Write the prototypes before full production; templates alone cannot establish correctness. Structural check success does not close this gate. Final authored answers and rendered visuals require review again before publication.

## The job

Author 772 flashcards and 36 performance activities across 12 teaching topics. Teach all 418 assessable targets in 96,140–137,940 words of standalone notes. Topic 12 organises Annexe A practical skills; it is not extra syllabus content.

For every topic, read its generated contract and work_order.json. The work order fixes each slot and every activity subpart, target, tariff, answer requirement and visual. Create the claim ledger, content-unit JSON and learning-items JSON, then render notes with the repository renderer. The visual-manifest lists the required SVG assets. The practical-experiences map fixes all 55 original teaching boxes and their content/skill links.

## Every item carries its labels

Copy slot ID, subtype/type, objective IDs, assessment objectives, Bloom level, command and tariff. Use variant_spec and the answer-shape templates. Write the actual stimulus, answer and credit points; do not present the template as a finished rubric. Multiple-choice parts have command_word null; confirm their provisional Bloom labels against the authored stem and options. Performance parts must sum to the declared total and preserve their AO split. Record any deviation instead of silently redesigning a slot.

## Rules from the syllabus and corpus

- Use newly written prompts, answers and visuals. Reword and independently check all internal report-derived material.
- The 299 internal report rows need fresh wording and verified arithmetic. The five commentary-only parts have no invented official allocations.
- Use 45 minutes for Paper 1 and retain the first/revised-proof caveat for 2022/2023 sources.
- Wet ion tests belong only to Paper 3; gas/flame tests can occur on all papers. Teach their observations without relying on supplied Annexe B notes.
- Mark investigation plans by setup, controls, measurement and conclusion. Mark graph plotting, curve and read-off separately.
- Supply realistic original data; recompute values and state units. Use the fixed calculation variants rather than cloning cards.
- The recall ceiling concerns marks. Audit actual demand after each topic. There is no per-topic recall cap. Subject recall above 24% triggers review, and above 25% blocks publication. Include activity subparts in the subject denominator.
- Follow the contract scope guards and glossary. Do not introduce orbital chemistry, gas-law conversions or out-of-scope reaction mechanisms.

## Build and checks

Use `.venv/bin/python standard/v0.2.0-draft/build/render_notes.py work/nam-6117-nssco-2026 <topic>`, followed by `.venv/bin/python work/nam-6117-nssco-2026/planning/check_resource_topic.py <topic>`. Use `checks/what_to_fix.py` under the standard folder to inspect the resulting failures. Repair failures and rerun. When complete, obtain independent review, fix findings and rerun checks before publishing. Do not commit or push.

## Plan dependencies

The command framework comes from the corrected Step 3 audit. Leaf exposure is deliberately unmeasured; do not invent frequency counts. Generator settings are in planning/slot-plan.json and applied by planning/build_resource_plan.py without modifying the standard. The structural exemplar is a small internal guide, not published learner output. Its checked scope is one concentration objective, two cards and one calculation. It is not an exemplar for every activity or visual type.

Use `planning/check_resource_topic.py <topic>` for the unchanged standard suite with Chemistry runtime extensions loaded in memory. The canonical profile schema does not accept conditioned_mechanisms or depictions; this adapter supplies them without editing standard/. Chemistry graphs require separate numerical/visual checks because the standard chart checker only models business break-even. The standard CLI reports PUBLISH but returns exit code 1 (it tests for pass); inspect check statuses or use this adapter, which fails on failed checks.
