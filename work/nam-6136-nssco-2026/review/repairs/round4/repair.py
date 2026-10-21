"""Fix all round-four findings from an immutable snapshot; no network/model calls."""
import copy,hashlib,json,re,shutil,sys
from pathlib import Path
OUT=Path(__file__).resolve().parent;WS=OUT.parents[2];REPO=WS.parents[1]
sys.path.insert(0,str(REPO/'standard/v0.2.0-draft/checks'))
from yyeni_checks import _artefact_text
def read(p):return json.loads(p.read_text())
def dump(p,d):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
def snap(p):
 b=OUT/'baseline'/p.relative_to(WS)
 if not b.exists():b.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,b)
 return read(b)
D={}
for td in sorted(p for p in (WS/'topics').iterdir() if (p/'contract.json').exists()):
 ip=next((td/'learning-items').glob('topic_*_items.json'));lp=td/'claims/canonical_claim_ledger.json'
 D[td.name]={'td':td,'ip':ip,'lp':lp,'items':snap(ip),'claims':snap(lp),'units':{p.name:snap(p) for p in (td/'content-units').glob('*.json')},'notes':snap(td/'authoring_notes.json')}
def it(t,n):return next(i for i in D[t]['items']['items'] if i['item_id'].split('-')[3]==str(n).zfill(3))
def bl(t,u,n):return next(b for b in D[t]['units'][f'CU-6136-{t}.{u:02d}.json']['blocks'] if b['block_id'].endswith('-'+str(n).zfill(2)))

# F1: both adjacent blocks refer to this one complete, independent worked dataset.
bl('7.1',6,4)['text']='This fictional worked example uses percentages of each population’s total, not percentages within each sex. Population C has 36% aged 0–14, 56% aged 15–64 and 8% aged 65 or over. Population D has 24%, 58% and 18% in the same bands. C has the larger young share; D has the larger older share. These differences can inform school and older-age service planning, without implying that everyone in either age group has identical needs.'
bl('7.1',6,5)['text']='The complete age-sex table for this worked example is: C, 0–14 male 18% female 18%, 15–64 male 28% female 28%, 65+ male 4% female 4%; D, 0–14 male 12% female 12%, 15–64 male 29% female 29%, 65+ male 9% female 9%. Each population totals 100%. Draw age groups vertically, youngest at the bottom, with males left and females right on equal horizontal percentage scales. C’s bar lengths on each side are 18%, 28% and 4%; D’s are 12%, 29% and 9%, in the same age order. Add a title, age labels, units and sex key. These broad age groups show grouped shares rather than exact year-by-year patterns. Use finer equal-width age bands for detailed age comparisons. No unseen plotted image is claimed verified.'

# F2: remove answer giveaways and use independent numbers in ALL related notes.
b=bl('3.1',10,5)
b['text']=b['text'].replace('For separate practice, 450 of 1,500 is 30%, 360 of 1,200 is 30%, and 560 of 1,400 is 40%. ','')
b=bl('10.1',10,4)
b['text']=b['text'].replace('For 60 households and 12 places, interval is five; a fair start among positions one to five can produce a reproducible selection.','For 48 households and 12 places, interval is four; choose the start fairly among positions one to four, then take every fourth entry.')
c=next(c for c in D['10.1']['claims']['claims'] if c['claim_id']=='CLM-6136-10.1-10-03-02')
c['text']='For 48 households and 12 places, interval is four; a fair start among positions one to four supports a reproducible selection. A repeating list pattern may bias the sample.'
bl('10.1',10,6)['text']='For this separate worked example, a list of 48 households and a sample of 12 gives interval 48 ÷ 12 = 4. A fair starting position of 2 produces 2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42 and 46. For two fictional villages of 30 and 15 households, a proportional sample of 9 allocates 6 and 3 places: 30/45 × 9 and 15/45 × 9. Randomly select within each village. For a list of 24 schools, a fair draw of four distinct numbers is random selection; the sample is the selected schools, while the draw is the method. Record refusals and limitations of the lists.'
bl('10.1',11,6)['text']='For a separate worked pie example, 20 journeys comprise 8 walking, 7 cycling and 5 using a bus. Their sector angles are 144°, 126° and 90°: divide each count by 20 and multiply by 360°. The angles total 360°. For production-cost shares of 50%, 30% and 20%, a 15 cm divided rectangle has sections 7.5, 4.5 and 3 cm, with boundaries at 7.5 and 12 cm. Label the whole, categories and period. A separate sketch-map example has a north–south road, a clinic at its north end, a bus stop midway and a reading room east of its south end; use symbols, a key, orientation and title, without implying measured scale. A research-process flow chart links question, planning/ethics, pilot, collection, presentation and conclusion; a pilot decision can loop back to revision. Arrows show procedure, not quantities. These specifications do not verify an unseen plotted figure.'

