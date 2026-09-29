# -*- coding: utf-8 -*-
"""Mine First Language English 0500 mark schemes.

0500 prints three things that between them define success in the subject:
  1. an item table per question: each item, the R/W sub-objectives it tests, its marks
  2. the task stem per item (what the candidate is told to do)
  3. level tables for every extended task, with what each band requires

Structure only is kept for learner-facing use. The level descriptors are recorded
so the analysis can say what separates one band from the next; no descriptor
wording is to reach a learner.
"""
import json, os, re, collections
ROOT = os.path.expanduser('~/mine')
SRC = os.path.join(ROOT, '0500')
JUNK = re.compile(r'(UCLES|Page \d+ of|PUBLISHED|Mark Scheme|www\.|Cambridge IGCSE|\[Turn over)')

ITEM_ROW = re.compile(r'^\s{0,4}(\d\s*\([a-z]\)(?:\s*\([ivx]+\))?|\d)\s{2,}((?:R|W)\d(?:(?:,\s*|\s+and\s+)(?:R|W)\d)*)\s{2,}(\d{1,2})\s*$')
STEM = re.compile(r'^\s{0,6}(\d\s*\([a-z]\)(?:\s*\([ivx]+\))?|\d|Section [AB])\s{2,}(\S.{8,}?)\s{2,}(\d{1,2})\s*$')
TABLE_HEAD = re.compile(r'(?:Table\s+([A-Z])\b[, ]*([A-Za-z &]+))?.*?give a mark out of (\d{1,2}) for ([A-Za-z &,]+)', re.I)
LEVEL_ROW = re.compile(r'^\s{0,4}(\d)\s{2,}(\d{1,2})\s*[–—-]\s*(\d{1,2})\s{2,}(\S.*)$|^\s{0,4}(\d)\s{2,}(\d{1,2})\s{3,}(\S.*)$')
TESTS = re.compile(r'This (?:question|section)\s+(?:also\s+|only\s+)?tests?\s+(?:the following\s+)?(reading|writing)\s+assessment objectives?\s+([RW\d,\sand]+?)\s*\((\d{1,2}) marks?\)', re.I)


def norm(s): return re.sub(r'\s+', ' ', s).strip()


def run():
    out = []
    for fn in sorted(os.listdir(SRC)):
        if '_ms_' not in fn:
            continue
        p = fn[:-4].split('_'); series, pv = p[1], p[3]
        raw = open(os.path.join(SRC, fn), encoding='utf-8', errors='ignore').read()
        lines = [l for l in raw.split('\n') if not JUNK.search(l)]
        items, stems, tables, tests = [], {}, [], []
        cur_q = None
        for i, ln in enumerate(lines):
            m = re.match(r'^\s*Question\s+(\d)\s*$', ln)
            if m:
                cur_q = m.group(1)
            m = re.match(r'^\s*Section\s+([AB])\b', ln)
            if m and pv[0] == '2':
                cur_q = m.group(1)
            m = ITEM_ROW.match(ln)
            if m:
                items.append({'item': re.sub(r'\s+', '', m.group(1)),
                              'objectives': re.findall(r'[RW]\d', m.group(2)),
                              'marks': int(m.group(3))})
                continue
            m = STEM.match(ln)
            if m and not re.match(r'^[RW]\d', m.group(2)):
                k = re.sub(r'\s+', '', m.group(1))
                st = norm(m.group(2))
                # carry the stem onto the next line when it wraps
                nxt = lines[i + 1].strip() if i + 1 < len(lines) else ''
                if nxt and not re.match(r'^(Award|Up to|Level|Table|\d)', nxt) and len(nxt) < 110:
                    st = norm(st + ' ' + re.sub(r'\s{3,}.*$', '', lines[i + 1]))
                if k not in stems:
                    stems[k] = {'item': k, 'stem': st[:220], 'marks': int(m.group(3)), 'q': cur_q}
            for t in TESTS.finditer(norm(ln + ' ' + (lines[i + 1] if i + 1 < len(lines) else ''))):
                tests.append({'q': cur_q, 'kind': t.group(1).lower(),
                              'objectives': re.findall(r'[RW]\d', t.group(2)),
                              'marks': int(t.group(3))})
            # a level table starts at its own 'Level  Marks ...' header; its name and
            # its out-of are read from the few lines above it
            if re.match(r'^\s*Level\s+Marks\b', ln):
                label, out_of, tname = None, None, None
                for back in lines[max(0, i - 14):i][::-1]:
                    h = TABLE_HEAD.search(back)
                    if h and out_of is None:
                        out_of, label = int(h.group(3)), norm(h.group(4)).strip(' ,.')
                    t2 = re.search(r'Table\s+([A-Z])\b[,:]?\s*([A-Za-z &]{3,40})', back)
                    if t2 and tname is None:
                        tname = (t2.group(1), norm(t2.group(2)))
                    if out_of and tname:
                        break
                tbl = {'q': cur_q, 'table': tname[0] if tname else None,
                       'name': tname[1] if tname else None,
                       'for': label or (tname[1].lower() if tname else None),
                       'out_of': out_of, 'levels': []}
                lvl = None
                for ln2 in lines[i + 1:i + 110]:
                    if re.match(r'^\s*Level\s+Marks\b', ln2):
                        break
                    r = LEVEL_ROW.match(ln2)
                    if r:
                        if r.group(1):
                            lvl = {'level': int(r.group(1)), 'lo': int(r.group(2)),
                                   'hi': int(r.group(3)), 'desc': norm(r.group(4))}
                        else:
                            lvl = {'level': int(r.group(5)), 'lo': int(r.group(6)),
                                   'hi': int(r.group(6)), 'desc': norm(r.group(7))}
                        tbl['levels'].append(lvl)
                        if lvl['level'] == 0:
                            break
                        continue
                    if lvl and ln2.strip():
                        lvl['desc'] = norm(lvl['desc'] + ' ' + ln2)
                for L in tbl['levels']:
                    L['desc'] = re.sub(r'\s*[\u2022\uf0b7]\s*', ' | ', L['desc']).strip(' |')
                if tbl['out_of'] is None and tbl['levels']:
                    tbl['out_of'] = max(L['hi'] for L in tbl['levels'])
                if tbl['levels']:
                    tables.append(tbl)
        out.append({'series': series, 'paper': pv[0], 'variant': pv[1:], 'file': fn[:-4],
                    'items': items, 'stems': list(stems.values()), 'tests': tests, 'tables': tables})
    return out


if __name__ == '__main__':
    rows = run()
    json.dump(rows, open(os.path.join(ROOT, '0500_markscheme.json'), 'w'), indent=1)
    for pap in ('1', '2'):
        rs = [r for r in rows if r['paper'] == pap]
        print('Paper %s: %d schemes | with item tables %d | with level tables %d | stems %d'
              % (pap, len(rs), sum(1 for r in rs if r['items']), sum(1 for r in rs if r['tables']),
                 sum(len(r['stems']) for r in rs)))
        tot = collections.Counter(sum(i['marks'] for i in r['items']) for r in rs if r['items'])
        print('   item-table totals across schemes:', dict(tot.most_common(5)))
