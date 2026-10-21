"""6136 Step 4: generate planner inputs, then use the unchanged standard builders.

The semantic decisions are data, separate from mechanical generation. This does
not author the final resources or confer plan approval. Run with repository cwd.
"""
import copy
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path
import yaml

WS = Path(__file__).resolve().parents[1]
REPO = WS.parents[1]
CUR = WS / 'curriculum'
EV = WS / 'assessment-evidence'
STD = REPO / 'standard/v0.2.0-draft'
STAMP = '2026-10-19'

def read(p): return json.loads(p.read_text())
def dump(p, d):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(d, indent=2, ensure_ascii=False) + '\n')
def ydump(p, d): p.write_text(yaml.safe_dump(d, sort_keys=False, allow_unicode=True))
def run(name, *args):
    subprocess.run([sys.executable, str(STD / 'build' / name), str(WS), *args], check=True)

facts = read(CUR / 'syllabus-facts.json')
dec = read(WS / 'planning/registry_decisions.json')
commands = read(EV / 'command-word-counts.json')['commands']
for dest, src in [('source-bullet-evidence.json', EV / 'assessment_evidence.json'),
                  ('source-bullet-exposure.json', CUR / 'exam-exposure.json'),
                  ('source-bullet-misconceptions.json', CUR / 'misconceptions.json')]:
    p = WS / 'planning' / dest
    if not p.exists(): dump(p, read(src))
source_records = read(WS / 'planning/source-bullet-evidence.json')['records']
mis = read(WS / 'planning/source-bullet-misconceptions.json')
weights = {a['code']: a['qualification_weight_percent'] for a in facts['assessment_objectives']}

TYPES = {
    'ds_overview': ['APP'],
    'ds_evidence_overview': ['INTERP'],
    'ds_member': ['FEATURE', 'INTERP'],
    'ds_concept': ['DEF', 'WHY'],
    'ds_mechanism': ['FEATURE', 'CHAIN'],
    'ds_strategy': ['FEATURE', 'EVAL'],
    'ds_quantitative': ['FEATURE', 'CALC', 'INTERP'],
    'ds_research_overview': ['PROC'],
    'ds_research_method': ['PROC', 'EVAL'],
    'ds_research_concept': ['DEF', 'PROC'],
    'ds_research_solution': ['PROC', 'APP'],
    'ds_research_data': ['PROC', 'INTERP'],
}
STRUCTURES = {
    'DEF': ['meaning', 'boundary'],
    'FEATURE': ['feature', 'relevance'],
    'WHY': ['reason', 'consequence'],
    'APP': ['context', 'action', 'reason'],
    'CHAIN': ['cause', 'mechanism', 'consequence'],
    'INTERP': ['evidence', 'relationship', 'meaning'],
    'EVAL': ['criterion', 'evidence', 'judgement', 'condition'],
    'PROC': ['purpose', 'sequence', 'record'],
    'CALC': ['method', 'working', 'unit', 'meaning'],
    'MISCON': ['error', 'distinction', 'test'],
    'short_answer': ['context', 'point', 'development'],
    'data_response': ['evidence', 'comparison', 'conclusion'],
    'practical_task': ['purpose', 'method', 'evidence', 'limitation', 'response'],
    'source_analysis': ['findings', 'evidence', 'conclusion', 'recommendation'],
}
SUBAOS = {
    'DEF': ['A', 'C'], 'FEATURE': ['A'], 'WHY': ['A'],
    'APP': ['A', 'D'], 'CHAIN': ['B'], 'INTERP': ['B'],
    'EVAL': ['B'], 'PROC': ['C'], 'CALC': ['B'],
    'MISCON': ['A', 'B', 'C'],
}
BLOOMS = {'DEF': 'Remember', 'FEATURE': 'Understand', 'WHY': 'Understand',
          'APP': 'Apply', 'CHAIN': 'Analyse', 'INTERP': 'Analyse',
          'EVAL': 'Evaluate', 'PROC': 'Apply', 'CALC': 'Apply', 'MISCON': 'Understand'}
