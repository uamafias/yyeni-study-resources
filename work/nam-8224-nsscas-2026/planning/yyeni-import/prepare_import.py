"""Prepare exact, reviewable YYeni import payloads; never writes to YYeni."""
import json, re
from pathlib import Path

HERE = Path(__file__).resolve().parent
WS = HERE.parents[1]
ROOT = WS.parents[1]
SCHOOL = 17
CLASSROOM = 'a5695c1d-390d-4025-b013-2e218a2c1ca9'
BASE = {'school_id': SCHOOL, 'classroom_id': CLASSROOM}
REVISION = '52422ac'
SECTIONS = {'1': '94698e36-c096-4e41-a695-116380f09ae5', '2': '27d8a4b7-388e-43d1-a6fd-efd19be2383f', '3': 'fc0f53e3-02ef-4af8-a1a9-a64a51af8f4c', '4': '755e7daf-df57-4ab2-8039-0b82504f8dd9'}
MAPPING = {
 '1.1.1':6507,'1.1.2':6507,'1.1.3':6507,'1.1.4':6507,'1.1.5':6508,
 '1.3.1':6554,'1.3.2':6555,'1.3.3':6557,'1.3.4':6589,'1.3.5':6613,'1.3.6':6616,'1.4':6619,
 '2.1.1':6621,'2.1.2':6622,'2.2.1':6626,'2.2.2':6629,'2.3.1':6631,'2.3.2':6632,'2.4.1':6635,'2.4.2':6635,'2.4.3':6637,
 '3.1.1':6645,'3.1.2':6646,'3.1.3':6650,'3.1.4':6652,'3.2.1':6658,'3.2.2':6661,'3.3.1':6663,'3.3.2':6666,
 '3.4.1':6670,'3.4.2':6674,'3.4.3':6675,'3.4.4':6677,'3.4.5':6679,'3.5.1':6685,'3.5.2':6738,
 '4.1.1':6742,'4.1.2':6748,'4.1.3':6748,'4.2.1':6755,'4.2.2':6790,'4.2.3':6826,'4.3.1':6827,'4.3.2':6828,'4.4.1':6832,'4.5':6835,'4.6.1':6836,'4.7.1':6873,'4.7.2':6875,
}

def save(name, data):
 (HERE/name).write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')

