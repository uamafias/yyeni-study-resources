"""Build planner inputs, then invoke the shared contract/work-order generators.

Step 3 files are frozen first. Canonical planning views change identifiers only;
the original semantic mappings and source texts remain available in the snapshot.
Fine-grained members do NOT inherit measured exposure from their umbrella.
"""
from pathlib import Path
from collections import Counter
import copy, hashlib, json, re, shutil, subprocess, sys
import yaml
from pypdf import PdfReader
from plan_spec_6137 import MEMBERS,TYPE_GROUPS,SUPPLEMENTS,SUBTYPES,VISUALS,RESOURCE_MEMBERS,JUDGEMENT_MEMBERS

W=Path(__file__).resolve().parents[1];ROOT=W.parents[1];C=W/'curriculum';E=W/'assessment-evidence';P=W/'planning'
SNAP=P/'step3-source'
def read(p):return json.loads(p.read_text())
def dump(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def norm(s):return re.sub(r'\s+',' ',s).strip()

def snapshot():
    sources=['assessment-evidence/assessment_evidence.json','curriculum/exam-exposure.json',
             'curriculum/misconceptions.json','curriculum/scope-scan.json']
    if not (SNAP/'manifest.json').exists():
        manifest={}
        for rel in sources:
            src=W/rel;dst=SNAP/rel;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dst)
            manifest[rel]=hashlib.sha256(dst.read_bytes()).hexdigest()
        dump(SNAP/'manifest.json',manifest)
    for rel,h in read(SNAP/'manifest.json').items():
        assert hashlib.sha256((SNAP/rel).read_bytes()).hexdigest()==h,'Step 3 snapshot changed: '+rel

def cwtitle(word):return word[0].upper()+word[1:]
def source_id(id):return 'OBJ-6137-'+id
def papers(topic):return ['2'] if topic=='4.2' else (['1','2','3'] if topic in ('1.5','2.3','4.1') else ['1','2'])

