#!/usr/bin/env python3
"""Generate the 0455 Cambridge IGCSE Economics teaching diagrams.

Every card-specific diagram is drawn from the figures its card states, so the picture and the
card agree. Generic diagrams carry no figures. Output: PNG (1600 x 1200) and SVG per diagram,
plus INDEX.md and index.csv mapping each file to the cards and note blocks it belongs with.

    python3 make_diagrams_0455.py <out_dir>
"""
import csv
import os
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, Rectangle
from scipy.interpolate import PchipInterpolator
from scipy.optimize import brentq, fsolve

OUT = sys.argv[1] if len(sys.argv) > 1 else 'out'
os.makedirs(OUT, exist_ok=True)

INK = '#0b0b0b'
INK2 = '#52514e'
MUTED = '#9a9893'
BLUE = '#2a78d6'      # original curve
ORANGE = '#eb6834'    # new / shifted curve
GREEN = '#1baf7a'     # third curve where a panel needs one
TINT_B = '#2a78d6'
TINT_O = '#eb6834'

plt.rcParams.update({
    'font.family': 'DejaVu Sans', 'font.size': 15, 'axes.linewidth': 1.6,
    'svg.fonttype': 'none', 'axes.edgecolor': INK, 'text.color': INK,
    'xtick.color': INK2, 'ytick.color': INK2, 'text.parse_math': False,
})

REGISTRY = []


def fmt(v):
    if isinstance(v, str):
        return v
    if abs(v - round(v)) < 1e-9:
        v = int(round(v))
        return f'{v:,}'.replace(',', ' ') if v >= 10000 else (f'{v:,}'.replace(',', ' ') if v >= 1000 else str(v))
    return f'{v:g}'


def new_fig(title, panels=1, size=(8, 6)):
    if panels == 1:
        fig, ax = plt.subplots(figsize=size, dpi=200)
        axes = [ax]
    elif panels == 2:
        fig, axes = plt.subplots(1, 2, figsize=(12, 6), dpi=200)
        axes = list(axes)
    else:
        fig, axes = plt.subplots(2, 2, figsize=(11, 10), dpi=200)
        axes = list(axes.flat)
    fig.patch.set_facecolor('white')
    fig.suptitle(title, fontsize=17, fontweight='bold', x=0.02, ha='left', y=0.985)
    return fig, axes


def frame(ax, xlabel, ylabel, xlim, ylim, xticks=None, yticks=None, sub=None):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    for s in ('top', 'right'):
        ax.spines[s].set_visible(False)
    ax.spines['left'].set_position(('data', xlim[0]))
    ax.spines['bottom'].set_position(('data', ylim[0]))
    # arrow heads on the axes
    ax.plot(1, ylim[0], '>', color=INK, transform=ax.get_yaxis_transform(), clip_on=False, ms=8)
    ax.plot(xlim[0], 1, '^', color=INK, transform=ax.get_xaxis_transform(), clip_on=False, ms=8)
    xt = xticks or {}
    yt = yticks or {}
    ax.set_xticks(list(xt.keys()))
    ax.set_xticklabels(list(xt.values()))
    ax.set_yticks(list(yt.keys()))
    ax.set_yticklabels(list(yt.values()))
    ax.tick_params(length=0, pad=6, labelsize=13)
    ax.set_xlabel(xlabel, fontsize=14, color=INK, labelpad=8, loc='right')
    ax.set_ylabel(ylabel, fontsize=14, color=INK, labelpad=8, loc='top')
    if xlim[0] == 0 and ylim[0] == 0:
        ax.text(xlim[0], ylim[0], '0', ha='right', va='top', fontsize=12, color=INK2,
                transform=ax.transData)
    else:
        kw = dict(transform=ax.transAxes, color=INK, lw=1.4, clip_on=False)
        for d in (0.025, 0.045):
            if xlim[0] != 0:
                ax.plot([d - 0.008, d + 0.008], [-0.018, 0.018], **kw)
            if ylim[0] != 0:
                ax.plot([-0.018, 0.018], [d - 0.008, d + 0.008], **kw)
    if sub:
        ax.set_title(sub, fontsize=14, color=INK, loc='left', pad=12)


def lin(p1, p2):
    """Linear curve through two (q, p) points; returns q(p)."""
    (q1, a), (q2, b) = p1, p2
    m = (q2 - q1) / (b - a)
    return lambda p: q1 + m * (p - a)


def draw_qp(ax, qf, prange, color, label, lw=2.6, ls='-', label_at='end', dx=0, dy=0, fs=15):
    p = np.linspace(prange[0], prange[1], 400)
    q = np.array([qf(x) for x in p])
    (x0, x1), (y0, y1) = ax.get_xlim(), ax.get_ylim()
    mx, my = 0.02 * (x1 - x0), 0.02 * (y1 - y0)
    keep = (q >= x0 + mx) & (q <= x1 - 3 * mx) & (p >= y0 + my) & (p <= y1 - my)
    q, p = q[keep], p[keep]
    ax.plot(q, p, color=color, lw=lw, ls=ls, solid_capstyle='round')
    if label:
        i = -1 if label_at == 'end' else 0
        ax.text(q[i] + dx, p[i] + dy, label, color=color if color not in (MUTED,) else INK2,
                fontsize=fs, fontweight='bold', ha='left', va='center')


def draw_xy(ax, x, y, color, label, lw=2.6, ls='-', lx=None, ly=None, fs=15, ha='left'):
    ax.plot(x, y, color=color, lw=lw, ls=ls, solid_capstyle='round')
    if label:
        ax.text(lx if lx is not None else x[-1], ly if ly is not None else y[-1], label,
                color=color, fontsize=fs, fontweight='bold', ha=ha, va='center')


def pt(ax, q, p, label=None, guides=True, xlim0=None, ylim0=None, off=(8, 8), ha='left', color=INK):
    xlim0 = ax.get_xlim()[0] if xlim0 is None else xlim0
    ylim0 = ax.get_ylim()[0] if ylim0 is None else ylim0
    if guides:
        ax.plot([q, q], [ylim0, p], ls=(0, (2, 3)), color=INK2, lw=1.2)
        ax.plot([xlim0, q], [p, p], ls=(0, (2, 3)), color=INK2, lw=1.2)
    ax.plot(q, p, 'o', color=color, ms=9, mec='white', mew=1.8, zorder=5)
    if label:
        ax.annotate(label, (q, p), xytext=off, textcoords='offset points', fontsize=15,
                    fontweight='bold', ha=ha, va='bottom', color=INK)


def arrow(ax, a, b, color=INK, rad=0.0, lw=2.0):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle='-|>', mutation_scale=18, color=color, lw=lw,
                                 connectionstyle=f'arc3,rad={rad}', zorder=4, shrinkA=8, shrinkB=8))


def bracket_h(ax, q1, q2, p, text, color=INK, below=True):
    """Horizontal gap between two quantities at price p."""
    ax.annotate('', (q1, p), (q2, p), arrowprops=dict(arrowstyle='<->', color=color, lw=1.8))
    ax.text((q1 + q2) / 2, p, text, ha='center', va='top' if below else 'bottom', fontsize=13,
            color=color, bbox=dict(fc='white', ec='none', pad=1.5),
            transform=ax.transData).set_y(p)


def note(ax, x, y, text, ha='left', va='top', fs=12.5, color=INK2):
    ax.text(x, y, text, ha=ha, va=va, fontsize=fs, color=color, linespacing=1.35,
            transform=ax.transAxes)


def save(fig, slug, meta):
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    png = os.path.join(OUT, slug + '.png')
    svg = os.path.join(OUT, slug + '.svg')
    fig.savefig(png, facecolor='white')
    fig.savefig(svg, facecolor='white')
    plt.close(fig)
    meta['file'] = slug
    REGISTRY.append(meta)


def ellipse(a, b, n=200):
    t = np.linspace(0, np.pi / 2, n)
    return a * np.cos(t), b * np.sin(t)


def ell_y(a, b, x):
    return b * np.sqrt(max(0.0, 1 - (x / a) ** 2))


# =========================================================================================
# TOPIC 1.3 / 1.4  PRODUCTION POSSIBILITY CURVES
# =========================================================================================

def g_ppc_anatomy():
    fig, (ax,) = new_fig('A production possibility curve: on, inside and beyond')
    frame(ax, 'Good X (units per year)', 'Good Y (units per year)', (0, 115), (0, 125))
    x, y = ellipse(90, 90)
    draw_xy(ax, x, y, BLUE, 'PPC', lx=92, ly=6)
    pt(ax, 90 * np.cos(0.8), 90 * np.sin(0.8), 'A', guides=False, off=(8, 6))
    pt(ax, 35, 40, 'B', guides=False, off=(8, 6))
    pt(ax, 98, 55, 'C', guides=False, off=(8, 6))
    note(ax, 0.45, 0.99, 'A  on the curve: resources fully and\n    efficiently employed\n'
         'B  inside: resources idle or misused\n'
         'C  beyond: cannot be produced with\n    current resources and technology')
    save(fig, '0455-T1.4-G01-ppc-on-inside-beyond', dict(
        topic='1.4', kind='generic', shows='PPC with a point on the curve (A), inside (B) and beyond (C).',
        cards=['ITEM-0455-1.4-001-DEF', 'ITEM-0455-1.4-006-DEF', 'ITEM-0455-1.4-021-FEATURE',
               'ITEM-0455-1.4-022-FEATURE', 'ITEM-0455-1.4-010-CHAIN'],
        blocks=['CU-0455-1.4.1 / 1.4.1-b3', 'CU-0455-1.4.2 / 1.4.2-b2'], figures='none (generic)'))


def g_ppc_opportunity_cost():
    fig, (ax,) = new_fig('Opportunity cost on a production possibility curve')
    frame(ax, 'Good X (units per year)', 'Good Y (units per year)', (0, 110), (0, 110),
          xticks={45: 'X1', 70: 'X2'}, yticks={ell_y(90, 90, 45): 'Y1', ell_y(90, 90, 70): 'Y2'})
    x, y = ellipse(90, 90)
    draw_xy(ax, x, y, BLUE, 'PPC', lx=92, ly=6)
    ya, yb = ell_y(90, 90, 45), ell_y(90, 90, 70)
    pt(ax, 45, ya, 'A')
    pt(ax, 70, yb, 'B')
    arrow(ax, (45, ya), (70, yb), INK, rad=-0.15)
    ax.annotate('', (100, ya), (100, yb), arrowprops=dict(arrowstyle='<->', color=ORANGE, lw=1.8))
    ax.text(101.5, (ya + yb) / 2, 'Y given up =\nopportunity cost', color=ORANGE, fontsize=12.5, va='center')
    ax.annotate('', (45, 8), (70, 8), arrowprops=dict(arrowstyle='<->', color=BLUE, lw=1.8))
    ax.text(57.5, 10, 'X gained', color=BLUE, fontsize=12.5, ha='center', va='bottom')
    save(fig, '0455-T1.3-G02-ppc-opportunity-cost', dict(
        topic='1.3', kind='generic', shows='Moving from A to B along a PPC: the Y given up is the opportunity cost of the X gained.',
        cards=['ITEM-0455-1.3-001-DEF', 'ITEM-0455-1.3-003-DEF', 'ITEM-0455-1.4-011-DEF', 'ITEM-0455-1.4-013-INTERP'],
        blocks=['CU-0455-1.3.1 / 1.3.1-b4', 'CU-0455-1.4.1 / 1.4.1-b4'], figures='none (generic)'))


def g_ppc_move_vs_shift():
    fig, (a1, a2) = new_fig('Movement along a PPC versus a shift of the PPC', panels=2)
    for ax, sub in ((a1, 'Movement along: the choice changes'), (a2, 'Shift: capacity changes')):
        frame(ax, 'Good X', 'Good Y', (0, 120), (0, 120), sub=sub)
    x, y = ellipse(90, 90)
    draw_xy(a1, x, y, BLUE, 'PPC', lx=92, ly=6)
    pa, pb = (45, ell_y(90, 90, 45)), (72, ell_y(90, 90, 72))
    pt(a1, *pa, 'A', guides=False); pt(a1, *pb, 'B', guides=False)
    arrow(a1, pa, pb, rad=-0.15)
    draw_xy(a2, x, y, BLUE, 'PPC1', lx=92, ly=6)
    x2, y2 = ellipse(108, 108)
    draw_xy(a2, x2, y2, ORANGE, 'PPC2', lx=103, ly=20)
    for t in (0.35, 0.8, 1.2):
        arrow(a2, (90 * np.cos(t), 90 * np.sin(t)), (106 * np.cos(t), 106 * np.sin(t)), ORANGE)
    save(fig, '0455-T1.4-G03-ppc-movement-vs-shift', dict(
        topic='1.4', kind='generic', shows='Left: movement along the PPC from A to B (reallocation). Right: outward shift from PPC1 to PPC2 (capacity grows).',
        cards=['ITEM-0455-1.4-011-DEF', 'ITEM-0455-1.4-016-DEF', 'ITEM-0455-1.4-023-FEATURE',
               'ITEM-0455-1.4-024-FEATURE', 'ITEM-0455-1.4-P03'],
        blocks=['CU-0455-1.4.4 / 1.4.4-b2', 'CU-0455-1.4.3 / 1.4.3-b4'], figures='none (generic)'))


def s_1_4_rising_cost():
    xs = np.linspace(0, 30, 300)
    fig, (ax,) = new_fig('Rising opportunity cost along the PPC')
    frame(ax, 'Fish (tonnes)', 'Maize (tonnes)', (0, 36), (0, 70),
          xticks={15: '15', 25: '25', 28: '28'}, yticks={10: '10', 25: '25', 45: '45', 60: '60'})
    draw_xy(ax, xs, FISH_MAIZE(xs), BLUE, 'PPC', lx=30.4, ly=3)
    pt(ax, 15, 45, 'A'); pt(ax, 25, 25, 'B'); pt(ax, 28, 10, 'C')
    arrow(ax, (15, 45), (25, 25), rad=-0.1); arrow(ax, (25, 25), (28, 10), rad=-0.1)
    note(ax, 0.42, 0.98, 'A to B: +10 t fish for -20 t maize (2 per tonne)\nB to C: +3 t fish for -15 t maize (5 per tonne)\n'
         'The cost per tonne rises: the curve bows out')
    save(fig, '0455-T1.4-S32-ppc-rising-opportunity-cost', dict(
        topic='1.4', kind='notes', shows='The fish and maize PPC with A (15 fish, 45 maize), B (25, 25) and C (28, 10): each extra tonne of fish costs more maize.',
        cards=['ITEM-0455-1.4-013-INTERP', 'ITEM-0455-1.4-015-CHAIN', 'ITEM-0455-1.4-P03'], blocks=['CU-0455-1.4.3 / 1.4.3-b3', 'CU-0455-1.4.1 / 1.4.1-b4'],
        figures='intercepts 60 maize, 30 fish; A (15, 45), B (25, 25), C (28, 10)'))


