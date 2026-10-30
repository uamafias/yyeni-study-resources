"""VIS-6137-2.6-02 -> ITEM-6137-2.6-002-INTERP (map-revision-01): Namibia conservation-location map.

Original map drawn from open data; no NACSO, atlas or examination map traced:
- base: namibia_map.py (NSA regions via geoBoundaries, Natural Earth land, GeoNames towns), as VIS-6137-2.2-02;
- state protected areas and communal conservancies: Atlas of Namibia (2022) figure 8.09 data
  (Protected_Areas_Atlas.shp, Communal_Conservancies_Atlas.shp). The Atlas source note says these boundaries were
  generated from coordinate tables and descriptions in the Government Gazette. The offshore Marine Protected Area
  is omitted. Conservancies: the 89 registered in the 2020 file; Torra (Kunene, registered June 1998) and
  Salambala (Zambezi, registered June 1998) are outlined and labelled;
- Cheetah Conservation Fund centre: a point at the GeoNames farm Elandsvreugde (geonameid 12761849); CCF states its
  centre is on this farm near Otjiwarongo (https://cheetah.org/about/who-we-are/ccf-global/, read 2026-10-30).
Atlas of Namibia: CC BY 4.0, (c) Namibia Nature Foundation.
"""
import math
import os
import sys
import warnings
import zipfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, WS, sha, build, check  # noqa: E402
import namibia_map as NM  # noqa: E402
from namibia_map import shapes  # noqa: E402
from shapely.geometry import Point  # noqa: E402
from shapely.ops import unary_union  # noqa: E402
warnings.filterwarnings('ignore')

RID = 'VIS-6137-2.6-02'
ITEM = 'ITEM-6137-2.6-002-INTERP'
W, HQ, HA = 1000, 1430, 1860
LON0, LON1, LAT_TOP, LAT_BOT = 11.4, 25.6, -16.0, -29.1
K = 960 / ((LON1 - LON0) * NM.COSPHI)
P = NM.Proj(LON0, LAT_TOP, K, 20, 62)
MAP_H = (LAT_TOP - LAT_BOT) * K
F809 = os.path.join(NM.SRC, 'atlas', 'Figure 8_09 Conservation areas 2020')
ZIP809 = os.path.join(NM.SRC, 'atlas', 'Atlas_ch_08_09.zip')
PARK, PARK_EDGE, CONS_EDGE, CENTRE = '#a9d18e', '#3f7a2e', '#9a5b1f', '#b03a2e'
CCF_GEONAMEID = 12761849
CCF_SOURCE = 'https://cheetah.org/about/who-we-are/ccf-global/'
NAMED = {'Torra': ('Kunene', 3494.08), 'Salambala': ('Zambezi', 936.21)}


def area_km2(g):
    """Approximate area of a lon/lat polygon: degree area scaled by cos(latitude) at the centroid."""
    return g.area * NM.KM_PER_DEG ** 2 * math.cos(math.radians(g.centroid.y))


def km(a, b):
    """Great-circle distance between (lon, lat) points, km (R = 6,371 km)."""
    la1, la2 = math.radians(a[1]), math.radians(b[1])
    dl = math.radians(b[0] - a[0])
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin(dl / 2) ** 2
    return 2 * 6371 * math.asin(math.sqrt(h))


def bearing(a, b):
    la1, la2 = math.radians(a[1]), math.radians(b[1])
    dl = math.radians(b[0] - a[0])
    y = math.sin(dl) * math.cos(la2)
    x = math.cos(la1) * math.sin(la2) - math.sin(la1) * math.cos(la2) * math.cos(dl)
    return (math.degrees(math.atan2(y, x)) + 360) % 360


def ccf_point():
    with zipfile.ZipFile(NM.GEONAMES) as z:
        for line in z.read('NA.txt').decode('utf-8').splitlines():
            r = line.split('\t')
            if int(r[0]) == CCF_GEONAMEID:
                assert r[1] == 'Elandsvreugde' and r[7] == 'FRM'
                return float(r[5]), float(r[4])
    raise KeyError(CCF_GEONAMEID)


