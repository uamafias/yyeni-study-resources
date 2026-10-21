"""Recompute the Step 3 ledger, raw-mode tariffs, exposures, links and scope controls."""
import json,re,hashlib
from pathlib import Path
from collections import Counter
WS=Path(__file__).resolve().parents[1];REPO=WS.parents[1];EV=WS/'assessment-evidence';CUR=WS/'curriculum'
def load(p):return json.loads(p.read_text())
# Step 4 has its own canonical registry map. Recheck the unchanged Step 3 bridge
# snapshots when present, rather than expecting those 102 bridge IDs downstream.
SNAP=WS/'planning'
def original(name, live):
 p=SNAP/name
 return load(p if p.exists() else live)
r=original('source-bullet-evidence.json',EV/'assessment_evidence.json')['records'];sources=load(EV/'source-manifest.json')
assert len(r)==419 and len({x['evidence_id'] for x in r})==419
assert sum(x['mark_tariff'] for x in r)==1000
paper_checks=[]
for source in sources:
 assert hashlib.sha256((REPO/source['path']).read_bytes()).hexdigest()==source['sha256']
 for mode in ['raw','layout']:
  assert len((EV/'extracted'/f'{source["source_id"]}-{mode}.txt').read_text())>500
 if source['kind']!='question_paper':continue
 rs=[x for x in r if x['source_id']==source['source_id']]
 raw=(EV/'extracted'/f'{source["source_id"]}-raw.txt').read_text()
 raw_tariffs=[int(n) for n in re.findall(r'\[(\d+)\]',raw) if 1<=int(n)<=6]
 assert [x['mark_tariff'] for x in rs]==raw_tariffs,source['source_id']
 expected={'P1':80,'P2':70,'P3':50}[source['paper_id']]
 assert sum(raw_tariffs)==expected
 byroot=Counter()
 for x in rs:byroot[x['question_ref'].split('(')[0]]+=x['mark_tariff']
 if source['paper_id']=='P1':assert dict(byroot)=={'1':20,'2':20,'3':20,'4':20}
 elif source['paper_id']=='P2':assert dict(byroot)=={'1':35,'2':35}
 else:assert byroot['3']==15 and byroot['1']+byroot['2']==35
 paper_checks.append({'source_id':source['source_id'],'parts':len(rs),'marks':sum(raw_tariffs),'raw_layout_ordered_tariffs':'PASS','root_totals':dict(byroot)})
assert len(paper_checks)==15
assert all(x['command_word']!='unresolved' and x['objective_ids'] and x['primary_topic_id'] for x in r)
facts=load(CUR/'syllabus-facts.json')
valid={f'SB-6136-{t["id"]}-{i:02d}' for t in facts['content_outline'] for i in range(1,len(t['specific_objectives'])+1)}
assert all(set(x['objective_ids'])<=valid for x in r)
exp=original('source-bullet-exposure.json',CUR/'exam-exposure.json')
assert len(exp['objectives'])==102 and {x['objective_id'] for x in exp['objectives']}==valid
for o in exp['objectives']:
 rs=[x for x in r if o['objective_id'] in x['objective_ids']]
 assert o['times_examined']==len(rs)
 assert o['marks_examined_overlap']==sum(x['mark_tariff'] for x in rs)
 assert set(o['evidence_ids'])=={x['evidence_id'] for x in rs}
 assert o['command_words']==dict(Counter(x['command_word'] for x in rs))
 assert o['distinct_years']==len({x['year'] for x in rs})
 years=o['distinct_years'];expected='frequent' if years>=4 else 'occasional' if years>=2 else 'rare' if years else 'unseen'
 assert o['exposure_class']==expected
for t in exp['topics']:
 rs=[x for x in r if x['primary_topic_id']==t['topic_id']]
 assert t['parts']==len(rs) and t['marks']==sum(x['mark_tariff'] for x in rs)
assert sum(t['marks'] for t in exp['topics'])==1000
commands=load(EV/'command-word-counts.json')['commands']
assert sum(c['count'] for c in commands)==419
assert sum(c['mark_total'] for c in commands)==1000
for c in commands:
 rs=[x for x in r if x['command_word']==c['word']]
 assert c['count']==len(rs)
 assert {int(k):v for k,v in c['tariffs_seen'].items()}==dict(Counter(x['mark_tariff'] for x in rs))
 assert set(c['evidence_ids'])=={x['evidence_id'] for x in rs}
 bytariff=Counter(x['mark_tariff'] for x in rs)
 assert c['modal_tariffs']==[n for n,count in sorted(bytariff.items()) if count==max(bytariff.values())]
scopes=load(CUR/'scope-scan.json')['entries']
for entry in scopes:
 regex=re.compile(entry['pattern'],re.I)
 assert all(regex.search(s) for s in entry['controls']['must_catch']),entry['construct']
 assert not any(regex.search(s) for s in entry['controls']['must_allow']),entry['construct']
mis=original('source-bullet-misconceptions.json',CUR/'misconceptions.json')['entries'];shapes=load(CUR/'answer-shapes.json')['6136']['shapes']
ids={x['evidence_id'] for x in r}
for m in mis:
 assert m['evidence_id'] in ids
 assert set(m['objective_ids'])<=valid
 assert m['a']!=m['b'] and m['discrimination_test'].endswith('?')
for shape in shapes:
 assert set(shape['evidence_ids'])<=ids
 for eid in shape['evidence_ids']:
  question=next(x for x in r if x['evidence_id']==eid)
  assert shape['marks']==question['mark_tariff'] and shape['command']==question['command_word']
for entry in mis+shapes:
 loc=entry['source_locator'];sid=next(s['source_id'] for s in sources if s['path']==loc['path'])
 s=next(s for s in sources if s['source_id']==sid)
 assert s['pdf_page_range'][0]<=loc['pdf_page']<=s['pdf_page_range'][1]
 assert loc['printed_page']+2==loc['pdf_page']
comments=load(EV/'report-comments-index.json')
assert all(c['evidence_id'] is None or c['evidence_id'] in ids for c in comments)
result={'result':'PASS','paper_checks':paper_checks,'papers':15,'annual_reports':5,'extraction_files':40,'question_parts':419,'marks':1000,
 'source_bullet_exposures':102,'curated_misconceptions':len(mis),'report_backed_answer_shapes':len(shapes),
 'scope_patterns_tested':len(scopes),'report_comments_indexed':len(comments),'report_comments_joined':sum(c['evidence_id'] is not None for c in comments),
 'limitations':['No standalone mark schemes or 2025 sources','Proof versions in 2021–2023','Source-bullet IDs precede Step 4 decomposition','Semantic mappings and conceptual curation are human/agent judgements; mechanical checks cannot prove meaning','Report text indexing is not an exhaustive count of unique errors','No learner resources or publication gate tested']}
(EV/'corpus-validation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='paper_checks'},indent=2))
