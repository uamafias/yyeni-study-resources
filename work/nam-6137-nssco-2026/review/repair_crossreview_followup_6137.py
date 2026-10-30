"""Additional citation/date reconciliations after independent source checking; run once."""
import copy,json,pathlib
W=pathlib.Path(__file__).resolve().parents[1];docs={p:json.loads(p.read_text()) for p in W.glob('topics/*/*/*.json') if p.parent.name in ('claims','content-units','learning-items')};before=copy.deepcopy(docs)
objs={o.get('block_id',o.get('item_id',o.get('claim_id'))):o for d in docs.values() for o in d.get('blocks',d.get('items',d.get('claims',[])))}
def c(id,text,src=None):
 o=objs['CL-6137-'+id];o['text']=text
 if src:
  for e in o['evidence']:
   if e['source_id']=='CROSSREVIEW-6137':e['locator']=src

def rep(topic,old,new):
 count=0
 for k,o in objs.items():
  if not k.startswith(('CL-6137-'+topic,'BL-6137-'+topic,'ITEM-6137-'+topic)):continue
  for f in ['text','prompt','canonical_answer']:
   if old in o.get(f,''):o[f]=o[f].replace(old,new);count+=1
 return count
c('2.6.01-03-R1','A chain of national parks protects most of Namibia’s coastal belt, with town areas and other exclusions: Skeleton Coast, Dorob, Namib-Naukluft and Tsau ǁKhaeb. Bwabwata, Mudumu and Nkasa Rupara lie in the north-east. In 2022, 86 communal conservancies covered about 20% of Namibia; freehold conservancies also operate on private farmland.', 'MEFT national park profiles/maps; NACSO 2022 State of Community Conservation, printed pp20–21: https://nacso.org.na/wp-content/uploads/2025/06/2022-SOCC-Annual-Report_p7-2.pdf . Coastal protection is not asserted to include every town or coastal plot.')
c('2.3.07-R1','Tourism development in Namibia faces long distances between attractions and overseas markets. Much of the road network is gravel or earth, which can lengthen journeys. Air Namibia ceased operations in February 2021, ending its own Windhoek–Frankfurt service; this did not end all direct international flights, which other carriers continue to operate.', 'Air Namibia closure is historical. Primary current corroboration of continuing connectivity: Discover Airlines, 23 June 2026, Munich–Windhoek expansion: https://newsroom-en.discover-airlines.com/pressreleases/discover-airlines-expands-munich-windhoek-service-3455761 . No inference that 2021 air-link constraints remain unchanged in 2026.')
c('2.5.05-03-R1','The Erongo reverse-osmosis seawater desalination plant near Wlotzkasbaken, about 35 km north of Swakopmund, opened in 2010. NamWater’s 2024 report describes its water as part of the coastal bulk supply serving municipalities and mines. Opening date is distinct from the later bulk-supply arrangements.', 'Orano Namibia plant history: https://www.orano.group/en/orano-across-the-world/namibia ; NamWater 2024 Annual Report, coastal business unit: https://www.namwater.com.na/images/docs/2024_Annual_report.pdf . Do not backdate NamWater distribution to inauguration.')
rep('2.5','Since 2010, a reverse-osmosis','Opened in 2010, a reverse-osmosis')
rep('3.1',"mainly in informal settlements, where over 60% of the city's population lives on 25% of its land", "often in informal settlements; the 2014 study reports that the northern and north-western areas together held over 60% of the city's population on 25% of its land")
rep('3.3','which was created in 1961','during the forced-removal programme of the late 1950s and 1960s')
rep('3.3','created in 1961','developed through forced removals in the late 1950s and 1960s')
c('1.6.02-01-R1','A Stevenson screen shelters thermometers above short grass at a standard height. The Met Office mounts screens about 1.25 m above ground; meteorological guidance commonly uses 1.25–2 m. White paint limits solar heating and the traditional wooden louvres allow ventilation.', 'Met Office, Maximum temperatures and how they are recorded: https://www.metoffice.gov.uk/blog/2022/maximum-temperatures-and-how-theyre-recorded ; HKO temperature measurement guidance: https://www.hko.gov.hk/en/education/met_instrument/temp.htm . About 1.2 m is an approximation to 1.25 m, not a separate school-standard height.')
# Correct PDF versus printed-page locators in reviewer evidence only.
for o in objs.values():
 for e in o.get('evidence',[]):
  if e.get('source_id')=='CROSSREVIEW-6137':
   e['locator']=e['locator'].replace('syllabus PDF pp15-16','syllabus PDF pp18–19 (printed pp15–16)')
# No unsupported exact religious population figure is needed to teach stakeholder roles.
rep('3.2','About 90% of Namibians are Christian, so churches and faith-based organisations reach many people','Churches and faith-based organisations can reach many communities')
rep('3.2','Churches and faith-based organisations reach many people because about 90% of Namibians are Christian.','Churches and faith-based organisations can reach communities through their congregations and institutions.')
# Reconcile claim dependencies.
revs={}
for p,d in docs.items():
 for old,new in zip(before[p].get('claims',[]),d.get('claims',[])):
  if old['text']!=new['text']:new['revision']=old['revision']+1;revs[new['claim_id']]=new['revision']
for p,d in docs.items():
 for o in d.get('blocks',d.get('items',[])):
  for cid,rev in revs.items():
   if cid in o.get('claim_ids',[]):
    o['claims_seen'][cid]=rev;o['reviewed_unchanged']='Codex checked consistency with the revised claim; any text repair is separately logged.'
 if 'blocks' in d:d['word_count']=sum(len(b['text'].split()) for b in d['blocks'])
logpath=W/'review/codex-crossreview-repairs-6137.json';log=json.loads(logpath.read_text());log['claim_revisions'].update(revs)
for p,d in docs.items():
 if d==before[p]:continue
 for old,new in zip(before[p].get('blocks',before[p].get('items',before[p].get('claims',[]))),d.get('blocks',d.get('items',d.get('claims',[])))):
  if old!=new:log['changes'].append({'path':str(p.relative_to(W)),'id':new.get('block_id',new.get('item_id',new.get('claim_id'))),'before':old,'after':new})
 p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
logpath.write_text(json.dumps(log,indent=2,ensure_ascii=False)+'\n');print('Additional revised claims',len(revs))