# F3: restore the comparison specified by the objective, in its existing slot.
i=it('2.2',3)
i['prompt']='Differentiate short-term and long-term development planning in their time horizon and level of action.'
i['canonical_answer']='Short-term planning sets nearer, detailed actions and immediate resource responsibilities. Long-term planning sets a broader direction and outcomes over a longer horizon; near-term actions should contribute to that direction.'
i['marking_guidance']=['Comparison, 2 marks: contrast the nearer implementation/action horizon with the longer strategic direction, and distinguish detailed immediate arrangements from broader intended outcomes. Separate descriptions must form an explicit contrast; accept equivalent accurate wording.','Original indicative practice guidance; not an official mark scheme.']

# F5: make the B-only performance task unmistakably source interpretation.
i=it('2.2','P02')
i['prompt']='Describe (a) how these three fictional programme results differ in progress towards their stated aims [3]. Under the HPP effective-governance pillar (accountable decisions), all 4 promised spending reports were published. Under economic advancement (productive opportunities), 8 trainees entered paid work against a target of 20. Under infrastructure development (usable networks), 6 workshop electricity connections were installed but only 2 function. Suggest (b) an immediate response where four training centres have opened but only one has regular tutors and attendance has not improved; qualified tutors can be reassigned within the available budget [3].'
i['canonical_answer']='(a) Publication meets the stated reporting target, supporting transparency without establishing success in every aspect of governance. The 8 recorded work outcomes fall short of the target of 20, so employment progress is incomplete. Six installed connections overstate usable provision because only two function; construction and actual access differ. (b) Reassign suitable tutors to the operating centres and publish a reliable timetable, checking their availability and effects on other centres. This makes existing space more usable. Monitor attendance and learning access to check whether the delivery barrier improves.'
i['marking_guidance']=['Evidence (a), 3 marks: interpret each supplied result against its stated target or usable-service aim: reporting target met, work target not met, and installed networks exceeding functioning networks. Award one distinct, supported interpretation for each; merely naming or defining a pillar earns no interpretation credit.','Meaning (b), up to 3 marks: propose feasible tutor/timetable arrangements, explain the link to usable training and state a relevant monitoring measure within the supplied resources.','Original indicative practice guidance; not an official mark scheme.']
i=it('10.1','P02')
i['prompt']=i['prompt'].replace('Consenting growers answer an interviewer’s neutral price questions','A researcher asks each consenting grower the same neutral price questions aloud and records their spoken answers')
i['prompt']=i['prompt'].replace('Name and describe interview and observation for the two data needs.','Name and describe the two collection methods used for price answers and permitted output records.')

