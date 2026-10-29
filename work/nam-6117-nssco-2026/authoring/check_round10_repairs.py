"""Check the delivered fields, not merely the repair source text."""
import json,re,collections
from pathlib import Path
from round10_repairs import ANCHORS,FRACTION_SENTENCES
W=Path(__file__).resolve().parents[1]
items={};mc=[];placements=[];notes=[];qa=[]
for t in range(1,13):
 d=W/f'topics/{t}'
 for x in json.loads((d/f'learning-items/topic_{t}_items.json').read_text())['items']:items[x['item_id']]=x
 parts=json.loads((d/'authored_assessment_parts.json').read_text())['parts']
 for p in parts:
  if p['task_id'].endswith('P01') and t<12:
   opts=dict(re.findall(r'^([A-D])\. (.+)$',p['prompt'],re.M));key=p['canonical_answer'][0]
   for letter in set(opts)-{key}:
    assert f'{letter}: ' in p['canonical_answer'],(t,p['part'],letter)
    assert f'{letter}: ' in '\n'.join(p['marking_guidance'])
   assert 'Other options reflect misconceptions' not in str(p)
   mc.append((p,opts,key))
 for f in (d/'content-units').glob('*.json'):
  u=json.loads(f.read_text());bs=u['blocks']
  for i,b in enumerate(bs):
   assert not re.search(r'\boriginal (?:practice|illustrative|example|results|cooling results|timed gas data|data|chip and powder)',b['text'],re.I),(t,b['block_id'])
   if b['block_id'].endswith('FINAL-METHOD'):
    assert bs[i-1]['heading']==ANCHORS[t],(t,i)
    assert b['heading'].startswith('Worked example:')
    assert not any(z['block_type']=='cross_link' for z in bs[:i]),t
    placements.append({'topic':t,'section':u['unit_id'],'heading':b['heading'],'immediately_after':bs[i-1]['heading'],'block_index':i})
   if b['block_id'].endswith('-R5'):assert not any(z['block_type']=='cross_link' for z in bs[:i]),(t,b['block_id'])
 text=next(p for p in d.glob('*.md') if re.match(r'^\d+-',p.name)).read_text();notes.append(text)
 if t==10:
  for s in FRACTION_SENTENCES:assert text.count(s)==1,(s,text.count(s))
 q=json.loads((d/'qa_report.json').read_text());assert not any(c['status']=='fail' for c in q['deterministic_checks']);qa.append({'topic':t,'generated_at':q['generated_at'],'release_decision':q['release_decision']})
assert len(mc)==132 and len(placements)==12
get=lambda stem:next(x for k,x in items.items() if k.startswith('ITEM-6117-'+stem+'-'))
assert 'below carbon' not in get('9-015')['prompt'] and 'zinc' in get('9-015')['prompt']
for k in ['10-028','10-045']:assert get(k)['command_word']=='State' and get(k)['prompt'].startswith('State ')
assert 'whether these records are sufficient' in get('11-003')['prompt']
assert 'more secure water source' not in get('11-003')['prompt']
for ident in ['3-P03','4-P03','6-P02','6-P03']:assert '![' in items['ITEM-6117-'+ident]['prompt']
for x in items.values():assert 'Other options reflect misconceptions' not in str(x)
metrics={}
for name,measure in [('whitespace_words',lambda s:len(s.split())),('unicode_characters_including_spaces',len)]:
 unique=tied=0
 for p,opts,key in mc:
  ns={k:measure(v) for k,v in opts.items()};others=[v for k,v in ns.items() if k!=key]
  unique+=ns[key]>max(others);tied+=ns[key]==max(others)
 metrics[name]={'correct_uniquely_longest':unique,'correct_tied_for_longest':tied,'correct_longest_including_ties':unique+tied,'questions':132}
r={'status':'pass','scope':'Author regression checks of all named follow-up repairs. Presence checks do not independently certify scientific correctness.','mc_questions_with_three_explicit_distractor_reasons':132,'generic_mc_feedback_instances':0,'length_metrics':metrics,'worked_example_placements':placements,'fraction_advice_sentence_counts':[1,1],'qa_runs':qa,'author_only_caveat':'Scientific distractor review, visual ledger and previous recomputations remain author checks. Independent acceptance of AO/recall and revised content is open.'}
(W/'planning/round10-repair-checks.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items() if k not in ['worked_example_placements','qa_runs']},indent=2))
