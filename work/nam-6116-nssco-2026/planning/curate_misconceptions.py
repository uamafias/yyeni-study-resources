#!/usr/bin/env python3
"""Gate 2: curate the raw examiner-evidenced misconception register.

The playbook requires this pass: drop duplicates, fragments and mere answering
habits, and write each survivor's discriminating test. On 0450 the register went
from 72 raw entries to 29 real confusions.

Four curation rules, applied in order and each recorded on the entry:
  DROP fragment        - the statement does not state what was confused
  DROP answering habit - spelling, handwriting, not reading the question: real,
                         but a behaviour, not a belief about biology
  MERGE duplicate      - the same confusion evidenced in more than one series;
                         kept once with every citation, which strengthens it
  KEEP                 - a stated false belief about the subject

A discriminating test is written only where the statement names both sides of
the confusion. Where it does not, the entry is kept with test=null and flagged
for a teacher, because inventing the distinction would defeat the point.
"""
import json, re, collections, difflib

WS = 'work/nam-6116-nssco-2026'
raw = json.load(open(f'{WS}/curriculum/misconceptions.json'))['misconceptions']

PAIR = re.compile(r'confus\w*\s+(?:the\s+)?(.{3,60}?)\s+(?:with|and|for)\s+(?:the\s+)?(.{3,60}?)'
                  r'(?=[.,;]|\s+(?:which|when|while|because|instead)\b|$)', re.I)
INSTEAD = re.compile(r'(?:gave|wrote|stated|described|named|defined)\s+(.{3,60}?)\s+instead of\s+(.{3,60}?)'
                     r'(?=[.,;]|$)', re.I)
HABIT = re.compile(r'spelling|misspel|handwriting|illegible|did not read the question|'
                   r'ran out of time|left blank|untidy|presentation of work', re.I)


def norm(t):
    return re.sub(r'[^a-z ]', '', t.lower()).strip()


kept, dropped, cwmiss = [], [], []
# Indicative 'Answer:' text printed beside a question is not examiner commentary.
# It leaks in as en-dash definition runs ("Effector - carry out a corrective action").
ANSWER_BLOCK = re.compile(r'(\s[-–]\s.{5,40}){2,}')
for e in raw:
    st = e['evidence_statement']
    if ANSWER_BLOCK.search(st):
        e['curation'] = 'drop: indicative answer text, not examiner commentary'
        dropped.append(e); continue
    if e['class'] == 'command-word miss':
        # A real failure, but a behaviour at the prompt, not a false belief about
        # biology. Mixing the two produces pseudo-confusions like
        # "the processes / stating them". Kept in its own register.
        e['curation'] = 'route: command-word miss register'
        cwmiss.append(e); continue
    pair = PAIR.search(st) or INSTEAD.search(st)
    if HABIT.search(st) and not pair:
        e['curation'] = 'drop: answering habit, not a belief about biology'
        dropped.append(e); continue
    if not pair and not re.search(r'thought|believ|assum|incorrect|wrongly|mistak|confus', st, re.I):
        e['curation'] = 'drop: fragment - does not state what was confused'
        dropped.append(e); continue
    e['confused_a'] = pair.group(1).strip() if pair else None
    e['confused_b'] = pair.group(2).strip() if pair else None
    e['discriminating_test'] = (
        f"Does the learner separate '{e['confused_a']}' from '{e['confused_b']}'? "
        f"A card is only correct if it names the feature that distinguishes them."
        if pair else None)
    e['needs_teacher_input'] = pair is None
    e['curation'] = 'keep'
    kept.append(e)

# merge duplicates: same confusion evidenced in more than one series
merged, seen = [], []
for e in kept:
    key = norm((e.get('confused_a') or '') + '|' + (e.get('confused_b') or '')) or norm(e['evidence_statement'])[:70]
    hit = None
    for m in merged:
        if difflib.SequenceMatcher(None, key, m['_key']).ratio() > 0.86:
            hit = m; break
    if hit:
        hit['evidence_sources'].append(e['evidence_source'])
        hit['series_count'] = len({s['examiner_report_year'] for s in hit['evidence_sources']})
    else:
        e['_key'] = key
        e['evidence_sources'] = [e.pop('evidence_source')]
        e['series_count'] = 1
        merged.append(e)
for m in merged:
    m.pop('_key', None)
    m['curated'] = True
    m['misconception_id'] = f"MISCON-6116-{merged.index(m)+1:03d}"

# --- second pass: entry-by-entry review (planning/misconception_review.json) ---
# The automatic pass above reads the two sides with a regex and takes the
# sub-topic from term matching. The review decides each entry by reading it.
review = json.load(open(f'{WS}/planning/misconception_review.json'))
byid = {m['misconception_id']: m for m in merged}
problems = [i for i in review['decisions'] if i not in byid] + \
           [i for i in byid if i not in review['decisions']]
for i, d in review['decisions'].items():
    if i in byid and not byid[i]['evidence_statement'].startswith(d['starts']):
        problems.append(f"{i}: statement no longer starts '{d['starts']}'")
if problems:
    raise SystemExit('misconception review does not match the register:\n  ' + '\n  '.join(problems))

