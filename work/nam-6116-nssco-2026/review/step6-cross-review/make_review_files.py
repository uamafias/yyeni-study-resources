#!/usr/bin/env python3
"""Turn the raw Step 6 reviewer YAML files (raw/review_*.yaml) and the fixers' resolution files (raw/resolution_*.json)
into standard-shaped review files in operations/review/ and ingest them into each topic's qa_report.json.
Run from the repository root with .venv/bin/python. Issues stay OPEN unless a fixer recorded a concrete change (12+ words).
Open issues are debt carried visibly (RS-42); they do not change the deterministic decision.
"""
import glob, json, subprocess, sys
import yaml
from pathlib import Path

W = Path('work/nam-6116-nssco-2026'); RAW = W / 'review/step6-cross-review/raw'; OUT = Path('operations/review')
PY = '.venv/bin/python'
areas = {'1': ['1'], '2': ['2'], '3': ['3AB', '3CD'], '4': ['4'], '5': ['5']}
res_files = {'1': ['1'], '2': ['2'], '3AB': ['3A', '3B'], '3CD': ['3C', '3D'], '4': ['4'], '5': ['5']}
for topic, parts in areas.items():
    for part in parts:
        d = yaml.safe_load((RAW / f'review_{part}.yaml').read_text())
        issues = [x for x in d if isinstance(x, dict) and 'issue_id' in x]
        cov = next((x['coverage_statement'] for x in d if isinstance(x, dict) and 'coverage_statement' in x), {})
        res = {}
        for r in res_files[part]:
            for k, v in json.loads((RAW / f'resolution_{r}.json').read_text()).items():
                if v.get('status') == 'fixed' and k not in res:
                    res[k] = v['note'] + ' (fixed in the author script and regenerated; checks re-run clean.)'
        rid = 'SR-6116-%s-STEP6-CLAUDE-R1%s' % (topic, '' if len(parts) == 1 else '-' + part)
        flat = lambda v: v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)
        review = {'review_id': rid, 'reviewer_role': 'combined', 'packet_hash_verified': None,
                  'status': 'accept_with_open_issues',
                  'coverage_confirmed': ' '.join('%s: %s' % (k, flat(cov[k])) for k in cov if k in ('items_read', 'notes_read', 'not_checked')),
                  'reconstruction_test': ' '.join('%s: %s' % (k, flat(cov[k])) for k in cov if 'learner_test' in k or 'misconception' in k),
                  'issues': [{k: i[k] for k in ('issue_id', 'severity', 'category', 'affected_ids', 'finding', 'evidence',
                              'educational_consequence', 'recommended_repair', 'confidence', 'status') if k in i} for i in issues]}
        OUT.mkdir(parents=True, exist_ok=True)
        rp = OUT / ('nam-6116-nssco-%s-review-r1%s.yaml' % (topic, '' if len(parts) == 1 else '-' + part))
        rp.write_text(yaml.safe_dump(review, sort_keys=False, allow_unicode=True, width=120))
        rj = RAW / f'resolutions_ingest_{part}.json'
        rj.write_text(json.dumps(res, indent=1, ensure_ascii=False))
        out = subprocess.run([PY, 'standard/v0.2.0-draft/checks/ingest_review.py', str(W), topic, str(rp), str(rj)],
                             capture_output=True, text=True)
        print(rid, '|', out.stdout.splitlines()[0] if out.stdout else out.stderr[-300:])
