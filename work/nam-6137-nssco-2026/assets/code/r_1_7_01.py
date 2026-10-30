"""VIS-6137-1.7-01 -> ITEM-6137-1.7-002-INTERP: simplified world map of rainforest, savannah and tropical desert.

Coastlines: Natural Earth 1:110m land (public domain; copy and SHA-256 in assets/sources). Projection:
equirectangular (plate carree), longitude 120 W-160 E, latitude 40 S-40 N, with the Equator and both
tropics (23.44 degrees). Vegetation zones are deliberately generalised polygons (author's
generalisation of widely published biome maps, approximate boundaries, stated on the figure), each
clipped to land with shapely; savannah is drawn only where neither of the other two classes lies.
"""
import json
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, WS, sha, build, check  # noqa: E402
from shapely.geometry import Polygon, shape, Point  # noqa: E402
from shapely.ops import unary_union  # noqa: E402

RID = 'VIS-6137-1.7-01'
ITEM = 'ITEM-6137-1.7-002-INTERP'
W, HQ, HA = 1000, 455, 810
LON0, LON1, LAT0, LAT1 = -120, 160, -40, 40
MX, MY, MW = 20, 70, 960
MH = MW * (LAT1 - LAT0) / (LON1 - LON0)
LAND_SRC = os.path.join(WS, 'assets', 'sources', 'ne_110m_land.geojson')
COL = {'R': '#1f6b3a', 'S': '#d9c25a', 'D': '#e9a46a', 'other': '#d6d6d0'}
ZONES = {
    'R': [[(-79, 2), (-75, 6), (-67, 6), (-60, 7), (-52, 4), (-50, 0), (-48, -2), (-50, -8), (-58, -12), (-66, -12), (-72, -11), (-77, -6), (-79, -2)],
          [(-89, 16), (-83, 15), (-80, 9), (-77, 7), (-79, 8), (-84, 10), (-88, 14)],
          [(-13, 9), (-8, 8), (-3, 7), (0, 6.5), (-3, 4.8), (-8, 4.5), (-12, 7)],
          [(5, 6), (9, 7), (15, 5), (25, 5), (30, 3), (30, -3), (26, -5), (18, -5), (14, -4), (9, -2), (9, 4)],
          [(95, 6), (100, 8), (104, 3), (110, 4), (118, 7), (126, 6), (141, -2), (150, -6), (147, -9), (141, -8), (130, -4), (120, -2), (115, -4), (105, -6), (97, 2)]],
    'D': [[(-17, 20), (-13, 27), (-9, 30), (0, 31), (10, 31), (20, 31), (30, 30), (33, 28), (35, 22), (36, 17), (30, 15), (20, 15.5), (10, 16), (0, 16), (-10, 17), (-17, 16)],
          [(35, 28), (37, 30), (46, 30), (51, 26), (57, 23), (55, 17), (48, 15), (43, 15), (39, 20)],
          [(69, 24), (70, 29), (73, 30), (75, 27), (72, 24)],
          [(11, -17), (13.5, -17), (16, -22), (16.8, -28), (15.5, -29.5), (14, -24), (12, -19)],
          [(115, -21), (128, -20), (138, -20), (142, -24), (140, -30), (130, -31), (122, -30), (116, -26)],
          [(-71.5, -15), (-69.5, -15), (-69, -27), (-70.5, -29), (-71.5, -24)],
          [(-116, 32), (-109, 34), (-104, 32), (-102, 28), (-106, 26), (-110, 27), (-114, 29)]],
    'S': [[(-17, 15), (-5, 15.5), (10, 15), (25, 14), (35, 12), (40, 9), (42, 4), (38, 0), (32, 4), (25, 6), (15, 7), (5, 8), (-3, 8.5), (-12, 10)],
          [(30, -3), (38, -2), (41, -4), (40, -10), (35, -20), (32, -24), (27, -25), (20, -22), (14, -17), (12, -8), (18, -6), (26, -6)],
          [(-60, -12), (-50, -9), (-44, -4), (-38, -6), (-40, -15), (-46, -21), (-55, -22), (-60, -16)],
          [(-72, 4), (-67, 8), (-62, 9), (-63, 6), (-68, 4)],
          [(122, -14), (130, -11), (137, -12), (142, -11), (145, -15), (147, -20), (140, -20), (130, -19), (123, -18)]],
}
CHECKPOINTS = {'R': [(-62, -3, 'Amazon'), (22, 0, 'Congo'), (114, 1, 'Borneo')],
               'S': [(10, 11, 'West African savannah'), (35, -8, 'East African savannah'), (-50, -15, 'Brazilian savannah'), (133, -16, 'northern Australia')],
               'D': [(10, 24, 'Sahara'), (47, 22, 'Arabian'), (15, -24, 'Namib'), (130, -25, 'central Australia')]}


def X(lon):
    return MX + (lon - LON0) / (LON1 - LON0) * MW


def Y(lat):
    return MY + (LAT1 - lat) / (LAT1 - LAT0) * MH


