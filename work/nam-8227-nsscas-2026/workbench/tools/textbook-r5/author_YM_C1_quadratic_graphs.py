"""YM31–35: fixed-source square completion, full sketch features and reconstruction."""
import json
import author_YM_C1_opening as opening
from author_YM_C1_opening import W,SRC,SHA,ev,v,fig,figures,compute,expression,equivalent
opening.base.answers.clear();opening.base.new.clear();figures.clear()
answers=opening.base.answers;new=opening.base.new;corrections=[]
SQUARE='8227:2020:M1:T1:O01:D01';VERTEX='8227:2020:M1:T1:O01:D02';SKETCH='8227:2020:M1:T1:O01:D03';RECON='8227:2020:M1:T1:O05:D01'

def add(kind,n,page,note,parts,direct,sketch=False,rep='text'):
    r=opening.add(kind,n,page,note,parts,direct)
    prior=new.pop();corrections.append({k:prior[k]for k in ['item_id','pdf_page','printed_page','continuation_pdf_pages']})
    r.update(representation=rep,sketch_response_required=sketch,
      mapping_rationale='A prescribed completed-square expression, vertex or sketch is directly assessed when requested. Reconstructing a quadratic from sufficient graph/point constraints is a separate decision. Merely using a diagram or an intermediate factorisation does not assess sketching or identity recognition.',
      precision_angle_check={'source':'Exact rational coefficients and graph labels; no angle quantities or physical units.','comparison':'Keep exact vertices, intercepts and root multiplicities. A qualitative sketch need not use equal physical axis scales, but its labels must agree with the same function.'})
    return r

def form(label,f,key,kp):
    p=v(label,f,key,kp,'Complete the square independently by factoring the nonunit quadratic coefficient, adding and subtracting the square of half the remaining linear coefficient, then distributing the outer factor. Expand the separately transcribed completed form to confirm equality; retain the requested form, not just an expanded equivalent.')
    p['author_answer_form']=key
    return p

def vertex(label,f,key,kp):
    f='('+f+')';vx='(-('+f+').expand().coeff(x,1)/(2*('+f+').expand().coeff(x,2)))'
    expr='Tuple('+vx+','+f+'.subs(x,'+vx+'))'
    p=v(label,expr,key,kp,'Independently locate the symmetry axis −b/(2a), substitute it into the original polynomial, and classify maximum/minimum by the original leading-coefficient sign. Compare the exact coordinate pair; the required nature is recorded separately.')
    p['vertex_nature']='minimum'if expression(f).expand().coeff(expression('x'),2)>0 else'maximum'
    return p

def sketch(label,f,kp,roots,keyfeatures,description):
    p={'subpart':label,'operation':{'kind':'polynomial-sketch','operands':[f]},'printed_key_features':{'labelled_x_intercepts':roots},'key_page_override':kp,
       'method':'Derive real intercepts with multiplicities, y-intercept and leading sign from the original polynomial. Independently derive the vertex/symmetry axis; compare all labelled features on the rendered key. The source-render comparison is an author reading, not automated image recognition.',
       'required_features':description}
    vv=vertex('unused',f,'0',kp)['operation']['operands'][0]
    p['additional_comparisons']=[{'operation':{'kind':'identity','operands':[vv]},'printed_key_normalised':keyfeatures}]
    p['additional_operations']={'vertex':{'kind':'identity','operands':[vv]},'original_y_intercept':{'kind':'identity','operands':['('+f+').subs(x,0)']}}
    p['additional_operation_expected']={'vertex':keyfeatures}
    return p

ps=[form('a','x**2-8*x+7','(x-4)**2-9',31),vertex('b','x**2-8*x+7','Tuple(4,-9)',31),
 sketch('c','x**2-8*x+7',31,['1','7'],'Tuple(4,-9)','Upward opening; vertex(4,−9), symmetry axisx4, roots1,7, y-intercept7. The source sketch and labelled minimum agree.')]
