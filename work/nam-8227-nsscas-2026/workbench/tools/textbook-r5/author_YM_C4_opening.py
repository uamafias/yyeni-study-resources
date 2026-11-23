"""Explicit rendered-page census/answer readings for YM chapter4 opening.
Only pages153–156are enumerated here; this is not a whole-chapter claim.
"""
import json,hashlib
from pathlib import Path
import sympy as sp
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2]
SRC='Y=mc as textbook.pdf';SHA='0b44ad3b67b1ea3de90cba780382d77deef347fae683cf6e28677f36c17a724f'
F=lambda tail:'8227:2020:M1:T5:'+tail
def ev(key=False):
    p=W/f'checks/r5/textbooks/{"YM-key-C4-602"if key else"YM-radian-153"}.png'
    return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def auto(label,expr,key,keypage,rounded=None,unit=None):
    row={'subpart':label,'operation':{'kind':'identity','operands':[expr]},'printed_key_normalised':key,
      'answer_pdf_page':keypage,'answer_printed_page':'A16'if keypage==602 else keypage-12,'source_evidence':ev(),'key_evidence':ev(keypage==602),
      'method':'Independently use180degrees=pi radians,or s=r theta with theta in radians; retain the exact value and compare any printed decimal under the explicitly stated book rounding rule.','units':unit}
    if rounded:
        printed,rounding=rounded
        row['additional_comparisons']=[{'operation':{'kind':'rounded','operands':[expr],**rounding},'printed_key_normalised':printed,'printed_display':printed}]
    return row
def rounded(label,expr,key,keypage,unit):
    row=auto(label,expr,key,keypage,unit=unit);row['operation'].update(kind='rounded',decimal_places=1)
    row['additional_operations']={'exact_conversion':{'kind':'identity','operands':[expr]}}
    return row
answers=[]
def add(kind,n,page,note,parts,demands):
    answers.append({'item_id':f'8227:TB:YM:C4:{kind}:{n}','source_pdf_page':page,'notes':note,
      'assessed_8227_demand_ids':demands,'component_demand_ids':[],
      'mapping_rationale':'Conversion tasks assess conversion,not automatic knowledge of the geometric definition of one radian. Arc calculations assess use of arc length; unit conversion remains a component when needed.',
      'exam_style':False,'exam_style_basis':'Ordinary worked Example/Try Now without source exam-style label or examination attribution.',
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'not applicable','quoted_value':note,'reason':'The task converts angles or calculates arc lengths; it does not solve a trigonometric equation with argument multiplier n.'}],
      'precision_angle_check':{'source':'YM PDF155: radians3sf or exactpi form; degrees1dp. PDF156arc-length examples round to3sf.',
      'comparison':'These local book notes are not universal NSSCAS instructions. Use marking-conventions.json and the individual question instructions for future resources; exact values are retained here. Angles in s=r theta must be radians.'},
      'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts})

add('Example',1,155,'Convert26degreesand114.5degrees to radians,retaining exactpi values and the printed3sf alternatives.',
 [auto('a','26*pi/180','13*pi/90',155,('0.454',{'significant_figures':3}),'radian'),auto('b','S(229)/2*pi/180','229*pi/360',155,('2.00',{'significant_figures':3}),'radian')],[F('O01:D02')])
add('Example',2,155,'Convert1.5radians and5pi/6radians to degrees; the first is shown to1decimal place,the second exactly150degrees.',
 [rounded('a','S(3)/2*180/pi','85.9',155,'degree'),auto('b','5*pi/6*180/pi','150',155,unit='degree')],[F('O01:D02')])
add('Try-Now',1,155,'Convert43,120and330degrees to radians; compare both exactpi and3sf values printed on keyPDF602(A16).',
 [auto('a','43*pi/180','43*pi/180',602,('0.750',{'significant_figures':3}),'radian'),auto('b','120*pi/180','2*pi/3',602,('2.09',{'significant_figures':3}),'radian'),auto('c','330*pi/180','11*pi/6',602,('5.76',{'significant_figures':3}),'radian')],[F('O01:D02')])
add('Try-Now',2,156,'Convert3.2radians,2.56radians and6pi/7radians to degrees to1decimal place; compare separate a,b,c key entries onPDF602.',
 [rounded('a','S(16)/5*180/pi','183.3',602,'degree'),rounded('b','S(64)/25*180/pi','146.7',602,'degree'),rounded('c','6*pi/7*180/pi','154.3',602,'degree')],[F('O01:D02')])
add('Example',3,156,'A circle has radius4cm and minor anglepi/5. Find minor and major arc lengths; the major angle is2pi−pi/5=9pi/5.',
 [auto('a','4*pi/5','4*pi/5',156,('2.51',{'significant_figures':3}),'cm'),auto('b','4*(2*pi-pi/5)','36*pi/5',156,('22.6',{'significant_figures':3}),'cm')],[F('O02:D01')])
add('Worked-illustration',1,154,'Unnumbered calculation converts one radian to180/pi degrees,approximately57.3degrees to1decimal place,using the complete turn2pi radians=360degrees.',
 [rounded('one-radian-in-degrees','180/pi','57.3',154,'degree')],[F('O01:D02')])

new=[{'item_id':'8227:TB:YM:C4:Worked-illustration:1','item_kind':'worked-illustration','exercise':'Worked illustration','item_number':'1','pdf_page':154,'printed_page':142,
 'notes':answers[-1]['notes'],'assessed_8227_demand_ids':[F('O01:D02')],'component_demand_ids':[],
 'representation':'text','source_evidence':ev(),'answer_key':{'available':True,'pdf_pages':[154],'printed_pages':[142],'locator':'Inline calculation: the actual size of one radian in degrees','source_path':SRC,'source_sha256':SHA}}]
