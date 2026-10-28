# Revision handover — 6145 NSSCO Economics

This replaces the original whole-subject authoring prompt, archived in planning/revision-01/baseline/. Revision-01 was **approved by Vitalis on 28 October 2026 and activated**. Do not run an old whole-subject bootstrap.

## Approved and activated starting state

Read planning/revision-01/approval-and-activation.json, STATUS.md and PLAN-6145-nssco-economics.md. Vitalis approved the 625-item revision and asked for Claude to start. Candidate curriculum, subject profile, contracts and orders are already live. Reviewed canonical content and the 580-item publication remain intact; the 45 new slots are pending. The saved baseline and activation hashes identify the starting state. Old topic QA describes the earlier 580-item scope, not a completed new build.

Claude starts the visual phase first, using CLAUDE-DIAGRAM-HANDOVER-6145.md. Codex’s nonvisual phase is pending and not running. Keep topic-file authoring sequential. The approved local authoring may proceed under Vitalis’s current instruction; the separate Git checkpoint is pending and must not be reported complete. Do not commit, push or upload from this handover.

Do not rerun planning/reopen_step4_6145.py or planning/write_revision_6145.py over the approved/activated state; they generated the proposal. Do not run old authoring bootstrap scripts. Preserve prior canonical content while filling approved slots.

## Stage 2: Codex nonvisual authoring

Role AUTHOR, workspace work/nam-6145-nssco-2026/. Read AGENTS.md, TEAM-PLAYBOOK.md and only the AUTHOR role brief. This narrowed assignment overrides the generic whole-subject run. Use `planning/revision-01/scope.json`, filtered owner Codex: **37 exact new slots**. Fill the named standard term or function, not a generic abstract category. Follow the labels and use current reviewed notes and the syllabus/corpus anchors. Add a claim where the named concept has no suitable canonical claim, and teach/map it in the existing content unit. Preserve source provenance and all prior fixes.

Complete the ten `notes-budget-work-order.json` tasks, preserving examinable points. Review the single internal-growth retargeting proposed in the plan and record it in authoring_notes before changing its existing prompt/claim dependencies. Do not alter valid cards merely for style, re-author the whole subject or pad prose to a minimum. Recalculate actual block words. If a budget cannot accommodate the named teaching, report it to the planner rather than silently changing the envelope.

Preserve all 580 existing IDs and labels and add exactly the assigned 37 cards. The eight pending Claude visual slots must remain explicitly pending, not filled with placeholders. Several topics will be incomplete until both phases finish; do not republish an incomplete extension as complete. Re-stamp and render affected canonical material, and record partial completion honestly.

## Stage 3: Claude diagrams

Claude’s visual phase is authorised to start first; paste CLAUDE-DIAGRAM-HANDOVER-6145.md into Claude. No Codex authoring is currently running. Its exact assignment is eight new and four existing diagram cards with 24 PNGs and 24 SVG masters. Codex will review those images and diagram edits. Claude also independently reviews Codex’s new nonvisual cards and budget edits; distinguish these review responsibilities in STATUS.

## Stage 4: finish and validate

Once all 625 items and assets exist, run all topic checks, complete slot/label reconciliation, copied-wording checking against subject-only assessment extracts, actual-word counts, claims/revision/hash checking, repeatable asset generation, per-side image-reference checks and canonical/export equality. Regenerate using the standard note/publish tools plus the subject-owned asset-copy helper described in the Claude handover. Never edit exports by hand. Report C-18, any C-26 and all not_run limitations honestly.

Then return for the human review/Git checkpoint. A later classroom import remains separately authorised. The later import maps local manifest sides to YYeni managed question_asset_id/answer_asset_id; it is not part of this authoring pass.
