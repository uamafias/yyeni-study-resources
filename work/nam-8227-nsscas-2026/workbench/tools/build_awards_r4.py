"""Assemble rendered-page award transcriptions; untranscribed is never absent."""
import collections,json,re
from analysis_sources import A,WB,ROOT,write,digest

def attach_question_award_links(questions):
 """Link source parts to the author register without depending on a built register."""
 by={q['source_key']:q for q in questions};key=None;pg=None;counts=collections.Counter()
 for q in questions:
  q['transcribed_award_pdf_pages']=[]
  for p in q['parts']:p['official_award_criterion_ids']=[];p['derived_award_completion_ids']=[]
 for line in (WB/'tools/award_rows_r4.txt').read_text().splitlines():
  if not line or line.startswith('#'):continue
  if line.startswith('@'):key,page=line[1:].split('|');pg=int(page);continue
  if line.startswith('^'):pg=int(line[1:]);continue
  fields=line.split('|');part,mark=fields[0],fields[2];q=by[key];counts[key]+=1
  p=next(p for p in q['parts']if(p['source_label']or'answer')==part)
  p['derived_award_completion_ids'if mark.startswith('~')else'official_award_criterion_ids'].append(f'{q["question_id"]}:AWARD:{counts[key]:02}')
  if pg not in q['transcribed_award_pdf_pages']:q['transcribed_award_pdf_pages'].append(pg)
 for q in questions:
  q['marking_evidence_note']='marking_excerpt_pdf_pages is the historical native-text scan only; transcribed_award_pdf_pages and criterion links include raster tables visually read in round4.'
  for p in q['parts']:
   p['marking_rule_status']=('official with derived completion'if p['derived_award_completion_ids']else'official complete'if p['official_award_criterion_ids']else'absent')
 return questions


