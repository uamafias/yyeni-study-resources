# -*- coding: utf-8 -*-
"""Independent audit of the 9093 AS plan. Re-derives what it can from the sources; trusts nothing the builder wrote.

    python3 verify_9093.py
"""
import collections, glob, json, os, re, subprocess, sys
HOME = os.path.expanduser('~')
REPO = os.path.join(HOME, 'mnt', 'YYeni Study Resources')
MINE = os.path.join(HOME, 'mine')
WS = os.environ.get('WS9093') or os.path.join(REPO, 'work', 'cie-9093-as-2024-2026')
STD = os.path.join(REPO, 'standard', 'v0.2.0-draft')
J = lambda rel: json.load(open(os.path.join(WS, rel)))
FAIL, OK = [], []


def check(name, cond, detail=''):
    (OK if cond else FAIL).append(name + ('' if cond else ': ' + detail))


facts = J('curriculum/syllabus-facts.json')
pdf = os.path.join(REPO, facts['source_document'])
lay = subprocess.run(['pdftotext', '-layout', pdf, '-'], capture_output=True, text=True, check=True).stdout.split('\f')
raw = subprocess.run(['pdftotext', pdf, '-'], capture_output=True, text=True, check=True).stdout.split('\f')


def norm(s):
    for a, b in (('–', '-'), ('—', '-'), ('’', "'"), ('‘', "'"), ('“', '"'), ('”', '"')):
        s = s.replace(a, b)
    s = re.sub(r'\s*/\s*', '/', s)
    return re.sub(r'\s+', ' ', s).strip().lower().rstrip('.')


on_page = lambda t, p: norm(t) in norm(lay[p - 1]) or norm(t) in norm(raw[p - 1])
reg = J('curriculum/objective_registry.json')
bad = [o['objective_id'] for o in reg['objectives'] if not on_page(o['syllabus_text'], o['syllabus_page'])]
check('every objective (and container) is verbatim on the page it cites (%d)' % len(reg['objectives']), not bad, ', '.join(bad))

fw = J('curriculum/assessment-framework.json')
p23 = norm(raw[22])
words = sorted(c['word'] for c in fw['command_words'])
check('command words are exactly the three on page 23', words == ['Analyse', 'Compare', 'Discuss']
      and all(norm(c['word']) in p23 and norm(c['meaning']) in p23 for c in fw['command_words']), str(words))
check('only Compare and Analyse are in use; Discuss is listed-not-observed',
      sorted(fw['command_words_in_use']) == ['Analyse', 'Compare'] and fw['command_words_listed_but_never_used'] == ['Discuss'])
p11 = re.sub(r'\s+', ' ', lay[10])
check('AS weights 15/45/40 and per-paper splits as page 11 states',
      all(x in p11 for x in ('AO1 15 20', 'AO2 45 30', 'AO3 40 20', 'AO1 30 0 10 40', 'AO2 10 80 10 20', 'AO3 60 20 0 0'))
      and {a['code']: a['qualification_weight_percent'] for a in fw['assessment_objectives']} == {'AO1': 15, 'AO2': 45, 'AO3': 40, 'AO4': 0, 'AO5': 0}
      and fw['per_component_ao_percent']['P1']['AO3'] == 60 and fw['per_component_ao_percent']['P2']['AO2'] == 80)
check('the paper facts are on their pages (marks, times, lengths)',
      all(norm(x) in norm(lay[p - 1]) for x, p in (('Written paper, 2 hours 15 minutes, 50 marks', 19), ('write a directed response of 150–200 words', 19),
                                                   ('read a text of approximately 550–750 words', 20), ('no more than 400 words', 20),
                                                   ('produce a continuous piece of writing of 600–900 words', 21), ('Written paper, 2 hours, 50 marks', 20))))