def inputs():
    snapshot();facts=read(C/'syllabus-facts.json');mined=read(C/'mining-objectives.json')['objectives']
    commands=read(C/'command-word-observations.json')['commands'];topics=facts['content_outline'];aos=list(facts['ao_weights']['qualification'])
    typemap={o:t for t,ids in TYPE_GROUPS.items() for o in ids.split()}
    source_by={o['objective_id']:o for o in mined};rows=[];crosswalk={};meta={};sources={}
    def node(id,parent,topic,syll,learner,kind,tier,page,related=None):
        cws={'geo_concept':['Define','Suggest'],'geo_member':['Name','Identify','Describe'],
          'geo_compare':['Distinguish','Compare','Describe'],'geo_process':['Describe','Explain','Complete'],
          'geo_cause':['Explain','Describe','Suggest'],'geo_impact':['Explain','Describe','Suggest'],
          'geo_evaluate':['Describe','How far do you agree'],'geo_data':['Calculate','Describe','Compare','Complete'],
          'geo_map':['Calculate','Identify','Describe'],'geo_photo':['Describe','Identify','Suggest'],
          'enq_method':['Describe','Explain','Suggest'],'enq_present':['Complete','Describe','Calculate'],
          'enq_conclusion':['What','Describe','Suggest'],'geo_feature':['Describe','Identify'],
          'geo_member_interpret':['Describe','Identify','Compare'],
          'geo_member_judgement':['How far do you agree','Suggest']}[kind]
        return {'objective_id':id,'parent_id':parent,'topic_id':topic,'syllabus_text':syll,
          'learner_objective':learner,'level':'NSSCO','route_status':'core','mandatory':True,
          'objective_type':kind,'depth_tier':tier,'assessment_objectives':aos if '3' in papers(topic) else ['A','B','C'],
          'command_words':cws,'prerequisite_ids':[],'related_ids':related or [],'status':'planned',
          'syllabus_page':page,'papers':papers(topic),
          'source_coverage':{'rating':0,'action':'generate_gap','rationale':'Author original teaching from the named syllabus source and internal assessment evidence; source provenance and any member decomposition are recorded in planning/registry-provenance-6137.json.'}}
    for topic in topics:
        tid=topic['topic_id'];root=source_id(tid)
        rows.append(node(root,None,tid,tid+' '+topic['title'],topic['title'],'geo_concept',4,topic['pdf_pages'][0]))
    for o in mined:
        old=o['objective_id'];tid=o['topic_id'];id=source_id(old);crosswalk[old]=id
        kind=typemap.get(old,'geo_feature')
        if old=='X.01':kind='geo_impact'
        if old=='X.02':kind='geo_impact'
        tier=3 if kind in ('geo_process','geo_cause','geo_impact','geo_evaluate','enq_method','enq_present','enq_conclusion') else 2
        rows.append(node(id,source_id(tid),tid,o['text'],o['text'],kind,tier,o['source']['pdf_page']))
        sources[id]={'source':o['source'],'derivation':'verbatim source outcome/aim; classification and paper assignment are planner judgement','source_mining_id':old}
        children=[]
        for i,member in enumerate(MEMBERS.get(old,'').split('|') if old in MEMBERS else [],1):
            cid=id+f'-{i:02d}';children.append(cid)
            # Single concise retrieval target; its process/context is developed in the umbrella slot/notes.
            ckind='geo_member'
            if old in RESOURCE_MEMBERS:ckind='geo_member_interpret'
            if old in JUDGEMENT_MEMBERS:ckind='geo_member_judgement'
            if tid=='4.1' and old in ('4.1.03','4.1.04'):ckind='enq_method'
            if tid=='4.1' and old=='4.1.07':ckind='enq_present'
            if tid=='4.1' and old=='4.1.08':ckind='enq_conclusion'
            if tid=='4.2' and old in ('4.2.02','4.2.03','4.2.07'):ckind='geo_map'
            if tid=='4.2' and old=='4.2.06':ckind='geo_photo'
            # Member wording is an explicit planner decomposition, never a fake source quotation.
            learner=('Interpret '+member+' from a supplied original resource' if ckind=='geo_member_interpret' else
                     'Judge '+member+' in a supplied setting against an explicit criterion' if ckind=='geo_member_judgement' else 'Explain or use '+member)
            rows.append(node(cid,id,tid,member,learner,ckind,1 if ckind=='geo_member' else 2,o['source']['pdf_page'],[id]))
            sources[cid]={'source':o['source'],'derivation':'planner decomposition of the named member within this source outcome; not verbatim independent syllabus bullet','member':member,'source_mining_id':old}
        if children:meta[id]={'members':children,'rule':'Teach the umbrella and its members without implying all members inherit the umbrella’s examination frequency.'}
    pdf=PdfReader(ROOT/facts['source_document'])
    for tid,suffix,label,phrase,page,kind,pp in SUPPLEMENTS:
        id=source_id(tid+'.'+suffix)
        if page:
            text=norm(pdf.pages[page-1].extract_text());hits=list(re.finditer(re.escape(phrase),text,re.I))
            assert hits,(id,phrase)
            hit=hits[-1] if phrase=='Surveys:' else hits[0]
            quote=text[hit.start():min(len(text),hit.start()+400)]
            src={'path':facts['source_document'],'pdf_page':page,'verbatim':quote}
        else:
            # Fixed part references, selected by the miner's demand reading, not a token exposure match.
            refs={'81':'6137-2024-P1-1(a)(i)','82':'6137-2024-P1-1(c)',
                  '83':'6137-2022-P2-4(b)(iii)','84':'6137-2022-P1-2(b)(ii)','85':'6137-2024-P1-1(b)(ii)'}
            r=next(r for r in read(SNAP/'assessment-evidence/assessment_evidence.json')['records'] if r['evidence_id']==refs[suffix])
            src={**r['source_locator'],'evidence_id':r['evidence_id'],'verbatim':r['source_excerpt']}
            page=8
        row=node(id,source_id(tid),tid,label,label,kind,3,page);row['papers']=pp;rows.append(row)
        sources[id]={'source':src,'derivation':'syllabus practical paragraph' if suffix.startswith('9') else 'explicit corpus teaching target within syllabus weathering types; contextual source, not a new closed syllabus list'}
    dump(C/'objective_registry.json',{'registry_id':'REG-NAM-6137-NSSCO-2026','qualification_profile_id':'nam-6137-nssco-2026',
        'subject_profile_id':'yyeni-6137-geography-2026','authority':facts['source_document'],
        'granularity_note':'Source bullets plus explicit listed members and source-backed practical/corpus subtargets. Only the eighteen topic roots are non-assessable. The original 142 source IDs have an explicit crosswalk; finer exposure remains unmeasured unless separately evidenced.',
        'papers_note':'All thematic content is available to Papers 1/2; only adopted 2026 coastal/tourism investigations plus integrated enquiry skills are assigned Paper 3. This does not remove other practical teaching.',
        'objectives':rows})
    dump(P/'registry-provenance-6137.json',{'sources':sources,'container_members':meta,'source_id_crosswalk':crosswalk})
    dump(C/'unit_titles.json',{str(i+1):t for i,t in enumerate(['Physical Geography','Economic activities and the use of resources','Population and Settlement Studies','Integrated Research and Map Skills'])})

    # Immutable source records are retained. This canonical planning view rekeys IDs without changing meaning.
    evidence=read(SNAP/'assessment-evidence/assessment_evidence.json')
    for r in evidence['records']:
        r['source_objective_ids']=r['objective_ids'];r['objective_ids']=[crosswalk[x] for x in r['source_objective_ids']]
        r['planner_identifier_note']='Identifiers only rekeyed through planning/registry-provenance-6137.json; original mapping and excerpt retained in planning/step3-source.'
    evidence['planner_view']='Identifier overlay only. No source part was assigned to a fine-grained member without separate semantic evidence.'
    dump(E/'assessment_evidence.json',evidence)
    exp=read(SNAP/'curriculum/exam-exposure.json')
    for o in exp['objectives']:
        old=o['objective_id'];o['objective_id']=crosswalk[old]
        klass=o['exam_exposure'];o['exposure_class']={'probed_high':'frequent','probed_mid':'occasional','probed_low':'rare','unprobed_2020_2024':'unseen'}[klass]
        o['source_mining_id']=old;o['required_subtypes']=[]
    for row in rows:
        if row['parent_id'] and row['objective_id'] not in crosswalk.values():
            exp['objectives'].append({'objective_id':row['objective_id'],'exam_exposure':'unmeasured_bullet_level',
                'exposure_class':'unseen','required_subtypes':[],
                'note':'No numerical frequency inherited from the umbrella; this is full syllabus/practical coverage, not a claim that the member was never examined.'})
    exp['planner_view']='Source counts unchanged after an identifier-only crosswalk. Finer member frequencies deliberately unmeasured; derived source counts remain independently recomputable.'
    dump(C/'exam-exposure.json',exp)

    target=facts['ao_weights']['qualification'];fwcommands=[]
    for c in commands:
        word=cwtitle(c['command_word']);role=['A']
        if word in ('Compare','Complete','Calculate','Identify','Plot','Draw','Add','Label','Shade','Find and calculate','Measure and calculate','Determine'):role=['B']
        if 'agree' in word.lower() or word.startswith('Do ') or word=='What':role=['C']
        linked=[r for r in evidence['records'] if r['command_word']==c['command_word']]
        role=sorted({a for r in linked for a in r['ao_focus']})
        fwcommands.append({'word':word,'meaning':'Observed primary operation; read the whole prompt and contextual answer-shape evidence.',
           'observed_count':c['count'],'observed_tariffs':c['tariff_counts'],'modal_tariff':c['modal_tariffs'][0],
           'exact_mark_tariff':c['modal_tariffs'][0],'observed_mark_values':c['tariffs_seen'],
           'papers':c['paper_counts'],'primary_assessment_objectives':role,'use_in_prompts':True,'used_at_level':True,
           'provenance':'corpus: command-word-observations.json; normalization is miner judgement',
           'assessment_objectives_provenance':'Union of linked record focus labels, including explicitly tagged miner judgement; not an official marking split.'})
    inactive=['Annotate','Contrast','Demonstrate','Devise','Plan','Differentiate','Locate','Match','Account for','Evaluate','Analyse','Justify','Predict','Sketch']
    for word in inactive:
        fwcommands.append({'word':word,'observed_count':0,'observed_tariffs':{},'exact_mark_tariff':None,
           'used_at_level':False,'use_in_prompts':False,'verdict':'not observed as the assessed opening/operation in this corpus; use an observed form instead'})
    blooms={'DEF':'Remember','FEATURE':'Remember','DIST':'Understand','PROC':'Understand','WHY':'Understand',
       'MECH':'Understand','BEN':'Understand','LIM':'Evaluate','APP':'Apply','CHAIN':'Analyse','EVAL':'Evaluate',
       'CALC':'Apply','INTERP':'Analyse','MISCON':'Understand','SYNTH':'Create'}
    allowed={k:['A','B','C','D'] for k in blooms}
    allowed['DEF']=['A'];allowed['EVAL']=['C','D'];allowed['MISCON']=['A','B','D']
    fw={'framework_id':'FW-NAM-6137-NSSCO-2026','authority':facts['source_document'],
       'assessment_objectives':[{'code':a['code'],'name':a['name'],'description':' '.join(a['can_do']),
           'qualification_weight_percent':target[a['code']],'source':a['source']} for a in facts['assessment_objectives']],
       'papers':[{**p,'ao_split':{a:100*n/p['marks'] for a,n in p['ao_split_marks'].items()},
            'ao_split_unit':'derived percent; authoritative transcribed marks remain in ao_split_marks'} for p in facts['papers']],
       'command_words':fwcommands,'command_words_listed_but_never_used':[v['syllabus_row'] for v in read(C/'command-word-verdicts.json')['verdicts'] if not v['use_in_prompts']],
       'command_word_table_source':'syllabus-facts.json preserves all 38 printed mixed glossary rows with page quotes; observed forms are separate.',
       'ao_mark_budget':{'per_paper_marks':{'P'+p['paper']:p['ao_split_marks'] for p in facts['papers']},
           'stated_qualification_weight_percent':target,'arithmetic_note':'The source grid contains marks, not percentages. Overall percentages are exactly the sum of AO marks divided by 200.'},
       'flashcard_subtype_ao_map':[{'subtype':s,'assessment_objectives':allowed[s],'blooms_level':b,'tests':'Use the declared subject answer structure; narrow AO labels by actual objective/task.'} for s,b in blooms.items()],
       'blooms_taxonomy':{'required_on_every_item':True,'levels':[{'level':x} for x in ('Remember','Understand','Apply','Analyse','Evaluate','Create')],
          'by_subtype':blooms,'by_performance_task':{'short_answer':'Apply','data_response':'Analyse','case_analysis':'Evaluate','practical_task':'Evaluate'}},
       'item_mix_target':{'basis':'marks-equivalent','target_share_percent':target}}
    dump(C/'assessment-framework.json',fw)
    qp={'profile_id':'nam-6137-nssco-2026','version':'0.2.0-draft','status':'draft','board':'NIED / DNEA, Namibia',
       'qualification':'Namibia Senior Secondary Certificate Ordinary Level','subject':'Geography','syllabus_code':'6137',
       'examination_years':[2026],'syllabus_version':'NIED 2016; first examination 2020; operator-confirmed later Paper 3 circular for 2026',
       'selected_level':'NSSCO','route':{'route_id':'papers-1-2-3','name':'Three written papers including Alternative to Practicals','included_paper_ids':['1','2','3'],'excluded_paper_ids':[],
           'notes':'2026 Paper 3 physical coasts and human tourism, according to the separate confirmed circular record.'},
       'language':'English','learner_entry_assumptions':['Namibian secondary learners; introduce every new term before use.'],
       'papers':[{'paper_id':p['paper'],'name':p['name'],'duration_minutes':p['duration_minutes'],'marks':p['marks'],
          'qualification_weight_percent':p['weight_percent'],'question_basis':p['source']['verbatim'],
          'assessment_objective_weights':{a:100*v/p['marks'] for a,v in p['ao_split_marks'].items()}} for p in facts['papers']],
       'assessment_objectives':[{k:a[k] for k in ('code','name','description','qualification_weight_percent')} for a in fw['assessment_objectives']],
       'command_words':[{'word':c['word'],'meaning':c.get('meaning','Observed task form.')} for c in fwcommands if c['use_in_prompts']],
       'scope':{'included_topic_ids':[t['topic_id'] for t in topics],'excluded_topic_ids':[],'optional_routes':[]},
       'source_authority':{'curricular':[facts['source_document'],'curriculum/paper3-prescribed-topics-2025-2029.json'],
          'assessment':['assessment-evidence/extraction-manifest.json'],'conceptual':['curriculum/glossary.json'],
          'conflict_rule':'Assessment sources establish demand; primary disciplinary sources settle scientific/statistical definitions. Preserve discrepancies explicitly.'},
       'example_selection_rules':['Use Namibian and southern African contexts, British English and N$ where relevant.','Use real verified places for case studies; invented named businesses for fictional scenarios.'],
       'notes':['Per-paper assessment_objective_weights are arithmetic percentages, not a transcription of the source marks grid. Exact marks and source pages are in syllabus-facts.json.']}
    (W/'qualification-profile.yaml').write_text(yaml.safe_dump(qp,sort_keys=False,allow_unicode=True))

    structures={'DEF':['meaning|term|definition'],'FEATURE':['feature|name|point'],
       'DIST':['difference|whereas|while'],'PROC':['step|sequence|first','result|record|measurement'],
       'WHY':['reason|because'],'MECH':['cause|because','effect|result'],
       'BEN':['advantage|benefit','because|effect'],'LIM':['limitation|problem','effect|because'],
       'APP':['given|resource|context|evidence','reason|because|application'],
       'CHAIN':['cause|factor','link|because','effect|result'],
       'EVAL':['judgement|decision|conclusion','evidence|reason|support'],
       'CALC':['method|working','answer|result','unit|units|ratio'],
       'INTERP':['pattern|trend|relationship|feature','evidence|value|data|observation'],
       'MISCON':['confusion|error','correct|distinction','test|discriminate'],
       'SYNTH':['link|combine','reason|effect'],
       'short_answer':['point|method','mark|marks'],
       'data_response':['resource|data','evidence|value','mark|marks'],
       'case_analysis':['judgement|decision','reason|evidence','mark|marks'],
       'practical_task':['hypothesis','method|sampling','data|evidence','conclusion','evaluation|improvement']}
    aoby={'*':{'DEF':['A'],'FEATURE':['A'],'DIST':['A'],'PROC':['A'],'WHY':['A'],'MECH':['A'],
           'BEN':['A'],'LIM':['C'],'APP':['B'],'CHAIN':['A'],'EVAL':['C'],'CALC':['B'],'INTERP':['B'],'MISCON':['A'],'SYNTH':['C']},
          'enq_method':{'PROC':['D'],'WHY':['D']},'enq_present':{'APP':['D'],'INTERP':['D']},
          'enq_conclusion':{'EVAL':['C'],'INTERP':['D']},'geo_map':{'CALC':['B'],'INTERP':['B']}}
    cwby={'DEF':['Define'],'FEATURE':['Name'],'DIST':['Distinguish'],'PROC':['Describe'],'WHY':['Explain'],
       'MECH':['Explain'],'BEN':['Describe'],'LIM':['Suggest'],'APP':['Suggest'],'CHAIN':['Explain'],
       'EVAL':['How far do you agree','What'],'CALC':['Calculate'],'INTERP':['Describe'],'MISCON':['Explain'],'SYNTH':['Explain']}
    tariff={'DEF:Define':1,'FEATURE:Name':1,'DIST:Distinguish':3,'PROC:Describe':3,'WHY:Explain':2,
       'MECH:Explain':3,'BEN:Describe':2,'LIM:Suggest':2,'APP:Suggest':3,'CHAIN:Explain':4,
       'EVAL:How far do you agree':5,'EVAL:What':3,'CALC:Calculate':3,'INTERP:Describe':3,'MISCON:Explain':2,'SYNTH:Explain':4}
    perf=[{'item_type':'short_answer','papers':['1'],'brief':'Seven-mark original thematic/resource mini-package: short knowledge and explanation parts totalling 5 A marks plus two evidence-reading B marks. Choose live commands and exact tariffs for each part. This is a teaching package, not a copied whole question. In integrated enquiry use content-linked interpretation, not a supposed Paper 1 fieldwork-method question.','ao_split':{'A':5,'B':2}},
      {'item_type':'data_response','papers':['2'],'brief':'Seven-mark original map/photograph/graph/data package, tailored to this topic: one knowledge mark, five analytical/resource marks and one supported decision mark. Supply all resources and keys needed. In map skills use a consistent 1:50000 map; use actual licensed photographs where the outcome names photographs.','ao_split':{'A':1,'B':5,'C':1}},
      {'item_type':'case_analysis','papers':['1'],'brief':'Five-mark judgement on a precise geographical claim with a verified named case where appropriate. Use How far do you agree; judge relevant facts and reach a supported decision. Four marks judge relevant facts and one credits the supported decision, which may be implied. Apply the 2024 demand without forcing equal-sided essays. In integrated enquiry apply the judgement to the supplied investigation evidence.','ao_split':{'C':5}}]
    for i in range(4):
        focus=['equipment, measurement and a usable sequence','sampling, recording and practical limitations','graphical completion, evidence and exceptions','independent investigation design, paired data and method evaluation'][i]
        perf.append({'item_type':'practical_task','papers':['3'],'brief':f'Original 30-mark investigation variant {i+1}: emphasis on {focus}. Use coastal processes for topic 1.5, tourism for topic 2.3, and alternating coastal/tourism contexts in topic 4.1. Include short parts with observed command/tariff combinations, two testable hypotheses, all data/stimuli, conclusions and specific evaluation. Planned allocation A6/B6/C6/D12 is a proportional teaching design from the 60-mark grid, not a claim that every official question has this split.','ao_split':{'A':6,'B':6,'C':6,'D':12}})
    sp={'profile_id':'yyeni-6137-geography-2026','version':'0.2.0-draft','status':'draft','subject_name':'Geography NSSCO 6137',
       'language_variant':'British English','purpose':'Full teaching notes, retrieval/application cards and resource/investigation practice for Namibian learners on the confirmed 2026 three-paper route.',
       'foundational_concepts':['process and landform','spatial evidence','cause and consequence','scale and time','sustainability','geographical enquiry'],
       'depth_model':{'note_mode':'full teaching depth','rule':'Teach every named member, causal link, method and relevant case detail. Member notes complement the umbrella explanation; avoid repeated prose. Word budgets are generated, not a target to skim just above.'},
       'answer_structures':structures,'variant_register':[
          {'term':'sampling','variants':['random','systematic','stratified'],'consequence':'Selection rules have different implications for coverage and bias.'},
          {'term':'plate boundary','variants':['constructive','destructive','conservative'],'consequence':'State the relevant movement and hazard mechanism.'},
          {'term':'wave type','variants':['constructive','destructive'],'consequence':'Compare relative swash/backwash and sediment effects, subject to local conditions.'},
          {'term':'industry type','variants':['primary','secondary','tertiary'],'consequence':'Distinguish resource extraction, processing and service provision.'},
          {'term':'migration type','variants':['internal','international'],'consequence':'Specify the boundary crossed and the source/destination population.'}],
       'conditioned_mechanisms':[
          {'mechanism_id':'CM-6137-BIOMASS','name':'Wood renewability','asserted_when':[r'\bwood\b',r'\brenewable\b'],
           'required_conditions':[{'name':'replenishment/sustainable harvesting','any_of':[r'\bregrow',r'\breplenish',r'\bsustainab',r'\bharvest']}]}],
       'glossary_homonyms':[{'term':'watershed','rule':'Use watershed for the divide in this NSSCO teaching context; distinguish the US catchment usage explicitly in teacher metadata.'},
          {'term':'relief','rule':'Distinguish land relief, relief rainfall and emergency aid.'},
          {'term':'discharge','rule':'Specify river-flow volume per time or waste discharge.'}],
       'prohibited_patterns':['No copied examination text or recycled map answers.','No invented numbers for real case studies.','No description of a picture as a replacement when visual interpretation is the learning target.','No universal conclusion/working/example-mark formula.','No greenhouse/ozone conflation.'],
       'depictions':{'chart_model':'none','code_fence_languages':[],
           'rule':'Use original PNG/SVG assets rendered from reproducible numerical/vector specifications. Images are linked in notes/items; no handwritten code-fence graphics. Full keys, units, orientation, readable labels and independent review are mandatory. The shared text-chart renderer is not a general Geography image validator.'},
       'slot_plan':{'subtypes_by_objective_type':SUBTYPES,'subtypes_by_tier':{1:[],2:[],3:[],4:[]},
          'high_tariff':{'threshold':99,'adds':[]},'command_words_by_subtype':cwby,'tariff_overrides':tariff,
          'tariff_override_reasons':{k:'Planner-selected observed command/tariff pair; marking shape must match this exact new task, with uncertainty labelled where complete schemes are absent.' for k in tariff},
          'ao_by_objective_type':aoby,'ao_by_paper':{'1+2':{'D':'A'}},
          'top_up':[],'misconception_slots':'one_per_entry','performance_tasks':perf,
          'note':'No padding to chase AO percentages. B labels require real evidence analysis; D labels require actual investigation/presentation work. Paper 3 focus follows the adopted circular. C remains Judgment and decision making; do not rely on shared AO-role name inference.'}}
    (W/'subject-profile.yaml').write_text(yaml.safe_dump(sp,sort_keys=False,allow_unicode=True))

    # Adapt only schema/identifiers. The curated error statements and their evidence remain intact.
    mc=read(SNAP/'curriculum/misconceptions.json');entries=[]
    for m in mc['misconceptions']:
        ids=[crosswalk[x] for x in m['objective_ids']];first=ids[0]
        # Select a concept-bearing home, rather than a generic skill secondary tag.
        if m['title']=='Service and evidence':first=source_id('4.2.05')
        if m['title']=='Tally counts and environmental scores':first=source_id('4.1.03')
        if m['title']=='Storeys and exact building height':first=source_id('4.1.06')
        topic=next(o['topic_id'] for o in rows if o['objective_id']==first)
        entries.append({**m,'entry_id':m['misconception_id'],'topic_id':topic,'objective_id':first,
           'objective_ids':ids,'a':m['confusion'],'b':m['distinction_to_teach'],'test':m['discriminating_card_demand'],
           'n':len(m['finding_ids']),'series':sorted({f.split('-')[1] for f in m['finding_ids']}),'evidence_scope':'question-specific'})
    mc['entries']=entries;mc['planner_view']='Build-compatible entry fields and identifier crosswalk; frozen original is retained in planning/step3-source.'
    dump(C/'misconceptions.json',mc)
    scan=read(SNAP/'curriculum/scope-scan.json');scan['entries']=[{
       'construct':r['limit_id'],'pattern':r['pattern'],'source':f"NIED 6137 syllabus PDF p{r['source']['pdf_page']}: {r['source']['verbatim']}",
       'controls':{'must_catch':r['must_catch'],'must_allow':r['must_leave']},'syllabus_sentence':r['source']['verbatim'],
       'provenance':{'sentence':'syllabus','pattern':'planner judgement; context-specific claim detector'}} for r in scan['rules']]
    dump(C/'scope-scan.json',scan)
    dump(C/'syllabus-exclusions.json',{t['topic_id']:[r['source'] for r in scan['rules']] for t in topics})
    dump(C/'dependency_graph.json',{'edges':[],'note':'Within each source outcome, teach the umbrella before its named members; integrate skills into the relevant content. Registry parent/related IDs carry these links.'})
    print('Registry',len([o for o in rows if o['parent_id']]),'assessable outcomes; source snapshot verified.')

def generate():
    for cmd in [
       ['conform_registry.py',str(W)],['make_contract.py',str(W),'--force'],['make_work_order.py',str(W),'--all']]:
        subprocess.run([sys.executable,str(ROOT/'standard/v0.2.0-draft/build'/cmd[0]),*cmd[1:]],cwd=ROOT,check=True)

if __name__=='__main__':
    inputs();generate()
