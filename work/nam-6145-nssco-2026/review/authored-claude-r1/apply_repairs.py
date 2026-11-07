"""Apply Jeremy-authorised text repairs to canonical records, retaining review history."""
import copy,hashlib,json,re,subprocess,sys
from pathlib import Path
from rubric_repairs import apply as fix_rubrics
HERE=Path(__file__).resolve().parent;WS=HERE.parents[1];ROOT=WS.parents[1]
sys.path.insert(0,str(ROOT/'standard/v0.2.0-draft/checks'))
from yyeni_checks import _artefact_text
assert not (HERE/'REPAIRS.json').exists(),'Repairs already applied; edit canonical records, do not replay.'
def read(p):return json.loads(p.read_text())
def save(p,d):p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
topics=['2.1','2.3','3.2','3.4','4.2','4.3','5.4','6.1','6.2','6.3','7.2','7.3','8.1','9.1']
data={}
for t in topics:
 td=WS/'topics'/t;wo=read(td/'work_order.json')
 paths={'ledger':td/'claims/canonical_claim_ledger.json','unit':td/wo['content_units'][0]['file'],'items':td/wo['output_files']['learning_items']}
 d={k:read(p) for k,p in paths.items()};d['paths']=paths;d['old']=copy.deepcopy({k:d[k] for k in paths});data[t]=d
def block(t,n):return next(b for b in data[t]['unit']['blocks'] if b['block_id']==f'B-6145-{t}-{n:03}')
def item(t,n):return next(i for i in data[t]['items']['items'] if i['item_id'].split('-')[-2]==f'{n:03}')
def claim(t,n):return next(c for c in data[t]['ledger']['claims'] if c['claim_id']==f'CLM-6145-{t}-{n:03}')

# 001: reserve extension/contraction for movements along curves.
replacements=[('A supply contraction','A decrease in supply (a leftward shift)'),('can contract bread supply','can decrease bread supply'),('contracting supply','decreasing supply'),('contracted supply curve','decreased supply curve'),('supply contracts left','supply shifts left'),('supply contraction','decrease in supply'),('supply-contraction','supply-decrease'),('contracted supply','decreased supply')]
for record,key in [(c,'text') for c in data['3.2']['ledger']['claims']]+[(b,'text') for b in data['3.2']['unit']['blocks']]:
 for old,new in replacements:record[key]=record[key].replace(old,new)
for it in data['3.2']['items']['items']:
 for k in ['prompt','canonical_answer']:
  for old,new in replacements:it[k]=it[k].replace(old,new)
 for old,new in replacements:
  it['marking_guidance']=[s.replace(old,new) for s in it['marking_guidance']]
  it['context']['facts']=[s.replace(old,new) for s in it['context']['facts']]
block('3.2',2)['text']+='\n\nAn extension of demand is a movement to a larger quantity demanded after an own-price fall; a contraction is the reverse movement after an own-price rise. For supply, extension accompanies a higher own price and contraction a lower own price, other conditions unchanged. Use increase or decrease for a shift of the whole relationship.'
block('3.2',10)['text']+=' Show a clear arrow from the original curve towards the new curve to identify the direction of the shift.'
# 006: make the limited cross-link explicit.
block('3.2',13)['text']=block('3.2',13)['text'].replace('topic 6.3 examines reasons and methods of government intervention','topic 6.3 examines other reasons and methods of intervention in business')

