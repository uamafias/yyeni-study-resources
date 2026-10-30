"""VIS-6137-1.1-01 -> ITEM-6137-1.1-012-INTERP: ocean-continent subduction cross-section (not to scale).

Geometry (master units = CSS px, 1000 wide). Ocean on the left, continent on the right.
The slab's upper surface is one function y_top(x); the overriding plate's base, the trench floor,
the mantle wedge and the melt zone are all derived from it, so the arrangement cannot drift apart.
"""
import math
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, build, check  # noqa: E402

RID = 'VIS-6137-1.1-01'
ITEM = 'ITEM-6137-1.1-012-INTERP'
W, HQ, HA = 1000, 700, 1150
Y0 = 40                 # vertical offset below the title
SEA = 170 + Y0          # sea level
FLOOR = 250 + Y0        # abyssal sea floor
BEND_X, BEND_L = 330, 260   # bend starts at BEND_X and straightens after BEND_L px
TRENCH_X = 470          # trench axis: where the overriding plate's front meets the slab top
DIP = 0.75              # tan(dip) of the straight slab section: about 37 degrees
THICK = 62              # oceanic lithosphere thickness (measured normal to the slab)
CONT_BASE = 370 + Y0    # base of the continental lithosphere
LAND = 150 + Y0         # general land surface


def y_top(x):
    """Upper surface of the oceanic plate: flat abyssal floor, then a bend whose slope increases
    steadily (quadratic) through the trench until it reaches the straight dip DIP."""
    if x <= BEND_X:
        return FLOOR
    a = DIP / (2 * BEND_L)
    if x <= BEND_X + BEND_L:
        return FLOOR + a * (x - BEND_X) ** 2
    return FLOOR + a * BEND_L ** 2 + DIP * (x - BEND_X - BEND_L)


def slope(x, h=0.5):
    return (y_top(x + h) - y_top(x - h)) / (2 * h)


def bottom_pt(x):
    """Point on the slab base: vertical offset THICK*sec(dip), so the normal thickness stays THICK
    without the loops a normal offset makes on the inside of a bend."""
    return (x, y_top(x) + THICK * math.hypot(1, slope(x)))


