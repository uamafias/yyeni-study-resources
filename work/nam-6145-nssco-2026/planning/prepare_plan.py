"""Step 4 curriculum inputs. Does not author or publish learner resources."""
import collections
import copy
import json
import re
from pathlib import Path
import yaml
from review_fixes import extend_types, improve_nodes, improve_profile, scope_fixes

WS=Path(__file__).resolve().parents[1]
def read(p):return json.loads((WS/p).read_text())
def write(p,x):(WS/p).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
facts=read('curriculum/syllabus-facts.json')
targets=facts['ao_weights']['derived_qualification_percent']
refs=read('planning/objective-reference.json')['objectives']

# Explicit lists are expanded without losing the original source-bullet reference.
MEMBERS={
 '1.2.1':'land|labour|capital|entrepreneurship',
 '1.2.2':'market economic system|planned economic system|mixed economic system',
 '1.3.1':'specialisation|division of labour',
 '1.3.3':'individual specialisation|regional specialisation|national specialisation',
 '2.1.2':'sole proprietor|partnership|private company|public limited company|multinational business|co-operative|close corporation|public corporation',
 '2.2.4':'white-collar union|blue-collar union|craft union',
 '2.3.2':'functions of money|qualities of money|types of money',
 '2.3.5':'central bank|stock exchange|commercial bank',
 '3.2.1':'demand|supply',
 '3.2.4':'changes in demand conditions|changes in supply conditions',
 '3.3.1':'price elasticity of demand|price elasticity of supply',
 '3.3.2':'application of price elasticity of demand|application of price elasticity of supply',
 '3.3.3':'calculation of price elasticity of demand|calculation of price elasticity of supply',
 '3.5.1':'pricing and output in perfect competition|pricing and output in monopoly',
 '4.1.1':'wage factors in occupational choice|non-wage factors in occupational choice',
 '4.2.2':'male and female earnings|skilled and unskilled earnings|private and public sector earnings|agricultural earnings|manufacturing earnings|service-sector earnings',
 '4.3.1':'income-group spending patterns|income-group saving patterns|income-group borrowing patterns',
 '4.3.2':'motives for spending|motives for saving|motives for borrowing',
 '5.3.1':'total cost|average cost|fixed cost|variable cost',
 '5.3.2':'total revenue|average revenue',
 '5.4.1':'horizontal integration|forward vertical integration|backward vertical integration',
 '5.4.5':'size of market|capital available|organisation of the firm',
 '6.1.1':'government as a producer of goods|government as a provider of services|government as an employer',
 '6.2.2':'full employment|prevention of inflation|economic growth|redistribution of income|balance of payments stability',
 '6.2.3':'fiscal policy|monetary policy',
 '6.2.4':'direct taxes|indirect taxes|progressive taxation|proportional taxation|regressive taxation',
 '7.3.1':'Gross Domestic Product|Gross National Product|National Income',
 '7.3.2':'output method of national-income measurement|income method of national-income measurement|expenditure method of national-income measurement',
 '7.4.3':'absolute advantage|comparative advantage',
 '8.1.1':'developed economy|developing economy',
 '8.1.3':'birth rate|death rate|fertility rate|net migration',
 '9.1.1':'social and private costs and benefits|short-term and long-term costs and benefits|conservation and exploitation of resources|free trade and protection|public and private expenditure',
}
TYPES={
 '1.1':'concept comparison evaluation', '1.2':'list list evaluation', '1.3':'list mechanism list',
 '2.1':'comparison list evaluation','2.2':'concept concept mechanism list mechanism evaluation concept',
 '2.3':'mechanism list quantitative evaluation list',
 '3.1':'concept comparison','3.2':'list diagram diagram mechanism diagram',
 '3.3':'list evaluation quantitative','3.4':'concept mechanism','3.5':'evaluation',
 '4.1':'comparison','4.2':'mechanism comparison mechanism comparison','4.3':'list mechanism mechanism',
 '5.1':'evaluation concept mechanism mechanism','5.2':'concept quantitative mechanism mechanism mechanism',
 '5.3':'list list mechanism mechanism','5.4':'list diagram mechanism mechanism evaluation',
 '6.1':'mechanism','6.2':'concept evaluation list comparison evaluation mechanism','6.3':'mechanism mechanism evaluation evaluation evaluation',
 '7.1':'quantitative comparison mechanism','7.2':'mechanism mechanism mechanism evaluation','7.3':'list list mechanism','7.4':'mechanism mechanism quantitative',
 '8.1':'list evaluation mechanism mechanism','8.2':'comparison mechanism mechanism','9.1':'evaluation',
}
type_ids={'concept':'economics_concept','comparison':'economics_comparison','mechanism':'economics_mechanism',
          'quantitative':'economics_quantitative','diagram':'economics_diagram','evaluation':'economics_policy_evaluation','list':'economics_list'}
