"""Restructure analysis groups after direct mapping; never feeds coverage."""
import collections
import json
from analysis_sources import A, WB, write, reference_label
from family_inputs import DEFINITIONS, BASE, memberships


def build_families(questions, demands, comparable=()):
    families={}
    for line in DEFINITIONS.strip().splitlines():
        slug,title,decision,branches=line.split('|')
        families[slug]={'pattern_id':'8227:FAMILY:'+slug,'family_slug':slug,'version':'analysis-r2',
                        'title':title,'discriminating_decision':decision,'structural_branches':branches.split(';'),
                        'question_parts':[],'cambridge_item_ids':[],'legacy_pattern_ids':[],
                        'direct_demand_ids':[],'response_formats':[],'hold_ids':[],
                        'disposition':'include','recipe_status':'analysis group/module only; recipe economy and branch boundaries require cross-vendor re-review',
                        'bloom_status':'unclassified; classify assessed criteria per reviewed recipe version/branch later'}
    part_index={p['part_id']:p for q in questions for p in q['parts']}
    for q in questions:
        for part in q['parts']:
            slugs=memberships(q,part)
            part['pattern_ids']=[families[s]['pattern_id'] for s in slugs]
            part['connected_structure_id']=q['question_id']
            for slug in slugs:
                f=families[slug];f['question_parts'].append(part['part_id'])
                f['legacy_pattern_ids']+=part['legacy_pattern_ids']
    # Required, currently unobserved demands have explicit candidates, not
    # invented NSSCAS observations or a separate generator per demand.
    extra={'segment-area':['8227:2020:M1:T5:O02:D03'],
           'monotonicity':['8227:2020:M1:T8:O03:D02'],
           'angle-units':['8227:2020:M1:T5:O01:D01','8227:2020:M1:T5:O01:D02'],
           'coefficient-identities':['8227:2020:M1:T1:O03:D01'],
           'ap-conditions':['8227:2020:M1:T2:O02:D01'],
           'function-analysis':['8227:2020:M1:T3:O01:D01','8227:2020:M1:T3:O01:D02','8227:2020:M1:T3:O01:D03'],
           'exponential-sketch':['8227:2020:M2:T2:O02:D01'],
           'unit-vector':['8227:2020:M1:T7:O03:D01'],
           'principal-values':['8227:2020:M1:T6:O04:D01'],
           'polynomial-reconstruction':['8227:2020:M1:T1:O05:D02'],
           'stationary-points':['8227:2020:M1:T8:O04:D02'],
           'numerical-method-chain':['8227:2020:M2:T6:O02:D02']}
    descriptors=json.loads((WB.parent/'curriculum/grade-descriptions.json').read_text())['descriptors']
    for item in comparable:
        if item['scope_check']['status']=='out-of-scope':continue
        for slug in item.get('family_slugs',[]):
            assert slug in families,slug
            families[slug]['cambridge_item_ids'].append(item['item_id'])
    ci={x['item_id']:x for x in comparable}
    for slug,f in families.items():
        members=[part_index[k] for k in f['question_parts']]
        items=[ci[k] for k in f['cambridge_item_ids']]
        f['direct_demand_ids']=sorted({d for p in members for d in p['directly_assessed_demand_ids']}
                                    |{d for x in items for d in x['assessed_8227_demand_ids']}|set(extra.get(slug,[])))
        f['response_formats']=sorted({p['response_format'] for p in members}|{i['response_format'] for i in items})
        f['legacy_pattern_ids']=sorted(set(f['legacy_pattern_ids']))
        f['hold_ids']=sorted({h for p in members for h in p['hold_ids']})
        f['held_parts']=[p['part_id'] for p in members if p['disposition']=='hold']
        f['usable_parts']=[p['part_id'] for p in members if p['disposition']=='include']
        f['evidence_status']=('examination-observed (NSSCAS 8227)' if f['usable_parts'] else
                              'comparable-examination-observed (Cambridge 9709)' if items else 'syllabus-derived')
        f['source_exemplar_rule']='Held exact parts are excluded as exemplars; other valid member parts and the prescribed demand remain included.'
        f['connected_structure_ids']=sorted({p['connected_structure_id'] for p in members})
        # Original reference identity is retained, but a broad group's relation
        # to a narrower part is internal unless the full demand/response matches.
        refs=[];seen=set()
        for source in [*members,*items]:
            demand_set=set(source.get('directly_assessed_demand_ids',source.get('assessed_8227_demand_ids',[])))
            same=source.get('disposition')!='hold' and demand_set==set(f['direct_demand_ids']) and f['response_formats']==[source['response_format']]
            for original in source['examination_references']:
                ref={**original,'source_relation':original['relation'],'relation':'same-type' if same else 'related',
                     'relation_reason':'exact demand set and response format match' if same else 'Related member of broader group; no same-type claim for the whole group'}
                if original['relation']=='derived-from':
                    ref={**original,'source_relation':'derived-from'}
                ref['learner_label']=reference_label(ref)
                identity=(ref['source_sha256'],ref['question'],ref['part'],ref['relation'])
                if identity not in seen:refs.append(ref);seen.add(identity)
        f['examination_references']=refs
        f['reference_union_rule']='Union by original source identity of member parts/items; family relation recalculated conservatively. Original relations remain on parts/items.'
        if not refs:f['syllabus_derived_reason']='Required demand has no verified usable examination exemplar in this group; retain as syllabus-derived.'
        relevant=[d for d in descriptors if set(d['demand_ids'])&set(f['direct_demand_ids'])]
        easiest=[d['descriptor_id'] for d in relevant if d['grade'] in ['e','c']]
        hardest=[d['descriptor_id'] for d in relevant if d['grade']=='a']
        floor_role='directly related descriptor calibration'
        easiest_branch='Simplest stated structural branch constrained by the linked e/c descriptors; parameter bounds require later authoring review.'
        if not easiest and slug=='polynomial-division':
            easiest=['8227:GRADE:C:10']
            floor_role='prerequisite scaffold only; full polynomial division is explicitly named at grade a, not grade c'
            easiest_branch='Identify quotient/remainder in a supplied simple division identity using the grade-c factor/remainder relation; do not label unscaffolded quadratic division grade c.'
        if not easiest and slug=='linearisation':
            easiest=['8227:GRADE:E:04','8227:GRADE:C:11']
            floor_role='prerequisite scaffold only; full linearisation is explicitly named at grade a'
            easiest_branch='Read gradient/intercept from a supplied straight-line relation and apply a simple log relation; choosing the linearising transformation remains the grade-a extension.'
        f['grade_variation_bounds']={'easiest_branch':easiest_branch,'floor_link_role':floor_role,'easiest_descriptor_ids':easiest,'hardest_descriptor_ids':hardest or easiest,
             'ceiling':'No further than grade a; where no specific a descriptor applies retain the narrower e/c statement under the syllabus grade-inheritance rule.',
             'implementation_limit':'These are calibration constraints, not authored parameter domains or claims that arbitrary hard values are grade a.'}
        assert easiest or hardest,(slug,'missing grade calibration')
        f['decision_evidence']={'part_links':f['question_parts'],'cambridge_item_links':f['cambridge_item_ids'],
                               'review_basis':'Claude report section 4; round-2 author restructure; re-review pending'}
    write(A/'problem-patterns.json',{'schema_version':'workbench-analysis-8227-r2','patterns':list(families.values()),
          'scope':'Revised analysis groups and reusable modules; no family/branch count is an approved recipe count.',
          'restructure_decisions':[
              'Merge PAT14-17 as connected function analysis, PAT58-62 as numerical chain, PAT25 into vector-product components, PAT11 into GP infinity; retain AP/GP link structure.',
              'Split root condition/proof, coordinate-shape/line-curve, graph-reading/sketch, diagram-vector/algebra-vector, rate/motion, proof/equation/exact evaluation, and antiderivative/reversal/preprocessing.',
              'Departure: 2025 P2 Q7(b) is identity-extrema, not R-form, because its double-angle reduction does not require calculating R or phase.',
              'Model-only parts remain modules of optimisation/connected-rate chains; family membership does not award calculus coverage.',
              'No automatic standalone supporting-drill recipes. Thin component groups remain design candidates awaiting scope/review decisions.']})
    return list(families.values())
