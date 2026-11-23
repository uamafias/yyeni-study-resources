"""All fixed-source parameter-elimination/calculus Examples21–24, PDF126–129."""
import hashlib,json,sys
from pathlib import Path
from author_YM_C4_trig_graphs import value,reasoning
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2]
sys.path.insert(0,str(W/'tools'))
from verify_textbook_answers_r5 import compute,expression,equivalent
SRC='sources/namibia/nsscas/8227-mathematics/textbooks/Goldie_Pure-Mathematics-2-and-3_2nd-edition_2018.pdf'
SHA='f030d64259ffe233a7408d2a64dea21c0a04f1ac0426439f5efaea694eb72e85'
PARAM='8227:2020:M2:T4:O03:D02';GEOM='8227:2020:M2:T4:O03:D03';STATIONARY='8227:2020:M1:T8:O04:D01';CLASSIFY='8227:2020:M1:T8:O04:D02'
POWER='8227:2020:M1:T8:O02:D01';ELEMENTARY='8227:2020:M2:T4:O01:D01';SIMULT='8227:PRIOR:NSSCO:simultaneous-equations';COORD='8227:PRIOR:NSSCO:coordinate-geometry'
def ev(page):
    p=W/'checks/r5/textbooks/Goldie-C4-126.png';return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[];corrections=[]
def add(n,page,note,parts,direct,components=None,sketch=False):
    for p in parts:
        kp=p.pop('key_page_override',page);p.update(source_pdf_page=page,source_evidence=ev(page),answer_pdf_page=kp,answer_printed_page=kp-14,key_evidence=ev(kp),review_date='2026-11-18')
    row={'item_id':f'8227:TB:Goldie:C4:Example:{n}','source_pdf_page':page,'notes':note,'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],
      'mapping_rationale':'A pure elimination example prepares parametric calculus butdoesnot assess a derivative. The following examples actually ask the derivative andgeometric lines/plots orstationary classification. Source solution extras do not enlarge the requested response.',
      'evidence_role':'directly related assessed practice'if direct else'prerequisite/supporting algebraic elimination;no direct derivative coverage',
      'representation':'text','sketch_response_required':sketch,
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'not applicable','quoted_value':note,'reason':'Parametric differentiation/geometry,not finite trig-equation solving.'},
       {'rule_id':'8227:QUAL10','status':'within'if n in[21,22,24]else'not applicable','quoted_value':note,
        'reason':'Actual polynomial powers are2or3;derivatives retain original regularity restrictions.'if n in[21,22,24]else'Ellipse trigonometric parameter,not a rational-power boundary.'},
       {'rule_id':'8227:QUAL08','status':'not applicable','quoted_value':note,'reason':'Eliminating a parameter isnot automatically a requested inverse function.'}],
      'exam_style':False,'exam_style_basis':'Ordinary worked Example;no examination attribution.',
      'precision_angle_check':{'source':'Example23usesradianθ. Its solution presents an exact normal line andthen a2dpdisplay,plus2dppointcoordinates;the stem doesnot demand replacing exact values by rounded ones.',
        'comparison':'Use exact internal lines/points. Coefficient tuples describeAx+By+C=0;only explicitly stated nonzero constant rescalings normalise the printed equation. Preserve finite-derivative restrictions separately from line forms that geometrically extend to axes.'},
      'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts}
    answers.append(row);return row

def pvalue(label,kind,X,Y,target,page,at=None):
    p=value(label,'0',target,page,'Independently differentiate the original parametric coordinates. A derivative usesY′/X′onlywhereX′≠0. A tangent/normal line is formed from the parameter tangent vector andverified at its original point,so vertical lines are representable without an invalid reciprocal slope.')
    p['operation']={'kind':kind,'variable':'t','operands':[X,Y]}
    if at is not None:p['operation']['at']=at
    return p
p=value('elimination','(t**3-2*t**2).subs(t,2*y)','8*y**3-8*y**2',126,
 'From the sourcey=t/2,solve t=2yandsubstitute into the original x(t),givingx=8y³−8y². This algebraic representation task doesnot ask for a parametric derivative.')
