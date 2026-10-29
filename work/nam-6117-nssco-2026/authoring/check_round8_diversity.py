"""Validate current changes, closed-book coverage and full source manifest."""
import json,math,hashlib,copy
from pathlib import Path
from round8_diversity import CHANGES
from round10_repairs import card as apply_round10
from round7_replacements import CHANGES as PREVIOUS
from round9_repairs import CARDS as LATEST,apply_card as apply_latest
from final_content_edits import CARDS as FINAL,apply_card as apply_final
W=Path(__file__).resolve().parents[1];R=W.parents[1];items={}
for t in range(1,13):
 for x in json.loads((W/f'topics/{t}/learning-items/topic_{t}_items.json').read_text())['items']:
  if x['item_type']=='flashcard':items['-'.join(x['item_id'].split('-')[2:4])]=x
rows={r['id']:r for r in json.loads((W/'planning/full-demand-audit.json').read_text())['records']}
for k,c in (PREVIOUS|CHANGES|LATEST|FINAL).items():
 c=copy.deepcopy(c);apply_latest(c,k);apply_final(c,k);apply_round10(c,k)
 for f in ['prompt','canonical_answer','marking_guidance']:assert items[k][f]==c[f],(k,f)
 assert rows[items[k]['item_id']]['recall_marks']==c['recall'],k
coverage={'lithium':'8-015','sodium':'8-015','potassium':'8-019','calcium':'8-021','barium':'8-019','ammonia':'8-037','carbon_dioxide':'8-039','chlorine':'8-042','hydrogen':'8-043','oxygen':'8-045','carbonate':'8-026','chloride':'8-028','bromide':'8-030','iodide':'8-032','nitrate':'8-034','sulfate':'8-036'}
for name,k in coverage.items():assert rows[items[k]['item_id']]['recall_marks']>0,(name,k)
assert items['10-032']['command_word']=='State'
assert items['12-014']['subtype']=='CALC' and items['12-014']['command_word']=='Calculate'
assert items['12-014']['objective_ids']==['OBJ-6117-12.2-02']
assert math.isclose((24.80-.20)-(1.20-.20),23.60)
wire=[k for k,x in items.items() if k.startswith('8-0') and 15<=int(k.split('-')[1])<=24 and 'wire' in x['prompt'].lower() and 'blank' in x['prompt'].lower()];assert wire==['8-017'],wire
manifest=json.loads((W/'review/copied-wording-sources.json').read_text());assert manifest['paths_scanned']==28 and manifest['distinct_file_contents']==24
for r in manifest['sources']:assert hashlib.sha256((R/r['path']).read_bytes()).hexdigest()==r['sha256']
p=json.loads((W/'planning/production-progress.json').read_text());assert (p['recall_marks'],p['marks'])==(392,1637)
report={'status':'pass','recall_marks':392,'marks':1637,'recall_percent':100*392/1637,'ao_marks':p['ao_marks'],'closed_book_coverage':{k:items[v]['item_id'] for k,v in coverage.items()},'wire_blank_cards_in_flame_cluster':wire,'copied_wording_source_paths':28,'distinct_source_contents':24,'current_revisions':[{'item_id':items[k]['item_id'],'prompt':items[k]['prompt'],'answer':items[k]['canonical_answer'],'credit':items[k]['marking_guidance'],'recall_marks':rows[items[k]['item_id']]['recall_marks']} for k in CHANGES],'limits':'Coverage is a direct text/credit check, not independent certification of every objective or cognitive-demand judgement.'}
(W/'planning/round8-diversity-checks.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n');print({k:v for k,v in report.items() if k!='current_revisions'})
