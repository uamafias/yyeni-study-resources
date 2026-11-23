"""Independent fixed-source derivations for YM PDF209–213."""
import hashlib,json
from pathlib import Path
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2]
SRC='Y=mc as textbook.pdf';SHA='0b44ad3b67b1ea3de90cba780382d77deef347fae683cf6e28677f36c17a724f'
BND='8227:2020:M1:T6:O06:D01';ALL='8227:2020:M1:T6:O06:D02';TRANS='8227:2020:M1:T6:O05:D02'
PROOF='8227:2020:M1:T6:O05:D01';REC='8227:2020:M2:T3:O01:D01';BASIC='8227:2020:M1:T6:O01:D01'
D='(x*pi/180)'
def ev(page):
    name='YM-key-610-611-full'if page==611 else'YM-key-612-613-full'if page in[612,613]else'YM-C4-209'if page<=212 else'YM-C4-213'
    p=W/f'checks/r5/textbooks/{name}.png'
    return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def roots(label,original,key,kp,branches,unit='degree',lo='0',hi=None,approx=False,opened=False):
    hi=hi or('360'if unit=='degree'else'2*pi')
    p={'subpart':label,'operation':{'kind':'bounded-trig-equation','operands':[original,lo,hi],'left_open':opened,'right_open':opened},
      'source_ratio_branches':[{'function':f,'argument':a,'ratio':r,'power':power,'angle_unit':unit}for f,a,r,power in branches],
      'key_page_override':kp,'review_date':'2026-11-18','source_angle_unit':unit,
      'method':'Factor or transform the original equation without dividing away a possibly zero factor. Solve every admissible branch in the original interval, reject out-of-range ratios and original poles, and substitute each candidate into the original equation. All exact roots precede any comparison with printed rounded values.'}
    if approx:p['printed_key_approximate_values']=key
    else:p['printed_key_normalised']=key
    return p
def transform(label,left,right,middle,domain,kp):
    return {'subpart':label,'operation':{'kind':'trig-identity-residual','operands':[left,right]},
      'printed_key_normalised':'0','check_mode':'show/prove','proof_expressions':[left,*middle,right],
      'original_common_domain':domain,'key_page_override':kp,'review_date':'2026-11-18',
      'method':'Independently check every stated transformation and substitution. For an equation reduction, retain any original denominator restriction when clearing it; equality of residual expressions is not permission to add original poles to the solution set.',
      'normalisation_note':'Zero verifies the independently derived expression difference; it is not a verbatim numerical key answer.'}
answers=[]
def add(kind,n,page,note,parts,direct=None):
    for p in parts:
        kp=p.pop('key_page_override');p.update(source_pdf_page=page,source_evidence=ev(page),
          answer_pdf_page=kp,answer_printed_page='A'+str(kp-586)if kp>=602 else kp-12,key_evidence=ev(kp))
    row={'item_id':f'8227:TB:YM:C4:{kind}:{n}','source_pdf_page':page,'notes':note,
      'assessed_8227_demand_ids':direct or[BND,ALL,TRANS],'component_demand_ids':[],
      'mapping_rationale':'The requested transformation/proof and complete bounded solution set are assessed. Factorisation or substitution used to reduce a trig equation is not automatically a separate polynomial-demand task. Supplied/hence results remain connected, and original zero factors,poles and intervals are preserved.',
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'within','quoted_value':note,
        'reason':'Actual input multipliers are1,2or1/2,including a70°shift; powers of a ratio are not extra argument multipliers.'},
        {'rule_id':'8227:LIMIT02','status':'within','quoted_value':note,'reason':'Finite interval solutions or the stated intermediate equation are asked for, not a general solution formula.'}],
      'exam_style':False,'exam_style_basis':'Ordinary worked Example/TryNow without exam attribution or an exam-style label.',
      'precision_angle_check':{'source':'Degrees/radians and exact-in-π requirements are preserved per part. Source keys sometimes retain extra digits.',
        'comparison':'Retain full internal accuracy; compare printed approximations at their written last place. Source between endpoints is read as strict where its own note expressly requires that interpretation.'},
      'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts}
    answers.append(row);return row