p['author_answer_form']='x=8y³−8y².'
add(21,126,'Eliminatetfromx=t³−2t²,y=t/2. Keep the output asxintermsofy;no derivative orgeometric slope isrequested.',[p],[],[SIMULT])
X='t**2';Y='2*t'
p=pvalue('i','parametric-derivative',X,Y,'1/t',126);p['original_common_domain']='FiniteY′/X′requires t≠0;the original curve also includes the vertex at0.'
p2=pvalue('ii','parametric-tangent',X,Y,'Tuple(2,-2*t,2*t**2)',127)
p2['normalisation_note']='Coefficient tuple is twice the printed x−ty+t²=0;the nonzero scale2doesnot alter the line.'
p2['author_answer_form']='x−ty+t²=0,including the vertex tangentx=0at t=0.'
p3=pvalue('iii','parametric-tangent',X,Y,'Tuple(2,-6,18)',127,'3')
p3['normalisation_note']='Twice the printedx−3y+9=0.'
p4=value('iv-elimination','(2*t)**2-4*(t**2)','0',127,'The original pair satisfiesy²=4x;as t rangesoverR,y rangesoverR,andx≥0. This is the complete sideways parabola,not just its upperbranch.')
p4['check_mode']='show/prove';p4['author_answer_form']='y²=4x.'
p5=reasoning('iv-sketch','Right-opening parabola y²=4xwithvertex(0,0),both ybranches,andthe tangentx−3y+9=0at(9,6),crossingtheaxesat(−9,0),(0,3).',
 'The original parameter map covers both positive andnegative y. Its tangent vector(2t,2)isneverzero;at t=0it isvertical,consistent with the vertex tangent. At t=3the exact pointis(9,6)andthe line has slope1/3. The source graph shows both parabola branches andthe full tangent.',127,'sketch')
p5['additional_operations']={'point_at_3':{'kind':'identity','operands':['Tuple(t**2,2*t).subs(t,3)']},'vertex_tangent_vector':{'kind':'identity','operands':['Tuple(diff(t**2,t),diff(2*t,t)).subs(t,0)']}}
p5['additional_operation_expected']={'point_at_3':'Tuple(9,6)','vertex_tangent_vector':'Tuple(0,2)'}
row=add(22,126,'Forx=t²,y=2t:finddy/dx,thegeneralpointtangent,thetangentatt=3,theneliminate tand sketchthecurvewiththattangent. Finite-slopeform1/texcludest=0,buttheimplicitgeneraltangentcorrectlyincludesitsverticalvertexcase.',[p,p2,p3,p4,p5],[PARAM,GEOM],[POWER,COORD],True)
corrections.append({'item_id':row['item_id'],'continuation_pdf_pages':[127]})
X='4*cos(t)';Y='3*sin(t)'
p=pvalue('i','parametric-derivative',X,Y,'-3*cos(t)/(4*sin(t))',128);p['normalised_notation']={'t':'sourceθinradians'};p['original_common_domain']='Finitegradientrequires sinθ≠0;theellipseitselfanditsnormalsalsoexistatthoseaxispoints.'
p2=pvalue('ii','parametric-normal',X,Y,'Tuple(-4*sin(t),3*cos(t),7*sin(t)*cos(t))',128)
p2['normalisation_note']='Minus the printed coefficient vector for4xsinθ−3ycosθ−7sinθcosθ=0.'
p2['author_answer_form']='4xsinθ−3ycosθ−7sinθcosθ=0;thisimplicitnormalalsohandlesaxispointswithoutdividingbycosθ.'
p3=pvalue('iii','parametric-normal',X,Y,'Tuple(-2*sqrt(2),3*sqrt(2)/2,7/2)',128,'pi/4')
p3['normalisation_note']='Minus onehalf ofthe printed exact4√2x−3√2y−7=0.'
p3['additional_comparisons']=[{'label':'printed2dpnormalconstant','operation':{'kind':'rounded','operands':['7/sqrt(2)'],'decimal_places':2},'printed_key_normalised':'4.95'}]
p4=value('iv','Tuple(4*cos(pi/4),3*sin(pi/4))','Tuple(4/sqrt(2),3/sqrt(2))',128,
 'Evaluate the exact original ellipsepoint. The source writes the exact trigonometric/radical pair before displaying its approximation;the exact pair is the canonical value.')
p4['additional_comparisons']=[{'label':label,'operation':{'kind':'rounded','operands':[expr],'decimal_places':2},'printed_key_normalised':key}
 for label,expr,key in [('displayed-x','4*cos(pi/4)','2.83'),('displayed-y','3*sin(pi/4)','2.12')]]
p5=reasoning('v','Ellipsecentredat(0,0),semiaxes4and3,withpoint(2√2,3√2/2)andnormal4x−3y−7/√2=0. The normal slope is4/3.',
 'The coordinate identityx²/16+y²/9=1determines the full ellipse. The normal passes through the exact sourcepoint. The source solution also draws a blue tangent of slope−3/4,but the question asks only for the curveandnormal;that extra tangent isnot a required answer feature.',128,'sketch')
