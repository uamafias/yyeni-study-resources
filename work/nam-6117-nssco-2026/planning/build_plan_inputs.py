"""Build Chemistry planning inputs from the approved syllabus and evidence.

Observed subtopic exposure is retained; no measured leaf-level frequency is
invented. Profiles conform to their schemas; generator extensions live in a
separate planning/slot-plan.json and are merged in memory by build_resource_plan.
"""
import json
import re
from collections import Counter
from pathlib import Path
import yaml

WORK=Path(__file__).resolve().parents[1]
ROOT=WORK.parents[1]
CUR=WORK/'curriculum'

def write(path,data):
    path.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')

# The source bullet is kept in syllabus-outcomes.json as the container; these
# are separately assessable members, with sibling links in the registry.
SPLITS={
 '1.5-05':['filtration','crystallisation and re-crystallisation','paper chromatography','simple distillation','fractional distillation'],
 '2.1.2-03':['proton','neutron','electron'],
 '2.4.3-05':['H2','Cl2','H2O','CH4','NH3','HCl'],
 '2.4.3-06':['N2','C2H4','CH3OH','CO2'],
 '2.4.3-08':['water: V-shaped','methane: tetrahedral','ammonia: pyramidal','carbon dioxide: linear'],
 '3.1-01':['wood','metals','glasses','ceramics','concrete','plastics','fibres'],
 '3.1-03':['metals','concrete','glass','cellulose in wood','synthetic polymers'],
 '4.2-06':['percentage composition','percentage yield','percentage purity'],
 '5.1-01':['electrode','electrolyte','anode','cathode'],
 '5.1-05':['molten lead(II) bromide','dilute sulfuric acid','concentrated hydrochloric acid','concentrated aqueous sodium chloride'],
 '5.1-10':['aluminium from aluminium oxide in molten cryolite','chlorine and sodium hydroxide from concentrated sodium chloride'],
 '6.2-01':['exothermic reaction','endothermic reaction'],
 '6.4-05':['concentration','pressure','particle size and surface area','catalyst','temperature','light'],
 '6.5-04':['concentration changes','temperature changes','pressure changes'],
 '6.6-01':['oxidation: oxygen gain and electron loss','reduction: oxygen loss and electron gain'],
 '7.1-01':['acid as proton donor','base as proton acceptor'],
 '7.1-07':['acids with metals','acids with bases','acids with carbonates'],
 '7.2-01':['basic oxides','acidic oxides','amphoteric oxides'],
 '7.3-07':['acid and metal oxide equations','acid and Group I/II hydroxide equations','acid and metal carbonate equations'],
 '7.4-02':['sodium, potassium and ammonium salts','nitrates','lead salts','hydroxides','carbonates','chlorides','sulfates'],
 '8.1-01':['cation: ammonium','cation: aluminium','cation: zinc','cation: calcium','cation: copper(II)','cation: iron(II)','cation: iron(III)',
            'flame: lithium','flame: sodium','flame: potassium','flame: calcium','flame: barium',
            'anion: carbonate','anion: chloride','anion: bromide','anion: iodide','anion: nitrate','anion: sulfate'],
 '8.2-01':['ammonia','carbon dioxide','chlorine','hydrogen','oxygen'],
 '9.3-05':['bauxite and aluminium','haematite and iron'],
 '9.3-06':['chalcopyrite and copper','galena and lead','uranium oxide and uranium'],
 '9.3-11':['aluminium by electrolysis','copper by reduction or roasting'],
 '10.2.1-04':['refinery gas','gasoline','naphtha','kerosene','diesel oil','fuel oil','bitumen'],
 '10.8.1-05':['nylon polyamide','Terylene polyester'],
 '11.3-01':['oxygen','nitrogen','carbon dioxide'],
 '11.3-02':['oxygen uses','carbon dioxide uses','nitrogen uses'],
}

