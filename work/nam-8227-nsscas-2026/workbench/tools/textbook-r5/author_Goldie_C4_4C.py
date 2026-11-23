"""Fixed-source Exercise4C1–13, Goldie PDF114–115."""
import hashlib,json
from pathlib import Path
from author_YM_C4_trig_graphs import value,reasoning
from author_YM_C4_composite_equations import roots
from author_Goldie_C4_opening import derivative
from author_Goldie_C4_4A import at_deriv,at,tangent,normal
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2]
SRC='sources/namibia/nsscas/8227-mathematics/textbooks/Goldie_Pure-Mathematics-2-and-3_2nd-edition_2018.pdf'
SHA='f030d64259ffe233a7408d2a64dea21c0a04f1ac0426439f5efaea694eb72e85'
ELEMENTARY='8227:2020:M2:T4:O01:D01';COMPOSITE='8227:2020:M2:T4:O01:D02';PRODUCT='8227:2020:M2:T4:O02:D01';QUOTIENT='8227:2020:M2:T4:O02:D02'
POWER='8227:2020:M1:T8:O02:D01';GRADIENT='8227:2020:M1:T8:O01:D01';TANGENT='8227:2020:M1:T8:O03:D01'
STATIONARY='8227:2020:M1:T8:O04:D01';CLASSIFY='8227:2020:M1:T8:O04:D02';BND='8227:2020:M1:T6:O06:D01';ALL='8227:2020:M1:T6:O06:D02'
ATTR={7:'9709,Paper21Q3,November2011',8:'9709,Paper21Q3,June2015',9:'9709,Paper21Q2,June2014',10:'9709,Paper2Q3,June2006',11:'9709,Paper33Q3,November2015',12:'9709,Paper3Q4,November2007',13:'9709,Paper3Q3,November2008'}
def ev(page):
    name='Goldie-key-C3-341'if page in[343,344]else'Goldie-C4-114'
    p=W/f'checks/r5/textbooks/{name}.png';return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[]
def add(n,page,note,parts,direct,components=None,rep='text'):
    for p in parts:
        kp=p.pop('key_page_override',343 if n<=7 else 344);p.pop('source_page_override',None)
        p.update(source_pdf_page=page,source_evidence=ev(page),answer_pdf_page=kp,answer_printed_page=kp-14,key_evidence=ev(kp),review_date='2026-11-18')
    row={'item_id':f'8227:TB:Goldie:C4:Exercise-4C:{n}','source_pdf_page':page,'notes':note,
      'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],
      'mapping_rationale':'Keep explicit product/quotient/chain instructions,original domains andthe precise geometric target. All-curves/all-points demands differ from finding a supplied unique point. Explicit-function tangents do not acquire implicit/parametric labels.',
      'representation':rep,'sketch_response_required':False,
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'within'if n in[7,10]else'not applicable','quoted_value':note,
        'reason':'Complete bounded equations have argument multipliers2or1andexplicit finite radian intervals;original poles are excluded.'if n in[7,10]else'Derivative formulas or unique-point geometric tasks;the periodic equation multiplier rule isnot a general restriction on composition inside a derivative.'},
       {'rule_id':'8227:QUAL10','status':'within'if n in[4,5]else'not applicable','quoted_value':note,
        'reason':'Actual inner polynomial powers are2andthe square-root exponent is1/2.'if n in[4,5]else'No power-rule boundary in the requested target.'},
       {'rule_id':'8227:QUAL09','status':'not applicable','quoted_value':note,'reason':'Tangents use an explicitly differentiated curve,not a new repeated-root/discriminant task.'}],
      'exam_style':n in ATTR,'exam_style_basis':'Printed book attribution:'+ATTR[n]+'. Internal source lead;original paper not newly verified here.'if n in ATTR else'Ordinary exercise without examination attribution.',
      'precision_angle_check':{'source':'All differentiation uses radian inputs. Q8asks bothmandcto3sf;Q11asks onlycto3sfandpermits exactm. Other outputs are exact.',
        'comparison':'Retain exact internal slopes/intercepts before the specified final coefficient rounding. Do not reuse an approximate line as an exact curve relation.'},
      'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts}
    answers.append(row);return row
