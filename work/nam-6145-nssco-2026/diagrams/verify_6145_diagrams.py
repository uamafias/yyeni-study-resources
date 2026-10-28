#!/usr/bin/env python3
"""
Check the 6145 diagram cards against independently calculated values.

    python3 work/nam-6145-nssco-2026/diagrams/verify_6145_diagrams.py [ITEM-ID ...]

The renderer draws from the spec. This script does not trust the spec: each card has its own
check function below, with the model written out again by hand and the expected values solved
with exact fractions. It then reads the drawn geometry back out of the SVG (pixel positions
inverted through each panel's recorded mapping) and compares it with those values, checks the
card's text states the same numbers, and checks the question side does not carry the solution.

It also writes phone-width (390 px) and greyscale previews to diagrams/inspection/ for the
visual pass. Those previews are for people to look at; this script cannot judge legibility.

Results go to diagrams/checks/<ITEM-ID>.json. Exit status is 1 if any check fails.
"""
import hashlib
import json
import os
import re
import sys
import xml.etree.ElementTree as ET
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
WS = os.path.dirname(HERE)
WORK_ORDER = os.path.join(WS, 'planning', 'revision-01', 'claude-visual-work-order.json')
NS = '{http://www.w3.org/2000/svg}'
PX_TOL = 1.5          # pixels: drawn position against the expected position
SCALE = 1.5           # PNG pixels per SVG unit (renderer's device scale factor)


