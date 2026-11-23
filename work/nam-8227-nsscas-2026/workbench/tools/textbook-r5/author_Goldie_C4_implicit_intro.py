"""Implicit definition/semicircle, Examples15–16 and Prompt3, PDF115–117."""
import hashlib,json,sys
from pathlib import Path
from author_YM_C4_trig_graphs import value,reasoning
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2]
sys.path.insert(0,str(W/'tools'))
from verify_textbook_answers_r5 import compute,expression,equivalent
SRC='sources/namibia/nsscas/8227-mathematics/textbooks/Goldie_Pure-Mathematics-2-and-3_2nd-edition_2018.pdf'
SHA='f030d64259ffe233a7408d2a64dea21c0a04f1ac0426439f5efaea694eb72e85'
IMPLICIT='8227:2020:M2:T4:O03:D01';GEOM='8227:2020:M2:T4:O03:D03';FUNCTION='8227:2020:M1:T3:O01:D01'
PRODUCT='8227:2020:M2:T4:O02:D01';ELEMENTARY='8227:2020:M2:T4:O01:D01';POWER='8227:2020:M1:T8:O02:D01'
def ev(page):
    name='Goldie-key-C3-341'if page==344 else'Goldie-C4-114'
    p=W/f'checks/r5/textbooks/{name}.png';return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[];corrections=[]
def add(kind,n,page,note,parts,direct,components=None,rep='text'):
    for part in parts:
        kp=part.pop('key_page_override',page);pp=part.pop('source_page_override',None)or page
        part.update(source_pdf_page=pp,source_evidence=ev(pp),answer_pdf_page=kp,answer_printed_page=kp-14,key_evidence=ev(kp),review_date='2026-11-18')
    row={'item_id':f'8227:TB:Goldie:C4:{kind}:{n}','source_pdf_page':page,'notes':note,'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],
      'mapping_rationale':'These examples actually treat y as a dependent variable andderive an implicit derivative;the geometric link belongs toExample16(ii). The graph prompt asks whether y is single-valued,not whether an existing function is one-to-one.',
      'representation':rep,'sketch_response_required':False,
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL10','status':'within'if kind=='Example'else'not applicable','quoted_value':note,
        'reason':'Integer powers2and3in the actual expressions/curve;chain/product rules retain dy/dx.'if kind=='Example'else'No derivative isrequested by the function-definition prompt.'},
       {'rule_id':'8227:QUAL08','status':'not applicable','quoted_value':note,'reason':'No inverse function is requested. The upper semicircle branch is a definition/example;vertical-line failure ofthe cubic isnot inverse one-to-one status.'}],
      'exam_style':False,'exam_style_basis':'Ordinary worked Example or prompt;no examination attribution.',
      'precision_angle_check':{'source':'Exact algebraic derivative,gradient andline equation. The sine-of-y building block assumes radian angular input.',
        'comparison':'Internal symbolpdenotesdy/dxonlyin the normalised formal derivative;it isnot an extra source parameter. Implicit slope−Fx/Fyis valid whereFy≠0;do not create finite slopes at vertical tangents.'},
      'expected_subpart_labels':[part['subpart']for part in parts],'subparts':parts}
    answers.append(row);return row
parts=[]
for label,expr,target in[('i','y**2','2*y*p'),('ii','x*y','x*p+y'),('iii','3*x**2*y**3','3*x*y**2*(3*x*p+2*y)'),('iv','sin(y)','cos(y)*p')]:
    part=value(label,'0',target,116,'Treatyasy(x),differentiateexplicitxdependenceandaddthechaintermFy*dy/dx. Applytheproductrulewherexandybothoccur. Comparethesourceexpressionwithpnormalisingdy/dx.')
    part['operation']={'kind':'implicit-expression-derivative','operands':[expr]};part['normalised_notation']={'p':'dy/dx'};parts.append(part)
