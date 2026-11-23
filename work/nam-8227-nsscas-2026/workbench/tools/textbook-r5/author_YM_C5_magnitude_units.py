"""YM236–239: norms, unit/parallel directions and prescribed-length positions."""
import json
import author_YM_C5_opening as prior
from author_YM_C5_opening import W,SRC,SHA,pp,ev,v,reasoning,fig,figures,compute,expression,equivalent,NOTATION,GEOM,SCALE
prior.answers.clear();prior.new.clear();figures.clear();prior.corrections.clear()
answers=prior.answers;new=prior.new;corrections=prior.corrections
MAG='8227:2020:M1:T7:O04:D01';UNIT='8227:2020:M1:T7:O03:D01';POS='8227:2020:M1:T7:O03:D03';DISP='8227:2020:M1:T7:O03:D02'
def extra(p,name,expr,key):
 p.setdefault('additional_operations',{})[name]={'kind':'identity','operands':[expr]};p.setdefault('additional_operation_expected',{})[name]=key;return p
def add(kind,n,page,note,parts,direct,new_item=False):
 r=prior.add(kind,n,page,note,parts,direct,new_item=new_item);r['representation']='text'
 r['component_demand_ids']=[MAG]if UNIT in direct else[]
 r['mapping_rationale']='The asked norm,unit vector,or prescribed-length position is direct. Component squaring and incidental scaling are not automatically separate coverage. A unit vector PARALLEL to a given vector may have either orientation; in the SAME DIRECTION only the positive normalisation is admissible.'
 r['scope_check']={'status':'in-scope','basis':note,'excluded_or_qualified_parts':[],'limits_considered':[],'qualifier_applicability_note':'No unrelated QUAL/LIMIT rule applies. Every normalised original is explicitly nonzero; keep real radical components and the original same-direction versus parallel wording.'}
 r['precision_angle_check']={'source':'Exact radicals,fractions and vector components; no angle quantities or requested rounding.','comparison':'Use Euclidean magnitude,not the sum of absolute components. Never normalise zero. Retain exact radicals and coordinate order; a point coordinate tuple and a free vector notation have different meanings.'}
 for p in parts:p.setdefault('given_representation','text');p.setdefault('response_format','symbolic')
 if new_item:
  new[-1].update(scope_check=r['scope_check'],component_demand_ids=r['component_demand_ids'],mapping_rationale=r['mapping_rationale'],representation='text')
 return r
def norm(label,components,key,kp):
 expr='sqrt('+'+'.join(f'({c})**2'for c in components)+')'
 p=v(label,expr,key,kp,'Compute the nonnegative Euclidean norm from the ORIGINAL signed components by squaring,summing and taking the positive square root. Keep the exact radical; the printed key is an independent comparison.');p.update(source_vector_components=components,source_vector_output='magnitude',assessed_8227_demand_ids=[MAG],response_format='numeric');return p
def unit(label,components,key,kp):
 length='sqrt('+'+'.join(f'({c})**2'for c in components)+')'
 expr='Tuple('+','.join(f'({c})/({length})'for c in components)+')'
 p=v(label,expr,key,kp,'Normalise the ORIGINAL nonzero vector by its positive Euclidean norm. The source asks for A unit vector PARALLEL,so the displayed same-direction choice is valid and its negative is also a valid answer. A single valid key choice is complete; absence of its negative is not a key defect.');p.update(assessed_8227_demand_ids=[UNIT],source_normalization_components=components,valid_alternatives=['The negative of the displayed unit vector, because the original wording requires parallel rather than same direction.'])
 if all('sqrt'not in c for c in components):p['source_unit_vector_components']=components
 extra(p,'unit-norm-squared','simplify('+ '+'.join(f'(({c})/({length}))**2'for c in components)+')','1')
 return p
