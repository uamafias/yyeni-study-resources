"""YM342–345: multi-lobe areas,horizontal strips and original branch restrictions."""
import json
import author_YM_C7_opening as h
from author_YM_C7_opening import W,SRC,SHA,pp,ev,v,reasoning,fig,figures,compute,expression,equivalent,extra
from author_Goldie_C5_opening import definite
h.answers.clear();h.new.clear();h.corrections.clear();figures.clear()
answers=h.answers;new=h.new;corrections=h.corrections
AREA='8227:2020:M1:T9:O04:D01';DEF='8227:2020:M1:T9:O03:D01';SKETCH='8227:2020:M1:T3:O05:D01';ROOT='8227:2020:M1:T1:O02:D02';GRAPH='8227:2020:M1:T4:O01:D01';INTERSECT='8227:2020:M1:T4:O02:D01';INT=h.INT
def val(label,expr,key,kp,direct,method,components=None):
 p=v(label,expr,key,kp,method);p.update(assessed_8227_demand_ids=direct,component_demand_ids=components or[],given_representation='text',response_format='symbolic');return p
def proper(label,f,lo,hi,key,kp,source_variable='x'):
 p=definite(label,f,lo,hi,key,kp);p.update(assessed_8227_demand_ids=[AREA],component_demand_ids=[DEF,INT],given_representation='graph',response_format='numeric',source_variable=source_variable,normalised_variable='x',original_integrand=f,original_bounds=[str(lo),str(hi)],units='units^2',printed_key_units='units^2')
 p['method']='Read the actual bounded/shaded region,derive the appropriate strip width and bounds,retain the original inverse BRANCH,and integrate on a continuous real interval. For horizontal strips the SOURCE variable y is consistently renamed x only inside the fixed-source checker. Compare the independently transcribed printed result.'
 return p
def multiarea(label,f,segments,key,kp):
 expr='+'.join(f'({sign})*integrate({f},(x,{lo},{hi}))'for lo,hi,sign in segments)
 p=val(label,expr,key,kp,[AREA],'Find ORIGINAL zeros,check the curve sign on EACH bounded component,and add positive geometric lobe areas. A signed integral or absolute value of the whole signed integral does not substitute for this split.',[DEF,INT])
 p.update(response_format='numeric',original_function=f,original_signed_segments=[dict(lower=str(a),upper=str(b),area_multiplier=s)for a,b,s in segments],units='units^2',printed_key_units='units^2')
 for j,(lo,hi,sign)in enumerate(segments):
  name=f'signed-component-{j+1}';p.setdefault('additional_operations',{})[name]={'kind':'proper-definite-integral','operands':[f,str(lo),str(hi)]}
 return p
def add(kind,n,page,note,parts,powers,rep='graph',new_item=False):
 direct=sorted({d for p in parts for d in p.get('assessed_8227_demand_ids',[])})
 comp=sorted({d for p in parts for d in p.get('component_demand_ids',[])}-set(direct))
 r=h.add(kind,n,page,note,parts,direct,comp,new_item=new_item,powers=powers)
 r.update(representation=rep,sketch_response_required=any(p.get('response_format')=='sketch'for p in parts),mapping_rationale='Requested area,requested sketch,and separately requested intercepts are direct. Strip integration and inverse rearrangement are components of area unless independently requested. Preserve diagram branch restrictions and distinguish actual response requirements from an optional sketch hint.')
 for p in parts:p['given_representation']=rep
 return r

