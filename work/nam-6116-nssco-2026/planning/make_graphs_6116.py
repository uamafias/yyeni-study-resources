#!/usr/bin/env python3
"""Generate the 6116 Biology graphs: question and answer variants, each from declared data.

Reuses the plotting approach of publish/cie-0455-igcse-2026/diagrams/make_diagrams_0455.py: matplotlib,
one house style, PNG (for display) and SVG (for editing) per figure, and a registry that ties each file
to its data, its objectives and its intended use. That script is not imported (it draws its own figures
when loaded); the style constants and frame helper are copied from it.

Every graph is drawn from data declared here, and says what kind of data it is:
  learner readings  invented but realistic results, presented to learners as a learner's results
  model curve       the standard shape of a relationship, with illustrative values; never presented as measured
  real data         published figures, approximate, with their source; to be checked before release

Variants. -Q: what a learner reads or completes (no answer marked; neutral letters where phases are asked).
          -A: the answer (readings, regions or labels marked). The A variant also serves the notes.

    python3 work/nam-6116-nssco-2026/planning/make_graphs_6116.py
Output: work/nam-6116-nssco-2026/visuals/generated/ and visuals/generated/graphs.json
"""
import json, os, hashlib, textwrap
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

WS = 'work/nam-6116-nssco-2026'
OUT = os.path.join(WS, 'visuals', 'generated')
os.makedirs(OUT, exist_ok=True)

# ---- house style, from make_diagrams_0455.py
INK, INK2, MUTED = '#0b0b0b', '#52514e', '#9a9893'
BLUE, ORANGE, GREEN = '#2a78d6', '#eb6834', '#1baf7a'
plt.rcParams.update({
    'font.family': 'DejaVu Sans', 'font.size': 15, 'axes.linewidth': 1.6,
    'svg.fonttype': 'none', 'axes.edgecolor': INK, 'text.color': INK,
    'xtick.color': INK2, 'ytick.color': INK2, 'text.parse_math': False,
    'svg.hashsalt': 'yyeni-6116',
})
REGISTRY = []


def new_fig(title, size=(8, 6)):
    fig, ax = plt.subplots(figsize=size, dpi=200)
    fig.patch.set_facecolor('white')
    fig.suptitle(textwrap.fill(title, 60), fontsize=16, fontweight='bold', x=0.02, ha='left', y=0.985)
    return fig, ax


def frame(ax, xlabel, ylabel, xlim, ylim, grid=True):
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    for s in ('top', 'right'):
        ax.spines[s].set_visible(False)
    ax.tick_params(length=4, pad=5, labelsize=12)
    ax.set_xlabel(xlabel, fontsize=13, color=INK, labelpad=8)
    ax.set_ylabel(ylabel, fontsize=13, color=INK, labelpad=8)
    if grid:
        ax.grid(True, color='#e3e2de', lw=0.8)
        ax.set_axisbelow(True)


def crosses(ax, xs, ys, color=INK):
    """Points as crosses, Annexe B convention (1.2.3: crosses or encircled dots)."""
    ax.plot(xs, ys, 'x', color=color, ms=10, mew=2.2, zorder=5)


def note(ax, text):
    ax.text(0.0, -0.2, textwrap.fill(text, 95), transform=ax.transAxes, fontsize=10.5, color=INK2, va='top')


def save(fig, slug, variant, meta):
    fig.tight_layout(rect=(0, 0.02, 1, 0.94))
    files = []
    for ext in ('png', 'svg'):
        p = os.path.join(OUT, '%s-%s.%s' % (slug, variant, ext))
        if meta.get('preserve_approved_files') and os.path.exists(p):
            approvals = json.load(open(os.path.join(WS, 'planning', 'operator_approvals.json')))['images']['assets']
            relative = os.path.relpath(p, WS)
            expected = approvals.get(slug, {}).get('files', {}).get(relative)
            if not expected or hashlib.sha256(open(p, 'rb').read()).hexdigest() != expected:
                raise RuntimeError('Cannot preserve a changed or unapproved generated file: ' + p)
        else:
            fig.savefig(p, facecolor='white', metadata={'Date': None} if ext == 'svg' else None)
        files.append(p)
    plt.close(fig)
    meta.setdefault('variants', {})[variant] = [
        {'path': os.path.relpath(p, WS), 'sha256': hashlib.sha256(open(p, 'rb').read()).hexdigest()} for p in files]


