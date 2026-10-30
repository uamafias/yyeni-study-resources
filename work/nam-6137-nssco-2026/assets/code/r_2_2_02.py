"""VIS-6137-2.2-02 -> ITEM-6137-2.2-013-INTERP (assigned); approved bindings 014, 015 and 016 (map-revision-01).

Original thematic map of Namibian farming built from open data, not traced from any atlas or examination map:
- base: namibia_map.py (NSA regions via geoBoundaries, Natural Earth land, GeoNames towns);
- farming-system areas: Atlas of Namibia (2022) figure 8.02 data, "farming system areas" shapefile, from
  Mendelsohn 2006 Farming Systems in Namibia (RAISON); four classes, clipped to the NSA outline;
- crop fields: Atlas figure 8.06 national cleared-land polygons (cleared_land.shp, Atlas of Namibia 2022; the file
  records no survey date), gridded here into 0.1-degree cells; a cell is shaded where fields cover at least 15 %
  of it. The region-level 1996-97 grids were not used: the north-central one is too coarse. The Atlas states that
  about 90 % of cleared land belongs to smallholders who mainly eat their harvests;
- commercial farms: Atlas figure 8.07 farm cadastre (MEFT, 9,168 farms), dissolved and outlined;
- irrigation: Atlas figure 8.02 AGRI_Irrigation_areas points with at least 50 ha irrigated in that dataset
  (Mendelsohn 2006 / NAU); nearby points merged; the key does not claim current operation;
- Otavi-Grootfontein-Tsumeb crop area: the triangle joining the three GeoNames town points (Atlas 8.02 text:
  maize and sunflowers grown on rain-fed and irrigated fields in this area).
Atlas of Namibia: CC BY 4.0, (c) Namibia Nature Foundation; data from the Environmental Information Service.
Card 015's inset is explicitly schematic: one plot keyed "vegetables for sale" beside a town, neighbouring plots
keyed only "cultivated, purpose not shown".
One common question map; a separate answer side for each bound card.
"""
import json
import os
import sys
import warnings
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, WS, sha, build, check  # noqa: E402
import namibia_map as NM  # noqa: E402
from namibia_map import shapes  # noqa: E402
from shapely.geometry import shape, Point, Polygon, box  # noqa: E402
from shapely.ops import unary_union  # noqa: E402
warnings.filterwarnings('ignore')

RID = 'VIS-6137-2.2-02'
ITEM = 'ITEM-6137-2.2-013-INTERP'
B14, B15, B16 = 'ITEM-6137-2.2-014-INTERP', 'ITEM-6137-2.2-015-INTERP', 'ITEM-6137-2.2-016-INTERP'
W, HQ = 1000, 1425
HA = {'answer': 1875, 'answer_014': 1875, 'answer_015': 1845, 'answer_016': 1875}
LON0, LON1, LAT_TOP, LAT_BOT = 11.4, 25.6, -16.0, -29.1
K = 960 / ((LON1 - LON0) * NM.COSPHI)
P = NM.Proj(LON0, LAT_TOP, K, 20, 62)
MAP_H = (LAT_TOP - LAT_BOT) * K
ATLAS = os.path.join(NM.SRC, 'atlas')
F802 = os.path.join(ATLAS, 'Figure 8_02 Major farm products and land uses')
F806 = os.path.join(ATLAS, 'Figure 8_06 Proportions of land cleared for crop farming')
F807 = os.path.join(ATLAS, 'Figure 8_07 Game farming 2020')
CLASSES = [('Mixed livestock and dryland cereal farming', 'cereal', 'Dryland crops with livestock'),
           ('Extensive cattle farming', 'cattle', 'Mainly cattle'),
           ('Mixed cattle and small stock farming', 'mixed', 'Cattle with sheep and goats'),
           ('Extensive small-stock farming', 'small', 'Mainly sheep and goats')]
FILL = {'cereal': '#f0d97a', 'cattle': '#9fc275', 'mixed': 'url(#mixpat)', 'small': 'url(#smallpat)', 'none': '#fbfbf8'}
FIELDS, EDGE, IRR = '#2f6b2f', '#3b2a1a', '#1f5f99'
TOWNS = ['Oshakati', 'Rundu', 'Katima Mulilo', 'Windhoek', 'Otavi', 'Grootfontein', 'Tsumeb', 'Mariental', 'Keetmanshoop']
NC = ['Omusati', 'Oshana', 'Ohangwena', 'Oshikoto']
ATLAS_ZIPS = {'8.02': 'Atlas_ch_08_02.zip', '8.06': 'Atlas_ch_08_06.zip', '8.07': 'Atlas_ch_08_07.zip'}


