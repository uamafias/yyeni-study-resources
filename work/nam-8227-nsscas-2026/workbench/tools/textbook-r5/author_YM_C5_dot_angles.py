"""YM252–255: dot products, between-vector angles and geometric orientation.

Reuse the existing Goldie fixed-source dot/angle operations and independent
vector checker. This is source analysis, not a runtime problem generator.
"""
import json
from author_Goldie_C10_dot_opening import angle, dot
import author_YM_C5_magnitude_units as h
from author_YM_C5_opening import W,SRC,SHA,pp,ev,v,reasoning,fig,figures,compute,expression,equivalent,NOTATION

h.prior.answers.clear(); h.prior.new.clear(); figures.clear(); h.prior.corrections.clear()
answers=h.prior.answers; new=h.prior.new; corrections=h.prior.corrections
MAG=h.MAG; POS=h.POS; DISP='8227:2020:M1:T7:O03:D02'
GEOM='8227:2020:M1:T7:O02:D03'; DOT='8227:2020:M1:T7:O04:D02'
ANGLE='8227:2020:M1:T7:O05:D01'; PERP='8227:2020:M1:T7:O05:D02'
extra=h.extra

def add(kind,number,page,note,parts,representation='text'):
    direct=sorted({d for part in parts for d in part.get('assessed_8227_demand_ids',[])})
    row=h.prior.add(kind,number,page,note,parts,direct)
    row.update(representation=representation,assessed_8227_demand_ids=direct,
      component_demand_ids=sorted({d for part in parts for d in part.get('component_demand_ids',[])}-set(direct)))
    row['mapping_rationale']='Requested scalar products, angles and perpendicularity conclusions are separate outcomes. Computing a dot product inside an angle/perpendicularity solution is a component unless explicitly requested. A spatial target angle requires the correct named rays and orientation, not merely substituting similar components.'
    row['scope_check']={'status':'in-scope','basis':note,'excluded_or_qualified_parts':[],
      'limits_considered':[],'qualifier_applicability_note':'All angle vectors are nonzero. Use the non-reflex between-vector angle in [0,180] degrees and exact signed components. No unrelated calculus/modulus/inverse-function restriction applies.'}
    row['precision_angle_check']={'source':'Example13(a) explicitly uses 1 decimal place; other approximate angle keys here display 1 decimal degree. Try13Q2(f/g) explicitly requests 1 decimal place. Example13(b) is exactly45 degrees. Example15 displays70.5 degrees.',
      'comparison':'Retain exact dot products and positive norms until the final inverse cosine, then compare at the recorded key precision. These are vector angles in degrees, not bearings or arbitrary signed polar directions. Do not infer a question accuracy instruction merely from a rounded key.'}
    for part in parts:
        part.setdefault('given_representation',representation)
        part.setdefault('response_format','numeric')
    return row

def scalar(label,u,w,key,key_page):
    part=dot(label,u,w,key,key_page)
    part['assessed_8227_demand_ids']=[DOT]
    return part

def between(label,u,w,key,key_page,method=None):
    part=angle(label,u,w,key,key_page,method=method)
    part.update(assessed_8227_demand_ids=[ANGLE],component_demand_ids=[DOT,MAG],response_format='numeric')
    return part

def perpendicular(label,u,w,key_page):
    part=dot(label,u,w,'0',key_page,
      'Compute the ORIGINAL signed dot product exactly and establish that it is zero. Both given vectors are nonzero, so this proves a right angle; a zero vector would not establish a defined between-vector angle.')
    part.update(check_mode='show/prove',response_format='proof/show-that',
      assessed_8227_demand_ids=[PERP],component_demand_ids=[DOT])
    return part

add('Example',12,252,'Compute the scalar products of (5,−8) with (1,2), and (−1,3,−2) with (1,1,−6), keeping missing components zero.',[
    scalar('a',['5','-8'],['1','2'],'-11',252),
    scalar('b',['-1','3','-2'],['1','1','-6'],'14',252)])
add('Try-Now-12',1,252,'Compute two dot products, including a zero j component in h=3i−4k.',[
    scalar('a',['3','-7'],['5','1'],'8',617),
    scalar('b',['1','-2','-2'],['3','0','-4'],'11',617)])
part=v('dot','4*5*cos(60*pi/180)','10',617,
    'Use ORIGINAL magnitudes4 and5 and the explicit60 degree angle. Convert to pi/3 for symbolic cosine. No component coordinates are supplied or invented.')
part['assessed_8227_demand_ids']=[DOT]
add('Try-Now-12',2,252,'Find the scalar product from magnitudes4,5 and included vector angle60 degrees.',[part])

parts=[between('a',['1','3'],['1','1'],'26.6',253),
       between('b',['8','-6','-10'],['4','-3','0'],'45',253)]
parts[1]['exact_angle_radians']='pi/4'
row=add('Example',13,253,'Find a2D and a3D between-vector angle through the signed dot product and both positive magnitudes.',parts)
row['source_label_warning']='In part(b), the norm working labels the vectors a and b, although the part defines c and d. The computed sqrt200 and5 belong to c and d; the later formula and final45 degree answer are correct.'

