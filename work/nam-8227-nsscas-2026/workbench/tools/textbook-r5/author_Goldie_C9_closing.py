"""Mixed rate/identity/branch evidence and both C9 investigations."""
import json
import author_Goldie_C9_opening as opening
from author_Goldie_C9_opening import W,SRC,SHA,add,answers,new,ev,fig,figures,value,reasoning,compute,expression,equivalent,RATE,POWER,CONSTANT
answers.clear();new.clear();figures.clear()
CURVE='8227:2020:M1:T9:O02:D02';IMPLICIT='8227:2020:M2:T4:O03:D01';COEFF='8227:2020:M1:T1:O03:D02'
TRIGINT='8227:2020:M2:T5:O01:D02';LOG='8227:2020:M2:T2:O02:D01';SKETCH='8227:2020:M1:T3:O05:D01'
def v(label,expr,key,method,page):return value(label,expr,key,page,method)
def partial(row,notes):row['scope_check'].update(status='in-scope-parts-only',excluded_or_qualified_parts=notes);return row

parts=[
 reasoning('draw-transect','Draw the segment from the markedHtoL,and use its approximate transverse relationship with the isobars.',
  'The source asks for a line on a copy of the map,not an exact coordinate construction. A valid line must join the two marked pressure centres and intersect successive isobars along the stated model transect. The map is not a graph ofpressureversusdistance until the values are read and plotted.',354,'sketch'),
 reasoning('distance-pressure-estimates','One source-consistent illustrative read isHabout(70°N,35°W),Labout(62°N,5°W),with transect length about900nautical miles,high1035andlow957in the map’s pressure units.',
  'Use the latitude-dependent nautical-mile scale on the printed map. The source key gives30°longitude separation at mean latitude66°,and an approximate900nautical-mile length. These are map estimates,not exact GPS coordinates. Its illustrative pressure profile starts1035andends957;read neighbouring contours and allow map resolution. No exact tolerance is commissioned here.',354,'matches'),
 reasoning('profile','A source-consistent proposed profile is p(x)=996+39cos(πx/900),0≤x≤900,with a decreasing half-wave.',
  'The illustrative mean is(1035+957)/2=996andhalf-range39. To join a high at0to a low at900with zero endpoint gradients,choose the half-period900,so b=π/900. This proposes a simple smooth model;the irregular contour spacings are not asserted to lie exactly on it. The key draws a continuation beyond900,but onlyHtoLis the observed transect.',354,'sketch'),
 v('gradient-parameters','Tuple(39*pi/900,pi/900)','Tuple(13*pi/300,pi/900)',
  'For the independently chosen source-consistent profile996+39cos(πx/900),differentiate it:dp/dx=−(39π/900)sin(πx/900). Thereforea=13π/300≈0.136andb=π/900≈0.0035in reciprocal-distance units. The source key’s decimals agree. These are illustrative fitted parameters,not unique exact quantities determined by a perfect physical map.',354),
 reasoning('suitability','The half-wave captures a smooth decline from a high to a low with relatively small endpoint gradients;it is an approximate local model.',
  'Check predicted steepest gradient near the midpoint against contour crowding and note that the source map is irregular. The source says the model covers the main features;that is qualitative. A single straight transect and this simplified gradient law do not establish an actual wind-speed law or justify periodic extrapolation beyond the map evidence.',354,'matches')]
parts[3]['key_normalisation_note']='The source key prints the cosine profile and its exact derivative−39π/900sin(πx/900),then gives a0.136,b0.0035as rounded constants. The normalised exact tuple comes from that displayed derivative,not invented precision for a measured map.'
parts[3]['additional_operations']={'profile_derivative':{'kind':'identity','operands':['diff(996+39*cos(pi*x/900),x)+39*pi*sin(pi*x/900)/900']},'endpoint_pressures':{'kind':'identity','operands':['Tuple((996+39*cos(pi*x/900)).subs(x,0),(996+39*cos(pi*x/900)).subs(x,900))']}};parts[3]['additional_operation_expected']={'profile_derivative':'0','endpoint_pressures':'Tuple(1035,957)'}
row=add('Investigation',1,236,'UnderPressure:drawHtoL on the weather map,estimate distance/pressures,suggesta,bfor dp/dx=−asinbx,and assess the approximate model. Every requested map/profile/model task is recorded as supporting representation/modelling evidence,not a new separable-ODE requirement.',parts,teaches=[RATE,TRIGINT],rep='diagram')
row['sketch_response_required']=True

