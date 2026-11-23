"""Fixed-source double-angle census and derivations, Goldie PDF82–85."""
import hashlib,json
from pathlib import Path
from author_YM_C4_trig_graphs import value,graph,reasoning
from author_YM_C4_composite_equations import roots,transform
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2]
SRC='sources/namibia/nsscas/8227-mathematics/textbooks/Goldie_Pure-Mathematics-2-and-3_2nd-edition_2018.pdf'
SHA='f030d64259ffe233a7408d2a64dea21c0a04f1ac0426439f5efaea694eb72e85'
COMP='8227:2020:M2:T3:O02:D02';DOUBLE='8227:2020:M2:T3:O02:D03';REC='8227:2020:M2:T3:O01:D01';PYTH='8227:2020:M2:T3:O02:D01';EVAL='8227:2020:M2:T3:O02:D05'
BND='8227:2020:M1:T6:O06:D01';ALL='8227:2020:M1:T6:O06:D02';TRANS='8227:2020:M1:T6:O05:D02';SKETCH='8227:2020:M1:T6:O02:D03';BASIC='8227:2020:M1:T6:O01:D01';RANGE='8227:2020:M1:T3:O02:D02';D='(x*pi/180)'
ATTR={10:'9709,Paper33Q4,November2014',11:'9709,Paper33Q3,June2013',12:'9709,Paper3Q3,June2009',13:'9709,Paper32Q3,June2010'}
def ev(page):
    name='Goldie-key-C3-337'if page==340 else'Goldie-C3-82'
    p=W/f'checks/r5/textbooks/{name}.png'
    return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[];new=[]
def add(kind,n,page,note,parts,direct,components=None,sketch=False,new_item=False):
    for p in parts:
        kp=p.pop('key_page_override',340);p.pop('source_page_override',None)
        p.update(source_pdf_page=page,source_evidence=ev(page),answer_pdf_page=kp,
          answer_printed_page=kp-14,key_evidence=ev(kp),review_date='2026-11-18')
    equation=kind=='Example'or kind=='Exercise-3C'and n in[1,2,3,4,6,8,9,11,12]
    attributed=kind=='Exercise-3C'and n in ATTR
    row={'item_id':f'8227:TB:Goldie:C3:{kind}:{n}','source_pdf_page':page,'notes':note,
      'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],
      'mapping_rationale':'Separate requested double/compound transformations,complete bounded roots,sketches and exact ratio outputs. A displayed explanatory derivation has teaching/component links rather than a fabricated assessed question. Original denominators and zero factors remain part of the problem.',
      'representation':'text','sketch_response_required':sketch,
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'within'if equation else'not applicable',
        'quoted_value':note,'reason':'Actual equation arguments use small integers1/2,with3in3C3–4and4in3C2(v);the original finite bounds remain. Derived triple-angle formulas are obtained by compound/double identities,not assumed as new memorisation scope.'if equation else'Exact ratio/simplification/proof or supplied-model teaching;no periodic root family is asked.'},
       {'rule_id':'8227:LIMIT02','status':'within'if equation else'not applicable','quoted_value':note,
        'reason':'Only the source finite interval is solved. A request for an exact value such ascosx ortan3adoesnotrequireanunboundedanglefamily.'}],
      'exam_style':attributed,'exam_style_basis':('Book prints Cambridge International AS & A Level Mathematics '+ATTR[n]+'. This is a textbook attribution lead,not renewed verification of the original examination PDF; textbook originals stay internal.')if attributed else'Unattributed Example/Exercise/exposition; no examination attribution or explicit exam-style label.',
      'precision_angle_check':{'source':'Degree/radian bounds are preserved;πroot sets stay exact. Numeric keys are compared at their written last place.3C8supplies tan26.6°≈0.5for a one-decimal complementary-angle answer.',
        'comparison':'Derive every exact root before matching rounded key values one-to-one. A missing root yields an incomplete key; it doesnot shift later printed values onto another root. The26.6°premise is a given rounded relation,not a claim of infinite decimal accuracy.'},
      'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts}
    if not direct:row['evidence_role']='prerequisite/supporting teaching exposition; not an explicit assessed question'
    answers.append(row)
    if new_item:new.append({'item_id':row['item_id'],'item_kind':'worked-derivation','exercise':kind,'item_number':str(n),
      'pdf_page':page,'printed_page':page-14,'notes':note,'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],
      'teaches_8227_demand_ids':components or direct,'representation':'text','source_evidence':ev(page),
      'evidence_role':row.get('evidence_role','directly related assessed practice'),'answer_key':{'available':True,'pdf_pages':[page],'printed_pages':[page-14],'locator':'Inline explanatory derivation'},'learner_display':False})
    return row