# F4: item-specific scoring criteria, not copied answers or generic mechanisms.
CRITERIA={
'5.1-032':('explain how lost cover and rainfall allow runoff to remove topsoil','link reduced productive soil to poorer growth or an appropriate protective response'),
'5.1-033':('connect vegetation clearance to reduced protection and movement of soil in runoff','identify loss at the original site or deposition affecting the lower field'),
'5.1-034':('compare harvesting with replacement through regrowth and establish a net annual loss of 55 trees','link continued stock decline to later fuel availability'),
'5.1-035':('identify loss of the growing medium rather than seed quantity as the stated constraint','explain why extra seed alone leaves that constraint unresolved'),
'5.1-036':('trace waste from its location through rain runoff into the shared supply','identify downstream water-use consequences or a matched pollution-prevention route'),
'5.1-037':('link habitat clearance to fewer suitable nesting opportunities','bound the observed bird-use change rather than infer changes to every species'),
'5.1-038':('derive a 20-unit loss reduction and connect it to water reaching crops','retain maintenance and farmers’ access conditions for the livelihood benefit'),
'5.1-041':('identify shared public provision of a usable market route','link timely produce delivery to possible sales or reduced spoilage'),
'5.1-042':('identify how members can check recorded contributions or spending','link scrutiny to fewer disputes, trust or continued participation'),
'5.1-043':('identify a scale-related finance or technical limitation of the neighbour group','explain the need for a maintenance actor capable of the wider task'),
'5.1-044':('identify suitable ground cover as an action available to the farmer','explain how reduced soil exposure protects later productive capacity'),
'5.1-045':('identify how consultation obtains evidence of varied local preferences','link adapting arrangements to relevant participation without assuming one representative speaks for everyone'),
'6.1-013':('trace exclusion from training to inability to obtain the required certificate','link the certification barrier to narrower eligibility for the stated jobs'),
'6.1-014':('identify insecure access despite the work already invested','link possible removal before harvest to lost benefit or weaker incentive to improve the land'),
'6.1-015':('identify overlap between paid hours and unchanged caring duties','explain why income opportunity need not remove workload or attendance barriers'),
'6.1-016':('connect departure to fewer workers available for planting','explain how low transfers leave added workload or delayed tasks uncompensated'),
'6.1-017':('connect loss of food plots to greater dependence on purchases','link lack of control over crop income to restricted household or individual choices'),
'6.2-012':('use documented organising to challenge the claim that women’s leadership lacks precedent','explain its relevance to voice while separating historical contribution from current equality'),
'6.2-013':('identify that binding resource choices precede consultation','explain why attendance after decisions offers limited substantive influence'),
'6.2-014':('distinguish equal written eligibility from the unaffordable journey','link the practical barrier to unequal usable access or participation'),
'6.2-015':('distinguish knowledge of a policy from an accessible enforcement route','explain why unreachable complaint support can leave exclusion unresolved'),
'6.2-018':('identify anticipated stigma or retaliation from public identification','link this fear to avoiding support or explain how confidentiality can reduce it'),
'6.2-019':('identify both travel and privacy barriers to use of the service','explain why low requests cannot establish low need or give a matched access response'),
'6.2-020':('explain a control, threat or coercion pathway associated with unequal power','retain responsibility with the perpetrator rather than blaming the person harmed'),
'6.2-021':('link feared educational exclusion or unavailable support to isolation and crisis','explain an appropriate education/support response without treating harmful abandonment as inevitable or excusable'),
'6.2-023':('identify the travel barrier despite suitable confidential support','explain how a competent outreach or travel arrangement could improve use while retaining privacy'),
'7.1-007':('connect usable water and accessible terrain to productive or residential opportunity','use the valley/steep-dry contrast without claiming that one factor explains every settlement'),
'7.1-008':('identify actual employment and housing opportunities at the accessible mine','explain why an unworked deposit alone offers no equivalent residential livelihood'),
'7.1-009':('link school places and shorter journeys to reduced education-access costs','explain residential attraction with a relevant housing or affordability condition'),
'7.1-010':('identify insecurity as the pressure causing departure','explain why productive resources do not make unsafe residence viable'),
'7.2-004':('identify reduced contamination exposure or less time obtaining water','link that improvement to potential school/work participation rather than guaranteed health'),
'7.2-005':('distinguish sufficient food quantity/energy from nutrient adequacy','explain how reliance on a narrow food range can leave nutritional needs unmet'),
'7.2-006':('distinguish physical space from qualified care delivery','link absent staff to treatment/referral limits despite an additional building'),
'7.2-007':('link low income to restricted food or care access','explain the reverse pathway from illness to lost earnings or added care costs'),
'8.1-026':('distinguish transferred responsibility from missing funds and operators','link inadequate delivery capacity to the risk of unchanged service access'),
'8.1-033':('identify training and electricity as separate supports missing from the workshop','link these gaps to idle capacity rather than assume construction equals useful output'),
'8.1-034':('connect distance and missing transport to difficulty reaching the clinic','explain why the building alone does not establish access for intended users'),
'8.1-035':('link lack of operating skill to idle or unusable machinery','explain why relevant training addresses the constraint more directly than extra machines'),
'8.1-036':('trace diverted funds to maintenance not being undertaken','link unresolved faults to reliability and a relevant accountability response'),
'8.1-037':('identify finance for a small input as the remaining constraint despite workers and orders','explain how suitable viable finance could activate existing productive capacity'),
'8.1-038':('identify the gap between changed procedures and staff’s ability to apply them','link training/practice support to actual implementation rather than a rule change alone'),
'9.1-004':('combine surplus, partner demand and a functioning cold chain as conditions for feasible exchange','link exchange to export receipts or meeting the partner’s need'),
'9.1-010':('link a lower unit price at unchanged quantity to lower export receipts','compare those receipts with fixed import costs to explain financing pressure'),
'9.1-015':('identify exposure from the stated 80% concentration and price fall','link the threatened receipts to import-financing capacity without assuming output fell'),
'9.1-022':('combine wider demand with available skills and reliable delivery','link these conditions to possible sales/local earnings rather than guaranteed benefit'),
'9.1-026':('identify failed quality requirements and missing testing skills as the binding barrier','explain why quality-control capability is more relevant than extra promotion'),
'10.1-024':('identify relevant responses or reasons excluded by fixed choices','explain the resulting loss of information or a suitable pilot/category improvement'),
'10.1-026':('identify neutral clarification or follow-up as a feature of interviews','explain its contribution to understanding reasons while avoiding leading prompts'),
'10.1-028':('distinguish directly visible evidence from private motives','explain why counts need additional appropriate evidence to support reasons'),
'10.1-030':('identify a mismatch in dates, definitions or population','explain how that mismatch weakens relevance to the new local question'),
'10.1-031':('identify the kind of evidence required by the defined variable','explain how method choice follows that need rather than precedes the question'),
'10.1-041':('identify that selection can operate only on units included in the frame','link omitted groups to coverage bias despite fair selection within the list'),
'10.1-043':('identify proximity rather than chance as the selection rule','contrast unequal selection chances with a fair draw from a complete list'),
'10.1-045':('identify planned representation of both groups in proportion to size','explain inclusion of the smaller group while retaining response/frame limitations'),
'10.1-047':('identify a repeating list pattern matching the fixed interval','explain resulting overrepresentation or systematic omission despite a consistent procedure')
}
for key,(cause,outcome) in CRITERIA.items():
 t,n=key.split('-');i=it(t,n)
 if i['subtype']=='CHAIN':i['marking_guidance']=['Mechanism, up to 2 marks: '+cause+'. Credit the stated factor and a valid causal link, not a disconnected list.','Consequence, 1 mark: '+outcome+'.','Original indicative practice guidance; not an official mark scheme.']
 else:i['marking_guidance']=['Reason, 1 mark: '+cause+'.','Consequence, 1 mark: '+outcome+'.','Original indicative practice guidance; not an official mark scheme.']
