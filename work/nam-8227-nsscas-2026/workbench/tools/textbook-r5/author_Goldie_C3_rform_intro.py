"""Fixed-source R-form exposition, Example 3.6 and Exercise 3D1–3, PDF86–89."""
import hashlib,json
from pathlib import Path
from author_YM_C4_trig_graphs import value,graph,reasoning
from author_YM_C4_composite_equations import roots
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2]
SRC='sources/namibia/nsscas/8227-mathematics/textbooks/Goldie_Pure-Mathematics-2-and-3_2nd-edition_2018.pdf'
SHA='f030d64259ffe233a7408d2a64dea21c0a04f1ac0426439f5efaea694eb72e85'
RFORM='8227:2020:M2:T3:O02:D04';COMP='8227:2020:M2:T3:O02:D02';RANGE='8227:2020:M1:T3:O02:D02'
SKETCH='8227:2020:M1:T6:O02:D03';BND='8227:2020:M1:T6:O06:D01';ALL='8227:2020:M1:T6:O06:D02'
def ev(page):
    name='Goldie-key-C3-337'if page==340 else'Goldie-key-C3-341'if page==341 else'Goldie-C3-86'
    p=W/f'checks/r5/textbooks/{name}.png'
    return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def rform(label,a,b,target,unit,key,kp,bounds,dp=None):
    p=value(label,'0',key,kp,
      'Match the coefficients of the original a*sin(t)+b*cos(t) to the specified target. Independently derive positive R by the coefficient norm and phase by a quadrant-aware atan2. Keep exact internal parameters; round only the requested/displayed phase. Verify both coefficient equations, rather than treating a rounded phase as an exact identity.')
    exact={'kind':'r-form-coefficients','operands':[a,b],'target':target,'angle_unit':unit,'phase_bounds':bounds,
      'left_open':True,'right_open':True}
    p['operation']={**exact,**({'phase_decimal_places':dp}if dp is not None else{})}
    p['additional_operations']={'unrounded_canonical_parameters':exact}
    p['phase_comparison_basis']='Exact phase unless a decimal display is explicitly compared; the unrounded candidate is retained separately for graph/solution checks.'
    return p
answers=[];new=[];corrections=[]
def add(kind,n,page,note,parts,direct,components=None,new_item=False,sketch=False):
    for p in parts:
        kp=p.pop('key_page_override',page)
        pp=p.pop('source_page_override',None)or page
        p.update(source_pdf_page=pp,source_evidence=ev(pp),answer_pdf_page=kp,
          answer_printed_page=kp-14,key_evidence=ev(kp),review_date='2026-11-18')
    row={'item_id':f'8227:TB:Goldie:C3:{kind}:{n}','source_pdf_page':page,'notes':note,
      'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],
      'mapping_rationale':'Only explicit requested forms, extrema, sketches and bounded roots are assessed. Unprompted generalisations are teaching/component evidence. The independently used norm/atan2 or half-angle verification methods do not become additional learner demands.',
      'representation':'text','sketch_response_required':sketch,
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'within'if kind=='Example'else'not applicable',
        'quoted_value':note,'reason':'Example3.6(iv) has argument multiplier1 and the explicit finite radian interval0≤θ≤2π.'if kind=='Example'else'The source asks a coefficient form, not a periodic root family.'},
       {'rule_id':'8227:QUAL07','status':'within'if kind=='Example'else'not applicable',
        'quoted_value':note,'reason':'The simple transformed sine has exact range[−2,2]; the requested sketch interval is retained.'if kind=='Example'else'No domain/range output is requested.'}],
      'exam_style':False,'exam_style_basis':'Unattributed exposition, Example3.6 or ordinary Exercise3D; no examination attribution on these items.',
      'precision_angle_check':{'source':'The expositions display36.9°/53.1° approximately. Exercise3D1/3 uses degree phases;3D2 uses exact radian phases. Positive amplitude and each stated phase interval are retained.',
        'comparison':'A displayed rounded phase is not an exact coefficient identity. Every later root/graph uses exact source coefficients or the unrounded phase; do not carry a printed rounded phase into another answer.'},
      'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts}
    if not direct:row['evidence_role']='prerequisite/supporting teaching exposition; no invented assessed question'
    answers.append(row)
    if new_item:new.append({'item_id':row['item_id'],'item_kind':'worked-derivation','exercise':kind,'item_number':str(n),
      'pdf_page':page,'printed_page':page-14,'notes':note,'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],
      'teaches_8227_demand_ids':components or direct,'representation':'text','source_evidence':ev(page),
      'evidence_role':row.get('evidence_role','directly related assessed practice'),
      'answer_key':{'available':True,'pdf_pages':sorted({p['answer_pdf_page']for p in parts}),
        'printed_pages':sorted({p['answer_printed_page']for p in parts}),'locator':'Inline explanatory derivation'},'learner_display':False})
    return row

