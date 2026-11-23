"""Rebuild twice in two independent fresh copies, preserving immutable inputs."""
import argparse,json,os,shutil,subprocess,sys,tempfile
from pathlib import Path
from analysis_sources import A,WB,ROOT,digest,write

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--keep-copies',action='store_true');args=parser.parse_args()
 baseline=json.loads((WB/'checks/repair-r7-baseline.json').read_text());sources=baseline['source_files']
 for p,h in sources.items():assert digest(ROOT/p)==h,('protected source changed',p)
 # Freeze all author inputs before copying; concurrent author edits invalidate proof.
 inputs={str(p.relative_to(ROOT)):digest(p)for p in sorted((WB/'tools').rglob('*'))if p.is_file()and '__pycache__'not in p.parts}
 folder=Path(tempfile.mkdtemp(prefix='8227-r7-fresh-proof-'));runs=[]
 for n in [1,2]:
  root=folder/f'copy-{n}';wb=root/WB.relative_to(ROOT)
  shutil.copytree(WB.parent,wb.parent,ignore=shutil.ignore_patterns('__pycache__','.DS_Store'))
  for relative in sources:
   target=root/relative;target.parent.mkdir(parents=True,exist_ok=True)
   try:os.link(ROOT/relative,target)
   except OSError:shutil.copy2(ROOT/relative,target)
  log=(folder/f'copy-{n}.log').open('w');proc=subprocess.Popen([sys.executable,str(wb/'tools/run_repair_r7.py'),'--single-rebuild'],cwd=root,stdout=log,stderr=subprocess.STDOUT,text=True)
  runs.append((root,wb,log,proc));print(f'Fresh copy {n}: PID {proc.pid}; log {log.name}',flush=True)
 checks=[]
 for root,wb,log,proc in runs:
  code=proc.wait();log.close();assert code==0,('fresh R7 build failed',log.name,Path(log.name).read_text()[-6000:])
  checks.append(json.loads((wb/'checks/r7/single-rebuild-r7.json').read_text()))
 first,second=[c['output_hashes']for c in checks];changed=[p for p in sorted(set(first)|set(second))if first.get(p)!=second.get(p)]
 assert not changed,('independent copies differed',changed)
 mismatches=[p for p,h in first.items()if not(ROOT/p).is_file()or digest(ROOT/p)!=h]
 if mismatches:write(WB/'checks/r7/fresh-copy-mismatches.json',dict(status='copies agree; author outputs differ',folder=str(folder),paths=mismatches))
 assert not mismatches,('fresh outputs differ from author checkout',mismatches)
 root,wb,_,_=runs[0];log=folder/'negative-fixtures.log'
 with log.open('w')as out:
  proc=subprocess.run([sys.executable,str(wb/'tools/run_repair_r7.py'),'--negative-only'],cwd=root,stdout=out,stderr=subprocess.STDOUT,text=True)
 assert proc.returncode==0,('fresh negative fixtures failed',str(log),log.read_text()[-6000:])
 negative=json.loads((wb/'checks/r7/negative-only-r7.json').read_text());prior=negative['previous_seeded_negative_results'];assert len(prior)==38
 for p,h in sources.items():assert digest(ROOT/p)==h
 assert inputs=={p:digest(ROOT/p)for p in inputs},'author inputs changed during fresh-copy proof'
 saved=dict(first_rebuild=checks[0]['commands'],second_rebuild=checks[1]['commands'],identical=True,output_hashes=first,outputs_compared=len(first),previous_seeded_negative_results=prior,execution='Two complete independent fresh-copy builds run concurrently, with no shared generated output. Immutable source PDFs linked, never edited.')
 write(A/'history/rebuild-verification-r7-final-fresh-copy.json',saved)
 write(WB/'checks/r7/fresh-copy-input-manifest.json',dict(status='pass',identical_across_both_fresh_copies_and_author=True,sha256=inputs))
 proof=dict(status='Two fresh-copy full rebuilds passed, outputs byte-identical and matched the author checkout; retained and new negative fixtures rejected',source_files_hash_checked=len(sources),author_input_files_hash_checked=len(inputs),commands_per_run=len(checks[0]['commands']),outputs_compared=len(first),double_rebuild=True,matches_author_checkout=True,established_subprocess_negatives_rejected=38,
  fixture_records=['checks/r7/negative-only-r7.json','checks/r6/working-validation.json','checks/r7/legacy-negative-protections.json','checks/r7/family-negative-validation.json','checks/r7/parallel-sources/validation.json','checks/r7/final-validation.json'],
  limitations='Author reproducibility and structural checks on this host; independent educational acceptance, application testing and production readiness are separate.')
 # Preserve complete negative-only proof in author workspace as well.
 write(WB/'checks/r7/negative-only-r7.json',negative);write(WB/'checks/r7/fresh-copy-proof.json',proof);print(json.dumps(proof,indent=2),flush=True)
 if not args.keep_copies:shutil.rmtree(folder)
 else:print('Copies retained: '+str(folder),flush=True)
if __name__=='__main__':main()