parts=[derivative(label,f,key,343,domain)for label,f,key,domain in[
 ('i','2*cos(x)+sin(x)','-2*sin(x)+cos(x)','All real radianx.'),('ii','tan(x)+5','sec(x)**2','cosx≠0.'),('iii','sin(x)-cos(x)','cos(x)+sin(x)','All real radianx.')]]
add(1,114,'Differentiate2cosx+sinx,tanx+5,andsinx−cosx. Keep the original tangent poles;all inputs are radians.',parts,[ELEMENTARY])
parts=[derivative(label,f,key,343,domain)for label,f,key,domain in[
 ('i','x*tan(x)','x*sec(x)**2+tan(x)','cosx≠0.'),('ii','sin(x)*cos(x)','cos(x)**2-sin(x)**2','All realx.'),('iii','exp(x)*sin(x)','exp(x)*(sin(x)+cos(x))','All realx.')]]
add(2,114,'Explicitly use product rule onx tanx,sinx cosx,ande^xsinx. Equivalentcos2xis accepted for the second derivative result;the required method still has to be demonstrated.',parts,[PRODUCT],[ELEMENTARY])
parts=[derivative(label,f,key,343,domain)for label,f,key,domain in[
 ('i','sin(x)/x','(x*cos(x)-sin(x))/x**2','x≠0.'),('ii','exp(x)/cos(x)','exp(x)*(sin(x)+cos(x))*sec(x)**2','cosx≠0.'),
 ('iii','(x+cos(x))/sin(x)','(sin(x)*(1-sin(x))-cos(x)*(x+cos(x)))/sin(x)**2','sinx≠0.')]]
add(3,114,'Explicitly use quotient rule onsinx/x,e^x/cosx,and(x+cosx)/sinx. Preserve each original denominator restriction,even if a later equivalent formula cancels something.',parts,[QUOTIENT],[ELEMENTARY])
parts=[derivative(label,f,key,344,domain)for label,f,key,domain in[
 ('i','tan(x**2+1)','2*x*sec(x**2+1)**2','cos(x²+1)≠0.'),('ii','sin(2*x)','2*cos(2*x)','All realx.'),('iii','log(sin(x))','1/tan(x)','sinx>0;the logarithm domain is not allnonpoleangles.')]]
parts[-1]['author_answer_form']='cosx/sinx(or cotx),with the originalsinx>0domain,includingzero derivativeatpositive sine maxima.'
parts[-1]['author_source_working_comparison']={'status':'key incomplete',
 'observed_step':'The printed derivative answer is1/tanx.',
 'correct_step':'Usecosx/sinxorcotxwiththeoriginalsinx>0domain;atpositive sine maxima the derivative is0.',
 'reason':'Read as literal real-function evaluation,1/tanxrequirescosx≠0,whereasln(sinx)is differentiable atx=π/2andotherpositive sine maxima. The formula agrees on the common domain,but a tangent intermediary introduces unnecessary holes. Treating it as cotangent shorthand requires preserving the original domain explicitly.'}
parts[-1]['additional_operations']={'original_derivative_at_sine_maximum':{'kind':'identity','operands':['diff(log(sin(x)),x).subs(x,pi/2)']},
 'printed_tangent_inner_denominator_at_same_angle':{'kind':'identity','operands':['cos(pi/2)']}}
