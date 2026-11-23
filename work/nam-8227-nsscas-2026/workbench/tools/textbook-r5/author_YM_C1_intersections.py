"""YM40–42: intersection multiplicity, parameter ranges and source boundaries."""
import json
import author_YM_C1_intervals as base
from author_YM_C1_intervals import opening,W,SRC,SHA,ev,v,reasoning,fig,figures,compute,expression,equivalent
opening.base.answers.clear();opening.base.new.clear();figures.clear();base.corrections.clear()
answers=opening.base.answers;new=opening.base.new;corrections=base.corrections
PAIR=base.PAIR;TANGENT='8227:2020:M1:T4:O02:D02';CALC='8227:2020:M1:T1:O02:D01';NATURE='8227:2020:M1:T1:O02:D02';CRIT=base.CRIT;INTERVAL=base.INTERVAL

def add(kind,n,page,note,parts,direct):
 r=base.add(kind,n,page,note,parts,direct)
 r['component_demand_ids']=[d for d in [CALC,NATURE]if d not in direct]
 r['mapping_rationale']='The explicit task is an intersection/tangency condition or parameter interval. Discriminant calculation is a component of establishing that requested geometric condition. Exact intersection coordinates are not invented when only a parameter set is requested. Linear degeneration and nonzero original denominators are checked separately.'
 return r

def condition(label,expr,key,kp,method):return v(label,expr,key,kp,method+' Eliminate from the original two equations, check the eliminated equation’s degree/domain, then interpret its root multiplicity as the number of geometric intersections.')

p=condition('k','solveset((4*x-4)**2-16*x**2,x,domain=S.Reals)','FiniteSet(Rational(1,2))',40,
 'For y2x+k and y²4x, substitution gives4x²+(4k−4)x+k²=0, with fixed leading coefficient4. Tangency requires Δ16−32k=0; k1/2. The repeated rootx1/4 givesy1 in both originals.')
p['additional_operations']={'tangent_point_checks':{'kind':'identity','operands':['Tuple(1-(2*Rational(1,4)+Rational(1,2)),1**2-4*Rational(1,4))']}};p['additional_operation_expected']={'tangent_point_checks':'Tuple(0,0)'}
add('Example',31,40,'Determine k for tangency between y=2x+k and y²=4x using a repeated root, not a pair of distinct intersections.',[p],[TANGENT])
for n,note,expr,key,method in [
 (1,'Find both slopes k for which y=kx+6 is tangent to y=x²+3x+2k.','solveset((3-x)**2-4*(2*x-6),x,domain=S.Reals)','FiniteSet(3,11)',
 'The intersection polynomial has a1 and coefficients3−k,2k−6. Set Δk²−14k+33 to zero; both3 and11 satisfy the original tangency condition.'),
 (2,'Find p for tangency of2y+x=p and y²+2x=13.','solveset(16-4*(2*x-13),x,domain=S.Reals)','FiniteSet(Rational(17,2))',
 'Eliminate x=p−2y. The genuine quadratic is y²−4y+2p−13=0. Δ68−8p=0 gives p17/2; its repeatedy2 recoversx9/2.')]:
 add('Try-Now-31',n,40,note,[condition('parameter',expr,key,590,method)],[TANGENT])
ps=[condition('a-x-range','solve_univariate_inequality(2*x**2-6*x+5>13,x,relational=False)','Union(Interval.open(-oo,-1),Interval.open(4,oo))',590,
 'Part(a) asks where the given curve exceeds13:2(x−4)(x+1)>0. Select both exterior open rays; this is a quadratic inequality rather than a tangency calculation.'),
 condition('b-tangent-k','solveset(64-8*(5-x),x,domain=S.Reals)','FiniteSet(-3)',590,
 'Against liney2x+k the intersection is2x²−8x+5−k=0. Tangency requires Δ24+8k=0; k−3, giving contactx2,y1.')]
add('Try-Now-31',3,41,'First solve a vertical-level inequality for y=2x²−6x+5; then find k for a specified tangent slope. These connected parts assess different requested results.',ps,[CRIT,INTERVAL,TANGENT])
p=condition('p-range','solve_univariate_inequality((2-x)**2-16>0,x,relational=False)','Union(Interval.open(-oo,-2),Interval.open(6,oo))',41,
 'Lineypx+1 versuscurveyx²+2x+5 givesx²+(2−p)x+4=0. Two distinct intersections require Δ(p−6)(p+2)>0. Exclude both tangency boundaries.')
