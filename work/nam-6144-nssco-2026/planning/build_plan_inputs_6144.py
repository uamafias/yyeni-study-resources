"""Compile explicit 6144 planning decisions into inputs for unchanged shared tools.

Step 3 files are snapshotted before adapting their shapes/IDs. No source meaning,
frequency or uncertain mapping is upgraded by member decomposition.
"""
import collections
import copy
import hashlib
import json
import re
import sys
from pathlib import Path

import yaml
from plan_inputs_6144 import MEMBERS, MEMBER_REQUIREMENTS, STRUCTURES, TYPES, TYPE_SLOTS

WS=Path(__file__).resolve().parents[1]
REPO=WS.parents[1]
CUR=WS/'curriculum'
E=WS/'assessment-evidence'
FACTS=json.loads((CUR/'syllabus-facts.json').read_text())
SNAP=E/'step3-accepted'
SNAP.mkdir(exist_ok=True)
for name,path in [('assessment_evidence.json',E/'assessment_evidence.json'),('exam-exposure.json',CUR/'exam-exposure.json'),
                  ('misconceptions.json',CUR/'misconceptions.json'),('scope-scan.json',CUR/'scope-scan.json')]:
    target=SNAP/name
    if not target.exists():target.write_bytes(path.read_bytes())
OLD=json.loads((SNAP/'assessment_evidence.json').read_text())
OLD_M=json.loads((SNAP/'misconceptions.json').read_text())['misconceptions']
OLD_S=json.loads((SNAP/'scope-scan.json').read_text())


def write(path,obj):path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def oid(topic,n):return f'OBJ-6144-{topic}.{n:02}'
def short(eid):return eid.removeprefix('EV-6144-')
TIER={'D':1,'F':1,'A':2,'C':3,'H':3,'E':4,'P':2,'Q':2,'I':3,'G':3,'R':3,'plc':3,
      'member_term':1,'member_method':2,'member_theory':3,'member_ratio':3,'member_graph':3,'member_document':3}
TYPE_SLOTS=copy.deepcopy(TYPE_SLOTS)
TYPE_SLOTS.update({'G':['APP'],'plc':['PROC'],'R':['SYNTH'],'member_graph':['APP'],'member_document':['SYNTH']})
CW={'DEF':['Define'],'FEATURE':['State'],'APP':['Explain'],'DIST':['Distinguish'],
    'CHAIN':['Explain'],'EVAL':['Evaluate'],'PROC':['Explain','Draw'],'CALC':['Calculate'],
    'INTERP':['Analyse'],'MISCON':['Explain'],'SYNTH':['Explain']}
BLOOM={'DEF':'Remember','FEATURE':'Remember','APP':'Apply','DIST':'Analyse','CHAIN':'Analyse',
       'EVAL':'Evaluate','PROC':'Apply','CALC':'Apply','INTERP':'Analyse','MISCON':'Understand','SYNTH':'Create'}
AO_MAP={st:('A' if st in ['DEF','FEATURE'] else 'ABCD' if st=='EVAL' else 'ABC') for st in CW}


def member_type(key,term):
    if key in ['1.1:12','1.2:04']:return 'F'
    if key=='2.1:02':return 'member_method'
    if key=='3.1:02':return 'member_theory'
    if key=='2.4:05' and term not in ['Income Statement','Statement of Financial Position']:return 'member_ratio'
    if key=='4.4:10':return 'Q'
    if key=='4.2:04':return 'member_graph' if term!='tabulation' else 'P'
    if key=='3.5:03':return 'member_document'
    if key in ['2.3:05','3.4:15','4.1:04','4.3:03','4.5:09','5.1:07','5.2:01','5.2:02','5.3:01']:return 'A'
    if key in ['3.2:03','4.4:09','4.4:12','4.5:05']:return 'member_method'
    if key=='4.3:02':return 'A'
    if key in ['3.4:11','3.5:01']:return 'P'
    return 'member_term'


def commands_for(kind,topic=None):
    if kind in ['G','member_graph']:return ['Draw']
    if kind=='plc':return ['Draw']
    return sorted(set(word for st in TYPE_SLOTS[kind] for word in CW[st]))


