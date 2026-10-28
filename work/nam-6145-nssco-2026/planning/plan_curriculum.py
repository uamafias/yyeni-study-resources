"""Step 4, 6145 only. Semantic classifications/decomposition are planner decisions."""
import collections
import copy
import json
import re
from pathlib import Path

import yaml

WS = Path(__file__).resolve().parents[1]
ROOT = WS.parents[1]
CUR = WS / 'curriculum'
E = WS / 'assessment-evidence'
load = lambda p: json.loads(p.read_text())
dump = lambda p,x: p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
facts = load(CUR/'syllabus-facts.json')
evidence = load(E/'assessment_evidence.json')
original = load(E/'syllabus-objective-index.json')['objectives']
commands = load(E/'command-word-analysis.json')
qpid,spid = 'nam-6145-nssco-2026','subject-nam-6145-economics'

# One classification per original bullet, assigned from its demand, not a token matcher.
TYPES = {
 '1.1':'concept mechanism policy_evaluation','1.2':'classification comparison policy_evaluation',
 '1.3':'definition cause_effect classification','2.1':'comparison classification policy_evaluation',
 '2.2':'definition definition mechanism classification cause_effect policy_evaluation mechanism',
 '2.3':'mechanism classification quantitative cause_effect policy_evaluation',
 '3.1':'definition classification','3.2':'diagram diagram diagram cause_effect diagram',
 '3.3':'definition mechanism quantitative','3.4':'definition classification','3.5':'policy_evaluation',
 '4.1':'comparison','4.2':'cause_effect comparison cause_effect comparison',
 '4.3':'comparison cause_effect cause_effect',
 '5.1':'mechanism definition cause_effect policy_evaluation',
 '5.2':'definition quantitative mechanism cause_effect cause_effect',
 '5.3':'classification quantitative cause_effect cause_effect',
 '5.4':'classification mechanism mechanism cause_effect cause_effect',
 '6.1':'mechanism','6.2':'definition policy_evaluation comparison classification mechanism cause_effect',
 '6.3':'policy_evaluation mechanism mechanism mechanism mechanism',
 '7.1':'quantitative classification cause_effect',
 '7.2':'classification cause_effect cause_effect policy_evaluation',
 '7.3':'classification classification mechanism','7.4':'cause_effect cause_effect quantitative',
 '8.1':'comparison cause_effect classification cause_effect',
 '8.2':'classification comparison cause_effect','9.1':'policy_evaluation'
}
# Explicit lists decomposed without losing the integrated parent learning outcome.
MEMBERS = {
 '1.2-01':['land','labour','capital','entrepreneurship'],
 '1.2-02':['market economic system','planned economic system','mixed economic system'],
 '1.3-03':['individual specialisation','regional specialisation','national specialisation'],
 '2.1-02':['sole proprietor','partnership','private company','public company','multinational company','co-operative','close corporation','public corporation'],
 '2.2-04':['white collar union','blue collar union','craft union'],
 '2.3-02':['functions of money','qualities of money','types of money'],
 '2.3-05':['central bank','stock exchange','commercial bank'],
 '3.1-02':['physical market','digital market'],
 '3.2-01':['demand','supply'],
 '3.3-01':['price elasticity of demand','price elasticity of supply'],
 '3.3-03':['calculation of price elasticity of demand','calculation of price elasticity of supply'],
 '3.4-02':['purpose of advertising','methods of advertising'],
 '3.5-01':['perfect competition pricing and output','monopoly pricing and output'],
 '4.1-01':['wage factors in occupational choice','non-wage factors in occupational choice'],
 '4.2-02':['male and female earnings','skilled and unskilled earnings','private and public sector earnings','agricultural, manufacturing and service-sector earnings'],
 '4.2-04':['economic rent','transfer earnings'],
 '4.3-01':['spending patterns by income','saving patterns by income','borrowing patterns by income'],
 '5.3-01':['total cost','average cost','fixed cost','variable cost'],
 '5.3-02':['total revenue','average revenue'],
 '6.1-01':['government as producer','government as employer'],
 '6.2-02':['full employment','price stability','economic growth','redistribution of income','balance of payments stability'],
 '6.2-03':['fiscal policy','monetary policy'],
 '7.4-03':['absolute advantage from output data','comparative advantage from opportunity-cost data'],
 '7.3-01':['Gross Domestic Product','Gross National Product','National Income'],
 '8.1-03':['birth rate','death rate','fertility rate','net migration'],
 '9.1-01':['social and private costs and benefits','short-run and long-run costs and benefits','conserving versus exploiting resources','free trade versus protection','public versus private expenditure']
}
# Unnamed member sets are judgement needed to realise an open syllabus list;
# they are explicitly labelled in the crosswalk, not attributed as printed lists.
OPEN_LISTS = {
 '2.3-02:functions of money':['medium of exchange','unit of account','store of value','standard of deferred payment'],
 '2.3-02:qualities of money':['durability','portability','divisibility','general acceptability','scarcity','homogeneity'],
 '2.3-02:types of money':['cash','bank deposits','electronic means of payment'],
 '5.4-01':['horizontal integration','forward vertical integration','backward vertical integration','conglomerate integration'],
 '5.4-02':['technical economies of scale','purchasing economies of scale','financial economies of scale','marketing economies of scale','managerial economies of scale','risk-bearing economies of scale'],
 '5.4-03':['communication diseconomies','co-ordination diseconomies','control and motivation diseconomies'],
 '6.2-04':['direct tax','indirect tax','progressive tax','proportional tax','regressive tax'],
 '7.1-02':['demand-pull inflation','cost-push inflation','monetary inflation'],
 '7.2-01':['employment','unemployment','labour force participation'],
 '7.2-02':['cyclical unemployment','structural unemployment','seasonal unemployment','frictional unemployment'],
 '7.3-02':['output method','income method','expenditure method'],
 '8.2-01':['real income per head','life expectancy','education and literacy','health, housing and sanitation indicators']
}
for k,v in OPEN_LISTS.items():
    if ':' not in k:MEMBERS[k]=v

