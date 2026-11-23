"""YM553: stationary output scope, common-log quadrature, asked sketch and volume."""
import json
import author_YM_C12_trig_powers as t
import author_YM_C12_trapezium_bias as b
import author_YM_C12_opening as a
from author_YM_C12_opening import h,W,SRC,SHA,pp,ev,fig,figures,extra,compute,expression,equivalent
from verify_textbook_answers_r5 import primitive_agrees
h.answers.clear();h.new.clear();h.corrections.clear();figures.clear();h.common.base.ev=ev
answers=h.answers;new=h.new;corrections=h.corrections
EXP=a.EXP;DEF=a.DEF;TRIG=t.TRIG;STAT=b.STAT;BIAS=b.BIAS;AREA='8227:2020:M1:T9:O04:D01';VOL='8227:2020:M1:T9:O04:D02';SKETCH='8227:2020:M2:T5:O04:D01'
def add(n,note,parts,rep='text'):
 r=a.add('Exercise-12',n,553,note,parts);r.update(representation=rep,sketch_response_required=any(p.get('response_format')=='sketch'for p in parts),mapping_rationale='Requestedstationaryabscissaandcoefficientareseparatefromunaskedordinates. ExplicitASKEDsketchinQ10directlyassessesintegrandgraph;othersareGIVEN. VolumeinQ11(b)usesx-axisrotationofactualsquaredordinate,notplanararea. Priorpart(a)integralcanbeusedbut(b)doesnotmandateHENCEroute. Q11(a)repeatsanearlieridentity/integralpart,notanewwholeproblemtype.',precision_angle_check=dict(source='Q9(b)log10quadrature3sf. Q10sketchexactequation/endpoints;keydisplays13.9atx2. Otheroutputsareexact,radians.',comparison='Retainpositiveoriginalcurvesandrequestedregionbounds. Noautomaticwholequestionduplicationfromasharedsubpart. Sketchfeaturesareauthorderivedandcomparedwithbook,notanofficialcriteriontable.'))
 if any(SKETCH in p.get('assessed_8227_demand_ids',[])or BIAS in p.get('assessed_8227_demand_ids',[])for p in parts):
  r['value_level_scope_decisions'].append(dict(rule_id='8227:QUAL11',status='within',quoted_value='Q10original4exp(x/2)+3on0≤x≤2.',reason='Simpleincreasingupward-bendingASKEDsketchandchord-overestimatejudgement. Formalpositivecurvatureisanindependentauthorcheck.'))
  r['scope_check']['limits_considered'].append('8227:QUAL11')
 return r
