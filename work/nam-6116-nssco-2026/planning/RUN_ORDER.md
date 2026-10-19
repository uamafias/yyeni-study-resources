# Planning scripts: run order

Run from the repository root. Each step reads the files the earlier steps wrote.

```bash
P=work/nam-6116-nssco-2026/planning
python3 $P/transcribe_syllabus.py      # syllabus PDF -> curriculum/syllabus-facts.json
python3 $P/decompose_objectives.py     # + planning/decomposition.json (judgement)
python3 $P/build_registry.py           # + planning/objective_overrides.json -> objective_registry.json
python3 $P/mine_papers.py              # full references and opening command words (repaired 2026-10-18)
python3 $P/mine_reports.py             # only if the reports change
python3 $P/map_and_expose.py           # sub-topic proposals for parts and statements
python3 $P/validate_mapping.py         # second method; marks agreed parts validated
python3 $P/build_evidence_map.py       # objective_mapping/map_*.json (+ review_low_confidence.json) -> assessment_evidence.json
python3 $P/build_exposure.py           # -> curriculum/exam-exposure.json (objective level, from the evidence map)
python3 $P/build_curriculum_evidence.py  # raw misconceptions, answer shapes, scope scan (+ scope_patterns.json)
python3 $P/curate_misconceptions.py    # + planning/misconception_review.json (judgement)
python3 $P/build_plan_inputs.py        # -> curriculum/assessment-framework.json
python3 $P/build_glossary.py           # -> curriculum/glossary.json
python3 standard/v0.2.0-draft/build/conform_registry.py work/nam-6116-nssco-2026
python3 standard/v0.2.0-draft/build/make_contract.py    work/nam-6116-nssco-2026 --force
python3 standard/v0.2.0-draft/build/make_work_order.py  work/nam-6116-nssco-2026 --all
python3 $P/audit_ao_demands.py          # proposed per-slot judgement audit from the pre-repair snapshot; no target tuning
python3 $P/apply_ao_demand_audit.py     # audited demands + post-authoring label decisions into work orders; exact marks rollup
python3 $P/notes_budget.py             # -> curriculum/notes-budget.json (reads the contracts for comparison)
python3 $P/apply_notes_budget.py       # operative budget into every work order and contract; old figure kept as superseded
python3 $P/apply_notes_budget.py --check
python3 $P/apply_ao_demand_audit.py --check
python3 $P/build_practical_coverage.py # -> curriculum/practical-coverage.json (written vs hands-on coverage)
python3 $P/build_visual_requirements.py # -> curriculum/visual-requirements.json (images, diagrams, model drawings)
# make_work_order.py must never be rerun alone: rerun make_contract.py --force first, then AO audit application and notes-budget steps above
```

Judgement inputs also include planning/references.json (approved sources, verification), planning/dependencies.json
(teaching dependencies) and planning/objective_overrides.json (types, complete tasks, with evidence).

Files under `planning/*.json` are judgement inputs, written and reviewed by hand. Everything
under `curriculum/` and `topics/` is generated from them and from the sources; never edit those.

Checks and documents:

```bash
python3 $P/verify_transcription.py     # every bullet re-read from the PDF a second way
python3 $P/check_unit_budgets.py work/nam-6116-nssco-2026 <T>   # after authoring: units declare the operative budget
python3 $P/make_exemplar.py            # -> exemplar/ (authored slices, stamped)
python3 $P/write_sample.py <rendered notes from a scratch run>   # -> exemplar/REPRESENTATIVE-SECTION.md
python3 $P/write_exemplar_readme.py    # -> exemplar/README.md, from the exemplar files
python3 $P/run_exemplar_checks.py      # both existing slices in isolated scratch workspace; records QA JSON and CLI exit mismatch
# write_sample.py uses the topic-3 scratch_notes path in review/exemplar-checks-step4.json
python3 $P/check_step4_repairs.py      # evidence schema/partition, corrected mappings, C-39 all topics, slot invariants and exact AO sum
python3 $P/audit_reasoning_coverage.py  # bounded B1–B7 planned routes; no sufficiency claim from percentages
python3 $P/write_step4_repair_report.py # mapping/AO/visual-hold packet, before regenerating PLAN/HANDOVER
python3 $P/write_plan_docs.py          # -> PLAN-6116-nssco-biology.md, HANDOVER-6116-nssco-biology.md
python3 $P/check_docs.py               # PLAN, HANDOVER, README and files agree
```

## Visual-bank preparation (planning; does not approve full authoring)

After building the visual requirements (run from the repository root, with the project interpreter):

```bash
.venv/bin/python $P/make_graphs_6116.py        # -> visuals/generated/*-Q|A.png|svg + graphs.json (0455 plotting approach)
.venv/bin/python $P/build_visual_bank.py --acquire  # local-notes extractions; web originals + Commons metadata via `harvest run`
.venv/bin/python $P/make_visual_variants.py    # -> visuals/variants/ teaching / question / answer, from planning/visual_labels.json
.venv/bin/python $P/build_visual_bank.py       # rebuild manifest, bindings and INDEX with the variants
.venv/bin/python $P/check_visual_bank.py       # integrity only: files, hashes, rights, needs, holds; never approval
.venv/bin/python $P/check_figure_item_candidates.py  # six exact draft graph pairs; confirms all 35 item holds remain
python3 $P/write_plan_docs.py
python3 $P/check_docs.py
```

Candidates come from planning/visual_bank_sources.json (seeds) and planning/visual_candidates/candidates_*.json (sourcing passes, which follow visual_candidates/BRIEF.md). Downloads go through the shared harvester (manifest `_harvest/manifests/nam-6116-visual-bank.csv`); this workspace holds no scraping code. originals/ are never edited; reference-only/ never implies reuse clearance. A held asset (identity in doubt) never counts towards a need. No YYeni write occurs.

## Step 5 packaging, labels and checks (added 2026-10-19)

```bash
.venv/bin/python $P/../topics/audit_authoring.py            # slot/label/hash invariants, totals, approved AO estimator
.venv/bin/python $P/../topics/check_wording.py              # 8-word overlap screen against papers and report pages
.venv/bin/python $P/../topics/check_release_hygiene.py      # learner-text wording gate (lexical only)
.venv/bin/python $P/../topics/audit_guidance_structure.py   # marking-guidance structure screen -> review/GUIDANCE-STRUCTURE-AUDIT.json
.venv/bin/python $P/../topics/audit_label_proposals.py      # AO/Bloom/command-word proposals (reads review/label-audit-inputs); applies nothing
.venv/bin/python $P/../topics/build_review_package.py       # REVIEW-ONLY copy without held-figure items -> review-package/
# one topic, isolated, exits non-zero on any failure:  work/nam-6116-nssco-2026/topics/scratch_check.sh <T> topics/<T>/author_...py
```

Never run `publish_subject.py` on this workspace while figure items are held: it exports them (see review/FRAMEWORK-REPORTS-FOR-VITALIS-2026-10-19.md).
The later label decisions are in `planning/post_authoring_label_decisions.json` and applied by `apply_ao_demand_audit.py`; the proposal audit remains a historical input. Regenerate the exemplar and all topic authors after applying work-order labels.
The planning order above was re-run in a scratch copy on 2026-10-19 after the profile edit and the content repairs: every work order was byte-identical and
every contract differed only in its `generated_at` stamp, so the repairs did not change the approved plan.
