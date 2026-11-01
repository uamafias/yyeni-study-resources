"""Structure explicitly authored content, retaining the approved slot identities.
This module supplies metadata/rendering, never physics prose or fallback answers.
"""
from pathlib import Path
import json,hashlib,sys,subprocess,copy,random,re
W=Path(__file__).resolve().parents[1];ROOT=W.parents[1]
def j(p):return json.loads((W/p).read_text())
def put(p,d):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
def oid(key):return key if key.startswith('OBJ-') else 'OBJ-6118-'+key
class Author:
 def __init__(self,topic):
  self.t=str(topic);self.wo=j(f'topics/{self.t}/work_order.json');self.contract=j(f'topics/{self.t}/contract.json');self.data={};self.mc=[];self.structured=[];self.practical=None;self.extra_blocks=[];self.deviations=[];self.figures={};self.miscons={}
 def add(self,key,core,detail,teach,prompt,answer,guidance=None,heading=None):
  key=oid(key);assert key not in self.data,key
  self.data[key]=dict(core=core,detail=detail,teach=teach,prompt=prompt,answer=answer,guidance=guidance,heading=heading)
 def misconception(self,entry_id,core,detail,teach,prompt,answer,guidance=None):
  self.miscons[entry_id]=dict(core=core,detail=detail,teach=teach,prompt=prompt,answer=answer,guidance=guidance)
 def plot(self,key,x,ys,xlabel,ylabel,title='',line=True,**kwargs):
  self.figures[oid(key)]=dict(x=x,ys=ys,xlabel=xlabel,ylabel=ylabel,title=title,line=line,**kwargs)
 def vector(self,key,components,unit='N',title='Vector addition'):
  self.figures[oid(key)]=dict(kind='vectors',components=components,unit=unit,title=title)
 def geometry(self,key,segments,circles=None,labels=None,title='Original construction'):
  self.figures[oid(key)]=dict(kind='geometry',segments=segments,circles=circles or [],labels=labels or [],title=title)
 def choice(self,key,prompt,correct,wrong1,wrong2,wrong3):
  # Every wrong alternative includes its own authored explanation.
  self.mc.append(dict(oid=oid(key),prompt=prompt,correct=correct,wrong=[wrong1,wrong2,wrong3]))
 def part(self,key,prompt,answer,marks,guidance):self.structured.append(dict(oid=oid(key),prompt=prompt,answer=answer,marks=marks,guidance=guidance))
 def build(self):
  from repairs import repair
  repair(self)
  baseline=j('review/claude-step6/first-repair-baseline.json')[self.t]
  oldclaims={c['claim_id']:c for c in baseline['claims']};revisions={}
  slots=self.wo['item_slots'];required={s['objective_id'] for s in slots};assert set(self.data)==required,(self.t,'missing',required-set(self.data),'extra',set(self.data)-required)
  td=W/'topics'/self.t;claims=[];cids={};blocks={u['unit_id']:[] for u in self.wo['content_units']}
  memberunit={o:u['unit_id'] for u in self.wo['content_units'] for o in u['objective_ids']}
  reg={o['objective_id']:o for o in j('curriculum/objective_registry.json')['objectives']}
  def claim(ob,text,typ='factual'):
   cid=f'CLM-6118-{self.t}-{len(claims)+1:03}';old=oldclaims.get(cid);revision=(old['revision']+(old['text']!=text or old['objective_ids']!=[ob])) if old else 1;revisions[cid]=revision;claims.append(dict(claim_id=cid,objective_ids=[ob],text=text,claim_type=typ,provenance='generated_gap',evidence=[],derived_from_claim_ids=[],revision=revision,verification=dict(status='unverified',method='Original authoring from the approved syllabus scope; awaiting Lotto/Claude semantic review.',reviewer_id=None,reviewed_at=None,confidence=0.9),publishable=False,notes=[]));return cid
  def block(unit,typ,heading,text,refs,aos,scope=None):
   b=dict(block_id=f'{unit}-B{len(blocks[unit])+1:03}',block_type=typ,heading=heading,text=text,claim_ids=refs,context_tags=[],assessment_objectives=aos,claims_seen={c:revisions[c] for c in refs});b['authored_hash']=hashlib.sha256((heading+'|'+text).encode()).hexdigest()
   if scope:b['generalisation_scope']=scope
   blocks[unit].append(b)
  for ob,d in self.data.items():
   cids[ob]=[claim(ob,d['core'],'definition' if reg[ob]['objective_type']=='phys_definition' else 'factual'),claim(ob,d['detail'])]
   heading=d['heading'] or reg[ob]['learner_objective'].rstrip('.');text=d['core']+' '+d['detail']+'\n\n'+d['teach']
   block(memberunit[ob],'plain_explanation',heading,text,cids[ob],['C'] if self.t in ('2','3') else reg[ob]['assessment_objectives'],[ob] if reg[ob]['objective_type']=='phys_container' else None)
  misrefs={}
  for slot in slots:
   if slot['subtype']=='MISCON':
    mid=slot['misconception_entry'];assert mid in self.miscons,(self.t,mid);d=self.miscons[mid];ob=slot['objective_id']
    ref=claim(ob,d['core']+' '+d['detail'],'misconception_correction');misrefs[mid]=[ref]
    block(memberunit[ob],'misconception','Distinguishing the ideas',d['core']+' '+d['detail']+'\n\n'+d['teach'],[ref],slot['assessment_objectives'])
  figure_paths={}
  if self.figures:
   from figures import graph,vectors,geometry
   for n,(ob,spec) in enumerate(self.figures.items(),1):
    name=f'figure-6118-{self.t}-{n:02}';params=dict(spec);kind=params.pop('kind','graph');{'vectors':vectors,'graph':graph,'geometry':geometry}[kind](td/'assets',name,**params);figure_paths[ob]='assets/'+name+'.png'
    unit=memberunit[ob];caption=spec.get('title') or self.data[ob]['prompt'];block(unit,'example',caption,caption+'. '+self.data[ob]['prompt']+'\n\n!['+caption.replace(']','')+']('+figure_paths[ob]+')',cids[ob],['C'] if self.t in ('2','3') else ['B'])
   put(td/'assets/figure-parameters.json',dict(origin='Original authored practice parameters',figures=self.figures))
   self.deviations.append(dict(from_='No science-specific chart renderer in the shared standard',to='Original scientific plots generated from declared numerical parameters using Matplotlib.',why='The shared chart renderer models business break-even graphs. Physics plots require the actual physical axes; no source picture or hand-edited graph is used.'))
  miscon_paths={}
  if getattr(self,'miscon_figure_specs',None):
   from figures import comparison
   for iid,spec in self.miscon_figure_specs.items():
    name='misconception-'+iid.lower();comparison(td/'assets',name,**{k:v for k,v in spec.items() if k!='kind'});miscon_paths[iid]='assets/'+name+'.png'
  items=[]
  def make(slot,objs,refs,prompt,answer,guidance,kind='flashcard',sub=None,aos=None,cw=None,marks=None,bloom=None):
   i=dict(item_id=slot['slot'],objective_ids=objs,claim_ids=list(dict.fromkeys(refs)),item_type=kind,subtype=sub if kind!='flashcard' else slot['subtype'],assessment_objectives=aos or slot['assessment_objectives'],blooms_level=bloom or slot['blooms_level'],command_word=cw if kind!='flashcard' else slot['command_word'],mark_tariff=marks if kind!='flashcard' else slot['mark_tariff'],difficulty=slot.get('difficulty',3),prompt=prompt,canonical_answer=answer,marking_guidance=guidance,context=dict(sector=None,business_size=None,ownership=None,situation=None,facts=[]),prerequisite_item_ids=[],core_status='core',intentional_duplicate_group=None,provenance='Original NSSCO Physics authoring; proposed practice rubric based on entered task architecture, not copied official credit wording.',qa_status='review_required',claims_seen={c:revisions[c] for c in refs});i['authored_hash']=hashlib.sha256((prompt+'|'+answer+'|'+'|'.join(guidance)).encode()).hexdigest();items.append(i);return i
  for s in slots:
   d=self.miscons[s['misconception_entry']] if s['subtype']=='MISCON' else self.data[s['objective_id']]
   d=dict(d,**getattr(self,'slot_overrides',{}).get(s['slot'],{}));ans=d['answer'].replace('~',' ')
   if s['subtype']!='MISCON' and s['objective_id'] in figure_paths and (s['subtype']=='INTERP' or any(t in d['prompt'].lower() for t in ['diagram','graph'])):ans+='\n\n![Original graphical solution]('+figure_paths[s['objective_id']]+')'
   if s['slot'] in miscon_paths:ans+='\n\n![Comparison on the prompt axes]('+miscon_paths[s['slot']]+')'
   guidance=d['guidance']
   assert guidance,(self.t,s['slot'],'missing authored credit points')
   make(s,[s['objective_id']],misrefs[s['misconception_entry']] if s['subtype']=='MISCON' else cids[s['objective_id']],d['prompt'],ans,guidance)
  for sup in getattr(self,'supplementals',[]):
   ob=sup['objective_id'];ss=dict(slot=sup['item_id'],subtype=sup['subtype'],assessment_objectives=sup['assessment_objectives'],blooms_level=sup['blooms_level'],command_word=sup['command_word'],mark_tariff=sup['mark_tariff'],difficulty=3)
   make(ss,[ob],cids[ob],sup['prompt'],sup['answer'],sup['guidance'],kind=sup.get('item_type','flashcard'),aos=sup['assessment_objectives'],cw=sup['command_word'],marks=sup['mark_tariff'],bloom=sup['blooms_level'])
  # Explicitly authored MC set; no fabricated distractor boilerplate.
  for task in self.wo['performance_tasks']:
   kind=task['item_type']
   if kind=='multiple_choice_set':
    assert len(self.mc)==12,(self.t,'MC count',len(self.mc));prompts=[];answers=[];refs=[];objs=[]
    rng=random.Random('6118-repair-v2-'+self.t);positions=list('AAABBBCCCDDD')
    while True:
     rng.shuffle(positions);seq=''.join(positions)
     if all(seq!=seq[:p]*(12//p) for p in [1,2,3,4,6]) and not re.search(r'(.)\1\1',seq):break
    for k,q in enumerate(self.mc,1):
     assert q['oid'] in cids,(self.t,q['oid']);choices=[(v[0],v[1],False) for v in q['wrong']];rng.shuffle(choices);choices.insert(ord(positions[k-1])-65,(q['correct'][0],q['correct'][1],True))
     prompts.append(str(k)+'. '+q['prompt']+'\n'+'\n'.join(f'{chr(65+n)}. {c[0]}' for n,c in enumerate(choices)))
     key=next(chr(65+n) for n,c in enumerate(choices) if c[2]);answers.append(f'{k}. Key {key}. '+' '.join(f'{chr(65+n)}: {c[1]}' for n,c in enumerate(choices)));refs+=cids[q['oid']];objs.append(q['oid'])
    obj=list(dict.fromkeys(objs));self.deviations.append(dict(from_='MC set bound only to the two topic anchors',to='MC objective IDs identify the outcomes actually tested by its 12 original questions.',why='Accurate question-to-claim mapping gives wider topic practice without falsely assigning every question to two broad anchors.'))
    self.deviations.append(dict(from_='Alternate seven/eight A-focused MC questions in the handover estimate',to='Each set uses seven knowledge questions followed by five application questions; A/B remains a proposed practice estimate.',why='The original application scenarios are retained rather than relabelled as recall. This changes the internal estimate to 182 A / 130 B over 312 questions, without changing any approved item slot, tariff or declared A/B set label.'))
    make(task,obj,refs,'Choose one correct option for each original practice question.\n\n'+'\n\n'.join(prompts),'\n\n'.join(answers),['Key: one mark for the correct option in each question, for 12 marks total.','Distractor feedback: the canonical answer explains the quantity, mechanism or calculation error behind every wrong option.'],kind=kind,aos=task['assessment_objectives'],cw=None,marks=12)
   elif kind=='short_answer':
    assert len(self.structured)==5 and sum(p['marks'] for p in self.structured)==8,(self.t,'structured parts')
    refs=[];objs=[];pp=[];aa=[];gg=[]
    for n,p in enumerate(self.structured):
     assert p['oid'] in cids,(self.t,p['oid']);refs+=cids[p['oid']];objs.append(p['oid']);label=chr(97+n);pp.append(f'({label}) {p["prompt"]} [{p["marks"]}]');aa.append(f'({label}) {p["answer"]}');gg.append(f'({label}) '+p['guidance'])
    make(task,list(dict.fromkeys(objs)),refs,'Original structured practice. Answer the parts with working and units where needed.\n\n'+'\n\n'.join(pp),'\n\n'.join(aa),gg+['Eight marks total; use the definition, reason or working requested by each part.'],kind=kind,aos=task['assessment_objectives'],cw=task['command_word'],marks=8)
    self.deviations.append(dict(from_='Structured task bound to the two broad source anchors',to='Part-specific objective IDs match the five authored demands.',why='The original structured task tests the indicated topic outcomes; its eight-mark total and A/B practice roles remain as planned.'))
   elif kind=='practical_task':
    assert self.practical is not None,(self.t,'missing practical');pr=self.practical;spec=next(s for s in j('curriculum/topic-task-specifications.json')['specifications'] if s['topic_id']==self.t);data=pr.get('data',spec['practical_data']);assert data
    table='| '+data['x_heading']+' | '+data['y_heading']+' |\n|---:|---:|\n'+'\n'.join(f'| {x:g} | {y:g} |' for x,y in data['rows'])
    comparison=pr.get('comparison_data');axis_y=pr.get('plot_y_heading',data['y_heading']);point_count=len(data['rows'])*(2 if comparison else 1)
    if comparison:
     assert [r[0] for r in comparison['rows']]==[r[0] for r in data['rows']]
     table='| '+data['x_heading']+' | '+data['y_heading']+' | '+comparison['y_heading']+' |\n|---:|---:|---:|\n'+'\n'.join(f'| {x:g} | {y:g} | {other[1]:g} |' for (x,y),other in zip(data['rows'],comparison['rows']))
    lo=data['rows'][0];hi=data['rows'][-1];dy=hi[1]-lo[1];dx=hi[0]-lo[0];slope=dy/dx;assert abs(slope-data['expected_gradient'])<1e-7
    response='Graph: '+pr['graph']+'\n\nGradient construction: choose the separated fitted-line points '+f'({lo[0]:g}, {lo[1]:g}) and ({hi[0]:g}, {hi[1]:g}). '+'Gradient = '+f'({hi[1]:g} − {lo[1]:g}) / ({hi[0]:g} − {lo[0]:g}) = {slope:g} '+pr['unit']+'. '+pr['meaning']+'\n\nArrangement: '+pr['arrangement']+'\n\nPlan: '+' '.join(f'{k+1}. {v}' for k,v in enumerate(pr['method']))+'\nControl and accuracy: '+pr['control']+'\nTable: '+pr['table']+'\nGraph and conclusion: '+pr['conclusion']
    from figures import graph
    pname=f'practical-6118-{self.t}'
    series={pr.get('plot_label','Idealised readings'):[p[1] for p in data['rows']]}
    if comparison:series[comparison['label']]=[p[1] for p in comparison['rows']]
    graph(td/'assets',pname,[p[0] for p in data['rows']],series,data['x_heading'],axis_y,('Black and shiny can temperatures' if comparison else axis_y.split(' / ')[0])+' against '+data['x_heading'].split(' / ')[0].lower(),fit=True,triangle=True,origin=not bool(comparison))
    put(td/'assets/practical-parameters.json',dict(origin='Original practice stimulus; reviewed axis/unit derivation',data=data,gradient=slope,gradient_unit=pr['unit'],gradient_meaning=pr['meaning'],construction=[lo,hi],aim=pr['aim'],arrangement=pr['arrangement'],plot_y_heading=axis_y,comparison_data=comparison))
    response+='\n\n![Original fitted practice graph](assets/'+pname+'.png)'
    dimless=self.t in ('17','18')
    pp='Investigation aim: '+pr['aim']+'. These are invented, idealised practice readings; real readings have scatter. '+pr.get('stimulus_note','')+'\n\n'+table+'\n\n(a) Draw '+axis_y+' vertically against '+data['x_heading']+' horizontally. '+('Plot both labelled cans and fit a separate line to each. ' if comparison else 'Plot the supplied readings and add a separate fitted line. ')+'[5]\n(b) Show two widely separated points on your fitted line and calculate '+('the black-can gradient. ' if comparison else 'its gradient. ')+('Explain why this ratio has no unit.' if dimless else 'State the gradient unit.')+' [3]\n(c) Plan how to '+pr['aim'].removeprefix('Investigate ').removeprefix('investigate ')+'. Name the equipment and arrangement, describe the measurements and repeats, state controls and a relevant precaution, design the results table and explain how the results answer the aim. [8]'
    obs=list(dict.fromkeys(task['objective_ids']+[oid(k) for k in pr.get('additional_objective_keys',[])]));assert all(o in cids for o in obs),(self.t,'practical anchors',obs);refs=[c for o in obs for c in cids[o]]
    if pr.get('additional_objective_keys'):
     self.deviations.append(dict(from_='Practical task limited to its two planned anchors',to='Additional explicitly practised representation objectives are cited.',why='The actual graph/table construction meaningfully practises these outcomes as well; the slot and mark allocation are unchanged.'))
    # Practice-method detail is a separately taught claim, not an unmentioned answer fact.
    for ob in obs:
     refs.append(claim(ob,pr['meaning']+' '+pr['control'],'procedural'))
    make(task,obs,refs,pp,response,['(a) Correct quantities and units on both axes (1); regular usable scales (1); points within half a small square, '+('all twelve (2) or ten/eleven (1); both series labelled with separate suitable fitted lines (1).' if comparison else 'all six (2) or four/five (1); a separate suitable fitted line (1).'),
     '(b) A visible wide triangle or two stated separated line coordinates (1); difference in vertical coordinates divided by difference in horizontal coordinates, with correct sign and result (1); '+('states no unit because both axis quantities form a dimensionless ratio (1).' if dimless else 'unit '+pr['unit']+' or a stated equivalent derived from vertical unit / horizontal unit (1).'),
     '(c) Equipment/arrangement (1): '+pr['arrangement'],
     '(c) Measurements (3): '+pr['measurement_credit'],
     '(c) Controls/precaution (2): one mark for a named variable AND how it is kept fixed; one for another specific control or a relevant precaution with its action. '+pr['control'],
     '(c) Table (1): '+pr['table'],
     '(c) Analysis/conclusion (1): '+pr['conclusion'],
     'Accept a physically equivalent operational method using suitable named equipment. Do not award a second graph-construction mark in (c). For later calculations, allow error carried forward from a plausible measured gradient when the subsequent relation is correct; do not reward a reversed axis interpretation. Proposed teaching rubric, not a reconstructed official mark scheme.'],kind=kind,aos=['C'],cw='Draw',marks=16)
  from card_repairs import rubric_policy
  for it in items:
   if it['item_type']=='flashcard':
    it['marking_guidance'].append(rubric_policy(it['subtype']))
    it['authored_hash']=hashlib.sha256((it['prompt']+'|'+it['canonical_answer']+'|'+'|'.join(it['marking_guidance'])).encode()).hexdigest()
  # Every part of every performance solution is also available in offline notes.
  for it in items:
   if it['item_type']!='flashcard':
    refs=it['claim_ids'];unit=memberunit[it['objective_ids'][0]];block(unit,'worked_application','Practice task with worked feedback',it['prompt']+'\n\nWorked feedback\n\n'+it['canonical_answer'],refs,it['assessment_objectives'])
  for ob,heading,text in self.extra_blocks:
   block(memberunit[ob],'worked_application',heading,text,cids[ob],['C'] if self.t in ('2','3') else ['A','B'])
  units=[]
  for u in self.wo['content_units']:
   unit=u['unit_id']
   count=sum(len(b['text'].split()) for b in blocks[unit]);bud=u['word_budget'];units.append(dict(unit_id=unit,title=self.contract['topic_title']+' — '+u['sub_topic'],objective_ids=u['objective_ids'],level='NSSCO',core_status='core',objective_type='physics_teaching',depth_tier=2,word_budget=dict(min=bud[0],target=(bud[0]+bud[1])//2,max=bud[1]),blocks=blocks[unit],word_count=count,qa_status='review_required'))
  assert len(items)==self.wo['planned_item_count']+len(getattr(self,'supplementals',[]))
  self.contract['depth_constraints']['item_budget']=len(items);self.contract['required_outputs']['learning_items']=len(items);put(td/'contract.json',self.contract)
  put(td/'claims/canonical_claim_ledger.json',dict(ledger_id='CLM-LEDGER-6118-'+self.t,claims=claims))
  for u in units:put(td/'content-units'/(u['unit_id']+'.json'),u)
  put(td/'learning-items'/f'topic_{self.t}_items.json',dict(dataset_id='ITEMS-6118-'+self.t,topic_id=self.t,items=items))
  dev=[dict({'from':x.pop('from_')} if 'from_' in x else {},**x) for x in copy.deepcopy(self.deviations)]
  put(td/'authoring_notes.json',dict(topic_id=self.t,author='Codex',deviations=dev,judgements=['New scenarios, numerical values, explanations and proposed practice rubrics are authored judgements. No official stem or marking text is reproduced.','Claims remain unverified and non-publishable pending the separate human/Claude review.']))
  subprocess.run([sys.executable,str(ROOT/'standard/v0.2.0-draft/build/render_notes.py'),str(W),self.t],check=True,capture_output=True,text=True)
  proc=subprocess.run([sys.executable,str(ROOT/'standard/v0.2.0-draft/checks/run_checks.py'),str(W),self.t,'--quiet'],capture_output=True,text=True)
  qa=j(f'topics/{self.t}/qa_report.json');bad=[x for x in qa['deterministic_checks'] if x['status']=='fail'];print(self.t,self.contract['topic_title'],len(claims),'claims',len(units),'units',len(items),'items',sum(u['word_count'] for u in units),'words',qa['release_decision']);print([(b['check_id'],b['message'],b['affected_ids'][:8]) for b in bad])
  return qa
