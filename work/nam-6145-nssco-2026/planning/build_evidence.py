"""Build 6145 evidence from inspected QPs, reports and human semantic mappings."""
import collections
import json
import re
from pathlib import Path

WS = Path(__file__).resolve().parents[1]
OUT = WS / 'assessment-evidence'
CURR = WS / 'curriculum'
load = lambda p: json.loads(p.read_text())
dump = lambda p, x: p.write_text(json.dumps(x, indent=2, ensure_ascii=False) + '\n')
facts = load(CURR / 'syllabus-facts.json')
records = load(OUT / 'question-parts-draft.json')
findings = load(OUT / 'report-findings-draft.json')
blocks = load(OUT / 'report-blocks.json')
maps = load(WS / 'planning/semantic-mappings.json')
misconceptions = load(WS / 'planning/curated-misconceptions.json')
anomalies = load(WS / 'planning/source-anomalies.json')

index = {}
for theme in facts['content_outline']:
    for topic in theme['topics']:
        for i, obj in enumerate(topic['specific_objectives'], 1):
            key = f"{topic['topic_id']}-{i:02d}"
            index[key] = {'objective_id': 'OBJ-6145-' + key,
                          'topic_id': topic['topic_id'], 'topic_title': topic['title'],
                          'syllabus_text': obj['verbatim'], 'source': obj,
                          'id_status': 'Syllabus bullet anchor; planner must preserve or explicitly crosswalk during list decomposition.'}
dump(OUT / 'syllabus-objective-index.json', {'objectives': list(index.values())})

grouped = collections.defaultdict(list)
for r in records:
    grouped[r['source_id']].append(r)
for sid, rows in grouped.items():
    assert len(rows) == len(maps[sid]), sid
    for r, mapping in zip(rows, maps[sid]):
        keys = mapping.split('+')
        assert all(k in index for k in keys), (sid, keys)
        r['objective_ids'] = [index[k]['objective_id'] for k in keys]
        r['primary_objective_id'] = r['objective_ids'][0]
        r['topic_id'] = index[keys[0]]['topic_id']
        r['mapping_method'] = 'Semantic reading of the question demand and context by Codex; explicit per-part mapping in planning/semantic-mappings.json. No keyword/token matching.'
        note = maps['mapping_notes'].get(sid + ':' + r['question_ref'])
        r['mapping_confidence'] = 'low' if note and 'Low confidence' in note else 'supporting_or_cross_cutting' if note else 'high'
        r['mapping_note'] = note
        r['mapping_provenance'] = 'judgement'

lookup = {r['source_id'] + ':' + r['question_ref']: r for r in records}
miscon_refs = collections.defaultdict(list)
for i, m in enumerate(misconceptions, 1):
    m['misconception_id'] = f'MISCON-6145-{i:03d}'
    m['correct_understanding'] = m.pop('boundary')
    m['discriminating_test'] = m.pop('test')
    m['objective_ids'] = ['OBJ-6145-' + x for x in m.pop('objectives')]
    m['topic_id'] = '.'.join(m['objective_ids'][0].split('-')[2].split('.')[:2])
    m['evidence_ids'] = [lookup[k]['evidence_id'] for k in m['refs']]
    m['evidence_locators'] = [{'finding_id': f['finding_id'], 'source_locator': f['source_locator']} for f in findings if f"{f['year']}-P{f['paper_id']}:{f['question_ref']}" in m['refs']]
    m['evidence_basis'] = 'Examiner performance comments, semantically read and curated; definitions/check questions are original judgement, not official answer wording.'
    m['provenance'] = 'corpus'
    for k in m['refs']:
        miscon_refs[k].append(m['misconception_id'])