p=transform('range-rewrite','2*p**2*sin(x)*cos(x)/q','p**2*sin(2*x)/q',[],
 'p=u>0is launchspeed,q=g>0isaccelerationmagnitude;levelground,noairresistance;physical0≤α≤π/2',82)
p2=reasoning('maximum','Maximum range u²/g occurs at α=π/4=45° under the supplied ideal level-ground model.',
 'The supplied model R=(u²/g)sin2αhas positive scale u²/g and2αin[0,π]. Sine reaches its maximum1uniquelyat2α=π/2there,soα=π/4. This is mathematical reasoning about a given formula,not assessment of projectile-motion derivation or empirical validity. Air resistance andunequal launch/landing heights would change the model.',82,'matches')
p2['additional_operations']={'sine_maximising_angle':{'kind':'bounded-trig-equation','operands':['sin(2*x)-1','0','pi/2']},
 'maximum_scaled_value':{'kind':'identity','operands':['p**2*sin(2*pi/4)/q']}}
add('Worked-derivation',4,82,'Headingless ideal projectile exposition:rewriteR=2u²sinαcosα/gas(u²/g)sin2α,anddeduceitsmaximising45°launchangleandmaximumu²/g. The supplied model assumeslevelgroundandignoredairresistance,u,gpositive.',[p,p2],[],[DOUBLE,RANGE],new_item=True)
parts=[transform('sine-square','sin(x)**2','(1-cos(2*x))/2',[], 'all real angles',82),
 transform('cosine-square','cos(x)**2','(1+cos(2*x))/2',[], 'all real angles',82)]
add('Worked-derivation',5,82,'Headingless calculus motivation rearrangescos2θtoobtain sin²θ=(1−cos2θ)/2andcos²θ=(1+cos2θ)/2. No integral is actually asked or evaluated here.',parts,[],[DOUBLE],new_item=True)

add('Example',4,83,'Solve sin2θ=sinθ on0°≤θ≤360°. Factor sinθ(2cosθ−1)=0withoutcancellingthesine-zero branch;the source explicitly warns aboutlostroots.',[
 roots('roots',f'sin(2*{D})-sin({D})','FiniteSet(0,60,180,300,360)',83,
 [('sin','x','0',1),('cos','x','1/2',1)])],[DOUBLE,TRANS,BND,ALL])
add('Example',5,84,'Solve2+cos2θ=sinθon0≤θ≤2π. Selectcos2θ=1−2sin²θ,thenrejectsinθ=−3/2;onlyθ=π/2remains.',[
 roots('roots','2+cos(2*x)-sin(x)','FiniteSet(pi/2)',84,
 [('sin','x','1',1),('sin','x','-3/2',1)],unit='radian')],[DOUBLE,TRANS,BND,ALL])

parts=[]
for label,expr,key,branches in[
 ('i',f'2*sin(2*{D})-cos({D})',['14.5','90','165.5','270'],[('cos','x','0',1),('sin','x','1/4',1)]),
 ('ii',f'tan(2*{D})-4*tan({D})',['0','35.3','144.7','180','215.3','324.7','360'],[('tan','x','0',1),('tan','x','1/sqrt(2)',1),('tan','x','-1/sqrt(2)',1)]),
 ('iii',f'cos(2*{D})+sin({D})','FiniteSet(90,210,330)',[('sin','x','1',1),('sin','x','-1/2',1)]),
 ('iv',f'tan({D})*tan(2*{D})-1','FiniteSet(30,150,210,330)',[('tan','x','1/sqrt(3)',1),('tan','x','-1/sqrt(3)',1)]),
 ('v',f'2*cos(2*{D})-1-cos({D})',['0','138.6','221.4','360'],[('cos','x','1',1),('cos','x','-3/4',1)])]:
    parts.append(roots(label,expr,key,340,branches,approx=isinstance(key,list)))