# item schema accepts every field a slot tells the author to carry
from jsonschema import Draft202012Validator
V = Draft202012Validator(json.load(open(os.path.join(STD, 'schemas', 'learning_items.schema.json'))))
AOS_BY_OBJ = {o['objective_id']: set(o['assessment_objectives']) for o in reg['objectives']}
PAPERS_BY_OBJ = {o['objective_id']: o.get('papers') or [] for o in reg['objectives']}
BLOOM = fw['blooms_taxonomy']['by_subtype']
TARIFFS = {'1.4': {10, 15, None}, '1.5': {25}, '2.1': {15, 10}, '2.3': {25}, '2.4': {25}, '2.5': {25}}
schema_bad, label_bad, tariff_bad, text_bad, pair_bad = [], [], [], [], []
n_slots = 0
aom = collections.Counter()
wos = {}
for wo_p in sorted(glob.glob(os.path.join(WS, 'topics', '*', 'work_order.json'))):
    wo = json.load(open(wo_p)); tid = wo['topic_id']; wos[tid] = wo
    ids = {s['slot']: s for s in wo['performance_tasks']}
    for s in wo['item_slots'] + wo['performance_tasks']:
        n_slots += 1
        flash = 'subtype' in s
        item = {'item_id': s['slot'], 'objective_ids': [s['objective_id']] if flash else s['objective_ids'],
                'claim_ids': ['CLM-X'], 'item_type': 'flashcard' if flash else s['item_type'],
                'subtype': s.get('subtype'), 'assessment_objectives': s['assessment_objectives'],
                'blooms_level': s['blooms_level'], 'command_word': s['command_word'], 'mark_tariff': s['mark_tariff'],
                'difficulty': s['difficulty'], 'prompt': 'x', 'canonical_answer': 'x', 'marking_guidance': ['x'],
                'context': dict({'sector': None, 'business_size': None, 'ownership': None, 'situation': None, 'facts': []},
                                **({'text_id': s['text_id']} if s.get('text_id') else {})),
                'prerequisite_item_ids': [s['written_about']] if s.get('written_about') else [], 'core_status': 'core',
                'intentional_duplicate_group': None, 'provenance': 'x', 'qa_status': 'review_required',
                'claims_seen': {'CLM-X': 1}, 'authored_hash': 'x'}
        errs = list(V.iter_errors({'dataset_id': 'x', 'topic_id': tid, 'items': [item]}))
        if errs:
            schema_bad.append('%s: %s' % (s['slot'], errs[0].message[:80]))
        if s['command_word'] not in (None, 'Analyse', 'Compare'):
            label_bad.append('%s command word %s' % (s['slot'], s['command_word']))
        if flash:
            if BLOOM[s['subtype']] != s['blooms_level']:
                label_bad.append('%s Bloom %s vs subtype %s' % (s['slot'], s['blooms_level'], s['subtype']))
            if set(s['assessment_objectives']) != AOS_BY_OBJ[s['objective_id']]:
                label_bad.append('%s AOs differ from its objective' % s['slot'])
            if s['command_word'] or s['mark_tariff']:
                label_bad.append('%s flashcard carries a command word or tariff' % s['slot'])
        else:
            if not set(s['assessment_objectives']) <= set().union(*[AOS_BY_OBJ[o] for o in s['objective_ids']]):
                label_bad.append('%s AOs outside its objectives' % s['slot'])
            if s['ao_marks'] and (sum(s['ao_marks'].values()) != s['mark_tariff'] or set(s['ao_marks']) != set(s['assessment_objectives'])):
                label_bad.append('%s ao_marks do not match its tariff and AOs' % s['slot'])
            if s['mark_tariff'] is not None and s['mark_tariff'] not in TARIFFS.get(tid, set()):
                tariff_bad.append('%s tariff %s' % (s['slot'], s['mark_tariff']))
            if s['mark_tariff'] == 15 and tid == '1.4' and s['command_word'] != 'Compare':
                label_bad.append('%s comparison without Compare' % s['slot'])
            if tid == '1.5' and s['command_word'] != 'Analyse':
                label_bad.append('%s text analysis without Analyse' % s['slot'])
            for a, v in s['ao_marks'].items():
                aom[a] += v
            if s.get('written_about'):
                first = ids.get(s['written_about'])
                if not first or first['item_type'] != 'writing_task' or first.get('text_id') != s.get('text_id'):
                    pair_bad.append(s['slot'])
    for x in wo['practice_texts']:
        if (x['words_min'], x['words_max']) != (550, 750) or not x['used_by']:
            text_bad.append(x['text_id'])
