"""R5 rendered source annotations: YM circular-measure practice,PDF157–164.
Question values and printed answers are transcribed separately. This checks
fixed source items; it does not generate learner questions.
"""
import json,hashlib
from pathlib import Path
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2]
SRC='Y=mc as textbook.pdf';SHA='0b44ad3b67b1ea3de90cba780382d77deef347fae683cf6e28677f36c17a724f'
F=lambda tail:'8227:2020:M1:T5:'+tail
ARC=F('O02:D01');AREA=F('O02:D02');SEG=F('O02:D03');CONV=F('O01:D02')
def ev(page):
    name=f'YM-key-C4-{page}'if page in[602,603]else f'YM-C4-{157+4*((page-157)//4)}'
    p=W/f'checks/r5/textbooks/{name}.png'
    return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def calc(label,expr,key,unit=None,rounding=None,mode=None,extra=None):
    row={'subpart':label,'operation':{'kind':'rounded'if rounding else'identity','operands':[expr],**(rounding or{})},'printed_key_normalised':key,'units':unit}
    if rounding:row['additional_operations']={'unrounded_or_exact_answer':{'kind':'identity','operands':[expr]}}
    if mode:row['check_mode']=mode
    if extra:
        rounded_key,policy=extra
        row['additional_comparisons']=[{'operation':{'kind':'rounded','operands':[expr],**policy},'printed_key_normalised':rounded_key,'printed_display':rounded_key}]
    return row
SF3={'significant_figures':3};DP1={'decimal_places':1};DP3={'decimal_places':3};DP4={'decimal_places':4}
answers=[];corrections=[]
def add(kind,n,page,key_page,note,parts,direct,components=None,reason=None):
    iid=f'8227:TB:YM:C4:{kind}:{n}'
    for part in parts:
        kp=part.pop('key_page_override',key_page);pp=part.pop('question_page_override',page)
        part.update(source_evidence=ev(pp),key_evidence=ev(kp),answer_pdf_page=kp,answer_printed_page={602:'A16',603:'A17'}.get(kp,kp-12),source_pdf_page=pp)
        part.setdefault('method','Derive from the original radius,angle,area or perimeter using s=r theta,A=r²theta/2and elementary triangle geometry. Use exact radians and full precision until the requested rounding; no printed intermediate answer is fed into the calculation.')
    row={'item_id':iid,'source_pdf_page':page,'notes':note,'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],
      'mapping_rationale':reason or'The requested arc/perimeter,sector area or segment area determines the direct demand. Intermediate use of another formula is a component. An arbitrary acute inverse ratio or chord calculation is prescribed prior knowledge,not automatically an AS principal-value or exact-special-angle demand.',
      'exam_style':False,'exam_style_basis':'Ordinary Exercise4.1or worked Example/TryNow; source labels Basic/Intermediate/Advanced are textbook difficulty labels,not examination attribution.',
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'not applicable','quoted_value':note,'reason':'Circular-measure or triangle task,not solving a trigonometric equation with multiplier n.'}],
      'precision_angle_check':{'source':'YM asks exactpi/exact chord in specified parts; other answers use local3sf convention unless more precisely stated. Show-that values retain their stated decimal-place tolerance.',
       'comparison':'Apply the actual NSSCAS question/report precision rules when authoring later. Radian-mode trig is essential for source angles here; retain full intermediate values rather than copying rounded workings.'},
      'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts}
    answers.append(row);return row

add('Try-Now',3,157,602,'Radius8cm,minor angle0.85radians: calculate minor and major arc lengths,including the complementary angle2pi−0.85.',
 [calc('a','8*S(85)/100','6.8','cm'),calc('b','8*(2*pi-S(85)/100)','43.5','cm',SF3)],[ARC])
add('Example',4,157,157,'Radius4cm,minor anglepi/5: find the major-sector area using9pi/5radians rather than the small displayed angle.',
 [calc('major-sector-area','4**2*(2*pi-pi/5)/2','72*pi/5','cm²',extra=('45.2',SF3))],[AREA])
