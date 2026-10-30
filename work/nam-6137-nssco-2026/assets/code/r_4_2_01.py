"""VIS-6137-4.2-01 -> ITEM-6137-4.2-002-INTERP (assigned); recorded reuses 026 and P01.

Original 1:50,000 training map of an invented area (geometry in map42.py): title, full key, 1 km grid
with metre labels, grid-north arrow, contours at a 10 m interval (1,500-1,530 m) around a 1,540 m spot
height at B, spot height 1,500 m at A, roads A-D, D-C and the curved A-B road, a river in the northern
plain, cultivated fields, a school at D and a clinic at C. Scale statement, 0-2 km scale bar and a
physical-size note (1 cm = 500 m only when printed 20 cm wide).
Answer sides: 002 (what the title, key, scale and north arrow establish), 026 (mapped human-use
relationships) and P01 (the package's four parts). All three share the unannotated question image.
"""
import math
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, build, check  # noqa: E402
import map42 as M  # noqa: E402

RID = 'VIS-6137-4.2-01'
ITEM = 'ITEM-6137-4.2-002-INTERP'
W, HQ, HA = 1000, 960, 1350
OX, OY, EXT = 105, 90, 6000
RIVER = [(6000, 5450), (5200, 5250), (4300, 5420), (3400, 5200), (2500, 5380), (1600, 5180), (800, 5360), (0, 5200)]
FIELDS = [[(500, 4400), (1100, 4400), (1100, 4950), (500, 4950)], [(1150, 4400), (1700, 4400), (1700, 4950), (1150, 4950)],
          [(500, 3700), (1100, 3700), (1100, 4350), (500, 4350)]]
CONTOUR, ROAD, WATER, FIELD = '#a0522d', '#c0392b', '#2f6fae', '#cfe3a6'


def P(x, y):
    return M.to_px(x, y, 0, 0, OX, OY, EXT)


def school(fig, x, y, layer='base'):
    fig.rect(x - 13, y - 13, 26, 26, INK, '#ffffff', 2, layer=layer)
    fig.line(x, y - 13, x, y - 30, INK, 2.5, layer)
    fig.poly([(x, y - 30), (x + 14, y - 25), (x, y - 20)], INK, INK, 1, layer=layer)


def clinic(fig, x, y, layer='base'):
    fig.circle(x, y, 15, '#ffffff', INK, 2.5, layer)
    fig.rect(x - 3.5, y - 10, 7, 20, '#c0392b', 'none', 0, layer=layer)
    fig.rect(x - 10, y - 3.5, 20, 7, '#c0392b', 'none', 0, layer=layer)


def draw_map(fig):
    fig.rect(OX, OY, EXT * M.PX_PER_M, EXT * M.PX_PER_M, '#f8f6ee', INK, 2.5)
    for f in FIELDS:
        fig.poly([P(*p) for p in f], FIELD, '#6b8e23', 1.5)
    rv = [P(*p) for p in RIVER]
    fig.path('M' + ' '.join('%s%.1f %.1f' % ('L' if i else '', x, y) for i, (x, y) in enumerate(rv)), 'none', WATER, 5)
    for lv in M.LEVELS:
        pts = [P(*p) for p in M.contour(lv)]
        fig.poly(pts, 'none', CONTOUR, 3 if lv in (1500, 1520) else 1.8)
    for lv, th in ((1500, 120), (1520, 120)):
        # label where the ray at angle th (degrees) meets the contour
        c = M.contour(lv, 360)
        x, y = P(*c[th])
        fig.text(x, y + 9, str(lv), 26, 'middle', 'bold', CONTOUR, halo=True)
    for g in range(1000, EXT, 1000):
        fig.line(*P(g, 0), *P(g, EXT), '#9fb3c8', 1.2)
        fig.line(*P(0, g), *P(EXT, g), '#9fb3c8', 1.2)
    road, _, _ = M.road_ab()
    for seg in (road, [M.PTS['A'], M.PTS['D']], [M.PTS['D'], M.PTS['C']]):
        pts = [P(*p) for p in seg]
        fig.poly(pts, 'none', '#ffffff', 9, closed=False)
        fig.poly(pts, 'none', ROAD, 5, closed=False)
    school(fig, *P(*M.PTS['D']))
    clinic(fig, *P(*M.PTS['C']))
    for k, (dx, dy, anc) in {'A': (-12, 30, 'end'), 'B': (14, -14, 'start'), 'C': (22, -16, 'start'), 'D': (-22, -16, 'end')}.items():
        x, y = P(*M.PTS[k])
        if k in 'AB':
            fig.circle(x, y, 5, INK, INK, 1)
        fig.text(x + dx, y + dy, k, 30, anc, 'bold', INK, halo=True)
    for k, val in (('A', 1500), ('B', 1540)):
        x, y = P(*M.PTS[k])
        fig.text(x + (-12 if k == 'A' else 14), y + (-12 if k == 'A' else 30), str(val), 26, 'end' if k == 'A' else 'start', 'bold', INK, halo=True)
    for g in range(0, EXT + 1, 1000):
        x, y = P(g, 0)
        fig.text(x, y + 30, str(g), 26, 'middle')
        if g:
            x, y = P(0, g)
            fig.text(x - 8, y + 9, str(g), 26, 'end')
    fig.text(OX + 300, OY + 670, 'x: metres east', 26, 'middle', 'bold')
    fig.text(26, OY + 300, 'y: metres north', 26, 'middle', 'bold', rotate=-90)


