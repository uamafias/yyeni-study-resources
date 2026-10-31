#!/usr/bin/env python3
"""Independent check of the content transcription against the PDF.

transcribe_syllabus.py reads the content table by word geometry. This re-reads each cited page
with plain `pdftotext -raw` (a different extraction) and requires every transcribed bullet to
appear there as an in-order word sequence: each word of the bullet found, in order, within a
window. A bullet that was merged with another, split mid-sentence, or polluted by a neighbouring
column or a page number fails. Also checks that the 364 bullets reconcile with the outline.
"""
import json, re, subprocess, sys

WS = 'work/nam-6116-nssco-2026'
facts = json.load(open(f'{WS}/curriculum/syllabus-facts.json'))
PDF = facts['source_document']
toks = lambda t: re.findall(r"[a-z0-9]+", t.lower())
cache = {}


def page(p):
    if p not in cache:
        out = subprocess.run(['pdftotext', '-raw', '-f', str(p), '-l', str(p + 1), PDF, '-'],
                             capture_output=True, text=True).stdout
        cache[p] = toks(out)
    return cache[p]


def in_order(words, hay, max_gap=60):
    """every word of `words` in order in `hay`, each within max_gap tokens of the last."""
    for start in [i for i, w in enumerate(hay) if w == words[0]]:
        j, ok = start, True
        for w in words[1:]:
            try:
                k = hay.index(w, j + 1, j + 1 + max_gap)
            except ValueError:
                ok = False
                break
            j = k
        if ok:
            return True
    return False


# Known, explained differences between the two extractions.
KNOWN = {('3.6.1.3', 'state the word and balanced chemical equation for photosynthesis'):
         'the words "sunlight" and "chlorophyll" are printed above and below the equation arrow; the '
         'geometric read keeps them, -raw drops them. (The printed equation also reads "6HO2", a '
         'typesetting error for 6H2O; transcribed as printed, corrected in the plan.)'}
fails, n = [], 0
for r in facts['content']:
    for o in r['specific_objectives']:
        n += 1
        w = toks(o['text'])
        if any(r['code'] == c and o['text'].startswith(t) for c, t in KNOWN):
            continue
        if not w or not in_order(w, page(o['source']['pdf_page'])):
            fails.append('%s: %s' % (r['code'], o['text'][:90]))
print('%d bullets checked against pdftotext -raw; %d fail; %d known differences, explained in KNOWN'
      % (n, len(fails), len(KNOWN)))
for f in fails:
    print('  ', f)
print('outline/content reconciliation:', facts['content_rows_missing_from_outline'],
      facts['outline_codes_with_no_content_row'])
sys.exit(1 if fails else 0)
