"""Run the established complete pipeline plus the R6 derived analysis checks.

The diagnostic mode is explicitly incomplete. Final mode additionally requires
all R6 author gates; neither mode grants independent educational acceptance.
"""
import argparse
import sys
import run_repair_checks as previous
from analysis_sources import WB, ROOT, digest


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--diagnostic', action='store_true')
    parser.add_argument('--single-rebuild', action='store_true')
    parser.add_argument('--negative-only', action='store_true')
    args = parser.parse_args()
    steps = list(previous.STEPS)
    index = steps.index('build_textbook_synthesis_r5.py') + 1
    steps[index:index] = ['build_textbook_exam_candidates_r6.py',
                          'build_objective_problem_map_r6.py',
                          'apply_textbook_figures_r6.py',
                          'check_textbook_family_prose_parallel_r6.py','check_textbook_figures_r6.py']
    # Retain the established population audit and all 38 negative fixtures.
    # The inherited R5 finalizer describes author population, not acceptance.
    # Final R6 author gates are checked independently below and in each round.
    steps.extend(['check_textbook_answer_pages_r6.py','verify_r6_preservation.py','check_repair_r6.py'])
    previous.STEPS = steps
    original_command = previous.command
    counter = 0

    def command(name, extra=()):
        nonlocal counter
        if name == 'apply_textbook_figures_r6.py':
            extra = ['--write-comparisons']
        if name == 'check_repair_r6.py' and not args.diagnostic:
            extra = [*extra, '--final']
        result = original_command(name, extra)
        counter += 1
        if counter == 1 or counter % 20 == 0 or name == 'check_repair_r6.py':
            print(f'Completed command {counter}: {name}', flush=True)
        return result

    previous.command = command
    original_hashes = previous.hashes

    def hashes():
        result = original_hashes()
        for name in ['working-validation.json', 'comparison-progress.json',
                     'family-membership-changes.json', 'family-membership-unresolved.json',
                     'preservation-verification.json','parallel-families/validation.json',
                     'parallel-figures/checkpoint.json']:
            path = WB / 'checks/r6' / name
            if path.is_file():
                result[str(path.relative_to(ROOT))] = digest(path)
        return result

    previous.hashes = hashes
    if args.negative_only:
        from analysis_sources import write
        negative=previous.run_negative_fixtures(hashes())
        write(WB/'checks/r6/previous-negative-fixtures.json',dict(status='pass',fixtures=negative))
        print(f'{len(negative)} previous seeded errors rejected',flush=True)
        return
    sys.argv = [sys.argv[0]] + (['--single-rebuild'] if args.single_rebuild else [])
    previous.main()
    print('Diagnostic scope only; no final R6 completion proof.' if args.diagnostic
          else 'Full author pipeline passed; focused independent review is still required.', flush=True)


if __name__ == '__main__':
    main()