p=val('a-ABC','Tuple(Tuple(-1,0),Tuple(1,0),Tuple(2,0))','Tuple(Tuple(-1,0),Tuple(1,0),Tuple(2,0))',627,[GRAPH],'Read the ordered labelled roots A,B,C from ORIGINAL factored cubic(x+1)(x−1)(x−2),not from a pixel measurement.')
extra(p,'all-root-incidences','Tuple(((x+1)*(x-1)*(x-2)).subs(x,-1),((x+1)*(x-1)*(x-2)).subs(x,1),((x+1)*(x-1)*(x-2)).subs(x,2))','Tuple(0,0,0)')
q=val('b-ABC','Tuple(Tuple(0,(x**2-5*x+4).subs(x,0)),Tuple(solve(x**2-5*x+4,x)[0],0),Tuple(solve(x**2-5*x+4,x)[1],0))','Tuple(Tuple(0,4),Tuple(1,0),Tuple(4,0))',627,[ROOT],'The second graph labels A at its Y-intercept,B/C at left/right roots. Solve the ORIGINAL quadratic and substitute x0 for A;the label roles differ from diagram(a).')
ps=[p,multiarea('a-area','(x+1)*(x-1)*(x-2)',[(-1,1,1),(1,2,-1)],'Rational(37,12)',627),q,multiarea('b-area','x**2-5*x+4',[(0,1,1),(1,4,-1)],'Rational(19,3)',627)]
add('Try-Now-18',1,342,'Two given diagrams ask labelled A/B/C AND total shaded area. The cubic labels three x-roots;the quadratic instead labels one y-intercept and two x-roots. Both shaded sign regions are included.',ps,['3','2','1','0'])
add('Try-Now-18',2,342,'TEXT-given total bounded area of12x(x+1)(2−x). Roots−1,0,2require a sign split;areas5and32sum37. The source suggests sketching as a method,not a separately tariffed response.',[multiarea('area','12*x*(x+1)*(2-x)',[(-1,0,-1),(0,2,1)],'37',627)],['3','2','1'],'text')
add('Try-Now-18',3,342,'TEXT-given area from−1to4for(x−4)(x−2)(x+1),split at internal root2. Add63/4and16/3rather than cancel signed lobes.',[multiarea('area','(x-4)*(x-2)*(x+1)',[(-1,2,1),(2,4,-1)],'Rational(253,12)',627)],['3','2','1','0'],'text')
add('Try-Now-18',4,342,'TEXT-given quadratic area restricted to x1..3,not the complete bounded lobe1..5. The graph hint does not alter those explicit bounds.',[multiarea('area','x**2-6*x+5',[(1,3,-1)],'Rational(16,3)',627)],['2','1','0'],'text')
p=reasoning('sketch','For x>0,y=4/√x is positive,decreasing and convex,with asymptotes x0 andy0;passes(1,4),(4,2). Mark the requested area betweenx1and4.',
 'The ORIGINAL even root is in a denominator,so the real domain isx>0. Derivative−2x^(−3/2)<0 and second derivative3x^(−5/2)>0. The curve approaches+∞asx→0+and0asx→∞. The printed answer graph shows the positive decreasing branch with the two area bounds;it does not justify extending the graph tox≤0.',627,'sketch')
p.update(assessed_8227_demand_ids=[SKETCH],component_demand_ids=[],response_format='sketch',credited_features=['Positive decreasing convex branch onx>0','Vertical asymptotex0 and horizontal asymptotey0','Points(1,4),(4,2)','Area boundariesx1,x4'],criteria_basis='Features derived from original equation and compared with printed response sketch;no official award table is supplied.')
extra(p,'endpoint-ordinates','Tuple((4/sqrt(x)).subs(x,1),(4/sqrt(x)).subs(x,4))','Tuple(4,2)')
extra(p,'shape-at-positive-sample','Tuple(diff(4/sqrt(x),x).subs(x,1),diff(4/sqrt(x),x,2).subs(x,1))','Tuple(-2,3)')
add('Try-Now-18',5,342,'Explicit SKETCH-and-area question for4/√x between1and4. Keep its two requested outputs distinct;the source key has an actual response sketch.',[p,proper('area','4/sqrt(x)',1,4,'8',627)],['−1/2'],'text')
p=proper('area','sqrt(x)',1,3,'2.80',343,'y')
p['operation']={'kind':'rounded','operands':['integrate(sqrt(x),(x,1,3))'],'significant_figures':3}
p['additional_operations']={'exact-area':{'kind':'proper-definite-integral','operands':['sqrt(x)','1','3']}}
p['additional_operation_expected']={'exact-area':'2*sqrt(3)-Rational(2,3)'}
p['source_precision_note']='The inline worked solution chooses3significant figures;the original prompt simply asks area. Record this source convention without inventing a universal rounding rule.'
add('Example',19,343,'Right-hand branch of y=x²,between y1and3and the y-axis. The diagram selectsx=+√y,not the negative branch. Exact area2√3−2/3is displayed2.80to3sf.',[p],['1/2'])
add('Try-Now-19',1,343,'Given x=y(3−y),find the positive region between the curve and y-axis on y0..3. SOURCE y is the strip variable.',[proper('area','x*(3-x)',0,3,'Rational(9,2)',627,'y')],['2','1'])
add('Try-Now-19',2,343,'Given y=x³,find the y-axis region between horizontal lines y8and27. Inversex=realcuberooty;all actual bounds are positive. This missing numbered item is recovered.',[proper('area','x**Rational(1,3)',8,27,'Rational(195,4)',627,'y')],['1/3'],new_item=True)
add('Try-Now-19',3,343,'Given y=(x−2)³,shaded with y-axis between y1and8. Correct horizontal width is realcuberooty+2;the translation contributes14to the area.',[proper('area','x**Rational(1,3)+2',1,8,'Rational(101,4)',627,'y')],['1/3','0'])
r=add('Example',20,344,'Same geometric region and same area asExample16,now demonstrated with horizontal strips x=4−y²,y0..2. It is an alternative representation/method,not another distinct problem type.',[proper('area','4-x**2',0,2,'Rational(16,3)',344,'y')],['2','0'])
r.update(source_duplicate_of='8227:TB:YM:C7:Example:16',duplicate_basis='The source explicitly identifies the SAME graph/region and same requested numerical area. Horizontal instead of vertical strips supplies an alternative method/representation,not extra problem-type breadth.')
r=add('Try-Now-20',1,344,'Repeated y=x³/y-axis area between y8and27,identical givens and requested result toTry19Q2;the drawing style differs.',[proper('area','x**Rational(1,3)',8,27,'Rational(195,4)',627,'y')],['1/3'])
r.update(source_duplicate_of='8227:TB:YM:C7:Try-Now-19:2',duplicate_basis='Same curve,boundaries and requested area asTry19Q2. Repeated source occurrence,not extra problem-type breadth.')
p=reasoning('area','The literal y=√(2x−1)has no negative-y branch,so the stated boundaries do not enclose the displayed region. The key3is the area for the DIFFERENT full parabola y²=2x−1 betweeny−1and2.',
 'The principal square root requires y≥0. Squaring gives x=(y²+1)/2 ONLY with that condition retained. The diagram wrongly includes y<0;at its lower endpoint(1,−1),the literal equation gives+1,not−1. Integrating(y²+1)/2from−1to2gives3for the full parabola,not for the stated square-root branch. If the lower boundary were changed to0,the actual square-root branch would bound area7/3;that is a different question,not a silent correction.',627,'key wrong')
