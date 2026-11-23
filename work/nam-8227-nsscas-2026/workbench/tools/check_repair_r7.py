"""R7 scoped final author checks, with commissioned negatives in memory.

Structural checks do not certify mathematical correctness or independent acceptance.
"""
import collections,copy,json,re
from analysis_sources import A,WB,ROOT,digest,write
from textbook_exam_comparison_r6 import candidate_ids,validate_relation,validate_candidate_decisions,validate_summary_anchors
from apply_textbook_family_repairs_r7 import validate as family_check,DUPLICATE_PREFIX
from apply_textbook_source_repairs_r7 import validate as source_check
from apply_textbook_notes_r7 import validate as notes_check
from check_repair_r6 import expect_failure


def relation_rows(data):
 return data['relations']+[r for e in data.get('member_level_exceptions',[])for r in e['exam_relations']]

def positive_parts(data,parts,usable=False):
 return {r['part_id']for r in relation_rows(data)if r['relation']!='rejected'and(not usable or parts[r['part_id']]['disposition']=='include'and not parts[r['part_id']].get('hold_ids'))}

def validate_rejection(r):
 if r['relation']=='rejected'and r.get('nonordered_connection'):
  assert r.get('nonordered_rejection_specific_reason')and r.get('substantive_difference_count_at_least',0)>=3,'nonordered rejection lacks a specific reason'
 if r['relation']=='rejected':
  assert not re.search(r'the target instead|none of these targets',r['rejection_reason'],re.I),'batch-worded rejection remains'


def validate_gap_notes(gaps,positives,required):
 by={r['part_id']:r for r in gaps['parts']}
 assert set(by)==set(required)and len(by)==len(gaps['parts']),'gap search population differs'
 for pid in required:
  r=by[pid]
  if pid not in positives and 'held source'not in r.get('decision',''):
   assert r.get('search_notes')and r.get('searched_book_pages')and r.get('closest_items_rejected'),'exam part has no textbook relation and no search note'
  assert r.get('rendered_reading_ids')and r.get('read_date')and r.get('full_corpus_absence_claim')is False


