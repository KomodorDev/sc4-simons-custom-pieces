"""Generate source-owned connection overviews from compiled models and resolved boundaries.

The image, selectable README block, and evidence share the same card records.
No Planner import, geometry generation, installation, or manual observation is
performed. Inputs currently require flat-reference, canonical-orientation pieces
with orthogonal source tile boundaries and one measured height per service group;
individual headings, grades, channel associations, and cuts remain explicit.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
import io
import json
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from .render_headers import draw_header, grid_caption, header_settings, level_and_height, piece_title, view_caption

EDGE_NAMES = {0: "West", 1: "North", 2: "East", 3: "South"}
CARDINAL_HEADINGS = {0: "North", 90: "East", 180: "South", 270: "West"}
EDGE_ORDER = {"South": 0, "North": 1, "West": 2, "East": 3}
HEADING_DISPLAY_TOLERANCE = 1e-8
GRADE_DISPLAY_TOLERANCE = 1e-12
BODY_SIZE = 28
PAGE_WIDTH = 2000
PAGE_MARGIN = 48
CARD_GAP = 40
INK = "#17314a"
LABEL_INK = "#455d72"
PAPER = "#f7f9fb"
SERVICE_COLOURS = {
    "hsr": "#007b84", "road": "#9a4e17", "street": "#9a4e17",
    "pedestrian": "#7750a4",
}


def service_colour(record):
    """Use redundant labels and restrained colour to distinguish service panels."""
    return SERVICE_COLOURS.get(record["network"].lower(), record["colour"])


def pale_colour(colour):
    """Mix the visual accent with white; this has no connector-data meaning."""
    values = [int(colour[index:index + 2], 16) for index in (1, 3, 5)]
    return "#" + "".join(f"{round(.10 * value + .90 * 255):02x}" for value in values)

def sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def json_read(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def outward_measurement(member):
    """Reverse incoming travel vectors and grades to point out of the piece."""
    if member["direction"] not in ("in", "out"):
        raise ValueError("A pilot endpoint must declare incoming or outgoing traffic")
    sign = 1 if member["direction"] == "out" else -1
    east, north = (sign * value for value in member["tangent"])
    length = math.hypot(east, north)
    if not math.isfinite(length) or length == 0:
        raise ValueError("An endpoint needs a finite, nonzero horizontal travel tangent")
    outward = [east / length, north / length]
    heading = math.degrees(math.atan2(outward[0], outward[1])) % 360
    if heading == 0:
        heading = 0.0
    grade = sign * member["grade"]
    if not math.isfinite(grade):
        raise ValueError("An endpoint needs a finite measured edge grade")
    if grade == 0:
        grade = 0.0  # Do not display negative zero for an incoming flat end.
    return {
        "outward_horizontal_unit_en": outward,
        "outward_heading_degrees": heading,
        "outward_grade_at_edge": grade,
        "outward_slope_at_edge_percent": 100 * grade,
    }


def common_heading(members):
    """Return the first heading only when every member agrees; never average."""
    first = members[0]["outward_heading_degrees"]
    differences = [abs((member["outward_heading_degrees"] - first + 180) % 360 - 180)
                   for member in members]
    return first if max(differences) <= HEADING_DISPLAY_TOLERANCE else None


def common_outward_grade(members):
    first = members[0]["outward_grade_at_edge"]
    return first if all(abs(member["outward_grade_at_edge"] - first) <= GRADE_DISPLAY_TOLERANCE
                        for member in members) else None


def heading_label(value):
    label = f"{value:g}°"
    for angle, direction in CARDINAL_HEADINGS.items():
        if abs((value - angle + 180) % 360 - 180) <= HEADING_DISPLAY_TOLERANCE:
            return label + f" ({direction})"
    return label


def display_title(piece_id, records, source_name):
    """Retain the public entry point while all view titles share one owner."""
    return piece_title(piece_id, records, source_name)


def wrap_text(draw, value, width, face):
    """Wrap at words or ID hyphens while preserving every source character."""
    lines = []
    for paragraph in str(value).split("\n"):
        remaining = paragraph
        while remaining and draw.textlength(remaining, font=face) > width:
            end = 1
            while end < len(remaining) and draw.textlength(remaining[:end + 1], font=face) <= width:
                end += 1
            break_at = max(remaining.rfind(" ", 0, end), remaining.rfind("-", 0, end) + 1)
            if break_at < end // 2:
                break_at = end
            lines.append(remaining[:break_at].rstrip())
            remaining = remaining[break_at:].lstrip()
        lines.append(remaining)
    return lines


def mono_font(size, font_factory):
    path = Path("/System/Library/Fonts/Menlo.ttc")
    return ImageFont.truetype(str(path), size) if path.is_file() else font_factory(size)


def coordinate_text(point):
    return "[" + ",".join(f"{number:g}" for number in point) + "]"


def classification_text(members):
    labels = []
    for engine, role in sorted({(member["engine_transport"], member["role"]) for member in members}):
        name = "Monorail" if engine == 7 else "Engine class"
        labels.append(f"{name} ({engine}); {role}")
    return " / ".join(labels)


def arrangement_text(record):
    incoming = [member for member in record["members"] if member["direction"] == "in"]
    outgoing = [member for member in record["members"] if member["direction"] == "out"]
    arrangement = f"{len(incoming)} incoming; {len(outgoing)} outgoing"
    declared_offsets = all(member["section_frame_offset_m"] is not None for member in record["members"])
    if (incoming and outgoing and declared_offsets
            and all(member["section_frame_offset_m"] > 0 for member in incoming)
            and all(member["section_frame_offset_m"] < 0 for member in outgoing)):
        running = "Right-hand running"
    elif (incoming and outgoing and declared_offsets
          and all(member["section_frame_offset_m"] < 0 for member in incoming)
          and all(member["section_frame_offset_m"] > 0 for member in outgoing)):
        running = "Left-hand running"
    else:
        running = "See member directions"
    return arrangement, running


def spacing_label(record):
    spacing = record["channel_spacing_m"]
    return f"{spacing:g} m" if spacing is not None else "See individual measured intersections"


def section_origin_label(record):
    anchor = record["anchor_enh_m"]
    return coordinate_text(anchor[:2]) if anchor is not None else "Not declared; see member endpoints"


def section_offset_label(record, *, signed=True):
    offset = record["section_offset_m"]
    if offset is None:
        return "Not declared"
    if record["centred_on_tile_boundary"]:
        return "Centred; 0 m"
    return f"Off-centre; {offset:+g} m" if signed else f"Off-centre; {offset:g} m"


def member_offset_label(member):
    offset = member["section_frame_offset_m"]
    return f"{offset:+g}" if offset is not None else "Not declared"


def build_records(piece):
    """Resolve presentation facts without inferring physical channels from PATH counts."""
    bundles = {bundle["id"]: bundle for bundle in piece["boundary_bundles"]}
    records = []
    for group in piece["groups"]:
        members = group["members"]
        if not members:
            raise ValueError("An overview group needs measured members")
        if len({member["edge"] for member in members}) != 1:
            raise ValueError("Overview members must belong to one source tile boundary")
        heights = {member["endpoint_m"][2] for member in members}
        if len(heights) != 1:
            raise ValueError("Overview currently requires one measured height per service group; use separate groups")
        bundle = bundles[group["boundary_bundle_id"]]
        edge = EDGE_NAMES[members[0]["edge"]]
        if edge.lower() != bundle["edge"]:
            raise ValueError("Resolved source boundary and measured route edge disagree")
        channels = deepcopy(group.get("channels", []))
        if not channels:
            raise ValueError("Overview requires explicit resolved physical-channel and cut associations")
        anchor = list(group["anchor_m"]) if group["anchor_m"] is not None else None
        if anchor is not None:
            anchor[2] = next(iter(heights))
        normal = group["outward_normal"]
        left = [-normal[1], normal[0]]
        measured = []
        for source in sorted(members, key=lambda item: item["id"]):
            member = {key: deepcopy(source[key]) for key in (
                "id", "source_port_id", "direction", "endpoint_m", "tangent", "grade", "edge",
                "engine_transport", "role", "service_network", "channel_id", "cut_id", "traffic_modes")}
            member.update(outward_measurement(source))
            member["section_frame_offset_m"] = (sum(
                (source["endpoint_m"][axis] - anchor[axis]) * left[axis] for axis in (0, 1))
                if anchor is not None else None)
            measured.append(member)
        profile = group.get("profile") or {}
        height = next(iter(heights))
        common = common_heading(measured)
        spacing = None
        cut_records = [cut for channel in channels for cut in channel["cuts"]]
        if len(channels) == 2 and len(cut_records) == 2 and common is not None:
            # Perpendicular-to-route spacing, separate from tile-edge offsets.
            radians = math.radians(common)
            route_left = [-math.cos(radians), math.sin(radians)]
            endpoints = [cut["endpoint_m"] for cut in cut_records]
            spacing = abs(sum((endpoints[1][axis] - endpoints[0][axis]) * route_left[axis]
                              for axis in (0, 1)))
        records.append({
            "id": group["id"], "component_id": group["component_id"],
            "profile_id": group.get("profile_id"), "resolved_profile": deepcopy(profile),
            "network": profile.get("network", measured[0]["service_network"]),
            "nominal_level": profile.get("nominal_level"), "path_height_m": height,
            "boundary_bundle_id": bundle["id"], "source_cell": deepcopy(bundle["source_cell"]),
            "boundary": edge, "anchor_enh_m": anchor, "section_offset_m": group["section_offset_m"],
            "centred_on_tile_boundary": (group["section_offset_m"] == 0
                                         if group["section_offset_m"] is not None else None),
            "physical_channel_count": len(channels), "edge_cut_count": len(cut_records),
            "channel_spacing_m": spacing, "channels": channels,
            "traffic_modes": sorted({mode for member in measured for mode in member["traffic_modes"]}),
            "common_outward_heading_degrees": common,
            "common_outward_grade_at_edge": common_outward_grade(measured),
            "colour": "#007b84" if height >= 30 else "#9a4e17" if height < 20 else "#7750a4",
            "members": measured,
        })
        if anchor is None:
            # The figure needs a marker position, but a drawn marker does not
            # invent a physical section origin. Use one actual endpoint.
            records[-1]["marker_enh_m"] = list(measured[0]["endpoint_m"])
    return records


def make_boundary_cards(records):
    """One physical source edge owns one card, with all service groups inside."""
    cards = {}
    ordered = sorted(records, key=lambda record: (
        *record["source_cell"], EDGE_ORDER[record["boundary"]], record["boundary_bundle_id"], record["id"]))
    for record in ordered:
        identifier = record["boundary_bundle_id"]
        if identifier not in cards:
            cards[identifier] = {
                "id": identifier, "marker": marker_label(len(cards)),
                "source_cell": record["source_cell"], "boundary": record["boundary"],
                "groups": [],
            }
        card = cards[identifier]
        if card["source_cell"] != record["source_cell"] or card["boundary"] != record["boundary"]:
            raise ValueError("One boundary card cannot combine different source tile edges")
        card["groups"].append(record)
        record["marker"] = card["marker"]
    return list(cards.values())


def marker_label(index):
    """Spreadsheet-style display references remain distinct from source IDs."""
    result = ""
    while index >= 0:
        index, digit = divmod(index, 26)
        result = chr(65 + digit) + result
        index -= 1
    return result


def render_boundary_card(card, width, font_factory):
    """Keep one edge card, with clearly bounded, jointly required service panels."""
    padding, line_height = 32, 36
    image = Image.new("RGB", (width, 16000), "#ffffff")
    draw = ImageDraw.Draw(image)
    regular = font_factory(BODY_SIZE)
    mono = mono_font(BODY_SIZE, font_factory)
    heading = font_factory(BODY_SIZE, True)
    card_heading = font_factory(36, True)
    inner_width = width - 2 * padding
    value_x = padding + 350
    y = padding
    runs, blocks, service_sections = [], [], []

    def text(value, x, top, *, face=regular, bold=False, colour=INK, available=None, kind="body"):
        allowed = width - padding - x if available is None else available
        lines = wrap_text(draw, value, allowed, face)
        for number, line in enumerate(lines):
            if draw.textlength(line, font=face) > allowed:
                raise ValueError("A card line exceeds its allocated width")
            position = [x, top + number * line_height]
            draw.text(tuple(position), line, font=face, fill=colour)
            runs.append({"text": line, "position": position, "kind": kind,
                         "bold": bold, "font_size": getattr(face, "size", BODY_SIZE),
                         "monospace": face is mono,
                         "bounds": list(draw.textbbox(tuple(position), line, font=face))})
        return max(1, len(lines)) * line_height

    def section(title):
        nonlocal y
        draw.line((padding, y, width - padding, y), fill="#dbe3e9", width=1)
        y += 18
        text(title, padding, y, face=heading, bold=True, kind="section_heading")
        y += 48

    def rows(values):
        nonlocal y
        for label, value, is_coordinate in values:
            first = text(label, padding, y, colour=LABEL_INK, available=326, kind="field_label")
            second = text(value, value_x, y, face=mono if is_coordinate else regular,
                          kind="field_value")
            blocks.append({"label": label, "value": value, "top": y})
            y += max(first, second) + 6
        y += 14

    # Letters are figure references; the authoritative boundary and group IDs stay intact.
    colour = card["groups"][0]["colour"]
    draw.ellipse((padding, y + 1, padding + 42, y + 43), fill=colour)
    draw.text((padding + 21, y + 21), card["marker"], font=font_factory(28, True),
              fill="#ffffff", anchor="mm")
    name = f"{card['boundary']} edge · cell {coordinate_text(card['source_cell'])}"
    title_height = text(name, padding + 58, y, face=card_heading, bold=True,
                        kind="card_heading")
    y += title_height + 20
    count = len(card["groups"])
    requirement = (f"All {count} service groups are required together at this edge."
                   if count > 1 else "This service group is required at this edge.")
    y += text(requirement, padding, y, face=heading, bold=True,
              kind="boundary_requirement") + 28
    for ordinal, record in enumerate(card["groups"], 1):
        panel_top = y
        panel_colour = service_colour(record)
        service_title = f"{ordinal} / {count}   {record['network'].upper()} — {level_and_height(record)}"
        # Measure before painting so long names expand the header instead of
        # colliding with the ID or the first measurement section.
        title_lines = wrap_text(draw, service_title, inner_width, heading)
        id_lines = wrap_text(draw, record["id"], inner_width, mono)
        header_height = 20 + line_height * (len(title_lines) + len(id_lines)) + 22
        header_bottom = panel_top + header_height
        draw.rectangle((16, panel_top, width - 17, header_bottom),
                       fill=pale_colour(panel_colour))
        draw.rectangle((16, panel_top, 21, header_bottom), fill=panel_colour)
        y += 16
        y += text(service_title, padding, y, face=heading, bold=True,
                  colour=panel_colour, kind="service_heading") + 6
        y += text(record["id"], padding, y, face=mono,
                  kind="service_identity") + 18
        y = header_bottom + 16
        arrangement, running = arrangement_text(record)
        nominal = level_and_height(record)
        if record["nominal_level"] is None:
            nominal += "; no nominal level"
        common_direction = record["common_outward_heading_degrees"]
        common_grade = record["common_outward_grade_at_edge"]
        section("Identity")
        rows([
            ("Network", record["network"].upper(), False),
            ("Component", record["component_id"], True),
            ("Game class / role", classification_text(record["members"]), False),
        ])
        section("Boundary and alignment")
        rows([
            ("Source cell / edge", f"{coordinate_text(record['source_cell'])} / {record['boundary']}", False),
            ("Section origin [E,N] (m)", section_origin_label(record), True),
            ("Centring / section offset", section_offset_label(record), False),
            ("Level (path height)", nominal, False),
            ("Outward heading", heading_label(common_direction) if common_direction is not None
             else "Different; see members", False),
            ("Slope at joining edge", f"{100 * common_grade:g}% (outward)" if common_grade is not None
             else "Different; see members", False),
        ])
        section("Channels and traffic")
        rows([
            ("Channels / cuts / members", f"{record['physical_channel_count']} / {record['edge_cut_count']} / {len(record['members'])}", False),
            ("Traffic arrangement", arrangement, False),
            ("Running convention", running, False),
            ("Channel spacing", spacing_label(record), False),
            ("Channel kinds", ", ".join(sorted({channel.get("kind", "unspecified") for channel in record["channels"]})), False),
            ("Traffic modes", ", ".join(record["traffic_modes"]), False),
        ])
        section("Directed members")
        column_widths = [130, 280, 145, 140, inner_width - 695]
        column_labels = ["Flow", "[E,N,H] (m)", "Offset (m)", "Heading", "Edge slope"]
        for member in record["members"]:
            full_id = member["id"] + f"   source: {member['source_port_id']}"
            used = text(full_id, padding, y, face=mono, kind="member_identity")
            y += used + 12
            y += text(f"Channel: {member['channel_id']} | Cut: {member['cut_id']}",
                      padding, y, face=mono, kind="member_association") + 8
            y += text("Modes: " + ", ".join(member["traffic_modes"]), padding, y,
                      colour=LABEL_INK, kind="member_modes") + 8
            x = padding
            row_height = line_height
            for label, col_width in zip(column_labels, column_widths):
                row_height = max(row_height, text(label, x, y, available=col_width - 5,
                                                  colour=LABEL_INK, kind="member_column"))
                x += col_width
            y += row_height
            values = ["Incoming" if member["direction"] == "in" else "Outgoing",
                      coordinate_text(member["endpoint_m"]), member_offset_label(member),
                      f"{member['outward_heading_degrees']:g}°", f"{member['outward_slope_at_edge_percent']:g}%"]
            x = padding
            row_height = line_height
            for index, (value, col_width) in enumerate(zip(values, column_widths)):
                row_height = max(row_height, text(value, x, y, available=col_width - 5,
                                                  face=regular if index == 0 else mono,
                                                  kind="member_value"))
                x += col_width
            y += row_height + 24
        section("Source references")
        rows([("Boundary ID", card["id"], True)])
        text("Profile", padding, y, colour=LABEL_INK, kind="field_label")
        y += line_height + 4
        y += text(record["profile_id"] or "No profile reference", padding, y, face=mono, available=inner_width,
                  kind="profile_reference")
        y += 28
        panel_bottom = y
        draw.rectangle((16, panel_top, width - 17, panel_bottom),
                       outline="#b9c9d5", width=2)
        draw.line((16, header_bottom, width - 17, header_bottom), fill="#b9c9d5", width=2)
        service_sections.append({
            "group_id": record["id"], "network": record["network"],
            "ordinal": ordinal, "total": count, "required_together": True,
            "title": service_title, "colour": panel_colour,
            "bounds": [16, panel_top, width - 17, panel_bottom],
            "header_bounds": [16, panel_top, width - 17, header_bottom],
        })
        y += 32
    bottom = y + padding
    if bottom >= image.height:
        raise ValueError("Boundary card exceeds its temporary layout canvas")
    image = image.crop((0, 0, width, bottom))
    border = ImageDraw.Draw(image)
    border.rectangle((0, 0, width - 1, bottom - 1), outline="#dbe3e9", width=2)
    border.line((1, 1, width - 2, 1), fill=colour, width=5)
    card["text_runs"] = runs
    card["field_rows"] = blocks
    card["service_sections"] = service_sections
    card["requirement"] = requirement
    card["size"] = [width, bottom]
    return image


def grid_convention(local):
    """Explain displayed southwest-zero indices without moving source coordinates."""
    east, north = local["origin_world_m"]
    min_column, max_row = round(east / 16), round(-north / 16)
    return (f"Display grid: X = source column − ({min_column}); "
            f"Y = {max_row} − source row.")


def compose_figure(piece, records, scene, camera, local, font_factory):
    """Paint geometry markers and complete cards; every wrapped line contributes height."""
    records = deepcopy(records)
    for record in records:
        marker = record.get("marker_enh_m", record["anchor_enh_m"])
        record["viewport_pixel"] = camera.project_world(*marker).tolist()
    cards = make_boundary_cards(records)
    card_width = (PAGE_WIDTH - 2 * PAGE_MARGIN - CARD_GAP) // 2
    card_images = [render_boundary_card(card, card_width, font_factory) for card in cards]
    row_heights = [max(image.height for image in card_images[start:start + 2])
                   for start in range(0, len(card_images), 2)]
    measuring = ImageDraw.Draw(Image.new("RGB", (PAGE_WIDTH, 1)))
    body = font_factory(BODY_SIZE)
    title = display_title(piece["id"], records, piece["piece"]["name"])
    captions = [title, view_caption("connection-overview", 45., 31.), grid_caption(local)]
    header = draw_header(measuring, captions, PAGE_WIDTH, font_factory, margin=PAGE_MARGIN)
    viewport_top = header["bottom"]
    conventions = [
        "Headings: 0° = North, 90° = East, 180° = South, and 270° = West; clockwise in plan view, pointing out of the piece.",
        "Coordinates [E,N,H] = [east,north,height] in metres. Source cells [column,row] increase east and south.",
        grid_convention(local),
        "Slope is measured outward at the joining edge; the interior may differ. Offsets are + left and − right facing out of the tile edge.",
        "Member offsets use the section origin. Counts distinguish physical channels / edge cuts / directed members; modes do not multiply channels.",
        "Incoming flow enters this piece; outgoing flow leaves it. Letters identify boundary cards; source IDs remain the stable identities.",
    ]
    if any(record["anchor_enh_m"] is None for record in records):
        conventions.append("Not declared means no section origin or offset was authored. Its marker uses an actual member endpoint; the measured intersections remain authoritative.")
    evidence_text = [
        "Checked: source-bound metadata, current manifest/DAT identity, saved route-resource identities, and compiled model structure.",
        "This render does not re-extract compiled PATHs or evaluate a candidate placement's occupied-tile fit.",
        "Unverified: physical seams, construction clearance, model collisions, and game operation.",
    ]
    def lines(sentences):
        return [line for value in sentences for line in
                wrap_text(measuring, value, PAGE_WIDTH - 2 * PAGE_MARGIN, body)]
    legend_lines, evidence_lines = lines(conventions), lines(evidence_text)
    legend_y = viewport_top + scene.height + 28
    cards_top = legend_y + 46 + len(legend_lines) * 36 + 40
    footer_y = cards_top + sum(row_heights) + CARD_GAP * (len(row_heights) - 1) + 38
    canvas = Image.new("RGB", (PAGE_WIDTH, footer_y + 46 + len(evidence_lines) * 36 + PAGE_MARGIN), PAPER)
    canvas.paste(scene, (PAGE_MARGIN, viewport_top))
    draw = ImageDraw.Draw(canvas)
    header = draw_header(draw, captions, PAGE_WIDTH, font_factory, margin=PAGE_MARGIN)
    draw.text((PAGE_MARGIN, legend_y), "Reading the connection cards", font=font_factory(30, True), fill=INK)
    for index, line in enumerate(legend_lines):
        draw.text((PAGE_MARGIN, legend_y + 46 + index * 36), line, font=body, fill=LABEL_INK)
    for card in cards:
        for index, record in enumerate(card["groups"]):
            px, py = [record["viewport_pixel"][axis] + (PAGE_MARGIN, viewport_top)[axis] for axis in (0, 1)]
            side = -1 if record["viewport_pixel"][0] < scene.width / 2 else 1
            badge = [px + side * 62, py - 38 - index * 58]
            if not (24 <= badge[0] <= canvas.width - 24 and viewport_top + 24 <= badge[1] <= legend_y - 24):
                raise ValueError("A boundary marker exceeds the reserved scene; increase camera padding")
            colour = record["colour"]
            draw.line([(px, py), tuple(badge)], fill=colour, width=3)
            draw.ellipse((px - 8, py - 8, px + 8, py + 8), fill="white", outline=colour, width=3)
            draw.ellipse((badge[0] - 23, badge[1] - 23, badge[0] + 23, badge[1] + 23), fill=colour)
            draw.text(tuple(badge), card["marker"], font=font_factory(30, True), fill="white", anchor="mm")
            record.update(output_pixel=[px, py], marker_output_pixel=badge,
                          marker_leader_output_pixels=[[px, py], badge])
    row_y = cards_top
    for row, start in enumerate(range(0, len(cards), 2)):
        for column, index in enumerate(range(start, min(start + 2, len(cards)))):
            x = PAGE_MARGIN + column * (card_width + CARD_GAP)
            canvas.paste(card_images[index], (x, row_y))
            cards[index]["output_box"] = [x, row_y, x + card_width, row_y + card_images[index].height]
        row_y += row_heights[row] + CARD_GAP
    draw.text((PAGE_MARGIN, footer_y), "Evidence", font=font_factory(30, True), fill=INK)
    for index, line in enumerate(evidence_lines):
        draw.text((PAGE_MARGIN, footer_y + 46 + index * 36), line, font=body, fill=LABEL_INK)
    return canvas, {
        "display_title": title, "size": list(canvas.size), "camera": camera.metadata(),
        "coordinate_system": local, "viewport_offset_xy": [PAGE_MARGIN, viewport_top],
        "viewport_size": list(scene.size), "title_occurrences": 1,
        "card_columns": 2, "body_font_pixels": BODY_SIZE,
        "header": header, "header_settings": header_settings(),
        "conventions": conventions, "figure_text": [*captions, *conventions, *evidence_text],
        "boundary_cards": [{**{key: value for key, value in card.items() if key != "groups"},
                            "group_ids": [record["id"] for record in card["groups"]]} for card in cards],
        "groups": records,
    }


def markdown_overview(evidence):
    """Selectable text uses the exact resolved records drawn in the figure."""
    lines = ["## Connection overview", "",
             "Generated from this piece's source-bound connector metadata and the current compiled model; marker letters refer to the boundary cards below.", "",
             "![Complete connection overview](previews/connection-overview.png)", "",
             "[Rendering sources and verification scope](evidence/connection-overview.json).", ""]
    for convention in evidence["conventions"]:
        lines.extend([convention, ""])
    groups = {record["id"]: record for record in evidence["groups"]}
    for card in evidence["boundary_cards"]:
        lines.extend([f"### Boundary {card['marker']}: `{card['id']}`", ""])
        count = len(card["group_ids"])
        lines.extend([(f"All {count} service groups are required together at this edge."
                       if count > 1 else "This service group is required at this edge."), ""])
        for ordinal, identifier in enumerate(card["group_ids"], 1):
            record = groups[identifier]
            lines.extend([f"#### Service group {ordinal} / {count}: {record['network'].upper()} — {level_and_height(record)}", ""])
            arrangement, running = arrangement_text(record)
            nominal = level_and_height(record) + ("; no nominal level" if record["nominal_level"] is None else "")
            direction = record["common_outward_heading_degrees"]
            grade = record["common_outward_grade_at_edge"]
            fields = [
                ("End / component", f"`{identifier}` / `{record['component_id']}`"),
                ("Network / game class / role", f"{record['network']} / {classification_text(record['members'])}"),
                ("Source cell / edge", f"`{coordinate_text(record['source_cell'])}` / {record['boundary']}"),
                ("Section origin [E,N] (m)", f"`{section_origin_label(record)}`" if record["anchor_enh_m"] is not None else section_origin_label(record)),
                ("Centring / section offset", section_offset_label(record, signed=False)),
                ("Level (path height)", nominal),
                ("Outward heading", heading_label(direction) if direction is not None else "Different; see members"),
                ("Slope at joining edge", f"{100 * grade:g}% outward" if grade is not None else "Different; see members"),
                ("Channels / edge cuts / directed members", f"{record['physical_channel_count']} / {record['edge_cut_count']} / {len(record['members'])}"),
                ("Traffic arrangement / running", f"{arrangement}; {running}"),
                ("Channel spacing", spacing_label(record)),
                ("Channel kinds", ", ".join(sorted({channel.get("kind", "unspecified") for channel in record["channels"]}))),
                ("Traffic modes", ", ".join(record["traffic_modes"])),
                ("Profile", f"`{record['profile_id']}`" if record["profile_id"] else "No profile reference"),
            ]
            lines.extend(["| Field | Value |", "| --- | --- |"])
            lines.extend(f"| {label} | {value} |" for label, value in fields)
            lines.extend(["", "| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |",
                          "| --- | --- | --- | --- | ---: | ---: | ---: |"])
            for member in record["members"]:
                lines.append(f"| `{member['id']}` / `{member['source_port_id']}` | `{member['channel_id']}` / `{member['cut_id']}` / {', '.join(member['traffic_modes'])} | "
                             f"{'Incoming' if member['direction'] == 'in' else 'Outgoing'} | `{coordinate_text(member['endpoint_m'])}` | "
                             f"{member_offset_label(member)} | {member['outward_heading_degrees']:g}° | {member['outward_slope_at_edge_percent']:g} |")
            lines.append("")
    lines.extend(["Rendering checks source metadata, current compiled resource identities, and model structure. It does not re-extract PATHs or evaluate placement; physical seams, construction clearance, collisions, and game operation remain unverified.", ""])
    return "\n".join(lines)


def readme_overview(original, content):
    """Use the same selectable text and fingerprint in a numbered or legacy guide."""
    from .piece_matrix import LAYOUT_MARKER, SPLIT_LAYOUT_MARKER
    if any(marker in original for marker in (LAYOUT_MARKER, SPLIT_LAYOUT_MARKER)) and content.startswith("## Connection overview\n"):
        import re
        return re.sub(r"(?m)^(#{2,5}) ", r"\1# ", content)
    return content


def _update_readme(path, content):
    begin, end = "<!-- BEGIN CONNECTOR OVERVIEW -->", "<!-- END CONNECTOR OVERVIEW -->"
    original = path.read_text(encoding="utf-8")
    content = readme_overview(original, content)
    block = begin + "\n\n" + content.rstrip() + "\n\n" + end
    if begin in original or end in original:
        if original.count(begin) != 1 or original.count(end) != 1:
            raise ValueError("README connector overview markers are incomplete or duplicated")
        before, rest = original.split(begin, 1)
        _, after = rest.split(end, 1)
        updated = before + block + after
    else:
        marker = "<!-- BEGIN CONNECTIONS -->"
        if marker in original:
            updated = original.replace(marker, block + "\n\n" + marker, 1)
        else:
            updated = original.rstrip() + "\n\n" + block + "\n"
    path.write_text(updated, encoding="utf-8")


def _within(root, relative):
    root, relative = Path(root).resolve(), Path(relative)
    path = (root / relative).resolve()
    if relative.is_absolute() or ".." in relative.parts or not path.is_relative_to(root):
        raise ValueError("Compiled resource paths must remain inside the selected build")
    return path


def render_overviews(custom_root, piece_ids, output_root=None, *, build=None, plugins=None,
                     domain_id="high-speed-rail", resolved=None):
    """Render selected registered types; canonical output also refreshes their README blocks.

    An explicit output_root writes per-piece artifacts outside the library instead.
    Pass the export stage's resolved report to share exactly the same records;
    standalone callers omit resolved and load the source library once here.
    This callable reads an existing build; it never builds or installs resources.
    """
    from .connector_metadata import load_library
    from .city_grid import make_camera, make_city_grid
    from .content import resource_fingerprints
    from .dbpf import decompress, entries
    from .export import compiled_manifest_sha256
    from .models import pack_s3d, parse_s3d, positions, validate_s3d
    from .piece_previews import local_piece_grid
    from .preview import TextureLibrary, font, font_fingerprint, read_piece_preview, render_fast_view, renderer_settings

    root = Path(custom_root).resolve()
    if resolved is None:
        resolved = load_library(root, piece_ids, domain_id=domain_id)
    if not piece_ids or len(set(piece_ids)) != len(piece_ids) or not set(piece_ids) <= resolved["pieces"].keys():
        raise ValueError("Overview selection must name unique pieces present in the resolved library report")
    domain = root / "domains" / domain_id
    build = Path(build or root / "dist/current")
    if not build.is_absolute():
        build = root / build
    build = build.resolve()
    manifest_path = build / "manifest.json"
    manifest = json_read(manifest_path)
    built_by_id = {piece["id"]: piece for piece in manifest["pieces"]}
    manifest_files = {item["path"]: item for item in manifest["files"]}
    if plugins is None:
        fixture = root / "local/validation-inputs/Plugins"
        settings = root / "local/settings.json"
        plugins = fixture if fixture.is_dir() else json_read(settings).get("plugins") if settings.is_file() else None
    if plugins is None:
        raise ValueError("Overview rendering needs an existing texture directory; pass plugins explicitly")
    library = TextureLibrary(Path(plugins).expanduser().resolve())
    staged = []
    for identifier in sorted(piece_ids):
        piece = resolved["pieces"][identifier]
        directory = domain / "00_pieces" / identifier
        built = built_by_id[identifier]
        comparable = lambda item: {key: value for key, value in item.items()
                                   if key not in ("asset_file", "purpose", "design_review")}
        if comparable(built) != comparable(piece["piece"]):
            raise ValueError(f"{identifier}: current compiled definition differs from source")
        dat_path = _within(build, built["asset_file"])
        raw_dat = dat_path.read_bytes()
        declared = manifest_files[built["asset_file"]]
        if sha256(raw_dat) != declared["sha256"] or len(raw_dat) != declared["bytes"]:
            raise ValueError("Compiled DAT differs from its selected manifest")
        resources = {key: decompress(raw) for key, raw in entries(raw_dat).items()}
        actual = resource_fingerprints(identifier, resources)
        saved = piece["connections"]["source"]["resource_fingerprints"]
        compared = {key: digest for key, digest in saved.items() if not key.startswith("construction:")}
        if not compared or any(actual.get(key) != digest for key, digest in compared.items()):
            raise ValueError(f"{identifier}: compiled route/model resources differ from measured source")
        raw_model = read_piece_preview(build, built)
        model = parse_s3d(raw_model)
        validation = validate_s3d(model)
        before_model = sha256(pack_s3d(model))
        textures, texture_sources = library.for_model(model)
        local = local_piece_grid(piece["piece"])
        vertices = [point for block in model["vertices"] for point in positions(block)]
        camera = make_camera(vertices, 45., 31., PAGE_WIDTH - 2 * PAGE_MARGIN, 1000,
                             bounds_world_m=local["bounds_world_m"], padding=90)
        grid, grid_data = make_city_grid(camera, local["bounds_world_m"], origin_world_m=local["origin_world_m"],
                                         font=font(21), bold_font=font(23, True), scale_caption_visible=False)
        scene = render_fast_view(model, textures, 45., 31., camera.width, camera.height,
                                 camera=camera, background_image=grid)
        if sha256(pack_s3d(model)) != before_model:
            raise ValueError("Overview rendering modified the parsed source model")
        image, evidence = compose_figure(piece, build_records(piece), scene, camera, local, font)
        buffer = io.BytesIO()
        image.save(buffer, format="PNG")
        image_bytes = buffer.getvalue()
        old_evidence_path = directory / "evidence/preview.json"
        old_evidence = json_read(old_evidence_path) if old_evidence_path.is_file() else None
        old_source = old_evidence.get("source", {}) if old_evidence else {}
        reviewed_matches = bool(old_evidence and old_source.get("model_sha256") == sha256(raw_model)
                                and old_source.get("source_dat_sha256") == sha256(raw_dat)
                                and old_evidence.get("textures") == texture_sources)
        source_files = [directory / filename for filename in ("piece.json", "connections.json", "connector-groups.jsonc")]
        source_files.append(domain / "domain.json")
        source_files.extend(root / "schemas" / name for name in
                            ("connector-groups.schema.json", "connector-profiles.schema.json"))
        profile_path = domain / json_read(domain / "domain.json").get("connector_profiles", "connector-profiles.json")
        if profile_path.is_file():
            source_files.append(profile_path)
        evidence.update({
            "purpose": "Source-owned connection overview; software source checks do not establish physical or game behavior.",
            "schema_version": 1, "piece_id": identifier, "file": "previews/connection-overview.png",
            "output_sha256": sha256(image_bytes), "source_inputs": {
                path.relative_to(root).as_posix(): sha256(path.read_bytes()) for path in source_files},
            "generator_sha256": sha256(Path(__file__).read_bytes()),
            "metadata_resolver_sha256": sha256((Path(__file__).parent / "connector_metadata.py").read_bytes()),
            "manifest_sha256": sha256(manifest_path.read_bytes()),
            "compiled_manifest_sha256": compiled_manifest_sha256(manifest),
            "source_manifest": str(manifest_path.relative_to(root)) if manifest_path.is_relative_to(root) else str(manifest_path),
            "source_dat": str(dat_path.relative_to(root)) if dat_path.is_relative_to(root) else str(dat_path),
            "source_preview_id": built["preview_id"],
            "source_dat_sha256": sha256(raw_dat), "source_model_sha256": sha256(raw_model),
            "render_model_sha256": before_model, "model_validation": validation,
            "saved_resource_fingerprints_checked": compared, "textures": texture_sources,
            "renderer": renderer_settings(), "grid": grid_data,
            "figure_typography": {
                "body_pixels": BODY_SIZE, "card_title_pixels": 36, "piece_title_pixels": 44,
                "bold_usage": "Piece and card titles, and section headings only",
                "fonts": [font_fingerprint(face)
                          for face in (font(BODY_SIZE), font(BODY_SIZE, True), mono_font(BODY_SIZE, font))],
            },
            "shared_framework_sources": {
                path.name: sha256(path.read_bytes())
                for path in sorted(Path(__file__).parent.glob("*.py"))},
            "previous_preview_evidence": {
                "file": old_evidence_path.relative_to(root).as_posix(),
                "sha256": sha256(old_evidence_path.read_bytes()) if old_evidence else None,
                "mandatory_current_build_truth": False,
            },
            "source_preview_png_used_as_input": False, "source_geometry_altered": False, "geometry_simplified": False,
            "marker_order": "source column, source row, edge rank South/North/West/East, boundary ID; groups by stable ID",
            "supported_inputs": "Registered canonical flat-reference pieces; one measured height per service group; explicit channel/cut associations; no free vertical placement or reflection",
            "evidence_states": {
                "boundary_metadata": "validated", "source_bindings": "validated",
                "manifest_payload": "matched", "saved_resource_identity": "matched",
                "compiled_path_reextraction": "not_run_by_renderer",
                "previous_preview_review": "matched" if reviewed_matches else "different_or_absent; current build retained",
                "occupied_tile_fit": "not_evaluated_no_candidate_placement",
                **{key: "unverified" for key in ("physical_seams", "construction_clearance", "model_collisions", "in_game")},
            },
            "derivations": {
                "channels_and_cuts": "Explicit source-backed associations; counts do not come from modes or directed-member counts",
                "heading": "degrees(atan2(outward_east,outward_north)) modulo 360; incoming travel tangent reversed",
                "edge_slope_percent": "100 * travel grade for outgoing; -100 * travel grade for incoming; never an interior average",
                "section_offset": "Declared resolved offset from source tile-edge midpoint; null when no section offset was authored",
                "member_offset": "Measured endpoint minus declared section origin, dotted with tile-edge outward-left direction; null when the section origin is undeclared",
                "display_anchor": "Declared section origin, or one actual measured endpoint when no origin was authored, projected with the actual model camera; a display marker does not declare a section origin",
            },
        })
        text = readme_overview((directory / "README.md").read_text(encoding="utf-8"), markdown_overview(evidence))
        evidence["selectable_markdown_sha256"] = sha256(text.encode("utf-8"))
        destination = directory if output_root is None else Path(output_root).resolve() / identifier
        staged.append((destination, directory, image_bytes, evidence, text))
    result = {"schema_version": 1, "pieces": {}}
    # Every selected source/resource/layout was checked before canonical files are written.
    for destination, directory, image_bytes, evidence, text in staged:
        (destination / "evidence").mkdir(parents=True, exist_ok=True)
        (destination / "previews").mkdir(parents=True, exist_ok=True)
        image_path, evidence_path = destination / "previews/connection-overview.png", destination / "evidence/connection-overview.json"
        image_path.write_bytes(image_bytes)
        evidence_path.write_text(json.dumps(evidence, indent=2, allow_nan=False) + "\n", encoding="utf-8")
        if output_root is None:
            _update_readme(directory / "README.md", text)
        result["pieces"][evidence["piece_id"]] = {
            "image": str(image_path), "evidence": str(evidence_path), "output_sha256": evidence["output_sha256"],
            "boundary_cards": len(evidence["boundary_cards"]),
        }
    return result


