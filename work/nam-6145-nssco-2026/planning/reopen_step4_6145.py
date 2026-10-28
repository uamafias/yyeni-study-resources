"""Generate revision-01 candidate inputs/orders, preserving reviewed IDs and live content.
Shared generators decide slots/counts/labels. This wrapper supplies explicit planner
judgements and migrates generated IDs by objective/subtype/misconception identity.
Nothing under standard, live curriculum, production topics or publish is written.
"""
import collections,copy,hashlib,json,re,shutil,sys,tempfile
from pathlib import Path
import yaml,jsonschema
W=Path(__file__).resolve().parents[1]; ROOT=W.parents[1]; R=W/'planning/revision-01'; B=R/'baseline'; C=R/'candidate'
sys.path.insert(0,str(ROOT/'standard/v0.2.0-draft/build'))
import make_contract as mc,make_work_order as mw,conform_registry as cr
load=lambda p:json.loads(p.read_text())
def dump(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def rows(t):return sorted(t,key=lambda x:tuple(int(y)for y in x.split('.')))
# key, source parent, existing content-unit group, focused retrieval target, slot kind
ADDS=[
('industrial-action','2.2-06','2.2','Industrial action','DEF'),
('currency-issue','2.3-05','2.3.5','Why a central bank issues currency','WHY'),
('government-banker','2.3-05','2.3.5','Why government uses the central bank as its banker','WHY'),
('last-resort','2.3-05','2.3.5','Why a central bank acts as lender of last resort','WHY'),
('bank-supervision','2.3-05','2.3.5','Why banks are supervised','WHY'),
('repo-rate','2.3-05','2.3.5','Repo rate','DEF'),
('nsx-liquidity','2.3-05','2.3.5','Why secondary share trading supports liquidity','WHY'),
('nsx-capital','2.3-05','2.3.5','Why listing can help a company raise capital','WHY'),
('occupational-mobility','4.1-01','4.1','Occupational mobility of labour','DEF'),
('geographical-mobility','4.1-01','4.1','Geographical mobility of labour','DEF'),
('gross-pay','4.2-01','4.2','Gross pay','DEF'),
('net-pay','4.2-01','4.2','Net pay','DEF'),
('time-rate','4.2-01','4.2','Time-rate payment','DEF'),
('piece-rate','4.2-01','4.2','Piece-rate payment','DEF'),
('value-added','5.1-02','5.1','Value added','DEF'),
('external-economies','5.4-02','5.4.2','External economies of scale','DEF'),
('external-diseconomies','5.4-03','5.4.3','External diseconomies of scale','DEF'),
('merit-goods','6.1-01','6.1.1','Merit goods','DEF'),
('privatisation','6.1-01','6.1.1','Privatisation','DEF'),
('nationalisation','6.1-01','6.1.1','Nationalisation','DEF'),
('income-tax-example','6.2-04','6.2.4','Personal income tax as a direct tax example','FEATURE'),
('company-tax-example','6.2-04','6.2.4','Company tax as a direct tax example','FEATURE'),
('vat-example','6.2-04','6.2.4','VAT as an indirect tax example','FEATURE'),
('excise-example','6.2-04','6.2.4','Excise duty as an indirect tax example','FEATURE'),
('inflation','7.1-02','7.1','Inflation','DEF'),
('current-account','7.4-01','7.4','Current account of the balance of payments','DEF'),
('current-account-components','7.4-01','7.4','Components of the current account','FEATURE'),
('age-dependency','8.1-04','8.1','Age-dependency ratio','DEF'),
('hdi','8.2-01','8.2.1','Human Development Index','DEF'),
('tariff','9.1-01','9.1.1','Import tariff','DEF'),
('quota','9.1-01','9.1.1','Import quota','DEF'),
('embargo','9.1-01','9.1.1','Trade embargo','DEF'),
('producer-subsidy','9.1-01','9.1.1','Why a domestic producer subsidy can protect domestic production','WHY'),
]
# Existing member outcomes need an additional answer shape, not a duplicate objective.
EXTRA=[('total-revenue-definition','OBJ-6145-5.3.2-01','DEF','Total revenue'),('average-revenue-definition','OBJ-6145-5.3.2-02','DEF','Average revenue'),('ped-formula-meaning','OBJ-6145-3.3.3-01','WHY','Why PED compares percentage quantity-demanded and price changes'),('pes-formula-meaning','OBJ-6145-3.3.3-02','WHY','Why PES compares percentage quantity-supplied and price changes')]
VISUALS=[
('ppc','1.1-02','1.1','Production possibility curve','Axes and units; attainable frontier; feasible/inefficient/unattainable points; opportunity cost from a movement. Do not imply a straight line has increasing opportunity cost.'),
('ped-curves','3.3-01','3.3','Demand elasticity diagrams','Use common axes/scales and a stated reference point or explicit numerical elasticities. Steepness alone across different scales does not establish elasticity. No unqualified straight-line slope=elasticity rule.'),
('pes-curves','3.3-01','3.3','Supply elasticity diagrams','Construct two supply curves with specified differing responsiveness at a declared reference point. Label axes/units and verify elasticities from the data. A supply line through the origin is unit elastic; cover limiting cases in the notes without overcrowding the card.'),
('labour-market','4.2-01','4.2','Labour market equilibrium and demand shift','Wage vertical; labour quantity horizontal; solve initial/new equilibrium; shift only labour demand for the stated product-demand increase.'),
('lrac','5.4-04','5.4','Long-run average cost and scale','Average cost against output; economies, minimum/optimum region and diseconomies. Do not label total cost or short-run diminishing returns as LRAC economies.'),
('maximum-price','6.3-02','6.3','Binding maximum price','Ceiling below equilibrium; quantities demanded/supplied and shortage. The control alone does not shift either curve.'),
('minimum-price','6.3-02','6.3','Binding minimum price','Floor above equilibrium; quantities demanded/supplied and surplus. Distinguish offered output from actual sales.'),
('minimum-wage','6.3-04','6.3','Binding minimum wage in the competitive model','Wage above equilibrium; labour demanded and supplied and excess supply. State competitive-model/employment assumptions; no universal unemployment claim.'),
]
def key(s):return(s['objective_id'],s['subtype'],s.get('misconception_entry'))
def main():
 for p,h in load(B/'preservation-hashes.json').items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,'Reviewed baseline changed: '+p
 reg=load(B/'curriculum/objective_registry.json');ob={o['objective_id']:o for o in reg['objectives']};exp=load(B/'curriculum/exam-exposure.json');er={o['objective_id']:o for o in exp['objectives']};profile=yaml.safe_load((B/'subject-profile.yaml').read_text());spec=[]
 by=profile['slot_plan']['subtypes_by_objective_type']
 for kind in ['DEF','WHY','FEATURE','PROC']:
  typ='economics_revision_'+kind.lower();by[typ]=[kind];profile['objective_types'].append({'type_id':typ,'label':'Focused '+kind+' revision','description':'Planner-scoped retrieval or representation within an existing syllabus outcome.','required_components':profile['answer_structures'][kind],'recommended_item_types':['flashcard']})
 def add(k,parent,unit,label,kind,visual=False):
  par=ob['OBJ-6145-'+parent];prefix='OBJ-6145-'+unit+'-';n=max([int(o.split('-')[-1])for o in ob if o.startswith(prefix)],default=0)+1;oid=prefix+f'{n:02d}'
  o=copy.deepcopy(par);o.update(objective_id=oid,parent_id=par['objective_id'],learner_objective=label,objective_type='economics_revision_'+kind.lower(),depth_tier=1,command_words=[profile['slot_plan']['command_words_by_subtype'][kind][0]],syllabus_guidance='Revision-01 planner decomposition of existing outcome; not a new printed syllabus bullet. Focus: '+label+'.',related_ids=[par['objective_id']]);ob[oid]=o;reg['objectives'].append(o)
  er[oid]={'objective_id':oid,'topic_id':par['topic_id'],'syllabus_text':par['syllabus_text'],'times_examined':0,'marks_examined':0,'evidence_ids':[],'exposure_class':'unseen','evidence':{'question_parts_naming_it':0,'distinct_series':0,'max_mark_tariff':0,'command_words_observed':{}},'grain_note':'New planner decomposition; do not copy parent exposure. Source parent: '+par['objective_id']}
  spec.append({'key':k,'objective_id':oid,'parent_objective_id':par['objective_id'],'topic_id':par['topic_id'],'unit_id':'CU-6145-'+unit,'target':label,'subtype':kind,'owner':'Claude'if visual else'Codex','reviewer':'Codex'if visual else'Claude','provenance':'judgement: bounded revision under original syllabus outcome','syllabus_pdf_page':par['syllabus_page'],'source_syllabus_text':par['syllabus_text']})
 for row in ADDS:add(*row)
 for k,oid,kind,label in EXTRA:
  o=ob[oid];o['command_words']=list(dict.fromkeys(o['command_words']+[profile['slot_plan']['command_words_by_subtype'][kind][0]]));er[oid].setdefault('required_subtypes',[]).append(kind);spec.append({'key':k,'objective_id':oid,'topic_id':o['topic_id'],'target':label,'subtype':kind,'owner':'Codex','reviewer':'Claude','provenance':'judgement: additional answer shape for existing member objective','syllabus_pdf_page':o['syllabus_page'],'source_syllabus_text':o['syllabus_text']})
 for k,p,u,l,req in VISUALS:add(k,p,u,l,'PROC',True);spec[-1]['visual_requirements']=req
 exp['objectives']=list(er.values());profile['depiction_rule']='Claude generates reproducible original economic diagrams from declared numeric parameters and exports question/answer PNGs plus SVG masters; Codex reviews geometry, economics, answer leakage and offline/mobile legibility. Do not misuse the shared business break-even chart model.'
 profile['depictions']={'chart_model':'none','code_fence_languages':['pseudocode','sql','text']}
 profile['slot_plan']['note']+=' Revision-01 adds precise retrieval targets and representations; existing IDs are migrated by semantic key. New objectives use single-purpose types to avoid duplicated definition/interpretation padding. depictions.chart_model none means the shared break-even model cannot validate these economic visuals; it does not excuse the separate geometry and visual review.'
 cross=load(B/'curriculum/objective-crosswalk.json');cross['revision_01_additions']=spec
 with tempfile.TemporaryDirectory(prefix='yyeni-6145-plan-')as td:
  tr=Path(td);ws=tr/'work'/W.name;ws.mkdir(parents=True);shutil.copytree(B/'curriculum',ws/'curriculum');shutil.copy2(B/'qualification-profile.yaml',ws/'qualification-profile.yaml');dump(ws/'curriculum/objective_registry.json',reg);dump(ws/'curriculum/exam-exposure.json',exp);dump(ws/'curriculum/objective-crosswalk.json',cross);(ws/'subject-profile.yaml').write_text(yaml.safe_dump(profile,sort_keys=False,allow_unicode=True))
  an=tr/'operations/analysis';an.mkdir(parents=True);shutil.copy2(ROOT/'operations/analysis/6145-nssco-economics-corpus-analysis.md',an/'6145-nssco-economics-corpus-analysis.md')
  mw.require_prerequisites(str(ws));_,errs=cr.conform(str(ws));assert not errs,errs;mc.build(str(ws),force=True)
  totals=collections.Counter();migration=[];summary=[];new_slots={};orders={}
  for t in rows([p.name for p in (B/'topics').iterdir()]):
   base=load(B/f'topics/{t}/work_order.json');bc=load(B/f'topics/{t}/contract.json');cp=ws/f'topics/{t}/contract.json';con=load(cp)
   # Reuse the approved topic scope limits and teaching envelope, not a new words-per-member quota.
   con['depth_constraints']=copy.deepcopy(bc['depth_constraints']);con['required_outputs']['content_units']=bc['required_outputs']['content_units'];con['subtype_waivers']=bc.get('subtype_waivers',[]);con['generated_by']='standard/build/make_contract.py; revision wrapper preserves approved teaching/scope envelope';dump(cp,con)
   wo=mw.build(str(ws),t)
   # The shared generator only reconciles required_outputs when item_budget changes.
   # Restoring a baseline budget can make that condition false while the initial
   # exposure-derived required_outputs count is still wrong. Always derive both.
   con=load(cp);con['depth_constraints']['item_budget']=wo['planned_item_count'];con['required_outputs']['learning_items']=wo['planned_item_count'];dump(cp,con)
   old={key(s):s for s in base['item_slots']};mx=max(int(s['slot'].split('-')[-2])for s in base['item_slots']);used=set();
   for s in wo['item_slots']:
    raw=s['slot'];k=key(s)
    if k in old:
     s['slot']=old[k]['slot'];used.add(k)
     for lab in ['assessment_objectives','blooms_level','command_word','mark_tariff','difficulty']:assert s[lab]==old[k][lab],(t,s['slot'],lab)
    else:mx+=1;s['slot']=f'ITEM-6145-{t}-{mx:03d}-{s["subtype"]}';new_slots[k]=s
    migration.append({'generated_slot':raw,'stable_slot':s['slot'],'objective_id':s['objective_id'],'subtype':s['subtype'],'existing':k in old})
   assert used==set(old),'Lost old slots '+t
   assert wo['performance_tasks']==base['performance_tasks'],'Changed performance tasks '+t
   oldunits={u['unit_id']:u for u in base['content_units']};assert set(oldunits)=={u['unit_id']for u in wo['content_units']}
   for u in wo['content_units']:u['word_budget']=oldunits[u['unit_id']]['word_budget']
   wo['item_slots'].sort(key=lambda s:s['slot']);wo['generated_by']='standard/build/make_work_order.py + planning/reopen_step4_6145.py stable-ID migration';orders[t]=wo;dump(ws/f'topics/{t}/work_order.json',wo);(ws/f'topics/{t}/work_order.md').write_text(mw.as_markdown(wo));marks=collections.Counter()
   for s in wo['item_slots']:
    for ao in s['assessment_objectives']:marks[ao]+=s['mark_tariff']/len(s['assessment_objectives'])
   for perf in profile['slot_plan']['performance_tasks']:marks.update(perf['ao_split'])
   totals.update(marks);summary.append({'topic_id':t,'title':wo['topic_title'],'objectives':wo['assessable_objective_count'],'existing_items':base['planned_item_count'],'new_cards':wo['planned_item_count']-base['planned_item_count'],'flashcards':len(wo['item_slots']),'packages':len(wo['performance_tasks']),'total':wo['planned_item_count'],'units':len(wo['content_units']),'notes_words':bc['depth_constraints']['word_budget'],'ao_marks':dict(marks)})
  for s in spec:
   slot=new_slots[(s['objective_id'],s['subtype'],None)];s.update(slot_id=slot['slot'],assessment_objectives=slot['assessment_objectives'],blooms_level=slot['blooms_level'],command_word=slot['command_word'],mark_tariff=slot['mark_tariff'])
  assert len(new_slots)==len(spec);fw=load(ws/'curriculum/assessment-framework.json');cmd={c['word']:c for c in fw['command_words']};ids=[]
  for t,wo in orders.items():
   for s in wo['item_slots']:
    assert cmd[s['command_word']]['use_in_prompts'] and str(s['mark_tariff'])in cmd[s['command_word']]['observed_tariffs'],s
    ids.append(s['slot'])
   ids.extend(s['slot']for s in wo['performance_tasks'])
  assert len(ids)==len(set(ids));target=fw['ao_mark_budget']['stated_qualification_weight_percent'];shares={a:100*totals[a]/sum(totals.values())for a in 'ABC'};gap=max(abs(shares[a]-target[a])for a in 'ABC');assert gap<=5,(shares,gap)
  # Shared rollup output is retained with its rounding limitation; exact audit below is authoritative.
  rs,sh,sy,mis,grand=mw.subject_rollup(str(ws),rows(orders));mw.write_rollup(str(ws),rs,sh,sy,mis,grand)
  C.mkdir(parents=True,exist_ok=True);shutil.copytree(ws/'curriculum',C/'curriculum',dirs_exist_ok=True);shutil.copytree(ws/'topics',C/'topics',dirs_exist_ok=True);shutil.copy2(ws/'subject-profile.yaml',C/'subject-profile.yaml');shutil.copy2(ws/'qualification-profile.yaml',C/'qualification-profile.yaml')
 schema=load(ROOT/'standard/v0.2.0-draft/schemas/subject_profile.schema.json');base_profile={k:v for k,v in profile.items()if k in schema['properties']};jsonschema.Draft202012Validator(schema).validate(base_profile)
 v={'status':'PROPOSED - generated and verified; approval pending','baseline_items':580,'topics':len(summary),'assessable_objectives':len([o for o in reg['objectives']if o['parent_id']]),'new_cards':len(spec),'new_nonvisual_cards':sum(s['owner']=='Codex'for s in spec),'new_visual_cards':sum(s['owner']=='Claude'for s in spec),'flashcards':sum(t['flashcards']for t in summary),'packages':sum(t['packages']for t in summary),'items':len(ids),'units':sum(t['units']for t in summary),'notes_words':{k:sum(t['notes_words'][k]for t in summary)for k in ['min','max']},'ao_marks':dict(totals),'ao_share_percent':shares,'ao_target_percent':target,'largest_gap_points':gap,'old_ids_and_labels_preserved':580,'misconception_slots_preserved':37,'by_topic':summary,'candidate_registry_schema_errors':0,'candidate_profile_limit':'Base profile validates; legacy full schema rejects runtime extensions slot_plan, conditioned_mechanisms, depiction_rule and depictions. No standard files changed.'}
 dump(R/'scope.json',spec);dump(R/'id-migration.json',migration);dump(R/'verification.json',v)
 visual=[]
 for s in spec:
  if s['owner']=='Claude':visual.append({**s,'existing_card':False})
 for s in load(B/'topics/3.2/work_order.json')['item_slots']:
  if s['subtype']=='PROC':visual.append({'slot_id':s['slot'],'topic_id':'3.2','target':s['objective_title'],'objective_id':s['objective_id'],'subtype':'PROC','assessment_objectives':s['assessment_objectives'],'blooms_level':s['blooms_level'],'command_word':s['command_word'],'mark_tariff':s['mark_tariff'],'owner':'Claude','reviewer':'Codex','existing_card':True,'visual_requirements':'Add generated question stimulus and worked answer visual to this existing market-forces task, preserving its original valid data and all labels. Check axes, intersections, shifts and quantities independently.'})
 for s in visual:
  stem=s['slot_id'].lower();s['question_png']=f'topics/{s["topic_id"]}/diagrams/{stem}-question.png';s['answer_png']=f'topics/{s["topic_id"]}/diagrams/{stem}-answer.png';s['question_svg']=s['question_png'][:-4]+'.svg';s['answer_svg']=s['answer_png'][:-4]+'.svg';s['learner_leakage_rule']='Question visual contains only given data/starter axes or initial situation. Complete solution curves, outcome labels and computed results belong in answer visual.'
 dump(R/'claude-visual-work-order.json',{'status':'proposed - not authorised for authoring until revised scope approval','cards':visual,'question_images':len(visual),'answer_images':len(visual),'total_png_assets':2*len(visual),'svg_masters':2*len(visual),'upload_status':'not uploaded; classroom import deferred','yyeni_contract_checked':'Live get_flashcard_contracts, 28 October 2026: question_asset_id and answer_asset_id, one managed image per side. Native card fields resolve to question_image_url/answer_image_url.','asset_policy':'Local generated PNG/SVG and declarative data are reviewed first. Import approved images as managed assets later; map returned IDs per card/side. Do not put temporary signed URLs or invented asset IDs in canonical items.'})
 # Preserve the reviewed live bank while candidate scope is under approval.
 for p,h in load(B/'preservation-hashes.json').items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,'Live content changed: '+p
 print(json.dumps({k:v[k]for k in ['new_cards','new_nonvisual_cards','new_visual_cards','flashcards','packages','items','assessable_objectives','ao_marks','ao_share_percent','largest_gap_points']},indent=2));print('Diagram cards',len(visual),'PNG assets',2*len(visual));print('All reviewed production and publication hashes unchanged.')
if __name__=='__main__':main()
