"""Activate Vitalis's approved two-map amendment; preserve original scope/history.
Idempotent. Does not author assets, regenerate contracts, publish, or grant acceptance.
"""
from pathlib import Path
import copy,hashlib,json
W=Path(__file__).resolve().parents[1]
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,d):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
PLAN=W/'planning/visual-resource-plan-6137.json'
APPROVAL=W/'planning/map-revision-01-approval-6137.json'
QUOTE='the descriptions looks go lets go ahead with it.. feel free to also find images online and edit those or make changes to them to make it ork but anyways is all upto you in terms of how best you can get the job done'
if APPROVAL.exists():
 a=read(APPROVAL)
 assert sha(PLAN)==a['active_visual_plan_sha256'],'Active plan changed after amendment; do not overwrite'
 print('Map amendment already active:',a['resource_ids']);raise SystemExit(0)
plan=read(PLAN);assert len(plan['resources'])==54
frozen=W/'planning/revisions/map-revision-01-before-6137'
frozen.mkdir(parents=True,exist_ok=True)
for p in [PLAN,W/'planning/plan-approval-manifest-6137.json']:
 (frozen/p.name).write_bytes(p.read_bytes())
base=copy.deepcopy(plan['resources'][0]);added=[];notes_updates={};slots={}
for t in sorted((W/'topics').iterdir()):
 wo=read(t/'work_order.json')
 for s in wo['item_slots']+wo['performance_tasks']:slots[s['slot']]=s
specs=[('2.2','Namibia farming distribution',['013','014','015','016'],[
 'Original thematic map with the four named north-central regions, eastern crop locations, central cattle and southern small-stock patterns, the Otavi–Grootfontein–Tsumeb triangle and sourced irrigated sites.',
 'Schematic vegetables-for-sale inset for card 015, explicitly labelled illustrative; adjacent cultivated plots have no inferred commercial/subsistence purpose.',
 'Use regional evidence to support broad generalisations; do not shade entire regions as exclusively one farming system or infer current project operation from a location.',
 'One common question map and a distinct answer annotation for each of the four bound cards; all named towns/regions required by prompts must be legible.'
 ]),('2.6','Namibia conservation locations',['002'],[
 'Show Etosha as a national-park area, Torra and Salambala as communal-conservancy areas, and the Cheetah Conservation Fund centre near Otjiwarongo as a point.',
 'Use verified gazette coordinates or openly licensed geographic data; explicitly label generalisation/approximation. Do not mistake a point conservation centre for a park boundary.',
 'Full key, north arrow, reliable scale bar, source date, accurate labels and source/licence credit.'
 ])]
for tid,family,nums,requirements in specs:
 notes_path=W/f'topics/{tid}/authoring_notes.json';notes=read(notes_path)
 concern=next(c for c in notes['scope_concerns'] if sorted(i.split('-')[3] for i in c['affected_items'])==sorted(nums))
 ids=sorted(concern['affected_items']);assigned=ids[0];slot=slots[assigned]
 n=max(int(r['resource_id'].rsplit('-',1)[1]) for r in plan['resources'] if r['topic_id']==tid)+1
 rid=f'VIS-6137-{tid}-{n:02d}'
 r=copy.deepcopy(base);r.update(resource_id=rid,topic_id=tid,family=family,assigned_item_id=assigned,objective_id=slot.get('objective_id'),objective_title=slot.get('objective_title'),authoring_method='original software-rendered thematic map from verified reusable geographic layers and sourced thematic evidence',authoring_owner='Claude visual author; Codex independent review',status='approved for authoring; not generated or accepted',question_path=f'assets/images/{assigned}-question.png',answer_path=f'assets/images/{assigned}-answer.png',master_path=f'assets/masters/{assigned}.svg',data_spec_path=f'assets/specs/{assigned}.json',approved_binding_item_ids=ids,scope_revision='map-revision-01')
 r['requirements']+=requirements
 r['source_policy']={'proposal':'authoring/MAP-REPAIR-PROPOSALS-6137.md','preferred_base':'geoBoundaries NAM ADM1 NAM-ADM1-33880854; metadata says Natural Earth / Public Domain, 14 units; validate actual names and geometry before use. Existing Natural Earth outline may be reused.','verified_metadata_url':'https://www.geoboundaries.org/api/current/gbOpen/NAM/ADM1/','adaptation_permission':'Vitalis authorises finding/adapting suitable online images; author must record each actual source and permission. Prefer editable geographic layers over retouching a finished map.','thematic_evidence':'Verify census/Atlas/Agribank farming locations and gazette/MEFT/CCF conservation locations. Original cartographic expression; no examination-map reproduction.'}
 plan['resources'].append(r);added.append(r)
 concern['resolution']={'approved_by':'Vitalis P Haupindi','approval_evidence':QUOTE,'approval_record':'planning/map-revision-01-approval-6137.json','resource_id':rid,'approved_scope':'Proposed map including sourced substitutes and, for farming, the clearly schematic card-015 inset. Authoring and independent review remain outstanding.'}
 concern['status']='scope approved; map authoring, binding and Codex review pending'
 notes_updates[notes_path]=notes
plan['active_revision']='map-revision-01';plan['resource_count']=len(plan['resources']);plan['approval_record']='planning/map-revision-01-approval-6137.json'
assert len(plan['resources'])==56 and len({r['resource_id'] for r in plan['resources']})==56
assert all(i in slots for r in added for i in r['approved_binding_item_ids'])
dump(PLAN,plan)
for p,d in notes_updates.items():dump(p,d)
a={'revision':'map-revision-01','subject':'6137 NSSCO Geography','approved':True,'approved_by':'Vitalis P Haupindi','approval_evidence':QUOTE,'approval_context':'User approved both descriptions after opening the map-proposal document and allowed choice of online images/adaptations. No additional permission is needed for this scope.','scope':'Two additional map resources for five existing cards, including the illustrative vegetable-plot inset; no extra slots or labels.','proposal_sha256':sha(W/'authoring/MAP-REPAIR-PROPOSALS-6137.md'),'before_resource_count':54,'after_resource_count':56,'resource_ids':[r['resource_id'] for r in added],'item_ids':[i for r in added for i in r['approved_binding_item_ids']],'original_approval_manifest_sha256':sha(frozen/'plan-approval-manifest-6137.json'),'previous_visual_plan_sha256':sha(frozen/PLAN.name),'active_visual_plan_sha256':sha(PLAN),'committed':False,'authored':False,'independently_accepted':False,'published':False}
dump(APPROVAL,a)
print('Activated',a['resource_ids'],'for',len(a['item_ids']),'existing cards; total resources',a['after_resource_count'])
