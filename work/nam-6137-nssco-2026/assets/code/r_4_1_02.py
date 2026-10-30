"""VIS-6137-4.1-02 -> ITEM-6137-4.1-034-INTERP (assigned): comparative presentation panels.

Base (notes BL-6137-4.1.07-07): dot plots of samples 10/20/30 and 18/20/22, both with mean 20; the
answer adds ranges 20 and 4.
The recorded reuses (036, 038, 042, 044) state different data in their prompts, so each gets its own
presentation-panel variant of this resource, with its own question/answer pair:
  036 choropleth + table: A 20, B 10 people/km2 under classes 0-<10, 10-<20, 20+ (BL-6137-4.1.07-08);
  038 scatter: visitors 20/40/60 against widths 100/140/120 cm (BL-6137-4.1.07-14);
  042 isoline segment: 10 at A, 20 at B, 15 crossing halfway under linear interpolation;
  044 enquiry flow chart with an evaluation loop back to the method (BL-6137-4.1.07-12, -21).
Package variants: P04 blank distance-size axes (0-100 m, 0-40 mm; answer A (0, 12), C (100, 32));
P05 blank percentage axes (answer residents 60%, visitors 80%); P06 signed tracer plan, record sheet
and axes -2..+5 m with A and B plotted (answer: 4 recovered, +8 m total; C -1, D +4).
Variant question sides are clipped shorter than their answer sides, which add an interpretation panel.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, Axes, table, build, check  # noqa: E402
from shapely.geometry import Polygon  # noqa: E402

RID = 'VIS-6137-4.1-02'
ITEM = 'ITEM-6137-4.1-034-INTERP'
W, HQ, HA = 1000, 590, 870
S1, S2 = [10, 20, 30], [18, 20, 22]
CLASSES = [('0 to under 10', 0, 10, '#f3ecd3'), ('10 to under 20', 10, 20, '#e6b35a'), ('20 or more', 20, 1e9, '#a6461e')]
DENS = {'A': 20, 'B': 10}
SCAT = [(20, 100), (40, 140), (60, 120)]
ISO = {'A': 10, 'B': 20, 'crossing': 15}
FLOW = ['Question and hypothesis', 'Method: frame, selection, measurement', 'Raw data record (kept unchanged)',
        'Analysis and presentation', 'Conclusion', 'Evaluation']
P04_PTS = {'A': (0, 12), 'C': (100, 32)}
P05_PCT = {'Residents': 12 / 20 * 100, 'Visitors': 16 / 20 * 100}
TRACERS = {'A': 3, 'B': 2, 'C': -1, 'D': 4, 'E': None}
BLUE = '#2f6fae'
# variant regions: (question height, answer height)
VREG = {'036': (660, 980), '038': (600, 920), '042': (730, 1100), '044': (680, 990),
        'p04': (590, 590), 'p05': (590, 590), 'p06': (770, 770)}
VY = {}
_y = HA + 70
for _k, (_q, _a) in VREG.items():
    VY[_k] = _y
    _y += _a + 70
H_ALL = _y


def answer_panel(fig, y0, y1, title, rows, layer):
    fig.rect(16, y0, W - 32, y1 - y0, '#f4faf6', C['answer'], 2, 8, layer)
    fig.text(36, y0 + 40, title, 28, 'start', 'bold', C['answer'], layer)
    yy = y0 + 84
    for n, s in rows:
        fig.marker(52, yy - 9, n, layer)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=layer) + 8
    return yy


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'Two samples with the same mean')
    fig.extra_h = H_ALL
    A = 'a'
    # ---- base: dot plots
    fig.text(W / 2, 80, 'Sample 1: 10, 20, 30;  Sample 2: 18, 20, 22', 26, 'middle')
    ax = Axes(fig, 200, 120, 720, 300, (0, 40), (0, 2))
    ax.draw(range(0, 41, 5), [], 'Reading (same unit in both samples)', None, grid=True)
    for row, vals, lab in ((1.5, S1, 'Sample 1'), (0.5, S2, 'Sample 2')):
        y = ax.Y(row)
        fig.text(ax.x0 - 16, y + 9, lab, 26, 'end', 'bold')
        for v in vals:
            fig.circle(ax.X(v), y, 14, BLUE, INK, 2)
        m = sum(vals) / len(vals)
        fig.line(ax.X(m), y - 34, ax.X(m), y + 34, '#c0392b', 4)
        fig.text(ax.X(m) + 10, y + 58, 'mean %g' % m, 26, 'start', 'bold', '#c0392b', halo=True)
    fig.circle(230, 545, 14, BLUE, INK, 2)
    fig.text(256, 554, 'one reading', 26)
    fig.line(470, 525, 470, 565, '#c0392b', 4)
    fig.text(490, 554, 'sample mean', 26)
    for row, vals in ((1.5, S1), (0.5, S2)):
        y = ax.Y(row) - 40
        lo, hi = min(vals), max(vals)
        fig.line(ax.X(lo), y, ax.X(hi), y, C['answer'], 4, A)
        for v in (lo, hi):
            fig.line(ax.X(v), y - 10, ax.X(v), y + 10, C['answer'], 4, A)
        fig.text(ax.X(hi) + 14, y + 9, 'range %d − %d = %d' % (hi, lo, hi - lo), 26, 'start', 'bold', C['answer'], A, halo=True)
    answer_panel(fig, HQ + 6, HA - 10, 'Interpretation', [
        ('1', 'Both samples have a mean of 20, but Sample 1 runs from 10 to 30 (range 20) while Sample 2 runs from 18 to 22 (range 4).'),
        ('2', 'Plotting the individual values shows the wider spread in Sample 1 that the mean alone hides.'),
        ('3', 'Equal means do not mean identical observations.')], A)

    sides = {'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'], 'forbidden': [r'range']},
             'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']}}

    def variant(key, bound, forbidden=()):
        V, VQ, VA = 'v-' + key, 'v-%s-q' % key, 'v-%s-a' % key
        y0 = VY[key]
        hq, ha = VREG[key]
        fig.rect(0, y0, W, ha, '#ffffff', 'none', 0, layer=V)
        sides[key + '_question'] = {'path': 'assets/images/%s-%s-question.png' % (bound, RID), 'layers': [V, VQ],
                                    'clip': (0, y0, W, hq), 'hide_base': True, 'bound_item': bound, 'forbidden': list(forbidden)}
        sides[key + '_answer'] = {'path': 'assets/images/%s-%s-answer.png' % (bound, RID), 'layers': [V, VA],
                                  'clip': (0, y0, W, ha), 'hide_base': True, 'bound_item': bound,
                                  'panels': [(16, y0 + hq + 6, W - 32, ha - hq - 16)] if ha > hq else []}
        return V, VQ, VA, y0, hq, ha

    # ---- 036 choropleth and table
    V, VQ, VA, y0, hq, ha = variant('036', 'ITEM-6137-4.1-036-INTERP', [r'highest', r'middle class'])
    fig.text(W / 2, y0 + 40, 'Population density of regions A and B', 28, 'middle', 'bold', layer=V)
    col = {k: next(c[3] for c in CLASSES if c[1] <= d < c[2]) for k, d in DENS.items()}
    pa = [(70, y0 + 90), (390, y0 + 80), (430, y0 + 250), (380, y0 + 420), (80, y0 + 400)]
    pb = [(390, y0 + 80), (600, y0 + 100), (620, y0 + 300), (580, y0 + 430), (380, y0 + 420), (430, y0 + 250)]
    fig.poly(pa, col['A'], INK, 2.5, layer=V)
    fig.poly(pb, col['B'], INK, 2.5, layer=V)
    fig.text(230, y0 + 262, 'A', 40, 'middle', 'bold', INK, V, halo=True)
    fig.text(520, y0 + 262, 'B', 40, 'middle', 'bold', INK, V, halo=True)
    fig.text(690, y0 + 110, 'Key: people per km²', 26, 'start', 'bold', layer=V)
    for i, (lab, lo, hi, c) in enumerate(CLASSES):
        fig.rect(690, y0 + 135 + i * 54, 44, 34, c, INK, 1.5, layer=V)
        fig.text(746, y0 + 161 + i * 54, lab, 26, layer=V)
    table(fig, 70, y0 + 470, [160, 400], 52, [['Region', 'Density (people per km²)'], ['A', '20'], ['B', '10']], layer=V, align=['middle'] * 2)
    fig.marker(660, y0 + 255, '1', VA)
    fig.marker(660, y0 + 201, '2', VA)
    fig.marker(230, y0 + 330, '3', VA)
    answer_panel(fig, y0 + hq + 6, y0 + ha - 10, 'Interpretation', [
        ('1', 'A (20 per km²) is in the highest class: 20 is the lower limit of “20 or more”, so it cannot be in “10 to under 20”.'),
        ('2', 'B (10 per km²) is in the middle class, “10 to under 20”: the boundary value goes up, so each value has one class.'),
        ('3', 'Each shade is an average for the whole region; it does not show whether people are spread evenly inside A or B.')], VA)

    # ---- 038 scatter
    V, VQ, VA, y0, hq, ha = variant('038', 'ITEM-6137-4.1-038-INTERP', [r'rises', r'falls'])
    fig.text(W / 2, y0 + 40, 'Visitor counts and path widths at three sites', 28, 'middle', 'bold', layer=V)
    sx = Axes(fig, 200, y0 + 80, 680, 400, (0, 70), (0, 160), layer=V)
    sx.draw(range(0, 71, 10), range(0, 161, 20), 'Visitors counted', 'Path width (cm)', ylabel_x=90, minor_y=range(10, 160, 20))
    for i, (v, w) in enumerate(SCAT, 1):
        fig.circle(sx.X(v), sx.Y(w), 11, BLUE, INK, 2, V)
        fig.text(sx.X(v), sx.Y(w) + (48 if i == 1 else -22), 'Site %d (%d, %d)' % (i, v, w), 26, 'middle', 'bold', INK, V, halo=True)
    for ((v1, w1), (v2, w2)), (dx, dy) in zip(zip(SCAT, SCAT[1:]), ((60, 40), (0, 56))):
        fig.arrow(sx.X(v1) + 14, sx.Y(w1) + 6, sx.X(v2) - 14, sx.Y(w2) + 6, C['answer'], 4, 16, VA)
        fig.text((sx.X(v1) + sx.X(v2)) / 2 + dx, (sx.Y(w1) + sx.Y(w2)) / 2 + dy, ('%+d cm' % (w2 - w1)).replace('-', '−'), 26, 'middle', 'bold', C['answer'], VA, halo=True)
    fig.marker(sx.X(26), sx.Y(135), '1', VA)
    fig.marker(sx.X(66), sx.Y(100), '2', VA)
    answer_panel(fig, y0 + hq + 6, y0 + ha - 10, 'Interpretation', [
        ('1', 'Width rises from 100 to 140 cm, then falls to 120 cm, so it does not increase at every step.'),
        ('2', 'Site 3 has the most visitors (60) yet is narrower than Site 2, which had 40.'),
        ('3', 'Three paired points cannot isolate current visitors as the only cause of width; slope, construction and earlier use may also matter.')], VA)

    # ---- 042 isoline segment
    V, VQ, VA, y0, hq, ha = variant('042', 'ITEM-6137-4.1-042-INTERP', [r'estimate', r'possible'])
    fig.text(W / 2, y0 + 40, 'Interpolating the value 15 between stations A and B', 28, 'middle', 'bold', layer=V)
    fig.rect(60, y0 + 70, 880, 230, '#f3f6fa', GREY, 1.5, 6, V)
    xa, xb, yl = 200, 800, y0 + 200
    fig.line(xa, yl, xb, yl, GREY, 3, V, dash='10 8')
    for x, val, dash in ((xa, 10, None), ((xa + xb) / 2, 15, '12 8'), (xb, 20, None)):
        fig.line(x, y0 + 100, x, y0 + 280, '#8e5ea2', 4, V, dash=dash)
        fig.text(x + 10, y0 + 124, str(val), 28, 'start', 'bold', '#8e5ea2', V, halo=True)
    for x, lab, anc, dx in ((xa, 'A = 10', 'end', -16), (xb, 'B = 20', 'start', 16)):
        fig.circle(x, yl, 12, INK, '#ffffff', 2, V)
        fig.text(x + dx, yl + 46, lab, 26, anc, 'bold', INK, V, halo=True)
    fig.text((xa + xb) / 2 + 14, yl + 46, 'halfway', 26, 'start', 'normal', INK, V, halo=True)
    fig.line(70, y0 + 334, 130, y0 + 334, '#8e5ea2', 4, V)
    fig.text(140, y0 + 343, 'isoline through a station', 26, layer=V)
    fig.line(510, y0 + 334, 570, y0 + 334, '#8e5ea2', 4, V, dash='12 8')
    fig.text(580, y0 + 343, 'interpolated isoline (15)', 26, layer=V)
    fig.text(70, y0 + 394, 'Section along A–B (linear interpolation):', 26, 'start', 'bold', layer=V)
    ix = Axes(fig, 200, y0 + 420, 600, 230, (0, 1), (5, 25), layer=V)
    ix.draw([], range(5, 26, 5), None, 'Value', ylabel_x=110)
    for t, lab in ((0, 'A'), (0.5, 'halfway'), (1, 'B')):
        fig.line(ix.X(t), ix.Y(5), ix.X(t), ix.Y(5) + 8, INK, 2, V)
        fig.text(ix.X(t), ix.Y(5) + 36, lab, 26, 'middle', 'bold', layer=V)
    ix.polyline([(0, 10), (1, 20)], BLUE, 4)
    fig.circle(ix.X(0.5), ix.Y(15), 10, '#ffffff', BLUE, 3, V)
    fig.line(ix.X(0), ix.Y(15), ix.X(1), ix.Y(15), '#8e5ea2', 2, V, dash='8 6')
    curve = [(t / 20, 10 + 10 * (t / 20) ** 2) for t in range(21)]
    ix.polyline(curve, '#7f7f7f', 3, VA, dash='9 7')
    fig.text(ix.X(0.62), ix.Y(9.2), 'another possible profile', 26, 'start', 'bold', '#5f5f5f', VA, halo=True)
    fig.marker(ix.X(0.5) - 30, ix.Y(17.5), '2', VA)
    fig.marker(ix.X(0.84), ix.Y(14), '3', VA)
    answer_panel(fig, y0 + hq + 6, y0 + ha - 10, 'Interpretation', [
        ('1', 'Values are estimated to rise from 10 at A to 20 at B, so 15 is an intermediate value.'),
        ('2', 'The 15 isoline is halfway only because change is assumed to be linear (the straight section line).'),
        ('3', 'It is an estimate, not an extra observation. If values change unevenly (dashed curve), the real crossing could lie elsewhere, and nothing is known beyond the segment.')], VA)

    # ---- 044 flow chart
    V, VQ, VA, y0, hq, ha = variant('044', 'ITEM-6137-4.1-044-INTERP', [r'rewrit'])
    fig.text(W / 2, y0 + 40, 'Enquiry flow chart', 28, 'middle', 'bold', layer=V)
    bx0, bw, bh, gap = 160, 540, 62, 34
    ys = [y0 + 72 + i * (bh + gap) for i in range(len(FLOW))]
    for i, (lab, by) in enumerate(zip(FLOW, ys)):
        fig.rect(bx0, by, bw, bh, '#eef3f7' if i != 2 else '#fff6d6', INK, 2, 8, V)
        fig.text(bx0 + bw / 2, by + 40, lab, 26, 'middle', 'bold', layer=V)
        if i:
            fig.arrow(bx0 + bw / 2, ys[i - 1] + bh + 2, bx0 + bw / 2, by - 2, INK, 3, 14, V, halo=False)
    rx = 820
    fig.line(bx0 + bw, ys[5] + bh / 2, rx, ys[5] + bh / 2, INK, 3, V)
    fig.line(rx, ys[5] + bh / 2, rx, ys[1] + bh / 2, INK, 3, V)
    fig.arrow(rx, ys[1] + bh / 2, bx0 + bw + 2, ys[1] + bh / 2, INK, 3, 14, V, halo=False)
    fig.lines(rx + 14, ys[2] + 20, ['revise the', 'method for', 'the next', 'collection'], 26, 32, layer=V)
    lx = 100
    fig.line(bx0, ys[5] + bh / 2, lx, ys[5] + bh / 2, '#c0392b', 3, VA, dash='10 7')
    fig.line(lx, ys[5] + bh / 2, lx, ys[0] + bh / 2, '#c0392b', 3, VA, dash='10 7')
    fig.arrow(lx, ys[0] + bh / 2, bx0 - 2, ys[0] + bh / 2, '#c0392b', 3, 14, VA, dash='10 7')
    cx, cy = lx, (ys[0] + ys[5]) / 2 + bh / 2
    fig.circle(cx, cy, 24, '#ffffff', '#c0392b', 3, VA)
    fig.line(cx - 12, cy - 12, cx + 12, cy + 12, '#c0392b', 4, VA)
    fig.line(cx - 12, cy + 12, cx + 12, cy - 12, '#c0392b', 4, VA)
    fig.text(52, (ys[0] + ys[5]) / 2 + bh / 2, 'not: rewrite the hypothesis', 26, 'middle', 'bold', '#c0392b', VA, halo=True, rotate=-90)
    fig.marker(bx0 + bw - 24, ys[0] + 4, '1', VA)
    fig.marker(rx, ys[3] + 70, '2', VA)
    fig.marker(lx, ys[1] + 30, '3', VA)
    answer_panel(fig, y0 + hq + 6, y0 + ha - 10, 'Interpretation', [
        ('1', 'The chart is a sequence from question to evaluation, with one revision loop.'),
        ('2', 'Evaluation feeds back to the method for a later collection; the original raw record stays as it was.'),
        ('3', 'The loop does not justify rewriting the first hypothesis after seeing the results (red dashed route).')], VA)

    # ---- P04 axes: distance-size
    V, VQ, VA, y0, hq, ha = variant('p04', 'ITEM-6137-4.1-P04')
    fig.text(W / 2, y0 + 40, 'Mean pebble length along the beach', 28, 'middle', 'bold', layer=V)
    a4 = Axes(fig, 200, y0 + 80, 680, 360, (0, 100), (0, 40), layer=V)
    a4.draw(range(0, 101, 10), range(0, 41, 5), 'Distance along the beach (m)', 'Mean pebble length (mm)', ylabel_x=90)
    for k, (d, m) in P04_PTS.items():
        fig.circle(a4.X(d), a4.Y(m), 10, C['answer'], '#ffffff', 2, VA)
        fig.text(a4.X(d) + (18 if d < 50 else -18), a4.Y(m) - 18, '%s (%d, %d)' % (k, d, m), 26, 'start' if d < 50 else 'end', 'bold', C['answer'], VA, halo=True)

    # ---- P05 axes: percentage bars
    V, VQ, VA, y0, hq, ha = variant('p05', 'ITEM-6137-4.1-P05')
    fig.text(W / 2, y0 + 40, 'Positive responses by group', 28, 'middle', 'bold', layer=V)
    a5 = Axes(fig, 230, y0 + 80, 560, 380, (0, 2), (0, 100), layer=V)
    a5.draw([], range(0, 101, 10), None, 'Positive responses (%)', ylabel_x=110)
    for i, (g, pct) in enumerate(P05_PCT.items()):
        fig.text(a5.X(i + 0.5), a5.Y(0) + 36, g, 26, 'middle', 'bold', layer=V)
        x0, x1 = a5.X(i + 0.25), a5.X(i + 0.75)
        fig.rect(x0, a5.Y(pct), x1 - x0, a5.Y(0) - a5.Y(pct), '#7fb89a', C['answer'], 2.5, layer=VA)
        fig.text((x0 + x1) / 2, a5.Y(pct) - 12, '%d%%' % pct, 26, 'middle', 'bold', C['answer'], VA, halo=True)
    fig.text(a5.X(1), a5.Y(0) + 76, 'Group (20 respondents each)', 26, 'middle', 'bold', layer=V)

    # ---- P06 signed tracer plan, sheet and axes
    V, VQ, VA, y0, hq, ha = variant('p06', 'ITEM-6137-4.1-P06', [r'\+8'])
    fig.text(W / 2, y0 + 40, 'Tracer trial: signed plan, record sheet and axes', 28, 'middle', 'bold', layer=V)
    fig.rect(40, y0 + 64, 920, 140, '#f6e7c1', GREY, 1.5, layer=V)
    fig.rect(40, y0 + 204, 920, 46, '#9cc3e0', GREY, 1.5, layer=V)
    fig.text(500, y0 + 236, 'Sea: observe from the shore only', 26, 'middle', 'bold', INK, V, halo=True)
    PXM, X0 = 100, 360
    ly = y0 + 150
    fig.line(X0 - 2 * PXM, ly, X0 + 5 * PXM, ly, INK, 3, V)
    for m in range(-2, 6):
        fig.line(X0 + m * PXM, ly - 8, X0 + m * PXM, ly + 8, INK, 2, V)
        fig.text(X0 + m * PXM, ly + 40, ('%+d' % m if m else '0 release').replace('-', '−') + (' m' if m == 5 else ''), 26, 'middle', 'bold' if m == 0 else 'normal', INK, V)
    fig.line(X0, ly - 40, X0, ly + 8, INK, 3, V, dash='6 5')
    for k, d in TRACERS.items():
        if d is None:
            continue
        x = X0 + d * PXM
        fig.poly([(x, ly - 4), (x - 13, ly - 28), (x + 13, ly - 28)], '#c0392b', INK, 1.5, layer=V)
        fig.text(x, ly - 36, k, 26, 'middle', 'bold', INK, V, halo=True)
    fig.arrow(870, y0 + 96, 940, y0 + 96, INK, 4, 16, V)
    fig.text(905, y0 + 136, 'N (+)', 26, 'middle', 'bold', INK, V, halo=True)
    rows = [['Tracer', 'Displacement (m)']] + [[k, ('%+d' % d).replace('-', '−') if d is not None else 'missing (not recovered)'] for k, d in TRACERS.items()]
    rec = [d for d in TRACERS.values() if d is not None]
    rows += [['Recovered', str(len(rec))], ['Signed total', '%+d m' % sum(rec)]]
    ty = table(fig, 40, y0 + 280, [160, 330], 50, rows, layer=V, cell_layers={(6, 1): VA, (7, 1): VA}, align=['middle', 'middle'])
    fig.text(40, ty + 36, 'North = +, south = −. Missing is not zero.', 26, layer=V)
    a6 = Axes(fig, 640, y0 + 300, 300, 360, (0, 4), (-2, 5), layer=V)
    a6.draw([], range(-2, 6), None, 'Displacement (m)', fmt_y=lambda v: ('%+d' % v if v else '0').replace('-', '−'), ylabel_x=565)
    fig.line(a6.X(0), a6.Y(0), a6.X(4), a6.Y(0), INK, 3, V)
    for i, k in enumerate('ABCD'):
        d = TRACERS[k]
        x0, x1 = a6.X(i + 0.2), a6.X(i + 0.8)
        lay = V if k in 'AB' else VA
        fig.rect(x0, min(a6.Y(d), a6.Y(0)), x1 - x0, abs(a6.Y(d) - a6.Y(0)), '#7fa7cf' if lay == V else '#7fb89a', INK if lay == V else C['answer'], 2, layer=lay)
        fig.text(a6.X(i + 0.5), a6.Y(-2) + 36, k, 26, 'middle', 'bold', layer=V)
    fig.text(a6.X(2), a6.Y(-2) + 72, 'Tracer', 26, 'middle', 'bold', layer=V)

    mean1, mean2 = sum(S1) / 3, sum(S2) / 3
    spec = {
        'kind': 'comparative presentation panels with reuse and package variants',
        'base_034': {'sample_1': S1, 'sample_2': S2, 'means': [mean1, mean2], 'ranges': [max(S1) - min(S1), max(S2) - min(S2)],
                     'notes_match': 'BL-6137-4.1.07-07'},
        'v036': {'bound_item': 'ITEM-6137-4.1-036-INTERP', 'densities': DENS, 'classes': [c[:3] if c[2] < 1e8 else (c[0], c[1], None) for c in CLASSES],
                 'answer': {'A': '20 or more', 'B': '10 to under 20'}},
        'v038': {'bound_item': 'ITEM-6137-4.1-038-INTERP', 'pairs_visitors_width_cm': SCAT, 'steps_cm': [40, -20]},
        'v042': {'bound_item': 'ITEM-6137-4.1-042-INTERP', 'values': ISO, 'crossing_fraction_linear': (15 - 10) / (20 - 10),
                 'alternative_profile': 'v = 10 + 10 t^2 (illustrative non-linear case; crosses 15 at t = 0.71)'},
        'v044': {'bound_item': 'ITEM-6137-4.1-044-INTERP', 'boxes': FLOW, 'loop': 'Evaluation -> Method', 'forbidden_route_answer': 'Evaluation -> Hypothesis (crossed)'},
        'p04': {'bound_item': 'ITEM-6137-4.1-P04', 'axes': {'x_m': [0, 100], 'y_mm': [0, 40]}, 'answer_points': P04_PTS},
        'p05': {'bound_item': 'ITEM-6137-4.1-P05', 'axes': {'y_percent': [0, 100]}, 'answer_bars': P05_PCT},
        'p06': {'bound_item': 'ITEM-6137-4.1-P06', 'tracers_m_north_positive': TRACERS, 'recovered': len(rec), 'signed_total_m': sum(rec),
                'mean_recovered_m': sum(rec) / len(rec), 'axes_y_m': [-2, 5], 'question_plots': ['A', 'B'], 'answer_plots': {'C': -1, 'D': 4}},
        'question_withholds': ['ranges (034)', 'class judgements (036)', 'step changes (038)', 'alternative profile (042)',
                               'crossed hypothesis route (044)', 'plotted answers (P04-P06)'],
        'independent_solution_034': ['equal means 20; ranges 20 vs 4 (1)', 'dispersion shown by individual values (1)', 'equal means ≠ identical data (1)'],
    }
    crossing_t = (ISO['crossing'] - ISO['A']) / (ISO['B'] - ISO['A'])
    checks = [
        check('034 means both 20; ranges 20 and 4', mean1 == mean2 == 20 and spec['base_034']['ranges'] == [20, 4]),
        check('036 A in 20+, B in 10-<20 (boundary goes up)', col['A'] == CLASSES[2][3] and col['B'] == CLASSES[1][3]),
        check('036 regions share a border and do not overlap', Polygon(pa).intersection(Polygon(pb)).area < 1 and Polygon(pa).boundary.intersection(Polygon(pb).boundary).length > 100),
        check('038 steps +40 then -20 cm', [b[1] - a[1] for a, b in zip(SCAT, SCAT[1:])] == [40, -20]),
        check('042 linear crossing at halfway (t = 0.5)', crossing_t == 0.5),
        check('042 alternative profile passes through A and B values', curve[0][1] == 10 and curve[-1][1] == 20),
        check('044 loop returns to the method box, not to the hypothesis', FLOW[1].startswith('Method')),
        check('P04 answer points equal the sheet means for A and C', P04_PTS == {'A': (0, 12), 'C': (100, 32)}),
        check('P05 bars 60% and 80%', P05_PCT == {'Residents': 60, 'Visitors': 80}),
        check('P06 4 recovered, total +8 m, mean +2 m', len(rec) == 4 and sum(rec) == 8 and sum(rec) / 4 == 2),
        check('P06 all recovered values within axes -2..+5', all(-2 <= d <= 5 for d in rec)),
    ]
    return build(RID, fig, spec, sides, checks)


if __name__ == '__main__':
    main()