def draw_key(fig):
    kx = 727
    fig.arrow(kx + 215, OY + 100, kx + 215, OY + 4, INK, 5, 22)
    fig.lines(kx + 215, OY + 130, ['Grid', 'north'], 26, 30, anchor='middle', weight='bold')
    fig.text(kx, OY + 26, 'Key', 30, 'start', 'bold')
    y = OY + 214
    items = [('contour', ['contour line,', 'interval 10 m']), ('spot', ['spot height (m)']), ('road', ['road']), ('river', ['river']),
             ('field', ['cultivation']), ('school', ['school']), ('clinic', ['clinic']), ('grid', ['1 km grid line'])]
    for kind, rows in items:
        cx = kx + 24
        if kind == 'contour':
            fig.line(kx, y - 9, kx + 48, y - 9, CONTOUR, 3)
        elif kind == 'spot':
            fig.circle(cx, y - 9, 5, INK, INK, 1)
        elif kind == 'road':
            fig.line(kx, y - 9, kx + 48, y - 9, ROAD, 5)
        elif kind == 'river':
            fig.line(kx, y - 9, kx + 48, y - 9, WATER, 5)
        elif kind == 'field':
            fig.rect(kx + 4, y - 24, 40, 30, FIELD, '#6b8e23', 1.5)
        elif kind == 'school':
            school(fig, cx, y - 2)
        elif kind == 'clinic':
            clinic(fig, cx, y - 9)
        elif kind == 'grid':
            fig.line(kx, y - 9, kx + 48, y - 9, '#9fb3c8', 2)
        fig.lines(kx + 62, y, rows, 26, 30)
        y += 30 * len(rows) + 15
    return y


def draw_scale(fig):
    y = OY + 720
    fig.text(OX, y, 'Scale 1:50,000', 28, 'start', 'bold')
    x0 = OX + 230
    for i in range(4):
        fig.rect(x0 + i * 50, y - 22, 50, 12, INK if i % 2 == 0 else '#ffffff', INK, 1.5)
    for km, lab in ((0, '0'), (1, '1'), (2, '2 km')):
        fig.text(x0 + km * 100, y + 18, lab, 26, 'middle')
    fig.para(OX, y + 62, 'At 1:50,000, 1 cm on the map = 500 m on the ground only when this image is printed 20 cm wide '
             '(grid squares 2 cm). At any other size, measure with the scale bar.', 26, 880, 32, fill=GREY)