p=rform('numerical-form','4','3','sin-plus','degree','Tuple(5,369/10)',86,['0','90'],1)
p2=reasoning('general-form','For (a,b)≠(0,0), choose R=√(a²+b²)>0 and a phase with cosα=a/R, sinα=b/R. Then a*sinθ+b*cosθ=R*sin(θ+α).',
 'The coefficient vector divided by its nonzero norm lies on the unit circle, so such a phase exists. Sine addition gives R*cosα*sinθ+R*sinα*cosθ, exactly the source expression. The zero vector needs separate treatment because its phase is undefined. The printed numerical36.9° is only a rounded illustration.',86,'matches')
p2['additional_operations']={'general_identity_on_nonzero_vector':{'kind':'trig-identity-residual',
 'operands':['sqrt(a**2+b**2)*sin(x+atan2(b,a))','a*sin(x)+b*cos(x)']}}
add('Worked-derivation',6,86,'Headingless sine R-form derivation for4sinθ+3cosθ, followed by a*sinθ+b*cosθ. The3–4–5 triangle gives R=5 and exact phaseatan(3/4), displayed36.9°; generalisation requires a nonzero coefficient pair.',[p,p2],[],[RFORM,COMP],new_item=True)

p=rform('numerical-form','4','3','cos-minus','degree','Tuple(5,531/10)',87,['0','90'],1)
p['source_page_override']=87
p2=reasoning('general-domain','For a*cosθ+b*sinθ with a nonzero coefficient pair, R=√(a²+b²) and a quadrant-aware phase give a valid cosine form. A phase convention must include one of ±180°; the printed strict interval excludes a valid negative-cosine axis case.',
 'The source note says r is always positive and in all cases a phase exists with−180°<α<180°. If a=−1,b=0, coefficient comparison forces cosα=−1,sinα=0, so no phase lies strictly between the two excluded endpoints. A half-closed interval such as(−180°,180°] can represent it; this is an example verification convention, not a recipe-policy decision. If a=b=0, the function is zero and no positive-amplitude representation/unique phase exists. The nonzero-vector identity itself is valid.',87,'key incomplete')
p2['source_page_override']=87
p2['additional_operations']={'negative_cosine_axis':{'kind':'r-form-coefficients','operands':['0','-1'],
 'target':'cos-minus','angle_unit':'radian'},
 'general_identity_on_nonzero_vector':{'kind':'trig-identity-residual',
 'operands':['sqrt(a**2+b**2)*cos(x-atan2(b,a))','a*cos(x)+b*sin(x)']}}
row=add('Worked-derivation',7,86,'Cosine alternative introduced at the foot ofPDF86 and developed on87:3cosθ+4sinθ=5cos(θ−atan(4/3)), with53.1°as a rounded display. The generic all-cases note needs nonzero-vector and phase-endpoint qualifications.',[p,p2],[],[RFORM,COMP],new_item=True)
corrections.append({'item_id':row['item_id'],'continuation_pdf_pages':[87]})

p=rform('i','sqrt(3)','-1','sin-minus','radian','Tuple(2,pi/6)',88,['0','pi/2'])
p2=value('ii','Tuple(sqrt(sqrt(3)**2+(-1)**2),-sqrt(sqrt(3)**2+(-1)**2))','Tuple(2,-2)',88,
 'The independently derived amplitude is2. Sine attains1 and−1, so the maximum/minimum are2/−2; they occur within a full original0..2πcycle as well.')