add('Example',32,41,'Determine all line slopes p giving two distinct intersections of y=px+1 with y=x²+2x+5. Select exterior parameter intervals from the discriminant.',[p],[PAIR,CRIT,INTERVAL])
rows=[
 (1,41,'Find p for two distinct intersections of2y+x=p andxy6.','solve_univariate_inequality(x**2-48>0,x,relational=False)','Union(Interval.open(-oo,-sqrt(48)),Interval.open(sqrt(48),oo))',
 'Withy=(p−x)/2, the intersection polynomialx²−px+12=0 has Δp²−48. Its nonzero constant prevents an original forbidden x0 root; both exterior intervals yield distinct valid points.'),
 (2,41,'Find k for two distinct intersections of y=2x−k and y=x²+kx−2.','solve_univariate_inequality((x-2)**2-4*(x-2)>0,x,relational=False)','Union(Interval.open(-oo,2),Interval.open(6,oo))',
 'The intersection polynomialx²+(k−2)x+k−2 has leading coefficient1. Δ(k−2)(k−6)>0; exclude2 and6.'),
 (3,42,'Find q for two distinct intersections of the source’s negative reciprocal y=−2/x with y=qx+3q.','solve_univariate_inequality(9*x**2-8*x>0,x,relational=False)','Union(Interval.open(-oo,0),Interval.open(Rational(8,9),oo))',
 'The native source confirms the minus sign in−2/x. Withx≠0, eliminate toqx²+3qx+2=0. Δ9q²−8q>0 givesq<0 orq>8/9, automatically excludingq0. Atq0 the original liney0 never meets−2/x; do not apply a quadratic proof to that constant equation.'),
 (4,42,'Find k where y=x+2 meets y²+(x+k)²=2, including tangency as explicitly allowed by the hint.','solve_univariate_inequality(4*(x+2)**2-8*(x**2+2)>=0,x,relational=False)','Interval(0,4)',
 'Direct substitution gives2x²+2(k+2)x+k²+2=0. Its leading coefficient2 is fixed; Δ4k(4−k)≥0 gives0≤k≤4. Equality endpoints are tangencies. No circle-centre/radius knowledge is needed: the implicit relation is supplied.')]
for n,page,note,expr,key,method in rows:
 add('Try-Now-32',n,page,note,[condition('parameter-range',expr,key,590,method)],[PAIR,CRIT,INTERVAL]+([TANGENT]if n==4 else[]))
p=condition('c-range','solve_univariate_inequality(36-4*(7+x)<0,x,relational=False)','Interval.open(2,oo)',42,
 'Subtracty2x−7 fromyx²−4x+c to getx²−6x+7+c=0. No intersection requires Δ8−4c<0, so c>2; equality would be a tangent.')
add('Example',33,42,'Determine c so the liney=2x−7 never meets y=x²−4x+c; no real intersection root means a strictly negative discriminant.',[p],[PAIR])
rows=[
 (1,'Find k for no intersection between y=x² and y=4x+k.','solve_univariate_inequality(16+4*x<0,x,relational=False)','Interval.open(-oo,-4)',
 'The intersection polynomialx²−4x−k has fixed leading coefficient1; Δ16+4k<0 givesk<−4.'),
 (2,'For nonzero k, find when y=kx²+1 and y=kx have no common points. Preserve the requested supporting sketch hint.','solve_univariate_inequality(x**2-4*x<0,x,relational=False)','Interval.open(0,4)',
 'The intersection polynomialkx²−kx+1 has a nonzero leading coefficient by the stem. Δk²−4k<0 gives0<k<4, which respects the original restriction.'),
 (3,'Find k for no intersection between y=kx²−3x and y=x−k. The printed key’s bounds±4 are wrong.','solve_univariate_inequality(16-4*x**2<0,x,relational=False)','Union(Interval.open(-oo,-4),Interval.open(4,oo))',
 'The native source gives−3x, not another linear coefficient. Elimination giveskx²−4x+k=0. For k≠0, Δ16−4k²<0 givesk<−2 or k>2. Atk0 the original lines intersect atx0, so it does not add an omitted no-intersection case. Examplek3 has Δ−20<0 and is valid despite being excluded by the key.'),
 (4,'Find k for no intersection betweenxy3 andy=−3x+k.','solve_univariate_inequality(x**2-36<0,x,relational=False)','Interval.open(-6,6)',
 'Eliminatingy gives−3x²+kx−3=0, with nonzero a−3 and Δk²−36. Its constant−3 ensures the forbidden hyperbola abscissax0 is never an introduced root. Negative Δ gives−6<k<6.')]