by_question_findings = collections.defaultdict(list)
for f in findings:
    key = f"{f['year']}-P{f['paper_id']}:{f['question_ref']}"
    # The report comments on the two parts of Q11 together.
    targets = [key] if key in lookup else ['2021-P1:11(a)', '2021-P1:11(b)'] if key == '2021-P1:11' else []
    assert targets, key
    f['evidence_ids'] = [lookup[k]['evidence_id'] for k in targets]
    f['objective_ids'] = sorted({o for k in targets for o in lookup[k]['objective_ids']})
    f['misconception_ids'] = sorted({m for k in targets for m in miscon_refs[k]})
    text = f['verbatim_internal'].lower()
    categories = []
    if f['misconception_ids']:
        categories.append('misconception')
    if re.search(r'listing|listed|development|develop|one.sid|both sides|conclusion|decision|link|repeating|mirror effect', text):
        categories.append('shallow development')
    if re.search(r'instead|rather|misinterpret|interpret.*question|question.*interpret|command|formula.*definition|definition.*formula|copied|statements instead', text):
        categories.append('command-word miss')
    if re.search(r'could not|cannot|failed|omitt|missing|left out|not know|lack.*knowledge|lack.*content|lost marks|did not|unable|could only', text):
        categories.append('omission')
    f['classifications'] = categories or ['performance observation']
    f['classification_provenance'] = 'judgement from the quoted report comment; genuine concept confusions are separately curated.'
    f['source_anomalies'] = [a['id'] for a in anomalies if a['source_id'] == f"{f['year']}-ER" and f['source_locator']['pdf_page'] in a['pdf_pages']]
    for k in targets:
        by_question_findings[k].append(f)

block_lookup = {(b['year'], b['paper_id'], b['question_ref']): b for b in blocks}
opening_overrides = {
 '2020-P1:8':'which','2020-P1:24(b)(iii)':'explain',
 '2020-P2:1(b)':'illustrate',
 '2021-P1:24(a)(i)':'comment','2021-P1:24(a)(ii)':'comment','2021-P1:25(c)':'discuss',
 '2021-P2:1(b)':'use',
 '2022-P1:3':'what','2022-P1:9':'which','2022-P1:13':'what','2022-P1:17':'which','2022-P1:24':'describe','2022-P1:26(c)':'suggest',
 '2022-P2:1(b)':'use','2022-P2:5(b)':'use','2022-P2:6(b)':'analyse','2022-P2:6(c)':'evaluate',
 '2023-P1:18':'which','2023-P1:1':'describe','2023-P1:9':'identify','2023-P1:10':'name','2023-P1:11':'what','2023-P1:14':'what','2023-P1:15':'explain','2023-P1:22':'identify','2023-P1:24':'how','2023-P1:25(d)':'what',
 '2024-P1:9':'show','2024-P1:17':'how','2024-P1:23(c)':'suggest',
 '2024-P2:1(a)':'outline','2024-P2:4(a)':'name'
}

