# -*- coding: utf-8 -*-
"""Measure how often each syllabus objective has actually been examined.

Evidence: every question part mined from the held papers, matched to the
objective whose syllabus wording it shares the most distinctive vocabulary with.
Matching is restricted to syllabus vocabulary, so a case-study company name
cannot drive the match.

RS-05 still governs: frequency calibrates emphasis, it never removes coverage.
"""
import json, os, re, math, collections, datetime
ROOT = os.path.expanduser('~/mine')
REPO = os.path.expanduser('~/mnt/YYeni Study Resources')

STOP = set('''the a an and or of to in for on with by from as is are was were be been
that this these those it its their they them not no but which who what when where why
how some many most other more less than then so such e.g eg i.e ie two one three four
give state define explain outline identify calculate analyse discuss consider using
describe draw name list following each both may might could would should business
businesses company companies example examples answer answers use used using refer
your you do think justify recommend'''.split())

def toks(s):
    return [w for w in re.findall(r"[a-z][a-z'-]+", (s or '').lower())
            if w not in STOP and len(w) > 3]

def build_index(reg_path):
    objs = json.load(open(reg_path))['objectives']
    idx, vocab = [], collections.Counter()
    for o in objs:
        if not o.get('parent_id'):
            continue                      # container rows are not assessable
        txt = o['syllabus_text'] + ' ' + o.get('syllabus_guidance', '')
        t = set(toks(txt))
        if t:
            idx.append({'id': o['objective_id'], 'topic': o['topic_id'],
                        'text': o['syllabus_text'], 'toks': t,
                        'type': o['objective_type'], 'tier': o['depth_tier']})
            for w in t:
                vocab[w] += 1
    N = float(len(idx))
    idf = {w: math.log(N / (1 + c)) + 1.0 for w, c in vocab.items()}
    return objs, idx, idf

def match(stem, idx, idf, floor=3.0):
    want = set(toks(stem)) & set(idf)     # syllabus vocabulary only
    if not want:
        return None, 0.0
    best, sc = None, 0.0
    for o in idx:
        s = sum(idf[w] for w in (want & o['toks']))
        if s > sc:
            best, sc = o, s
    return (best, round(sc, 2)) if sc >= floor else (None, round(sc, 2))

def run(code, reg_path, out_name, authority):
    objs, idx, idf = build_index(reg_path)
    qs = json.load(open(os.path.join(ROOT, '%s_questions.json' % code)))
    ms = json.load(open(os.path.join(ROOT, '%s_markscheme.json' % code)))
    # the mark scheme restates every question and covers papers the QP miner
    # could not parse, so it is the fuller source of stems
    seen, parts = set(), []
    for r in ms:
        if not r.get('stem') or not r.get('marks'):
            continue
        k = (r['series'], r['paper'], r['variant'], r['qid'])
        if k in seen:
            continue
        seen.add(k)
        parts.append({'series': r['series'], 'paper': r['paper'],
                      'variant': r.get('variant', ''), 'file': r.get('file'),
                      'stem': r['stem'], 'cw': r['cw'], 'marks': r['marks']})
    hit = collections.defaultdict(list)
    unmatched = 0
    for p in parts:
        o, sc = match(p['stem'], idx, idf)
        if o is None:
            unmatched += 1
            continue
        hit[o['id']].append(p)

    total_marks = sum(p['marks'] for p in parts)
    rows = []
    for o in idx:
        ps = hit.get(o['id'], [])
        marks = sum(p['marks'] for p in ps)
        series = sorted({p['series'] for p in ps})
        rows.append({
            'objective_id': o['id'], 'topic_id': o['topic'],
            'syllabus_text': o['text'],
            'times_examined': len(ps),
            'marks_examined': marks,
            'series_spread': len(series), 'series': series,
            'tariffs': dict(collections.Counter(p['marks'] for p in ps)),
            'command_words': dict(collections.Counter(p['cw'] for p in ps if p['cw'])),
            'modal_tariff': (collections.Counter(p['marks'] for p in ps).most_common(1)[0][0]
                             if ps else None)})
    # exposure class from series spread, not raw count: a topic examined five
    # times in one series is a quirk; one examined in twelve series is core.
    for r in rows:
        s = r['series_spread']
        r['exposure_class'] = ('core' if s >= 10 else
                               'frequent' if s >= 6 else
                               'occasional' if s >= 2 else
                               'rare' if s == 1 else 'unseen')
    out = {'exposure_id': 'EXPOSURE-CIE-%s-IGCSE-2026' % code,
           'generated_at': datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
           'authority': authority,
           'evidence_window': '%d question parts carrying %d marks, mined from %d published '
                              'mark schemes across %d examination series, 2020-2025.'
                              % (len(parts), total_marks,
                                 len({p['file'] for p in parts if p.get('file')}),
                                 len({p['series'] for p in parts})),
           'method': 'Each question part matched to the objective sharing the most '
                     'distinctive syllabus vocabulary (IDF-weighted, syllabus terms only, '
                     'score floor 3.0). Unmatched parts are reported, not distributed.',
           'principle': 'RS-05: past-paper frequency may calibrate emphasis but MUST NOT '
                        'remove or weaken syllabus-mandated coverage.',
           'status': 'measured',
           'unmatched_parts': unmatched,
           'objectives': sorted(rows, key=lambda r: (-r['series_spread'], -r['marks_examined']))}
    json.dump(out, open(os.path.join(ROOT, 'out', out_name), 'w'), indent=1)

    cl = collections.Counter(r['exposure_class'] for r in rows)
    print('\n%s  %d parts / %d marks  | matched %d, unmatched %d (%.0f%%)'
          % (code, len(parts), total_marks, len(parts) - unmatched, unmatched,
             100.0 * unmatched / max(len(parts), 1)))
    print('   exposure classes:', dict(cl))
    print('   top 12 objectives by series spread:')
    for r in out['objectives'][:12]:
        print('     %-20s %-9s sp=%-2d n=%-3d marks=%-4d %s'
              % (r['objective_id'], r['exposure_class'], r['series_spread'],
                 r['times_examined'], r['marks_examined'], r['syllabus_text'][:46]))
    print('   never seen in the corpus: %d objectives' % cl.get('unseen', 0))
    return out

run('0450', os.path.join(REPO, 'work/cie-0450-igcse-2026/curriculum/objective_registry.json'),
    '0450_exam_exposure.json',
    'Cambridge IGCSE Business Studies 0450 syllabus for 2026, section 3, matched against '
    '84 published question papers and mark schemes, 2020-2025.')
run('0455', os.path.join(ROOT, 'out', '0455_objective_registry.json'),
    '0455_exam_exposure.json',
    'Cambridge IGCSE Economics 0455 syllabus for 2026, section 3, matched against '
    '84 published question papers and mark schemes, 2020-2025.')
