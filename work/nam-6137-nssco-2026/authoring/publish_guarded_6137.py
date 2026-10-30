"""Fail-closed Geography publication. Default is a read-only preflight.

Only --publish writes publish/nam-6137-nssco-2026. No network operations.
See HANDOVER-6137-all-visuals.md for the review/manifest interface.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys

W = Path(__file__).resolve().parents[1]
ROOT = W.parents[1]


def read(path):
    return json.loads(path.read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def local(path):
    p = (W / path).resolve()
    if not p.is_relative_to(W) or not p.is_file():
        raise ValueError('Missing or out-of-workspace file: ' + str(path))
    return p


def snapshot():
    """Exact content reviewed; excludes mutable reports and renderer scripts."""
    paths = list((W / 'curriculum').glob('*'))
    paths += list((W / 'planning').glob('*.json'))
    paths += list(W.glob('*profile.yaml'))
    paths += list(W.glob('PLAN-*.md'))
    for td in (W / 'topics').iterdir():
        paths += [td / n for n in ['contract.json', 'work_order.json', 'authoring_notes.json']]
        for folder in ['claims', 'content-units', 'learning-items']:
            paths += list((td / folder).glob('*.json'))
        paths += list(td.glob('*.md'))
    return {str(p.relative_to(W)): sha(p) for p in sorted(set(paths)) if p.is_file()}


def preflight():
    errors = []
    items, expected, notes = {}, {}, []
    block_hashes = {}
    for td in sorted((W / 'topics').iterdir()):
        wo = read(td / 'work_order.json')
        for s in wo['item_slots'] + wo['performance_tasks']:
            expected[s['slot']] = s
        for i in read(td / wo['output_files']['learning_items'])['items']:
            if i['item_id'] in items:
                errors.append('Duplicate item: ' + i['item_id'])
            items[i['item_id']] = i
        q = read(td / 'qa_report.json')
        if q.get('release_decision') != 'publish' or any(c['status'] == 'fail' for c in q['deterministic_checks']):
            errors.append('Failed topic: ' + td.name)
        notes.append(td / wo['output_files']['notes'])
        for u in wo['content_units']:
            unit = read(td / u['file'])
            block_hashes.update({b['block_id']: hashlib.sha256(json.dumps(b, sort_keys=True, ensure_ascii=False).encode()).hexdigest() for b in unit['blocks']})
            count = sum(len(b['text'].split()) for b in unit['blocks'])
            if not unit['word_budget']['min'] <= count <= unit['word_budget']['max']:
                errors.append('Section budget: ' + str(td / u['file']))
    if len(expected) != 801 or set(expected) != set(items):
        errors.append('Expected exactly all 801 approved slots once')
    for iid in set(items) & set(expected):
        for key in ['subtype', 'assessment_objectives', 'blooms_level', 'command_word', 'mark_tariff', 'item_type']:
            if key in expected[iid] and items[iid].get(key) != expected[iid][key]:
                errors.append('Slot label mismatch: ' + iid + '/' + key)
        if re.search(r'VISUAL PENDING|PROVISIONAL PHOTO|Provisional scene-matched', json.dumps(items[iid]), re.I):
            errors.append('Unresolved stimulus: ' + iid)
    plan = read(W / 'planning/visual-resource-plan-6137.json')['resources']
    resources = {r['resource_id']: r for r in plan}
    mp = W / 'assets/asset-manifest-6137.json'
    if not mp.exists():
        errors.append('Missing assets/asset-manifest-6137.json')
        return errors, []
    manifest = read(mp)
    actual = {r['resource_id']: r for r in manifest['resources']}
    if len(actual) != len(manifest['resources']) or set(actual) != set(resources):
        errors.append('Manifest must cover exactly the active visual plan without duplicates')
    for rid, spec in resources.items():
        try:
            r = actual[rid]
            for key in ['question_path', 'answer_path', 'master_path', 'data_spec_path']:
                if r[key] != spec[key]:
                    raise ValueError('Path differs from approved plan: ' + key)
            for rel, digest in r['file_hashes'].items():
                if sha(local(rel)) != digest:
                    raise ValueError('Asset hash mismatch: ' + rel)
            required_paths = [spec[k] for k in ['question_path', 'answer_path', 'master_path', 'data_spec_path'] if spec[k] is not None]
            if 'photo' in spec['kind'].lower():
                required_paths += ['assets/masters/' + spec['assigned_item_id'] + '.svg', 'assets/specs/' + spec['assigned_item_id'] + '.json']
            if not all(p in r['file_hashes'] for p in required_paths):
                raise ValueError('Missing required file hashes')
            review = r['independent_review']
            if review['reviewer'] != 'Codex' or review['verdict'] != 'accept' or review['file_hashes'] != r['file_hashes']:
                raise ValueError('Independent image acceptance absent or stale')
            local(review['report_path'])
            bound_ids = {b['item_id'] for b in manifest['item_bindings'] if b['resource_id'] == rid}
            current_items = {iid: hashlib.sha256(json.dumps(items[iid], sort_keys=True, ensure_ascii=False).encode()).hexdigest() for iid in sorted(bound_ids)}
            if review.get('item_hashes') != current_items:
                raise ValueError('Reviewed card text absent or stale')
            if not review.get('notes_block_hashes') or any(block_hashes.get(bid) != digest for bid, digest in review['notes_block_hashes'].items()):
                raise ValueError('Reviewed notes text absent or stale')
            if 'photo' in spec['kind'].lower():
                licence = r['licence']
                if not all(licence.get(k) for k in ['source_url', 'creator', 'licence_url', 'attribution', 'derivative_permission']):
                    raise ValueError('Incomplete photo provenance/permission record')
        except (KeyError, ValueError) as exc:
            errors.append(rid + ': ' + str(exc))
    bindings = manifest.get('item_bindings', [])
    seen = set()
    for b in bindings:
        try:
            key = (b['item_id'], b['resource_id'])
            if key in seen or b['item_id'] not in items or b['resource_id'] not in resources:
                raise ValueError('Duplicate or unknown item/resource binding')
            seen.add(key)
            r = actual[b['resource_id']]
            for k, field in [('question_path', 'prompt'), ('answer_path', 'canonical_answer')]:
                p = local(b[k])
                if str(p.relative_to(W)) not in r['file_hashes']:
                    raise ValueError('Unhashed image variant')
                links = re.findall(r'!\[[^\]]*\]\(([^)]+)\)', items[b['item_id']][field])
                td = W / 'topics' / b['item_id'].split('-')[2]
                if not any((td / 'learning-items' / link).resolve() == p for link in links):
                    raise ValueError('Card does not link actual ' + field + ' image')
            if b.get('yyeni_asset_id') is not None:
                raise ValueError('YYeni asset IDs must remain empty before import')
        except (KeyError, ValueError) as exc:
            errors.append('Binding: ' + str(exc))
    required = {(r['assigned_item_id'], r['resource_id']) for r in plan}
    for td in (W / 'topics').iterdir():
        n = read(td / 'authoring_notes.json')
        required |= {(r['item_id'], r['resource_id']) for r in n.get('visual_reuses', [])}
        for concern in n.get('scope_concerns', []):
            resolution = concern.get('resolution', {})
            if resolution.get('approved_by') != 'Vitalis P Haupindi' or not resolution.get('approval_evidence'):
                errors.append('Unapproved map-plan concern: ' + td.name)
            for iid in concern['affected_items']:
                if not any(b['item_id'] == iid for b in bindings):
                    errors.append('Map-stimulus binding absent: ' + iid)
        for iid, spec in n.get('performance_parts', {}).items():
            if spec.get('assets_required') and not any(b['item_id'] == iid for b in bindings):
                errors.append('Practical stimulus binding absent: ' + iid)
    for pair in sorted(required - seen):
        errors.append('Missing binding: ' + str(pair))
    linked = set()
    for p in notes:
        for rel in re.findall(r'!\[[^\]]*\]\(([^)]+)\)', p.read_text()):
            target = (p.parent / rel).resolve()
            if not target.is_relative_to(W) or not target.is_file():
                errors.append('Broken notes image: ' + str(p) + '/' + rel)
            else:
                linked.add(str(target.relative_to(W)))
    for r in actual.values():
        if r['answer_path'] not in linked:
            errors.append('Answer image missing from teaching notes: ' + r['resource_id'])
    rp = W / 'review/subject-acceptance-6137.json'
    if not rp.exists():
        errors.append('Independent whole-subject acceptance not recorded')
    else:
        r = read(rp)
        if r.get('reviewer') != 'Claude' or r.get('verdict') != 'publish' or r.get('source_hashes') != snapshot() or r.get('manifest_sha256') != sha(mp):
            errors.append('Whole-subject acceptance absent or stale')
        local(r['report_path'])
    return errors, bindings


def main():
    ap = argparse.ArgumentParser(__doc__)
    ap.add_argument('--publish', action='store_true')
    args = ap.parse_args()
    # Refresh deterministic reports, not just their previous decisions, before writing.
    if args.publish:
        for td in sorted((W / 'topics').iterdir()):
            result = subprocess.run([sys.executable, str(ROOT / 'standard/v0.2.0-draft/checks/run_checks.py'), str(W), td.name], cwd=ROOT, capture_output=True, text=True)
            if not (td / 'qa_report.json').is_file():
                raise ValueError('Check tool did not produce a report: ' + result.stderr)
        result = subprocess.run([sys.executable, str(W / 'authoring/audit_authored_6137.py')], cwd=ROOT, capture_output=True, text=True)
        if result.returncode or read(W / 'authoring/draft-audit-6137.json')['result'] != 'DRAFTS_RECONCILE':
            raise ValueError('Live full-subject audit failed: ' + result.stderr)
        result = subprocess.run([sys.executable, str(ROOT / 'operations/tools/check_copied_wording.py'), str(W), str(W / 'assessment-evidence/extracted')], cwd=ROOT, capture_output=True, text=True)
        if result.returncode:
            raise ValueError('Live copied-wording check failed: ' + result.stdout)
    errors, bindings = preflight()
    if errors:
        print('NOT READY: ' + str(len(errors)) + ' publication blockers')
        print('\n'.join(errors))
        return 1
    print('Preflight passed; ' + str(len(bindings)) + ' exact item-image bindings')
    if not args.publish:
        return 0
    subprocess.run([sys.executable, str(ROOT / 'standard/v0.2.0-draft/build/publish_subject.py'), str(W)], cwd=ROOT, check=True)
    out = ROOT / 'publish' / W.name
    for rel in read(W / 'assets/asset-manifest-6137.json')['resources']:
        for name in rel['file_hashes']:
            p = local(name)
            target = out / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, target)
    # Rebase source-relative image references to each published file location.
    from os.path import relpath
    for p in list((out / 'notes').glob('*.md')) + list((out / 'flashcards').glob('*.json')):
        text = p.read_text()
        source_dir = W / 'topics' / p.name.split('-')[0]
        if p.suffix == '.json':
            source_dir /= 'learning-items'
        def rebase(match):
            target = (source_dir / match[2]).resolve()
            return match[1] + relpath(out / target.relative_to(W), p.parent) + ')'
        text = re.sub(r'(!\[[^\]]*\]\()([^)]+)\)', rebase, text)
        p.write_text(text)
    saved = [i for p in (out / 'flashcards').glob('*.json') for i in read(p)['items']]
    if len(saved) != 801 or len({i['item_id'] for i in saved}) != 801:
        raise ValueError('Published count/IDs mismatch')
    sidecar = {'workspace': W.name, 'items': bindings, 'upload_status': 'not uploaded; import requires separate approval'}
    (out / 'IMAGE-SIDECAR.json').write_text(json.dumps(sidecar, indent=2) + '\n')
    print('Published locally; no upload/import/Git operations performed')
    return 0


if __name__ == '__main__':
    sys.exit(main())
