"""Bind planned resources to generated slots; no assets or learner answers are generated."""
from pathlib import Path
from collections import defaultdict
import json,sys
from plan_spec_6137 import VISUALS
W=Path(__file__).resolve().parents[1]
def read(p):return json.loads(p.read_text())
def dump(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')

TARGETS=[
 ['1.1.04-01','1.1.04-02','1.1.04-03'],
 ['1.2.84','1.2.85','1.2.82'],
 ['1.3.01','1.3.02','1.3.04'],
 ['1.4.02','1.4.03','1.4.04'],
 ['1.5.04','1.5.06','1.5.07','1.5.09'],
 ['1.5.91','1.5.92','1.5.93','P03'],
 ['1.6.03','1.6.04','1.6.07','1.6.08'],
 ['1.7.01','1.7.04'],['2.1.07'],['2.2.02'],
 ['2.3.91','2.3.92','2.3.93','2.3.05'],
 ['2.4.03'],['2.5.04'],['2.6.04'],
 ['3.1.07','3.1.06','3.1.09'],['3.2.02'],
 ['3.3.01','3.3.04'],['4.1.04','4.1.07','4.1.08'],
 ['4.2.01','4.2.02','4.2.03','4.2.07'],
 ['4.2.06','4.2.06','4.2.06-01','4.2.06-01','4.2.06-02','4.2.06-02']]

def build():
    used=set();resources=[];counts=defaultdict(int)
    for (tid,family,n,method),selectors in zip(VISUALS,TARGETS):
        assert len(selectors)==n
        wo=read(W/'topics'/tid/'work_order.json')
        for selector in selectors:
            if selector.startswith('P'):
                pool=[s for s in wo['performance_tasks'] if s['slot'].endswith('-'+selector)]
            else:
                pool=[s for s in wo['item_slots'] if s['objective_id']=='OBJ-6137-'+selector and s['slot'] not in used]
                pool.sort(key=lambda s: {'INTERP':0,'CALC':1,'APP':2,'PROC':3}.get(s['subtype'],4))
            assert pool,(tid,selector)
            slot=pool[0];used.add(slot['slot']);counts[tid]+=1
            rid=f'VIS-6137-{tid}-{counts[tid]:02d}'
            photo='photograph' in method
            resources.append({'resource_id':rid,'topic_id':tid,'family':family,'assigned_item_id':slot['slot'],
              'objective_id':slot.get('objective_id'),'objective_title':slot.get('objective_title') or slot['brief'],
              'kind':'licensed_photo' if photo else 'generated_diagram_or_chart',
              'authoring_method':method,'authoring_owner':'Claude visual author; Codex independent review',
              'question_path':f"assets/images/{slot['slot']}-question.png",
              'answer_path':f"assets/images/{slot['slot']}-answer.png",
              'master_path':None if photo else f"assets/masters/{slot['slot']}.svg",
              'data_spec_path':None if photo else f"assets/specs/{slot['slot']}.json",
              'status':'planned, not generated or approved',
              'requirements':['One resource at a time; define data/geometry and solve independently before rendering.',
                  'Question image reveals no answer; answer image uses the same geometry/data.',
                  'Check full size, phone width and greyscale; read all labels, units, scales, keys and direction arrows.',
                  'Codex separately checks content, geometry/data, prompt, answer, rubric and notes support.',
                  'Capture source/licence and derivative permissions for photographs; do not trace exam maps or reproduce official figures.'],
              'yyeni_asset_id':None,'upload_status':'not authorised or attempted'})
    dump(W/'planning/visual-resource-plan-6137.json',{'purpose':'Existing planned slots requiring concrete visual resources; no additional item slots created.',
        'resources':resources,'additional_reuse_rule':'Other cards may reuse or crop a planned original master with its ID and answer-separation checks. A table can support data reasoning but cannot replace a required photograph, map or plotted-form task.',
        'publication_contract':'Before publishing, a subject-scoped helper must copy every referenced asset, verify hashes and link resolution, and emit an import sidecar keyed by exact item IDs. The shared publisher alone does not prove image delivery. No cloud storage upload/import is included in this planning approval.'})
    print(len(resources),'resource sets;',sum(r['kind']=='licensed_photo' for r in resources),'licensed photographs')

if __name__=='__main__':build()
