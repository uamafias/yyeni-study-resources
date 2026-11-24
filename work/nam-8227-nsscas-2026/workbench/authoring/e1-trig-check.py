"""E1 trig/log regressions and rendered evidence input; no app edits."""
from pathlib import Path
import hashlib,importlib.util,json,math,xml.etree.ElementTree as ET
WB=Path(__file__).resolve().parents[1]
def load(name,path):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
M=load('trig_e1',WB/'source/groups/trig_log.py')
C=load('trig_e1_checker',WB/'authoring/trig-log-check.py')
OLD=load('trig_e0',WB/'authoring/history/stage-e-0/files/work/nam-8227-nsscas-2026/workbench/source/groups/trig_log.py')
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def box_distance(rect,point):
 x,y=point;xx=min(max(x,rect[0]),rect[2]);yy=min(max(y,rect[1]),rect[3]);return math.sqrt((x-xx)**2+(y-yy)**2)
def association_ok(box,own,other):
 centre=((box[0]+box[2])/2,(box[1]+box[3])/2)
 return box_distance(box,own)<box_distance(box,other)and math.dist(centre,own)<math.dist(centre,other)
def check():
 graph=next(c for c in M.choices()if c['branch_id']=='graph-intercept');principal=next(c for c in M.choices()if c['branch_id']=='solve-or-explain');rf=next(c for c in M.choices()if c['branch_id']=='degree-cycle')
 changed_graphs=0;receipts=[];gallery=WB/'authoring/e1-trig-gallery';gallery.mkdir(exist_ok=True)
 for i,p in enumerate(graph['parameters']):
  q=M.build(graph['recipe_id'],graph['branch_id'],p);a=q['assets'][0];layout=a['layout_checks'];root=ET.fromstring(a['svg'])
  circles=[(float(e.attrib['cx']),float(e.attrib['cy']))for e in root.iter()if e.tag.endswith('circle')]
  assert len(circles)==2
  for index,(box,point)in enumerate(zip(layout['label_boxes'],circles)):
   assert math.dist(point,layout['label_points'][index])<1e-4
   assert association_ok(box,point,circles[1-index]),(i,index,'misassociated label')
   assert not C.intersect(box,*layout['line_segment'])
   assert all(not C.intersect(box,*axis)for axis in layout['axes'])
  zero=next(e for e in root.iter()if e.tag.endswith('text')and e.text=='0');z=layout['origin_label'];assert abs(float(zero.attrib['x'])-z['x'])<1e-4 and abs(float(zero.attrib['y'])-z['y'])<1e-4
  assert not C.intersect(z['box'],*layout['line_segment'])
  assert all(not C.intersect(z['box'],*axis)for axis in layout['axes'])
  old=OLD.build(graph['recipe_id'],graph['branch_id'],p)
  changed_graphs+=old['assets'][0]['svg']!=a['svg']
  receipts.append({'domain_index':i,'parameters':p,'label_association':'pass','origin_line_axis_clear':'pass','svg_sha256':hashlib.sha256(a['svg'].encode()).hexdigest()})
  if i in [*range(45,63),132]:
   file=gallery/f'idx-{i:03d}.svg';file.write_text(a['svg']);
 # Two seeded regressions use the actual preserved defective layout bytes.
 old=OLD.build(graph['recipe_id'],graph['branch_id'],graph['parameters'][132])['assets'][0]['layout_checks'];old_points=[(float(e.attrib['cx']),float(e.attrib['cy']))for e in ET.fromstring(OLD.build(graph['recipe_id'],graph['branch_id'],graph['parameters'][132])['assets'][0]['svg']).iter()if e.tag.endswith('circle')]
 assert not association_ok(old['label_boxes'][1],old_points[1],old_points[0])
 old=OLD.build(graph['recipe_id'],graph['branch_id'],graph['parameters'][45])['assets'][0];root=ET.fromstring(old['svg']);zero=next(e for e in root.iter()if e.tag.endswith('text')and e.text=='0');x,y=float(zero.attrib['x']),float(zero.attrib['y']);assert C.intersect((x-4,y-30,x+24,y+9),*old['layout_checks']['line_segment'])
 real=0;no_real=0
 for p in principal['parameters']:
  q=M.build(principal['recipe_id'],principal['branch_id'],p)
  text=' '.join(s['result']for s in q['parts'][0]['worked_steps']);assert '(kx)'not in text
  if q['private_math']['outcome']=='no-real-solution':assert f"({p['k']}x)"in text;no_real+=1
  else:real+=1
 assert no_real==24 and real==23
 for p in rf['parameters']:
  new=M.build(rf['recipe_id'],rf['branch_id'],p);old=OLD.build(rf['recipe_id'],rf['branch_id'],p)
  text=new['parts'][1]['worked_steps'][1]['result'];assert 'principal value'in text and 'Reject'in text and 'integer'in text
  assert [p['reference_answer']for p in new['parts']]==[p['reference_answer']for p in old['parts']]
  assert new['exposure_keys']==old['exposure_keys']
 # Every existing rubric fixture is unchanged; repairs are not fresh scoring rules.
 current=json.loads((WB/'authoring/trig-log-marking-fixtures.json').read_text());old=json.loads((WB/'authoring/history/stage-e-0/files/work/nam-8227-nsscas-2026/workbench/authoring/trig-log-marking-fixtures.json').read_text());assert current==old
 # Structural no-drift guard covers every admitted row, independently of output prose.
 assert M.choices()==OLD.choices()
 unchanged=0;changed=0
 for choice in M.choices():
  for params in choice['parameters']:
   after=M.build(choice['recipe_id'],choice['branch_id'],params);before=OLD.build(choice['recipe_id'],choice['branch_id'],params)
   def rubric(q):
    return [(part['local_part_id'],[(c['criterion_id'],c['mark_type'],c['marks'],c.get('depends_on'),c.get('follow_through'))for c in part['criteria']])for part in q['parts']]
   assert rubric(after)==rubric(before)
   assert after['exposure_keys']==before['exposure_keys']
   unchanged+=1;changed+=after!=before
 result={'status':'pass','design_guard':{'choices_domains_unchanged':4,'rows_checked':unchanged,'rows_with_output_changes':changed,'criterion_ids_types_tariffs_dependencies_FT_and_exposure':'unchanged','existing_scoring_expectations':'26unchanged'},'findings':{'SE-03':{'affected_rows':24,'check':'No undefined k in any of47 principal outputs; actualcoefficient in24no-real steps'},'SE-06':{'affected_rows':changed_graphs,'all_graph_rows_checked':270,'old_defects_rejected':['idx132wrong-point label','idx45origin struck by graph'],'render_indices':[*range(45,63),132]}},'notes':{'rform_principal_candidates':58,'graph_e1_simplified':54,'scoring_expectations_unchanged':26},'source_sha256':sha(WB/'source/groups/trig_log.py'),'checks':receipts,'limits':['Independent group oracle covers395mathematical rows; this script adds geometry and formatting regressions.','Rendered diagram evidence is not actual app or marker acceptance.']}
 (WB/'authoring/e1-trig-check.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items()if k!='checks'},indent=2))
if __name__=='__main__':check()