def sha(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()


class Side:
    """One rendered side: its SVG tree, panel mappings and helpers to read geometry back."""

    def __init__(self, path):
        self.path = path
        self.root = ET.parse(path).getroot()
        self.W = float(self.root.get('width'))
        self.H = float(self.root.get('height'))
        self.panels = {}
        for g in self.root.iter(NS + 'g'):
            if g.get('data-role') == 'panel':
                xs, ys = g.get('data-map').split(';')
                x0, x1, px0, px1 = map(float, xs.split(','))
                y0, y1, py0, py1 = map(float, ys.split(','))
                self.panels[g.get('data-id')] = (g, (x0, x1, px0, px1), (y0, y1, py0, py1))

    def to_data(self, panel, px, py):
        _, (x0, x1, px0, px1), (y0, y1, py0, py1) = self.panels[panel]
        return (x0 + (px - px0) / (px1 - px0) * (x1 - x0), y0 + (py - py0) / (py1 - py0) * (y1 - y0))

    def px_per_unit(self, panel):
        _, (x0, x1, px0, px1), (y0, y1, py0, py1) = self.panels[panel]
        return abs(px1 - px0) / (x1 - x0), abs(py1 - py0) / (y1 - y0)

    def in_box(self, panel, px, py, slack=3):
        _, (x0, x1, px0, px1), (y0, y1, py0, py1) = self.panels[panel]
        return min(px0, px1) - slack <= px <= max(px0, px1) + slack and min(py0, py1) - slack <= py <= max(py0, py1) + slack

    def elements(self, role, panel=None):
        scope = self.panels[panel][0] if panel else self.root
        return [e for e in scope.iter() if e.get('data-role') == role]

    def by_id(self, role, ident, panel=None):
        hits = [e for e in self.elements(role, panel) if e.get('data-id') == ident]
        return hits[0] if hits else None

    def point(self, panel, ident):
        e = self.by_id('point', ident, panel)
        if e is None:
            return None
        if e.tag == NS + 'circle':
            return self.to_data(panel, float(e.get('cx')), float(e.get('cy')))
        ln = e.find(NS + 'line')  # a cross: the centre is the midpoint of either stroke
        return self.to_data(panel, (float(ln.get('x1')) + float(ln.get('x2'))) / 2,
                            (float(ln.get('y1')) + float(ln.get('y2'))) / 2)

    def curve(self, panel, ident):
        e = self.by_id('curve', ident, panel)
        if e is None:
            return None
        nums = [float(v) for v in re.findall(r'-?\d+(?:\.\d+)?', e.get('d'))]
        pix = list(zip(nums[0::2], nums[1::2]))
        return [self.to_data(panel, a, b) for a, b in pix], pix

    def texts(self):
        out = []
        for t in self.root.iter(NS + 'text'):
            out.append({'text': t.text or '', 'x': float(t.get('x')), 'y': float(t.get('y')),
                        'size': float(t.get('font-size')), 'anchor': t.get('text-anchor'),
                        'bold': t.get('font-weight') == 'bold', 'role': t.get('data-role')})
        return out

    def all_text(self):
        return ' '.join(t['text'] for t in self.texts())


def text_box(t):
    # Arial averages about 0.55 em per character (0.6 em bold); good enough to find clashes.
    w = len(t['text']) * t['size'] * (0.6 if t['bold'] else 0.55)
    h = t['size']
    x0 = {'start': t['x'], 'middle': t['x'] - w / 2, 'end': t['x'] - w}[t['anchor']]
    return (x0, t['y'] - 0.8 * h, x0 + w, t['y'] + 0.25 * h)


def overlap(a, b):
    return not (a[2] <= b[0] or b[2] <= a[0] or a[3] <= b[1] or b[3] <= a[1])


class Report:
    def __init__(self, item):
        self.item = item
        self.rows = []

    def check(self, name, ok, detail=''):
        self.rows.append({'check': name, 'result': 'pass' if ok else 'FAIL', 'detail': detail})
        return ok

    def note(self, name, detail):
        self.rows.append({'check': name, 'result': 'note', 'detail': detail})

    @property
    def failed(self):
        return [r for r in self.rows if r['result'] == 'FAIL']


def generic_checks(R, card, sides):
    """Checks every card gets: files, sizes, curves inside their axes, text inside the canvas."""
    from PIL import Image
    for side in ('question', 'answer'):
        S = sides[side]
        png = os.path.join(WS, card[side + '_png'])
        R.check('%s PNG exists' % side, os.path.exists(png), card[side + '_png'])
        im = Image.open(png)
        R.check('%s PNG is 1.5x the SVG canvas' % side,
                im.size == (round(S.W * SCALE), round(S.H * SCALE)), '%s vs %s' % (im.size, (S.W, S.H)))
        for pid in S.panels:
            for e in S.elements('curve', pid):
                _, pix = S.curve(pid, e.get('data-id'))
                outside = [p for p in pix if not S.in_box(pid, *p)]
                R.check('%s curve %s stays inside its axes' % (side, e.get('data-id')), not outside,
                        '%d of %d vertices outside' % (len(outside), len(pix)))
        tb = os.path.join(HERE, 'checks', os.path.basename(card[side + '_png'])[:-4] + '.textboxes.json')
        if os.path.exists(tb):
            # Boxes measured by the browser at render time.
            boxes = [({'text': b['text']}, (b['x'], b['y'], b['x'] + b['w'], b['y'] + b['h'])) for b in json.load(open(tb))]
            how = 'measured'
        else:
            boxes = [(t, text_box(t)) for t in S.texts()]
            how = 'estimated'
        off = [t['text'] for t, b in boxes if b[0] < 0 or b[2] > S.W or b[1] < 0 or b[3] > S.H]
        R.check('%s text inside the canvas (%s widths)' % (side, how), not off, '; '.join(off))
        clashes = []
        for i in range(len(boxes)):
            for j in range(i + 1, len(boxes)):
                if overlap(boxes[i][1], boxes[j][1]):
                    clashes.append('%r / %r' % (boxes[i][0]['text'], boxes[j][0]['text']))
        R.check('%s no text boxes overlap (%s widths)' % (side, how), not clashes, '; '.join(clashes))
        # Point markers should not sit under a label.
        under = []
        for pid in S.panels:
            for e in S.elements('point', pid):
                if e.tag != NS + 'circle':
                    continue
                cx, cy = float(e.get('cx')), float(e.get('cy'))
                mb = (cx - 9, cy - 9, cx + 9, cy + 9)
                for t, b in boxes:
                    if overlap(mb, b):
                        under.append('%s under %r' % (e.get('data-id'), t['text']))
        R.check('%s no point marker under a label' % side, not under, '; '.join(under))


def write_previews(card):
    from PIL import Image
    out = os.path.join(HERE, 'inspection')
    os.makedirs(out, exist_ok=True)
    made = []
    for side in ('question', 'answer'):
        src = os.path.join(WS, card[side + '_png'])
        im = Image.open(src).convert('RGB')
        base = os.path.splitext(os.path.basename(src))[0]
        w = 390
        phone = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
        p1 = os.path.join(out, base + '-phone390.png')
        phone.save(p1)
        p2 = os.path.join(out, base + '-grey.png')
        im.convert('L').save(p2)
        made += [os.path.relpath(p1, WS), os.path.relpath(p2, WS)]
    return made


def load_item(card):
    path = os.path.join(WS, 'topics', card['topic_id'], 'learning-items', 'topic_%s_items.json' % card['topic_id'])
    for it in json.load(open(path))['items']:
        if it['item_id'] == card['slot_id']:
            return it
    return None


def near(a, b, tol):
    return abs(a - b) <= tol


def check_points(R, S, panel, expected, label):
    ux, uy = S.px_per_unit(panel)
    for k, (x, y) in expected.items():
        got = S.point(panel, k)
        ok = got is not None and near(got[0], float(x), PX_TOL / ux) and near(got[1], float(y), PX_TOL / uy)
        R.check('%s point %s drawn at (%s, %s)' % (label, k, x, y), ok, 'read back %s' % (got,))


def seg_dist(px, py, pts):
    """Shortest distance in pixels from (px, py) to a drawn polyline."""
    best = float('inf')
    for (ax, ay), (bx, by) in zip(pts, pts[1:]):
        dx, dy = bx - ax, by - ay
        L2 = dx * dx + dy * dy
        t = 0 if L2 == 0 else max(0, min(1, ((px - ax) * dx + (py - ay) * dy) / L2))
        best = min(best, ((ax + t * dx - px) ** 2 + (ay + t * dy - py) ** 2) ** 0.5)
    return best


def check_curve_fn(R, S, panel, ident, fn, label, through=()):
    """Every drawn vertex satisfies y = fn(x) within a pixel and a half; the curve passes the points."""
    got = S.curve(panel, ident)
    if not R.check('%s curve %s present' % (label, ident), got is not None):
        return
    data, _ = got
    ux, uy = S.px_per_unit(panel)
    worst = max(abs(y - float(fn(F(x).limit_denominator(10 ** 6)))) * uy for x, y in data)
    R.check('%s curve %s follows its equation' % (label, ident), worst <= PX_TOL, 'worst vertical error %.2f px' % worst)
    pts = [(dx * ux, dy * uy) for dx, dy in data]
    for (x, y) in through:
        d = seg_dist(float(x) * ux, float(y) * uy, pts)
        R.check('%s curve %s passes through (%s, %s)' % (label, ident, x, y), d <= PX_TOL, '%.2f px' % d)


def check_curve_x_of_y(R, S, panel, ident, g, label, through=()):
    """Every drawn vertex satisfies x = g(y) within a pixel and a half; the curve passes the points."""
    got = S.curve(panel, ident)
    if not R.check('%s curve %s present' % (label, ident), got is not None):
        return
    data, _ = got
    ux, uy = S.px_per_unit(panel)
    worst = max(abs(x - float(g(F(y).limit_denominator(10 ** 6)))) * ux for x, y in data)
    R.check('%s curve %s follows its equation' % (label, ident), worst <= PX_TOL, 'worst horizontal error %.2f px' % worst)
    pts = [(dx * ux, dy * uy) for dx, dy in data]
    for (x, y) in through:
        d = seg_dist(float(x) * ux, float(y) * uy, pts)
        R.check('%s curve %s passes through (%s, %s)' % (label, ident, x, y), d <= PX_TOL, '%.2f px' % d)


def check_arrow(R, S, panel, ident, frm, to, label):
    a = S.by_id('arrow', ident, panel)
    ok = a is not None and a.get('data-from') == '%s,%s' % frm and a.get('data-to') == '%s,%s' % to
    if ok:
        # The drawn shaft must point the same way as the movement it claims to show.
        dx_px, dy_px = float(a.get('x2')) - float(a.get('x1')), float(a.get('y2')) - float(a.get('y1'))
        ux, uy = S.px_per_unit(panel)
        ex, ey = (to[0] - frm[0]) * ux, -(to[1] - frm[1]) * uy
        cos = (dx_px * ex + dy_px * ey) / ((dx_px ** 2 + dy_px ** 2) ** 0.5 * (ex ** 2 + ey ** 2) ** 0.5)
        ok = cos > 0.999
    R.check('%s arrow %s runs from %s to %s' % (label, ident, frm, to), ok)


def check_text_has(R, label, text, needles):
    missing = [n for n in needles if n not in text]
    R.check(label, not missing, 'missing: %s' % missing if missing else 'all present')


def check_no_leak(R, question_text, forbidden):
    leaked = [f for f in forbidden if f.lower() in question_text.lower()]
    R.check('question side carries none of the solution labels', not leaked, 'leaked: %s' % leaked if leaked else '')


# ---------------------------------------------------------------------------------------------
# Card checks. Each one restates its model by hand and solves it with exact fractions.
# ---------------------------------------------------------------------------------------------

def card_ppc(R, card, sides, item):
    """1.1-011: PPC cattle = 80 - maize^2/500, A..E at maize 0, 50, 100, 150, 200."""
    f = lambda m: F(80) - F(m) ** 2 / 500
    sched = {k: (m, f(m)) for k, m in zip('ABCDE', (0, 50, 100, 150, 200))}
    R.check('schedule solves to A80 B75 C60 D35 E0',
            [sched[k][1] for k in 'ABCDE'] == [80, 75, 60, 35, 0], str({k: str(v[1]) for k, v in sched.items()}))
    steps = [sched[a][1] - sched[b][1] for a, b in ('AB', 'BC', 'CD', 'DE')]
    R.check('opportunity cost of each 50 t of maize rises (bowed-out curve)',
            steps == [5, 15, 25, 35] and all(steps[i] < steps[i + 1] for i in range(3)), str([str(s) for s in steps]))
    J, K = (50, 40), (100, 80)
    R.check('J is inside: at 50 t the district could have 75 cattle, more than 40', f(J[0]) > J[1], 'f(50)=%s' % f(J[0]))
    # K is unattainable only if no frontier point has at least 100 t maize AND at least 80 cattle.
    attain = [m for m in range(K[0], 201) if f(m) >= K[1]]
    R.check('K is outside: no frontier point gives 100 t and 80 cattle', not attain and f(K[0]) < K[1],
            'f(100)=%s' % f(K[0]))
    oc = sched['C'][1] - sched['D'][1]
    R.check('C to D: +50 t maize costs 25 cattle', oc == 25 and sched['D'][0] - sched['C'][0] == 50, 'oc=%s' % oc)

    Q, A = sides['question'], sides['answer']
    cells = [t['text'] for t in Q.texts() if t['role'] == 'cell']
    R.check('question table shows the schedule exactly',
            cells == ['Combination', 'A', 'B', 'C', 'D', 'E', 'Maize (tonnes)', '0', '50', '100', '150', '200',
                      'Cattle (head)', '80', '75', '60', '35', '0'], str(cells))
    check_text_has(R, 'question states J and K', Q.all_text(), ['J: 50 t maize and 40 cattle', 'K: 100 t maize and 80 cattle'])
    R.check('question side draws no curve or point', not Q.elements('curve') and not Q.elements('point'))
    check_no_leak(R, Q.all_text(), ['PPC', 'inside', 'outside', 'unattainable', 'inefficient', 'opportunity cost'])

    check_curve_fn(R, A, 'ppc', 'PPC', f, 'answer', through=[sched[k] for k in 'ABCDE'])
    check_points(R, A, 'ppc', dict(sched, J=J, K=K), 'answer')
    a1, a2 = A.by_id('arrow', 'C-across', 'ppc'), A.by_id('arrow', 'down-to-D', 'ppc')
    R.check('answer arrow runs right from C by 50 t at 60 cattle', a1 is not None and a1.get('data-from') == '100,60'
            and a1.get('data-to') == '150,60' and float(a1.get('x2')) > float(a1.get('x1'))
            and abs(float(a1.get('y2')) - float(a1.get('y1'))) < 0.01)
    R.check('answer arrow runs down to D by 25 cattle', a2 is not None and a2.get('data-from') == '150,60'
            and a2.get('data-to') == '150,35' and float(a2.get('y2')) > float(a2.get('y1'))
            and abs(float(a2.get('x2')) - float(a2.get('x1'))) < 0.01)
    check_text_has(R, 'answer arrows are labelled with the change', A.all_text(), ['+50 t maize', '\u221225 cattle'])
    ticks = [t['text'] for t in A.texts() if t['role'] is None and t['anchor'] == 'end' and t['text'] in ('20', '40', '60', '80', '100')]
    R.check('answer keeps every cattle tick label, so J and K can be read', sorted(ticks, key=int) == ['20', '40', '60', '80', '100'], str(ticks))
    check_text_has(R, 'answer image states the result', A.all_text(),
                   ['inside', 'outside', 'unattainable', '50 t more maize, 25 fewer cattle', '= 25 cattle'])

    if R.check('learning item exists', item is not None):
        check_text_has(R, 'prompt gives the facts the answer uses', item['prompt'], ['maize', 'J', 'K', 'C', 'D'])
        check_text_has(R, 'canonical answer states the values', item['canonical_answer'],
                       ['(0, 80)', '(50, 75)', '(100, 60)', '(150, 35)', '(200, 0)', 'J (50, 40)', 'K (100, 80)', '25 cattle', '50 t'])
        g = ' '.join(item['marking_guidance']).lower()
        check_text_has(R, 'guidance names the PROC parts', g, ['diagram', 'labels', 'original', 'change'])
        marks = sum(int(m) for m in re.findall(r'\((\d)\)', ' '.join(item['marking_guidance'])))
        R.check('guidance allocates the 4-mark tariff', marks == item['mark_tariff'] == 4, 'sum %d' % marks)


def card_ped(R, card, sides, item):
    """3.3-019: two demand curves through R (100, N$20); price rises to N$30."""
    P0, P1, Q0 = F(20), F(30), F(100)
    pct_p = (P1 - P0) / P0
    data = {'maize': F(75), 'crisps': F(25)}
    ped = {k: ((q - Q0) / Q0) / pct_p for k, q in data.items()}
    R.check('price change is +50%', pct_p == F(1, 2))
    R.check('maize meal PED = -25% / 50% = -0.5, inelastic', ped['maize'] == F(-1, 2) and abs(ped['maize']) < 1)
    R.check('crisps PED = -75% / 50% = -1.5, elastic', ped['crisps'] == F(-3, 2) and abs(ped['crisps']) > 1)
    # Straight lines through the two observed points of each product, written as Q = a - bP.
    def through(q0, p0, q1, p1):
        b = (q0 - q1) / (p1 - p0)
        return lambda p: q0 + b * p0 - b * F(p)
    g_m, g_c = through(Q0, P0, data['maize'], P1), through(Q0, P0, data['crisps'], P1)
    R.check('maize line is Q = 150 - 2.5P', g_m(0) == 150 and g_m(1) == F(295, 2))
    R.check('crisps line is Q = 250 - 7.5P', g_c(0) == 250 and g_c(1) == F(485, 2))

    Q, A = sides['question'], sides['answer']
    cells = [t['text'] for t in Q.texts() if t['role'] == 'cell']
    R.check('question table shows the data exactly', cells == [
        'Product', 'Old price', 'New price', 'Old sales', 'New sales',
        'Maize meal', 'N$20', 'N$30', '100', '75', 'Crisps (one brand)', 'N$20', 'N$30', '100', '25'], str(cells))
    R.check('question side draws no curve or point', not Q.elements('curve') and not Q.elements('point'))
    check_no_leak(R, Q.all_text(), ['inelastic', 'elastic', '\u22120.5', '\u22121.5', '-0.5', '-1.5', 'D maize', 'D crisps'])

    check_curve_x_of_y(R, A, 'ped', 'D-maize', g_m, 'answer', through=[(100, 20), (75, 30)])
    check_curve_x_of_y(R, A, 'ped', 'D-crisps', g_c, 'answer', through=[(100, 20), (25, 30)])
    check_points(R, A, 'ped', {'R': (100, 20), 'M': (75, 30), 'C': (25, 30)}, 'answer')
    check_arrow(R, A, 'ped', 'R-to-M', (100, 20), (75, 30), 'answer')
    check_arrow(R, A, 'ped', 'R-to-C', (100, 20), (25, 30), 'answer')
    # On one set of axes and from one point, the more elastic curve must be the flatter one on screen.
    ux, uy = A.px_per_unit('ped')
    steep = {k: abs(F(10) * F(uy).limit_denominator(10**6) / ((Q0 - q) * F(ux).limit_denominator(10**6))) for k, q in data.items()}
    R.check('elastic crisps curve is drawn flatter than inelastic maize curve from R', steep['crisps'] < steep['maize'],
            'pixel slopes %.2f vs %.2f' % (float(steep['crisps']), float(steep['maize'])))
    R.check('both curves share one panel (common axes and scales)', len(A.panels) == 1)
    check_text_has(R, 'answer image states both calculations', A.all_text(),
                   ['+50%', '\u221225% \u00f7 +50% = \u22120.5, inelastic', '\u221275% \u00f7 +50% = \u22121.5, elastic',
                    'PED \u22120.5', 'PED \u22121.5', 'same starting point'])

    if R.check('learning item exists', item is not None):
        check_text_has(R, 'prompt gives the facts the answer uses', item['prompt'],
                       ['100 packets', 'N$20', 'N$30', '75 packets', '25 packets', 'initial values'])
        check_text_has(R, 'canonical answer states the values', item['canonical_answer'],
                       ['(100, N$20)', '(75, N$30)', '(25, N$30)', '\u22120.5', '\u22121.5', 'inelastic', 'elastic', '50 per cent'])
        g = ' '.join(item['marking_guidance']).lower()
        check_text_has(R, 'guidance names the PROC parts', g, ['diagram', 'labels', 'original', 'change'])
        marks = sum(int(m) for m in re.findall(r'\((\d)\)', ' '.join(item['marking_guidance'])))
        R.check('guidance allocates the 4-mark tariff', marks == item['mark_tariff'] == 4, 'sum %d' % marks)


def card_pes(R, card, sides, item):
    """3.3-020: two supply curves through R (50 chairs, N$400); price rises to N$600."""
    P0, P1, Q0 = F(400), F(600), F(50)
    pct_p = (P1 - P0) / P0
    data = {'A': F(90), 'B': F(60)}
    pes = {k: ((q - Q0) / Q0) / pct_p for k, q in data.items()}
    R.check('price change is +50%', pct_p == F(1, 2))
    R.check('workshop A PES = 80% / 50% = 1.6, elastic', pes['A'] == F(8, 5) and pes['A'] > 1)
    R.check('workshop B PES = 20% / 50% = 0.4, inelastic', pes['B'] == F(2, 5) and pes['B'] < 1)

    def through(q0, p0, q1, p1):
        b = (q1 - q0) / (p1 - p0)
        return lambda p: q0 + b * (F(p) - p0)
    g_a, g_b = through(Q0, P0, data['A'], P1), through(Q0, P0, data['B'], P1)
    R.check('workshop A line is Q = 0.2P - 30', g_a(0) == -30 and g_a(100) == -10)
    R.check('workshop B line is Q = 0.05P + 30', g_b(0) == 30 and g_b(100) == 35)
    # For a straight line, (dQ/dP)(P/Q) at R equals the initial-value arc figure.
    R.check('point elasticity at R matches: A 0.2 x 400/50 = 1.6, B 0.05 x 400/50 = 0.4',
            F(1, 5) * P0 / Q0 == pes['A'] and F(1, 20) * P0 / Q0 == pes['B'])
    R.check('A meets the price axis (P = 150) and B the quantity axis (Q = 30), consistent with elastic and inelastic',
            g_a(150) == 0 and g_b(0) == 30)

    Q, A = sides['question'], sides['answer']
    cells = [t['text'] for t in Q.texts() if t['role'] == 'cell']
    R.check('question table shows the data exactly', cells == [
        'Workshop', 'Old price', 'New price', 'Old supply', 'New supply',
        'A (unused machines)', 'N$400', 'N$600', '50', '90', 'B (near capacity)', 'N$400', 'N$600', '50', '60'], str(cells))
    R.check('question side draws no curve or point', not Q.elements('curve') and not Q.elements('point'))
    check_no_leak(R, Q.all_text(), ['inelastic', 'elastic', '1.6', '0.4', 'S workshop A', 'S workshop B'])

    check_curve_x_of_y(R, A, 'pes', 'S-A', g_a, 'answer', through=[(50, 400), (90, 600)])
    check_curve_x_of_y(R, A, 'pes', 'S-B', g_b, 'answer', through=[(50, 400), (60, 600)])
    check_points(R, A, 'pes', {'R': (50, 400), 'A': (90, 600), 'B': (60, 600)}, 'answer')
    check_arrow(R, A, 'pes', 'R-to-A', (50, 400), (90, 600), 'answer')
    check_arrow(R, A, 'pes', 'R-to-B', (50, 400), (60, 600), 'answer')
    ux, uy = A.px_per_unit('pes')
    steep = {k: (200 * uy) / (float(q - Q0) * ux) for k, q in data.items()}
    R.check('elastic workshop A curve is drawn flatter than inelastic workshop B curve from R', steep['A'] < steep['B'],
            'pixel slopes %.2f vs %.2f' % (steep['A'], steep['B']))
    R.check('both curves share one panel (common axes and scales)', len(A.panels) == 1)
    check_text_has(R, 'answer image states both calculations', A.all_text(),
                   ['+50%', '+80% \u00f7 +50% = 1.6, elastic', '+20% \u00f7 +50% = 0.4, inelastic', 'PES 1.6', 'PES 0.4',
                    'same starting point'])

    if R.check('learning item exists', item is not None):
        check_text_has(R, 'prompt gives the facts the answer uses', item['prompt'],
                       ['50 chairs', 'N$400', 'N$600', '90 chairs', '60 chairs', 'unused machines', 'near capacity', 'initial values'])
        check_text_has(R, 'canonical answer states the values', item['canonical_answer'],
                       ['(50, N$400)', '(90, N$600)', '(60, N$600)', '1.6', '0.4', 'inelastic', 'elastic', '50 per cent'])
        g = ' '.join(item['marking_guidance']).lower()
        check_text_has(R, 'guidance names the PROC parts', g, ['diagram', 'labels', 'original', 'change'])
        marks = sum(int(m) for m in re.findall(r'\((\d)\)', ' '.join(item['marking_guidance'])))
        R.check('guidance allocates the 4-mark tariff', marks == item['mark_tariff'] == 4, 'sum %d' % marks)


def card_labour(R, card, sides, item):
    """4.2-025: S L = 10W - 100, D1 L = 400 - 10W; demand rises by 100 workers at every wage."""
    s = lambda w: 10 * F(w) - 100
    d1 = lambda w: 400 - 10 * F(w)
    d2 = lambda w: d1(w) + 100
    # Solve S = D for each demand curve.
    w1 = F(500, 20)
    w2 = F(600, 20)
    R.check('E1 solves S = D1 at N$25 and 150 workers', s(w1) == d1(w1) == 150 and w1 == 25)
    R.check('E2 solves S = D2 at N$30 and 200 workers', s(w2) == d2(w2) == 200 and w2 == 30)
    R.check('schedule in the prompt matches the curves',
            [d1(w) for w in (15, 20, 25, 30, 35)] == [250, 200, 150, 100, 50]
            and [s(w) for w in (15, 20, 25, 30, 35)] == [50, 100, 150, 200, 250])
    R.check('employment rises by less than the 100-worker shift (50), because the wage rises', d2(w2) - d1(w1) == 50)

    Q, A = sides['question'], sides['answer']
    R.check('question shows only the original curves D1 and S', sorted(e.get('data-id') for e in Q.elements('curve')) == ['D1', 'S'])
    R.check('question marks no equilibrium point', not Q.elements('point'))
    check_curve_x_of_y(R, Q, 'labour', 'D1', d1, 'question', through=[(150, 25)])
    check_curve_x_of_y(R, Q, 'labour', 'S', s, 'question', through=[(150, 25)])
    check_no_leak(R, Q.all_text(), ['E1', 'E2', 'D2', 'N$25', 'N$30', '150 housekeepers', '200 housekeepers', 'derived'])
    check_text_has(R, 'question states the cause and the size of the shift', Q.all_text(),
                   ['More tourists', '100 more housekeepers at every wage'])

    R.check('answer has D1, D2 and S only: supply is not shifted', sorted(e.get('data-id') for e in A.elements('curve')) == ['D1', 'D2', 'S'])
    check_curve_x_of_y(R, A, 'labour', 'D1', d1, 'answer', through=[(150, 25)])
    check_curve_x_of_y(R, A, 'labour', 'D2', d2, 'answer', through=[(200, 30)])
    check_curve_x_of_y(R, A, 'labour', 'S', s, 'answer', through=[(150, 25), (200, 30)])
    R.check('S is drawn identically on both sides', Q.by_id('curve', 'S').get('d') == A.by_id('curve', 'S').get('d'))
    R.check('D1 is drawn identically on both sides', Q.by_id('curve', 'D1').get('d') == A.by_id('curve', 'D1').get('d'))
    check_points(R, A, 'labour', {'E1': (150, 25), 'E2': (200, 30)}, 'answer')
    check_arrow(R, A, 'labour', 'shift-at-35', (50, 35), (150, 35), 'answer')
    check_arrow(R, A, 'labour', 'shift-at-15', (250, 15), (350, 15), 'answer')
    R.check('shift arrows join D1 to D2 at their wages', d1(35) == 50 and d2(35) == 150 and d1(15) == 250 and d2(15) == 350)
    check_text_has(R, 'answer image states both equilibria and the cause', A.all_text(),
                   ['N$25 an hour, 150 housekeepers', 'N$30 an hour, 200 housekeepers', '100 more housekeepers wanted at every wage',
                    'Only labour demand shifts', 'derived'])

    if R.check('learning item exists', item is not None):
        check_text_has(R, 'prompt gives the facts the answer uses', item['prompt'],
                       ['N$15, 20, 25, 30 and 35', '250, 200, 150, 100 and 50', '50, 100, 150, 200 and 250', '100 more'])
        check_text_has(R, 'canonical answer states the values', item['canonical_answer'],
                       ['N$25', '150', 'N$30', '200', 'derived', 'supply', '100'])
        g = ' '.join(item['marking_guidance']).lower()
        check_text_has(R, 'guidance names the PROC parts', g, ['diagram', 'labels', 'original', 'change'])
        marks = sum(int(m) for m in re.findall(r'\((\d)\)', ' '.join(item['marking_guidance'])))
        R.check('guidance allocates the 4-mark tariff', marks == item['mark_tariff'] == 4, 'sum %d' % marks)


def card_lrac(R, card, sides, item):
    """5.4-031: LRAC from total costs at six factory scales; AC = 4 + (Q - 40)^2 / 200."""
    q = [10, 20, 30, 40, 50, 60]
    tc = [85000, 120000, 135000, 160000, 225000, 360000]
    ac = [F(c, x * 1000) for c, x in zip(tc, q)]
    R.check('average cost = total cost / output gives 8.50, 6.00, 4.50, 4.00, 4.50, 6.00',
            ac == [F(17, 2), 6, F(9, 2), 4, F(9, 2), 6], str([str(a) for a in ac]))
    f = lambda x: 4 + (F(x) - 40) ** 2 / 200
    R.check('declared U-shaped equation passes through every computed average', all(f(x) == a for x, a in zip(q, ac)))
    R.check('average cost falls to 40 and rises after it (U shape, single minimum)',
            all(ac[i] > ac[i + 1] for i in range(3)) and all(ac[i] < ac[i + 1] for i in range(3, 5)) and min(ac) == ac[3] == 4)
    R.check('total cost rises at every step, even where average cost falls', all(tc[i] < tc[i + 1] for i in range(5)))
    R.check('20 to 40: total cost +N$40,000 while average cost falls N$2.00', tc[3] - tc[1] == 40000 and ac[1] - ac[3] == 2)

    Q, A = sides['question'], sides['answer']
    cells = [t['text'] for t in Q.texts() if t['role'] == 'cell']
    R.check('question table shows outputs and total costs exactly', cells == [
        "Output ('000 litres)", '10', '20', '30', '40', '50', '60',
        "Total cost (N$ '000)", '85', '120', '135', '160', '225', '360'], str(cells))
    R.check('question side draws no curve or point', not Q.elements('curve') and not Q.elements('point'))
    check_no_leak(R, Q.all_text(), ['economies', 'diseconom', 'optimum', '8.5', '4.00', '6.00', 'N$4'])
    check_text_has(R, 'question states that each output has its own factory (long run)', Q.all_text(), ['factory built for each output'])
    ytitle = [t['text'] for t in Q.texts() if t['role'] == 'y-title']
    R.check('vertical axis is average cost, not total cost', ytitle == ['Average cost (N$ per litre)'], str(ytitle))

    check_curve_fn(R, A, 'lrac', 'LRAC', f, 'answer', through=list(zip(q, ac)))
    check_points(R, A, 'lrac', {'P10': (10, F(17, 2)), 'P20': (20, 6), 'P30': (30, F(9, 2)), 'M': (40, 4),
                                'P50': (50, F(9, 2)), 'P60': (60, 6)}, 'answer')
    check_arrow(R, A, 'lrac', 'P20-to-M', (20, 6), (40, 4), 'answer')
    eco, dis = A.by_id('span', 'economies', 'lrac'), A.by_id('span', 'diseconomies', 'lrac')
    R.check('economies span ends and diseconomies span starts at the minimum (40)',
            eco is not None and dis is not None and float(eco.get('data-x2')) == 40 and float(dis.get('data-x1')) == 40
            and float(eco.get('data-x1')) < 40 < float(dis.get('data-x2')))
    check_text_has(R, 'answer image labels the regions and the optimum', A.all_text(),
                   ['Economies of scale', 'Diseconomies of scale', 'optimum scale = 40,000 litres at N$4.00',
                    'N$120,000', 'N$160,000', 'N$6.00 to N$4.00', 'LRAC'])
    R.check('answer never labels total cost as the plotted curve', 'total cost' not in ' '.join(
        t['text'].lower() for t in A.texts() if t['role'] in ('curve-label', 'y-title')))

    if R.check('learning item exists', item is not None):
        check_text_has(R, 'prompt gives the facts the answer uses', item['prompt'],
                       ['10, 20, 30, 40, 50 and 60 thousand litres', 'N$85,000', 'N$120,000', 'N$135,000', 'N$160,000',
                        'N$225,000', 'N$360,000', 'built for'])
        check_text_has(R, 'canonical answer states the values', item['canonical_answer'],
                       ['N$8.50', 'N$6.00', 'N$4.50', 'N$4.00', '40,000 litres', 'economies of scale', 'diseconomies of scale',
                        'optimum', 'N$120,000', 'N$160,000'])
        g = ' '.join(item['marking_guidance']).lower()
        check_text_has(R, 'guidance names the PROC parts', g, ['diagram', 'labels', 'original', 'change'])
        marks = sum(int(m) for m in re.findall(r'\((\d)\)', ' '.join(item['marking_guidance'])))
        R.check('guidance allocates the 4-mark tariff', marks == item['mark_tariff'] == 4, 'sum %d' % marks)


def check_control_market(R, Q, A, panel, d, s, level, kind, label):
    """Shared checks for a price or wage control: binding side, no shifted curves, quantities read off D and S."""
    R.check('question shows only the original curves D and S', sorted(e.get('data-id') for e in Q.elements('curve')) == ['D', 'S'])
    R.check('question draws no control line and marks no point', not Q.elements('hline') and not Q.elements('point'))
    R.check('answer still has only D and S: the control shifts neither curve',
            sorted(e.get('data-id') for e in A.elements('curve')) == ['D', 'S'])
    for c in ('D', 'S'):
        R.check('%s drawn identically on both sides' % c, Q.by_id('curve', c).get('d') == A.by_id('curve', c).get('d'))
    h = A.elements('hline', panel)
    R.check('answer draws one %s line at %s' % (kind, level), len(h) == 1 and float(h[0].get('data-y')) == float(level))
    if h:
        ux, uy = A.px_per_unit(panel)
        y_px = float(h[0].get('y1'))
        R.check('%s line is horizontal' % kind, abs(float(h[0].get('y2')) - y_px) < 0.01)


def card_maxprice(R, card, sides, item):
    """6.3-017: bread, D Q = 1200 - 50P, S Q = 50P - 200; maximum price N$12."""
    d = lambda p: 1200 - 50 * F(p)
    s = lambda p: 50 * F(p) - 200
    pe = F(1400, 100)
    R.check('equilibrium solves D = S at N$14 and 500 loaves', d(pe) == s(pe) == 500 and pe == 14)
    cap = F(12)
    R.check('maximum price N$12 is below equilibrium, so it binds', cap < pe)
    R.check('at N$12 quantity demanded 600 and supplied 400', d(cap) == 600 and s(cap) == 400)
    R.check('shortage 200; quantity bought limited to supply (400 < 500)', d(cap) - s(cap) == 200 and min(d(cap), s(cap)) == 400 < 500)
    R.check('schedule in the prompt matches the curves',
            [d(p) for p in (10, 12, 14, 16)] == [700, 600, 500, 400] and [s(p) for p in (10, 12, 14, 16)] == [300, 400, 500, 600])
    Q, A = sides['question'], sides['answer']
    check_control_market(R, Q, A, 'maxprice', d, s, 12, 'maximum-price', 'answer')
    check_curve_x_of_y(R, A, 'maxprice', 'D', d, 'answer', through=[(500, 14), (600, 12)])
    check_curve_x_of_y(R, A, 'maxprice', 'S', s, 'answer', through=[(500, 14), (400, 12)])
    check_points(R, A, 'maxprice', {'E': (500, 14), 'Qs': (400, 12), 'Qd': (600, 12)}, 'answer')
    sp = A.by_id('span', 'shortage', 'maxprice')
    R.check('shortage span runs from 400 to 600 at the maximum price', sp is not None and float(sp.get('data-x1')) == 400
            and float(sp.get('data-x2')) == 600 and float(sp.get('data-y')) == 12)
    check_no_leak(R, Q.all_text(), ['shortage', 'N$14', '500 loaves', 'supplied 400', 'demanded 600', 'E (original)'])
    check_text_has(R, 'question states the control', Q.all_text(), ['maximum price', 'N$12 a loaf'])
    check_text_has(R, 'answer image states the result', A.all_text(),
                   ['N$14 a loaf, 500 loaves', 'supplied 400, demanded 600', 'Shortage = 600 \u2212 400 = 200', 'Only 400 loaves',
                    'Neither curve shifts', 'Maximum price N$12'])
    if R.check('learning item exists', item is not None):
        check_text_has(R, 'prompt gives the facts the answer uses', item['prompt'],
                       ['N$10, N$12, N$14 and N$16', '300, 400, 500 and 600', '700, 600, 500 and 400', 'maximum price of N$12'])
        check_text_has(R, 'canonical answer states the values', item['canonical_answer'],
                       ['N$14', '500', 'N$12', '600', '400', '200', 'shortage', 'below', 'Neither curve shifts'])
        g = ' '.join(item['marking_guidance']).lower()
        check_text_has(R, 'guidance names the PROC parts', g, ['diagram', 'labels', 'original', 'change'])
        marks = sum(int(m) for m in re.findall(r'\((\d)\)', ' '.join(item['marking_guidance'])))
        R.check('guidance allocates the 4-mark tariff', marks == item['mark_tariff'] == 4, 'sum %d' % marks)


def card_minprice(R, card, sides, item):
    """6.3-018: mahangu, D Q = 700 - 2P, S Q = 2P - 100; minimum price N$250."""
    d = lambda p: 700 - 2 * F(p)
    s = lambda p: 2 * F(p) - 100
    pe = F(800, 4)
    R.check('equilibrium solves D = S at N$200 and 300 bags', d(pe) == s(pe) == 300 and pe == 200)
    floor = F(250)
    R.check('minimum price N$250 is above equilibrium, so it binds', floor > pe)
    R.check('at N$250 quantity demanded 200 and supplied 400', d(floor) == 200 and s(floor) == 400)
    R.check('surplus 200; quantity bought 200 is below quantity offered 400 and below the old 300',
            s(floor) - d(floor) == 200 and min(d(floor), s(floor)) == 200 < 300)
    R.check('schedule in the prompt matches the curves',
            [s(p) for p in (150, 200, 250, 300)] == [200, 300, 400, 500] and [d(p) for p in (150, 200, 250, 300)] == [400, 300, 200, 100])
    Q, A = sides['question'], sides['answer']
    check_control_market(R, Q, A, 'minprice', d, s, 250, 'minimum-price', 'answer')
    check_curve_x_of_y(R, A, 'minprice', 'D', d, 'answer', through=[(300, 200), (200, 250)])
    check_curve_x_of_y(R, A, 'minprice', 'S', s, 'answer', through=[(300, 200), (400, 250)])
    check_points(R, A, 'minprice', {'E': (300, 200), 'Qd': (200, 250), 'Qs': (400, 250)}, 'answer')
    sp = A.by_id('span', 'surplus', 'minprice')
    R.check('surplus span runs from 200 to 400 at the minimum price', sp is not None and float(sp.get('data-x1')) == 200
            and float(sp.get('data-x2')) == 400 and float(sp.get('data-y')) == 250)
    check_no_leak(R, Q.all_text(), ['surplus', 'N$200 a bag', '300 bags', 'supplied 400', 'demanded 200', 'E (original)'])
    check_text_has(R, 'question states the control', Q.all_text(), ['minimum price of N$250 a bag'])
    check_text_has(R, 'answer image states the result and separates offers from sales', A.all_text(),
                   ['N$200 a bag, 300 bags', 'demanded 200, supplied 400', 'Surplus = 400 \u2212 200 = 200', 'offer 400 but sell only 200',
                    'Neither curve shifts', 'Minimum price N$250'])
    if R.check('learning item exists', item is not None):
        check_text_has(R, 'prompt gives the facts the answer uses', item['prompt'],
                       ['N$150, N$200, N$250 and N$300', '200, 300, 400 and 500', '400, 300, 200 and 100', 'minimum price of N$250'])
        check_text_has(R, 'canonical answer states the values', item['canonical_answer'],
                       ['N$200', '300', 'N$250', '400', '200', 'surplus', 'above', 'Neither curve shifts', 'only 200 are bought'])
        g = ' '.join(item['marking_guidance']).lower()
        check_text_has(R, 'guidance names the PROC parts', g, ['diagram', 'labels', 'original', 'change'])
        marks = sum(int(m) for m in re.findall(r'\((\d)\)', ' '.join(item['marking_guidance'])))
        R.check('guidance allocates the 4-mark tariff', marks == item['mark_tariff'] == 4, 'sum %d' % marks)


def card_minwage(R, card, sides, item):
    """6.3-019: guards, D L = 900 - 20W, S L = 20W - 100; minimum wage N$30 in the competitive model."""
    d = lambda w: 900 - 20 * F(w)
    s = lambda w: 20 * F(w) - 100
    we = F(1000, 40)
    R.check('equilibrium solves D = S at N$25 and 400 guards', d(we) == s(we) == 400 and we == 25)
    floor = F(30)
    R.check('minimum wage N$30 is above equilibrium, so it binds', floor > we)
    R.check('at N$30 labour demanded 300 and supplied 500', d(floor) == 300 and s(floor) == 500)
    R.check('excess supply 200 = 100 fewer jobs + 100 more people seeking work',
            s(floor) - d(floor) == 200 and d(we) - d(floor) == 100 and s(floor) - s(we) == 100)
    R.check('a floor below N$25 would not bind (e.g. N$20: wage stays N$25)', F(20) < we)
    R.check('schedule in the prompt matches the curves',
            [d(w) for w in (20, 25, 30, 35)] == [500, 400, 300, 200] and [s(w) for w in (20, 25, 30, 35)] == [300, 400, 500, 600])
    Q, A = sides['question'], sides['answer']
    check_control_market(R, Q, A, 'minwage', d, s, 30, 'minimum-wage', 'answer')
    check_curve_x_of_y(R, A, 'minwage', 'D', d, 'answer', through=[(400, 25), (300, 30)])
    check_curve_x_of_y(R, A, 'minwage', 'S', s, 'answer', through=[(400, 25), (500, 30)])
    check_points(R, A, 'minwage', {'E': (400, 25), 'Ld': (300, 30), 'Ls': (500, 30)}, 'answer')
    sp = A.by_id('span', 'excess', 'minwage')
    R.check('excess-supply span runs from 300 to 500 at the minimum wage', sp is not None and float(sp.get('data-x1')) == 300
            and float(sp.get('data-x2')) == 500 and float(sp.get('data-y')) == 30)
    check_no_leak(R, Q.all_text(), ['excess', 'N$25 an hour', '400 guards', 'firms want 300', '500 want work', 'E (original)'])
    check_text_has(R, 'question names the competitive model and the control', Q.all_text(), ['Competitive labour market', 'minimum wage', 'N$30 an hour'])
    alltext = (Q.all_text() + ' ' + A.all_text()).lower()
    R.check('images avoid a blanket unemployment claim', 'unemployment' not in alltext)
    check_text_has(R, 'answer image states the result within the model', A.all_text(),
                   ['N$25 an hour, 400 guards', 'firms want 300, 500 want work', 'Excess supply of labour = 500 \u2212 300 = 200',
                    'In this competitive model', 'Neither curve shifts', 'Minimum wage N$30'])
    if R.check('learning item exists', item is not None):
        check_text_has(R, 'prompt gives the facts the answer uses', item['prompt'],
                       ['competitive', 'N$20, N$25, N$30 and N$35', '500, 400, 300 and 200', '300, 400, 500 and 600', 'minimum wage of N$30'])
        check_text_has(R, 'canonical answer states the values and the model condition', item['canonical_answer'],
                       ['N$25', '400', 'N$30', '300', '500', '200', 'above the equilibrium wage', 'competitive', 'Neither curve shifts'])
        R.check('answer avoids a blanket unemployment claim', 'unemployment' not in item['canonical_answer'].lower())
        g = ' '.join(item['marking_guidance']).lower()
        check_text_has(R, 'guidance names the PROC parts', g, ['diagram', 'labels', 'original', 'change'])
        marks = sum(int(m) for m in re.findall(r'\((\d)\)', ' '.join(item['marking_guidance'])))
        R.check('guidance allocates the 4-mark tariff', marks == item['mark_tariff'] == 4, 'sum %d' % marks)


def check_existing_item(R, item, spec_path):
    """Existing cards: the reviewed item text must be byte-for-byte what it was before the images were added."""
    import importlib.util
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(WS)), 'standard', 'v0.2.0-draft', 'checks'))
    from yyeni_checks import _artefact_text
    spec = json.load(open(spec_path))
    want = spec['preserved_item_authored_hash']
    now = hashlib.sha256(_artefact_text(item).encode()).hexdigest()
    R.check('existing item text unchanged (hash matches the reviewed stamp)', now == want == item.get('authored_hash'),
            'text %s, stamp %s, preserved %s' % (now[:12], (item.get('authored_hash') or '')[:12], want[:12]))


