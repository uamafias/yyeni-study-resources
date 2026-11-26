"""Run the standard local export and include the Physics assets and review status."""
from pathlib import Path
import json,re,shutil,subprocess,sys,datetime,hashlib,collections
W=Path(__file__).resolve().parents[1];ROOT=W.parents[1];OUT=ROOT/'publish'/W.name
def read(p):return json.loads(p.read_text())
def write(p,d):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
approval_path=W/'review/step7-approval.json';approval=read(approval_path) if approval_path.exists() else None
pilot_path=W/'review/pilot-completion.json';pilot=read(pilot_path) if pilot_path.exists() else None
rows=[];counts=collections.Counter();deviations=[];all_ids=[];assets=[]
for n in range(1,29):
 td=W/'topics'/str(n);q=read(td/'qa_report.json');assert q['release_decision']=='publish'
 assert not [c for c in q['deterministic_checks'] if c['status']=='fail']
 wo=read(td/'work_order.json');items=read(td/'learning-items'/f'topic_{n}_items.json')['items'];expected={s['slot'] for s in wo['item_slots']+wo['performance_tasks']}
 actual={i['item_id'] for i in items};assert expected<=actual and len(items)==len(actual),(n,'slot mismatch')
 assert all(re.match(r'ITEM-6118-'+str(n)+r'-R\d{2}-',x) for x in actual-expected),(n,'unexpected repair ID')
 counts.update(i['item_type'] for i in items);all_ids += [i['item_id'] for i in items]
 rows.append(dict(topic_id=str(n),title=read(td/'contract.json')['topic_title'],**q['metrics'],final_check='PUBLISH — zero failed deterministic checks',warnings=[c['check_id'] for c in q['deterministic_checks'] if c['status']=='warn'],not_run=[c['check_id'] for c in q['deterministic_checks'] if c['status']=='not_run']))
 deviations.extend(dict(topic_id=str(n),**d) for d in read(td/'authoring_notes.json')['deviations'])
 for p in sorted((td/'assets').glob('*.png')):assets.append(p)
assert len(all_ids)==len(set(all_ids))
repair=read(W/'review/claude-step6/repair-validation.json');assert repair['status']=='pass' and repair['items']==len(all_ids)
followup=read(W/'review/claude-step6/followup-validation.json');assert followup['status']=='pass' and followup['items']==len(all_ids)
assert counts['multiple_choice_set']==26 and counts['short_answer']==26 and counts['practical_task']==25 and counts['flashcard']>=590,counts
subprocess.run([sys.executable,str(ROOT/'standard/v0.2.0-draft/build/publish_subject.py'),str(W),'--out',str(OUT)],check=True)
for section in ['notes','flashcards']:
 (OUT/section/'assets').mkdir(parents=True,exist_ok=True)
 for p in assets:shutil.copy2(p,OUT/section/'assets'/p.name)
# Resolve every local image reference from the exported material, rather than assuming copy succeeded.
references=[]
for section in ['notes','flashcards']:
 for p in (OUT/section).iterdir():
  if p.is_file():
   for name in re.findall(r'assets/[A-Za-z0-9_.-]+\.png',p.read_text()):
    target=p.parent/name;assert target.is_file(),target;references.append(str(target.relative_to(OUT)))
manifest=read(OUT/'MANIFEST.json');assert not manifest['not_published'] and manifest['totals']['topics']==28
manifest['delivery_status']='Local authoring export for Lotto/Claude review; no platform import or external release.'
manifest['semantic_review']='Claude reviewed the baseline and first repairs; follow-up build prepared for Lotto/Claude verdict'
if approval:
 manifest['delivery_status']='Operator-approved Step 7 repository release; platform import not performed.'
 manifest['semantic_review']='Claude partial cross-review and follow-up feedback, Codex repairs, Lotto approval to proceed to Step 7 on '+approval['decision_date']+'. Review limits retained.'
 manifest['operator_approval']=approval
manifest['item_type_counts']=dict(counts)
if pilot:
 manifest['delivery_status']='Physics pilot complete by operator instruction; 616 new YYeni cards active, 1429 old shared cards archived; open discussions retained.'
 manifest['pilot_completion']=dict(path='review/pilot-completion.json',status=pilot['pilot_status'],totals=pilot['totals'])
