"""Build Workbench examples directly from recipe plans, with no historical card bank.

This authoring command writes candidate content only. Saved learner snapshots and
independent review archives are never rewritten. No DB/provider calls occur.
"""
from collections import Counter
from copy import deepcopy
import argparse
import hashlib
import json
from pathlib import Path
import sys
import types

API = Path(__file__).resolve().parents[1]
ROOT = API.parents[1]
DATA = API / 'data/imports/nam-6131-nssco-2026'
if 'services' not in sys.modules:
    module = types.ModuleType('services')
    module.__path__ = [str(API / 'services')]
    sys.modules['services'] = module
from services.math_workbench.registry import recipes, generate_question


def build():
    path = DATA / 'workbench-authoring-plan.json'
    plan = json.loads(path.read_text())
    if plan['schema_version'] != 'workbench-authoring-plan-v1':
        raise ValueError('Unsupported Workbench authoring plan')
    definitions = plan['recipes']
    ids = [r['recipe_id'] for r in definitions]
    if len(set(ids)) != len(ids) or set(ids) != {r.recipe_id for r in recipes()}:
        raise ValueError('Authoring plan must cover each registered recipe exactly once')
    cards = []
    for definition in definitions:
        rid = definition['recipe_id']
        seen = set()
        for example in definition['examples']:
            params = example['params']
            identity = (params['seed'], params['slot'])
            if identity in seen:
                raise ValueError('Duplicate authoring example identity')
            seen.add(identity)
            q = generate_question(rid, params['seed'], version=params['recipe_version'])
            metadata = example.get('metadata', {})
            if set(metadata) - {'source_card_key', 'syllabus_pdf_pages', 'evidence_relation'}:
                raise ValueError('Unexpected question metadata in authoring plan')
            q.update(deepcopy(metadata))
            cards.append({'recipe_id': rid, 'generator_id': rid,
                          'generator_params': deepcopy(params),
                          'native_lesson_id': definition['native_lesson_id'],
                          'source_kind': definition['source_kind'],
                          'objective_ids': q['objective_ids'], 'question_snapshot': q,
                          'contract_hash': q['grading_contract']['contract_hash']})
    summary = deepcopy(plan['summary'])
    kinds = Counter(c['source_kind'] for c in cards)
    summary.update(authoring_plan_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                   active_recipe_cards=len(cards), active_recipes=len(ids),
                   retained_recipe_cards=kinds['retained_generator'],
                   new_recipe_cards=kinds['new_generator'],
                   new_recipes=len({c['recipe_id'] for c in cards if c['source_kind']=='new_generator'}),
                   objectives_with_direct_cards=len({o for c in cards for o in c['objective_ids']}))
    return {'schema_version': 'yyeni-maths-workbench-exam-bank-v1',
            'summary': summary, 'recipe_cards': cards}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=DATA / 'workbench-bank.json')
    args = parser.parse_args()
    bank = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(bank, separators=(',', ':'), ensure_ascii=False) + '\n')
    print(json.dumps(bank['summary'], indent=2))


if __name__ == '__main__':
    main()
