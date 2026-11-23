"""Bounded R7 close-out author decisions layered on the accepted R7 analysis.

No item-level demand retags, new recipes or guessed source equivalences.
"""
import copy,json,re
from analysis_sources import A,WB,ROOT,digest,write

FILES=['textbook-closeout-motion-decisions.json','textbook-closeout-curve-decisions.json','textbook-closeout-family-gap-inputs.json']
LIMIT=('Same-type and structural-branch counts are lower bounds. Roughly one in five or six sampled rejections was judged related; these small samples do not estimate a population error rate. In step 3 search every family member and the accepted item-level assessed/component union links (R5-03), not only recorded relations. A rejection means relation not established; a templated rejection reason is not source comparison evidence.')
TEMPLATE_STATUS='template: exam text + source summary; not a part-specific comparison'


def documents():
 return [json.loads((WB/'tools'/name).read_text())for name in FILES if(WB/'tools'/name).is_file()]


def readings():
 rows={}
 for d in documents():
  for r in d.get('readings',[]):
   r=copy.deepcopy(r)
   if r.get('reader')=='Codex AUTHOR':r['original_reader_label']=r['reader'];r['reader']='Codex author'
   assert r['reading_id']not in rows or rows[r['reading_id']]==r
   rows[r['reading_id']]=r
 return list(rows.values())


def decisions():return [r for d in documents()for r in d.get('relations',[])]


def prose(text):
 """Spacing only in newly authored display prose, never identifiers/operands."""
 text=re.sub(r'([,;:])(?=[A-Za-z])',r'\1 ',text)
 text=re.sub(r'\)(?=[A-Za-z])',') ',text)
 text=text.replace('integral2..3v','integral 2..3 v').replace('at3 responses','at 3 responses')
 return text


def apply_family_metadata(families,items):
 idx={f['family_id']:f for f in families}
 for raw in decisions():
  if raw.get('sample_id'):
   idx[raw['family_id']].setdefault('related_member_leads_closeout',[]).append(dict(part_id=raw['part_id'],selections=copy.deepcopy(raw['exemplar_item_selections']),basis='Best-member subpart checked in R7 close-out',sample_id=raw['sample_id']))
 for d in documents():
  policy=d.get('prompt_policy_recommendation')
  if not policy:continue
  for r in policy['member_pose_annotations']:
   f=idx[r['family_id']];m=next(m for m in f['members']if m['item_id']==r['item_id']and set(r['part_labels'])<=set(m['part_labels']))
   m['pose_classification_closeout']=copy.deepcopy(r)
  fid='8227:TEXTBOOK-FAMILY:trig-derivation-teaching-support'
  f=idx[fid]
  f['pose_classification_closeout']=dict(rule=policy['selected_rule'],reason=policy['family_disposition_limit'])
  f['empty_demand_disposition_r7']['reason']='The eighteen selected members form a heterogeneous teaching/derivation container with no one common directly assessed demand. Goldie C3 Prompt 3 nevertheless poses a validity decision and the concrete 60°/30° test; these member facets remain direct requested responses under the same criterion as Goldie C4 Prompt 2 and YM Example 58. No family-wide identity-proof claim is licensed and accepted item links remain unchanged.'
 return families


