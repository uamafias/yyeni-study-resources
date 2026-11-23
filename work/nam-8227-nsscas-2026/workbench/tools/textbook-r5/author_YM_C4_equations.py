"""Fixed textbook source transcriptions: bounded trig equations, YM PDF202–208."""
import json,hashlib
from pathlib import Path
from author_YM_C4_trig_graphs import value
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2]
SRC='Y=mc as textbook.pdf';SHA='0b44ad3b67b1ea3de90cba780382d77deef347fae683cf6e28677f36c17a724f'
BND='8227:2020:M1:T6:O06:D01';ALL='8227:2020:M1:T6:O06:D02';REC='8227:2020:M2:T3:O01:D01'
PRINCIPAL='8227:2020:M1:T6:O04:D01'
BASIC='8227:2020:M1:T6:O01:D01';SKETCH='8227:2020:M1:T6:O02:D03'
def ev(page):
    name='YM-key-611-bounded'if page==611 else'YM-C4-201'if page<=204 else'YM-C4-205'
    p=W/f'checks/r5/textbooks/{name}.png'
    return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def eq(label,fn,arg,target,key,unit='degree',lo='0',hi=None,power=1,approx=False,dp=None,open_bounds=False,statement=None):
    hi=hi or('360'if unit=='degree'else'2*pi');scale='pi/180'if unit=='degree'else'1'
    expression=f'{fn}(({arg})*({scale}))**{power}-({target})'
    p={'subpart':label,'operation':{'kind':'bounded-trig-equation','operands':[expression,lo,hi],
       'left_open':open_bounds,'right_open':open_bounds},'review_date':'2026-11-18',
       'source_angle_unit':unit,'source_argument':arg,'source_equation':statement or f'{fn}({arg})^{power}={target}',
       'method':'Independently solve the original finite-interval equation, preserving every root and endpoint restriction. Convert the entire angle argument to radians only for the symbolic evaluator; source answers retain their original angular unit. Compare the printed exact set or each rounded value only after the complete exact solution set has been derived.'}
    p['source_ratio_model']={'function':fn,'argument':arg,'ratio':target,'power':power,'angle_unit':unit}
    if approx:
        p['printed_key_approximate_values']=key
        if dp is not None:p['key_decimal_places']=dp
    else:p['printed_key_normalised']=key
    return p
answers=[]
def add(kind,n,page,note,parts,reciprocal=False):
    for p in parts:
        kp=p.pop('key_page_override',page if kind=='Example' else 611)
        p.update(source_pdf_page=page,source_evidence=ev(page),answer_pdf_page=kp,
          answer_printed_page='A'+str(kp-586)if kp>=602 else kp-12,key_evidence=ev(kp))
    direct=[BND,ALL]+([REC]if reciprocal else[])
    row={'item_id':f'8227:TB:YM:C4:{kind}:{n}','source_pdf_page':page,'notes':note,
      'assessed_8227_demand_ids':direct,'component_demand_ids':[PRINCIPAL],
      'component_demand_roles':{PRINCIPAL:'The source reference-angle method uses an inverse function to obtain a basic angle. This is a supporting method component; no standalone principal-value response is asked, and a valid graphical/special-angle method can avoid it.'},
      'mapping_rationale':'The learner must solve within the stated interval and recover all admissible roots. A special value appearing in an equation does not by itself make separate exact-ratio evaluation assessed when calculator/graph methods are allowed. Reciprocal conversion is directly relevant when the asked equation uses sec,cosec orcot; no implicit differentiation or graph-sketch response is invented.',
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'within',
        'quoted_value':'; '.join(p.get('source_equation','')+'; argument='+p.get('source_argument','')for p in parts),
        'reason':'Actual source multipliers are1,2,3 or1/2; only small integer/simple fractional multipliers occur. Every original finite interval is retained; shifts are part of the angle, not extra radians.'},
       {'rule_id':'8227:LIMIT02','status':'within','quoted_value':note,
        'reason':'Only finite bounded solution sets are asked for; general forms of solution are not introduced.'}],
      'exam_style':False,'exam_style_basis':'Ordinary Example/TryNow, not labelled exam-style and not attributed to an examination.',
      'precision_angle_check':{'source':'Degrees are generally given to1decimal place; radian keys usually3significant figures, with some extra digits. Explicit exact special-angle answers are preserved.',
       'comparison':'Source advice to round a basic angle before later transformations is a book convention, not a new NSSCAS marking rule. The check retains full intermediate accuracy. A more accurate printed approximation is not rejected merely because it has an extra digit.'},
      'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts}
    answers.append(row);return row

