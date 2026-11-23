"""Goldie PDF78–81: every compound-angle task and initial double-angle derivation."""
import hashlib,json
from pathlib import Path
from author_YM_C4_trig_graphs import value,reasoning
from author_YM_C4_composite_equations import roots,transform
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2]
SRC='sources/namibia/nsscas/8227-mathematics/textbooks/Goldie_Pure-Mathematics-2-and-3_2nd-edition_2018.pdf'
SHA='f030d64259ffe233a7408d2a64dea21c0a04f1ac0426439f5efaea694eb72e85'
COMP='8227:2020:M2:T3:O02:D02';DOUBLE='8227:2020:M2:T3:O02:D03';PYTH='8227:2020:M2:T3:O02:D01';EVAL='8227:2020:M2:T3:O02:D05'
EXACT='8227:2020:M1:T6:O03:D01';BND='8227:2020:M1:T6:O06:D01';ALL='8227:2020:M1:T6:O06:D02';TRANS='8227:2020:M1:T6:O05:D02'
TRI='8227:PRIOR:NSSCO:right-triangle-trig';COORD='8227:PRIOR:NSSCO:coordinate-geometry';D='(x*pi/180)'
def ev(page):
    p=W/f'checks/r5/textbooks/{"Goldie-key-C3-337"if page==340 else"Goldie-C3-78"}.png'
    return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[];new=[]
ATTR={7:'Cambridge International AS & A Level Mathematics9709,Paper21Q7,November2014',
 8:'Cambridge International AS & A Level Mathematics9709,Paper3Q5,November2007',
 9:'Cambridge International AS & A Level Mathematics9709,Paper32Q4,November2009',
 10:'Cambridge International AS & A Level Mathematics9709,Paper3Q4,June2008',
 11:'Cambridge International AS & A Level Mathematics9709,Paper33Q6,November2015'}
def add(kind,n,page,note,parts,direct,components=None,rep='text',new_item=False):
    for p in parts:
        kp=p.pop('key_page_override',340)
        p.update(source_pdf_page=page,source_evidence=ev(page),answer_pdf_page=kp,
          answer_printed_page=kp-14,key_evidence=ev(kp),review_date='2026-11-18')
    equation=kind=='Exercise-3B'and n in[4,5,8,9,10]
    attributed=kind=='Exercise-3B'and n in ATTR
    row={'item_id':f'8227:TB:Goldie:C3:{kind}:{n}','source_pdf_page':page,'notes':note,
      'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],
      'mapping_rationale':'Classify required compound-angle expansion/recognition,exact evaluation, bounded solving or connected geometry. Retain original conditions and symbol roles. Do not silently repair φ to θ or interchange α and β to make a key match. Numerical checks are not universal proofs.',
      'representation':rep,'sketch_response_required':False,
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'within'if equation else'not applicable',
        'quoted_value':note,'reason':'Original bounded equations use small integer argument multipliers1,including fixed30°/45°/60°/120°shifts. Ratio powers and algebraic tangent substitutions are not extra input multipliers.'if equation else'No complete periodic root set is requested; formal identities and exact ratio outputs are not general solutions.'},
       {'rule_id':'8227:LIMIT02','status':'within'if equation else'not applicable','quoted_value':note,
        'reason':'Every original finite interval and pole is kept. Question9requires both ordered angle pairs in0°<α,β<180°.'if equation else'The task asks an expression/value/proof discussion,not unrestricted angle families.'}],
      'exam_style':attributed,
      'exam_style_basis':('Book attribution: '+ATTR[n]+'. This is a textbook attribution lead; the original examination PDF is not reverified by this item record. Textbook text remains internal.')if attributed else'Unattributed Example/Exercise/Prompt/exposition; no examination provenance or explicit exam-style label.',
      'precision_angle_check':{'source':'3B4 uses degrees0..180;3B5uses radians0..π;decimal keys use their written precision.3B1requires surds,and3B7/11forbid a calculator.',
        'comparison':'Preserve exact coefficients/ratio branches before rounding. Original tangent poles are distinct from cosθ=0 introduced by a substitution; retain a valid θ=90°branch in3B4(iii).'},
      'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts}
    if not direct:row['evidence_role']='prerequisite/supporting teaching exposition; no explicit assessed demand claimed'
    answers.append(row)
    if new_item:new.append({'item_id':row['item_id'],'item_kind':'worked-derivation','exercise':kind,'item_number':str(n),
      'pdf_page':page,'printed_page':page-14,'notes':note,'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],
      'representation':rep,'teaches_8227_demand_ids':components or direct,'source_evidence':ev(page),'answer_key':{'available':True,'pdf_pages':[page],'printed_pages':[page-14],'locator':'Inline worked derivation'},'learner_display':False})
    return row