SHAPES = {
 'definition': 'Give the essential distinguishing features of the term; include qualifiers such as price adjustment, per head, time period or the next-best alternative when needed. An example alone is not automatically a definition.',
 'list': 'Supply the requested number of distinct relevant points. Obey the named actor and any exclusion in the question; do not substitute a definition for reasons or types.',
 'formula': 'State the complete formula with the correct numerator and denominator. Percentage changes belong inside elasticity ratios; elasticity itself is a coefficient, not a percentage.',
 'calculation': 'Select relevant data, state the method, substitute values and report the correct magnitude and units. Follow the actual request for working; do not assume every task awards a separate method mark.',
 'diagram_selection': 'Read the initial equilibrium and the specified cause, select the correct curve/change and identify the requested outcome; use the figure rather than a memorised direction.',
 'diagram_only': 'Draw the required initial situation, correct shift or binding price, relevant new equilibrium/imbalance and complete labels. Do not count an unrequested prose answer as a substitute for the diagram.',
 'diagram_analysis': 'Provide a correct labelled diagram and explain the stated mechanism in words, naming the curve or control and the resulting price/quantity or shortage/surplus. Mark splits are task-specific.',
 'comparison': 'State the distinguishing basis for both concepts or groups and connect the comparison to the named situation. Avoid giving two unrelated definitions without the requested contrast.',
 'two_sided_evaluation': 'Develop the relevant case for and against the proposition, apply it to the named context, and make a supported judgement where requested/evidenced. Opposite wording of the same undeveloped point is not a new argument.',
 'focused_evaluation': 'Develop reasons or consequences relevant to the particular aim, decision or actor. A reason-selection task is not automatically a debate; use the exact task-specific report guidance.',
 'multi_element': 'Cover every requested component of the answer and connect them where a link is asked for; do not earn apparent breadth by repeating one element.',
 'causal_analysis': 'Identify the relevant factor, state the direction of change, and develop the economic mechanism to the specified outcome and actor. Refer to the supplied evidence when required.',
 'enquiry_design': 'Frame original questions that would obtain evidence about the stated economic costs. Cover the named affected groups; statements describing accidents do not meet a request for enquiry questions.'
}
two_sided = {
 '2020-P1:23(e)','2020-P1:24(c)','2020-P2:1(c)','2020-P2:5(d)',
 '2021-P1:24(b)','2021-P2:6(d)',
 '2022-P1:25(d)','2022-P2:1(d)','2022-P2:3(c)','2022-P2:4(c)',
 '2023-P1:26(c)','2023-P1:26(d)','2023-P2:1(e)','2023-P2:2(c)',
 '2023-P2:3(c)','2023-P2:4(c)','2023-P2:5(c)','2023-P2:6(d)',
 '2024-P1:24(d)','2024-P2:1(b)','2024-P2:2(d)','2024-P2:4(d)','2024-P2:5(d)'
}
focused_evaluation = {
 '2020-P1:23(c)','2021-P1:25(b)','2021-P1:25(c)','2021-P2:1(c)','2021-P2:2(b)','2021-P2:2(c)',
 '2022-P1:25(c)','2022-P1:26(c)','2022-P1:26(d)','2022-P2:1(c)',
 '2022-P2:2(c)','2022-P2:5(c)','2022-P2:6(c)','2023-P1:25(c)',
 '2024-P1:23(b)','2024-P1:23(c)','2024-P2:1(d)','2024-P2:3(d)',
 '2024-P2:6(d)'
}
multi_element = {'2021-P1:24(c)','2023-P2:2(a)','2023-P2:2(b)','2020-P2:5(c)'}
shape_usage = collections.defaultdict(list)
for r in records:
    key = r['source_id'] + ':' + r['question_ref']
    stem = r['stem_internal'].lower()
    first = re.search(r'[a-z]+', stem)[0]
    r['command_word'] = opening_overrides.get(key, 'use' if first == 'using' else 'what' if first == 'to' else 'write down' if first == 'write' else first)
    r['command_word_provenance'] = 'corpus; normalise Using to Use; where a context/condition precedes the instruction, count the operative opening, not the context words.'
    r['secondary_directives'] = sorted(set(re.findall(r'\b(?:analyse|calculate|define|describe|discuss|evaluate|explain|give|identify|justify|outline|state|suggest|draw|illustrate|show)\b', stem)) - {r['command_word']})
    r['command_family'] = 'interrogative' if r['command_word'] in {'what','who','why','which','how','when','is','to'} else 'directive'
    r['context_type'] = ('short recall/application' if r['paper_id'] == '1' and r['section'] == 'A' else 'economic case/data interpretation')
    r['context_constraints'] = []
    if 'except' in stem or 'other than' in stem:
        r['context_constraints'].append('Exclude the examples/factors explicitly ruled out by this question.')
    if any(x in stem for x in ('extract', 'table', 'article', 'information', 'this business', 'this company')):
        r['context_constraints'].append('Use the specified source/context; generic facts alone may not meet the demand.')
    if 'formula' in stem:
        family = 'formula'
    elif key == '2023-P1:25(d)':
        family = 'enquiry_design'
    elif 'diagram' in stem:
        if key in {'2020-P1:8','2022-P1:9','2022-P1:10'}:
            family = 'diagram_selection'
        elif key in {'2020-P1:23(a)(ii)','2022-P1:26(b)','2024-P1:9'}:
            family = 'diagram_only'
        else:
            family = 'diagram_analysis'
    elif key in {'2020-P1:23(b)(ii)','2020-P1:24(b)(ii)','2021-P1:25(a)(i)','2022-P1:13','2023-P1:14','2023-P1:25(b)','2023-P2:1(c)','2024-P1:17'}:
        family = 'calculation'
    elif key in two_sided:
        family = 'two_sided_evaluation'
    elif key in focused_evaluation:
        family = 'focused_evaluation'
    elif key in multi_element:
        family = 'multi_element'
    elif 'difference' in stem or 'distinguish' in stem or key == '2022-P2:2(a)':
        family = 'comparison'
    elif r['command_word'] == 'define' or re.search(r'\bmeaning\b|what is meant|to what does', stem):
        family = 'definition'
    elif r['command_word'] in {'list','name','state','identify','mention','indicate','write down'} and not (r['command_word'] == 'identify' and 'explain' in stem):
        family = 'list'
    else:
        family = 'causal_analysis'
    r['answer_shape_id'] = 'SHAPE-6145-' + family
    shape_usage[family].append(r)
    r['ao_focus'] = ['C'] if family in {'two_sided_evaluation','focused_evaluation','enquiry_design'} else ['B'] if family in {'calculation','diagram_analysis','diagram_only','diagram_selection','causal_analysis','comparison','multi_element'} and not (r['paper_id'] == '1' and r['section'] == 'A') else ['A']
    r['ao_focus_provenance'] = 'judgement about task demand; not an exact official per-part AO split. Syllabus per-paper targets remain authoritative.'
    r['examiner_findings'] = [f['finding_id'] for f in by_question_findings[key]]
    r['common_errors'] = [{'finding_id': f['finding_id'], 'classifications': f['classifications']}
                          for f in by_question_findings[key] if f['classifications'] != ['performance observation']]
    r['misconception_ids'] = miscon_refs[key]
    block = block_lookup.get((r['year'], r['paper_id'], r['question_ref']))
    # Parent report comment covers two independent short-answer parts.
    if not block and key in {'2021-P1:11(a)', '2021-P1:11(b)'}:
        block = block_lookup[(2021, '1', '11')]
    # Q4(d) in 2020 P2 has guidance, but no separate performance comment.
    if not block and key == '2020-P2:4(d)':
        block = block_lookup[(2020, '2', '4(c)')]
    r['creditworthy_points'] = []
    r['credit_evidence_status'] = 'no standalone MS; report guidance used' if block else 'no per-part report guidance located'
    r['strong_response_features'] = [SHAPES[family]] + r['context_constraints']
    if block and not (r['source_id'] == '2020-P1' and r['section'] == 'B'):
        r['creditworthy_points'].append({'shape': SHAPES[family], 'provenance': 'judgement distilled from corpus answer/guidance; no official wording reproduced',
                                         'report_block_id': block['block_id'], 'source_locator': block['source_locator'],
                                         'allocation_warning': 'Use specific source guidance for allocations. This family description does not assert one mark per sentence or an identical split across all questions.'})
    elif r['source_id'] == '2020-P1' and r['section'] == 'B':
        r['credit_evidence_status'] = 'performance comment only; no full answer/marking grid in report for this part'
    r['source_anomalies'] = [a['id'] for a in anomalies if a['source_id'] == f"{r['year']}-ER" and any(f['source_locator']['pdf_page'] in a['pdf_pages'] for f in by_question_findings[key])]
    r['notes'] = ['Internal source stems are for audit only; all learner scenarios and solutions must be newly authored.']
    if r['mapping_note']:
        r['notes'].append(r['mapping_note'])

