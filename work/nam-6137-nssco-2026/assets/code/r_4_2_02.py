"""VIS-6137-4.2-02 -> ITEM-6137-4.2-008-INTERP (assigned); recorded reuses 007, 009-014 and P01.

Measurement panel of the same training world (map42.py) at 1:50,000: a window x 1,500-5,000 m,
y 500-4,500 m with contours, the straight A-B line (4 cm = 2 km), the curved A-B road (6 cm = 3 km, solved
length), square ABCD (side 4 cm), a 1 cm reference square, spot heights A 1,500 m and B 1,540 m, a 0-3 km
(6 cm) scale bar, grid north and a physical-size note. Right: the given measurements and a section along
the straight A-B line computed from the same terrain (vertical scale exaggerated).
Answer (008 and reuses 007, 009-013, P01): straight 2 km, road 3 km, square 4 km2, 1 cm square 0.25 km2,
gradient 40:2,000 = 1:50 (average; the section varies). Reuse 014 has its own answer side comparing
1:20 (40 m over 800 m) with 1:50 (40 m over 2,000 m) drawn to one scale.
"""
import math
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, Axes, build, check  # noqa: E402
import map42 as M  # noqa: E402

RID = 'VIS-6137-4.2-02'
ITEM = 'ITEM-6137-4.2-008-INTERP'
W, HQ, HA = 1000, 790, 1170
OX, OY = 95, 90
X0, X1, Y0, Y1 = 1500, 5000, 500, 4500
CONTOUR, ROAD = '#a0522d', '#c0392b'
REF_PX = (556, 285)             # top-left of the 1 cm (50 px) reference square, drawn in the record box


def P(x, y):
    return M.to_px(x, y, X0, Y0, OX, OY, Y1 - Y0)


