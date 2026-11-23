"""All source coordinate/plot/limit outputs, Goldie Examples19–20, PDF124–125."""
import hashlib,json,sys
from pathlib import Path
from author_YM_C4_trig_graphs import value,reasoning
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2]
sys.path.insert(0,str(W/'tools'))
from verify_textbook_answers_r5 import compute,expression,equivalent
SRC='sources/namibia/nsscas/8227-mathematics/textbooks/Goldie_Pure-Mathematics-2-and-3_2nd-edition_2018.pdf'
SHA='f030d64259ffe233a7408d2a64dea21c0a04f1ac0426439f5efaea694eb72e85'
PARAM='8227:2020:M2:T4:O03:D02';SKETCH='8227:2020:M1:T3:O05:D01';RANGE='8227:2020:M1:T3:O02:D02';COORD='8227:PRIOR:NSSCO:coordinate-geometry'
def ev(page):
    p=W/'checks/r5/textbooks/Goldie-C4-122.png';return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[]
def add(n,page,note,parts,direct,components):
    for p in parts:
        kp=p.pop('key_page_override',page);p.update(source_pdf_page=page,source_evidence=ev(page),answer_pdf_page=kp,answer_printed_page=kp-14,key_evidence=ev(kp),review_date='2026-11-18')
    row={'item_id':f'8227:TB:Goldie:C4:Example:{n}','source_pdf_page':page,'notes':note,'assessed_8227_demand_ids':direct,'component_demand_ids':components,
      'mapping_rationale':'Coordinate tables andparametric plots do not assess a parametric derivative. Example19doesask for a single-valued rationalfunction graph;Example20asks a multivalued curve plot andwhetheranyxvaluesareexcluded,not a complete image range. Keep prerequisite/context links separate fromassessed calculus.',
      'evidence_role':'directly related assessed function-graph practice;parametric-derivative preparation only'if direct else'prerequisite/supporting parametric representation;no directly assessed derivative coverage',
      'representation':'text','sketch_response_required':True,
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'not applicable','quoted_value':note,'reason':'No periodic-equation solving ortrig multiplier.'},
       {'rule_id':'8227:QUAL07','status':'within','quoted_value':note,'reason':'Simple inverse-square/quadratic projection domains,ranges andexcluded values;the full parameter definition andrequested plotting window are distinguished.'},
       {'rule_id':'8227:QUAL08','status':'not applicable','quoted_value':note,'reason':'No inverse function is requested. A multivalued parametric curve isnot silently forced into y=f(x).'}],
      'exam_style':False,'exam_style_basis':'Worked Examples in a green extension/representation section;no examination attribution.',
      'precision_angle_check':{'source':'Unitless parameter t;all tabulated values are exact integers orterminatingdecimals. No trig angle orrounding requirement.',
        'comparison':'Align every printed table cell by its parameter label,not by source/key order. InExample20,part(ii)bounds onlythe requested plot;part(iii)asks foranyexcludedvalues,so the keyx<0isvalid under both fullandplot-restricted interpretations.'},
      'source_interpretation':{'teaching_context_demand_id':PARAM,'role':'Prepares parametric differentiation;no derivative isasked.','scope_of_ranges':'Retain both original parameter domain andany part-specific plotting restriction.'},
      'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts}
    answers.append(row);return row

def cell(label,expr,key,page,t):
    p=value(label,expr,key,page,'Evaluateboth original Cartesian coordinate functions at this exact sourceparameter. Compare the separately transcribed printed table row aligned by t. Repeated Cartesian positions at different tvalues are not automatically duplicates or invalid cases.')
    p['source_parameter_value']=t;return p
parts=[]
for t,key in[('1','Tuple(2,36)'),('2','Tuple(4,9)'),('3','Tuple(6,4)'),('-1','Tuple(-2,36)'),('-2','Tuple(-4,9)'),('-3','Tuple(-6,4)')]:
    label='i-t-'+t.replace('-','minus-');parts.append(cell(label,f'Tuple(2*t,36/t**2).subs(t,{t})',key,124,t))
p=reasoning('ii','Two branches ofy=144/x²,x≠0:allordinatespositive,y-axissymmetry,verticalasymptotex=0,andthe six labelled sourcepoints.',
 'Fromx=2t,t=x/2;substitution givesy=36/(x/2)²=144/x². Negative andpositive sourceparameters trace separate branches;never join across t=0. The left branch rises toward the y-axis andthe right branch falls away from it. The finite source plot andits labelled samples are a viewport,not finite domain endpoints. The full curve has no x-axis crossing.',124,'sketch')
p['additional_operations']={'eliminated_parameter_residual':{'kind':'identity','operands':['144/(2*t)**2-36/t**2']},
 'reflection_residual':{'kind':'identity','operands':['144/(-t)**2-144/t**2']}}
