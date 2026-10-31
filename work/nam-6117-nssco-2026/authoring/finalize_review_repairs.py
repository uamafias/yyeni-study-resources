"""Run after topic builders: delivery separation, self-marking protocol and repair lineage.
Baseline backup is optional; source generation and these final repairs are reproducible.
"""
import json,re,sys,hashlib
from pathlib import Path
W=Path(__file__).resolve().parents[1];R=W.parents[1]
sys.path.insert(0,str(R/'standard/v0.2.0-draft/checks'))
from yyeni_checks import _artefact_text
B=Path('/private/tmp/6117-pre-review-repair')
def read(p):return json.loads(p.read_text())
def save(p,d):p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
roles={
 '1':['VIS-6117-1-01','VIS-6117-1-03-blank'],
 '2':['VIS-6117-2-01'],
 '3':['VIS-6117-3-readings','VIS-6117-3-graph-blank'],
 '4':['VIS-6117-4-readings'],
 '6':['VIS-6117-6-blank'],
 '10':['VIS-6117-10-04-learner'],
 '11':['VIS-6117-11-04-learner'],
 '12':['VIS-6117-12-02-learner','VIS-6117-12-03-learner']}
manifest=[];draw=[]
for t in map(str,range(1,13)):
 T=W/'topics'/t
 # Every visual defaults to teacher/answer-only unless explicitly allowed.
 for p in sorted((T/'visuals').glob('*.svg')):
  manifest.append({'file':str(p.relative_to(W)),'role':'learner_stimulus' if p.stem in roles.get(t,[]) else 'teaching_or_answer_only','delivery_rule':'Never attach the whole visual directory to a learner question.'})
 path=T/f'learning-items/topic_{t}_items.json';d=read(path)
 for x in d['items']:
  for vis in ['10-04','11-04','12-01','12-02','12-03']:
   base='VIS-6117-'+vis
   x['prompt']=re.sub(re.escape(base)+r'(?![\w-])',f'![Learner stimulus](visuals/{base}-learner.svg)',x['prompt'])
  if x['context']['facts']:
   x['context']['facts']=[f for f in x['context']['facts'] if not f.startswith('Reference visual')]
  if x['item_type']=='flashcard' and x.get('command_word')=='Draw':
   protocol=' Sketch on paper before revealing the answer. Compare your drawing with every credit point in the marking guidance, awarding only points your drawing shows. Drawing feedback is self-assessed; this text platform does not automatically grade sketches.'
   x['prompt']=x['prompt'].replace(protocol,'')
   if protocol.strip() not in x['context']['facts']:x['context']['facts'].append(protocol.strip())
   draw.append(x['item_id'])
 # Add the safe supplied stimuli to relevant practical tasks, including tasks whose prompt omitted a link.
 for x in d['items']:
  if x['item_type']=='practical_task':
   for vis in roles.get(t,[]):
    if vis not in x['prompt']:x['prompt']+=f'\n\n![Learner stimulus](visuals/{vis}.svg)'
   answer_vis={'10':'VIS-6117-10-04-answer','11':'VIS-6117-11-04-answer','12':'VIS-6117-12-02-answer'}.get(t)
   if answer_vis and answer_vis not in x['canonical_answer']:x['canonical_answer']+=f'\n\n![Answer reference](visuals/{answer_vis}.svg)'
 parts_path=T/'authored_assessment_parts.json';pd=read(parts_path)
 for p in pd['parts']:
  for vis in ['10-04','11-04','12-01','12-02','12-03']:
   p['prompt']=re.sub(re.escape('VIS-6117-'+vis)+r'(?![\w-])',f'![Learner stimulus](visuals/VIS-6117-{vis}-learner.svg)',p['prompt'])
 save(parts_path,pd)
 oldbank={x['item_id']:x for x in read(B/t/f'learning-items/topic_{t}_items.json')['items']} if B.exists() else {}
 ledger_path=T/'claims/canonical_claim_ledger.json';ld=read(ledger_path)
 oldclaims={c['claim_id']:c for c in read(B/t/'claims/canonical_claim_ledger.json')['claims']} if B.exists() else {}
 for c in ld['claims']:
  old=oldclaims.get(c['claim_id'])
  if old:c['revision']=max(c['revision'],old['revision']+(c['text']!=old['text']))
 revisions={c['claim_id']:c['revision'] for c in ld['claims']};save(ledger_path,ld)
 def stamp(x,old):
  x['claims_seen']={c:revisions[c] for c in x.get('claim_ids',[])}
  h=hashlib.sha256(_artefact_text(x).encode()).hexdigest()
  if old and old.get('authored_hash')!=h:
   x['prior_hash']=old['authored_hash'];x['repair_note']='Independent-review repairs: original MC key permutation, direct credit points, corrected wording and separated learner visual assets; claim references refreshed.'
  x['authored_hash']=h
 for x in d['items']:stamp(x,oldbank.get(x['item_id']))
 save(path,d)
 for p in (T/'content-units').glob('*.json'):
  u=read(p);oldpath=B/t/'content-units'/p.name
  oldblocks={b['block_id']:b for b in read(oldpath)['blocks']} if oldpath.exists() else {}
  for b in u['blocks']:stamp(b,oldblocks.get(b['block_id']))
  save(p,u)
 # Preserve manual source clarifications from the earlier authored draft.
 np=T/'authoring_notes.json';nd=read(np)
 if (B/t/'authoring_notes.json').exists():
  od=read(B/t/'authoring_notes.json')
  for k,v in od.items():
   if k not in nd:nd[k]=v
 nd['review_repairs']={'rubrics':'Template prefixes removed. Credit-point meaning requires semantic review; C-16 vocabulary matching is explicitly not_run when unmatched.','drawings':'Paper sketch plus reveal-and-compare credit-point self-assessment; no automated image grading.','visuals':'Only learner_stimulus files in planning/visual-delivery-audit.json may be supplied before answering.'}
 if t=='1':nd['kelvin_verification']='Syllabus PDF viewer p. 10 explicitly gives T/°C + 273.15 = T/K; retain 298.15 K for 25.00 °C.'
 if t=='7':nd['limewater_deviation']='7-P01 qualifies the syllabus shorthand: initial CO2 makes limewater milky; excess CO2 can clear it by forming soluble hydrogen carbonate. This is an author scientific clarification, not an examiner-report allocation.'
 save(np,nd)
save(W/'planning/visual-delivery-audit.json',{'policy':'Default deny for question delivery. Teaching notes and keyed figures are answer material, never blank learner worksheets.','files':manifest,'drawing_cards_with_self_feedback':draw,'limitation':'Role allowlist and separate SVG content prevent the reported panel leaks. Independent visual/scientific review is still required.'})
print('Repaired delivery and lineage for 12 topics;',len(draw),'drawing cards with self-assessment instructions.')