check('a synthetic item built from every slot validates against the item schema (%d slots)' % n_slots, not schema_bad, '; '.join(schema_bad[:4]))
check('every slot: AOs match its objective, Bloom matches its subtype, command words only where the papers use them', not label_bad, '; '.join(label_bad[:4]))
check('every performance tariff is one the paper task carries', not tariff_bad, '; '.join(tariff_bad[:4]))
check('every practice text has the syllabus length (550-750) and is used', not text_bad, ', '.join(text_bad))
check('every part (b) is written about a part (a) on the same text', not pair_bad, ', '.join(pair_bad))
tot = sum(aom.values())
share = {a: round(100 * aom[a] / tot) for a in ('AO1', 'AO2', 'AO3')}
gap = max(abs(share[a] - w) for a, w in (('AO1', 15), ('AO2', 45), ('AO3', 40)))
check('practice marks by AO match the AS weights within 5 points (%s, gap %d)' % (share, gap), gap <= 5)
cov = open(os.path.join(WS, 'curriculum', 'ao_coverage.md')).read()
check('ao_coverage.md states the same gap', 'largest gap %d points' % gap in cov)

mc = J('curriculum/misconceptions.json')['entries']
slots = [s for w in wos.values() for s in w['item_slots']]
perf = [s for w in wos.values() for s in w['performance_tasks']]
miss = [m['misconception_id'] for m in mc if not any(s.get('misconception_id') == m['misconception_id'] and s['objective_id'] == m['objective_id'] for s in slots)]
check('every misconception has a MISCON slot on its objective (%d)' % len(mc), not miss, ', '.join(miss))
sys.path.insert(0, os.path.join(MINE, 'gen'))
from er9093 import load
from mtest9093 import CUE
E = load()
noev = []
for m in mc:
    r = re.compile(m['evidence_pattern'], re.I)
    if not any(e['task'] in m['report_tasks'] and (e['error'] or CUE.search(e['sentence'])) and r.search(e['sentence']) for e in E):
        noev.append(m['misconception_id'])
check('every misconception is re-found in the examiner reports by its own pattern', not noev, ', '.join(noev))
objs = [o['objective_id'] for o in reg['objectives'] if o.get('parent_id')]
nof = [o for o in objs if not any(s['objective_id'] == o for s in slots)]
nop = [o for o in objs if not any(o in s['objective_ids'] for s in perf)]
check('every objective has a flashcard', not nof, ', '.join(nof))
check('every objective is exercised by a performance task', not nop, ', '.join(nop))
p2a1 = [o['objective_id'] for o in reg['objectives'] if o.get('parent_id') and o['papers'] == ['2'] and 'AO1' in o['assessment_objectives']]
check('no Paper 2 objective claims AO1 (Paper 2 assesses none)', not p2a1, ', '.join(p2a1))

ct_bad = [p for p in glob.glob(os.path.join(WS, 'topics', '*', 'contract.json'))
          if any(len(x.split()) > 4 or '[' in x for x in json.load(open(p))['depth_constraints']['excluded_constructs'])]
check('contract exclusions are scannable terms, not tagged sentences', not ct_bad, ', '.join(ct_bad))

docs = {n: open(os.path.join(WS, n)).read() for n in ('PLAN-9093-as-english-language.md', 'HANDOVER-9093-as-english-language.md')}
paths = set()
for t in docs.values():
    for m in re.findall(r'`((?:work|standard|operations)/[^`<> ]+|AGENTS\.md)`', t):
        paths.add(m)