for n,note,expr,key,method in rows:
 p=condition('parameter-range',expr,key,591,method)
 if n==3:
  p['author_expected_normalised']='Union(Interval.open(-oo,-2),Interval.open(2,oo))'
  p['additional_operations']={'valid_counterexample_discriminant':{'kind':'identity','operands':['16-4*3**2']},'linear_boundary_root':{'kind':'real-roots','operands':['-4*x']}}
  p['additional_operation_expected']={'valid_counterexample_discriminant':'-20','linear_boundary_root':'FiniteSet(0)'}
 ps=[p]
 if n==2:
  ps.append(reasoning('supporting-sketch','For the parameter polynomialk(k−4), draw an upward parabola crossing at0,4; it is negative strictly between those open endpoints.',
   'This is the source’s explicit hint to draw a sketch when the parameter condition is a quadratic inequality. Its answer section gives the correct range but no separate sketch. Derive the orientation, critical values and open interval fromk²−4k; no publisher sketch match is claimed.',591,'no key'))
 r=add('Try-Now-33',n,42,note,ps,[PAIR]+([CRIT,INTERVAL]if n in[2,3,4]else[]))
 if n==2:
  q=r['subparts'][-1];q.update(answer_pdf_page=None,answer_printed_page=None,key_presence='no separate key',inspected_key_pdf_pages=[591],key_evidence=ev(591))
  r['sketch_response_required']=True

refs=[
 (63,40,'Tangent intersection schematic','A nondegenerate quadratic elimination with Δ0 has one repeated solution, represented by a line touching a parabola at one point. This is a simple supplied-curve case, not a universal theorem for every curve.',[PAIR,TANGENT],'graph',[],None),
 (64,40,'Two-point intersection schematic','For a genuine quadratic elimination, Δ>0 gives two distinct real intersections. The source draws a secant line crossing a parabola twice.',[PAIR],'graph',[],None),
 (65,40,'No-intersection schematic','For a genuine real quadratic elimination, Δ<0 gives no real intersection point. The displayed line stays below the upward parabola.',[PAIR],'graph',[],None),
 (66,41,'Example32 parameter-sign parabola','The parameter polynomialp²−4p−12=(p−6)(p+2) opens upward, with roots−2,6 and negative interior. Strict positivity selects the two exterior ranges.',[CRIT,INTERVAL],'graph',[('expand((p-6)*(p+2))','p**2-4*p-12')],'Example:32'),
 (67,41,'Example32 parameter number line','Open endpoints−2,6 and outward rays express two distinct intersections. Closing an endpoint would admit a tangent.',[PAIR,INTERVAL],'diagram',[],'Example:32'),
 (68,41,'Example32 orientation reminder','The sketch concerns a quadratic in parameterp, not the originalx-coordinate curve. Its positive leading coefficient determines the exterior sign regions.',[CRIT,INTERVAL],'table',[],'Example:32'),
 (69,42,'Strict versus inclusive endpoint reminder','The source explicitly contrasts>,≥,<,≤. Tangency may be included only when the requested intersection condition permits a repeated root.',[INTERVAL,TANGENT],'table',[],None)]
for args in refs:fig(*args)
for f in figures:
 f['item_id']=f['item_id'].replace('Goldie:C5:','YM:C1:');f['parent_item_id']=f['parent_item_id'].replace('Goldie:C5:','YM:C1:')if f['parent_item_id']else None
 f['printed_page']=f['pdf_page']-11;f['source_evidence']=ev(f['pdf_page']);f['value_level_scope_decisions']=[]
notes={40:'All three intersection schematics, Example31 and both numbered Try31 tasks starting here recorded. The third Try31 task starts41.',41:'Try31Q3, Example32 and first two numbered Try32 tasks recorded. The worked parameter sketch, number line and orientation callout are separate teaching records.',42:'Both remaining Try32 tasks, Example33, all four Try33 tasks and the endpoint reminder recorded. The nonzero-k and denominator domains are explicit; source−2/x sign and Try33Q3 wrong key are native-verified. Try33Q2 sketch is author-derived because no separate key sketch is printed.'}
pages=[]
for page in range(40,43):
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 pages.append({'pdf_page':page,'printed_page':page-11,'chapter':1,'page_status':'items enumerated','item_ids':ids,'continuation_item_ids':[],
 'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-19','non_item_content':notes[page],
 'scope_screen':'Simple supplied quadratic/reciprocal/implicit relations reduce directly to intersection equations. No extra circle theorem or advanced tangent method is assumed. All parameter degenerations and original denominator exclusions are checked.'})
if __name__=='__main__':
 for name,data in [('answers-YM-C1-intersections.json',{'scope':'Every40–42original response, including the explicitly hinted sketch.','items':answers}),('census-YM-C1-intersections.json',{'book':'YM','book_id':'8227-SRC-017','chapter':1,'source_path':SRC,'source_sha256':SHA,'scope':'Complete40–42page census.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(row['item_id'],p['subpart'])
   for n,op in p.get('additional_operations',{}).items():
    if n in p.get('additional_operation_expected',{}):assert equivalent(compute(op),expression(p['additional_operation_expected'][n])),(row['item_id'],p['subpart'],n)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'figures;',len(pages),'pages')