subjects = [t for th in facts['content_outline'] for t in th['topics']]
registry=[];crosswalk=[]
type_labels = sorted({x for v in TYPES.values() for x in v.split()}|{'member','calculation','quantitative_family'})
for t in subjects:
    tid=t['topic_id']; rootid='OBJ-6145-'+tid
    base={'objective_id':rootid,'parent_id':None,'topic_id':tid,'syllabus_text':tid+' '+t['title'],
          'learner_objective':t['title'],'level':'NSSCO','route_status':'core','mandatory':True,
          'objective_type':'economics_container','assessment_objectives':['A','B','C'],
          'command_words':['Define','Explain','Discuss'],'prerequisite_ids':[],'related_ids':[],
          'depth_tier':4,'source_coverage':{'rating':0,'action':'generate_gap','rationale':'Original teaching derived from the approved syllabus and mined 6145 evidence; no third-party notes approved.'},
          'status':'planned','syllabus_page':t['source']['pdf_page'],'papers':['1','2']}
    registry.append(base)
    types=TYPES[tid].split();assert len(types)==len(t['specific_objectives']),tid
    for n,(o,typ) in enumerate(zip(t['specific_objectives'],types),1):
        anchor=f'{tid}-{n:02d}';oid='OBJ-6145-'+anchor
        obj=copy.deepcopy(base);obj.update(objective_id=oid,parent_id=rootid,
          syllabus_text=o['verbatim'],learner_objective=o['verbatim'][0].upper()+o['verbatim'][1:],
          objective_type='economics_'+typ,depth_tier=4 if typ=='policy_evaluation' else 3 if typ in {'cause_effect','mechanism','diagram','quantitative'} else 2,
          command_words=['Define','Explain','Use','Discuss','Evaluate','Calculate','State','Identify'],
          sub_topic=tid,sub_topic_heading=t['title'])
        if anchor in {'3.3-03','5.3-02','7.4-03'}:
            obj['objective_type']='economics_quantitative_family'
        registry.append(obj)
        children=[]
        for j,label in enumerate(MEMBERS.get(anchor,[]),1):
            child=copy.deepcopy(obj);cid=f'OBJ-6145-{tid}.{n}-{j:02d}'
            # A member row anchors its precise meaning and consequence; the parent
            # practises the full comparison/list/integrated outcome.
            child.update(objective_id=cid,parent_id=oid,learner_objective=label[0].upper()+label[1:],
                         objective_type='economics_member',depth_tier=1,
                         syllabus_text=o['verbatim'],syllabus_guidance='Member focus: '+label+'. '+('Planner-specified realisation of the open syllabus outcome.' if anchor in OPEN_LISTS or anchor=='3.1-02' else 'Named member of this printed syllabus outcome.'),
                         command_words=['Define','Identify','Explain'])
            if anchor in {'3.3-03','5.3-02','7.4-03'}:
                child.update(objective_type='economics_calculation',depth_tier=3,command_words=['Calculate','Explain'])
            registry.append(child);children.append(cid)
            for k,member in enumerate(OPEN_LISTS.get(anchor+':'+label,[]),1):
                grand=copy.deepcopy(child);gid=f'OBJ-6145-{tid}.{n}.{j}-{k:02d}'
                grand.update(objective_id=gid,parent_id=cid,learner_objective=member[0].upper()+member[1:],syllabus_guidance='Member focus: '+member+'. Planner realisation of the open money outcome; not a verbatim printed member list.')
                registry.append(grand);children.append(gid)
        crosswalk.append({'syllabus_anchor':oid,'assessable_parent':oid,'member_objective_ids':children,
                          'source':o,'provenance':'judgement: decomposition; original wording remains syllabus evidence',
                          'coverage_rule':'Parent retains integrated skill; children ensure each member is taught. Do not write the same definition repeatedly at both levels.'})
