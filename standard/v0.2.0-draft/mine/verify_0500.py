# -*- coding: utf-8 -*-
"""Independent audit of the 0500 plan. Re-derives what it can from the sources; trusts nothing the builder wrote.

    python3 verify_0500.py
"""
import glob, json, os, re, subprocess, sys
HOME = os.path.expanduser('~')
REPO = os.path.join(HOME, 'mnt', 'YYeni Study Resources')
MINE = os.path.join(HOME, 'mine')
WS = os.environ.get('WS0500') or os.path.join(REPO, 'work', 'cie-0500-igcse-2024-2026')
STD = os.path.join(REPO, 'standard', 'v0.2.0-draft')
J = lambda rel: json.load(open(os.path.join(WS, rel)))
FAIL, OK = [], []


def check(name, cond, detail=''):
    (OK if cond else FAIL).append(name + ('' if cond else ': ' + detail))


facts = J('curriculum/syllabus-facts.json')
pdf = os.path.join(REPO, facts['source_document'])
pages = subprocess.run(['pdftotext', '-layout', pdf, '-'], capture_output=True, text=True, check=True).stdout.split('\f')


def norm(s):
    for a, b in (('–', '-'), ('—', '-'), ('’', "'"), ('‘', "'")):
        s = s.replace(a, b)
    s = re.sub(r'\s*/\s*', '/', s)
    return re.sub(r'\s+', ' ', s).strip().lower().rstrip('.')


reg = J('curriculum/objective_registry.json')
bad = [o['objective_id'] for o in reg['objectives'] if norm(o['syllabus_text']) not in norm(pages[o['syllabus_page'] - 1])]
check('every objective (and container) is verbatim on the page it cites (%d)' % len(reg['objectives']), not bad, ', '.join(bad))

# command words: exactly the syllabus table, page 30
p30 = norm(pages[29])
fw = J('curriculum/assessment-framework.json')
words = [c['word'] for c in fw['command_words']]
check('command words are exactly the four on page 30', sorted(words) == ['Describe', 'Explain', 'Give', 'Identify']
      and all(norm(c['word'] + ' ' + c['meaning']) in p30 for c in fw['command_words']), str(words))
check('AO weights 50/50 and per-paper 80/20, 20/80 as page 10 states',
      fw['per_component_ao_percent']['P1']['AO1'] == 80 and fw['per_component_ao_percent']['P2']['AO2'] == 80
      and '80 20 0' in re.sub(r'\s+', ' ', pages[9]))
check('W5 removal cited to page 35 and present there', 'has been removed from paper 1 reading only' in norm(pages[34]))

# item schema accepts every field a slot tells the author to carry (the C-00 class of defect)
from jsonschema import Draft202012Validator
V = Draft202012Validator(json.load(open(os.path.join(STD, 'schemas', 'learning_items.schema.json'))))
SUBS_BY_OBJ = {o['objective_id']: set(o.get('sub_objectives') or []) for o in reg['objectives']}
BLOOM = fw['blooms_taxonomy']['by_subtype']
TASK_SUBS = {}
for k, t in J('curriculum/answer-shapes.json')['0500']['tasks'].items():
    TASK_SUBS[k] = set(t.get('sub_objectives') or []) | {s for p in (t.get('split') or {}).values() for s in p['sub_objectives']}
TARIFFS = {'1.1': {1, 2, 3}, '1.2': {15}, '1.3': {1}, '1.4': {3, 15}, '1.5': {25}, '2.1': {15}, '2.2': {40},
           '2.3': {40}, '2.4': {40}, '2.5': {None}}