def crop_cells(nam, step=0.1, threshold=0.15):
    """Grid the Atlas national cleared-land polygons into 0.1-degree cells; keep cells whose fields cover >= 15 %."""
    from shapely.strtree import STRtree
    cl = [g for g, r in shapes(os.path.join(F806, 'cleared_land.shp'))]
    tree = STRtree(cl)
    keep = []
    for i in range(int(round((25.3 - 11.7) / step))):
        for j in range(int(round((-16.9 + 29.0) / step))):
            x, y = round(11.7 + i * step, 2), round(-29.0 + j * step, 2)
            c = box(x, y, x + step, y + step)
            idx = tree.query(c)
            if len(idx) and c.intersects(nam) and sum(cl[k].intersection(c).area for k in idx) / c.area >= threshold:
                keep.append(c)
    return unary_union(keep).intersection(nam), len(keep)


def irrigation():
    pts = sorted(shapes(os.path.join(F802, 'AGRI_Irrigation_areas.shp'), lambda r: (r['IRRIGATED_'] or 0) >= 50),
                 key=lambda t: -t[1]['IRRIGATED_'])
    kept = []
    for g, r in pts:
        if all(g.distance(k[0]) > 0.25 for k in kept):
            kept.append((g, r, [r['NAME']]))
        else:
            next(k for k in kept if g.distance(k[0]) <= 0.25)[2].append(r['NAME'])
    return kept


def answer_panel(fig, layer, top, height, items):
    fig.rect(16, top + 6, W - 32, height - 16, '#f4faf6', C['answer'], 2, 8, layer)
    fig.text(36, top + 46, 'Interpretation', 28, 'start', 'bold', C['answer'], layer)
    yy = top + 90
    for k, s in items:
        fig.marker(52, yy - 9, k, layer)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=layer) + 8
    assert yy <= top + height - 10, (layer, yy, top + height)
    return yy