parts[-1]['additional_operation_expected']={'original_derivative_at_sine_maximum':'0','printed_tangent_inner_denominator_at_same_angle':'0'}
add(4,114,'Explicitly use chain rule ontan(x²+1),sin2x,andln(sinx). The last formula is valid only where sinx>0;the tangent composite retains its own poles.',parts,[COMPOSITE],[ELEMENTARY,POWER])
parts=[derivative(label,f,key,344,domain)for label,f,key,domain in[
 ('i','sqrt(cos(x))','-sin(x)/(2*sqrt(cos(x)))','Originalcosx≥0;finite derivative formulacosx>0.'),
 ('ii','exp(x)*tan(x)','exp(x)*(tan(x)+sec(x)**2)','cosx≠0.'),('iii','sin(4*x**2)','8*x*cos(4*x**2)','All realx.'),
 ('iv','exp(cos(2*x))','-2*sin(2*x)*exp(cos(2*x))','All realx.'),('v','sin(x)/(1+cos(x))','1/(1+cos(x))','1+cosx≠0.'),
 ('vi','log(tan(x))','1/(sin(x)*cos(x))','tanx>0andcosx≠0;not the entire domain of the simplified reciprocal.')]]
add(5,114,'Choose an appropriate method for√cosx,e^x tanx,sin(4x²),e^(cos2x),sinx/(1+cosx),andln(tanx). Readsin4x²as sin(4x²),not(sin4x)²;preserve root/log domains.',parts,[COMPOSITE,PRODUCT,QUOTIENT],[ELEMENTARY,POWER])
f='x*cos(x)'
add(6,114,'Fory=xcosx:differentiate,find gradientatx=π,andfindtangentandnormal there. The curve point is(π,−π),withgradient−1;tangentandnormalare distinctexactlines.',[
 derivative('i',f,'cos(x)-x*sin(x)',344),value('ii',at_deriv(f,'pi'),'-1',344),value('iii',tangent(f,'pi'),'-x',344),value('iv',normal(f,'pi'),'x-2*pi',344)],
 [PRODUCT,GRADIENT,TANGENT],[ELEMENTARY])
p=roots('abscissae','sec(2*x)**2-4','FiniteSet(pi/6,pi/3)',344,[('cos','2*x','1/2',1),('cos','2*x','-1/2',1)],unit='radian',hi='pi/2')
p['additional_operations']={'original_derivative_residual':{'kind':'trig-identity-residual','operands':['diff(tan(2*x)/2,x)','sec(2*x)**2']}}
p['additional_operation_expected']={'original_derivative_residual':'0'}
p['method']='Differentiate the original half-tangent tosec²(2x),equate the gradientto4,solvebothcos(2x)=±1/2branches on0..π/2,andexclude theoriginalpoleπ/4. Checkeachrootagainsttheoriginalderivative.'
add(7,114,'Given graph ofy=(1/2)tan2xon0≤x≤π/2,findbothx-coordinateswheregradient4. Thepoleπ/4splits thegivenviewport;it isnot a validpoint.',[p],[GRADIENT,BND,ALL],[COMPOSITE],rep='graph')
f='6*sin(x)-2*cos(2*x)';m=at_deriv(f,'pi/6');c=f'({at(f,"pi/6")})-({m})*pi/6'
parts=[]
for label,expr,key in [('m',m,'8.66'),('c',c,'-2.53')]:
 p=value(label,expr,key,344,'Derive the exact slope from the original curve at its supplied point,then the exact intercept;round this requested coefficient only at the final3sf display.')
 p['operation']={'kind':'rounded','operands':[expr],'significant_figures':3};p['additional_operations']={'exact_coefficient_before_rounding':{'kind':'identity','operands':[expr]}};parts.append(p)
parts[0]['assertions']=[{'expression':at(f,'pi/6'),'expected':'2'}]
add(8,114,'For y=6sinx−2cos2x,find tangentat(π/6,2)iny=mx+cformwithbothmandcto3sf. The supplied point is independently verified onthecurve.',parts,[TANGENT],[COMPOSITE,ELEMENTARY])
add(9,115,'Find gradientsatx=0for3sinx+tan2xand6/(1+e^(2x)). Each asks a gradient value,not a tangent equation orstationarypoint.',[
 value('i',at_deriv('3*sin(x)+tan(2*x)','0'),'5',344),value('ii',at_deriv('6/(1+exp(2*x))','0'),'-3',344)],[GRADIENT],[COMPOSITE,ELEMENTARY,QUOTIENT])
