"""Source-only272–279audit: retain ordinary vector facets inside extra line methods."""
import hashlib,json
import author_Goldie_C8_opening as base
from author_Goldie_C10_opening import W,SRC,SHA,ev,v,reasoning,fig,figures,compute,expression,equivalent,ADD,GEOM,DISP,POS,MAG

base.ev=ev;base.answers.clear();base.new.clear();figures.clear()
answers=base.answers;new=base.new
SCALE='8227:2020:M1:T7:O02:D02'

def add(kind,n,page,note,parts,direct,components=None,rep='text',continuation=None,excluded=None):
    row=base.add(kind,n,page,note,parts,direct,components,rep=rep,continuation=continuation)
    row['item_id']=row['item_id'].replace(':C8:',':C10:')
    new[-1]['item_id']=row['item_id']
    row['value_level_scope_decisions']=[]
    row['mapping_rationale']='Retain the original requested position,displacement,magnitude or geometric scaling result. A supplied vector sum may be evaluated without requiring construction or classification of vector line equations. No separate prescribed line-equation objective is invented.'
    row['scope_check']={'status':'in-scope-parts-only'if excluded else'in-scope','basis':note,'excluded_or_qualified_parts':excluded or[],
      'limits_considered':[],'qualifier_applicability_note':'No QUAL01–11orLIMIT01–08specific algebra/calculus restriction applies to these fixed vector calculations. The actual M1:T7scope boundary is stated part by part.'}
    row['precision_angle_check']={'source':'Exact signed components,midpoints and ratios. No angle or rounding instruction applies to these retained outputs.',
      'comparison':'Keep signed displacements distinct from nonnegative lengths. A point on a line need not lie between its endpoints;only an explicit segment/internal condition removes external division.'}
    new[-1].update(scope_check=row['scope_check'],value_level_scope_decisions=[],mapping_rationale=row['mapping_rationale'])
    return row

p=v('vector-identity','expand(a+q*(b-a)-((1-q)*a+q*b))','0',358,
 'Substitute AB=OB−OA into the given OP=OA+λABand distribute the scalar. Both expressions agree componentwise for every realλ;the word fraction doesnot itself impose0<λ<1.')
p['check_mode']='show/prove'
add('Prompt',7,273,'Given OP=OA+λAB,show OP=(1−λ)OA+λOB. This is an addition/scaling identity from an explicitly supplied relation,not a request to derive the equation of an arbitrary line.',[p],[ADD,SCALE],[POS])

parts=[]
p=v('i-lambda2','Tuple(2+2*2,-1+2*4)','Tuple(6,7)',274,
 'Evaluate the supplied linear combination atλ=2. The vector arithmetic gives(6,7),beyondB;no formal vector-line-equation construction is required.');p['check_mode']='show/prove';parts.append(p)
for label,q,key in [('minus2','-2','Tuple(-2,-9)'),('minus1','-1','Tuple(0,-5)'),('zero','0','Tuple(2,-1)'),('half','Rational(1,2)','Tuple(3,1)'),('three-quarters','Rational(3,4)','Tuple(Rational(7,2),2)'),('one','1','Tuple(4,3)'),('three','3','Tuple(8,11)')]:
    parts.append(v('ii-'+label,f'Tuple(2+({q})*2,-1+({q})*4)',key,358,
      'Substitute the individually stated parameter into the original supplied position vector(2,−1)+λ(2,4). All seven values are verified on the native source crop;the native answer crop includes theλ=1point(4,3).'))
p=reasoning('iii-plotted-points','Plot(−2,−9),(0,−5),(2,−1),(3,1),(7/2,2),(4,3),(8,11);they lie on y=2x−5andthe extended line throughA(2,−1),B(4,3).',
 'Each source position hasx=2+2λ,y=−1+4λ,so y−2x+5=0. On consistently scaled perpendicular axes all seven points are collinear withAandB. The source Figure10.23showsA,Bandthe same direction;the response must extend far enough to include all requested positions,not just the figure viewport.',275,'sketch')
