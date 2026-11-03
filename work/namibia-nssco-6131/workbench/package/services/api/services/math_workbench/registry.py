"""Callable seeded whole-exam-question recipes and canonical recipe cards.

This registry is the workbench content contract. The old single-answer Recall
schema has different limits; integration must not truncate these whole questions
to fit its six-mark field or silently split their solution steps into cards.
"""
from copy import deepcopy
from dataclasses import dataclass
from hashlib import sha256
import json
import random
import re
from functools import lru_cache

from . import numbers, geometry, algebra, graphs, linear, statistics, coverage, extensions, legacy


@dataclass(frozen=True)
class Recipe:
    recipe_id: str
    title: str
    objective_ids: tuple[str, ...]
    module: object
    version: int = 7
    builder: object = None


RECIPE_VERSIONS = {
    'wb6131:'+key:7 for key in (
        'negative-fractional-enlargement','combined-transformations','three-by-three-matrix-arithmetic','instrument-measurements','constructing-nets','plane-figure-vocabulary','polynomial-operations','six-way-conversions',
        'proper-subsets','defining-sets-all-forms','frequency-bar-pie-pictogram',
        'complete-linear-programme','linear-quadratic-graph-intersections',
        'locus-constructions','solve-completing-square','angle-properties',
        'power-sum-exponential-graphs-sum','power-sum-exponential-graphs-exponential')}

RECIPE_VERSIONS.update({'wb6131:'+key:9 for key in (
    'graphical-linear-solution','general-intersecting-line-loci','ratio-all-shares',
    'exponential-equation-forms','combined-transformations','locus-constructions',
    'defining-sets-all-forms','telephone-bill','cell-phone-bill','till-receipt',
    'payment-receipt','clothing-account','contextual-direct-inverse-variation',
    'standard-form-four-operations','check-calculator-answer','similarity-problems',
    'geometric-nth-term-and-sum','three-by-three-matrix-arithmetic',
    'speed-time-rates','line-equation-from-graph',
    *('power-sum-exponential-graphs-'+suffix for suffix in
      ('power-minus-2','power-minus-1','power-0','power-1','power-2','power-3','sum','exponential')))})


RECIPE_VERSIONS.update({'wb6131:power-sum-exponential-graphs-'+suffix:10 for suffix in
    ('power-minus-2','power-minus-1','power-0','power-1','power-2','power-3','sum','exponential')})

# Claude R8 Low repairs; unchanged settings retain their existing versions.
RECIPE_VERSIONS.update({'wb6131:legacy:nssco_introduction_functions:1': 8, 'wb6131:contextual-direct-inverse-variation': 10, 'wb6131:legacy:nssco_equations_of_straight_lines:2': 8, 'wb6131:legacy:nssco_polynomials_algebraic_fractions:4': 8, 'wb6131:legacy:nssco_visual_quadratics:2': 8, 'wb6131:legacy:nssco_visual_loci:2': 8, 'wb6131:telephone-bill': 10, 'wb6131:legacy:nssco_matrix_basics:4': 8, 'wb6131:legacy:nssco_transformations_coordinates:5': 10, 'wb6131:legacy:nssco_directed_numbers_in_action:4': 8, 'wb6131:legacy:nssco_introduction_functions:2': 8, 'wb6131:legacy:nssco_linear_simultaneous_equations:4': 8, 'wb6131:speed-time-rates': 10, 'wb6131:legacy:nssco_determinants_inverses:4': 8, 'wb6131:legacy:nssco_polynomials_algebraic_fractions:5': 8, 'wb6131:legacy:nssco_linear_simultaneous_equations:2': 8, 'wb6131:till-receipt': 10, 'wb6131:legacy:nssco_sketching_quadratics_gradients:2': 8, 'wb6131:general-intersecting-line-loci': 10, 'wb6131:power-sum-exponential-graphs-exponential': 11, 'wb6131:legacy:nssco_quadratic_graphs:2': 8, 'wb6131:graphical-linear-solution': 10, 'wb6131:legacy:nssco_transformations_coordinates:4': 8, 'wb6131:legacy:nssco_number_classifications_properties:2': 8, 'wb6131:locus-constructions': 10, 'wb6131:legacy:nssco_introduction_functions:3': 8, 'wb6131:check-calculator-answer': 10, 'wb6131:legacy:nssco_straight_line_graphs_gradients:5': 8, 'wb6131:legacy:nssco_sketching_quadratics_gradients:1': 8, 'wb6131:ratio-all-shares': 10, 'wb6131:combined-transformations': 10, 'wb6131:legacy:nssco_equations_of_straight_lines:5': 8})