schema_bad, label_bad, tariff_bad, text_bad = [], [], [], []
LEN = {'1.1': (700, 750), '1.2': (700, 750), '1.3': (500, 650), '1.4': (500, 650), '1.5': (500, 650), '2.1': (650, 750), '2.2': (650, 750)}
n_slots = 0
for wo_p in sorted(glob.glob(os.path.join(WS, 'topics', '*', 'work_order.json'))):
    wo = json.load(open(wo_p)); tid = wo['topic_id']
    for s in wo['item_slots'] + wo['performance_tasks']:
        n_slots += 1
        flash = 'subtype' in s
        item = {'item_id': s['slot'], 'objective_ids': [s['objective_id']] if flash else s['objective_ids'],
                'claim_ids': ['CLM-X'], 'item_type': 'flashcard' if flash else s['item_type'],
                'subtype': s.get('subtype'), 'assessment_objectives': s['assessment_objectives'],
                'sub_objectives': s['sub_objectives'], 'blooms_level': s['blooms_level'],
                'command_word': s['command_word'], 'mark_tariff': s['mark_tariff'], 'difficulty': s['difficulty'],
                'prompt': 'x', 'canonical_answer': 'x', 'marking_guidance': ['x'],
                'context': dict({'sector': None, 'business_size': None, 'ownership': None, 'situation': None, 'facts': []},
                                **({'text_id': s['text_id']} if s.get('text_id') else {})),
                'prerequisite_item_ids': [], 'core_status': 'core', 'intentional_duplicate_group': None,
                'provenance': 'x', 'qa_status': 'review_required', 'claims_seen': {'CLM-X': 1}, 'authored_hash': 'x'}
        errs = list(V.iter_errors({'dataset_id': 'x', 'topic_id': tid, 'items': [item]}))
        if errs:
            schema_bad.append('%s: %s' % (s['slot'], errs[0].message[:80]))
        aos = sorted({'AO1' if x.startswith('R') else 'AO2' for x in s['sub_objectives']})
        if aos != sorted(s['assessment_objectives']):
            label_bad.append('%s AO %s vs skills %s' % (s['slot'], s['assessment_objectives'], s['sub_objectives']))
        if s['command_word'] not in (None, 'Identify', 'Explain', 'Give', 'Describe'):
            label_bad.append('%s command word %s' % (s['slot'], s['command_word']))
        if flash:
            if BLOOM[s['subtype']] != s['blooms_level']:
                label_bad.append('%s Bloom %s vs subtype %s' % (s['slot'], s['blooms_level'], s['subtype']))
            if not set(s['sub_objectives']) <= SUBS_BY_OBJ[s['objective_id']]:
                label_bad.append('%s skills outside its objective' % s['slot'])
        else:
            allowed = set().union(*[TASK_SUBS[m] for m in s['models']])
            if not set(s['sub_objectives']) <= allowed:
                label_bad.append('%s skills %s outside its task %s' % (s['slot'], s['sub_objectives'], s['models']))
            if s['mark_tariff'] not in TARIFFS[tid]:
                tariff_bad.append('%s tariff %s' % (s['slot'], s['mark_tariff']))
    for x in wo['practice_texts']:
        if (x['words_min'], x['words_max']) != LEN[tid] or not x['used_by']:
            text_bad.append(x['text_id'])
check('a synthetic item built from every slot validates against the item schema (%d slots)' % n_slots, not schema_bad, '; '.join(schema_bad[:4]))
check('every slot: AO matches its skills, Bloom matches its subtype, skills inside its objective or task', not label_bad, '; '.join(label_bad[:4]))
check('every performance tariff is one the syllabus task carries', not tariff_bad, '; '.join(tariff_bad[:4]))
check('every practice text has the syllabus length for its task and is used', not text_bad, ', '.join(text_bad))

