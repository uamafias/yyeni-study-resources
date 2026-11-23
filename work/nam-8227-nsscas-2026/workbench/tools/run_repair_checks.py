"""Rebuild twice, compare all assembled outputs, reject seeded bad fixtures."""
import argparse,json
import subprocess
import sys
from pathlib import Path
from analysis_sources import A, ROOT, WB, digest, write

STEPS=['screen_provenance_r5.py','annotate_provenance_screen_r5.py','build_source_addenda.py','build_cambridge.py','build_analysis.py','check_repair_r2.py',
       'build_marking_register.py','scan_convention_context_r4.py','build_textbook_discovery.py','discover_goldie_items.py',
       'textbook-r5/author_Goldie_1B.py','textbook-r5/author_Goldie_1C.py','textbook-r5/author_Goldie_C1_examples.py','textbook-r5/author_Goldie_C1_prompts.py','textbook-r5/author_Goldie_C7.py','textbook-r5/author_Goldie_C2_opening.py','textbook-r5/author_Goldie_C2_2A.py','textbook-r5/author_Goldie_C2_log_intro.py','textbook-r5/author_Goldie_C2_2B.py','textbook-r5/author_Goldie_C2_log_graphs.py','textbook-r5/author_Goldie_C2_natural_intro.py','textbook-r5/author_Goldie_C2_natural_examples.py','textbook-r5/author_Goldie_C2_2D.py','textbook-r5/author_Goldie_C2_models.py','textbook-r5/author_Goldie_C8_opening.py','textbook-r5/author_Goldie_C8_8B.py','textbook-r5/author_Goldie_C8_log_section.py','textbook-r5/author_Goldie_C8_trig_opening.py','textbook-r5/author_Goldie_C8_8D.py','textbook-r5/author_Goldie_C8_8E_activity.py','textbook-r5/author_Goldie_C8_8G.py','textbook-r5/author_Goldie_C8_closing.py','textbook-r5/author_Goldie_C9_opening.py','textbook-r5/author_Goldie_C9_closing.py','textbook-r5/author_Goldie_C10_opening.py','textbook-r5/author_Goldie_C10_calculations.py','textbook-r5/author_Goldie_C10_10B.py','textbook-r5/author_Goldie_C10_dot_opening.py','textbook-r5/author_Goldie_C10_10C.py','textbook-r5/author_Goldie_C10_line_opening.py','textbook-r5/author_Goldie_C10_closing.py','textbook-r5/author_Goldie_C11.py','textbook-r5/author_Goldie_C3_opening.py','textbook-r5/author_Goldie_C3_compound.py','textbook-r5/author_Goldie_C3_double.py','textbook-r5/author_Goldie_C3_rform_intro.py','textbook-r5/author_Goldie_C3_rform_exercises.py','textbook-r5/author_Goldie_C3_closing.py','textbook-r5/author_Goldie_C4_opening.py','textbook-r5/author_Goldie_C4_4A.py','textbook-r5/author_Goldie_C4_logs_intro.py','textbook-r5/author_Goldie_C4_logs_examples.py','textbook-r5/author_Goldie_C4_4B.py','textbook-r5/author_Goldie_C4_trig_intro.py','textbook-r5/author_Goldie_C4_4C.py','textbook-r5/author_Goldie_C4_implicit_intro.py','textbook-r5/author_Goldie_C4_implicit_stationary.py','textbook-r5/author_Goldie_C4_4D.py','textbook-r5/author_Goldie_C4_param_opening.py','textbook-r5/author_Goldie_C4_param_plots.py','textbook-r5/author_Goldie_C4_param_examples.py','textbook-r5/author_Goldie_C4_4E.py','textbook-r5/author_Goldie_C4_closing.py','textbook-r5/author_Goldie_C5_opening.py','textbook-r5/author_Goldie_C5_5A.py','textbook-r5/author_Goldie_C5_middle.py','textbook-r5/author_Goldie_C5_5B.py','textbook-r5/author_Goldie_C5_5C.py','textbook-r5/author_Goldie_C5_numerical_opening.py','textbook-r5/author_Goldie_C5_closing.py','textbook-r5/author_Goldie_C6_opening.py','textbook-r5/author_Goldie_C6_6A.py','textbook-r5/author_Goldie_C6_iteration_intro.py','textbook-r5/author_Goldie_C6_6B.py','textbook-r5/author_Goldie_C6_closing.py','textbook-r5/author_YM_C1_opening.py','textbook-r5/author_YM_C1_transformed.py','textbook-r5/author_YM_C1_discriminant.py','textbook-r5/author_YM_C1_quadratic_graphs.py','textbook-r5/author_YM_C1_intervals.py','textbook-r5/author_YM_C1_intersections.py','textbook-r5/author_YM_C1_identities_cubics.py','textbook-r5/author_YM_C1_exercise.py','textbook-r5/author_YM_C1_closing.py','textbook-r5/author_YM_C2_opening.py','textbook-r5/author_YM_C2_AP.py','textbook-r5/author_YM_C2_GP.py','textbook-r5/author_YM_C2_AP_sums.py','textbook-r5/author_YM_C2_blocks_GP_sums.py','textbook-r5/author_YM_C2_thresholds_sigma.py','textbook-r5/author_YM_C2_convergence.py','textbook-r5/author_YM_C2_applications.py','textbook-r5/author_YM_C2_finance_bounce.py','textbook-r5/author_YM_C2_progression_closing.py','textbook-r5/author_YM_C2_binomial_opening.py','textbook-r5/author_YM_C2_binomial_notation.py','textbook-r5/author_YM_C2_binomial_terms.py','textbook-r5/author_YM_C2_coefficient_parameters.py','textbook-r5/author_YM_C2_binomial_exercise.py','textbook-r5/author_YM_C2_closing.py','textbook-r5/author_YM_C3_opening.py','textbook-r5/author_YM_C3_ranges.py','textbook-r5/author_YM_C3_composition.py','textbook-r5/author_YM_C3_inverse_opening.py','textbook-r5/author_YM_C3_inverse_graphs.py','textbook-r5/author_YM_C3_restricted_composites.py','textbook-r5/author_YM_C3_transformations.py','textbook-r5/author_YM_C3_function_exercise.py','textbook-r5/author_YM_C3_geometry_opening.py','textbook-r5/author_YM_C3_geometry_constraints.py','textbook-r5/author_YM_C3_geometry_exercise.py','textbook-r5/author_YM_C3_closing.py','textbook-r5/author_YM_C4_opening.py','textbook-r5/author_YM_C4_arcs.py','textbook-r5/author_YM_C4_trig_graphs.py','textbook-r5/author_YM_C4_graph_deductions.py','textbook-r5/author_YM_C4_exact_angles.py','textbook-r5/author_YM_C4_related_angles.py','textbook-r5/author_YM_C4_ratios.py','textbook-r5/author_YM_C4_identity_intro.py','textbook-r5/author_YM_C4_proofs.py','textbook-r5/author_YM_C4_equations.py','textbook-r5/author_YM_C4_composite_equations.py','textbook-r5/author_YM_C4_progressions.py','textbook-r5/author_YM_C4_principal_values.py','textbook-r5/author_YM_C4_inverse_functions.py','textbook-r5/author_YM_C4_geometry.py','textbook-r5/author_YM_C4_exercise_4_2.py','textbook-r5/author_YM_C4_final.py','textbook-r5/author_YM_C4_summary.py','textbook-r5/author_YM_C5_opening.py','textbook-r5/author_YM_C5_magnitude_units.py','textbook-r5/author_YM_C5_operations.py','textbook-r5/author_YM_C5_displacement_geometry.py','textbook-r5/author_YM_C5_spatial_geometry.py','textbook-r5/author_YM_C5_dot_angles.py','textbook-r5/author_YM_C5_spatial_angles.py','textbook-r5/author_YM_C5_closing.py','textbook-r5/author_YM_C6_opening.py','textbook-r5/author_YM_C6_rules.py','textbook-r5/author_YM_C6_gradients_tangents.py','textbook-r5/author_YM_C6_normals_angles.py','textbook-r5/author_YM_C6_monotonicity.py','textbook-r5/author_YM_C6_rates.py','textbook-r5/author_YM_C6_second_derivatives.py','textbook-r5/author_YM_C6_inflexions.py','textbook-r5/author_YM_C6_stationary_constraints.py','textbook-r5/author_YM_C6_optimisation.py','textbook-r5/author_YM_C6_applied_geometry.py','textbook-r5/author_YM_C6_exam_style.py','textbook-r5/author_YM_C6_closing.py','textbook-r5/author_YM_C7_opening.py','textbook-r5/author_YM_C7_rules.py','textbook-r5/author_YM_C7_constants.py','textbook-r5/author_YM_C7_definite_opening.py','textbook-r5/author_YM_C7_areas.py','textbook-r5/author_YM_C7_horizontal_areas.py','textbook-r5/author_YM_C7_connected_areas.py','textbook-r5/author_YM_C7_improper.py','textbook-r5/author_YM_C7_volume_opening.py','textbook-r5/author_YM_C7_washers.py','textbook-r5/author_YM_C7_motion_opening.py','textbook-r5/author_YM_C7_motion_exercise.py','textbook-r5/author_YM_C7_exercise_advanced.py','textbook-r5/author_YM_C7_closing.py','textbook-r5/author_YM_C8_opening.py','textbook-r5/author_YM_C8_equations.py','textbook-r5/author_YM_C8_graphs.py','textbook-r5/author_YM_C8_inequalities.py','textbook-r5/author_YM_C8_polynomial_division.py','textbook-r5/author_YM_C8_theorems.py','textbook-r5/author_YM_C8_exercise.py','textbook-r5/author_YM_C8_closing.py','textbook-r5/author_YM_C9_opening.py','textbook-r5/author_YM_C9_log_laws.py','textbook-r5/author_YM_C9_log_equations.py','textbook-r5/author_YM_C9_exponential_opening.py','textbook-r5/author_YM_C9_natural_opening.py','textbook-r5/author_YM_C9_natural_equations.py','textbook-r5/author_YM_C9_exponential_graphs.py','textbook-r5/author_YM_C9_log_graphs.py','textbook-r5/author_YM_C9_translations.py','textbook-r5/author_YM_C9_linearisation.py','textbook-r5/author_YM_C9_fitted_models.py','textbook-r5/author_YM_C9_exercise_basic.py','textbook-r5/author_YM_C9_exercise_models.py','textbook-r5/author_YM_C9_closing.py','textbook-r5/author_YM_C10_opening.py','textbook-r5/author_YM_C10_compound_sine.py','textbook-r5/author_YM_C10_compound_cos_tan.py','textbook-r5/author_YM_C10_compound_equations.py','textbook-r5/author_YM_C10_double_opening.py','textbook-r5/author_YM_C10_half_angles_proofs.py','textbook-r5/author_YM_C10_double_equations.py','textbook-r5/author_YM_C10_rform_opening.py','textbook-r5/author_YM_C10_rform_cycles_extrema.py','textbook-r5/author_YM_C10_composite_extrema.py','textbook-r5/author_YM_C10_exercise_examstyle.py','textbook-r5/author_YM_C10_closing.py','textbook-r5/author_YM_C11_opening.py','textbook-r5/author_YM_C11_quotients.py','textbook-r5/author_YM_C11_exponentials.py','textbook-r5/author_YM_C11_logarithms.py','textbook-r5/author_YM_C11_trig_derivatives.py','textbook-r5/author_YM_C11_trig_geometry.py','textbook-r5/author_YM_C11_implicit_opening.py','textbook-r5/author_YM_C11_parametric_opening.py','textbook-r5/author_YM_C11_parametric_geometry.py','textbook-r5/author_YM_C11_parametric_diagrams.py','textbook-r5/author_YM_C11_exercise.py','textbook-r5/author_YM_C11_closing.py','textbook-r5/author_YM_C12_opening.py','textbook-r5/author_YM_C12_curves.py','textbook-r5/author_YM_C12_logarithms.py','textbook-r5/author_YM_C12_log_geometry.py','textbook-r5/author_YM_C12_trig_opening.py','textbook-r5/author_YM_C12_trig_powers.py','textbook-r5/author_YM_C12_reverse_trig.py','textbook-r5/author_YM_C12_trig_regions.py','textbook-r5/author_YM_C12_trapezium_opening.py','textbook-r5/author_YM_C12_trapezium_bias.py','textbook-r5/author_YM_C12_trapezium_regions.py','textbook-r5/author_YM_C12_exercise_basic.py','textbook-r5/author_YM_C12_exercise_advanced.py','textbook-r5/author_YM_C12_examstyle.py','textbook-r5/author_YM_C12_closing.py','textbook-r5/author_YM_C13_opening.py','textbook-r5/author_YM_C13_graph_choices.py','textbook-r5/author_YM_C13_iteration_intro.py','textbook-r5/author_YM_C13_iteration_examples.py','textbook-r5/author_YM_C13_iteration_branches.py','textbook-r5/author_YM_C13_log_power.py','textbook-r5/author_YM_C13_convergence.py','textbook-r5/author_YM_C13_calculus.py','textbook-r5/author_YM_C13_geometry.py','textbook-r5/author_YM_C13_exercise.py','textbook-r5/author_YM_C13_examstyle.py','textbook-r5/author_YM_C13_closing.py','verify_textbook_answers_r5.py','verify_textbook_trig_numeric_r5.py','verify_textbook_vectors_r5.py','verify_textbook_integration_r5.py','verify_textbook_numerical_roots_r5.py','build_textbook_inventory.py','build_textbook_census_r5.py','build_textbook_progress.py','check_repair_r3.py','verify_textbook_r4.py','check_repair_r4.py']

