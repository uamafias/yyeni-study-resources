from pathlib import Path
import json,hashlib
W=Path(__file__).resolve().parents[1]; ROOT=W.parents[1]
r=json.loads((W/'planning/plan-verification-6137.json').read_text())
table='| Topic | Teaching outcomes* | Flashcards | Practice packages | Notes words |\n|---|---:|---:|---:|---:|\n'
for t in r['topics']:table+=f"| {t['topic_id']} {t['title']} | {t['objectives']} | {t['flashcards']} | {t['practice_packages']} | {t['notes_min']:,}–{t['notes_max']:,} |\n"
table+='| **Total** | **522** | **737** | **64** | **126,242–181,203** |\n\n*Planner teaching outcomes: 140 source bullets, two cross-cutting aims, 362 decomposed named members and 18 explicit practical/corpus supplements; these are not 522 verbatim syllabus bullets.\n'
aot='| AO | Syllabus target | Planned marks-equivalent share |\n|---|---:|---:|\n'
for a,name in [('A','Knowledge with understanding'),('B','Analysis'),('C','Judgment and decision making'),('D','Investigation')]:aot+=f"| {a} {name} | {r['ao_target'][a]}% | {r['ao_percent'][a]:.2f}% |\n"
plan='''# Plan — Namibia NSSCO Geography 6137

Owner: Vitalis P Haupindi. Workspace: `work/nam-6137-nssco-2026/`. Step 4 planning only; awaiting scope approval and the human Git checkpoint. No production notes/cards, image uploads or classroom imports are authorised by this document.

## 0. What the syllabus says

Read all 46 PDF pages before corpus analysis. Source transcription: `curriculum/syllabus-facts.json`; detailed tables and citations: `operations/analysis/6137-nssco-geography-syllabus-brief.md` at repository root. Paper 1: 120 minutes, 75 sat marks, 37.5%, three 25-mark questions, one per section. Paper 2: 105 minutes, 65 marks, 32.5%, compulsory resource/map skills. Paper 3: 120 minutes, 60 marks, 30%, two compulsory investigations. Specification-grid cells are marks, not percentages: P1 A40/B20/C15/D0; P2 A8/B50/C7/D0; P3 A12/B12/C12/D24.

The later circular confirmed by Vitalis fixes 2026 Paper 3 as **Coastal/Marine Processes and Leisure and Tourism**. Its original PDF is not on file; keep the mirrored-source and operator-confirmation provenance. Full Paper 1/2 coverage remains compulsory. Enquiry skills are integrated into relevant contexts.

## 1. What the corpus says

Fifteen 2020–2024 papers contain 535 terminal allocations and 1,375 offered marks; five report sections supply 546 preserved report blocks. Paper 1 offered marks exceed marks sat because of choice. Twenty selected answer shapes cover 26 marked allocations; 27 curated conceptual confusions become discrimination slots. Maps recovered for 2021–2024, not 2020 Amersfoort. No standalone schemes or 2025 papers are held. Do not invent unsupported map answers or official mark schemes.

Frozen Step 3 inputs and hashes live in `planning/step3-source/`. Current evidence changes identifiers only through `planning/registry-provenance-6137.json`; original excerpts, marks, errors and source references remain intact. Exposure counts remain at the original 142-outcome resolution. The 380 finer member/supplement entries are explicitly unmeasured; their builder budget class is not evidence of non-examination. DTM stage decomposition is a planner teaching breakdown, informed by the held staged corpus figure, not a newly transcribed closed syllabus list.

## 2. Command words and tariffs

Use `curriculum/assessment-framework.json`: only commands marked `use_in_prompts: true`, at observed tariffs. All generated flashcard combinations reconcile to that table. Read each complete prompt and answer shape; the same opening word can demand different work. Paper 3 conclusion cards may use the observed What/3 pattern; do not force Paper 1 How far do you agree/5 onto investigation conclusions. Each practice subpart must have a live command/tariff and an evidence-supported mark allocation, even when the whole package is longer.

## 3. Answer shapes

Use `curriculum/answer-shapes.json` and linked report evidence. Explanations require causal development; comparisons require matched contrasts; calculations require named units and transparent working when credited; map answers must cite the actual supplied resource. Judgement must address the precise claim and reach a supported decision. Investigation methods must be executable, with equipment, locations, sampling, recording and controls where relevant. Conclusions must use data and acknowledge exceptions. Never use a generic one-mark-per-sentence rubric or invent marks for examples, working or conclusions.

## 4. Card types, assessment objectives and Bloom levels

Generated work orders decide 737 flashcard slots, with distinct subtype, AO, Bloom, command and tariff labels. Do not change labels silently. Existing member slots were retargeted to real interpretation or supported judgement, not padded to chase percentages. A B-labelled card needs an actual usable resource; a C card needs a decision, evidence and criterion; D requires genuine enquiry/presentation.

There are 64 practice packages: 17 short-answer (7 marks, A5/B2), 18 data-response (7 marks, A1/B5/C1), 17 case-analysis (5 marks, C5), and 12 investigation halves (30 marks, A6/B6/C6/D12). The latter split is a proportional teaching allocation from the grid, not a claim about every official question. Four investigation halves each belong to 1.5, 2.3 and 4.1; alternate coasts/tourism in 4.1, allowing six paired practice papers. Derived `planning/performance-specs-6137.json` makes package labels/splits explicit. Authors select 2–4 genuinely exercised outcomes from each declared pool and record them; individual subparts still need evidence-supported allocations.

## 5. The topics

'''+table+'''
There are 160 content units. The large notes budget comes from full named-outcome coverage and the standard's generated depth budgets, including finer outcomes with unmeasured exposure. It is a proposed scope for approval, not already written prose. Do not pad to minimum length, collapse named mechanisms into abstract templates, or silently cut sections to save words. Teach each named examinable point, worked procedure and relevant example clearly; report any genuine budget/design problem before changing the plan.

## 6. AO balance, in marks

'''+aot+f'''
Independent unrounded recomputation gives a largest gap of **{r['largest_gap_percentage_points']:.3f} percentage points**, below the five-point limit. Shared rounded report: `curriculum/ao_coverage.md`. This is the whole bank, not a promise that every topic mirrors the qualification. Per-topic C-18 warnings remain visible. No automatic top-up slots were added.

## 7. Misconceptions, glossary and scope

`curriculum/glossary.json` settles 63 senses. Five source ambiguities have primary-source decisions in `planning/definition-decisions-6137.md`: drainage basin versus watershed divide; age dependency ratio and specified bands; infant mortality denominator/age; period total fertility; replenishment conditions for wood biomass. Preserve the distinctions rather than copying ambiguous source wording. HIV/AIDS and climate/ozone terms also require precise distinctions.

All 27 curated misconception entries have planned diagnostic cards. All 13 source-grounded scope detectors are supplied to contracts; interpret them in context, not as a ban on mentioning an excluded term in a warning. `planning/case-study-register-6137.json` fixes case choices and records research leads. A lead is not proof that future case prose has been verified. Read dated primary sources before using real-place facts or statistics; do not invent current figures. Learner businesses, where needed, are invented and locally recognisable.

## 8. Rules particular to this subject

`planning/visual-resource-plan-6137.json` binds **54 original resource sets to existing slots**: 48 software-generated diagram/chart/map sets and six licensed photographic resources. This is not 54 additional cards. Geography requires photographs, spatial representations and process sketches as well as Cartesian charts. Do not replace a required image with prose. Maps need consistent geometry, scale, key, grid, contour values and north direction; use original schematic places, not traced exam maps. Required photographs need recorded licences, attribution and derivative permissions.

Claude authors visual resources **one at a time**: specify numbers/geometry; solve independently; render; inspect full size, phone width and greyscale; check Geography concepts and mechanisms, labels and question/answer separation; record checklist and hashes. Codex independently reviews each completed resource, prompt, answer and rubric. Geometry tests alone cannot validate the teaching claim. Visual authoring begins only after the scope/checkpoint is cleared; none has been generated here.

Use the derived local PNG/SVG paths and exact item IDs. Keep question figures free of answer annotations. Notes must teach the figure before cards assess it. The current chart schema/checkers specialise in break-even charts; never fake that schema for Geography. Use ordinary image links plus asset specifications/manifest. Before publication a subject-scoped guarded helper must verify complete slots, referenced assets, hashes, note links and an import sidecar. Asset IDs remain null until a separately authorised upload/import; a GCS URL alone is not import proof.

Structural exemplars are isolated under `exemplar/work/nam-6137-nssco-2026/`: five cards in two thin slices, excluded from production totals. Both yield PUBLISH with zero FAIL, one AO warning and three NOT_RUN checks each. Claims remain unverified and non-publishable pending independent review. C-35/C-41 do not validate Geography geometry; C-43 is not run without a practice text. A shared CLI bug returns exit 1 for PUBLISH because it tests for pass; preserve raw reports, inspect actual failures and do not treat NOT_RUN as a pass. No shared tool was edited.

Do not rerun old Step 3 miners or the planning builder after approval: they overwrite the activated identifier view or generated contracts. Reopening scope requires a recorded revision and regenerated counts. Do not run an authoring template over reviewed content. Subject review, Git publication and classroom import are separate checkpoints.
'''
(W/'PLAN-6137-nssco-geography.md').write_text(plan)
handover='''# Handover prompt — Namibia NSSCO Geography 6137

## Start here

WAIT until Vitalis's Step 4 plan approval and human plan Git checkpoint are recorded in STATUS.md. This prompt is prepared for later use and does not itself grant authoring approval. Workspace `work/nam-6137-nssco-2026/`; syllabus 6137 only; owner Vitalis P Haupindi. On activation read AGENTS.md, TEAM-PLAYBOOK.md, then only AUTHOR.md for the author role. Read PLAN-6137-nssco-geography.md and the isolated exemplar. Follow the approved role/delegation boundaries in the playbook.

## The job

Author the whole approved subject from generated contracts/work orders: 737 flashcards and 64 practice packages across 18 topics, 160 content units, notes within generated budgets. The five exemplar cards are examples, not production cards. Use the exact generated filenames, IDs and source provenance. PLAN section 5 is the approved scope table once signed off. Keep the 2026 Paper 3 coasts/tourism focus while covering all Paper 1/2 content. Read notes as a learner starting this material: include every named point examiners credit, clear mechanisms and usable worked examples. Avoid abstract prose that reaches minimum length without teaching examinable content.

## Every item carries its labels

Copy subtype, assessment_objectives, blooms_level, command_word and mark_tariff from each slot. AOs and Bloom are separate axes. Use planning/performance-specs-6137.json for package splits/labels and the work-order objective pools; record 2–4 selected outcomes. Package parts require their own observed commands/tariffs and defensible rubrics. Report genuinely wrong slots; do not silently change counts or labels.

## Rules that come from the syllabus and the corpus

Read syllabus-facts, framework, answer-shapes, glossary, misconceptions and exclusions; then linked internal question/report evidence. Official material is mined, never reproduced in learner resources. No unsupported 2020 map-dependent answers, inferred mark schemes or imaginary current facts. Use verified primary sources for the fixed case choices in planning/case-study-register-6137.json. Preserve the five definition decisions. Fine-member exposure is unmeasured; never claim a member is frequent or absent from inherited umbrella counts. Papers 1/2 remain full scope; the circular confirmation establishes coasts/tourism for 2026 Paper 3.

## Voice

English-medium Namibian secondary learners. Teach named facts, reasoning, limitations and examples directly. Use N$ where relevant. Claims must support every answer and rubric point from the notes. No author/tooling instructions, invented-example labels scattered through learner prose, generic filler, or unsupported statistics about real places. Keep internal provenance in metadata.

## The work order is a baseline, not a cage

It fixes approved slots and scope. Add no new slots and change no planner outputs without a documented reopened scope. If a subtype is unsuitable or a needed visual has no usable stimulus, report the exact slot and proposed repair. Do not rerun planning/build_plan_6137.py or the old miners after approval; frozen Step 3 inputs are preserved separately. Never overwrite reviewed prose with a template script.

## Finishing each topic

Validate structured artifacts, render notes, run the standard checks and inspect qa_report.json. Require zero FAIL, preserve WARN and NOT_RUN. Shared run_checks.py currently exits 1 even when release_decision is publish; its exit test expects pass. Record that limitation and inspect actual report failures; do not change standard/. The two structural slices each have 40 pass, one warn and three not_run. Their PUBLISH is structural, not a subject review verdict. Independently review Geography figures because C-35/C-41 are break-even-specific; C-43 does not run without practice text. Completeness must reconcile every planned slot once, correct labels, all claims/notes, and no copied official wording.

## Boundaries

Only 6137 paths and authorised subject analysis/status/tracker updates. Preserve unrelated 0455 work. Claude handles the 54 visual resources one by one under planning/visual-resource-plan-6137.json: define data/geometry, independently calculate, render in software, inspect full size/phone/greyscale, then review every label, answer and rubric before moving on. Codex supplies a separate semantic and geometry/data review. Geography also needs six licensed photographs; it is not exclusively X/Y charts. Record licences and attribution; never trace official maps. Keep editable masters/specs, PNGs, hashes and question/answer separation. Do not force Geography into the break-even context.chart schema.

No upload, classroom import, Git commit or push without the appropriate user authorisation/checkpoint. Prepare a guarded subject publication helper that checks complete slots, all references/assets/hashes and emits an exact-item-ID image sidecar. Shared publisher success alone does not prove asset delivery. Keep YYeni asset IDs empty until a separately approved import.

## Report back when the subject is finished

Give topic/card/package/notes counts; exact check failures/warnings/not_run; every changed slot or scope concern; claim/source gaps; visual review statuses and hashes; originality and calculation findings; local publication status. Distinguish self-checking from independent review. Stop at the next required human/reviewer checkpoint. Do not claim publication, upload, remote push or classroom persistence without verifying that target.
'''
(W/'HANDOVER-6137-nssco-geography.md').write_text(handover)
(W/'exemplar/README.md').write_text('''# Structural exemplar — 6137

Two deliberately thin slices, not a reduced production syllabus: weathering/erosion (three cards) and sampling (two cards). Read the generated work orders, claims, content units, rendered notes and item JSON under work/nam-6137-nssco-2026/. The copied analysis/registry supports unchanged shared gates. These five items are excluded from the 801 production plan.

Both QA reports: release_decision publish; 40 PASS, one WARN (C-18), three NOT_RUN (C-35/C-41/C-43), zero FAIL. CLI incorrectly exits 1 for publish; raw logs are retained in ../planning/exemplar-checks.log. Claims are unverified/non-publishable pending independent review. This demonstrates structure only. It neither validates Geography images nor supplies a subject review verdict.
''')
(W/'planning/STEP4-REPORT-6137.md').write_text('# Step 4 planning report — 6137\n\nAwaiting Vitalis’s scope approval; no production authoring or Git actions.\n\n'+table+'\n'+aot+'\nIndependent plan reconciliation: PASS. See plan-verification-6137.json for every assertion, exact totals, AO computation and limitations. 54 resources are planned, not generated; six require licensed photographs. Original Step 3 evidence hashes and 535 record contents are preserved. Fine exposure remains unmeasured. The two five-card exemplar slices have zero failed checks; NOT_RUN and warnings remain visible. Shared CLI exit semantics and Geography image-check limitations are documented in PLAN section 8. Plan size includes 522 teaching outcomes, not 522 source bullets.\n\nFull case facts and visuals still need authoring and independent review. User approval and the plan Git checkpoint precede Step 5.\n')
status=W/'STATUS.md';s=status.read_text().replace('Current role: Planner, step 4 in progress;','Current role: Planner, step 4 ready for scope approval;').replace('- [ ] 4 Plan built','- [x] 4 Plan built — 522 teaching outcomes, 737 flashcards, 64 practice packages, 160 content units; 54 planned resources; independently recomputed largest AO gap 0.948 percentage points.')
s=s.split('\n## Step 4 — scope ready for Vitalis')[0]
s+='''\n## Step 4 — scope ready for Vitalis\n\nThe approved analysis has been turned into generated contracts/work orders for all 18 topics. Read PLAN-6137-nssco-geography.md; the prepared author prompt is HANDOVER-6137-nssco-geography.md. Notes budget: 126,242–181,203 words. Planning reconciliation PASS; structural exemplars have zero failures, with warnings and NOT_RUN retained. No production notes/cards or images have been authored. The five isolated exemplar cards are excluded from the 801-item production plan. Earlier “no plan” statements describe earlier steps only.\n\nFrozen Step 3 evidence and identifier provenance are retained; 380 finer outcomes have no invented frequency counts. Primary definition decisions and fixed case choices are recorded separately. Shared CLI exit and image-check limitations remain unresolved and documented. No standard/ changes, publication, cloud upload, classroom import, commit or push occurred.\n\nNext checkpoint: YOU approve the concrete topic/notes/item scope and AO balance. Then the human plan Git checkpoint precedes Step 5 authoring. Both boxes remain open.\n''';status.write_text(s)
p=ROOT/'operations/SUBJECT-TRACKER.md';s=p.read_text();lines=s.splitlines();lines=[('| Namibia NSSCO | 6137 | Geography | `nam-6137-nssco-2026` | Vitalis | Codex | in progress | Step 4 plan ready: 737 flashcards + 64 practice packages, 54 planned resources, all 18 topics; largest AO gap 0.948 points. Awaiting scope approval and plan Git checkpoint. Maps 2021–2024; confirmed 2026 P3 coasts/tourism. No production authoring or push. |' if '| 6137 |' in x else x) for x in lines];p.write_text('\n'.join(lines)+'\n')
files=[W/'PLAN-6137-nssco-geography.md',W/'HANDOVER-6137-nssco-geography.md',W/'qualification-profile.yaml',W/'subject-profile.yaml',*sorted((W/'curriculum').glob('*.json')),*sorted((W/'topics').glob('*/contract.json')),*sorted((W/'topics').glob('*/work_order.json')),W/'planning/visual-resource-plan-6137.json',W/'planning/performance-specs-6137.json',W/'planning/case-study-register-6137.json']
manifest={'purpose':'Candidate scope fingerprints for human approval; not an approval record','approved':False,'committed':False,'files':{str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}}
(W/'planning/plan-approval-manifest-6137.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(table);print(aot)