# misconceptions and coverage
mc = J('curriculum/misconceptions.json')['entries']
slots = [s for p in glob.glob(os.path.join(WS, 'topics', '*', 'work_order.json')) for s in json.load(open(p))['item_slots']]
perf = [s for p in glob.glob(os.path.join(WS, 'topics', '*', 'work_order.json')) for s in json.load(open(p))['performance_tasks']]
miss = [m['misconception_id'] for m in mc if not any(s.get('misconception_id') == m['misconception_id'] and s['objective_id'] == m['objective_id'] for s in slots)]
check('every misconception has a MISCON slot on its objective (%d)' % len(mc), not miss, ', '.join(miss))
objs = [o['objective_id'] for o in reg['objectives'] if o.get('parent_id')]
nof = [o for o in objs if not any(s['objective_id'] == o for s in slots)]
nop = [o for o in objs if not any(o in s['objective_ids'] for s in perf)]
check('every objective has a flashcard', not nof, ', '.join(nof))
check('every objective is exercised by a performance task', not nop, ', '.join(nop))

# contracts: scannable exclusions only
ct_bad = [p for p in glob.glob(os.path.join(WS, 'topics', '*', 'contract.json'))
          if any(len(x.split()) > 3 or '[' in x for x in json.load(open(p))['depth_constraints']['excluded_constructs'])]
check('contract exclusions are scannable terms, not tagged sentences', not ct_bad, ', '.join(ct_bad))

# documents: paths exist, no other subject named
docs = {n: open(os.path.join(WS, n)).read() for n in ('PLAN-0500-igcse-first-language-english.md', 'HANDOVER-0500-igcse-first-language-english.md')}
paths = set()
for t in docs.values():
    for m in re.findall(r'`((?:work|standard|operations)/[^`<> ]+|AGENTS\.md)`', t):
        paths.add(m)
missing = [p for p in sorted(paths) if not os.path.exists(os.path.join(REPO, p))]
check('every path the plan and handover name exists (%d)' % len(paths), not missing, ', '.join(missing))
other = [c for c in ('0450', '0455', '9609', '9709', '9618', '9702', '0460', '9093') if any(c in t for t in docs.values())]
check('plan and handover name no other syllabus code', not other, ', '.join(other))

# derivation: no 8-word run shared with Cambridge material that is not also in the syllabus
def grams(text, n=8):
    w = re.findall(r"[a-z0-9']+", norm(text))
    return {hash(' '.join(w[i:i + n])) for i in range(len(w) - n + 1)}
syl = set().union(*[grams(p) for p in pages])
corpus = set()
for f in glob.glob(os.path.join(MINE, '0500', '0500_*_*.txt')):
    corpus |= grams(open(f, errors='ignore').read())
corpus -= syl
mine = {}
for rel in ['PLAN-0500-igcse-first-language-english.md', 'HANDOVER-0500-igcse-first-language-english.md',
            'curriculum/answer-shapes.json', 'curriculum/misconceptions.json', 'curriculum/glossary.json',
            'exemplar/texts/TXT-0500-1.3-EX.md', 'exemplar/learning-items/topic_1.3_items.json'] + \
           [os.path.relpath(p, WS) for p in glob.glob(os.path.join(WS, 'topics', '*', 'work_order.json'))] + \
           [os.path.relpath(p, WS) for p in glob.glob(os.path.join(WS, 'exemplar', 'content-units', '*.json'))]:
    if not os.path.exists(os.path.join(WS, rel)):
        continue
    txt = open(os.path.join(WS, rel)).read()
    hits = grams(txt) & corpus
    if hits:
        mine[rel] = len(hits)
check('no 8-word run shared with the 0500 papers, inserts, mark schemes or reports beyond the syllabus itself',
      not mine, json.dumps(mine))

# after authoring: every item carries its slot's labels, or records why not; authored text shares no 8-word run with the corpus
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
            for k in ('blooms_level', 'sub_objectives', 'command_word', 'mark_tariff', 'assessment_objectives'):
                if it.get(k) != s.get(k) and it['item_id'] not in noted:
                    drift.append('%s.%s' % (it['item_id'], k))
            if s.get('text_id') and (it.get('context') or {}).get('text_id') != s['text_id']:
                drift.append('%s.text_id' % it['item_id'])
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
