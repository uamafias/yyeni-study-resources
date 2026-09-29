# -*- coding: utf-8 -*-
"""Mine the 0500 Principal Examiner Reports: what strong and weak answers do, per task.

For a language subject the success description matters as much as the failure one,
so both are kept (the business miners kept failures only). Every sentence is
filed under the task it discusses and tagged strong / weak / advice. Nothing here
is reproduced for learners; the analysis paraphrases.
"""
import os, re, json, collections
ROOT = os.path.expanduser('~/mine')
SRC = os.path.join(ROOT, '0500')
NOISE = re.compile(r'(UCLES|Principal Examiner Report|www\.|^\s*\d+\s*$|Cambridge IGCSE|©)')

TASK_P1 = [
 (r'1\s*\(\s*f\s*\)|summary', 'P1 Q1(f) summary'),
 (r'1\s*\(\s*[a-e]\s*\)', 'P1 Q1(a-e) comprehension'),
 (r'2\s*\(\s*a\s*\)', 'P1 Q2(a) word or phrase with the same meaning'),
 (r'2\s*\(\s*b\s*\)', 'P1 Q2(b) own-words meaning of single words'),
 (r'2\s*\(\s*c\s*\)', 'P1 Q2(c) one example, explain the effect'),
 (r'2\s*\(\s*d\s*\)', 'P1 Q2(d) language task'),
 (r'^3\b|question 3', 'P1 Q3 extended response to reading'),
]
TASK_P2 = [
 (r'section a|question 1', 'P2 Section A directed writing'),
 (r'question [23]\b.*describe|descriptive', 'P2 Section B descriptive composition'),
 (r'question [45]\b.*(?:story|narrative)|narrative', 'P2 Section B narrative composition'),
 (r'question [2345]|section b', 'P2 Section B composition (either)'),
]
STRONG = re.compile(r'\b(strong(?:er|est)?|best|most successful|more successful|high(?:er)?[- ]level|'
                    r'effective(?:ly)?|skilful|sophisticated|confident(?:ly)?|excellent|good responses|'
                    r'well[- ]developed|top of|highest)\b', re.I)
WEAK = re.compile(r'\b(weak(?:er|est)?|less successful|less effective|limited|did not|failed to|'
                  r'unable|struggled|lifted|copied|misread|misunderstood|lost focus|repeated|'
                  r'mechanical|thin|brief|lacked|often|some candidates|a few candidates|too (?:long|short))\b', re.I)
ADVICE = re.compile(r'\b(should|need(?:s|ed)? to|are (?:advised|reminded|encouraged)|it is important|'
                    r'would benefit|must|remember)\b', re.I)


def sentences(block):
    txt = re.sub(r'\s+', ' ', block)
    txt = re.sub(r'\s*[•●]\s*', ' • ', txt)
    return [s.strip(' •') for s in re.split(r'(?<=[.!?])\s+(?=[A-Z•‘\'"(])|\s•\s', txt)
            if 25 < len(s.strip()) < 600]


P1_PART = {('1', 'f'): 'P1 Q1(f) summary', ('2', 'a'): 'P1 Q2(a) word or phrase with the same meaning',
           ('2', 'b'): 'P1 Q2(b) own-words meaning of single words',
           ('2', 'c'): 'P1 Q2(c) one example, explain the effect', ('2', 'd'): 'P1 Q2(d) language task'}


def p1_task(q, letter):
    if q == '3':
        return 'P1 Q3 extended response to reading'
    if q == '1':
        return P1_PART.get((q, letter), 'P1 Q1(a-e) comprehension')
    if q == '2':
        return P1_PART.get((q, letter), 'P1 Q2 (general)')
    return None


def task_of(label, paper, body_head):
    lab = (label + ' ' + body_head[:120]).lower()
    for rx, name in (TASK_P1 if paper == '1' else TASK_P2):
        if re.search(rx, lab):
            return name
    return None


def run():
    out = []
    for fn in sorted(os.listdir(SRC)):
        if not fn.endswith('_er.txt'):
            continue
        series = fn.split('_')[1]
        raw = open(os.path.join(SRC, fn), encoding='utf-8', errors='ignore').read()
        lines = [l for l in raw.split('\n') if not NOISE.search(l)]
        # split by paper variant heading
        cuts = [(i, m.group(1), m.group(2)) for i, l in enumerate(lines)
                for m in [re.match(r'^\s*Paper\s+0500/(\d)(\d)\s*$', l)] if m]
        for k, (i, pap, var) in enumerate(cuts):
            if pap not in ('1', '2'):
                continue
            end = cuts[k + 1][0] if k + 1 < len(cuts) else len(lines)
            blk = lines[i:end]
            # key messages and general comments
            sec, cur_task, buf, cur_q = 'preamble', None, [], None
            def flush():
                if not buf:
                    return
                for s in sentences('\n'.join(buf)):
                    kind = ('strong' if STRONG.search(s) and not re.search(r'\bless (?:strong|effective|successful)\b', s, re.I)
                            else 'weak' if WEAK.search(s) else 'advice' if ADVICE.search(s) else 'other')
                    if re.search(r'\bless (?:strong|effective|successful)\b|\bweaker\b', s, re.I):
                        kind = 'weak'
                    out.append({'series': series, 'paper': pap, 'variant': var, 'section': sec,
                                'task': cur_task, 'kind': kind, 'text': s})
            for l in blk:
                st = l.strip()
                if re.match(r'^Key messages', st):
                    flush(); buf = []; sec, cur_task = 'key messages', None; continue
                if re.match(r'^General comments', st):
                    flush(); buf = []; sec, cur_task = 'general', None; continue
                if re.match(r'^Comments on specific questions', st):
                    flush(); buf = []; sec = 'specific'; continue
                m = re.match(r'^(Question\s+(\d)(?:\s*\(([a-z])\))?(?:\s*\([ivx]+\))?|Section\s+[AB])\b(.*)$', st)
                if sec == 'specific' and m and len(st) < 160:
                    if pap == '1' and m.group(2):
                        cur_q = m.group(2)
                        t = p1_task(cur_q, m.group(3) or ('f' if 'summary' in st.lower() and cur_q == '1' else None))
                    else:
                        t = task_of(m.group(1), pap, m.group(4))
                    if t:
                        flush(); buf = []; cur_task = t; continue
                # a part letter at the start of a line inside a Paper 1 question block
                mp = re.match(r'^\(([a-f])\)\s', st)
                if sec == 'specific' and pap == '1' and mp and cur_task and cur_task.startswith('P1'):
                    q = '1' if 'Q1' in cur_task else '2' if 'Q2' in cur_task else None
                    if q:
                        t = p1_task(q, mp.group(1))
                        if t and t != cur_task:
                            flush(); buf = []; cur_task = t
                buf.append(l)
            flush()
    return out


if __name__ == '__main__':
    rows = run()
    json.dump(rows, open(os.path.join(ROOT, '0500_examiner_statements.json'), 'w'), indent=1)
    c = collections.Counter((r['task'] or r['section'], r['kind']) for r in rows)
    tasks = sorted({r['task'] or r['section'] for r in rows}, key=str)
    print('%d sentences from %d reports' % (len(rows), len({r['series'] for r in rows})))
    print('%-46s %7s %6s %7s %6s  %s' % ('task', 'strong', 'weak', 'advice', 'other', 'series'))
    for t in tasks:
        ser = len({r['series'] for r in rows if (r['task'] or r['section']) == t})
        print('%-46s %7d %6d %7d %6d  %d' % (t[:46], c[(t, 'strong')], c[(t, 'weak')], c[(t, 'advice')], c[(t, 'other')], ser))
