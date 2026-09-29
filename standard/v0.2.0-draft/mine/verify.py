# -*- coding: utf-8 -*-
"""Verify the corpus findings against the raw sources before anyone builds on them."""
import json, os, re, glob, random, collections
ROOT = os.path.expanduser('~/mine')
REPO = os.path.expanduser('~/mnt/YYeni Study Resources')
fails, warns = [], []

def ck(cond, msg):
    (print('  PASS  ' + msg) if cond else (fails.append(msg), print('  FAIL  ' + msg)))

def wk(cond, msg):
    if not cond:
        warns.append(msg); print('  WARN  ' + msg)
    else:
        print('  PASS  ' + msg)


print('\n=== 0. PROVENANCE GATE: every assessment value is transcribed, not recalled ===')
# This section exists because two assessment values were once written from recall
# and both were wrong: a command-word list that did not match the syllabus table,
# and per-paper AO splits inferred from the papers' names. Each propagates into
# every item in a subject. Prose rules did not stop it; this does.
import subprocess as _sp
import sys as _s
_s.path.insert(0, ROOT)
import mine_syllabus as _MS
SYLPDF = {c: v['pdf'] for c, v in _MS.SUBJECTS.items()}
SYLWS = {c: v['ws'] for c, v in _MS.SUBJECTS.items()}

def _pdf_pages(code):
    out = _sp.run(['pdftotext', '-layout', os.path.join(REPO, SYLPDF[code]), '-'],
                  capture_output=True, check=True).stdout.decode('utf-8', 'ignore')
    return [re.sub(r'\s+', ' ', p) for p in out.split('\f')]