def registry():
    objectives=[];crosswalk={};member_ids={};provenance=[]
    def node(key,parent,topic,text,learner,kind,page,sourcebullet=None):
        obj={'objective_id':key,'parent_id':parent,'topic_id':topic,'syllabus_text':text,
             'learner_objective':learner,'level':'NSSCO','route_status':'core','mandatory':True,
             'objective_type':kind,'assessment_objectives':list('ABCD') if kind=='E' else ['A'] if kind in ['D','F','member_term'] else list('ABC'),
             'command_words':commands_for(kind,topic),'prerequisite_ids':[], 'related_ids':[],
             'depth_tier':TIER[kind],'source_coverage':{'rating':0,'action':'generate_gap','rationale':'Original learner teaching to be authored from the transcribed syllabus and mined assessment demand. Held third-party notes are supplementary, not approved derivation sources.'},
             'status':'planned','syllabus_page':page,'sub_topic':'.'.join(key.split('-')[2].split('.')[:3]),
             'papers':['1','2']}
        if sourcebullet:obj['syllabus_guidance']=MEMBER_REQUIREMENTS.get(sourcebullet,'Retain the full demand of the source bullet; introduce and practise each named member within that demand.')
        objectives.append(obj);return obj
    for topic in FACTS['content_outline']:
        tid=topic['topic_id'];classes=TYPES[tid].split()
        assert len(classes)==len(topic['specific_objectives']),(tid,len(classes),len(topic['specific_objectives']))
        root=f'OBJ-6144-{tid}'
        node(root,None,tid,topic['title'],topic['title'],'F',topic['title_sources'][0]['page'])
        for n,(bullet,kind) in enumerate(zip(topic['specific_objectives'],classes),1):
            key=f'{tid}:{n:02}';identifier=oid(tid,n)
            if key=='4.4:04':kind='plc'
            learner=re.sub(r'\s*\(a detailed knowledge of legal requirements and procedures is not expected\)','',bullet['text'])
            node(identifier,root,tid,bullet['text'],learner,kind,bullet['source']['page'],key)
            old=f'SYL-6144-{tid}-{n:02}';crosswalk[old]=identifier
            provenance.append({'objective_id':identifier,'source_syllabus_bullet_id':old,'source':bullet['source'],'kind':'syllabus bullet','type_and_depth_provenance':'judgement'})
            for m,term in enumerate(MEMBERS.get(key,'').split(';') if key in MEMBERS else [],1):
                child=f'{identifier}-{m:02}';mk=member_type(key,term)
                title=f'{term}: '+MEMBER_REQUIREMENTS.get(key,'Explain its meaning and role within the parent syllabus demand.')
                child_node=node(child,identifier,tid,bullet['text'],title,mk,bullet['source']['page'],key)
                child_node['prerequisite_ids']=[identifier]
                member_ids[(key,term)]=child
                basis='corpus instantiation of a syllabus demand' if key=='3.4:15' else 'named syllabus member or glossary-supported decomposition'
                provenance.append({'objective_id':child,'source_syllabus_bullet_id':old,'source':bullet['source'],
                                   'member':term,'kind':basis,'type_and_depth_provenance':'judgement',
                                   'note':'Parent wording is kept verbatim. A child is a teaching target, not a claim of an extra verbatim syllabus bullet or of direct past examination.'})
    # Annexe A explicitly lists these additional ratios beyond topic 2.4's list.
    for n,term in enumerate(['mark up','debtors collection period','creditors payment period'],1):
        ident=f'OBJ-6144-2.4.98-{n:02}'
        node(ident,'OBJ-6144-2.4','2.4',term,f'Calculate and interpret {term}, using the formula and conventions in Annexe A.','member_ratio',34)
        provenance.append({'objective_id':ident,'source':{'page':34,'printed_page':30,'verbatim':term,'provenance':'syllabus'},'kind':'Annexe A named ratio; direct exposure not asserted','type_and_depth_provenance':'judgement'})
    return {'registry_id':'REG-NAM-6144-NSSCO-2026','qualification_profile_id':'nam-6144-nssco-2026',
            'subject_profile_id':'yyeni-business-6144-nssco-2026','authority':FACTS['source_document'],
            'granularity_note':'22 topic roots, all 146 original syllabus bullets, explicitly named member targets, plus three Annexe A ratios. Parent wording retained; source relationships and planning judgements are in objective-provenance.json.',
            'papers_note':'Both papers draw on the subject; no topic-to-paper exclusion is invented.', 'objectives':objectives},crosswalk,member_ids,provenance


