"""YM441: original exercise expressions, branch omissions and plotted-root key typo."""
import hashlib,json,math
from author_YM_C9_log_laws import law
from author_YM_C9_log_equations import solution
import author_YM_C9_opening as g
from author_YM_C9_opening import h,W,SRC,SHA,pp,v,fig,figures,extra,compute,expression,equivalent
from author_YM_C4_trig_graphs import reasoning
g.answers.clear();g.new.clear();g.corrections.clear();figures.clear()
answers=g.answers;new=g.new;corrections=g.corrections
LOG=g.LOG;EXP=g.EXP;LAW='8227:2020:M2:T2:O01:D02';GRAPH='8227:2020:M2:T2:O02:D02';INV='8227:2020:M1:T3:O03:D02'
def ev(page):
 name='YM-C9-key-641'if page>=641 else'YM-C9-key-637'if page>=637 else f'YM-C9-{408+4*((page-408)//4)}-source'
 p=W/f'checks/r5/textbooks/{name}.png';return dict(path=str(p.relative_to(W.parents[2])),sha256=hashlib.sha256(p.read_bytes()).hexdigest())
h.common.base.ev=ev

def add(n,note,parts):
 r=g.add('Exercise-9',n,441,note,parts);r.update(component_demand_ids=sorted({d for p in parts for d in p.get('component_demand_ids',[])}-set(r['assessed_8227_demand_ids'])),representation='text',sketch_response_required=any(p.get('response_format')=='sketch'for p in parts),mapping_rationale='Classify each original requested log-law,notation,exponential solve,inverse or graph output directly. Preserve original argument domains. An internal CAS logarithm ratio is an oracle,not an imposed learner change-of-base method. Power substitutions must retain positive exponential values.',scope_check=dict(status='in-scope',basis=note,excluded_or_qualified_parts=[],limits_considered=['8227:LIMIT06','8227:QUAL08']),value_level_scope_decisions=[dict(rule_id='8227:LIMIT06',status='within',quoted_value=note,reason='No learner change-of-base formula is required;solve using the stated log/exponential rules or graph.'),dict(rule_id='8227:QUAL08',status='within'if n==6 else'not applicable',quoted_value=note,reason='AtQ6(a)the original full-domain function is not one-to-one;the conditional positive inverse branch is recorded without silently restricting the source. Other items do not request an inverse branch restriction.'if n==6 else'No inverse is requested in this item.')],precision_angle_check=dict(source='Q5explicitly3sf. Q8asks an approximate graphical root without precision. Other algebraic outputs exact unless a later item says otherwise.',comparison='No angles. Keep original domains and full real branch restrictions;do not impose2dp/3sf where not asked. Approximate source graph is compared by mathematical features and original equation,not pixel coincidence.'))
 return r
ps=[law('a','log(5*a)/log(10)','(log(5)+log(b))/log(10)',640,domain='Originala>0;printedunrelatedbdoesnotbelongtothisexpression.'),law('b','log((a*b)**2)/log(10)','(2*log(a)+2*log(b))/log(10)',640,domain='Originalab≠0;printedpositive-factorbranchusesa>0,b>0. Full-domain expansion2log|a|+2log|b|.'),law('c','log((x*y*t)**Rational(1,3))/log(10)','(log(x)+log(y)+log(t))/(3*log(10))',640,domain='Checkersymboltdenotessourcez. Originalxyz>0;printedseparate-logbranchusespositiveindividualfactors.')]
ps[0]['author_expected_normalised']='(log(5)+log(a))/log(10)'
ps[1]['full_original_domain_answer']='2log|a|+2log|b|fornonzeroa,b.';ps[2]['source_symbol_basis']={'t':'originalz'}
add(1,'Expand log(5a),log((ab)^2),log(cuberoot(xyz)). SourceQ1(a)keychangesatounrelatedb;correctloga. Positive-factor conventions for the other expansions stay explicit.',ps)
add(2,'Compress three source sums into one logarithm. The base3constant+1becomeslog_3(3),so part(c)hasnumerator3a^4anddenominatorb^20.',[law('a','(log(3)-log(8))/log(10)','log(Rational(3,8))/log(10)',640,expand=False),law('b','4*(log(3)-log(8))/log(10)','log(Rational(3,8)**4)/log(10)',640,expand=False),law('c','(4*log(a)-20*log(b))/log(3)+1','log(3*a**4/b**20)/log(3)',640,'3',False,domain='Originala>0,b>0.')])
ps=[g.conversion('a','log_6(36)=2','6²=36',641,'Eq(6**2,36)'),g.conversion('b','log_14(1/196)=−2','14^(−2)=1/196',641,'Eq(Rational(14)**(-2),Rational(1,196))'),g.conversion('c','log_a(b)=4','a^4=b',641)]
add(3,'Convert three original logarithmic relations to exponential notation;retain positive nonunitbaseaandpositiveargumentbin the generic relation.',ps)
ps=[g.conversion('a','64^(1/2)=8','log_64(8)=1/2',641,'Eq(64**Rational(1,2),8)'),g.conversion('b','(1/12)^2=1/144','log_(1/12)(1/144)=2',641,'Eq(Rational(1,12)**2,Rational(1,144))')]
ps.append(g.conversion('c','a^(−14)=b','log_a(b)=−14',641))
ps[-1]['source_reading_resolution']='Native source and key both print exponent−14,not−1/4. The apparent fractional-exponent defect from a small contact was CLEARED before registering any defect.'
add(4,'Convert64^(1/2)=8,(1/12)^2=1/144,anda^(−14)=b. Native source andkeyagree−14;do not invent a lost fractional bar from the small preview.',ps)
def rounded(label,expr,key):
 p=v(label,expr,key,641,'Solve the ORIGINAL positive-base exponential equation,retain any positive intermediate root,then apply logarithms and round once to the explicitly requested3sf. Negative roots of an auxiliary quadratic cannot equal a positive exponential.');p['operation']={'kind':'rounded','operands':[expr],'significant_figures':3};p.update(assessed_8227_demand_ids=[EXP],response_format='numeric');return p
