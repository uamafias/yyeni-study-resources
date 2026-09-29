# -*- coding: utf-8 -*-
"""Build the misconception register: examiner-evidenced confusions, attached to
syllabus objectives, classified by the KIND of mistake so the author knows what
shape of card fixes it."""
import json, os, re, collections
ROOT = os.path.expanduser('~/mine')
REPO = os.path.expanduser('~/mnt/YYeni Study Resources')

STOPW = set('''the a an and or of to in for on with by from as is are was were be been being
that this these those it its their his her they them not no but which who whom whose what
when where why how some many most other others more less than then so such e.g. eg i.e. ie
candidates candidate answers answer responses response weaker stronger able unable often
number few several most given used use using two one three four rather instead between
term terms vague precision ideas about would could may might will shall can'''.split())

def toks(s):
    return [w for w in re.findall(r"[a-z][a-z'’-]+", s.lower()) if w not in STOPW and len(w) > 2]

# --- the kind of confusion decides the kind of card that repairs it ----------
DIRECTIONAL = re.compile(
    r'^(caus|consequenc|effect|reason|purpose|role|function|characteristic|feature|'
    r'benefit|advantage|disadvantage|how |why |influence|impact|stage|sector|method)', re.I)
POLAR = re.compile(r'\b(un)?limited\b|appreciat|depreciat|surplus|deficit|rise|fall|'
                   r'increase|decrease|direct|indirect|left|right|inward|outward', re.I)

def classify(a, b):
    ha, hb = a.split()[0], b.split()[0]
    if DIRECTIONAL.match(a) or DIRECTIONAL.match(b):
        if re.match(r'^(caus|reason)', a) and re.match(r'^(consequenc|effect|impact)', b) or \
           re.match(r'^(consequenc|effect|impact)', a) and re.match(r'^(caus|reason)', b):
            return 'cause_vs_consequence'
        return 'wrong_angle_same_concept'
    if POLAR.search(a) and POLAR.search(b):
        return 'opposite_direction'
    if ha == hb or a in b or b in a:
        return 'near_neighbour_term'
    return 'adjacent_concept'

# extraction artefacts: one side is not a concept
# One side is not a concept: it is answer-craft language the pair regex caught.
BAD = re.compile(r'^(explanation|activities|term|vague|precision|then provided|'
                 r'identifying|stated|selecting|wrongly assumed|listed|listing|'
                 r'new points|additional (knowledge|points)|discussion|points about|'
                 r'demonstrating|mix(ed)? )', re.I)
CRAFTY = re.compile(r'\b(knowledge points?|demonstrat\w+|development|analysis|'
                    r'listed|discussion about|points about|spoke of|answers?)\b', re.I)

def load_pairs(code):
    d = json.load(open(os.path.join(ROOT, 'out', '%s_confusion_pairs.json' % code)))
    out = []
    for k, v in d.items():
        a, b = [x.strip() for x in k.split('  <>  ')]
        if BAD.match(a) or BAD.match(b):
            continue
        if CRAFTY.search(a) or CRAFTY.search(b):
            continue
        if not toks(a) or not toks(b):
            continue
        out.append({'a': a, 'b': b, 'n': v['n'], 'series': v['series'],
                    'kind': classify(a, b)})
    return out

def registry(code, path):
    objs = json.load(open(os.path.join(REPO, path)))['objectives']
    idx = []
    for o in objs:
        t = set(toks(o['syllabus_text']))
        if t:
            idx.append((o['objective_id'], o.get('topic_id'), o['syllabus_text'], t))
    return idx

def attach(pairs, idx):
    import math
    df = collections.Counter()
    for _, _, _, t in idx:
        for w in t:
            df[w] += 1
    N = float(len(idx))
    def w_(x):
        return math.log(N / (1 + df.get(x, 0))) + 1.0
    for p in pairs:
        want = set(toks(p['a'])) | set(toks(p['b']))
        best, score = None, 0
        for oid, tid, txt, t in idx:
            s = sum(w_(x) for x in (want & t))
            if s > score or (s == score and s and best and len(oid) > len(best[0])):
                best, score = (oid, tid, txt), s
        p['objective_id'] = best[0] if score else None
        p['topic_id'] = best[1] if score else None
        p['objective_text'] = best[2][:90] if score else None
        p['match_strength'] = round(score, 2)
    return pairs

if __name__ == '__main__':
    out = {}
    for code, path in (('0450', 'work/cie-0450-igcse-2026/curriculum/objective_registry.json'),
                       ('0455', 'work/cie-0455-igcse-2026/curriculum/objective_registry.json')):
        idx = registry(code, path)
        ps = attach(load_pairs(code), idx)
        out[code] = ps
        hit = sum(1 for p in ps if p['match_strength'] >= 2.5)
        print('%s  %d curated confusions, %d attached to an objective' % (code, len(ps), hit))
        print('  by kind:', dict(collections.Counter(p['kind'] for p in ps)))
        print('\n  attached (strength >=1), by topic:')
        for p in sorted([x for x in ps if x['match_strength'] >= 2.5],
                        key=lambda x: (x['topic_id'] or 'z', -x['n'])):
            print('   %-6s %-22s %-46s' % (p['topic_id'], p['kind'], (p['a'] + ' / ' + p['b'])[:46]))
    json.dump(out, open(os.path.join(ROOT, 'out', 'misconception_register.json'), 'w'), indent=1)
