"""D4 -> D4.1 text-only invariant guard against the immutable D4 archive.

This compares data, not pedagogical quality or learner-response recognition.
It never edits authored designs, fixtures, archives or existing builders.
"""
import argparse,copy,hashlib,json,re
from pathlib import Path

HERE=Path(__file__).resolve().parent
P=HERE.parent;W=P.parent;ROOT=W.parents[2]
ARCHIVE=P/'history/d4-candidate'
EXPECTED='71ee10b6388064079137412da8834623b63e7179af7e0b8a280a345f13f1e4bb'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:json.loads(p.read_text())

CANONICAL=['planning/visual-design.json','planning/calculus-design.json','planning/trig-model-design.json']
DERIVED=['planning/pilot-design.json','planning/part-evidence-register.json']
FIXTURES=[
 'planning/d4/calculus-case-inputs.json',
 'planning/d4/calculus-exemplar-oracle.json',
 'planning/d4/calculus-misread-oracle.json',
 'planning/d4/trig-d4-fixtures.json',
 'planning/d4/visual-exemplar-oracle.json',
 'planning/d4/visual-rule-fixtures.json',
 'planning/d4/visual-d4-independent-checks.json',
 'planning/d4/misread-policy-check.json',
 'planning/d4/motion-cases.json',
 'planning/d4/motion-marking-check.json',
 'planning/d4/visual-domain-checks.json',
 'planning/d4/visual-rounding-fixtures.json',
 'planning/d4/calculus-domain-audit.json',
 'planning/d4/motion-design-check.json',
 'planning/d4/motion-separation.json',
 'planning/d4/choice-capacities.json',
 'checks/plan-repair-d4-trig-validation.json',
 'planning/visual-design-asset-checks.json',
]

def archived(relative):return ARCHIVE/(W/relative).relative_to(ROOT)
def snapshot(relative):return read(archived(relative)),read(W/relative)
def hash_map(x):return isinstance(x,dict)and all(isinstance(v,str)and re.fullmatch(r'[0-9a-f]{64}',v)for v in x.values())

def allowed(a,b,path,kind):
    """Permit only the prompt's textual leaves and declared provenance changes."""
    key=path.rsplit('/',1)[-1]
    if kind in ['canonical','derived']:
        if path.endswith('/misread_policy/operational_rules')and isinstance(a,str)and isinstance(b,str):return 'D4-S02 propagated operational clarification'
        if path.endswith('/misread_policy/eligibility_notes')and isinstance(a,str)and isinstance(b,str):return 'listed branch-specific eligibility prose'
        named_status=(key in ['bloom_status','classification_status'] or re.search(r'/same_type_checks/\d+/status$',path))
        if named_status and isinstance(a,str)and isinstance(b,str):
            assert ('pending'in b.lower()or'propos'in b.lower()),('status stopped being pending/proposed',path,b)
            return 'named stale round/gate status text'
        if key in ['check_path','precision_fixture_path']and isinstance(a,str)and isinstance(b,str):
            assert b==a.replace('planning/d3/','planning/d4/'),('unexpected receipt-path rewrite',path,a,b)
            return 'named current D4 receipt path'
        if kind=='derived':
            if key in ['origin_design_input_sha256','part_evidence_register_sha256']and isinstance(a,str)and isinstance(b,str)and re.fullmatch(r'[0-9a-f]{64}',b):return 'derived input content hash'
            if key=='inputs'and hash_map(a)and hash_map(b)and set(a)==set(b):return 'derived input hash map'
    if kind=='fixture':
        if key in ['inputs','input_sha256','input_hashes','file_hashes']and hash_map(a)and hash_map(b)and set(a)==set(b):return 'fixture input hash map'
        if key=='status'and isinstance(a,str)and isinstance(b,str):
            norm=lambda v:v.replace('D4.1','D4').replace('D3','D4')
            if a.startswith('pass')and b.startswith('pass')and norm(a)==norm(b):return 'listed D3/D4 validation status stamp'
        if key=='render_path'and isinstance(a,str)and isinstance(b,str):
            assert Path(a).is_absolute()and not Path(b).is_absolute()and '..'not in Path(b).parts
            assert a.endswith('/'+b)and(ROOT/b).is_file(),('render identity changed',a,b)
            return 'D4-N01 same render identity, repo-relative path'
    return None

def compare(a,b,kind,path='',changes=None):
    if changes is None:changes=[]
    if type(a)==type(b)and a==b:return changes
    reason=allowed(a,b,path,kind)
    if reason:
        changes.append(dict(path=path,reason=reason,before=a,after=b));return changes
    assert type(a)==type(b),('data type changed',path,type(a).__name__,type(b).__name__)
    if isinstance(a,dict):
        assert set(a)==set(b),('JSON key set changed',path,sorted(set(a)^set(b)))
        for k in a:compare(a[k],b[k],kind,path+'/'+k,changes)
    elif isinstance(a,list):
        assert len(a)==len(b),('list length changed',path,len(a),len(b))
        for i,(x,y)in enumerate(zip(a,b)):compare(x,y,kind,path+'/'+str(i),changes)
    else:raise AssertionError(('non-textual or unlisted value changed',path,a,b))
    return changes

def count_ledgers(x):
    if isinstance(x,dict):return int('gross_awards'in x and'net_awards'in x)+sum(count_ledgers(v)for v in x.values())
    if isinstance(x,list):return sum(count_ledgers(v)for v in x)
    return 0