def g_ppc_inward():
    fig, (ax,) = new_fig('An inward shift of the PPC: capacity shrinks')
    frame(ax, 'Good X (units per year)', 'Good Y (units per year)', (0, 115), (0, 115))
    x, y = ellipse(100, 100)
    draw_xy(ax, x, y, BLUE, 'PPC1', lx=101, ly=6)
    x2, y2 = ellipse(72, 72)
    draw_xy(ax, x2, y2, ORANGE, 'PPC2', lx=60, ly=8, ha='right')
    for t in (0.35, 0.8, 1.2):
        arrow(ax, (98 * np.cos(t), 98 * np.sin(t)), (74 * np.cos(t), 74 * np.sin(t)), ORANGE)
    note(ax, 0.55, 0.98, 'e.g. a drought ruins grazing land,\nor a flood destroys boats and\nprocessing halls')
    save(fig, '0455-T1.4-G04-ppc-inward-shift', dict(
        topic='1.4', kind='generic', shows='Inward shift from PPC1 to PPC2 after a loss of resources.',
        cards=['ITEM-0455-1.4-016-DEF', 'ITEM-0455-1.4-020-CHAIN'],
        blocks=['CU-0455-1.4.4 / 1.4.4-b2', 'CU-0455-1.4.4 / 1.4.4-b4'], figures='none (generic)'))


# notes 1.4.3-b3: intercepts 60 / 30 through A (15, 45), B (25, 25), C (28, 10); two shaping nodes keep it bowed
FISH_MAIZE = PchipInterpolator([0, 7, 15, 20, 25, 28, 30], [60, 53.4, 45, 36.5, 25, 10, 0])


def s_1_4_002():
    # vertical maize ('000 t), horizontal fish ('000 t); intercepts 60 and 30; A(20,40), B(25,25)
    def f(params):
        p, q = params
        g = lambda x: 60 * (1 - (x / 30) ** p) ** (1 / q)
        return [g(20) - 40, g(25) - 25]
    p, q = fsolve(f, [2.5, 1.2])
    xs = np.linspace(0, 30, 300)
    ys = 60 * np.clip(1 - (xs / 30) ** p, 0, None) ** (1 / q)
    fig, (ax,) = new_fig('Movement along a PPC: maize meal into canned fish')
    frame(ax, "Canned fish ('000 tonnes a year)", "Maize meal ('000 tonnes a year)", (0, 36), (0, 70),
          xticks={20: '20', 25: '25', 30: '30'}, yticks={25: '25', 40: '40', 60: '60'})
    draw_xy(ax, xs, ys, BLUE, 'PPC1', lx=30.4, ly=3)
    pt(ax, 20, 40, 'A'); pt(ax, 25, 25, 'B')
    arrow(ax, (20, 40), (25, 25), rad=-0.1)
    note(ax, 0.45, 0.98, 'A to B: +5 000 t fish, -15 000 t maize meal\n'
         'Opportunity cost of the 5 000 t of fish\n= 15 000 t of maize meal')
    save(fig, '0455-T1.4-S01-ppc-movement-fish-maize', dict(
        topic='1.4', kind='card', shows='PPC1 from 60 000 t maize meal to 30 000 t fish; movement along it from A (20 000 fish, 40 000 maize) to B (25 000 fish, 25 000 maize).',
        cards=['ITEM-0455-1.4-002-DIAGRAM'], blocks=['CU-0455-1.4.1 / 1.4.1-b2'],
        figures='intercepts 60 000 t maize, 30 000 t fish; A (20 000, 40 000); B (25 000, 25 000) - B corrected from 30 000 t of fish, which is the fish intercept'))


def s_1_4_007():
    a, b = 30, 50 / np.sqrt(1 - (20 / 30) ** 2)
    fig, (ax,) = new_fig('Points on, inside and beyond an island economy’s PPC')
    frame(ax, 'Shrimp (tonnes per season)', 'Rice (tonnes per season)', (0, 36), (0, 80),
          xticks={14: '14', 20: '20', 25: '25'}, yticks={40: '40', 50: '50', 60: '60'})
    x, y = ellipse(a, b)
    draw_xy(ax, x, y, BLUE, 'PPC1', lx=30.4, ly=3)
    pt(ax, 20, 50, 'Y'); pt(ax, 14, 40, 'X'); pt(ax, 25, 60, 'Z')
    arrow(ax, (14, 40), (20, 50), rad=0.1)
    note(ax, 0.55, 0.98, 'X  inside: 14% of boats idle\nY  on the curve: full use\nZ  beyond: not yet reachable')
    save(fig, '0455-T1.4-S02-ppc-points-rice-shrimp', dict(
        topic='1.4', kind='card', shows='PPC1 for rice and shrimp with X inside (40 rice, 14 shrimp), Y on (50, 20) and Z beyond (60, 25); arrow X to Y as the idle boats return.',
        cards=['ITEM-0455-1.4-007-DIAGRAM'], blocks=['CU-0455-1.4.2 / 1.4.2-b2', 'CU-0455-1.4.2 / 1.4.2-b4'],
        figures='Y (20 t shrimp, 50 t rice); X (14, 40); Z (25, 60)'))


def s_1_4_012():
    b, a, pw = 45, 23.3, 2.26
    xs = np.linspace(0, a, 300)
    ys = b * np.clip(1 - (xs / a) ** pw, 0, None)
    fig, (ax,) = new_fig('Movement along a PPC: wine into machine tools')
    frame(ax, "Machine tools ('000 units a year)", 'Bottled wine (million litres a year)', (0, 28), (0, 52),
          xticks={12: '12', 18: '18'}, yticks={20: '20', 35: '35'})
    draw_xy(ax, xs, ys, BLUE, 'PPC1', lx=a + 0.4, ly=2)
    pt(ax, 12, 35, 'A'); pt(ax, 18, 20, 'B')
    arrow(ax, (12, 35), (18, 20), rad=-0.1)
    note(ax, 0.5, 0.98, 'A to B: +6 000 machine tools,\n-15 million litres of wine\nThe curve does not move')
    save(fig, '0455-T1.4-S03-ppc-movement-wine-tools', dict(
        topic='1.4', kind='card', shows='Movement along PPC1 from A (12 000 tools, 35 m litres) to B (18 000 tools, 20 m litres).',
        cards=['ITEM-0455-1.4-012-DIAGRAM', 'ITEM-0455-1.4-015-CHAIN'], blocks=['CU-0455-1.4.3 / 1.4.3-b2'],
        figures='A (12 000, 35); B (18 000, 20); intercepts drawn, not stated on the card'))


def s_1_4_017():
    fig, (ax,) = new_fig('An outward shift of the PPC: technical colleges')
    frame(ax, 'Aircraft (units per year)', 'Soyabeans (million tonnes a year)', (0, 62), (0, 140),
          xticks={39: '39', 52: '52'}, yticks={80: '80', 100: '100', 120: '120'})
    x, y = ellipse(40, 100)
    draw_xy(ax, x, y, BLUE, 'PPC1', lx=37.5, ly=30, ha='right')
    x2, y2 = ellipse(52, 120)
    draw_xy(ax, x2, y2, ORANGE, 'PPC2', lx=52.6, ly=6)
    for t in (0.4, 0.9, 1.3):
        arrow(ax, (40 * np.cos(t), 100 * np.sin(t)), (52 * np.cos(t), 120 * np.sin(t)), ORANGE)
    yc = ell_y(52, 120, 39)
    pt(ax, 39, yc, 'C')
    note(ax, 0.55, 0.98, 'C: 39 aircraft with 80 million t\nof soyabeans - beyond PPC1,\non PPC2')
    save(fig, '0455-T1.4-S04-ppc-outward-shift-colleges', dict(
        topic='1.4', kind='card', shows='PPC1 (100 m t soyabeans, 40 aircraft) shifts out to PPC2 (120 m t, 52 aircraft); point C on PPC2.',
        cards=['ITEM-0455-1.4-017-DIAGRAM', 'ITEM-0455-1.4-024-FEATURE'], blocks=['CU-0455-1.4.4 / 1.4.4-b3'],
        figures='PPC1 100 / 40; PPC2 120 / 52; C (39 aircraft, 80 m t) - corrected from 48 aircraft, which lies outside PPC2'))


# =========================================================================================
# TOPIC 2.3 / 2.4  DEMAND AND SUPPLY CURVES
# =========================================================================================

def g_demand_move_shift():
    fig, (a1, a2) = new_fig('Demand: movement along the curve versus a shift of the curve', panels=2)
    frame(a1, 'Quantity', 'Price', (0, 110), (0, 140), xticks={40: 'Q1', 70: 'Q2'}, yticks={70: 'P1', 40: 'P2'},
          sub='A change in the good’s own price')
    D = lin((10, 100), (100, 10))
    draw_qp(a1, D, (12, 98), BLUE, 'D', dx=2)
    pt(a1, 40, 70, 'A'); pt(a1, 70, 40, 'B')
    arrow(a1, (40, 70), (70, 40), rad=0)
    note(a1, 0.38, 0.98, 'Price falls: extension in demand\nPrice rises: contraction in demand')
    frame(a2, 'Quantity', 'Price', (0, 120), (0, 140), sub='A change in a condition of demand')
    draw_qp(a2, lin((10, 90), (80, 20)), (20, 90), BLUE, 'D1', dx=2)
    draw_qp(a2, lin((35, 90), (105, 20)), (20, 90), ORANGE, 'D2', dx=2)
    draw_qp(a2, lin((0, 75), (55, 20)), (20, 75), GREEN, 'D3', dx=2)
    arrow(a2, (52, 48), (76, 48), ORANGE)
    arrow(a2, (45, 55), (21, 55), GREEN)
    note(a2, 0.42, 0.98, 'D1 to D2: increase in demand\nD1 to D3: decrease in demand\n(income, tastes, prices of\nrelated goods, population ...)')
    save(fig, '0455-T2.3-G05-demand-movement-vs-shift', dict(
        topic='2.3', kind='generic', shows='Left: movement along D from a price change. Right: shifts of the demand curve, right (increase) and left (decrease).',
        cards=['ITEM-0455-2.3-014-DEF', 'ITEM-0455-2.3-020-FEATURE', 'ITEM-0455-2.3-017-APP', 'ITEM-0455-2.3-018-CHAIN', 'ITEM-0455-2.3-P03'],
        blocks=['CU-0455-2.3.2 / 2.3.2-b4', 'CU-0455-2.3.4 / 2.3.4-b2', 'CU-0455-2.3.4 / 2.3.4-b5'], figures='none (generic)'))


def g_supply_move_shift():
    fig, (a1, a2) = new_fig('Supply: movement along the curve versus a shift of the curve', panels=2)
    frame(a1, 'Quantity', 'Price', (0, 110), (0, 140), xticks={40: 'Q1', 70: 'Q2'}, yticks={40: 'P1', 70: 'P2'},
          sub='A change in the good’s own price')
    S = lin((10, 10), (100, 100))
    draw_qp(a1, S, (12, 98), BLUE, 'S', dx=2)
    pt(a1, 40, 40, 'A'); pt(a1, 70, 70, 'B')
    arrow(a1, (40, 40), (70, 70))
    note(a1, 0.03, 0.98, 'Price rises: extension in supply\nPrice falls: contraction in supply')
    frame(a2, 'Quantity', 'Price', (0, 120), (0, 140), sub='A change in a condition of supply')
    draw_qp(a2, lin((20, 20), (90, 90)), (20, 90), BLUE, 'S1', dx=2)
    draw_qp(a2, lin((45, 20), (115, 90)), (20, 85), ORANGE, 'S2', dx=2)
    draw_qp(a2, lin((0, 30), (60, 90)), (30, 90), GREEN, 'S3', dx=2)
    arrow(a2, (55, 55), (79, 55), ORANGE)
    arrow(a2, (55, 55), (31, 55), GREEN)
    note(a2, 0.03, 0.98, 'S1 to S2: increase in supply\nS1 to S3: decrease in supply\n(costs, weather, technology,\nsubsidies, taxes ...)')
    save(fig, '0455-T2.4-G06-supply-movement-vs-shift', dict(
        topic='2.4', kind='generic', shows='Left: movement along S from a price change. Right: shifts of the supply curve, right (increase) and left (decrease).',
        cards=['ITEM-0455-2.4-014-DEF', 'ITEM-0455-2.4-020-FEATURE', 'ITEM-0455-2.4-018-CHAIN', 'ITEM-0455-2.4-P03'],
        blocks=['CU-0455-2.4.2 / 2.4.2-b4', 'CU-0455-2.4.4 / 2.4.4-b5'], figures='none (generic)'))


def s_2_3_002():
    D = lin((300, 12), (380, 10))
    fig, (ax,) = new_fig('A movement along the demand curve: yoghurt in Otavi')
    frame(ax, 'Quantity (tubs a week)', 'Price (N$ per tub)', (180, 520), (7, 16),
          xticks={300: '300', 380: '380'}, yticks={10: '10', 12: '12'})
    draw_qp(ax, lin((300, 12), (380, 10)), (8, 15), BLUE, 'D', dx=8)
    draw_qp(ax, lin((300, 12), (420, 14)), (9.5, 14.5), MUTED, 'S1', lw=1.6, ls='--', dx=6)
    draw_qp(ax, lin((380, 10), (500, 12)), (8.5, 13), MUTED, 'S2', lw=1.6, ls='--', dx=6)
    pt(ax, 300, 12, 'A'); pt(ax, 380, 10, 'B')
    arrow(ax, (300, 12), (380, 10))
    save(fig, '0455-T2.3-S05-demand-movement-yoghurt', dict(
        topic='2.3', kind='card', shows='Demand curve D; movement along it from A (N$12, 300 tubs) to B (N$10, 380 tubs). S1 and S2 faint.',
        cards=['ITEM-0455-2.3-002-DIAGRAM'], blocks=[], figures='A (300, N$12); B (380, N$10)'))


def s_2_3_007():
    fig, (ax,) = new_fig('A movement up the demand curve: juice in Opuwo')
    frame(ax, 'Quantity (bottles a week)', 'Price (N$ per bottle)', (280, 640), (6, 18),
          xticks={380: '380', 500: '500'}, yticks={10: '10', 14: '14'})
    draw_qp(ax, lin((500, 10), (380, 14)), (7, 16.5), BLUE, 'D', dx=8, label_at='start')
    draw_qp(ax, lin((500, 10), (580, 12)), (8, 13), MUTED, 'S1', lw=1.6, ls='--', dx=6)
    draw_qp(ax, lin((380, 14), (460, 16)), (12, 17), MUTED, 'S2', lw=1.6, ls='--', dx=6)
    pt(ax, 500, 10, 'A'); pt(ax, 380, 14, 'B')
    arrow(ax, (500, 10), (380, 14))
    save(fig, '0455-T2.3-S06-demand-movement-juice', dict(
        topic='2.3', kind='card', shows='Movement up D from A (N$10, 500 bottles) to B (N$14, 380 bottles); poor-harvest supply shift shown faintly.',
        cards=['ITEM-0455-2.3-007-DIAGRAM'], blocks=[], figures='A (500, N$10); B (380, N$14)'))


