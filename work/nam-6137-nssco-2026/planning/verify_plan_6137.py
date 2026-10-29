"""Read-only plan reconciliation; never substitutes for learner-content review."""
from pathlib import Path
from collections import Counter
import json,hashlib,yaml,jsonschema,re
W=Path(__file__).resolve().parents[1]
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def verify():
 checks=[]
 def check(ok,label):
  checks.append({'check':label,'passed':bool(ok)})
  if not ok:raise AssertionError(label)
 snap=W/'planning/step3-source'
 check(all(sha(snap/p)==h for p,h in read(snap/'manifest.json').items()),'Frozen Step 3 hashes unchanged')
 old=read(snap/'assessment-evidence/assessment_evidence.json')['records'];new=read(W/'assessment-evidence/assessment_evidence.json')['records']
 check(len(old)==len(new)==535,'535 marked records retained')
 for a,b in zip(old,new):
  check(all(b[k]==v for k,v in a.items() if k!='objective_ids') and b['source_objective_ids']==a['objective_ids'],'Evidence retained: '+a['evidence_id'])
 reg=read(W/'curriculum/objective_registry.json')['objectives']; ids={r['objective_id'] for r in reg}; assess={r['objective_id'] for r in reg if r['parent_id']}
 schemas=W.parents[1]/'standard/v0.2.0-draft/schemas'
 for filename,schema in [('curriculum/objective_registry.json','objective_registry.schema.json'),('qualification-profile.yaml','qualification_profile.schema.json')]:
  artifact=yaml.safe_load((W/filename).read_text());jsonschema.validate(artifact,read(schemas/schema));check(True,'Schema '+filename)
 check(len(ids)==540 and len(assess)==522,'540 unique nodes / 522 assessable outcomes')
 check(all(not r['parent_id'] or r['parent_id'] in ids for r in reg),'Registry parents resolve')
 exposure=read(W/'curriculum/exam-exposure.json')['objectives']; coarse={r['source_mining_id']:r for r in exposure if r.get('source_mining_id')}
 for a in read(snap/'curriculum/exam-exposure.json')['objectives']:
  check(coarse[a['objective_id']]['evidence']==a['evidence'],'Coarse exposure retained: '+a['objective_id'])
 check(len(coarse)==142 and sum(r['exam_exposure']=='unmeasured_bullet_level' for r in exposure)==380,'Fine outcomes have no invented exposure counts')
 profile=yaml.safe_load((W/'subject-profile.yaml').read_text()); perf=profile['slot_plan']['performance_tasks']; commands={r['word']:r for r in read(W/'curriculum/assessment-framework.json')['command_words']}
 totals=Counter();rows=[]; slots=set();covered=set();specs=[]
 for path in sorted((W/'topics').glob('*/work_order.json'),key=lambda p:tuple(map(int,p.parent.name.split('.')))):
  wo=read(path);c=read(path.parent/'contract.json'); cards=wo['item_slots']; tasks=wo['performance_tasks']; allslots=cards+tasks
  check(len(allslots)==wo['planned_item_count']==c['required_outputs']['learning_items'],'Contract/work-order counts '+wo['topic_id'])
  check(len(c['depth_constraints']['excluded_constructs'])==13,'All 13 scope rules '+wo['topic_id'])
  check(len(wo['content_units'])==c['required_outputs']['content_units'],'Content units '+wo['topic_id'])
  check(set(c['scope']['included_objective_ids'])=={s['objective_id'] for s in cards},'All outcomes have cards '+wo['topic_id'])
  for s in cards:
   check(s['slot'] not in slots,'Unique slot '+s['slot']); slots.add(s['slot']);covered.add(s['objective_id'])
   cw=commands[s['command_word']];check(cw['use_in_prompts'] and str(s['mark_tariff']) in cw['observed_tariffs'],'Observed command/tariff '+s['slot'])
   check(s['blooms_level'] in ['Remember','Understand','Apply','Analyse','Evaluate','Create'],'Bloom '+s['slot'])
   for ao in s['assessment_objectives']:totals[ao]+=s['mark_tariff']/len(s['assessment_objectives'])
  for s in tasks:
   check(s['slot'] not in slots,'Unique task '+s['slot']); slots.add(s['slot']);p=next(p for p in perf if p['item_type']==s['item_type']);totals.update(p['ao_split'])
   specs.append({'item_id':s['slot'],'item_type':s['item_type'],'mark_tariff':sum(p['ao_split'].values()),'assessment_objectives':list(p['ao_split']),'ao_mark_split':p['ao_split'],'blooms_level':s['blooms_level'],'objective_pool':c['scope']['included_objective_ids'],'objective_selection':'Select 2-4 genuinely exercised outcomes; record the selection. Each subpart must use an observed command and tariff.','brief':s['brief']})
  rows.append({'topic_id':wo['topic_id'],'title':wo['topic_title'],'objectives':wo['assessable_objective_count'],'flashcards':len(cards),'practice_packages':len(tasks),'items':len(allslots),'notes_min':sum(u['word_budget'][0] for u in wo['content_units']),'notes_max':sum(u['word_budget'][1] for u in wo['content_units'])})
 check(covered==assess,'Every assessable objective planned')
 target={'A':30,'B':41,'C':17,'D':12}; percentages={a:100*totals[a]/sum(totals.values()) for a in target};gap=max(abs(percentages[a]-target[a]) for a in target)
 check(gap<=5,'Independent mark-weighted whole-bank AO gap <=5')
 resources=read(W/'planning/visual-resource-plan-6137.json')['resources'];check(len(resources)==54 and len({r['assigned_item_id'] for r in resources})==54,'54 distinct resource assignments');check(all(r['assigned_item_id'] in slots for r in resources),'All resources bind existing slots');check(sum(r['kind']=='licensed_photo' for r in resources)==6,'Six licensed photograph requirements')
 exemplars={}
 for tid in ['1.2','4.1']:
  q=read(W/'exemplar/work/nam-6137-nssco-2026/topics'/tid/'qa_report.json'); failures=[r for r in q['deterministic_checks'] if r.get('status','').lower()=='fail'];check(not failures and q['release_decision']=='publish','Structural exemplar zero failures '+tid);exemplars[tid]={'release_decision':q['release_decision'],'statuses':dict(Counter(r['status'] for r in q['deterministic_checks']))}
 report={'purpose':'Planning checks only; no production learner PUBLISH claim','result':'PASS','checks':checks,'topics':rows,'totals':{k:sum(r[k] for r in rows) for k in ['objectives','flashcards','practice_packages','items','notes_min','notes_max']},'ao_marks':dict(totals),'ao_percent':percentages,'ao_target':target,'largest_gap_percentage_points':gap,'exemplars':exemplars,'limitations':['QA CLI exits 1 on publish because its exit test expects pass; raw QA reports retained.','C-35/C-41 do not validate Geography images; C-43 not run without practice text.','Exemplars test structure, not independent subject review.','Fine-grain exposure unmeasured; not inherited from umbrella bullets.']}
 (W/'planning/performance-specs-6137.json').write_text(json.dumps({'tasks':specs,'note':'Derived from generated work orders and profile; not new slots.'},indent=2)+'\n')
 (W/'planning/plan-verification-6137.json').write_text(json.dumps(report,indent=2)+'\n'); print(json.dumps({k:report[k] for k in ['result','totals','ao_percent','largest_gap_percentage_points','exemplars']},indent=2));return report
if __name__=='__main__':verify()
