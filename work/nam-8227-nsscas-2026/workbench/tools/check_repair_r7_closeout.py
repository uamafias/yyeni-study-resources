"""Checks the bounded accepted-R7 close-out, not a new content-acceptance gate."""
import copy,collections,json,re
from analysis_sources import A,WB,ROOT,digest,write
from textbook_closeout_r7 import documents,readings,decisions,LIMIT,TEMPLATE_STATUS
from check_repair_r6 import expect_failure


def validate_related_lead(record,family):
 related=[x for x in family.get('related_member_leads_closeout',[])if x['part_id']==record['part_id']]
 if record['relation']=='rejected'and record.get('nonordered_connection')and related:
  assert record.get('best_subpart_rejection_reason')and record.get('reviewed_member_subpart_selections'),'related member subpart lead has no member-level rejection reason'


def canonical_r6_restoration(text):
 # Transform subjects only. Positive target-instead predicates stay positive;
 # every negative batch predicate stays negative, including other-target forms.
 verbs={'asks':'ask','requires':'require','requests':'request','credits':'credit','uses':'use','has':'have'}
 text=re.sub(r'None of these (?:other )?targets (asks|requires|requests|credits|uses|has)',lambda m:'This exam part does not '+verbs[m[1].lower()],text,flags=re.I)
 return re.sub(r'The target instead','This exam part',text,flags=re.I)


def validate_restored_negation(record):
 expected=canonical_r6_restoration(record['r6_rejection_reason'])
 normalise=lambda text:re.sub(r'\s+',' ',text).strip().casefold()
 assert normalise(record['restored_r6_comparison_text'])==normalise(expected),'restored R6 sentence meaning or polarity changed'
 assert record['restored_r6_comparison_text']in record['rejection_reason'],'restored R6 comparison missing from reason'


def refresh_reading_records():
 # Native page reads are unchanged; current relation annotations are regenerated
 # from the canonical authored source, rather than freezing stale D0 decisions.
 for stem,source in [('motion-family-reading','textbook-closeout-motion-decisions.json'),('curve-family-reading','textbook-closeout-curve-decisions.json')]:
  document=json.loads((WB/'tools'/source).read_text())
  document['annotation_status']='D2: native reads retained; relation annotations refreshed from canonical inputs after D1 S3-10 and D2 S28.'
  write(WB/'checks/r7-closeout'/f'{stem}.json',document)
  lines=[f'# {stem} — current relation annotations','','Native source/read hashes are retained. Current annotations are generated from `tools/'+source+'`; no new source-reading claim is inferred.','','| Pair | Relation / direction | Comparison / check |','|---|---|---|']
  for row in document.get('relations',[]):
   lines.append('| '+str(row.get('sample_id',row.get('part_id','')))+' | '+row['relation']+' / '+str(row.get('difficulty_relative_to_exam',''))+' | '+str(row.get('differing_decision',row.get('independent_check',row.get('rejection_reason','')))).replace('|','\\|')+' |')
  (WB/'checks/r7-closeout'/f'{stem}.md').write_text('\n'.join(lines)+'\n')


