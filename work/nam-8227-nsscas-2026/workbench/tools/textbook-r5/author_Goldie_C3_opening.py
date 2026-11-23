"""Fixed-source author census/derivations for Goldie PDF71–77 and C2 closing page70."""
import hashlib,json,math,sys
from pathlib import Path
from author_YM_C4_trig_graphs import value,reasoning
from author_YM_C4_composite_equations import roots,transform
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2]
sys.path.insert(0,str(W/'tools'))
from verify_textbook_answers_r5 import compute,expression
SRC='sources/namibia/nsscas/8227-mathematics/textbooks/Goldie_Pure-Mathematics-2-and-3_2nd-edition_2018.pdf'
SHA='f030d64259ffe233a7408d2a64dea21c0a04f1ac0426439f5efaea694eb72e85'
REC='8227:2020:M2:T3:O01:D01';SIX='8227:2020:M2:T3:O01:D02';PYTH='8227:2020:M2:T3:O02:D01';COMPOUND='8227:2020:M2:T3:O02:D02'
EXACT='8227:2020:M1:T6:O03:D01';BND='8227:2020:M1:T6:O06:D01';ALL='8227:2020:M1:T6:O06:D02';TRANS='8227:2020:M1:T6:O05:D02'
INTERPRET='8227:2020:M1:T6:O02:D02';FEATURE='8227:2020:M1:T6:O02:D01';TRI='8227:PRIOR:NSSCO:right-triangle-trig';D='(x*pi/180)'
def ev(page):
    name='Goldie-key-C3-337'if page in[339,340]else'Goldie-C3-70'if page<=73 else'Goldie-C3-74'
    p=W/f'checks/r5/textbooks/{name}.png'
    return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[];new_items=[];corrections=[]
def add(kind,n,page,note,parts,direct,components=None,roles=None,new=False):
    iid=f'8227:TB:Goldie:C3:{kind}:{n}'
    for p in parts:
        kp=p.pop('key_page_override',339)
        p.update(source_pdf_page=page,source_evidence=ev(page),answer_pdf_page=kp,
          answer_printed_page=kp-14 if kp else None,key_evidence=ev(kp or 339),review_date='2026-11-18')
    equation=kind=='Exercise-3A'and n in[1,7]or kind=='Example'and n==2
    row={'item_id':iid,'source_pdf_page':page,'notes':note,'assessed_8227_demand_ids':direct,
      'component_demand_ids':components or[],'component_demand_roles':roles or{},
      'mapping_rationale':'Map the requested reciprocal ratios, graph/sign properties, exact values, bounded solutions or compound-identity derivation. An acute right-triangle inversion is prior geometry, not principal-range classification. A model estimate or one-angle witness is not complete bounded-root coverage.',
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'within'if equation else'not applicable',
        'quoted_value':note,'reason':'Actual bounded equations use argument multiplier1; reciprocal functions and ratio powers are not new input multipliers.'if equation else'No finite periodic root set is requested; exact evaluation/proof/model reasoning is not a general-solution exercise.'},
       {'rule_id':'8227:LIMIT02','status':'within'if equation else'not applicable','quoted_value':note,
        'reason':'Retain every root in the explicit inclusive0°..360°interval and exclude original poles.'if equation else'Activity3.1 asks for an angle, so45° is a valid witness; it does not ask for all unbounded solutions.'}],
      'exam_style':False,'exam_style_basis':'Unattributed worked example, exercise, prompt or activity. CP/PS icons indicate question character, not examination provenance or an explicit exam-style label.',
      'precision_angle_check':{'source':'Exact fractions/surds are required in3A2; decimal angle keys elsewhere use the written one-decimal precision. Degrees are preserved, and source model b relates to radian wavelength2π/b.',
        'comparison':'Compute exact roots before comparing printed approximations. cot at90°/270° is0 using cos/sin, even though tan itself is undefined there; retain each original function domain.'},
      'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts}
    if not direct:row['evidence_role']='prerequisite/supporting source exposition; no forced direct demand coverage'
    answers.append(row)
    if new:new_items.append({'item_id':iid,'item_kind':'worked-illustration'if kind=='Worked-illustration'else'worked-derivation','exercise':kind,'item_number':str(n),
      'pdf_page':page,'printed_page':page-14,'notes':note,'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],
      'evidence_role':row.get('evidence_role','directly related assessed practice'),'representation':'text','teaches_8227_demand_ids':components or direct,'source_evidence':ev(page),
      'answer_key':{'available':True,'pdf_pages':[page],'printed_pages':[page-14],'locator':'Inline derivation on the same source page'},
      'learner_display':False,'exam_style':False,'exam_style_basis':row['exam_style_basis']})
    return row