row=add('Example',15,116,'Differentiatey²,xy,3x²y³,andsinywithrespecttoxwhileydepends onx. These are implicit-differentiation buildingblocks carryingdy/dx,not a complete curve equation to solve for a slope.',parts,[IMPLICIT],[PRODUCT,ELEMENTARY,POWER])
row['direct_demand_aspects']=[{'demand_id':IMPLICIT,'assessed_facet':'Building-blocktotalderivatives;thisdrilldoesnotalonecoverthefullimplicit-curve/geometricdemand.'}]
F='y**3+x*y-2'
part=value('i','0','-y/(3*y**2+x)',117,'From the original curveF=0,computeFxandFythen solveFx+Fy*dy/dx=0whereFy≠0. The printed result is separately transcribed,not used by the derivative calculation.')
part['operation']={'kind':'implicit-derivative','operands':[F]};part['original_common_domain']='OnF=0where3y²+x≠0;vertical slope cases excluded from this finite expression.'
part2=value('ii-gradient','(-diff(y**3+x*y-2,x)/diff(y**3+x*y-2,y)).subs({x:1,y:1})','-1/4',117)
part2['assertions']=[{'expression':'(y**3+x*y-2).subs({x:1,y:1})','expected':'0'},
 {'expression':'diff(y**3+x*y-2,y).subs({x:1,y:1})','expected':'4'}]
part3=value('ii-tangent','1+((-diff(y**3+x*y-2,x)/diff(y**3+x*y-2,y)).subs({x:1,y:1}))*(x-1)','(5-x)/4',117,
 'The verified point(1,1)has finite slope−1/4;form the tangent from that point. This is equivalent to the printedx+4y−5=0.')
row=add('Example',16,116,'Fory³+xy=2,finddy/dxintermsofx,y;hence gradientat(1,1)andthetangentthere. Checkthepointactuallyliesonthecurve andtheimplicitdenominatorisnonzero.',[part,part2,part3],[IMPLICIT,GEOM],[PRODUCT,POWER])
corrections.append({'item_id':row['item_id'],'continuation_pdf_pages':[117]})
part=reasoning('single-valued-test','The whole curve isnot the graph of a single-valued realfunctionyofx:one xcan have several yvalues.',
 'Forx=−3,the implicit equationy³−3y=2has bothy=2andy=−1. Both satisfy the original exactly,so a vertical line meets the curve at two distinct points. This is the function-definition test,not the horizontal-line test for one-to-one status. The displayed multibranch graph supports the same conclusion.',344,'matches')
