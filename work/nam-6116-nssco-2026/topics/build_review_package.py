#!/usr/bin/env python3
"""Build a REVIEW-ONLY copy of the Biology 6116 notes and flashcards with every held-figure item left out.

Run from the repository root:  .venv/bin/python work/nam-6116-nssco-2026/topics/build_review_package.py

Why this exists. standard/v0.2.0-draft/build/publish_subject.py exports every item of a topic and reads neither
topics/<T>/authoring_notes.json nor visuals_pending, so a normal build would package items whose figures are not
supplied, under an INDEX that calls the folder "the copy to upload". standard/ is not edited in this lane, so this
wrapper keeps the standard builder and changes only what goes into it:

  1. copies the topic datasets into a temporary workspace and removes the items listed under visuals_pending;
  2. runs the standard publish_subject.py on that copy, writing to work/nam-6116-nssco-2026/review-package/
     (never to publish/, which is the learner-upload location);
  3. rewrites the generated INDEX.md heading and upload sentence and adds REVIEW-ONLY.md and HELD-ITEMS-OMITTED.json;
  4. refuses to finish if any exported prompt, answer or guidance still contains explicit figure-reference wording (see
     FIGURE_REF), and fails if publish/nam-6116-nssco-2026 exists.

Limit of the guard: it screens for explicit wording ("Fig.", "VIS-", "the diagram below", "in the graph", lettered
labels). It is a heuristic and is validated against the 35 known held prompts, every one of which it must catch. It
cannot prove that an unflagged prompt is answerable without a figure; that is a reviewer's judgement.

The result is for repository review. It is not a learner package: all claims are unverified and
not marked publishable, no figure need is met, and the omitted items stay in the source slots. Omitting them does not
mark any visual requirement fulfilled.
"""
import glob, hashlib, json, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path

W = Path(__file__).resolve().parents[1]
ROOT = W.parents[1]
OUT = W / 'review-package'
LEARNER = ROOT / 'publish' / W.name
_NOUN = r'(?:diagram|graph|figure|image|picture|photograph|photomicrograph|drawing|slide|chart|trace|micrograph|illustration)'
FIGURE_REF = re.compile(
    r'\bFig\.|\bFigure\s+[\dA-Z]|VIS-|'
    r'\b(?:in|on|from|using|see|of) (?:the|this|that) ' + _NOUN + r'\b|'
    r'\b' + _NOUN + r'\b[^.?!]{0,40}\b(?:below|above|opposite|supplied|provided|attached|overleaf)\b|'
    r'\b(?:shown|marked|labelled|lettered|indicated) (?:in|on|by) (?:the|this) ' + _NOUN + r'\b|'
    r'\bletters? (?:on|in|marked|shown)\b|\blabels? on the ' + _NOUN + r'\b|\bis a (?:labelled )?' + _NOUN + r' (?:of|showing|that shows)\b', re.I)


# Items the screen flags but a person has read and judged to need no supplied figure (the learner draws the diagram or
# graph, or the prompt is a generic procedure). Keyed by a hash of the exact text: if the text changes, the exemption lapses.
REVIEWED_NOT_FIGURE = {
    'ITEM-6116-4-110-CALC': ('4f410a0aa89deb82', 'learner draws the genetic diagram; nothing is supplied'),
    'ITEM-6116-1-040-INTERP': ('caab85762bcbda8a', 'learner labels axes they are asked to draw; nothing is supplied'),
    'ITEM-6116-5-108-MISCON': ('81305e5cf557ad7e', 'the poster is described in words; the learner needs no supplied image'),
    'ITEM-6116-1-044-PROC': ('461ef68b2673b3fe', 'generic procedure for interpreting any graph; no graph is supplied'),
}


def text_hash(item):
    return hashlib.sha256('\n'.join([item['prompt'], item['canonical_answer']] + list(item.get('marking_guidance') or [])).encode()).hexdigest()[:16]


def figure_ref(item):
    blob = ' '.join([item['prompt'], item['canonical_answer']] + list(item.get('marking_guidance') or []))
    m = FIGURE_REF.search(blob)
    return blob[max(0, m.start() - 40):m.end() + 40].replace('\n', ' ') if m else None