def s_2_3_015():
    D1 = lambda p: 85 - 0.05 * p
    D2 = lambda p: 105 - 0.05 * p
    S = lambda p: -5 + 0.05 * p
    fig, (ax,) = new_fig('A shift of the demand curve: lodge rooms')
    frame(ax, 'Quantity (rooms a weekend)', 'Price (N$ a night)', (20, 95), (400, 1600),
          xticks={40: '40', 50: 'Q2', 60: '60'}, yticks={900: '900', 1100: 'P2'})
    draw_qp(ax, D1, (300, 1500), BLUE, 'D1', dx=-6, label_at='end')
    draw_qp(ax, D2, (500, 1500), ORANGE, 'D2', dx=2, label_at='end')
    draw_qp(ax, S, (300, 1500), INK2, 'S', dx=2)
    pt(ax, 40, 900, 'E1'); pt(ax, 50, 1100, 'E2')
    pt(ax, 60, 900, None)
    ax.annotate('60 rooms demanded\nat N$900 on D2', (60, 900), xytext=(10, -40), textcoords='offset points', fontsize=12, color=INK2)
    arrow(ax, (54, 620), (74, 620), ORANGE)
    save(fig, '0455-T2.3-S07-demand-shift-lodge', dict(
        topic='2.3', kind='card', shows='D1 shifts right to D2 (tastes); at N$900 demand rises from 40 to 60 rooms; new equilibrium E2 at a higher price P2 and quantity Q2 with supply S.',
        cards=['ITEM-0455-2.3-015-DIAGRAM'], blocks=['CU-0455-2.3.4 / 2.3.4-b3'], figures='E1 (40 rooms, N$900); 60 rooms at N$900 on D2; E2 shown symbolically (the card gives no figures)'))


def s_2_3_schedule():
    fig, (ax,) = new_fig('From schedule to curve: Kaoko Juice demand in Opuwo')
    frame(ax, 'Quantity (bottles a week)', 'Price (N$ per bottle)', (0, 110), (0, 18),
          xticks={40: '40', 60: '60', 90: '90'}, yticks={8: '8', 12: '12', 15: '15'})
    qs, ps = [30, 40, 60, 90, 100], [16.5, 15, 12, 8, 6.9]
    ax.plot(qs, ps, color=BLUE, lw=2.6)
    ax.text(101, 6.9, 'D', color=BLUE, fontsize=15, fontweight='bold', va='center')
    for q, p in [(40, 15), (60, 12), (90, 8)]:
        pt(ax, q, p)
    save(fig, '0455-T2.3-S25-demand-schedule-juice', dict(
        topic='2.3', kind='notes', shows='Demand curve drawn through the schedule: N$15 - 40, N$12 - 60, N$8 - 90 bottles.',
        cards=['ITEM-0455-2.3-020-FEATURE', 'ITEM-0455-2.3-006-DEF'], blocks=['CU-0455-2.3.2 / 2.3.2-b3', 'CU-0455-2.3.2 / 2.3.2-b5'],
        figures='(40, N$15), (60, N$12), (90, N$8)'))


def s_2_4_002():
    fig, (ax,) = new_fig('A movement along the supply curve: milk in Otavi')
    frame(ax, 'Quantity (litres a week)', 'Price (N$ per litre)', (300, 800), (5, 16),
          xticks={500: '500', 620: '620'}, yticks={10: '10', 12: '12'})
    draw_qp(ax, lin((500, 10), (620, 12)), (6, 14.5), BLUE, 'S', dx=8)
    draw_qp(ax, lin((500, 10), (400, 12)), (8, 13), MUTED, 'D1', lw=1.6, ls='--', dx=6, label_at='start')
    draw_qp(ax, lin((620, 12), (520, 14)), (10, 14.5), MUTED, 'D2', lw=1.6, ls='--', dx=6, label_at='start')
    pt(ax, 500, 10, 'A'); pt(ax, 620, 12, 'B')
    arrow(ax, (500, 10), (620, 12))
    save(fig, '0455-T2.4-S08-supply-movement-milk', dict(
        topic='2.4', kind='card', shows='Movement up S from A (N$10, 500 litres) to B (N$12, 620 litres).',
        cards=['ITEM-0455-2.4-002-DIAGRAM'], blocks=[], figures='A (500, N$10); B (620, N$12)'))


def s_2_4_007():
    fig, (ax,) = new_fig('A movement along the supply curve: ginger juice')
    frame(ax, 'Quantity (bottles a week)', 'Price (N$ per bottle)', (350, 1150), (4, 15),
          xticks={600: '600', 900: '900'}, yticks={8: '8', 12: '12'})
    draw_qp(ax, lin((600, 8), (900, 12)), (5, 14), BLUE, 'S', dx=10)
    draw_qp(ax, lin((600, 8), (480, 10)), (6.5, 10), MUTED, 'D1', lw=1.6, ls='--', dx=8, label_at='start')
    draw_qp(ax, lin((900, 12), (780, 14)), (10.5, 14), MUTED, 'D2', lw=1.6, ls='--', dx=8, label_at='start')
    pt(ax, 600, 8, 'A'); pt(ax, 900, 12, 'B')
    arrow(ax, (600, 8), (900, 12))
    save(fig, '0455-T2.4-S09-supply-movement-ginger-juice', dict(
        topic='2.4', kind='card', shows='Movement up S from A (N$8, 600 bottles) to B (N$12, 900 bottles).',
        cards=['ITEM-0455-2.4-007-DIAGRAM'], blocks=['CU-0455-2.4.2 / 2.4.2-b4'], figures='A (600, N$8); B (900, N$12)'))


def s_2_4_015():
    D = lambda p: 190 - p
    S1 = lambda p: 40 + (p - 150) / 3
    S2 = lambda p: 60 + (p - 150) / 3
    fig, (ax,) = new_fig('A shift of the supply curve: cheaper vinyl for sign painters')
    frame(ax, 'Quantity (signs a month)', 'Price (N$ per sign)', (10, 95), (80, 200),
          xticks={40: '40', 55: '55', 60: '60'}, yticks={135: '135', 150: '150'})
    draw_qp(ax, D, (110, 185), INK2, 'D', dx=2, label_at='start')
    draw_qp(ax, S1, (95, 195), BLUE, 'S1', dx=-8)
    draw_qp(ax, S2, (95, 185), ORANGE, 'S2', dx=2)
    pt(ax, 40, 150, 'E1'); pt(ax, 55, 135, 'E2', off=(-28, -24))
    ax.plot([60, 60], [80, 150], ls=(0, (2, 3)), color=INK2, lw=1.2)
    pt(ax, 60, 150, None, guides=False)
    arrow(ax, (42, 170), (61, 170), ORANGE)
    save(fig, '0455-T2.4-S10-supply-shift-signs', dict(
        topic='2.4', kind='card', shows='S1 shifts right to S2 after the vinyl cost falls; E1 (N$150, 40 signs) to E2 (N$135, 55 signs); 60 signs offered at N$150 on S2.',
        cards=['ITEM-0455-2.4-015-DIAGRAM', 'ITEM-0455-2.4-P04'], blocks=['CU-0455-2.4.4 / 2.4.4-b3'],
        figures='E1 (40, N$150); E2 (55, N$135); S2 at N$150 = 60'))


def s_2_4_schedule():
    fig, (ax,) = new_fig('From schedule to curve: Marula Foods supply')
    frame(ax, 'Quantity (packets a month)', 'Price (N$ per packet)', (0, 750), (0, 50),
          xticks={300: '300', 450: '450', 600: '600'}, yticks={20: '20', 30: '30', 40: '40'})
    draw_qp(ax, lin((300, 20), (600, 40)), (14, 45), BLUE, 'S', dx=8)
    for q, p in [(300, 20), (450, 30), (600, 40)]:
        pt(ax, q, p)
    save(fig, '0455-T2.4-S26-supply-schedule-marula', dict(
        topic='2.4', kind='notes', shows='Supply curve through the schedule: N$20 - 300, N$30 - 450, N$40 - 600 packets.',
        cards=['ITEM-0455-2.4-001-DEF', 'ITEM-0455-2.4-019-FEATURE'], blocks=['CU-0455-2.4.1 / 2.4.1-b3', 'CU-0455-2.4.2 / 2.4.2-b2'],
        figures='(300, N$20), (450, N$30), (600, N$40)'))


# =========================================================================================
# TOPIC 2.5 / 2.6  EQUILIBRIUM AND PRICE CHANGES
# =========================================================================================

def s_2_5_schedule():
    D = lambda p: 200 - 10 * p
    S = lambda p: 10 * p
    fig, (ax,) = new_fig('Finding the equilibrium: Kaoko Juice in Opuwo')
    frame(ax, 'Quantity (bottles a week)', 'Price (N$ per bottle)', (0, 160), (0, 15),
          xticks={80: '80', 100: '100', 120: '120'}, yticks={8: '8', 10: '10', 12: '12'})
    draw_qp(ax, D, (6.5, 14), BLUE, 'D', dx=3, label_at='start')
    draw_qp(ax, S, (6.5, 14), ORANGE, 'S', dx=3)
    pt(ax, 100, 10, 'E')
    ax.annotate('', (80, 12), (120, 12), arrowprops=dict(arrowstyle='<->', color=INK, lw=1.6))
    ax.text(100, 12.25, 'surplus 40', ha='center', fontsize=12.5)
    ax.annotate('', (80, 8), (120, 8), arrowprops=dict(arrowstyle='<->', color=INK, lw=1.6))
    ax.text(100, 7.35, 'shortage 40', ha='center', fontsize=12.5)
    save(fig, '0455-T2.5-S27-equilibrium-schedule-juice', dict(
        topic='2.5', kind='notes', shows='D and S from the schedules cross at E (N$10, 100 bottles); surplus of 40 at N$12, shortage of 40 at N$8.',
        cards=['ITEM-0455-2.5-001-DEF', 'ITEM-0455-2.5-011-FEATURE', 'ITEM-0455-2.5-P03'], blocks=['CU-0455-2.5.1 / 2.5.1-b3'],
        figures='D: 120/100/80 at N$8/10/12; S: 80/100/120 at N$8/10/12'))


def s_2_5_surplus_jam():
    D = lin((150, 30), (120, 40))
    S = lin((150, 30), (180, 40))
    fig, (ax,) = new_fig('Disequilibrium: jam held above its equilibrium price')
    frame(ax, 'Quantity (jars a week)', 'Price (N$ per jar)', (0, 230), (0, 50),
          xticks={120: '120', 150: '150', 180: '180'}, yticks={30: '30', 40: '40'})
    draw_qp(ax, D, (20, 46), BLUE, 'D', dx=3, label_at='start')
    draw_qp(ax, S, (20, 46), ORANGE, 'S', dx=3)
    pt(ax, 150, 30, 'E')
    ax.plot([0, 215], [40, 40], color=INK, lw=1.4, ls='--')
    ax.text(216, 40, 'price held\nat N$40', fontsize=12, va='center')
    ax.annotate('', (120, 40), (180, 40), arrowprops=dict(arrowstyle='<->', color=INK, lw=1.8))
    ax.text(150, 41, 'surplus 60', ha='center', va='bottom', fontsize=12.5)
    save(fig, '0455-T2.5-S28-surplus-jam', dict(
        topic='2.5', kind='notes', shows='Jam market clears at N$30 (150 jars); held at N$40, 120 jars demanded and 180 offered: surplus of 60.',
        cards=['ITEM-0455-2.5-006-DEF', 'ITEM-0455-2.5-012-FEATURE'], blocks=['CU-0455-2.5.2 / 2.5.2-b2', 'CU-0455-2.5.2 / 2.5.2-b3'],
        figures='E (150, N$30); at N$40: D 120, S 180'))


def s_2_5_002():
    S = lambda p: 220 + 4 * (p - 85)
    D1 = lambda p: 475 - 3 * p
    D2 = lambda p: 545 - 3 * p
    fig, (ax,) = new_fig('A rise in demand: school shirts in December')
    frame(ax, 'Quantity (shirts a month)', 'Price (N$ per shirt)', (150, 340), (60, 112),
          xticks={220: '220', 260: '260', 290: '290'}, yticks={85: '85', 95: '95'})
    draw_qp(ax, D1, (66, 108), BLUE, 'D1', dx=4, label_at='start')
    draw_qp(ax, D2, (66, 108), ORANGE, 'D2', dx=4, label_at='end')
    draw_qp(ax, S, (64, 108), INK2, 'S', dx=4)
    pt(ax, 220, 85, 'E1', off=(-30, 6)); pt(ax, 260, 95, 'E2', off=(8, 4))
    ax.annotate('', (220, 85), (290, 85), arrowprops=dict(arrowstyle='<->', color=INK, lw=1.6))
    ax.text(293, 86, 'shortage\nat N$85', ha='left', va='bottom', fontsize=12)
    arrow(ax, (185, 100), (232, 100), ORANGE)
    save(fig, '0455-T2.5-S11-demand-rise-shirts', dict(
        topic='2.5', kind='card', shows='D1 shifts to D2; shortage at N$85; new equilibrium E2 (N$95, 260 shirts) from E1 (N$85, 220).',
        cards=['ITEM-0455-2.5-002-DIAGRAM'], blocks=['CU-0455-2.5.1 / 2.5.1-b4'],
        figures='E1 (220, N$85); E2 (260, N$95); shortage gap at N$85 drawn to 290 (implied by the drawn D2)'))


def s_2_5_007():
    D = lambda p: 150 - (5 / 3) * (p - 30)
    S1 = lambda p: 150 + 5 * (p - 30)
    S2 = lambda p: 190 + 5 * (p - 30)
    fig, (ax,) = new_fig('A rise in supply: faster jam-filling equipment')
    frame(ax, 'Quantity (jars a week)', 'Price (N$ per jar)', (100, 230), (12, 40),
          xticks={150: '150', 160: '160', 190: '190'}, yticks={24: '24', 30: '30'})
    draw_qp(ax, D, (12, 38), INK2, 'D', dx=3, label_at='start')
    draw_qp(ax, S1, (17, 36), BLUE, 'S1', dx=3)
    draw_qp(ax, S2, (12, 36), ORANGE, 'S2', dx=4)
    pt(ax, 150, 30, 'E1', off=(-34, 6)); pt(ax, 160, 24, 'E2', off=(8, -22))
    ax.annotate('', (150, 30), (190, 30), arrowprops=dict(arrowstyle='<->', color=INK, lw=1.6))
    ax.text(192, 30, 'surplus 40', ha='left', va='center', fontsize=12)
    arrow(ax, (125, 20), (150, 20), ORANGE)
    save(fig, '0455-T2.5-S12-supply-rise-jam', dict(
        topic='2.5', kind='card', shows='S1 shifts to S2; surplus of 40 at N$30; new equilibrium E2 (N$24, 160 jars) from E1 (N$30, 150).',
        cards=['ITEM-0455-2.5-007-DIAGRAM'], blocks=['CU-0455-2.5.2 / 2.5.2-b4'], figures='E1 (150, N$30); S2 at N$30 = 190; E2 (160, N$24)'))