p=v('particular-curve','integrate(3*x**2-2,x)+(0-integrate(3*x**2-2,x).subs(x,1))','x**3-2*x+1',
 'The source continuation supplies(1,0)for the explicit gradient3x²−2. Integrate to the familyx³−2x+C,then0=1−2+CgivesC=1. Check both the derivative and the actual point;the constant is fixed now,not arbitrary.',240)
p['additional_operations']={'gradient':{'kind':'identity','operands':['diff(x**3-2*x+1,x)-(3*x**2-2)']},'point':{'kind':'identity','operands':['(x**3-2*x+1).subs(x,1)']}};p['additional_operation_expected']={'gradient':'0','point':'0'}
row=add('Worked-illustration',2,240,'The unnumbered continuation of Example9.4selects the curve through(1,0)fromdy/dx=3x²−2. This is ordinary fixed-constant recovery,not the following separable Example9.7.',[p],[CONSTANT,CURVE])

p=reasoning('implicit-verification','On the branch through(0,0)with−π/2<y<π/2,implicit differentiation of siny=xgives y′=1/cosy=1/√(1−x²),for−1<x<1.',
 'Differentiate siny=xusing the chain rule:cosy·y′=1. The principal square root equals|cosy|,notcosyglobally. On the connected branch containing the initial valuey=0,cosy>0until an excluded derivative-singular endpoint,so the required positive reciprocal agrees. The initial condition is satisfied. The source’s equality omits the absolute-value/branch qualification;retain it as a source caution. No memorised inverse-sine differentiation formula is required.',243,'show/prove')
p['additional_operations']={'implicit_derivative_check':{'kind':'identity','operands':['cos(y)*(1/cos(y))-1']},'initial_condition':{'kind':'identity','operands':['sin(0)-0']},'opposite_branch_signs':{'kind':'identity','operands':['Tuple(sign(1/cos(pi)),sign(1/sqrt(1-sin(pi)**2)))']}};p['additional_operation_expected']={'implicit_derivative_check':'0','initial_condition':'0','opposite_branch_signs':'Tuple(-1,1)'}
row=partial(add('Example',9,242,'Verify the supplied implicit relation siny=xagainst a displayed derivative and initial conditiony(0)=0. The prescribed implicit differentiation is retained with the connected branch and positive-root condition explicit;the unrestricted source equality is not accepted globally.',[p],[IMPLICIT],continuation=[243]),['The derivative identity requires the branch through(0,0),−π/2<y<π/2and−1<x<1. No general inverse-trig integration is commissioned.'])

p=v('i-fixed-curve','integrate(x**2-1,x)+(2-integrate(x**2-1,x).subs(x,3))','x**3/3-x-4',
 'The derivative depends only onx. Integrate to x³/3−x+C,then imposey(3)=2to obtainC=−4. Differentiate and substitute the original point independently.',354)
p['additional_operations']={'point':{'kind':'identity','operands':['(x**3/3-x-4).subs(x,3)']}};p['additional_operation_expected']={'point':'2'}
partial(add('Exercise-9C',1,243,'Retain(i):recover the curve fromdy/dx=x²−1andy(3)=2. The following(ii)–(vi)require general variable separation and remain additional.',[p],[POWER,CONSTANT,CURVE]),['ii–vi:general separation-of-variables procedures,not direct explicit-gradient integration.'])

p=v('i-height-rate-coefficient','(20-k*x**2)/(diff(Rational(4,3)*x**3,x))','5/x**2-k/4',
 'From the supplied volumeV=(4/3)h³,dV/dh=4h². Net inflow is20−kh²,so dh/dt=(20−kh²)/(4h²)=5/h²−k/4forh>0. At h1andheight-rate4.95,k/4=0.05,so the requested relation is5/h²−1/20. The initially empty point h=0is a limiting start where this height derivative is singular;do not substitute0into the rate formula.',245)