ps=[rounded('a','log(Rational(26,5))/(6*log(18))','Rational(951,10000)'),rounded('b','-log(58)/(5*log(8))','-Rational(391,1000)'),rounded('c','log(5)/log(3)','Rational(146,100)')]
ps[1]['original_equation']='8^(−5x)−5=53;the native exponenthasanOUTSIDEnegative−5x.'
ps[2]['original_equation']='9^x+5(3^x−10)=0';extra(ps[2],'auxiliary-factorisation','expand((x-5)*(x+10))','x**2+5*x-50')
add(5,'Solve three original exponential equations to3sf. Native(b)exponentis−5x;in(c),substitutionu=3^xgives(u−5)(u+10)=0andonlypositiveu5isadmissible.',ps)
p=reasoning('a','The source positive-branch inverse is3^(x/4),but no single inverse exists on the original full domainx≠0.','Originalf(x)=log_3(x^4) is even on its full real domainofnonzero real inputs:f(1)=f(−1)=0. The source states no positive-input restriction. Restrictingtox>0givesinverse3^(x/4);restrictingtox<0gives−3^(x/4). The printed positive root needs its original-domain branch stated.',641,'key incomplete');p.update(assessed_8227_demand_ids=[INV],response_format='symbolic',original_domain='Allnonzeroreals;no sourcepositivityrestriction.',source_key='y=fourthroot(3^x)');extra(p,'actual-noninjection','Tuple(log(1**4),log((-1)**4))','Tuple(0,0)')
q=v('b','solve(log(y)/log(6)+5-x,y)[0]','6**(x-5)',641,'Swap ORIGINAL input/output inlog_6x+5and solve. Originalx>0rangeR givesinverseinputR,rangepositive.');q.update(assessed_8227_demand_ids=[INV],response_format='symbolic')
r=v('c','solve(5**(y/3)-x,y)[0]','log(x**3)/log(5)',641,'Native ORIGINALfunctionis5^(x/3),not5^((x−1)/3). Swapandsolve:inverse3log_5x=log_5(x³),withinverseinputx>0.');r.update(assessed_8227_demand_ids=[INV],response_format='symbolic',original_domain='OriginalinputR;inverseinputx>0.')
# Normalise only on the explicitly positive inverse-input branch.
r['operation']={'kind':'identity','operands':['expand_log(solve(5**(y/3)-x,y)[0],force=True)']};r['printed_key_normalised']='3*log(x)/log(5)'
add(6,'Find inverses oflog_3(x^4),log_6x+5,and5^(x/3). The first needs a domain branch absent from the source;the other originalfunctionsarealreadyone-to-one.',[p,q,r])
def graph(label,answer,proof):
 p=reasoning(label,answer,proof,641,'sketch');p.update(assessed_8227_demand_ids=[GRAPH],response_format='sketch',credited_features=answer.split(';'),criteria_basis='Author-derived exact original-function features checked on printed key,not official marking rows.');return p
p=graph('negative-exponential','y=−3^x;domainR;range(−∞,0);y-intercept(0,−1);horizontalasymptotey0;strictlydecreasing;nox-intercept','The outside minus reflects3^xinthe x-axis. Its valueisnegativeforallrealinput,including−1at0. The source sketch has the correct curve andlabel.');extra(p,'original-exp-axis-point','-3**0','-1')
q=graph('negative-logarithm','y=−log_3x;domainx>0;rangeR;x-intercept(1,0);verticalasymptotex0;strictlydecreasing;noy-intercept','The outside minus changes the logarithm output,not the positive-input domain. Its limitat0+is+∞andat∞is−∞. Source sketch agrees.');extra(q,'original-log-axis-point','-log(1)/log(3)','0')
add(7,'Sketch the two ORIGINAL output-negated curves−3^xand−log_3x. Keep their very different domains,asymptotesandintercepts;negativeoutputsdo not implynegativeinputs.',[p,q])
p=graph('exponential-on-stated-interval','Plot e^x on0≤x≤1 atx0,.5,1;points(0,1),(.5,√e),(1,e);includeclosedendpoints','Use the stated0..1interval and0.5step. The key draws a broader mathematicallyvalidcurve;itsunrequestedextensiondoesnotredefine the learner’s original domain.');extra(p,'original-required-table','Tuple(exp(0),exp(Rational(1,2)),exp(1))','Tuple(1,sqrt(E),E)')
q=graph('suitable-straight-line','Liney=5−5x;sharedaxeswiththeexponential;intercept(0,5);zero(1,0);intersectionnear(.626,1.87)','Rewrite the ORIGINAL equation as intersection ofe^xand5−5x. The printed graph visually intersects nearx.63,not the caption1.8. The root lies inside the requested0..1interval.')
lo,hi=0.,1.
for _ in range(80):
 mid=(lo+hi)/2
 if math.exp(mid)+5*mid-5>0:hi=mid
 else:lo=mid
