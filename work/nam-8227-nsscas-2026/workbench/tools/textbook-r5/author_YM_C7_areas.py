"""YM338–341: specified shaded regions,strip explanation and signed area."""
import json
import author_YM_C7_opening as h
from author_YM_C7_opening import W,SRC,SHA,pp,ev,v,fig,figures,compute,expression,equivalent,extra
from author_Goldie_C5_opening import definite
h.answers.clear();h.new.clear();h.corrections.clear();figures.clear()
answers=h.answers;new=h.new;corrections=h.corrections
AREA='8227:2020:M1:T9:O04:D01';DEF='8227:2020:M1:T9:O03:D01';ROOT='8227:2020:M1:T1:O02:D02';INT=h.INT
def area(label,f,lo,hi,key,kp,sign=1):
 p=definite(label,f,lo,hi,key,kp)
 p['operation']={'kind':'identity','operands':[f'{sign}*integrate({f},(x,{lo},{hi}))']}
 p['method']='Read the ORIGINAL shaded region and derive its actual boundary abscissas. Determine the sign of the curve on that interval,check continuity,then integrate with the explicit sign needed for positive geometric area. A different unshaded lobe is not included merely because it is bounded by the same curve.'
 p.update(assessed_8227_demand_ids=[AREA],component_demand_ids=[DEF,INT],given_representation='graph',response_format='numeric',units='units^2',printed_key_units='units^2',original_integrand=f,shaded_interval=[str(lo),str(hi)],curve_sign_on_shaded_interval='nonnegative'if sign==1 else'nonpositive')
 p['additional_operations']={'original-proper-signed-integral':{'kind':'proper-definite-integral','operands':[f,str(lo),str(hi)]}}
 p['additional_operation_expected']={'original-proper-signed-integral':f'({key})/({sign})'}
 return p
def add(kind,n,page,note,parts,powers,rep='graph'):
 direct=sorted({d for p in parts for d in p.get('assessed_8227_demand_ids',[])})
 comp=sorted({d for p in parts for d in p.get('component_demand_ids',[])}-set(direct))
 r=h.add(kind,n,page,note,parts,direct,comp,new_item=kind=='Try-Now'and n==16,powers=powers);r.update(representation=rep,mapping_rationale='The requested geometric AREA is directly assessed;ordinary definite integration is a component. Coordinate intercepts are direct only when separately requested. Shading determines which lobes/bounds belong to the task;worked solution sketches are not source givens or separately requested responses.')
 for p in parts:p['given_representation']=rep
 return r
