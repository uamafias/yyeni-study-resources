"""One-time final propagation of source/date repairs and reviewed visual context metadata."""
import copy,json,pathlib
W=pathlib.Path(__file__).resolve().parents[1];D={p:json.loads(p.read_text()) for p in W.glob('topics/*/*/*.json') if p.parent.name in ('content-units','learning-items','claims')};B=copy.deepcopy(D)
O={o.get('block_id',o.get('item_id',o.get('claim_id'))):o for d in D.values() for o in d.get('blocks',d.get('items',d.get('claims',[])))}
replacements={
 '1.3': [('When the volume of water falls, the river has less energy and can no longer carry all its load, so it deposits some of it.','When flow weakens enough to reduce sediment-transport capacity, a river deposits some of its load; water loss can contribute to this, depending on channel conditions.')],
 '1.5': [('Waves are driven by the wind, so they usually approach the shore at the angle of the prevailing wind, and the swash runs diagonally up the beach.','When breaking waves approach the shore obliquely, swash runs diagonally up the beach.'),('Net drift is therefore usually in the general direction of the prevailing wind along that coast.','Local wind can influence wave direction, but distant swell and refraction mean drift cannot always be inferred from the local wind.'),('Waves driven by the prevailing wind approach at an angle','In this wind-generated wave model, waves approach at an angle')],
 '1.6': [('about 1.2 m above the ground in the school model; national weather services use a fixed height between 1.25 m and 2 m','about 1.25 m above short grass; meteorological practice uses a standard height within roughly 1.25–2 m')],
 '2.5': [('Since 2010 a reverse-osmosis plant near Wlotzkasbaken, north of Swakopmund, has supplied water that the national water utility delivers to Swakopmund, nearby uranium mines and other parts of the Erongo Region.','A reverse-osmosis plant near Wlotzkasbaken, north of Swakopmund, opened in 2010. NamWater contracted to receive its desalinated water in 2013; its 2024 report describes the plant supplying the coastal network and uranium mines.'),('because groundwater is available all year and is not lost to evaporation as dam water is','because usable aquifers can retain water through dry periods and are protected from direct open-water evaporation, subject to storage, recharge, quality and abstraction'),('groundwater is not lost to evaporation as dam water is','groundwater stores are protected from direct open-water evaporation, though their reliability depends on recharge, quality and abstraction')]
}
for k,o in O.items():
 for t,pairs in replacements.items():
  if not k.startswith(('CL-6137-'+t,'BL-6137-'+t,'ITEM-6137-'+t)):continue
  for f in ['text','canonical_answer']:
   if f in o:
    for a,b in pairs:o[f]=o[f].replace(a,b)
# Limit status-metadata cleanup to the ten contexts actually re-reviewed.
m=json.loads((W/'assets/asset-manifest-6137.json').read_text());ids={'VIS-6137-'+s for s in ['1.5-05','1.5-06','1.5-07','1.5-08','3.3-01','3.3-02','4.1-01','4.1-02','4.1-03','4.2-03']}
for b in m['item_bindings']:
 if b['resource_id'] in ids:
  o=O[b['item_id']];s=o['context']['situation'];o['context']['situation']=s.replace('Claude, self-reviewed; awaiting Codex visual review','Claude authored; independently reviewed by Codex')
revs={}
for p,d in D.items():
 for old,new in zip(B[p].get('claims',[]),d.get('claims',[])):
  if old['text']!=new['text']:new['revision']+=1;revs[new['claim_id']]=new['revision']
for d in D.values():
 for o in d.get('blocks',d.get('items',[])):
  for cid,rev in revs.items():
   if cid in o.get('claim_ids',[]):o['claims_seen'][cid]=rev;o['reviewed_unchanged']='Codex checked consistency with revised claim; repairs logged separately.'
 if 'blocks' in d:d['word_count']=sum(len(b['text'].split()) for b in d['blocks'])
p=W/'review/codex-crossreview-repairs-6137.json';log=json.loads(p.read_text());log['claim_revisions'].update(revs)
for f,d in D.items():
 if d==B[f]:continue
 for old,new in zip(B[f].get('blocks',B[f].get('items',B[f].get('claims',[]))),d.get('blocks',d.get('items',d.get('claims',[])))):
  if old!=new:log['changes'].append({'path':str(f.relative_to(W)),'id':new.get('block_id',new.get('item_id',new.get('claim_id'))),'before':old,'after':new})
 f.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
p.write_text(json.dumps(log,indent=2,ensure_ascii=False)+'\n');print(len(revs),'additional claim revisions')
