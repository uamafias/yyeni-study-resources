"""Isolated, rerunnable propagation/negative checks for B.3--B.5 author prose."""
import copy
import hashlib
import json
from pathlib import Path
import apply_textbook_family_prose_parallel_r6 as p


def main():
    wb=Path(__file__).resolve().parents[1]
    document=json.loads((wb/'analysis/textbook-families.json').read_text())
    repaired=p.apply(copy.deepcopy(document),wb=wb)
    result=p.validate(repaired,wb=wb)
    negatives=[]
    def expect(name,fn):
        try:fn()
        except AssertionError as e:negatives.append(dict(fixture=name,result='rejected',reason=str(e)))
        else:raise AssertionError(('seeded prose corruption passed',name))
    for name,field,value in [
        ('missing-nearest-sibling','nearest_sibling_family_id',None),
        ('unpropagated-units','units_and_precision','generic units'),
        ('lost-ordered-progression','difficulty_progression','single item')]:
        bad=copy.deepcopy(repaired)
        f=next(f for f in bad['families']if len(f['members'])>1)
        f[field]=value
        expect(name,lambda bad=bad:p.validate(bad,wb=wb))
    bad=copy.deepcopy(repaired)
    bad['families'][0]['members'][0]['membership_reason']='Shared topic'
    expect('generic-membership-reason',lambda:p.validate(bad,wb=wb))
    baseline=p._read(wb)
    baseline['entries'][0]['members'][0]['membership_evidence_r6']['responses'][0]['derived_answer']='SEEDED WRONG MATHEMATICS'
    expect('answer-mathematics-change-during-hash-refresh',lambda:p._current_evidence(baseline,wb))
    result.update(negative_fixtures=negatives,
        distinct_units_and_precision=len({f['units_and_precision']for f in repaired['families']}),
        distinct_membership_reasons=len({m['membership_reason']for f in repaired['families']for m in f['members']}),
        source_input_hash_refreshes=sum(r.get('source_input_sha256')!=r.get('author_baseline_source_input_sha256')
            for f in repaired['families']for m in f['members']for r in m['membership_evidence_r6']['responses']),
        command='python3 work/nam-8227-nsscas-2026/workbench/tools/check_textbook_family_prose_parallel_r6.py',
        author_input_sha256=hashlib.sha256((wb/'tools'/p.INPUT_NAME).read_bytes()).hexdigest(),
        applier_sha256=hashlib.sha256(Path(p.__file__).read_bytes()).hexdigest())
    target=wb/'checks/r6/parallel-families/validation.json'
    target.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({k:v for k,v in result.items()if k not in ['negative_fixtures','limits']},indent=2))
    print(len(negatives),'seeded prose corruptions rejected')


if __name__=='__main__':main()
