#!/usr/bin/env python3
"""
Build the review contact sheet for the 6145 diagram cards.

    python3 work/nam-6145-nssco-2026/diagrams/make_contact_sheet.py

Writes diagrams/contact-sheet.png (every question and answer image side by side, two cards per
row, at reduced size) and diagrams/contact-sheet.md (an index linking each full-size PNG, SVG
master, spec, checklist and verifier report). The sheet is for a reviewer's first look; legibility
must still be judged on the full-size images and the 390-px previews in diagrams/inspection/.
"""
import json
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
WS = os.path.dirname(HERE)
WORK_ORDER = os.path.join(WS, 'planning', 'revision-01', 'claude-visual-work-order.json')
THUMB = 420
GAP = 24
LABEL = 54


def font(size):
    for p in ('/System/Library/Fonts/Supplemental/Arial Bold.ttf', '/System/Library/Fonts/Supplemental/Arial.ttf'):
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def main():
    cards = json.load(open(WORK_ORDER))['cards']
    thumbs = []
    for c in cards:
        pair = []
        for side in ('question', 'answer'):
            im = Image.open(os.path.join(WS, c[side + '_png'])).convert('RGB')
            pair.append(im.resize((THUMB, round(im.height * THUMB / im.width)), Image.LANCZOS))
        thumbs.append((c, pair))
    rows = [thumbs[i:i + 2] for i in range(0, len(thumbs), 2)]
    row_h = [LABEL + max(max(p[0].height, p[1].height) for _, p in r) + GAP for r in rows]
    W = 2 * (2 * THUMB + GAP) + 3 * GAP
    sheet = Image.new('RGB', (W, sum(row_h) + GAP), 'white')
    d = ImageDraw.Draw(sheet)
    f, fs = font(22), font(18)
    y = GAP
    for r, h in zip(rows, row_h):
        x = GAP
        for c, (q, a) in r:
            d.text((x, y), '%s  %s' % (c['slot_id'], 'existing' if c['existing_card'] else 'new'), fill='black', font=f)
            d.text((x, y + 26), 'question', fill='#555555', font=fs)
            d.text((x + THUMB + GAP, y + 26), 'answer', fill='#555555', font=fs)
            for k, im in enumerate((q, a)):
                xx = x + k * (THUMB + GAP)
                sheet.paste(im, (xx, y + LABEL))
                d.rectangle([xx - 1, y + LABEL - 1, xx + THUMB, y + LABEL + im.height], outline='#999999')
            x += 2 * THUMB + 2 * GAP
        y += h
    out = os.path.join(HERE, 'contact-sheet.png')
    sheet.save(out)

    lines = ['# 6145 diagram cards: contact sheet and index', '',
             'Contact sheet: [contact-sheet.png](contact-sheet.png) (reduced size; judge legibility on the full-size '
             'images and the 390-px previews in `inspection/`).', '',
             '| # | Item | Target | Question | Answer | Spec | Checklist | Verifier |', '|---|---|---|---|---|---|---|---|']
    for n, c in enumerate(cards, 1):
        iid = c['slot_id']
        rel = lambda p: os.path.relpath(os.path.join(WS, p), HERE)
        lines.append('| %d | %s%s | %s | [png](%s) / [svg](%s) | [png](%s) / [svg](%s) | [spec](specs/%s.json) | '
                     '[checklist](checklists/%s.md) | [report](checks/%s.json) |' % (
                         n, iid, ' (existing)' if c['existing_card'] else '', c['target'],
                         rel(c['question_png']), rel(c['question_svg']), rel(c['answer_png']), rel(c['answer_svg']),
                         iid, iid, iid))
    open(os.path.join(HERE, 'contact-sheet.md'), 'w').write('\n'.join(lines) + '\n')
    print('contact sheet -> %s (%dx%d)' % (os.path.relpath(out, WS), sheet.width, sheet.height))


if __name__ == '__main__':
    main()
