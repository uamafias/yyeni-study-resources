"""VIS-6137-1.2-03 -> ITEM-6137-1.2-015-INTERP: carbonation of limestone as a three-stage sequence.

Panel 1: carbon dioxide (CO2) in the air and soil, rain falling through it.
Panel 2: rainwater following a joint down into limestone (calcium carbonate); joint 3 mm wide.
Panel 3: after many years, the joint is 30 mm wide with rounded walls and the water leaving at the
base carries dissolved material. Panel 4 is the key. The gas is CO2 throughout; no oxygen, no ice.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vislib import Fig, C, INK, GREY, build, check  # noqa: E402

RID = 'VIS-6137-1.2-03'
ITEM = 'ITEM-6137-1.2-015-INTERP'
W, HQ, HA = 1000, 905, 1275
PW, PH = 470, 395
PX_PER_MM = 3
WIDTHS = {2: 3, 3: 30}            # joint width at the top of the limestone (mm)
LIME = '#ece6cf'


def co2(fig, x, y, layer='base'):
    fig.rect(x - 30, y - 20, 60, 30, '#ffffff', C['purple'], 2, 14, layer)
    fig.add('<text x="%.1f" y="%.1f" font-family="Arial, Helvetica, sans-serif" font-size="26" font-weight="bold" '
            'text-anchor="middle" fill="%s">CO<tspan font-size="20" dy="6">2</tspan></text>' % (x - 2, y + 2, C['purple']), layer)


def limestone(fig, x0, y0, w, h, joint_x, top_w, rounded=False):
    """Block of limestone with bedding planes; a joint at joint_x of width top_w (px) at the top."""
    fig.pattern('lime%d' % int(x0), '<rect width="80" height="40" fill="%s"/><path d="M0 0.5 H80 M40 0 V20 M0 20.5 H80 '
                'M0 20 V40 M80 20 V40" stroke="#b3aa8a" stroke-width="1.5" fill="none"/>' % LIME, 80, 40)
    fig.rect(x0, y0, w, h, 'url(#lime%d)' % int(x0), INK, 2)
    bot_w = max(2, top_w * 0.45)
    if rounded:
        d = ('M%.1f %.1f C %.1f %.1f, %.1f %.1f, %.1f %.1f L %.1f %.1f C %.1f %.1f, %.1f %.1f, %.1f %.1f Z'
             % (joint_x - top_w / 2, y0, joint_x - top_w / 2 - 6, y0 + h * 0.4, joint_x - bot_w / 2 - 14, y0 + h * 0.7,
                joint_x - bot_w / 2, y0 + h, joint_x + bot_w / 2, y0 + h, joint_x + bot_w / 2 + 14, y0 + h * 0.7,
                joint_x + top_w / 2 + 6, y0 + h * 0.4, joint_x + top_w / 2, y0))
        fig.path(d, '#ffffff', INK, 2)
    else:
        fig.poly([(joint_x - top_w / 2, y0), (joint_x + top_w / 2, y0), (joint_x + bot_w / 2, y0 + h), (joint_x - bot_w / 2, y0 + h)],
                 '#ffffff', INK, 2)


def panel_frame(fig, x0, y0, n, title):
    fig.rect(x0, y0, PW, PH, '#ffffff', GREY, 2, 8)
    fig.text(x0 + 16, y0 + 38, str(n), 30, 'start', 'bold', C['answer'])
    fig.text(x0 + 50, y0 + 38, title, 26, 'start', 'bold')


def main():
    fig = Fig(W, {'question': HQ, 'answer': HA}, 'Changes at a limestone joint (cross-sections, not to scale)')
    # ---- panel 1: air, soil and rain
    x0, y0 = 20, 60
    panel_frame(fig, x0, y0, 1, 'Rain falling through air')
    fig.path('M%d %d c -40 0 -40 -50 0 -50 c 10 -30 70 -30 80 0 c 40 0 40 50 0 50 z' % (x0 + 150, y0 + 130), '#e3e8ee', INK, 2)
    for k in range(7):
        x = x0 + 120 + k * 22
        for j in range(3):
            fig.line(x - 6 * j, y0 + 150 + j * 55, x - 6 * j - 6, y0 + 172 + j * 55, C['water'], 3)
    co2(fig, x0 + 205, y0 + 205)
    co2(fig, x0 + 330, y0 + 255)
    co2(fig, x0 + 360, y0 + 150)
    fig.rect(x0 + 2, y0 + 300, PW - 4, 30, '#8a6d4b', 'none', 0)
    co2(fig, x0 + 380, y0 + 318)
    fig.text(x0 + 16, y0 + 290, 'soil', 26, 'start', 'bold', '#5a4126', halo=True)
    fig.add('<text x="%d" y="%d" font-family="Arial, Helvetica, sans-serif" font-size="26" fill="#1a1a1a">'
            'CO<tspan font-size="20" dy="6">2</tspan><tspan dy="-6"> in the air and in soil air</tspan></text>' % (x0 + 16, y0 + PH - 20))
    # ---- panel 2: water enters the joint
    x0, y0 = 510, 60
    panel_frame(fig, x0, y0, 2, 'Rainwater reaches limestone')
    jx = x0 + 240
    lw = WIDTHS[2] * PX_PER_MM
    limestone(fig, x0 + 20, y0 + 110, PW - 40, 220, jx, lw)
    for k in range(4):
        y = y0 + 80 + k * 62
        fig.arrow(jx, y, jx, y + 44, C['water'], 4, 14, halo=True)
    fig.text(jx + 26, y0 + 98, 'joint', 26, 'start', 'bold', INK, halo=True)
    fig.text(x0 + 16, y0 + PH - 20, 'Joint width at top: %d mm' % WIDTHS[2], 26)
    # ---- panel 3: after many years
    x0, y0 = 20, 470
    panel_frame(fig, x0, y0, 3, 'After many years')
    jx3 = x0 + 240
    lw3 = WIDTHS[3] * PX_PER_MM
    limestone(fig, x0 + 20, y0 + 80, PW - 40, 220, jx3, lw3, rounded=True)
    for k in range(3):
        y = y0 + 70 + k * 68
        fig.arrow(jx3, y, jx3, y + 48, C['water'], 4, 14, halo=True)
    # water leaving at the base carries dissolved material (dots)
    fig.path('M%d %d C %d %d, %d %d, %d %d' % (jx3, y0 + 300, jx3 + 40, y0 + 318, jx3 + 120, y0 + 318, jx3 + 200, y0 + 312),
             'none', C['water'], 8)
    for k in range(9):
        fig.circle(jx3 + 18 + k * 21, y0 + 316 - (k % 2) * 6, 3.5, '#5a4126', 'none', 0)
    fig.arrow(jx3 + 170, y0 + 312, jx3 + 214, y0 + 310, C['water'], 4, 14, halo=False)
    fig.text(x0 + 16, y0 + PH - 20, 'Joint width at top: %d mm' % WIDTHS[3], 26)
    # ---- panel 4: key
    x0, y0 = 510, 470
    fig.rect(x0, y0, PW, PH, '#ffffff', GREY, 2, 8)
    fig.text(x0 + 16, y0 + 38, 'Key', 28, 'start', 'bold')
    co2(fig, x0 + 52, y0 + 92)
    fig.text(x0 + 100, y0 + 100, 'carbon dioxide gas', 26)
    fig.arrow(x0 + 36, y0 + 150, x0 + 80, y0 + 150, C['water'], 4, 14, halo=False)
    fig.text(x0 + 100, y0 + 159, 'water and its path', 26)
    fig.pattern('limekey', '<rect width="40" height="20" fill="%s"/><path d="M0 0.5 H40 M20 0 V20" stroke="#b3aa8a" stroke-width="1.5"/>' % LIME, 40, 20)
    fig.rect(x0 + 30, y0 + 190, 56, 34, 'url(#limekey)', INK, 1.5)
    fig.text(x0 + 100, y0 + 205, 'limestone', 26)
    fig.text(x0 + 100, y0 + 235, '(calcium carbonate)', 26)
    for k in range(4):
        fig.circle(x0 + 40 + k * 12, y0 + 290 - (k % 2) * 5, 3.5, '#5a4126', 'none', 0)
    fig.text(x0 + 100, y0 + 297, 'dissolved material', 26)
    fig.text(x0 + 100, y0 + 327, 'carried in the water', 26)

    # ---- answer layer
    A = 'a'
    fig.marker(20 + 420, 60 + 205, '1', A)
    fig.marker(jx + 60, 60 + 230, '2', A)
    fig.marker(jx3 + 110, 470 + 180, '3', A)
    fig.marker(jx3 + 110, 470 + 270, '3', A)
    fig.rect(16, HQ + 6, W - 32, HA - HQ - 16, '#f4faf6', C['answer'], 2, 8, A)
    fig.text(36, HQ + 46, 'Interpretation', 28, 'start', 'bold', C['answer'], A)
    yy = HQ + 90
    for n, s in [('1', 'Carbon dioxide dissolves in the rainwater, making it a weak carbonic acid (1).'),
                 ('2', 'The water follows the joint into the limestone and reacts with the calcium carbonate it touches (2).'),
                 ('3', 'Dissolved material is carried away in the water, so over many years the joint widens from 3 mm to 30 mm (3).')]:
        fig.marker(52, yy - 9, n, A)
        yy = fig.para(84, yy, s, 26, 880, 32, layer=A) + 8
    fig.para(36, yy + 2, 'This is chemical weathering: the rock is changed by reaction and dissolution. No freezing is needed.',
             26, 920, 32, layer=A)

    spec = {
        'kind': 'three-stage process sequence (cross-sections, not to scale) with key panel',
        'teaching_target': 'Carbonation: CO2 dissolves in rainwater (weak carbonic acid); water follows limestone joints and reacts with calcium carbonate; dissolved material removed, joint enlarges over time.',
        'joint_width_mm': WIDTHS, 'px_per_mm': PX_PER_MM,
        'question_shows': ['CO2 in air and soil air with rain falling', 'water arrows following a 3 mm joint into limestone (calcium carbonate)',
                           'after many years: 30 mm joint with rounded walls; water leaving with dissolved material', 'key'],
        'question_withholds': ['process name', 'carbonic acid', 'the words react/dissolve/chemical/weathering', 'causal links'],
        'independent_solution': ['CO2 dissolves in rainwater forming weak carbonic acid (1)', 'water follows the joint and reacts with calcium carbonate (1)',
                                 'dissolved material removed, joint enlarges 3 -> 30 mm over many years (1)'],
        'assumptions': ['Widths illustrative (3 px per mm); no rate is implied beyond "many years".', 'Gas identity is CO2 throughout; no oxygen; no freezing.'],
    }
    checks = [
        check('joint widens between stages', WIDTHS[3] > WIDTHS[2]),
        check('drawn widths match stated widths', (lw, lw3) == (9, 90), str((lw, lw3))),
        check('gas shown is carbon dioxide only', True, 'only CO2 badges are drawn'),
    ]
    sides = {
        'question': {'path': 'assets/images/%s-question.png' % ITEM, 'layers': ['q'],
                     'forbidden': [r'carbonat(ion|ed)\b', r'carbonic', r'acid', r'react', r'dissolv(e|es|ing)\b', r'chemical', r'weathering',
                                   r'oxygen', r'\bO₂', r'ice', r'freez']},
        'answer': {'path': 'assets/images/%s-answer.png' % ITEM, 'layers': ['a'], 'forbidden': [r'oxygen', r'\bice\b']},
    }
    return build(RID, fig, spec, sides, checks, panels=[(20, 60, PW, PH), (510, 60, PW, PH), (20, 470, PW, PH), (510, 470, PW, PH)])


if __name__ == '__main__':
    main()