def register(meta):
    REGISTRY.append(meta)


# =========================================================================== osmosis (exemplar data)
def osmosis():
    conc = [0.0, 0.2, 0.4, 0.6, 0.8]
    start = [2.50, 2.40, 2.50, 2.60, 2.50]
    end = [2.80, 2.52, 2.45, 2.34, 2.15]
    pct = [round(100 * (e - s) / s, 2) for s, e in zip(start, end)]
    meta = {'asset_id': 'BIO-6116-GRAPH-OSMOSIS-001', 'title': 'Potato tissue: change in mass against sucrose concentration',
            'data_kind': 'learner readings', 'data_source': 'exemplar ITEM-6116-3-P03 table (invented, realistic)',
            'data': {'concentration_mol_dm3': conc, 'change_in_mass_percent': pct},
            'objective_ids': ['OBJ-6116-3.3.2-04', 'OBJ-6116-1.2.2-02', 'OBJ-6116-1.2.3-02', 'OBJ-6116-1.2.3-03',
                              'OBJ-6116-1.2.3-06', 'OBJ-6116-1.2.3-07', 'OBJ-6116-1.2.3-08'],
            'uses': {'Q': 'question side: blank labelled grid to plot the table on', 'A': 'answer side and notes: model completed graph'}}
    fig, ax = new_fig('Plot the results: percentage change in mass against sucrose concentration')
    frame(ax, 'Sucrose concentration / mol dm⁻³', 'Change in mass / %', (-0.02, 0.9), (-16, 14))
    ax.axhline(0, color=INK2, lw=1)
    note(ax, 'Plot the five results from the table as crosses and draw a line of best fit.')
    save(fig, meta['asset_id'], 'Q', meta)
    fig, ax = new_fig('Percentage change in mass of potato tissue against sucrose concentration')
    frame(ax, 'Sucrose concentration / mol dm⁻³', 'Change in mass / %', (-0.02, 0.9), (-16, 14))
    ax.axhline(0, color=INK2, lw=1)
    crosses(ax, conc, pct)
    fit = np.polyfit(conc, pct, 2)
    xs = np.linspace(0, 0.8, 200); ax.plot(xs, np.polyval(fit, xs), color=BLUE, lw=2.4)
    x0 = min(r.real for r in np.roots(fit) if abs(r.imag) < 1e-9 and 0 <= r.real <= 0.8)
    ax.plot([x0, x0], [-16, 0], ls=(0, (2, 3)), color=INK2, lw=1.2)
    ax.annotate('no change in mass at about %.2f mol dm⁻³' % x0, (x0, 0), xytext=(14, 30), textcoords='offset points',
                fontsize=12, arrowprops=dict(arrowstyle='->', color=INK2))
    note(ax, 'Learner readings (invented). Crosses for points; axes labelled quantity / unit; heading names y against x.')
    meta['answer_reading'] = {'zero_crossing_mol_dm3': round(float(x0), 2)}
    save(fig, meta['asset_id'], 'A', meta)
    register(meta)