missing = [p for p in sorted(paths) if not os.path.exists(os.path.join(REPO, p))]
check('every path the plan and handover name exists (%d)' % len(paths), not missing, ', '.join(missing))
other = [c for c in ('0450', '0455', '0500', '9609', '9709', '9618', '9702', '0460') if any(c in t for t in docs.values())]
check('plan and handover name no other syllabus code', not other, ', '.join(other))
check('the handover never tells the author to use Discuss', not re.search(r'use `?Discuss`? (where|in)', docs['HANDOVER-9093-as-english-language.md']))


def grams(text, n=8):
    w = re.findall(r"[a-z0-9']+", norm(text))
    return {hash(' '.join(w[i:i + n])) for i in range(len(w) - n + 1)}


syl = set().union(*[grams(p) for p in lay + raw])
corpus = set()
for f in glob.glob(os.path.join(MINE, '9093', '9093_*_*.txt')):
    if re.search(r'_(qp|ms)_[12]\d|_er\.txt', f):
        corpus |= grams(open(f, errors='ignore').read())
corpus -= syl
mine = {}
for rel in ['PLAN-9093-as-english-language.md', 'HANDOVER-9093-as-english-language.md', 'subject-profile.yaml',
            'curriculum/answer-shapes.json', 'curriculum/misconceptions.json', 'curriculum/glossary.json'] + \
           [os.path.relpath(p, WS) for p in glob.glob(os.path.join(WS, 'topics', '*', 'work_order.json'))] + \
           [os.path.relpath(p, WS) for p in glob.glob(os.path.join(WS, 'exemplar', '*', '*'))]:
    if not os.path.isfile(os.path.join(WS, rel)):
        continue
    hits = grams(open(os.path.join(WS, rel)).read()) & corpus
    if hits:
        mine[rel] = len(hits)
check('no 8-word run shared with the 9093 AS papers, schemes or reports beyond the syllabus itself', not mine, json.dumps(mine))

authored = sorted(glob.glob(os.path.join(WS, 'topics', '*', 'learning-items', '*.json')))
if authored:
    drift, undeclared, n_items = [], [], 0
    for f in authored:
        tdir = os.path.dirname(os.path.dirname(f))
        wo = json.load(open(os.path.join(tdir, 'work_order.json')))
        slot = {s['slot']: s for s in wo['item_slots'] + wo['performance_tasks']}
        notes_p = os.path.join(tdir, 'authoring_notes.json')
        noted = json.dumps(json.load(open(notes_p))) if os.path.exists(notes_p) else ''
        for it in json.load(open(f))['items']:
            n_items += 1
            s = slot.get(it['item_id'])
            if not s:
                if it['item_id'] not in noted:
                    undeclared.append(it['item_id'])
                continue
            for k in ('blooms_level', 'command_word', 'mark_tariff', 'assessment_objectives'):
                if it.get(k) != s.get(k) and it['item_id'] not in noted:
                    drift.append('%s.%s' % (it['item_id'], k))
            if s.get('text_id') and (it.get('context') or {}).get('text_id') != s['text_id']:
                drift.append('%s.text_id' % it['item_id'])
            if s.get('written_about') and s['written_about'] not in (it.get('prerequisite_item_ids') or []):
                drift.append('%s.prerequisite_item_ids' % it['item_id'])
            if re.search(r'\bDiscuss\b', it.get('prompt', '')):
                drift.append('%s.Discuss' % it['item_id'])
    check('authored items carry their slot labels or record the change (%d items)' % n_items, not drift, ', '.join(drift[:8]))
    check('no authored item lacks a slot without a recorded reason', not undeclared, ', '.join(undeclared[:8]))
    hits = {}
    for f in glob.glob(os.path.join(WS, 'topics', '*', 'texts', '*.md')) + authored + \
            glob.glob(os.path.join(WS, 'topics', '*', 'content-units', '*.json')):
        h = grams(open(f).read()) & corpus
        if h:
            hits[os.path.relpath(f, WS)] = len(h)
    check('authored texts, items and notes share no 8-word run with the corpus', not hits, json.dumps(hits)[:400])

for o in OK:
    print('PASS ', o)
for f in FAIL:
    print('FAIL ', f)
print('\n%d pass, %d fail' % (len(OK), len(FAIL)))
sys.exit(1 if FAIL else 0)
