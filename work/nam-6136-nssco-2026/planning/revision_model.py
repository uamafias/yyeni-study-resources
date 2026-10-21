"""Explicit 6136 demand decisions after Claude F-01..F-21. No standard edits.

Source outcome clauses remain authoritative; these are pedagogical judgements,
not official item-level marking allocations. Stable IDs survive folded examples.
"""
from collections import Counter
import re

PARENTS = {
 '1.1': ['DEF APP','FEATURE INTERP','WHY INTERP','WHY EVAL CALC','FEATURE INTERP','WHY INTERP','WHY CHAIN'],
 '1.2': ['DEF APP','APP CHAIN','EVAL APP'],
 '2.1': ['FEATURE APP'], '2.2': ['WHY PROC','DIST EVAL'],
 '3.1': ['DEF DIST','FEATURE APP','WHY CHAIN','WHY APP','DIST APP','FEATURE CHAIN','FEATURE APP','WHY APP','DIST APP','FEATURE CALC INTERP',None,'WHY APP','FEATURE CHAIN','EVAL APP'],
 '4.1': ['DEF WHY','FEATURE INTERP','DIST EVAL','FEATURE EVAL','WHY CHAIN','APP CHAIN'],
 '4.2': ['DEF INTERP CALC','WHY INTERP','FEATURE CHAIN','APP EVAL','DIST INTERP'],
 '5.1': ['FEATURE DIST','FEATURE CHAIN','FEATURE INTERP','WHY EVAL','WHY CHAIN','WHY APP','EVAL APP','CHAIN INTERP'],
 '6.1': ['FEATURE WHY','WHY CHAIN','EVAL INTERP'],
 '6.2': ['DEF APP','FEATURE INTERP CALC','EVAL INTERP','EVAL APP','WHY CHAIN','APP CHAIN'],
 '7.1': ['DIST CALC','WHY INTERP','CALC INTERP','EVAL APP','APP INTERP','INTERP CALC','EVAL INTERP'],
 '7.2': ['WHY CHAIN CALC','EVAL INTERP','CHAIN EVAL'],
 '7.3': ['DIST APP','DIST EVAL','DIST APP','CALC INTERP','CHAIN EVAL','WHY EVAL','WHY CHAIN'],
 '8.1': ['WHY APP','FEATURE DIST','DIST WHY','WHY CHAIN','WHY CHAIN'],
 '9.1': ['DEF APP','WHY CHAIN','DIST CALC','CALC CHAIN','INTERP CHAIN','DEF APP','EVAL CHAIN','APP CHAIN'],
 '9.2': ['DIST APP','EVAL CHAIN','FEATURE APP'], '9.3': ['EVAL INTERP','EVAL APP'],
 '10.1': ['FEATURE APP','FEATURE WHY','FEATURE PROC','DIST APP','DIST FEATURE','FEATURE PROC','WHY EVAL','DEF PROC APP','DIST APP','PROC WHY','INTERP CALC PROC','INTERP EVAL APP'],
}
# Complete example lists remain taught in the parent, with at least one worked
# example, but do not create one compulsory two-card set per illustrative case.
FOLD_LISTS = {'1.1:1','1.1:5','2.1:1','4.1:4','4.1:5','6.2:4','7.2:2'}
FOLD_MEMBERS = {'2.2:2': {3}, '7.3:6': {1}}

TERM_KEYS = {'1.1:1','1.1:6','3.1:1','3.1:2','3.1:4','3.1:5','3.1:7','3.1:9','3.1:10',
             '3.1:12','7.1:1','7.1:3','7.3:1','7.3:3','8.1:1','8.1:2','8.1:3','9.1:3','9.2:1',
             '10.1:3','10.1:4','10.1:5','10.1:9'}
FACTOR_KEYS = {'1.1:7','3.1:3','4.2:3','5.1:2','5.1:5','5.1:6','6.1:2','6.1:3','6.2:3','6.2:5','7.1:2','7.2:1','8.1:4','8.1:5'}
STRATEGY_KEYS = {'4.1:3','4.2:4','5.1:4','5.1:7','7.1:4','7.3:6','9.3:1'}
DATA_KEYS = {'1.1:3','7.3:4'}