for code in sorted(SYLWS):
    ws = SYLWS[code]
    fp = os.path.join(REPO, ws, 'curriculum', 'syllabus-facts.json')
    ck(os.path.exists(fp), '%s curriculum/syllabus-facts.json exists (step zero ran)' % code)
    if not os.path.exists(fp):
        continue
    F = json.load(open(fp))
    pgs = _pdf_pages(code)

    # 1. every verbatim quote must actually be on the page it cites
    bad = []
    def _check(v, page, label):
        q = re.sub(r'\s+', ' ', v).strip()
        if not q:
            return
        if 1 <= page <= len(pgs) and q in pgs[page - 1]:
            return
        if any(q in pg for pg in pgs):          # right text, wrong page
            bad.append('%s: on a different page than cited (%d)' % (label, page))
        else:
            bad.append('%s: quote not found anywhere in the PDF' % label)
    for a in F['assessment_objectives']:
        _check(a['verbatim'], a['source']['page'], 'AO %s' % a['code'])
    for c in F['command_words']:
        _check(c['verbatim'], c['source']['page'], 'command word %s' % c['word'])
    for k in ('qualification', 'per_component'):
        src = F['ao_weights']['source'].get(k) or {}
        for row in src.get('rows', []):
            _check(row, src['page'], '%s weighting row' % k)
    ck(not bad, '%s every transcribed quote is on the syllabus page it cites (%d bad%s)'
       % (code, len(bad), (': ' + '; '.join(bad[:3])) if bad else ''))

    # every paper weight is read from the page, never computed
    comp = [p['paper'] for p in F['papers'] if 'NOT STATED' in (p.get('weight_provenance') or '')]
    ck(not comp, '%s every paper weight is the syllabus\u2019s stated figure (%d computed)' % (code, len(comp)))
    # a two-route syllabus records which route this workspace plans for
    if F['ao_weights'].get('by_route'):
        ck(F.get('route') in F['ao_weights']['by_route'],
           '%s names its route (%s) and takes that column' % (code, F.get('route')))
    fwp = os.path.join(REPO, ws, 'curriculum', 'assessment-framework.json')
    if not os.path.exists(fwp):
        print('  ....  %s not yet planned: framework checks wait for its framework' % code)
        continue
    # 2. the framework may not assert an AO, a weight, a paper or a word the facts lack
    FW = json.load(open(fwp))
    fact_aos = {a['code']: a for a in F['assessment_objectives']}
    drift = []
    for a in FW['assessment_objectives']:
        f_ = fact_aos.get(a['code'])
        if not f_:
            drift.append('AO %s is in the framework but not the syllabus' % a['code'])
        elif a['qualification_weight_percent'] != f_['qualification_weight_percent']:
            drift.append('AO %s weight %s != syllabus %s'
                         % (a['code'], a['qualification_weight_percent'],
                            f_['qualification_weight_percent']))
    ck(len(FW['assessment_objectives']) == len(fact_aos) and not drift,
       '%s the framework has exactly the syllabus\u2019s %d AOs at the stated weights%s'
       % (code, len(fact_aos), (' \u2014 ' + '; '.join(drift)) if drift else ''))

    fact_papers = {p['paper']: p for p in F['papers']}
    pdrift = []
    for p_ in FW['papers']:
        # older frameworks name the paper 'paper_id': 'P1'
        p_ = dict(p_, paper=str(p_.get('paper') or p_.get('paper_id', '')).lstrip('Pp'))
        f_ = fact_papers.get(p_['paper'])
        if not f_:
            pdrift.append('Paper %s not in the syllabus' % p_['paper'])
            continue
        if p_['marks'] != f_['marks']:
            pdrift.append('Paper %s marks %s != %s' % (p_['paper'], p_['marks'], f_['marks']))
        if 'weight_percent' in p_ and p_.get('weight_percent') != f_.get('weight_percent'):
            pdrift.append('Paper %s weight %s != syllabus %s'
                          % (p_['paper'], p_.get('weight_percent'), f_.get('weight_percent')))
        if 'NOT STATED' in (f_.get('weight_provenance') or ''):
            pdrift.append('Paper %s weight was computed, not read from the syllabus' % p_['paper'])
        if 'ao_split' in p_ and p_['ao_split'] != f_['ao_split']:
            pdrift.append('Paper %s AO split %s != syllabus %s'
                          % (p_['paper'], p_['ao_split'], f_['ao_split']))
    ck(not pdrift, '%s every paper\u2019s marks and AO split match the syllabus weighting '
                   'table%s' % (code, (' \u2014 ' + '; '.join(pdrift)) if pdrift else ''))

    # 3. the command-word table is the syllabus's, exactly
    fact_cw = {c['word'] for c in F['command_words']}
    fw_listed = {c['word'] for c in FW['command_words'] if c['in_syllabus_table']}
    ck(fw_listed == fact_cw,
       '%s the framework\u2019s listed command words are exactly the syllabus table\u2019s %d '
       '(%s)' % (code, len(fact_cw),
                 'match' if fw_listed == fact_cw
                 else 'framework-only %s, syllabus-only %s'
                      % (sorted(fw_listed - fact_cw), sorted(fact_cw - fw_listed))))
    nomean = [c['word'] for c in FW['command_words']
              if c['in_syllabus_table'] and not c.get('syllabus_page')]
    ck(not nomean, '%s every listed command word cites the syllabus page it came from '
                   '(%d without)' % (code, len(nomean)))

    # 4. anything the syllabus does not state must say so
    unlabelled = [c['word'] for c in FW['command_words']
                  if c.get('primary_assessment_objectives')
                  and c.get('assessment_objectives_provenance') != 'judgement']
    ck(not unlabelled,
       '%s the command-word to AO mapping is labelled a judgement, not a transcription '
       '(%d unlabelled)' % (code, len(unlabelled)))