# =========================================================================== enzymes (model curves)
def enzyme_temperature():
    t = np.linspace(0, 70, 300)
    # rising collision term times a smooth denaturation fall-off, so the peak is rounded, not a cusp
    rate = np.exp((t - 40) / 14) / (1 + np.exp((t - 44) / 2.6))
    rate = rate / rate.max()
    t_opt = float(t[rate.argmax()])
    meta = {'asset_id': 'BIO-6116-GRAPH-ENZYME-TEMP-001', 'title': 'Rate of an enzyme-controlled reaction against temperature',
            'data_kind': 'model curve', 'data_source': 'standard shape with an optimum near 40 °C, illustrative values',
            'data': {'optimum_C': round(t_opt)}, 'objective_ids': ['OBJ-6116-3.5-04'],
            'uses': {'Q': 'question side: describe and explain the shape', 'A': 'answer side and notes: optimum and denaturation marked'}}
    for v in ('Q', 'A'):
        fig, ax = new_fig('Rate of reaction against temperature for an enzyme')
        frame(ax, 'Temperature / °C', 'Rate of reaction / arbitrary units', (0, 70), (0, 1.15))
        ax.plot(t, rate, color=BLUE, lw=2.6)
        if v == 'A':
            ax.axvline(t_opt, ls=(0, (2, 3)), color=INK2, lw=1.2)
            ax.text(t_opt + 0.8, 1.07, 'optimum', fontsize=12)
            ax.text(5, 0.62, 'more kinetic energy:\nmore collisions,\nfaster rate', fontsize=11, color=INK2)
            ax.text(50, 0.62, 'active site changes\nshape: enzyme\ndenatured', fontsize=11, color=INK2)
        note(ax, 'Model curve: the shape of the relationship, with illustrative values; not a measured result.')
        save(fig, meta['asset_id'], v, meta)
    register(meta)


def enzyme_ph():
    ph = np.linspace(1, 13, 300)
    rate = np.exp(-((ph - 7) / 1.7) ** 2)
    meta = {'asset_id': 'BIO-6116-GRAPH-ENZYME-PH-001', 'title': 'Rate of an enzyme-controlled reaction against pH',
            'data_kind': 'model curve', 'data_source': 'standard shape for an enzyme with an optimum near pH 7 (e.g. salivary amylase), illustrative values',
            'data': {'optimum_pH': 7}, 'objective_ids': ['OBJ-6116-3.5-05'],
            'uses': {'Q': 'question side', 'A': 'answer side and notes: optimum and denaturation either side marked'}}
    for v in ('Q', 'A'):
        fig, ax = new_fig('Rate of reaction against pH for an enzyme')
        frame(ax, 'pH', 'Rate of reaction / arbitrary units', (1, 13), (0, 1.15))
        ax.plot(ph, rate, color=BLUE, lw=2.6)
        if v == 'A':
            ax.axvline(7, ls=(0, (2, 3)), color=INK2, lw=1.2); ax.text(7.2, 1.07, 'optimum pH', fontsize=12)
            ax.text(1.4, 0.55, 'too acidic:\nactive site\nchanges shape', fontsize=11, color=INK2)
            ax.text(9.6, 0.55, 'too alkaline:\nactive site\nchanges shape', fontsize=11, color=INK2)
        note(ax, 'Model curve with illustrative values. Enzymes differ in their optimum pH.')
        save(fig, meta['asset_id'], v, meta)
    register(meta)


# =========================================================================== photosynthesis (model curves)
def photosynthesis_light():
    li = np.linspace(0, 100, 300)
    hi = 1.0 * (1 - np.exp(-li / 22)); lo = 0.55 * (1 - np.exp(-li / 14))
    meta = {'asset_id': 'BIO-6116-GRAPH-PHOTO-LIGHT-001', 'title': 'Rate of photosynthesis against light intensity at two carbon dioxide concentrations',
            'data_kind': 'model curve', 'data_source': 'standard limiting-factor shape, illustrative values',
            'data': {'curves': ['higher CO2', 'lower CO2']},
            'objective_ids': ['OBJ-6116-3.6.1.3-04', 'OBJ-6116-3.6.1.3-05', 'OBJ-6116-3.6.1.3-10'],
            'uses': {'Q': 'question side: letters P, Q and R on regions to identify the limiting factor',
                     'A': 'answer side and notes: limiting factor named for each region'}}
    for v in ('Q', 'A'):
        fig, ax = new_fig('Rate of photosynthesis against light intensity')
        frame(ax, 'Light intensity / arbitrary units', 'Rate of photosynthesis / arbitrary units', (0, 100), (0, 1.15))
        ax.plot(li, hi, color=BLUE, lw=2.6); ax.plot(li, lo, color=ORANGE, lw=2.6)
        ax.text(101, hi[-1], 'higher CO₂', color=BLUE, fontsize=12, va='center')
        ax.text(101, lo[-1], 'lower CO₂', color=ORANGE, fontsize=12, va='center')
        marks = [(12, 0.42, 'P'), (80, 0.99, 'Q'), (80, 0.58, 'R')]
        for x, y, letter in marks:
            ax.text(x, y + 0.04, letter, fontsize=14, fontweight='bold')
        if v == 'A':
            ax.text(14, 0.18, 'P: light intensity limits\n(rate rises as light increases)', fontsize=10.5, color=INK2)
            ax.text(45, 1.08, 'Q, R: light no longer limits;\nCO₂ concentration (or temperature) limits', fontsize=10.5, color=INK2)
        note(ax, 'Model curves with illustrative values; the plateau height depends on the factor that limits.')
        save(fig, meta['asset_id'], v, meta)
    register(meta)