p['additional_operation_expected']={'eliminated_parameter_residual':'0','reflection_residual':'0'};parts.append(p)
p=reasoning('iii','As t→0fromeither side,x→0andy→+∞;the y-axis is a verticalasymptote. t=0itself isundefined.',
 'The coordinate2tapproaches0with thesignoft,while36/t²ispositiveandunboundedfrombothsides. These are limits,not an actual point(0,∞)norpermission tosubstitutet=0.',124,'matches')
p['additional_operations']={'two_sided_coordinate_limits':{'kind':'identity','operands':['Tuple(limit(2*t,t,0,dir="-"),limit(2*t,t,0,dir="+"),limit(36/t**2,t,0,dir="-"),limit(36/t**2,t,0,dir="+"))']}}
p['additional_operation_expected']={'two_sided_coordinate_limits':'Tuple(0,0,oo,oo)'};parts.append(p)
row=add(19,124,'Forx=2t,y=36/t²:findpointscorrespondingtot=1,2,3,−1,−2,−3;plot/jointheseparatebranches;explain t→0. The original parameter isall realt≠0,not merelythe six sampledvalues.',parts,[SKETCH],[COORD])
row['source_interpretation']['original_parameter_domain']='Real t except0;the sample list isnot a parameter interval.'
parts=[]
for t,key in[
 ('-2','Tuple(4,-6)'),('-3/2','Tuple(9/4,-15/8)'),('-1','Tuple(1,0)'),('-1/2','Tuple(1/4,3/8)'),('0','Tuple(0,0)'),
 ('1/2','Tuple(1/4,-3/8)'),('1','Tuple(1,0)'),('3/2','Tuple(9/4,15/8)'),('2','Tuple(4,6)')]:
    label='i-t-'+t.replace('-','minus-').replace('/','-over-');parts.append(cell(label,f'Tuple(t**2,t**3-t).subs(t,{t})',key,125,t))
p=reasoning('ii','For−2≤t≤2,theplotis a x-axis-reflected pair ofarmsendingat(4,±6),with a loopthrough(0,0)andnode(1,0). Its xprojectionis[0,4].',
 'The parameter order matters. t=−1and1give the same point(1,0),so a node isexpected rather than an invalid duplicate. t=0gives the included origin. The verticaltangent at0andloop extremaat t=±1/√3follow fromdx/dt=2t,dy/dt=3t²−1;these are author feature checks,not additionally requested learner derivatives. Preserve both includedendpointst=±2.',125,'sketch')
p['additional_operations']={'x_axis_reflection_residual':{'kind':'identity','operands':['Tuple((-t)**2-t**2,((-t)**3-(-t))+(t**3-t))']},
 'restricted_x_projection':{'kind':'real-image-range','variable':'t','operands':['t**2','Interval(-2,2)']},
 'loop_extremum_points':{'kind':'identity','operands':['Tuple(Tuple(t**2,t**3-t).subs(t,-1/sqrt(3)),Tuple(t**2,t**3-t).subs(t,1/sqrt(3)))']},
 'origin_tangent_vector':{'kind':'identity','operands':['Tuple(diff(t**2,t).subs(t,0),diff(t**3-t,t).subs(t,0))']}}
p['additional_operation_expected']={'x_axis_reflection_residual':'Tuple(0,0)','restricted_x_projection':'Interval(0,4)','loop_extremum_points':'Tuple(Tuple(1/3,2/(3*sqrt(3))),Tuple(1/3,-2/(3*sqrt(3))))','origin_tangent_vector':'Tuple(0,-1)'};parts.append(p)
p=reasoning('iii','Yes:x<0is excluded. That answers the source question asking whether there are any such values. The part(ii)restrictedplot also excludesx>4;the unrestricted original curve doesnot.',
 'Becausex=t²≥0for every realt,negative xcannotoccur under either interpretation. The original pair is initially defined without an overall parameter bound andhas xprojection[0,∞). Part(ii)specifically requests a sketch for−2≤t≤2,whose xprojectionis[0,4]. The literal question saysany,notall;thereforetheprintedx<0isvalidandisnot a missing-answer defect. Do not silently turn this existence question into a complete-range task.',125,'matches')
p['additional_operations']={'full_original_x_projection':{'kind':'real-image-range','variable':'t','operands':['t**2','S.Reals']},
 'restricted_plot_x_projection':{'kind':'real-image-range','variable':'t','operands':['t**2','Interval(-2,2)']}}