# 002: named functions and descriptions, supported by primary institutional sources.
old=block('2.3',9)['text'].split('\n\n',1)[0]
new='''A central bank issues currency: it arranges the supply of notes and coins for circulation through the banking system. As banker to government, it holds government accounts and processes public payments. As banker to commercial banks, it provides accounts and settlement facilities so banks can settle obligations to one another. As lender of last resort, it may provide emergency liquidity to banks facing exceptional liquidity difficulty, subject to applicable conditions; this is not an unconditional rescue or ordinary lending to households.

It holds and manages official foreign-exchange reserves, helping meet external obligations and support the currency framework. It conducts monetary policy, influencing interest and credit conditions to pursue price stability and related objectives. Banking supervision and payment-system oversight support sound financial operation. These functions are distinct from a commercial bank deciding an individual customer's deposit or loan terms. The Bank of Namibia describes its [currency and government-banking operations](https://www.bon.com.na/About-Us/Departments/Banking-Services.aspx) and [reserve-management responsibilities](https://www.bon.com.na/About-Us/Departments/Financial-Markets.aspx); its [institutional overview](https://www.bon.com.na/About-Us.aspx) places them within the wider central-bank role.'''
block('2.3',9)['text']=block('2.3',9)['text'].replace(old,new)
cl=claim('2.3',19)
cl['text']='A central bank issues currency, acts as banker to government and commercial banks, may provide conditional lender-of-last-resort liquidity, manages official foreign reserves and conducts monetary policy under its institutional framework.'
cl['evidence']=[{'source_id':'BON-FUNCTIONS','locator':u+' ; checked 8 November 2026','support_type':'paraphrase'} for u in ['https://www.bon.com.na/About-Us/Departments/Banking-Services.aspx','https://www.bon.com.na/About-Us/Departments/Financial-Markets.aspx','https://www.bon.com.na/About-Us.aspx']]
i=item('2.3',15)
i['prompt']='Identify two central-bank functions and distinguish each from ordinary commercial-bank customer services.'
i['canonical_answer']='Issuing notes and coins supplies official currency for circulation. Acting as banker to government processes public payments and holds its accounts. These are central-bank functions rather than an ordinary commercial bank assessing a household loan.'
i['marking_guidance']=['Feature/example (1): issuing notes and coins supplies official currency, distinct from a customer loan.','Distinct characteristic/example (1): banker to government holds its accounts/processes public payments rather than ordinary household account services.']
# FEATURE maps the institutional container: its existing claim set includes monetary roles;
# explicitly cite the central-bank function claim that supports the revised named examples.
if cl['claim_id'] not in i['claim_ids']:i['claim_ids'].append(cl['claim_id'])
# P01's role-contrast part now has concrete functions without changing the planned demand.
p=next(i for i in data['2.3']['items']['items'] if i['item_id'].endswith('P01'))
p['canonical_answer']=p['canonical_answer'].replace('Central banks perform system-level monetary functions, while commercial banks provide customer deposit/credit services; monetary policy is distinct from assessing an individual customer loan.','A central bank issues official currency, while commercial banks distribute it and provide customer accounts. A central bank acts as banker to government, while a commercial bank assesses ordinary customer credit. These are two distinct role contrasts.')
p['marking_guidance'][-1]='Distinct role contrasts (2): central-bank currency issue versus commercial customer/distribution services (1); government banking versus ordinary customer-credit assessment (1). Marks allocation 8.'
if cl['claim_id'] not in p['claim_ids']:p['claim_ids'].append(cl['claim_id'])

# 003: teach the standard term without inventing statutory limits.
block('2.1',3)['text']=block('2.1',3)['text'].replace('Business obligations can therefore place the owner’s personal resources at risk under the applicable rules.','Business obligations can therefore place the owner’s personal resources at risk: this is commonly called unlimited liability, with the applicable legal rules determining enforcement.')
claim('2.1',8)['text']+=' Personal responsibility for business obligations is commonly called unlimited liability; the applicable rules determine enforcement.'
for i in data['2.1']['items']['items']:
 if i['item_id'].endswith(('005-FEATURE','P03')):
  i['canonical_answer']+=' A sole proprietor’s personal exposure to business obligations is commonly called unlimited liability.'

# 004: restore the familiar word in non-currency prose, without spurious peg teaching.
block('7.3',1)['text']=block('7.3',1)['text'].replace('where capital-consumption allowance is deducted','where capital consumption, commonly called depreciation, is deducted')
u=data['7.3']['unit'];b=copy.deepcopy(block('7.3',4))
b['block_id']='B-6145-7.3-010';b['heading']='Depreciation means consumption of productive capital';b['block_type']='plain_explanation'
b['text']='Capital consumption is the wearing out or using up of productive capital during production; the familiar accounting term is depreciation. A gross measure is before the relevant depreciation deduction, while a net measure is after it. This use of depreciation concerns productive assets, rather than a currency losing value. Compare national measures on the same stated accounting basis.'
u['blocks'].insert(u['blocks'].index(block('7.3',4))+1,b)
item('7.3',4)['canonical_answer']='Gross Domestic Product plus net factor income from abroad.'
item('7.3',4)['marking_guidance']=['Definition/key term (1): GDP adjusted by factor income received from abroad minus corresponding factor income paid abroad.']
item('7.3',6)['canonical_answer']='Income earned by a country’s factors of production over a stated period.'
item('7.3',6)['marking_guidance']=['Definition/key term (1): factor income earned from production over the period.']

# 007: use a concrete unlabelled cost situation rather than a definition cue.
i=item('5.4',22)
i['prompt']='Explain the error in calling this an economy of scale: an invented firm expands its long-run operations, but coordination delays raise cost per unit from N$8 to N$11. All inputs can be adjusted.'
i['canonical_answer']='Coordination delays make the expanded long-run operation costlier per unit, rising N$3. This is a diseconomy of scale, whereas an economy would lower long-run average cost; it is not a fixed-input diminishing-returns case.'
i['marking_guidance']=['Confusion (1): expansion alone is mistaken for an economy despite coordination losses.','Boundary/test (1): long-run unit cost rises N$8 to N$11, identifying diseconomies rather than a cost-saving economy.']

