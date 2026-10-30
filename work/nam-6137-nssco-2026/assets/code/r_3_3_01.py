"""VIS-6137-3.3-01 -> ITEM-6137-3.3-002-INTERP; reused by 003 (panel A), 004 (panel B), 005 (panel C).

Three plan panels at one scale (same frame size and 500 m scale bar), each with exactly eight house
symbols: A spread among farm plots, B along one east-west route, C grouped around a crossroads.
Schematic, not real places. The question names only A, B, C; the answer adds dispersed, linear and
nucleated. House positions are listed in the spec; the check confirms eight per panel and the
spacing contrast (mean nearest-neighbour distance).
"""
import math
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, build, check  # noqa: E402

RID = 'VIS-6137-3.3-01'
ITEM = 'ITEM-6137-3.3-002-INTERP'
W, HQ, HA = 1000, 640, 905
PW, PH = 300, 420
HOUSES = {
    'A': [(45, 60), (200, 50), (250, 160), (90, 190), (170, 260), (40, 330), (250, 330), (140, 380)],
    'B': [(30, 200), (65, 228), (105, 200), (140, 228), (180, 200), (215, 228), (250, 200), (282, 228)],
    'C': [(125, 180), (175, 180), (125, 245), (175, 245), (100, 205), (200, 220), (150, 150), (150, 280)],
}
FIELD = '#e7efcf'


def house(fig, x, y):
    fig.poly([(x - 11, y + 9), (x - 11, y - 3), (x, y - 13), (x + 11, y - 3), (x + 11, y + 9)], '#b0413e', INK, 1.5)


def nn_mean(pts):
    return sum(min(math.dist(p, q) for q in pts if q != p) for p in pts) / len(pts)


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'Three settlement patterns (plans at the same scale; schematic)')
    for k, key in enumerate('ABC'):
        x0, y0 = 20 + k * 330, 70
        fig.rect(x0, y0, PW, PH, FIELD, GREY, 2, 6)
        fig.text(x0 + 14, y0 + 38, key, 32, 'start', 'bold', INK, halo=True)
        if key == 'A':
            for gx in (100, 200):
                fig.line(x0 + gx, y0 + 50, x0 + gx, y0 + PH, '#8a9a5b', 2, dash='6 5')
            for gy in (120, 230, 300):
                fig.line(x0, y0 + gy, x0 + PW, y0 + gy, '#8a9a5b', 2, dash='6 5')
            fig.line(x0, y0 + 400, x0 + PW, y0 + 400, '#8c8c8c', 6)
        if key == 'B':
            fig.line(x0, y0 + 214, x0 + PW, y0 + 214, '#8c8c8c', 10)
        if key == 'C':
            fig.line(x0, y0 + 212, x0 + PW, y0 + 212, '#8c8c8c', 10)
            fig.line(x0 + 150, y0 + 50, x0 + 150, y0 + PH, '#8c8c8c', 10)
        for hx, hy in HOUSES[key]:
            house(fig, x0 + hx, y0 + hy)
    # scale bar and north arrow, key
    sb = 0.4                                     # px per metre: 500 m = 200 px in every panel
    fig.line(40, 530, 40 + 500 * sb, 530, INK, 4)
    for t in (0, 250, 500):
        fig.line(40 + t * sb, 522, 40 + t * sb, 538, INK, 2)
    fig.text(40, 566, '0', 26, 'middle')
    fig.text(40 + 500 * sb, 566, '500 m', 26, 'middle')
    fig.text(150, 600, 'same scale in A, B and C', 26, 'start', 'normal', GREY)
    fig.arrow(330, 570, 330, 512, INK, 4, 14)
    fig.text(345, 560, 'N', 26, 'start', 'bold')
    house(fig, 430, 530)
    fig.text(452, 539, 'house', 26)
    fig.line(560, 530, 610, 530, '#8c8c8c', 8)
    fig.text(622, 539, 'road', 26)
    fig.line(710, 530, 760, 530, '#8a9a5b', 2, dash='6 5')
    fig.text(772, 539, 'field boundary', 26)

    A = 'a'
    for k, (key, lab) in enumerate((('A', 'dispersed'), ('B', 'linear'), ('C', 'nucleated'))):
        fig.text(20 + k * 330 + PW / 2, 70 + PH + 0 - 12, lab, 28, 'middle', 'bold', C['answer'], A, halo=True)
        fig.marker(20 + k * 330 + PW - 30, 100, str(k + 1), A)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Interpretation (8 houses in every panel)', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for k, s in [('1', 'A: houses lie apart with farm plots between them: dispersed.'),
                 ('2', 'B: houses line up along the east–west road: linear.'),
                 ('3', 'C: houses cluster round the crossroads: nucleated. The plans show form only, not wealth or the exact historical cause.')]:
        fig.marker(52, yy - 9, k, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8

    nn = {k: round(nn_mean(v), 1) for k, v in HOUSES.items()}
    spec = {'kind': 'three plan panels at one scale (schematic)', 'houses_panel_coords': HOUSES, 'scale_px_per_m': sb, 'panel_px': [PW, PH],
            'mean_nearest_neighbour_px': nn, 'reuses': {'ITEM-6137-3.3-003-INTERP': 'panel A', 'ITEM-6137-3.3-004-INTERP': 'panel B', 'ITEM-6137-3.3-005-INTERP': 'panel C'},
            'question_withholds': ['dispersed', 'linear', 'nucleated'],
            'independent_solution': ['A dispersed (1)', 'B linear (1)', 'C nucleated; form only (1)']}
    ys_b = [y for x, y in HOUSES['B']]
    checks = [check('eight houses in every panel', all(len(v) == 8 for v in HOUSES.values())),
              check('A most spread out (largest mean nearest-neighbour distance)', nn['A'] > nn['B'] and nn['A'] > nn['C'], str(nn)),
              check('B houses all within 20 px of the east-west road', all(abs(y - 214) <= 20 for y in ys_b)),
              check('C houses all within 90 px of the crossroads', all(math.dist((x, y), (150, 212)) <= 90 for x, y in HOUSES['C'])),
              check('B spans the panel width (elongated)', max(x for x, y in HOUSES['B']) - min(x for x, y in HOUSES['B']) > 0.8 * PW)]
    sides = {'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'], 'forbidden': [r'dispers', r'linear', r'nucleat']},
             'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']}}
    return build(RID, fig, spec, sides, checks, panels=[(20 + k * 330, 70, PW, PH) for k in range(3)])


if __name__ == '__main__':
    main()
