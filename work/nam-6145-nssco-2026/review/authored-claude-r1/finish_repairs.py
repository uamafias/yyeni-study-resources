"""Verify repairs, retain explicit resolutions and regenerate local publication."""
import hashlib,json,subprocess,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent;WS=HERE.parents[1];ROOT=WS.parents[1]
read=lambda p:json.loads(p.read_text())
def save(p,d):p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
res={
'6145-AUTH-R1-001':'Replaced every supply-shift contraction reference in learner blocks, prompts, answers, guidance and the causal claim with decrease or leftward shift. Added precise extension/contraction terminology for movements along demand and supply. Revised claim 3.2-020, updated citing revisions and restamped changed derivatives.',
'6145-AUTH-R1-002':'Expanded central-bank teaching into named currency issue, government banking, interbank settlement, conditional emergency liquidity, reserve management and monetary-policy functions with descriptions and primary Bank of Namibia sources. Revised claim 2.3-019 and made the existing FEATURE and short-answer role contrasts concrete without changing slot labels.',
'6145-AUTH-R1-003':'Named unlimited liability in the sole-proprietor notes and relevant answers, retaining the qualification about applicable enforcement rules. Revised supporting claim 2.1-008 and advanced its citations, recording unchanged correct derivatives explicitly.',
'6145-AUTH-R1-004':'Restored depreciation as the familiar productive-capital term in non-currency teaching and a dedicated explanatory block. Kept currency-free wording separate from numeric factor-income examples to avoid a false currency-condition match. Shortened the GNP and National Income model definitions while retaining accounting qualifications in notes.',
'6145-AUTH-R1-005':'Replaced generic marking guidance on 89 affected cards with individually written credit points from each actual question and answer. Every point has an explicit one-mark allocation, and four- and seven-mark responses retain their required mechanism or evaluation architecture and unchanged tariffs.',
'6145-AUTH-R1-006':'Reworded the topic 3.2 cross-reference to say that 6.3 examines other reasons and methods of intervention in business, without implying further price-control teaching there.',
'6145-AUTH-R1-007':'Replaced the definition-cue misconception prompt with an expanded firm facing coordination delays and unit costs rising from N$8 to N$11. The answer now diagnoses the scenario as long-run diseconomies and distinguishes fixed-input diminishing returns.',
'6145-AUTH-R1-008':'Shortened the one-mark fertility answer to a measure of births per woman and made its credit point distinguish the whole-population birth-rate denominator. The notes retain the detailed general and total fertility distinctions.'}
save(HERE/'RESOLUTIONS.json',res)
repairs=read(HERE/'REPAIRS.json')
frozen=read(HERE/'FROZEN.json')
for p,h in frozen.items():
 if p.endswith(('contract.json','work_order.json')):assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
for t in repairs['topics']:
 path=HERE/(t+'-review.yaml')
 if path.exists():
  subprocess.run([sys.executable,str(ROOT/'standard/v0.2.0-draft/checks/ingest_review.py'),str(WS),t,str(path),str(HERE/'RESOLUTIONS.json')],cwd=ROOT,check=True,capture_output=True,text=True)
 subprocess.run([sys.executable,str(ROOT/'standard/v0.2.0-draft/checks/run_checks.py'),str(WS),t,'--quiet'],cwd=ROOT,capture_output=True,text=True)
 q=read(WS/'topics'/t/'qa_report.json');fails=[x for x in q['deterministic_checks'] if x['status']=='fail']
 assert q['release_decision']=='publish' and not fails,(t,fails)
rows=[];ids=set();objectives=set();types={};openissues=[]
for td in sorted((WS/'topics').iterdir(),key=lambda p:list(map(int,p.name.split('.')))):
 if not td.is_dir():continue
 wo=read(td/'work_order.json');q=read(td/'qa_report.json');note=read(td/'authoring_notes.json')
 assert q['release_decision']=='publish'
 for r in q['semantic_reviews']:
  openissues.extend(i['issue_id'] for i in r.get('issues',[]) if i['status'] not in ['resolved','rejected'])
 slots={s['slot']:s for s in wo['item_slots']+wo['performance_tasks']}
 items=read(td/wo['output_files']['learning_items'])['items'];assert len(items)==len(slots)
 for i in items:
  sid=i['item_id'];assert sid not in ids;ids.add(sid);s=slots[sid]
  for key in ['command_word','mark_tariff','blooms_level','assessment_objectives']:assert i[key]==s[key],(sid,key)
  assert i['subtype']==s.get('subtype') and i['item_type']==s.get('item_type','flashcard')
  assert set(i['objective_ids'])==set(s.get('objective_ids') or [s['objective_id']])
  objectives.update(i['objective_ids']);types[i['item_type']]=types.get(i['item_type'],0)+1
 rows.append({'topic':td.name,**note['counts'],'deterministic_failures':0,'warning_checks':[x['check_id'] for x in q['deterministic_checks'] if x['status']=='warn'],'not_run_checks':[x['check_id'] for x in q['deterministic_checks'] if x['status']=='not_run']})
