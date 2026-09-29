# -*- coding: utf-8 -*-
"""Mine AS Business 9609 mark schemes.

9609 states its answer architecture more explicitly than the IGCSE syllabuses do.
Every question opens with a grid: one column per assessment objective, the marks
available in each, and the band descriptor that earns them. So the answer shape
is not inferred from award wording - it is read straight off the grid.

The grid is a table flattened into text, so an AO's name and its mark count land
on different lines in the same column. They are paired by column position.
"""
import json, os, re, collections

ROOT = os.path.expanduser('~/mine')
SRC = os.path.join(ROOT, '9609')

# Paper 1 question 4 is a single five-mark part with no letter, so the part
# letter is optional. Requiring it silently dropped every Analyse 5 question.
QID = re.compile(r'^(\s{2,14})(\d{1,2}(?:\s*\([a-z]\))?(?:\s*\([ivx]+\))?)\s{2,}([A-Z]\S.*)$')
CW = re.compile(r'^\s*(Define|Explain|Identify|State|Calculate|Analyse|Evaluate|'
                r'Assess|Advise|Justify|Briefly explain|Outline|Describe)\b', re.I)
JUNK = re.compile(r'(UCLES|Page \d+ of|PUBLISHED|Cambridge International|Mark Scheme|'
                  r'GENERIC MARKING|^\s*Question\s+Answer\s+Marks)')
AO_TOK = re.compile(r'AO(\d)\b')
MK_TOK = re.compile(r'(?<![\d.])(\d{1,2})\s+marks?\b')
BAND = re.compile(r'(\d+)\s*[–—-]\s*(\d+)\s*marks?\s*(.{0,90})')
MARKCELL = re.compile(r'\s{3,}(\d{1,2})(?:\s|$)')


def norm(s):
    return re.sub(r'\s+', ' ', s).strip()


def blocks(lines):
    out, cur, key = [], [], None
    for ln in lines:
        if JUNK.search(ln):
            continue
        m = QID.match(ln)
        if m:
            if key:
                out.append((key, cur))
            key, cur = re.sub(r'\s+', '', m.group(2)), [ln]
            continue
        if key is not None:
            cur.append(ln)
    if key:
        out.append((key, cur))
    return out


def tariff(chunk):
    for ln in chunk[:3]:
        for m in MARKCELL.finditer(ln):
            if m.start(1) >= 70:
                v = int(m.group(1))
                if 1 <= v <= 20:
                    return v
    return None


def grid(chunk):
    """Marks per assessment objective. Three layouts, one answer.

    9609 mark schemes changed shape twice over the corpus:

      list    (2020-2022)  no AO attribution at all, just "(2 marks)" bands
      table   (2023-2024)  a grid, AO names across one header row and the marks
                           beneath each in its own column
      inline  (2024-2025)  AO name on its own line, "2 marks for DEVELOPED
                           application ..." on the lines under it

    The table is read by column position; the inline form by segmenting the
    block at each AO heading. Both are the same fact - how many marks each
    objective carries - so both are read rather than one being preferred.
    """
    lines = list(chunk)
    multi = [ln for ln in lines if len(set(AO_TOK.findall(ln))) >= 2]

    if multi:                                   # table layout
        region = []
        for ln in lines:
            if 'Indicative content' in ln:
                break
            region.append(ln)
        aos, marks = [], []
        for ln in region:
            for m in AO_TOK.finditer(ln):
                aos.append(('AO%s' % m.group(1), m.start()))
            for m in MK_TOK.finditer(ln):
                marks.append((int(m.group(1)), m.start()))
        seen = {}
        for code, col in aos:
            seen.setdefault(code, col)
        out, used = {}, set()
        for code, col in sorted(seen.items(), key=lambda kv: kv[1]):
            best, bd = None, 10 ** 9
            for k, (v, mc) in enumerate(marks):
                if k in used:
                    continue
                d = abs(mc - col)
                if d < bd:
                    best, bd = k, d
            if best is not None and bd <= 45:
                used.add(best)
                out[code] = marks[best][0]
        layout = 'table'
    else:                                       # inline layout
        segs, cur, code = [], [], None
        for ln in lines:
            m = AO_TOK.search(ln)
            if m and len(ln.strip()) < 60:
                if code:
                    segs.append((code, cur))
                code, cur = 'AO%s' % m.group(1), []
                continue
            if code:
                cur.append(ln)
        if code:
            segs.append((code, cur))
        out = {}
        for c, body in segs:
            vals = [int(x) for x in MK_TOK.findall(' '.join(body[:12]))]
            if vals:
                out[c] = max(out.get(c, 0), max(vals))
        layout = 'inline' if out else 'list'

    flat = norm(' '.join(lines))
    bands = [{'lo': int(a), 'hi': int(b), 'descriptor': norm(c)[:80]}
             for a, b, c in BAND.findall(flat)]
    return out, bands, layout