def attach_closeout(main,exceptions,fs,parts,normalise,register):
 """Replace only commissioned pairs and add named heterogeneous member links."""
 for raw0 in decisions():
  raw=copy.deepcopy(raw0)
  for k in ['differing_decision','rejection_reason','best_member_reason']:
   if k in raw:raw[k]=prose(raw[k])
  r=normalise(raw,raw['family_id'])
  if r is None:
   f=fs[raw['family_id']]
   register(f,raw['part_id'],'Close-out native best-member comparison, including rejected closest source.',raw['exemplar_item_selections'])
   r=normalise(raw,raw['family_id'])
  assert r is not None
  r['closeout_review']='R7 accepted; named close-out correction, confirmation at step-3 review'
  key=(r['family_id'],r['part_id'])
  if raw.get('relation_scope')=='member-level'and key in main and main[key].get('closeout_review'):
   mid=r['exemplar_member_ids'][0];labels=r['exemplar_part_labels'][mid]
   exceptions.append(dict(family_id=r['family_id'],member_id=mid,part_labels=labels,exam_relations=[r],r7_origin='Close-out explicit additional member-response relation.'))
  else:main[key]=r
  if raw.get('sample_id'):
   # Old whole-response exception records are historical; retain positive narrow
   # exceptions, but do not leave a contradictory named rejection for this pair.
   for e in exceptions:
    if e['family_id']==r['family_id']:
     e['exam_relations']=[x for x in e['exam_relations']if not(x['part_id']==r['part_id']and x['relation']=='rejected')]
   exceptions[:]=[e for e in exceptions if e['exam_relations']]
 for d in documents():
  for removal in d.get('relation_removals',[]):
   key=(removal['family_id'],removal['part_id']);assert key in main
   r=main[key];r.update(relation='rejected',rejection_reason=prose(removal['reason']),nonordered_rejection_specific_reason=prose(removal['reason']),substantive_difference_count_at_least=3,best_subpart_rejection_reason=prose(removal['reason']),reviewed_member_subpart_selections=r.get('exemplar_item_selections'),closeout_review='R7-02 native bounded search removes invalid relation')
   for k in ['differing_decision','difficulty_relative_to_exam']:r.pop(k,None)
   for e in exceptions:
    if e['family_id']==key[0]:e['exam_relations']=[x for x in e['exam_relations']if x['part_id']!=key[1]]
   exceptions[:]=[e for e in exceptions if e['exam_relations']]

 # Every still-active generated rejection has an honest template status. Fresh
 # page decisions supersede templates and are not falsely marked as templates.
 author=json.loads((WB/'tools/textbook-relation-decisions-r7.json').read_text())
 template={(r['family_id'],r.get('baseline_member_id'),r['part_id']):r for r in author['batch_rejection_rewrites']}
 for r in list(main.values())+[r for e in exceptions for r in e['exam_relations']]:
  if r['relation']=='rejected'and 'Source comparison:'in r.get('rejection_reason',''):
   r['rejection_reason_status']=TEMPLATE_STATUS
   r['extraction_warning']='Pasted exam extraction may be garbled. Read the native page; this template is not comparison evidence.'
 return main,exceptions


def patch_gap_records():
 p=WB/'tools/textbook-closeout-family-gap-inputs.json'
 if not p.exists():return
 d=json.loads(p.read_text());path=A/'textbook-gap-search-r7.json';g=json.loads(path.read_text())
 # The accepted pre-closeout author record is the deterministic source, not the
 # previous output of this overlay.
 baseline=A/'history/textbook-gap-search-r7-before-closeout.json'
 if baseline.exists():g=json.loads(baseline.read_text())
 changes=d.get('gap_patches',[])
 if isinstance(changes,dict):changes=[dict(part_id=k,**v)for k,v in changes.items()]
 for patch in changes:
  row=next(r for r in g['parts']if r['part_id']==patch['part_id'])
  for key in patch.get('remove_fields',[]):row.pop(key,None)
  remove=set(patch.get('remove_rejected_item_ids',[]))
  if remove:row['closest_items_rejected']=[r for r in row.get('closest_items_rejected',[])if r['item_id']not in remove]
  row.update({k:copy.deepcopy(v)for k,v in patch.items()if k not in ['remove_fields','remove_rejected_item_ids']})
  for key in ['reason','search_notes']:
   if key in row:row[key]=prose(row[key])
 for r in readings():
  if not any(x['reading_id']==r['reading_id']for x in g['readings']):g['readings'].append(r)
 g['counts'].update(active_positive_parts=sum(r['decision']in ['same type','structural branch']for r in g['parts']),held_internal_comparisons=sum('held source'in r['decision']for r in g['parts']),bounded_no_match_parts=sum(r['decision']=='no match found'for r in g['parts']))
 g['accepted_r7_counts']=copy.deepcopy(g.get('accepted_r7_counts',json.loads(baseline.read_text())['counts']))
 g['counts'].pop('new_active_relation_rows',None)
 g['status']='R7 accepted; close-out gap corrections authored; confirmation at start of step-3 review'
 g['closeout_limits']=LIMIT
 write(path,g)
 lines=['# Direct textbook searches — R7 close-out','',g['status'],'',LIMIT,'','| Part | Decision | Reason / search boundary |','|---|---|---|']
 for r in g['parts']:lines.append('| '+r['part_id']+' | '+r['decision']+' | '+r['reason'].replace('|','\\|')+' '+r.get('search_notes','').replace('|','\\|')+' |')
 lines+=['',g['rights'],'','Full source locators, selected responses, rejected closest items and native reading metadata are in the JSON.']
 (A/'textbook-gap-search-r7.md').write_text('\n'.join(lines)+'\n')
