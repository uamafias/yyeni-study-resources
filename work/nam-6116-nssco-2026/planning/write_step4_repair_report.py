#!/usr/bin/env python3
"""Write the operator packet from repaired mappings and the proposed AO audit."""
import collections
from fractions import Fraction
import json
from pathlib import Path

WS = Path('work/nam-6116-nssco-2026')
J = lambda p: json.loads((WS/p).read_text())
audit = J('planning/ao_demand_audit.json')['records']
rollup = J('curriculum/ao-demand-rollup.json')
ev = J('assessment-evidence/assessment_evidence.json')['records']
exceptions = J('assessment-evidence/mapping_exceptions.json')['exceptions']
assets = J('visuals/manifest.json')['assets']
bindings = J('visuals/bindings.json')['bindings']
needs = collections.Counter(n['status'] for b in bindings for n in b['needs'].values())
changed = collections.Counter(r['subtype'] for r in audit if r['assessment_objectives'] != r['previous_assessment_objectives'])
L = ['# NSSCO Biology 6116 — targeted Step 4 repairs', '',
     '**Status: Lotto approved the full plan and all current sourced/generated bank images on 2026-10-18. Full authoring has not started.**', '',
     'This packet supersedes the open repair instructions in CODEX-PLAN-REVIEW-2026-10-18.md. It does not replace the future post-authoring review.', '',
     '## Evidence repairs', '',
     '- Nucleus: 2024 P2 6(a) now maps directly to OBJ-6116-3.2-01 (cell structures). The source is a dividing animal cell rather than the palisade/liver examples named in that objective; this contextual limitation is recorded. It no longer credits prepared-slide meiosis.',
     '- Pesticide uptake: 2023 P2 2(c) remains unresolved. No available mark scheme or figure settles the uptake process. No direct objective mapping is assigned and no uptake mechanism is asserted. Contextual links remain visible but do not count.',
     '- Extinction: 2022 P2 1(d)(i) asks a definition. It remains linked to glossary/conservation context, but no longer credits habitat-destruction causes. Confidence is high in this exclusion decision, not in a direct mapping.',
     f'- {len(ev)} direct records plus {len(exceptions)} exception records account for all 341 original parts. Direct confidence: ' + ', '.join(f"{c} {sum(r['notes'][0] == 'mapping confidence: '+c for r in ev)}" for c in ('high', 'medium', 'low')) + '. Paper 1 remains unmapped.',
     '', 'The schema requires nonempty objective_ids for direct records. Exceptions are therefore retained in `assessment-evidence/mapping_exceptions.json`, outside the direct map, with counts_towards_direct_exposure=false. The raw paper inventory is unchanged. Exposure now names 264 of 540 objectives.', '',
     '## Proposed demand-based AO rule', '',
     '| AO | Classify the actual demand | Do not infer from |', '|---|---|---|',
     '| A | Recall, explain, compare or discuss taught content, including a rehearsed causal account or known implications (syllabus PDF p.38, A1–A4). | The presence of explain, why, discuss, a mechanism or comparison. |',
     '| B | Information handling (B1–B4), reasoned explanation, inference, prediction and problem solving (B5–B7). Supplied data or an unfamiliar context are not universal prerequisites; distinguish genuine reasoning from rehearsal of a taught account. | An unfamiliar organism/place name alone, or a subtype called APP/EVAL. |',
     '| C | Practical operation/planning, observation/measurement/data, conclusions or method evaluation (PDF p.39, C1–C5). | A laboratory noun alone. Isolated apparatus naming can be A3; practical operation is C1. |', '',
     'AO is separate from Bloom. The operator supplied a detailed corpus review and classification direction (planning/ao_operator_review.json). Its paraphrases/model answers are retained as operator evidence, not independently reverified official marking guidance. Generic taught comparisons are A; genotype inference and consequential data processing are B; investigation demands are C. Actual authored prompts must be audited again. Paper 1 examples do not extend the direct exposure map.', '',
     '### Concrete contrasts', '',
     '| Demand | Proposed classification and reason |', '|---|---|',
     '| Explain why a plant cell in pure water does not burst (ITEM-6116-3-156-WHY). | A: reproduce taught osmosis and cell-wall resistance. |',
     '| Infer the isotonic interval from new gain/loss readings (exemplar ITEM-6116-3-164-APP). | C4: process and interpret supplied practical observations. The equivalent non-practical data reasoning is B3/B4. |',
     '| Infer why wet seedlings wilt after excess fertiliser (ITEM-6116-3-166-APP). | B: reconcile supplied observations with a conditional mechanism; a cause is not asserted beyond the evidence. |',
     '| Relate many mitochondria in villus cells to their work (ITEM-6116-3-174-APP). | A: the existing exemplar rehearses a taught adaptation/function link. Its APP name does not establish B. |',
     '| Explain a probability and small-sample departure from a supplied parental cross (ITEM-6116-4-111-WHY). | Provisional B: reasoning from the cross. A rehearsed 3:1 account without an inference remains A; this is explicitly ambiguous. |',
     '| List learned advantages/disadvantages of dialysis versus transplant, or breast-feeding versus bottle-feeding. | A: taught arguments, following operator direction. Genuine reasoned judgement may be B even in a familiar setting; the reasoning demand must be specified. |', '',
     '## Slot audit and exact resulting balance', '',
     f'All {len(audit)} flashcard slots have an objective-specific demand, proposed AO, rationale/status and authoring condition in `planning/ao_demand_audit.json`. These decisions are applied to each work-order slot as ao_demand. {rollup["slots_changed"]} labels change: ' + ', '.join(f'{st} {n}' for st, n in sorted(changed.items())) + '.', '',
     'WHY slots were not moved together: 66 taught explanations are A, three genetics-reasoning slots remain B (conditional on a supplied cross), and 22 practical WHY slots remain C. The 51 CHAIN slots specify reproduction of taught accounts: each retains A. Absence of novel evidence alone is not the classification test. Nine taught DIST contrasts and two taught misconception discriminations also move to A. Seven generic EVAL comparisons are A following the operator direction; one rehearsed APP exemplar remains A. Breastfeeding study explanations and standard-ratio recognition remain debatable.', '',
     'No item, tariff, command word, Bloom label or objective was added/deleted to chase balance. There are still **540 objectives, 871 flashcards + 15 tasks = 886 items**, and **50,800–80,040 words** of operative notes budget.', '',
     '| AO | Exact marks-equivalent | Exact fraction of total | Percentage | Target | Gap |', '|---|---:|---:|---:|---:|---:|']
