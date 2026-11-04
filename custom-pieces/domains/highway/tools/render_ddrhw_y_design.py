#!/usr/bin/env python3
"""Draw the DD RHW Y source experiment, without inventing compiled geometry."""
from __future__ import annotations

import argparse
import hashlib
import math
from pathlib import Path
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

HIGHWAY = Path(__file__).resolve().parents[1]
LIBRARY = HIGHWAY.parents[1]
REPOSITORY = LIBRARY.parent
sys.path.insert(0, str(LIBRARY / "framework"))
from scp import jsonc

SUBJECT = HIGHWAY / "01_assemblies/ddrhw-compact-diagonal-y-junction"
COLOURS = {"A-B": "#1976ba", "B-A": "#b86c1d", "A-C": "#228047",
           "C-A": "#bf497c", "B-C": "#7954b3", "C-B": "#168b91"}
INK, MUTED, GRID = "#203844", "#536875", "#d8e0e4"
HEADER = '''// title: "Compact DD RHW Y source schematic provenance"
// summary: "Bind the source-only drawing to its actual geometry and renderer."
//
// Used when: Regenerating or reviewing the first DD RHW Y source schematic.
// Read by: Contributors reviewing the owning assembly design and testing documents.
// Updated by: domains/highway/tools/render_ddrhw_y_design.py after source-geometry checks.
// Affects: The source schematic only; it establishes no model, ownership, installation, or game result.
'''


def font(size):
    for candidate in ("DejaVuSans.ttf", "arial.ttf", "/System/Library/Fonts/Supplemental/Arial.ttf"):
        try:
            return ImageFont.truetype(candidate, size)
        except OSError:
            pass
    return ImageFont.load_default(size=size)


def arrow(draw, points, index, colour):
    point = np.asarray(points[index])
    direction = point - points[max(0, index-3)]
    direction /= np.linalg.norm(direction)
    normal = np.array([-direction[1], direction[0]])
    triangle = [point+9*direction, point-10*direction+6*normal, point-10*direction-6*normal]
    draw.polygon([tuple(p) for p in triangle], fill=colour)