CW = {'DEF': ['Define'], 'FEATURE': ['State'], 'WHY': ['Explain'],
      'APP': ['Suggest'], 'CHAIN': ['Explain'], 'INTERP': ['Describe'],
      'EVAL': ['Discuss'], 'PROC': ['Describe'], 'CALC': ['Calculate'], 'MISCON': ['Explain']}
TARIFFS = {'DEF:Define': 1, 'FEATURE:State': 2, 'WHY:Explain': 2,
           'APP:Suggest': 3, 'CHAIN:Explain': 3, 'INTERP:Describe': 2,
           'EVAL:Discuss': 4, 'PROC:Describe': 4, 'CALC:Calculate': 2,
           'MISCON:Explain': 2}

qpid = 'nam-6136-nssco-2026'
spid = 'yyeni-development-studies-6136-v0.2.0-draft'
profile = {
    'profile_id': qpid, 'version': '0.2.0-draft', 'status': 'draft',
    'board': 'Namibia: NIED syllabus; DNEA examinations', 'qualification': 'NSSCO',
    'subject': 'Development Studies', 'syllabus_code': '6136',
    'examination_years': [2026], 'syllabus_version': 'NIED 2017; implementation 2019; first examination 2020; no stated expiry',
    'selected_level': 'NSSCO Grades 10–11',
    'route': {'route_id': 'all-three-papers', 'name': 'All ten themes and all three compulsory papers',
              'included_paper_ids': ['P1', 'P2', 'P3'], 'excluded_paper_ids': [],
              'notes': '2026 is intended resource use, not a printed terminal syllabus year.'},
    'language': 'en-GB', 'guided_learning_hours': None,
    'learner_entry_assumptions': ['No previous Junior Secondary Development Studies study is assumed.'],
    'papers': [{'paper_id': 'P'+p['paper'], 'name': 'Paper '+p['paper']+' '+p['name'],
                'duration_minutes': p['duration_minutes'], 'marks': p['marks'],
                'qualification_weight_percent': p['weight_percent'], 'question_basis': p['verbatim'],
                'assessment_objective_weights': p['ao_split']} for p in facts['papers']],
    'assessment_objectives': [{'code': a['code'], 'name': a['name'], 'description': ' '.join(a['can_do']),
                               'qualification_weight_percent': weights[a['code']]} for a in facts['assessment_objectives']],
    'command_words': [{'word': c['word'], 'meaning': c['meaning']} for c in facts['command_words']],
    'scope': {'included_topic_ids': [t['id'] for t in facts['content_outline']], 'excluded_topic_ids': [], 'optional_routes': []},
    'source_authority': {'curricular': [facts['source_document']],
                         'assessment': ['assessment-evidence/source-manifest.json; 15 papers and five reports, 2020–2024'],
                         'conceptual': ['Official syllabus terminology and independently authored explanations; glossary.json'],
                         'conflict_rule': 'Syllabus governs scope and assessment; paper governs actual tariff where a report contradicts it. Preserve all ambiguities in GAPS.md.'},
    'example_selection_rules': ['Use original Namibian or southern African contexts; invented organisations; N$.',
                                'Historical syllabus examples remain dated examples. Do not assert current policies, agency activities or health advice without verifying an official source.'],
    'notes': ['AO percentages aggregate printed grid rows; individual A.1/A.2 shares are not inferred.',
              'Standalone mark schemes and 2025 sources unavailable; source set accepted by Jeremy.'],
}
ydump(WS / 'qualification-profile.yaml', profile)

