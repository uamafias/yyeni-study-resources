# -*- coding: utf-8 -*-
"""Cambridge states its own scope limits inside the subject content.

"(formula and calculations of PED will not be assessed)", "Note: marginal cost
is not required." These are the real excluded_constructs - the board's own
boundary - and they beat any heuristic about which neighbouring topic owns a
word. This walks the content section, tracks the current topic, and captures
every stated limit against it.
"""
import json, os, re, collections
ROOT = os.path.expanduser('~/mine')

TOPIC = re.compile(r'^\s{5,}([1-6]\.\d{1,2})(?:\.\d{1,2})?\s{2,}\S')
SUBT  = re.compile(r'^\s{5,}([1-6]\.\d{1,2}\.\d{1,2})\s')
LIMIT = re.compile(
    r'((?:[A-Z(][^.\n]{0,200}?)?'
    r'(?:will not be (?:assessed|required|examined|tested)'
    r'|(?:is|are) not required'
    r'|(?:is|are) not (?:assessed|examined|expected|tested)'
    r'|no calculations? (?:are |is )?required'
    r'|Note: [^.\n]{0,120}? not required)[^.\n]{0,80})')
JUNK = re.compile(r'(Back to contents|cambridgeinternational\.org|syllabus for 2026)')

def run(code, start_pat, end_pat):
    lines = open(os.path.join(ROOT, '%s_syllabus.txt' % code),
                 encoding='utf-8', errors='ignore').read().split('\n')
    s = next(i for i, l in enumerate(lines) if re.match(start_pat, l))
    e = next(i for i, l in enumerate(lines) if i > s and re.match(end_pat, l))
    cur, out, buf = None, collections.defaultdict(list), []
    for ln in lines[s:e]:
        if JUNK.search(ln):
            continue
        m = SUBT.match(ln) or TOPIC.match(ln)
        if m:
            cur = m.group(1)
            if '.' in cur and cur.count('.') == 2:
                cur = '.'.join(cur.split('.')[:2])
        buf.append((cur, ln))
    # limits often wrap over two or three lines, so rebuild a rolling window
    for i, (tid, ln) in enumerate(buf):
        window = ' '.join(x[1] for x in buf[max(0, i - 2):i + 3])
        window = re.sub(r'\s+', ' ', window)
        for m in LIMIT.finditer(window):
            txt = re.sub(r'\s+', ' ', m.group(1)).strip()
            # Cambridge usually states the limit inside a parenthesis or after
            # 'Note:'. When it does, that clause is the exclusion; the run-up to
            # it is the objective, which belongs in scope, not out of it.
            par = txt.rfind('(')
            if par > 0 and re.search(r'(will not be|not required|not assessed)', txt[par:]):
                txt = txt[par + 1:]
            txt = txt.strip('( )').rstrip('0123456789 ').strip()
            # keep only a limit that names WHAT is excluded, not a bare verb phrase
            txt = re.sub(r'^Note:\s*', '', txt).strip()
            head = re.split(r'(will not be|is not|are not)', txt)[0].strip()
            if len(head) < 6:
                continue
            txt = txt[0].upper() + txt[1:]
            if txt.count('(') != txt.count(')'):
                txt = txt.replace('(', '').replace(')', '')
            txt = re.sub(r'\s-\s', '-', txt)
            if not txt.endswith('.'):
                txt += '.'
            if 20 < len(txt) < 230 and tid and txt not in out[tid]:
                out[tid].append(txt)
    # drop any entry that is contained in a longer entry for the same topic
    clean = {}
    for k, v in out.items():
        keep = [x for x in v if not any(x != y and x.lower().strip('.') in y.lower()
                                        for y in v)]
        if keep:
            clean[k] = keep
    return clean

WS = {'0450': 'work/cie-0450-igcse-2026', '0455': 'work/cie-0455-igcse-2026',
      '9609': 'work/cie-9609-as-2026-2028'}
# An AS workspace keeps only limits stated on AS topics (1-5 in 9609); the A Level
# topics have their own limits and belong to a different route.
ROUTE_MAX_UNIT = {'9609': 5}

if __name__ == '__main__':
    import sys
    codes = sys.argv[1:] or ['0450', '0455']
    for code in codes:
        sp, ep = r'^\s*3\s+Subject content\s*$', r'^\s*4\s+Details of the assessment'
        d = run(code, sp, ep)
        cap = ROUTE_MAX_UNIT.get(code)
        if cap:
            d = {k: v for k, v in d.items() if int(k.split('.')[0]) <= cap}
        REPO = os.path.expanduser('~/mnt/YYeni Study Resources')
        json.dump(d, open(os.path.join(REPO, WS[code], 'curriculum', 'syllabus-exclusions.json'), 'w'),
                  indent=1)
        json.dump(d, open(os.path.join(ROOT, 'out', '%s_syllabus_exclusions.json' % code), 'w'),
                  indent=1)
        print('\n%s  %d topics carry a stated limit' % (code, len(d)))
        for k in sorted(d, key=lambda x: [int(y) for y in x.split('.')]):
            for t in d[k]:
                print('   %-5s %s' % (k, t[:130]))