ps=[norm('a',['-2','4'],'2*sqrt(5)',237),norm('b',['1','0'],'1',237),norm('c',['-1','4','-3'],'sqrt(26)',237),norm('d',['0','0','1'],'1',237)]
add('Example',3,237,'Find magnitudes of four original2D/3Dvectors(−2,4),(1,0),(−1,4,−3),(0,0,1); identify the already-unit norms without changing directions.',ps,[MAG])
add('Try-Now',3,237,'Find exact magnitudes of original columns(4,−3),(0,1),(−2,5,−1),(0,1,0),retaining both already-unit cases.',[norm('a',['4','-3'],'5',615),norm('b',['0','1'],'1',615),norm('c',['-2','5','-1'],'sqrt(30)',615),norm('d',['0','1','0'],'1',615)],[MAG])
add('Example',4,238,'Find a unit vector PARALLEL to(2,sqrt5)and(1,−1,−2). Positive-normalised examples are valid; their negatives also meet the original parallel-only wording.',[unit('a',['2','sqrt(5)'],'Tuple(Rational(2,3),sqrt(5)/3)',238),unit('b',['1','-1','-2'],'Tuple(1/sqrt(6),-1/sqrt(6),-2/sqrt(6))',238)],[UNIT],new_item=True)
add('Try-Now',4,238,'Find a unit vector parallel to each of(−3,sqrt7),(−4,−2),(7,−2,−2),(1,5,−3),using actual positive norms4,2sqrt5,sqrt57,sqrt35.',[
 unit('a',['-3','sqrt(7)'],'Tuple(-Rational(3,4),sqrt(7)/4)',615),unit('b',['-4','-2'],'Tuple(-2/sqrt(5),-1/sqrt(5))',615),unit('c',['7','-2','-2'],'Tuple(7/sqrt(57),-2/sqrt(57),-2/sqrt(57))',615),unit('d',['1','5','-3'],'Tuple(1/sqrt(35),5/sqrt(35),-3/sqrt(35))',616)],[UNIT])
def prescribed(label,components,length,key,kp):
 norm='sqrt('+'+'.join(f'({c})**2'for c in components)+')'
 expr='Tuple('+','.join(f'({length})*({c})/({norm})'for c in components)+')'
 p=v(label,expr,key,kp,'The ORIGINAL direction vector is nonzero. Divide it by its exact norm,then multiply by the given POSITIVE target length. Retain SAME direction,so the negative normalisation is not an alternative. The resulting components are the requested position coordinates from O.');p.update(assessed_8227_demand_ids=[UNIT,POS],original_direction_components=components,target_magnitude=length)
 extra(p,'reconstructed-norm-squared','simplify('+ '+'.join(f'(({length})*({c})/({norm}))**2'for c in components)+')',f'({length})**2')
 return p
p=prescribed('R',['8','1','-4'],'2','Tuple(Rational(16,9),Rational(2,9),-Rational(8,9))',239)
add('Example',5,239,'Find coordinates of R with |OR|2 and OR in the SAME direction as8i+j−4k; normalise norm9 then scale to(16/9,2/9,−8/9).',[p],[UNIT,POS])
add('Try-Now-5',1,239,'Find R with |OR|6 in the same direction as2i−3j+6k; norm7 gives(12/7,−18/7,36/7).',[prescribed('R',['2','-3','6'],'6','Tuple(Rational(12,7),-Rational(18,7),Rational(36,7))',616)],[UNIT,POS])
add('Try-Now-5',2,239,'Find A at distance5 from O in the direction of OB for B(2,−1,4); retain the positive direction and exact sqrt21 components.',[prescribed('A',['2','-1','4'],'5','Tuple(10/sqrt(21),-5/sqrt(21),20/sqrt(21))',616)],[UNIT,POS])
p=v('c','Tuple(24*Rational(2,3),24*(-Rational(2,3)),24*(-Rational(1,3)))','Tuple(16,-16,-8)',616,'The source ALREADY gives the unit direction(2/3,−2/3,−1/3). Verify its norm1,then multiply every component by the given magnitude24; no additional renormalisation or sign choice is needed.');p['assessed_8227_demand_ids']=[UNIT,SCALE];extra(p,'given-unit-norm','Rational(2,3)**2+(-Rational(2,3))**2+(-Rational(1,3))**2','1');extra(p,'result-norm-squared','16**2+(-16)**2+(-8)**2','24**2')
add('Try-Now-5',3,239,'Recover c of magnitude24 from supplied unit direction(2/3,−2/3,−1/3),giving16i−16j−8k.',[p],[UNIT,SCALE])