add('Example',21,31,'Complete x²−8x+7 into the prescribed form, use it for the minimum vertex, then sketch with both intercepts and symmetry.',ps,[SQUARE,VERTEX,SKETCH],True)
for n,f,key,vert,roots in [(1,'x**2+3*x-4','(x+Rational(3,2))**2-Rational(25,4)','Tuple(-Rational(3,2),-Rational(25,4))',['-4','1']),
                         (2,'x**2-6*x+8','(x-3)**2-1','Tuple(3,-1)',['2','4'])]:
    ps=[form('completed-form',f,key,588),vertex('a-vertex',f,vert,588),sketch('b-sketch',f,588,roots,vert,
       'Upward parabola with exact labelled vertex '+vert+', complete roots '+','.join(roots)+' and original y-intercept; show the minimum and symmetry axis.')]
    if n==1:
        ps[-1]['author_source_graph_comparison']={'status':'key wrong','reason':'The exact vertex coordinate printed below the graph is correct, but the horizontal guide tick on the y-axis says−6½ rather than−6¼. These cannot both label the same vertex.',
          'observed_features':'Correct coordinate(−3/2,−25/4), but incorrect vertical tick−6½.','correct_features':'Use−25/4=−6¼ consistently.'}
    add('Try-Now-21',n,32,'Complete and sketch '+f+' using the prescribed form; retain exact vertex, minimum, intercepts and consistent guide labels.',ps,[SQUARE,VERTEX,SKETCH],True)
ps=[form('a-completed-form','5*x**2+8*x-2','5*(x+Rational(4,5))**2-Rational(26,5)',32),
 v('a-minimum','(5*x**2+8*x-2).subs(x,-Rational(4,5))','-Rational(26,5)',32,'The completed form has a positive coefficient5 multiplying a nonnegative square. Its least value is−26/5; confirm by substitution.'),
 v('b-minimising-x','-8/(2*5)','-Rational(4,5)',32,'The square vanishes at x−4/5. This is the abscissa, distinct from the minimum function value−26/5.')]
add('Example',22,32,'Complete 5x²+8x−2, state its minimum value and the x-value where it occurs. The nonunit outer coefficient scales the subtracted square.',ps,[SQUARE,VERTEX])
ps=[]
for l,f,key,vx,vy in [('a','3*x**2-6*x-3','3*(x-1)**2-6','1','-6'),('b','2*x**2-6*x-10','2*(x-Rational(3,2))**2-Rational(29,2)','Rational(3,2)','-Rational(29,2)'),('c','2*x**2+7*x-15','2*(x+Rational(7,4))**2-Rational(169,8)','-Rational(7,4)','-Rational(169,8)'),('d','3*x**2+2*x+Rational(1,3)','3*(x+Rational(1,3))**2','-Rational(1,3)','0')]:
    ps.extend([form(l+'-i-form',f,key,588),v(l+'-ii-minimum','('+f+').subs(x,'+vx+')',vy,588,'The original leading coefficient is positive. The square term is nonnegative and reaches zero at the independently derived vertex; compare the least value exactly.'),
     v(l+'-ii-x','-('+f+').expand().coeff(x,1)/(2*('+f+').expand().coeff(x,2))',vx,588,'Locate the zero of the completed square, independently confirmed as −b/(2a). Keep the x-value separate from the minimum y-value.')])
add('Try-Now',22,32,'Complete all four nonunit-coefficient quadratics and state each minimum value and attaining x. Fractional vertices and the zero minimum are explicit.',ps,[SQUARE,VERTEX])
ps=[form('a-form','8*x-x**2','16-(x-4)**2',33),v('a-constants','Tuple(16,-4)','Tuple(16,-4)',33,'The required form is a−(x+b)². Expansion gives the linear coefficient −2b=8, so b−4 and a16; these constants are not the generic leading coefficient a in ax²+bx+c.'),
 vertex('b','8*x-x**2','Tuple(4,16)',33),sketch('c','8*x-x**2',33,['0','8'],'Tuple(4,16)','Downward parabola, maximum(4,16), roots0,8 and y-intercept0; symmetry axisx4.')]
