#!/usr/bin/env python3
"""Reproduce the proposed slot-demand audit from the pre-repair slot snapshot.

This does not search for an AO target. Each record includes the objective wording,
the planned demand and an explicit uncertainty/authoring condition. No slots added.
"""
import json
from pathlib import Path

WS = Path('work/nam-6116-nssco-2026')
before = json.loads((WS/'planning/ao_slots_before_repair.json').read_text())['slots']
practical = {'prac_mmo', 'prac_presentation', 'prac_analysis', 'prac_quantitative',
             'prac_conclusion', 'prac_investigation', 'task_drawing', 'task_drawing_interp', 'prac_trend'}
reg = {o['objective_id']: o for o in json.loads((WS/'curriculum/objective_registry.json').read_text())['objectives']}
# Explicit cases read in their existing exemplar, not inferred from the subtype name.
exemplar_cases = {
 'ITEM-6116-3-156-WHY': ('AO1', 'Existing exemplar asks why a plant cell in pure water does not burst: taught osmosis and wall resistance; no unfamiliar evidence.'),
 'ITEM-6116-3-158-WHY': ('AO1', 'Existing exemplar compares red-blood-cell and leaf-cell responses in pure water: a taught wall/no-wall contrast, not new data.'),
 'ITEM-6116-3-165-CHAIN': ('AO1', 'Existing exemplar reproduces the taught water route from soil to xylem; no new evidence is interpreted.'),
 'ITEM-6116-3-169-CHAIN': ('AO1', 'Existing exemplar gives the taught active-transport account for mineral uptake; the waterlogging consequence is taught, not inferred from supplied unfamiliar results.'),
 'ITEM-6116-3-171-CHAIN': ('AO1', 'Existing exemplar gives the taught villus/kidney transport account; naming two taught sites does not create unfamiliar application.'),
 'ITEM-6116-3-174-APP': ('AO1', 'Existing exemplar states that villus cells have many mitochondria and asks how this relates to their work: this repeats a taught adaptation/function link. APP as a name does not justify B.'),
 'ITEM-6116-3-161-APP': ('AO2', 'Existing exemplar supplies an unfamiliar stem-tissue treatment and firmness observation; infer water movement and turgor. Borderline transfer: retain B provisionally only if the specimen-level observation is genuinely new, not a renamed taught example.'),
 'ITEM-6116-3-164-APP': ('AO2', 'Existing exemplar supplies new mass-gain/loss readings; infer an interval for the zero-change concentration rather than repeat the definition of osmosis.'),
 'ITEM-6116-3-166-APP': ('AO2', 'Existing exemplar supplies wet soil plus wilting after excess fertiliser; propose a conditional explanation reconciling these observations, with alternatives accepted.'),
 'ITEM-6116-3-170-APP': ('AO2', 'Existing exemplar supplies a flooded field, plentiful soil ions and deficient plants; infer a limiting uptake process from the combination, not merely name a process.'),
 'ITEM-6116-3-172-APP': ('AO2', 'Existing exemplar perturbs respiration in kidney cells and requires a prediction of urine glucose; apply the mechanism to the supplied perturbation.'),
 'ITEM-6116-4-111-WHY': ('AO2', 'Existing exemplar supplies parental genotypes and asks for a probability explanation and small-sample departure; reason from the cross. A memorised 3:1 account alone is A.'),
}
genetic_why = {
 'ITEM-6116-4-116-WHY': 'Reason from supplied co-dominant parental alleles to an outcome/probability; do not merely recite a taught co-dominance explanation.',
 'ITEM-6116-4-118-WHY': 'Reason from supplied parental sex-linked genotypes and offspring sex to an outcome/probability; a generic account of sex linkage alone is A.',
}
records = []
for s in before:
    st, oid, sid = s['subtype'], s['objective_id'], s['slot']
    typ = reg[oid]['objective_type']
    status = 'specified_taught_demand'
    if typ in practical:
        ao, rule = 'AO3', 'C-practical'
        demand = 'Assess the practical technique, plan, measurement, practical-data interpretation or method evaluation named by this objective.'
        condition = 'Keep an actual practical procedure/observation context. Isolated apparatus naming without practical use can be A3 and must be reclassified at item review.'
        status = 'conditional_on_practical_demand'
    elif sid in genetic_why:
        ao, rule = 'AO2', 'B-inference'
        demand, condition = genetic_why[sid], 'Supply the cross within this self-contained card; justify the answer from it. Otherwise A.'
        status = 'conditional_on_supplied_cross'
    elif sid in exemplar_cases:
        ao, demand = exemplar_cases[sid]
        rule = 'A-taught' if ao == 'AO1' else 'B-inference'
        condition = 'Existing exemplar wording inspected; any later rewritten prompt must be classified again.'
        status = 'exemplar_inspected'
        if sid in ('ITEM-6116-3-161-APP', 'ITEM-6116-4-111-WHY'):
            status = 'ambiguous_provisional_B'
            condition += ' Teacher decision required on whether the reasoning exceeds rehearsal of the taught case.'
    elif st in ('DEF', 'FEATURE', 'PROC', 'MECH', 'WHY', 'CHAIN', 'DIST', 'MISCON'):
        ao, rule = 'AO1', 'A-taught'
        demand = ('Reproduce, explain or discriminate the taught account required by this particular objective: ' + s['objective_title'] + '. The specified demand is taught knowledge/understanding rather than a reasoning task.')
        condition = 'Do not infer the AO from explain, compare or discuss. Re-evaluate genuine reasoned inference even in a familiar setting; absence of supplied data alone does not establish A.'
    elif st == 'EVAL':
        ao, rule = 'AO1', 'A-taught'
        demand = 'Generic taught comparison/arguments on both sides of: ' + s['objective_title'] + '. Operator classifies this taught demand as A, including the A4 implications where applicable.'
        condition = 'A genuine reasoning/decision demand may be B even in a familiar setting; do not change the label solely because this subtype is EVAL or the verb is discuss.'
        status = 'operator_classified_taught_A'
    elif st in ('CALC', 'INTERP'):
        ao, rule = 'AO2', 'B-data'
        demand = 'Manipulate/translate supplied quantities, graph, key or diagram information for: ' + s['objective_title']
        condition = 'Supply all quantities, observations or key branches needed. Recalling a formula or recognising a rehearsed label alone is A.'
        status = 'conditional_on_information_processing'
    elif st == 'APP':
        ao, rule = 'AO2', 'B-inference'
        demand = 'Apply the principle in this objective to a self-contained unfamiliar observation/case, as already required by the original APP plan: ' + s['objective_title']
        condition = 'This existing APP design calls for consequential case information and an inference: record both in authoring_notes.json. That is this slot design, not a universal syllabus requirement for B. A renamed organism or place alone is insufficient.'
        status = 'conditional_on_unfamiliar_input'
    else:
        raise ValueError(f'Unreviewed demand {sid} {st} {typ}')
    # Operator supplied a targeted corpus review. These boundaries do not force label changes.
    if sid in ('ITEM-6116-3-437-CHAIN', 'ITEM-6116-3-438-APP'):
        status = 'ambiguous_provisional_' + ('A' if ao == 'AO1' else 'B')
        condition += ' Breastfeeding boundary (2022 P2 6(a)(iii)): generic antibody/passive-immunity knowledge is A; explaining the supplied infection pattern remains A/B debatable. A table alone does not establish B; retain the current planned label pending actual prompt review.'
    if sid == 'ITEM-6116-4-110-CALC':
        status = 'ambiguous_provisional_B'
        condition += ' Standard-ratio boundary (2024 P1 34): recognition of a rehearsed 3:1 cross is A/B debatable. This slot remains provisionally B for a full derivation; do not silently replace it with ratio recognition.'
    records.append({**s, 'previous_assessment_objectives': s['assessment_objectives'],
                    'assessment_objectives': [ao], 'rule': rule, 'status': status,
                    'planned_demand': demand, 'condition': condition})
out = {'provenance': 'planning judgement under the plan approved by Lotto, 2026-10-18; boundary cases retained',
       'source': 'syllabus PDF pp.38–39; existing work-order demands and inspected exemplar prompts; operator-supplied corpus review in planning/ao_operator_review.json (not independently reverified in this follow-up)',
       'rule': {'A-taught': 'Recall, explanation, comparison or implications of taught knowledge, including a rehearsed mechanism; command word and subtype are not AO evidence.',
                'B-data': 'Select, transform or manipulate supplied information (B1–B4), not merely recall its representation.',
                'B-inference': 'Reasoned explanation, prediction, inference or problem solving (B5–B7), distinguished from reproduction of taught accounts. Supplied data and unfamiliar context are useful evidence, not universal prerequisites for B; assess the actual reasoning demand.',
                'C-practical': 'C1–C5 practical operation/planning, observations/data, conclusions or method evaluation; apparatus words alone do not suffice.'},
       'records': records}
(WS/'planning/ao_demand_audit.json').write_text(json.dumps(out, indent=2, ensure_ascii=False)+'\n')
print(f'AO demand audit: {len(records)} slot decisions; no target or tolerance used')