# One source-bullet parent, plus one member per explicit semantic decision.
# The page-continuation enterprise repeat has one canonical parent and two source links.
objectives = []
bridge = []
by_key = {}
by_type = {key: 'ds_'+typ for typ, keys in dec['types'].items() for key in keys.split()}
for t in facts['content_outline']:
    tid = t['id']; root = 'OBJ-6136-'+tid
    def objective(oid, parent, text, learner, typ, tier, page, guidance=''):
        aos = ['B', 'C', 'D'] if tid == '10.1' else ['A', 'B']
        item = {'objective_id': oid, 'parent_id': parent, 'topic_id': tid,
                'syllabus_text': text, 'learner_objective': learner, 'level': 'NSSCO',
                'route_status': 'core', 'mandatory': True, 'objective_type': typ,
                'assessment_objectives': aos, 'command_words': list(dict.fromkeys(w for st in TYPES.get(typ, []) for w in CW[st])),
                'prerequisite_ids': [], 'related_ids': [], 'depth_tier': tier,
                'source_coverage': {'rating': 0, 'action': 'generate_gap',
                                    'rationale': 'Author original teaching prose from the official syllabus and internal assessment evidence. Supplemental third-party notes are not approved derivation text.'},
                'status': 'planned', 'sub_topic': tid, 'sub_topic_heading': t['title'],
                'syllabus_page': page, 'syllabus_guidance': guidance,
                'papers': ['3'] if tid == '10.1' else ['1', '2']}
        objectives.append(item)
        return item
    objective(root, None, t['title'], t['title'], 'topic_container', 4, t['source_pages'][0]+3)
    for n, b in enumerate(t['specific_objectives'], 1):
        key = f'{tid}:{n}'
        if key == '3.1:11': continue
        oid = f'OBJ-6136-{tid}.{n:02d}-00'
        members = dec['members'].get(key, '').split('|') if key in dec['members'] else []
        typ = 'ds_overview' if members else by_type.get(key, 'ds_mechanism')
        if members and by_type.get(key) in ['ds_strategy', 'ds_quantitative']:
            typ = 'ds_evidence_overview'
        if tid == '10.1':
            typ = 'ds_research_overview' if members else ('ds_research_solution' if n in (8, 12) else 'ds_research_method')
        guidance = dec.get('member_policy_notes', {}).get(key, '')
        if typ == 'ds_evidence_overview':
            guidance += ' Use original comparative evidence to interpret the relationship among members; definition recall alone cannot answer this slot.'
        if members:
            guidance += ' Parent practises the integrated relationship or choice; members practise distinct targets. Do not duplicate the parent as a long-list recall card.'
        parent = objective(oid, root, b['text'], b['text'][0].upper()+b['text'][1:], typ, 3 if not members else 4, b['pdf_page'], guidance)
        by_key[key] = {'parent': oid, 'members': []}
        for i, member in enumerate(members, 1):
            mid = f'OBJ-6136-{tid}.{n:02d}-{i:02d}'
            mt = 'ds_member'
            if tid == '10.1':
                mt = 'ds_research_solution' if n == 12 else ('ds_research_data' if n == 11 else 'ds_research_concept' if n in (3, 4, 5, 9) else 'ds_research_method')
            if key in ('3.1:6', '3.1:7', '3.1:9', '4.1:3', '4.2:4', '5.1:4', '7.2:2', '9.3:1'):
                mt = 'ds_strategy'
            learner = f'In {t["title"]}, explain and apply {member}; retain the parent outcome’s required relationship and judgement.'
            objective(mid, oid, member, learner, mt, 2, b['pdf_page'],
                      f'Semantic decomposition of {b["source_bullet_id"]}, not an additional syllabus claim. '+guidance)
            by_key[key]['members'].append(mid)
        bridge.append({'source_bullet_id': b['source_bullet_id'], 'source_bridge_id': f'SB-6136-{tid}-{n:02d}',
                       'source_text': b['text'], 'pdf_page': b['pdf_page'], 'registry_parent_id': oid,
                       'registry_member_ids': by_key[key]['members'], 'decomposition': 'judgement',
                       'exposure_rule': 'Question demand is assigned to the canonical parent unless an explicit member-level decision names the member. Never copy the entire parent frequency to every child.'})
        if key == '3.1:12':
            prev = t['specific_objectives'][10]
            by_key['3.1:11'] = by_key[key]
            bridge.append({'source_bullet_id': prev['source_bullet_id'], 'source_bridge_id': 'SB-6136-3.1-11',
                           'source_text': prev['text'], 'pdf_page': prev['pdf_page'], 'registry_parent_id': oid,
                           'registry_member_ids': by_key[key]['members'], 'decomposition': 'consolidated repeated page continuation',
                           'exposure_rule': 'Consolidate with 3.1:12; do not add a second objective or double-count a question.'})

