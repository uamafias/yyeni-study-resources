"""YM368–369: Exercise7 Q7–11 and the first explicitly exam-style example."""
import json
import author_YM_C7_opening as h
from author_YM_C7_opening import W,SRC,SHA,pp,v,fig,figures,compute,expression,equivalent,extra
from author_YM_C7_volume_opening import ev
h.answers.clear();h.new.clear();h.corrections.clear();figures.clear()
answers=h.answers;new=h.new;corrections=h.corrections
MOTION='8227:2020:M1:T9:O04:D03';DM='8227:2020:M1:T8:O03:D04';POINT='8227:2020:M1:T8:O04:D01';NATURE='8227:2020:M1:T8:O04:D02';GRAD='8227:2020:M1:T8:O01:D01';TANGENT='8227:2020:M1:T8:O03:D01';INTERSECT='8227:2020:M1:T4:O02:D01';CURVE='8227:2020:M1:T9:O02:D02';CONST='8227:2020:M1:T9:O02:D01';AREA='8227:2020:M1:T9:O04:D01';VOL='8227:2020:M1:T9:O04:D02';DEF='8227:2020:M1:T9:O03:D01';INT=h.INT
def val(label,expr,key,kp,direct,method,components=None,units=None,show=False):
 p=v(label,expr,key,kp,method);p.update(assessed_8227_demand_ids=direct,component_demand_ids=components or [],given_representation='text',response_format='proof/show-that' if show else 'symbolic')
 if units:p.update(units=units,printed_key_units=units)
 if show:p['check_mode']='show/prove'
 return p
def add(kind,n,page,note,parts,powers,rep='text'):
 direct=sorted({d for p in parts for d in p.get('assessed_8227_demand_ids',[])})
 comp=sorted({d for p in parts for d in p.get('component_demand_ids',[])}-set(direct))
 r=h.add(kind,n,page,note,parts,direct,comp,powers=powers)
 r.update(representation=rep,mapping_rationale='Retain each requested result, the actual interval and original branch. Total distance across a reversal requires a sign split. An equation solved after squaring or a root substitution must be checked in the original. Symbolic motion parameters remain positive where the source states that condition.')
 for p in parts:p['given_representation']=rep
 if kind=='Example' and n==40:
  r.update(exam_style=True,exam_style_basis='Source section7.3 explicitly says Exam-Style Questions on PDF369. This is textbook-labelled practice,not an official examination attribution.')
 return r