p=reasoning('estimate-amplitude','No unique metric amplitude is determined by the unscaled photograph. A defensible estimate must state an assumed human/scene scale and distinguish crest-to-trough height from amplitude.',
 'The source asks an estimate, not a measured unique value. A sine model oscillates about a chosen midline; its amplitude is half its crest-to-trough height. The picture has perspective and no metric axis. The key explicitly says answers vary and suggests a≈1.6–1.8m. This is an illustrative estimate under an unstated scene scale, not a calibrated measurement.',339,'matches')
p2=reasoning('model-parameters','One internally consistent illustration is a≈1.7m and b≈3rad/m, giving y=1.7sin(3x) and wavelength2π/3m after choosing coordinates/midline.',
 'The source coefficient a is amplitude and b=2π/wavelength in a radian horizontal coordinate. Neither physical scale nor full wavelength is uniquely supplied, so numerical estimates remain conditional. The key first suggests a≈1.6–1.8 then substitutes1.5 in its example formula; that is an internal coefficient-copy inconsistency, not evidence that every a=1.5 estimate is impossible. Preserve the answers-vary scope while correcting the displayed substitution.',339,'key wrong')
p2['additional_operations']={'illustrative_wavelength':{'kind':'identity','operands':['2*pi/3']},
 'consistent_chosen_amplitude':{'kind':'identity','operands':['17/10']}}
p3=reasoning('model-judgement','A sine curve is a local approximation to an oscillatory wave, with limitations for this breaking, asymmetric, nonperiodic-looking segment.',
 'The qualitative repeating rise/fall motivates a sine model as the key says. The pictured breaking wave is not symmetric and does not establish a fixed amplitude/period across many cycles. A useful judgement names both the intended approximation and missing scale/phase/offset data; it does not certify predictive accuracy from one photograph.',339,'matches')
row=add('Prompt',1,71,'From the wave photograph estimate amplitude in metres, then use those estimates to suggest a,b for y=a sin(bx) and judge whether a sine curve is a good model. Metric scale,midline andwavelength are not uniquely given.',[p,p2,p3],[],[FEATURE,INTERPRET],roles={FEATURE:'Identify amplitude and wavelength parameters in the chosen model, rather than measure a calibrated graph.',INTERPRET:'Supporting interpretation of a contextual approximate sine model, not supplied-axis graph coverage.'})
row['representation']='diagram'

add('Example',1,73,'Find cosec120° exactly in surd form by taking the reciprocal of sin120°=√3/2.',
 [value('answer','1/sin(2*pi/3)','2/sqrt(3)',73,'Use the original120° input in quadrantII; sine ispositive√3/2,so its reciprocal is2/√3.')],[REC,EXACT])
row=add('Example',2,73,'Solve sec²θ=4+2tanθ on0°≤θ≤360°. Use sec²θ=1+tan²θ to obtain(tanθ−3)(tanθ+1)=0, retaining four roots and excluding tangent/secant poles.',
 [roots('roots',f'sec({D})**2-4-2*tan({D})',['71.6','135','251.6','315'],74,
  [('tan','x','3',1),('tan','x','-1',1)],approx=True)],[REC,PYTH,BND,ALL])