def pairs(text):
    return [(int(a), int(b)) for a, b in re.findall(r'\((\d+),\s*(\d+)\)', text)]


def card_ds002(R, card, sides, item):
    """3.2-002 (existing): D through (80,8),(60,12),(40,16); S through (40,8),(60,12),(80,16); price N$8 to N$16."""
    dpts, spts = [(80, 8), (60, 12), (40, 16)], [(40, 8), (60, 12), (80, 16)]
    d = lambda p: 120 - 5 * F(p)
    s = lambda p: 5 * F(p)
    R.check('D is the straight line Q = 120 - 5P through all three demand points', all(d(p) == q for q, p in dpts))
    R.check('S is the straight line Q = 5P through all three supply points', all(s(p) == q for q, p in spts))
    R.check('D slopes down and S slopes up', d(16) < d(8) and s(16) > s(8))
    Q, A = sides['question'], sides['answer']
    cells = [t['text'] for t in Q.texts() if t['role'] == 'cell']
    R.check('question table shows the card data exactly', cells == [
        'Price (N$ per unit)', '8', '12', '16', 'Demand (units)', '80', '60', '40', 'Supply (units)', '40', '60', '80'], str(cells))
    R.check('question side has no axes, curves or points (the learner draws and labels them)',
            not Q.panels and not Q.elements('curve') and not Q.elements('point'))
    check_no_leak(R, Q.all_text(), ['slopes', 'along D', 'along S', 'Quantity (units per week)'])
    check_curve_x_of_y(R, A, 'ds', 'D', d, 'answer', through=dpts)
    check_curve_x_of_y(R, A, 'ds', 'S', s, 'answer', through=spts)
    check_points(R, A, 'ds', {'D8': (80, 8), 'D16': (40, 16), 'S8': (40, 8), 'S16': (80, 16)}, 'answer')
    check_arrow(R, A, 'ds', 'along-D', (80, 8), (40, 16), 'answer')
    check_arrow(R, A, 'ds', 'along-S', (40, 8), (80, 16), 'answer')
    check_text_has(R, 'answer image states points and movements', A.all_text(),
                   ['(80, N$8), (60, N$12), (40, N$16)', '(40, N$8), (60, N$12), (80, N$16)',
                    'quantity demanded 80 to 40 along D', 'quantity supplied 40 to 80 along S'])
    if R.check('learning item exists', item is not None):
        check_existing_item(R, item, os.path.join(HERE, 'specs', card['slot_id'] + '.json'))
        R.check('canonical answer plots exactly the drawn points', pairs(item['canonical_answer']) == dpts + spts,
                str(pairs(item['canonical_answer'])))
        check_text_has(R, 'prompt carries the table data', item['prompt'], ['N$8, N$12, N$16', '80,60,40', '40,60,80', 'N$8 to N$16'])


