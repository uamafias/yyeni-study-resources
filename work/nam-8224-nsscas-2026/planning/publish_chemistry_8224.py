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


def manuscript_hashes(workspace):
    workspace=Path(workspace)
    paths=[]
    for topic in (workspace/'topics').iterdir():
        if not topic.is_dir():
            continue
        paths.extend(topic/name for name in ('contract.json','work_order.json','authoring_notes.json') if (topic/name).is_file())
        for name in ('claims','content-units','learning-items','assets'):
            paths.extend(p for p in (topic/name).rglob('*') if p.is_file())
    return {str(p.relative_to(workspace)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)}


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
    review=workspace/'review/claude-full-r1'
    validation_path=review/'operator-final-validation.json'
    validation=json.loads(validation_path.read_text()) if validation_path.is_file() else {}
    reviewed=(validation.get('status')=='complete' and validation.get('verdict')=='publish'
              and validation.get('manuscript_sha256')==manuscript_hashes(workspace))
    index=output/'INDEX.md'
    text=index.read_text()
    heading,body=text.split('\n',1)
    body=body.replace('Every topic here passes the full deterministic check suite. Semantic review runs on published material rather than ahead of it, so the **Open issues** column is debt that ships visibly and is cleared in a maintenance pass - it is not a warning that the topic is unusable.',
                      'All topics have zero failed deterministic checks. Independent Chemistry review and human diagram approval are outstanding. An empty Open issues cell does not mean that semantic review has occurred.')
    body=body.replace('This folder is the copy to upload.', 'This folder is the local review package; release and YYeni import are separate steps.')
    body=body.replace('`build/publish_subject.py`', '`python3 work/nam-8224-nsscas-2026/planning/publish_chemistry_8224.py`')
    notice='**AUTHORING COMPLETE — REVIEW PENDING.** This is a local review build. Claim verification and human visual approval are recorded in the source workspace.'
    if reviewed:
        notice=('**INDEPENDENT REVIEW COMPLETE — HUMAN APPROVALS PENDING.** Claude reviewed all21 topics,390 sampled items and30 PNG figures. '
                'Four substantive findings were repaired;12 low-severity findings remain open. '
                '[Review report](review/REVIEW.md). Human diagram and claim approvals remain outstanding; no YYeni import has been performed.')
        body=body.replace('Independent Chemistry review and human diagram approval are outstanding. An empty Open issues cell does not mean that semantic review has occurred.',
                          'Independent Chemistry review is complete for its stated coverage. The per-topic Open issues column reflects automated QA records; the review report lists the12 open low-severity findings. Human approvals remain outstanding.')
        (output/'review').mkdir(parents=True,exist_ok=True)
        for name in ('REVIEW.md','coverage.json','findings.json','repairs.json','operator-final-validation.json','operator-source-locator-correction.json'):
            if (review/name).is_file():shutil.copy2(review/name,output/'review'/name)
    index.write_text(heading+'\n\n'+notice+'\n'+body)
    (output/'MANIFEST.json').write_text(json.dumps({'qualification':qualification,'build_status':'reviewed_human_approvals_pending' if reviewed else 'authored_review_pending','independent_semantic_review':'complete' if reviewed else 'pending','human_diagram_approval':'pending','claim_approval':'pending','open_review_findings':12 if reviewed else None,'topics':manifest},indent=2)+'\n')
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
