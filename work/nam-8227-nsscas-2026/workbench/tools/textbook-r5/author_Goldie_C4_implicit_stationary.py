"""Fixed-source implicit stationary Examples17–18 and figures, PDF118–120."""
import hashlib,json,sys
from pathlib import Path
from author_YM_C4_trig_graphs import value,reasoning
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2]
sys.path.insert(0,str(W/'tools'))
from verify_textbook_answers_r5 import compute,expression,equivalent
SRC='sources/namibia/nsscas/8227-mathematics/textbooks/Goldie_Pure-Mathematics-2-and-3_2nd-edition_2018.pdf'
SHA='f030d64259ffe233a7408d2a64dea21c0a04f1ac0426439f5efaea694eb72e85'
IMPLICIT='8227:2020:M2:T4:O03:D01';GEOM='8227:2020:M2:T4:O03:D03';STATIONARY='8227:2020:M1:T8:O04:D01';CLASSIFY='8227:2020:M1:T8:O04:D02'
BND='8227:2020:M1:T6:O06:D01';ALL='8227:2020:M1:T6:O06:D02';PRODUCT='8227:2020:M2:T4:O02:D01';ELEMENTARY='8227:2020:M2:T4:O01:D01'
def ev(page):
    p=W/'checks/r5/textbooks/Goldie-C4-118.png';return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[];corrections=[]
def add(n,page,note,parts,direct,components):
    for p in parts:
        kp=p.pop('key_page_override',page);p.update(source_pdf_page=page,source_evidence=ev(page),answer_pdf_page=kp,answer_printed_page=kp-14,key_evidence=ev(kp),review_date='2026-11-18')
    row={'item_id':f'8227:TB:Goldie:C4:Example:{n}','source_pdf_page':page,'notes':note,'assessed_8227_demand_ids':direct,'component_demand_ids':components,
      'mapping_rationale':'Implicit differentiation andthe actual stationary/gradient decisions are assessed. A parametric branch check used by the author to audit a singularity isnot a learner-assessed parametric demand. A node requires branch reasoning beyond setting the implicit numerator tozero.',
      'representation':'graph'if n==18 else'text','sketch_response_required':False,
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'within'if n==18 else'not applicable','quoted_value':note,
        'reason':'Bothangles arebounded0..πandthetrigargumentshavemultiplier1.'if n==18 else'Polynomialimplicitcurve,nottrigonometricrootfamilies.'},
       {'rule_id':'8227:LIMIT05','status':'not applicable','quoted_value':note,
        'reason':'Thedegree-fourdividendlimitisforpolynomialdivision,notacubicimplicitcurveoradegree-sixsubstitutionequation. No polynomial division is requested.'},
       {'rule_id':'8227:QUAL10','status':'within'if n==17 else'not applicable','quoted_value':note,'reason':'Actualpowersinthecubicarepositiveintegers.'if n==17 else'Trigimplicitcurve;no rational-power boundary.'}],
      'exam_style':False,'exam_style_basis':'Ordinary worked Example without examination attribution.',
      'precision_angle_check':{'source':'Exact radicals andradianmultiples ofπ. Four explicit sourcepoints must be checked individually.',
        'comparison':'KeepFy≠0for a regular implicit slope;whenFx=Fy=0,qualifythebranchratherthanaccept0/0aszero. Degree-sixeliminationdoesnotadd a division-scope exclusion.'},
      'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts}
    answers.append(row);return row
F='x**3+y**3-3*x*y'
p=value('i','0','3*x**2+3*y**2*p-3*(x*p+y)',118,
 'Treatyasy(x)anddifferentiatetheoriginalcurveequation. Normalisep=dy/dx;thetotalderivativeequationiszero. Thisformalrelationisvalidonalocaldifferentiablebranch,butneednotdetermineaslopeatasingularpoint.')
