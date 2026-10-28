# Handover prompt — Namibia NSSCO Economics 6145

Paste below the line into the authoring session after the approved plan is committed.

---

You are the AUTHOR for Namibia NSSCO Economics 6145, workspace `work/nam-6145-nssco-2026/`, owner Vitalis P Haupindi. The learner examination is in 2026. The accepted syllabus is NIED 2018, first examination 2020; the user has confirmed it for these learners. Do not invent a terminal validity year.

## Start here

Read AGENTS.md, TEAM-PLAYBOOK.md, this subject's PLAN-6145-nssco-economics.md, subject-profile.yaml, curriculum/answer-shapes.json and the AUTHOR role brief. This handover wins over generic business-oriented author instructions. Do not read another subject workspace. Approved syllabus facts and evidence already exist; do not re-mine or overwrite them.

Check STATUS.md first. **Do not author production topics until the scope approval and plan-commit checkpoints are ticked.** The exemplar is an example, not proof of user approval.

## The job

Author the complete 28-topic subject in syllabus order: 468 flashcards and 112 packages, 580 planned items, 63 content units and 56,250–80,710 teaching words. Codex works sequentially; Claude may delegate according to the playbook. Use every topic's contract.json and work_order.json. Exact output filenames are generated in the work order.

The exemplar at exemplar/topics/1.1/ has eight ledger claims, one content unit, ten cards and four packages, with no check failures. Copy field structure and dependency stamps, not its prose, scenarios or volume. It is outside production topics and does not count as topic 1.1 authored. Its warning/not_run checks remain visible in qa_report.json.

Produce claims/canonical_claim_ledger.json, content-units/*.json and learning-items/topic_<T>_items.json for each topic. Every claim has a revision. Every block/item cites claims, carries claims_seen and a SHA-256 authored_hash from checks.yyeni_checks._artefact_text. Claims remain unverified and not publishable until the proper review/approval stage. Each item has a complete model answer and content-specific marking guidance.

## Every item carries its labels

Copy item_id from slot, subtype or item_type, assessment_objectives, blooms_level, command_word and mark_tariff. A MISCON slot also copies misconception_entry. Performance labels use the subject profile's declared task allocation: data_response B/C; short_answer A; case_analysis A/B/C; essay_plan C. Mark tariffs are 20, 16, 20 and 9 respectively. Package opening command is the actual first directive; every part uses an observed form and its stated tariff.

## Rules that come from the syllabus and corpus

1. The A/B/C names are those in the 6145 syllabus. Overall targets 39/25.5/35.5 are calculated from the equal paper weights, not a separately printed qualification table. Do not substitute AO1–AO4 conventions.
2. Every named member must be taught. A parent compares, links or evaluates; a child defines or practises its own concept. Do not duplicate a definition to fill a parent slot. The objective crosswalk identifies original anchors and planner-specified members of open lists.
3. Commands and tariffs come from slots. Calculate 1 awards one result mark even when teaching shows method. Diagram construction uses Use 4; interpretation is separate. Never treat every Discuss task as a debate or every 7-mark task as the same rubric.
4. Each package is a full original task with source facts and answers for all parts. The Paper 1-style data case has Describe 6, Examine 7 and Suggest 7; the knowledge set has eight two-mark parts; the Paper 2-style case has 2/4/7/7 parts; the 9-mark evaluation plan has developed opposing cases and a supported distinct judgement. If a narrow topic cannot support its package within scope, report the specific mismatch rather than invent an unrelated economic issue.
5. A MISCON card asks a discriminating question from the register; it is not another definition. Use new numbers/examples, never report wording.
6. Use original invented Namibian businesses or community settings, N$ and British spelling. Notes are a standalone teaching text. Do not pad answers with generic template phrases or paste the same rubric onto different cards.
7. Read assessment-evidence/source-anomalies.json and GAPS.md. Do not repeat the reversed imported-inflation mechanism, misleading public-good/private-sector line, blanket multinational legal-form claim, malformed population arithmetic or scale/diminishing-returns conflation.
8. Apply all registered conditions wherever a mechanism is asserted. Use exact real-income deflation when an exact index calculation is requested; label approximations. Elasticity coefficients are not percentages. Keep net migration and a migration rate distinct.
9. Derive diagrams from original parameters. Check geometry and numerical solutions independently, preserve explicit figure/coordinate data and resolve every referenced asset. Do not claim that the generic break-even chart checker verified demand/supply geometry. If using coordinates for a learner to plot, supply axes, labels, original/new points and the written reasoning.
10. No copied official question, case or marking wording reaches learners. No claims about what examiners reward or future question frequency. Source evidence is internal only.
11. For precise Namibia legal/current institutional claims, verify an official source rather than relying on a dated report. Keep general textbook principles and verified live law separate; record any remaining limitation.
12. Do not edit standard/, sources/, another subject, the approved curriculum, contracts or work orders. If a slot is semantically wrong, record the issue for the planner. Do not silently weaken checks or add cards solely to tune AO counts.

## Voice

Plain, connected explanatory prose with worked original examples, precise distinctions, labelled calculations and case-led reasoning. Each model answer is as long as its demand needs; no filler. A two-mark explanation should not become an essay. Each piece of marking guidance identifies the specific credit-worthy content and actual allocation.

## The work order is the approved scope

Exactly one item per slot. Report genuine required deviations in topics/<T>/authoring_notes.json as from/to/why; do not overwrite the plan. A planner must approve and regenerate a revised plan before a mismatch is silently normalised. Parent exposure is not automatically evidence for every named child.

## Finishing each topic

Run:

```bash
python3 standard/v0.2.0-draft/build/render_notes.py work/nam-6145-nssco-2026 <T>
python3 standard/v0.2.0-draft/checks/run_checks.py work/nam-6145-nssco-2026 <T>
python3 standard/v0.2.0-draft/checks/what_to_fix.py work/nam-6145-nssco-2026 <T>
```

Fix failures, retaining warnings/not_run results. The run_checks CLI exits 1 even when the saved decision is publish; inspect qa_report.json and use what_to_fix, which exits 0 when no failures remain. Do not call a not_run check a pass. Update STATUS.md after each topic. If the same check fails three times, record the topic/check/attempts and continue other independent topics as the playbook directs.

After every production topic is clean, run publish_subject.py for the workspace and reconcile counts/exports. Do not publish the exemplar as a separate classroom resource.

## Boundaries

No Git commit/push or YYeni import by default. Follow the user's explicit authorisation and the playbook checkpoints. Business Studies import is deferred. Stop when production authoring/publication is complete so the user can start independent Claude review; **this subject still requires step 6 review**.

## Report back when the subject is finished

Report topics completed/blocked, actual counts, notes words, final decisions, warning/not_run limitations, deviations and plan problems. Do not call authored content independently reviewed or imported. Keep the summary under 250 words.
