#!/usr/bin/env python3
"""Subject-level publication wrapper: require QA and carry local visual assets.

The shared publisher copies notes and items but has no image-asset handling.
This wrapper adds packaging without changing any shared-standard behaviour.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys

WS = Path(__file__).resolve().parents[1]
ROOT = WS.parents[1]
sys.path.insert(0, str(ROOT / 'standard/v0.2.0-draft/build'))
from publish_subject import collect, publish, write_index


def package(workspace, output):
    workspace, output = Path(workspace), Path(output)
    rows = collect(str(workspace))
    for row in rows:
        q = row['qa']
        if q.get('release_decision') != 'publish' or any(c['status']=='fail' for c in q.get('deterministic_checks', [])):
            raise ValueError(f"Topic {row['topic_id']} has not passed its checks")
    copies = []
    # Preflight every reference before creating or changing output.
    for row in rows:
        topic = Path(row['dir']).resolve()
        texts = [Path(row['notes_path']).read_text()]
        texts += [str(i.get(k) or '') for i in row['items'] for k in ('prompt','canonical_answer')]
        refs = set(re.findall(r'!\[[^\]]*\]\(([^\s)]+)\)', '\n'.join(texts)))
        for ref in sorted(refs):
            asset = (topic / ref).resolve()
            if not ref.startswith('assets/') or not asset.is_relative_to(topic) or not asset.is_file():
                raise ValueError(f'Unpackaged or unsafe image reference: {ref}')
        for asset in sorted((topic/'assets').glob('*')):
            if asset.is_file():
                for directory in ('notes','flashcards'):
                    target = output/directory/'assets'/asset.name
                    if target.exists() and target.read_bytes() != asset.read_bytes():
                        raise ValueError(f'Asset filename collision: {target}')
                    copies.append((asset,target))
    manifest, skipped, qualification = publish(str(workspace),str(output))
    if skipped:
        raise ValueError('Publication skipped topics: '+repr(skipped))
    write_index(str(output),manifest,qualification,str(workspace))
    (output/'MANIFEST.json').write_text(json.dumps({'qualification':qualification,'topics':manifest},indent=2)+'\n')
    for source,target in copies:
        target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(source,target)
    assets=[{'path':str(t.relative_to(output)),'sha256':hashlib.sha256(t.read_bytes()).hexdigest()} for _,t in copies]
    (output/'ASSETS.json').write_text(json.dumps({'assets':assets},indent=2)+'\n')
    return assets


if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--workspace',type=Path,default=WS)
    ap.add_argument('--out',type=Path,default=ROOT/'publish'/WS.name)
    args=ap.parse_args()
    print('Packaged',len(package(args.workspace,args.out)),'asset copies')