add('Exercise-3C',1,84,'Solve five single/double-angle equations on0°≤θ≤360°:2sin2θ=cosθ,tan2θ=4tanθ,cos2θ+sinθ=0,tanθtan2θ=1,and2cos2θ=1+cosθ. Preserve zero factors andboth original tangent domains.',parts,[DOUBLE,TRANS,BND,ALL])
parts=[]
for label,expr,key,branches in[
 ('i','sin(2*x)-2*sin(x)','FiniteSet(-pi,0,pi)',[('sin','x','0',1),('cos','x','1',1)]),
 ('ii','tan(2*x)-2*tan(x)','FiniteSet(-pi,0,pi)',[('tan','x','0',1)]),
 ('iii','cos(2*x)-cos(x)','FiniteSet(-2*pi/3,0,2*pi/3)',[('cos','x','1',1),('cos','x','-1/2',1)]),
 ('iv','1+cos(2*x)-2*sin(x)**2','FiniteSet(-3*pi/4,-pi/4,pi/4,3*pi/4)',[('sin','x','1/sqrt(2)',1),('sin','x','-1/sqrt(2)',1)]),
 ('v','sin(4*x)-cos(2*x)','FiniteSet(-11*pi/12,-3*pi/4,-7*pi/12,-pi/4,pi/12,pi/4,5*pi/12,3*pi/4)',[('cos','2*x','0',1),('sin','2*x','1/2',1)])]:
    parts.append(roots(label,expr,key,340,branches,unit='radian',lo='-pi',hi='pi'))
add('Exercise-3C',2,84,'Solve five equations on−π≤θ≤π,specificallyincluding1+cos2θ=2sin²θand sin4θ=cos2θ. Part(v)usesan equationin2θandmustkeepallnegativeandpositiveradianroots.',parts,[DOUBLE,TRANS,BND,ALL])

p=value('derive','sin(3*x)','3*sin(x)-4*sin(x)**3',340,
 'Follow the source-required3θ=2θ+θsplit. Sineaddition gives sin2θcosθ+cos2θsinθ;substitute double-angleformsandcos²θ=1−sin²θtoobtain3sinθ−4sin³θ. The main independent expansion starts fromthe originalsin3θ.')
p['operation']={'kind':'trig-expand','operands':['sin(3*x)']}
p['additional_operations']={'required_compound_step':{'kind':'trig-compound-expand','family':'sin','operands':['2*x','x']},
 'polynomial_equivalence':{'kind':'trig-identity-residual','operands':['2*sin(x)*cos(x)**2+(1-2*sin(x)**2)*sin(x)','3*sin(x)-4*sin(x)**3']}}
p2=roots('solve','sin(3*x)-sin(x)','FiniteSet(0,pi/4,3*pi/4,pi,5*pi/4,7*pi/4,2*pi)',340,
 [('sin','x','0',1),('sin','x','1/sqrt(2)',1),('sin','x','-1/sqrt(2)',1)],unit='radian')
p2['dependency']={'source_part':'derive','role':'Hence use the derived cubic,withoutdividingawaythesine-zero roots.'}
add('Exercise-3C',3,84,'Write sin3θas sin(2θ+θ)andexpressitin sinθ;hencesolve sin3θ=sinθon0≤θ≤2π. A derived triple-angleformula is notanaddedmemorisationrequirement.',[p,p2],[COMP,DOUBLE,TRANS,BND,ALL])
add('Exercise-3C',4,84,'Solve cos3θ=1−3cosθon0°≤θ≤360°. Derivingcos3θfromcompound/doubleformsgives4cos³θ=1,thenrecoverbothboundedroots.',[
 roots('roots',f'cos(3*{D})-1+3*cos({D})',['51','309'],340,[('cos','x','(1/4)**(1/3)',1)],approx=True)],[COMP,DOUBLE,TRANS,BND,ALL])
p=value('answer','(1+cos(2*x))/sin(2*x)','cot(x)',340,
 'Use1+cos2θ=2cos²θandsin2θ=2sinθcosθ,then cancelon theoriginaldomain sin2θ≠0. The simplifiedcotθdoesnotremove theoriginalexclusionatcosθ=0.')