def main(render=True):
    regs = NM.regions()
    nam = NM.namibia(regs)
    land = NM.land((LON0, LAT_BOT, LON1, LAT_TOP)).difference(nam)
    fsys = {}
    for name, key, _ in CLASSES:
        fsys[key] = unary_union([g for g, r in shapes(os.path.join(F802, 'farming system areas.shp'), lambda r, n=name: r['LANDUSE'] == n)]).intersection(nam)
    fields, ncells = crop_cells(nam)
    comm = unary_union([g.buffer(0.01) for g, r in shapes(os.path.join(F807, 'Tourism_Conservation Farms.shp'))]).buffer(-0.01)
    comm = unary_union([p for p in getattr(comm, 'geoms', [comm]) if p.area > 0.05]).intersection(nam)
    irr = irrigation()
    towns = NM.towns(TOWNS)
    tri = Polygon([towns[t][:2] for t in ('Otavi', 'Grootfontein', 'Tsumeb')])

    fig = Fig(W, dict({'question': HQ}, **HA), 'Farming in Namibia')
    fig.pattern('mixpat', '<rect width="14" height="14" fill="#9fc275"/><path d="M0 14 L14 0 M-4 4 L4 -4 M10 18 L18 10" stroke="#e7b9a2" stroke-width="5"/>', 14, 14)
    fig.pattern('smallpat', '<rect width="12" height="12" fill="#f0d2c2"/><circle cx="3" cy="3" r="1.6" fill="#8a4b2f"/><circle cx="9" cy="9" r="1.6" fill="#8a4b2f"/>', 12, 12)
    fig.pattern('tripat', '<rect width="8" height="8" fill="#ffffff" fill-opacity="0.55"/><path d="M0 8 L8 0 M-2 2 L2 -2 M6 10 L10 6" stroke="#1a1a1a" stroke-width="1.6"/>', 8, 8)
    fig.pattern('vegpat', '<rect width="10" height="10" fill="#4f9a3a"/><circle cx="5" cy="5" r="2" fill="#ffffff"/>', 10, 10)
    fig.rect(P.ox, P.oy, 960, MAP_H, '#dceefa', INK, 2)
    fig.path(P.path(land, 0.02), '#e2e2de', '#9a9a9a', 1)
    fig.path(P.path(nam, 0.005), FILL['none'], 'none', 0)
    for key in ('cereal', 'cattle', 'mixed', 'small'):
        fig.path(P.path(fsys[key], 0.01), FILL[key], 'none', 0)
    fig.path(P.path(fields, 0.002), FIELDS, 'none', 0)
    for n, g in regs.items():
        fig.path(P.path(g, 0.01), 'none', '#7c7c7c', 1.2)
    fig.path(P.path(comm, 0.01), 'none', '#ffffff', 7)
    fig.path(P.path(comm, 0.01), 'none', EDGE, 3.5)
    fig.path(P.path(nam, 0.005), 'none', INK, 2.2)
    fig.path(P.path(tri), 'url(#tripat)', INK, 2.5)
    for g, r, names in irr:
        x, y = P.xy(g.x, g.y)
        fig.circle(x, y, 9, IRR, '#ffffff', 2.5)
    for t, (lon, lat, gid) in towns.items():
        x, y = P.xy(lon, lat)
        fig.rect(x - 6, y - 6, 12, 12, INK, '#ffffff', 2)
    off = {'Oshakati': (-12, 9, 'end'), 'Rundu': (0, -18, 'middle'), 'Katima Mulilo': (-12, -16, 'end'), 'Windhoek': (12, 9, 'start'),
           'Otavi': (-12, 24, 'end'), 'Grootfontein': (14, 22, 'start'), 'Tsumeb': (-12, -12, 'end'), 'Mariental': (14, 9, 'start'),
           'Keetmanshoop': (8, 32, 'start')}
    for t, (lon, lat, gid) in towns.items():
        x, y = P.xy(lon, lat)
        dx, dy, an = off[t]
        fig.text(x + dx, y + dy, t, 26, an, 'bold', INK, halo=True)
    # north-central region labels in the Angola strip, with leader lines to a point inside each region
    lab = {'Omusati': (14.2, -16.55, 14.55, -18.3), 'Oshana': (15.45, -16.95, 15.7, -18.1),
           'Ohangwena': (16.95, -16.55, 16.9, -17.6), 'Oshikoto': (18.3, -16.95, 17.4, -18.35)}
    for n, (lx, ly, tx, ty) in lab.items():
        x0, y0 = P.xy(lx, ly)
        x1, y1 = P.xy(tx, ty)
        assert regs[n].contains(Point(tx, ty)), n
        fig.line(x0, y0 + 6, x1, y1, INK, 1.6)
        fig.circle(x1, y1, 4, INK, '#ffffff', 1.5)
        fig.text(x0, y0, n, 26, 'middle', 'bold', INK, halo=True)
    for n, (lon, lat) in {'Kunene': (13.2, -18.9), 'Erongo': (15.0, -21.7), 'Otjozondjupa': (19.0, -20.3), 'Omaheke': (19.9, -21.55),
                          'Khomas': (16.4, -23.25), 'Hardap': (16.0, -24.6), '//Karas': (16.55, -27.2), 'Zambezi': (24.6, -18.0)}.items():
        assert regs[n].contains(Point(lon, lat)), n
        x, y = P.xy(lon, lat)
        fig.text(x, y + 9, n, 26, 'middle', 'normal', '#4d4d4d', halo=True, italic=True)
    for n, (lon, lat) in {'ANGOLA': (20.9, -16.45), 'BOTSWANA': (22.7, -20.6), 'SOUTH AFRICA': (22.9, -28.6),
                          'ZAMBIA': (24.6, -16.45), 'Atlantic Ocean': (12.9, -25.0)}.items():
        x, y = P.xy(lon, lat)
        fig.text(x, y + 9, n, 26, 'middle', 'normal', GREY, italic=n.startswith('Atl'), rotate=-90 if n.startswith('Atl') else None)
    NM.north_arrow(fig, 70, 520)
    NM.scale_bar(fig, P, 40, P.oy + MAP_H - 66)

    # inset for card 015: explicitly schematic, not linked to a real town or farm
    ix, iy, iw, ih = 676, 418, 300, 520
    fig.rect(ix, iy, iw, ih, '#ffffff', INK, 2.5)
    fig.lines(ix + 14, iy + 34, ['Inset: plots beside', 'a northern town', '(schematic, not a', 'surveyed farm)'], 26, 30, weight='bold')
    gx, gy = ix + 14, iy + 152
    fig.rect(gx, gy, 272, 176, '#f4f1e6', '#9a9a9a', 1)
    fig.rect(gx + 6, gy + 8, 88, 70, '#c9c9c9', INK, 1.5)
    fig.text(gx + 50, gy + 52, 'Town', 26, 'middle', 'bold')
    fig.line(gx, gy + 98, gx + 272, gy + 98, '#ffffff', 12)
    fig.line(gx, gy + 98, gx + 272, gy + 98, '#8a8a8a', 6)
    sale = (gx + 104, gy + 12, 70, 68)
    fig.rect(*sale, 'url(#vegpat)', INK, 2)
    for (px, py, pw, ph) in ((gx + 184, gy + 12, 80, 68), (gx + 8, gy + 114, 78, 54), (gx + 96, gy + 114, 82, 54), (gx + 188, gy + 114, 76, 54)):
        fig.rect(px, py, pw, ph, '#e3cf8f', INK, 1.5)
    ky = gy + 214
    fig.rect(ix + 14, ky - 22, 34, 26, 'url(#vegpat)', INK, 1.5)
    fig.lines(ix + 58, ky, ['Vegetables', 'for sale'], 26, 30)
    fig.rect(ix + 14, ky + 48, 34, 26, '#e3cf8f', INK, 1.5)
    fig.lines(ix + 58, ky + 70, ['Cultivated:', 'purpose not shown'], 26, 30)
    fig.line(ix + 14, ky + 124, ix + 48, ky + 124, '#8a8a8a', 6)
    fig.text(ix + 58, ky + 133, 'Road', 26)
    assert ky + 133 < iy + ih - 8

    # key
    ky0 = P.oy + MAP_H + 46
    fig.text(30, ky0, 'Key', 28, 'start', 'bold')
    rows1 = [(FILL['cereal'], CLASSES[0][2]), (FILL['cattle'], CLASSES[1][2]), (FILL['mixed'], CLASSES[2][2]),
             (FILL['small'], CLASSES[3][2]), (FILL['none'], 'Little or no farming')]
    for i, (fl, s) in enumerate(rows1):
        y = ky0 + 22 + i * 40
        fig.rect(30, y, 44, 28, fl, INK, 1.2)
        fig.text(86, y + 23, s, 26)
    x2 = 520
    y = ky0 + 22
    fig.rect(x2, y, 44, 28, FIELDS, INK, 1.2)
    fig.text(x2 + 56, y + 23, 'Crop fields ≥15% of land', 26)
    y += 40
    fig.line(x2, y + 14, x2 + 44, y + 14, EDGE, 4)
    fig.text(x2 + 56, y + 23, 'Edge of commercial farms', 26)
    y += 40
    fig.rect(x2, y, 44, 28, 'url(#tripat)', INK, 2)
    fig.text(x2 + 56, y + 23, 'Otavi–Grootfontein–Tsumeb', 26)
    y += 40
    fig.circle(x2 + 22, y + 14, 9, IRR, '#ffffff', 2.5)
    fig.text(x2 + 56, y + 23, 'Irrigation area (location)', 26)
    y += 40
    fig.rect(x2 + 16, y + 8, 12, 12, INK, '#ffffff', 2)
    fig.line(x2 + 32, y + 14, x2 + 44, y + 14, '#7c7c7c', 1.2)
    fig.text(x2 + 56, y + 23, 'Town; region boundary', 26)
    sy = ky0 + 250
    for s in ['Generalised. Farming areas, crop fields, farms and irrigation:',
              'Atlas of Namibia 2022 data (CC BY 4.0). Regions: NSA (CC BY',
              '3.0 IGO). Towns: GeoNames. East–west scale within 5%.']:
        fig.text(30, sy, s, 26, 'start', 'normal', GREY)
        sy += 32
    assert sy <= HQ, sy

    # ---- answer sides: one per bound card -------------------------------------------------------
    def mk(lon, lat, k, layer):
        x, y = P.xy(lon, lat)
        fig.marker(x, y, k, layer)

    A13, A14, A15, A16 = 'a', 'a14', 'a15', 'a16'
    mk(15.9, -17.75, '1', A13)
    mk(17.4, -21.0, '2', A13)
    mk(17.0, -26.4, '2', A13)
    mk(18.25, -24.0, '3', A13)
    mk(17.95, -28.2, '3', A13)
    answer_panel(fig, A13, HQ, HA['answer'] - HQ, [
        ('1', 'Dryland crops and dense crop fields lie across the north, densest in the north-central regions, with more along the northern border near Rundu and in Zambezi.'),
        ('2', 'Inside the commercial farms, central areas are mainly cattle; farther south (Hardap, //Karas) sheep and goats dominate, with mixed areas between.'),
        ('3', 'Irrigation areas, e.g. near Mariental and on the southern border (the Orange River), are local crop sites inside livestock areas: exceptions to the north–south pattern.')])
    for n, (lon, lat) in {'1': (16.3, -17.7), '2': (20.3, -17.95), '3': (14.4, -18.8)}.items():
        mk(lon, lat, n, A14)
    mk(23.4, -17.8, '2', A14)
    answer_panel(fig, A14, HQ, HA['answer_014'] - HQ, [
        ('1', 'The largest block of crop-field cells covers Oshana, eastern Omusati, western Ohangwena and north-western Oshikoto: a north-central cluster by the Angolan border.'),
        ('2', 'Farther east, crop fields form narrower patches along the northern border near Rundu and in Zambezi.'),
        ('3', 'Fields thin out westwards across Omusati and are almost absent in Kunene. The cells show where fields are dense (mostly household farms), not the purpose of every field.')])
    sx, sy0 = sale[0] + sale[2] / 2, sale[1] + sale[3] / 2
    fig.circle(sx, sy0, 44, 'none', C['answer'], 5, A15)
    fig.marker(sale[0] + sale[2] + 2, sale[1] - 2, '1', A15)
    fig.marker(sale[0] + sale[2] / 2, gy + 98, '2', A15)
    fig.marker(gx + 140, gy + 150, '3', A15)
    answer_panel(fig, A15, HQ, HA['answer_015'] - HQ, [
        ('1', 'One small plot is keyed vegetables for sale: a small-scale cash-crop site.'),
        ('2', 'It lies next to the town and beside the road, close to buyers and transport.'),
        ('3', 'The other plots are keyed only as cultivated, so the inset does not show whether they are sold or used at home: it shows one sale site, not a cash-crop belt.')])
    mk(15.6, -19.75, '1', A16)
    mk(18.4, -21.0, '2', A16)
    mk(17.0, -26.4, '2', A16)
    mk(17.75, -19.95, '3', A16)
    answer_panel(fig, A16, HQ, HA['answer_016'] - HQ, [
        ('1', 'Commercial farms cover most of central and southern Namibia; their northern edge runs south of Etosha and the northern communal lands.'),
        ('2', 'They produce different livestock: mainly cattle in central areas (Otjozondjupa, Omaheke, Khomas) but mainly sheep and goats in Hardap and //Karas.'),
        ('3', 'The hatched Otavi–Grootfontein–Tsumeb triangle is a crop area far inland, inside the central cattle zone and not near the coast.')])

    # ---- independent checks of the statements the answers make --------------------------------
    def share(geom, region):
        return geom.intersection(regs[region]).area / regs[region].area
    nc = {n: round(share(fields, n), 3) for n in NC + ['Kavango West', 'Kavango East', 'Zambezi', 'Kunene']}
    in_comm = {n: {k: round(fsys[k].intersection(regs[n]).intersection(comm).area / max(regs[n].intersection(comm).area, 1e-9), 2) for k in fsys}
               for n in ('Otjozondjupa', 'Omaheke', 'Khomas', 'Hardap', '//Karas')}
    om = regs['Omusati']

    def band(n, x0, x1):
        b = regs[n].intersection(box(x0, -20, x1, -17))
        return fields.intersection(b).area / b.area
    west_om = fields.intersection(om).intersection(box(13, -20, 14.6, -17)).area / om.intersection(box(13, -20, 14.6, -17)).area
    east_om = fields.intersection(om).intersection(box(14.6, -20, 16, -17)).area / om.intersection(box(14.6, -20, 16, -17)).area
    irr_near = lambda lon, lat: min(Point(lon, lat).distance(g) for g, r, n in irr)
    checks = [
        check('all 14 NSA regions present with current names', set(regs) == {'Zambezi', 'Erongo', 'Hardap', '//Karas', 'Kavango East', 'Khomas', 'Kunene', 'Ohangwena', 'Omaheke',
                                                                             'Omusati', 'Oshana', 'Oshikoto', 'Otjozondjupa', 'Kavango West'}),
        check('north-central regions each have a larger share of dense crop cells than Kunene and either Kavango region', min(nc[n] for n in NC) > max(nc['Kunene'], nc['Kavango West'], nc['Kavango East']), str(nc)),
        check('Ohangwena and Oshana have the largest dense-crop shares', sorted(nc, key=nc.get)[-2:] in (['Oshana', 'Ohangwena'], ['Ohangwena', 'Oshana']), str(nc)),
        check('crop cells exist along the Kavango (both regions) and in Zambezi', nc['Kavango West'] > 0.02 and nc['Kavango East'] > 0.02 and nc['Zambezi'] > 0.05, str(nc)),
        check('commercial farms in central regions are mainly cattle', all(in_comm[n]['cattle'] >= 0.5 for n in ('Otjozondjupa', 'Omaheke', 'Khomas')), str(in_comm)),
        check('commercial farms in Hardap and //Karas are mainly small stock with mixed areas', all(in_comm[n]['small'] >= 0.5 and in_comm[n]['mixed'] > 0.2 for n in ('Hardap', '//Karas')), str(in_comm)),
        check('no farming class overlaps another', all(fsys[a].intersection(fsys[b]).area < 0.01 for a in fsys for b in fsys if a < b)),
        check('commercial farmland lies south of the northern crop belt; its few dense crop cells are in the Otavi-Grootfontein-Tsumeb area or at irrigation points',
              comm.bounds[3] < -18.5 and all(p.distance(tri) < 0.35 or min(p.distance(g) for g, r, n in irr) < 0.3
                                             for p in getattr(fields.intersection(comm), 'geoms', []) if p.area > 0.002),
              'north edge %.2f; share of crop cells inside commercial farms %.3f' % (comm.bounds[3], fields.intersection(comm).area / fields.area)),
        check('maize triangle lies inside the cattle class and over 300 km from Swakopmund on the coast', fsys['cattle'].buffer(0.05).contains(tri) and tri.distance(Point(14.53, -22.68)) * NM.KM_PER_DEG * NM.COSPHI > 300, '%.0f km' % (tri.distance(Point(14.53, -22.68)) * NM.KM_PER_DEG * NM.COSPHI)),
        check('Otavi-Grootfontein-Tsumeb triangle lies inside the commercial farmland', comm.buffer(0.02).contains(tri)),
        check('irrigation points near Mariental (Hardap) and on the Orange River', irr_near(17.86, -24.32) < 0.05 and irr_near(17.56, -28.44) < 0.05),
        check('answer markers lie in the classes they point to', fsys['cattle'].contains(Point(17.4, -21.0)) and fsys['small'].contains(Point(17.0, -26.4)) and fsys['cereal'].contains(Point(15.9, -17.75))
              and fields.contains(Point(16.3, -17.7)) and fsys['small'].contains(Point(17.0, -26.4)) and fsys['cattle'].contains(Point(18.4, -21.0))),
        check('crop marker 2 points at fields on the Kavango near Rundu and in Zambezi', fields.distance(Point(20.3, -17.95)) < 0.1 and fields.distance(Point(23.4, -17.8)) < 0.1),
        check('crop block covers western Ohangwena and north-western Oshikoto, not their eastern parts', band('Ohangwena', 15.5, 16.5) > 0.8 and band('Ohangwena', 17.0, 18.0) < 0.1
              and band('Oshikoto', 16.0, 17.0) > 0.25 and band('Oshikoto', 17.0, 18.5) < 0.05,
              str([round(band(*a), 2) for a in (('Ohangwena', 15.5, 16.5), ('Ohangwena', 17.0, 18.0), ('Oshikoto', 16.0, 17.0), ('Oshikoto', 17.0, 18.5))])),
        check('crop cells thin out westwards across Omusati and are absent from Kunene',
              west_om < 0.5 * east_om and nc['Kunene'] == 0, 'Omusati west of 14.6 E %.2f, east of 14.6 E %.2f' % (west_om, east_om)),
    ]
    spec = {
        'kind': 'original thematic map of Namibia from open data (no examination or atlas map traced)',
        'base': NM.base_sources(),
        'thematic_sources': {
            'atlas': {'citation': 'Atlas of Namibia Team, 2022, Atlas of Namibia: its land, water and life, Namibia Nature Foundation, Windhoek',
                      'licence': 'CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/), stated on https://atlasofnamibia.online/chapter-8/farming',
                      'text_used': 'chapter 8 farming page, read 2026-10-30: central cattle and southern sheep/goats; 60-80 % of sheep in Hardap and ||Kharas; '
                                   'largest crop clearing in central northern Namibia; about 90 % of cleared land belongs to smallholders; '
                                   'maize and sunflowers in the Otavi-Grootfontein-Tsumeb area; irrigation along the Orange River, Hardap Dam, Kunene and Okavango rivers'},
            'data_zips': {k: {'url': 'https://the-eis.com/elibrary/sites/default/files/downloads/literature/' + v,
                              'local_copy': os.path.relpath(os.path.join(ATLAS, v), WS), 'sha256': sha(os.path.join(ATLAS, v))} for k, v in ATLAS_ZIPS.items()},
            'farming_system_areas': 'Figure 8_02/farming system areas.shp (from Mendelsohn 2006, Farming Systems in Namibia, RAISON)',
            'crop_fields': {'file': 'Figure 8_06/cleared_land.shp', 'method': '0.1-degree grid, cells with >= 15 % cleared', 'cells': ncells,
                            'date_limit': 'the national file records no survey date; the Atlas region grids date from 1996-2018'},
            'commercial_farms': 'Figure 8_07/Tourism_Conservation Farms.shp (MEFT farm cadastre, 9,168 farms), dissolved; parts under 0.05 sq deg dropped',
            'irrigation': {'file': 'Figure 8_02/AGRI_Irrigation_areas.shp', 'rule': '>= 50 ha irrigated in the dataset; points within 0.25 deg merged',
                           'points': [{'lon': g.x, 'lat': g.y, 'merged': n} for g, r, n in irr], 'limit': 'locations only; current operation not shown'},
            'maize_triangle': 'triangle joining the GeoNames points of Otavi, Grootfontein and Tsumeb',
        },
        'measured': {'dense_crop_share_by_region': nc, 'class_shares_inside_commercial_farms': in_comm},
        'inset_015': 'schematic only: one plot keyed vegetables for sale beside a town and road; four plots keyed cultivated, purpose not shown',
        'question_withholds': ['interpretation panels and markers'],
        'independent_solution': {
            ITEM: ['northern crop belt, densest north-central (1)', 'central cattle to southern small stock inside commercial farms (1)', 'irrigation sites as local exceptions (1)'],
            B14: ['north-central cluster, Ohangwena/Oshana/eastern Omusati, thinning into Oshikoto (1)', 'named regions or eastern Kavango/Zambezi evidence (1)', 'qualified extent: few fields in the west; density not purpose (1)'],
            B15: ['keyed sale plot = small-scale cash crop (1)', 'beside town and road (1)', 'neighbouring plots purpose not shown (1)'],
            B16: ['commercial farms over central and south (1)', 'cattle centre vs sheep/goats south (1)', 'inland Otavi-Grootfontein-Tsumeb crop area (1)']},
    }
    if not render:
        return fig, spec, checks
    q = [r'Interpretation', r'densest', r'cluster', r'dominate']
    sides = {
        'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'], 'forbidden': q},
        'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': [A13]},
        'answer_014': {'path': 'assets/images/%s-%s-answer.png' % (B14, RID), 'layers': [A14], 'bound_item': B14},
        'answer_015': {'path': 'assets/images/%s-%s-answer.png' % (B15, RID), 'layers': [A15], 'bound_item': B15},
        'answer_016': {'path': 'assets/images/%s-%s-answer.png' % (B16, RID), 'layers': [A16], 'bound_item': B16},
    }
    panels = [(16, HQ + 6, W - 32, HA[k] - HQ - 16) for k in HA]
    return build(RID, fig, spec, sides, checks, panels=panels)


if __name__ == '__main__':
    main()