# Native enlargement resolves the apparent sign issue as -(-4), which is correct.
ps[2]['source_reading_clarification']='Native source annotation is (−b,a):(−(−4),16), giving(4,16). No vertex-sign defect. The nearby a<0 uses a for the generic leading coefficient−1, distinct from the stem’s named constanta16; avoid that notation collision in new explanations.'
add('Example',23,33,'Complete the downward quadratic8x−x² in a−(x+b)², state its constants and maximum vertex, then sketch. Keep source constant a distinct from the generic leading coefficient.',ps,[SQUARE,VERTEX,SKETCH],True)
for n,f,key,constants,vert,roots,kp in [(1,'6*x-x**2','9-(x-3)**2','Tuple(9,-3)','Tuple(3,9)',['0','6'],588),
 (2,'2*x**2-3*x','2*(x-Rational(3,4))**2-Rational(9,8)','Tuple(2,-Rational(3,4),-Rational(9,8))','Tuple(Rational(3,4),-Rational(9,8))',['0','Rational(3,2)'],589)]:
    ps=[form('a-form',f,key,kp),v('a-constants',constants,constants,kp,'Read the constants in the prescribed completed-square form after independently expanding it to the original polynomial; preserve the sign inside the bracket.'),vertex('b',f,vert,589 if n==2 else 588),
     sketch('c',f,589,roots,vert,'Show both roots, y-intercept0, the exact vertex '+vert+' and its symmetry axis. The sign of the original quadratic coefficient determines upward/downward orientation.')]
    # Constants are also independently recovered by polynomial coefficient comparison.
    expr='Tuple(9,-3)'if n==1 else'Tuple(2,-Rational(3,4),-Rational(9,8))'
    ps[1]['operation']['operands']=[('Tuple((-(-6)/2)**2,-6/2)'if n==1 else'Tuple(2,-3/(2*2),0-(-3)**2/(4*2))')]
    add('Try-Now-23',n,33,'Complete, identify constants, find vertex and sketch '+f+'. Its prescribed completed form and consequent graph stay linked.',ps,[SQUARE,VERTEX,SKETCH],True)
ps=[sketch('sketch','x**2/2-3*x+5',34,[],'Tuple(3,Rational(1,2))','Upward parabola with minimum(3,1/2), axisx3 and y-intercept5; no real x-intercepts. Both source methods agree; Δ−1 confirms no crossing.')]
add('Example',24,34,'Sketch y=x²/2−3x+5. The worked example compares completion of squares with the vertex formula; the positive minimum means no real crossings.',ps,[SKETCH],True)
ps=[]
for l,f,roots,vert,desc in [('a','x**2+5*x-14',['-7','2'],'Tuple(-Rational(5,2),-Rational(81,4))','Upward, roots−7,2, intercept−14; vertex(−5/2,−81/4).'),
 ('b','x**2-6*x+13',[],'Tuple(3,4)','Upward, no real roots, intercept13; vertex(3,4), reflected point(6,13).'),
 ('c','12+x-x**2',['-3','4'],'Tuple(Rational(1,2),Rational(49,4))','Downward, roots−3,4, intercept12; vertex(1/2,49/4).'),
 ('d','-4*x**2+16*x-7',['Rational(1,2)','Rational(7,2)'],'Tuple(2,9)','Downward, roots1/2,7/2, intercept−7; vertex(2,9), reflected point(4,−7).')]:ps.append(sketch(l,f,589,roots,vert,desc))
add('Try-Now',24,34,'Sketch four quadratics with upward/downward orientation and either two or no real crossings. All printed vertices, intercepts and extra symmetric points are checked.',ps,[SKETCH],True)
p=v('equation','expand((8/(((-1)+3)*((-1)-1)))*(x+3)*(x-1))','-2*x**2-4*x+6',35,
 'The diagram gives roots−3,1, vertex(−1,8) and y-intercept6. Start y=A(x+3)(x−1); vertex height gives A−2. Independently using y(0)=6 gives the same A. All redundant givens must agree.')