ps=[val('a-v3','(integrate(5-6*t,t)+2).subs(t,3)','-10',630,[MOTION],'Integrate ORIGINAL acceleration5−6t and impose v0=2. The recovered velocity is5t−3t²+2,whose value at3 is−10m/s. Preserve its sign.',[INT,CONST],'m/s'),val('b-rest','solveset(5*t-3*t**2+2,t,domain=Interval.open(0,oo))','FiniteSet(2)',630,[MOTION],'The SAME recovered velocity has roots−1/3 and2;the requested positive time is2s.',[INT],'s'),val('c-total-distance','integrate(5*t-3*t**2+2,(t,0,2))-integrate(5*t-3*t**2+2,(t,2,3))','Rational(3,2)',630,[MOTION],'Velocity changes from positive to negative at2 INSIDE the requested0..3 interval. Add positive distances6 and9/2,giving21/2m. The printed key instead integrates signed velocity over the whole interval to get3/2m,which is displacement,not total distance.',[INT],'m')]
ps[-1].update(author_expected_normalised='Rational(21,2)',source_interpretation='Confirmed source key gives signed displacement3/2m for a TOTAL DISTANCE request. Native key read;keep the actual positive distance distinct.')
ps[-1]['additional_operations']={'first-signed':{'kind':'proper-definite-integral','operands':['5*x-3*x**2+2','0','2']},'second-signed':{'kind':'proper-definite-integral','operands':['5*x-3*x**2+2','2','3']},'whole-signed':{'kind':'proper-definite-integral','operands':['5*x-3*x**2+2','0','3']}}
ps[-1]['additional_operation_expected']={'first-signed':'6','second-signed':'-Rational(9,2)','whole-signed':'Rational(3,2)'}
r=add('Exercise-7',7,368,'Source Intermediate Level:recover velocity,find positive rest time,and total distance across a direction reversal. The key confuses signed displacement with total distance.',ps,['1','2','0']);r['connected_part_structure']='The rest time2 from(b) is the required integration split in(c).'
p=val('a-Kx','solve(3*x-x**2,x)[1]**2','9',630,[INTERSECT],'Set u=√(original x),u≥0. ORIGINAL3√x=x becomes3u=u²,with u0 or3. K is the non-origin intersection,so originalx=u²=9.')
p['source_root_basis']={'checker x':'sqrt(original x),nonnegative'}
extra(p,'original-intersection','3*sqrt(9)-9','0')
q=val('b-area','integrate(3*sqrt(x)-x,(x,0,9))','Rational(27,2)',630,[AREA],'The given shaded lens is between3√x andx from0 toK9. The root curve is upper there. Integrate the difference,not either separate axis area.',[DEF,INT],'units^2')
add('Exercise-7',8,368,'Source Intermediate Level:given root curve/line lens,identify the non-origin intersection and its area.',[p,q],['1/2','1'],'graph')
p=val('a-Ax','solve(3*x**2+x-2,x)[1]**2','Rational(4,9)',630,[GRAD],'Let u=√(original x)>0. ORIGINAL3√x−2/√x=−1 gives3u²+u−2=0,with candidatesu2/3 and−1. Reject negativeu BEFORE squaring;the only admissible originalx is4/9.')
p['source_root_basis']={'checker x':'sqrt(original x)>0'}
extra(p,'original-candidate-gradients','Tuple(3*sqrt(Rational(4,9))-2/sqrt(Rational(4,9)),3*sqrt(1)-2/sqrt(1))','Tuple(-1,1)')
q=val('b-Ay','(2*x**Rational(3,2)-4*sqrt(x)+2).subs(x,Rational(4,9))','-Rational(2,27)',630,[CURVE,CONST],'Integrate ORIGINAL derivative3√x−2/√x to2x^(3/2)−4√x+c. Actual point(4,10) fixes c2. Evaluate that SAME fixed curve at A_x4/9 to get−2/27.',[INT])
extra(q,'given-point-and-derivative','Tuple((2*x**Rational(3,2)-4*sqrt(x)+2).subs(x,4),simplify(diff(2*x**Rational(3,2)-4*sqrt(x)+2,x)-(3*sqrt(x)-2/sqrt(x))))','Tuple(10,0)')
r=add('Exercise-7',9,368,'Source Intermediate Level:unique point with gradient−1,then its ordinate using a separate curve point. Reject the negative square-root substitution candidate.',[p,q],['1/2','−1/2']);r['original_domain']='Original derivative requires x>0.'
p=val('a-BC','Tuple(Tuple(0,sqrt(1+2*0)),Tuple(solve(1+2*x-3**2,x)[0],3))','Tuple(Tuple(0,1),Tuple(4,3))',630,[INTERSECT],'Use ORIGINAL y=√(1+2x). B is atx0;C has stated y3,so its x-coordinate is4. Both lie on the positive-root branch.')
q=val('b-normal','3-(1/diff(sqrt(1+2*x),x).subs(x,4))*(x-4)','-3*x+15',630,[TANGENT],'Tangent slope atC is1/3,so normal slope−3. Use ORIGINAL pointC(4,3),not the y-intercept B.')
t=val('c-volume','pi*integrate(((1-x**2)/2)**2,(x,0,1))','2*pi/15',630,[VOL],'The GIVEN shaded region lies LEFT of the y-axis betweenA(−1/2,0),B(0,1) and the axes. SOURCE y0..1 is renamed checkerx. Original inverse coordinate=(y²−1)/2≤0;radius is its absolute distance(1−y²)/2. Square that radius and integrateπdy.',[DEF,INT],'units^3')
t.update(rotation_axis='y',source_variable='y',normalised_variable='x')
add('Exercise-7',10,368,'Source Intermediate Level:root-curve coordinates,normal atC,and y-axis rotation of a different LEFT-of-axis shaded region. The normal is not the rotation boundary.',[p,q,t],['4','2','0'],'graph')
ps=[val('a-acceleration','diff(t*(k**2-t**2),t)','k**2-3*t**2',630,[DM],'Differentiate ORIGINAL v=t(k²−t²),with k a POSITIVE constant.',units='m/s^2'),val('b-max-v','(t*(k**2-t**2)).subs(t,k/sqrt(3))','2*k**3/(3*sqrt(3))',630,[POINT,NATURE],'On the journey0≤t≤k,velocity is nonnegative. Acceleration0 gives t=k/√3 inside that interval;the derivative of acceleration there is negative. Endpoint velocities0 confirm the maximum2k³/(3√3).',[DM],'m/s',True),val('c-i-time','solve(k-t,t)[0]','k',630,[DM],'Factor ORIGINAL velocity t(k−t)(k+t). Since k>0,the next positive rest time after0 is k;root−k is outside the journey.',units='s'),val('c-ii-distance','integrate(t*(k**2-t**2),(t,0,k))','k**4/4',630,[MOTION],'For k>0 and0≤t≤k,ORIGINAL velocity is nonnegative. Therefore distanceAZ equals its integral k⁴/4. The positivity condition makes this a valid distance identity.',[INT],'m',True)]
extra(ps[1],'maximum-curvature','diff(t*(k**2-t**2),t,2).subs(t,k/sqrt(3))','-2*sqrt(3)*k')
extra(ps[2],'factorisation-and-next-rest','Tuple(expand(t*(k-t)*(k+t)-t*(k**2-t**2)),(t*(k**2-t**2)).subs(t,k))','Tuple(0,0)')
r=add('Exercise-7',11,368,'Source Advanced Level:positive-parameter rest-to-rest motion,acceleration,shown maximum velocity,journey time,and shown distance. The source level is not a Bloom label.',ps,['2','3','1']);r.update(original_domain='k>0;journey0≤t≤k.',connected_part_structure='Acceleration in(a) supplies the hence maximum in(b);next rest time in(c)(i) bounds the distance proof in(ii).')
p=val('a-normal-proof','diff(sqrt(1+4*x),x).subs(x,6)*((0-5)/(8-6))','-1',369,[TANGENT],'Differentiate ORIGINAL y=√(1+4x):tangent atP(6,5) has slope2/5. The GIVEN line throughP,Q(8,0) has slope−5/2. Their product−1,withP on both,establishes PQ is the normal. A reciprocal-slope assertion without incidence is incomplete.',show=True)
extra(p,'curve-and-line-incidence','Tuple(sqrt(1+4*6)-5,(20-5*x/2).subs(x,6)-5,(20-5*x/2).subs(x,8))','Tuple(0,0,0)')
q=val('b-volume','pi*integrate(1+4*x,(x,0,6))+pi*integrate((20-5*x/2)**2,(x,6,8))','284*pi/3',369,[VOL],'The shaded solid rotates the LOWER-envelope region to the x-axis:root-curve discs0..6 plus line/cone discs6..8. Use the SAME given points and normal. Equivalent cone volume(1/3)π5²*2 adds to78π,giving284π/3. The source requires all necessary working and an exact result.',[DEF,INT],'units^3')
q['required_method']='Showing all necessary working;exact volume (source textbook condition).'
q['additional_operations']={'root-discs':{'kind':'proper-definite-integral','operands':['1+4*x','0','6']},'normal-discs':{'kind':'proper-definite-integral','operands':['(20-5*x/2)**2','6','8']},'independent-cone-mensuration':{'kind':'identity','operands':['pi*5**2*2/3']}}
q['additional_operation_expected']={'root-discs':'78','normal-discs':'Rational(50,3)','independent-cone-mensuration':'50*pi/3'}
r=add('Example',40,369,'Explicit Exam-Style section:show PQ is the normal to a root curve,then find the exact volume of the curve-plus-normal region to the axis.',[p,q],['1','2','0'],'graph');r['connected_part_structure']='Normal established in(a) is the final region boundary in(b);the given P,Q determine its radius/height.'

