"""Audit source integrity, demand completeness, quoted anchors and derived counts."""
from pathlib import Path
from collections import Counter
import json,hashlib,re
import jsonschema
ROOT=Path(__file__).resolve().parents[3];W=ROOT/'work/nam-6118-nssco-2026'
def j(p):return json.loads((W/p).read_text())
def norm(s):return ' '.join(s.split())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
def ck(label,condition):
 assert condition,label
 checks.append(label)
manifest=j('assessment-evidence/extraction-manifest.json')
for r in manifest['records']:
 ck('Source hash '+r['source_id'],sha(ROOT/r['path'])==r['sha256'])
 for mode,out in r['outputs'].items():ck('Extraction hash '+r['source_id']+' '+mode,sha(W/out['path'])==out['sha256'])
ev=j('assessment-evidence/assessment_evidence.json');jsonschema.validate(ev,json.loads((ROOT/'standard/v0.2.0-draft/schemas/assessment_evidence.schema.json').read_text()));ck('Evidence schema',True)
rs=ev['records'];by={r['evidence_id']:r for r in rs};ck('Unique 622 demand IDs',len(by)==len(rs)==622)
idx={o['objective_id'] for o in j('curriculum/source-objective-index.json')['objectives']}|{'6118-ANNEX-D-01'}
for y in range(2020,2026):
 for p,total in [('1',40),('2',80),('3',40)]:
  parts=[r for r in rs if r['year']==y and r['paper_id']==p]
  ck(f'{y} P{p} marks',sum(r['mark_tariff'] for r in parts)==total)
  if p=='1':ck(f'{y} forty distinct MC numbers',{int(r['question_ref']) for r in parts}==set(range(1,41)))
ck('All demand objective IDs are real anchors',all(set(r['objective_ids'])<=idx for r in rs))
ck('Every mapping records semantic method',all(any('manual_semantic' in n for n in r['notes']) for r in rs))
ck('2025 fuse meaning correction',by['6118-2025-P2-027']['objective_ids']==['6118-5.5-04'] and 'fuse' in by['6118-2025-P2-027']['context_summary'])
detail=j('assessment-evidence/demand-review.json')['records'];usable={r['evidence_id'] for r in detail if r['usable_for_exposure']}
ck('Compensated item alone excluded',set(by)-usable=={'6118-2024-P1-009'})
ck('Usable 959 marks',sum(by[k]['mark_tariff'] for k in usable)==959)
# Commentary wording is preserved line-by-line from the located native pages.
comment=j('assessment-evidence/report-commentary.json')['records'];cb={f['finding_id']:f for f in comment}
for f in comment:
 source=(W/f"planning/extracted/{f['year']}-report.layout.txt").read_text()
 source_pages=[]
 for p in f['pdf_pages']:
  m=re.search(rf'=== SOURCE PDF PAGE {p} ===(.*?)(?==== SOURCE PDF PAGE|\Z)',source,re.S);assert m,(f['finding_id'],p)
  source_pages.append(m[1])
 original=norm(' '.join(source_pages))
 ck('Commentary source lines '+f['finding_id'],all(norm(line) in original for line in f['internal_verbatim'].splitlines() if line.strip()))
 ck('Commentary source demand links '+f['finding_id'],all(e in by and by[e]['year']==f['year'] and by[e]['paper_id']==f['paper_id'] for e in f['linked_evidence_ids']))
for m in j('curriculum/misconceptions.json')['entries']:
 ck('Curated misconception located '+m['entry_id'],all(fid in cb and norm(m['internal_verbatim_anchor']).lower() in norm(cb[fid]['internal_verbatim']).lower() for fid in m['finding_ids']))
 ck('Curated misconception objective '+m['entry_id'],set(m['objective_ids'])<=idx)