def expand(label,family,a,b,key,kp=340):
    p=value(label,'0',key,kp,
      'Independently apply the requested compound-angle formula to the two original arguments. Evaluate only the constant special-angle coefficients, keeping the unknown argument/multiple intact. Compare equivalent exact forms on the common domain.')
    p['operation']={'kind':'trig-compound-expand','family':family,'operands':[a,b]}
    p['original_common_domain']='All real angles for sine/cosine. Tangent expansion additionally needs both individual tangent inputs andthe combined tangent/denominator defined.'
    return p

p=value('answer','cos(x)*cos(3*x)-sin(x)*sin(3*x)','cos(4*x)',78,
 'Recognise cosAcosB−sinAsinB ascos(A+B),withA=θandB=3θ. Independent symbolic simplification confirms cos4θ; reverse-pattern recognition is the learner decision.')
add('Example',3,78,'Simplify cosθcos3θ−sinθsin3θ by recognising the cosine-addition pattern in reverse.',[p],[COMP,EVAL])
parts=[expand('i','sin','pi/4','pi/6','sqrt(3)/(2*sqrt(2))+1/(2*sqrt(2))'),
 expand('ii','cos','pi/2','pi/4','-1/sqrt(2)'),
 expand('iii','tan','pi/4','-pi/6','(sqrt(3)-1)/(sqrt(3)+1)'),
 expand('iv','tan','pi/4','pi/6','(sqrt(3)+1)/(sqrt(3)-1)')]
row=add('Exercise-3B',1,78,'Use compound-angle formulas to write sin75°,cos135°,tan15°,tan75°as exact surds,using the specified45°±30°and90°+45°decompositions.',parts,[COMP,EVAL,EXACT])
row['direct_demand_aspects']={EXACT:'Part(ii)directly evaluates the45°-related135°angle. The75°/15°compound outputs do not establish broader Module1special-angle coverage.',COMP:'The source explicitly requires compound-angle formulas,not a calculator or an unrelated exact-value shortcut.'}
parts=[expand('i','sin','x','pi/4','(sin(x)+cos(x))/sqrt(2)'),
 expand('ii','cos','x','-pi/6','(sqrt(3)*cos(x)+sin(x))/2'),
 expand('iii','sin','pi/3','-x','(sqrt(3)*cos(x)-sin(x))/2'),
 expand('iv','cos','2*x','pi/4','(cos(2*x)-sin(2*x))/sqrt(2)'),
 expand('v','tan','x','pi/4','(tan(x)+1)/(1-tan(x))'),
 expand('vi','tan','x','-pi/4','(tan(x)-1)/(1+tan(x))')]
add('Exercise-3B',2,78,'Expand sin(θ+45°),cos(θ−30°),sin(60°−θ),cos(2θ+45°),tan(θ+45°),tan(θ−45°). Retain original tangent common domains.',parts,[COMP],[EXACT])

p=value('i','sin(2*x)*cos(y)-cos(2*x)*sin(x)','sin(x)',340,
 'Read the actual source firstcosine ascosφ,whilethe final sine is sinθ. The key sinθwouldfollowonlyifthe source cosφwerecosθ(or under a special relation). Preserve literal two-angle text; independently rewrite it as sinθ+sin2θ(cosφ−cosθ).')
p['assertions']=[{'expression':'sin(2*x)*cos(y)-cos(2*x)*sin(x)-(sin(x)+sin(2*x)*(cos(y)-cos(x)))','expected':'0'},
 {'expression':'sin(pi/3)*cos(pi/3)-cos(pi/3)*sin(pi/6)-sin(pi/6)','expected':'(sqrt(3)-3)/4'}]
parts=[p,value('ii','cos(y)*cos(7*y)-sin(y)*sin(7*y)','cos(8*y)',340,
 'Recognise the cosine-addition pattern with argumentsφand7φ,so the simplified result iscos8φ.'),
 value('iii','sin(2*pi/3)*cos(pi/3)+cos(2*pi/3)*sin(pi/3)','0',340,
 'Use sine addition120°+60°=180°,whose sine is0; verify independently from exact ratios.'),
 value('iv','cos(x)**2-sin(x)**2','cos(2*x)',340,
 'Recognise cosine addition with equal arguments;cos²θ−sin²θ=cos2θ.')]