def merge(bs):
    """A question that runs over a page break reappears under the same id.

    Each reappearance carries only part of the AO grid, so the parts are joined
    before the grid is read. The tariff is taken from the first appearance,
    which is the one that carries the Marks cell.
    """
    out, order = {}, []
    for qid, chunk in bs:
        if qid not in out:
            out[qid] = list(chunk)
            order.append(qid)
        else:
            out[qid].extend(chunk)
    return [(q, out[q]) for q in order]


def run():
    rows = []
    for fn in sorted(os.listdir(SRC)):
        if '_ms_' not in fn or not fn.endswith('.txt'):
            continue
        p = fn[:-4].split('_')
        series, pv = p[1], p[3]
        lines = open(os.path.join(SRC, fn), encoding='utf-8', errors='ignore').read().split('\n')
        for qid, chunk in merge(blocks(lines)):
            m = QID.match(chunk[0])
            stem = norm(m.group(3)) if m else ''
            stem = re.sub(r'\s{3,}\d{1,2}\s*$', '', stem)
            cw = CW.match(stem)
            if not cw:
                # "Refer to Table 2.1 and other information. Calculate ..." -
                # the command word is the first one after the stimulus pointer,
                # which can itself contain full stops ("Fig. 1.1").
                rm = re.search(r'\b(Define|Explain|Identify|State|Calculate|Analyse|'
                               r'Evaluate|Assess|Advise|Justify)\b', stem)
                if stem.lower().startswith('refer') and rm:
                    cw = rm
            g, bands, layout = grid(chunk)
            t = tariff(chunk)
            rows.append({'code': '9609', 'series': series, 'paper': pv[0], 'variant': pv[1:],
                         'qid': qid, 'stem': stem[:200],
                         'cw': cw.group(1).title() if cw else None,
                         'marks': t, 'ao_marks': g, 'ao_total': sum(g.values()) or None,
                         'bands': bands[:6], 'ms_layout': layout, 'file': fn[:-4]})
    return rows


if __name__ == '__main__':
    rows = run()
    json.dump(rows, open(os.path.join(ROOT, '9609_markscheme.json'), 'w'), indent=1)
    tot = collections.defaultdict(int)
    for r in rows:
        if r['marks']:
            tot[(r['series'], r['paper'], r['variant'])] += r['marks']
    v = sorted(tot.values())
    p1 = sorted(x for k, x in tot.items() if k[1] == '1')
    p2 = sorted(x for k, x in tot.items() if k[1] == '2')
    print('blocks %d | cw %d | tariff %d | AO grid %d'
          % (len(rows), sum(1 for r in rows if r['cw']),
             sum(1 for r in rows if r['marks']),
             sum(1 for r in rows if r['ao_marks'])))
    print('paper totals: P1 median %s (should be 40), P2 median %s (should be 60)'
          % (p1[len(p1) // 2] if p1 else '-', p2[len(p2) // 2] if p2 else '-'))
    agree = sum(1 for r in rows if r['marks'] and r['ao_total'] == r['marks'])
    both = sum(1 for r in rows if r['marks'] and r['ao_total'])
    print('AO grid sums to the tariff on %d/%d questions (%.0f%%)'
          % (agree, both, 100.0 * agree / max(both, 1)))