def adapt_evidence(crosswalk,members,reg):
    # Explicit semantic child links selected from the already read questions. A list
    # question that could credit any two members does not give exposure to all of them.
    direct={
      ('2.2:02','span of control'):['2020-P1-2(b)'],
      ('2.2:02','delegation'):['2020-P1-2(d)','2023-P1-4(a)(ii)'],
      ('2.2:02','responsibility'):['2023-P1-4(a)(i)'],
      ('2.1:02','private limited companies'):['2020-P2-1(a)','2021-P2-1(b)','2022-P1-1(b)'],
      ('2.1:02','partnerships'):['2021-P2-1(b)','2024-P2-2(b)'],
      ('2.1:02','sole proprietors'):['2024-P2-2(b)'],
      ('2.1:02','co-operatives'):['2022-P1-4(a)(i)'],
      ('2.1:02','close corporations'):['2023-P2-2(b)'],
      ('2.1:02','franchises'):['2022-P2-1(b)'],
      ('3.1:02','Herzberg'):['2020-P2-4(a)','2024-P2-2(a)'],
      ('3.1:02','Taylor'):['2020-P1-5(c)'],('3.1:02','Maslow'):['2020-P1-5(c)'],
      ('2.4:02','unit costs'):['2022-P1-5(a)(ii)','2024-P1-1(a)(i)'],
      ('2.4:02','fixed costs'):['2024-P1-1(b)'],('2.4:02','variable costs'):['2024-P1-1(b)'],
      ('2.4:03','income'):['2024-P1-1(a)(ii)'],('2.4:03','expenses'):['2024-P1-1(a)(ii)'],
      ('2.4:05','return on capital employed'):['2021-P2-5(b)'],
      ('2.4:05','net profit margin'):['2021-P2-5(b)','2022-P1-5(d)'],
      ('2.4:05','gross profit margin'):['2022-P1-5(d)'],
      ('2.4:05','current ratio'):['2020-P2-1(b)','2022-P2-4(b)','2023-P2-3(b)'],
      ('2.4:05','quick/liquid ratio'):['2020-P2-1(b)','2022-P2-4(b)','2023-P2-3(b)'],
      ('2.4:05','solvency ratio'):['2024-P2-5(a)'],
      ('3.4:12','redundancy'):['2020-P1-5(a)(i)','2024-P1-3(b)'],
      ('3.4:15','quality circles'):['2021-P2-3(b)','2024-P2-3(b)'],
      ('3.4:15','worker councils'):['2024-P2-3(b)'],
      ('3.4:15','democratic leadership'):['2021-P2-3(b)','2023-P1-5(d)'],
      ('4.4:06','brand name'):['2021-P1-2(c)'],('4.4:06','brand loyalty'):['2021-P1-2(c)'],
      ('4.4:10','cost plus prices'):['2022-P1-3(c)'],
      ('4.1:05','market orientation'):['2021-P1-3(c)','2024-P1-2(c)'],
      ('4.1:05','product orientation'):['2021-P1-3(c)','2024-P1-2(c)'],
      ('4.4:13','informative advertising'):['2021-P1-5(c)','2024-P1-5(c)'],
      ('4.4:13','persuasive advertising'):['2021-P1-5(c)','2024-P1-5(c)'],
    }
    record_ids={short(r['evidence_id']) for r in OLD}
    assert all(ref in record_ids for values in direct.values() for ref in values)
    child_links=collections.defaultdict(list)
    for key,refs in direct.items():
        for ref in refs:child_links[ref].append(members[key])
    schema=json.loads((REPO/'standard/v0.2.0-draft/schemas/assessment_evidence.schema.json').read_text())
    allowed=set(schema['properties']['records']['items']['properties'])
    records=[];unresolved=[]
    for old in OLD:
        if not old['objective_ids']:
            unresolved.append(old);continue
        r={k:copy.deepcopy(v) for k,v in old.items() if k in allowed}
        r['objective_ids']=[crosswalk[x] for x in old['objective_ids']]+child_links[short(old['evidence_id'])]
        r['objective_ids']=list(dict.fromkeys(r['objective_ids']))
        r['evidence_type']='past_paper'
        r['source_locator']=f"{old['source_locator']['path']}, PDF p.{old['source_locator']['pdf_page']}, Q{old['question_ref']}; ER {old['year']} PDF pp.{','.join(map(str,old['report_locator']['pdf_pages']))}"
        r['command_word']=old['command_word'].capitalize()
        r['notes']=old['notes']+['Canonical planner projection; full source context, uncertainty and detailed report guidance remain in step3-accepted/assessment_evidence.json. Child mappings are explicit semantic selections in build_plan_inputs_6144.py.']
        records.append(r)
    write(E/'assessment_evidence.json',{'map_id':'EVIDENCE-NAM-6144-NSSCO-2026','status':'partial','records':records})
    write(E/'unresolved-records.json',{'records':unresolved,'note':'Retained internally; excluded from schema-required non-empty mappings rather than inventing an objective match.'})
    exposures=[]
    for o in reg['objectives']:
        if not o['parent_id']:continue
        rr=[r for r in records if o['objective_id'] in r['objective_ids']]
        series={r['exam_series'] for r in rr};maximum=max((r['mark_tariff'] for r in rr),default=0)
        expclass='core' if len(series)>=4 else 'frequent' if len(series)>=2 else 'occasional' if maximum>=8 else 'rare' if rr else 'unseen'
        exposures.append({'objective_id':o['objective_id'],'topic_id':o['topic_id'],'exposure_class':expclass,
                          'exam_exposure':'probed_high' if maximum>=8 else 'probed_low' if rr else 'unprobed_2020_2024',
                          'evidence':{'question_parts_naming_it':len(rr),'distinct_series':len(series),'max_mark_tariff':maximum,
                                      'command_words_observed':dict(collections.Counter(r['command_word'] for r in rr))},
                          'evidence_ids':[r['evidence_id'] for r in rr], 'required_subtypes':[],
                          'times_examined':len(rr),'marks_examined':sum(r['mark_tariff'] for r in rr),
                          'command_words':dict(collections.Counter(r['command_word'] for r in rr)),
                          'mapping_note':'No member inherits its container’s frequency. Direct semantic child links only; lack of a child link does not establish that the child was never examined.'})
    write(CUR/'exam-exposure.json',{'exposure_id':'EXPOSURE-6144-PLANNER','classes':{'probed_high':'8 marks or more','probed_low':'6 marks or fewer','unprobed_2020_2024':'No direct mapped record in the held 2020–2024 collection.'},
                                   'class_allocation_note':'Exposure_class calibrates depth budget; required skill slots come from semantic objective types, not an indiscriminate exposure floor.','objectives':exposures})
    miscon=[]
    objbyid={o['objective_id']:o for o in reg['objectives']}
    for m in OLD_M:
        old_target=m['objective_ids'][0]
        target=crosswalk[old_target]
        miscon.append({'entry_id':m['misconception_id'],'topic_id':objbyid[target]['topic_id'],'objective_id':target,
                       'objective_ids':[crosswalk[x] for x in m['objective_ids']], 'a':m['title'],'b':m['correct_distinction'],
                       'test':m['discriminating_test'],'n':len(m['evidence_ids']),'evidence_ids':m['evidence_ids'],'sources':m['sources'],
                       'note':'One primary slot drills this confusion; additional topic links remain visible without generating duplicate cards.'})
    write(CUR/'misconceptions.json',{'misconceptions_id':'MISCONCEPTIONS-NAM-6144','entries':miscon})
    scopes=[{'construct':r['rule_id'],'pattern':r['pattern'],'source':f"NIED 6144 PDF p.{r['source']['page']}: {r['source']['verbatim']}",
             'authority':'syllabus limit; operational regex is judgement','must_catch':r['must_catch'],'must_allow':r['must_allow']} for r in OLD_S['rules']]
    write(CUR/'scope-scan.json',{'scope_scan_id':'SCOPE-6144-PLANNER','entries':scopes,'semantic_review_requirements':OLD_S['semantic_review_requirements']})
    write(CUR/'syllabus-exclusions.json',{t['topic_id']:[x['text'] for x in FACTS['scope_limits_and_requirements'] if x.get('topic_id')==t['topic_id']] for t in FACTS['content_outline']})
    write(CUR/'unit_titles.json',{t['theme_id']:t['title'] for t in FACTS['themes']})