STRUCTURES = {
 'DEF':['meaning'], 'FEATURE':['feature'], 'DIST':['comparison'], 'WHY':['reason'],
 'APP':['context','reason'], 'CHAIN':['mechanism','consequence'],
 'INTERP':['evidence','relationship'], 'EVAL':['judgement','reason'],
 'PROC':['sequence','application'], 'CALC':['working','unit'],
 'MISCON':['error','distinction'],
 'short_answer':['point','development'], 'data_response':['evidence','meaning'],
 'practical_task':['method','evidence','response'], 'source_analysis':['findings','evidence','conclusion'],
}
CW = {'DEF':['Define'],'FEATURE':['Identify','Name','State','Describe'],
      'DIST':['Differentiate','Compare'],'WHY':['Explain'], 'APP':['Suggest','Explain'],
      'CHAIN':['Explain'], 'INTERP':['Describe','Compare'],
      'EVAL':['Choose','Describe and evaluate','Explain','Discuss','Suggest'],
      'PROC':['Name and describe','Describe'], 'CALC':['Calculate','By how much'], 'MISCON':['Explain']}
TARIFFS = {'Define':1,'Identify':1,'Name':1,'State':2,'Describe':2,
 'DIST:Differentiate':2,'DIST:Compare':2,'WHY:Explain':2,'APP:Suggest':3,'APP:Explain':3,
 'CHAIN:Explain':3,'INTERP:Describe':3,'INTERP:Compare':3,
 'EVAL:Choose':3,'EVAL:Describe and evaluate':4,'EVAL:Explain':4,'EVAL:Discuss':4,'EVAL:Suggest':3,
 'PROC:Name and describe':4,'PROC:Describe':4,'CALC:Calculate':2,'CALC:By how much':2,'MISCON:Explain':2}
SUBAOS={'DEF':['A','C'],'FEATURE':['A','C'],'DIST':['A','B','C'],'WHY':['A','C'],
        'APP':['A','B','C','D'],'CHAIN':['B'],'INTERP':['B'],'EVAL':['B'],
        'PROC':['A','C'],'CALC':['B'],'MISCON':['A','B','C','D']}
BLOOMS={'DEF':'Remember','FEATURE':'Remember','DIST':'Understand','WHY':'Understand',
        'APP':'Apply','CHAIN':'Analyse','INTERP':'Analyse','EVAL':'Evaluate','PROC':'Apply','CALC':'Apply','MISCON':'Understand'}

def key_parts(key):
 t,b=key.split(':');return t,int(b)
def oid_for(key,member=0):
 t,b=key_parts(key);return f'OBJ-6136-{t}.{b:02d}-{member:02d}'

def parent_subtypes(key):
 t,b=key_parts(key);s=PARENTS[t][b-1];assert s is not None,key
 return s.split()

def folded(key,index):return key in FOLD_LISTS or index in FOLD_MEMBERS.get(key,set())

def member_role(key,i,text):
 if key=='4.2:5':return 'comparison'
 if key in {'1.1:7','4.2:3','5.1:5','6.1:3','6.2:3','7.1:2','8.1:5'}:return 'causal_evidence'
 if key=='5.1:2':return 'feature'
 if key in TERM_KEYS:return 'term'
 if key in FACTOR_KEYS:return 'factor'
 if key in STRATEGY_KEYS:return 'strategy'
 if key in DATA_KEYS:return 'indicator'
 if key=='10.1:2':return 'research_feature'
 if key in {'10.1:6','10.1:10'}:return 'research_method'
 if key=='10.1:11':return 'research_representation' if i>1 else 'research_interpretation'
 if key=='10.1:12':return 'research_recommendation' if i==2 else 'research_conclusion'
 return 'feature'