dump(CUR/'objective_registry.json',{'registry_id':'REG-NAM-6145-2026','qualification_profile_id':qpid,'subject_profile_id':spid,
 'authority':facts['source_document'],'granularity_note':'96 original specific-outcome anchors plus explicit member objectives. Each parent practises the integrated demand, each child a precise member. All 28 topic containers are non-assessable.',
 'objectives':registry})
dump(CUR/'objective-crosswalk.json',{'crosswalk':crosswalk,'open_list_realisations':OPEN_LISTS})
dump(CUR/'unit_titles.json',{th['theme_id']:th['title'].title() for th in facts['content_outline']})
dump(CUR/'syllabus-exclusions.json',{t['topic_id']:[] for t in subjects})

qp={'profile_id':qpid,'version':'0.1.0-draft','status':'draft','board':'Namibia NIED / DNEA','qualification':'Namibia NSSCO',
 'subject':'Economics','syllabus_code':'6145','examination_years':[2026],'syllabus_version':'NIED 2018; first examination 2020; user-confirmed for 2026 learners',
 'selected_level':'Ordinary Level','route':{'route_id':'NSSCO-6145','name':'Full NSSCO','included_paper_ids':['P1','P2'],'excluded_paper_ids':[]},
 'language':'English','learner_entry_assumptions':['No previous Economics study assumed.'],
 'papers':[{'paper_id':'P'+p['paper'],'name':p['name'],'duration_minutes':p['duration_minutes'],'marks':p['marks'],
            'qualification_weight_percent':p['weight_percent'],'question_basis':'All topics; structure and choices transcribed in curriculum/syllabus-facts.json.',
            'assessment_objective_weights':p['ao_split']} for p in facts['papers']],
 'assessment_objectives':[{'code':a['code'],'name':a['name'],'description':'; '.join(a['can_do']),
                          'qualification_weight_percent':facts['derived_qualification_ao_weights']['values_percent'][a['code']]} for a in facts['assessment_objectives']],
 'command_words':[{'word':c['word'].title(),'meaning':c['meaning']} for c in facts['command_words']],
 'scope':{'included_topic_ids':[t['topic_id'] for t in subjects],'excluded_topic_ids':[],'optional_routes':[]},
 'source_authority':{'curricular':[facts['source_document']],'assessment':['assessment-evidence/sources.json; ten QPs and five report sections'],
                     'conceptual':['6145 syllabus content and glossary; original examples and checked economic reasoning'],
                     'conflict_rule':'Syllabus first; quarantine report anomalies. Overall AO weights are calculated from the stated equal paper weights, not a separate printed table.'},
 'example_selection_rules':['Invented Namibian businesses; N$; British spelling.','Never reproduce official cases, prompts or marking wording.'],
 'notes':['All three qualification AO weights are calculated, with source references in syllabus-facts.json.','No multiple-choice component is described in this syllabus.','Standalone mark schemes missing; report-guidance gaps and 14 source anomalies retained.']}
