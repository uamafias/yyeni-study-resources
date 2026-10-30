"""VIS-6137-4.2-03 -> ITEM-6137-4.2-016-INTERP (assigned); recorded reuses 015, 017-020 (base images) and 022
(relief-panel variant).

Base: a direction panel of the same training world (map42.py) at 1:50,000 on the perpendicular 1 km grid:
A, B, C, D with straight lines A->B (east), A->D (north) and A->C (equal 2,000 m east and north offsets),
a grid-north arrow and a compass circle marked N, NE, E, SE, S, SW, W, NW with 45 degree ticks (no
degree labels on the question side). Answer: bearings 090, 000, 045; reverse B->A 270; the circle in
degrees; a 225 degree reading for C would point south-west (opposite quadrant); straight-line
directions do not show a safe road.
022 variant: the hill around B from the same terrain, with closed contours 1,510, 1,520 and 1,530 m and
the 1,540 m spot height (interval 10 m, 1:50,000). Answer adds the hill reading, the closer spacing on
the east (steeper) than the west, and a west-east section through B from the same terrain.
"""
import math
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, Axes, build, check  # noqa: E402
import map42 as M  # noqa: E402

RID = 'VIS-6137-4.2-03'
ITEM = 'ITEM-6137-4.2-016-INTERP'
B022 = 'ITEM-6137-4.2-022-INTERP'
W, HQ, HA = 1000, 620, 990
OX, OY = 95, 90
X0, X1, Y0, Y1 = 1000, 5000, 1000, 5000
CX, CY, CR = 790, 320, 120
VY, VHQ, VHA = HA + 70, 520, 990
RX0, RX1, RY0, RY1 = 2400, 5300, 400, 3500
CONTOUR = '#a0522d'


def P(x, y, x0=X0, y0=Y0, ox=OX, oy=OY, h=Y1 - Y0):
    return M.to_px(x, y, x0, y0, ox, oy, h)


def bearing(p, q):
    return math.degrees(math.atan2(q[0] - p[0], q[1] - p[1])) % 360