p['operation']={'kind':'implicit-expression-derivative','operands':[F]};p['normalised_notation']={'p':'dy/dx'}
p['author_answer_form']='3x²+3y²(dy/dx)=3(x(dy/dx)+y).'
p2=reasoning('ii','The regular horizontal-tangent point is(∛2,∛4). The origin also lies on a horizontal-tangent local branch,but it is a node with another vertical-tangent branch;the full curve has no unique dy/dx there.',
 'For a regular horizontal tangent,Fx=3x²−3y=0givesy=x². Substitution inF=0givesx³(x³−2)=0. AtB=(∛2,∛4),Fy=3y²−3x=3∛2≠0,sothe horizontal slope isvalid. AtA=(0,0),bothFxandFyvanish;the source necessary condition alone isinsufficient. The rational parametrisationX=3t/(1+t³),Y=3t²/(1+t³)lies onF=0andhas tangentvector(3,0)att=0. Swapping these coordinates gives another local parametrisation with tangentvector(0,3)at the origin. This verifies a horizontal branch there whiledisclosing the singularity omitted by the source explanation.',118,'key incomplete')
X='3*x/(1+x**3)';Y='3*x**2/(1+x**3)'
p2['additional_operations']={'elimination_factorisation':{'kind':'identity','operands':['factor((x**3+y**3-3*x*y).subs(y,x**2))']},
 'regular_point_curve_residual':{'kind':'identity','operands':['(x**3+y**3-3*x*y).subs({x:2**(1/3),y:2**(2/3)})']},
 'regular_Fy':{'kind':'identity','operands':['diff(x**3+y**3-3*x*y,y).subs({x:2**(1/3),y:2**(2/3)})']},
 'singular_partial_derivatives':{'kind':'identity','operands':['Tuple(diff(x**3+y**3-3*x*y,x).subs({x:0,y:0}),diff(x**3+y**3-3*x*y,y).subs({x:0,y:0}))']},
 'horizontal_branch_curve_residual':{'kind':'identity','operands':[f'cancel(({X})**3+({Y})**3-3*({X})*({Y}))']},
 'horizontal_branch_tangent_vector':{'kind':'identity','operands':[f'Tuple(diff({X},x).subs(x,0),diff({Y},x).subs(x,0))']},
 'vertical_branch_tangent_vector':{'kind':'identity','operands':[f'Tuple(diff({Y},x).subs(x,0),diff({X},x).subs(x,0))']}}
p2['additional_operation_expected']={'elimination_factorisation':'x**3*(x**3-2)','regular_point_curve_residual':'0','regular_Fy':'3*2**(1/3)',
 'singular_partial_derivatives':'Tuple(0,0)','horizontal_branch_curve_residual':'0','horizontal_branch_tangent_vector':'Tuple(3,0)','vertical_branch_tangent_vector':'Tuple(0,3)'}
add(17,118,'Forx³+y³=3xy,differentiateimplicitlyandhencefindanystationarypoints. Thesourceincludesoriginand(∛2,∛4);theoriginneedsanexplicitsingular-branchqualificationbecausebothimplicitpartialsarezero.',[p,p2],[IMPLICIT,GEOM,STATIONARY],[PRODUCT])
F='sin(x)+sin(y)-1'
p=value('i-derivative','0','-cos(x)/cos(y)',119,'DifferentiateF=0onaregularbranchandisolateitsfinitegradientwherecosy≠0.')
p['operation']={'kind':'implicit-derivative','operands':[F]};p['original_common_domain']='0≤x,y≤π,onF=0wherecosy≠0.'
p2=value('i-stationary-points','0','FiniteSet(Tuple(pi/2,0),Tuple(pi/2,pi))',119,
 'Foraregularhorizontalgradient,cosx=0givesx=π/2astheonlyboundedx. ThenoriginalF=0requiressiny=0,sobothy=0andπareincluded;Fy=±1isnonzeroatboth. Checktheoriginalequation,notmerelythederivativenumerator.')
p2['operation']={'kind':'identity','operands':['FiniteSet(Tuple(pi/2,asin(0)),Tuple(pi/2,pi-asin(0)))']}
p2['additional_operations']={'bounded_x_candidates':{'kind':'bounded-trig-equation','operands':['cos(x)','0','pi']},
 'bounded_y_candidates_after_x':{'kind':'bounded-trig-equation','operands':['sin(x)','0','pi']},
 'original_and_regular_checks':{'kind':'identity','operands':['Tuple((sin(x)+sin(y)-1).subs({x:pi/2,y:0}),(sin(x)+sin(y)-1).subs({x:pi/2,y:pi}),cos(0),cos(pi))']}}