targets = {'AO1': 47, 'AO2': 28, 'AO3': 25}
for a in targets:
    m = Fraction(rollup['marks'][a]); share = rollup['shares_percent'][a]
    L.append(f'| {a} | {float(m):g} | {m / Fraction(rollup["total_marks"])} | {share:.10f}% | {targets[a]}% | {share-targets[a]:+.10f} |')
L += ['', '**Total: 2,029 marks-equivalent. Largest gap: 11.6126170527 points (B), outside five-point tolerance.** No tolerance or label adjustment was made to hide it.', '',
      'These are exact aggregates of provisional planned demands. Performance tasks retain the existing planning assumptions per topic: MCQ 12 marks split 7.5 A / 4.5 B, structured 8 split 5 A / 3 B, practical 10 C. Fractional MCQ allocations are marks-equivalent modelling, not literal half-mark MCQs; authored sets will need integer question-by-question AOs and a fresh total. Conditional B/C slots cannot be certified until prompts supply their required information/practical context.', '',
      '### Explicit ambiguous cases', '',
      '| Slot | Objective | Provisional AO | Decision needed |', '|---|---|---|---|']
for r in audit:
    if r['status'].startswith('ambiguous'):
        L.append(f'| {r["slot"]} | {r["objective_title"]} | {"/".join(r["assessment_objectives"])} | {r["condition"]} |')
