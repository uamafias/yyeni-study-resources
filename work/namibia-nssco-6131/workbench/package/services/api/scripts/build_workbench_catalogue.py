"""Publish callable Workbench settings for local assignment, not static flashcards.

Uses the reviewed candidate bank without rewriting it. Independent approval and
full clause coverage remain pending. This does not merge overlapping exam types.
"""
from collections import defaultdict,Counter
from pathlib import Path
import hashlib,json

API=Path(__file__).resolve().parents[1]
ROOT=API.parents[1]
DATA=API/'data/imports/nam-6131-nssco-2026'
SERVICE=API/'services/math_workbench'
HOLDS={}

def build():
    raw=(DATA/'workbench-bank.json').read_bytes();bank=json.loads(raw)
    homes=json.loads((DATA/'catalogue-homes.json').read_text())
    aliases=json.loads((SERVICE/'pilot_aliases.json').read_text())
    groups=defaultdict(list);native={}
    for card in bank['recipe_cards']:
        groups[card['recipe_id']].append(card)
        if card['recipe_id'].startswith('wb6131:legacy:'):
            native[card['native_lesson_id']]=homes[card['recipe_id'].split(':')[2]]
    alias_topics={}
    for key,alias in aliases.items():
        for card in groups[alias['recipe_id']]:alias_topics[card['native_lesson_id']]=alias['topic']
    rows=[]
    for rid,cards in groups.items():
        home=native[cards[0]['native_lesson_id']]
        existing=[(key,value) for key,value in aliases.items() if value['recipe_id']==rid]
        scopes=[]
        if existing:
            scopes.extend((key,alias['task'],alias['title']) for key,alias in existing)
            remaining={c['question_snapshot'].get('source_branch',{}).get('task') for c in cards}-{alias['task'] for _,alias in existing}
            for task in sorted(remaining):
                matching=[c for c in cards if c['question_snapshot'].get('source_branch',{}).get('task')==task]
                title='Lowest common multiple' if task=='lcm' else matching[0]['question_snapshot']['title']
                scopes.append(('lcm' if task=='lcm' else rid+':task:'+task,task,title))
        else:
            titles=list(dict.fromkeys(c['question_snapshot']['title'] for c in cards))
            scopes=[(rid,None,' / '.join(titles))]
        for key,task,title in scopes:
            chosen=[c for c in cards if task is None or c['question_snapshot'].get('source_branch',{}).get('task')==task]
            assert chosen,(key,'No canonical task examples')
            marks=[c['question_snapshot']['proposed_total_marks'] for c in chosen]
            objectives=sorted({o for c in chosen for o in c['objective_ids']})
            rows.append({'id':key,'recipeId':rid,'topic':alias_topics.get(cards[0]['native_lesson_id'],home['topic']),
                'syllabusTopic':home['syllabusTopic'],'title':title,'description':title,
                'lessonId':cards[0]['native_lesson_id'],'objectiveIds':objectives,
                'task':task,'marks':max(marks),'marksMin':min(marks),'marksMax':max(marks),
                'canonicalExamples':len(chosen),'distinctSavedQuestions':len({c['question_snapshot']['fingerprint'] for c in chosen}),
                'availability':'held' if rid in HOLDS else 'available','holdReason':HOLDS.get(rid,''),
                'reviewStatus':'candidate; full-bank approval pending'})
    # Existing pilot keys stay first; each source setting is represented once,
    # except the intentional HCF/LCM task split (distinct exam demands).
    rows.sort(key=lambda r:(r['id'] not in aliases,list(aliases).index(r['id']) if r['id'] in aliases else 0,r['syllabusTopic'],r['topic'],r['title'],r['id']))
    assert len({r['id'] for r in rows})==len(rows)
    assert {r['recipeId'] for r in rows}==set(groups)
    fingerprints=defaultdict(set)
    for c in bank['recipe_cards']:fingerprints[c['question_snapshot']['fingerprint']].add(c['recipe_id'])
    summary={'sourceBankSha256':hashlib.sha256(raw).hexdigest(),'recipeSettings':len(groups),
        'assignmentTypes':len(rows),'availableTypes':sum(r['availability']=='available' for r in rows),
        'heldTypes':sum(r['availability']=='held' for r in rows),'savedExamples':len(bank['recipe_cards']),
        'syllabusTopics':len({r['syllabusTopic'] for r in rows}),'lessonGroups':len({r['topic'] for r in rows}),
        'mappedObjectives':len({o for r in rows for o in r['objectiveIds']}),
        'identicalQuestionGroupsAcrossSettings':sum(len(v)>1 for v in fingerprints.values()),
        'coverageCertified':False,'independentlyApproved':False}
    return {'summary':summary,'recipes':rows}

if __name__=='__main__':
    result=build()
    (SERVICE/'catalogue.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    (ROOT/'apps/web/components/MathsWorkbench/recipeCatalogue.json').write_text(json.dumps(result['recipes'],indent=2,ensure_ascii=False)+'\n')
    print(json.dumps(result['summary'],indent=2))
