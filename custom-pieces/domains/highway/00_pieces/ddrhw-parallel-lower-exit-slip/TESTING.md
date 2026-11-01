---
title: "Testing: DD RHW-4 — L1 Exit Slip Lanes — Parallel"
summary: "Check this parallel component against its saved resources and retain separate human game observations."
audience: "contributors"
document_type: "reference"
---

# Testing: DD RHW-4 — L1 Exit Slip Lanes — Parallel

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

This record covers **ddrhw-parallel-lower-exit-slip**, used once as **P04** in the [parallel diamond](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/README.md). It has 2 occupied tiles in a 2 × 2 rectangle, the exact authored 0° reference at X6, Y8, and the functional levels described in the [piece guide](README.md#2-piece-and-placement). Saved native through routes, added access fragments, actual model support, material flags, physical joins, rotations, and adaptive resources where present have distinct software checks. Human appearance and travel observations remain separate.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `channel-11-out` | road / 1 / primary | out | [-8.0, -15.029437, 4.364109]; [-0.7071067811865587, -0.7071067811865365]; -0.179118533 | `path-interface-6f98c9419d701c4a592c` |
| `channel-12-out` | road / 1 / primary | out | [-3.2, -24.0, 7.5]; [-0.7071067811865475, -0.7071067811865477]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `channel-01-in` | road / 1 / primary | in | [-3.2, -24.0, 15.0]; [0.7071067811865475, 0.7071067811865477]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `channel-02-in` | road / 1 / primary | in | [-0.970563, -8.0, 6.144726]; [-0.7071067811865476, -0.7071067811865476]; -0.17907534 | `path-interface-61a771345641cff0130a` |
| `channel-13-out` | road / 1 / primary | out | [3.2, -24.0, 7.5]; [-0.7071067811865474, -0.7071067811865478]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `channel-03-in` | road / 1 / primary | in | [3.2, -24.0, 15.0]; [0.7071067811865474, 0.7071067811865478]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `channel-04-in` | road / 1 / primary | in | [8.0, -19.2, 7.5]; [-0.7071067811865474, -0.7071067811865478]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `channel-14-out` | road / 1 / primary | out | [8.0, -19.2, 15.0]; [0.7071067811865474, 0.7071067811865478]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `channel-05-in` | road / 1 / primary | in | [8.0, -12.8, 7.5]; [-0.7071067811865475, -0.7071067811865477]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `channel-15-out` | road / 1 / primary | out | [8.0, -12.8, 15.0]; [0.7071067811865475, 0.7071067811865477]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `channel-16-out` | road / 1 / primary | out | [8.0, 0.104467, 7.5]; [-0.9404586044448431, -0.3399082425091487]; 0.0 | `path-interface-dd0badef63ec6dee79f2` |
| `channel-17-out` | road / 1 / primary | out | [12.8, -8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `channel-06-in` | road / 1 / primary | in | [12.8, -8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `channel-18-out` | road / 1 / primary | out | [19.2, -8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `channel-07-in` | road / 1 / primary | in | [19.2, -8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `channel-08-in` | road / 1 / primary | in | [24.0, -3.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `channel-19-out` | road / 1 / primary | out | [24.0, -3.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `channel-09-in` | road / 1 / primary | in | [24.0, 3.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `channel-20-out` | road / 1 / primary | out | [24.0, 3.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `channel-10-in` | road / 1 / primary | in | [24.0, 6.194881, 7.5]; [-0.9864122952117507, -0.16428872102212644]; 0.0 | `path-interface-0da9b7f162296ea51351` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `channel-01-in` → `channel-15-out` | primary |
| road | `channel-02-in` → `channel-11-out` | primary |
| road | `channel-03-in` → `channel-14-out` | primary |
| road | `channel-04-in` → `channel-13-out` | primary |
| road | `channel-05-in` → `channel-12-out` | primary |
| road | `channel-06-in` → `channel-20-out` | primary |
| road | `channel-07-in` → `channel-19-out` | primary |
| road | `channel-08-in` → `channel-18-out` | primary |
| road | `channel-09-in` → `channel-17-out` | primary |
| road | `channel-10-in` → `channel-16-out` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `channel-01-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-10-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-10-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-10-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-10-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-10-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-10-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-10-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-10-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-10-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use Windows SimCity 4 with the pinned NAM 50 right-hand-traffic inputs, including through Wine or CrossOver. The shared [build guide](../../../../docs/BUILD_AND_INSTALL.md) owns private input settings and explicit installation. Use the complete fifteen-component assembly for travel tests: this individual component can expose required route fragments at more than one city-tile edge. A matching-looking isolated end is insufficient to create the whole journey.

Prepare the [assembly's flat reference test area](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#2-test-setup), keep the camera north-up for placement, and use the exact occupied cells **(X7, Y8), (X6, Y7)**. The full core occupies 31 cells inside X1–X8 and Y1–Y8; the preserved drawing reference still shows X0–X9 and Y0–Y9. One tile is 16 m. Additional outside road approaches are separate from that core count.

## 3. Software checks

Run from the repository directory containing `custom-pieces/`. These commands inspect an existing build and its current source-bound connector records; they do not install anything, supply missing inputs, or approve a manual case. An absent or failing report is not a software pass.

```sh
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/ddrhw-parallel-diamond-slip-lanes-02
python3 -B custom-pieces/scp.py connectors check --domain highway --piece ddrhw-parallel-lower-exit-slip --build dist/ddrhw-parallel-diamond-slip-lanes-02
python3 -B custom-pieces/scp.py docs-check --piece ddrhw-parallel-lower-exit-slip
```

The [complete saved-assembly check](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#3-software-checks) checks this component in all fifteen placements, including physical model overhang and the traffic fragments owned by its neighbours. The ordinary build's manifest and verification report identify the actual measured resources. Retain every software failure with its source fingerprint; rerunning a renderer cannot repair it.

The current slip-lane revision changes the highway-shoulder traffic routes and their white markings within the existing construction footprint. Read outward from a through lane toward its ramp: each lower route has an 8 m smooth sideways taper and a 4 m straight shoulder section; each upper route has a 5 m taper and a 1 m straight shoulder section. The lower routes begin 6.788225 m farther upstream in already owned native highway tiles. The upper routes retain their previous outer ports because the unchanged 31-cell layout provides less shoulder distance there. These distances are measured along the straight highway axis. On-ramps follow the same profiles in reverse. The auxiliary-lane centre is 5.5 m from the highway axis; the checked 2.5 m-wide car corridor leaves 0.421875 m to the native barrier foot on the straight section. These are compressed experimental dimensions, not a real-road design standard. Native through PATHs, roadway outside the native 8 m deck edge, grades, ground terminals, permanent identifiers, and construction ownership retain their previous scope. Check the matching saved report before treating this source revision as verified. This component supplies highway or ramp geometry. The three ground components P01, P02, and P03 own the implemented adaptive Avenue pavement and retained pedestrian routes. Connecting this elevated component does not itself select a sidewalk appearance. Read the [actual mechanism and limits](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#3-software-checks).

The earlier narrow ground mouths are retained: each terminal keeps its 6 m grade join, narrows to 3.5 m over 3 m, and stays narrow through its R6 turn and Avenue joining collar. The ramp centreline crosses the retained pedestrian-route centreline 3.258752 m from the grade join, after that 3 m ground taper is complete. The asphalt footprint reaches the pedestrian route earlier, while the ground taper is still narrowing; this is the actual driveway crossing.

## 4. Game checks

1. Select this exact component through the assembly button, match P04 at **X6, Y8**, and confirm that the occupied preview squares match **(X7, Y8), (X6, Y7)** before clicking.
2. Place the full assembly using the order in its guide. Inspect this component's saved model from both opposing oblique views, and compare its real join with the neighbouring models; look for gaps, blocked barrier openings, misplaced supports, or a sudden pavement-colour patch.
3. Repeat fresh placement in the four distinct proper rotations. Rotate the camera separately after placement, because camera movement and a newly rotated piece test different things.
4. For an adaptive Avenue cell, connect ordinary Avenue outside the core, add nearby development, and compare its pavement variant with the neighbouring Avenue. Connecting the Avenue alone does not select the developed pavement appearance. Inspect both narrow driveway crossings, then check pedestrian Route Query and visible walking separately; a sidewalk image does not create a pedestrian PATH, and the crossing remains road asphalt. For a component without Avenue cells, inspect the neighbouring adaptive owners instead of expecting this piece to change pavement itself.
5. Run every required car and pedestrian journey listed by the exact matrix. Record Route Query and visible travel separately. Also confirm that every declared forbidden transfer stays unavailable; a visually clear road surface is not traffic evidence.
6. Inspect shadows, demolish the component, replace it, save the city, quit completely, and reload. Check that no temporary placement handle remains and that the component and its traffic neighbours remain correct.

Record only explicit observations through [the shared observation workflow](../../../../docs/TESTING.md), selecting **ddrhw-parallel-lower-exit-slip** and its exact current cases. No observation of the older adaptive probe, R40 diamond, or another rotation automatically approves this new component.

## 5. Results and known issues

The implementation is experimental. The generated records below are authoritative for the current evidence scope; **all new human game observations remain unverified** until the user confirms their exact cases. In particular, outside native DD RHW connections, over-Avenue placement, Avenue redraw, temporary-handle collision behaviour, pedestrian pavement variants, moving traffic, camera rotations, demolition, and save/reload require game checks.

The whole-cell traffic partition is intentionally different from the physical model split. The revised traffic route and matching white markings use the existing shoulder. Read from the highway through lane toward the ramp: the lower L1 shoulder section has a 8 m smooth sideways taper, followed by 4 m straight and parallel to the highway. An on-ramp follows the reverse sequence in its direction of travel. These two lengths are measured along the straight highway axis and describe the shoulder section, not the complete ramp. The lower route starts 6.788225 m farther upstream, within an already owned native highway tile. The auxiliary-lane centre is 5.5 m from the highway axis. Its checked 2.5 m-wide car corridor leaves 0.421875 m to the native barrier foot at the straight shoulder section. The two occupied cells lie diagonally inside a sparse 2 × 2 rectangle. Its construction reference is an empty corner, so align both occupied preview cells instead of assuming that the reference position is a third tile. Complete boundary cards include both highway levels and every access fragment; matching only the named ramp is insufficient. This is a limitation to understand when choosing replacement modules, not permission to discard a required boundary service.

Adaptive pavement is implemented through native texture variants and correctly rotating model props, rather than a fixed sidewalk slab. Its visible appearance depends on the native development rules, and a sidewalk replacement mod needs its own compatibility check. The approximately 1.149 m clearance applies where the terminal asphalt and retained pedestrian centreline run beside one another; the actual driveway crossings are deliberately excluded. A measured route clearance does not establish visible walking, a continuous pavement strip, or a particular pedestrian-versus-car priority in the game.

<!-- BEGIN MANUAL SUMMARY -->

### Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/3 applicable cases passed; 0 failed, 0 stale.
- [ ] In-game rendering: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Route Query: 0/40 applicable cases passed; 0 failed, 0 stale.
- [ ] Visible travel: 0/40 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 461, passed: 0, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-parallel-lower-exit-slip/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-parallel-lower-exit-slip/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-b0fa3bba38db48447050">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-b0fa3bba38db48447050"></a>

**General: unverified** — `software_resources-b0fa3bba38db48447050`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-b0fa3bba38db48447050">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-b0fa3bba38db48447050"></a>

**General: unverified** — `software_connectivity-b0fa3bba38db48447050`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-parallel-lower-exit-slip:canonical-southeast | <a href="#case-preview_review-5c6fc8b99f5b1e38e23f">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-lower-exit-slip:canonical-top | <a href="#case-preview_review-57f7ce273d5d5ea6fb03">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-lower-exit-slip:connection-overview | <a href="#case-preview_review-043636f03a9217c2fde3">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-parallel-lower-exit-slip:canonical-southeast</summary>

<a id="case-preview_review-5c6fc8b99f5b1e38e23f"></a>

**General: unverified** — `preview_review-5c6fc8b99f5b1e38e23f`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-parallel-lower-exit-slip:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-lower-exit-slip:canonical-top</summary>

<a id="case-preview_review-57f7ce273d5d5ea6fb03"></a>

**General: unverified** — `preview_review-57f7ce273d5d5ea6fb03`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-parallel-lower-exit-slip:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-lower-exit-slip:connection-overview</summary>

<a id="case-preview_review-043636f03a9217c2fde3"></a>

**General: unverified** — `preview_review-043636f03a9217c2fde3`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-parallel-lower-exit-slip:connection-overview.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-2e95d1a948c33f76e34f">[ ] unverified</a> | <a href="#case-in_game_render-4df8b5dca435e10b4af6">[ ] unverified</a> | <a href="#case-in_game_render-0fa702a194362fff1761">[ ] unverified</a> | <a href="#case-in_game_render-0821a24e8076663aefb3">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-2e95d1a948c33f76e34f"></a>

**0° CCW: unverified** — `in_game_render-2e95d1a948c33f76e34f`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-4df8b5dca435e10b4af6"></a>

**90° CCW: unverified** — `in_game_render-4df8b5dca435e10b4af6`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-0fa702a194362fff1761"></a>

**180° CCW: unverified** — `in_game_render-0fa702a194362fff1761`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-0821a24e8076663aefb3"></a>

**270° CCW: unverified** — `in_game_render-0821a24e8076663aefb3`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-2e95d1a948c33f76e34f">[ ] unverified</a> | <a href="#case-in_game_placement-4df8b5dca435e10b4af6">[ ] unverified</a> | <a href="#case-in_game_placement-0fa702a194362fff1761">[ ] unverified</a> | <a href="#case-in_game_placement-0821a24e8076663aefb3">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-2e95d1a948c33f76e34f"></a>

**0° CCW: unverified** — `in_game_placement-2e95d1a948c33f76e34f`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-4df8b5dca435e10b4af6"></a>

**90° CCW: unverified** — `in_game_placement-4df8b5dca435e10b4af6`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-0fa702a194362fff1761"></a>

**180° CCW: unverified** — `in_game_placement-0fa702a194362fff1761`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-0821a24e8076663aefb3"></a>

**270° CCW: unverified** — `in_game_placement-0821a24e8076663aefb3`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-2e95d1a948c33f76e34f">[ ] unverified</a> | <a href="#case-in_game_demolition-4df8b5dca435e10b4af6">[ ] unverified</a> | <a href="#case-in_game_demolition-0fa702a194362fff1761">[ ] unverified</a> | <a href="#case-in_game_demolition-0821a24e8076663aefb3">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-2e95d1a948c33f76e34f"></a>

**0° CCW: unverified** — `in_game_demolition-2e95d1a948c33f76e34f`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-4df8b5dca435e10b4af6"></a>

**90° CCW: unverified** — `in_game_demolition-4df8b5dca435e10b4af6`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-0fa702a194362fff1761"></a>

**180° CCW: unverified** — `in_game_demolition-0fa702a194362fff1761`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-0821a24e8076663aefb3"></a>

**270° CCW: unverified** — `in_game_demolition-0821a24e8076663aefb3`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-2e95d1a948c33f76e34f">[ ] unverified</a> | <a href="#case-in_game_save_reload-4df8b5dca435e10b4af6">[ ] unverified</a> | <a href="#case-in_game_save_reload-0fa702a194362fff1761">[ ] unverified</a> | <a href="#case-in_game_save_reload-0821a24e8076663aefb3">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-2e95d1a948c33f76e34f"></a>

**0° CCW: unverified** — `in_game_save_reload-2e95d1a948c33f76e34f`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-4df8b5dca435e10b4af6"></a>

**90° CCW: unverified** — `in_game_save_reload-4df8b5dca435e10b4af6`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-0fa702a194362fff1761"></a>

**180° CCW: unverified** — `in_game_save_reload-0fa702a194362fff1761`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-0821a24e8076663aefb3"></a>

**270° CCW: unverified** — `in_game_save_reload-0821a24e8076663aefb3`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 40 cases; unverified: 40</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-15-out; entry: channel-01-in; exit: channel-15-out | — | <a href="#case-in_game_route_query-1fa520b339b7d034ab00">[ ] unverified</a> | <a href="#case-in_game_route_query-2a3476377c7a91f641aa">[ ] unverified</a> | <a href="#case-in_game_route_query-adb38f5f7441fef31dce">[ ] unverified</a> | <a href="#case-in_game_route_query-106992a9fb52c0639f9e">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-11-out; entry: channel-02-in; exit: channel-11-out | — | <a href="#case-in_game_route_query-f28046d5ff0529f3997b">[ ] unverified</a> | <a href="#case-in_game_route_query-2584c25dcbf3d2895978">[ ] unverified</a> | <a href="#case-in_game_route_query-e597ee5d2b0c0f8533c5">[ ] unverified</a> | <a href="#case-in_game_route_query-2a48920e1c78c82cd160">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-14-out; entry: channel-03-in; exit: channel-14-out | — | <a href="#case-in_game_route_query-c24da3d8497415fa6c36">[ ] unverified</a> | <a href="#case-in_game_route_query-dff719ed02c72e24d6dd">[ ] unverified</a> | <a href="#case-in_game_route_query-dff20dc97fac6aabfb4b">[ ] unverified</a> | <a href="#case-in_game_route_query-b3596d59672f1d83e05a">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-13-out; entry: channel-04-in; exit: channel-13-out | — | <a href="#case-in_game_route_query-051d0e4b86a7b9c82763">[ ] unverified</a> | <a href="#case-in_game_route_query-191a098407f650ef36ea">[ ] unverified</a> | <a href="#case-in_game_route_query-539c2d15f2c0aa02a070">[ ] unverified</a> | <a href="#case-in_game_route_query-1fc5ac63adcff7c2b1cc">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-12-out; entry: channel-05-in; exit: channel-12-out | — | <a href="#case-in_game_route_query-e96d644ebd2be7589764">[ ] unverified</a> | <a href="#case-in_game_route_query-3b8916bebb0a1b5661e5">[ ] unverified</a> | <a href="#case-in_game_route_query-c7c69a440ef2dc8fb94f">[ ] unverified</a> | <a href="#case-in_game_route_query-372051e87a8e97c62c3c">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-06-in>channel-20-out; entry: channel-06-in; exit: channel-20-out | — | <a href="#case-in_game_route_query-6becdf74122ba4f58f57">[ ] unverified</a> | <a href="#case-in_game_route_query-739307b770a162cf0fe4">[ ] unverified</a> | <a href="#case-in_game_route_query-ed7873dbac223184b9c5">[ ] unverified</a> | <a href="#case-in_game_route_query-9620d463f635e4090491">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-07-in>channel-19-out; entry: channel-07-in; exit: channel-19-out | — | <a href="#case-in_game_route_query-e648234c4e6f689eb43d">[ ] unverified</a> | <a href="#case-in_game_route_query-478664bfd260cc028e61">[ ] unverified</a> | <a href="#case-in_game_route_query-0fe631cc75839d1c422a">[ ] unverified</a> | <a href="#case-in_game_route_query-82d6e1c6569f7295d40b">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out | — | <a href="#case-in_game_route_query-616ebaa1590f2df822b3">[ ] unverified</a> | <a href="#case-in_game_route_query-01f6f4a00b0c2471b899">[ ] unverified</a> | <a href="#case-in_game_route_query-f60fbe114cb3fc1af62d">[ ] unverified</a> | <a href="#case-in_game_route_query-27a04248f8bb3bbc6e18">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-09-in>channel-17-out; entry: channel-09-in; exit: channel-17-out | — | <a href="#case-in_game_route_query-0d87f34c9b86cb44db24">[ ] unverified</a> | <a href="#case-in_game_route_query-cd5ab6d4d7b74bc9ad5c">[ ] unverified</a> | <a href="#case-in_game_route_query-66dc55b75512fc37babb">[ ] unverified</a> | <a href="#case-in_game_route_query-4050e7374ba354f8b38e">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out | — | <a href="#case-in_game_route_query-29bedbdf30e3256c884f">[ ] unverified</a> | <a href="#case-in_game_route_query-696fb55ce622feab97d7">[ ] unverified</a> | <a href="#case-in_game_route_query-371f26ed5b1173f84870">[ ] unverified</a> | <a href="#case-in_game_route_query-9d63aafaeea36dd1349f">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-01-in>channel-15-out; entry: channel-01-in; exit: channel-15-out</summary>

<a id="case-in_game_route_query-1fa520b339b7d034ab00"></a>

**0° CCW: unverified** — `in_game_route_query-1fa520b339b7d034ab00`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-15-out; entry: channel-01-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_route_query-2a3476377c7a91f641aa"></a>

**90° CCW: unverified** — `in_game_route_query-2a3476377c7a91f641aa`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-15-out; entry: channel-01-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_route_query-adb38f5f7441fef31dce"></a>

**180° CCW: unverified** — `in_game_route_query-adb38f5f7441fef31dce`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-15-out; entry: channel-01-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_route_query-106992a9fb52c0639f9e"></a>

**270° CCW: unverified** — `in_game_route_query-106992a9fb52c0639f9e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-15-out; entry: channel-01-in; exit: channel-15-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-02-in>channel-11-out; entry: channel-02-in; exit: channel-11-out</summary>

<a id="case-in_game_route_query-f28046d5ff0529f3997b"></a>

**0° CCW: unverified** — `in_game_route_query-f28046d5ff0529f3997b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-11-out; entry: channel-02-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_route_query-2584c25dcbf3d2895978"></a>

**90° CCW: unverified** — `in_game_route_query-2584c25dcbf3d2895978`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-11-out; entry: channel-02-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_route_query-e597ee5d2b0c0f8533c5"></a>

**180° CCW: unverified** — `in_game_route_query-e597ee5d2b0c0f8533c5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-11-out; entry: channel-02-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_route_query-2a48920e1c78c82cd160"></a>

**270° CCW: unverified** — `in_game_route_query-2a48920e1c78c82cd160`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-11-out; entry: channel-02-in; exit: channel-11-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-03-in>channel-14-out; entry: channel-03-in; exit: channel-14-out</summary>

<a id="case-in_game_route_query-c24da3d8497415fa6c36"></a>

**0° CCW: unverified** — `in_game_route_query-c24da3d8497415fa6c36`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-14-out; entry: channel-03-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_route_query-dff719ed02c72e24d6dd"></a>

**90° CCW: unverified** — `in_game_route_query-dff719ed02c72e24d6dd`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-14-out; entry: channel-03-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_route_query-dff20dc97fac6aabfb4b"></a>

**180° CCW: unverified** — `in_game_route_query-dff20dc97fac6aabfb4b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-14-out; entry: channel-03-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_route_query-b3596d59672f1d83e05a"></a>

**270° CCW: unverified** — `in_game_route_query-b3596d59672f1d83e05a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-14-out; entry: channel-03-in; exit: channel-14-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-04-in>channel-13-out; entry: channel-04-in; exit: channel-13-out</summary>

<a id="case-in_game_route_query-051d0e4b86a7b9c82763"></a>

**0° CCW: unverified** — `in_game_route_query-051d0e4b86a7b9c82763`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-13-out; entry: channel-04-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_route_query-191a098407f650ef36ea"></a>

**90° CCW: unverified** — `in_game_route_query-191a098407f650ef36ea`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-13-out; entry: channel-04-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_route_query-539c2d15f2c0aa02a070"></a>

**180° CCW: unverified** — `in_game_route_query-539c2d15f2c0aa02a070`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-13-out; entry: channel-04-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_route_query-1fc5ac63adcff7c2b1cc"></a>

**270° CCW: unverified** — `in_game_route_query-1fc5ac63adcff7c2b1cc`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-13-out; entry: channel-04-in; exit: channel-13-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-05-in>channel-12-out; entry: channel-05-in; exit: channel-12-out</summary>

<a id="case-in_game_route_query-e96d644ebd2be7589764"></a>

**0° CCW: unverified** — `in_game_route_query-e96d644ebd2be7589764`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-12-out; entry: channel-05-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_route_query-3b8916bebb0a1b5661e5"></a>

**90° CCW: unverified** — `in_game_route_query-3b8916bebb0a1b5661e5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-12-out; entry: channel-05-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_route_query-c7c69a440ef2dc8fb94f"></a>

**180° CCW: unverified** — `in_game_route_query-c7c69a440ef2dc8fb94f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-12-out; entry: channel-05-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_route_query-372051e87a8e97c62c3c"></a>

**270° CCW: unverified** — `in_game_route_query-372051e87a8e97c62c3c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-12-out; entry: channel-05-in; exit: channel-12-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-06-in>channel-20-out; entry: channel-06-in; exit: channel-20-out</summary>

<a id="case-in_game_route_query-6becdf74122ba4f58f57"></a>

**0° CCW: unverified** — `in_game_route_query-6becdf74122ba4f58f57`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-20-out; entry: channel-06-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_route_query-739307b770a162cf0fe4"></a>

**90° CCW: unverified** — `in_game_route_query-739307b770a162cf0fe4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-20-out; entry: channel-06-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_route_query-ed7873dbac223184b9c5"></a>

**180° CCW: unverified** — `in_game_route_query-ed7873dbac223184b9c5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-20-out; entry: channel-06-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_route_query-9620d463f635e4090491"></a>

**270° CCW: unverified** — `in_game_route_query-9620d463f635e4090491`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-20-out; entry: channel-06-in; exit: channel-20-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-07-in>channel-19-out; entry: channel-07-in; exit: channel-19-out</summary>

<a id="case-in_game_route_query-e648234c4e6f689eb43d"></a>

**0° CCW: unverified** — `in_game_route_query-e648234c4e6f689eb43d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-19-out; entry: channel-07-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_route_query-478664bfd260cc028e61"></a>

**90° CCW: unverified** — `in_game_route_query-478664bfd260cc028e61`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-19-out; entry: channel-07-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_route_query-0fe631cc75839d1c422a"></a>

**180° CCW: unverified** — `in_game_route_query-0fe631cc75839d1c422a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-19-out; entry: channel-07-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_route_query-82d6e1c6569f7295d40b"></a>

**270° CCW: unverified** — `in_game_route_query-82d6e1c6569f7295d40b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-19-out; entry: channel-07-in; exit: channel-19-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out</summary>

<a id="case-in_game_route_query-616ebaa1590f2df822b3"></a>

**0° CCW: unverified** — `in_game_route_query-616ebaa1590f2df822b3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_route_query-01f6f4a00b0c2471b899"></a>

**90° CCW: unverified** — `in_game_route_query-01f6f4a00b0c2471b899`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_route_query-f60fbe114cb3fc1af62d"></a>

**180° CCW: unverified** — `in_game_route_query-f60fbe114cb3fc1af62d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_route_query-27a04248f8bb3bbc6e18"></a>

**270° CCW: unverified** — `in_game_route_query-27a04248f8bb3bbc6e18`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-09-in>channel-17-out; entry: channel-09-in; exit: channel-17-out</summary>

<a id="case-in_game_route_query-0d87f34c9b86cb44db24"></a>

**0° CCW: unverified** — `in_game_route_query-0d87f34c9b86cb44db24`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-17-out; entry: channel-09-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_route_query-cd5ab6d4d7b74bc9ad5c"></a>

**90° CCW: unverified** — `in_game_route_query-cd5ab6d4d7b74bc9ad5c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-17-out; entry: channel-09-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_route_query-66dc55b75512fc37babb"></a>

**180° CCW: unverified** — `in_game_route_query-66dc55b75512fc37babb`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-17-out; entry: channel-09-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_route_query-4050e7374ba354f8b38e"></a>

**270° CCW: unverified** — `in_game_route_query-4050e7374ba354f8b38e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-17-out; entry: channel-09-in; exit: channel-17-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out</summary>

<a id="case-in_game_route_query-29bedbdf30e3256c884f"></a>

**0° CCW: unverified** — `in_game_route_query-29bedbdf30e3256c884f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_route_query-696fb55ce622feab97d7"></a>

**90° CCW: unverified** — `in_game_route_query-696fb55ce622feab97d7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_route_query-371f26ed5b1173f84870"></a>

**180° CCW: unverified** — `in_game_route_query-371f26ed5b1173f84870`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_route_query-9d63aafaeea36dd1349f"></a>

**270° CCW: unverified** — `in_game_route_query-9d63aafaeea36dd1349f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 40 cases; unverified: 40</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-15-out; entry: channel-01-in; exit: channel-15-out | — | <a href="#case-in_game_visible_travel-1fa520b339b7d034ab00">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2a3476377c7a91f641aa">[ ] unverified</a> | <a href="#case-in_game_visible_travel-adb38f5f7441fef31dce">[ ] unverified</a> | <a href="#case-in_game_visible_travel-106992a9fb52c0639f9e">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-11-out; entry: channel-02-in; exit: channel-11-out | — | <a href="#case-in_game_visible_travel-f28046d5ff0529f3997b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2584c25dcbf3d2895978">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e597ee5d2b0c0f8533c5">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2a48920e1c78c82cd160">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-14-out; entry: channel-03-in; exit: channel-14-out | — | <a href="#case-in_game_visible_travel-c24da3d8497415fa6c36">[ ] unverified</a> | <a href="#case-in_game_visible_travel-dff719ed02c72e24d6dd">[ ] unverified</a> | <a href="#case-in_game_visible_travel-dff20dc97fac6aabfb4b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b3596d59672f1d83e05a">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-13-out; entry: channel-04-in; exit: channel-13-out | — | <a href="#case-in_game_visible_travel-051d0e4b86a7b9c82763">[ ] unverified</a> | <a href="#case-in_game_visible_travel-191a098407f650ef36ea">[ ] unverified</a> | <a href="#case-in_game_visible_travel-539c2d15f2c0aa02a070">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1fc5ac63adcff7c2b1cc">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-12-out; entry: channel-05-in; exit: channel-12-out | — | <a href="#case-in_game_visible_travel-e96d644ebd2be7589764">[ ] unverified</a> | <a href="#case-in_game_visible_travel-3b8916bebb0a1b5661e5">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c7c69a440ef2dc8fb94f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-372051e87a8e97c62c3c">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-06-in>channel-20-out; entry: channel-06-in; exit: channel-20-out | — | <a href="#case-in_game_visible_travel-6becdf74122ba4f58f57">[ ] unverified</a> | <a href="#case-in_game_visible_travel-739307b770a162cf0fe4">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ed7873dbac223184b9c5">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9620d463f635e4090491">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-07-in>channel-19-out; entry: channel-07-in; exit: channel-19-out | — | <a href="#case-in_game_visible_travel-e648234c4e6f689eb43d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-478664bfd260cc028e61">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0fe631cc75839d1c422a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-82d6e1c6569f7295d40b">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out | — | <a href="#case-in_game_visible_travel-616ebaa1590f2df822b3">[ ] unverified</a> | <a href="#case-in_game_visible_travel-01f6f4a00b0c2471b899">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f60fbe114cb3fc1af62d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-27a04248f8bb3bbc6e18">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-09-in>channel-17-out; entry: channel-09-in; exit: channel-17-out | — | <a href="#case-in_game_visible_travel-0d87f34c9b86cb44db24">[ ] unverified</a> | <a href="#case-in_game_visible_travel-cd5ab6d4d7b74bc9ad5c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-66dc55b75512fc37babb">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4050e7374ba354f8b38e">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out | — | <a href="#case-in_game_visible_travel-29bedbdf30e3256c884f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-696fb55ce622feab97d7">[ ] unverified</a> | <a href="#case-in_game_visible_travel-371f26ed5b1173f84870">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9d63aafaeea36dd1349f">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-01-in>channel-15-out; entry: channel-01-in; exit: channel-15-out</summary>

<a id="case-in_game_visible_travel-1fa520b339b7d034ab00"></a>

**0° CCW: unverified** — `in_game_visible_travel-1fa520b339b7d034ab00`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-15-out; entry: channel-01-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_visible_travel-2a3476377c7a91f641aa"></a>

**90° CCW: unverified** — `in_game_visible_travel-2a3476377c7a91f641aa`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-15-out; entry: channel-01-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_visible_travel-adb38f5f7441fef31dce"></a>

**180° CCW: unverified** — `in_game_visible_travel-adb38f5f7441fef31dce`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-15-out; entry: channel-01-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_visible_travel-106992a9fb52c0639f9e"></a>

**270° CCW: unverified** — `in_game_visible_travel-106992a9fb52c0639f9e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-15-out; entry: channel-01-in; exit: channel-15-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-02-in>channel-11-out; entry: channel-02-in; exit: channel-11-out</summary>

<a id="case-in_game_visible_travel-f28046d5ff0529f3997b"></a>

**0° CCW: unverified** — `in_game_visible_travel-f28046d5ff0529f3997b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-11-out; entry: channel-02-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_visible_travel-2584c25dcbf3d2895978"></a>

**90° CCW: unverified** — `in_game_visible_travel-2584c25dcbf3d2895978`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-11-out; entry: channel-02-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_visible_travel-e597ee5d2b0c0f8533c5"></a>

**180° CCW: unverified** — `in_game_visible_travel-e597ee5d2b0c0f8533c5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-11-out; entry: channel-02-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_visible_travel-2a48920e1c78c82cd160"></a>

**270° CCW: unverified** — `in_game_visible_travel-2a48920e1c78c82cd160`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-11-out; entry: channel-02-in; exit: channel-11-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-03-in>channel-14-out; entry: channel-03-in; exit: channel-14-out</summary>

<a id="case-in_game_visible_travel-c24da3d8497415fa6c36"></a>

**0° CCW: unverified** — `in_game_visible_travel-c24da3d8497415fa6c36`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-14-out; entry: channel-03-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_visible_travel-dff719ed02c72e24d6dd"></a>

**90° CCW: unverified** — `in_game_visible_travel-dff719ed02c72e24d6dd`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-14-out; entry: channel-03-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_visible_travel-dff20dc97fac6aabfb4b"></a>

**180° CCW: unverified** — `in_game_visible_travel-dff20dc97fac6aabfb4b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-14-out; entry: channel-03-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_visible_travel-b3596d59672f1d83e05a"></a>

**270° CCW: unverified** — `in_game_visible_travel-b3596d59672f1d83e05a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-14-out; entry: channel-03-in; exit: channel-14-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-04-in>channel-13-out; entry: channel-04-in; exit: channel-13-out</summary>

<a id="case-in_game_visible_travel-051d0e4b86a7b9c82763"></a>

**0° CCW: unverified** — `in_game_visible_travel-051d0e4b86a7b9c82763`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-13-out; entry: channel-04-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_visible_travel-191a098407f650ef36ea"></a>

**90° CCW: unverified** — `in_game_visible_travel-191a098407f650ef36ea`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-13-out; entry: channel-04-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_visible_travel-539c2d15f2c0aa02a070"></a>

**180° CCW: unverified** — `in_game_visible_travel-539c2d15f2c0aa02a070`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-13-out; entry: channel-04-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_visible_travel-1fc5ac63adcff7c2b1cc"></a>

**270° CCW: unverified** — `in_game_visible_travel-1fc5ac63adcff7c2b1cc`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-13-out; entry: channel-04-in; exit: channel-13-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-05-in>channel-12-out; entry: channel-05-in; exit: channel-12-out</summary>

<a id="case-in_game_visible_travel-e96d644ebd2be7589764"></a>

**0° CCW: unverified** — `in_game_visible_travel-e96d644ebd2be7589764`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-12-out; entry: channel-05-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_visible_travel-3b8916bebb0a1b5661e5"></a>

**90° CCW: unverified** — `in_game_visible_travel-3b8916bebb0a1b5661e5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-12-out; entry: channel-05-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_visible_travel-c7c69a440ef2dc8fb94f"></a>

**180° CCW: unverified** — `in_game_visible_travel-c7c69a440ef2dc8fb94f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-12-out; entry: channel-05-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_visible_travel-372051e87a8e97c62c3c"></a>

**270° CCW: unverified** — `in_game_visible_travel-372051e87a8e97c62c3c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-12-out; entry: channel-05-in; exit: channel-12-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-06-in>channel-20-out; entry: channel-06-in; exit: channel-20-out</summary>

<a id="case-in_game_visible_travel-6becdf74122ba4f58f57"></a>

**0° CCW: unverified** — `in_game_visible_travel-6becdf74122ba4f58f57`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-20-out; entry: channel-06-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_visible_travel-739307b770a162cf0fe4"></a>

**90° CCW: unverified** — `in_game_visible_travel-739307b770a162cf0fe4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-20-out; entry: channel-06-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_visible_travel-ed7873dbac223184b9c5"></a>

**180° CCW: unverified** — `in_game_visible_travel-ed7873dbac223184b9c5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-20-out; entry: channel-06-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_visible_travel-9620d463f635e4090491"></a>

**270° CCW: unverified** — `in_game_visible_travel-9620d463f635e4090491`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-20-out; entry: channel-06-in; exit: channel-20-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-07-in>channel-19-out; entry: channel-07-in; exit: channel-19-out</summary>

<a id="case-in_game_visible_travel-e648234c4e6f689eb43d"></a>

**0° CCW: unverified** — `in_game_visible_travel-e648234c4e6f689eb43d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-19-out; entry: channel-07-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_visible_travel-478664bfd260cc028e61"></a>

**90° CCW: unverified** — `in_game_visible_travel-478664bfd260cc028e61`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-19-out; entry: channel-07-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_visible_travel-0fe631cc75839d1c422a"></a>

**180° CCW: unverified** — `in_game_visible_travel-0fe631cc75839d1c422a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-19-out; entry: channel-07-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_visible_travel-82d6e1c6569f7295d40b"></a>

**270° CCW: unverified** — `in_game_visible_travel-82d6e1c6569f7295d40b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-19-out; entry: channel-07-in; exit: channel-19-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out</summary>

<a id="case-in_game_visible_travel-616ebaa1590f2df822b3"></a>

**0° CCW: unverified** — `in_game_visible_travel-616ebaa1590f2df822b3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_visible_travel-01f6f4a00b0c2471b899"></a>

**90° CCW: unverified** — `in_game_visible_travel-01f6f4a00b0c2471b899`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_visible_travel-f60fbe114cb3fc1af62d"></a>

**180° CCW: unverified** — `in_game_visible_travel-f60fbe114cb3fc1af62d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_visible_travel-27a04248f8bb3bbc6e18"></a>

**270° CCW: unverified** — `in_game_visible_travel-27a04248f8bb3bbc6e18`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-09-in>channel-17-out; entry: channel-09-in; exit: channel-17-out</summary>

<a id="case-in_game_visible_travel-0d87f34c9b86cb44db24"></a>

**0° CCW: unverified** — `in_game_visible_travel-0d87f34c9b86cb44db24`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-17-out; entry: channel-09-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_visible_travel-cd5ab6d4d7b74bc9ad5c"></a>

**90° CCW: unverified** — `in_game_visible_travel-cd5ab6d4d7b74bc9ad5c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-17-out; entry: channel-09-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_visible_travel-66dc55b75512fc37babb"></a>

**180° CCW: unverified** — `in_game_visible_travel-66dc55b75512fc37babb`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-17-out; entry: channel-09-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_visible_travel-4050e7374ba354f8b38e"></a>

**270° CCW: unverified** — `in_game_visible_travel-4050e7374ba354f8b38e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-17-out; entry: channel-09-in; exit: channel-17-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out</summary>

<a id="case-in_game_visible_travel-29bedbdf30e3256c884f"></a>

**0° CCW: unverified** — `in_game_visible_travel-29bedbdf30e3256c884f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_visible_travel-696fb55ce622feab97d7"></a>

**90° CCW: unverified** — `in_game_visible_travel-696fb55ce622feab97d7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_visible_travel-371f26ed5b1173f84870"></a>

**180° CCW: unverified** — `in_game_visible_travel-371f26ed5b1173f84870`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_visible_travel-9d63aafaeea36dd1349f"></a>

**270° CCW: unverified** — `in_game_visible_travel-9d63aafaeea36dd1349f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 360 cases; unverified: 360</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1e19317eb88c3c9b9aae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-afc9902b769c50aa3ff5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-53eb06b86597620a3dfb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2d29adc892e7237f6545">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c6087de923aaf5be3823">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5f787a28cc572aa3fb63">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1541f8172c66aa625537">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5ccb89060a3d9f1bdf7c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1d293b217f34f699af94">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-602ecf47c382982c2282">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6838083068899e6db5b1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aef1b60690b32534eb86">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2781924f8f9549b389ef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eef939b4450e18ade700">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8089ae192034260bb5bf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3454b174c92246b267a7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e18e21820a6767425c62">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9e3093f11c0f96e1deb9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a17f6e7db262a474b12b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e8dd36f177746cf2c759">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ceb9022d9c04387777e6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e422500e79a6f641b65a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-26fd2e363556aabd99a5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1fd894e45f154482bf3a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3abddb3b6785ba1d5457">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d46963cefb2994549d0a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-78418648c7d01a827ddc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5ce91b96a15b0a607e42">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3049cd6ca39c33b7f6e7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cbf212c3c7d4882304a3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-02b4836fb7d98cf91cbb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2320da9854178cb64e85">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1f3c9364a008be6e7f51">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9257f215ad565bcde986">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d37dca36ddeb8c780319">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ab03eacbb3a7908cc52a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-beaac1309ddbd009e9f2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b15a4ce71cdd6b5af419">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a6b54dacbae6e5e55dbd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-623663cae04e7724be14">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-12e30c98f69302a54128">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c2aae65a8ab527975935">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-91d5671fd06517f5aa43">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0fe9dc9d18e2a255be16">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-05f2c4aa2138dce9c28e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-714a9b10c51c2a2bd3ed">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-328dec7be73778a02c6e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b33a8269dbc1856edd92">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e0f4f033dbdcb5915cdf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-36b4bdd3afce7c70990a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f9a0653d86f92dfda680">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2103dda7e3e2569c6761">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e7a9b89b924ee50b2981">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3ffbcb6a9aec4a012c97">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5edbd459202756a3c7ff">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ca13b8aa56e07e3cf2c4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5c9d0955f81d8226a817">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7b088cc26dda648428fc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2abc6c030a5cd7b4617e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f8e0a0ee072e0a6656d9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cb4d80c2d0bf944e4175">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7a5f493424a8d1444957">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8fd2e44ad9de46609b89">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0a3de178a5001384ed73">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7f4ea71a24372d720b23">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0af8d6de53e10a617329">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-43884f14888c0edee4a5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ffb1cd8214b29484e1a7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8b0070642dd155edf0fb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fa15c04322f0ba32e296">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3687ec78fe1618f5464d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c49df4c5e3cbe114c60f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ec42db807cad000a383a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ba253204c56936f64566">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-70ec6e0dd156380a7676">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-64986bf5d85ca37a4439">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f9f9fe139944f70a85d5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-848b70045084fc2a46fd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fad6420e6ae74ece305d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8454fa00ea3e92033fb2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-705bb9ecb799f5dd49fe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b6175ac767a3057c2a23">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ed7ea903b955cd2d966f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6f841da3cd6840640c2c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a6a02fdfb9faab980a21">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-903e93da8bda912d1d80">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0e466fea0923aa521799">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dc64b106226ca275fa75">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1f481357e2bcc14133f9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7e04de8d257168cce3f1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bc02e163c88047c7cc57">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-23e72e23aa613936582f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d7d6095d6966fc47f687">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9ad5a15126f480cfee1b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6bde6d47499f9fb0fdcc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7c1f4c4dc44e61ac53bb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ac84551be725eb2eca26">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0dc2c98ee33baed947d1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bfdeb9acd270b61641a5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5ba2a23a722ec78c0c99">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-119b5fe658fe952cb707">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-74b465cbc2e045dde739">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fb898bc2d69334289149">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-07f2e5399bd1ca8799b4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2236d0763cd30bfb3e26">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-067e5cb5fbad8f5ee33d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ddf4e3ccd10f85972f89">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b2b1be08ab5bba2c1bae">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-363cd96f9801137cf988">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8d9933a545ba09c2203f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-374f88cfd838907cb681">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a78a6d77df7393f0dfbb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d4a3cbc4861dcc9b00cf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3936dc99876120fabd9d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-be0bdf0c1a0c6b630e46">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-69910ce97e36f45d090f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b222f748ad4042326d6a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8679c90bfc8302de6fb6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d329637006115fbb3b48">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b2121d83fb49a995c59e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5ee8cd717645d3554ae4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1f3772478f311565cafc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-92ccbefdf49404076658">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-de5f6e9ad99277522680">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c217b99c9b08561eca7e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3b4b847bcaf14aac33f4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cbf9e4d9bce762b06fce">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-22ec1bb77985f4c5069d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9aff43ccc7e363890fff">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-33bd76698aa20bd655e8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a1f595be449028422c46">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-66fcf2a326ca676cf038">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ab2c3e8b5e058c06531e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8f6acf68b313fb1a52c4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f525c9ade0cdb0be6801">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4cb29963e518a616a523">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2da18ec045e7b9828e6f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-20e0d921f230b18b23d4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-edc851c2c5954925127a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-36b48d8b2d6a5ec03758">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5800351aa8f2db29469c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1b9cfd720fca203de3d4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-48647277df72016e585a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-07654aab16c70d79b361">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7cd9f697abe3a4781ee4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3d1c98d51585df97a045">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7c2dad2207c6a0f954e7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dff159bf9a7344308d71">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b542d09c2577ae4da250">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d0a47a617e5b5c10fc62">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8c84485c672cc7ad89fa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ee8276c2dec2515bd8d7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-14b5f287aeef64137dbc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8e836107014b20f496f5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cfe9ff84af077c5b181d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d8b08a8baded41ac61a1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8582b3300a20544ecc84">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-63616c8123ddbaed1f53">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0518384faf865023c83c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3e37377888ff2be87898">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e958c35eba65c60e2838">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4e9a7f673c2c8f9a166e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b455a3932f4ada3655b7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-292d5e07b551345da245">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d6dc60c1ad6e4384e59d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a71b06d1374685709e1e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-67e1ebdb442a6f0f1d63">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-afbe69eae8c7c75a3ccd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ce5f39adcfd352c55f5c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e574a3ae2e1bfda1a321">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ae13415c211217d4dea4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e75a044bdfdd330b9fda">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7e4e8b76268eba35a640">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d96dff6a92d09bdb2548">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-248dbd2a6b9c490dacb4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-71c9f4bbb042589812fe">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c1f9ff5e2340fe03271a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2ae502fa4d1d7095a60f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-27f9e156481202b6841d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-18705a49f105e76418ad">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-20de0deb91457a7441f6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f9fec90152b9e8eb4a77">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d6c114c072d604780179">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-572c74e25839f40efd89">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-10ac1adb5581470143b4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b09ff6ef05f1fde5ba87">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5840fb642d68a94fea5b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-02eca90790cb34fb32d3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-117c29001974da1f2d40">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e2862ce01423ac8d3825">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8edbbfe9bfc4a201df32">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d4789a1716eefbbd180f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8d42a2cd65414a18311d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-58d828ae0a2f32b5d950">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d41c3c22e2182f945466">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d0358a3c877611bd9c7f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7206f4d09bea82636cb7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-75b3d329afce6e63fc82">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3a55ee24e09f7566f397">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-553832dd684136b021b4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a229aa4fdbbe8e2f5e78">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0ead3dd9d9feb7d81f19">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d0f38c9b249f76346609">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fc3d0ad7db1201159598">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ab06d5f5ffd6e60d0410">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-badd86565876a40fe8f7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aeaec9bcd3babe557f99">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a9efa58525bff8b43888">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-51063ac521bda54b89f8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-099d01520f09931dbcd3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4f320f046fae39c0a4c2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-df162d033e6c03529d49">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a14f8c68b430847472e8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e70b306c18410a6b4f18">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-06fbe969e4f589130a6e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eee8e41f70be160f6f57">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e6c21dd157beccc107ee">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b426d0ae772f10701c2b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f5ea31ff5ff4a55bb28b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-36532e4d549c86f6f9b4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a693f70432bd048c579a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b84957b2aa3ca03e6dd1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-670a351927c7f3d0da76">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-377e89250a64eeb8f812">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-70b1715ae1379c541398">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-da76252d439206b5c2da">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2a5282410dd55efa2609">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ffcbd4bba75bedaefeb1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a019ba45b7443c73633f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-69fe7255f69c60e9039e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4187dbf51bb4b37718cb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c423103e0cc5f906301e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4cbf1ae2e1fd08144792">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ec7537da7a281332cfbb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5a0dbbc2df2cea7a3a10">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e9ad47dc892b4c369702">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f400e0c746fe6219e612">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-05fa68bc786e0ddeea64">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7094b68204a26618788a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a5d828efecb0b8dfe095">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-45cdc8c145f615173c17">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a57eade8b88b7016a375">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d5a72917985591636295">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5a16f45bbde141cc002e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-270263c1fdc7ed04769e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a305345e7bcd32766044">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-59a46858beac0d6f5c91">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-316225ff84e73ff2a196">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d24ddeeb47fb3ed0c071">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c6cb65a9381232b4cc9e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fa75b526e3c462195c19">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-05ecd73d0933e4a51e37">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-36d37664c569038db2d7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e0a8e3322a9b784a914c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-51b140d06789937b736d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-48abc0ae2a1dc056ad6b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-22c56716f1d0ab2fa822">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-25b8fa74a144275a8787">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-822d849d5ad46d346774">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6115ea1f4b39a7c17ac1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5378e79bc92aae38bef3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-93201d419762b57f9d88">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a08cca8723a4b06a4a8f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-61074bd62f33ff5b9724">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-49acb456a4ef30a2c4f9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bc5edd4f209ecb72dcac">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3d35321bea2fd74e1fb4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4008034355224e811ce7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bbfb321e6abba462ad72">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7a2aab80df6c2bf294a9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-583a89985bc78a1ca14f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8c02d1b5a119ac45db51">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-317aa026d3b84a6c99f9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a233bd957f1e0675c4db">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-188df4e924c0dc83bd8b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-be0e603e4e94a8ed2bf9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cb910f345cded7f4ceb8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ef23cadc520175bdda50">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9a9b9c122fe296dfa14b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9ccf821cfa979943e12c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-821dd7831fbfaccb1645">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8634a2431ae2d7d00cc1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9274a5630f724db9efc7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bb1c04571248acc5fee0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8d31e79bb136c201d80c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-52761e4f8075f45df844">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2afedc92006f1a96a180">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7a70d4a04b865bec74fb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b24e81414eaa779aad65">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3c36b196c27b7614efeb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c4dda14d30d618e4bacc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0e4299c86e3f8c205f15">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7d55e18b1fa1e70e1beb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-669e57ae04bcade76190">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-de0cbaebbbd6f0e12af0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8cf455e6681a0c28c1f0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-01a1d7c04707bb42ec78">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-50e5c7cba47700d498c9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c27389bb6240dda63956">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ee3dfaaaeac26bd885c1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fad920843a69c051878e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b41a83e32be517b7e041">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6db5ba0b16deb89c985a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cd034e541f8ba52f3259">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d43a2f8478548ab723f4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8c8e682b34e2b9e29ccc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-87c1443f536057a3fa85">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6328f54ab03a5014552a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7c7504538e0b4f5d659f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eb5e6ab2570bf46b0280">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c10cc1a252fbacbdf0a1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5ff304824384171ad891">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9894437b1ed0e090ab47">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f02ffbbb5bf77146699c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b672e6da36b69cf7a77e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c197994d054a03c0bf97">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-903337fe6ec2f4262ead">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dab23f79501c833d65ba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ebf1527efb5c8a825c09">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1adb691e450a452937aa">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7da31cd73fcddcb40dfa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-45f683148a50d856f201">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8c49d5094cb181650a40">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c9faf52b2efae4d85442">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-53a63ae6100ad7538785">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4ca6ba0788e997f807d6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b82bedabe9c34b271d71">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dccfb9d01f51df6d6c35">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-73514cdb84e2651b8da0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a3426f8fbfc3f6190d3d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fd76c4eb5a6b9c593df0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-45ddfc45c19bc7a529be">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-62dab4c6713f14f5cddf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1e2f4f7cc9d28889c858">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9872b7069a3b6ad333a3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-28bc28dfbac2479ac312">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a26b25547fa3db4357ba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e12612b46b7ddc276462">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-067c3e064989e95bc088">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-650e31041cc170a1651d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-55abd261f2fa1777f717">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0127099ecc551b17044a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fe75dcdba23de8828c44">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0bf62c70aea04dff3ee1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-301c1e45879bfc4ed4a9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c178189ee4dfe4e076f7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ba00bdb70f09198cbb6e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-33690caeb11d2aee5ad8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ba74c7356eadb327a8b4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a39af13291ecb677d53d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3c4e5ecd51feddef37ca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-27fce84750883fae0e82">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7479c5e92a3dcff3a867">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-850dbcd916be10eaf65a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5af2fb676acf6f8ccf1c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3c6bc52c07a4d9650e89">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a00978272f3249571eb7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-96290276ea76e6713a10">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e9172d2991fad0e90650">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-92e75c1c61df30d97dc7">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1e19317eb88c3c9b9aae"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1e19317eb88c3c9b9aae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-afc9902b769c50aa3ff5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-afc9902b769c50aa3ff5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-53eb06b86597620a3dfb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-53eb06b86597620a3dfb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2d29adc892e7237f6545"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2d29adc892e7237f6545`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c6087de923aaf5be3823"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c6087de923aaf5be3823`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5f787a28cc572aa3fb63"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5f787a28cc572aa3fb63`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1541f8172c66aa625537"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1541f8172c66aa625537`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5ccb89060a3d9f1bdf7c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5ccb89060a3d9f1bdf7c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1d293b217f34f699af94"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1d293b217f34f699af94`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-602ecf47c382982c2282"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-602ecf47c382982c2282`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6838083068899e6db5b1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6838083068899e6db5b1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aef1b60690b32534eb86"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-aef1b60690b32534eb86`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2781924f8f9549b389ef"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2781924f8f9549b389ef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eef939b4450e18ade700"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-eef939b4450e18ade700`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8089ae192034260bb5bf"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8089ae192034260bb5bf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3454b174c92246b267a7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3454b174c92246b267a7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e18e21820a6767425c62"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e18e21820a6767425c62`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9e3093f11c0f96e1deb9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9e3093f11c0f96e1deb9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a17f6e7db262a474b12b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a17f6e7db262a474b12b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e8dd36f177746cf2c759"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e8dd36f177746cf2c759`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ceb9022d9c04387777e6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ceb9022d9c04387777e6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e422500e79a6f641b65a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e422500e79a6f641b65a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-26fd2e363556aabd99a5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-26fd2e363556aabd99a5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1fd894e45f154482bf3a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1fd894e45f154482bf3a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3abddb3b6785ba1d5457"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3abddb3b6785ba1d5457`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d46963cefb2994549d0a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d46963cefb2994549d0a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-78418648c7d01a827ddc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-78418648c7d01a827ddc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5ce91b96a15b0a607e42"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5ce91b96a15b0a607e42`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3049cd6ca39c33b7f6e7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3049cd6ca39c33b7f6e7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cbf212c3c7d4882304a3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cbf212c3c7d4882304a3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-02b4836fb7d98cf91cbb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-02b4836fb7d98cf91cbb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2320da9854178cb64e85"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2320da9854178cb64e85`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1f3c9364a008be6e7f51"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1f3c9364a008be6e7f51`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9257f215ad565bcde986"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9257f215ad565bcde986`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d37dca36ddeb8c780319"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d37dca36ddeb8c780319`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ab03eacbb3a7908cc52a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ab03eacbb3a7908cc52a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-beaac1309ddbd009e9f2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-beaac1309ddbd009e9f2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b15a4ce71cdd6b5af419"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b15a4ce71cdd6b5af419`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a6b54dacbae6e5e55dbd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a6b54dacbae6e5e55dbd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-623663cae04e7724be14"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-623663cae04e7724be14`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-12e30c98f69302a54128"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-12e30c98f69302a54128`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c2aae65a8ab527975935"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c2aae65a8ab527975935`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-91d5671fd06517f5aa43"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-91d5671fd06517f5aa43`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0fe9dc9d18e2a255be16"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0fe9dc9d18e2a255be16`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-05f2c4aa2138dce9c28e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-05f2c4aa2138dce9c28e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-714a9b10c51c2a2bd3ed"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-714a9b10c51c2a2bd3ed`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-328dec7be73778a02c6e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-328dec7be73778a02c6e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b33a8269dbc1856edd92"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b33a8269dbc1856edd92`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e0f4f033dbdcb5915cdf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e0f4f033dbdcb5915cdf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-36b4bdd3afce7c70990a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-36b4bdd3afce7c70990a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f9a0653d86f92dfda680"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f9a0653d86f92dfda680`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2103dda7e3e2569c6761"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2103dda7e3e2569c6761`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e7a9b89b924ee50b2981"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e7a9b89b924ee50b2981`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3ffbcb6a9aec4a012c97"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3ffbcb6a9aec4a012c97`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5edbd459202756a3c7ff"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5edbd459202756a3c7ff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ca13b8aa56e07e3cf2c4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ca13b8aa56e07e3cf2c4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5c9d0955f81d8226a817"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5c9d0955f81d8226a817`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7b088cc26dda648428fc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7b088cc26dda648428fc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2abc6c030a5cd7b4617e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2abc6c030a5cd7b4617e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f8e0a0ee072e0a6656d9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f8e0a0ee072e0a6656d9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cb4d80c2d0bf944e4175"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cb4d80c2d0bf944e4175`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7a5f493424a8d1444957"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7a5f493424a8d1444957`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8fd2e44ad9de46609b89"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8fd2e44ad9de46609b89`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0a3de178a5001384ed73"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0a3de178a5001384ed73`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7f4ea71a24372d720b23"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7f4ea71a24372d720b23`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0af8d6de53e10a617329"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0af8d6de53e10a617329`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-43884f14888c0edee4a5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-43884f14888c0edee4a5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ffb1cd8214b29484e1a7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ffb1cd8214b29484e1a7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8b0070642dd155edf0fb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8b0070642dd155edf0fb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fa15c04322f0ba32e296"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fa15c04322f0ba32e296`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3687ec78fe1618f5464d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3687ec78fe1618f5464d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c49df4c5e3cbe114c60f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c49df4c5e3cbe114c60f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ec42db807cad000a383a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ec42db807cad000a383a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ba253204c56936f64566"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ba253204c56936f64566`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-70ec6e0dd156380a7676"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-70ec6e0dd156380a7676`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-64986bf5d85ca37a4439"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-64986bf5d85ca37a4439`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f9f9fe139944f70a85d5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f9f9fe139944f70a85d5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-848b70045084fc2a46fd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-848b70045084fc2a46fd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fad6420e6ae74ece305d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fad6420e6ae74ece305d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8454fa00ea3e92033fb2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8454fa00ea3e92033fb2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-705bb9ecb799f5dd49fe"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-705bb9ecb799f5dd49fe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b6175ac767a3057c2a23"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b6175ac767a3057c2a23`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ed7ea903b955cd2d966f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ed7ea903b955cd2d966f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6f841da3cd6840640c2c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6f841da3cd6840640c2c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a6a02fdfb9faab980a21"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a6a02fdfb9faab980a21`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-903e93da8bda912d1d80"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-903e93da8bda912d1d80`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0e466fea0923aa521799"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0e466fea0923aa521799`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dc64b106226ca275fa75"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dc64b106226ca275fa75`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1f481357e2bcc14133f9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1f481357e2bcc14133f9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7e04de8d257168cce3f1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7e04de8d257168cce3f1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bc02e163c88047c7cc57"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bc02e163c88047c7cc57`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-23e72e23aa613936582f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-23e72e23aa613936582f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d7d6095d6966fc47f687"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d7d6095d6966fc47f687`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9ad5a15126f480cfee1b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9ad5a15126f480cfee1b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6bde6d47499f9fb0fdcc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6bde6d47499f9fb0fdcc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7c1f4c4dc44e61ac53bb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7c1f4c4dc44e61ac53bb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ac84551be725eb2eca26"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ac84551be725eb2eca26`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0dc2c98ee33baed947d1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0dc2c98ee33baed947d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bfdeb9acd270b61641a5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bfdeb9acd270b61641a5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5ba2a23a722ec78c0c99"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5ba2a23a722ec78c0c99`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-119b5fe658fe952cb707"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-119b5fe658fe952cb707`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-74b465cbc2e045dde739"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-74b465cbc2e045dde739`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fb898bc2d69334289149"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fb898bc2d69334289149`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-07f2e5399bd1ca8799b4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-07f2e5399bd1ca8799b4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2236d0763cd30bfb3e26"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2236d0763cd30bfb3e26`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-067e5cb5fbad8f5ee33d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-067e5cb5fbad8f5ee33d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ddf4e3ccd10f85972f89"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ddf4e3ccd10f85972f89`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b2b1be08ab5bba2c1bae"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b2b1be08ab5bba2c1bae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-363cd96f9801137cf988"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-363cd96f9801137cf988`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8d9933a545ba09c2203f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8d9933a545ba09c2203f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-374f88cfd838907cb681"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-374f88cfd838907cb681`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a78a6d77df7393f0dfbb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a78a6d77df7393f0dfbb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d4a3cbc4861dcc9b00cf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d4a3cbc4861dcc9b00cf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3936dc99876120fabd9d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3936dc99876120fabd9d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-be0bdf0c1a0c6b630e46"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-be0bdf0c1a0c6b630e46`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-69910ce97e36f45d090f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-69910ce97e36f45d090f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b222f748ad4042326d6a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b222f748ad4042326d6a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8679c90bfc8302de6fb6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8679c90bfc8302de6fb6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d329637006115fbb3b48"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d329637006115fbb3b48`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b2121d83fb49a995c59e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b2121d83fb49a995c59e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5ee8cd717645d3554ae4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5ee8cd717645d3554ae4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1f3772478f311565cafc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1f3772478f311565cafc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-92ccbefdf49404076658"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-92ccbefdf49404076658`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-de5f6e9ad99277522680"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-de5f6e9ad99277522680`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c217b99c9b08561eca7e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c217b99c9b08561eca7e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3b4b847bcaf14aac33f4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3b4b847bcaf14aac33f4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cbf9e4d9bce762b06fce"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cbf9e4d9bce762b06fce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-22ec1bb77985f4c5069d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-22ec1bb77985f4c5069d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9aff43ccc7e363890fff"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9aff43ccc7e363890fff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-33bd76698aa20bd655e8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-33bd76698aa20bd655e8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a1f595be449028422c46"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a1f595be449028422c46`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-66fcf2a326ca676cf038"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-66fcf2a326ca676cf038`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ab2c3e8b5e058c06531e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ab2c3e8b5e058c06531e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8f6acf68b313fb1a52c4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8f6acf68b313fb1a52c4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f525c9ade0cdb0be6801"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f525c9ade0cdb0be6801`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4cb29963e518a616a523"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4cb29963e518a616a523`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2da18ec045e7b9828e6f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2da18ec045e7b9828e6f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-20e0d921f230b18b23d4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-20e0d921f230b18b23d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-edc851c2c5954925127a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-edc851c2c5954925127a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-36b48d8b2d6a5ec03758"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-36b48d8b2d6a5ec03758`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5800351aa8f2db29469c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5800351aa8f2db29469c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1b9cfd720fca203de3d4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1b9cfd720fca203de3d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-48647277df72016e585a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-48647277df72016e585a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-07654aab16c70d79b361"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-07654aab16c70d79b361`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7cd9f697abe3a4781ee4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7cd9f697abe3a4781ee4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3d1c98d51585df97a045"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3d1c98d51585df97a045`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7c2dad2207c6a0f954e7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7c2dad2207c6a0f954e7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dff159bf9a7344308d71"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dff159bf9a7344308d71`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b542d09c2577ae4da250"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b542d09c2577ae4da250`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d0a47a617e5b5c10fc62"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d0a47a617e5b5c10fc62`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8c84485c672cc7ad89fa"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8c84485c672cc7ad89fa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ee8276c2dec2515bd8d7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ee8276c2dec2515bd8d7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-14b5f287aeef64137dbc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-14b5f287aeef64137dbc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8e836107014b20f496f5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8e836107014b20f496f5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cfe9ff84af077c5b181d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cfe9ff84af077c5b181d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d8b08a8baded41ac61a1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d8b08a8baded41ac61a1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8582b3300a20544ecc84"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8582b3300a20544ecc84`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-63616c8123ddbaed1f53"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-63616c8123ddbaed1f53`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0518384faf865023c83c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0518384faf865023c83c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3e37377888ff2be87898"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3e37377888ff2be87898`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e958c35eba65c60e2838"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e958c35eba65c60e2838`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4e9a7f673c2c8f9a166e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4e9a7f673c2c8f9a166e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b455a3932f4ada3655b7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b455a3932f4ada3655b7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-292d5e07b551345da245"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-292d5e07b551345da245`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d6dc60c1ad6e4384e59d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d6dc60c1ad6e4384e59d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a71b06d1374685709e1e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a71b06d1374685709e1e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-67e1ebdb442a6f0f1d63"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-67e1ebdb442a6f0f1d63`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-afbe69eae8c7c75a3ccd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-afbe69eae8c7c75a3ccd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ce5f39adcfd352c55f5c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ce5f39adcfd352c55f5c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e574a3ae2e1bfda1a321"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e574a3ae2e1bfda1a321`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ae13415c211217d4dea4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ae13415c211217d4dea4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e75a044bdfdd330b9fda"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e75a044bdfdd330b9fda`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7e4e8b76268eba35a640"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7e4e8b76268eba35a640`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d96dff6a92d09bdb2548"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d96dff6a92d09bdb2548`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-248dbd2a6b9c490dacb4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-248dbd2a6b9c490dacb4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-71c9f4bbb042589812fe"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-71c9f4bbb042589812fe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c1f9ff5e2340fe03271a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c1f9ff5e2340fe03271a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2ae502fa4d1d7095a60f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2ae502fa4d1d7095a60f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-27f9e156481202b6841d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-27f9e156481202b6841d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-18705a49f105e76418ad"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-18705a49f105e76418ad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-20de0deb91457a7441f6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-20de0deb91457a7441f6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f9fec90152b9e8eb4a77"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f9fec90152b9e8eb4a77`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d6c114c072d604780179"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d6c114c072d604780179`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-572c74e25839f40efd89"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-572c74e25839f40efd89`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-10ac1adb5581470143b4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-10ac1adb5581470143b4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b09ff6ef05f1fde5ba87"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b09ff6ef05f1fde5ba87`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5840fb642d68a94fea5b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5840fb642d68a94fea5b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-02eca90790cb34fb32d3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-02eca90790cb34fb32d3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-117c29001974da1f2d40"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-117c29001974da1f2d40`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e2862ce01423ac8d3825"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e2862ce01423ac8d3825`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8edbbfe9bfc4a201df32"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8edbbfe9bfc4a201df32`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d4789a1716eefbbd180f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d4789a1716eefbbd180f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8d42a2cd65414a18311d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8d42a2cd65414a18311d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-58d828ae0a2f32b5d950"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-58d828ae0a2f32b5d950`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d41c3c22e2182f945466"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d41c3c22e2182f945466`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d0358a3c877611bd9c7f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d0358a3c877611bd9c7f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7206f4d09bea82636cb7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7206f4d09bea82636cb7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-75b3d329afce6e63fc82"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-75b3d329afce6e63fc82`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3a55ee24e09f7566f397"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3a55ee24e09f7566f397`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-553832dd684136b021b4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-553832dd684136b021b4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a229aa4fdbbe8e2f5e78"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a229aa4fdbbe8e2f5e78`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0ead3dd9d9feb7d81f19"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0ead3dd9d9feb7d81f19`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d0f38c9b249f76346609"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d0f38c9b249f76346609`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fc3d0ad7db1201159598"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fc3d0ad7db1201159598`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ab06d5f5ffd6e60d0410"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ab06d5f5ffd6e60d0410`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-badd86565876a40fe8f7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-badd86565876a40fe8f7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aeaec9bcd3babe557f99"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-aeaec9bcd3babe557f99`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a9efa58525bff8b43888"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a9efa58525bff8b43888`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-51063ac521bda54b89f8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-51063ac521bda54b89f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-099d01520f09931dbcd3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-099d01520f09931dbcd3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4f320f046fae39c0a4c2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4f320f046fae39c0a4c2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-df162d033e6c03529d49"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-df162d033e6c03529d49`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a14f8c68b430847472e8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a14f8c68b430847472e8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e70b306c18410a6b4f18"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e70b306c18410a6b4f18`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-06fbe969e4f589130a6e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-06fbe969e4f589130a6e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eee8e41f70be160f6f57"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-eee8e41f70be160f6f57`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e6c21dd157beccc107ee"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e6c21dd157beccc107ee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b426d0ae772f10701c2b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b426d0ae772f10701c2b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f5ea31ff5ff4a55bb28b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f5ea31ff5ff4a55bb28b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-36532e4d549c86f6f9b4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-36532e4d549c86f6f9b4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a693f70432bd048c579a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a693f70432bd048c579a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b84957b2aa3ca03e6dd1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b84957b2aa3ca03e6dd1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-670a351927c7f3d0da76"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-670a351927c7f3d0da76`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-377e89250a64eeb8f812"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-377e89250a64eeb8f812`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-70b1715ae1379c541398"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-70b1715ae1379c541398`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-da76252d439206b5c2da"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-da76252d439206b5c2da`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2a5282410dd55efa2609"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2a5282410dd55efa2609`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ffcbd4bba75bedaefeb1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ffcbd4bba75bedaefeb1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a019ba45b7443c73633f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a019ba45b7443c73633f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-69fe7255f69c60e9039e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-69fe7255f69c60e9039e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4187dbf51bb4b37718cb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4187dbf51bb4b37718cb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c423103e0cc5f906301e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c423103e0cc5f906301e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4cbf1ae2e1fd08144792"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4cbf1ae2e1fd08144792`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ec7537da7a281332cfbb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ec7537da7a281332cfbb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5a0dbbc2df2cea7a3a10"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5a0dbbc2df2cea7a3a10`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e9ad47dc892b4c369702"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e9ad47dc892b4c369702`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f400e0c746fe6219e612"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f400e0c746fe6219e612`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-05fa68bc786e0ddeea64"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-05fa68bc786e0ddeea64`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7094b68204a26618788a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7094b68204a26618788a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a5d828efecb0b8dfe095"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a5d828efecb0b8dfe095`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-45cdc8c145f615173c17"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-45cdc8c145f615173c17`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a57eade8b88b7016a375"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a57eade8b88b7016a375`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d5a72917985591636295"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d5a72917985591636295`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5a16f45bbde141cc002e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5a16f45bbde141cc002e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-270263c1fdc7ed04769e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-270263c1fdc7ed04769e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a305345e7bcd32766044"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a305345e7bcd32766044`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-59a46858beac0d6f5c91"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-59a46858beac0d6f5c91`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-316225ff84e73ff2a196"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-316225ff84e73ff2a196`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d24ddeeb47fb3ed0c071"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d24ddeeb47fb3ed0c071`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c6cb65a9381232b4cc9e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c6cb65a9381232b4cc9e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fa75b526e3c462195c19"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fa75b526e3c462195c19`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-05ecd73d0933e4a51e37"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-05ecd73d0933e4a51e37`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-36d37664c569038db2d7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-36d37664c569038db2d7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e0a8e3322a9b784a914c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e0a8e3322a9b784a914c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-51b140d06789937b736d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-51b140d06789937b736d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-48abc0ae2a1dc056ad6b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-48abc0ae2a1dc056ad6b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-22c56716f1d0ab2fa822"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-22c56716f1d0ab2fa822`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-25b8fa74a144275a8787"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-25b8fa74a144275a8787`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-822d849d5ad46d346774"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-822d849d5ad46d346774`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6115ea1f4b39a7c17ac1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6115ea1f4b39a7c17ac1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5378e79bc92aae38bef3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5378e79bc92aae38bef3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-93201d419762b57f9d88"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-93201d419762b57f9d88`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a08cca8723a4b06a4a8f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a08cca8723a4b06a4a8f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-61074bd62f33ff5b9724"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-61074bd62f33ff5b9724`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-49acb456a4ef30a2c4f9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-49acb456a4ef30a2c4f9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bc5edd4f209ecb72dcac"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bc5edd4f209ecb72dcac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3d35321bea2fd74e1fb4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3d35321bea2fd74e1fb4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4008034355224e811ce7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4008034355224e811ce7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bbfb321e6abba462ad72"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bbfb321e6abba462ad72`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7a2aab80df6c2bf294a9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7a2aab80df6c2bf294a9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-583a89985bc78a1ca14f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-583a89985bc78a1ca14f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8c02d1b5a119ac45db51"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8c02d1b5a119ac45db51`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-317aa026d3b84a6c99f9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-317aa026d3b84a6c99f9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a233bd957f1e0675c4db"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a233bd957f1e0675c4db`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-188df4e924c0dc83bd8b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-188df4e924c0dc83bd8b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-be0e603e4e94a8ed2bf9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-be0e603e4e94a8ed2bf9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cb910f345cded7f4ceb8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cb910f345cded7f4ceb8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ef23cadc520175bdda50"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ef23cadc520175bdda50`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9a9b9c122fe296dfa14b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9a9b9c122fe296dfa14b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9ccf821cfa979943e12c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9ccf821cfa979943e12c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-821dd7831fbfaccb1645"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-821dd7831fbfaccb1645`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8634a2431ae2d7d00cc1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8634a2431ae2d7d00cc1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9274a5630f724db9efc7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9274a5630f724db9efc7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bb1c04571248acc5fee0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bb1c04571248acc5fee0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8d31e79bb136c201d80c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8d31e79bb136c201d80c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-52761e4f8075f45df844"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-52761e4f8075f45df844`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2afedc92006f1a96a180"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2afedc92006f1a96a180`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7a70d4a04b865bec74fb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7a70d4a04b865bec74fb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b24e81414eaa779aad65"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b24e81414eaa779aad65`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3c36b196c27b7614efeb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3c36b196c27b7614efeb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c4dda14d30d618e4bacc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c4dda14d30d618e4bacc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0e4299c86e3f8c205f15"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0e4299c86e3f8c205f15`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7d55e18b1fa1e70e1beb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7d55e18b1fa1e70e1beb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-669e57ae04bcade76190"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-669e57ae04bcade76190`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-de0cbaebbbd6f0e12af0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-de0cbaebbbd6f0e12af0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8cf455e6681a0c28c1f0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8cf455e6681a0c28c1f0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-01a1d7c04707bb42ec78"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-01a1d7c04707bb42ec78`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-50e5c7cba47700d498c9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-50e5c7cba47700d498c9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c27389bb6240dda63956"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c27389bb6240dda63956`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ee3dfaaaeac26bd885c1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ee3dfaaaeac26bd885c1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fad920843a69c051878e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fad920843a69c051878e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b41a83e32be517b7e041"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b41a83e32be517b7e041`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6db5ba0b16deb89c985a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6db5ba0b16deb89c985a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cd034e541f8ba52f3259"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cd034e541f8ba52f3259`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d43a2f8478548ab723f4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d43a2f8478548ab723f4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8c8e682b34e2b9e29ccc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8c8e682b34e2b9e29ccc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-87c1443f536057a3fa85"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-87c1443f536057a3fa85`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6328f54ab03a5014552a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6328f54ab03a5014552a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7c7504538e0b4f5d659f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7c7504538e0b4f5d659f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eb5e6ab2570bf46b0280"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-eb5e6ab2570bf46b0280`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c10cc1a252fbacbdf0a1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c10cc1a252fbacbdf0a1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5ff304824384171ad891"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5ff304824384171ad891`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9894437b1ed0e090ab47"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9894437b1ed0e090ab47`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f02ffbbb5bf77146699c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f02ffbbb5bf77146699c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b672e6da36b69cf7a77e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b672e6da36b69cf7a77e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c197994d054a03c0bf97"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c197994d054a03c0bf97`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-903337fe6ec2f4262ead"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-903337fe6ec2f4262ead`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dab23f79501c833d65ba"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-dab23f79501c833d65ba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ebf1527efb5c8a825c09"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ebf1527efb5c8a825c09`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1adb691e450a452937aa"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1adb691e450a452937aa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7da31cd73fcddcb40dfa"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7da31cd73fcddcb40dfa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-45f683148a50d856f201"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-45f683148a50d856f201`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8c49d5094cb181650a40"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8c49d5094cb181650a40`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c9faf52b2efae4d85442"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c9faf52b2efae4d85442`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-53a63ae6100ad7538785"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-53a63ae6100ad7538785`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4ca6ba0788e997f807d6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4ca6ba0788e997f807d6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b82bedabe9c34b271d71"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b82bedabe9c34b271d71`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dccfb9d01f51df6d6c35"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dccfb9d01f51df6d6c35`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-73514cdb84e2651b8da0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-73514cdb84e2651b8da0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a3426f8fbfc3f6190d3d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a3426f8fbfc3f6190d3d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fd76c4eb5a6b9c593df0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fd76c4eb5a6b9c593df0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-45ddfc45c19bc7a529be"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-45ddfc45c19bc7a529be`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-62dab4c6713f14f5cddf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-62dab4c6713f14f5cddf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1e2f4f7cc9d28889c858"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1e2f4f7cc9d28889c858`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9872b7069a3b6ad333a3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9872b7069a3b6ad333a3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-28bc28dfbac2479ac312"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-28bc28dfbac2479ac312`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a26b25547fa3db4357ba"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a26b25547fa3db4357ba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e12612b46b7ddc276462"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e12612b46b7ddc276462`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-067c3e064989e95bc088"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-067c3e064989e95bc088`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-650e31041cc170a1651d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-650e31041cc170a1651d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-55abd261f2fa1777f717"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-55abd261f2fa1777f717`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0127099ecc551b17044a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0127099ecc551b17044a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fe75dcdba23de8828c44"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fe75dcdba23de8828c44`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0bf62c70aea04dff3ee1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0bf62c70aea04dff3ee1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-301c1e45879bfc4ed4a9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-301c1e45879bfc4ed4a9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c178189ee4dfe4e076f7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c178189ee4dfe4e076f7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ba00bdb70f09198cbb6e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ba00bdb70f09198cbb6e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-33690caeb11d2aee5ad8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-33690caeb11d2aee5ad8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ba74c7356eadb327a8b4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ba74c7356eadb327a8b4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a39af13291ecb677d53d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a39af13291ecb677d53d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3c4e5ecd51feddef37ca"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3c4e5ecd51feddef37ca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-27fce84750883fae0e82"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-27fce84750883fae0e82`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7479c5e92a3dcff3a867"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7479c5e92a3dcff3a867`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-850dbcd916be10eaf65a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-850dbcd916be10eaf65a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5af2fb676acf6f8ccf1c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5af2fb676acf6f8ccf1c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3c6bc52c07a4d9650e89"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3c6bc52c07a4d9650e89`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a00978272f3249571eb7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a00978272f3249571eb7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-96290276ea76e6713a10"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-96290276ea76e6713a10`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e9172d2991fad0e90650"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e9172d2991fad0e90650`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-92e75c1c61df30d97dc7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-92e75c1c61df30d97dc7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

This new type implements one functional part of the human-approved close parallel layout. It preserves the [frozen source proposal](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/TESTING.md#32-close-parallel-ramps-and-perpendicular-avenue-approaches) and leaves the retained R40 and compact assemblies available with their own resource identities and evidence. This piece's exact source is [piece.jsonc](piece.jsonc); the shared placement plan is [assembly.jsonc](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/assembly.jsonc).

The ground-mouth revision narrowed terminal asphalt while preserving the 6 m grade interfaces and its saved traffic routes. The later slip-lane revision lengthens the shoulder treatment and changes its access PATHs and white markings, while retaining all fifteen permanent types, the 31-cell union, and those narrow ground mouths. The earlier `ddrhw-parallel-diamond-parts-01` and `ddrhw-parallel-diamond-pedestrian-mouths-01` build identities retain their original scopes. The current revision uses `ddrhw-parallel-diamond-slip-lanes-02`; only its own matching saved-resource report can establish its software result.
