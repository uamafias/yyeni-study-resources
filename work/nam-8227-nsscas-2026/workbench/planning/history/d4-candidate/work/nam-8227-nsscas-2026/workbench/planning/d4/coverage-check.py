"""Derive the D4 planning coverage ledger; not a runtime resource builder.

The examination scan reads only question-analysis part->demand links. Accepted
family records supply dispositions, never demand coverage or exam weights.
"""
from pathlib import Path
from fractions import Fraction
import argparse, collections, copy, hashlib, json
W = Path(__file__).resolve().parents[2]
P = W / 'planning'
BASE = P / 'history/d1-candidate/work/nam-8227-nsscas-2026/workbench/planning/coverage-plan.json'
NAMES = ['visual-design.json', 'calculus-design.json', 'trig-model-design.json']
def read(p): return json.loads(p.read_text())
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def encoded(o): return json.dumps(o, ensure_ascii=False, indent=2) + '\n'
def esc(s): return str(s).replace('|', '&#124;').replace('\n', ' ')
def slim(d): return d.replace('8227:2020:', '')
def part_label(p):
    label = p['qualified_part_id']
    if p.get('assessment_condition'): label += ' [only ' + p['assessment_condition'] + ']'
    return label

def examination_scan():
    # This function deliberately has no family/pattern input. Tariffs are full
    # part tariffs, not invented criterion allocations to separate objectives.
    qs = read(W / 'analysis/question-analysis.json')['questions']
    stats = collections.defaultdict(lambda: dict(parts=[], usable=[], marks=0, share=Fraction(), papers=set(), years=set()))
    total = 0; part_ids = set(); paper_marks = collections.Counter(); all_share = Fraction()
    for q in qs:
        for p in q['parts']:
            pid = p['part_id']; assert pid not in part_ids; part_ids.add(pid)
            marks = p['printed_marks']; total += marks; paper_marks[(q['year'], q['paper'])] += marks
            ds = p['directly_assessed_demand_ids']; assert ds and len(ds) == len(set(ds))
            for d in ds:
                s = stats[d]; s['parts'].append(pid); s['marks'] += marks
                s['share'] += Fraction(marks, len(ds)); all_share += Fraction(marks, len(ds))
                s['papers'].add((q['year'], q['paper'])); s['years'].add(q['year'])
                if p['disposition'] != 'hold': s['usable'].append(pid)
    assert len(qs) == 119 and len(part_ids) == 250 and total == 750
    assert len(paper_marks) == 10 and set(paper_marks.values()) == {75}
    assert all_share == 750
    rows = {}
    for d, s in stats.items():
        rows[d] = dict(exam_part_count=len(s['parts']), usable_exam_part_count=len(s['usable']),
            full_linked_part_marks=s['marks'], linked_part_marks_percent_of_750=round(100*s['marks']/750, 3),
            papers_of_10=len(s['papers']), years_of_5=len(s['years']),
            paper_ids=[f'{y}:P{p}' for y,p in sorted(s['papers'])], years=sorted(s['years']),
            exam_part_ids=s['parts'], equal_split_mark_share=dict(numerator=s['share'].numerator,
                denominator=s['share'].denominator, rounded_1dp=round(float(s['share']),1),
                basis='Informational 1dp uses binary-float round for reviewer comparability; exact fraction authoritative. Judgement-only crosscheck: printed part marks divided equally over ALL its direct demand IDs, including supplementary IDs. Not official criterion credit.'))
    return rows, stats