STEPS += [
    'textbook-r5/author_textbook_synthesis_algebra_r5.py',
    'textbook-r5/author_textbook_synthesis_polynomial_r5.py',
    'textbook-r5/author_textbook_synthesis_series_r5.py',
    'textbook-r5/author_textbook_synthesis_functions_r5.py',
    'textbook-r5/author_textbook_synthesis_vectors_r5.py',
    'textbook-r5/author_textbook_synthesis_logs_r5.py',
    'textbook-r5/author_textbook_synthesis_power_diff_r5.py',
    'textbook-r5/author_textbook_synthesis_elementary_diff_r5.py',
    'textbook-r5/author_textbook_synthesis_implicit_param_r5.py',
    'textbook-r5/author_textbook_synthesis_numerical_r5.py',
    'textbook-r5/author_textbook_synthesis_power_integral_r5.py',
    'textbook-r5/author_textbook_synthesis_circular_r5.py',
    'textbook-r5/author_textbook_synthesis_basic_trig_r5.py',
    'textbook-r5/author_textbook_synthesis_advanced_trig_r5.py',
    'textbook-r5/author_textbook_synthesis_retained_facets_r5.py',
    'textbook-r5/author_textbook_synthesis_elementary_integral_r5.py',
    'textbook-r5/author_textbook_synthesis_integration_boundaries_r5.py',
    'build_textbook_synthesis_r5.py',
    'check_textbook_synthesis_r5.py',
    'audit_textbook_completion_r5.py',
    'finalize_textbook_inventory_r5.py',
    'audit_textbook_completion_r5.py',
]