def photosynthesis_co2():
    c = np.linspace(0, 0.5, 300)
    r = 1 - np.exp(-c / 0.09)
    meta = {'asset_id': 'BIO-6116-GRAPH-PHOTO-CO2-001', 'title': 'Rate of photosynthesis against carbon dioxide concentration',
            'data_kind': 'model curve', 'data_source': 'standard shape, illustrative values',
            'data': {}, 'objective_ids': ['OBJ-6116-3.6.1.3-05', 'OBJ-6116-3.6.1.3-10'],
            'uses': {'Q': 'question side', 'A': 'answer side and notes: limiting regions marked'}}
    for v in ('Q', 'A'):
        fig, ax = new_fig('Rate of photosynthesis against carbon dioxide concentration')
        frame(ax, 'Carbon dioxide concentration / %', 'Rate of photosynthesis / arbitrary units', (0, 0.5), (0, 1.15))
        ax.plot(c, r, color=BLUE, lw=2.6)
        if v == 'A':
            ax.text(0.02, 0.85, 'CO₂ limits here', fontsize=11, color=INK2)
            ax.text(0.28, 1.05, 'another factor (light or\ntemperature) limits here', fontsize=11, color=INK2)
        note(ax, 'Model curve with illustrative values.')
        save(fig, meta['asset_id'], v, meta)
    register(meta)


# =========================================================================== breathing (learner readings)
def breathing():
    minutes = list(range(0, 21))
    rate = [14, 14, 14, 14, 14, 22, 28, 31, 33, 34, 34, 30, 25, 21, 18, 16, 15, 14, 14, 14, 14]
    meta = {'asset_id': 'BIO-6116-GRAPH-BREATHING-001', 'title': 'Breathing rate before, during and after exercise',
            'data_kind': 'learner readings', 'data_source': 'invented, realistic (rest 0-4 min, exercise 5-10 min, recovery after)',
            'data': {'minute': minutes, 'breaths_per_minute': rate}, 'objective_ids': ['OBJ-6116-3.9-07', 'OBJ-6116-1.2.3-08'],
            'uses': {'Q': 'question side: describe and explain the changes', 'A': 'answer side and notes: phases marked'}}
    for v in ('Q', 'A'):
        fig, ax = new_fig('Breathing rate of a learner before, during and after exercise')
        frame(ax, 'Time / min', 'Breathing rate / breaths per minute', (0, 20), (0, 40))
        ax.plot(minutes, rate, color=BLUE, lw=2.2); crosses(ax, minutes, rate)
        if v == 'A':
            ax.axvspan(5, 10, color='#fde9df', zorder=0)
            ax.text(5.2, 37, 'exercise', fontsize=12); ax.text(11.2, 37, 'recovery', fontsize=12)
        else:
            ax.axvline(5, ls=(0, (2, 3)), color=INK2); ax.axvline(10, ls=(0, (2, 3)), color=INK2)
            ax.text(5.2, 37, 'starts', fontsize=11); ax.text(10.2, 37, 'stops', fontsize=11)
        note(ax, 'Learner readings (invented).')
        save(fig, meta['asset_id'], v, meta)
    register(meta)