registry = {'registry_id': 'REG-NAM-6136-NSSCO-2026', 'qualification_profile_id': qpid, 'subject_profile_id': spid,
            'authority': facts['authority'], 'generated_at': STAMP, 'objectives': objectives,
            'granularity_note': 'Topic roots are structural. Assessable source outcomes are decomposed into integrated parent and member objectives; repeated enterprise source rows are consolidated. Full provenance in source-bullet-bridge.json.',
            'papers_note': 'Papers 1/2 draw on whole curriculum; topic 10.1 planning focuses on Paper 3. Research can use any content context. This teaching allocation is judgement, not a claim that research terminology cannot occur on other papers.'}
dump(CUR / 'objective_registry.json', registry)
dump(CUR / 'source-bullet-bridge.json', {'policy': dec['policy'], 'entries': bridge})
dump(CUR / 'unit_titles.json', {x['theme']: x['title'] for x in facts['content_themes']})
lookup = {b['source_bridge_id']: b for b in bridge}
obj_by_id = {o['objective_id']: o for o in objectives}

# Preserve the full internal question transcription in the Step 3 snapshot. The
# canonical map conforms to the assessment-evidence schema and names final IDs.
fine_path = WS / 'planning/member_evidence_decisions.json'
fine = read(fine_path) if fine_path.exists() else {}
records = []
for old in source_records:
    ids = list(dict.fromkeys(lookup[x]['registry_parent_id'] for x in old['objective_ids']))
    ids += [x for x in fine.get(old['evidence_id'], []) if x not in ids]
    assert all(x in obj_by_id for x in ids)
    loc = old['source_locator']
    r = {k: copy.deepcopy(old[k]) for k in ['evidence_id', 'source_id', 'year', 'paper_id', 'variant', 'question_ref', 'mark_tariff', 'command_word',
                                            'context_type', 'creditworthy_points', 'examiner_findings', 'strong_response_features']}
    r.update({'evidence_type': 'past_paper', 'objective_ids': ids,
              'exam_series': str(old['year'])+' annual; month not asserted',
              'ao_focus': list(dict.fromkeys(x.split('.')[0] for x in old['ao_focus'])),
              'source_locator': f'{loc["path"]} PDF p.{loc["pdf_page"]}; {old["paper_id"]} {old["question_ref"]}',
              'context_summary': 'Original text retained internally in planning/source-bullet-evidence.json; never reproduce it for learners.',
              'common_errors': [x['summary'] if isinstance(x, dict) else x for x in old['common_errors']],
              'notes': old['notes'] + ['AO focus is planner judgement of task demand, not official item AO credit.',
                                       'Source-bullet mapping preserved separately; child mapping only where explicitly adjudicated.']})
    records.append(r)
dump(EV / 'assessment_evidence.json', {'map_id': 'CORPUS-NAM-6136-2020-2024', 'status': 'partial', 'records': records})
# partial refers to absent standalone schemes / incomplete member-level mappings,
# not lost paper parts: all 419 paper parts and all 1,000 marks remain here.
exposures = []
for o in objectives:
    if not o['parent_id']: continue
    rs = [r for r in records if o['objective_id'] in r['objective_ids']]
    years = sorted({r['year'] for r in rs}); cw = dict(Counter(r['command_word'] for r in rs))
    exposures.append({'objective_id': o['objective_id'], 'topic_id': o['topic_id'],
                      'exposure_class': 'frequent' if len(years) >= 4 else 'occasional' if len(years) >= 2 else 'rare' if years else 'unseen',
                      'exam_exposure': 'measured_registry_assignment',
                      'evidence': {'question_parts_naming_it': len(rs), 'distinct_series': len(years),
                                   'max_mark_tariff': max([r['mark_tariff'] for r in rs] or [0]),
                                   'command_words_observed': cw, 'evidence_ids': [r['evidence_id'] for r in rs],
                                   'years': years, 'marks_examined_overlap': sum(r['mark_tariff'] for r in rs)},
                      'required_subtypes': TYPES[o['objective_type']],
                      'assignment_limit': 'Zero means no direct member assignment in this conservative map; it is not proof that the member was absent from assessment. Parent frequencies are not inherited.'})
