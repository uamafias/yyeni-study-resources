"""Carry forward source reads only for explicit schema repairs; re-read changed mathematics."""
import json
from analysis_sources import A,WB,ROOT,write,digest,evidence_path
from award_read_audit_r4 import fingerprint

def build():
 old=json.loads((A/'history/award-register-r4.json').read_text());oldrows={r['criterion_id']:r for t in old['award_tables']for r in t['rows']}
 prior=json.loads((A/'history/award-second-read-r4.json').read_text())
 current=json.loads((A/'award-register-r4-draft.json').read_text())
 repairs=json.loads((A/'award-repairs-r5.json').read_text())['rows'];manual={(r['source_key'],r['row_number']):r for r in repairs}
 log={'status':'R4 source reads retained with explicit schema audit; R5 changed mathematics re-read on source crops; independent check pending','rows':{}}
 counts={'unchanged':0,'schema_only':0,'source_row_re_read':0}
 for table in current['award_tables']:
  for row in table['rows']:
   key=row['criterion_id'];previous=oldrows[key];check=prior['rows'][key]
   assert fingerprint(previous)==check['row_fingerprint'],('R4 history check',key)
   a={k:v for k,v in previous.items()if k not in ['first_read','second_read']};z={k:v for k,v in row.items()if k not in ['first_read','second_read']};changes=[k for k in sorted(a.keys()|z.keys())if a.get(k)!=z.get(k)]
   entry=dict(check);entry['row_fingerprint']=fingerprint(row)
   repair=manual.get((table['source_key'],int(key.rsplit(':',1)[1])))
   if repair:
    name=repair['detail_image_name']
    if name:
     detail=json.loads((WB/f'checks/r5/{name}.json').read_text());assert detail['render_scale']>=4 and detail['inspection'].startswith('Codex author re-read')
     assert digest(evidence_path(detail['path']))==detail['sha256']
     entry.update(status='author R5 re-read against scale4source crop',evidence_path=detail['path'],evidence_sha256=detail['sha256'],notes=repair['reading'])
    else:
     assert key.endswith(':12')and table['source_key']=='2025-2-Q3'
     entry['notes']='R5 derived c.a.o. retained as inference from completed paths; no claim of a printed missing row.'
    entry['prior_read_fingerprint']=check['row_fingerprint'];entry['changed_fields']=changes;counts['source_row_re_read']+=1
   elif changes:
    assert set(changes)<={'accepted_alternatives','establishes_given_result'},(key,changes)
    if 'establishes_given_result'in changes:assert row['source_mark_type']=='E'and row['establishes_given_result']is True
    if 'accepted_alternatives'in changes:assert row['what_earns_it']in previous['accepted_alternatives']and row['accepted_alternatives']==[x for x in previous['accepted_alternatives']if x!=row['what_earns_it']]
    entry['schema_repair']={'basis':'Existing source transcription and R4 source read retained; explicit E establishment flag and/or duplicated main-answer removal only','prior_read_fingerprint':check['row_fingerprint'],'changed_fields':changes,'date':'2026-11-17'};counts['schema_only']+=1
   else:counts['unchanged']+=1
   log['rows'][key]=entry
 write(A/'award-second-read-r4.json',log);write(A/'award-audit-reconciliation-r5.json',{'counts':counts,'limits':'No new source reading is claimed for mechanical schema corrections; changed mathematics is separately evidenced.'});print(counts)
if __name__=='__main__':build()
