"""Portable R7 author rebuild/negative runner; safe to invoke from another cwd.

The caller may run this script in a separate repository copy. All paths resolve
from analysis_sources, never the original author's workstation path. Two rebuilds
in that copy certify determinism only; external copy comparisons and independent
educational acceptance remain separate proofs. No publication is performed.

The old R6 --final wrappers assert a frozen 500-family prose projection and old
figure taxonomy. R7 intentionally changes named families and figure records, so
those wrappers are replaced by R7 checks, while their ten negative protections
are retained here on the appropriate baseline/current in-memory records.
"""
import argparse
import copy
import gzip
import json
import subprocess
import sys
from pathlib import Path
import run_repair_checks as previous
from analysis_sources import A,ROOT,WB,digest,write

BASE_HASHES=previous.hashes

PROOF_NAMES={'rebuild-verification-r7.json','single-rebuild-r7.json','negative-only-r7.json','fresh-copy-proof.json','fresh-copy-input-manifest.json','fresh-copy-mismatches.json'}
CHECKERS=['check_textbook_answer_pages_r6.py','verify_r6_preservation.py',
          'check_repair_r6.py','check_textbook_source_repairs_r7.py',
          '@family-r7','@legacy-protections','check_repair_r7.py']


def steps():
    result=list(previous.STEPS)
    # previous.STEPS ends with synthesis check, population audit, inventory
    # finalizer and final population audit. The map must hash that final state.
    result.extend(['build_textbook_exam_candidates_r6.py',
                   'build_textbook_answer_page_audit_r7.py',
                   'apply_textbook_figures_r6.py',
                   'build_objective_problem_map_r6.py',*CHECKERS])
    return result


def hashes():
    result=BASE_HASHES()
    paths=[WB/'checks/r6/working-validation.json',WB/'checks/r6/preservation-verification.json',
           * (WB/'checks/r7').rglob('*.json'),* (WB/'checks/r7').rglob('*.md')]
    for path in sorted(paths):
        if path.is_file() and path.name not in PROOF_NAMES and 'rebuild-drift' not in path.parts:
            result[str(path.relative_to(ROOT))]=digest(path)
    return dict(sorted(result.items()))


def legacy_protections():
    """Preserve five R6 prose + five figure rejections without old final gates."""
    import apply_textbook_family_prose_parallel_r6 as prose
    import apply_textbook_figures_r6 as figures
    baseline=WB/'checks/r7/parallel-families/assembled-r6-baseline.json.gz'
    document=json.loads(gzip.decompress(baseline.read_bytes()))
    repaired=prose.apply(copy.deepcopy(document),wb=WB)
    prose.validate(repaired,wb=WB)
    rejected=[]
    def reject(name,fn):
        try:fn()
        except AssertionError as exc:
            rejected.append({'fixture':name,'result':'rejected','reason':str(exc)})
        else:raise AssertionError(('legacy protection unexpectedly passed',name))
    for name,field,value in [('missing-nearest-sibling','nearest_sibling_family_id',None),
                             ('unpropagated-units','units_and_precision','generic units'),
                             ('lost-ordered-progression','difficulty_progression','single item')]:
        bad=copy.deepcopy(repaired);f=next(f for f in bad['families']if len(f['members'])>1);f[field]=value
        reject(name,lambda bad=bad:prose.validate(bad,wb=WB))
    bad=copy.deepcopy(repaired);bad['families'][0]['members'][0]['membership_reason']='Shared topic'
    reject('generic-membership-reason',lambda:prose.validate(bad,wb=WB))
    authored=prose._read(WB)
    authored['entries'][0]['members'][0]['membership_evidence_r6']['responses'][0]['derived_answer']='SEEDED WRONG MATHEMATICS'
    reject('answer-mathematics-change-during-hash-refresh',lambda:prose._current_evidence(authored,WB))
    items=json.loads((A/'textbook-inventory.json').read_text())['items']
    # Validate current R7 records directly: reapplying an old taxonomy would
    # overwrite the very R7 corrections that this round must preserve.
    figures.validate(items,figures.comparison_index(items))
    mutations=[('pending-figure-status',lambda i:i['exam_representation_check'].update(status='comparison pending')),
               ('unclassified-figure',lambda i:i.update(figure_record_type='unclassified')),
               ('content-certification-from-parent',lambda i:i.update(content_check='verified by parent answer')),
               ('invented-exam-part',lambda i:i['exam_representation_check'].update(examination_part_ids=['8227:EXAM:9999:P1:Q1:a'])),
               ('textbook-image-learner-display',lambda i:i.update(learner_display=True))]
    for name,mutate in mutations:
        bad=copy.deepcopy(items);mutate(figures._figures(bad)[0])
        reject(name,lambda bad=bad:figures.validate(bad))
    report={'status':'pass','prose_basis':'Frozen assembled R6 baseline with guarded current author evidence; not a claim that R7 keeps the old 500-family final projection.',
            'figure_basis':'Current R7 canonical records; old taxonomy is not reapplied.',
            'negative_fixtures':rejected,'limits':'Structural rejection protections, not independent content acceptance.'}
    write(WB/'checks/r7/legacy-negative-protections.json',report)
    print(json.dumps({'legacy_negative_protections_rejected':len(rejected)},indent=2))


