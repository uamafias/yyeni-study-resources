"""Exercise the existing v1 loader read-only; never register or activate a package."""
import argparse,hashlib,json,shutil,sys,tempfile
from pathlib import Path
from build_source import ROOT,WB,S,dump,read,sha
sys.path.insert(0,str(ROOT))
from yyeni_workbench_tools.__main__ import build_candidate,verified_provider,inventory,canonical

def verify(app_root):
 definition=read(WB/'package-definition.json');expected=hashlib.sha256(canonical({'definition':definition,'source':inventory(S)})).hexdigest()
 candidate=WB/'candidates'/expected[:16]
 built=build_candidate(WB,None)if not candidate.exists()else {'candidate':str(candidate),'manifest_sha256':sha(candidate/'manifest.json'),'state':'candidate','counts':read(candidate/'manifest.json')['counts']}
 assert read(candidate/'manifest.json')['source_input_sha256']==expected
 _,p=verified_provider(candidate,app_root)
 samples=[]
 for row in p.catalogue():
  for seed in (0,1,42,2**63-1):
   q=p.generate(row['id'],seed);assert q['recipe_version']=='0.1.5'and q['generator_version']==2
   samples.append({'selection_id':row['id'],'seed':seed,'fingerprint':q['fingerprint'],'instance_hash':q['instance_hash']})
 assets=read(candidate/'asset-index.json');asset_roles=0
 for h,row in assets.items():
  for role in row['roles']:
   assert p.resolve_asset('8227:asset:'+h,h,role).read_bytes()==(candidate/row['path']).read_bytes();asset_roles+=1
 negative=[]
 with tempfile.TemporaryDirectory(prefix='candidate-audit-',dir=WB/'authoring')as temp:
  temp=Path(temp);copy=temp/'relocated';shutil.copytree(candidate,copy)
  _,other=verified_provider(copy,app_root)
  for row in p.catalogue():assert p.generate(row['id'],42)==other.generate(row['id'],42)
  # The actual package verifier must reject each corruption before provider import.
  for case in ('changed-file','missing-file','unlisted-file'):
   bad=temp/case;shutil.copytree(candidate,bad)
   if case=='changed-file':(bad/'provider.py').write_text((bad/'provider.py').read_text()+'\n# seeded corruption\n')
   elif case=='missing-file':(bad/'provider.py').unlink()
   else:(bad/'unlisted.txt').write_text('seeded')
   try:verified_provider(bad,app_root)
   except ValueError:negative.append(case)
   else:raise AssertionError('Corrupt candidate was accepted: '+case)
  # A sealed but unsuitable new catalogue field is not silently accepted by v1.
  bad=temp/'unknown-field';shutil.copytree(candidate,bad)
  cat=read(bad/'catalogue.json');recipes=read(bad/'recipes.json')
  cat[0]['blooms_level']=3;recipes[0]['public']['blooms_level']=3
  dump(bad/'catalogue.json',cat);dump(bad/'recipes.json',recipes)
  manifest=read(bad/'manifest.json');manifest['files']['catalogue.json']=sha(bad/'catalogue.json');manifest['files']['recipes.json']=sha(bad/'recipes.json');dump(bad/'manifest.json',manifest)
  try:verified_provider(bad,app_root)
  except ValueError:negative.append('unsupported-catalogue-field')
  else:raise AssertionError('Unsupported metadata accepted by old allowlist')
 result=dict(status='pass',scope='Existing app provider-v1 loader/contracts read-only; not server/UI, marker, import or release acceptance',candidate=str(candidate.relative_to(ROOT)),manifest_sha256=sha(candidate/'manifest.json'),source_input_sha256=expected,counts=built['counts'],validated_instances=len(samples),prepared_assets=len(assets),resolved_asset_roles=asset_roles,relocated_candidate='14 selection replays byte-identical including frozen memo/instance hashes',negative_fixtures_rejected=negative,app_contract_hashes={str(path.relative_to(app_root)):sha(path)for path in [app_root/'services/api/workbench_platform'/name for name in ('loader.py','contracts.py','presentation.py','marking.py')]},samples=samples,release_approved=False,registry_modified=False)
 dump(WB/'checks/stage-e/candidate.json',result);print(json.dumps({k:v for k,v in result.items()if k!='samples'},indent=2))
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--app-root',type=Path,required=True);verify(a.parse_args().app_root.resolve())
