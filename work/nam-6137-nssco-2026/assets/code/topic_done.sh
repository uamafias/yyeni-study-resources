#!/bin/sh
# Restamp, render and check one topic after its visual resources are linked.
#   sh work/nam-6137-nssco-2026/assets/code/topic_done.sh <TOPIC> "<repair note>"
set -e
cd "$(dirname "$0")/../../../.."
WSP=work/nam-6137-nssco-2026
python3 operations/tools/restamp.py $WSP "$1" --note "$2"
python3 standard/v0.2.0-draft/build/render_notes.py $WSP "$1" | tail -2
python3 standard/v0.2.0-draft/checks/run_checks.py $WSP "$1" > /dev/null 2>&1 || true
python3 - "$WSP/topics/$1/qa_report.json" <<'PY'
import json, sys
q = json.load(open(sys.argv[1]))
st = {}
for c in q['deterministic_checks']:
    st.setdefault(c['status'], []).append(c.get('check_id') or c.get('id'))
print('decision:', q.get('release_decision'), {k: (len(v) if k == 'pass' else v) for k, v in st.items()})
PY