# Claude R9 residual repairs; unchanged settings retain their existing versions.
RECIPE_VERSIONS.update({'wb6131:legacy:nssco_logarithms:4': 8, 'wb6131:power-sum-exponential-graphs-exponential': 12, 'wb6131:legacy:nssco_factorisation_basics:3': 9, 'wb6131:legacy:nssco_polynomials_algebraic_fractions:1': 8, 'wb6131:power-sum-exponential-graphs-sum': 11, 'wb6131:nonlinear-inverse-composite': 8, 'wb6131:legacy:nssco_visual_loci:2': 9, 'wb6131:legacy:nssco_algebraic_manipulation_expansion:3': 8, 'wb6131:legacy:nssco_visual_quadratics:2': 9, 'wb6131:legacy:nssco_determinants_inverses:3': 8, 'wb6131:check-calculator-answer': 11, 'wb6131:legacy:nssco_quadratic_graphs:4': 8, 'wb6131:legacy:nssco_logarithms:5': 8, 'wb6131:graphical-linear-solution': 11, 'wb6131:legacy:nssco_algebraic_manipulation_expansion:2': 8, 'wb6131:legacy:nssco_factorisation_basics:2': 9, 'wb6131:legacy:nssco_linear_simultaneous_equations:3': 8, 'wb6131:legacy:nssco_quadratic_graphs:2': 9, 'wb6131:legacy:nssco_sequences:4': 8, 'wb6131:legacy:nssco_linear_simultaneous_equations:5': 8, 'wb6131:legacy:nssco_linear_simultaneous_equations:2': 9, 'wb6131:legacy:nssco_functions:2': 8, 'wb6131:legacy:nssco_transformations_coordinates:5': 11, 'wb6131:legacy:nssco_algebraic_manipulation_expansion:5': 8, 'wb6131:legacy:nssco_sketching_quadratics_gradients:1': 9, 'wb6131:legacy:nssco_linear_simultaneous_equations:4': 9})

# Keep the parallel-locus tick adjustment limited to y-axis labels.
RECIPE_VERSIONS['wb6131:legacy:nssco_visual_loci:2']=10

@lru_cache(maxsize=1)
def _recipes():
    rows = {}
    for module in (numbers, geometry, algebra, graphs, linear, statistics, coverage, extensions):
        for builder in module.BUILDERS:
            for q in builder(0, random.Random(0)):
                rid = q['recipe_id']
                assert rid not in rows, rid
                rows[rid] = Recipe(rid, q['title'], tuple(q['objective_ids']), module, version=RECIPE_VERSIONS.get(rid,7), builder=builder)
    for definition in legacy.recipe_definitions():
        rid=definition['recipe_id']
        version=9 if rid in ('wb6131:legacy:nssco_transformations_coordinates:3','wb6131:legacy:nssco_transformations_coordinates:5','wb6131:legacy:nssco_visual_transformations:4') else 8 if definition['generator_id'] in ('nssco_factorisation_basics','nssco_factorising_quadratics','nssco_factorisation_extension') or rid=='wb6131:legacy:nssco_advanced_graphs:5' else 7
        rows[rid]=Recipe(rid,definition['title'],tuple(definition['objective_ids']),legacy,version=RECIPE_VERSIONS.get(rid,version))
    return rows


def recipes():
    return tuple(_recipes().values())