add('Example',15,339,'Given graph y=x² shaded betweenx1and3above the axis;find area26/3squareunits.',[area('area','x**2',1,3,'Rational(26,3)',339)],['2'])
add('Try-Now',15,339,'Two separately shaded positive regions:3x² between1and3,and2x²+1between1and4. Use the labelled boundaries,not0.',[area('a','3*x**2',1,3,'26',627),area('b','2*x**2+1',1,4,'45',627)],['2','0'])
add('Example',16,339,'Given graph y=√(4−x),shaded from the y-axis to its x-intercept4. The finite endpoint root does not make the area improper.',[area('area','sqrt(4-x)',0,4,'Rational(16,3)',339)],['1/2'])
add('Try-Now',16,340,'Two positive shaded regions:the negative parabola−x(x+2)between its roots−2and0;and√(16+3x)between labelledx−4and3.',[area('a','-x*(x+2)',-2,0,'Rational(4,3)',627),area('b','sqrt(16+3*x)',-4,3,'26',627)],['2','1','1/2'])
p=v('a-intercepts','Tuple(Tuple(-1,0),Tuple(5,0),Tuple(0,-5))','Tuple(Tuple(-1,0),Tuple(5,0),Tuple(0,-5))',340,'Factor the ORIGINAL x²−4x−5=(x−5)(x+1). The given graph fixes A as the left root,B as the right root,C as the y-intercept. Check all incidences,not just the unordered root set.')
p['operation']={'kind':'identity','operands':['Tuple(Tuple(solve(x**2-4*x-5,x)[0],0),Tuple(solve(x**2-4*x-5,x)[1],0),Tuple(0,(x**2-4*x-5).subs(x,0)))']}
p.update(assessed_8227_demand_ids=[ROOT],component_demand_ids=[],given_representation='graph',response_format='symbolic')
r=add('Example',17,340,'Find the three labelled intercepts of x²−4x−5,then the shaded BELOW-axis area between its roots. Signed integral−36gives positive area36.',[p,area('b-area','x**2-4*x-5',-1,5,'36',340,-1)],['2','1','0']);r['connected_part_structure']='Part(a)root coordinates supply both bounds in(b);the graph supplies which below-axis region is shaded.'
add('Try-Now',17,341,'Only the shaded BELOW-axis lobe is requested in each graph. In(b),x(x−1)(x−2)has two bounded lobes,but the positive lobe0..1is UNSHADED;the requested interval is1..2,area1/4(native shading inspected).',[area('a','x*(x-3)',0,3,'Rational(9,2)',627,-1),area('b','x*(x-1)*(x-2)',1,2,'Rational(1,4)',627,-1)],['2','1','3'])
p=v('area','-integrate(x*(x-3),(x,0,3))+integrate(x*(x-3),(x,3,4))','Rational(19,3)',341,'The ORIGINAL text gives curve x(x−3),axis and x0..4. Derive roots0,3;the curve is negative0..3and positive3..4. Add POSITIVE lobe areas9/2and11/6,giving19/3. Absolute value of the whole signed integral would be8/3and is wrong. The solution draws a sketch as a method;the original prompt does not request a separate sketch response.')
p.update(assessed_8227_demand_ids=[AREA],component_demand_ids=[DEF,INT],given_representation='text',response_format='numeric',units='units^2',printed_key_units='units^2',original_integrand='x*(x-3)',shaded_intervals=[{'bounds':['0','3'],'sign':'negative'},{'bounds':['3','4'],'sign':'positive'}])
p['additional_operations']={'left-signed':{'kind':'proper-definite-integral','operands':['x*(x-3)','0','3']},'right-signed':{'kind':'proper-definite-integral','operands':['x*(x-3)','3','4']},'whole-signed':{'kind':'proper-definite-integral','operands':['x*(x-3)','0','4']}}
p['additional_operation_expected']={'left-signed':'-Rational(9,2)','right-signed':'Rational(11,6)','whole-signed':'-Rational(8,3)'}
add('Example',18,341,'TEXT-given area across an axis crossing:split at root3and add magnitudes. The source solution sketch is a teaching asset,not a given image or an asked sketch.',[p],['2','1'],'text')