def seed_market_base(R, sides, panel_curves):
    """Seed-packet market shared by 3.2-006/010/017: D0 Q = 120 - 3P and S0 Q = 3P from the cards' points."""
    d0 = lambda p: 120 - 3 * F(p)
    s0 = lambda p: 3 * F(p)
    R.check('D0 points (90,10),(60,20),(30,30) lie on Q = 120 - 3P', all(d0(p) == q for q, p in [(90, 10), (60, 20), (30, 30)]))
    R.check('S0 points (30,10),(60,20),(90,30) lie on Q = 3P', all(s0(p) == q for q, p in [(30, 10), (60, 20), (90, 30)]))
    R.check('E0 solves D0 = S0 at N$20 and 60 packets', d0(20) == s0(20) == 60)
    return d0, s0


def card_eq006(R, card, sides, item):
    """3.2-006 (existing): equilibrium at N$20, 60 packets; shortage of 60 at N$10; price adjusts up."""
    d, s = seed_market_base(R, sides, None)
    R.check('at N$10: supplied 30, demanded 90, excess demand 60', s(10) == 30 and d(10) == 90 and d(10) - s(10) == 60)
    Q, A = sides['question'], sides['answer']
    cells = [t['text'] for t in Q.texts() if t['role'] == 'cell']
    R.check('question table shows the card data exactly', cells == [
        'Price (N$ per packet)', '10', '20', '30', 'Demand (packets)', '90', '60', '30', 'Supply (packets)', '30', '60', '90'], str(cells))
    R.check('question side has no axes, curves or points', not Q.panels and not Q.elements('curve') and not Q.elements('point'))
    check_no_leak(R, Q.all_text(), ['E:', 'excess demand', 'N$20 a packet', 'shortage'])
    R.check('answer has D and S only (no shift)', sorted(e.get('data-id') for e in A.elements('curve')) == ['D', 'S'])
    check_curve_x_of_y(R, A, 'eq', 'D', d, 'answer', through=[(90, 10), (60, 20), (30, 30)])
    check_curve_x_of_y(R, A, 'eq', 'S', s, 'answer', through=[(30, 10), (60, 20), (90, 30)])
    check_points(R, A, 'eq', {'E': (60, 20), 'Qs': (30, 10), 'Qd': (90, 10)}, 'answer')
    check_arrow(R, A, 'eq', 'S-up-to-E', (30, 10), (60, 20), 'answer')
    check_arrow(R, A, 'eq', 'D-up-to-E', (90, 10), (60, 20), 'answer')
    sp = A.by_id('span', 'excess-demand', 'eq')
    R.check('excess-demand span runs 30 to 90 at N$10', sp is not None and float(sp.get('data-x1')) == 30
            and float(sp.get('data-x2')) == 90 and float(sp.get('data-y')) == 10)
    check_text_has(R, 'answer image states E, the shortage and the adjustment', A.all_text(),
                   ['N$20 a packet and 60 packets', 'supplied 30, demanded 90, excess demand 60', 'pushed up towards N$20',
                    'contracts along D', 'extends along S'])
    if R.check('learning item exists', item is not None):
        check_existing_item(R, item, os.path.join(HERE, 'specs', card['slot_id'] + '.json'))
        ans = item['canonical_answer']
        R.check('canonical answer matches the drawn values', all(k in ans for k in ['(60,20)', 'N$20', '60', 'Qs 30', 'Qd 90', 'excess demand 60', 'upward']))
        R.check('prompt points equal the drawn points', pairs(item['prompt']) == [(90, 10), (60, 20), (30, 30), (30, 10), (60, 20), (90, 30)],
                str(pairs(item['prompt'])))