add('Try-Now-13',1,254,'Find the angles between (3,4)/(5,12), and (−1,3,−2)/(1,1,−6), preserving the signed dot products.',[
    between('a',['3','4'],['5','12'],'14.3',617),
    between('b',['-1','3','-2'],['1','1','-6'],'52.6',617)])
r=['9','-2','-6']; s=['2','-6','3']; t=['2','-1','2']
parts=[h.norm('a-r',r,'11',617),h.norm('b-s',s,'7',617),h.norm('c-t',t,'3',617),
       scalar('d-r-dot-s',r,s,'12',617),scalar('e-s-dot-t',s,t,'16',617),
       between('f-angle-r-s',r,s,'81.0',617),between('g-angle-s-t',s,t,'40.4',617)]
for part in parts[-2:]: part['source_precision']='The question explicitly requests 1 decimal place.'
add('Try-Now-13',2,254,'For three given3D vectors, find all three magnitudes, two specified dot products and both corresponding angles to1 decimal place.',parts)
add('Try-Now-13',3,254,'Find the between-vector angle for p=(1,1,3),q=(−2,1,1), without replacing it by a polar direction.',[
    between('angle',['1','1','3'],['-2','1','1'],'75.7',617)])

part=v('a-B','Tuple(-3+2,3+(-3),3+6)','Tuple(-1,0,9)',254,
    'Original A=(−3,3,3) and AB=(2,−3,6) give B=A+AB. Do not add a displacement to the wrong endpoint.')
part.update(assessed_8227_demand_ids=[POS,DISP],component_demand_ids=[])
part2=v('b-q','solve(2*(-4)+(-3)*6+6*q,q)[0]','Rational(13,3)',254,
    'Original AB=(2,−3,6),CD=(−4,6,q). PERPENDICULAR means zero dot product:−8−18+6q=0, giving q13/3. This differs from the earlier PARALLEL task with these same known components; that task required q−12.')
part2.update(assessed_8227_demand_ids=[PERP],component_demand_ids=[DOT])
extra(part2,'substitute-original-zero-dot','2*(-4)+(-3)*6+6*Rational(13,3)','0')
add('Example',14,254,'Recover B from a position and displacement, then determine q13/3 so AB andCD are perpendicular.',[part,part2])
a=['1','7','3']; b=['1','-1','2']; c=['2','1','-3']
add('Try-Now-14',1,254,'Show the same nonzero vector a=(1,7,3) is perpendicular to b=(1,−1,2) and separately to c=(2,1,−3).',[
    perpendicular('a',a,b,617),perpendicular('b',a,c,617)])
part=reasoning('selection','Only e and f are perpendicular to a.',
    'For ORIGINAL a=(−2,4,6), calculate every candidate dot product: with c=(−3,2,1) it is20; with d=(−1,2,3) it is28; with e=(3,3,−1) it is0; with f=(4,−1,2) it is0. All candidates and a are nonzero. Select both zero cases and reject both nonzero cases, rather than stopping after the first valid vector.',617,'matches')
part.update(assessed_8227_demand_ids=[PERP],component_demand_ids=[DOT],
  selected_vectors=['e','f'],candidate_dot_products={'c':20,'d':28,'e':0,'f':0})
extra(part,'all-candidate-dots','Tuple((-2)*(-3)+4*2+6*1,(-2)*(-1)+4*2+6*3,(-2)*3+4*3+6*(-1),(-2)*4+4*(-1)+6*2)','Tuple(20,28,0,0)')
add('Try-Now-14',2,255,'Select every listed vector perpendicular to a=(−2,4,6), checking c,d,e andf.',[part])

part=v('a-CP','Tuple(Rational(3,5)*4,0,Rational(3,5)*(-3))','Tuple(Rational(12,5),0,-Rational(9,5))',255,
    'Original O,A,B,C are on orthogonal axes with OA4,OB12/5,OC3. CA=(4,0,−3) has length5, and pointP is ON CA with CP3, so CP=(3/5)CA=(12/5,0,−9/5). This establishes the requested printed vector, not a coordinate estimate from the picture.')
part.update(check_mode='show/prove',response_format='proof/show-that',
  assessed_8227_demand_ids=[GEOM,DISP],component_demand_ids=[MAG])
part2=v('b-OP','Tuple(Rational(3,5)*4,0,3+Rational(3,5)*(-3))','Tuple(Rational(12,5),0,Rational(6,5))',255,
    'Use OP=OC+CP, including the ORIGINAL height3 offset. CP alone is not the position ofP fromO.')
part2['assessed_8227_demand_ids']=[POS]
part3=v('b-BP','Tuple(Rational(12,5)-0,0-Rational(12,5),Rational(6,5)-0)','Tuple(Rational(12,5),-Rational(12,5),Rational(6,5))',255,
    'Use BP=OP−OB with ORIGINAL B=(0,12/5,0). Keep the negative j component and the arrow direction BtoP.')