figure_specs=[
 (154,'One-radian definition diagram','ArcABhas lengthr,OA=OB=r,and the central angle is1radian. It explicitly teaches arc/radius=1; not a separately posed definition question.',[F('O01:D01')],None,'diagram'),
 (154,'Full-turn radian diagram','Six consecutive one-radian sectors plus the remainder2pi−6≈0.283185307radians make a complete turn. Radius-equal arc pieces visualise the geometric unit.',[F('O01:D01'),F('O01:D02')],None,'diagram'),
 (155,'Angle-conversion identity panel','2pi rad=360degrees;pi rad=180degrees;1rad=180/pidegrees≈57.3;1degree=pi/180rad≈0.01746.',[F('O01:D02')],None,'table'),
 (155,'Special-angle conversion table','Degree row0,30,36,45,60,90,180,270,360corresponds to0,pi/6,pi/5,pi/4,pi/3,pi/2,pi,3pi/2,2pi.',[F('O01:D02')],None,'table'),
 (155,'Degrees/radians conversion arrows','Forward degree-to-radian arrow multiplies bypi/180; reverse divides bypi/180(or multiplies180/pi).',[F('O01:D02')],None,'diagram'),
 (156,'Arc-length derivation and circle','The proportion theta/(2pi)of circumference2pir produces s=r theta; labelled centreO,radii r,angle theta radians and arcAB=s. Degree formula is displayed as the preceding comparison.',[F('O02:D01')],None,'diagram'),
 (156,'Example3given sector','OA=OB=4cm andangleAOB=pi/5on a circle; minor arcAB is distinguished from the major arc.',[F('O02:D01')],'8227:TB:YM:C4:Example:3','diagram'),
 (156,'Example3major-angle solution diagram','The full turn minuspi/5is9pi/5; the major sector and arc are explicitly distinguished from the small given sector. The radius stays4cm.',[F('O02:D01')],'8227:TB:YM:C4:Example:3','diagram')]
for n,(page,label,note,teaches,parent,rep)in enumerate(figure_specs,1):
    has_arc=F('O02:D01')in teaches
    new.append({'item_id':f'8227:TB:YM:C4:Teaching-figure:{n}','item_kind':'teaching-figure','exercise':'Teaching figure','item_number':str(n),
      'pdf_page':page,'printed_page':page-12,'source_label':label,'parent_item_id':parent,'notes':note,'what_it_shows':note,
      'assessed_8227_demand_ids':[],'component_demand_ids':[],'teaches_8227_demand_ids':teaches,'representation':rep,'source_evidence':ev(),'learner_display':False,
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'not applicable','quoted_value':note,'reason':'Radian/arc teaching illustration,not a bounded trigonometric equation.'}],
      'value_level_scope_review_status_r5':'author actual-value/representation check complete; independent check pending',
      'exam_representation_check':{'status':'arc diagram representation observed; exact book task not claimed identical'if has_arc else'teaching support; no directly assessed NSSCAS radian-definition/conversion part identified',
      'examination_part_ids':['8227:EXAM:2021:P1:Q7:a','8227:EXAM:2022:P1:Q8:a']if has_arc else[],
      'relation':'NSSCAS arc tasks combine different givens and shapes; this textbook diagram is teaching evidence,not full examination coverage.'if has_arc else'The examined gap remains distinguishable from explicit teaching support; do not turn a figure into an assessed question.'},
      'mathematical_feature_review':{'status':'author checked labels and numerical relationships on render; independent check pending',
       'method':'Use theta=s/r,2pi per full turn and180degrees=pi radians; recompute every special-angle table entry and complementary major angle. Diagrams are schematic,so read labels rather than measuring from the picture.'}})

# Independent arithmetic checks on every conversion-table entry and the sector
# relationships; these do not turn the figure into a separately assessed task.
for degree,radian in zip([0,30,36,45,60,90,180,270,360],[0,sp.pi/6,sp.pi/5,sp.pi/4,sp.pi/3,sp.pi/2,sp.pi,3*sp.pi/2,2*sp.pi]):
    assert sp.simplify(degree*sp.pi/180-radian)==0
assert 0<2*sp.pi-6<1 and sp.simplify(sp.pi/5+9*sp.pi/5-2*sp.pi)==0

pages=[]
existing={153:[],154:[],155:[r['item_id']for r in answers[:3]],156:[r['item_id']for r in answers[3:5]]}
for page in range(153,157):
    own=existing[page]+[i['item_id']for i in new if i['pdf_page']==page]
    pages.append({'pdf_page':page,'printed_page':page-12,'chapter':4,'page_status':'items enumerated'if own else'prose only',
      'item_ids':own,'continuation_item_ids':[],'source_evidence':ev(),
      'non_item_content':'Chapter cover and syllabus-outline bullet list; decorative biographical photograph is not a mathematical figure.'if page==153 else'All worked illustrations,formal tasks,teaching tables and diagrams are enumerated; intervening prose explains those same ideas.',
      'reader':'Codex author','date':'2026-11-17'})
if __name__=='__main__':
    for name,data in [
      ('answers-YM-C4-opening.json',{'scope':'Only the five existing Examples/TryNow plus newly found inline one-radian conversion onPDF154–156; full chapter still pending.','items':answers}),
      ('census-YM-C4-opening.json',{'book':'YM','book_id':'8227-SRC-017','chapter':4,'source_path':SRC,'source_sha256':SHA,
       'scope':'Opening pages153–156only; wider chapter page population pending. Teaching support for radian meaning is kept separate from directly assessed conversion practice.','new_items':new,'corrections':[],'pages':pages})]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(len(new),'new source records;',len(answers),'answer-checked items')
