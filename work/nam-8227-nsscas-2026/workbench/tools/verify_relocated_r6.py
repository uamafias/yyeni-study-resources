"""Rebuild R6 in an independent directory; never copy generated data back."""
import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from analysis_sources import A, WB, ROOT, digest, write


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--diagnostic', action='store_true')
    parser.add_argument('--keep-copy', action='store_true')
    args = parser.parse_args()
    temporary = Path(tempfile.mkdtemp(prefix='8227-r6-relocation-'))
    copy_root = temporary / 'resources'
    copy_wb = copy_root / WB.relative_to(ROOT)
    shutil.copytree(WB.parent, copy_wb.parent,
                    ignore=shutil.ignore_patterns('__pycache__', '.DS_Store'))
    baseline = json.loads((WB / 'checks/repair-r6-baseline.json').read_text())
    sources = dict(baseline['source_files'])
    for record in json.loads((A / 'source-holdings.json').read_text())['records']:
        if record.get('sha256') and (ROOT / record['path']).is_file():
            assert record['path'] not in sources or sources[record['path']] == record['sha256']
            sources[record['path']] = record['sha256']
    for relative, sha in sources.items():
        source = ROOT / relative
        assert digest(source) == sha, ('source changed', relative)
        target = copy_root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        try:
            os.link(source, target)
        except OSError:
            shutil.copy2(source, target)
    print(f'Fresh R6 workspace: {temporary}; {len(sources)} immutable source hashes checked.', flush=True)
    log_path = temporary / 'rebuild.log'
    command = [sys.executable, str(copy_wb / 'tools/run_repair_r6.py')]
    if args.diagnostic:
        command += ['--diagnostic', '--single-rebuild']
    with log_path.open('w') as log:
        process = subprocess.Popen(command, cwd=copy_root, stdout=log, stderr=subprocess.STDOUT, text=True)
        print(f'Rebuild PID {process.pid}; progress log: {log_path}', flush=True)
        code = process.wait()
    assert code == 0, ('fresh-copy rebuild failed', str(log_path), log_path.read_text()[-6000:])
    if args.diagnostic:
        check = json.loads((copy_wb / 'checks/r5/single-rebuild-final.json').read_text())
        report = dict(status='diagnostic single rebuild passed; not a final R6 proof',
            source_files_hash_checked=len(sources), commands=len(check['commands']),
            outputs=len(check['output_hashes']), matches_author_checkout='not checked in diagnostic mode',
            full_double_rebuild=False, old_negative_fixtures='not run in single diagnostic rebuild')
        write(WB / 'checks/r6/relocation-diagnostic.json', report)
    else:
        check = json.loads((copy_wb / 'checks/rebuild-verification.json').read_text())
        r6 = json.loads((copy_wb / 'checks/r6/working-validation.json').read_text())
        assert check['identical'] and len(check['seeded_negative_results']) == 38
        assert r6['status'].startswith('author final structural checks pass')
        assert len(r6['negative_fixtures']) >= 11
        mismatches = [p for p, sha in check['output_hashes'].items()
                      if not (ROOT / p).is_file() or digest(ROOT / p) != sha]
        assert not mismatches, ('fresh-copy differs from author outputs', mismatches)
        report = dict(status='pass', source_files_hash_checked=len(sources),
            workspace_copy='independent directory; no source-path edits', double_rebuild=True,
            commands_per_run=len(check['first_rebuild']), outputs_compared=check['outputs_compared'],
            matches_author_checkout=True, previous_seeded_errors_rejected=38,
            r6_seeded_errors_rejected=len(r6['negative_fixtures']),
            limits='Author reproducibility and structural regression checks on this macOS host; not independent educational review or application acceptance.')
        write(WB / 'checks/fresh-copy-verification-r6.json', report)
        write(A / 'history/rebuild-verification-r6-final-fresh-copy.json', check)
    print(json.dumps(report, indent=2), flush=True)
    if args.keep_copy:
        print(f'Copy retained: {temporary}', flush=True)
    else:
        shutil.rmtree(temporary)


if __name__ == '__main__':
    main()
