"""Check declared pipeline code/author records across the two proof copies."""
import argparse,json
from pathlib import Path
from analysis_sources import ROOT,WB,digest,write

def main():
 p=argparse.ArgumentParser();p.add_argument('proof_folder',type=Path);args=p.parse_args()
 # These orchestration/presentation tools do not execute inside either build.
 excluded={'render_repair_r6_final.py','freeze_analysis_r6.py','check_r6_build_inputs.py',
           'verify_parallel_relocated_r6.py','verify_relocated_r6.py','finalize_parallel_proof_r6.py'}
 paths=[x for x in (WB/'tools').rglob('*')if x.is_file()and'__pycache__'not in x.parts
        and x.suffix in ['.py','.swift','.json','.txt','.csv']and x.name not in excluded]
 expected={str(x.relative_to(ROOT)):digest(x)for x in sorted(paths)}
 manifests=[]
 for number in [1,2]:
  root=args.proof_folder/f'copy-{number}'
  actual={path:digest(root/path)for path in expected if(root/path).is_file()}
  assert actual==expected,('pipeline tool/author input differs',number,[path for path,sha in expected.items()if actual.get(path)!=sha])
  manifests.append(actual)
 write(WB/'checks/r6/fresh-build-input-manifest.json',dict(status='pass',files_compared=len(expected),
  identical_across_both_fresh_copies_and_author=True,sha256=expected,
  excluded_nonexecuted_orchestrators=sorted(excluded),
  limitation='Post-run equality of declared pipeline code and author records; not an assertion that every inherited generated analysis file was rebuilt from empty directories. The two copies execute the complete declared pipeline independently.'))
 print(len(expected),'pipeline code/author-record hashes match both proof copies and author checkout')
if __name__=='__main__':main()
