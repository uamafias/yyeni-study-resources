# STATUS — 8224 Chemistry (Namibia NSSCAS)
Workspace: work/nam-8224-nsscas-2026/   Owner: Jeremy   Authoring tool: Codex   Review tool: Claude Code

Pilot: first NSSCAS subject; run with Vitalis's agreement (Jeremy, 2026-10-18). Topic 1.1 (Atoms, molecules and stoichiometry) is the step 4 exemplar slice. This workspace began before the playbook was read; earlier files (`CLAIM.md`, `REVIEW.md`, `REVIEW-RESPONSE.md`, `curriculum/SYLLABUS-SUMMARY.md`, `assessment-evidence/`) are working notes. They do not replace `syllabus-facts.json` or the corpus analysis.

- [x] 0 Claim: tracker row added (uncommitted) — 2026-10-18
- [x] 1 Sources found — 2026-10-18 (syllabus NIED 2020, updated 20 Nov 2020; 12 papers 2021-2024; 0 mark schemes; 1 examiner report, 2025 only)
- [x] 1 YOU: sources complete — Jeremy, 2026-10-18
- [x] 2 Syllabus facts written (`curriculum/syllabus-facts.json`; 143 quotes re-verified by `planning/mine_syllabus_8224.py --verify`; brief at `operations/analysis/8224-nsscas-chemistry-syllabus-brief.md`) — 2026-10-18
- [x] 2 YOU: AO table and paper table checked against the PDF — Jeremy, 2026-10-18
- [x] 3 Corpus analysis written (`operations/analysis/8224-nsscas-chemistry-corpus-analysis.md`; evidence 475 records, `curriculum/exam-exposure.json`, `answer-shapes.json` (partial), `misconceptions.json` (19, single-source), `scope-scan.json` (10 drafts), gap register and all 76 diagram-dependent records visually checked) — 2026-10-21
- [x] 3 YOU: analysis read — Jeremy authorised progression into planning, 2026-10-21
- [x] 4 Plan built — 2026-10-22. Both structural exemplars reach PUBLISH with zero failed checks; Topic 5.1 is validated against its five-objective reduced scratch contract. Current AO gap: 4 points; approval and commit outstanding.
- [x] 4 YOU: plan approved — Jeremy, 2026-10-22 (explicit “approved” in this session)
- [x] 4 YOU: plan committed locally — 2026-10-22, after Jeremy’s approval; remote push outstanding
- [ ] 5 Topics authored: 0 / N   (blocked: none)
- [ ] 5 Published
- [ ] 6 Reviewed by Claude: verdict _
- [ ] 6 YOU: verdict read
- [ ] 7 YOU: committed and pushed
- [ ] 8 (diagram) Compare with existing YYeni NSSCAS Chemistry cards (school 17, classroom `a5695c1d-390d-4025-b013-2e218a2c1ca9`; 0 cards on 2026-10-18)
- [ ] 8 (diagram) YOU: approve replacements, preview and import into YYeni

## Quality policy (reconciled with the playbook, 2026-10-22)
- Codex authors this subject and Claude Code performs the required independent cross-vendor review in a fresh context.
- RS-12 governs claims: source-backed, externally verified against an approved authority, or transparently derived from verified premises. There is no blanket two-source publication rule.
- A knowledgeable Chemistry teacher sample is recommended when available, but is not a release prerequisite. RS-13 still requires human approval for unresolved low-confidence, jurisdiction-specific, contested, medical, legal or safety-sensitive claims.
- Every generated diagram is viewed by a person, not only checked by data checks.

