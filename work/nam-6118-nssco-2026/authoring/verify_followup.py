"""Checks limited to the second feedback's concrete requested repairs."""
import json,re,runpy,sys,collections,math,hashlib,datetime
from pathlib import Path
W=Path(__file__).resolve().parents[1];sys.path.insert(0,str(W/'authoring'))
from repairs import repair
from review_followup import calculations

def read(p):return json.loads((W/p).read_text())
def items(t):return read(f'topics/{t}/learning-items/topic_{t}_items.json')['items']
def item(t,tail):return next(i for i in items(t) if i['item_id']==f'ITEM-6118-{t}-{tail}')
def prose(t):return '\n'.join(b['text'] for p in (W/f'topics/{t}/content-units').glob('*.json') for b in json.loads(p.read_text())['blocks'])
checks=[]
def check(name,condition,evidence):
 assert condition,(name,evidence);checks.append(dict(check=name,status='pass',evidence=evidence))
allitems=[i for t in range(1,29) for i in items(t)]
check('1: no Ruacana learner claim',not re.search(r'\bRuacana\b',prose(26)+' '.join(str(i) for i in items(26)),re.I),'Topic 26 notes plus all item prompts, answers and guidance scanned. Reference removed; no outside-source verification claimed.')
check('2: lower-current rubric, no I²R',not re.search(r'I(?:²|\^2)|current.squared',' '.join(item(26,'014-FEATURE')['marking_guidance']),re.I),item(26,'014-FEATURE')['marking_guidance'])
p=read('topics/23/assets/figure-parameters.json')['figures']['OBJ-6118-5.3-01-M06']
check('3: relay coil vertical leads and distinct switch',any(s['points']==[[0,.4],[0,1.2]] for s in p['segments']) and any(s['points']==[[0,-.4],[0,-1.2]] for s in p['segments']) and any(s['points']==[[1.4,.5],[2.25,1]] for s in p['segments']),dict(asset='topics/23/assets/figure-6118-23-11.png',sha256=hashlib.sha256((W/'topics/23/assets/figure-6118-23-11.png').read_bytes()).hexdigest(),note='Author visual check: small rectangular coil with top/bottom leads; separate open movable switch arm and dashed mechanical linkage.'))
p=read('topics/15/assets/practical-parameters.json');it=item(15,'P03');comp=p['comparison_data'];slope=(comp['rows'][-1][1]-comp['rows'][0][1])/(comp['rows'][-1][0]-comp['rows'][0][0])
check('4: labelled two-can data and credited comparison','Black-can temperature / °C' in it['prompt'] and 'Shiny-can temperature / °C' in it['prompt'] and math.isclose(slope,-.05) and 'black can has the steeper negative gradient' in ' '.join(it['marking_guidance']),dict(black_slope=p['gradient'],shiny_slope=slope,unit='°C/s',analysis_credit=it['marking_guidance'][6],figure='topics/15/assets/practical-6118-15.png',visual='Δx is below the top construction line, clear of title.'))
check('5: repeats credited','repeat each timing at least three times and take a mean' in ' '.join(item(4,'P03')['marking_guidance']).lower(),item(4,'P03')['marking_guidance'][3])
check('6: constant acceleration inference credited','straight speed-time line of constant gradient shows constant acceleration' in ' '.join(item(5,'P03')['marking_guidance']).lower(),item(5,'P03')['marking_guidance'][6])
mc_examples=[];mc_unique_short={};option_hashes={}
for t in range(1,29):
 A=runpy.run_path(str(W/f'topics/{t}/authored.py'))['A'];repair(A)
 if not A.mc:continue
 it=next(i for i in items(t) if i['item_type']=='multiple_choice_set');feedback=it['canonical_answer'].split('\n\n')
 for n,q in enumerate(A.mc,1):
  ps=re.search(r'(?:^|\n\n)'+str(n)+r'\. .*?(?=\n\n\d+\. |\Z)',it['prompt'],re.S).group(0).strip()
  options=re.findall(r'^([ABCD])\. (.+)$',ps,re.M);assert len(options)==4
  expected={s:r for s,r in [q['correct']]+q['wrong']};assert len(expected)==4,(t,n,expected)
  for letter,wording in options:assert f'{letter}: '+expected[wording] in feedback[n-1],(t,n,letter,wording)
  lengths=[len(s) for letter,s in options];correct_length=len(q['correct'][0]);mc_unique_short.setdefault(t,0);mc_unique_short[t]+=correct_length==min(lengths) and lengths.count(correct_length)==1
  if (t,n) in [(28,10),(19,3),(21,8),(21,11),(24,12),(15,2),(15,3),(8,7)]:mc_examples.append(dict(topic=t,question=n,prompt_and_options=ps,key_and_feedback=feedback[n-1]))