corrections.append({'item_id':row['item_id'],'continuation_pdf_pages':[74]})

items=[]
for label,original,key,branches in[
 ('i',f'csc({D})-1','FiniteSet(90)',[('sin','x','1',1)]),
 ('ii',f'sec({D})-2','FiniteSet(60,300)',[('cos','x','1/2',1)]),
 ('iii',f'cot({D})-4',['14.0','194.0'],[('tan','x','1/4',1)]),
 ('iv',f'sec({D})+3',['109.5','250.5'],[('cos','x','-1/3',1)]),
 ('v',f'cot({D})+1','FiniteSet(135,315)',[('tan','x','-1',1)]),
 ('vi',f'csc({D})+2','FiniteSet(210,330)',[('sin','x','-1/2',1)])]:
    items.append(roots(label,original,key,339,branches,approx=isinstance(key,list)))
add('Exercise-3A',1,74,'Solve six reciprocal equations on0°≤θ≤360°: cosecθ=1,secθ=2,cotθ=4,secθ=−3,cotθ=−1,cosecθ=−2. Recover every allowed quadrant root and exclude original poles.',items,[REC,BND,ALL])
items=[]
for label,expr,key in[('i','cot(3*pi/4)','-1'),('ii','sec(5*pi/6)','-2/sqrt(3)'),
 ('iii','csc(4*pi/3)','-2/sqrt(3)'),('iv','sec(7*pi/6)','-2/sqrt(3)'),
 ('v','cot(3*pi/2)','0'),('vi','csc(5*pi/4)','-sqrt(2)')]:
    items.append(value(label,expr,key,339,'Use exact unit-circle sine/cosine at the original related special angle, then form the requested reciprocal/quotient with its correct sign. cot270°=cos270°/sin270°=0; do not confuse it with the undefined tangent.'))
add('Exercise-3A',2,74,'Without a calculator find cot135°,sec150°,cosec240°,sec210°,cot270°,cosec225° as fractions orsurds. The axis-angle cotangent is defined andzero.',items,[REC,EXACT])

p=value('i','Tuple(acos(1/2)*180/pi,90-acos(1/2)*180/pi)','Tuple(60,30)',339,
 'A=90° andsecB=2 implycosB=1/2. TriangleB isacute,soB=60°andC=30°. These are exact special angles,not an unrestricted inverse equation.')
p2=value('ii','tan(pi/3)','sqrt(3)',339,'Use the derived acute B=60°to findtanB=√3.')
p3=value('iii','1+tan(pi/3)**2-sec(pi/3)**2','0',339,'Substitute the exact derived tangent/secant ratios:1+3=4. Confirm the stated identity for this triangle; the zero is a residual,not a literal printed scalar key.')
p3['check_mode']='show/prove';p3['key_page_override']=74;p3['key_presence']='Stated show-that result in the source question; no separate answer-key proof'
add('Exercise-3A',3,74,'Right triangleABC hasA=90°andsecB=2. FindB,C,tanB,andshow1+tan²B=sec²B for the derived special-angle triangle.',[p,p2,p3],[REC,EXACT,PYTH],[TRI])
p=value('i','Tuple(atan(1)*180/pi,90-atan(1)*180/pi)','Tuple(45,45)',339,
 'M=90°andcotN=1giveequal positive legs,soN=L=45°. Use the triangleacute-angle constraint.')
p2=value('ii','Tuple(sec(pi/4),csc(pi/4),tan(pi/4))','Tuple(sqrt(2),sqrt(2),1)',339,
 'The45°right triangle has sinL=cosL=1/√2,sosecL=cosecL=√2andtanL=1.')
p3=value('iii','1+tan(pi/4)**2-sec(pi/4)**2','0',339,
 'The derived exact ratios give1+1=2=sec²L,confirming this stated equality independently.')
