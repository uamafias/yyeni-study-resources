"""Freeze the completed R6 author handback only after the fresh-copy proof."""
import argparse
import json
import platform
import subprocess
from analysis_sources import A, WB, ROOT, digest, write
from verify_r6_preservation import verify


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    target = A / 'analysis-snapshot.json'
    if args.check:
        snapshot = json.loads(target.read_text())
        assert snapshot['snapshot_version'] == '8227-analysis-r6'
        for group in ['files', 'source_files', 'review_files']:
            for path, sha in snapshot[group].items():
                assert digest(ROOT / path) == sha, (group, path, 'hash mismatch')
        print(json.dumps(dict(snapshot='all R6 hashes match',
            files=len(snapshot['files']), sources=len(snapshot['source_files']),
            review_files=len(snapshot['review_files'])), indent=2))
        return
    preservation = verify(save=False)
    inputs=json.loads((WB/'checks/r6/fresh-build-input-manifest.json').read_text())
    assert inputs['status']=='pass' and inputs['identical_across_both_fresh_copies_and_author']
    for path,sha in inputs['sha256'].items():
        assert digest(ROOT/path)==sha,('pipeline input changed after proof',path)
    fresh = json.loads((WB / 'checks/fresh-copy-verification-r6.json').read_text())
    proof = json.loads((A / 'history/rebuild-verification-r6-final-fresh-copy.json').read_text())
    assert fresh['status'] == 'pass' and fresh['double_rebuild'] and fresh['matches_author_checkout']
    assert proof['identical'] and len(proof['seeded_negative_results']) == 38
    for path, sha in proof['output_hashes'].items():
        assert digest(ROOT / path) == sha, ('assembled output changed after fresh-copy proof', path)
    validation = json.loads((WB / 'checks/r6/working-validation.json').read_text())
    assert validation['status'].startswith('author final structural checks pass')
    assert len(validation['negative_fixtures']) >= 11
    baseline = json.loads((WB / 'checks/repair-r6-baseline.json').read_text())
    paths = [p for p in WB.parent.rglob('*') if p.is_file() and p != target
             and 'review' not in p.relative_to(WB.parent).parts and '__pycache__' not in p.parts
             and p.name != '.DS_Store']
    paths += [ROOT / p for p in ['AGENTS.md', 'TEAM-PLAYBOOK.md', 'BLOOM-CLASSIFICATION.md',
        'workbench/playbook/README.md', 'workbench/playbook/quality.md',
        'workbench/playbook/templates.md', 'workbench/playbook/textbook-analysis.md']]
    files = {str(p.relative_to(ROOT)): digest(p) for p in sorted(set(paths))}
    reviews = {path: digest(ROOT / path) for path in baseline['review_file_hashes']}
    write(target, dict(snapshot_version='8227-analysis-r6', date='2026-11-22',
        status='author repair complete; focused Claude cross-vendor check required; independent acceptance pending',
        resource_git_head=subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
        scope='Revised round6 source-analysis repair only. No step3 PLAN, contract, recipes, runtime generators, work orders, imports or learner assignment.',
        history=dict(path=str((A / 'history/analysis-snapshot-r5.json').relative_to(ROOT)),
                     sha256=preservation['r5_snapshot_sha256']),
        files=files, source_files=baseline['source_files'], review_files=reviews,
        environment=dict(python=platform.python_version(), macos=platform.mac_ver()[0]),
        checks=['checks/fresh-copy-verification-r6.json', 'checks/r6/preservation-verification.json',
                'checks/r6/working-validation.json', 'checks/repair-r6-report.md'],
        verification_levels=dict(structural='author deterministic double rebuild in a fresh directory, 38 prior and at least11R6 seeded errors rejected',
            content='source/render author evidence and retained accepted R5 population; specific limits in repair report',
            independent_review='R6 awaits focused Claude check; same-model parallel author assistance is not cross-vendor review',
            owner='binding owner decisions preserved; no final resource or production acceptance claimed',
            app_and_production='not tested, published, installed, imported or assigned')))
    print(json.dumps(dict(frozen_files=len(files), sources=len(baseline['source_files']),
                          review_files=len(reviews), snapshot_sha256=digest(target)), indent=2))


if __name__ == '__main__':
    main()
