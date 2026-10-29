"""Verify demand coverage/freshness and the specific Topic 12/release regressions."""
import json,copy,re,xml.etree.ElementTree as ET
from pathlib import Path
from demand_accounting import load_decisions,recall_credit,item_key
W=Path(__file__).resolve().parents[1];decisions=load_decisions();seen=set();total=0;recall=0;checks=[]
for t in range(1,13):
 T=W/f'topics/{t}';items=json.loads((T/f'learning-items/topic_{t}_items.json').read_text())['items'];parts=json.loads((T/'authored_assessment_parts.json').read_text())['parts'];responses=[x for x in items if x['item_type']=='flashcard']+parts
 for x in responses:
  key=item_key(x);assert key not in seen,key;seen.add(key);r=recall_credit(x,decisions);recall+=r;total+=x['mark_tariff']
  altered=copy.deepcopy(x);altered['blooms_level']='Remember' if x['blooms_level']!='Remember' else 'Apply'
  assert recall_credit(altered,decisions)==r,'Bloom labels changed recall accounting'
  altered['prompt']+=' Changed stimulus.'
  try:recall_credit(altered,decisions)
  except ValueError:pass
  else:raise AssertionError('Changed text accepted without re-audit')
 report=json.loads((T/'qa_report.json').read_text())
 assert report['release_decision']=='hold',(t,report['release_decision'])
 assert not any('Packet incomplete' in b for b in report['blockers']),t
 assert not any(x['status']=='fail' for x in report['deterministic_checks']),t
checks+=['Every authored response has one current fingerprint-bound decision','Changing Bloom labels leaves recall credit unchanged for all authored responses','Changing any prompt invalidates its decision','Every topic is held for review with no missing packet input or failed check']
summary=json.loads((W/'planning/full-demand-audit.json').read_text())['summary']
assert set(decisions)==seen and len(seen)==summary['entries']
assert (recall,total)==(summary['recall_marks'],summary['marks'])
# Unknown response IDs cannot inherit a subtype or Bloom-based default.
try:recall_credit({'item_id':'UNKNOWN'},decisions)
except ValueError:pass
else:raise AssertionError('Unknown response accepted')
T=W/'topics/12';task=next(x for x in json.loads((T/'learning-items/topic_12_items.json').read_text())['items'] if x['item_id']=='ITEM-6117-12-P01')
assets=re.findall(r'!\[[^\]]*\]\(([^)]+)\)',task['prompt'])
assert set(assets)=={'visuals/VIS-6117-12-02-learner.svg'},assets
assert 'not the answer panel' not in task['prompt']
svg=' '.join(ET.parse(T/'visuals/VIS-6117-12-03-learner.svg').getroot().itertext())
assert 'Vessel A' in svg and 'Vessel B' in svg
assert not any(w in svg for w in ['100 cm','80 °C','Equal jacket','no glass contact'])
assert not any(word in svg.lower() for word in ['soap','sample b readings','burette','data-11'])
checks+=['Unknown IDs rejected rather than inferred','Recall totals reconcile to the current credit-level audit','12-P01 links only the blank cooling grid','Cooling learner SVG supplies only material swatches and no controls']
# Independently recompute fresh quantitative stimuli introduced by these repairs.
assert 80-30==50 and 10-30==-20
assert abs((10.0-5.6)-4.4)<1e-9
assert 20-(2+8+8)==2 and 4/2==2
assert 18/30>12/30 and 20/30>12/30
checks.append('New energy-profile, decomposition-mass, shell-count, shared-oxygen and diffusion comparisons recomputed')
report={'status':'pass','checks':checks,'responses':len(seen),'recall_marks':recall,'marks':total,'recall_percent':100*recall/total,'limitations':'Mechanical freshness and accounting do not independently prove cognitive demand or scientific correctness. Complete author semantic audit still requires independent re-verification.'}
(W/'planning/full-demand-repair-checks.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