p['additional_operations']={'independent_intercept_scale':{'kind':'identity','operands':['6/(3*(-1))']},'vertex_height':{'kind':'identity','operands':['(-2*x**2-4*x+6).subs(x,-1)']}}
p['additional_operation_expected']={'independent_intercept_scale':'-2','vertex_height':'8'}
add('Example',25,35,'Reconstruct a quadratic from the supplied graph: roots−3,1 plus either vertex(−1,8) or intercept6. Check all redundant graph labels.',[p],[RECON],rep='graph')
ps=[v('a','expand((3/((0-2)*(0+3)))*(x-2)*(x+3))','-x**2/2-x/2+3',589,
 'Roots2,−3 fix the factor form A(x−2)(x+3). The given y-intercept3 gives−6A=3 and A−1/2. Expand only after determining the shared scale.'),
 v('b','expand((-1/(0-2)**2)*(x-2)**2)','-x**2/4+x-1',589,
 'Touching the axis at2 means a double root, not two unspecified crossings. Use A(x−2)². The given y-intercept−1 gives4A−1 and A−1/4.')]
add('Try-Now',25,35,'Reconstruct two parabolas from prose givens: two distinct roots plus y-intercept, or one touching root plus y-intercept. Multiplicity changes the factor structure.',ps,[RECON])
p=v('equation','expand(((3-(-1))/(0-2)**2)*(x-2)**2-1)','x**2-4*x+3',35,
 'Use vertex form A(x−2)²−1. The extra point(0,3) gives4A−1=3, hence A1. Independently verify the resulting vertex and intercept from the original derived polynomial.')
add('Example',26,35,'Reconstruct a quadratic from turning point(2,−1) and y-intercept3 using vertex form; the given diagram reflects those same constraints.',[p],[RECON],rep='graph')

refs=[
 (41,31,'Upward/downward extrema orientation','For real a≠0, ax²+bx+c opens upward ifa>0 and downward ifa<0. Its vertex gives a global minimum or maximum respectively.',[VERTEX],'graph',[],None),
 (42,31,'Example21 completed-square sketch','Forx²−8x+7, the source labels roots1,7, intercept7 and minimum(4,−9); all derive from(x−4)²−9.',[SQUARE,VERTEX,SKETCH],'graph',[('Tuple((1-4)**2-9,(7-4)**2-9,(0-4)**2-9)','Tuple(0,0,7)')],'Example:21'),
 (43,31,'Quadratic sketch feature checklist','The source asks for opening orientation, x/y intercepts and turning point. A feature-based response should keep all labels tied to one polynomial; it is not a plot of unrelated chosen points.',[SKETCH],'table',[],'Example:21'),
 (44,32,'Vertex sign reminder','y=(x+p)²+q has vertex(−p,q), whereas y=(x−p)²+q has vertex(p,q). The bracket sign reverses the vertex abscissa.',[SQUARE,VERTEX],'table',[('Tuple((-2+2)**2+3,(2-2)**2+3)','Tuple(3,3)')],None),
 (45,32,'Nonunit coefficient completion note','Take5 out of5x²+8x−2 before completing the inner square. The adjustment inside the bracket is multiplied by5 on distribution.',[SQUARE],'table',[('expand(5*(x+Rational(4,5))**2-Rational(26,5))','5*x**2+8*x-2')],'Example:22'),
 (46,33,'Example23 downward sketch','y=8x−x² has roots0,8 and maximum(4,16). Native source confirms its side annotation is−(−4), not−4. The a<0 remark uses the generic leading-coefficient symbol, not the named constanta16.',[VERTEX,SKETCH],'graph',[('Tuple(8*0-0**2,8*4-4**2,8*8-8**2)','Tuple(0,16,0)')],'Example:23'),
 (47,34,'General vertex formula reference','For actual quadratic a≠0, vertex(−b/(2a),−(b²−4ac)/(4a)), axisx=−b/(2a). It is an alternative to completion when the question does not enforce that method.',[VERTEX],'table',[('simplify(a*(-b/(2*a))**2+b*(-b/(2*a))+c)','-(b**2-4*a*c)/(4*a)')],None),
 (48,34,'Example24 two vertex methods','Both completion and the coordinate formula give(3,1/2) forx²/2−3x+5. Methods are alternatives for one source task, not separate problem types.',[SQUARE,VERTEX],'table',[('expand((x-3)**2/2+Rational(1,2))','x**2/2-3*x+5')],'Example:24'),
 (49,34,'Example24 no-crossing sketch','The parabola’s minimum1/2 is above the axis, with y-intercept5. Δ−1 gives no real roots; the source figure must retain that vertical position.',[SKETCH],'graph',[('(-3)**2-4*Rational(1,2)*5','-1')],'Example:24'),
 (50,35,'Root-factor reconstruction reference','Given rootsx1,x2, use y=A(x−x1)(x−x2), with A≠0 determined by a further compatible point away from those roots. A touching root is repeated.',[RECON],'table',[],None),
 (51,35,'Example25 given reconstruction graph','Labels supply roots−3,1, vertex(−1,8) and intercept6. Both extra data independently giveA−2; do not generate arbitrary independent labels.',[RECON],'graph',[('Tuple(-2*(0+3)*(0-1),-2*(-1+3)*(-1-1))','Tuple(6,8)')],'Example:25'),
 (52,35,'Vertex-form reconstruction reference','Given vertex(p,q), use y=A(x−p)²+q. A further point with x≠p determinesA; a point at the vertex alone leaves its scale undetermined.',[RECON],'table',[],None),
 (53,35,'Example26 vertex-and-intercept graph','The upward graph has vertex(2,−1), intercept3 and equation(x−2)²−1. Those same data determineA1.',[RECON],'graph',[('Tuple((2-2)**2-1,(0-2)**2-1)','Tuple(-1,3)')],'Example:26')]
