"""Author repair checks, with independent source scans; not independent review."""
import collections
import inspect
import json
import re
import subprocess
import sys
from pypdf import PdfReader
from analysis_sources import A, ROOT, WB, clean, digest, reference_label, write
from demand_coverage import compute
from source_defects import recomputations


def read(path):return json.loads(path.read_text())

def main():
 q=read(A/'question-analysis.json')['questions'];parts=[p for x in q for p in x['parts']]
 qi={x['source_key']:x for x in q};pi={x['source_key']:x for x in parts}
 demands=read(A/'demand-registry.json')['demands'];valid={d['demand_id'] for d in demands}
 rows=read(A/'demand-dispositions.json')['rows'];families=read(A/'problem-patterns.json')['patterns']
 items=read(A/'cambridge-evidence.json')['items'];base=read(WB/'checks/repair-r2-baseline.json')
 review=WB/'review/opus-5-5-step-1-3'
 assert digest(A/'history/analysis-snapshot-r1.json')=='1afe99d597617897cb3bf0489cd3bcbc236624fef05cef53a8aa4a92704a561f'
 for path,sha in base['review_file_hashes'].items():assert digest(ROOT/path)==sha,('review modified',path)
 for path,sha in base['original_sources'].items():assert digest(ROOT/path)==sha,('source modified',path)
 assert len(parts)==250 and len(q)==119 and len(demands)==138
 old=read(A/'history/question-analysis-r1.json')['questions']
 assert [p['part_id'] for x in old for p in x['parts']]==[p['part_id'] for p in parts]
 # Independent simple bracket scan: do not invoke the builder's scan/answer functions.
 tariff=[];all_text=[]
 for year in range(2021,2026):
  for paper in [1,2]:
   selected=[x for x in q if x['year']==year and x['paper']==paper]
   source=ROOT/selected[0]['question_source_path'];found=[]
   for n,page in enumerate(PdfReader(source).pages,1):
    text=page.extract_text()
    if n>1 and re.search(r'FORMULAE\s+AND\s+NOTATIONS',text,re.I):break
    if n>1:found += [int(x) for x in re.findall(r'\[\s*(\d+)\s*\]',text)];all_text.append((year,paper,n,text))
   expected=[p['printed_marks'] for x in selected for p in x['parts']]
   assert found==expected and sum(found)==75,(year,paper)
   tariff.append({'year':year,'paper':paper,'parts':len(found),'marks':sum(found),'ordered_match':True})
 # Literal objective checking is independent of the authored normalization.
 syllabus=read(A/'extracted/syllabus.json');source_pages={n:clean(p.extract_text()) for n,p in enumerate(PdfReader(ROOT/syllabus['source']).pages,1)}
 objectives=read(WB.parent/'curriculum/objective_registry.json')['objectives']
 for obj in objectives:
  assert clean(obj['syllabus_text']) in source_pages[obj['source']['pdf_page']],obj['objective_id']
  assert obj['normalized_math_text']
 # Both supplementary roles and all AS links must exist; supplementary links do not count AS coverage.
 registry=read(A/'demand-registry.json')
 extra={x['demand_id'] for x in registry['supplementary_demands']}
 for p in parts:
  assert p['directly_assessed_demand_ids'] and set(p['directly_assessed_demand_ids'])<=valid|extra,p['source_key']
  assert isinstance(p['directly_assessed_objective_ids'],list) and isinstance(p['prerequisite_demand_ids'],list)
  for edge in p['prerequisite_demand_ids']:assert edge['role'] and edge['demand_id'] in valid|extra
  for key in ['given_representation','diagram_assets','diagram_parameters','response_format','examination_references']:assert key in p
  assert p['given_representation']['kind'] in ['text','diagram','graph','table']
  assert p['response_format'] in ['numeric','symbolic','proof/show-that','sketch','explanation']
 assert compute(demands,parts,items)==rows
 assert list(inspect.signature(compute).parameters)==['demands','parts','comparable_items']
 assert not re.search(r'^\s*(?:from|import).*famil',inspect.getsource(sys.modules['demand_coverage']),re.M)
 # Recompute coverage independently with a dictionary, without family links.
 for row in rows:
  expected=sorted(p['part_id'] for p in parts if row['demand_id'] in p['directly_assessed_demand_ids'] and p['disposition']!='hold')
  assert row['observed_part_links']==expected,row['demand_id']
  assert row['status'] in ['examination-observed (NSSCAS 8227)','comparable-examination-observed (Cambridge 9709)','syllabus-derived']
  assert row['disposition'] and row['reason']
 # Reviewer's 18 explicit-cue/award questions, including both nested (b) parts.
 required={
 '2021-1-Q12':[('a','b'),('a','c'),('b','c')],'2021-2-Q6':[('a','b')],
 '2021-2-Q12':[('a.i','a.ii')],'2022-1-Q1':[('a','b')],'2022-1-Q2':[('a','b')],
 '2022-1-Q9':[('a','b')],'2022-2-Q1':[('a','b')],'2022-2-Q4':[('a','b')],
 '2022-2-Q6':[('a','b.i'),('a','b.ii')],'2023-1-Q2':[('c.i','c.ii')],
 '2023-1-Q8':[('a','b')],'2023-2-Q8':[('a','b')],'2024-1-Q12':[('a','b')],
 '2024-2-Q9':[('a','b')],'2024-2-Q10':[('a','b')],
 '2025-1-Q5':[('a','b')],'2025-1-Q6':[('a','b')],'2025-2-Q4':[('a','b')]}
 for key,edges in required.items():
  actual={(e['from_part'],e['to_part']) for e in qi[key]['dependencies']}
  assert set(edges)<=actual,(key,edges,actual)
 cue_gaps=[]
 scans=read(A/'part-source-scan.json')['parts']
 for key,part in pi.items():
  if scans[key]['cue_hits'] and not part['dependency_edges'] and part.get('cue_scan_disposition',{}).get('status')!='within-part cue; no preceding assessed part':cue_gaps.append(key)
 assert not cue_gaps,('unannotated cues',cue_gaps)
 # Confirm the automatic award census, not a claimed complete official memo bank.
 award=read(A/'award-source-scan.json')['questions']
 expected_keys={f'{y}-2-Q{i}' for y,end in [(2021,4),(2023,9),(2024,11)] for i in range(1,end+1)}
 assert set(award)==expected_keys and len(award)==24
 for k,pages in award.items():assert qi[k]['marking_excerpt_pdf_pages']==pages
 for k in ['2024-2-Q9','2024-2-Q10']:assert any(e['type']=='follow-through' for e in qi[k]['dependencies'])
 assert all(e['type']!='follow-through' for e in qi['2023-2-Q6']['dependencies'] if e['to_part']=='d')
 # All 11 response parts and the two connected graph-reading parts are included.
 sketches=[p for p in parts if p['requires_sketch_response']]
 dependent=[p for p in parts if p['requires_learner_sketch_reading']]
 assert len(sketches)==11 and len(dependent)==2
 for p in sketches+dependent:assert p['disposition']=='include' and p['capability_hold'] is None
 assert all(p.get('sketch_credited_features') for p in sketches)
 assets=[a for a in read(A/'asset-index.json')['assets'] if not a['asset_id'].startswith('9709_')]
 assert len(assets)==32
 for asset in assets+[a for i in items for a in i['diagram_assets']]:
  assert digest(ROOT/asset['path'])==asset['sha256']
  assert digest(ROOT/asset['source_path'])==asset['source_sha256']
  assert len(asset['crop_box_pdf_points'])==4 and asset['origin']=='rendered-source-crop; original bytes unchanged'
 # References: exact fields, source bytes, generated labels, conservative family relation.
 reference_count=0
 ci={i['item_id']:i for i in items};pids={p['part_id']:p for p in parts}
 for obj in parts+families+items:
  refs=obj['examination_references']
  assert refs or obj.get('syllabus_derived_reason')
  for ref in refs:
   assert set(['board','syllabus_code','year','session','paper','question','part','printed_page','pdf_page','source_path','source_sha256','relation','verified_by','learner_label'])<=set(ref)
   assert digest(ROOT/ref['source_path'])==ref['source_sha256']
   assert ref['learner_label']==reference_label(ref)
   assert ref['learner_label'] is None if ref['relation']=='related' else bool(ref['learner_label'])
   reference_count+=1
 for f in families:
  bounds=f['grade_variation_bounds'];assert bounds['hardest_descriptor_ids'] and bounds['easiest_descriptor_ids']
  sources=[pids[k] for k in f['question_parts']]+[ci[k] for k in f['cambridge_item_ids']]
  actual={(r['source_sha256'],r['question'],r['part']) for r in f['examination_references']}
  expected={(r['source_sha256'],r['question'],r['part']) for s in sources for r in s['examination_references']}
  assert actual==expected,f['pattern_id']
  for r in f['examination_references']:
   if r['relation']=='same-type':
    matches=[s for s in sources if any(r['source_sha256']==x['source_sha256'] and r['question']==x['question'] and r['part']==x['part'] for x in s['examination_references'])]
    assert any(set(s.get('directly_assessed_demand_ids',s.get('assessed_8227_demand_ids',[])))==set(f['direct_demand_ids']) and f['response_formats']==[s['response_format']] and s.get('disposition')!='hold' for s in matches)
 # Original Cambridge text and matching sources are human checks, not proven by hashes.
 for i in items:
  assert i['transcription_status']=='checked-against-rendered-page' and i['verbatim_text']
  assert i['scope_check']['status'] in ['in-scope','in-scope-parts-only','out-of-scope']
  loc=i['mark_scheme_locator'];assert loc['pdf_pages'] and digest(ROOT/loc['source_path'])==loc['source_sha256']
  assert sum(p['marks'] for p in i['assessed_parts'])==i['marks']
  assert all(p['examination_references'] and set(p['directly_assessed_demand_ids'])<=valid|extra for p in i['assessed_parts'])
  assert {d for p in i['assessed_parts'] for d in p['directly_assessed_demand_ids'] if d in valid}==set(i['assessed_8227_demand_ids'])
  assert all(r['board']=='Cambridge International' and r['learner_label'] for r in i['examination_references'])
 grades=read(WB.parent/'curriculum/grade-descriptions.json')['descriptors']
 assert collections.Counter(x['grade'] for x in grades)=={'a':15,'c':16,'e':15}
 assert all(x['objective_ids'] and x['demand_ids'] for x in grades)
 conditions=read(WB.parent/'curriculum/assessment-conditions.json')
 # Reviewer math sampling re-run independently of source transcriptions/answers.
 maths=recomputations();review_maths=read(review/'inputs.json')['mathematical_sampling']['scripted_recomputation']['results']
 assert set(review_maths)<=set(maths)
 assert set(maths)-set(review_maths)=={'2024P2Q7','2021P2Q12_report'},'unexpected added source recomputation'
 differences=[]
 def compare(current,expected,path):
  if isinstance(expected,dict):
   for k,v in expected.items():compare(current[k],v,path+'.'+k)
  elif isinstance(expected,list):
   assert len(current)==len(expected),path
   for n,(a,b) in enumerate(zip(current,expected)):compare(a,b,path+'['+str(n)+']')
  elif current!=expected:
   differences.append({'field':path,'current':current,'reviewer':expected})
 for key in review_maths:compare(maths[key],review_maths[key],key)
 assert len(differences)==1 and differences[0]['field']=='2023P2Q7.F(radian_root)',differences
 assert abs(differences[0]['current']-differences[0]['reviewer'])<=2.1e-6
 oldparts={p['part_id']:p for x in old for p in x['parts']}
 primary_changes=[{'part_id':p['part_id'],'marks':p['printed_marks'],
       'old_primary':oldparts[p['part_id']]['primary_objective_id'],'new_primary':p['primary_objective_id']}
       for p in parts if oldparts[p['part_id']]['primary_objective_id']!=p['primary_objective_id']]
 write(WB/'checks/reviewer-scan-reconciliation.json',{
  'author':'Codex; these are author reruns, not independent acceptance',
  'ordered_tariffs':tariff,'objective_literal_matches':60,'grade_statements':46,
  'dependency_review_questions_checked':len(required),'unannotated_cue_parts':cue_gaps,
  'award_excerpt_questions':len(award),'source_integrity_originals':len(base['original_sources']),
  'review_files_unchanged':len(base['review_file_hashes']),'recomputations':maths,
  'reviewer_recomputation_baseline':review_maths,'R5_additional_recomputation_ids':sorted(set(maths)-set(review_maths)),'recomputation_differences':differences,
  'cross_paper_theme':conditions['cross_paper_theme'],'changed_primary_links':primary_changes,
  'mathematical_difference_explanation':'F(radian_root)=1 at converged precision; reviewer 0.999998 evaluated the displayed six-decimal iterate. All values agree at stated rounding. No degree-mode acceptance adopted.',
  'demand_presence_scan':{name:[{'year':y,'paper':p,'pdf_page':n,'hit':m.group(0)} for y,p,n,t in all_text for m in re.finditer(rx,t,re.I)] for name,rx in {
   'monotonicity':r'increasing|decreasing','inflexion':r'inflexion|inflection','quadratic-division-leads':r'divid|quotient',
   'segment':r'\bsegment\b','unit-vector':r'unit\s+vector','iteration-failure-leads':r'converg|diverg|oscillat'}.items()},
  'differences':'16 zero-usable NSSCAS demands plus inflexion facet are reconciled in gap-demand-reconciliation.json. New direct links change cross-paper and coverage counts without changing 250 parts/750 marks. Award count 22→24 is a correction.',
  'references_checked':reference_count,'cambridge_verified_items':len(items),
  'limits':['Human mathematics/transcription judgments remain subject to cross-vendor re-review','No complete award criterion bank','No exhaustive textbook/corpus classification','No app runtime acceptance']})
 print(json.dumps({'status':'author repair checks passed','parts':len(parts),'demands':len(demands),'families':len(families),'cambridge_items':len(items),'references':reference_count,'award_questions':len(award)},indent=2))
if __name__=='__main__':main()