(WS/'qualification-profile.yaml').write_text(yaml.safe_dump(qp,sort_keys=False,allow_unicode=True))

structures={'DEF':['meaning|definition','distinguishing feature|qualifier'], 'FEATURE':['feature|characteristic'],
 'WHY':['reason','because|link'],'DIST':['difference|whereas','test|distinguishing'],
 'APP':['context','reasoning|because','result|therefore'], 'MECH':['initial change','mechanism','effect'],
 'CHAIN':['initial change','mechanism','effect','actor|household|firm|government|economy'],
 'BEN':['benefit','because','actor|household|firm|government|economy'],
 'LIM':['limitation','because','actor|household|firm|government|economy'],
 'EVAL':['argument for','argument against','judgement','condition'],
 'CALC':['formula','working','answer','unit|coefficient'],
 'INTERP':['relationship','evidence','explanation'], 'PROC':['diagram','labels','original','change'],
 'MISCON':['confusion','boundary','test'],
 'short_answer':['parts','allocation','precision'],
 'data_response':['context','parts','allocation','mechanism','judgement'],
 'case_analysis':['context','parts','allocation','mechanism','judgement'],
 'essay_plan':['argument for','argument against','judgement','condition']}
sp={'profile_id':spid,'version':'0.1.0-draft','status':'draft','subject_name':'NSSCO Economics 6145','language_variant':'British English',
 'purpose':'Standalone teaching notes with original retrieval and applied practice for the confirmed 6145 examination.',
 'foundational_concepts':['scarcity','opportunity cost','incentives','economic agents','conditional causal reasoning'],
 'objective_types':[{'type_id':'economics_'+t,'label':t.replace('_',' ').title(),'description':'6145 '+t.replace('_',' ')+' demand.',
                      'required_components':['precise meaning','relevant example or discrimination'], 'recommended_item_types':['flashcard']} for t in type_labels],
 'assessment_skill_model':[{'skill_id':a['code'],'label':a['name'],'definition':'; '.join(a['can_do']),
                            'authoring_requirements':['Follow the 6145 answer shapes and the slot labels.']} for a in facts['assessment_objectives']],
 'application_model':{'core_rule':'The supplied case facts must affect the explanation, not merely decorate a recalled answer.',
  'context_dimensions':['economic agent','sector','income group','time horizon','market condition'],
  'worked_application_policy':{'minimum_per_major_objective':1,'contrast_required_for_decisions':True,'coverage_dimensions':['initial change','mechanism','outcome']},
  'pseudo_application_patterns':['Adding a business name to a definition without using any case facts.']},
 'analysis_model':{'chain_template':['initial change','economic mechanism','consequence for the specified agent'],
                   'rules':['State the direction of change and relevant conditions.','Do not count repeated or mirrored points as new analysis.']},
 'evaluation_model':{'judgement_template':['relevant case for','relevant case against','supported judgement with condition'],
                     'decision_dimensions':['distribution','time horizon','capacity','implementation','opportunity cost'],
                     'rules':['Use two sides for whether/always decisions, not every descriptive Discuss task.','Conclusion must add a supported condition or priority, not repeat an earlier claim.']},
 'depth_model':{'allocation_factors':['syllabus depth','concept difficulty','measured exposure','named-member coverage'],
                'tiers':[{'tier':i,'label':label,'typical_use':label,'indicative_word_range':{'min':200,'max':470},'indicative_item_range':{'min':1,'max':5}} for i,label in enumerate(['precise member','concept/application','causal or quantitative reasoning','integrated judgement'],1)]},
 'quantitative_model':{'required_components':['formula','substitution','checked result','unit or coefficient'],
                       'interpretation_rules':['Elasticity is not a percentage.','Use price-index deflation for exact real-income calculations; label approximations.','Convert persons and millions consistently.']},
 'legal_and_jurisdiction_model':{'core_rule':'Use Namibia as the context; no unsupported current thresholds, statutory section numbers or universal legal-form claims.',
                               'high_risk_topics':['2.1','2.2','6.2','6.3']},
 'learning_item_model':{'item_types':['flashcard','short_answer','data_response','case_analysis','essay_plan'],
                        'flashcard_subtypes':[k for k in structures if k not in {'short_answer','data_response','case_analysis','essay_plan'}],
                        'rules':['One main retrieval target per flashcard.','Each package supplies its own facts and a worked answer for every part.','Marking guidance identifies concrete content and allocations; do not paste generic rubric text.']},
 'terminology_rules':['Social costs include private and external costs.','Capital-account legacy language must not turn investment flows into service exports.','Keep ownership sector distinct from the stage of production.'],
 'prohibited_patterns':['Unqualified causal universals.','Copied assessment wording.','Generic repeated answer templates.','Treating a source error as an economic law.'],
 'semantic_review_questions':['Can the learner reconstruct every answer from the notes?','Are mechanisms and diagrams consistent?','Is each judgement conditional?','Does the rubric credit the actual answer rather than generic keywords?'],
 'variant_register':[{'term':'unemployment','variants':['cyclical','structural','seasonal','frictional'],'consequence':'The cause determines the classification and the appropriate policy.'},
                     {'term':'elasticity','variants':['elastic','inelastic','unit elastic','perfectly inelastic'],'consequence':'Magnitude determines quantity/revenue responsiveness; coefficient has no percentage unit.'}],
 'answer_structures':structures}
