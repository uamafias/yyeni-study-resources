"""Shared drawing and rendering helpers for the 6137 Geography visual resources.

Each resource module (r_<resource>.py) builds ONE layered SVG master from its own data/geometry:

    layer "base"  - shown on every side
    layer "q"     - question-only elements (blank boxes, prompts on the figure)
    layer "a"     - answer-only annotations
    layer "v-<name>" - extra variant layers (practical record sheets, plotted versions, ...)

Every PNG is rendered from that one master by hiding layers, so the question and answer images
share identical geometry. Rendering: SVG -> Chromium (Playwright) screenshot at 1.5x. The browser's
own text measurements are saved so the automated checks test clipping and label collisions on real
widths. Previews at 390 px (phone width) and in greyscale are written for visual inspection.

Requires Python 3, Pillow and Playwright with its Chromium build. No network access.
"""
import hashlib
import html
import json
import math
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.dirname(HERE)
WS = os.path.dirname(ASSETS)

FONT = 'Arial, Helvetica, sans-serif'
INK = '#1a1a1a'
GREY = '#6b6b6b'
SCALE = 1.5
MIN_FONT = 26          # px at a 1000-px-wide master: about 10 px when the PNG is shown 390 px wide

# Colour palette chosen for distinct greyscale lightness as well as hue.
C = {
    'sea': '#cfe6f5', 'sea_dark': '#7fb2d6', 'ocean_crust': '#3d4f5c', 'oc_lith': '#7a8a96',
    'cont_crust': '#c9a26b', 'cont_lith': '#e3cfa6', 'mantle': '#f3dcc8', 'magma': '#c0392b',
    'land': '#dfe8c4', 'land_dark': '#a8bb78', 'rock': '#b8b2a7', 'rock_dark': '#7d766b',
    'water': '#4a90c8', 'ice': '#e8f4fb', 'sand': '#ecd9a0', 'veg': '#6f9e4f', 'red': '#b03a2e',
    'blue': '#1f5f99', 'orange': '#d9822b', 'purple': '#6c4f8f', 'green': '#2e7d4f', 'answer': '#0b6e4f',
    'highlight': '#fff3b0',
}


def esc(s):
    return html.escape(str(s), quote=True)


def f(v):
    return ('%.2f' % v).rstrip('0').rstrip('.')