def generate_question(recipe_id, seed, *, version=None):
    if type(seed) is not int or not 0 <= seed < 2**63:
        raise ValueError('seed must be an integer in [0, 2**63)')
    recipe = _recipes().get(recipe_id)
    if recipe is None:
        raise ValueError(f'Unknown workbench recipe: {recipe_id}')
    if version is not None and version != recipe.version:
        raise ValueError('Unsupported recipe version; use the immutable saved question snapshot for historical work')
    # Every recipe has its own stream, independent of registry ordering.
    stream_seed = int.from_bytes(sha256(f'{recipe_id}:{recipe.version}:{seed}'.encode()).digest()[:16], 'big')
    if recipe.module is legacy:
        q=legacy.generate(recipe_id,seed,version=recipe.version)
    else:
        candidates = recipe.builder(seed, random.Random(stream_seed), recipe_id.removeprefix('wb6131:'))
        q = deepcopy(next(q for q in candidates if q['recipe_id'] == recipe_id))
    q['generator_id'] = recipe_id
    q['generator_version'] = recipe.version
    q['generator_seed'] = seed
    known_pools={'wb6131:cube-and-prism-measures':16,'wb6131:irregular-symmetry':12,
                 'wb6131:sphere-cone-pyramid-measures':19,
                 'wb6131:conversion-graph':25,
                 'wb6131:standard-form-four-operations':24,
                 'wb6131:power-sum-exponential-graphs-power-0':54,
                 'wb6131:line-equation-from-graph':66}
    pool=known_pools.get(recipe_id)
    if recipe.module is legacy:
        from services.math_generators import get_generator
        definition=next(d for d in legacy.recipe_definitions() if d['recipe_id']==recipe_id)
        pool=getattr(get_generator(definition['generator_id']),'bank_sizes',{}).get(definition['legacy_setting'])
    q['generation_space']={'kind':'finite_parameterised_or_prepared',
        'distinct_instance_count':pool,'seed_range':[0,2**63-1],
        'disclosure':'Parameter ranges and prepared banks are finite. A new seed does not guarantee a new question; diversity is checked by question fingerprint. Null count means not exhaustively enumerated.'}
    q['card_key'] = f'{recipe_id}:seed:{seed}'
    from .diagrams import learner_assets
    visible_assets=learner_assets(q['assets'])
    from services.math_generators.prose_formatting import normalise_notation,markdown_result
    q['stem']=normalise_notation(q['stem'])
    for p in q['parts']:
        for key in ('prompt','reference_answer','teaching_context'):
            if key in p:p[key]=normalise_notation(p[key])
        for item in p['worked_steps']:
            for key in ('action','reason','result'):item[key]=normalise_notation(item[key])
        for item in p['criteria']:item['achievement']=normalise_notation(item['achievement'])
    from .content_format import attach_display_content
    attach_display_content(q)
    # Fingerprint the exact learner-facing normalised text.
    q['fingerprint']=sha256(json.dumps({'stem':q['stem'],'parts':[p['prompt'] for p in q['parts']],
        'assets':visible_assets},sort_keys=True,ensure_ascii=False).encode()).hexdigest()
    validate_question(q)
    q['grading_contract'] = grading_contract(q)
    q.pop('legacy_source_contract',None)
    return q


def validate_question(q):
    from services.math_generators.prose_formatting import notation_faults
    assert not notation_faults(q['stem']), ('Invalid stem notation',notation_faults(q['stem']))
    assert not any(re.search(r'\d{12,}',s) for s in [q['stem'],*(p['prompt'] for p in q['parts'])]), 'Long digit artefact in question prompt'
    assert all(a.get('role') in ('question_and_solution','solution_only') for a in q['assets']), 'Asset roles must be explicit'
    assert q['parts'] and q['objective_ids']
    assert set(q['objective_ids'])=={o for p in q['parts'] for o in p['objective_ids']}, 'Every mapped objective needs an assessed part'
    assert q['proposed_total_marks'] == sum(p['proposed_marks'] for p in q['parts'])
    for p in q['parts']:
        assert p['prompt'].strip() and p['reference_answer'].strip()
        texts=[p['prompt'],p['reference_answer'],p.get('teaching_context',''),*[s[k] for s in p['worked_steps'] for k in ('action','reason','result')],*[c['achievement'] for c in p['criteria']]]
        assert not any(notation_faults(t) for t in texts), ('Invalid authored notation',[(notation_faults(t),t[:160]) for t in texts if notation_faults(t)])
        assert p['objective_ids'] and set(p['objective_ids']) <= set(q['objective_ids'])
        assert sum(c['marks'] for c in p['criteria']) == p['proposed_marks']
        assert all(c['marks'] > 0 and c['achievement'].strip() for c in p['criteria'])
        assert p['worked_steps'] and all(s['action'] and s['reason'] and s['result'] for s in p['worked_steps']), (q['recipe_id'],p['worked_steps'])


def learner_question(q):
    """The complete allowlisted payload for a learner's current question.

    Generation seeds, future questions, criteria, working and reference answers
    remain server-side. The lifecycle API must still enforce ownership/position.
    """
    from .diagrams import learner_assets
    return {'stem':q['stem'],'max_marks':q['proposed_total_marks'],
            'parts':[{'part_id':chr(97+i),'prompt':p['prompt'],'max_marks':p['proposed_marks']}
                     for i,p in enumerate(q['parts'])],
            'assets':learner_assets(q['assets'])}


