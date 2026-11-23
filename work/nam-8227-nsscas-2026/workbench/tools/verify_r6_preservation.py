"""Verify immutable inputs against the saved R6 baseline and owner revision."""
import json
from analysis_sources import A, WB, ROOT, digest, write


def verify(save=True):
    baseline = json.loads((WB / 'checks/repair-r6-baseline.json').read_text())
    revision = json.loads((WB / 'checks/r6/prompt-revision.json').read_text())
    assert digest(A / 'history/analysis-snapshot-r5.json') == baseline['snapshot_r5_sha256']
    for path, sha in baseline['source_files'].items():
        assert digest(ROOT / path) == sha, ('original source changed', path)
    changed = []
    allowed = {r['path']: r for r in revision['baseline_review_hash_changes']}
    for path, sha in baseline['review_file_hashes'].items():
        current = digest(ROOT / path)
        if current != sha:
            assert path in allowed, ('review input changed without owner revision', path)
            assert sha == allowed[path]['baseline_sha256']
            assert current == allowed[path]['current_sha256']
            changed.append(path)
    assert set(changed) == set(allowed), 'owner revision record no longer matches the review inputs'
    fields = ['item_id', 'assessed_8227_demand_ids', 'component_demand_ids',
              'objective_ids', 'learner_display']
    items = json.loads((A / 'textbook-inventory.json').read_text())['items']
    assert [{k: i[k] for k in fields} for i in items] == json.loads(
        (A / 'history/r6-accepted-item-links-r5.json').read_text()), 'accepted item links changed'
    result = dict(status='pass', source_files_checked=len(baseline['source_files']),
                  baseline_review_files_checked=len(baseline['review_file_hashes']),
                  owner_revised_review_paths=changed, accepted_item_link_projections_preserved=len(items),
                  r5_snapshot_sha256=digest(A / 'history/analysis-snapshot-r5.json'),
                  limitation='Checks the named saved baseline; does not infer educational acceptance from hashes.')
    if save:
        write(WB / 'checks/r6/preservation-verification.json', result)
    return result


if __name__ == '__main__':
    print(json.dumps(verify(), indent=2))
