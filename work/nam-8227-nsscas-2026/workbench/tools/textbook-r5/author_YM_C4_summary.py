"""Census and fixed mathematical checks of the three C4 summary pages."""
import hashlib,json,sys
from pathlib import Path
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2]
sys.path.insert(0,str(W/'tools'))
from verify_textbook_answers_r5 import compute,expression,equivalent
SRC='Y=mc as textbook.pdf';SHA='0b44ad3b67b1ea3de90cba780382d77deef347fae683cf6e28677f36c17a724f'
CONV='8227:2020:M1:T5:O01:D02';ARC='8227:2020:M1:T5:O02:D01';AREA='8227:2020:M1:T5:O02:D02'
EXACT='8227:2020:M1:T6:O03:D01';BASIC='8227:2020:M1:T6:O01:D01';P='8227:2020:M1:T6:O04:D01'
FEATURE='8227:2020:M1:T6:O02:D01';TRANS='8227:2020:M1:T6:O05:D02';REC='8227:2020:M2:T3:O01:D01';PYTH='8227:2020:M2:T3:O02:D01'
def ev():
    p=W/'checks/r5/textbooks/YM-C5-229.png'
    return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def scalar(expr,target):return {'operation':{'kind':'identity','operands':[expr]},'source_normalised':target}
def identity(left,right,domain='All real angles on the common domain of the written expressions'):
    return {'operation':{'kind':'trig-identity-residual','operands':[left,right]},'source_normalised':'0','original_common_domain':domain}
figures=[]
def add(n,page,label,note,teaches,checks,rep='diagram'):
    results=[]
    for c in checks:
        derived=compute(c['operation'])
        if c.get('source_features'):
            assert all(equivalent(derived[k],expression(v))for k,v in c['source_features'].items()),(label,derived)
        else:assert equivalent(derived,expression(c['source_normalised'])),(label,derived,c)
        results.append({**c,'derived':str(derived),'comparison':'agrees with source feature/formula; author check, independent acceptance pending'})
    figures.append({'item_id':f'8227:TB:YM:C4:Teaching-figure:{n}','item_kind':'teaching-figure','exercise':'Teaching figure','item_number':str(n),
      'pdf_page':page,'printed_page':page-12,'source_label':label,'notes':note,'what_it_shows':note,
      'assessed_8227_demand_ids':[],'component_demand_ids':[],'teaches_8227_demand_ids':teaches,
      'representation':rep,'source_evidence':ev(),'learner_display':False,
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL08','status':'within'if P in teaches else'not applicable',
        'quoted_value':note,'reason':'Principal inverse branches and their endpoint inclusion are retained; tangent input branch and inverse output range are open.'if P in teaches else'Formula/diagram reference,not inverse construction or a periodic equation to solve.'}],
      'value_level_scope_review_status_r5':'author summary values/formulas read2026-11-18; independent check pending',
      'exam_representation_check':{'status':'final cross-book/examination comparison pending','examination_part_ids':[],
        'relation':'Textbook summary teaching representation,not an assessed task or official award.'},
      'mathematical_feature_review':{'status':'rendered summary read and every stated check independently computed; independent acceptance pending',
        'method':'Derive from exact circle/triangle relations or original analytic trig functions. Formula assertions use their common defined domain; graph domains/ranges and endpoint conventions are explicit.',
        'checks':results}})

add(187,229,'Degree/radian conversion flow','Degree input multiplies byπ/180 to become radians; reverse flow multiplies by180/π,or divides byπ/180. The reverse arrow is read right to left,not as a reversed division expression.',[CONV],
 [scalar('180*pi/180','pi'),scalar('pi/(pi/180)','180'),scalar('(pi/180)*(180/pi)','1')])
add(188,229,'Degree arc diagram','Circle centreO,radiusr,angle x°; arcAB=(x/360)2πr. The central angle determines that minor arc,not its chord.',[ARC,CONV],
 [identity('x*2*pi*p/360','p*(x*pi/180)')])
add(189,229,'Radian arc diagram','Circle centreO,radiusr,angleθradians; arcAB=s=rθ. This follows from the central angle fractionθ/(2π).',[ARC],
 [identity('x*2*pi*p/(2*pi)','p*x')])
add(190,229,'Degree sector diagram','The shaded sector has radiusr,angle x° andarea(x/360)πr². Its straight edges are both radii.',[AREA,CONV],
 [identity('x*pi*p**2/360','p**2*(x*pi/180)/2')])
add(191,229,'Radian sector diagram','The shaded sector has radiusr,angleθradians andarea r²θ/2; no segment/chord subtraction is shown.',[AREA],
 [identity('x*pi*p**2/(2*pi)','p**2*x/2')])