refs=[
 (11,338,'Parabola and finite bounded area','y=x²between a andb,with0<a<b;vertical boundaries andx-axis enclose the positive shaded region.',[AREA],'graph',None,'teaching-figure'),
 (12,338,'Coarse rectangular strip approximation','Several vertical rectangles of widthΔxapproximate the area under y=x². Their coarse total is an approximation,not an exact finite-strip integral.',[AREA],'graph',None,'teaching-figure'),
 (13,338,'Finer rectangular strip approximation','More,narrower strips approximate the SAME bounded positive region. A chosen sampling convention and a limit are distinct from saying a finite sum is exactly the area.',[AREA],'graph',None,'teaching-figure'),
 (14,338,'Limiting strip area diagram','y=x²,shadedbetween a,b;the differential-strip notation supports the area integral. Do not treat a literal zero-width finite rectangle as having nonzero area.',[AREA],'graph',None,'teaching-figure'),
 (15,338,'Nonnegative-curve area formula','For integrable y=f(x)≥0on a≤x≤b,area=∫a^b f(x)dx. This positivity and ordered-bounds condition must survive variation.',[AREA],'table',None,'teaching-figure'),
 (16,339,'Example15 given shaded parabola','y=x²,vertical boundariesx1and3,shaded above axis. The origin is not the lower area bound.',[AREA],'graph','Example:15','given-figure'),
 (17,339,'Try15(a) given shaded parabola','y=3x²,bounds1,3,above-axis shading and labelledaxes.',[AREA],'graph','Try-Now:15','given-figure'),
 (18,339,'Try15(b) given lifted parabola','y=2x²+1,bounds1,4,above-axis shading. Its positivey-intercept does not change the labelled lower bound1.',[AREA],'graph','Try-Now:15','given-figure'),
 (19,339,'Example16 given root curve','y=√(4−x),shading fromx0to4. The curve decreases from(0,2)to(4,0)and remains nonnegative.',[AREA],'graph','Example:16','given-figure'),
 (20,340,'Try16(a) given inverted parabola','y=−x(x+2),roots−2,0,vertex(−1,1),shaded positive bounded region.',[AREA],'graph','Try-Now:16','given-figure'),
 (21,340,'Try16(b) given root graph','y=√(16+3x),shading between−4and3;end ordinates2and5,y-intercept4. The domain endpoint−16/3is not a labelled area boundary.',[AREA],'graph','Try-Now:16','given-figure'),
 (22,340,'Below-axis area reference','If f≤0on an ordered interval,the signed integral is nonpositive and geometricarea=−∫f. Omitting an explicit negative sign in shorthand must never turn geometric area negative.',[AREA],'table',None,'teaching-figure'),
 (23,340,'Example17 given intercept labels and shading','y=x²−4x−5;Aleftroot,Brightroot,Cy-intercept;below-axis bounded region shaded. Actual coordinates(−1,0),(5,0),(0,−5).',[AREA],'graph','Example:17','given-figure'),
 (24,341,'Try17(a) given negative lobe','y=x(x−3),below-axis lobe0..3shaded. Roots must be derived from the expression,not measured from an unscaled sketch.',[AREA],'graph','Try-Now:17','given-figure'),
 (25,341,'Try17(b) given one shaded cubic lobe','y=x(x−1)(x−2). ONLYnegative lobe1..2is shaded;positive lobe0..1is white. Native source read confirms this distinction;adding both would answer a different region.',[AREA],'graph','Try-Now:17','given-figure'),
 (26,341,'Example18 SOLUTION sketch','Worked sketch of y=x(x−3)marks0,3,4and both signed regions. It is generated in the solution to a TEXT-given question,not supplied in the prompt;no separate learner sketch is demanded.',[AREA],'graph','Example:18','teaching-figure'),
 (27,341,'Signed integral versus area comparison','On0..4,the signed integral−8/3differs from total area19/3. Split at the sign-changing root and add magnitudes;Abs(the whole integral)is not the total area.',[AREA],'table','Example:18','teaching-figure')]
for n,page,label,note,teaches,rep,parent,kind in refs:
 fig(n,page,label,note,teaches,rep,[],parent);r=figures[-1];r['item_id']=f'8227:TB:YM:C7:Teaching-figure:{n}'
 r.update(printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind=kind,parent_item_id='8227:TB:YM:C7:'+parent if parent else None)
 r['mathematical_feature_review']['method']='Read the actual rendered shading,bounds,axis labels and expressions. Recompute all parent areas/intercepts from original functions. Explicitly distinguish given images from solution sketches,and one shaded lobe from other unshaded lobes. This is an author source check,not automatic image interpretation or independent acceptance.'
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=7,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-19',non_item_content='All strip/area reference diagrams,Examples15–18 andTry15–17enumerated. Source area prose is attached to reference panels. Example18solution sketch is not an extra requested response;Try17(b)shading was checked natively.',scope_screen='Area under/below/crossing thex-axis,with proper finite integrals and exact boundaries. No visual-response capability hold is introduced.')for page in range(338,342)]
h.pages=pages
if __name__=='__main__':h.save('areas','Complete rendered338–341area/diagram census;exact requested regions and signs independently checked.')