type_words={
 'concept':['Define','Describe','Explain'], 'comparison':['Define','Explain','Outline'],
 'mechanism':['Explain','Analyse','Describe'], 'quantitative':['Define','Calculate','Explain'],
 'diagram':['Explain','Analyse','Illustrate'], 'evaluation':['Define','Explain','Discuss','Evaluate'],
 'list':['Identify','Describe','Explain'],
}
extend_types(type_ids, type_words)
nodes=[]
decomposition=[]
for topic in facts['topics']:
    tid=topic['topic_id']; root='OBJ-6145-'+tid
    base={'topic_id':tid,'level':'NSSCO','route_status':'core','mandatory':True,
          'prerequisite_ids':[],'related_ids':[],'status':'planned','papers':['1','2'],
          'syllabus_page':topic['source']['page'],'sub_topic':tid,'sub_topic_heading':topic['topic_title'],
          'source_coverage':{'rating':0,'action':'generate_gap','rationale':'Original teaching text derived from the official syllabus and mined assessment demand; no third-party teaching text is approved for reproduction.'}}
    nodes.append(dict(base,objective_id=root,parent_id=None,syllabus_text=f"{tid} {topic['topic_title']}",
                      learner_objective=topic['topic_title'],objective_type='economics_topic',
                      assessment_objectives=['A','B','C'],command_words=[],depth_tier=4))
    types=TYPES[tid].split(); assert len(types)==len(topic['specific_objectives'])
    for number,(text,kind) in enumerate(zip(topic['specific_objectives'],types),1):
        oid=f'OBJ-6145-{tid}-{number:02}'; key=f'{tid}.{number}'
        tier=1 if kind=='concept' else 4 if kind=='evaluation' else 3 if kind in ('mechanism','diagram','quantitative') else 2
        aos=['A','C'] if kind=='evaluation' else ['A','B'] if tier>=2 else ['A']
        node=dict(base,objective_id=oid,parent_id=root,syllabus_text=text,learner_objective=text[0].upper()+text[1:],
                  objective_type=type_ids[kind],assessment_objectives=aos,command_words=type_words[kind],depth_tier=tier)
        nodes.append(node)
        member_ids=[]
        for j,member in enumerate(MEMBERS.get(key,'').split('|') if key in MEMBERS else [],1):
            mid=f'{oid}-M{j:02}'; member_ids.append(mid)
            mkind=('quantitative' if member.startswith('calculation of') else
                   'evaluation' if key=='3.5.1' else 'mechanism' if key in ('3.3.2','4.3.2') else
                   'comparison' if key in ('4.1.1','4.2.2','9.1.1') else 'concept')
            nodes.append(dict(base,objective_id=mid,parent_id=oid,
                syllabus_text=member,syllabus_guidance=f'Explicit member of: {text}',
                learner_objective=('Calculate and interpret ' if mkind=='quantitative' else 'Explain ' if mkind in ('mechanism','comparison') else 'Evaluate ' if mkind=='evaluation' else 'Describe ')+member,
                objective_type=type_ids[mkind],assessment_objectives=['A','B'] if mkind!='evaluation' else ['B','C'],
                command_words=type_words[mkind],depth_tier=1 if mkind=='concept' else 4 if mkind=='evaluation' else 2))
        if member_ids:
            decomposition.append({'source_objective_id':oid,'member_objective_ids':member_ids,
                'source_bullet':text,'provenance':'syllabus list decomposition; integration/tax/national-income subtypes additionally evidenced by corpus',
                'coverage_rule':'Teach the source relationship as well as each member. Counts on the source bullet do not transfer automatically to every member.'})
