"""YM49–51 exam-style/revision outputs and chapter summary census."""
import json
import author_YM_C1_intervals as base
import author_YM_C1_quadratic_graphs as graphs
import author_YM_C1_identities_cubics as identities
from author_YM_C1_intervals import opening,W,SRC,SHA,ev,v,reasoning,fig,figures,compute,expression,equivalent
opening.base.answers.clear();opening.base.new.clear();figures.clear();base.corrections.clear()
answers=opening.base.answers;new=opening.base.new;corrections=base.corrections
PAIR=base.PAIR;TANGENT='8227:2020:M1:T4:O02:D02';CRIT=base.CRIT;INTERVAL=base.INTERVAL;SQUARE=graphs.SQUARE;VERTEX=graphs.VERTEX;RECON=graphs.RECON;CUBIC=identities.CUBIC;IDENTITY=identities.IDENTITY
RECOG='8227:2020:M1:T1:O04:D01';SOLVE='8227:2020:M1:T1:O04:D02';FILTER='8227:2020:M1:T1:O04:D03';CALC='8227:2020:M1:T1:O02:D01';NATURE='8227:2020:M1:T1:O02:D02'

def add(kind,n,page,note,parts,direct,rep='text'):
 r=base.add(kind,n,page,note,parts,direct,rep)
 r['exam_style']=True;r['exam_style_basis']='Explicit YM1.7 Exam-Style Questions heading on49, or Revision Exercise1 with printed tariffs on50. This is source-labelled textbook exam-style, not a claim of NSSCAS examination observation.'
 r['mapping_rationale']='Explicit requested proof, parameter, coordinate pair, completed form or reconstruction is direct. Intermediate discriminants/quadratic solving stay components. Source chapter summaries teach their stated facets without creating extra assessed-response tasks.'
 return r

ps=[v('a-k-range','solve_univariate_inequality(36-4*x<0,x,relational=False)','Interval.open(9,oo)',49,
 'For monicy=x²−6x+k=(x−3)²+k−9, the whole graph is strictly above the axis exactly when its minimumk−9>0. Equivalently Δ36−4k<0. The positive leading coefficient is essential to the above-axis interpretation.'),
 v('b-tangent-k','solveset(16-4*(x-7),x,domain=S.Reals)','FiniteSet(11)',49,
 'Eliminatey=−2x+7 against the original parabola to getx²−4x+k−7=0. Repeated root condition Δ44−4k0 givesk11, contact(2,3).')]
ps[0].update(assessed_8227_demand_ids=[NATURE,'8227:2020:M1:T1:O02:D03'],component_demand_ids=[])
ps[1].update(assessed_8227_demand_ids=[TANGENT],component_demand_ids=[CALC,NATURE])
add('Example',38,49,'Find k for an entire upward parabola above the axis, then for a specified line tangent to it. Strict positivity and tangency are separate parameter conditions.',ps,[NATURE,'8227:2020:M1:T1:O02:D03',TANGENT])
p=reasoning('a-universal-meeting','Every real k gives at least one real intersection; the discriminant is(3k+1)²≥0.',
 'Equate2x²−3x+1 withkx+k²:2x²−(k+3)x+1−k²=0. The leading coefficient2 never vanishes. Its discriminant(k+3)²−8(1−k²)=(3k+1)² is nonnegative for all realk. Equality means one tangent intersection, not two distinct points; all otherk give two.',592,'show/prove')
p['additional_operations']={'discriminant_identity':{'kind':'identity','operands':['expand((k+3)**2-8*(1-k**2))-(3*k+1)**2']}};p['additional_operation_expected']={'discriminant_identity':'0'}
p2=v('b-tangent-k','solveset((3*x+1)**2,x,domain=S.Reals)','FiniteSet(-Rational(1,3))',592,
 'The discriminant square vanishes only atk−1/3. The leading coefficient2 remains nonzero, so this is genuine tangency.')
p3=v('b-contact','Tuple(((-Rational(1,3))+3)/4,(-Rational(1,3))*(((-Rational(1,3))+3)/4)+(-Rational(1,3))**2)','Tuple(Rational(2,3),-Rational(1,9))',592,
 'At the tangent parameter use the repeated-root abscissa(k+3)/4=2/3 and recover its ordinate from the original linekx+k². Direct substitution in the original curve gives the same−1/9.')
