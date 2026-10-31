---
title: "Testing: DD RHW-4 — L1 Entry Slip Lanes — Parallel"
summary: "Check this parallel component against its saved resources and retain separate human game observations."
audience: "contributors"
document_type: "reference"
---

# Testing: DD RHW-4 — L1 Entry Slip Lanes — Parallel

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

This record covers **ddrhw-parallel-lower-entry-slip**, used once as **P05** in the [parallel diamond](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/README.md). It has 2 occupied tiles in a 2 × 2 rectangle, the exact authored 0° reference at X1, Y3, and the functional levels described in the [piece guide](README.md#2-piece-and-placement). Saved native through routes, added access fragments, actual model support, material flags, physical joins, rotations, and adaptive resources where present have distinct software checks. Human appearance and travel observations remain separate.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `channel-11-out` | road / 1 / primary | out | [-3.2, -24.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `channel-01-in` | road / 1 / primary | in | [-3.2, -24.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `channel-02-in` | road / 1 / primary | in | [-0.104467, -8.0, 7.5]; [-0.3399082425091487, -0.9404586044448431]; 0.0 | `path-interface-48c3c82aba723ead8555` |
| `channel-12-out` | road / 1 / primary | out | [3.2, -24.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `channel-03-in` | road / 1 / primary | in | [3.2, -24.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `channel-04-in` | road / 1 / primary | in | [8.0, -19.2, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `channel-13-out` | road / 1 / primary | out | [8.0, -19.2, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `channel-05-in` | road / 1 / primary | in | [8.0, -12.8, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `channel-14-out` | road / 1 / primary | out | [8.0, -12.8, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `channel-15-out` | road / 1 / primary | out | [8.0, 0.970563, 6.144726]; [-0.7071067811865476, -0.7071067811865476]; 0.17907534 | `path-interface-bdb541c0b77034d43fb5` |
| `channel-16-out` | road / 1 / primary | out | [12.8, -8.0, 7.5]; [-0.7071067811865477, -0.7071067811865475]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `channel-06-in` | road / 1 / primary | in | [12.8, -8.0, 15.0]; [0.7071067811865477, 0.7071067811865475]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `channel-07-in` | road / 1 / primary | in | [15.029437, 8.0, 4.364109]; [-0.7071067811865365, -0.7071067811865587]; 0.179118533 | `path-interface-58833f9593752a9d0c32` |
| `channel-17-out` | road / 1 / primary | out | [19.2, -8.0, 7.5]; [-0.7071067811865478, -0.7071067811865474]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `channel-08-in` | road / 1 / primary | in | [19.2, -8.0, 15.0]; [0.7071067811865478, 0.7071067811865474]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `channel-09-in` | road / 1 / primary | in | [24.0, -3.2, 7.5]; [-0.7071067811865478, -0.7071067811865474]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `channel-18-out` | road / 1 / primary | out | [24.0, -3.2, 15.0]; [0.7071067811865478, 0.7071067811865474]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `channel-10-in` | road / 1 / primary | in | [24.0, 3.2, 7.5]; [-0.7071067811865477, -0.7071067811865475]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `channel-19-out` | road / 1 / primary | out | [24.0, 3.2, 15.0]; [0.7071067811865477, 0.7071067811865475]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `channel-01-in` → `channel-14-out` | primary |
| road | `channel-02-in` → `channel-11-out` | primary |
| road | `channel-03-in` → `channel-13-out` | primary |
| road | `channel-04-in` → `channel-12-out` | primary |
| road | `channel-05-in` → `channel-11-out` | primary |
| road | `channel-06-in` → `channel-19-out` | primary |
| road | `channel-07-in` → `channel-15-out` | primary |
| road | `channel-08-in` → `channel-18-out` | primary |
| road | `channel-09-in` → `channel-17-out` | primary |
| road | `channel-10-in` → `channel-16-out` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `channel-01-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-01-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-02-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-03-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-04-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-05-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-06-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-18-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-07-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-17-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-08-in` | road / `channel-19-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-11-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-12-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-13-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-14-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-15-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `channel-09-in` | road / `channel-16-out` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
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

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use Windows SimCity 4 with the pinned NAM 50 right-hand-traffic inputs, including through Wine or CrossOver. The shared [build guide](../../../../docs/BUILD_AND_INSTALL.md) owns private input settings and explicit installation. Use the complete fifteen-component assembly for travel tests: this individual component can expose required route fragments at more than one city-tile edge. A matching-looking isolated end is insufficient to create the whole journey.

Prepare the [assembly's flat reference test area](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#2-test-setup), keep the camera north-up for placement, and use the exact occupied cells **(X2, Y3), (X1, Y2)**. The full core occupies 31 cells inside X1–X8 and Y1–Y8; the preserved drawing reference still shows X0–X9 and Y0–Y9. One tile is 16 m. Additional outside road approaches are separate from that core count.

## 3. Software checks

Run from the repository directory containing `custom-pieces/`. These commands inspect an existing build and its current source-bound connector records; they do not install anything, supply missing inputs, or approve a manual case. An absent or failing report is not a software pass.

```sh
python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/ddrhw-parallel-diamond-pedestrian-mouths-01
python3 -B custom-pieces/scp.py connectors check --domain highway --piece ddrhw-parallel-lower-entry-slip --build dist/ddrhw-parallel-diamond-pedestrian-mouths-01
python3 -B custom-pieces/scp.py docs-check --piece ddrhw-parallel-lower-entry-slip
```

The [complete saved-assembly check](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#3-software-checks) checks this component in all fifteen placements, including physical model overhang and the traffic fragments owned by its neighbours. The ordinary build's manifest and verification report identify the actual measured resources. Retain every software failure with its source fingerprint; rerunning a renderer cannot repair it.

The current revision changes only the two ground terminals' visible asphalt width: each retains its 6 m grade join, narrows to 3.5 m over 3 m, and stays narrow through its R6 turn and Avenue joining collar. The ramp centreline crosses the retained pedestrian-route centreline 3.258752 m from the grade join, after the 3 m taper is complete. The asphalt footprint reaches the pedestrian route earlier, while the taper is still narrowing; this is the actual driveway crossing. Traffic PATHs, permanent identifiers, construction ownership, and the other thirteen physical components retain their previous scope. This component supplies highway or ramp geometry. The three ground components P01, P02, and P03 own the implemented adaptive Avenue pavement and retained pedestrian routes. Connecting this elevated component does not itself select a sidewalk appearance. Read the [actual mechanism and limits](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/TESTING.md#3-software-checks).

## 4. Game checks

1. Select this exact component through the assembly button, match P05 at **X1, Y3**, and confirm that the occupied preview squares match **(X2, Y3), (X1, Y2)** before clicking.
2. Place the full assembly using the order in its guide. Inspect this component's saved model from both opposing oblique views, and compare its real join with the neighbouring models; look for gaps, blocked barrier openings, misplaced supports, or a sudden pavement-colour patch.
3. Repeat fresh placement in the four distinct proper rotations. Rotate the camera separately after placement, because camera movement and a newly rotated piece test different things.
4. For an adaptive Avenue cell, connect ordinary Avenue outside the core, add nearby development, and compare its pavement variant with the neighbouring Avenue. Connecting the Avenue alone does not select the developed pavement appearance. Inspect both narrow driveway crossings, then check pedestrian Route Query and visible walking separately; a sidewalk image does not create a pedestrian PATH, and the crossing remains road asphalt. For a component without Avenue cells, inspect the neighbouring adaptive owners instead of expecting this piece to change pavement itself.
5. Run every required car and pedestrian journey listed by the exact matrix. Record Route Query and visible travel separately. Also confirm that every declared forbidden transfer stays unavailable; a visually clear road surface is not traffic evidence.
6. Inspect shadows, demolish the component, replace it, save the city, quit completely, and reload. Check that no temporary placement handle remains and that the component and its traffic neighbours remain correct.

Record only explicit observations through [the shared observation workflow](../../../../docs/TESTING.md), selecting **ddrhw-parallel-lower-entry-slip** and its exact current cases. No observation of the older adaptive probe, R40 diamond, or another rotation automatically approves this new component.

## 5. Results and known issues

The implementation is experimental. The generated records below are authoritative for the current evidence scope; **all new human game observations remain unverified** until the user confirms their exact cases. In particular, outside native DD RHW connections, over-Avenue placement, Avenue redraw, temporary-handle collision behaviour, pedestrian pavement variants, moving traffic, camera rotations, demolition, and save/reload require game checks.

The whole-cell traffic partition is intentionally different from the physical model split. The two occupied cells lie diagonally inside a sparse 2 × 2 rectangle. Its construction reference is an empty corner, so align both occupied preview cells instead of assuming that the reference position is a third tile. Complete boundary cards include both highway levels and every access fragment; matching only the named ramp is insufficient. This is a limitation to understand when choosing replacement modules, not permission to discard a required boundary service.

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

Current totals: unverified: 421, passed: 0, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-parallel-lower-entry-slip/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-parallel-lower-entry-slip/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-311b633728bfe92c407c">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-311b633728bfe92c407c"></a>

**General: unverified** — `software_resources-311b633728bfe92c407c`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-311b633728bfe92c407c">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-311b633728bfe92c407c"></a>

**General: unverified** — `software_connectivity-311b633728bfe92c407c`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-a3bd188382bef08c9463">[ ] unverified</a> | <a href="#case-in_game_render-9eaac7e86e34562d1ea1">[ ] unverified</a> | <a href="#case-in_game_render-626c0fc57e6ed875cd11">[ ] unverified</a> | <a href="#case-in_game_render-8808184965606d5a7b3c">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-a3bd188382bef08c9463"></a>

**0° CCW: unverified** — `in_game_render-a3bd188382bef08c9463`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-9eaac7e86e34562d1ea1"></a>

**90° CCW: unverified** — `in_game_render-9eaac7e86e34562d1ea1`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-626c0fc57e6ed875cd11"></a>

**180° CCW: unverified** — `in_game_render-626c0fc57e6ed875cd11`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-8808184965606d5a7b3c"></a>

**270° CCW: unverified** — `in_game_render-8808184965606d5a7b3c`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-a3bd188382bef08c9463">[ ] unverified</a> | <a href="#case-in_game_placement-9eaac7e86e34562d1ea1">[ ] unverified</a> | <a href="#case-in_game_placement-626c0fc57e6ed875cd11">[ ] unverified</a> | <a href="#case-in_game_placement-8808184965606d5a7b3c">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-a3bd188382bef08c9463"></a>

**0° CCW: unverified** — `in_game_placement-a3bd188382bef08c9463`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-9eaac7e86e34562d1ea1"></a>

**90° CCW: unverified** — `in_game_placement-9eaac7e86e34562d1ea1`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-626c0fc57e6ed875cd11"></a>

**180° CCW: unverified** — `in_game_placement-626c0fc57e6ed875cd11`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-8808184965606d5a7b3c"></a>

**270° CCW: unverified** — `in_game_placement-8808184965606d5a7b3c`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-a3bd188382bef08c9463">[ ] unverified</a> | <a href="#case-in_game_demolition-9eaac7e86e34562d1ea1">[ ] unverified</a> | <a href="#case-in_game_demolition-626c0fc57e6ed875cd11">[ ] unverified</a> | <a href="#case-in_game_demolition-8808184965606d5a7b3c">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-a3bd188382bef08c9463"></a>

**0° CCW: unverified** — `in_game_demolition-a3bd188382bef08c9463`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-9eaac7e86e34562d1ea1"></a>

**90° CCW: unverified** — `in_game_demolition-9eaac7e86e34562d1ea1`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-626c0fc57e6ed875cd11"></a>

**180° CCW: unverified** — `in_game_demolition-626c0fc57e6ed875cd11`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-8808184965606d5a7b3c"></a>

**270° CCW: unverified** — `in_game_demolition-8808184965606d5a7b3c`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-a3bd188382bef08c9463">[ ] unverified</a> | <a href="#case-in_game_save_reload-9eaac7e86e34562d1ea1">[ ] unverified</a> | <a href="#case-in_game_save_reload-626c0fc57e6ed875cd11">[ ] unverified</a> | <a href="#case-in_game_save_reload-8808184965606d5a7b3c">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-a3bd188382bef08c9463"></a>

**0° CCW: unverified** — `in_game_save_reload-a3bd188382bef08c9463`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-9eaac7e86e34562d1ea1"></a>

**90° CCW: unverified** — `in_game_save_reload-9eaac7e86e34562d1ea1`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-626c0fc57e6ed875cd11"></a>

**180° CCW: unverified** — `in_game_save_reload-626c0fc57e6ed875cd11`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-8808184965606d5a7b3c"></a>

**270° CCW: unverified** — `in_game_save_reload-8808184965606d5a7b3c`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 40 cases; unverified: 40</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out | — | <a href="#case-in_game_route_query-d1cdc890eaf86fd188a8">[ ] unverified</a> | <a href="#case-in_game_route_query-730ea60a125dc4a4de6d">[ ] unverified</a> | <a href="#case-in_game_route_query-43ddfb9f7c28c70ca00e">[ ] unverified</a> | <a href="#case-in_game_route_query-ff82aef4d9a94187e56a">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-11-out; entry: channel-02-in; exit: channel-11-out | — | <a href="#case-in_game_route_query-946a2c6ee75daa793b94">[ ] unverified</a> | <a href="#case-in_game_route_query-83251aa883fd2c95bfbb">[ ] unverified</a> | <a href="#case-in_game_route_query-d8668ca19b2d4ce4ade3">[ ] unverified</a> | <a href="#case-in_game_route_query-292810e993b543c8626b">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-13-out; entry: channel-03-in; exit: channel-13-out | — | <a href="#case-in_game_route_query-5cccc8479e80b1a566c6">[ ] unverified</a> | <a href="#case-in_game_route_query-695202aaf0f232b52fe5">[ ] unverified</a> | <a href="#case-in_game_route_query-cfef215cd306b789a191">[ ] unverified</a> | <a href="#case-in_game_route_query-7974a5d5c84679a3d212">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out | — | <a href="#case-in_game_route_query-35bd0b7cdb84fdba7f89">[ ] unverified</a> | <a href="#case-in_game_route_query-845c9cd4adba50838d66">[ ] unverified</a> | <a href="#case-in_game_route_query-f3057d936d9bb49de214">[ ] unverified</a> | <a href="#case-in_game_route_query-1bf33a70ddca838fe85e">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out | — | <a href="#case-in_game_route_query-83e473750ab4f2bd499e">[ ] unverified</a> | <a href="#case-in_game_route_query-6b11b213cbb60b37b94f">[ ] unverified</a> | <a href="#case-in_game_route_query-ca6f89f3b689647c2555">[ ] unverified</a> | <a href="#case-in_game_route_query-06837326516f968675d6">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out | — | <a href="#case-in_game_route_query-c9577c70736b483a4245">[ ] unverified</a> | <a href="#case-in_game_route_query-c918b90b9a095b5db5af">[ ] unverified</a> | <a href="#case-in_game_route_query-1f208c6f16b9d97a3c50">[ ] unverified</a> | <a href="#case-in_game_route_query-9a0fd7ab90f2ecc04323">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-07-in>channel-15-out; entry: channel-07-in; exit: channel-15-out | — | <a href="#case-in_game_route_query-17a917ccfe3146c7aa19">[ ] unverified</a> | <a href="#case-in_game_route_query-9f65502a8f5534b541ba">[ ] unverified</a> | <a href="#case-in_game_route_query-7dd1094ac33be5b97602">[ ] unverified</a> | <a href="#case-in_game_route_query-05f3eeea4fe49b716a3c">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out | — | <a href="#case-in_game_route_query-d60259cf72572e68df9e">[ ] unverified</a> | <a href="#case-in_game_route_query-09fbca67a15faaf9a0f2">[ ] unverified</a> | <a href="#case-in_game_route_query-f298285cf2e6bc869be9">[ ] unverified</a> | <a href="#case-in_game_route_query-869f2c0b63b460ce008a">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-09-in>channel-17-out; entry: channel-09-in; exit: channel-17-out | — | <a href="#case-in_game_route_query-c85ec139cbad546d4c90">[ ] unverified</a> | <a href="#case-in_game_route_query-4274d3f2f873d7f9ecd6">[ ] unverified</a> | <a href="#case-in_game_route_query-0cab6a881d7afb1debef">[ ] unverified</a> | <a href="#case-in_game_route_query-61108446d97ee624c63a">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out | — | <a href="#case-in_game_route_query-5eaf01044ad42856d703">[ ] unverified</a> | <a href="#case-in_game_route_query-d1a6d6c90bdb40c69f76">[ ] unverified</a> | <a href="#case-in_game_route_query-6676dc41f343dc41b0ad">[ ] unverified</a> | <a href="#case-in_game_route_query-0be4708565edf1a27268">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out</summary>

<a id="case-in_game_route_query-d1cdc890eaf86fd188a8"></a>

**0° CCW: unverified** — `in_game_route_query-d1cdc890eaf86fd188a8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_route_query-730ea60a125dc4a4de6d"></a>

**90° CCW: unverified** — `in_game_route_query-730ea60a125dc4a4de6d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_route_query-43ddfb9f7c28c70ca00e"></a>

**180° CCW: unverified** — `in_game_route_query-43ddfb9f7c28c70ca00e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_route_query-ff82aef4d9a94187e56a"></a>

**270° CCW: unverified** — `in_game_route_query-ff82aef4d9a94187e56a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-02-in>channel-11-out; entry: channel-02-in; exit: channel-11-out</summary>

<a id="case-in_game_route_query-946a2c6ee75daa793b94"></a>

**0° CCW: unverified** — `in_game_route_query-946a2c6ee75daa793b94`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-11-out; entry: channel-02-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_route_query-83251aa883fd2c95bfbb"></a>

**90° CCW: unverified** — `in_game_route_query-83251aa883fd2c95bfbb`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-11-out; entry: channel-02-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_route_query-d8668ca19b2d4ce4ade3"></a>

**180° CCW: unverified** — `in_game_route_query-d8668ca19b2d4ce4ade3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-11-out; entry: channel-02-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_route_query-292810e993b543c8626b"></a>

**270° CCW: unverified** — `in_game_route_query-292810e993b543c8626b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-11-out; entry: channel-02-in; exit: channel-11-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-03-in>channel-13-out; entry: channel-03-in; exit: channel-13-out</summary>

<a id="case-in_game_route_query-5cccc8479e80b1a566c6"></a>

**0° CCW: unverified** — `in_game_route_query-5cccc8479e80b1a566c6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-13-out; entry: channel-03-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_route_query-695202aaf0f232b52fe5"></a>

**90° CCW: unverified** — `in_game_route_query-695202aaf0f232b52fe5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-13-out; entry: channel-03-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_route_query-cfef215cd306b789a191"></a>

**180° CCW: unverified** — `in_game_route_query-cfef215cd306b789a191`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-13-out; entry: channel-03-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_route_query-7974a5d5c84679a3d212"></a>

**270° CCW: unverified** — `in_game_route_query-7974a5d5c84679a3d212`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-13-out; entry: channel-03-in; exit: channel-13-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out</summary>

<a id="case-in_game_route_query-35bd0b7cdb84fdba7f89"></a>

**0° CCW: unverified** — `in_game_route_query-35bd0b7cdb84fdba7f89`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_route_query-845c9cd4adba50838d66"></a>

**90° CCW: unverified** — `in_game_route_query-845c9cd4adba50838d66`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_route_query-f3057d936d9bb49de214"></a>

**180° CCW: unverified** — `in_game_route_query-f3057d936d9bb49de214`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_route_query-1bf33a70ddca838fe85e"></a>

**270° CCW: unverified** — `in_game_route_query-1bf33a70ddca838fe85e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out</summary>

<a id="case-in_game_route_query-83e473750ab4f2bd499e"></a>

**0° CCW: unverified** — `in_game_route_query-83e473750ab4f2bd499e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_route_query-6b11b213cbb60b37b94f"></a>

**90° CCW: unverified** — `in_game_route_query-6b11b213cbb60b37b94f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_route_query-ca6f89f3b689647c2555"></a>

**180° CCW: unverified** — `in_game_route_query-ca6f89f3b689647c2555`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_route_query-06837326516f968675d6"></a>

**270° CCW: unverified** — `in_game_route_query-06837326516f968675d6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out</summary>

<a id="case-in_game_route_query-c9577c70736b483a4245"></a>

**0° CCW: unverified** — `in_game_route_query-c9577c70736b483a4245`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_route_query-c918b90b9a095b5db5af"></a>

**90° CCW: unverified** — `in_game_route_query-c918b90b9a095b5db5af`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_route_query-1f208c6f16b9d97a3c50"></a>

**180° CCW: unverified** — `in_game_route_query-1f208c6f16b9d97a3c50`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_route_query-9a0fd7ab90f2ecc04323"></a>

**270° CCW: unverified** — `in_game_route_query-9a0fd7ab90f2ecc04323`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-07-in>channel-15-out; entry: channel-07-in; exit: channel-15-out</summary>

<a id="case-in_game_route_query-17a917ccfe3146c7aa19"></a>

**0° CCW: unverified** — `in_game_route_query-17a917ccfe3146c7aa19`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-15-out; entry: channel-07-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_route_query-9f65502a8f5534b541ba"></a>

**90° CCW: unverified** — `in_game_route_query-9f65502a8f5534b541ba`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-15-out; entry: channel-07-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_route_query-7dd1094ac33be5b97602"></a>

**180° CCW: unverified** — `in_game_route_query-7dd1094ac33be5b97602`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-15-out; entry: channel-07-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_route_query-05f3eeea4fe49b716a3c"></a>

**270° CCW: unverified** — `in_game_route_query-05f3eeea4fe49b716a3c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-15-out; entry: channel-07-in; exit: channel-15-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out</summary>

<a id="case-in_game_route_query-d60259cf72572e68df9e"></a>

**0° CCW: unverified** — `in_game_route_query-d60259cf72572e68df9e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_route_query-09fbca67a15faaf9a0f2"></a>

**90° CCW: unverified** — `in_game_route_query-09fbca67a15faaf9a0f2`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_route_query-f298285cf2e6bc869be9"></a>

**180° CCW: unverified** — `in_game_route_query-f298285cf2e6bc869be9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_route_query-869f2c0b63b460ce008a"></a>

**270° CCW: unverified** — `in_game_route_query-869f2c0b63b460ce008a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-09-in>channel-17-out; entry: channel-09-in; exit: channel-17-out</summary>

<a id="case-in_game_route_query-c85ec139cbad546d4c90"></a>

**0° CCW: unverified** — `in_game_route_query-c85ec139cbad546d4c90`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-17-out; entry: channel-09-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_route_query-4274d3f2f873d7f9ecd6"></a>

**90° CCW: unverified** — `in_game_route_query-4274d3f2f873d7f9ecd6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-17-out; entry: channel-09-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_route_query-0cab6a881d7afb1debef"></a>

**180° CCW: unverified** — `in_game_route_query-0cab6a881d7afb1debef`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-17-out; entry: channel-09-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_route_query-61108446d97ee624c63a"></a>

**270° CCW: unverified** — `in_game_route_query-61108446d97ee624c63a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-17-out; entry: channel-09-in; exit: channel-17-out.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out</summary>

<a id="case-in_game_route_query-5eaf01044ad42856d703"></a>

**0° CCW: unverified** — `in_game_route_query-5eaf01044ad42856d703`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_route_query-d1a6d6c90bdb40c69f76"></a>

**90° CCW: unverified** — `in_game_route_query-d1a6d6c90bdb40c69f76`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_route_query-6676dc41f343dc41b0ad"></a>

**180° CCW: unverified** — `in_game_route_query-6676dc41f343dc41b0ad`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_route_query-0be4708565edf1a27268"></a>

**270° CCW: unverified** — `in_game_route_query-0be4708565edf1a27268`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 40 cases; unverified: 40</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out | — | <a href="#case-in_game_visible_travel-d1cdc890eaf86fd188a8">[ ] unverified</a> | <a href="#case-in_game_visible_travel-730ea60a125dc4a4de6d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-43ddfb9f7c28c70ca00e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ff82aef4d9a94187e56a">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-02-in>channel-11-out; entry: channel-02-in; exit: channel-11-out | — | <a href="#case-in_game_visible_travel-946a2c6ee75daa793b94">[ ] unverified</a> | <a href="#case-in_game_visible_travel-83251aa883fd2c95bfbb">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d8668ca19b2d4ce4ade3">[ ] unverified</a> | <a href="#case-in_game_visible_travel-292810e993b543c8626b">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-03-in>channel-13-out; entry: channel-03-in; exit: channel-13-out | — | <a href="#case-in_game_visible_travel-5cccc8479e80b1a566c6">[ ] unverified</a> | <a href="#case-in_game_visible_travel-695202aaf0f232b52fe5">[ ] unverified</a> | <a href="#case-in_game_visible_travel-cfef215cd306b789a191">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7974a5d5c84679a3d212">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out | — | <a href="#case-in_game_visible_travel-35bd0b7cdb84fdba7f89">[ ] unverified</a> | <a href="#case-in_game_visible_travel-845c9cd4adba50838d66">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f3057d936d9bb49de214">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1bf33a70ddca838fe85e">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out | — | <a href="#case-in_game_visible_travel-83e473750ab4f2bd499e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6b11b213cbb60b37b94f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ca6f89f3b689647c2555">[ ] unverified</a> | <a href="#case-in_game_visible_travel-06837326516f968675d6">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out | — | <a href="#case-in_game_visible_travel-c9577c70736b483a4245">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c918b90b9a095b5db5af">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1f208c6f16b9d97a3c50">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9a0fd7ab90f2ecc04323">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-07-in>channel-15-out; entry: channel-07-in; exit: channel-15-out | — | <a href="#case-in_game_visible_travel-17a917ccfe3146c7aa19">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9f65502a8f5534b541ba">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7dd1094ac33be5b97602">[ ] unverified</a> | <a href="#case-in_game_visible_travel-05f3eeea4fe49b716a3c">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out | — | <a href="#case-in_game_visible_travel-d60259cf72572e68df9e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-09fbca67a15faaf9a0f2">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f298285cf2e6bc869be9">[ ] unverified</a> | <a href="#case-in_game_visible_travel-869f2c0b63b460ce008a">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-09-in>channel-17-out; entry: channel-09-in; exit: channel-17-out | — | <a href="#case-in_game_visible_travel-c85ec139cbad546d4c90">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4274d3f2f873d7f9ecd6">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0cab6a881d7afb1debef">[ ] unverified</a> | <a href="#case-in_game_visible_travel-61108446d97ee624c63a">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out | — | <a href="#case-in_game_visible_travel-5eaf01044ad42856d703">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d1a6d6c90bdb40c69f76">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6676dc41f343dc41b0ad">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0be4708565edf1a27268">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out</summary>

<a id="case-in_game_visible_travel-d1cdc890eaf86fd188a8"></a>

**0° CCW: unverified** — `in_game_visible_travel-d1cdc890eaf86fd188a8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_visible_travel-730ea60a125dc4a4de6d"></a>

**90° CCW: unverified** — `in_game_visible_travel-730ea60a125dc4a4de6d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_visible_travel-43ddfb9f7c28c70ca00e"></a>

**180° CCW: unverified** — `in_game_visible_travel-43ddfb9f7c28c70ca00e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

<a id="case-in_game_visible_travel-ff82aef4d9a94187e56a"></a>

**270° CCW: unverified** — `in_game_visible_travel-ff82aef4d9a94187e56a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-01-in>channel-14-out; entry: channel-01-in; exit: channel-14-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-02-in>channel-11-out; entry: channel-02-in; exit: channel-11-out</summary>

<a id="case-in_game_visible_travel-946a2c6ee75daa793b94"></a>

**0° CCW: unverified** — `in_game_visible_travel-946a2c6ee75daa793b94`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-11-out; entry: channel-02-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_visible_travel-83251aa883fd2c95bfbb"></a>

**90° CCW: unverified** — `in_game_visible_travel-83251aa883fd2c95bfbb`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-11-out; entry: channel-02-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_visible_travel-d8668ca19b2d4ce4ade3"></a>

**180° CCW: unverified** — `in_game_visible_travel-d8668ca19b2d4ce4ade3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-11-out; entry: channel-02-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_visible_travel-292810e993b543c8626b"></a>

**270° CCW: unverified** — `in_game_visible_travel-292810e993b543c8626b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-02-in>channel-11-out; entry: channel-02-in; exit: channel-11-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-03-in>channel-13-out; entry: channel-03-in; exit: channel-13-out</summary>

<a id="case-in_game_visible_travel-5cccc8479e80b1a566c6"></a>

**0° CCW: unverified** — `in_game_visible_travel-5cccc8479e80b1a566c6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-13-out; entry: channel-03-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_visible_travel-695202aaf0f232b52fe5"></a>

**90° CCW: unverified** — `in_game_visible_travel-695202aaf0f232b52fe5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-13-out; entry: channel-03-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_visible_travel-cfef215cd306b789a191"></a>

**180° CCW: unverified** — `in_game_visible_travel-cfef215cd306b789a191`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-13-out; entry: channel-03-in; exit: channel-13-out.

No observation recorded.

<a id="case-in_game_visible_travel-7974a5d5c84679a3d212"></a>

**270° CCW: unverified** — `in_game_visible_travel-7974a5d5c84679a3d212`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-03-in>channel-13-out; entry: channel-03-in; exit: channel-13-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out</summary>

<a id="case-in_game_visible_travel-35bd0b7cdb84fdba7f89"></a>

**0° CCW: unverified** — `in_game_visible_travel-35bd0b7cdb84fdba7f89`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_visible_travel-845c9cd4adba50838d66"></a>

**90° CCW: unverified** — `in_game_visible_travel-845c9cd4adba50838d66`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_visible_travel-f3057d936d9bb49de214"></a>

**180° CCW: unverified** — `in_game_visible_travel-f3057d936d9bb49de214`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out.

No observation recorded.

<a id="case-in_game_visible_travel-1bf33a70ddca838fe85e"></a>

**270° CCW: unverified** — `in_game_visible_travel-1bf33a70ddca838fe85e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-04-in>channel-12-out; entry: channel-04-in; exit: channel-12-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out</summary>

<a id="case-in_game_visible_travel-83e473750ab4f2bd499e"></a>

**0° CCW: unverified** — `in_game_visible_travel-83e473750ab4f2bd499e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_visible_travel-6b11b213cbb60b37b94f"></a>

**90° CCW: unverified** — `in_game_visible_travel-6b11b213cbb60b37b94f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_visible_travel-ca6f89f3b689647c2555"></a>

**180° CCW: unverified** — `in_game_visible_travel-ca6f89f3b689647c2555`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

<a id="case-in_game_visible_travel-06837326516f968675d6"></a>

**270° CCW: unverified** — `in_game_visible_travel-06837326516f968675d6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-05-in>channel-11-out; entry: channel-05-in; exit: channel-11-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out</summary>

<a id="case-in_game_visible_travel-c9577c70736b483a4245"></a>

**0° CCW: unverified** — `in_game_visible_travel-c9577c70736b483a4245`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_visible_travel-c918b90b9a095b5db5af"></a>

**90° CCW: unverified** — `in_game_visible_travel-c918b90b9a095b5db5af`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_visible_travel-1f208c6f16b9d97a3c50"></a>

**180° CCW: unverified** — `in_game_visible_travel-1f208c6f16b9d97a3c50`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out.

No observation recorded.

<a id="case-in_game_visible_travel-9a0fd7ab90f2ecc04323"></a>

**270° CCW: unverified** — `in_game_visible_travel-9a0fd7ab90f2ecc04323`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-06-in>channel-19-out; entry: channel-06-in; exit: channel-19-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-07-in>channel-15-out; entry: channel-07-in; exit: channel-15-out</summary>

<a id="case-in_game_visible_travel-17a917ccfe3146c7aa19"></a>

**0° CCW: unverified** — `in_game_visible_travel-17a917ccfe3146c7aa19`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-15-out; entry: channel-07-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_visible_travel-9f65502a8f5534b541ba"></a>

**90° CCW: unverified** — `in_game_visible_travel-9f65502a8f5534b541ba`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-15-out; entry: channel-07-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_visible_travel-7dd1094ac33be5b97602"></a>

**180° CCW: unverified** — `in_game_visible_travel-7dd1094ac33be5b97602`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-15-out; entry: channel-07-in; exit: channel-15-out.

No observation recorded.

<a id="case-in_game_visible_travel-05f3eeea4fe49b716a3c"></a>

**270° CCW: unverified** — `in_game_visible_travel-05f3eeea4fe49b716a3c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-07-in>channel-15-out; entry: channel-07-in; exit: channel-15-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out</summary>

<a id="case-in_game_visible_travel-d60259cf72572e68df9e"></a>

**0° CCW: unverified** — `in_game_visible_travel-d60259cf72572e68df9e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_visible_travel-09fbca67a15faaf9a0f2"></a>

**90° CCW: unverified** — `in_game_visible_travel-09fbca67a15faaf9a0f2`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_visible_travel-f298285cf2e6bc869be9"></a>

**180° CCW: unverified** — `in_game_visible_travel-f298285cf2e6bc869be9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out.

No observation recorded.

<a id="case-in_game_visible_travel-869f2c0b63b460ce008a"></a>

**270° CCW: unverified** — `in_game_visible_travel-869f2c0b63b460ce008a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-08-in>channel-18-out; entry: channel-08-in; exit: channel-18-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-09-in>channel-17-out; entry: channel-09-in; exit: channel-17-out</summary>

<a id="case-in_game_visible_travel-c85ec139cbad546d4c90"></a>

**0° CCW: unverified** — `in_game_visible_travel-c85ec139cbad546d4c90`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-17-out; entry: channel-09-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_visible_travel-4274d3f2f873d7f9ecd6"></a>

**90° CCW: unverified** — `in_game_visible_travel-4274d3f2f873d7f9ecd6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-17-out; entry: channel-09-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_visible_travel-0cab6a881d7afb1debef"></a>

**180° CCW: unverified** — `in_game_visible_travel-0cab6a881d7afb1debef`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-17-out; entry: channel-09-in; exit: channel-17-out.

No observation recorded.

<a id="case-in_game_visible_travel-61108446d97ee624c63a"></a>

**270° CCW: unverified** — `in_game_visible_travel-61108446d97ee624c63a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-09-in>channel-17-out; entry: channel-09-in; exit: channel-17-out.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out</summary>

<a id="case-in_game_visible_travel-5eaf01044ad42856d703"></a>

**0° CCW: unverified** — `in_game_visible_travel-5eaf01044ad42856d703`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_visible_travel-d1a6d6c90bdb40c69f76"></a>

**90° CCW: unverified** — `in_game_visible_travel-d1a6d6c90bdb40c69f76`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_visible_travel-6676dc41f343dc41b0ad"></a>

**180° CCW: unverified** — `in_game_visible_travel-6676dc41f343dc41b0ad`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out.

No observation recorded.

<a id="case-in_game_visible_travel-0be4708565edf1a27268"></a>

**270° CCW: unverified** — `in_game_visible_travel-0be4708565edf1a27268`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:channel-10-in>channel-16-out; entry: channel-10-in; exit: channel-16-out.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 320 cases; unverified: 320</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6cb386346968a166f71b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f6d7bf247f4dc9e7b759">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eecce2faec764577b864">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a89ac9ded09b59dd7171">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-22075f8465f1bcc67cbf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e485026a3f8446ac8e79">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-542a09c4efd2cd29b22a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c70668ab62f08975ce1e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-42edd6ba43c150054c91">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8ac3d04df0793286dbca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7b03c7971745eeaab941">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-11cf99ceb27d774698b7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-60ea056a4d00bbaaede1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6e883d0f4243f990a2c4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eef874aab1280b1f4d03">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-018ae4240d7305eded04">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3e7801edd7b7b1ce5390">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-643c41945b4963c8f6f9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ff0e7406c42dc0766231">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-72393515caac6c5f0bba">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b9e6a73a832f377ad49b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d962d85d466a20f77f80">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-95248d66d5180995eada">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b53570153919029d74ef">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e820d08deb04948dd0f8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-18cda6454bc9e836f619">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d29767f9576022693420">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-81db71d685a965f1ab52">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-351636182e75231cca77">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6f14f47b9d42ca054298">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-977f363642c3077e70ed">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a21d711bed67df19219f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7725c070123b5519bde1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7bdb7a30572fb5b1e50e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-25ec2b8ae3b39b8d84e0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-107f9206cdb2e4995e98">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-68b6e361d3f3efa08f4c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-97756fd3dce081dcdeb6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8691079c50935b79f19d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5df122ed07b570ffeae5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fda3f34b6e18a862327d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4703f9f6cd3f6cc3d366">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e026289e678a3b58f75c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-69ec1310fc79bd419cc7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f5cf841544f154b57461">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-176765fd1b52b0228457">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a8c122465e33bf9b3a59">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-791a81ed7dbae35651f4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1150166a8335b4f3efd6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-33d16b14f72915d4da0a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f3ba762873ebad66f0d1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fb069816973c33cba440">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-30ccbd80ec31ad785856">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3538c9e63bd94d820f36">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1aa727d5dd79193c3cc8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2b325e7d310256f85705">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-629aa9d1b402342235e5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3f7d494df955b16f8c53">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1d86d728f8f0270c594c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4fa621ea6b31007db46a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-99ce1c77e2e37831efcf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d1d6b639ac49a1e9cf4d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1d6bc1a96fa87cc1f791">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-61ea42a971e9d3e347ae">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7632cd75772344b48067">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-30c757e16d8fcb6b67e8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-962ceb5c0d2f202a586e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-628cab961d6f9ce53aa6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e371cfc6f43f446578a8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b090e39b899d6326731b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-297c589e0efd5f14ea7b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e7b6d1d5ad190c123312">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-30c9323694b2a1fe50a0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7690674585382f771605">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9dcfa6764412ab5f5c92">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-64b4da2fc8f221162fed">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6c423208a227fa09149a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-abf0f7a9849721f0d2d4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e22e126cece82882b6d8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f0025d85e13605cbb6da">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-45aee83a3cc9ab9748b1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5808c500953da6c94cc9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-21127abd240b8bfbbe59">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2e66b9bd4583d1a216f0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-24db5e66db90d4adfe96">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7053930f2126744dc569">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-382a7d05c246b12bbd78">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c27c1ec488e0e1839713">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-623f6ba1e7786eab8fb7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-931d28df4a1e6d6b2448">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7400f46f9282ed7ba42e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e4b1ca96cb1c83244549">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d8921e77b80d29e29156">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-22a370b356cc0db3cd05">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d52d29159ecd601513da">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9e4bd8d7b385cdf8820f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-143efd0d616179423784">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-abc572ef0656bdebe37a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-702e7c51adf1325321f5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fc59deaaab2406489d9e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b0344099b9c160c857a9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5d1c4d4405c7aa3d704e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9b211338780f6f789907">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-774d16597b8f4f8ad3af">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b83371f1a2922f19cc49">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-af00f9699985c714c792">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a372c4f64b13b29c752e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9e5be78697bd02751b6f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-29c02fd4e5f262daa9d7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f14b8c1a6443dda6b0b7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5e3e91bfef0a72275b34">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fa865ed4d5fd1b2dfaf7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3f301b3d510e3d864572">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7654bdbf3fece87644e1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fd00baf4cee03dcf8764">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fbc27fc8ccefdaa22836">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-98270c95cad2e8f622b3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-be1bef6c9fceb9ecf408">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1bf9190fe6c681f321f9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-80934b8a37b216bd2401">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-93394d963e94f0761c94">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f47579c29f7d290d0c2e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1eef1bf4b5b7c47526a3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e49955d94d86afba4d14">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fd0cd8c465f93669f1e9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dd4b83580ad91946441e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1db9d150e7c733495f7b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b2635b54d6557cfd5cf9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-49165d4de7a121a89600">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e918c40c3ca709bcab7e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c5e423292e41a1fbf54b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e7d62d6386e519b33ebb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1f653b9ec7cc0c8bcf3a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7bb51e3c4c86e533a594">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f6c12f35cee498c630d0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-97b2d007e72507a9b449">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a696ec2ea309ae9560d6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9448ebf9fdd6751b0723">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c153e5a8f777888c4769">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5d4fc5d9f21bddb9ee0c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7ff0567132f30b467672">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-86216f0b0ccce0ad8a1a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-99d24ce5ec6d8a38f1c9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-36f6e5876d8c027df933">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-817f725a6f0a81b658a5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5c163bac76d14cf7889b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3843ed7f98b4b8bb57a7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-263609b9dccc0d7fd747">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-dd65aa7aa6844042a992">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3c67fe1199771f1de351">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e4ec513374f2c1075b05">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-914732d54504f084b60e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-267cb126a989849e449d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-397678aaeb06503642fb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b8154ee77af4e4c3c41b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-25948751abb199e154d9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-67b6d55c4bbfb5b14b2a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-05a2e3da8938219bfe81">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c0cdc6b2c79ee8017957">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b89ae4e82d2125de7d30">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-63f2c3d57279b8a2bc9e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c26dd66afa3639f6c0b6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2bb6e885a4edfff5b739">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c2707ecc7ab2af3e5ce1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b215dddc7bc005785ede">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e65f7e4271f192773b6c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1a1d836de41c445ebf28">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dc8caab0b40d0b620678">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b71e6e40ad52db565ab3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e27d6683c8c490b46dc7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9aeb557faf87a348af03">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d85054a8a0810b27c334">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-af00967868df5e11d364">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-598ed09be111ad635b40">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b8f1313e17ac6e1b4e0b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-78802dd204df18c3c077">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f06f08b8149eb262f0a8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-644b16a5dba3eff76003">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-06f4321b1b16b935e8b5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9dd0b0c4ac3618d5f6b6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cf63ae55ec816cd08d91">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e4dfb90cc98451fe7256">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f32be9ba8316a8c33e91">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fc09495451c5b87d028e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0d917ade6d4a0b5cb5b2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-16f242321d4e56af92a7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9eaf10ded9d633664d10">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-43318919af28df26c587">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7399ac924f81f0f5b5ef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f7d6b4760e41dc2092c9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d96c34f85cfaf28660e9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f1561fb758afcdcb14e7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d1a03572cdc022f6115b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7911af7e2b9b80d1f51f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-56271a08c20ad3f1b8af">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-22acb87f3180afe0d8e0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3b7e284b4ce254fed1a5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6cf7c1c8bd8b8d101575">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-21b74ba0a03b1b85097a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e537c0384bffe3bd7966">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e005d98a305bea3ab73d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-667bac51a492588d0af9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-857d39e0b180c2c97061">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f1d45ca9fe5d51e6431b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-dfcb7a1a5c9356e59ed2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-35d45f89a77e4e403034">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cd0a02aa7eb4fd077d46">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7a7adf8cb3332215fa7b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-257f360950218fb15c77">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9848cba9119e706c3135">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7c46b0636133bd7b127e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-56e28aa989830fd9e62b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4256c799a3e366a90f95">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-56e7075b8eebbe6a53fd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e891b2f9f662916e6f00">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c6cc6a44f3069df649b5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d4b0a076d26daa3f5a24">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aca85f6a6057dd6b09e2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dac299b3eb42d3a9a57b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7dff9a3a433fed64fe3d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1b5cbbe43761c919a0d8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2597e5e55dc38e1c21af">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-555dddecbb350b1313b5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c3116cad6952374be439">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-60eaa900f574dd4b30b6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b67d98d7de9f323e5612">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8186b82491b846771106">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-73792854cd27037b2309">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b9936625df4702f56cb5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-86d1b220fa750aa728d0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c5ab410c4c2cffe4657a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1a51eec7c7e67a101808">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-92b069cf41e56bf2a984">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-68e91d39bd8f8c3b8119">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2f233e449cbfe6cd3353">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3b7ecc88c6b40fb67662">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-571280ee0534c1b6a02c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2b942dde5539c461b386">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-392df1992c49479f6100">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-95ad9c075851edc582a1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1e7297575f27077ef2c0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a30047c96c9ecbf89bf7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-45e5322f51b558034c26">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7fcb6d5f2f7ea92021b5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-680114312f01c51872e2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cad977e98191b77efcbc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bd2a8e3d2882c419e14f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b2b33bc37198e9ae5d05">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c1577b896e6b05c225f4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-463e2085a2756739f678">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-04cf01b4a4030548da35">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3d3d6b5937076c8ebe07">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-216a067a282666fe4b86">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bae3c93a6a43048157f3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-33c001d74ed1e69b39fb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2bc76c5891946c1ffdcb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-dca957790473fdb95fe5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-23f261b353373094926e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1d707d9374f97504c11b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2cf94ca993d4f1565d66">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-984a2082508825b0fb30">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1a396f1f9faa23c94810">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6d4b3ea01f219aced6a5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7923ce99c11f1355e460">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9e209779ca26ce627c57">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eee5a00366acc82b3a68">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-54c91ed564edcb496595">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cda43e565e246d8bdc42">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-68207278853d3d6c364f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0dcce7deee14044e8440">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-68c7204f1061aa14692e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a1592abb5890b06ea095">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-62ec4b2fe40457b93b84">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ef6f9d596c220b4f1058">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-194d4db97741245b665a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dc0e83ebb2c50ac5655e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ddb5eb875a3c5fb30d65">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3da1177d880274c206fc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d4e0120bc0e16fc7202d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c2a22b0b86cb75a6b50f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-234a1502e5a26ac54f71">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4bed9c9682f71e88458f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7cfae3cbc31ebb76da62">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-66910c4c9e3b891eddd3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-30536969ab708cf686cc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5dcc1c121ad64e51ee0c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f5bb3f83e3b7bd1f5d97">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a6ced321847fe15fe35c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cd7d75480398b755b6d5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b5fa4815072a9559262f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c691113f0b3c3845bd60">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-def2c109dc941d5fb654">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4727c6031f9da7102726">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2b7739437197102e975e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a2c74e199fb9dc9d0113">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-afcbdd0fa6f77f6905c7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9206b0912b19028f857d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ccb66c64628a917d637f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-58cd04fda17184eb5780">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b1d884d40b8dc91f1c27">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f2e4f16d1f7517a437da">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3ea90547f668979812a3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5690367d321ef272f9b1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a91b066ac72d144878cd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f52f775c1cf0c843a158">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5ce63bcf89d5a71e8863">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c5a1f0efe5296d1f35f1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1effda40faf50729e3ab">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7d71b343032173e3617b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-212cb2e14bb0663a9722">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-29058435a71314e97fe3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e1e4ce80b7d801160b07">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2ffe645931cfc760efd9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-620ae7cfbe9fdd2e13cb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9a5ab1d26a3ee702c7f7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d67a1b1d377bc8ea1217">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7933ce37df03ca52f9b2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d7f0dec9ce1ff1d9456f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-339f40b7740fea065638">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e8ede59c277dcd20caa0">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6cb386346968a166f71b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6cb386346968a166f71b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f6d7bf247f4dc9e7b759"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f6d7bf247f4dc9e7b759`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eecce2faec764577b864"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-eecce2faec764577b864`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a89ac9ded09b59dd7171"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a89ac9ded09b59dd7171`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-22075f8465f1bcc67cbf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-22075f8465f1bcc67cbf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e485026a3f8446ac8e79"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e485026a3f8446ac8e79`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-542a09c4efd2cd29b22a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-542a09c4efd2cd29b22a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c70668ab62f08975ce1e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c70668ab62f08975ce1e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-42edd6ba43c150054c91"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-42edd6ba43c150054c91`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8ac3d04df0793286dbca"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8ac3d04df0793286dbca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7b03c7971745eeaab941"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7b03c7971745eeaab941`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-11cf99ceb27d774698b7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-11cf99ceb27d774698b7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-60ea056a4d00bbaaede1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-60ea056a4d00bbaaede1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6e883d0f4243f990a2c4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6e883d0f4243f990a2c4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eef874aab1280b1f4d03"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-eef874aab1280b1f4d03`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-018ae4240d7305eded04"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-018ae4240d7305eded04`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3e7801edd7b7b1ce5390"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3e7801edd7b7b1ce5390`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-643c41945b4963c8f6f9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-643c41945b4963c8f6f9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ff0e7406c42dc0766231"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ff0e7406c42dc0766231`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-72393515caac6c5f0bba"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-72393515caac6c5f0bba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b9e6a73a832f377ad49b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b9e6a73a832f377ad49b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d962d85d466a20f77f80"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d962d85d466a20f77f80`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-95248d66d5180995eada"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-95248d66d5180995eada`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b53570153919029d74ef"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b53570153919029d74ef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e820d08deb04948dd0f8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e820d08deb04948dd0f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-18cda6454bc9e836f619"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-18cda6454bc9e836f619`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d29767f9576022693420"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d29767f9576022693420`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-81db71d685a965f1ab52"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-81db71d685a965f1ab52`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-351636182e75231cca77"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-351636182e75231cca77`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6f14f47b9d42ca054298"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6f14f47b9d42ca054298`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-977f363642c3077e70ed"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-977f363642c3077e70ed`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a21d711bed67df19219f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a21d711bed67df19219f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-01-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7725c070123b5519bde1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7725c070123b5519bde1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7bdb7a30572fb5b1e50e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7bdb7a30572fb5b1e50e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-25ec2b8ae3b39b8d84e0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-25ec2b8ae3b39b8d84e0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-107f9206cdb2e4995e98"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-107f9206cdb2e4995e98`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-68b6e361d3f3efa08f4c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-68b6e361d3f3efa08f4c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-97756fd3dce081dcdeb6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-97756fd3dce081dcdeb6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8691079c50935b79f19d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8691079c50935b79f19d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5df122ed07b570ffeae5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5df122ed07b570ffeae5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fda3f34b6e18a862327d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fda3f34b6e18a862327d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4703f9f6cd3f6cc3d366"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4703f9f6cd3f6cc3d366`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e026289e678a3b58f75c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e026289e678a3b58f75c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-69ec1310fc79bd419cc7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-69ec1310fc79bd419cc7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f5cf841544f154b57461"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f5cf841544f154b57461`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-176765fd1b52b0228457"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-176765fd1b52b0228457`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a8c122465e33bf9b3a59"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a8c122465e33bf9b3a59`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-791a81ed7dbae35651f4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-791a81ed7dbae35651f4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1150166a8335b4f3efd6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1150166a8335b4f3efd6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-33d16b14f72915d4da0a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-33d16b14f72915d4da0a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f3ba762873ebad66f0d1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f3ba762873ebad66f0d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fb069816973c33cba440"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fb069816973c33cba440`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-30ccbd80ec31ad785856"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-30ccbd80ec31ad785856`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3538c9e63bd94d820f36"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3538c9e63bd94d820f36`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1aa727d5dd79193c3cc8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1aa727d5dd79193c3cc8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2b325e7d310256f85705"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2b325e7d310256f85705`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-629aa9d1b402342235e5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-629aa9d1b402342235e5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3f7d494df955b16f8c53"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3f7d494df955b16f8c53`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1d86d728f8f0270c594c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1d86d728f8f0270c594c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4fa621ea6b31007db46a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4fa621ea6b31007db46a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-99ce1c77e2e37831efcf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-99ce1c77e2e37831efcf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d1d6b639ac49a1e9cf4d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d1d6b639ac49a1e9cf4d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1d6bc1a96fa87cc1f791"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1d6bc1a96fa87cc1f791`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-61ea42a971e9d3e347ae"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-61ea42a971e9d3e347ae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-02-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7632cd75772344b48067"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7632cd75772344b48067`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-30c757e16d8fcb6b67e8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-30c757e16d8fcb6b67e8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-962ceb5c0d2f202a586e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-962ceb5c0d2f202a586e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-628cab961d6f9ce53aa6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-628cab961d6f9ce53aa6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e371cfc6f43f446578a8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e371cfc6f43f446578a8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b090e39b899d6326731b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b090e39b899d6326731b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-297c589e0efd5f14ea7b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-297c589e0efd5f14ea7b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e7b6d1d5ad190c123312"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e7b6d1d5ad190c123312`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-30c9323694b2a1fe50a0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-30c9323694b2a1fe50a0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7690674585382f771605"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7690674585382f771605`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9dcfa6764412ab5f5c92"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9dcfa6764412ab5f5c92`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-64b4da2fc8f221162fed"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-64b4da2fc8f221162fed`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6c423208a227fa09149a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6c423208a227fa09149a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-abf0f7a9849721f0d2d4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-abf0f7a9849721f0d2d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e22e126cece82882b6d8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e22e126cece82882b6d8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f0025d85e13605cbb6da"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f0025d85e13605cbb6da`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-45aee83a3cc9ab9748b1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-45aee83a3cc9ab9748b1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5808c500953da6c94cc9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5808c500953da6c94cc9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-21127abd240b8bfbbe59"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-21127abd240b8bfbbe59`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2e66b9bd4583d1a216f0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2e66b9bd4583d1a216f0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-24db5e66db90d4adfe96"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-24db5e66db90d4adfe96`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7053930f2126744dc569"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7053930f2126744dc569`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-382a7d05c246b12bbd78"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-382a7d05c246b12bbd78`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c27c1ec488e0e1839713"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c27c1ec488e0e1839713`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-623f6ba1e7786eab8fb7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-623f6ba1e7786eab8fb7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-931d28df4a1e6d6b2448"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-931d28df4a1e6d6b2448`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7400f46f9282ed7ba42e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7400f46f9282ed7ba42e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e4b1ca96cb1c83244549"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e4b1ca96cb1c83244549`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d8921e77b80d29e29156"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d8921e77b80d29e29156`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-22a370b356cc0db3cd05"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-22a370b356cc0db3cd05`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d52d29159ecd601513da"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d52d29159ecd601513da`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9e4bd8d7b385cdf8820f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9e4bd8d7b385cdf8820f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-03-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-143efd0d616179423784"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-143efd0d616179423784`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-abc572ef0656bdebe37a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-abc572ef0656bdebe37a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-702e7c51adf1325321f5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-702e7c51adf1325321f5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fc59deaaab2406489d9e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fc59deaaab2406489d9e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b0344099b9c160c857a9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b0344099b9c160c857a9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5d1c4d4405c7aa3d704e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5d1c4d4405c7aa3d704e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9b211338780f6f789907"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9b211338780f6f789907`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-774d16597b8f4f8ad3af"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-774d16597b8f4f8ad3af`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b83371f1a2922f19cc49"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b83371f1a2922f19cc49`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-af00f9699985c714c792"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-af00f9699985c714c792`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a372c4f64b13b29c752e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a372c4f64b13b29c752e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9e5be78697bd02751b6f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9e5be78697bd02751b6f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-29c02fd4e5f262daa9d7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-29c02fd4e5f262daa9d7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f14b8c1a6443dda6b0b7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f14b8c1a6443dda6b0b7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5e3e91bfef0a72275b34"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5e3e91bfef0a72275b34`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fa865ed4d5fd1b2dfaf7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fa865ed4d5fd1b2dfaf7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3f301b3d510e3d864572"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3f301b3d510e3d864572`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7654bdbf3fece87644e1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7654bdbf3fece87644e1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fd00baf4cee03dcf8764"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fd00baf4cee03dcf8764`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fbc27fc8ccefdaa22836"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fbc27fc8ccefdaa22836`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-98270c95cad2e8f622b3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-98270c95cad2e8f622b3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-be1bef6c9fceb9ecf408"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-be1bef6c9fceb9ecf408`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1bf9190fe6c681f321f9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1bf9190fe6c681f321f9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-80934b8a37b216bd2401"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-80934b8a37b216bd2401`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-93394d963e94f0761c94"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-93394d963e94f0761c94`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f47579c29f7d290d0c2e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f47579c29f7d290d0c2e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1eef1bf4b5b7c47526a3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1eef1bf4b5b7c47526a3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e49955d94d86afba4d14"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e49955d94d86afba4d14`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fd0cd8c465f93669f1e9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fd0cd8c465f93669f1e9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dd4b83580ad91946441e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-dd4b83580ad91946441e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1db9d150e7c733495f7b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1db9d150e7c733495f7b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b2635b54d6557cfd5cf9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b2635b54d6557cfd5cf9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-04-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-49165d4de7a121a89600"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-49165d4de7a121a89600`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e918c40c3ca709bcab7e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e918c40c3ca709bcab7e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c5e423292e41a1fbf54b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c5e423292e41a1fbf54b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e7d62d6386e519b33ebb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e7d62d6386e519b33ebb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1f653b9ec7cc0c8bcf3a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1f653b9ec7cc0c8bcf3a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7bb51e3c4c86e533a594"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7bb51e3c4c86e533a594`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f6c12f35cee498c630d0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f6c12f35cee498c630d0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-97b2d007e72507a9b449"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-97b2d007e72507a9b449`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a696ec2ea309ae9560d6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a696ec2ea309ae9560d6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9448ebf9fdd6751b0723"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9448ebf9fdd6751b0723`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c153e5a8f777888c4769"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c153e5a8f777888c4769`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5d4fc5d9f21bddb9ee0c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5d4fc5d9f21bddb9ee0c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7ff0567132f30b467672"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7ff0567132f30b467672`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-86216f0b0ccce0ad8a1a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-86216f0b0ccce0ad8a1a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-99d24ce5ec6d8a38f1c9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-99d24ce5ec6d8a38f1c9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-36f6e5876d8c027df933"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-36f6e5876d8c027df933`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-817f725a6f0a81b658a5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-817f725a6f0a81b658a5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5c163bac76d14cf7889b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5c163bac76d14cf7889b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3843ed7f98b4b8bb57a7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3843ed7f98b4b8bb57a7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-263609b9dccc0d7fd747"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-263609b9dccc0d7fd747`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-dd65aa7aa6844042a992"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-dd65aa7aa6844042a992`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3c67fe1199771f1de351"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3c67fe1199771f1de351`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e4ec513374f2c1075b05"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e4ec513374f2c1075b05`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-914732d54504f084b60e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-914732d54504f084b60e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-267cb126a989849e449d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-267cb126a989849e449d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-397678aaeb06503642fb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-397678aaeb06503642fb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b8154ee77af4e4c3c41b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b8154ee77af4e4c3c41b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-25948751abb199e154d9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-25948751abb199e154d9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-67b6d55c4bbfb5b14b2a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-67b6d55c4bbfb5b14b2a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-05a2e3da8938219bfe81"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-05a2e3da8938219bfe81`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c0cdc6b2c79ee8017957"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c0cdc6b2c79ee8017957`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b89ae4e82d2125de7d30"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b89ae4e82d2125de7d30`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-05-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-63f2c3d57279b8a2bc9e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-63f2c3d57279b8a2bc9e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c26dd66afa3639f6c0b6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c26dd66afa3639f6c0b6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2bb6e885a4edfff5b739"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2bb6e885a4edfff5b739`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c2707ecc7ab2af3e5ce1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c2707ecc7ab2af3e5ce1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b215dddc7bc005785ede"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b215dddc7bc005785ede`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e65f7e4271f192773b6c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e65f7e4271f192773b6c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1a1d836de41c445ebf28"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1a1d836de41c445ebf28`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dc8caab0b40d0b620678"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dc8caab0b40d0b620678`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b71e6e40ad52db565ab3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b71e6e40ad52db565ab3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e27d6683c8c490b46dc7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e27d6683c8c490b46dc7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9aeb557faf87a348af03"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9aeb557faf87a348af03`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d85054a8a0810b27c334"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d85054a8a0810b27c334`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-af00967868df5e11d364"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-af00967868df5e11d364`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-598ed09be111ad635b40"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-598ed09be111ad635b40`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b8f1313e17ac6e1b4e0b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b8f1313e17ac6e1b4e0b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-78802dd204df18c3c077"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-78802dd204df18c3c077`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f06f08b8149eb262f0a8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f06f08b8149eb262f0a8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-644b16a5dba3eff76003"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-644b16a5dba3eff76003`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-06f4321b1b16b935e8b5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-06f4321b1b16b935e8b5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9dd0b0c4ac3618d5f6b6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9dd0b0c4ac3618d5f6b6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cf63ae55ec816cd08d91"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cf63ae55ec816cd08d91`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e4dfb90cc98451fe7256"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e4dfb90cc98451fe7256`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f32be9ba8316a8c33e91"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f32be9ba8316a8c33e91`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fc09495451c5b87d028e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fc09495451c5b87d028e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0d917ade6d4a0b5cb5b2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0d917ade6d4a0b5cb5b2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-16f242321d4e56af92a7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-16f242321d4e56af92a7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9eaf10ded9d633664d10"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9eaf10ded9d633664d10`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-43318919af28df26c587"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-43318919af28df26c587`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7399ac924f81f0f5b5ef"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7399ac924f81f0f5b5ef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f7d6b4760e41dc2092c9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f7d6b4760e41dc2092c9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d96c34f85cfaf28660e9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d96c34f85cfaf28660e9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f1561fb758afcdcb14e7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f1561fb758afcdcb14e7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-06-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d1a03572cdc022f6115b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d1a03572cdc022f6115b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7911af7e2b9b80d1f51f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7911af7e2b9b80d1f51f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-56271a08c20ad3f1b8af"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-56271a08c20ad3f1b8af`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-22acb87f3180afe0d8e0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-22acb87f3180afe0d8e0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3b7e284b4ce254fed1a5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3b7e284b4ce254fed1a5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6cf7c1c8bd8b8d101575"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6cf7c1c8bd8b8d101575`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-21b74ba0a03b1b85097a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-21b74ba0a03b1b85097a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e537c0384bffe3bd7966"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e537c0384bffe3bd7966`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e005d98a305bea3ab73d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e005d98a305bea3ab73d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-667bac51a492588d0af9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-667bac51a492588d0af9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-857d39e0b180c2c97061"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-857d39e0b180c2c97061`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f1d45ca9fe5d51e6431b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f1d45ca9fe5d51e6431b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-dfcb7a1a5c9356e59ed2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-dfcb7a1a5c9356e59ed2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-35d45f89a77e4e403034"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-35d45f89a77e4e403034`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cd0a02aa7eb4fd077d46"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cd0a02aa7eb4fd077d46`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7a7adf8cb3332215fa7b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7a7adf8cb3332215fa7b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-257f360950218fb15c77"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-257f360950218fb15c77`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9848cba9119e706c3135"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9848cba9119e706c3135`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7c46b0636133bd7b127e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7c46b0636133bd7b127e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-56e28aa989830fd9e62b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-56e28aa989830fd9e62b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4256c799a3e366a90f95"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4256c799a3e366a90f95`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-56e7075b8eebbe6a53fd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-56e7075b8eebbe6a53fd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e891b2f9f662916e6f00"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e891b2f9f662916e6f00`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c6cc6a44f3069df649b5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c6cc6a44f3069df649b5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d4b0a076d26daa3f5a24"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d4b0a076d26daa3f5a24`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aca85f6a6057dd6b09e2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-aca85f6a6057dd6b09e2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dac299b3eb42d3a9a57b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-dac299b3eb42d3a9a57b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7dff9a3a433fed64fe3d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7dff9a3a433fed64fe3d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1b5cbbe43761c919a0d8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1b5cbbe43761c919a0d8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2597e5e55dc38e1c21af"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2597e5e55dc38e1c21af`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-555dddecbb350b1313b5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-555dddecbb350b1313b5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c3116cad6952374be439"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c3116cad6952374be439`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-07-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-60eaa900f574dd4b30b6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-60eaa900f574dd4b30b6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b67d98d7de9f323e5612"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b67d98d7de9f323e5612`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8186b82491b846771106"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8186b82491b846771106`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-73792854cd27037b2309"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-73792854cd27037b2309`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b9936625df4702f56cb5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b9936625df4702f56cb5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-86d1b220fa750aa728d0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-86d1b220fa750aa728d0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c5ab410c4c2cffe4657a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c5ab410c4c2cffe4657a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1a51eec7c7e67a101808"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1a51eec7c7e67a101808`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-92b069cf41e56bf2a984"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-92b069cf41e56bf2a984`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-68e91d39bd8f8c3b8119"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-68e91d39bd8f8c3b8119`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2f233e449cbfe6cd3353"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2f233e449cbfe6cd3353`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3b7ecc88c6b40fb67662"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3b7ecc88c6b40fb67662`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-571280ee0534c1b6a02c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-571280ee0534c1b6a02c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2b942dde5539c461b386"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2b942dde5539c461b386`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-392df1992c49479f6100"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-392df1992c49479f6100`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-95ad9c075851edc582a1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-95ad9c075851edc582a1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1e7297575f27077ef2c0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1e7297575f27077ef2c0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a30047c96c9ecbf89bf7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a30047c96c9ecbf89bf7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-45e5322f51b558034c26"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-45e5322f51b558034c26`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7fcb6d5f2f7ea92021b5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7fcb6d5f2f7ea92021b5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-680114312f01c51872e2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-680114312f01c51872e2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cad977e98191b77efcbc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cad977e98191b77efcbc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bd2a8e3d2882c419e14f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bd2a8e3d2882c419e14f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b2b33bc37198e9ae5d05"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b2b33bc37198e9ae5d05`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c1577b896e6b05c225f4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c1577b896e6b05c225f4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-463e2085a2756739f678"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-463e2085a2756739f678`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-04cf01b4a4030548da35"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-04cf01b4a4030548da35`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3d3d6b5937076c8ebe07"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3d3d6b5937076c8ebe07`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-216a067a282666fe4b86"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-216a067a282666fe4b86`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bae3c93a6a43048157f3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bae3c93a6a43048157f3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-33c001d74ed1e69b39fb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-33c001d74ed1e69b39fb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2bc76c5891946c1ffdcb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2bc76c5891946c1ffdcb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-08-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-dca957790473fdb95fe5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-dca957790473fdb95fe5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-23f261b353373094926e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-23f261b353373094926e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1d707d9374f97504c11b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1d707d9374f97504c11b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2cf94ca993d4f1565d66"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2cf94ca993d4f1565d66`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-984a2082508825b0fb30"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-984a2082508825b0fb30`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1a396f1f9faa23c94810"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1a396f1f9faa23c94810`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6d4b3ea01f219aced6a5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6d4b3ea01f219aced6a5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7923ce99c11f1355e460"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7923ce99c11f1355e460`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9e209779ca26ce627c57"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9e209779ca26ce627c57`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eee5a00366acc82b3a68"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-eee5a00366acc82b3a68`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-54c91ed564edcb496595"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-54c91ed564edcb496595`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cda43e565e246d8bdc42"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cda43e565e246d8bdc42`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-68207278853d3d6c364f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-68207278853d3d6c364f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0dcce7deee14044e8440"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0dcce7deee14044e8440`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-68c7204f1061aa14692e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-68c7204f1061aa14692e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a1592abb5890b06ea095"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a1592abb5890b06ea095`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-62ec4b2fe40457b93b84"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-62ec4b2fe40457b93b84`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ef6f9d596c220b4f1058"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ef6f9d596c220b4f1058`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-194d4db97741245b665a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-194d4db97741245b665a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dc0e83ebb2c50ac5655e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dc0e83ebb2c50ac5655e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ddb5eb875a3c5fb30d65"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ddb5eb875a3c5fb30d65`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3da1177d880274c206fc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3da1177d880274c206fc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d4e0120bc0e16fc7202d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d4e0120bc0e16fc7202d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c2a22b0b86cb75a6b50f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c2a22b0b86cb75a6b50f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-16-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-234a1502e5a26ac54f71"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-234a1502e5a26ac54f71`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4bed9c9682f71e88458f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4bed9c9682f71e88458f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7cfae3cbc31ebb76da62"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7cfae3cbc31ebb76da62`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-66910c4c9e3b891eddd3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-66910c4c9e3b891eddd3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-30536969ab708cf686cc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-30536969ab708cf686cc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5dcc1c121ad64e51ee0c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5dcc1c121ad64e51ee0c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f5bb3f83e3b7bd1f5d97"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f5bb3f83e3b7bd1f5d97`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a6ced321847fe15fe35c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a6ced321847fe15fe35c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-09-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cd7d75480398b755b6d5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cd7d75480398b755b6d5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b5fa4815072a9559262f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b5fa4815072a9559262f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c691113f0b3c3845bd60"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c691113f0b3c3845bd60`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-def2c109dc941d5fb654"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-def2c109dc941d5fb654`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-11-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4727c6031f9da7102726"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4727c6031f9da7102726`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2b7739437197102e975e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2b7739437197102e975e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a2c74e199fb9dc9d0113"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a2c74e199fb9dc9d0113`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-afcbdd0fa6f77f6905c7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-afcbdd0fa6f77f6905c7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-12-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9206b0912b19028f857d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9206b0912b19028f857d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ccb66c64628a917d637f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ccb66c64628a917d637f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-58cd04fda17184eb5780"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-58cd04fda17184eb5780`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b1d884d40b8dc91f1c27"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b1d884d40b8dc91f1c27`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-13-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f2e4f16d1f7517a437da"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f2e4f16d1f7517a437da`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3ea90547f668979812a3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3ea90547f668979812a3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5690367d321ef272f9b1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5690367d321ef272f9b1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a91b066ac72d144878cd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a91b066ac72d144878cd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-14-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f52f775c1cf0c843a158"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f52f775c1cf0c843a158`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5ce63bcf89d5a71e8863"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5ce63bcf89d5a71e8863`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c5a1f0efe5296d1f35f1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c5a1f0efe5296d1f35f1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1effda40faf50729e3ab"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1effda40faf50729e3ab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-15-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7d71b343032173e3617b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7d71b343032173e3617b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-212cb2e14bb0663a9722"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-212cb2e14bb0663a9722`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-29058435a71314e97fe3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-29058435a71314e97fe3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e1e4ce80b7d801160b07"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e1e4ce80b7d801160b07`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-17-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2ffe645931cfc760efd9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2ffe645931cfc760efd9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-620ae7cfbe9fdd2e13cb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-620ae7cfbe9fdd2e13cb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9a5ab1d26a3ee702c7f7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9a5ab1d26a3ee702c7f7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d67a1b1d377bc8ea1217"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d67a1b1d377bc8ea1217`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-18-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7933ce37df03ca52f9b2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7933ce37df03ca52f9b2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d7f0dec9ce1ff1d9456f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d7f0dec9ce1ff1d9456f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-339f40b7740fea065638"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-339f40b7740fea065638`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e8ede59c277dcd20caa0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e8ede59c277dcd20caa0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: channel-10-in; to port: channel-19-out; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-parallel-lower-entry-slip:canonical-southeast | <a href="#case-preview_review-0c0de95137d7828a28c4">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-lower-entry-slip:canonical-top | <a href="#case-preview_review-7b4ba8c200ef88eb616d">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-parallel-lower-entry-slip:connection-overview | <a href="#case-preview_review-d043730150b7ec26286c">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-parallel-lower-entry-slip:canonical-southeast</summary>

<a id="case-preview_review-0c0de95137d7828a28c4"></a>

**General: unverified** — `preview_review-0c0de95137d7828a28c4`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-lower-entry-slip:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-lower-entry-slip:canonical-top</summary>

<a id="case-preview_review-7b4ba8c200ef88eb616d"></a>

**General: unverified** — `preview_review-7b4ba8c200ef88eb616d`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-lower-entry-slip:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-parallel-lower-entry-slip:connection-overview</summary>

<a id="case-preview_review-d043730150b7ec26286c"></a>

**General: unverified** — `preview_review-d043730150b7ec26286c`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-parallel-lower-entry-slip:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

This new type implements one functional part of the human-approved close parallel layout. It preserves the [frozen source proposal](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/TESTING.md#32-close-parallel-ramps-and-perpendicular-avenue-approaches) and leaves the retained R40 and compact assemblies available with their own resource identities and evidence. This piece's exact source is [piece.jsonc](piece.jsonc); the shared placement plan is [assembly.jsonc](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-parallel-diamond/assembly.jsonc).

The ground-mouth revision narrows terminal asphalt while preserving the 6 m grade interfaces, every saved traffic route, all fifteen permanent types, and the 31-cell construction union. The earlier `ddrhw-parallel-diamond-parts-01` build retains its original wider mouths and its own immutable evidence; the current revision is measured separately as `ddrhw-parallel-diamond-pedestrian-mouths-01`.
