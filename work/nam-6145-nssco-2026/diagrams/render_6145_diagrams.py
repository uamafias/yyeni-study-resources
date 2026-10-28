#!/usr/bin/env python3
"""
Render the 6145 diagram cards from their declarative specifications.

    python3 work/nam-6145-nssco-2026/diagrams/render_6145_diagrams.py [ITEM-ID ...]

Each card has one spec, diagrams/specs/<ITEM-ID>.json, holding the model (equations or
schedules), the axes and scales, and two layer lists: what the question side shows and what
the answer side shows. This script turns each side into an SVG master and then rasterises
that SVG to PNG with Playwright's Chromium, so the PNG is always a picture of the SVG.

Paths come from planning/revision-01/claude-visual-work-order.json; nothing is named by hand.

Every drawn mark carries data-* attributes in model units, and every plotting panel records
its data-to-pixel mapping, so verify_6145_diagrams.py can read the geometry back out of the
SVG and test it against independently calculated values.

Requires: Python 3, Playwright with its Chromium build (python3 -m playwright install chromium).
"""
import json
import math
import os
import sys
from xml.sax.saxutils import escape

HERE = os.path.dirname(os.path.abspath(__file__))
WS = os.path.dirname(HERE)
WORK_ORDER = os.path.join(WS, 'planning', 'revision-01', 'claude-visual-work-order.json')
SPECS = os.path.join(HERE, 'specs')

FONT = 'Arial, Helvetica, sans-serif'
INK = '#111111'
GRID = '#d9d9d9'
STYLES = {
    # Colour helps on screen; the dash pattern and width carry the distinction in greyscale.
    'demand': {'stroke': '#1f4e9c', 'width': 4.5, 'dash': None},
    'supply': {'stroke': '#b03a2e', 'width': 4.5, 'dash': None},
    'demand_new': {'stroke': '#1f4e9c', 'width': 4.5, 'dash': '16 10'},
    'supply_new': {'stroke': '#b03a2e', 'width': 4.5, 'dash': '16 10'},
    'supply_alt': {'stroke': '#6a3d9a', 'width': 4.5, 'dash': '16 10'},
    'curve': {'stroke': '#1f4e9c', 'width': 4.5, 'dash': None},
    'curve_alt': {'stroke': '#b03a2e', 'width': 4.5, 'dash': '16 10'},
    'control': {'stroke': '#1b6e3a', 'width': 4.0, 'dash': '22 8 4 8'},
    'guide': {'stroke': '#555555', 'width': 2.2, 'dash': '7 6'},
    'arrow': {'stroke': INK, 'width': 3.2, 'dash': None},
    'span': {'stroke': INK, 'width': 3.0, 'dash': None},
}


def load_work_order():
    wo = json.load(open(WORK_ORDER))
    return {c['slot_id']: c for c in wo['cards']}


def fmt(v):
    return ('%.2f' % v).rstrip('0').rstrip('.')


class Panel:
    """A plotting area with a linear data-to-pixel mapping."""

    def __init__(self, spec):
        self.px0, self.py0, self.pw, self.ph = spec['frame']  # pixel box of the plot area
        ax = spec['axes']
        self.x0, self.x1 = ax['x']['min'], ax['x']['max']
        self.y0, self.y1 = ax['y']['min'], ax['y']['max']
        self.spec = spec

    def X(self, x):
        return self.px0 + (x - self.x0) / (self.x1 - self.x0) * self.pw

    def Y(self, y):
        return self.py0 + self.ph - (y - self.y0) / (self.y1 - self.y0) * self.ph

    def mapping(self):
        return '%s,%s,%s,%s;%s,%s,%s,%s' % (fmt(self.x0), fmt(self.x1), fmt(self.px0), fmt(self.px0 + self.pw),
                                            fmt(self.y0), fmt(self.y1), fmt(self.py0 + self.ph), fmt(self.py0))


def evaluate(expr, **var):
    # Expressions are plain arithmetic in one variable, written in the spec.
    return float(eval(expr, {'__builtins__': {}, 'sqrt': math.sqrt}, var))


def line(x1, y1, x2, y2, st, extra=''):
    dash = ' stroke-dasharray="%s"' % st['dash'] if st.get('dash') else ''
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s"%s '
            'stroke-linecap="round"%s/>' % (fmt(x1), fmt(y1), fmt(x2), fmt(y2), st['stroke'], st['width'], dash, extra))