row=add('Exercise-3B',3,79,'Simplify four expressions. Literal(i)is sin2θcosφ−cos2θsinθ,with mismatchedφ/θ;its key assumescosθinstead. (ii)usesφand7φ;(iii)adds120°and60°;(iv)is the equal-angle cosine form.',parts,[COMP,EVAL,DOUBLE])
row['source_label_warning']='Part(i)has a source symbol mismatch,confirmedat4x. Do not silently substituteφ=θ. The otherparts provide valid compound/double-angle evidence.'

parts=[]
for label,original,key,branch in[
 ('i',f'cos(pi/3+{D})-sin({D})','FiniteSet(15)',[('tan','x','2-sqrt(3)',1)]),
 ('ii',f'sin(pi/4-{D})-cos({D})','FiniteSet(315/2)',[('tan','x','1-sqrt(2)',1)]),
 ('iii',f'tan(pi/4+{D})-tan(pi/4-{D})','FiniteSet(0,180)',[('sin','2*x','0',1)]),
 ('iv',f'2*sin({D})-3*cos({D}-pi/3)',['111.7'],[('tan','x','3/(4-3*sqrt(3))',1)]),
 ('v',f'sin({D})-cos({D}+2*pi/3)','FiniteSet(165)',[('tan','x','sqrt(3)-2',1)])]:
    p=roots(label,original,key,340,branch,hi='180',approx=isinstance(key,list))
    if label=='iii':p.update(difference_disposition='key incomplete',difference_reason='The printed key omitsθ=90°. At90°,theoriginal tangent values aretan135°=tan(−45°)=−1,bothdefined. Clearing the original denominators gives sin2θ=0; excluding its45°/135°poles leaves0°,90°,180°.')
    parts.append(p)
add('Exercise-3B',4,79,'Solve five compound-angle equations on0°≤θ≤180°. In(iii)tan(45°+θ)=tan(45°−θ),θ=90°is valid despite tanθbeingundefined;the source key misses this branch.',parts,[COMP,TRANS,BND,ALL])
parts=[roots('i','sin(x+pi/4)-cos(x)','FiniteSet(pi/8)',340,[('tan','x','sqrt(2)-1',1)],unit='radian',hi='pi'),
 roots('ii','2*cos(x-pi/3)-cos(x+pi/2)',['2.79'],340,[('tan','x','-1/(sqrt(3)+1)',1)],unit='radian',hi='pi',approx=True)]
add('Exercise-3B',5,79,'On0≤θ≤πsolve sin(θ+π/4)=cosθand2cos(θ−π/3)=cos(θ+π/2). Keep exactπ/8for(i),andthe derived non-special radian root for(ii).',parts,[COMP,TRANS,BND,ALL])

parts=[value('i:sin','Abs(-4-0)/sqrt((-4-0)**2+(1-4)**2)','4/5',79,
 'AtB,the downward verticalBPandBAform acuteα. Horizontal magnitude4andvertical3givehypotenuse5,so sinα=4/5.'),
 value('i:cos','Abs(1-4)/sqrt((-4-0)**2+(1-4)**2)','3/5',340,
 'Use the same positive3–4–5triangle atB;cosα=3/5.'),
 value('ii:sin','Abs(6-0)/sqrt((6-0)**2+(-2-4)**2)','sqrt(2)/2',340,
 'BC has equal positive horizontal/downward-vertical magnitudes6,soβ=45°andsinβ=1/√2.'),
 value('ii:cos','Abs(-2-4)/sqrt((6-0)**2+(-2-4)**2)','sqrt(2)/2',340,
 'The equal-leg right triangle givescosβ=1/√2.'),
 expand('iii','sin','atan(4/3)','pi/4','7/(5*sqrt(2))',79),
 expand('iv:tan','tan','atan(4/3)','pi/4','-7',79)]
for p in parts:
    if p['subpart']in['i:sin','iii','iv:tan']:p['check_mode']='show/prove'
for p in parts:
    if p['subpart'].startswith('i:'):p['source_assessed_part_id']='i'
    if p['subpart'].startswith('ii:'):p['source_assessed_part_id']='ii'