def build(final=False):
 qs=json.loads((A/'question-analysis.json').read_text())['questions'];by={q['source_key']:q for q in qs}
 index=json.loads((A/'report-page-index-r4.json').read_text());pages={(p['year'],p['pdf_page']):p for p in index['pages']}
 tables={};key=None
 for line in (WB/'tools/award_rows_r4.txt').read_text().splitlines():
  if not line or line.startswith('#'):continue
  if line.startswith('^'):
   pg=int(line[1:]);continue
  if line.startswith('@'):
   key,pg=line[1:].split('|');pg=int(pg);assert key in by and key not in tables,key
   tables[key]={'source_key':key,'question_id':by[key]['question_id'],'rows':[]};continue
  assert key
  fields=line.split('|');assert len(fields)==7,(key,len(fields),line)
  part,path,mark,criterion,condition,alternatives,derived=fields
  official=not mark.startswith('~');mark=mark.removeprefix('~')
  value=int(re.search(r'\d+$',mark)[0]);kind=mark[:-len(str(value))];assert kind in ['M','A','B','DM','DA','DB','E','SC'],(key,mark)
  q=by[key];p=next((p for p in q['parts']if (p['source_label']or'answer')==part),None);assert p,(key,part)
  page=pages[q['year'],pg];n=len(tables[key]['rows'])+1
  printed_alternatives=[x for x in alternatives.split(';;')if x]
  if re.search(r'\bo\.e\.',condition):printed_alternatives.append('Equivalent forms accepted (o.e.)')
  printed_alternatives=list(dict.fromkeys(x for x in printed_alternatives if x.strip()!=criterion.strip()))
  qualifiers=[code for code,pattern in [('F.T.',r'F\.T\.'),('c.a.o.',r'c\.a\.o\.'),('www',r'\bwww\b'),('s.o.i.',r's\.?o\.?i\.'),('allow one slip',r'allow one slip')]if re.search(pattern,condition,re.I)]
  tables[key]['rows'].append({'criterion_id':f'{q["question_id"]}:AWARD:{n:02}','part_id':p['part_id'],'part':part,
   'exclusive_method_path':path,'path_kind':'special-case-cap' if kind=='SC' else 'full-credit',
   'evidence_kind':'official award table' if official else 'derived completion; printed award row absent',
   'accepted_for_pilot':official and not path.startswith('rejected-'),
   'source_mark_type':kind if official else None,'mark_type':'A' if kind=='E' else kind.removeprefix('D'),'value':value,
   'what_earns_it':criterion,'condition':condition,'accepted_alternatives':printed_alternatives,'alternative_award_aggregation':'exclusive; never sum',
   'qualifier_codes':qualifiers,'dependent_award':kind.startswith('D'),'derived_additions':[]if not derived else [{'status':'derived','text':derived}],
   'source_locator':{'source_path':page['source_path'],'source_sha256':page['source_sha256'],'report_year':q['year'],'paper':q['paper'],
      'question':q['question'],'part':part,'pdf_page':pg,'printed_page':pg-2},
   'first_read':{'reviewer':'Codex author','date':'2026-11-17','basis':'rendered page, including raster award table','evidence_path':page['render_path'],'evidence_sha256':page['render_sha256']},
   'second_read':{'status':'pending; never inferred from text or first transcription'}})
  if kind=='E':tables[key]['rows'][-1]['establishes_given_result']=True
 audit_path=A/'award-second-read-r4.json'
 audit=json.loads(audit_path.read_text())['rows']if audit_path.exists()else {}
 from award_read_audit_r4 import fingerprint
 for t in tables.values():
  for row in t['rows']:
   check=audit.get(row['criterion_id'])
   if check and check['row_fingerprint']==fingerprint(row):row['second_read']=check
 coverage=[]
 for q in qs:
  key=q['source_key'];t=tables.get(key)
  if t:
   t['part_reconciliation']=[]
   for p in q['parts']:
    rr=[r for r in t['rows']if r['part_id']==p['part_id']];assert rr,(key,p['source_label'],'no rows')
    paths=collections.defaultdict(int);special={}
    for r in rr:
     if r['path_kind']=='special-case-cap':special[r['exclusive_method_path']]=special.get(r['exclusive_method_path'],0)+r['value']
     else:paths[r['exclusive_method_path']]+=r['value']
    assert paths and all(v==p['printed_marks']for v in paths.values()),(key,p['source_label'],dict(paths),p['printed_marks'])
    assert all(v<=p['printed_marks']for v in special.values()),(key,special)
    official_totals={name:sum(r['value']for r in rr if r['exclusive_method_path']==name and r['evidence_kind']=='official award table')for name in paths}
    derived_totals={name:paths[name]-official_totals[name]for name in paths}
    t['part_reconciliation'].append({'part_id':p['part_id'],'paper_tariff':p['printed_marks'],'exclusive_path_aggregation':'maximum; never sum','exclusive_full_path_totals':dict(paths),'special_case_caps':special,'derived_row_ids':[r['criterion_id']for r in rr if r['evidence_kind']!='official award table'],'official_full_path_totals':official_totals,'derived_tariff_completion_by_path':derived_totals,'official_breakdown_complete':not any(derived_totals.values())})
   t['paper_tariff']=sum(p['printed_marks']for p in q['parts'])
  coverage.append({'source_key':key,'question_id':q['question_id'],'status':'table_present'if t else 'not_transcribed',
   'source_locators':list({(r['source_locator']['pdf_page']):r['source_locator']for r in t['rows']}.values())if t else [],
   'absence_claimed':False,'part_table_coverage':[{'part_id':p['part_id'],'status':'table_present'if any(r['part_id']==p['part_id'] and r['evidence_kind']=='official award table'for r in t['rows'])else 'absent','evidence_locators':[r['source_locator']for r in t['rows']if r['part_id']==p['part_id']],'absence_reason':next((r['condition']for r in t['rows']if r['part_id']==p['part_id'] and r['evidence_kind']!='official award table'),None)}for p in q['parts']]if t else []})
 if final:
  assert len(tables)==119,'No final register while an award table remains untranscribed'
  assert all('row_fingerprint'in r['second_read']for t in tables.values()for r in t['rows']),'Second-read incomplete or stale'
 result={'schema_version':'8227-awards-r4','status':'author second-read complete; independent review pending'if final else 'author transcription; inspect second_read_rows for current checked extent',
   'coverage':{'questions':len(qs),'tables_transcribed':len(tables),'criterion_rows':sum(len(t['rows'])for t in tables.values()),
      'untranscribed':len(qs)-len(tables),'absent_tables':0,'official_rows':sum(r['evidence_kind']=='official award table'for t in tables.values()for r in t['rows']),'derived_completion_rows':sum(r['evidence_kind']!='official award table'for t in tables.values()for r in t['rows']),'second_read_rows':sum(r['second_read'].get('row_fingerprint')is not None for t in tables.values()for r in t['rows'])},'award_tables':list(tables.values()),'question_coverage':coverage,
   'mark_type_normalisation':{'M':'method','A':'accuracy','B':'independent statement or accuracy','DM':'dependent method; dependency condition retained','DA':'dependent accuracy','DB':'dependent independent/statement award as printed','E':'establishment: normalised A carries establishes_given_result=true; learner must establish the supplied result','SC':'special-case cap; alternative to full path, never added','F.T.':'follow-through of specified earlier work only','c.a.o.':'correct answer only','www':'without wrong working','s.o.i.':'seen or implied','allow one slip':'limited tolerance for one slip exactly where printed; not universal'},
   'limits':'Source rows are normalised mathematical transcriptions. Printed conditions/alternatives retained separately. Derived blank values flagged. SC paths are capped alternatives, never extra marks. This is not a runtime rubric.'}
 write(A/'award-register-r4-draft.json',result);print(json.dumps(result['coverage'],indent=2));return result
if __name__=='__main__':build()
