#!/usr/bin/env python3
"""
Apply one diagram card's canonical text to its topic: the learning item, any new claims, and the
notes blocks that teach and show the diagram.

    python3 work/nam-6145-nssco-2026/diagrams/apply_card_text.py ITEM-ID

Reads diagrams/cardtext/<ITEM-ID>.json:

    item         full learning item (new card) or the fields to change (existing card)
    new_claims   claims to add to the topic ledger (revision 1)
    unit_objectives   objective ids the content unit must list (added, never removed)
    blocks       [{"op": "insert_after"|"replace", "anchor"|"block_id": ..., "block": {...}}]
    block_text_edits  [{"block_id", "old", "new"}] exact substring replacements in existing blocks

Running it twice changes nothing the second time. New items, claims and blocks are stamped here
(authored_hash, qa_status, claims_seen). Edited existing artefacts are left for
operations/tools/restamp.py, which records prior_hash and the repair note.
"""
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WS = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(WS))
sys.path.insert(0, os.path.join(ROOT, 'standard', 'v0.2.0-draft', 'checks'))
from yyeni_checks import _artefact_text  # noqa: E402


def stamp(x):
    x['authored_hash'] = hashlib.sha256(_artefact_text(x).encode()).hexdigest()


def dump(path, data):
    raw = open(path).read()
    lines = raw.split('\n')
    ind = len(lines[1]) - len(lines[1].lstrip(' ')) if len(lines) > 1 else 1
    open(path, 'w').write(json.dumps(data, indent=ind or 1, ensure_ascii=False) + ('\n' if raw.endswith('\n') else ''))


def main(iid):
    spec = json.load(open(os.path.join(HERE, 'cardtext', iid + '.json')))
    T = spec['topic_id']
    td = os.path.join(WS, 'topics', T)
    led_path = os.path.join(td, 'claims', 'canonical_claim_ledger.json')
    ledger = json.load(open(led_path))
    rev = {c['claim_id']: c['revision'] for c in ledger['claims']}
    for c in spec.get('new_claims', []):
        if c['claim_id'] not in rev:
            ledger['claims'].append(c)
            rev[c['claim_id']] = c['revision']
            print('claim added', c['claim_id'])
    dump(led_path, ledger)

    unit_path = os.path.join(td, 'content-units', spec['unit_id'] + '.json')
    unit = json.load(open(unit_path))
    for o in spec.get('unit_objectives', []):
        if o not in unit['objective_ids']:
            unit['objective_ids'].append(o)
            print('unit objective added', o)
    ids = [b['block_id'] for b in unit['blocks']]
    for op in spec.get('blocks', []):
        b = dict(op['block'])
        b['claims_seen'] = {c: rev[c] for c in b['claim_ids']}
        if b['block_id'] in ids:
            cur = unit['blocks'][ids.index(b['block_id'])]
            if op['op'] == 'insert_after':
                # A block this card created: it is new authoring, so it is stamped fresh, not repaired.
                cur.clear(); cur.update(b); stamp(cur)
            else:
                keep = {k: cur[k] for k in ('authored_hash', 'prior_hash', 'repair_note') if k in cur}
                cur.clear(); cur.update(b); cur.update(keep)
            print('block refreshed', b['block_id'])
        else:
            stamp(b)
            pos = ids.index(op['anchor']) + 1
            unit['blocks'].insert(pos, b)
            ids.insert(pos, b['block_id'])
            print('block inserted', b['block_id'], 'after', op['anchor'])
    for ed in spec.get('block_text_edits', []):
        blk = unit['blocks'][ids.index(ed['block_id'])]
        if ed['old'] in blk['text']:
            blk['text'] = blk['text'].replace(ed['old'], ed['new'])
            print('block edited', ed['block_id'])
        elif ed['new'] not in blk['text']:
            sys.exit('edit for %s matches neither old nor new text' % ed['block_id'])
    unit['word_count'] = sum(len((b.get('text') or '').split()) for b in unit['blocks'])
    dump(unit_path, unit)

    items_path = os.path.join(td, 'learning-items', 'topic_%s_items.json' % T)
    data = json.load(open(items_path))
    items = data['items']
    it = spec['item']
    found = [x for x in items if x['item_id'] == it['item_id']]
    if found:
        x = found[0]
        for k, v in it.items():
            x[k] = v
        x['claims_seen'] = {c: rev[c] for c in x['claim_ids']}
        if spec.get('new_card'):
            # A card this revision created: stamped fresh, so it carries no repair history.
            for k in ('prior_hash', 'repair_note'):
                x.pop(k, None)
            stamp(x)
        print('item updated', it['item_id'])
    else:
        x = dict(it)
        x['qa_status'] = 'review_required'
        x['claims_seen'] = {c: rev[c] for c in x['claim_ids']}
        stamp(x)
        # Keep the file in slot order: after the last item whose id sorts before this one.
        pos = len(items)
        for n, y in enumerate(items):
            if y['item_id'] > x['item_id'] and y['item_id'].split('-')[2] == x['item_id'].split('-')[2]:
                pos = n
                break
        items.insert(pos, x)
        print('item added', it['item_id'])
    dump(items_path, data)


if __name__ == '__main__':
    main(sys.argv[1])
