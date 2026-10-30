"""Shared Namibia base map for the two map-revision-01 resources (VIS-6137-2.2-02 and VIS-6137-2.6-02).

Layers and sources (local copies and SHA-256 in assets/sources/maps; acquired with the YYeni Web Harvester,
log _harvest/logs/harvest_log.csv, manifests _harvest/manifests/6137-map-revision-01-*.csv):
- regions: geoBoundaries gbHumanitarian NAM ADM1 (boundary ID NAM-ADM1-65246180), source Namibia Statistics
  Agency via OCHA HDX, licence CC BY 3.0 IGO, 14 regions. The gbOpen file named in the handover
  (NAM-ADM1-33880854, Natural Earth) was downloaded and checked first but holds only 13 pre-2013 regions
  ("Caprivi", a single "Kavango"), so it is not used. "Karas" is printed with its official name //Karas.
- neighbouring land: Natural Earth 1:110m land (public domain), the copy already used by VIS-6137-1.7-01.
- towns: GeoNames country dump NA.zip (CC BY 4.0); geonameid recorded per town.
Projection: equirectangular with longitude scaled by cos(22.5 deg S), so north-south distances are true
to the scale bar and east-west distances are within about 5 % across Namibia (stated on the figure).
"""
import json
import math
import os
import sys
import zipfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import INK, GREY, WS, sha  # noqa: E402
import shapefile  # noqa: E402
from shapely.geometry import shape, box  # noqa: E402
from shapely.ops import unary_union  # noqa: E402

SRC = os.path.join(WS, 'assets', 'sources', 'maps')
REGIONS = os.path.join(SRC, 'geoBoundaries-gbHumanitarian-NAM-ADM1.geojson')
REGIONS_META = os.path.join(SRC, 'geoBoundaries-gbHumanitarian-NAM-ADM1-metadata.json')
REJECTED_BASE = os.path.join(SRC, 'geoBoundaries-NAM-ADM1.geojson')
LAND = os.path.join(WS, 'assets', 'sources', 'ne_110m_land.geojson')
GEONAMES = os.path.join(SRC, 'geonames-NA.zip')
KM_PER_DEG = 111.32
COSPHI = math.cos(math.radians(22.5))
OFFICIAL = {'Karas': '//Karas'}
TOWN_IDS = {'Oshakati': 3354021, 'Rundu': 3353383, 'Katima Mulilo': 877178, 'Windhoek': 3352136, 'Otavi': 3353934,
            'Grootfontein': 3357114, 'Tsumeb': 3352593, 'Mariental': 3355595, 'Keetmanshoop': 3356264,
            'Otjiwarongo': 3353811, 'Opuwo': 3354077, 'Swakopmund': 3352844}


class Proj:
    def __init__(self, lon0, lat_top, px_per_unit, ox, oy):
        self.lon0, self.lat_top, self.k, self.ox, self.oy = lon0, lat_top, px_per_unit, ox, oy

    def xy(self, lon, lat):
        return self.ox + (lon - self.lon0) * COSPHI * self.k, self.oy + (self.lat_top - lat) * self.k

    def km_px(self, km):
        """Pixels for a north-south distance of `km`."""
        return km / KM_PER_DEG * self.k

    def path(self, geom, tol=0.0):
        g = geom.simplify(tol, preserve_topology=True) if tol else geom
        polys = [g] if g.geom_type == 'Polygon' else [p for p in getattr(g, 'geoms', []) if p.geom_type == 'Polygon']
        d = []
        for p in polys:
            if p.is_empty:
                continue
            for ring in [p.exterior] + list(p.interiors):
                d.append('M' + ' L'.join('%.1f %.1f' % self.xy(x, y) for x, y in ring.coords) + ' Z')
        return ' '.join(d)

    def line_path(self, geom, tol=0.0):
        g = geom.simplify(tol) if tol else geom
        lines = [g] if g.geom_type == 'LineString' else list(getattr(g, 'geoms', []))
        return ' '.join('M' + ' L'.join('%.1f %.1f' % self.xy(x, y) for x, y in ln.coords) for ln in lines)


def regions():
    feats = json.load(open(REGIONS))['features']
    return {OFFICIAL.get(f['properties']['shapeName'], f['properties']['shapeName']): shape(f['geometry']).buffer(0) for f in feats}