p=reasoning('iv:meaning','The negative tangent indicates the obtuse angleα+βbetween90°and180°,not a negative geometric angle.',
 'αandβareacuteinteriorpiecesofangleABC,sotheirsumisbetween0°and180°. The dot product BA·BC=(−4)(6)+(−3)(−6)=−6isnegative,soABCisobtuse. Its sine7/(5√2)ispositiveandcosine−1/(5√2)isnegative,consistentwithtan=−7.',340,'matches')
p['additional_operations']={'independent_angle_cosine':{'kind':'identity','operands':['(-4*6+(-3)*(-6))/(sqrt(4**2+3**2)*sqrt(6**2+6**2))']}}
parts.append(p)
add('Exercise-3B',6,79,'GivenA(−4,1),B(0,4),C(6,−2)andP(0,1),use the markedα,βatBtofindtheir exactsin/cosvalues,show sin(α+β)=7/(5√2),show tan(α+β)=−7,andinterpretthenegativevalue.',parts,[COMP,EXACT],[TRI,COORD],rep='diagram')

p=transform('i:reduction','2*tan(x)**2+sec(x)**2-5+4*tan(x)','3*tan(x)**2+4*tan(x)-4',[], 'cosα != 0;source0°<α<90°',80)
p2=value('i:tan','0','FiniteSet(2/3)',340,
 'From the independently verified quadratic3t²+4t−4=0,find all real t andkeep only t>0 becauseαisacute. This gives the unique admissibletanα=2/3,not the negative root−2.')
p2['operation']={'kind':'polynomial-roots-in-interval','operands':['3*x**2+4*x-4','0','oo']}
p2['source_assessed_part_id']='i';p['source_assessed_part_id']='i'
p3=value('ii','1/((1/6-2/3)/(1+(1/6)*(2/3)))','-20/9',340,
 'The sourcecot(α+β)=6gives tan(α+β)=1/6. Solving the compound formula for tanβwithtanα=2/3gives−9/20,so cotβ=−20/9. No numerical angle or extra periodic family is needed.')
p3['dependency']={'source_part':'i','role':'Use the selected acute tanαbranch before recovering the exact cotβ.'}
add('Exercise-3B',7,80,'For0°<α<90°,2tan²α+sec²α=5−4tanα. Show3tan²α+4tanα−4=0andfindexacttanα;then givencot(α+β)=6findexactcotβwithoutacalculator.',[p,p2,p3],[PYTH,COMP,EVAL])

p=transform('i','(tan(pi/4+x)-tan(x)-2)*(1-tan(x))','tan(x)**2+2*tan(x)-1',[],
 'cosx != 0,cos(π/4+x) != 0,1−tanx != 0;preservealloriginalpoles',80)
p2=roots('ii',f'tan(pi/4+{D})-tan({D})-2','FiniteSet(45/2,225/2)',340,
 [('tan','x','-1+sqrt(2)',1),('tan','x','-1-sqrt(2)',1)],hi='180')
p2['dependency']={'source_part':'i','role':'Hence use the quadratic,butsubstitute roots into the original two-tangent equation andexcludeits poles.'}
add('Exercise-3B',8,80,'Show tan(45°+x)−tanx=2reduces to tan²x+2tanx−1=0;hence solve on0°≤x≤180°. Both original tangent terms must remain defined.',[p,p2],[COMP,TRANS,BND,ALL])

p=reasoning('ordered-pairs','(α,β)≈(45.0°,26.6°)or(116.6°,135.0°). The key reverses the α/βrolesinbothpairs.',
 'Letu=tanβandtanα=2u. The sumcondition3=(3u)/(1−2u²)gives2u²+u−1=0,so u=1/2or−1. Each tangent has exactlyoneanglein(0°,180°). Thus thepairsare(45°,atan(1/2))and(180°−atan2,135°),with inverseangles convertedtodegrees. Their sumtangentis3andtanα/tanβ=2. The printedreversepairs insteadhave tanα/tanβ≈1/2. Domain1−2u²isnonzeroforbothroots.',340,'key wrong')
p['additional_operations']={'tan_beta_roots':{'kind':'real-roots','operands':['2*x**2+x-1']},
 'exact_degree_pairs':{'kind':'identity','operands':['Tuple(Tuple(45,atan(1/2)*180/pi),Tuple(180-atan(2)*180/pi,135))']},
 'first_pair_original_conditions':{'kind':'identity','operands':['Tuple(tan(pi/4)/tan(atan(1/2)),tan(pi/4+atan(1/2)))']},
 'second_pair_original_conditions':{'kind':'identity','operands':['Tuple(tan(pi-atan(2))/tan(3*pi/4),tan(pi-atan(2)+3*pi/4))']}}
