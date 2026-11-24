"""D4 design-only double derivation and negative fixtures; no runtime generation."""
import json,hashlib,subprocess,sys
from pathlib import Path
P=Path(__file__).resolve().parents[1];W=P.parent;ROOT=W.parents[2];H=P/'d4'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
commands=[('visual-domain-checks.py',[]),('visual-exemplar-oracle.py',[]),('visual-rule-fixtures.py',[]),('visual-d4-independent-checks.py',[]),('calculus-design-check.py',[]),('calculus-misread-check.py',[]),('trig-d4-check.py',[]),('motion-design-check.py',[]),('motion-marking-check.py',[]),('misread-policy-check.py',[]),('render-motion-exemplars.py',[]),('build-design-records.py',[]),('build-given-representation-register.py',[]),('coverage-check.py',['--write']),('coverage-check.py',['--check']),('build-checkpoint.py',[]),('check-design-integration.py',[]),('check-markdown-math.mjs',[])]
generated=[H/n for n in ['visual-domain-checks.json','visual-rounding-fixtures.json','visual-exemplar-oracle.json','visual-rule-fixtures.json','visual-d4-independent-checks.json','calculus-domain-audit.json','calculus-exemplar-oracle.json','calculus-misread-oracle.json','trig-d4-fixtures.json','motion-design-check.json','motion-separation.json','motion-marking-check.json','misread-policy-check.json','choice-capacities.json','given-representation-register.json','given-representation-register.md','coverage-check.json','deviation-register.json']]
generated +=[P/n for n in ['pilot-design.json','part-evidence-register.json','part-evidence-register.md','coverage-plan.json','coverage-plan.md','OWNER-CHECKPOINT.md']]
generated +=[W/n for n in ['exemplars/WB8227-motion-integration.md','checks/plan-repair-d4-trig-validation.json','checks/plan-repair-d4-part-register-audit.json','checks/plan-repair-d4-math-syntax.json']]
def output_hashes():return {str(p.relative_to(W)):sha(p)for p in generated}
rounds=[]
for n in [1,2]:
 for name,args in commands:
  result=subprocess.run(['node'if name.endswith('.mjs')else sys.executable,str(H/name),*args],cwd=ROOT,text=True,capture_output=True)
  assert result.returncode==0,(name,result.stdout[-2000:],result.stderr[-4000:])
 now=output_hashes();rounds.append(dict(round=n,commands=len(commands),result='pass'))
 if n==1:before=now
 else:assert before==now,('D4 derived outputs differ',[(k,before.get(k),now.get(k))for k in before if before.get(k)!=now.get(k)])
negative=[]
for file in ['calculus-negative-fixtures.json','visual-negative-fixtures.json']:
 for row in json.loads((H/file).read_text())['results']:
  seed=row.get('negative_fixture',row.get('seed'));name=row['script'];r=subprocess.run([sys.executable,str(H/name),'--negative-fixture',seed],cwd=ROOT,text=True,capture_output=True)
  assert r.returncode!=0,('negative fixture admitted',name,seed)
  negative.append(dict(script=name,seed=seed,result='rejected',exit_code=r.returncode))
for seed in ['vertex-only-R1','dependency-cascade']:
 r=subprocess.run([sys.executable,str(H/'motion-marking-check.py'),'--negative-fixture',seed],cwd=ROOT,text=True,capture_output=True);assert r.returncode!=0,seed;negative.append(dict(script='motion-marking-check.py',seed=seed,result='rejected',exit_code=r.returncode))
assert output_hashes()==before,'a seeded failure changed a live derived record'
proof=dict(status='pass',scope='D4 design-only double derivation in author checkout, not an analysis rebuild or two fresh-copy execution',rounds=rounds,byte_identical_derived_outputs=len(before),outputs=before,seeded_subprocess_rejections=len(negative),negative_fixtures=negative,inline_motion_domain_rejections=5,inline_ledger_rejections=4,analysis_inputs_changed=False,limits='Fixed-fixture gross evidence and ledger tests do not implement a learner-response marker. Existing accepted R7 analysis proof and D3 independent two-copy proof remain preserved by immutable hashes, not rerun as D4 evidence.')
(H/'design-rebuild-proof.json').write_text(json.dumps(proof,indent=2)+'\n');print(json.dumps({k:v for k,v in proof.items()if k in ['status','rounds','byte_identical_derived_outputs','seeded_subprocess_rejections','inline_motion_domain_rejections','inline_ledger_rejections']},indent=2))
