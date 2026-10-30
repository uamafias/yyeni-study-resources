"""VIS-6137-1.4-01 -> ITEM-6137-1.4-007-INTERP: wind-erosion features in three panels plus a key.

(A) Residual rock, side view: narrow stem below a wider top; sand grains moving near the ground.
(B) Loose-sediment patch, cross-section: earlier surface (dashed) and the present surface 15 cm
    lower at the centre (survey pegs), rocky margin unchanged - values from notes BL-6137-1.4.02-09.
(C) Stony surface, plan view before and after: gravel covers 40% then 70% (notes BL-6137-1.4.02-09);
    the same stones are drawn in both squares, only the fines between them are removed.
"""
import math
import os
import random
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, build, check  # noqa: E402

RID = 'VIS-6137-1.4-01'
ITEM = 'ITEM-6137-1.4-007-INTERP'
W, HQ, HA = 1000, 925, 1300
PW, PH = 470, 395
FINE = '#e9d29a'
ROCK = '#b9886a'
GRAVEL = '#7d766b'


def frame(fig, x0, y0, lab, title):
    fig.rect(x0, y0, PW, PH, '#ffffff', GREY, 2, 8)
    fig.text(x0 + 16, y0 + 38, lab, 30, 'start', 'bold', C['answer'])
    fig.text(x0 + 52, y0 + 38, title, 26, 'start', 'bold')


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'Three features in a dry, windy area (not to scale)')
    A = 'a'
    # ---- (A) residual rock
    x0, y0 = 20, 60
    frame(fig, x0, y0, 'A', 'Isolated rock, side view')
    g = y0 + 330
    fig.rect(x0 + 2, g, PW - 4, 20, FINE, 'none', 0)
    cx = x0 + 250
    shape = [(-40, 0), (-34, 60), (-30, 120), (-60, 150), (-120, 175), (-110, 215), (-20, 238), (90, 225), (125, 185), (70, 150),
             (32, 122), (36, 60), (44, 0)]
    rock = [(cx + 0.85 * dx, g - 0.85 * dy) for dx, dy in shape]
    fig.poly(rock, ROCK, INK, 2.5)
    rnd = random.Random(7)
    for k in range(26):
        x = x0 + 20 + rnd.random() * 220
        y = g - 6 - rnd.random() * 70
        fig.circle(x, y, 3.2, '#8a6a2e', 'none', 0)
    fig.arrow(x0 + 24, g - 100, x0 + 200, g - 100, INK, 4, 16)
    fig.text(x0 + 24, g - 150, 'wind with', 26, 'start', 'normal', INK, halo=True)
    fig.text(x0 + 24, g - 118, 'moving sand', 26, 'start', 'normal', INK, halo=True)
    fig.text(x0 + 16, y0 + PH - 16, 'Most sand moves near the ground', 26)
    # ---- (B) loose-sediment patch
    x0, y0 = 510, 60
    frame(fig, x0, y0, 'B', 'Loose-sediment patch, section')
    top = y0 + 160
    fig.poly([(x0 + 20, top), (x0 + 120, top), (x0 + 160, top + 30), (x0 + 235, top + 60), (x0 + 310, top + 30), (x0 + 350, top),
              (x0 + 450, top), (x0 + 450, y0 + 290), (x0 + 20, y0 + 290)], FINE, INK, 2.5)
    fig.poly([(x0 + 20, top - 2), (x0 + 120, top - 2), (x0 + 110, y0 + 290), (x0 + 20, y0 + 290)], '#a59d8f', INK, 2)
    fig.poly([(x0 + 350, top - 2), (x0 + 450, top - 2), (x0 + 450, y0 + 290), (x0 + 360, y0 + 290)], '#a59d8f', INK, 2)
    fig.line(x0 + 120, top, x0 + 350, top, INK, 2.5, dash='10 7')
    fig.line(x0 + 235, top - 40, x0 + 235, top + 60, INK, 3)
    fig.text(x0 + 245, top - 22, 'survey peg', 26, 'start', 'normal', INK, halo=True)
    fig.text(x0 + 30, top - 52, 'rock', 26, 'start', 'normal', INK, halo=True)
    fig.text(x0 + 440, top - 52, 'rock', 26, 'end', 'normal', INK, halo=True)
    fig.text(x0 + 16, y0 + PH - 50, 'Centre: 15 cm lower than the earlier', 26)
    fig.text(x0 + 16, y0 + PH - 18, 'surface; rocky margins unchanged', 26)
    # ---- (C) stony surface before/after. A 6 x 6 jittered grid of stone polygons fills the later square;
    # the earlier square shows only the stones then exposed. Cover is computed from the polygon areas.
    x0, y0 = 20, 470
    frame(fig, x0, y0, 'C', 'Stony surface, plan view')
    rnd = random.Random(11)
    SQ, N = 180, 6
    cell = SQ / N
    stones = []
    for i in range(N):
        for j in range(N):
            cxs, cys = (i + 0.5) * cell + rnd.uniform(-0.5, 0.5), (j + 0.5) * cell + rnd.uniform(-0.5, 0.5)
            apo = cell * 0.5 * rnd.uniform(0.92, 0.97)          # octagonal stone: apothem just inside the cell
            pts = []
            for k in range(8):
                ang = math.pi / 8 + 2 * math.pi * k / 8 + rnd.uniform(-0.08, 0.08)
                rr = apo / math.cos(math.pi / 8) * rnd.uniform(0.97, 1.0)
                pts.append((cxs + rr * math.cos(ang), cys + rr * math.sin(ang)))
            stones.append(pts)
    from shapely.geometry import Polygon
    from shapely.ops import unary_union
    area = lambda P: Polygon(P).area
    overlap = sum(Polygon(P).area for P in stones) - unary_union([Polygon(P) for P in stones]).area
    total = SQ * SQ
    order = list(range(len(stones)))
    rnd.shuffle(order)
    later_cover = sum(area(P) for P in stones) / total
    earlier, acc = [], 0.0
    for k in order:                                      # stones exposed earlier: add until cover reaches 40%
        if acc + area(stones[k]) / total <= 0.405:
            earlier.append(k)
            acc += area(stones[k]) / total
    earlier_cover = acc
    for bx, title, pct, idx, fines in [(x0 + 30, 'Earlier', 40, earlier, True), (x0 + 260, 'Later', 70, range(len(stones)), False)]:
        by = y0 + 100
        fig.text(bx + 90, by - 16, title, 26, 'middle', 'bold')
        fig.rect(bx, by, SQ, SQ, FINE if fines else '#f6efdc', INK, 2)
        if fines:
            for _ in range(220):
                fig.circle(bx + 4 + rnd.random() * 172, by + 4 + rnd.random() * 172, 1.6, '#a38545', 'none', 0)
        for k in idx:
            fig.poly([(bx + px, by + py) for px, py in stones[k]], GRAVEL, INK, 1.2)
        fig.text(bx + 90, by + 214, 'gravel cover %d%%' % pct, 26, 'middle')
    # ---- (D) key
    x0, y0 = 510, 470
    fig.rect(x0, y0, PW, PH, '#ffffff', GREY, 2, 8)
    fig.text(x0 + 16, y0 + 38, 'Key', 28, 'start', 'bold')
    rows = [('rect', FINE, 'loose fine sediment'), ('rect', ROCK, 'rock (A)'), ('rect', '#a59d8f', 'rock (B)'),
            ('stone', GRAVEL, 'gravel and stones'), ('dash', None, 'earlier ground surface'), ('arrow', None, 'wind direction')]
    for i, (kind, col, lab) in enumerate(rows):
        yy = y0 + 86 + i * 50
        if kind == 'rect':
            fig.rect(x0 + 30, yy - 22, 40, 26, col, INK, 1.5)
        elif kind == 'stone':
            fig.circle(x0 + 50, yy - 9, 12, col, INK, 1.2)
        elif kind == 'dash':
            fig.line(x0 + 26, yy - 9, x0 + 74, yy - 9, INK, 2.5, dash='10 7')
        else:
            fig.arrow(x0 + 26, yy - 9, x0 + 76, yy - 9, INK, 4, 14)
        fig.text(x0 + 92, yy, lab, 26)

    # ---- answer layer
    cx, g = 20 + 300, 60 + 330
    fig.marker(48, 126, '1', A)
    fig.text(74, 135, 'rock pedestal', 26, 'start', 'bold', C['answer'], A, halo=True)
    fig.text(cx - 44, g - 30, 'narrow stem', 26, 'end', 'bold', C['answer'], A, halo=True)
    fig.text(cx + 30, g - 214, 'wider top', 26, 'start', 'bold', C['answer'], A, halo=True)
    bx0, top = 510, 60 + 160
    fig.line(bx0 + 226, top, bx0 + 226, top + 56, C['answer'], 3, A)       # beside the peg, to the hollow floor
    fig.line(bx0 + 218, top, bx0 + 234, top, C['answer'], 3, A)
    fig.line(bx0 + 218, top + 56, bx0 + 234, top + 56, C['answer'], 3, A)
    fig.text(bx0 + 214, top + 36, '15 cm', 26, 'end', 'bold', C['answer'], A, halo=True)
    fig.marker(bx0 + 150, top + 98, '2', A)
    fig.text(bx0 + 176, top + 107, 'deflation hollow', 26, 'start', 'bold', C['answer'], A, halo=True)
    fig.marker(20 + 260 + 180 - 4, 470 + 70, '3', A)
    fig.text(20 + 260 + 90, 470 + 100 + 248, 'desert pavement', 26, 'middle', 'bold', C['answer'], A, halo=True)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Interpretation', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for n, s in [('1', 'A: a narrow stem below a wider top is a rock pedestal; abrasion by sand moving near the ground wears the lower part most.'),
                 ('2', 'B: the centre has been lowered 15 cm while the rock margins stayed put, so loose material was removed: a deflation hollow.'),
                 ('3', 'C: fine sediment has gone from between the stones and gravel now covers 70% of the surface, not 40%: a desert pavement left by selective removal. Stones are exposed and concentrated, not added.')]:
        fig.marker(52, yy - 9, n, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8

    spec = {
        'kind': 'three-panel resource (side view, section, plan before/after) with key; schematic',
        'teaching_target': 'Distinguish a rock pedestal (residual narrow stem, wider top), a deflation hollow (lowered loose-sediment patch) and a desert pavement (concentrated stony cover after removal of fines).',
        'panel_B': {'lowering_cm': 15, 'margins': 'unchanged'},
        'panel_C': {'stated_gravel_cover_percent': [40, 70], 'drawn_cover_percent': [round(100 * earlier_cover, 1), round(100 * later_cover, 1)],
                    'stones_later': len(stones), 'stones_earlier': len(earlier),
                    'note': 'Earlier stones are a subset of the later stones (the rest were then covered by fines); none is added.'},
        'question_withholds': ['pedestal', 'deflation', 'hollow', 'pavement', 'abrasion'],
        'independent_solution': ['A: narrow stem below wider top -> pedestal (1)', 'B: centre lowered 15 cm, margins unchanged -> deflation hollow (1)',
                                 'C: fines removed, stones exposed and concentrated, cover 40 -> 70% -> desert pavement (1)'],
        'assumptions': ['Percentages are stated values from notes block 1.4.02-09, not measured from the drawing.',
                        'The pedestal drawing does not claim abrasion acted alone (notes 1.4.02-03).'],
    }
    stem_w = 36 + 44
    top_w = 120 + 125
    checks = [
        check('pedestal stem narrower than its top', stem_w < top_w, 'stem ~%d px, top ~%d px' % (stem_w, top_w)),
        check('moving sand drawn near the ground only', True, 'grains within 76 px of the ground line'),
        check('panel B: centre lower than the dashed earlier surface; margins at the earlier level', True, 'centre depth 60 px'),
        check('panel C: drawn cover matches the stated 40% and 70% within 2 points',
              abs(100 * earlier_cover - 40) <= 2 and abs(100 * later_cover - 70) <= 2,
              'drawn %.1f%% and %.1f%%' % (100 * earlier_cover, 100 * later_cover)),
        check('panel C: every earlier stone is also present later (none added)', set(earlier) <= set(range(len(stones)))),
        check('panel C: stones do not overlap (union area equals summed area)', overlap < 1, 'overlap %.2f px2' % overlap),
    ]
    sides = {
        'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'],
                     'forbidden': [r'pedestal', r'deflat', r'hollow', r'pavement', r'abras']},
        'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']},
    }
    return build(RID, fig, spec, sides, checks, panels=[(20, 60, PW, PH), (510, 60, PW, PH), (20, 470, PW, PH), (510, 470, PW, PH)])


if __name__ == '__main__':
    main()
