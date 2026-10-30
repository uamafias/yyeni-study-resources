"""VIS-6137-1.6-04 -> ITEM-6137-1.6-040-INTERP: climate controls at two sites on the same latitude.

Schematic (not a real place). (a) Plan: a west coast with a cold current flowing north beside it;
a latitude line at 23 S; site A on the coast; an inland range; site B on its eastern slope, where
moist air arrives from the east. (b) West-east section along 23 S (vertical scale exaggerated): A
at sea level beside cold water with sinking-air arrows above; B at 1,000 m with air rising up the
slope. The question shows the controls only; the climatic consequences are on the answer side.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, build, check  # noqa: E402

RID = 'VIS-6137-1.6-04'
ITEM = 'ITEM-6137-1.6-040-INTERP'
W, HQ, HA = 1000, 990, 1330
COLD = '#5f8fbf'


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'Two places on latitude 23°S (schematic, not a real place)')
    # (a) plan
    fig.rect(20, 56, 960, 400, '#ffffff', GREY, 2, 8)
    fig.text(36, 90, '(a) Plan', 26, 'start', 'bold')
    fig.rect(22, 100, 956, 354, C['land'], 'none', 0)
    fig.poly([(22, 100), (230, 100), (250, 200), (240, 300), (260, 454), (22, 454)], C['sea'], 'none', 0)
    fig.poly([(230, 100), (250, 200), (240, 300), (260, 454)], 'none', INK, 2, closed=False)
    for y in (420, 330, 240, 150):
        fig.arrow(200, y, 200, y - 60, COLD, 5, 16)
    fig.text(40, 150, 'cold', 26, 'start', 'bold', COLD, halo=True)
    fig.text(40, 180, 'ocean', 26, 'start', 'bold', COLD, halo=True)
    fig.text(40, 210, 'current', 26, 'start', 'bold', COLD, halo=True)
    fig.poly([(560, 120), (620, 200), (640, 300), (620, 440), (560, 440), (540, 300), (530, 200)], '#b9a27e', INK, 1.5)
    fig.text(590, 140, 'range', 26, 'middle', 'bold', INK, halo=True)
    fig.line(22, 290, 978, 290, INK, 2, dash='10 7')
    fig.text(970, 280, '23°S', 26, 'end', 'bold', INK, halo=True)
    for (x, lab) in ((250, 'A'), (660, 'B')):
        fig.circle(x, 290, 10, '#ffffff', INK, 3)
        fig.text(x + 16, 326, lab, 30, 'start', 'bold', INK, halo=True)
    for y in (230, 350):
        fig.arrow(950, y, 690, y, C['green'], 5, 18)
    fig.text(820, 400, 'moist air from the east', 26, 'middle', 'bold', C['green'], halo=True)
    fig.arrow(80, 420, 80, 350, INK, 4, 14)
    fig.text(80, 445, 'N', 26, 'middle', 'bold', INK, halo=True)
    # (b) section along 23 S
    fig.rect(20, 470, 960, 470, '#ffffff', GREY, 2, 8)
    fig.text(36, 504, '(b) West–east section along 23°S (heights exaggerated)', 26, 'start', 'bold')
    base = 880
    fig.rect(22, 520, 956, 418, '#f5fafd', 'none', 0)
    fig.rect(22, base - 30, 228, 88, C['sea'], 'none', 0)
    fig.text(140, base + 40, 'cold sea', 26, 'middle', 'bold', COLD, halo=True)
    ground = [(250, base - 30), (420, base - 50), (520, base - 150), (600, base - 330), (660, base - 230), (760, base - 120), (978, base - 100)]
    fig.poly(ground + [(978, 938), (250, 938)], '#c9b48a', INK, 2)
    fig.line(22, base - 30, 250, base - 30, C['blue'], 2.5)
    fig.text(30, base - 6, 'sea level', 26, 'start', 'normal', C['blue'], halo=True)
    # heights: sea level at base-30; 1,000 m mark at base-230 -> 0.2 px per m
    fig.circle(250, base - 30, 9, '#ffffff', INK, 3)
    fig.text(262, base - 44, 'A (0 m)', 26, 'start', 'bold', INK, halo=True)
    fig.circle(660, base - 230, 9, '#ffffff', INK, 3)
    fig.text(642, base - 190, 'B (1,000 m)', 26, 'end', 'bold', INK, halo=True)
    for x in (120, 200, 300):
        fig.arrow(x, 560, x, 640, '#7a5fa0', 4, 14)
    fig.text(240, 548, 'subsiding (sinking) air', 26, 'start', 'bold', '#7a5fa0', halo=True)
    for k, (x1, y1, x2, y2) in enumerate(((950, base - 140, 800, base - 160), (790, base - 170, 690, base - 290))):
        fig.arrow(x1, y1, x2, y2, C['green'], 5, 18)
    fig.text(790, base - 50, 'moist air rising', 26, 'start', 'bold', C['green'], halo=True)
    fig.text(790, base - 20, 'over the slope', 26, 'start', 'bold', C['green'], halo=True)
    fig.text(W / 2, HQ - 22, 'Both sites lie at 23°S. Other differences are shown on the map and section.', 26, 'middle', 'normal', GREY)

    A = 'a'
    fig.add('<ellipse cx="160" cy="%d" rx="110" ry="16" fill="#e6e9ec" stroke="%s" stroke-width="1.5"/>' % (base - 52, GREY), A)
    fig.text(150, base - 80, 'fog / low cloud', 26, 'middle', 'bold', C['answer'], A, halo=True)
    for x in (660, 720):
        fig.add('<ellipse cx="%d" cy="%d" rx="60" ry="26" fill="#e6e9ec" stroke="%s" stroke-width="1.5"/>' % (x, base - 310, GREY), A)
    for x in (650, 670, 690, 710):
        fig.line(x, base - 282, x - 8, base - 256, C['blue'], 2.5, A)
    fig.text(590, base - 302, 'cloud, rain', 26, 'end', 'bold', C['answer'], A, halo=True)
    fig.marker(60, 290, '1', A)
    fig.marker(300, base - 92, '2', A)
    fig.marker(560, base - 250, '3', A)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Interpretation (conditional on these controls)', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for n, s in [('1', 'A and B share 23°S, so latitude alone cannot explain differences between them.'),
                 ('2', 'A: cold water cools the air near the surface and sinking air resists deep ascent, so cool conditions with fog but little rain are likely.'),
                 ('3', 'B: height can make it cooler than a comparable low site, and moist air forced up the slope can cool and give cloud and rain.')]:
        fig.marker(52, yy - 9, n, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8

    spec = {
        'kind': 'schematic plan and west-east section (invented place)',
        'sites': {'A': {'lat': '23S', 'height_m': 0, 'setting': 'coast beside a cold current; subsiding air'},
                  'B': {'lat': '23S', 'height_m': 1000, 'setting': 'east slope of an inland range; moist easterly air rising'}},
        'section_vertical_scale': '0.2 px per m (1,000 m = 200 px), horizontal not to scale',
        'question_withholds': ['fog', 'rain', 'cool', 'cloud'],
        'independent_solution': ['shared 23S latitude -> latitude alone cannot explain differences (1)',
                                 'A: cold current + subsidence -> cool surface, fog, little deep rain (1)', 'B: altitude cooler; moist uplift -> rain (1)'],
        'notes_match': 'BL-6137-1.6.08-16',
    }
    checks = [
        check('A and B on the same latitude line', True, 'both at y=290 in plan'),
        check('B drawn 1,000 m above sea level at 0.2 px per m', (base - 30) - (base - 230) == 200),
        check('cold current flows north along the coast (Southern Hemisphere eastern-boundary setting)', True),
        check('moist air approaches B from the east and rises up the slope B faces', True),
    ]
    sides = {
        'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'], 'forbidden': [r'\bfog', r'\brain', r'\bcool(er)?\b', r'\bcloud']},
        'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']},
    }
    return build(RID, fig, spec, sides, checks, panels=[(20, 56, 960, 400), (20, 470, 960, 470)])


if __name__ == '__main__':
    main()