TYPES={
 'chem_fact':(['DEF'],'Recognise or recall a chemical fact'),
 'chem_description':(['FEATURE','MECH'],'Describe familiar chemical structure or properties'),
 'chem_explanation':(['MECH','APP'],'Explain a familiar relationship and apply it to a fresh case'),
 'chem_process':(['PROC','APP'],'Describe a chemical sequence and select conditions or steps'),
 'chem_comparison':(['DIST','APP'],'Distinguish related chemical ideas in a given case'),
 'chem_applied':(['APP','INTERP'],'Use supplied information to infer a chemical answer'),
 'chem_quantitative':(['CALC','CALC'],'Solve two numerical variants with method and units'),
 'chem_stoichiometry':(['CALC','CALC','CALC','CALC'],'Solve direct, inverse, conversion and linked stoichiometric variants'),
 'chem_diagram':(['APP','INTERP'],'Construct and interpret a chemistry representation'),
 'chem_practical':(['PROC','INTERP'],'Carry out or interpret a practical technique on paper'),
 'chem_qualitative':(['PROC','INTERP'],'Describe and interpret reagent/observation sequences'),
 'chem_gas_flame':(['FEATURE','PROC'],'Know a gas/flame test and apply a safe observation sequence'),
 'chem_evaluation':(['LIM','APP'],'Evaluate a chemical or environmental consequence'),
 'chem_container':([], 'Non-assessable topic container'),
}

STRUCTURES={
 'DEF':['meaning|definition|identity|formula|fact'],
 'FEATURE':['property|feature|observation|colour|test'],
 'MECH':['cause|because|reason','effect|result|therefore'],
 'APP':['given|data|case|condition|label','reason|because|therefore|structure|bond|apparatus|axis|electron'],
 'PROC':['method|step|sequence','observation|result|conclusion'],
 'DIST':['difference|whereas|contrast','reason|because|structure'],
 'INTERP':['data|graph|diagram|table|observation','conclusion|inference|shows|means'],
 'CALC':['equation|formula','substitution|working','answer|result','unit|units'],
 'LIM':['limitation|error|problem','effect|consequence','improvement|reason'],
 'MISCON':['error|mistake|confusion','correct|instead','test|distinguish|because'],
 'multiple_choice_set':['key|correct option','distractor|wrong option','reason|because'],
 'short_answer':['marks|mark','point|reason|working'],
 'practical_task':['method|apparatus','data|table|graph|observation','conclusion|improvement'],
 'calculation':['equation|formula','working|substitution','answer|result','unit|units'],
}
CW={'DEF':['State','Define','Name','Identify'],'FEATURE':['State','Describe'],'MECH':['Explain','Describe'],
    'APP':['Suggest','Explain','Deduce'],'PROC':['Describe'],'DIST':['Distinguish','Compare','Explain'],
    'INTERP':['State','Deduce','Explain'],'CALC':['Calculate'],
    'LIM':['Suggest','Explain'],'MISCON':['Explain']}
AO={'DEF':['A'],'FEATURE':['A'],'MECH':['A'],'PROC':['A'],'DIST':['A'],
    'APP':['B'],'INTERP':['B'],'CALC':['B'],'LIM':['B'],'MISCON':['B']}
BLOOM={'DEF':'Remember','FEATURE':'Remember','MECH':'Understand','PROC':'Apply','DIST':'Understand',
       'APP':'Apply','INTERP':'Analyse','CALC':'Apply','LIM':'Evaluate','MISCON':'Understand'}

def type_for(row,member):
    text=row['syllabus_text'].lower(); sub=row['syllabus_subtopic'];key=row['outcome_id'].removeprefix('SYL-6117-')
    if key in ['6.4-05','2.3.3-05','10.3-02','10.4-02','11.4-03','11.4-09','7.1-07']:
        return 'chem_explanation'  # familiar mechanism plus a fresh reaction/condition
    if sub.startswith('12.') or sub.startswith(('1.2','1.4')):return 'chem_practical'
    if sub=='8.1':return 'chem_gas_flame' if member and member.startswith('flame:') else 'chem_qualitative'
    if sub=='8.2':return 'chem_gas_flame'
    if sub=='4.2':return 'chem_stoichiometry'
    if sub=='1.1' or text.startswith('calculate') or key in ['1.3-02','1.3-03','1.3-06','1.5-09']:return 'chem_quantitative'
    if 'diagram' in text or text.startswith(('draw','sketch')) or key in ['2.4.3-05','2.4.3-06','2.4.3-07','10.8.1-03','10.8.1-05','10.8.2-03','10.8.2-06']:return 'chem_diagram'
    if sub=='1.5' and key in ['1.5-01','1.5-05','1.5-07','1.5-08']:return 'chem_practical'
    if text.startswith(('distinguish','compare','differentiate')):return 'chem_comparison'
    if text.startswith(('interpret','deduce','predict','suggest','evaluate','analyse')):return 'chem_applied'
    if text.startswith(('explain','relate','account')):return 'chem_explanation'
    if text.startswith(('define','state','recall','name','identify')):return 'chem_fact'
    if any(x in text for x in ['advantages and disadvantages','dangers','implications','global concern']):return 'chem_evaluation'
    if any(x in text for x in ['manufacture','preparation','extraction','formation of','purification','conversion','softening','hydrolysis']):return 'chem_process'
    return 'chem_description'

