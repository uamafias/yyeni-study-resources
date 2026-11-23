"""Goldie trig derivative activities, prompts and Examples11–14, PDF110–113."""
import hashlib,json,sys
from pathlib import Path
from author_YM_C4_trig_graphs import value,graph,reasoning
from author_YM_C4_composite_equations import transform
from author_Goldie_C4_opening import derivative
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2]
sys.path.insert(0,str(W/'tools'))
from verify_textbook_answers_r5 import compute,expression,equivalent
SRC='sources/namibia/nsscas/8227-mathematics/textbooks/Goldie_Pure-Mathematics-2-and-3_2nd-edition_2018.pdf'
SHA='f030d64259ffe233a7408d2a64dea21c0a04f1ac0426439f5efaea694eb72e85'
ELEMENTARY='8227:2020:M2:T4:O01:D01';COMPOSITE='8227:2020:M2:T4:O01:D02';PRODUCT='8227:2020:M2:T4:O02:D01';QUOTIENT='8227:2020:M2:T4:O02:D02'
POWER='8227:2020:M1:T8:O02:D01';GRADIENT='8227:2020:M1:T8:O01:D01';BASIC='8227:2020:M1:T6:O01:D01';SKETCH='8227:2020:M1:T6:O02:D03'
def ev(page):
    name='Goldie-key-C3-341'if page==343 else'Goldie-C4-110'
    p=W/f'checks/r5/textbooks/{name}.png';return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[];corrections=[]
def add(kind,n,page,note,parts,direct,components=None,sketch=False,rep='text'):
    for p in parts:
        kp=p.pop('key_page_override',page);pp=p.pop('source_page_override',None)or page
        p.update(source_pdf_page=pp,source_evidence=ev(pp),answer_pdf_page=kp,answer_printed_page=kp-14,key_evidence=ev(kp),review_date='2026-11-18')
    row={'item_id':f'8227:TB:Goldie:C4:{kind}:{n}','source_pdf_page':page,'notes':note,'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],
      'mapping_rationale':'Classify the actual gradient-graph,derivative orquotient proof request. The degree/radian prompt andvisual-evidence prompt are supporting conceptual tasks;they do not automatically assess the circle-arc definition ofa radian orrequire a first-principles proof.',
      'representation':rep,'sketch_response_required':sketch,
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'not applicable','quoted_value':note,
        'reason':'These are derivative/graph/formula tasks,not finite trig-equation solving;do not impose the equation multiplier restriction on a derivative coefficientk.'},
       {'rule_id':'8227:LIMIT03','status':'not applicable','quoted_value':note,
        'reason':'Graphical discovery andexplanation ofwhyit isnotproof do not impose a differentiation-from-first-principles requirement.'}],
      'exam_style':False,'exam_style_basis':'Ordinary Activity/Prompt/Example;no examination attribution.',
      'precision_angle_check':{'source':'Activity4.2andallstandardtrigderivatives use radian inputs. Prompt5explicitlyswitches the coordinate todegrees.',
        'comparison':'For degree coordinates,d/dx sin(πx/180)=(π/180)cos(πx/180);theunit factor cannotbe dropped. Every tangent/exponential-of-tangent original pole is retained.'},
      'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts}
    if not direct:row['evidence_role']='prerequisite/supporting conceptual evidence;no inventedcore-demandcoverage'
    answers.append(row);return row
p=graph('sine-gradient','cos','1','1','0','-2*pi','2*pi','radian',343,
 {'amplitude':'1','period':'2*pi','window_range':'Interval(-1,1)','window_zero_locations':'FiniteSet(-3*pi/2,-pi/2,pi/2,3*pi/2)',
  'window_global_max_locations':'FiniteSet(-2*pi,0,2*pi)','window_global_min_locations':'FiniteSet(-pi,pi)'})
p['method']='Infer derivative-graph zeros at the sine turns,positive/negative signs from its increasing/decreasing intervals,gradient1at the origin from its shown radian tangent y=x,andthe repeated±1extrema. These features give y=cosx on−2π..2π. Compare the separate keyplot;this graphical discovery isnot a universal analytic proof.'
p2=graph('cosine-gradient','sin','-1','1','0','-2*pi','2*pi','radian',343,
 {'amplitude':'1','period':'2*pi','window_range':'Interval(-1,1)','window_zero_locations':'FiniteSet(-2*pi,-pi,0,pi,2*pi)',
  'window_global_max_locations':'FiniteSet(-pi/2,3*pi/2)','window_global_min_locations':'FiniteSet(-3*pi/2,pi/2)'})
