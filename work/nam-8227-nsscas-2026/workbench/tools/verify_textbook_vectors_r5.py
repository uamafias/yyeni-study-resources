"""Independent Python-math/Fraction checks for fixed-source vector operands."""
import argparse,json,math
from fractions import Fraction
from analysis_sources import WB,ROOT,write
from verify_textbook_answers_r5 import compute,expression

def source_round(result,op):
 if op['kind']=='rounded':
  if 'decimal_places'in op:return round(result,op['decimal_places'])
  places=op['significant_figures']-1-int(math.floor(math.log10(abs(result))))if result else 0
  return round(result,places)
 return result

def independent_unit(components):
 vector=[float(Fraction(v))for v in components];norm=math.hypot(*vector)
 assert norm>0,'zero vector cannot be normalised'
 return tuple(v/norm for v in vector)

def independent_pair_angle(vectors):
 u,v=[[float(Fraction(z))for z in row]for row in vectors]
 assert len(u)==len(v)and len(u)>=2
 nu,nv=math.hypot(*u),math.hypot(*v)
 assert nu>0 and nv>0,'zero vector has no between-vector angle'
 # Chord/sum geometry gives a method independent of the source dot/acos.
 minus=math.hypot(*(a/nu-b/nv for a,b in zip(u,v)))
 plus=math.hypot(*(a/nu+b/nv for a,b in zip(u,v)))
 return 2*math.atan2(minus,plus)

def check_pair_angle(part,actual):
 angle=independent_pair_angle(part['source_angle_vectors'])
 result=angle if part.get('source_angle_unit')=='radian'else math.degrees(angle)
 target=source_round(result,part['operation'])
 assert math.isclose(actual,target,abs_tol=1e-12,rel_tol=1e-12),('independent between-vector angle discrepancy',actual,target)
 return target

def independent_value(part):
 vector=[float(Fraction(v))for v in part['source_vector_components']]
 if part['source_vector_output']=='magnitude':result=math.hypot(*vector)
 else:
  assert len(vector)==2 and any(vector),'zero vector has no direction'
  result=math.degrees(math.atan2(vector[1],vector[0]))
 return source_round(result,part['operation'])