def text(x, y, s, size=28, anchor='start', weight='normal', fill=INK, extra='', halo=False):
    # A white halo keeps a label legible where it crosses a grid line or curve.
    h = (' stroke="#ffffff" stroke-width="7" paint-order="stroke" stroke-linejoin="round"' if halo else '')
    return ('<text x="%s" y="%s" font-family="%s" font-size="%s" text-anchor="%s" font-weight="%s" '
            'fill="%s"%s%s>%s</text>' % (fmt(x), fmt(y), FONT, size, anchor, weight, fill, h, extra, escape(s)))


def arrowhead(x1, y1, x2, y2, color, size=18):
    ang = math.atan2(y2 - y1, x2 - x1)
    a1, a2 = ang + math.radians(152), ang - math.radians(152)
    pts = [(x2, y2), (x2 + size * math.cos(a1), y2 + size * math.sin(a1)),
           (x2 + size * math.cos(a2), y2 + size * math.sin(a2))]
    return '<polygon points="%s" fill="%s"/>' % (' '.join('%s,%s' % (fmt(a), fmt(b)) for a, b in pts), color)


def draw_axes(p, out, marks=None):
    ax = p.spec['axes']
    marks = marks or {'x': [], 'y': []}
    show_grid = ax.get('grid', False)
    # Minor grid lines help plotting between labelled ticks; they carry no labels.
    for t in ax['x'].get('minor', []):
        if show_grid:
            out.append(line(p.X(t), p.Y(p.y0), p.X(t), p.Y(p.y1), {'stroke': '#ececec', 'width': 1.2}))
    for t in ax['y'].get('minor', []):
        if show_grid:
            out.append(line(p.X(p.x0), p.Y(t), p.X(p.x1), p.Y(t), {'stroke': '#ececec', 'width': 1.2}))
    for t in ax['x'].get('ticks', []):
        if show_grid and t != p.x0:
            out.append(line(p.X(t), p.Y(p.y0), p.X(t), p.Y(p.y1), {'stroke': GRID, 'width': 1.5}))
    for t in ax['y'].get('ticks', []):
        if show_grid and t != p.y0:
            out.append(line(p.X(p.x0), p.Y(t), p.X(p.x1), p.Y(t), {'stroke': GRID, 'width': 1.5}))
    ink = {'stroke': INK, 'width': 3.2}
    # Axes start at the origin of the data range and end in an arrowhead.
    out.append(line(p.X(p.x0), p.Y(p.y0), p.X(p.x1) + 18, p.Y(p.y0), ink))
    out.append(arrowhead(p.X(p.x1), p.Y(p.y0), p.X(p.x1) + 26, p.Y(p.y0), INK, 20))
    out.append(line(p.X(p.x0), p.Y(p.y0), p.X(p.x0), p.Y(p.y1) - 18, ink))
    out.append(arrowhead(p.X(p.x0), p.Y(p.y1), p.X(p.x0), p.Y(p.y1) - 26, INK, 20))
    fs = ax.get('tick_size', 27)
    if ax['x'].get('tick_labels', True):
        for t in ax['x'].get('ticks', []):
            out.append(line(p.X(t), p.Y(p.y0), p.X(t), p.Y(p.y0) + 9, ink))
            # A tick label that would collide with a marked value (for example 35 beside 40) gives way.
            crowded = any(abs(p.X(t) - p.X(m)) < 48 and t != m for m in marks['x'])
            if (t != p.x0 or not ax.get('shared_zero', True)) and not crowded:
                out.append(text(p.X(t), p.Y(p.y0) + 38, fmt(t), fs, 'middle'))
    if ax['y'].get('tick_labels', True):
        for t in ax['y'].get('ticks', []):
            out.append(line(p.X(p.x0) - 9, p.Y(t), p.X(p.x0), p.Y(t), ink))
            crowded = any(abs(p.Y(t) - p.Y(m)) < 30 and t != m for m in marks['y'])
            if (t != p.y0 or not ax.get('shared_zero', True)) and not crowded:
                out.append(text(p.X(p.x0) - 15, p.Y(t) + 8, fmt(t), fs, 'end'))
    if ax.get('shared_zero', True) and ax['x'].get('tick_labels', True):
        out.append(text(p.X(p.x0) - 15, p.Y(p.y0) + 34, '0', fs, 'end'))
    ts = ax.get('title_size', 28)
    xt = ax['x'].get('title')
    if xt:
        out.append(text(p.X(p.x1) + 30, p.Y(p.y0) + ax['x'].get('title_dy', 76), xt, ts, 'end', 'bold',
                        extra=' data-role="x-title"'))
    yt = ax['y'].get('title')
    if yt:
        out.append(text(p.X(p.x0) + ax['y'].get('title_dx', -12), p.Y(p.y1) - 40, yt, ts,
                        ax['y'].get('title_anchor', 'start'), 'bold', extra=' data-role="y-title"'))