## Step 3 limits to carry forward
- No mark schemes 2021-2024; one examiner report (2025, papers not held). All 19 misconceptions are single-source.
- All 76 diagram-dependent evidence records were checked against 46 page images on 2026-10-21; see `assessment-evidence/IMAGE-REVIEW.md`. One locator was corrected and no meaning mapping changed.
- 2024 Paper 2 Q1(a)-(f): 6 marks inferred at 1 each (page shows only a total of 6).
- The keyword-based frequency count in `assessment-evidence/FREQUENCY-COUNT.md` is superseded by analysis section 5; do not quote it.
- Step 4 has started: `objective_registry.json`, `assessment-framework.json`, `glossary.json`, `subject-profile.yaml`, `qualification-profile.yaml`, 21 topic contracts and 21 work orders have been regenerated after Claude's review. The repaired plan has 253 objectives, 565 flashcards, 66 performance tasks and AO mix A 44%, B 39%, C 18% (largest gap 4 points). Topic 1.1 is complete (27 claims, 5 units, 30 items) and reached `DECISION: PUBLISH`. The thin Topic 5.1 titration slice (6 claims, 1 unit, 4 items, 426 content words) now passes reduced-contract validation. Both exemplars have 40 PASS, 1 WARN and 3 NOT_RUN results, with zero failures. The practical slice warning compares its legitimate 100% AO C to whole-qualification targets; graph/chart/practice-text checks are inapplicable. These are structural check results, not independent claim verification or release approval.

## Open items carried over (not playbook steps)
- The shared learning-item schema does not permit the planner's `EQUATION` or `DIAGRAM` subtypes. Topic 1.1 records one transparent `EQUATION` → `PROC` exemplar deviation. Resolve the standard-versus-plan contract before whole-subject authoring; do not silently relabel all affected slots.
- YYeni template objective records need repair (lessons 6626, 6658, 6508, 6674 and 6832 identified in the live audit). Topic 1.2 also needs a lesson in the existing classroom and lesson 6658 needs moving to the correct existing section. Nothing has been repaired: changes require an exact YYeni preview and approval.
- The old keyword frequency classifier remains unvalidated and superseded. The 2024 Paper 2 page-image check confirmed six one-response parts under `[Total: 6]`; the one-mark-per-part allocation remains explicitly inferred.
- Evidence and knowledge gaps are maintained in `assessment-evidence/GAPS.md`; authoring uses the local corpus rather than per-card web searches.
- Parked: `work/nied-6117-nssco-2020-2024/` (NSSCO 6117, earlier start; Lotto covers Ordinary).

## Step 4 completion — 2026-10-22
- `planning/validate_practical_exemplar_8224.py` copies the local curriculum/evidence into a temporary workspace, narrows only the Topic 5.1 registry branch and exemplar contract, renders notes and runs the unchanged shared check suite. Durable outputs are in `exemplar/5.1/`, including the reduced contract, context, report and hash manifest. The full practical contract and 84-slot work order remain intact.
- Fixed early rounding: 24.375 cm³ is retained through cV and the final concentration is 0.09750 mol dm⁻³ to four significant figures.
- Corrected the framework's permitted subtype/AO union to include C for PROC, APP, CALC, INTERP, EVAL and SYNTH; the subject profile still chooses actual AOs by objective and paper.
- Corrected nested exposure evidence to recompute from direct objective mappings. All 39 practical criteria currently have no direct bullet-level evidence mapping; the existing broad skill-category figures are retained only as explicitly labelled planning proxies (`frequency_basis`). They must not be described as per-objective examination frequencies. No contracts, work orders or slot allocations were regenerated.
- Shared CLI defect observed: `run_checks.py` prints PUBLISH but returns 1 because it compares the release decision with `pass`. The workspace validator checks the persisted `publish` decision and every check status; no standard file was edited.
- Next checkpoint: Jeremy reviews the topic and AO tables in the plan and explicitly approves it. Resolve the EQUATION/DIAGRAM schema mismatch before whole-subject authoring, then commit the approved plan.

## Approval recorded — 2026-10-22
Jeremy explicitly approved the completed plan: 21 topics, 253 objectives, 565 flashcards, 66 tasks and 65,205–92,861 notes words. Scope approval is complete. The shared-schema decision is pending separately; a minimal patch preserving the plan is prepared under `planning/schema-compatibility/`. No standard file has been changed.