class Fig:
    def __init__(self, width, heights, title=None):
        """heights: {'question': H, 'answer': H, ...} - each side is clipped to its own height."""
        self.w = width
        self.heights = dict(heights)
        self.h = max(self.heights.values())
        self.extra_h = 0
        self.layers = {}
        self.order = []
        self.defs = []
        if title:
            self.text(width / 2, 38, title, size=28, anchor='middle', weight='bold')

    def add(self, svg, layer='base'):
        if layer not in self.layers:
            self.layers[layer] = []
            self.order.append(layer)
        self.layers[layer].append(svg)

    def under(self, svg, layer='au'):
        """Add to a layer drawn beneath everything else (e.g. answer shading under the base map)."""
        if layer not in self.layers:
            self.layers[layer] = []
            self.order.insert(0, layer)
        self.layers[layer].append(svg)

    # ---- primitives -------------------------------------------------------------------------
    def path(self, d, fill='none', stroke=INK, sw=2, layer='base', extra=''):
        self.add('<path d="%s" fill="%s" stroke="%s" stroke-width="%s" stroke-linejoin="round" %s/>'
                 % (d, fill, stroke, f(sw), extra), layer)

    def poly(self, pts, fill='none', stroke=INK, sw=2, closed=True, layer='base', extra=''):
        d = 'M' + ' L'.join('%s %s' % (f(x), f(y)) for x, y in pts) + (' Z' if closed else '')
        self.path(d, fill, stroke, sw, layer, extra)

    def line(self, x1, y1, x2, y2, stroke=INK, sw=2, layer='base', dash=None, extra=''):
        ds = ' stroke-dasharray="%s"' % dash if dash else ''
        self.add('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" stroke-linecap="round"%s %s/>'
                 % (f(x1), f(y1), f(x2), f(y2), stroke, f(sw), ds, extra), layer)

    def rect(self, x, y, w, h, fill='none', stroke=INK, sw=2, rx=0, layer='base', extra=''):
        self.add('<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s" stroke="%s" stroke-width="%s" %s/>'
                 % (f(x), f(y), f(w), f(h), f(rx), fill, stroke, f(sw), extra), layer)

    def circle(self, cx, cy, r, fill='none', stroke=INK, sw=2, layer='base', extra=''):
        self.add('<circle cx="%s" cy="%s" r="%s" fill="%s" stroke="%s" stroke-width="%s" %s/>'
                 % (f(cx), f(cy), f(r), fill, stroke, f(sw), extra), layer)

    def text(self, x, y, s, size=24, anchor='start', weight='normal', fill=INK, layer='base', halo=False,
             italic=False, rotate=None, extra=''):
        st = ' font-style="italic"' if italic else ''
        tr = ' transform="rotate(%s %s %s)"' % (f(rotate), f(x), f(y)) if rotate else ''
        hl = (' stroke="#ffffff" stroke-width="6" stroke-linejoin="round" paint-order="stroke"' if halo else '')
        self.add('<text x="%s" y="%s" font-family="%s" font-size="%s" font-weight="%s" text-anchor="%s" fill="%s"%s%s%s %s>%s</text>'
                 % (f(x), f(y), FONT, f(size), weight, anchor, fill, st, tr, hl, extra, esc(s)), layer)

    def lines(self, x, y, rows, size=22, lh=None, **kw):
        lh = lh or size * 1.28
        for i, r in enumerate(rows):
            self.text(x, y + i * lh, r, size=size, **kw)
        return y + len(rows) * lh

    def para(self, x, y, text, size=26, width=900, lh=None, **kw):
        """Wrap text to an estimated width (Arial ~0.52 em per character); returns the next y.
        The browser-measured clipping check catches any estimate that is too generous."""
        per = max(8, int(width / (size * 0.52)))
        rows, cur = [], ''
        for w in text.split():
            if cur and len(cur) + 1 + len(w) > per:
                rows.append(cur)
                cur = w
            else:
                cur = (cur + ' ' + w).strip()
        if cur:
            rows.append(cur)
        return self.lines(x, y, rows, size, lh, **kw)

    def arrow(self, x1, y1, x2, y2, stroke=INK, sw=4, head=18, layer='base', halo=True, dash=None):
        ang = math.atan2(y2 - y1, x2 - x1)
        bx, by = x2 - head * 0.8 * math.cos(ang), y2 - head * 0.8 * math.sin(ang)
        if halo:
            self.line(x1, y1, bx, by, '#ffffff', sw + 5, layer)
        self.line(x1, y1, bx, by, stroke, sw, layer, dash=dash)
        p1 = (x2 - head * math.cos(ang - 0.42), y2 - head * math.sin(ang - 0.42))
        p2 = (x2 - head * math.cos(ang + 0.42), y2 - head * math.sin(ang + 0.42))
        if halo:
            self.poly([(x2, y2), p1, p2], '#ffffff', '#ffffff', 5, layer=layer)
        self.poly([(x2, y2), p1, p2], stroke, stroke, 1, layer=layer)

    def marker(self, x, y, label, layer='a', r=19, fill=None):
        self.circle(x, y, r, fill or C['answer'], '#ffffff', 2.5, layer)
        self.text(x, y + 9, label, 26, 'middle', 'bold', '#ffffff', layer)

    def pattern(self, pid, svg_body, w=12, h=12):
        self.defs.append('<pattern id="%s" patternUnits="userSpaceOnUse" width="%s" height="%s">%s</pattern>'
                         % (pid, w, h, svg_body))

    # ---- output -----------------------------------------------------------------------------
    def master(self, meta=None):
        H = max(self.h, self.extra_h)
        out = ['<?xml version="1.0" encoding="UTF-8"?>',
               '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d">'
               % (self.w, H, self.w, H)]
        if meta:
            out.append('<metadata>%s</metadata>' % esc(json.dumps(meta, ensure_ascii=False)))
        out.append('<defs>%s</defs>' % ''.join(self.defs))
        out.append('<rect x="0" y="0" width="%d" height="%d" fill="#ffffff"/>' % (self.w, H))
        for name in self.order:
            out.append('<g id="layer-%s">' % name)
            out.extend('  ' + s for s in self.layers[name])
            out.append('</g>')
        out.append('</svg>')
        return '\n'.join(out) + '\n'