p2['additional_operations']={'exact_original_coefficients_norm':{'kind':'identity','operands':['sqrt(sqrt(3)**2+(-1)**2)']}}
p3=graph('iii','sin','2','1','0','0','2*pi','radian',88,
 {'amplitude':'2','period':'2*pi','window_range':'Interval(-2,2)'})
p3['operation']['phase_offset']='-pi/6'
p3['author_source_graph_comparison']={'status':'key wrong',
 'reason':'The source asks a sketch only for0≤θ≤2π, but Figure3.12 explicitly continues beyond2π and labels a third zero13π/6, with an axis tick5π/2. The curve shape is correct for the unrestricted function; its extent does not respect the requested interval.',
 'observed_features':['The stem interval is0≤θ≤2π.','Figure3.12 labels13π/6 as another zero beyond the right boundary.','The requested graph should stop at(2π,−1); its only interval zeros areπ/6 and7π/6.']}
p4=roots('iv','sqrt(3)*sin(x)-cos(x)-1','FiniteSet(pi/3,pi)',89,
 [('sin','x-pi/6','1/2',1)],unit='radian')
p4['dependency']={'source_part':'i','role':'Use the exact R-form while retaining the original0≤θ≤2πinterval; the shifted argument range is−π/6..11π/6.'}
row=add('Example',6,87,'For√3sinθ−cosθ, find the form r*sin(θ−α)with r>0,0<α<π/2; state extrema; sketch on0≤θ≤2π; solve the original expression=1on that interval. The source sketch extends beyond its requested domain.',[p,p2,p3,p4],[RFORM,RANGE,SKETCH,BND,ALL],[COMP],sketch=True)
corrections.append({'item_id':row['item_id'],'continuation_pdf_pages':[88,89]})

parts=[]
for label,a,b,key,dp in[
 ('i','1','1','Tuple(sqrt(2),45)',None),
 ('ii','21','20','Tuple(29,464/10)',1),
 ('iii','sqrt(3)','1','Tuple(2,60)',None),
 ('iv','2','sqrt(5)','Tuple(3,418/10)',1)]:
    parts.append(rform(label,a,b,'cos-minus','degree',key,340,['0','90'],dp))
add('Exercise-3D',1,89,'Express cosθ+sinθ,20cosθ+21sinθ,cosθ+√3sinθ,and√5cosθ+2sinθas r*cos(θ−α),r>0and0°<α<90°; retain the specified positive acute phase.',parts,[RFORM],[COMP])
parts=[rform('i','-1','1','cos-plus','radian','Tuple(sqrt(2),pi/4)',341,['0','pi/2']),
 rform('ii','-1','sqrt(3)','cos-plus','radian','Tuple(2,pi/6)',341,['0','pi/2'])]
add('Exercise-3D',2,89,'Express cosθ−sinθand√3cosθ−sinθas r*cos(θ+α),r>0and0<α<π/2. The plus inside cosine requires a negative original sine coefficient.',parts,[RFORM],[COMP])
parts=[rform('i','1','2','sin-plus','degree','Tuple(sqrt(5),634/10)',341,['0','90'],1),
 rform('ii','2','sqrt(5)','sin-plus','degree','Tuple(3,482/10)',341,['0','90'],1)]
add('Exercise-3D',3,89,'Express sinθ+2cosθand2sinθ+√5cosθas r*sin(θ+α),r>0and0°<α<90°. Compare sine/cosine coefficients in the target order, not a memorised reversed ratio.',parts,[RFORM],[COMP])