improve_nodes(nodes)
scope_fixes()
assert len({n['objective_id'] for n in nodes})==len(nodes)
write('curriculum/objective_registry.json',{'registry_id':'OBJREG-NAM-6145-NSSCO-2026',
    'qualification_profile_id':'nam-6145-nssco-2026','subject_profile_id':'subject-6145-nssco-2026',
    'authority':facts['source_document'],'generated_at':'2026-11-07',
    'granularity_note':f'All 96 original specific-objective bullets retained with stable mining IDs; {len(decomposition)} explicit or corpus-supported lists further decomposed into member objectives. Source relationships remain assessable.',
    'papers_note':'Both papers cover the syllabus; paper AO splits do not allocate individual topics exclusively.', 'objectives':nodes})
write('planning/decomposition-map.json',{'entries':decomposition,'node_count':len(nodes),'assessable_count':len(nodes)-28})
misconceptions=read('curriculum/misconceptions.json')
for entry in misconceptions['entries']:
    entry['n']=len(entry['source_evidence'])
    entry['a']=entry['confusion']
    entry['test']=entry['discriminating_test']
write('curriculum/misconceptions.json',misconceptions)

# Exposure remains measured on the source bullet. Member rows explicitly have no
# directly mapped QP evidence; they receive no borrowed frequency or marks.
exp=read('curriculum/exam-exposure.json')
existing={e['objective_id']:e for e in exp['objectives']}
for n in nodes:
    if not n['parent_id'] or n['objective_id'] in existing:continue
    exp['objectives'].append({'objective_id':n['objective_id'],'topic_id':n['topic_id'],
        'syllabus_text':n['syllabus_text'],'exam_exposure':'unprobed_2020_2024',
        'evidence':{'question_parts_naming_it':0,'distinct_series':0,'max_mark_tariff':0,'command_words_observed':{},
                    'marks_examined':0,'series':[],'tariffs':{},'modal_tariff':None,'evidence_ids':[]},
        'mapping_note':'Member coverage is explicit; source-bullet evidence is not multiplied across members. Zero direct mappings is not proof of no assessment.'})
write('curriculum/exam-exposure.json',exp)

cw_counts=read('assessment-evidence/command-word-counts.json')['commands']
cw_def={c['word']:c for c in facts['command_words']}
commands=[]
for c in cw_counts:
    d=cw_def.get(c['word']); word=c['word'].capitalize()
    permitted=c['use_in_prompts']
    commands.append({'word':word,'meaning':d['meaning'] if d else 'Observed task wording; interpret the complete question demand.',
        'meaning_provenance':'syllabus' if d else 'judgement','in_syllabus_table':bool(d),
        'syllabus_page':d['source']['page'] if d else None,'syllabus_verbatim':d['verbatim'] if d else None,
        'primary_assessment_objectives':['A','B','C'],'assessment_objectives_provenance':'judgement',
        'observed_count':c['count'],'observed_tariffs':c['tariff_counts'],'modal_tariff':c['modal_tariff'],
        'exact_mark_tariff':c['modal_tariff'] if permitted else None,'used_at_level':permitted,'use_in_prompts':permitted,
        'papers':c['per_paper'],'verdict':c['verdict'],'observation_provenance':'corpus: 2020–2024 QPs; one primary demand per part',
        'embedded_only_count':c['embedded_only_count']})
subtypes={
 'DEF':(['A'],'Remember'),'FEATURE':(['A'],'Remember'),'DIST':(['A'],'Understand'),
 'WHY':(['A','B'],'Understand'),'MECH':(['B'],'Analyse'),'CHAIN':(['B'],'Analyse'),
 'BEN':(['B'],'Analyse'),'LIM':(['B'],'Analyse'),'EVAL':(['C'],'Evaluate'),
 'APP':(['A'],'Apply'),'INTERP':(['B'],'Analyse'),'CALC':(['B'],'Apply'),
 'DIAGRAM':(['B'],'Apply'),'MISCON':(['A','B'],'Understand'),'SYNTH':(['B','C'],'Analyse')}
aos=[{'code':a['code'],'name':a['name'],'description':' '.join(a['can_do']),
       'qualification_weight_percent':targets[a['code']],
       'provenance':'name/definition: syllabus PDF17; overall weight: calculation from PDF19 and equal paper weights'} for a in facts['assessment_objectives']]
