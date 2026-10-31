"""Apply the October 29 review repair after apply_full_demand_repairs.py."""
import json,copy,hashlib,sys,re
from pathlib import Path
from round3_changes import CHANGES,RECALL_EXTRA
from round4_rubrics import RUBRICS
W=Path(__file__).resolve().parents[1];R=W.parents[1]
sys.path.insert(0,str(R/'standard/v0.2.0-draft/checks'))
from yyeni_checks import _artefact_text

def read(p):return json.loads(p.read_text())
def save(p,d):p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
def fp(x):return hashlib.sha256(json.dumps({k:x.get(k) for k in ['prompt','canonical_answer','marking_guidance','mark_tariff']},sort_keys=True,ensure_ascii=False).encode()).hexdigest()
audit=read(W/'planning/demand-audit-before-2026-10-29.json');base={r['id']:r for r in audit['records']};rows=[];changes=[]
for t in range(1,13):
 T=W/f'topics/{t}';p=T/f'learning-items/topic_{t}_items.json';d=read(p);lp=T/'claims/canonical_claim_ledger.json';ld=read(lp);units={q:read(q) for q in (T/'content-units').glob('*.json')}
 for x in d['items']:
  if x['item_type']!='flashcard':continue
  before=copy.deepcopy(x);key=f"{t}-{x['item_id'].split('-')[3]}";c=CHANGES.get(key)
  if c:
   for k in ['prompt','canonical_answer','marking_guidance','blooms_level']:x[k]=c[k]
   for k,v in [('assessment_objectives',c['ao']),('subtype',c['subtype'])]:
    if v:x[k]=v
   x['command_word']=x['prompt'].split()[0]
  # A one-mark rubric names the complete accepted answer, not an abstract category.
  if x['mark_tariff']==1 and not c:
   x['marking_guidance']=[x['canonical_answer'].rstrip('.')+' (1). Accept scientifically equivalent wording.']
  if key in RUBRICS:x['marking_guidance']=RUBRICS[key]
  if key in ['4-025','4-026','4-027','4-028']:
   x['prompt']=re.sub(r' Use only relative atomic masses.*?distractors\.', '',x['prompt'])
   x['prompt']=re.sub(r'Ar:.*$', {'4-025':'Ar: C 12, H 1, O 16.','4-026':'Ar: C 12, H 1.','4-027':'Ar: N 14, O 16.','4-028':'Ar: C 12, H 1.'}[key], x['prompt'])
  if t==1 and x['subtype']=='CALC':x['difficulty']=2
  row=copy.deepcopy(base[x['item_id']]);recall=c['recall'] if c else RECALL_EXTRA.get(key,row['recall_marks'])
  assert 0<=recall<=x['mark_tariff'],key
  row.update(subtype=x['subtype'],recall_marks=recall,non_recall_marks=x['mark_tariff']-recall,prompt=x['prompt'],credit_points=x['marking_guidance'],fingerprint=fp(x))
  row['basis']='Under the documented execution-versus-recitation rule: '+('all credited content is familiar factual/procedural knowledge, counted conservatively.' if recall==x['mark_tariff'] else 'mixed familiar factual/test knowledge and application; factual credit is counted separately.' if recall else 'credit requires executing numerical operations, using supplied evidence, or the specified linked causal explanation; no separate formula-recitation credit.')
  if key in RECALL_EXTRA:row['credit_allocation_detail']={'recall_marks':recall,'rubric':x['marking_guidance'],'rule':'Count the familiar reagent, product, test or factual explanation credit conservatively; remaining credit requires applying the specified procedure to the case.'}
  if c:row.pop('credit_allocation_detail',None)
  rows.append(row)
  cid='CLM-'+x['item_id'].removeprefix('ITEM-')
  for claim in ld['claims']:
   if claim['claim_id']==cid and claim['text']!=x['canonical_answer']:claim['text']=x['canonical_answer'];claim['revision']+=1
  if fp(before)!=fp(x):
   changes.append({'id':x['item_id'],'before':before,'after':copy.deepcopy(x)})
   for u in units.values():
    for b in u['blocks']:
     if cid in b.get('claim_ids',[]) and before['prompt'] in b.get('text',''):
      b['text']=x['prompt']+'\n\n'+x['canonical_answer']+'\n\nChecking the response: '+' '.join(x['marking_guidance']);b['assessment_objectives']=x['assessment_objectives']
 for x in read(T/'authored_assessment_parts.json')['parts']:
  row=copy.deepcopy(base[x['task_id']+':'+x['part']]);assert row['fingerprint']==fp(x);rows.append(row)
 revisions={c['claim_id']:c['revision'] for c in ld['claims']}
 def stamp(x):
  old=x.get('authored_hash');new=hashlib.sha256(_artefact_text(x).encode()).hexdigest()
  if old and old!=new:x.update(prior_hash=old,repair_note='October 29 review: stimulus and explicit credit repaired; independent semantic review remains open.')
  for cid in x.get('claims_seen',{}):
   if x['claims_seen'][cid]!=revisions[cid]:x['claims_seen'][cid]=revisions[cid];x['reviewed_unchanged']='Factual teaching retained; linked worked example updated.'
  x['authored_hash']=new
 for x in d['items']:stamp(x)
 for q,u in units.items():
  for b in u['blocks']:stamp(b)
  u['word_count']=sum(len(b['text'].split()) for b in u['blocks']);save(q,u)
 save(p,d);save(lp,ld)
summary={'entries':len(rows),'cards':sum(r['kind']=='card' for r in rows),'activity_parts':sum(r['kind']=='activity_part' for r in rows),'marks':sum(r['marks'] for r in rows),'recall_marks':sum(r['recall_marks'] for r in rows)};summary['recall_percent']=100*summary['recall_marks']/summary['marks']
audit.update(method='Credit-based author judgement, independent of Bloom labels. Recitation of a fact/formula/procedure is recall; executing it on supplied quantities is numerical application (AO B). Explicit mixed factual credit is counted. Linked explanations must earn the stated cause and consequence. See RECALL-RULE-2026-10-29.md. Prior full-bank decisions retained except the documented corrections; no claim of a new independent full-bank audit.',summary=summary,records=rows)
save(W/'planning/full-demand-audit.json',audit)
log=W/'planning/round3-repair-log.json'
if changes:save(log,{'changes':changes,'summary':summary})
print(json.dumps(summary,indent=2))
