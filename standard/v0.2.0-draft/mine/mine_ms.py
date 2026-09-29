# -*- coding: utf-8 -*-
"""Mine Cambridge mark schemes for the GRAMMAR of a credit-worthy answer.

The mark scheme restates the question in its Answer column, so it is a
self-sufficient source: command word, tariff and required answer structure all
come from the same block. Nothing mined here is reproduced in learner output.
"""
import json, os, re, collections

ROOT = os.path.expanduser('~/mine')

QID_LINE = re.compile(r'^(\s{2,14})(\d{1,2}\s*(?:\([a-z]\))?\s*(?:\([ivx]+\))?)(\s{2,})(\S.*)$')
QID_OK   = re.compile(r'^\d{1,2}(\([a-z]\))?(\([ivx]+\))?$')
HEADER_JUNK = re.compile(
    r'(UCLES|Page \d+ of|PUBLISHED|www\.|Cambridge (IGCSE|International|Pre-U)|'
    r'Mark Scheme|GENERIC MARKING|MARKING PRINCIPLE|Social Science-Specific|'
    r'^\s*Question\s+Answer\s+Marks)')

CW = re.compile(
    r'^\s*(Identify|Define|State|Give|Name|Outline|Describe|Explain|Calculate|'
    r'Analyse|Analyze|Discuss|Consider|Evaluate|Assess|Justify|Recommend|Draw|'
    r'Complete|Using|Refer|Which|What|Why|How|List)\b', re.I)

AWARD = re.compile(
    r'\b(?:Award|award)\s+(one|two|three|four|five|six|1|2|3|4|5|6)\s+mark[s]?\s+'
    r'(for each|per|for)\s+(.{0,100})', re.I)
ONEEACH = re.compile(r'\bOne mark (?:each )?for each of (\w+)\s+(.{0,70})', re.I)
NUM = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,
       '1':1,'2':2,'3':3,'4':4,'5':5,'6':6}

TAG      = re.compile(r'\[(k|app|an|ev|kn)\]', re.I)
CREDIT1  = re.compile(r'\(1\)')
BAND     = re.compile(r'^\s{6,}([0-3])\s{3,}(\S.*?)\s{3,}(\d+\s*[–—-]\s*\d+|\d+)\s*$')
SUBHEAD  = re.compile(r'^\s{5,}([A-Z][A-Za-z /\'’-]{3,45}):\s*$')
REFUSE   = re.compile(r'((?:Do not (?:award|credit|accept)|Not accepting|[Nn]o marks for|Reject)'
                      r'[^.\n]{0,170})')
REQUIRE  = re.compile(r'((?:Answers must|Responses must|Candidates must|For both marks|'
                      r'To gain (?:full|the) mark)[^.\n]{0,170})')
APPLIST  = re.compile(r'Application marks may be awarded for(?: appropriate use of)?'
                      r'(?: the following)?:?(.{0,300})', re.S)
MARKCELL = re.compile(r'\s{3,}(\d{1,2})(?:\s|$)')

def norm(s): return re.sub(r'\s+', ' ', s).strip()

def question_blocks(lines):
    out, cur, key = [], [], None
    for ln in lines:
        if HEADER_JUNK.search(ln):
            continue
        m = QID_LINE.match(ln)
        if m and QID_OK.match(re.sub(r'\s+', '', m.group(2))):
            if key:
                out.append((key, cur))
            key, cur = re.sub(r'\s+', '', m.group(2)), [ln]
            continue
        if key is not None:
            cur.append(ln)
    if key:
        out.append((key, cur))
    return out

def stem_of(chunk):
    """The restated question: the qid line's text plus following lines until the
    first award/answer line."""
    m = QID_LINE.match(chunk[0])
    buf = [m.group(4)] if m else []
    for ln in chunk[1:6]:
        s = ln.strip()
        if not s:
            break
        if re.match(r'^(Award|Points might|Two from|One mark|Coherent|Logical|'
                    r'Relevant|Up to|Level|Answers)', s):
            break
        buf.append(s)
    txt = norm(' '.join(buf))
    # strip a trailing Marks/Notes-column spill
    txt = re.sub(r'\s{3,}\d{1,2}\s.*$', '', txt)
    return txt[:260]

CELL = re.compile(r'(?<![\d.])(\d{1,2})(?![\d.])')
ANSWER_START = re.compile(r'^\s*(Award|Points might|Two from|One mark|Coherent|Logical|'
                          r'Relevant|Up to|Level|Answers|Any two|\u2022)')