GAP_REASONS = {
 'function-analysis': 'Domain/range restrictions, one-to-one decisions, composite functions and inverse-function reasoning are outside these nine designs. The logarithm sketch and supplied log model do not assess that connected analysis. Retain the whole accepted group for a separately evidenced design.',
 'numerical-method-chain': 'No chosen branch brackets roots or applies/reviews an iteration with stopping conditions. Trapezium quadrature approximates an integral and does not supply numerical root finding. Retain this examination-observed group for a later distinct design.',
 'constrained-optimisation': 'The stationary-point designs receive an explicit polynomial; none constructs a contextual/geometric model, imposes its admissible constraints and then optimises it. Do not claim modelling coverage from differentiation alone.',
 'quadratic-substitution': 'Recognising a substitution, solving the resulting quadratic and recovering/filtering the original unknown are outside the nine selected branch demands. Routine algebra within other parts supplies no coverage of this decision chain.',
 'binomial-selection': 'Term/coefficient selection and parameter conditions in a binomial expansion are not assessed by these designs. Keep the observed variations for later source-based branch design.',
 'product-quotient': 'The implicit branch uses a product rule within its prescribed implicit equation. That narrow facet does not provide the explicit product/quotient selection, quotient forms or full breadth of this accepted group.',
 'trig-integration': 'No selected integral requires choosing a trigonometric identity before integration. Polynomial/exponential motion and logarithm quadrature do not replace this directly required integration decision.',
 'circular-symbolic': 'Arc/sector composite perimeter and area with symbolic relationships are outside the chosen pilot. Vector angles and quadrature width do not assess circular measure or geometric assembly.',
 'circular-contact': 'Circle/sector contact relations and the selection of geometry needed for their areas are outside the nine designs; do not infer this from generic angle calculations.',
 'segment-area': 'Sector-minus-triangle construction of a circular segment area is not assessed; preserve its scope and angular/area conventions for later native-page design.',
 'coordinate-shapes': 'The pilot does not construct equations from geometric line/shape constraints. A normal line following an implicit gradient is only its expressly tagged tangent/normal facet.',
 'line-curve': 'The pilot does not solve line/curve intersections or interpret tangency as a repeated root. Labelled intercepts supplied in a modulus graph do not assess this algebraic/geometric chain.',
 'advanced-trig-proof': 'R-form conversion and principal inverse evaluation do not require proving an identity from reciprocal, compound or double-angle relationships. Explicit proof marking and its alternatives need their own later design.',
 'basic-trig-proof': 'No selected branch asks the learner to prove a basic trigonometric identity. The implicit show-derivative branch tests different content and cannot cover this required proof demand.',
 'parametric': 'No selected curve is parametrically defined; eliminating or differentiating a parameter and geometric conditions involving dx/dt remain outside the pilot.',
}
SELECTED_REASONS = {
 'bounded-trig': 'Only the R-form degree-cycle root part is selected here. Recovery of both roots in its stated cycle is assessed; other basic-equation/identity structures and intervals remain later scope.',
 'r-form': 'Selected only as the prescribed two-part R-form reduction and degree-cycle equation. This does not cover every extremum interpretation or reciprocal/compound-identity route in the accepted group.',
 'principal-values': 'One uncued solve-or-explain branch is selected. Its principal-range decision is unconditional; exact special-angle evaluation is assessed only on the real-solution instances. Defective 2023 Paper 1 Question 9 stays held.',
 'implicit': 'Selected gradient and connected show-derivative/gradient/normal branches use a bounded implicit product family. Parametric or other implicit structures remain later scope; a supplied derivative is not counted as newly differentiated.',
 'stationary-points': 'Selected explicit cubic extrema and flat-point classification branches. Their point finding and local sign/classification evidence do not provide constrained modelling or all curve families.',
 'motion-integration': 'Selected polynomial velocity recovery, positive exponential distance and an uncued quadratic-velocity interval sign-change check, including a bounded minority with no sign change. Source alternatives, event constraints and higher reversal counts outside these domains remain later scope.',
 'motion-differentiation': 'Selected only exponential acceleration and the direct motion/derivative facets named in the part ledger. Other event-conditioned derivatives and motion models remain later scope.',
 'modulus-reading': 'Selected integer-coefficient graph reconstruction from must-read vertex/intercepts. Domains exclude named-error coincidences and the original tuple; modulus graph construction/equations are outside this branch.',
 'trapezium-chain': 'Selected logarithmic quadrature, hence scaling, own sketch and Apply-level chord/bias reasoning. The corrected D1-TRAP-FT-BRIDGE is accepted under OD-5; final plan approval remains pending; other integrands and unsupported higher reasoning labels are not included.',
 'vector-product': 'Selected prescribed scalar-combination/perpendicularity and origin-angle parts with nonzero distinct vectors. General 3D diagram interpretation, unit vectors and unrelated vector geometry remain later scope.',
 'linearisation': 'Selected transformed straight-line parameter recovery from a given graph and a separate given-gradient model branch. Choosing a model from raw contextual data or all functional forms is not assessed.',
 'exponential-equations': 'Selected only the logarithmic model target equation in gradient-target. Unrelated exponential equations and inequalities remain later scope.',
}