p['additional_operation_expected']={'full_original_x_projection':'Interval(0,oo)','restricted_plot_x_projection':'Interval(0,4)'};parts.append(p)
row=add(20,125,'Forx=t²,y=t³−t:tabulate nine half-unit parameter values−2..2,sketch thatrestrictedcurve,andstatewhetheranyxvaluesareundefined. The keyx<0isvalid;part(iii)doesnotaskforacompleteprojectionrange.',parts,[],[COORD,RANGE])
row['direct_demand_aspects']=[{'role':'supporting parametric-curve representation,not a required derivative task','assessed_facet':'Coordinate evaluation,parameter-ordered multivalued plot,andexistence ofexcludedx;no parametric derivative isasked andno complete image range is required.'}]
row['source_interpretation'].update(original_parameter_domain='Real t in the initial definition',plot_parameter_domain='−2≤t≤2only inpart(ii)',
 original_x_projection='[0,∞)',plot_x_projection='[0,4]',key_adjudication='matches:thewordanymakesx<0a validanswer underbothscopes;clears theearlierauthorleadthatx>4wasnecessarilymissing.')
figures=[]
for n,page,label,note,parent,rep,method in[
 (35,124,'Example4.19 coordinate table','Sixparameter-labelledcolumnsfort=−3,−2,−1,1,2,3giveX=−6,−4,−2,2,4,6andY=4,9,36,36,9,4. Theanswer-tableorderdiffersfromthestemlist;labelsfixthealignment.',19,'table',
  'EverycolumnisindependentlyevaluatedfromX=2t,Y=36/t²intheparentanswerchecks. t=0isnotatablecellnoravalidparameter.'),
 (36,124,'Figure4.13 inverse-square parametric plot','Twopositivebranchesmirrorintheverticalaxis;sixsourcepointslabelt=±1,±2,±3. Thegridisafiniteviewport,whilethetextseparatelygivesthey-axisasymptote.',19,'graph',
  'Eliminationgivesy=144/x²withx≠0;parentpointsandlimitsverifytheshape. Thevisibleendsatthelabelledsamplesarenotnewdomainrestrictions.'),
 (37,125,'Example4.20 half-step coordinate table','Ninetvaluesfrom−2to2inhalfsteps;thepositionsatt=−1and1coincideat(1,0). Allterminatingdecimalcellsareexactrationalvaluesfortheseparameters.',20,'table',
  'Everycellisindependentlyevaluatedfromt²,t³−t. Keepbothparameterlabelsattherepeatedposition;ratherthanflaggingit asaninvalidduplicate.'),
 (38,125,'Figure4.14 bounded parametric loop','The−2≤t≤2plotincludesoriginandendpoints(4,±6),crossesitselfat(1,0),andhasanupper/lowerloopwithheight±2/(3√3). It isnot a single-valuedyfunctionofx.',20,'graph',
  'Parenttable,loop-extremumandorigin-tangentchecksverifythenode,verticaltangentandrestrictedxprojection[0,4]. Thefullunrestrictedcurvehaslargerextent;thekeyexistenceanswerx<0isstillvalid.')]:
    figures.append({'item_id':f'8227:TB:Goldie:C4:Teaching-figure:{n}','item_kind':'teaching-figure','exercise':'Teaching figure','item_number':str(n),'pdf_page':page,'printed_page':page-14,
     'source_label':label,'notes':note,'what_it_shows':note,'assessed_8227_demand_ids':[],'component_demand_ids':[],'teaches_8227_demand_ids':[PARAM],
     'representation':rep,'source_evidence':ev(page),'parent_item_id':f'8227:TB:Goldie:C4:Example:{parent}','learner_display':False,
     'value_level_scope_decisions':[{'rule_id':'8227:QUAL07','status':'within','quoted_value':note,'reason':'Actualinverse-square/quadraticdomain/rangeandtheexplicitparameterviewportarepreserved.'}],
     'value_level_scope_review_status_r5':'authorparameter/table/plotfeaturesread2026-11-18;independentcheckpending',
     'exam_representation_check':{'status':'finalcross-book/examinationcomparisonpending','examination_part_ids':[],'relation':'Textbookrepresentation/prerequisitesupport,notevidenceofassessedparametricdifferentiationorexamfrequency.'},
     'mathematical_feature_review':{'status':'authorsourcerenderandparentfixedsourcechecks;independentacceptancepending','method':method}})
pages=[{'pdf_page':page,'printed_page':page-14,'chapter':4,'page_status':'items enumerated',
 'item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],
 'continuation_item_ids':[],'source_evidence':ev(page),'non_item_content':'AllExamples19–20parts,coordinate-tablesandplotsenumerated. Greensectioncontext/technologyrangeadviceandtheparameter-eliminationintroductionareprose,notadditionallearnerquestions.',
 'reader':'Codex author','date':'2026-11-18'}for page in[124,125]]
if __name__=='__main__':
    for name,data in[
     ('answers-Goldie-C4-param-plots.json',{'scope':'Everyexplicitcoordinate,plotandlimit/excluded-valueoutputofExamples19–20;theearlierdomain-errorleadisclearedbyliteralquestionreading.','items':answers}),
     ('census-Goldie-C4-param-plots.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':4,'source_path':SRC,'source_sha256':SHA,
      'scope':'Complete124–125includingallsourcecoordinate/plotrepresentations.','new_items':figures,'corrections':[], 'pages':pages})]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures')