def side_svg(master, visible, clip=None, hide_base=False):
    """Hide every layer not in `visible` (base is visible unless hide_base). With clip=(x, y, w, h)
    the side shows only that region of the master (used for variant panels stored below the figure)."""
    names = re.findall(r'<g id="layer-([^"]+)">', master)
    hidden = [n for n in names if (n != 'base' or hide_base) and n not in visible]
    css = ''.join('#layer-%s{display:none}' % n for n in hidden)
    out = master.replace('<defs>', '<defs><style>%s</style>' % css, 1)
    if clip:
        x, y, w, h = clip
        out = re.sub(r'<svg ([^>]*?)width="\d+" height="\d+" viewBox="[^"]*"',
                     lambda m: '<svg %swidth="%d" height="%d" viewBox="%d %d %d %d"' % (m.group(1), w, h, x, y, w, h), out, count=1)
    return out


def rasterise(jobs):
    """jobs: [(svg_text, png_path, width, height)] -> list of visible text boxes per job."""
    from playwright.sync_api import sync_playwright
    results = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        for svg, png, w, h in jobs:
            page = browser.new_page(viewport={'width': w, 'height': h}, device_scale_factor=SCALE)
            page.set_content('<html><body style="margin:0;background:#fff">%s</body></html>' % svg.split('?>', 1)[-1])
            page.wait_for_timeout(120)
            page.screenshot(path=png, clip={'x': 0, 'y': 0, 'width': w, 'height': h})
            boxes = page.evaluate('''() => Array.from(document.querySelectorAll('svg text'))
                .filter(t => t.getClientRects().length > 0)
                .map(t => { const r = t.getBoundingClientRect();
                            return {text: t.textContent, x: r.x, y: r.y, w: r.width, h: r.height,
                                    layer: (t.closest('g[id^="layer-"]') || {id: ''}).id}; })''')
            results.append(boxes)
            page.close()
        browser.close()
    return results


def small_fonts(svg, visible):
    """Text elements in visible layers whose font-size is below MIN_FONT."""
    out = []
    for name, body in re.findall(r'<g id="layer-([^"]+)">(.*?)</g>\n', svg, re.S):
        if name != 'base' and name not in visible:
            continue
        for size, txt in re.findall(r'<text[^>]*font-size="([0-9.]+)"[^>]*>([^<]*)</text>', body):
            if float(size) < MIN_FONT:
                out.append((float(size), html.unescape(txt)[:30]))
    return out


def text_problems(boxes, w, h, allow_overlap=()):
    probs = []
    for b in boxes:
        if b['x'] < 0 or b['y'] < 0 or b['x'] + b['w'] > w + 0.5 or b['y'] + b['h'] > h + 0.5:
            probs.append('clipped: %r' % b['text'])
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            a, b = boxes[i], boxes[j]
            ox = min(a['x'] + a['w'], b['x'] + b['w']) - max(a['x'], b['x'])
            oy = min(a['y'] + a['h'], b['y'] + b['h']) - max(a['y'], b['y'])
            if ox > 1.5 and oy > 3:
                pair = (a['text'], b['text'])
                if pair in allow_overlap or pair[::-1] in allow_overlap:
                    continue
                probs.append('overlap: %r / %r' % pair)
    return probs


def previews(png, stem):
    """Write phone-width (390 px) colour and greyscale previews of one PNG."""
    from PIL import Image
    im = Image.open(png).convert('RGB')
    small = im.resize((390, round(im.height * 390 / im.width)), Image.LANCZOS)
    p1 = os.path.join(ASSETS, 'inspection', stem + '-390.png')
    p2 = os.path.join(ASSETS, 'inspection', stem + '-390-grey.png')
    small.save(p1)
    small.convert('L').save(p2)
    return p1, p2


def inspection_sheet(stems, out_stem):
    """Place the 390-px colour and greyscale previews of several sides on one sheet."""
    from PIL import Image
    ims = []
    for s in stems:
        ims.append(Image.open(os.path.join(ASSETS, 'inspection', s + '-390.png')).convert('RGB'))
        ims.append(Image.open(os.path.join(ASSETS, 'inspection', s + '-390-grey.png')).convert('RGB'))
    gap = 16
    W = sum(i.width for i in ims) + gap * (len(ims) + 1)
    H = max(i.height for i in ims) + 2 * gap
    sheet = Image.new('RGB', (W, H), '#888888')
    x = gap
    for i in ims:
        sheet.paste(i, (x, gap))
        x += i.width + gap
    p = os.path.join(ASSETS, 'inspection', out_stem + '-phone-sheet.png')
    sheet.save(p)
    return p


