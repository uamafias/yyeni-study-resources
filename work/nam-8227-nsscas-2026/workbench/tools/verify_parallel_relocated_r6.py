"""Two complete builds in separate fresh directories, then all prior negatives.

The two fresh directories run concurrently; neither consumes the other's outputs.
Original PDFs are linked as read-only tool inputs and hash-verified before/after.
"""
import argparse,json,os,shutil,subprocess,sys,tempfile
from pathlib import Path
from analysis_sources import A,WB,ROOT,digest,write

def main():
 p=argparse.ArgumentParser();p.add_argument('--keep-copies',action='store_true');args=p.parse_args()
 base=json.loads((WB/'checks/repair-r6-baseline.json').read_text());sources=base['source_files']
 for relative,sha in sources.items():assert digest(ROOT/relative)==sha,('source changed',relative)
 folder=Path(tempfile.mkdtemp(prefix='8227-r6-parallel-proof-'));runs=[]
 for n in [1,2]:
  root=folder/f'copy-{n}';wb=root/WB.relative_to(ROOT)
  shutil.copytree(WB.parent,wb.parent,ignore=shutil.ignore_patterns('__pycache__','.DS_Store'))
  for relative in sources:
   target=root/relative;target.parent.mkdir(parents=True,exist_ok=True)
   try:os.link(ROOT/relative,target)
   except OSError:shutil.copy2(ROOT/relative,target)
  log=(folder/f'copy-{n}.log').open('w')
  proc=subprocess.Popen([sys.executable,str(wb/'tools/run_repair_r6.py'),'--single-rebuild'],cwd=root,stdout=log,stderr=subprocess.STDOUT,text=True)
  runs.append((root,wb,log,proc));print(f'Fresh copy{n},PID{proc.pid},log:{log.name}',flush=True)
 checks=[]
 for root,wb,log,proc in runs:
  code=proc.wait();log.close()
  assert code==0,('fresh R6 build failed',log.name,Path(log.name).read_text()[-5000:])
  checks.append(json.loads((wb/'checks/r5/single-rebuild-final.json').read_text()))
 first,second=[c['output_hashes']for c in checks]
 changes=[path for path in sorted(set(first)|set(second))if first.get(path)!=second.get(path)]
 assert not changes,('independent fresh builds differed',changes)
 root,wb,_,_=runs[0]
 negative=subprocess.run([sys.executable,str(wb/'tools/run_repair_r6.py'),'--negative-only'],cwd=root,capture_output=True,text=True)
 (folder/'negative-fixtures.log').write_text(negative.stdout+'\n'+negative.stderr)
 assert negative.returncode==0,('prior negative fixtures failed',str(folder/'negative-fixtures.log'),negative.stderr[-3000:])
 prior=json.loads((wb/'checks/r6/previous-negative-fixtures.json').read_text())['fixtures']
 r6=json.loads((wb/'checks/r6/working-validation.json').read_text())
 assert len(prior)==38 and len(r6['negative_fixtures'])>=11
 family=json.loads((wb/'checks/r6/parallel-families/validation.json').read_text())
 figure=json.loads((wb/'checks/r6/parallel-figures/checkpoint.json').read_text())
 assert len(family['negative_fixtures'])==5 and len(figure['new_negative_fixtures'])==5
 mismatches=[path for path,sha in first.items()if not(ROOT/path).is_file()or digest(ROOT/path)!=sha]
 if mismatches:
  write(WB/'checks/r6/fresh-copy-output-mismatches.json',dict(status='fresh builds agree; author checkout requires refresh',copy_root=str(root),mismatches=mismatches,output_hashes=first))
 assert not mismatches,('fresh builds do not match author outputs',str(folder),mismatches)
 for relative,sha in sources.items():assert digest(ROOT/relative)==sha,('source modified by build',relative)
 manifest=dict(first_rebuild=checks[0]['commands'],second_rebuild=checks[1]['commands'],outputs_compared=len(first),identical=True,changed_paths=[],output_hashes=first,seeded_negative_results=prior,r6_negative_fixtures=r6['negative_fixtures'],family_negative_fixtures=family['negative_fixtures'],figure_negative_fixtures=figure['new_negative_fixtures'],execution='Concurrent complete builds in two independent fresh directories;no shared generated outputs.')
 write(A/'history/rebuild-verification-r6-final-fresh-copy.json',manifest)
 report=dict(status='pass',source_files_hash_checked=len(sources),double_rebuild=True,matches_author_checkout=True,commands_per_run=len(checks[0]['commands']),outputs_compared=len(first),previous_seeded_errors_rejected=len(prior),r6_seeded_errors_rejected=len(r6['negative_fixtures']),family_seeded_errors_rejected=5,figure_seeded_errors_rejected=5,total_seeded_errors_rejected=len(prior)+len(r6['negative_fixtures'])+10,execution=manifest['execution'],limits='Author reproducibility/structural proof on this macOS host; not independent educational review,app orproduction acceptance.')
 write(WB/'checks/fresh-copy-verification-r6.json',report);print(json.dumps(report,indent=2),flush=True)
 if not args.keep_copies:shutil.rmtree(folder)
 else:print(f'Copies retained:{folder}',flush=True)
if __name__=='__main__':main()
