"""Freeze the R7 author hand-back after full fresh-copy and negative proof."""
import argparse,json,platform,subprocess
from analysis_sources import A,WB,ROOT,digest,write

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');args=parser.parse_args();target=A/'analysis-snapshot.json'
 if args.check:
  d=json.loads(target.read_text());assert d['snapshot_version']=='8227-analysis-r7'
  for group in ['files','source_files','review_files']:
   for p,h in d[group].items():assert digest(ROOT/p)==h,(group,p,'hash mismatch')
  print(json.dumps(dict(snapshot='all R7 hashes match',files=len(d['files']),sources=len(d['source_files']),review_files=len(d['review_files'])),indent=2));return
 baseline=json.loads((WB/'checks/repair-r7-baseline.json').read_text());fresh=json.loads((WB/'checks/r7/fresh-copy-proof.json').read_text());proof=json.loads((A/'history/rebuild-verification-r7-final-fresh-copy.json').read_text())
 assert fresh['double_rebuild']and fresh['matches_author_checkout']and proof['identical']and len(proof['previous_seeded_negative_results'])==38
 for p,h in proof['output_hashes'].items():assert digest(ROOT/p)==h,('output changed after proof',p)
 inputs=json.loads((WB/'checks/r7/fresh-copy-input-manifest.json').read_text())
 for p,h in inputs['sha256'].items():assert digest(ROOT/p)==h,('author input changed after proof',p)
 validation=json.loads((WB/'checks/r7/final-validation.json').read_text());assert len(validation['new_negative_fixtures'])==4
 assert digest(A/'history/analysis-snapshot-r6.json')==baseline['snapshot_r6_sha256']
 for p,h in {**baseline['source_files'],**baseline['review_file_hashes']}.items():assert digest(ROOT/p)==h
 paths=[p for p in WB.parent.rglob('*')if p.is_file()and p!=target and 'review'not in p.relative_to(WB.parent).parts and '__pycache__'not in p.parts and p.name!='.DS_Store']
 paths +=[ROOT/p for p in ['AGENTS.md','TEAM-PLAYBOOK.md','BLOOM-CLASSIFICATION.md','workbench/playbook/README.md','workbench/playbook/quality.md','workbench/playbook/templates.md','workbench/playbook/textbook-analysis.md']]
 write(target,dict(snapshot_version='8227-analysis-r7',date='2026-11-23',status='author repair complete; Claude short cross-vendor check pending; step 3 waits',resource_git_head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),scope='R7 gap, rejection, family and named record repair only; no PLAN, recipes, runtime generators, work orders, imports or assignment.',history=dict(path=str((A/'history/analysis-snapshot-r6.json').relative_to(ROOT)),sha256=baseline['snapshot_r6_sha256']),files={str(p.relative_to(ROOT)):digest(p)for p in sorted(set(paths))},source_files=baseline['source_files'],review_files=baseline['review_file_hashes'],environment=dict(python=platform.python_version(),macos=platform.mac_ver()[0]),checks=['checks/repair-r7-report.md','checks/r7/fresh-copy-proof.json','checks/r7/final-validation.json','checks/r7/negative-only-r7.json'],verification_levels=dict(structural='Two independent fresh-copy rebuilds match author output; retained and new negative suites reject seeded faults.',content='Source-image author comparisons and independently recomputed named corrections; source-item tags unchanged; limits in R7 report.',independent_review='Previous named scope accepted; current R7 awaits Claude short check. Parallel author assistance is not independent review.',app_and_production='No app tests, deployment, publication, installation, import or learner assignment.')))
 print(json.dumps(dict(frozen_files=len(paths),sources=len(baseline['source_files']),review_files=len(baseline['review_file_hashes']),snapshot_sha256=digest(target)),indent=2))
if __name__=='__main__':main()
