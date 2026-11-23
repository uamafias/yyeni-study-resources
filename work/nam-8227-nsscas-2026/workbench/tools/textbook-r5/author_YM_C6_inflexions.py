"""YM298–301: stationary inflexions,classification and explicit sketch tasks."""
import json
import sympy as sp
import author_YM_C6_opening as h
from author_YM_C6_opening import W,SRC,SHA,pp,ev,v,reasoning,fig,figures,compute,expression,equivalent
h.answers.clear();h.new.clear();h.corrections.clear();figures.clear()
answers=h.answers;new=h.new;corrections=h.corrections
POWER=h.POWER;POINT='8227:2020:M1:T8:O04:D01';NATURE='8227:2020:M1:T8:O04:D02';extra=h.extra
def responses(prefix,fn,cases,kp,sketch=False,features=None):
 """Cases are separately transcribed source coordinates and nature labels."""
 key='FiniteSet('+','.join(f'Tuple({x0},{y0})'for typ,x0,y0 in cases)+')'
 p=v(prefix+'coordinates','0',key,kp,'Differentiate the ORIGINAL function,solve for all stationary abscissas,and evaluate their ordinates in the ORIGINAL function. Compare the independently transcribed source coordinates;do not evaluate the derivative to obtain an ordinate.')
 p['operation']={'kind':'stationary-points','operands':[fn]};p.update(assessed_8227_demand_ids=[POINT],component_demand_ids=[POWER]);parts=[p]
 labels='; '.join(f'{typ}({x0},{y0})'for typ,x0,y0 in cases)
 p=reasoning(prefix+'nature',labels,'Use derivative sign changes at every original stationary root. Maximum changes+to−,minimum−to+,andstationaryinflexion retains the first-derivative sign while the curvature changes. A zero SECOND derivative alone is inconclusive. Source first-derivative tables or second-derivative tests are retained;the independent exact checks below verify the sign/nature from the ORIGINAL polynomial.',kp,'matches')
 p.update(assessed_8227_demand_ids=[NATURE],component_demand_ids=[POWER],source_nature_labels=[dict(nature=typ,x=x0,y=y0)for typ,x0,y0 in cases])
 f=expression(fn);x=expression('x');d1=sp.diff(f,x);d2=sp.diff(f,x,2)
 for index,(typ,x0,y0)in enumerate(cases):
  root=expression(x0);left=root-sp.Rational(1,100);right=root+sp.Rational(1,100)
  signs=(sp.sign(d1.subs(x,left)),sp.sign(d1.subs(x,right)))
  if typ=='maximum':assert signs==(1,-1)and d2.subs(x,root)<0
  elif typ=='minimum':assert signs==(-1,1)and d2.subs(x,root)>0
  else:assert typ=='stationary inflexion'and signs in[(1,1),(-1,-1)]and d2.subs(x,root)==0 and d2.subs(x,left)*d2.subs(x,right)<0
  extra(p,f'critical-{index}-derivative',f'diff({fn},x).subs(x,{x0})','0')
  p.setdefault('independent_nature_checks',[]).append(dict(x=x0,first_derivative_left=str(d1.subs(x,left)),first_derivative_right=str(d1.subs(x,right)),second_derivative_at=str(d2.subs(x,root)),second_derivative_left=str(d2.subs(x,left)),second_derivative_right=str(d2.subs(x,right)),method='Exact local polynomial derivative/curvature signs at±1/100around each separately verified stationary root.'))
 parts.append(p)
 if sketch:
  p=reasoning(prefix+'sketch','; '.join(features),'Sketch the ORIGINAL polynomial using its leading-term tails,original yintercept,and all verified stationary coordinates/types. Do not turn an inflexion into an extremum or make a double root cross the axis. These listed features are derived from the original function and compared with the source graph;they are not official award criteria.',kp,'sketch')
  p.update(assessed_8227_demand_ids=[POINT,NATURE],response_format='sketch',credited_features=features,author_feature_basis='Original function and verified source stationary points;source sketch checked on rendered page.')
  extra(p,'original-yintercept',f'({fn}).subs(x,0)',str(f.subs(x,0)));parts.append(p)
 return parts