def main():
 registry=json.loads((WS/'curriculum/objective_registry.json').read_text())['objectives']
 assets=json.loads((HERE/'managed-images.json').read_text()) if (HERE/'managed-images.json').exists() else {}
 resolved=json.loads((HERE/'created-destinations.json').read_text()) if (HERE/'created-destinations.json').exists() else {}
 mapping=dict(MAPPING)
 for topic in ('1.2','5.1'):
  for o in registry:
   if o['topic_id']==topic and o['objective_type']!='chem_topic_container':
    mapping[o['objective_id'].removeprefix('OBJ-8224-').split('-')[0]]=resolved.get(topic, {}).get('lesson_id', 'PENDING:'+topic)
 cards=[]; tasks=[]; notes=[]; images={}; previews=[]
 pattern=r'!\[([^\]]*)\]\(([^)]+)\)'
 def rewrite(text):
  def sub(m):
   image=assets.get(Path(m[2]).name)
   return f'![{m[1]}]({image["url"]})' if image else m[0]
  return re.sub(pattern,sub,text)
 for t in sorted((WS/'topics').iterdir(),key=lambda p:tuple(map(int,p.name.split('.')))):
  if not t.is_dir(): continue
  topic=t.name
  for image in sorted((t/'assets').glob('*.png')):
   geo=json.loads(image.with_suffix('.geometry.json').read_text())
   images[image.name]={'path':str(image.relative_to(ROOT)),'alt_text':geo['title'],'grading_context':geo['description']}
  items=json.loads((t/f'learning-items/topic_{topic}_items.json').read_text())['items']
  topic_tasks=[]
  for i in items:
   first=i['objective_ids'][0].removeprefix('OBJ-8224-').split('-')[0]
   lesson=mapping[first]
   if i['item_type']!='flashcard':
    topic_tasks.append(i); tasks.append(i); continue
   card={'lesson_id':lesson,'question':i['prompt'],'answer':i['canonical_answer'],'bloom_level':i['blooms_level'].lower(),'difficulty':i['difficulty'],'card_type':i['subtype'],
    'source_metadata':{'repository':'uamafias/yyeni-study-resources','path':str((t/f'learning-items/topic_{topic}_items.json').relative_to(ROOT)),'revision':REVISION,'external_id':i['item_id'],'tags':['NSSCAS','Chemistry','8224',f'topic:{topic}',f'command:{i["command_word"]}',f'marks:{i["mark_tariff"]}']+[f'AO:{x}' for x in i['assessment_objectives']]}}
   for side,key in [('question','prompt'),('answer','canonical_answer')]:
    refs=list(re.finditer(pattern,i[key]));assert len(refs)<=1
    if refs:
     name=Path(refs[0][2]).name
     card[side]=re.sub(pattern,'',i[key]).strip()
     card[side+'_asset_id']=assets.get(name,{}).get('asset_id','PENDING:'+name)
   cards.append(card)
  note=next(t.glob(f'{topic}-*.md'))
  title=next(o['learner_objective'].split(' (syllabus topic')[0] for o in registry if o['topic_id']==topic and o['objective_type']=='chem_topic_container')
  resource={'topic':topic,'filename':note.name,'title':f'{topic} {title} — learner notes','section_id':SECTIONS.get(topic[0],resolved.get('5.1',{}).get('section_id')),'content':rewrite(note.read_text()),'kind':'notes'}
  notes.append(resource)
  if topic_tasks:
   lines=[f'# {topic} {title} — practice tasks and worked answers','']
   for i in topic_tasks:
    lines.extend([f'## {i["item_id"]}',f'{i["mark_tariff"]} marks · Bloom: {i["blooms_level"]}',rewrite(i['prompt']),'','### Worked answer',rewrite(i['canonical_answer']),'','### Marking guidance',*i.get('marking_guidance',[]),''])
   notes.append({'topic':topic,'filename':f'{topic}-practice-tasks.md','title':f'{topic} {title} — practice tasks and worked answers','section_id':resource['section_id'],'content':'\n\n'.join(lines),'kind':'practice'})
  previews.extend([{'item_id':c['source_metadata']['external_id'],**c} for c in cards if c['source_metadata']['external_id'].startswith(f'ITEM-8224-{topic}-')])
 assert len(cards)==565 and len(tasks)==66
 changes=[{'domain':'curriculum','action':'create_lesson','parameters':{**BASE,'section_id':SECTIONS['1'],'title':'1.2 Atomic structure','objectives':[{'text':o['learner_objective']} for o in registry if o['topic_id']=='1.2' and o['objective_type']!='chem_topic_container']}},
 {'domain':'curriculum','action':'create_section','parameters':{**BASE,'title':'PRACTICAL SKILLS — PAPER 3','module_context':'NSSCAS Chemistry 8224 Annexe A practical assessment skills.'}}]
 save('curriculum-changes.json',changes)
 save('cards.json',cards);save('resources.json',notes);save('image-jobs.json',images);save('lesson-mapping.json',mapping)
 (HERE/'resources').mkdir(exist_ok=True)
 for r in notes:
  (HERE/'resources'/r['filename']).write_text(r['content'])
 save('summary.json',{'target':BASE,'flashcards':len(cards),'practice_tasks':len(tasks),'resources':len(notes),'figures':len(images),'unresolved_lessons':sorted({c['lesson_id'] for c in cards if isinstance(c['lesson_id'],str)}),'unresolved_images':sum(any(str(c.get(k,'')).startswith('PENDING:') for k in ['question_asset_id','answer_asset_id']) for c in cards)})
 review=['# Exact YYeni Chemistry import preview','',f'Target: school {SCHOOL}, NSSCAS Chemistry ({CLASSROOM}).','565 flashcards, 66 practice tasks in downloadable resources, 21 learner-note files. No assignments or learner charges.','']
 for c in cards:
  review += [f'## {c["source_metadata"]["external_id"]}',f'Lesson: {c["lesson_id"]}; Bloom: {c["bloom_level"]}; difficulty: {c["difficulty"]}; type: {c["card_type"]}',c['question'],'','**Answer**',c['answer'],'']
  for key in ['question_asset_id','answer_asset_id']:
   if key in c:
    image=next((x for x in assets.values() if x['asset_id']==c[key]),None)
    review.append(f'{key}: {c[key]}')
    if image:review.append(f'![{image["alt_text"]}]({image["url"]})')
 (HERE/'IMPORT-PREVIEW.md').write_text('\n\n'.join(review))
 print((HERE/'summary.json').read_text())

if __name__=='__main__':main()