add('Try-Now',38,49,'Prove universal intersection of the parameter line and fixed quadratic; identify the unique tangent parameter and hence its full contact point.',[p,p2,p3],[PAIR,TANGENT])
ps=[base.interval('a','2*x**2-3*x>9','Union(Interval.open(-oo,-Rational(3,2)),Interval.open(3,oo))',592,'The standard polynomial2x²−3x−9=(2x+3)(x−3) is strictly positive outside its roots.'),
 graphs.form('b-completed-form','2*x**2-3*x','2*(x-Rational(3,4))**2-Rational(9,8)',592),graphs.vertex('b-vertex','2*x**2-3*x','Tuple(Rational(3,4),-Rational(9,8))',592)]
add('Revision-Exercise-1',1,50,'Solve the vertical-level inequality for2x²−3x, then complete its square and state the vertex. The printed tariffs are3+4marks.',ps,[CRIT,INTERVAL,SQUARE,VERTEX])
ps=[v('a-no-meeting-k','solve_univariate_inequality(x**2-144<0,x,relational=False)','Interval.open(-12,12)',592,
 'The original curve excludesx0. Againsty+x=k, multiplication bynonzerox gives3x²−kx+12=0. Constant12 prevents a spurious zero root. No meeting requires Δk²−144<0.'),
 base.system('b-pairs',['y+x-15','x*y-2*x**2-12'],'FiniteSet(Tuple(4,11),Tuple(1,14))',592,
 'Atk15, the eliminated equation3x²−15x+12=0 givesx1,4, both nonzero. Recover y14,11 respectively fromy15−x; A/B naming is interchangeable because no orientation is specified.')]
add('Revision-Exercise-1',2,50,'Find the no-intersection parameter range for y=2x+12/x andy+x=k, then full pairs atk15. Preserve the curve’s original x≠0 domain.',ps,[PAIR])
p=v('real-roots','18/x**4+1/x**2-4','FiniteSet(-Rational(3,2),Rational(3,2))',592,
 'Originalx≠0. Setu=1/x²>0, giving18u²+u−4=0 withu4/9 or−1/2. Reject negativeu before returning tox. The positive reciprocal square gives bothx±3/2; source notes thatx²−2 has no real solution.')
p['operation']={'kind':'real-roots','operands':['18/x**4+1/x**2-4']}
add('Revision-Exercise-1',3,50,'Find real roots of the reciprocal-quartic equation18/x⁴+1/x²=4, keeping the positive substitution range and both recovered signs.',[p],[RECOG,SOLVE,FILTER])
p=v('equation','expand((8/(0-2)**2)*(x-2)**2-8)','2*x**2-8*x',592,
 'Use vertex formA(x−2)²−8 and the original origin constraint, yieldingA2. This repeats Try26(a); it is a separate source occurrence, not additional problem-type breadth.')
r=add('Revision-Exercise-1',4,50,'Reconstruct the parabola through the origin with vertex(2,−8); this repeats Try26(a) exactly.',[p],[RECON]);r['source_interpretation']='Exact repeat of8227:TB:YM:C1:Try-Now:26part(a); retain the revision occurrence/tariff but do not count it as a distinct problem type.'
p=v('equation','expand((6/((0+3)*(0-Rational(2,3))**2))*(x+3)*(x-Rational(2,3))**2)','(x+3)*(3*x-2)**2/2',592,
 'Read crossing−3, touching2/3 and intercept6. With monic factorsA(x+3)(x−2/3)², intercept givesA9/2. Replacing the double factor by(3x−2)² dividesAby9, giving outer1/2. The diagram’s root is2/3, not2.')
add('Revision-Exercise-1',5,50,'Reconstruct the given cubic with one crossing, one rational touching root and y-intercept6. Preserve multiplicity and factor scaling.',[p],[CUBIC],rep='graph')
p=identities.coeff('constants','(x+a)*(2*x**2-3*x+4)','2*x**3+b*x**2-2*x+c',['a','b','c'],'Tuple(2,1,8)',592,
 'The x coefficient4−3a−2 determinesa2; then x² givesb1 and the constantc8. Check every coefficient of the original identity.')
add('Revision-Exercise-1',6,50,'Determine a,b,c in the cubic identity formed from a linear factor and supplied quadratic.',[p],[IDENTITY])
p=v('a','3*x-11*sqrt(x)-4','FiniteSet(16)',592,
 'Originala≥0. Useu=√a≥0, giving3u²−11u−4=(3u+1)(u−4). Onlyu4 survives;u−1/3 is inadmissible before squaring. Thusa16, not the squared image1/9 of the rejected negative substitution value.')
