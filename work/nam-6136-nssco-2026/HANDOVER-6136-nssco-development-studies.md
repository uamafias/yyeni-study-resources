# Handover — NSSCO Development Studies 6136

Workspace: `work/nam-6136-nssco-2026/`. Owner: Jeremy. Final author: Codex.
Independent final reviewer: Claude Code. Whole subject, Grades 10–11.

**Authoring authorisation:** Jeremy explicitly approved this revised version once the Claude-feedback corrections are complete and validated, and authorised starting the build (2026-10-20). Confirm the revision audit in STATUS.md, then begin. The human plan commit remains pending; Jeremy’s explicit instruction permits building before it. Never commit or push on his behalf.

## Start here

Read TEAM-PLAYBOOK.md, AGENTS.md, the AUTHOR role at Step 5, STATUS.md and PLAN-6136-nssco-development-studies.md. The playbook decides sequence/checkpoints. This handover wins over conflicting generic AUTHOR defaults. Sources, corrected syllabus and corpus checkpoints are already approved; do not repeat them. Do not use the old three-theme retrofit’s process exceptions.

Jeremy rejected an additional two-topic authoring trial and a blanket teacher-access requirement on 2026-10-20. Use the approved 6136 syllabus, papers and examiner reports as the basis for quality. Read curriculum/quality-evidence.json for the specific source-backed criteria, and subject-profile.yaml for the adapted reasoning/method/answer requirements. Existing subject profiles supplied reusable patterns; their content, AO weights, tariffs and commands do not govern this subject. Keep genuine source and technical limitations explicit. Follow the existing whole-subject playbook checkpoints without adding a new trial stage.

## The job

Author all 18 topics: 505 flashcards plus 38 structured/practical activities. The per-topic generated work order is authoritative. Treat integrated outcomes and their retained members as related teaching targets, not unrelated essays. Illustrative examples remain taught but are folded into parent lessons. Read curriculum/objective-demand.json for semantic roles and command provenance. Parent items must require a relationship or application distinct from the member items. Notes upper budgets are planning ceilings; lower allocations are advisory warnings, not a requirement to pad. Report shorter complete units and genuine duplication/depth problems.

For each topic produce its claim ledger, content-units and learning-items files, then render notes using the standard tool. Read the two thin structural examples under exemplar/proof/work/nam-6136-nssco-2026/topics/. They demonstrate structure and traceability, not volume or final prose. These are thin Codex planning examples; final resources must meet the full work orders and must not be represented as independently reviewed because the examples passed structural checks.

Codex authors topics one after another in this session, as Step 5 directs. Write only this subject’s authorised topic paths. Never commit or push. Re-run each topic’s checks and fix failures; Claude Code independently reviews the completed subject at Step 6.

## Every item carries its labels

Use each flashcard slot’s exact id as item_id, subtype, assessment_objectives, blooms_level, command_word and mark_tariff. Each flashcard’s actual demand is specified in curriculum/slot-demand-specs.json; fulfil its source/inference/decision requirement, not only the labels. Each performance slot has its full labels and subparts in curriculum/performance-slot-specs.json. Use the first subpart command as the parent item command; parent tariff is the sum of parts. The full research packages contain A1+A2=35 and B=15 marks, 50 total; these are package totals, not single-command tariffs. Keep A/B/C/D, not generic AO1–AO4. All practice AO splits are planner estimates.

Claims have revision 1 initially, verification.status unverified and publishable false; items/units use review_required. Cite claims that genuinely support each objective. Teach every cited claim in a content-unit block. Stamp each block/item with claims_seen and authored_hash after authoring; use the exact _artefact_text algorithm demonstrated in the exemplar. Preserve a proper revision trail on repairs.

## Rules that come from the syllabus and the corpus

