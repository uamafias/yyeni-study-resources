"""Write assets/asset-manifest-6137.json from the per-resource records, check reports and the approved plan.

    python3 work/nam-6137-nssco-2026/assets/code/build_manifest.py

Each resource carries the four planned paths exactly as the plan states them (null for the licensed
photographs' master/spec), file_hashes for every file the resource produced (master, spec, every image
side and variant, and the photo original and display copy), its code and checklist paths, and, for
photographs, the licence record. No independent_review is written: Codex adds it after inspection.
Bindings list every assigned target, recorded reuse and package variant; yyeni_asset_id stays null.
"""
import json
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import ASSETS, WS, sha  # noqa: E402

plan = json.load(open(os.path.join(WS, 'planning', 'visual-resource-plan-6137.json')))['resources']
manifest_path = os.path.join(ASSETS, 'asset-manifest-6137.json')
previous_manifest = json.load(open(manifest_path)) if os.path.isfile(manifest_path) else {}
previous = {r['resource_id']: r for r in previous_manifest.get('resources', [])}
resources, bindings = [], []
for pe in plan:
    rid = pe['resource_id']
    rec = json.load(open(os.path.join(ASSETS, 'records', rid + '.json')))
    rep = json.load(open(os.path.join(ASSETS, 'checks', pe['assigned_item_id'] + '.json')))
    files = list(rep['sha256']) + [p for p in rec.get('extra_files', []) if p not in rep['sha256']]
    for b in rec['bindings']:
        files += [p for p in (b['question_path'], b['answer_path']) if p not in files]
    entry = {'resource_id': rid, 'topic_id': pe['topic_id'], 'kind': pe['kind'], 'assigned_item_id': pe['assigned_item_id'],
             'question_path': pe['question_path'], 'answer_path': pe['answer_path'],
             'master_path': pe['master_path'], 'data_spec_path': pe['data_spec_path'],
             'file_hashes': {p: sha(os.path.join(WS, p)) for p in files},
             'code_paths': rec['code_paths'], 'checklist_path': rec['checklist_path'], 'check_report_path': rec['check_report_path'],
             'automated_checks_passed': rep['passed'], 'status': rec['status']}
    if rec.get('licence'):
        lic = dict(rec['licence'])
        lic['derivative_permission'] = 'Permitted by %s (%s). %s.' % (lic['licence'], lic['licence_url'], lic['derivative_terms'])
        lic['original_sha256'] = sha(os.path.join(WS, [p for p in rec['extra_files'] if p.endswith('_original.jpg')][0]))
        entry['licence'] = lic
    if rec.get('notes'):
        entry['notes'] = rec['notes']
    old_review = previous.get(rid, {}).get('independent_review')
    if old_review and old_review.get('file_hashes') == entry['file_hashes']:
        entry['independent_review'] = old_review
        entry['status'] = 'reviewed by Codex; accept'
    resources.append(entry)
    for b in rec['bindings']:
        bindings.append({'item_id': b['item_id'], 'resource_id': rid, 'question_path': b['question_path'],
                         'answer_path': b['answer_path'], 'yyeni_asset_id': None})
out = {'subject': '6137 NSSCO Geography', 'generated_by': 'assets/code/build_manifest.py',
       'author': previous_manifest.get('author', 'Claude (visual author); per-resource independent review records are authoritative'),
       'resources': resources, 'item_bindings': bindings}
p = os.path.join(WS, 'assets', 'asset-manifest-6137.json')
json.dump(out, open(p, 'w'), indent=1, ensure_ascii=False)
open(p, 'a').write('\n')
print('resources', len(resources), 'bindings', len(bindings), 'files', sum(len(r['file_hashes']) for r in resources))