p2['source_page_override']=111
p2['method']='Apply the same slope-sign/turning-point construction to the radian cosine curve. Gradientzeros occur at its turns andthe derivative is−sinx. Preserve the requested−2π..2πviewport andthe reflectedsine sign.'
row=add('Activity',2,110,'Use the given radian sine graph withtangent y=xnear0andtheemptygradientframe toconstruct its gradientgraph on−2π..2π;then sketchcosxandconstruct its gradientgraph similarly. Markzeros,signs and±1gradient features rather than infer a formula froma picture alone.',[p,p2],[GRADIENT,ELEMENTARY,SKETCH],[BASIC],True,'graph')
corrections.append({'item_id':row['item_id'],'continuation_pdf_pages':[111]})
p=reasoning('degree-coordinate-tangent','No. With x measured in degrees,the tangent at the origin is y=(π/180)x,not y=x.',
 'The plotted function isg(x)=sin(πx/180). Chain rule givesg′(0)=π/180rather than1,andg(0)=0. The source key says tocompare thedegree/radian graphs;this exact derivative supplies the unit conversion that a correctly scaledgraph must reflect.',343,'matches')
p['additional_operations']={'degree_gradient_at_origin':{'kind':'identity','operands':['diff(sin(pi*x/180),x).subs(x,0)']},
 'radian_gradient_at_origin':{'kind':'identity','operands':['diff(sin(x),x).subs(x,0)']}}
p['additional_operation_expected']={'degree_gradient_at_origin':'pi/180','radian_gradient_at_origin':'1'}
add('Prompt',5,111,'Decide whethery=xremains tangent toy=sinxwhen the horizontal coordinate is degrees. Explain the angular-unit factor;this isnot direct evidence for defining a radian by arc/radius.',[p],[],[ELEMENTARY,GRADIENT])
p=reasoning('visual-evidence-limit','A graph-based resemblance is evidence for a conjecture,not an exact proof that two functions agree for every allowed input.',
 'A finite-window,finite-resolution sketch gives approximate slopes at selected positions. It cannot establish exact equality for every realargument or every pole-separated domain component. The source key calls this a demonstration bylooking,not a proof. No first-principles derivation is requested here.',343,'matches')
add('Prompt',6,111,'Explain why the graphical evidence resemblingcosxand−sinxdoesnot constitute proof ofthetwo derivativeformulas. This is supporting evidence reasoning,not an invented8227formal-proof demand.',[p],[],[ELEMENTARY])
p=transform('proof','(cos(x)*cos(x)-sin(x)*(-sin(x)))/cos(x)**2','sec(x)**2',
 ['(cos(x)**2+sin(x)**2)/cos(x)**2','1/cos(x)**2'],'cosx≠0;originaltangentandquotientpoles remainexcluded.',111)
p['method']='Startfromtanx=sinx/cosx. Use the quotient rule andthe earlier established radian sine/cosine derivatives,then sin²+cos²=1. This proves the requested tan derivative without assuming that same derivative as a premise.'
p['author_answer_form']='d(tanx)/dx=sec²x,oncosx≠0.'
p['additional_operations']={'original_quotient_identity':{'kind':'trig-identity-residual','operands':['tan(x)','sin(x)/cos(x)']},
 'direct_derivative_cross_check':{'kind':'identity','operands':['diff(tan(x),x)']}}
p['additional_operation_expected']={'original_quotient_identity':'0','direct_derivative_cross_check':'sec(x)**2'}
add('Activity',3,111,'Write tanx=sinx/cosxandusequotientrule toshowd(tanx)/dx=sec²xforradianx. Preserve cosx≠0;the standard sine/cosine derivatives are premises,not conclusions of this proof.',[p],[QUOTIENT,ELEMENTARY])
add('Example',11,112,'Differentiatecos2xwithradiancoordinatex:innerderivative2gives−2sin2x. The following panels generalise tosin/cos/tanofkx;theyareteachingreference,not additional assessed exercises.',[
 derivative('derivative','cos(2*x)','-2*sin(2*x)',112)],[COMPOSITE],[ELEMENTARY])
add('Example',12,112,'Differentiatex²sinxby productrulewithxmeasuredinradians;result2xsinx+x²cosx. No sketch orstationary point isrequested.',[
 derivative('derivative','x**2*sin(x)','2*x*sin(x)+x**2*cos(x)',112)],[PRODUCT],[ELEMENTARY,POWER])
add('Example',13,113,'Differentiatee^(tanx)usingu=tanxwithradianinput. Theoriginaldomainexcludes cosx=0;the derivative ise^(tanx)sec²x.',[
 derivative('derivative','exp(tan(x))','exp(tan(x))*sec(x)**2',113,'cosx≠0.')],[COMPOSITE],[ELEMENTARY])
add('Example',14,113,'Differentiate(1+sinx)/cosxby quotientruleandradiantrigderivatives;Pythagoreansimplificationgivessec²x(1+sinx). Retain all originalcosine-zero poles evenifan equivalent expression cancels a factor.',[
 derivative('derivative','(1+sin(x))/cos(x)','sec(x)**2*(1+sin(x))',113,'cosx≠0.')],[QUOTIENT],[ELEMENTARY])
