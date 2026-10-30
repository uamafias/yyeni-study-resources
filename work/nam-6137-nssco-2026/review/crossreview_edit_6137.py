"""Logged repairs made during Claude's whole-subject cross-review of 6137 Geography (playbook step 6).

Every change to a notes block, item or claim is appended to review/crossreview-text-changes-6137.jsonl with
the review issue it repairs, the before text and the after text. New claims are added at revision 1 and cited
by the artefact that now carries the content; existing claim text is never rewritten here, so no other citing
artefact goes stale. Restamping and rendering are done afterwards per topic with assets/code/topic_done.sh.
Work orders, contracts, curriculum and slot labels are never touched: assert_labels() refuses an item edit
that would change a planned label.
"""
import copy
import glob
import json
import os
import time

HERE = os.path.dirname(os.path.abspath(__file__))
WS = os.path.dirname(HERE)
LOG = os.path.join(HERE, 'crossreview-text-changes-6137.jsonl')
LABELS = ('item_type', 'subtype', 'assessment_objectives', 'blooms_level', 'command_word', 'mark_tariff', 'objective_ids')


def _dump(path, raw, data):
    lines = raw.split('\n')
    ind = len(lines[1]) - len(lines[1].lstrip(' ')) if len(lines) > 1 else 1
    with open(path, 'w') as fh:
        fh.write(json.dumps(data, indent=ind or 1, ensure_ascii=False) + ('\n' if raw.endswith('\n') else ''))


def _log(rec):
    rec['logged'] = time.strftime('%Y-%m-%dT%H:%M:%S')
    with open(LOG, 'a') as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + '\n')


def _unit_of(topic, block_id):
    for p in glob.glob(os.path.join(WS, 'topics', topic, 'content-units', '*.json')):
        raw = open(p).read()
        unit = json.loads(raw)
        for b in unit['blocks']:
            if b['block_id'] == block_id:
                return p, raw, unit, b
    raise KeyError(block_id)


def block(topic, block_id, issue, old, new, cite=()):
    """Replace exactly one occurrence of `old` (or append when old == '') and optionally cite new claims."""
    p, raw, unit, b = _unit_of(topic, block_id)
    before = b['text']
    if old == '':
        b['text'] = before.rstrip() + ' ' + new.strip()
    else:
        assert before.count(old) == 1, '%s: old text occurs %d times' % (block_id, before.count(old))
        b['text'] = before.replace(old, new)
    for cid in cite:
        if cid not in b['claim_ids']:
            b['claim_ids'].append(cid)
        b['claims_seen'][cid] = 1
    unit['word_count'] = sum(len(x['text'].split()) for x in unit['blocks'])
    _dump(p, raw, unit)
    _log({'kind': 'block', 'topic': topic, 'id': block_id, 'issue': issue, 'before': before, 'after': b['text'],
          'cited_new_claims': list(cite), 'unit_word_count': unit['word_count'], 'budget': unit['word_budget']})
    return unit['word_count'], unit['word_budget']


def unit_words(topic):
    out = {}
    for p in sorted(glob.glob(os.path.join(WS, 'topics', topic, 'content-units', '*.json'))):
        u = json.load(open(p))
        out[u['unit_id']] = (sum(len(x['text'].split()) for x in u['blocks']), u['word_budget']['min'], u['word_budget']['max'])
    return out


def _items(topic):
    p = os.path.join(WS, 'topics', topic, 'learning-items', 'topic_%s_items.json' % topic)
    raw = open(p).read()
    return p, raw, json.loads(raw)


def item(topic, item_id, issue, cite=(), **fields):
    """Set item fields (prompt, canonical_answer, marking_guidance, parts, ...); planned labels may not change."""
    p, raw, data = _items(topic)
    it = next(i for i in data['items'] if i['item_id'] == item_id)
    for k in fields:
        assert k not in LABELS, 'refusing to change planned label ' + k
    before = {k: copy.deepcopy(it.get(k)) for k in fields}
    for k, v in fields.items():
        it[k] = v
    for cid in cite:
        if cid not in it['claim_ids']:
            it['claim_ids'].append(cid)
        it['claims_seen'][cid] = 1
    _dump(p, raw, data)
    _log({'kind': 'item', 'topic': topic, 'id': item_id, 'issue': issue, 'before': before, 'after': fields,
          'cited_new_claims': list(cite)})


