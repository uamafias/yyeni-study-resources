"""Render only the eight resources repaired during Codex visual review."""
from pathlib import Path
import subprocess
import sys
import json

W = Path(__file__).resolve().parents[1]
CODE = W / 'assets/code'
RESOURCES = ['r_1_1_03', 'r_1_5_08', 'r_1_6_03', 'r_2_3_03', 'r_3_2_01', 'r_4_2_07', 'r_4_2_09', 'r_4_1_01']
for name in RESOURCES:
    r = subprocess.run([sys.executable, str(CODE / (name + '.py'))], capture_output=True, text=True)
    (W / 'review' / (name + '-rerender.log')).write_text(r.stdout + r.stderr)
    if r.returncode or '"passed": true' not in r.stdout:
        raise RuntimeError(name + ' failed; inspect its rerender.log')
    print(name + ': rendered; author geometry/layout checks pass', flush=True)
manifest = json.loads((W / 'assets/asset-manifest-6137.json').read_text())
for resource in manifest['resources']:
    if any(Path(p).stem in RESOURCES for p in resource['code_paths']):
        subprocess.run([sys.executable, str(CODE / 'finalise.py'), resource['assigned_item_id']], check=True)
subprocess.run([sys.executable, str(CODE / 'build_manifest.py')], check=True)