add('Example',38,202,'Solve sinθ=−0.5 on0°≤θ≤360°; the source presents both graph intersections and quadrant/reference-angle methods.',
 [eq('roots','sin','x','-1/2','FiniteSet(210,330)')])
add('Try-Now',38,203,'Twelve basic sine/cosine/tangent equations on0°≤θ≤360°, correct to1decimal place: positive and negative non-special ratios as well as .5,1,√3/2.',
 [eq(label,fn,'x',target,key,approx=True,dp=1)for label,fn,target,key in[
 ('a','cos','1/2',['60','300']),('b','tan','1',['45','225']),('c','sin','sqrt(3)/2',['60','120']),
 ('d','sin','0.6',['36.9','143.1']),('e','cos','-0.7',['134.4','225.6']),('f','tan','2.5',['68.2','248.2']),
 ('g','cos','0.456',['62.9','297.1']),('h','sin','-0.843',['237.5','302.5']),('i','tan','-3.481',['106.0','286.0']),
 ('j','sin','0.75',['48.6','131.4']),('k','sin','-0.707',['225.0','315.0']),('l','tan','-1.863',['118.2','298.2'])]])
add('Example',39,203,'Solve secx=2.1 on0°≤x≤180°; reciprocal cosine conversion leaves only the quadrantI root, reported61.6°.',
 [eq('roots','sec','x','2.1',['61.6'],hi='180',approx=True,dp=1)],True)
add('Try-Now',39,203,'Six reciprocal equations on90°≤x≤360°, correct to1decimal place: cosecx=2,secx=−2,cotx=−1,secx=2.987,cotx=2.11,cosecx=−2.5.',
 [eq(label,fn,'x',target,key,lo='90',approx=True,dp=1)for label,fn,target,key in[
 ('a','csc','2',['150']),('b','sec','-2',['120','240']),('c','cot','-1',['135','315']),
 ('d','sec','2.987',['289.6']),('e','cot','2.11',['205.4']),('f','csc','-2.5',['203.6','336.4'])]],True)
add('Example',40,204,'Solve2tanx+√5=0 between0and2π in radians; both negative-tangent quadrants are needed and the worked answers are2.30,5.44.',
 [eq('roots','tan','x','-sqrt(5)/2',['2.30','5.44'],unit='radian',approx=True,open_bounds=True,statement='2tanx+√5=0')])
add('Try-Now',40,204,'Six radian equations between0and2π: cosx=−3/7,cotx=−2.9,tanx=6,7sinx=4,3secx=√17,4cosecx+√29=0. Preserve each complete pair.',
 [eq(label,fn,'x',target,key,unit='radian',approx=True,open_bounds=True,statement=stmt)for label,fn,target,key,stmt in[
 ('a','cos','-3/7',['2.01','4.27'],'cosx=−3/7'),('b','cot','-2.9',['2.81','5.95'],'cotx=−2.9'),
 ('c','tan','6',['1.406','4.55'],'tanx=6'),('d','sin','4/7',['0.608','2.53'],'7sinx=4'),
 ('e','sec','sqrt(17)/3',['0.756','5.53'],'3secx=√17'),('f','csc','-sqrt(29)/4',['3.98','5.45'],'4cosecx+√29=0')]],True)
row=add('Example',41,204,'The source asks cos²y=0.25 but prints the interval0°≤θ≤360° for a different variable. Its working consistently solves y on that interval, yielding60°,120°,240°,300°; the variable mismatch is a source-print defect.',
 [eq('roots','cos','x','1/4','FiniteSet(60,120,240,300)',power=2)])
row['source_interpretation']='The recorded answer adopts the intended y interval evidenced by the worked solution; the literal mismatched-variable stem is not silently treated as unambiguous.'
add('Try-Now-41',1,205,'Find all angles0°..360°inclusive satisfying cos²y=1/8. Both cosine signs yield four roots, not only the positive square root.',
 [eq('roots','cos','x','1/8',['69.3','110.7','249.3','290.7'],power=2,approx=True,dp=1)])
add('Try-Now-41',2,205,'Solve cosec²y=8/7 on0≤y≤π. The positive-sine interval leaves two interior radian roots; sine zero endpoints are undefined.',
 [eq('roots','csc','x','8/7',['1.21','1.93'],unit='radian',hi='pi',power=2,approx=True)],True)
add('Example',42,205,'Solve sinθ=.25 on−2π≤θ≤0. The two coterminal roots must remain negative; source working gives−3.39 and−6.03radians.',
 [eq('roots','sin','x','1/4',['-3.39','-6.03'],unit='radian',lo='-2*pi',hi='0',approx=True)])