def card_dshift010(R, card, sides, item):
    """3.2-010 (existing): demand rises by 30 at every price; E0 (60, N$20) to E1 (75, N$25)."""
    d0, s = seed_market_base(R, sides, None)
    d1 = lambda p: 150 - 3 * F(p)
    R.check('D1 points (120,10),(90,20),(60,30) lie on Q = 150 - 3P', all(d1(p) == q for q, p in [(120, 10), (90, 20), (60, 30)]))
    R.check('D1 is 30 to the right of D0 at every price', all(d1(p) - d0(p) == 30 for p in (10, 20, 30)))
    R.check('E1 solves D1 = S at N$25 and 75 packets', d1(25) == s(25) == 75)
    R.check('at the old N$20, excess demand is 30 (90 demanded, 60 supplied)', d1(20) - s(20) == 30)
    Q, A = sides['question'], sides['answer']
    cells = [t['text'] for t in Q.texts() if t['role'] == 'cell']
    R.check('question table shows the card data exactly', cells == [
        'Price (N$ per packet)', '10', '20', '30', 'Original demand D0', '90', '60', '30', 'New demand D1', '120', '90', '60',
        'Supply S (unchanged)', '30', '60', '90'], str(cells))
    R.check('question side has no axes, curves or points', not Q.panels and not Q.elements('curve') and not Q.elements('point'))
    check_no_leak(R, Q.all_text(), ['E0', 'E1', 'N$25', '75 packets', 'shifts right'])
    R.check('answer has D0, D1 and S only: supply is not shifted', sorted(e.get('data-id') for e in A.elements('curve')) == ['D0', 'D1', 'S'])
    check_curve_x_of_y(R, A, 'dshift', 'D0', d0, 'answer', through=[(90, 10), (60, 20), (30, 30)])
    check_curve_x_of_y(R, A, 'dshift', 'D1', d1, 'answer', through=[(120, 10), (90, 20), (60, 30)])
    check_curve_x_of_y(R, A, 'dshift', 'S', s, 'answer', through=[(30, 10), (60, 20), (90, 30), (75, 25)])
    check_points(R, A, 'dshift', {'E0': (60, 20), 'E1': (75, 25)}, 'answer')
    check_arrow(R, A, 'dshift', 'shift-at-30', (30, 30), (60, 30), 'answer')
    check_arrow(R, A, 'dshift', 'shift-at-10', (90, 10), (120, 10), 'answer')
    check_text_has(R, 'answer image states both equilibria and the shift', A.all_text(),
                   ['N$20, 60 packets', 'N$25, 75 packets', '30 more packets demanded at every price', 'supply does not move'])
    if R.check('learning item exists', item is not None):
        check_existing_item(R, item, os.path.join(HERE, 'specs', card['slot_id'] + '.json'))
        ans = item['canonical_answer']
        R.check('canonical answer matches the drawn values', all(k in ans for k in ['E0=(60,20)', 'E1=(75,25)', 'N$20 to N$25', '60 to 75', 'right of D0']))


