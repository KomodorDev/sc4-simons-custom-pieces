#!/usr/bin/env python3
"""Compare both parallel-diamond alignments in one unchanged source frame.

This source-coordinate schematic reads the independent traffic expectations,
not compiled S3D models or the two guides' differently translated display grids.
It does not verify saved game resources, install anything, or record a game test.
Run from the repository root with Python 3.11+, NumPy, and Matplotlib installed.
"""
from __future__ import annotations

from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import platform
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'framework'))
from scp.check_bootstrap import SourcePackages
sys.meta_path.insert(0, SourcePackages(ROOT))
from scp import jsonc
from scp.dbpf import require
from scp_highway import parallel_verify as alignment_a
from scp_highway import parallel_alignment_b_verify as alignment_b

SUBJECT = 'ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b'
LIMITS = (-88., 104.)
RAMP_COLOURS = {'lower-off': '#ce7900', 'lower-on': '#158466',
                'upper-off': '#c23d8f', 'upper-on': '#2565b8'}
RAMP_LABELS = {'lower-off': 'L1 exit ramp', 'lower-on': 'L1 entry ramp',
               'upper-off': 'L2 exit ramp', 'upper-on': 'L2 entry ramp'}
HEADER = '''// title: "Parallel-diamond source-coordinate alignment comparison"
// summary: "Bind the A/B grid comparison to independent route expectations, one unchanged source frame, and the generated image bytes."
//
// Used when: Explaining why adjacent diagonal Avenue positions require different whole-cell component cuts.
// Read by: Contributors and players comparing the parallel diamond alignments.
// Updated by: domains/highway/tools/draw_parallel_alignment_comparison.py.
// Affects: This supplementary schematic and its reproducibility; supplies no saved-model, installation, or game observation.
'''


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def source_record(relative):
    raw = (ROOT / relative).read_bytes()
    return {'path': relative, 'bytes': len(raw), 'sha256': digest(raw)}


