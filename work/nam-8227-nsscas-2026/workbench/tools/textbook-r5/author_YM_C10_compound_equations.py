"""YM460–461: full bounded compound-angle roots and original denominator checks."""
import json
from author_YM_C4_composite_equations import roots
import author_YM_C10_opening as o
import author_YM_C10_compound_sine as s
import author_YM_C9_opening as g
from author_YM_C9_opening import h,W,SRC,SHA,pp,v,fig,figures,extra,compute,expression,equivalent
from author_YM_C4_trig_graphs import reasoning
g.answers.clear();g.new.clear();g.corrections.clear();figures.clear()
answers=g.answers;new=g.new;corrections=g.corrections;ev=o.ev;h.common.base.ev=ev
COMP=o.COMPOUND;EVAL=o.EXACT;BND='8227:2020:M1:T6:O06:D01';ALL='8227:2020:M1:T6:O06:D02';RECIP=o.RECIP;D='(x*pi/180)'
def exact(label,expr,key,kp,direct,method,show=False):
 p=v(label,expr,key,kp,method);p.update(assessed_8227_demand_ids=direct,response_format='proof/show-that'if show else'symbolic')
 if show:p['check_mode']='show/prove'
 return p

def bounded(label,original,key,kp,branches,lo='0',hi='360',opened=False):
 p=roots(label,original,key,kp,branches,lo=lo,hi=hi,approx=True,opened=opened);p.update(assessed_8227_demand_ids=[COMP,EVAL,BND,ALL],response_format='numeric',original_equation_zero_form=original,method='Expand/transform the ORIGINAL compound-angle equation and preserve every original denominator restriction. Solve all admissible branches on the ORIGINAL finite degree interval,then substitute each root into the ORIGINAL expression. Derive the full exact root set before comparing separately transcribed source approximations;do not manufacture missing roots from a tangent-only rule.')
 return p

def add(kind,n,page,note,parts):
 r=o.add(kind,n,page,note,parts);r.update(mapping_rationale='The explicit show/reduce output and complete bounded roots are distinct assessed outputs. The original compound angle and every tangent/secant pole remain in the oracle. A forced hence method preserves the linked earlier result;an incidental quadratic is a component rather than separate full polynomial coverage.',value_level_scope_decisions=[dict(rule_id='8227:QUAL03',status='within',quoted_value=note,reason='Actualangleargumentshavemultiplier±1andfixed30/45/60/120degreeshifts. Squaredratiosare not doubled input multipliers.'),dict(rule_id='8227:LIMIT02',status='within',quoted_value=note,reason='Everyrequestedsolutionintervalisfinite;no generalperiodicsolutionfamilyisasked.')],scope_check=dict(status='in-scope',basis=note,excluded_or_qualified_parts=[],limits_considered=['8227:QUAL03','8227:LIMIT02']),precision_angle_check=dict(source='Allbounds/anglesinthissegmentaredegrees. Sourcefiniteanglekeysdisplay1decimalplace;parameter/exactoutputsremainunrounded.',comparison='Keep full inverse-angle precision and all exact branches before comparing each printed approximation. Original poles/endpoints cannot be added by denominatorclearing. No unasked general solution forms.'))
 return r