add(192,230,'30/60 special-angle triangle','A right triangle with hypotenuse2 andlegs1,√3 has acute angles30°and60°. Opposite/adjacent labels determine the ratios.',[EXACT],
 [scalar('1**2+sqrt(3)**2-2**2','0'),scalar('atan(1/sqrt(3))','pi/6')])
add(193,230,'30/60 exact ratio table','The table gives sin30=1/2,cos30=√3/2,tan30=1/√3;sin60=√3/2,cos60=1/2,tan60=√3.',[EXACT],
 [scalar('Tuple(sin(pi/6),cos(pi/6),tan(pi/6),sin(pi/3),cos(pi/3),tan(pi/3))','Tuple(1/2,sqrt(3)/2,1/sqrt(3),sqrt(3)/2,1/2,sqrt(3))')],'table')
add(194,230,'45-degree exact ratio triangle','The right isosceles triangle has legs1,1,hypotenuse√2 andboth acute angles45°.',[EXACT],
 [scalar('1**2+1**2-sqrt(2)**2','0'),scalar('atan(1)','pi/4')])
add(195,230,'0/45/90 exact ratio table','Sine rows0,1/√2,1;cosine rows1,1/√2,0;tangent0,1,undefined. The90°tangent pole is not a finite value.',[EXACT],
 [scalar('Tuple(sin(0),sin(pi/4),sin(pi/2),cos(0),cos(pi/4),cos(pi/2),tan(0),tan(pi/4))','Tuple(0,1/sqrt(2),1,1,1/sqrt(2),0,0,1)'),scalar('cos(pi/2)','0')],'table')
add(196,230,'CAST quadrant sign diagram','QuadrantsI,II,III,IV correspond to allpositive,sinepositive,tangentpositive,cosinepositive; their reference-angle rays areβ,180−β,180+β,360−β.',[EXACT,BASIC],
 [scalar('Tuple(sign(sin(pi/4)),sign(cos(pi/4)),sign(tan(pi/4)),sign(sin(3*pi/4)),sign(cos(3*pi/4)),sign(tan(3*pi/4)),sign(sin(5*pi/4)),sign(cos(5*pi/4)),sign(tan(5*pi/4)),sign(sin(7*pi/4)),sign(cos(7*pi/4)),sign(tan(7*pi/4)))','Tuple(1,1,1,1,-1,-1,-1,-1,1,-1,1,-1)')])
add(197,230,'Nine related-angle formulas','The sine row is sin(180−β)=sinβ,sin(180+β)=−sinβ,sin(360−β)=−sinβ. Cosine andtangent use their correct quadrant signs. A4xcrop confirms the final sine minus sign that is faint on the contact sheet.',[EXACT,TRANS],
 [identity(left,right)for left,right in[
  ('sin(pi-x)','sin(x)'),('sin(pi+x)','-sin(x)'),('sin(2*pi-x)','-sin(x)'),
  ('cos(pi-x)','-cos(x)'),('cos(pi+x)','-cos(x)'),('cos(2*pi-x)','cos(x)'),
  ('tan(pi-x)','-tan(x)'),('tan(pi+x)','tan(x)'),('tan(2*pi-x)','-tan(x)')]],'table')
add(198,230,'Negative-angle unit-circle diagram','The ray at−θis the reflection across the x-axis of the ray atθ; cosis unchanged,sin changes sign,andthe clockwise ray is coterminal with360°−θ.',[BASIC,EXACT],
 [identity('cos(-x)','cos(x)'),identity('sin(-x)','-sin(x)')])
add(199,230,'Negative-angle formula table','Sine andtangent are odd; cosine is even. Tangent formulas hold only away from its poles.',[TRANS],
 [identity('sin(-x)','-sin(x)'),identity('cos(-x)','cos(x)'),identity('tan(-x)','-tan(x)')],'table')
add(200,230,'Complementary-angle triangle','The two acute angles areθand90°−θin a right triangle; opposite andadjacent roles interchange.',[EXACT],
 [identity('sin(pi/2-x)','cos(x)'),identity('cos(pi/2-x)','sin(x)')])
add(201,230,'Complementary-angle formula table','sin(90°−θ)=cosθ,cos(90°−θ)=sinθ,andtan(90°−θ)=cotθwhere both sides are defined.',[TRANS,REC],
 [identity('sin(pi/2-x)','cos(x)'),identity('cos(pi/2-x)','sin(x)'),identity('tan(pi/2-x)','cot(x)','sin(x) != 0')],'table')
