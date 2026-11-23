"""Coverage from assessed-part demand edges only. No family input or import."""
from collections import defaultdict

NSSCAS = 'examination-observed (NSSCAS 8227)'
CAMBRIDGE = 'comparable-examination-observed (Cambridge 9709)'
SYLLABUS = 'syllabus-derived'


def compute(demands, parts, comparable_items=()):
    valid = {d['demand_id'] for d in demands}
    observed, held, comparable = defaultdict(list), defaultdict(list), defaultdict(list)
    for p in parts:
        assert p['directly_assessed_demand_ids'], p['part_id']
        for did in p['directly_assessed_demand_ids']:
            if did in valid:
                target = held if p['disposition'] == 'hold' else observed
                target[did].append(p['part_id'])
    for item in comparable_items:
        if item['scope_check']['status'] == 'out-of-scope':
            continue
        assert item['transcription_status'] == 'checked-against-rendered-page'
        for did in item['assessed_8227_demand_ids']:
            assert did in valid, (item['item_id'], did)
            comparable[did].append(item['item_id'])
    rows = []
    for d in demands:
        did = d['demand_id']
        status = NSSCAS if observed[did] else CAMBRIDGE if comparable[did] else SYLLABUS
        links, clinks = sorted(set(observed[did])), sorted(set(comparable[did]))
        # Disposition is a selection decision; missing evidence does not delete
        # a prescribed demand. Source holds attach to exact exemplars, not to
        # the whole valid syllabus demand.
        reason = (f'Include prescribed demand: {d["learner_action"]}. '
                  + (f'Directly assessed in {len(links)} usable NSSCAS parts.' if links else
                     f'No usable NSSCAS part; {len(clinks)} verified comparable items.' if clinks else
                     'No usable examination item established; retain for syllabus-derived analysis.'))
        rows.append({'demand_id': did, 'objective_id': d['objective_id'],
                     'disposition': 'include', 'reason': reason, 'status': status,
                     'observed_part_links': links, 'held_source_part_links': sorted(set(held[did])),
                     'cambridge_item_links': clinks, 'recipe_ids': [],
                     'coverage_certified': False})
    return rows


def objective_rows(objectives, demand_rows):
    rows = []
    for obj in objectives:
        dr = [d for d in demand_rows if d['objective_id'] == obj['objective_id']]
        rows.append({'objective_id': obj['objective_id'], 'demands': dr,
                     'observed_part_links': sorted({p for d in dr for p in d['observed_part_links']}),
                     'cambridge_item_links': sorted({p for d in dr for p in d['cambridge_item_links']}),
                     'unobserved_demand_ids': [d['demand_id'] for d in dr if not d['observed_part_links']],
                     'status': 'Demand-level evidence only; observed links do not establish complete variation coverage',
                     'recipe_ids': [], 'coverage_certified': False})
    return rows