def run():
 read=lambda p:json.loads(p.read_text())
 fdata=read(A/'textbook-families.json');fs=fdata['families'];items=read(A/'textbook-inventory.json')['items'];idx={i['item_id']:i for i in items}
 parts={p['part_id']:p for q in read(A/'question-analysis.json')['questions']for p in q['parts']};ledger=read(A/'textbook-exam-relations-r7.json');readings={r['reading_id']:r for r in ledger['readings']};byf={f['family_id']:f for f in fs}
 for f in fs:
  validate_candidate_decisions(f,parts);validate_summary_anchors(f,parts)
  for r in f['exam_relations']:validate_relation(r,f,parts,readings);validate_rejection(r)
  for e in f['member_level_exceptions']:
   for r in e['exam_relations']:validate_relation(r,f,parts,readings);validate_rejection(r)
 assert all(not r.get('additional_source_decisions')for r in relation_rows(ledger)if r['relation']=='same type')
 fam=family_check(fs,items,wb=WB);src=source_check(items,fs,wb=WB);notes=notes_check(items)
 olditems=read(A/'history/textbook-inventory-r6.json')['items'];keys=['item_id','assessed_8227_demand_ids','component_demand_ids','objective_ids','learner_display']
 assert [{k:i[k]for k in keys}for i in items]==[{k:i[k]for k in keys}for i in olditems],'accepted item demand links changed'
 pairs=lambda rows:collections.Counter((m['item_id'],p)for f in rows for m in f['members']for p in m['part_labels'])
 assert pairs(fs)==pairs(read(A/'history/textbook-families-r6.json')['families']),'source response multiplicity changed'
 assert all(i['learner_display']is False for i in items),'textbook original became learner-displayable'
 b=read(WB/'checks/repair-r7-baseline.json')
 assert digest(A/'history/analysis-snapshot-r6.json')==b['snapshot_r6_sha256']
 for p,h in {**b['source_files'],**b['review_file_hashes']}.items():assert digest(ROOT/p)==h,('protected source/review changed',p)
 gaps=read(A/'textbook-gap-search-r7.json');required=[r['part_id']for r in gaps['parts']]
 # Compare to immutable reviewer list rather than trusting current gap population.
 reviewed=read(WB/'review/opus-5-5-repair-r6/no-textbook-relation-parts-r6.json')
 assert set(required)=={'8227:EXAM:'+r['part']for r in reviewed['syllabus_parts']}
 positives=positive_parts(ledger,parts);validate_gap_notes(gaps,positives,required)
 for r in gaps['parts']:
  if r['decision']=='no match found':assert r['part_id']not in positives,'search says no match despite positive relation'
  if 'held source'in r['decision']:
   assert parts[r['part_id']]['disposition']!='include'and r['learner_display']is False and r['design_anchor']is False
 comparisons=read(WB/'checks/r7/disputed-pair-review.json');assert len(comparisons['pairs'])==28
 target=next(r for r in comparisons['pairs']if r['pair']=='PAIR-024');assert target['new_relation']=='same type'
 used_reads={rid for r in gaps['parts']+comparisons['pairs']for rid in r['rendered_reading_ids']}
 for rid in used_reads:
  rr=readings[rid];assert rr['reader']=='Codex author'and rr['read_date']=='2026-11-23'
  assert digest(ROOT/rr['render_path'])==rr['render_sha256'],'gap/dispute native evidence changed'
 for r in gaps['parts']:
  for spec in r.get('selected_textbook_items',[])+r.get('closest_items_rejected',[]):
   assert spec['item_id']in idx and set(spec['part_labels'])<={z['subpart']for z in idx[spec['item_id']].get('answer_verification_r5',[])},'gap search selector invalid'
 write(WB/'checks/r7/gap-and-dispute-input-check.json',dict(status='author selector and native reading hashes checked after root integration; not independent content acceptance',gap_search_parts=22,active_positive_parts=gaps['counts']['active_positive_parts'],held_internal_comparisons=2,bounded_no_match_parts=gaps['counts']['bounded_no_match_parts'],disputed_entries=28,unique_native_readings_checked=len(used_reads),input_sha256={str(p.relative_to(ROOT)):digest(p)for p in [A/'textbook-gap-search-r7.json',WB/'tools/textbook-exam-overrides-r7.json']}))
 for r in comparisons['pairs']:
  assert r['read_date']=='2026-11-23'and isinstance(r['agree_with_reviewer'],bool)and r['reason']
  actual=[z for z in relation_rows(ledger)if z['family_id']==r['family_id']and z['part_id']==r['part_id']]
  assert any(z['relation']==r['new_relation']for z in actual),('disputed decision not integrated',r['pair'])
 mapping=read(A/'objective-problem-map.json')
 for p,h in mapping['inputs'].items():assert digest(ROOT/p)==h,('map rebuilt before final input',p)
 assert mapping['unfinished_family_part_decisions']==0
 mapped_pairs={(r['family_id'],r['part_id'],kind)for o in mapping['objectives']for d in o['demands']for field,kind in [('same_type_textbook_practice','same type'),('textbook_structural_branches','structural branch')]for r in d[field]}
 for r in relation_rows(ledger):
  if r['relation']!='rejected'and parts[r['part_id']]['disposition']=='include'and not parts[r['part_id']].get('hold_ids'):
   assert (r['family_id'],r['part_id'],r['relation'])in mapped_pairs,('usable selected-response relation vanished from objective map',r['family_id'],r['part_id'])
 for name in ['objective-problem-map.md','textbook-insights.md']:
  assert 'no verified relation recorded yet'not in(A/name).read_text().lower(),'stale relation label'
 # Required four cases test the real final-state validators, not implementation mirrors.
 negatives=[]
 broken=copy.deepcopy(gaps);r=next(x for x in broken['parts']if x['part_id']not in positives and 'held source'not in x['decision']);r.pop('search_notes')
 negatives.append(expect_failure('unmatched-part-without-search-note','no textbook relation and no search note',lambda:validate_gap_notes(broken,positives,required)))
 r=copy.deepcopy(next(r for r in ledger['relations']if r.get('nonordered_connection')));r.update(relation='rejected');r.pop('nonordered_rejection_specific_reason',None)
 negatives.append(expect_failure('nonordered-rejection-without-specific-reason','nonordered rejection lacks',lambda:validate_rejection(r)))
 broken=copy.deepcopy(fs);f=next(f for f in broken if f.get('empty_demand_disposition_r7')and not f['assessed_demand_ids']);f.pop('empty_demand_disposition_r7')
 negatives.append(expect_failure('empty-family-without-disposition','empty family missing explicit disposition',lambda:family_check(broken,items,wb=WB)))
 broken=copy.deepcopy(fs);f=next(f for f in broken if f['distinction_basis'].startswith('Compared with '));prefix=f['distinction_basis'].split(': ',1)[0]+': ';f['distinction_basis']=prefix+f['distinction_basis']
 negatives.append(expect_failure('doubled-comparison-prefix','doubled sibling prefix',lambda:family_check(broken,items,wb=WB)))
 before=read(A/'history/textbook-exam-relations-r6.json');counts=lambda d:dict(collections.Counter(r['relation']for r in relation_rows(d)))
 no={pid for pid in parts if pid not in positives};usable={pid for pid,p in parts.items()if p['disposition']=='include'and not p.get('hold_ids')};unusable_no=sorted(no-usable)
 result=dict(status='R7 accepted; named close-out author structural checks pass; confirmation at start of step-3 review',families=fam,source_repairs=src,notes=notes,
  counts=dict(before=dict(main_decisions=len(before['relations']),relations_all_rows=counts(before),parts_without_any_relation=len(set(parts)-positive_parts(before,parts)),same_type_demands=b['counts']['same_type_demand_count']),
   after=dict(main_decisions=len(ledger['relations']),member_exception_rows=sum(len(e['exam_relations'])for e in ledger['member_level_exceptions']),relations_all_rows=counts(ledger),mixed_branch_rows=sum(r['relation']=='structural branch'and r.get('difficulty_relative_to_exam')=='mixed'for r in relation_rows(ledger)),parts_without_any_relation=len(no),usable_parts_without_any_relation=len(no&usable),same_type_demands=mapping['counts']['by_demand']['with_same_type_textbook_practice'])),
  parts_without_any_relation=sorted(no),held_parts_without_relation=unusable_no,commissioned_gap_parts=22,disputed_pairs=28,unchanged_item_links=len(items),source_response_pairs=len(pairs(fs)),new_negative_fixtures=negatives,
  limitations=['Author evidence and structural checks are not independent educational acceptance.','Same-type counts remain a commissioned-pair lower bound, not a full relabel.',str(gaps['counts']['bounded_no_match_parts'])+' bounded direct searches found no complete counterpart in inspected pages; no absolute absence claim.','All note prose conservatively quarantined; no full text repair.'])
 write(WB/'checks/r7/final-validation.json',result);print(json.dumps({k:v for k,v in result.items()if k not in ['new_negative_fixtures','parts_without_any_relation']},indent=2));return result

if __name__=='__main__':run()