def x_at_depth(y):
    lo, hi = BEND_X, 2000
    for _ in range(60):
        mid = (lo + hi) / 2
        if y_top(mid) < y:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def main():
    TRENCH_Y = y_top(TRENCH_X)
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'Cross-section across a plate margin (not to scale)')
    xs_end = x_at_depth(HQ - 20)                   # slab leaves the drawn panel near the bottom edge
    top = [(x, y_top(x)) for x in range(0, int(xs_end) + 1, 4)]
    bot = [bottom_pt(x) for x in range(0, int(xs_end) + 1, 4)]
    bot = [p for p in bot if p[0] >= 0]
    x_meet = x_at_depth(CONT_BASE)                 # slab top reaches the continental base here

    # mantle background and the panel frame
    fig.rect(0, SEA - 120, W, HQ - (SEA - 120), C['mantle'], 'none', 0)
    # ocean water above sea floor up to sea level
    coast_x = 585
    ocean = [(0, SEA)] + [(coast_x, SEA)]
    cont_front = [(TRENCH_X + 8, y_top(TRENCH_X + 8)), (520, 255 + Y0), (560, 205 + Y0), (coast_x, SEA)]
    water = [(0, SEA), (coast_x, SEA)] + cont_front[::-1] + [(x, y_top(x)) for x in range(TRENCH_X + 8, -1, -4)]
    fig.rect(0, Y0 + 50, W, SEA - Y0 - 50, '#ffffff', 'none', 0)
    fig.poly(water, C['sea'], 'none', 0)
    # oceanic plate (lithosphere) with a thin crust band on top
    slab = top + bot[::-1]
    fig.defs.append('<clipPath id="panel"><rect x="0" y="0" width="%d" height="%d"/></clipPath>' % (W, HQ))
    fig.poly(slab, C['oc_lith'], INK, 2, extra='clip-path="url(#panel)"')
    crust = [(x, y_top(x)) for x in range(0, int(xs_end) + 1, 4)]
    crust_b = []
    for x in range(0, int(xs_end) + 1, 4):
        crust_b.append((x, y_top(x) + 12 * math.hypot(1, slope(x))))
    fig.poly(crust + crust_b[::-1], C['ocean_crust'], 'none', 0, extra='clip-path="url(#panel)"')
    # continental plate: front wall, coast, land surface, base along slab top then horizontal
    land = [(coast_x, SEA), (640, LAND + 8), (W, LAND)]
    under = [(x, y_top(x)) for x in range(int(x_meet), TRENCH_X + 7, -4)]
    cont = cont_front + land[1:] + [(W, CONT_BASE), (x_meet, CONT_BASE)] + under
    fig.poly(cont, C['cont_lith'], INK, 2)
    cont_crust = cont_front + land[1:] + [(W, LAND + 70), (700, LAND + 72), (600, 250 + Y0), (540, 275 + Y0)]
    fig.poly(cont_crust, C['cont_crust'], 'none', 0)
    fig.poly(cont_front + land[1:], 'none', INK, 2.5, closed=False)
    # sea level line
    fig.line(0, SEA, coast_x, SEA, C['blue'], 2.5)
    fig.text(14, SEA - 10, 'Sea level', 26, 'start', 'normal', C['blue'])
    fig.text(200, SEA + 48, 'Ocean', 28, 'middle', 'normal', C['blue'], italic=True)

    # volcanoes on the overriding plate
    vx = [735, 820]
    for x in vx:
        base_y = LAND
        fig.poly([(x - 48, base_y + 2), (x - 9, base_y - 62), (x + 9, base_y - 62), (x + 48, base_y + 2)],
                 '#8c6a4f', INK, 2)
        fig.poly([(x - 9, base_y - 62), (x, base_y - 54), (x + 9, base_y - 62)], C['magma'], 'none', 0)

    # labels shown on both sides
    fig.text(200, FLOOR + 42, 'Plate P: oceanic lithosphere', 26, 'middle', 'bold', '#ffffff')
    fig.lines(915, CONT_BASE - 76, ['Plate Q:', 'continental', 'lithosphere'], 26, 30, anchor='middle', weight='bold')
    fig.line(TRENCH_X, TRENCH_Y - 4, 425, SEA + 24, INK, 1.5)
    fig.text(425, SEA + 18, 'Trench', 26, 'middle', 'bold', INK, halo=True)
    fig.text(778, LAND - 80, 'Volcanoes', 26, 'middle', 'bold', INK, halo=True)
    fig.text(170, 610 + Y0, 'Mantle (asthenosphere)', 26, 'middle', 'bold', '#7a4a2a')

    # plate-motion arrows (inside each plate, pointing towards the margin)
    fig.arrow(60, FLOOR + 92, 250, FLOOR + 92, INK, 6, 24)
    fig.arrow(965, LAND + 112, 815, LAND + 112, INK, 6, 24)

    # key
    ky = HQ - 66
    fig.rect(530, ky - 28, 458, 84, '#ffffff', GREY, 1.5, 6)
    fig.arrow(546, ky, 616, ky, INK, 5, 18)
    fig.text(628, ky + 9, 'direction of plate movement', 26)
    fig.poly([(560, ky + 42), (580, ky + 18), (600, ky + 42)], '#8c6a4f', INK, 1.5)
    fig.text(628, ky + 42, 'volcano', 26)

    # ---- answer layer ---------------------------------------------------------------------------
    A = 'a'
    # melt zone in the mantle wedge above the slab, and magma routes to the volcanoes
    mx = x_at_depth(CONT_BASE + 70)
    sl = slope(mx)
    nx, ny = sl / math.hypot(1, sl), -1 / math.hypot(1, sl)       # upward unit normal of the slab top
    RX, RY = 52, 18
    mcx, mcy = mx + nx * (RY + 10), y_top(mx) + ny * (RY + 10)     # melt zone sits just above the slab
    ang = math.degrees(math.atan(sl))
    fig.add('<ellipse cx="%s" cy="%s" rx="%s" ry="%s" transform="rotate(%s %s %s)" fill="#e8a090" fill-opacity="0.9" '
            'stroke="%s" stroke-width="2"/>' % (mcx, mcy, RX, RY, ang, mcx, mcy, C['magma']), A)
    for x in vx:
        fig.path('M%s %s C %s %s, %s %s, %s %s' % (mcx, mcy - 8, mcx - 6, CONT_BASE - 40, x, LAND + 60, x, LAND - 56),
                 'none', C['magma'], 4, A, extra='stroke-dasharray="10 6"')
    # water released from the slab top rises a short way into the wedge below the melt zone
    for x in (mx + 45, mx + 80, mx + 115):
        fig.arrow(x, y_top(x) - 3, x - 8, y_top(x) - 30, C['blue'], 2.5, 10, A, halo=False)
    # earthquake foci along the interface and within the slab
    for x in (500, 545, 595, 645, 695, 785, 835):
        y = y_top(x) + 14
        fig.add('<path d="M%s %s l6 -10 l6 10 l-6 10 z" fill="#ffd23f" stroke="%s" stroke-width="1.5"/>'
                % (x - 6, y, INK), A)
    # numbered markers matching the three mark points
    fig.marker(300, FLOOR + 92, '1')
    fig.marker(890, LAND + 68, '1')
    fig.marker(TRENCH_X + 6, TRENCH_Y + 38, '2')
    fig.marker(740, y_top(740) + 31 * math.hypot(1, slope(740)), '2')
    fig.marker(735 - 70, LAND - 40, '3')
    fig.text(mcx + 64, mcy - 24, 'melting', 26, 'start', 'bold', C['magma'], A, halo=True)

    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Interpretation', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for n, s in [('1', 'The arrows point towards each other: the plates converge.'),
                 ('2', 'At the trench the oceanic slab bends down and descends beneath the overriding continental plate into the mantle.'),
                 ('3', 'The volcanoes lie on the overriding plate, inland from the trench.')]:
        fig.marker(52, yy - 9, n, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8
    yy += 6
    yy = fig.para(36, yy, 'Why there: water released from the descending slab lowers the melting temperature of the '
                  'mantle above it, and some of that magma rises to the volcanoes. The slab does not simply melt by friction.',
                  26, 920, 32, layer=A) + 14
    fig.add('<path d="M%s %s l7 -12 l7 12 l-7 12 z" fill="#ffd23f" stroke="%s" stroke-width="1.5"/>' % (36, yy - 9, INK), A)
    fig.text(62, yy, 'earthquake focus (plate interface and descending slab)', 26, layer=A)
    yy += 38
    fig.arrow(43, yy + 4, 43, yy - 22, C['blue'], 2.5, 10, A, halo=False)
    fig.text(62, yy, 'water released from the slab', 26, layer=A)
    fig.add('<path d="M%s %s h44" stroke="%s" stroke-width="4" stroke-dasharray="10 6"/>' % (480, yy - 9, C['magma']), A)
    fig.text(536, yy, 'rising magma', 26, layer=A)

    spec = {
        'kind': 'process cross-section (schematic, not to scale)',
        'teaching_target': 'Ocean-continent convergence with subduction: converging arrows, slab descending from the trench, volcanoes on the overriding plate inland from the trench.',
        'viewing_direction': 'vertical cross-section; left = ocean, right = continent',
        'geometry': {
            'canvas_px': [W, HQ, HA], 'sea_level_y': SEA, 'abyssal_floor_y': FLOOR,
            'trench_axis': [TRENCH_X, round(TRENCH_Y, 1)], 'bend_start_x': BEND_X, 'slab_dip_straight_section_deg': round(math.degrees(math.atan(DIP)), 1),
            'slab_thickness_px': THICK, 'continental_base_y': CONT_BASE,
            'slab_top_meets_continental_base_x': round(x_meet, 1), 'volcano_x': vx,
            'slab_top_y_below_volcanoes': [round(y_top(x), 1) for x in vx], 'melt_zone_centre': [round(mcx, 1), round(mcy, 1)],
        },
        'question_shows': ['two plate-motion arrows pointing towards each other', 'oceanic plate P bending down at a labelled trench',
                           'continental plate Q above the descending slab', 'two volcanoes on plate Q inland from the trench', 'key'],
        'question_withholds': ['margin type name', 'the words converge/subduct/descend', 'melt zone and magma route', 'earthquake foci'],
        'independent_solution': ['converging arrows -> convergence (1)', 'slab bends at trench and descends beneath plate Q (1)',
                                 'volcanoes on overriding plate Q, displaced inland from trench (1)'],
        'assumptions': ['Not to scale; vertical exaggeration of surface relief.',
                        'Melting shown in the mantle wedge above the slab (water-assisted), not friction melting of the whole slab.'],
    }
    vt = [y_top(x) for x in vx]
    checks = [
        check('arrows converge', 70 < 250 and 960 > 820 and 250 < 820, 'P arrow points +x, Q arrow points -x, P left of Q'),
        check('slab descends monotonically beyond trench', all(y_top(x + 4) > y_top(x) for x in range(TRENCH_X, int(xs_end), 4))),
        check('slab dip never decreases (single bend, no kink)', all(slope(x + 4) >= slope(x) - 1e-9 for x in range(0, int(xs_end), 4))),
        check('trench is the deepest point of the sea floor', all(y_top(x) <= TRENCH_Y for x in range(0, TRENCH_X + 1)) and TRENCH_Y > FLOOR and all(y >= SEA for y in (TRENCH_Y,))),
        check('volcanoes on overriding side, inland from trench', all(x > coast_x > TRENCH_X for x in vx)),
        check('slab lies below the overriding plate under the volcanoes', all(v > CONT_BASE for v in vt), str([round(v) for v in vt])),
        check('melt zone (rotated ellipse) wholly above slab top and below continental base',
              all(CONT_BASE < mcy + RX * math.sin(math.radians(ang)) * k + RY * math.cos(math.radians(ang)) * j < y_top(mcx + RX * math.cos(math.radians(ang)) * k - RY * math.sin(math.radians(ang)) * j)
                  for k in (-1, 0, 1) for j in (-1, 1))),
    ]
    sides = {
        'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'],
                     'forbidden': [r'destruct', r'subduct', r'converg', r'descend', r'melt', r'magma']},
        'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']},
    }
    return build(RID, fig, spec, sides, checks)


if __name__ == '__main__':
    main()