def add(kind,n,page,note,parts):
 r=h.add(kind,n,page,note,parts,[POINT,NATURE],[POWER],powers=[p['operation']['operands'][0]for p in parts if p.get('operation',{}).get('kind')=='stationary-points'])
 r.update(representation='text',sketch_response_required=any(p.get('response_format')=='sketch'for p in parts),mapping_rationale='The GIVEN is an algebraic function in text,even when the requested RESPONSE is a sketch or the solution contains a graph. Coordinates,natureandvisualfeaturesremain separate outputs. Stationary inflexions are prescribed8227content;they are neither maxima nor minima.')
 for p in parts:p['given_representation']='text'
 return r

parts=responses('a-','-x**3-3*x**2+9*x+10',[('minimum','-3','-17'),('maximum','1','15')],621,True,['Negative-leading cubic,lefttailup/righttaildown','Minimum(−3,−17)','Maximum(1,15)','yintercept10','Threecrossingsconsistentwiththeextrema'])
parts+=responses('b-','x**3-4*x**2+4*x',[('maximum','Rational(2,3)','Rational(32,27)'),('minimum','2','0')],622,True,['Positive-leading cubic','Maximum(2/3,32/27)','Minimum/touchingdouble-root(2,0)','Crossingrootand yintercept(0,0)'])
add('Try-Now',26,298,'For two cubics,locate,classifyANDSKETCHeach,including the factorised touching-root case x(x−2)².',parts)
parts=responses('','x**3+1',[('stationary inflexion','0','1')],298,True,['Increasingcubicwithlefttaildown/righttailup','Stationaryinflexion(0,1)andhorizontal tangent','yintercept1','Crossingxintercept−1'])
r=add('Example',27,298,'Find,classifyandsketch the stationary inflexion ofx³+1. Source nature conclusioncopies(0,−1),contradicting its own correct coordinate calculation and graph(0,1).',parts)
r['source_label_warning']='Only the later nature sentence misprints ordinate−1;the stationary coordinate calculation and finalgraphcorrectlyuse+1. The inflexion classification itself is correct.'
parts=responses('a-','x**3-1',[('stationary inflexion','0','-1')],622,True,['Increasingcubic','Stationaryinflexion(0,−1)','yintercept−1','Crossingrootx1'])
parts+=responses('b-','-x**3',[('stationary inflexion','0','0')],622,True,['Decreasingnegative-leadingcubic','Horizontalstationaryinflexionatorigin','Triplecrossingroot0','No maximum/minimum'])
add('Try-Now',27,299,'Forx³−1and−x³,locateandclassifythe stationaryinflexion andsketcheachcurve;the derivative retains its sign across0.',parts)
add('Example',28,300,'Use the second derivative toclassifythe stationary points of−9x³+45x²−72x+36andSKETCHthe cubic.',responses('','-9*x**3+45*x**2-72*x+36',[('minimum','Rational(4,3)','-Rational(4,3)'),('maximum','2','0')],300,True,['Negative-leadingcubic','yintercept36','Minimum(4/3,−4/3)','Maximum/touchingroot(2,0)','Simplecrossingroot1']))
add('Try-Now-28',1,300,'Locate,classifyandsketch2x³+3x²−12x+7,including the minimum touching theaxis atx1.',responses('','2*x**3+3*x**2-12*x+7',[('maximum','-2','27'),('minimum','1','0')],622,True,['Positive-leadingcubic','Maximum(−2,27)','Minimum/touchingroot(1,0)','yintercept7','Othercrossingroot−7/2']))
add('Try-Now-28',2,300,'Locate,classifyandsketchx³−4x²−11x+30,retaining exact fractional stationary coordinates.',responses('','x**3-4*x**2-11*x+30',[('maximum','-1','36'),('minimum','Rational(11,3)','-Rational(400,27)')],622,True,['Positive-leadingcubic','Maximum(−1,36)','Minimum(11/3,−400/27)','yintercept30','Threecrossingsat−3,2,5']))
add('Example',29,301,'Forx4−4x³+2findstationarycoordinatesandnature ONLY. Thezero-second-derivativepoint0requiresa sign/curvature test;no sketch is requested.',responses('','x**4-4*x**3+2',[('stationary inflexion','0','2'),('minimum','3','-25')],301))
parts=responses('a-','x**4-2*x**3',[('stationary inflexion','0','0'),('minimum','Rational(3,2)','-Rational(27,16)')],622)
parts+=responses('b-','x**2*(3-x)',[('minimum','0','0'),('maximum','2','4')],622)
add('Try-Now-29',1,301,'Locateandclassifyallstationarypointsofthe quarticx4−2x³andcubicx²(3−x);no sketches are requested.',parts)