refs=[(101,368,'Exercise7Q8 given root-curve/line lens','y=3√x andy=x intersectO andK;shading is their lens0..9. No separate learner sketch is asked.',[AREA],'graph','Exercise-7:8','given-figure'),(102,368,'Exercise7Q10 given root curve and LEFT-axis shading','y=√(1+2x),Aonnegative x-axis,Bony-axis,Cwithy3. Shading is the small regionLEFT ofy-axis,not a region involving the normal atC.',[VOL],'graph','Exercise-7:10','given-figure'),(103,369,'Example40 given normal candidate and composite shaded region','Root√(1+4x),P(6,5),Q(8,0). Shading followsroot0..6 thenline6..8 to the x-axis;it is not the lens between the functions.',[TANGENT,VOL],'graph','Example:40','given-figure'),(104,369,'Example40 SOLUTION cone labels','Worked diagram adds r5,h2 on the final cone segment. These labels are derived solution data,not additional original givens.',[VOL],'graph','Example:40','teaching-figure')]
for n,page,label,note,teaches,rep,parent,kind in refs:
 fig(n,page,label,note,teaches,rep,[],parent);figures[-1].update(item_id=f'8227:TB:YM:C7:Teaching-figure:{n}',printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind=kind,parent_item_id='8227:TB:YM:C7:'+parent)
 figures[-1]['mathematical_feature_review']['method']='Read original shading,axis side,point labels and region switches. Recompute parent results from original equations. Distinguish normal candidate from verified normal,and actual given diagrams from later cone labels.'
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=7,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-19',non_item_content='All Exercise7Q7–11 and Example40 enumerated. Source section7.3 starts369 and explicitly labels exam-style practice;the preceding Advanced Level exercise is not automatically an examination attribution. Four actual given/solution graphs recorded.',scope_screen='Preserve signed-motion reversal,positive parameters and inverse branches. Example40 requires normal proof and exact composite volume;no capability hold or reduced visual demand.')for page in range(368,370)]
h.pages=pages
if __name__=='__main__':h.save('exercise-advanced','Complete rendered368–369Exercise7Q7–11/Example40census;all16responseschecked,wrongdistancekeyretained.')