def main():
    if LEARNER.exists():
        sys.exit('REFUSED: %s exists. A learner-upload package must not be built while figure items are held; '
                 'remove it deliberately if it is a mistake.' % LEARNER)
    held = {}
    for t in range(1, 6):
        notes = json.loads((W / 'topics' / str(t) / 'authoring_notes.json').read_text())
        held[str(t)] = sorted(v['item_id'] for v in notes.get('visuals_pending', []))
    tmp = Path(tempfile.mkdtemp())
    try:
        ws = tmp / 'work' / W.name
        for name in ('qualification-profile.yaml',):
            (ws).mkdir(parents=True, exist_ok=True)
            shutil.copy(W / name, ws / name)
        (ws / 'curriculum').mkdir(exist_ok=True)
        for name in ('objective_registry.json', 'unit_titles.json'):
            if (W / 'curriculum' / name).exists():
                shutil.copy(W / 'curriculum' / name, ws / 'curriculum' / name)
        counts = {}
        for t in range(1, 6):
            src, dst = W / 'topics' / str(t), ws / 'topics' / str(t)
            (dst / 'learning-items').mkdir(parents=True)
            for f in ('contract.json', 'qa_report.json'):
                shutil.copy(src / f, dst / f)
            for md in src.glob('[0-9]-*.md'):
                shutil.copy(md, dst / md.name)
            kept = total = 0
            for f in sorted(glob.glob(str(src / 'learning-items/*.json'))):
                d = json.loads(Path(f).read_text())
                total += len(d['items'])
                d['items'] = [i for i in d['items'] if i['item_id'] not in held[str(t)]]
                kept += len(d['items'])
                (dst / 'learning-items' / Path(f).name).write_text(json.dumps(d, ensure_ascii=False))
            counts[str(t)] = {'authored': total, 'omitted_held': total - kept, 'in_review_package': kept}
            assert total - kept == len(held[str(t)]), ('held id not found in items', t)
            qa = json.loads((dst / 'qa_report.json').read_text())
            if qa.get('release_decision') == 'reject':
                sys.exit('Topic %s checks reject; fix before building a review package.' % t)
        if OUT.exists():
            shutil.rmtree(OUT)
        subprocess.run([sys.executable, str(ROOT / 'standard/v0.2.0-draft/build/publish_subject.py'), str(ws),
                        '--out', str(OUT)], check=True, cwd=str(ROOT))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    # Safety gate. First prove the screen catches every known held prompt, then require it to find nothing in the export.
    held_ids = {i for v in held.values() for i in v}
    all_items = {}
    for t in range(1, 6):
        for f in glob.glob(str(W / f'topics/{t}/learning-items/*.json')):
            for i in json.loads(Path(f).read_text())['items']:
                all_items[i['item_id']] = i
    missed = sorted(i for i in held_ids if not figure_ref(all_items[i]))
    if missed:
        shutil.rmtree(OUT)
        sys.exit('REFUSED: the figure-reference screen does not catch these known held items, so it cannot be trusted: %s' % missed)
    leaks = {}
    for f in glob.glob(str(OUT / 'flashcards/*.json')):
        for i in json.loads(Path(f).read_text())['items']:
            hit = figure_ref(i)
            ex = REVIEWED_NOT_FIGURE.get(i['item_id'])
            if hit and not (ex and ex[0] == text_hash(i)):
                leaks[i['item_id']] = hit
    if leaks:
        shutil.rmtree(OUT)
        sys.exit('REFUSED: exported items contain figure-reference wording: %s' % json.dumps(leaks, indent=1))
    print('  figure-reference screen: caught all %d known held items; found 0 in the %d exported items'
          % (len(held_ids), sum(c['in_review_package'] for c in counts.values())))

    idx = (OUT / 'INDEX.md').read_text()
    idx = re.sub(r'^# ', '# REVIEW ONLY. NOT FOR LEARNERS. ', idx, count=1)
    idx = re.sub(r'This folder is the copy to upload\..*?`build/publish_subject\.py`; nothing in it is edited by hand\.',
                 'This folder is an internal review copy built by `topics/build_review_package.py`, not a learner upload. '
                 'Items whose figures are not yet supplied are left out; see HELD-ITEMS-OMITTED.json. '
                 'Rebuild it with `topics/build_review_package.py`; nothing in it is edited by hand.', idx, flags=re.S)
    idx = re.sub(r'Semantic review runs on published material rather than ahead of it, so the \*\*Open issues\*\* column is debt that '
                 r'ships visibly and is cleared in a maintenance pass - it is not a warning that the topic is unusable\.',
                 'The standard builder\'s Open issues column is not populated for this subject: semantic review, teacher '
                 'verification of every claim and the figures are all still open, so read this folder as a draft under review.', idx)
    idx = idx.replace('Every topic here passes the full deterministic check suite.',
                      'Every topic here passes the deterministic checks, which verify structure only: no claim is verified '
                      'by a Biology teacher and no figure is supplied.')
    (OUT / 'INDEX.md').write_text(idx)
    # Machine-readable state: nothing in the package may read as cleared.
    banner = {'review_only': True, 'learner_upload': False, 'release_status': 'unreleased',
              'claims_verified_by_teacher': 0, 'figures_supplied': False,
              'status_note': 'Review copy. Deterministic checks verify structure only; no Biology teacher has verified any claim; '
                             'held-figure items are omitted; not for learners or for import into YYeni.'}
    mp = OUT / 'MANIFEST.json'
    man = json.loads(mp.read_text())
    man.update(banner)
    man['gate'] = ('REVIEW ONLY. Deterministic structural checks passed; Step 6 sampled review completed with a '
                   'review-copy-only verdict. No claim has been teacher-verified; the operator waived that checkpoint '
                   'for this subject. Held figures and learner delivery remain open.')
    for t in man['topics']:
        dec = t.pop('release_decision', 'unknown')
        t['structural_check_result'] = 'pass' if dec == 'publish' else dec
        t['release_decision'] = 'review_only_unreleased'
        t['open_review_issues'] = None
        t['open_review_issues_note'] = ('Not tracked by the builder for this subject. Step 6 sampled review is recorded '
                                        'separately; claim verification and held figures remain open.')
        t['claims_verified_by_teacher'] = 0
    man['held_items_omitted'] = {tt: len(v) for tt, v in held.items()}
    man['builder_skipped_topics'] = man.pop('not_published', [])
    man['builder_skipped_topics_note'] = 'Topics the standard builder skipped on a failed check. Empty here. It says nothing about release: this whole folder is an unreleased review copy.'
    mp.write_text(json.dumps(man, indent=1, ensure_ascii=False) + '\n')
    for f in glob.glob(str(OUT / 'flashcards/*.json')):
        d = json.loads(Path(f).read_text())
        d = {**banner, **d}
        Path(f).write_text(json.dumps(d, indent=1, ensure_ascii=False))
    for f in glob.glob(str(OUT / 'notes/*.md')):
        txt = Path(f).read_text()
        txt = re.sub(r'^\*[^\n]*rendered from the approved content units[^\n]*\*$',
                     '*Draft study notes for review. Written from authored content units that no Biology teacher has verified.*',
                     txt, count=1, flags=re.M)
        assert 'approved content units' not in txt, f
        Path(f).write_text('> REVIEW-ONLY DRAFT: unverified, unreleased, not for learners. Figure items are not included.\n\n' + txt)
    n_held = sum(len(v) for v in held.values())
    omitted = {'purpose': 'Held-figure items left out of the review package. Each stays in its source slot and its visual need stays open.',
               'omitted_total': n_held, 'by_topic': {t: {'count': len(v), 'item_ids': v} for t, v in held.items()},
               'counts': counts,
               'note': 'Omitting an item does not fulfil its visual requirement (curriculum/visual-requirements.json, visuals/bindings.json).'}
    (OUT / 'HELD-ITEMS-OMITTED.json').write_text(json.dumps(omitted, indent=2, ensure_ascii=False) + '\n')
    (OUT / 'REVIEW-ONLY.md').write_text(
        '# Review-only package: not for learners\n\n'
        'Built by `work/nam-6116-nssco-2026/topics/build_review_package.py`. Do not upload this folder, import it into YYeni '
        'or give it to learners.\n\n'
        '- **Items:** %d authored, %d held for figures and omitted here, %d in this package.\n'
        '- **Claims:** all 1,102 are unverified and marked not publishable. The operator waived the named-teacher '
        'checkpoint for this subject; the waiver is not verification.\n'
        '- **Figures:** no figure requirement is met. The bank has 258 assets; 254 are operator-approved and none '
        'scientifically verified. The YYeni connector exposes an image-attachment route, but actual display and '
        'learner image or drawing submission remain untested.\n'
        '- **Notes header:** the standard renderer\'s own first line ("rendered from the approved content units") is replaced in this copy by a '
        'draft statement; the workspace notes still carry the renderer line, which needs a framework change.\n'
        '- **Checks:** deterministic checks verify structure only. Step 6 sampled review gave a review-copy-only '
        'verdict, with a reviewer-independence caveat. Later repairs have not had another independent read.\n'
        '- **Figure guard:** exported text was screened for explicit figure-reference wording; the screen caught all 35 known held items. It cannot prove that an unflagged prompt is answerable without a figure.\n\n'
        'Omitted item IDs: HELD-ITEMS-OMITTED.json.\n' % (sum(c['authored'] for c in counts.values()), n_held,
                                                      sum(c['in_review_package'] for c in counts.values())))
    print('review package: %s' % OUT)
    print('  items authored %d, held and omitted %d, in package %d' % (sum(c['authored'] for c in counts.values()), n_held,
                                                                     sum(c['in_review_package'] for c in counts.values())))


if __name__ == '__main__':
    main()