def main():
    regs = NM.regions()
    nam = NM.namibia(regs)
    land = NM.land((LON0, LAT_BOT, LON1, LAT_TOP)).difference(nam)
    parks = {r['NAME']: (g, r) for g, r in shapes(os.path.join(F809, 'Protected_Areas_Atlas.shp')) if r['NAME'] != 'Marine Protected Area'}
    park_all = unary_union([g for g, r in parks.values()]).intersection(nam)
    etosha = parks['Etosha National Park'][0].intersection(nam)
    cons_recs = [(g, r) for g, r in shapes(os.path.join(F809, 'Communal_Conservancies_Atlas.shp')) if r['CATEGORY'] == 'Conservancy' and r['STATUS'] == 'Registered']
    cons = {r['NAME']: (g, r) for g, r in cons_recs}
    assert sum(r['NAME'] in NAMED for g, r in cons_recs) == len(NAMED)
    cons_all = unary_union([g for g, r in cons_recs]).difference(park_all).intersection(nam)
    towns = NM.towns(['Otjiwarongo', 'Windhoek', 'Katima Mulilo', 'Rundu', 'Opuwo'])
    ccf = ccf_point()

    fig = Fig(W, {'question': HQ, 'answer': HA}, 'Wildlife conservation areas in Namibia')
    fig.pattern('conspat', '<rect width="10" height="10" fill="#f6e9cf"/><path d="M0 10 L10 0 M-3 3 L3 -3 M7 13 L13 7" stroke="#c99a5b" stroke-width="2"/>', 10, 10)
    fig.rect(P.ox, P.oy, 960, MAP_H, '#dceefa', INK, 2)
    fig.path(P.path(land, 0.02), '#e2e2de', '#9a9a9a', 1)
    fig.path(P.path(nam, 0.005), '#fbfaf5', 'none', 0)
    fig.path(P.path(cons_all, 0.005), 'url(#conspat)', '#c99a5b', 0.8)
    fig.path(P.path(park_all, 0.005), PARK, '#6f9e5a', 1)
    for n, g in regs.items():
        fig.path(P.path(g, 0.01), 'none', '#8c8c8c', 1.1)
    fig.path(P.path(nam, 0.005), 'none', INK, 2.2)
    fig.path(P.path(etosha, 0.003), 'none', PARK_EDGE, 4)
    for n in NAMED:
        fig.path(P.path(cons[n][0], 0.002), 'none', '#ffffff', 7)
        fig.path(P.path(cons[n][0], 0.002), 'none', CONS_EDGE, 4)
    for t, (lon, lat, gid) in towns.items():
        x, y = P.xy(lon, lat)
        fig.rect(x - 6, y - 6, 12, 12, INK, '#ffffff', 2)
    cx, cy = P.xy(*ccf)
    star = [(cx + (17 if i % 2 == 0 else 7) * math.sin(math.pi * i / 5), cy - (17 if i % 2 == 0 else 7) * math.cos(math.pi * i / 5)) for i in range(10)]
    fig.poly(star, CENTRE, '#ffffff', 2.5)
    off = {'Otjiwarongo': (12, -14, 'start'), 'Windhoek': (12, 9, 'start'), 'Katima Mulilo': (-12, -14, 'end'), 'Rundu': (0, -18, 'middle'),
           'Opuwo': (12, -10, 'start')}
    for t, (lon, lat, gid) in towns.items():
        x, y = P.xy(lon, lat)
        dx, dy, an = off[t]
        fig.text(x + dx, y + dy, t, 26, an, 'bold', INK, halo=True)
    fig.lines(cx + 22, cy + 34, ['Cheetah Conservation', 'Fund centre'], 26, 30, weight='bold', halo=True)
    ex, ey = P.xy(15.85, -18.95)
    fig.lines(ex, ey, ['Etosha', 'National Park'], 26, 30, anchor='middle', weight='bold', halo=True)
    # named conservancies: labels in open space with leader lines
    for n, (lx, ly, anchor) in {'Torra': (12.0, -21.35, 'start'), 'Salambala': (23.9, -19.0, 'middle')}.items():
        g = cons[n][0]
        tx, ty = P.xy(g.representative_point().x, g.representative_point().y)
        x0, y0 = P.xy(lx, ly)
        hx = x0 + (60 if anchor == 'start' else 0)
        fig.line(hx, y0 - 26, tx, ty, INK, 1.8)
        fig.circle(tx, ty, 4, INK, '#ffffff', 1.5)
        fig.lines(x0, y0, [n, 'Conservancy'], 26, 30, anchor=anchor, weight='bold', halo=True)
    for n, (lon, lat) in {'Kunene': (13.7, -18.3), 'Zambezi': (23.0, -17.9), 'Otjozondjupa': (19.6, -19.6), 'Erongo': (15.4, -22.0),
                          'Khomas': (16.5, -23.0), 'Hardap': (17.0, -24.6), '//Karas': (17.6, -27.0), 'Omaheke': (19.4, -23.2)}.items():
        assert regs[n].contains(Point(lon, lat)), n
        x, y = P.xy(lon, lat)
        fig.text(x, y + 9, n, 26, 'middle', 'normal', '#4d4d4d', halo=True, italic=True)
    for n, (lon, lat) in {'ANGOLA': (20.9, -16.45), 'BOTSWANA': (22.7, -21.3), 'SOUTH AFRICA': (22.9, -28.6),
                          'ZAMBIA': (24.6, -16.45), 'Atlantic Ocean': (12.9, -25.0)}.items():
        x, y = P.xy(lon, lat)
        fig.text(x, y + 9, n, 26, 'middle', 'normal', GREY, italic=n.startswith('Atl'), rotate=-90 if n.startswith('Atl') else None)
    NM.north_arrow(fig, 70, 720)
    NM.scale_bar(fig, P, 40, P.oy + MAP_H - 66)

    ky0 = P.oy + MAP_H + 46
    fig.text(30, ky0, 'Key', 28, 'start', 'bold')
    y = ky0 + 22
    fig.rect(30, y, 44, 28, PARK, '#6f9e5a', 1.2)
    fig.text(86, y + 23, 'State protected area (e.g. national park)', 26)
    y += 40
    fig.rect(30, y, 44, 28, 'url(#conspat)', '#c99a5b', 1.2)
    fig.text(86, y + 23, 'Registered communal conservancy (2020)', 26)
    y += 40
    fig.rect(30, y + 2, 20, 24, 'none', PARK_EDGE, 4)
    fig.rect(54, y + 2, 20, 24, 'none', CONS_EDGE, 4)
    fig.text(86, y + 23, 'Bold outline: named park or conservancy', 26)
    y += 40
    sx, sy = 52, y + 16
    star = [(sx + (17 if i % 2 == 0 else 7) * math.sin(math.pi * i / 5), sy - (17 if i % 2 == 0 else 7) * math.cos(math.pi * i / 5)) for i in range(10)]
    fig.poly(star, CENTRE, '#ffffff', 2.5)
    fig.text(86, y + 23, 'Conservation centre', 26)
    y += 40
    fig.rect(34, y + 8, 12, 12, INK, '#ffffff', 2)
    fig.line(52, y + 14, 74, y + 14, '#8c8c8c', 1.2)
    fig.text(86, y + 23, 'Town; region boundary', 26)
    sy2 = y + 76
    for s in ['Parks and conservancies: Atlas of Namibia 2022 data from Government',
              'Gazette boundaries (CC BY 4.0). Regions: NSA (CC BY 3.0 IGO). Towns and',
              'farm Elandsvreugde: GeoNames. East–west scale within 5%.']:
        fig.text(30, sy2, s, 26, 'start', 'normal', GREY)
        sy2 += 32
    assert sy2 <= HQ, sy2

    A = 'a'
    fig.marker(*P.xy(16.8, -18.62), '1', A)
    fig.marker(cx - 14, cy + 42, '2', A)
    for n in NAMED:
        g = cons[n][0]
        fig.marker(*P.xy(g.centroid.x + (-0.6 if n == 'Torra' else 0.55), g.centroid.y + (0.3 if n == 'Torra' else 0.1)), '3', A)
    d_ccf = km(towns['Otjiwarongo'][:2], ccf)
    b_ccf = bearing(towns['Otjiwarongo'][:2], ccf)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Interpretation', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for k, s in [('1', 'Etosha National Park is a large state-protected area in northern Namibia, south of the north-central regions: an area, not a point.'),
                 ('2', 'The Cheetah Conservation Fund is one centre, shown as a point about %d km east of Otjiwarongo in a straight line, not as a protected area.' % (round(d_ccf / 5) * 5)),
                 ('3', 'Torra (north-west, in Kunene) and Salambala (north-east, in Zambezi, south-east of Katima Mulilo) are communal conservancies: areas, but in a different key category from the park.')]:
        fig.marker(52, yy - 9, k, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8
    assert yy <= HA - 10, yy

    def region_of(g):
        return max(regs, key=lambda n: regs[n].intersection(g).area)
    areas = {'Etosha': (area_km2(parks['Etosha National Park'][0]), parks['Etosha National Park'][1]['AREA_KM2_'])}
    areas.update({n: (area_km2(cons[n][0]), v[1]) for n, v in NAMED.items()})
    kat = towns['Katima Mulilo'][:2]
    sal = (cons['Salambala'][0].centroid.x, cons['Salambala'][0].centroid.y)
    checks = [
        check('Etosha, Torra and Salambala areas match the Atlas attribute areas within 5 %', all(abs(a - b) / b < 0.05 for a, b in areas.values()),
              str({k: (round(a), b) for k, (a, b) in areas.items()})),
        check('Torra lies in Kunene and Salambala in Zambezi', region_of(cons['Torra'][0]) == 'Kunene' and region_of(cons['Salambala'][0]) == 'Zambezi'),
        check('Torra is north-west (west of 15 E) and Salambala north-east (east of 23 E), both registered June 1998',
              cons['Torra'][0].centroid.x < 15 and cons['Salambala'][0].centroid.x > 23 and all(cons[n][1]['YEAR_REG'] == 1998 and cons[n][1]['MONTH_REG'] == 6 for n in NAMED)),
        check('Etosha is in the north (centroid north of 19.5 S) and south of the north-central crop regions',
              etosha.centroid.y > -19.5 and all(regs[n].centroid.y > etosha.centroid.y for n in ('Omusati', 'Oshana', 'Ohangwena'))),
        check('CCF point is 35-45 km from Otjiwarongo, bearing east (75-105 deg), in Otjozondjupa',
              35 <= d_ccf <= 45 and 75 <= b_ccf <= 105 and regs['Otjozondjupa'].contains(Point(*ccf)), '%.1f km, %.0f deg' % (d_ccf, b_ccf)),
        check('CCF point lies outside every state protected area and conservancy', not park_all.contains(Point(*ccf)) and not cons_all.contains(Point(*ccf))),
        check('Salambala centre lies 30-60 km south-east (110-160 deg) of Katima Mulilo', 30 < km(kat, sal) < 60 and 110 < bearing(kat, sal) < 160,
              '%.0f km, %.0f deg' % (km(kat, sal), bearing(kat, sal))),
        check('all registered conservancy records drawn (89 records, %d names)' % len(cons), len(cons_recs) == 89, str(len(cons_recs))),
    ]
    spec = {
        'kind': 'original conservation-location map of Namibia from open data (no NACSO, atlas or examination map traced)',
        'base': NM.base_sources(),
        'thematic_sources': {
            'atlas_data': {'citation': 'Atlas of Namibia Team, 2022, Atlas of Namibia: its land, water and life, Namibia Nature Foundation, Windhoek',
                           'licence': 'CC BY 4.0', 'zip': {'url': 'https://the-eis.com/elibrary/sites/default/files/downloads/literature/Atlas_ch_08_09.zip',
                                                           'record': 'https://the-eis.com/elibrary/search/26651',
                                                           'local_copy': os.path.relpath(ZIP809, WS), 'sha256': sha(ZIP809)},
                           'files': ['Protected_Areas_Atlas.shp (24 areas; offshore Marine Protected Area omitted)', 'Communal_Conservancies_Atlas.shp (89 registered)'],
                           'boundary_method': 'Atlas source note: generated from coordinate tables and descriptions in the Government Gazette'},
            'ccf_centre': {'point_lonlat': ccf, 'geonames': 'farm Elandsvreugde, geonameid %d (CC BY 4.0)' % CCF_GEONAMEID,
                           'ccf_statement': 'CCF centre is on the farm Elandsvreugde near Otjiwarongo', 'url': CCF_SOURCE, 'read': '2026-10-30',
                           'distance_from_otjiwarongo_km': round(d_ccf, 1), 'bearing_deg': round(b_ccf),
                           'note': 'straight-line distance; the existing claim CL-6137-2.6.01-01-R1 gives about 44 km east (road distance from a travel source)'},
        },
        'named_features': {'Etosha National Park': {'atlas_area_km2': areas['Etosha'][1], 'year': parks['Etosha National Park'][1]['YEAR']},
                           'Torra': dict(cons['Torra'][1]), 'Salambala': dict(cons['Salambala'][1])},
        'question_withholds': ['interpretation panel and markers'],
        'independent_solution': ['Etosha = northern park area (1)', 'CCF = point centre ~40 km east of Otjiwarongo (1)',
                                 'Torra NW / Salambala NE conservancy areas; key separates areas from the point (1)'],
    }
    sides = {'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'], 'forbidden': [r'Interpretation', r'km east', r'not an area', r'not a point']},
             'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': [A]}}
    return build(RID, fig, spec, sides, checks)


if __name__ == '__main__':
    main()
