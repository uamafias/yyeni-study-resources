"""Deterministic D3 design-only double derivation and regression fixtures.

Never invokes the analysis pipeline or runtime recipe generation. Historical
checks are retained; analysis immutability is separately verified by freeze-plan.
"""
import json,hashlib,subprocess,sys
from pathlib import Path
P=Path(__file__).resolve().parents[1];W=P.parent;ROOT=W.parents[2];H=P/'d3'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def run(name,*args,node=False,negative=False):
 command=['node'if node else sys.executable,str(H/name),*args]
 r=subprocess.run(command,cwd=ROOT,text=True,capture_output=True)
 if negative:assert r.returncode!=0,(name,args,'seed accepted')
 else:assert r.returncode==0,(name,r.stdout[-2000:],r.stderr[-4000:])
 return dict(script=name,args=list(args),exit_code=r.returncode,status='rejected' if negative else 'pass')
commands=[('visual-domain-checks.py',[]),('visual-exemplar-oracle.py',[]),('visual-rule-fixtures.py',[]),('visual-d3-independent-checks.py',[]),('calculus-design-check.py',[]),('calculus-misread-check.py',[]),('trig-d3-check.py',[]),('motion-design-check.py',[]),('misread-policy-check.py',[]),('render-motion-exemplars.py',[]),('build-design-records.py',[]),('coverage-check.py',['--write']),('coverage-check.py',['--check']),('build-checkpoint.py',[]),('check-design-integration.py',[]),('check-markdown-math.mjs',[])]
def outputs():
 paths=list(H.glob('*.json'))+list((W/'checks').glob('plan-repair-d3-*.json'))
 paths +=[P/n for n in ['pilot-design.json','part-evidence-register.json','part-evidence-register.md','coverage-plan.json','coverage-plan.md','OWNER-CHECKPOINT.md']]+[W/'exemplars/WB8227-motion-integration.md']
 return {str(p.relative_to(W)):sha(p)for p in paths if p.name not in ['design-rebuild-proof.json','plan-repair-d3-preservation.json']}
rounds=[]
for n in [1,2]:
 steps=[]
 for name,args in commands:
  r=run(name,*args,node=name.endswith('.mjs'));steps.append(r)
 current=outputs();rounds.append(dict(round=n,commands=len(steps),status='pass'))
 if n==1:first=current
 else:assert current==first,('D3 design outputs differ',[(k,first.get(k),current.get(k))for k in set(first)|set(current)if first.get(k)!=current.get(k)])
negative=[]
for row in json.loads((H/'calculus-negative-fixtures.json').read_text())['results']:
 name,seed=row['script'],row['negative_fixture'];r=subprocess.run([sys.executable,str(H/name),'--negative-fixture',seed],cwd=ROOT,text=True,capture_output=True);assert r.returncode!=0,(name,seed,'accepted');negative.append(dict(script=name,seed=seed,status='rejected',exit_code=r.returncode))
for seed in ['modulus-parabola','vector-wrong-resultant','trapezium-original','trapezium-original-part','trapezium-original-sketch','trapezium-precision-collision']:
 r=subprocess.run([sys.executable,str(H/'visual-domain-checks.py'),'--negative-fixture',seed],cwd=ROOT,text=True,capture_output=True);assert r.returncode!=0,seed;negative.append(dict(script='visual-domain-checks.py',seed=seed,status='rejected',exit_code=r.returncode))
assert outputs()==first,'negative fixture modified a live design output'
report=dict(status='pass',scope='D3 design-only double derivation in author checkout; not an analysis rebuild or fresh-copy runtime proof',rounds=rounds,byte_identical_outputs=len(first),outputs=first,seeded_subprocess_rejections=len(negative),negative_fixtures=negative,inline_motion_domain_rejections=5,analysis_inputs_changed=False,limits='Existing accepted R7 three-location/76-negative analysis proof remains preserved by unchanged hashes, not re-executed here. Same-vendor independent audits and cross-vendor/owner acceptance are distinct.')
(H/'design-rebuild-proof.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(dict(status='pass',rounds=2,commands_per_round=len(commands),byte_identical_outputs=len(first),seeded_subprocess_rejections=len(negative),inline_motion_domain_rejections=5),indent=2))
