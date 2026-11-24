"""Compare two concurrent independent full close-out rebuilds to the author.

Never refreshes author analysis to conceal stale outputs. Immutable source files
are linked as inputs only and hash checked in all three trees before and after.
All tools, including regenerated raw author data, must remain byte-identical.
"""
import argparse
import copy
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from analysis_sources import A,WB,ROOT,digest,write
import run_repair_r7_closeout as runner

PROOF=WB/'checks/r7-closeout/fresh-copy-proof.json'
MANIFEST=WB/'checks/r7-closeout/fresh-copy-input-manifest.json'
MISMATCH=WB/'checks/r7-closeout/fresh-copy-mismatches.json'
HISTORY=A/'history/rebuild-verification-r7-closeout-final-fresh-copy.json'
FIXTURE_SPECS=[
    ('r6_core','checks/r6/working-validation.json','negative_fixtures',12),
    ('legacy_protections','checks/r7/legacy-negative-protections.json','negative_fixtures',10),
    ('r7_family','checks/r7/family-negative-validation.json','negative_fixtures',4),
    ('r7_source','checks/r7/parallel-sources/validation.json','negative_fixtures',5),
    ('r7_new','checks/r7/final-validation.json','new_negative_fixtures',4),
    ('r7_closeout_new','checks/r7-closeout/final-validation.json','new_negative_fixtures',3),
]


def tool_hashes(root,wb):
    return {str(p.relative_to(root)):digest(p)for p in sorted((wb/'tools').rglob('*'))
            if p.is_file() and '__pycache__'not in p.parts and p.name!='.DS_Store'}


def verify_sources(root,sources):
    actual={p:digest(root/p)for p in sources}
    assert actual==sources,('protected source files changed',str(root),[p for p in sources if actual[p]!=sources[p]])
    return actual


def verify_tools(root,wb,expected):
    actual=tool_hashes(root,wb)
    changed=[p for p in sorted(set(expected)|set(actual)) if expected.get(p)!=actual.get(p)]
    assert not changed,('author tools changed during fresh-copy proof',str(root),changed)
    return actual


def copied_projection(root,wb):
    result=subprocess.run([sys.executable,str(wb/'tools/run_repair_r7_closeout.py'),'--print-hashes'],cwd=root,capture_output=True,text=True)
    assert result.returncode==0,('fresh-copy projection failed',str(root),result.stderr[-4000:])
    return json.loads(result.stdout)


