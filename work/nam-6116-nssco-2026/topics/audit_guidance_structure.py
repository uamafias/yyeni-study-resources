#!/usr/bin/env python3
"""Classify marking_guidance structure against mark_tariff for every item. Run from the repository root.

A list length that differs from the tariff is a review candidate, not an error: an "any three from" option list or
several explicit mark sentences in one entry can be valid. This script sorts the candidates so a person reviews the
unclear ones, and writes review/GUIDANCE-STRUCTURE-AUDIT.json.

Categories (first match wins):
  one_entry_per_mark       len(guidance) == tariff
  explicit_marks_in_entries  the entries state mark counts ("1 mark", "2 marks", "1 mark each") whose sum equals the tariff
  option_list              an "any N of / at least N / either / one from" rule, with N marks available
  review_unclear           none of the above; a person must read it
Also reports high-tariff (>= 4) and held items, which are reviewed whatever their category.
"""
import glob, json, re
from collections import Counter
from pathlib import Path

W = Path(__file__).resolve().parents[1]
NUM = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6}
rows, held = [], set()
for t in range(1, 6):
    held |= {v['item_id'] for v in json.loads((W / f'topics/{t}/authoring_notes.json').read_text()).get('visuals_pending', [])}
for t in range(1, 6):
    for f in sorted(glob.glob(str(W / f'topics/{t}/learning-items/*.json'))):
        for i in json.loads(Path(f).read_text())['items']:
            if i['item_type'] != 'flashcard':
                continue
            g = i['marking_guidance']; tariff = i['mark_tariff']; blob = ' '.join(g)
            marks = 0
            for m in re.finditer(r'\b(\d+) marks?\b(?: each)?', blob):
                marks += int(m.group(1))
            each = re.search(r'(\d+) marks? (?:each for|for each of) (?:any )?(one|two|three|four|five|six|\d)', blob)
            if each:
                n = NUM.get(each.group(2)) or int(each.group(2)); marks = int(each.group(1)) * n
            aw = re.search(r'\bAward (\d+) marks?\b', blob)
            if aw: marks = int(aw.group(1))
            anyn = re.search(r'\b(any|at least) (one|two|three|four|five|six)\b', blob, re.I)
            if len(g) == tariff:
                cat = 'one_entry_per_mark'
            elif marks == tariff:
                cat = 'explicit_marks_in_entries'
            elif anyn and (NUM[anyn.group(2).lower()] <= tariff):
                cat = 'option_list'
            else:
                cat = 'review_unclear'
            rows.append({'item_id': i['item_id'], 'topic': t, 'tariff': tariff, 'entries': len(g), 'stated_marks': marks,
                         'category': cat, 'held': i['item_id'] in held, 'high_tariff': tariff >= 4})
cnt = Counter(r['category'] for r in rows)
differs = [r for r in rows if r['entries'] != r['tariff']]
out = {'purpose': 'Structure screen of marking guidance against tariff. A difference is a review candidate, not a proven error.',
       'flashcards': len(rows), 'entries_differ_from_tariff': len(differs), 'by_category': dict(cnt),
       'differs_by_topic': dict(Counter(r['topic'] for r in differs)),
       'to_review': [r for r in rows if r['category'] == 'review_unclear' or r['held'] or (r['high_tariff'])],
       'all_rows': rows,
       'convention': 'One entry per mark is the default. An entry may state several explicit marks ("1 mark: ... 1 mark: ...") or an option rule ("1 mark each for any two of ..."). How YYeni displays multi-mark guidance has not been demonstrated; confirm in the real interface before release.'}
(W / 'review/GUIDANCE-STRUCTURE-AUDIT.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n')
print('flashcards', len(rows), '| entries differ from tariff', len(differs), '| categories', dict(cnt), '| to review', len(out['to_review']))