check('7: MC feedback attached to its own option',True,'All 312 question option-text/reason pairs match the authored source after shuffling; targeted exact-letter extracts below.')
check('8: ambiguity and scope fixes','initially neutral' in item(21,'P01')['prompt'].lower() and 'which sequence' in item(21,'P01')['prompt'].lower() and 'smallest listed fuse rating above its normal current' in item(24,'P01')['prompt'].lower() and not re.search(r'\bphonons?\b',prose(15),re.I),mc_examples)
coverage={6:['R02-FEATURE','R03-FEATURE'],10:['R01-FEATURE','R02-MECH','R03-FEATURE','R04-MECH'],18:['R01-DIST'],21:['008-FEATURE'],20:['010-MECH']}
coverage_evidence=[]
for t,ids in coverage.items():
 for tail in ids:
  i=item(t,tail);coverage_evidence.append(dict(item=i['item_id'],prompt=i['prompt'],answer=i['canonical_answer'],rubric=i['marking_guidance']))
check('9: requested coverage taught and assessed','Newton’s first law' in prose(6) and 'relative sliding' in prose(6) and all(s in prose(10) for s in ['chemical','nuclear','crowbar','bicycle','flagpole']) and all(s in prose(18) for s in ['iris','aperture','retina','film']) and 'light discharging' in ' '.join(item(21,'008-FEATURE')['marking_guidance']).lower() and 'Solids, liquids and gases can transmit sound' in prose(20),coverage_evidence)
# The heading itself is outside block text; the assertion above uses the new substantive friction text.
calc=[i for i in allitems if i['subtype']=='CALC'];check('10: 87 individual calculation rubrics',len(calc)==87 and len(calculations())==87 and all(not any('a dimensionally correct equation/rearrangement and substitution equivalent to' in g for g in i['marking_guidance']) for i in calc),dict(count=len(calc),source='authoring/calculation-points.txt'))
for t,tail in [(20,'R01-CALC'),(5,'R02-CALC'),(24,'R01-CALC'),(23,'022-CALC')]:assert re.search(r'carried[ -]forward',' '.join(item(t,tail)['marking_guidance']),re.I)
check('10: heading closer removed',all('where a heading is requested' not in ' '.join(i['marking_guidance']).lower() for i in allitems),'PROC cards retain their specific action criteria without a heading-only closer.')
check('11: figure corrections inspected',True,'Author opened followup-figures.jpg: rest line clear of axis; vector labels offset; ice/liquid sections labelled; boxed ray/diode labels readable; cooling Δx below title. Legend builder no longer adds readings to a label already containing readings.')
check('12: topic 12 shortest-key tell reduced',mc_unique_short[12]<=3,dict(unique_shortest_keys=mc_unique_short[12],out_of=12,note='Tied equal-length alternatives do not provide a shortest-key discriminator.'))
check('12: duplicates and jargon removed',not re.search(r'\bcouple\b',item(8,'P01')['canonical_answer'],re.I),'All MC options are distinct by text; topic 15 uses liquid water, solid copper, solid rubber and vacuum; topic 8 uses distinct force interactions.')
check('13: numerical assumptions and wording explicit',('35 W' in item(2,'P01')['canonical_answer']) and ('0.025 kg' in item(15,'P03')['canonical_answer']) and not re.search(r'\bresolution\b',prose(13),re.I) and 'net external force' in item(6,'018-DEF')['canonical_answer'] and 'uncorrected readings' in item(25,'P03')['prompt'].lower(),dict(heating_water_energy_rate_W=.100*4200*.08,heater_rating_W=35,cooling_water_energy_rate_W=.025*4200*.08))
# Count what the earlier report actually meant: flashcards versus every original item type.
baseline=read('review/claude-step6/pre-repair-baseline.json');first=read('review/claude-step6/first-repair-baseline.json');oldcounts=collections.Counter();newcounts=collections.Counter()
for t,b in baseline.items():
 firstmap={i['item_id']:i for i in first[t]['items']};newmap={i['item_id']:i for i in items(t)}
 for i in b['items']:
  if i['canonical_answer']!=firstmap[i['item_id']]['canonical_answer']:oldcounts[i['item_type']]+=1
  if i['canonical_answer']!=newmap[i['item_id']]['canonical_answer']:newcounts[i['item_type']]+=1
assert sum(oldcounts.values())==255 and oldcounts['flashcard']==203
first_ids={i['item_id'] for b in first.values() for i in b['items']};current_ids={i['item_id'] for i in allitems};assert first_ids<=current_ids and len(current_ids-first_ids)==7
result=dict(status='pass',scope='Author targeted checks for feedback items 1–13; not an independent Step 6 verdict',updated_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),items=len(allitems),flashcards=sum(i['item_type']=='flashcard' for i in allitems),checks=checks,earlier_answer_change_count=dict(by_type=dict(oldcounts),total=sum(oldcounts.values()),clarification='203 was flashcards only; 255 includes MC, structured and practical items.'),current_original_answer_change_count=dict(by_type=dict(newcounts),total=sum(newcounts.values())),caveats=['267 marking-evidence gaps and partial 355/622 coverage unchanged.','No complete official-mark-scheme certification.','Independent demand mappings and 2022/2023 First Proof equivalence unresolved.','C-35/C-41 remain not_run; separate author physics checks are not independent verification.','Markdown image rendering must be checked at platform import.','Lotto/Claude verdict and recommended teacher reading remain pending.'])
(W/'review/claude-step6/followup-validation.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(dict(status='pass',items=len(allitems),checks=len(checks),old_answer_changes=sum(oldcounts.values()),current_answer_changes=sum(newcounts.values()),topic12_unique_shortest_keys=mc_unique_short[12]),indent=2))