f='x+2*cos(x)'
p=roots('stationary-abscissae','1-2*sin(x)','FiniteSet(pi/6,5*pi/6)',344,[('sin','x','1/2',1)],unit='radian')
p['additional_operations']={'original_curve_derivative':{'kind':'identity','operands':[f'diff({f},x)']}}
p['additional_operation_expected']={'original_curve_derivative':'1-2*sin(x)'}
p2=reasoning('classification','Maximumatx=π/6;minimumatx=5π/6.',
 'The second derivative is−2cosx. Itsvalues are−√3and+√3respectively,so the two stationary points have the statednatures. Both lie in0..2π;theendpointsarenotstationary.',344,'matches')
p2['additional_operations']={'second_derivative_values':{'kind':'identity','operands':[f'Tuple({at_deriv(f,"pi/6",2)},{at_deriv(f,"5*pi/6",2)})']}}
p2['additional_operation_expected']={'second_derivative_values':'Tuple(-sqrt(3),sqrt(3))'}
add(10,115,'Fory=x+2cosxon0≤x≤2π,findallstationaryx-coordinatesandclassifyeverypoint. Thecompleteboundedtrigsolutionsetistwoangles,notonlyaprincipalinversevalue.',[p,p2],[STATIONARY,CLASSIFY,BND,ALL],[ELEMENTARY])
f='(2-tan(x))/(1+tan(x))';m=at_deriv(f,'pi/4');c=f'({at(f,"pi/4")})-({m})*pi/4'
p=value('c',c,'1.68',344,'Derive the exact intercept fromtheoriginalcurve andslope atπ/4;roundc to3sf as requested,keepingmexact.')
p['operation']={'kind':'rounded','operands':[c],'significant_figures':3};p['additional_operations']={'exact_intercept':{'kind':'identity','operands':[c]}}
add(11,115,'Fory=(2−tanx)/(1+tanx),findtangentatx=π/4as y=mx+c. Onlycisrequestedto3sf;keepm=−3/2exact. Originalcosx≠0and1+tanx≠0.',[
 value('m',m,'-3/2',344),p],[TANGENT],[QUOTIENT,COMPOSITE,ELEMENTARY])
f='exp(-x)*sin(x)';r='pi/4'
p=value('i','solve(diff(exp(-x)*sin(x),x),x)[0]','pi/4',344,'The original derivative ise^(−x)(cosx−sinx). On0≤x≤π,the sole equalitycosx=sinxhasx=π/4. The source explicitly gives uniqueness;this isnot an all-points search acrossunboundedperiods.')
p['additional_operations']={'original_derivative_zero_at_answer':{'kind':'identity','operands':[at_deriv(f,r)]}}
p['additional_operation_expected']={'original_derivative_zero_at_answer':'0'}
p2=reasoning('ii','The stationarypoint is a maximum.',
 'The second derivative is−2e^(−x)cosx. Atπ/4it is−√2e^(−π/4)<0,so thepoint is a maximum.',344,'matches')
p2['additional_operations']={'second_derivative_at_answer':{'kind':'identity','operands':[at_deriv(f,r,2)]}}
p2['additional_operation_expected']={'second_derivative_at_answer':'-sqrt(2)*exp(-pi/4)'}
add(12,115,'Fory=e^(−x)sinx,givenonestationarypointfor0≤x≤π:finditsx-coordinateanddetermineitsnature. Neitheritsordinate norafullunboundedstationaryfamilyisasked.',[p,p2],[STATIONARY,CLASSIFY],[PRODUCT,COMPOSITE,ELEMENTARY])
f='exp(x)/cos(x)';p=value('abscissa','solve(diff(exp(x)/cos(x),x),x)[0]','-pi/4',344,
 'The derivative ise^x(1+tanx)/cosx. On the givenopenprincipalbranchcosx>0,the unique zero istanx=−1,sox=−π/4. Preserve the excludedendpoints anddo not claim a classification that wasnotasked.')