framework={'framework_id':'ASSESS-NAM-6145-NSSCO-2026','generated_by':'planning/prepare_plan.py',
 'authority':facts['source_document'],'syllabus_facts_ref':'curriculum/syllabus-facts.json',
 'assessment_objectives':aos,'papers':facts['papers'],'command_words':commands,
 'command_words_listed_but_never_used':[],
 'flashcard_subtype_ao_map':[{'subtype':k,'assessment_objectives':v[0],'blooms_level':v[1]} for k,v in subtypes.items()],
 'item_mix_target':{'target_share_percent':targets,'basis':'marks-equivalent, not item count'},
 'ao_mark_budget':{'stated_qualification_weight_percent':targets,
     'provenance':'CALCULATED overall target, not a separately stated syllabus row. Legacy generator key retained; see syllabus-facts.json for the exact computation.',
     'per_component_percent':facts['ao_weights']['per_component_percent']},
 'blooms_taxonomy':{'levels':[{'level':x} for x in ['Remember','Understand','Apply','Analyse','Evaluate','Create']],
                    'by_performance_task':{'short_answer':'Remember','data_response':'Analyse','essay_plan':'Evaluate'}},
 'tariff_rule':'Choose only observed command/tariff pairs; the whole task determines demand and marking. Per-part AOs outside explicitly labelled sections are judgements.'}
write('curriculum/assessment-framework.json',framework)

profile={'profile_id':'nam-6145-nssco-2026','version':'0.1.0-draft','status':'draft',
 'board':'Namibia: NIED curriculum; DNEA assessment','qualification':'NSSCO','subject':'Economics','syllabus_code':'6145',
 'syllabus_version':'NIED 2018; implementation 2019; first examination 2020','examination_years':[2026],
 'selected_level':'Ordinary Level, Grades 10–11','language':'English',
 'route':{'route_id':'nssco-both-papers','name':'Full NSSCO','included_paper_ids':['P1','P2'],
          'notes':'Both compulsory. P2 offers 120 marks but a candidate attempts 80.'},
 'prior_teaching':'No prior Economics study assumed; ordinary school numeracy and English reading.',
 'learner_entry_assumptions':['No prior Economics qualification required.'],
 'assessment_objectives':aos,'papers':[dict(p,paper_id='P'+p['paper'],qualification_weight_percent=p['weight_percent']) for p in facts['papers']],
 'command_words':[c['word'] for c in commands if c['use_in_prompts']],
 'scope':{'included_topic_ids':[t['topic_id'] for t in facts['topics']], 'excluded_topic_ids':[]},
 'source_authority':{'curricular':[facts['source_document']],'assessment':['assessment-evidence/extraction-manifest.json'],
    'conceptual':['curriculum/glossary.json','curriculum/syllabus-facts.json'],
    'conflict_rule':'Syllabus sets scope; QP sets tariff; report suggests credit structure. Resolve discrepancies explicitly; do not copy them.'},
 'notes':['Overall AO targets are calculated 39/25.5/35.5.','2021–2023 QPs are marked First Proof. Standalone mark schemes and 2025 QPs absent.','NSSCO pilot remains unconfirmed; Jeremy explicitly approved proceeding.']}
(WS/'qualification-profile.yaml').write_text(yaml.safe_dump(profile,sort_keys=False,allow_unicode=True))

structures={
 'DEF':['meaning|definition','key term|essential element'], 'FEATURE':['characteristic|feature','distinction|example'],
 'DIST':['difference|boundary','test|contrast'],'WHY':['reason|because','consequence|purpose'],
 'MECH':['starting change|initial change','because|mechanism','consequence|therefore'],
 'CHAIN':['starting change|initial change','because|mechanism','consequence|therefore'],
 'BEN':['benefit|advantage','because|mechanism','agent|firm|worker|consumer|government'],
 'LIM':['limitation|disadvantage','because|mechanism','agent|firm|worker|consumer|government'],
 'EVAL':['argument for|benefit','argument against|limitation','condition|trade-off','judgement|conclusion'],
 'APP':['context|scenario','reason|because','conclusion|consequence'],
 'INTERP':['relationship|pattern','evidence|comparison','explanation|reason'],
 'CALC':['formula','substitution|working','units|interpretation'],
 'DIAGRAM':['axes|labels','original equilibrium','change|control','explanation|interpretation'],
 'MISCON':['confusion','boundary|difference','test|distinguish'],
 'SYNTH':['link|relationship','consequence','condition|judgement'],
 'short_answer':['meaning|identification','separate points|distinct elements','marks|allocation'],
 'data_response':['context|data','mechanism|explanation','both sides|opposing arguments','judgement|conclusion','marks|allocation'],
 'essay_plan':['argument for','argument against','condition','judgement','marks|allocation']}