add('Exercise-3B',9,80,'Bothα,βliein0°<angle<180°,tanα=2tanβ,andtan(α+β)=3. Find every ordered pair. Preserve the source roles; the key gives the transposed pairs.',[p],[COMP,BND,ALL])

p=transform('i','(tan(pi/6+x)-2*tan(pi/3-x))*sqrt(3)*(1-tan(x)/sqrt(3))*(1+sqrt(3)*tan(x))',
 'tan(x)**2+6*sqrt(3)*tan(x)-5',[],
 'cosx != 0andbothoriginalshiftedtangentsdefined. Forx=90°theoriginalresidualis−1/√3,soexclusionbytanxdoesnotloseasolution.',80)
p['additional_operations']={'original_at90':{'kind':'identity','operands':['tan(pi/6+pi/2)-2*tan(pi/3-pi/2)']}}
p2=roots('ii',f'tan(pi/6+{D})-2*tan(pi/3-{D})',['24.7','95.3'],340,
 [('tan','x','-3*sqrt(3)+4*sqrt(2)',1),('tan','x','-3*sqrt(3)-4*sqrt(2)',1)],hi='180',approx=True)
p2['dependency']={'source_part':'i','role':'Use the verified quadraticwhile checking theoriginalshifted-poleconditions.'}
add('Exercise-3B',10,80,'Show tan(30°+θ)=2tan(60°−θ)reduces totan²θ+6√3tanθ−5=0;henceorotherwise solve on0°≤θ≤180°. Check theθ=90°casewhenintroducingtanθ.',[p,p2],[COMP,TRANS,BND,ALL])

p=value('answer','(a-b)/(1+a*b)','3/11',340,
 'From sin(A+45°)=2√2cosA,expand andprove cosA≠0,thentanA=3. From4sec²B+5=12tanB,letb=tanB,giving4b²−12b+9=0andb=3/2. The originalconditions have a unique pair oftangentvalues,not uniqueangles. Applytan(A−B)=(a−b)/(1+ab);thedenominator11/2isnonzero.')
p['operation'].update(conditions=['(a+1)/sqrt(2)-2*sqrt(2)','4*(1+b**2)+5-12*b'],unknowns=['a','b'])
add('Exercise-3B',11,80,'Given sin(A+45°)=2√2cosAand4sec²B+5=12tanB,find exacttan(A−B)withoutacalculator. The equations determine tangentvalues despite possibleperiodicanglechoices.',[p],[COMP,PYTH,EVAL])

p=reasoning('check-strategy','Use exact testangleswherebothsidesaredefined:45°helpschecksine/cosinedoubleangles;30°canchecktangentbecause45°wouldmakeits2θtangentundefined.',
 'Forθ=45°,sin2θ=1andcos2θ=0areeasy,withsinθ=cosθ=1/√2. Thisθisunsuitablefortan2θ. Insteadθ=30°givestanθ=1/√3,tan2θ=√3and2tanθ/(1−tan²θ)=√3. Such checks can find a wrongsignorcoefficientbutdonotestablishanidentityfor everyangle.',340,'matches')
p['additional_operations']={'sine_cosine_test':{'kind':'identity','operands':['Tuple(sin(pi/2),2*sin(pi/4)*cos(pi/4),cos(pi/2),cos(pi/4)**2-sin(pi/4)**2)']},
 'valid_tangent_test':{'kind':'identity','operands':['Tuple(tan(pi/3),2*tan(pi/6)/(1-tan(pi/6)**2))']}}
p2=reasoning('proof-distinction','A finite numerical check is not a proof. An algebraic derivation from the already established compound identities proves the double-angle result on its common domain.',
 'Testing examplesaddresses onlythoseinputs. Substituteφ=θintothegeneralcompoundformulasandusePythagoreanidentitiestoobtainvalidsymbolicrelations. Tangentrequiresitsoriginaltermsdefined;do not inferuniversal validityatpolesfromsuccessfulfinitechecks.',340,'matches')
add('Prompt',4,81,'While reading double-angle derivations,suggest how to check them andexplainwhether a check is the same as a proof. The source distinguishes useful45°sine/cosine tests from valid30°tangent tests.',[p,p2],[],[DOUBLE])
answers[-1]['evidence_role']='prerequisite/supporting proof-versus-check discussion; no forced direct trig-demand coverage'