1. Fill every slot once. Use the slot’s observed command/tariff; standalone Analyse, Evaluate and Assess do not open prompts. Syllabus glossary inclusion alone is insufficient.
2. Read answer-shapes.json and retain the limits on each exemplar. New rubrics are indicative original practice guidance, never attributed as official schemes. No universal one-mark-per-bullet rule; graphs, conclusions and reports can have bands.
3. Every MISCON slot names its register entry, distinguishes the two ideas and includes a separating test. Do not turn a study habit into an invented evidenced misconception.
4. Use glossary.json consistently; explain terms in ordinary language before asking learners to apply them.
5. Never copy assessment wording, scenarios, report phrases or answer allocations. Internal evidence and the Step 3 snapshots must not be rendered to learners.
6. Use invented organisations, Namibian/southern African settings, British English and N$. Label synthetic data as such. Do not invent current facts or claims about real people or institutions.
7. Historical NDP, population-policy and NIC examples stay in source context. Verify any current policy, agency function, health or legal statement against a primary official source and record the date/source. Prefer conceptual explanations where a current claim adds nothing.
8. Research is practical: explain instruments, sampling decisions, pilots, representation, findings, conclusions, recommendations and methodological limits with evidence. Learners may collect in groups but each presents an individual report; it is not formal assessed coursework. Fictional model enquiries must never be presented as learners’ actual work.
9. Recompute every number. Distinguish percentage points from percentage change and totals from per-person measures. No supplied value is silently invented in an answer.
10. Depictions follow the profile’s supported no-renderer policy: original tables and learner plotting/construction tasks, with explicit model coordinates, axes, scales, keys and labels. Teach the syllabus forms, including sketch maps and flow charts. No hand-authored ASCII or code-fenced plots. C-35/C-41 have no compatible general Development Studies graph model; do not claim their not_run results are passes. Graph-data correctness and suitability require independent review.
11. Keep conditions and variant distinctions with the relevant claims. Treat gender, violence, poverty, traditional societies and HIV sensitively and without stereotyping or unsupported absolutes.
12. Contracts carry the syllabus instruction/assessment safeguards plus a labelled sampling-depth policy. Every contract includes a generated per-theme teaching ceiling. No content theme is excluded. Scope patterns cannot replace semantic reading. Generate no line-graph construction tasks under the examiner-report-based practice policy.

## Voice

Direct explanatory prose for Namibian secondary learners who may be meeting the subject for the first time. Notes must stand alone offline. Use developed explanations and short original worked examples; avoid lists where learners need to see a mechanism or decision.

## The work order is a baseline, not a cage

Report a genuinely unsuitable slot and record every proposed change as {from, to, why} in the topic’s authoring_notes.json. Do not silently alter labels or reduce the plan to fit what was written. Planner corrections and regeneration belong to the planning role; authors do not edit curriculum, contracts or work orders. A persistent check failure after three attempts is reported with attempts/evidence, then the lead continues other topics.

## Finishing each topic

Run from the repository root, using the environment with yaml/jsonschema available:

```bash
python3 standard/v0.2.0-draft/build/render_notes.py work/nam-6136-nssco-2026 <T>
python3 standard/v0.2.0-draft/checks/run_checks.py work/nam-6136-nssco-2026 <T>
python3 standard/v0.2.0-draft/checks/what_to_fix.py work/nam-6136-nssco-2026 <T>
```

The current run_checks wrapper prints DECISION: PUBLISH with zero failures but exits nonzero because it compares release_decision to pass. Record the JSON decision and actual failures explicitly; do not change the standard or treat an unexplained exit as a pass. what_to_fix.py supplies the prescribed fix loop.

The lead re-runs every topic’s checks. Report warnings and not_run by id/reason. The playbook says not_run is never a pass; any required pilot-incompatible check is referred to the standard owner. Read planning/standard-compatibility.json, especially the stale subject-profile schema and graph-check limitations. Do not mark the NSSCO pilot complete while a required compatibility issue remains unresolved.

After authoring passes the applicable gates and required standard issues are resolved, use publish_subject.py as Step 5 directs. This creates repository upload output; it does not import into YYeni. Independent Claude Code review follows as Step 6, with its human commit/start checkpoint.

## Boundaries

Write only this subject’s assigned topic files, designated status and generated publish output at the authorised stage. Never edit standard/, original sources, another workspace, curriculum, the generated plan or the exemplar. No commits/pushes, no platform mutations/imports. Distinguish planning examples from completed Codex-authored topics. Claude Code is the independent resource reviewer. The cross-vendor review is required even if all deterministic checks return PUBLISH.

## Report back when the subject is finished

Under 250 words: topics completed/blocked; claims, units, items and notes words; check decision and warnings/no-opinion checks; every deviation; plan problems; unresolved standard compatibility issues. Update STATUS.md accurately. Do not label a blocked or partial subject complete.


## Post-resource-review repair requirements (2026-10-20)

Jeremy authorised correcting the completed draft after Claude’s FIX CONTENT BEFORE PUBLICATION verdict. The amendment in `curriculum/post-resource-review-amendments.json` resolves PL-1–PL-5: multi-point teaching breadth, natural member targets, named examined examples, genuine comparison/evaluation and prerequisite calculation methods. Stable slots, labels and unit ceilings remain unchanged. Section B uses own-enquiry scaffolds; no fictional model may stand in for completed personal fieldwork. The resource repair manuscript is `review/repairs/repair_resources.py`, replayed after the original author manuscripts. No new Claude review is authorised.