def locate(x,wanted,path=()):
    if isinstance(x,dict):
        for k,v in x.items():
            if k==wanted:return path+(k,)
            p=locate(v,wanted,path+(k,))
            if p:return p
    elif isinstance(x,list):
        for i,v in enumerate(x):
            p=locate(v,wanted,path+(i,))
            if p:return p
    return None
def replace_path(x,path,value):
    for k in path[:-1]:x=x[k]
    x[path[-1]]=value
def value_at(x,path):
    for k in path:x=x[k]
    return x

def build():
    assert sha(P/'history/plan-manifest-d4.json')==EXPECTED,'wrong D4 archive manifest'
    results=[];all_changes=[];semantic_ledgers=0
    for kind,files in [('canonical',CANONICAL),('derived',DERIVED),('fixture',FIXTURES)]:
        for rel in files:
            a,b=snapshot(rel);changes=compare(a,b,kind)
            semantic_ledgers+=count_ledgers(a)if kind=='fixture'else 0
            results.append(dict(path=rel,kind=kind,status='unchanged except listed text/provenance',baseline_sha256=sha(archived(rel)),current_sha256=sha(W/rel),permitted_changed_leaves=len(changes),fixed_evidence_ledgers=count_ledgers(a)if kind=='fixture'else None))
            all_changes.extend(dict(file=rel,**c)for c in changes)
    cases=[]
    for rel,key in [('planning/d4/calculus-exemplar-oracle.json','checks'),('planning/d4/motion-cases.json',None),('planning/d4/visual-exemplar-oracle.json','cases'),('checks/plan-repair-d4-trig-validation.json','exemplar_checks')]:
        a,b=snapshot(rel);items=a if key is None else a[key]
        for item in items:
            case=item['case_id']
            if not case.startswith('WB8227-'):case=item['recipe_id']+':'+item['branch_id']+':'+case
            cases.append(case)
    assert len(cases)==len(set(cases))==42,('canonical example partition failed',len(cases),len(set(cases)))
    negative=[]
    def reject(name,original,mutated,kind):
        try:compare(original,mutated,kind)
        except AssertionError as exc:negative.append(dict(seed=name,status='rejected',diagnostic=str(exc)[:300]))
        else:raise AssertionError('seeded semantic change passed: '+name)
    original,_=snapshot('planning/calculus-design.json')
    marks=locate(original,'marks');mutated=copy.deepcopy(original);replace_path(mutated,marks,value_at(original,marks)+1);reject('criterion-tariff-change',original,mutated,'canonical')
    answer=locate(original,'expected_answers');mutated=copy.deepcopy(original);oldanswer=value_at(mutated,answer);first=next(iter(oldanswer));oldanswer[first]='seeded wrong answer';reject('canonical-answer-change',original,mutated,'canonical')
    tuples=locate(original,'accepted_tuple_keys');assert tuples;mutated=copy.deepcopy(original);arr=value_at(mutated,tuples);arr.reverse();reject('domain-tuple-order-change',original,mutated,'canonical')
    original,_=snapshot('planning/d4/misread-policy-check.json')
    total=locate(original,'net_total');mutated=copy.deepcopy(original);replace_path(mutated,total,value_at(original,total)+1);reject('fixture-net-score-change',original,mutated,'fixture')
    tags=locate(original,'datum_id');mutated=copy.deepcopy(original);replace_path(mutated,tags,'different-datum');reject('fixture-datum-tag-change',original,mutated,'fixture')
    return dict(status='pass',scope='D4 to D4.1 text-only invariants against immutable D4 candidate; not independent content acceptance or runtime validation',baseline_manifest_sha256=EXPECTED,canonical_design_files=3,derived_design_files=2,fixed_fixture_and_domain_files=len(FIXTURES),canonical_examples_checked=42,canonical_case_ids=cases,fixed_evidence_ledgers_compared=semantic_ledgers,ledger_count_limit='Raw ledger records across receipts; overlaps between reports are not claimed as unique submissions.',files=results,permitted_text_or_provenance_changes=all_changes,semantic_seeds_rejected=len(negative),negative_fixtures=negative,unchanged_invariants=['all counts and list ordering','recipe/selection/branch/part/criterion IDs','versions and Bloom/classification values','marks, tariffs and criterion types','domains, admitted/excluded tuples and parameter values','canonical answers and exact/rounded fixture values','gross and net awards, deduction slots, datum tags, tariffs and ledger ordering'],allowlist='Only misread_policy operational_rules/eligibility_notes strings; named bloom/classification/same-type status labels; named D3-to-D4 receipt paths; derived hash maps; listed D3-to-D4 validation stamp; same-render absolute-to-repo-relative path. All other leaves exact.')

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');args=ap.parse_args();doc=build();text=json.dumps(doc,indent=2,ensure_ascii=False)+'\n';dest=HERE/'no-score-change-check.json'
    if args.check:assert dest.read_text()==text,'invariant receipt is stale'
    else:dest.write_text(text)
    print(json.dumps({k:doc[k]for k in ['status','canonical_design_files','derived_design_files','fixed_fixture_and_domain_files','canonical_examples_checked','fixed_evidence_ledgers_compared','semantic_seeds_rejected']},indent=2))
