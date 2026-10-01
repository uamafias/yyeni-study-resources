#!/usr/bin/env python3
"""Assemble learning-items/topic_12_items.json from the part files."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _lib
from _lib import stamp, save, WS
import items_part1, items_part2, items_part3, items_tasks

WO = json.load(open(os.path.join(_lib.TDIR, 'work_order.json')))

PROV = 'Authored for the 9702 AS Physics resource from the topic 12 claim ledger.'

def flash(slot, txt):
    mis = txt.get('misconception')
    prov = PROV
    if mis:
        prov = 'Discrimination card for misconception entry %s, from curriculum/misconceptions.json; %s' % (mis, PROV)
    it = {
        'item_id': 'ITEM-9702-12-' + slot,
        'objective_ids': [slot_meta['objective_id'] for slot_meta in [None] ] if False else None,
        'claim_ids': txt['claims'],
        'item_type': 'flashcard',
        'subtype': slot.split('-')[-1],
        'assessment_objectives': None,
        'blooms_level': None,
        'command_word': None,
        'mark_tariff': None,
        'difficulty': None,
        'prompt': txt['prompt'],
        'canonical_answer': txt['answer'],
        'marking_guidance': txt['guidance'],
        'context': {'sector': None, 'business_size': None, 'ownership': None, 'situation': None, 'facts': []},
        'prerequisite_item_ids': [],
        'core_status': 'core',
        'intentional_duplicate_group': None,
        'provenance': prov,
        'qa_status': 'review_required',
    }
    meta = SLOT[slot]
    it['objective_ids'] = [meta['objective_id']]
    it['assessment_objectives'] = list(meta['assessment_objectives'])
    it['blooms_level'] = meta['blooms_level']
    it['command_word'] = meta['command_word']
    it['mark_tariff'] = meta['mark_tariff']
    it['difficulty'] = meta['difficulty']
    it['claims_seen'] = {cid: _lib.CLAIMS[cid]['revision'] for cid in txt['claims']}
    return stamp(it)

def task(slot_id, t, meta):
    it = {
        'item_id': 'ITEM-9702-12-' + slot_id,
        'objective_ids': t['objective_ids'],
        'claim_ids': t['claims'],
        'item_type': 'practical_task',
        'subtype': None,
        'assessment_objectives': ['AO3'],
        'blooms_level': meta['blooms_level'],
        'command_word': t['command_word'],
        'mark_tariff': 20,
        'difficulty': 4,
        'prompt': t['prompt'],
        'canonical_answer': t['answer'],
        'marking_guidance': t['guidance'],
        'context': {'sector': None, 'business_size': None, 'ownership': None, 'situation': None, 'facts': []},
        'prerequisite_item_ids': [],
        'core_status': 'core',
        'intentional_duplicate_group': None,
        'provenance': PROV,
        'qa_status': 'review_required',
        'claims_seen': {cid: _lib.CLAIMS[cid]['revision'] for cid in t['claims']},
    }
    return stamp(it)

# index the work order slots
SLOT = {}
for s in WO['item_slots']:
    SLOT[s['slot'].replace('ITEM-9702-12-', '')] = s

ALL = {}
for part in (items_part1, items_part2, items_part3):
    ALL.update(part.S)

items = []
missing = []
for s in WO['item_slots']:
    key = s['slot'].replace('ITEM-9702-12-', '')
    if key not in ALL:
        missing.append(key)
        continue
    items.append(flash(key, ALL[key]))
assert not missing, missing

for pt in WO['performance_tasks']:
    sid = pt['slot'].replace('ITEM-9702-12-', '')
    items.append(task(sid, items_tasks.T[sid], pt))

order = {s['slot']: n for n, s in enumerate(WO['item_slots'])}
order.update({p['slot']: 1000 + n for n, p in enumerate(WO['performance_tasks'])})
items.sort(key=lambda i: order[i['item_id']])

ds = {'dataset_id': 'ITEMS-9702-12', 'topic_id': '12', 'items': items}
save(os.path.join(_lib.TDIR, 'learning-items/topic_12_items.json'), ds)
print('items:', len(items))