# The runtime explicitly supports these extensions, although the shared subject
# schema predates them. They are reported, never patched out of the standard.
sp['conditioned_mechanisms']=[{'mechanism_id':'CM-6145-PRICE-REVENUE','name':'Price rise increases total revenue','asserted_when':[r'\bprice ris\w*\b',r'\btotal revenue\b',r'\bincreas\w*\b'],
 'required_conditions':[{'name':'inelastic demand for the relevant change','any_of':[r'\binelastic\b',r'\bPED.*(?:below|less than) 1\b']}],
 'rationale':'Revenue does not rise with price for all elasticities.'}]

sp['conditioned_mechanisms'] += [
 {'mechanism_id':'CM-6145-MINIMUM-WAGE','name':'A binding wage floor creates excess labour supply in the basic competitive model',
  'asserted_when':[r'\bminimum wage\b',r'\b(?:raises?|increases?|creates?|causes?)\b',r'\bunemployment\b'],
  'required_conditions':[{'name':'the floor is above the equilibrium wage in the competitive model','any_of':[r'\babove (?:the )?(?:market|equilibrium) wage\b',r'\bbinding wage floor\b']}],
  'rationale':'A floor below equilibrium is not binding; do not generalise beyond the stated model.'},
 {'mechanism_id':'CM-6145-DEPRECIATION','name':'Depreciation improves the current account',
  'asserted_when':[r'\bdepreciat\w*\b',r'\bcurrent account\b',r'\bimprov\w*\b'],
  'required_conditions':[{'name':'trade quantities and supply can respond sufficiently','any_of':[r'\bsupply can respond\b',r'\bsufficient(?:ly)? respons\w*\b',r'\belastic enough\b']}],
  'rationale':'The import bill and production constraints can offset price competitiveness.'},
 {'mechanism_id':'CM-6145-GROWTH','name':'Growth improves living standards',
  'asserted_when':[r'\beconomic growth\b',r'\b(?:raises?|improves?) living standards\b'],
  'required_conditions':[{'name':'distribution and external costs are considered','any_of':[r'\bdistribut\w*\b',r'\bshared\b',r'\bexternal costs?\b']}],
  'rationale':'Higher output alone does not establish better living standards for every person.'}
]