def route_record(routes):
    rows = [{'source_city_cell': list(cell), 'routes': entries}
            for cell, entries in sorted(routes.items(), key=lambda row: (row[0][1], row[0][0]))]
    raw = json.dumps(rows, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()
    return {'sha256': digest(raw), 'cell_count': len(routes),
            'route_fragment_count': sum(len(entries) for entries in routes.values()),
            'point_count': sum(len(route['points']) for entries in routes.values() for route in entries),
            'ramp_fragments': dict(sorted(Counter(route['approved_ramp'] for entries in routes.values()
                                                   for route in entries if 'approved_ramp' in route).items()))}


def local_traffic(routes, cells):
    """Normalize one complete owner without moving its cuts or traffic lanes."""
    east, south = min(cell[0] for cell in cells), min(cell[1] for cell in cells)
    return sorted((cell[0] - east, cell[1] - south, route['transport'],
                   tuple((round(point[0] - 16. * east, 5), round(point[1] + 16. * south, 5),
                          round(point[2], 5)) for point in route['points']))
                  for cell in cells for route in routes[cell])


def native_axis_offsets(routes, avenue_offset):
    """Check that the independent native lanes support the labelled axes."""
    highway, avenue = set(), set()
    for entries in routes.values():
        for route in entries:
            if route['transport'] != 1 or 'approved_ramp' in route:
                continue
            for east, north, height in route['points']:
                if height > 1.:
                    highway.add(round(north - east + 8., 5))
                else:
                    avenue.add(round(north + east - avenue_offset, 5))
    require(highway == {-3.2, 3.2} and avenue == {-11.2, -4.8, 4.8, 11.2},
            'Independent native lanes no longer support the diagram axis equations')
    return {'highway_north_minus_east_plus_8_m': sorted(highway),
            'avenue_north_plus_east_minus_phase_m': sorted(avenue)}


def main():
    try:
        import matplotlib
        matplotlib.use('Agg')
        from matplotlib import pyplot as plt, patheffects
        from matplotlib.collections import LineCollection
        from matplotlib.lines import Line2D
        from matplotlib.patches import Patch, Rectangle
    except ImportError as error:
        raise SystemExit('Install the drawing dependencies with: python3 -m pip install matplotlib numpy') from error

    matplotlib.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10,
                                'svg.hashsalt': 'scp-parallel-alignment-comparison-v1'})
    sources = [alignment_a.expected_cell_routes(alignment_a.HIGHWAY_SLIP_PROFILE),
               alignment_b.expected_cell_routes()]
    require(set(sources[0]) == alignment_a.OWNED_CELLS and len(sources[0]) == 31,
            'Alignment A no longer matches its retained 31-cell comparison contract')
    require(set(sources[1]) == alignment_b.OWNED_CELLS and len(sources[1]) == 34,
            'Alignment B no longer matches its reviewed 34-cell comparison contract')
    partitions = (alignment_a.PARTITIONS, alignment_b.PARTITIONS)
    require(all(len(rows) == 15 for rows in partitions)
            and partitions[0].keys() == partitions[1].keys(),
            'Comparison requires the same fifteen functional roles in each alignment')
    bounding_tiles = [[max(cell[axis] for cell in rows) - min(cell[axis] for cell in rows) + 1
                       for axis in (0, 1)] for rows in sources]
    require(bounding_tiles == [[8, 8], [9, 9]], 'Comparison ownership bounding rectangles changed')
    offsets = [native_axis_offsets(rows, 16. * index) for index, rows in enumerate(sources)]
    normalized = [{name: local_traffic(routes, cells) for name, cells in groups.items()}
                  for routes, groups in zip(sources, partitions)]
    matches = [[first, second] for first, traffic_a in normalized[0].items()
               for second, traffic_b in normalized[1].items() if traffic_a == traffic_b]
    require(not matches, 'An entire A traffic owner now matches B; revisit the diagram reuse statement')
    ramps = {route['approved_ramp'] for rows in sources for entries in rows.values()
             for route in entries if 'approved_ramp' in route}
    require(ramps == RAMP_COLOURS.keys(), 'Comparison needs exactly the four directed ramp identities')
    crossings = ((4., -4.), (12., 4.))
    require(all(abs(north - east + 8.) < 1e-12 for east, north in crossings)
            and math.isclose(math.dist(*crossings), 8. * math.sqrt(2.), abs_tol=1e-12),
            'Crossing shift must stay on the same native DD axis')
    figure, axes = plt.subplots(1, 2, figsize=(15., 8.5), dpi=180)
    figure.patch.set_facecolor('#f7f9fc')
    figure.subplots_adjust(left=.065, right=.985, bottom=.245, top=.83, wspace=.13)
    figure.suptitle('Assembly - DD RHW-4 — Parallel Diagonal Avenue Diamond',
                   fontsize=18, fontweight='bold', x=.525, y=.975, color='#17283b')
    figure.text(.525, .935,
                'Connection overview | Alignment A and Alignment B · source-coordinate schematic',
                ha='center', fontsize=12, color='#43576d')
    figure.text(.525, .902,
                'Identical limits and scale; native DD highway unchanged. Model surfaces are not drawn.',
                ha='center', fontsize=10, color='#52657a')
    minimum, maximum = LIMITS
    text_box = {'boxstyle': 'round,pad=.3', 'facecolor': 'white',
                'edgecolor': '#d8e1eb', 'alpha': .96}

    for index, (axis, routes, crossing) in enumerate(zip(axes, sources, crossings)):
        axis.set_facecolor('#ffffff')
        for column, row in sorted(routes):
            axis.add_patch(Rectangle((16. * column - 8., -16. * row - 8.), 16., 16.,
                                     facecolor='#e5edf6', edgecolor='#b7c8db',
                                     linewidth=.65, zorder=1))
        for value in range(-88, 105, 16):
            axis.axhline(value, color='#e4e9ef', linewidth=.65, zorder=0)
            axis.axvline(value, color='#e4e9ef', linewidth=.65, zorder=0)
        # The same unshifted highway axis is drawn in both panels. Only the
        # Avenue's additive term changes; the guide-origin translations are
        # deliberately absent from these computations.
        axis.plot((minimum, maximum), (minimum - 8., maximum - 8.),
                  color='#27394f', linewidth=1.1, linestyle='-.', zorder=2)
        avenue_offset = 0. if index == 0 else 16.
        axis.plot((minimum, maximum), (-minimum + avenue_offset, -maximum + avenue_offset),
                  color='#64748b', linewidth=1.05, linestyle='--', zorder=2)
        native_highway, native_avenue, pedestrians = [], [], []
        ramp_segments = {key: [] for key in RAMP_COLOURS}
        for entries in routes.values():
            for route in entries:
                points = [(point[0], point[1]) for point in route['points']]
                if 'approved_ramp' in route:
                    ramp_segments[route['approved_ramp']].append(points)
                elif route['transport'] == 2:
                    pedestrians.append(points)
                elif max(point[2] for point in route['points']) > 1.:
                    native_highway.append(points)
                else:
                    native_avenue.append(points)
        axis.add_collection(LineCollection(native_avenue, colors='#778394', linewidths=1.7, zorder=3))
        axis.add_collection(LineCollection(pedestrians, colors='#99a7b8', linewidths=.8,
                                           linestyles='dotted', zorder=3))
        axis.add_collection(LineCollection(native_highway, colors='#263c57', linewidths=1.7, zorder=4))
        for key, segments in ramp_segments.items():
            halo = LineCollection(segments, colors='white', linewidths=4., zorder=5)
            colour = LineCollection(segments, colors=RAMP_COLOURS[key], linewidths=2.6, zorder=6)
            axis.add_collection(halo); axis.add_collection(colour)
        for point, label in zip(crossings, ('A', 'B')):
            axis.scatter(*point, s=60 if label == 'AB'[index] else 35,
                         facecolor='#17283b' if label == 'AB'[index] else 'white',
                         edgecolor='#17283b', linewidth=.9, zorder=8)
        axis.annotate(f'{"AB"[index]} crossing ({crossing[0]:g}, {crossing[1]:g})',
                      xy=crossing, xytext=(-77., 86.), ha='left', va='center',
                      fontsize=10, color='#20344d', bbox=text_box,
                      arrowprops={'arrowstyle': '-', 'color': '#65778e', 'lw': .8}, zorder=10)
        axis.text(.97, .025, 'DD axis: n = e − 8\nL1: 7.5 m → southwest\nL2: 15 m → northeast',
                  transform=axis.transAxes, ha='right', va='bottom', color='#263c57',
                  fontsize=9, bbox=text_box, zorder=10)
        axis.text(.025, .025, 'Avenue axis: n = −e' + (' + 16' if index else '') + '\nGround height: 0 m',
                  transform=axis.transAxes, ha='left', va='bottom', color='#52657a',
                  fontsize=9, bbox=text_box, zorder=10)
        axis.set(xlim=LIMITS, ylim=LIMITS, aspect='equal',
                 xlabel='East e (metres)', ylabel='North n (metres)')
        axis.set_xticks(range(-64, 97, 32)); axis.set_yticks(range(-64, 97, 32))
        axis.tick_params(labelsize=9, colors='#43576d')
        for spine in axis.spines.values():
            spine.set_color('#bac9da')
        width, depth = bounding_tiles[index]
        axis.set_title(f'Alignment {"AB"[index]}  |  {len(routes)} owned cells  |  {width} × {depth} tiles',
                       fontsize=13, fontweight='bold', color='#20344d', pad=13)

    # The right-angle steps are actual eight-metre source-coordinate changes,
    # rather than a diagram scaled independently from the comparison panels.
    axis = axes[1]
    axis.plot((4., 12., 12.), (-4., -4., 4.), color='#edb74a', linewidth=1.6, zorder=8)
    shift = axis.annotate('', xy=crossings[1], xytext=crossings[0],
                          arrowprops={'arrowstyle': '-|>', 'color': '#141f30', 'lw': 1.6}, zorder=9)
    shift.arrow_patch.set_path_effects([patheffects.Stroke(linewidth=3.8, foreground='white'),
                                       patheffects.Normal()])
    axis.annotate('+8 m east', xy=(8., -4.), xytext=(8., -26.), ha='center', va='top',
                  fontsize=8.5, bbox=text_box,
                  arrowprops={'arrowstyle': '-', 'color': '#bd8d29', 'lw': .8}, zorder=11)
    axis.annotate('+8 m north', xy=(12., 0.), xytext=(37., 11.), ha='left', va='bottom',
                  fontsize=8.5, bbox=text_box,
                  arrowprops={'arrowstyle': '-', 'color': '#bd8d29', 'lw': .8}, zorder=11)
    axis.text(.97, .97, 'A → B: 11.313708 m\nalong the fixed DD axis', transform=axis.transAxes,
              ha='right', va='top', fontsize=9, color='#20344d', bbox=text_box, zorder=10)
    # This ordinary Avenue tile is not counted among B's 34 custom cells.
    axis.add_patch(Rectangle((24., -24.), 16., 16., facecolor='none', edgecolor='#41836e',
                             linestyle='--', linewidth=1.2, zorder=3))

    handles = [Line2D([0], [0], color=colour, linewidth=3., label=RAMP_LABELS[key])
               for key, colour in RAMP_COLOURS.items()]
    handles += [Line2D([0], [0], color='#263c57', linewidth=1.7,
                      label='Native DD lanes (both deck heights share plan positions)'),
                Line2D([0], [0], color='#778394', linewidth=1.7, label='Native Avenue lanes'),
                Patch(facecolor='#e5edf6', edgecolor='#b7c8db', label='Custom-owned 16 × 16 m city cell'),
                Patch(facecolor='none', edgecolor='#41836e', linestyle='--',
                      label='B ordinary Avenue centre (unowned source cell [2,1])')]
    figure.legend(handles=handles, loc='lower center', bbox_to_anchor=(.525, .092),
                  ncol=2, frameon=False, fontsize=9.5, columnspacing=2., handlelength=2.5)
    figure.text(.525, .057,
                'City centres: 16k metres; tile edges: 16k ± 8 metres. Grid squares have equal physical size in both panels.',
                ha='center', color='#43576d', fontsize=9)
    figure.text(.525, .027,
                'Both alignments retain 15 component roles. Different whole-cell traffic cuts prevent direct reuse of an entire A type in B.',
                ha='center', color='#43576d', fontsize=9)
    destination = ROOT / 'domains/highway/01_assemblies' / SUBJECT
    previews, evidence = destination / 'previews', destination / 'evidence'
    previews.mkdir(parents=True, exist_ok=True); evidence.mkdir(parents=True, exist_ok=True)
    png, svg = previews / 'alignment-comparison.png', previews / 'alignment-comparison.svg'
    figure.savefig(png, dpi=180, facecolor=figure.get_facecolor(),
                   metadata={'Software': 'SCP source-coordinate alignment comparison'})
    figure.savefig(svg, facecolor=figure.get_facecolor(),
                   metadata={'Date': None, 'Creator': 'SCP source-coordinate alignment comparison'})
    plt.close(figure)
    source_paths = [Path(__file__).relative_to(ROOT).as_posix(),
                    'framework/scp/check_bootstrap.py', 'framework/scp/jsonc.py',
                    'domains/highway/implementation/scp_highway/parallel_verify.py',
                    'domains/highway/implementation/scp_highway/parallel_alignment_b_verify.py',
                    'domains/highway/implementation/scp_highway/assembly_verify.py', alignment_a.APPROVAL]
    report = {'schema_version': 1, 'purpose': 'Supplementary source-coordinate schematic; no model surfaces are drawn.',
              'input_kind': 'Independent expected traffic route centres, not decoded candidate models or guide display coordinates.',
              'coordinate_frame': {'axes': ['east_m', 'north_m'], 'city_cell_north': '-16 * source_row',
                                   'tile_size_m': 16., 'cell_centres_m': '16k', 'cell_edges_m': '16k ± 8',
                                   'guide_display_origin_translations_applied': False,
                                   'equal_panel_limits_east_m': list(LIMITS), 'equal_panel_limits_north_m': list(LIMITS)},
              'axes': {'fixed_dd': 'north = east - 8', 'avenue_a': 'north = -east',
                       'avenue_b': 'north = -east + 16'},
              'crossings': {'A_en_m': list(crossings[0]), 'B_en_m': list(crossings[1]),
                            'translation_en_m': [8., 8.], 'distance_along_fixed_dd_m': math.dist(*crossings)},
              'alignments': {name: {**route_record(routes), 'owned_source_city_cells': [list(cell) for cell in sorted(routes)],
                                    'bounding_tiles': bounding_tiles[index], 'component_roles': len(partitions[index]),
                                    'native_axis_offsets': offsets[index]}
                             for index, (name, routes) in enumerate(zip(('A', 'B'), sources))},
              'ordinary_b_avenue_centre': {'source_city_cell': [2, 1], 'included_in_custom_ownership': False},
              'whole_alignment_a_type_reused_in_b': False,
              'necessary_whole_traffic_reuse_check': {
                  'source': 'Complete independent expected route set per owner in its local cell frame',
                  'coordinate_comparison_decimals': 5, 'candidate_role_pairs': 225,
                  'matching_a_b_role_pairs': matches,
                  'limit': 'A mismatch excludes exact whole-type reuse; this does not establish broader neighbour compatibility.'},
              'sources': [source_record(relative) for relative in source_paths],
              'renderer': {'python_version': platform.python_version(), 'matplotlib_version': matplotlib.__version__,
                           'figure_inches': [15., 8.5], 'png_dpi': 180, 'png_pixels': [2700, 1530],
                           'ramp_colours': RAMP_COLOURS, 'svg_hashsalt': matplotlib.rcParams['svg.hashsalt']},
              'outputs': [source_record(path.relative_to(ROOT).as_posix()) for path in (png, svg)],
              'saved_model_verification_performed': False, 'installed': False, 'in_game_tested': False}
    target = evidence / 'alignment-comparison.jsonc'
    target.write_text(jsonc.document(report, source=HEADER + '{}\n'), encoding='utf-8')
    print(json.dumps({'schematic': png.relative_to(ROOT).as_posix(),
                      'evidence': target.relative_to(ROOT).as_posix(),
                      'owned_cells': [len(routes) for routes in sources],
                      'shift_en_m': [8., 8.], 'distance_along_dd_m': math.dist(*crossings)}, indent=2))


if __name__ == '__main__':
    main()