for args in refs:fig(*args)
for f in figures:
    f['item_id']=f['item_id'].replace('Goldie:C5:','YM:C1:');f['parent_item_id']=f['parent_item_id'].replace('Goldie:C5:','YM:C1:')if f['parent_item_id']else None
    f['printed_page']=f['pdf_page']-11;f['source_evidence']=ev(f['pdf_page']);f['value_level_scope_decisions']=[]
notes={31:'Every Example21 response, its sketch, the orientation pair and checklist recorded. Its source nonzero leading coefficient is explicit.',32:'Both independently numbered Try21 questions, Example22 and all twelve Try22 outputs recorded; two reference/callout records retained.',33:'Every Example23 and both Try23 tasks recorded, including each sketch. Native source clears the apparent Example23 vertex-sign lead; the notation collision is distinguished.',34:'Example24 and all four Try24 sketches recorded. Vertex formula, two-method block and the no-crossing graph have teaching records.',35:'Every Example25/26 and both Try25 outputs recorded. Both reconstruction forms and their given graphs have records, with redundant data checked.'}
pages=[]
for page in range(31,36):
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 pages.append({'pdf_page':page,'printed_page':page-11,'chapter':1,'page_status':'items enumerated','item_ids':ids,'continuation_item_ids':[],
 'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-19','non_item_content':notes[page],
 'scope_screen':'All completion/extrema/sketch/reconstruction content accounted for. Direct assessed fields follow requested outputs; graph data-reading is distinct from producing a sketch.'})
if __name__=='__main__':
 for name,data in [('answers-YM-C1-quadratic-graphs.json',{'scope':'Every31–35source response and labelled sketch feature.','items':answers}),('census-YM-C1-quadratic-graphs.json',{'book':'YM','book_id':'8227-SRC-017','chapter':1,'source_path':SRC,'source_sha256':SHA,'scope':'Complete31–35page census.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if p['operation']['kind']!='polynomial-sketch':assert equivalent(compute(p['operation']),expression(p['printed_key_normalised'])),(row['item_id'],p['subpart'])
   for c in p.get('additional_comparisons',[]):assert equivalent(compute(c['operation']),expression(c['printed_key_normalised'])),(row['item_id'],p['subpart'],'feature')
   for n,op in p.get('additional_operations',{}).items():
    if n in p.get('additional_operation_expected',{}):assert equivalent(compute(op),expression(p['additional_operation_expected'][n])),(row['item_id'],p['subpart'],n)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'figures;',len(pages),'pages')