sp['depiction_rule']='Use original generated economic diagrams or complete coordinate tables; label axes, curves, equilibrium and changes. Never claim a generic business break-even renderer validates supply/demand geometry.'
sp['slot_plan']={
 'note':'6145-specific design from the approved corpus; no MCQ paper. AO marks are planning estimates, not official per-part allocations. Parent outcomes integrate skills; member rows prevent omissions.',
 'subtypes_by_objective_type':{
  'economics_member':['DEF'], 'economics_calculation':['CALC','INTERP'], 'economics_quantitative_family':['INTERP'], 'economics_definition':['DEF','FEATURE'], 'economics_concept':['DEF','WHY'],
  'economics_classification':['FEATURE','DIST'], 'economics_comparison':['DEF','DIST'],
  'economics_mechanism':['DEF','MECH'], 'economics_cause_effect':['DEF','CHAIN'],
  'economics_diagram':['DEF','PROC','INTERP'], 'economics_quantitative':['DEF','CALC','INTERP'],
  'economics_policy_evaluation':['BEN','LIM','EVAL']},
 'subtypes_by_tier':{1:[],2:['APP'],3:['APP'],4:[]},
 'command_words_by_subtype':{'DEF':['Define'],'FEATURE':['Identify'],'WHY':['Explain'],'DIST':['Explain'],
  'APP':['Explain'],'MECH':['Explain'],'CHAIN':['Explain'],'BEN':['Explain'],'LIM':['Explain'],
  'EVAL':['Evaluate'],'CALC':['Calculate'],'INTERP':['Explain'],'PROC':['Use'],'MISCON':['Explain']},
 'tariff_overrides':{'DEF:Define':2,'FEATURE:Identify':1,'WHY:Explain':2,'DIST:Explain':2,
  'APP:Explain':2,'MECH:Explain':2,'CHAIN:Explain':2,'BEN:Explain':2,'LIM:Explain':2,
  'EVAL:Evaluate':8,'CALC:Calculate':1,'INTERP:Explain':4,'PROC:Use':4,'MISCON:Explain':2},
 'high_tariff':{'threshold':100,'adds':[]}, 'top_up':[], 'misconception_slots':'one_per_entry',
 'performance_tasks':[
  {'item_type':'data_response','brief':'Original 20-mark Paper 1 Section B-style case: (a) Describe 6, developing three relevant features; (b) Examine 7, tracing effects in this original case; (c) Suggest 7, selecting and justifying an appropriate course of action. Keep all parts within this topic. Include source data, complete model answers and exact content-specific mark guidance. AO split is an estimate of the task demands, not a quotation of an official grid.', 'ao_split':{'B':6,'C':14}},
  {'item_type':'short_answer','brief':'Original 16-mark knowledge mini-test: eight separate two-mark short responses on this topic. Vary definitions, distinctions and precise reasons; avoid repeating a member definition. Each part uses an observed 2-mark command. Give answers and content-specific mark allocation. This is a short practice set, not a whole paper.', 'ao_split':{'A':16}},
  {'item_type':'case_analysis','brief':'Original 20-mark 6145 Paper 2 structured case: (a) Define 2; (b) Explain 4; (c) Explain 7 using a diagram or a developed mechanism as appropriate; (d) Discuss 7 evaluating a genuine decision in this topic. Supply all data, an original invented Namibian case, full answers and task-specific marking. Where a narrow topic cannot support the decision without scope creep, report it before authoring.', 'ao_split':{'A':6,'B':7,'C':7}},
  {'item_type':'essay_plan','brief':'An original 9-mark Evaluate decision plan: a relevant developed case for, a developed case against and a supported condition-based judgement. Use only this topic’s concepts and fresh context. Provide the complete plan and a content-specific rubric; this is an extended-response drill, not a full Paper 2 essay.', 'ao_split':{'C':9}}]}
(WS/'subject-profile.yaml').write_text(yaml.safe_dump(sp,sort_keys=False,allow_unicode=True))

ao_codes={'DEF':['A'],'FEATURE':['A'],'WHY':['A'],'DIST':['A','B'],'APP':['B'],'MECH':['B'],'CHAIN':['B'],
          'BEN':['B'],'LIM':['B'],'EVAL':['C'],'CALC':['B'],'INTERP':['B'],'PROC':['B'],'MISCON':['B']}
