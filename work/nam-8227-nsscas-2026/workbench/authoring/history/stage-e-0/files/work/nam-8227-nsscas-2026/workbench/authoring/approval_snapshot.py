"""Preserve the owner-approved Stage-D bytes while permitting Stage-E status updates."""
import hashlib,json,shutil,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
WB=ROOT/'work/nam-8227-nsscas-2026/workbench'
ARCHIVE=WB/'planning/approvals/stage-d-4a054832'
EXPECTED='4a0548320dcb9209dcd28e18bd4f6c77423480de6538fcbf1b0f8b6d0e17d8ec'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,d):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
def initialize():
 p=WB/'planning/plan-manifest.json'
 assert sha(p)==EXPECTED,'Approved manifest changed'
 ARCHIVE.mkdir(parents=True,exist_ok=True)
 target=ARCHIVE/'manifest.json'
 if not target.exists():shutil.copyfile(p,target)
 assert sha(target)==EXPECTED
 receipt=ARCHIVE/'approval.json'
 if not receipt.exists():
  dump(receipt,dict(owner='Vitalis',date='2026-11-24',authority='Explicit user instruction in this session',manifest_sha256=EXPECTED,content_digest='e9cd8f58345364e7b3bb45fadf2bab162571cc4c101df5beff2189a514fd8780',scope=['counts','gaps','capabilities','exemplars','MR03-OPS-D4 operations'],authorized_stage='E',release_approved=False,commit_or_push_authorized=False,original_overrides={}))
 return json.loads(receipt.read_text())
def preserve(paths):
 d=initialize();m=json.loads((ARCHIVE/'manifest.json').read_text())
 for rel in paths:
  assert rel in m['files'],rel
  dst=ARCHIVE/'original'/rel
  if not dst.exists():
   assert sha(ROOT/rel)==m['files'][rel],rel
   dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/rel,dst)
  assert sha(dst)==m['files'][rel]
  d['original_overrides'][rel]=str(dst.relative_to(ROOT))
 dump(ARCHIVE/'approval.json',d)
def verify():
 d=initialize();m=json.loads((ARCHIVE/'manifest.json').read_text());n=0
 for key in ['files','source_files','review_files']:
  for rel,s in m[key].items():
   p=ROOT/d['original_overrides'].get(rel,rel)
   assert sha(p)==s,rel
   n+=1
 assert hashlib.sha256(json.dumps(m['files'],sort_keys=True,separators=(',',':')).encode()).hexdigest()==m['content_digest']
 print(json.dumps(dict(status='pass',manifest_sha256=EXPECTED,pins_verified=n,preserved_originals=len(d['original_overrides']),approval_record=str((ARCHIVE/'approval.json').relative_to(ROOT)))))
if __name__=='__main__':
 if len(sys.argv)>1 and sys.argv[1]=='preserve':preserve(sys.argv[2:])
 else:verify()