def framework():
    words=json.loads((E/'command-word-evidence.json').read_text());fw_words=[]
    for w in words:
        live=w['use_in_prompts'];tariffs=w['tariffs_seen'];name=w['word'].capitalize()
        mode=w['modal_tariffs'][0] if w['modal_tariffs'] else None
        fw_words.append({'word':name,'in_syllabus_table':w['in_syllabus_table'],
                         'syllabus_page':w['syllabus_sources'][0]['page'] if w['syllabus_sources'] else None,
                         'observed_count':w['substantive_task_count'] if live else 0,
                         'observed_tariffs':tariffs,'modal_tariff':mode,'exact_mark_tariff':mode if live else None,
                         'used_at_level':live,'use_in_prompts':live,'tariffs_by_paper':w['per_paper'],
                         'source_evidence_ids':w['evidence_ids'],'provenance':'corpus',
                         'primary_assessment_objectives':list('ABCD') if any(t>=8 for t in tariffs) else list('ABC') if any(t>=6 for t in tariffs) else ['A'],
                         'assessment_objectives_provenance':'judgement; actual per-part AO splits retained in corpus evidence, not inferred from word alone'})
    return {'framework_id':'ASSESS-NAM-6144-NSSCO-2026','syllabus_facts_ref':'curriculum/syllabus-facts.json',
            'provenance_rule':'syllabus=transcribed; corpus=counted; judgement=selected teaching/task allocation. Do not conflate them.',
            'assessment_objectives':[{'code':a['code'],'name':a['name'],'description':' '.join(a['can_do']),
                                      'qualification_weight_percent':a['qualification_weight_percent'],'source':a['source'],'provenance':'syllabus'} for a in FACTS['assessment_objectives']],
            'papers':[{**p,'name':'Short structured questions' if p['paper']=='1' else 'Business case study','provenance':'syllabus'} for p in FACTS['papers']],
            'command_words':fw_words,'command_words_listed_but_never_used':[w['word'] for w in fw_words if not w['use_in_prompts']],
            'ao_mark_budget':{'stated_qualification_weight_percent':FACTS['ao_weights']['qualification_percent'],'source':'NIED 6144 PDF p.24, printed p.20'},
            'item_mix_target':{'target_share_percent':FACTS['ao_weights']['qualification_percent'],'note':'Item count is descriptive. Whole-subject marks-equivalent is an approximation; performance AO splits are exact corpus shapes.'},
            'flashcard_subtype_ao_map':[{'subtype':st,'assessment_objectives':list(AO_MAP[st]),'blooms_level':BLOOM[st],'provenance':'judgement grounded in corpus demand'} for st in CW],
            'blooms_taxonomy':{'levels':[{'level':b} for b in ['Remember','Understand','Apply','Analyse','Evaluate','Create']],
                               'by_performance_task':{'short_answer':'Apply','data_response':'Analyse','essay_plan':'Evaluate','case_analysis':'Evaluate'}},
            'marking_patterns':{'P1_c':{'marks':6,'ao_split':{'A':2,'B':2,'C':2}},'P1_d':{'marks':8,'ao_split':{'A':2,'B':2,'C':2,'D':2}},
                                'P2_a':{'marks':8,'ao_split':{'A':2,'B':2,'C':4}},'P2_b':{'marks':12,'ao_split':{'A':4,'B':2,'C':2,'D':4}}}}