p['additional_operations']={'calibrated_loss_coefficient':{'kind':'identity','operands':['solve(5-k/4-Rational(495,100),k)[0]']}};p['additional_operation_expected']={'calibrated_loss_coefficient':'Rational(1,5)'}
p['check_mode']='show/prove';p['author_answer_form']='dh/dt=5/h²−1/20,forh>0;the specified initially empty state is a boundary limit.'
p2=v('ii-given-rational-identity','cancel(-20+2000/((10+x)*(10-x))-20*x**2/(100-x**2))','0',
 'The source supplies the entire rational identity. Put the right side over denominator100−h²:−20(100−h²)+2000=20h². The equality holds whereverh≠±10;those exclusions cannot be cancelled away. This is verification of a supplied algebraic identity,not choosing a partial-fraction form.',245)
p2['check_mode']='show/prove'
row=partial(add('Exercise-9C',8,244,'The supplied tank lawV=(4/3)h³continues onto245. Retain(i)net connected rates/calibration and(ii)verification of the fully supplied rational identity. Part(iii)explicitly solves the differential equation and remains additional.',[p,p2],[RATE],continuation=[245],rep='diagram',exam_attribution='Cambridge9709Paper3Q8November2008'),['iii:general separation/rational integration to solve the differential equation.'])
row['component_demand_ids']=['8227:2020:M1:T1:O03:D01']
row['direct_demand_aspects']=[{'demand_id':RATE,'assessed_facet':'i only:net connected rates and calibration. Part(ii)is a supplied algebraic identity verification,retained as supporting structure rather than another rate demand.'}]
# The opening part starts244; both requested responses actually occur245.
for p in[p,p2]:p['source_pdf_page']=245;p['source_evidence']=ev(245)

p=v('i-depth-rate','-k*sqrt(x)/diff(pi*x**3,x)','-k/(3*pi*x**(Rational(3,2)))',
 'The cone’s semi-vertical angle60°givesr=h tan60°=√3h. ThusV=(π/3)r²h=πh³anddV/dh=3πh². The stipulated loss isdV/dt=−k√hwithk>0. Divide the two rates for h>0to getdh/dt=−[k/(3π)]h^(−3/2),soA=k/(3π)>0. This forms a connected-rate equation;it does not solve it.',246)
p['check_mode']='show/prove'
partial(add('Exercise-9C',13,246,'Use the given60°cone geometry and volume loss proportional to√hto establish the depth-rate formdh/dt=−Ah^(−3/2),A>0. Retain(i);the following ODE solution and time comparison are additional.',[p],[RATE],rep='diagram',exam_attribution='Cambridge9709Paper31Q10November2013'),['ii–iii:solve the state-dependent differential equation and use that solution.'])

parts=[]
p=reasoning('assumptions','Choose and state initial/ambient temperatures,a cooling constant,common heat capacity/density for mixing,a milk fraction convention,and an unchanged cooling constant for the comparison.',
 'The investigation is open. The source key explicitly chooses the9A7data:initial95°C,ambient15°C,initial loss0.5°C/s,so the model coefficient is1/160persecond. Use those as one declared mathematical scenario,not measured universal coffee behaviour or a drinking-safety claim. The original question does not demand a unique parameter set.',355,'matches');parts.append(p)
p=v('unmixed-model','Tuple((15+80*exp(-x/160)).subs(x,0),diff(15+80*exp(-x/160),x).subs(x,0))','Tuple(95,-Rational(1,2))',
 'Independently check the explicitly proposed profileθ(t)=15+80e^(−t/160):its initial temperature is95andinitial derivative−0.5. Its derivative equals−(θ−15)/160andits limit is15. This checks a candidate model without requiring a general ODE-solving method.',355)
p['additional_operations']={'model_residual':{'kind':'identity','operands':['diff(15+80*exp(-x/160),x)+(80*exp(-x/160))/160']}};p['additional_operation_expected']={'model_residual':'0'};parts.append(p)
p=v('milk-first-10percent-final-mixture','Rational(9,10)*95+Rational(1,10)*5-15','71',
 'Under equal heat capacities and10percent milk as a fraction of the final mixture,the immediate mixture is0.9·95+0.1·5=86°C. Its excess above room temperature is71,so the source key’s profile15+71e^(−t/160)is correct under this convention. If10percent instead means milk volume relative to the original coffee,the excess is790/11,not71;record the convention rather than flagging an unconditional key error.',355)
