"""Author semantic review decisions, keyed to actual prompts; independent review still required."""
import json
from pathlib import Path
W=Path(__file__).resolve().parents[1]
if (W/'planning/full-demand-audit.json').exists():
 raise SystemExit('Superseded by the full 1,008-response audit. Run apply_full_demand_repairs.py and check_full_demand_repairs.py; do not reset current labels with the old MECH-only audit.')
# Read prompts for all 151 MECH cards; inspect canonical answers/rubrics for these borderline/factual cases.
# Conservative classification: familiar definitions, named processes and stock products count as recall.
factual={'2':['077','087','134'],'5':['002','008','019'],'6':['004','006','023','029'],'7':['003','008','013','015','017','021','023'],'10':['021','027','041','048'],'11':['058','061']}
records=[];added=0
for t in map(str,range(1,13)):
 p=W/f'topics/{t}/learning-items/topic_{t}_items.json';d=json.loads(p.read_text())
 for x in d['items']:
  if x.get('subtype')!='MECH':continue
  recall=x['item_id'].split('-')[3] in factual.get(t,[])
  if recall:
   x['blooms_level']='Remember';added+=x['mark_tariff']
  records.append({'item_id':x['item_id'],'prompt':x['prompt'],'marks':x['mark_tariff'],'reviewed_demand':'recall' if recall else 'causal explanation or relational reasoning','decision_basis':'Stock fact, definition, process or product can be reproduced without explaining a new relationship; counted conservatively as recall.' if recall else 'Prompt requires a cause-to-effect explanation, comparison of consequences, or reasoning from the stated quantities/structure; not excluded from recall merely because its command is Explain/Describe.','independent_confirmation_required':True})
 p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
report={'review_type':'author semantic triage, not independent validation','coverage':'All 151 MECH prompts read; canonical answers and credit points inspected for the factual/borderline decisions. Other subtypes and activity parts are not exhaustively demand-audited here.','records':records,'conservative_recall_marks_in_mech':added,'limitation':'Adjusted total remains an estimate, not proof of the syllabus recall ceiling. The independent reviewer must confirm these decisions and sample remaining subtypes; subject-level 24% warning remains active.'}
(W/'planning/mechanism-demand-audit.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
print(len(records),'MECH cards;',added,'marks counted as recall')