dump(CUR / 'exam-exposure.json', {'exposure_id': 'EXPOSURE-NAM-6136-NSSCO-2026-REGISTRY',
                                 'classes': {'frequent': '4–5 distinct annual series', 'occasional': '2–3', 'rare': '1', 'unseen': '0 assigned; not absence proof'},
                                 'method': 'Canonical source-bullet parents plus explicit member-level semantic decisions; no token propagation.',
                                 'objectives': exposures})

# Canonical misconceptions retain original source IDs in the preserved snapshot.
for m in mis['entries']:
    m['entry_id'] = m['misconception_id']
    m['source_bridge_objective_ids'] = m['objective_ids']
    m['objective_ids'] = list(dict.fromkeys(lookup[x]['registry_parent_id'] for x in m['objective_ids']))
    m['objective_id'] = m['objective_ids'][0]
    m['test'] = m['discrimination_test']
dump(CUR / 'misconceptions.json', mis)

fw_commands = []
for c in commands:
    rs = [r for r in records if r['command_word'] == c['word']]
    fw_commands.append({**c, 'observed_count': c['count'], 'observed_tariffs': sorted(map(int, c['tariffs_seen'])),
                        'modal_tariff': min(c['modal_tariffs']), 'exact_mark_tariff': min(c['modal_tariffs']),
                        'used_at_level': True, 'use_in_prompts': True,
                        'primary_assessment_objectives': list(dict.fromkeys(a for r in rs for a in r['ao_focus']))})
observed = {c['word'] for c in commands}
unused = read(EV / 'command-word-counts.json')['listed_entries_not_observed_as_primary_commands']
# Compound glossary definitions and noun cues remain in syllabus-facts. Do not
# make C-14 prohibit e.g. every noun 'relationship' inside a legitimate question.
for word in ['Analyse', 'Evaluate', 'Assess', 'Contrast', 'Complete', 'Annotate', 'Justify']:
    if word not in observed:
        fw_commands.append({'word': word, 'observed_count': 0, 'observed_tariffs': [], 'modal_tariff': None,
                            'exact_mark_tariff': None, 'used_at_level': False, 'use_in_prompts': False,
                            'provenance': 'Not observed as a primary command in the counted 2020–2024 corpus. Compound Describe and evaluate is separately observed.'})
fw = {'framework_id': 'FW-NAM-6136-NSSCO-2026', 'provenance': {'syllabus': 'curriculum/syllabus-facts.json',
      'corpus': 'assessment-evidence/command-word-counts.json',
      'judgement': 'subtype/AO labels, selected observed tariffs and practice-task AO splits are planner judgements, not official item allocations'},
      'assessment_objectives': profile['assessment_objectives'],
      'papers': copy.deepcopy(facts['papers']), 'command_words': fw_commands,
      'command_words_listed_but_never_used': unused,
      'ao_mark_budget': {'stated_qualification_weight_percent': weights,
                         'source': 'Derived sums of printed sub-objective grid marks on syllabus p.20 / PDF23; see syllabus-facts.json'},
      'item_mix_target': {'target_share_percent': weights, 'measure': 'marks-equivalent; item counts are descriptive'},
      'flashcard_subtype_ao_map': [{'subtype': st, 'assessment_objectives': aos, 'blooms_level': BLOOMS[st]} for st, aos in SUBAOS.items()],
      'blooms_taxonomy': {'levels': [{'level': x} for x in ['Remember', 'Understand', 'Apply', 'Analyse', 'Evaluate', 'Create']],
                         'by_performance_task': {'short_answer': 'Apply', 'data_response': 'Analyse', 'practical_task': 'Apply', 'source_analysis': 'Evaluate'}},
      'allocation_limit': 'Tariffs are observed question sizes; rubric text authored for new tasks is indicative. No universal one-point-per-mark rule or invented official scheme.'}
dump(CUR / 'assessment-framework.json', fw)
dump(CUR / 'glossary.json', {
    'glossary_id': 'GLOSS-NAM-6136-NSSCO-2026',
    'authority': 'Planner definitions for consistent original authoring; not quoted official definitions or current policy/medical guidance.',
    'entries': [{'term': term, 'meaning': meaning, 'provenance': 'judgement; settled conceptual teaching sense'}
                for term, meaning in read(WS / 'planning/glossary_decisions.json').items()]})