def command(name,args=()):
 p=subprocess.run([sys.executable,str(WB/'tools'/name),*args],cwd=ROOT,capture_output=True,text=True)
 if p.returncode:raise RuntimeError(name+' failed:\n'+p.stdout+'\n'+p.stderr)
 return {'command':[sys.executable,str((WB/'tools'/name).relative_to(ROOT)),*args],'exit_code':p.returncode}

def hashes():
 # All current assembly outputs and evidence images; history, manually maintained
 # narratives and frozen raw derivatives are verified separately by the snapshot.
 paths=[*A.glob('*.json'),*A.glob('*.md'),*(A/'assets').glob('*'),*(WB.parent/'curriculum').glob('*.json'),
        WB/'checks/reviewer-scan-reconciliation.json',WB/'checks/crop-containment.json',
        WB/'checks/repair-r3-validation.json',WB/'checks/repair-r4-validation.json',WB/'checks/repair-r5-part1-validation.json',WB/'checks/repair-r5-textbook-working-validation.json',WB/'checks/r5/vector-independent-checks.json',WB/'checks/r5/integration-independent-checks.json',WB/'checks/r5/numerical-root-independent-checks.json',WB/'checks/textbook-synthesis-validation-r5.json']
 paths=[p for p in paths if p.is_file() and p.name!='analysis-snapshot.json']
 return {str(p.relative_to(ROOT)):digest(p) for p in sorted(paths)}