keys=j('assessment-evidence/published-mc-keys.json')['records'];ck('Five complete MC key tables',len(keys)==5 and all(set(k['answers'])=={str(n) for n in range(1,41)} for k in keys))
ck('199 answers and compensation marker',Counter(a for k in keys for a in k['answers'].values())['*']==1 and sum(a in 'ABCD' for k in keys for a in k['answers'].values())==199)
for shape in j('curriculum/answer-shapes.json')['entries']:
 y=by[shape['evidence_ids'][0]]['year'];p=shape['source_pdf_page'];path=W/f'planning/extracted/{y}-report.layout.txt'
 if shape['source_read_method'] in ('source_image_checked_with_OCR_anchor','manually_checked_OCR_table'):
  source=(W/f'planning/extracted/{y}-report.ocr-draft.txt').read_text()
 else:source=path.read_text()
 ck('Shape quote '+shape['shape_id'],norm(shape['internal_verbatim_anchor']).lower() in norm(source).lower())
 ck('Shape tariff '+shape['shape_id'],all(by[e]['mark_tariff']==shape['mark_tariff'] for e in shape['evidence_ids']))
ex=j('curriculum/exam-exposure.json')
for o in ex['objectives']:
 raw=[r for r in rs if o['objective_id'] in r['objective_ids']]
 for label,arr in [('evidence',raw),('usable_evidence',[r for r in raw if r['evidence_id'] in usable])]:
  v=o[label];ck('Exposure '+o['objective_id']+' '+label,v['question_parts_naming_it']==len(arr) and v['distinct_series']==len({r['year'] for r in arr}) and v['max_mark_tariff']==max((r['mark_tariff'] for r in arr),default=0) and v['command_words_observed']==dict(Counter(r['command_word'] for r in arr if r['command_word'])) and set(v['evidence_ids'])=={r['evidence_id'] for r in arr})
 n=o['usable_evidence']['distinct_series'];ck('Exposure class '+o['objective_id'],o['exposure_class']==('frequent' if n>=3 else 'occasional' if n==2 else 'rare' if n==1 else 'unseen'))
ck('Primary content shares 719 marks',sum(x['primary_content_marks'] for x in ex['primary_content_topic_shares'])==719)
for t in ex['primary_content_topic_shares']:
 arr=[r for r in rs if r['evidence_id'] in usable and r['paper_id'] in ('1','2') and (r['objective_ids'][0].split('-')[1].split('.')[0] if 'ANNEX' not in r['objective_ids'][0] else '5')==t['topic_id']]
 ck('Primary topic share '+t['topic_id'],t['primary_content_marks']==sum(r['mark_tariff'] for r in arr))
cc=j('curriculum/command-word-census.json')
ck('Primary imperative coverage 379',sum(c['observed_count'] for c in cc['commands'])==379 and len(cc['unlabelled_structured_practical'])==3)
for c in cc['commands']:
 arr=[r for r in rs if r['command_word']==c['word']];tc=Counter(r['mark_tariff'] for r in arr)
 ck('Command counts '+c['word'],c['observed_count']==len(arr) and c['observed_tariffs']==sorted(tc) and c['modal_tariffs']==sorted(k for k,v in tc.items() if v==max(tc.values())))
for e in j('curriculum/scope-scan.json')['entries']:
 ck('Scope catches '+e['construct'],all(re.search(e['pattern'],s,re.I) for s in e['controls']['must_catch']))
 ck('Scope allows '+e['construct'],all(not re.search(e['pattern'],s,re.I) for s in e['controls']['must_allow']))
ck('Partial marking coverage honestly retained',ev['status']=='partial' and sum(bool(r['creditworthy_points']) for r in rs)==355)
report=dict(status='pass',date='2026-10-31',checks_passed=len(checks),checks=checks,limits=['No independent semantic review is implied.','No claim that every memo row, scientific source answer or exam image has been verified.','This audit validates Step 3 evidence, not uncreated topic publication artifacts.'])
(W/'review/corpus-verification.json').write_text(json.dumps(report,indent=2)+'\n')
print(f'PASS: {len(checks)} checks; source/extraction integrity, all 18 mark totals, schema, located quotations, mapping IDs, exposure, command census and bounded scope examples.')