# Every raw examiner performance comment is retained; pure positive observations
# are not inflated into learner mistakes. Split compound observations at sentences
# for an auditable statement inventory, inheriting the reviewed paragraph mapping.
statements = []
for f in findings:
    for i, sentence in enumerate(re.split(r'(?<=[.!?])\s+(?=[A-Z])', f['verbatim_internal']), 1):
        statements.append({'statement_id': f"{f['finding_id']}-S{i:02d}",
                           'finding_id': f['finding_id'], 'verbatim_internal': sentence,
                           'source_locator': f['source_locator'], 'objective_ids': f['objective_ids'],
                           'classifications': f['classifications'],
                           'classification_note': 'Paragraph-level classifications inherited; sentence spans preserve the original observation without claiming every sentence is an independent misconception.'})
dump(OUT / 'examiner-findings.json', {'findings': findings, 'statements': statements,
     'note': 'Question-specific performance observations; general teaching recommendations are retained in selected report-page extracts and synthesised in the analysis, not counted as pupil misconceptions.'})
dump(OUT / 'assessment_evidence.json', {'evidence_id': 'EVIDENCE-NAM-6145-NSSCO-2026',
     'mapping_method': maps['method'], 'records': records,
     'not_learner_facing': True, 'part_count': len(records),
     'marks_offered': sum(r['mark_tariff'] for r in records)})