assert .62598<mid<.62599
r=reasoning('approximate-root','x≈0.626,or about0.63by a reasonable graph reading.','Independent standard-library bisection ofh(x)=exp(x)+5x−5on[0,1]gives0.6259832407. h′=exp(x)+5>0ensuresuniqueness;h(0)<0,h(1)>0. The native printedcaptionx≈1.8contradicts both the equation and its own graph. No officialgraphreading toleranceis supplied.',641,'key wrong');r.update(assessed_8227_demand_ids=[EXP],component_demand_ids=[GRAPH],response_format='numeric',printed_key_display='x≈1.8',independent_bisection_result=mid);extra(r,'key-root-positive-residual','exp(Rational(18,10))+5*Rational(18,10)-5>0','True')
add(8,'Plot e^xon0..1withstep0.5,addline5−5x,andreadtheroot. Correctx≈0.626;nativekeycaption1.8iswrongalthoughitsdrawnintersectionisnear.63.',[p,q,r])
ps=[solution('a','2*x-10*(x-3)','Interval.open(3,oo)','FiniteSet(Rational(15,4))',641,'log(2x)−log(x−3)=1'),solution('b','x**2+12*x-3-10*x**2','Interval.open(0,oo)','FiniteSet(Rational(1,3),1)',641,'log(x²+12x−3)=1+2logx'),solution('c','4*(x+2)**2-81*x','Interval.open(0,oo)','FiniteSet(Rational(1,4),16)',641,'2log(x+2)+log4=logx+4log3')]
add(9,'Solve three original base10logequations andfilterallargumentdomains. The rationalroots15/4,{1/3,1},{1/4,16}all satisfytheiroriginaldomains.',ps)
p=rounded('x','log(6)/log(2)','Rational(258,100)');p['requested_precision']='Noexplicitprecisioninthequestion;3sfusedonlytomatchtheprinted2.58display.';p.update(original_equation='2^(x+2)−3=7×2^(x−1)',required_method='Substitutiony=2^x;solve4y−3=(7/2)y,theny6>0andx=log_2(6).');extra(p,'original-substitution-root','4*6-3-Rational(7,2)*6','0')
add(10,'Use the explicitly requested substitutiony=2^xin2^(x+2)−3=7×2^(x−1). The linear auxiliary rooty6givesxlog_2(6),printed2.58.',[p])
fig(107,441,'Negative logarithm input/output warning','The source note correctly distinguishes no real logarithm ofnegativeinputfroma permitted negative logarithm output. Alsoexcludezeroargument. This teaches Q7but isnot an extra asked sketch.',[GRAPH],'table',[],'Exercise-9:7');figures[-1].update(item_id='8227:TB:YM:C9:Teaching-figure:107',printed_page=pp(441),source_evidence=ev(441),value_level_scope_decisions=[],item_kind='teaching-figure',parent_item_id='8227:TB:YM:C9:Exercise-9:7');figures[-1]['mathematical_feature_review']['method']='Read original note and compare both actual reflected function domains/intercepts independently.'
pages=[dict(pdf_page=441,printed_page=pp(441),chapter=9,page_status='items enumerated',item_ids=[r['item_id']for r in answers]+[r['item_id']for r in figures],continuation_item_ids=[],source_evidence=ev(441),reader='Codex author',date='2026-11-20',non_item_content='AllExercise9Q1–10,alltheirassessedoutputsandthelog-domainnotepanelenumerated. Actual nativeexponents−5xandx/3retained.',scope_screen='Originalfunctionbranchandsourcedomainambiguityexplicit;internalchange-of-baseoracleisnotrequiredlearnermethod.')]
def save():
 for name,data in [('answers-YM-C9-exercise-basic.json',dict(scope='Complete441exerciseQ1–10,including actualsourceexponentsandkeydefects.',items=answers)),('census-YM-C9-exercise-basic.json',dict(book='YM',book_id='8227-SRC-017',chapter=9,source_path=SRC,source_sha256=SHA,scope='Complete441page/item/referencecensus.',new_items=new+figures,corrections=corrections,pages=pages))]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for r in answers:
  for p in r['subparts']:
   if'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(r['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():
    if name in p.get('additional_operation_expected',{}):assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(r['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
if __name__=='__main__':save()