figures=[]
for n,page,label,note,parent,rep,method in[
 (16,86,'Figure3.9 sine R-form triangle','The right triangle has adjacent4,opposite3,hypotenuse5; its acuteαhas cosα=4/5,sinα=3/5. It supports the sine-plus coefficient order.','Worked-derivation:6','diagram',
 'The original4sinθ+3cosθ fixes the two legs; their norm and coefficient equations independently determine the phase. The36.9°label is approximate.'),
 (17,86,'Sine R-form coefficient flow','The displayed generalisation matches a=Rcosα,b=Rsinα for a*sinθ+b*cosθ. A nonzero coefficient vector is required.','Worked-derivation:6','table',
 'The parent exact coefficient proof expands the addition formula; no positive amplitude/unique phase is claimed for the zero vector.'),
 (18,87,'Figure3.10 cosine R-form triangle','The alternative triangle uses adjacent3,opposite4,hypotenuse5, giving a cosine-minus phaseatan(4/3),approximately53.1°.','Worked-derivation:7','diagram',
 'The coefficient order changes with the target family. Exact internal phases, not displayed approximations, are used for validation.'),
 (19,87,'Cosine R-form coefficient flow and phase note','The reference matches a=Rcosα,b=Rsinα in a*cosθ+b*sinθ. The note uses a strict−180°<α<180°interval and claims all cases; the parent records the missing endpoint/zero-vector qualifications.','Worked-derivation:7','table',
 'A negative cosine axis needs one of the±180°representatives, while the zero vector has no unique phase. Neither is silently forced into the printed strict convention.'),
 (20,88,'Figure3.11 Example3.6 exact triangle','The coefficient triangle has legs√3 and1,hypotenuse2,withα=π/6. The minus cosine coefficient selects sine-minus.','Example:6','diagram',
 'Independent coefficient matching givesR=2andα=π/6; the phase signs are checked against the original√3sinθ−cosθ.'),
 (21,88,'Figure3.12 Example3.6 extended sketch','The plotted2sin(θ−π/6)curve has extrema±2and labels zerosπ/6,7π/6,13π/6. It extends past the requested2πboundary; the parent records that source display defect.','Example:6','graph',
 'The correct requested-window features are computed independently: zerosπ/6,7π/6;maximum at2π/3,minimum at5π/3,andboth endpoint ordinates−1. The source full curve is distinguished from the required interval.'),
 (22,89,'Figure3.13 shifted-argument sine solutions','The reference sine graph gives argument rootsπ/6and5π/6for value1/2. Adding the source phaseπ/6returns originalθ=π/3andπ.','Example:6','graph',
 'The original equation is solved independently; the substituted argument interval−π/6..11π/6is retained. The adjacent warning explains why a standard0..2πsearch is not always appropriate after a phase shift.')]:
    figures.append({'item_id':f'8227:TB:Goldie:C3:Teaching-figure:{n}','item_kind':'teaching-figure','exercise':'Teaching figure','item_number':str(n),
      'pdf_page':page,'printed_page':page-14,'source_label':label,'notes':note,'what_it_shows':note,
      'assessed_8227_demand_ids':[],'component_demand_ids':[],'teaches_8227_demand_ids':[RFORM],
      'representation':rep,'source_evidence':ev(page),'parent_item_id':'8227:TB:Goldie:C3:'+parent,'learner_display':False,
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'not applicable','quoted_value':note,
        'reason':'A teaching/solution representation, not a separate periodic-equation response.'}],
      'value_level_scope_review_status_r5':'author actual coefficient/phase/interval evidence read2026-11-18; independent check pending',
      'exam_representation_check':{'status':'final cross-book/examination comparison pending','examination_part_ids':[],
        'relation':'Textbook teaching representation; no official award or examination-frequency claim.'},
      'mathematical_feature_review':{'status':'author source render and parent exact coefficient/graph/root checks; independent acceptance pending','method':method}})
pages=[{'pdf_page':page,'printed_page':page-14,'chapter':3,'page_status':'items enumerated',
 'item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],
 'continuation_item_ids':[r['item_id']for r in corrections if page in r['continuation_pdf_pages']],
 'source_evidence':ev(page),'non_item_content':'All headingless R-form expositions, Example3.6 parts/continuations, Exercise3D1–3 and seven teaching figures/flows enumerated. The shifted-domain warning is attached to the relevant worked example, not invented as another assessed task.',
 'reader':'Codex author','date':'2026-11-18'}for page in range(86,90)]
if __name__=='__main__':
    for name,data in[
      ('answers-Goldie-C3-rform-intro.json',{'scope':'All fixed source tasks/expositions onPDF86–89; remaining R-form exercises pending.','items':answers}),
      ('census-Goldie-C3-rform-intro.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':3,'source_path':SRC,'source_sha256':SHA,
        'scope':'PDF86–89: every task, continuation and mathematical teaching representation.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(len(answers),'items;',len(figures),'figures;',sum(len(r['subparts'])for r in answers),'outputs')