def fixture_records(wb,negative):
    old=negative['previous_seeded_negative_results'];assert len(old)==38
    assert all(r['exit_code']!=0 and r['unchanged_output_hashes']is True for r in old)
    counts={'established_subprocess':38};records={'established_subprocess':copy.deepcopy(old)}
    for name,path,key,count in FIXTURE_SPECS:
        doc=json.loads((wb/path).read_text());rows=doc[key]
        assert isinstance(rows,(list,dict))and len(rows)==count,('retained fixture count changed',name,len(rows),count)
        values=list(rows.values())if isinstance(rows,dict)else rows
        for row in values:
            assert isinstance(row,dict)and row.get('result')in ['rejected','failed as required'],('fixture lacks explicit failure proof',name,row)
        counts[name]=count;records[name]=rows
    assert sum(counts.values())==76
    return counts,records


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--keep-copies',action='store_true');args=parser.parse_args()
    baseline=json.loads((WB/'checks/repair-r7-baseline.json').read_text());sources=baseline['source_files']
    verify_sources(ROOT,sources)
    before_tools=tool_hashes(ROOT,WB);author_before=runner.hashes()
    folder=Path(tempfile.mkdtemp(prefix='8227-r7-closeout-fresh-proof-'));runs=[]
    try:
        for n in [1,2]:
            root=folder/f'copy-{n}';wb=root/WB.relative_to(ROOT)
            shutil.copytree(WB.parent,wb.parent,ignore=shutil.ignore_patterns('__pycache__','.DS_Store'))
            for relative in sources:
                target=root/relative;target.parent.mkdir(parents=True,exist_ok=True)
                if target.exists():
                    assert digest(target)==sources[relative],('copied source differs',relative)
                    continue
                try:os.link(ROOT/relative,target)
                except OSError:shutil.copy2(ROOT/relative,target)
            verify_sources(root,sources);copied_tools=verify_tools(root,wb,before_tools)
            log=(folder/f'copy-{n}.log').open('w')
            proc=subprocess.Popen([sys.executable,str(wb/'tools/run_repair_r7_closeout.py'),'--single-rebuild'],cwd=root,stdout=log,stderr=subprocess.STDOUT,text=True)
            runs.append(dict(root=root,wb=wb,log=log,proc=proc,tools_before=copied_tools))
            print(f'Fresh close-out copy {n}: PID {proc.pid}; log {log.name}',flush=True)
        checks=[]
        for run in runs:
            code=run['proc'].wait();run['log'].close()
            assert code==0,('fresh close-out build failed',run['log'].name,Path(run['log'].name).read_text()[-7000:])
            checks.append(json.loads((run['wb']/'checks/r7-closeout/single-rebuild-r7-closeout.json').read_text()))
            run['tools_after_build']=verify_tools(run['root'],run['wb'],before_tools)
            verify_sources(run['root'],sources)
        first,second=[c['output_hashes']for c in checks]
        changed=[p for p in sorted(set(first)|set(second))if first.get(p)!=second.get(p)]
        assert not changed,('independent close-out copies differed',str(folder),changed)
        # Detect concurrent output changes as well as stale author outputs. This
        # helper must never repair either condition by copying generated files.
        author_after=runner.hashes()
        changed_author=[p for p in sorted(set(author_before)|set(author_after))if author_before.get(p)!=author_after.get(p)]
        assert not changed_author,('author outputs changed during proof; retry from a stable author build',changed_author)
        mismatches=[p for p in sorted(set(first)|set(author_after))if first.get(p)!=author_after.get(p)]
        if mismatches:
            write(MISMATCH,dict(status='FAILED: fresh copies agree, but author outputs are stale or incomplete; author outputs were not refreshed.',folder=str(folder),paths=mismatches,fresh_hashes={p:first.get(p)for p in mismatches},author_hashes={p:author_after.get(p)for p in mismatches}))
        assert not mismatches,('fresh close-out outputs differ from author checkout; rebuild author outputs explicitly before rerunning',str(folder),mismatches)
        run=runs[0];log=folder/'negative-fixtures.log'
        with log.open('w')as out:
            result=subprocess.run([sys.executable,str(run['wb']/'tools/run_repair_r7_closeout.py'),'--negative-only'],cwd=run['root'],stdout=out,stderr=subprocess.STDOUT,text=True)
        assert result.returncode==0,('fresh close-out negatives failed',str(log),log.read_text()[-7000:])
        negative=json.loads((run['wb']/'checks/r7-closeout/negative-only-r7-closeout.json').read_text())
        counts,records=fixture_records(run['wb'],negative)
        # Checker replay must not change any projected analysis or checks.
        replay=copied_projection(run['root'],run['wb'])
        changed_replay=[p for p in sorted(set(first)|set(replay))if first.get(p)!=replay.get(p)]
        assert not changed_replay,('negative checker replay changed output projection',changed_replay)
        tools_after={}
        for n,current in enumerate(runs,1):
            tools_after[f'copy_{n}']=verify_tools(current['root'],current['wb'],before_tools)
            verify_sources(current['root'],sources)
        tools_after['author']=verify_tools(ROOT,WB,before_tools);verify_sources(ROOT,sources)
        assert runner.hashes()==author_before,'author output projection changed during negative fixtures'
        saved=dict(first_rebuild=checks[0]['commands'],second_rebuild=checks[1]['commands'],identical=True,output_hashes=first,outputs_compared=len(first),previous_seeded_negative_results=negative['previous_seeded_negative_results'],negative_fixture_counts=counts,negative_fixture_records=records,execution='Two complete independent fresh-copy builds run concurrently, with no shared generated outputs. Source PDFs linked as immutable inputs and hash verified in all copies before and after.')
        write(HISTORY,saved)
        write(MANIFEST,dict(status='pass',identical_across_author_and_two_fresh_copies_before_and_after=True,tools_sha256_before=before_tools,tools_sha256_after=tools_after,source_files_sha256=sources))
        proof=dict(status='Two fresh-copy full close-out rebuilds passed, outputs byte-identical and matched the unchanged author checkout; all retained and close-out negatives rejected.',source_files_hash_checked=len(sources),author_tool_files_hash_checked=len(before_tools),commands_per_run=len(checks[0]['commands']),outputs_compared=len(first),double_rebuild=True,matches_author_checkout=True,negative_fixture_counts=counts,total_seeded_errors_rejected=sum(counts.values()),fixture_records=[p for _,p,_,_ in FIXTURE_SPECS],tool_manifest_path=str(MANIFEST.relative_to(WB)),history_path=str(HISTORY.relative_to(WB)),limitations='Author reproducibility and structural checks on this host; independent educational acceptance, application testing and production readiness remain separate.')
        # Only proof records are transferred. Generated analysis is never copied
        # back to make a stale author checkout appear to agree.
        write(WB/'checks/r7-closeout/negative-only-r7-closeout.json',negative)
        write(PROOF,proof);print(json.dumps(proof,indent=2),flush=True)
    except BaseException:
        for run in runs:
            if run['proc'].poll()is None:run['proc'].terminate()
            if not run['log'].closed:run['log'].close()
        print('Failed proof copies and logs retained: '+str(folder),flush=True)
        raise
    else:
        if args.keep_copies:print('Copies retained: '+str(folder),flush=True)
        else:shutil.rmtree(folder)


if __name__=='__main__':main()