p['operation']={'kind':'real-roots','operands':['3*x-11*sqrt(x)-4']}
p['additional_operations']={'rejected_image_residual':{'kind':'identity','operands':['3*Rational(1,9)-11*sqrt(Rational(1,9))-4']}};p['additional_operation_expected']={'rejected_image_residual':'-Rational(22,3)'}
add('Revision-Exercise-1',7,50,'Solve3a−11√a−4=0 using a nonnegative square-root substitution; test the discarded branch before squaring back.',[p],[RECOG,SOLVE,FILTER])
refs=[
 (81,49,'Example38 inequality-sign reversal note','For the upward parabola,36−4k<0 givesk9+ after dividing by−4 and reversing the sign. The entire-curve-above interpretation depends on its fixed positive leading coefficient.',[NATURE],'table',[],'Example:38'),
 (82,50,'Revision5 given cubic graph','The curve crosses at−3, touches at2/3 and has intercept6. These values fix one shared scale; hand annotations are not publisher givens.',[CUBIC],'graph',[('(0+3)*(3*0-2)**2/2','6')],'Revision-Exercise-1:5'),
 (83,51,'Summary negative-discriminant orientation pair','For real quadratic coefficients witha≠0, Δ<0 gives no real roots: upward curves remain above the axis and downward curves below it.',[NATURE],'graph',[],None),
 (84,51,'Summary repeated-root orientation pair','Δ0 gives one distinct repeated real root for a nondegenerate quadratic. The repeated rational label again requires rational coefficients; this repeats the earlier table-domain caution.',[NATURE],'graph',[],None),
 (85,51,'Summary positive-discriminant orientation pair','Δ>0 gives two distinct real roots, with two crossings in either orientation. The summary here does not falsely require rationality for the generic positive case.',[NATURE],'graph',[],None),
 (86,51,'Summary extrema and symmetry orientations','Forf(x)=a(x+p)²+q,a≠0, symmetry isx−p and vertex(−p,q). Positivea gives a minimum; negativea gives a maximum. The glyphx−p denotesx=−p in the summary prose.',[SQUARE,VERTEX],'graph',[],None),
 (87,51,'Summary line/curve intersection table','After genuine quadratic elimination, Δ>0 means two distinct intersections, Δ0 tangency in these simple cases, and Δ<0 no intersection. Check the elimination degree and original domain before applying the table.',[PAIR,TANGENT],'table',[],None)]
for args in refs:fig(*args)
for f in figures:
 f['item_id']=f['item_id'].replace('Goldie:C5:','YM:C1:');f['parent_item_id']=f['parent_item_id'].replace('Goldie:C5:','YM:C1:')if f['parent_item_id']else None
 f['printed_page']=f['pdf_page']-11;f['source_evidence']=ev(f['pdf_page']);f['value_level_scope_decisions']=[]
notes={49:'All Example38/Try38 outputs recorded under the explicit Exam-Style heading. Universal meeting includes tangency; the sign-reversal callout is retained.',50:'Every seven-question revision output recorded, including the given cubic diagram. Printed tariffs total30 (7+6+4+3+3+4+3). The repeated parabola task is explicitly identified without inflating problem-type breadth.',51:'All chapter-summary teaching graphics/tables accounted for: three root-case orientation pairs, extrema pair, intersection table and associatedΔ≥0/support prose. The repeated-root rationality caution is linked to its prior source defect. No learner question starts here.'}
pages=[]
for page in range(49,52):
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 pages.append({'pdf_page':page,'printed_page':page-11,'chapter':1,'page_status':'items enumerated','item_ids':ids,'continuation_item_ids':[],
 'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-19','non_item_content':notes[page],
 'scope_screen':'Every closing exam-style/revision response and summary reference recorded. Original domains, repeated/real-root semantics and factor scaling preserved; summary support is not extra assessed practice.'})
if __name__=='__main__':
 for name,data in [('answers-YM-C1-closing.json',{'scope':'Every49–50response;51summary references have no separate learner answers.','items':answers}),('census-YM-C1-closing.json',{'book':'YM','book_id':'8227-SRC-017','chapter':1,'source_path':SRC,'source_sha256':SHA,'scope':'Complete49–51census, finishing theC1source envelope12–51.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if'operation'in p:assert equivalent(compute(p['operation']),expression(p['printed_key_normalised'])),(row['item_id'],p['subpart'])
   for n,op in p.get('additional_operations',{}).items():
    if n in p.get('additional_operation_expected',{}):assert equivalent(compute(op),expression(p['additional_operation_expected'][n])),(row['item_id'],p['subpart'],n)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'figures;',len(pages),'pages')