p2['additional_operation_expected']={'bounded_x_candidates':'FiniteSet(pi/2)','bounded_y_candidates_after_x':'FiniteSet(0,pi)','original_and_regular_checks':'Tuple(0,0,1,-1)'}
points=[('pi/6','pi/6'),('pi/6','5*pi/6'),('5*pi/6','pi/6'),('5*pi/6','5*pi/6')]
residuals=','.join(f'(sin(x)+sin(y)-1).subs({{x:{a},y:{b}}})'for a,b in points)
p3=value('ii-point-checks',f'Tuple({residuals})','Tuple(0,0,0,0)',120,
 'Independently substituteeachofthefourstatedpointpairsintheoriginalequation. Bothsinπ/6andsin5π/6equal1/2,butthecosineshaveoppositesigns.')
p3['check_mode']='show/prove'
slopes=','.join(f'(-cos(x)/cos(y)).subs({{x:{a},y:{b}}})'for a,b in points)
p4=value('ii-gradients',f'Tuple({slopes})','Tuple(-1,1,1,-1)',120,
 'Computeoriginalpartialderivativesandthefinitegradientateachverifiedpointin thegivenorder. Cosinequadrants,notnumericaldenominatorsalone,determine the signs.')
p5=reasoning('ii-classification','(π/2,0)is a minimum and(π/2,π)is a maximum on their local branches.',
 'The original boxboundsalreadygive0≤y≤π. Near the lower branch,cosy>0whilecosxchangespositive-to-negativeacrossπ/2;therefore−cosx/cosychangesnegative-to-positive. Near the upper branch,cosy<0so thegradientchangespositive-to-negative. These are local sign arguments,not a claim that four isolated sampledslopesaloneprovearbitrarycurvebehaviour.',120,'matches')