def breathing_volume_trace():
    """An item-specific trace: peak spacing and height both change at exercise."""
    seconds = np.linspace(0, 120, 2401)
    # Illustrative breaths: 12/min at rest, 24/min during exercise.
    phase = np.where(seconds < 60, seconds / 5, (seconds - 60) / 2.5)
    depth = np.where(seconds < 60, 0.35, 0.85)
    volume = depth * (1 - np.cos(2 * np.pi * phase)) / 2
    meta = {'asset_id': 'BIO-6116-GRAPH-BREATH-VOLUME-001',
            'title': 'Breath volume trace at rest and during exercise',
            'data_kind': 'model trace',
            'data_source': 'illustrative model: 12 breaths/min and 0.35 L per breath at rest; 24 breaths/min and 0.85 L per breath during exercise; not measured',
            'data': {'rest': {'breaths_per_minute': 12, 'volume_per_breath_L': 0.35},
                     'exercise': {'breaths_per_minute': 24, 'volume_per_breath_L': 0.85}},
            'objective_ids': ['OBJ-6116-3.9-07'],
            'uses': {'Q': 'exact stimulus for ITEM-6116-3-451-APP: compare peak frequency and height',
                     'A': 'answer-side trace with the two changes named'}}
    for v in ('Q', 'A'):
        fig, ax = new_fig('Breath volume at rest and during exercise', (10, 5.5))
        frame(ax, 'Time / s', 'Volume of each breath / L', (0, 120), (0, 1.0))
        ax.plot(seconds, volume, color=BLUE, lw=1.8)
        ax.axvline(60, color=INK2, ls=(0, (3, 3)), lw=1.2)
        ax.text(30, 0.93, 'rest', ha='center', fontsize=13)
        ax.text(90, 0.93, 'exercise', ha='center', fontsize=13)
        if v == 'A':
            ax.text(65, 0.70, 'more peaks per minute', fontsize=11, color=INK2)
            ax.text(65, 0.58, 'higher peaks', fontsize=11, color=INK2)
        note(ax, 'Illustrative trace, not a volunteer measurement. The vertical axis shows breath volume above the baseline.')
        save(fig, meta['asset_id'], v, meta)
    register(meta)


# =========================================================================== growth curve (learner readings)
def growth():
    day = list(range(0, 92, 7))
    height = [0, 1, 3, 7, 14, 24, 36, 47, 55, 60, 63, 64, 65, 65]
    meta = {'asset_id': 'BIO-6116-GRAPH-GROWTH-001', 'title': 'Height of an annual plant from sowing to maturity',
            'data_kind': 'learner readings', 'data_source': 'invented, realistic (a bean plant measured weekly)',
            'data': {'day': day, 'height_cm': height}, 'objective_ids': ['OBJ-6116-4.3.5-08', 'OBJ-6116-1.2.3-03'],
            'uses': {'Q': 'question side: plot or describe the curve', 'A': 'answer side and notes: phases of growth marked'}}
    for v in ('Q', 'A'):
        fig, ax = new_fig('Height of a bean plant from sowing')
        frame(ax, 'Time after sowing / days', 'Height / cm', (0, 95), (0, 72))
        if v == 'A':
            ax.plot(day, height, color=BLUE, lw=2.2); crosses(ax, day, height)
            ax.text(3, 8, 'slow start', fontsize=11, color=INK2); ax.text(30, 40, 'rapid growth', fontsize=11, color=INK2)
            ax.text(62, 67.5, 'growth stops at maturity', fontsize=11, color=INK2)
        note(ax, 'Plot the weekly heights from the table as crosses and join them.' if v == 'Q'
             else 'Learner readings (invented).')
        save(fig, meta['asset_id'], v, meta)
    register(meta)


