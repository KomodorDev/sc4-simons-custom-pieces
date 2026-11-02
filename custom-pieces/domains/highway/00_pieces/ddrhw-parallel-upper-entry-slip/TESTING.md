---
title: "Testing: DD RHW-4 — L2 Entry Slip Lanes — Parallel"
summary: "Check this parallel component against its saved resources and retain separate human game observations."
audience: "contributors"
document_type: "reference"
---

# Testing: DD RHW-4 — L2 Entry Slip Lanes — Parallel

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

The current policy is **no cast shadow from this component**. Verify that appearance on a fresh placement after restarting with the checked no-shadow revision; older saved-attachment cleanup is a separate pending observation. The assembly’s [current no-shadow test](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#44-independent-module-shadow-test) owns the detailed camera, quality, zoom, and lifecycle procedure.

This record covers **ddrhw-parallel-upper-entry-slip**, used once as **P07** in the [parallel diamond](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/README.md). It has 2 occupied tiles in a 2 × 2 rectangle, the exact authored 0° reference at X7, Y8, and the functional levels described in the [piece guide](README.md#2-piece-and-placement). Saved native through routes, added access fragments, actual model support, material flags, physical joins, rotations, and adaptive resources where present have distinct software checks. Human appearance and travel observations remain separate.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `channel-11-out` | road / 1 / primary | out | [-8.0, -19.2, 7.5]; [-0.7071067811865477, -0.7071067811865475]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `channel-01-in` | road / 1 / primary | in | [-8.0, -19.2, 15.0]; [0.7071067811865477, 0.7071067811865475]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `channel-12-out` | road / 1 / primary | out | [-8.0, -12.8, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `channel-02-in` | road / 1 / primary | in | [-8.0, -12.8, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `channel-03-in` | road / 1 / primary | in | [-3.2, -8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `channel-13-out` | road / 1 / primary | out | [-3.2, -8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `channel-04-in` | road / 1 / primary | in | [0.970563, -24.0, 10.06235]; [0.7071067811865476, 0.7071067811865476]; 0.28202968 | `path-interface-e8e293f72dffb05f48c3` |
| `channel-05-in` | road / 1 / primary | in | [3.2, -8.0, 7.5]; [-0.7071067811865477, -0.7071067811865475]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `channel-14-out` | road / 1 / primary | out | [3.2, -8.0, 15.0]; [0.7071067811865477, 0.7071067811865475]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `channel-15-out` | road / 1 / primary | out | [8.0, -16.970563, 12.866039]; [0.7071067811865476, 0.7071067811865476]; 0.282027457 | `path-interface-e2ac8445a31ecbb4b6d6` |
| `channel-16-out` | road / 1 / primary | out | [8.0, -3.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `channel-06-in` | road / 1 / primary | in | [8.0, -3.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `channel-17-out` | road / 1 / primary | out | [8.0, 3.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `channel-07-in` | road / 1 / primary | in | [8.0, 3.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `channel-18-out` | road / 1 / primary | out | [8.0, 6.194881, 7.5]; [-0.9864122952117411, -0.16428872102218395]; 0.0 | `path-interface-0da9b7f162296ea51351` |
| `channel-08-in` | road / 1 / primary | in | [12.8, 8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `channel-19-out` | road / 1 / primary | out | [12.8, 8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `channel-09-in` | road / 1 / primary | in | [16.104467, -8.0, 15.0]; [0.3399082425092716, 0.9404586044447987]; 0.0 | `path-interface-751c8ea9e23ef086a5d5` |
| `channel-10-in` | road / 1 / primary | in | [19.2, 8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `channel-20-out` | road / 1 / primary | out | [19.2, 8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `channel-01-in` → `channel-14-out` | primary |
| road | `channel-02-in` → `channel-13-out` | primary |
| road | `channel-03-in` → `channel-12-out` | primary |
| road | `channel-04-in` → `channel-15-out` | primary |
| road | `channel-05-in` → `channel-11-out` | primary |
| road | `channel-06-in` → `channel-20-out` | primary |
| road | `channel-07-in` → `channel-19-out` | primary |
| road | `channel-08-in` → `channel-18-out` | primary |
| road | `channel-08-in` → `channel-17-out` | primary |
| road | `channel-09-in` → `channel-20-out` | primary |
| road | `channel-10-in` → `channel-16-out` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `channel-01-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-01-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-02-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-03-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-04-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-05-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-06-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-07-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-07-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-07-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-07-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-07-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-07-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-07-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-07-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-07-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-08-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-08-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-08-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-08-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-08-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-08-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-08-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-08-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-09-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-09-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-09-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-09-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-09-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-09-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-09-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-09-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-09-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-10-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-10-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-10-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-10-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-10-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-10-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-10-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-10-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `channel-10-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use Windows SimCity 4 with the pinned NAM 50 right-hand-traffic inputs, including through Wine or CrossOver. The shared [build guide](../../../../docs/BUILD_AND_INSTALL.md) owns private input settings and explicit installation. Use the complete fifteen-component assembly for travel tests: this individual component can expose required route fragments at more than one city-tile edge. A matching-looking isolated end is insufficient to create the whole journey.

Prepare the [assembly's flat reference test area](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#2-test-setup), keep the camera north-up for placement, and use the exact occupied cells **(X8, Y8), (X7, Y7)**. The full core occupies 31 cells inside X1–X8 and Y1–Y8; the preserved drawing reference still shows X0–X9 and Y0–Y9. One tile is 16 m. Additional outside road approaches are separate from that core count.

## 3. Software checks

Run from the repository directory containing `custom-pieces/`. These commands inspect an existing build and its current source-bound connector records; they do not install anything, supply missing inputs, or approve a manual case. An absent or failing report is not a software pass.

```sh
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/ddrhw-parallel-diamond-slip-lanes-02
python3 -B custom-pieces/scp.py connectors check --domain highway --piece ddrhw-parallel-upper-entry-slip --build dist/ddrhw-parallel-diamond-slip-lanes-02
python3 -B custom-pieces/scp.py docs-check --piece ddrhw-parallel-upper-entry-slip
```

The [complete saved-assembly check](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#3-software-checks) checks this component in all fifteen placements, including physical model overhang and the traffic fragments owned by its neighbours. The ordinary build's manifest and verification report identify the actual measured resources. Retain every software failure with its source fingerprint; rerunning a renderer cannot repair it.

The current slip-lane revision changes the highway-shoulder traffic routes and their white markings within the existing construction footprint. Read outward from a through lane toward its ramp: each lower route has an 8 m smooth sideways taper and a 4 m straight shoulder section; each upper route has a 5 m taper and a 1 m straight shoulder section. The lower routes begin 6.788225 m farther upstream in already owned native highway tiles. The upper routes retain their previous outer ports because the unchanged 31-cell layout provides less shoulder distance there. These distances are measured along the straight highway axis. On-ramps follow the same profiles in reverse. The auxiliary-lane centre is 5.5 m from the highway axis; the checked 2.5 m-wide car corridor leaves 0.421875 m to the native barrier foot on the straight section. These are compressed experimental dimensions, not a real-road design standard. Native through PATHs, roadway outside the native 8 m deck edge, grades, ground terminals, permanent identifiers, and construction ownership retain their previous scope. Check the matching saved report before treating this source revision as verified. This component supplies highway or ramp geometry. The three ground components P01, P02, and P03 own the implemented adaptive Avenue pavement and retained pedestrian routes. Connecting this elevated component does not itself select a sidewalk appearance. Read the [actual mechanism and limits](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#3-software-checks).

The earlier narrow ground mouths are retained: each terminal keeps its 6 m grade join, narrows to 3.5 m over 3 m, and stays narrow through its R6 turn and Avenue joining collar. The ramp centreline crosses the retained pedestrian-route centreline 3.258752 m from the grade join, after that 3 m ground taper is complete. The asphalt footprint reaches the pedestrian route earlier, while the ground taper is still narrowing; this is the actual driveway crossing.

## 4. Game checks

Test the new outside native approach separately from the fixed piece: place a fresh copy with clear space beyond its highway end, inspect the native DD tile, and extend an already working NAM DD highway to that outside tile with the RealHighway drawing tool. Repeat all four placement orientations, compare both deck directions, and check Route Query, actual travel, occupied neighbours, demolition, and save/reload separately. The [network specification](../../NETWORK_SPEC.md#12-native-highway-approach-experiment) defines the exact helper coordinates and limits. These native-joining observations remain unverified.

1. Select this exact component through the assembly button, match P07 at **X7, Y8**, and confirm that the occupied preview squares match **(X8, Y8), (X7, Y7)** before clicking.
2. Place the full assembly using the order in its guide. Inspect this component's saved model from both opposing oblique views, and compare its real join with the neighbouring models; look for gaps, blocked barrier openings, misplaced supports, or a sudden pavement-colour patch.
3. Repeat fresh placement in the four distinct proper rotations. Rotate the camera separately after placement, because camera movement and a newly rotated piece test different things.
4. For an adaptive Avenue cell, connect ordinary Avenue outside the core, add nearby development, and compare its pavement variant with the neighbouring Avenue. Connecting the Avenue alone does not select the developed pavement appearance. Inspect both narrow driveway crossings, then check pedestrian Route Query and visible walking separately; a sidewalk image does not create a pedestrian PATH, and the crossing remains road asphalt. For a component without Avenue cells, inspect the neighbouring adaptive owners instead of expecting this piece to change pavement itself.
5. Run every required car and pedestrian journey listed by the exact matrix. Record Route Query and visible travel separately. Also confirm that every declared forbidden transfer stays unavailable; a visually clear road surface is not traffic evidence.
6. Inspect for unwanted cast shadows at Medium and High quality; this component intentionally supplies none. Demolish the component, replace it, save the city, quit completely, and reload. Check that no temporary placement handle or old shadow attachment remains and that the component and its traffic neighbours remain correct.

Record only explicit observations through [the shared observation workflow](../../../../docs/TESTING.md), selecting **ddrhw-parallel-upper-entry-slip** and its exact current cases. No observation of the older adaptive probe, R40 diamond, or another rotation automatically approves this new component.

## 5. Results and known issues

The implementation is experimental. The generated records below are authoritative for the current evidence scope; **all new human game observations remain unverified** until the user confirms their exact cases. In particular, outside native DD RHW connections, over-Avenue placement, Avenue redraw, temporary-handle collision behaviour, pedestrian pavement variants, moving traffic, camera rotations, demolition, and save/reload require game checks.

The whole-cell traffic partition is intentionally different from the physical model split. The revised traffic route and matching white markings use the existing shoulder. Read from the highway through lane toward the ramp: the upper L2 shoulder section has a 5 m smooth sideways taper, followed by 1 m straight and parallel to the highway. An on-ramp follows the reverse sequence in its direction of travel. These two lengths are measured along the straight highway axis and describe the shoulder section, not the complete ramp. The upper route keeps its previous outer traffic port: a longer shoulder treatment would need traffic ownership beyond the retained 31-cell layout. The auxiliary-lane centre is 5.5 m from the highway axis. Its checked 2.5 m-wide car corridor leaves 0.421875 m to the native barrier foot at the straight shoulder section. The two occupied cells lie diagonally inside a sparse 2 × 2 rectangle. Its construction reference is an empty corner, so align both occupied preview cells instead of assuming that the reference position is a third tile. Complete boundary cards include both highway levels and every access fragment; matching only the named ramp is insufficient. This is a limitation to understand when choosing replacement modules, not permission to discard a required boundary service.

Adaptive pavement is implemented through native texture variants and correctly rotating model props, rather than a fixed sidewalk slab. Its visible appearance depends on the native development rules, and a sidewalk replacement mod needs its own compatibility check. The approximately 1.149 m clearance applies where the terminal asphalt and retained pedestrian centreline run beside one another; the actual driveway crossings are deliberately excluded. A measured route clearance does not establish visible walking, a continuous pavement strip, or a particular pedestrian-versus-car priority in the game.

<!-- BEGIN MANUAL SUMMARY -->

### Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/3 applicable cases passed; 0 failed, 0 stale.
- [ ] In-game rendering: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Route Query: 0/44 applicable cases passed; 0 failed, 0 stale.
- [ ] Visible travel: 0/44 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 465, passed: 0, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-parallel-upper-entry-slip/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-parallel-upper-entry-slip/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-5673f882ca9f2be73133">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-5673f882ca9f2be73133"></a>

**General: unverified** — `software_resources-5673f882ca9f2be73133`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-5673f882ca9f2be73133">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-5673f882ca9f2be73133"></a>

**General: unverified** — `software_connectivity-5673f882ca9f2be73133`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-parallel-upper-entry-slip:canonical-southeast | <a href="#case-preview_review-5f5e809102acebe219e2">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-upper-entry-slip:canonical-top | <a href="#case-preview_review-36adab1c9e0adcd7db93">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-upper-entry-slip:connection-overview | <a href="#case-preview_review-1e4c041af0e59716c2cf">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-parallel-upper-entry-slip:canonical-southeast</summary>

<a id="case-preview_review-5f5e809102acebe219e2"></a>

**General: unverified** — `preview_review-5f5e809102acebe219e2`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-parallel-upper-entry-slip:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-upper-entry-slip:canonical-top</summary>

<a id="case-preview_review-36adab1c9e0adcd7db93"></a>

**General: unverified** — `preview_review-36adab1c9e0adcd7db93`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-parallel-upper-entry-slip:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-upper-entry-slip:connection-overview</summary>

<a id="case-preview_review-1e4c041af0e59716c2cf"></a>

**General: unverified** — `preview_review-1e4c041af0e59716c2cf`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-parallel-upper-entry-slip:connection-overview.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-701d53baffa501be3ea7">[ ] unverified</a> | <a href="#case-in_game_render-626c97ef132a7dc1744c">[ ] unverified</a> | <a href="#case-in_game_render-d295f91b3a1986f36401">[ ] unverified</a> | <a href="#case-in_game_render-614b70fde26f7524dabc">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-701d53baffa501be3ea7"></a>

**0° CCW: unverified** — `in_game_render-701d53baffa501be3ea7`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-626c97ef132a7dc1744c"></a>

**90° CCW: unverified** — `in_game_render-626c97ef132a7dc1744c`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-d295f91b3a1986f36401"></a>

**180° CCW: unverified** — `in_game_render-d295f91b3a1986f36401`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-614b70fde26f7524dabc"></a>

**270° CCW: unverified** — `in_game_render-614b70fde26f7524dabc`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-701d53baffa501be3ea7">[ ] unverified</a> | <a href="#case-in_game_placement-626c97ef132a7dc1744c">[ ] unverified</a> | <a href="#case-in_game_placement-d295f91b3a1986f36401">[ ] unverified</a> | <a href="#case-in_game_placement-614b70fde26f7524dabc">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-701d53baffa501be3ea7"></a>

**0° CCW: unverified** — `in_game_placement-701d53baffa501be3ea7`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-626c97ef132a7dc1744c"></a>

**90° CCW: unverified** — `in_game_placement-626c97ef132a7dc1744c`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-d295f91b3a1986f36401"></a>

**180° CCW: unverified** — `in_game_placement-d295f91b3a1986f36401`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-614b70fde26f7524dabc"></a>

**270° CCW: unverified** — `in_game_placement-614b70fde26f7524dabc`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-701d53baffa501be3ea7">[ ] unverified</a> | <a href="#case-in_game_demolition-626c97ef132a7dc1744c">[ ] unverified</a> | <a href="#case-in_game_demolition-d295f91b3a1986f36401">[ ] unverified</a> | <a href="#case-in_game_demolition-614b70fde26f7524dabc">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-701d53baffa501be3ea7"></a>

**0° CCW: unverified** — `in_game_demolition-701d53baffa501be3ea7`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-626c97ef132a7dc1744c"></a>

**90° CCW: unverified** — `in_game_demolition-626c97ef132a7dc1744c`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-d295f91b3a1986f36401"></a>

**180° CCW: unverified** — `in_game_demolition-d295f91b3a1986f36401`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-614b70fde26f7524dabc"></a>

**270° CCW: unverified** — `in_game_demolition-614b70fde26f7524dabc`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-701d53baffa501be3ea7">[ ] unverified</a> | <a href="#case-in_game_save_reload-626c97ef132a7dc1744c">[ ] unverified</a> | <a href="#case-in_game_save_reload-d295f91b3a1986f36401">[ ] unverified</a> | <a href="#case-in_game_save_reload-614b70fde26f7524dabc">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-701d53baffa501be3ea7"></a>

**0° CCW: unverified** — `in_game_save_reload-701d53baffa501be3ea7`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-626c97ef132a7dc1744c"></a>

**90° CCW: unverified** — `in_game_save_reload-626c97ef132a7dc1744c`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-d295f91b3a1986f36401"></a>

**180° CCW: unverified** — `in_game_save_reload-d295f91b3a1986f36401`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-614b70fde26f7524dabc"></a>

**270° CCW: unverified** — `in_game_save_reload-614b70fde26f7524dabc`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 44 cases; unverified: 44</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out | — | <a href="#case-in_game_route_query-be6cbbd827eb607ca9f7">[ ] unverified</a> | <a href="#case-in_game_route_query-d058e534eaefb6a76ace">[ ] unverified</a> | <a href="#case-in_game_route_query-d8611410d71ed63607c9">[ ] unverified</a> | <a href="#case-in_game_route_query-4a1642e029475913d982">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-13-out; entry: channel-02-in; exit: channel-13-out | — | <a href="#case-in_game_route_query-9d23535fe72ba9801464">[ ] unverified</a> | <a href="#case-in_game_route_query-b876243ac5f1ec723f56">[ ] unverified</a> | <a href="#case-in_game_route_query-d4657ddf1cad1feeb1da">[ ] unverified</a> | <a href="#case-in_game_route_query-6f19e889be2561c012c0">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-12-out; entry: channel-03-in; exit: channel-12-out | — | <a href="#case-in_game_route_query-d8ca1775df84aa31f076">[ ] unverified</a> | <a href="#case-in_game_route_query-7bd26dd2d9452d0d60c5">[ ] unverified</a> | <a href="#case-in_game_route_query-dafe4330dddbe04dda2b">[ ] unverified</a> | <a href="#case-in_game_route_query-dedd3e2092d0046f819e">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-15-out; entry: channel-04-in; exit: channel-15-out | — | <a href="#case-in_game_route_query-4ae3f55d9291f755c75f">[ ] unverified</a> | <a href="#case-in_game_route_query-5ab3b609ed7d0c2c1ac8">[ ] unverified</a> | <a href="#case-in_game_route_query-b88c9d6e5d2bf856772e">[ ] unverified</a> | <a href="#case-in_game_route_query-433531945677c900529a">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out | — | <a href="#case-in_game_route_query-ab9c989a6e29c87b252b">[ ] unverified</a> | <a href="#case-in_game_route_query-584f1110f6a50c753f22">[ ] unverified</a> | <a href="#case-in_game_route_query-dd2d8e4b701b7f247bec">[ ] unverified</a> | <a href="#case-in_game_route_query-18ac65a9cf1a7dce125c">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-06-in>channel-20-out; entry: channel-06-in; exit: channel-20-out | — | <a href="#case-in_game_route_query-2685f065254bb9abb247">[ ] unverified</a> | <a href="#case-in_game_route_query-7cf19625f3590d2fd79e">[ ] unverified</a> | <a href="#case-in_game_route_query-17d72a3a06a18efd3434">[ ] unverified</a> | <a href="#case-in_game_route_query-9e0f96a45c503f042071">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-07-in>channel-19-out; entry: channel-07-in; exit: channel-19-out | — | <a href="#case-in_game_route_query-1e98f1a507a388fff896">[ ] unverified</a> | <a href="#case-in_game_route_query-7933309aee07f5eeb72c">[ ] unverified</a> | <a href="#case-in_game_route_query-273010c511a7fdbf9e32">[ ] unverified</a> | <a href="#case-in_game_route_query-f0181eee828973464840">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out | — | <a href="#case-in_game_route_query-618133673926bb261bc2">[ ] unverified</a> | <a href="#case-in_game_route_query-eca36e1b5402e47a388a">[ ] unverified</a> | <a href="#case-in_game_route_query-dd040f71054cef9a3d0b">[ ] unverified</a> | <a href="#case-in_game_route_query-098ce0ae9dea84b2d2f2">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out | — | <a href="#case-in_game_route_query-1ee09d8832a4d037fee3">[ ] unverified</a> | <a href="#case-in_game_route_query-96f2293636c53d85a171">[ ] unverified</a> | <a href="#case-in_game_route_query-6f09baf98a4acdf19f85">[ ] unverified</a> | <a href="#case-in_game_route_query-fb76e66f60429ccca46c">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-09-in>channel-20-out; entry: channel-09-in; exit: channel-20-out | — | <a href="#case-in_game_route_query-bd924e97601e13226f4a">[ ] unverified</a> | <a href="#case-in_game_route_query-8d712bb9e07c9c290a6e">[ ] unverified</a> | <a href="#case-in_game_route_query-9c9812fdc10b0d04173b">[ ] unverified</a> | <a href="#case-in_game_route_query-bec89bf5d39226f7de65">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out | — | <a href="#case-in_game_route_query-d20c322fa31793aee640">[ ] unverified</a> | <a href="#case-in_game_route_query-324b46dac9b7ee84b95f">[ ] unverified</a> | <a href="#case-in_game_route_query-c3cba5b9eb5b8078ff2f">[ ] unverified</a> | <a href="#case-in_game_route_query-ff130e311f01ab765527">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out</summary>

<a id="case-in_game_route_query-be6cbbd827eb607ca9f7"></a>

**0° CCW: unverified** — `in_game_route_query-be6cbbd827eb607ca9f7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_route_query-d058e534eaefb6a76ace"></a>

**90° CCW: unverified** — `in_game_route_query-d058e534eaefb6a76ace`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_route_query-d8611410d71ed63607c9"></a>

**180° CCW: unverified** — `in_game_route_query-d8611410d71ed63607c9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_route_query-4a1642e029475913d982"></a>

**270° CCW: unverified** — `in_game_route_query-4a1642e029475913d982`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-02-in>channel-13-out; entry: channel-02-in; exit: channel-13-out</summary>

<a id="case-in_game_route_query-9d23535fe72ba9801464"></a>

**0° CCW: unverified** — `in_game_route_query-9d23535fe72ba9801464`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-13-out; entry: channel-02-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_route_query-b876243ac5f1ec723f56"></a>

**90° CCW: unverified** — `in_game_route_query-b876243ac5f1ec723f56`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-13-out; entry: channel-02-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_route_query-d4657ddf1cad1feeb1da"></a>

**180° CCW: unverified** — `in_game_route_query-d4657ddf1cad1feeb1da`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-13-out; entry: channel-02-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_route_query-6f19e889be2561c012c0"></a>

**270° CCW: unverified** — `in_game_route_query-6f19e889be2561c012c0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-13-out; entry: channel-02-in; exit: channel-13-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-03-in>channel-12-out; entry: channel-03-in; exit: channel-12-out</summary>

<a id="case-in_game_route_query-d8ca1775df84aa31f076"></a>

**0° CCW: unverified** — `in_game_route_query-d8ca1775df84aa31f076`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-12-out; entry: channel-03-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_route_query-7bd26dd2d9452d0d60c5"></a>

**90° CCW: unverified** — `in_game_route_query-7bd26dd2d9452d0d60c5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-12-out; entry: channel-03-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_route_query-dafe4330dddbe04dda2b"></a>

**180° CCW: unverified** — `in_game_route_query-dafe4330dddbe04dda2b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-12-out; entry: channel-03-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_route_query-dedd3e2092d0046f819e"></a>

**270° CCW: unverified** — `in_game_route_query-dedd3e2092d0046f819e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-12-out; entry: channel-03-in; exit: channel-12-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-04-in>channel-15-out; entry: channel-04-in; exit: channel-15-out</summary>

<a id="case-in_game_route_query-4ae3f55d9291f755c75f"></a>

**0° CCW: unverified** — `in_game_route_query-4ae3f55d9291f755c75f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-15-out; entry: channel-04-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_route_query-5ab3b609ed7d0c2c1ac8"></a>

**90° CCW: unverified** — `in_game_route_query-5ab3b609ed7d0c2c1ac8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-15-out; entry: channel-04-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_route_query-b88c9d6e5d2bf856772e"></a>

**180° CCW: unverified** — `in_game_route_query-b88c9d6e5d2bf856772e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-15-out; entry: channel-04-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_route_query-433531945677c900529a"></a>

**270° CCW: unverified** — `in_game_route_query-433531945677c900529a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-15-out; entry: channel-04-in; exit: channel-15-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out</summary>

<a id="case-in_game_route_query-ab9c989a6e29c87b252b"></a>

**0° CCW: unverified** — `in_game_route_query-ab9c989a6e29c87b252b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_route_query-584f1110f6a50c753f22"></a>

**90° CCW: unverified** — `in_game_route_query-584f1110f6a50c753f22`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_route_query-dd2d8e4b701b7f247bec"></a>

**180° CCW: unverified** — `in_game_route_query-dd2d8e4b701b7f247bec`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_route_query-18ac65a9cf1a7dce125c"></a>

**270° CCW: unverified** — `in_game_route_query-18ac65a9cf1a7dce125c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-06-in>channel-20-out; entry: channel-06-in; exit: channel-20-out</summary>

<a id="case-in_game_route_query-2685f065254bb9abb247"></a>

**0° CCW: unverified** — `in_game_route_query-2685f065254bb9abb247`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-20-out; entry: channel-06-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_route_query-7cf19625f3590d2fd79e"></a>

**90° CCW: unverified** — `in_game_route_query-7cf19625f3590d2fd79e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-20-out; entry: channel-06-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_route_query-17d72a3a06a18efd3434"></a>

**180° CCW: unverified** — `in_game_route_query-17d72a3a06a18efd3434`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-20-out; entry: channel-06-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_route_query-9e0f96a45c503f042071"></a>

**270° CCW: unverified** — `in_game_route_query-9e0f96a45c503f042071`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-20-out; entry: channel-06-in; exit: channel-20-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-07-in>channel-19-out; entry: channel-07-in; exit: channel-19-out</summary>

<a id="case-in_game_route_query-1e98f1a507a388fff896"></a>

**0° CCW: unverified** — `in_game_route_query-1e98f1a507a388fff896`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-19-out; entry: channel-07-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_route_query-7933309aee07f5eeb72c"></a>

**90° CCW: unverified** — `in_game_route_query-7933309aee07f5eeb72c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-19-out; entry: channel-07-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_route_query-273010c511a7fdbf9e32"></a>

**180° CCW: unverified** — `in_game_route_query-273010c511a7fdbf9e32`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-19-out; entry: channel-07-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_route_query-f0181eee828973464840"></a>

**270° CCW: unverified** — `in_game_route_query-f0181eee828973464840`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-19-out; entry: channel-07-in; exit: channel-19-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out</summary>

<a id="case-in_game_route_query-618133673926bb261bc2"></a>

**0° CCW: unverified** — `in_game_route_query-618133673926bb261bc2`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_route_query-eca36e1b5402e47a388a"></a>

**90° CCW: unverified** — `in_game_route_query-eca36e1b5402e47a388a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_route_query-dd040f71054cef9a3d0b"></a>

**180° CCW: unverified** — `in_game_route_query-dd040f71054cef9a3d0b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_route_query-098ce0ae9dea84b2d2f2"></a>

**270° CCW: unverified** — `in_game_route_query-098ce0ae9dea84b2d2f2`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out</summary>

<a id="case-in_game_route_query-1ee09d8832a4d037fee3"></a>

**0° CCW: unverified** — `in_game_route_query-1ee09d8832a4d037fee3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_route_query-96f2293636c53d85a171"></a>

**90° CCW: unverified** — `in_game_route_query-96f2293636c53d85a171`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_route_query-6f09baf98a4acdf19f85"></a>

**180° CCW: unverified** — `in_game_route_query-6f09baf98a4acdf19f85`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_route_query-fb76e66f60429ccca46c"></a>

**270° CCW: unverified** — `in_game_route_query-fb76e66f60429ccca46c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-09-in>channel-20-out; entry: channel-09-in; exit: channel-20-out</summary>

<a id="case-in_game_route_query-bd924e97601e13226f4a"></a>

**0° CCW: unverified** — `in_game_route_query-bd924e97601e13226f4a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-20-out; entry: channel-09-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_route_query-8d712bb9e07c9c290a6e"></a>

**90° CCW: unverified** — `in_game_route_query-8d712bb9e07c9c290a6e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-20-out; entry: channel-09-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_route_query-9c9812fdc10b0d04173b"></a>

**180° CCW: unverified** — `in_game_route_query-9c9812fdc10b0d04173b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-20-out; entry: channel-09-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_route_query-bec89bf5d39226f7de65"></a>

**270° CCW: unverified** — `in_game_route_query-bec89bf5d39226f7de65`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-20-out; entry: channel-09-in; exit: channel-20-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out</summary>

<a id="case-in_game_route_query-d20c322fa31793aee640"></a>

**0° CCW: unverified** — `in_game_route_query-d20c322fa31793aee640`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_route_query-324b46dac9b7ee84b95f"></a>

**90° CCW: unverified** — `in_game_route_query-324b46dac9b7ee84b95f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_route_query-c3cba5b9eb5b8078ff2f"></a>

**180° CCW: unverified** — `in_game_route_query-c3cba5b9eb5b8078ff2f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_route_query-ff130e311f01ab765527"></a>

**270° CCW: unverified** — `in_game_route_query-ff130e311f01ab765527`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 44 cases; unverified: 44</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out | — | <a href="#case-in_game_visible_travel-be6cbbd827eb607ca9f7">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d058e534eaefb6a76ace">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d8611410d71ed63607c9">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4a1642e029475913d982">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-13-out; entry: channel-02-in; exit: channel-13-out | — | <a href="#case-in_game_visible_travel-9d23535fe72ba9801464">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b876243ac5f1ec723f56">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d4657ddf1cad1feeb1da">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6f19e889be2561c012c0">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-12-out; entry: channel-03-in; exit: channel-12-out | — | <a href="#case-in_game_visible_travel-d8ca1775df84aa31f076">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7bd26dd2d9452d0d60c5">[ ] unverified</a> | <a href="#case-in_game_visible_travel-dafe4330dddbe04dda2b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-dedd3e2092d0046f819e">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-15-out; entry: channel-04-in; exit: channel-15-out | — | <a href="#case-in_game_visible_travel-4ae3f55d9291f755c75f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5ab3b609ed7d0c2c1ac8">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b88c9d6e5d2bf856772e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-433531945677c900529a">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out | — | <a href="#case-in_game_visible_travel-ab9c989a6e29c87b252b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-584f1110f6a50c753f22">[ ] unverified</a> | <a href="#case-in_game_visible_travel-dd2d8e4b701b7f247bec">[ ] unverified</a> | <a href="#case-in_game_visible_travel-18ac65a9cf1a7dce125c">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-06-in>channel-20-out; entry: channel-06-in; exit: channel-20-out | — | <a href="#case-in_game_visible_travel-2685f065254bb9abb247">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7cf19625f3590d2fd79e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-17d72a3a06a18efd3434">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9e0f96a45c503f042071">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-07-in>channel-19-out; entry: channel-07-in; exit: channel-19-out | — | <a href="#case-in_game_visible_travel-1e98f1a507a388fff896">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7933309aee07f5eeb72c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-273010c511a7fdbf9e32">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f0181eee828973464840">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out | — | <a href="#case-in_game_visible_travel-618133673926bb261bc2">[ ] unverified</a> | <a href="#case-in_game_visible_travel-eca36e1b5402e47a388a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-dd040f71054cef9a3d0b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-098ce0ae9dea84b2d2f2">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out | — | <a href="#case-in_game_visible_travel-1ee09d8832a4d037fee3">[ ] unverified</a> | <a href="#case-in_game_visible_travel-96f2293636c53d85a171">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6f09baf98a4acdf19f85">[ ] unverified</a> | <a href="#case-in_game_visible_travel-fb76e66f60429ccca46c">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-09-in>channel-20-out; entry: channel-09-in; exit: channel-20-out | — | <a href="#case-in_game_visible_travel-bd924e97601e13226f4a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8d712bb9e07c9c290a6e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9c9812fdc10b0d04173b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-bec89bf5d39226f7de65">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out | — | <a href="#case-in_game_visible_travel-d20c322fa31793aee640">[ ] unverified</a> | <a href="#case-in_game_visible_travel-324b46dac9b7ee84b95f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c3cba5b9eb5b8078ff2f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ff130e311f01ab765527">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out</summary>

<a id="case-in_game_visible_travel-be6cbbd827eb607ca9f7"></a>

**0° CCW: unverified** — `in_game_visible_travel-be6cbbd827eb607ca9f7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_visible_travel-d058e534eaefb6a76ace"></a>

**90° CCW: unverified** — `in_game_visible_travel-d058e534eaefb6a76ace`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_visible_travel-d8611410d71ed63607c9"></a>

**180° CCW: unverified** — `in_game_visible_travel-d8611410d71ed63607c9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_visible_travel-4a1642e029475913d982"></a>

**270° CCW: unverified** — `in_game_visible_travel-4a1642e029475913d982`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-02-in>channel-13-out; entry: channel-02-in; exit: channel-13-out</summary>

<a id="case-in_game_visible_travel-9d23535fe72ba9801464"></a>

**0° CCW: unverified** — `in_game_visible_travel-9d23535fe72ba9801464`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-13-out; entry: channel-02-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_visible_travel-b876243ac5f1ec723f56"></a>

**90° CCW: unverified** — `in_game_visible_travel-b876243ac5f1ec723f56`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-13-out; entry: channel-02-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_visible_travel-d4657ddf1cad1feeb1da"></a>

**180° CCW: unverified** — `in_game_visible_travel-d4657ddf1cad1feeb1da`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-13-out; entry: channel-02-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_visible_travel-6f19e889be2561c012c0"></a>

**270° CCW: unverified** — `in_game_visible_travel-6f19e889be2561c012c0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-13-out; entry: channel-02-in; exit: channel-13-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-03-in>channel-12-out; entry: channel-03-in; exit: channel-12-out</summary>

<a id="case-in_game_visible_travel-d8ca1775df84aa31f076"></a>

**0° CCW: unverified** — `in_game_visible_travel-d8ca1775df84aa31f076`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-12-out; entry: channel-03-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_visible_travel-7bd26dd2d9452d0d60c5"></a>

**90° CCW: unverified** — `in_game_visible_travel-7bd26dd2d9452d0d60c5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-12-out; entry: channel-03-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_visible_travel-dafe4330dddbe04dda2b"></a>

**180° CCW: unverified** — `in_game_visible_travel-dafe4330dddbe04dda2b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-12-out; entry: channel-03-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_visible_travel-dedd3e2092d0046f819e"></a>

**270° CCW: unverified** — `in_game_visible_travel-dedd3e2092d0046f819e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-12-out; entry: channel-03-in; exit: channel-12-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-04-in>channel-15-out; entry: channel-04-in; exit: channel-15-out</summary>

<a id="case-in_game_visible_travel-4ae3f55d9291f755c75f"></a>

**0° CCW: unverified** — `in_game_visible_travel-4ae3f55d9291f755c75f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-15-out; entry: channel-04-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_visible_travel-5ab3b609ed7d0c2c1ac8"></a>

**90° CCW: unverified** — `in_game_visible_travel-5ab3b609ed7d0c2c1ac8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-15-out; entry: channel-04-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_visible_travel-b88c9d6e5d2bf856772e"></a>

**180° CCW: unverified** — `in_game_visible_travel-b88c9d6e5d2bf856772e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-15-out; entry: channel-04-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_visible_travel-433531945677c900529a"></a>

**270° CCW: unverified** — `in_game_visible_travel-433531945677c900529a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-15-out; entry: channel-04-in; exit: channel-15-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out</summary>

<a id="case-in_game_visible_travel-ab9c989a6e29c87b252b"></a>

**0° CCW: unverified** — `in_game_visible_travel-ab9c989a6e29c87b252b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_visible_travel-584f1110f6a50c753f22"></a>

**90° CCW: unverified** — `in_game_visible_travel-584f1110f6a50c753f22`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_visible_travel-dd2d8e4b701b7f247bec"></a>

**180° CCW: unverified** — `in_game_visible_travel-dd2d8e4b701b7f247bec`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_visible_travel-18ac65a9cf1a7dce125c"></a>

**270° CCW: unverified** — `in_game_visible_travel-18ac65a9cf1a7dce125c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-06-in>channel-20-out; entry: channel-06-in; exit: channel-20-out</summary>

<a id="case-in_game_visible_travel-2685f065254bb9abb247"></a>

**0° CCW: unverified** — `in_game_visible_travel-2685f065254bb9abb247`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-20-out; entry: channel-06-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_visible_travel-7cf19625f3590d2fd79e"></a>

**90° CCW: unverified** — `in_game_visible_travel-7cf19625f3590d2fd79e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-20-out; entry: channel-06-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_visible_travel-17d72a3a06a18efd3434"></a>

**180° CCW: unverified** — `in_game_visible_travel-17d72a3a06a18efd3434`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-20-out; entry: channel-06-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_visible_travel-9e0f96a45c503f042071"></a>

**270° CCW: unverified** — `in_game_visible_travel-9e0f96a45c503f042071`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-20-out; entry: channel-06-in; exit: channel-20-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-07-in>channel-19-out; entry: channel-07-in; exit: channel-19-out</summary>

<a id="case-in_game_visible_travel-1e98f1a507a388fff896"></a>

**0° CCW: unverified** — `in_game_visible_travel-1e98f1a507a388fff896`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-19-out; entry: channel-07-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_visible_travel-7933309aee07f5eeb72c"></a>

**90° CCW: unverified** — `in_game_visible_travel-7933309aee07f5eeb72c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-19-out; entry: channel-07-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_visible_travel-273010c511a7fdbf9e32"></a>

**180° CCW: unverified** — `in_game_visible_travel-273010c511a7fdbf9e32`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-19-out; entry: channel-07-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_visible_travel-f0181eee828973464840"></a>

**270° CCW: unverified** — `in_game_visible_travel-f0181eee828973464840`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-19-out; entry: channel-07-in; exit: channel-19-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out</summary>

<a id="case-in_game_visible_travel-618133673926bb261bc2"></a>

**0° CCW: unverified** — `in_game_visible_travel-618133673926bb261bc2`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_visible_travel-eca36e1b5402e47a388a"></a>

**90° CCW: unverified** — `in_game_visible_travel-eca36e1b5402e47a388a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_visible_travel-dd040f71054cef9a3d0b"></a>

**180° CCW: unverified** — `in_game_visible_travel-dd040f71054cef9a3d0b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_visible_travel-098ce0ae9dea84b2d2f2"></a>

**270° CCW: unverified** — `in_game_visible_travel-098ce0ae9dea84b2d2f2`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out</summary>

<a id="case-in_game_visible_travel-1ee09d8832a4d037fee3"></a>

**0° CCW: unverified** — `in_game_visible_travel-1ee09d8832a4d037fee3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_visible_travel-96f2293636c53d85a171"></a>

**90° CCW: unverified** — `in_game_visible_travel-96f2293636c53d85a171`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_visible_travel-6f09baf98a4acdf19f85"></a>

**180° CCW: unverified** — `in_game_visible_travel-6f09baf98a4acdf19f85`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_visible_travel-fb76e66f60429ccca46c"></a>

**270° CCW: unverified** — `in_game_visible_travel-fb76e66f60429ccca46c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-09-in>channel-20-out; entry: channel-09-in; exit: channel-20-out</summary>

<a id="case-in_game_visible_travel-bd924e97601e13226f4a"></a>

**0° CCW: unverified** — `in_game_visible_travel-bd924e97601e13226f4a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-20-out; entry: channel-09-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_visible_travel-8d712bb9e07c9c290a6e"></a>

**90° CCW: unverified** — `in_game_visible_travel-8d712bb9e07c9c290a6e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-20-out; entry: channel-09-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_visible_travel-9c9812fdc10b0d04173b"></a>

**180° CCW: unverified** — `in_game_visible_travel-9c9812fdc10b0d04173b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-20-out; entry: channel-09-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_visible_travel-bec89bf5d39226f7de65"></a>

**270° CCW: unverified** — `in_game_visible_travel-bec89bf5d39226f7de65`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-20-out; entry: channel-09-in; exit: channel-20-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out</summary>

<a id="case-in_game_visible_travel-d20c322fa31793aee640"></a>

**0° CCW: unverified** — `in_game_visible_travel-d20c322fa31793aee640`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_visible_travel-324b46dac9b7ee84b95f"></a>

**90° CCW: unverified** — `in_game_visible_travel-324b46dac9b7ee84b95f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_visible_travel-c3cba5b9eb5b8078ff2f"></a>

**180° CCW: unverified** — `in_game_visible_travel-c3cba5b9eb5b8078ff2f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_visible_travel-ff130e311f01ab765527"></a>

**270° CCW: unverified** — `in_game_visible_travel-ff130e311f01ab765527`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 356 cases; unverified: 356</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a851c802d697803e8f52">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-22c9a86ab196f9a98bb3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3ebb6d01caa212d82ff8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-84f076b635ebf6d3197a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-278a1a7d7ea29b7fc590">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-657a8d2bf5e2b1c876d1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-37e20776b99b8cdb02c8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7e6a17166b56df00cd18">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-54cedfc0491e8bf01523">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8e2af58d2091bae38866">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f525ffc5790e1a26e8a1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b0a56660ae7b46f02818">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0b0d7435c9b247d5258e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a5a463b91d18b0823fdb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cecd8cc8abf99a48df66">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fdcd5411b5903394e8a8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-353113ad73bc771ca613">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cce37d1a2ac268da80b6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-570d3da901817621725a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-83b26acee0ffeb465bda">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0a991cb9efd224d16fe9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9d673ef43266b336ce15">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-16fac59b51e3b7d77c4e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-23f0f21f36593f22ffda">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f339070d8d10d79f9d15">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e2bcbd98f62a53f50d08">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e05d058fb18fbcd7d2d9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6ba71eb2b9a2f2a86011">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e9aebc8c77bf16e727a4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7cc6a0211ea74c4cf2d9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-042aa39ae82630df05cb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-83a7788a473ca08311f2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8acba46a3a4f31599208">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2df44b940b7984b79333">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d73563a0e689a8ca1e95">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e946be095ae31d50e502">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bdc8ae1bf952fb32e71b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-05c8cbae2fa1f8f0c038">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-696ab655e368c0b5c3dc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f673698a048db4300afd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e4bdc17c821873b68230">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6764ff2a8b0ce3a61500">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-17054e53ae61906fd9b7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b09aef0ac82b8f065dc3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c9ffeec9714e63b644b5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7f406ba40d152914dfdb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c0a9334d77f60a426a73">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-86b4c041a0d58611e779">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-94dae94e21ba9ae287c2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f1f0098e7de228fecb68">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-28316efa2db088746dc9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-56cc2be357a362b7d315">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7b3437f96aa06c16c1bd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b69752f5e1f4ca78b783">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c23f7e443b9a004bafea">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-00984e3d5fb6a4b09c05">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-35ada28323ec7eabaaf3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-81a940766aa1c9844b1e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-67bf0b11e238c8b8b6bf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-abb3dddffa06f3cb0505">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4bbe0e6c9d6b4673e106">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-38f9864409bb2e37a7fa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d3eced1af186088bda7e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3e8de7a4be542baab864">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-499c96d5f2b7aa057ed7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-805dc525660e91ab059b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a8d3295a97bb8ec7d368">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4bf0dada2ebb78a55ae2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a018e2a4cc0d2d46e0d6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-056f85c8d0414345af91">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-01aedb06f2c56e0dbe98">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f408be755fe87f4b1200">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a8c08d2be42e5261f728">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e1008c0799d8897e626a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-689da73c4b5cbb8e4cc1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f897d16977e17bac76cb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-09ed927ec4efd95f9aa4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1463563c9072e2587b1f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2b8de842d6719c8b0353">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b8b698e2a7781e700d92">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0a6674f457cf4923ddfa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1d2d0db1c3345c316a89">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cfe5434cd9a7465da9c6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-34204e9a5c35381fa23f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7fc3bf4b8b5b2d8a1f13">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-48c4b4fa5a3a0bff5751">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-05d2a5b7d17f35484c04">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-90aa41165c2de67beac8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4bd4f56aed7b3fab0fcd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-35f1a96cb51f23d9aad0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-822bcb2703b2c36ded28">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-26b824baab87a0559aed">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3df106344513829b9d92">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-98a287286045cf7133d6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-995b713069b0df338bc9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a1ef7badb0fb8359967b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-08911640c7763ac13a3d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-16a3135c34335fc923ff">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7f4439cc3a6d3ef6352e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fe1c0bd3d82f4e154551">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0c60924f3a56e7b6e6d1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-169fae5717da7927b8d4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-676649e5e18df29b4452">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e28a6a62ee9de556334f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f9a48f55b21bca9ffd46">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-65f6e98dd6fdc85211be">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-50ab05d4e3ca9f2e0b57">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-29401d9a790a07b89324">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1baab1807a609ca8c322">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-874ef77133842089c7f4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ed4685a540bfbdf6f374">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bee7bebf4fa42022f96a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c3ab6fac8c86e4c02d82">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-83ad40ad4f966852624c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4ef37c63e2a1cea8a891">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0ed3f9b7e4c00d68958b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1372d73ea4cd9aeb7d9e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-80daeea2d7e41310083e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b39769db66a8bb58a64c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f4657ec02387c2bdbc2c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f75a1e99a1395a8fce88">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-35fc1c9898d5abc14310">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-28704fc6676ec435731d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-328abd19fbf83fa284f7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6055562585bf76898046">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dd0489d07fd45927b0cd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-83ae8f060c039719308f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e9747451b9ebeb28665d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-868018f7bdb64f5a94ee">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e5aab89c59c82339a9ca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d5f5b7c35ea3598c90ce">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-08b2301669bd98a25f57">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2547aad666e7278304ac">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7553ef0701daa094f59b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-43d92c33f5ee4f2e0414">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c57b455e148c00631c3e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-669b77de64df70971b37">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3fcae206b05eb700c5a1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-622228507025ac598f3c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ad8b8f0f1a2503bbd431">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-09bcae19c968ffac789f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fb880b921d88ae0445dd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-63e0efef0062eb4aad76">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3a840863fd260d1c7851">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0e3085cc3b1cfecd18fb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3f9d3bcd2e9576ecceda">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-40e15bcd229cd601340f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9910f7367611bda85652">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6d3edd6f86972197920b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3ca29ac96533419b8178">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7ca2212d79d9faa1270e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c7b6b3f69bc2f21475c3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fec1d13caa8b9483e2c4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-85316b17f8e464abb8e9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dc685732ea2417d3ead8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-de54372c2a19b08cce51">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3dc2ab0a1da2a4414afa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bbee66ca79c0aa28134f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-13104b3f09047bff7e81">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c2953c3987b15b482ebb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fc2fd7d64e1d5f60cd4d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f540d20fd6dbf746e491">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e973af35260024066385">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9f7d5c26930a7448c27c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8dccd871afbef6b9325a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-def19d2a2e93556aecbc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-690953f7d38291acec40">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ccbc3c8f1474f98475b9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-394b11469ddd61e23120">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ade111552e01d5886a4f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6b1d7da96a4ab068e2dc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-adeaf591690e0d767337">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-96e9d13c96dbf9ca7aca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-72d11c90e933dc71c9db">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-efc1a8914643b73cedbc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e61dd1f901630e02623b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-93ef4c25495dc876780a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b3dd23ae5ee83a725af6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-504f70a5795d3fb23ec8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-08520efb904262e3b5f8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-eab2d1c1308ea80eda63">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-74b61a5198e8a8cd3801">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-63e7e9baa5ec16867ce3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-49e52a88a99f69e1b292">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-843168188006ea40ff32">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bd7428b71a92379007b9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-070fe4309a5a5db0f134">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8bdb46296dc54ff14455">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0e7ada239c2718768bb4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-42dc9aa44e9e89d55281">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-54b2be6e9c4e590ce5d7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-572c7cded49252e45fd8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8baf50dcd58e781c2d12">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2fd5aacd07e7305074ea">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-10bb4505e52163d67f52">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fe4aae8492ec0e376a88">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0e1b9411d189c4bf7190">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f3676e44be093036ac7f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f8a231b06c3b5be543ea">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-59fa887559689aa418a9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-eba8384ac8ec3de29938">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e614fd873bb51401a143">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a1e958e66878b4f98b92">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c433a894319125d16c66">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-afc9dae213597ff4050a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f42c76dc599d7bd89aa3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0e9fcf6d55b198be9381">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eb6871a2e4e6ec85304f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b69c31de727cbcc10695">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8fbb82c3037b297f938e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-158cfc2c1a071186839d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9e30432f56a0d6ab69dd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c5d9e3396975d05d6ceb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-611cdeb4c85b8812b125">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b314a1667862f6ef518b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-22709fe71a6efe2180d8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b610c9dbeaef591ba59f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bdda2dd085828d12f565">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c310d698843acaeb3709">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-83595e2a73d720bdbc73">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6db24bcb7ae38afbc505">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c51c1ce37d6b74976b64">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-74792c43df5dfebd4fee">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-127dc7890296811176b7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ca5d5bfe1bb4017b058e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8d405ce35f41b17cabee">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a03c485c3fb509cd74e2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e5d5be100fa8905ad383">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-93f18b557b2791d3efb1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fcb617e49a8fe6e7dff5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6ef977616b9d06f21df7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8837e796d04fdc171308">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ab315a9ad6ff03692069">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d0ef9b9ba84e3fd11ff7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cdbff4ecdfd3258a5150">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8d8dc5bde7f40a13d9e4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ec14a59f6bff2c2679d4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-63cd521f34f0b7609bde">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-296dc9f0aabc8de356f6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f21ba81d1807cf4a2c97">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6d5320f1b194c082112b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-691625c5920d4510a0bc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3fdc4b38270b42dec556">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c3f1f20caef83b05cf0e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-56d893e8d11011cefb71">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d2aabbdc7e199dc2763e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eb950a966f23664ab928">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-029e2df8fddc3486cde8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-11b822e2d01901925581">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c4b89c7909aa57071562">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e5092a1232b9088833bd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fbdbba089c43a0dcaa03">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d52043b513fa627771f9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cbe506411bfbd42d1a93">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fca72824c01be7e8fc68">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6cd380b3c2be3d22b36d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-620bb69800dd7c6284c5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3d7218324d88e465d773">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3c6562765880dd9d3f47">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-abda45bbfe0123b86432">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-647d80f351975b465d92">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3ee74b5e1cb555bbabcf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fdfea3bf0f5b8e470ffe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-717a338f041ea29ff499">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f7cf7efafa9fe6b49825">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-35450065c958ef03af01">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8136a66eda72bffbb4ed">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-caac1fc24124cf9332e2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-124bb87469e05a60bba3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c8beb54fcd4601f11fe6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-591f2b5fe8b337e0f009">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c7e0a148fab8c6bf6abd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bc5708b5c29b2ff65209">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3eb9077b057e96ad0c76">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8dadee0f7cdf3b1b658f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-88764060a9532a3322cc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ad58650ba559bb2c76af">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-579c86c6d932b79d2ddc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e3a7d061c0b6a3e64873">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5ef2a1edf7990af9bd37">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-173322082c578b53d843">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3ff4226c14eb4e0aaf5c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a99ab0b823b0589d9d0d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-af52dc6ae25ba0967917">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ba8b9a8938946522199f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-230eab31be4c1fb71980">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7b921b0e7a9f880c20a5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e74015cfd6ed48b6694a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6b3d2f50960e4567ebae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4a52320c4370567e0d1a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ed225a42839ad4503921">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d967974de7e63e20ddb5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fe0edd54bc3bbd776bbc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b1c2a3b147cd9cb3a0bf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3a7df544bec6767f5199">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-52ab4b89fb57ca1025c8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e4760cbfab8b9091fc98">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b3cd80ef8a76160d7aa6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4120d125fe91fc2b0fed">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b07855d6c42e4e5da065">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6a4db7bc776df5f94702">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e7f7e11f7808e2e3574a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2d704f623dbfedc7be18">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-19d5fed5cf073ee552a6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a8c9fea8cb091ab6971d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-90e64ac50be80bb48c32">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ee75fa0e287c752e4955">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8c9d69f3e046ba3ccc18">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-32e8dcd7597ce8db47de">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-37cb11462d9a2ea401a3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-98dabf14b2e5ac44931b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e24300a0155b69ff0ab4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cb8df38c1a397a8733b9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fd80d87001ffb64ed6a2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4241017e5bdbea8988a4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-09baedca5f024db0ec10">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c9353888dd9fded6aa16">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9f95470c4f2ceb361564">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6422b530b09fab0922b3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6425f47c507c5d57d23e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a873f1cdbbe7c6513066">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9017b6ca1d3318b07e26">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f7b5560382652517b3d7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-51b3aff18bd6d21965ba">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-aaa9acd41d2d7d9e262c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e1e2e0750a6d9c5cf3bd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-412fa967deff3f571122">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e06f8814375266f3295b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-353b442c2b29d77b2487">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-25ab278fc1ad44faca6c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bd3e225039a4c2c44e9d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4a6637530af3d2eeda7d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8966baf4e88278af1726">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cf1cccbbf0c34e8ae8dc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8aca5c317f0fd10d7770">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7b68316ecb0366bf89c8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-119824842c02bda8cdd6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1e499a0d35db0fbd8078">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-41c53e191c7e606e2378">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9a456d52ed1dd82a462b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9d33e9d9bb2d5d3ccbd6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-94abb54a6d27dec2bac4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0557b11c240930087b5c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-faa434610f4d4e1564e7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1872ec9d10fcfef7685b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d5a170f89760e07ba641">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8138e2dbb755081de63c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0447a32c9907f3d170df">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d61b46629c26f561b11c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d788f46fd4f567416706">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5310436f1a51fe777027">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9d0678b25e87319f5f1b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-12bc239eba24d5ebefd1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a3a969b411f275e3b91a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-978d05ed923489da843f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-11c8ad159797d67e9c99">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a851c802d697803e8f52"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a851c802d697803e8f52`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-22c9a86ab196f9a98bb3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-22c9a86ab196f9a98bb3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3ebb6d01caa212d82ff8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3ebb6d01caa212d82ff8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-84f076b635ebf6d3197a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-84f076b635ebf6d3197a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-278a1a7d7ea29b7fc590"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-278a1a7d7ea29b7fc590`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-657a8d2bf5e2b1c876d1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-657a8d2bf5e2b1c876d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-37e20776b99b8cdb02c8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-37e20776b99b8cdb02c8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7e6a17166b56df00cd18"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7e6a17166b56df00cd18`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-54cedfc0491e8bf01523"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-54cedfc0491e8bf01523`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8e2af58d2091bae38866"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8e2af58d2091bae38866`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f525ffc5790e1a26e8a1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f525ffc5790e1a26e8a1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b0a56660ae7b46f02818"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b0a56660ae7b46f02818`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0b0d7435c9b247d5258e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0b0d7435c9b247d5258e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a5a463b91d18b0823fdb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a5a463b91d18b0823fdb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cecd8cc8abf99a48df66"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cecd8cc8abf99a48df66`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fdcd5411b5903394e8a8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fdcd5411b5903394e8a8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-353113ad73bc771ca613"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-353113ad73bc771ca613`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cce37d1a2ac268da80b6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cce37d1a2ac268da80b6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-570d3da901817621725a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-570d3da901817621725a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-83b26acee0ffeb465bda"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-83b26acee0ffeb465bda`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0a991cb9efd224d16fe9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0a991cb9efd224d16fe9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9d673ef43266b336ce15"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9d673ef43266b336ce15`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-16fac59b51e3b7d77c4e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-16fac59b51e3b7d77c4e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-23f0f21f36593f22ffda"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-23f0f21f36593f22ffda`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f339070d8d10d79f9d15"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f339070d8d10d79f9d15`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e2bcbd98f62a53f50d08"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e2bcbd98f62a53f50d08`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e05d058fb18fbcd7d2d9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e05d058fb18fbcd7d2d9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6ba71eb2b9a2f2a86011"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6ba71eb2b9a2f2a86011`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e9aebc8c77bf16e727a4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e9aebc8c77bf16e727a4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7cc6a0211ea74c4cf2d9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7cc6a0211ea74c4cf2d9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-042aa39ae82630df05cb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-042aa39ae82630df05cb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-83a7788a473ca08311f2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-83a7788a473ca08311f2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8acba46a3a4f31599208"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8acba46a3a4f31599208`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2df44b940b7984b79333"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2df44b940b7984b79333`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d73563a0e689a8ca1e95"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d73563a0e689a8ca1e95`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e946be095ae31d50e502"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e946be095ae31d50e502`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bdc8ae1bf952fb32e71b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bdc8ae1bf952fb32e71b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-05c8cbae2fa1f8f0c038"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-05c8cbae2fa1f8f0c038`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-696ab655e368c0b5c3dc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-696ab655e368c0b5c3dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f673698a048db4300afd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f673698a048db4300afd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e4bdc17c821873b68230"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e4bdc17c821873b68230`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6764ff2a8b0ce3a61500"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6764ff2a8b0ce3a61500`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-17054e53ae61906fd9b7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-17054e53ae61906fd9b7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b09aef0ac82b8f065dc3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b09aef0ac82b8f065dc3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c9ffeec9714e63b644b5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c9ffeec9714e63b644b5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7f406ba40d152914dfdb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7f406ba40d152914dfdb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c0a9334d77f60a426a73"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c0a9334d77f60a426a73`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-86b4c041a0d58611e779"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-86b4c041a0d58611e779`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-94dae94e21ba9ae287c2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-94dae94e21ba9ae287c2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f1f0098e7de228fecb68"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f1f0098e7de228fecb68`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-28316efa2db088746dc9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-28316efa2db088746dc9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-56cc2be357a362b7d315"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-56cc2be357a362b7d315`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7b3437f96aa06c16c1bd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7b3437f96aa06c16c1bd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b69752f5e1f4ca78b783"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b69752f5e1f4ca78b783`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c23f7e443b9a004bafea"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c23f7e443b9a004bafea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-00984e3d5fb6a4b09c05"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-00984e3d5fb6a4b09c05`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-35ada28323ec7eabaaf3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-35ada28323ec7eabaaf3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-81a940766aa1c9844b1e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-81a940766aa1c9844b1e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-67bf0b11e238c8b8b6bf"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-67bf0b11e238c8b8b6bf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-abb3dddffa06f3cb0505"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-abb3dddffa06f3cb0505`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4bbe0e6c9d6b4673e106"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4bbe0e6c9d6b4673e106`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-38f9864409bb2e37a7fa"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-38f9864409bb2e37a7fa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d3eced1af186088bda7e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d3eced1af186088bda7e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3e8de7a4be542baab864"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3e8de7a4be542baab864`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-499c96d5f2b7aa057ed7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-499c96d5f2b7aa057ed7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-805dc525660e91ab059b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-805dc525660e91ab059b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a8d3295a97bb8ec7d368"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a8d3295a97bb8ec7d368`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4bf0dada2ebb78a55ae2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4bf0dada2ebb78a55ae2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a018e2a4cc0d2d46e0d6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a018e2a4cc0d2d46e0d6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-056f85c8d0414345af91"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-056f85c8d0414345af91`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-01aedb06f2c56e0dbe98"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-01aedb06f2c56e0dbe98`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f408be755fe87f4b1200"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f408be755fe87f4b1200`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a8c08d2be42e5261f728"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a8c08d2be42e5261f728`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e1008c0799d8897e626a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e1008c0799d8897e626a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-689da73c4b5cbb8e4cc1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-689da73c4b5cbb8e4cc1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f897d16977e17bac76cb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f897d16977e17bac76cb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-09ed927ec4efd95f9aa4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-09ed927ec4efd95f9aa4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1463563c9072e2587b1f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1463563c9072e2587b1f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2b8de842d6719c8b0353"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2b8de842d6719c8b0353`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b8b698e2a7781e700d92"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b8b698e2a7781e700d92`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0a6674f457cf4923ddfa"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0a6674f457cf4923ddfa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1d2d0db1c3345c316a89"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1d2d0db1c3345c316a89`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cfe5434cd9a7465da9c6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cfe5434cd9a7465da9c6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-34204e9a5c35381fa23f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-34204e9a5c35381fa23f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7fc3bf4b8b5b2d8a1f13"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7fc3bf4b8b5b2d8a1f13`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-48c4b4fa5a3a0bff5751"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-48c4b4fa5a3a0bff5751`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-05d2a5b7d17f35484c04"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-05d2a5b7d17f35484c04`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-90aa41165c2de67beac8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-90aa41165c2de67beac8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4bd4f56aed7b3fab0fcd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4bd4f56aed7b3fab0fcd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-35f1a96cb51f23d9aad0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-35f1a96cb51f23d9aad0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-822bcb2703b2c36ded28"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-822bcb2703b2c36ded28`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-26b824baab87a0559aed"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-26b824baab87a0559aed`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3df106344513829b9d92"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3df106344513829b9d92`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-98a287286045cf7133d6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-98a287286045cf7133d6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-995b713069b0df338bc9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-995b713069b0df338bc9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a1ef7badb0fb8359967b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a1ef7badb0fb8359967b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-08911640c7763ac13a3d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-08911640c7763ac13a3d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-16a3135c34335fc923ff"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-16a3135c34335fc923ff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7f4439cc3a6d3ef6352e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7f4439cc3a6d3ef6352e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fe1c0bd3d82f4e154551"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fe1c0bd3d82f4e154551`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0c60924f3a56e7b6e6d1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0c60924f3a56e7b6e6d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-169fae5717da7927b8d4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-169fae5717da7927b8d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-676649e5e18df29b4452"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-676649e5e18df29b4452`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e28a6a62ee9de556334f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e28a6a62ee9de556334f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f9a48f55b21bca9ffd46"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f9a48f55b21bca9ffd46`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-65f6e98dd6fdc85211be"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-65f6e98dd6fdc85211be`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-50ab05d4e3ca9f2e0b57"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-50ab05d4e3ca9f2e0b57`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-29401d9a790a07b89324"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-29401d9a790a07b89324`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1baab1807a609ca8c322"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1baab1807a609ca8c322`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-874ef77133842089c7f4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-874ef77133842089c7f4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ed4685a540bfbdf6f374"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ed4685a540bfbdf6f374`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bee7bebf4fa42022f96a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bee7bebf4fa42022f96a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c3ab6fac8c86e4c02d82"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c3ab6fac8c86e4c02d82`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-83ad40ad4f966852624c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-83ad40ad4f966852624c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4ef37c63e2a1cea8a891"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4ef37c63e2a1cea8a891`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0ed3f9b7e4c00d68958b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0ed3f9b7e4c00d68958b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1372d73ea4cd9aeb7d9e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1372d73ea4cd9aeb7d9e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-80daeea2d7e41310083e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-80daeea2d7e41310083e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b39769db66a8bb58a64c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b39769db66a8bb58a64c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f4657ec02387c2bdbc2c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f4657ec02387c2bdbc2c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f75a1e99a1395a8fce88"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f75a1e99a1395a8fce88`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-35fc1c9898d5abc14310"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-35fc1c9898d5abc14310`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-28704fc6676ec435731d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-28704fc6676ec435731d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-328abd19fbf83fa284f7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-328abd19fbf83fa284f7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6055562585bf76898046"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6055562585bf76898046`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dd0489d07fd45927b0cd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-dd0489d07fd45927b0cd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-83ae8f060c039719308f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-83ae8f060c039719308f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e9747451b9ebeb28665d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e9747451b9ebeb28665d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-868018f7bdb64f5a94ee"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-868018f7bdb64f5a94ee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e5aab89c59c82339a9ca"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e5aab89c59c82339a9ca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d5f5b7c35ea3598c90ce"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d5f5b7c35ea3598c90ce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-08b2301669bd98a25f57"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-08b2301669bd98a25f57`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2547aad666e7278304ac"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2547aad666e7278304ac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7553ef0701daa094f59b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7553ef0701daa094f59b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-43d92c33f5ee4f2e0414"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-43d92c33f5ee4f2e0414`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c57b455e148c00631c3e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c57b455e148c00631c3e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-669b77de64df70971b37"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-669b77de64df70971b37`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3fcae206b05eb700c5a1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3fcae206b05eb700c5a1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-622228507025ac598f3c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-622228507025ac598f3c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ad8b8f0f1a2503bbd431"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ad8b8f0f1a2503bbd431`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-09bcae19c968ffac789f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-09bcae19c968ffac789f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fb880b921d88ae0445dd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fb880b921d88ae0445dd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-63e0efef0062eb4aad76"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-63e0efef0062eb4aad76`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3a840863fd260d1c7851"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3a840863fd260d1c7851`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0e3085cc3b1cfecd18fb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0e3085cc3b1cfecd18fb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3f9d3bcd2e9576ecceda"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3f9d3bcd2e9576ecceda`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-40e15bcd229cd601340f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-40e15bcd229cd601340f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9910f7367611bda85652"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9910f7367611bda85652`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6d3edd6f86972197920b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6d3edd6f86972197920b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3ca29ac96533419b8178"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3ca29ac96533419b8178`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7ca2212d79d9faa1270e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7ca2212d79d9faa1270e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c7b6b3f69bc2f21475c3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c7b6b3f69bc2f21475c3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fec1d13caa8b9483e2c4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fec1d13caa8b9483e2c4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-85316b17f8e464abb8e9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-85316b17f8e464abb8e9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dc685732ea2417d3ead8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-dc685732ea2417d3ead8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-de54372c2a19b08cce51"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-de54372c2a19b08cce51`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3dc2ab0a1da2a4414afa"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3dc2ab0a1da2a4414afa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bbee66ca79c0aa28134f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bbee66ca79c0aa28134f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-13104b3f09047bff7e81"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-13104b3f09047bff7e81`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c2953c3987b15b482ebb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c2953c3987b15b482ebb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fc2fd7d64e1d5f60cd4d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fc2fd7d64e1d5f60cd4d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f540d20fd6dbf746e491"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f540d20fd6dbf746e491`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e973af35260024066385"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e973af35260024066385`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9f7d5c26930a7448c27c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9f7d5c26930a7448c27c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8dccd871afbef6b9325a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8dccd871afbef6b9325a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-def19d2a2e93556aecbc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-def19d2a2e93556aecbc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-690953f7d38291acec40"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-690953f7d38291acec40`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ccbc3c8f1474f98475b9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ccbc3c8f1474f98475b9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-394b11469ddd61e23120"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-394b11469ddd61e23120`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ade111552e01d5886a4f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ade111552e01d5886a4f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6b1d7da96a4ab068e2dc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6b1d7da96a4ab068e2dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-adeaf591690e0d767337"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-adeaf591690e0d767337`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-96e9d13c96dbf9ca7aca"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-96e9d13c96dbf9ca7aca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-72d11c90e933dc71c9db"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-72d11c90e933dc71c9db`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-efc1a8914643b73cedbc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-efc1a8914643b73cedbc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e61dd1f901630e02623b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e61dd1f901630e02623b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-93ef4c25495dc876780a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-93ef4c25495dc876780a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b3dd23ae5ee83a725af6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b3dd23ae5ee83a725af6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-504f70a5795d3fb23ec8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-504f70a5795d3fb23ec8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-08520efb904262e3b5f8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-08520efb904262e3b5f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-eab2d1c1308ea80eda63"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-eab2d1c1308ea80eda63`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-74b61a5198e8a8cd3801"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-74b61a5198e8a8cd3801`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-63e7e9baa5ec16867ce3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-63e7e9baa5ec16867ce3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-49e52a88a99f69e1b292"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-49e52a88a99f69e1b292`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-843168188006ea40ff32"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-843168188006ea40ff32`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bd7428b71a92379007b9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bd7428b71a92379007b9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-070fe4309a5a5db0f134"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-070fe4309a5a5db0f134`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8bdb46296dc54ff14455"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8bdb46296dc54ff14455`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0e7ada239c2718768bb4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0e7ada239c2718768bb4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-42dc9aa44e9e89d55281"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-42dc9aa44e9e89d55281`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-54b2be6e9c4e590ce5d7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-54b2be6e9c4e590ce5d7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-572c7cded49252e45fd8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-572c7cded49252e45fd8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8baf50dcd58e781c2d12"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8baf50dcd58e781c2d12`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2fd5aacd07e7305074ea"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2fd5aacd07e7305074ea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-10bb4505e52163d67f52"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-10bb4505e52163d67f52`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fe4aae8492ec0e376a88"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fe4aae8492ec0e376a88`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0e1b9411d189c4bf7190"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0e1b9411d189c4bf7190`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f3676e44be093036ac7f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f3676e44be093036ac7f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f8a231b06c3b5be543ea"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f8a231b06c3b5be543ea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-59fa887559689aa418a9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-59fa887559689aa418a9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-eba8384ac8ec3de29938"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-eba8384ac8ec3de29938`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e614fd873bb51401a143"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e614fd873bb51401a143`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a1e958e66878b4f98b92"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a1e958e66878b4f98b92`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c433a894319125d16c66"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c433a894319125d16c66`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-afc9dae213597ff4050a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-afc9dae213597ff4050a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f42c76dc599d7bd89aa3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f42c76dc599d7bd89aa3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0e9fcf6d55b198be9381"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0e9fcf6d55b198be9381`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eb6871a2e4e6ec85304f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-eb6871a2e4e6ec85304f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b69c31de727cbcc10695"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b69c31de727cbcc10695`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8fbb82c3037b297f938e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8fbb82c3037b297f938e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-158cfc2c1a071186839d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-158cfc2c1a071186839d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9e30432f56a0d6ab69dd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9e30432f56a0d6ab69dd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c5d9e3396975d05d6ceb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c5d9e3396975d05d6ceb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-611cdeb4c85b8812b125"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-611cdeb4c85b8812b125`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b314a1667862f6ef518b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b314a1667862f6ef518b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-22709fe71a6efe2180d8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-22709fe71a6efe2180d8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b610c9dbeaef591ba59f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b610c9dbeaef591ba59f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bdda2dd085828d12f565"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bdda2dd085828d12f565`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c310d698843acaeb3709"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c310d698843acaeb3709`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-83595e2a73d720bdbc73"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-83595e2a73d720bdbc73`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6db24bcb7ae38afbc505"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6db24bcb7ae38afbc505`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c51c1ce37d6b74976b64"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c51c1ce37d6b74976b64`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-74792c43df5dfebd4fee"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-74792c43df5dfebd4fee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-127dc7890296811176b7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-127dc7890296811176b7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ca5d5bfe1bb4017b058e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ca5d5bfe1bb4017b058e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8d405ce35f41b17cabee"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8d405ce35f41b17cabee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a03c485c3fb509cd74e2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a03c485c3fb509cd74e2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e5d5be100fa8905ad383"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e5d5be100fa8905ad383`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-93f18b557b2791d3efb1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-93f18b557b2791d3efb1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fcb617e49a8fe6e7dff5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fcb617e49a8fe6e7dff5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6ef977616b9d06f21df7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6ef977616b9d06f21df7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8837e796d04fdc171308"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8837e796d04fdc171308`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ab315a9ad6ff03692069"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ab315a9ad6ff03692069`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d0ef9b9ba84e3fd11ff7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d0ef9b9ba84e3fd11ff7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cdbff4ecdfd3258a5150"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cdbff4ecdfd3258a5150`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8d8dc5bde7f40a13d9e4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8d8dc5bde7f40a13d9e4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ec14a59f6bff2c2679d4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ec14a59f6bff2c2679d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-63cd521f34f0b7609bde"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-63cd521f34f0b7609bde`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-296dc9f0aabc8de356f6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-296dc9f0aabc8de356f6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f21ba81d1807cf4a2c97"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f21ba81d1807cf4a2c97`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6d5320f1b194c082112b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6d5320f1b194c082112b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-691625c5920d4510a0bc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-691625c5920d4510a0bc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3fdc4b38270b42dec556"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3fdc4b38270b42dec556`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c3f1f20caef83b05cf0e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c3f1f20caef83b05cf0e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-56d893e8d11011cefb71"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-56d893e8d11011cefb71`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d2aabbdc7e199dc2763e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d2aabbdc7e199dc2763e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eb950a966f23664ab928"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-eb950a966f23664ab928`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-029e2df8fddc3486cde8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-029e2df8fddc3486cde8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-11b822e2d01901925581"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-11b822e2d01901925581`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c4b89c7909aa57071562"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c4b89c7909aa57071562`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e5092a1232b9088833bd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e5092a1232b9088833bd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fbdbba089c43a0dcaa03"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fbdbba089c43a0dcaa03`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d52043b513fa627771f9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d52043b513fa627771f9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cbe506411bfbd42d1a93"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cbe506411bfbd42d1a93`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fca72824c01be7e8fc68"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fca72824c01be7e8fc68`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6cd380b3c2be3d22b36d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6cd380b3c2be3d22b36d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-620bb69800dd7c6284c5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-620bb69800dd7c6284c5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3d7218324d88e465d773"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3d7218324d88e465d773`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3c6562765880dd9d3f47"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3c6562765880dd9d3f47`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-abda45bbfe0123b86432"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-abda45bbfe0123b86432`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-647d80f351975b465d92"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-647d80f351975b465d92`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3ee74b5e1cb555bbabcf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3ee74b5e1cb555bbabcf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fdfea3bf0f5b8e470ffe"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fdfea3bf0f5b8e470ffe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-717a338f041ea29ff499"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-717a338f041ea29ff499`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f7cf7efafa9fe6b49825"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f7cf7efafa9fe6b49825`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-35450065c958ef03af01"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-35450065c958ef03af01`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8136a66eda72bffbb4ed"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8136a66eda72bffbb4ed`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-caac1fc24124cf9332e2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-caac1fc24124cf9332e2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-124bb87469e05a60bba3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-124bb87469e05a60bba3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c8beb54fcd4601f11fe6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c8beb54fcd4601f11fe6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-591f2b5fe8b337e0f009"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-591f2b5fe8b337e0f009`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c7e0a148fab8c6bf6abd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c7e0a148fab8c6bf6abd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bc5708b5c29b2ff65209"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bc5708b5c29b2ff65209`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3eb9077b057e96ad0c76"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3eb9077b057e96ad0c76`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8dadee0f7cdf3b1b658f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8dadee0f7cdf3b1b658f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-88764060a9532a3322cc"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-88764060a9532a3322cc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ad58650ba559bb2c76af"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ad58650ba559bb2c76af`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-579c86c6d932b79d2ddc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-579c86c6d932b79d2ddc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e3a7d061c0b6a3e64873"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e3a7d061c0b6a3e64873`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5ef2a1edf7990af9bd37"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5ef2a1edf7990af9bd37`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-173322082c578b53d843"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-173322082c578b53d843`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3ff4226c14eb4e0aaf5c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3ff4226c14eb4e0aaf5c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a99ab0b823b0589d9d0d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a99ab0b823b0589d9d0d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-af52dc6ae25ba0967917"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-af52dc6ae25ba0967917`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ba8b9a8938946522199f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ba8b9a8938946522199f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-230eab31be4c1fb71980"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-230eab31be4c1fb71980`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7b921b0e7a9f880c20a5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7b921b0e7a9f880c20a5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e74015cfd6ed48b6694a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e74015cfd6ed48b6694a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6b3d2f50960e4567ebae"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6b3d2f50960e4567ebae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4a52320c4370567e0d1a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4a52320c4370567e0d1a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ed225a42839ad4503921"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ed225a42839ad4503921`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d967974de7e63e20ddb5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d967974de7e63e20ddb5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fe0edd54bc3bbd776bbc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fe0edd54bc3bbd776bbc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b1c2a3b147cd9cb3a0bf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b1c2a3b147cd9cb3a0bf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3a7df544bec6767f5199"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3a7df544bec6767f5199`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-52ab4b89fb57ca1025c8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-52ab4b89fb57ca1025c8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e4760cbfab8b9091fc98"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e4760cbfab8b9091fc98`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b3cd80ef8a76160d7aa6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b3cd80ef8a76160d7aa6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4120d125fe91fc2b0fed"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4120d125fe91fc2b0fed`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b07855d6c42e4e5da065"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b07855d6c42e4e5da065`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6a4db7bc776df5f94702"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6a4db7bc776df5f94702`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e7f7e11f7808e2e3574a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e7f7e11f7808e2e3574a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2d704f623dbfedc7be18"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2d704f623dbfedc7be18`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-19d5fed5cf073ee552a6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-19d5fed5cf073ee552a6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a8c9fea8cb091ab6971d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a8c9fea8cb091ab6971d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-90e64ac50be80bb48c32"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-90e64ac50be80bb48c32`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ee75fa0e287c752e4955"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ee75fa0e287c752e4955`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8c9d69f3e046ba3ccc18"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8c9d69f3e046ba3ccc18`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-32e8dcd7597ce8db47de"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-32e8dcd7597ce8db47de`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-37cb11462d9a2ea401a3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-37cb11462d9a2ea401a3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-98dabf14b2e5ac44931b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-98dabf14b2e5ac44931b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e24300a0155b69ff0ab4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e24300a0155b69ff0ab4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cb8df38c1a397a8733b9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cb8df38c1a397a8733b9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fd80d87001ffb64ed6a2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fd80d87001ffb64ed6a2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4241017e5bdbea8988a4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4241017e5bdbea8988a4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-09baedca5f024db0ec10"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-09baedca5f024db0ec10`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c9353888dd9fded6aa16"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c9353888dd9fded6aa16`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9f95470c4f2ceb361564"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9f95470c4f2ceb361564`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6422b530b09fab0922b3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6422b530b09fab0922b3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6425f47c507c5d57d23e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6425f47c507c5d57d23e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a873f1cdbbe7c6513066"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a873f1cdbbe7c6513066`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9017b6ca1d3318b07e26"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9017b6ca1d3318b07e26`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f7b5560382652517b3d7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f7b5560382652517b3d7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-51b3aff18bd6d21965ba"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-51b3aff18bd6d21965ba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-aaa9acd41d2d7d9e262c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-aaa9acd41d2d7d9e262c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e1e2e0750a6d9c5cf3bd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e1e2e0750a6d9c5cf3bd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-412fa967deff3f571122"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-412fa967deff3f571122`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e06f8814375266f3295b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e06f8814375266f3295b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-353b442c2b29d77b2487"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-353b442c2b29d77b2487`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-25ab278fc1ad44faca6c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-25ab278fc1ad44faca6c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bd3e225039a4c2c44e9d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bd3e225039a4c2c44e9d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4a6637530af3d2eeda7d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4a6637530af3d2eeda7d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8966baf4e88278af1726"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8966baf4e88278af1726`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cf1cccbbf0c34e8ae8dc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cf1cccbbf0c34e8ae8dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8aca5c317f0fd10d7770"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8aca5c317f0fd10d7770`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7b68316ecb0366bf89c8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7b68316ecb0366bf89c8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-119824842c02bda8cdd6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-119824842c02bda8cdd6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1e499a0d35db0fbd8078"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1e499a0d35db0fbd8078`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-41c53e191c7e606e2378"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-41c53e191c7e606e2378`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9a456d52ed1dd82a462b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9a456d52ed1dd82a462b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9d33e9d9bb2d5d3ccbd6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9d33e9d9bb2d5d3ccbd6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-94abb54a6d27dec2bac4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-94abb54a6d27dec2bac4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0557b11c240930087b5c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0557b11c240930087b5c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-faa434610f4d4e1564e7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-faa434610f4d4e1564e7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1872ec9d10fcfef7685b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1872ec9d10fcfef7685b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d5a170f89760e07ba641"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d5a170f89760e07ba641`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8138e2dbb755081de63c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8138e2dbb755081de63c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0447a32c9907f3d170df"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0447a32c9907f3d170df`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d61b46629c26f561b11c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d61b46629c26f561b11c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d788f46fd4f567416706"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d788f46fd4f567416706`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5310436f1a51fe777027"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5310436f1a51fe777027`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9d0678b25e87319f5f1b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9d0678b25e87319f5f1b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-12bc239eba24d5ebefd1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-12bc239eba24d5ebefd1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a3a969b411f275e3b91a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a3a969b411f275e3b91a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-978d05ed923489da843f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-978d05ed923489da843f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-11c8ad159797d67e9c99"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-11c8ad159797d67e9c99`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

This new type implements one functional part of the human-approved close parallel layout. It preserves the [frozen source proposal](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/TESTING.md#32-close-parallel-ramps-and-perpendicular-avenue-approaches) and leaves the retained R40 and compact assemblies available with their own resource identities and evidence. This piece's exact source is [piece.jsonc](piece.jsonc); the shared placement plan is [assembly.jsonc](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/assembly.jsonc).

The ground-mouth revision narrowed terminal asphalt while preserving the 6 m grade interfaces and its saved traffic routes. The later slip-lane revision lengthens the shoulder treatment and changes its access PATHs and white markings, while retaining all fifteen permanent types, the 31-cell union, and those narrow ground mouths. The earlier `ddrhw-parallel-diamond-parts-01` and `ddrhw-parallel-diamond-pedestrian-mouths-01` build identities retain their original scopes. The current revision uses `ddrhw-parallel-diamond-slip-lanes-02`; only its own matching saved-resource report can establish its software result.
