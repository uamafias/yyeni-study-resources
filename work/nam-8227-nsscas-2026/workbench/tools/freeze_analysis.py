"""Freeze or verify this subject's author-repair evidence. Never changes sources."""
import argparse
import hashlib
import json
import platform
import subprocess
from importlib.metadata import version
from analysis_sources import A, ROOT, WB, digest, write


def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args()
 target=A/'analysis-snapshot.json'
 if args.check:
  data=json.loads(target.read_text())
  for key in ['files','source_files','review_files']:
   for path,sha in data[key].items():assert digest(ROOT/path)==sha,(key,path,'hash mismatch')
  print(json.dumps({'snapshot':'all hashes match','files':len(data['files']),'sources':len(data['source_files']),'review_files':len(data['review_files'])},indent=2));return
 baseline=json.loads((WB/'checks/repair-r2-baseline.json').read_text())
 review_baseline=json.loads((WB/'checks/repair-r5-baseline.json').read_text())
 assert digest(A/'history/analysis-snapshot-r4.json')==review_baseline['snapshot_r4_sha256']
 completion=json.loads((A/'textbook-author-completion-r5.json').read_text())
 assert completion['independent_acceptance']is False
 fresh=json.loads((WB/'checks/fresh-copy-verification-r5.json').read_text())
 assert fresh['status']=='pass'and fresh['matches_author_checkout']and len(fresh['seeded_negative_results'])==38
 assert digest(A/'history/analysis-snapshot-r3.json')=='208a33a2027295d09c84f70423b370aa27e5626df289114842181383ce64389d'
 assert digest(A/'history/analysis-snapshot-r2.json')=='85b782f9dc620f0b1697c29cb4a4bdf942f345a66abace60fd7c61b6b6f174ee'
 old=json.loads((A/'history/analysis-snapshot-r1.json').read_text())
 assert digest(A/'history/analysis-snapshot-r1.json')=='1afe99d597617897cb3bf0489cd3bcbc236624fef05cef53a8aa4a92704a561f'
 revision='11cd03fe639f9936dd9f83fd04bd6f04d5181676'
 reconciliation=[]
 for path,expected in old['files'].items():
  original=subprocess.check_output(['git','show',revision+':'+path],cwd=ROOT)
  assert hashlib.sha256(original).hexdigest()==expected,('R1 Git object mismatch',path)
  current=digest(ROOT/path)
  reconciliation.append({'path':path,'r1_expected_sha256':expected,'r1_git_object_matches':True,
       'current_sha256':current,'state':'unchanged' if current==expected else 'author repair; new hash frozen in R5'})
 write(WB/'checks/round1-manifest-reconciliation.json',{'r1_commit':revision,'r1_files':reconciliation,
    'original_source_hashes':baseline['original_sources'],'history_snapshot_sha256':digest(A/'history/analysis-snapshot-r1.json')})
 sources=dict(baseline['original_sources'])
 for record in json.loads((A/'source-holdings.json').read_text())['records']:
  if record.get('sha256')and(ROOT/record['path']).is_file():
   assert digest(ROOT/record['path'])==record['sha256'],('source holding changed',record['path'])
   sources[record['path']]=record['sha256']
 for d in json.loads((A/'cambridge-corpus-index.json').read_text())['documents']:
  assert digest(ROOT/d['path'])==d['sha256'],('Cambridge source changed',d['path'])
  sources[d['path']]=d['sha256']
 for path,sha in baseline['original_sources'].items():assert digest(ROOT/path)==sha
 for path,sha in review_baseline['review_file_hashes'].items():assert digest(ROOT/path)==sha
 paths=[p for p in WB.parent.rglob('*') if p.is_file() and 'review' not in p.relative_to(WB.parent).parts
      and '__pycache__' not in p.parts and p!=target]
 # Shared policies are read-only references, not a new framework implementation.
 paths += [ROOT/p for p in ['AGENTS.md','TEAM-PLAYBOOK.md','BLOOM-CLASSIFICATION.md',
      'workbench/playbook/README.md','workbench/playbook/quality.md','workbench/playbook/templates.md','workbench/playbook/textbook-analysis.md',
      'operations/tools/pdf_ocr_macos.swift']]
 files={str(p.relative_to(ROOT)):digest(p) for p in sorted(set(paths))}
 write(target,{'snapshot_version':'8227-analysis-r5','date':'2026-11-21','status':'author repair and textbook analysis complete; ready for focused independent cross-vendor check; acceptance pending',
      'resource_git_head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
      'scope':'Repair round5and completed step2source analysis only. T1–T6author complete;independent acceptance pending. No step3PLAN/contract,work orders,recipes,runtime generators or publication.',
      'history':{'path':str((A/'history/analysis-snapshot-r4.json').relative_to(ROOT)),'sha256':digest(A/'history/analysis-snapshot-r4.json'),
                 'r3_path':str((A/'history/analysis-snapshot-r3.json').relative_to(ROOT)),'r3_sha256':digest(A/'history/analysis-snapshot-r3.json'),
                 'r1_path':str((A/'history/analysis-snapshot-r1.json').relative_to(ROOT)),'r1_sha256':digest(A/'history/analysis-snapshot-r1.json')},
      'files':files,'source_files':sources,'review_files':review_baseline['review_file_hashes'],
      'environment':{'python':platform.python_version(),'macos':platform.mac_ver()[0],
         'macos_build':subprocess.check_output(['sw_vers','-buildVersion'],text=True).strip(),
         'swift':subprocess.check_output(['swift','--version'],text=True).splitlines()[0],
         'dependencies':{n:version(n) for n in ['pypdf','PyMuPDF','Pillow','sympy']}},
      'checks':['checks/derivative-verification.json','checks/rebuild-verification.json',
          'checks/reviewer-scan-reconciliation.json','checks/round1-manifest-reconciliation.json',
          'checks/repair-r4-validation.json','checks/crop-containment.json','checks/repair-r5-report.md','checks/fresh-copy-verification-r5.json',
          'checks/repair-r5-part1-validation.json','checks/repair-r5-textbook-working-validation.json','checks/textbook-synthesis-validation-r5.json',
          'analysis/textbook-completion-audit-r5.json','analysis/textbook-author-completion-r5.json'],
      'verification_levels':{'structural':'author checks; deterministic assembly and seeded failure checks',
         'content':'source/render author inspection,119question tables,250part reconciliations,821award rows,891textbook pages,3940source records and5752independent-method response checks;not independent repair acceptance',
         'independent_review':'Earlier named scope accepted with repairs;currentR5Part1corrections and both complete textbook analyses await fresh cross-vendor classification and answer checks',
         'owner':'binding decisions applied; no claim of final resource acceptance',
         'app_and_production':'not tested, installed, imported, assigned or activated'},
      'source_limits':['One original PDF-named source is documented HTML/403 and excluded',
         'Proof/final equivalence and full official memo bank remain unresolved',
         'OCR text is discovery only; original run environment not completely recorded',
         'Cambridge discovery corpus is not exhaustively classified; selected originals are verified separately',
         'All 2021-2025 report sections read; 95 consolidated marking rules and 119 question award records, including three explicitly derived completions are author transcriptions, not independent review',
         'All891agreed textbook pages enumerated,3940records individually mapped,1758figures,5752response checks,380analysis families and138-demandinsights;independent correctness/classification acceptance pending',
         'Radian interpretation lacks a posed textbook exercise despite two teaching figures;source defects,extra methods and ambiguous regions remain binding',
         'Provenance compares119questions with3208local pages;158above-threshold candidates visually read;missing confirmed matches are unresolved,not proven original']})
 print(json.dumps({'frozen_files':len(files),'source_paths':len(sources),'review_files':len(review_baseline['review_file_hashes']),'snapshot_sha256':digest(target)},indent=2))
if __name__=='__main__':main()
