"""VIS-6137-2.3-02 -> ITEM-6137-2.3-038-PROC (assigned); variant bound to ITEM-6137-2.3-P05.

Base: (a) plan of a footpath with stations A, B, C and a tape line perpendicular to the path at each,
edges defined where bare ground meets continuous vegetation; (b) cross-section at a station: tape for
width between the edges, a straight pole across the path as the depth reference and a ruler down to
the lowest point; (c) a record sheet (three width readings, mean, depth, 10-minute count).
P05 variant (rebuilt in map-revision-01 to practise the syllabus method, OBJ-6137-2.3.92: erosion against distance
from a tourist hot spot): five stations at 30 m intervals (systematic sampling) along a path from a viewpoint car
park; width = three tape readings at right angles, edge to edge; depth = mean of five ruler readings at equal
intervals below a pole laid across the path. S1 0 m 215/220/225 (mean 220), depth 8.0; S2 30 m 165/170/175 (170),
6.4; S3 60 m 130/140/150 (140), depth from 3.8, 4.4, 4.0, 4.6, 4.2 = 4.2; S4 90 m 150/155/160 (155), 3.0, field
note: wet, muddy hollow; S5 120 m 90/95/100 (95), 1.6. S2 and S4 mean widths and S3 depth are blank; S1, S3 and
S5 are plotted on axes of distance 0-120 m against mean width 0-250 cm. Answer: S2 170, S4 155, S3 depth 4.2 cm;
S2 (30, 170) and S4 (90, 155) plotted. No visitor counts are used: distance stands for concentrated use, and the
survey does not measure years of trampling.
"""
import math
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, Axes, table, build, check  # noqa: E402

RID = 'VIS-6137-2.3-02'
ITEM = 'ITEM-6137-2.3-038-PROC'
P05 = 'ITEM-6137-2.3-P05'
W, HQ, HA = 1000, 960, 1290
VY, VH = 1350, 1400
STATIONS = [('S1', 0, (215, 220, 225), 8.0), ('S2', 30, (165, 170, 175), 6.4), ('S3', 60, (130, 140, 150), None),
            ('S4', 90, (150, 155, 160), 3.0), ('S5', 120, (90, 95, 100), 1.6)]
S3_DEPTHS = (3.8, 4.4, 4.0, 4.6, 4.2)
BLANK_WIDTH = ('S2', 'S4')
VEG = '#b9d39a'
BARE = '#d8c39b'