p3['check_mode']='show/prove';p3['key_page_override']=74;p3['key_presence']='Stated show-that result in the source question; no separate answer-key proof'
add('Exercise-3A',4,74,'Right triangleLMN hasM=90°andcotN=1. FindL,N,then secL,cosecL,tanL,andshow1+tan²L=sec²L.',[p,p2,p3],[REC,EXACT,PYTH],[TRI])
p=value('i','6/(3/2)','4',339,'A positive1.5m vertical height and6m horizontal shadow givecotα=adjacent/opposite=6/1.5=4. This is the requested ratio,not an assumed angle.')
p['check_mode']='show/prove';p['key_page_override']=74;p['key_presence']='Stated show-that result in the source question; no separate answer-key proof'
p2=value('ii','atan(1/4)*180/pi','14',339,'The sun elevation isacute,soα=atan(1/4),converted todegrees. Compare withthe written14.0°key onlyafter derivation.')
p2['operation']={'kind':'rounded','operands':['atan(1/4)*180/pi'],'decimal_places':1}
add('Exercise-3A',5,74,'A1.5m tall person casts a6m shadow atsun elevationα. Showcotα=4andfindα in degrees; the physical acute angle excludes periodic alternatives.',[p,p2],[REC],[TRI])

p=reasoning('i','0° < α < 90°',
 'secαpositive requirescosα>0,andcosecαpositive requiressinα>0,soonlyquadrantIremains. Therecotα=cosα/sinα>0. At0°cosecandcotareundefined;at90°secisundefinedandcotis0,so neitherendpoint qualifies. The printed inclusive0°≤α≤90°keyis wrong.',339,'key wrong')
p2=reasoning('ii','No angle makes allthree negative.',
 'Forsecandcosectobebothnegative,cosandsinmustbothbenegative,placingαinopenquadrantIII. Theirquotientcotisthenpositive,contradictingallnegative. Axes cannot qualifybecauseatleastoneoriginalreciprocalisundefinedorzero.',339,'matches')
p3=reasoning('iii','No angle makes secα,cosecα,cotα allequal.',
 'Equalityofsecandcosecforcescosα=sinα≠0;thereforecotα=1. Allequalitywouldforcecosα=sinα=1,contradictingsin²α+cos²α=1. Thisis a universal contradiction onthecommon originaldomain,not just absence in a finite plotted sample.',339,'matches')
add('Exercise-3A',6,75,'For0°≤α≤360°,decidewhen secα,cosecα,cotαareallpositive,whetherallcanbenegative,andwhetherallcanbeequal. Giveexplanations,withoriginalundefinedaxisangles excluded.',[p,p2,p3],[SIX,REC])

items=[]
for label,original,key,branches in[
 ('i',f'cos({D})-sec({D})','FiniteSet(0,180,360)',[('cos','x','1',1),('cos','x','-1',1)]),
 ('ii',f'csc({D})-sec({D})','FiniteSet(45,225)',[('tan','x','1',1)]),
 ('iii',f'2*sin({D})-3*cot({D})','FiniteSet(60,300)',[('cos','x','1/2',1)]),
 ('iv',f'csc({D})**2+cot({D})**2-2',['54.7','125.3','234.7','305.3'],[('tan','x','sqrt(2)',1),('tan','x','-sqrt(2)',1)]),
 ('v',f'3*sec({D})**2-10*tan({D})',['18.4','71.6','198.4','251.6'],[('tan','x','3',1),('tan','x','1/3',1)]),
 ('vi',f'1+cot({D})**2-2*tan({D})**2','FiniteSet(45,135,225,315)',[('tan','x','1',1),('tan','x','-1',1)])]:
    items.append(roots(label,original,key,339,branches,approx=isinstance(key,list)))
add('Exercise-3A',7,75,'Solve six original equations on0°≤x≤360°:cosx=secx,cosecx=secx,2sinx=3cotx,cosec²x+cot²x=2,3sec²x−10tanx=0,and1+cot²x=2tan²x. Preserveoriginalpolesandallvalidbranches.',items,[REC,PYTH,TRANS,BND,ALL])

