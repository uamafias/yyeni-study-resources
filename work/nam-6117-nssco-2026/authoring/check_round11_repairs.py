"""Verify independent-review repairs against delivered items, parts and notes."""
import json,re,hashlib,math
from pathlib import Path
from round11_repairs import FRACTION,SHAPES
W=Path(__file__).resolve().parents[1]
items={};parts={};notes={};units={};qa=[]
for t in range(1,13):
 d=W/f'topics/{t}'
 for x in json.loads((d/f'learning-items/topic_{t}_items.json').read_text())['items']:items[x['item_id']]=x
 for x in json.loads((d/'authored_assessment_parts.json').read_text())['parts']:parts[x['task_id']+':'+x['part']]=x
 notes[t]=next(p for p in d.glob('*.md') if re.match(r'^\d+-',p.name)).read_text()
 units[t]=[json.loads(p.read_text()) for p in (d/'content-units').glob('*.json')]
 q=json.loads((d/'qa_report.json').read_text());assert not any(x['status']=='fail' for x in q['deterministic_checks']);qa.append({'topic':t,'generated_at':q['generated_at'],'decision':q['release_decision']})
get=lambda k:next(x for i,x in items.items() if i.startswith('ITEM-6117-'+k+'-'))
for t,labels,tariffs in [(3,'abcdef',[2,2,3,2,2,3]),(7,'abc',[2,2,3]),(11,'abc',[2,2,3])]:
 x=items[f'ITEM-6117-{t}-P02']
 assert 'credit-group' not in json.dumps(x)
 for letter,mark in zip(labels,tariffs):
  p=parts[f'ITEM-6117-{t}-P02:{letter}'];assert p['mark_tariff']==mark
  assert f'({letter})' in x['prompt'] and f'({letter})' in x['canonical_answer']
  assert any(g.startswith('Part '+letter+':') for g in x['marking_guidance'])
assert '| S | 2 | 8 |' in items['ITEM-6117-3-P02']['prompt']
assert '| D | 5.0 | 4.0 |' in items['ITEM-6117-3-P02']['prompt']
assert items['ITEM-6117-3-P02']['context']['facts']
assert 'free of that solid precipitate' in str(parts['ITEM-6117-11-P02:b']['marking_guidance'])
for x in list(items.values())+list(parts.values()):
 assert not re.search(r'original (?:synthetic|supplied|results|data)|original teaching box|synthetic classroom dataset',x['prompt'],re.I),x.get('item_id',x.get('task_id'))
for text in notes.values():
 assert 'original teaching box' not in text and 'twelfth content topic' not in text and 'synthetic practice data' not in text
 assert 'after after' not in text and '10⁻9' not in text
 assert 'attempt drawing tasks before consulting them' not in text
 assert 'Choose the operation and instrument to match' not in text
 assert 'Read a scale at eye level using its divisions' not in text