p=exact('a-k','sin(pi/3)/(2+cos(pi/3))','sqrt(3)/5',460,[COMP,EVAL],'Expand ORIGINALsin(60°−x)=2sinx. Itscoefficientsgivesin60cosx=(2+cos60)sinx. A hypotheticalcosx0doesNOTsatisfytheoriginal,so legitimate division gives tanx=sin60/(2+cos60)=√3/5. Showtheequationreduction,notonlytheconstant.',True)
q=bounded('b-roots',f'sin(pi/3-{D})-2*sin({D})',['19.1','199.1'],460,[('tan','x','sqrt(3)/5',1)],opened=True);q['depends_on_source_parts']=['a-k']
add('Example',11,460,'Show originalsin(60°−x)=2sinxreduces totanx√3/5,thenHENCEsolveonSTRICT0<x<360degrees. Two actualroots19.1and199.1.',[p,q])
ps=[bounded('a',f'cos({D}-pi/3)-3*cos({D})',['70.9','-109.1'],643,[('tan','x','5/sqrt(3)',1)],lo='-180',hi='180'),bounded('b',f'sin(pi/6-{D})-4*sin({D})',['5.9','-174.1'],643,[('tan','x','1/(8+sqrt(3))',1)],lo='-180',hi='180')]
add('Try-Now-11',1,460,'Two originalcompound equationsonCLOSED−180..180degrees:cos(x−60)=3cosxandsin(30−x)=4sinx. Retainthenegativecoterminalrootineachpair.',ps)
p=s.proof('a-identity','sin(x+pi/3)+sin(x+2*pi/3)','sqrt(3)*cos(x)',643,'Allrealθ;checkerxistheradianformoforiginaldegreeθ.','Expand both ORIGINALsine sums. The sinθcoefficients cos60+cos120cancel;cosθcoefficientssin60+sin120addto√3.')
q=exact('b-i-exact-sum','sin(105*pi/180)+sin(165*pi/180)','sqrt(Rational(3,2))',643,[COMP,EVAL],'Use ORIGINAL hence identityatθ45degrees. The exactsumis√3cos45=√6/2=√(3/2);do not approximate each original sine separately.');q['depends_on_source_parts']=['a-identity']
r=bounded('b-ii-roots',f'sin({D}+pi/3)+sin({D}+2*pi/3)-sec({D})',['40.6','139.4'],643,[('cos','x','1/sqrt(3)',2)],hi='180');r.update(depends_on_source_parts=['a-identity'],component_demand_ids=[RECIP],original_domain='0≤θ≤180degrees,excluding90wheresecundefined.')
add('Try-Now-11',2,460,'Prove thesine-sumidentity,thenHENCEfindexactsum105°/165°andsolveitsoriginalsecantequationon0..180degrees. Clearingcosθdoesnotadmit90degrees.',[p,q,r])
p=exact('a-tan-B','solve((t+x)/(1-t*x)-4,x)[0]','(4-t)/(1+4*t)',461,[COMP,EVAL],'From ORIGINALtanA=t,tan(A+B)=4,thecompoundformula gives t+tanB=4(1−t tanB). Solve forfinite tanB. The source result has a real parameter pole:ift=−1/4,tanB is undefined rather than a finite number. Retain1+4t≠0andtheoriginalcompounddenominator.');p.update(original_constraints='tanA=tfinite,tan(A+B)=4finite;requestedtanBfiniteonlywhent≠−1/4.',response_format='symbolic')
q=bounded('b-roots',f'2*tan(pi/4-{D})-3*tan({D})',['18.4','116.6','198.4','296.6'],461,[('tan','x','1/3',1),('tan','x','-2',1)]);q['original_domain']='0≤x≤360degrees,excludingtanxpoles90/270andtan(45−x)poles135/315.'
add('Example',12,461,'Parametercompoundtangentrecoveryandaseparateoriginalequation2tan(45−x)=3tanxon0..360degrees. Allfourrootssurviveoriginalpoles;parameterpole t−1/4explicit.',[p,q])
p=s.proof('a-reduced-quadratic','-(tan(pi/4+x)-4*tan(pi/4-x))*(1-tan(x))*(1+tan(x))','3*tan(x)**2-10*tan(x)+3',643,'Originaltan(π/4+x)andtan(π/4−x)defined. On the requested0<x<90degreeinterval,x45isexcludedandtanxfinite;cleared1±tanxnonzero.','Expand ORIGINALshiftedtangents,collecttheiractualrationalresidual,andmultiplybynonzerooriginaldenominators. The residual’snegativeproduces3tan²x−10tanx+3. This is equation equivalence on that domain,not permissiontoadd45degrees.')
q=bounded('b-roots',f'tan(pi/4+{D})-4*tan(pi/4-{D})',['18.4','71.6'],643,[('tan','x','1/3',1),('tan','x','3',1)],hi='90',opened=True);q.update(depends_on_source_parts=['a-reduced-quadratic'],original_domain='Strict0<x<90degrees,excluding45becausebothshiftedtangentshavepoles.')
add('Try-Now',12,461,'SHOW originaltan(45+x)=4tan(45−x)reducestothespecifiedquadratic;HENCEsolveonSTRICT0<x<90degrees. Both18.4and71.6arevalid;45isnot.',[p,q])
refs=[(51,460,'Example11 ORIGINAL compound-reduction working','Expandtheoriginalsin60−x,collectcoefficients,andcheckcosx0isnotasolutionbeforedividing.',COMP,'table','Example:11'),(52,460,'Example11 degree30/60 solution triangle','Exactsin60√3/2,cos60.5supplytheactualreductionconstant.',s.SPECIAL,'diagram','Example:11'),(53,460,'Example11 tangent-sign quadrant diagram','Positivek√3/5givesquadrantsIandIII,withopen0/360boundsretained.',ALL,'diagram','Example:11'),(54,461,'Example12 parameter-tangent working','Finite tanB=(4−t)/(1+4t);t−1/4ispole,notavalidfiniteformularesult.',COMP,'table','Example:12'),(55,461,'Example12 original-equation quadratic working','2(1−tanx)=3tanx(1+tanx);roots1/3and−2beforeallanglebranches.',COMP,'table','Example:12'),(56,461,'Example12 positive-tangent quadrant diagram','Tanx1/3gives18.4,198.4degreesinsideclosed0..360.',ALL,'diagram','Example:12'),(57,461,'Example12 negative-tangent quadrant diagram','Tanx−2gives116.6,296.6degrees;originalshiftedtangentpolesexcluded.',ALL,'diagram','Example:12')]
for n,page,label,note,d,rep,parent in refs:
 fig(n,page,label,note,[d],rep,[],parent);figures[-1].update(item_id=f'8227:TB:YM:C10:Teaching-figure:{n}',printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='teaching-figure',parent_item_id='8227:TB:YM:C10:'+parent);figures[-1]['mathematical_feature_review']['method']='Readactualfiniteintervals,allquadrantbranchesandoriginalshiftedtangentpoles. Recomputecompleteexactrootsetsbeforecomparingprinteddecimals;providedguideplotsareworkingsolutions,notextraquestiongivens.'
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=10,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-20',non_item_content='AllExamples11–12,Try11Q1–2/Try12andsevenactualworking/triangle/quadrantpanelsenumerated.',scope_screen='Originalsmallargumentmultipliers,finiteintervalsandpolespreserved. Sourceparameterexpressionrecordedonlywhereitsrequestedfinitevalueexists.')for page in[460,461]]
def save():
 for name,data in [('answers-YM-C10-compound-equations.json',dict(scope='Complete460–461originalcompoundequations,boundedrootsandparameterdomain.',items=answers)),('census-YM-C10-compound-equations.json',dict(book='YM',book_id='8227-SRC-017',chapter=10,source_path=SRC,source_sha256=SHA,scope='Complete460–461page/item/figurecensus.',new_items=new+figures,corrections=corrections,pages=pages))]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if'printed_key_normalised'in p:assert equivalent(compute(p['operation']),expression(p['printed_key_normalised'])),(row['item_id'],p['subpart'])
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
if __name__=='__main__':save()