add('Try-Now',4,158,602,'Radius8cm,minor angle0.85radians: find major-sector area. The major sector includes the rest of the circle,not the small labelled wedge.',
 [calc('major-sector-area','8**2*(2*pi-S(85)/100)/2','174','cm²',SF3)],[AREA])
add('Example',5,158,158,'Sector radius6cm and perimeter21cm: recover arc9cm,then angle1.5radians and area27cm².',
 [calc('a','(21-2*6)/S(6)','1.5','radian'),calc('b','6**2*((21-2*6)/S(6))/2','27','cm²')],[ARC,AREA])
add('Try-Now',5,158,602,'Sector radius4cm and perimeter13cm: recover arc5cm,then angle1.25radians and area10cm².',
 [calc('a','(13-2*4)/S(4)','1.25','radian'),calc('b','4**2*((13-2*4)/S(4))/2','10','cm²')],[ARC,AREA])
add('Example',6,158,158,'Sector radius12cm and area57.6cm²: infer its angle from area,then calculate the perimeter including both radii.',
 [calc('perimeter','2*12+2*(S(576)/10)/12','33.6','cm')],[ARC],[AREA])
add('Try-Now',6,159,602,'Sector radius10cm and area60cm²: recover arc12cm and add both radii to obtain the perimeter.',
 [calc('perimeter','2*10+2*60/S(10)','32','cm')],[ARC],[AREA])
add('Example',7,159,159,'Right triangleAOBhasOA=12cm,OB=5cm,with arcs centred atAandB. Show angleBAOto4dp and calculate the overlapping shaded region as the two sectors minus the triangle.',
 [calc('a','atan(S(5)/12)','0.3948','radian',DP4,'show/prove'),calc('b','72*atan(S(5)/12)+S(25)/2*atan(S(12)/5)-30','13.1','cm²',SF3)],[AREA],reason='Part(a)is prior-knowledge acute-angle computation. Part(b)directly asks compound area assembled from sectors; it is not full evidence for the distinct single-circle segment-area demand.')
add('Try-Now-7',1,160,602,'Right triangleABCwithAC=2cm,BC=2sqrt3cm,and arcCDof radius2centredA: subtract the60degree sector from the triangle to find shadedBDC.',
 [calc('shaded-area','2*sqrt(3)-2*pi/3','1.37','cm²',SF3)],[AREA],['8227:2020:M1:T6:O03:D01'])
ob='6/cos(S(3)/5)';ab='6*tan(S(3)/5)';angle='pi/2-S(3)/5'
add('Try-Now-7',2,160,603,'Right triangleOABhasOA=6cm andangleAOB=0.6radians;OBCis a sector withOAperpendicularOC. ShowOBto3dp,then find the plate perimeter and area without roundingOBearly.',
 [calc('a',ob,'7.270','cm',DP3,'show/prove'),calc('b',f'6+({ab})+({ob})+({ob})*({angle})','24.4','cm',SF3),calc('c',f'6*({ab})/2+({ob})**2*({angle})/2','38.0','cm²',SF3)],[ARC,AREA])
add('Example',8,161,161,'SectorXOYhas radius6cm and angle2pi/3. Find exact arc/perimeter/sector area,then segment area and exact chordXYusing the cosine rule.',
 [calc('a-i','6*2*pi/3','4*pi','cm'),calc('a-ii','6*2*pi/3+12','4*pi+12','cm',extra=('24.6',SF3)),
  calc('a-iii','6**2*(2*pi/3)/2','12*pi','cm²'),calc('b','6**2*(2*pi/3-sin(2*pi/3))/2','22.1','cm²',SF3),
  calc('c','sqrt(6**2+6**2-2*6*6*cos(2*pi/3))','6*sqrt(3)','cm',extra=('10.4',SF3))],[ARC,AREA,SEG],['8227:2020:M1:T6:O03:D01'])