p['additional_operations']={'relative_to_original_convention':{'kind':'identity','operands':['(95+Rational(1,10)*5)/(1+Rational(1,10))-15']}};p['additional_operation_expected']={'relative_to_original_convention':'Rational(790,11)'};parts.append(p)
p=v('milk-at-end-profile','expand(Rational(9,10)*(15+80*exp(-x/160))+Rational(1,10)*5)','14+72*exp(-x/160)',
 'First cool the unmixed coffee for the same elapsed timet,then mix10percent of the final mixture at5°C. Equal-heat-capacity weighted averaging gives14+72e^(−t/160). This is a comparison under the declared constant assumptions;the source key does not separately print this intermediate expression.',355)
p['key_presence']='Author-derived intermediate supporting the key’s final comparison';p['check_mode']='no key';p['key_normalisation_note']='This exact intermediate profile is author-derived;the source only gives the early-milk profile and final ordering. The stored target is not presented as a verbatim printed key.';parts.append(p)
p=reasoning('comparison','For anyt>0,the milk-at-end mixture is cooler by1−e^(−t/160)degrees in the chosen10percent-final-mixture scenario.',
 'Subtract the late profile from the early one:(15+71E)−(14+72E)=1−E,whereE=e^(−t/160)lies strictly between0and1for t>0. At0the profiles coincide. The source’s final comparison agrees under these assumptions. If adding milk changes the cooling coefficient or the fraction is defined differently,recalculate rather than using a universal rule.',355,'matches')
p['additional_operations']={'profile_difference':{'kind':'identity','operands':['(15+71*exp(-x/160))-(14+72*exp(-x/160))']}};p['additional_operation_expected']={'profile_difference':'1-exp(-x/160)'};parts.append(p)
row=add('Investigation',2,247,'Cooling:state model assumptions,choose initial/room data,compare adding5°Cmilk immediately versus after cooling,and explain which final mixture is cooler. Both conventions for10percent are distinguished;the source choice is one conditional scenario,not an exact physical law.',parts,teaches=[RATE],rep='text')
row['scope_check'].update(status='in-scope-parts-only',excluded_or_qualified_parts=['The open investigation’s general ODE-model solution is additional. Retained work checks explicit exponential profiles,weighted mixing and their comparison under declared assumptions.'])

for n,page,label,note,teaches,rep,checks,parent in [
 (7,236,'Figure9.4 weather-map transect','The map marksHandL,pressure contours and a latitude-dependent nautical-mile scale. Read values and length before proposing a one-dimensional pressure profile;do not treat longitude degrees as a constant distance scale.',[RATE],'diagram',[],'Investigation:1'),
 (8,240,'Figure9.5 vertical family of explicit primitives','The curvesx³−2x+CforC2,0,−1are vertical translations with the same derivative3x²−2. Their axis intercepts differ. A point condition selects a particularC.',[CONSTANT,CURVE],'graph',[('Tuple((x**3-2*x+2).subs(x,0),(x**3-2*x).subs(x,0),(x**3-2*x-1).subs(x,0))','Tuple(2,0,-1)')],None),
 (9,241,'Figure9.6 shifted reciprocal family','The given curves−1/(x+C),C0,1,−1,have vertical asymptotes0,−1,1respectively and horizontaly=0. Their picture can teach rational domains/shifts even though deriving them by separating variables is additional.',[SKETCH],'graph',[],None),
 (10,242,'Figure9.7 positive physical velocity branch','The givenv=√(6t+4)starts atv2forphysicalt0and increases concave down. The mathematical root expression is defined back tot=−2/3,but that earlier branch segment is outside the stated motion interval. Deriving the curve by ODE separation is additional.',[RATE,SKETCH],'graph',[('sqrt(6*0+4)','2')],None),
 (11,245,'Exercise9C8 inverted tank','The drawing represents an inverted pyramidal tank. The given volume lawV=(4/3)h³controls the rate calculation;differentiate that supplied law rather than inferring unstated lengths from the perspective drawing. Emptyh0is a limiting start.',[RATE],'diagram',[('diff(Rational(4,3)*x**3,x)','4*x**2')],'Exercise-9C:8'),
 (12,246,'Exercise9C13 cone section','The semi-vertical angle is60°and the current depth ish,so current surfaceradius is√3h. This is the semi-angle at the vertex,not a full120°angle to insert into tan. The cone volume isπh³.',[RATE],'diagram',[('tan(pi/3)','sqrt(3)')],'Exercise-9C:13'),
 (13,247,'General versus particular integral summary','The arbitrary integration constant generates a family;additional point data select a particular member. These facts apply to prescribed explicit primitives. The surrounding general separable-ODE outcome is not thereby prescribed.',[CONSTANT,CURVE],'table',[],None),
 (14,239,'Logarithm argument versus additive constant warning','The source correctly distinguishes ln|x+C|fromln|x|+C. However its surrounding Example9.6has e^y=x+C>0,so its solution must usex+C>0;an absolute value must not invent a negative-argument solution branch.',[LOG],'table',[],None),
 (15,238,'Positive-variable logarithm reminder','The given y>0permits ln|y|=lny. That specific domain condition is essential and is not an unconditional rule for all realy.',[LOG],'table',[],None),
 (16,238,'Exponentiated constant reminder','Fromlny=x²/2+Cwithy>0,exponentiation givesy=e^C e^(x²/2),not e^(x²/2)+e^C. The multiplicative constante^Cis strictly positive.',[LOG],'table',[('exp(x**2/2+c)-exp(c)*exp(x**2/2)','0')],None)]:
 fig(n,page,label,note,teaches,rep,checks,parent)
