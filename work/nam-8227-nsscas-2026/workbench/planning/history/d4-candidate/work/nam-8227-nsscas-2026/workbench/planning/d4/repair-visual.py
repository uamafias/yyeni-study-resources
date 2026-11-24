"""D4 visual design edits; no runtime authoring or source-analysis changes."""
from pathlib import Path
import json,re
P=Path(__file__).resolve().parents[1];W=P.parent
read=lambda p:json.loads(p.read_text())
def dump(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
d=read(P/'visual-design.json')
for r in d['recipes']:
 r['proposed_version']='0.1.4'
 for b in r['branches']:
  for q in b['part_specs']:
   q['bloom']['status']='D4 proposal; changed-scope confirmation then Vitalis approval pending'
 r['status']='D4 paper-design proposal; confirmation and Vitalis exact-manifest approval pending'
d['status']='D4 paper-design proposal; no runtime resources; confirmation then Vitalis approval pending'
trap=next(r for r in d['recipes']if r['recipe_id']=='WB8227-trapezium-sketch-estimate')['branches'][0]
trap['scale_slip_feedback_fixture']='At k=2, k^2 and k+2 happen to equal 2k=4. The value coincidence alone is not a numerical misconception. Seeing the correct factorised square earns b:B1 (official row04); visibly wrong log-law reasoning then loses b:B2 under its correct-working (www) requirement, even if the numerical scale coincides. The normal fixture therefore earns b1/2, total9/10. This is a feedback fixture and a proposed D4 marking clarification, not an OD-1 penalty. No domain change.'
qb=next(q for q in trap['part_specs']if q['part_id']=='b')
qb['criteria'][1]['required']='Correct visible 2k scale times own(a) final/working value; exact product or any 3sf-correct representation. Visibly wrong log-law reasoning invalidates B2 (www), even when the numeric multiplier coincides. Missing factorisation/log-law derivation alone does not prevent this B2 when the correct visible product is shown; B1 separately assesses that form/derivation.'
qb['criteria'][1]['qualifiers']=['FT','www','D4 proposed clarification; final-manifest approval pending']
dump(P/'visual-design.json',d)
a=read(P/'visual-design-asset-checks.json');a['version']='0.1.4';a['stage']='D4 paper-design records; Claude confirmation then Vitalis approval pending';a['exemplar_recomputation']='planning/d4/visual-exemplar-oracle.json; all nine cases independently recalculated'
for v in a['independent_domain_checks'].values():v['source']='planning/d4/visual-domain-checks.py and .json'
a['independent_domain_checks']['WB8227-trapezium-sketch-estimate']['strict_all_parts_unseen_capacity']=2
dump(P/'visual-design-asset-checks.json',a)
shared_line=read(P/'d4/shared-misread-policy.json')['work_order_line']
source_line='OD-6 sources: NSSCAS 2025 examiner report PDF345 item4 (`CONVENTION:108`) and Cambridge International 9709/12 March2016 mark scheme PDF3, Penalties. The Cambridge convention is comparable-board evidence adopted by Vitalis, not a Namibian published allocation. The per-datum unit, deduction order, eligibility ledger and gross-before-net dependency mechanics are proposed operational rules in MR03, pending approval of the exact manifest; they are not further owner decisions. Practice feedback names the misread.'
for folder in ['work-orders','exemplars']:
 for rid in ['WB8227-modulus-graph-recovery','WB8227-trapezium-sketch-estimate','WB8227-vector-geometry']:
  f=W/folder/(rid+'.md');s=f.read_text().replace('v0.1.3','v0.1.4').replace('stage-D3 repair','stage-D4 repair').replace('stage-D3 design repair','stage-D4 design repair').replace('D3 v0.1.4','D4 v0.1.4').replace('Claude D3 confirmation','Claude D4 changed-scope confirmation').replace('Claude D4 changed-scope confirmation of D1','Claude D4 changed-scope confirmation of this design').replace('planning/d3/visual','planning/d4/visual')
  s=s.replace('Owner decision6 includes this demand','The 16 November owner decision 6 (visual demands) includes this demand').replace('under owner decision6','under the 16 November owner decision 6 (visual demands)').replace('owner decision6','the 16 November owner decision 6 (visual demands)').replace('Owner decision6','The 16 November owner decision 6 (visual demands)')
  s=s.replace('**Shared rules `subject-rules.md` D1-MR01–09 bind every row.**','**Shared rules `subject-rules.md` D1-MR01–09 apply with their stated authority: OD-backed principles bind; proposed operational details await exact-manifest approval.**')
  s=s.replace('Visible wrong logarithm reasoning loses b:B1; a valid visible own(a) product may still earn b:B2.','Seeing the factorised square retains b:B1 (official row04). Visibly wrong log-law reasoning then loses b:B2 under its correct-working (www) requirement, even when k=2 makes the numerical scale coincide; the fixture earns b1/2, total9/10. This is a proposed D4 marking clarification, not an OD-1 penalty.')
  s=re.sub(r'^OD-6 sources:.*$',lambda m:source_line,s,flags=re.M)
  for heading in [r'^\*\*Misread per part `a`:\*\*.*$',r'^\*\*Misread per part \(OD-6 / D1-MR03\):\*\*.*$',r'^\*\*Per-part misread policy \(OD-6 / D1-MR03\):\*\*.*$']:
   s=re.sub(heading,lambda m:shared_line,s,flags=re.M)
  # A short older exemplar summary is superseded by the single shared MR03 pointer.
  s=s.replace('- OD-6 applies once per genuinely misread datum at its first-use part; all A/B follow through with correct misread-data work, M/DM as usual. Later parts using that datum receive no second deduction. Own figures, easier/changed/no-solution tasks use ordinary canonical marking; no earned A/B means no deduction. OD-1/OD-5 still bind.','- OD-6 governs the misread principle; apply the single proposed operational settlement in subject-rules MR03. Deduct after gross marking from the first A/B earned on the datum anywhere in question order; dependencies retain gross awards. Eligibility is decided once and reused. Practice feedback names the misread. OD-1/OD-5 remain scoped to their named rules.')
  old='D3 edge fixtures: in the changed case, misreading $OA=(1,2,1)$ as $(1,-2,1)$ makes $OA\\cdot OC=0$ while $OB\\cdot OC=-3$, so no $p$ solves the altered question. OD-6 is ineligible (no solution); a correct zero-dot setup earns a:M1 only, not MR follow-through accuracy. Misreading one of the learner\'s own computed components is ordinary accuracy marking. If no A/B is earned in the first-use part, no deduction is made or carried into a later part. Later E/F must retain a fixture for a more precise angle such as $79.98^\\circ$: this D3 repair does not settle that response-form decision.'
  new='D4 ineligible-reuse fixture: in the changed case, misreading $OA=(1,2,1)$ as $(1,-2,1)$ gives $OA\\cdot OC=0$ and $OB\\cdot OC=-3$, so no $p$ solves the altered question. Eligibility is recorded as false once and remains false in (b). A visible zero-dot attempt earns a:M1 only, 1/3. In (b), the learner\'s dot is −6, the correct magnitudes are $\\sqrt6$ and $\\sqrt{11}$, and the resulting angle is $137.6^\\circ$. Canonical marking awards only b:M1 and b:M2, 2/4; **total3/7**, with no MR penalty and no MR accuracy follow-through. Own-figure miscopies are ordinary accuracy errors. The later acceptance decision for a more precise angle such as $79.98^\\circ$ remains open.'
  s=s.replace(old,new)
  if 'trapezium' in rid:
   s=s.replace('Correct visible $2k$ times their own(a) value, as present in the coherent final answer or working.', 'Correct visible $2k$ times their own(a) value, as present in the coherent final answer or working, with no visibly wrong log-law reasoning (www). Missing factorisation/log-law derivation alone does not prevent B2 when the correct visible product is shown; B1 assesses the form/derivation separately.')
   s=s.replace('A wrong scale does not earn the mark; the numerical result alone does not show the hence method.','A wrong scale, or a scale reached by visibly wrong log-law working (www), does not earn b:B2; a numerical coincidence alone does not establish the hence method. A correctly seen factorised square still earns b:B1.')
   s=s.replace('Correct visible$2k$ times **their(a)**, exact or correct3sf;','Correct visible$2k$ times **their(a)** with correct working (www), exact or correct3sf;')
  if 'vector' in rid:
   insert='\nD4 deferred-deduction fixture: in the normal case, genuinely misread $OB=(-2,1,-1)$ and then use the named wrong resultant $p(OA-OB)$. The visible zero-dot equation gives a:M1 only, 1/3; correct misread-data work in (b) earns all four gross awards. The first A/B earned on this datum is b:B1, so apply the one net MR deduction there: b3/4, **total4/7**, not5/7. The named error is not rescued and the deduction never removes the gross award used by a dependency. Practice feedback names both the miscopied sign and the separate resultant error.\n'
   if 'D4 deferred-deduction fixture:'not in s:s+='\n'+insert
  f.write_text('\n'.join(x.rstrip()for x in s.splitlines())+'\n')
# Preserve the three existing IDs while distinguishing OD-5 from the proposed B2 detail.
rows=read(P/'d3/visual-deviation-rows.json');row=rows['rows'][0]
row.update(part='d:DB1 (OD-5 settled); b:B2 (D4 proposed clarification)',departure=row['departure']+' Separately, the D4 b:B2 clarification applies a wrong-working exclusion (www): correct factorisation retains b:B1, while a visibly wrong-law coincident multiplier loses b:B2. Missing derivation alone does not remove B2 for a correct visible product.',rationale=row['rationale']+' The b:B2 clarification is a proposed marking interpretation; it is not attributed to OD-1 or to the OD-5 owner extension.',approval='OD-5 DB1 extension accepted; D4 b:B2 interpretation and final plan approval pending',status_class='owner-accepted DB1 extension; proposed B2 criterion interpretation')
dump(P/'d4/visual-deviation-rows.json',rows)
print('D4 visual source edits saved; seven shared policies await root propagation')