row=add('Try-Now-8',1,161,603,'SectorXOYhas radius4cm andangle5pi/6. Find exact arc/perimeter/sector area,segment area,and exact chordXY. Source names an undefinedB inangleXOB; the figure labelsY.',
 [calc('a-i','4*5*pi/6','10*pi/3','cm'),calc('a-ii','4*5*pi/6+8','10*pi/3+8','cm'),calc('a-iii','4**2*(5*pi/6)/2','20*pi/3','cm²'),
  calc('b','4**2*(5*pi/6-sin(5*pi/6))/2','16.9','cm²',SF3),
  calc('c','sqrt(4**2+4**2-2*4*4*cos(5*pi/6))','sqrt(2*sqrt(6)+2*sqrt(2))','cm')],[ARC,AREA,SEG],['8227:2020:M1:T6:O03:D01'])
for p in row['subparts']:
    if p['subpart']in['b','c']:p.update(source_pdf_page=162,source_evidence=ev(162))
row['subparts'][-1]['source_defect_id']='TB-YM-C4-Try8-Q1c-EXTRA-RADICAL'
corrections.append({'item_id':row['item_id'],'continuation_pdf_pages':[162]})
small='10*sin(S(3)/5)'
add('Try-Now-8',2,162,603,'PlateABCDcombines the major segment of radius10cm,minor central angle1.2radians,and an external semicircle on chordBD. Show the smaller radius to3dp,then find total outer perimeter and area.',
 [calc('a',small,'5.646','cm',DP3,'show/prove'),calc('b',f'10*(2*pi-S(6)/5)+pi*({small})','68.6','cm',SF3),
  calc('c',f'100*(2*pi-S(6)/5+sin(S(6)/5))/2+pi*({small})**2/2','351','cm²',SF3)],[ARC,AREA,SEG])
row=add('Example',9,162,162,'Radiusr,sectorangleθ: equal areas of triangleAOBandsegmentAXBimplyθ=p sinθ. Determinepwith0<θ<piandr>0,so division bysinθis valid.',
 [calc('p','2','2')],[AREA,SEG])
# Solving this transcendental equation is unnecessary. Solve the *area identity*
# for the unknown factor p after theta=p sin(theta),with sin(theta)nonzero.
row['subparts'][0]['operation']={'kind':'identity','operands':['solve(Eq(sin(x),Symbol("p")*sin(x)-sin(x)),Symbol("p"))[0]']}
row['subparts'][0]['method']='Equate r²sinθ/2to r²(θ−sinθ)/2,cancel r²/2,and substituteθ=p sinθ. This gives(p−2)sinθ=0; for the nondegenerate minor sector0<θ<pi,sinθ>0,hencep=2. No numerical solution forθis required.'
row=add('Try-Now',9,162,603,'Withcircle radiusr,central angle2θand a semicircle on chordAB,find the crescent area as semicircle minus the minor segment; use0<θ<pi/2.',
 [calc('shaded-area','pi*(Symbol("r")*sin(x))**2/2-Symbol("r")**2*x+Symbol("r")**2*sin(2*x)/2','Symbol("r")**2*(pi*sin(x)**2-2*x+sin(2*x))/2','length²')],[AREA,SEG])
row['subparts'][0]['method']='Half chord isr sinθ,so semicircle area ispi r²sin²θ/2. The segment area isr²(2θ−sin2θ)/2; subtract it and collect terms. Assumes the depicted nondegenerate minor-sector geometry0<θ<pi/2,r>0.'

add('Exercise-4.1',1,163,603,'Convert15,18,75and225degrees to exact radians in terms ofpi; these four values are separate response subparts.',
 [calc(label,f'{degree}*pi/180',key,'radian')for label,degree,key in [('a',15,'pi/12'),('b',18,'pi/10'),('c',75,'5*pi/12'),('d',225,'5*pi/4')]],[CONV])