p['additional_operations']={'collinearity':{'kind':'identity','operands':['expand((-1+4*q)-2*(2+2*q)+5)']}};p['additional_operation_expected']={'collinearity':'0'};parts.append(p)
for label,coordinate,key in [('A',['2','-1'],'0'),('B',['4','3'],'1'),('M',['3','1'],'Rational(1,2)'),('N',['Rational(7,2)','2'],'Rational(3,4)')]:
    p=v('iv-'+label,f'({coordinate[0]}-2)/2',key,358,
      'Use the xcomponent of the source position and then confirm its ycomponent with the same parameter. The nonzero source xdirection component2allows this division;it is not a general assumption for all vector directions.')
    p['additional_operations']={'second_coordinate':{'kind':'identity','operands':[f'-1+4*(({coordinate[0]}-2)/2)-({coordinate[1]})']}};p['additional_operation_expected']={'second_coordinate':'0'};parts.append(p)
for label,conclusion,why in [('a','BetweenAandB.','For0<λ<1,the position is a strict convex combination(1−λ)A+λB.'),('b','BeyondBfromA.','λ>1adds more than the fullA-to-Bdisplacement.'),('c','BeyondAawayfromB.','λ<0reverses the nonzeroA-to-Bdisplacement fromA.')]:
    parts.append(reasoning('v-'+label,conclusion,why,358,'matches'))
row=add('Activity',2,274,'Activity10.2evaluates a supplied position-vector sum atλ=2andseven further signed/fractional values,plots all points,identifies four named positions,andinterprets three parameter intervals geometrically.',parts,[POS,GEOM],[ADD,SCALE],rep='graph',continuation=[275],
 excluded=['The concluding interpretation of the supplied expression as a general vector equation of a line is additional;the retained arithmetic,plotting and signed-scalar position decisions are prescribed vector facets.'])
row['sketch_response_required']=True;new[-1]['sketch_response_required']=True

p=reasoning('iii-all-ratio-points','N=(−1,13/4,3/2)orN=(−4,11/2,0). The source gives only the first.',
 'AB=(4,−3,2),withnonzero norm√29. Write AN=λABas geometric collinearity,so lengths give3|λ|=|1−λ|. Squaring is safe because both sides are nonnegative:9λ²=(1−λ)²has exactlyλ=1/4and−1/2. Addition fromA=(−2,4,1)gives the internal and external points. Direct substitution verifies3|AN|=|NB|inbothcases. The actual question says line,not segment,so neither may be omitted.',278,'key incomplete')
p['printed_key_text']='N=(−1,3.25,1.5);the worked text asserts N must lie one quarter of the way along AB.'
p['additional_operations']={
 'all_ratio_multipliers':{'kind':'identity','operands':['FiniteSet(*solve(9*q**2-(1-q)**2,q))']},
 'internal_point':{'kind':'identity','operands':['Tuple(-2+Rational(1,4)*(2-(-2)),4+Rational(1,4)*(1-4),1+Rational(1,4)*(3-1))']},
 'external_point':{'kind':'identity','operands':['Tuple(-2-Rational(1,2)*(2-(-2)),4-Rational(1,2)*(1-4),1-Rational(1,2)*(3-1))']},
 'external_original_ratio':{'kind':'identity','operands':['3*sqrt((-4-(-2))**2+(Rational(11,2)-4)**2+(0-1)**2)-sqrt((2-(-4))**2+(1-Rational(11,2))**2+(3-0)**2)']}}