def profiles(reg,fw):
    q={'profile_id':'nam-6144-nssco-2026','version':'0.2.0-draft','status':'draft',
       'board':'Namibia Ministry of Education / NIED and DNEA','qualification':'Namibia Senior Secondary Certificate Ordinary Level',
       'subject':'Business Studies','syllabus_code':'6144','syllabus_version':'NIED 2019; filename June 2020 final',
       'examination_years':[2026],'selected_level':'NSSCO Grades 10–11','route':{'route_id':'nssco','name':'Ordinary Level','included_paper_ids':['P1','P2']},
       'language':'English','guided_learning_hours':130,'learner_entry_assumptions':['No prior Business Studies assumed.'],
       'papers':[{'paper_id':'P'+p['paper'],'name':p['name'],'duration_minutes':p['duration_minutes'],'marks':p['marks'],
                  'qualification_weight_percent':p['weight_percent'],'question_basis':p['description'],'assessment_objective_weights':p['ao_split']} for p in fw['papers']],
       'assessment_objectives':[{k:a[k] for k in ['code','name','description','qualification_weight_percent']} for a in fw['assessment_objectives']],
       'command_words':[{'word':c['word'],'meaning':c['meaning']} for c in FACTS['command_words']],
       'scope':{'included_topic_ids':[t['topic_id'] for t in FACTS['content_outline']],'excluded_topic_ids':[],'optional_routes':[]},
       'source_authority':{'curricular':[FACTS['source_document']],'assessment':['2020–2024 official question papers and examiner report Business Studies sections'],
                           'conceptual':['Syllabus concepts and glossary; verified or transparently derived teaching claims still required at authoring.'],
                           'conflict_rule':'Syllabus defines scope; retain report/source defects as issues, never propagate them into new teaching.'},
       'example_selection_rules':['Invented Namibian businesses, British English and N$.','Original cases and datasets; no official question/answer wording.'],
       'notes':['2026 is the learner target examination year, not an inferred syllabus expiry date.','Source and analysis checkpoints approved by Vitalis; plan approval pending.']}
    type_specs=[{'type_id':k,'label':k,'description':f'Semantically selected {k} demand; see objective-provenance.json.',
                 'required_components':STRUCTURES.get(v[0],['meaning']), 'recommended_item_types':v} for k,v in TYPE_SLOTS.items()]
    s={'profile_id':'yyeni-business-6144-nssco-2026','version':'0.2.0-draft','status':'draft','subject_name':'NSSCO Business Studies 6144',
       'language_variant':'British English','purpose':'Standalone teaching, offline revision, source of record for original flashcards and practice; full approved NSSCO scope.',
       'foundational_concepts':['business objectives','stakeholders','cost and profit','cash and liquidity','ownership and control'],
       'objective_types':type_specs,
       'assessment_skill_model':[{'skill_id':a['code'],'label':a['name'],'definition':a['description'],
                                 'authoring_requirements':['Use the exact requested beneficiary and dimension.','Keep AO labels distinct from Bloom demand.']} for a in fw['assessment_objectives']],
       'application_model':{'core_rule':'Use an original relevant business fact and explain why it changes the answer.',
                            'context_dimensions':['activity','ownership','workforce','market','finance','community'],
                            'worked_application_policy':{'minimum_per_major_objective':1,'contrast_required_for_decisions':True,'coverage_dimensions':['constraint','effect','choice']},
                            'pseudo_application_patterns':['A business name without a causal link.','Copied case sentences without processing.']},
       'analysis_model':{'chain_template':['precise point','because mechanism','effect on the requested party'],'rules':['Develop consequences rather than repeat a definition.','Respect how/why and worker/business distinctions.']},
       'evaluation_model':{'judgement_template':['relevant alternatives or positive/negative considerations','case-dependent comparison','choice','supporting decisive reason'],
                           'decision_dimensions':['feasibility','cost','worker/customer effect','objectives','constraints'],
                           'rules':['Assess the actual option(s), not an irrelevant alternative.','One-sided repetition is not a developed judgement.']},
       'depth_model':{'allocation_factors':['Syllabus demand','Direct evidence, not inherited member frequency','Integrated explanations avoid repetition'],
                      'tiers':[{'tier':n,'label':label,'typical_use':label,'indicative_word_range':{'min':0,'max':470},'indicative_item_range':{'min':1,'max':4}} for n,label in enumerate(['precise knowledge','application/procedure','developed analysis/construction','decision'],1)]},
       'quantitative_model':{'required_components':['formula','substitution','result and format','interpretation'],
                             'interpretation_rules':['Ratios to two decimal places under Annexe A.','Preserve % versus x:1.','Use benchmark ratios as contextual references, not universal financial laws.']},
       'legal_and_jurisdiction_model':{'core_rule':'Name the syllabus model and qualify jurisdiction-sensitive legal statements; no invented current rates, statutory lists or registration steps.',
                                      'high_risk_topics':['ownership','worker protection','social security','consumer protection']},
       'learning_item_model':{'item_types':['flashcard','short_answer','data_response','essay_plan','case_analysis'],
                              'flashcard_subtypes':list(CW),'rules':['Every item has AO and Bloom labels.','Every answer is taught in the notes.','Original question wording and contexts.']},
       'terminology_rules':['Follow the subject glossary while retaining its recorded source issues.','Discriminate profit/cash, revenue/profit, market/marketing and production/productivity.'],
       'prohibited_patterns':['No learner-facing exam-frequency or examiner-behaviour claims.','No detailed registration procedures.','No quantitative social-cost-benefit analysis.','No unsupported current legal detail.'],
       'semantic_review_questions':['Can the learner reconstruct the answer from these notes?','Does the task actually exercise the declared outcome and Bloom level?','Are conditions and the requested beneficiary explicit?'],
       'variant_register':[{'term':'limited company','variants':['private','public'],'consequence':'Ownership/share-market access differs; public limited is not synonymous with state owned.'},
                            {'term':'training','variants':['on-the-job','off-the-job'],'consequence':'Setting, cost and disruption differ.'},
                            {'term':'production methods','variants':['job','batch','flow'],'consequence':'Volume, variety and sequence differ. This family trigger must not match an incidental reference to production cost.'}],
       'answer_structures':{**STRUCTURES,'SYNTH':['input|brief','design|draft|document','output|criterion']},
       'conditioned_mechanisms':[{'mechanism_id':'CM-6144-SCALE','name':'Growth lowers unit cost','asserted_when':[r'\b(?:growth|larger|expand)\b',r'\b(?:lower|reduce|fall)\b',r'\b(?:unit cost|average cost)\b'],
                                 'required_conditions':[{'name':'Coordination/diseconomies may offset scale savings','any_of':[r'\bdiseconom',r'\bprovided\b',r'\bif\b',r'\bcoordination\b']}]}],
       'depictions':{'chart_model':'none','note':'Break-even renderer does not model this subject’s charts. Use original source data and a subject-local deterministic renderer; preserve C35/C41 not_run and validate graphics separately.'},
       'slot_plan':{'subtypes_by_objective_type':TYPE_SLOTS,'subtypes_by_tier':{n:[] for n in range(1,5)},
                    'high_tariff':{'threshold':99,'adds':[]}, 'top_up':[],
                    'command_words_by_subtype':{**CW,'APP':['Explain','Draw']},
                    'tariff_overrides':{'DEF:Define':2,'FEATURE:State':2,'APP:Explain':6,'APP:Draw':8,
                                        'DIST:Distinguish':6,'CHAIN:Explain':6,'EVAL:Evaluate':8,
                                        'PROC:Explain':6,'PROC:Draw':6,'CALC:Calculate':6,'INTERP:Analyse':8,'MISCON:Explain':6,'SYNTH:Explain':8},
                    'misconception_slots':'one_per_entry',
                    'performance_tasks':[
                        {'item_type':'short_answer','brief':'An original Paper 1 20-mark question: short knowledge 4+2, developed application/analysis 6, judgement 8. Use this topic’s performance-blueprints.json for exact objectives and command words.','ao_split':{'A':10,'B':4,'C':4,'D':2}},
                        {'item_type':'data_response','brief':'An original Paper 2 20-mark case pair: analytical 8 plus evaluative 12. Use this topic’s performance-blueprints.json for exact scope and commands.','ao_split':{'A':6,'B':4,'C':6,'D':4}},
                        {'item_type':'essay_plan','brief':'A compact 12-mark decision plan on this topic’s specified comparison; use performance-blueprints.json. No full extra essay or new content.','ao_split':{'A':4,'B':2,'C':2,'D':4}},
                        {'item_type':'case_analysis','brief':'Two linked 12-mark decisions: first assess the original case, then reassess it after one stated constraint changes. Explain why the judgement changes or holds. Use performance-blueprints.json. Each part carries A4/B2/C2/D4; reuse taught scope with original facts.','ao_split':{'A':8,'B':4,'C':4,'D':8}}]}}
    (WS/'qualification-profile.yaml').write_text(yaml.safe_dump(q,sort_keys=False,allow_unicode=True))
    (WS/'subject-profile.yaml').write_text(yaml.safe_dump(s,sort_keys=False,allow_unicode=True))


