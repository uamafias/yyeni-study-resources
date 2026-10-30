"""VIS-6137-1.1-02 -> ITEM-6137-1.1-013-INTERP: constructive (divergent) margin cross-section, not to scale.

A mid-ocean ridge: sea floor rises to a crest with a central rift opening; magma below the ridge
reaches the opening through a fissure. Crust is banded by age, symmetric about the centre line, so
"new crust at the centre, older crust farther away" can be read from the question image. Everything
is generated from the distance d = x - CX from the centre line.
"""
import math
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, build, check  # noqa: E402

RID = 'VIS-6137-1.1-02'
ITEM = 'ITEM-6137-1.1-013-INTERP'
W, HQ, HA = 1000, 700, 1120
CX = 500
SEA = 120
CRUST = 24                       # crust thickness (px)
BANDS = [(0, 70, '#4a1f14', 'newest'), (70, 200, '#8a4a32', 'older'),
         (200, 340, '#bf7f5e', 'older still'), (340, 600, '#deb08f', 'oldest')]


def floor_y(x):
    d = abs(x - CX)
    ridge = 300 - 80 * math.exp(-(d / 230) ** 2)          # broad ridge, crest 80 px above the plains
    rift = 26 * math.exp(-(d / 22) ** 2)                  # central rift valley (the opening)
    return ridge + rift


def lith_base(x):
    d = abs(x - CX)
    return floor_y(x) + CRUST + 6 + 6.0 * math.sqrt(d)    # lithosphere thickens away from the ridge


