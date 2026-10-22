#!/usr/bin/env python3
"""Build a one-objective visual pilot and exercise render/check/package end to end."""
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
from xml.etree import ElementTree as ET

WS=Path(__file__).resolve().parents[1]
ROOT=WS.parents[1]
EX=WS/'exemplar/visual'
sys.path.insert(0,str(ROOT/'standard/v0.2.0-draft/checks'))
from yyeni_checks import _artefact_text, run
from publish_chemistry_8224 import package


def read(p):return json.loads(p.read_text())
def write(p,x):
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def stamp(x):x['authored_hash']=hashlib.sha256(_artefact_text(x).encode()).hexdigest()


def main():
    prior=read(EX/'assets-manifest.json')
    subprocess.run([sys.executable,str(WS/'planning/render_chemistry_visuals_8224.py')],check=True)
    assert prior==read(EX/'assets-manifest.json'),'Visual generation was not reproducible'
    for p in (EX/'assets').glob('*.svg'):
        root=ET.parse(p).getroot()
        assert root.tag.endswith('svg')
        assert not any(e.tag.endswith(('script','foreignObject')) for e in root.iter())
    oid='OBJ-8224-1.2.1-04'
    texts=[
        'An electron has negative charge and a proton has positive charge; a neutron has no net electric charge.',
        'Between oppositely charged plates, the electric force on an electron points towards the positive plate, while the force on a proton points towards the negative plate.',
        'A neutron travelling through this electric field continues without electric deflection because it has no net charge.',
        'For equal entry speeds in the same field, the much lighter electron is deflected more strongly than the proton.',
    ]
    claims=[]
    for n,text in enumerate(texts,1):
        claims.append({'claim_id':f'CLM-8224-VIS-{n:03}','objective_ids':[oid],'text':text,'claim_type':'factual','provenance':'generated_gap','evidence':[{'source_id':'SRC-8224-ER-2025','locator':'Chemistry 8224 Paper 2 Q2(a)–(b), printed pages 74–75','support_type':'paraphrase'}],'derived_from_claim_ids':[],'revision':1,'verification':{'status':'unverified','method':'Source-backed pilot; independent semantic review remains required.','reviewer_id':None,'reviewed_at':None,'confidence':0.9},'publishable':False,'notes':[]})
    cids=[c['claim_id'] for c in claims]
    prose=('An electric field can change the direction of a moving charged particle. In this diagram the upper plate is positive and the lower plate is negative. An electron entering from the left bends upwards towards the positive plate. A proton entering from the left bends downwards towards the negative plate. The neutron follows the straight path because it has no net electric charge. The paths begin changing direction as the charged particles enter the field. '
           'The drawing communicates the signs of the charges and the directions of the forces. Its distances and deflections are schematic: do not read a radius or a force magnitude from it. The larger electron deflection represents its greater response at equal entry speeds, but the drawing does not give a numerical ratio. When particles enter with the same speed, the electron is deflected more strongly than the much heavier proton. A quantitative comparison would require defined field strength, speed and masses. '
           'To interpret a particle-path question, first identify the two plate signs. Next identify the charge of each particle. Opposite charges attract, so a negative particle bends towards the positive plate and a positive particle towards the negative plate. Then check that an uncharged particle remains on the initial straight path. Labelling the plates and all three paths makes the reasoning visible. The arrows on the paths indicate motion; the separate field arrow points from the positive plate towards the negative plate.\n\n'
           '![Electron, proton and neutron paths between labelled electric plates](assets/8224-electric-field.png)')
    block={'block_id':'VIS-1.2-b1','block_type':'plain_explanation','heading':'Particle paths in an electric field','text':prose,'claim_ids':cids,'context_tags':[],'assessment_objectives':['A','B'],'claims_seen':dict.fromkeys(cids,1)}
    stamp(block)
    unit={'unit_id':'CU-8224-1.2-VIS','title':'Electric-field diagram pilot','objective_ids':[oid],'level':'NSSCAS','core_status':'core','objective_type':'chem_particle_field','depth_tier':2,'word_budget':{'min':200,'target':260,'max':400},'blocks':[block],'word_count':len(prose.split()),'qa_status':'review_required','notes':['One-objective visual pilot only; not the complete Topic 1.2.']}
    slot=next(s for s in read(WS/'topics/1.2/work_order.json')['item_slots'] if s['objective_id']==oid and s['subtype']=='DIAGRAM')
    item={'item_id':slot['slot'],'objective_ids':[oid],'claim_ids':cids,'item_type':'flashcard','subtype':'DIAGRAM','assessment_objectives':slot['assessment_objectives'],'blooms_level':slot['blooms_level'],'command_word':slot['command_word'],'mark_tariff':slot['mark_tariff'],'difficulty':slot['difficulty'],'prompt':'Sketch the paths of an electron, a proton and a neutron entering horizontally between a positive upper plate and a negative lower plate. Label the plates and paths. Directions only; no scale is required.','canonical_answer':'![Labelled directions of electron, proton and neutron paths](assets/8224-electric-field.png)\nElectron towards the positive upper plate; proton towards the negative lower plate; neutron straight. Deflection starts upon entering the field. At equal entry speeds the electron bends more strongly; the drawing is not quantitatively to scale.','marking_guidance':['Required labels: plate signs and all three particles. Bonds or axes: horizontal entry direction, with arrows on paths. Unambiguous representation: electron upwards, proton downwards, neutron straight.'],'context':{'sector':None,'business_size':None,'ownership':None,'situation':None,'facts':[]},'prerequisite_item_ids':[],'core_status':'core','intentional_duplicate_group':None,'provenance':'Original visual pilot for the approved Chemistry plan.','qa_status':'review_required','claims_seen':dict.fromkeys(cids,1)}
    stamp(item)
    with tempfile.TemporaryDirectory(prefix='8224-visual-') as tmp:
        scratch=Path(tmp)
        for directory in ('curriculum','assessment-evidence'):shutil.copytree(WS/directory,scratch/directory)
        for name in ('subject-profile.yaml','qualification-profile.yaml'):shutil.copy2(WS/name,scratch/name)
        reg=read(scratch/'curriculum/objective_registry.json')
        reg['objectives']=[o for o in reg['objectives'] if o.get('topic_id')!='1.2' or o['objective_id']==oid or not o.get('parent_id')]
        write(scratch/'curriculum/objective_registry.json',reg)
        td=scratch/'topics/1.2'
        contract=read(WS/'topics/1.2/contract.json')
        contract['scope']['included_objective_ids']=[oid]
        contract['depth_constraints']['item_budget']=1
        contract['depth_constraints']['word_budget']={'min':200,'max':400}
        contract['required_outputs'].update(content_units=1,learning_items=1)
        write(td/'contract.json',contract)
        write(td/'claims/canonical_claim_ledger.json',{'ledger_id':'CLM-LEDGER-8224-VIS','claims':claims})
        write(td/'content-units/CU-8224-1.2-VIS.json',unit)
        write(td/'learning-items/topic_1.2_items.json',{'dataset_id':'ITEMS-8224-VIS','topic_id':'1.2','items':[item]})
        shutil.copytree(EX/'assets',td/'assets')
        subprocess.run([sys.executable,str(ROOT/'standard/v0.2.0-draft/build/render_notes.py'),str(scratch),'1.2'],check=True)
        report=run(str(scratch),'1.2')
        write(EX/'qa_report.json',report)
        write(td/'qa_report.json',report)
        failures=[c for c in report['deterministic_checks'] if c['status']=='fail']
        if failures:raise ValueError(failures)
        assert report['release_decision']=='publish'
        assets=package(scratch,scratch/'published')
        for directory in ('claims','content-units','learning-items'):
            shutil.copytree(td/directory,EX/directory,dirs_exist_ok=True)
        shutil.copy2(td/'contract.json',EX/'contract.json')
        for p in td.glob('*.md'):shutil.copy2(p,EX/p.name)
        shutil.copytree(scratch/'published',EX/'publish-preview',dirs_exist_ok=True)
        write(EX/'validation.json',{'structural_checks':'publish','failed_checks':0,'reproducible_assets':True,'svg_xml_valid':True,'packaged_asset_copies':len(assets),'missing_published_images':0,'scope':'One-objective pilot; not full Topic 1.2','model_visual_inspection':'Completed; font fallback in formula caption repaired.','human_visual_review':'Pending before final publication; model inspection is not human approval.','generator':'planning/render_chemistry_visuals_8224.py','publisher':'planning/publish_chemistry_8224.py'})
    print('Visual pipeline: PUBLISH; source and packaged images resolve; hashes reproduce.')


if __name__=='__main__':main()