def build():
    out = copy.deepcopy(read(BASE))
    assert len(out['demands']) == 138 and len(out['accepted_selection_dispositions']) == 67 and len(out['non_specific_demands']) == 8
    demand_ids = {r['demand_id'] for r in out['demands']}
    direct = collections.defaultdict(list); conditional = collections.defaultdict(list); prior = collections.defaultdict(list)
    recipes=[]; branch_count=0; n_parts=0; levels=collections.Counter(); selected=collections.defaultdict(list)
    for name in NAMES:
        for r in read(P/name)['recipes']:
            recipes.append(r)
            for sid in r['accepted_selection_ids']: selected[sid].append(r['recipe_id'])
            for b in r['branches']:
                branch_count+=1; bs=b['branch_id'].split(':')[-1]; qb=r['recipe_id']+':'+bs
                bl=b.get('whole_bloom',b.get('whole_card_bloom')); bl=bl['level'] if isinstance(bl,dict) else bl
                part_levels=[part['bloom']['level']if isinstance(part['bloom'],dict)else part['bloom']for part in b['part_specs']];assert max(part_levels)==bl,(qb,part_levels,bl)
                levels[str(bl)]+=1
                for part in b['part_specs']:
                    n_parts+=1; local=part.get('local_part_id',part['part_id'].split(':')[-1]); qp=qb+':'+local
                    ref=dict(recipe_id=r['recipe_id'], branch_id=bs,qualified_branch_id=qb,part_id=local,
                        qualified_part_id=qp,marks_for_part=part['marks'],meaning='Named direct assessment facet only; the full part tariff is not allocated wholly to each demand.')
                    for d in part['directly_assessed_demand_ids']:
                        assert d in demand_ids,(qp,d); direct[d].append(copy.deepcopy(ref))
                    for condition, ds in part.get('conditional_directly_assessed_demand_ids',{}).items():
                        for d in ds:
                            assert d in demand_ids,(qp,d); conditional[d].append(dict(copy.deepcopy(ref),assessment_condition=condition,
                                meaning='Conditional direct assessment facet only on instances satisfying this case; not inherited by other instances.'))
                    for d in part.get('prerequisite_demand_ids',[]):
                        did=d['demand_id'] if isinstance(d,dict) else d
                        prior[did].append(dict(copy.deepcopy(ref),role=d.get('role','prerequisite only') if isinstance(d,dict) else 'prerequisite only',meaning='Prerequisite/support only; never counted as direct demand coverage.'))
    assert len(recipes)==9 and branch_count==14 and n_parts==27
    assert len(direct)==38 and len(set(conditional)-set(direct))==1
    assert dict(levels)=={'3':13,'4':1}
    motion=next(r for r in recipes if r['recipe_id']=='WB8227-motion-integration');assert [b['capacity']for b in motion['branches']]==[137,56,168]
    stats, raw_stats=examination_scan()
    zero=dict(exam_part_count=0,usable_exam_part_count=0,full_linked_part_marks=0,linked_part_marks_percent_of_750=0,papers_of_10=0,years_of_5=0,paper_ids=[],years=[],exam_part_ids=[],equal_split_mark_share=dict(numerator=0,denominator=1,rounded_1dp=0,basis='Judgement-only equal split; not official criterion credit.'))
    unconditional_ids=set(direct); conditional_ids=set(conditional); facet=unconditional_ids|conditional_ids
    for row in out['demands']:
        d=row['demand_id']; row['planned_direct_parts']=direct[d]; row['conditional_direct_parts']=conditional[d]; row['prerequisite_only_parts']=prior[d]
        row['examination_weight']=copy.deepcopy(stats.get(d,zero))
        if direct[d]:
            row['pilot_disposition']='pilot-direct-facets'; row['reason']='The named proposed parts directly assess this bounded facet. This is a paper design, not implementation or complete objective/examination-pattern coverage. Other facets remain explicit in the linked work orders and later syllabus scope.'
        elif conditional[d]:
            row['pilot_disposition']='pilot-conditional-direct-facets'; row['reason']='The principal-inverse solve-or-explain branch directly assesses exact special-angle evaluation only on real-solution instances. The no-real-solution outcome tests the principal-range decision and does not inherit this secondary link. This is not unconditional or full-demand coverage.'
        else:
            row['pilot_disposition']='later-syllabus-scope-not-excluded'
            row['reason']='This required action is outside the selected pilot assessment: '+row['learner_action']+'.'+(' It is used only as a prerequisite/support in the named parts; this does not cover it directly.' if prior[d] else '')+' Retain it for later branch design using native pages and accepted assessed/component union evidence; the pilot boundary is not a syllabus exclusion.'
        row['full_demand_coverage_claimed']=False; row['implemented_coverage']=False
    for row in out['accepted_selection_dispositions']:
        sid=row['selection_id']; short=sid.split(':')[-1]; chosen=selected[sid]; row['selected_recipe_ids']=chosen
        row['pilot_disposition']='selected-subset-proposed-not-authored' if chosen else 'later-included-not-authored'
        row['reason']=SELECTED_REASONS.get(short) if chosen else GAP_REASONS.get(short)
        if not row['reason']: row['reason']='The '+row['title']+' task structures are outside the nine selected recipe boundaries. Preserve this accepted group and all directly linked required actions; no full-group coverage is inferred from shared arithmetic, prerequisites or topic labels.'
        row['next_action']='Review the named bounded work orders, their omitted facets and native-source comparisons; preserve unselected structures for later design after owner approval.' if chosen else 'After pilot acceptance, inspect native syllabus/exam/textbook pages and every assessed/component-union member; decide genuine problem types/branches before setting recipe counts.'
    for row in out['non_specific_demands']:
        d=row['demand_id']; row['planned_direct_parts']=direct[d]; row['conditional_direct_parts']=conditional[d]; row['prerequisite_only_parts']=prior[d];row['examination_weight']=copy.deepcopy(stats.get(d,zero))
        if d.endswith(':MODEL'):
            row['pilot_disposition']='later-cross-cutting-model-construction-not-assessed'
            row['reason']='The nine recipes provide expressions, graphs or prescribed models. Recovering constants in a supplied log model and proving a supplied implicit derivative do not construct a model from geometric/contextual constraints. Keep the 10 observed parts/26 overlapping full part marks visible outside the 138-content-demand denominator.'
            row['next_action']='Design a separate contextual/geometric model-construction task with constraints and criterion evidence; do not infer it from successful calculation.'
        else:
            row['pilot_disposition']='prior-skill-baseline-not-AS-direct-coverage'
            row['reason']='This is an NSSCO prior-skill category, outside the 138 AS content demands. Related arithmetic/algebra/geometry can support the proposed tasks, but no standalone prior-skill recipe is commissioned and no AS direct coverage is claimed.'
            row['next_action']='Keep necessary prior knowledge explicit in each work order and practice guidance; plan a separate diagnostic/remediation choice only if later classroom scope requires it.'
        row['full_demand_coverage_claimed']=False; row['implemented_coverage']=False
    content_share=sum((raw_stats[d]['share'] for d in demand_ids if d in raw_stats),Fraction())
    # Re-run the reviewer's 15 stored numeric comparisons. This is a frequency
    # crosscheck, not preservation of its superseded D0 pilot assignments.
    review=read(W/'review/opus-5-5-step-3/check-coverage.json')['exam_weight']['top15_by_mark_share']
    comparisons=[]
    for r in review:
        s=stats[r['demand_id']]; observed=(s['exam_part_count'],s['usable_exam_part_count'],s['full_linked_part_marks'],s['equal_split_mark_share']['rounded_1dp'],s['papers_of_10'])
        expected=(r['exam_parts'],r['usable_parts'],r['marks_full'],r['marks_share_split'],r['papers_of_10'])
        assert observed==expected,(r['demand_id'],observed,expected)
        comparisons.append(dict(demand_id=r['demand_id'],numeric_comparison='agree',current_direct_facet=r['demand_id'] in unconditional_ids,current_conditional_facet=r['demand_id'] in conditional_ids))
    full_frequency_path=W/'review/opus-5-5-d1-short-check/check-coverage-demand-frequency-step3.json'
    full_frequency=read(full_frequency_path);assert len(full_frequency)==138
    all_comparisons=[]
    for row in full_frequency:
        did=row[0]; ss=stats.get(did,zero)
        actual=(ss['exam_part_count'],ss['usable_exam_part_count'],ss['full_linked_part_marks'],ss['equal_split_mark_share']['rounded_1dp'],ss['papers_of_10'],ss['years_of_5'])
        expected=tuple(row[2:8]);assert actual==expected,(did,actual,expected)
        all_comparisons.append(dict(demand_id=did,numeric_comparison='agree',fields=['parts','usable_parts','full_linked_marks','rounded_share_1dp','papers','years']))
    rounded_row_sum=sum((Fraction(str(row[5]))for row in full_frequency),Fraction())
    assert rounded_row_sum==Fraction('720.1')and content_share==Fraction(2162,3)
    uncond_objs={d.rsplit(':D',1)[0]for d in unconditional_ids};cond_objs={d.rsplit(':D',1)[0]for d in conditional_ids}-uncond_objs
    assert len(uncond_objs)==25 and cond_objs=={'8227:2020:M1:T6:O03'}
    partial_groups={'tangent-normal','gradient-evaluation','definite-integral','standard-antiderivatives'}
    for row in out['accepted_selection_dispositions']:
        if row['selection_id'].split(':')[-1]not in partial_groups:continue
        overlap=set(row['direct_demand_ids'])&facet; links={}
        for did in sorted(overlap):
            for pp in direct[did]+conditional[did]:
                key=pp['qualified_part_id']; info=links.setdefault(key,dict(qualified_part_id=key,recipe_id=pp['recipe_id'],matching_demand_ids=[]))
                info['matching_demand_ids'].append(did)
        row['decision_partly_exercised_by']=list(links.values())
        row['decision_overlap_count']=len(overlap);row['accepted_group_direct_demand_count']=len(row['direct_demand_ids'])
        row['reason']='This remains a later accepted parent group, not another selected recipe. '+str(len(overlap))+' of its '+str(len(row['direct_demand_ids']))+' directly linked demand facets have named bounded pilot decisions; explicit part links follow. This is partial decision overlap, not full examination-pattern breadth or group acceptance.'
    geometric=[]
    for question in read(W/'analysis/question-analysis.json')['questions']:
        for part in question['parts']:
            rep=part['given_representation'];kind=rep.get('kind')if isinstance(rep,dict)else rep
            if kind=='diagram':geometric.append(part['part_id'])
    assert len(geometric)==28
    # All27 givens are explicitly classified from their current authored work orders.
    # Missing representation is an error, never silently counted as no diagram.
    givens_path=P/'d4/given-representation-register.json'
    givens=read(givens_path)['parts'];assert len(givens)==27
    expected_ids={r['recipe_id']+':'+b['branch_id'].split(':')[-1]+':'+p.get('local_part_id',p['part_id'].split(':')[-1])for r in recipes for b in r['branches']for p in b['part_specs']}
    assert {x['qualified_part_id']for x in givens}==expected_ids
    assert all(x['kind']in ['text','diagram','graph','table']for x in givens)
    pilot_geometric=[x['qualified_part_id']for x in givens if x['kind']=='diagram']
    out['representation_gaps']=[dict(gap_id='D8227-G09',representation='given geometric diagram',exam_part_count=len(geometric),exam_part_ids=geometric,pilot_part_count=len(pilot_geometric),pilot_part_ids=pilot_geometric,given_representation_declarations='planning/d4/given-representation-register.json',disposition='later untested representation; not excluded from syllabus',reason='Every pilot part has an explicit given-format declaration from its work order. Modulus/log graphs and learner-requested sketches are distinct from reading supplied geometric givens.',next_action='A later source-backed recipe must retain geometric must-read givens and same-data diagram checks.')]
    original_pilot_path=P/'history/d0-candidate/work/nam-8227-nsscas-2026/workbench/planning/pilot-design.json'
    original=read(original_pilot_path)
    old_direct={d for r in original['recipes']for b in r['branches']for p in b['part_specs']for d in p['directly_assessed_demand_ids']}
    out['facet_changes_from_D0']=dict(added_unconditional=sorted(unconditional_ids-old_direct),removed_unconditional=sorted(old_direct-unconditional_ids),moved_to_conditional_only=sorted(old_direct&(conditional_ids-unconditional_ids)),reason='Set differences are derived from frozen D0 part links and current directly/conditionally assessed part links, not typed changes.')
    deck_spec_path=P/'d4/deck-compositions.json';decks=read(deck_spec_path)
    def components(rs,selection):
        answer=[]
        for rid,slug in selection:
            rr=next(r for r in rs if r['recipe_id']==rid);bb=next(b for b in rr['branches']if b['branch_id'].split(':')[-1]==slug)
            answer.append(dict(recipe_id=rid,branch_id=slug,marks=sum(p['marks']for p in bb['part_specs'])))
        return answer
    before=components(original['recipes'],decks['D0_symbolic']);current=components(recipes,decks['current']['symbolic'])
    out['representative_deck_change']=dict(D0=sum(x['marks']for x in before),D4=sum(x['marks']for x in current),D0_components=before,D4_components=current,current_deck_totals={name:sum(x['marks']for x in components(recipes,choice))for name,choice in decks['current'].items()},explanation='Every component tariff and total is derived from the named branch part marks. Composition selections are explicit Stage-D inputs, not live application decks.')
    out.update(date='2026-11-24',version='0.1.4',status='D4 proposed; Claude confirmation then Vitalis owner approval pending',
        counts=dict(recipes_proposed=9,branch_choices_proposed=14,work_orders=9,exemplar_documents=9,manual_paper_cases_planned=42,
            branch_qualified_assessed_parts=27,specific_demands_with_unconditional_direct_facets=len(unconditional_ids),specific_demands_with_conditional_only_direct_facets=len(conditional_ids-unconditional_ids),
            specific_demands_with_planned_direct_facets=len(facet),specific_demands_outside_pilot_direct_facets=138-len(facet),objectives_with_planned_direct_facets=len({d.rsplit(':D',1)[0] for d in facet}),objectives_with_unconditional_direct_facets=len(uncond_objs),objectives_with_conditional_only_direct_facets=len(cond_objs),conditional_only_objective_ids=sorted(cond_objs),
            specific_demands_accounted=138,analysis_selections_accounted=67,supplementary_demands_accounted=8,accepted_groups_with_selected_subsets=len([s for s,v in selected.items() if v]),accepted_groups_later=67-len([s for s,v in selected.items() if v]),
            whole_choice_bloom_counts=dict(sorted(levels.items())),implemented_recipes=0,runtime_generated_instances=0,approved_choices=0,generator_modules_selected=None),
        limits='All 138 specific demands, 67 accepted analysis selections and eight supplementary/prior-skill categories are accounted. Direct links mean named bounded design facets, not complete examination-demand coverage. Conditional links apply only in the stated case. R5-03 assessed/component unions and all-member native-page searches remain design authority; counts are lower bounds. Family tags, templated distinction/rejection text and damaged extracted notes are not design evidence.',
        examination_weight_method=dict(source='analysis/question-analysis.json',coverage_input='Each part.directly_assessed_demand_ids only; no pattern/family data is read by examination_scan.',
            questions=119,parts=250,papers=10,years=5,printed_marks_denominator=750,paper_tariff=75,
            held_parts_included=3,held_policy='All printed examination demands remain observed even when original items are held. usable_exam_part_count excludes the three held originals.',
            full_marks_rule='Each linked demand receives the FULL tariff of its directly linked part as contextual examination weight, not criterion credit. Multi-demand part tariffs overlap: do not sum these per-demand marks or their percentages to infer a 750-mark distribution.',
            optional_share_rule='Equal-split share is a judgement-only reviewer crosscheck. Divide each part tariff by the number of ALL direct demand IDs (including supplementary categories). Across all IDs it sums to 750; content-only sum excludes supplementary allocations. It is not official mark allocation or prediction.',
            content_only_equal_split_sum=dict(numerator=content_share.numerator,denominator=content_share.denominator,rounded_1dp=round(float(content_share),1)),
            supplementary_equal_split_sum_1dp=round(float(Fraction(750)-content_share),1),
            reviewer_crosscheck=dict(available_source='review/opus-5-5-step-3/check-coverage.json',full_frequency_source='review/opus-5-5-d1-short-check/check-coverage-demand-frequency-step3.json',all_138_numeric_comparisons=all_comparisons,all_138_agree=True,stored_top15_numeric_comparisons=comparisons,all_15_agree=True,
                aggregate_difference=dict(reviewer_D0_content_share_1dp=720.1,current_content_share_1dp=round(float(content_share),1),current_content_share_exact=str(content_share),current_supplementary_share_exact=str(Fraction(750)-content_share),explanation='Explained by reviewer and reproduced:720.1 reproduces the reviewer binary-float one-decimal row-rounding convention; exact decimal half-up row-rounding instead sums to720.5. Neither is the exact share total. Every full reviewer row agrees. Exact content2162/3≈720.7 plus supplementary88/3≈29.3 reconciles750; rounded per-row values must not be summed as an exact allocation.'),
                previous_missing_source_resolved='The step3prompt named a file not placed in that folder. D1shortcheck now supplies check-coverage-demand-frequency-step3.json; all138numericrows and15embeddedtoprows verified against current part-link rescan.')),
        input_sha256={name:sha(W/name) for name in ['analysis/demand-registry.json','analysis/demand-dispositions.json','analysis/problem-patterns.json','analysis/question-analysis.json']})
    out['input_sha256'].update({'planning/'+n:sha(P/n) for n in NAMES})
    out['input_sha256'].update({'planning/d4/given-representation-register.json':sha(givens_path),'planning/d4/deck-compositions.json':sha(deck_spec_path),'planning/history/d0-candidate/work/nam-8227-nsscas-2026/workbench/planning/pilot-design.json':sha(original_pilot_path)})
    out['input_sha256']['review/opus-5-5-step-3/check-coverage.json']=sha(W/'review/opus-5-5-step-3/check-coverage.json')
    out['input_sha256']['review/opus-5-5-d1-short-check/check-coverage-demand-frequency-step3.json']=sha(full_frequency_path)
    assert len({r['demand_id'] for r in out['demands']})==138
    assert len({r['selection_id'] for r in out['accepted_selection_dispositions']})==67
    assert len({r['demand_id'] for r in out['non_specific_demands']})==8
    assert sum(bool(r['planned_direct_parts'] or r['conditional_direct_parts']) for r in out['demands'])==39
    assert sum(bool(r['selected_recipe_ids']) for r in out['accepted_selection_dispositions'])==12
    return out