conditions=[
 {'mechanism_id':'CM-6145-PED-REVENUE','name':'Price change and total revenue',
  'asserted_when':[r'\bprice (?:rise|rises|increase|increases)\b',r'\btotal revenue\b',r'\b(?:raises|increases|higher)\b'],
  'required_conditions':[{'name':'Relevant demand elasticity and other demand conditions unchanged','any_of':[r'\binelastic\b',r'\belasticity\b',r'\bother things equal\b']}],
  'rationale':'A price increase does not universally raise revenue.'},
 {'mechanism_id':'CM-6145-SCALE','name':'Larger output and average cost',
  'asserted_when':[r'\b(?:larger|increased|higher) output\b',r'\baverage cost\b',r'\b(?:fall|falls|lower|reduce)\b'],
  'required_conditions':[{'name':'A mechanism such as fixed-cost spreading or economies of scale','any_of':[r'\bfixed costs?\b',r'\beconomies of scale\b',r'\bcapacity\b']}],
  'rationale':'Increasing output and increasing scale are distinct; average costs need not fall indefinitely.'},
 {'mechanism_id':'CM-6145-CURRENCY','name':'Depreciation and trade performance',
  'asserted_when':[r'\bdepreciat\w*\b',r'\b(?:improves|improve|better)\b',r'\b(?:current account|trade balance)\b'],
  'required_conditions':[{'name':'Export demand or supply response and import demand response','any_of':[r'\brespond\w*\b',r'\belastic\w*\b',r'\bcapacity\b']}],
  'rationale':'Use plain-language response conditions; no advanced named trade condition.'},
 {'mechanism_id':'CM-6145-WAGE','name':'Minimum wage and unemployment',
  'asserted_when':[r'\bminimum wage\b',r'\b(?:raises|increases|causes|creates)\b',r'\bunemployment\b'],
  'required_conditions':[{'name':'Binding price floor in the stated competitive labour-market model','any_of':[r'\babove (?:the )?(?:market|equilibrium) wage\b',r'\bbinding\b']}],
  'rationale':'Elasticity affects magnitude, not whether labour demand must be elastic for a binding floor to create excess supply.'},
 {'mechanism_id':'CM-6145-GROWTH','name':'Growth and living standards',
  'asserted_when':[r'\beconomic growth\b',r'\b(?:raises|improves|increases)\b',r'\bliving standards\b'],
  'required_conditions':[{'name':'Population, distribution and social/environmental costs considered','any_of':[r'\bdistribut\w*\b',r'\bper (?:person|capita)\b',r'\bexternal cost\b',r'\benvironment\w*\b']}],
  'rationale':'Aggregate output does not guarantee every household is better off.'}]
slot_plan={
 'note':'Subject-specific shapes only; no MCQ component. No automatic AO top-up or count padding. Overall targets are derived from the syllabus, not a newly stated weight table.',
 'subtypes_by_objective_type':{'economics_list':['FEATURE'],
      'economics_concept':['DEF','FEATURE'],'economics_comparison':['DIST','APP'],
      'economics_mechanism':['MECH','APP'],'economics_diagram':['DIAGRAM','INTERP'],
      'economics_quantitative':['CALC','INTERP'],'economics_policy_evaluation':['BEN','LIM','EVAL']},
 'subtypes_by_tier':{1:[],2:[],3:[],4:[]},
 'high_tariff':{'threshold':7,'adds':[]},'top_up':[],'misconception_slots':'one_per_entry',
 'command_words_by_subtype':{k:[v] for k,v in {'DEF':'Define','FEATURE':'Identify','DIST':'Explain','WHY':'Explain','MECH':'Explain','CHAIN':'Analyse','BEN':'Explain','LIM':'Explain','EVAL':'Evaluate','APP':'Explain','INTERP':'Analyse','CALC':'Calculate','DIAGRAM':'Explain','MISCON':'Explain','SYNTH':'Discuss'}.items()},
 'tariff_overrides':{'DEF:Define':1,'FEATURE:Identify':2,'DIST:Explain':2,'MECH:Explain':4,'CHAIN:Analyse':4,
     'BEN:Explain':4,'LIM:Explain':4,'EVAL:Evaluate':7,'APP:Explain':2,'INTERP:Analyse':4,
     'CALC:Calculate':2,'DIAGRAM:Explain':7,'MISCON:Explain':2,'SYNTH:Discuss':7},
 'performance_tasks':[
   {'item_type':'short_answer','brief':'Original Paper 1 Section A practice: four separate 2-mark short questions (8 marks total), each retrieving a precise meaning, distinction or named feature from this topic. Give the distinct credit elements and allocations. No multiple-choice set.','ao_split':{'A':8}},
   {'item_type':'data_response','brief':'Original 20-mark structured economic scenario with supplied data: Describe (6), Explain (7), Discuss (7). Use the topic’s own specified mechanisms and a balanced decision in context. Include a diagram where the topic requires it; otherwise use a short table. The A6/B7/C7 split is a planner practice allocation, not a transcribed universal mark scheme.','ao_split':{'A':6,'B':7,'C':7}},
   {'item_type':'essay_plan','brief':'Two contrasting 7-mark Evaluate plans (14 marks total) within this topic: change the economic agent, time horizon or constraint between the two scenarios. For each develop an argument for, an argument against, the decisive condition and a justified judgement. Explain each allocation; do not add a conclusion mark above seven or reproduce an official rubric.','ao_split':{'C':14}}]}