content_performance = [
    {'item_type': 'short_answer', 'papers': ['1', '2'], 'marks': 6, 'ao_split': {'A': 3, 'B': 3},
     'brief': 'An original 6-mark structured mini-task: State two relevant features [2], then Explain a source-supported consequence [4]. Both tariff pairs are observed. Use two to four appropriate objectives from this topic. AO split A3/B3 is a planning estimate. Do not turn the answer into a six-point list.'},
    {'item_type': 'data_response', 'papers': ['1', '2'], 'marks': 6, 'ao_split': {'B': 6},
     'brief': 'An original 6-mark data mini-task with a short self-contained table: Describe a supported pattern [2], then Discuss a choice using that evidence [4]. Both tariff pairs are observed. Name a decisive criterion and a condition. Use fresh figures, not a copied source.'},
]
research_performance = []
for i, theme in enumerate(['water access and survey design', 'rural production and sampling', 'education access and representation', 'community waste and evaluating recommendations'], 1):
    research_performance += [
        {'item_type': 'practical_task', 'papers': ['3'], 'marks': 35, 'ao_split': {'B': 10, 'C': 18, 'D': 7},
         'brief': f'Cycle {i}, {theme}: original supplied-investigation pack, 35 marks in total. Compose subparts using only observed primary-command/tariff pairs; each part is at most six marks. Plan the enquiry, apply sampling/data collection, pilot an instrument, organise and interpret supplied original data, and solve a practical research obstacle. Supply all context and datasets. AO B10/C18/D7 is a planner split, not an official Section A grid. Use distinct tasks and original figures in each cycle.'},
        {'item_type': 'source_analysis', 'papers': ['3'], 'marks': 15, 'ao_split': {'B': 5, 'C': 7, 'D': 3},
         'brief': f'Cycle {i}, {theme}: own-investigation rehearsal, 15 marks in subparts of at most six. Model the reasoning first with a clearly fictional completed enquiry and its data, then supply prompts to transfer the method to the learner’s actual investigation. Link research question, aims, methods, findings, evidence, conclusion, recommendation, implementer and limitations. Never invent a learner’s actual fieldwork. Keep the personal report requirement. AO B5/C7/D3 is a planner split. This paired cycle totals the syllabus Paper 3 split B15/C25/D10.'}
    ]
