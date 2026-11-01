# RHW Ramp — L1 Entry Parallel Grade — Parallel — Alignment B

Reusable Alignment B component for the close parallel diagonal diamond.

<!-- PIECE README LAYOUT: 2 -->

[1. Views](#1-views) · [2. Piece and placement](#2-piece-and-placement) · [3. Connection matrix](#3-connection-matrix) · [Testing ↗ (separate document)](TESTING.md)

## 1. Views

The angled view shows this type's actual model and overhang; the north-up view shows its relation to the city grid. These software pictures do not establish game appearance, native-neighbour compatibility, or visible traffic. Use the component's own pictures when comparing it with another type.

<!-- BEGIN PIECE VIEWS -->

![RHW Ramp — L1 Entry Parallel Grade — Parallel — Alignment B — Clean angled view](previews/preview.png)

![RHW Ramp — L1 Entry Parallel Grade — Parallel — Alignment B — Clean top view](previews/preview-top.png)

<!-- END PIECE VIEWS -->

## 2. Piece and placement

This is the fixed entry height transition between its flat lateral departure and the Avenue right-turn terminal. Its physical ramp runs parallel to the highway. It carries the complete native traffic fragments required by every city tile it owns, even when the corresponding visible highway model is supplied by a neighbouring slip component.

**Permanent ID:** `ddrhw-parallel-b-lower-entry-grade`. **Recipe:** `highway_ddrhw_parallel_b_lower_entry_grade`. This component owns **3 city tiles** inside a **2 × 2 bounding footprint**. Its local occupied cells are **[1,0], [0,1], [1,1]**, measured from the reference corner with columns increasing east and rows increasing south. Empty cells inside that rectangle remain unowned. Physical grade between 7.5 m and 0 m; actual cell-edge ports have their own measured intermediate heights.

1. Open **Transportation → Highways → SCP | DD RHW-4 — Parallel Diagonal Avenue Diamond**, and select **SCP | ASSEMBLY | DD RHW-4 — Parallel Diagonal Avenue Diamond — Alignment B**.
2. Starting at P01, press **Tab 12 times** to reach **P13 — RHW Ramp — L1 Entry Parallel Grade — Parallel — Alignment B**. Shift+Tab moves backward. Each click places this component, rather than the whole junction.
3. In the [B reference layout](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond-alignment-b/README.md#3-placements), use **X2, Y5**, with the authored **0°** orientation. Home and End rotate the selected type. Match its actual occupied preview cells before clicking; the reference corner can itself be empty.
4. Join only the complete matching B boundary described by its connection card and the assembly placement plan. A similar A model does not establish matching whole-cell PATH ownership. For an independent layout, check every direction, endpoint, height, angle, and grade; compatibility with an untested neighbour remains unverified.

This component has no adaptive Avenue cells of its own. Dynamic pavement belongs to the crossing, the two ground terminals, and the ordinary native Avenue around them; no fixed sidewalk slab is added here.

All B components intentionally generate no custom cast shadows. A **PATH** is the directed game traffic resource; a visible road surface and a PATH connection establish different facts. Preserve this type's complete owned-cell traffic data when reusing it. New B identifiers require fresh placement, and game results are recorded separately in [TESTING.md](TESTING.md).

<!-- BEGIN PIECE OVERVIEW -->

Place one l1 entry parallel grade for Alignment B of the close parallel diagonal diamond. Use the complete connection cards and assembly grid; heights are fixed.

Exact reusable identifier: `ddrhw-parallel-b-lower-entry-grade`.

Footprint: **2 × 2 tiles**. Exact menu name: **RHW Ramp — L1 Entry Parallel Grade — Parallel — Alignment B**.

<!-- END PIECE OVERVIEW -->

## 3. Connection matrix

The generated matrix describes this piece's intrinsic measured journeys. Its connector overview identifies exposed boundaries, including any overhang; it does not establish compatibility with an untested neighbour. Route Query and visible travel retain separate observation cases.

<!-- BEGIN PIECE CONNECTION MATRIX -->

### Directed entrance/exit matrix

Read **from an entrance row to an exit column**. **Saved PATH** checks the saved traffic route; **Route Query** checks the route shown by the game; **Visible travel** checks a vehicle completing that journey. For HSR, visible travel means a moving train.

**Game appearance:** [?](TESTING.md#case-in_game_render-2f81982b55bf2ce2a1f4) — the complete piece’s appearance in the game, checked separately from its journeys.

**Legend:** ✅ confirmed; ❌ failed; ? not established. **Forbidden** means the movement is unavailable; its in-game check confirms that it stays unavailable. Click a result for its exact test case. Scope, evidence, and limitations remain in [the test checklist](TESTING.md#test-checklist).

| Entrance ↓ / Exit → | **Road · South exit**<br>`channel-06-out`<br>Variant: access-ramp | **Road · South exit**<br>`channel-07-out`<br>Variant: dd-rhw-l1 | **Road · South exit**<br>`channel-08-out`<br>Variant: dd-rhw-l1 | **Road · East exit**<br>`channel-09-out`<br>Variant: dd-rhw-l2 | **Road · East exit**<br>`channel-10-out`<br>Variant: dd-rhw-l2 |
| --- | --- | --- | --- | --- | --- |
| **Road · South entrance**<br>`channel-01-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-75b83547c768d45af3ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-7b9cefaff8063e0719b6) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-75b83547c768d45af3ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-81cda6b29dbb0b27c824) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-75b83547c768d45af3ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c5829065c86412159e8e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-75b83547c768d45af3ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-98c41d66581a8544a48e) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-75b83547c768d45af3ff)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-7ff2dac135f42aac3a02)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-7ff2dac135f42aac3a02) |
| **Road · South entrance**<br>`channel-02-in`<br>Variant: dd-rhw-l2 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-75b83547c768d45af3ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-0ffa6220bdac40c42999) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-75b83547c768d45af3ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-8025486b2a8f37811912) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-75b83547c768d45af3ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d75ca289b1f938e21118) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-75b83547c768d45af3ff)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-3865139866625ba8c96d)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-3865139866625ba8c96d) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-75b83547c768d45af3ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-6a6b5ad6823142562210) |
| **Road · East entrance**<br>`channel-03-in`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-75b83547c768d45af3ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-c2ff94978dc0f036c75a) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-75b83547c768d45af3ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-d27455d5ee6bf0dceb76) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-75b83547c768d45af3ff)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-b8e265afb724d969433e)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-b8e265afb724d969433e) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-75b83547c768d45af3ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-4fa88819770e1fbb26b1) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-75b83547c768d45af3ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-a64f69ad6ff2beb16081) |
| **Road · East entrance**<br>`channel-04-in`<br>Variant: dd-rhw-l1 | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-75b83547c768d45af3ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-bb26929ce51123c465fb) | **Saved PATH:** [?](TESTING.md#case-software_connectivity-75b83547c768d45af3ff)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-492d3489a2fe59747e92)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-492d3489a2fe59747e92) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-75b83547c768d45af3ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-48c2c03c5d6047455530) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-75b83547c768d45af3ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-57f2ee447f105c0d8243) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-75b83547c768d45af3ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-faac9829a271a799c834) |
| **Road · East entrance**<br>`channel-05-in`<br>Variant: access-ramp | **Saved PATH:** [?](TESTING.md#case-software_connectivity-75b83547c768d45af3ff)<br>**Route Query:** [?](TESTING.md#case-in_game_route_query-76a6e23dc9d117bcd037)<br>**Visible travel:** [?](TESTING.md#case-in_game_visible_travel-76a6e23dc9d117bcd037) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-75b83547c768d45af3ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-e2565bbab95c6646be83) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-75b83547c768d45af3ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-34f2b5299616fc5d8904) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-75b83547c768d45af3ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-2258fda8f83392b6c727) | **Forbidden**<br>**Saved PATH:** [?](TESTING.md#case-software_connectivity-75b83547c768d45af3ff)<br>In-game check: [?](TESTING.md#case-in_game_forbidden_transfer-98253f47a69712812063) |

Source: [connections.json](connections.json).

<!-- END PIECE CONNECTION MATRIX -->

<!-- BEGIN CONNECTOR OVERVIEW -->

### Connection overview

Generated from this piece's source-bound connector metadata and the current compiled model; marker letters refer to the boundary cards below.

![Complete connection overview](previews/connection-overview.png)

[Rendering sources and verification scope](evidence/connection-overview.json).

Headings: 0° = North, 90° = East, 180° = South, and 270° = West; clockwise in plan view, pointing out of the piece.

Coordinates [E,N,H] = [east,north,height] in metres. Source cells [column,row] increase east and south.

Display grid: X = source column − (0); Y = 1 − source row.

Slope is measured outward at the joining edge; the interior may differ. Offsets are + left and − right facing out of the tile edge.

Member offsets use the section origin. Counts distinguish physical channels / edge cuts / directed members; modes do not multiply channels.

Incoming flow enters this piece; outgoing flow leaves it. Letters identify boundary cards; source IDs remain the stable identities.

Not declared means no section origin or offset was authored. Its marker uses an actual member endpoint; the measured intersections remain authoritative.

#### Boundary A: `boundary-01`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (6.39058 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-01-access-network-lower-on-01` / `access-network-lower-on` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[0,1]` / South |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (6.39058 m); no nominal level |
| Outward heading | 225° |
| Slope at joining edge | 17.9116% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 0 incoming; 1 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-06-out` / `channel-06-out` | `access-lower-on` / `cut-channel-06-out` / car | Outgoing | `[-0.970563,-24,6.39058]` | Not declared | 225° | 17.9116 |

#### Boundary B: `boundary-02`

This service group is required at this edge.

##### Service group 1 / 1: ROAD — Custom (0.083612 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-02-access-network-lower-on-01` / `access-network-lower-on` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,0]` / East |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (0.083612 m); no nominal level |
| Outward heading | 45° |
| Slope at joining edge | -11.5841% outward |
| Channels / edge cuts / directed members | 1 / 1 / 1 |
| Traffic arrangement / running | 1 incoming; 0 outgoing; See member directions |
| Channel spacing | See individual measured intersections |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-05-in` / `channel-05-in` | `access-lower-on` / `cut-channel-05-in` / car | Incoming | `[24,0.970563,0.083612]` | Not declared | 45° | -11.5841 |

#### Boundary C: `boundary-04`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-04-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,1]` / South |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (7.5 m); no nominal level |
| Outward heading | 225° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 2 / 2 / 2 |
| Traffic arrangement / running | 0 incoming; 2 outgoing; See member directions |
| Channel spacing | 4.52548 m |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-07-out` / `channel-07-out` | `lower-mainline-axis-plus-2-26274-negative` / `cut-channel-07-out` / car | Outgoing | `[12.8,-24,7.5]` | Not declared | 225° | 0 |
| `member-channel-08-out` / `channel-08-out` | `lower-mainline-axis-minus-2-26274-negative` / `cut-channel-08-out` / car | Outgoing | `[19.2,-24,7.5]` | Not declared | 225° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-04-upper-mainline-02` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,1]` / South |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (15 m); no nominal level |
| Outward heading | 225° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 2 / 2 / 2 |
| Traffic arrangement / running | 2 incoming; 0 outgoing; See member directions |
| Channel spacing | 4.52548 m |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-01-in` / `channel-01-in` | `upper-mainline-axis-plus-2-26274-positive` / `cut-channel-01-in` / car | Incoming | `[12.8,-24,15]` | Not declared | 225° | 0 |
| `member-channel-02-in` / `channel-02-in` | `upper-mainline-axis-minus-2-26274-positive` / `cut-channel-02-in` / car | Incoming | `[19.2,-24,15]` | Not declared | 225° | 0 |

#### Boundary D: `boundary-03`

All 2 service groups are required together at this edge.

##### Service group 1 / 2: ROAD — Custom (7.5 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-03-lower-mainline-01` / `lower-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,1]` / East |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (7.5 m); no nominal level |
| Outward heading | 45° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 2 / 2 / 2 |
| Traffic arrangement / running | 2 incoming; 0 outgoing; See member directions |
| Channel spacing | 4.52548 m |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-03-in` / `channel-03-in` | `lower-mainline-axis-minus-2-26274-negative` / `cut-channel-03-in` / car | Incoming | `[24,-19.2,7.5]` | Not declared | 45° | 0 |
| `member-channel-04-in` / `channel-04-in` | `lower-mainline-axis-plus-2-26274-negative` / `cut-channel-04-in` / car | Incoming | `[24,-12.8,7.5]` | Not declared | 45° | 0 |

##### Service group 2 / 2: ROAD — Custom (15 m)

| Field | Value |
| --- | --- |
| End / component | `boundary-03-upper-mainline-02` / `upper-mainline` |
| Network / game class / role | road / Engine class (1); primary |
| Source cell / edge | `[1,1]` / East |
| Section origin [E,N] (m) | Not declared; see member endpoints |
| Centring / section offset | Not declared |
| Level (path height) | Custom (15 m); no nominal level |
| Outward heading | 45° |
| Slope at joining edge | 0% outward |
| Channels / edge cuts / directed members | 2 / 2 / 2 |
| Traffic arrangement / running | 0 incoming; 2 outgoing; See member directions |
| Channel spacing | 4.52548 m |
| Channel kinds | road-lane |
| Traffic modes | car |
| Profile | No profile reference |

| Member / measured source | Channel / cut / modes | Flow | Endpoint [E,N,H] (m) | Offset (m) | Outward heading | Edge slope (%) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `member-channel-09-out` / `channel-09-out` | `upper-mainline-axis-minus-2-26274-positive` / `cut-channel-09-out` / car | Outgoing | `[24,-19.2,15]` | Not declared | 45° | 0 |
| `member-channel-10-out` / `channel-10-out` | `upper-mainline-axis-plus-2-26274-positive` / `cut-channel-10-out` / car | Outgoing | `[24,-12.8,15]` | Not declared | 45° | 0 |

The overview uses source metadata, current compiled resource identities, and the saved model. Current placement, connection, and traffic results belong to the generated connection matrix and linked testing records.

<!-- END CONNECTOR OVERVIEW -->
