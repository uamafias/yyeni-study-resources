"""VIS-6137-3.3-02 -> ITEM-6137-3.3-015-INTERP; reused by 016 (CBD), 017 (housing), 018 (industry),
019 (shopping), 020 (open space) and 021 (transport).

A schematic urban land-use plan matching notes BL-6137-3.3.04-14 (not a measured map of Windhoek or any
real town; stated on the figure). Main roads meet at the central junction, where the CBD (offices, shops,
services) sits; housing lies west and south (buildings of varied form); industry lies beside a freight
railway on the east; a shopping strip lines the northern access road; a park lies south-east.
"""
import os
import random
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, build, check  # noqa: E402
from shapely.geometry import Point, Polygon  # noqa: E402

RID = 'VIS-6137-3.3-02'
ITEM = 'ITEM-6137-3.3-015-INTERP'
W, HQ, HA = 1000, 900, 1260
J = (480, 400)                                   # central junction
ZONES = {
    'housing_west': ([(40, 90), (400, 90), (400, 470), (40, 470)], '#f2d39b', 'housing'),
    'housing_south': ([(40, 470), (400, 470), (400, 520), (540, 520), (540, 740), (40, 740)], '#f2d39b', 'housing'),
    'cbd': ([(410, 330), (550, 330), (550, 470), (410, 470)], '#c0392b', 'cbd'),
    'shops_north': ([(500, 90), (560, 90), (560, 320), (500, 320)], '#8e5ea2', 'shops'),
    'industry': ([(700, 260), (840, 260), (840, 640), (700, 640)], '#7f8c8d', 'industry'),
    'park': ([(560, 540), (690, 540), (690, 740), (560, 740)], '#6aa84f', 'park'),
}
KEY = [('#c0392b', 'CBD: offices, shops, services'), ('#f2d39b', 'housing'), ('#8e5ea2', 'shops'), ('#7f8c8d', 'industry'), ('#6aa84f', 'park / open space')]


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'Schematic land-use plan of a town (not a measured map)')
    fig.rect(20, 70, 960, 690, '#f7f5ee', GREY, 2, 6)
    for name, (pts, col, kind) in ZONES.items():
        fig.poly(pts, col, INK, 1.5)
    rnd = random.Random(5)
    placed = []
    for name in ('housing_west', 'housing_south'):
        poly = Polygon(ZONES[name][0])
        for _ in range(500):
            s = rnd.choice((10, 14, 20, 26))
            x, y = rnd.uniform(50, 530), rnd.uniform(100, 730)
            sq = Polygon([(x, y), (x + s, y), (x + s, y + s), (x, y + s)])
            if poly.contains(sq.buffer(6)) and abs(x + s / 2 - J[0]) > 30 and abs(y + s / 2 - J[1]) > 30 \
                    and not any(sq.buffer(5).intersects(o) for o in placed):
                placed.append(sq)
                fig.rect(x, y, s, s, '#ffffff', '#8a6d3b', 1.2)
    for x in range(420, 521, 30):
        for y in (345, 445):
            fig.rect(x, y, 22, 18, '#ffffff', INK, 1)
    for y in range(100, 316, 30):
        fig.rect(510, y, 40, 20, '#ffffff', INK, 1)
    for (x, y) in ((720, 290), (720, 400), (720, 510), (770, 340), (770, 460), (770, 570)):
        fig.rect(x, y, 50, 44, '#c9c9c9', INK, 1.2)
    for (x, y) in ((600, 600), (640, 660), (590, 690), (650, 580)):
        fig.circle(x, y, 12, '#3f7f45', 'none', 0)
    # roads: N-S and E-W main roads meet at the junction; freight railway on the east
    fig.line(J[0], 70, J[0], 760, '#555555', 12)
    fig.line(20, J[1], 980, J[1], '#555555', 12)
    fig.line(J[0], 70, J[0], 760, '#ffffff', 2, dash='14 10')
    fig.line(20, J[1], 980, J[1], '#ffffff', 2, dash='14 10')
    fig.line(870, 70, 870, 760, INK, 5)
    for y in range(80, 760, 22):
        fig.line(860, y, 880, y, INK, 2)
    fig.line(840, 450, 870, 450, INK, 3)
    fig.text(895, 120, 'freight', 26, 'start', 'bold', INK, halo=True)
    fig.text(895, 152, 'railway', 26, 'start', 'bold', INK, halo=True)
    fig.arrow(950, 260, 950, 190, INK, 4, 16)
    fig.text(950, 290, 'N', 28, 'middle', 'bold')
    # key
    ky = 800
    for i, (col, lab) in enumerate(KEY):
        x, y = [(30, ky), (470, ky), (690, ky), (30, ky + 40), (330, ky + 40)][i]
        fig.rect(x, y - 22, 30, 24, col, INK, 1.5)
        fig.text(x + 40, y, lab, 26)
    fig.line(690, ky + 31, 740, ky + 31, '#555555', 10)
    fig.text(750, ky + 40, 'main road', 26)

    A = 'a'
    labels = [('CBD', 480, 312, '1'), ('housing (west)', 200, 280, '2'), ('housing (south)', 230, 640, '2'),
              ('industry', 770, 250, '3'), ('shopping strip', 600, 210, '4'), ('park', 625, 530, '5')]
    for lab, x, y, n in labels:
        fig.text(x, y, lab, 26, 'middle', 'bold', INK, A, halo=True)
    fig.marker(560, 312, '1', A)
    fig.marker(690, 240, '3', A)
    fig.marker(640, 160, '4', A)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Interpretation', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for k, s in [('1', 'The CBD (offices, shops, services) sits at the central junction where the main roads meet.'),
                 ('2', 'Housing occupies the west and south; industry lies beside the eastern freight railway; a shopping strip lines the northern access road; the park is south-east.'),
                 ('3', 'Different functions occupy connected but separate locations. This is a schematic model, not a measured map of Windhoek, and it records no incomes.')]:
        fig.marker(52, yy - 9, k, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8

    zp = {n: Polygon(p) for n, (p, c, k) in ZONES.items()}
    spec = {'kind': 'schematic urban land-use plan (model, not a real town)', 'zones': {n: {'polygon': p, 'use': k} for n, (p, c, k) in ZONES.items()},
            'junction': J, 'railway_x': 870, 'notes_match': 'BL-6137-3.3.04-14',
            'reuses': {'ITEM-6137-3.3-016-INTERP': 'CBD', 'ITEM-6137-3.3-017-INTERP': 'housing', 'ITEM-6137-3.3-018-INTERP': 'industry',
                       'ITEM-6137-3.3-019-INTERP': 'shopping', 'ITEM-6137-3.3-020-INTERP': 'open space', 'ITEM-6137-3.3-021-INTERP': 'transport'},
            'question_withholds': ['zone names written on the map (key only)'],
            'independent_solution': ['functions in distinct connected locations (1)', 'industry by freight corridor; CBD at junction (1)',
                                     'schematic, not a measured Windhoek map or income evidence (1)']}
    checks = [check('CBD contains the central junction', zp['cbd'].contains(Point(J))),
              check('industry lies east of the junction and adjacent to the railway', zp['industry'].bounds[0] > J[0] and 870 - zp['industry'].bounds[2] <= 40),
              check('housing lies west and south', zp['housing_west'].centroid.x < J[0] and zp['housing_south'].centroid.y > J[1]),
              check('shopping strip north of the junction beside the N road', zp['shops_north'].bounds[3] < J[1] and abs(zp['shops_north'].bounds[0] - J[0]) <= 30),
              check('park south-east of the junction', zp['park'].centroid.x > J[0] and zp['park'].centroid.y > J[1]),
              check('zones do not overlap', all(zp[a].intersection(zp[b]).area < 1 for a in zp for b in zp if a < b))]
    sides = {'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q']},
             'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']}}
    return build(RID, fig, spec, sides, checks)


if __name__ == '__main__':
    main()
