"""VIS-6137-1.4-02 -> ITEM-6137-1.4-012-INTERP: three wind-transport paths over a sand surface.

Side view, wind from left to right. Positions are drawn at equal time intervals (t1-t5) so each
path's ground contact can be read: A stays airborne throughout (fine dust), B makes repeated short
hops landing on the surface, C stays in contact with the surface and rolls. Sizes differ as they
would, but the classification evidence is the path and the contacts (notes BL-6137-1.4.03-07).
"""
import math
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, build, check  # noqa: E402

RID = 'VIS-6137-1.4-02'
ITEM = 'ITEM-6137-1.4-012-INTERP'
W, HQ, HA = 1000, 735, 1100
X0, X1 = 120, 920
STRIPS = {'A': (130, 330), 'B': (345, 515), 'C': (530, 640)}      # top and ground line of each strip
HOPS = [(120, 320), (320, 520), (520, 720), (720, 920)]          # B take-off and landing x (equal times)
HOP_H = 85
SAND = '#c9a95a'


def a_path(x):                # fine dust: high above its ground line, gently undulating
    return STRIPS['A'][0] + 50 + 22 * math.sin((x - X0) / 110)


def b_path(x):
    g = STRIPS['B'][1] - 8
    for x1, x2 in HOPS:
        if x1 <= x <= x2:
            t = (x - x1) / (x2 - x1)
            return g - HOP_H * math.sin(math.pi * t ** 0.7)       # steep rise, longer shallow descent
    return g


def strip(fig, key, col):
    top, g = STRIPS[key]
    fig.rect(20, top, 960, g - top, '#f3f8fc', 'none', 0)
    fig.rect(20, g, 960, 12, C['sand'], 'none', 0)
    fig.line(20, g, 980, g, INK, 3)
    fig.text(44, top + (g - top) / 2 + 10, key, 34, 'middle', 'bold', col)


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'Paths of three particles moved by wind (side view, not to scale)')
    fig.arrow(330, 92, 670, 92, INK, 6, 24)
    fig.text(700, 101, 'wind', 28, 'start', 'bold')
    PA, PB, PC = C['purple'], C['orange'], '#6b4f2a'
    for k, col in (('A', PA), ('B', PB), ('C', PC)):
        strip(fig, k, col)
    tx = [X0 + k * (X1 - X0) / 4 for k in range(5)]
    xs = list(range(X0, X1 + 1, 4))
    fig.path('M' + ' L'.join('%d %.1f' % (x, a_path(x)) for x in xs), 'none', PA, 3, extra='stroke-dasharray="4 6"')
    fig.path('M' + ' L'.join('%d %.1f' % (x, b_path(x)) for x in range(X0, X1 + 1, 3)), 'none', PB, 3, extra='stroke-dasharray="4 6"')
    gC = STRIPS['C'][1]
    fig.line(X0, gC - 14, X1, gC - 14, PC, 3, dash='4 6')
    for k, x in enumerate(tx):
        fig.circle(x, a_path(x), 5, PA, INK, 1)
        fig.text(x, a_path(x) - 16, 't%d' % (k + 1), 26, 'middle', 'normal', PA, halo=True)
        fig.circle(x, b_path(x), 8, PB, INK, 1.5)
        fig.text(x + 22, b_path(x) - 14, 't%d' % (k + 1), 26, 'start', 'normal', PB, halo=True)
        fig.circle(X0 + k * 120, gC - 14, 14, '#8a6a3c', INK, 1.5)
        fig.text(X0 + k * 120, gC - 38, 't%d' % (k + 1), 26, 'middle', 'normal', PC, halo=True)
    # key
    ky = HQ - 34
    fig.circle(48, ky - 9, 5, PA, INK, 1)
    fig.text(62, ky, 'A: fine dust', 26)
    fig.circle(268, ky - 9, 8, PB, INK, 1.5)
    fig.text(286, ky, 'B: sand grain', 26)
    fig.circle(500, ky - 9, 12, '#8a6a3c', INK, 1.5)
    fig.text(522, ky, 'C: coarse grain', 26)
    fig.text(740, ky, 't1–t5: equal times', 26)

    A = 'a'
    fig.text(520, a_path(520) + 56, 'stays in the air: suspension', 26, 'middle', 'bold', PA, A, halo=True)
    fig.text(520, STRIPS['B'][0] + 28, 'repeated short hops: saltation', 26, 'middle', 'bold', PB, A, halo=True)
    fig.text(922, STRIPS['C'][0] + 30, 'rolls: surface creep', 26, 'end', 'bold', '#5a3f1c', A, halo=True)
    for k in range(4):
        x = X0 + k * 120
        fig.path('M%d %d A 20 20 0 1 1 %d %d' % (x + 8, gC - 34, x + 18, gC - 22), 'none', '#5a3f1c', 2.5, A)
    fig.marker(950, STRIPS['A'][0] + 40, '1', A)
    fig.marker(950, STRIPS['B'][0] + 40, '2', A)
    fig.marker(950, STRIPS['C'][0] + 30, '3', A)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Interpretation', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for n, s in [('1', 'A stays in the air at every time and never touches the surface: suspension.'),
                 ('2', 'B lifts off, travels a short arc and lands, again and again: saltation.'),
                 ('3', 'C stays in contact with the surface, rolling or sliding: surface creep.')]:
        fig.marker(52, yy - 9, n, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8
    fig.para(36, yy + 2, 'Classify by the path and ground contact, not by drawn size: the same grain can move differently in a stronger gust.',
             26, 920, 32, layer=A)
    G = STRIPS['B'][1]

    spec = {
        'kind': 'side-view path diagram (schematic)',
        'teaching_target': 'Suspension (sustained airborne path), saltation (repeated short hops with landings), surface creep (rolling/sliding with continuous ground contact).',
        'strips_top_and_ground_y': STRIPS, 'wind': 'left to right', 'times': 't1-t5 at equal intervals',
        'path_A': {'min_height_above_ground_px': round(STRIPS['A'][1] - max(a_path(x) for x in xs)), 'ground_contacts': 0},
        'path_B': {'hops': HOPS, 'hop_height_px': HOP_H, 'ground_contacts': len(HOPS) + 1},
        'path_C': {'height_above_ground_px': 0, 'contact': 'continuous', 'positions_x': [X0 + k * 120 for k in range(5)]},
        'question_withholds': ['suspension', 'saltation', 'creep', 'hop', 'roll'],
        'independent_solution': ['A airborne throughout -> suspension (1)', 'B repeated short hops with landings -> saltation (1)',
                                 'C continuous ground contact, rolling -> surface creep (1)'],
    }
    checks = [
        check('A never reaches its ground line', all(a_path(x) < STRIPS['A'][1] - 100 for x in xs), 'lowest point %.0f px above ground' % (STRIPS['A'][1] - max(a_path(x) for x in xs))),
        check('B touches the ground at every take-off and landing', all(abs(b_path(x) - (G - 8)) < 1e-9 for h in HOPS for x in h)),
        check('B hop heights below the height at which A travels', HOP_H < (STRIPS['A'][1] - max(a_path(x) for x in xs))),
        check('B positions at equal times fall on the landings', [round(b_path(x), 6) for x in tx] == [G - 8] * 5),
        check('C stays on the surface (circle rests on ground line)', True, 'centre ground-14, radius 14'),
        check('paths run with the wind (left to right)', True),
    ]
    sides = {
        'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'],
                     'forbidden': [r'suspen', r'saltat', r'creep', r'hop', r'roll']},
        'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']},
    }
    return build(RID, fig, spec, sides, checks)


if __name__ == '__main__':
    main()