part['additional_operations']={'two_distinct_y_at_same_x':{'kind':'identity','operands':['Tuple((y**3+x*y-2).subs({x:-3,y:2}),(y**3+x*y-2).subs({x:-3,y:-1}))']}}
part['additional_operation_expected']={'two_distinct_y_at_same_x':'Tuple(0,0)'}
row=add('Prompt',3,117,'Given the multibranch graph ofy³+xy=2,explain whyit isnot a functiony=f(x). Use the vertical-line/single-valued test;do not substitute a one-to-one/inverse-function test.',[part],[FUNCTION],rep='graph')
row['direct_demand_aspects']=[{'demand_id':FUNCTION,'assessed_facet':'Single-valued function definition via a vertical line;not every notation facet ofthe demand.'}]
figures=[]
for n,page,label,note,parent,teaches,checks,method in[
 (24,115,'Figure4.5 upper semicircle','x²+y²=4withy≥0is theuppersemicircle ofradius2;domain−2≤x≤2andrange0≤y≤2. Thebranchrestrictionisessentialforthisexampletobeafunction.',None,[IMPLICIT,FUNCTION],
  [('Tuple(sqrt(4-(-2)**2),sqrt(4-0**2),sqrt(4-2**2))','Tuple(0,2,0)')],
  'Pythagorasgivesx²+y²4;upperbranchchoosesy=√(4−x²),withbothendpointsy0included. This is implicit-definition support,not a separately requested inverse or derivative.'),
 (25,115,'Semicircle first-quadrant radius inset','InsetrighttriangleOP hasradius2,horizontalcoordinatexandverticalcoordinatey,withPshowninthefirstquadrant. Itmotivatesx²+y²=2²;thefulluppersemicirclealsocontainsnegative-xpoints.',None,[IMPLICIT],
  [('(sqrt(4-x**2))**2+x**2','4')],
  'Theinsetusespositiveleglengthsforthepicturedquadrant. Do not freelychangePtoa differentquadrantwhileleavingdirectedcoordinate/leglabelsunchanged.'),
 (26,117,'Figure4.6 multibranch implicit cubic','y³+xy=2hasonepositivebranchforallxandtwonegativebranchesforx<−3,meetingat(−3,−1). Atx=−3,y=−1andy=2arebothpresent;sothewholecurveisnotasingle-valuedfunction.','Prompt:3',[FUNCTION,IMPLICIT],
  [('Tuple((y**3+x*y-2).subs({x:-3,y:-1}),(y**3+x*y-2).subs({x:-3,y:2}))','Tuple(0,0)'),
   ('diff(2/y-y**2,y).subs(y,-1)','0')],
  'Parameteriseforanalysisbyx=2/y−y²withy≠0. Onnegativey,thefoldisaty−1,x−3;thepositivebranchnevercrossesthex-axis. Thegivengraphqualitativelymatchesandfailsaverticallinetest.')]:
    results=[]
    for expr,target in checks:
        got=compute({'kind':'identity','operands':[expr]});assert equivalent(got,expression(target)),(label,got)
        results.append({'operation':{'kind':'identity','operands':[expr]},'source_normalised':target,'derived':str(got)})
    figures.append({'item_id':f'8227:TB:Goldie:C4:Teaching-figure:{n}','item_kind':'given-figure'if n==26 else'teaching-figure','exercise':'Teaching figure','item_number':str(n),
     'pdf_page':page,'printed_page':page-14,'source_label':label,'notes':note,'what_it_shows':note,
     'assessed_8227_demand_ids':[],'component_demand_ids':[],'teaches_8227_demand_ids':teaches,'representation':'diagram'if n==25 else'graph',
     'source_evidence':ev(page),'parent_item_id':'8227:TB:Goldie:C4:'+parent if parent else None,'learner_display':False,
     'value_level_scope_decisions':[{'rule_id':'8227:QUAL08','status':'not applicable','quoted_value':note,'reason':'Implicit/function-definitionteaching,not aninversetask.'}],
     'value_level_scope_review_status_r5':'authorbranch/coordinate/curveread2026-11-18;independentcheckpending',
     'exam_representation_check':{'status':'finalcross-book/examinationcomparisonpending','examination_part_ids':[],'relation':'Internaltextbookdefinition/givenrepresentation;notexaminationfrequencyorofficialmarking.'},
     'mathematical_feature_review':{'status':'authorsourcerenderandexplicitcurve/branchchecks;independentacceptancepending','method':method,'checks':results}})
pages=[]
for page in[115,116,117]:
    own=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
    if page==115:own+=[f'8227:TB:Goldie:C4:Exercise-4C:{n}'for n in range(9,14)]
    pages.append({'pdf_page':page,'printed_page':page-14,'chapter':4,'page_status':'items enumerated','item_ids':own,
     'continuation_item_ids':[r['item_id']for r in corrections if page in r['continuation_pdf_pages']],
     'source_evidence':ev(page),'non_item_content':'All4C9–13on115,implicitdefinition/semicircleandinset,Examples15–16withcontinuation,andPrompt3/multibranchgraphenumerated. Stationary-pointprocedureparagraph117isproseadvice:solvegradientzerojointlywithoriginalcurve,not a newly posed task.',
     'reader':'Codex author','date':'2026-11-18'})
if __name__=='__main__':
    for name,data in[
     ('answers-Goldie-C4-implicit-intro.json',{'scope':'Everyimplicitbuildingblock/example/prompton115–117;the4Cpartsof115liveinthe4Csegment.','items':answers}),
     ('census-Goldie-C4-implicit-intro.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':4,'source_path':SRC,'source_sha256':SHA,
      'scope':'Completepages115–117,includingthe4Ccontinuation.','new_items':figures,'corrections':corrections,'pages':pages})]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures')