def member_subtypes(key,i,role):
 if role=='term':
  return ['DEF','CALC'] if key=='3.1:10' else ['DEF']
 return {'factor':['WHY'],'strategy':['EVAL'],'indicator':['INTERP'],
         'causal_evidence':['CHAIN'],'comparison':['DIST'],
         'feature':['FEATURE'],'research_feature':['FEATURE'],
         'research_method':['PROC','WHY'],'research_representation':['PROC'],
         'research_interpretation':['INTERP'],'research_conclusion':['INTERP'],
         'research_recommendation':['APP']}[role]

def member_learner(key,i,text,role):
 from repair_review_demands import NATURAL_TITLES
 if role=='feature' and text in NATURAL_TITLES:return NATURAL_TITLES[text]
 verb={'term':'Define','factor':'Explain the influence or mechanism of','strategy':'Judge the suitability of',
       'causal_evidence':'Use a new evidence-bearing case to infer the causal influence of',
       'comparison':'Differentiate the two concepts in',
       'indicator':'Interpret evidence using','feature':'Describe the relevant characteristics or role of',
       'research_feature':'State and apply the selection requirement of','research_method':'Describe how to select and use',
       'research_representation':'Construct and justify the use of','research_interpretation':'Interpret collected evidence to establish',
       'research_conclusion':'Draw an evidence-supported','research_recommendation':'Propose a feasible, evidence-linked'}[role]
 if key=='10.1:2' and i==4:text='a specific area, time and date'
 return f'{verb} {text}.'

def source_commands(text,source_records,bridge_id,member_evidence_ids=None):
 # Verbs come from the literal source; this does not select the teaching type.
 words=[];trans={'define':'Define','describe':'Describe','explain':'Explain','discuss':'Discuss',
 'suggest':'Suggest','identify':'Identify','name':'Name','differentiate':'Differentiate',
 'distinguish':'Differentiate','compare':'Compare','interpret':'Describe','analyse':'Describe'}
 for v in re.findall(r'\b(?:define|describe|explain|discuss|suggest|identify|name|differentiate|distinguish|compare|interpret|analyse)\b',text,re.I):
  if trans[v.lower()] not in words:words.append(trans[v.lower()])
 rs=[r for r in source_records if bridge_id in r['objective_ids']] if member_evidence_ids is None else [r for r in source_records if r['evidence_id'] in member_evidence_ids]
 observed=list(dict.fromkeys(r['command_word'] for r in rs))
 return words,observed

def planned_commands(subtypes,literal,observed,role,text,key):
 # Explicit semantic adaptations are recorded alongside literal and observed
 # forms; they are never called observed on an unseen member.
 planned=[];why=[]
 for st in subtypes:
  if st=='FEATURE':
   word=next((w for w in CW[st] if w in literal or w in observed),'Describe')
  elif st=='DIST':word='Compare' if 'Compare' in observed else 'Differentiate'
  elif st=='EVAL':
   word='Discuss' if key in {'1.2:3','9.3:1','9.3:2'} else 'Describe and evaluate' if key=='7.3:2' else 'Explain'
  elif st=='PROC':word='Name and describe' if key in {'10.1:6','10.1:10'} else 'Describe'
  else:word=CW[st][0]
  if word not in planned:planned.append(word)
  why.append({'subtype':st,'planned_command':word,'authority':'syllabus' if word in literal else 'corpus' if word in observed else 'judgement',
              'reason':'Source-demand-shaped practice. A planner adaptation uses an observed 6136 command for this answer function, not proof that this member was previously tested.'})
 # Registry candidates must not prefer an irrelevant observed word over the
 # command chosen for its semantic role. Single target types have narrow lists.
 return planned,why

def aos(subtypes,key,role,member=0):
 research=key.startswith('10.1:');out={}
 for st in subtypes+['MISCON']:
  a='B' if st in {'CHAIN','INTERP','EVAL','CALC'} else 'C' if research else 'A'
  if research and st=='APP':a='D' if key in {'10.1:8','10.1:12'} else 'C'
  out[st]=[a]
 return out

