#!/usr/bin/env python3
"""Merge a semantic review into a topic's qa_report, with a written resolution per issue.

    python3 ingest_review.py <workspace> <topic_id> <review.yaml> [resolutions.json]

Ingesting a review was a hand edit until 2026-09-12, which is how review R3 came to be
answered in the artefacts while the qa report still showed only R1 and R2. At ~3 000 topic
builds a hand edit is a defect generator, so it is a script.

An issue is marked resolved only where the resolutions file gives a reason of at least 12
words saying what changed. Everything else stays open, which is what RS-42 counts against
the release bar. Resolution is the author's claim, never a verdict: run_checks still holds
the build for re-review (RS-28).
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yyeni_checks import _json, _yaml  # noqa: E402

MIN_WORDS = 12


def main():
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    ws, topic, review_path = sys.argv[1], sys.argv[2], sys.argv[3]
    res = _json(sys.argv[4]) if len(sys.argv) > 4 else {}
    review = _yaml(review_path)
    qa_path = os.path.join(ws, 'topics', topic, 'qa_report.json')
    qa = _json(qa_path)

    rid = review.get('review_id')
    if not rid:
        sys.exit('The review file has no review_id.')

    issues = []
    for i in review.get('issues', []):
        iid = i.get('issue_id')
        out = {k: i.get(k) for k in ('issue_id', 'severity', 'category', 'affected_ids', 'finding',
                                     'educational_consequence', 'recommended_repair', 'confidence')
               if i.get(k) is not None}
        reason = (res.get(iid) or '').strip()
        if reason:
            if len(reason.split()) < MIN_WORDS:
                sys.exit('%s: a resolution must say what changed - %d words is not a reason.'
                         % (iid, len(reason.split())))
            out['status'] = 'resolved'
            out['resolution'] = reason
        else:
            out['status'] = i.get('status', 'open')
        issues.append(out)

    entry = {'review_id': rid, 'reviewer_role': review.get('reviewer_role', 'combined'),
             'status': review.get('status', 'reject'),
             'packet_hash_verified': review.get('packet_hash_verified'),
             'coverage_confirmed': review.get('coverage_confirmed'),
             'reconstruction_test': review.get('reconstruction_test'),
             'source': os.path.relpath(review_path, ws if os.path.isabs(review_path) else '.'),
             'issues': issues}

    reviews = [r for r in qa.get('semantic_reviews', []) if r.get('review_id') != rid
               and r.get('status') != 'not_run']
    reviews.append(entry)
    qa['semantic_reviews'] = reviews
    json.dump(qa, open(qa_path, 'w'), indent=2, ensure_ascii=False)

    n_open = sum(1 for i in issues if i['status'] not in ('resolved', 'rejected'))
    blocking = sum(1 for i in issues
                   if i['status'] not in ('resolved', 'rejected') and i['severity'] in ('critical', 'high'))
    print('%s ingested: %d issues, %d resolved, %d open (%d blocking under RS-42).'
          % (rid, len(issues), len(issues) - n_open, n_open, blocking))
    print('Re-run run_checks.py to recompute the release decision.')


if __name__ == '__main__':
    main()
