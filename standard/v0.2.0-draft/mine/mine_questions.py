import glob, json, os, re, sys
from collections import Counter, defaultdict

CODE = sys.argv[1]
CW = ['Calculate','Consider','Define','Explain','Identify','Justify','Outline','State',
      'Analyse','Describe','Discuss','Give','Suggest','Using','Complete','Draw','Comment']
mark = re.compile(r'\[(\d+)\]')
# a question part line: optional number, a letter in brackets, optional roman, then text
QP = re.compile(r'^(?:(\d{1,2})\s+)?\(?([a-z])\)?\s*(?:\((i{1,3}|iv|v)\)\s*)?(.{10,})$')

recs = []
for f in sorted(glob.glob(os.path.join(CODE, '%s_*_qp_*.txt' % CODE))):
    base = os.path.basename(f).replace('.txt', '')
    _, sy, _, pv = base.split('_')
    series, yy, paper, variant = sy[0], sy[1:], pv[0], pv[1:]
    lines = open(f, errors='ignore').read().split('\n')
    pend, qno = None, None
    for ln in lines:
        s = ln.strip()
        if not s or 'UCLES' in s or 'brackets' in s or 'BLANK PAGE' in s:
            continue
        m = QP.match(s)
        if m:
            body = m.group(4).strip()
            cw = next((c for c in CW if re.match(r'%s\b' % c, body)), None)
            if cw:
                if m.group(1): qno = m.group(1)
                pend = {'code': CODE, 'series': series + yy, 'paper': paper, 'variant': variant,
                        'q': '%s(%s)%s' % (qno or '?', m.group(2),
                                           '(%s)' % m.group(3) if m.group(3) else ''),
                        'cw': cw, 'stem': re.sub(r'\s+', ' ', body)[:220], 'file': base}
                continue
        if pend:
            mm = mark.search(ln)
            if mm:
                pend['marks'] = int(mm.group(1))
                recs.append(pend); pend = None
json.dump(recs, open('%s_questions.json' % CODE, 'w'), indent=1)
print('%s: %d question parts mined from %d papers'
      % (CODE, len(recs), len(glob.glob(os.path.join(CODE, '%s_*_qp_*.txt' % CODE)))))
by = defaultdict(Counter)
for r in recs: by[r['cw']][r['marks']] += 1
print('\ncommand word -> tariffs (count)')
for c, cnt in sorted(by.items(), key=lambda x: -sum(x[1].values())):
    tot = sum(cnt.values())
    print('  %-10s %4d  %s' % (c, tot, ', '.join('%dm x%d' % (k, v) for k, v in sorted(cnt.items()))))
pp = defaultdict(Counter)
for r in recs: pp['P' + r['paper']][r['marks']] += 1
print('\nby paper: ')
for p, c in sorted(pp.items()):
    print('  %s  %s' % (p, dict(sorted(c.items()))))