add('Exercise-4.1',2,163,603,'Convert3pi/4,5pi/6,2.8and5.7radians to degrees; round to1dpwhere necessary,not exact integer conversions.',
 [calc('a','3*pi/4*180/pi','135','degree'),calc('b','5*pi/6*180/pi','150','degree'),calc('c','S(14)/5*180/pi','160.4','degree',DP1),calc('d','S(57)/10*180/pi','326.6','degree',DP1)],[CONV])
row=add('Exercise-4.1',3,163,603,'Complete four sector-table rows:(a)r=4cm,s=6cm;(b)r=8m,A=64m²;(c)θ=2.5,s=20cm;(d)s=6m,A=27m². Each row has two unknowns and retains its own units.',
 [calc('a-angle','6/S(4)','1.5','radian'),calc('a-area','4*6/S(2)','12','cm²'),
  calc('b-angle','2*64/S(8)**2','2','radian'),calc('b-arc','2*64/S(8)','16','m'),
  calc('c-radius','20/(S(5)/2)','8','cm'),calc('c-area','(20/(S(5)/2))*20/2','80','cm²'),
  calc('d-radius','2*27/S(6)','9','m'),calc('d-angle','6/(2*27/S(6))','2/3','radian')],[ARC,AREA])
row['subparts'][5].update(printed_key_units='cm',source_defect_id='TB-YM-C4-Ex41-Q3c-AREA-UNIT')
add('Exercise-4.1',4,163,603,'Annular sector has inner radiusOA=8cm,radial widthAD=12cm,and inner-sector area80cm². Outer radius is20cm; findθ,complete boundary perimeter,and shaded area.',
 [calc('a','2*80/S(8)**2','2.5','radian'),calc('b','(8+8+12)*(2*80/S(8)**2)+2*12','94','cm'),calc('c','((8+12)**2-8**2)*(2*80/S(8)**2)/2','420','cm²')],[ARC,AREA])
add('Exercise-4.1',5,163,603,'Circle radius3cm has two central anglesAOC=BOC=2.3radians. Find remaining angleAOBto4sfand shadedACBParea to3sf,using remaining sector plus the two triangles.',
 [calc('a','2*pi-2*S(23)/10','1.683','radian',{'significant_figures':4}),calc('b','9*(2*pi-2*S(23)/10)/2+9*sin(S(23)/10)','14.3','cm²',SF3)],[AREA])
row=add('Exercise-4.1',6,163,603,'Circle radiusr,tangentPTatP,andanglePOT=α,withQonOT. Express the perimeterPQTof the curvilinear triangle inrandα; r>0,0<α<pi/2.',
 [calc('perimeter','Symbol("r")*x+Symbol("r")*tan(x)+Symbol("r")/cos(x)-Symbol("r")','Symbol("r")*x+Symbol("r")*tan(x)+Symbol("r")/cos(x)-Symbol("r")','length')],[ARC])
row['subparts'][0]['method']='ArcPQ=rα; right triangleOPTgivesPT=r tanαandOT=r/cosα,soQT=OT−r. Add the three boundary lengths. The printed alternative sqrt(r²+r²tan²α)equalsr/cosαonly under the stated positive-radius acute-angle geometry.'