dump(CURR / 'misconceptions.json', {'misconceptions': misconceptions,
     'curation': 'Genuine conceptual distinctions only. Omission, weak development, answering a neighbouring question, unit errors and copying the extract are handled separately. No invented errors are labelled examiner-evidenced.'})
dump(OUT / 'source-anomalies.json', {'anomalies': anomalies})

# Exact coverage is generated, never typed. First mapping owns marks; secondary
# links contribute exposure counts but never double-count the headline mark share.
objective_rows = []
for key, obj in index.items():
    rows = [r for r in records if obj['objective_id'] in r['objective_ids']]
    primary = [r for r in rows if r['primary_objective_id'] == obj['objective_id']]
    series = sorted({r['exam_series'] for r in rows})
    n = len(series)
    objective_rows.append({**obj, 'times_examined': len(rows), 'marks_examined': sum(r['mark_tariff'] for r in primary),
       'marks_linked_including_secondary': sum(r['mark_tariff'] for r in rows),
       'series': series, 'series_spread': n,
       'max_tariff': max((r['mark_tariff'] for r in rows), default=0),
       'command_words': dict(collections.Counter(r['command_word'] for r in rows)),
       'tariffs': dict(collections.Counter(r['mark_tariff'] for r in rows)),
       'evidence_ids': [r['evidence_id'] for r in rows],
       'exposure_class': 'core' if n >= 4 else 'frequent' if n == 3 else 'occasional' if n == 2 else 'rare' if n == 1 else 'unseen'})
topic_rows = []
for th in facts['content_outline']:
    for t in th['topics']:
        rows = [r for r in records if r['topic_id'] == t['topic_id']]
        topic_rows.append({'topic_id': t['topic_id'], 'title': t['title'], 'question_parts': len(rows),
                          'primary_marks_offered': sum(r['mark_tariff'] for r in rows),
                          'share_of_offered_marks_percent': round(sum(r['mark_tariff'] for r in rows) / 10, 1),
                          'series': sorted({r['year'] for r in rows}),
                          'evidence_ids': [r['evidence_id'] for r in rows]})