add('Try-Now-42',1,205,'Solve cosθ=.642 on−2π≤θ≤0; a positive key value cannot satisfy the original interval.',
 [eq('roots','cos','x','0.642',['-0.874','5.41'],unit='radian',lo='-2*pi',hi='0',approx=True)])
row=add('Try-Now-42',2,205,'Solve tanθ=−.255 on−180°≤θ≤0°. The printed numerical root−14.3°is valid, but its key quadrant label must be checked separately.',
 [eq('roots','tan','x','-0.255',['-14.3'],lo='-180',hi='0',approx=True,dp=1)])
row['source_label_warning']='The key labels−14.3°as Quad3, but its positive coterminal angle345.7°is quadrantIV. Numerical answer and quadrant label have separate dispositions.'
add('Try-Now-42',3,205,'Solve cosθ=−.325 on−270°≤θ≤0°; both negative representatives−109.0°and−251.0°remain in the interval.',
 [eq('roots','cos','x','-0.325',['-109.0','-251.0'],lo='-270',hi='0',approx=True,dp=1)])
add('Try-Now-42',4,205,'Solve cosθ=.75 andtanθ=2 separately on−π≤θ≤π; one cosine pair is symmetric and the tangent pair differs byπ.',
 [eq('a','cos','x','0.75',['0.723','-0.723'],unit='radian',lo='-pi',hi='pi',approx=True),
  eq('b','tan','x','2',['1.11','-2.03'],unit='radian',lo='-pi',hi='pi',approx=True)])
add('Example',43,206,'Solve sin2θ=.5 andsin(θ/2)=.5 on0°≤θ≤360°; transform the argument interval before finding every original-angle root. Two input cycles versus half a cycle give different root counts.',
 [eq('a','sin','2*x','1/2','FiniteSet(15,75,195,255)'),eq('b','sin','x/2','1/2','FiniteSet(60,300)')])
add('Try-Now',43,207,'On0°≤θ≤360°, solve cos2θ=−.5,tan2θ=1,cos(θ/2)=.4,sin(θ/2)=−.4. The last has no solution because the half-angle lies in0°..180°.',
 [eq('a','cos','2*x','-1/2','FiniteSet(60,120,240,300)'),
  eq('b','tan','2*x','1','FiniteSet(45/2,225/2,405/2,585/2)'),
  eq('c','cos','x/2','0.4',['132.8'],approx=True,dp=1),
  eq('d','sin','x/2','-0.4','EmptySet')])
add('Example',44,207,'Solve2cos2θ+√3=0 strictly between0and2π. Four exact roots are5π/12,7π/12,17π/12,19π/12; enumerate both argument turns before dividing by2.',
 [eq('roots','cos','2*x','-sqrt(3)/2','FiniteSet(5*pi/12,7*pi/12,17*pi/12,19*pi/12)',unit='radian',open_bounds=True,statement='2cos2θ+√3=0')])
add('Try-Now',44,207,'Four radian equations between0and2π: sin2θ=−1/√2,cot3θ=−.7,sin(θ/2)=.2,andcos(θ/2)+(−√3/2)=0. Enlarged stems confirm both easily missed negative signs. Multipliers2,3,1/2 require different argument windows.',
 [eq('a','sin','2*x','-1/sqrt(2)','FiniteSet(5*pi/8,7*pi/8,13*pi/8,15*pi/8)',unit='radian',open_bounds=True),
  eq('b','cot','3*x','-0.7',['0.727','1.77','2.82','3.87','4.92','5.96'],unit='radian',approx=True,open_bounds=True),
  eq('c','sin','x/2','0.2',['0.421','5.86'],unit='radian',approx=True,open_bounds=True),
  eq('d','cos','x/2','sqrt(3)/2','FiniteSet(pi/3)',unit='radian',open_bounds=True,statement='cos(θ/2)+(−√3/2)=0')],True)
add('Example',45,208,'Solve tan(2θ−78°)=−1.57 on0°≤θ≤360°; the transformed interval−78°..642° includes a negative representative and four original roots.',
 [eq('roots','tan','2*x-78','-1.57',['100.2','10.2','280.2','190.2'],approx=True,dp=1)])
add('Try-Now-45',1,208,'Four shifted equations on0°≤θ≤360°: cos(2θ−15°)=−.145;cosec(2θ+15°)=1.333;sin(θ/2−27°)=.6;3sec²(θ/2+30°)=4. Closed endpoints matter in the last part.',
 [eq('a','cos','2*x-15','-0.145',['56.7','138.3','236.7','318.3'],approx=True,dp=1),
  eq('b','csc','2*x+15','1.333',['16.8','58.2','196.8','238.2'],approx=True,dp=1),
  eq('c','sin','x/2-27','0.6',['127.7','340.3'],approx=True,dp=1),
  eq('d','sec','x/2+30','4/3','FiniteSet(0,240,360)',power=2)],True)