p=reasoning('witness','θ=45° is a valid acute solution.',
 'The task asks for an angle. Direct substitution givessin105°=cos(−15°)=(√6+√2)/4. Alternatively,sin(θ+60°)−cos(θ−60°)=(√3−1)(cosθ−sinθ)/2,so45°works. The later source derivation explicitly requests the acute instance. Do not invent a requirement to enumerate all unbounded roots.',339,'matches')
p['additional_operations']={'original_equation_residual':{'kind':'identity','operands':['sin(105*pi/180)-cos(-15*pi/180)']}}
row=add('Activity',1,75,'Find an angleθsuchthat sin(θ+60°)=cos(θ−60°);suggested graph/numerical exploration precedes the exact compound-angle method revisited onPDF77.',[p],[BND],[COMPOUND])
row['sketch_response_required']=False
row['source_interpretation']={'response_requirement':'One valid acute angle, not a mandatory graph or a proof of all unrestricted roots.',
    'optional_methods':'Rendered75 says either graph drawing or numerical search may find the solution;77 revisits it by compound-angle expansion. A graph and a compound-formula derivation are not both mandatory.',
    'mapping_basis':'The explicit bounded acute-angle solution is direct; compound-angle expansion is one optional component route, not an enforced method.'}
p.update(response_format='numeric',assessed_8227_demand_ids=[BND],component_demand_ids=[COMPOUND])
corrections.append({'item_id':row['item_id'],'continuation_pdf_pages':[77]})

p=reasoning('assumptions','The displayed geometric proof uses triangle area=base×height/2, additive areas, the triangle sine-area formula, right-triangle cosine ratios, and nonzero positive side lengths a,b.',
 'For the pictured altitudeDinsideAB,θandφareacute,a,b,hpositive,andareaABC=areaADC+areaDBC. The whole included angle isθ+φ. Heights satisfyh=a cosφ=b cosθ; substitution anddivisionbyabgive thesine-additionformula. The picturealoneproves this configuration,notall obtuse/negativeanglecases;independent analytic/Euler reasoning supports the general identity.',339,'matches')
add('Prompt',2,76,'While reading the sine-addition geometric proof, list every assumed result. The altitudeCDsplits triangleABC,withangleACD=θandDCB=φandpositive sidesa,b.',[p],[],[COMPOUND,TRI])

parts=[]
for label,left,right,method in[
 ('i','cos(x-y)','cos(x)*cos(y)+sin(x)*sin(y)','Replaceθbyπ/2−θinthe sine-additionidentityandusecofunctions;cos(θ−φ)=cosθcosφ+sinθsinφ.'),
 ('ii','cos(x+y)','cos(x)*cos(y)-sin(x)*sin(y)','Replaceφby−φinthe derived cosine-differenceidentityanduseeven cosine/oddsine.'),
 ('iii','tan(x+y)','(tan(x)+tan(y))/(1-tan(x)*tan(y))','Write tan(θ+φ)=sin(θ+φ)/cos(θ+φ),expand,anddivide numerator/denominatorbycosθcosφonlywhenbotharenonzero.'),
 ('iv','tan(x-y)','(tan(x)-tan(y))/(1+tan(x)*tan(y))','Replaceφby−φinthetangent-additionformula,retainingindividualtanandcombined-anglepoles.')]:
    p=transform(label,left,right,[],
      'All real θ,φforcosine; tangent forms additionally requirecosθcosφ!=0andcos(θ±φ)!=0.',339)
    p['method']=method+' Independently verify the resulting exact expression identity on its common domain.'
    parts.append(p)
row=add('Activity',2,76,'Derive cos(θ−φ),cos(θ+φ),tan(θ+φ),tan(θ−φ)from the prior sine forms using the stipulated substitutions/quotient method. Part(iv)continuesonPDF77.',parts,[COMPOUND])
corrections.append({'item_id':row['item_id'],'continuation_pdf_pages':[77]})