def answer_panel(fig, layer, title, rows):
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, layer)
    fig.text(36, HQ + 46, title, 28, 'start', 'bold', C['answer'], layer)
    yy = HQ + 90
    for n, s in rows:
        fig.marker(52, yy - 9, n, layer)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=layer) + 8
    return yy


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA, 'answer_026': HA, 'answer_p01': HA},
              'Training map: an invented farming area (original, not a real place)')
    draw_map(fig)
    ky = draw_key(fig)
    draw_scale(fig)

    A = 'a'
    fig.marker(972, 38, '1', A)
    fig.marker(727 + 100, OY + 18, '2', A)
    fig.marker(OX + 520, OY + 690, '3', A)
    fig.marker(727 + 160, OY + 60, '3', A)
    answer_panel(fig, A, 'What each element establishes', [
        ('1', 'Title: the area and purpose, an invented training area, so no real-place facts can be read from it.'),
        ('2', 'Key: what each symbol and colour means, e.g. contours (10 m interval), roads, river, cultivation, school and clinic.'),
        ('3', 'Scale 1:50,000 and bar: ground distances (1 cm = 500 m at print size). Grid-north arrow: direction and bearings.'),
        ('4', 'None of these shows how reliable a service is, its opening hours or any fact not mapped.')])

    A26 = 'a026'
    xd, yd = P(*M.PTS['D'])
    xc, yc = P(*M.PTS['C'])
    fig.marker(xd - 40, yd + 40, '1', A26)
    fig.marker(xc + 40, yc + 40, '1', A26)
    fig.marker(*P(2000, 3000), '2', A26)
    fig.marker(*P(1100, 4675), '3', A26)
    answer_panel(fig, A26, 'Mapped human-use relationships', [
        ('1', 'The key identifies a school at D (education) and a clinic at C (healthcare).'),
        ('2', 'Roads join A to D and D to C, so the map shows a connection between these points.'),
        ('3', 'Cultivated fields are keyed separately, north-west of D near the river.'),
        ('4', 'The map does not show capacity, opening hours, or how often or cheaply any transport runs.')])

    AP = 'ap01'
    xa, ya = P(*M.PTS['A'])
    xb, yb = P(*M.PTS['B'])
    fig.line(xa, ya, xb, yb, C['answer'], 4, AP, dash='10 7')
    fig.text((xa + xb) / 2, ya - 14, '4 cm = 2 km', 26, 'middle', 'bold', C['answer'], AP, halo=True)
    fig.marker(xc + 40, yc + 40, 'a', AP)
    fig.marker((xa + xb) / 2, ya + 30, 'b', AP)
    fig.marker(*P(3000, 3000), 'c', AP)
    answer_panel(fig, AP, 'Package P01', [
        ('a', 'The clinic supplies healthcare.'),
        ('b', '4 cm × 500 m = 2,000 m = 2 km from A to B.'),
        ('c', 'E.g. B is east of A; D is north of A and C north of B; square ABCD is 2 km × 2 km = 4 km²; B is 40 m higher than A.'),
        ('d', 'Reject the claim: a road symbol shows a connection, not how often or how cheaply transport runs.')])

    road, amp, rlen = M.road_ab()
    hts = {k: M.height(*M.PTS[k]) for k in 'ABCD'}
    spec = {
        'kind': 'original 1:50,000 training map (generated terrain; not a real place, not traced)',
        'geometry_source': 'assets/code/map42.py (shared by VIS-6137-4.2-01 to -04)',
        'scale': '1:50,000 when the 1,000 px image is printed 20 cm wide (0.1 px per metre)', 'extent_m': [0, EXT, 0, EXT],
        'points_m': M.PTS, 'heights_m': {k: round(v, 3) for k, v in hts.items()},
        'terrain': {'base_m': M.BASE, 'summit_m_at_B': M.PEAK, 'sigma_m': {'west': round(M.SIG_W, 2), 'east': M.SIG_E, 'north': M.SIG_N, 'south': M.SIG_S},
                    'contours_m': M.LEVELS, 'interval_m': M.INTERVAL_M},
        'roads': {'A-D': 2000, 'D-C': 2000, 'A-B_curved_length_m': round(rlen, 3), 'A-B_curve_amplitude_m': round(amp, 1)},
        'key': ['contour (10 m)', 'spot height', 'road', 'river', 'cultivation', 'school (at D)', 'clinic (at C)', '1 km grid'],
        'reuses': {'ITEM-6137-4.2-026-INTERP': 'answer_026 side', 'ITEM-6137-4.2-P01': 'answer_p01 side (with VIS-6137-4.2-02)'},
        'question_withholds': ['interpretation of title/key/scale/north', 'service relationships', 'P01 answers'],
        'independent_solution_002': ['title identifies area/purpose (1)', 'key decodes symbols (1)', 'scale and north give distance/direction; no service facts (1)'],
    }
    checks = [
        check('h(A) = 1500 m and h(B) = 1540 m exactly', abs(hts['A'] - 1500) < 1e-6 and abs(hts['B'] - 1540) < 1e-9),
        check('every drawn contour lies inside the map frame', all(0 <= x <= EXT and 0 <= y <= EXT for lv in M.LEVELS for x, y in M.contour(lv))),
        check('contours are nested along every ray from B (each higher one inside the lower)',
              all(math.dist(ph, M.PTS['B']) < math.dist(pl, M.PTS['B']) for lo, hi in zip(M.LEVELS, M.LEVELS[1:]) for pl, ph in zip(M.contour(lo), M.contour(hi)))),
        check('A lies on the 1500 m contour', abs(hts['A'] - 1500) < 1e-6),
        check('curved A-B road is 3,000 m (6 cm) long; straight A-B 2,000 m (4 cm)', abs(rlen - 3000) < 0.01 and math.dist(M.PTS['A'], M.PTS['B']) == 2000),
        check('river and fields lie below 1,495 m (plain) and outside the 1,500 m contour', all(M.height(x, y) < 1495 for x, y in RIVER + [p for f in FIELDS for p in f])),
        check('1 km grid = 100 px = 2 cm at 50 px/cm', 1000 * M.PX_PER_M == 100),
        check('key lists every symbol drawn', ky < HQ),
    ]
    sides = {'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q']},
             'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']},
             'answer_026': {'path': 'assets/images/ITEM-6137-4.2-026-INTERP-%s-answer.png' % RID, 'layers': [A26], 'bound_item': 'ITEM-6137-4.2-026-INTERP'},
             'answer_p01': {'path': 'assets/images/ITEM-6137-4.2-P01-%s-answer.png' % RID, 'layers': [AP], 'bound_item': 'ITEM-6137-4.2-P01'}}
    return build(RID, fig, spec, sides, checks)


if __name__ == '__main__':
    main()