def run():
 read=lambda p:json.loads(p.read_text())
 fs=read(A/'textbook-families.json')['families'];byf={f['family_id']:f for f in fs};items={i['item_id']:i for i in read(A/'textbook-inventory.json')['items']}
 ledger=read(A/'textbook-exam-relations-r7.json');rows=ledger['relations']+[r for e in ledger['member_level_exceptions']for r in e['exam_relations']]
 baseline=read(WB/'checks/repair-r7-closeout-baseline.json')
 assert digest(A/'history/analysis-snapshot-r7.json')==baseline['snapshot_r7_sha256']
 for p,h in {**baseline['source_files'],**baseline['review_file_hashes']}.items():assert digest(ROOT/p)==h,('protected source/review changed',p)
 required=read(WB/'review/opus-5-5-repair-r7/kept-rejections-r7.json')['pairs']
 selected=[r for r in decisions()if r.get('sample_id')]
 assert {r['sample_id']for r in selected}=={r['sample_id']for r in required}and len(selected)==12
 scans=[]
 for d in documents():scans+=d.get('all_family_members',d.get('family_readings',[]))
 scans={x['family_id']:x for x in scans}
 natives={r['reading_id']:r for r in readings()}
 for r in natives.values():
  assert r['reader']=='Codex author'and r['read_date']=='2026-11-23'
  assert digest(ROOT/r['render_path'])==r['render_sha256'],'close-out native page hash changed'
  assert baseline['source_files'][r['source_path']]==r['source_sha256']
 pair_rows=[]
 for raw in selected:
  f=byf[raw['family_id']];scan=scans[f['family_id']]
  assert scan.get('all_members_read',scan.get('every_member_read'))is True
  actual={(m['item_id'],tuple(m['part_labels']))for m in f['members']}
  seen={(m['item_id'],tuple(m.get('selected_family_part_labels',m.get('part_labels',[]))))for m in scan['members']}
  assert actual==seen,('best-member comparison did not read every family member',f['family_id'])
  for m in scan['members']:
   assert m['rendered_reading_ids']and set(m['rendered_reading_ids'])<=set(natives)
  candidates=[r for r in rows if r['family_id']==f['family_id']and r['part_id']==raw['part_id']and r.get('sample_id')==raw['sample_id']]
  assert len(candidates)==1,('closeout pair absent or duplicated',raw['sample_id'])
  r=candidates[0];assert r['relation']==raw['relation'];validate_related_lead(r,f)
  assert r['exemplar_item_selections']==raw['exemplar_item_selections']and r['read_date']=='2026-11-23'
  pair_rows.append(dict(sample_id=r['sample_id'],family_id=f['family_id'],part_id=r['part_id'],best_member_selections=r['exemplar_item_selections'],relation=r['relation'],difficulty_relative_to_exam=r.get('difficulty_relative_to_exam'),reason=r.get('differing_decision',r.get('rejection_reason')),members_read=len(scan['members'])))
 author=read(WB/'tools/textbook-relation-decisions-r7.json');batch=author['batch_rejection_rewrites'];assert len(batch)==403
 for r in batch:
  validate_restored_negation(r)
  assert r['rejection_reason_status']==TEMPLATE_STATUS
  assert r['restored_r6_comparison_text']in r['rejection_reason']
  assert not re.search(r'(?:it does not perform|;|before exponential preimages;) Relation not established',r['rejection_reason'])
 assert author['closeout_batch_rejection_audit']['truncations_fixed']==11
 for r in rows:
  if r['relation']=='rejected'and 'Source comparison:'in r.get('rejection_reason',''):assert r['rejection_reason_status']==TEMPLATE_STATUS
  validate_related_lead(r,byf[r['family_id']])
 gaps=read(A/'textbook-gap-search-r7.json');bygap={g['part_id']:g for g in gaps['parts']}
 for pid in ['8227:EXAM:2023:P2:Q4:c','8227:EXAM:2023:P2:Q2:answer']:
  g=bygap[pid];assert g['decision']=='no match found'and g.get('closest_items_rejected')and g['searched_book_pages']
  assert not any(r['part_id']==pid and r['relation']!='rejected'for r in rows),('bounded gap retains a false positive relation',pid)
 graph=bygap['8227:EXAM:2024:P1:Q9:c'];assert graph['decision']=='structural branch'
 assert not re.search(r'closest rejected:.*example\s*16',graph['search_notes'],re.I),'selected graph member still called rejected'
 assert '8227:TB:YM:C4:Example:16'not in {r['item_id']for r in graph.get('closest_items_rejected',[])},'selected graph member still listed as rejected'
 f=byf['8227:TEXTBOOK-FAMILY:trig-point-value-parameter-support'];assert '8227:2020:M1:T6:O03:D01'in f['assessed_demand_ids']
 f=byf['8227:TEXTBOOK-FAMILY:explicit-second-derivative-zero'];assert '8227:2020:M2:T4:O02:D01'in f['assessed_demand_ids']
 assert any(r['family_id']==f['family_id']and r['part_id']=='8227:EXAM:2022:P2:Q5:a'for r in rows)
 for f in fs:
  if f['family_id'].endswith('differentiation-conceptual-proof-support'):assert 'quotient'in f['empty_demand_disposition_r7']['reason']and 'product rule'not in f['empty_demand_disposition_r7']['reason']
 policy=next(d['prompt_policy_recommendation']for d in documents()if d.get('prompt_policy_recommendation'))
 c=next(d for d in documents()if d.get('gap_patches'))
 exponential=byf['8227:TEXTBOOK-FAMILY:exponential-scale-context-support']
 assert {(m['item_id'],tuple(m['part_labels']))for m in exponential['members']}=={(m['item_id'],tuple(m['part_labels']))for m in c['exponential_member_readings']},'exponential comparison omitted a family member'
 for rr in c['exponential_member_readings']:assert rr['reading_id']in natives
 for change in read(WB/'tools/textbook-closeout-cosmetic-inputs.json')['changes']:
  assert re.sub(r'\s','',change['before'])==re.sub(r'\s','',change['after']),'cosmetic correction changed mathematical/text characters'
 for ann in policy['member_pose_annotations']:
  m=next(m for m in byf[ann['family_id']]['members']if m['item_id']==ann['item_id']and set(ann['part_labels'])<=set(m['part_labels']))
  assert m['pose_classification_closeout']==ann
 for p in [A/'objective-problem-map.md',A/'textbook-insights.md']:assert LIMIT in p.read_text()
 mapping=read(A/'objective-problem-map.json');assert LIMIT in mapping['limits']
 for p,h in mapping['inputs'].items():assert digest(ROOT/p)==h,('stale map input',p)
 # The commissioned fixture uses a real related best-member lead; a generic
 # whole-response dismissal must not hide the unreviewed matching sub-part.
 r=copy.deepcopy(next(r for r in rows if r.get('sample_id')));r.update(relation='rejected',nonordered_connection=True,rejection_reason='The whole selected source response differs.')
 r.pop('best_subpart_rejection_reason',None);r.pop('reviewed_member_subpart_selections',None)
 negatives=[expect_failure('nonordered-related-lead-without-member-level-reason','related member subpart lead has no member-level rejection reason',lambda:validate_related_lead(r,byf[r['family_id']]))]
 neg=copy.deepcopy(next(r for r in batch if 'None of these targets' in r['r6_rejection_reason']))
 for field in ['restored_r6_comparison_text','rejection_reason']:neg[field]=neg[field].replace('does not ', '')
 negatives.append(expect_failure('restored-r6-negation-lost','restored R6 sentence meaning or polarity changed',lambda:validate_restored_negation(neg)))
 over=copy.deepcopy(next(r for r in batch if 'The target instead asks the learner' in r['r6_rejection_reason']and 'This exam part asks the learner' in r['restored_r6_comparison_text']))
 for field in ['restored_r6_comparison_text','rejection_reason']:over[field]=over[field].replace('This exam part asks the learner','This exam part does not ask the learner')
 negatives.append(expect_failure('restored-r6-positive-sentence-over-negated','restored R6 sentence meaning or polarity changed',lambda:validate_restored_negation(over)))
 refresh_reading_records()
 before=read(A/'history/textbook-exam-relations-r7-before-closeout.json')
 kind=lambda rs:dict(collections.Counter(r['relation']for r in rs))
 oldrows=before['relations']+[r for e in before['member_level_exceptions']for r in e['exam_relations']]
 parts={p['part_id']:p for q in read(A/'question-analysis.json')['questions']for p in q['parts']}
 absent=lambda rs:sorted(set(parts)-{r['part_id']for r in rs if r['relation']!='rejected'})
 result=dict(status='Accepted R7 plus D2 sentence-polarity repair: author checks pass; D2 focused confirmation pending',pair_redecisions=pair_rows,native_readings_checked=len(natives),all_member_family_count=len(scans),template_records_labelled=403,truncated_reasons_fixed=11,
  before=dict(main_decisions=len(before['relations']),relations_by_kind=kind(oldrows),parts_without_any_relation=len(absent(oldrows)),same_type_demands=73),
  after=dict(main_decisions=len(ledger['relations']),relations_by_kind=kind(rows),parts_without_any_relation=len(absent(rows)),same_type_demands=mapping['counts']['by_demand']['with_same_type_textbook_practice']),
  no_relation_part_ids=absent(rows),new_negative_fixtures=negatives,gap_counts=gaps['counts'],limits=LIMIT)
 write(WB/'checks/r7-closeout/final-validation.json',result);print(json.dumps({k:v for k,v in result.items()if k not in ['pair_redecisions','new_negative_fixtures','no_relation_part_ids']},indent=2));return result

if __name__=='__main__':run()