p['additional_operation_expected']={'all_ratio_multipliers':'FiniteSet(-Rational(1,2),Rational(1,4))','internal_point':'Tuple(-1,Rational(13,4),Rational(3,2))','external_point':'Tuple(-4,Rational(11,2),0)','external_original_ratio':'0'}
add('Example',12,277,'ForA(−2,4,1),B(2,1,3),retain(iii):find every pointNonthelinewith3|AN|=|NB|. The worked solution omits the external point. Earlier(i)line-equation construction and(ii)membership in that formal equation are additional.',[p],[POS,GEOM],[DISP,MAG],continuation=[278],
 excluded=['Parts(i)/(ii)require vector line-equation construction/use,not a prescribed8227representation. Part(iii)is independently solvable by vector scaling and geometric ratio.'])

parts=[]
for label,a,b,ab,mag,mid in [
 ('i',[2,3],[4,11],'Tuple(2,8)','sqrt(68)','Tuple(3,7)'),
 ('ii',[4,3],[0,0],'Tuple(-4,-3)','5','Tuple(2,Rational(3,2))'),
 ('iii',[-2,-1],[4,7],'Tuple(6,8)','10','Tuple(1,3)'),
 ('iv',[-3,4],[3,-4],'Tuple(6,-8)','10','Tuple(0,0)'),
 ('v',[-10,-8],[-5,4],'Tuple(5,12)','13','Tuple(-Rational(15,2),-2)')]:
    delta=[f'({y})-({x})'for x,y in zip(a,b)]
    p=v(label+'-a-AB','Tuple('+','.join(delta)+')',ab,358,'Compute destinationBminus originAfor the original ordered endpoints. Native source confirms the final pair hasB=(−5,+4).');p['source_arrow_tail']=a;p['source_arrow_head']=b;parts.append(p)
    p=v(label+'-b-length','sqrt('+'+'.join(f'({d})**2'for d in delta)+')',mag,358,'Square the actual signed differences before summing and taking the nonnegative root.');p['source_vector_components']=[str(y-x)for x,y in zip(a,b)];p['source_vector_output']='magnitude';parts.append(p)
    parts.append(v(label+'-c-midpoint','Tuple('+','.join(f'(({x})+({y}))/2'for x,y in zip(a,b))+')',mid,358,'Average corresponding endpoint coordinates;the midpoint is a position vector relative to the same origin.'))
add('Exercise-10D',1,278,'For five ordered2Dendpoint pairs,findAB,its exact magnitude,andthe midpoint position vector. All15original outputs are prescribed despite their placement in the vector-line section.',parts,[DISP,MAG,POS],[ADD])
p=v('ii-midpoint','Tuple((-1+(-3))/2,(-2+4)/2,(1+(-5))/2)','Tuple(-2,1,-2)',358,
 'AverageA=(−1,−2,1)andB=(−3,4,−5)componentwise. This independently asked midpoint doesnot require the line equation from(i).')
add('Exercise-10D',5,279,'FromA(−1,−2,1),B(−3,4,−5),C(0,−2,4),retain(ii):the midpointMofAB. Parts(i)/(iii)ask vector line equations;the latter also gives an unsigned ratio onBC.',[p],[POS],[ADD],
 excluded=['Part(i)constructs the lineAB;part(iii)constructs a lineMNandis outside prescribed vector-equation methods. Its wording doesnot explicitly placeNonthesegment;the source’s internal-only choice is a boundary lead,not a verified retained response.'])

for n,page,label,note,teaches,rep,checks,parent in [
 (50,272,'Figure10.22 joining vector and subdivision grid','A=(2,−1),B=(4,3),AB=(2,4),|AB|=√20,M=(3,1),N=(7/2,2). These named positions share one coordinate model;the grid’s viewport is not the full extended line.',[DISP,POS,MAG],'graph',[('Tuple(4-2,3-(-1))','Tuple(2,4)'),('sqrt((4-2)**2+(3-(-1))**2)','sqrt(20)'),('Tuple(2+Rational(3,4)*(4-2),-1+Rational(3,4)*(3-(-1)))','Tuple(Rational(7,2),2)')],None),
 (51,275,'Figure10.23 signed vector route','The three stages areOtoA(2,−1),thenλsteps ofAB=(2,4). λ0and1locateAandB;fractionalpositive values interpolate;negative values reverse the direction. The source also interprets the supplied expression as a line equation,which is additional formal representation.',[ADD,SCALE,GEOM,POS],'graph',[],'Activity:2'),
 (52,276,'Direction and location convention reference','Scalar multiples of(1,2),including(−5,−10),generate the same unoriented line. A negative multiple reverses the directed vector;it doesnot have the same directed orientation. Equivalent bases shift parameter values without changing the set of line points. This is boundary explanation,not a new assessed line-equation skill.',[SCALE,GEOM],'table',[('Tuple(-5,-10)','Tuple(-5*1,-5*2)')],None)]:
    fig(n,page,label,note,teaches,rep,checks,parent)