p['original_common_domain']='sin(2θ) != 0;equivalentlysinθ != 0andcosθ != 0'
add('Exercise-3C',5,84,'Simplify(1+cos2θ)/sin2θwithitsoriginaldenominatordomain; the resultcotθcannotbeusedtofilloriginalholes.',[p],[DOUBLE,REC,EVAL])

def paired_graphs(n,scale,offset,roots_key):
    parts=[graph('i:cos','cos','1','2','0','0','2*pi','radian',340,
      {'sample_values':'Tuple(1,-1,1,-1,1)','window_range':'Interval(-1,1)'},at=['0','pi/2','pi','3*pi/2','2*pi']),
      graph('i:sin','sin',str(scale),'1',str(offset),'0','2*pi','radian',340,
      {'sample_values':f'Tuple({offset},{scale+offset},{offset},{-scale+offset},{offset})','window_range':f'Interval({-scale+offset},{scale+offset})'},at=['0','pi/2','pi','3*pi/2','2*pi'])]
    for p in parts:p['source_assessed_part_id']='i'
    left=f'{scale}*sin(x)+({offset})-cos(2*x)'
    right=f'2*sin(x)**2+{scale}*sin(x)+({offset-1})'
    p=transform('ii',left,right,[], 'all real x',85)
    p2=roots('iii',left,roots_key,340,[('sin','x','1/2',1),('sin','x','-1'if n==6 else'-2',1)],unit='radian')
    p2['dependency']={'source_part':'ii','role':'Use the derived sine polynomialand original0≤x≤2πinterval; rejectinadmissible ratios.'}
    parts.extend([p,p2]);return parts
row=add('Exercise-3C',6,85,'Sketch cos2xandsinxon0≤x≤2π;showintersectionsobey2sin²x+sinx−1=0;solveexactly. The3π/2intersectionisatasharedminimum,touchingratherthanatransversecrossing.',
 paired_graphs(6,1,0,'FiniteSet(pi/6,5*pi/6,3*pi/2)'),[BASIC,SKETCH,DOUBLE,TRANS,BND,ALL],sketch=True)
row['source_interpretation']='The exactroot3π/2mustnotbelostbycountingonlyvisiblecrossings. Bothcurveshaveordinate−1andderivative0there;thecurvefeaturesderivefromtheoriginalfunctions.'
p=transform('proof','(1-tan(x)**2)/(1+tan(x)**2)','cos(2*x)',
 ['(cos(x)**2-sin(x)**2)/(cos(x)**2+sin(x)**2)'],'cosθ != 0because theoriginalleftuses tanθ',85)
add('Exercise-3C',7,85,'Show(1−tan²θ)/(1+tan²θ)=cos2θonitsoriginaltangentdomain. Therightsidealoneisdefinedmorewidely.',[p],[DOUBLE,EVAL],[PYTH])
p=transform('i','tan(pi/4+x)*tan(pi/4-x)','1',
 ['(sin(pi/4+x)*sin(pi/4-x))/(cos(pi/4+x)*cos(pi/4-x))'],
 'cos(π/4+θ)cos(π/4−θ) != 0. Thisoriginaldomaincanincludeθ=π/2;anunshiftedtanθsubstitutionmustnotintroduceafalseexclusion.',85)
p2=value('ii','90-266/10','634/10',340,
 'Use the supplied roundedtan26.6°≈1/2andthecomplementaryreciprocalrelationshiptoobtainθ≈90°−26.6°=63.4°. The sourceforbidscalculatorusefor thelearner;independentatan2roundingchecksitsone-decimalaccuracy.')
p2['additional_operations']={'independent_actual_angle_1dp':{'kind':'rounded','operands':['atan(2)*180/pi'],'decimal_places':1}}
add('Exercise-3C',8,85,'Show tan(π/4+θ)tan(π/4−θ)=1;then givantan26.6°≈0.5solve tanθ=2for0°<θ<90°,withoutacalculator,to1dp.',[p,p2],[COMP,REC,EVAL,BND])
add('Exercise-3C',9,85,'Sketchcos2xand3sinx−1on0≤x≤2π;showtheirintersectionsobey2sin²x+3sinx−2=0andfindtheexactπroots. Theinadmissiblesinx=−2branchmustberejected.',
 paired_graphs(9,3,-1,'FiniteSet(pi/6,5*pi/6)'),[SKETCH,DOUBLE,TRANS,BND,ALL],sketch=True)