sp = {
    'profile_id': spid, 'version': '0.2.0-draft', 'status': 'draft', 'subject_name': 'NSSCO Development Studies 6136',
    'language_variant': 'en-GB', 'purpose': 'Standalone teaching, retrieval and applied practice across all ten themes, calibrated to the approved syllabus and corpus.',
    'foundational_concepts': ['development', 'sustainability', 'evidence', 'inequality', 'resources', 'participation', 'research'],
    'objective_types': [{'type_id': typ, 'label': typ, 'description': 'Planner-declared development-studies teaching role; no business default is used.',
                         'required_components': ['meaning', 'context', 'boundary'], 'recommended_item_types': ['flashcard']} for typ in TYPES],
    'assessment_skill_model': [{'skill_id': a['code'], 'label': a['name'], 'definition': ' '.join(a['can_do']),
                               'authoring_requirements': ['Match the labelled task demand; do not infer credit solely from the command.']} for a in facts['assessment_objectives']],
    'application_model': {'core_rule': 'Context must change the answer; a place name alone is insufficient.',
                          'context_dimensions': ['resource availability', 'population', 'stakeholders', 'cost', 'time', 'data quality'],
                          'worked_application_policy': {'minimum_per_major_objective': 1, 'contrast_required_for_decisions': True,
                                                        'coverage_dimensions': ['urban/rural', 'Namibia/southern Africa', 'household/community/national']},
                          'pseudo_application_patterns': ['place name added to a generic list', 'copying a stimulus without interpretation']},
    'analysis_model': {'chain_template': ['evidence or cause', 'mechanism', 'consequence for a development outcome'],
                       'rules': ['Name who is affected and how.', 'Separate a relationship from proof of causation.', 'Preserve necessary conditions.']},
    'evaluation_model': {'judgement_template': ['criterion', 'evidence', 'weighing', 'conclusion and condition'],
                         'decision_dimensions': ['feasibility', 'equity', 'cost', 'environment', 'time', 'evidence quality'],
                         'rules': ['Compare alternatives against the same criterion.', 'Keep conclusions within the evidence.', 'Do not present an indicative practice rubric as an official scheme.']},
    'depth_model': {'allocation_factors': ['syllabus demand', 'exposure', 'misconception risk'],
                    'tiers': [{'tier': n, 'label': label, 'typical_use': use, 'indicative_word_range': {'min': 100, 'max': 500},
                               'indicative_item_range': {'min': 1, 'max': 3}} for n, label, use in [(1, 'term', 'precise meaning'), (2, 'member', 'one distinct target'), (3, 'outcome', 'applied relationship'), (4, 'integration', 'relationships among listed members')]]},
    'quantitative_model': {'required_components': ['method', 'variable meanings', 'substitution', 'unit', 'interpretation'],
                           'interpretation_rules': ['Distinguish absolute change, percentage change and percentage points.', 'Compare equivalent units and denominators.', 'Use clearly fictional original data and recompute all values.']},
    'legal_and_jurisdiction_model': {'core_rule': 'Teach syllabus principles. Verify any current legal or policy claim using an official source; date historical examples.',
                                    'high_risk_topics': ['national plans', 'population policies', 'health', 'gender-based violence', 'international agencies']},
    'learning_item_model': {'item_types': ['flashcard', 'short_answer', 'data_response', 'practical_task', 'source_analysis'],
                            'flashcard_subtypes': list(SUBAOS), 'rules': ['One main target per card.', 'Parent slots practise integration, not another exhaustive list.',
                                                                                      'Every slot is filled once; new labels or deviations must be recorded.', 'Never copy exam/report phrasing.']},
    'terminology_rules': ['British English; N$; preserve official terms with a plain explanation.', 'Do not conflate gender equality with identical lived opportunities or population density with distribution.'],
    'prohibited_patterns': ['examiners reward', 'unsupported universal policy claims', 'fabricated learner fieldwork', 'copied assessment questions'],
    'semantic_review_questions': ['Can every answer be reconstructed from the notes?', 'Does source evidence change the answer?', 'Are named historical policies clearly dated?', 'Does research practice require application rather than definition recall?'],
    'variant_register': [
        {'term': 'capital', 'variants': ['money capital', 'capital goods'], 'consequence': 'Finance purchases productive assets; money is not itself the produced equipment.', 'teach_as': 'distinction'},
        {'term': 'education classification', 'variants': ['traditional and modern', 'formal, informal and non-formal'], 'consequence': 'These classify different aspects; do not treat the two groupings as interchangeable.', 'teach_as': 'two independent classifications'},
        {'term': 'population description', 'variants': ['density', 'distribution'], 'consequence': 'Number per unit area differs from the spatial pattern.', 'teach_as': 'distinction'},
        {'term': 'research statement', 'variants': ['hypothesis', 'research question'], 'consequence': 'A tentative testable proposition differs from the question the enquiry investigates.', 'teach_as': 'paired examples'},
    ],
    'answer_structures': STRUCTURES,
    'conditioned_mechanisms': [
        {'mechanism_id': 'renewable-use', 'asserted_when': [r'\bwood\b', r'\b(?:renewable|sustainable)\b'],
         'required_conditions': [{'name': 'regrowth and harvesting balance', 'any_of': [r'regrowth', r'replant', r'regenerat', r'harvest.*rate']}]},
        {'mechanism_id': 'tourism-local-benefit', 'asserted_when': [r'\btourism\b', r'\b(?:increases?|raises?) local incomes?\b'],
         'required_conditions': [{'name': 'local participation or retention', 'any_of': [r'local.*(?:own|employ|suppl|retain)', r'if.*local', r'when.*local']}]},
    ],
    'depictions': {'chart_model': 'none', 'rule': 'No compatible general graph renderer is available in the standard. Use original data tables and learner plotting tasks; no hand-drawn ASCII, code-fenced or generated-image plots. Model answers state axes, scales, labels, values and shape. Independent review must check graph suitability and numeric consistency; C-35/C-41 do not validate these graphs.'},
    'slot_plan': {'subtypes_by_objective_type': TYPES, 'subtypes_by_tier': {1: [], 2: [], 3: [], 4: []},
                  'command_words_by_subtype': CW, 'tariff_overrides': TARIFFS,
                  'ao_by_objective_type': {'*': {'DEF': ['A'], 'MISCON': ['A'], 'APP': ['A']},
                                           'ds_research_concept': {'DEF': ['C'], 'MISCON': ['C']},
                                           'ds_research_method': {'MISCON': ['C']},
                                           'ds_research_solution': {'APP': ['D'], 'MISCON': ['C']},
                                           'ds_research_data': {'MISCON': ['C']},
                                           'ds_research_overview': {'MISCON': ['C']}},
                  'high_tariff': {'threshold': 7, 'adds': []}, 'top_up': [],
                  'misconception_slots': 'one_per_entry', 'performance_tasks': content_performance + research_performance},
}
quality = read(WS / 'planning/profile_quality_decisions.json')
sp['answer_structures'] = quality['answer_structures']
sp['application_model']['core_rule'] += ' ' + ' '.join(quality['application_rules'])
sp['analysis_model']['rules'] += quality['analysis_rules']
sp['evaluation_model']['rules'] += quality['evaluation_rules']
sp['quantitative_model']['interpretation_rules'] += quality['quantitative_rules']
sp['semantic_review_questions'] = quality['semantic_review_questions']
# Store learning-from-profiles provenance in a separate curriculum file: the
# 6136 profile itself remains about this subject and keeps its existing keys.
sp['purpose'] += ' Quality requirements are grounded in the 6136 evidence criteria; reusable profile patterns were adapted at Jeremy’s request on 2026-10-20.'
shapes = {s['id']: s for s in read(CUR / 'answer-shapes.json')['6136']['shapes']}
criteria = []
for c in quality['evidence_criteria']:
    criteria.append({**c, 'basis': '6136 report-backed demand; transfer to new activities is planner judgement',
                     'citations': [{'shape_id': sid, 'evidence_ids': shapes[sid]['evidence_ids'],
                                    'source_locator': shapes[sid]['source_locator'],
                                    'allocation_limit': shapes[sid]['applies_to']} for sid in c['answer_shape_ids']]})
