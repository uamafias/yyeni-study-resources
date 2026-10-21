"""Cross-passage numerical and task/guidance regression checks for F1–F5."""
import json,re,sys,math
from pathlib import Path
OUT=Path(__file__).resolve().parent;WS=OUT.parents[2]
def read(p):return json.loads(p.read_text())
def block(t,u,n):return next(b for b in read(WS/'topics'/t/'content-units'/f'CU-6136-{t}.{u:02d}.json')['blocks'] if b['block_id'].endswith('-'+str(n).zfill(2)))
def item(t,n):return next(i for i in read(WS/'topics'/t/'learning-items'/f'topic_{t}_items.json')['items'] if i['item_id'].split('-')[3]==str(n).zfill(3))
def numbers(p,s):return [float(x) for x in re.search(p,s).groups()]
checks={}
def check(n,value):checks[n]=bool(value);assert value,n
def pyramid_ok(overview,construction):
 cpart,dpart=construction.split('C,',1)[1].split('; D,',1)
 c=[float(n) for n in re.findall(r'(?:male|female) (\d+(?:\.\d+)?)%',cpart)]
 d=[float(n) for n in re.findall(r'(?:male|female) (\d+(?:\.\d+)?)%',dpart.split('Each population',1)[0])]
 if len(c)!=6 or len(d)!=6:return False
 cy,cw,co=numbers(r'Population C has (\d+)% aged 0–14, (\d+)% aged 15–64 and (\d+)% aged 65',overview)
 dy,dw,do=numbers(r'Population D has (\d+)%, (\d+)% and (\d+)%',overview)
 cb=numbers(r'C’s bar lengths on each side are (\d+)%, (\d+)% and (\d+)%',construction)
 db=numbers(r'D’s are (\d+)%, (\d+)% and (\d+)%',construction)
 return sum(c)==sum(d)==100 and [sum(c[j:j+2]) for j in [0,2,4]]==[cy,cw,co] and [sum(d[j:j+2]) for j in [0,2,4]]==[dy,dw,do] and c[::2]==c[1::2]==cb and d[::2]==d[1::2]==db