def path(geom):
    polys = [geom] if geom.geom_type == 'Polygon' else list(getattr(geom, 'geoms', []))
    d = ''
    for p in polys:
        if p.geom_type != 'Polygon' or p.is_empty:
            continue
        for ring in [p.exterior] + list(p.interiors):
            d += 'M' + ' L'.join('%.1f %.1f' % (X(x), Y(y)) for x, y in ring.coords) + ' Z '
    return d


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'Three vegetation regions (simplified world map)')
    land = unary_union([shape(f['geometry']) for f in json.load(open(LAND_SRC))['features']])
    frame = Polygon([(LON0, LAT0), (LON1, LAT0), (LON1, LAT1), (LON0, LAT1)])
    land = land.intersection(frame)
    zones = {k: unary_union([Polygon(p) for p in v]).intersection(land) for k, v in ZONES.items()}
    zones['S'] = zones['S'].difference(zones['R']).difference(zones['D'])
    fig.rect(MX, MY, MW, MH, '#e3f0f8', INK, 1.5)
    fig.path(path(land), COL['other'], '#888888', 0.8)
    fig.pattern('dpat', '<rect width="8" height="8" fill="%s"/><circle cx="2" cy="2" r="1.4" fill="#7a3d12"/>'
                '<circle cx="6" cy="6" r="1.4" fill="#7a3d12"/>' % COL['D'], 8, 8)
    fill = dict(COL, D='url(#dpat)')
    for k in ('S', 'R', 'D'):
        fig.path(path(zones[k]), fill[k], 'none', 0)
    fig.path(path(land), 'none', '#555555', 0.8)
    for lat, lab in ((23.44, 'Tropic of Cancer 23½°N'), (0, 'Equator 0°'), (-23.44, 'Tropic of Capricorn 23½°S')):
        fig.line(MX, Y(lat), MX + MW, Y(lat), INK, 1.8, dash='10 6')
        fig.text(MX + 8, Y(lat) - 6, lab, 26, 'start', 'bold', INK, halo=True)
    fig.text(MX + MW - 8, MY + MH - 10, '40°S', 26, 'end', 'normal', INK, halo=True)
    fig.text(MX + MW - 8, MY + 30, '40°N', 26, 'end', 'normal', INK, halo=True)
    ky = MY + MH + 44
    for i, (k, lab) in enumerate((('R', 'tropical rainforest'), ('S', 'savannah'), ('D', 'tropical desert'), ('other', 'other land'))):
        x = 30 + [0, 300, 500, 760][i]
        fig.rect(x, ky - 22, 30, 24, 'url(#dpat)' if k == 'D' else COL[k], INK, 1.2)
        fig.text(x + 40, ky, lab, 26)
    fig.text(30, ky + 40, 'Boundaries generalised and approximate. Coastlines: Natural Earth.', 26, 'start', 'normal', GREY)

    A = 'a'
    for lon, lat, lab, anchor in ((-62, -2, 'Amazon', 'middle'), (22, -1, 'Congo', 'middle'), (122, 2, 'SE Asia', 'start'),
                                  (5, 25, 'Sahara', 'middle'), (48, 22, 'Arabia', 'start'), (14, -30, 'Namib', 'end'),
                                  (128, -26, 'Australia', 'middle')):
        fig.text(X(lon), Y(lat) + 9, lab, 26, anchor, 'bold', INK, A, halo=True)
    fig.marker(X(-62), Y(8), '1', A)
    fig.marker(X(30), Y(-14), '2', A)
    fig.marker(X(20), Y(33), '3', A)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Interpretation', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for n, s in [('1', 'Rainforest lies near the Equator in separate blocks (Amazon, Congo, South-east Asia), not one continuous belt.'),
                 ('2', 'Savannah lies in the tropics on several continents, often between the rainforest and drier land (Africa, South America, northern Australia).'),
                 ('3', 'Tropical deserts lie mostly near the tropics (Sahara, Arabia, Australia), including west-coast deserts such as the Namib, not one uniform band.')]:
        fig.marker(52, yy - 9, n, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8

    hits = {k: [(name, zones[k].contains(Point(lon, lat))) for lon, lat, name in pts] for k, pts in CHECKPOINTS.items()}
    spec = {
        'kind': 'thematic world map (equirectangular), generalised vegetation classes',
        'extent': {'lon': [LON0, LON1], 'lat': [LAT0, LAT1]}, 'tropics_deg': 23.44,
        'coastline_source': {'name': 'Natural Earth 1:110m land (public domain)', 'url': 'https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_110m_land.geojson',
                             'local_copy': 'assets/sources/ne_110m_land.geojson', 'sha256': sha(LAND_SRC), 'retrieved': '2026-10-30'},
        'vegetation_zones': {'method': "author's generalisation of widely published biome maps; polygons in lon/lat, clipped to land; approximate",
                             'polygons_lonlat': ZONES},
        'checkpoint_tests': hits,
        'question_withholds': ['region names on the map'],
        'independent_solution': ['rainforest in separate low-latitude blocks (1)', 'savannah in tropical areas of several continents (1)',
                                 'deserts near the tropics incl. west-coast examples, not continuous (1)'],
    }
    checks = [
        check('known rainforest, savannah and desert locations fall in the right class', all(ok for v in hits.values() for n, ok in v), str(hits)),
        check('rainforest blocks are separate (more than one polygon)', getattr(zones['R'], 'geoms', None) is not None and len(zones['R'].geoms) >= 3),
        check('all rainforest lies within 15 degrees of the Equator', abs(zones['R'].bounds[1]) <= 15 and abs(zones['R'].bounds[3]) <= 17,
              str([round(b, 1) for b in zones['R'].bounds])),
        check('classes do not overlap', zones['S'].intersection(zones['R']).area < 1e-6 and zones['S'].intersection(zones['D']).area < 1e-6),
    ]
    sides = {
        'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'],
                     'forbidden': [r'Amazon', r'Congo', r'Sahara', r'Namib', r'Arabia']},
        'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']},
    }
    return build(RID, fig, spec, sides, checks)


if __name__ == '__main__':
    main()
