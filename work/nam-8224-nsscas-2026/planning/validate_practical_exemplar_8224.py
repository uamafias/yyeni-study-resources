#!/usr/bin/env python3
"""Check the thin practical slice in isolation without weakening the full topic.

Only the registry branch and contract counts/scope are reduced. All assessment
evidence, exposure requirements, scope exclusions and standard checks are retained.
"""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

WS = Path(__file__).resolve().parents[1]
ROOT = WS.parents[1]
EX = WS / 'exemplar' / '5.1'


def read(path):
    return json.loads(path.read_text())


def write(path, data):
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n')


with tempfile.TemporaryDirectory(prefix='8224-practical-') as tmp:
    scratch = Path(tmp)
    for directory in ('curriculum', 'assessment-evidence'):
        shutil.copytree(WS / directory, scratch / directory)
    for name in ('subject-profile.yaml', 'qualification-profile.yaml'):
        shutil.copy2(WS / name, scratch / name)
    topic = scratch / 'topics' / '5.1'
    shutil.copytree(EX, topic, ignore=shutil.ignore_patterns('qa_report.json', 'packet.sha256', 'validation-context.json'))
    units = [read(p) for p in (topic / 'content-units').glob('*.json')]
    objectives = sorted({oid for u in units for oid in u['objective_ids']})
    items = [i for p in (topic / 'learning-items').glob('*.json') for i in read(p)['items']]
    registry_path = scratch / 'curriculum' / 'objective_registry.json'
    registry = read(registry_path)
    registry['objectives'] = [o for o in registry['objectives']
                              if o.get('topic_id') != '5.1' or o['objective_id'] in objectives or not o.get('parent_id')]
    write(registry_path, registry)
    contract = read(WS / 'topics' / '5.1' / 'contract.json')
    contract['contract_id'] += '-EXEMPLAR-ONLY'
    contract['scope']['included_objective_ids'] = objectives
    contract['depth_constraints']['item_budget'] = len(items)
    contract['depth_constraints']['word_budget'] = {'min': 400, 'max': 700}
    contract['required_outputs']['learning_items'] = len(items)
    contract['required_outputs']['content_units'] = len(units)
    write(topic / 'contract.json', contract)
    subprocess.run([sys.executable, str(ROOT / 'standard/v0.2.0-draft/build/render_notes.py'), str(scratch), '5.1'], check=True)
    result = subprocess.run([sys.executable, str(ROOT / 'standard/v0.2.0-draft/checks/run_checks.py'), str(scratch), '5.1'])
    for path in topic.glob('*.md'):
        shutil.copy2(path, EX / path.name)
    for name in ('qa_report.json', 'contract.json'):
        shutil.copy2(topic / name, EX / name)
    write(EX / 'validation-context.json', {
        'scope': 'Thin structural exemplar only; not the complete 39-objective/84-item Topic 5.1.',
        'included_objective_ids': objectives, 'learning_items': len(items), 'content_units': len(units),
        'adjustments': ['Five-objective registry branch', 'Reduced exemplar scope and counts in scratch contract', '400–700-word exemplar budget'],
        'unchanged': ['Full assessment evidence and exposure requirements', 'All syllabus exclusions', 'Shared standard and check suite', 'Full Topic 5.1 contract and work order'],
    })
    paths = sorted(p for p in EX.rglob('*') if p.is_file() and p.name != 'packet.sha256')
    (EX / 'packet.sha256').write_text(''.join(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(EX)}\n' for p in paths))
    report = read(EX / 'qa_report.json')
    # The shared CLI prints PUBLISH but exits 1 because it compares with 'pass'.
    # Use the persisted decision and inspect every individual check as well.
    sys.exit(0 if report['release_decision'] == 'publish' and not any(
        c['status'] == 'fail' for c in report['deterministic_checks']) else 1)
