#!/usr/bin/env python3
"""Make teaching / question / answer variants of stored originals from planning/visual_labels.json.

teaching  syllabus terms on the image
question  neutral letters only, no terms
answer    the question image plus a key (letter = term)
The original file is read, never written. Covered regions (burnt-in labels, a wrong scale label) are recorded.
Writes visuals/variants/<asset>-{teaching,question,answer}.png and visuals/variants/variants.json.
"""
import hashlib, json, pathlib
import matplotlib
from PIL import Image, ImageDraw, ImageFont

WS = pathlib.Path('work/nam-6116-nssco-2026')
OUT = WS / 'visuals/variants'
FONT = pathlib.Path(matplotlib.get_data_path()) / 'fonts/ttf/DejaVuSans-Bold.ttf'
INK, HALO, LINE = (17, 17, 17), (255, 255, 255), (255, 255, 255)


def font(size):
    return ImageFont.truetype(str(FONT), size)


def boxed_text(d, xy, text, f, pad):
    x, y = xy
    W, H = d.im.size
    l, t, r, b = d.textbbox((x, y), text, font=f, anchor='mm')
    # keep the whole label inside the frame: shift, never shrink or crop
    x += max(0, pad + 2 - l) - max(0, r + pad + 2 - W)
    y += max(0, pad + 2 - t) - max(0, b + pad + 2 - H)
    l, t, r, b = d.textbbox((x, y), text, font=f, anchor='mm')
    d.rectangle([l - pad, t - pad, r + pad, b + pad], fill=HALO, outline=INK, width=max(1, pad // 3))
    d.text((x, y), text, font=f, fill=INK, anchor='mm')


def render(src, spec, mode):
    im = Image.open(src).convert('RGB')
    w = im.width
    size = max(14, int(w * 0.028)); pad = max(3, size // 4); lw = max(2, size // 9)
    d = ImageDraw.Draw(im)
    for x0, y0, x1, y1, _ in spec['cover']:
        d.rectangle([x0, y0, x1, y1], fill=HALO)
    f = font(size)
    for lab in spec['labels']:
        text = lab['term'].split(' (')[0] if mode == 'teaching' else lab['letter']
        if lab['point']:
            # dark line with a light edge, so the leader shows on pale and dark tissue
            d.line([tuple(lab['text_at']), tuple(lab['point'])], fill=LINE, width=lw + 4)
            d.line([tuple(lab['text_at']), tuple(lab['point'])], fill=INK, width=lw)
            r = lw * 2
            d.ellipse([lab['point'][0] - r, lab['point'][1] - r, lab['point'][0] + r, lab['point'][1] + r], fill=INK, outline=LINE)
        boxed_text(d, tuple(lab['text_at']), text, f, pad)
    if mode != 'answer':
        return im
    keyf = font(max(13, int(size * 0.8)))
    lines = [f"{l['letter']}  {l['term']}" for l in spec['labels']]
    lh = int(keyf.size * 1.45)
    panel = Image.new('RGB', (w, lh * (len(lines) + 1) + 2 * pad), HALO)
    pd = ImageDraw.Draw(panel)
    pd.text((pad * 2, pad), 'Key', font=keyf, fill=INK)
    for i, s in enumerate(lines, 1):
        pd.text((pad * 2, pad + i * lh), s, font=keyf, fill=INK)
    out = Image.new('RGB', (w, im.height + panel.height), HALO)
    out.paste(im, (0, 0)); out.paste(panel, (0, im.height))
    return out


def main():
    spec = json.loads((WS / 'planning/visual_labels.json').read_text())
    OUT.mkdir(parents=True, exist_ok=True)
    records = []
    for aid, s in spec['assets'].items():
        src = WS / s['source']
        before = hashlib.sha256(src.read_bytes()).hexdigest()
        uncertain = [f"{l['letter']} {l['term']}: {l['review']}" for l in s['labels'] if l['review'].startswith('uncertain')]
        for mode in ('teaching', 'question', 'answer'):
            p = OUT / f'{aid}-{mode}.png'
            render(src, s, mode).save(p, optimize=True)
            records.append({'asset_id': aid, 'variant': mode, 'path': str(p.relative_to(WS)),
                            'derived_from': s['source'], 'objective_ids': s['objective_ids'],
                            'covered_regions': [c[4] for c in s['cover']],
                            'changes': ('Added syllabus teaching labels and leader marks' if mode == 'teaching' else
                                        'Added neutral letter labels and leader marks' if mode == 'question' else
                                        'Added neutral letter labels, leader marks and answer-key panel') +
                                       ('; covered regions: ' + '; '.join(c[4] for c in s['cover']) if s['cover'] else '; no regions masked'),
                            'scale_note': s.get('scale_note'), 'missing': s.get('missing'),
                            'label_review': 'pending; uncertain labels: ' + ('; '.join(uncertain) if uncertain else 'none flagged')})
        if hashlib.sha256(src.read_bytes()).hexdigest() != before:
            raise SystemExit('original changed: ' + str(src))
    (OUT / 'variants.json').write_text(json.dumps({'generated_by': 'planning/make_visual_variants.py',
                                                   'rule': 'Derived files. Originals untouched. Every variant awaits label review.',
                                                   'variants': records}, indent=2, ensure_ascii=False) + '\n')
    print(f'{len(records)} variants from {len(spec["assets"])} originals')


if __name__ == '__main__':
    main()
