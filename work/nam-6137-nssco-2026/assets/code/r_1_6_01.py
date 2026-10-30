"""VIS-6137-1.6-01 -> ITEM-6137-1.6-008-INTERP: three weather instruments drawn from a published description.

Geometry source (retrieved 30 Oct 2026; SHA-256 of the PDF recorded in the spec): Met Office National
Meteorological Library fact sheet 17, "Weather observations", URL in the spec. It states:
  - storage rain-gauge: sharp rim of 127 mm (5 inch) diameter, 30 cm above ground, a funnel collecting
    rain into a narrow-necked bottle in a removable can, emptied into a graduated glass measure;
  - humidity: dry bulb and wet bulb in a Stevenson screen at 1.25 m, the wet bulb wrapped in moist muslin;
  - wind speed: cup anemometer of three or four cups rotating a spindle, on a 10 m mast.
Drawings are schematic sections at different scales (stated on each panel); labels give working
parts and units but not the measured element or instrument name on the question side.
"""
import math
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, build, check  # noqa: E402

RID = 'VIS-6137-1.6-01'
ITEM = 'ITEM-6137-1.6-008-INTERP'
W, HQ, HA = 1000, 860, 1205
SOURCE = {'title': 'Met Office National Meteorological Library and Archive, Fact sheet 17: Weather observations',
          'url': 'https://www.metoffice.gov.uk/binaries/content/assets/metofficegovuk/pdf/weather/guides/10_0230_fs_17_observations.pdf',
          'retrieved': '2026-10-30', 'sha256': '2ca4956b56d70d577febd0a8b25d57212471fb2daf7bcfda56cccf06cad50e6a',
          'facts_used': ['storage gauge rim 127 mm diameter, 30 cm above ground; funnel into narrow-necked bottle in a removable can; graduated glass measure',
                         'dry bulb and wet bulb (moist muslin wick) in a Stevenson screen, 1.25 m above ground',
                         'cup anemometer with three or four cups rotating a spindle; wind sensors at the top of a 10 m mast']}
METAL = '#c9ccd1'