add('Example',46,209,'Solve sinxcosx=cos²x on0°≤x≤360°. Factoringcosx preserves the90°and270°roots that division bycosx would lose.',[
 roots('roots',f'sin({D})*cos({D})-cos({D})**2','FiniteSet(45,90,225,270)',209,[('cos','x','0',1),('tan','x','1',1)])])
for n,original,key,branches,unit in[
 (1,f'2*sin({D})*cos({D})-cos({D})','FiniteSet(30,90,150,270)',[('cos','x','0',1),('sin','x','1/2',1)],'degree'),
 (2,f'3*tan({D})-7*sin({D})',['0','64.6','180','295.4','360'],[('sin','x','0',1),('cos','x','3/7',1)],'degree'),
 (3,'tan(x)**2-tan(x)','FiniteSet(0,pi/4,pi,5*pi/4,2*pi)',[('tan','x','0',1),('tan','x','1',1)],'radian'),
 (4,f'sin({D})*cos({D})-3*cos({D})','FiniteSet(90,270)',[('cos','x','0',1),('sin','x','3',1)],'degree'),
 (5,'sin(2*x)*tan(2*x)-sin(2*x)','FiniteSet(0,pi/8,pi/2,5*pi/8,pi,9*pi/8,3*pi/2,13*pi/8,2*pi)',[('sin','2*x','0',1),('tan','2*x','1',1)],'radian')]:
    notes={1:'Solve2sinθcosθ=cosθ on0°..360°inclusive; keepcosθ=0 as well as sinθ=1/2.',
      2:'Solve3tanθ=7sinθ on0°..360°inclusive; sine-zero roots0°,180°,360°survive, while tangent poles remain invalid.',
      3:'Solve tan²θ−tanθ=0 on0..2πinclusive; factor tangent rather than cancel it, retaining both interval endpoints.',
      4:'Solve sinθcosθ=3cosθ on0°..360°inclusive; cosθ=0 is valid, while sinθ=3 has no real solution.',
      5:'Solve sin2x tan2x=sin2x on0..2πinclusive. The supplied sine2x graph supports the five sine-zero roots; four tangent-equals-one roots are also required, and tangent poles remain excluded.'}
    add('Try-Now-46',n,209,notes[n],[roots('roots',original,key,611 if n<=3 else 612,branches,unit=unit,approx=isinstance(key,list))])

add('Example',47,210,'Solve2cos²x−3cosx+1=0 and3sin²x−5cosx=5 strictly between0°and360°. The source explicitly excludes endpoints, so thecosx=1 branch in(a)adds no root.',[
 roots('a',f'2*cos({D})**2-3*cos({D})+1','FiniteSet(60,300)',210,[('cos','x','1/2',1),('cos','x','1',1)],opened=True),
 roots('b',f'3*sin({D})**2-5*cos({D})-5',['131.8','180','228.2'],210,[('cos','x','-2/3',1),('cos','x','-1',1)],approx=True,opened=True)])
for n,original,key,branches,hi,unit in[
 (1,f'tan({D})**2-9*tan({D})+14',['63.43','81.9','243.4','261.9'],[('tan','x','7',1),('tan','x','2',1)],'360','degree'),
 (2,f'sec({D})**2-sec({D})-2','FiniteSet(60,180,300)',[('cos','x','1/2',1),('cos','x','-1',1)],'360','degree'),
 (3,f'3*sin({D})**2-2*cos({D})-3',['90','131.8','228.2','270'],[('cos','x','0',1),('cos','x','-2/3',1)],'360','degree'),
 (4,f'15*sin({D})**2-13-cos({D})',['70.5','113.6'],[('cos','x','1/3',1),('cos','x','-2/5',1)],'180','degree'),
 (5,f'3*tan({D})**2-2*sec({D})**2-1','FiniteSet(60,120,240,300)',[('cos','x','1/2',1),('cos','x','-1/2',1)],'360','degree'),
 (6,'9*sec(x)**2-24*sec(x)+16',['0.723','5.56'],[('cos','x','3/4',1)],'2*pi','radian')]:
    statements={1:'tan²θ−9tanθ+14=0;0°≤θ≤360°',2:'sec²x−secx−2=0;0°≤x≤360°',
      3:'3sin²x−2cosx−3=0;0°≤x≤360°',4:'15sin²x=13+cosx;0°≤x≤180°',
      5:'3tan²θ=2sec²θ+1;0°≤θ≤360°',6:'9sec²x=24secx−16;strictly0<x<2π'}
    add('Try-Now-47',n,210,'Reduce and solve '+statements[n]+'. Keep all roots of each admissible ratio and reject the original reciprocal-function poles.',[
      roots('roots',original,key,612,branches,unit=unit,hi=hi,approx=isinstance(key,list),opened=n==6)],
      [BND,ALL,TRANS]+([REC]if n in[2,5,6]else[]))