def band_of(x):
    d = abs(x - CX)
    for i, (a, b, col, name) in enumerate(BANDS):
        if a <= d < b:
            return i
    return len(BANDS) - 1


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'Cross-section across a plate margin (not to scale)')
    xs = list(range(0, W + 1, 4))
    # mantle, ocean
    fig.rect(0, SEA, W, HQ - SEA, C['mantle'], 'none', 0)
    fig.poly([(0, SEA), (W, SEA)] + [(x, floor_y(x)) for x in xs[::-1]], C['sea'], 'none', 0)
    fig.line(0, SEA, W, SEA, C['blue'], 2.5)
    fig.text(16, SEA - 12, 'Sea level', 26, 'start', 'normal', C['blue'])
    fig.text(170, SEA + 62, 'Ocean', 28, 'middle', 'normal', C['blue'], italic=True)
    # lithospheric mantle (below the crust) on each side of the fissure
    gap = 9
    for side in (-1, 1):
        sx = [x for x in xs if (x - CX) * side >= gap]
        top = [(x, floor_y(x) + CRUST) for x in sx]
        bot = [(x, lith_base(x)) for x in sx]
        fig.poly(top + bot[::-1], C['oc_lith'], INK, 1.5)
    # age-banded crust, symmetric about the centre line, split by the fissure
    for side in (-1, 1):
        for i, (a, b, col, name) in enumerate(BANDS):
            lo, hi = max(a, gap), min(b, CX)
            if lo >= hi:
                continue
            seg = [CX + side * d for d in range(int(lo), int(hi) + 1, 2)]
            top = [(x, floor_y(x)) for x in seg]
            bot = [(x, floor_y(x) + CRUST) for x in seg]
            fig.poly(top + bot[::-1], col, 'none', 0)
        sx = [x for x in xs if (x - CX) * side >= gap]
        fig.poly([(x, floor_y(x)) for x in sx], 'none', INK, 2, closed=False)
    # magma chamber and fissure to the central opening
    mcy = 470
    fig.add('<ellipse cx="%d" cy="%d" rx="95" ry="34" fill="%s" stroke="%s" stroke-width="2"/>' % (CX, mcy, C['magma'], INK))
    fig.poly([(CX - gap + 2, floor_y(CX)), (CX + gap - 2, floor_y(CX)), (CX + 7, mcy - 30), (CX - 7, mcy - 30)],
             C['magma'], 'none', 0)
    # labels
    fig.text(170, 348, 'Plate R', 28, 'middle', 'bold', '#ffffff')
    fig.text(830, 348, 'Plate S', 28, 'middle', 'bold', '#ffffff')
    fig.text(CX, 640, 'Mantle', 28, 'middle', 'bold', '#7a4a2a')
    fig.text(CX + 70, SEA + 50, 'Central opening', 26, 'start', 'bold', INK, halo=True)
    fig.line(CX + 66, SEA + 44, CX + 6, floor_y(CX) - 8, INK, 1.5)
    # plate-motion arrows inside each plate, pointing away from the centre
    fig.arrow(290, 372, 80, 372, INK, 6, 24)
    fig.arrow(710, 372, 920, 372, INK, 6, 24)
    # key (age bands and symbols)
    ky = 545
    fig.rect(14, ky - 30, 330, 150, '#ffffff', GREY, 1.5, 6)
    fig.text(28, ky, 'Oceanic crust', 26, 'start', 'bold')
    for i, (a, b, col, name) in enumerate(BANDS):
        fig.rect(28 + i * 74, ky + 14, 66, 24, col, INK, 1)
    fig.text(28, ky + 66, 'newest', 26)
    fig.text(322, ky + 66, 'oldest', 26, 'end')
    fig.arrow(28, ky + 100, 98, ky + 100, INK, 5, 18)
    fig.text(110, ky + 109, 'plate movement', 26)
    fig.rect(700, ky - 30, 286, 66, '#ffffff', GREY, 1.5, 6)
    fig.rect(716, ky - 12, 40, 26, C['magma'], INK, 1)
    fig.text(770, ky + 10, 'magma', 26)

    # ---- answer layer ---------------------------------------------------------------------------
    A = 'a'
    fig.arrow(CX, mcy - 40, CX, floor_y(CX) + 12, '#ffffff', 3, 12, A, halo=False)    # magma rising in the fissure
    # spreading arrows on the crust bands either side: new crust carried outwards
    for side in (-1, 1):
        x0 = CX + side * 40
        x1 = CX + side * 150
        fig.arrow(x0, floor_y(x0) - 14, x1, floor_y(x1) - 14, C['answer'], 4, 16, A)
    # mantle upwelling beneath the ridge
    for side in (-1, 1):
        fig.path('M%d %d C %d %d, %d %d, %d %d' % (CX + side * 50, 695, CX + side * 40, 630, CX + side * 90, 600,
                                                   CX + side * 150, 588), 'none', '#7a4a2a', 3, A,
                 extra='stroke-dasharray="8 6"')
    fig.marker(185, 405, '1')
    fig.marker(815, 405, '1')
    fig.marker(CX - 42, floor_y(CX) + 64, '2')
    fig.marker(CX + 120, floor_y(CX + 120) - 50, '3')
    fig.marker(CX - 120, floor_y(CX - 120) - 50, '3')
    fig.text(CX + 108, mcy + 10, 'magma rises', 26, 'start', 'bold', C['magma'], A, halo=True)

    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Interpretation', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for n, s in [('1', 'The arrows point away from the centre: plates R and S move apart.'),
                 ('2', 'Magma rises through the fissure into the central opening, where it cools and solidifies.'),
                 ('3', 'The newest crust lies at the centre, with progressively older crust farther away on both '
                       'sides: new crust forms at the opening and moves outward with the separating plates.')]:
        fig.marker(52, yy - 9, n, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8
    yy += 4
    fig.para(36, yy, 'Pressure falls as mantle rises beneath the separating plates (dashed), so some of it partly '
             'melts. The margin is constructive because lithosphere is added.', 26, 920, 32, layer=A)

    left = [band_of(CX - d) for d in range(gap, CX, 10)]
    right = [band_of(CX + d) for d in range(gap, CX, 10)]
    spec = {
        'kind': 'process cross-section (schematic, not to scale)',
        'teaching_target': 'Divergence at a constructive margin: arrows apart, magma rising into the central opening and solidifying, new crust at the centre carried outward.',
        'viewing_direction': 'vertical cross-section across a mid-ocean ridge',
        'geometry': {'centre_x': CX, 'sea_level_y': SEA, 'crest_floor_y': round(floor_y(CX), 1),
                     'plain_floor_y': round(floor_y(0), 1), 'crust_px': CRUST,
                     'age_bands_distance_px': [[a, b, name] for a, b, c, name in BANDS],
                     'magma_chamber': [CX, mcy, 95, 34]},
        'question_shows': ['arrows pointing away from the centre in plates R and S', 'central opening (labelled) with a magma-filled fissure from a magma body',
                           'crust age bands with a newest-to-oldest key', 'key'],
        'question_withholds': ['margin type name', 'rising/cooling/solidifying arrows and wording', 'outward crust-transport arrows', 'mantle upwelling'],
        'independent_solution': ['arrows point away from the centre -> plates move apart (1)', 'magma reaches the opening and cools there (1)',
                                 'newest crust at the centre, older outward on both sides -> new crust carried outward (1)'],
        'assumptions': ['Not to scale; age bands are schematic, not dated.', 'Symmetry is idealised; the notes state perfect symmetry is not required in reality.'],
    }
    checks = [
        check('arrows diverge from the centre line', 330 > 100 and 670 < 900 and 100 < CX < 900),
        check('crest is the highest sea floor', all(floor_y(x) >= floor_y(CX + 40) - 1e-9 for x in range(0, W, 5) if abs(x - CX) > 40)),
        check('rift opening is lower than the crest beside it', floor_y(CX) > floor_y(CX + 40)),
        check('age bands symmetric', left == right),
        check('age increases monotonically away from centre', left == sorted(left)),
        check('fissure connects magma body to the opening', mcy - 34 < mcy - 30 + 10 and floor_y(CX) < mcy),
        check('lithosphere thickens away from the ridge', lith_base(CX + 400) - floor_y(CX + 400) > lith_base(CX + 50) - floor_y(CX + 50)),
    ]
    sides = {
        'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'],
                     'forbidden': [r'construct', r'diverg', r'apart', r'rise', r'cool', r'solidif', r'spread']},
        'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']},
    }
    return build(RID, fig, spec, sides, checks)


if __name__ == '__main__':
    main()