def annual_plant_dry_mass():
    day = [0, 2, 4, 6, 8, 10, 12, 14]
    dry_mass = [1.20, 1.02, 0.86, 0.78, 0.88, 1.18, 1.65, 2.25]
    meta = {'asset_id': 'BIO-6116-GRAPH-DRY-MASS-001',
            'title': 'Mean dry mass of an annual plant after sowing',
            'data_kind': 'model data',
            'data_source': 'illustrative values showing initial loss of seed reserves followed by photosynthetic gain; not measured',
            'data': {'day_after_sowing': day, 'mean_dry_mass_g': dry_mass},
            'objective_ids': ['OBJ-6116-4.3.5-08'],
            'uses': {'Q': 'exact stimulus for ITEM-6116-4-089-PROC: dry mass first falls, then rises',
                     'A': 'answer-side graph with the two phases named'}}
    for v in ('Q', 'A'):
        fig, ax = new_fig('Mean dry mass of an annual plant after sowing')
        frame(ax, 'Time after sowing / days', 'Mean dry mass / g', (0, 14), (0, 2.5))
        ax.plot(day, dry_mass, color=GREEN, lw=2.2)
        crosses(ax, day, dry_mass)
        if v == 'A':
            ax.annotate('reserves used in respiration', (4, 0.86), (0.2, 1.65), fontsize=10.5,
                        arrowprops=dict(arrowstyle='->', color=INK2))
            ax.annotate('photosynthetic gain exceeds loss', (11, 1.4), (5.5, 2.2), fontsize=10.5,
                        arrowprops=dict(arrowstyle='->', color=INK2))
        note(ax, 'Illustrative model values, not results from a measured plant.')
        save(fig, meta['asset_id'], v, meta)
    register(meta)


# =========================================================================== variation (learner readings)
def variation():
    rng = np.random.default_rng(6116)
    lengths = np.clip(rng.normal(8.0, 1.3, 120), 4.0, 12.0).round(1)
    bins = np.arange(4, 12.5, 1.0)
    counts, _ = np.histogram(lengths, bins)
    groups = {'A': 31, 'B': 9, 'AB': 3, 'O': 57}
    meta = {'asset_id': 'BIO-6116-GRAPH-VARIATION-001', 'title': 'Continuous and discontinuous variation',
            'data_kind': 'learner readings', 'data_source': 'invented: 120 leaf lengths (seeded, normal about 8 cm); blood groups of 100 learners',
            'data': {'leaf_length_bins_cm': bins.tolist(), 'counts': counts.tolist(), 'blood_groups': groups},
            'objective_ids': ['OBJ-6116-4.4.3-04', 'OBJ-6116-1.2.3-03'],
            'uses': {'A': 'notes and answer side: histogram for continuous variation, bar chart with gaps for discontinuous'}}
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(12, 6), dpi=200)
    fig.patch.set_facecolor('white')
    fig.suptitle('Continuous variation (histogram) and discontinuous variation (bar chart)', fontsize=16, fontweight='bold', x=0.02, ha='left')
    a1.bar(bins[:-1], counts, width=1.0, align='edge', color=BLUE, edgecolor='white')
    frame(a1, 'Leaf length / cm', 'Number of leaves', (4, 12), (0, max(counts) + 6), grid=False)
    a2.bar(list(groups), list(groups.values()), width=0.6, color=ORANGE)
    frame(a2, 'Blood group', 'Number of learners', (-0.6, 3.6), (0, 65), grid=False)
    a1.text(4, -9, 'bars touch: length varies continuously', fontsize=10.5, color=INK2)
    a2.text(-0.6, -11, 'bars separate: distinct categories', fontsize=10.5, color=INK2)
    save(fig, meta['asset_id'], 'A', meta)
    register(meta)


# =========================================================================== populations
def sigmoid():
    t = np.linspace(0, 30, 300)
    n = 1000 / (1 + np.exp(-(t - 13) / 2.2))
    meta = {'asset_id': 'BIO-6116-GRAPH-SIGMOID-001', 'title': 'Sigmoid population growth curve',
            'data_kind': 'model curve', 'data_source': 'logistic curve, carrying capacity 1000, illustrative',
            'data': {}, 'objective_ids': ['OBJ-6116-5.3-05'],
            'uses': {'Q': 'question side: phases lettered A, B, C to name and explain',
                     'A': 'answer side and notes: lag, exponential (log) and stationary phases named'}}
    marks = [(3.5, 'A', 'lag'), (13, 'B', 'exponential (log)'), (25, 'C', 'stationary')]
    for v in ('Q', 'A'):
        fig, ax = new_fig('Growth of a population with limited resources')
        frame(ax, 'Time / days', 'Number of organisms', (0, 30), (0, 1150))
        ax.plot(t, n, color=BLUE, lw=2.6)
        for x, letter, name in marks:
            y = 1000 / (1 + np.exp(-(x - 13) / 2.2))
            ax.text(x, y + 60, name if v == 'A' else letter, fontsize=13, fontweight='bold', ha='center')
        note(ax, 'Model curve with illustrative values.')
        save(fig, meta['asset_id'], v, meta)
    register(meta)