refs=[(37,298,'Two stationary-inflexion sign sketches','Firstderivativepositive→zero→positive,ornegative→zero→negative,doesnotreverse direction. For these polynomialinflexions the curvature changes;zero derivativeorzero secondderivativealone is insufficient.',[POINT,NATURE],'graph',None),(38,298,'Example27 first-derivative sign table','Forx³+1,derivative3x²gives0.03at±0.1and0at0. Theordinatefromthe original functionis+1;the later−1sentenceis a copylabeldefect.',[NATURE],'table','Example:27'),(39,298,'Example27 worked inflexion sketch','Source graphcorrectlylabels(0,1)withhorizontal tangent,increasingonbothsides. It is a solution illustration,not a given-inputdiagram.',[POINT,NATURE],'graph','Example:27'),(40,299,'Maximum/second-derivative explanatory pair','At an ordinarynondegenerate stationarymaximum,fprime0andfsecond<0. The sketchcomparesoriginalfunctionanditsderivative. A secondderivative0wouldnotbe classifiedbythiscriterion.',[NATURE],'graph',None),(41,299,'Minimum/second-derivative explanatory pair','At an ordinarynondegenerate stationaryminimum,fprime0andfsecond>0. Itis a local criterion,notautomatically a globalminimum over everydomain.',[NATURE],'graph',None),(42,300,'Example28 worked cubic sketch','Original−9x³+45x²−72x+36,yintercept36,min(4/3,−4/3),max(2,0),negativeleadingtails. Source sketchpreserves thetouchingmaximumroot2.',[POINT,NATURE],'graph','Example:28'),(43,301,'Example29 zero-second-derivative sign table','Atstationaryx0forx4−4x³+2,fsecond0is inconclusive. Sourcefirst-derivative samples−0.124and−0.116remainnegative,andcurvaturechanges,so(0,2)isa stationaryinflexion. The other stationarypoint(3,−25)isminimum.',[NATURE],'table','Example:29')]
for n,page,label,note,teaches,rep,parent in refs:
 fig(n,page,label,note,teaches,rep,[],parent);r=figures[-1];r['item_id']=r['item_id'].replace('Goldie:C5:','YM:C6:');r['parent_item_id']=r['parent_item_id'].replace('Goldie:C5:','YM:C6:')if r['parent_item_id']else None;r.update(printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[])
 r['item_kind']='teaching-figure'
 r['mathematical_feature_review']['method']='Inspect actual point labels,root touch/crossing,derivative-sign table and tail directions. Independently compute stationary coordinates,local derivative signs and curvature;separate solution graphs from given-input representations.'
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=6,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-19',non_item_content='AllTry26/27,Examples27–29,Try28Q1/2,Try29Q1a/bandsevenreferencepanelsare enumerated over298–301. Explicit sketch requests are retained;Example29/Try29doNOTasksketches. First/secondderivativeexplanationsareworking,not additionalnumberedquestions.',scope_screen='Stationarypointlocation,maximum/minimum/inflexionclassification,andexplicitpolynomialsketchresponsesare prescribed. Nonstationaryinflexionx2inExample29isnotpartofitsstationarypointrequest.')for page in range(298,302)]
if __name__=='__main__':
 for name,data in [('answers-YM-C6-inflexions.json',dict(scope='All298–301explicit tasks.',items=answers)),('census-YM-C6-inflexions.json',dict(book='YM',book_id='8227-SRC-017',chapter=6,source_path=SRC,source_sha256=SHA,scope='Complete298–301page census.',new_items=new+figures,corrections=corrections,pages=pages))]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for r in answers:
  for p in r['subparts']:
   if 'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(r['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(r['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