p=reasoning('validity','The sine/cosine identities hold for all real angles. The tangent quotient forms hold on the common domain: individualtansmustexistandthe relevant combined cosine/denominator mustbenonzero.',
 'sin/cosadditionfollowfromcomplexrotationorangleadditionforallrealinputs. Tangentdivisionintroducesrestrictionscosθ≠0,cosφ≠0,and1∓tanθtanφ≠0. The source sum/difference90°exceptionsarenecessarybutindividualtanvaluesmustalsoexist. Thesearecommon-domainconditions,notpermissiontosubstituteanundefinedterm.',340,'matches')
p2=value('test-60-30','Tuple(sin(pi/3+pi/6),sin(pi/3-pi/6),cos(pi/3+pi/6),cos(pi/3-pi/6),tan(pi/3-pi/6))',
 'Tuple(1,1/2,0,sqrt(3)/2,1/sqrt(3))',340,
 'Testθ=60°,φ=30°: sine/cosine sum/difference values areexact; tan(θ−φ)=1/√3. The excluded tan(θ+φ)=tan90°isundefined,anditsquotientdenominatoris0. Do not use the successful sine/cosine test as a proof of all angles.')
p2['additional_operations']={'tangent_sum_denominator':{'kind':'identity','operands':['1-tan(pi/3)*tan(pi/6)']}}
add('Prompt',3,77,'Are the four derived compound-angle results validforallθ,φ? Testthemwithθ=60°,φ=30°; the sum tangent isundefined.',[p,p2],[COMPOUND])

p=value('counterexample','Tuple(sin(pi/6+pi/3),sin(pi/6)+sin(pi/3))','Tuple(1,(1+sqrt(3))/2)',75,
 'Use the source θ=30°counterexample: sin(30°+60°)=1but sin30°+sin60°=(1+√3)/2≈1.366. This refutes additive sine without claiming the two expressions are never equal.')
add('Worked-illustration',1,75,'Unnumbered warning suppliesθ=30°to disprove sin(θ+60°)=sinθ+sin60°. Preserve its exact counterexample andapproximate rightside.',[p],[],[COMPOUND],new=True)
parts=[transform('tan-pythagorean','1+tan(x)**2','sec(x)**2',
 ['(cos(x)**2+sin(x)**2)/cos(x)**2','1/cos(x)**2'],'cos(x) != 0',73),
 transform('cot-pythagorean','1+cot(x)**2','csc(x)**2',
 ['(sin(x)**2+cos(x)**2)/sin(x)**2','1/sin(x)**2'],'sin(x) != 0',73)]
add('Worked-derivation',1,73,'The unnumbered exposition derives tan²θ+1=sec²θ by dividing sin²θ+cos²θ=1bycos²θ,and1+cot²θ=cosec²θbydividingbysin²θ. Originalzero-divisor exclusions are retained.',parts,[],[PYTH],new=True)
parts=[transform('sine-sum','sin(x+y)','sin(x)*cos(y)+cos(x)*sin(y)',[], 'all real θ,φ; the displayed triangle proof itself assumes the shown acute split/positive lengths',76),
 transform('sine-difference','sin(x-y)','sin(x)*cos(y)-cos(x)*sin(y)',[], 'all real θ,φ; substitute−φanduseodd/evenproperties',76)]
for p in parts:p['method']='The source uses triangle area andtwo altitude-cosine relations; the author independently checks the analytic sine sum/difference identities. Equivalently,Euler rotation multiplication gives the sum formula andodd/even substitution gives thedifference. A geometric acute-only picture is not itself a proof of every configuration.'
add('Worked-derivation',2,76,'Unnumbered geometric sine-addition proof followedbysine-differencefromφ→−φ. The universal identities are independently checked,withthe displayed acute triangle assumptions separatelylistedbyPrompt2.',parts,[],[COMPOUND],new=True)

