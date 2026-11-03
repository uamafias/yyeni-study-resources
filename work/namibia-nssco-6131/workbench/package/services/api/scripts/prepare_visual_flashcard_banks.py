"""Prepare all authored visual families through the existing PNG image path.

Immutable output: a changed bank must use a new version/directory. No DB or AI.
"""
import argparse
import hashlib
import importlib
import json
from pathlib import Path
import sys
import types

API=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(API))
package=types.ModuleType('services');package.__path__=[str(API/'services')];sys.modules['services']=package
from services.math_generators.figures import validate_figure
from prepared_diagram_png import render

ROOT=API/'data/flashcard_diagrams/v1'
PREFIX='yyeni-diagram:v1:'


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--font',required=True);ap.add_argument('--count',type=int,default=32)
    args=ap.parse_args()
    if not 23<=args.count<=64:ap.error('Use between 23 and 64 prepared instances per level')
    if (ROOT/'manifest.json').exists():raise SystemExit('Bank exists. Preserve it; create a new version for changed assets.')
    ROOT.mkdir(parents=True,exist_ok=True)
    checkpoint=ROOT/'draft-progress.json'
    manifest=json.loads(checkpoint.read_text()) if checkpoint.exists() else {}
    for name in ('geometry','graphs','statistics'):
        module=importlib.import_module('services.math_generators.family_visual_'+name)
        for gen in module.GENERATORS:
            group=manifest.setdefault(gen.generator_id,{'title':gen.title,'lesson_id':gen.lesson_id,'labels':gen.labels,'levels':{}})
            for level in gen.levels:
                if str(level) in group['levels']:
                    print(f'{gen.generator_id} level {level}: already prepared',flush=True);continue
                rows=[];seen=set()
                for seed in range(1,513):
                    p=gen.generate(seed,level); m=dict(p.machine)
                    qspec=m.pop('question_figure');aspec=m.pop('reference_figure') or qspec
                    identity=json.dumps([p.question,qspec],sort_keys=True,ensure_ascii=False)
                    if identity in seen:continue
                    seen.add(identity);refs={}
                    for role,spec in [('question',qspec),('answer',aspec)]:
                        data=render(spec,args.font);digest=hashlib.sha256(data).hexdigest()
                        if len(data)>149000:raise ValueError((gen.generator_id,level,seed,'PNG exceeds existing inline image bound'))
                        path=ROOT/(digest+'.png')
                        if not path.exists():path.write_bytes(data)
                        refs[role]=PREFIX+digest
                    m.update(reference_images=refs,prepared_bank_version=1,source_seed=seed)
                    rows.append({'question':p.question,'answer':p.answer,'skill':p.skill,'machine':m,
                                 'steps':[v.to_dict() for v in p.steps],'marking':dict(p.marking)})
                    if len(rows)>=args.count:break
                if len(rows)<23:raise ValueError((gen.generator_id,level,'Insufficient distinct diagram instances',len(rows)))
                group['levels'][str(level)]=rows
                checkpoint.write_text(json.dumps(manifest,ensure_ascii=False)+'\n')
                print(f'{gen.generator_id} level {level}: {len(rows)} prepared',flush=True)
            manifest[gen.generator_id]=group
    (ROOT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print(f'Finished {len(manifest)} visual families; {sum(len(v["levels"]) for v in manifest.values())} levels',flush=True)

if __name__=='__main__':main()