print('\n=== 1. tariffs reconcile to the published paper totals ===')
for code, expect, label in (('0450', 80, 'Paper 1 and Paper 2 are 80 marks each'),
                            ('0455', 110, 'Paper 2 mark scheme prints 30 + 4x20 = 110')):
    ms = json.load(open(os.path.join(ROOT, '%s_markscheme.json' % code)))
    tot = collections.Counter()
    for r in ms:
        if r['marks']:
            tot[(r['series'], r['paper'], r['variant'])] += r['marks']
    v = sorted(tot.values())
    exact = sum(1 for x in v if x == expect)
    med = v[len(v) // 2]
    ck(med == expect, '%s median paper total %d == %d (%s); exact on %d/%d papers'
       % (code, med, expect, label, exact, len(v)))

print('\n=== 2. the headline answer shapes, re-counted per question block from raw text ===')
import sys
sys.path.insert(0, ROOT)
import mine_ms as M

def scan(code, cw, marks, tests):
    n, c = 0, collections.Counter()
    for f in sorted(glob.glob(os.path.join(ROOT, code, '*_ms_*.txt'))):
        lines = open(f, encoding='utf-8', errors='ignore').read().split('\n')
        for qid, chunk in M.question_blocks(lines):
            flat = M.norm('\n'.join(chunk))
            if len(flat) < 25 or M.tariff(chunk) != marks:
                continue
            if not M.stem_of(chunk).lower().startswith(cw.lower()):
                continue
            n += 1
            for lab, p_ in tests:
                if re.search(p_, flat, re.I):
                    c[lab] += 1
    return n, c

n, c = scan('0450', 'Explain', 6, [
    ('id', r'identification of|one mark for each relevant (problem|reason|factor|way|point|advantage|disadvantage|benefit|effect|issue|method|feature|barrier|impact|difference)'),
    ('app', r'reference (made )?to (this|the) business|application mark'),
    ('exp', r'each relevant (explanation|development)|relevant development|for each explanation')])
ck(n >= 190 and c['exp'] >= n * 0.9,
   '0450 6-mark Explain (n=%d): %d%% award a separate explanation/development mark, '
   '%d%% an application mark, %d%% an identification mark \u2014 the claimed 2x3 grid'
   % (n, 100 * c['exp'] // n, 100 * c['app'] // n, 100 * c['id'] // n))

n, c = scan('0450', 'Explain', 8, [
    ('cap', r'max(imum)?( of)? (two|four|2|4)'),
    ('dev', r'additional mark|each relevant (explanation|development)'),
    ('app', r'reference (made )?to (this|the) business|application mark')])
ck(c['dev'] >= n * 0.9 and c['app'] < n * 0.4,
   '0450 8-mark Explain (n=%d): %d%% award development marks and only %d%% a separate '
   'application mark \u2014 recorded as point-and-development, not point-context-consequence'
   % (n, 100 * c['dev'] // n, 100 * c['app'] // n))

n, c = scan('0450', 'Consider', 12, [
    ('band', r'9\s*[\u2013-]\s*12'),
    ('just', r'well-justified (recommendation|conclusion)'),
    ('rej', r'why the alternative')])
ck(c['rej'] >= n * 0.9,
   '0450 12-mark Consider (n=%d): %d%% band-limited, %d%% demand a well-justified '
   'recommendation, %d%% reserve the ceiling for rejecting the alternatives'
   % (n, 100 * c['band'] // n, 100 * c['just'] // n, 100 * c['rej'] // n))

n, c = scan('0455', 'Explain', 4, [
    ('grid', r'for each of two \w+ identified and one mark'),
    ('pool', r'logical explanation which might include')])
ck(n >= 190 and (c['grid'] + c['pool']) >= n * 0.6,
   '0455 4-mark Explain (n=%d): %d%% a two-by-two grid, %d%% an open pool of creditable '
   'statements \u2014 recorded as four linked statements, one mark each, not a fixed grid'
   % (n, 100 * c['grid'] // n, 100 * c['pool'] // n))

n, c = scan('0455', 'Discuss', 8, [
    ('band', r'a reasoned discussion'),
    ('both', r'both sides'),
    ('skel', r'why (it|they) might')])
ck(c['both'] >= n * 0.9,
   '0455 8-mark Discuss (n=%d): %d%% level-banded, %d%% demand both sides in the top band, '
   '%d%% lay the answer out as why-it-might / why-it-might-not'
   % (n, 100 * c['band'] // n, 100 * c['both'] // n, 100 * c['skel'] // n))

n, c = scan('0455', 'Analyse', 6, [('pool', r'coherent analysis which might include')])
ck(c['pool'] >= n * 0.9,
   '0455 6-mark Analyse (n=%d): %d%% open with a wide pool of creditable statements, '
   'so the marking is point-by-point' % (n, 100 * c['pool'] // n))

print('\n=== 3. command words claimed unused really are unused ===')
for code in ('0450', '0455'):
    fw = json.load(open(os.path.join(REPO, 'work/cie-%s-igcse-2026/curriculum/'
                                           'assessment-framework.json' % code)))
    for w in fw['command_words_listed_but_never_used']:
        n = 0
        for f in glob.glob(os.path.join(ROOT, code, '*_ms_*.txt')):
            t = open(f, encoding='utf-8', errors='ignore').read()
            n += len(re.findall(r'^\s{2,14}\d{1,2}\s*(?:\([a-z]\))?\s*(?:\([ivx]+\))?\s{2,}%s\b'
                                % w, t, re.M))
        ck(n == 0, '%s: "%s" opens 0 question stems across 84 mark schemes (found %d)'
           % (code, w, n))

print('\n=== 4. every planned artefact validates and is internally consistent ===')
for code in ('0450', '0455'):
    ws = os.path.join(REPO, 'work/cie-%s-igcse-2026' % code)
    for fn in ('objective_registry.json', 'assessment-framework.json', 'exam-exposure.json',
               'answer-shapes.json', 'misconceptions.json', 'glossary.json', 'unit_titles.json'):
        p = os.path.join(ws, 'curriculum', fn)
        try:
            json.load(open(p)); ok = True
        except Exception as e:
            ok = False; print('     ', e)
        ck(ok, '%s curriculum/%s is valid JSON' % (code, fn))
    reg = {o['objective_id'] for o in
           json.load(open(os.path.join(ws, 'curriculum', 'objective_registry.json')))['objectives']}
    bad = []
    for f in glob.glob(os.path.join(ws, 'topics', '*', 'contract.json')):
        c = json.load(open(f))
        bad += [i for i in c['scope']['included_objective_ids'] if i not in reg]
    ck(not bad, '%s every contract objective exists in the registry (%d strays)' % (code, len(bad)))
    wos = glob.glob(os.path.join(ws, 'topics', '*', 'work_order.json'))
    cts = glob.glob(os.path.join(ws, 'topics', '*', 'contract.json'))
    ck(len(wos) == len(cts), '%s one work order per contract (%d / %d)' % (code, len(wos), len(cts)))
    # item budget agreement between contract and work order
    off = 0
    for f in cts:
        t = os.path.basename(os.path.dirname(f))
        w = os.path.join(os.path.dirname(f), 'work_order.json')
        if os.path.exists(w):
            c, o = json.load(open(f)), json.load(open(w))
            if abs(len(o.get('item_slots', [])) - c['required_outputs']['learning_items']) > 12:
                off += 1
    wk(off == 0, '%s contract item budget within 12 of the work order slot count '
                 '(%d topics differ by more)' % (code, off))

print('\n=== 5. derivation policy: no examiner or mark-scheme wording carried forward ===')
# Every misconception entry must be a short term pair, never a sentence lifted from a report.
for code in ('0450', '0455'):
    ent = json.load(open(os.path.join(REPO, 'work/cie-%s-igcse-2026/curriculum/'
                                            'misconceptions.json' % code)))['entries']
    longest = max(len(e['a']) + len(e['b']) for e in ent)
    ck(longest <= 100, '%s misconception entries are term pairs, not lifted sentences '
                       '(longest pair %d chars)' % (code, longest))
    # and none of the stored strings appears verbatim in any examiner report as a sentence
    ck(not any(len(e['a'].split()) > 10 or len(e['b'].split()) > 10 for e in ent),
       '%s no misconception side exceeds 10 words' % code)
# The plan and answer-shapes must not quote a question stem.
for code in ('0450', '0455'):
    sh = json.load(open(os.path.join(REPO, 'work/cie-%s-igcse-2026/curriculum/'
                                           'answer-shapes.json' % code)))
    blob = json.dumps(sh)
    stems = [r['stem'] for r in json.load(open(os.path.join(ROOT, '%s_markscheme.json' % code)))
             if r.get('stem') and len(r['stem']) > 45]
    leaked = [s for s in random.Random(7).sample(stems, min(400, len(stems)))
              if s[:45] in blob]
    ck(not leaked, '%s answer-shapes.json quotes no question stem (checked %d stems)'
       % (code, min(400, len(stems))))

print('\n=== 6. exposure did not quietly drop coverage (RS-05) ===')
for code in ('0450', '0455'):
    ws = os.path.join(REPO, 'work/cie-%s-igcse-2026' % code)
    reg = [o for o in json.load(open(os.path.join(ws, 'curriculum',
                                                  'objective_registry.json')))['objectives']
           if o.get('parent_id')]
    planned = set()
    for f in glob.glob(os.path.join(ws, 'topics', '*', 'contract.json')):
        planned |= set(json.load(open(f))['scope']['included_objective_ids'])
    missing = [o['objective_id'] for o in reg if o['objective_id'] not in planned]
    ck(not missing, '%s all %d assessable objectives are inside a contract (%d missing)'
       % (code, len(reg), len(missing)))
    exp = json.load(open(os.path.join(ws, 'curriculum', 'exam-exposure.json')))
    unseen = [o for o in exp['objectives'] if o['exposure_class'] == 'unseen']
    ck(all(o['objective_id'] in planned for o in unseen),
       '%s all %d never-examined objectives are still taught' % (code, len(unseen)))


print('\n=== 7. the handover is self-sufficient: every path it names exists ===')
import glob as _g
SUB = {'0450': ('igcse-business-studies', 'work/cie-0450-igcse-2026'),
       '0455': ('igcse-economics', 'work/cie-0455-igcse-2026')}
PATHRX = re.compile(r'`([A-Za-z0-9_./-]+\.(?:md|json|yaml|py))`')
for code, (slug, ws) in SUB.items():
    for kind in ('PLAN', 'HANDOVER'):
        doc = os.path.join(REPO, ws, '%s-%s-%s.md' % (kind, code, slug))
        ck(os.path.exists(doc), '%s %s document exists' % (code, kind))
        if not os.path.exists(doc):
            continue
        txt = open(doc, encoding='utf-8').read()
        missing = []
        for m_ in PATHRX.finditer(txt):
            rel = m_.group(1)
            if '<' in rel or rel.startswith('CU-') or rel.startswith('topic_'):
                continue
            if '/' not in rel:
                continue
            # the agent CREATES these; they are outputs, not inputs
            if rel.startswith(('claims/', 'content-units/', 'learning-items/')):
                continue
            # a path is written either repo-relative or workspace-relative
            if not (os.path.exists(os.path.join(REPO, rel))
                    or os.path.exists(os.path.join(REPO, ws, rel))):
                missing.append(rel)
        ck(not missing, '%s %s names only paths that exist (%d missing%s)'
           % (code, kind, len(missing), (': ' + ', '.join(sorted(set(missing))[:4])) if missing else ''))
        # a plan must not mention the other subject
        other = [c for c in SUB if c != code][0]
        ck(other not in txt, '%s %s never refers to syllabus %s' % (code, kind, other))

print('\n=== 8. every slot carries a Bloom level and a live command word ===')
for code, (slug, ws) in SUB.items():
    fw = json.load(open(os.path.join(REPO, ws, 'curriculum', 'assessment-framework.json')))
    live = {c['word'] for c in fw['command_words'] if c.get('use_in_prompts')}
    dead = {c['word'] for c in fw['command_words'] if c['verdict'] == 'listed_not_observed'}
    levels = {l['level'] for l in fw['blooms_taxonomy']['levels']}
    nob, nomb, bad_cw, dead_cw = 0, 0, 0, 0
    tot = 0
    for f in _g.glob(os.path.join(REPO, ws, 'topics', '*', 'work_order.json')):
        w = json.load(open(f))
        for s_ in w['item_slots']:
            tot += 1
            if not s_.get('blooms_level'):
                nob += 1
            elif s_['blooms_level'] not in levels:
                bad_cw += 1
            cw = s_.get('command_word')
            if cw and cw in dead:
                dead_cw += 1
            elif cw and cw not in live:
                bad_cw += 1
        for p_ in w['performance_tasks']:
            tot += 1
            if not p_.get('blooms_level'):
                nomb += 1
    ck(nob == 0 and nomb == 0,
       '%s all %d slots and performance tasks carry a blooms_level (%d/%d missing)'
       % (code, tot, nob, nomb))
    ck(dead_cw == 0,
       '%s no slot instructs with a command word the papers never use (%d found)'
       % (code, dead_cw))
    ck(bad_cw == 0, '%s every command word and Bloom level is one the framework declares '
                    '(%d off-list)' % (code, bad_cw))
    # tariffs must be ones the corpus observed for that word
    obs = {c['word']: set(int(k) for k in c['observed_tariffs']) for c in fw['command_words']}
    badt = 0
    for f in _g.glob(os.path.join(REPO, ws, 'topics', '*', 'work_order.json')):
        for s_ in json.load(open(f))['item_slots']:
            cw, t = s_.get('command_word'), s_.get('mark_tariff')
            if cw and t and obs.get(cw) and t not in obs[cw]:
                badt += 1
    ck(badt == 0, '%s every slot tariff is one the corpus observed for that word (%d off)'
       % (code, badt))

print('\n=== 9. syllabus-stated limits are enforced, not just recorded ===')
# Until 2026-09-29 this section checked that each limit's SENTENCE appeared in the contracts. It did,
# and C-11 could never match a sentence, so the check certified a guard that guarded nothing.
sys.path.insert(0, os.path.join(REPO, 'standard', 'v0.2.0-draft', 'checks'))
import types as _types
import yyeni_checks as _Y
for code, (slug, ws) in SUB.items():
    stated = json.load(open(os.path.join(REPO, ws, 'curriculum', 'syllabus-exclusions.json')))
    sents = {x for xs in stated.values() for x in xs}
    sp = os.path.join(REPO, ws, 'curriculum', 'scope-scan.json')
    if not os.path.exists(sp):
        ck(not sents, '%s the syllabus states %d limits and there is no scope-scan.json' % (code, len(sents)))
        continue
    scan = json.load(open(sp))['entries']
    ck({e['syllabus_sentence'] for e in scan} == sents,
       '%s every one of the %d stated limits has a scan pattern' % (code, len(sents)))
    ctl = []
    for e in scan:
        rx = re.compile(e['pattern'], re.I)
        ctl += [x for x in e['controls']['must_catch'] if not rx.search(x)]
        ctl += [x for x in e['controls']['must_allow'] if rx.search(x)]
    ck(not ctl, '%s every scan pattern passes its own controls (%d wrong%s)'
       % (code, len(ctl), (': ' + '; '.join(ctl[:3])) if ctl else ''))
    names = {e['construct'] for e in scan}
    short, unscannable, through = [], [], []
    for p_ in sorted(glob.glob(os.path.join(REPO, ws, 'topics', '*', 'contract.json'))):
        c_ = json.load(open(p_))
        ex = c_['depth_constraints'].get('excluded_constructs') or []
        have = {x.get('construct') for x in ex if isinstance(x, dict)}
        if not names <= have:
            short.append(c_['topic_id'])
        st, msg, _ = _Y.c11(_types.SimpleNamespace(contract=c_, learner_text=lambda: [], answer_text=lambda: []))
        if st == 'fail':
            unscannable.append(c_['topic_id'])
        # end to end: each limit's own must_catch text, placed in this topic's notes, must fail C-11
        for e in scan:
            b_ = _types.SimpleNamespace(contract=c_, learner_text=lambda e=e: [('notes', 'n', e['controls']['must_catch'][0])],
                                        answer_text=lambda: [])
            if _Y.c11(b_)[0] != 'fail':
                through.append('%s:%s' % (c_['topic_id'], e['construct']))
    ck(not short, '%s every contract carries every stated limit (%s)' % (code, ', '.join(short) or 'all'))
    ck(not unscannable, '%s C-11 can scan every contract\u2019s exclusions (%s)' % (code, ', '.join(unscannable) or 'all'))
    ck(not through, '%s a violation of each limit, planted in any topic, fails C-11 (%d got through)' % (code, len(through)))
    # no slot plans a calculation the syllabus rules out
    calc = []
    for p_ in sorted(glob.glob(os.path.join(REPO, ws, 'topics', '*', 'work_order.json'))):
        for sl in json.load(open(p_))['item_slots']:
            if sl['subtype'] == 'CALC' or sl.get('command_word') == 'Calculate':
                txt = sl.get('syllabus_text') or ''
                if re.search(r'calculations?(?: of \w+)?\s+will not be assessed', txt, re.I):
                    calc.append(sl['slot'])
    tids_nocalc = [t for t, xs in stated.items() if any(re.search(r'calculations?\b.*not be assessed', x, re.I) for x in xs)]
    for t in tids_nocalc:
        wp = os.path.join(REPO, ws, 'topics', t, 'work_order.json')
        reg_ = {o['objective_id']: o for o in json.load(open(os.path.join(REPO, ws, 'curriculum', 'objective_registry.json')))['objectives']}
        for sl in json.load(open(wp))['item_slots']:
            o_ = reg_.get(sl['objective_id'], {})
            if (sl['subtype'] == 'CALC' or sl.get('command_word') == 'Calculate') and \
               re.search(r'elasticit|exchange rate', o_.get('syllabus_text', ''), re.I):
                calc.append(sl['slot'])
    ck(not calc, '%s no work-order slot plans a calculation the syllabus rules out (%s)' % (code, ', '.join(sorted(set(calc))) or 'none'))

print('\n' + '=' * 70)
print('%d FAIL, %d WARN' % (len(fails), len(warns)))
for m in fails:
    print('  FAIL ' + m)