def main():
    facts=json.loads((CUR/'syllabus-facts.json').read_text())
    raw=json.loads((CUR/'syllabus-outcomes.json').read_text())
    audit=json.loads((WORK/'assessment-evidence/command-part-audit.json').read_text())
    papers=[];aos=[]
    for p in facts['papers']:
        num=p['paper'];marks=p['marks']['value']
        split={a['code']:100*a['marks_by_paper']['value'][num]/marks for a in facts['assessment_objectives']}
        papers.append({'paper_id':'P'+num,'name':p['name']['value'],'marks':marks,
                       'duration_minutes':p['duration_minutes']['value'],'qualification_weight_percent':p['qualification_weight_percent']['value'],
                       'question_basis':p['description']['value'],'assessment_objective_weights':split})
    for a in facts['assessment_objectives']:
        aos.append({'code':a['code'],'name':a['name']['value'],'description':' '.join(c['verbatim_entry'] for c in a['criteria']),
                    'qualification_weight_percent':a['qualification_weight_percent']['value']})
    qid='namibia-6117-nssco-2026';sid='yyeni-chemistry-6117-nssco-2026'
    qual={'profile_id':qid,'version':'0.1.0','status':'draft','board':'Namibia DNEA / NIED','qualification':'NSSCO',
          'subject':'Chemistry','syllabus_code':'6117','examination_years':[2026],'syllabus_version':'2018; first examination 2020',
          'selected_level':'Ordinary Level, Grades 10–11','route':{'route_id':'all-three-papers','name':'Papers 1, 2 and 3','included_paper_ids':['P1','P2','P3']},
          'language':'English','papers':papers,'assessment_objectives':aos,
          'command_words':[{'word':x['word'],'meaning':x['verbatim_entry']} for x in facts['command_words']],
          'scope':{'included_topic_ids':[str(t['topic']) for t in facts['content_outline']]+['12'],'excluded_topic_ids':[],'optional_routes':[]},
          'source_authority':{'curricular':[facts['syllabus_file']],'assessment':['Local 2020–2025 papers and six examiner reports'],
                              'conceptual':[facts['syllabus_file']],'conflict_rule':'Syllabus governs scope. Independently verify report answers, especially the recorded 2025 mole calculation.'},
          'learner_entry_assumptions':['Junior Secondary science and mathematics'],
          'notes':['Topic 12 is a teaching organisation for Annexe A skills, not an additional board content topic.','AO weights are approximate; recall must not exceed 25%.','Syllabus Paper 1 duration: 45 minutes; 2025 cover states one hour.','2022/2023 papers are proof versions.']}
    (WORK/'qualification-profile.yaml').write_text(yaml.safe_dump(qual,sort_keys=False,allow_unicode=True))
    profile={'profile_id':sid,'version':'0.1.0','status':'draft','subject_name':'NSSCO Chemistry 6117','language_variant':'British English',
     'purpose':'Full syllabus teaching notes and self-contained retrieval, calculation, visual and practical activities; original examples and supported marking structures.',
     'foundational_concepts':['particles and bonding','amount of substance','energy and reaction rate','chemical evidence','safe measurement and fair tests'],
     'objective_types':[{'type_id':k,'label':k.replace('chem_','').replace('_',' '),'description':v[1],
                         'required_components':['syllabus concept','original example or diagnostic','supported answer structure'],
                         'recommended_item_types':v[0]} for k,v in TYPES.items()],
     'assessment_skill_model':[{'skill_id':a['code'],'label':a['name'],'definition':a['description'],'authoring_requirements':['Use the slot AO and Bloom label; do not infer AO from the command alone.']} for a in aos],
     'application_model':{'core_rule':'Use fresh substances, values or experimental contexts to apply the same syllabus idea.',
       'context_dimensions':['substance','apparatus','data','conditions'],'worked_application_policy':{'minimum_per_major_objective':1,'contrast_required_for_decisions':True,'coverage_dimensions':['context','reason','consequence']},
       'pseudo_application_patterns':['Adding a name to an unchanged definition','Reusing an official question with substituted numbers']},
     'analysis_model':{'chain_template':['evidence or condition','chemical reason','supported conclusion'],'rules':['Distinguish observation from inference.','Use particle, energy or mole reasoning where the task requires it.']},
     'evaluation_model':{'judgement_template':['criterion','evidence','limitation and improvement'],'decision_dimensions':['safety','fairness','precision','validity'],'rules':['Do not claim repeats remove systematic error.','Tie each improvement to a named source of error.']},
     'depth_model':{'allocation_factors':['syllabus demand','calculation stages','required representations','observed answer shape'],
       'tiers':[{'tier':i,'label':label,'typical_use':use,'indicative_word_range':{'min':lo,'max':hi},'indicative_item_range':{'min':1,'max':3}} for i,label,use,lo,hi in [(1,'Anchor','Fact or definition',150,230),(2,'Explanation','Chemical reason or sequence',230,330),(3,'Application','Data, calculation or representation',270,390),(4,'Container','Organising heading',0,0)]]},
     'quantitative_model':{'required_components':['equation','unit conversion','substitution','unrounded working','rounded answer and unit'],
                          'interpretation_rules':['Recompute every result independently.','Use 24 dm³/mol at room conditions when specified.','Distinguish mass concentration from amount concentration.']},
     'learning_item_model':{'item_types':['flashcard','multiple_choice_set','short_answer','calculation','practical_task'],'flashcard_subtypes':list(CW),
                           'rules':['Every slot carries AO, Bloom, command, tariff and an answer rubric.','No invented allocation for commentary-only evidence.','Official question and report wording remains internal.']},
     'terminology_rules':['Use ion charges and oxidation states consistently.','Distinguish a coloured precipitate from a coloured solution.','State aqueous/molten and electrode conditions when predicting electrolysis products.','Pressure changes equilibrium yield only where gas stoichiometry permits; rate and yield are distinct.','Do not conflate concentration with strength.','Keep every item self-contained.'],
     'prohibited_patterns':['Content beyond explicit scope limits','Copied assessment wording','Unverified report arithmetic','Invented credit allocations for the five commentary-only parts'],
     'semantic_review_questions':['Can a learner answer from the notes alone?','Are every listed syllabus member and required skill covered?','Do answers distinguish observation, inference and explanation?','Are apparatus and graph visuals scientifically possible?'],
     'answer_structures':STRUCTURES,
     'variant_register':[{'term':'electrolysis','variants':['aqueous','molten','inert electrode','copper electrode'],'consequence':'Electrode products and charge carriers depend on the stated conditions.'},
                         {'term':'acid','variants':['strong','weak','concentrated','dilute'],'consequence':'Strength is degree of ionisation; concentration is amount per volume.'}]}
    (WORK/'subject-profile.yaml').write_text(yaml.safe_dump(profile,sort_keys=False,allow_unicode=True))
    counts=Counter();grouped={}
    for g in audit['groups']:
        counts[g['word']]+=g['parts'];grouped.setdefault(g['word'],Counter()).update({int(k):v for k,v in g['tariff_counts'].items()})
    glossary_forms={s.strip().lower() for g in facts['command_words'] for s in g['word'].split('/')}
    words=[]
    for word,c in counts.items():
        allowed=word not in ['use','which','what']
        words.append({'word':word.title(),'observed_count':c,'modal_tariff':min(k for k,v in grouped[word].items() if v==max(grouped[word].values())),
          'exact_mark_tariff':min(k for k,v in grouped[word].items() if v==max(grouped[word].values())) if allowed else None,
          'observed_tariffs':sorted(grouped[word]),'used_at_level':allowed,'use_in_prompts':allowed,'in_syllabus_glossary':word in glossary_forms,
          'primary_assessment_objectives':['A','B','C'],'provenance':'corpus: command-part-audit.json; prompt eligibility is planning judgement'})
    fw={'framework_id':'FRAMEWORK-NAM-6117-NSSCO-2026','authority':facts['syllabus_file'],'syllabus_facts_ref':'curriculum/syllabus-facts.json',
        'assessment_objectives':aos,'papers':[{'paper':p['paper_id'][1:],'name':p['name'],'marks':p['marks'],'duration_minutes':p['duration_minutes'],
              'weight_percent':p['qualification_weight_percent'],'ao_split':p['assessment_objective_weights']} for p in papers],
        'command_words':words,'command_words_listed_but_never_used':audit['glossary_comparison']['unused_glossary_entries'],
        'command_words_used_but_not_listed':audit['glossary_comparison']['observed_forms_outside_glossary'],
        'ao_mark_budget':{'per_paper_marks':{'P'+p['paper']:{a['code']:a['marks_by_paper']['value'][p['paper']] for a in facts['assessment_objectives']} for p in facts['papers']},
              'stated_qualification_weight_percent':{'A':50,'B':30,'C':20},'recall_limit_percent':25,
              'provenance':'syllabus printed pp.38–40 / PDF pp.41–43; weights approximate'},
        'flashcard_subtype_ao_map':[{'subtype':s,'assessment_objectives':list(set(AO[s]+(['A'] if s=='APP' else [])+(['C'] if s in ['PROC','INTERP','FEATURE','MISCON','LIM'] else []))),
          'tests':STRUCTURES[s],'blooms_level':BLOOM[s]} for s in CW],
        'blooms_taxonomy':{'levels':[{'level':x} for x in ['Remember','Understand','Apply','Analyse','Evaluate','Create']],
             'by_performance_task':{'multiple_choice_set':'Apply','short_answer':'Apply','calculation':'Apply','practical_task':'Analyse'}},
        'item_mix_target':{'target_share_percent':{'A':50,'B':30,'C':20}},
        'provenance_rule':'Syllabus requirements, measured corpus frequencies and planning judgements remain distinct.'}
    write(CUR/'assessment-framework.json',fw)
    objectives=[];source_map=[]
    for t in facts['content_outline']+[{'topic':12,'name':'Practical skills and investigation planning'}]:
        tid=str(t['topic']);objectives.append({'objective_id':'OBJ-6117-'+tid,'parent_id':None,'topic_id':tid,
          'syllabus_text':tid+' '+t['name'],'learner_objective':t['name'],'level':'NSSCO','route_status':'core','mandatory':True,
          'objective_type':'chem_container','assessment_objectives':['C'] if tid=='12' else ['A','B','C'],'command_words':[],
          'prerequisite_ids':[],'related_ids':[],'depth_tier':4,'source_coverage':{'rating':0,'action':'generate_gap','rationale':'Author original teaching material from the syllabus and mined evidence.'},'status':'planned','papers':['3'] if tid=='12' else ['1','2','3']})
    # Fifteen individually named Annex A skills; two subskills split the first
    # requirement. These are additional skill practice, not duplicate content.
    practicals=[('12.1','Read scales accurately and record appropriate precision.','C3'),('12.1','Interpolate between scale divisions.','C3'),
      ('12.1','Take repeated measurements where appropriate.','C3'),('12.2','Describe and explain experimental arrangements and techniques.','C1'),
      ('12.2','Complete tables and process numerical data.','C3'),('12.2','Draw, complete and label apparatus diagrams.','C1'),
      ('12.3','Justify a conclusion by reference to the data.','C4'),('12.3','Interpret and evaluate observations and experimental data.','C4'),
      ('12.3','Plot graphs and interpret graphical information.','C3'),('12.4','Identify sources of error and suggest procedural improvements.','C5'),
      ('12.5','Plan an investigation with predictions, suitable apparatus and techniques.','C2'),('12.3','Determine a gradient, intercept or intersection from a graph.','C4'),
      ('12.2','Select apparatus with reasons for a practical procedure.','C1'),('12.4','Explain precautions and critically suggest improvements.','C5'),
      ('12.6','Describe gas and ion tests and draw conclusions from results.','C4')]
    records=list(raw['outcomes'])
    pc=Counter()
    for sub,text,criterion in practicals:
        pc[sub]+=1;records.append({'outcome_id':f'SYL-6117-{sub}-{pc[sub]:02d}','syllabus_subtopic':sub,'subtopic_heading':'Annexe A practical requirements',
          'syllabus_text':text,'source_pdf_page':47,'source_printed_page':44,'source_lines':[],'criterion':criterion})
    for r in records:
        key=r['outcome_id'].removeprefix('SYL-6117-');sub=r['syllabus_subtopic'];tid=sub.split('.')[0]
        members=SPLITS.get(key,[None]);ids=[]
        for index,member in enumerate(members,1):
            oid='OBJ-6117-'+key+(f'-{index:02d}' if member else '')
            kind=type_for(r,member);label=r['syllabus_text'] if member is None else r['syllabus_text'].split(':')[0]+' — focus: '+member
            wet=kind=='chem_qualitative';practical=kind in ['chem_practical','chem_qualitative'];papers=['3'] if wet or tid=='12' else ['1','2','3']
            aos_=['C'] if practical else ['A','C'] if kind=='chem_gas_flame' else ['A','B','C']
            opening=re.match(r'^([A-Za-z]+)(?:\s+and\s+([A-Za-z]+))?',r['syllabus_text'])
            verbs={'define','state','name','identify','describe','explain','compare','distinguish','differentiate','interpret','deduce','predict','suggest','calculate','construct','classify','outline','discuss','use','recall','draw','sketch','evaluate','analyse','relate','record','present','locate','handle','make','solve','add','take','complete','select','determine','plan'}
            commands=[v.title() for v in opening.groups() if v and v.lower() in verbs] if opening else []
            if kind=='chem_quantitative' and not commands:commands=['Calculate']
            obj={'objective_id':oid,'parent_id':'OBJ-6117-'+tid,'topic_id':tid,'syllabus_text':r['syllabus_text'],
              'learner_objective':label,'level':'NSSCO','route_status':'core','mandatory':True,'objective_type':kind,
              'assessment_objectives':aos_,'command_words':commands,'prerequisite_ids':[],'related_ids':[],
              'depth_tier':1 if kind=='chem_fact' else 3 if kind in ['chem_quantitative','chem_stoichiometry','chem_applied','chem_diagram','chem_practical','chem_qualitative'] else 2,
              'source_coverage':{'rating':0,'action':'generate_gap','rationale':'Original notes and tasks required; internal report answer rows are not learner-ready text.'},
              'status':'planned','sub_topic':sub,'sub_topic_heading':r['subtopic_heading'],'syllabus_page':r['source_pdf_page'],'papers':papers}
            objectives.append(obj);ids.append(oid)
            source_map.append({'objective_id':oid,'source_outcome_id':r['outcome_id'],'syllabus_subtopic':sub,
              'member':member,'pdf_page':r['source_pdf_page'],'printed_page':r['source_printed_page'],
              'source_lines':r['source_lines'],'criterion':r.get('criterion'),'source_basis':'syllabus bullet' if r['source_lines'] else 'judgement: Annex A skill paraphrase, PDF p.47'})
        if len(ids)>1:
            for obj in objectives:
                if obj['objective_id'] in ids:obj['related_ids']=[i for i in ids if i!=obj['objective_id']]
    write(CUR/'objective_registry.json',{'registry_id':'OBJREG-NAM-6117-NSSCO-2026','qualification_profile_id':qid,'subject_profile_id':sid,
        'authority':facts['syllabus_file'],'granularity_note':'Specific syllabus bullets; selected lists decomposed into separate members. Original bullet containers and source lines remain in syllabus-outcomes.json; source mapping retains every membership.',
        'papers_note':'All content can support experimental contexts. Wet cation/anion tests are Paper 3 only; flame and gas tests may occur on all papers. Topic 12 organises Annex A.',
        'objectives':objectives})
    write(CUR/'objective-source-map.json',{'mapping_basis':'Each registry leaf inherits a specific syllabus bullet or an explicitly labelled Annex A skill paraphrase.','objectives':source_map})
    exposure=json.loads((CUR/'exam-exposure.json').read_text())
    exposure['objectives']=[{'objective_id':o['objective_id'],'topic_id':o['topic_id'],'syllabus_text':o['syllabus_text'],
       'times_examined':0,'marks_examined':0,'series_spread':0,'command_words':{},'evidence':{},'exposure_class':'unmeasured',
       'status':'not_counted_at_individual_outcome_level','subtopic_reference':'syllabus:'+o['sub_topic'],
       'note':'Zero is a placeholder for no audited leaf count, not evidence of no examination. Subtopic and C-criterion counts above remain the measured data.'} for o in objectives if o['parent_id']]
    exposure['leaf_exposure_note']='Individual outcome counts are unmeasured. Do not spread subtopic frequency across every child. All syllabus outcomes receive full coverage.'
    write(CUR/'exam-exposure.json',exposure)
    scan=json.loads((CUR/'scope-scan.json').read_text())
    if 'entries' not in scan:
        scan['entries']=[{'construct':r['construct'],'pattern':r.get('pattern',''), 'source':str(r['source'])} for r in scan.get('rules',[])]
        assert all(r['pattern'] for r in scan['entries']), 'Build valid scope patterns first.'
        write(CUR/'scope-scan.json',scan)
    write(CUR/'syllabus-exclusions.json',{'all':[x['context_verbatim'] for x in facts['stated_limits']]})
    write(CUR/'unit_titles.json',{str(t['topic']):t['name'] for t in facts['content_outline']}|{'12':'Practical skills'})
    slot={'subtypes_by_objective_type':{k:v[0] for k,v in TYPES.items()},'subtypes_by_tier':{str(i):[] for i in range(1,5)},
      'high_tariff':{'threshold':99,'adds':[]},'command_words_by_subtype':CW,
      'tariff_overrides':{},
      'ao_by_objective_type':{'*':AO,'chem_practical':{'PROC':['C'],'INTERP':['C'],'MISCON':['C']},'chem_qualitative':{'PROC':['C'],'INTERP':['C'],'MISCON':['C']},
                              'chem_gas_flame':{'FEATURE':['A'],'PROC':['C']},'chem_diagram':{'APP':['A'],'INTERP':['B']}},
      'top_up':[],'misconception_slots':'one_per_entry',
      'performance_tasks':[{'item_type':'multiple_choice_set','papers':['1'],'brief':'A set of {n} original four-option questions; key, reason and misconception-based distractor explanations for each.'},
         {'item_type':'short_answer','papers':['2'],'brief':'An original structured chemistry activity with separately marked parts, worked answers and specific credit points.','ao_split':{'A':5,'B':3}},
         {'item_type':'practical_task','papers':['3'],'brief':'An original experimental context using appropriate apparatus, observations or data; independently checked answers, distinct credit points and a required visual.','ao_split':{'C':12}}]}
    extra={str(topic):[{'item_type':'calculation','papers':['2'],
            'brief':'An original multi-step mole/concentration calculation with unit conversion and independent arithmetic checks.' if topic==4 else 'An original calorimetry or bond-energy calculation with signs, units and independently checked arithmetic.',
            'ao_split':{'A':1,'B':4}}] for topic in [4,6]}
    write(WORK/'planning/slot-plan.json',{'slot_plan':slot,'additional_performance_by_topic':extra,'note':'Merged in memory into the schema-valid subject profile by build_resource_plan.py; no files under standard are edited.'})
    misconceptions=json.loads((CUR/'misconceptions.json').read_text())
    targets=['5.1-07','7.4-01','6.4-01','12.1-01','2.2-01','8.2-01-05','2.2-01','4.1-03','8.2-01-05',
             '2.4.2-05','12.2-02','8.1-01-05','6.4-09','12.5-01','2.1.2-09','2.4.2-01','5.1-04','2.1.2-09','8.1-01-05']
    assert len(targets)==len(misconceptions['records'])
    valid={o['objective_id'] for o in objectives}
    misconceptions['entries']=[]
    for entry,target in zip(misconceptions['records'],targets):
        oid='OBJ-6117-'+target;assert oid in valid,oid
        misconceptions['entries'].append({'entry_id':entry['id'],'topic_id':target.split('.')[0],'objective_id':oid,
            'n':1,'a':entry['confusion'],'test':entry['diagnostic_test'],'evidence_ids':[entry['evidence_id']]})
    write(CUR/'misconceptions.json',misconceptions)
    terms={
      'atom':'An electrically neutral particle of an element with equal numbers of protons and electrons.',
      'ion':'An atom or group of atoms with a net charge after gaining or losing electrons.',
      'isotope':'Atoms of the same element with the same proton number and different nucleon numbers.',
      'allotrope':'A different structural form of the same element.',
      'ionic bond':'Electrostatic attraction between oppositely charged ions.',
      'covalent bond':'Attraction between the nuclei of bonded atoms and their shared electrons.',
      'mole':'An amount of substance containing approximately 6.022 × 10²³ specified particles.',
      'Avogadro constant':'Approximately 6.022 × 10²³ particles per mole.',
      'relative atomic mass':'Average atomic mass relative to one twelfth of the mass of a carbon-12 atom; no unit.',
      'relative formula mass':'Sum of the relative atomic masses in a chemical formula; no unit.',
      'concentration':'Mass or amount of dissolved substance per unit solution volume; specify g/dm³ or mol/dm³.',
      'strong acid':'An acid that ionises completely in aqueous solution.',
      'weak acid':'An acid that ionises only partially in aqueous solution.',
      'base':'A proton acceptor in the aqueous proton-transfer model used here.',
      'alkali':'A water-soluble base that gives hydroxide ions in aqueous solution.',
      'precipitate':'An insoluble solid formed from substances in solution.',
      'solution':'A homogeneous mixture of a solute and solvent.',
      'observation':'A recorded change seen or measured, such as colour, a precipitate or gas bubbles.',
      'inference':'A conclusion drawn from observations, such as the identity of a gas or ion.',
      'titre':'Volume delivered from a burette, calculated as final reading minus initial reading.',
      'anode':'Electrode at which oxidation occurs; positive in an electrolytic cell.',
      'cathode':'Electrode at which reduction occurs; negative in an electrolytic cell.',
      'electrolyte':'A molten or dissolved ionic substance that conducts through mobile ions.',
      'rate of reaction':'Change in an appropriate measured quantity per unit time.',
      'catalyst':'A substance that increases reaction rate and is chemically unchanged at the end.',
      'dynamic equilibrium':'In a closed system, forward and reverse reaction rates are equal and macroscopic composition remains constant.',
      'oxidation':'Loss of electrons or gain of oxygen in the syllabus models.',
      'reduction':'Gain of electrons or loss of oxygen in the syllabus models.',
      'accuracy':'Closeness of a measured value to the accepted value.',
      'precision':'Closeness of repeated readings to one another, distinguished from accuracy.',
      'independent variable':'The variable deliberately changed during an investigation.',
      'dependent variable':'The measured response in an investigation.',
      'control variable':'A relevant variable kept constant to make a fair comparison.',
      'hydrocarbon':'A compound containing carbon and hydrogen only.',
      'homologous series':'A family sharing a functional group and general formula, with similar chemical properties.',
      'polymer':'A large molecule formed by joining repeating monomer units.',
      'biodegradable':'Capable of being broken down by microorganisms.',
    }
    write(CUR/'glossary.json',{'glossary_id':'GLOSSARY-NAM-6117','status':'planning_review',
       'authority':'Original wording consistent with the syllabus; review alongside the source objectives.',
       'terms':[{'term':term,'sense':sense,'homonym_warning':None} for term,sense in terms.items()]})
    print('Built planning inputs:',len(objectives),'registry entries;',len(source_map),'assessable objectives')


if __name__=='__main__':main()
