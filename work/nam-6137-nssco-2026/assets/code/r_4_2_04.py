"""VIS-6137-4.2-04 -> ITEM-6137-4.2-034-INTERP (assigned); recorded reuses 033 and 035-040 (base images).

Coordinate panel with its own extent (allowed by map_geometry.coordinate_panel): a 30-second graticule
from 23 deg 00' 00" S to 23 deg 02' 00" S and 17 deg 00' 00" E to 17 deg 02' 00" E, drawn in a real
projection (Transverse Mercator on WGS84, central meridian 17 deg 01' E, origin 23 deg 01' S, k0 = 1;
map42.tm) at 1:50,000 when printed 20 cm wide. P (23 deg 00' 30" S, 17 deg 00' 30" E) and Q (23 deg 01' 30" S,
17 deg 01' 30" E) are plotted from their coordinates; the coordinates are also printed. True north (along
the meridians), scale bar, key and projection note are shown. The graticule is not a linear grid relabelled
in degrees: every line is projected point by point. The panel is an exercise extent, not a map of a
named place.
Answer: Q is 1' farther south and 1' farther east; midpoint M 23 deg 01' 00" S, 17 deg 01' 00" E; 1' of
latitude is about 1.85 km but 1' of longitude about 1.71 km here (both from the ellipsoid and agreeing with
the projected geometry); 23 deg 01' 30" = 23.025 deg S.
"""
import math
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, build, check  # noqa: E402
import map42 as M  # noqa: E402

RID = 'VIS-6137-4.2-04'
ITEM = 'ITEM-6137-4.2-034-INTERP'
W, HQ, HA = 1000, 690, 1100
LATS = [-(23 + s / 3600) for s in range(0, 121, 30)]          # 23 deg 00' 00" S ... 23 deg 02' 00" S
LONS = [17 + s / 3600 for s in range(0, 121, 30)]
PQ = {'P': (-(23 + 30 / 3600), 17 + 30 / 3600), 'Q': (-(23 + 90 / 3600), 17 + 90 / 3600)}
MID = (-(23 + 60 / 3600), 17 + 60 / 3600)
CXP, CYP = 335, 330                    # px position of the projection origin (centre of the panel)


def px(lat, lon):
    e, n = M.tm(lat, lon)
    return CXP + e * M.PX_PER_M, CYP - n * M.PX_PER_M


