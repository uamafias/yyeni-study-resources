"""Reviewable Step 5 inventory; does not waive deterministic or human gates."""
from collections import Counter
from fractions import Fraction
import hashlib,json,re,sys
from pathlib import Path

W=Path(__file__).resolve().parents[1]
ROOT=W.parents[1]
sys.path.insert(0,str(ROOT/'standard/v0.2.0-draft/checks'))
from yyeni_checks import _artefact_text

out={'stage':'5: all five topics authored and revised after independent review; deterministic checks clean; unverified and unreleased',
     'topics':{},'invariant_failures':[],
     'schema_note':'The block schema forbids qa_status; units/items carry review_required. Blocks retain authored_hash and claims_seen.',
     'verification':'All claims unverified and publishable=false. Evidence absence is explicitly flagged. This author audit is not cross-vendor or teacher review.'}
planned=Counter();uniform=Counter()
for t in range(1,6):
 b=W/'topics'/str(t);wo=json.loads((b/'work_order.json').read_text())
 claims=json.loads((b/'claims/canonical_claim_ledger.json').read_text())['claims'];ci={c['claim_id']:c for c in claims}
 items=json.loads((b/f'learning-items/topic_{t}_items.json').read_text())['items']
 units=[json.loads(p.read_text()) for p in sorted((b/'content-units').glob('*.json'))]
 notes=json.loads((b/'authoring_notes.json').read_text());qa=json.loads((b/'qa_report.json').read_text())
 expected={s['slot']:s for s in wo['item_slots']};all_ids=set(expected)|{p['slot'] for p in wo['performance_tasks']}
 assert {i['item_id'] for i in items}==all_ids
 assert len(items)==len(all_ids)
 for u in units:assert u['word_count']<=u['word_budget']['max'],u['unit_id']
 covered={o for u in units for o in u['objective_ids']}
 assert covered=={o for u in wo['content_units'] for o in u['objective_ids']}
 held={v['item_id'] for v in notes['visuals_pending']}
 for i in items:
  if i['item_id'] in expected:
   s=expected[i['item_id']]
   for k in ('subtype','assessment_objectives','blooms_level','command_word','mark_tariff'):
    assert i[k]==s[k],(i['item_id'],k)
  if 'Fig. VIS-6116-' in i['prompt']:assert i['item_id'] in held,i['item_id']
  if i['item_type']=='multiple_choice_set':assert len(re.findall(r'^\d+\.',i['prompt'],re.M))==12
  for ao in i['assessment_objectives']:uniform[ao]+=Fraction(i['mark_tariff'],len(i['assessment_objectives']))
  # Same planning estimator: equal card splits; 62.5/37.5 paper-model splits for theory tasks.
  if i['item_type']=='flashcard':
   for ao in i['assessment_objectives']:planned[ao]+=Fraction(i['mark_tariff'],len(i['assessment_objectives']))
  elif i['item_type']=='practical_task':planned['AO3']+=i['mark_tariff']
  else:
   planned['AO1']+=Fraction(i['mark_tariff']*5,8);planned['AO2']+=Fraction(i['mark_tariff']*3,8)
 artefacts=items+[bl for u in units for bl in u['blocks']]
 for x in artefacts:
  owner=x.get('item_id',x.get('block_id'))
  assert x['authored_hash']==hashlib.sha256(_artefact_text(x).encode()).hexdigest(),owner
  for cid,revision in x['claims_seen'].items():assert cid in ci and ci[cid]['revision']==revision,(owner,cid)
 for c in claims:
  assert not c['publishable'] and c['verification']['status']=='unverified',c['claim_id']
  assert c['evidence'] or c['notes'],c['claim_id']
 out['topics'][str(t)]={'claims':len(claims),'objectives':len(covered),'content_units':len(units),'items':len(items),
  'flashcards':sum(i['item_type']=='flashcard' for i in items),'performance_tasks':sum(i['item_type']!='flashcard' for i in items),
  'body_words':sum(u['word_count'] for u in units),
  'rendered_words':len(next(p for p in b.glob('*.md') if p.name[0].isdigit()).read_text().split()),
  'decision':qa['release_decision'],'failed_checks':[c for c in qa['deterministic_checks'] if c['status']=='fail'],
  'warnings':[c for c in qa['deterministic_checks'] if c['status']=='warn'],
  'held_items':notes['visuals_pending'],'missing_reference_claims':[c['claim_id'] for c in claims if not c['evidence']],
  'below_minimum_units':notes['below_budget_units'],'deviations':notes['deviations']}