# 008: compact, broad definition; the notes retain precise GFR/TFR distinctions.
item('8.1',14)['canonical_answer']='A measure of births per woman.'
item('8.1',14)['marking_guidance']=['Definition/key term (1): births relative to women, rather than births per thousand of the whole population.']

# Optional media reminder: retain audience and affordability conditions.
block('3.4',3)['text']+=' Television can combine sound and moving images for viewers, while a leaflet can give local written detail. Their suitability still depends on audience access, attention and the campaign budget.'

rubrics=[]
for d in data.values():rubrics.extend(fix_rubrics(d['items']['items']))
changed=[];revisions=[]
for t,d in data.items():
 oldclaims={c['claim_id']:c for c in d['old']['ledger']['claims']}
 changedclaims={}
 for cl in d['ledger']['claims']:
  before=oldclaims[cl['claim_id']]
  if cl['text']!=before['text'] or cl['evidence']!=before['evidence']:
   cl['revision']=before['revision']+1;changedclaims[cl['claim_id']]=cl['revision']
   revisions.append({'claim_id':cl['claim_id'],'from_revision':before['revision'],'to_revision':cl['revision'],'old_text':before['text'],'new_text':cl['text']})
 oldartefacts={a.get('block_id') or a.get('item_id'):a for a in d['old']['unit']['blocks']+d['old']['items']['items']}
 for a in d['unit']['blocks']+d['items']['items']:
  aid=a.get('block_id') or a.get('item_id');before=oldartefacts.get(aid)
  for cid in a['claim_ids']:
   rev=next(cl['revision'] for cl in d['ledger']['claims'] if cl['claim_id']==cid)
   a.setdefault('claims_seen',{})[cid]=rev
  if any(c in a['claim_ids'] for c in changedclaims):
   if before and _artefact_text(a)==_artefact_text(before):a['reviewed_unchanged']='Re-read after the cited claim revision: the existing specific example or institutional boundary remains correct and needs no learner-text change.'
  if not before:a['authored_hash']=hashlib.sha256(_artefact_text(a).encode()).hexdigest()
  if not before or _artefact_text(a)!=_artefact_text(before):changed.append(aid)
 unit=d['unit'];unit['word_count']=sum(len(b['text'].split()) for b in unit['blocks'])
 assert unit['word_budget']['min']<=unit['word_count']<=unit['word_budget']['max'],(t,unit['word_count'])
 for k,p in d['paths'].items():save(p,d[k])
 note=read(WS/'topics'/t/'authoring_notes.json');note['counts']['notes_words']=unit['word_count'];note['post_review_locked']=True
 note['review_repairs']={'review_id':'6145-AUTH-R1','date':'2026-11-08','source':'review/authored-claude-r1/REPAIRS.json','regeneration':'Canonical JSON is the repaired source of record. Initial build_authored.py files are pre-review authoring snapshots; use render_notes.py, restamp.py and run_checks.py for maintenance.'}
 save(WS/'topics'/t/'authoring_notes.json',note)
 subprocess.run([sys.executable,str(ROOT/'operations/tools/restamp.py'),str(WS),t,'--note','Jeremy-authorised repairs for Claude review 6145-AUTH-R1: terminology, central-bank functions, precise definitions, specific credit points and misconception discrimination.'],cwd=ROOT,check=True,capture_output=True,text=True)
 subprocess.run([sys.executable,str(ROOT/'standard/v0.2.0-draft/build/render_notes.py'),str(WS),t],cwd=ROOT,check=True,capture_output=True,text=True)
 subprocess.run([sys.executable,str(ROOT/'standard/v0.2.0-draft/checks/run_checks.py'),str(WS),t,'--quiet'],cwd=ROOT,capture_output=True,text=True)
 q=read(WS/'topics'/t/'qa_report.json')
 failures=[c for c in q['deterministic_checks'] if c['status']=='fail']
 if failures:print(json.dumps({'topic':t,'failures':failures},ensure_ascii=False))
save(HERE/'REPAIRS.json',{'review_id':'6145-AUTH-R1','authorisation':'Jeremy: make those improvements','topics':topics,'changed_artefacts':changed,'revised_claims':revisions,'specific_rubrics':rubrics,'status':'Applied; qualification and issue closure still required.'})
print(json.dumps({'topics':len(topics),'changed_artefacts':len(changed),'revised_claims':len(revisions),'specific_rubrics':len(rubrics)}))