def sha(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()


def rel(path):
    return os.path.relpath(path, WS)


def plan_entry(resource_id):
    plan = json.load(open(os.path.join(WS, 'planning', 'visual-resource-plan-6137.json')))
    return next(r for r in plan['resources'] if r['resource_id'] == resource_id)


def build(resource_id, fig, spec, sides, checks=None, allow_overlap=(), panels=()):
    """Write spec JSON, master SVG and each side's PNG; run automated text checks.

    sides: {name: {'path': workspace-relative png path, 'layers': [...], 'forbidden': [regex, ...]}}
    The 'question' and 'answer' sides must use the plan's exact paths.
    """
    pe = plan_entry(resource_id)
    assert sides['question']['path'] == pe['question_path'], 'question path differs from plan'
    assert sides['answer']['path'] == pe['answer_path'], 'answer path differs from plan'
    spec = dict(spec)
    # Licensed-photo plan entries carry no master/spec path; their layered master and spec are still
    # written (at the conventional paths) so the annotated answer is reproducible and hashed.
    m_rel = pe['master_path'] or 'assets/masters/%s.svg' % pe['assigned_item_id']
    s_rel = pe['data_spec_path'] or 'assets/specs/%s.json' % pe['assigned_item_id']
    spec.update({'resource_id': resource_id, 'assigned_item_id': pe['assigned_item_id'],
                 'master_path': m_rel, 'data_spec_path': s_rel, 'plan_master_path': pe['master_path'], 'plan_data_spec_path': pe['data_spec_path'],
                 'sides': {k: {'path': v['path'], 'visible_layers': ([] if v.get('hide_base') else ['base']) + list(v['layers']),
                               'clip': v.get('clip'), 'height_px': (v['clip'][3] if v.get('clip') else fig.heights[k]),
                               'bound_item': v.get('bound_item')} for k, v in sides.items()},
                 'render': {'engine': 'Chromium via Playwright', 'device_scale_factor': SCALE,
                            'master_viewbox': [fig.w, fig.h]}})
    master = fig.master({'resource_id': resource_id, 'note': 'Layered master: base, q (question only), '
                         'a (answer only), v-* (variants). Generated by assets/code; do not hand-edit.'})
    mp = os.path.join(WS, m_rel)
    sp = os.path.join(WS, s_rel)
    open(mp, 'w').write(master)
    json.dump(spec, open(sp, 'w'), indent=1, ensure_ascii=False)
    open(sp, 'a').write('\n')
    panels = list(panels)
    hq, ha = fig.heights.get('question'), fig.heights.get('answer')
    if hq and ha and ha > hq and (16, hq + 6, fig.w - 32, ha - hq - 16) not in panels:
        panels.append((16, hq + 6, fig.w - 32, ha - hq - 16))      # the answer panel below the figure
    jobs = []
    for name, sd in sides.items():
        clip = sd.get('clip')
        w, h = (clip[2], clip[3]) if clip else (fig.w, fig.heights[name])
        jobs.append((side_svg(master, set(sd['layers']), clip, sd.get('hide_base', False)), os.path.join(WS, sd['path']), w, h))
    boxes = rasterise(jobs)
    report = {'resource_id': resource_id, 'sides': {}, 'checks': []}
    item = pe['assigned_item_id']
    for (name, sd), bx, job in zip(sides.items(), boxes, jobs):
        probs = text_problems(bx, job[2], job[3], allow_overlap)
        ox, oy = (sd['clip'][0], sd['clip'][1]) if sd.get('clip') else (0, 0)
        side_panels = [(px - ox, py - oy, pw, ph) for (px, py, pw, ph) in panels + list(sd.get('panels', []))]
        for (px, py, pw, ph) in side_panels:
            for b in bx:
                mx, my = b['x'] + b['w'] / 2, b['y'] + b['h'] / 2
                if px <= mx <= px + pw and py <= my <= py + ph and (
                        b['x'] < px - 1 or b['x'] + b['w'] > px + pw + 1 or b['y'] < py - 1 or b['y'] + b['h'] > py + ph + 1):
                    probs.append('outside its panel: %r' % b['text'])
        alltext = ' '.join(b['text'] for b in bx)
        svg_side = jobs[list(sides).index(name)][0]
        small = small_fonts(svg_side, set(sd['layers']))
        if small:
            probs.append('font below %spx: %s' % (MIN_FONT, small[:6]))
        for pat in sd.get('forbidden', []):
            if re.search(pat, alltext, re.I):
                probs.append('forbidden text on %s side: %s' % (name, pat))
        json.dump(bx, open(os.path.join(ASSETS, 'checks', '%s-%s.textboxes.json' % (item, name)), 'w'), indent=1)
        stem = '%s-%s' % (item, name)
        previews(os.path.join(WS, sd['path']), stem)
        report['sides'][name] = {'path': sd['path'], 'text_elements': len(bx), 'problems': probs,
                                 'min_font_px': min([b['h'] for b in bx] or [0])}
    inspection_sheet(['%s-%s' % (item, n) for n in sides], item)
    for c in (checks or []):
        report['checks'].append(c)
    report['passed'] = all(not s['problems'] for s in report['sides'].values()) and all(c['ok'] for c in report['checks'])
    files = [m_rel, s_rel] + [sd['path'] for sd in sides.values()]
    report['sha256'] = {p: sha(os.path.join(WS, p)) for p in files}
    json.dump(report, open(os.path.join(ASSETS, 'checks', item + '.json'), 'w'), indent=1)
    print(json.dumps({k: v for k, v in report.items() if k != 'sha256'}, indent=1))
    for p, h in report['sha256'].items():
        print(h[:16], p)
    return report


def check(name, ok, detail=''):
    return {'check': name, 'ok': bool(ok), 'detail': detail}


def write_record(resource_id, code, bindings, notes_links, extra_files=(), licence=None, notes=None):
    """Per-resource record read by the manifest builder: code, checklist, bindings and extra files."""
    pe = plan_entry(resource_id)
    item = pe['assigned_item_id']
    rec = {'resource_id': resource_id, 'code_paths': list(code) + ['assets/code/vislib.py'],
           'checklist_path': 'assets/checklists/%s.md' % item, 'check_report_path': 'assets/checks/%s.json' % item,
           'extra_files': list(extra_files), 'bindings': bindings, 'notes_links': notes_links,
           'status': 'self-reviewed by Claude; awaiting Codex review'}
    if licence:
        rec['licence'] = licence
    if notes:
        rec['notes'] = notes
    json.dump(rec, open(os.path.join(ASSETS, 'records', resource_id + '.json'), 'w'), indent=1, ensure_ascii=False)
    return rec


def binding(item_id, q, a):
    return {'item_id': item_id, 'question_path': q, 'answer_path': a}


class Axes:
    """Linear data-to-pixel mapping with ticked, labelled axes and light gridlines."""

    def __init__(self, fig, x0, y0, w, h, xr, yr, layer='base'):
        self.fig, self.x0, self.y0, self.w, self.h = fig, x0, y0, w, h
        self.xr, self.yr, self.layer = xr, yr, layer

    def X(self, v):
        return self.x0 + (v - self.xr[0]) / (self.xr[1] - self.xr[0]) * self.w

    def Y(self, v):
        return self.y0 + self.h - (v - self.yr[0]) / (self.yr[1] - self.yr[0]) * self.h

    def invX(self, px):
        return self.xr[0] + (px - self.x0) / self.w * (self.xr[1] - self.xr[0])

    def invY(self, py):
        return self.yr[0] + (self.y0 + self.h - py) / self.h * (self.yr[1] - self.yr[0])

    def draw(self, xticks, yticks, xlabel, ylabel, fmt_x=str, fmt_y=str, grid=True, minor_y=None, minor_x=None,
             ylabel_x=None, tick_labels=True, layer=None):
        f, L = self.fig, layer or self.layer
        for v in (minor_y or []):
            f.line(self.x0, self.Y(v), self.x0 + self.w, self.Y(v), '#eeeeee', 1, L)
        for v in (minor_x or []):
            f.line(self.X(v), self.y0, self.X(v), self.y0 + self.h, '#eeeeee', 1, L)
        if grid:
            for v in yticks:
                f.line(self.x0, self.Y(v), self.x0 + self.w, self.Y(v), '#d6d6d6', 1.2, L)
            for v in xticks:
                f.line(self.X(v), self.y0, self.X(v), self.y0 + self.h, '#d6d6d6', 1.2, L)
        f.line(self.x0, self.y0 + self.h, self.x0 + self.w, self.y0 + self.h, INK, 2.5, L)
        f.line(self.x0, self.y0, self.x0, self.y0 + self.h, INK, 2.5, L)
        for v in xticks:
            f.line(self.X(v), self.y0 + self.h, self.X(v), self.y0 + self.h + 8, INK, 2, L)
            if tick_labels:
                f.text(self.X(v), self.y0 + self.h + 36, fmt_x(v), 26, 'middle', layer=L)
        for v in yticks:
            f.line(self.x0 - 8, self.Y(v), self.x0, self.Y(v), INK, 2, L)
            if tick_labels:
                f.text(self.x0 - 14, self.Y(v) + 9, fmt_y(v), 26, 'end', layer=L)
        if xlabel:
            f.text(self.x0 + self.w / 2, self.y0 + self.h + 74, xlabel, 26, 'middle', 'bold', layer=L)
        if ylabel:
            lx = ylabel_x if ylabel_x is not None else self.x0 - 92
            f.text(lx, self.y0 + self.h / 2, ylabel, 26, 'middle', 'bold', rotate=-90, layer=L)

    def polyline(self, pts, stroke=INK, sw=4, layer=None, dash=None):
        d = 'M' + ' L'.join('%.2f %.2f' % (self.X(x), self.Y(y)) for x, y in pts)
        extra = 'stroke-dasharray="%s" stroke-linecap="round"' % dash if dash else 'stroke-linecap="round"'
        self.fig.path(d, 'none', stroke, sw, layer or self.layer, extra=extra)


def pchip(xs, ys):
    """Monotone piecewise-cubic Hermite interpolant (Fritsch-Carlson); returns f(x)."""
    n = len(xs)
    h = [xs[i + 1] - xs[i] for i in range(n - 1)]
    d = [(ys[i + 1] - ys[i]) / h[i] for i in range(n - 1)]
    m = [0.0] * n
    m[0], m[-1] = d[0], d[-1]
    for i in range(1, n - 1):
        if d[i - 1] * d[i] <= 0:
            m[i] = 0.0
        else:
            w1, w2 = 2 * h[i] + h[i - 1], h[i] + 2 * h[i - 1]
            m[i] = (w1 + w2) / (w1 / d[i - 1] + w2 / d[i])

    def fn(x):
        for i in range(n - 1):
            if xs[i] <= x <= xs[i + 1]:
                t = (x - xs[i]) / h[i]
                h00, h10 = 2 * t ** 3 - 3 * t ** 2 + 1, t ** 3 - 2 * t ** 2 + t
                h01, h11 = -2 * t ** 3 + 3 * t ** 2, t ** 3 - t ** 2
                return h00 * ys[i] + h10 * h[i] * m[i] + h01 * ys[i + 1] + h11 * h[i] * m[i + 1]
        raise ValueError(x)
    return fn


def smooth_closed(pts, n=10):
    """Sample a closed Catmull-Rom spline through pts; returns the dense point list (draw and test the same points)."""
    out = []
    m = len(pts)
    for i in range(m):
        p0, p1, p2, p3 = pts[i - 1], pts[i], pts[(i + 1) % m], pts[(i + 2) % m]
        for k in range(n):
            t = k / n
            t2, t3 = t * t, t * t * t
            out.append(tuple(0.5 * ((2 * p1[j]) + (-p0[j] + p2[j]) * t + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * t2
                                    + (-p0[j] + 3 * p1[j] - 3 * p2[j] + p3[j]) * t3) for j in (0, 1)))
    return out


def table(fig, x, y, colw, rowh, rows, layer='base', header_fill='#eef3f7', cell_layers=None, align=None):
    """Draw a ruled table. rows: list of lists of cell text (first row = header, bold).
    cell_layers: optional {(r, c): layer} to put a cell's text on another layer (e.g. answer-only values).
    align: optional list per column of 'start'/'middle'."""
    ncol = len(colw)
    tw = sum(colw)
    for r, row in enumerate(rows):
        fig.rect(x, y + r * rowh, tw, rowh, header_fill if r == 0 else '#ffffff', INK, 1.4, layer=layer)
        cx = x
        for c, cell in enumerate(row):
            if c:
                fig.line(cx, y + r * rowh, cx, y + (r + 1) * rowh, INK, 1.2, layer)
            if cell not in (None, ''):
                lay = (cell_layers or {}).get((r, c), layer)
                al = (align or ['start'] * ncol)[c]
                tx = cx + 10 if al == 'start' else cx + colw[c] / 2
                colr = C['answer'] if lay not in (layer, 'base') and lay.endswith('a') else INK
                fig.text(tx, y + r * rowh + rowh / 2 + 9, cell, 26, al, 'bold' if r == 0 else ('bold' if colr != INK else 'normal'),
                         colr, lay)
            cx += colw[c]
    return y + len(rows) * rowh
