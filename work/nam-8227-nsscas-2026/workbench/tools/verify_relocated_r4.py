"""Rebuild an isolated copy, with fresh workspace files and local source hard links."""
import json,shutil,tempfile,subprocess,sys,os
from pathlib import Path
from analysis_sources import A,WB,ROOT,digest,write

def main():
 temporary=Path(tempfile.mkdtemp(prefix='8227-r4-relocation-'));copy_root=temporary/'resources';copy_wb=copy_root/WB.relative_to(ROOT)
 shutil.copytree(WB.parent,copy_wb.parent,ignore=shutil.ignore_patterns('__pycache__','.DS_Store'))
 baseline=json.loads((A/'history/analysis-snapshot-r3.json').read_text())
 sources=baseline['source_files']
 for relative,sha in sources.items():
  target=copy_root/relative;target.parent.mkdir(parents=True,exist_ok=True)
  assert digest(ROOT/relative)==sha,('source changed',relative)
  try:os.link(ROOT/relative,target)
  except OSError:shutil.copy2(ROOT/relative,target)
 # Sources are read only inputs; workspace records are real independent copies.
 print('Isolated workspace and source copies prepared; running two rebuilds.',flush=True)
 completed=subprocess.run([sys.executable,str(copy_wb/'tools/run_repair_checks.py')],cwd=copy_root,text=True,capture_output=True)
 (temporary/'rebuild.log').write_text(completed.stdout+'\n'+completed.stderr)
 assert completed.returncode==0,('fresh-copy rebuild failed',str(temporary/'rebuild.log'),completed.stdout[-1000:],completed.stderr[-1800:])
 check=json.loads((copy_wb/'checks/rebuild-verification.json').read_text())
 assert check['identical'] and len(check['seeded_negative_results'])==7
 write(WB/'checks/fresh-copy-verification-r4.json',{'status':'pass','workspace_copy':'isolated temporary repository layout; no path edits','source_files_hash_checked':len(sources),
  'workspace_files':'independent copies; source PDFs hardlinked as immutable inputs or copied','double_rebuild':True,'outputs_compared':check['outputs_compared'],
  'seeded_negative_results':check['seeded_negative_results'],'limits':'macOS with the documented installed dependencies. This establishes relocation on this host, not Linux support or independent educational acceptance.'})
 shutil.rmtree(temporary)
 print(json.dumps({'fresh_copy_double_rebuild':'pass','outputs_compared':check['outputs_compared'],'negative_fixtures':7}))
if __name__=='__main__':main()