figures=[]
specs=[
 (157,'TryNow3given circle','Radius8cm andminor angle0.85radians on circleAOB; a complementary major arc is required.','Try-Now:3',[ARC],'diagram'),
 (157,'Sector-area derivation diagram','Sector angleθradians,common radiusr and shaded major/minor sector lead toA=r²θ/2. Degree-area comparison and formula panel belong to this same teaching illustration.',None,[AREA],'diagram'),
 (157,'Example4given circle','Radius4cm,minor anglepi/5andpointCon themajor arc; identify major sectorOACB.','Example:4',[AREA],'diagram'),
 (157,'Example4solution major sector','Major angle is9pi/5on the same radius4circle; the solution diagram explicitly marks the complementary region.','Example:4',[AREA],'diagram'),
 (158,'TryNow4given circle','Radius8cm,minor angle0.85radians; required area is the major sector.','Try-Now:4',[AREA],'diagram'),
 (158,'Example5given sector','Sector boundary has two equal radiir andarc lengths;θis unknown,with source radius6cm/perimeter21cm.','Example:5',[ARC,AREA],'diagram'),
 (158,'Example5solution sector','The same sector now labels both radii6andarc9;θ=1.5is derived,not a new given.','Example:5',[ARC,AREA],'diagram'),
 (158,'TryNow5given sector','Radius4,two radial sides,arc s andunknownθ; perimeter13cmis in the accompanying stem.','Try-Now:5',[ARC,AREA],'diagram'),
 (158,'Example6given sector','Both radii12andsector area57.6are shown;θis unknown. Perimeter includes both radii.','Example:6',[ARC,AREA],'diagram'),
 (159,'TryNow6given sector','Both radii10andarea60are shown; recover the arc before calculating full perimeter.','Try-Now:6',[ARC,AREA],'diagram'),
 (159,'Example7overlapping arcs','Right triangleAOBhasOA12,OB5;P,QlieonAB,arcOPcentredAandarcOQcentredBbound the shaded overlap.','Example:7',[AREA],'diagram'),
 (160,'TryNow7question1triangle and arc','AC=2,BC=2sqrt3,BCperpendicularAC;DliesonABandarcCDhascentreA,radius2; shadedBDCis triangle minussector.','Try-Now-7:1',[AREA],'diagram'),
 (160,'TryNow7question2metal plate','OA6,angleAOB0.6,OAperpendicularOC,ABperpendicularOA;OBCis a sector,soOC=OB; outer boundary includesOCandarcBC.','Try-Now-7:2',[ARC,AREA],'diagram'),
 (160,'Triangle trigonometry formula table','Sine rule,cosine rule,andtriangle areaab sinC/2are displayed as OrdinaryLevel support. No separate AS task is asked.',None,[],'table'),
 (161,'Example8given segment','Two radii6andcentral angle2pi/3; chordXYsplits sector into triangle and shaded minor segment.','Example:8',[ARC,AREA,SEG],'diagram'),
 (161,'TryNow8question1given segment','Two radii4andcentral angle5pi/6; chordXYbounds shaded segment. Diagram labelsYalthough source sentence erroneously namesB.','Try-Now-8:1',[ARC,AREA,SEG],'diagram'),
 (162,'TryNow8question2plate','Major segmentDABofradius10andminor angleBOD1.2joins a semicircleBCDwhose diameter isBD. Dashed radii are not part of the perimeter.','Try-Now-8:2',[ARC,AREA,SEG],'diagram'),
 (162,'Example9given sector and chord','Two radiir,angleθ,triangleAOBandsegmentAXB; equality of their areas is supplied in the stem.','Example:9',[AREA,SEG],'diagram'),
 (162,'Example9solution partition','Same sector divided and labelled triangle/segment; total sector area is the sum of those two regions.','Example:9',[AREA,SEG],'diagram'),
 (162,'TryNow9crescent','SemicircleAYBhasdiameterAB;sectorOAXBhasradiusrandangle2θ; shaded crescent is semicircle minuscircle segmentAXB.','Try-Now:9',[AREA,SEG],'diagram'),
 (163,'Exercise4.1question3given table','Four rows mix radius,angle,arc,area,andcmormunits; two blanks per row require forward and reverse calculations.','Exercise-4.1:3',[ARC,AREA],'table'),
 (163,'Exercise4.1question4annular sector','OA=8,AD=12along a common radius;OC=OD=20andinner radiusOB=8; the given80cm²belongs to theinner sector.','Exercise-4.1:4',[ARC,AREA],'diagram'),
 (163,'Exercise4.1question5compound circle area','Common radius3,central anglesAOCandBOCboth2.3radians; shadedACBPcontains the remaining sector andboth triangles.','Exercise-4.1:5',[AREA],'diagram'),
 (163,'Exercise4.1question6tangent boundary','OP=r,PTtangent,OPperpendicularPT,QonOTandanglePOT=α; arcPQ,QTandPTform the perimeter.','Exercise-4.1:6',[ARC],'diagram'),
 (164,'Sine plotting table','Angles0through360degrees every30degrees; sin values use0,±0.5,±0.87,±1. Rounded0.87stands for√3/2.',None,['8227:2020:M1:T6:O01:D01'],'table'),
 (164,'Sine graph and amplitude-period annotations','Sine0..360degrees,smooth extrema±1at90/270,zeros0/180/360,amplitude1andperiod360degrees(2pi). Degree ticksand supplementaryπlabelsare displayed.',None,['8227:2020:M1:T6:O01:D01','8227:2020:M1:T6:O02:D01'],'graph')]
