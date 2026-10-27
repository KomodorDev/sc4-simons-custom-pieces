# HSR Modular Symmetric Split and Return

<!-- PIECE README LAYOUT: 2 -->

[1. Views](#1-views) · [2. Piece and placement](#2-piece-and-placement) · [3. Connection matrix](#3-connection-matrix) · [Testing](TESTING.md)

This reusable High Speed Rail (HSR) junction splits one travel direction into two outlets and merges two entrances into the opposite return direction. Every train path remains at nominal Level 2 (L2), measured at 15.5 m. The pictured fork is one component assembled with further tracks; it is not a complete one-click interchange.

**Status: experimental.** Software pictures and saved-resource checks do not establish human preview approval, game appearance, or train operation. The exact menu name is **HSR Modular Symmetric Split and Return**, and the permanent type ID is `hsr-component-modular-south-junction`.

## 1. Views

Both clean pictures show the same complete saved model at its authored 0° orientation. North is up in the top view; X increases eastward, Y increases northward, and each city tile measures 16 × 16 m. The local picture grid belongs to this reusable type. Its software reference is not a certified mouse-click anchor.

<!-- BEGIN PIECE VIEWS -->

![HSR Modular Symmetric Split and Return — Clean angled view](previews/preview.png)

![HSR Modular Symmetric Split and Return — Clean top view](previews/preview-top.png)

<!-- END PIECE VIEWS -->

The [angled-view evidence](evidence/preview.json) and [top-view evidence](evidence/preview-top.json) identify the actual saved model, textures, camera, captions, and image fingerprints. The connection overview in chapter 3 adds measured boundary cards to that same reusable type.

## 2. Piece and placement

<!-- BEGIN PIECE OVERVIEW -->

Flat L2 paired split and return with three northern outlets for native paired or centred one-way HSR and one southern native paired connection.

Exact reusable identifier: `hsr-component-modular-south-junction`.

Footprint: **3 × 6 tiles**. Exact menu name: **HSR Modular Symmetric Split and Return**.

<!-- END PIECE OVERVIEW -->

### Function and complete joining boundaries

At the authored 0° orientation, the southern paired end connects to a shorter paired end facing north and two separated outer northern ends. The left outer track enters the piece and joins the southbound track. The right outer track leaves the piece from the northbound track. The central paired end continues the two mainline directions. These four permitted journeys are intrinsic to the piece, and the matrix reports them separately from forbidden transfers.

A paired boundary contains both opposite-direction tracks and must continue them together. The southern paired end and the recessed central northern paired end use the native Level 2 paired section. Each outer northern end contains one centred directed track. Its measured centre, height, travel direction, and physical model still require a complete comparison before another piece is accepted as a continuation. The empty tiles around the recessed northern end are not additional declared attachment points.

The permanent construction definition is [piece.json](piece.json), and its geometry belongs in [geometry.json](geometry.json). The [authored connector groups](connector-groups.jsonc), [resolved export](connector-data.json), and [measured connections](connections.json) describe this piece’s intrinsic boundaries and journeys. The library does not supply automatic compatibility discovery, and this guide does not publish a neighbour shortlist.

### Place and rotate the piece

After following the [separate installation procedure](../../../../docs/BUILD_AND_INSTALL.md), use a disposable flat test city. A proper rotation turns the whole piece and all its travel directions together; it does not reflect the piece or reverse a directed track.

1. Open **Transportation → Rail**, hover over the SCP buttons, and select **HSR Modular Symmetric Split and Return**. An assembly can expose the same reusable type through its Tab/Shift+Tab component cycle.
2. Move the complete cursor preview onto clear terrain. Press **Home** or **End** to rotate; on the documented Mac keyboard, **Fn + ←** and **Fn + →** provide those keys. Use only the supported construction states listed below.
3. At 0°, identify the southern paired end, the recessed central paired end facing north, and the two outer northern single-track ends. The left outer end receives traffic; the right outer end sends traffic. Keep the 3 × 6 tile construction rectangle clear for the first trial.
4. Click once to place the component. Supply matching outside connections and travel demand. Inspect tracks, decks, walls, supports, and shadows, then check the permitted journeys and unavailable movements separately.

## 3. Connection matrix

<!-- BEGIN PIECE CONNECTION MATRIX -->

### Directed entrance/exit matrix

Read **from an entrance row to an exit column**. **Saved PATH** checks the saved traffic route; **Route Query** checks the route shown by the game; **Visible travel** checks a vehicle completing that journey. For HSR, visible travel means a moving train.

**Game appearance:** [?](TESTING.md#case-in_game_render-c8a33b58b9fbd61e4079) — the complete piece’s appearance in the game, checked separately from its journeys.

**Legend:** ✅ confirmed; ❌ failed; ? not established. **Forbidden** means the movement is unavailable; its in-game check confirms that it stays unavailable. Click a result for its exact test case. Scope, evidence, and limitations remain in [the test checklist](TESTING.md#test-checklist).

| Entrance ↓ / Exit → | **HSR · South exit**<br>`Sout` | **HSR · North exit**<br>`Nout` | **HSR · North exit**<br>`Rout` |
| --- | --- | --- | --- |
| **HSR · North entrance**<br>`Lin` | **Saved PATH:** [✅](TESTING.md#case-software_connectivity-8d7f9e5f7613da7f657b)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-cf0d19c93952223d47d1)<br>**Visible train travel:** [?](TESTING.md#case-in_game_visible_travel-cf0d19c93952223d47d1) | **Forbidden**<br>**Saved PATH:** [✅](TESTING.md#case-software_connectivity-8d7f9e5f7613da7f657b)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-cebd07ace4c23e3b0b40) | **Forbidden**<br>**Saved PATH:** [✅](TESTING.md#case-software_connectivity-8d7f9e5f7613da7f657b)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-9cc44127a3b0a3f352f1) |
| **HSR · North entrance**<br>`Nin` | **Saved PATH:** [✅](TESTING.md#case-software_connectivity-8d7f9e5f7613da7f657b)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-591b8068a7af8a82744c)<br>**Visible train travel:** [?](TESTING.md#case-in_game_visible_travel-591b8068a7af8a82744c) | **Forbidden**<br>**Saved PATH:** [✅](TESTING.md#case-software_connectivity-8d7f9e5f7613da7f657b)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0d1db4aa8702d16edfa7) | **Forbidden**<br>**Saved PATH:** [✅](TESTING.md#case-software_connectivity-8d7f9e5f7613da7f657b)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-b1c116c697c9ef2bdbe6) |
| **HSR · South entrance**<br>`Sin` | **Forbidden**<br>**Saved PATH:** [✅](TESTING.md#case-software_connectivity-8d7f9e5f7613da7f657b)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0f95ab42ea20b9fade96) | **Saved PATH:** [✅](TESTING.md#case-software_connectivity-8d7f9e5f7613da7f657b)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-3e9107af6496c7d3ac4a)<br>**Visible train travel:** [?](TESTING.md#case-in_game_visible_travel-3e9107af6496c7d3ac4a) | **Saved PATH:** [✅](TESTING.md#case-software_connectivity-8d7f9e5f7613da7f657b)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-abb9d42e6ab5a4275279)<br>**Visible train travel:** [?](TESTING.md#case-in_game_visible_travel-abb9d42e6ab5a4275279) |

Source: [connections.json](connections.json).

<!-- END PIECE CONNECTION MATRIX -->

<!-- BEGIN CONNECTOR OVERVIEW -->

### Connection overview

Generated from this piece's source-bound connector metadata and the current compiled model; marker letters refer to the boundary cards below.

![Complete connection overview](previews/connection-overview.png)

[Rendering sources and verification scope](evidence/connection-overview.json).

Headings: 0° = North, 90° = East, 180° = South, and 270° = West; clockwise in plan view, pointing out of the piece.

Coordinates [E,N,H] = [east,north,height] in metres. Source cells [column,row] increase east and south.

Display grid: X = source column − (0); Y = 5 − source row.

Slope is measured outward at the joining edge; the interior may differ. Offsets are + left and − right facing out of the tile edge.

Member offsets use the section origin. Counts distinguish physical channels / edge cuts / directed members; modes do not multiply channels.

Incoming flow enters this piece; outgoing flow leaves it. Letters identify boundary cards; source IDs remain the stable identities.

#### Boundary A: `cell-0-0-north`

This service group is required at this edge.

##### Service group 1 / 1: HSR — Level 2 (15.5 m)

| Field | Value |
| --- | --- |
| End / component | `left-northern-end` / `symmetric-split-return` |
| Network / game class / role | hsr / Monorail (7); primary |
| Source cell / edge | `[0,0]` / North |
| Section origin [E,N] (m) | `[0,8]` |
| Centring / section offset | Centred; 0 m |
| Level (path height) | Level 2 (15.5 m) |
| Outward heading | 0° (North) |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | rail |
| Traffic modes | monorail |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `left-northern-end-lin` / `Lin` | `left-return-branch` / `left-northern-end-left-return-branch-cut` / monorail | Incoming | `[0,8,15.5]` | +0 | 0° | 0 |

#### Boundary B: `cell-1-2-north`

This service group is required at this edge.

##### Service group 1 / 1: HSR — Level 2 (15.5 m)

| Field | Value |
| --- | --- |
| End / component | `north-paired-end` / `symmetric-split-return` |
| Network / game class / role | hsr / Monorail (7); primary |
| Source cell / edge | `[1,2]` / North |
| Section origin [E,N] (m) | `[16,-24]` |
| Centring / section offset | Centred; 0 m |
| Level (path height) | Level 2 (15.5 m) |
| Outward heading | 0° (North) |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 2 / 2 / 2 |
| Traffic arrangement / running | 1 incoming; 1 outgoing; Right-hand running |
| Channel spacing | 4 m |
| Channel kinds | rail |
| Traffic modes | monorail |
| Profile | `hsr-l2-orth-scp-paired15-t2-opposed-rhd-v1` |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `north-paired-end-nin` / `Nin` | `southbound-mainline` / `north-paired-end-southbound-mainline-cut` / monorail | Incoming | `[14,-24,15.5]` | +2 | 0° | 0 |
| `north-paired-end-nout` / `Nout` | `northbound-mainline` / `north-paired-end-northbound-mainline-cut` / monorail | Outgoing | `[18,-24,15.5]` | -2 | 0° | 0 |

#### Boundary C: `cell-1-5-south`

This service group is required at this edge.

##### Service group 1 / 1: HSR — Level 2 (15.5 m)

| Field | Value |
| --- | --- |
| End / component | `south-paired-end` / `symmetric-split-return` |
| Network / game class / role | hsr / Monorail (7); primary |
| Source cell / edge | `[1,5]` / South |
| Section origin [E,N] (m) | `[16,-88]` |
| Centring / section offset | Centred; 0 m |
| Level (path height) | Level 2 (15.5 m) |
| Outward heading | 180° (South) |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 2 / 2 / 2 |
| Traffic arrangement / running | 1 incoming; 1 outgoing; Right-hand running |
| Channel spacing | 4 m |
| Channel kinds | rail |
| Traffic modes | monorail |
| Profile | `hsr-l2-orth-scp-paired15-t2-opposed-rhd-v1` |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `south-paired-end-sin` / `Sin` | `northbound-mainline` / `south-paired-end-northbound-mainline-cut` / monorail | Incoming | `[18,-88,15.5]` | +2 | 180° | 0 |
| `south-paired-end-sout` / `Sout` | `southbound-mainline` / `south-paired-end-southbound-mainline-cut` / monorail | Outgoing | `[14,-88,15.5]` | -2 | 180° | 0 |

#### Boundary D: `cell-2-0-north`

This service group is required at this edge.

##### Service group 1 / 1: HSR — Level 2 (15.5 m)

| Field | Value |
| --- | --- |
| End / component | `right-northern-end` / `symmetric-split-return` |
| Network / game class / role | hsr / Monorail (7); primary |
| Source cell / edge | `[2,0]` / North |
| Section origin [E,N] (m) | `[32,8]` |
| Centring / section offset | Centred; 0 m |
| Level (path height) | Level 2 (15.5 m) |
| Outward heading | 0° (North) |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | rail |
| Traffic modes | monorail |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `right-northern-end-rout` / `Rout` | `right-departure-branch` / `right-northern-end-right-departure-branch-cut` / monorail | Outgoing | `[32,8,15.5]` | +0 | 0° | 0 |

Rendering checks source metadata, current compiled resource identities, and model structure. It does not re-extract PATHs or evaluate placement; physical seams, construction clearance, collisions, and game operation remain unverified.

<!-- END CONNECTOR OVERVIEW -->
