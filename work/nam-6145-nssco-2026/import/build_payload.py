"""Map the reviewed publication to YYeni's supported native import contract."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
BASE = {'1.1':7434,'1.2':15420,'1.3':15423,'2.1':7443,'2.2':15425,
        '2.3':15428,'3.1':17843,'3.2':17844,'3.3':17845,'3.4':17846,
        '3.5':17847,'4.1':7464,'4.2':7464,'4.3':7464,'5.1':7469,
        '5.2':7478,'5.3':7488,'5.4':7494,'6.1':7502,'6.2':7508,
        '6.3':17848,'7.1':7518,'7.2':7524,'7.3':7529,'7.4':7531,
        '8.1':17849,'8.2':7536,'9.1':7540}

def lesson(topic, item):
    slot = item['item_id'].split('-')[3]
    n = int(slot) if slot.isdigit() else None
    if topic == '1.1':
        return 15419 if slot in {'006','P02','P03'} else 7435 if slot in {'003','004','005'} else 7434
    if topic == '1.2':
        return 15422 if slot in {'017','P02','P03'} else 15421 if n and 10 <= n <= 16 else 15420
    if topic == '1.3' and n and n >= 8:
        return 15424
    if topic == '2.1':
        return 7439 if slot in {'001','002','022'} else 7444 if slot in {'020','P02','P03'} else 7443
    if topic == '2.3':
        return 15427 if n and n <= 10 else 15429 if n and 11 <= n <= 14 else 15428
    if topic == '2.2' and item['blooms_level'] == 'Evaluate':
        return 15426
    return BASE[topic]

cards, mapping = [], []
for path in sorted((ROOT / 'publish/nam-6145-nssco-2026/flashcards').glob('*.json')):
    packet = json.loads(path.read_text())
    topic = packet['topic_number']
    for item in packet['items']:
        tags = ['NSSCO', '6145', 'topic:'+topic, 'item_type:'+item['item_type'],
                'command_word:'+item['command_word'], 'mark_tariff:'+str(item['mark_tariff'])]
        tags += ['AO:'+ao for ao in item['assessment_objectives']]
        tags += item['objective_ids']
        cards.append(dict(lesson_id=lesson(topic,item), question=item['prompt'],
            answer=item['canonical_answer'], explanation='\n\n'.join(item['marking_guidance']),
            bloom_level=item['blooms_level'].lower(), difficulty=item['difficulty'],
            card_type=item['subtype'] or item['item_type'], source_metadata=dict(
                repository='https://github.com/uamafias/yyeni-study-resources',
                path=str(path.relative_to(ROOT)), external_id=item['item_id'], tags=tags)))
        mapping.append({'external_id':item['item_id'],'topic':topic,'lesson_id':lesson(topic,item)})
assert len(cards) == 458 and len({c['source_metadata']['external_id'] for c in cards}) == 458
(OUT/'cards.json').write_text(json.dumps(cards,ensure_ascii=False,indent=2)+'\n')
(OUT/'lesson-map.json').write_text(json.dumps(mapping,indent=2)+'\n')
print(f'Prepared {len(cards)} cards across {len(BASE)} published topics')
