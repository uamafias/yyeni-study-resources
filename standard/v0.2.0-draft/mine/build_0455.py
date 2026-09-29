# -*- coding: utf-8 -*-
"""Build the Cambridge IGCSE Economics 0455 objective registry from the syllabus.

Section 3 Subject content is a two-column table: Topic | Guidance. The split
column moves page to page, so it is read off each table's own header row.
"""
import json, os, re, datetime
ROOT = os.path.expanduser('~/mine')
SRC = os.path.join(ROOT, '0455_syllabus.txt')

UNIT   = re.compile(r'^\s{5,}([1-6])\s{5,}([A-Z].{4,70})\s*$')
# A two-digit minor number eats the column padding: '2.9     Market economic
# system' has five spaces, '2.10 Market failure' has one. Requiring four dropped
# topics 2.10 and 2.11 silently, so the gap is closed by requiring only that the
# number be followed by whitespace and a capitalised title.
TOPIC  = re.compile(r'^\s{5,}([1-6]\.\d{1,2})\s{1,}([A-Z(].{3,80}?)\s*$')
SUB    = re.compile(r'^(\s{5,})([1-6]\.\d{1,2}\.\d{1,2})\s+(\S.*)$')
HDR    = re.compile(r'^(\s+)Topic(\s+)Guidance\s*$')
JUNK   = re.compile(r'(Back to contents|cambridgeinternational\.org|syllabus for 2026|'
                    r'^\s*$|^\s*\d+\s*$)')

def parse():
    lines = open(SRC, encoding='utf-8', errors='ignore').read().split('\n')
    start = next(i for i, l in enumerate(lines) if re.match(r'^\s*3 Subject content\s*$', l))
    end   = next(i for i, l in enumerate(lines)
                 if i > start and re.match(r'^\s*4\s+Details of the assessment', l))
    body = lines[start:end]

    units, topics, subs = {}, {}, []
    split_at, cur_topic, cur = 60, None, None
    for ln in body:
        if JUNK.search(ln):
            continue
        h = HDR.match(ln)
        if h:
            split_at = len(h.group(1)) + len('Topic') + len(h.group(2))
            continue
        u = UNIT.match(ln)
        if u and not TOPIC.match(ln):
            units[u.group(1)] = u.group(2).strip()
            continue
        t = TOPIC.match(ln)
        if t and not SUB.match(ln):
            title = re.sub(r'\s+continued$', '', t.group(2).strip())
            topics[t.group(1)] = title
            cur_topic = t.group(1)
            cur = None
            continue
        s = SUB.match(ln)
        if s:
            rest = s.group(3)
            left = rest[:max(0, split_at - len(s.group(1)) - len(s.group(2)) - 1)].strip()
            right = rest[max(0, split_at - len(s.group(1)) - len(s.group(2)) - 1):].strip()
            cur = {'id': s.group(2), 'title': left, 'guidance': right,
                   'topic_id': '.'.join(s.group(2).split('.')[:2])}
            subs.append(cur)
            continue
        if cur is not None and ln.strip():
            col = len(ln) - len(ln.lstrip())
            if col >= split_at - 4:
                cur['guidance'] = (cur['guidance'] + ' ' + ln.strip()).strip()
            else:
                seg = ln[:split_at].strip()
                tail = ln[split_at:].strip()
                if seg:
                    cur['title'] = (cur['title'] + ' ' + seg).strip()
                if tail:
                    cur['guidance'] = (cur['guidance'] + ' ' + tail).strip()
    for s in subs:
        s['title'] = re.sub(r'\s+', ' ', s['title'])
        s['guidance'] = re.sub(r'\s+', ' ', s['guidance'])
    return units, topics, subs

# --- objective typing, mirroring the 0450 generator's core() rule ------------
def core(text):
    """Strip e.g./such as/for example clauses before typing: an illustrative
    noun inside an example must not decide the objective's type."""
    return re.split(r'\b(?:e\.?g\.?|such as|for example|including|,? including)\b',
                    text, 1, flags=re.I)[0]

TYPES = [
 ('economics_diagram',        r'\bdiagram|\bcurve\b|\bppc\b|shift|movement along|drawing and interpretation'),
 ('economics_quantitative',   r'calculat|elasticity|formula|index|rate of|per head|percentage'),
 ('economics_definition',     r'\bdefinitions? (and|of)\b|^\s*definition|definitions of|\bdefine\b|the meaning of'),
 ('economics_cause_effect',   r'\bcauses?\b|\bconsequences?\b|\beffects?\b|\bimpact\b|\binfluences?\b|reasons for'),
 ('economics_policy_evaluation', r'policy|policies|government (aim|measure|intervention)|measures to'),
 ('economics_comparison',     r'difference between|compared|versus|distinction'),
 ('economics_classification', r'types of|classification|categories|components of|functions of|characteristics of'),
 ('economics_mechanism',      r'how .* works|mechanism|process|determination|allocat'),
]
def otype(title, guidance):
    t = core(title + '. ' + guidance).lower()
    for name, pat in TYPES:
        if re.search(pat, t):
            return name
    return 'economics_concept'

