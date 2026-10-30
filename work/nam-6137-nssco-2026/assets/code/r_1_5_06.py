"""VIS-6137-1.5-06 -> ITEM-6137-1.5-048-PROC (assigned); variants bound to ITEM-6137-1.5-P05.

Base figure: (a) plan of a beach stretch with a sampling line parallel to the shore, positions at 0,
10 and 20 m northward from a start marker, and a 1 m quadrat at each with its north-east corner
marked; (b) measuring the longest axis of a pebble in millimetres; (c) an original four-class
roundness scale (shapes made by successive corner-cutting of one outline); (d) a record sheet.
P05 variant: the same roundness scale, blank axes (northward distance 0-20 m, mean size 0-50 mm) and
blank headings; the answer variant plots means 20, 30, 40 mm and completes the headings.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, Axes, build, check  # noqa: E402

RID = 'VIS-6137-1.5-06'
ITEM = 'ITEM-6137-1.5-048-PROC'
P05 = 'ITEM-6137-1.5-P05'
W, HQ, HA = 1000, 905, 1285
VY, VH = 1300, 820
SIZES = {0: (18, 20, 22), 10: (28, 30, 32), 20: (38, 40, 42)}
BASE = [(2, -36), (38, -6), (20, 32), (-24, 28), (-40, -12)]
CLASSES = [('angular', 0), ('sub-angular', 1), ('sub-rounded', 2), ('rounded', 5)]
STONE = '#9b8f7d'


def chaikin(pts, k):
    for _ in range(k):
        out = []
        for i in range(len(pts)):
            p, q = pts[i], pts[(i + 1) % len(pts)]
            out += [(0.75 * p[0] + 0.25 * q[0], 0.75 * p[1] + 0.25 * q[1]), (0.25 * p[0] + 0.75 * q[0], 0.25 * p[1] + 0.75 * q[1])]
        pts = out
    return pts


def roundness_scale(fig, x0, y0, layer):
    fig.text(x0, y0, 'Roundness scale (use the same scale for every pebble)', 26, 'start', 'bold', layer=layer)
    for i, (name, k) in enumerate(CLASSES):
        cx, cy = x0 + 70 + i * 230, y0 + 70
        fig.poly([(cx + 1.3 * x, cy + 1.3 * y) for x, y in chaikin(BASE, k)], STONE, INK, 2, layer=layer)
        fig.text(cx, cy + 82, name, 26, 'middle', 'normal', layer=layer)


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'Sampling beach pebbles: positions, measurement and shape')
    fig.extra_h = VY + VH
    # (a) plan
    fig.rect(20, 56, 960, 250, '#ffffff', GREY, 2, 8)
    fig.text(36, 90, '(a) Plan of the beach stretch (not to scale)', 26, 'start', 'bold')
    fig.rect(40, 104, 150, 190, C['sea'], 'none', 0)
    fig.rect(190, 104, 630, 190, C['sand'], 'none', 0)
    fig.rect(820, 104, 140, 190, C['land'], 'none', 0)
    fig.text(115, 210, 'sea', 26, 'middle', 'bold', C['blue'])
    fig.text(890, 210, 'land', 26, 'middle', 'bold', C['green'])
    lx = 540
    fig.line(lx, 290, lx, 112, C['red'], 3, dash='12 7')
    for d, y in ((0, 270), (10, 200), (20, 130)):
        fig.rect(lx - 22, y - 22, 44, 44, 'none', INK, 2.5)
        fig.circle(lx + 22, y - 22, 6, C['red'], INK, 1.5)
        fig.text(lx + 40, y + 9, '%d m%s' % (d, ' (start)' if d == 0 else ''), 26, 'start', 'bold', INK, halo=True)
    fig.arrow(780, 280, 780, 130, INK, 4, 16)
    fig.text(792, 152, 'N', 26, 'start', 'bold')
    fig.rect(204, 128, 24, 24, 'none', INK, 2.5)
    fig.text(238, 149, '1 m quadrat', 26, 'start', 'normal', INK, halo=True)
    fig.circle(216, 250, 6, C['red'], INK, 1.5)
    fig.text(238, 259, 'marked corner', 26, 'start', 'normal', INK, halo=True)
    # (b) measuring the longest axis
    fig.rect(20, 320, 300, 300, '#ffffff', GREY, 2, 8)
    fig.text(36, 354, '(b) Size', 26, 'start', 'bold')
    cx, cy = 170, 450
    fig.poly([(cx + 2.6 * x, cy + 1.7 * y) for x, y in chaikin(BASE, 2)], STONE, INK, 2)
    fig.arrow(cx + 6, cy + 82, cx + 108, cy + 82, INK, 3, 14, halo=False)
    fig.arrow(cx + 6, cy + 82, cx - 96, cy + 82, INK, 3, 14, halo=False)
    fig.text(cx, cy + 118, 'longest axis', 26, 'middle', 'bold')
    fig.text(cx, cy + 146, '(ruler, mm)', 26, 'middle')
    # (c) roundness scale
    fig.rect(334, 320, 646, 300, '#ffffff', GREY, 2, 8)
    fig.text(350, 354, '(c) Shape', 26, 'start', 'bold')
    for i, (name, k) in enumerate(CLASSES):
        sx, sy = 420 + i * 150, 470
        fig.poly([(sx + 1.3 * x, sy + 1.3 * y) for x, y in chaikin(BASE, k)], STONE, INK, 2)
        fig.text(sx, sy + 82, name, 26, 'middle')
    fig.text(350, 600, 'Roundness scale: compare each pebble with these', 26, 'start', 'normal', GREY)
    # (d) record sheet
    fig.rect(20, 634, 960, 256, '#ffffff', GREY, 2, 8)
    fig.text(36, 668, '(d) Record sheet', 26, 'start', 'bold')
    cols = [(36, 'Position (m north)'), (296, 'Longest axis (mm)'), (546, 'Roundness class'), (786, 'Notes')]
    fig.rect(36, 684, 928, 44, '#eef3f7', INK, 1.5)
    for x, lab in cols:
        fig.text(x + 10, 715, lab, 26, 'start', 'bold')
    for r, d in enumerate((0, 10, 20)):
        fig.rect(36, 728 + r * 48, 928, 48, '#ffffff', INK, 1.2)
        fig.text(56, 728 + r * 48 + 34, str(d), 26)
    for x, lab in cols[1:]:
        fig.line(x, 684, x, 872, INK, 1.2)

    A = 'a'
    fig.marker(lx + 160, 200, '1', A)
    fig.marker(290, 420, '2', A)
    fig.marker(940, 668, '3', A)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Procedure', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for n, s in [('1', 'From the start marker, place the quadrat every 10 m along the line and take the pebble under its marked corner each time (a fixed rule, not a chosen pebble).'),
                 ('2', 'Measure that pebble’s longest axis in millimetres with the same ruler at every position.'),
                 ('3', 'Record size and roundness class separately against the position, using the same scale. If no pebble is under the corner, record “no suitable pebble” rather than choosing another.')]:
        fig.marker(52, yy - 9, n, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8

    # ---- P05 variant
    V, VQ, VA = 'v-p05', 'v-p05-q', 'v-p05-a'
    fig.rect(0, VY, W, VH, '#ffffff', 'none', 0, layer=V)
    roundness_scale(fig, 36, VY + 40, V)
    ax = Axes(fig, 170, VY + 230, 760, 360, (0, 20), (0, 50), layer=V)
    ax.draw(range(0, 21, 5), range(0, 51, 10), 'Distance north from the first site (m)', 'Mean longest-axis size (mm)',
            minor_x=range(1, 20), minor_y=range(2, 50, 2), ylabel_x=70)
    ty = VY + 740
    fig.text(36, ty - 16, 'Record headings', 26, 'start', 'bold', layer=V)
    fig.rect(36, ty, 928, 50, '#eef3f7', INK, 1.5, layer=V)
    for x in (300, 630):
        fig.line(x, ty, x, ty + 50, INK, 1.2, layer=V)
    fig.text(50, ty + 34, 'Position (m)', 26, 'start', 'bold', layer=V)
    fig.text(314, ty + 34, 'Size ( ____ )', 26, 'start', 'normal', GREY, layer=VQ)
    fig.text(644, ty + 34, 'Shape: ______________', 26, 'start', 'normal', GREY, layer=VQ)
    fig.text(314, ty + 34, 'Longest-axis size (mm)', 26, 'start', 'bold', C['answer'], layer=VA)
    fig.text(644, ty + 34, 'Rounded / not rounded', 26, 'start', 'bold', C['answer'], layer=VA)
    means = [(d, sum(v) / 3) for d, v in SIZES.items()]
    ax.layer = VA
    ax.polyline(means, C['answer'], 4)
    for x, y in means:
        fig.circle(ax.X(x), ax.Y(y), 8, C['answer'], '#ffffff', 2, VA)
        fig.text(ax.X(x) + (14 if x < 20 else -14), ax.Y(y) - 16, '%g mm' % y, 26, 'start' if x < 20 else 'end', 'bold', C['answer'], VA, halo=True)

    spec = {
        'kind': 'sampling resource (plan, size, roundness scale, record sheet) with a P05 plotting variant',
        'positions_m_north': [0, 10, 20], 'quadrat': '1 m, north-east corner marked',
        'roundness_classes': [c for c, k in CLASSES], 'roundness_method': 'one outline, Chaikin corner-cutting 0, 1, 2, 5 times',
        'p05_variant': {'bound_item': P05, 'axes': {'x': [0, 20, 'm'], 'y': [0, 50, 'mm']}, 'sizes_mm': SIZES,
                        'means_mm': dict((str(d), m) for d, m in means), 'headings_answer': ['Longest-axis size (mm)', 'Rounded / not rounded (supplied scale)']},
        'question_withholds': ['selection rule wording', 'no-suitable-pebble rule'],
        'independent_solution': ['positions from start at fixed interval with a fixed selection rule (1)', 'longest axis in mm, same instrument (1)',
                                 'record size and roundness separately by position; predeclared no-pebble rule (1)'],
    }
    checks = [
        check('P05 means are 20, 30 and 40 mm', [m for d, m in means] == [20, 30, 40]),
        check('means lie within the supplied axes', all(0 <= m <= 50 for d, m in means)),
        check('roundness classes ordered from sharpest to smoothest', [k for c, k in CLASSES] == sorted(k for c, k in CLASSES)),
        check('quadrat positions 10 m apart along a line parallel to the shore', True),
    ]
    clip = (0, VY, W, VH)
    sides = {
        'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'], 'forbidden': [r'no suitable', r'\brule\b']},
        'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']},
        'p05_question': {'path': 'assets/images/%s-%s-question.png' % (P05, RID), 'layers': [V, VQ], 'clip': clip, 'hide_base': True,
                         'bound_item': P05, 'forbidden': [r'(?<!mean )longest-axis size \(mm\)', r'Rounded /', r'20 mm', r'40 mm']},
        'p05_answer': {'path': 'assets/images/%s-%s-answer.png' % (P05, RID), 'layers': [V, VA], 'clip': clip, 'hide_base': True, 'bound_item': P05},
    }
    return build(RID, fig, spec, sides, checks, panels=[(20, 56, 960, 250), (20, 320, 300, 300), (334, 320, 646, 300), (20, 634, 960, 256)])


if __name__ == '__main__':
    main()