def sample(el, p):
    kind = el['kind']
    if kind == 'points':
        return [tuple(pt) for pt in el['points']]
    lo, hi = el['domain']
    n = el.get('samples', 200)
    vals = [lo + (hi - lo) * i / n for i in range(n + 1)]
    if kind == 'y_of_x':
        return [(v, evaluate(el['expr'], x=v)) for v in vals]
    if kind == 'x_of_y':
        return [(evaluate(el['expr'], y=v), v) for v in vals]
    raise ValueError('unknown curve kind %s' % kind)


def draw_curve(el, p, out):
    st = dict(STYLES[el.get('style', 'curve')])
    pts = sample(el, p)
    d = 'M ' + ' L '.join('%s %s' % (fmt(p.X(x)), fmt(p.Y(y))) for x, y in pts)
    dash = ' stroke-dasharray="%s"' % st['dash'] if st.get('dash') else ''
    attrs = ' data-role="curve" data-id="%s" data-kind="%s"' % (escape(el['id']), el['kind'])
    if 'expr' in el:
        attrs += ' data-expr="%s" data-domain="%s,%s"' % (escape(el['expr']), fmt(el['domain'][0]), fmt(el['domain'][1]))
    out.append('<path d="%s" fill="none" stroke="%s" stroke-width="%s"%s stroke-linejoin="round" '
               'stroke-linecap="round"%s/>' % (d, st['stroke'], st['width'], dash, attrs))
    lab = el.get('label')
    if lab:
        x, y = lab['at']
        out.append(text(p.X(x) + lab.get('dx', 0), p.Y(y) + lab.get('dy', 0), lab['text'], lab.get('size', 30),
                        lab.get('anchor', 'start'), 'bold', st['stroke'], halo=True,
                        extra=' data-role="curve-label" data-for="%s"' % escape(el['id'])))


def draw_point(el, p, out):
    x, y = el['at']
    cx, cy = p.X(x), p.Y(y)
    guides = el.get('guides')
    if guides:
        # true draws both projections; 'x' only the drop to the quantity axis, 'y' only the line to the price axis.
        g = STYLES['guide']
        if guides in (True, 'y'):
            out.append(line(cx, cy, p.X(p.x0), cy, g, ' data-role="guide"'))
        if guides in (True, 'x'):
            out.append(line(cx, cy, cx, p.Y(p.y0), g, ' data-role="guide"'))
    for side, s in (el.get('axis_labels') or {}).items():
        if side == 'x':
            out.append(text(cx, p.Y(p.y0) + 38, s, 24, 'middle', 'bold', halo=True, extra=' data-role="axis-mark"'))
        else:
            out.append(text(p.X(p.x0) - 15, cy + 8, s, 24, 'end', 'bold', halo=True, extra=' data-role="axis-mark"'))
    marker = el.get('marker', 'dot')
    attrs = ' data-role="point" data-id="%s" data-x="%s" data-y="%s"' % (escape(el['id']), fmt(x), fmt(y))
    if marker == 'dot':
        out.append('<circle cx="%s" cy="%s" r="9" fill="%s" stroke="#ffffff" stroke-width="2.5"%s/>'
                   % (fmt(cx), fmt(cy), el.get('fill', INK), attrs))
    elif marker == 'ring':
        out.append('<circle cx="%s" cy="%s" r="10" fill="#ffffff" stroke="%s" stroke-width="4"%s/>'
                   % (fmt(cx), fmt(cy), el.get('fill', INK), attrs))
    elif marker == 'cross':
        out.append('<g%s>%s%s</g>' % (attrs, line(cx - 11, cy - 11, cx + 11, cy + 11, {'stroke': INK, 'width': 4}),
                                      line(cx - 11, cy + 11, cx + 11, cy - 11, {'stroke': INK, 'width': 4})))
    lab = el.get('label')
    if lab:
        out.append(text(cx + lab.get('dx', 14), cy + lab.get('dy', -14), lab['text'], lab.get('size', 28),
                        lab.get('anchor', 'start'), lab.get('weight', 'bold'), halo=True,
                        extra=' data-role="point-label" data-for="%s"' % escape(el['id'])))