refs=[
 (12,236,'Cartesian component movement arrows','The small component key marks horizontal x and vertical y directions in the2D drawing; the signs follow the shown arrows. This is a2D convention,not a universal promise that the page-vertical axis in every3D sketch has the same name.',[NOTATION],'diagram',[]),
 (13,236,'Position vector and planar components','The OA sketch resolves the arrow into horizontal x and vertical y components,represented by a column. A coordinate point A and displacement OA correspond only after choosing originO.',[NOTATION,POS],'diagram',[]),
 (14,236,'Translated grid displacement LM','The source grid arrow LtoM has3horizontal units and−2vertical units,so LM=(3,−2). It need not start at the origin. Reverse direction negates both components.',[NOTATION,DISP],'graph',[]),
 (15,236,'Spatial position vector OP grid','The source position P(3,2,4) corresponds to vectorOP with the same ordered components and column entries. Its magnitude is not any single displayed component.',[NOTATION,POS],'diagram',[('sqrt(3**2+2**2+4**2)','sqrt(29)')]),
 (16,236,'Two/three-dimensional norm formula boxes','Euclidean magnitudes are sqrt(x²+y²) andsqrt(x²+y²+z²) for orthogonal Cartesian components. The norm is nonnegative; a zero vector has norm0 but cannot supply a unique direction for normalisation.',[MAG],'table',[]),
 (17,237,'Example3 already-unit-vector note','Source vectors(1,0)and(0,0,1) have magnitude1 and are unit vectors already. Unit status depends on norm,not on being two-dimensional or having every component nonzero.',[MAG,UNIT],'table',[('Tuple(sqrt(1**2+0**2),sqrt(0**2+0**2+1**2))','Tuple(1,1)')]),
 (18,237,'Unit direction arrow','The unit arrow keeps the given nonzero direction while its magnitude is1. The diagram does not prescribe a unique drawing origin for a free vector.',[UNIT],'diagram',[]),
 (19,237,'Two/three-dimensional normalisation tables','Divide each component by the SAME positive magnitude. The formula requires a nonzero original vector; it gives the same-direction unit vector. If the task merely asks parallel,either orientation is admissible.',[UNIT],'table',[]),
 (20,238,'Planar Cartesian basis vectors','The2D sketch writes OP=xi+yj,withi andj orthogonal unit basis vectors. The point coordinates(4,3) correspond to4i+3j only for the position vector from O.',[NOTATION,POS],'diagram',[]),
 (21,238,'Spatial Cartesian basis vectors','The3D sketch adds basis vector k in the shown positive z direction. PointQ(3,2,4) corresponds to position vector3i+2j+4k; coordinate order does not change under the drawn perspective.',[NOTATION,POS],'diagram',[]),
 (22,239,'Coordinate point versus vector notation note','Coordinate pairs/triples name points; bold/basis/column notation names the vector from the selected origin. Equivalent basis and column forms retain every signed component.',[NOTATION,POS],'table',[]),
 (23,239,'Equal opposite sides of parallelogram','For consecutive A,B,C,D,the source shows AB=DC andDA=CB. These are equal oriented vectors; AD would have the opposite direction fromDA. Do not identify vectors merely because their lengths agree.',[GEOM],'diagram',[])]
for n,page,label,note,teaches,rep,checks in refs:
 fig(n,page,label,note,teaches,rep,checks,None)
 f=figures[-1];f['item_id']=f['item_id'].replace('Goldie:C5:','YM:C5:');f.update(printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='teaching-figure')
 f['mathematical_feature_review']['method']='Inspect original component signs,arrow endpoints,basis labels and exact vector formulas. Recompute listed features independently of the printed result; manual diagram reading and exact arithmetic do not imply automated image assessment.'
pages=[{'pdf_page':page,'printed_page':pp(page),'chapter':5,'page_status':'items enumerated','item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],'continuation_item_ids':[],'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-19','non_item_content':'All Examples3–5,Try3/4/5Q1–3 and every column/basis/norm/unit/point/equality teaching panel are recorded. Previously uncatalogued Example4 has its own source record. Native239 confirms Example5 final coordinate2/9 is CORRECT; the suspected8/9 reading was false.','scope_screen':'Norm,unit/position-vector and notation demands are within scope. All originals normalised here are nonzero. Exact radicals and same-direction versus parallel distinctions are preserved; no new scope restriction or official award table is invented.'}for page in range(236,240)]

if __name__=='__main__':
 for name,data in [('answers-YM-C5-magnitude-units.json',{'scope':'Every236–239 requested response,including newly recovered Example4.','items':answers}),('census-YM-C5-magnitude-units.json',{'book':'YM','book_id':'8227-SRC-017','chapter':5,'source_path':SRC,'source_sha256':SHA,'scope':'Complete236–239 page census.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if 'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(row['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references/assets;',len(pages),'pages')