def item_replace(topic, item_id, issue, field, old, new):
    it = get_item(topic, item_id)
    val = it[field]
    assert isinstance(val, str) and val.count(old) == 1, '%s.%s: old text occurs %s times' % (item_id, field, val.count(old) if isinstance(val, str) else '?')
    item(topic, item_id, issue, **{field: val.replace(old, new)})


def get_item(topic, item_id):
    return next(i for i in _items(topic)[2]['items'] if i['item_id'] == item_id)


def get_block(topic, block_id):
    return _unit_of(topic, block_id)[3]


def add_claim(topic, claim_id, objective_ids, text, issue, source_note):
    """Add a new claim at revision 1, modelled on the ledger's own entries, marked as reviewer-authored."""
    p = os.path.join(WS, 'topics', topic, 'claims', 'canonical_claim_ledger.json')
    raw = open(p).read()
    led = json.loads(raw)
    assert all(c['claim_id'] != claim_id for c in led['claims']), 'duplicate claim ' + claim_id
    tmpl = next(c for c in led['claims'] if set(c['objective_ids']) & set(objective_ids))
    new = {
        'claim_id': claim_id, 'objective_ids': list(objective_ids), 'text': text,
        'claim_type': 'factual', 'provenance': 'source_synthesised',
        'evidence': [tmpl['evidence'][0],
                     {'source_id': 'CROSSREVIEW-6137', 'locator': source_note, 'support_type': 'corroboration'}],
        'derived_from_claim_ids': [],
        'verification': {'status': 'unverified', 'method': 'Added by Claude during whole-subject cross-review to repair '
                         + issue + '; needs Codex verification of the added content.', 'reviewer_id': None,
                         'reviewed_at': None, 'confidence': 0.8},
        'publishable': False, 'revision': 1,
    }
    led['claims'].append(new)
    _dump(p, raw, led)
    _log({'kind': 'claim_added', 'topic': topic, 'id': claim_id, 'issue': issue, 'after': new})


def _bump_seen(obj, claim_id, rev, hits, where):
    if isinstance(obj, dict):
        if isinstance(obj.get('claims_seen'), dict) and claim_id in obj['claims_seen']:
            obj['claims_seen'][claim_id] = rev
            hits.append(where + '/' + str(obj.get('item_id') or obj.get('block_id') or obj.get('part_id') or obj.get('label') or '?'))
        for k, v in obj.items():
            _bump_seen(v, claim_id, rev, hits, where)
    elif isinstance(obj, list):
        for v in obj:
            _bump_seen(v, claim_id, rev, hits, where)


def revise_claim(topic, claim_id, new_text, issue, source_note):
    """Raise a claim's revision with corrected text (Codex's revision pattern) and move every citer's claims_seen
    to the new revision, across all topics. Citing text must be checked separately: this only keeps C-29/C-30 true."""
    p = os.path.join(WS, 'topics', topic, 'claims', 'canonical_claim_ledger.json')
    raw = open(p).read()
    led = json.loads(raw)
    c = next(x for x in led['claims'] if x['claim_id'] == claim_id)
    before = copy.deepcopy(c)
    c['text'] = new_text
    c['revision'] = c['revision'] + 1
    c['evidence'].append({'source_id': 'CROSSREVIEW-6137', 'locator': source_note, 'support_type': 'corroboration'})
    c['verification']['method'] = (c['verification'].get('method') or '') + ' Revised by Claude (final cross-check of Codex repairs, ' + issue + '); needs Codex verification.'
    _dump(p, raw, led)
    hits = []
    for t in sorted(os.listdir(os.path.join(WS, 'topics'))):
        files = glob.glob(os.path.join(WS, 'topics', t, 'content-units', '*.json')) + glob.glob(os.path.join(WS, 'topics', t, 'learning-items', '*.json'))
        for f in files:
            fraw = open(f).read()
            data = json.loads(fraw)
            n = len(hits)
            _bump_seen(data, claim_id, c['revision'], hits, os.path.basename(f))
            if len(hits) > n:
                _dump(f, fraw, data)
    _log({'kind': 'claim_revised', 'topic': topic, 'id': claim_id, 'issue': issue, 'before': before, 'after': c, 'claims_seen_moved': hits})
    return c['revision'], hits