def g_four_shifts():
    fig, axes = new_fig('Four shifts, four consequences', panels=4)
    subs = ['Demand increases', 'Demand decreases', 'Supply increases', 'Supply decreases']
    for k, (ax, sub) in enumerate(zip(axes, subs)):
        frame(ax, 'Quantity', 'Price', (0, 120), (0, 110), sub=sub)
        D1 = lin((20, 90), (90, 20)); S1 = lin((20, 20), (90, 90))
        if k == 0:
            D2 = lin((40, 90), (110, 20)); curves = [(D1, BLUE, 'D1'), (D2, ORANGE, 'D2'), (S1, INK2, 'S')]
            e1, e2 = (55, 55), (65, 65); txt = 'P up, Q up'
        elif k == 1:
            D2 = lin((0, 90), (70, 20)); curves = [(D1, BLUE, 'D1'), (D2, ORANGE, 'D2'), (S1, INK2, 'S')]
            e1, e2 = (55, 55), (45, 45); txt = 'P down, Q down'
        elif k == 2:
            S2 = lin((40, 20), (110, 90)); curves = [(S1, BLUE, 'S1'), (S2, ORANGE, 'S2'), (D1, INK2, 'D')]
            e1, e2 = (55, 55), (65, 45); txt = 'P down, Q up'
        else:
            S2 = lin((0, 20), (70, 90)); curves = [(S1, BLUE, 'S1'), (S2, ORANGE, 'S2'), (D1, INK2, 'D')]
            e1, e2 = (55, 55), (45, 65); txt = 'P up, Q down'
        for f, c, l in curves:
            draw_qp(ax, f, (20, 90), c, l, dx=2)
        pt(ax, *e1, 'E1', guides=False, off=(-30, -4)); pt(ax, *e2, 'E2', guides=False, off=(8, -4))
        note(ax, 0.62, 0.15, txt, fs=13.5, color=INK)
    save(fig, '0455-T2.6-G07-four-shifts', dict(
        topic='2.6', kind='generic', shows='Four panels: demand up, demand down, supply up, supply down, with the direction of price and quantity in each.',
        cards=['ITEM-0455-2.6-001-DEF', 'ITEM-0455-2.6-009-FEATURE', 'ITEM-0455-2.6-002-CHAIN', 'ITEM-0455-2.6-007-APP', 'ITEM-0455-2.6-008-CHAIN', 'ITEM-0455-2.6-P03'],
        blocks=['CU-0455-2.6.2 / 2.6.2-b2', 'CU-0455-2.6.2 / 2.6.2-b4'], figures='none (generic)'))


def s_2_6_005():
    S = lambda p: 900 + 50 * (p - 10)
    D1 = lambda p: 900 - 25 * (p - 10)
    D2 = lambda p: 1050 - 25 * (p - 10)
    fig, (ax,) = new_fig('A rise in demand for milk after a new mine opens')
    frame(ax, 'Quantity (litres a week)', 'Price (N$ per litre)', (700, 1250), (5, 16),
          xticks={900: '900', 1000: '1 000', 1050: '1 050'}, yticks={10: '10', 12: '12'})
    draw_qp(ax, D1, (6, 15.5), BLUE, 'D1', dx=-40)
    draw_qp(ax, D2, (6, 15.5), ORANGE, 'D2', dx=10)
    draw_qp(ax, S, (5.5, 15), INK2, 'S', dx=10)
    pt(ax, 900, 10, 'E1', off=(-34, 6)); pt(ax, 1000, 12, 'E2', off=(8, 6))
    ax.annotate('', (900, 10), (1050, 10), arrowprops=dict(arrowstyle='<->', color=INK, lw=1.6))
    ax.text(1062, 10.15, 'shortage 150 at N$10', ha='left', va='bottom', fontsize=12)
    save(fig, '0455-T2.6-S13-demand-rise-milk-mine', dict(
        topic='2.6', kind='card', shows='D1 shifts to D2 as incomes rise; shortage of 150 at N$10; E1 (N$10, 900 litres) to E2 (N$12, 1 000 litres).',
        cards=['ITEM-0455-2.6-005-DIAGRAM'], blocks=['CU-0455-2.6.2 / 2.6.2-b4'], figures='E1 (900, N$10); D2 at N$10 = 1 050; E2 (1 000, N$12)'))


# =========================================================================================
# TOPIC 2.7 / 2.8  ELASTICITY
# =========================================================================================

def g_ped():
    fig, (a1, a2) = new_fig('Price elasticity of demand: the same price rise, two responses', panels=2)
    for ax, sub, f, q2 in ((a1, 'Price-elastic demand (flatter)', lin((70, 40), (20, 60)), 20),
                           (a2, 'Price-inelastic demand (steeper)', lin((70, 40), (62, 60)), 62)):
        frame(ax, 'Quantity demanded', 'Price', (0, 110), (0, 100),
              xticks={q2: 'Q2', 70: 'Q1'}, yticks={40: 'P1', 60: 'P2'}, sub=sub)
        draw_qp(ax, f, (32, 66) if ax is a1 else (20, 80), BLUE, 'D', dx=2, label_at='start')
        pt(ax, 70, 40, 'A'); pt(ax, q2, 60, 'B', off=(-24, 6))
        arrow(ax, (70, 40), (q2, 60))
    note(a1, 0.45, 0.98, 'large fall in quantity:\nrevenue tends to fall')
    note(a2, 0.03, 0.2, 'small fall in quantity:\nrevenue tends to rise', fs=12.5)
    save(fig, '0455-T2.7-G08-ped-elastic-vs-inelastic', dict(
        topic='2.7', kind='generic', shows='Same price rise P1 to P2: large quantity response on a flatter (elastic) curve, small on a steeper (inelastic) curve.',
        cards=['ITEM-0455-2.7-001-DEF', 'ITEM-0455-2.7-020-FEATURE', 'ITEM-0455-2.7-019-APP', 'ITEM-0455-2.7-011-EVAL'],
        blocks=['CU-0455-2.7.2 / 2.7.2-b4', 'CU-0455-2.7.4 / 2.7.4-b2'], figures='none (generic)'))


def s_2_7_004():
    D = lambda p: 200 - 50 * (p - 10)
    fig, (ax,) = new_fig('Elastic demand: a small price rise, a large fall in sales')
    frame(ax, 'Quantity demanded (bottles a week)', 'Price (N$ per bottle)', (0, 340), (0, 15),
          xticks={100: 'Q2', 200: '200'}, yticks={10: '10', 12: '12'})
    draw_qp(ax, D, (7.5, 13.2), BLUE, 'D', dx=6)
    pt(ax, 200, 10, 'A'); pt(ax, 100, 12, 'B')
    arrow(ax, (200, 10), (100, 12))
    note(ax, 0.55, 0.98, 'Flat curve: the move along the\nquantity axis is large next to\nthe move along the price axis')
    save(fig, '0455-T2.7-S14-elastic-demand-juice', dict(
        topic='2.7', kind='card', shows='Flat demand curve; price rise N$10 to N$12 moves quantity from 200 to a much smaller Q2.',
        cards=['ITEM-0455-2.7-004-DIAGRAM'], blocks=['CU-0455-2.7.2 / 2.7.2-b4'], figures='A (200, N$10); B at N$12 with Q2 symbolic (the card gives no figure)'))


def s_2_7_013():
    fig, (ax,) = new_fig('Inelastic demand: a price rise raises total spending')
    q1, q2 = 100, 94
    frame(ax, 'Quantity demanded (sacks a week)', 'Price (N$ per sack)', (0, 150), (0, 130),
          xticks={}, yticks={100: '100', 110: '110'})
    ax.xaxis.labelpad = 26
    ax.text(q2 - 0.8, -3, 'Q2', ha='right', va='top', fontsize=13, color=INK2)
    ax.text(q1 + 0.8, -3, 'Q1', ha='left', va='top', fontsize=13, color=INK2)
    ax.add_patch(Rectangle((0, 0), q2, 100, fc=TINT_B, alpha=0.14, ec='none'))
    ax.add_patch(Rectangle((0, 100), q2, 10, fc=TINT_O, alpha=0.35, ec='none'))
    ax.add_patch(Rectangle((q2, 0), q1 - q2, 100, fc=MUTED, alpha=0.35, ec='none'))
    draw_qp(ax, lin((100, 100), (94, 110)), (75, 124), BLUE, 'D', dx=2)
    pt(ax, q1, 100, 'A'); pt(ax, q2, 110, 'B', off=(-24, 6))
    ax.text(45, 50, 'spending at both prices', ha='center', fontsize=12.5, color=INK2)
    ax.text(45, 105, 'gained: +N$10 on each sack still bought', ha='center', va='center', fontsize=11.5)
    ax.annotate('lost: the few sacks\nno longer bought', (97, 40), xytext=(110, 40), fontsize=11.5,
                va='center', arrowprops=dict(arrowstyle='-', color=INK2))
    save(fig, '0455-T2.7-S15-inelastic-demand-revenue-rice', dict(
        topic='2.7', kind='card', shows='Steep demand curve; price N$100 to N$110; spending rectangle gains the top strip and loses a thin side strip, so total spending rises.',
        cards=['ITEM-0455-2.7-013-DIAGRAM', 'ITEM-0455-2.7-012-DEF', 'ITEM-0455-2.7-016-CHAIN'], blocks=['CU-0455-2.7.4 / 2.7.4-b3'],
        figures='prices N$100 and N$110; quantities symbolic (the card gives none)'))


def g_pes():
    fig, (a1, a2) = new_fig('Price elasticity of supply: the same rise in demand, two outcomes', panels=2)
    for ax, sub, S, e2 in ((a1, 'Inelastic supply (steeper)', lin((50, 30), (58, 80)), None),
                           (a2, 'Elastic supply (flatter)', lin((50, 30), (100, 45)), None)):
        frame(ax, 'Quantity', 'Price', (0, 120), (0, 100), sub=sub)
        D1 = lin((50, 30), (20, 60)); D2 = lin((80, 30), (50, 60))
        draw_qp(ax, D1, (12, 75), BLUE, 'D1', dx=-14, label_at='end')
        draw_qp(ax, D2, (12, 75), ORANGE, 'D2', dx=2, label_at='end')
        draw_qp(ax, S, (20, 85) if ax is a1 else (17, 48), INK2, 'S', dx=2)
        pt(ax, 50, 30, 'E1', guides=False, off=(-32, -18))
        # solve D2 = S
        p = brentq(lambda pp: D2(pp) - S(pp), 0, 100)
        pt(ax, D2(p), p, 'E2', guides=False, off=(8, 4))
    note(a1, 0.45, 0.98, 'mostly a higher price')
    note(a2, 0.45, 0.98, 'mostly a larger quantity')
    save(fig, '0455-T2.8-G10-pes-inelastic-vs-elastic', dict(
        topic='2.8', kind='generic', shows='The same demand shift D1 to D2 lands mainly on price where supply is inelastic and mainly on quantity where supply is elastic.',
        cards=['ITEM-0455-2.8-001-DEF', 'ITEM-0455-2.8-008-DEF', 'ITEM-0455-2.8-007-CHAIN', 'ITEM-0455-2.8-009-CHAIN', 'ITEM-0455-2.8-012-DEF', 'ITEM-0455-2.8-011-EVAL'],
        blocks=['CU-0455-2.8.2 / 2.8.2-b4', 'CU-0455-2.8.4 / 2.8.4-b2'], figures='none (generic)'))


def s_2_8_004():
    S = lambda p: 300 + (2 / 3) * (p - 40)
    D1 = lambda p: 380 - 2 * p
    D2 = lambda p: 460 - 2 * p
    fig, (ax,) = new_fig('Inelastic supply: a festival weekend at the fish market')
    frame(ax, 'Quantity (kilos)', 'Price (N$ per kilo)', (240, 400), (15, 95),
          xticks={300: '300', 320: '320'}, yticks={40: '40', 70: '70'})
    draw_qp(ax, D1, (25, 70), BLUE, 'D1', dx=-12, label_at='start')
    draw_qp(ax, D2, (35, 90), ORANGE, 'D2', dx=3, label_at='start')
    draw_qp(ax, S, (17, 88), INK2, 'S1', dx=3)
    pt(ax, 300, 40, 'E1', off=(-36, -6)); pt(ax, 320, 70, 'E2', off=(10, 0))
    save(fig, '0455-T2.8-S16-inelastic-supply-fish', dict(
        topic='2.8', kind='card', shows='Steep supply S1; D1 shifts to D2; E1 (N$40, 300 kg) to E2 (N$70, 320 kg).',
        cards=['ITEM-0455-2.8-004-DIAGRAM'], blocks=['CU-0455-2.8.2 / 2.8.2-b4'], figures='E1 (300, N$40); E2 (320, N$70)'))


# =========================================================================================
# TOPIC 2.10 / 2.11  MARKET FAILURE AND INTERVENTION
# =========================================================================================

def s_2_10_007():
    S = lambda p: 300 + 20 * (p - 60)
    D1 = lambda p: 900 - 10 * p
    D2 = lambda p: 1800 - 10 * p
    fig, (ax,) = new_fig('Under-provision: flu vaccinations in Oshakati')
    frame(ax, 'Quantity (vaccinations a season)', 'Price (N$ per vaccination)', (0, 1450), (0, 130),
          xticks={300: '300', 900: '900'}, yticks={60: '60', 90: 'P2'})
    draw_qp(ax, D1, (32, 85), BLUE, 'D1', dx=10, label_at='start')
    draw_qp(ax, D2, (50, 125), ORANGE, 'D2', dx=10, label_at='start')
    draw_qp(ax, S, (46, 105), INK2, 'S', dx=10)
    pt(ax, 300, 60, 'E1'); pt(ax, 900, 90, 'E2')
    ax.annotate('', (300, 8), (900, 8), arrowprops=dict(arrowstyle='<->', color=ORANGE, lw=1.8))
    ax.text(600, 9.5, '600 under-provided', ha='center', va='bottom', fontsize=12.5, color=INK)
    note(ax, 0.55, 0.98, 'D1: buyers’ own benefit only\nD2: also counting the protection\n      given to others')
    save(fig, '0455-T2.10-S17-under-provision-vaccinations', dict(
        topic='2.10', kind='card', shows='Market settles at E1 (N$60, 300); a demand curve counting benefits to others (D2) would cross S near 900; gap of 600.',
        cards=['ITEM-0455-2.10-007-DIAGRAM', 'ITEM-0455-2.10-P03'], blocks=['CU-0455-2.10.3 / 2.10.3-b5'],
        figures='E1 (300, N$60); E2 near 900 at a higher price P2 (symbolic). No social-cost or marginal labels, which are outside 0455'))


def s_2_11_004():
    D = lambda p: 9000 - 500 * p
    S = lambda p: -1000 + 500 * p
    S1 = lambda p: -2000 + 500 * p
    fig, (ax,) = new_fig('An indirect tax of N$2 a litre on a sugary drink')
    frame(ax, 'Quantity (litres a week)', 'Price (N$ per litre)', (0, 6000), (0, 17),
          xticks={3500: '3 500', 4000: '4 000'}, yticks={9: '9', 10: '10', 11: '11'})
    ax.add_patch(Rectangle((0, 9), 3500, 2, fc=TINT_O, alpha=0.22, ec='none'))
    ax.text(150, 8.6, 'shaded: tax revenue  N$2 \u00d7 3\u2009500 = N$7\u2009000', ha='left', va='top', fontsize=12,
            bbox=dict(fc='white', ec='none', alpha=0.85, pad=1.5))
    draw_qp(ax, D, (7, 16), INK2, 'D', dx=60, label_at='start')
    draw_qp(ax, S, (4, 14), BLUE, 'S', dx=60)
    draw_qp(ax, S1, (6, 16), ORANGE, 'S1', dx=60)
    pt(ax, 4000, 10, 'E1', off=(8, -20)); pt(ax, 3500, 11, 'E2', off=(-10, 8), ha='right')
    ax.plot([3500, 3500], [9, 11], color=INK, lw=0)
    ax.annotate('', (5000, 11.95), (5000, 9.95), arrowprops=dict(arrowstyle='<->', color=ORANGE, lw=1.8))
    ax.text(5080, 10.95, 'N$2\ntax', fontsize=12, va='center', color=INK)
    save(fig, '0455-T2.11-S18-indirect-tax-sugary-drink', dict(
        topic='2.11', kind='card', shows='S shifts up by the N$2 tax to S1; E1 (N$10, 4 000 litres) to E2 (N$11, 3 500); sellers keep N$9; tax revenue N$7 000 shaded.',
        cards=['ITEM-0455-2.11-004-DIAGRAM', 'ITEM-0455-2.7-018-WHY', 'ITEM-0455-2.7-P04'], blocks=['CU-0455-2.11.2 / 2.11.2-b4'],
        figures='E1 (4 000, N$10); E2 (3 500, N$11); seller price N$9; revenue N$7 000 - card and block corrected from N$12 / 3 000, which assumed the whole tax passes to buyers'))