def markdown(j):
    c=j['counts']; lines=['# Proposed pilot coverage — NSSCAS Mathematics 8227, D4','',
        'Owner Vitalis; PLANNER Codex; 24 November 2026. Edition NIED December 2020, Grade 12. **Proposed paper designs only: Claude D4 confirmation, then Vitalis approval. No runtime implementation or full-demand coverage is certified.**','',
        f"The fixed nine recipes contain {c['branch_choices_proposed']} choices, {c['branch_qualified_assessed_parts']} assessed part slots and {c['manual_paper_cases_planned']} manual paper cases. There are **38 unconditional direct-demand facets plus one conditional-only facet** (39 of 138 demands; **26 / 60 objectives: 25 unconditional, one conditional-only, M1:T6:O03**); 99 required demands have no direct facet in this pilot. The exact special-angle link applies only to principal-inverse real-solution instances. Twelve accepted groups have selected subsets; 55 remain later scope. All 138 content demands, 67 accepted groups and eight supplementary categories retain dispositions.",'',
        'Proposed whole-choice Bloom counts: Apply 3 = 13; Analyse 4 = 1. Stationary classification is Apply under OD-4; the interval sign-change decision in motion is the only Analyse branch. The trapezium bias part is Apply, and the uncued principal decision is one Apply branch. No card is counted under more than its maximum genuinely assessed part level.','',
        'Use accepted item-level assessed/component union links (R5-03) and search every adopted/compared family member. Recorded same-type/branch counts are lower bounds. A topic tag, shared prerequisite, family distinction/precision template, templated rejection or damaged extracted note is not design evidence. Native pages and the work-order criteria govern design decisions.','',
        '## Examination weight: meaning and limits','',
        'Each demand row below is recomputed from **part → directly assessed demand links only** in `analysis/question-analysis.json`: 119 questions, 250 parts, ten 75-mark papers over 2021–2025 = **750 printed marks**. The three held originals remain in observed totals; usable counts exclude them. No family memberships are consulted for this scan.','',
        '“Parts / full linked marks / papers / years” counts each directly linked part once for that demand and includes its full printed tariff. Multi-demand parts appear against several demands, so these mark figures overlap and must not be summed as a mark allocation. The JSON also preserves all part locators and a judgement-only equal-split crosscheck: split each part tariff over all its direct IDs, including supplementary IDs. This sums to 750 over all IDs (720.7 content; 29.3 supplementary, rounded), not an official allocation. Neither statistic forecasts future examination frequency or proves that a pilot facet covers the full demand.','',
        'All **138** full reviewer numeric rows in `review/opus-5-5-d1-short-check/check-coverage-demand-frequency-step3.json` agree, as do all 15 embedded top rows from the step-3 coverage check. The previous 0.6 difference is now explained and reproduced: 720.1 reproduces binary-float per-row rounding in the reviewer table; decimal half-up rounding of the exact per-row fractions sums to 720.5. Neither rounded-row sum is the exact total. The exact content total is 2162/3 = 720.666… (720.7 rounded), plus supplementary 88/3 = 29.333… = 750. The earlier missing-file citation was a reviewer omission, now resolved by the supplied full table. Do not sum rounded per-demand shares as an exact allocation.','',
        '## Explicit scope changes and representation gap','',
        'Relative to D0, vector M1:T7:O02:D01 add/subtract replaces uncredited O02:D03 geometric interpretation. The new extended implicit gradient slot directly assesses **M1:T8:O01:D01 (Interpret curve gradient from a supplied derivative)**. Principal M1:T6:O03:D01 exact special-angle evaluation moved from unconditional to conditional-only; it applies only to real-solution instances. The 38 unconditional facets therefore are not the same set as the D0 38.','',
        '| Gap | Examination evidence | Pilot status / next action |','|---|---|---|',
        '| D8227-G09: given geometric diagrams | 28 directly recorded exam parts have given_representation=diagram; full part IDs are in the JSON | No selected pilot part supplies a geometric diagram. This representation remains untested until a later source-backed batch; modulus/log graphs, column vectors and learner sketches do not substitute for reading spatial givens. |','',
        'The symbolic composition increases from 14 to 19 through principal 2→3 (+1) and the implicit branch swap from gradient-only 5 to show-that/gradient/normal 4+2+3=9 (+4). It is not simply adding four proof marks to the previous composition.','',
        '## Specific-demand dispositions','',
        '| Demand / required action | Exam weight: parts (usable); full linked marks; papers/10; years/5 | Pilot disposition | Named direct facet, conditional facet or next action |',
        '|---|---|---|---|']
    for r in j['demands']:
        e=r['examination_weight']; ew=f"{e['exam_part_count']} ({e['usable_exam_part_count']}); {e['full_linked_part_marks']}; {e['papers_of_10']}; {e['years_of_5']}"
        links=[part_label(x) for x in r['planned_direct_parts']+r['conditional_direct_parts']]
        note='; '.join(links) if links else r['reason']
        if r['prerequisite_only_parts']: note+=' Prerequisite only: '+ '; '.join(part_label(x) for x in r['prerequisite_only_parts'])+'.'
        lines.append('| '+esc(r['demand_id']+' / '+r['learner_action'])+' | '+ew+' | '+r['pilot_disposition']+' | '+esc(note)+' |')
    lines+=['','## Accepted analysis selections: all 67 retained','',
        'These dispositions preserve accepted groups without equating a family tag with direct demand coverage. Selected means a bounded subset proposed in a named work order; unselected structures remain required later scope. Original-source holds remain effective.','',
        '| Accepted group / title | D4 disposition; selected recipes | Scope boundary and next action |','|---|---|---|']
    for r in j['accepted_selection_dispositions']:
        note=r['reason']+' '+r['next_action']
        if r.get('decision_partly_exercised_by'):note+=' Decision partly exercised by: '+ '; '.join(x['qualified_part_id']+' ['+', '.join(x['matching_demand_ids'])+']'for x in r['decision_partly_exercised_by'])+'.'
        if r['held_original_part_ids']:note+=' Held originals: '+', '.join(r['held_original_part_ids'])+'.'
        if r['source_hold_ids']:note+=' Source holds: '+', '.join(r['source_hold_ids'])+'.'
        lines.append('| '+esc(r['selection_id']+' / '+r['title'])+' | '+esc(r['pilot_disposition']+'; '+(', '.join(r['selected_recipe_ids']) or 'none'))+' | '+esc(note)+' |')
    lines+=['','## Supplementary ability and prior knowledge: all eight retained','',
        'These are outside the 138 specific AS content demands. Their examination context cannot be silently folded into content coverage.','',
        '| Category | Disposition | Exam parts; full linked marks | Reason and next action |','|---|---|---|---|']
    for r in j['non_specific_demands']:
        e=r['examination_weight'];lines.append('| '+r['demand_id']+' | '+r['pilot_disposition']+' | '+f"{e['exam_part_count']}; {e['full_linked_part_marks']}"+' | '+esc(r['reason']+' '+r['next_action'])+' |')
    lines+=['','All runtime/approved counts remain zero. No required demand is excluded because a selected recipe omits it, because it is absent from sampled papers or because a current response capability is unverified. Textbook originals remain internal. Diagram/sketch capabilities require later local acceptance using the real resources; no capability hold is introduced.','',
        'Rebuild/check: `python3 work/nam-8227-nsscas-2026/workbench/planning/d4/coverage-check.py --write` then `--check`. These commands derive planning records only; they create no runtime items or question generator.','']
    return '\n'.join(lines)

if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--write',action='store_true');a.add_argument('--check',action='store_true');args=a.parse_args()
    assert args.write != args.check, 'Choose exactly --write or --check'
    j=build(); outputs={P/'coverage-plan.json':encoded(j),P/'coverage-plan.md':markdown(j)}
    for p,s in outputs.items():
        if args.write:p.write_text(s)
        else:assert p.read_text()==s, str(p)+' is stale'
    receipt=dict(result='pass',mode='write'if args.write else'check',counts=j['counts'],exam_denominator=j['examination_weight_method']['printed_marks_denominator'],all138_agree=True,top15_agree=True,representation_gap=j['representation_gaps'][0],facet_changes=j['facet_changes_from_D0'],deck_change=j['representative_deck_change'],inputs=j['input_sha256'])
    receipt['mode']='check' # deterministic receipt for either successful derivation mode
    (P/'d4/coverage-check.json').write_text(encoded(receipt))
    print(encoded(receipt),end='')
