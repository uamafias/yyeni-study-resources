"""Repeat the scoped R6 working build; this is not final relocated validation."""
import json
import subprocess
import sys
from analysis_sources import A,WB,ROOT,digest,write


COMMANDS=['build_textbook_synthesis_r5.py','build_textbook_exam_candidates_r6.py',
          'build_objective_problem_map_r6.py','apply_textbook_figures_r6.py','check_textbook_family_prose_parallel_r6.py','check_textbook_figures_r6.py','check_repair_r6.py']
OUTPUTS=['textbook-families.json','textbook-families.md','textbook-insights.md',
         'textbook-exam-candidates-r6.json','objective-problem-map.json',
         'objective-problem-map.md','textbook-figure-comparisons-r6.json','textbook-figure-comparisons-r6.md']
TOOLS=COMMANDS+['textbook_family_repairs_r6.py','textbook_exam_comparison_r6.py',
                'analysis_sources.py','rebuild_working_r6.py',
                'apply_textbook_r6.py','textbook-note-spacing-r6.json','textbook-family-prose-r6.json',
                'textbook-note-spacing-parallel-r6.json','textbook-note-spacing-root-r6.json',
                'apply_textbook_figures_r6.py','textbook-figure-repairs-r6.json',
                'apply_textbook_family_prose_parallel_r6.py','textbook-family-prose-parallel-r6.json',
                'check_repair_r5.py',
                'build_provenance.py','provenance_inputs.py','annotate_provenance_screen_r5.py']
INPUTS=['textbook-inventory.json','question-analysis.json','demand-registry.json','cambridge-evidence.json']


def build():
    rounds=[]
    for n in range(2):
        for name in COMMANDS:
            result=subprocess.run([sys.executable,str(WB/'tools'/name)]+(['--write-comparisons'] if name=='apply_textbook_figures_r6.py' else []),cwd=ROOT,
                                  capture_output=True,text=True)
            assert result.returncode==0,(name,result.stdout,result.stderr)
        rounds.append({name:digest(A/name)for name in OUTPUTS})
        print('Scoped working round',n+1,'passed',flush=True)
    assert rounds[0]==rounds[1],'scoped working rebuild is not deterministic'
    families=json.loads((A/'textbook-families.json').read_text())
    ledger=json.loads((WB/'tools/textbook-exam-relations-r6.json').read_text())
    checks=json.loads((WB/'checks/r6/working-validation.json').read_text())
    result=dict(status='scoped working double rebuild passed; NOT the final fresh-copy full rebuild',
        commands_per_round=COMMANDS,rounds=2,byte_identical_analysis_outputs=rounds[0],
        pair_decisions=len(ledger['relations']),families=len(families['families']),
        ledger_sha256=digest(WB/'tools/textbook-exam-relations-r6.json'),
        analysis_input_sha256={name:digest(A/name)for name in INPUTS},
        tool_sha256={name:digest(WB/'tools'/name)for name in TOOLS},
        new_seeded_errors_rejected=len(checks['negative_fixtures']),
        full_rebuild_and_previous_38_negative_fixtures='not re-run in this checkpoint')
    write(WB/'checks/r6/working-double-rebuild.json',result)
    return result


if __name__=='__main__':build()