reviewed, extra = [], []
for i, d in review['decisions'].items():
    m = byid[i]
    if d['action'] == 'drop':
        m['curation'] = 'drop on review: ' + d['reason']
        dropped.append(m)
        continue
    if d['action'] == 'merge_into':
        tgt = byid[d['into']]
        tgt['evidence_sources'] += m['evidence_sources']
        tgt.setdefault('merged_statements', []).append(m['evidence_statement'])
        tgt['series_count'] = len({s['examiner_report_year'] for s in tgt['evidence_sources']})
        continue
    for side_key, src_key in (('confused_a', 'a'), ('confused_b', 'b')):
        m[side_key] = d[src_key]
    m['proposed_sub_topic'] = d['sub_topic']
    m['mapping_method'] = 'read on review'
    m['discriminating_test'] = d['test']
    m['needs_teacher_input'] = bool(d.get('needs_teacher_input'))
    if d.get('teacher_note'):
        m['teacher_note'] = d['teacher_note']
    for k_ in ('resolution', 'authoring_constraint'):
        if d.get(k_):
            m[k_] = d[k_]
    m['curation'] = 'keep on review'
    m['_objective_starts'] = d['objective_starts']
    reviewed.append(m)
    for k, s in enumerate(d.get('split_out', []), start=1):
        extra.append({**{x: m[x] for x in ('class', 'evidence_statement', 'evidence_sources',
                                             'series_count', 'curated')},
                      'misconception_id': None, 'split_from': i,
                      'proposed_sub_topic': s['sub_topic'], 'mapping_method': 'read on review',
                      'confused_a': s['a'], 'confused_b': s['b'],
                      'discriminating_test': s['test'], 'needs_teacher_input': False,
                      '_objective_starts': s['objective_starts'],
                      'curation': 'keep on review (split from a statement naming two confusions)'})
# IDs stay stable across reviews; split-outs take the next free numbers
nxt = max(int(i.rsplit('-', 1)[1]) for i in byid) + 1
for e in extra:
    e['misconception_id'] = f"MISCON-6116-{nxt:03d}"; nxt += 1
merged = sorted(reviewed + extra, key=lambda m: m['misconception_id'])

# Attach each entry to the one objective it discriminates. build/make_work_order.py
# (slot_plan.misconception_slots: one_per_entry) reads `entries` with topic_id,
# objective_id, entry_id, n and a.
reg = [o for o in json.load(open(f'{WS}/curriculum/objective_registry.json'))['objectives']
       if o.get('parent_id')]
for m in merged:
    pre = m.pop('_objective_starts')
    hits = [o for o in reg if o['syllabus_text'].startswith(pre)]
    if len(hits) != 1:
        raise SystemExit('%s: objective prefix matched %d objectives' % (m['misconception_id'], len(hits)))
    m['objective_id'], m['topic_id'] = hits[0]['objective_id'], hits[0]['topic_id']
entries = [{'entry_id': m['misconception_id'], 'topic_id': m['topic_id'],
            'objective_id': m['objective_id'], 'n': len(m['evidence_sources']),
            'a': '%s vs %s' % (m['confused_a'], m['confused_b']),
            'authoring_constraint': m.get('authoring_constraint')} for m in merged]

out = {
    'provenance': 'corpus',
    'curated': True,
    'curation_date': '2026-10-18',
    'review': 'planning/misconception_review.json (provenance: judgement)',
    'rule': ('Every entry cites at least one examiner statement. None is invented. Entries '
             'evidenced in more than one series carry every citation and are stronger for it. '
             'Where the examiner did not name both sides of the confusion, discriminating_test '
             'is null and needs_teacher_input is true: the distinction is not invented here.'),
    'counts': {'raw': len(raw), 'dropped': len(dropped),
               'routed_to_command_word_register': len(cwmiss), 'kept_after_merge': len(merged),
               'multi_series': sum(1 for m in merged if m['series_count'] > 1),
               'with_discriminating_test': sum(1 for m in merged if m['discriminating_test']),
               'needing_teacher_input': sum(1 for m in merged if m['needs_teacher_input'])},
    'misconceptions': merged,
    'entries': entries,
    'command_word_misses': [{'statement': c['evidence_statement'][:300],
                             'source': c['evidence_source'],
                             'proposed_sub_topic': c['proposed_sub_topic'],
                             'note': 'candidates answered a different question than the one asked'}
                            for c in cwmiss],
    'dropped': [{'statement': d['evidence_statement'][:160], 'reason': d['curation']} for d in dropped],
}
json.dump(out, open(f'{WS}/curriculum/misconceptions.json', 'w'), indent=2, ensure_ascii=False)
c = out['counts']
print(f"raw {c['raw']} -> dropped {c['dropped']} -> command-word register {c['routed_to_command_word_register']} "
      f"-> kept {c['kept_after_merge']} misconceptions")
print(f"  evidenced in more than one series : {c['multi_series']}")
print(f"  with a discriminating test written: {c['with_discriminating_test']}")
print(f"  needing teacher input             : {c['needing_teacher_input']}")
print("\nmulti-series confusions (the strongest evidence):")
for m in merged:
    if m['series_count'] > 1:
        print(f"   x{m['series_count']}  {m.get('confused_a')} / {m.get('confused_b')}")