p5['unrequested_solution_features']=['The source Figure4.16also draws a tangent;do not require it when markingtheaskednormal sketch.']
p5['additional_operations']={'ellipse_identity':{'kind':'identity','operands':['(4*cos(t))**2/16+(3*sin(t))**2/9']},
 'normal_point_residual':{'kind':'identity','operands':['4*(4*cos(pi/4))-3*(3*sin(pi/4))-7/sqrt(2)']},
 'normal_at_top_axis':{'kind':'parametric-normal','variable':'t','operands':[X,Y],'at':'pi/2'}}
p5['additional_operation_expected']={'ellipse_identity':'1','normal_point_residual':'0','normal_at_top_axis':'Tuple(-4,0,0)'}
row=add(23,127,'Forx=4cosθ,y=3sinθ:derivegradient,generalnormal,normalatθ=π/4,thatpoint,andacurve/normal sketch. The exact lines are preserved;the optional blue tangent drawn in the model solution isnot a learner requirement.',[p,p2,p3,p4,p5],[PARAM,GEOM],[ELEMENTARY,COORD],True)
corrections.append({'item_id':row['item_id'],'continuation_pdf_pages':[128]})
X='2*t+1';Y='3*t-t**3'
p=pvalue('points','parametric-stationary-points',X,Y,'FiniteSet(Tuple(3,2),Tuple(-1,-2))',129)
p['author_source_working_comparison']={'status':'key wrong','observed_step':'At t=−1,theinlineworkingstatesx=−1,y=2,beforecorrectlyconcludingminimum(−1,−2).',
 'correct_step':'At t=−1,y=3(−1)−(−1)³=−2. The printed final point/classification iscorrect;the intermediatey=2is a sign typo.',
 'reason':'The source inline ordinate contradicts its own original cubic andfinalminimum point. Independent derivation agrees with the final set andidentifies the single wrong working value.'}
p2=reasoning('classification','Maximumat(3,2),minimumat(−1,−2).',
 'dx/dt=2>0,soparameterorderingagreeswithxordering. dy/dx=3(1−t²)/2changespositive-to-negativeat1andnegative-to-positiveat−1. The nearbysource tvalues0.9/1.1and−1.1/−0.9give±0.285/−0.315with the stated left/right positions. Alternatively d²y/dx²=−3t/2gives opposite signs at the two points.',129,'matches')
p2['additional_operations']={'nearby_x_and_slopes':{'kind':'identity','operands':['Tuple(Tuple(2*t+1,3*(1-t**2)/2).subs(t,9/10),Tuple(2*t+1,3*(1-t**2)/2).subs(t,11/10),Tuple(2*t+1,3*(1-t**2)/2).subs(t,-11/10),Tuple(2*t+1,3*(1-t**2)/2).subs(t,-9/10))']},
 'second_derivative_values':{'kind':'identity','operands':['Tuple((-3*t/2).subs(t,1),(-3*t/2).subs(t,-1))']}}