def line(fig, pts, **kw):
    fig.poly([px(*p) for p in pts], 'none', closed=False, **kw)


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'Latitude and longitude panel (exercise extent, 1:50,000)')
    corners = [px(LATS[0], LONS[0]), px(LATS[0], LONS[-1]), px(LATS[-1], LONS[-1]), px(LATS[-1], LONS[0])]
    fig.poly(corners, '#f8f6ee', INK, 2.5)
    for lat in LATS:
        line(fig, [(lat, LONS[0] + i * (LONS[-1] - LONS[0]) / 20) for i in range(21)], stroke='#7a8fa6', sw=1.6)
    for lon in LONS:
        line(fig, [(LATS[0] + i * (LATS[-1] - LATS[0]) / 20, lon) for i in range(21)], stroke='#7a8fa6', sw=1.6)
    for i, lat in enumerate(LATS):
        x, y = px(lat, LONS[0]) if i % 2 == 0 else px(lat, LONS[-1])
        fig.text(x - 10 if i % 2 == 0 else x + 10, y + 9, M.dms(lat, 'S'), 26, 'end' if i % 2 == 0 else 'start')
    for i, lon in enumerate(LONS):
        x, y = px(LATS[-1], lon) if i % 2 == 0 else px(LATS[0], lon)
        fig.text(x, y + 44 if i % 2 == 0 else y - 14, M.dms(lon, 'E'), 26, 'middle')
    for k, (lat, lon) in PQ.items():
        x, y = px(lat, lon)
        fig.circle(x, y, 8, '#c0392b', INK, 2)
        fig.text(x + 14, y - 12, k, 30, 'start', 'bold', INK, halo=True)
    rx = 672
    fig.arrow(rx + 280, 210, rx + 280, 120, INK, 5, 20)
    fig.lines(rx + 280, 240, ['True', 'north'], 26, 30, anchor='middle', weight='bold')
    fig.text(rx, 140, 'Plotted points', 26, 'start', 'bold')
    for i, (k, (lat, lon)) in enumerate(PQ.items()):
        fig.text(rx, 176 + i * 70, k, 26, 'start', 'bold')
        fig.lines(rx + 34, 176 + i * 70, [M.dms(lat, 'S') + ',', M.dms(lon, 'E')], 26, 32)
    fig.line(rx, 330, rx + 44, 330, '#7a8fa6', 2)
    fig.lines(rx + 56, 339, ['graticule line', '(every 30″)'], 26, 30)
    fig.circle(rx + 22, 400, 8, '#c0392b', INK, 2)
    fig.text(rx + 56, 409, 'plotted point', 26)
    for i in range(2):
        fig.rect(rx + i * 50, 450, 50, 12, INK if i == 0 else '#ffffff', INK, 1.5)
    fig.text(rx, 490, '0', 26, 'middle')
    fig.text(rx + 100, 490, '1 km', 26, 'middle')
    fig.para(40, 590, 'Transverse Mercator projection (WGS84), central meridian 17°01′E. 1:50,000 only when printed 20 cm wide; '
             'otherwise use the scale bar. The extent is an exercise area, not a named place.', 26, 920, 32, fill=GREY)

    A = 'a'
    mx, my = px(*MID)
    fig.circle(mx, my, 8, C['answer'], '#ffffff', 2, A)
    fig.text(mx + 14, my + 30, 'M', 30, 'start', 'bold', C['answer'], A, halo=True)
    (px_, py_), (qx, qy) = px(*PQ['P']), px(*PQ['Q'])
    fig.arrow(px_, py_ + 14, px_, qy, C['answer'], 3, 14, A, dash='8 6')
    fig.arrow(px_ + 14, qy, qx - 10, qy, C['answer'], 3, 14, A, dash='8 6')
    fig.text(px_ - 12, (py_ + qy) / 2 + 9, '1′ S', 26, 'end', 'bold', C['answer'], A, halo=True)
    fig.text((px_ + qx) / 2, qy + 32, '1′ E', 26, 'middle', 'bold', C['answer'], A, halo=True)
    lat_km = M.meridian_minute_m(MID[0]) / 1000
    lon_km = M.parallel_minute_m(MID[0]) / 1000
    fig.marker(qx + 36, qy + 36, '1', A)
    fig.marker(mx - 30, my - 30, '2', A)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Reading the coordinates', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for n, s in [('1', 'Q is 1′ farther south (23°01′30″S has the larger south value) and 1′ farther east (17°01′30″E) than P.'),
                 ('2', 'Midpoint M: add 30″ to each of P’s coordinates, giving 23°01′00″S, 17°01′00″E.'),
                 ('3', 'Equal angular steps are not equal ground lengths: here 1′ of latitude ≈ %.2f km but 1′ of longitude ≈ %.2f km.' % (lat_km, lon_km)),
                 ('4', 'Decimal: 23°01′30″ = 23 + 1/60 + 30/3,600 = 23.025° S (or −23.025°), not 23.0130.')]:
        fig.marker(52, yy - 9, n, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8

    eP, nP = M.tm(*PQ['P'])
    eQ, nQ = M.tm(*PQ['Q'])
    dlat_m = nP - nQ
    dlon_m = eQ - eP
    conv_deg = math.degrees(math.atan2(*(lambda a, b: (b[0] - a[0], b[1] - a[1]))(M.tm(LATS[-1], LONS[0]), M.tm(LATS[0], LONS[0]))))
    spec = {
        'kind': 'graticule panel in a real projection (Transverse Mercator, WGS84)',
        'projection': {'name': 'Transverse Mercator', 'ellipsoid': 'WGS84', 'central_meridian': '17°01′00″E', 'origin_latitude': '23°01′00″S', 'k0': 1,
                       'formulae': 'Snyder 1987, Map Projections - A Working Manual, eqs 8-9 to 8-13 (implemented in map42.tm)'},
        'scale': '1:50,000 when printed 20 cm wide (0.1 px per projected metre)',
        'graticule_interval': '30″', 'extent': ['23°00′00″S-23°02′00″S', '17°00′00″E-17°02′00″E'],
        'points': {k: [M.dms(lat, 'S'), M.dms(lon, 'E')] for k, (lat, lon) in PQ.items()}, 'midpoint': [M.dms(MID[0], 'S'), M.dms(MID[1], 'E')],
        'projected_m': {'P': [round(eP, 2), round(nP, 2)], 'Q': [round(eQ, 2), round(nQ, 2)]},
        'one_minute_km_at_23_01S': {'latitude': round(lat_km, 4), 'longitude': round(lon_km, 4)},
        'decimal_latitude_Q': 23 + 1 / 60 + 30 / 3600,
        'reuses_base_images': ['ITEM-6137-4.2-033-CALC', 'ITEM-6137-4.2-035-CALC', 'ITEM-6137-4.2-036-INTERP', 'ITEM-6137-4.2-037-CALC',
                               'ITEM-6137-4.2-038-INTERP', 'ITEM-6137-4.2-039-CALC', 'ITEM-6137-4.2-040-INTERP'],
        'question_withholds': ['midpoint', 'differences', 'ground lengths of a minute', 'decimal conversion'],
        'independent_solution_034': ['Q farther south and east (1)', 'each coordinate differs by 1′ (1)', 'equal angles ≠ equal ground lengths (1)'],
    }
    checks = [
        check('P to Q: one minute south and one minute east', abs((PQ['P'][0] - PQ['Q'][0]) * 60 - 1) < 1e-9 and abs((PQ['Q'][1] - PQ['P'][1]) * 60 - 1) < 1e-9),
        check('midpoint 23°01′00″S, 17°01′00″E', spec['midpoint'] == ['23°01′00″S', '17°01′00″E']),
        check('projected P-Q offsets agree with ellipsoid minute lengths (within 0.5%)',
              abs(dlat_m - lat_km * 1000) / (lat_km * 1000) < 0.005 and abs(dlon_m - lon_km * 1000) / (lon_km * 1000) < 0.005, 'N %.1f m, E %.1f m' % (dlat_m, dlon_m)),
        check('1′ latitude longer than 1′ longitude at 23°S', lat_km > lon_km),
        check('decimal 23°01′30″ = 23.025', abs(spec['decimal_latitude_Q'] - 23.025) < 1e-12),
        check('meridian convergence across the panel negligible (< 0.05°)', abs(conv_deg) < 0.05, '%.4f°' % conv_deg),
    ]
    sides = {'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'], 'forbidden': [r'23\.025', r'1\.85', r'1\.71', r'\bM\b', r'midpoint']},
             'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']}}
    return build(RID, fig, spec, sides, checks)


if __name__ == '__main__':
    main()