overview=block('7.1',6,4)['text'];construction=block('7.1',6,5)['text']
check('pyramid_overview_table_and_bars_agree',pyramid_ok(overview,construction))
check('negative_wrong_pyramid_bar_rejected',not pyramid_ok(overview,construction.replace('C’s bar lengths on each side are 18%','C’s bar lengths on each side are 20%')))
check('negative_wrong_age_share_rejected',not pyramid_ok(overview.replace('C has 36%','C has 45%'),construction))
s=block('10.1',10,6)['text']
n,k,interval=numbers(r'list of (\d+) households and a sample of (\d+) gives interval \d+ ÷ \d+ = (\d+)',s)
start,=numbers(r'starting position of (\d+)',s)
selection=[int(x) for x in re.search(r'produces (.+?)\.',s).group(1).replace('and',',').replace(' ','').split(',') if x]
check('sampling_example_recomputed',n/k==interval and selection==list(range(int(start),int(n)+1,int(interval))) and len(selection)==k)
a,b,sample,aa,bb=numbers(r'villages of (\d+) and (\d+) households, a proportional sample of (\d+) allocates (\d+) and (\d+)',s)
check('stratification_example_recomputed',[a/(a+b)*sample,b/(a+b)*sample]==[aa,bb])
s=block('10.1',11,6)['text']
total,a,b,c=numbers(r'(\d+) journeys comprise (\d+) walking, (\d+) cycling and (\d+) using a bus',s)
angles=numbers(r'angles are (\d+)°, (\d+)° and (\d+)°',s)
check('pie_example_recomputed',a+b+c==total and all(math.isclose(v/total*360,angle) for v,angle in zip([a,b,c],angles)) and sum(angles)==360)
sa,sb,sc,length=numbers(r'shares of (\d+)%, (\d+)% and (\d+)%, a (\d+) cm',s)
lengths=numbers(r'sections (\d+(?:\.\d+)?), (\d+(?:\.\d+)?) and (\d+(?:\.\d+)?) cm',s)
boundaries=numbers(r'boundaries at (\d+(?:\.\d+)?) and (\d+(?:\.\d+)?) cm',s)
check('rectangle_example_recomputed',sa+sb+sc==100 and [v/100*length for v in [sa,sb,sc]]==lengths and sum(lengths)==length and [lengths[0],sum(lengths[:2])]==boundaries)
check('research_worked_datasets_distinct_from_assessments',(total,a,b,c)!=(12,6,3,3) and lengths!=[8,7,5] and 'north–south road' in s and 'west–east road' not in s)
check('practice_answer_sentence_removed','For separate practice' not in block('3.1',10,5)['text'])
horizon=item('2.2',3)
check('planning_horizons_compared',all(x in horizon['prompt'].lower() for x in ['short-term','long-term','differentiate']) and 'pillar' not in horizon['prompt'])
task=item('2.2','P02')
check('b_only_task_requires_interpretation',task['assessment_objectives']==['B'] and all(x in task['prompt'] for x in ['all 4','target of 20','only 2 function']) and 'merely naming or defining a pillar earns no interpretation credit' in ' '.join(task['marking_guidance']))
research=item('10.1','P02');stem=research['prompt'].split('A1(1)',1)[0];part2=re.search(r'A1\(2\)(.+?)\[4\]',research['prompt']).group(1)
check('method_name_not_given_in_stem_or_next_question','interview' not in (stem+part2).lower() and 'spoken answers' in stem and 'price answers' in part2)
check('spoiled_inside_output_fact_retained','these totals include spoiled bags' in stem)
generic=[];duplicates=[];fullanswers=[]
for p in (WS/'topics').glob('*/learning-items/topic_*_items.json'):
 for i in read(p)['items']:
  gs=i['marking_guidance'];g=' '.join(gs)
  if re.search(r'identify the stated mechanism|connect the two supplied conditions|use both resource/implementation facts|connect both supplied conditions|develop the supplied barrier',g):generic.append(i['item_id'])
  if i['item_id'].endswith('-P01') and sum(x.startswith('Development (b)') for x in gs)>1:duplicates.append(i['item_id'])
  if i['item_type']=='flashcard' and i['subtype']!='DEF' and i['mark_tariff']>1 and len(i['canonical_answer'])>40 and i['canonical_answer'] in g:fullanswers.append(i['item_id'])
check('generic_guidance_family_removed',not generic)
check('duplicate_p01_criteria_removed',not duplicates)
check('non_definition_multimark_guidance_not_full_answer_copy',not fullanswers)
preserved=0;intentional=[]
for p in (OUT/'baseline/topics').glob('*/content-units/*.json'):
 current=read(WS/p.relative_to(OUT/'baseline'))
 byid={b['block_id']:b for b in current['blocks']}
 for old in read(p)['blocks']:
  if '\n\nApplied example:' not in old['text']:continue
  oldp=old['text'].split('\n\nApplied example:',1)[0];newp=byid[old['block_id']]['text']
  if oldp in newp:preserved+=1
  else:intentional.append(old['block_id'])
check('restored_teaching_retained_with_one_logged_numeric_change',preserved==65 and intentional==['BLK-6136-10.1.10-04'] and block('10.1',10,4)['text'].startswith('Systematic sampling selects at a fixed interval'))
sys.path.insert(0,str(WS/'topics'))
from audit_research import audit
rows,numeric=audit(write_report=False)
check('existing_research_and_card_numerics_pass',all(numeric.values()))
result={'date':'2026-10-21','checks':checks,'numeric_checks':len(numeric),'negative_cases':2,'full_answer_copies':fullanswers,'generic_guides':generic,'preserved_original_paragraphs':preserved,'intentional_numeric_revision':intentional,'independent_approval':False}
dump=OUT/'targeted-validation.json';dump.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'targeted_checks':len(checks),'numerical_checks':len(numeric),'negative_cases':2}))