dump(CURR / 'exam-exposure.json', {'exposure_id': 'EXPOSURE-NAM-6145-NSSCO-2026',
     'status': 'measured', 'principle': 'Exposure calibrates emphasis, never removes any syllabus outcome.',
     'denominator': {'offered_marks': 1000, 'candidate_marks_across_five_years': 800,
                     'note': 'Paper 2 offers 120 but candidate answers 80 each year. Offered-topic share is not an estimate of learner choice or future probability.'},
     'exposure_class_definitions': {'core': '4–5 distinct annual series', 'frequent': '3 annual series', 'occasional': '2 annual series', 'rare': '1 annual series', 'unseen': '0 observed in this held corpus'},
     'method': 'Recomputed from semantic question-part mappings. Primary mapping owns marks; secondary links contribute objective exposure only. Five series is the full window, so thresholds are explicitly calibrated to that window.',
     'objective_registry_status': 'Pre-plan syllabus bullet anchors; decomposition requires an explicit crosswalk, never a token rematch.',
     'unmatched_parts': 0, 'uncertain_mapping_parts': [r['evidence_id'] for r in records if r['mapping_confidence'] != 'high'],
     'objectives': objective_rows, 'topics': topic_rows})

syllabus_words = {x['word'] for x in facts['command_words']}
command_rows = []
for word in sorted(syllabus_words | {r['command_word'] for r in records}):
    rows = [r for r in records if r['command_word'] == word]
    tariffs = collections.Counter(r['mark_tariff'] for r in rows)
    highest_count = max(tariffs.values(), default=0)
    modes = sorted(t for t, count in tariffs.items() if count == highest_count)
    command_rows.append({'word': word, 'in_syllabus_table': word in syllabus_words,
                         'count': len(rows), 'tariffs': dict(sorted(tariffs.items())), 'modal_tariffs': modes,
                         'papers': sorted({r['paper_id'] for r in rows}),
                         'verdict': 'listed_not_observed' if not rows else 'observed_listed' if word in syllabus_words else 'observed_not_listed',
                         'use_in_prompts': bool(rows),
                         'evidence_ids': [r['evidence_id'] for r in rows],
                         'note': 'Interrogative framing, not a standalone command-word definition.' if rows and all(r['command_family'] == 'interrogative' for r in rows) else None})
dump(OUT / 'command-word-analysis.json', {'method': 'One primary opening per independently tariffed part; embedded instructions are retained in secondary_directives but not double-counted. Context/Except/With the help prefaces are ignored; Use and Using are normalised to Use. Interrogatives are explicitly separated from imperative verbs.',
    'count': len(records), 'commands': command_rows,
    'secondary_directives': {w: {'count': sum(w in r['secondary_directives'] for r in records), 'tariffs': sorted({r['mark_tariff'] for r in records if w in r['secondary_directives']}), 'evidence_ids': [r['evidence_id'] for r in records if w in r['secondary_directives']]} for w in sorted({w for r in records for w in r['secondary_directives']})}})

shape_rows = []
for name, rows in sorted(shape_usage.items()):
    shape_rows.append({'shape_id': 'SHAPE-6145-' + name, 'name': name,
                       'architecture': SHAPES[name], 'provenance': 'judgement from cited question/report evidence',
                       'observed_command_tariff_pairs': [list(p) for p in sorted({(r['command_word'], r['mark_tariff']) for r in rows})],
                       'evidence_ids': [r['evidence_id'] for r in rows],
                       'report_block_ids': sorted({c['report_block_id'] for r in rows for c in r['creditworthy_points']})})
