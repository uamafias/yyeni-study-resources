"""Read-only slot, label, tariff and baseline audit for the 0455 coverage review.

Run from the repository root: python3 work/cie-0455-igcse-2026/review/codex_audit.py
Prints JSON; does not modify content or the plan.
"""
import json
import re
import subprocess
from collections import Counter
from pathlib import Path

WS = Path('work/cie-0455-igcse-2026')
framework = {c['word']: c for c in json.loads((WS/'curriculum/assessment-framework.json').read_text())['command_words']}
rows = []
for topic in sorted((WS/'topics').iterdir(), key=lambda p: tuple(map(int, p.name.split('.')))):
    order = json.loads((topic/'work_order.json').read_text())
    path = next((topic/'learning-items').glob('*.json'))
    items = json.loads(path.read_text())['items']
    notes = json.dumps(json.loads((topic/'authoring_notes.json').read_text()))
    counts = Counter(i['item_id'] for i in items)
    lookup = {i['item_id']: i for i in items}
    slots = order['item_slots'] + order['performance_tasks']
    slot_ids = {s['slot'] for s in slots}
    differences = []
    for slot in slots:
        sid = slot['slot']
        if counts[sid] != 1:
            differences.append({'id': sid, 'field': 'item_id', 'expected_count': 1,
                                'actual_count': counts[sid], 'recorded_in_notes': sid in notes})
            continue
        for key in ('subtype', 'assessment_objectives', 'blooms_level', 'command_word', 'mark_tariff', 'item_type'):
            if key in slot and slot[key] != lookup[sid].get(key):
                documented = sid in notes
                if key == 'subtype' and slot[key] == 'DIAGRAM' and lookup[sid].get(key) == 'SYNTH':
                    documented = documented or ('DIAGRAM' in notes and 'SYNTH' in notes and
                        bool(re.search(r'(?<!\d)' + re.escape(sid.split('-')[3]) + r'(?!\d)', notes)))
                differences.append({'id': sid, 'field': key, 'expected': slot[key],
                                    'actual': lookup[sid].get(key), 'recorded_in_notes': documented})
    extras = []
    for item in items:
        sid = item['item_id']
        if sid in slot_ids:
            continue
        number = sid.split('-')[3]
        subtype = sid.split('-')[-1]
        # Authors use full first IDs followed by abbreviated IDs such as "009-CALC".
        short = number + '-' + subtype
        mentioned = sid in notes or bool(re.search(r'(?<![\w-])' + re.escape(short) + r'(?![\w-])', notes))
        replacement = f'ITEM-0455-{topic.name}-{number}-DIAGRAM'
        is_replacement = subtype == 'SYNTH' and replacement in slot_ids and replacement in notes and 'SYNTH' in notes
        if is_replacement:
            mentioned = True
        extras.append({'id': sid, 'recorded_in_notes': mentioned,
                       'record_form': 'full' if sid in notes else 'documented_replacement' if is_replacement else 'abbreviated' if mentioned else 'not_found'})
    unsupported = []
    for item in items:
        word = item.get('command_word')
        if word and (word not in framework or not framework[word]['use_in_prompts'] or
                     str(item.get('mark_tariff')) not in framework[word]['observed_tariffs']):
            unsupported.append(item['item_id'])
    baseline = json.loads(subprocess.check_output(['git','show','HEAD:'+str(path)]))['items']
    old_ids = {i['item_id'] for i in baseline}
    qa = json.loads((topic/'qa_report.json').read_text())
    rows.append({'topic': topic.name, 'items': len(items), 'planned_slots': len(slots),
                 'new_ids': sorted(set(lookup)-old_ids), 'removed_ids': sorted(old_ids-set(lookup)),
                 'slot_differences': differences, 'extra_items': extras, 'unsupported_tariffs': unsupported,
                 'decision': qa['release_decision'],
                 'non_pass_checks': [c for c in qa['deterministic_checks'] if c['status'] != 'pass']})
print(json.dumps({'totals': {'topics': len(rows), 'items': sum(r['items'] for r in rows),
                            'slots': sum(r['planned_slots'] for r in rows),
                            'new_ids': sum(len(r['new_ids']) for r in rows),
                            'removed_ids': sum(len(r['removed_ids']) for r in rows)},
                  'topics': rows}, indent=2))