p2['additional_operation_expected']={'nearby_x_and_slopes':'Tuple(Tuple(14/5,57/200),Tuple(16/5,-63/200),Tuple(-6/5,-63/200),Tuple(-4/5,57/200))','second_derivative_values':'Tuple(-3/2,3/2)'}
add(24,129,'Forx=2t+1,y=3t−t³,findallstationarypointsanddistinguish their natures. x increases witht,so the first-derivative sign test mustbeapplied inCartesianleft/rightorder. The source has an inliney=2typoatt=−1butthefinal minimum(−1,−2)is correct.',[p,p2],[PARAM,GEOM,STATIONARY,CLASSIFY],[POWER])
figures=[]
for n,page,label,note,parent,rep,checks,method in[
 (39,126,'Parametric derivative chain-rule flow','dy/dx=(dy/dt)(dt/dx)=(dy/dt)/(dx/dt),provided dx/dt≠0. Theexplicitregularityconditionmustsurviveanysubsequentcancellation.',None,'table',
  [('(diff(2*t,t))/(diff(t**2,t))','1/t')],'Chainruleandinverselocalparameterderivativejustifytheformulaonaregularbranch;theexampleconfirmsitsrestrictiont≠0.'),
 (40,127,'Figure4.15 sideways parabola andtangent','Fullparabolay²=4x,tangentat(9,6),x-axisintercept−9andy-axisintercept3. Thecurvehasboth ybranches;thelinecanextend tonegativexeven thoughthecurvehasx≥0.','Example:22','graph',
  [('Tuple(9-3*6+9,(-9)-3*0+9,0-3*3+9)','Tuple(0,0,0)')],'Parentparameterelimination,pointandimplicit-linechecksverifythecurve/tangentrelationship. Acurveparameterdomainisnot a restriction ontheentiretangentline.'),
 (41,128,'Figure4.16 ellipse withnormal andextra tangent','Ellipseaxes4/3,exactpoint(2√2,3√2/2),displayedpoint(2.83,2.12),normalpositive slope4/3. Theblue tangent isextra solutioncontext,notrequiredbythequestion.','Example:23','graph',
  [('(4*cos(t))**2/16+(3*sin(t))**2/9','1')],'Useexactpoint/linecoefficientsandonlythencheckdisplayrounding. Allsourcegeometrycomesfromthe sameellipseparameters.'),
 (42,129,'Example4.24 local maximum sign sketch','Smallworked-solutiondiagramshowsincreasingthenhorizontal thendecreasingnear(3,2). Nearbyxvalues2.8and3.2correspondtot0.9and1.1.','Example:24','diagram',
  [('Tuple((3*(1-t**2)/2).subs(t,9/10),(3*(1-t**2)/2).subs(t,11/10))','Tuple(57/200,-63/200)')],'Checkactualxorderingaswellasderivativesigns;parametervaluessmaller/largerneednotalwaysmeanCartesianleft/right.'),
 (43,129,'Example4.24 local minimum sign sketch','Smallworked-solutiondiagramshowsdecreasingthenhorizontal thenincreasingnear(−1,−2). Theinliney=2isatyposourcevalue,not the minimumordinate.','Example:24','diagram',
  [('Tuple((3*(1-t**2)/2).subs(t,-11/10),(3*(1-t**2)/2).subs(t,-9/10),(3*t-t**3).subs(t,-1))','Tuple(-63/200,57/200,-2)')],'Theparentindependentpointandsignchecksresolve thecontradictoryinlinevalue andpreservethecorrect finalpoint.'),
 (44,129,'Alternative parametric second-derivative flow','d²y/dx²=[d/dt(dy/dx)]/(dx/dt),onaregularparameterbranch. Thisis anunprompted alternativemethod,not anextra question ormandatorymethod.','Example:24','table',
  [('diff(3*(1-t**2)/2,t)/diff(2*t+1,t)','-3*t/2')],'Differentiatewithrespecttotthen dividebydx/dt. Do notusethed/dtvaluealone as d²y/dx²;thechainfactorisessential.')]:
    results=[]
    for expr,target in checks:
        got=compute({'kind':'identity','operands':[expr]});assert equivalent(got,expression(target)),(label,got)
        results.append({'operation':{'kind':'identity','operands':[expr]},'source_normalised':target,'derived':str(got)})
    figures.append({'item_id':f'8227:TB:Goldie:C4:Teaching-figure:{n}','item_kind':'teaching-figure','exercise':'Teaching figure','item_number':str(n),'pdf_page':page,'printed_page':page-14,
     'source_label':label,'notes':note,'what_it_shows':note,'assessed_8227_demand_ids':[],'component_demand_ids':[],'teaches_8227_demand_ids':[PARAM,GEOM],
     'representation':rep,'source_evidence':ev(page),'parent_item_id':'8227:TB:Goldie:C4:'+parent if parent else None,'learner_display':False,
     'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'not applicable','quoted_value':note,'reason':'Derivative/geometry/formula support,not a bounded periodic equation.'}],
     'value_level_scope_review_status_r5':'authorcoordinates/line/regularity/sourceworkingread2026-11-18;independentcheckpending',
     'exam_representation_check':{'status':'finalcross-book/examinationcomparisonpending','examination_part_ids':[],'relation':'Internaltextbookworked/referencevisual;notexaminationfrequencyorofficialmarking.'},
     'mathematical_feature_review':{'status':'authorsourcerenderandparent/exactchecks;independentacceptancepending','method':method,'checks':results}})
pages=[{'pdf_page':page,'printed_page':page-14,'chapter':4,'page_status':'items enumerated',
 'item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],
 'continuation_item_ids':[r['item_id']for r in corrections if page in r['continuation_pdf_pages']],
 'source_evidence':ev(page),'non_item_content':'AllExamples21–24withcontinuations,theparametricchainflow,curve/linefigures,twolocalsignpanelsandalternativesecond-derivativeflowenumerated. Methodproseisattachedtorelevanttasks,nottreatedasextraproblems.',
 'reader':'Codex author','date':'2026-11-18'}for page in range(126,130)]
if __name__=='__main__':
    for name,data in[
     ('answers-Goldie-C4-param-examples.json',{'scope':'AllExample21–24parts;exactlines,parameterregularityandworkingtypoexplicit.','items':answers}),
     ('census-Goldie-C4-param-examples.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':4,'source_path':SRC,'source_sha256':SHA,
      'scope':'Complete126–129includingallworked/referencefigures.','new_items':figures,'corrections':corrections,'pages':pages})]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures')