def render(report, output):
    if not all(report["checks"].values()):
        raise ValueError("Refusing to draw a source candidate with failed checks")
    image = Image.new("RGB", (1700, 1050), "#ffffff")
    draw = ImageDraw.Draw(image)
    def text(position, value, size=22, colour=INK, anchor=None):
        draw.text(position, value, font=font(size), fill=colour, anchor=anchor)
    text((60, 34), "Assembly - DD RHW-4 — Compact Y-Junction — Diagonal Stem", 32)
    text((60, 83), "Connection overview — source schematic, north up", 24)
    text((60, 124), "SCHEMATIC · measured lane routes and provisional road widths", 20, MUTED)

    routes = {name: np.asarray(points) for name, points in report["routes"].items()}
    sockets = report["native_socket_members"]
    columns = [s["outside_cell_col_row"][0] for s in sockets]
    rows = [s["outside_cell_col_row"][1] for s in sockets]
    west, east = min(columns)*16-8, max(columns)*16+8
    south, north = -max(rows)*16-8, -min(rows)*16+8
    scale = min(910/(east-west), 690/(north-south))
    left, top = 105, 245
    width, height = (east-west)*scale, (north-south)*scale
    def plan(point):
        return (left+(point[0]-west)*scale, top+(north-point[1])*scale)
    for col in range(min(columns), max(columns)+2):
        x = left+(col*16-8-west)*scale
        draw.line([(x, top), (x, top+height)], fill=GRID, width=1)
    for row in range(min(rows), max(rows)+2):
        y = top+(north-(-row*16+8))*scale
        draw.line([(left, y), (left+width, y)], fill=GRID, width=1)
    for col in range(min(columns), max(columns)+1):
        text((plan((col*16, south))[0], top+height+20), f"X{col-min(columns)}", 20, anchor="mt")
    for row in range(min(rows), max(rows)+1):
        text((left-18, plan((west, -row*16))[1]), f"Y{max(rows)-row}", 20, anchor="rm")
    for route in routes.values():
        tangent = np.gradient(route[:, :2], axis=0)
        tangent /= np.linalg.norm(tangent, axis=1)[:, None]
        normal = np.column_stack([-tangent[:, 1], tangent[:, 0]])
        half_width = report["parameters"]["provisional_pavement_width_m"]/2
        left_edge, right_edge = route[:, :2]+half_width*normal, route[:, :2]-half_width*normal
        draw.polygon([plan(point) for point in np.vstack([left_edge, right_edge[::-1]])], fill="#edf0f2")
    for name, route in routes.items():
        points = [plan(point) for point in route]
        if name in ("B-A", "C-A"):
            for index in range(0, len(points)-1, 16):
                draw.line(points[index:index+9], fill=COLOURS[name], width=4)
        else:
            draw.line(points, fill=COLOURS[name], width=5, joint="curve")
        arrow(draw, points, int((len(points)-1)*0.35), COLOURS[name])
    for socket in sockets:
        col, row = socket["outside_cell_col_row"]
        first, last = plan((16*col-8, -16*row+8)), plan((16*col+8, -16*row-8))
        draw.rectangle([first, last], outline=MUTED, width=2)
        text(plan((16*col, -16*row)), socket["arm"], 25, anchor="mm")
    text((left+width-18, top-35), "N", 22, anchor="mm")
    draw.line([(left+width-18, top+20), (left+width-18, top-12)], fill=INK, width=2)
    draw.polygon([(left+width-18, top-20), (left+width-23, top-10), (left+width-13, top-10)], fill=INK)

    text((1100, 211), "One lane for each journey", 25)
    for index, name in enumerate(routes):
        y = 263+index*48
        draw.line([(1100, y+12), (1140, y+12)], fill=COLOURS[name], width=5)
        route = routes[name]
        text((1157, y), f"{name.replace('-', ' → ')}     {route[0, 2]:g} → {route[-1, 2]:g} m", 23)
    text((1100, 574), "B and C ramps: height profiles", 24)
    px, py, pw, ph = 1130, 635, 490, 235
    max_run = max(report["route_measurements"][name]["length"] for name in ("B-C", "C-B"))
    for z in (7.5, 10, 12.5, 15):
        y = py+ph*(15-z)/7.5
        draw.line([(px, y), (px+pw, y)], fill=GRID, width=1)
        text((px-12, y), f"{z:g}", 18, anchor="rm")
    for station in range(0, math.ceil(max_run), 20):
        x = px+pw*station/max_run
        draw.line([(x, py), (x, py+ph)], fill=GRID, width=1)
        text((x, py+ph+10), str(station), 18, anchor="mt")
    for name in ("B-C", "C-B"):
        route = routes[name]
        stations = np.r_[0, np.linalg.norm(np.diff(route[:, :2], axis=0), axis=1).cumsum()]
        points = [(px+pw*s/max_run, py+ph*(15-z)/7.5) for s, z in zip(stations, route[:, 2])]
        draw.line(points, fill=COLOURS[name], width=4)
    text((px+pw/2, py+ph+40), "Distance along each lane (m)", 19, anchor="mt")
    road_width = report["parameters"]["provisional_pavement_width_m"]
    text((60, 982), f"Grid: 16 m squares. Grey bands: provisional {road_width:g} m corridors. Outlined cells: outside native sockets.", 21, MUTED)
    output.parent.mkdir(parents=True, exist_ok=True)
    image.save(output)
    return {"width_px": image.width, "height_px": image.height,
            "display_frame": {"southwest_tile_centre_en_m": [16*min(columns), -16*max(rows)],
                              "x_range": [0, max(columns)-min(columns)], "y_range": [0, max(rows)-min(rows)]},
            "scope": "Source-only lane curves and unclipped provisional width strips; not compiled models or construction ownership."}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--geometry", type=Path, default=SUBJECT/"evidence/design-geometry.jsonc")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--evidence", type=Path, required=True)
    args = parser.parse_args(argv)
    result = render(jsonc.load(args.geometry), args.output)
    result["input_fingerprints"] = {"design_geometry_sha256": hashlib.sha256(args.geometry.read_bytes()).hexdigest(),
                                    "renderer_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    result["image"] = {"path": args.output.resolve().relative_to(REPOSITORY).as_posix(),
                       "sha256": hashlib.sha256(args.output.read_bytes()).hexdigest()}
    args.evidence.parent.mkdir(parents=True, exist_ok=True)
    if not args.evidence.exists():
        args.evidence.write_text(HEADER, encoding="utf-8")
    jsonc.dump(args.evidence, result)
    print("Source schematic generated; no game model or construction-footprint claim.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