def namibia(regs=None):
    return unary_union(list((regs or regions()).values()))


def land(bounds):
    return unary_union([shape(f['geometry']) for f in json.load(open(LAND))['features']]).intersection(box(*bounds))


def towns(names):
    rows = {}
    with zipfile.ZipFile(GEONAMES) as z:
        for line in z.read('NA.txt').decode('utf-8').splitlines():
            r = line.split('\t')
            rows[int(r[0])] = r
    out = {}
    for n in names:
        r = rows[TOWN_IDS[n]]
        assert r[1] == n, (n, r[1])
        out[n] = (float(r[5]), float(r[4]), TOWN_IDS[n])
    return out


def base_sources():
    meta = json.load(open(REGIONS_META))
    rej = json.load(open(REJECTED_BASE))['features']
    return {
        'regions': {'dataset': 'geoBoundaries gbHumanitarian NAM ADM1', 'boundaryID': meta['boundaryID'], 'source': meta['boundarySource'],
                    'licence': meta['boundaryLicense'], 'year_represented': meta['boundaryYearRepresented'], 'units': len(json.load(open(REGIONS))['features']),
                    'url': meta['gjDownloadURL'], 'metadata_url': 'https://www.geoboundaries.org/api/current/gbHumanitarian/NAM/ADM1/',
                    'local_copy': os.path.relpath(REGIONS, WS), 'sha256': sha(REGIONS), 'retrieved': '2026-10-30',
                    'attribution': 'Namibia Statistics Agency via OCHA HDX / geoBoundaries (CC BY 3.0 IGO)'},
        'rejected_regions': {'dataset': 'geoBoundaries gbOpen NAM ADM1 NAM-ADM1-33880854 (named in the handover)', 'local_copy': os.path.relpath(REJECTED_BASE, WS),
                             'sha256': sha(REJECTED_BASE), 'units_in_file': len(rej),
                             'names_in_file': sorted(f['properties']['shapeName'] for f in rej),
                             'reason': 'pre-2013 regions: Caprivi (now Zambezi) and a single Kavango (now Kavango East and West)'},
        'neighbouring_land': {'name': 'Natural Earth 1:110m land (public domain)', 'local_copy': os.path.relpath(LAND, WS), 'sha256': sha(LAND)},
        'towns': {'name': 'GeoNames NA.zip country dump (CC BY 4.0)', 'url': 'https://download.geonames.org/export/dump/NA.zip',
                  'local_copy': os.path.relpath(GEONAMES, WS), 'sha256': sha(GEONAMES), 'retrieved': '2026-10-30'},
        'projection': 'equirectangular, longitude scaled by cos(22.5 deg); scale bar true north-south, east-west within about 5 %',
    }


def shapes(path, keep=None):
    r = shapefile.Reader(path, encoding='latin1')
    out = []
    for sr in r.iterShapeRecords():
        if sr.shape.shapeType == 0 or not sr.shape.points:
            continue
        rec = sr.record.as_dict()
        if keep is None or keep(rec):
            out.append((shape(sr.shape.__geo_interface__).buffer(0) if sr.shape.shapeType in (5, 15, 25) else shape(sr.shape.__geo_interface__), rec))
    return out


def north_arrow(fig, x, y, layer='base'):
    fig.poly([(x, y - 34), (x - 13, y + 8), (x, y), (x + 13, y + 8)], INK, INK, 1.5, layer=layer)
    fig.text(x, y - 44, 'N', 28, 'middle', 'bold', layer=layer)


def scale_bar(fig, proj, x, y, km=(0, 100, 200, 300), layer='base'):
    for i in range(len(km) - 1):
        x0, x1 = x + proj.km_px(km[i]), x + proj.km_px(km[i + 1])
        fig.rect(x0, y, x1 - x0, 12, INK if i % 2 == 0 else '#ffffff', INK, 1.5, layer=layer)
    for v in km:
        fig.text(x + proj.km_px(v), y + 42, str(v), 26, 'middle', layer=layer)
    fig.text(x + proj.km_px(km[-1]) + 30, y + 42, 'km', 26, 'start', layer=layer)
