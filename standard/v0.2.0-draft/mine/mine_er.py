import glob, json, os, re, sys
CODE = sys.argv[1]

NOISE = re.compile(r'(©\s*UCLES|www\.cambridgeinternational|Cambridge IGCSE.*Principal Examiner|'
                   r'Principal Examiner Report for Teachers|^\s*Page \d+|^\s*\d+\s*$)', re.I)
# An ERROR statement: a candidate subject plus a failure signal. Positive statements are dropped -
# what a resource can act on is where learners lose marks, not where they succeed.
CAND = re.compile(r'\b(candidates?|answers?|responses?|scripts?|some|many|most|few|weaker)\b', re.I)
ERROR = re.compile(r"\b(did not|didn't|failed to|could not|were unable|unable to|struggl\w*|"
                   r"confus\w*|misunderstood|misunderst\w*|misread|misinterpret\w*|incorrect\w*|"
                   r"wrongly|erroneous|common error|omitted|omission|missed|lacked|lacking|"
                   r"insufficient|vague|generic|superficial|too brief|no development|undeveloped|"
                   r"simply (?:stated|listed|described)|merely|instead of|rather than|"
                   r"little evidence|not always|seldom|rarely)\b", re.I)
POSITIVE_ONLY = re.compile(r'^\s*(many|most|some|the majority of)?\s*(candidates|answers|responses)?'
                           r'\s*(were able to|correctly|successfully|did well|scored well|'
                           r'demonstrated good|showed good)', re.I)

out = []
for f in sorted(glob.glob(os.path.join(CODE, '%s_*_er*.txt' % CODE))):
    base = os.path.basename(f).replace('.txt', '')
    series = base.split('_')[1]
    raw = open(f, errors='ignore').read()
    raw = '\n'.join(l for l in raw.split('\n') if not NOISE.search(l))
    # rebuild paragraphs: a blank line ends one, every other newline is a wrap
    paras, qcur = [], None
    for para in re.split(r'\n\s*\n', raw):
        p = re.sub(r'\s*\n\s*', ' ', para).strip()
        p = re.sub(r'[ \t]{2,}', ' ', p)
        if p:
            paras.append(p)
    for p in paras:
        qm = re.match(r'^Question\s+(\d+)\s*(\([a-z]\))?\s*(\([ivx]+\))?', p)
        if qm:
            qcur = (qm.group(1) + (qm.group(2) or '') + (qm.group(3) or ''))
        for sent in re.split(r'(?<=[.!?])\s+(?=[A-Z(])', p):
            s = sent.strip()
            if not (55 <= len(s) <= 400):
                continue
            if not CAND.search(s) or not ERROR.search(s):
                continue
            if POSITIVE_ONLY.match(s) and not ERROR.search(s[:40]):
                continue
            out.append({'code': CODE, 'series': series, 'question': qcur,
                        'statement': s, 'source': base})
json.dump(out, open('%s_examiner_errors.json' % CODE, 'w'), indent=1)
print('%s: %d ERROR statements from %d reports' % (CODE, len(out), len(glob.glob(os.path.join(CODE, '%s_*_er*.txt' % CODE)))))
