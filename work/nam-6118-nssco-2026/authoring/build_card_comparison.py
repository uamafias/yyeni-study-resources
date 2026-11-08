"""Build the teacher-only comparison from complete, read-only YYeni page snapshots.
Usage: python build_card_comparison.py /private/tmp/6118-existing-card-report
Raw classroom card text is not copied into the repository report.
"""
from pathlib import Path
import sys,json,collections,hashlib,unicodedata,html,re,datetime
W=Path(__file__).resolve().parents[1];P=Path(sys.argv[1])
read=lambda p:json.loads(p.read_text())
pages={int(p.stem.split('-')[1]):read(p) for p in P.glob('page-*.json')};cards=[];n=0
while True:
 page=pages[n];assert page['total']==1429;cards+=page['cards']
 if page['next_offset'] is None:break
 assert page['next_offset']==n+len(page['cards']);n=page['next_offset']
assert len(cards)==1429==len({c['card_id'] for c in cards})
assert all(c['is_active'] is True and c['learner_owner_id'] is None for c in cards)
lessons=read(P/'lessons.json');assert len(lessons)==196==len({x['id'] for x in lessons});lessonmap={x['id']:x for x in lessons}
assert all(c['lesson_id'] in lessonmap for c in cards)
items=[i for t in range(1,29) for i in read(W/f'topics/{t}/learning-items/topic_{t}_items.json')['items']];new=[i for i in items if i['item_type']=='flashcard'];assert len(new)==616 and len(items)==693
norm=lambda s:re.sub(r'\s+',' ',html.unescape(unicodedata.normalize('NFKC',s or '')).casefold()).strip()
digest=lambda s:hashlib.sha256(norm(s).encode()).hexdigest()
qa=lambda q,a:digest(q+'\n'+a)
oldq=collections.defaultdict(list);oldqa=collections.defaultdict(list)
for c in cards:oldq[digest(c['question'])].append(c['card_id']);oldqa[qa(c['question'],c['answer'])].append(c['card_id'])
exact=[];sameq=[];unmatched=[]
for c in new:
 key=qa(c['prompt'],c['canonical_answer']);qkey=digest(c['prompt'])
 if key in oldqa:exact.append(dict(item_id=c['item_id'],existing_card_ids=oldqa[key],match='normalized question and answer text'))
 elif qkey in oldq:sameq.append(dict(item_id=c['item_id'],existing_card_ids=oldq[qkey],match='same normalized question, different answer text; semantic review needed'))
 else:unmatched.append(c['item_id'])
assert len(exact)+len(sameq)+len(unmatched)==616
old_section=collections.Counter(lessonmap[c['lesson_id']]['section'] for c in cards)
new_section=collections.Counter()
for c in new:
 t=int(c['item_id'].split('-')[2]);name='Scientific processes' if t<=3 else 'General Physics' if t<=11 else 'Thermal Physics' if t<=15 else 'Properties of waves' if t<=20 else 'Electricity and magnetism' if t<=26 else 'Nuclear Physics';new_section[name]+=1
section_rows=[dict(section=s,existing_active_cards=old_section[s],new_flashcards=new_section[s],existing_lessons=sum(l['section']==s for l in lessons)) for s in dict.fromkeys(l['section'] for l in lessons)]
old_bloom=collections.Counter(c['bloom_level'] or 'not recorded' for c in cards);new_bloom=collections.Counter(c['blooms_level'] for c in new)
img=[c['item_id'] for c in new if re.search(r'!\[[^\]]*\]\(',c['canonical_answer'])]
report=dict(report='Existing YYeni Physics classroom cards compared with the reviewed repository deck',generated_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),scope=dict(school_id=68,school='2026 Angra Pequena SSS',classroom_id='b718027a-df8e-4062-a7d6-aa6c3ba6da5a',classroom='NSSCO PHYSICS (6118)',source='YYeni browse_flashcards; every page from offset 0 through 1400, final next_offset null; curriculum sections/lessons fully paginated',read_only=True,archived_history='Not enumerated by the shared-active-card browse; no historical archive total claimed.'),totals=dict(existing_active_shared_cards=len(cards),new_flashcards=len(new),new_assessment_tasks=77,new_total_repository_items=693,new_topic_count=28,existing_missing_bloom=sum(c['bloom_level'] is None for c in cards),existing_missing_max_mark=sum(c['max_mark'] is None for c in cards),new_missing_bloom=sum(not c.get('blooms_level') for c in new),new_missing_max_mark=sum(not c.get('mark_tariff') for c in new),existing_cards_with_image_urls=sum(bool(c.get('question_image_url') or c.get('answer_image_url')) for c in cards),new_cards_with_markdown_answer_figures=len(img),new_cards_with_exact_question_answer_match=len(exact),new_cards_with_same_question_different_answer=len(sameq),new_cards_with_no_exact_question_match=len(unmatched),existing_exact_qa_duplicate_groups=sum(len(v)>1 for v in oldqa.values()),existing_extra_exact_qa_duplicates=sum(len(v)-1 for v in oldqa.values() if len(v)>1)),sections=section_rows,existing_bloom_counts=dict(old_bloom),new_bloom_counts=dict(new_bloom),existing_card_type_counts=dict(collections.Counter(c['card_type'] or 'not recorded' for c in cards)),matches=dict(exact_question_and_answer=exact,same_question_different_answer=sameq,new_no_exact_question_match_ids=unmatched),new_markdown_figure_item_ids=img,method=['Unicode NFKC, HTML entity decoding, case folding and whitespace normalization only; punctuation, numbers, equations and figure references are retained.','Question-and-answer equality is a text match, not approval to reuse legacy cards or their metadata. Same question with a different answer does not establish that either answer is wrong.','Section groupings compare broad curriculum areas; they are authored grouping judgements, not an independent objective-to-objective coverage audit.','No semantic completeness or quality score is inferred from card totals, metadata or string similarity.','Existing card bodies and learner data are excluded from this report. Private input snapshots stay outside Git.'],import_decisions=['Do not append or replace automatically from this comparison.','Map the 28 repository topics to the existing lessons before import.','Retain the 77 assessment tasks as separate resources; do not import them as flashcards.','Convert local Markdown figures to managed YYeni assets and verify question/answer rendering at import.','Review same-question/different-answer pairs before deciding which existing cards to retain, update or archive.','Any import, archive or learner assignment remains a separate explicitly approved platform operation.'],retained_caveats=['267 marking-evidence gaps and partial 355/622 demand coverage.','Independent demand-to-syllabus mappings and 2022/2023 First Proof equivalence unresolved.','C-35/C-41 remain not_run; author checks do not substitute for full independent review.','Markdown image answers have not been verified on the platform.'],source_fingerprints=[dict(offset=k,count=len(v['cards']),sha256=hashlib.sha256((P/f'page-{k}.json').read_bytes()).hexdigest()) for k,v in sorted(pages.items())])
out=W/'review/yyeni-card-comparison.json';out.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(report['totals'],indent=2));print(json.dumps(section_rows,indent=2))