DEPTH_CEILINGS={
 '1':'Teach indicator meaning, use and limitations; no HDI geometric-mean or MPI weighting formulae. Country categories and example indicators illustrate the parent outcome.',
 '2':'Compare short/long planning and evaluate one clearly dated plan example. Do not teach every historical NDP as a separate examinable programme or assert it is current.',
 '3':'Teach named energy/technology forms, productive use and contextual trade-offs. No engineering designs, nuclear physics or advanced cost theory.',
 '4':'Teach industrial strategies, urban patterns, problems and feasible responses at NSSCO depth. Named NICs and industries are illustrations, not compulsory country histories.',
 '5':'Teach the listed rural systems, schemes, conservation and tourism with concrete local reasoning. Avoid agronomy or tourism-management specialisms.',
 '6':'Teach roles, opportunities, inequalities and development responses sensitively. No invented current law, clinical advice, personal disclosure exercises or causal stereotypes.',
 '7':'Teach population rates/structure, health provision and education relationships. Do not add extra DTM stages or clinical treatment guidance; use synthetic data for practice.',
 '8':'Teach listed political terms and approaches and their development implications; no comparative constitutional-law syllabus or ideological history survey.',
 '9':'Teach trade measures, patterns, investment/aid and named cooperation bodies. No detailed balance-of-payments sub-account accounting or advanced macroeconomic theory.',
 '10':'Teach random, systematic and stratified sampling; enquiry planning, instruments, pilot, representation, evidence and practical project responses. No cluster/quota/snowball sampling or inferential statistics. Prioritise suitable bar/pie/divided-rectangle forms; no generated line-graph practice, following report advice (not a syllabus ban).'
}

def connections(objectives,lookup):
 byid={o['objective_id']:o for o in objectives}
 pairs=[('7.3:3',3,'7.3:6',0),('1.1:4',0,'1.1:5',0),('1.1:2',4,'8.1:3',0),
 ('3.1:12',4,'4.1:3',4),('3.1:12',4,'9.2:2',1),('3.1:12',2,'5.1:4',2),
 ('3.1:4',1,'5.1:2',2),('8.1:4',3,'9.1:8',1)]
 for ka,ia,kb,ib in pairs:
  a,b=oid_for(ka,ia),oid_for(kb,ib)
  if a in byid and b in byid:
   byid[a]['related_ids'].append(b);byid[b]['related_ids'].append(a)
   byid[b]['syllabus_guidance']+=' Reuse the canonical definition taught at '+a+'; practise this outcome’s distinct application rather than another identical definition.'
 for key,prereq in [('1.1:4','1.1:1'),('4.2:2','4.2:1'),('7.1:6','7.1:1'),('9.1:4','9.1:3'),
                    ('10.1:8','10.1:6'),('10.1:10','10.1:9'),('10.1:11','10.1:5'),('10.1:12','10.1:11')]:
  byid[oid_for(key)]['prerequisite_ids'].append(oid_for(prereq))

def components(*rows):
 return [{'command_word':w,'mark_tariff':n,'ao_split_judgement':a,'purpose':purpose,'section':section} for w,n,a,purpose,section in rows]