p=transform('i','cos(x-pi/3)+cos(x+pi/3)','cos(x)',[], 'all real angles',85)
p2=value('ii','0','FiniteSet((3-sqrt(17))/4)',340,
 'Use theprovedsumidentityinbothnumeratoranddenominator,sothegivenquotientiscos2x/cosx=3withcosx≠0. Putc=cosx:2c²−3c−1=0. Solveindependentlyandkeepc∈[−1,1];theotherrootexceeds1. Noangleintervalisneededbecauseanexactcosinevalueisrequested.')
p2['operation']={'kind':'polynomial-roots-in-interval','operands':['2*x**2-3*x-1','-1','1']}
p2['dependency']={'source_part':'i','role':'Use thecosinesumidentityandpreservetheoriginalquotientdenominator.'}
add('Exercise-3C',10,85,'Show cos(θ−60°)+cos(θ+60°)=cosθ;then giventheshifted2xsumovertheshiftedxsum=3,findexactcosx. Preserve a nonzero denominator.',[p,p2],[COMP,DOUBLE,EVAL])
p=roots('roots',f'tan(2*{D})-5*cot({D})',['40.2','139.8'],340,
 [('cos','x','0',1),('cos','x','sqrt(7/12)',1),('cos','x','-sqrt(7/12)',1)],hi='180',approx=True,opened=True)
p.update(difference_disposition='key incomplete',difference_reason='Thekeyomitsx=90°,whereoriginaltan180°=0andcot90°=0arebothdefined. Originaldenominatorclearinggivescosx(7−12cos²x)=0;thecosine-zero branchisvalid.')
add('Exercise-3C',11,85,'Solve tan2x=5cotxon0°<x<180°. Theoriginalsinxandcos2xdenominatorsmustbenonzero,butcosx=0isallowed. Thekeymissesvalid90°.',[p],[DOUBLE,REC,TRANS,BND,ALL])
p=transform('i','csc(2*x)+cot(2*x)','cot(x)',
 ['(1+cos(2*x))/sin(2*x)','2*cos(x)**2/(2*sin(x)*cos(x))'],'sin2θ != 0;retainalloriginalpoles',85)
p2=roots('ii',f'csc(2*{D})+cot(2*{D})-2',['26.6','206.6'],340,[('tan','x','1/2',1)],approx=True)
p2['dependency']={'source_part':'i','role':'Hence usecotθ=2on theoriginaldomain,notthroughanintroducedhole.'}
add('Exercise-3C',12,85,'Prove cosec2θ+cot2θ=cotθ;hencesolvetheoriginalsum=2on0°≤θ≤360°,keepingtheoriginalsin2θpolesexcluded.',[p,p2],[DOUBLE,REC,EVAL,BND,ALL])
parts=[]
for label,family,a,b,key in[
 ('i','sin','atan(4/3)','-pi/6','(4*sqrt(3)-3)/10'),
 ('ii:tan2a','tan','atan(4/3)','atan(4/3)','-24/7'),
 ('ii:tan3a','tan','2*atan(4/3)','atan(4/3)','-44/117')]:
    p=value(label,'0',key,340,
      'Thegivenacute cos a=3/5gives sin a=4/5andtan a=4/3. Applytheappropriatecompound/doubleformulaexactly,withoriginalcos2a=−7/25andcos3a=−117/125bothnonzero. Do notevaluateathencarryroundedangles.')
    p['operation']={'kind':'trig-compound-expand','family':family,'operands':[a,b]}
    if label.startswith('ii:'):p['source_assessed_part_id']='ii'
    if label=='ii:tan3a':p['dependency']={'source_part':'ii:tan2a','role':'Hence use thederivedtan2ain thecompound2a+astep.'}
    parts.append(p)
add('Exercise-3C',13,85,'Given cos a=3/5and0°≤a≤90°,withfullworkingandwithoutcalculatinga,find exactsin(a−30°),tan2a,andhencetan3a. Thelastvalueusescompound2a+a,nounstatedtriple-anglememorisation.',parts,[COMP,DOUBLE,EVAL])