add('Example',48,211,'Show2tan²θsin²θ=1 reduces to2sin⁴θ+sin²θ−1=0,then solve on0°≤θ≤360°. Clearingcos²θ preserves the originalcosθ≠0 restriction.',[
 transform('a','(2*tan(x)**2*sin(x)**2-1)*cos(x)**2','2*sin(x)**4+sin(x)**2-1',
  ['2*sin(x)**4-cos(x)**2'],'cos(x) != 0; the original equation is defined only there',211),
 roots('b',f'2*tan({D})**2*sin({D})**2-1','FiniteSet(45,135,225,315)',211,[('sin','x','1/sqrt(2)',1),('sin','x','-1/sqrt(2)',1)])])
add('Try-Now-48',1,211,'Show4sin⁴θ+5=7cos²θ becomes4u²+7u−2=0 withu=sin²θ; hence solve on0°..360°inclusive. Rejectu=−2, retainu=1/4.',[
 transform('a','4*sin(x)**4+5-7*cos(x)**2','4*sin(x)**4+7*sin(x)**2-2',[],
  'all real angles; u=sin(x)**2 lies in[0,1]',612),
 roots('b',f'4*sin({D})**4+5-7*cos({D})**2','FiniteSet(30,150,210,330)',612,[('sin','x','1/2',1),('sin','x','-1/2',1)])])
add('Try-Now-48',2,211,'Showcos⁴x≡1−2sin²x+sin⁴x,then solve8sin⁴x+cos⁴x=2cos²x on0°..360°. The valid substitution root issin²x=1/3,with both sine signs.',[
 transform('a','cos(x)**4','1-2*sin(x)**2+sin(x)**4',['(1-sin(x)**2)**2'],'all real x',612),
 roots('b',f'8*sin({D})**4+cos({D})**4-2*cos({D})**2',['35.3','144.7','215.3','324.7'],612,
  [('sin','x','1/sqrt(3)',1),('sin','x','-1/sqrt(3)',1)],approx=True)])
add('Example',49,212,'Solve4sin²x+8cosx−7=0 on0°..360°,rejectingcosx=3/2; hence solve its half-angle version on0°..360°,which retains onlyθ=120°.',[
 roots('a',f'4*sin({D})**2+8*cos({D})-7','FiniteSet(60,300)',212,[('cos','x','3/2',1),('cos','x','1/2',1)]),
 roots('b','4*sin(x*pi/360)**2+8*cos(x*pi/360)-7','FiniteSet(120)',212,[('cos','x/2','3/2',1),('cos','x/2','1/2',1)])])
p={'subpart':'a','operation':{'kind':'polynomial-roots-in-interval','operands':['3*x**2+8*x+4','-1','1']},
 'printed_key_normalised':'FiniteSet(-2/3)','key_page_override':612,'review_date':'2026-11-18',
 'method':'Substitute sin²x=1−cos²x into3sin²x−8cosx−7=0, obtaining3c²+8c+4=(3c+2)(c+2)=0. Rejectc=−2 because a real cosine lies in[−1,1], leavingc=−2/3.',
 'assertions':[{'expression':'(3*sin(x)**2-8*cos(x)-7)+(3*cos(x)**2+8*cos(x)+4)','expected':'0'}]}
