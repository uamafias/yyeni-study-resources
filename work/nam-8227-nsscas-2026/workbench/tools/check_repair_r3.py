"""Focused R3 structural checks and independent mathematical source spot checks."""
import collections,json,math
import sympy as s
from analysis_sources import A,WB,ROOT,write,digest

def read(name):return json.loads((A/name).read_text())
def alias(x):
 m,t,o,d=map(int,x.split('.'));return f'8227:2020:M{m}:T{t}:O{o:02}:D{d:02}'
def main():
 qs=read('question-analysis.json')['questions'];parts=[p for q in qs for p in q['parts']];by={p['source_key']:p for p in parts}
 required={k:['1.6.3.1'] for k in ['2021-2-Q6:b','2022-1-Q9:b','2022-2-Q3:a','2022-2-Q3:b','2023-2-Q3:a','2024-1-Q12:b','2024-2-Q2:answer','2024-2-Q9:b']}
 required.update({'2023-2-Q7:a':['1.9.1.2'],'2025-2-Q8:answer':['1.8.2.2'],'2022-2-Q10:b':['2.3.2.3'],'2025-2-Q7:a':['2.3.2.1'],'2021-1-Q4:b':['1.9.3.1']})
 for key,demands in required.items():assert all(alias(d) in by[key]['directly_assessed_demand_ids'] for d in demands),key
 assert alias('2.5.1.1') not in by['2023-2-Q7:a']['directly_assessed_demand_ids']
 for key,src in [('2023-2-Q6:d','a'),('2025-1-Q4:c','a'),('2025-1-Q4:c','b'),('2024-2-Q11:c','a')]:
  assert any(e['from_part']==src and e['type']=='cue' for e in by[key]['dependency_edges']),key
 for p in parts:
  assert p['directly_assessed_demand_ids']
  for r in p['examination_references']:
   if p['disposition']=='hold':assert r['learner_display'] is False,(p['part_id'],r)
   if r['relation']=='derived-from':assert r['learner_display'] is False and r['learner_label'].startswith('Adapted from Cambridge')
 visual=[]
 for p in parts:
  if any(p['diagram_parameters'].get(k) for k in ['fixed','variable','relations']):visual.append(p['diagram_parameters'])
 cb=read('cambridge-evidence.json')['items']
 for i in cb:
  if i['diagram_assets']:visual.append(i['diagram_parameters'])
 assert len(visual)==62,len(visual)
 for v in visual:
  assert set(['fixed','variable','relations'])<=set(v)
  assert 'constraints' not in v
  assert all(isinstance(v[k],list) and all(x==x.strip() and x for x in v[k]) for k in ['fixed','variable','relations'])
 assert next(i for i in cb if i['item_id']=='8227:CAMBRIDGE:s15:11:8-iii')['purpose']=='variety'
 assets=read('asset-index.json')['assets'];assert len(assets)==39
 for a in assets:assert digest(ROOT/a['path'])==a['sha256']
 crop=json.loads((WB/'checks/crop-containment.json').read_text());assert len(crop['rows'])==39 and all(r['status']=='pass' for r in crop['rows'])
 mc=read('marking-conventions.json');assert len(mc['award_tables'])==119 and len(mc['question_coverage'])==119
 assert {r['source_locator']['report_year'] for r in mc['rules']}==set(range(2021,2026))
 for table in mc['award_tables']:
  assert sum(r['paper_tariff'] for r in table['part_reconciliation'])==table['paper_tariff']
  for row in table['part_reconciliation']:assert all(x==row['paper_tariff'] for x in row['exclusive_full_path_totals'].values())
  assert all(str(r['source_locator']['paper'])in ['1','2'] for r in table['rows'])
 pv=read('nsscas-cambridge-provenance.json');assert len(pv['question_search_register'])==119
 for match in pv['matches']:
  ev=match['rendered_confirmation'];assert digest(ROOT/ev['path'])==ev['sha256']
  assert match['confidence'] in ['identical','adapted']
  for side in ['nsscas_locator','cambridge_locator']:
   loc=match[side];assert digest(ROOT/loc['source_path'])==loc['source_sha256'] and len(loc['pdf_pages'])==len(loc['printed_pages'])
  for pair in match['part_correspondence']:
   p=next(p for p in parts if p['part_id']==pair['nsscas_part_id'])
   assert any(r.get('provenance_match_id')==match['match_id'] for r in p['examination_references'])
 tb=read('textbook-inventory.json');assert len(tb['items'])==len({i['item_id'] for i in tb['items']})
 for i in tb['items']:
  assert i['learner_display'] is False
  assert i['scope_check']['status'] in ['in-scope','in-scope-parts-only','out-of-scope']
  assert i['answer_key']['available'] in [True,False,None]
  assert i['pdf_page']>0 and i['printed_page']>0
  assert i['representation'] in ['text','diagram','graph','table']
 assert not tb['coverage']['exhaustive'] and not tb['coverage']['formal_stop_rule_applied']
 reading=read('textbook-reading-r3.json');assert reading['catalogued_items_with_render_evidence']==len(tb['items'])
 for ev in reading['author_reading']:assert digest(ROOT/ev['evidence_path'])==ev['sha256']
 # Independent calculations use expressions transcribed from source images, not analysis generator answer functions.
 x=s.symbols('x',positive=True);checks=[]
 def check(locator,description,actual,expected):
  assert s.simplify(actual-expected)==0,(locator,description,actual,expected)
  checks.append({'locator':locator,'check':description,'recomputed':str(actual),'expected':str(expected),'pass':True})
 assert math.isclose(math.exp(.3*math.log(10)),1.99526231496888,abs_tol=1e-13)
 checks.append({'locator':'YM PDF439 Example33','check':'exp(0.3 ln10) independently recomputes the inverse log','recomputed':math.exp(.3*math.log(10)),'pass':True})
 assert abs(10**.3-1.20)>.79
 checks[-1]['source_defect_confirmed']='b approximately1.99526231497, not1.20'
 check('YM PDF119 Example10','g(7)=2, so inverse(-2)=7 fails inverse definition',s.sqrt(7-3),2)
 assert s.sqrt(7-3)!=-2
 check('YM PDF122 Example12(b)','square root cannot produce negative output',s.sqrt(9-5),2)
 check('YM PDF298 Example27','stationary point ordinate',s.Integer(0)**3+1,1)
 check('YM PDF368 Exercise7 Q9','gradient equation positive sqrt(x)=2/3',3*s.Rational(2,3)-2/s.Rational(2,3),-1)
 f=2*x**s.Rational(3,2)-4*s.sqrt(x)+2
 check('YM PDF368 Exercise7 Q9','integrated initial-condition curve ordinate at x=4/9',f.subs(x,s.Rational(4,9)),-s.Rational(2,27))
 check('YM PDF351 Example26','improper integral via independent symbolic limit',s.limit(-1/x,x,s.oo)-(-1),1)
 check('YM PDF353 Example28','endpoint radical improper integral',s.integrate((3-x)**(-s.Rational(1,2)),(x,0,3)),2*s.sqrt(3))
 check('YM PDF161 Example8','segment at angle2pi/3,r6',s.Rational(1,2)*36*(2*s.pi/3-s.sin(2*s.pi/3)),12*s.pi-9*s.sqrt(3))
 check('YM PDF217 Example53(b)','stem principal arctan1',s.atan(1),s.pi/4)
 assert s.simplify(s.atan(-1/s.sqrt(2))-s.pi/4)!=0
 theta=s.symbols('theta',real=True)
 area=s.integrate(s.cos(x),(x,theta,s.pi/2))
 check('YM PDF578 TryNow9 Q2','independent area integral gives rectangle-area equation',theta*s.cos(theta)-area,theta*s.cos(theta)+s.sin(theta)-1)
 # The source grouping was rechecked at enlarged scale and is correct; no false defect is retained.
 iteration=.5
 for _ in range(70):iteration=(1-math.sin(iteration))/math.cos(iteration)
 assert abs(iteration*math.cos(iteration)+math.sin(iteration)-1)<1e-7
 checks[-1]['numeric_root']=iteration;checks[-1]['source_grouping']='whole numerator 1-sin(theta); confirmed on enlarged source image'
 before=json.loads((A/'history/question-analysis-r2.json').read_text())['questions'];bp=[p for q in before for p in q['parts']]
 def stats(ps):return {'parts':len(ps),'direct_links':sum(len(p['directly_assessed_demand_ids'])for p in ps),'dependency_edges':sum(len(p['dependency_edges'])for p in ps)}
 old=read('history/demand-dispositions-r2.json')['rows'];now=read('demand-dispositions.json')['rows']
 changes=[{'demand_id':a['demand_id'],'before':len(a['observed_part_links']),'after':len(b['observed_part_links'])}for a,b in zip(old,now)if len(a['observed_part_links'])!=len(b['observed_part_links'])]
 result={'status':'pass; author checks only','before':stats(bp),'after':stats(parts),'demand_count_changes':changes,
   'thin_demands_before':sum(0<len(r['observed_part_links'])<=2 for r in old),'thin_demands_after':sum(0<len(r['observed_part_links'])<=2 for r in now),
   'independent_source_recomputations':checks,'textbook_items':len(tb['items']),'unclassified_textbook_heading_leads':reading['unclassified_heading_leads'],
   'limits':'Structural and independent calculation methods by the author; not an independent vendor judgement. Full textbook source analysis, answer checking and second-vendor sample remain incomplete.'}
 write(WB/'checks/repair-r3-validation.json',result);print(json.dumps({k:v for k,v in result.items()if k not in ['independent_source_recomputations','demand_count_changes']},indent=2))
if __name__=='__main__':main()
