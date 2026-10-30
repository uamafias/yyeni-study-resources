"""VIS-6137-1.5-04 -> ITEM-6137-1.5-033-INTERP: plan of a depositional coast with four sediment features.

Land lies south, sea north; net sediment drift is eastward along the shore. W: a sand strip along the
straight shore. X: a sand ridge attached to the shore at its western end, crossing part of an
estuary mouth, with a free curved tip (river keeps the gap open). Y: a ridge joining both sides of a
bay, with enclosed water behind. Z: a ridge joining an offshore island to the mainland.
Connections are checked from the polygon geometry (shapely).
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, build, check, smooth_closed  # noqa: E402
from shapely.geometry import Polygon  # noqa: E402

RID = 'VIS-6137-1.5-04'
ITEM = 'ITEM-6137-1.5-033-INTERP'
W, HQ, HA = 1000, 790, 1110
COAST = 470
LAND = '#dfe8c4'
LAGOON = '#9cc9e6'

LAND_POLY = [(22, COAST), (300, COAST), (310, 520), (330, 640), (360, 640), (410, 520), (430, COAST), (520, COAST),
             (540, 560), (610, 600), (680, 560), (700, COAST), (978, COAST), (978, 700), (22, 700)]
BEACH_W = smooth_closed([(36, COAST + 2), (60, COAST - 26), (180, COAST - 32), (292, COAST - 26), (300, COAST + 2), (180, COAST + 4)], 8)
SPIT_X = smooth_closed([(288, COAST - 28), (340, COAST - 34), (385, COAST - 30), (408, COAST - 14), (410, COAST + 14), (400, COAST + 18),
                        (394, COAST - 2), (372, COAST - 12), (330, COAST - 10), (292, COAST - 4)], 8)
BAR_Y = smooth_closed([(510, COAST + 4), (530, COAST - 18), (610, COAST - 26), (690, COAST - 18), (712, COAST + 4), (690, COAST + 8),
                       (610, COAST + 2), (530, COAST + 8)], 8)
LAGOON_Y = [(520, COAST + 6), (700, COAST + 6), (680, 560), (610, 598), (540, 560)]
ISLAND = smooth_closed([(800, 250), (860, 222), (920, 248), (932, 305), (885, 348), (815, 340), (792, 298)], 8)
TOMBOLO_Z = smooth_closed([(846, 330), (868, 332), (872, 400), (884, COAST + 4), (826, COAST + 4), (838, 400)], 8)


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'Plan of a depositional coast (not to scale)')
    fig.rect(20, 56, 960, 646, C['sea'], GREY, 2, 8)
    fig.poly(LAND_POLY, LAND, INK, 2)
    fig.poly(LAGOON_Y, LAGOON, INK, 1.5)
    fig.path('M345 640 C 350 680, 330 690, 345 700', 'none', C['water'], 8)
    fig.text(380, 668, 'river', 26, 'start', 'normal', C['blue'], halo=True)
    for poly in (BEACH_W, SPIT_X, BAR_Y, TOMBOLO_Z):
        fig.poly(poly, C['sand'], INK, 2)
    fig.poly(ISLAND, LAND, INK, 2)
    fig.text(860, 295, 'island', 26, 'middle', 'bold', INK, halo=True)
    fig.text(120, 640, 'LAND', 30, 'middle', 'bold', C['green'])
    fig.text(120, 150, 'SEA', 30, 'middle', 'bold', C['blue'])
    for lab, (x, y) in (('W', (165, COAST - 50)), ('X', (370, COAST - 58)), ('Y', (610, COAST - 42)), ('Z', (800, 446))):
        fig.text(x, y, lab, 32, 'middle', 'bold', INK, halo=True)
    fig.arrow(200, 330, 520, 330, C['blue'], 6, 22)
    fig.text(360, 310, 'net drift along the coast', 26, 'middle', 'bold', C['blue'], halo=True)
    fig.arrow(940, 180, 940, 100, INK, 4, 16)
    fig.text(940, 208, 'N', 28, 'middle', 'bold')
    ky = HQ - 50
    for i, (col, lab) in enumerate([(C['sand'], 'sand and shingle'), (LAND, 'land'), (C['sea'], 'sea'), (LAGOON, 'enclosed water')]):
        fig.rect(40 + [0, 290, 450, 610][i], ky - 22, 30, 24, col, INK, 1.5)
        fig.text(80 + [0, 290, 450, 610][i], ky, lab, 26)
    fig.text(40, ky + 40, 'All four ridges are built of loose sand and shingle.', 26)

    A = 'a'
    fig.text(165, COAST - 82, 'beach', 26, 'middle', 'bold', C['answer'], A, halo=True)
    fig.text(370, COAST - 90, 'spit', 26, 'middle', 'bold', C['answer'], A, halo=True)
    fig.text(610, COAST - 74, 'bay-mouth bar', 26, 'middle', 'bold', C['answer'], A, halo=True)
    fig.text(610, 545, 'lagoon', 26, 'middle', 'bold', C['answer'], A, halo=True)
    fig.text(830, 400, 'tombolo', 26, 'end', 'bold', C['answer'], A, halo=True)
    fig.marker(250, COAST - 82, '1', A)
    fig.marker(495, COAST - 82, '2', A)
    fig.marker(912, 420, '3', A)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Interpretation', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for n, s in [('1', 'W lies along the shore: a beach. X is attached only at its western end and projects with a free, curved tip: a spit, consistent with the eastward drift.'),
                 ('2', 'Y joins both sides of the bay and encloses water behind it: a bay-mouth bar with a lagoon.'),
                 ('3', 'Z links the island to the mainland: a tombolo.')]:
        fig.marker(52, yy - 9, n, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8

    land, isl = Polygon(LAND_POLY), Polygon(ISLAND)
    spit, bar, tomb = Polygon(SPIT_X), Polygon(BAR_Y), Polygon(TOMBOLO_Z)
    east_shore = Polygon([(410, 520), (430, COAST), (520, COAST), (520, 700), (410, 700)])
    spec = {
        'kind': 'plan view of a coast (schematic), north at top',
        'features': {'W': 'beach along the straight shore', 'X': 'ridge attached at the west end, free curved tip across part of an estuary mouth',
                     'Y': 'ridge joining both sides of a bay, enclosed water behind', 'Z': 'ridge joining an island to the mainland'},
        'drift': 'eastward along the shore', 'polygons': {'land': LAND_POLY, 'W': BEACH_W, 'X': SPIT_X, 'Y': BAR_Y, 'lagoon': LAGOON_Y,
                                                           'island': ISLAND, 'Z': TOMBOLO_Z},
        'question_withholds': ['beach', 'spit', 'bar', 'tombolo', 'lagoon'],
        'independent_solution': ['W along shore = beach vs X attached at one end with free tip = spit (1)', 'Y closing the bay = bay-mouth bar (1)',
                                 'Z island-mainland connection = tombolo (1)'],
    }
    checks = [
        check('X joins the shore (via beach W) at its western end only (free tip does not reach the east shore)',
              spit.distance(land.union(Polygon(BEACH_W))) < 1 and spit.distance(east_shore) > 5, 'gap to east shore %.1f px' % spit.distance(east_shore)),
        check('Y touches both sides of the bay', bar.distance(Polygon([(500, COAST), (520, COAST), (520, 700), (500, 700)])) < 1
              and bar.distance(Polygon([(700, COAST), (720, COAST), (720, 700), (700, 700)])) < 1),
        check('Z touches both the island and the mainland', tomb.distance(isl) < 2 and tomb.distance(land) < 2),
        check('island is separate from the mainland except through Z', isl.distance(land) > 50),
    ]
    sides = {
        'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'],
                     'forbidden': [r'beach', r'spit', r'\bbar\b', r'tombolo', r'lagoon']},
        'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']},
    }
    return build(RID, fig, spec, sides, checks)


if __name__ == '__main__':
    main()