figures=[]
for n,page,label,note,rep,teaches,parent,method in[
 (11,82,'Figure3.5 ideal projectile diagram','A contextualgolfphotographaccompaniesaheight-versus-horizontal-distanceparabola,initialvelocityu,launchangleα,levelground,andrangeR. Thephotoiscontext,notacalibratedmetricinput.','diagram',[DOUBLE],'Worked-derivation:4',
  'Readthegivensandmodelassumptions;theparentderivesR=(u²/g)sin2αanditsmaximumforpositiveu,g. Noempiricalmechanicsorphotometricvalidationisclaimed.'),
 (12,82,'Power-reduction formula flow','Thetwoboxesrearrange cos2θtosin²θ=(1−cos2θ)/2andcos²θ=(1+cos2θ)/2. Calculusismotivation;nointegralisasked.','table',[DOUBLE],'Worked-derivation:5',
  'Bothidentitiesareindependentlycheckedintheparentexpositoryderivation;donotcountthisascompletedintegrationpractice.'),
 (13,83,'Figure3.6 sine-zero branch','Thedegreesinegraphon0°..360°marks0°,180°,360°asthesine-zero branchofExample3.4. Inclusiveendpointrootsmustbothremain.','graph',[BND,ALL],'Example:4',
  'Theoriginalsin2θ−sinθfactorisationandindependentrootenumerationretainallsine-zeroroots. Thedisplayedprincipal0°doesnotreplace180°and360°.'),
 (14,83,'Figure3.7 cosine-half branch','Thedegreecosinegraphmeetshorizontal1/2at60°and300°,addingtheotherExample3.4roots. Thetwo-branchstructureisexplicit.','graph',[BND,ALL],'Example:4',
  'Independentexactcosθ=1/2rootsarecheckedagainsttheoriginalequationandcombinedwiththesine-zerobranch;nozero-factorcancellation.'),
 (15,84,'Figure3.8 sine-one peak','The radiansinegraphhasitsuniqueheight1pointatπ/2on0..2π;theotheralgebraicratio−3/2isinadmissible.','graph',[BND,ALL],'Example:5',
  'Theparentoriginalequationisindependentlyreduced;range[−1,1]rejects−3/2,andtheoriginalintervalcontainsonepeak.')]:
    figures.append({'item_id':f'8227:TB:Goldie:C3:Teaching-figure:{n}','item_kind':'teaching-figure','exercise':'Teaching figure','item_number':str(n),
      'pdf_page':page,'printed_page':page-14,'source_label':label,'notes':note,'what_it_shows':note,
      'assessed_8227_demand_ids':[],'component_demand_ids':[],'teaches_8227_demand_ids':teaches,'representation':rep,
      'source_evidence':ev(page),'parent_item_id':'8227:TB:Goldie:C3:'+parent,'learner_display':False,
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'not applicable','quoted_value':note,
        'reason':'Teaching/solutionfigure,notaseparatebounded-equationresponse. Originalunits/intervalsarekeptintheparent.'}],
      'value_level_scope_review_status_r5':'authoractualvaluesread2026-11-18;independentcheckpending',
      'exam_representation_check':{'status':'finalcross-book/examinationcomparisonpending','examination_part_ids':[],
        'relation':'Textbookteachingrepresentation;noofficialmarkingorfrequencyclaim.'},
      'mathematical_feature_review':{'status':'authordiagramandparentexactderivationchecked;independentacceptancepending','method':method}})
pages=[{'pdf_page':page,'printed_page':page-14,'chapter':3,'page_status':'items enumerated',
 'item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],
 'continuation_item_ids':[],'source_evidence':ev(page),
 'non_item_content':'Allheadinglessexpositions,Examples3.4/3.5,13Exercise3Cquestionsandfiveteachingfiguresenumerated. Requiredresponsegraphsareattachedtosourcepartchecks,notcountedagainasgivenbodyfigures.',
 'reader':'Codex author','date':'2026-11-18'}for page in range(82,86)]
if __name__=='__main__':
    for name,data in[
      ('answers-Goldie-C3-double.json',{'scope':'Everyexplicitresponse/derivationonPDF82–85;chapter3after85remainspending.','items':answers}),
      ('census-Goldie-C3-double.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':3,'source_path':SRC,'source_sha256':SHA,
        'scope':'PDF82–85;allformal/headinglesstasksandteachingfigures.','new_items':new+figures,'corrections':[],'pages':pages})]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(len(answers),'items;',len(figures),'figures;',sum(len(r['subparts'])for r in answers),'outputs')