p.update(assessed_8227_demand_ids=[],component_demand_ids=[AREA],response_format='numeric',given_representation='graph',printed_key_normalised='3',source_interpretation='Defective original equation/diagram pair. Retain internal diagnosis and intended full-parabola interpretation separately;no valid literal area coverage claimed.')
extra(p,'source-intended-parabola-area','integrate((x**2+1)/2,(x,-1,2))','3')
extra(p,'actual-branch-with-CHANGED-lower-bound','integrate((x**2+1)/2,(x,0,2))','Rational(7,3)')
extra(p,'false-negative-branch-point','-1-sqrt(2*1-1)','-2')
r=add('Try-Now-20',2,344,'The source labels the curve y=√(2x−1)but draws/shades a full sideways parabola including negativey. Its finite key3drops the original y≥0condition.',[p],['2','0'])
r['scope_check'].update(status='in-scope-parts-only',excluded_or_qualified_parts=['No valid literal bounded-region exemplar:source equation and negative-y diagram conflict.'])
r.update(evidence_role='prerequisite/supporting defective source diagnosis;no valid directly assessed coverage.',source_domain_caution='Do not replace a principal square-root branch with its squared equation without retaining y≥0.')
p=proper('area','-x**2+7*x-6',1,6,'Rational(125,6)',345)
p['method']='Solve ORIGINAL curve-line intersections −x²+8x−5=x+1 to get1,6. The parabola minus the line is(x−1)(6−x)≥0between them. Integrate this UPPER-minus-LOWER vertical width. No absolute-value shortcut or subtraction in the wrong order is allowed.'
p['component_demand_ids'].append(INTERSECT)
extra(p,'intersection-roots','FiniteSet(*solve((-x**2+8*x-5)-(x+1),x))','FiniteSet(1,6)')
add('Example',21,345,'Area between parabola−x²+8x−5and line x+1:derive their intersections1,6,then integrate the nonnegative difference,not either individual axis area alone.',[p],['2','1','0'])

