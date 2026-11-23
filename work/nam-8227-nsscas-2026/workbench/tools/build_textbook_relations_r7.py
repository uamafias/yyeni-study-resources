"""Extend the accepted R6 relation bank with explicit R7 source decisions.

No topical similarity is promoted to a match. Unreviewed new candidates remain
open, and rejected records mean relation not established, not no practice.
"""
import collections,copy,json,re
from analysis_sources import A,WB,write

PATH=A/'textbook-exam-relations-r7.json'

def _read(name,default):
 p=WB/'tools'/name
 return json.loads(p.read_text())if p.exists()else default

def _selection(record,old_families):
 if record.get('exemplar_item_selections'):return record['exemplar_item_selections']
 f=old_families[record['family_id']];members={m['member_id']:m for m in f['members']}
 return [dict(item_id=members[mid]['item_id'],part_labels=record.get('exemplar_part_labels',{}).get(mid,members[mid]['part_labels']))for mid in record.get('exemplar_member_ids',[])]

def _locate(selection,families,preferred):
 options=[]
 for f in families:
  if f.get('retired'):continue
  matched=[]
  for spec in selection:
   m=next((m for m in f['members']if m['item_id']==spec['item_id']and set(spec['part_labels'])<=set(m['part_labels'])),None)
   if m is None:break
   matched.append((m,spec['part_labels']))
  else:options.append((f,matched))
 assert options,('R7 selected responses do not share a family',preferred,selection)
 return next((x for x in options if x[0]['family_id']==preferred),options[0])

