"""Audit the complete approved slot set and local publication, and record step 5."""
import json
from collections import Counter
from pathlib import Path
WS=Path(__file__).resolve().parents[2]
ROOT=WS.parents[1]
PUB=ROOT/'publish'/WS.name
read=lambda p:json.loads(p.read_text())
progress=read(WS/'authoring-progress.json')
manifest=read(PUB/'MANIFEST.json')
assert progress['completed_topics']==28 and manifest['totals']['topics']==28
assert not manifest['not_published']
ids=set();objectives=set();types=Counter();warnings=Counter();not_run=Counter();deviations=[]
for row in progress['rows']:
    td=WS/'topics'/row['topic'];wo=read(td/'work_order.json')
    qa=read(td/'qa_report.json')
    assert qa['release_decision']=='publish'
    assert not any(c['status']=='fail' for c in qa['deterministic_checks'])
    for c in qa['deterministic_checks']:
        if c['status']=='warn':warnings[c['check_id']]+=1
        if c['status']=='not_run':not_run[c['check_id']]+=1
    slots={s['slot']:s for s in wo['item_slots']+wo['performance_tasks']}
    source=read(td/wo['output_files']['learning_items'])['items']
    published=next(r for r in manifest['topics'] if r['topic_id']==row['topic'])
    output=read(PUB/'flashcards'/published['flashcards'])['items']
    assert len(source)==len(output)==len(slots)
    assert (td/published['notes']).read_bytes()==(PUB/'notes'/published['notes']).read_bytes()
    for item,copy in zip(source,output):
        sid=item['item_id'];assert sid not in ids;ids.add(sid)
        slot=slots[sid]
        for key in ['command_word','mark_tariff','assessment_objectives','blooms_level']:
            assert item[key]==slot[key],(sid,key)
        expected=set(slot.get('objective_ids') or [slot['objective_id']])
        assert set(item['objective_ids'])==expected
        assert all(copy['objective_titles'])
        assert {k:v for k,v in copy.items() if k!='objective_titles'}==item
        objectives.update(expected);types[item['item_type']]+=1
    deviations.extend({'topic':row['topic'],**d} for d in read(td/'authoring_notes.json')['deviations'])
assert len(ids)==458 and len(objectives)==197 and types['flashcard']==378
assert sum(types.values())-types['flashcard']==80
audit={'stage':'5 complete; final Claude semantic review pending',
 'topics':28,'blocked_topics':[],'objectives_covered':197,**progress['totals'],
 'item_types':dict(types),'rendered_notes_words':manifest['totals']['notes_words'],
 'warnings':dict(warnings),'not_run':dict(not_run),'deviations':deviations,
 'checks':['All 28 topic release decisions publish; zero deterministic failures.',
 'All 458 IDs unique and all approved commands/tariffs/AOs/Bloom labels and objective mappings preserved.',
 'Published notes match rendered sources byte-for-byte; item payloads match except generated objective titles.',
 'Claims remain unverified/publishable false pending independent semantic review.'],
 'limits':['C-18 reports topic-level item-count AO warnings; the approved marks-equivalent plan is unchanged (A801/B630/C693; largest share gap 4.16 points).',
 'C-35 and C-41 not_run: no generated graphic stimulus; approved learner construction instructions and numerical schedules are used.',
 'C-43 not_run: no extended language practice-text stimulus applies.',
 'Local publication is assembled; no authored-subject commit, push or upload performed.']}
(WS/'authoring-audit.json').write_text(json.dumps(audit,indent=2)+'\n')
lines=['# 6145 NSSCO Economics — authoring completion','',
 'Step 5 complete. 28 topics; 197 objectives; 467 claims; 28 units; 378 flashcards and 80 tasks. '+
 '49,975 content words; 52,429 rendered words including headings and generated front matter. No blocked topics.','',
 '| Topic | Claims | Units | Items | Content words | Final checks |',
 '|---|---:|---:|---:|---:|---|']
for r in progress['rows']:
    lines.append(f"| {r['topic']} | {r['claims']} | {r['units']} | {r['items']} | {r['notes_words']} | PUBLISH |")
lines+=['','All topics have zero deterministic failures. C-18 item-count warnings remain; the approved marks-equivalent balance and all item labels are preserved. '+
 'C-35/C-41 are not_run because no generated graphic stimulus is present; construction schedules follow the approved method. C-43 is not_run because language practice texts do not apply.','',
 '## Recorded deviations','']
for d in deviations:lines.append(f"- {d['topic']}: {d['from']} Changed to {d['to']} Reason: {d['why']}")
lines+=['','## Publication and next checkpoint','',
 f'Local publication: `publish/{WS.name}/INDEX.md`. All 28 notes and 28 item files verified against source. '+
 'No upload, authored-subject commit or push. Final Claude content review and Jeremy’s reading of its verdict are pending. '+
 'All 467 claims remain unverified and publishable false; deterministic PUBLISH is not semantic certification.','',
 'Existing source gaps and standard-tool limitations remain as documented in the approved plan. '+
 'The cross-topic audit and file-level counts are in authoring-audit.json.']
(WS/'AUTHORING-REPORT.md').write_text('\n'.join(lines)+'\n')
progress['note']='Step 5 complete: all 28 topics qualified and locally published. Independent Claude semantic review pending.'
(WS/'authoring-progress.json').write_text(json.dumps(progress,indent=2)+'\n')
status=(WS/'STATUS.md').read_text()
status=status.replace('- [ ] 5 Topics authored: 28 / 28 — current qualified topics and exact totals in authoring-progress.json.',
 '- [x] 5 Topics authored: 28 / 28 — 467 claims, 28 units, 458 items, 49,975 content words; all PUBLISH, zero failures, none blocked.')
status=status.replace('- [ ] 5 Published','- [x] 5 Published locally — publish/nam-6145-nssco-2026/; 28 topics, 458 items, 52,429 rendered words; no upload or push.')
start=status.index('## Next step');end=status.index('## Decisions',start)
status=status[:start]+'''## Next step

Step 5 complete in /Users/jeremytiboth/Documents/yyeni-study-resources-6145, branch nssco-6145-economics. Final topic and publication audit: AUTHORING-REPORT.md and authoring-audit.json. All 197 objectives covered; all 28 topics PUBLISH with zero deterministic failures. The local publication index is publish/nam-6145-nssco-2026/INDEX.md.

Step 6 is the final authored-subject Claude review, started by Jeremy at the playbook checkpoint. Prior Claude r1–r3 reviews examined the plan only. Review the full authored content, conditions, calculations, independent question/answer integrity and rubric quality, then repair findings and republish as needed. No authored-subject commit or push has been made; the original shared checkout remains untouched by this completion step.

'''+status[end:]
(WS/'STATUS.md').write_text(status)
print(json.dumps({'topics':28,'items':dict(types),'content_words':49975,'rendered_words':52429,'publication':str(PUB)}))
