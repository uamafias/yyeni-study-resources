"""Build, validate and check candidate subject packages without exporting app copies."""
from __future__ import annotations

import argparse
import ast
import hashlib
import importlib
import json
from pathlib import Path
import shutil
import sys

REPO = Path(__file__).resolve().parents[1]
SEEDS = (0, 1, 42, 2**63 - 1)
PUBLIC_FIELDS = {'id','recipeId','recipeVersion','title','topic','topicKey','task','objectiveIds',
                 'demandIds','description','marks','minMarks','maxMarks','markRange','availability',
                 'holdReason','searchText','renewal','state','syllabusTopic','marksMin','marksMax',
                 'canonicalExamples','distinctSavedQuestions','reviewStatus'}
BLOCKED_IMPORTS = {'models','db','settings','services','routers','fastapi','sqlalchemy',
                   'media','requests','httpx','urllib','socket','subprocess'}


def read(path):
    return json.loads(path.read_text())


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False)+'\n')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical(value):
    return json.dumps(value,sort_keys=True,ensure_ascii=False,allow_nan=False,separators=(',',':')).encode()


def inventory(root):
    result = {}
    for path in sorted(root.rglob('*')):
        if path.is_symlink():
            raise ValueError('Source/release trees must not contain symlinks')
        if '__pycache__' in path.relative_to(root).parts or path.suffix in ('.pyc','.pyo'):
            continue
        if path.is_file() and path != root/'manifest.json':
            result[path.relative_to(root).as_posix()] = sha(path)
    return result


def install_contract(app_root):
    api = app_root.resolve()/'services/api'
    if not (api/'workbench_platform/loader.py').is_file():
        raise ValueError('Pass --app-root pointing to a Yeni checkout with provider contract v1')
    sys.path.insert(0,str(api))
    from workbench_platform.loader import Provider, verify_package
    return Provider, verify_package


def manifest_path(path):
    path=path.resolve()
    for candidate in (path/'manifest.json', path/'package/manifest.json'):
        if candidate.is_file() and read(candidate).get('provider_api_version')==1:
            return candidate
    raise ValueError('Pass the exact built candidate/release directory (or the existing Maths workbench directory)')


def entry_for(path):
    value=read(path)
    return {**{k:value[k] for k in ('package_id','version','curriculum','state')},
            'manifest':path.relative_to(REPO).as_posix(), 'manifest_sha256':sha(path),
            'enabled_recipe_ids':(value.get('approved_recipe_ids',[]) if value['state']=='approved'
                                  else [r['id'] for r in read(path.parent/value['catalogue'])])}


def verified_provider(path,app_root):
    path=manifest_path(path)
    Provider,verify=install_contract(app_root)
    checked=verify(REPO,entry_for(path),allow_candidates=True)
    return path,Provider(checked)


def source_import_checks(root):
    findings=[]
    for path in sorted(root.rglob('*.py')):
        for node in ast.walk(ast.parse(path.read_text())):
            names=([node.module] if isinstance(node,ast.ImportFrom) and not node.level and node.module
                   else [a.name for a in node.names] if isinstance(node,ast.Import) else [])
            for name in names:
                if name.split('.')[0] in BLOCKED_IMPORTS:
                    findings.append({'file':path.relative_to(root).as_posix(),'line':node.lineno,'import':name})
    return findings


def build_candidate(workbench,output):
    definition=read(workbench/'package-definition.json')
    source=workbench/'source'
    if not source.is_dir() or (source/'manifest.json').exists():
        raise ValueError('Author source/ first; a source manifest is not an authoring input')
    files=inventory(source)
    findings=source_import_checks(source)
    if findings:
        raise ValueError('App/network imports in resource source: '+json.dumps(findings))
    definitions=read(source/'recipes.json')
    if not isinstance(definitions,list) or not definitions:
        raise ValueError('recipes.json must contain recipe definitions with public descriptors')
    catalogue=[]
    for recipe in definitions:
        public=dict(recipe['public'])
        if set(public)-PUBLIC_FIELDS:
            raise ValueError('Private/unknown public descriptor fields')
        public['state']='candidate'
        catalogue.append(public)
    if len({r['id'] for r in catalogue})!=len(catalogue):
        raise ValueError('Duplicate selection identity')
    input_digest=hashlib.sha256(canonical({'definition':definition,'source':files})).hexdigest()
    output=(output or workbench/'candidates'/input_digest[:16]).resolve()
    if output.exists():
        raise ValueError('Candidate directory already exists; verify it or choose a new output path')
    if output.is_relative_to(source) or not output.is_relative_to(workbench.resolve()):
        raise ValueError('Candidate output must be inside its workbench and outside source/')
    shutil.copytree(source,output,ignore=shutil.ignore_patterns('__pycache__','*.pyc','*.pyo'))
    write(output/'catalogue.json',catalogue)
    metadata={k:definition[k] for k in ('package_id','version','curriculum','provider_entrypoint','requires')}
    metadata.update(schema_version=1,provider_api_version=1,state='candidate',
                    dependency_versions=definition.get('dependency_versions',{}),
                    catalogue='catalogue.json',rules='subject-rules.json',provenance='provenance.json',
                    files=inventory(output),approved_recipe_ids=[],review={'verdict':'pending'},
                    coverage=definition['coverage'],
                    counts={'recipeSettings':len({r['recipeId'] for r in catalogue}),
                            'assignmentTypes':len(catalogue)},source_input_sha256=input_digest)
    if definition.get('author_checks_entrypoint'):
        metadata['author_checks_entrypoint']=definition['author_checks_entrypoint']
    if definition.get('structural_branches'):
        metadata['structural_branches']=definition['structural_branches']
    write(output/'manifest.json',metadata)
    return {'candidate':str(output),'manifest_sha256':sha(output/'manifest.json'),
            'state':'candidate','counts':metadata['counts']}