def panel(fig, y0, y1, title, rows, layer):
    fig.rect(16, y0, W - 32, y1 - y0, '#f4faf6', C['answer'], 2, 8, layer)
    fig.text(36, y0 + 40, title, 28, 'start', 'bold', C['answer'], layer)
    yy = y0 + 84
    for n, s in rows:
        fig.marker(52, yy - 9, n, layer)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=layer) + 8
    return yy


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'Direction panel on a perpendicular grid (grid north)')
    fig.extra_h = VY + VHA
    mw = (X1 - X0) * M.PX_PER_M
    fig.rect(OX, OY, mw, mw, '#f8f6ee', INK, 2.5)
    for g in range(X0 + 1000, X1, 1000):
        fig.line(*P(g, Y0), *P(g, Y1), '#9fb3c8', 1.4)
        fig.line(*P(X0, g), *P(X1, g), '#9fb3c8', 1.4)
        fig.text(P(g, Y0)[0], OY + mw + 30, str(g), 26, 'middle')
        fig.text(OX - 8, P(X0, g)[1] + 9, str(g), 26, 'end')
    A_ = P(*M.PTS['A'])
    for k in 'BCD':
        fig.arrow(*A_, *P(*M.PTS[k]), INK, 3.5, 18)
    for k, (dx, dy, anc) in {'A': (-12, 32, 'end'), 'B': (12, 32, 'start'), 'C': (12, -12, 'start'), 'D': (-12, -12, 'end')}.items():
        x, y = P(*M.PTS[k])
        fig.circle(x, y, 7, INK, '#ffffff', 2)
        fig.text(x + dx, y + dy, k, 30, anc, 'bold', INK, halo=True)
    fig.arrow(OX + mw + 40, OY + 110, OX + mw + 40, OY + 10, INK, 5, 20)
    fig.lines(OX + mw + 40, OY + 140, ['Grid', 'north'], 26, 30, anchor='middle', weight='bold')
    fig.text(OX, OY + mw + 72, 'Grid squares 1 km (1:50,000); x east, y north in metres.', 26, 'start', 'normal', GREY)
    # compass circle
    fig.circle(CX, CY, CR, '#ffffff', INK, 2.5)
    for i, lab in enumerate(['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']):
        a = math.radians(45 * i)
        fig.line(CX + (CR - 14) * math.sin(a), CY - (CR - 14) * math.cos(a), CX + CR * math.sin(a), CY - CR * math.cos(a), INK, 3)
        r = CR + (26 if len(lab) == 1 else 34)
        fig.text(CX + r * math.sin(a), CY - r * math.cos(a) + 9, lab, 26, 'middle', 'bold')
    fig.circle(CX, CY, 4, INK, INK, 1)
    fig.text(CX, CY + CR + 82, 'Compass circle (clockwise)', 26, 'middle', 'bold')

    A = 'a'
    for k, (dx, dy) in {'B': (0, -14), 'D': (-56, 0), 'C': (-30, -26)}.items():
        mx, my = (A_[0] + P(*M.PTS[k])[0]) / 2, (A_[1] + P(*M.PTS[k])[1]) / 2
        fig.text(mx + dx, my + dy, '%03d°' % round(bearing(M.PTS['A'], M.PTS[k])), 28, 'middle', 'bold', C['answer'], A, halo=True)
    bx, by = P(*M.PTS['B'])
    fig.arrow(bx - 10, by + 60, A_[0] + 10, A_[1] + 60, C['answer'], 3, 16, A, dash='10 7')
    fig.text((bx + A_[0]) / 2, by + 92, 'B→A 270°', 28, 'middle', 'bold', C['answer'], A, halo=True)
    for i in range(8):
        a = math.radians(45 * i)
        r = CR - 44
        fig.text(CX + r * math.sin(a), CY - r * math.cos(a) + 9, '%03d' % (45 * i), 26, 'middle', 'bold', C['answer'], A, halo=True)
    fig.marker(OX + mw - 30, OY + 30, '1', A)
    fig.marker((bx + A_[0]) / 2 - 110, by + 82, '2', A)
    fig.marker(CX - CR - 30, CY + CR, '3', A)
    panel(fig, HQ + 6, HA - 10, 'Bearings from grid north (clockwise)', [
        ('1', 'A→B is due east: 090°. A→D is due north: 000°. A→C has equal 2,000 m east and north offsets, so it bisects the right angle: 045°.'),
        ('2', 'Reverse: B→A = 090° + 180° = 270°. B has the same northing as A, so there is no north–south offset.'),
        ('3', 'A reading of 225° for C would point south-west, the opposite quadrant, so recheck it. These straight lines do not show a safe road.')], A)

    # ---- 022 relief variant
    V, VQ, VA = 'v-022', 'v-022-q', 'v-022-a'
    fig.rect(0, VY, W, VHA, '#ffffff', 'none', 0, layer=V)
    fig.text(W / 2, VY + 40, 'Relief panel (1:50,000; contour interval 10 m)', 28, 'middle', 'bold', layer=V)
    rox, roy = 60, VY + 80
    rw, rh = (RX1 - RX0) * M.PX_PER_M, (RY1 - RY0) * M.PX_PER_M

    def R(x, y):
        return M.to_px(x, y, RX0, RY0, rox, roy, RY1 - RY0)
    fig.rect(rox, roy, rw, rh, '#f8f6ee', INK, 2.5, layer=V)
    for lv in (1510, 1520, 1530):
        fig.poly([R(*p) for p in M.contour(lv)], 'none', CONTOUR, 3 if lv == 1520 else 2, layer=V)
        x, y = R(*M.contour(lv, 360)[270])
        fig.text(x, y + 9, str(lv), 26, 'middle', 'bold', CONTOUR, V, halo=True)
    bx, by = R(*M.PTS['B'])
    fig.circle(bx, by, 5, INK, INK, 1, V)
    fig.text(bx + 10, by - 12, '1540', 26, 'start', 'bold', INK, V, halo=True)
    kx = rox + rw + 50
    fig.arrow(kx + 300, roy + 90, kx + 300, roy + 10, INK, 4, 18, V)
    fig.text(kx + 300, roy + 120, 'N', 26, 'middle', 'bold', layer=V)
    fig.line(kx, roy + 30, kx + 50, roy + 30, CONTOUR, 3, V)
    fig.text(kx + 62, roy + 39, 'contour (m)', 26, layer=V)
    fig.circle(kx + 25, roy + 80, 5, INK, INK, 1, V)
    fig.text(kx + 62, roy + 89, 'spot height (m)', 26, layer=V)
    fig.text(kx, roy + 150, 'Contour interval 10 m', 26, 'start', 'bold', layer=V)
    for i in range(2):
        fig.rect(kx + i * 50, roy + 186, 50, 12, INK if i == 0 else '#ffffff', INK, 1.5, layer=V)
    fig.text(kx, roy + 226, '0', 26, 'middle', layer=V)
    fig.text(kx + 100, roy + 226, '1 km', 26, 'middle', layer=V)
    fig.text(kx, roy + 270, '1 cm = 500 m when printed', 26, 'start', 'normal', GREY, V)
    fig.text(kx, roy + 302, '20 cm wide; else use the bar.', 26, 'start', 'normal', GREY, V)
    # answer: spacing annotations and W-E section
    e1530 = max(p[0] for p in M.contour(1530))
    e1510 = max(p[0] for p in M.contour(1510))
    w1530 = min(p[0] for p in M.contour(1530))
    w1510 = min(p[0] for p in M.contour(1510))
    fig.line(*R(w1510, 2000), *R(w1530, 2000), C['answer'], 5, VA)
    fig.line(*R(e1530, 2000), *R(e1510, 2000), C['answer'], 5, VA)
    fig.text(bx, by + 40, 'hill', 30, 'middle', 'bold', C['answer'], VA, halo=True)
    sx = Axes(fig, kx + 110, roy + 360, 330, 150, (RX0, RX1), (1500, 1545), layer=VA)
    sx.draw([3000, 4000, 5000], [1510, 1520, 1530, 1540], 'x (m east) along y = 2000', 'Height (m)', ylabel_x=kx + 20)
    prof = [(x, M.height(x, 2000)) for x in range(RX0, RX1 + 1, 25)]
    sx.polyline(prof, '#6b4f2a', 4)
    fig.marker(bx, by - 52, '1', VA)
    fig.marker(*R(e1510 + 250, 2400), '2', VA)
    panel(fig, VY + VHQ + 186, VY + VHA - 10, 'Interpretation', [
        ('1', 'Height rises inwards from 1,510 m to the 1,540 m spot height: a hill.'),
        ('2', 'With a common 10 m interval, contours are closer on the east (steeper) than the west (gentler).'),
        ('3', 'Contours show relief only: they do not show vegetation or what people do there.')], VA)

    bearings = {k: bearing(M.PTS['A'], M.PTS[k]) for k in 'BCD'}
    west_gap = (w1530 - w1510)
    east_gap = (e1510 - e1530)
    spec = {
        'kind': 'direction panel and relief-panel variant from the 4.2 training world',
        'geometry_source': 'assets/code/map42.py', 'window_m': {'x': [X0, X1], 'y': [Y0, Y1]},
        'bearings_from_A': {k: round(v, 6) for k, v in bearings.items()}, 'reverse_B_to_A': round(bearing(M.PTS['B'], M.PTS['A']), 6),
        'compass_circle': {'labels': ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'], 'answer_degrees': [45 * i for i in range(8)]},
        'reuses_base_images': {'ITEM-6137-4.2-015-CALC': 'A->C 045', 'ITEM-6137-4.2-017-CALC': 'E 090 on the circle', 'ITEM-6137-4.2-018-INTERP': 'B east of A, same northing',
                               'ITEM-6137-4.2-019-CALC': 'B->A 270', 'ITEM-6137-4.2-020-INTERP': '225 is SW, opposite of 045'},
        'v022': {'bound_item': B022, 'window_m': {'x': [RX0, RX1], 'y': [RY0, RY1]}, 'contours_m': [1510, 1520, 1530], 'spot_height_m': 1540,
                 'gap_1510_1530_on_y2000_m': {'west': round(west_gap, 1), 'east': round(east_gap, 1)}},
        'question_withholds': ['degree values', 'reverse bearing', 'hill and steepness reading (022)'],
        'independent_solution_016': ['A->B 090, A->D 000 (1)', 'A->C 045 (equal offsets) (1)', 'directions only, no road evidence (1)'],
    }
    checks = [
        check('A->B 090, A->C 045, A->D 000; B->A 270', [round(bearings[k]) for k in 'BCD'] == [90, 45, 0] and round(bearing(M.PTS['B'], M.PTS['A'])) == 270),
        check('225 is the reverse of 045 (south-west quadrant)', (45 + 180) % 360 == 225 and 180 < 225 < 270),
        check('022 contours closed inside the relief window', all(RX0 <= x <= RX1 and RY0 <= y <= RY1 for lv in (1510, 1520, 1530) for x, y in M.contour(lv))),
        check('022 east side steeper (smaller 1510-1530 gap on y = 2000)', east_gap < west_gap, 'east %.0f m, west %.0f m' % (east_gap, west_gap)),
        check('022 spot height 1540 inside the 1530 contour', abs(M.height(*M.PTS['B']) - 1540) < 1e-9),
    ]
    sides = {
        'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'], 'forbidden': [r'\d\d\d°', r'270', r'225']},
        'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']},
        '022_question': {'path': 'assets/images/%s-%s-question.png' % (B022, RID), 'layers': [V, VQ], 'clip': (0, VY, W, VHQ), 'hide_base': True,
                         'bound_item': B022, 'forbidden': [r'hill', r'steep']},
        '022_answer': {'path': 'assets/images/%s-%s-answer.png' % (B022, RID), 'layers': [V, VA], 'clip': (0, VY, W, VHA), 'hide_base': True,
                       'bound_item': B022, 'panels': [(16, VY + VHQ + 186, W - 32, VHA - VHQ - 196)]},
    }
    return build(RID, fig, spec, sides, checks)


if __name__ == '__main__':
    main()