dump(CURR / 'answer-shapes.json', {'shapes': shape_rows,
     'general_warning': 'Shape families are planning guidance, not an invented universal mark scheme. Consult the cited report guidance for each exact command/tariff/context. In particular, Discuss does not always mean two sides and Evaluate does not always prescribe a conclusion mark.',
     'task_specific_allocations': [
       {'evidence_id':'EV-6145-2020-P2-1(b)', 'shape':'7 marks: diagram up to 4, explanation up to 3; binding minimum wage, not shifting curves.', 'source_locator':{'source_id':'2020-ER','pdf_page':146}},
       {'evidence_id':'EV-6145-2020-P2-1(c)', 'shape':'9 marks: opposing cases plus a separate valid conclusion; avoid repeating a credited point as the conclusion.', 'source_locator':{'source_id':'2020-ER','pdf_page':147}},
       {'evidence_id':'EV-6145-2021-P2-2(a)', 'shape':'6 marks: three developed features; bare names capped at 3.', 'source_locator':{'source_id':'2021-ER','pdf_page':138}},
       {'evidence_id':'EV-6145-2022-P1-26(b)', 'shape':'4 marks for diagram only; explanation is not requested.', 'source_locator':{'source_id':'2022-ER','pdf_page':164}},
       {'evidence_id':'EV-6145-2022-P2-4(b)', 'shape':'7 marks combines quota definition and diagram; prose analysis is not credited as an extra substitute.', 'source_locator':{'source_id':'2022-ER','pdf_page':172}},
       {'evidence_id':'EV-6145-2023-P2-2(c)', 'shape':'7 marks: developed two-sided IT/productivity evaluation and distinct conclusion; one side stays in lower band.', 'source_locator':{'source_id':'2023-ER','pdf_page':185}},
       {'evidence_id':'EV-6145-2024-P2-6(b)', 'shape':'4 marks: two causes developed once; direction of change required, static labels capped at 2.', 'source_locator':{'source_id':'2024-ER','pdf_page':186}},
       {'evidence_id':'EV-6145-2024-P2-2(d)', 'shape':'7 marks: government borrowing evaluated from both sides; one-sided response capped at 4 in this report.', 'source_locator':{'source_id':'2024-ER','pdf_page':181}}
     ]})

checks = []
for sid, rows in sorted(grouped.items()):
    total = sum(r['mark_tariff'] for r in rows)
    assert total == (80 if rows[0]['paper_id'] == '1' else 120), (sid, total)
    if rows[0]['paper_id'] == '1':
        sums = {sec: sum(r['mark_tariff'] for r in rows if r['section'] == sec) for sec in 'AB'}
        assert sums == {'A': 40, 'B': 40}, (sid, sums)
    else:
        sums = {str(q): sum(r['mark_tariff'] for r in rows if r['question_ref'].split('(')[0] == str(q)) for q in range(1, 7)}
        assert all(v == 20 for v in sums.values()), (sid, sums)
    checks.append({'source_id': sid, 'parts': len(rows), 'marks_offered': total, 'section_or_question_totals': sums})
assert len({r['evidence_id'] for r in records}) == len(records)
assert sum(t['primary_marks_offered'] for t in topic_rows) == 1000
assert sum(c['count'] for c in command_rows) == len(records)
assert all(m['evidence_ids'] for m in misconceptions)
summary = {'question_parts':len(records), 'marks_offered':1000, 'candidate_marks':800,
           'parts_with_credit_shape': sum(bool(r['creditworthy_points']) for r in records),
           'parts_with_common_errors': sum(bool(r['common_errors']) for r in records),
           'report_performance_comments':len(findings), 'report_statement_spans':len(statements),
           'curated_misconceptions':len(misconceptions),
           'mapping_confidence':dict(collections.Counter(r['mapping_confidence'] for r in records)),
           'source_anomalies':len(anomalies), 'exposure_classes':dict(collections.Counter(r['exposure_class'] for r in objective_rows)),
           'listed_not_observed':[c['word'] for c in command_rows if not c['count']],
           'source_checks':checks}
dump(OUT / 'verification.json', summary)
print(json.dumps(summary,indent=2))
print('COMMANDS')
for c in sorted(command_rows, key=lambda x:-x['count']):
    print(c['word'],c['count'],c['modal_tariffs'],c['tariffs'])
print('TOPICS BY PRIMARY OFFERED MARKS')
for t in sorted(topic_rows,key=lambda t:-t['primary_marks_offered']):
    print(t['topic_id'],t['primary_marks_offered'],t['share_of_offered_marks_percent'],t['title'])