row=add(18,119,'Forsinx+siny=1in0≤x,y≤π,usingthegivenclosedcurve:deriveimplicitgradientandallstationarycoordinates;verifyfourstatedπ/6/5π/6pointpairs,findtheirgradients,andconcludethenaturesofthetwostationarypoints.',[p,p2,p3,p4,p5],[IMPLICIT,GEOM,STATIONARY,CLASSIFY,BND,ALL],[ELEMENTARY])
corrections.append({'item_id':row['item_id'],'continuation_pdf_pages':[120]})
figures=[]
for n,page,label,note,parent,teaches,checks,method in[
 (27,118,'Figure4.7 folium andstationary labels','Thefoliumx³+y³=3xyhasanodeAattheoriginandaregularhorizontal-tangentB=(∛2,∛4). ThesourcelabelsAandBasstationarywithoutdisclosingthatAalsohasaverticaltangentbranch.','Example:17',[IMPLICIT,GEOM,STATIONARY],
  [('Tuple((x**3+y**3-3*x*y).subs({x:0,y:0}),(x**3+y**3-3*x*y).subs({x:2**(1/3),y:2**(2/3)}))','Tuple(0,0)')],
  'Parentbranchparametrisationsindependentlyverifybothorigintangentsandtheloop. Thegivenpointsetispreservedwithasourcequalification,notdiscardedbyblindlydividingat0/0.'),
 (28,119,'Figure4.8 bounded implicit sine curve','sinx+siny=1in[0,π]²hasbottom(π/2,0),top(π/2,π),andsideverticaltangencies(0,π/2),(π,π/2). Theroundedcloseddiamondisnotafunctionyofxoverthewholebox.','Example:18',[IMPLICIT,GEOM,STATIONARY,CLASSIFY],
  [('Tuple(sin(pi/2)+sin(0)-1,sin(pi/2)+sin(pi)-1,sin(0)+sin(pi/2)-1,sin(pi)+sin(pi/2)-1)','Tuple(0,0,0,0)')],
  'Theoriginalboxandimplicitregularitydistinguishhorizontalextremafromtheverticalsidetangencies. Sourcekeyslopesatfourintermediatepointsagreewiththeanalyticalbranchsigns.'),
 (29,120,'Figure4.9 lower-branch slope summary','Threeillustratedlower-branchslopeschangefromnegativeatx=π/6,tozeroatπ/2,topositiveat5π/6,showingthelocalminimumaty=0.','Example:18',[IMPLICIT,CLASSIFY],
  [('Tuple(-cos(pi/6)/cos(pi/6),-cos(pi/2)/cos(0),-cos(5*pi/6)/cos(pi/6))','Tuple(-1,0,1)')],
  'Acompressedworked-solutiondiagram,notanadditionalsketchrequest. Parentpointchecksandnearbybranchsignsjustifyitsthreegradients.'),
 (30,120,'Figure4.9 upper-branch slope summary','Threeillustratedupper-branchslopeschangefrompositiveatx=π/6,tozeroatπ/2,tonegativeat5π/6,showingthelocalmaximumaty=π.','Example:18',[IMPLICIT,CLASSIFY],
  [('Tuple(-cos(pi/6)/cos(5*pi/6),-cos(pi/2)/cos(pi),-cos(5*pi/6)/cos(5*pi/6))','Tuple(1,0,-1)')],
  'Upperbranchcosyisnegative,sothecorrespondingslopepatternreverses. Thisworkedrepresentationisnotseparatelearnerpractice.')]:
    results=[]
    for expr,target in checks:
        got=compute({'kind':'identity','operands':[expr]});assert equivalent(got,expression(target)),(label,got)
        results.append({'operation':{'kind':'identity','operands':[expr]},'source_normalised':target,'derived':str(got)})
    figures.append({'item_id':f'8227:TB:Goldie:C4:Teaching-figure:{n}','item_kind':'given-figure'if n==28 else'teaching-figure','exercise':'Teaching figure','item_number':str(n),
     'pdf_page':page,'printed_page':page-14,'source_label':label,'notes':note,'what_it_shows':note,'assessed_8227_demand_ids':[],'component_demand_ids':[],
     'teaches_8227_demand_ids':teaches,'representation':'graph','source_evidence':ev(page),'parent_item_id':'8227:TB:Goldie:C4:'+parent,'learner_display':False,
     'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'within'if n>=28 else'not applicable','quoted_value':note,
       'reason':'Actualsineanglesbounded0..πwithmultiplier1.'if n>=28 else'Algebraicfolium;notaperiodicequation.'}],
     'value_level_scope_review_status_r5':'authorcurve/branch/slopefeaturesread2026-11-18;independentcheckpending',
     'exam_representation_check':{'status':'finalcross-book/examinationcomparisonpending','examination_part_ids':[],'relation':'Internaltextbookgiven/workedgraph;notofficialmarkingorexaminationfrequency.'},
     'mathematical_feature_review':{'status':'authorsourcerenderandexplicitcurve/branchchecks;independentacceptancepending','method':method,'checks':results}})
# Page120alsohasExercise4D1;thefollowingsegmentownsthecompletepagecensus.
pages=[{'pdf_page':page,'printed_page':page-14,'chapter':4,'page_status':'items enumerated',
 'item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],
 'continuation_item_ids':[],'source_evidence':ev(page),'non_item_content':'AllExamples17–18startsandgiven/workedgraphsrecorded. Example18continues120withanswerdiagrams;page120censusawaitsExercise4D1. Theintroductoryclassificationparagraphisproseadvice,notaseparatetask.',
 'reader':'Codex author','date':'2026-11-18'}for page in[118,119]]
if __name__=='__main__':
    for name,data in[
     ('answers-Goldie-C4-implicit-stationary.json',{'scope':'EveryexplicitpartofExamples17–18,includingthesingular-originqualificationandallfourpoint/gradientchecks.','items':answers}),
     ('census-Goldie-C4-implicit-stationary.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':4,'source_path':SRC,'source_sha256':SHA,
      'scope':'Completepages118–119;workedfigures120recordedbutitscompletecensusawaitstheexercise.','new_items':figures,'corrections':corrections,'pages':pages})]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures')