figures=[]
for n,page,label,note,rep,checks,parent in[
 (16,110,'Figure4.3 radian sine andorigin tangent','Giveny=sinxover−2π..2π,withhorizontalturnsatoddπ/2andliney=xthroughorigin,matchingtheunitradslopethere. Thecoordinateunitispartofthemeaning.','graph',
  [('diff(sin(x),x).subs(x,0)','1'),('Tuple(sin(-3*pi/2),sin(-pi/2),sin(pi/2),sin(3*pi/2))','Tuple(1,-1,1,-1)')],'Activity:2'),
 (17,110,'Figure4.4 blank gradient response frame','Blankaxesforxfrom−2πto2πandgradientfrom−1to1;thisisalearnerresponseframe,not a supplied derivativegraph. Thegradientordinateisnotthesameasdisplacement.','graph',[],'Activity:2'),
 (18,111,'Sine derivative summary','d(sinx)/dx=cosxforradianx. Thewarning explicitlyrestrictstheunscaledformulatothisangularunit.','table',[('diff(sin(x),x)','cos(x)')],None),
 (19,111,'Cosine derivative summary','d(cosx)/dx=−sinxforradianx;theminussignisessential.','table',[('diff(cos(x),x)','-sin(x)')],None),
 (20,112,'Linear-argument cosine derivative panel','d(cos(kx))/dx=−k sin(kx),radianinputandconstantk.','table',[('diff(cos(k*x),x)','-k*sin(k*x)')],'Example:11'),
 (21,112,'Linear-argument sine derivative panel','d(sin(kx))/dx=k cos(kx),radianinputandconstantk.','table',[('diff(sin(k*x),x)','k*cos(k*x)')],'Example:11'),
 (22,112,'Linear-argument tangent derivative panel','d(tan(kx))/dx=k sec²(kx),radianinputandconstantk,wherecos(kx)≠0. Thek=0constantcaseisvalidwithoutpoles.','table',[('diff(tan(k*x),x)','k*sec(k*x)**2')],'Example:11')]:
    results=[]
    for expr,target in checks:
        got=compute({'kind':'identity','operands':[expr]});assert equivalent(got,expression(target)),(label,got)
        results.append({'operation':{'kind':'identity','operands':[expr]},'source_normalised':target,'derived':str(got)})
    figures.append({'item_id':f'8227:TB:Goldie:C4:Teaching-figure:{n}','item_kind':'given-figure'if n==16 else'teaching-figure','exercise':'Teaching figure','item_number':str(n),
     'pdf_page':page,'printed_page':page-14,'source_label':label,'notes':note,'what_it_shows':note,
     'assessed_8227_demand_ids':[],'component_demand_ids':[],'teaches_8227_demand_ids':[GRADIENT,ELEMENTARY]if n<18 else[COMPOSITE,ELEMENTARY],
     'representation':rep,'source_evidence':ev(page),'parent_item_id':'8227:TB:Goldie:C4:'+parent if parent else None,'learner_display':False,
     'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'not applicable','quoted_value':note,'reason':'Derivative/formula/response-frame support,not a finite trig equation with constrained multiplier.'}],
     'value_level_scope_review_status_r5':'authorangularunits/arguments/labelsread2026-11-18;independentcheckpending',
     'exam_representation_check':{'status':'finalcross-book/examinationcomparisonpending','examination_part_ids':[],'relation':'Textbookteaching/given/responseframerepresentation;notexaminationfrequencyorofficialcriteria.'},
     'mathematical_feature_review':{'status':'authorsourcerenderandexplicitderivative/featurechecks;independentacceptancepending','method':'Checkradianunits,exactturnsandslopes;blankframehasnoanswerclaim;formulaidentitiesretainoriginalpoles.','checks':results}})
pages=[]
for page in range(110,114):
    own=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
    if page==110:own.append('8227:TB:Goldie:C4:Exercise-4B:12')
    pages.append({'pdf_page':page,'printed_page':page-14,'chapter':4,'page_status':'items enumerated','item_ids':own,
     'continuation_item_ids':[r['item_id']for r in corrections if page in r['continuation_pdf_pages']],
     'source_evidence':ev(page),'non_item_content':'All4B12on110,Activity4.2withcontinuation,Activity4.3,Prompts5/6,Examples11–14,andsevenmathematicalreference/given/response-frameelementsenumerated. Explicitradianwarningandvisual-evidencelimitationareattachedtorelevantrecords.',
     'reader':'Codex author','date':'2026-11-18'})
if __name__=='__main__':
    for name,data in[
     ('answers-Goldie-C4-trig-intro.json',{'scope':'Allactivities/prompts/exampleson110–113;4B12detailsinitsownsegment.','items':answers}),
     ('census-Goldie-C4-trig-intro.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':4,'source_path':SRC,'source_sha256':SHA,
      'scope':'Completepages110–113,including4B12andalltrigderivativeteachingrepresentations.','new_items':figures,'corrections':corrections,'pages':pages})]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures')