def _cell(ln, lo=64, hi=112):
    """A value sitting in the Marks column: isolated, right of the Answer column."""
    for m in CELL.finditer(ln):
        i, j = m.start(1), m.end(1)
        if not (lo <= i <= hi):
            continue
        if i > 0 and ln[max(0, i - 3):i] != '   ':
            continue
        if j < len(ln) and ln[j] not in ' \t':
            continue
        v = int(m.group(1))
        if 1 <= v <= 20:
            return v
    return None

def tariff(chunk, stem=None, nmax=5):
    """Read the Marks cell from the stem region of the block.

    Validated against published paper totals: 73 of 84 0450 papers sum to
    exactly 80; 0455 Paper 2 sums to 110, which is 30 (Section A) + 4 x 20
    (Section B, of which a candidate answers three, for 90).
    """
    for k, ln in enumerate(chunk):
        if k and ANSWER_START.match(ln):
            return _cell(ln)
        v = _cell(ln)
        if v:
            return v
        if k >= nmax:
            break
    return None

def bands(chunk):
    out = []
    for ln in chunk:
        m = BAND.match(ln)
        if m:
            rng = m.group(3).replace('–', '-').replace('—', '-')
            lo, _, hi = rng.partition('-')
            out.append({'band': int(m.group(1)), 'lo': int(lo.strip()),
                        'hi': int((hi or lo).strip()),
                        'descriptor': norm(m.group(2))[:120]})
    return out

def analyse(code):
    src, rows = os.path.join(ROOT, code), []
    for fn in sorted(os.listdir(src)):
        if '_ms' not in fn or not fn.endswith('.txt'):
            continue
        p = fn[:-4].split('_')
        series, pv = p[1], (p[3] if len(p) > 3 else '?')
        with open(os.path.join(src, fn), encoding='utf-8', errors='ignore') as fh:
            lines = fh.read().split('\n')
        for qid, chunk in question_blocks(lines):
            flat = norm('\n'.join(chunk))
            if len(flat) < 25:
                continue
            stem = stem_of(chunk)
            cwm = CW.match(stem)
            awards = [{'n': NUM[m.group(1).lower()], 'mode': m.group(2).lower(),
                       'for': norm(m.group(3))[:95]} for m in AWARD.finditer(flat)]
            for m in ONEEACH.finditer(flat):
                awards.append({'n': 1, 'mode': 'for each of %s' % m.group(1).lower(),
                               'for': norm(m.group(2))[:95]})
            am = APPLIST.search(flat)
            rows.append({
                'code': code, 'series': series, 'paper': pv[0], 'variant': pv[1:],
                'qid': qid, 'stem': stem,
                'cw': cwm.group(1).title() if cwm else None,
                'marks': tariff(chunk),
                'credit_tokens': len(CREDIT1.findall(flat)),
                'tags': dict(collections.Counter(
                    x.lower().replace('kn', 'k') for x in TAG.findall(flat))),
                'awards': awards[:8],
                'bands': bands(chunk),
                'skeleton': [norm(m.group(1)) for m in
                             (SUBHEAD.match(l) for l in chunk) if m][:12],
                'refuse': [norm(x) for x in REFUSE.findall(flat)][:6],
                'require': [norm(x) for x in REQUIRE.findall(flat)][:4],
                'application_anchors': ([norm(x) for x in re.split(r'•', am.group(1))
                                         if 2 < len(norm(x)) < 55][:8] if am else []),
                'file': fn[:-4]})
    return rows

if __name__ == '__main__':
    for code in ('0450', '0455'):
        rows = analyse(code)
        json.dump(rows, open(os.path.join(ROOT, '%s_markscheme.json' % code), 'w'), indent=1)
        # validation: do per-paper tariffs sum to the published paper total?
        tot = collections.defaultdict(int)
        for r in rows:
            if r['marks']:
                tot[(r['series'], r['paper'], r['variant'])] += r['marks']
        vals = sorted(tot.values())
        print('%s blocks=%d cw=%d tariff=%d | per-paper tariff sums: median=%d  '
              'p10=%d p90=%d' % (code, len(rows),
                                 sum(1 for r in rows if r['cw']),
                                 sum(1 for r in rows if r['marks']),
                                 vals[len(vals)//2], vals[len(vals)//10],
                                 vals[(9*len(vals))//10]))