def draw_hline(el, p, out):
    st = STYLES[el.get('style', 'control')]
    y = el['y']
    x1, x2 = el.get('from_x', p.x0), el.get('to_x', p.x1)
    out.append(line(p.X(x1), p.Y(y), p.X(x2), p.Y(y), st,
                    ' data-role="hline" data-id="%s" data-y="%s"' % (escape(el['id']), fmt(y))))
    lab = el.get('label')
    if lab:
        out.append(text(p.X(lab.get('x', x2)) + lab.get('dx', 8), p.Y(y) + lab.get('dy', -12), lab['text'],
                        lab.get('size', 26), lab.get('anchor', 'start'), 'bold', st['stroke'], halo=True))


def draw_arrow(el, p, out):
    st = STYLES[el.get('style', 'arrow')]
    (x1, y1), (x2, y2) = el['from'], el['to']
    a, b, c, d = p.X(x1), p.Y(y1), p.X(x2), p.Y(y2)
    # Shorten both ends so the arrow does not cover the points it joins.
    L = math.hypot(c - a, d - b)
    trim0, trim1 = el.get('trim', [14, 16])
    ux, uy = (c - a) / L, (d - b) / L
    # An optional sideways offset keeps a movement arrow off the curve it follows.
    off = el.get('offset_px', 0)
    a, b, c, d = a + uy * off, b - ux * off, c + uy * off, d - ux * off
    a, b, c, d = a + ux * trim0, b + uy * trim0, c - ux * trim1, d - uy * trim1
    out.append(line(a, b, c - ux * 10, d - uy * 10, st,
                    ' data-role="arrow" data-id="%s" data-from="%s,%s" data-to="%s,%s" data-offset-px="%s"'
                    % (escape(el['id']), fmt(x1), fmt(y1), fmt(x2), fmt(y2), fmt(off))))
    out.append(arrowhead(a, b, c, d, st['stroke'], 22))
    lab = el.get('label')
    if lab:
        out.append(text((a + c) / 2 + lab.get('dx', 0), (b + d) / 2 + lab.get('dy', 0), lab['text'],
                        lab.get('size', 26), lab.get('anchor', 'start'), 'bold', halo=True))


def draw_span(el, p, out):
    """A two-headed horizontal measure, used for shortages, surpluses and changes in quantity."""
    st = STYLES['span']
    y = el['y']
    x1, x2 = el['x1'], el['x2']
    py = p.Y(y) + el.get('offset_px', 0)
    a, c = p.X(x1), p.X(x2)
    out.append(line(a + 12, py, c - 12, py, st, ' data-role="span" data-id="%s" data-x1="%s" data-x2="%s" data-y="%s"'
                    % (escape(el['id']), fmt(x1), fmt(x2), fmt(y))))
    out.append(arrowhead(c, py, a, py, INK, 18))
    out.append(arrowhead(a, py, c, py, INK, 18))
    for xx in (a, c):
        out.append(line(xx, py - 12, xx, py + 12, st))
    lab = el.get('label')
    if lab:
        out.append(text((a + c) / 2 + lab.get('dx', 0), py + lab.get('dy', -14), lab['text'], lab.get('size', 26),
                        'middle', 'bold', halo=True))


def draw_text(el, p, out):
    if 'px' in el:
        x, y = el['px']
    else:
        x, y = p.X(el['at'][0]), p.Y(el['at'][1])
    lines = el['text'] if isinstance(el['text'], list) else [el['text']]
    for i, s in enumerate(lines):
        out.append(text(x + el.get('dx', 0), y + el.get('dy', 0) + i * el.get('leading', 32), s,
                        el.get('size', 26), el.get('anchor', 'start'), el.get('weight', 'normal'),
                        el.get('fill', INK), halo=el.get('halo', True)))


def draw_table(el, out):
    x, y = el['px']
    widths = el['col_widths']
    rh = el.get('row_height', 46)
    fs = el.get('size', 28)
    rows = [el['header']] + el['rows']
    W = sum(widths)
    out.append('<g data-role="table" data-id="%s">' % escape(el.get('id', 'table')))
    if el.get('title'):
        out.append(text(x, y - 14, el['title'], fs, 'start', 'bold'))
    out.append('<rect x="%s" y="%s" width="%s" height="%s" fill="#f1f4f9" stroke="%s" stroke-width="2"/>'
               % (fmt(x), fmt(y), fmt(W), fmt(rh), INK))
    out.append('<rect x="%s" y="%s" width="%s" height="%s" fill="none" stroke="%s" stroke-width="2"/>'
               % (fmt(x), fmt(y), fmt(W), fmt(rh * len(rows)), INK))
    for r in range(1, len(rows)):
        out.append(line(x, y + r * rh, x + W, y + r * rh, {'stroke': '#888888', 'width': 1.5}))
    cx = x
    for w in widths[:-1]:
        cx += w
        out.append(line(cx, y, cx, y + rh * len(rows), {'stroke': '#888888', 'width': 1.5}))
    for r, row in enumerate(rows):
        cx = x
        for c, cell in enumerate(row):
            out.append(text(cx + widths[c] / 2, y + r * rh + rh / 2 + fs * 0.36, str(cell), fs, 'middle',
                            'bold' if r == 0 else 'normal',
                            extra=' data-role="cell" data-row="%d" data-col="%d"' % (r, c)))
            cx += widths[c]
    out.append('</g>')