# depth tier: 1 recall, 2 apply, 3 analyse, 4 evaluate
def tier(title, guidance, typ):
    t = (title + ' ' + guidance).lower()
    if typ == 'economics_policy_evaluation' or re.search(r'evaluat|whether|extent to which|effectiveness', t):
        return 4
    if typ in ('economics_cause_effect', 'economics_mechanism', 'economics_diagram') or \
       re.search(r'analys|consequence|effect|impact|relationship', t):
        return 3
    if typ in ('economics_definition',) or re.search(r'^definition', t):
        return 1
    return 2

AO_BY_TIER = {1: ['AO1'], 2: ['AO1', 'AO2'], 3: ['AO1', 'AO2'], 4: ['AO1', 'AO2', 'AO3']}
# 0455 command words, from the question-paper corpus
CW_BY_AO = {'AO1': ['Define', 'Identify', 'State', 'Give', 'Describe', 'Calculate'],
            'AO2': ['Explain', 'Analyse', 'Draw'],
            'AO3': ['Discuss']}

def build():
    units, topics, subs = parse()
    objs = []
    for tid in sorted(topics, key=lambda x: [int(y) for y in x.split('.')]):
        objs.append({
            'objective_id': 'OBJ-0455-%s' % tid,
            'parent_id': None, 'topic_id': tid,
            'syllabus_text': '%s %s' % (tid, topics[tid]),
            'learner_objective': '%s (syllabus topic %s, within %s %s)'
                                 % (topics[tid], tid, tid.split('.')[0],
                                    units.get(tid.split('.')[0], '')),
            'level': 'IGCSE', 'route_status': 'core', 'mandatory': True,
            'objective_type': 'economics_concept',
            'assessment_objectives': ['AO1', 'AO2', 'AO3'],
            'command_words': [], 'prerequisite_ids': [],
            'depth_tier': 4, 'status': 'planned'})
        for s in subs:
            if s['topic_id'] != tid:
                continue
            typ = otype(s['title'], s['guidance'])
            dt = tier(s['title'], s['guidance'], typ)
            aos = AO_BY_TIER[dt]
            objs.append({
                'objective_id': 'OBJ-0455-%s' % s['id'],
                'parent_id': 'OBJ-0455-%s' % tid, 'topic_id': tid,
                'syllabus_text': s['title'],
                'syllabus_guidance': s['guidance'],
                'learner_objective': s['title'],
                'level': 'IGCSE', 'route_status': 'core', 'mandatory': True,
                'objective_type': typ,
                'assessment_objectives': aos,
                'command_words': sorted({c for a in aos for c in CW_BY_AO[a]}),
                'prerequisite_ids': [], 'depth_tier': dt, 'status': 'planned'})
    return units, topics, objs

if __name__ == '__main__':
    units, topics, objs = build()
    reg = {'registry_id': 'OBJREG-CIE-0455-IGCSE-2026',
           'generated_at': datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
           'authority': 'Cambridge IGCSE Economics 0455 syllabus for 2026, section 3 Subject content.',
           'granularity_note': 'One objective per syllabus sub-topic (N.N.N), plus one container per topic (N.N).',
           'objectives': objs}
    os.makedirs(os.path.join(ROOT, 'out'), exist_ok=True)
    json.dump(reg, open(os.path.join(ROOT, 'out', '0455_objective_registry.json'), 'w'), indent=1)
    json.dump({k: 'Unit %s — %s' % (k, v) for k, v in units.items()},
              open(os.path.join(ROOT, 'out', '0455_unit_titles.json'), 'w'), indent=1)
    import collections
    print('units  %d: %s' % (len(units), '; '.join('%s %s' % kv for kv in sorted(units.items()))))
    print('topics %d   objectives %d (%d assessable sub-topics)'
          % (len(topics), len(objs), sum(1 for o in objs if o['parent_id'])))
    print('types :', dict(collections.Counter(o['objective_type'] for o in objs if o['parent_id'])))
    print('tiers :', dict(collections.Counter(o['depth_tier'] for o in objs if o['parent_id'])))
    print('\nsample:')
    for o in objs[1:5]:
        print('  %-18s t%d %-26s %s' % (o['objective_id'], o['depth_tier'],
                                        o['objective_type'], o['syllabus_text'][:52]))
        print('      guidance: %s' % o.get('syllabus_guidance', '')[:96])