for f in figures:
 f['item_id']=f['item_id'].replace(':C5:',':C9:');f['parent_item_id']=f['parent_item_id'].replace(':C5:',':C9:')if f['parent_item_id']else None;f['source_evidence']=ev(f['pdf_page']);f['value_level_scope_decisions']=[{'rule_id':'8227:LIMIT07','status':'not applicable','quoted_value':f['notes'],'reason':'Given/reference evidence,not a required general integration procedure.'}]
notes={240:'The unnumbered explicit-gradient fixed-point illustration and Figure9.5are retained. Example9.7solves a state-dependent ODE by separation and is additional.',241:'Example9.7continues;its reciprocal-family diagram is retained for domain/shift representation. Example9.8forms and solves an inverse-velocity acceleration equation;its unsupplied separation method is additional,not new required motion practice.',242:'Example9.8continues;its positive-branch diagram is retained. Example9.9asks verification of a supplied implicit relation;that proof is retained with branch limits and continues243.',243:'Example9.9continuation needs|cosy|and a branch restriction;the caution is recorded.9C1(i)is prescribed direct fixed-point recovery;ii–virequire separation.9C2/3ODEsolutions and ensuing model extrapolations remain additional.',244:'9C4–7require ODEsolution methods.9C8begins with a given cubic volume law;its connected-rate/identity parts on245are retained separately from the ODEsolution.',245:'9C8(i)/(ii)andthe tank figure are retained.9C9/10solve population ODEmodels;they are additional. A picture or later scalar prediction does not imply the full method is prescribed.',246:'9C11/12require general separation.9C13(i)is prescribed cone connected rates and its diagram is retained;ii/iiiuse the additional ODEsolution.',247:'The Cooling investigation has every conditional model/mixing/comparison response recorded. Its answer is not universal physical guidance. The general/particular constant reference is retained;the broader ODEoutcomes remain additional.'}
pages=[]
for page in range(240,248):
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 continuation=['8227:TB:Goldie:C9:Example:9']if page==243 else['8227:TB:Goldie:C9:Exercise-9C:8']if page==245 else[]
 pages.append({'pdf_page':page,'printed_page':page-14,'chapter':9,'page_status':'items enumerated'if ids or continuation else'scope-screened; no in-scope item starts','item_ids':ids,'continuation_item_ids':continuation,'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-18','non_item_content':notes[page],'scope_screen':'Part-level explicit-gradient/rate/identity/implicit-verification content is separated from unprescribed general ODEsolving.'})
if __name__=='__main__':
 for name,data in [('answers-Goldie-C9-closing.json',{'scope':'Both investigations and every retained fixed-curve,implicit-proof,tank-identity and cone-rate response.','items':answers}),('census-Goldie-C9-closing.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':9,'source_path':SRC,'source_sha256':SHA,'scope':'Complete240–247;earlier reference figures/investigation are linked by the opening census.','new_items':new+figures,'corrections':[],'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for r in answers:
  for p in r['subparts']:
   if 'operation'in p:
    got=compute(p['operation']);assert equivalent(got,expression(p['printed_key_normalised'])),(r['item_id'],p['subpart'],got)
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(r['item_id'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures')