manifest['asset_files']=[dict(path='notes/assets/'+p.name,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in assets]
write(OUT/'MANIFEST.json',manifest)
banner=('> **Operator-approved repository release.** Lotto authorised Step 7 on '+approval['decision_date']+'. 693 items across 28 topics; Claude partial cross-review and Codex repair records are retained in review/. All topics have zero failed mechanical checks. Evidence/mapping limits and platform image verification remain open. Platform import has not occurred.\n\n') if approval else '> **Authoring export for review.** All 28 topics have zero failed mechanical checks. Lotto/Claude’s verdict remains pending.\n\n'
if pilot:banner='> **Physics pilot complete by operator instruction.** 616 new flashcards are active on YYeni; all 1,429 old shared cards are archived. The 77 assessment tasks remain repository resources. No learners were assigned or charged. Evidence, mapping, paper-version, chart/rendering and platform-mark discussions remain open in review/pilot-completion.json; operator completion does not clear those caveats.\n\n'
index=OUT/'INDEX.md';index.write_text(banner+index.read_text())
totals=dict(topics=28,claims=sum(r['claim_count'] for r in rows),content_units=sum(r['content_unit_count'] for r in rows),items=len(all_ids),flashcards=counts['flashcard'],mc_sets=26,mc_questions=312,structured_tasks=26,practical_tasks=counts['practical_task'],content_words=sum(r['word_count'] for r in rows),rendered_notes_words=manifest['totals']['notes_words'],original_image_assets=len(assets))
report=dict(qualification_id=W.name,status='repairs_built_ready_for_claude_recheck',updated_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),author='Codex',totals=totals,topics=rows,blocked_topics=[],remaining_topics=[],deviations=deviations,validation=dict(slot_identity_check='All 666 baseline identities retained once; explicitly logged repair supplements added',deterministic_failures=0,local_image_references_checked=len(references),missing_image_assets=0),limitations=['Mechanical publish verdicts are not independent verification of physics or source-to-syllabus judgements.','Claims remain unverified/non-publishable and items remain review_required.','C-18 warns about item-count AO mix; the approved balance is by marks, not card count.','C-26 flags individual content-unit word budgets; depth follows objective needs and notes are not padded to quotas.','Science figures have separate automated repair checks and author visual inspection; shared business-specific C-35/C-41 remain not applicable and are not claimed as passes.','MC internal practice split is estimated at seven A and five B per set rather than alternating seven/eight A; set IDs, A/B labels and tariffs remain approved.','267 entered-marking-evidence gaps, 2022/2023 First Proof equivalence and independent mapping review remain as documented.','Working syllabus approval and the explicitly waived non-major Paper 1 duration conflict stand.','The standard CLI exit-code mismatch is unchanged; actual failed-check lists and what_to_fix govern the result.'],local_export=str(OUT),independent_review='Claude baseline and first-repair feedback implemented; follow-up verdict pending',source_wording_review='Author 12-word answer comparison against transcribed syllabus passed; independent source review pending',git_publication='No authoring commit or push performed',platform_import='not performed')
if approval:
 report.update(status='repository_release_approved',operator_release_approval=approval,independent_review=approval['reviewer'],git_publication='Step 7 commit and push authorised for shared origin/main; session verifies the remote branch SHA after pushing.')
if pilot:
 report.update(status='pilot_complete_with_open_discussions',platform_import='616 new flashcards active; 1429 original shared cards archived; complete inventory verified',pilot_completion=dict(path='review/pilot-completion.json',totals=pilot['totals'],verification=pilot['verification'],open_discussions=pilot['open_discussions']))
 report['git_publication']='Original package published to origin/main at 8c460ecd; final fixes, comparison and pilot handover are on follow-up PR #3, which remains open for Vitalis.'
 report['limitations']=[x.replace('remain not applicable and are not claimed as passes','remain not_run and are not claimed as passes') for x in report['limitations']]
write(W/'authoring/progress.json',report);write(OUT/'BUILD-REPORT.json',report)
(OUT/'review').mkdir(exist_ok=True)
for name in ['REPAIR-LOG.md','repair-validation.json','followup-validation.json','followup-figures.jpg','card-change-counts.json','what-to-fix-results.json']:
 shutil.copy2(W/'review/claude-step6'/name,OUT/'review'/name)
if approval:shutil.copy2(approval_path,OUT/'review/step7-approval.json')
if pilot:
 for name in ['pilot-completion.json','yyeni-imported-ids.json','yyeni-lesson-map.json']:shutil.copy2(W/'review'/name,OUT/'review'/name)
comparison_path=W/'review/yyeni-card-comparison.json'
if comparison_path.exists():
 comparison=read(comparison_path);shutil.copy2(comparison_path,OUT/'review/yyeni-card-comparison.json')
 report['yyeni_card_comparison']=dict(path='review/yyeni-card-comparison.json',scope=comparison['scope'],totals=comparison['totals'])
 write(W/'authoring/progress.json',report);write(OUT/'BUILD-REPORT.json',report)
print(json.dumps(totals,indent=2))