part3['assessed_8227_demand_ids']=[DISP]
part4=between('c-angle-BPC',['12/5','-12/5','6/5'],['12/5','0','-9/5'],'70.5',255,
    method='The target angle is BPC. Chosen BP andCP both point INTO the common vertexP, so their dot product gives the same angle as the two OUTGOING raysPB andPC. Their dot is18/5 and norms18/5,3, giving cos(theta)=1/3. Reversing just one arrow without supplementing the angle would instead give109.5 degrees.')
part4['source_vertex_orientation']={'target':'BPC','chosen_vectors':['BP','CP'],
    'both_directed_into':'P','valid_alternative':['PB','PC'],
    'invalid_without_supplement':['BP','PC']}
extra(part4,'exact-cosine','(Rational(12,5)**2+(-Rational(12,5))*0+Rational(6,5)*(-Rational(9,5)))/(Rational(18,5)*3)','Rational(1,3)')
add('Example',15,255,'Orthogonal-axis pyramid OA4,OB2.4,OC3,with P onCA andCP3: establish CP,find OP/BP,then use a scalar product for the actual angle BPC.',[part,part2,part3,part4],representation='diagram')

references=[
    (53,252,'Parallel-vector scalar product property','For nonzero vectors in the SAME direction,theta0 gives a dot b=|a||b|. Opposite parallel vectors give the negative product. The source drawing is the same-direction case, not a universal claim for all parallel vectors.',[DOT],'diagram',None),
    (54,252,'Right-angle and zero-dot-product property','The drawing has nonzero perpendicular vectors and theta90, so their dot product is0. Conversely zero dot product gives an ordinary right angle only when both vectors have a defined nonzero direction.',[PERP,DOT],'diagram',None),
    (55,253,'Between-vector inverse-cosine formula','cos(theta)=(a dot b)/(|a||b|) requires two nonzero vectors. The intended non-reflex angle lies in[0,pi]; retain the signed numerator so obtuse angles are not lost.',[ANGLE],'table',None),
    (56,253,'Printed inverse-cosine calculator sequences','The worked examples illustrate evaluating arccos of the exact dot/norm quotient in degree mode. Hardware button layout and sequencing are source-specific and were not independently operated; do not treat the pictured controls as an app capability or universal device instruction.',[ANGLE],'table','Example:13'),
    (57,255,'Example15 given orthogonal-axis pyramid','O is the trihedral right-angle vertex; OA4,OB12/5,OC3. P lies on CA with CP3, so P=(12/5,0,6/5). AngleBPC uses the rays atP, not an arbitrary projected angle or mixed arrow direction.',[GEOM,DISP,ANGLE],'diagram','Example:15')]
for number,page,label,note,teaches,representation,parent in references:
    fig(number,page,label,note,teaches,representation,[],parent)
    record=figures[-1]
    record['item_id']=record['item_id'].replace('Goldie:C5:','YM:C5:')
    if record['parent_item_id']:
        record['parent_item_id']=record['parent_item_id'].replace('Goldie:C5:','YM:C5:')
    record.update(printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],
      item_kind='given-figure' if number==57 else 'teaching-figure')
    record['mathematical_feature_review']['method']='Read the original vector directions, common vertex, orthogonal axes and exact segment ratios. Recompute scalar products and angle identities separately; a perspective drawing or pictured calculator sequence is not an automated proof.'

pages=[]
for page in range(252,256):
    identifiers=[row['item_id'] for row in answers if row['source_pdf_page']==page]
    identifiers += [row['item_id'] for row in figures if row['pdf_page']==page]
    pages.append({'pdf_page':page,'printed_page':pp(page),'chapter':5,
      'page_status':'items enumerated','item_ids':identifiers,'continuation_item_ids':[],
      'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-19',
      'non_item_content':'All Examples12–15,Try12Q1/2,Try13Q1–3 andTry14Q1/2 outputs, property diagrams, angle formula, calculator guidance and pyramid figure are enumerated over252–255. Intermediate dot/norm work does not become a separately asked response unless the question asks it.',
      'scope_screen':'Scalar product, between-vector angle and perpendicularity are prescribed. All angle vectors are nonzero. Exact signs, source degree units, final display precision and the target geometric vertex are retained.'})

if __name__=='__main__':
    payloads=[('answers-YM-C5-dot-angles.json',{'scope':'Every252–255 explicit scalar-product,angle,perpendicularity and pyramid output.','items':answers}),
      ('census-YM-C5-dot-angles.json',{'book':'YM','book_id':'8227-SRC-017','chapter':5,
       'source_path':SRC,'source_sha256':SHA,'scope':'Complete252–255 page census.',
       'new_items':new+figures,'corrections':corrections,'pages':pages})]
    for name,payload in payloads:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    for row in answers:
        for part in row['subparts']:
            if 'operation' in part:
                expected=part.get('author_expected_normalised',part['printed_key_normalised'])
                assert equivalent(compute(part['operation']),expression(expected)),(row['item_id'],part['subpart'])
            for name,operation in part.get('additional_operations',{}).items():
                assert equivalent(compute(operation),expression(part['additional_operation_expected'][name])),(row['item_id'],part['subpart'],name)
    print(len(answers),'items;',sum(len(row['subparts']) for row in answers),'responses;',len(figures),'references/assets;',len(pages),'pages')