for f in figures:
    f['item_id']=f['item_id'].replace(':C5:',':C10:');f['parent_item_id']=f['parent_item_id'].replace(':C5:',':C10:')if f['parent_item_id']else None
    f['source_evidence']=ev(f['pdf_page']);f['value_level_scope_decisions']=[]

notes={272:'10C12andfigure49are linked here. Figure10.22andthe joining/ratio calculations are retained as teaching evidence before the formal line-equation section.',
 273:'Joining-vector/norm/midpoint/three-quarter exposition belongs toFigure10.22. The unnumbered algebraic rewrite isPrompt7. No unasked numeric illustration is counted as a new response.',
 274:'EveryActivity10.2subpart is recorded,including allseven(ii)parameters. The final whole-line interpretation remains additional representation.',
 275:'Figure10.23andall signed-scalar position cases are recorded;formal line-equation nonuniqueness/direction discussion remains boundary explanation.',
 276:'Line-equation reparameterisation/location/nonuniqueness and general vector-line form are additional exposition. The scalar-sign/direction caution is retained infigure52. No separately asked task starts.',
 277:'Activity10.3asks five vector-line plots/comparisons andis excluded as original formal-line-equation practice. Its answer graph on358was read. Example12retains only the independent unsigned-ratio task;the source/key defect is explicit.',
 278:'Example12continues;all15outputs of10D1are retained.10D2(i–viii)asks vector equations andis additional. Exact key page358was read.',
 279:'10D3(i–v)asks vector equations;10D4(i–v)tests membership in formal parametric vector lines;both remain additional.10D5retains the independent midpoint only. The headingless pen/pencil activity asks parallel/intersecting/skew3Dlines andis additional;it is not missed by the census.'}
pages=[]
for page in range(272,280):
    ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
    if page==272:ids+=['8227:TB:Goldie:C10:Exercise-10C:12','8227:TB:Goldie:C10:Teaching-figure:49']
    continuation=['8227:TB:Goldie:C10:Activity:2']if page==275 else['8227:TB:Goldie:C10:Example:12']if page==278 else[]
    pages.append({'pdf_page':page,'printed_page':page-14,'chapter':10,'page_status':'items enumerated','item_ids':ids,'continuation_item_ids':continuation,
      'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-18','non_item_content':notes[page],
      'scope_screen':'Rendered-page read with item/part-level retention of prescribed vector facets. Original formal vector-line-equation tasks remain additional,with reasons;no whole-section blanket exclusion.'})

if __name__=='__main__':
    for name,data in [('answers-Goldie-C10-line-opening.json',{'scope':'Every retained272–279response;formal vector-line-equation tasks explicitly screened.','items':answers}),
      ('census-Goldie-C10-line-opening.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':10,'source_path':SRC,'source_sha256':SHA,'scope':'Complete272–279page/item boundary census,including inherited10C12andfigure49.','new_items':new+figures,'corrections':[],'pages':pages})]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    for r in answers:
        for p in r['subparts']:
            if 'operation'in p:assert equivalent(compute(p['operation']),expression(p['printed_key_normalised'])),(r['item_id'],p['subpart'])
            for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(r['item_id'],p['subpart'],name)
    print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures')