def g_subsidy():
    fig, (ax,) = new_fig('A subsidy to producers: supply shifts right')
    frame(ax, 'Quantity', 'Price', (0, 120), (0, 110), xticks={50: 'Q1', 62: 'Q2'}, yticks={50: 'P1', 38: 'P2'})
    D = lin((50, 50), (20, 80)); S1 = lin((50, 50), (80, 80)); S2 = lin((74, 50), (104, 80))
    draw_qp(ax, D, (25, 95), INK2, 'D', dx=2, label_at='end')
    draw_qp(ax, S1, (20, 90), BLUE, 'S1', dx=2)
    draw_qp(ax, S2, (8, 82), ORANGE, 'S2', dx=2)
    pt(ax, 50, 50, 'E1', off=(-34, 4)); pt(ax, 62, 38, 'E2', off=(8, -18))
    ax.annotate('', (95, 71), (95, 59), arrowprops=dict(arrowstyle='<->', color=ORANGE, lw=1.8))
    ax.text(97, 65, 'subsidy\nper unit', fontsize=12, va='center')
    save(fig, '0455-T2.11-G11-subsidy', dict(
        topic='2.11', kind='generic', shows='A per-unit subsidy shifts supply down/right from S1 to S2: lower price, larger quantity.',
        cards=['ITEM-0455-2.4-017-APP', 'ITEM-0455-2.8-014-APP', 'ITEM-0455-2.11-009-FEATURE'], blocks=['CU-0455-2.11.2 / 2.11.2-b4 (last sentence)'],
        figures='none (generic)'))


def s_2_11_max_bread():
    fig, (ax,) = new_fig('A maximum price on bread: a shortage')
    frame(ax, "Quantity ('000 loaves a week)", 'Price (N$ per loaf)', (0, 12), (0, 15),
          xticks={5: '5', 7.5: '7.5', 9: '9'}, yticks={8: '8', 10: '10', 12: '12'})
    ax.plot([10, 9, 7.5, 6, 5.2], [6.7, 8, 10, 12, 13.3], color=BLUE, lw=2.6)
    ax.text(10.1, 6.7, 'D', color=BLUE, fontsize=15, fontweight='bold', va='center')
    ax.plot([4.3, 5, 7.5, 9.5, 10.3], [7, 8, 10, 12, 13], color=ORANGE, lw=2.6)
    ax.text(10.4, 13, 'S', color=ORANGE, fontsize=15, fontweight='bold', va='center')
    pt(ax, 7.5, 10, 'E')
    ax.plot([0, 11.2], [8, 8], color=INK, lw=1.6, ls='--')
    ax.text(11.25, 8, 'maximum\nprice N$8', fontsize=12, va='center')
    ax.annotate('', (5, 8), (9, 8), arrowprops=dict(arrowstyle='<->', color=INK, lw=1.8))
    ax.text(7, 7.7, 'shortage 4 000', ha='center', va='top', fontsize=12.5)
    save(fig, '0455-T2.11-S29-maximum-price-bread', dict(
        topic='2.11', kind='card', shows='Bread market clears at N$10 (7 500); a maximum price of N$8 gives 9 000 demanded and 5 000 supplied: shortage of 4 000.',
        cards=['ITEM-0455-2.11-005-INTERP', 'ITEM-0455-2.11-P01'], blocks=['CU-0455-2.11.2 / 2.11.2-b3'],
        figures='D 9 000 / 7 500 / 6 000 and S 5 000 / 7 500 / 9 500 at N$8 / 10 / 12'))


def s_2_11_min_beef():
    fig, (ax,) = new_fig('A minimum price on beef: a surplus')
    frame(ax, 'Quantity (tonnes a month)', 'Price (N$ per kg)', (0, 1500), (0, 85),
          xticks={700: '700', 900: '900', 1050: '1 050'}, yticks={45: '45', 54: '54', 72: '72'})
    ax.plot([1100, 900, 700, 500, 430], [36, 45, 54, 72, 80], color=BLUE, lw=2.6)
    ax.text(1110, 36, 'D', color=BLUE, fontsize=15, fontweight='bold', va='center')
    ax.plot([760, 900, 1050, 1300, 1380], [36, 45, 54, 72, 78], color=ORANGE, lw=2.6)
    ax.text(1390, 78, 'S', color=ORANGE, fontsize=15, fontweight='bold', va='center')
    pt(ax, 900, 45, 'E', off=(-4, 10), ha='center')
    ax.plot([0, 1300], [54, 54], color=INK, lw=1.6, ls='--')
    ax.text(150, 55, 'minimum price N$54', fontsize=12, va='bottom')
    ax.annotate('', (700, 54), (1050, 54), arrowprops=dict(arrowstyle='<->', color=INK, lw=1.8))
    ax.text(875, 56.5, 'surplus 350', ha='center', va='bottom', fontsize=12.5)
    save(fig, '0455-T2.11-S30-minimum-price-beef', dict(
        topic='2.11', kind='card', shows='Beef clears at N$45 (900 t); a minimum price of N$54 gives 700 demanded and 1 050 supplied: surplus of 350 t.',
        cards=['ITEM-0455-2.11-P02'], blocks=['CU-0455-2.11.2 / 2.11.2-b3'],
        figures='D 900 / 700 / 500 and S 900 / 1 050 / 1 300 at N$45 / 54 / 72'))


# =========================================================================================
# TOPIC 3.3 / 3.7 / 3.8
# =========================================================================================

def s_3_3_labour():
    S = lambda w: 1200 + 5 * (w - 100)
    D1 = lambda w: 1200 - 5 * (w - 100)
    D2 = lambda w: 1350 - 5 * (w - 130)
    fig, (ax,) = new_fig('A rise in demand for certified water engineers')
    frame(ax, 'Number of certified engineers', 'Wage (N$ a month)', (900, 1700), (30, 190),
          xticks={1200: '1 200', 1350: '1 350'}, yticks={100: 'W1', 130: 'W2'})
    draw_qp(ax, D1, (45, 170), BLUE, 'D1', dx=-60, label_at='end')
    draw_qp(ax, D2, (75, 180), ORANGE, 'D2', dx=15, label_at='end')
    draw_qp(ax, S, (50, 175), INK2, 'S1', dx=15)
    pt(ax, 1200, 100, 'E1', off=(-38, 4)); pt(ax, 1350, 130, 'E2', off=(10, 4))
    ax.annotate('', (1200, 100), (1500, 100), arrowprops=dict(arrowstyle='<->', color=INK, lw=1.6))
    ax.text(1510, 100, 'shortage at W1', ha='left', va='center', fontsize=12)
    save(fig, '0455-T3.3-S19-labour-market-engineers', dict(
        topic='3.3', kind='card', shows='Demand for engineers shifts D1 to D2; shortage at W1; wage rises to W2 and employment from 1 200 to 1 350.',
        cards=['ITEM-0455-3.3-008-SYNTH', 'ITEM-0455-3.3-005-CHAIN', 'ITEM-0455-3.3-011-CHAIN'], blocks=['CU-0455-3.3.3 / 3.3.3-b4'],
        figures='employment 1 200 to 1 350; wages symbolic W1, W2 (the card gives none)'))


def g_labour():
    fig, (ax,) = new_fig('Wage determination: demand for and supply of labour')
    frame(ax, 'Number of workers', 'Wage', (0, 120), (0, 110), xticks={55: 'L*'}, yticks={55: 'W*', 80: 'W high', 30: 'W low'})
    D = lin((20, 90), (90, 20)); S = lin((20, 20), (90, 90))
    draw_qp(ax, D, (20, 90), BLUE, 'D (employers)', dx=2, label_at='start')
    draw_qp(ax, S, (20, 90), ORANGE, 'S (workers)', dx=2)
    pt(ax, 55, 55, 'E')
    ax.annotate('', (30, 80), (80, 80), arrowprops=dict(arrowstyle='<->', color=INK, lw=1.4))
    ax.text(55, 81.5, 'surplus of workers: wage pressed down', ha='center', va='bottom', fontsize=11.5)
    ax.annotate('', (30, 30), (80, 30), arrowprops=dict(arrowstyle='<->', color=INK, lw=1.4))
    ax.text(55, 28, 'shortage of workers: wage bid up', ha='center', va='top', fontsize=11.5)
    save(fig, '0455-T3.3-G14-wage-determination', dict(
        topic='3.3', kind='generic', shows='Labour market: equilibrium wage W* where demand for and supply of labour meet; surplus above, shortage below.',
        cards=['ITEM-0455-3.3-004-DEF', 'ITEM-0455-3.3-006-APP', 'ITEM-0455-3.3-P02'], blocks=['CU-0455-3.3.2 / 3.3.2-b2', 'CU-0455-3.3.2 / 3.3.2-b3'],
        figures='none (generic)'))


def s_3_7_004():
    q = np.linspace(110, 800, 300)
    afc = 6000 / q
    atc = afc + 15
    fig, (ax,) = new_fig('Average costs fall as output rises: Kaoko Juice')
    frame(ax, 'Output (crates a month)', 'Cost (N$ per crate)', (0, 860), (0, 75),
          xticks={200: '200', 600: '600'}, yticks={10: '10', 25: '25', 30: '30', 45: '45'})
    draw_xy(ax, q, atc, BLUE, 'ATC1', lx=805, ly=atc[-1] + 1)
    draw_xy(ax, q, afc, ORANGE, 'AFC1', lx=805, ly=afc[-1] - 1)
    pt(ax, 200, 45, 'A'); pt(ax, 600, 25, 'B')
    pt(ax, 200, 30, None); pt(ax, 600, 10, None)
    arrow(ax, (200, 45), (600, 25), rad=0.15)
    ax.annotate('', (700, 6000 / 700), (700, 6000 / 700 + 15), arrowprops=dict(arrowstyle='<->', color=INK, lw=1.4))
    ax.text(712, 6000 / 700 + 7.5, 'AVC\nN$15', fontsize=11.5, va='center')
    save(fig, '0455-T3.7-S20-average-costs-juice', dict(
        topic='3.7', kind='card', shows='AFC (N$6 000 / output) and ATC (AFC + N$15); movement from A (200 crates, N$45) to B (600 crates, N$25).',
        cards=['ITEM-0455-3.7-004-DIAGRAM'], blocks=[], figures='FC N$6 000; VC N$15 a crate; A (200, N$45), B (600, N$25); AFC N$30 and N$10'))


def s_3_8_002():
    D = lambda p: 3600 - 150 * (p - 30)
    S1 = lambda p: 3600 + 150 * (p - 30)
    S2 = lambda p: 3900 + 150 * (p - 28)
    fig, (ax,) = new_fig('New sellers enter: braai-wood at Swakopmund')
    frame(ax, 'Quantity (bundles a month)', 'Price (N$ per bundle)', (2400, 5200), (20, 38),
          xticks={3600: '3 600', 3900: '3 900'}, yticks={28: '28', 30: '30'})
    draw_qp(ax, D, (23, 36), INK2, 'D', dx=40, label_at='start')
    draw_qp(ax, S1, (22, 36), BLUE, 'S1', dx=-160)
    draw_qp(ax, S2, (22, 34), ORANGE, 'S2', dx=40)
    pt(ax, 3600, 30, 'E1', off=(-38, 6)); pt(ax, 3900, 28, 'E2', off=(10, -20))
    arrow(ax, (3900, 24.5), (4350, 24.5), ORANGE)
    save(fig, '0455-T3.8-S21-entry-braai-wood', dict(
        topic='3.8', kind='card', shows='Four new sellers shift S1 to S2; E1 (N$30, 3 600) to E2 (N$28, 3 900).',
        cards=['ITEM-0455-3.8-002-DIAGRAM'], blocks=[], figures='E1 (3 600, N$30); E2 (3 900, N$28)'))


def s_3_8_007():
    D = lambda p: 9000 - 600 * (p - 22)
    fig, (ax,) = new_fig('The demand curve facing a single fuel station')
    frame(ax, 'Quantity (litres a month)', 'Price (N$ per litre)', (4000, 12500), (15, 30),
          xticks={7200: '7 200', 9000: '9 000'}, yticks={22: '22', 25: '25'})
    draw_qp(ax, D, (17, 29), BLUE, 'D', dx=120)
    pt(ax, 9000, 22, 'E1'); pt(ax, 7200, 25, 'E2')
    arrow(ax, (9000, 22), (7200, 25))
    save(fig, '0455-T3.8-S22-single-seller-fuel', dict(
        topic='3.8', kind='card', shows='Downward-sloping demand facing the only station; price N$22 to N$25 moves sales from 9 000 to 7 200 litres along D.',
        cards=['ITEM-0455-3.8-007-DIAGRAM', 'ITEM-0455-3.8-008-INTERP'], blocks=['CU-0455-3.8.2 / 3.8.2-b3'],
        figures='E1 (9 000, N$22); E2 (7 200, N$25)'))


# =========================================================================================
# TOPIC 4.6  ECONOMIC GROWTH
# =========================================================================================

def s_4_6_008():
    a, b = 45, 60 / np.sqrt(1 - (30 / 45) ** 2)
    fig, (ax,) = new_fig('A recession: moving inside the PPC')
    frame(ax, 'Maize (tonnes a year)', 'Fish (tonnes a year)', (0, 52), (0, 95),
          xticks={24: '24', 30: '30'}, yticks={48: '48', 60: '60'})
    x, y = ellipse(a, b)
    draw_xy(ax, x, y, BLUE, 'PPC', lx=45.5, ly=3)
    pt(ax, 30, 60, 'A'); pt(ax, 24, 48, 'B', off=(-24, -20))
    arrow(ax, (30, 60), (24, 48))
    note(ax, 0.55, 0.98, 'The curve does not move:\ncapacity is unchanged.\nB inside = idle workers and boats')
    save(fig, '0455-T4.6-S23-recession-inside-ppc', dict(
        topic='4.6', kind='card', shows='Economy moves from A on the PPC (30 t maize, 60 t fish) to B inside it (24, 48); the curve stays put.',
        cards=['ITEM-0455-4.6-008-DIAGRAM', 'ITEM-0455-4.6-007-DEF', 'ITEM-0455-4.6-027-FEATURE'], blocks=['CU-0455-4.6.3 / 4.6.3-b4'],
        figures='A (30, 60); B (24, 48); intercepts drawn, not stated on the card'))


