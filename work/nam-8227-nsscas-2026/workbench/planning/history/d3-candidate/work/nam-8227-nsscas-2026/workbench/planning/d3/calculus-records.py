"""D3 calculus review receipts, with readable proposed deviations."""
from pathlib import Path
import json,hashlib,subprocess,sys,concurrent.futures
H=Path(__file__).resolve().parent;W=H.parent.parent;repo=W.parents[2]
load=lambda p:json.loads(p.read_text());save=lambda p,v:p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n')
rows=load(W/'planning/d2/calculus-deviations.json')
source_rows=[
'2023 P2 Q8(a), AWARD03; report PDF339: derivative of 4y and constant zero.',
'2023 P2 Q8(a), AWARD04; report PDF339: E1 establishing the supplied target.',
'2023 P2 Q8(b), AWARD05–06; report PDF339: point recovery and gradient substitution.',
'2021 P2 Q10(b), AWARD04–06; report PDF241: normal gradient, construction and accuracy.',
'2025 P2 Q5, AWARD01–05; report PDF359: five-mark implicit gradient route.',
'2021 P1 Q11(a), AWARD04; report PDF234: full stationary coordinate.',
'2025 P1 Q9(b), AWARD07; report PDF351: stationary x accuracy.',
'2025 P1 Q9(c), AWARD08–09; report PDF351: M1/B1 single minimum classification.',
'2023 P2 Q8(a), AWARD01–04; report PDF339: product/remaining-term/target proof.',
'2025 P2 Q5, AWARD05; report PDF359: C.A.O. accuracy, without an explicit www restriction.'
]
departures=[
'Replace the source linear-y derivative by the y² derivative 2yy′, retaining one B1.',
'Normalise terminal E1 to A1 while retaining the complete correct forward proof requirement.',
'Supply P instead of requiring recovery of its y-axis coordinate; retain two substitution marks.',
'Supply P instead of recovering its y-value from the curve; retain M1/DM1/A1.',
'Use an exclusive explicit-root allocation: quadratic solve, correct local root, differentiation, point substitution and www gradient.',
'Require both stationary coordinates for the final A1 within the same four-mark location budget.',
'Require the full stationary coordinate instead of x alone within the same three-mark location budget.',
'Use a proposed B1/M1/A1 three-mark classification tariff for mixed extrema and inflexions; routine sign tests remain Apply3 under OD-4.',
'Map valid divided and log-absolute proofs to S1–S4. Back-substitution belongs only in S4; the explicit-root identity may occupy S3.',
'Add a www gate to gradient-only G5, requiring a correct differentiated expression; retain the unqualified H2 numeric accuracy in the extended branch.'
]
rationales=[
'Keep explicit implicit-chain and constant-zero evidence on the newly authored curve.',
'Use the common M/A/B vocabulary without changing the evidence, dependency or tariff.',
'Avoid re-awarding differentiation in the later gradient part and disclose the scaffold difference.',
'Retain the normal-construction evidence while disclosing the changed givens.',
'A complete valid alternative earns the same five-mark cap; store its actual method path rather than fabricated product-rule evidence.',
'The selected cubic has two stationary points, so its response must address the complete pair.',
'A curve-point request includes both coordinates; OD-1 still prohibits unsupported answers.',
'Separate actual derivative behaviour, a valid classification test and a justified type; first-derivative signs alone suffice.',
'Credit complete valid forward proofs fairly at one four-mark cap, with no follow-through into a supplied target.',
'The wrong exponential index gives the right point gradient in all27 admitted cases at x=0. G5 must not endorse wrong working; H1/H2 follows its separately evidenced application rubric.'
]
for i,row in enumerate(rows):
 row.update(official_row=source_rows[i],departure=departures[i],rationale=rationales[i],status='Proposed marking adaptation; Claude D3 confirmation and Vitalis approval of the exact final manifest are pending.',status_class='proposed-adaptation',recipe_version='0.1.3')
 row['file_locator']='work/nam-8227-nsscas-2026/workbench/work-orders/'+row['recipe_id']+'.md'
rows[8]['departure']+=' D3 clarifies the invalid ln(y) route at the negative supplied branch: no S1/S2/S4; separately correct S3 evidence only, maximum 1/4.'
rows[7]['rationale']+=' Its former Analyse claim is superseded by owner OD-4; only the tariff adaptation remains proposed.'
save(H/'calculus-deviations.json',rows)
negatives=[('calculus-design-check.py',n)for n in ['implicit-chain','implicit-original','proof-given-answer-credit','index-error-accuracy-credit','classification-analyse','alternative-proof-missing-slot']]+[('calculus-misread-check.py',n)for n in ['missing-policy','double-deduction','no-accuracy-negative-total','proof-target-follow-through','back-substitution-in-S3','normal-positive-reciprocal','invalid-log-full-credit']]
def run(seed):
 script,name=seed;p=subprocess.run([sys.executable,str(H/script),'--negative-fixture',name],capture_output=True,text=True)
 assert p.returncode!=0,('Negative did not fail',seed)
 return dict(script=script,negative_fixture=name,status='rejected',exit_code=p.returncode,diagnostic=p.stderr.strip().splitlines()[-1])