for n,(page,label,note,parent,teaches,rep)in enumerate(specs,9):
    parent_id=f'8227:TB:YM:C4:{parent}'if parent else None
    figures.append({'item_id':f'8227:TB:YM:C4:Teaching-figure:{n}','item_kind':'teaching-figure','exercise':'Teaching figure','item_number':str(n),
      'pdf_page':page,'printed_page':page-12,'source_label':label,'parent_item_id':parent_id,'notes':note,'what_it_shows':note,
      'assessed_8227_demand_ids':[],'component_demand_ids':[],'teaches_8227_demand_ids':teaches,'representation':rep,'source_evidence':ev(page),'learner_display':False,
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'not applicable','quoted_value':note,'reason':'No bounded trigonometric equation is posed by this figure; angle labels alone do not invoke multiplier limits.'}],
      'value_level_scope_review_status_r5':'author actual-value/geometry reading complete; independent check pending',
      'exam_representation_check':{'status':'representation comparison pending cross-book family synthesis','examination_part_ids':[],
       'relation':'This is explicit textbook teaching/given evidence. Do not infer an exact NSSCAS same-type task solely from a circle or sine-curve topic.'},
      'mathematical_feature_review':{'status':'author checked labels and source relationships; independent review pending',
       'method':'For task figures,independent parent answer derivations check radius,angle,arc,sector/segment and boundary relationships. For the formula table,standard triangle identities are labelled prior knowledge. Sine plotting values and amplitude/period follow direct evaluations,not pixel measurements.'}})
pages=[]
for page in range(157,165):
    own=[r['item_id']for r in answers if r['source_pdf_page']==page]+[f['item_id']for f in figures if f['pdf_page']==page]
    pages.append({'pdf_page':page,'printed_page':page-12,'chapter':4,'page_status':'items enumerated',
      'item_ids':own,'continuation_item_ids':['8227:TB:YM:C4:Try-Now-8:1']if page==162 else[],
      'source_evidence':ev(page),'non_item_content':'All formal tasks and mathematical diagrams/tables are enumerated. Calculator-mode and precision callouts are prose guidance,not additional independent questions.',
      'reader':'Codex author','date':'2026-11-17'})
if __name__=='__main__':
    for name,data in [
      ('answers-YM-C4-arcs.json',{'scope':'All formal items onPDF157–163; complete subpart results,with actual answer pages and explicit source defects. This is not whole-book acceptance.','items':answers}),
      ('census-YM-C4-arcs.json',{'book':'YM','book_id':'8227-SRC-017','chapter':4,'source_path':SRC,'source_sha256':SHA,
       'scope':'PDF157–164inclusive; all tasks,continuations and mathematical figures/tables on these pages. No statement about later chapter pages.','new_items':figures,'corrections':corrections,'pages':pages})]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(len(answers),'formal items;',len(figures),'mathematical figures/tables')
