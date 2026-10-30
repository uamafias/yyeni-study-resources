"""Insert the current SHA-256 table into a resource checklist and confirm it matches the check report.

    python3 work/nam-6137-nssco-2026/assets/code/finalise.py <ITEM-ID>

The checklist is written by hand (the visual and semantic review); this only fills the block between
<!-- hashes --> and <!-- /hashes --> so the recorded hashes are never typed.
"""
import json
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import ASSETS, WS, sha  # noqa: E402

item = sys.argv[1]
rep = json.load(open(os.path.join(ASSETS, 'checks', item + '.json')))
extra = json.load(open(os.path.join(ASSETS, 'records', rep['resource_id'] + '.json'))).get('extra_files', []) \
    if os.path.exists(os.path.join(ASSETS, 'records', rep['resource_id'] + '.json')) else []
files = list(rep['sha256']) + [p for p in extra if p not in rep['sha256']]
rows = ['| File | SHA-256 |', '|---|---|']
for p in files:
    h = sha(os.path.join(WS, p))
    if p in rep['sha256'] and rep['sha256'][p] != h:
        sys.exit('stale check report for ' + p + ': re-run the resource build')
    rows.append('| `%s` | `%s` |' % (p, h))
cp = os.path.join(ASSETS, 'checklists', item + '.md')
text = open(cp).read()
a, b = text.index('<!-- hashes -->'), text.index('<!-- /hashes -->')
open(cp, 'w').write(text[:a] + '<!-- hashes -->\n' + '\n'.join(rows) + '\n' + text[b:])
print('hashes written to', os.path.relpath(cp, WS), '; automated checks passed:', rep['passed'])