with concurrent.futures.ThreadPoolExecutor(max_workers=4)as pool:results=list(pool.map(run,negatives))
save(H/'calculus-negative-fixtures.json',dict(status='pass',seeds=len(results),results=results,scope='D3 planner contracts and evidence expectations, no runtime marker tested.'))
files=['work-orders/WB8227-implicit-normal.md','work-orders/WB8227-stationary-inflexion.md','exemplars/WB8227-implicit-normal.md','exemplars/WB8227-stationary-inflexion.md','planning/calculus-design.json','planning/calculus-source-reads.md','planning/d3/calculus-domain-audit.json','planning/d3/calculus-exemplar-oracle.json','planning/d3/calculus-misread-oracle.json','planning/d3/calculus-negative-fixtures.json','planning/d3/calculus-deviations.json']
dispositions=[
 dict(finding_id='D2-OD6',status='repaired; author-checked, independent confirmation pending',files=files[:6],check='planning/d3/calculus-misread-check.py: eight parts, twelve independently worked misread cases, eleven edge expectations; seven targeted negatives fail.',detail='Consistent OD-6 authority and ledger. Removed stationary copy of implicit G1–G5. Fixed proof target remains unchanged. No repeat penalty; no earned A/B means no deduction.'),
 dict(finding_id='D2-S07',status='repaired; author-checked',files=files[:4]+[files[5]],check='Both classification branches and all eight parts have Apply3; current checks point to d3 receipts.',detail='Removed stale stationary Analyse4 statement and D1 current-receipt references.'),
 dict(finding_id='D2-S08',status='repaired; author-checked',files=[files[0],files[2],files[4]],check='S3 excludes back-substitution; S4 owns it. Failed back-substitution fixture gives3/4; seeded S3 regression fails.',detail='All valid paths are exclusive and retain a four-mark cap.'),
 dict(finding_id='calc-D2-04',status='clarified; author-checked',files=[files[0],files[2],files[4]],check='E-index expression at x=0 has canonical value in27/27 tuples; extended H1/H2 explicitly2/2, proof S2/S4 remain0; gradient-only G5 www remains0.'),
 dict(finding_id='calc-D2-05',status='clarified; author-checked',files=[files[0],files[2],files[4]],check='N1 explicitly equals−1/(their m); wrong reciprocal negative fails.'),
 dict(finding_id='calc-D2-06',status='clarified; author-checked',files=[files[1],files[3],files[4],files[5]],check='Native syllabus PDF14/printed11 reread. O03:D01 and O03:D03 listed only as conditional factor-theorem route prerequisites;128 quartic divisions recompute.'),
 dict(finding_id='calc-D2-07',status='clarified; author-checked',files=[files[0],files[4]],check='Actual path storage now explicitly covers product, root, divided and log-absolute alternatives; no fabricated product-rule evidence.'),
 dict(finding_id='calc-D2-08',status='clarified proposed allocation; confirmation pending',files=[files[0],files[2],files[4]],check='Invalid ln(y) on supplied negative branch maximum1/4 only with separately correct S3 evidence; seeded full-credit allocation fails.',deviation='CALC-D2-DEV09; D3 clarification')]
counts=dict(recipes=2,choices=4,parts=8,exemplars=12,whole_choice_bloom={'3':4},implicit={'point_tasks':27,'curves':23,'proof_identities':8,'strict_gradient':23,'strict_normal':8},stationary={'two_extrema_raw':540,'two_extrema_shapes':30,'flat_raw':256,'flat_shapes':16,'flat_outcomes':{'stationary inflexion':128,'minimum':64,'maximum':64}})
save(W/'checks/plan-repair-d3-calc-dispositions.json',dict(status='D3 author-side repair complete; Claude confirmation then Vitalis approval pending',scope='Implicit/stationary only; no owned domains or exemplar parameters changed.',counts_before=counts,counts_after=counts,dispositions=dispositions,deviations_path='planning/d3/calculus-deviations.json',negative_seeds_rejected=len(results),file_hashes={f:hashlib.sha256((W/f).read_bytes()).hexdigest()for f in files},limits=['The shared canonical calculus-design.json also contains root-owned motion; its final hash may change at root close-out.','Manual marking vectors are design expectations, not automatic marking tests.','No stage-E authoring, runtime grading, app or publication tested.']))
print(json.dumps(dict(status='pass',negative_seeds=len(results),deviations=len(rows),dispositions=len(dispositions)),indent=2))
