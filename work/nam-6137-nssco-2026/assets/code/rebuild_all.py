"""Re-run every resource module, then refresh every checklist hash table.

    python3 work/nam-6137-nssco-2026/assets/code/rebuild_all.py

Rendering is deterministic on this machine (re-runs give byte-identical PNGs), so this is safe after a
toolkit change: any image that changes is reported, and its checklist must then be re-inspected.
"""
import glob
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WS = os.path.dirname(os.path.dirname(HERE))
before = {}
for rep in glob.glob(os.path.join(WS, 'assets', 'checks', 'ITEM-*.json')):
    if rep.endswith('textboxes.json'):
        continue
    before.update(json.load(open(rep)).get('sha256', {}))
failed = []
for mod in sorted(glob.glob(os.path.join(HERE, 'r_*.py'))):
    r = subprocess.run([sys.executable, mod], capture_output=True, text=True)
    if r.returncode or '"passed": true' not in r.stdout:
        failed.append(os.path.basename(mod))
after = {}
for rep in glob.glob(os.path.join(WS, 'assets', 'checks', 'ITEM-*.json')):
    if rep.endswith('textboxes.json'):
        continue
    d = json.load(open(rep))
    after.update(d.get('sha256', {}))
    item = os.path.basename(rep)[:-5]
    if os.path.exists(os.path.join(WS, 'assets', 'checklists', item + '.md')):
        subprocess.run([sys.executable, os.path.join(HERE, 'finalise.py'), item], capture_output=True)
changed = sorted(p for p in after if before.get(p) != after[p] and p.endswith('.png'))
print('modules failing checks:', failed or 'none')
print('PNG files whose bytes changed:', changed or 'none')