figures=[]
def figure(n,page,label,note,rep,teaches,method,parent=None,kind='teaching-figure',checks=None):
    row={'item_id':f'8227:TB:Goldie:C3:Teaching-figure:{n}','item_kind':kind,'exercise':'Teaching figure','item_number':str(n),
      'pdf_page':page,'printed_page':page-14,'source_label':label,'notes':note,'what_it_shows':note,
      'assessed_8227_demand_ids':[],'component_demand_ids':[],'teaches_8227_demand_ids':teaches,'representation':rep,
      'source_evidence':ev(page),'learner_display':False,'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'not applicable',
        'quoted_value':note,'reason':'Source given/teaching representation,not a new equation response. Positive amplitude/frequency are the displayed generic-wave convention; original reciprocal poles remain open.'}],
      'value_level_scope_review_status_r5':'author actual figure values/relations read2026-11-18;independent check pending',
      'exam_representation_check':{'status':'final cross-book/examination comparison pending','examination_part_ids':[],
        'relation':'Textbook visual/support representation; no official examination award or frequency claim.'},
      'mathematical_feature_review':{'status':'author source diagram andexplicit features checked;independent acceptance pending','method':method}}
    if parent:row['parent_item_id']='8227:TB:Goldie:C3:'+parent
    if checks:row['mathematical_feature_review']['checks']=checks
    figures.append(row)
figure(1,71,'Wave photograph used for modelling estimate','The photograph is task data for estimating a metric amplitude; it has no calibrated axis or provided physical scale. Perspective,midline andphase remain judgement assumptions.','diagram',[FEATURE,INTERPRET],
 'Read as an approximate contextual model prompt,not a calibrated graph. No unique numerical geometry is claimed. The parent derivation lists necessary scale/shape assumptions.','Prompt:1','given-figure')
figure(2,71,'Figure3.1 sine amplitude and wavelength','For the displayed positive a,b convention,y=a sinbxhas amplitudeaandwavelength2π/b. Zerosat0,π/b,2π/b,3π/b alternatecrossingdirection.','graph',[FEATURE,INTERPRET],
 'At bx=π/2and3π/2the ordinatesare±a;adding2π/brepeats the argument. These features presupposea,b>0,not an unrestricted signedparameter interpretation.','Prompt:1')
for n,family,companion,poles,zeros,period in[
 (3,'csc','sin','FiniteSet(-2*pi,-pi,0,pi,2*pi)','EmptySet','2*pi'),
 (4,'sec','cos','FiniteSet(-3*pi/2,-pi/2,pi/2,3*pi/2)','EmptySet','2*pi'),
 (5,'cot','tan','FiniteSet(-2*pi,-pi,0,pi,2*pi)','FiniteSet(-3*pi/2,-pi/2,pi/2,3*pi/2)','pi')]:
    residual='sin(x)'if family in['csc','cot']else'cos(x)'
    derived_poles=compute({'kind':'bounded-trig-equation','operands':[residual,'-2*pi','2*pi']})
    assert derived_poles==expression(poles)
    if family=='cot':
        derived_zeros=compute({'kind':'bounded-trig-equation','operands':['cos(x)','-2*pi','2*pi']});assert derived_zeros==expression(zeros)
    checks={'window_radians':'[-2π,2π]','axis_unit':'degrees,−360..360','poles':poles,'zeros':zeros,'period':period,
      'range':'S.Reals'if family=='cot'else'Union(Interval(-oo,-1),Interval(1,oo))'}
    for k in range(61):
        t=-2*math.pi+4*math.pi*(k+.137)/61
        if family=='csc':f=lambda z:1/math.sin(z)
        elif family=='sec':f=lambda z:1/math.cos(z)
        else:f=lambda z:math.cos(z)/math.sin(z)
        assert abs(f(t)-f(t+float(expression(period))))<1e-8
        if family!='cot':assert abs(f(t))>=1-1e-12
        else:assert f(t+1e-7)<f(t-1e-7)
    figure(n,72,'Figure3.2 '+family+' and '+companion,
      'The blue '+family+' curve andred '+companion+' companion use−360°..360°axes. Original reciprocal poles are open; '+('cotangent decreases between sine-zero polesandhaszerosatodd90°evenwhere tangent isundefined.'if family=='cot'else'The reciprocal has nozeroandrange(−∞,−1]∪[1,∞);touching values±1occurwhere the companion is±1.'),
      'graph',[REC,SIX],
      'Derive poles from zeros of the original sin/cos denominator. Reciprocal magnitude follows from |sin|,|cos|≤1; every permitted reciprocal value is attained. Cot zeros followcos=0withsinnonzeroandits derivative−cosec²isnegative on each branch. IndependentPythonmath checks61points for periodicity andrange/orientation; these samples supplement the analytic reasoning.',checks=checks)