def performance_plans(titles):
 plans={}
 quantitative={'1.1':'GNP per person','3.1':'sector employment shares','4.2':'urban population shares',
               '6.2':'women’s participation percentages','7.1':'population density and rates',
               '7.2':'health-service coverage','7.3':'literacy/enrolment','9.1':'exports minus imports'}
 for tid,title in titles.items():
  if tid=='10.1':continue
  a=components(('State',2,{'A':2},f'Two relevant {title} facts or terms','content'),
               ('Explain',4,{'A':1,'B':3},f'Use two supplied facts to develop a new relationship or contrast in {title}; generic recall cannot earn the B credit','content'))
  if tid in quantitative:
   b=components(('Calculate',2,{'B':2},f'Compute {quantitative[tid]} from an original table, with working and unit','content'),
                ('Explain',4,{'B':4},'Interpret the result with another supplied fact; distinguish what the data establishes and the decision it supports','content'))
  else:
   b=components(('Describe',3,{'B':3},f'Infer a relationship in a new {title} table or short contrasting sources and cite two relevant observations','content'),
                ('Suggest',3,{'B':3},'Propose and justify a choice using the supplied evidence and stated development criterion','content'))
  plans[tid]=[{'item_type':'short_answer','title':title+' evidence-linked explanation','parts':a},
              {'item_type':'data_response','title':title+' numerical interpretation' if tid in quantitative else title+' source comparison','parts':b}]
 A1=components(
  ('Identify',1,{'C':1},'Identify the enquiry population from the supplied water-access survey','A1'),
  ('Design',5,{'C':5},'Design five usable questionnaire elements for the stated enquiry, with neutral wording and recordable responses','A1'),
  ('Describe',4,{'C':4},'Carry out systematic selection from the stated household list after a suitable start','A1'),
  ('Explain',2,{'C':2},'Explain how consent and privacy are protected in this non-sensitive survey','A1'),
  ('Suggest',3,{'D':3},'Repair the specific pilot wording difficulty and explain the improvement','A1'),
  ('Calculate',2,{'B':2},'Calculate a survey proportion or difference from supplied counts','A1'),
  ('Draw',4,{'C':4},'Construct a suitable bar chart from the original categorical counts','A1'),
  ('Describe',4,{'B':4},'Use the chart and source evidence to describe the water-access pattern','A1'),
  ('State',2,{'D':2},'State two feasible aims for a small community water-storage activity','A2'),
  ('Describe',3,{'D':3},'Organise volunteers, permissions and responsibilities for that activity','A2'),
  ('Suggest',2,{'D':2},'Propose feasible funding linked to the stated cost/resources','A2'),
  ('Explain',3,{'D':3},'Match one implementation obstacle to a practical response and responsible implementer','A2'))
 # Distinct second stimulus: price/production survey; 20+15 as observed in 2022.
 A2=components(
  ('Name',1,{'C':1},'Name the collection method shown by the invented farm-price survey','A1'),
  ('Name and describe',4,{'C':4},'Apply interview and observation procedures to the two stated data needs','A1'),
  ('Describe',4,{'C':4},'Select a stratified sample using the supplied village groups','A1'),
  ('Explain',3,{'C':3},'Explain why the sample design fits this enquiry and its limitations','A1'),
  ('Suggest',3,{'D':3},'Resolve the stated practical access/recording obstacle without changing the enquiry aim','A1'),
  ('Design',5,{'C':5},'Design a short observation record for the stated rural-production variables','A1'),
  ('Calculate',2,{'B':2},'Calculate the production difference between two periods','A2'),
  ('Describe',3,{'B':3},'Compare the two periods using appropriate figures','A2'),
  ('Draw',4,{'C':4},'Construct a divided rectangle from the supplied resource-use shares','A2'),
  ('Explain',3,{'B':3},'Infer a plausible relationship between resource use and output, bounded by the supplied evidence','A2'),
  ('Suggest',3,{'D':3},'A practical improvement to the stated production/recording problem','A2'))
 A3=components(
  ('State',2,{'C':2},'State the enquiry aim and a measurable objective for school access','A1'),
  ('Describe',4,{'C':4},'Apply random selection from the supplied complete school list','A1'),
  ('Explain',3,{'C':3},'Justify one collection method by its fit to this enquiry’s question and participants','A1'),
  ('Design',5,{'C':5},'Design an interview schedule that produces the specified attendance data','A1'),
  ('Calculate',2,{'B':2},'Convert a stated share into an angle, with clear units','A1'),
  ('Draw',4,{'C':4},'Construct a pie chart whose categories sum to the given total','A1'),
  ('Describe',4,{'B':4},'Interpret the education-access pattern, including one comparison supported by figures','A1'),
  ('Identify',1,{'B':1},'Identify an exception to that pattern from the data','A1'),
  ('State',2,{'D':2},'Two achievable aims for a small school-book access project','A2'),
  ('Describe',3,{'D':3},'Organise collection, distribution and record-keeping with responsible actors','A2'),
  ('Suggest',2,{'D':2},'Feasible funding or in-kind support using stated community resources','A2'),
  ('Explain',3,{'D':3},'Link a stated implementation problem to an appropriate response','A2'))
 A4=components(
  ('Define',1,{'C':1},'Define a research term needed in the supplied waste enquiry','A1'),
  ('Describe',4,{'C':4},'Collect and record observable waste categories using a stated sampling frame','A1'),
  ('Name and describe',4,{'C':4},'Apply two data collection methods to different information needs','A1'),
  ('Explain',3,{'C':3},'Explain one selection decision and why a named bias remains possible','A1'),
  ('Suggest',3,{'D':3},'Respond to the supplied safety/access difficulty by changing the procedure appropriately','A1'),
  ('Draw',4,{'C':4},'Construct a simple sketch map with the specified locations and key','A1'),
  ('Describe',3,{'B':3},'Read the spatial pattern using map evidence','A1'),
  ('Calculate',2,{'B':2},'Calculate an absolute difference between the two supplied collection periods','A1'),
  ('Identify',1,{'B':1},'Identify the observation that challenges the proposed explanation','A1'),
  ('Describe',3,{'B':3},'Interpret a second short waste-service stimulus','A2'),
  ('Explain',3,{'B':3},'Compare two proposals against the stated evidence and criterion','A2'),
  ('Suggest',4,{'D':4},'Propose a feasible action plan, obstacle response and implementer using the supplied resources','A2'))
 B1=components(
  ('State',2,{'C':2},'State the actual topic/area and linked aim','B'),
  ('Explain',2,{'C':2},'Explain what the pilot revealed and the revision actually made','B'),
  ('Describe',4,{'C':4},'Describe the collection procedure actually used','B'),
  ('Describe',4,{'B':4},'Support the enquiry findings with evidence and explain their implication','B'),
  ('Suggest',3,{'D':3},'A feasible recommendation with an implementer tied to those findings','B'))
 B2=components(
  ('Explain',2,{'C':2},'Two factors that informed selection of the research issue','B'),
  ('Describe',4,{'C':4},'Explain the actual sampling procedure and its fit to the population','B'),
  ('Describe',6,{'B':6},'An evidence-linked report of findings with valid conclusions and stated limits','B'),
  ('Suggest',3,{'D':3},'A matched response to a practical difficulty encountered by the researcher','B'))
 B3=components(
  ('State',2,{'C':2},'State the research question/hypothesis and one linked objective','B'),
  ('Explain',3,{'C':3},'Justify the presentation method actually used','B'),
  ('Describe',4,{'B':4},'Compare the relevant findings using actual evidence','B'),
  ('Outline',3,{'B':3},'Conclusions answering the research question within its limits','B'),
  ('Suggest',3,{'D':3},'A practical recommendation and responsible implementer','B'))
 B4=components(
  ('Describe',4,{'C':4},'Advantages and disadvantages of doing this enquiry locally','B'),
  ('Explain',2,{'C':2},'Explain a real pilot adjustment','B'),
  ('Describe',6,{'B':6},'Findings, evidence, implications and a supported conclusion in a report','B'),
  ('Suggest',3,{'D':3},'Resolve a researcher obstacle rather than merely restating the community issue','B'))
 plans['10.1']=[]
 for i,(title,a,b) in enumerate(zip(['Water access: instrument and community storage','Rural production: stratification and second dataset','Education access: representation and community book project','Community waste: sketch map, counterevidence and local enquiry'],[A1,A2,A3,A4],[B1,B2,B3,B4]),1):
  assert sum(p['mark_tariff'] for p in a)==35,(i,sum(p['mark_tariff'] for p in a))
  assert sum(p['mark_tariff'] for p in b)==15
  # A complete cycle is one 50-mark multipart package. Unique truthful task
  # kinds also avoid the stock perf_split(kind) ambiguity for repeated kinds
  # with different section allocations. No fake item types or label padding.
  kind=['practical_task','data_response','case_analysis','source_analysis'][i-1]
  plans['10.1'].append({'item_type':kind,'title':title+' — supplied enquiry and own-investigation transfer',
                       'cycle':i,'parts':a+b,'section_totals':{'A':35,'B':15}})
 return plans
