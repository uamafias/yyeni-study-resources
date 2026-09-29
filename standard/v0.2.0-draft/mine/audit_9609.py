# -*- coding: utf-8 -*-
"""Does the already-published subject survive the gate that caught the 0450 errors?

9609 was planned before the provenance rule existed and its notes and flashcards
are already published. So the question is not "is it documented the new way" but
"is it WRONG in the two ways 0450 was wrong": AO weights that do not match the
syllabus, and a command-word list that is not the syllabus's.
"""
import json, os, re, collections
REPO = os.path.expanduser('~/mnt/YYeni Study Resources')
WS = os.path.join(REPO, 'work/cie-9609-as-2026-2028')
fails, notes = [], []

def ck(c, m):
    print(('  PASS  ' if c else '  FAIL  ') + m)
    if not c:
        fails.append(m)

def nt(m):
    print('  NOTE  ' + m)
    notes.append(m)

F = json.load(open(os.path.join(WS, 'curriculum', 'syllabus-facts.json')))
FW = json.load(open(os.path.join(WS, 'curriculum', 'assessment-framework.json')))

print('\n=== 9609: the two failure modes ===')

# 1. AO weights. The AS/A Level syllabus states them per QUALIFICATION ROUTE, so
#    an AS-only workspace must use the AS column, not the A Level one and not an
#    average of the two.
AS_STATED = {'AO1': 30, 'AO2': 30, 'AO3': 20, 'AO4': 20}
A_STATED = {'AO1': 25, 'AO2': 25, 'AO3': 25, 'AO4': 25}
have = {a['code']: a['qualification_weight_percent'] for a in FW['assessment_objectives']}
ck(have == AS_STATED,
   'qualification AO weights are the syllabus\'s AS Level column %s (framework has %s)'
   % (AS_STATED, have))
if have == A_STATED:
    nt('the framework is using the A Level column, which is the wrong route')

# 2. Per-paper splits, against the component weighting table read off the PDF.
fact_p = {p['paper']: p for p in F['papers']}
drift = []
for p in FW.get('papers', []):
    num = str(p.get('paper') or p.get('paper_id', '')).replace('P', '')
    f_ = fact_p.get(num)
    if not f_:
        continue
    if p.get('marks') and p['marks'] != f_['marks']:
        drift.append('P%s marks %s != %s' % (num, p['marks'], f_['marks']))
    split = p.get('ao_split') or {}
    if split and split != f_['ao_split']:
        drift.append('P%s AO split %s != syllabus %s' % (num, split, f_['ao_split']))
ck(not drift, 'each paper matches the syllabus component table%s'
   % ((' — ' + '; '.join(drift)) if drift else ''))

# the derived mark budget is the place a wrong split would actually show
bud = FW['ao_mark_budget']['per_paper']
for pid, marks in (('P1', 40), ('P2', 60)):
    f_ = fact_p[pid[-1]]
    want = {a: round(marks * v / 100.0) for a, v in f_['ao_split'].items()}
    ck(bud.get(pid) == want,
       '%s mark budget %s equals the syllabus split applied to %d marks %s'
       % (pid, bud.get(pid), marks, want))

# 3. The command-word table.
fact_cw = {c['word'] for c in F['command_words']}
fw_cw = {c['word'] for c in FW['command_words']}
ck(fw_cw == fact_cw,
   'the framework\'s command words are exactly the syllabus table\'s %d (%s)'
   % (len(fact_cw), 'match' if fw_cw == fact_cw
      else 'framework-only %s, syllabus-only %s'
           % (sorted(fw_cw - fact_cw), sorted(fact_cw - fw_cw))))

# 4. Is every "not used at AS" claim actually evidenced, or was it asserted?
unevidenced = []
for c in FW['command_words']:
    if c.get('exact_mark_tariff') is None:
        note = c.get('evidence_note') or ''
        if not re.search(r'(zero|\d+)\s+\w*\s*(occurrence|paper)', note, re.I):
            unevidenced.append(c['word'])
ck(not unevidenced,
   'every excluded command word cites a count, not an assertion (%s)'
   % (', '.join(unevidenced) if unevidenced else 'all cite counts'))

print('\n=== what 9609 lacks against the current standard (enrichment, not error) ===')
for fn, what in (('answer-shapes.json', 'the answer architecture behind each tariff'),
                 ('misconceptions.json', 'examiner-evidenced confusions per objective'),
                 ('syllabus-exclusions.json', 'the board\'s own stated content limits')):
    p = os.path.join(WS, 'curriculum', fn)
    (print('  present  %s' % fn) if os.path.exists(p)
     else nt('missing curriculum/%s — %s' % (fn, what)))
has_bloom = 'blooms_taxonomy' in FW
(print('  present  blooms_taxonomy') if has_bloom
 else nt('the framework carries no Bloom\'s taxonomy, so published items have no level'))

# how much is already published, and does it carry a Bloom level?
pub = os.path.join(REPO, 'publish/cie-9609-as-2026-2028')
if os.path.isdir(pub):
    import glob
    cards = glob.glob(os.path.join(pub, 'flashcards', '*.json'))
    n, withb = 0, 0
    for f in cards:
        d = json.load(open(f))
        items = d if isinstance(d, list) else (d.get('items') or d.get('flashcards') or [])
        for it in items:
            n += 1
            if it.get('blooms_level'):
                withb += 1
    print('\n  published: %d flashcard files, %d items, %d carrying a Bloom level'
          % (len(cards), n, withb))

print('\n' + '=' * 66)
print('%d FAIL, %d gaps' % (len(fails), len(notes)))