def s_4_6_013():
    a, b = 110, 40 / np.sqrt(1 - (80 / 110) ** 2)
    fig, (ax,) = new_fig('Growth in capacity: the PPC shifts outward')
    frame(ax, 'Beef (tonnes a year)', 'Copper (tonnes a year)', (0, 150), (0, 85),
          xticks={80: '80', 96: '96'}, yticks={40: '40', 48: '48'})
    x, y = ellipse(a, b)
    draw_xy(ax, x, y, BLUE, 'PPC1', lx=104, ly=6, ha='right')
    x2, y2 = ellipse(a * 1.2, b * 1.2)
    draw_xy(ax, x2, y2, ORANGE, 'PPC2', lx=133, ly=4)
    pt(ax, 80, 40, 'A', off=(-24, -20)); pt(ax, 96, 48, 'C')
    arrow(ax, (80, 40), (96, 48), ORANGE)
    note(ax, 0.6, 0.98, 'A fifth more of each good:\n80 to 96 t beef,\n40 to 48 t copper')
    save(fig, '0455-T4.6-S24-growth-outward-shift', dict(
        topic='4.6', kind='card', shows='PPC1 shifts out by a fifth to PPC2; A (80 t beef, 40 t copper) to C (96, 48).',
        cards=['ITEM-0455-4.6-013-DIAGRAM', 'ITEM-0455-4.6-012-DEF', 'ITEM-0455-4.6-016-CHAIN'], blocks=['CU-0455-4.6.4 / 4.6.4-b4'],
        figures='A (80, 40); C (96, 48)'))


def g_two_routes():
    fig, (a1, a2) = new_fig('Two routes to higher output', panels=2)
    for ax, sub in ((a1, 'Using spare capacity: towards the curve'), (a2, 'Growing capacity: the curve shifts out')):
        frame(ax, 'Good X', 'Good Y', (0, 120), (0, 120), sub=sub)
    x, y = ellipse(90, 90)
    draw_xy(a1, x, y, BLUE, 'PPC', lx=92, ly=6)
    pt(a1, 40, 40, 'A', guides=False); pt(a1, 60, 60, 'B', guides=False)
    arrow(a1, (40, 40), (60, 60))
    note(a1, 0.03, 0.2, 'more spending puts idle\nresources to work\n(demand-side)', fs=12.5)
    draw_xy(a2, x, y, BLUE, 'PPC1', lx=92, ly=6)
    x2, y2 = ellipse(108, 108)
    draw_xy(a2, x2, y2, ORANGE, 'PPC2', lx=103, ly=20)
    for t in (0.35, 0.8, 1.2):
        arrow(a2, (90 * np.cos(t), 90 * np.sin(t)), (106 * np.cos(t), 106 * np.sin(t)), ORANGE)
    note(a2, 0.03, 0.2, 'investment, technology, more or\nbetter-trained workers\n(supply-side)', fs=12.5)
    save(fig, '0455-T4.6-G09-two-routes-to-growth', dict(
        topic='4.6', kind='generic', shows='Left: a move from inside towards the PPC (spare capacity used). Right: an outward shift of the PPC (capacity grows).',
        cards=['ITEM-0455-4.6-028-FEATURE', 'ITEM-0455-4.6-020-DEF', 'ITEM-0455-4.6-023-EVAL', 'ITEM-0455-4.6-024-APP', 'ITEM-0455-4.6-P03', 'ITEM-0455-4.6-P04'],
        blocks=['CU-0455-4.6.4 / 4.6.4-b2', 'CU-0455-4.6.4 / 4.6.4-b3', 'CU-0455-4.6.6 / 4.6.6-b3', 'CU-0455-4.6.6 / 4.6.6-b4'], figures='none (generic)'))


# =========================================================================================
# TOPIC 6.3  FOREIGN EXCHANGE
# =========================================================================================

def s_6_3_005():
    fig, (ax,) = new_fig('The market for US dollars in Windhoek')
    frame(ax, 'Quantity of US dollars (millions)', 'Price of US$1 (N$)', (1.5, 9.5), (12.8, 17.2),
          xticks={3: '3', 4: '4', 5: '5', 6: '6', 7: '7'}, yticks={14: '14', 15: '15', 16: '16'})
    ax.plot([8, 7, 5, 4, 3.5], [13.5, 14, 15, 16, 16.7], color=BLUE, lw=2.6)
    ax.text(8.1, 13.5, 'D', color=BLUE, fontsize=15, fontweight='bold', va='center')
    ax.plot([2.5, 3, 5, 6, 6.6], [13.5, 14, 15, 16, 16.6], color=ORANGE, lw=2.6)
    ax.text(6.7, 16.6, 'S', color=ORANGE, fontsize=15, fontweight='bold', va='center')
    pt(ax, 5, 15, 'E', off=(10, -4))
    ax.annotate('', (4, 16), (6, 16), arrowprops=dict(arrowstyle='<->', color=INK, lw=1.4))
    ax.text(6.15, 16, 'surplus at N$16: price falls', ha='left', va='center', fontsize=11.5)
    ax.annotate('', (3, 14), (7, 14), arrowprops=dict(arrowstyle='<->', color=INK, lw=1.4))
    ax.text(4.3, 13.85, 'shortage at N$14: price rises', ha='left', va='top', fontsize=11.5)
    save(fig, '0455-T6.3-S31-fx-market-us-dollars', dict(
        topic='6.3', kind='card', shows='Market for US dollars: equilibrium at N$15 per US$1 with 5 million; surplus at N$16, shortage at N$14.',
        cards=['ITEM-0455-6.3-005-APP', 'ITEM-0455-6.3-003-DEF'], blocks=['CU-0455-6.3.2 / 6.3.2-b2'],
        figures='D 7 / 5 / 4 and S 3 / 5 / 6 million at N$14 / 15 / 16'))


def g_fx(kind):
    app = kind == 'app'
    title = ('Appreciation: demand for the Namibian dollar rises' if app
             else 'Depreciation: supply of the Namibian dollar rises')
    fig, (ax,) = new_fig(title)
    frame(ax, 'Quantity of Namibian dollars', 'Price of N$1 in foreign currency (e.g. euros)', (0, 120), (0, 135),
          xticks={55: 'Q1', (65 if app else 65): 'Q2'}, yticks={55: 'R1', (65 if app else 45): 'R2'})
    D1 = lin((20, 90), (90, 20)); S1 = lin((20, 20), (90, 90))
    if app:
        D2 = lin((40, 90), (110, 20))
        draw_qp(ax, D1, (20, 90), BLUE, 'D1', dx=2, label_at='start')
        draw_qp(ax, D2, (20, 90), ORANGE, 'D2', dx=2, label_at='start')
        draw_qp(ax, S1, (20, 90), INK2, 'S', dx=2)
        pt(ax, 55, 55, 'E1', off=(-32, -4)); pt(ax, 65, 65, 'E2')
        arrow(ax, (38, 72), (58, 72), ORANGE)
        txt = ('More foreign buyers of exports,\nmore tourists, more inflows of\nsavings (e.g. higher interest rates)\n'
               '→ N$1 buys more foreign currency')
    else:
        S2 = lin((40, 20), (110, 90))
        draw_qp(ax, S1, (20, 90), BLUE, 'S1', dx=2)
        draw_qp(ax, S2, (20, 85), ORANGE, 'S2', dx=2)
        draw_qp(ax, D1, (20, 90), INK2, 'D', dx=2, label_at='start')
        pt(ax, 55, 55, 'E1', off=(-32, -4)); pt(ax, 65, 45, 'E2', off=(8, -20))
        arrow(ax, (48, 30), (68, 30), ORANGE)
        txt = ('More Namibian dollars sold to pay\nfor imports or to buy assets abroad\n'
               '→ N$1 buys less foreign currency')
    note(ax, 0.5, 0.98, txt)
    save(fig, '0455-T6.3-G12-fx-appreciation' if app else '0455-T6.3-G13-fx-depreciation', dict(
        topic='6.3', kind='generic',
        shows=('Market for N$: demand shifts D1 to D2; the exchange rate rises from R1 to R2 (appreciation).' if app
               else 'Market for N$: supply shifts S1 to S2; the exchange rate falls from R1 to R2 (depreciation).'),
        cards=(['ITEM-0455-6.3-004-MECH', 'ITEM-0455-6.3-006-CHAIN', 'ITEM-0455-6.3-008-CHAIN', 'ITEM-0455-6.3-009-APP'] if app
               else ['ITEM-0455-6.3-007-DEF', 'ITEM-0455-6.3-011-CHAIN', 'ITEM-0455-6.3-P03']),
        blocks=(['CU-0455-6.3.2 / 6.3.2-b4', 'CU-0455-6.3.3 / 6.3.3-b3'] if app
                else ['CU-0455-6.3.2 / 6.3.2-b4', 'CU-0455-6.3.4 / 6.3.4-b2']),
        figures='none (generic)'))


# =========================================================================================
# ADDED 2026-10-13: special elasticities, intervention diagrams, costs, currency, pyramids
# =========================================================================================

def s_2_6_010():
    S = lambda p: 1200 + 100 * (p - 14)
    D1 = lambda p: 1200 - 100 * (p - 14)
    D2 = lambda p: 1000 - 100 * (p - 12)
    fig, (ax,) = new_fig('A fall in demand for bread after a factory closes')
    frame(ax, 'Quantity (loaves a week)', 'Price (N$ per loaf)', (500, 1700), (8, 22),
          xticks={1000: '1 000', 1200: '1 200'}, yticks={12: '12', 14: '14'})
    draw_qp(ax, D1, (9, 18), BLUE, 'D1', dx=10, label_at='start')
    draw_qp(ax, D2, (9, 18), ORANGE, 'D2', dx=10, label_at='start')
    draw_qp(ax, S, (9, 18), INK2, 'S', dx=10)
    pt(ax, 1200, 14, 'E1', off=(10, 2)); pt(ax, 1000, 12, 'E2', off=(-36, -22))
    ax.annotate('', (800, 14), (1200, 14), arrowprops=dict(arrowstyle='<->', color=INK, lw=1.6))
    ax.text(1000, 14.2, 'surplus at N$14', ha='center', va='bottom', fontsize=12)
    arrow(ax, (900, 16.5), (620, 16.5), ORANGE)
    note(ax, 0.02, 0.98, 'Lower incomes: demand shifts left, D1 to D2.\nS does not move. Price N$14 to N$12,\nsales 1 200 to 1 000 loaves a week')
    save(fig, '0455-T2.6-S33-demand-fall-bread', dict(
        topic='2.6', kind='card', shows='Demand for bread shifts left from D1 to D2 as incomes fall; surplus at N$14; E1 (N$14, 1 200 loaves) to E2 (N$12, 1 000 loaves) along an unchanged S.',
        cards=['ITEM-0455-2.6-010-DIAGRAM'], blocks=['CU-0455-2.6.2 / 2.6.2-b6'],
        figures='E1 (1 200, N$14); E2 (1 000, N$12); surplus at N$14 drawn without a figure (the card gives none)'))


def g_unit_ped():
    k = 2400
    fig, (ax,) = new_fig('Unit elastic demand: equal spending at every price')
    frame(ax, 'Quantity demanded', 'Price', (0, 120), (0, 110),
          xticks={30: 'Q1', 60: 'Q2'}, yticks={80: 'P1', 40: 'P2'})
    ax.add_patch(Rectangle((0, 0), 30, 80, fc=TINT_B, alpha=0.20, ec=BLUE, lw=1.2))
    ax.add_patch(Rectangle((0, 0), 60, 40, fc=TINT_O, alpha=0.20, ec=ORANGE, lw=1.2))
    draw_qp(ax, lambda p: k / p, (21, 104), BLUE, 'D  (PED = 1)', dx=2, label_at='start')
    pt(ax, 30, 80, 'A'); pt(ax, 60, 40, 'B')
    arrow(ax, (30, 80), (60, 40), rad=-0.15)
    ax.text(15, 60, 'P1 × Q1', ha='center', va='center', fontsize=12.5, color=BLUE, fontweight='bold')
    ax.text(45, 20, 'P2 × Q2', ha='center', va='center', fontsize=12.5, color=ORANGE, fontweight='bold')
    note(ax, 0.45, 0.98, 'The two rectangles have the same area:\nthe price change is offset exactly by\nthe change in quantity, so spending\ndoes not change. The curve bends\ntowards the origin.')
    save(fig, '0455-T2.7-G15-unit-elastic-demand', dict(
        topic='2.7', kind='generic', shows='A unit elastic demand curve (a rectangular hyperbola): the spending rectangles at A (P1, Q1) and B (P2, Q2) have equal areas.',
        cards=['ITEM-0455-2.7-021-DEF', 'ITEM-0455-2.7-025-MECH'], blocks=['CU-0455-2.7.2 / 2.7.2-b6', 'CU-0455-2.7.4 / 2.7.4-b6'],
        figures='none (generic)'))


def s_2_7_022():
    S1 = lambda p: 300 + 5 * (p - 40)
    S2 = lambda p: 300 + 5 * (p - 60)
    fig, (ax,) = new_fig('Perfectly inelastic demand: anti-venom for a hospital')
    frame(ax, 'Quantity (doses a week)', 'Price (N$ per dose)', (0, 500), (0, 90),
          xticks={300: '300'}, yticks={40: '40', 60: '60'})
    ax.plot([300, 300], [4, 84], color=BLUE, lw=2.6, solid_capstyle='round')
    ax.text(306, 84, 'D', color=BLUE, fontsize=15, fontweight='bold', va='center')
    draw_qp(ax, S1, (8, 80), INK2, 'S1', dx=8)
    draw_qp(ax, S2, (20, 86), ORANGE, 'S2', dx=-34)
    pt(ax, 300, 40, 'E1', off=(10, -22)); pt(ax, 300, 60, 'E2', off=(-36, 6))
    arrow(ax, (380, 44), (318, 56), ORANGE)
    note(ax, 0.02, 0.98, 'Costs rise: S1 shifts left to S2.\nPrice N$40 to N$60, quantity stays 300.\nPED = 0 / 50 = 0\nSpending N$12 000 to N$18 000 a week')
    save(fig, '0455-T2.7-S34-perfectly-inelastic-demand-antivenom', dict(
        topic='2.7', kind='card', shows='Vertical demand D at 300 doses; supply shifts left from S1 to S2; E1 (N$40, 300) to E2 (N$60, 300): the whole change lands on price.',
        cards=['ITEM-0455-2.7-022-DIAGRAM'], blocks=['CU-0455-2.7.2 / 2.7.2-b6'],
        figures='D vertical at 300; E1 (300, N$40); E2 (300, N$60); spending N$12 000 and N$18 000'))


def s_2_7_023():
    S1 = lambda p: 40 + 0.01 * (p - 5000)
    S2 = lambda p: 60 + 0.01 * (p - 5000)
    fig, (ax,) = new_fig('Perfectly elastic demand: a maize grower')
    frame(ax, 'Quantity (tonnes)', 'Price (N$ per tonne)', (0, 100), (0, 11000),
          xticks={40: '40', 60: '60'}, yticks={5000: '5 000'})
    ax.plot([2, 92], [5000, 5000], color=BLUE, lw=2.6, solid_capstyle='round')
    ax.text(93, 5000, 'D', color=BLUE, fontsize=15, fontweight='bold', va='center')
    draw_qp(ax, S1, (1500, 8200), INK2, 'S1', dx=-6)
    draw_qp(ax, S2, (2200, 8200), ORANGE, 'S2', dx=1.5)
    pt(ax, 40, 5000, 'E1', off=(-34, 6)); pt(ax, 60, 5000, 'E2', off=(8, -22))
    arrow(ax, (38, 2600), (58, 2600), ORANGE)
    note(ax, 0.02, 0.98, 'Good rains: S1 shifts right to S2.\nQuantity 40 to 60 tonnes; price stays N$5 000.\nPED is infinite.\nRevenue N$200 000 to N$300 000')
    save(fig, '0455-T2.7-S35-perfectly-elastic-demand-maize', dict(
        topic='2.7', kind='card', shows='Horizontal demand D at N$5 000 a tonne; supply shifts right from S1 to S2; E1 (40 t) to E2 (60 t) at the same price: the whole change lands on quantity.',
        cards=['ITEM-0455-2.7-023-DIAGRAM'], blocks=['CU-0455-2.7.2 / 2.7.2-b6'],
        figures='D horizontal at N$5 000; E1 (40, N$5 000); E2 (60, N$5 000); revenue N$200 000 and N$300 000'))