refs=[
 (28,342,'Try18Q1(a) given cubic and both shaded lobes','y=(x+1)(x−1)(x−2);A,B,Care x-roots−1,1,2. Both positive−1..1andnegative1..2regions are shaded.',[AREA],'graph','Try-Now-18:1','given-figure'),
 (29,342,'Try18Q1(b) given quadratic and differently assigned labels','y=x²−5x+4;A=(0,4),B=(1,0),C=(4,0). Shading includes positive0..1andnegative1..4.',[AREA],'graph','Try-Now-18:1','given-figure'),
 (31,342,'Horizontal-strip area illustration','Right-hand branch y=x²with0<a<b on the Y-axis;area lies between y-axis andx=√y. Horizontal strip width is a coordinatex,not the ordinatey.',[AREA],'graph',None,'teaching-figure'),
 (32,342,'Nonnegative horizontal-width formula','For x=f(y)≥0and ordered compatible y-boundaries,the area is∫xdy. Inverse selection retains original branch and real-domain restrictions.',[AREA],'table',None,'teaching-figure'),
 (33,343,'Example19 given right branch and y-bounds','Right branch y=x²,y1andy3,y-axis,shaded positive horizontal widths. Diagram rules outx=−√y.',[AREA],'graph','Example:19','given-figure'),
 (34,343,'Try19Q1 given sideways quadratic','x=y(3−y),meetsy-axis at0,3,bulges right;the enclosed shaded area uses horizontal strips0≤y≤3.',[AREA],'graph','Try-Now-19:1','given-figure'),
 (35,343,'Try19Q2 given cubic and horizontal boundaries','y=x³withhorizontal boundaries8,27;shading fromy-axis to the positive cube-root inverse.',[AREA],'graph','Try-Now-19:2','given-figure'),
 (36,343,'Try19Q3 shifted cubic and horizontal shading','y=(x−2)³,y1andy8;right boundaryx=cuberooty+2. The whole horizontal translation contributes to width.',[AREA],'graph','Try-Now-19:3','given-figure'),
 (37,344,'Example20 given square-root region','y=√(4−x),bothcoordinateaxes,regionbounded0≤y≤2,0≤x≤4−y². Same actual region asExample16;the source demonstrates horizontal strips.',[AREA],'graph','Example:20','given-figure'),
 (38,344,'Try20Q1 repeated cubic region','Same y=x³,y8and27 region asTry19Q2;redrawn sketch does not create an additional type.',[AREA],'graph','Try-Now-20:1','given-figure'),
 (39,344,'Try20Q2 DEFECTIVE negative square-root branch','Caption y=√(2x−1)requiresy≥0,but the given curve/shading extends down to y−1. Intended full parabola and actual branch are distinct;the equation/diagram pair cannot be reused as valid.',[AREA],'graph','Try-Now-20:2','given-figure'),
 (40,345,'General curve-line shaded interval','Uppercurve f,lowerline g,intersectionsA/Bwithabscissasa,b. Vertical width f−gmustremainnonnegative on the chosen connected interval.',[AREA],'graph',None,'teaching-figure'),
 (41,345,'Upper-minus-lower area formula','Area=∫a^b(f−g)dx wheref≥g;the source calls them exterior/interior,but the operative relationship is upper/lower. If ordering changes,split at actual intersections.',[AREA],'table',None,'teaching-figure'),
 (42,345,'Example21 given parabola/line region','y=−x²+8x−5andy=x+1;the parabola is upper on their bounded interval. The given sketch does not label intersection abscissas.',[AREA],'graph','Example:21','given-figure'),
 (43,345,'Example21 SOLUTION sketch with derived boundaries','The worked illustration adds x1and6after solving intersections. These are solution labels,not givens in the original graph.',[AREA],'graph','Example:21','teaching-figure')]
for n,page,label,note,teaches,rep,parent,kind in refs:
 fig(n,page,label,note,teaches,rep,[],parent);r=figures[-1]
 r.update(item_id=f'8227:TB:YM:C7:Teaching-figure:{n}',printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind=kind,parent_item_id='8227:TB:YM:C7:'+parent if parent else None)
 r['mathematical_feature_review']['method']='Read original labels,shading,inverse branch and axis orientation;recompute parent areas from the original equations. Distinguish source givens,response sketches,and worked-solution diagrams. The negative-y square-root conflict is retained as a defect,not silently corrected.'
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=7,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-19',non_item_content='Every Try18Q1–5,Example19/Try19Q1–3,Example20/Try20Q1–2,curve-line reference andExample21 enumerated. Try19Q2is newly recovered;two repeated regions are explicitly linked. Optional sketch hint is distinguished from Q5explicit sketch instruction.',scope_screen='Areas with correct sign/lobe/axis/inverse choices. Try20Q2is defective because principal-root equation conflicts with its negative-y diagram. No capability hold is used.')for page in range(342,346)]
h.pages=pages
if __name__=='__main__':h.save('horizontal-areas','Complete rendered342–345census;original domains and diagram/solution roles retained.')
