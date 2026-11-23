"""Fixed-source Exercise3D4–14, Goldie PDF90–91; source audit only."""
import hashlib,json
from pathlib import Path
from author_YM_C4_trig_graphs import value,graph,reasoning
from author_YM_C4_composite_equations import roots
from author_Goldie_C3_rform_intro import rform
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2]
SRC='sources/namibia/nsscas/8227-mathematics/textbooks/Goldie_Pure-Mathematics-2-and-3_2nd-edition_2018.pdf'
SHA='f030d64259ffe233a7408d2a64dea21c0a04f1ac0426439f5efaea694eb72e85'
RFORM='8227:2020:M2:T3:O02:D04';COMP='8227:2020:M2:T3:O02:D02';RANGE='8227:2020:M1:T3:O02:D02'
SKETCH='8227:2020:M1:T6:O02:D03';BND='8227:2020:M1:T6:O06:D01';ALL='8227:2020:M1:T6:O06:D02';D='(x*pi/180)'
ATTR={11:'9709,Paper22Q6,November2009',12:'9709,Paper2Q5,June2008',13:'9709,Paper3Q4,June2006',14:'9709,Paper3Q5,November2005'}
def ev(page):
    name='Goldie-key-C3-341'if page==341 else'Goldie-C3-90'
    p=W/f'checks/r5/textbooks/{name}.png'
    return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[];corrections=[]
def add(n,page,note,parts,direct,components=None,sketch=False,representation='text'):
    for p in parts:
        kp=p.pop('key_page_override',341);pp=p.pop('source_page_override',None)or page
        p.update(source_pdf_page=pp,source_evidence=ev(pp),answer_pdf_page=kp,answer_printed_page=kp-14,key_evidence=ev(kp),review_date='2026-11-18')
    has_equation=any(p.get('operation',{}).get('kind')=='bounded-trig-equation'for p in parts)
    row={'item_id':f'8227:TB:Goldie:C3:Exercise-3D:{n}','source_pdf_page':page,'notes':note,
      'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],
      'mapping_rationale':'Explicit R-forms,requested extrema/attaining angles,sketches and complete bounded solutions are assessed. Arithmetic and right-triangle projection used along the way remain components. A reciprocal of a positive affine sinusoid is not a request to define the reciprocal trigonometric functions.',
      'representation':representation,'sketch_response_required':sketch,
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'within'if has_equation else'not applicable','quoted_value':note,
        'reason':'Explicit finite interval; argument multiplier1,or2inQ8. The auxiliary phase is not rounded before solving.'if has_equation else'No periodic-equation solution requested.'},
       {'rule_id':'8227:LIMIT02','status':'within'if has_equation else'not applicable','quoted_value':note,
        'reason':'All roots are requested only in the stated finite interval; no unbounded general-solution formula.'if has_equation else'The task asks coefficient forms/features,not a general solution.'},
       {'rule_id':'8227:QUAL07','status':'within'if n in[6,7,8,9]else'not applicable','quoted_value':note,
        'reason':'Simple transformed sine/cosine extrema;Q9reciprocal denominator stays strictly positive3−√3,so reciprocal order reverses. This scalar monotonicity step needs no extra function technique.'if n in[6,7,8,9]else'No function range is asked.'}],
      'exam_style':n in ATTR,'exam_style_basis':'Printed textbook attribution:'+ATTR[n]+'. This is an internal book locator,not a newly verified original-paper match.'if n in ATTR else'Ordinary exercise without an examination attribution.',
      'precision_angle_check':{'source':'Q4/7radians;Q5/6/8–14degrees. Q11–13explicitlyrequire phase to2dp; the key instead displays1dp. Other decimal phases/roots are compared at their own written last place.',
        'comparison':'Retain exact internal phase/roots. NSSCAS final precision comes from its own question and assessment conditions,not a copied textbook convention.'},
      'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts}
    answers.append(row);return row

def fg(label,family,a,b,h,unit,lo,hi,features,status='sketch'):
    p=graph(label,family,a,b,'0',lo,hi,unit,341,features,status=status);p['operation']['phase_offset']=h;return p