blooms={'DEF':'Remember','FEATURE':'Remember','WHY':'Understand','DIST':'Understand','APP':'Apply','MECH':'Understand','CHAIN':'Analyse','BEN':'Understand','LIM':'Analyse','EVAL':'Evaluate','CALC':'Apply','INTERP':'Analyse','PROC':'Apply','MISCON':'Analyse'}
fwcmd=[]
for c in commands['commands']:
    d=copy.deepcopy(c);d.update(word=c['word'].title(),observed_count=c['count'],modal_tariff=c['modal_tariffs'][0] if c['modal_tariffs'] else None,
      observed_tariffs=c['tariffs'],exact_mark_tariff=c['modal_tariffs'][0] if c['modal_tariffs'] else None,
      used_at_level=bool(c['count']),primary_assessment_objectives=['A','B','C'])
    fwcmd.append(d)
fw={'framework_id':'FRAMEWORK-NAM-6145-2026','syllabus_facts_ref':'curriculum/syllabus-facts.json',
    'assessment_objectives':facts['assessment_objectives'],'papers':facts['papers'],
    'command_words':fwcmd,'command_words_listed_but_never_used':[],
    'ao_mark_budget':{'stated_qualification_weight_percent':facts['derived_qualification_ao_weights']['values_percent'],
       'provenance_note':'Compatibility field name in the shared generator. These targets are CALCULATED from the stated paper weights and AO splits, not separately stated qualification percentages.'},
    'item_mix_target':{'target_share_percent':facts['derived_qualification_ao_weights']['values_percent']},
    'flashcard_subtype_ao_map':[{'subtype':k,'assessment_objectives':v,'blooms_level':blooms[k]} for k,v in ao_codes.items()],
    'blooms_taxonomy':{'levels':[{'level':x} for x in ['Remember','Understand','Apply','Analyse','Evaluate','Create']],
                       'by_performance_task':{'short_answer':'Understand','data_response':'Evaluate','case_analysis':'Analyse','essay_plan':'Evaluate'}},
    'source_note':'Primary-opening tariffs only. Embedded Calculate at 2 marks is retained in command-word-analysis.json; the slot plan deliberately uses primary Calculate 1 here.'}
dump(CUR/'assessment-framework.json',fw)

mis=load(CUR/'misconceptions.json')
mis['entries']=[{**m,'entry_id':m['misconception_id'],'objective_id':m['objective_ids'][0],
                'a':m['title'],'b':m['correct_understanding'],'test':m['discriminating_test'],'n':len(m['evidence_ids'])} for m in mis['misconceptions']]
dump(CUR/'misconceptions.json',mis)

# Member exposure remains zero until separately read at that grain: never smear
# every parent question onto every list member. The status explains this boundary.
exp=load(CUR/'exam-exposure.json');old={o['objective_id']:o for o in exp['objectives']}
new=[]
for o in registry:
    if not o['parent_id']:continue
    if o['objective_id'] in old:
        row=copy.deepcopy(old[o['objective_id']])
    else:
        row={'objective_id':o['objective_id'],'topic_id':o['topic_id'],'syllabus_text':o['syllabus_text'],
             'times_examined':0,'marks_examined':0,'marks_linked_including_secondary':0,'series':[],'series_spread':0,
             'max_tariff':0,'command_words':{},'tariffs':{},'evidence_ids':[],'exposure_class':'unseen',
             'grain_note':'No separate member-level mapping asserted; the parent evidence remains available. Unseen at this finer grain is not a claim that the member never appeared in a paper.'}
    matched=[r for r in evidence['records'] if o['objective_id'] in r['objective_ids']]
    row['evidence']={'question_parts_naming_it':len(matched),'distinct_series':len({r['exam_series'] for r in matched}),'max_mark_tariff':max((r['mark_tariff'] for r in matched),default=0),'command_words_observed':dict(collections.Counter(r['command_word'] for r in matched))}
    new.append(row)
exp['objectives']=new;exp['objective_registry_status']='Decomposed registry with explicit crosswalk; original semantic mappings preserved, no fabricated member exposure.'
dump(CUR/'exam-exposure.json',exp)
dump(CUR/'dependency_graph.json',{'edges':[],'rule':'All topics follow syllabus order; required concepts must also be taught locally before an item uses them.'})
print('Registry:',len(registry),'nodes,',len(registry)-28,'assessable; source anchors retained:',len(original))
