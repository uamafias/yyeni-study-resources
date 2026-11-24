"""D4 scoped trig/log authoring-record edits; no runtime generation."""
from pathlib import Path
import json,re
P=Path(__file__).resolve().parents[1];W=P.parent
p=P/'trig-model-design.json';d=json.loads(p.read_text())
def local_strings(obj):
 if isinstance(obj,dict):
  for k,v in obj.items():
   if k in ['official_award_basis','misread_policy']:continue
   if isinstance(v,str):
    if k in ['status','bloom_review_status']:obj[k]=v.replace('D2','D4').replace('D3','D4')
    elif k in ['qualifier','follow_through']and 'c.a.o.'in v and 'eligible misread'not in v:obj[k]=v+' For an eligible misread only, OD-6 A/B follow-through overrides c.a.o./not-F.T.; judge dependencies and www on gross earned awards before the one net deduction.'
   else:local_strings(v)
 elif isinstance(obj,list):
  for v in obj:local_strings(v)
local_strings(d);d['version']='0.1.4';d['status']='Stage-D D4 repaired proposal; changed-scope confirmation and Vitalis approval pending; no runtime items';d['date']='2026-11-24'
d['finite_capacity_check']['status']='run planning/d4/trig-d4-check.py; finite design checks only, no runtime generation'
d['author_checks'].update(finite_discrimination_and_cases='checks/plan-repair-d4-trig-validation.json',command='python3 work/nam-8227-nsscas-2026/workbench/planning/d4/trig-d4-check.py',syntax_check='Current D4 offline AST/KaTeX check; historical counts are not current acceptance.')
for r in d['recipes']:
 r['proposed_version']='0.1.4'
 for c in r['exemplar_cases']:c['recipe_version']='0.1.4'
 if r['recipe_id']=='WB8227-principal-inverse':
  r['branches'][0]['misread_eligibility_notes']={'status':'proposed operational interpretation; exact-manifest approval pending','same_decision':'A real-to-real or no-real-to-no-real question-datum misread may qualify when object and difficulty are unchanged. A designed no-real-solution outcome is not itself an exclusion.','changed_decision':'A real/no-real outcome flip changes the object: decide ineligibility at first use and retain normal canonical marking in all later work. A supplementary-angle coincidence cannot award an unsupported canonical conclusion.'}
p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
for rid in ['principal-inverse','trig-rform-equation','log-linear-model']:
 for folder in ['work-orders','exemplars']:
  path=W/f'{folder}/WB8227-{rid}.md';s=path.read_text().replace('0.1.3','0.1.4').replace('23 November 2026','24 November 2026').replace('Stage-D D3 repair','Stage-D D4 repair').replace('D3 repair awaits','D4 repair awaits').replace(', D3\n',', D4\n')
  s=s.replace('await the short check and owner approval','await D4 confirmation and owner approval').replace('after the short independent check','after the D4 changed-scope confirmation').replace('The D2 script is a design checker','The D4 script is a design checker')
  if rid=='principal-inverse'and folder=='work-orders':
   s+='\n## D4 designed-outcome eligibility\n\nHere “no real solution” is a designed outcome. A misread that retains the canonical real/no-real decision can qualify under OD-6 if object and difficulty are unchanged; the no-solution exclusion means creating no solution when the canonical task has one. For $(k,\\theta)=(3,-3\\pi/4)$ read as $(3,3\\pi/4)$, the comparison $3\\pi/4>\\pi/2$ and justified no-real conclusion earn all three gross awards, then one net A/B deduction: **2/3**. A decision-flipping misread is ineligible at first use and stays canonical throughout. This is a proposed operational application, pending approval with the exact manifest.\n'
  if rid=='principal-inverse'and folder=='exemplars':
   s=s.replace('The principal inverse-sine interval is $[-\\pi/2,\\pi/2]$ [P-B1]. The actual target satisfies $-3\\pi/4<-\\pi/2$ [P-M1].','The principal inverse-sine interval is $[-\\pi/2,\\pi/2]$. The actual target comparison $-3\\pi/4<-\\pi/2$ uses that bound [P-B1, P-M1].')
   s+='\n## D4 same no-real decision fixture\n\nReading the changed question’s target $-3\\pi/4$ as $3\\pi/4$ retains the designed no-real decision and comparison demand. Showing $3\\pi/4>\\pi/2$ and concluding “no real solution” earns gross P-B1/P-M1/P-A1 = 3; the proposed operational ledger deducts one A/B mark after marking, giving **2/3**. The bare interval sentence still earns no P-B1 by itself. Eligibility is decided once; a real-to-no-real outcome flip receives normal canonical marking instead.\n'
  if rid=='trig-rform-equation'and folder=='work-orders':
   s=s.replace('Let $\\alpha=\\tan^{-1}(b/a)$ and $\\beta=\\sin^{-1}(c/R)$, in degrees. b-M2 requires the transformed roots inside $\\alpha<\\theta+\\alpha<360^\\circ+\\alpha$:', 'For canonical instances, let $\\alpha=\\tan^{-1}(b/a)$ and $\\beta=\\sin^{-1}(c/R)$ in degrees; the transformed roots lie inside $\\alpha<\\theta+\\alpha<360^\\circ+\\alpha$. The b-M2 award itself is judged on the learner’s own shifted interval, as specified below:')
  if rid in ['trig-rform-equation','log-linear-model']:
   s=s.replace('c.a.o.;','c.a.o. (OD-6 eligible-misread F.T. excepted);').replace('A1 c.a.o. |','A1 c.a.o. (OD-6 eligible-misread F.T. excepted) |').replace('remain c.a.o.;','remain c.a.o. (OD-6 eligible-misread F.T. excepted);')
  path.write_text(s)
print('D4 trig/log version, authority/status, qualifiers and text notes repaired; policies left for root propagation')
