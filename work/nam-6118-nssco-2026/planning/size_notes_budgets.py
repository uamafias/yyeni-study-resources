"""Derive note depth from teaching demand, without budgeting a full essay per list member."""
from pathlib import Path
import json
W=Path(__file__).resolve().parents[1]
reg=json.loads((W/'curriculum/objective_registry.json').read_text())['objectives']
ordinary={'phys_definition':(90,150),'phys_feature':(80,140),'phys_quantitative':(180,280),'phys_graph':(160,260),'phys_procedure':(160,240),'phys_explanation':(180,280),'phys_comparison':(140,220),'phys_derivation':(200,320),'phys_container':(35,65)}
member={'phys_definition':(50,90),'phys_feature':(60,100),'phys_quantitative':(100,180),'phys_graph':(100,180),'phys_procedure':(90,150),'phys_explanation':(90,150),'phys_comparison':(90,150),'phys_derivation':(140,220)}
total=[0,0]
for p in (W/'topics').glob('*/contract.json'):
 c=json.loads(p.read_text());rs=[o for o in reg if o['topic_id']==c['topic_id'] and o['parent_id']];lo=hi=0
 for o in rs:
  table=member if '-M' in o['objective_id'] else ordinary;a,b=table[o['objective_type']];lo+=a;hi+=b
 c['depth_constraints']['word_budget']={'min':lo,'max':hi}
 c['depth_constraints']['word_budget_basis']='Derived from the explicit source/member/type depth policy in planning/size_notes_budgets.py; a short list-member explanation is not budgeted as a standalone chapter. Include definitions, mechanisms, calculations and diagram guidance where needed; do not pad to a quota.'
 c['generated_by']='standard make_contract.py plus planning/size_notes_budgets.py (word budgets only)';p.write_text(json.dumps(c,indent=2,ensure_ascii=False)+'\n');total[0]+=lo;total[1]+=hi
print('Generated notes range:',*total)