def human_population():
    years = [1800, 1900, 1950, 1975, 2000, 2010, 2022]
    billions = [1.0, 1.6, 2.5, 4.1, 6.1, 6.9, 8.0]
    meta = {'asset_id': 'BIO-6116-GRAPH-HUMANPOP-001', 'title': 'World human population, 1800-2022',
            'preserve_approved_files': True,
            'data_kind': 'real data', 'data_source': 'approximate published estimates (UN World Population Prospects; Our World in Data). VERIFY each value against the source before release.',
            'data': {'year': years, 'population_billions': billions}, 'objective_ids': ['OBJ-6116-5.3-08', 'OBJ-6116-5.3-06'],
            'uses': {'Q': 'question side: describe and interpret the trend', 'A': 'answer side and notes: trend marked'}}
    for v in ('Q', 'A'):
        fig, ax = new_fig('World human population, 1800 to 2022')
        frame(ax, 'Year', 'Population / billions', (1795, 2030), (0, 9))
        ax.plot(years, billions, color=BLUE, lw=2.4); crosses(ax, years, billions)
        if v == 'A':
            ax.text(1830, 3.0, 'slow growth', fontsize=11, color=INK2)
            ax.text(1955, 7.3, 'very rapid growth\nafter 1950', fontsize=11, color=INK2)
        note(ax, 'Approximate published estimates; values to be verified before release.')
        save(fig, meta['asset_id'], v, meta)
    register(meta)


def model_town_population():
    year = [0, 1, 2, 3]
    population = [20000, 21000, 21840, 22386]
    meta = {'asset_id': 'BIO-6116-GRAPH-MODEL-TOWN-001',
            'title': 'Model-town population from the table in item 5-045',
            'data_kind': 'model data',
            'data_source': 'illustrative values stated in ITEM-6116-5-045-APP; not a real population',
            'data': {'year': year, 'population': population, 'annual_growth_percent': [None, 5.0, 4.0, 2.5]},
            'objective_ids': ['OBJ-6116-5.3-08'],
            'uses': {'Q': 'exact stimulus for ITEM-6116-5-045-APP: population rises as annual percentage growth falls',
                     'A': 'answer-side graph with both trends named'}}
    for v in ('Q', 'A'):
        fig, ax = new_fig('Population of a model town', (8.5, 5.5))
        frame(ax, 'Year', 'Population / people', (0, 3), (19000, 23000))
        ax.set_xticks(year)
        ax.plot(year, population, color=BLUE, lw=2.2)
        crosses(ax, year, population)
        if v == 'A':
            ax.text(0.25, 22550, 'Population rises each year,\nbut additions become smaller.', fontsize=11, color=INK2)
        note(ax, 'Model-town values from the question table; the annual percentage growth rates are in that table.')
        save(fig, meta['asset_id'], v, meta)
    register(meta)