def card_sshift017(R, card, sides, item):
    """3.2-017 (existing): supply rises by 30 at every price; E0 (60, N$20) to E1 (75, N$15)."""
    d, s0 = seed_market_base(R, sides, None)
    s1 = lambda p: 3 * F(p) + 30
    R.check('S1 points (60,10),(90,20),(120,30) lie on Q = 3P + 30', all(s1(p) == q for q, p in [(60, 10), (90, 20), (120, 30)]))
    R.check('S1 is 30 to the right of S0 at every price', all(s1(p) - s0(p) == 30 for p in (10, 20, 30)))
    R.check('E1 solves D = S1 at N$15 and 75 packets', d(15) == s1(15) == 75)
    R.check('at the old N$20, excess supply is 30 (90 supplied, 60 demanded)', s1(20) - d(20) == 30)
    Q, A = sides['question'], sides['answer']
    cells = [t['text'] for t in Q.texts() if t['role'] == 'cell']
    R.check('question table shows the card data exactly', cells == [
        'Price (N$ per packet)', '10', '20', '30', 'Demand D (unchanged)', '90', '60', '30', 'Original supply S0', '30', '60', '90',
        'New supply S1', '60', '90', '120'], str(cells))
    R.check('question side has no axes, curves or points', not Q.panels and not Q.elements('curve') and not Q.elements('point'))
    check_no_leak(R, Q.all_text(), ['E0', 'E1', 'N$15', '75 packets', 'shifts right'])
    R.check('answer has D, S0 and S1 only: demand is not shifted', sorted(e.get('data-id') for e in A.elements('curve')) == ['D', 'S0', 'S1'])
    check_curve_x_of_y(R, A, 'sshift', 'D', d, 'answer', through=[(90, 10), (60, 20), (30, 30), (75, 15)])
    check_curve_x_of_y(R, A, 'sshift', 'S0', s0, 'answer', through=[(30, 10), (60, 20), (90, 30)])
    check_curve_x_of_y(R, A, 'sshift', 'S1', s1, 'answer', through=[(60, 10), (90, 20), (120, 30)])
    check_points(R, A, 'sshift', {'E0': (60, 20), 'E1': (75, 15)}, 'answer')
    check_arrow(R, A, 'sshift', 'shift-at-10', (30, 10), (60, 10), 'answer')
    check_arrow(R, A, 'sshift', 'shift-at-30', (90, 30), (120, 30), 'answer')
    check_text_has(R, 'answer image states both equilibria and the shift', A.all_text(),
                   ['N$20, 60 packets', 'N$15, 75 packets', '30 more packets supplied at every price', 'demand does not move'])
    if R.check('learning item exists', item is not None):
        check_existing_item(R, item, os.path.join(HERE, 'specs', card['slot_id'] + '.json'))
        ans = item['canonical_answer']
        R.check('canonical answer matches the drawn values', all(k in ans for k in ['E0=(60,20)', 'E1=(75,15)', 'N$20 falling to N$15', '60 rising to 75', 'rightward']))