p=a.primitive('primitive','exp(-x)*(1+exp(x))','-exp(-x)+x',651)
add(7,'Indefiniteoriginale^(−x)(1+e^x)expands toe^(−x)+1,primitive−e^(−x)+x+C. Noidentitypower-reductionrequired.',[p])
f='4*exp(x/2)-6*x+3'
p=a.val('a-shown-M-x','solve(diff('+f+',x),x)[0]','log(9)',651,'Originalderivative2e^(x/2)−6vanishesonlywhen e^(x/2)=3,x2ln3=ln9. Onlyabscissaasked,notMordinate.',[STAT]);p.update(check_mode='show/prove',response_format='proof/show-that',given_representation='graph')
q=a.val('a-constant','exp(2*log(3))','9',651,'Fromindependentlyderivedstationaryx2ln3=ln9,identifyintegera9intheaskedformlna.',[STAT]);q.update(depends_on_source_parts=['a-shown-M-x'],given_representation='graph')
r=a.dv('b-exact-area',f,0,2,'8*exp(1)-14',651);r.update(assessed_8227_demand_ids=[AREA],component_demand_ids=[EXP,DEF],given_representation='graph',units='units^2',printed_key_units='units^2',original_positive_region='Theminimum15−12ln3ispositive;thereforethecurveabovexaxisthroughout[0,2].')
add(8,'GIVEN4e^(x/2)−6x+3andminimumM:(a)SHOWabscissalnaandidentifya9;(b)exactarea0..2is8e−14. Requestedln-formandpositivegeometricareaarepreserved.',[p,q,r],'graph')
p=a.dv('a-shown-integral','6/(2*x-7)',6,16,'log(125)',553);p.update(check_mode='show/prove',response_format='proof/show-that')
q=b.estimate('b-common-log-estimate','log(x)/log(10)',1,17,4,'Rational(27,2)',651,sf=3,rep='text');q.update(source_common_log_base=10,source_function='log_10(x)')
add(9,'(a)SHOW6..16reciprocalintegral6/(2x−7)=ln125,safeinterval;(b)REQUIREDfour-intervalestimateoflog10xon1..17to3sf13.5. Base10nodeevaluationisnotarequestedchange-of-basemethod.',[p,q])
f='4*exp(x/2)+3'
p=a.dv('a-shown-I',f,0,2,'8*exp(1)-2',553);p.update(check_mode='show/prove',response_format='proof/show-that')
q=a.reasoning('b-sketch','Positiveincreasingupward-bendinggraphon0≤x≤2,from(0,7)to(2,4e+3).','Originalfprime2e^(x/2)>0andfsecond e^(x/2)>0. Endpoints7and4e+3≈13.9;nosourceinterceptsorzerosinthisclosedviewport. Bookkey652showsbothendpointsandcurvebend. ThisisanASKEDsketch,notamereGIVENgraph.',652,'sketch');q.update(assessed_8227_demand_ids=[SKETCH],component_demand_ids=[],given_representation='text',response_format='sketch',credited_features=['Closedviewport0≤x≤2','Positivegraphwith(0,7)','Endordinate4e+3atx2;keylabels13.9approximately','Increasingupward-bendingcurve'],criteria_basis='Author-derivedfromequationandcomparedwithtextbookkey652;noofficialawardtable.');extra(q,'original-endpoint-values','Tuple(('+f+').subs(x,0),('+f+').subs(x,2))','Tuple(7,4*exp(1)+3)')
r=b.bias('c-overestimate','Morethan8e−2:straighttopsareabovethecurve.','Originalfsecond=e^(x/2)>0on[0,2]. ThuspiecewiselinearchordsoverestimatetruepositiveintegralI8e−2. Useownsketchfrom(b),notincreasingalone.',652,('diff('+f+',x,2)','exp(x/2)'),'0≤x≤2','concave (YM upward-bending convention)');r['depends_on_source_parts']=['a-shown-I','b-sketch']
add(10,'I=0..2integral4e^(x/2)+3:(a)SHOW8e−2;(b)ASKEDsketchonclosedviewport;(c)whethertrapeziumestimateisgreaterorless. Sketch,biasandexactintegralaredistinctdemands.',[p,q,r])
p=t.proof('a-identity','tan(x)**2+cos(x)**2','sec(x)**2+cos(2*x)/2-Rational(1,2)',553,'Usetan²=sec²−1andcos²=(1+cos2x)/2onoriginalcosx≠0.');p['original_common_domain']='cosx≠0'
q=t.dv('a-exact-integral','tan(x)**2+cos(x)**2',0,'pi/4','Rational(5,4)-pi/8',652,[t.SQUARE,TRIG,DEF]);q.update(depends_on_source_parts=['a-identity'],required_method='HENCEusetheprovedform;noindependentidentitychoicedemandadded.')
r=a.dv('b-exact-volume','pi*(tan(x)+cos(x))**2',0,'pi/4','pi*(Rational(13,4)-sqrt(2)-pi/8)',652);r.update(assessed_8227_demand_ids=[VOL],component_demand_ids=[TRIG,DEF],given_representation='graph',units='units^3',printed_key_units='units^3',axis_of_rotation='x-axis',available_from_source_parts=['a-exact-integral'],required_method='Rotateactualregionaroundx-axis:diskareaπy². Expand(tanx+cosx)²=tan²x+cos²x+2sinx. Prior(a)canbeused,butstem(b)doesnotmandateHENCE. Intervalavoidstanpole.')
rw=add(11,'(a)SHOWtan²+cos²identityandHENCEexact0..π/4integral;(b)GIVENtanx+cosxregionrotatedaboutx-axis,exactvolumeπ(13/4−√2−π/8). Part(a)repeatsTry16Q1;wholequestionaddsvolume.',[p,q,r],'graph');rw.update(source_part_repeats={'a':'8227:TB:YM:C12:Try-Now-16:1'},duplicate_basis='Sameidentityandfiniteintegralonly;new(b)rotationsoliddemandmustnotbecollapsedintoawholequestionduplicate.');rw['value_level_scope_decisions'].append(dict(rule_id='8227:QUAL06',status='within',quoted_value='Q11(b)rotatedcompletelyaboutthex-axis;0≤x≤π/4.',reason='Actualrotationaxisisoneoftheprescribedcoordinateaxes;useπy²disks.'))
refs=[(110,553,'Exercise12Q8 GIVEN exponential minimum graph','Original4e^(x/2)−6x+3,Mabscissaln9andpositiveordinate15−12ln3;notanASKEDsketch.',[STAT,AREA],'graph','Exercise-12:8','given-figure'),(111,553,'Exercise12Q11(b) GIVEN rotation region','Positivey=tanx+cosxbetweenx0andπ/4,shadetox-axis. Rotationaboutx-axisrequiresdiskradiusy,notareaunchanged.',[VOL],'graph','Exercise-12:11','given-figure')]
for n,page,label,note,ds,rep,parent,kind in refs:
 fig(n,page,label,note,ds,rep,[],parent);figures[-1].update(item_id=f'8227:TB:YM:C12:Teaching-figure:{n}',printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind=kind,parent_item_id='8227:TB:YM:C12:'+parent)
 figures[-1]['mathematical_feature_review']['method']='ReadGIVENminimum/rotationgeometryandseparateASKEDsketchfromitsanswer-keygraph. Deriveoriginalendpoints,monotonicity,curvatureanddiskintegral;retainx-axisandviewport.'
