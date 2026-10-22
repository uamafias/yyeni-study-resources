You are Claude Code, the independent cross-vendor REVIEWER of NSSCAS Chemistry 8224, workspace work/nam-8224-nsscas-2026. Codex authored the resource. Jeremy explicitly requested this Claude review. Perform ONE complete Step 6 review, not a spot check. No subagents.

First read AGENTS.md, TEAM-PLAYBOOK.md section4 Step6, standard/v0.2.0-draft/roles/REVIEWER.md and the subject HANDOVER and STATUS. TEAM-PLAYBOOK wins conflicts: it permits learner-facing repairs and requires checks, completeness, copied wording, truth, level/scope, numbers/pictures, misconceptions and learner tests. You are not authoring a new plan.

The build is uncommitted. The operator made a complete topics/publish pre-repair archive and SHA256 snapshot in review/claude-full-r1. Do not commit or push. Review the actual filesystem snapshot; do not use git HEAD as the manuscript. Do not wait for a commit: the user explicitly requested this review now. Report this baseline limitation honestly.

Inputs in review/claude-full-r1:
- packet-index.json lists all21 topics. packet-<T>.json includes EVERY content block with exact IDs, all claims and evidence, contract and at least20 sampled items (all items where fewer than20), including all tasks, misconceptions, equations/calculations and diagram items. Read every block in every packet and all sampled items. There are390 sampled items. Packets are convenience inputs, not editable sources.
- preflight-checks.json and check-<T>.log contain newly rerun checks; metadata-completeness.json contains a fresh frozen-slot audit. Check the findings yourself from these raw results; do not equate PUBLISH with semantic certification. C32 has limited numeric parsing; C35/C41 do not validate these PNG/SVG depictions. Inspect actual diagram PNGs with Read, and recompute worked numbers independently.
- ../copied-wording.md and copied-wording.log contain the newly run comparison against ONLY the12 held Chemistry papers and2025 examiner-report PDF, excluding syllabus. Review ALL8–11-word matches; repair12+ runs unless a documented standard definition or formula. Retain allowed matches with reasons in the report.

Read source references as needed in sources/reference-pack. Official scope/qualitative notes/Data Booklet text is at planning/authoring-scratch/syllabus-layout.txt; Annexe E printed p64 is the official IR table. All other subject workspaces are out of scope. Do not browse or copy exercises. Do not rely on an old textbook for post2019 SI mole definitions. Do not claim independent verification of an unsupported source detail merely because it is plausible.

Required review:
1. Confirm all21 deterministic check decisions and warn/not_run limitations.
2. Confirm one item per frozen slot, no hidden additions, exact objectives/AOs/Bloom/command/tariff, and all51 subtype deviations recorded. Read topic authoring_notes for the81 deviations/clarifications; identify actual plan defects rather than assuming any documented deviation is acceptable.
3. Complete copied-wording disposition.
4. Read EVERY topic's full teaching text, all390 sampled items and inspect generated figures. Check mechanisms, conditions, unsupported facts, crosslinks, chemical formulae/equations and arithmetic. Source focuses in authoring_notes are priority uncertainties, not findings automatically.
5. Check every planned misconception actually discriminates the wrong idea and can be answered from the notes. For two top-tariff objectives construct an answer from the notes and assess sufficiency.
6. Write coverage evidence listing all21 topics, the sampled item IDs, notes read, images inspected, numeric examples checked and source passages used. If access/time/context prevents a requirement, report incomplete coverage. Do not claim complete review of unread files.

Permitted repairs: Edit learner-facing text in this workspace's topics/ ONLY, including blocks, items and claims. Never edit curriculum/, contracts, work orders, standard/, authoring generators, other subjects, git/settings/tool files, or external applications. Do not mass mark claims verified/publishable. A changed claim requires revision increment, updating claims_seen on every dependent block/item, and reviewed_unchanged reasons where appropriate. Record all repairs with exact IDs and before/after rationale. Source-scope or plan changes must be findings, not silent repairs. Keep item count and frozen metadata. Update authoring_notes only to record review clarifications/repairs. Do not overwrite earlier author deviations.

You have Read/Glob/Grep/Write/Edit only. The operator executes shell validation, restamping, rendering, copied-wording recheck and repackaging after your edits. Supply exact topics requiring those operations; do not say you ran them. You may adjust authored_hash using Edit only if known exactly; otherwise operator handles restamping. Claim revision changes still require correct dependency revisions in your edits.

Write these outputs under review/claude-full-r1/:
- REVIEW.md: verdict publish OR fix the plan first; separate factual review readiness and outstanding human approval; findings table (exact IDs, severity/category, passage evidence, educational consequence, repair, confidence, fixed/open), plan problems, source gaps, copied-wording allowances, warnings/not_run and learner-test answers. Do not invent a publish verdict if material issues remain.
- coverage.json: per-topic evidence, sampled item IDs, images inspected, arithmetic checked, source passages, coverage limitations.
- repairs.json: changed paths, changed claim IDs/revisions, topics needing restamp/render/check, and exact repair rationale.
- findings.json: structured findings with exact IDs, severity, status and reasons.
Update STATUS.md Step6 with your actual coverage and preliminary verdict, explicitly final operator validation still pending.

Do the full review sequentially, finish permitted repairs, write outputs, and stop. Final response concise with verdict, major findings and affected topics. No user questions, no new authoring tasks, no commit/push, no human diagram approval impersonation.