CARDS = {
    'ITEM-6145-1.1-011-PROC': card_ppc,
    'ITEM-6145-3.3-019-PROC': card_ped,
    'ITEM-6145-3.3-020-PROC': card_pes,
    'ITEM-6145-4.2-025-PROC': card_labour,
    'ITEM-6145-5.4-031-PROC': card_lrac,
    'ITEM-6145-6.3-017-PROC': card_maxprice,
    'ITEM-6145-6.3-018-PROC': card_minprice,
    'ITEM-6145-6.3-019-PROC': card_minwage,
    'ITEM-6145-3.2-002-PROC': card_ds002,
    'ITEM-6145-3.2-006-PROC': card_eq006,
    'ITEM-6145-3.2-010-PROC': card_dshift010,
    'ITEM-6145-3.2-017-PROC': card_sshift017,
}


def main(ids):
    cards = {c['slot_id']: c for c in json.load(open(WORK_ORDER))['cards']}
    os.makedirs(os.path.join(HERE, 'checks'), exist_ok=True)
    bad = 0
    for iid in ids or list(CARDS):
        card = cards[iid]
        sides = {s: Side(os.path.join(WS, card[s + '_svg'])) for s in ('question', 'answer')}
        R = Report(iid)
        generic_checks(R, card, sides)
        CARDS[iid](R, card, sides, load_item(card))
        previews = write_previews(card)
        files = {}
        for s in ('question', 'answer'):
            for kind in ('svg', 'png'):
                files[card[s + '_' + kind]] = sha(os.path.join(WS, card[s + '_' + kind]))
        rep = {'item_id': iid, 'files_sha256': files, 'previews': previews, 'checks': R.rows,
               'passed': len([r for r in R.rows if r['result'] == 'pass']), 'failed': len(R.failed)}
        json.dump(rep, open(os.path.join(HERE, 'checks', iid + '.json'), 'w'), indent=2)
        print('%s: %d passed, %d failed' % (iid, rep['passed'], rep['failed']))
        for r in R.failed:
            print('   FAIL %s  %s' % (r['check'], r['detail']))
        bad += len(R.failed)
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