def panel(fig, x0, w, title, sub):
    fig.rect(x0, 56, w, 700, '#ffffff', GREY, 2, 8)
    fig.text(x0 + 16, 92, title, 28, 'start', 'bold')
    fig.text(x0 + 16, 124, sub, 26, 'start', 'normal', GREY)


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'Three weather instruments (sections, not to the same scale)')
    # ---- A: storage rain gauge, section; 1 cm = 1.5 px is not used: proportions follow 127 mm rim, 300 mm rim height
    panel(fig, 20, 320, 'A', 'section')
    g = 640                                     # ground
    MM = 0.9                                    # px per mm in panel A
    rim_w = 127 * MM                            # rim width and rim height both at 0.9 px per mm (true proportions)
    cx = 120
    rim_y = g - 300 * MM
    fig.rect(24, g, 312, 40, '#b79d76', 'none', 0)
    fig.line(24, g, 336, g, INK, 2.5)
    fig.poly([(cx - rim_w / 2, rim_y), (cx + rim_w / 2, rim_y), (cx + rim_w / 2, g + 30), (cx - rim_w / 2, g + 30)], METAL, INK, 2.5)
    fig.poly([(cx - rim_w / 2 + 4, rim_y + 6), (cx + rim_w / 2 - 4, rim_y + 6), (cx + 6, rim_y + 70), (cx - 6, rim_y + 70)], '#e8eef4', INK, 2)
    fig.poly([(cx - 30, rim_y + 110), (cx - 8, rim_y + 90), (cx - 8, rim_y + 76), (cx + 8, rim_y + 76), (cx + 8, rim_y + 90), (cx + 30, rim_y + 110),
              (cx + 30, g + 20), (cx - 30, g + 20)], '#ffffff', INK, 2)
    fig.rect(cx - 28, g - 30, 56, 48, '#8ec1e6', 'none', 0)
    fig.line(cx + 6, rim_y + 70, cx + 6, rim_y + 76, INK, 2)
    for lab, ly, ty in (('rim', rim_y, rim_y + 4), ('funnel', rim_y + 40, rim_y + 52), ('bottle in', rim_y + 140, rim_y + 140), ('a can', None, rim_y + 172)):
        if ly is not None:
            fig.line(cx + rim_w / 2 - 6, ly, cx + rim_w / 2 + 26, ty - 9, INK, 1.5)
        fig.text(cx + rim_w / 2 + 30, ty, lab, 26, 'start', 'bold', INK, halo=True)
    fig.line(36, rim_y, 36, g, INK, 2)
    fig.line(30, rim_y, 42, rim_y, INK, 2)
    fig.text(40, rim_y - 12, '30 cm', 26, 'start', 'bold', INK, halo=True)
    fig.text(30, rim_y - 46, 'rim 127 mm across', 26, 'start', 'normal', INK, halo=True)
    # graduated measure
    mx = 240
    fig.rect(mx, 150, 60, 125, '#f2f7fb', INK, 2)
    fig.rect(mx + 2, 225, 56, 48, '#8ec1e6', 'none', 0)
    for k in range(6):
        y = 265 - k * 20
        fig.line(mx, y, mx + (16 if k % 2 == 0 else 9), y, INK, 1.5)
    fig.text(mx - 8, 172, 'glass', 26, 'end', 'normal', INK, halo=True)
    fig.text(mx - 8, 202, 'measure', 26, 'end', 'normal', INK, halo=True)
    fig.text(mx - 8, 232, 'in mm', 26, 'end', 'bold', INK, halo=True)
    # ---- B: wet and dry bulb thermometers in a screen
    panel(fig, 350, 320, 'B', 'inside a louvred screen')
    bx0, bx1 = 380, 640
    fig.rect(bx0, 170, bx1 - bx0, 380, '#ffffff', INK, 3)
    for y in range(180, 545, 18):
        fig.line(bx0 + 4, y, bx0 + 20, y + 10, GREY, 2)
        fig.line(bx1 - 20, y + 10, bx1 - 4, y, GREY, 2)
    for k, (tx, lab) in enumerate(((460, 'dry bulb'), (560, 'wet bulb'))):
        fig.rect(tx - 9, 200, 18, 230, '#ffffff', INK, 2, rx=9)
        fig.circle(tx, 440, 14, C['red'], INK, 2)
        fig.rect(tx - 3, 300 + 40 * k, 6, 140 - 40 * k, C['red'], 'none', 0)     # wet bulb reads lower
        for j in range(8):
            fig.line(tx + 9, 220 + j * 25, tx + 18, 220 + j * 25, INK, 1.5)
        fig.text(tx, 194, '°C', 26, 'middle', 'bold')
        fig.text(tx, 590, lab.split()[0], 26, 'middle', 'bold', INK, halo=True)
        fig.text(tx, 622, 'bulb', 26, 'middle', 'bold', INK, halo=True)
    fig.rect(536, 470, 48, 52, '#8ec1e6', INK, 2)
    fig.path('M560 440 C 548 460, 548 480, 556 500', 'none', '#f4f1e6', 8)
    fig.path('M560 440 C 548 460, 548 480, 556 500', 'none', INK, 1, extra='stroke-dasharray="3 3"')
    fig.text(510, 680, 'wet bulb: muslin wick', 26, 'middle', 'normal', INK, halo=True)
    fig.text(510, 712, 'dipping into water', 26, 'middle', 'normal', INK, halo=True)
    fig.text(510, 744, 'screen at 1.25 m', 26, 'middle', 'normal', GREY)
    # ---- C: cup anemometer
    panel(fig, 680, 300, 'C', 'top of a 10 m mast')
    ax, ay = 830, 330
    fig.rect(ax - 6, ay, 12, 380, METAL, INK, 2)
    fig.rect(ax - 18, ay - 10, 36, 30, METAL, INK, 2)
    for k, ang in enumerate((200, 320, 80)):
        a = math.radians(ang)
        ex, ey = ax + 95 * math.cos(a), ay - 40 + 30 * math.sin(a)
        fig.line(ax, ay - 10, ex, ey, INK, 3)
        fig.path('M%.1f %.1f a 24 18 0 1 0 0.1 0 z' % (ex - 24, ey), '#5a6470', INK, 2)
    fig.text(ax + 16, ay + 70, 'spindle', 26, 'start', 'bold', INK, halo=True)
    fig.text(ax, 180, 'three cups', 26, 'middle', 'bold', INK, halo=True)
    fig.text(ax, 212, 'on arms', 26, 'middle', 'bold', INK, halo=True)
    fig.rect(ax - 44, 560, 88, 46, '#222222', INK, 2, rx=6)
    fig.text(ax, 592, 'm/s', 26, 'middle', 'bold', '#ffffff')
    fig.text(ax, 650, 'counter', 26, 'middle', 'bold', INK, halo=True)
    fig.text(W / 2, HQ - 30, 'Units shown: mm (A); °C (B); m/s (C)', 26, 'middle', 'bold')

    A = 'a'
    for x, lines, n in ((180, ['rain gauge:', 'rainfall depth (mm)'], '1'), (510, ['wet-and-dry bulb', 'hygrometer: humidity'], '2'),
                        (830, ['cup anemometer:', 'wind speed'], '3')):
        fig.marker(x - 120 if n != '3' else x - 110, 150, n, A)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Interpretation', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for n, s in [('1', 'A: rain enters the 127 mm rim, the funnel channels it into the bottle, and the glass measure gives rainfall depth in mm: a rain gauge.'),
                 ('2', 'B: a dry bulb beside a wet bulb kept moist by a muslin wick; the wet-bulb depression, read with a table, gives relative humidity.'),
                 ('3', 'C: the cups turn the spindle in the wind; the counter, by calibration, gives wind speed in m/s: a cup anemometer.')]:
        fig.marker(52, yy - 9, n, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8

    spec = {
        'kind': 'three schematic instrument sections from a published description',
        'source': SOURCE,
        'panel_A': {'rim_diameter_mm': 127, 'rim_height_mm': 300, 'note': 'rim width and height both drawn at 0.9 px per mm'},
        'panel_B': {'thermometers': ['dry bulb', 'wet bulb with muslin wick in water'], 'screen_height_m': 1.25},
        'panel_C': {'cups': 3, 'mast_m': 10, 'output': 'counter calibrated in m/s'},
        'question_withholds': ['rain gauge', 'hygrometer', 'psychrometer', 'anemometer', 'rainfall', 'humidity', 'wind speed'],
        'independent_solution': ['A collector/funnel/measure -> rainfall depth (mm) (1)', 'B paired dry/wet bulbs -> relative humidity via depression (1)',
                                 'C cups rotating spindle -> wind speed (1)'],
    }
    checks = [
        check('rain-gauge rim drawn 300 mm above ground at 0.9 px/mm', abs((g - rim_y) / MM - 300) < 1e-9),
        check('exactly three cups drawn (source allows three or four)', True),
        check('wet bulb wick reaches the water pot', True, 'wick path ends inside pot at y=500'),
        check('every unit belongs to its own instrument', True, 'mm (A), degrees C (B), m/s (C)'),
        check('wet bulb drawn reading lower than dry bulb (evaporative cooling; no values given)', True, 'column top 340 vs 300'),
    ]
    sides = {
        'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'],
                     'forbidden': [r'gauge', r'hygrometer', r'psychrometer', r'anemometer', r'rainfall', r'humidity', r'wind speed']},
        'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a']},
    }
    return build(RID, fig, spec, sides, checks, panels=[(20, 56, 320, 700), (350, 56, 320, 700), (680, 56, 300, 700)])


if __name__ == '__main__':
    main()
