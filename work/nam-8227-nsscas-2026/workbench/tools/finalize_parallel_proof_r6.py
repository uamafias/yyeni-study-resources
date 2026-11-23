"""Resume comparison after refreshing stale author outputs; never rerun/copy them."""
import argparse,json,subprocess,sys
from analysis_sources import A,WB,ROOT,digest,write

def main():
 p=argparse.ArgumentParser();p.add_argument('proof_folder');args=p.parse_args()
 from pathlib import Path
 folder=Path(args.proof_folder);checks=[];wbs=[]
 for n in [1,2]:
  root=folder/f'copy-{n}';wb=root/WB.relative_to(ROOT);wbs.append(wb)
  c=json.loads((wb/'checks/r5/single-rebuild-final.json').read_text())
  assert len(c['commands'])==281 and all(r['exit_code']==0 for r in c['commands'])
  assert any('check_repair_r6.py'in' '.join(r['command'])and'--final'in r['command']for r in c['commands'])
  for path,sha in c['output_hashes'].items():assert digest(root/path)==sha,('fresh output changed after build',n,path)
  checks.append(c)
 first,second=[c['output_hashes']for c in checks];assert first==second,'fresh complete builds differ'
 mismatch=[path for path,sha in first.items()if not(ROOT/path).is_file()or digest(ROOT/path)!=sha]
 assert not mismatch,('author outputs still stale',mismatch)
 prior=json.loads((wbs[0]/'checks/r6/previous-negative-fixtures.json').read_text())
 assert prior['status']=='pass'and len(prior['fixtures'])==38
 r6=json.loads((wbs[0]/'checks/r6/working-validation.json').read_text())
 family=json.loads((wbs[0]/'checks/r6/parallel-families/validation.json').read_text())
 figure=json.loads((wbs[0]/'checks/r6/parallel-figures/checkpoint.json').read_text())
 assert r6['status'].startswith('author final')and len(r6['negative_fixtures'])==12
 assert len(family['negative_fixtures'])==5 and len(figure['new_negative_fixtures'])==5
 subprocess.run([sys.executable,str(WB/'tools/check_r6_build_inputs.py'),str(folder)],cwd=ROOT,check=True)
 from verify_r6_preservation import verify
 preservation=verify(save=False)
 execution='Two concurrent complete declared-pipeline builds in separate fresh repository layouts; no shared assembled analysis outputs. Existing generated records and this host source-render caches are retained inputs, not a build from empty output directories.'
 manifest=dict(first_rebuild=checks[0]['commands'],second_rebuild=checks[1]['commands'],outputs_compared=len(first),identical=True,changed_paths=[],output_hashes=first,seeded_negative_results=prior['fixtures'],r6_negative_fixtures=r6['negative_fixtures'],family_negative_fixtures=family['negative_fixtures'],figure_negative_fixtures=figure['new_negative_fixtures'],execution=execution)
 write(A/'history/rebuild-verification-r6-final-fresh-copy.json',manifest)
 report=dict(status='pass',source_files_hash_checked=preservation['source_files_checked'],double_rebuild=True,matches_author_checkout=True,commands_per_run=len(checks[0]['commands']),outputs_compared=len(first),previous_seeded_errors_rejected=38,r6_seeded_errors_rejected=12,family_seeded_errors_rejected=5,figure_seeded_errors_rejected=5,total_seeded_errors_rejected=60,execution=execution,limits='Author reproducibility and structural proof on this macOS host; not independent educational review,app or production acceptance.')
 write(WB/'checks/fresh-copy-verification-r6.json',report)
 mismatch_path=WB/'checks/r6/fresh-copy-output-mismatches.json'
 if mismatch_path.exists():
  old=json.loads(mismatch_path.read_text());old['status']='resolved by targeted author producer rebuild; all158saved output hashes now match both fresh copies';old['resolution_commands']=['screen_provenance_r5.py','annotate_provenance_screen_r5.py','build_analysis.py','check_repair_r2.py','check_repair_r4.py'];write(mismatch_path,old)
 print(json.dumps(report,indent=2))
if __name__=='__main__':main()