def extrema(label,a,b,maxangle,minangle,unit='degree',keymax=None,keymin=None):
    R=f'sqrt(({a})**2+({b})**2)'
    p=value(label,f'Tuple({R},-{R})',f'Tuple({R},-{R})',341,
      'Derive the norm from the two original coefficients. A full sinusoidal cycle attains both±R. Derive the smallest positive attaining angle from the unrounded phase,check it in the original expression,and only then compare the printed display.')
    if keymax is not None:
        p['additional_comparisons']=[{'label':name,'operation':{'kind':'rounded','operands':[expr],'decimal_places':1},'printed_key_normalised':key}
          for name,expr,key in [('smallest-positive-maximum',maxangle,keymax),('smallest-positive-minimum',minangle,keymin)]]
    else:p['additional_comparisons']=[{'label':'smallest-positive-maximum','operation':{'kind':'identity','operands':[maxangle]},'printed_key_normalised':'2*pi/3'},
      {'label':'smallest-positive-minimum','operation':{'kind':'identity','operands':[minangle]},'printed_key_normalised':'5*pi/3'}]
    return p

add(4,90,'Express sinθ−cosθ and√7sinθ−√2cosθ as r*sin(θ−α),r>0,0<α<π/2. The second phase is an approximate0.49radian display.',[
 rform('i','1','-1','sin-minus','radian','Tuple(sqrt(2),pi/4)',341,['0','pi/2']),
 rform('ii','sqrt(7)','-sqrt(2)','sin-minus','radian','Tuple(3,49/100)',341,['0','pi/2'],2)],[RFORM],[COMP])
parts=[]
for label,a,b,key,dp in[
 ('i','-sqrt(3)','1','Tuple(2,-60)',None),('ii','-2*sqrt(2)','2*sqrt(2)','Tuple(4,-45)',None),
 ('iii','1','sqrt(3)','Tuple(2,30)',None),('iv','5','12','Tuple(13,226/10)',1),
 ('v','1','-sqrt(3)','Tuple(2,150)',None),('vi','sqrt(2)','-sqrt(2)','Tuple(2,135)',None)]:
    parts.append(rform(label,a,b,'cos-minus','degree',key,341,['-180','180'],dp))
add(5,90,'Six cosine-minus R-forms with−180°<α<180°:cosθ−√3sinθ;2√2cosθ−2√2sinθ;sinθ+√3cosθ;5sinθ+12cosθ;sinθ−√3cosθ;√2sinθ−√2cosθ. Negative and obtuse phases are required by actual coefficient signs.',parts,[RFORM],[COMP])

p=fg('iii','cos','13','1','180*atan(12/5)/pi','degree','0','360',{'amplitude':'13','period':'360','y_intercept':'5','window_range':'Interval(-13,13)'})
add(6,90,'For5cosθ−12sinθ:form r*cos(θ+α)with positive acute degree phase; state extrema;sketch0°≤θ≤360°;solve original=4on that interval. Key phase67.7°does not equalatan(12/5),which rounds67.4°.',[
 rform('i','-12','5','cos-plus','degree','Tuple(13,677/10)',341,['0','90'],1),
 value('ii','Tuple(sqrt(5**2+(-12)**2),-sqrt(5**2+(-12)**2))','Tuple(13,-13)',341),p,
 roots('iv',f'5*cos({D})-12*sin({D})-4',['4.7','220.5'],341,[('cos','x+180*atan(12/5)/pi','4/13',1)],approx=True)],
 [RFORM,RANGE,SKETCH,BND,ALL],[COMP],True)
add(7,90,'For3sinθ−√3cosθ:form r*sin(θ−α)with0<α<π/2; state extrema and smallest positive attainingθ;sketch0≤θ≤2π;solve original=√3on that interval.',[
 rform('i','3','-sqrt(3)','sin-minus','radian','Tuple(2*sqrt(3),pi/6)',341,['0','pi/2']),
 extrema('ii','3','-sqrt(3)','pi/2+atan(sqrt(3)/3)','3*pi/2+atan(sqrt(3)/3)','radian'),
 fg('iii','sin','2*sqrt(3)','1','-pi/6','radian','0','2*pi',{'amplitude':'2*sqrt(3)','period':'2*pi','y_intercept':'-sqrt(3)','window_global_max_locations':'FiniteSet(2*pi/3)','window_global_min_locations':'FiniteSet(5*pi/3)'}),
 roots('iv','3*sin(x)-sqrt(3)*cos(x)-sqrt(3)','FiniteSet(pi/3,pi)',341,[('sin','x-pi/6','1/2',1)],unit='radian')],[RFORM,RANGE,SKETCH,BND,ALL],[COMP],True)