def run_negative_fixtures(after):
 negative=[]
 for fixture in ['tariff','label','crop','held-reference','alternatives-summed','missing-award-coverage','absolute-evidence','E-without-flag','self-alternative','stale-marking-status','shared-sibling-note','qualifier-without-value','matches-without-method','census-missing-item','inline-answer-page-offset','lost-trig-branch','trig-pole-root','cosine-axis-branch-lost','half-angle-axis-branch-lost','singular-implicit-point','proper-integral-pole','singular-parametric-derivative','nonconstant-primitive-error','exponential-derivative-sign','log-primitive-coefficient','naive-atan-direction','zero-vector-angle','L1-instead-of-magnitude','zero-unit-vector','zero-pair-angle','pair-angle-supplement']:
  if fixture in ['E-without-flag','self-alternative','stale-marking-status','shared-sibling-note','qualifier-without-value','matches-without-method','census-missing-item','inline-answer-page-offset','singular-implicit-point','proper-integral-pole','singular-parametric-derivative','nonconstant-primitive-error','exponential-derivative-sign','log-primitive-coefficient']:
   stage='part1'if fixture in ['E-without-flag','self-alternative','stale-marking-status']else'textbook-working'
   script='check_repair_r5.py';extra=['--stage',stage]
  elif fixture in ['naive-atan-direction','zero-vector-angle','L1-instead-of-magnitude','zero-unit-vector','zero-pair-angle','pair-angle-supplement']:
   script='verify_textbook_vectors_r5.py';extra=[]
  elif fixture in ['lost-trig-branch','trig-pole-root','cosine-axis-branch-lost','half-angle-axis-branch-lost']:
   script='verify_textbook_trig_numeric_r5.py';extra=[]
  else:
   script='check_repair_r4.py'if fixture in ['alternatives-summed','missing-award-coverage','absolute-evidence']else'build_analysis.py';extra=[]
  p=subprocess.run([sys.executable,str(WB/'tools'/script),*extra,'--negative-fixture',fixture],cwd=ROOT,capture_output=True,text=True)
  expected={'tariff':'ordered tariffs','label':'label alignment','crop':'crop containment',
            'held-reference':'held reference is learner-displayable','alternatives-summed':'exclusive alternative awards were summed','missing-award-coverage':'question has neither table nor recorded absence','absolute-evidence':'absolute evidence path','E-without-flag':'E row lacks establishes_given_result flag','self-alternative':'main answer repeated as alternative','stale-marking-status':'marking_rule_status disagrees with linked rows','shared-sibling-note':'item note shared with a sibling','qualifier-without-value':'qualifier applied with no quoted value','matches-without-method':'answer matches with no method','census-missing-item':'census entry has no inventory record','inline-answer-page-offset':'inline answer printed-page mismatch','lost-trig-branch':'composite root-count discrepancy','trig-pole-root':'symbolic answer contains original pole','cosine-axis-branch-lost':'composite root-count discrepancy','half-angle-axis-branch-lost':'composite root-count discrepancy','singular-implicit-point':'singular implicit candidate needs branch analysis','proper-integral-pole':'proper integral crosses original discontinuity','singular-parametric-derivative':'singular parametric derivative needs branch analysis','nonconstant-primitive-error':'source primitive has a nonconstant error','exponential-derivative-sign':'source exponential derivative has the wrong sign','log-primitive-coefficient':'source log primitive has the wrong coefficient','naive-atan-direction':'independent vector discrepancy','zero-vector-angle':'zero vector has no direction','L1-instead-of-magnitude':'independent vector discrepancy','zero-unit-vector':'zero vector cannot be normalised','zero-pair-angle':'zero vector has no between-vector angle','pair-angle-supplement':'independent between-vector angle discrepancy'}[fixture]
  assert p.returncode!=0 and 'AssertionError' in p.stderr and expected in p.stderr,(fixture,'seeded negative failed for expected reason',p.stdout,p.stderr)
  assert hashes()==after,('failed build modified outputs',fixture)
  negative.append({'fixture':fixture,'exit_code':p.returncode,'last_error':p.stderr.strip().splitlines()[-1],
                   'unchanged_output_hashes':True})
 for fixture,expected in [
     ('unknown-member','unknown textbook member'),
     ('lost-connected-response','unknown connected source response'),
     ('unsupported-family-demand','unsupported textbook family demand'),
     ('forged-response-exclusion','unwarranted response exclusion'),
 ]:
  p=subprocess.run([sys.executable,str(WB/'tools/check_textbook_synthesis_r5.py'),'--negative-fixture',fixture],cwd=ROOT,capture_output=True,text=True)
  assert p.returncode!=0 and 'AssertionError' in p.stderr and expected in p.stderr,(fixture,'seeded synthesis error did not fail for expected reason',p.stdout,p.stderr)
  assert hashes()==after,('failed synthesis check modified outputs',fixture)
  negative.append({'fixture':fixture,'exit_code':p.returncode,'last_error':p.stderr.strip().splitlines()[-1],'unchanged_output_hashes':True})
 for fixture,expected in [
     ('missing-volume-axis','missing applicable qualifier record'),
     ('explicit-as-implicit','explicit item incorrectly classified as implicit/parametric geometry'),
     ('unresolved-family-response','unresolved source family responses'),
 ]:
  p=subprocess.run([sys.executable,str(WB/'tools/audit_textbook_completion_r5.py'),'--negative-fixture',fixture],cwd=ROOT,capture_output=True,text=True)
  assert p.returncode!=0 and 'AssertionError'in p.stderr and expected in p.stderr,(fixture,'seeded completion error did not fail for expected reason',p.stdout,p.stderr)
  assert hashes()==after,('failed completion check modified outputs',fixture)
  negative.append({'fixture':fixture,'exit_code':p.returncode,'last_error':p.stderr.strip().splitlines()[-1],'unchanged_output_hashes':True})
 return negative

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--single-rebuild',action='store_true',help='Refresh the author checkout once; never reports a deterministic double pass.');args=parser.parse_args()
 first=[command(step) for step in STEPS]+[command('check_repair_r5.py',['--stage','part1']),command('check_repair_r5.py',['--stage','textbook-working'])];before=hashes()
 if args.single_rebuild:
  result={'status':'one author-checkout rebuild passed; not a double-rebuild proof','commands':first,'output_hashes':before}
  write(WB/'checks/r5/single-rebuild-final.json',result)
  print(json.dumps({'single_rebuild':'pass','commands':len(first),'outputs':len(before)},indent=2));return
 diagnostic_before={p: (ROOT/p).read_bytes()for p in before if Path(p).name in ['textbook-answer-verification-r5.json','textbook-inventory.json','integration-independent-checks.json']}
 second=[command(step) for step in STEPS]+[command('check_repair_r5.py',['--stage','part1']),command('check_repair_r5.py',['--stage','textbook-working'])];after=hashes()
 changes=[p for p in sorted(set(before)|set(after)) if before.get(p)!=after.get(p)]
 if changes:
  diagnostic=WB/'checks/r5/rebuild-drift';diagnostic.mkdir(parents=True,exist_ok=True)
  for path in changes:
   if path in diagnostic_before:
    (diagnostic/(Path(path).stem+'-first.json')).write_bytes(diagnostic_before[path])
    (diagnostic/(Path(path).stem+'-second.json')).write_bytes((ROOT/path).read_bytes())
  write(diagnostic/'manifest.json',{'changed_paths':changes,'first_hashes':{p:before.get(p)for p in changes},'second_hashes':{p:after.get(p)for p in changes},'limitation':'Failed reproducibility check;diagnostic copies do not constitute a passed rebuild.'})
 assert not changes,('nondeterministic outputs',changes)
 negative=run_negative_fixtures(after)
 write(WB/'checks/rebuild-verification.json',{'first_rebuild':first,'second_rebuild':second,
       'outputs_compared':len(after),'identical':True,'changed_paths':changes,
       'output_hashes':after,'seeded_negative_results':negative,
       'limits':'Deterministic author assembly and structural regression checks; no independent educational, marking, runtime or production acceptance.'})
 print(json.dumps({'rebuilds':'2 passed','outputs_byte_identical':len(after),'negative_fixtures_rejected':len(negative)},indent=2))
if __name__=='__main__':main()
