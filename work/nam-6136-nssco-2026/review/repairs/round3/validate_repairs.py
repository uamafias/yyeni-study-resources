"""Check third-review regressions on actual learner files; no model/network calls."""
import copy
import json
import re
import sys
from pathlib import Path

OUT=Path(__file__).resolve().parent;WS=OUT.parents[2]
def read(p):return json.loads(p.read_text())
def item(t,n):return next(i for i in read(WS/'topics'/t/'learning-items'/f'topic_{t}_items.json')['items'] if i['item_id'].split('-')[3]==str(n).zfill(3))
def blocks(t):return [b for p in (WS/'topics'/t/'content-units').glob('*.json') for b in read(p)['blocks']]
allblocks=[b for p in (WS/'topics').iterdir() if (p/'contract.json').exists() for b in blocks(p.name)]
checks={};details={}
def check(name,ok,evidence):
    checks[name]=bool(ok);details[name]=evidence
    assert ok,(name,evidence)

copies=[]
for td in (WS/'topics').iterdir():
    if not (td/'contract.json').exists():continue
    items=read(next((td/'learning-items').glob('topic_*_items.json')))['items']
    for b in blocks(td.name):
        copies.extend((b['block_id'],i['item_id']) for i in items if len(i['prompt'])>25 and i['prompt'] in b['text'])
check('no_full_card_prompts_pasted_into_notes',not copies,copies)
current={b['block_id']:b for b in allblocks};preserved=[];lost=[]
for p in (OUT/'baseline/topics').glob('*/content-units/*.json'):
    for b in read(p)['blocks']:
        if '\n\nApplied example:' not in b['text']:continue
        original=b['text'].split('\n\nApplied example:',1)[0]
        original=re.sub(r'\s*\(ITEM-6136-[^)]+\)','',original)
        if original not in current[b['block_id']]['text']:lost.append(b['block_id'])
        else:preserved.append(b['block_id'])
check('restored_teaching_paragraphs_preserved',len(preserved)==66 and not lost,{'preserved':len(preserved),'lost':lost})
b=next(b for b in allblocks if b['block_id']=='BLK-6136-4.2.05-04')
check('survey_population_consistent','100 people available for work' in b['text'] and 'seeking more work' not in b['text'],b['block_id'])
check('production_loss_denominator_supplied','these totals include spoiled bags' in item('10.1','P02')['prompt'],item('10.1','P02')['item_id'])
education=item('7.3',6);note=next(b for b in allblocks if b['block_id']=='BLK-6136-7.3.02-02')
check('education_routes_align',all('traditional' in x.lower() and 'modern' in x.lower() and 'no formal qualification' in x for x in [education['prompt'],note['text']]) and 'allowance' not in note['text'] and 'preparation for a recognised assessment' not in note['text'],education['item_id'])
sdg=next(b for b in allblocks if b['block_id']=='BLK-6136-1.2.01-R01')['text']
check('sdg_goals_and_climate_mechanism_taught',all(x in sdg for x in ['Quality Education','Gender Equality','Climate Action','economic, social and environmental','drought','livelihoods','future needs']) and 'examination figure' not in sdg,sdg)
card=item('1.2',6)
check('sdg_three_mark_demand_and_guidance',card['mark_tariff']==3 and 'name one Sustainable' in card['prompt'] and 'SDG 8' not in card['canonical_answer'] and sum('1 mark:' in s for s in card['marking_guidance'])==3,card['marking_guidance'])
hpp=item('2.2',3);hpppractice=item('2.2','P02')
check('hpp_guidance_and_three_pillar_practice','shorter implementation' not in ' '.join(hpp['marking_guidance']) and '[3]' in hpppractice['prompt'] and all(x in hpppractice['canonical_answer'] for x in ['Effective governance','Economic advancement','Infrastructure development']),[hpp['item_id'],hpppractice['item_id']])
check('sustainable_pillars_retrieval_practice','two pillars of sustainable development [2]' in item('1.2','P01')['prompt'],item('1.2','P01')['item_id'])
check('no_internal_item_ids_in_learner_notes',not any('ITEM-6136-' in b['text'] for b in allblocks),[])
details['four_mark_model_answer_words']={t:len(item(t,'P01')['canonical_answer'].split('(b)',1)[1].split()) for t in ['5.1','6.1','6.2','7.1','7.2','7.3','8.1','9.1','9.2','9.3']}
sys.path.insert(0,str(WS/'topics'))
from audit_research import audit
rows,numeric=audit(write_report=False)
check('authored_numerical_and_tariff_checks',all(numeric.values()),{'checks':len(numeric),'packages':rows})
packages={i['item_id'].rsplit('-',1)[-1]:copy.deepcopy(i) for i in read(WS/'topics/10.1/learning-items/topic_10.1_items.json')['items'] if i['item_type']!='flashcard'}
packages['P02']['prompt']=packages['P02']['prompt'].replace('these totals include spoiled bags;','')
try:
    audit(packages_override=packages,write_report=False)
    caught=False
except AssertionError as exc:
    caught='output_totals_include_spoiled' in str(exc)
check('negative_case_missing_denominator_rejected',caught,'An in-memory copy lacking the spoiled-inside-output fact was rejected. Learner files were not mutated.')
report={'date':'2026-10-21','checks':checks,'details':details,'independent_approval':False}
(OUT/'targeted-validation.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'passed':len(checks),'numeric_checks':len(numeric),'preserved_teaching_paragraphs':len(preserved)},indent=2))