slot_plan['note']+=' Short 2-mark APP and DIST slots model Paper 1 Section A, which the syllabus assigns to AO A even where Bloom demand is Apply or Understand. MECH/BEN/LIM at 4 marks carry B; evaluation is credited separately. A mechanism needs one MECH and one short application, not a duplicate automatic CHAIN. Paired evaluation plans practise transfer under a changed condition, not repeated facts.'
sp={'profile_id':'subject-6145-nssco-2026','version':'0.1.0-draft','status':'draft','subject_name':'NSSCO Economics 6145',
 'language_variant':'British English','purpose':'Original full-depth notes and retrieval/application/evaluation practice for Namibian learners.',
 'answer_structures':structures,'slot_plan':slot_plan,'conditioned_mechanisms':conditions,
 'variant_register':[{'term':'vertical integration','variants':['forward','backward'],'consequence':'A later production stage differs from an earlier stage.'},
   {'term':'price elasticity','variants':['demand','supply'],'consequence':'Quantity demanded and quantity supplied use different mechanisms and symbols.'},
   {'term':'population growth','variants':['natural','migration'],'consequence':'Natural increase excludes migration; total growth includes net migration.'}],
 'depictions':{'chart_model':'none','code_fence_languages':[]},
 'depiction_rule':{'mode':'tables_and_construction','note':'The standard renderer supports break-even charts, not demand/supply or PPF diagrams. Supply a numerical schedule and precise axes/curve/equilibrium construction and interpretation for the learner to plot. Do not substitute an unrelated chart or hand-author picture/code fences. A graphical production extension needs a separate reviewed renderer.'},
 'prohibited_patterns':['Examiner or mark-scheme wording in learner material.','Unconditional causal guarantees.','Generic business cases unrelated to the specified economic mechanism.','Treating a calculation as an interpretation.','Legal shareholder limits, tax rates or current statistics asserted without a verified source.'],
 'legal_and_jurisdiction_model':{'core_rule':'Teach economic ownership/liability distinctions; do not invent current legal limits or statutory details. Verify jurisdiction-specific assertions before authoring them.','high_risk_topics':['2.1','2.2','6.3']},
 'glossary_homonyms':['Production differs from productivity.','Public limited company differs from public corporation.','Transfer earnings differ from transfer payments.','Budget balance differs from trade balance.'],
 'authoring_constraints':['All scenarios use invented entities and labelled teaching data, N$ and Namibian/southern African contexts.','Notes teach every cited claim; cards are independently answerable.','Keep short-run diminishing returns separate from long-run scale effects.','All lists in decomposition-map.json must be covered member by member.']}
improve_profile(sp)
(WS/'subject-profile.yaml').write_text(yaml.safe_dump(sp,sort_keys=False,allow_unicode=True))
write('curriculum/unit_titles.json',{str(i):t['title'].split(': ',1)[1].title() for i,t in enumerate(facts['content_outline'],1)})
print(f'{len(nodes)-28} assessable objectives; {len(decomposition)} decomposed lists; {len(nodes)} total nodes.')