add(8,90,'For2sin2θ+3cos2θ:form r*sin(2θ+α)with positive acute degree phase; state extrema and smallest positive attainingθ;sketch0°≤θ≤360°(two cycles);solve original=1on that interval.',[
 rform('i','2','3','sin-plus','degree','Tuple(sqrt(13),563/10)',341,['0','90'],1),
 extrema('ii','2','3','(90-180*atan(3/2)/pi)/2','(270-180*atan(3/2)/pi)/2',keymax='168/10',keymin='1068/10'),
 fg('iii','sin','sqrt(13)','2','180*atan(3/2)/pi','degree','0','360',{'amplitude':'sqrt(13)','period':'180','y_intercept':'3','window_range':'Interval(-sqrt(13),sqrt(13))'}),
 roots('iv',f'2*sin(2*{D})+3*cos(2*{D})-1',['53.8','159.9','233.8','339.9'],341,[('sin','2*x+180*atan(3/2)/pi','1/sqrt(13)',1)],approx=True)],
 [RFORM,RANGE,SKETCH,BND,ALL],[COMP],True)
p=value('iv','Tuple(1/(3-sqrt(1**2+sqrt(2)**2)),1/(3+sqrt(1**2+sqrt(2)**2)))',
 'Tuple(1/(3-sqrt(3)),1/(3+sqrt(3)))',341,
 'The denominator range is[3−√3,3+√3],strictly positive. Reciprocal is strictly decreasing there,so maximum occurs at the denominator minimum,and minimum at its maximum. Attainingθare swapped from(ii).')
p['additional_comparisons']=[{'label':label,'operation':{'kind':'rounded','operands':[expr],'decimal_places':1},'printed_key_normalised':key}
 for label,expr,key in[('smallest-positive-maximum','180+180*atan(sqrt(2))/pi','2347/10'),('smallest-positive-minimum','180*atan(sqrt(2))/pi','547/10')]]
p['assertions']=[{'expression':'sign(3-sqrt(3))','expected':'1'}]
add(9,90,'For cosθ+√2sinθ:form r*cos(θ−α)with acute degree phase; extrema and smallest positive attainingθ;sketch0°≤θ≤360°;then extrema/attainingθof1/(3+cosθ+√2sinθ). The denominator is always positive,so reciprocal extrema swap.',[
 rform('i','sqrt(2)','1','cos-minus','degree','Tuple(sqrt(3),547/10)',341,['0','90'],1),
 extrema('ii','sqrt(2)','1','180*atan(sqrt(2))/pi','180+180*atan(sqrt(2))/pi',keymax='547/10',keymin='2347/10'),
 fg('iii','cos','sqrt(3)','1','-180*atan(sqrt(2))/pi','degree','0','360',{'amplitude':'sqrt(3)','period':'360','y_intercept':'1','window_range':'Interval(-sqrt(3),sqrt(3))'}),p],
 [RFORM,RANGE,SKETCH],[COMP],True)

p=reasoning('i','12sinθ+8cosθ=13.',
 'Read120cm and80cm as perpendicular table sides and130cm as the vertical separation of parallel corridor walls. At the shown acute tilt,the vertical span is120sinθ+80cosθ. Equating it to130and dividing by10gives the stated equation. Both vertical projections are positive; do not replace the width by a slanted side.',90,'show/prove')
p['additional_operations']={'vertical_projection_reduction':{'kind':'trig-identity-residual','operands':['(120*sin(x)+80*cos(x)-130)/10','12*sin(x)+8*cos(x)-13']}}
row=add(10,90,'A120cm×80cm rectangular table touches parallel corridor walls130cm apart at the shown acute tiltθ. Show12sinθ+8cosθ=13,then find both physically admissible acute degree angles. The diagram continues onPDF91.',[
 p,roots('ii',f'12*sin({D})+8*cos({D})-13',['30.6','82.0'],341,[('sin','x+180*atan(2/3)/pi','13/(4*sqrt(13))',1)],hi='90',approx=True,opened=True)],
 [BND,ALL],[RFORM,COMP],representation='diagram')
