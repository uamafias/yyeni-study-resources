"""Small, explicit edits to canonical 6137 items and notes blocks for linking visual resources.

Every change is logged to assets/records/text-changes-6137.jsonl with the before and after text, so
the report can list every changed passage. Restamping is done afterwards with
operations/tools/restamp.py; claims are never touched here.
"""
import glob
import json
import os
import time

HERE = os.path.dirname(os.path.abspath(__file__))
WS = os.path.dirname(os.path.dirname(HERE))
LOG = os.path.join(WS, 'assets', 'records', 'text-changes-6137.jsonl')


def _dump(path, raw, data):
    lines = raw.split('\n')
    ind = len(lines[1]) - len(lines[1].lstrip(' ')) if len(lines) > 1 else 1
    with open(path, 'w') as fh:
        fh.write(json.dumps(data, indent=ind or 1, ensure_ascii=False) + ('\n' if raw.endswith('\n') else ''))


def _log(rec):
    rec['logged'] = time.strftime('%Y-%m-%dT%H:%M:%S')
    with open(LOG, 'a') as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + '\n')


def img_card(item_id, side, alt):
    """Markdown link from topics/<T>/learning-items/ to the planned image."""
    return '![%s](../../../assets/images/%s-%s.png)' % (alt, item_id, side)


def img_notes(item_id, alt, side='answer'):
    """Markdown link from the rendered notes in topics/<T>/ to the planned image."""
    return '![%s](../../assets/images/%s-%s.png)' % (alt, item_id, side)


def items_path(topic):
    return os.path.join(WS, 'topics', topic, 'learning-items', 'topic_%s_items.json' % topic)


def edit_item(topic, item_id, resource_id, why, **fields):
    p = items_path(topic)
    raw = open(p).read()
    data = json.loads(raw)
    it = next(i for i in data['items'] if i['item_id'] == item_id)
    before = {k: it.get(k) for k in fields}
    for k, v in fields.items():
        if k == 'situation':
            it['context']['situation'] = v
        else:
            it[k] = v
    _dump(p, raw, data)
    _log({'kind': 'item', 'topic': topic, 'id': item_id, 'resource_id': resource_id, 'why': why,
          'before': before, 'after': fields})


def get_item(topic, item_id):
    data = json.load(open(items_path(topic)))
    return next(i for i in data['items'] if i['item_id'] == item_id)


def edit_block(topic, block_id, resource_id, why, old, new):
    """Replace exactly one occurrence of `old` in a block's text and recompute the unit word_count."""
    for p in glob.glob(os.path.join(WS, 'topics', topic, 'content-units', '*.json')):
        raw = open(p).read()
        unit = json.loads(raw)
        for b in unit['blocks']:
            if b['block_id'] == block_id:
                assert b['text'].count(old) == 1, 'old text must occur exactly once in ' + block_id
                before = b['text']
                b['text'] = before.replace(old, new)
                unit['word_count'] = sum(len(x['text'].split()) for x in unit['blocks'])
                _dump(p, raw, unit)
                _log({'kind': 'block', 'topic': topic, 'id': block_id, 'resource_id': resource_id, 'why': why,
                      'before': before, 'after': b['text'], 'unit_word_count': unit['word_count'],
                      'budget': unit['word_budget']})
                return unit['word_count'], unit['word_budget']
    raise KeyError(block_id)


def get_block(topic, block_id):
    for p in glob.glob(os.path.join(WS, 'topics', topic, 'content-units', '*.json')):
        for b in json.load(open(p))['blocks']:
            if b['block_id'] == block_id:
                return b
    raise KeyError(block_id)