# Extend the same repair to four other non-definition guides with full-answer copies.
INTERP={
13:('use the absolute enrolment comparison and the correctly calculated 60%/80% coverage rates','explain the reversal of ranking when the denominator is considered'),
14:('use the equal overall averages and the 25-percentage-point rural gap accurately','explain why equal averages cannot establish equal rural provision'),
15:('establish the increase of 140 registered learners and the 80% to 90% coverage change','interpret wider registration without treating it as completion or learning evidence'),
16:('establish the rise of 50 learners and unchanged 10% coverage','explain that numbers grew with the eligible population rather than its participation share')}
for n,(evidence,relationship) in INTERP.items():
 i=it('7.3',n);i['marking_guidance']=['Evidence, up to 2 marks: '+evidence+'.','Relationship, 1 mark: '+relationship+'.','Original indicative practice guidance; not an official mark scheme.']
# Retain the specific P01 criterion and remove only the duplicated generic line.
for t in ['5.1','6.1','6.2','7.1','7.2','7.3','8.1','9.1','9.2','9.3']:
 i=it(t,'P01');i['marking_guidance']=[g for g in i['marking_guidance'] if 'develop the supplied barrier through its direct effect' not in g]

changes=[];revisions=[]
for t,d in D.items():
 oldclaims={c['claim_id']:c for c in read(OUT/'baseline'/d['lp'].relative_to(WS))['claims']};revised={}
 for c in d['claims']['claims']:
  old=oldclaims[c['claim_id']]
  if c['text']!=old['text']:
   c['revision']=old.get('revision',1)+1;c['revised_at']='2026-10-21';revised[c['claim_id']]=c['revision'];revisions.append({'claim_id':c['claim_id'],'before':old,'after':copy.deepcopy(c)})
 oldarts={i['item_id']:i for i in read(OUT/'baseline'/d['ip'].relative_to(WS))['items']}
 for name in d['units']:oldarts.update({b['block_id']:b for b in read(OUT/'baseline'/d['td'].relative_to(WS)/'content-units'/name)['blocks']})
 for x in d['items']['items']+[b for u in d['units'].values() for b in u['blocks']]:
  aid=x.get('item_id',x.get('block_id'));old=oldarts[aid];h0=hashlib.sha256(_artefact_text(old).encode()).hexdigest();h1=hashlib.sha256(_artefact_text(x).encode()).hexdigest()
  cites=set(x.get('claim_ids',[]))&set(revised)
  if cites:
   x['claims_seen'].update({cid:revised[cid] for cid in cites})
   if h0==h1:
    x['prior_hash']=old.get('authored_hash',h0);x['reviewed_unchanged']='The revised claim changes only the illustrative systematic-sampling numbers. Rechecked this artefact’s definition or independently supplied task dataset: its method and calculations remain correct with its own frame, sample and starting position.'
  if h0!=h1:changes.append({'id':aid,'before_text_sha256':h0,'after_text_sha256':h1})
 for name,u in d['units'].items():
  u['word_count']=sum(len((b['heading']+' '+b['text']).split()) for b in u['blocks']);assert u['word_count']<=u['word_budget']['max'],(u['unit_id'],u['word_count'],u['word_budget']);dump(d['td']/'content-units'/name,u)
 dump(d['ip'],d['items']);dump(d['lp'],d['claims'])
 if any(x['id'].startswith(('BLK-6136-'+t+'.','ITEM-6136-'+t+'-')) for x in changes):
  d['notes'].setdefault('deviations',[]).append({'from':'Round-four findings F1–F5','to':'One coherent age-sex worked dataset, independent research practice numbers, explicit horizon comparison, item-specific scoring criteria and unambiguous interpretation/method-identification tasks. Existing slots and labels retained.','why':'Jeremy authorised fixing all five findings on 2026-10-21. All adjacent representations and guidance are checked together; no new review is authorised.'})
  d['notes']['post_review_status']='Round-four repairs applied by Codex; validation recorded in review/repairs/round4/validation.json. No fifth review authorised.';dump(d['td']/'authoring_notes.json',d['notes'])
dump(OUT/'actions.json',{'date':'2026-10-21','author':'Codex','findings':['F1','F2','F3','F4','F5'],'changes':changes,'claim_revisions':revisions,'specific_guidance_items':len(CRITERIA)+len(INTERP),'claude_contacted':False})
print(json.dumps({'changed_artefacts':len(changes),'specific_guidance_items':len(CRITERIA)+len(INTERP),'claim_revisions':len(revisions)}))
