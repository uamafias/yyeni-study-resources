#!/usr/bin/env python3
"""Derive misconceptions, answer shapes and the scope scan from mined evidence.

Playbook step 3 items 4.7, 4.8 and 5. Subject-specific per step 4.2.

answer-shapes.json carries a hard limitation. The playbook asks what a creditable
answer looks like "from the mark schemes' structure", and NSSCO 6116 has no mark
schemes at all. What exists instead is indicative 'Answer:' text printed beside
some questions in the examiner reports: no tariff breakdown, no award grammar, no
band descriptors, present for only a subset of parts. Shapes are therefore
derived from observed tariff-to-command-word behaviour and labelled with the
evidence actually behind them. Nothing about marking is invented.
"""
import json, re, collections

WS = 'work/nam-6116-nssco-2026'
EV = f'{WS}/assessment-evidence'

facts = json.load(open(f'{WS}/curriculum/syllabus-facts.json'))
papers = json.load(open(f'{EV}/paper_evidence.json'))
reports = json.load(open(f'{EV}/examiner_evidence.json'))
parts, stmts = papers['question_parts'], reports['statements']

# --- misconceptions: examiner-evidenced only, never invented -----------------
mis = []
for s in stmts:
    if s['class'] in ('misconception', 'command-word miss'):
        mis.append({
            'misconception_id': f"MISCON-6116-{len(mis)+1:03d}",
            'class': s['class'],
            'proposed_sub_topic': s['proposed_sub_topic'],
            'mapping_confidence': s['mapping_confidence'],
            'evidence_statement': s['statement'],
            'evidence_source': {'examiner_report_year': s['year'], 'paper': s['paper'],
                                'question_ref': s['question_ref'],
                                'pdf_pages': s['source']['pdf_pages']},
            'curated': False,
            'discriminating_test': None,
        })
json.dump({'provenance': 'corpus',
           'rule': ('Every entry cites an examiner statement. None is invented. '
                    'curated=false: the playbook requires a curation pass to drop duplicates, '
                    'fragments and answering habits (0450 went 72 raw -> 29 real), and to write '
                    'the discriminating test for each. That pass has not run.'),
           'raw_count': len(mis), 'misconceptions': mis},
          open(f'{WS}/curriculum/misconceptions.json', 'w'), indent=2, ensure_ascii=False)

# --- answer shapes: tariff behaviour per command word ------------------------
shapes = {}
# 'direct question' marks a part asked as a question ("How many stomata ...?"): it has no command
# word, so it is not a word that could open a prompt.
for w in sorted({p['command_word'] for p in parts if p['command_word'] and p['command_word'] != 'direct question'}):
    ts = [p['mark_tariff'] for p in parts if p['command_word'] == w]
    by_paper = collections.Counter(p['paper'] for p in parts if p['command_word'] == w)
    shapes[w] = {
        'parts_seen': len(ts),
        'tariffs_seen': sorted(set(ts)),
        'modal_tariff': collections.Counter(ts).most_common(1)[0][0],
        'max_tariff': max(ts),
        'papers': dict(by_paper),
        'in_syllabus_glossary': w in {g['word'].lower().replace('/ ', '/')
                                      for g in facts['command_words']},
        'answer_structure': None,
        'evidence_for_structure': 'none - no mark schemes exist for this syllabus',
    }
json.dump({'provenance': 'corpus',
           'limitation': ('NO MARK SCHEMES EXIST for NSSCO 6116. answer_structure is null for every '
                          'command word because the evidence that would fix it does not exist. '
                          'Tariff behaviour below is measured from the papers. The examiner reports '
                          'print indicative answers for a subset of parts; those are partial and are '
                          'not award grammar. Marking guidance must not be invented from this file.'),
           'indicative_answer_blocks_available': reports['indicative_answer_blocks_seen'],
           'command_words': shapes},
          open(f'{WS}/curriculum/answer-shapes.json', 'w'), indent=2, ensure_ascii=False)

# --- scope scan: the syllabus's own stated limits ----------------------------
# Patterns are judgement (planning/scope_patterns.json); the limits are syllabus.
# Every stated limit must have exactly one pattern and every pattern must pass its
# own examples, or this stops: a limit recorded but not scannable is not enforced
# (build/make_contract.py), and a pattern that catches required content blocks
# authors on ordinary text (TEAM-PLAYBOOK section 8, C-11).
spec = json.load(open(f'{WS}/planning/scope_patterns.json'))
stated = facts['stated_exclusions']
entries, problems = [], []
for ex in stated:
    hits = [p_ for p_ in spec['patterns']
            if p_['sub_topic'] == ex['sub_topic'] and p_['limit_contains'] in ex['limit']]
    if len(hits) != 1:
        problems.append('%s "%s": %d patterns' % (ex['sub_topic'], ex['limit'], len(hits)))
        continue
    p_ = hits[0]
    rx = re.compile(p_['pattern'], re.I)
    problems += ['%s misses "%s"' % (p_['construct'], t) for t in p_['must_catch'] if not rx.search(t)]
    problems += ['%s wrongly catches "%s"' % (p_['construct'], t) for t in p_['must_leave_alone'] if rx.search(t)]
    if any(e_['construct'] == p_['construct'] for e_ in entries):
        continue                      # the same limit stated on two objectives
    entries.append({'construct': p_['construct'], 'pattern': p_['pattern'],
                    'source': {'authority': 'syllabus', 'sub_topic': ex['sub_topic'],
                               'printed_page': ex['printed_page'], 'pdf_page': ex['pdf_page'],
                               'quote': ex['quote']},
                    'must_catch': p_['must_catch'], 'must_leave_alone': p_['must_leave_alone'],
                    'pattern_provenance': 'judgement'})
if problems:
    raise SystemExit('scope patterns do not cover the stated limits:\n  ' + '\n  '.join(problems))
pats = entries
json.dump({'scan_id': 'SCOPE-6116', 'status': 'tested', 'rule': spec['rule'], 'entries': entries},
          open(f'{WS}/curriculum/scope-scan.json', 'w'), indent=2, ensure_ascii=False)
json.dump({'exclusions': [{'id': 'EXC-6116-%02d' % (i + 1), 'stated': ex['quote'],
                           'sub_topic': ex['sub_topic'], 'objective': ex['objective'],
                           'syllabus_page': ex['printed_page'], 'pdf_page': ex['pdf_page']}
                          for i, ex in enumerate(stated)]},
          open(f'{WS}/curriculum/syllabus-exclusions.json', 'w'), indent=2, ensure_ascii=False)

print(f"misconceptions.json : {len(mis)} raw examiner-evidenced entries (uncurated)")
print(f"answer-shapes.json  : {len(shapes)} command words, answer_structure null throughout (no mark schemes)")
print(f"scope-scan.json     : {len(pats)} stated exclusions")