assert not openissues,openissues
assert len(ids)==458 and len(objectives)==197 and types['flashcard']==378
totals={k:sum(r[k] for r in rows) for k in ['claims','units','items','notes_words']}
save(WS/'authoring-progress.json',{'completed_topics':28,'required_topics':28,'rows':rows,'totals':totals,'note':'Claude authored-subject r1 complete. All eight findings addressed by Codex at Jeremy’s request and recorded as author resolutions; no claim of a second independent review.'})
subprocess.run([sys.executable,str(ROOT/'standard/v0.2.0-draft/build/publish_subject.py'),str(WS)],cwd=ROOT,check=True)
pub=ROOT/'publish'/WS.name;manifest=read(pub/'MANIFEST.json')
assert manifest['totals']['items']==458 and manifest['totals']['topics']==28 and not manifest['not_published']
for r in manifest['topics']:
 assert r['open_review_issues']==0
 assert (pub/'notes'/r['notes']).read_bytes()==(WS/'topics'/r['topic_id']/r['notes']).read_bytes()
 source=read(WS/'topics'/r['topic_id']/('learning-items/topic_'+r['topic_id']+'_items.json'))['items']
 published=read(pub/'flashcards'/r['flashcards'])['items']
 assert [{k:v for k,v in i.items() if k!='objective_titles'} for i in published]==source
repairs.update({'status':'All eight findings addressed; deterministic qualification passes and local publication refreshed. Author resolutions, not a second independent review.','resolutions':res,'optional_improvements':['Added shift-direction arrow reminder.','Added television and leaflet examples with audience and budget conditions.'],'verification':{'topics_publish':28,'objectives':197,'totals':totals,'rendered_notes_words':manifest['totals']['notes_words'],'unique_open_issues':0,'item_types':types,'approved_slot_metadata_preserved':True,'curriculum_contracts_work_orders_changed':False}})
save(HERE/'REPAIRS.json',repairs)
lines=['# Claude authored-review repairs — 6145 Economics','',
 'Jeremy authorised all improvements on 8 November 2026. All eight findings are addressed; 89 specific rubrics replace generic guidance. Three supporting claims advance from revision 1 to revision 2, with citing records updated and the required unchanged-text rationale retained.','']
for key,value in res.items():lines+=['## '+key,'',value,'']
lines+=['## Verification','',f"All 28 topics PUBLISH with zero deterministic failures. The approved 197 objectives, 378 flashcards, 80 tasks and all slot labels remain unchanged. Updated content words: {totals['notes_words']:,}; rendered words: {manifest['totals']['notes_words']:,}. Published notes and item payloads match canonical sources. No open review issues remain.",'',
 'Copied-wording scan: no 12-word run; the one standard 8-word exchange-rate phrase is retained as Claude accepted. C18 item-count warnings and C35/C41/C43 not_run limits remain unchanged.','',
 'Two optional reminders were also added: arrows for curve shifts and television/leaflet advertising media. No curriculum, contract, work order, source or standard-tool edits.','',
 'This is the author’s documented repair completion, not a new Claude verdict. Claims are not automatically marked independently verified. Initial build_authored.py files remain pre-review snapshots; repaired canonical JSON is protected against accidental overwrite and maintained through restamp/render/check tools. No push or upload performed.']
(HERE/'REPAIRS.md').write_text('\n'.join(lines)+'\n')
# Preserve original completion report as a historical snapshot, then append current state.
p=WS/'AUTHORING-REPORT.md';text=p.read_text();text+='\n\n## Post-review repair completion — 8 November 2026\n\n'+f"Claude r1: PUBLISH with two medium and six low findings. All eight are now addressed by author resolutions. All 28 topics still PUBLISH; 458 items and 197 objectives preserved. Current content words {totals['notes_words']:,}; rendered words {manifest['totals']['notes_words']:,}. See review/authored-claude-r1/REPAIRS.md and RESOLUTIONS.json. No second independent review, push or upload is implied.\n";p.write_text(text)
p=WS/'STATUS.md';text=p.read_text();text=text.replace('2 medium and 6 low findings remain open','2 medium and 6 low findings addressed by author resolutions on 2026-11-08')
start=text.index('## Next step');end=text.index('## Decisions',start)
text=text[:start]+f'''## Next step

Claude authored-subject review r1 is complete: PUBLISH, no plan rebuild. Jeremy requested all improvements; all eight findings are addressed in canonical learner content and recorded through the standard resolution workflow. See review/authored-claude-r1/REPAIRS.md. All 28 topics PUBLISH, 197 objectives, 378 flashcards plus 80 tasks, {totals['notes_words']:,} content words and {manifest['totals']['notes_words']:,} rendered words. No open review issues remain. This is author repair completion rather than a second Claude verdict.

Jeremy's review-verdict-read and final commit/push checkpoints remain unticked. Local authored checkpoint before review is 97573395. No repair commit, push or upload has been made.

'''+text[end:]
text+='\n- 2026-11-08 — Jeremy instructed “make those improvements”. All eight Claude findings and both optional reminders addressed; three claim revisions and 89 item-specific rubrics recorded. Affected topics restamped, rendered and checked; all 28 PUBLISH. Review resolutions ingested and local publication refreshed, with zero open issues and no scope/slot changes.\n'
p.write_text(text)
print(json.dumps({'issues_resolved':8,'rubrics':89,'topics_publish':28,'totals':totals,'rendered_words':manifest['totals']['notes_words']}))