add('Try-Now-45',2,208,'Solve2sin(2θ+30°)+√3=0 on−360°<θ≤360°; list all eight positive and negative representatives, without a general solution formula.',
 [eq('roots','sin','2*x+30','-sqrt(3)/2','FiniteSet(105,135,285,315,-45,-75,-225,-255)',lo='-360',statement='2sin(2θ+30°)+√3=0')])
answers[-1]['subparts'][0]['operation']['left_open']=True

# Both unnumbered worked columns in the reminder are inventoried individually.
# Their displayed acute representatives do not claim a complete unbounded set.
illustrations=[]
for n,expr,key,note in[
 (1,'asin(3/8)*180/pi','22.0','The2sinθ=.75 column derives the acute representative asin(.375)=22.0°, illustrating an output multiplier; no full solution interval is supplied.'),
 (2,'asin(3/4)*90/pi','24.3','The sin2θ=.75 column derives the acute representative asin(.75)/2=24.3°, illustrating an input multiplier. Its intermediate line mislabels θ as2θ after division.')]:
    p=value('acute-illustration',expr,key,205,'Independently evaluate the displayed acute example from the original fixed ratio, retaining full internal accuracy and rounding the final illustrative value to1decimal place. This does not assert a complete equation solution set without a stated interval.')
    p['operation']={'kind':'rounded','operands':[expr],'decimal_places':1};p['source_equation']=note;p['source_argument']='x'if n==1 else'2*x'
    p['review_date']='2026-11-18'
    row=add('Illustration-multiplier-comparison',n,205,note,[p])
    row.update(assessed_8227_demand_ids=[],component_demand_ids=[],
      mapping_rationale='A teaching-only acute illustration of the position of a multiplier; it is not a separately asked bounded-equation task and does not earn whole-demand coverage.',
      value_level_scope_decisions=[{'rule_id':'8227:QUAL03','status':'within','quoted_value':'Output factor2 or input factor2, ratio.75','reason':'Both fixed illustrations use a small integer factor; their unstated full interval is not invented.'}])
    row['subparts'][0]['answer_pdf_page']=205;row['subparts'][0]['answer_printed_page']=193;row['subparts'][0]['key_evidence']=ev(205)
    illustrations.append({'item_id':row['item_id'],'item_kind':'worked-illustration','exercise':'Unnumbered multiplier comparison','item_number':str(n),
      'pdf_page':205,'printed_page':193,'notes':note,'assessed_8227_demand_ids':[],'component_demand_ids':[],
      'representation':'text','source_evidence':ev(205),'learner_display':False,
      'evidence_role':'prerequisite/supporting inline worked illustration; no directly assessed bounded-equation coverage'})

figures=[]
specs=[
 (202,'Example38 sine intersections','Sine over0°..360°intersects y=−.5 at210°and330°, in quadrantsIII/IV.','Example:38',[BASIC,BND,ALL],'graph'),
 (202,'Example38 reference-angle CAST','The negative-sine rays have reference30°in quadrantsIII/IV.','Example:38',[BND,ALL],'diagram'),
 (203,'Example39 restricted CAST','Positive cosine permitsI/IV globally, but the0°..180°interval keeps onlyI.','Example:39',[BND,ALL,REC],'diagram'),
 (203,'Six reciprocal conversions','Each of sin,cos,tan,cot,sec,cosec is paired with the reciprocal of its partner, on common defined domains.',None,[REC],'table'),
 (204,'Example40 negative tangent CAST','QuadrantsII/IVand reference atan(√5/2)give both radian roots.','Example:40',[BND,ALL],'diagram'),
 (204,'Example41 all-sign cosine CAST','Cos²y=.25 requires cos y=±.5; all four quadrant rays are shown. The stem mismatches y with a θ interval.','Example:41',[BND,ALL],'diagram'),
 (205,'Example42 clockwise sine CAST','Positive sine gives clockwise representatives in[−2π,0], both negative.','Example:42',[BND,ALL],'diagram'),
 (205,'Output multiplier versus input multiplier','The reminder compares2sinθ=.75 withsin2θ=.75 using a single acute illustrative angle; it does not claim these are complete bounded solution sets.',None,[BND],'table'),
 (206,'Example43a two-turn CAST','For sin2θ=.5, the argument2θ spans0°..720°before division by2.','Example:43',[BND,ALL],'diagram'),
 (206,'Example43a double-frequency sine','The sine2θ graph marks15°,75°,195°,255°at height.5 on0°..360°.','Example:43',[BND,ALL,SKETCH],'graph'),
 (206,'Example43b half-turn CAST','For sin(θ/2)=.5, the argument spans0°..180°only; quadrantsIII/IVare excluded.','Example:43',[BND,ALL],'diagram'),
 (206,'Example43b half-frequency sine','The half-frequency sine graph on0°..360°meets.5 at60°and300°.','Example:43',[BND,ALL,SKETCH],'graph'),
 (207,'Example44 exact reference triangle','A1,√3,2triangle supplies cos(π/6)=√3/2; the negative cosine sign is selected separately.','Example:44',[BND,ALL],'diagram'),
 (207,'Example44 radian CAST','Cosine negative inII/III; the argument2θcovers two turns, yielding four roots.','Example:44',[BND,ALL],'diagram'),
 (208,'Example45 shifted argument CAST','The transformed argument spans−78°..642°; a negative representative and later turns must all be retained before reversing the affine transform.','Example:45',[BND,ALL],'diagram')]