row['direct_demand_aspects']=[{'objective_id':'8227:2020:ABILITY:08:MODEL','role':'cross-cutting modelling decision,not an extra core-demand coverage count','evidence':'Derive vertical span from the120cm×80cmrectangle and130cmcorridor shown onPDF90–91.'}]
corrections.append({'item_id':row['item_id'],'continuation_pdf_pages':[91]})
for n,a,b,target,key,rootskey,original,branches,opened in[
 (11,'4','3','cos-minus','Tuple(5,531/10)',['27.3','79.0'],f'3*cos({D})+4*sin({D})-9/2',[('cos','x-180*atan(4/3)/pi','9/10',1)],True),
 (12,'-1','5','cos-plus','Tuple(sqrt(26),113/10)',['27.02','310.4'],f'5*cos({D})-sin({D})-4',[('cos','x+180*atan(1/5)/pi','4/sqrt(26)',1)],False),
 (13,'24','7','cos-minus','Tuple(25,737/10)',['20.6','126.9'],f'7*cos({D})+24*sin({D})-15',[('cos','x-180*atan(24/7)/pi','3/5',1)],False)]:
    p=rform('i',a,b,target,'degree',key,341,['0','90'],2)
    p['printed_precision_requirement']={'requested_decimal_places':2,'printed_decimal_places':1,'status':'key incomplete','reason':'The question explicitly asks2decimalplaces; the printed answer gives only1. The unrounded phase remains independently derived.'}
    add(n,91,{11:'For3cosx+4sinx,form R*cos(x−α),R>0,0°<α<90°,αto2dp;hence solve original=4.5strictly0°<x<360°.',
      12:'For5cosθ−sinθ,form R*cos(θ+α),R>0,0°<α<90°,αto2dp;hence solve original=4on0°≤θ≤360°.',
      13:'For7cosθ+24sinθ,form R*cos(θ−α),R>0,0°<α<90°,αto2dp;hence solve original=15on0°≤θ≤360°.'}[n],
      [p,roots('ii',original,rootskey,341,branches,approx=True,opened=opened)],[RFORM,BND,ALL],[COMP])
p=roots('roots',f'8*sin({D})-6*cos({D})-7',['81.3','172.4'],341,[('sin','x-180*atan(3/4)/pi','7/10',1)],approx=True)
p['additional_operations']={'required_working_R_form':{'kind':'r-form-coefficients','operands':['8','-6'],'target':'sin-minus','angle_unit':'degree','phase_bounds':['0','90'],'left_open':True,'right_open':True}}
add(14,91,'By expressing8sinθ−6cosθas R*sin(θ−α),solve original=7on0°≤θ≤360°. The R-form is explicitly required working,not an extra separately numbered answer.',[p],[RFORM,BND,ALL],[COMP])

figures=[{'item_id':'8227:TB:Goldie:C3:Teaching-figure:23','item_kind':'given-figure','exercise':'Given figure','item_number':'23',
 'pdf_page':91,'printed_page':77,'source_label':'Exercise3D10 table/corridor geometry','notes':'Rotated rectangular120cm×80cmtable between parallel walls130cmapart;θis the acute angle between the120cmlong side and the lower wall. A right-angle marker fixes perpendicular sides. Vertical span is the sum of their vertical projections.',
 'what_it_shows':'The acute angle and both perpendicular side lengths determine120sinθ+80cosθ,which must equal the130cmwall separation.',
 'assessed_8227_demand_ids':[],'component_demand_ids':[],'teaches_8227_demand_ids':[BND,ALL,RFORM],'representation':'diagram',
 'source_evidence':ev(91),'parent_item_id':'8227:TB:Goldie:C3:Exercise-3D:10','learner_display':False,
 'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'within','quoted_value':'12sinθ+8cosθ=13,0°<θ<90°',
  'reason':'Multiplier1andfinite acute geometry domain.'}],
 'value_level_scope_review_status_r5':'author actual dimensions/angle/parallel-wall geometry checked2026-11-18; independent check pending',
 'exam_representation_check':{'status':'final cross-book/examination comparison pending','examination_part_ids':[],
  'relation':'Internal textbook modelling diagram; not evidence of examination frequency.'},
 'mathematical_feature_review':{'status':'author source render/projection derivation/both original-equation roots checked; independent acceptance pending',
  'method':'Read side lengths130,120,80andright-angle marker; derive both projections without using diagram scale. Verify two acute roots by original span and compare the separately transcribed key.'}}]
pages=[{'pdf_page':page,'printed_page':page-14,'chapter':3,'page_status':'items enumerated',
 'item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],
 'continuation_item_ids':[r['item_id']for r in corrections if page in r['continuation_pdf_pages']],
 'source_evidence':ev(page),'non_item_content':'All Exercise3D4–14parts and the continuing corridor diagram enumerated. Examination attributions are book statements,not newly verified source-paper provenance.',
 'reader':'Codex author','date':'2026-11-18'}for page in[90,91]]
if __name__=='__main__':
    for name,data in[
      ('answers-Goldie-C3-rform-exercises.json',{'scope':'Every Exercise3D4–14response onPDF90–91. Source key341,each item internal.','items':answers}),
      ('census-Goldie-C3-rform-exercises.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':3,'source_path':SRC,'source_sha256':SHA,
        'scope':'PDF90–91alltasks/continuations/given figures.','new_items':figures,'corrections':corrections,'pages':pages})]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(len(answers),'items;',len(figures),'figures;',sum(len(r['subparts'])for r in answers),'outputs')
