# Handover prompt — Namibia NSSCAS Chemistry 8224

Paste everything below the line into the authoring tool with this repository open. It is self-contained.

## Live checkpoint — 2026-10-22

Jeremy explicitly approved the completed Step 4 plan on 22 October 2026. Scope: 21 topics, 253 assessable objectives, 565 flashcards, 66 tasks and 65,205–92,861 notes words. AO mix A 44%, B 39%, C 18%; largest rounded gap 4 points.

- Topic 1.1 is complete: 27 claims, five units and 30 items. Its report again reaches PUBLISH with zero failed checks.
- The thin `exemplar/5.1/` titration slice now passes all applicable checks against its five-objective reduced scratch contract: six claims, one 426-word unit, three supporting cards and one 20-mark task. Run `python3 work/nam-8224-nsscas-2026/planning/validate_practical_exemplar_8224.py` to reproduce. The full practical contract and 84-slot work order are unchanged. The scratch result does not certify the complete practical topic or independently verify claims.
- Fixed early rounding in the practical calculation, practical AO C permissions in the framework, and direct evidence metadata. Broad practical skill-category frequencies are explicitly labelled planning proxies; no individual practical criterion currently has a direct evidence mapping. Do not describe the proxy numbers as criterion-specific frequencies.

Do not rebuild Topic 1.1 or ask Jeremy to approve the scope again. Record/commit the approved plan, resolve the shared-schema compatibility decision, then proceed to whole-subject authoring.

The EQUATION/DIAGRAM mismatch remains a pre-build issue: those planned subtypes are absent from the shared schema. Topic 1.1’s single EQUATION-to-PROC exception is recorded in its authoring notes. Before whole-subject authoring, ask the standard owner to resolve the schema or approve regenerating the plan with supported subtypes and explicit semantic safeguards. Do not silently relabel slots or edit `standard/`.

Claude Code is reserved for the fresh-context review after the complete subject is authored. Do not invoke it for the exemplars. See `STATUS.md` for validation details and the shared CLI exit-code defect.

---

You are authoring the complete learner resource for **Namibia NSSCAS Chemistry, syllabus code 8224**, for the 2026 examination. The learners are Namibian secondary students, English medium. They may have nothing else to study from.

## Start here

Read these before writing anything:

1. `AGENTS.md` — you are the AUTHOR.
2. `work/nam-8224-nsscas-2026/PLAN-8224-nsscas-chemistry.md` — the plan approved by Jeremy on 22 October 2026; it wins over generic guidance.
3. `work/nam-8224-nsscas-2026/subject-profile.yaml` — answer structures, variants, conditioned mechanisms, prohibited patterns and slot plan.
4. `work/nam-8224-nsscas-2026/curriculum/answer-shapes.json` — observed command-word and tariff shapes.
5. `standard/v0.2.0-draft/roles/AUTHOR.md` — where it conflicts with this handover, this handover wins.

The syllabus facts, objective registry and assessment evidence have already been verified. Do not re-derive them, search the web card by card, or open another subject workspace. Work from the local corpus and approved local authorities. Under RS-12, every factual claim must be source-backed, externally verified against an approved authority, or transparently derived from verified premises.

## The job

Author **21 topics, 565 flashcards, 66 performance tasks and 65,205–92,861 words of notes**. Work in numerical topic order. Topics 1.1–4.7 serve Papers 1 and 2; 5.1 is the integrated Paper 3 practical-skills resource.

For each topic `<T>`, read `topics/<T>/contract.json` and `topics/<T>/work_order.json`, then produce:

1. `claims/canonical_claim_ledger.json` — 2–4 canonical claims per objective, each with provenance and verification status.
2. Every `content-units/*.json` file named in the work order — full teaching notes, worked examples and cross-links.
3. `learning-items/topic_<T>_items.json` — exactly one item per flashcard slot and performance-task slot.
4. Render the notes, run the checks, and fix every failure.

Every item carries its planned `item_id`, `subtype` or `item_type`, `objective_id` or `objective_ids`, `assessment_objectives`, `blooms_level`, `command_word` and `mark_tariff`. Do not redesign the plan silently. Record a necessary deviation in `authoring_notes.json` as `{from, to, why}`.

## Chemistry rules

- Use British English and the exact syllabus terminology.
- Give formulae, charges, structures, balanced equations and state symbols unambiguously.
- A calculation shows the relationship, conversion, substitution, working, answer, unit and justified significant figures. Distinguish s.t.p. (22.4 dm³ mol⁻¹) from r.t.p. (24.0 dm³ mol⁻¹).
- A definition retains every chemically meaningful condition. Do not turn non-definition objectives into definition cards.
- An EQUATION item requires correct reactants and products, balance, and state symbols where the objective requires them.
- A MISCON item names its `misconception_entry` and discriminates the wrong idea from the correct one using the entry’s test. Keep the one-report provenance; never call it a recurring or board-wide error.
- Paper 3 material teaches performance: measurements, observations, precision, repeats, tables, graphs, gradients, uncertainty, conclusions, specific errors and realistic improvements. Do not turn the supplied qualitative-analysis notes into recall trivia.
- Every generated visual must be viewed by a person before publication.
- Never reproduce wording from a question paper, examiner report or other published source. Mine the demand and write an original prompt, scenario and answer.
- Do not make frequency, examiner-behaviour or mark-scheme claims in learner-facing material.
- Respect every `excluded_constructs` entry. `adjacent_topics` names where related content is taught; a passing cross-link is allowed, teaching the neighbour here is not.

## Performance tasks

The work order preassigns each task’s objectives, AOs, Bloom level, command word and tariff. Multiple-choice sets contain original four-option questions with a key and an explanation of every distractor. Structured responses use linked 1–3 mark parts. Calculation tasks require complete working. Topic 5.1 has six distinct practical families: volumetric/acid-base titration, redox titration, thermometric/enthalpy, rates/gravimetric, qualitative analysis, and planning/evaluation.

## Finishing each topic

```bash
python3 standard/v0.2.0-draft/build/render_notes.py work/nam-8224-nsscas-2026 <T>
python3 standard/v0.2.0-draft/checks/run_checks.py   work/nam-8224-nsscas-2026 <T>
python3 standard/v0.2.0-draft/checks/what_to_fix.py  work/nam-8224-nsscas-2026 <T>
```

Loop until `what_to_fix.py` reports nothing to fix. If the same check fails after three attempts, record the topic, check, output and attempted repairs in `STATUS.md`, then continue with the other topics.

When every topic reads PUBLISH:

```bash
python3 standard/v0.2.0-draft/build/publish_subject.py work/nam-8224-nsscas-2026
```

Do not edit anything under `standard/`, regenerate the planning inputs, touch another workspace, modify YYeni, import cards, assign a deck or approve a fee. Those are separate operations.

## Review and report

Codex is the authoring tool for this run. Claude Code performs the required fresh-context cross-vendor review after authoring. A Chemistry teacher sample is welcome when available but is not a release prerequisite.

Report in under 250 words: topics completed or blocked; totals for claims, content units, items and notes words; final check results; every deviation; and anything in the plan that proved wrong.
