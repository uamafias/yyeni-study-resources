"""Freeze the bounded close-out after reproducibility and regression proof."""
import argparse,json,platform,subprocess
from analysis_sources import A,WB,ROOT,digest,write

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');args=parser.parse_args();target=A/'analysis-snapshot.json'
 if args.check:
  snapshot=json.loads(target.read_text());assert snapshot['snapshot_version']=='8227-analysis-r7-closeout'
  for group in ['files','source_files','review_files']:
   for p,h in snapshot[group].items():assert digest(ROOT/p)==h,(group,p,'hash mismatch')
  print(json.dumps(dict(snapshot='all close-out hashes match',files=len(snapshot['files']),sources=len(snapshot['source_files']),review_files=len(snapshot['review_files'])),indent=2));return
 baseline=json.loads((WB/'checks/repair-r7-closeout-baseline.json').read_text());proof=json.loads((WB/'checks/r7-closeout/fresh-copy-proof.json').read_text());history=json.loads((A/'history/rebuild-verification-r7-closeout-final-fresh-copy.json').read_text());inputs=json.loads((WB/'checks/r7-closeout/fresh-copy-input-manifest.json').read_text());check=json.loads((WB/'checks/r7-closeout/final-validation.json').read_text())
 assert digest(A/'history/analysis-snapshot-r7.json')==baseline['snapshot_r7_sha256']
 assert proof['double_rebuild']and proof['matches_author_checkout']and history['identical']and proof['total_seeded_errors_rejected']==74
 assert len(check['new_negative_fixtures'])==1
 for p,h in history['output_hashes'].items():assert digest(ROOT/p)==h,('output changed after fresh proof',p)
 assert inputs['identical_across_author_and_two_fresh_copies_before_and_after']
 for p,h in inputs['tools_sha256_before'].items():assert digest(ROOT/p)==h,('pipeline input changed after proof',p)
 for p,h in {**baseline['source_files'],**baseline['review_file_hashes']}.items():assert digest(ROOT/p)==h,('protected source/review changed',p)
 paths=[p for p in WB.parent.rglob('*')if p.is_file()and p!=target and 'review'not in p.relative_to(WB.parent).parts and '__pycache__'not in p.parts and p.name!='.DS_Store']
 paths +=[ROOT/p for p in ['AGENTS.md','TEAM-PLAYBOOK.md','BLOOM-CLASSIFICATION.md','workbench/playbook/README.md','workbench/playbook/quality.md','workbench/playbook/templates.md','workbench/playbook/textbook-analysis.md']]
 files={str(p.relative_to(ROOT)):digest(p)for p in sorted(set(paths))}
 write(target,dict(snapshot_version='8227-analysis-r7-closeout',date='2026-11-23',status='Accepted R7 close-out author complete; next step 3, with Claude confirmation at start of step-3 review',resource_git_head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),scope='Twelve best-member re-decisions, three gap changes, family demands/prompt policy, template annotations, planning limits and cosmetic spacing only. No PLAN, recipes, runtime generators, work orders, imports or assignment.',history=dict(path=str((A/'history/analysis-snapshot-r7.json').relative_to(ROOT)),sha256=baseline['snapshot_r7_sha256']),files=files,source_files=baseline['source_files'],review_files=baseline['review_file_hashes'],environment=dict(python=platform.python_version(),macos=platform.mac_ver()[0]),checks=['checks/repair-r7-closeout.md','checks/r7-closeout/fresh-copy-proof.json','checks/r7-closeout/final-validation.json','checks/r7-closeout/negative-only-r7-closeout.json'],verification_levels=dict(structural='Two full independent fresh-copy builds match author outputs; all retained and the close-out fixture reject seeded errors.',content='Native all-member and best-subpart author reads; accepted source-item links unchanged; bounded search and template limitations retained.',independent_review='Claude accepted R7; named close-out corrections are confirmed at the start of step-3 review. No extra standalone review round is required.',app_and_production='No recipe runtime, app or production acceptance. No commit, push, publication, import or learner assignment.')))
 print(json.dumps(dict(frozen_files=len(files),sources=len(baseline['source_files']),review_files=len(baseline['review_file_hashes']),snapshot_sha256=digest(target)),indent=2))
if __name__=='__main__':main()
