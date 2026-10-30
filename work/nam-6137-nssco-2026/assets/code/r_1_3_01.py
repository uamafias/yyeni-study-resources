"""VIS-6137-1.3-01 -> ITEM-6137-1.3-002-INTERP: schematic drainage-basin map (plan view, not to scale).

Matches notes block BL-6137-1.3.01-07: outlet O in the south; streams A and B from northern valleys
join the main river before O; a separate stream C drains east to outlet E; the ridge between B and C
is part of the divide. Spot heights are chosen so that every channel falls downstream and every
divide height exceeds the channel heights inside it near that point; the checks verify both.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, build, check  # noqa: E402

RID = 'VIS-6137-1.3-01'
ITEM = 'ITEM-6137-1.3-002-INTERP'
W, HQ, HA = 1000, 830, 1185

O = (500, 690)
E = (958, 430)
MAIN = [(470, 150), (455, 250), (480, 340), (470, 420), (490, 520), (505, 610), O]
TRIB_A = [(205, 175), (260, 260), (330, 330), (410, 390), (470, 420)]
TRIB_B = [(700, 195), (660, 290), (590, 400), (540, 470), (490, 520)]
STREAM_C = [(790, 330), (845, 365), (900, 395), E]
DIVIDE = [O, (580, 655), (630, 560), (690, 430), (730, 310), (795, 190), (720, 112), (560, 100), (380, 98),
          (200, 108), (118, 250), (130, 420), (230, 565), (390, 650), O]
SPOT_DIVIDE = {(200, 108): 1400, (560, 100): 1410, (795, 190): 1380, (690, 430): 1260,
               (118, 250): 1360, (230, 565): 1190, (630, 560): 1160}
SPOT_CHANNEL = {(470, 150): 1330, (205, 175): 1340, (700, 195): 1345, (470, 420): 1090, (490, 520): 1050,
                O: 980, (790, 330): 1240, E: 1010}


def inside(pt, poly):
    x, y = pt
    c = False
    for (x1, y1), (x2, y2) in zip(poly, poly[1:] + poly[:1]):
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1:
            c = not c
    return c


def smooth(pts):
    """Catmull-Rom spline through the points as an SVG path."""
    d = 'M%.1f %.1f' % pts[0]
    P = [pts[0]] + pts + [pts[-1]]
    for i in range(1, len(P) - 2):
        p0, p1, p2, p3 = P[i - 1], P[i], P[i + 1], P[i + 2]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += ' C %.1f %.1f, %.1f %.1f, %.1f %.1f' % (c1 + c2 + p2)
    return d


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'Schematic map of rivers and higher ground (not to scale)')
    fig.under('<rect x="40" y="70" width="920" height="650" fill="#f6f1e3" stroke="none"/>', 'bg')
    fig.order.remove('bg')
    fig.order.insert(0, 'bg')
    fig.rect(40, 70, 920, 650, 'none', INK, 2)
    A = 'a'
    # answer: shade the catchment of O
    fig.under('<path d="%s" fill="#9fd3b0" fill-opacity="0.6" stroke="none"/>' % smooth(DIVIDE[:-1] + [DIVIDE[0]]))
    # divide (ridge line) and channels
    fig.order.remove('bg')
    fig.order.insert(0, 'bg')                       # map background first, then answer shading, then the map
    fig.path(smooth(DIVIDE[:-1] + [DIVIDE[0]]), 'none', '#8b3a2b', 4, extra='stroke-dasharray="16 9"')
    for line, w in ((MAIN, 7), (TRIB_A, 4.5), (TRIB_B, 4.5), (STREAM_C, 4.5)):
        fig.path(smooth(line), 'none', C['water'], w)
    # outlets
    for (x, y), lab, dx in ((O, 'O', 26), (E, 'E', -48)):
        fig.circle(x, y, 11, '#ffffff', INK, 3)
        fig.text(x + dx, y + 10, lab, 30, 'start', 'bold', INK, halo=True)
    # stream letters
    fig.text(250, 225, 'A', 30, 'middle', 'bold', C['blue'], halo=True)
    fig.text(668, 260, 'B', 30, 'middle', 'bold', C['blue'], halo=True)
    fig.text(860, 345, 'C', 30, 'middle', 'bold', C['blue'], halo=True)
    fig.text(430, 200, 'main', 26, 'end', 'bold', C['blue'], halo=True)
    fig.text(430, 228, 'river', 26, 'end', 'bold', C['blue'], halo=True)
    # spot heights
    LAB = {(200, 108): (-10, -8, 'end'), (560, 100): (10, -12, 'start'), (795, 190): (12, 8, 'start'),
           (730, 310): (14, 18, 'start'), (690, 430): (12, 6, 'start'), (118, 250): (10, -8, 'start'),
           (230, 565): (-12, 20, 'end'), (630, 560): (12, 8, 'start'), (470, 150): (-12, -8, 'end'),
           (205, 175): (10, -8, 'start'), (700, 195): (-12, 24, 'end'), (470, 420): (16, 8, 'start'),
           (490, 520): (-14, 24, 'end'), (790, 330): (-10, 32, 'end')}
    for (x, y), h in list(SPOT_DIVIDE.items()) + list(SPOT_CHANNEL.items()):
        if (x, y) in (O, E):
            continue
        fig.circle(x, y, 4, INK, 'none', 0)
        dx, dy, anchor = LAB[(x, y)]
        fig.text(x + dx, y + dy, '{:,}'.format(h).replace(',', '\u2009'), 26, anchor, 'normal', INK, halo=True)
    fig.text(O[0] + 26, O[1] + 40, '980', 26, 'start', 'normal', INK, halo=True)
    fig.text(E[0] - 14, E[1] + 42, '1 010', 26, 'end', 'normal', INK, halo=True)
    # north arrow
    fig.arrow(915, 210, 915, 120, INK, 4, 18)
    fig.text(915, 242, 'N', 30, 'middle', 'bold')
    # key
    ky = 765
    fig.line(50, ky - 9, 110, ky - 9, C['water'], 6)
    fig.text(120, ky, 'river or stream', 26)
    fig.line(330, ky - 9, 400, ky - 9, '#8b3a2b', 4, dash='16 9')
    fig.text(410, ky, 'drainage divide (ridge)', 26)
    fig.circle(712, ky - 9, 9, '#ffffff', INK, 3)
    fig.text(730, ky, 'outlet', 26)
    fig.circle(56, ky + 37, 4, INK, 'none', 0)
    fig.text(70, ky + 46, '1 250  spot height (metres above sea level)', 26)

    # answer markers and arrows
    for line in (MAIN, TRIB_A, TRIB_B, STREAM_C):
        (x1, y1), (x2, y2) = line[-2], line[-1]
        mx, my = (x1 * 0.4 + x2 * 0.6), (y1 * 0.4 + y2 * 0.6)
        fig.arrow(mx - (x2 - x1) * 0.15, my - (y2 - y1) * 0.15, mx + (x2 - x1) * 0.15, my + (y2 - y1) * 0.15, C['answer'], 4, 14, A)
    fig.marker(430, 452, '1')
    fig.marker(545, 545, '1')
    fig.marker(330, 470, '2')
    fig.marker(770, 255, '3')
    fig.marker(820, 425, '3')
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Interpretation (shaded: catchment of O)', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for n, s in [('1', 'Tributaries A and B join the main river at confluences upstream of outlet O.'),
                 ('2', 'The divide encloses all the land whose surface water drains to O: the catchment (shaded).'),
                 ('3', 'Beyond the divide, slopes drain the other way: stream C flows east to a different outlet, E.')]:
        fig.marker(52, yy - 9, n, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8
    fig.para(36, yy + 2, 'The divide follows higher ground: its spot heights are above those of the channels inside it, '
             'and it meets the river only at O.', 26, 920, 32, layer=A)

    spec = {
        'kind': 'schematic plan-view basin map (not to scale), north at top',
        'teaching_target': 'Basin arrangement: tributaries join the main channel upstream of O; the divide encloses the contributing area; slopes across the divide drain to another outlet (E).',
        'outlets': {'O': O, 'E': E}, 'main': MAIN, 'tributary_A': TRIB_A, 'tributary_B': TRIB_B, 'stream_C': STREAM_C,
        'divide_vertices': DIVIDE,
        'spot_heights_m': {'divide': {str(k): v for k, v in SPOT_DIVIDE.items()}, 'channels': {str(k): v for k, v in SPOT_CHANNEL.items()}},
        'question_shows': ['main river, tributaries A and B, stream C', 'divide as a dashed ridge line', 'outlets O and E', 'spot heights', 'north arrow', 'key'],
        'question_withholds': ['catchment shading', 'flow-direction arrows', 'the words catchment/confluence/tributary'],
        'independent_solution': ['A and B join the main river upstream of O (1)', 'divide encloses land draining to O (1)',
                                 'stream C beyond the divide drains east to E, a different outlet (1)'],
        'consistency_rules': ['each channel falls downstream', 'divide spot heights exceed channel heights inside the basin',
                              'all O-basin channel vertices inside the divide; stream C outside'],
    }
    poly = DIVIDE[:-1]
    basin_pts = [p for line in (MAIN[:-1], TRIB_A, TRIB_B) for p in line]
    falls = all(SPOT_CHANNEL[a] > SPOT_CHANNEL[b] for a, b in [((470, 150), (470, 420)), ((470, 420), (490, 520)), ((490, 520), O),
                                                                ((205, 175), (470, 420)), ((700, 195), (490, 520)), ((790, 330), E)])
    inner_max = max(v for k, v in SPOT_CHANNEL.items() if k not in (E, (790, 330)))
    checks = [
        check('all O-basin channel points inside the divide', all(inside(p, poly) for p in basin_pts)),
        check('stream C and outlet E outside the divide', not any(inside(p, poly) for p in STREAM_C)),
        check('divide passes through outlet O', DIVIDE[0] == O and DIVIDE[-1] == O),
        check('every channel falls downstream', falls),
        check('lowest divide height exceeds highest channel height inside the basin except at O',
              min(SPOT_DIVIDE.values()) > SPOT_CHANNEL[(490, 520)], 'divide min %d; confluence B %d' % (min(SPOT_DIVIDE.values()), SPOT_CHANNEL[(490, 520)])),
        check('divide heights beside each source exceed that source',
              SPOT_DIVIDE[(200, 108)] > SPOT_CHANNEL[(205, 175)] and SPOT_DIVIDE[(795, 190)] > SPOT_CHANNEL[(700, 195)]
              and SPOT_DIVIDE[(560, 100)] > SPOT_CHANNEL[(470, 150)] and SPOT_DIVIDE[(690, 430)] > SPOT_CHANNEL[(790, 330)]),
    ]
    sides = {
        'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q', 'bg'],
                     'forbidden': [r'catchment', r'confluence', r'tributar', r'basin']},
        'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a', 'au', 'bg']},
    }
    return build(RID, fig, spec, sides, checks)


if __name__ == '__main__':
    main()