def check(path,app_root):
    path,provider=verified_provider(path,app_root)
    manifest=provider.verified.manifest
    checks=manifest.get('author_checks_entrypoint')
    oracle=None
    if checks:
        if not isinstance(checks,str) or checks.count(':')!=1:
            raise ValueError('Invalid author_checks_entrypoint')
        module,name=checks.split(':')
        if module.replace('.','/')+'.py' not in manifest['files']:
            raise ValueError('Author oracle must be sealed in the reviewed candidate')
        oracle=getattr(importlib.import_module(provider.namespace+'.'+module),name)
    results=[]
    fingerprints={}
    for row in provider.catalogue():
        required=manifest.get('structural_branches',{}).get(row['id'],[])
        seeds=list(SEEDS)+list(range(2,8192 if required else 130))
        branches={}
        failed=[]
        distinct=set()
        for seed in dict.fromkeys(seeds):
            try:
                question=provider.generate(row['id'],seed)
                if oracle:
                    result=oracle(question)
                    if not isinstance(result,dict) or result.get('valid') is not True:
                        raise ValueError('Independent author oracle failed')
                branch=question.get('source_branch',{}).get('kind') or json.dumps(question.get('source_branch',{}),sort_keys=True)
                if required and branch not in required:
                    raise ValueError('Instance uses an undeclared structural branch')
                branches[branch]=branches.get(branch,0)+1
                distinct.add(question['fingerprint'])
            except ValueError as exc:
                if str(exc)=='Seed produces another selection branch':
                    continue
                failed.append({'seed':seed,'error':type(exc).__name__,'message':str(exc)[:200]})
            if required and all(branches.get(branch,0)>=64 for branch in required):
                break
            if len(failed)>=8:
                break
        results.append({'key':row['id'],'checked':sum(branches.values()),'branches':branches,
                        'required_branches':required,'branch_coverage_passed':bool(required) and all(branches.get(branch,0)>=64 for branch in required),
                        'distinct_instances':len(distinct),'failures':failed})
        fingerprints[row['id']]=distinct
    technical=not any(r['failures'] or not r['checked'] for r in results)
    report={'schema_version':1,'manifest_sha256':sha(path), 'scope':manifest['coverage'],
            'package_id':manifest['package_id'],'results':results,
            'gates':{'structure_and_integrity':'pass' if technical else 'fail',
                     'independent_author_oracle':'pass' if technical and oracle else 'not_run',
                     'structural_branch_coverage':'pass' if all(r['branch_coverage_passed'] for r in results) else 'not_run',
                     'independent_review': 'pass' if manifest['state']=='approved' else 'not_run'},
            'release_approved':manifest['state']=='approved' and technical and bool(oracle) and all(r['branch_coverage_passed'] for r in results)}
    return report


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--app-root',type=Path,default=REPO.parent/'yyeni')
    sub=parser.add_subparsers(dest='command',required=True)
    for name in ('validate','check','what-to-fix','register'):
        command=sub.add_parser(name)
        command.add_argument('path',type=Path)
        command.add_argument('--report',type=Path)
    build=sub.add_parser('build-candidate')
    build.add_argument('path',type=Path)
    build.add_argument('--output',type=Path)
    build.add_argument('--report',type=Path)
    args=parser.parse_args()
    try:
        if args.command=='build-candidate':
            result=build_candidate(args.path.resolve(),args.output)
            verified_provider(Path(result['candidate']),args.app_root)
            code=0
        elif args.command=='validate':
            path,provider=verified_provider(args.path,args.app_root)
            result={'result':'pass','package_id':provider.package_id,'state':provider.verified.manifest['state'],
                    'manifest_sha256':sha(path),'choices':len(provider.catalogue()),
                    'content_approval':'not established by structural validation'}
            code=0
        elif args.command=='register':
            path,provider=verified_provider(args.path,args.app_root)
            registry=REPO/'workbench/registry.json'
            value=read(registry) if registry.exists() else {'schema_version':1,'packages':[]}
            entries=[entry for entry in value['packages'] if entry['package_id']!=provider.package_id]
            entries.append(entry_for(path))
            write(registry,{'schema_version':1,'packages':entries})
            result={'registry':str(registry),'registry_sha256':sha(registry),
                    'state':provider.verified.manifest['state'],'app_release_selected':False}
            code=0
        elif args.command=='what-to-fix':
            report=read(args.path)
            pending=[{'gate':gate,'status':status} for gate,status in report['gates'].items() if status!='pass']
            result={'pending':pending,'recipe_failures':[r for r in report.get('results',[]) if r.get('failures')],
                    'next':'Resolve applicable missing checks and obtain an independent review before publication' if pending else 'Review the full quality contract before publication'}
            code=int(bool(pending or result['recipe_failures']))
        else:
            result=check(args.path,args.app_root)
            code=int(not result['release_approved'])
        if args.report:
            write(args.report,result)
        print(json.dumps(result,ensure_ascii=False,allow_nan=False))
        return code
    except (OSError,ValueError,KeyError,TypeError,ImportError,AttributeError) as exc:
        result={'result':'fail','error':type(exc).__name__,'message':str(exc)}
        if getattr(args,'report',None):
            write(args.report,result)
        print(json.dumps(result),file=sys.stderr)
        return 1


if __name__=='__main__':
    raise SystemExit(main())
