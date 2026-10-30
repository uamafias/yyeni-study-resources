"""Shared builder for the six licensed photographs of topic 4.2 (VIS-6137-4.2-05 to -10).

Each original was acquired with the YYeni Web Harvester (manifest
_harvest/manifests/6137-4.2-licensed-photos.csv) into assets/sources/photos/, and its SHA-1 was checked
against the SHA-1 Wikimedia Commons records for the file. The builder:
- writes a display derivative (EXIF-transposed, resized to 1,500 px wide, metadata stripped) beside the
  original and embeds it in the layered master;
- question side: title, photograph and full attribution caption (no answer markings);
- answer side: the same photograph with numbered markers on the observed features and an observation
  panel written after inspecting the actual image.
Licences (all permit redistribution and derivatives with attribution; CC BY-SA adaptations are shared
under the same licence) are recorded per resource in the spec and record.
"""
import base64
import hashlib
import io
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, GREY, WS, build, check, write_record, binding  # noqa: E402

W = 1000
SRC = os.path.join(WS, 'assets', 'sources', 'photos')


def sha256(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()


def sha1(path):
    return hashlib.sha1(open(path, 'rb').read()).hexdigest()


def display_copy(rid):
    from PIL import Image, ImageOps
    orig = os.path.join(SRC, '%s_original.jpg' % rid)
    out = os.path.join(SRC, '%s_display.jpg' % rid)
    im = ImageOps.exif_transpose(Image.open(orig)).convert('RGB')
    if im.width > 1500:
        im = im.resize((1500, round(im.height * 1500 / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, 'JPEG', quality=86, optimize=True)
    data = buf.getvalue()
    if not os.path.exists(out) or open(out, 'rb').read() != data:
        open(out, 'wb').write(data)
    return orig, out, im.size, data


def make(rid, item, title, licence, markers, rows, panel_title, checks_extra=(), withholds=(), solution=()):
    orig, disp, (dw, dh), data = display_copy(rid)
    assert sha1(orig) == licence['commons_sha1'], 'original differs from the Commons file'
    ph = round(W * dh / dw)
    py = 64
    credit = ('Photo: %s, “%s”, Wikimedia Commons, %s. Resized%s.' %
              (licence['creator'], licence['title'], licence['licence'],
               '; the answer version is annotated and shared under %s' % licence['licence'] if 'SA' in licence['licence']
               else '; the answer version is annotated'))
    lines = len(credit) // 64 + 2
    hq = py + ph + 20 + 32 * lines
    ha = hq + 120 + 34 * sum(1 + len(s) // 62 for _, s in rows) + 20
    fig = Fig(W, {'question': hq, 'answer': ha}, title)
    fig.add('<image x="0" y="%d" width="%d" height="%d" preserveAspectRatio="none" href="data:image/jpeg;base64,%s"/>'
            % (py, W, ph, base64.b64encode(data).decode()))
    fig.para(20, py + ph + 36, credit, 26, 960, 32, fill=GREY)
    A = 'a'
    for n, (x, y) in markers:
        fig.circle(x, py + y, 24, 'none', '#ffffff', 5, A)
        fig.marker(x, py + y, n, A, r=21)
    fig.rect(16, hq + 6, W - 32, ha - hq - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, hq + 46, panel_title, 28, 'start', 'bold', C['answer'], A)
    yy = hq + 90
    for n, s in rows:
        fig.marker(52, yy - 9, n, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8
    spec = {'kind': 'licensed photograph (actual image, not generated)', 'photo_display_px': [dw, dh],
            'licence': licence, 'original_path': os.path.relpath(orig, WS), 'original_sha256': sha256(orig), 'original_sha1': sha1(orig),
            'display_path': os.path.relpath(disp, WS), 'display_sha256': sha256(disp),
            'derivative': 'EXIF-transposed, resized to %d px wide, re-encoded JPEG q86; answer side adds numbered markers and a text panel' % dw,
            'markers_photo_px_at_1000_wide': {n: [x, y] for n, (x, y) in markers},
            'observations_after_inspection': [s for _, s in rows],
            'question_withholds': list(withholds), 'independent_solution': list(solution)}
    checks = [check('original SHA-1 equals the Wikimedia Commons SHA-1', sha1(orig) == licence['commons_sha1']),
              check('licence permits redistribution and derivatives', licence['redistribution'] and licence['derivatives']),
              check('markers lie inside the photograph', all(0 <= x <= W and 0 <= y <= ph for _, (x, y) in markers))] + list(checks_extra)
    sides = {'question': {'path': 'assets/images/%s-question.png' % item, 'layers': ['q']},
             'answer': {'path': 'assets/images/%s-answer.png' % item, 'layers': ['a']}}
    rep = build(rid, fig, spec, sides, checks, panels=[(16, hq + 6, W - 32, ha - hq - 16)])
    return rep, os.path.relpath(disp, WS), os.path.relpath(orig, WS)


def licence_record(meta, retrieved='2026-10-30'):
    sa = 'SA' in meta['licence']
    return dict(meta, retrieved=retrieved, redistribution=True, derivatives=True,
                attribution='%s, “%s”, via Wikimedia Commons, %s (%s)' % (meta['creator'], meta['title'], meta['licence'], meta['licence_url']),
                derivative_terms='Adaptations must credit the creator and indicate changes' + ('; they must be shared under %s' % meta['licence'] if sa else ''),
                acquisition='YYeni Web Harvester, manifest _harvest/manifests/6137-4.2-licensed-photos.csv, run 20261030-111155-608')
