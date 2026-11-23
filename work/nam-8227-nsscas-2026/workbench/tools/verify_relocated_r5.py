"""Run the complete R5 double rebuild in a fresh repository layout on this host."""
import argparse,json,os,shutil,subprocess,sys,tempfile
from pathlib import Path
from analysis_sources import A,WB,ROOT,digest,write

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--keep-copy',action='store_true');args=parser.parse_args()
    temporary=Path(tempfile.mkdtemp(prefix='8227-r5-relocation-'))
    copy_root=temporary/'resources';copy_wb=copy_root/WB.relative_to(ROOT)
    shutil.copytree(WB.parent,copy_wb.parent,ignore=shutil.ignore_patterns('__pycache__','.DS_Store'))
    baseline=json.loads((A/'history/analysis-snapshot-r4.json').read_text())
    sources=dict(baseline['source_files'])
    # R5 legitimately acquired one scientific-context reference after R4.
    # Historical manifests alone cannot enumerate new source dependencies.
    for record in json.loads((A/'source-holdings.json').read_text())['records']:
        if record.get('sha256')and(ROOT/record['path']).is_file():
            assert record['path']not in sources or sources[record['path']]==record['sha256']
            sources[record['path']]=record['sha256']
    for relative,sha in sources.items():
        source=ROOT/relative;assert digest(source)==sha,('source changed',relative)
        target=copy_root/relative;target.parent.mkdir(parents=True,exist_ok=True)
        try:os.link(source,target)
        except OSError:shutil.copy2(source,target)
    print('Fresh workspace prepared; two full R5 rebuilds starting. Source files are immutable inputs.',flush=True)
    completed=subprocess.run([sys.executable,str(copy_wb/'tools/run_repair_checks.py')],cwd=copy_root,text=True,capture_output=True)
    (temporary/'rebuild.log').write_text(completed.stdout+'\n'+completed.stderr)
    assert completed.returncode==0,('fresh-copy rebuild failed',str(temporary/'rebuild.log'),completed.stdout[-1500:],completed.stderr[-2500:])
    check=json.loads((copy_wb/'checks/rebuild-verification.json').read_text())
    assert check['identical']and len(check['seeded_negative_results'])==38
    # The freshly rebuilt outputs must match the named author checkout too.
    # A missing or stale local output is a failure,not silently copied back.
    mismatches=[p for p,sha in check['output_hashes'].items()if not(ROOT/p).is_file()or digest(ROOT/p)!=sha]
    assert not mismatches,('fresh-copy differs from author outputs',mismatches)
    report=dict(status='pass',workspace_copy='independent temporary workspace in a fresh repository layout; no source-path edits',
        source_files_hash_checked=len(sources),workspace_files='independent copies;source PDFs hardlinked as immutable inputs or copied',
        double_rebuild=True,commands_per_run=len(check['first_rebuild']),outputs_compared=check['outputs_compared'],
        matches_author_checkout=True,seeded_negative_results=check['seeded_negative_results'],
        limits='Relocation on this macOS host with documented dependencies;not another operating system,independent educational review,app test or production acceptance.')
    write(WB/'checks/fresh-copy-verification-r5.json',report)
    write(WB/'analysis/history/rebuild-verification-r5-final-fresh-copy.json',check)
    print(json.dumps({k:v for k,v in report.items()if k not in ['seeded_negative_results']},indent=2),flush=True)
    if not args.keep_copy:shutil.rmtree(temporary)
if __name__=='__main__':main()
