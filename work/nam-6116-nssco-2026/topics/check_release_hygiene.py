#!/usr/bin/env python3
"""Learner-text hygiene gate. Run from the repository root: python3 topics/check_release_hygiene.py [topic ...]

Fails when pipeline or authoring wording reaches text a learner would read: rendered notes, content-unit blocks,
prompts, canonical answers and marking guidance. The only allowed figure token is `Fig. VIS-6116-<objective>` in the
prompt of an item listed under visuals_pending in topics/<T>/authoring_notes.json (the HANDOVER names the figure that
way until the real one is attached). Held items must also be in that list: an item that cites a figure but is not held
fails. This checks wording only; it is not scientific review and does not release anything.
"""
import glob, json, re, sys
from pathlib import Path

W = Path(__file__).resolve().parents[1]
BAD = re.compile(
    r"remain(?:s|ed)? (?:pending|held|unresolved|a genuine gap|required)|"
    r"\b(?:still|also) (?:needs?|requires?) (?:review|a reviewed|delivery|verif)|"
    r"pending (?:figure|specimen|image|review|verif|visual|data|model|variant|graph|stimulus)|"
    r"awaits? (?:the )?(?:reviewed|figure|image|visual|answer variant)|"
    r"reviewed (?:figure|stimulus|key|specimen|question|answer|graph|micrograph|curve|diagram|picture|field|teaching|trace|image|scale|photo|variant|model)|"
    r"VIS-6116|visual hold|image bank|\bthe bank\b|\bCodex\b|\bauthoring\b|"
    r"\bA/B (?:class|reason|level|label|debat)\w*|\bB reasoning\b|\bAO[123] (?:classification|label)|past[- ]paper|examiner|mapping remains|"
    r"teacher (?:should|must|needs to) verify|before (?:learner )?release|model (?:drawing|answer) (?:and|is|are)[^.]{0,40}(?:needed|required|pending)|"
    r"this specimen:|\bSRC-[A-Z]+\b|supplied by the (?:school|teacher) later",
    re.I)
PROPOSED = re.compile(r"\bProposed(?: marks?| points?| answer)?\s*:")   # rubric label; the plain word is fine in biology
FIG = re.compile(r"Fig\. VIS-6116-[0-9A-Za-z.\-]+")
LABELS = re.compile(r"^(?:Named fact|Named feature|Data/reading|What the pattern shows or means|Final answer and unit or ratio|"
                    r"Working/method|First step or sequence|Result or outcome|Reason, because|Reason and consequence|"
                    r"Error or limitation|This situation|Because; inference|Because/inference|How/first cause|"
                    r"Independent variable changed|Dependent variable measured|Controlled variables kept the same|"
                    r"Repeat and mean|Error|Correct distinction)\s*:", re.I)

def texts(t):
    b = W / 'topics' / str(t)
    notes = json.loads((b / 'authoring_notes.json').read_text())
    held = {v['item_id'] for v in notes.get('visuals_pending', [])}
    for f in sorted(glob.glob(str(b / 'learning-items/*.json'))):
        for i in json.loads(Path(f).read_text())['items']:
            yield i['item_id'], 'prompt', i['prompt'], i['item_id'] in held
            yield i['item_id'], 'answer', i['canonical_answer'], False
            for g in i.get('marking_guidance') or []:
                yield i['item_id'], 'guidance', g, False
    for f in sorted(glob.glob(str(b / 'content-units/*.json'))):
        u = json.loads(Path(f).read_text())
        for blk in u['blocks']:
            yield u['unit_id'], 'notes:' + blk['heading'], blk['text'], False
    for f in glob.glob(str(b / '[0-9]-*.md')):
        yield Path(f).name, 'rendered notes', Path(f).read_text(), False

def main(topics):
    bad = []
    for t in topics:
        notes = json.loads((W / 'topics' / str(t) / 'authoring_notes.json').read_text())
        held = {v['item_id'] for v in notes.get('visuals_pending', [])}
        seen_fig = set()
        for ident, where, text, is_held in texts(t):
            if is_held:
                seen_fig.add(ident)
            stripped = FIG.sub('', text) if (where == 'prompt' and is_held) else text
            if where in ('guidance', 'answer', 'prompt') and PROPOSED.search(text): bad.append((t, ident, where, 'Proposed:', text[:80]))
            m = BAD.search(stripped)
            if m: bad.append((t, ident, where, m.group(0), text[max(0, m.start() - 40):m.end() + 50].replace('\n', ' ')))
            if where == 'guidance' and LABELS.match(text.strip()): bad.append((t, ident, where, 'template label', text[:80]))
            if where == 'prompt' and FIG.search(text) and not is_held: bad.append((t, ident, where, 'figure cited but item not held', text[:80]))
            if where == 'prompt' and is_held and len(FIG.findall(text)) != 1: bad.append((t, ident, where, 'held prompt must cite exactly one figure', text[:80]))
    for b in bad: print('  T%s %s [%s] "%s" ... %s' % b)
    print('hygiene: %s (%d problems)' % ('PASS' if not bad else 'FAIL', len(bad)))
    return 1 if bad else 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:] or [1, 2, 3, 4, 5]))