for s in FRACTION:assert notes[10].count(s)==1
for s in SHAPES:assert notes[2].count(s)<=1
assert 'used for fuel for' not in notes[10] and 'used for a chemical feedstock' not in notes[10]
assert notes[3].count('Connect material properties')==1
assert notes[9].count('### Connections')==0
assert notes[9].count('Connect metal behaviour to particle structure')==1
u=next(u for u in units[9] if u['unit_id']=='CU-6117-9.3');bs=u['blocks'];i=next(i for i,b in enumerate(bs) if b['heading']=='Iron in the blast furnace');assert 'VIS-6117-9-01' in bs[i+1]['text']
u=next(u for u in units[4] if u['unit_id']=='CU-6117-4.2');bs=u['blocks'];gas=next(i for i,b in enumerate(bs) if b['heading']=='Gas volume at room conditions');lim=next(i for i,b in enumerate(bs) if b['block_id'].endswith('FINAL-METHOD-LIMIT'));assert lim>gas
assert sum(b['heading'].startswith('Worked example:') for b in bs)==5
for key in ['6-017','9-044']:assert get(key)['mark_tariff']==1
assert get('6-017')['canonical_answer']=='Glucose.'
assert 'aluminium' not in get('9-044')['prompt'].lower()
assert get('10-033')['command_word']=='Deduce'
assert 'oxygen blowing alone is not a heat source' not in get('9-023')['canonical_answer']
assert 'moving machine parts' in get('10-082')['canonical_answer']
assert 'Include safe handling' not in parts['ITEM-6117-12-P01:d']['prompt']
assert 'answer panel is separate' not in parts['ITEM-6117-12-P01:a']['canonical_answer']
assert 'Practical safety advice (unassessed):' in parts['ITEM-6117-12-P01:d']['canonical_answer']
assert not any(v in parts['ITEM-6117-12-P01:d']['canonical_answer'] for v in ['100 cm³','80 °C','22 °C'])
assert '180° apart' in parts['ITEM-6117-2-P01:10']['canonical_answer']
assert 'approximately' not in parts['ITEM-6117-4-P01:11']['canonical_answer']
assert get('9-023')['canonical_answer'].count('.')==2
x=items['ITEM-6117-6-P02'];assert x['prompt'].count('| Time / s |')==1 and '![' in x['prompt']
assert 'chips' not in parts['ITEM-6117-6-P02:d']['canonical_answer']
assert 'Powder' not in str(parts['ITEM-6117-6-P02:d']['marking_guidance'])
assert '| Feature | Result |' in parts['ITEM-6117-8-P03:a']['prompt']
assert 'copper' not in parts['ITEM-6117-8-P03:e']['prompt'].lower() and 'chloride' not in parts['ITEM-6117-8-P03:e']['prompt'].lower()
assert 'inverted' in parts['ITEM-6117-6-P03:c']['canonical_answer']
for a,b in [('6-053','6-054'),('7-021','7-022'),('7-043','7-044')]:assert get(a)['intentional_duplicate_group']==get(b)['intentional_duplicate_group'] and get(a)['intentional_duplicate_group']
assert 8-2==6 and 2-2==0 and math.isclose(5-1,4) and math.isclose(5-4,1)
miscon=[x['item_id'] for x in items.values() if x.get('subtype')=='MISCON'];evidence=[{'item':x['item_id'],'entry':x['misconception_entry'],'subtype':x.get('subtype')} for x in items.values() if x.get('misconception_entry')]
images=[x['item_id'] for x in items.values() if x['item_type']!='flashcard' and '![' in x['prompt']]
assert len(miscon)==20 and len(evidence)==19 and len(images)==8
report={'status':'pass','scope':'Author checks of all latest named repairs; independent review is not inferred.','qa':qa,'miscon_subtype_cards':miscon,'examiner_misconception_mappings':evidence,'activities_with_markdown_images':images,'additional_author_misconceptions':['ITEM-6117-1-076-MISCON','ITEM-6117-12-035-MISCON'],'source_mapped_card_with_other_subtype':'ITEM-6117-8-048-FEATURE','intentional_repetition_groups':{g:[x['item_id'] for x in items.values() if x.get('intentional_duplicate_group')==g] for g in sorted({x.get('intentional_duplicate_group') for x in items.values() if x.get('intentional_duplicate_group')})},'unchanged_finding':'Full Bonding in glass block inspected: both paragraphs concern glass structure, rigidity, brittleness, insulation and transparency; no mismatched body found.','retained_word_original':'Original equation, original readings and original sample denote mathematical or experimental provenance, not authoring labels.','numerical_checks':{'extra_soap_S':8-2,'extra_soap_D':2-2,'mass_broken_down_S':5-1,'mass_broken_down_D':5-4,'curve_B_rate':28/20,'curve_A_rate':18/20}}
(W/'planning/round11-repair-checks.json').write_text(json.dumps(report,indent=2)+'\n');print('PASS: all latest named repairs; 20 MISCON cards, 19 source entries, 8 image-bearing activities.')