def g_unit_pes():
    fig, (ax,) = new_fig('Unit elastic supply: straight lines through the origin')
    frame(ax, 'Quantity supplied', 'Price', (0, 120), (0, 140))
    for slope, c, lab in ((2.2, BLUE, 'S1'), (1.0, ORANGE, 'S2'), (0.45, GREEN, 'S3')):
        qmax = min(100 / slope, 100)
        q = np.linspace(0, qmax, 200)
        draw_xy(ax, q, slope * q, c, lab, lx=qmax + 1.5, ly=slope * qmax)
    q0 = 40
    pt(ax, q0, 40, 'A', guides=False, off=(-22, 6)); pt(ax, 1.5 * q0, 60, 'B', guides=False, off=(-22, 6))
    arrow(ax, (q0, 40), (1.5 * q0, 60))
    note(ax, 0.06, 0.99, 'Any straight supply line that starts at the origin has\nPES = 1 at every point, whatever its slope:\nfrom A to B price rises 50% and quantity supplied 50%')
    save(fig, '0455-T2.8-G16-unit-elastic-supply', dict(
        topic='2.8', kind='generic', shows='Three straight supply lines of different slopes, each through the origin: all unit elastic (PES = 1); A to B on S2 shows equal percentage changes.',
        cards=['ITEM-0455-2.8-017-CALC'], blocks=['CU-0455-2.8.2 / 2.8.2-b6'], figures='none (generic)'))


def s_2_8_015():
    D1 = lambda p: 10000 - 40 * (p - 100)
    D2 = lambda p: 10000 - 40 * (p - 250)
    fig, (ax,) = new_fig('Perfectly inelastic supply: seats at a cup final')
    frame(ax, 'Quantity (tickets)', 'Price (N$ per ticket)', (0, 17000), (0, 420),
          xticks={10000: '10 000'}, yticks={100: '100', 250: '250'})
    ax.plot([10000, 10000], [8, 315], color=INK2, lw=2.6, solid_capstyle='round')
    ax.text(10200, 315, 'S', color=INK2, fontsize=15, fontweight='bold', va='center')
    draw_qp(ax, D1, (20, 300), BLUE, 'D1', dx=200, label_at='start')
    draw_qp(ax, D2, (100, 320), ORANGE, 'D2', dx=250, dy=14)
    pt(ax, 10000, 100, 'E1', off=(-38, 6)); pt(ax, 10000, 250, 'E2', off=(-38, 6))
    arrow(ax, (12200, 120), (13800, 160), ORANGE)
    note(ax, 0.02, 0.98, 'The final: D1 shifts right to D2.\nPrice N$100 to N$250, still 10 000 tickets.\nPES = 0')
    save(fig, '0455-T2.8-S36-perfectly-inelastic-supply-stadium', dict(
        topic='2.8', kind='card', shows='Vertical supply S at 10 000 seats; demand shifts right from D1 to D2; E1 (N$100) to E2 (N$250) with the quantity unchanged.',
        cards=['ITEM-0455-2.8-015-DIAGRAM'], blocks=['CU-0455-2.8.2 / 2.8.2-b6'],
        figures='S vertical at 10 000; E1 (10 000, N$100); E2 (10 000, N$250)'))


def s_2_8_016():
    D1 = lambda p: 200 - 5 * (p - 80)
    D2 = lambda p: 350 - 5 * (p - 80)
    fig, (ax,) = new_fig('Perfectly elastic supply: a T-shirt printer')
    frame(ax, 'Quantity (shirts a week)', 'Price (N$ per shirt)', (0, 600), (0, 140),
          xticks={200: '200', 350: '350'}, yticks={80: '80'})
    ax.plot([8, 555], [80, 80], color=INK2, lw=2.6, solid_capstyle='round')
    ax.text(560, 80, 'S', color=INK2, fontsize=15, fontweight='bold', va='center')
    draw_qp(ax, D1, (45, 120), BLUE, 'D1', dx=8, label_at='start')
    draw_qp(ax, D2, (45, 125), ORANGE, 'D2', dx=8, label_at='start')
    pt(ax, 200, 80, 'E1', off=(-34, 6)); pt(ax, 350, 80, 'E2', off=(8, 6))
    arrow(ax, (325, 58), (445, 58), ORANGE)
    note(ax, 0.45, 0.98, 'Sports day: D1 shifts right to D2.\nSales 200 to 350 shirts, still at N$80.\nPES is infinite')
    save(fig, '0455-T2.8-S37-perfectly-elastic-supply-tshirts', dict(
        topic='2.8', kind='card', shows='Horizontal supply S at N$80; demand shifts right from D1 to D2; E1 (200 shirts) to E2 (350 shirts) at the same price.',
        cards=['ITEM-0455-2.8-016-DIAGRAM'], blocks=['CU-0455-2.8.2 / 2.8.2-b6'],
        figures='S horizontal at N$80; E1 (200, N$80); E2 (350, N$80)'))


def _price_limit(title, slug, xlabel, ylabel, xlim, ylim, D, S, prange_d, prange_s, eq, limit, q_d, q_s,
                 line_label, gap_label, xticks, yticks, meta, gap_above=True, d_name='D', s_name='S'):
    fig, (ax,) = new_fig(title)
    frame(ax, xlabel, ylabel, xlim, ylim, xticks=xticks, yticks=yticks)
    draw_qp(ax, D, prange_d, BLUE, d_name, dx=0.01 * (xlim[1] - xlim[0]), label_at='start')
    draw_qp(ax, S, prange_s, ORANGE, s_name, dx=0.01 * (xlim[1] - xlim[0]))
    pt(ax, eq[0], eq[1], 'E', off=(10, -4) if gap_above else (10, 2))
    span = xlim[1] - xlim[0]
    ax.plot([xlim[0], xlim[0] + 0.86 * span], [limit, limit], color=INK, lw=1.6, ls='--')
    ax.text(xlim[0] + 0.865 * span, limit, line_label, fontsize=12, va='center')
    lo, hi = sorted((q_d, q_s))
    for q in (lo, hi):
        ax.plot([q, q], [ylim[0], limit], ls=(0, (2, 3)), color=INK2, lw=1.2)
        ax.plot(q, limit, 'o', color=INK, ms=7, mec='white', mew=1.5, zorder=5)
    ax.annotate('', (lo, limit), (hi, limit), arrowprops=dict(arrowstyle='<->', color=INK, lw=1.8))
    dy = 0.025 * (ylim[1] - ylim[0])
    ax.text((lo + hi) / 2, limit + dy if gap_above else limit - dy, gap_label, ha='center',
            va='bottom' if gap_above else 'top', fontsize=12.5, bbox=dict(fc='white', ec='none', pad=1.5))
    save(fig, slug, meta)


def s_2_11_011():
    _price_limit('A maximum price on bread in Ondangwa: a shortage', '0455-T2.11-S38-maximum-price-bread-ondangwa',
                 'Quantity (loaves per week)', 'Price (N$ per loaf)', (0, 10500), (0, 17),
                 lin((6000, 12), (7500, 9)), lin((6000, 12), (4000, 9)), (5, 15.5), (6, 15.5),
                 (6000, 12), 9, 7500, 4000, 'maximum\nprice N$9', 'shortage 3 500',
                 {4000: '4 000', 6000: '6 000', 7500: '7 500'}, {9: '9', 12: '12'},
                 dict(topic='2.11', kind='card', shows='Bread market clears at N$12 (6 000 loaves); a maximum price of N$9 gives 7 500 demanded and 4 000 supplied: a shortage of 3 500 a week.',
                      cards=['ITEM-0455-2.11-011-DIAGRAM'], blocks=['CU-0455-2.11.2 / 2.11.2-b8'],
                      figures='E (6 000, N$12); at N$9: D 7 500, S 4 000; shortage 3 500'), gap_above=False)


def s_2_11_013():
    _price_limit('A minimum price on milk: a surplus', '0455-T2.11-S39-minimum-price-milk',
                 'Quantity (litres per day)', 'Price (N$ per litre)', (14000, 46000), (8, 21),
                 lin((30000, 14), (26000, 17)), lin((30000, 14), (36000, 17)), (9.5, 20.5), (9.5, 19.5),
                 (30000, 14), 17, 26000, 36000, 'minimum\nprice N$17', 'surplus 10 000',
                 {26000: '26 000', 30000: '30 000', 36000: '36 000'}, {14: '14', 17: '17'},
                 dict(topic='2.11', kind='card', shows='Milk market clears at N$14 (30 000 litres a day); a minimum price of N$17 gives 26 000 demanded and 36 000 supplied: a surplus of 10 000 litres a day.',
                      cards=['ITEM-0455-2.11-013-DIAGRAM'], blocks=['CU-0455-2.11.2 / 2.11.2-b9'],
                      figures='E (30 000, N$14); at N$17: D 26 000, S 36 000; surplus 10 000'))


def s_2_11_014():
    _price_limit('A minimum wage for security guards: unemployment', '0455-T2.11-S40-minimum-wage-guards',
                 'Quantity of labour (guards)', 'Wage rate (N$ per hour)', (3000, 7200), (10, 32),
                 lin((5000, 20), (4200, 25)), lin((5000, 20), (5600, 25)), (12, 30.5), (12, 29.5),
                 (5000, 20), 25, 4200, 5600, 'minimum\nwage N$25', 'unemployment 1 400',
                 {4200: '4 200', 5000: '5 000', 5600: '5 600'}, {20: '20', 25: '25'},
                 dict(topic='2.11', kind='card', shows='Labour market for guards clears at N$20 an hour (5 000 guards); a minimum wage of N$25 gives 4 200 demanded and 5 600 supplied: 1 400 unemployed.',
                      cards=['ITEM-0455-2.11-014-DIAGRAM'], blocks=['CU-0455-2.11.2 / 2.11.2-b10'],
                      figures='E (5 000, N$20); at N$25: D 4 200, S 5 600; excess supply of labour 1 400'))


def s_2_11_017():
    _price_limit('A minimum exchange rate for the lune: excess supply', '0455-T2.11-S41-minimum-exchange-rate-lune',
                 'Quantity of lunes (millions a month)', 'Price of the lune (US$ per lune)', (550, 1100), (0.36, 0.72),
                 lin((800, 0.50), (700, 0.60)), lin((800, 0.50), (900, 0.60)), (0.385, 0.69), (0.385, 0.68),
                 (800, 0.50), 0.60, 700, 900, 'minimum\nexchange\nrate US$0.60', 'excess supply 200 million',
                 {700: '700', 800: 'Q*', 900: '900'}, {0.50: '0.50', 0.60: '0.60'},
                 dict(topic='2.11', kind='card', shows='Market for lunes clears at US$0.50 (quantity Q*); a minimum rate of US$0.60 gives 700 million demanded and 900 million supplied: 200 million excess supply, bought by the central bank.',
                      cards=['ITEM-0455-2.11-017-DIAGRAM'], blocks=['CU-0455-2.11.2 / 2.11.2-b11'],
                      figures='market rate US$0.50 at Q* (symbolic: the card gives no equilibrium quantity); at US$0.60: D 700 m, S 900 m; excess supply 200 m'))


def s_2_11_018():
    D = lambda p: 1000 - 0.3 * (p - 8000)
    S = lambda p: 1000 + 0.6 * (p - 8000)
    S1 = lambda p: 1000 + 0.6 * (p - 6500)
    fig, (ax,) = new_fig('A subsidy of N$1 500 on each solar water heater')
    frame(ax, 'Quantity (heaters per month)', 'Price (N$ per heater)', (0, 1750), (4500, 10500),
          xticks={1000: '1 000', 1300: '1 300'}, yticks={7000: '7 000', 8000: '8 000', 8500: '8 500'})
    ax.add_patch(Rectangle((0, 7000), 1300, 1500, fc=TINT_O, alpha=0.20, ec='none'))
    ax.text(650, 5000, 'shaded: cost of the subsidy\nN$1 500 × 1 300 = N$1 950 000', ha='left', va='center', fontsize=11.5,
            bbox=dict(fc='white', ec='none', alpha=0.85, pad=1.5), zorder=6)
    draw_qp(ax, D, (5000, 10200), INK2, 'D', dx=15, label_at='start')
    draw_qp(ax, S, (6400, 10200), BLUE, 'S', dx=15)
    draw_qp(ax, S1, (4800, 9900), ORANGE, 'S1', dx=15)
    pt(ax, 1000, 8000, 'E1', off=(-38, 6)); pt(ax, 1300, 7000, 'E2', off=(10, -22))
    pt(ax, 1300, 8500, None, guides=False)
    ax.annotate('', (1300, 8500), (1300, 7000), arrowprops=dict(arrowstyle='<->', color=ORANGE, lw=1.8))
    ax.text(1325, 7750, 'subsidy\nN$1 500', fontsize=12, va='center')
    save(fig, '0455-T2.11-S42-subsidy-solar-heaters', dict(
        topic='2.11', kind='card', shows='Supply shifts down by the N$1 500 subsidy from S to S1; D unchanged; E1 (N$8 000, 1 000 heaters) to E2 (N$7 000, 1 300); subsidy cost N$1 950 000 shaded.',
        cards=['ITEM-0455-2.11-018-DIAGRAM'], blocks=['CU-0455-2.11.2 / 2.11.2-b12'],
        figures='E1 (1 000, N$8 000); E2 (1 300, N$7 000); S at 1 300 = N$8 500 (S1 + N$1 500); cost N$1 950 000'))


def s_3_3_026():
    D = lin((20, 90), (90, 20)); S1 = lin((20, 20), (90, 90)); S2 = lin((45, 20), (115, 90))
    fig, (ax,) = new_fig('More trained welders: supply of labour shifts right')
    frame(ax, 'Number of welders', 'Wage (N$ per month)', (0, 125), (0, 135),
          xticks={55: 'Q1', 67.5: 'Q2'}, yticks={55: 'W1', 42.5: 'W2'})
    draw_qp(ax, D, (20, 92), BLUE, 'D', dx=2, label_at='start')
    draw_qp(ax, S1, (20, 92), INK2, 'S1', dx=2)
    draw_qp(ax, S2, (20, 88), ORANGE, 'S2', dx=2)
    pt(ax, 55, 55, 'E1', off=(-34, 4)); pt(ax, 67.5, 42.5, 'E2', off=(8, -22))
    ax.annotate('', (55, 55), (80, 55), arrowprops=dict(arrowstyle='<->', color=INK, lw=1.4))
    ax.text(82, 55, 'surplus of welders\nat W1: wage bid down', fontsize=11.5, va='center')
    arrow(ax, (52, 30), (72, 30), ORANGE)
    note(ax, 0.42, 0.98, '150 newly qualified welders a year:\nS1 to S2, demand unchanged.\nWage falls W1 to W2; employment\nrises Q1 to Q2')
    save(fig, '0455-T3.3-S43-labour-supply-welders', dict(
        topic='3.3', kind='card', shows='Supply of welders shifts right from S1 to S2 with demand unchanged; surplus at W1; wage falls to W2 and employment rises from Q1 to Q2.',
        cards=['ITEM-0455-3.3-026-SYNTH'], blocks=['CU-0455-3.3.3 / 3.3.3-b8'],
        figures='wages and employment symbolic (W1, W2, Q1, Q2): the card gives none'))