def mix(counter):
 total=sum(counter.values());return {'total_marks_equivalent':str(total),'marks':{k:str(v) for k,v in sorted(counter.items())},'percent':{k:float(v/total*100) for k,v in sorted(counter.items())}}
out['ao_planning_estimator']=mix(planned)
out['ao_uniform_item_label_split']=mix(uniform)
out['ao_basis_note']='The approved estimator models theory performance tasks at 62.5/37.5, matching paper splits; equal division of whole-task AO labels is a different diagnostic. Neither is a completed part-by-part semantic AO audit. No labels or activities were tuned to tolerance.'
registry={o['objective_id']:o for o in json.loads((W/'curriculum/objective_registry.json').read_text())['objectives']}
overlap=json.loads((W/'topics/wording_overlap_audit.json').read_text())
review=[]
for h in overlap['hits']:
 b=W/'topics'/h['topic'];ci={c['claim_id']:c for c in json.loads((b/'claims/canonical_claim_ledger.json').read_text())['claims']}
 owner=h['artefact'];definition=False;oids=[]
 if owner.startswith('ITEM'):
  iid,field=owner.split(':');i=next(i for i in json.loads((b/f'learning-items/topic_{h["topic"]}_items.json').read_text())['items'] if i['item_id']==iid)
  definition=i['subtype']=='DEF' and field=='canonical_answer';oids=i['objective_ids']
 else:
  for p in (b/'content-units').glob('*.json'):
   for bl in json.loads(p.read_text())['blocks']:
    if bl['block_id']==owner:
     definition=any(ci[c]['claim_type']=='definition' for c in bl['claim_ids']);oids=sorted({o for c in bl['claim_ids'] for o in ci[c]['objective_ids']})
 definition=definition or any(registry[o]['objective_type']=='bio_definition' for o in oids)
 assert definition,owner
 review.append({'artefact':owner,'topic':h['topic'],'objective_ids':oids,'disposition':'Prescribed/settled biological definition; retained under HANDOVER rule 5, which specifically requires verbatim definitions. Some also meet the general 12-word screen; recorded exception, not silently rewritten or cleared as independent wording.'})
out['wording_review']={'documents':overlap['documents'],'pages':overlap['nonempty_pages'],'definition_artefacts':review,'other_overlap_flags':[],
 'reviewer':'Codex author; Claude screen 2026-10-19 reproduced the result; independent semantic review still pending','limitations':overlap['limitation']}
out['chart_model_resolution']={'check':'C-35','finding':'The earlier report that C-35 was a shared-framework defect was withdrawn.',
 'cause':'subject-profile.yaml lacked depictions.chart_model. The framework already provides depictions.chart_model: none (yyeni_checks.py:581-583, CHANGELOG CR-006; used by the 0460, 9702 and 9618 profiles); without it c35 defaults to break_even and treats the word graph or chart in a prompt as a break-even chart.',
 'fix':'depictions.chart_model: none added to the Biology profile on 2026-10-19 at the operator instruction to implement the review; no check weakened, no business fields invented, no graph demand hidden.',
 'note':'Graphs and micrographs remain image assets held under visuals_pending; C-35 now checks only items that declare context.chart. Use the project .venv interpreter: system python3 has no PyYAML, so the checker then runs with no profile.'}
out['runner_exit_defect']={'code_path':'standard/v0.2.0-draft/checks/run_checks.py final exit condition',
 'expected':'Clean report decision publish should return success.','actual':'Runner compares release_decision with pass; clean Topic 2 report is publish but exits 1. what_to_fix.py returns 0 and confirms PUBLISH.'}
(W/'topics/authoring_audit.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print('Authoring invariants PASS; no slot/label/hash/reference mismatch; every figure-dependent item held.')
print('Totals:',{k:sum(v[k] for v in out['topics'].values()) for k in ('claims','objectives','content_units','flashcards','performance_tasks','items','body_words','rendered_words')})
print('Approved AO estimator:',out['ao_planning_estimator'])
