# Handover — NSSCO Chemistry 6117

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