for n,(page,label,note,parent,teaches,rep)in enumerate(specs,122):
    figures.append({'item_id':f'8227:TB:YM:C4:Teaching-figure:{n}','item_kind':'teaching-figure','exercise':'Teaching figure','item_number':str(n),
     'pdf_page':page,'printed_page':page-12,'source_label':label,'parent_item_id':f'8227:TB:YM:C4:{parent}'if parent else None,
     'notes':note,'what_it_shows':note,'assessed_8227_demand_ids':[],'component_demand_ids':[],'teaches_8227_demand_ids':teaches,
     'representation':rep,'source_evidence':ev(page),'learner_display':False,
     'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'within','quoted_value':note,'reason':'Actual shown arguments are a single angle or small/simple multiplier; not general solution formulae.'}],
     'value_level_scope_review_status_r5':'author original intervals,argument scaling and ray/root labels read2026-11-18; independent check pending',
     'exam_representation_check':{'status':'final cross-book/examination comparison pending','examination_part_ids':[],
       'relation':'Worked-method teaching representation,not an independently assessed sketch or examination-frequency claim.'},
     'mathematical_feature_review':{'status':'author graph/diagram features checked against parent equation roots; independent acceptance pending',
       'method':'Graph intersections are verified by exact function substitution and complete bounded root sets; quadrant rays are compared with signs and interval restrictions. No pixel or proprietary-software comparison is claimed.'}})
    figure=figures[-1]
    if parent:
        source=next(r for r in answers if r['item_id']==f'8227:TB:YM:C4:{parent}')
        part='a'if 'Example43a'in label else'b'if 'Example43b'in label else None
        figure['parent_subpart']=part
        own=[p for p in source['subparts']if part is None or p['subpart']==part]
        figure['value_level_scope_decisions'][0]['quoted_value']='; '.join(p['source_equation']for p in own)
    else:
        figure['value_level_scope_decisions']=[{'rule_id':'8227:QUAL03','status':'within'if n==129 else'not applicable',
          'quoted_value':'2sinθ=.75 compared withsin2θ=.75'if n==129 else'sin=1/cosec,cos=1/sec,tan=1/cot and reverse reciprocal relationships',
          'reason':'Actual output/input factor2in the comparison.'if n==129 else'This table teaches reciprocal definitions; it is not a bounded multiplier equation.'}]
pages=[]
for page in range(202,209):
 pages.append({'pdf_page':page,'printed_page':page-12,'chapter':4,'page_status':'items enumerated',
  'item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],
  'continuation_item_ids':[],'source_evidence':ev(page),
  'non_item_content':'All formal tasks,inline worked columns and mathematical teaching figures/tables enumerated. The comparison reminder onPDF205has two separately recorded illustrative columns,not additional full solution-set exercises.',
  'reader':'Codex author','date':'2026-11-18'})
if __name__=='__main__':
 for name,data in[
  ('answers-YM-C4-equations.json',{'scope':'All21formal items and2unnumbered worked illustrations onPDF202–208; bounded equations are independently solved before printed approximations are compared.','items':answers}),
  ('census-YM-C4-equations.json',{'book':'YM','book_id':'8227-SRC-017','chapter':4,'source_path':SRC,'source_sha256':SHA,
   'scope':'PDF202–208inclusive; formal tasks,unnumbered worked columns and all mathematical teaching diagrams/graphs/tables.','new_items':figures+illustrations,'corrections':[],'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 print(len(answers),'items;',len(figures),'figures;',sum(len(r['subparts'])for r in answers),'equations')
