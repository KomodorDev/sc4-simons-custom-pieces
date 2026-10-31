---
title: "Testing: DD RHW-4 — L2 Exit Slip Lanes — Parallel"
summary: "Check this parallel component against its saved resources and retain separate human game observations."
audience: "contributors"
document_type: "reference"
---

# Testing: DD RHW-4 — L2 Exit Slip Lanes — Parallel

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

This record covers **ddrhw-parallel-upper-exit-slip**, used once as **P06** in the [parallel diamond](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/README.md). It has 2 occupied tiles in a 2 × 2 rectangle, the exact authored 0° reference at X1, Y2, and the functional levels described in the [piece guide](README.md#2-piece-and-placement). Saved native through routes, added access fragments, actual model support, material flags, physical joins, rotations, and adaptive resources where present have distinct software checks. Human appearance and travel observations remain separate.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `channel-11-out` | road / 1 / primary | out | [-8.0, -19.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `channel-01-in` | road / 1 / primary | in | [-8.0, -19.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `channel-12-out` | road / 1 / primary | out | [-8.0, -12.8, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `channel-02-in` | road / 1 / primary | in | [-8.0, -12.8, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `channel-03-in` | road / 1 / primary | in | [-6.194881, -8.0, 7.5]; [-0.16428872102218395, -0.9864122952117411]; 0.0 | `path-interface-321f3c2125b6bde219f3` |
| `channel-04-in` | road / 1 / primary | in | [-3.2, -8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `channel-13-out` | road / 1 / primary | out | [-3.2, -8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `channel-05-in` | road / 1 / primary | in | [3.2, -8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `channel-14-out` | road / 1 / primary | out | [3.2, -8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `channel-15-out` | road / 1 / primary | out | [8.0, -16.104467, 15.0]; [0.9404586044447987, 0.3399082425092716]; 0.0 | `path-interface-53fdf60e4bef5b46033e` |
| `channel-16-out` | road / 1 / primary | out | [8.0, -3.2, 7.5]; [-0.7071067811865475, -0.7071067811865477]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `channel-06-in` | road / 1 / primary | in | [8.0, -3.2, 15.0]; [0.7071067811865475, 0.7071067811865477]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `channel-17-out` | road / 1 / primary | out | [8.0, 3.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `channel-07-in` | road / 1 / primary | in | [8.0, 3.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `channel-08-in` | road / 1 / primary | in | [12.8, 8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `channel-18-out` | road / 1 / primary | out | [12.8, 8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `channel-09-in` | road / 1 / primary | in | [16.970563, -8.0, 12.866039]; [0.7071067811865476, 0.7071067811865476]; -0.282027457 | `path-interface-8f6f5a8624b510f03427` |
| `channel-10-in` | road / 1 / primary | in | [19.2, 8.0, 7.5]; [-0.7071067811865475, -0.7071067811865477]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `channel-19-out` | road / 1 / primary | out | [19.2, 8.0, 15.0]; [0.7071067811865475, 0.7071067811865477]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `channel-20-out` | road / 1 / primary | out | [24.0, -0.970563, 10.06235]; [0.7071067811865476, 0.7071067811865476]; -0.28202968 | `path-interface-18bc8998b3c8e8765f76` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `channel-01-in` → `channel-15-out` | primary |
| road | `channel-01-in` → `channel-14-out` | primary |
| road | `channel-02-in` → `channel-13-out` | primary |
| road | `channel-03-in` → `channel-12-out` | primary |
| road | `channel-04-in` → `channel-12-out` | primary |
| road | `channel-05-in` → `channel-11-out` | primary |
| road | `channel-06-in` → `channel-19-out` | primary |
| road | `channel-07-in` → `channel-18-out` | primary |
| road | `channel-08-in` → `channel-17-out` | primary |
| road | `channel-09-in` → `channel-20-out` | primary |
| road | `channel-10-in` → `channel-16-out` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `channel-01-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
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
| road / `channel-06-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-20-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
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

Prepare the [assembly's flat reference test area](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#2-test-setup), keep the camera north-up for placement, and use the exact occupied cells **(X2, Y2), (X1, Y1)**. The full core occupies 31 cells inside X1–X8 and Y1–Y8; the preserved drawing reference still shows X0–X9 and Y0–Y9. One tile is 16 m. Additional outside road approaches are separate from that core count.

## 3. Software checks

Run from the repository directory containing `custom-pieces/`. These commands inspect an existing build and its current source-bound connector records; they do not install anything, supply missing inputs, or approve a manual case. An absent or failing report is not a software pass.

```sh
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/ddrhw-parallel-diamond-slip-lanes-02
python3 -B custom-pieces/scp.py connectors check --domain highway --piece ddrhw-parallel-upper-exit-slip --build dist/ddrhw-parallel-diamond-slip-lanes-02
python3 -B custom-pieces/scp.py docs-check --piece ddrhw-parallel-upper-exit-slip
```

The [complete saved-assembly check](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#3-software-checks) checks this component in all fifteen placements, including physical model overhang and the traffic fragments owned by its neighbours. The ordinary build's manifest and verification report identify the actual measured resources. Retain every software failure with its source fingerprint; rerunning a renderer cannot repair it.

The current slip-lane revision changes the highway-shoulder traffic routes and their white markings within the existing construction footprint. Read outward from a through lane toward its ramp: each lower route has an 8 m smooth sideways taper and a 4 m straight shoulder section; each upper route has a 5 m taper and a 1 m straight shoulder section. The lower routes begin 6.788225 m farther upstream in already owned native highway tiles. The upper routes retain their previous outer ports because the unchanged 31-cell layout provides less shoulder distance there. These distances are measured along the straight highway axis. On-ramps follow the same profiles in reverse. The auxiliary-lane centre is 5.5 m from the highway axis; the checked 2.5 m-wide car corridor leaves 0.421875 m to the native barrier foot on the straight section. These are compressed experimental dimensions, not a real-road design standard. Native through PATHs, roadway outside the native 8 m deck edge, grades, ground terminals, permanent identifiers, and construction ownership retain their previous scope. Check the matching saved report before treating this source revision as verified. This component supplies highway or ramp geometry. The three ground components P01, P02, and P03 own the implemented adaptive Avenue pavement and retained pedestrian routes. Connecting this elevated component does not itself select a sidewalk appearance. Read the [actual mechanism and limits](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#3-software-checks).

The earlier narrow ground mouths are retained: each terminal keeps its 6 m grade join, narrows to 3.5 m over 3 m, and stays narrow through its R6 turn and Avenue joining collar. The ramp centreline crosses the retained pedestrian-route centreline 3.258752 m from the grade join, after that 3 m ground taper is complete. The asphalt footprint reaches the pedestrian route earlier, while the ground taper is still narrowing; this is the actual driveway crossing.

## 4. Game checks

1. Select this exact component through the assembly button, match P06 at **X1, Y2**, and confirm that the occupied preview squares match **(X2, Y2), (X1, Y1)** before clicking.
2. Place the full assembly using the order in its guide. Inspect this component's saved model from both opposing oblique views, and compare its real join with the neighbouring models; look for gaps, blocked barrier openings, misplaced supports, or a sudden pavement-colour patch.
3. Repeat fresh placement in the four distinct proper rotations. Rotate the camera separately after placement, because camera movement and a newly rotated piece test different things.
4. For an adaptive Avenue cell, connect ordinary Avenue outside the core, add nearby development, and compare its pavement variant with the neighbouring Avenue. Connecting the Avenue alone does not select the developed pavement appearance. Inspect both narrow driveway crossings, then check pedestrian Route Query and visible walking separately; a sidewalk image does not create a pedestrian PATH, and the crossing remains road asphalt. For a component without Avenue cells, inspect the neighbouring adaptive owners instead of expecting this piece to change pavement itself.
5. Run every required car and pedestrian journey listed by the exact matrix. Record Route Query and visible travel separately. Also confirm that every declared forbidden transfer stays unavailable; a visually clear road surface is not traffic evidence.
6. Inspect shadows, demolish the component, replace it, save the city, quit completely, and reload. Check that no temporary placement handle remains and that the component and its traffic neighbours remain correct.

Record only explicit observations through [the shared observation workflow](../../../../docs/TESTING.md), selecting **ddrhw-parallel-upper-exit-slip** and its exact current cases. No observation of the older adaptive probe, R40 diamond, or another rotation automatically approves this new component.

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
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-parallel-upper-exit-slip/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-parallel-upper-exit-slip/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-d6a5f833ba420944301f">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-d6a5f833ba420944301f"></a>

**General: unverified** — `software_resources-d6a5f833ba420944301f`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-d6a5f833ba420944301f">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-d6a5f833ba420944301f"></a>

**General: unverified** — `software_connectivity-d6a5f833ba420944301f`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-f375ad5bde0008a6816a">[ ] unverified</a> | <a href="#case-in_game_render-dc493e55bf39c8053152">[ ] unverified</a> | <a href="#case-in_game_render-ee2d92ca181f6c764191">[ ] unverified</a> | <a href="#case-in_game_render-0db55804c43c8cec9e14">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-f375ad5bde0008a6816a"></a>

**0° CCW: unverified** — `in_game_render-f375ad5bde0008a6816a`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-dc493e55bf39c8053152"></a>

**90° CCW: unverified** — `in_game_render-dc493e55bf39c8053152`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-ee2d92ca181f6c764191"></a>

**180° CCW: unverified** — `in_game_render-ee2d92ca181f6c764191`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-0db55804c43c8cec9e14"></a>

**270° CCW: unverified** — `in_game_render-0db55804c43c8cec9e14`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-f375ad5bde0008a6816a">[ ] unverified</a> | <a href="#case-in_game_placement-dc493e55bf39c8053152">[ ] unverified</a> | <a href="#case-in_game_placement-ee2d92ca181f6c764191">[ ] unverified</a> | <a href="#case-in_game_placement-0db55804c43c8cec9e14">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-f375ad5bde0008a6816a"></a>

**0° CCW: unverified** — `in_game_placement-f375ad5bde0008a6816a`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-dc493e55bf39c8053152"></a>

**90° CCW: unverified** — `in_game_placement-dc493e55bf39c8053152`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-ee2d92ca181f6c764191"></a>

**180° CCW: unverified** — `in_game_placement-ee2d92ca181f6c764191`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-0db55804c43c8cec9e14"></a>

**270° CCW: unverified** — `in_game_placement-0db55804c43c8cec9e14`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-f375ad5bde0008a6816a">[ ] unverified</a> | <a href="#case-in_game_demolition-dc493e55bf39c8053152">[ ] unverified</a> | <a href="#case-in_game_demolition-ee2d92ca181f6c764191">[ ] unverified</a> | <a href="#case-in_game_demolition-0db55804c43c8cec9e14">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-f375ad5bde0008a6816a"></a>

**0° CCW: unverified** — `in_game_demolition-f375ad5bde0008a6816a`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-dc493e55bf39c8053152"></a>

**90° CCW: unverified** — `in_game_demolition-dc493e55bf39c8053152`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-ee2d92ca181f6c764191"></a>

**180° CCW: unverified** — `in_game_demolition-ee2d92ca181f6c764191`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-0db55804c43c8cec9e14"></a>

**270° CCW: unverified** — `in_game_demolition-0db55804c43c8cec9e14`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-f375ad5bde0008a6816a">[ ] unverified</a> | <a href="#case-in_game_save_reload-dc493e55bf39c8053152">[ ] unverified</a> | <a href="#case-in_game_save_reload-ee2d92ca181f6c764191">[ ] unverified</a> | <a href="#case-in_game_save_reload-0db55804c43c8cec9e14">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-f375ad5bde0008a6816a"></a>

**0° CCW: unverified** — `in_game_save_reload-f375ad5bde0008a6816a`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-dc493e55bf39c8053152"></a>

**90° CCW: unverified** — `in_game_save_reload-dc493e55bf39c8053152`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-ee2d92ca181f6c764191"></a>

**180° CCW: unverified** — `in_game_save_reload-ee2d92ca181f6c764191`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-0db55804c43c8cec9e14"></a>

**270° CCW: unverified** — `in_game_save_reload-0db55804c43c8cec9e14`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 44 cases; unverified: 44</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-15-out; entry: channel-01-in; exit: channel-15-out | — | <a href="#case-in_game_route_query-05074bd527f878be50d8">[ ] unverified</a> | <a href="#case-in_game_route_query-de0ded5018ca698c6931">[ ] unverified</a> | <a href="#case-in_game_route_query-cad0fbb3c36bd810694b">[ ] unverified</a> | <a href="#case-in_game_route_query-263c931eedd5be445d57">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out | — | <a href="#case-in_game_route_query-6427b509ad0ac2de32a3">[ ] unverified</a> | <a href="#case-in_game_route_query-100eec4e0ba399e7bcd5">[ ] unverified</a> | <a href="#case-in_game_route_query-c03986d56b1dc35c2880">[ ] unverified</a> | <a href="#case-in_game_route_query-1338b5957e0f4a5de367">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-13-out; entry: channel-02-in; exit: channel-13-out | — | <a href="#case-in_game_route_query-87dea103e4f2ef8bc397">[ ] unverified</a> | <a href="#case-in_game_route_query-004d762f912ad795ff67">[ ] unverified</a> | <a href="#case-in_game_route_query-0b35cd4e691ba0c5be85">[ ] unverified</a> | <a href="#case-in_game_route_query-4427e0e454d2fc4a9469">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-12-out; entry: channel-03-in; exit: channel-12-out | — | <a href="#case-in_game_route_query-a3299d8d63026d24097f">[ ] unverified</a> | <a href="#case-in_game_route_query-81d02bcb88e050ddc620">[ ] unverified</a> | <a href="#case-in_game_route_query-6e470984579671a9d782">[ ] unverified</a> | <a href="#case-in_game_route_query-1e933da37d6f898592e5">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out | — | <a href="#case-in_game_route_query-4069c78079ab894b79de">[ ] unverified</a> | <a href="#case-in_game_route_query-64651927189a1bc3c94a">[ ] unverified</a> | <a href="#case-in_game_route_query-4af31d69cbcdf0bf1ac3">[ ] unverified</a> | <a href="#case-in_game_route_query-e98fe4c831a6a4fe8ebf">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out | — | <a href="#case-in_game_route_query-589bb9c8fde64ee59a4f">[ ] unverified</a> | <a href="#case-in_game_route_query-ce952a68382d3c5ee9e4">[ ] unverified</a> | <a href="#case-in_game_route_query-1b0335d66ff2635c4a58">[ ] unverified</a> | <a href="#case-in_game_route_query-678dcdb46637c30c2dd4">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out | — | <a href="#case-in_game_route_query-4694be6bf83e22005c2e">[ ] unverified</a> | <a href="#case-in_game_route_query-9670738fcf83b73a3500">[ ] unverified</a> | <a href="#case-in_game_route_query-4617c9af9af52bbdf4be">[ ] unverified</a> | <a href="#case-in_game_route_query-4413e7eaa5a971f9ed7a">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-07-in>channel-18-out; entry: channel-07-in; exit: channel-18-out | — | <a href="#case-in_game_route_query-06c33ec17b1fb6e562ac">[ ] unverified</a> | <a href="#case-in_game_route_query-2b3cc0fd70681d3b0db9">[ ] unverified</a> | <a href="#case-in_game_route_query-eef3caa963d7fc59819c">[ ] unverified</a> | <a href="#case-in_game_route_query-02754e4fee5b97785dba">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out | — | <a href="#case-in_game_route_query-98549cedbf58ca5edc14">[ ] unverified</a> | <a href="#case-in_game_route_query-979a4e17bd2a86583ed6">[ ] unverified</a> | <a href="#case-in_game_route_query-3864a671cdd046020ffa">[ ] unverified</a> | <a href="#case-in_game_route_query-dfc017795e8dfd3cbdbc">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-09-in>channel-20-out; entry: channel-09-in; exit: channel-20-out | — | <a href="#case-in_game_route_query-2cb89a014b5c28ef00f3">[ ] unverified</a> | <a href="#case-in_game_route_query-641610768f732ba53396">[ ] unverified</a> | <a href="#case-in_game_route_query-30e5d426a53bf71f9cf4">[ ] unverified</a> | <a href="#case-in_game_route_query-d16ec4ec430c7390769d">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out | — | <a href="#case-in_game_route_query-14da93b5190ca86946cf">[ ] unverified</a> | <a href="#case-in_game_route_query-763dbaae90367a7cc080">[ ] unverified</a> | <a href="#case-in_game_route_query-274f676658d7b5a48071">[ ] unverified</a> | <a href="#case-in_game_route_query-bb12c33f8786a3910fba">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-01-in>channel-15-out; entry: channel-01-in; exit: channel-15-out</summary>

<a id="case-in_game_route_query-05074bd527f878be50d8"></a>

**0° CCW: unverified** — `in_game_route_query-05074bd527f878be50d8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-15-out; entry: channel-01-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_route_query-de0ded5018ca698c6931"></a>

**90° CCW: unverified** — `in_game_route_query-de0ded5018ca698c6931`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-15-out; entry: channel-01-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_route_query-cad0fbb3c36bd810694b"></a>

**180° CCW: unverified** — `in_game_route_query-cad0fbb3c36bd810694b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-15-out; entry: channel-01-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_route_query-263c931eedd5be445d57"></a>

**270° CCW: unverified** — `in_game_route_query-263c931eedd5be445d57`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-15-out; entry: channel-01-in; exit: channel-15-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out</summary>

<a id="case-in_game_route_query-6427b509ad0ac2de32a3"></a>

**0° CCW: unverified** — `in_game_route_query-6427b509ad0ac2de32a3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_route_query-100eec4e0ba399e7bcd5"></a>

**90° CCW: unverified** — `in_game_route_query-100eec4e0ba399e7bcd5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_route_query-c03986d56b1dc35c2880"></a>

**180° CCW: unverified** — `in_game_route_query-c03986d56b1dc35c2880`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_route_query-1338b5957e0f4a5de367"></a>

**270° CCW: unverified** — `in_game_route_query-1338b5957e0f4a5de367`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-02-in>channel-13-out; entry: channel-02-in; exit: channel-13-out</summary>

<a id="case-in_game_route_query-87dea103e4f2ef8bc397"></a>

**0° CCW: unverified** — `in_game_route_query-87dea103e4f2ef8bc397`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-13-out; entry: channel-02-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_route_query-004d762f912ad795ff67"></a>

**90° CCW: unverified** — `in_game_route_query-004d762f912ad795ff67`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-13-out; entry: channel-02-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_route_query-0b35cd4e691ba0c5be85"></a>

**180° CCW: unverified** — `in_game_route_query-0b35cd4e691ba0c5be85`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-13-out; entry: channel-02-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_route_query-4427e0e454d2fc4a9469"></a>

**270° CCW: unverified** — `in_game_route_query-4427e0e454d2fc4a9469`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-13-out; entry: channel-02-in; exit: channel-13-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-03-in>channel-12-out; entry: channel-03-in; exit: channel-12-out</summary>

<a id="case-in_game_route_query-a3299d8d63026d24097f"></a>

**0° CCW: unverified** — `in_game_route_query-a3299d8d63026d24097f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-12-out; entry: channel-03-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_route_query-81d02bcb88e050ddc620"></a>

**90° CCW: unverified** — `in_game_route_query-81d02bcb88e050ddc620`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-12-out; entry: channel-03-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_route_query-6e470984579671a9d782"></a>

**180° CCW: unverified** — `in_game_route_query-6e470984579671a9d782`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-12-out; entry: channel-03-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_route_query-1e933da37d6f898592e5"></a>

**270° CCW: unverified** — `in_game_route_query-1e933da37d6f898592e5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-12-out; entry: channel-03-in; exit: channel-12-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out</summary>

<a id="case-in_game_route_query-4069c78079ab894b79de"></a>

**0° CCW: unverified** — `in_game_route_query-4069c78079ab894b79de`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_route_query-64651927189a1bc3c94a"></a>

**90° CCW: unverified** — `in_game_route_query-64651927189a1bc3c94a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_route_query-4af31d69cbcdf0bf1ac3"></a>

**180° CCW: unverified** — `in_game_route_query-4af31d69cbcdf0bf1ac3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_route_query-e98fe4c831a6a4fe8ebf"></a>

**270° CCW: unverified** — `in_game_route_query-e98fe4c831a6a4fe8ebf`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out</summary>

<a id="case-in_game_route_query-589bb9c8fde64ee59a4f"></a>

**0° CCW: unverified** — `in_game_route_query-589bb9c8fde64ee59a4f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_route_query-ce952a68382d3c5ee9e4"></a>

**90° CCW: unverified** — `in_game_route_query-ce952a68382d3c5ee9e4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_route_query-1b0335d66ff2635c4a58"></a>

**180° CCW: unverified** — `in_game_route_query-1b0335d66ff2635c4a58`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_route_query-678dcdb46637c30c2dd4"></a>

**270° CCW: unverified** — `in_game_route_query-678dcdb46637c30c2dd4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out</summary>

<a id="case-in_game_route_query-4694be6bf83e22005c2e"></a>

**0° CCW: unverified** — `in_game_route_query-4694be6bf83e22005c2e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_route_query-9670738fcf83b73a3500"></a>

**90° CCW: unverified** — `in_game_route_query-9670738fcf83b73a3500`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_route_query-4617c9af9af52bbdf4be"></a>

**180° CCW: unverified** — `in_game_route_query-4617c9af9af52bbdf4be`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_route_query-4413e7eaa5a971f9ed7a"></a>

**270° CCW: unverified** — `in_game_route_query-4413e7eaa5a971f9ed7a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-07-in>channel-18-out; entry: channel-07-in; exit: channel-18-out</summary>

<a id="case-in_game_route_query-06c33ec17b1fb6e562ac"></a>

**0° CCW: unverified** — `in_game_route_query-06c33ec17b1fb6e562ac`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-18-out; entry: channel-07-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_route_query-2b3cc0fd70681d3b0db9"></a>

**90° CCW: unverified** — `in_game_route_query-2b3cc0fd70681d3b0db9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-18-out; entry: channel-07-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_route_query-eef3caa963d7fc59819c"></a>

**180° CCW: unverified** — `in_game_route_query-eef3caa963d7fc59819c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-18-out; entry: channel-07-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_route_query-02754e4fee5b97785dba"></a>

**270° CCW: unverified** — `in_game_route_query-02754e4fee5b97785dba`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-18-out; entry: channel-07-in; exit: channel-18-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out</summary>

<a id="case-in_game_route_query-98549cedbf58ca5edc14"></a>

**0° CCW: unverified** — `in_game_route_query-98549cedbf58ca5edc14`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_route_query-979a4e17bd2a86583ed6"></a>

**90° CCW: unverified** — `in_game_route_query-979a4e17bd2a86583ed6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_route_query-3864a671cdd046020ffa"></a>

**180° CCW: unverified** — `in_game_route_query-3864a671cdd046020ffa`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_route_query-dfc017795e8dfd3cbdbc"></a>

**270° CCW: unverified** — `in_game_route_query-dfc017795e8dfd3cbdbc`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-09-in>channel-20-out; entry: channel-09-in; exit: channel-20-out</summary>

<a id="case-in_game_route_query-2cb89a014b5c28ef00f3"></a>

**0° CCW: unverified** — `in_game_route_query-2cb89a014b5c28ef00f3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-20-out; entry: channel-09-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_route_query-641610768f732ba53396"></a>

**90° CCW: unverified** — `in_game_route_query-641610768f732ba53396`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-20-out; entry: channel-09-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_route_query-30e5d426a53bf71f9cf4"></a>

**180° CCW: unverified** — `in_game_route_query-30e5d426a53bf71f9cf4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-20-out; entry: channel-09-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_route_query-d16ec4ec430c7390769d"></a>

**270° CCW: unverified** — `in_game_route_query-d16ec4ec430c7390769d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-20-out; entry: channel-09-in; exit: channel-20-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out</summary>

<a id="case-in_game_route_query-14da93b5190ca86946cf"></a>

**0° CCW: unverified** — `in_game_route_query-14da93b5190ca86946cf`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_route_query-763dbaae90367a7cc080"></a>

**90° CCW: unverified** — `in_game_route_query-763dbaae90367a7cc080`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_route_query-274f676658d7b5a48071"></a>

**180° CCW: unverified** — `in_game_route_query-274f676658d7b5a48071`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_route_query-bb12c33f8786a3910fba"></a>

**270° CCW: unverified** — `in_game_route_query-bb12c33f8786a3910fba`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 44 cases; unverified: 44</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-15-out; entry: channel-01-in; exit: channel-15-out | — | <a href="#case-in_game_visible_travel-05074bd527f878be50d8">[ ] unverified</a> | <a href="#case-in_game_visible_travel-de0ded5018ca698c6931">[ ] unverified</a> | <a href="#case-in_game_visible_travel-cad0fbb3c36bd810694b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-263c931eedd5be445d57">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out | — | <a href="#case-in_game_visible_travel-6427b509ad0ac2de32a3">[ ] unverified</a> | <a href="#case-in_game_visible_travel-100eec4e0ba399e7bcd5">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c03986d56b1dc35c2880">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1338b5957e0f4a5de367">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-13-out; entry: channel-02-in; exit: channel-13-out | — | <a href="#case-in_game_visible_travel-87dea103e4f2ef8bc397">[ ] unverified</a> | <a href="#case-in_game_visible_travel-004d762f912ad795ff67">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0b35cd4e691ba0c5be85">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4427e0e454d2fc4a9469">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-12-out; entry: channel-03-in; exit: channel-12-out | — | <a href="#case-in_game_visible_travel-a3299d8d63026d24097f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-81d02bcb88e050ddc620">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6e470984579671a9d782">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1e933da37d6f898592e5">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out | — | <a href="#case-in_game_visible_travel-4069c78079ab894b79de">[ ] unverified</a> | <a href="#case-in_game_visible_travel-64651927189a1bc3c94a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4af31d69cbcdf0bf1ac3">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e98fe4c831a6a4fe8ebf">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out | — | <a href="#case-in_game_visible_travel-589bb9c8fde64ee59a4f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ce952a68382d3c5ee9e4">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1b0335d66ff2635c4a58">[ ] unverified</a> | <a href="#case-in_game_visible_travel-678dcdb46637c30c2dd4">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out | — | <a href="#case-in_game_visible_travel-4694be6bf83e22005c2e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9670738fcf83b73a3500">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4617c9af9af52bbdf4be">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4413e7eaa5a971f9ed7a">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-07-in>channel-18-out; entry: channel-07-in; exit: channel-18-out | — | <a href="#case-in_game_visible_travel-06c33ec17b1fb6e562ac">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2b3cc0fd70681d3b0db9">[ ] unverified</a> | <a href="#case-in_game_visible_travel-eef3caa963d7fc59819c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-02754e4fee5b97785dba">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out | — | <a href="#case-in_game_visible_travel-98549cedbf58ca5edc14">[ ] unverified</a> | <a href="#case-in_game_visible_travel-979a4e17bd2a86583ed6">[ ] unverified</a> | <a href="#case-in_game_visible_travel-3864a671cdd046020ffa">[ ] unverified</a> | <a href="#case-in_game_visible_travel-dfc017795e8dfd3cbdbc">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-09-in>channel-20-out; entry: channel-09-in; exit: channel-20-out | — | <a href="#case-in_game_visible_travel-2cb89a014b5c28ef00f3">[ ] unverified</a> | <a href="#case-in_game_visible_travel-641610768f732ba53396">[ ] unverified</a> | <a href="#case-in_game_visible_travel-30e5d426a53bf71f9cf4">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d16ec4ec430c7390769d">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out | — | <a href="#case-in_game_visible_travel-14da93b5190ca86946cf">[ ] unverified</a> | <a href="#case-in_game_visible_travel-763dbaae90367a7cc080">[ ] unverified</a> | <a href="#case-in_game_visible_travel-274f676658d7b5a48071">[ ] unverified</a> | <a href="#case-in_game_visible_travel-bb12c33f8786a3910fba">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-01-in>channel-15-out; entry: channel-01-in; exit: channel-15-out</summary>

<a id="case-in_game_visible_travel-05074bd527f878be50d8"></a>

**0° CCW: unverified** — `in_game_visible_travel-05074bd527f878be50d8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-15-out; entry: channel-01-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_visible_travel-de0ded5018ca698c6931"></a>

**90° CCW: unverified** — `in_game_visible_travel-de0ded5018ca698c6931`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-15-out; entry: channel-01-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_visible_travel-cad0fbb3c36bd810694b"></a>

**180° CCW: unverified** — `in_game_visible_travel-cad0fbb3c36bd810694b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-15-out; entry: channel-01-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_visible_travel-263c931eedd5be445d57"></a>

**270° CCW: unverified** — `in_game_visible_travel-263c931eedd5be445d57`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-15-out; entry: channel-01-in; exit: channel-15-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out</summary>

<a id="case-in_game_visible_travel-6427b509ad0ac2de32a3"></a>

**0° CCW: unverified** — `in_game_visible_travel-6427b509ad0ac2de32a3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_visible_travel-100eec4e0ba399e7bcd5"></a>

**90° CCW: unverified** — `in_game_visible_travel-100eec4e0ba399e7bcd5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_visible_travel-c03986d56b1dc35c2880"></a>

**180° CCW: unverified** — `in_game_visible_travel-c03986d56b1dc35c2880`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_visible_travel-1338b5957e0f4a5de367"></a>

**270° CCW: unverified** — `in_game_visible_travel-1338b5957e0f4a5de367`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-02-in>channel-13-out; entry: channel-02-in; exit: channel-13-out</summary>

<a id="case-in_game_visible_travel-87dea103e4f2ef8bc397"></a>

**0° CCW: unverified** — `in_game_visible_travel-87dea103e4f2ef8bc397`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-13-out; entry: channel-02-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_visible_travel-004d762f912ad795ff67"></a>

**90° CCW: unverified** — `in_game_visible_travel-004d762f912ad795ff67`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-13-out; entry: channel-02-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_visible_travel-0b35cd4e691ba0c5be85"></a>

**180° CCW: unverified** — `in_game_visible_travel-0b35cd4e691ba0c5be85`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-13-out; entry: channel-02-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_visible_travel-4427e0e454d2fc4a9469"></a>

**270° CCW: unverified** — `in_game_visible_travel-4427e0e454d2fc4a9469`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-13-out; entry: channel-02-in; exit: channel-13-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-03-in>channel-12-out; entry: channel-03-in; exit: channel-12-out</summary>

<a id="case-in_game_visible_travel-a3299d8d63026d24097f"></a>

**0° CCW: unverified** — `in_game_visible_travel-a3299d8d63026d24097f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-12-out; entry: channel-03-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_visible_travel-81d02bcb88e050ddc620"></a>

**90° CCW: unverified** — `in_game_visible_travel-81d02bcb88e050ddc620`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-12-out; entry: channel-03-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_visible_travel-6e470984579671a9d782"></a>

**180° CCW: unverified** — `in_game_visible_travel-6e470984579671a9d782`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-12-out; entry: channel-03-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_visible_travel-1e933da37d6f898592e5"></a>

**270° CCW: unverified** — `in_game_visible_travel-1e933da37d6f898592e5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-12-out; entry: channel-03-in; exit: channel-12-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out</summary>

<a id="case-in_game_visible_travel-4069c78079ab894b79de"></a>

**0° CCW: unverified** — `in_game_visible_travel-4069c78079ab894b79de`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_visible_travel-64651927189a1bc3c94a"></a>

**90° CCW: unverified** — `in_game_visible_travel-64651927189a1bc3c94a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_visible_travel-4af31d69cbcdf0bf1ac3"></a>

**180° CCW: unverified** — `in_game_visible_travel-4af31d69cbcdf0bf1ac3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_visible_travel-e98fe4c831a6a4fe8ebf"></a>

**270° CCW: unverified** — `in_game_visible_travel-e98fe4c831a6a4fe8ebf`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out</summary>

<a id="case-in_game_visible_travel-589bb9c8fde64ee59a4f"></a>

**0° CCW: unverified** — `in_game_visible_travel-589bb9c8fde64ee59a4f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_visible_travel-ce952a68382d3c5ee9e4"></a>

**90° CCW: unverified** — `in_game_visible_travel-ce952a68382d3c5ee9e4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_visible_travel-1b0335d66ff2635c4a58"></a>

**180° CCW: unverified** — `in_game_visible_travel-1b0335d66ff2635c4a58`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_visible_travel-678dcdb46637c30c2dd4"></a>

**270° CCW: unverified** — `in_game_visible_travel-678dcdb46637c30c2dd4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out</summary>

<a id="case-in_game_visible_travel-4694be6bf83e22005c2e"></a>

**0° CCW: unverified** — `in_game_visible_travel-4694be6bf83e22005c2e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_visible_travel-9670738fcf83b73a3500"></a>

**90° CCW: unverified** — `in_game_visible_travel-9670738fcf83b73a3500`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_visible_travel-4617c9af9af52bbdf4be"></a>

**180° CCW: unverified** — `in_game_visible_travel-4617c9af9af52bbdf4be`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_visible_travel-4413e7eaa5a971f9ed7a"></a>

**270° CCW: unverified** — `in_game_visible_travel-4413e7eaa5a971f9ed7a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-07-in>channel-18-out; entry: channel-07-in; exit: channel-18-out</summary>

<a id="case-in_game_visible_travel-06c33ec17b1fb6e562ac"></a>

**0° CCW: unverified** — `in_game_visible_travel-06c33ec17b1fb6e562ac`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-18-out; entry: channel-07-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_visible_travel-2b3cc0fd70681d3b0db9"></a>

**90° CCW: unverified** — `in_game_visible_travel-2b3cc0fd70681d3b0db9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-18-out; entry: channel-07-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_visible_travel-eef3caa963d7fc59819c"></a>

**180° CCW: unverified** — `in_game_visible_travel-eef3caa963d7fc59819c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-18-out; entry: channel-07-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_visible_travel-02754e4fee5b97785dba"></a>

**270° CCW: unverified** — `in_game_visible_travel-02754e4fee5b97785dba`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-18-out; entry: channel-07-in; exit: channel-18-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out</summary>

<a id="case-in_game_visible_travel-98549cedbf58ca5edc14"></a>

**0° CCW: unverified** — `in_game_visible_travel-98549cedbf58ca5edc14`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_visible_travel-979a4e17bd2a86583ed6"></a>

**90° CCW: unverified** — `in_game_visible_travel-979a4e17bd2a86583ed6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_visible_travel-3864a671cdd046020ffa"></a>

**180° CCW: unverified** — `in_game_visible_travel-3864a671cdd046020ffa`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_visible_travel-dfc017795e8dfd3cbdbc"></a>

**270° CCW: unverified** — `in_game_visible_travel-dfc017795e8dfd3cbdbc`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-17-out; entry: channel-08-in; exit: channel-17-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-09-in>channel-20-out; entry: channel-09-in; exit: channel-20-out</summary>

<a id="case-in_game_visible_travel-2cb89a014b5c28ef00f3"></a>

**0° CCW: unverified** — `in_game_visible_travel-2cb89a014b5c28ef00f3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-20-out; entry: channel-09-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_visible_travel-641610768f732ba53396"></a>

**90° CCW: unverified** — `in_game_visible_travel-641610768f732ba53396`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-20-out; entry: channel-09-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_visible_travel-30e5d426a53bf71f9cf4"></a>

**180° CCW: unverified** — `in_game_visible_travel-30e5d426a53bf71f9cf4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-20-out; entry: channel-09-in; exit: channel-20-out.

No observation recorded.

<a id="case-in_game_visible_travel-d16ec4ec430c7390769d"></a>

**270° CCW: unverified** — `in_game_visible_travel-d16ec4ec430c7390769d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-20-out; entry: channel-09-in; exit: channel-20-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out</summary>

<a id="case-in_game_visible_travel-14da93b5190ca86946cf"></a>

**0° CCW: unverified** — `in_game_visible_travel-14da93b5190ca86946cf`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_visible_travel-763dbaae90367a7cc080"></a>

**90° CCW: unverified** — `in_game_visible_travel-763dbaae90367a7cc080`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_visible_travel-274f676658d7b5a48071"></a>

**180° CCW: unverified** — `in_game_visible_travel-274f676658d7b5a48071`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_visible_travel-bb12c33f8786a3910fba"></a>

**270° CCW: unverified** — `in_game_visible_travel-bb12c33f8786a3910fba`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 356 cases; unverified: 356</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7db861a5971a8652e19c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2bc44759b1c69621fef8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-784f2996015a4825edbf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0dfc1aa33297a8279c65">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e9cc59e52e360adf7ed5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-24edb680d5e194fb2c72">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1cc2086320da6fc5a33d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8f897a6c4e57ddfeaeb8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ca81e0744393fdbb2255">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1bdaa9799a1fed1d0c5f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-93035df7a62f40dac5ab">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-334cdee23895442f2f07">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0535b6b5ed2ad465d39d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c43245dda4b50062d37d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2a9ff5a3fb8c9822f302">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1007844caabfe1bf4a88">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-176dc802ee0595c54e08">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-91a309e549d05eb08215">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-58a7ca87b548a0561f3e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6c77aa691456cad2db04">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6ae758240248c9ff34e6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-17401a3db691d138b48e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-31ae7685f9369fc721bb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4c6221e83ed025562eb1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0c6d4c497332793204d4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f9281b5d6c5b8030a081">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fc185f44591f63424c55">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-250f13e9c4d9a97c6490">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2e5d4d1dc639697678e9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d9a58fcd3e9637ad8cd1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d5b11046cff4cbcf30f3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-321dcddf5b9088d60d59">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-547eaf6b97393c8c9595">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-111bed85f99b6e3dbe30">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2ef9b3e0d8312bb21393">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-13782a0717cfb2ec4605">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-544e87fd5359ef3fe942">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a635513adddc83c7782b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-501514d68b0bc9345c9d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3daaffbee7d54f7abfdf">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-53b5f4abf0073fa99ce4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e3e23143277b29c0f434">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-31889928474d6b7731e8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0b7aa35ae1b5db884f78">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1bc115a6b2b62d4b1a63">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-98302a7fbecc8f1a153e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c921c2122995d70d86a7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0095d366fef87f1eaacf">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ef1c219418f866c54ed1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f038ced915e2bd3b1936">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-101f85e09bf3d99ba6ef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-12e0f92a1dc88fc6b0e9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-19cd0b6a481b23890a4a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-79f45e720bf0f4df7a8d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a2a79b8c19dc513447d1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9c5845154d9c221d7f1c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-65d312f1f8e08340bb01">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6291a78c1ca2750c4543">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e30eab8205da17880d6f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7975575032235088e91d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f4632cebdee978a653f6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c3d0768e2ff4c170eab0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-03731ff29613c4456ea4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-473ba6fcfc9b2544dcc1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3648a0f6c284a12ce0ba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-798500c5f82a1cf9fce0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d9234e713f39bfc307e1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d82e430022e357c23802">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1b32cdab047079a4c459">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-25d1c223abd140d017cc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-40ab1c4074496af29c59">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-df7d8dca082df9b882c9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-32cf5df4c19f61b9adf9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9be38479f5e32cfe9531">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c1fee9b78b751844d2d1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ed3c8dc373d11721723f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0ec52bf7d1a177c46544">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7ceceedefbe1599e30d1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-494d0e7fbe80137e660d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ec8e7af2f9f4458d5ede">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a27c40abd4a7b52df64d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-703d319be90f6e2f72b0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9d24765e66843da7c940">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d72f619e137c62c3f279">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cef52ef589512f8dad97">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-886cbc3be3f1b4e5e1b0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-121444384affce67ffe3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f0ebbad6c194e5697a37">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f8599fbc281fbe40f203">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-70eafc0ec054939ac31c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b30de0a9ccf15599d6d1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-903d57840b2eb9c027a2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ebf41b4c299421482963">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3eefa88551915d41be9e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b7ca4dc8f6889f5151aa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-55fe3ebacc68912e6299">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a26679feb51a1b315c1b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8d00a58b39785842445d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-098d34e9950cf49e3356">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-87744211b8e6657253a8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e6785d771c701a721c5d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a75fb650a9a9d61ad029">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fcbb12a7f6d4a8d7da9e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4615b2f78d9e77e7ba7a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5e23635be76b490a944e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6f78c8220e24f0acd278">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ec5462ab406f5644d5c9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eb64c6379f1a7c90090d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d87df7141833674e27bb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-091da1a1c1bae3f5f286">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3e6d42cba1265f17d5e5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7d14c34ebcb5ddada649">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4138a34b177b8dbd6788">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-16e241a7b9787e34a14f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-718510334f37bec2d2f0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-edf90c62522877518067">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-10dc78820eb96e563510">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a0fe26a6ed6ae8e9ccc3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1f62cacba457aa79c5f0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6dd51534fc26ee25b2c0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ffaf37660060c220ae7f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-863f25d0d9d2e4920880">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-54b74ecfbc0fc49b342f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f60c940621e6b723d0f8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fcc947157dfc40338479">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-48ae3e8d8ad93172e7d4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8ee3dae9294bf45b7491">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dc0f67279986c79e8939">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3f852cfb53e00266037f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bb67d6d880bec2b23a26">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8c1b4ec447d1420697b0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f2f70110ffa4f0bd9087">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7410591712d2b3aa0b55">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3726fbf644525ea34c98">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-048054da23e7049c5026">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3380b017432d97f23e7f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-23505c08baa6d02fa37b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c099df54dc08b6ed6984">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ba2f081c86f149676a7e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a8c7f9534cca3ba9071d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bbc190c9023bbe435138">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fd29d3bba613cb6207e5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-74520f895157fce34ee7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-997c03c518691b72d437">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ff569a80afe00149062b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1c5cbcfcce62ac435390">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-da3aa5072ad80eaed986">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0cfcdf7254ebfba85d0f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fdfea12e238aee6d630a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6a695f7cfe575f84931c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-055a07b89a59147af7cf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1b03822b864d9e71ac03">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-501532ccf2e0a23d10b0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ef868a3f3f3544157dff">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2b46a6ca7c300bffe269">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-68f0fd9f66ea332501ea">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f32ef0de22a211bedd77">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8f1acd1aa38859c2758a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c102d95ef9d1b1da4874">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-805d6c0c48b917751e7d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-177032a32d86101ce687">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-67fa7afd559c9368c385">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-48068dadbd9a21b333fb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e6359222705706909cb8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-14650468d96ed8c6c613">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e387fa0ab60bad370ee3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d36b2a25d52e9a700599">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-364225b7fad1f6d6f701">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-dfc4a3808b4e4c71b4d0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-892abe9079bffb2303d7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-953636e8ecb486fa88a4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3698a49763dd4ec3db37">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8f40479ff96a64e3e434">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a626cb9e32643ecd875f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6b957b146f8584b87105">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4f450318923d79c6857d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1c789b3871cebd1c1c8b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-16dd180e486e14ce0191">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9bbb723a129c07818467">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-268cbf0428e46408cf35">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fba684a739a3a99a6024">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-139a6c25d4eeeeaea8ea">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a88ebde970b102f52b68">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-185dd88713173e9fb32d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7d977659a4532fa69db0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c423d6c53a00f87ec9db">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6e9d169967db048b575e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-31c491e65ca17eda953c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9e140aca59f5d40eb045">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7cc5d957989885a33b81">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8587b16c03137af0dfc5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-32e7f72951335b8c95f4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e1a2ec0d4be49806cd3c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e58dfb23f6f0a0f840f8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e9ed4d9936d8c76e3a15">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e713424fed00289aac91">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c51ae7d39f2bb26044bc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7f68e8dc393efb9abc85">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-490cf2dc2960a5df6eca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0e06b24dc8a1f5282799">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cf1dcb764f45fa85b062">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6f916f7cf33098a60c43">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eaa4749d149f532ac57a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-742663cbd845dd90e03e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-467cfb45ad0b8969cc5c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1dfe3055b3a1895537f0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4d0957e476d5b6ade051">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f9f311db9bd5a9c44de8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7b54a51213bb87e9f5a1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ffc2dbac7d19252e17f4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-16782a33a90e27e55cdd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e68da32f6155aedc6450">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8696ed330d7a30859224">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-357b67c00e3636583359">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e6eacd80d07b43df3240">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2f2b6c1028f7771663ce">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cb5fad379b7b05098056">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2017a1a602040c5d5d44">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c8c1998792e8275c64e3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-acc320e34cde7ec8daa8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-751f863cfaf2e94c26a3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cba40f199a2ffd569982">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f556d7c6bb6ded19f950">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3a212e4dee7bd225aecc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ec84ebceeb6abe434db9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-702ad5b237eb9cd5c41d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-289d417794a95248c7cf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eaf1b5f38a1ee99d083f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0df627298cbc2f32a22f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-daa2306ae99faddba715">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-973f6632a600a83a268d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cbc218fb81b656e0a02f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b2551567c97f68501fa9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4ad14b946d96c27f50f3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e4a1932204d5e3214c42">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4f45043ed617387559f5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0729c983638e5a231c54">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2569da04e1a4c6646f6b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4ee0d0489a768042caa2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e69bbeb0c8896d4bc177">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8aeff58d0f022c7fc45f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bb40b0119d1006fd1ef7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-975532ae919784140178">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1c3e64af2c00e7b5ef52">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5d26c8a6da9459071846">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6c01720c21593f284ead">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-afa435831beae7dc63d4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-20cf9c9a5ec8b2232b0b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-635fd5f6a9b356c15771">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5be3e86d3ae3ab4e724b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bfcab026b2dea096421b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b3bc555666416d660333">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-71e96fbb07010b7c6bdf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a3e8ce22196b8232cec7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-80649314f70d2b4f4f24">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c0a85205fc36fd391f96">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1db2002e69243f81767d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e7894a1ce3b1cadfac29">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-92a10a2983cb640392dc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-59412cc7a7e6053ee24c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e3c78c88191498b85191">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7953f971d8a2b9a03b04">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-766c2a4b8e5386cc7d0f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e697c817da20214ba0d5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-46b377fd2bc68cb7ab13">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-09f6483c32de2adec9be">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b274f16513213f68f883">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5df2eba0b97c6576d95a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-00e5238bbad7ec34d62d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f38093db702d6663f57b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-637ff3b7a0cc86664ab8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-33c5334eaa8ad7edea79">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-86931637487578b810ac">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-419c7eb64fabcc079313">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4dfc2231e228d7d1db0c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4309105097906fa44b77">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-56e378b57ed8298452cf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-205fae828575a1a0f093">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d7015d78e1d1e7c4ff3d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ae2ae234615d13d60f90">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5c397f4940c5f23b0f9b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1670930d88c983b95e49">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-baa63c8b8dab73d0288d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e325f90f85d9c3e52301">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a23f4987366819b01828">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0518e1399a95775542ec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5e1ebeff7853f70c731b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f006a33884e921d22bce">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ad02ec66c08d5b77fb69">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-34b615fa0a2da268e657">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2e37eb9252e7decec8b2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-38aebf58f20a032ef391">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7b043fc947bbfa6742bd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8a6a5f5f4fcf9f4d1d74">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-709c4e1c2dc9d49f1ca3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c1720d19105b1e746577">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-990af91943b6815bc35b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d21faf5b858c7fdd9068">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-38d3ee5af291631cb22f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aba2894ea3ddeda49a9e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6350e47728e080d5a8fc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-535278c5ef9302a9d6a6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-017c9a21ec2c52087fa2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-adb05368965b185f1b74">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-034562010273122dfb1a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ea6d55f9fe1568a20de0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-294a71b543c6e5dc129d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d6349273e73f11ca09f2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-40be866cf8b81857170d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5ecbe9b14d9698c515b3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-899fff6de4fb590760f0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-01e77d7270cb574a26da">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f650a6d91f5f90573511">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-59cecd5bdcf210a355ef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-49ae9f57f5dc6da29ba7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0b1a06be47bc8fe5cc11">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-dfe9d8d21ce5b761380f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-400c99e31a87823bebda">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ec0b55735560a09fce21">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-59e67bbec9b2cae0e98c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7bbcf103a517eff9a862">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3b6a06bb48222cbdb077">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2f78f227c82ca963d5b9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-82b5c7d646777233a81e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-658876f6bca9fbf7643c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-201ea4b2f1701dca128a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8232d9a5a503b5817bc1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-763aa211e2b660c545a9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-725c1980f5be35fd8bd7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-87d632ecec6c23b3c16f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-125aef2c7baa009174db">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f78b55098296d15ced46">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d25fa09e2b5aa88165ea">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d1e098df284fb54504f3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c2216e373d9eb0e8f2ca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9ad57df1478bca810018">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2dee6943e84f6bd9866b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9361fb6c871501401da6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0f4a8ecffb5609d010ba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-43ed391188bb6ae73b6c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f5f022ca3785ee47e661">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2e38bcad6cebae51d72f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2880b1f2304656d6ca73">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a98d019767124c914b88">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-891a6da76a16c5af8add">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fd73473782efd8910ee9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a349bcdb3d24faabeb7d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-75d515a5b20a58aa4d49">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2f612b963456ee7e7fa6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ba6a590ea21810404c1e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8f7e7b422ea2d8738a5a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3fa35807a2d273e78e77">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b1f2024834557f40182c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2169f314f03960808edf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-59e5b1670178e6d8ae65">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c1ae35a12f636c2d26c8">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7db861a5971a8652e19c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7db861a5971a8652e19c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2bc44759b1c69621fef8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2bc44759b1c69621fef8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-784f2996015a4825edbf"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-784f2996015a4825edbf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0dfc1aa33297a8279c65"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0dfc1aa33297a8279c65`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e9cc59e52e360adf7ed5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e9cc59e52e360adf7ed5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-24edb680d5e194fb2c72"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-24edb680d5e194fb2c72`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1cc2086320da6fc5a33d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1cc2086320da6fc5a33d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8f897a6c4e57ddfeaeb8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8f897a6c4e57ddfeaeb8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ca81e0744393fdbb2255"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ca81e0744393fdbb2255`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1bdaa9799a1fed1d0c5f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1bdaa9799a1fed1d0c5f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-93035df7a62f40dac5ab"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-93035df7a62f40dac5ab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-334cdee23895442f2f07"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-334cdee23895442f2f07`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0535b6b5ed2ad465d39d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0535b6b5ed2ad465d39d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c43245dda4b50062d37d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c43245dda4b50062d37d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2a9ff5a3fb8c9822f302"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2a9ff5a3fb8c9822f302`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1007844caabfe1bf4a88"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1007844caabfe1bf4a88`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-176dc802ee0595c54e08"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-176dc802ee0595c54e08`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-91a309e549d05eb08215"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-91a309e549d05eb08215`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-58a7ca87b548a0561f3e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-58a7ca87b548a0561f3e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6c77aa691456cad2db04"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6c77aa691456cad2db04`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6ae758240248c9ff34e6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6ae758240248c9ff34e6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-17401a3db691d138b48e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-17401a3db691d138b48e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-31ae7685f9369fc721bb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-31ae7685f9369fc721bb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4c6221e83ed025562eb1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4c6221e83ed025562eb1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0c6d4c497332793204d4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0c6d4c497332793204d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f9281b5d6c5b8030a081"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f9281b5d6c5b8030a081`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fc185f44591f63424c55"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fc185f44591f63424c55`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-250f13e9c4d9a97c6490"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-250f13e9c4d9a97c6490`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2e5d4d1dc639697678e9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2e5d4d1dc639697678e9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d9a58fcd3e9637ad8cd1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d9a58fcd3e9637ad8cd1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d5b11046cff4cbcf30f3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d5b11046cff4cbcf30f3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-321dcddf5b9088d60d59"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-321dcddf5b9088d60d59`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-547eaf6b97393c8c9595"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-547eaf6b97393c8c9595`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-111bed85f99b6e3dbe30"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-111bed85f99b6e3dbe30`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2ef9b3e0d8312bb21393"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2ef9b3e0d8312bb21393`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-13782a0717cfb2ec4605"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-13782a0717cfb2ec4605`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-544e87fd5359ef3fe942"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-544e87fd5359ef3fe942`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a635513adddc83c7782b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a635513adddc83c7782b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-501514d68b0bc9345c9d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-501514d68b0bc9345c9d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3daaffbee7d54f7abfdf"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3daaffbee7d54f7abfdf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-53b5f4abf0073fa99ce4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-53b5f4abf0073fa99ce4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e3e23143277b29c0f434"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e3e23143277b29c0f434`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-31889928474d6b7731e8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-31889928474d6b7731e8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0b7aa35ae1b5db884f78"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0b7aa35ae1b5db884f78`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1bc115a6b2b62d4b1a63"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1bc115a6b2b62d4b1a63`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-98302a7fbecc8f1a153e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-98302a7fbecc8f1a153e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c921c2122995d70d86a7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c921c2122995d70d86a7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0095d366fef87f1eaacf"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0095d366fef87f1eaacf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ef1c219418f866c54ed1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ef1c219418f866c54ed1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f038ced915e2bd3b1936"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f038ced915e2bd3b1936`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-101f85e09bf3d99ba6ef"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-101f85e09bf3d99ba6ef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-12e0f92a1dc88fc6b0e9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-12e0f92a1dc88fc6b0e9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-19cd0b6a481b23890a4a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-19cd0b6a481b23890a4a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-79f45e720bf0f4df7a8d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-79f45e720bf0f4df7a8d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a2a79b8c19dc513447d1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a2a79b8c19dc513447d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9c5845154d9c221d7f1c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9c5845154d9c221d7f1c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-65d312f1f8e08340bb01"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-65d312f1f8e08340bb01`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6291a78c1ca2750c4543"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6291a78c1ca2750c4543`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e30eab8205da17880d6f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e30eab8205da17880d6f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7975575032235088e91d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7975575032235088e91d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f4632cebdee978a653f6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f4632cebdee978a653f6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c3d0768e2ff4c170eab0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c3d0768e2ff4c170eab0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-03731ff29613c4456ea4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-03731ff29613c4456ea4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-473ba6fcfc9b2544dcc1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-473ba6fcfc9b2544dcc1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3648a0f6c284a12ce0ba"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3648a0f6c284a12ce0ba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-798500c5f82a1cf9fce0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-798500c5f82a1cf9fce0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d9234e713f39bfc307e1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d9234e713f39bfc307e1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d82e430022e357c23802"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d82e430022e357c23802`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1b32cdab047079a4c459"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1b32cdab047079a4c459`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-25d1c223abd140d017cc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-25d1c223abd140d017cc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-40ab1c4074496af29c59"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-40ab1c4074496af29c59`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-df7d8dca082df9b882c9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-df7d8dca082df9b882c9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-32cf5df4c19f61b9adf9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-32cf5df4c19f61b9adf9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9be38479f5e32cfe9531"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9be38479f5e32cfe9531`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c1fee9b78b751844d2d1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c1fee9b78b751844d2d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ed3c8dc373d11721723f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ed3c8dc373d11721723f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0ec52bf7d1a177c46544"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0ec52bf7d1a177c46544`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7ceceedefbe1599e30d1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7ceceedefbe1599e30d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-494d0e7fbe80137e660d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-494d0e7fbe80137e660d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ec8e7af2f9f4458d5ede"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ec8e7af2f9f4458d5ede`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a27c40abd4a7b52df64d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a27c40abd4a7b52df64d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-703d319be90f6e2f72b0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-703d319be90f6e2f72b0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9d24765e66843da7c940"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9d24765e66843da7c940`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d72f619e137c62c3f279"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d72f619e137c62c3f279`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cef52ef589512f8dad97"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cef52ef589512f8dad97`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-886cbc3be3f1b4e5e1b0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-886cbc3be3f1b4e5e1b0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-121444384affce67ffe3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-121444384affce67ffe3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f0ebbad6c194e5697a37"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f0ebbad6c194e5697a37`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f8599fbc281fbe40f203"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f8599fbc281fbe40f203`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-70eafc0ec054939ac31c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-70eafc0ec054939ac31c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b30de0a9ccf15599d6d1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b30de0a9ccf15599d6d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-903d57840b2eb9c027a2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-903d57840b2eb9c027a2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ebf41b4c299421482963"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ebf41b4c299421482963`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3eefa88551915d41be9e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3eefa88551915d41be9e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b7ca4dc8f6889f5151aa"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b7ca4dc8f6889f5151aa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-55fe3ebacc68912e6299"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-55fe3ebacc68912e6299`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a26679feb51a1b315c1b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a26679feb51a1b315c1b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8d00a58b39785842445d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8d00a58b39785842445d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-098d34e9950cf49e3356"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-098d34e9950cf49e3356`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-87744211b8e6657253a8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-87744211b8e6657253a8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e6785d771c701a721c5d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e6785d771c701a721c5d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a75fb650a9a9d61ad029"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a75fb650a9a9d61ad029`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fcbb12a7f6d4a8d7da9e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fcbb12a7f6d4a8d7da9e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4615b2f78d9e77e7ba7a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4615b2f78d9e77e7ba7a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5e23635be76b490a944e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5e23635be76b490a944e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6f78c8220e24f0acd278"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6f78c8220e24f0acd278`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ec5462ab406f5644d5c9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ec5462ab406f5644d5c9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eb64c6379f1a7c90090d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-eb64c6379f1a7c90090d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d87df7141833674e27bb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d87df7141833674e27bb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-091da1a1c1bae3f5f286"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-091da1a1c1bae3f5f286`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3e6d42cba1265f17d5e5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3e6d42cba1265f17d5e5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7d14c34ebcb5ddada649"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7d14c34ebcb5ddada649`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4138a34b177b8dbd6788"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4138a34b177b8dbd6788`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-16e241a7b9787e34a14f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-16e241a7b9787e34a14f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-718510334f37bec2d2f0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-718510334f37bec2d2f0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-edf90c62522877518067"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-edf90c62522877518067`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-10dc78820eb96e563510"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-10dc78820eb96e563510`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a0fe26a6ed6ae8e9ccc3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a0fe26a6ed6ae8e9ccc3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1f62cacba457aa79c5f0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1f62cacba457aa79c5f0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6dd51534fc26ee25b2c0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6dd51534fc26ee25b2c0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ffaf37660060c220ae7f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ffaf37660060c220ae7f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-863f25d0d9d2e4920880"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-863f25d0d9d2e4920880`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-54b74ecfbc0fc49b342f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-54b74ecfbc0fc49b342f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f60c940621e6b723d0f8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f60c940621e6b723d0f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fcc947157dfc40338479"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fcc947157dfc40338479`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-48ae3e8d8ad93172e7d4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-48ae3e8d8ad93172e7d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8ee3dae9294bf45b7491"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8ee3dae9294bf45b7491`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dc0f67279986c79e8939"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dc0f67279986c79e8939`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3f852cfb53e00266037f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3f852cfb53e00266037f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bb67d6d880bec2b23a26"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bb67d6d880bec2b23a26`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8c1b4ec447d1420697b0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8c1b4ec447d1420697b0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f2f70110ffa4f0bd9087"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f2f70110ffa4f0bd9087`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7410591712d2b3aa0b55"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7410591712d2b3aa0b55`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3726fbf644525ea34c98"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3726fbf644525ea34c98`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-048054da23e7049c5026"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-048054da23e7049c5026`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3380b017432d97f23e7f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3380b017432d97f23e7f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-23505c08baa6d02fa37b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-23505c08baa6d02fa37b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c099df54dc08b6ed6984"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c099df54dc08b6ed6984`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ba2f081c86f149676a7e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ba2f081c86f149676a7e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a8c7f9534cca3ba9071d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a8c7f9534cca3ba9071d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bbc190c9023bbe435138"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bbc190c9023bbe435138`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fd29d3bba613cb6207e5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fd29d3bba613cb6207e5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-74520f895157fce34ee7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-74520f895157fce34ee7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-997c03c518691b72d437"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-997c03c518691b72d437`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ff569a80afe00149062b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ff569a80afe00149062b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1c5cbcfcce62ac435390"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1c5cbcfcce62ac435390`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-da3aa5072ad80eaed986"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-da3aa5072ad80eaed986`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0cfcdf7254ebfba85d0f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0cfcdf7254ebfba85d0f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fdfea12e238aee6d630a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fdfea12e238aee6d630a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6a695f7cfe575f84931c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6a695f7cfe575f84931c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-055a07b89a59147af7cf"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-055a07b89a59147af7cf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1b03822b864d9e71ac03"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1b03822b864d9e71ac03`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-501532ccf2e0a23d10b0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-501532ccf2e0a23d10b0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ef868a3f3f3544157dff"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ef868a3f3f3544157dff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2b46a6ca7c300bffe269"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2b46a6ca7c300bffe269`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-68f0fd9f66ea332501ea"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-68f0fd9f66ea332501ea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f32ef0de22a211bedd77"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f32ef0de22a211bedd77`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8f1acd1aa38859c2758a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8f1acd1aa38859c2758a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c102d95ef9d1b1da4874"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c102d95ef9d1b1da4874`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-805d6c0c48b917751e7d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-805d6c0c48b917751e7d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-177032a32d86101ce687"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-177032a32d86101ce687`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-67fa7afd559c9368c385"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-67fa7afd559c9368c385`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-48068dadbd9a21b333fb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-48068dadbd9a21b333fb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e6359222705706909cb8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e6359222705706909cb8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-14650468d96ed8c6c613"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-14650468d96ed8c6c613`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e387fa0ab60bad370ee3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e387fa0ab60bad370ee3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d36b2a25d52e9a700599"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d36b2a25d52e9a700599`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-364225b7fad1f6d6f701"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-364225b7fad1f6d6f701`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-dfc4a3808b4e4c71b4d0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-dfc4a3808b4e4c71b4d0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-892abe9079bffb2303d7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-892abe9079bffb2303d7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-953636e8ecb486fa88a4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-953636e8ecb486fa88a4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3698a49763dd4ec3db37"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3698a49763dd4ec3db37`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8f40479ff96a64e3e434"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8f40479ff96a64e3e434`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a626cb9e32643ecd875f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a626cb9e32643ecd875f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6b957b146f8584b87105"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6b957b146f8584b87105`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4f450318923d79c6857d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4f450318923d79c6857d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1c789b3871cebd1c1c8b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1c789b3871cebd1c1c8b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-16dd180e486e14ce0191"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-16dd180e486e14ce0191`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9bbb723a129c07818467"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9bbb723a129c07818467`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-268cbf0428e46408cf35"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-268cbf0428e46408cf35`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fba684a739a3a99a6024"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fba684a739a3a99a6024`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-139a6c25d4eeeeaea8ea"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-139a6c25d4eeeeaea8ea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a88ebde970b102f52b68"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a88ebde970b102f52b68`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-185dd88713173e9fb32d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-185dd88713173e9fb32d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7d977659a4532fa69db0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7d977659a4532fa69db0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c423d6c53a00f87ec9db"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c423d6c53a00f87ec9db`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6e9d169967db048b575e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6e9d169967db048b575e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-31c491e65ca17eda953c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-31c491e65ca17eda953c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9e140aca59f5d40eb045"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9e140aca59f5d40eb045`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7cc5d957989885a33b81"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7cc5d957989885a33b81`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8587b16c03137af0dfc5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8587b16c03137af0dfc5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-32e7f72951335b8c95f4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-32e7f72951335b8c95f4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e1a2ec0d4be49806cd3c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e1a2ec0d4be49806cd3c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e58dfb23f6f0a0f840f8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e58dfb23f6f0a0f840f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e9ed4d9936d8c76e3a15"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e9ed4d9936d8c76e3a15`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e713424fed00289aac91"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e713424fed00289aac91`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c51ae7d39f2bb26044bc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c51ae7d39f2bb26044bc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7f68e8dc393efb9abc85"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7f68e8dc393efb9abc85`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-490cf2dc2960a5df6eca"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-490cf2dc2960a5df6eca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0e06b24dc8a1f5282799"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0e06b24dc8a1f5282799`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cf1dcb764f45fa85b062"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cf1dcb764f45fa85b062`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6f916f7cf33098a60c43"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6f916f7cf33098a60c43`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eaa4749d149f532ac57a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-eaa4749d149f532ac57a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-742663cbd845dd90e03e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-742663cbd845dd90e03e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-467cfb45ad0b8969cc5c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-467cfb45ad0b8969cc5c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1dfe3055b3a1895537f0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1dfe3055b3a1895537f0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4d0957e476d5b6ade051"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4d0957e476d5b6ade051`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f9f311db9bd5a9c44de8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f9f311db9bd5a9c44de8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7b54a51213bb87e9f5a1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7b54a51213bb87e9f5a1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ffc2dbac7d19252e17f4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ffc2dbac7d19252e17f4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-16782a33a90e27e55cdd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-16782a33a90e27e55cdd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e68da32f6155aedc6450"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e68da32f6155aedc6450`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8696ed330d7a30859224"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8696ed330d7a30859224`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-357b67c00e3636583359"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-357b67c00e3636583359`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e6eacd80d07b43df3240"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e6eacd80d07b43df3240`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2f2b6c1028f7771663ce"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2f2b6c1028f7771663ce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cb5fad379b7b05098056"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cb5fad379b7b05098056`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2017a1a602040c5d5d44"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2017a1a602040c5d5d44`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c8c1998792e8275c64e3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c8c1998792e8275c64e3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-acc320e34cde7ec8daa8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-acc320e34cde7ec8daa8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-751f863cfaf2e94c26a3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-751f863cfaf2e94c26a3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cba40f199a2ffd569982"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cba40f199a2ffd569982`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f556d7c6bb6ded19f950"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f556d7c6bb6ded19f950`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3a212e4dee7bd225aecc"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3a212e4dee7bd225aecc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ec84ebceeb6abe434db9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ec84ebceeb6abe434db9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-702ad5b237eb9cd5c41d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-702ad5b237eb9cd5c41d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-289d417794a95248c7cf"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-289d417794a95248c7cf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eaf1b5f38a1ee99d083f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-eaf1b5f38a1ee99d083f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0df627298cbc2f32a22f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0df627298cbc2f32a22f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-daa2306ae99faddba715"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-daa2306ae99faddba715`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-973f6632a600a83a268d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-973f6632a600a83a268d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cbc218fb81b656e0a02f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cbc218fb81b656e0a02f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b2551567c97f68501fa9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b2551567c97f68501fa9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4ad14b946d96c27f50f3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4ad14b946d96c27f50f3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e4a1932204d5e3214c42"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e4a1932204d5e3214c42`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4f45043ed617387559f5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4f45043ed617387559f5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0729c983638e5a231c54"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0729c983638e5a231c54`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2569da04e1a4c6646f6b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2569da04e1a4c6646f6b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4ee0d0489a768042caa2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4ee0d0489a768042caa2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e69bbeb0c8896d4bc177"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e69bbeb0c8896d4bc177`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8aeff58d0f022c7fc45f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8aeff58d0f022c7fc45f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bb40b0119d1006fd1ef7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bb40b0119d1006fd1ef7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-975532ae919784140178"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-975532ae919784140178`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1c3e64af2c00e7b5ef52"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1c3e64af2c00e7b5ef52`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5d26c8a6da9459071846"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5d26c8a6da9459071846`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6c01720c21593f284ead"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6c01720c21593f284ead`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-afa435831beae7dc63d4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-afa435831beae7dc63d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-20cf9c9a5ec8b2232b0b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-20cf9c9a5ec8b2232b0b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-635fd5f6a9b356c15771"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-635fd5f6a9b356c15771`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5be3e86d3ae3ab4e724b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5be3e86d3ae3ab4e724b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bfcab026b2dea096421b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bfcab026b2dea096421b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b3bc555666416d660333"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b3bc555666416d660333`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-71e96fbb07010b7c6bdf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-71e96fbb07010b7c6bdf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a3e8ce22196b8232cec7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a3e8ce22196b8232cec7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-80649314f70d2b4f4f24"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-80649314f70d2b4f4f24`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c0a85205fc36fd391f96"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c0a85205fc36fd391f96`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1db2002e69243f81767d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1db2002e69243f81767d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e7894a1ce3b1cadfac29"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e7894a1ce3b1cadfac29`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-92a10a2983cb640392dc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-92a10a2983cb640392dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-59412cc7a7e6053ee24c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-59412cc7a7e6053ee24c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e3c78c88191498b85191"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e3c78c88191498b85191`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7953f971d8a2b9a03b04"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7953f971d8a2b9a03b04`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-766c2a4b8e5386cc7d0f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-766c2a4b8e5386cc7d0f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e697c817da20214ba0d5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e697c817da20214ba0d5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-46b377fd2bc68cb7ab13"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-46b377fd2bc68cb7ab13`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-09f6483c32de2adec9be"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-09f6483c32de2adec9be`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b274f16513213f68f883"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b274f16513213f68f883`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5df2eba0b97c6576d95a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5df2eba0b97c6576d95a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-00e5238bbad7ec34d62d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-00e5238bbad7ec34d62d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f38093db702d6663f57b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f38093db702d6663f57b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-637ff3b7a0cc86664ab8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-637ff3b7a0cc86664ab8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-33c5334eaa8ad7edea79"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-33c5334eaa8ad7edea79`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-86931637487578b810ac"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-86931637487578b810ac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-419c7eb64fabcc079313"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-419c7eb64fabcc079313`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4dfc2231e228d7d1db0c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4dfc2231e228d7d1db0c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4309105097906fa44b77"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4309105097906fa44b77`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-56e378b57ed8298452cf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-56e378b57ed8298452cf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-205fae828575a1a0f093"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-205fae828575a1a0f093`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d7015d78e1d1e7c4ff3d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d7015d78e1d1e7c4ff3d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ae2ae234615d13d60f90"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ae2ae234615d13d60f90`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5c397f4940c5f23b0f9b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5c397f4940c5f23b0f9b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1670930d88c983b95e49"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1670930d88c983b95e49`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-baa63c8b8dab73d0288d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-baa63c8b8dab73d0288d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e325f90f85d9c3e52301"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e325f90f85d9c3e52301`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a23f4987366819b01828"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a23f4987366819b01828`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0518e1399a95775542ec"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0518e1399a95775542ec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5e1ebeff7853f70c731b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5e1ebeff7853f70c731b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f006a33884e921d22bce"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f006a33884e921d22bce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ad02ec66c08d5b77fb69"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ad02ec66c08d5b77fb69`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-34b615fa0a2da268e657"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-34b615fa0a2da268e657`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2e37eb9252e7decec8b2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2e37eb9252e7decec8b2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-38aebf58f20a032ef391"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-38aebf58f20a032ef391`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7b043fc947bbfa6742bd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7b043fc947bbfa6742bd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8a6a5f5f4fcf9f4d1d74"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8a6a5f5f4fcf9f4d1d74`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-709c4e1c2dc9d49f1ca3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-709c4e1c2dc9d49f1ca3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c1720d19105b1e746577"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c1720d19105b1e746577`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-990af91943b6815bc35b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-990af91943b6815bc35b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d21faf5b858c7fdd9068"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d21faf5b858c7fdd9068`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-38d3ee5af291631cb22f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-38d3ee5af291631cb22f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aba2894ea3ddeda49a9e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-aba2894ea3ddeda49a9e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6350e47728e080d5a8fc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6350e47728e080d5a8fc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-535278c5ef9302a9d6a6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-535278c5ef9302a9d6a6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-017c9a21ec2c52087fa2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-017c9a21ec2c52087fa2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-adb05368965b185f1b74"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-adb05368965b185f1b74`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-034562010273122dfb1a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-034562010273122dfb1a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ea6d55f9fe1568a20de0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ea6d55f9fe1568a20de0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-294a71b543c6e5dc129d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-294a71b543c6e5dc129d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d6349273e73f11ca09f2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d6349273e73f11ca09f2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-40be866cf8b81857170d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-40be866cf8b81857170d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5ecbe9b14d9698c515b3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5ecbe9b14d9698c515b3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-899fff6de4fb590760f0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-899fff6de4fb590760f0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-01e77d7270cb574a26da"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-01e77d7270cb574a26da`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f650a6d91f5f90573511"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f650a6d91f5f90573511`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-59cecd5bdcf210a355ef"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-59cecd5bdcf210a355ef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-49ae9f57f5dc6da29ba7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-49ae9f57f5dc6da29ba7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0b1a06be47bc8fe5cc11"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0b1a06be47bc8fe5cc11`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-dfe9d8d21ce5b761380f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-dfe9d8d21ce5b761380f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-400c99e31a87823bebda"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-400c99e31a87823bebda`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ec0b55735560a09fce21"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ec0b55735560a09fce21`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-59e67bbec9b2cae0e98c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-59e67bbec9b2cae0e98c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7bbcf103a517eff9a862"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7bbcf103a517eff9a862`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3b6a06bb48222cbdb077"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3b6a06bb48222cbdb077`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2f78f227c82ca963d5b9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2f78f227c82ca963d5b9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-82b5c7d646777233a81e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-82b5c7d646777233a81e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-658876f6bca9fbf7643c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-658876f6bca9fbf7643c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-201ea4b2f1701dca128a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-201ea4b2f1701dca128a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8232d9a5a503b5817bc1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8232d9a5a503b5817bc1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-763aa211e2b660c545a9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-763aa211e2b660c545a9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-725c1980f5be35fd8bd7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-725c1980f5be35fd8bd7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-87d632ecec6c23b3c16f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-87d632ecec6c23b3c16f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-125aef2c7baa009174db"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-125aef2c7baa009174db`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f78b55098296d15ced46"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f78b55098296d15ced46`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d25fa09e2b5aa88165ea"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d25fa09e2b5aa88165ea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d1e098df284fb54504f3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d1e098df284fb54504f3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c2216e373d9eb0e8f2ca"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c2216e373d9eb0e8f2ca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9ad57df1478bca810018"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9ad57df1478bca810018`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2dee6943e84f6bd9866b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2dee6943e84f6bd9866b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9361fb6c871501401da6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9361fb6c871501401da6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0f4a8ecffb5609d010ba"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0f4a8ecffb5609d010ba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-43ed391188bb6ae73b6c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-43ed391188bb6ae73b6c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f5f022ca3785ee47e661"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f5f022ca3785ee47e661`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2e38bcad6cebae51d72f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2e38bcad6cebae51d72f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2880b1f2304656d6ca73"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2880b1f2304656d6ca73`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a98d019767124c914b88"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a98d019767124c914b88`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-891a6da76a16c5af8add"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-891a6da76a16c5af8add`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fd73473782efd8910ee9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fd73473782efd8910ee9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a349bcdb3d24faabeb7d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a349bcdb3d24faabeb7d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-75d515a5b20a58aa4d49"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-75d515a5b20a58aa4d49`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2f612b963456ee7e7fa6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2f612b963456ee7e7fa6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ba6a590ea21810404c1e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ba6a590ea21810404c1e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8f7e7b422ea2d8738a5a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8f7e7b422ea2d8738a5a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3fa35807a2d273e78e77"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3fa35807a2d273e78e77`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b1f2024834557f40182c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b1f2024834557f40182c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2169f314f03960808edf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2169f314f03960808edf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-59e5b1670178e6d8ae65"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-59e5b1670178e6d8ae65`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c1ae35a12f636c2d26c8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c1ae35a12f636c2d26c8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-20-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-parallel-upper-exit-slip:canonical-southeast | <a href="#case-preview_review-4103c5e47fd467f86632">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-upper-exit-slip:canonical-top | <a href="#case-preview_review-89405a7692900cd9617f">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-upper-exit-slip:connection-overview | <a href="#case-preview_review-5614cf9db5396bc4e1a4">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-parallel-upper-exit-slip:canonical-southeast</summary>

<a id="case-preview_review-4103c5e47fd467f86632"></a>

**General: unverified** — `preview_review-4103c5e47fd467f86632`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-upper-exit-slip:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-upper-exit-slip:canonical-top</summary>

<a id="case-preview_review-89405a7692900cd9617f"></a>

**General: unverified** — `preview_review-89405a7692900cd9617f`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-upper-exit-slip:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-upper-exit-slip:connection-overview</summary>

<a id="case-preview_review-5614cf9db5396bc4e1a4"></a>

**General: unverified** — `preview_review-5614cf9db5396bc4e1a4`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-upper-exit-slip:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

This new type implements one functional part of the human-approved close parallel layout. It preserves the [frozen source proposal](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/TESTING.md#32-close-parallel-ramps-and-perpendicular-avenue-approaches) and leaves the retained R40 and compact assemblies available with their own resource identities and evidence. This piece's exact source is [piece.jsonc](piece.jsonc); the shared placement plan is [assembly.jsonc](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/assembly.jsonc).

The ground-mouth revision narrowed terminal asphalt while preserving the 6 m grade interfaces and its saved traffic routes. The later slip-lane revision lengthens the shoulder treatment and changes its access PATHs and white markings, while retaining all fifteen permanent types, the 31-cell union, and those narrow ground mouths. The earlier `ddrhw-parallel-diamond-parts-01` and `ddrhw-parallel-diamond-pedestrian-mouths-01` build identities retain their original scopes. The current revision uses `ddrhw-parallel-diamond-slip-lanes-02`; only its own matching saved-resource report can establish its software result.