parts=[]
for label,left,right in[
 ('sin','sin(2*x)','2*sin(x)*cos(x)'),
 ('cos-difference','cos(2*x)','cos(x)**2-sin(x)**2'),
 ('cos-sine-form','cos(2*x)','1-2*sin(x)**2'),
 ('cos-cosine-form','cos(2*x)','2*cos(x)**2-1'),
 ('tan','tan(2*x)','2*tan(x)/(1-tan(x)**2)')]:
    p=transform(label,left,right,[],
      'Allrealθforsine/cosine;tangentcommon-domainrequirescosθ != 0andcos2θ != 0.',81)
    p['method']='Setthetwooriginalcompoundargumentsequal. Independentlyverifythe resulting analytic identity;thealternatecosineformsfollowfromsin²θ+cos²θ=1. Preserveoriginaltangentdomaininadditiontothesource45°/135°combined-angleexceptions.'
    parts.append(p)
add('Worked-derivation',3,81,'Unnumbered exposition substitutesφ=θtoderivesin2θ,cos2θ,andtan2θ;then rewritescos2θas1−2sin²θandas2cos²θ−1. Allfive statedforms are checked withcommondomains.',parts,[],[DOUBLE],new_item=True)

figures=[]
for n,page,label,note,rep,teaches,parent,kind,method in[
 (9,79,'3B6 given coordinate triangle','A(−4,1),B(0,4),C(6,−2),P(0,1). AtB,αisbetweendownwardverticalandBA;βbetweenthatverticalandBC. The sumα+βistheobtuseangleABC.','diagram',[COMP,EXACT],'Exercise-3B:6','given-figure',
  'Independentcoordinateleglengthsgivesin/cosratios;BA·BC=−6confirmsanobtuseincludedangle. Theparentcompoundcalculationskeepα/βontherenderedrays.'),
 (10,81,'Double-angle derivation flow','The displayedcompound-to-double substitutionandfiveboxedresultsformsine,threecosineforms,andtangent. Tangentinputsanddenominatorsretaintheircommondomain.','table',[DOUBLE],'Worked-derivation:3','teaching-figure',
  'Allfiveformulasarecheckedintheparentanalyticderivation. Theadjacentpromptseparatesfinitechecksfromproofandavoidsundefined45°tangenttests.')]:
    figures.append({'item_id':f'8227:TB:Goldie:C3:Teaching-figure:{n}','item_kind':kind,'exercise':'Teaching figure','item_number':str(n),
      'pdf_page':page,'printed_page':page-14,'source_label':label,'notes':note,'what_it_shows':note,
      'assessed_8227_demand_ids':[],'component_demand_ids':[],'teaches_8227_demand_ids':teaches,'representation':rep,
      'source_evidence':ev(page),'parent_item_id':'8227:TB:Goldie:C3:'+parent,'learner_display':False,
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'not applicable','quoted_value':note,
        'reason':'A given diagram orproof/teaching flowisnotanewbounded-equationresponse.'}],
      'value_level_scope_review_status_r5':'author actual diagram/flowread2026-11-18;independentcheckpending',
      'exam_representation_check':{'status':'final cross-book/examinationcomparisonpending','examination_part_ids':[],
        'relation':'Textbook representation; no official award or examination-frequency claim.'},
      'mathematical_feature_review':{'status':'author diagram/parentexactderivationchecked;independentacceptancepending','method':method}})
pages=[{'pdf_page':page,'printed_page':page-14,'chapter':3,'page_status':'items enumerated',
 'item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],
 'continuation_item_ids':[],'source_evidence':ev(page),'non_item_content':'AllExercise3Bquestions,Example3.3,double-anglepromptandheadinglessderivation,andtwomathematicalfiguresenumerated. Page81endswithproseintroducingmodellingonthenextpage;noactivitystartthereisomitted.',
 'reader':'Codex author','date':'2026-11-18'}for page in range(78,82)]
if __name__=='__main__':
    for name,data in[
      ('answers-Goldie-C3-compound.json',{'scope':'Allcompound-angleitemsandinitialdouble-anglederivationonPDF78–81.','items':answers}),
      ('census-Goldie-C3-compound.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':3,'source_path':SRC,'source_sha256':SHA,
        'scope':'PDF78–81;allquestions,expositionsandfigures.','new_items':new+figures,'corrections':[],'pages':pages})]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(len(answers),'items;',len(figures),'figures;',sum(len(r['subparts'])for r in answers),'outputs')
