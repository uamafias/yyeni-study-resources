"""Shared geometry for the 4.2 training maps (VIS-6137-4.2-01 to -04).

One generated terrain, one road network and one map scale are used by every 4.2 map panel, so all
contour, spot-height, distance and bearing statements come from the same world
(topics/4.2/authoring_notes.json map_geometry):
- local grid: x east, y grid north, metres; A (2000, 2000), B (4000, 2000), C (4000, 4000), D (2000, 4000);
- terrain: plain at 1,490 m with one asymmetric hill summit at B (1,540 m). The western spread is solved
  so that h(A) = 1,500 m exactly; the eastern and northern slopes are steeper than the western and
  southern ones, so contour spacing varies around the hill;
- scale 1:50,000 at the declared print width: 1 cm = 500 m, so 0.1 px per metre when the 1,000 px image
  is printed 20 cm wide (50 px per cm);
- the curved A-B road is a half-sine bump south of the A-B line whose amplitude is solved numerically
  for a ground length of exactly 3,000 m (6 cm on the map).
Contours are traced by bisection along rays from the summit (every contour drawn is closed and
star-shaped about B because h falls monotonically along each ray).
The coordinate panel (VIS-6137-4.2-04) uses a Transverse Mercator projection on the WGS84 ellipsoid
(Snyder 1987, eqs 8-9 to 8-13), central meridian 17 deg 01' E, origin latitude 23 deg 01' S, k0 = 1.
"""
import math

PX_PER_M = 0.1                   # 1:50,000 at 50 px per cm
PRINT_WIDTH_CM = 20
PTS = {'A': (2000, 2000), 'B': (4000, 2000), 'C': (4000, 4000), 'D': (2000, 4000)}
BASE, PEAK = 1490.0, 1540.0
SIG_W = 2000 / math.sqrt(2 * math.log(5))     # gives h(A) = 1500 exactly
SIG_E, SIG_N, SIG_S = 800.0, 900.0, 1000.0
LEVELS = [1500, 1510, 1520, 1530]
INTERVAL_M = 10


def height(x, y):
    bx, by = PTS['B']
    dx, dy = x - bx, y - by
    sx = SIG_W if dx < 0 else SIG_E
    sy = SIG_S if dy < 0 else SIG_N
    return BASE + (PEAK - BASE) * math.exp(-((dx / sx) ** 2 + (dy / sy) ** 2) / 2)


def contour(level, n=180):
    """Closed contour at `level` as a list of (x, y) ground points (metres)."""
    bx, by = PTS['B']
    out = []
    for i in range(n):
        th = 2 * math.pi * i / n
        lo, hi = 0.0, 8000.0
        for _ in range(60):
            mid = (lo + hi) / 2
            if height(bx + mid * math.cos(th), by + mid * math.sin(th)) > level:
                lo = mid
            else:
                hi = mid
        out.append((bx + lo * math.cos(th), by + lo * math.sin(th)))
    return out


def road_ab(n=400):
    """A -> B road: x = 2000 + 2000 t, y = 2000 - a sin(pi t); a solved for length 3,000 m."""
    def pts(a):
        return [(2000 + 2000 * i / n, 2000 - a * math.sin(math.pi * i / n)) for i in range(n + 1)]

    def length(p):
        return sum(math.dist(p[i], p[i + 1]) for i in range(len(p) - 1))
    lo, hi = 0.0, 3000.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if length(pts(mid)) < 3000:
            lo = mid
        else:
            hi = mid
    p = pts(lo)
    return p, lo, length(p)


def path_length(p):
    return sum(math.dist(p[i], p[i + 1]) for i in range(len(p) - 1))


def to_px(x, y, x0, y0, ox, oy, h_m):
    """Ground (x, y) -> SVG px for a panel whose ground window starts at (x0, y0) with height h_m,
    drawn with its top-left corner at (ox, oy)."""
    return ox + (x - x0) * PX_PER_M, oy + (y0 + h_m - y) * PX_PER_M


# ---- Transverse Mercator (WGS84) for the coordinate panel ----------------------------------------
A_WGS = 6378137.0
F_WGS = 1 / 298.257223563
E2 = F_WGS * (2 - F_WGS)
EP2 = E2 / (1 - E2)
LON0 = math.radians(17 + 1 / 60)
LAT0 = math.radians(-(23 + 1 / 60))


def _m(phi):
    e2, e4, e6 = E2, E2 ** 2, E2 ** 3
    return A_WGS * ((1 - e2 / 4 - 3 * e4 / 64 - 5 * e6 / 256) * phi
                    - (3 * e2 / 8 + 3 * e4 / 32 + 45 * e6 / 1024) * math.sin(2 * phi)
                    + (15 * e4 / 256 + 45 * e6 / 1024) * math.sin(4 * phi)
                    - (35 * e6 / 3072) * math.sin(6 * phi))


def tm(lat_deg, lon_deg, k0=1.0):
    """Forward Transverse Mercator: (lat, lon) in signed degrees -> (easting, northing) metres from the origin."""
    phi, lam = math.radians(lat_deg), math.radians(lon_deg)
    n = A_WGS / math.sqrt(1 - E2 * math.sin(phi) ** 2)
    t = math.tan(phi) ** 2
    c = EP2 * math.cos(phi) ** 2
    a = (lam - LON0) * math.cos(phi)
    x = k0 * n * (a + (1 - t + c) * a ** 3 / 6 + (5 - 18 * t + t ** 2 + 72 * c - 58 * EP2) * a ** 5 / 120)
    y = k0 * (_m(phi) - _m(LAT0) + n * math.tan(phi) * (a ** 2 / 2 + (5 - t + 9 * c + 4 * c ** 2) * a ** 4 / 24
                                                       + (61 - 58 * t + t ** 2 + 600 * c - 330 * EP2) * a ** 6 / 720))
    return x, y


def dms(deg, hemi):
    d = abs(deg)
    s_total = round(d * 3600)
    dd, rem = divmod(s_total, 3600)
    mm, ss = divmod(rem, 60)
    return '%d°%02d′%02d″%s' % (dd, mm, ss, hemi)


def meridian_minute_m(lat_deg):
    phi = math.radians(lat_deg)
    return A_WGS * (1 - E2) / (1 - E2 * math.sin(phi) ** 2) ** 1.5 * math.radians(1 / 60)


def parallel_minute_m(lat_deg):
    phi = math.radians(lat_deg)
    return A_WGS / math.sqrt(1 - E2 * math.sin(phi) ** 2) * math.cos(phi) * math.radians(1 / 60)