DRAW = {'curve': draw_curve, 'point': draw_point, 'hline': draw_hline, 'arrow': draw_arrow,
        'span': draw_span, 'text': draw_text}


def side_canvas(spec, side):
    # A side may declare its own canvas, for example a question that shows only a data table.
    return tuple(spec[side].get('canvas', spec['canvas']))


def build_side(spec, side):
    W, H = side_canvas(spec, side)
    out = ['<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" '
           'data-item="%s" data-side="%s">' % (W, H, W, H, spec['item_id'], side),
           '<title>%s</title>' % escape(spec[side]['title']),
           '<desc>%s</desc>' % escape(spec[side]['description']),
           '<rect width="100%" height="100%" fill="#ffffff"/>']
    for el in spec[side].get('static', []):
        if el['type'] == 'table':
            draw_table(el, out)
        elif el['type'] == 'text':
            draw_text(el, None, out)
    for pspec in spec['panels']:
        if side not in pspec.get('sides', ['question', 'answer']):
            continue
        p = Panel(pspec)
        out.append('<g data-role="panel" data-id="%s" data-map="%s">' % (escape(pspec['id']), p.mapping()))
        if pspec.get('heading'):
            out.append(text(p.px0 + p.pw / 2, p.py0 - pspec.get('heading_dy', 70), pspec['heading'], 28, 'middle', 'bold'))
        marks = {'x': [], 'y': []}
        for el in pspec.get(side, []):
            for k in (el.get('axis_labels') or {}):
                marks[k].append(el['at'][0 if k == 'x' else 1])
        draw_axes(p, out, marks)
        for el in pspec.get(side, []):
            DRAW[el['type']](el, p, out)
        out.append('</g>')
    out.append('</svg>')
    return '\n'.join(out) + '\n'


def rasterise(jobs):
    """Render each SVG to PNG with Chromium at 1.5x, so a 1000-px master gives a 1500-px PNG."""
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        for svg_path, png_path, (W, H) in jobs:
            page = browser.new_page(viewport={'width': W, 'height': H}, device_scale_factor=1.5)
            page.set_content('<html><body style="margin:0;background:#fff">%s</body></html>'
                             % open(svg_path).read().split('?>', 1)[-1])
            page.wait_for_timeout(100)
            page.screenshot(path=png_path, clip={'x': 0, 'y': 0, 'width': W, 'height': H})
            # Record the laid-out box of every text element, as the browser measured it, so the
            # verifier can test clipping and label collisions on real widths rather than guesses.
            boxes = page.evaluate('''() => Array.from(document.querySelectorAll('svg text')).map(t => {
                const b = t.getBBox(); return {text: t.textContent, x: b.x, y: b.y, w: b.width, h: b.height}; })''')
            json.dump(boxes, open(os.path.join(HERE, 'checks', os.path.basename(png_path)[:-4] + '.textboxes.json'), 'w'), indent=1)
            page.close()
        browser.close()


def render(item_ids=None):
    wo = load_work_order()
    names = sorted(f[:-5] for f in os.listdir(SPECS) if f.endswith('.json'))
    if item_ids:
        names = [n for n in names if n in item_ids]
    jobs = []
    os.makedirs(os.path.join(HERE, 'checks'), exist_ok=True)
    for name in names:
        spec = json.load(open(os.path.join(SPECS, name + '.json')))
        card = wo[spec['item_id']]
        for side in ('question', 'answer'):
            svg_path = os.path.join(WS, card[side + '_svg'])
            png_path = os.path.join(WS, card[side + '_png'])
            os.makedirs(os.path.dirname(svg_path), exist_ok=True)
            open(svg_path, 'w').write(build_side(spec, side))
            jobs.append((svg_path, png_path, side_canvas(spec, side)))
            print('svg  ->', os.path.relpath(svg_path, WS))
    rasterise(jobs)
    for _, png, _ in jobs:
        print('png  ->', os.path.relpath(png, WS))


if __name__ == '__main__':
    render(sys.argv[1:] or None)