def build_for(families,parts,items):
 baseline=json.loads((A/'history/textbook-exam-relations-r6.json').read_text())
 oldf={f['family_id']:f for f in json.loads((A/'history/textbook-families-r6.json').read_text())['families']}
 fs={f['family_id']:f for f in families};main={};exceptions=[];archived=[]
 author=_read('textbook-relation-decisions-r7.json',{})
 updates={(r['family_id'],r['part_id']):r for r in author.get('batch_rejection_rewrites',[])if r['record_scope']=='main'}
 updates.update({(r['family_id'],r['part_id']):r for r in author.get('nonordered_main_pair_decisions',[])})
 named={(r['family_id'],r['part_id']):r for r in author.get('named_relation_corrections',[])}
 extra=_read('textbook-exam-overrides-r7.json',dict(relations=[],gap_relations=[],readings=[]))
 readings={r['reading_id']:copy.deepcopy(r)for r in baseline['readings']}
 from textbook_closeout_r7 import readings as closeout_readings,attach_closeout,LIMIT
 for r in extra.get('readings',[])+author.get('readings',[])+closeout_readings():
  assert r['reading_id']not in readings or readings[r['reading_id']]==r
  readings[r['reading_id']]=copy.deepcopy(r)

 def register(f,pid,reason,selection):
  if not set(f['assessed_demand_ids'])&set(parts[pid]['directly_assessed_demand_ids']):
   rows=f.setdefault('source_search_candidates_r7',[])
   if not any(r['part_id']==pid for r in rows):rows.append(dict(part_id=pid,reason=reason,exemplar_item_selections=selection,basis='Explicit rendered-source/selected-response comparison; item-level demand links unchanged.'))

 def normalise(record,origin,force_target=None):
  r=copy.deepcopy(record);r.setdefault('family_id',origin)
  preferred=r['family_id'];f=fs.get(preferred)
  if f and f.get('retired'):preferred=f['canonical_family_id']
  selection=_selection(r,oldf)
  if r['relation']!='rejected' or selection:
   f,matched=_locate(selection,families,preferred)
   r['family_id']=f['family_id'];r['exemplar_member_ids']=[m['member_id']for m,_ in matched]
   r['exemplar_part_labels']={m['member_id']:labels for m,labels in matched}
   r['exemplar_item_selections']=copy.deepcopy(selection)
   if r['relation']!='rejected':register(f,r['part_id'],'Source search or preserved positive selected-response relation.',selection)
  elif f and f.get('retired'):
   r['family_id']=f['canonical_family_id'];f=fs[r['family_id']]
  else:f=fs.get(r['family_id'])
  if not f:return None
  candidates={pid for pid,p in parts.items()if set(f['assessed_demand_ids'])&set(p['directly_assessed_demand_ids'])}|{x['part_id']for x in f.get('source_search_candidates_r7',[])}
  if r['part_id']not in candidates:
   archived.append(dict(record=r,reason='Not a current family demand/source-search candidate after the named R7 membership or demand repair.'))
   return None
  r['r7_relation_origin']=origin
  if r['relation']!='rejected':r.pop('rejection_reason',None)
  return r

 for raw in baseline['relations']:
  r=copy.deepcopy(raw);key=(r['family_id'],r['part_id'])
  if key in updates:
   patch=updates[key];r.update({k:copy.deepcopy(v)for k,v in patch.items()if k not in ['record_scope','baseline_member_id','baseline_exception_part_labels']})
  if key in named:r.update(copy.deepcopy(named[key]))
  r=normalise(r,raw['family_id'])
  if r is None:continue
  key=(r['family_id'],r['part_id'])
  if key not in main:main[key]=r
  elif r['relation']!='rejected':
   mid=r['exemplar_member_ids'][0];labels=r['exemplar_part_labels'][mid]
   exceptions.append(dict(family_id=r['family_id'],member_id=mid,part_labels=labels,exam_relations=[r],r7_origin='Preserved positive from merged R6 family.'))

 batch_exception={(r['family_id'],r.get('baseline_member_id'),r['part_id']):r for r in author.get('batch_rejection_rewrites',[])if r['record_scope']=='member exception'}
 nonordered_exception={(r['family_id'],r['baseline_member_id'],r['part_id']):r for r in author.get('nonordered_exception_decisions',[])}
 for old in baseline['member_level_exceptions']:
  for raw in old['exam_relations']:
   r=dict(copy.deepcopy(raw),family_id=old['family_id'])
   patch=batch_exception.get((old['family_id'],old['member_id'],r['part_id']))
   if patch:r.update(copy.deepcopy(patch))
   patch=nonordered_exception.get((old['family_id'],old['member_id'],r['part_id']))
   if patch:r.update(copy.deepcopy(patch))
   r=normalise(r,old['family_id'])
   if r is None:continue
   sel=[dict(item_id=next(m['item_id']for m in oldf[old['family_id']]['members']if m['member_id']==old['member_id']),part_labels=old['part_labels'])]
   f,matched=_locate(sel,families,r['family_id']);m,labels=matched[0]
   exceptions.append(dict(family_id=f['family_id'],member_id=m['member_id'],part_labels=labels,exam_relations=[r],r7_origin='Preserved R6 named response exception.'))

 # Correct the eight exact-value target descriptions before fresh positive decisions.
 for patch in extra.get('rejection_reason_overrides',[]):
  key=(patch['family_id'],patch['part_id'])
  assert key in main
  main[key].update(copy.deepcopy(patch))

 # Fresh native-page decisions supersede the sampled/baseline decision only.
 review=json.loads((WB/'review/opus-5-5-repair-r6/blind-pair-disagreements.json').read_text())
 reviewed={(r['family_id'],r['part_id'])for r in review}
 for raw in extra.get('relations',[])+extra.get('gap_relations',[]):
  r=normalise(raw,raw['family_id'])
  if r is None:
   # Negative fresh decisions also need a registered source-search candidate.
   f,matched=_locate(raw['exemplar_item_selections'],families,raw['family_id'])
   register(f,raw['part_id'],'Fresh R7 source comparison, including rejected closest candidates.',raw['exemplar_item_selections'])
   r=normalise(raw,raw['family_id'])
  assert r is not None
  key=(r['family_id'],r['part_id']);main[key]=r
  if (raw['family_id'],raw['part_id'])in reviewed:
   wanted={(x['item_id'],tuple(x['part_labels']))for x in raw['exemplar_item_selections']}
   kept=[]
   for e in exceptions:
    same=e['family_id']==r['family_id']and any(x['part_id']==r['part_id']for x in e['exam_relations'])
    if same:
     m=next(m for m in fs[e['family_id']]['members']if m['member_id']==e['member_id'])
     same=(m['item_id'],tuple(e['part_labels']))in wanted
    if not same:kept.append(e)
   exceptions=kept

 # Additional native decisions on families first given assessed demands in R7.
 for raw in author.get('new_family_candidate_decisions',[]):
  r=normalise(raw,raw['family_id']);assert r is not None
  main[(r['family_id'],r['part_id'])]=r

 main,exceptions=attach_closeout(main,exceptions,fs,parts,normalise,register)
 pending=[]
 for f in families:
  candidates={pid for pid,p in parts.items()if set(f['assessed_demand_ids'])&set(p['directly_assessed_demand_ids'])}|{r['part_id']for r in f.get('source_search_candidates_r7',[])}
  pending.extend(dict(family_id=f['family_id'],part_id=pid)for pid in sorted(candidates)if(f['family_id'],pid)not in main)
 internal_held=[]
 for raw in extra.get('internal_held_comparisons',[]):
  assert raw['learner_display']is False and raw['design_anchor']is False
  assert parts[raw['part_id']]['disposition']!='include' or parts[raw['part_id']].get('hold_ids')
  f,matched=_locate(raw['exemplar_item_selections'],families,raw['family_id'])
  held=dict(copy.deepcopy(raw),family_id=f['family_id'],exemplar_member_ids=[m['member_id']for m,_ in matched])
  internal_held.append(held)
  f.setdefault('r7_internal_intended_type_comparisons',[]).append(copy.deepcopy(held))
 data=dict(closeout_limits=LIMIT,internal_held_comparisons=internal_held,schema_version='8227-textbook-exam-relations-r7',status='author decisions assembled; open candidates remain'if pending else'R7 accepted; close-out author decisions complete; confirmation at start of step-3 review',readings=list(readings.values()),relations=list(main.values()),member_level_exceptions=exceptions,archived_noncurrent_r6_records=archived,
  candidate_policy='Uncapped direct-demand overlap plus explicitly sourced R7 search candidates; no item demand relabelling.',rejection_policy='Relation not established, not proof of different decisions or absent practice.',same_type_limit='R6-03: counts remain lower bounds; only the commissioned R7 pairs were re-decided.')
 write(PATH,data);write(WB/'checks/r7/candidate-decisions-pending.json',dict(count=len(pending),pairs=pending))
 return data