ambiguous = [r for r in audit if r['status'].startswith('ambiguous')]
L += ['', f"The two disputed boundaries are recorded on {len(ambiguous)} affected slots ({sum(r['mark_tariff'] for r in ambiguous)} marks): the taught/study-pattern breastfeeding pair, the full-cross/standard-ratio boundary, and the genetics WHY probability explanation. These are not four new items. Existing planned derivation/inference remains provisionally B; taught antibody explanation remains provisionally A. Neither the presence of a table nor recognition of a standard ratio settles the AO. Generic taught comparisons are no longer listed as unresolved. The original APP input requirements remain this plan's task design, not universal syllabus prerequisites for B.", '',
      '## Visual holds and derivative disclosure', '',
      f'The manifest contains {len(assets)} asset records and {sum(len(a["files"]) for a in assets)} files; {sum(bool(a.get("hold")) for a in assets)} assets have explicit content/provenance/data holds. Needs: ' + ', '.join(f'{n} {s}' for s, n in needs.items()) + '. **All 254 image assets operator-approved; scientific verification remains separately pending; zero fulfilled requirements.**', '',
      'All previous holds remain. ROOT-001, STEM-001 and BLOOD-001 variants, HUM-021/HUM-026 cell identities and the unverified HUMANPOP graph are now explicitly excluded from candidate needs until their exact uses are resolved. Missing assets remain gaps; label/scale defects remain recorded, not repaired by an inferred key. Original files are unchanged.', '',
      'Each derivative now records its actual added labels/leaders/key panel and any masked labels/scale text, its source original, and draft creator/licence/change attribution. Asset-level changes text distinguishes the unchanged original from edited variants. The checker rejects absent derivative change disclosure and any held file used as a need candidate. Draft attribution is not a scientific or reuse-terms approval.', '',
      '## Validation and limits', '',
      '- check_step4_repairs.py: evidence schema, direct/exception partition, nucleus correction, pesticide/extinction exclusions, C-39 on all five topics, unchanged slot IDs/tariffs/commands/Bloom, permitted AOs and an independent rational total pass.',
      '- apply_ao_demand_audit.py --check and apply_notes_budget.py --check pass; work-order mix tables and mandatory demand annotations are regenerated.',
      '- check_visual_bank.py passes integrity/hold/derivative-disclosure checks. It does not approve images.',
      '- Existing exemplars regenerated from the audited labels. Both scratch slices receive PUBLISH with no failed check; C-18 warns, and C-35/C-41/C-43 remain NOT_RUN because those slices contain no applicable graphical stimulus/depiction/practice text. Unit-budget checks pass. No full-subject PUBLISH is claimed.',
      '- New shared-framework finding: standard/v0.2.0-draft/checks/run_checks.py final line exits 0 only for release_decision==pass, while successful yyeni_checks.run returns publish. Minimal reproduction: run either successful exemplar slice; report says PUBLISH, shell exit is 1. Expected exit 0 for a successful publish decision. The harness records both values and asserts no failed checks; standard/ is untouched.',
      '- PLAN/HANDOVER, representative sample and README regenerated; check_docs.py guards the repaired mapping counts and AO table as well as the existing consistency checks.', '',
      '## Approved scope and remaining checks', '',
      'The operator has settled generic taught comparisons as A and clarified that B does not universally require supplied data/unfamiliarity. The remaining boundaries are breastfeeding explanations of a study pattern and recognition of standard genetic ratios; provisional slot labels are unchanged. The percentage mismatch alone does not establish a reasoning-practice deficit. Lotto approved checking coverage before redesign. The bounded audit in REASONING-COVERAGE-AUDIT.md identifies planned routes for B1–B7; authored breadth, frequency and quality remain unverified. No additional activities or demand redesign are justified solely by the mismatch. The repository tolerance remains reported, not silently changed. Full-plan approval is recorded; full authoring has not started.', '',
      'Teacher/visual verification, missing visual assets, the unnamed school reference, the recall-ceiling denominator and the 2026 Paper 1 duration remain recorded holds/issues. Full-plan and image approvals are recorded in planning/operator_approvals.json. No full authoring, standard/ edits, commit, push or YYeni write occurred.', '']
(WS/'review/STEP4-REPAIRS-2026-10-18.md').write_text('\n'.join(L))
print('Step 4 repair packet written')