def check_scalar(part,actual):
 target=independent_value(part)
 assert math.isfinite(actual)and math.isclose(actual,target,rel_tol=1e-12,abs_tol=1e-12),('independent vector discrepancy',part['source_vector_components'],part['source_vector_output'],actual,target)
 return target

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--negative-fixture',choices=['naive-atan-direction','zero-vector-angle','L1-instead-of-magnitude','zero-unit-vector','zero-pair-angle','pair-angle-supplement']);args=parser.parse_args()
 if args.negative_fixture:
  if args.negative_fixture=='zero-pair-angle':
   independent_pair_angle([['0','0','0'],['1','0','0']])
  elif args.negative_fixture=='pair-angle-supplement':
   check_pair_angle({'source_angle_vectors':[['3','4'],['5','-12']],'operation':{'kind':'rounded','decimal_places':1}},59.5)
  elif args.negative_fixture=='zero-unit-vector':
   independent_unit(['0','0','0'])
  elif args.negative_fixture=='zero-vector-angle':
   independent_value({'source_vector_components':['0','0'],'source_vector_output':'direction-degrees','operation':{'kind':'identity'}})
  elif args.negative_fixture=='naive-atan-direction':
   check_scalar({'source_vector_components':['-4','-4'],'source_vector_output':'direction-degrees','operation':{'kind':'identity'}},45.0)
  else:check_scalar({'source_vector_components':['4','2'],'source_vector_output':'magnitude','operation':{'kind':'identity'}},6.0)
  raise AssertionError('seeded vector fixture unexpectedly passed')
 scalar=[];arrows=[];units=[];perimeters=[];named=[];angles=[];dots=[]
 for path in sorted((WB/'tools/textbook-r5').glob('answers-*.json')):
  for item in json.loads(path.read_text())['items']:
   for part in item['subparts']:
    if 'source_vector_components'in part:
     actual=float(compute(part['operation']));target=check_scalar(part,actual)
     scalar.append({'item_id':item['item_id'],'subpart':part['subpart'],'source_vector_components':part['source_vector_components'],'output':part['source_vector_output'],'independent_math_value':target,'CAS_value_after_source_rounding':actual})
    if 'source_angle_vectors'in part:
     actual=float(compute(part['operation']));target=check_pair_angle(part,actual)
     angles.append({'item_id':item['item_id'],'subpart':part['subpart'],'source_vectors':part['source_angle_vectors'],'unit':part.get('source_angle_unit','degree'),'independent_chord_angle_after_source_rounding':target,'CAS_dot_angle':actual})
    if 'source_cosine_vectors'in part:
     independent=math.cos(independent_pair_angle(part['source_cosine_vectors']));actual=float(compute(part['operation']))
     assert math.isclose(independent,actual,abs_tol=1e-12),('independent between-vector cosine discrepancy',item['item_id'],part['subpart'])
     angles.append({'item_id':item['item_id'],'subpart':part['subpart'],'source_vectors':part['source_cosine_vectors'],'output':'cosine','independent_chord_cosine':independent,'CAS_cosine':actual})
    if 'source_dot_vectors'in part:
     u,v=[[float(Fraction(z))for z in row]for row in part['source_dot_vectors']]
     independent=(math.hypot(*u)**2+math.hypot(*v)**2-math.hypot(*(a-b for a,b in zip(u,v)))**2)/2
     actual=float(compute(part['operation']));assert math.isclose(actual,independent,rel_tol=1e-12,abs_tol=1e-12),('independent norm-identity dot discrepancy',item['item_id'],part['subpart'])
     dots.append({'item_id':item['item_id'],'subpart':part['subpart'],'source_vectors':part['source_dot_vectors'],'independent_norm_identity':independent,'CAS_dot':actual})
    if 'source_unit_vector_components'in part:
     expected=independent_unit(part['source_unit_vector_components']);actual=[float(v)for v in compute(part['operation'])]
     assert len(actual)==len(expected)and all(math.isclose(a,b,abs_tol=1e-12)for a,b in zip(actual,expected)),('independent unit vector discrepancy',item['item_id'],part['subpart'])
     units.append({'item_id':item['item_id'],'subpart':part['subpart'],'original_components':part['source_unit_vector_components'],'independent_unit':expected,'CAS_unit':actual})
    if 'source_perimeter_points'in part:
     points=[[float(Fraction(v))for v in row]for row in part['source_perimeter_points']]
     expected=source_round(math.fsum(math.dist(a,b)for a,b in zip(points,points[1:]+points[:1])),part['operation'])
     actual=float(compute(part['operation']));assert math.isclose(actual,expected,abs_tol=1e-12),('independent perimeter discrepancy',item['item_id'],part['subpart'])
     perimeters.append({'item_id':item['item_id'],'subpart':part['subpart'],'points':part['source_perimeter_points'],'independent_perimeter_after_source_rounding':expected,'CAS_value':actual})
    if part.get('operation',{}).get('kind')in['named-point-location','named-point-displacements']:
     op=part['operation'];target=tuple(Fraction(str(v))for v in expression(op['operands'][0]));points={name:tuple(Fraction(v)for v in row)for name,row in op['points'].items()}
     if op['kind']=='named-point-location':expected={name for name,point in points.items()if point==target}
     else:expected={tail+head for tail,a in points.items()for head,b in points.items()if tuple(v-u for u,v in zip(a,b))==target}
     actual={str(v)for v in compute(op)};assert actual==expected,('independent named-point discrepancy',item['item_id'],part['subpart'],actual,expected)
     named.append({'item_id':item['item_id'],'subpart':part['subpart'],'kind':op['kind'],'independent_Fraction_matches':sorted(expected),'CAS_matches':sorted(actual),'named_points':len(points)})
    if 'source_arrow_tail'in part:
     tail=part['source_arrow_tail'];head=part['source_arrow_head'];assert len(tail)==len(head)
     wanted=[Fraction(str(b))-Fraction(str(a))for a,b in zip(tail,head)]
     actual=list(compute(part['operation']));assert len(actual)==len(wanted)
     assert all(Fraction(str(a))==b for a,b in zip(actual,wanted)),('independent directed-endpoint discrepancy',item['item_id'],part['subpart'])
     arrows.append({'item_id':item['item_id'],'subpart':part['subpart'],'tail':tail,'head':head,'independent_fraction_displacement':[str(v)for v in wanted]})
 assert scalar and arrows,'source vector inputs missing'
 write(WB/'checks/r5/vector-independent-checks.json',{'status':'author independent numeric/endpoint checks;cross-vendor acceptance pending','scalar_checks':scalar,'directed_endpoint_checks':arrows,'unit_vector_checks':units,'perimeter_checks':perimeters,'named_point_checks':named,'between_vector_angle_checks':angles,'dot_product_checks':dots,'methods':'Python math.hypot and atan2 versus symbolic source operations;Fraction endpoint subtraction versus CAS tuples. Rounding follows the original source instruction.','limits':'These checks do not validate source-image transcription,all future vector parameters,a sketch-marker implementation or full scalar-product angle coverage.'})
 print(len(scalar),'independent magnitude/direction checks;',len(arrows),'directed endpoint checks;',len(units),'units;',len(perimeters),'perimeters;',len(named),'named-point checks;',len(angles),'pair angles;',len(dots),'dots')
if __name__=='__main__':main()
