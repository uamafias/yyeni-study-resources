# Handover — Namibia NSSCO Physics 6118

## Start here

This is a draft authoring handover, effective only after the operator approves the Step 4 plan. Read AGENTS.md, the active Author role, PLAN-6118-nssco-physics.md, the relevant generated work_order.json and the original structural exemplars. Work only in the assigned topic inside work/nam-6118-nssco-2026/. The plan follows the operator-approved 2018 working syllabus; do not reopen that decision or the waived non-major Paper 1 duration conflict.

## The job

Fill every generated slot, one topic after another in Codex. The complete subject has 28 topics and 666 planned learning items. Each topic needs a canonical claim ledger, the specified content units, one item per flashcard/performance slot and rendered offline notes. Treat topic-task-specifications.json as the concrete context/objective/data binding for performance tasks. Source containers need an overview and their members need targeted teaching; do not repeat a complete chapter for each member.

## Every item carries its labels

Carry item/slot IDs, objective IDs, claim IDs, subtype or performance item_type, A/B/C, Bloom level, primary command and tariff. Keep the axes distinct. Generated cards can be single-AO or A/B as the slot states; integrated practical tasks carry C. Performance tasks contain 12 MC questions, eight structured marks or 16 practical marks. The MC A/B 7.5/4.5 is an estimate across sets: alternate seven/eight A-focused questions rather than inventing a fractional-mark question. Give every question/part an explicit correct answer and complete marking guidance.

## Rules that come from the syllabus and the corpus

Use syllabus-facts.json, the registry and the explicit crosswalk. All 335 source bullets are represented; the larger registry counts include semantic decomposition and containers, not card quotas. Existing demand links were retained at a source container when a finer member link was not justified. Exam exposure does not remove coverage and must not be copied to every member automatically.

Use the 156 located answer-shape entries and the narrowly located supplementary task anchors. All calculate/define/explain primary demands have table checks. Other gaps remain: the 267 entries in assessment-evidence/GAPS.md are not reconstructed official rubrics. A proposed original teaching rubric is a judgement; never describe it as an official row. Source errors in inverse gradients, refraction arithmetic, wire diameter and tariff columns must not enter the authored material.

Use only the observed command/tariff pairs in the framework. A one-mark definition card asks a precise core meaning; teach longer conditions completely in notes and structured practice. A Describe-one-action card is not a complete method. Full planning is practised at eight marks. Distinguish graph construction from drawing a conclusion, and define each physical quantity before using it. All textbook exposition and examples are original. Do not reuse the exemplar scenarios or numerical values in the final bank.

Write each equation in plain text with clear symbols and units. Convert prefixes and squared/cubed units correctly. State assumptions such as fixed temperature, an ideal transformer or no external resultant force where the result needs them. A gradient’s unit and physical meaning come from the actual axes. Do not force a graph through the origin unless data support it. Preserve a negative slope. For an echo, one-way distance uses half the travel time.

Three explicit scope limits and 35 further depth/condition statements apply. Energy-source wording about no nuclide formulas does not remove nuclear decay equations. Diverging lenses are limited to eye correction. Illustrative examples in a source are not automatically mandatory independent card quotas.

## Voice

Plain British English for Namibian secondary learners. Explain with connected paragraphs and concrete examples; introduce terminology before using it. Use N$ only where money is relevant. Give units and working, not just formula lists. Invented data must say that they are practice data. No claims about what examiners always want, no copied official stems, no invented assurance that a source version is final.

## The work order is a baseline, not a cage

Do not silently alter a slot. If its objective, command or task is inappropriate, record the change and reason in authoring_notes.json and raise it with the operator. Do not add cards merely to chase an AO percentage. The planned whole-subject AO comparison uses the raw specification-grid target A47/B28/C25; final grade weighting implies a different 50/30/20. Keep both visible. Do not invent a denominator for the 24% recall statement.

## Finishing each topic

Run the standard render_notes.py, run_checks.py and what_to_fix.py for the topic. Fix real failed checks. The standard run_checks.py CLI currently returns 1 even for a publish decision because it checks for the literal string pass; inspect qa_report.json and failed checks rather than treating that existing wrapper mismatch as a content failure. Do not edit standard/ to hide it. The exemplar reports have zero failed checks; warnings and not-run checks remain explicit. Claims stay unverified and non-publishable until the appropriate operator/review decisions.

## Boundaries

Do not edit standard/, another workspace or the approved curriculum. Do not commit, push or publish during authoring without the required authorisation. The main topics presently contain plans only; the exemplars are thin drafts, not the completed topics. The 2022/2023 First Proof equivalence and the absence of 2020 MC difficulty/answer evidence remain caveats. Independent demand-to-syllabus and content review is scheduled for Step 6, with Lotto and Claude; no independent review is claimed by the current planner.

## Report back when the subject is finished

Report topics completed, counts of claims/units/items/notes words, the mechanical check result, deviations and unresolved limitations. Keep actual publication separate from a check suite’s publish verdict. Preserve operator decisions and unrelated files.