def path_y(x):
    return 230 + 50 * math.sin((x - 60) / 140)


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'Footpath investigation: stations and measurements')
    fig.extra_h = VY + VH
    # (a) plan
    fig.rect(20, 56, 960, 300, VEG, GREY, 2, 8)
    fig.text(36, 90, '(a) Plan (not to scale)', 26, 'start', 'bold')
    xs = list(range(22, 979, 6))
    hw = lambda x: 26 + 10 * math.sin(x / 90)
    fig.poly([(x, path_y(x) - hw(x)) for x in xs] + [(x, path_y(x) + hw(x)) for x in xs[::-1]], BARE, INK, 1.5)
    for lab, x in (('A', 220), ('B', 500), ('C', 780)):
        y = path_y(x)
        dy = (path_y(x + 1) - path_y(x - 1)) / 2
        n = math.hypot(1, dy)
        ux, uy = -dy / n, 1 / n                              # unit normal to the path direction
        d = hw(x) / n                                       # distance along the normal from centre line to each edge
        fig.line(x - ux * d, y - uy * d, x + ux * d, y + uy * d, C['red'], 3.5)
        fig.circle(x - ux * d, y - uy * d, 6, C['red'], INK, 1)
        fig.circle(x + ux * d, y + uy * d, 6, C['red'], INK, 1)
        fig.text(x + 20, y - hw(x) - 18, lab, 30, 'start', 'bold', INK, halo=True)
    fig.text(500, 340, 'red lines: tape across the path at each station', 26, 'middle', 'normal', INK, halo=True)
    # (b) cross-section at a station
    fig.rect(20, 370, 960, 270, '#ffffff', GREY, 2, 8)
    fig.text(36, 404, '(b) Section across the path at one station', 26, 'start', 'bold')
    gy = 540
    ground = [(60, gy - 30), (300, gy - 30), (330, gy - 6), (500, gy + 14), (670, gy - 6), (700, gy - 30), (940, gy - 30)]
    fig.poly(ground + [(940, 620), (60, 620)], BARE, INK, 2)
    fig.rect(60, gy - 44, 240, 14, VEG, 'none', 0)
    fig.rect(700, gy - 44, 240, 14, VEG, 'none', 0)
    fig.line(250, gy - 52, 750, gy - 52, '#5a4126', 8)
    fig.text(500, gy - 100, 'pole: depth reference', 26, 'middle', 'bold', INK, halo=True)
    fig.line(500, gy - 48, 500, gy + 14, C['blue'], 4)
    fig.text(512, gy - 4, 'ruler', 26, 'start', 'bold', C['blue'], halo=True)
    fig.line(300, gy - 30, 700, gy - 30, C['red'], 3, dash='10 6')
    fig.text(500, 606, 'tape: edge to edge', 26, 'middle', 'bold', C['red'], halo=True)
    fig.text(300, gy - 66, 'edge', 26, 'middle', 'bold', INK, halo=True)
    fig.text(700, gy - 66, 'edge', 26, 'middle', 'bold', INK, halo=True)
    # (c) record sheet
    fig.text(36, 690, '(c) Record sheet   (edge = where bare ground meets continuous vegetation)', 26, 'start', 'bold')
    table(fig, 30, 706, [140, 170, 170, 170, 150, 140], 52,
          [['Station', 'Width 1 (cm)', 'Width 2 (cm)', 'Width 3 (cm)', 'Mean (cm)', 'Depth (cm)'], ['A', '', '', '', '', ''], ['B', '', '', '', '', ''], ['C', '', '', '', '', '']],
          align=['middle'] * 6)
    fig.text(36, 940, 'Pedestrians counted in 10 minutes:  A ____   B ____   C ____', 26)

    A = 'a'
    fig.marker(930, 120, '1', A)
    fig.marker(930, 440, '2', A)
    fig.marker(960, 654, '3', A)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Procedure', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for n, s in [('1', 'Define the edges (bare ground meets continuous vegetation) and lay the tape at right angles to the path at each station.'),
                 ('2', 'Measure the width edge to edge three times at each station, and the depth from the pole down to the lowest point.'),
                 ('3', 'Record every reading in cm on the sheet, then calculate the mean width for each station.')]:
        fig.marker(52, yy - 9, n, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8

    # ---- P05 variant: erosion against distance from a hot spot
    V, VQ, VA = 'v-p05', 'v-p05-q', 'v-p05-a'
    fig.rect(0, VY, W, VH, '#ffffff', 'none', 0, layer=V)
    fig.text(W / 2, VY + 40, 'Footpath erosion and distance from a viewpoint car park', 28, 'middle', 'bold', layer=V)
    sy = VY + 130
    fig.rect(20, sy - 34, 160, 68, '#d8d8d8', INK, 1.5, layer=V)
    fig.lines(100, sy - 6, ['Car park', '(hot spot)'], 26, 28, anchor='middle', weight='bold', layer=V)
    x0, x1 = 196, 900
    fig.line(180, sy, x1 + 50, sy, BARE, 26, V)
    for st, d, ws, dep in STATIONS:
        x = x0 + d / 120 * (x1 - x0)
        fig.line(x, sy - 30, x, sy + 30, C['red'], 4, V)
        fig.text(x + (12 if d == 0 else 0), sy - 42, st, 26, 'middle', 'bold', INK, V)
        fig.text(x + (14 if d == 0 else 0), sy + 62, '%d m' % d, 26, 'middle', 'normal', INK, V)
    s4x = x0 + 90 / 120 * (x1 - x0)
    fig.text(s4x, sy + 98, 'wet, muddy hollow', 26, 'middle', 'normal', C['blue'], V)
    fig.text(20, sy + 146, 'Red lines: stations every 30 m (tape at right angles to the path).', 26, 'start', 'normal', INK, V)
    fig.lines(20, sy + 190, ['Width: three readings, edge to edge (edge = where bare ground meets',
                             'continuous vegetation). Depth: pole laid across the path; ruler',
                             'readings at five equally spaced points below it; mean.'], 26, 32, layer=V)
    rows = [['Station', 'Distance (m)', 'Widths (cm)', 'Mean width (cm)', 'Mean depth (cm)']]
    cl = {}
    for i_, (st, d, ws, dep) in enumerate(STATIONS, 1):
        rows.append([st, str(d), ', '.join(map(str, ws)), str(sum(ws) // 3), '%.1f' % (dep if dep is not None else sum(S3_DEPTHS) / 5)])
        if st in BLANK_WIDTH:
            cl[(i_, 3)] = VA
        if dep is None:
            cl[(i_, 4)] = VA
    ty = sy + 310
    y = table(fig, 20, ty, [115, 165, 210, 225, 225], 50, rows, layer=V, cell_layers=cl, align=['middle'] * 5)
    for i_, (st, d, ws, dep) in enumerate(STATIONS, 1):
        if st in BLANK_WIDTH:
            fig.text(20 + 115 + 165 + 210 + 112, ty + i_ * 50 + 34, '______', 26, 'middle', 'normal', GREY, VQ)
        if dep is None:
            fig.text(20 + 115 + 165 + 210 + 225 + 112, ty + i_ * 50 + 34, '______', 26, 'middle', 'normal', GREY, VQ)
    fig.text(20, y + 40, 'S3 depth readings (cm): %s' % ', '.join('%.1f' % v for v in S3_DEPTHS), 26, 'start', 'normal', INK, V)
    ax = Axes(fig, 190, y + 90, 720, 380, (0, 120), (0, 250), layer=V)
    ax.draw(range(0, 121, 30), range(0, 251, 50), 'Distance from car park (m)', 'Mean width (cm)', minor_y=range(0, 251, 10),
            minor_x=range(0, 121, 10), ylabel_x=80)
    for st, d, ws, dep in STATIONS:
        m = sum(ws) / 3
        lay = VA if st in BLANK_WIDTH else V
        fig.circle(ax.X(d), ax.Y(m), 9, C['answer'] if lay == VA else INK, '#ffffff', 2, lay)
        if lay == VA:
            fig.text(ax.X(d) + 16, ax.Y(m) - 16, '%s (%d, %d)' % (st, d, m), 26, 'start', 'bold', C['answer'], VA, halo=True)
        else:
            fig.text(ax.X(d) + (14 if d < 120 else -14), ax.Y(m) + 34, st, 26, 'start' if d < 120 else 'end', 'bold', INK, V, halo=True)
    p05_bottom = y + 90 + 380 + 90

    means = {st: sum(ws) / 3 for st, d, ws, dep in STATIONS}
    depths = {st: (dep if dep is not None else round(sum(S3_DEPTHS) / 5, 2)) for st, d, ws, dep in STATIONS}
    order = [st for st, d, ws, dep in STATIONS]
    spec = {
        'kind': 'footpath station plan, section and record sheet; P05 variant (erosion against distance from a hot spot)',
        'definitions': {'edge': 'where bare ground meets continuous vegetation', 'width': 'edge to edge, perpendicular to the path, three readings',
                        'depth': 'mean of five ruler readings at equally spaced points below a pole laid across the path'},
        'p05': {'bound_item': P05, 'hot_spot': 'viewpoint car park', 'sampling': 'systematic, stations every 30 m from 0 to 120 m',
                'stations': STATIONS, 'S3_depth_readings_cm': S3_DEPTHS, 'means_cm': means, 'mean_depths_cm': depths,
                'field_note': {'S4': 'wet, muddy hollow'}, 'axes': {'x': [0, 120, 'm'], 'y': [0, 250, 'cm']},
                'given_plotted': [(0, 220), (60, 140), (120, 95)], 'answer': {'S2': 170, 'S4': 155, 'S3_depth': 4.2, 'plotted': [(30, 170), (90, 155)]},
                'no_visitor_counts': 'distance stands for concentrated use; the survey does not measure years of trampling'},
        'independent_solution_038': ['define edges and tape orientation (1)', 'repeat perpendicular width measurements at each station (1)',
                                     'record readings in cm and calculate each station mean (1)'],
    }
    w = [means[k] for k in order]
    dd = [depths[k] for k in order]
    checks = [
        check('mean widths 220, 170, 140, 155, 95 cm', w == [220, 170, 140, 155, 95]),
        check('S3 mean depth (3.8+4.4+4.0+4.6+4.2)/5 = 4.2 cm', abs(depths['S3'] - 4.2) < 1e-9),
        check('width falls overall but rises S3 to S4 at the recorded wet hollow (H1 every-step not supported)',
              w[0] > w[-1] and w[3] > w[2] and all(a > b for a, b in zip(w[:3], w[1:3])) and w[3] > w[4]),
        check('depth falls at every station (H2 supported)', all(a > b for a, b in zip(dd, dd[1:])), str(dd)),
        check('stations at equal 30 m intervals from the hot spot', [d for st, d, ws, dep in STATIONS] == [0, 30, 60, 90, 120]),
        check('plotted points within axes; variant fits its panel', all(0 <= m <= 250 for m in w) and p05_bottom <= VY + VH, str(p05_bottom)),
    ]
    clip = (0, VY, W, VH)
    sides = {
        'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q']},
        'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']},
        'p05_question': {'path': 'assets/images/%s-%s-question.png' % (P05, RID), 'layers': [V, VQ], 'clip': clip, 'hide_base': True,
                         'bound_item': P05, 'forbidden': [r'\(30, 170\)', r'\(90, 155\)', r'H1', r'supported']},
        'p05_answer': {'path': 'assets/images/%s-%s-answer.png' % (P05, RID), 'layers': [V, VA], 'clip': clip, 'hide_base': True, 'bound_item': P05},
    }
    return build(RID, fig, spec, sides, checks, panels=[(20, 56, 960, 300), (20, 370, 960, 270)])


if __name__ == '__main__':
    main()
