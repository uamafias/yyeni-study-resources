"""Round4 source-register invariants; failing fixtures never mutate author files."""
import argparse,copy,json,collections
from analysis_sources import A,WB,ROOT,digest,write,evidence_path

def validate_awards(mc):
 questions=json.loads((A/'question-analysis.json').read_text())['questions']
 expected={q['source_key']:q for q in questions};coverage={q['source_key']:q for q in mc['question_coverage']}
 assert set(coverage)==set(expected),'question has neither table nor recorded absence'
 tables={t['source_key']:t for t in mc['award_tables']}
 for key,q in expected.items():
  c=coverage[key];assert c['status']in ['table_present','absent'],'question has neither table nor recorded absence'
  if c['status']=='absent':assert c.get('rendered_absence_evidence'),'recorded absence needs rendered evidence';continue
  assert key in tables and c['source_locators'],('table coverage without table',key)
  t=tables[key];parts={p['part_id']:p for p in q['parts']};rr={r['part_id']:r for r in t['part_reconciliation']}
  assert set(parts)==set(rr),('missing part reconciliation',key)
  for p in parts.values():
   recon=rr[p['part_id']];assert recon['paper_tariff']==p['printed_marks']
   assert recon['exclusive_path_aggregation']=='maximum; never sum','exclusive alternative awards were summed'
   actual=collections.Counter();special=collections.Counter()
   for row in t['rows']:
    if row['part_id']!=p['part_id']:continue
    (special if row['path_kind']=='special-case-cap'else actual)[row['exclusive_method_path']]+=row['value']
   assert dict(actual)==recon['exclusive_full_path_totals'],('row values differ from reconciled path totals',key,p['part_id'])
   assert dict(special)==recon['special_case_caps']
   assert set(p['official_award_criterion_ids'])=={r['criterion_id']for r in t['rows']if r['part_id']==p['part_id']and r['evidence_kind']=='official award table'}
   assert set(p['derived_award_completion_ids'])=={r['criterion_id']for r in t['rows']if r['part_id']==p['part_id']and r['evidence_kind']!='official award table'}
   assert all(v==p['printed_marks']for v in recon['exclusive_full_path_totals'].values()),('path tariff',key)
  assert sum(r['paper_tariff']for r in rr.values())==t['paper_tariff']
  for row in t['rows']:
   assert row['alternative_award_aggregation']=='exclusive; never sum','exclusive alternative awards were summed'
   assert isinstance(row['accepted_alternatives'],list)
   assert row['second_read']['row_fingerprint']
   if row['evidence_kind']!='official award table':assert row['accepted_for_pilot']is False
   for check in [row['first_read'],row['second_read']]:
    # second-read audit retains its own naming, with the same scoped evidence.
    path=check.get('evidence_path',check.get('image_path'));sha=check.get('evidence_sha256',check.get('image_sha256'))
    assert digest(evidence_path(path))==sha,(row['criterion_id'],'changed row evidence')
 return {'questions':len(coverage),'part_reconciliations':sum(len(t['part_reconciliation'])for t in tables.values()),'rows':sum(len(t['rows'])for t in tables.values())}

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--negative-fixture',choices=['alternatives-summed','missing-award-coverage','absolute-evidence']);arg=parser.parse_args()
 mc=json.loads((A/'marking-conventions.json').read_text())
 if arg.negative_fixture=='alternatives-summed':mc['award_tables'][0]['rows'][0]['alternative_award_aggregation']='sum'
 if arg.negative_fixture=='missing-award-coverage':mc['question_coverage'].pop()
 if arg.negative_fixture=='absolute-evidence':evidence_path(str((WB/'checks/r4/provenance-01.png').resolve()))
 counts=validate_awards(mc)
 assert not arg.negative_fixture,'fixture did not fail'
 scan=json.loads((A/'convention-context-scan-r4.json').read_text());assert scan['counts']['pending_author_disposition']==0
 rules={r['rule_id']:r for r in mc['rules']};aliases={a:r['rule_id']for r in mc['rules']for a in r['historical_rule_ids']}
 rows={r['criterion_id']:r for t in mc['award_tables']for r in t['rows']}
 for hit in scan['native_hits']:
  d=hit['disposition'];assert d['reason'] and d['status']!='pending author disposition'
  assert all(r in rules or r in aliases for r in d['convention_rule_ids'])
 for r in rules.values():
  assert all(x in rows for x in r['award_row_links'])
  assert r['evidence'] and all(digest(evidence_path(e['render_path']))==e['render_sha256']for e in r['evidence'])
 for p in (WB/'checks/r3').glob('*-manifest.json'):
  for entry in json.loads(p.read_text()):
   for key in ['path','evidence_sheet']:
    if key in entry:evidence_path(entry[key])
 provenance=json.loads((A/'nsscas-cambridge-provenance.json').read_text())
 assert len(provenance['matches'])>=31
 assert len(provenance['structural_comparisons_without_source_claim'])==3
 for m in provenance['structural_comparisons_without_source_claim']:assert not m['examination_references']
 for m in provenance['matches']:
  ev=m['rendered_confirmation'];assert digest(evidence_path(ev['path']))==ev['sha256']
  assert m['explains_source_defect']is None or m['explains_source_defect'].startswith('SRC-')
  assert all(r['learner_display']is False for r in m['examination_references'])
 tb=json.loads((A/'textbook-inventory.json').read_text());items={i['item_id']:i for i in tb['items']}
 assert len(items)==len(tb['items']),'duplicate textbook identity'
 reading=json.loads((A/'textbook-reading-r3.json').read_text())
 for lead in reading['discovery_leads']:
  if lead.get('author_disposition'):continue
  for item_id in lead['item_ids']:
   i=items[item_id]
   assert lead['pdf_page']in[i['pdf_page'],*i['continuation_pdf_pages']],('heading linked to different page',item_id)
 for i in items.values():
  assert i['learner_display']is False
  if not i['assessed_8227_demand_ids']:
   if i['scope_check']['status']=='out-of-scope'and (i['disposition'].startswith('exclude:')or i['evidence_role'].startswith('excluded source occurrence')):
    assert i['evidence_role'].startswith('excluded source occurrence')
    assert not i.get('teaches_8227_demand_ids')and not i['component_demand_ids'],'excluded source task acquired coverage'
   else:assert i['evidence_role'].startswith('prerequisite/supporting')
  check=i['answer_key'].get('author_check')
  if check:
   assert check['verification_status']
   assert check['pdf_pages'] or (check.get('record_type','').startswith('author-derived')and check.get('source_pdf_pages')and check.get('answer_check_notes')),'answer check lacks either published location or explicit derived evidence'
   for path in check.get('evidence_sheets',[]):evidence_path(path)
 for d in tb['per_demand']:
  actual={i['item_id']for i in items.values()if d['demand_id']in i['assessed_8227_demand_ids']and i['scope_check']['status']!='out-of-scope'and not i['disposition'].startswith('source ambiguity')}
  assert actual==set(d['item_ids']) and len(actual)==d['textbook_item_count']
 page_audit=json.loads((A/'textbook-page-audit-r4.json').read_text())
 assert page_audit['target_pages']==759 and page_audit['render_read_pages']==759
 assert not page_audit['unread_pdf_pages']
 result={'status':'author structural pass; independent review not implied','awards':counts,'rules':len(rules),'context_scan':scan['counts'],
  'confirmed_provenance_pairs':len(provenance['matches']),
  'textbooks':{'catalogued_items':len(items),'heading_leads':len(reading['discovery_leads']),'unclassified_heading_leads':reading['unclassified_heading_leads'],'target_source_pages_read':page_audit['render_read_pages'],'answer_locator_checks':sum(bool(i['answer_key'].get('author_check',{}).get('pdf_pages'))for i in items.values()),'author_answer_records':sum(bool(i['answer_key'].get('author_check'))for i in items.values())},
  'limits':'Source-derived gaps, prose/table disagreements and unfinished textbook completeness/qualifier/answer accuracy checks remain visible. This does not accept recipes, runtime marking, website or production.'}
 write(WB/'checks/repair-r4-validation.json',result);print(json.dumps(result,indent=2))
if __name__=='__main__':main()
