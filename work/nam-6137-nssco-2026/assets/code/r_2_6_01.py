"""VIS-6137-2.6-01 -> ITEM-6137-2.6-011-INTERP: schematic habitat change, earlier and later plans.

Earlier: one connected block of tree cover. Later: the same outline with a cleared corridor through it,
leaving two separate patches. No animal counts are shown (stated). Areas are computed with shapely
for the spec, but no area figure is printed, as the card needs none.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, build, check, smooth_closed  # noqa: E402
from shapely.geometry import Polygon  # noqa: E402

RID = 'VIS-6137-2.6-01'
ITEM = 'ITEM-6137-2.6-011-INTERP'
W, HQ, HA = 1000, 600, 960
TREE = '#3f7f45'
BLOCK = [(40, 80), (120, 40), (260, 50), (380, 70), (430, 160), (400, 280), (300, 330), (160, 320), (60, 270), (30, 170)]
CORRIDOR = [(200, 0), (260, 0), (270, 400), (210, 400)]


def panel(fig, x0, title):
    fig.rect(x0, 70, 470, 420, '#f1ead8', GREY, 2, 8)
    fig.text(x0 + 16, 106, title, 28, 'start', 'bold')


def path(geom, ox, oy):
    polys = [geom] if geom.geom_type == 'Polygon' else list(geom.geoms)
    return ' '.join('M' + ' L'.join('%.1f %.1f' % (x + ox, y + oy) for x, y in p.exterior.coords) + ' Z' for p in polys)


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'Tree cover in one area: earlier and later (schematic plan)')
    blk = Polygon(smooth_closed(BLOCK, 8))
    later = blk.difference(Polygon(CORRIDOR))
    for x0, title, geom in ((20, 'Earlier', blk), (510, 'Later', later)):
        panel(fig, x0, title)
        fig.path(path(geom, x0 + 10, 130), TREE, INK, 2)
    fig.rect(510 + 10 + 200, 130 + 30, 70, 330, 'none', 'none', 0)
    fig.text(510 + 245, 470, 'cleared corridor', 26, 'middle', 'bold', INK, halo=True)
    fig.rect(40, 518, 30, 24, TREE, INK, 1.5)
    fig.text(80, 538, 'tree cover', 26)
    fig.rect(300, 518, 30, 24, '#f1ead8', INK, 1.5)
    fig.text(340, 538, 'open or cleared ground', 26)
    fig.text(W / 2, 584, 'No animal counts or species records are shown.', 26, 'middle', 'normal', GREY)

    A = 'a'
    for (sx, sy, ex, ey) in ((130, 300, 400, 260),):
        fig.arrow(20 + 10 + sx, 130 + sy - 100, 20 + 10 + ex, 130 + ey - 100, C['answer'], 4, 16, A)
    fig.text(245, 460, 'one connected block', 26, 'middle', 'bold', C['answer'], A, halo=True)
    fig.line(510 + 10 + 150, 300, 510 + 10 + 320, 300, C['red'], 4, A, dash='10 7')
    fig.text(510 + 245, 290, '✖', 30, 'middle', 'bold', C['red'], A, halo=True)
    fig.text(510 + 120, 260, 'patch 1', 26, 'middle', 'bold', '#ffffff', A)
    fig.text(510 + 360, 260, 'patch 2', 26, 'middle', 'bold', '#ffffff', A)
    fig.marker(510 + 60, 430, '1', A)
    fig.marker(510 + 245, 330, '2', A)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Interpretation', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for n, s in [('1', 'The tree cover is reduced and fragmented: one connected block becomes two separate patches.'),
                 ('2', 'The cleared corridor interrupts the earlier connection, so movement or access to resources may be constrained for species that need tree cover.'),
                 ('3', 'With no counts or species-use records, it cannot show an exact animal-population loss.')]:
        fig.marker(52, yy - 9, n, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8

    spec = {'kind': 'two-panel schematic plan (earlier/later)', 'block_area_px2': round(blk.area), 'later_area_px2': round(later.area),
            'later_patches': len(later.geoms) if later.geom_type == 'MultiPolygon' else 1, 'stated_limits': ['no animal counts or species records'],
            'question_withholds': ['fragment', 'population', 'loss'],
            'independent_solution': ['one block becomes two patches: fragmentation (1)', 'corridor breaks the connection (1)',
                                     'possible movement/resource constraint, not a measured population loss (1)']}
    checks = [check('later habitat splits into exactly two patches', later.geom_type == 'MultiPolygon' and len(later.geoms) == 2),
              check('later area smaller than earlier', later.area < blk.area, '%d vs %d px2' % (later.area, blk.area)),
              check('no animal numbers drawn', True)]
    sides = {'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'], 'forbidden': [r'fragment', r'population', r'\bloss']},
             'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']}}
    return build(RID, fig, spec, sides, checks, panels=[(20, 70, 470, 420), (510, 70, 470, 420)])


if __name__ == '__main__':
    main()