def glossary():
    text=(WS/'planning/syllabus-layout.txt').read_text();pages={int(k):v for k,v in re.findall(r'--- PDF PAGE (\d+) ---\n(.*?)(?=\n--- PDF PAGE|\Z)',text,re.S)}
    entries=[];current=None;started=False
    for page in range(29,34):
        for line in pages[page].splitlines():
            if not line.strip() or 'NSSCO Business Studies Syllabus' in line or re.match(r'^\s*\d+\s*$',line):continue
            if line.startswith('AIDA model'):started=True
            if not started:continue
            m=re.match(r'^([A-Za-z][A-Za-z’ /-]*?[a-z])\s{2,}(.+)$',line)
            if m:
                current={'term':m.group(1).strip(),'meaning':m.group(2).strip(),'source':{'pdf_page':page,'printed_page':page-4,'provenance':'syllabus'}};entries.append(current)
            elif current is not None and line.startswith(' '):current['meaning']+=' '+' '.join(line.split())
    assert len(entries)>=55,len(entries)
    write(CUR/'glossary.json',{'glossary_id':'GLOSSARY-6144-NSSCO','entries':entries,
                              'source_issues':['Syllabus direct/variable and indirect/fixed wording is a simplified model; do not assert these cost classifications are universally interchangeable.','Social costs/benefits are used as external costs/benefits in the syllabus glossary; distinguish this syllabus usage from broader definitions.','Use inventory-turnover actual meaning while retaining the recorded classification discrepancy.']})


def main():
    if any((WS/'topics').glob('*/claims/canonical_claim_ledger.json')):
        raise SystemExit('Production authoring exists. Reopen planning explicitly before regenerating shared curriculum inputs; this script must not overwrite a live author packet.')
    reg,crosswalk,members,prov=registry()
    write(CUR/'objective_registry.json',reg)
    write(CUR/'objective-provenance.json',{'sources':prov,'member_count':len(members),'decisions':'Member/type/depth choices are planning judgements. No inherited frequencies; no source wording is presented as a new official bullet.'})
    write(CUR/'objective-crosswalk.json',{'syllabus_bullets':crosswalk,'members':[{'source_member':list(key),'objective_id':value} for key,value in members.items()]})
    adapt_evidence(crosswalk,members,reg)
    fw=framework();write(CUR/'assessment-framework.json',fw)
    profiles(reg,fw);glossary()
    print('Registry:',len(reg['objectives']),'nodes;',len(reg['objectives'])-22,'assessable targets;',len(members),'named member targets')


if __name__=='__main__':main()
