#!/usr/bin/env python3
"""Run the YYeni deterministic check suite over one topic."""
import sys, os, json, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yyeni_checks import run

ap = argparse.ArgumentParser()
ap.add_argument('workspace', help='path to work/<qualification-workspace>')
ap.add_argument('topic', help='topic id, e.g. 5.2')
ap.add_argument('--out', default=None, help='where to write qa_report.json (default: <workspace>/topics/<topic>/qa_report.json)')
ap.add_argument('--quiet', action='store_true')
a = ap.parse_args()

rep = run(a.workspace, a.topic)
out = a.out or os.path.join(a.workspace, 'topics', a.topic, 'qa_report.json')
with open(out, 'w') as fh:
    json.dump(rep, fh, indent=2)

if not a.quiet:
    for c in rep['deterministic_checks']:
        print('%-6s %-8s %s' % (c['check_id'], c['status'].upper(), c['message'][:150]))
    print('\nDECISION: %s   ->  %s' % (rep['release_decision'].upper(), out))
sys.exit(0 if rep['release_decision'] == 'pass' else 1)