add(202,230,'Reciprocal quotient and Pythagorean summary table','Eight formulas group reciprocal identities,cot/tanquotients,andthree Pythagorean identities. Reciprocal/quotient common domains exclude zero denominators; do not extend equal expressions through an original pole.',[REC,PYTH,TRANS],
 [identity(left,right)for left,right in[
  ('csc(x)','1/sin(x)'),('sec(x)','1/cos(x)'),('cot(x)','1/tan(x)'),
  ('tan(x)','sin(x)/cos(x)'),('cot(x)','cos(x)/sin(x)'),
  ('sin(x)**2+cos(x)**2','1'),('1+cot(x)**2','csc(x)**2'),('1+tan(x)**2','sec(x)**2')]],'table')
for n,family in[(203,'sin'),(204,'cos'),(205,'tan')]:
    op={'kind':'trig-features','family':family,'angle_unit':'radian','operands':['1','1','0','0','2*pi'],'at':['0','pi','2*pi']}
    fields={'period':'pi'if family=='tan'else'2*pi','window_zero_locations':'FiniteSet(0,pi,2*pi)'if family!='cos'else'FiniteSet(pi/2,3*pi/2)'}
    if family=='tan':fields['window_poles']='FiniteSet(pi/2,3*pi/2)'
    add(n,231,'Basic '+family+' summary graph',
      'The basic '+family+' graph uses aligned radianπ,2πanddegree180°,360°ticks. '+('Two tangent poles atπ/2and3π/2separate increasing branches; they are not graph points.'if family=='tan'else'The unshifted amplitude is1andperiod2π.'),[BASIC],
      [{'operation':op,'source_features':fields}],'graph')
add(206,231,'Sine-transform coefficient annotation','For y=a sin(bx)+c,nonzero a affects amplitude|a|,nonzero b gives period2π/|b|,andc shifts the midline vertically. Zero a or b gives a degenerate constant; the period rule is not applicable then.',[FEATURE],
 [scalar('Abs(-3)','3'),scalar('2*pi/Abs(-2)','pi')])
for n,family,lo,hi,target,note in[
 (207,'sin','-pi/2','pi/2','Tuple(asin(x),Interval(-1,1),Interval(-pi/2,pi/2))','asin has input[−1,1],output[−90°,90°]with both endpoints included; it increases through the origin.'),
 (208,'cos','0','pi','Tuple(acos(x),Interval(-1,1),Interval(0,pi))','acos has input[−1,1],output[0°,180°]with both endpoints included; it decreases through(0,90°).'),
 (209,'tan','-pi/2','pi/2','Tuple(atan(x),S.Reals,Interval.open(-pi/2,pi/2))','atan has all real inputs andopen output(−90°,90°); finite inputs never reach the horizontal asymptotes.')]:
    # Helper requires closed forward endpoints; tangent is handled explicitly
    # because its principal forward domain and inverse range are open.
    if family=='tan':
        checks=[scalar('Tuple(atan(-1),atan(0),atan(1))','Tuple(-pi/4,0,pi/4)'),
          scalar('limit(atan(x),x,oo)','pi/2'),scalar('limit(atan(x),x,-oo)','-pi/2')]
    else:checks=[{'operation':{'kind':'inverse-principal-affine-trig','family':family,'operands':['1','1','0',lo,hi],
           'return_fields':['expression','domain','range']},'source_normalised':target}]
    add(n,231,'Principal inverse '+family+' summary graph',note,[P],checks,'graph')
pages=[{'pdf_page':page,'printed_page':page-12,'chapter':4,'page_status':'items enumerated',
 'item_ids':[r['item_id']for r in figures if r['pdf_page']==page],'continuation_item_ids':[],'source_evidence':ev(),
 'non_item_content':'Summary/reference pages: no separate learner tasks. All mathematical figures/tables/annotation flows are separately enumerated and checked; chapter5cover starts onPDF232.',
 'reader':'Codex author','date':'2026-11-18'}for page in[229,230,231]]
if __name__=='__main__':
    (W/'tools/textbook-r5/census-YM-C4-summary.json').write_text(json.dumps({'book':'YM','book_id':'8227-SRC-017','chapter':4,
      'source_path':SRC,'source_sha256':SHA,'scope':'All summary teaching diagrams andtables onPDF229–231. No additional assessed item is invented.',
      'new_items':figures,'corrections':[],'pages':pages},ensure_ascii=False,indent=2)+'\n')
    print(len(figures),'summary figures/tables checked;',sum(len(r['mathematical_feature_review']['checks'])for r in figures),'explicit feature/formula checks')