def command(name,counter):
    if name=='@family-r7':
        script=WB/'checks/r7/parallel-families/verify_family_repairs.py';extra=[]
    elif name=='@legacy-protections':
        script=Path(__file__).resolve();extra=['--legacy-protections']
    else:
        script=WB/'tools'/name;extra=['--write-comparisons'] if name=='apply_textbook_figures_r6.py' else []
    process=subprocess.run([sys.executable,str(script),*extra],cwd=ROOT,capture_output=True,text=True)
    if process.returncode:
        raise RuntimeError(f'{name} failed:\n{process.stdout}\n{process.stderr}')
    if name=='@family-r7':
        write(WB/'checks/r7/family-negative-validation.json',json.loads(process.stdout))
    counter[0]+=1
    if counter[0]==1 or counter[0]%20==0 or name=='check_repair_r7.py':
        print(f'Completed command {counter[0]}: {name}',flush=True)
    return {'command':[sys.executable,str(script.relative_to(ROOT)),*extra],'exit_code':process.returncode}


def run_steps(names,counter):
    rows=[command(name,counter)for name in names]
    if names!=CHECKERS:
        for stage in ['part1','textbook-working']:
            script=WB/'tools/check_repair_r5.py'
            p=subprocess.run([sys.executable,str(script),'--stage',stage],cwd=ROOT,capture_output=True,text=True)
            if p.returncode:raise RuntimeError(f'check_repair_r5.py {stage} failed:\n{p.stdout}\n{p.stderr}')
            counter[0]+=1
            if counter[0]%20==0:print(f'Completed command {counter[0]}: check_repair_r5.py {stage}',flush=True)
            rows.append({'command':[sys.executable,str(script.relative_to(ROOT)),'--stage',stage],'exit_code':p.returncode})
    return rows


def previous_negatives():
    # The established runner asserts unchanged hashes after every one of its 38
    # failing subprocess fixtures. Use this round's complete hash projection.
    original=previous.hashes
    previous.hashes=hashes
    try:return previous.run_negative_fixtures(hashes())
    finally:previous.hashes=original


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--single-rebuild',action='store_true',help='One author rebuild; never reports double-rebuild determinism.')
    parser.add_argument('--negative-only',action='store_true',help='Check the current canonical outputs and run retained/new fixture suites without rebuilding source producers.')
    parser.add_argument('--legacy-protections',action='store_true',help=argparse.SUPPRESS)
    args=parser.parse_args()
    if args.legacy_protections:legacy_protections();return
    assert not(args.single_rebuild and args.negative_only),'choose single-rebuild or negative-only'
    counter=[0]
    if args.negative_only:
        commands=run_steps(CHECKERS,counter);negative=previous_negatives()
        write(WB/'checks/r7/negative-only-r7.json',{'status':'current canonical checker and negative suites passed; no rebuild performed',
             'commands':commands,'previous_seeded_negative_results':negative,'previous_seeded_negative_count':len(negative),
             'limits':'No fresh-copy or deterministic rebuild proof; no independent content acceptance.'})
        print(f'Current canonical checkers passed; {len(negative)} established subprocess fixtures rejected.',flush=True);return
    first=run_steps(steps(),counter);before=hashes()
    if args.single_rebuild:
        write(WB/'checks/r7/single-rebuild-r7.json',{'status':'one author rebuild passed; not double-rebuild proof',
              'commands':first,'output_hashes':before,'outputs_compared':len(before),
              'limits':'No independent educational, runtime or production acceptance.'})
        print(json.dumps({'single_rebuild':'pass','commands':len(first),'outputs':len(before)},indent=2));return
    first_bytes={p:(ROOT/p).read_bytes()for p in before if Path(p).suffix in ['.json','.md']}
    second=run_steps(steps(),counter);after=hashes()
    changed=[p for p in sorted(set(before)|set(after))if before.get(p)!=after.get(p)]
    if changed:
        folder=WB/'checks/r7/rebuild-drift';folder.mkdir(parents=True,exist_ok=True)
        for index,path in enumerate(changed):
            if path in first_bytes:
                (folder/f'{index:03d}-first-{Path(path).name}').write_bytes(first_bytes[path])
                if (ROOT/path).exists():(folder/f'{index:03d}-second-{Path(path).name}').write_bytes((ROOT/path).read_bytes())
        write(folder/'manifest.json',{'changed_paths':changed,'first_hashes':{p:before.get(p)for p in changed},
                                     'second_hashes':{p:after.get(p)for p in changed},'status':'failed determinism; diagnostic copies are not proof of completion'})
    assert not changed,('nondeterministic R7 outputs',changed)
    negative=previous_negatives()
    write(WB/'checks/r7/rebuild-verification-r7.json',{'first_rebuild':first,'second_rebuild':second,'outputs_compared':len(after),
          'identical':True,'changed_paths':[],'output_hashes':after,'previous_seeded_negative_results':negative,
          'previous_seeded_negative_count':len(negative),
          'limits':'Two deterministic author rebuilds in this checkout. External fresh-copy comparison, independent educational review and production acceptance remain separate.'})
    print(json.dumps({'rebuilds':'two passed','outputs_byte_identical':len(after),'established_subprocess_negatives_rejected':len(negative)},indent=2))


if __name__=='__main__':main()
