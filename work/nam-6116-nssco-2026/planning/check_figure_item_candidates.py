#!/usr/bin/env python3
"""Check exact graph-to-item candidate records without lifting any figure hold."""
import hashlib
import json
from pathlib import Path

WS = Path('work/nam-6116-nssco-2026')
records = json.loads((WS/'planning/figure_item_candidates.json').read_text())['candidates']
assets = {a['asset_id']: a for a in json.loads((WS/'visuals/manifest.json').read_text())['assets']}
held = {}
items = {}
for topic in range(1, 6):
    base = WS/f'topics/{topic}'
    for row in json.loads((base/'authoring_notes.json').read_text())['visuals_pending']:
        held[row['item_id']] = row
    for row in json.loads((base/f'learning-items/topic_{topic}_items.json').read_text())['items']:
        items[row['item_id']] = row

assert len(held) == 35, f'Expected 35 held items; found {len(held)}'
assert len({r['item_id'] for r in records}) == len(records)
for r in records:
    item_id, aid = r['item_id'], r['asset_id']
    assert item_id in held and item_id in items, item_id
    assert not r['hold_lifted'] and r['selection_status'].startswith('exact draft candidate'), item_id
    asset = assets[aid]
    assert asset['source_kind'] == 'original_graph', aid
    assert set(items[item_id]['objective_ids']) & set(asset['objective_ids']), item_id
    for name, variant in (('question_file', 'question'), ('answer_file', 'answer')):
        f = r[name]
        match = [x for x in asset['files'] if x['path'] == f['path'] and x['variant'] == variant]
        assert len(match) == 1 and match[0]['sha256'] == f['sha256'], (item_id, name)
        assert hashlib.sha256((WS/f['path']).read_bytes()).hexdigest() == f['sha256'], (item_id, name)
print(f'figure-item candidates PASS: {len(records)} exact draft graph pairs; {len(held)} items still held')
