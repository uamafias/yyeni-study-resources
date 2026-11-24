"""E1 visual regression checks on actual emitted SVG and learner text.

The geometric oracle parses the emitted path/text and uses segment orientation,
independent of the placement routine's Liang-Barsky calculation. Conservative
Arial-15 label rectangles include stroke clearance. Raw response recognition is
not implemented or asserted by these author checks.
"""
import hashlib,importlib,importlib.util,json,re
from pathlib import Path
import xml.etree.ElementTree as ET
from build_source import WB,ROOT,load_source,dump
V=importlib.import_module(load_source().__package__+'.groups.visual')
H=WB/'authoring/history/stage-e-0/files'/WB.relative_to(ROOT)/'source/groups/visual.py'
spec=importlib.util.spec_from_file_location('_e1_old_visual',H);OLD=importlib.util.module_from_spec(spec);spec.loader.exec_module(OLD)
OUT=WB/'authoring/visual/e1';OUT.mkdir(parents=True,exist_ok=True)

def crosses(a,b,c,d):
    def orient(p,q,r):return(q[0]-p[0])*(r[1]-p[1])-(q[1]-p[1])*(r[0]-p[0])
    def between(p,q,r):return min(p[0],q[0])-1e-9<=r[0]<=max(p[0],q[0])+1e-9 and min(p[1],q[1])-1e-9<=r[1]<=max(p[1],q[1])+1e-9
    vals=[orient(a,b,c),orient(a,b,d),orient(c,d,a),orient(c,d,b)]
    return (vals[0]*vals[1]<0 and vals[2]*vals[3]<0)or any(abs(z)<1e-9 and between(p,q,r)for z,p,q,r in ((vals[0],a,b,c),(vals[1],a,b,d),(vals[2],c,d,a),(vals[3],c,d,b)))
def hits(segment,box):
    left,top,right,bottom=box;left-=2;top-=2;right+=2;bottom+=2
    a,b=segment
    if any(left<=x<=right and top<=y<=bottom for x,y in (a,b)):return True
    corners=[(left,top),(right,top),(right,bottom),(left,bottom)]
    return any(crosses(a,b,corners[i],corners[(i+1)%4])for i in range(4))
def svg_labels(svg):
    root=ET.fromstring(svg);ns='{http://www.w3.org/2000/svg}'
    path=next(e for e in root.iter(ns+'path')if e.get('stroke')=='#1565c0')
    coords=[tuple(map(float,pair))for pair in re.findall(r'[ML](-?[\d.]+),(-?[\d.]+)',path.get('d'))]
    arms=list(zip(coords,coords[1:]));boxes=[]
    for text in root.iter(ns+'text'):
        label=''.join(text.itertext())
        if not re.fullmatch('[VLRY](?:/[VLRY])*',label):continue
        x,y=float(text.get('x')),float(text.get('y'));width=11*len(label)+4
        anchor=text.get('text-anchor','start');left=x-width/2 if anchor=='middle'else x-width if anchor=='end'else x
        box=(left,y-16,left+width,y+5)
        boxes.append({'text':label,'box':box,'arm_hits':sum(hits(arm,box)for arm in arms)})
    return boxes