pages=[dict(pdf_page=553,printed_page=pp(553),chapter=12,page_status='items enumerated',item_ids=[r['item_id']for r in answers]+[r['item_id']for r in figures if r['pdf_page']==553],continuation_item_ids=[],source_evidence=ev(553),reader='Codex author',date='2026-11-20',non_item_content='AllExercise12Q7–11includingaskedsketch,areaandrotationsolidparts;twoGIVENsourcegraphsenumerated. Q10responsegraphisonkey652anditsfeaturesarekeptinthepartanswerreview;notsourcegivenoraseparatequestion-pagefigure.',scope_screen='Finitecontinuousintervals,radiantrig,common-lognodeevaluation,andactualx-axisrotation. SourceAdvancedlabelisnotBloomclassification.')]
def save():
 for row in answers:
  for p in row['subparts']:
   if'operation'in p:
    got=compute(p['operation']);expected=expression(p.get('author_expected_normalised',p['printed_key_normalised']))
    assert primitive_agrees(p['operation'],got,expected)if p.get('answer_equivalence')=='up-to-additive-constant'else equivalent(got,expected),(row['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():
    if name in p.get('additional_operation_expected',{}):assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
 for name,data in [('answers-YM-C12-exercise-advanced.json',dict(scope='Complete553Exercise12Q7–11responses.',items=answers)),('census-YM-C12-exercise-advanced.json',dict(book='YM',book_id='8227-SRC-017',chapter=12,source_path=SRC,source_sha256=SHA,scope='Complete553page/item/givenandanswer-graphrecords.',new_items=new+figures,corrections=corrections,pages=pages))]:(W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
if __name__=='__main__':save()