def clipped(pts):
    return [p for p in pts if X0 <= p[0] <= X1 and Y0 <= p[1] <= Y1]


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA, 'answer_014': HA}, 'Measuring distance, area and gradient (1:50,000)')
    mw, mh = (X1 - X0) * M.PX_PER_M, (Y1 - Y0) * M.PX_PER_M
    fig.rect(OX, OY, mw, mh, '#f8f6ee', INK, 2.5)
    fig.add('<clipPath id="mapclip"><rect x="%d" y="%d" width="%d" height="%d"/></clipPath>' % (OX, OY, mw, mh))
    for lv in M.LEVELS:
        pts = [P(*p) for p in M.contour(lv)]
        d = 'M' + ' L'.join('%.1f %.1f' % p for p in pts) + ' Z'
        fig.path(d, 'none', CONTOUR, 2.4 if lv in (1500, 1520) else 1.5, extra='clip-path="url(#mapclip)"')
    for g in range(2000, X1, 1000):
        fig.line(*P(g, Y0), *P(g, Y1), '#9fb3c8', 1.2)
        fig.text(P(g, Y0)[0], OY + mh + 30, str(g), 26, 'middle')
    for g in range(1000, Y1, 1000):
        fig.line(*P(X0, g), *P(X1, g), '#9fb3c8', 1.2)
        fig.text(OX - 8, P(X0, g)[1] + 9, str(g), 26, 'end')
    sq = [P(*M.PTS[k]) for k in 'ABCD']
    fig.poly(sq, 'none', '#555555', 2.5, extra='stroke-dasharray="4 6"')
    road, amp, rlen = M.road_ab()
    for seg in (road, [M.PTS['A'], M.PTS['D']], [M.PTS['D'], M.PTS['C']]):
        pts = [P(*p) for p in seg]
        fig.poly(pts, 'none', '#ffffff', 9, closed=False)
        fig.poly(pts, 'none', ROAD, 5, closed=False)
    xa, ya = P(*M.PTS['A'])
    xb, yb = P(*M.PTS['B'])
    fig.line(xa, ya, xb, yb, INK, 3, dash='10 7')
    for k, (dx, dy, anc) in {'A': (-12, 32, 'end'), 'B': (12, 32, 'start'), 'C': (14, -14, 'start'), 'D': (-14, -14, 'end')}.items():
        x, y = P(*M.PTS[k])
        fig.circle(x, y, 5, INK, INK, 1)
        fig.text(x + dx, y + dy, k, 30, anc, 'bold', INK, halo=True)
    fig.text(xa + 10, ya - 14, '1500', 26, 'start', 'bold', INK, halo=True)
    fig.text(xb + 12, yb - 12, '1540', 26, 'start', 'bold', INK, halo=True)
    fig.arrow(OX + mw + 32, OY + 90, OX + mw + 32, OY + 10, INK, 4, 18)
    fig.text(OX + mw + 32, OY + 118, 'N', 26, 'middle', 'bold')
    # scale bar 0-3 km = 6 cm = 300 px
    sy = OY + mh + 92
    fig.text(OX, sy, 'Scale 1:50,000', 26, 'start', 'bold')
    bx0 = OX + 200
    for i in range(6):
        fig.rect(bx0 + i * 50, sy - 22, 50, 12, INK if i % 2 == 0 else '#ffffff', INK, 1.5)
    for km in range(4):
        fig.text(bx0 + km * 100, sy + 18, str(km) + (' km' if km == 3 else ''), 26, 'middle')
    fig.para(OX, sy + 112, '1 cm = 500 m only when this image is printed 20 cm wide; otherwise measure with the scale bar. Contour interval 10 m. Square ABCD: A–B dashed, B–C dotted, C–D and D–A along roads.',
             26, 880, 32, fill=GREY)
    # given measurements and section
    rx0 = 540
    fig.rect(rx0, OY, 440, 270, '#eef3f7', INK, 1.5, 6)
    rx, ry = REF_PX
    fig.rect(rx, ry, 50, 50, '#ffffff', INK, 2)
    fig.text(rx + 64, ry + 34, '1 cm square', 26)
    fig.lines(rx0 + 16, OY + 72, ['straight A–B: 4 cm', 'road A–B: 6 cm', 'square side AB: 4 cm', 'spot heights: A 1,500 m, B 1,540 m'], 26, 36)
    fig.text(rx0 + 16, OY + 36, 'Measured on the map:', 26, 'start', 'bold')
    ax = Axes(fig, 710, 440, 260, 140, (0, 2000), (1490, 1550))
    ax.draw([0, 1000, 2000], [1500, 1520, 1540], 'Distance from A (m)', 'Height (m)', ylabel_x=618, minor_y=[1510, 1530])
    prof = [(d, M.height(2000 + d, 2000)) for d in range(0, 2001, 25)]
    ax.polyline(prof, '#6b4f2a', 4)
    fig.lines(820, 392, ['Section A–B', '(vertical scale exaggerated)'], 26, 30, anchor='middle', weight='bold')

    A = 'a'
    fig.text((xa + xb) / 2 + 20, ya + 34, '2 km', 26, 'middle', 'bold', C['answer'], A, halo=True)
    rmid = P(*road[len(road) // 2])
    fig.text(rmid[0], rmid[1] + 32, 'road 3 km', 26, 'middle', 'bold', C['answer'], A, halo=True)
    fig.text(*P(3000, 3350), '4 km²', 28, 'middle', 'bold', C['answer'], A, halo=True)
    fig.text(970, ry + 34, '= 0.25 km²', 26, 'end', 'bold', C['answer'], A)
    fig.line(ax.X(2000) - 8, ax.Y(1500), ax.X(2000) - 8, ax.Y(1540), C['answer'], 3, A)
    fig.text(ax.X(2000) - 16, ax.Y(1520) + 9, 'rise 40 m', 26, 'end', 'bold', C['answer'], A, halo=True)
    rows = [('1', 'Straight A–B: 4 cm × 500 m = 2 km. Road: 6 cm × 500 m = 3 km, longer because it follows a different path; travel time and frequency are not shown.'),
            ('2', 'Square ABCD: 2 km × 2 km = 4 km². A 1 cm square: 0.5 km × 0.5 km = 0.25 km² (both sides convert).'),
            ('3', 'Gradient A→B: rise 40 m over 2,000 m = 40:2,000 = 1:50, an average; the section shows the slope is not uniform.')]
    panel(fig, A, 'Measurements', rows)

    A14 = 'a014'
    rows14 = [('1', '1:20 is steeper: the same 40 m rise happens over 800 m instead of 2,000 m.'),
              ('2', 'Each ratio is an average between two points; it does not show the slope at every point or which line is higher up.')]
    yy = panel(fig, A14, 'Average gradients (same scales for both; vertical exaggerated)', rows14)
    hs, vs = 0.2, 1.5                         # px per m horizontally; vertical exaggeration for the triangles
    for i, (run, lab) in enumerate(((800, '1:20  (40 m in 800 m)'), (2000, '1:50  (40 m in 2,000 m)'))):
        tx, ty = 90 + i * 330, yy + 80
        fig.poly([(tx, ty), (tx + run * hs, ty), (tx + run * hs, ty - 40 * vs)], '#dfe9f3' if i else '#f6d5c9', INK, 2, layer=A14)
        fig.text(tx, ty + 34, lab, 26, 'start', 'bold', layer=A14)

    sq_side = math.dist(M.PTS['A'], M.PTS['B'])
    spec = {
        'kind': 'measurement panel of the 4.2 training world at 1:50,000, with a terrain section',
        'geometry_source': 'assets/code/map42.py', 'window_m': {'x': [X0, X1], 'y': [Y0, Y1]},
        'measurements_cm': {'straight_AB': sq_side / 500, 'road_AB': rlen / 500, 'square_side': sq_side / 500, 'ref_square_side': 1, 'ref_square_px': 50},
        'ground': {'straight_AB_m': sq_side, 'road_AB_m': round(rlen, 3), 'square_area_km2': (sq_side / 1000) ** 2, 'ref_square_km2': 0.25,
                   'rise_AB_m': M.height(*M.PTS['B']) - M.height(*M.PTS['A']), 'gradient': '1:%g' % (2000 / 40)},
        'section': 'h(x, 2000) for x in 2000..4000 from the shared terrain; vertical exaggeration about 14x',
        'reuses': {'ITEM-6137-4.2-007-CALC': 'scale bar 6 cm = 3 km; answer side', 'ITEM-6137-4.2-009-CALC': 'straight A-B',
                   'ITEM-6137-4.2-010-INTERP': 'route vs chord', 'ITEM-6137-4.2-011-CALC': 'square area', 'ITEM-6137-4.2-012-INTERP': '1 cm square',
                   'ITEM-6137-4.2-013-CALC': 'gradient', 'ITEM-6137-4.2-014-INTERP': 'answer_014 side', 'ITEM-6137-4.2-P01': 'measurement/height variant (answer side)'},
        'question_withholds': ['ground distances', 'areas', 'gradient'],
        'independent_solution_008': ['straight 2 km vs road 3 km (1)', 'route longer because different path (1)', 'no travel time or frequency (1)'],
    }
    prof_ok = all(b[1] >= a[1] for a, b in zip(prof, prof[1:]))
    checks = [
        check('straight A-B 2,000 m = 4 cm; road 3,000 m = 6 cm', sq_side == 2000 and abs(rlen - 3000) < 0.01),
        check('square ABCD 4 km2; 1 cm square 0.25 km2', (sq_side / 1000) ** 2 == 4 and (500 / 1000) ** 2 == 0.25),
        check('rise A->B 40 m; gradient 1:50', abs(M.height(*M.PTS['B']) - M.height(*M.PTS['A']) - 40) < 1e-6 and 2000 / 40 == 50),
        check('section rises monotonically from 1500 to 1540 (non-uniform)', prof_ok and abs(prof[0][1] - 1500) < 1e-6 and abs(prof[-1][1] - 1540) < 1e-9),
        check('scale bar 3 km = 300 px = 6 cm', 3000 * M.PX_PER_M == 300),
        check('road and points inside the map window', all(X0 <= x <= X1 and Y0 <= y <= Y1 for x, y in road + list(M.PTS.values()))),
        check('1:20 steeper than 1:50 (rise/run)', 40 / 800 > 40 / 2000),
    ]
    sides = {'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'], 'forbidden': [r'km²', r'1:50\b(?!,)', r'\b2 km\b']},
             'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']},
             'answer_014': {'path': 'assets/images/ITEM-6137-4.2-014-INTERP-%s-answer.png' % RID, 'layers': [A14], 'bound_item': 'ITEM-6137-4.2-014-INTERP'}}
    return build(RID, fig, spec, sides, checks)


def panel(fig, layer, title, rows):
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, layer)
    fig.text(36, HQ + 46, title, 28, 'start', 'bold', C['answer'], layer)
    yy = HQ + 90
    for n, s in rows:
        fig.marker(52, yy - 9, n, layer)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=layer) + 8
    return yy


if __name__ == '__main__':
    main()