p['additional_operations']={'original_derivative_at_answer':{'kind':'identity','operands':[at_deriv(f,'-pi/4')]}}
p['additional_operation_expected']={'original_derivative_at_answer':'0'}
add(13,115,'Fory=e^x/cosxwith−π/2<x<π/2,givenonestationarypoint,finditsx-coordinate. Thebranchrestrictionrulesoutotherperiodicpossibilities;classificationisnotrequested.',[p],[STATIONARY],[QUOTIENT,ELEMENTARY])
figures=[{'item_id':'8227:TB:Goldie:C4:Teaching-figure:23','item_kind':'given-figure','exercise':'Given figure','item_number':'23','pdf_page':114,'printed_page':100,
 'source_label':'Exercise4C7 bounded half-tangent graph','notes':'Giveny=(1/2)tan2xon0≤x≤π/2,splitattheverticalasymptoteπ/4;zerosatbothincludedendpoints. Eachbranchisincreasingandthegradient4isattainedonceoneachside.',
 'what_it_shows':'Two pole-separated branches onthefiniteoriginalviewport;not a continuouscurveacrossπ/4.','assessed_8227_demand_ids':[],'component_demand_ids':[],
 'teaches_8227_demand_ids':[GRADIENT,COMPOSITE],'representation':'graph','source_evidence':ev(114),'parent_item_id':'8227:TB:Goldie:C4:Exercise-4C:7','learner_display':False,
 'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'within','quoted_value':'sec²(2x)=4,0≤x≤π/2,originalpoleπ/4excluded','reason':'Multiplier2andexplicitfiniteinterval.'}],
 'value_level_scope_review_status_r5':'authorfunction/viewport/poleread2026-11-18;independentcheckpending',
 'exam_representation_check':{'status':'finalcross-book/examinationcomparisonpending','examination_part_ids':[],'relation':'Internaltextbookgivenviewport;notexaminationfrequencyorofficialmarking.'},
 'mathematical_feature_review':{'status':'authorsourcerenderandoriginalderivative/rootcheck;independentacceptancepending',
  'method':'Differentiatetohalf×2sec²(2x);gradientpositiveonbothdomaincomponents;separateboundedsolvinggivesπ/6andπ/3. Originalpoles/endpointsarecheckedexplicitly.'}}]
# Page115alsoopensimplicitfunctions;thefollowingsegmentownsthecompletepagecensus.
pages=[{'pdf_page':114,'printed_page':100,'chapter':4,'page_status':'items enumerated',
 'item_ids':[r['item_id']for r in answers if r['source_pdf_page']==114]+[r['item_id']for r in figures],
 'continuation_item_ids':[],'source_evidence':ev(114),'non_item_content':'All4C1–8partsandthegivenhalftangentgraphexplicitlyenumerated.4C9–13on115areauthoredherebuttheirpagecensusawaitsitsimplicit-functionintro.',
 'reader':'Codex author','date':'2026-11-18'}]
if __name__=='__main__':
    for name,data in[
     ('answers-Goldie-C4-4C.json',{'scope':'All13Exercise4Cquestionsandeveryexplicitpart,PDF114–115.','items':answers}),
     ('census-Goldie-C4-4C.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':4,'source_path':SRC,'source_sha256':SHA,
      'scope':'Complete114;questionrecords115awaitcombinedpagecensuswithimplicitintro.','new_items':figures,'corrections':[],'pages':pages})]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures')