add('Try-Now',49,212,'From3sin²x−8cosx−7=0,show the only real cosine ratio is−2/3; hence solve the70°shifted equation on0°≤θ≤180°.',[
 p,roots('b','3*sin((x+70)*pi/180)**2-8*cos((x+70)*pi/180)-7',['61.8','158.2'],612,
  [('cos','x+70','-2/3',1),('cos','x+70','-2',1)],hi='180',approx=True)])
add('Example',50,213,'Express(5+2tanx)/(3+2tanx)=1+tanx as2tan²x+3tanx−2=0,and hence solve on0≤x≤π; retaincosx≠0 and3+2tanx≠0.',[
 transform('quadratic','-((5+2*tan(x))/(3+2*tan(x))-1-tan(x))*(3+2*tan(x))','2*tan(x)**2+3*tan(x)-2',[],
  'cos(x) != 0 and3+2*tan(x) != 0; multiplication by the denominator is only on that original domain',213),
 roots('solutions','(5+2*tan(x))/(3+2*tan(x))-1-tan(x)',['0.464','2.03'],213,[('tan','x','1/2',1),('tan','x','-2',1)],unit='radian',hi='pi',approx=True)])
add('Try-Now-50',1,213,'Prove(tanx+1)/(sinxtanx+cosx)≡sinx+cosx;hence solve its equality to3sinx−2cosx on0≤x≤2π,keeping the original tangent poles excluded.',[
 transform('a','(tan(x)+1)/(sin(x)*tan(x)+cos(x))','sin(x)+cos(x)',
  ['(sin(x)+cos(x))/(sin(x)**2+cos(x)**2)'],'cos(x) != 0 andsin(x)*tan(x)+cos(x) != 0',612),
 roots('b','(tan(x)+1)/(sin(x)*tan(x)+cos(x))-3*sin(x)+2*cos(x)',['0.983','4.12'],612,[('tan','x','3/2',1)],unit='radian',approx=True)],[PROOF,BND,ALL,TRANS])
add('Try-Now-50',2,213,'Express2cos²x=tan²x as2cos⁴x+cos²x−1=0;solve on0≤x≤π giving exact answers inπ. Originalcosx=0 is undefined.',[
 transform('a','(2*cos(x)**2-tan(x)**2)*cos(x)**2','2*cos(x)**4+cos(x)**2-1',
  ['2*cos(x)**4-sin(x)**2'],'cos(x) != 0',612),
 roots('b','2*cos(x)**2-tan(x)**2','FiniteSet(pi/4,3*pi/4)',613,[('cos','x','1/sqrt(2)',1),('cos','x','-1/sqrt(2)',1)],unit='radian',hi='pi')])
add('Try-Now-50',3,213,'Use the supplied Example35identity to solve(1/sinθ−1/tanθ)²=2/5 on0≤θ≤2π. The identity is given,not a new requested proof; its original poles remain excluded.',[
 roots('roots','(1/sin(x)-1/tan(x))**2-2/5',['1.13','5.16'],613,[('cos','x','3/7',1)],unit='radian',approx=True)])
add('Try-Now-50',4,213,'Find all x strictly between−πandπ satisfying2cot2x=5. The doubled argument gives four roots in this interval.',[
 roots('roots','2*cot(2*x)-5',['0.190','1.76','-1.38','-2.95'],613,[('cot','2*x','5/2',1)],unit='radian',lo='-pi',hi='pi',approx=True,opened=True)],[BND,ALL,REC])