def main():
    receipts=[];baseline_hits=[];changed={key:0 for key in ('SE-02-modulus','SE-02-vector','SE-02-trapezium','SE-04','SE-05','SE-07')};image_index=[]
    for choice in V.choices():
        for index,parameters in enumerate(choice['parameters']):
            q=V.build(choice['recipe_id'],choice['branch_id'],parameters);old=OLD.build(choice['recipe_id'],choice['branch_id'],parameters)
            rid=choice['recipe_id'];entry={'recipe_id':rid,'domain_index':index,'parameters':parameters}
            if rid==V.RECIPES[0]:
                labels=svg_labels(q['assets'][0]['svg']);oldlabels=svg_labels(old['assets'][0]['svg'])
                assert labels and not any(x['arm_hits']for x in labels),(index,labels)
                if any(x['arm_hits']for x in oldlabels):baseline_hits.append(index)
                entry['labels']=labels
                assert not re.search(r'(?<!\d)-?1\\lvert',q['parts'][0]['reference_answer'])
                changed['SE-02-modulus']+=q['parts'][0]['reference_answer']!=old['parts'][0]['reference_answer']
                changed['SE-05']+=q['assets'][0]['svg']!=old['assets'][0]['svg']
                name=f'modulus-{index:02d}';(OUT/(name+'.svg')).write_text(q['assets'][0]['svg']);image_index.append({'name':name,'kind':'modulus','domain_index':index})
            elif rid==V.RECIPES[1]:
                b=q['parts'][1];d=q['parts'][3]
                assert 'follow'not in (b['reference_answer']+d['reference_answer']).lower()
                assert not re.search(r'\bown\b',(b['reference_answer']+d['reference_answer']).lower())
                assert 'Unambiguous concavity shorthand for the same own curve can establish the geometry; increasing alone cannot.'in d['criteria'][1]['achievement']
                assert not any(re.search(r'(?<!\d)1\\ln',x)for x in (b['prompt'],b['worked_steps'][1]['result'],b['criteria'][0]['achievement']))
                assert '\\frac{2}{2}'not in q['parts'][0]['worked_steps'][1]['result']
                assert '\\sum_{j=1}^{1}'not in q['parts'][0]['worked_steps'][1]['result']
                assert 'recognise a square'not in json.dumps(q['practice_help'])
                solution=next(a for a in q['assets']if a['role']=='solution');assert solution['part_ids']==['c','d']
                changed['SE-02-trapezium']+=b['prompt']!=old['parts'][1]['prompt']
                changed['SE-04']+=(b['reference_answer']!=old['parts'][1]['reference_answer']and d['reference_answer']!=old['parts'][3]['reference_answer'])
                changed['SE-07']+=d['criteria'][1]['achievement']!=old['parts'][3]['criteria'][1]['achievement']
                name=f'trap-solution-{index:02d}';(OUT/(name+'.svg')).write_text(solution['svg']);image_index.append({'name':name,'kind':'trapezium-solution','domain_index':index})
                if index==0:
                    (OUT/'blank-frame.svg').write_text(q['assets'][0]['svg']);image_index.append({'name':'blank-frame','kind':'blank-frame','domain_index':0})
            else:
                displayed=' '.join(step['result']for step in q['parts'][0]['worked_steps'])
                assert not re.search(r'(?<!\d)1p|(?<!\d)1\(',displayed),displayed
                changed['SE-02-vector']+=displayed!=' '.join(step['result']for step in old['parts'][0]['worked_steps'])
            # IDs, mark types, tariffs and dependency/follow-through objects stay exact.
            for part,oldpart in zip(q['parts'],old['parts']):
                assert part['local_part_id']==oldpart['local_part_id']
                for criterion,oldcriterion in zip(part['criteria'],oldpart['criteria']):
                    assert {k:v for k,v in criterion.items()if k!='achievement'}=={k:v for k,v in oldcriterion.items()if k!='achievement'}
            receipts.append(entry)
    # Seed the old crossed-arm geometry: the actual new check must reject it.
    assert 4 in baseline_hits and 19 in baseline_hits,baseline_hits
    assert any(x['arm_hits']for x in svg_labels(OLD.build(V.RECIPES[0],V.choices()[0]['branch_id'],V.choices()[0]['parameters'][19])['assets'][0]['svg']))
    assert changed=={'SE-02-modulus':16,'SE-02-vector':20,'SE-02-trapezium':8,'SE-04':22,'SE-05':44,'SE-07':22},changed
    result={'status':'pass','scope':'Same-vendor E1 author checks of all96visual instances; not raw marker/app/cross-vendor acceptance','instances':len(receipts),'changed_instance_counts':changed,'all44_label_arm_checks':'pass','baseline_label_arm_collision_indices':baseline_hits,'negative_fixture':'old idx19 crossed-arm SVG detected; old idx4 also detected','structural_marking_fields':'exactly unchanged on all96rows; achievement text repaired only','cases':receipts,'concavity_shorthand_expectation':{'submission':'A correct own sketch of ln(x-1); Underestimate, because ln(x-1) is concave down.','part':'d','expected_gross_marks':2,'out_of':2,'status':'declared approved-rubric expectation, not a recognizer test','basis':'Trapezium WO:79; unchanged DB1 allowance restored'},'source_sha256':hashlib.sha256((WB/'source/groups/visual.py').read_bytes()).hexdigest(),'notes_folded':['Shortened guard-digit decimals and simplified width factors/one interior ordinate','Answer-free second-integrand help no longer names the square','Solution diagram binds c and d; narrow-strip chords dashed']}
    dump(WB/'authoring/e1-visual-check.json',result);dump(OUT/'index.json',image_index)
    print(json.dumps({k:v for k,v in result.items()if k not in ('cases','baseline_label_arm_collision_indices')},indent=2))
if __name__=='__main__':main()