def grading_contract(q):
    from .diagrams import learner_assets
    contract = {'schema_version': 'maths-workbench-whole-question-v1',
                'recipe_id': q['recipe_id'], 'generator_version': q['generator_version'],
                'seed': q['generator_seed'], 'question_fingerprint': q['fingerprint'],
                'question': {'stem': q['stem'], 'parts': [p['prompt'] for p in q['parts']], 'assets': learner_assets(q['assets'])},
                'private_reference_assets': q['assets'],
                'max_marks': q['proposed_total_marks'], 'parts': [],
                'tariff_status': 'authored_proposal_pending_independent_review',
                'working_policy': 'Assess mathematical achievements, not matching the count or wording of model steps.',
                'alternative_methods': 'Accept all valid methods unless the specific part explicitly requires a method.',
                'dependencies': 'Apply only the explicit part-level dependencies and follow-through criteria. There is no blanket follow-through award and no double credit for one achievement.',
                'accuracy': 'Follow the instance instructions; where an inexact result has no stated precision, NSSCO normally requires 3 significant figures, and angles in degrees to 1 decimal place.',
                'feedback_policy': 'Recognise correct progress; diagnose only from submitted evidence; explain one consequential mathematical action or decision per meaningful step, with its reason and result.'}
    contract['review_policy']='Unclear or unreadable evidence, a disputed criterion, or a faulty question requires clarification/review. Do not invent a misconception, final grade or compulsory correction from uncertainty. Preserve the original submission. Do not claim a request was sent, a reviewer assigned, or a mark changed unless the service confirms that action.'
    contract['feedback_format']={'recognised_progress':'Credit the valid mathematical work actually present.',
        'first_relevant_error':'Identify the earliest relevant error supported by the submitted evidence; otherwise leave empty.',
        'repair_steps':'When mathematical correction is needed, provide an ordered list of action, reason and result. Use as many meaningful steps as the demand requires, without equating steps with marks. Leave empty for correct work or unresolved evidence.',
        'next_action':'Give the learner a concrete next action without falsely claiming a service action has happened.'}
    for index, p in enumerate(q['parts']):
        label = chr(97+index)
        contract['parts'].append({'part_id': label, 'max_marks': p['proposed_marks'],
                                  'reference_answer': p['reference_answer'],
                                  'criteria': [{'criterion_id': f'{label}.{j+1}', **c} for j,c in enumerate(p['criteria'])],
                                  'worked_steps': p['worked_steps'], 'objective_ids': p['objective_ids'],
                                  'alternative_methods': p['alternative_methods'],
                                  'depends_on_parts':p.get('depends_on_parts',[]),
                                  'follow_through_policy':p.get('follow_through_policy','Use the attached source criteria; no universal follow-through rule.')})
    source=q.get('legacy_source_contract') or q.get('grading_contract',{}).get('source_marking_contract')
    if source:
        contract['source_marking_contract']=source
        contract['dependencies']='Use the specific follow-through routes in the attached source marking contract; do not infer a universal entitlement.'
    contract['contract_hash'] = sha256(json.dumps(contract,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
    return contract


def regenerate_card(card):
    """Verify raw historical evidence; derived display caches may improve."""
    params=card['generator_params']
    q=generate_question(card['recipe_id'],params['seed'],version=params['recipe_version'])
    saved=card['question_snapshot']
    def evidence(value):
        if isinstance(value,dict):
            return {k:evidence(v) for k,v in value.items() if not k.endswith('_content') and k!='contract_hash'}
        if isinstance(value,(list,tuple)):
            return [evidence(v) for v in value]
        return value
    if (q['fingerprint']!=saved['fingerprint']
            or card['contract_hash']!=saved['grading_contract']['contract_hash']
            or grading_contract(saved)['contract_hash']!=card['contract_hash']
            or evidence(q['grading_contract'])!=evidence(saved['grading_contract'])):
        raise ValueError('Frozen recipe-card fingerprint or contract mismatch')
    return q


def plan_recipe_cards(recipe_id, count=10):
    if type(count) is not int or not 1 <= count <= 100:
        raise ValueError('count must be between 1 and 100')
    result, fingerprints = [], set()
    for seed in range(5000):
        q = generate_question(recipe_id,seed)
        if q['fingerprint'] in fingerprints:
            continue
        fingerprints.add(q['fingerprint'])
        result.append({'recipe_id': recipe_id, 'generator_id': recipe_id,
                       'generator_params': {'seed': seed, 'recipe_version': q['generator_version'], 'slot': len(result)+1},
                       'objective_ids': q['objective_ids'], 'question_snapshot': q,
                       'contract_hash': q['grading_contract']['contract_hash']})
        if len(result) == count:
            return result
    raise ValueError(f'{recipe_id} did not supply {count} distinct canonical examples')
