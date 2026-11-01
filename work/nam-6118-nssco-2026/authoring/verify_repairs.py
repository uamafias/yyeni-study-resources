"""Targeted repair checks, without treating the business chart rules as Physics validation."""
from pathlib import Path
import json,math,re,hashlib,collections,datetime
W=Path(__file__).resolve().parents[1]
def read(p):return json.loads((W/p).read_text())
def put(p,x):(W/p).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
# Independently entered expected values from dimensional derivation, not copied from answer keys.
expected={1:(1.6,'s per oscillation'),2:(.08,'°C/s'),3:(3,'cm/s'),4:(1.4,'s per oscillation'),5:(.2,'m/s²'),6:(12,'mm/N'),7:(.8,'g/cm³'),8:(.5,'N⁻¹ m⁻¹'),9:(.8,'°C/min'),10:(3,'J/s or W'),11:(10000,'Pa/m'),12:(.6,'mm/°C'),13:(.7,'mm/°C'),14:(800,'J/K'),15:(-.08,'°C/s'),16:(20,'cm/s'),17:(1,'no unit'),18:(1.5,'no unit'),20:(170,'m/s'),22:(1.45,'V per cell'),23:(12,'V/A or Ω'),24:(5,'J/s or W'),25:(2,'N/A'),26:(.05,'V per turn')}
practical=[];assets=[];keys={};allitems=[];figs={};standard=[]
for t in range(1,29):
 items=read(f'topics/{t}/learning-items/topic_{t}_items.json')['items'];allitems+=items
 q=read(f'topics/{t}/qa_report.json');assert not [c for c in q['deterministic_checks'] if c['status']=='fail'],t
 standard += [dict(topic=t,**c) for c in q['deterministic_checks'] if c['check_id'] in ['C-35','C-41']]
 for i in items:
  assert i['qa_status']=='review_required'
  if i['item_type']=='multiple_choice_set':
   seq=''.join(re.findall(r'\d+\. Key ([ABCD])\.',i['canonical_answer']));assert len(seq)==12
   assert collections.Counter(seq)==dict(A=3,B=3,C=3,D=3)
   assert all(seq!=seq[:p]*(12//p) for p in [1,2,3,4,6]);keys[t]=seq
  if i['item_type']=='flashcard':
   assert not re.match(r'^(Link\b|Combine\b|Draw\b|Place\b|Put\b|Use\b|Name\b|Find\b|Connect\b|Change\b|Measure\b|Record\b|Check\b|Keep\b|Minimise\b|Take\b|Add\b|Show\b|Label\b|Plot\b|Set\b|Align\b|Subtract\b|Divide\b|Read\b|Compare\b|Wind\b|Observe\b|Rub\b)',i['canonical_answer']),i['item_id']
   assert not any(s.startswith(('Method step:','Property or unit:','Combine the linked ideas')) for s in i['marking_guidance'])
 if t in expected:
  p=read(f'topics/{t}/assets/practical-parameters.json');d=p['data'];rows=d['rows'];x0,y0=rows[0];x1,y1=rows[-1];slope=(y1-y0)/(x1-x0)
  assert math.isclose(slope,expected[t][0],abs_tol=1e-9),(t,slope)
  assert p['gradient_unit']==expected[t][1],(t,p['gradient_unit'])
  assert p['construction']==[rows[0],rows[-1]]
  it=next(i for i in items if i['item_type']=='practical_task' and i['mark_tariff']==16)
  assert p.get('plot_y_heading',d['y_heading'])+' vertically against '+d['x_heading']+' horizontally' in it['prompt']
  assert p['gradient_meaning'] in it['canonical_answer']
  assert p['arrangement'] in it['canonical_answer']
  assert len(it['marking_guidance'])==8
  practical.append(dict(topic=t,horizontal=d['x_heading'],vertical=d['y_heading'],coordinates=[rows[0],rows[-1]],delta_y=y1-y0,delta_x=x1-x0,gradient=slope,unit=p['gradient_unit'],interpretation=p['gradient_meaning'],rubric_allocation='5 graph + 3 gradient + 8 plan (1 arrangement + 3 measurement + 2 control/precaution + 1 table + 1 conclusion)'))
 pp=W/f'topics/{t}/assets/figure-parameters.json'
 if pp.exists():
  fs=json.loads(pp.read_text())['figures'];figs[t]=fs
  def validate(v):
   if v.get('kind','graph')=='graph':
    assert v.get('xlabel') and v.get('ylabel')
    for y in v['ys'].values():assert len(y)==len(v['x']) and all(math.isfinite(a) for a in y)
   elif v.get('panels'):
    for p in v['panels']:validate(p)
   elif v.get('kind')=='geometry':
    for s in v['segments']:assert len(s['points'])>=2 and all(math.isfinite(z) for xy in s['points'] for z in xy)
   elif v.get('kind')=='vectors':assert all(m>0 for m,a in v['components'])
  for k,v in fs.items():validate(v)
 for p in sorted((W/f'topics/{t}/assets').glob('*.png')):
  assets.append(dict(path=str(p.relative_to(W)),sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
assert len(set(keys.values()))==26,'MC sequences must differ between topics'
assert math.isclose(1/expected[8][0],2) and math.isclose(expected[14][0]/.2,4000) and math.isclose(expected[16][0]/100,.2) and math.isclose(2*expected[20][0],340)
for t in [18,23,25,26]:
 aa=[a['sha256'] for a in assets if a['path'].startswith(f'topics/{t}/') and '/figure-' in a['path']];assert len(aa)==len(set(aa)),('duplicate figures',t)
# Numeric definitions of the repaired lens/waveform/diode figures.
di=figs[23]['OBJ-6118-5.2.4-06-M03'];xx=di['x'];yy=di['ys']['Diode'];assert max(abs(i) for x,i in zip(xx,yy) if x<.5)<.00003
assert yy[-1]>.5 and yy[-1]>1000*abs(yy[0])
for ob,peak,period in [('OBJ-6118-5.7.2.2-02-M01',2,1),('OBJ-6118-5.7.2.2-02-M02',4,.5)]:
 v=figs[26][ob];y=next(iter(v['ys'].values()));assert math.isclose(max(y),peak,abs_tol=1e-9);assert all(abs(y[j]-peak*math.sin(2*math.pi*x/period))<1e-9 for j,x in enumerate(v['x']))
# Long matching source wording is checked against existing transcribed syllabus quotations.
def tokens(s):return re.findall(r"[a-z0-9]+(?:['’][a-z]+)?",s.lower())
def quotes(o):
 if isinstance(o,dict):
  for k,v in o.items():
   if k=='verbatim' and isinstance(v,str):yield v
   else:yield from quotes(v)
 elif isinstance(o,list):
  for v in o:yield from quotes(v)
sh=set()
for s in quotes(read('curriculum/syllabus-facts.json')):
 tok=tokens(s);sh.update(tuple(tok[j:j+12]) for j in range(len(tok)-11))
hits=[]
for i in allitems:
 tok=tokens(i['canonical_answer']);matches=[' '.join(tok[j:j+12]) for j in range(len(tok)-11) if tuple(tok[j:j+12]) in sh]
 if matches:hits.append(dict(item=i['item_id'],matches=matches))
assert not hits,hits
baseline=read('review/claude-step6/pre-repair-baseline.json');baselineids={i['item_id'] for b in baseline.values() for i in b['items']};ids={i['item_id'] for i in allitems};assert len(ids)==len(allitems) and baselineids<=ids
for t in [9,23,25,26,27,28]:
 learner=' '.join(b['text'] for p in (W/f'topics/{t}/content-units').glob('*.json') for b in json.loads(p.read_text())['blocks'])
 assert not re.search(r'\b(?:inverters?|controllers?|conductance|antineutrino|domains|remanence|laminations|ECB|Ruacana|phonons|resolution)\b',learner,re.I),t
result=dict(status='pass',checked_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),scope='Author repair validation; not an independent review or official-mark-scheme verification',items=len(allitems),baseline_ids_preserved=len(baselineids),supplemental_items=sorted(ids-baselineids),practical_derivations=practical,mc_keys=keys,figures=assets,automated_figure_checks=['Finite and coherent declared data','Distinct figure hashes within each affected topic','Correct diode low-current region and knee','Generator amplitudes and periods','All 24 practical slopes and units independently entered above','Prompt axis order, explicit wide two-point construction, named equipment and marking allocation','All baseline identities retained','No flashcard instruction openings from the reported authoring vocabulary','No 12-word answer match to transcribed syllabus quotations'],shared_chart_checks=standard,source_wording=dict(syllabus_12_word_answer_matches=hits,scope='Canonical answers, including performance feedback; excludes headings and curriculum/source quotations. No claim of full-publisher-corpus plagiarism review.'),remaining=['Claude re-check of repaired content; final Step 6 decision not issued.','Teacher subject review is still recommended.','267 exam-demand marking-evidence gaps remain; no new official marking schemes were acquired.','Independent demand mappings and First Proof equivalence remain unresolved.'])
put('review/claude-step6/repair-validation.json',result)
print(json.dumps(dict(status=result['status'],items=len(allitems),baseline_ids_preserved=len(baselineids),supplementals=len(ids-baselineids),practicals=len(practical),figures=len(assets),mc_sets=len(keys)),indent=2))
