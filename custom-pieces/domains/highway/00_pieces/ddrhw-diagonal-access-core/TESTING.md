---
title: "Testing: DD RHW-4 \u2014 and Avenue Access Core"
summary: "Inspect this piece\u2019s exact checks, resource evidence, and explicit human observations."
audience: "contributors"
document_type: "reference"
---

# Testing: DD RHW-4 — and Avenue Access Core

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

Coordinates the crossing and the ramp landing fragments that share its five construction tiles. It preserves both opposing highway decks, the four avenue car lanes, and both avenue pedestrian channels. Ramp access uses only the adjacent avenue carriageway; cross-avenue turns are excluded. The generated records below describe movements measured from saved PATH resources, meaning the game’s directed traffic routes. A measured route does not establish game operation or a complete native joining boundary.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `1-N-in-1` | road / 1 / primary | in | [-3.2, -8.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-668896c488171c19873d` |
| `1-N-in-2` | road / 1 / primary | in | [3.2, -8.0, 0.0]; [0.7071067811865475, -0.7071067811865476]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `1-W-out-3` | road / 1 / primary | out | [8.0, -35.2, 7.5]; [-0.7071067811865475, -0.7071067811865477]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `1-W-in-4` | road / 1 / primary | in | [8.0, -35.2, 15.0]; [0.7071067811865475, 0.7071067811865477]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `1-W-out-5` | road / 1 / primary | out | [8.0, -28.8, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `1-W-in-6` | road / 1 / primary | in | [8.0, -28.8, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `1-W-out-7` | road / 1 / primary | out | [8.0, -3.2, 0.0]; [-0.7071067811865476, 0.7071067811865475]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `1-W-out-8` | road / 1 / primary | out | [8.0, 3.2, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `1-E-out-9` | road / 1 / primary | out | [24.0, -35.2, 0.0]; [0.7071067811865475, -0.7071067811865477]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `1-E-out-10` | road / 1 / primary | out | [24.0, -28.8, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `1-S-in-11` | road / 1 / primary | in | [28.8, -24.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `1-N-in-12` | road / 1 / primary | in | [28.8, -8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `1-N-out-13` | road / 1 / primary | out | [28.8, -8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `1-S-in-14` | road / 1 / primary | in | [35.2, -24.0, 0.0]; [-0.7071067811865477, 0.7071067811865475]; 0.0 | `path-interface-668896c488171c19873d` |
| `1-N-in-15` | road / 1 / primary | in | [35.2, -8.0, 7.5]; [-0.7071067811865477, -0.7071067811865475]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `1-N-out-16` | road / 1 / primary | out | [35.2, -8.0, 15.0]; [0.7071067811865477, 0.7071067811865475]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `2-N-in-1` | pedestrian / 2 / primary | in | [-7.3, -8.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-2ec6b824afff9b450810` |
| `2-W-out-2` | pedestrian / 2 / primary | out | [8.0, 7.3, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-ef45fb4474012bf121a0` |
| `2-E-out-3` | pedestrian / 2 / primary | out | [24.0, -39.3, 0.0]; [0.7071067811865477, -0.7071067811865475]; 0.0 | `path-interface-ef45fb4474012bf121a0` |
| `2-S-in-4` | pedestrian / 2 / primary | in | [39.3, -24.0, 0.0]; [-0.7071067811865475, 0.7071067811865477]; 0.0 | `path-interface-2ec6b824afff9b450810` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `1-N-in-1` → `1-E-out-9` | primary |
| road | `1-N-in-2` → `1-E-out-10` | primary |
| road | `1-W-in-4` → `1-N-out-16` | primary |
| road | `1-W-in-6` → `1-N-out-13` | primary |
| road | `1-S-in-11` → `1-W-out-7` | primary |
| road | `1-N-in-12` → `1-W-out-5` | primary |
| road | `1-S-in-14` → `1-W-out-8` | primary |
| road | `1-N-in-15` → `1-W-out-3` | primary |
| pedestrian | `2-N-in-1` → `2-E-out-3` | primary |
| pedestrian | `2-S-in-4` → `2-W-out-2` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `1-N-in-1` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-1` | road / `1-W-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-1` | road / `1-W-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-1` | road / `1-W-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-1` | road / `1-E-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-1` | road / `1-N-out-13` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-1` | road / `1-N-out-16` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-1` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-1` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-2` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-2` | road / `1-W-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-2` | road / `1-W-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-2` | road / `1-W-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-2` | road / `1-E-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-2` | road / `1-N-out-13` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-2` | road / `1-N-out-16` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-2` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-2` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-4` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-4` | road / `1-W-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-4` | road / `1-W-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-4` | road / `1-W-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-4` | road / `1-E-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-4` | road / `1-E-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-4` | road / `1-N-out-13` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-4` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-4` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-6` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-6` | road / `1-W-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-6` | road / `1-W-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-6` | road / `1-W-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-6` | road / `1-E-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-6` | road / `1-E-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-6` | road / `1-N-out-16` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-6` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-6` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-11` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-11` | road / `1-W-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-11` | road / `1-W-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-11` | road / `1-E-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-11` | road / `1-E-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-11` | road / `1-N-out-13` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-11` | road / `1-N-out-16` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-11` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-11` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-12` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-12` | road / `1-W-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-12` | road / `1-W-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-12` | road / `1-E-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-12` | road / `1-E-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-12` | road / `1-N-out-13` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-12` | road / `1-N-out-16` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-12` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-12` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-14` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-14` | road / `1-W-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-14` | road / `1-W-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-14` | road / `1-E-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-14` | road / `1-E-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-14` | road / `1-N-out-13` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-14` | road / `1-N-out-16` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-14` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-14` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-15` | road / `1-W-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-15` | road / `1-W-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-15` | road / `1-W-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-15` | road / `1-E-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-15` | road / `1-E-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-15` | road / `1-N-out-13` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-15` | road / `1-N-out-16` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-15` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-15` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-N-in-1` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-N-in-1` | road / `1-W-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-N-in-1` | road / `1-W-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-N-in-1` | road / `1-W-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-N-in-1` | road / `1-E-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-N-in-1` | road / `1-E-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-N-in-1` | road / `1-N-out-13` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-N-in-1` | road / `1-N-out-16` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-N-in-1` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-S-in-4` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-S-in-4` | road / `1-W-out-5` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-S-in-4` | road / `1-W-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-S-in-4` | road / `1-W-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-S-in-4` | road / `1-E-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-S-in-4` | road / `1-E-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-S-in-4` | road / `1-N-out-13` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-S-in-4` | road / `1-N-out-16` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-S-in-4` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use the exact NAM 50 right-hand-traffic profile in `config/profiles/nam50-rhd.jsonc`, flat terrain, and the [assembly test setup](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#2-test-setup). Keep personal settings and game archives outside Git. Building does not install this component.

## 3. Software checks

From the repository root, build the selected component with `python3 -B custom-pieces/scp.py build --include ddrhw-diagonal-access-core --output custom-pieces/dist/highway-component`, then run `python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/highway-component`. Run the shared [highway checks](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#3-software-checks) for geometry, saved paths, and assembled seams. Model verification checks actual saved triangles and PATH points; it does not merely reread a source label.

## 4. Game checks

Place this component as part of the complete assembly in each of its four rotations. Check its roads, barriers, and neighbouring seams; use Route Query and visible traffic to observe each listed movement independently. Check avenue pedestrians where present. For ramp or junction components, confirm that each permitted right turn works, each cross-avenue left turn stays unavailable, and the opposite upper-deck barrier remains closed. Demolish and replace it, save the city, reload it, and inspect shadows at several game times. Use the [shared observation procedure](../../../../docs/TESTING.md) to record only matching human observations.

## 5. Results and known issues

The assembly’s executed checks, their source version, and remaining limitations are recorded in [Results and known issues](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#5-results-and-known-issues). This component is experimental and has no human game pass. Native DD models have local overhangs; pavement coverage and corridor face-intersection checks are not a complete vehicle swept-volume or structural proof.

The adaptive-ground integration retains the complete saved car, pedestrian, and ramp routes, but its game behaviour remains unverified for this component. Test a fresh placement from the current build in all four rotations, compare the selection preview with the placed decks, and inspect automatic pavement at the Avenue ends and ramp mouths. Retained routes do not establish working transfers between the adaptive Avenue tiles and neighbouring highway tiles, ordinary Avenue overplacement or redraw, or pedestrian travel. The canonical software views remain a static geometry and ground-artwork reference. The isolated prototype’s pavement and rotation observations do not transfer to this full component; use the [assembly testing guide](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md) and [network specification](../../NETWORK_SPEC.md) for the exact scope.

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
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-diagonal-access-core/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-diagonal-access-core/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-b5f3022ace3685e7c41a">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-b5f3022ace3685e7c41a"></a>

**General: unverified** — `software_resources-b5f3022ace3685e7c41a`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-b5f3022ace3685e7c41a">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-b5f3022ace3685e7c41a"></a>

**General: unverified** — `software_connectivity-b5f3022ace3685e7c41a`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-diagonal-access-core:canonical-southeast | <a href="#case-preview_review-f171c5fb3e196d1d1198">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-diagonal-access-core:canonical-top | <a href="#case-preview_review-a7ba8c8eb8ed1691e6dd">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-diagonal-access-core:connection-overview | <a href="#case-preview_review-d0bb86b2495e2bb1120f">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-diagonal-access-core:canonical-southeast</summary>

<a id="case-preview_review-f171c5fb3e196d1d1198"></a>

**General: unverified** — `preview_review-f171c5fb3e196d1d1198`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-diagonal-access-core:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-diagonal-access-core:canonical-top</summary>

<a id="case-preview_review-a7ba8c8eb8ed1691e6dd"></a>

**General: unverified** — `preview_review-a7ba8c8eb8ed1691e6dd`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-diagonal-access-core:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-diagonal-access-core:connection-overview</summary>

<a id="case-preview_review-d0bb86b2495e2bb1120f"></a>

**General: unverified** — `preview_review-d0bb86b2495e2bb1120f`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-diagonal-access-core:connection-overview.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-9089693028482b301540">[ ] unverified</a> | <a href="#case-in_game_render-1110e621c41fb103a23c">[ ] unverified</a> | <a href="#case-in_game_render-5ebf37a2241aebd1717a">[ ] unverified</a> | <a href="#case-in_game_render-2b30446aa089e20c1cc1">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-9089693028482b301540"></a>

**0° CCW: unverified** — `in_game_render-9089693028482b301540`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-1110e621c41fb103a23c"></a>

**90° CCW: unverified** — `in_game_render-1110e621c41fb103a23c`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-5ebf37a2241aebd1717a"></a>

**180° CCW: unverified** — `in_game_render-5ebf37a2241aebd1717a`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-2b30446aa089e20c1cc1"></a>

**270° CCW: unverified** — `in_game_render-2b30446aa089e20c1cc1`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-9089693028482b301540">[ ] unverified</a> | <a href="#case-in_game_placement-1110e621c41fb103a23c">[ ] unverified</a> | <a href="#case-in_game_placement-5ebf37a2241aebd1717a">[ ] unverified</a> | <a href="#case-in_game_placement-2b30446aa089e20c1cc1">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-9089693028482b301540"></a>

**0° CCW: unverified** — `in_game_placement-9089693028482b301540`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-1110e621c41fb103a23c"></a>

**90° CCW: unverified** — `in_game_placement-1110e621c41fb103a23c`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-5ebf37a2241aebd1717a"></a>

**180° CCW: unverified** — `in_game_placement-5ebf37a2241aebd1717a`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-2b30446aa089e20c1cc1"></a>

**270° CCW: unverified** — `in_game_placement-2b30446aa089e20c1cc1`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-9089693028482b301540">[ ] unverified</a> | <a href="#case-in_game_demolition-1110e621c41fb103a23c">[ ] unverified</a> | <a href="#case-in_game_demolition-5ebf37a2241aebd1717a">[ ] unverified</a> | <a href="#case-in_game_demolition-2b30446aa089e20c1cc1">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-9089693028482b301540"></a>

**0° CCW: unverified** — `in_game_demolition-9089693028482b301540`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-1110e621c41fb103a23c"></a>

**90° CCW: unverified** — `in_game_demolition-1110e621c41fb103a23c`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-5ebf37a2241aebd1717a"></a>

**180° CCW: unverified** — `in_game_demolition-5ebf37a2241aebd1717a`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-2b30446aa089e20c1cc1"></a>

**270° CCW: unverified** — `in_game_demolition-2b30446aa089e20c1cc1`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-9089693028482b301540">[ ] unverified</a> | <a href="#case-in_game_save_reload-1110e621c41fb103a23c">[ ] unverified</a> | <a href="#case-in_game_save_reload-5ebf37a2241aebd1717a">[ ] unverified</a> | <a href="#case-in_game_save_reload-2b30446aa089e20c1cc1">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-9089693028482b301540"></a>

**0° CCW: unverified** — `in_game_save_reload-9089693028482b301540`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-1110e621c41fb103a23c"></a>

**90° CCW: unverified** — `in_game_save_reload-1110e621c41fb103a23c`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-5ebf37a2241aebd1717a"></a>

**180° CCW: unverified** — `in_game_save_reload-5ebf37a2241aebd1717a`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-2b30446aa089e20c1cc1"></a>

**270° CCW: unverified** — `in_game_save_reload-2b30446aa089e20c1cc1`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 32 cases; unverified: 32</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-1>1-E-out-9; entry: 1-N-in-1; exit: 1-E-out-9 | — | <a href="#case-in_game_route_query-c6f40f775cea53813d1b">[ ] unverified</a> | <a href="#case-in_game_route_query-d62731d831dc39b8f7aa">[ ] unverified</a> | <a href="#case-in_game_route_query-c0437c786984b356eddc">[ ] unverified</a> | <a href="#case-in_game_route_query-6697e8fc2480f7c0ee47">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-2>1-E-out-10; entry: 1-N-in-2; exit: 1-E-out-10 | — | <a href="#case-in_game_route_query-9ce40e67119d246b2399">[ ] unverified</a> | <a href="#case-in_game_route_query-f670ed9f5b80f40cc4e0">[ ] unverified</a> | <a href="#case-in_game_route_query-3b566fd50b2dae5210c6">[ ] unverified</a> | <a href="#case-in_game_route_query-1653892d19d64cd8f641">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-16; entry: 1-W-in-4; exit: 1-N-out-16 | — | <a href="#case-in_game_route_query-bf1fe0fa1bcea17388c2">[ ] unverified</a> | <a href="#case-in_game_route_query-be1fc994b22784f562d3">[ ] unverified</a> | <a href="#case-in_game_route_query-cd8ed095b4c23a50f59f">[ ] unverified</a> | <a href="#case-in_game_route_query-8538db65c33fdd0351ba">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-6>1-N-out-13; entry: 1-W-in-6; exit: 1-N-out-13 | — | <a href="#case-in_game_route_query-b8b62df29af47d4a901b">[ ] unverified</a> | <a href="#case-in_game_route_query-9c386ddbc26d402e7562">[ ] unverified</a> | <a href="#case-in_game_route_query-14fe1375c2c6956576fe">[ ] unverified</a> | <a href="#case-in_game_route_query-e6d01e09468f35e242bc">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-S-in-11>1-W-out-7; entry: 1-S-in-11; exit: 1-W-out-7 | — | <a href="#case-in_game_route_query-79471e1b55455f675529">[ ] unverified</a> | <a href="#case-in_game_route_query-14a80db676313ec96eb3">[ ] unverified</a> | <a href="#case-in_game_route_query-5c546425b046ff38f3b1">[ ] unverified</a> | <a href="#case-in_game_route_query-1616e70bfc860d0fedaf">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-12>1-W-out-5; entry: 1-N-in-12; exit: 1-W-out-5 | — | <a href="#case-in_game_route_query-c7dcd003d64809dc03bb">[ ] unverified</a> | <a href="#case-in_game_route_query-7bffe3ffd520d4a177b3">[ ] unverified</a> | <a href="#case-in_game_route_query-a6e893f9b1955a9cd2fe">[ ] unverified</a> | <a href="#case-in_game_route_query-2f1f0eb871df5ac66912">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-S-in-14>1-W-out-8; entry: 1-S-in-14; exit: 1-W-out-8 | — | <a href="#case-in_game_route_query-6e7209e3e86b188e1bdf">[ ] unverified</a> | <a href="#case-in_game_route_query-8013c7fe4de224242b97">[ ] unverified</a> | <a href="#case-in_game_route_query-7a93826fabcc8257e47b">[ ] unverified</a> | <a href="#case-in_game_route_query-6549c21a183820e632b6">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-15>1-W-out-3; entry: 1-N-in-15; exit: 1-W-out-3 | — | <a href="#case-in_game_route_query-95a89cc316af4c9c09fd">[ ] unverified</a> | <a href="#case-in_game_route_query-1aa808994537f37545d3">[ ] unverified</a> | <a href="#case-in_game_route_query-8a3a98d2a283ca075d38">[ ] unverified</a> | <a href="#case-in_game_route_query-b3f9794123027f798a18">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-1>1-E-out-9; entry: 1-N-in-1; exit: 1-E-out-9</summary>

<a id="case-in_game_route_query-c6f40f775cea53813d1b"></a>

**0° CCW: unverified** — `in_game_route_query-c6f40f775cea53813d1b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-1>1-E-out-9; entry: 1-N-in-1; exit: 1-E-out-9.

No observation recorded.

<a id="case-in_game_route_query-d62731d831dc39b8f7aa"></a>

**90° CCW: unverified** — `in_game_route_query-d62731d831dc39b8f7aa`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-1>1-E-out-9; entry: 1-N-in-1; exit: 1-E-out-9.

No observation recorded.

<a id="case-in_game_route_query-c0437c786984b356eddc"></a>

**180° CCW: unverified** — `in_game_route_query-c0437c786984b356eddc`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-1>1-E-out-9; entry: 1-N-in-1; exit: 1-E-out-9.

No observation recorded.

<a id="case-in_game_route_query-6697e8fc2480f7c0ee47"></a>

**270° CCW: unverified** — `in_game_route_query-6697e8fc2480f7c0ee47`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-1>1-E-out-9; entry: 1-N-in-1; exit: 1-E-out-9.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-2>1-E-out-10; entry: 1-N-in-2; exit: 1-E-out-10</summary>

<a id="case-in_game_route_query-9ce40e67119d246b2399"></a>

**0° CCW: unverified** — `in_game_route_query-9ce40e67119d246b2399`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-2>1-E-out-10; entry: 1-N-in-2; exit: 1-E-out-10.

No observation recorded.

<a id="case-in_game_route_query-f670ed9f5b80f40cc4e0"></a>

**90° CCW: unverified** — `in_game_route_query-f670ed9f5b80f40cc4e0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-2>1-E-out-10; entry: 1-N-in-2; exit: 1-E-out-10.

No observation recorded.

<a id="case-in_game_route_query-3b566fd50b2dae5210c6"></a>

**180° CCW: unverified** — `in_game_route_query-3b566fd50b2dae5210c6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-2>1-E-out-10; entry: 1-N-in-2; exit: 1-E-out-10.

No observation recorded.

<a id="case-in_game_route_query-1653892d19d64cd8f641"></a>

**270° CCW: unverified** — `in_game_route_query-1653892d19d64cd8f641`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-2>1-E-out-10; entry: 1-N-in-2; exit: 1-E-out-10.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-16; entry: 1-W-in-4; exit: 1-N-out-16</summary>

<a id="case-in_game_route_query-bf1fe0fa1bcea17388c2"></a>

**0° CCW: unverified** — `in_game_route_query-bf1fe0fa1bcea17388c2`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-16; entry: 1-W-in-4; exit: 1-N-out-16.

No observation recorded.

<a id="case-in_game_route_query-be1fc994b22784f562d3"></a>

**90° CCW: unverified** — `in_game_route_query-be1fc994b22784f562d3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-16; entry: 1-W-in-4; exit: 1-N-out-16.

No observation recorded.

<a id="case-in_game_route_query-cd8ed095b4c23a50f59f"></a>

**180° CCW: unverified** — `in_game_route_query-cd8ed095b4c23a50f59f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-16; entry: 1-W-in-4; exit: 1-N-out-16.

No observation recorded.

<a id="case-in_game_route_query-8538db65c33fdd0351ba"></a>

**270° CCW: unverified** — `in_game_route_query-8538db65c33fdd0351ba`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-16; entry: 1-W-in-4; exit: 1-N-out-16.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-6>1-N-out-13; entry: 1-W-in-6; exit: 1-N-out-13</summary>

<a id="case-in_game_route_query-b8b62df29af47d4a901b"></a>

**0° CCW: unverified** — `in_game_route_query-b8b62df29af47d4a901b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-6>1-N-out-13; entry: 1-W-in-6; exit: 1-N-out-13.

No observation recorded.

<a id="case-in_game_route_query-9c386ddbc26d402e7562"></a>

**90° CCW: unverified** — `in_game_route_query-9c386ddbc26d402e7562`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-6>1-N-out-13; entry: 1-W-in-6; exit: 1-N-out-13.

No observation recorded.

<a id="case-in_game_route_query-14fe1375c2c6956576fe"></a>

**180° CCW: unverified** — `in_game_route_query-14fe1375c2c6956576fe`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-6>1-N-out-13; entry: 1-W-in-6; exit: 1-N-out-13.

No observation recorded.

<a id="case-in_game_route_query-e6d01e09468f35e242bc"></a>

**270° CCW: unverified** — `in_game_route_query-e6d01e09468f35e242bc`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-6>1-N-out-13; entry: 1-W-in-6; exit: 1-N-out-13.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-S-in-11>1-W-out-7; entry: 1-S-in-11; exit: 1-W-out-7</summary>

<a id="case-in_game_route_query-79471e1b55455f675529"></a>

**0° CCW: unverified** — `in_game_route_query-79471e1b55455f675529`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-11>1-W-out-7; entry: 1-S-in-11; exit: 1-W-out-7.

No observation recorded.

<a id="case-in_game_route_query-14a80db676313ec96eb3"></a>

**90° CCW: unverified** — `in_game_route_query-14a80db676313ec96eb3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-11>1-W-out-7; entry: 1-S-in-11; exit: 1-W-out-7.

No observation recorded.

<a id="case-in_game_route_query-5c546425b046ff38f3b1"></a>

**180° CCW: unverified** — `in_game_route_query-5c546425b046ff38f3b1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-11>1-W-out-7; entry: 1-S-in-11; exit: 1-W-out-7.

No observation recorded.

<a id="case-in_game_route_query-1616e70bfc860d0fedaf"></a>

**270° CCW: unverified** — `in_game_route_query-1616e70bfc860d0fedaf`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-11>1-W-out-7; entry: 1-S-in-11; exit: 1-W-out-7.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-12>1-W-out-5; entry: 1-N-in-12; exit: 1-W-out-5</summary>

<a id="case-in_game_route_query-c7dcd003d64809dc03bb"></a>

**0° CCW: unverified** — `in_game_route_query-c7dcd003d64809dc03bb`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-12>1-W-out-5; entry: 1-N-in-12; exit: 1-W-out-5.

No observation recorded.

<a id="case-in_game_route_query-7bffe3ffd520d4a177b3"></a>

**90° CCW: unverified** — `in_game_route_query-7bffe3ffd520d4a177b3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-12>1-W-out-5; entry: 1-N-in-12; exit: 1-W-out-5.

No observation recorded.

<a id="case-in_game_route_query-a6e893f9b1955a9cd2fe"></a>

**180° CCW: unverified** — `in_game_route_query-a6e893f9b1955a9cd2fe`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-12>1-W-out-5; entry: 1-N-in-12; exit: 1-W-out-5.

No observation recorded.

<a id="case-in_game_route_query-2f1f0eb871df5ac66912"></a>

**270° CCW: unverified** — `in_game_route_query-2f1f0eb871df5ac66912`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-12>1-W-out-5; entry: 1-N-in-12; exit: 1-W-out-5.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-S-in-14>1-W-out-8; entry: 1-S-in-14; exit: 1-W-out-8</summary>

<a id="case-in_game_route_query-6e7209e3e86b188e1bdf"></a>

**0° CCW: unverified** — `in_game_route_query-6e7209e3e86b188e1bdf`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-14>1-W-out-8; entry: 1-S-in-14; exit: 1-W-out-8.

No observation recorded.

<a id="case-in_game_route_query-8013c7fe4de224242b97"></a>

**90° CCW: unverified** — `in_game_route_query-8013c7fe4de224242b97`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-14>1-W-out-8; entry: 1-S-in-14; exit: 1-W-out-8.

No observation recorded.

<a id="case-in_game_route_query-7a93826fabcc8257e47b"></a>

**180° CCW: unverified** — `in_game_route_query-7a93826fabcc8257e47b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-14>1-W-out-8; entry: 1-S-in-14; exit: 1-W-out-8.

No observation recorded.

<a id="case-in_game_route_query-6549c21a183820e632b6"></a>

**270° CCW: unverified** — `in_game_route_query-6549c21a183820e632b6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-14>1-W-out-8; entry: 1-S-in-14; exit: 1-W-out-8.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-15>1-W-out-3; entry: 1-N-in-15; exit: 1-W-out-3</summary>

<a id="case-in_game_route_query-95a89cc316af4c9c09fd"></a>

**0° CCW: unverified** — `in_game_route_query-95a89cc316af4c9c09fd`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-15>1-W-out-3; entry: 1-N-in-15; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_route_query-1aa808994537f37545d3"></a>

**90° CCW: unverified** — `in_game_route_query-1aa808994537f37545d3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-15>1-W-out-3; entry: 1-N-in-15; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_route_query-8a3a98d2a283ca075d38"></a>

**180° CCW: unverified** — `in_game_route_query-8a3a98d2a283ca075d38`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-15>1-W-out-3; entry: 1-N-in-15; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_route_query-b3f9794123027f798a18"></a>

**270° CCW: unverified** — `in_game_route_query-b3f9794123027f798a18`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-15>1-W-out-3; entry: 1-N-in-15; exit: 1-W-out-3.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 32 cases; unverified: 32</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-1>1-E-out-9; entry: 1-N-in-1; exit: 1-E-out-9 | — | <a href="#case-in_game_visible_travel-c6f40f775cea53813d1b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d62731d831dc39b8f7aa">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c0437c786984b356eddc">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6697e8fc2480f7c0ee47">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-2>1-E-out-10; entry: 1-N-in-2; exit: 1-E-out-10 | — | <a href="#case-in_game_visible_travel-9ce40e67119d246b2399">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f670ed9f5b80f40cc4e0">[ ] unverified</a> | <a href="#case-in_game_visible_travel-3b566fd50b2dae5210c6">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1653892d19d64cd8f641">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-16; entry: 1-W-in-4; exit: 1-N-out-16 | — | <a href="#case-in_game_visible_travel-bf1fe0fa1bcea17388c2">[ ] unverified</a> | <a href="#case-in_game_visible_travel-be1fc994b22784f562d3">[ ] unverified</a> | <a href="#case-in_game_visible_travel-cd8ed095b4c23a50f59f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8538db65c33fdd0351ba">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-6>1-N-out-13; entry: 1-W-in-6; exit: 1-N-out-13 | — | <a href="#case-in_game_visible_travel-b8b62df29af47d4a901b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9c386ddbc26d402e7562">[ ] unverified</a> | <a href="#case-in_game_visible_travel-14fe1375c2c6956576fe">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e6d01e09468f35e242bc">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-S-in-11>1-W-out-7; entry: 1-S-in-11; exit: 1-W-out-7 | — | <a href="#case-in_game_visible_travel-79471e1b55455f675529">[ ] unverified</a> | <a href="#case-in_game_visible_travel-14a80db676313ec96eb3">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5c546425b046ff38f3b1">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1616e70bfc860d0fedaf">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-12>1-W-out-5; entry: 1-N-in-12; exit: 1-W-out-5 | — | <a href="#case-in_game_visible_travel-c7dcd003d64809dc03bb">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7bffe3ffd520d4a177b3">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a6e893f9b1955a9cd2fe">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2f1f0eb871df5ac66912">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-S-in-14>1-W-out-8; entry: 1-S-in-14; exit: 1-W-out-8 | — | <a href="#case-in_game_visible_travel-6e7209e3e86b188e1bdf">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8013c7fe4de224242b97">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7a93826fabcc8257e47b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6549c21a183820e632b6">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-15>1-W-out-3; entry: 1-N-in-15; exit: 1-W-out-3 | — | <a href="#case-in_game_visible_travel-95a89cc316af4c9c09fd">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1aa808994537f37545d3">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8a3a98d2a283ca075d38">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b3f9794123027f798a18">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-1>1-E-out-9; entry: 1-N-in-1; exit: 1-E-out-9</summary>

<a id="case-in_game_visible_travel-c6f40f775cea53813d1b"></a>

**0° CCW: unverified** — `in_game_visible_travel-c6f40f775cea53813d1b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-1>1-E-out-9; entry: 1-N-in-1; exit: 1-E-out-9.

No observation recorded.

<a id="case-in_game_visible_travel-d62731d831dc39b8f7aa"></a>

**90° CCW: unverified** — `in_game_visible_travel-d62731d831dc39b8f7aa`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-1>1-E-out-9; entry: 1-N-in-1; exit: 1-E-out-9.

No observation recorded.

<a id="case-in_game_visible_travel-c0437c786984b356eddc"></a>

**180° CCW: unverified** — `in_game_visible_travel-c0437c786984b356eddc`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-1>1-E-out-9; entry: 1-N-in-1; exit: 1-E-out-9.

No observation recorded.

<a id="case-in_game_visible_travel-6697e8fc2480f7c0ee47"></a>

**270° CCW: unverified** — `in_game_visible_travel-6697e8fc2480f7c0ee47`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-1>1-E-out-9; entry: 1-N-in-1; exit: 1-E-out-9.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-2>1-E-out-10; entry: 1-N-in-2; exit: 1-E-out-10</summary>

<a id="case-in_game_visible_travel-9ce40e67119d246b2399"></a>

**0° CCW: unverified** — `in_game_visible_travel-9ce40e67119d246b2399`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-2>1-E-out-10; entry: 1-N-in-2; exit: 1-E-out-10.

No observation recorded.

<a id="case-in_game_visible_travel-f670ed9f5b80f40cc4e0"></a>

**90° CCW: unverified** — `in_game_visible_travel-f670ed9f5b80f40cc4e0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-2>1-E-out-10; entry: 1-N-in-2; exit: 1-E-out-10.

No observation recorded.

<a id="case-in_game_visible_travel-3b566fd50b2dae5210c6"></a>

**180° CCW: unverified** — `in_game_visible_travel-3b566fd50b2dae5210c6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-2>1-E-out-10; entry: 1-N-in-2; exit: 1-E-out-10.

No observation recorded.

<a id="case-in_game_visible_travel-1653892d19d64cd8f641"></a>

**270° CCW: unverified** — `in_game_visible_travel-1653892d19d64cd8f641`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-2>1-E-out-10; entry: 1-N-in-2; exit: 1-E-out-10.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-16; entry: 1-W-in-4; exit: 1-N-out-16</summary>

<a id="case-in_game_visible_travel-bf1fe0fa1bcea17388c2"></a>

**0° CCW: unverified** — `in_game_visible_travel-bf1fe0fa1bcea17388c2`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-16; entry: 1-W-in-4; exit: 1-N-out-16.

No observation recorded.

<a id="case-in_game_visible_travel-be1fc994b22784f562d3"></a>

**90° CCW: unverified** — `in_game_visible_travel-be1fc994b22784f562d3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-16; entry: 1-W-in-4; exit: 1-N-out-16.

No observation recorded.

<a id="case-in_game_visible_travel-cd8ed095b4c23a50f59f"></a>

**180° CCW: unverified** — `in_game_visible_travel-cd8ed095b4c23a50f59f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-16; entry: 1-W-in-4; exit: 1-N-out-16.

No observation recorded.

<a id="case-in_game_visible_travel-8538db65c33fdd0351ba"></a>

**270° CCW: unverified** — `in_game_visible_travel-8538db65c33fdd0351ba`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-16; entry: 1-W-in-4; exit: 1-N-out-16.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-6>1-N-out-13; entry: 1-W-in-6; exit: 1-N-out-13</summary>

<a id="case-in_game_visible_travel-b8b62df29af47d4a901b"></a>

**0° CCW: unverified** — `in_game_visible_travel-b8b62df29af47d4a901b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-6>1-N-out-13; entry: 1-W-in-6; exit: 1-N-out-13.

No observation recorded.

<a id="case-in_game_visible_travel-9c386ddbc26d402e7562"></a>

**90° CCW: unverified** — `in_game_visible_travel-9c386ddbc26d402e7562`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-6>1-N-out-13; entry: 1-W-in-6; exit: 1-N-out-13.

No observation recorded.

<a id="case-in_game_visible_travel-14fe1375c2c6956576fe"></a>

**180° CCW: unverified** — `in_game_visible_travel-14fe1375c2c6956576fe`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-6>1-N-out-13; entry: 1-W-in-6; exit: 1-N-out-13.

No observation recorded.

<a id="case-in_game_visible_travel-e6d01e09468f35e242bc"></a>

**270° CCW: unverified** — `in_game_visible_travel-e6d01e09468f35e242bc`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-6>1-N-out-13; entry: 1-W-in-6; exit: 1-N-out-13.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-S-in-11>1-W-out-7; entry: 1-S-in-11; exit: 1-W-out-7</summary>

<a id="case-in_game_visible_travel-79471e1b55455f675529"></a>

**0° CCW: unverified** — `in_game_visible_travel-79471e1b55455f675529`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-11>1-W-out-7; entry: 1-S-in-11; exit: 1-W-out-7.

No observation recorded.

<a id="case-in_game_visible_travel-14a80db676313ec96eb3"></a>

**90° CCW: unverified** — `in_game_visible_travel-14a80db676313ec96eb3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-11>1-W-out-7; entry: 1-S-in-11; exit: 1-W-out-7.

No observation recorded.

<a id="case-in_game_visible_travel-5c546425b046ff38f3b1"></a>

**180° CCW: unverified** — `in_game_visible_travel-5c546425b046ff38f3b1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-11>1-W-out-7; entry: 1-S-in-11; exit: 1-W-out-7.

No observation recorded.

<a id="case-in_game_visible_travel-1616e70bfc860d0fedaf"></a>

**270° CCW: unverified** — `in_game_visible_travel-1616e70bfc860d0fedaf`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-11>1-W-out-7; entry: 1-S-in-11; exit: 1-W-out-7.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-12>1-W-out-5; entry: 1-N-in-12; exit: 1-W-out-5</summary>

<a id="case-in_game_visible_travel-c7dcd003d64809dc03bb"></a>

**0° CCW: unverified** — `in_game_visible_travel-c7dcd003d64809dc03bb`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-12>1-W-out-5; entry: 1-N-in-12; exit: 1-W-out-5.

No observation recorded.

<a id="case-in_game_visible_travel-7bffe3ffd520d4a177b3"></a>

**90° CCW: unverified** — `in_game_visible_travel-7bffe3ffd520d4a177b3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-12>1-W-out-5; entry: 1-N-in-12; exit: 1-W-out-5.

No observation recorded.

<a id="case-in_game_visible_travel-a6e893f9b1955a9cd2fe"></a>

**180° CCW: unverified** — `in_game_visible_travel-a6e893f9b1955a9cd2fe`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-12>1-W-out-5; entry: 1-N-in-12; exit: 1-W-out-5.

No observation recorded.

<a id="case-in_game_visible_travel-2f1f0eb871df5ac66912"></a>

**270° CCW: unverified** — `in_game_visible_travel-2f1f0eb871df5ac66912`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-12>1-W-out-5; entry: 1-N-in-12; exit: 1-W-out-5.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-S-in-14>1-W-out-8; entry: 1-S-in-14; exit: 1-W-out-8</summary>

<a id="case-in_game_visible_travel-6e7209e3e86b188e1bdf"></a>

**0° CCW: unverified** — `in_game_visible_travel-6e7209e3e86b188e1bdf`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-14>1-W-out-8; entry: 1-S-in-14; exit: 1-W-out-8.

No observation recorded.

<a id="case-in_game_visible_travel-8013c7fe4de224242b97"></a>

**90° CCW: unverified** — `in_game_visible_travel-8013c7fe4de224242b97`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-14>1-W-out-8; entry: 1-S-in-14; exit: 1-W-out-8.

No observation recorded.

<a id="case-in_game_visible_travel-7a93826fabcc8257e47b"></a>

**180° CCW: unverified** — `in_game_visible_travel-7a93826fabcc8257e47b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-14>1-W-out-8; entry: 1-S-in-14; exit: 1-W-out-8.

No observation recorded.

<a id="case-in_game_visible_travel-6549c21a183820e632b6"></a>

**270° CCW: unverified** — `in_game_visible_travel-6549c21a183820e632b6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-14>1-W-out-8; entry: 1-S-in-14; exit: 1-W-out-8.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-15>1-W-out-3; entry: 1-N-in-15; exit: 1-W-out-3</summary>

<a id="case-in_game_visible_travel-95a89cc316af4c9c09fd"></a>

**0° CCW: unverified** — `in_game_visible_travel-95a89cc316af4c9c09fd`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-15>1-W-out-3; entry: 1-N-in-15; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-1aa808994537f37545d3"></a>

**90° CCW: unverified** — `in_game_visible_travel-1aa808994537f37545d3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-15>1-W-out-3; entry: 1-N-in-15; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-8a3a98d2a283ca075d38"></a>

**180° CCW: unverified** — `in_game_visible_travel-8a3a98d2a283ca075d38`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-15>1-W-out-3; entry: 1-N-in-15; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-b3f9794123027f798a18"></a>

**270° CCW: unverified** — `in_game_visible_travel-b3f9794123027f798a18`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-15>1-W-out-3; entry: 1-N-in-15; exit: 1-W-out-3.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — pedestrian — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: pedestrian; role: primary; journey: 2:2-N-in-1>2-E-out-3; entry: 2-N-in-1; exit: 2-E-out-3 | — | <a href="#case-in_game_route_query-ae4abfea13e971292160">[ ] unverified</a> | <a href="#case-in_game_route_query-276d8023fee6fdf4df1e">[ ] unverified</a> | <a href="#case-in_game_route_query-c15b764b2b54dd6756dc">[ ] unverified</a> | <a href="#case-in_game_route_query-a9e3311b4224e342834e">[ ] unverified</a> |
| **Route Query**<br>Service: pedestrian; role: primary; journey: 2:2-S-in-4>2-W-out-2; entry: 2-S-in-4; exit: 2-W-out-2 | — | <a href="#case-in_game_route_query-c46b00ba0146236696c7">[ ] unverified</a> | <a href="#case-in_game_route_query-e388fd63c6471581f8a3">[ ] unverified</a> | <a href="#case-in_game_route_query-2495c8c2cabce0bb0d85">[ ] unverified</a> | <a href="#case-in_game_route_query-f9e38c5acf145936fcfd">[ ] unverified</a> |


<details>
<summary>Route Query — Service: pedestrian; role: primary; journey: 2:2-N-in-1>2-E-out-3; entry: 2-N-in-1; exit: 2-E-out-3</summary>

<a id="case-in_game_route_query-ae4abfea13e971292160"></a>

**0° CCW: unverified** — `in_game_route_query-ae4abfea13e971292160`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-N-in-1>2-E-out-3; entry: 2-N-in-1; exit: 2-E-out-3.

No observation recorded.

<a id="case-in_game_route_query-276d8023fee6fdf4df1e"></a>

**90° CCW: unverified** — `in_game_route_query-276d8023fee6fdf4df1e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-N-in-1>2-E-out-3; entry: 2-N-in-1; exit: 2-E-out-3.

No observation recorded.

<a id="case-in_game_route_query-c15b764b2b54dd6756dc"></a>

**180° CCW: unverified** — `in_game_route_query-c15b764b2b54dd6756dc`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-N-in-1>2-E-out-3; entry: 2-N-in-1; exit: 2-E-out-3.

No observation recorded.

<a id="case-in_game_route_query-a9e3311b4224e342834e"></a>

**270° CCW: unverified** — `in_game_route_query-a9e3311b4224e342834e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-N-in-1>2-E-out-3; entry: 2-N-in-1; exit: 2-E-out-3.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: pedestrian; role: primary; journey: 2:2-S-in-4>2-W-out-2; entry: 2-S-in-4; exit: 2-W-out-2</summary>

<a id="case-in_game_route_query-c46b00ba0146236696c7"></a>

**0° CCW: unverified** — `in_game_route_query-c46b00ba0146236696c7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-S-in-4>2-W-out-2; entry: 2-S-in-4; exit: 2-W-out-2.

No observation recorded.

<a id="case-in_game_route_query-e388fd63c6471581f8a3"></a>

**90° CCW: unverified** — `in_game_route_query-e388fd63c6471581f8a3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-S-in-4>2-W-out-2; entry: 2-S-in-4; exit: 2-W-out-2.

No observation recorded.

<a id="case-in_game_route_query-2495c8c2cabce0bb0d85"></a>

**180° CCW: unverified** — `in_game_route_query-2495c8c2cabce0bb0d85`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-S-in-4>2-W-out-2; entry: 2-S-in-4; exit: 2-W-out-2.

No observation recorded.

<a id="case-in_game_route_query-f9e38c5acf145936fcfd"></a>

**270° CCW: unverified** — `in_game_route_query-f9e38c5acf145936fcfd`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-S-in-4>2-W-out-2; entry: 2-S-in-4; exit: 2-W-out-2.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — pedestrian — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: pedestrian; role: primary; journey: 2:2-N-in-1>2-E-out-3; entry: 2-N-in-1; exit: 2-E-out-3 | — | <a href="#case-in_game_visible_travel-ae4abfea13e971292160">[ ] unverified</a> | <a href="#case-in_game_visible_travel-276d8023fee6fdf4df1e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c15b764b2b54dd6756dc">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a9e3311b4224e342834e">[ ] unverified</a> |
| **Visible travel**<br>Service: pedestrian; role: primary; journey: 2:2-S-in-4>2-W-out-2; entry: 2-S-in-4; exit: 2-W-out-2 | — | <a href="#case-in_game_visible_travel-c46b00ba0146236696c7">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e388fd63c6471581f8a3">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2495c8c2cabce0bb0d85">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f9e38c5acf145936fcfd">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: pedestrian; role: primary; journey: 2:2-N-in-1>2-E-out-3; entry: 2-N-in-1; exit: 2-E-out-3</summary>

<a id="case-in_game_visible_travel-ae4abfea13e971292160"></a>

**0° CCW: unverified** — `in_game_visible_travel-ae4abfea13e971292160`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-N-in-1>2-E-out-3; entry: 2-N-in-1; exit: 2-E-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-276d8023fee6fdf4df1e"></a>

**90° CCW: unverified** — `in_game_visible_travel-276d8023fee6fdf4df1e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-N-in-1>2-E-out-3; entry: 2-N-in-1; exit: 2-E-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-c15b764b2b54dd6756dc"></a>

**180° CCW: unverified** — `in_game_visible_travel-c15b764b2b54dd6756dc`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-N-in-1>2-E-out-3; entry: 2-N-in-1; exit: 2-E-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-a9e3311b4224e342834e"></a>

**270° CCW: unverified** — `in_game_visible_travel-a9e3311b4224e342834e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-N-in-1>2-E-out-3; entry: 2-N-in-1; exit: 2-E-out-3.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: pedestrian; role: primary; journey: 2:2-S-in-4>2-W-out-2; entry: 2-S-in-4; exit: 2-W-out-2</summary>

<a id="case-in_game_visible_travel-c46b00ba0146236696c7"></a>

**0° CCW: unverified** — `in_game_visible_travel-c46b00ba0146236696c7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-S-in-4>2-W-out-2; entry: 2-S-in-4; exit: 2-W-out-2.

No observation recorded.

<a id="case-in_game_visible_travel-e388fd63c6471581f8a3"></a>

**90° CCW: unverified** — `in_game_visible_travel-e388fd63c6471581f8a3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-S-in-4>2-W-out-2; entry: 2-S-in-4; exit: 2-W-out-2.

No observation recorded.

<a id="case-in_game_visible_travel-2495c8c2cabce0bb0d85"></a>

**180° CCW: unverified** — `in_game_visible_travel-2495c8c2cabce0bb0d85`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-S-in-4>2-W-out-2; entry: 2-S-in-4; exit: 2-W-out-2.

No observation recorded.

<a id="case-in_game_visible_travel-f9e38c5acf145936fcfd"></a>

**270° CCW: unverified** — `in_game_visible_travel-f9e38c5acf145936fcfd`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-S-in-4>2-W-out-2; entry: 2-S-in-4; exit: 2-W-out-2.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 224 cases; unverified: 224</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 1-N-in-1; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-df720693a84b5dd0c454">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-090e8bc7d22bccb7da9d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1f392098a1af18e5df36">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-05268379e958e14fd090">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-1; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f7e041046e4a052ed1b8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c5d6b04c9ebb9384fe3e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b8de77ae2c311e2d334c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-79c5a3808f7f5dac14a8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-1; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-984e29f5b3494ab34eb0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fb62271c637b78576cf9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-75fa277c36e6fc52cf09">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-56e84d757dcbc0b266e3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-1; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-486baadf43d62b48f73d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-191828b70fa4fe142aca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a63a2aef0c675dcd677f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cd03e6c990c2e3048d1c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-1; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e959d8bea608d3a2d4fa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a4f26933b410b6623176">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-afb48e46465858b4d864">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0b5b453b3f19464fa49b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-1; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d606b080abb7cd8aeec9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-70f6d90f7e5ba555d5e2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cb8b024cd3822754235c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cf88c9a36b316e795726">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-1; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-dc1a98f1de1171a4f786">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eefcf1ba04f9ddc5785b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d84d3fbc8b784c3d666d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-95087689b9c855a26e35">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-2; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7776798361bc9c0ed7fb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a08bf071edabf5068585">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-39b00fbb33949426d589">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e097020e6538e26a87f7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-2; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7c743cd58e0982076e6f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-57435634825a53609597">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0c8f8dc2d58409f680f7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0979014c2a9213e7f9f9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-2; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-dd6d90b7c1df7a2df7b4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bc533d5b183908bb5bff">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c91372f573550ba23297">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-222b64875a378c48cb55">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-2; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-41b322a2a0e43ebfde6c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1fc147c7e7095a0e050e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fa2dd2dc94fdcc60f879">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a72ba20eab2d001b9e97">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-2; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3d8206074e0c2e01b0d0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f0eb11e4328d4ccc0275">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2d9f9a6f979d646064a9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-46de31f8cf7463715177">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-2; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-404a1d6a4966f0c212e0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0f2f6f051a1b278cb86b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-227e63c8b08dfd6ca0ce">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7dd1a1c435ed37d99251">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-2; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7ac828b6fc796a3601b3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1b0d05c5c1d27b2cf74d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-02e0cb877788250220c0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-45c5c3d74742fe674fbb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b49d96fd379a8ed5cbc9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-265c830ab21aa3919fbf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5845870823e37e34a6b8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d825687f17cec0002023">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6ce950ee680ac257ccd0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-47382f9b42a837ff80b4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c3242d477d123265fc52">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-87480af298d1f75dec71">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bf046ebb0fd3c77be4be">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5972fe19d6e8524bc373">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-65ff84aea80e728ac357">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5e9a66d76e7724ba9508">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9e7e9702c54730a5fdd1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-84329585853141f60ca4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5df35a395f762e5bafa8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3cc4ed636b1aed6373d4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-63ba2822f5c2e12aaf0c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-697b5d4433a0560fbc6a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-42159a86ed41f4d83bcd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aa73720ae273bb0bee66">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7fec7e498b6001b34b32">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7c928b8b38fe7a692708">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5d2eeae150e3216f02fb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8c004db8bfd8514d11ac">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6b7a581aaca49a132947">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dd9e2c2667f7cace84f2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b07018da5d89ac9d4b10">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aac434b98369ed0c82bb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-6; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b5c653b01f2cdd295de9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cf5d0d72d45f15d04258">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d0f24335b4c34174e604">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4912da79563e622b928d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-6; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d69afe4cba44082b51fd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-85f26718e630dd31d515">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dda4c91bbd4903d3cbc0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c6fae16481d2faa3847c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-6; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6381d1ed716f23ab4b76">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cb6e2f6e7db596280f95">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-173d6f3bd9e1d073fb9e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2c174aa07dff983193de">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-6; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-14f17a59235b0c88d420">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f1adb0239d54ce1c87d2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4c0d650108a36341b6d4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4e826aefedc04c8759a8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-6; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f29c2ee5b8cd0a9a71ca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-28e3fb9702bdd9c0c839">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0b4dd5aee25655eb79e7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ed7af0e7f0a8299e47cd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-6; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fc7f90169b6d68d09094">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b14ef2c85bf5d7b81237">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ad5427c0923576d0e1b0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c1de57d0ee56fa37e420">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-6; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-eefaeb17333f6b61dfb6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bd4f67668033ed1e889b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6ae6e55f5f450a9f1fef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2bb05e9a2431e9ee197a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-11; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0f8ed606be25318cbe6d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-78373865db3d971e462a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-85d21063e0017683e867">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3829c60ec76719c37563">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-11; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e218efc4442dea9d7b97">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6fdf65f45746c607bdb7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-95cde79e59d70e1bda2e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8a9dd9b54a3482fe7943">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-11; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-50c4292c270c710c0ed9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a9385f5dbd71a02a8a5c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3782be9a4c37e2e41940">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6fc378021566e9daa8e6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-11; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3cbc020486c7ef04bc5b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6062aaebe6c762f0003d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a5b7cfcba679b2109e3f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-86569ce43dc018337f4e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-11; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-499b644bba1f1924e41a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1ec557ba7edf30e07225">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8e784ddff575e97ee07f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3cd56a1deeece224f490">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-11; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-dd4db6744fde8c2f3bf8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-652f5077dad55fc9d76d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0c58b5a4814f9a92abf5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cad1d6ba6391645abebe">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-11; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c314b61037b5ab961185">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9bcdc262d6c74aa6020c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1b19337468598c534f77">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ec51a7e855fb0e7b297a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-12; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-44af3e231d1e30e3834f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-726cdc64adf28d1bbfb7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-edef583d4633c7672035">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1ce648feaf1fbca1f990">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-12; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b5bf0e063c55cd7bc863">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aed44104697c1fb5f531">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-11b4e3431fc409e41fae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-499b4626b484207fa10e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-12; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8fff45cbdc4019aaf4f6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-27aca9c08a132241c4b1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-61562ff216612b9f3f57">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9c0524559b679c3d9871">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-12; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3f11247060d725a4cb46">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e8c0a530ccd114b9752d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3ab956907bbcb5949249">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1bf15607bc450ffce04f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-12; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e2000a64480ec5027604">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9eb8098bfa05c514731a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b24ebc45571b9e1cc7ea">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-db3d052d4fdabc0dd45c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-12; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1b13fcaa1788a07a4d06">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4e844458cc987e8ebc32">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6541ebad5ad6fab150e7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-43194951a69d1fe997bc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-12; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-abd776e55ea0c743bd1c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2a1c4b0a705db8115798">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-54ec10a79e5e74efe9e8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2f6ea75f3107b4f43c7b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-14; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c0683b628fcd846d2b7d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ec90e73596e27df7a413">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c643a00371dd3258aa35">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-352d0901e5e6fe8817f9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-14; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fe619ed293a4f3316118">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fba12e0002412a6eb0bb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7566271cdfd4c7db19a5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d03c27ec9dffdeb17d28">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-14; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9e41b43cb310d85acb6c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-acad61facbcfa7f5c1fa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-18f93223f146b2a7a966">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0883816300bdf2b5da9e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-14; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-aed0ed0173e7f1db8a10">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-da80c00083f4c6dc365b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8859da67e186aaf5d2de">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ab3a15cba77fd47264a2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-14; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-712abe34019bb63cde6a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ed487cf57711835627ab">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-67bda9d515f9d5545cc9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eeed8220bc1be9c1b98a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-14; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-301885ceb611caa4f36b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cbfcacc159bc13b9cbf1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-60f23cc65637defdfa0a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5304cd1e3c26516e6c4e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-14; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d3772860742e1cb4419d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7ed53950fc4543760b3a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d48701a4a785e2da344e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-52509e388fec12132b34">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-15; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d529b6361ba8cf93f980">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-698c2d16e062c8bc6287">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ed7876a94f501025927f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d062b30c3e5626bdb8f6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-15; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e09e9d4e111b9017aea5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f64db5e56aabedde2234">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5b73029efda3419d8759">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c8ffe61d8078157037be">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-15; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f85e61aa95757c830c6e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5e563ce52894d3a2e9e0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b516b47e7824039fae8c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7541c2ec13374dc97b98">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-15; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-69b5e27b7e784f3daf7d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3b8255226d0133932269">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-92ba1aa1ecd322ff9bd3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-10b14d277450f18d23d9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-15; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bbbc4c07ec25a78aa27a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b2c1480b2a99d6dc5e2b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0df30d7c46ab0a2998c2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-40e868c6443f1ae3a4bf">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-15; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5757602bf88c1528713d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4066d341a0f9ed97e02f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-41d3a1f53db4ba482519">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-78eaaa3f428c9515682f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-15; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-019e69358071f8dd3077">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3a7e956cc4baaf937fdb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a0055dfb16e840a31d82">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bc46f414dcc31ccfcce0">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: 1-N-in-1; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-df720693a84b5dd0c454"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-df720693a84b5dd0c454`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-1; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-090e8bc7d22bccb7da9d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-090e8bc7d22bccb7da9d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-1; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1f392098a1af18e5df36"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1f392098a1af18e5df36`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-1; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-05268379e958e14fd090"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-05268379e958e14fd090`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-1; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-1; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f7e041046e4a052ed1b8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f7e041046e4a052ed1b8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-1; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c5d6b04c9ebb9384fe3e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c5d6b04c9ebb9384fe3e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-1; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b8de77ae2c311e2d334c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b8de77ae2c311e2d334c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-1; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-79c5a3808f7f5dac14a8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-79c5a3808f7f5dac14a8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-1; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-1; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-984e29f5b3494ab34eb0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-984e29f5b3494ab34eb0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-1; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fb62271c637b78576cf9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fb62271c637b78576cf9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-1; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-75fa277c36e6fc52cf09"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-75fa277c36e6fc52cf09`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-1; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-56e84d757dcbc0b266e3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-56e84d757dcbc0b266e3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-1; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-1; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-486baadf43d62b48f73d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-486baadf43d62b48f73d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-1; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-191828b70fa4fe142aca"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-191828b70fa4fe142aca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-1; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a63a2aef0c675dcd677f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a63a2aef0c675dcd677f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-1; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cd03e6c990c2e3048d1c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cd03e6c990c2e3048d1c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-1; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-1; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e959d8bea608d3a2d4fa"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e959d8bea608d3a2d4fa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-1; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a4f26933b410b6623176"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a4f26933b410b6623176`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-1; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-afb48e46465858b4d864"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-afb48e46465858b4d864`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-1; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0b5b453b3f19464fa49b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0b5b453b3f19464fa49b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-1; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-1; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d606b080abb7cd8aeec9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d606b080abb7cd8aeec9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-1; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-70f6d90f7e5ba555d5e2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-70f6d90f7e5ba555d5e2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-1; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cb8b024cd3822754235c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cb8b024cd3822754235c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-1; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cf88c9a36b316e795726"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cf88c9a36b316e795726`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-1; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-1; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-dc1a98f1de1171a4f786"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-dc1a98f1de1171a4f786`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-1; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eefcf1ba04f9ddc5785b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-eefcf1ba04f9ddc5785b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-1; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d84d3fbc8b784c3d666d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d84d3fbc8b784c3d666d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-1; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-95087689b9c855a26e35"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-95087689b9c855a26e35`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-1; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-2; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7776798361bc9c0ed7fb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7776798361bc9c0ed7fb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a08bf071edabf5068585"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a08bf071edabf5068585`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-39b00fbb33949426d589"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-39b00fbb33949426d589`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e097020e6538e26a87f7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e097020e6538e26a87f7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-2; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7c743cd58e0982076e6f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7c743cd58e0982076e6f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-57435634825a53609597"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-57435634825a53609597`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0c8f8dc2d58409f680f7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0c8f8dc2d58409f680f7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0979014c2a9213e7f9f9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0979014c2a9213e7f9f9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-2; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-dd6d90b7c1df7a2df7b4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-dd6d90b7c1df7a2df7b4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bc533d5b183908bb5bff"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bc533d5b183908bb5bff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c91372f573550ba23297"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c91372f573550ba23297`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-222b64875a378c48cb55"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-222b64875a378c48cb55`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-2; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-41b322a2a0e43ebfde6c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-41b322a2a0e43ebfde6c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1fc147c7e7095a0e050e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1fc147c7e7095a0e050e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fa2dd2dc94fdcc60f879"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fa2dd2dc94fdcc60f879`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a72ba20eab2d001b9e97"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a72ba20eab2d001b9e97`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-2; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3d8206074e0c2e01b0d0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3d8206074e0c2e01b0d0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f0eb11e4328d4ccc0275"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f0eb11e4328d4ccc0275`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2d9f9a6f979d646064a9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2d9f9a6f979d646064a9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-46de31f8cf7463715177"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-46de31f8cf7463715177`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-2; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-404a1d6a4966f0c212e0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-404a1d6a4966f0c212e0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0f2f6f051a1b278cb86b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0f2f6f051a1b278cb86b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-227e63c8b08dfd6ca0ce"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-227e63c8b08dfd6ca0ce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7dd1a1c435ed37d99251"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7dd1a1c435ed37d99251`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-2; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7ac828b6fc796a3601b3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7ac828b6fc796a3601b3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1b0d05c5c1d27b2cf74d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1b0d05c5c1d27b2cf74d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-02e0cb877788250220c0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-02e0cb877788250220c0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-45c5c3d74742fe674fbb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-45c5c3d74742fe674fbb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b49d96fd379a8ed5cbc9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b49d96fd379a8ed5cbc9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-265c830ab21aa3919fbf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-265c830ab21aa3919fbf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5845870823e37e34a6b8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5845870823e37e34a6b8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d825687f17cec0002023"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d825687f17cec0002023`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6ce950ee680ac257ccd0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6ce950ee680ac257ccd0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-47382f9b42a837ff80b4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-47382f9b42a837ff80b4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c3242d477d123265fc52"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c3242d477d123265fc52`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-87480af298d1f75dec71"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-87480af298d1f75dec71`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bf046ebb0fd3c77be4be"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bf046ebb0fd3c77be4be`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5972fe19d6e8524bc373"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5972fe19d6e8524bc373`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-65ff84aea80e728ac357"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-65ff84aea80e728ac357`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5e9a66d76e7724ba9508"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5e9a66d76e7724ba9508`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9e7e9702c54730a5fdd1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9e7e9702c54730a5fdd1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-84329585853141f60ca4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-84329585853141f60ca4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5df35a395f762e5bafa8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5df35a395f762e5bafa8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3cc4ed636b1aed6373d4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3cc4ed636b1aed6373d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-63ba2822f5c2e12aaf0c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-63ba2822f5c2e12aaf0c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-697b5d4433a0560fbc6a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-697b5d4433a0560fbc6a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-42159a86ed41f4d83bcd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-42159a86ed41f4d83bcd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aa73720ae273bb0bee66"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-aa73720ae273bb0bee66`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7fec7e498b6001b34b32"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7fec7e498b6001b34b32`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7c928b8b38fe7a692708"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7c928b8b38fe7a692708`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5d2eeae150e3216f02fb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5d2eeae150e3216f02fb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8c004db8bfd8514d11ac"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8c004db8bfd8514d11ac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6b7a581aaca49a132947"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6b7a581aaca49a132947`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dd9e2c2667f7cace84f2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-dd9e2c2667f7cace84f2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b07018da5d89ac9d4b10"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b07018da5d89ac9d4b10`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aac434b98369ed0c82bb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-aac434b98369ed0c82bb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-6; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b5c653b01f2cdd295de9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b5c653b01f2cdd295de9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-6; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cf5d0d72d45f15d04258"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cf5d0d72d45f15d04258`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-6; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d0f24335b4c34174e604"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d0f24335b4c34174e604`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-6; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4912da79563e622b928d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4912da79563e622b928d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-6; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-6; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d69afe4cba44082b51fd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d69afe4cba44082b51fd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-6; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-85f26718e630dd31d515"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-85f26718e630dd31d515`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-6; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dda4c91bbd4903d3cbc0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-dda4c91bbd4903d3cbc0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-6; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c6fae16481d2faa3847c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c6fae16481d2faa3847c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-6; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-6; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6381d1ed716f23ab4b76"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6381d1ed716f23ab4b76`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-6; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cb6e2f6e7db596280f95"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cb6e2f6e7db596280f95`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-6; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-173d6f3bd9e1d073fb9e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-173d6f3bd9e1d073fb9e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-6; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2c174aa07dff983193de"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2c174aa07dff983193de`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-6; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-6; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-14f17a59235b0c88d420"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-14f17a59235b0c88d420`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-6; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f1adb0239d54ce1c87d2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f1adb0239d54ce1c87d2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-6; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4c0d650108a36341b6d4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4c0d650108a36341b6d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-6; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4e826aefedc04c8759a8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4e826aefedc04c8759a8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-6; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-6; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f29c2ee5b8cd0a9a71ca"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f29c2ee5b8cd0a9a71ca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-6; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-28e3fb9702bdd9c0c839"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-28e3fb9702bdd9c0c839`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-6; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0b4dd5aee25655eb79e7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0b4dd5aee25655eb79e7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-6; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ed7af0e7f0a8299e47cd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ed7af0e7f0a8299e47cd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-6; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-6; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fc7f90169b6d68d09094"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fc7f90169b6d68d09094`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-6; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b14ef2c85bf5d7b81237"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b14ef2c85bf5d7b81237`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-6; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ad5427c0923576d0e1b0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ad5427c0923576d0e1b0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-6; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c1de57d0ee56fa37e420"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c1de57d0ee56fa37e420`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-6; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-6; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-eefaeb17333f6b61dfb6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-eefaeb17333f6b61dfb6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-6; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bd4f67668033ed1e889b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bd4f67668033ed1e889b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-6; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6ae6e55f5f450a9f1fef"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6ae6e55f5f450a9f1fef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-6; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2bb05e9a2431e9ee197a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2bb05e9a2431e9ee197a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-6; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-11; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0f8ed606be25318cbe6d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0f8ed606be25318cbe6d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-78373865db3d971e462a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-78373865db3d971e462a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-85d21063e0017683e867"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-85d21063e0017683e867`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3829c60ec76719c37563"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3829c60ec76719c37563`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-11; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e218efc4442dea9d7b97"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e218efc4442dea9d7b97`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6fdf65f45746c607bdb7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6fdf65f45746c607bdb7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-95cde79e59d70e1bda2e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-95cde79e59d70e1bda2e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8a9dd9b54a3482fe7943"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8a9dd9b54a3482fe7943`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-11; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-50c4292c270c710c0ed9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-50c4292c270c710c0ed9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a9385f5dbd71a02a8a5c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a9385f5dbd71a02a8a5c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3782be9a4c37e2e41940"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3782be9a4c37e2e41940`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6fc378021566e9daa8e6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6fc378021566e9daa8e6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-11; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3cbc020486c7ef04bc5b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3cbc020486c7ef04bc5b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6062aaebe6c762f0003d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6062aaebe6c762f0003d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a5b7cfcba679b2109e3f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a5b7cfcba679b2109e3f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-86569ce43dc018337f4e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-86569ce43dc018337f4e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-11; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-499b644bba1f1924e41a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-499b644bba1f1924e41a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1ec557ba7edf30e07225"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1ec557ba7edf30e07225`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8e784ddff575e97ee07f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8e784ddff575e97ee07f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3cd56a1deeece224f490"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3cd56a1deeece224f490`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-11; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-dd4db6744fde8c2f3bf8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-dd4db6744fde8c2f3bf8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-652f5077dad55fc9d76d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-652f5077dad55fc9d76d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0c58b5a4814f9a92abf5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0c58b5a4814f9a92abf5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cad1d6ba6391645abebe"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cad1d6ba6391645abebe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-11; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c314b61037b5ab961185"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c314b61037b5ab961185`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9bcdc262d6c74aa6020c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9bcdc262d6c74aa6020c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1b19337468598c534f77"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1b19337468598c534f77`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ec51a7e855fb0e7b297a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ec51a7e855fb0e7b297a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-12; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-44af3e231d1e30e3834f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-44af3e231d1e30e3834f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-12; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-726cdc64adf28d1bbfb7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-726cdc64adf28d1bbfb7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-12; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-edef583d4633c7672035"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-edef583d4633c7672035`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-12; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1ce648feaf1fbca1f990"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1ce648feaf1fbca1f990`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-12; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-12; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b5bf0e063c55cd7bc863"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b5bf0e063c55cd7bc863`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-12; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aed44104697c1fb5f531"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-aed44104697c1fb5f531`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-12; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-11b4e3431fc409e41fae"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-11b4e3431fc409e41fae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-12; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-499b4626b484207fa10e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-499b4626b484207fa10e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-12; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-12; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8fff45cbdc4019aaf4f6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8fff45cbdc4019aaf4f6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-12; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-27aca9c08a132241c4b1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-27aca9c08a132241c4b1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-12; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-61562ff216612b9f3f57"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-61562ff216612b9f3f57`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-12; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9c0524559b679c3d9871"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9c0524559b679c3d9871`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-12; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-12; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3f11247060d725a4cb46"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3f11247060d725a4cb46`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-12; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e8c0a530ccd114b9752d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e8c0a530ccd114b9752d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-12; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3ab956907bbcb5949249"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3ab956907bbcb5949249`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-12; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1bf15607bc450ffce04f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1bf15607bc450ffce04f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-12; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-12; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e2000a64480ec5027604"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e2000a64480ec5027604`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-12; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9eb8098bfa05c514731a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9eb8098bfa05c514731a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-12; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b24ebc45571b9e1cc7ea"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b24ebc45571b9e1cc7ea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-12; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-db3d052d4fdabc0dd45c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-db3d052d4fdabc0dd45c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-12; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-12; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1b13fcaa1788a07a4d06"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1b13fcaa1788a07a4d06`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-12; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4e844458cc987e8ebc32"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4e844458cc987e8ebc32`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-12; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6541ebad5ad6fab150e7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6541ebad5ad6fab150e7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-12; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-43194951a69d1fe997bc"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-43194951a69d1fe997bc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-12; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-12; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-abd776e55ea0c743bd1c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-abd776e55ea0c743bd1c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-12; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2a1c4b0a705db8115798"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2a1c4b0a705db8115798`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-12; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-54ec10a79e5e74efe9e8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-54ec10a79e5e74efe9e8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-12; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2f6ea75f3107b4f43c7b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2f6ea75f3107b4f43c7b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-12; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-14; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c0683b628fcd846d2b7d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c0683b628fcd846d2b7d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ec90e73596e27df7a413"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ec90e73596e27df7a413`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c643a00371dd3258aa35"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c643a00371dd3258aa35`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-352d0901e5e6fe8817f9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-352d0901e5e6fe8817f9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-14; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fe619ed293a4f3316118"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fe619ed293a4f3316118`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fba12e0002412a6eb0bb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fba12e0002412a6eb0bb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7566271cdfd4c7db19a5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7566271cdfd4c7db19a5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d03c27ec9dffdeb17d28"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d03c27ec9dffdeb17d28`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-14; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9e41b43cb310d85acb6c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9e41b43cb310d85acb6c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-acad61facbcfa7f5c1fa"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-acad61facbcfa7f5c1fa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-18f93223f146b2a7a966"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-18f93223f146b2a7a966`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0883816300bdf2b5da9e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0883816300bdf2b5da9e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-14; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-aed0ed0173e7f1db8a10"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-aed0ed0173e7f1db8a10`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-da80c00083f4c6dc365b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-da80c00083f4c6dc365b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8859da67e186aaf5d2de"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8859da67e186aaf5d2de`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ab3a15cba77fd47264a2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ab3a15cba77fd47264a2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-14; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-712abe34019bb63cde6a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-712abe34019bb63cde6a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ed487cf57711835627ab"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ed487cf57711835627ab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-67bda9d515f9d5545cc9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-67bda9d515f9d5545cc9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eeed8220bc1be9c1b98a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-eeed8220bc1be9c1b98a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-14; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-301885ceb611caa4f36b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-301885ceb611caa4f36b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cbfcacc159bc13b9cbf1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cbfcacc159bc13b9cbf1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-60f23cc65637defdfa0a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-60f23cc65637defdfa0a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5304cd1e3c26516e6c4e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5304cd1e3c26516e6c4e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-14; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d3772860742e1cb4419d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d3772860742e1cb4419d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7ed53950fc4543760b3a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7ed53950fc4543760b3a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d48701a4a785e2da344e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d48701a4a785e2da344e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-52509e388fec12132b34"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-52509e388fec12132b34`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-15; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d529b6361ba8cf93f980"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d529b6361ba8cf93f980`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-698c2d16e062c8bc6287"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-698c2d16e062c8bc6287`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ed7876a94f501025927f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ed7876a94f501025927f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d062b30c3e5626bdb8f6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d062b30c3e5626bdb8f6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-W-out-5; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-15; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e09e9d4e111b9017aea5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e09e9d4e111b9017aea5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f64db5e56aabedde2234"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f64db5e56aabedde2234`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5b73029efda3419d8759"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5b73029efda3419d8759`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c8ffe61d8078157037be"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c8ffe61d8078157037be`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-15; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f85e61aa95757c830c6e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f85e61aa95757c830c6e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5e563ce52894d3a2e9e0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5e563ce52894d3a2e9e0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b516b47e7824039fae8c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b516b47e7824039fae8c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7541c2ec13374dc97b98"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7541c2ec13374dc97b98`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-15; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-69b5e27b7e784f3daf7d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-69b5e27b7e784f3daf7d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3b8255226d0133932269"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3b8255226d0133932269`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-92ba1aa1ecd322ff9bd3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-92ba1aa1ecd322ff9bd3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-10b14d277450f18d23d9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-10b14d277450f18d23d9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-E-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-15; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bbbc4c07ec25a78aa27a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bbbc4c07ec25a78aa27a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b2c1480b2a99d6dc5e2b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b2c1480b2a99d6dc5e2b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0df30d7c46ab0a2998c2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0df30d7c46ab0a2998c2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-40e868c6443f1ae3a4bf"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-40e868c6443f1ae3a4bf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-E-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-15; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5757602bf88c1528713d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5757602bf88c1528713d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4066d341a0f9ed97e02f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4066d341a0f9ed97e02f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-41d3a1f53db4ba482519"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-41d3a1f53db4ba482519`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-78eaaa3f428c9515682f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-78eaaa3f428c9515682f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-N-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-15; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-019e69358071f8dd3077"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-019e69358071f8dd3077`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3a7e956cc4baaf937fdb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3a7e956cc4baaf937fdb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a0055dfb16e840a31d82"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a0055dfb16e840a31d82`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bc46f414dcc31ccfcce0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bc46f414dcc31ccfcce0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 1-N-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → pedestrian — 64 cases; unverified: 64</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 1-N-in-1; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-66207e5cd46a640fa5c1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d3895d4e047600c7eabc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7cff7025091c0282eb7b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f7ad0807f126550c27d8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-1; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3599d92470898cbf80ba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9a1f1ba3ccb128084ff7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-161ecdb8175f4fa18da7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9aae6a837b8ef497a07c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-2; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ee85cf3a7147df07d568">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b596fa38a8e04c5e9e28">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-65c459a7dce39abf5d58">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3026cf2fbcb6701dccff">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-2; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-00cb07143aaab168ebbf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bae5bff22f4b18455c34">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e37e5398857c810f3b03">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9dd6e4beac84f26e1cfe">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bf3a4961fcb2b3c201d7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dfad08808ba713ae7a26">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b5a060a33d10a97ad684">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0a13044ac78e151947c5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1a2c1801a04725cb1fec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-66b6c40f243fd50176db">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-15298145597fe7802b11">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3d31a314dcd038bbe33f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-6; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1cc550ba1f48eb2c39c9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dcf18814e5b4c542fdf2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c18011b30d2d0719facf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-af7e461f9f45e34e35be">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-6; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1a6907cfe195ce614e8d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-742204cef203da08eec2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-def34110747e0ea3e5f0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cd3f5ca38747d03848fa">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-11; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c2feef91ef21675d15c9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e2b1f5f4c7923d3d8e15">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aa2f76716f51b8b026dc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-403761a181ccb914f30a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-11; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-81f04fb3e3b9a7757efa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cace9a20375918d5ef11">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-732860c73f86da3c68fc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0594a678340e331562dc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-12; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-30ccae8de5b0fe198a77">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7389ffffc2a587f000e0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6f8ddbeb36ad81190c3a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-30e95a7402590b7bc287">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-12; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-162060b2dd2eccc3511a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-812c07e6ea76bb0a20e4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3db8808ba79617fc8caf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5f8997e14eb27a3b9c51">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-14; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ce6405418fe95ea7aa7a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8d3246bdd701a8e2017e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9876c5a930fa1e23ceeb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-69c865406dc63d1d8137">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-14; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-82437140ddf1f9611ef8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-63939c055f270b3e1fae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f31b85fedde99a11aa46">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aab4c3bd7907a499a7c8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-15; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6dbd088c59d6db5d5cfe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6b781baf652d500dee86">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-72caf1f694232273af49">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9dfd740ffc024b322b0a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-15; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6913e6e3b004775077eb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e6acd0cd3fbafef5fc55">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-de9399145da68bf81bb7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4e9093e831f4614a1b9f">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: 1-N-in-1; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-66207e5cd46a640fa5c1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-66207e5cd46a640fa5c1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-1; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d3895d4e047600c7eabc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d3895d4e047600c7eabc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-1; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7cff7025091c0282eb7b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7cff7025091c0282eb7b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-1; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f7ad0807f126550c27d8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f7ad0807f126550c27d8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-1; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-1; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3599d92470898cbf80ba"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3599d92470898cbf80ba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-1; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9a1f1ba3ccb128084ff7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9a1f1ba3ccb128084ff7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-1; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-161ecdb8175f4fa18da7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-161ecdb8175f4fa18da7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-1; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9aae6a837b8ef497a07c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9aae6a837b8ef497a07c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-1; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-2; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ee85cf3a7147df07d568"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ee85cf3a7147df07d568`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b596fa38a8e04c5e9e28"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b596fa38a8e04c5e9e28`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-65c459a7dce39abf5d58"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-65c459a7dce39abf5d58`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3026cf2fbcb6701dccff"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3026cf2fbcb6701dccff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-2; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-00cb07143aaab168ebbf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-00cb07143aaab168ebbf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bae5bff22f4b18455c34"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bae5bff22f4b18455c34`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e37e5398857c810f3b03"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e37e5398857c810f3b03`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9dd6e4beac84f26e1cfe"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9dd6e4beac84f26e1cfe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bf3a4961fcb2b3c201d7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bf3a4961fcb2b3c201d7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dfad08808ba713ae7a26"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-dfad08808ba713ae7a26`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b5a060a33d10a97ad684"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b5a060a33d10a97ad684`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0a13044ac78e151947c5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0a13044ac78e151947c5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1a2c1801a04725cb1fec"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1a2c1801a04725cb1fec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-66b6c40f243fd50176db"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-66b6c40f243fd50176db`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-15298145597fe7802b11"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-15298145597fe7802b11`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3d31a314dcd038bbe33f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3d31a314dcd038bbe33f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-6; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1cc550ba1f48eb2c39c9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1cc550ba1f48eb2c39c9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-6; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dcf18814e5b4c542fdf2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-dcf18814e5b4c542fdf2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-6; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c18011b30d2d0719facf"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c18011b30d2d0719facf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-6; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-af7e461f9f45e34e35be"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-af7e461f9f45e34e35be`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-6; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-6; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1a6907cfe195ce614e8d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1a6907cfe195ce614e8d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-6; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-742204cef203da08eec2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-742204cef203da08eec2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-6; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-def34110747e0ea3e5f0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-def34110747e0ea3e5f0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-6; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cd3f5ca38747d03848fa"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cd3f5ca38747d03848fa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-6; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-11; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c2feef91ef21675d15c9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c2feef91ef21675d15c9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e2b1f5f4c7923d3d8e15"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e2b1f5f4c7923d3d8e15`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aa2f76716f51b8b026dc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-aa2f76716f51b8b026dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-403761a181ccb914f30a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-403761a181ccb914f30a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-11; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-81f04fb3e3b9a7757efa"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-81f04fb3e3b9a7757efa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cace9a20375918d5ef11"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cace9a20375918d5ef11`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-732860c73f86da3c68fc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-732860c73f86da3c68fc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0594a678340e331562dc"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0594a678340e331562dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-11; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-12; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-30ccae8de5b0fe198a77"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-30ccae8de5b0fe198a77`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-12; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7389ffffc2a587f000e0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7389ffffc2a587f000e0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-12; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6f8ddbeb36ad81190c3a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6f8ddbeb36ad81190c3a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-12; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-30e95a7402590b7bc287"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-30e95a7402590b7bc287`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-12; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-12; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-162060b2dd2eccc3511a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-162060b2dd2eccc3511a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-12; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-812c07e6ea76bb0a20e4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-812c07e6ea76bb0a20e4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-12; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3db8808ba79617fc8caf"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3db8808ba79617fc8caf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-12; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5f8997e14eb27a3b9c51"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5f8997e14eb27a3b9c51`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-12; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-14; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ce6405418fe95ea7aa7a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ce6405418fe95ea7aa7a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8d3246bdd701a8e2017e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8d3246bdd701a8e2017e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9876c5a930fa1e23ceeb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9876c5a930fa1e23ceeb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-69c865406dc63d1d8137"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-69c865406dc63d1d8137`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-14; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-82437140ddf1f9611ef8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-82437140ddf1f9611ef8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-63939c055f270b3e1fae"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-63939c055f270b3e1fae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f31b85fedde99a11aa46"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f31b85fedde99a11aa46`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aab4c3bd7907a499a7c8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-aab4c3bd7907a499a7c8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-15; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6dbd088c59d6db5d5cfe"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6dbd088c59d6db5d5cfe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6b781baf652d500dee86"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6b781baf652d500dee86`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-72caf1f694232273af49"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-72caf1f694232273af49`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9dfd740ffc024b322b0a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9dfd740ffc024b322b0a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-15; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6913e6e3b004775077eb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6913e6e3b004775077eb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e6acd0cd3fbafef5fc55"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e6acd0cd3fbafef5fc55`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-de9399145da68bf81bb7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-de9399145da68bf81bb7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4e9093e831f4614a1b9f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4e9093e831f4614a1b9f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-15; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — pedestrian → road — 64 cases; unverified: 64</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-W-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e75f34a97169a4a54ad0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-53bbc3ad5fd7c979bf49">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f56cb7ade7b40366d8ff">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-555d19efff847a72a623">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-W-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b8268b9fcb586b36e4d3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0663c8ab09d3c2560ebe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ced459db7df573804034">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dd09e7851cfb7d6e4146">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-W-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-dbc2473e5868c0e793da">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-75b694341315bfac9c12">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-22f9cb7a38fedc3f7cb5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-55d3914b6575f2c35643">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-W-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ced061156bcff10f4d3a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d2ec636c9067b45381a3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0362d6cf09c6b0b251a2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-79f7b0e53bb6b8305f5b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-E-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-88e5b96c429dd3888d30">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b2247bdabc2b53f27ab0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3a7b587e5c5b72d30580">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b2e8dc3f8562babbd625">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-E-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9c50253cbbaf94db070a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e472682f6b0852b59b35">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ddc41bc3bfcb06f55fa3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3ebd7968a09ef160cd87">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-N-out-13; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7c48ff4e9b8159eef310">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2e9aa464d0ab66c9c380">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-62949b2a6fc393ee1d48">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-947c22a99a0e72e3c1f2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-N-out-16; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-24fb61a2a4a6e7322673">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d3ffc3b43e7f60f2842c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-25cf44b69ea0d0a86891">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1ab05dea87df605bc2f8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-W-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-99a359bdf423d8fa27e9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3d5f04122ce15335251e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7829c1db337f0dc84a05">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5bdb04c8dc6528ae07ad">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-W-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-038fdadba6fa09c80c7a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-929e6cd79b7c16f8e4ab">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-decee506e8723a152007">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-de23881b35e9599a70f4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-W-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-59dd98b6760487a31e3d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-160ca6e217e8ec236e13">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fd6e0a55f6d4a278adbc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-86a4ae417865b06bb176">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-W-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3d8d3c6ddfee827b515e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e7746d4f27631b59ab9d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-78114e77549b48140016">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d60e4ed0db3729e41562">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-E-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a790f3bc897e0450aa29">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-09ba3e83d96d620410a8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c637e24a35fef63998ac">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-330cc48709e35789fd72">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-E-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8bf8fe900e27404a5bca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-90fd69c3ada6bea7461b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-168a1cc9cbe28fe4bd77">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-492110eabd7d1bc071e8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-N-out-13; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0b235462c955fbb18eb5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e0d89bc6e51f5f6cb70a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e7b93159f2f11f0a7016">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-acb609d4a08ee89f0975">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-N-out-16; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fd79ee0a084277462fd1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bdd5342acfadcef71916">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6d15c75d8203f6331250">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a2c9448956e6a69a776e">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: 2-N-in-1; to port: 1-W-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e75f34a97169a4a54ad0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e75f34a97169a4a54ad0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-53bbc3ad5fd7c979bf49"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-53bbc3ad5fd7c979bf49`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f56cb7ade7b40366d8ff"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f56cb7ade7b40366d8ff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-555d19efff847a72a623"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-555d19efff847a72a623`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-N-in-1; to port: 1-W-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b8268b9fcb586b36e4d3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b8268b9fcb586b36e4d3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0663c8ab09d3c2560ebe"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0663c8ab09d3c2560ebe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ced459db7df573804034"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ced459db7df573804034`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dd09e7851cfb7d6e4146"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dd09e7851cfb7d6e4146`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-N-in-1; to port: 1-W-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-dbc2473e5868c0e793da"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-dbc2473e5868c0e793da`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-75b694341315bfac9c12"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-75b694341315bfac9c12`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-22f9cb7a38fedc3f7cb5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-22f9cb7a38fedc3f7cb5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-55d3914b6575f2c35643"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-55d3914b6575f2c35643`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-N-in-1; to port: 1-W-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ced061156bcff10f4d3a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ced061156bcff10f4d3a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d2ec636c9067b45381a3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d2ec636c9067b45381a3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0362d6cf09c6b0b251a2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0362d6cf09c6b0b251a2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-79f7b0e53bb6b8305f5b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-79f7b0e53bb6b8305f5b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-N-in-1; to port: 1-E-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-88e5b96c429dd3888d30"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-88e5b96c429dd3888d30`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-E-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b2247bdabc2b53f27ab0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b2247bdabc2b53f27ab0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-E-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3a7b587e5c5b72d30580"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3a7b587e5c5b72d30580`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-E-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b2e8dc3f8562babbd625"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b2e8dc3f8562babbd625`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-E-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-N-in-1; to port: 1-E-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9c50253cbbaf94db070a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9c50253cbbaf94db070a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-E-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e472682f6b0852b59b35"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e472682f6b0852b59b35`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-E-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ddc41bc3bfcb06f55fa3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ddc41bc3bfcb06f55fa3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-E-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3ebd7968a09ef160cd87"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3ebd7968a09ef160cd87`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-E-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-N-in-1; to port: 1-N-out-13; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7c48ff4e9b8159eef310"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7c48ff4e9b8159eef310`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-N-out-13; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2e9aa464d0ab66c9c380"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2e9aa464d0ab66c9c380`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-N-out-13; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-62949b2a6fc393ee1d48"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-62949b2a6fc393ee1d48`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-N-out-13; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-947c22a99a0e72e3c1f2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-947c22a99a0e72e3c1f2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-N-out-13; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-N-in-1; to port: 1-N-out-16; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-24fb61a2a4a6e7322673"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-24fb61a2a4a6e7322673`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-N-out-16; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d3ffc3b43e7f60f2842c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d3ffc3b43e7f60f2842c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-N-out-16; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-25cf44b69ea0d0a86891"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-25cf44b69ea0d0a86891`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-N-out-16; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1ab05dea87df605bc2f8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1ab05dea87df605bc2f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-N-out-16; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-W-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-99a359bdf423d8fa27e9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-99a359bdf423d8fa27e9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3d5f04122ce15335251e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3d5f04122ce15335251e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7829c1db337f0dc84a05"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7829c1db337f0dc84a05`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5bdb04c8dc6528ae07ad"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5bdb04c8dc6528ae07ad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-W-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-038fdadba6fa09c80c7a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-038fdadba6fa09c80c7a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-929e6cd79b7c16f8e4ab"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-929e6cd79b7c16f8e4ab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-decee506e8723a152007"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-decee506e8723a152007`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-de23881b35e9599a70f4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-de23881b35e9599a70f4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-5; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-W-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-59dd98b6760487a31e3d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-59dd98b6760487a31e3d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-160ca6e217e8ec236e13"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-160ca6e217e8ec236e13`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fd6e0a55f6d4a278adbc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fd6e0a55f6d4a278adbc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-86a4ae417865b06bb176"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-86a4ae417865b06bb176`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-W-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3d8d3c6ddfee827b515e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3d8d3c6ddfee827b515e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e7746d4f27631b59ab9d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e7746d4f27631b59ab9d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-78114e77549b48140016"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-78114e77549b48140016`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d60e4ed0db3729e41562"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d60e4ed0db3729e41562`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-E-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a790f3bc897e0450aa29"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a790f3bc897e0450aa29`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-09ba3e83d96d620410a8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-09ba3e83d96d620410a8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c637e24a35fef63998ac"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c637e24a35fef63998ac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-330cc48709e35789fd72"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-330cc48709e35789fd72`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-E-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8bf8fe900e27404a5bca"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8bf8fe900e27404a5bca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-90fd69c3ada6bea7461b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-90fd69c3ada6bea7461b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-168a1cc9cbe28fe4bd77"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-168a1cc9cbe28fe4bd77`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-492110eabd7d1bc071e8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-492110eabd7d1bc071e8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-N-out-13; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0b235462c955fbb18eb5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0b235462c955fbb18eb5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-13; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e0d89bc6e51f5f6cb70a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e0d89bc6e51f5f6cb70a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-13; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e7b93159f2f11f0a7016"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e7b93159f2f11f0a7016`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-13; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-acb609d4a08ee89f0975"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-acb609d4a08ee89f0975`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-13; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-N-out-16; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fd79ee0a084277462fd1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fd79ee0a084277462fd1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-16; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bdd5342acfadcef71916"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bdd5342acfadcef71916`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-16; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6d15c75d8203f6331250"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6d15c75d8203f6331250`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-16; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a2c9448956e6a69a776e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a2c9448956e6a69a776e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-16; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — pedestrian → pedestrian — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 2-W-out-2; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f870fdade6c1dace97dc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d3336348a277659d8843">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ee5a5b92307344227ec1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2a0af5c73ae82d6965f7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 2-E-out-3; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d198fe80e24c35d30deb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5f8770ca2cc643e99fd5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-55c211ae93f3c83bba8e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1ed70c5ecea888af452d">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: 2-N-in-1; to port: 2-W-out-2; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f870fdade6c1dace97dc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f870fdade6c1dace97dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 2-W-out-2; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d3336348a277659d8843"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d3336348a277659d8843`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 2-W-out-2; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ee5a5b92307344227ec1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ee5a5b92307344227ec1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 2-W-out-2; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2a0af5c73ae82d6965f7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2a0af5c73ae82d6965f7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 2-W-out-2; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 2-E-out-3; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d198fe80e24c35d30deb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d198fe80e24c35d30deb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 2-E-out-3; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5f8770ca2cc643e99fd5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5f8770ca2cc643e99fd5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 2-E-out-3; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-55c211ae93f3c83bba8e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-55c211ae93f3c83bba8e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 2-E-out-3; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1ed70c5ecea888af452d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1ed70c5ecea888af452d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 2-E-out-3; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

Created on branch `codex/double-decker-diagonal-highway` for a compact Tokyo-style interchange. The earlier source-only schematic remains separately identified in the assembly’s design history. Saved-city resource identifiers are reserved locally and must remain stable; public allocation and redistribution are pending.