figure(6,74,'Figure3.3 Example3.2 tangent intersections','The tangent graph meets horizontal3and−1at71.6°,251.6°and135°,315°on0°..360°. Dashed tangent poles are not roots.','graph',[REC,PYTH,BND,ALL],
 'Parent originalsec²−4−2tanequation is independently factored andallfourroots checked againstits originalpoles. The sketch explains the two separate tangent levels.','Example:2')
figure(7,76,'Figure3.4 triangle altitude for sine addition','ABCis splitbyaltitudeCD=h;AC=b,BC=a,angleACD=θ,DCB=φ. Thus h=bcosθ=acosφandareasadd. The picturedsplit haspositive lengthsandacuteθ,φ.','diagram',[COMPOUND],
 'Right-triangle definitions give the twoheightrelations. Substituteinto the additive sine-area formula anddividebynonzeroab. The author analytic identity check extends beyond this one acute geometricconfiguration.','Worked-derivation:2')
figure(8,77,'Compound-angle formula reference panel','The three paired boxes give sine,cosineandtangent sum/difference formulas. Tangent expressions needthecommon domain,including individuallydefinedtanθ,tanφandnonzero1∓tanθtanφ.','table',[COMPOUND],
 'Allsixidentities are checked by the two sine exposition outputsandfourActivity3.2derivations;Prompt3checkscommon-domainrestrictionsandspecific60°/30°values. This isone referencepanel,not sixnewproblemtypes.')
new_items.extend(figures)
pages=[]
for page in range(71,78):
    pages.append({'pdf_page':page,'printed_page':page-14,'chapter':3,'page_status':'items enumerated',
      'item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],
      'continuation_item_ids':[r['item_id']for r in corrections if page in r['continuation_pdf_pages']],
      'source_evidence':ev(page),'non_item_content':'Allformalquestions,boxedprompts/activities,headingless mathematicalderivations/counterexample,andmathematicalfiguresenumerated. Proofequationsandtheir inlinecalloutsbelongtotheir worked derivation;theyarenotadditional independentfigures. Activity3.1isrevisitedonPDF77ratherthan countedagain.',
      'reader':'Codex author','date':'2026-11-18'})
if __name__=='__main__':
    for name,data in[
      ('answers-Goldie-C3-opening.json',{'scope':'AllsourceitemsandexplicitresponsesonPDF71–77;furtherchapter3pending.','items':answers}),
      ('census-Goldie-C3-opening.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':3,'source_path':SRC,'source_sha256':SHA,
        'scope':'PDF71–77,allformal/headinglesstasksandfigures.','new_items':new_items,'corrections':corrections,'pages':pages}),
      ('census-Goldie-C2-closing.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':2,'source_path':SRC,'source_sha256':SHA,
        'scope':'PDF70closingoutcomesonly;doesnotcompletechapter2.','new_items':[],'corrections':[],
        'pages':[{'pdf_page':70,'printed_page':56,'chapter':2,'page_status':'prose only','item_ids':[],'continuation_item_ids':[],
          'source_evidence':ev(70),'non_item_content':'Chapter2learning-outcome list only;no question,worked example ormathematicalteachingfigure.','reader':'Codex author','date':'2026-11-18'}]})]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(len(answers),'items;',len(figures),'figures;',sum(len(r['subparts'])for r in answers),'outputs')