def pyramids():
    chain = ['grass', 'grasshoppers', 'birds', 'eagle']
    numbers = [5000, 800, 20, 1]
    biomass = [2000, 300, 12, 3]
    meta = {'asset_id': 'BIO-6116-GRAPH-PYRAMID-001', 'title': 'Pyramids of numbers and biomass for one food chain',
            'data_kind': 'model data', 'data_source': 'illustrative values for a grassland food chain',
            'data': {'chain': chain, 'numbers': numbers, 'biomass_g_per_m2': biomass},
            'objective_ids': ['OBJ-6116-5.1-10', 'OBJ-6116-5.1-11', 'OBJ-6116-5.1-14'],
            'uses': {'Q': 'question side: bars only, trophic levels to name', 'A': 'answer side and notes: organisms and trophic levels named'}}
    levels = ['producer', 'primary consumer', 'secondary consumer', 'tertiary consumer']
    for v in ('Q', 'A'):
        fig, axes = plt.subplots(1, 2, figsize=(12, 6), dpi=200)
        fig.patch.set_facecolor('white')
        fig.suptitle('Pyramid of numbers and pyramid of biomass', fontsize=16, fontweight='bold', x=0.02, ha='left')
        for ax, vals, label in ((axes[0], numbers, 'numbers'), (axes[1], biomass, 'biomass / g per m²')):
            w = np.sqrt(np.array(vals) / max(vals)) * 10
            for i, (wi, val) in enumerate(zip(w, vals)):
                ax.barh(i, wi, left=-wi / 2, height=0.8, color=GREEN if i == 0 else BLUE, edgecolor='white')
                txt = '%s: %s (%s)' % (levels[i], chain[i], val) if v == 'A' else '?'
                ax.text(5.6, i, txt, va='center', fontsize=10.5)
            ax.set_xlim(-5.5, 14); ax.set_ylim(-0.6, 3.6); ax.axis('off'); ax.set_title(label, fontsize=13, loc='left')
        fig.text(0.02, 0.03, 'Schematic: bar widths shrink with the value at each level but are not to scale '
                 '(5000 against 1 cannot be drawn to scale). Illustrative values.', fontsize=10.5, color=INK2)
        save(fig, meta['asset_id'], v, meta)
    register(meta)


def grassland_biomass_item():
    levels = ['producers', 'primary consumers', 'secondary consumers', 'tertiary consumers']
    values = [800, 80, 12, 2]
    meta = {'asset_id': 'BIO-6116-GRAPH-GRASSLAND-BIOMASS-001',
            'title': 'Grassland biomass pyramid for item 5-016',
            'data_kind': 'model data',
            'data_source': 'illustrative dry-mass values stated in ITEM-6116-5-016-APP; not a field measurement',
            'data': {'level': levels, 'dry_mass_g_per_m2': values},
            'objective_ids': ['OBJ-6116-5.1-14'],
            'uses': {'Q': 'exact stimulus for ITEM-6116-5-016-APP: four stated biomass values',
                     'A': 'answer-side pyramid with decreasing biomass annotated'}}
    for v in ('Q', 'A'):
        fig, ax = new_fig('Biomass pyramid for a grassland', (10, 5.5))
        ax.set_xlim(-4.5, 8.5); ax.set_ylim(-0.7, 3.9); ax.axis('off')
        for i, (level, val) in enumerate(zip(levels, values)):
            width = 7.0 * np.sqrt(val / 800)
            ax.barh(i, width, left=-width / 2, height=0.75, color=GREEN if i == 0 else BLUE)
            ax.text(4.1, i, f'{level}: {val} g/m²', va='center', fontsize=11)
        if v == 'A':
            ax.text(-4.2, 3.6, 'Standing biomass decreases at each higher level.', fontsize=11, color=INK2)
        fig.text(0.02, 0.035, 'Illustrative standing dry mass at one site and time; bar widths are schematic, not to scale.',
                 fontsize=10.5, color=INK2)
        save(fig, meta['asset_id'], v, meta)
    register(meta)


if __name__ == '__main__':
    for f in (osmosis, enzyme_temperature, enzyme_ph, photosynthesis_light, photosynthesis_co2, breathing, growth,
              variation, sigmoid, human_population, pyramids, breathing_volume_trace, annual_plant_dry_mass,
              grassland_biomass_item, model_town_population):
        f()
    for m in REGISTRY:
        m.update({'source_kind': 'original_graph', 'kinds': ['graph'],
                  'generator': 'planning/make_graphs_6116.py (approach of make_diagrams_0455.py)',
                  'rights': {'status': 'original project asset', 'attribution': 'YYeni', 'creator': 'YYeni', 'licence': 'project-owned'},
                  'scientific_review': {'status': 'pending', 'reviewer': None, 'date': None}})
    json.dump({'generated_by': 'planning/make_graphs_6116.py', 'graphs': REGISTRY},
              open(os.path.join(OUT, 'graphs.json'), 'w'), indent=2, ensure_ascii=False)
    print('%d graphs, %d files' % (len(REGISTRY), sum(len(f) for m in REGISTRY for f in m['variants'].values())))