def s_3_7_018():
    q = np.linspace(0, 6000, 200)
    fig, (ax,) = new_fig('Fixed, variable and total cost: Otjiwa Dairy')
    frame(ax, 'Output (litres a month)', 'Costs (N$)', (0, 7200), (0, 42000),
          xticks={3000: '3 000', 6000: '6 000'}, yticks={6000: '6 000', 24000: '24 000', 30000: '30 000'})
    draw_xy(ax, q, 6000 + 0 * q, GREEN, 'FC', lx=6080, ly=6000)
    draw_xy(ax, q, 4 * q, ORANGE, 'VC', lx=6080, ly=24000)
    draw_xy(ax, q, 6000 + 4 * q, BLUE, 'TC', lx=6080, ly=30000)
    for y in (24000, 30000):
        ax.plot([0, 6000], [y, y], ls=(0, (2, 3)), color=INK2, lw=1.2)
    ax.plot([6000, 6000], [0, 30000], ls=(0, (2, 3)), color=INK2, lw=1.2)
    ax.annotate('', (3000, 12000), (3000, 18000), arrowprops=dict(arrowstyle='<->', color=INK, lw=1.6))
    ax.text(3080, 15000, 'gap = fixed cost\nN$6 000 at every output', fontsize=12, va='center')
    note(ax, 0.03, 0.98, 'FC: N$6 000 whatever the output\nVC: N$4 a litre, 0 to N$24 000\nTC = FC + VC: N$6 000 to N$30 000')
    save(fig, '0455-T3.7-S44-cost-lines-dairy', dict(
        topic='3.7', kind='card', shows='Fixed cost flat at N$6 000; variable cost rising from 0 to N$24 000 and total cost from N$6 000 to N$30 000 over 0 to 6 000 litres; the TC-VC gap is the fixed cost.',
        cards=['ITEM-0455-3.7-018-SYNTH'], blocks=['CU-0455-3.7.2 / 3.7.2-b6'],
        figures='FC N$6 000; VC N$4 a litre; at 6 000 litres VC N$24 000, TC N$30 000'))


def s_4_4_014():
    D = lambda p: 50 - 1000 * (p - 0.10)
    S1 = lambda p: 50 + 1000 * (p - 0.10)
    q2 = D(1 / 12)
    S2 = lambda p: q2 + 1000 * (p - 1 / 12)
    fig, (ax,) = new_fig('The central bank sells crowns: the crown depreciates')
    frame(ax, 'Quantity of crowns', 'Price of 1 crown (US$)', (0, 120), (0.05, 0.16),
          xticks={50: 'Q1', q2: 'Q2'}, yticks={0.10: '0.10', 1 / 12: '0.083'})
    draw_qp(ax, D, (0.06, 0.13), INK2, 'D', dx=1.5, label_at='start')
    draw_qp(ax, S1, (0.062, 0.128), BLUE, 'S1', dx=1.5)
    draw_qp(ax, S2, (0.052, 0.125), ORANGE, 'S2', dx=1.5)
    pt(ax, 50, 0.10, 'E1', off=(-34, 4)); pt(ax, q2, 1 / 12, 'E2', off=(10, -20))
    arrow(ax, (52, 0.066), (76, 0.066), ORANGE)
    note(ax, 0.02, 0.98, 'Central bank sells crowns for US dollars:\nsupply of crowns shifts right, S1 to S2.\n10 crowns per US$1 = US$0.10 a crown\n12 crowns per US$1 = about US$0.083 a crown')
    save(fig, '0455-T4.4-S45-crown-depreciation', dict(
        topic='4.4', kind='card', shows='Market for crowns: the central bank sells crowns, so supply shifts right from S1 to S2; the price of a crown falls from US$0.10 (10 per US$1) to about US$0.083 (12 per US$1).',
        cards=['ITEM-0455-4.4-014-APP'], blocks=['CU-0455-4.4.2 / 4.4.2-b7'],
        figures='rate 10 to 12 crowns per US$1 drawn as US$0.10 to US$0.083 per crown; quantities symbolic (Q1, Q2): the card gives none'))


AGE_BANDS_K = ['0-4', '5-9', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49',
               '50-54', '55-59', '60-64', '65-69', '70-74', '75+']
AGE_BANDS_M = AGE_BANDS_K[:-1] + ['75-79', '80+']


def _pyramid(title, slug, bands, male, female, groups, text, meta):
    fig, (ax,) = new_fig(title, size=(8, 7.5))
    y = np.arange(len(bands))
    ax.barh(y, [-m for m in male], color=BLUE, height=0.82, alpha=0.9)
    ax.barh(y, female, color=ORANGE, height=0.82, alpha=0.9)
    lim = max(max(male), max(female)) * 1.25
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-0.7, len(bands) + 0.6)
    ax.set_yticks(y)
    ax.set_yticklabels(bands)
    ticks = [t for t in range(-int(lim), int(lim) + 1) if t % 2 == 0]
    ax.set_xticks(ticks)
    ax.set_xticklabels([str(abs(t)) for t in ticks])
    ax.axvline(0, color=INK, lw=1.2)
    for s in ('top', 'right', 'left'):
        ax.spines[s].set_visible(False)
    ax.tick_params(length=0, pad=6, labelsize=12)
    ax.set_xlabel('Share of the whole population in each age group (%)', fontsize=13, labelpad=8)
    ax.set_ylabel('Age (years)', fontsize=13, labelpad=8)
    ax.text(-lim * 0.95, len(bands) + 0.05, 'Males', color=BLUE, fontsize=15, fontweight='bold', va='center')
    ax.text(lim * 0.95, len(bands) + 0.05, 'Females', color=ORANGE, fontsize=15, fontweight='bold', va='center', ha='right')
    for lo, hi, lab in groups:
        ax.annotate('', (lim * 1.02, lo - 0.4), (lim * 1.02, hi + 0.4), xycoords='data',
                    arrowprops=dict(arrowstyle='-', color=INK2, lw=1.4), annotation_clip=False)
        ax.text(lim * 1.05, (lo + hi) / 2, lab, fontsize=12.5, va='center', ha='left', color=INK, clip_on=False)
    ax.set_title(text, fontsize=13, color=INK2, loc='left', pad=12)
    fig.tight_layout(rect=(0, 0, 0.84, 0.95))
    png = os.path.join(OUT, slug + '.png'); svg = os.path.join(OUT, slug + '.svg')
    fig.savefig(png, facecolor='white'); fig.savefig(svg, facecolor='white')
    plt.close(fig)
    meta['file'] = slug
    REGISTRY.append(meta)


def s_5_3_017():
    shares = [15.5, 14, 12.5, 11, 9.5, 8, 6.5, 5.5, 4.5, 3.5, 2.8, 2.1, 1.6, 1.4, 0.9, 0.7]
    half = [v / 2 for v in shares]
    _pyramid('A young population: Country K', '0455-T5.3-S46-pyramid-young-country-k', AGE_BANDS_K, half, half,
             [(0, 2, '0-14\n42%'), (3, 12, '15-64\n55%'), (13, 15, '65+\n3%')],
             'Wide base, narrow top: each bar is narrower than the one below',
             dict(topic='5.3', kind='card', shows='Population pyramid for Country K: 42% aged 0-14, 55% aged 15-64, 3% aged 65 and over; each bar narrower than the one below (a young population).',
                  cards=['ITEM-0455-5.3-017-INTERP'], blocks=['CU-0455-5.3.3 / 5.3.3-b5'],
                  figures='0-14 = 42% (15.5, 14, 12.5); 15-64 = 55% (11, 9.5, 8, 6.5, 5.5, 4.5, 3.5, 2.8, 2.1, 1.6); 65+ = 3% (1.4, 0.9, 0.7); five-year bands invented to sum to the card\'s shares, split evenly by sex'))


def s_5_3_018():
    shares = [4.4, 4.7, 4.9, 5.2, 5.5, 5.8, 6.0, 6.3, 6.4, 6.5, 6.5, 6.3, 6.5, 7.0, 6.4, 6.2, 5.4]
    male = [v / 2 for v in shares[:-1]] + [1.8]
    female = [v / 2 for v in shares[:-1]] + [3.6]
    _pyramid('An ageing population: Country M', '0455-T5.3-S47-pyramid-ageing-country-m', AGE_BANDS_M, male, female,
             [(0, 2, '0-14\n14%'), (3, 12, '15-64\n61%'), (13, 16, '65+\n25%')],
             'Narrow base, broad top; at 80+ the female bar is twice the male bar',
             dict(topic='5.3', kind='card', shows='Population pyramid for Country M: 14% aged 0-14, 61% aged 15-64, 25% aged 65 and over; at 80+ the female bar is twice the male bar (an ageing population).',
                  cards=['ITEM-0455-5.3-018-INTERP'], blocks=['CU-0455-5.3.3 / 5.3.3-b5'],
                  figures='0-14 = 14% (4.4, 4.7, 4.9); 15-64 = 61%; 65+ = 25% (7.0, 6.4, 6.2, 5.4); 80+ male 1.8, female 3.6; five-year bands invented to sum to the card\'s shares'))


def s_6_3_018():
    S = lambda p: 20 + 400 * (p - 0.055)
    D = lambda p: 20 - 400 * (p - 0.055)
    D1 = lambda p: 22 - 400 * (p - 0.060)
    fig, (ax,) = new_fig('Foreign orders for wine: demand for the rand rises')
    frame(ax, 'Quantity of rand traded (R billion a week)', 'Exchange rate (US$ per rand)', (10, 34), (0.042, 0.078),
          xticks={20: '20', 22: '22'}, yticks={0.055: '0.055', 0.060: '0.060'})
    draw_qp(ax, D, (0.045, 0.068), BLUE, 'D', dx=0.3, label_at='start')
    draw_qp(ax, D1, (0.045, 0.069), ORANGE, 'D1', dx=0.3, label_at='start')
    draw_qp(ax, S, (0.045, 0.069), INK2, 'S', dx=0.3)
    pt(ax, 20, 0.055, 'E1', off=(-36, 4)); pt(ax, 22, 0.060, 'E2', off=(-14, 10))
    ax.annotate('', (20, 0.055), (24, 0.055), arrowprops=dict(arrowstyle='<->', color=INK, lw=1.4))
    ax.text(24.4, 0.055, 'excess demand\nat US$0.055', fontsize=11.5, va='center')
    arrow(ax, (22.6, 0.0495), (25.6, 0.0495), ORANGE)
    note(ax, 0.02, 0.98, 'Wine buyers abroad need rand: D shifts\nright to D1; S does not move.\nThe rand appreciates')
    save(fig, '0455-T6.3-S48-rand-demand-wine', dict(
        topic='6.3', kind='card', shows='Market for rand: demand shifts right from D to D1 as foreign wine orders rise; excess demand at US$0.055; E1 (US$0.055, R20 bn) to E2 (US$0.060, R22 bn): the rand appreciates.',
        cards=['ITEM-0455-6.3-018-DIAGRAM'], blocks=['CU-0455-6.3.2 / 6.3.2-b6'],
        figures='E1 (R20 bn, US$0.055); E2 (R22 bn, US$0.060) as the card\'s worked example; excess demand drawn without a figure'))


BUILD_ADDED = [s_2_6_010, g_unit_ped, s_2_7_022, s_2_7_023, g_unit_pes, s_2_8_015, s_2_8_016,
               s_2_11_011, s_2_11_013, s_2_11_014, s_2_11_017, s_2_11_018,
               s_3_3_026, s_3_7_018, s_4_4_014, s_5_3_017, s_5_3_018, s_6_3_018]


BUILD = [g_ppc_anatomy, g_ppc_opportunity_cost, g_ppc_move_vs_shift, g_ppc_inward,
         s_1_4_002, s_1_4_rising_cost, s_1_4_007, s_1_4_012, s_1_4_017,
         g_demand_move_shift, s_2_3_schedule, s_2_3_002, s_2_3_007, s_2_3_015,
         g_supply_move_shift, s_2_4_schedule, s_2_4_002, s_2_4_007, s_2_4_015,
         s_2_5_schedule, s_2_5_surplus_jam, s_2_5_002, s_2_5_007,
         g_four_shifts, s_2_6_005,
         g_ped, s_2_7_004, s_2_7_013,
         g_pes, s_2_8_004,
         s_2_10_007, s_2_11_004, g_subsidy, s_2_11_max_bread, s_2_11_min_beef,
         g_labour, s_3_3_labour, s_3_7_004, s_3_8_002, s_3_8_007,
         s_4_6_008, s_4_6_013, g_two_routes,
         s_6_3_005, lambda: g_fx('app'), lambda: g_fx('dep')] + BUILD_ADDED


def write_index():
    def tkey(m):
        return [int(x) for x in m['topic'].split('.')] + [m['file']]
    rows = sorted(REGISTRY, key=tkey)
    with open(os.path.join(OUT, 'index.csv'), 'w', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['file_png', 'file_svg', 'topic', 'kind', 'shows', 'add_to_cards', 'add_to_notes_blocks', 'figures'])
        for m in rows:
            w.writerow([m['file'] + '.png', m['file'] + '.svg', m['topic'], m['kind'], m['shows'],
                        '; '.join(m['cards']), '; '.join(m['blocks']), m['figures']])
    titles = {'1.3': 'Opportunity cost', '1.4': 'Production possibility curve (PPC) diagrams', '2.3': 'Demand',
              '2.4': 'Supply', '2.5': 'Price determination', '2.6': 'Price changes',
              '2.7': 'Price elasticity of demand (PED)', '2.8': 'Price elasticity of supply (PES)',
              '2.10': 'Market failure', '2.11': 'Mixed economic system', '3.3': 'Workers',
              '3.7': 'Firms’ costs, revenue and objectives', '3.8': 'Market structure',
              '4.4': 'Monetary policy', '4.6': 'Economic growth', '5.3': 'Population',
              '6.3': 'Foreign exchange rates'}
    L = ['# Diagrams — 0455 Cambridge IGCSE Economics', '',
         f'{len(rows)} diagrams, each as a PNG (1600 × 1200 or wider, white background) and an SVG. '
         'Add them to the cards and note sections listed against each one.', '',
         '- **card**: drawn from the figures one card states; the card and the picture agree.',
         '- **notes**: drawn from figures stated in a notes section.',
         '- **generic**: no figures; a teaching picture for the idea, usable on any card listed.', '',
         'Card IDs are the `item_id` in `work/cie-0455-igcse-2026/topics/<topic>/learning-items/`. '
         'Note sections are `content unit / block id`.', '']
    cur = None
    for m in rows:
        if m['topic'] != cur:
            cur = m['topic']
            L += ['', f'## {cur} {titles.get(cur, "")}', '']
        L += [f'### `{m["file"]}.png`  ·  {m["kind"]}', '', m['shows'], '',
              f'- **Add to cards:** {", ".join("`" + c + "`" for c in m["cards"]) or "none"}',
              f'- **Add to notes:** {", ".join(m["blocks"]) or "none"}',
              f'- **Figures:** {m["figures"]}', '']
    open(os.path.join(OUT, 'INDEX.md'), 'w').write('\n'.join(L) + '\n')


if __name__ == '__main__':
    for f in BUILD:
        f()
    write_index()
    print(len(REGISTRY), 'diagrams ->', OUT)