specs=[
 (209,'Example46 cosine-zero graph','The cosine graph marks its zeros90°and270°,preserving the branch lost by cancellation.','Example:46',None),
 (209,'Example46 tangent-one CAST','Tangent equals1inI/III, adding45°and225°to the cosine-zero branch.','Example:46',None),
 (209,'Try46Q5 given sine2x graph','Given graph has zeros0,π/2,π,3π/2,2π; the task also needs tangent-equals-one roots.','Try-Now-46:5',None),
 (210,'Example47a cosine-half CAST','The positive-cosine branch supplies60°and300°in the strict0°..360°interval.','Example:47','a'),
 (210,'Example47a excluded endpoint graph','The cosine1graph identifies0°and360°,both explicitly excluded by the source open interval.','Example:47','a'),
 (210,'Example47b negative-cosine CAST','Cosine−2/3gives two quadrantII/IIIroots,not the separate cosine−1root.','Example:47','b'),
 (210,'Example47b cosine-minus-one graph','The cosine graph contributes the axis-angle root180°,which is not obtained from an interior-quadrant mnemonic alone.','Example:47','b'),
 (211,'Example48 four sine-sign rays','Sin²θ=1/2gives sine±1/√2and four45°reference rays.','Example:48','b'),
 (212,'Example49a cosine-half rays','Cosx=1/2gives60°and300°; cosx=3/2is separately rejected as impossible.','Example:49','a'),
 (212,'Example49b restricted half-angle rays','The half-angle argument spans0°..180°,so the earlier300°argument is unavailable.','Example:49','b'),
 (213,'Example50 positive-tangent restricted CAST','Tanx=1/2in0..πkeepsIand excludesIII; basic angleatan(1/2).','Example:50','solutions'),
 (213,'Example50 negative-tangent restricted CAST','Tanx=−2in0..πkeepsIIand excludesIV; x=π−atan2.','Example:50','solutions')]
figures=[]
for n,(page,label,note,parent,part)in enumerate(specs,137):
 figures.append({'item_id':f'8227:TB:YM:C4:Teaching-figure:{n}','item_kind':'given-figure'if n==139 else'teaching-figure',
  'exercise':'Teaching figure','item_number':str(n),'pdf_page':page,'printed_page':page-12,'source_label':label,
  'parent_item_id':f'8227:TB:YM:C4:{parent}','parent_subpart':part,'notes':note,'what_it_shows':note,
  'assessed_8227_demand_ids':[],'component_demand_ids':[],'teaches_8227_demand_ids':[BND,ALL],
  'representation':'graph'if n in[137,139,141,143]else'diagram','source_evidence':ev(page),'learner_display':False,
  'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'within','quoted_value':note,
    'reason':'Fixed source single-angle,doubled-angle orhalf-angle graph/ray; no general solution form.'}],
  'value_level_scope_review_status_r5':'author original graph zeros,interval endpoints and ray signs read2026-11-18; independent check pending',
  'exam_representation_check':{'status':'final cross-book/examination comparison pending','examination_part_ids':[],
    'relation':'Source supporting graph/ray; showing it does not mean a learner sketch is requested.'},
  'mathematical_feature_review':{'status':'author mathematical features checked against parent solution branches; independent acceptance pending',
    'method':'Substitute every labelled zero/ray into its original factor equation and preserve original poles. Boundary graphs distinguish axis-angle roots from interior quadrant rays.'}})
pages=[]
for page in range(209,214):
 pages.append({'pdf_page':page,'printed_page':page-12,'chapter':4,'page_status':'items enumerated',
  'item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],
  'continuation_item_ids':[],'source_evidence':ev(page),
  'non_item_content':'All formal tasks and separate mathematical figures enumerated. Prose warnings about cancellation,open endpoints and impossible ratios remain linked instructional evidence.',
  'reader':'Codex author','date':'2026-11-18'})
if __name__=='__main__':
 for name,data in[
  ('answers-YM-C4-composite-equations.json',{'scope':'Every formal task/output onPDF209–213; connected transformations and original denominator restrictions retained.','items':answers}),
  ('census-YM-C4-composite-equations.json',{'book':'YM','book_id':'8227-SRC-017','chapter':4,'source_path':SRC,'source_sha256':SHA,
   'scope':'PDF209–213inclusive; allformal tasks and separate mathematical graphs/diagrams.','new_items':figures,'corrections':[],'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 print(len(answers),'items;',len(figures),'figures;',sum(len(r['subparts'])for r in answers),'outputs')
