"""One-time Codex repairs of final-resource review findings. Return these diffs to Claude; no self-acceptance."""
from pathlib import Path
import json,copy
W=Path(__file__).resolve().parents[1]
D={p:json.loads(p.read_text()) for p in W.glob('topics/*/*/*.json') if p.parent.name in ['claims','content-units','learning-items']};B=copy.deepcopy(D)
objects={o.get('claim_id',o.get('block_id',o.get('item_id'))):o for d in D.values() for o in d.get('claims',d.get('blocks',d.get('items',[])))}
# Use one measured dated supply share instead of choosing a denominator for an ambiguous summary.
c=objects['CL-6137-2.4.04-R1'];c['text']="Ruacana on the Kunene River is a run-of-river hydroelectric station. In 2018/19 it supplied 26% of all electricity used in Namibia, according to the Atlas of Namibia energy chapter. Its output depends strongly on river flow and can fall during low-flow periods, increasing the need for other generation or imports."
c['evidence'].append({'source_id':'CODEX-FINAL-6137','locator':'Atlas of Namibia, Energy, figure 10.22 and accompanying text: https://atlasofnamibia.online/chapter-10/energy . The dated 2018/19 total-use share is distinguished from the historical 95% share of local grid generation before 2016.','support_type':'corroboration'})
b=objects['BL-6137-2.4.04-03'];b['text']="Ruacana on the Kunene River is Namibia's named hydroelectric example. It is a run-of-river station with little storage, so output depends strongly on river flow. The Kunene rises in Angola and its catchment rainfall affects the supply. In 2018/19 Ruacana contributed 26% of all electricity used in Namibia. This is a dated share of total use, including imported electricity, rather than a share of local generation alone. When flow is low, Namibia needs more power from other stations or imports."
i=objects['ITEM-6137-2.4-025-EVAL'];i['canonical_answer']=i['canonical_answer'].replace(", and the Kunene supplies up to 45 per cent of Namibia's electricity",'; in 2018/19 it supplied 26% of all electricity used in Namibia')
# 51.6% is a monthly observation, not an annual total.
for o in objects.values():
 for f in ['text','canonical_answer']:
  if f not in o:continue
  o[f]=o[f].replace('and local plants supplied about half (51.6%) in 2025','and in December 2025 local generation supplied 51.6% of electricity supplied to the domestic economy').replace('in 2025 local plants supplied about half (51.6%)','in December 2025 local generation accounted for 51.6% of electricity supplied to the domestic economy')
c=objects['CL-6137-2.4.10-R1'];c['evidence'].append({'source_id':'CODEX-FINAL-6137','locator':'Namibia Statistics Agency, Electricity December 2025, PDF p2: 213957 MWh local / (213957+201024) MWh supply = 51.6%, monthly not annual. https://nsa.org.na/wp-content/uploads/2026/02/Electricity_December-2025.pdf','support_type':'corroboration'})
# Distance is the measured explanatory variable; accumulated visitor use was not observed.
i=objects['ITEM-6137-2.3-P05'];i['canonical_answer']=i['canonical_answer'].replace('Distance only stands in for use: the survey does not measure how many people have walked the path over the years','The survey compares distance with present path form; it does not measure visitor numbers, years of use or change over time')
i['marking_guidance']=[s.replace('the limit that distance only stands in for years of use','the limit that distance does not itself measure visitor use or erosion through time') for s in i['marking_guidance']]
revs={}
for p,d in D.items():
 for old,new in zip(B[p].get('claims',[]),d.get('claims',[])):
  if old['text']!=new['text']:new['revision']+=1;revs[new['claim_id']]=new['revision']
for d in D.values():
 for o in d.get('blocks',d.get('items',[])):
  for cid,rev in revs.items():
   if cid in o.get('claim_ids',[]):o['claims_seen'][cid]=rev;o['reviewed_unchanged']='Codex checked consistency with the revised dated electricity statistic; any text changes are separately logged for Claude.'
 if 'blocks' in d:d['word_count']=sum(len(b['text'].split()) for b in d['blocks'])
changes=[]
for p,d in D.items():
 if d==B[p]:continue
 for old,new in zip(B[p].get('claims',B[p].get('blocks',B[p].get('items',[]))),d.get('claims',d.get('blocks',d.get('items',[])))):
  if old!=new:changes.append({'path':str(p.relative_to(W)),'id':new.get('claim_id',new.get('block_id',new.get('item_id'))),'before':old,'after':new})
 p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
code=W/'assets/code/r_2_3_01.py';s=code.read_text();assert "('Facilities clean', 'Facilities broken')" in s;code.write_text(s.replace("('Facilities clean', 'Facilities broken')","('Facilities clean', 'Facilities dirty')"))
(W/'review/codex-final-resource-repairs-6137.json').write_text(json.dumps({'reviewer':'Codex','changes':changes,'claim_revisions':revs,'renderer_change':{'path':'assets/code/r_2_3_01.py','old':"('Facilities clean', 'Facilities broken')",'new':"('Facilities clean', 'Facilities dirty')"},'needs_cross_vendor_review':True},indent=2,ensure_ascii=False)+'\n')
print(len(changes),'objects changed; revised claims',revs)
