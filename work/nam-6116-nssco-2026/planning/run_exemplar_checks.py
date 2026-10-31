#!/usr/bin/env python3
"""Verify existing exemplar slices in isolation; never author production topics."""
import collections
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

WS = Path('work/nam-6116-nssco-2026')
scratch = Path(tempfile.mkdtemp(prefix='6116-step4-'))/WS.name
scratch.mkdir()
for name in ('curriculum', 'assessment-evidence'):
    shutil.copytree(WS/name, scratch/name)
for name in ('qualification-profile.yaml', 'subject-profile.yaml'):
    shutil.copy2(WS/name, scratch/name)
registry = json.loads((scratch/'curriculum/objective_registry.json').read_text())
results = []
for t in ('3', '4'):
    dst = scratch/'topics'/t
    shutil.copytree(WS/'exemplar'/t, dst)
    units = [json.loads(p.read_text()) for p in sorted((dst/'content-units').glob('*.json'))]
    items = json.loads((dst/f'learning-items/topic_{t}_items.json').read_text())['items']
    ids = {oid for u in units for oid in u['objective_ids']}
    registry['objectives'] = [o for o in registry['objectives'] if o['topic_id'] != t or not o['parent_id'] or o['objective_id'] in ids]
    contract = json.loads((WS/f'topics/{t}/contract.json').read_text())
    contract['scope']['included_objective_ids'] = sorted(ids)
    contract['scope']['included_count'] = len(ids)
    contract['required_outputs']['content_units'] = len(units)
    contract['required_outputs']['learning_items'] = len(items)
    contract['depth_constraints']['item_budget'] = len(items)
    contract['depth_constraints']['word_budget'] = {k: sum(u['word_budget'][k] for u in units) for k in ('min', 'max')}
    (dst/'contract.json').write_text(json.dumps(contract, indent=2))
    wo = json.loads((WS/f'topics/{t}/work_order.json').read_text())
    slots = {i['item_id'] for i in items}
    wo['item_slots'] = [s for s in wo['item_slots'] if s['slot'] in slots]
    wo['performance_tasks'] = [s for s in wo['performance_tasks'] if s['slot'] in slots]
    # Topic 3 is the complete ten-objective slice; topic 4 deliberately demonstrates two objectives.
    assert {s['slot'] for s in wo['item_slots']} == {i['item_id'] for i in items if i.get('subtype')}
    wo['content_units'] = [u for u in wo['content_units'] if any(x in ids for x in u['objective_ids'])]
    wo['planned_item_count'] = len(items)
    wo['assessable_objective_count'] = len(ids)
    (dst/'work_order.json').write_text(json.dumps(wo, indent=2))
    results.append({'topic': t, 'objectives': sorted(ids), 'items': len(items)})
(scratch/'curriculum/objective_registry.json').write_text(json.dumps(registry, indent=2))
for r in results:
    t = r['topic']
    for script, args in [('standard/v0.2.0-draft/build/render_notes.py', [str(scratch), t]),
                         ('standard/v0.2.0-draft/checks/run_checks.py', [str(scratch), t, '--quiet']),
                         (str(WS/'planning/check_unit_budgets.py'), [str(scratch), t])]:
        result = subprocess.run([sys.executable, script, *args], capture_output=True, text=True)
        print(result.stdout)
        if script.endswith('/checks/run_checks.py'):
            qa = json.loads((scratch/f'topics/{t}/qa_report.json').read_text())
            r['checks_cli_returncode'] = result.returncode
            print('topic', t, 'decision', qa['release_decision'], 'CLI exit', result.returncode)
            print([(c['check_id'], c['status']) for c in qa['deterministic_checks'] if c['status'] != 'pass'])
            assert qa['release_decision'].lower() == 'publish'
            assert not any(c['status'] == 'fail' for c in qa['deterministic_checks'])
        elif result.returncode:
            print(result.stderr)
            raise SystemExit(result.returncode)
    r['qa'] = json.loads((scratch/f'topics/{t}/qa_report.json').read_text())
    r['scratch_notes'] = str(next((scratch/f'topics/{t}').glob('[0-9]*.md')))
out = {'scratch_workspace': str(scratch), 'slices': results,
       'scope': 'existing exemplar slices only; no production authoring or subject publication'}
(WS/'review/exemplar-checks-step4.json').write_text(json.dumps(out, indent=2)+'\n')
print('Exemplar checks saved; scratch retained for rendered sample:', scratch)
