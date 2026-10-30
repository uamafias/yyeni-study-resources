"""VIS-6137-3.1-03 -> ITEM-6137-3.1-037-INTERP: density map and table for regions A and B.

Values (card and notes BL-6137-3.1.09-07): A 20,000 residents in 1,000 km^2; B 30,000 in 3,000 km^2.
Regions are drawn to scale: A 20 km x 50 km, B 50 km x 60 km at PX_PER_KM, with a scale bar. The
question map is unshaded (key given); the answer shades A in the 20+ class and B in 10-<20.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, table, build, check  # noqa: E402

RID = 'VIS-6137-3.1-03'
ITEM = 'ITEM-6137-3.1-037-INTERP'
W, HQ, HA = 1000, 800, 1120
PX_PER_KM = 5.5
REG = {'A': (20000, 20, 50), 'B': (30000, 50, 60)}          # residents, width km, height km
CLASSES = [('0 to under 10', 0, 10, '#f3ecd3'), ('10 to under 20', 10, 20, '#e6b35a'), ('20 or more', 20, 1e9, '#a6461e')]


def cls(d):
    return next(c for c in CLASSES if c[1] <= d < c[2])


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'Population density of regions A and B (schematic map, to scale)')
    x, y0 = 60, 110
    boxes = {}
    for k in ('A', 'B'):
        pop, wk, hk = REG[k]
        w, h = wk * PX_PER_KM, hk * PX_PER_KM
        dens = pop / (wk * hk)
        fig.under('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s"/>' % (x, y0, w, h, cls(dens)[3]))
        fig.rect(x, y0, w, h, 'none', INK, 2.5)
        fig.text(x + w / 2, y0 + h / 2 + 12, k, 40, 'middle', 'bold', INK, halo=True)
        boxes[k] = (x, w, h)
        x += w + 40
    fig.line(60, y0 + 360, 60 + 20 * PX_PER_KM, y0 + 360, INK, 4)
    for t in (0, 10, 20):
        fig.line(60 + t * PX_PER_KM, y0 + 352, 60 + t * PX_PER_KM, y0 + 368, INK, 2)
    fig.text(60, y0 + 400, '0', 26, 'middle')
    fig.text(60 + 20 * PX_PER_KM, y0 + 400, '20 km', 26, 'middle')
    # key
    kx = 640
    fig.text(kx, 140, 'Key: people per km²', 26, 'start', 'bold')
    for i, (lab, lo, hi, col) in enumerate(CLASSES):
        fig.rect(kx, 165 + i * 50, 40, 32, col, INK, 1.5)
        fig.text(kx + 52, 190 + i * 50, lab, 26)
    table(fig, 60, 570, [180, 300, 300], 52, [['Region', 'Residents', 'Area (km²)']] +
          [[k, '{:,}'.format(REG[k][0]), '{:,}'.format(REG[k][1] * REG[k][2])] for k in ('A', 'B')], align=['middle'] * 3)

    A = 'a'
    for k in ('A', 'B'):
        x, w, h = boxes[k]
        d = REG[k][0] / (REG[k][1] * REG[k][2])
        fig.text(x + w / 2, y0 + h + 34, '%d per km²' % d, 26, 'middle', 'bold', C['answer'], A, halo=True)
    fig.marker(36, 140, '1', A)
    fig.marker(900, 610, '2', A)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Interpretation', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for k, s in [('1', 'A: 20,000 ÷ 1,000 = 20 people per km² (highest class). B: 30,000 ÷ 3,000 = 10 per km² (middle class).'),
                 ('2', 'B has more people in total but a lower average density, because its area is three times larger.'),
                 ('3', 'Shading gives an average; it does not show how evenly people are spread within A or B.')]:
        fig.marker(52, yy - 9, k, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8

    dens = {k: REG[k][0] / (REG[k][1] * REG[k][2]) for k in REG}
    spec = {'kind': 'schematic choropleth to scale with data table', 'regions': {k: {'residents': v[0], 'area_km2': v[1] * v[2], 'drawn_km': [v[1], v[2]]} for k, v in REG.items()},
            'px_per_km': PX_PER_KM, 'densities': dens, 'classes': [(c[0], c[1], c[2] if c[2] < 1e8 else None) for c in CLASSES],
            'question_withholds': ['shading', 'density values'],
            'independent_solution': ['A 20/km2 highest class; B 10/km2 middle class (1)', 'B larger total, lower density (1)', 'average hides distribution (1)']}
    checks = [check('areas 1,000 and 3,000 km2', [REG[k][1] * REG[k][2] for k in 'AB'] == [1000, 3000]),
              check('densities 20 and 10', dens == {'A': 20, 'B': 10}),
              check('A in 20+ class, B in 10-<20 class', cls(dens['A'])[0] == '20 or more' and cls(dens['B'])[0] == '10 to under 20'),
              check('drawn to scale (area ratio 1:3)', abs((50 * 60) / (20 * 50) - 3) < 1e-9)]
    sides = {'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'], 'forbidden': [r'per km²$', r'\b20 per', r'\b10 per']},
             'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a', 'au']}}
    return build(RID, fig, spec, sides, checks)


if __name__ == '__main__':
    main()
