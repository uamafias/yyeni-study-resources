"""Audit saved draft coverage and source copying without treating drafts as reviewed."""
from pathlib import Path
from collections import Counter,defaultdict
import json,re,hashlib
W=Path(__file__).resolve().parents[1]
def read(p):return json.loads(p.read_text())
def tokens(s):return re.findall(r"[a-z0-9]+(?:'[a-z]+)?",s.lower())
def audit():
 report={'scope':'Saved authored drafts only; not whole-subject semantic approval','topics':[],'failures':[],'mandatory_visuals_pending':[],'copied_runs_12_plus':[]}
 official={}
 for p in (W/'assessment-evidence/extracted').glob('*.txt'):
  if '.compact.' in p.name:continue
  words=tokens(p.read_text());
  for n in range(max(0,len(words)-11)):official.setdefault(tuple(words[n:n+12]),p.name)
 visuals=read(W/'planning/visual-resource-plan-6137.json')['resources']
 framework={c['word']:c for c in read(W/'curriculum/assessment-framework.json')['command_words']}
 for td in sorted((W/'topics').iterdir(),key=lambda p:tuple(map(int,p.name.split('.')))):
  ip=td/'learning-items'/('topic_'+td.name+'_items.json')
  if not ip.exists():continue
  items=read(ip)['items'];wo=read(td/'work_order.json');slots=wo['item_slots']+wo['performance_tasks'];lookup={i['item_id']:i for i in items};claims=read(td/'claims/canonical_claim_ledger.json')['claims'];cids={c['claim_id'] for c in claims}
  assert len(items)==len(lookup)==len(slots)
  for s in slots:
   assert s['slot'] in lookup,s['slot'];i=lookup[s['slot']]
   for k in ['subtype','assessment_objectives','blooms_level','command_word','mark_tariff','item_type']:
    if k in s:assert i[k]==s[k],(i['item_id'],k)
   assert set(i['claim_ids'])<=cids
  specs=read(td/'authoring_notes.json').get('performance_parts',{})
  for itemid,spec in specs.items():
   parttotals=Counter()
   for part in spec['parts']:
    parttotals[part['ao']]+=part['mark_tariff'];command=framework[part['command_word']];assert command['use_in_prompts'] and str(part['mark_tariff']) in command['observed_tariffs'],(itemid,part)
   assert dict(parttotals)==spec['ao_split'],itemid
   assert sum(parttotals.values())==lookup[itemid]['mark_tariff'],itemid
  units=[read(td/u['file']) for u in wo['content_units']]
  assert all(u['word_budget']['min']<=u['word_count']<=u['word_budget']['max'] for u in units)
  qa=read(td/'qa_report.json');fails=[c for c in qa['deterministic_checks'] if c['status']=='fail'];assert not fails
  pending=[r['resource_id'] for r in visuals if r['topic_id']==td.name and not (W/r['question_path']).exists()]
  report['mandatory_visuals_pending']+=pending
  report['topics'].append({'topic_id':td.name,'claims':len(claims),'content_units':len(units),'flashcards':sum(i['item_type']=='flashcard' for i in items),'practice_packages':sum(i['item_type']!='flashcard' for i in items),'items':len(items),'notes_words':len((td/wo['output_files']['notes']).read_text().split()),'deterministic_decision':qa['release_decision'],'check_statuses':dict(Counter(c['status'] for c in qa['deterministic_checks'])),'complete_for_review':not pending,'all_claims_unverified':all(c['verification']['status']=='unverified' and not c['publishable'] for c in claims)})
  texts=[(b['block_id'],b['text']) for u in units for b in u['blocks']]+[(i['item_id'],i['prompt']+' '+i['canonical_answer']+' '+' '.join(i['marking_guidance'])) for i in items]
  for owner,text in texts:
   words=tokens(text)
   matches={(' '.join(words[n:n+12]),official[tuple(words[n:n+12])]) for n in range(max(0,len(words)-11)) if tuple(words[n:n+12]) in official}
   for phrase,source in sorted(matches):report['copied_runs_12_plus'].append({'owner':owner,'phrase':phrase,'source':source})
 report['total_authored_items']=sum(t['items'] for t in report['topics']);report['planned_items']=801;report['unwritten_items']=801-report['total_authored_items'];report['authored_topics']=len(report['topics']);report['planned_topics']=18
 report['result']='DRAFTS_RECONCILE' if not report['copied_runs_12_plus'] else 'COPY_REVIEW_REQUIRED'
 (W/'authoring/draft-audit-6137.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report,ensure_ascii=False,indent=2));return report
if __name__=='__main__':audit()
