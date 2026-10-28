#!/usr/bin/env python3
"""
Build the 6145 diagram asset manifest from the specs, the verifier reports and the card text.

    python3 work/nam-6145-nssco-2026/diagrams/build_manifest.py

Writes diagrams/asset-manifest.json, keyed by repository item ID, with one entry per side:
image and SVG master paths (workspace-relative), SHA-256 hashes, the description shown as alt
text, and the semantic values the image encodes. Only cards whose verifier report has no
failures and whose files still match the hashes in that report are listed as ready.

Managed YYeni asset IDs do not exist yet. They are filled in at the later, teacher-approved
import; until then question_asset_id and answer_asset_id are null.
"""
import hashlib
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
WS = os.path.dirname(HERE)
WORK_ORDER = os.path.join(WS, 'planning', 'revision-01', 'claude-visual-work-order.json')


def sha(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()


def main():
    cards = json.load(open(WORK_ORDER))['cards']
    review_path = os.path.join(HERE, 'CODEX-REVIEW-6145.json')
    review = json.load(open(review_path)) if os.path.exists(review_path) else {'items': {}}
    out = {'manifest': '6145 diagram cards, revision-01', 'workspace': 'work/nam-6145-nssco-2026',
           'paths_are_relative_to': 'work/nam-6145-nssco-2026',
           'upload_status': 'not uploaded; managed asset IDs are assigned at the later teacher-approved import',
           'items': {}}
    for c in cards:
        iid = c['slot_id']
        spec_p = os.path.join(HERE, 'specs', iid + '.json')
        rep_p = os.path.join(HERE, 'checks', iid + '.json')
        if not os.path.exists(spec_p):
            out['items'][iid] = {'status': 'pending', 'topic_id': c['topic_id'], 'target': c['target']}
            continue
        spec = json.load(open(spec_p))
        rep = json.load(open(rep_p)) if os.path.exists(rep_p) else {'failed': None, 'files_sha256': {}}
        entry = {'topic_id': c['topic_id'], 'target': c['target'], 'existing_card': c['existing_card'],
                 'spec': os.path.relpath(spec_p, WS), 'renderer': 'diagrams/render_6145_diagrams.py',
                 'verifier_report': os.path.relpath(rep_p, WS), 'model': spec['model']}
        stale = []
        for side in ('question', 'answer'):
            png, svg = c[side + '_png'], c[side + '_svg']
            h_png, h_svg = sha(os.path.join(WS, png)), sha(os.path.join(WS, svg))
            if rep['files_sha256'].get(png) != h_png or rep['files_sha256'].get(svg) != h_svg:
                stale.append(side)
            entry[side] = {'png': png, 'svg_master': svg, 'png_sha256': h_png, 'svg_sha256': h_svg,
                           'title': spec[side]['title'], 'alt_text': spec[side]['description'],
                           'yyeni_asset_id': None,
                           'yyeni_field': 'question_asset_id' if side == 'question' else 'answer_asset_id'}
        ok = rep.get('failed') == 0 and not stale
        entry['status'] = 'ready for Codex review' if ok else 'NOT READY: %s' % (
            'verifier failures' if rep.get('failed') else 'files changed since verification (%s)' % ', '.join(stale))
        entry['checks_passed'] = rep.get('passed')
        # Independent review is valid only for the image bytes and learner text actually read.
        accepted = review.get('items', {}).get(iid, {})
        text_file = os.path.join(WS, 'topics', c['topic_id'], 'learning-items',
                                 'topic_%s_items.json' % c['topic_id'])
        item = next((i for i in json.load(open(text_file))['items'] if i['item_id'] == iid), None)
        text_hash = (hashlib.sha256(json.dumps({k: item.get(k) for k in
                     ('prompt', 'canonical_answer', 'marking_guidance', 'assessment_objectives',
                      'blooms_level', 'command_word', 'mark_tariff')}, sort_keys=True,
                      ensure_ascii=False).encode()).hexdigest() if item else None)
        reviewed_files = {entry[side][p]: entry[side][h] for side in ('question', 'answer')
                          for p, h in (('png', 'png_sha256'), ('svg_master', 'svg_sha256'))}
        if (ok and accepted.get('status') == 'accepted'
                and accepted.get('learner_text_sha256') == text_hash
                and accepted.get('files_sha256') == reviewed_files):
            # This status describes the accepted visual subset. Whole-subject
            # review/publication is tracked in STATUS.md, not inferred here.
            entry['status'] = 'reviewed by Codex; visual subset accepted'
            entry['independent_review'] = os.path.relpath(review_path, WS)
        out['items'][iid] = entry
    json.dump(out, open(os.path.join(HERE, 'asset-manifest.json'), 'w'), indent=2, ensure_ascii=False)
    for iid, e in out['items'].items():
        print('%-26s %s' % (iid, e['status']))


if __name__ == '__main__':
    main()