dump(CUR / 'quality-evidence.json', {'authority': quality['authority'],
    'review_policy': 'Use official 6136 syllabus and assessment evidence, automated checks and cross-vendor semantic review. No additional two-topic trial or blanket teacher-access gate. Keep actual unresolved source/technical limitations visible.',
    'profile_pattern_provenance': quality['reference_patterns'], 'criteria': criteria})
ydump(WS / 'subject-profile.yaml', sp)

# Scope limits remain those actually stated by the syllabus, including the three
# instruction/assessment safeguards. No list of invented content bans is added.
dump(CUR / 'syllabus-exclusions.json', {t['id']: [] for t in facts['content_outline']})
run('conform_registry.py')
run('make_contract.py', '--force')
run('make_work_order.py', '--all')

summary = []
for t in facts['content_outline']:
    tid = t['id']; wo = read(WS / 'topics' / tid / 'work_order.json'); c = read(WS / 'topics' / tid / 'contract.json')
    summary.append({'topic_id': tid, 'title': t['title'], 'objectives': wo['assessable_objective_count'],
                    'items': wo['planned_item_count'], 'flashcards': len(wo['item_slots']), 'performance_tasks': len(wo['performance_tasks']),
                    'content_units': len(wo['content_units']), 'notes_words': c['depth_constraints']['word_budget'],
                    'marks_equivalent': wo['marks_equivalent_total'], 'ao': wo['planned_ao_mix_by_marks']})
dump(WS / 'planning/plan-summary.json', {'date': STAMP, 'topics': summary,
     'totals': {'topics': len(summary), 'objectives': sum(x['objectives'] for x in summary), 'items': sum(x['items'] for x in summary),
                'flashcards': sum(x['flashcards'] for x in summary), 'performance_tasks': sum(x['performance_tasks'] for x in summary),
                'words_min': sum(x['notes_words']['min'] for x in summary), 'words_max': sum(x['notes_words']['max'] for x in summary)}})
print('Planner inputs and standard-generated contracts/work orders complete. Plan approval remains pending.')
