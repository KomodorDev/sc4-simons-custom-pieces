---
title: "Testing: DD RHW-4 Level 1 (7.5 m) and Level 2 (15 m) over Avenue Ground (0 m) \u2014 Diagonal Crossing 90\u00b0"
summary: "Inspect this piece\u2019s exact checks, resource evidence, and explicit human observations."
audience: "contributors"
document_type: "reference"
---

# Testing: DD RHW-4 Level 1 (7.5 m) and Level 2 (15 m) over Avenue Ground (0 m) — Diagonal Crossing 90°

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

Preserves the native diagonal DD RHW-4 through lanes at 7.5 m and 15 m over a ground diagonal avenue. This standalone crossing has no ramp transfers; the compact interchange uses a separate coordinated access core. The generated records below describe movements measured from saved PATH resources, meaning the game’s directed traffic routes. A measured route does not establish game operation or a complete native joining boundary.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `avenue-lane-01-a` | road / 1 / primary | in | [-3.2, -8.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-668896c488171c19873d` |
| `avenue-lane-02-a` | road / 1 / primary | in | [3.2, -8.0, 0.0]; [0.7071067811865475, -0.7071067811865476]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `lower-lane-02-b` | road / 1 / primary | out | [8.0, -35.2, 7.5]; [-0.7071067811865475, -0.7071067811865477]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `upper-lane-01-a` | road / 1 / primary | in | [8.0, -35.2, 15.0]; [0.7071067811865475, 0.7071067811865477]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `lower-lane-01-b` | road / 1 / primary | out | [8.0, -28.8, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `upper-lane-02-a` | road / 1 / primary | in | [8.0, -28.8, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `avenue-lane-03-b` | road / 1 / primary | out | [8.0, -3.2, 0.0]; [-0.7071067811865476, 0.7071067811865475]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `avenue-lane-04-b` | road / 1 / primary | out | [8.0, 3.2, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `avenue-lane-01-b` | road / 1 / primary | out | [24.0, -35.2, 0.0]; [0.7071067811865475, -0.7071067811865477]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `avenue-lane-02-b` | road / 1 / primary | out | [24.0, -28.8, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `avenue-lane-03-a` | road / 1 / primary | in | [28.8, -24.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `lower-lane-01-a` | road / 1 / primary | in | [28.8, -8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `upper-lane-02-b` | road / 1 / primary | out | [28.8, -8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `avenue-lane-04-a` | road / 1 / primary | in | [35.2, -24.0, 0.0]; [-0.7071067811865477, 0.7071067811865475]; 0.0 | `path-interface-668896c488171c19873d` |
| `lower-lane-02-a` | road / 1 / primary | in | [35.2, -8.0, 7.5]; [-0.7071067811865477, -0.7071067811865475]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `upper-lane-01-b` | road / 1 / primary | out | [35.2, -8.0, 15.0]; [0.7071067811865477, 0.7071067811865475]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `avenue-walkway-01-a` | pedestrian / 2 / primary | in | [-7.3, -8.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-2ec6b824afff9b450810` |
| `avenue-walkway-02-b` | pedestrian / 2 / primary | out | [8.0, 7.3, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-ef45fb4474012bf121a0` |
| `avenue-walkway-01-b` | pedestrian / 2 / primary | out | [24.0, -39.3, 0.0]; [0.7071067811865477, -0.7071067811865475]; 0.0 | `path-interface-ef45fb4474012bf121a0` |
| `avenue-walkway-02-a` | pedestrian / 2 / primary | in | [39.3, -24.0, 0.0]; [-0.7071067811865475, 0.7071067811865477]; 0.0 | `path-interface-2ec6b824afff9b450810` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `avenue-lane-01-a` → `avenue-lane-01-b` | primary |
| road | `avenue-lane-02-a` → `avenue-lane-02-b` | primary |
| road | `upper-lane-01-a` → `upper-lane-01-b` | primary |
| road | `upper-lane-02-a` → `upper-lane-02-b` | primary |
| road | `avenue-lane-03-a` → `avenue-lane-03-b` | primary |
| road | `lower-lane-01-a` → `lower-lane-01-b` | primary |
| road | `avenue-lane-04-a` → `avenue-lane-04-b` | primary |
| road | `lower-lane-02-a` → `lower-lane-02-b` | primary |
| pedestrian | `avenue-walkway-01-a` → `avenue-walkway-01-b` | primary |
| pedestrian | `avenue-walkway-02-a` → `avenue-walkway-02-b` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `avenue-lane-01-a` | road / `lower-lane-02-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `avenue-lane-01-a` | road / `lower-lane-01-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `avenue-lane-01-a` | road / `avenue-lane-03-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `avenue-lane-01-a` | road / `avenue-lane-04-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `avenue-lane-01-a` | road / `avenue-lane-02-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `avenue-lane-01-a` | road / `upper-lane-02-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `avenue-lane-01-a` | road / `upper-lane-01-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `avenue-lane-01-a` | pedestrian / `avenue-walkway-02-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `avenue-lane-01-a` | pedestrian / `avenue-walkway-01-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `avenue-lane-02-a` | road / `lower-lane-02-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `avenue-lane-02-a` | road / `lower-lane-01-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `avenue-lane-02-a` | road / `avenue-lane-03-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `avenue-lane-02-a` | road / `avenue-lane-04-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `avenue-lane-02-a` | road / `avenue-lane-01-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `avenue-lane-02-a` | road / `upper-lane-02-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `avenue-lane-02-a` | road / `upper-lane-01-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `avenue-lane-02-a` | pedestrian / `avenue-walkway-02-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `avenue-lane-02-a` | pedestrian / `avenue-walkway-01-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-01-a` | road / `lower-lane-02-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-01-a` | road / `lower-lane-01-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-01-a` | road / `avenue-lane-03-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-01-a` | road / `avenue-lane-04-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-01-a` | road / `avenue-lane-01-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-01-a` | road / `avenue-lane-02-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-01-a` | road / `upper-lane-02-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-01-a` | pedestrian / `avenue-walkway-02-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-01-a` | pedestrian / `avenue-walkway-01-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-02-a` | road / `lower-lane-02-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-02-a` | road / `lower-lane-01-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-02-a` | road / `avenue-lane-03-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-02-a` | road / `avenue-lane-04-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-02-a` | road / `avenue-lane-01-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-02-a` | road / `avenue-lane-02-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-02-a` | road / `upper-lane-01-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-02-a` | pedestrian / `avenue-walkway-02-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `upper-lane-02-a` | pedestrian / `avenue-walkway-01-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `avenue-lane-03-a` | road / `lower-lane-02-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `avenue-lane-03-a` | road / `lower-lane-01-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `avenue-lane-03-a` | road / `avenue-lane-04-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `avenue-lane-03-a` | road / `avenue-lane-01-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `avenue-lane-03-a` | road / `avenue-lane-02-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `avenue-lane-03-a` | road / `upper-lane-02-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `avenue-lane-03-a` | road / `upper-lane-01-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `avenue-lane-03-a` | pedestrian / `avenue-walkway-02-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `avenue-lane-03-a` | pedestrian / `avenue-walkway-01-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-01-a` | road / `lower-lane-02-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-01-a` | road / `avenue-lane-03-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-01-a` | road / `avenue-lane-04-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-01-a` | road / `avenue-lane-01-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-01-a` | road / `avenue-lane-02-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-01-a` | road / `upper-lane-02-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-01-a` | road / `upper-lane-01-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-01-a` | pedestrian / `avenue-walkway-02-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-01-a` | pedestrian / `avenue-walkway-01-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `avenue-lane-04-a` | road / `lower-lane-02-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `avenue-lane-04-a` | road / `lower-lane-01-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `avenue-lane-04-a` | road / `avenue-lane-03-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `avenue-lane-04-a` | road / `avenue-lane-01-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `avenue-lane-04-a` | road / `avenue-lane-02-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `avenue-lane-04-a` | road / `upper-lane-02-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `avenue-lane-04-a` | road / `upper-lane-01-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `avenue-lane-04-a` | pedestrian / `avenue-walkway-02-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `avenue-lane-04-a` | pedestrian / `avenue-walkway-01-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-02-a` | road / `lower-lane-01-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-02-a` | road / `avenue-lane-03-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-02-a` | road / `avenue-lane-04-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-02-a` | road / `avenue-lane-01-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-02-a` | road / `avenue-lane-02-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-02-a` | road / `upper-lane-02-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-02-a` | road / `upper-lane-01-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-02-a` | pedestrian / `avenue-walkway-02-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `lower-lane-02-a` | pedestrian / `avenue-walkway-01-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `avenue-walkway-01-a` | road / `lower-lane-02-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `avenue-walkway-01-a` | road / `lower-lane-01-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `avenue-walkway-01-a` | road / `avenue-lane-03-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `avenue-walkway-01-a` | road / `avenue-lane-04-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `avenue-walkway-01-a` | road / `avenue-lane-01-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `avenue-walkway-01-a` | road / `avenue-lane-02-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `avenue-walkway-01-a` | road / `upper-lane-02-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `avenue-walkway-01-a` | road / `upper-lane-01-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `avenue-walkway-01-a` | pedestrian / `avenue-walkway-02-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `avenue-walkway-02-a` | road / `lower-lane-02-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `avenue-walkway-02-a` | road / `lower-lane-01-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `avenue-walkway-02-a` | road / `avenue-lane-03-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `avenue-walkway-02-a` | road / `avenue-lane-04-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `avenue-walkway-02-a` | road / `avenue-lane-01-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `avenue-walkway-02-a` | road / `avenue-lane-02-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `avenue-walkway-02-a` | road / `upper-lane-02-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `avenue-walkway-02-a` | road / `upper-lane-01-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `avenue-walkway-02-a` | pedestrian / `avenue-walkway-01-b` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use the exact NAM 50 right-hand-traffic profile in `config/profiles/nam50-rhd.jsonc`, flat terrain, and the [assembly test setup](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#2-test-setup). Keep personal settings and game archives outside Git. Building does not install this component.

## 3. Software checks

From the repository root, build the selected component with `python3 -B custom-pieces/scp.py build --include ddrhw-l1-and-l2-over-avenue-l0-crossing-diagonal-90deg --output custom-pieces/dist/highway-component`, then run `python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/highway-component`. Run the shared [highway checks](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#3-software-checks) for geometry, saved paths, and assembled seams. Model verification checks actual saved triangles and PATH points; it does not merely reread a source label.

## 4. Game checks

Place this component as part of the complete assembly in each of its four rotations. Check its roads, barriers, and neighbouring seams; use Route Query and visible traffic to observe each listed movement independently. Check avenue pedestrians where present. Demolish and replace it, save the city, reload it, and inspect shadows at several game times. Use the [shared observation procedure](../../../../docs/TESTING.md) to record only matching human observations.

## 5. Results and known issues

The current assembly’s executed checks and remaining limitations are recorded in [Results and known issues](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#5-results-and-known-issues). This component is experimental and has no human game pass. Native DD models have local overhangs; pavement coverage and corridor face-intersection checks are not a complete vehicle swept-volume or structural proof.

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
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-l1-and-l2-over-avenue-l0-crossing-diagonal-90deg/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-l1-and-l2-over-avenue-l0-crossing-diagonal-90deg/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-5709bfee0535c2b49d2d">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-5709bfee0535c2b49d2d"></a>

**General: unverified** — `software_resources-5709bfee0535c2b49d2d`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-5709bfee0535c2b49d2d">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-5709bfee0535c2b49d2d"></a>

**General: unverified** — `software_connectivity-5709bfee0535c2b49d2d`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-1937e6ab87db596fdea9">[ ] unverified</a> | <a href="#case-in_game_render-3725c79c60db19f8ff11">[ ] unverified</a> | <a href="#case-in_game_render-21e1a9fe02b4f139e699">[ ] unverified</a> | <a href="#case-in_game_render-afe011dbb2387a9ff2be">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-1937e6ab87db596fdea9"></a>

**0° CCW: unverified** — `in_game_render-1937e6ab87db596fdea9`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-3725c79c60db19f8ff11"></a>

**90° CCW: unverified** — `in_game_render-3725c79c60db19f8ff11`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-21e1a9fe02b4f139e699"></a>

**180° CCW: unverified** — `in_game_render-21e1a9fe02b4f139e699`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-afe011dbb2387a9ff2be"></a>

**270° CCW: unverified** — `in_game_render-afe011dbb2387a9ff2be`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-1937e6ab87db596fdea9">[ ] unverified</a> | <a href="#case-in_game_placement-3725c79c60db19f8ff11">[ ] unverified</a> | <a href="#case-in_game_placement-21e1a9fe02b4f139e699">[ ] unverified</a> | <a href="#case-in_game_placement-afe011dbb2387a9ff2be">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-1937e6ab87db596fdea9"></a>

**0° CCW: unverified** — `in_game_placement-1937e6ab87db596fdea9`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-3725c79c60db19f8ff11"></a>

**90° CCW: unverified** — `in_game_placement-3725c79c60db19f8ff11`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-21e1a9fe02b4f139e699"></a>

**180° CCW: unverified** — `in_game_placement-21e1a9fe02b4f139e699`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-afe011dbb2387a9ff2be"></a>

**270° CCW: unverified** — `in_game_placement-afe011dbb2387a9ff2be`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-1937e6ab87db596fdea9">[ ] unverified</a> | <a href="#case-in_game_demolition-3725c79c60db19f8ff11">[ ] unverified</a> | <a href="#case-in_game_demolition-21e1a9fe02b4f139e699">[ ] unverified</a> | <a href="#case-in_game_demolition-afe011dbb2387a9ff2be">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-1937e6ab87db596fdea9"></a>

**0° CCW: unverified** — `in_game_demolition-1937e6ab87db596fdea9`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-3725c79c60db19f8ff11"></a>

**90° CCW: unverified** — `in_game_demolition-3725c79c60db19f8ff11`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-21e1a9fe02b4f139e699"></a>

**180° CCW: unverified** — `in_game_demolition-21e1a9fe02b4f139e699`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-afe011dbb2387a9ff2be"></a>

**270° CCW: unverified** — `in_game_demolition-afe011dbb2387a9ff2be`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-1937e6ab87db596fdea9">[ ] unverified</a> | <a href="#case-in_game_save_reload-3725c79c60db19f8ff11">[ ] unverified</a> | <a href="#case-in_game_save_reload-21e1a9fe02b4f139e699">[ ] unverified</a> | <a href="#case-in_game_save_reload-afe011dbb2387a9ff2be">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-1937e6ab87db596fdea9"></a>

**0° CCW: unverified** — `in_game_save_reload-1937e6ab87db596fdea9`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-3725c79c60db19f8ff11"></a>

**90° CCW: unverified** — `in_game_save_reload-3725c79c60db19f8ff11`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-21e1a9fe02b4f139e699"></a>

**180° CCW: unverified** — `in_game_save_reload-21e1a9fe02b4f139e699`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-afe011dbb2387a9ff2be"></a>

**270° CCW: unverified** — `in_game_save_reload-afe011dbb2387a9ff2be`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 32 cases; unverified: 32</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:avenue-lane-01-a>avenue-lane-01-b; entry: avenue-lane-01-a; exit: avenue-lane-01-b | — | <a href="#case-in_game_route_query-7fac93716e874d0e91f9">[ ] unverified</a> | <a href="#case-in_game_route_query-77b4fb7b0dfbe4ee6d7d">[ ] unverified</a> | <a href="#case-in_game_route_query-a14404d3c753772da4d6">[ ] unverified</a> | <a href="#case-in_game_route_query-1a9aa27f2500bca1c57c">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:avenue-lane-02-a>avenue-lane-02-b; entry: avenue-lane-02-a; exit: avenue-lane-02-b | — | <a href="#case-in_game_route_query-ab54caa6dd51363531a9">[ ] unverified</a> | <a href="#case-in_game_route_query-51f9f4f6e8b84c6ed5ec">[ ] unverified</a> | <a href="#case-in_game_route_query-a1246218987bf69cdd8b">[ ] unverified</a> | <a href="#case-in_game_route_query-a9c2d64641fbd2813b28">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:upper-lane-01-a>upper-lane-01-b; entry: upper-lane-01-a; exit: upper-lane-01-b | — | <a href="#case-in_game_route_query-431853dbe37083269c0f">[ ] unverified</a> | <a href="#case-in_game_route_query-3564afda2c0ce75c88ac">[ ] unverified</a> | <a href="#case-in_game_route_query-7070bd5f80862d6e818d">[ ] unverified</a> | <a href="#case-in_game_route_query-2fdf1bfc58e0f8245797">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:upper-lane-02-a>upper-lane-02-b; entry: upper-lane-02-a; exit: upper-lane-02-b | — | <a href="#case-in_game_route_query-7e3337d5aff0cb3b9dfd">[ ] unverified</a> | <a href="#case-in_game_route_query-c989abac74362507eb55">[ ] unverified</a> | <a href="#case-in_game_route_query-fe2d9e816845210c6ab8">[ ] unverified</a> | <a href="#case-in_game_route_query-b1355ac46beb861c388e">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:avenue-lane-03-a>avenue-lane-03-b; entry: avenue-lane-03-a; exit: avenue-lane-03-b | — | <a href="#case-in_game_route_query-fb3d0acb042014de9c03">[ ] unverified</a> | <a href="#case-in_game_route_query-15c823f1992f12a339d8">[ ] unverified</a> | <a href="#case-in_game_route_query-ecb32f3b74b6759934db">[ ] unverified</a> | <a href="#case-in_game_route_query-aec3b93747a03e5b908f">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:lower-lane-01-a>lower-lane-01-b; entry: lower-lane-01-a; exit: lower-lane-01-b | — | <a href="#case-in_game_route_query-15d0ef6416e43a23e26c">[ ] unverified</a> | <a href="#case-in_game_route_query-c70c77bc357520c826e0">[ ] unverified</a> | <a href="#case-in_game_route_query-c7c761820f5a0e38e17c">[ ] unverified</a> | <a href="#case-in_game_route_query-54aa42276e920693d789">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:avenue-lane-04-a>avenue-lane-04-b; entry: avenue-lane-04-a; exit: avenue-lane-04-b | — | <a href="#case-in_game_route_query-422e0ad896eed7747753">[ ] unverified</a> | <a href="#case-in_game_route_query-a3ec9473ded339c2b0e8">[ ] unverified</a> | <a href="#case-in_game_route_query-fdc2dfbc6187bd35df37">[ ] unverified</a> | <a href="#case-in_game_route_query-4248833c54dbd4e82f04">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:lower-lane-02-a>lower-lane-02-b; entry: lower-lane-02-a; exit: lower-lane-02-b | — | <a href="#case-in_game_route_query-72283520a3a97713da28">[ ] unverified</a> | <a href="#case-in_game_route_query-c53b1e8898c2baed66ae">[ ] unverified</a> | <a href="#case-in_game_route_query-4a5079c9bd3fe1c81349">[ ] unverified</a> | <a href="#case-in_game_route_query-3d5a46bf2062e6d154df">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:avenue-lane-01-a>avenue-lane-01-b; entry: avenue-lane-01-a; exit: avenue-lane-01-b</summary>

<a id="case-in_game_route_query-7fac93716e874d0e91f9"></a>

**0° CCW: unverified** — `in_game_route_query-7fac93716e874d0e91f9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:avenue-lane-01-a>avenue-lane-01-b; entry: avenue-lane-01-a; exit: avenue-lane-01-b.

No observation recorded.

<a id="case-in_game_route_query-77b4fb7b0dfbe4ee6d7d"></a>

**90° CCW: unverified** — `in_game_route_query-77b4fb7b0dfbe4ee6d7d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:avenue-lane-01-a>avenue-lane-01-b; entry: avenue-lane-01-a; exit: avenue-lane-01-b.

No observation recorded.

<a id="case-in_game_route_query-a14404d3c753772da4d6"></a>

**180° CCW: unverified** — `in_game_route_query-a14404d3c753772da4d6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:avenue-lane-01-a>avenue-lane-01-b; entry: avenue-lane-01-a; exit: avenue-lane-01-b.

No observation recorded.

<a id="case-in_game_route_query-1a9aa27f2500bca1c57c"></a>

**270° CCW: unverified** — `in_game_route_query-1a9aa27f2500bca1c57c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:avenue-lane-01-a>avenue-lane-01-b; entry: avenue-lane-01-a; exit: avenue-lane-01-b.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:avenue-lane-02-a>avenue-lane-02-b; entry: avenue-lane-02-a; exit: avenue-lane-02-b</summary>

<a id="case-in_game_route_query-ab54caa6dd51363531a9"></a>

**0° CCW: unverified** — `in_game_route_query-ab54caa6dd51363531a9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:avenue-lane-02-a>avenue-lane-02-b; entry: avenue-lane-02-a; exit: avenue-lane-02-b.

No observation recorded.

<a id="case-in_game_route_query-51f9f4f6e8b84c6ed5ec"></a>

**90° CCW: unverified** — `in_game_route_query-51f9f4f6e8b84c6ed5ec`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:avenue-lane-02-a>avenue-lane-02-b; entry: avenue-lane-02-a; exit: avenue-lane-02-b.

No observation recorded.

<a id="case-in_game_route_query-a1246218987bf69cdd8b"></a>

**180° CCW: unverified** — `in_game_route_query-a1246218987bf69cdd8b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:avenue-lane-02-a>avenue-lane-02-b; entry: avenue-lane-02-a; exit: avenue-lane-02-b.

No observation recorded.

<a id="case-in_game_route_query-a9c2d64641fbd2813b28"></a>

**270° CCW: unverified** — `in_game_route_query-a9c2d64641fbd2813b28`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:avenue-lane-02-a>avenue-lane-02-b; entry: avenue-lane-02-a; exit: avenue-lane-02-b.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:upper-lane-01-a>upper-lane-01-b; entry: upper-lane-01-a; exit: upper-lane-01-b</summary>

<a id="case-in_game_route_query-431853dbe37083269c0f"></a>

**0° CCW: unverified** — `in_game_route_query-431853dbe37083269c0f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-a>upper-lane-01-b; entry: upper-lane-01-a; exit: upper-lane-01-b.

No observation recorded.

<a id="case-in_game_route_query-3564afda2c0ce75c88ac"></a>

**90° CCW: unverified** — `in_game_route_query-3564afda2c0ce75c88ac`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-a>upper-lane-01-b; entry: upper-lane-01-a; exit: upper-lane-01-b.

No observation recorded.

<a id="case-in_game_route_query-7070bd5f80862d6e818d"></a>

**180° CCW: unverified** — `in_game_route_query-7070bd5f80862d6e818d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-a>upper-lane-01-b; entry: upper-lane-01-a; exit: upper-lane-01-b.

No observation recorded.

<a id="case-in_game_route_query-2fdf1bfc58e0f8245797"></a>

**270° CCW: unverified** — `in_game_route_query-2fdf1bfc58e0f8245797`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-a>upper-lane-01-b; entry: upper-lane-01-a; exit: upper-lane-01-b.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:upper-lane-02-a>upper-lane-02-b; entry: upper-lane-02-a; exit: upper-lane-02-b</summary>

<a id="case-in_game_route_query-7e3337d5aff0cb3b9dfd"></a>

**0° CCW: unverified** — `in_game_route_query-7e3337d5aff0cb3b9dfd`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-a>upper-lane-02-b; entry: upper-lane-02-a; exit: upper-lane-02-b.

No observation recorded.

<a id="case-in_game_route_query-c989abac74362507eb55"></a>

**90° CCW: unverified** — `in_game_route_query-c989abac74362507eb55`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-a>upper-lane-02-b; entry: upper-lane-02-a; exit: upper-lane-02-b.

No observation recorded.

<a id="case-in_game_route_query-fe2d9e816845210c6ab8"></a>

**180° CCW: unverified** — `in_game_route_query-fe2d9e816845210c6ab8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-a>upper-lane-02-b; entry: upper-lane-02-a; exit: upper-lane-02-b.

No observation recorded.

<a id="case-in_game_route_query-b1355ac46beb861c388e"></a>

**270° CCW: unverified** — `in_game_route_query-b1355ac46beb861c388e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-a>upper-lane-02-b; entry: upper-lane-02-a; exit: upper-lane-02-b.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:avenue-lane-03-a>avenue-lane-03-b; entry: avenue-lane-03-a; exit: avenue-lane-03-b</summary>

<a id="case-in_game_route_query-fb3d0acb042014de9c03"></a>

**0° CCW: unverified** — `in_game_route_query-fb3d0acb042014de9c03`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:avenue-lane-03-a>avenue-lane-03-b; entry: avenue-lane-03-a; exit: avenue-lane-03-b.

No observation recorded.

<a id="case-in_game_route_query-15c823f1992f12a339d8"></a>

**90° CCW: unverified** — `in_game_route_query-15c823f1992f12a339d8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:avenue-lane-03-a>avenue-lane-03-b; entry: avenue-lane-03-a; exit: avenue-lane-03-b.

No observation recorded.

<a id="case-in_game_route_query-ecb32f3b74b6759934db"></a>

**180° CCW: unverified** — `in_game_route_query-ecb32f3b74b6759934db`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:avenue-lane-03-a>avenue-lane-03-b; entry: avenue-lane-03-a; exit: avenue-lane-03-b.

No observation recorded.

<a id="case-in_game_route_query-aec3b93747a03e5b908f"></a>

**270° CCW: unverified** — `in_game_route_query-aec3b93747a03e5b908f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:avenue-lane-03-a>avenue-lane-03-b; entry: avenue-lane-03-a; exit: avenue-lane-03-b.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:lower-lane-01-a>lower-lane-01-b; entry: lower-lane-01-a; exit: lower-lane-01-b</summary>

<a id="case-in_game_route_query-15d0ef6416e43a23e26c"></a>

**0° CCW: unverified** — `in_game_route_query-15d0ef6416e43a23e26c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-a>lower-lane-01-b; entry: lower-lane-01-a; exit: lower-lane-01-b.

No observation recorded.

<a id="case-in_game_route_query-c70c77bc357520c826e0"></a>

**90° CCW: unverified** — `in_game_route_query-c70c77bc357520c826e0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-a>lower-lane-01-b; entry: lower-lane-01-a; exit: lower-lane-01-b.

No observation recorded.

<a id="case-in_game_route_query-c7c761820f5a0e38e17c"></a>

**180° CCW: unverified** — `in_game_route_query-c7c761820f5a0e38e17c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-a>lower-lane-01-b; entry: lower-lane-01-a; exit: lower-lane-01-b.

No observation recorded.

<a id="case-in_game_route_query-54aa42276e920693d789"></a>

**270° CCW: unverified** — `in_game_route_query-54aa42276e920693d789`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-a>lower-lane-01-b; entry: lower-lane-01-a; exit: lower-lane-01-b.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:avenue-lane-04-a>avenue-lane-04-b; entry: avenue-lane-04-a; exit: avenue-lane-04-b</summary>

<a id="case-in_game_route_query-422e0ad896eed7747753"></a>

**0° CCW: unverified** — `in_game_route_query-422e0ad896eed7747753`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:avenue-lane-04-a>avenue-lane-04-b; entry: avenue-lane-04-a; exit: avenue-lane-04-b.

No observation recorded.

<a id="case-in_game_route_query-a3ec9473ded339c2b0e8"></a>

**90° CCW: unverified** — `in_game_route_query-a3ec9473ded339c2b0e8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:avenue-lane-04-a>avenue-lane-04-b; entry: avenue-lane-04-a; exit: avenue-lane-04-b.

No observation recorded.

<a id="case-in_game_route_query-fdc2dfbc6187bd35df37"></a>

**180° CCW: unverified** — `in_game_route_query-fdc2dfbc6187bd35df37`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:avenue-lane-04-a>avenue-lane-04-b; entry: avenue-lane-04-a; exit: avenue-lane-04-b.

No observation recorded.

<a id="case-in_game_route_query-4248833c54dbd4e82f04"></a>

**270° CCW: unverified** — `in_game_route_query-4248833c54dbd4e82f04`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:avenue-lane-04-a>avenue-lane-04-b; entry: avenue-lane-04-a; exit: avenue-lane-04-b.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:lower-lane-02-a>lower-lane-02-b; entry: lower-lane-02-a; exit: lower-lane-02-b</summary>

<a id="case-in_game_route_query-72283520a3a97713da28"></a>

**0° CCW: unverified** — `in_game_route_query-72283520a3a97713da28`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-a>lower-lane-02-b; entry: lower-lane-02-a; exit: lower-lane-02-b.

No observation recorded.

<a id="case-in_game_route_query-c53b1e8898c2baed66ae"></a>

**90° CCW: unverified** — `in_game_route_query-c53b1e8898c2baed66ae`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-a>lower-lane-02-b; entry: lower-lane-02-a; exit: lower-lane-02-b.

No observation recorded.

<a id="case-in_game_route_query-4a5079c9bd3fe1c81349"></a>

**180° CCW: unverified** — `in_game_route_query-4a5079c9bd3fe1c81349`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-a>lower-lane-02-b; entry: lower-lane-02-a; exit: lower-lane-02-b.

No observation recorded.

<a id="case-in_game_route_query-3d5a46bf2062e6d154df"></a>

**270° CCW: unverified** — `in_game_route_query-3d5a46bf2062e6d154df`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-a>lower-lane-02-b; entry: lower-lane-02-a; exit: lower-lane-02-b.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 32 cases; unverified: 32</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:avenue-lane-01-a>avenue-lane-01-b; entry: avenue-lane-01-a; exit: avenue-lane-01-b | — | <a href="#case-in_game_visible_travel-7fac93716e874d0e91f9">[ ] unverified</a> | <a href="#case-in_game_visible_travel-77b4fb7b0dfbe4ee6d7d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a14404d3c753772da4d6">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1a9aa27f2500bca1c57c">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:avenue-lane-02-a>avenue-lane-02-b; entry: avenue-lane-02-a; exit: avenue-lane-02-b | — | <a href="#case-in_game_visible_travel-ab54caa6dd51363531a9">[ ] unverified</a> | <a href="#case-in_game_visible_travel-51f9f4f6e8b84c6ed5ec">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a1246218987bf69cdd8b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a9c2d64641fbd2813b28">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:upper-lane-01-a>upper-lane-01-b; entry: upper-lane-01-a; exit: upper-lane-01-b | — | <a href="#case-in_game_visible_travel-431853dbe37083269c0f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-3564afda2c0ce75c88ac">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7070bd5f80862d6e818d">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2fdf1bfc58e0f8245797">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:upper-lane-02-a>upper-lane-02-b; entry: upper-lane-02-a; exit: upper-lane-02-b | — | <a href="#case-in_game_visible_travel-7e3337d5aff0cb3b9dfd">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c989abac74362507eb55">[ ] unverified</a> | <a href="#case-in_game_visible_travel-fe2d9e816845210c6ab8">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b1355ac46beb861c388e">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:avenue-lane-03-a>avenue-lane-03-b; entry: avenue-lane-03-a; exit: avenue-lane-03-b | — | <a href="#case-in_game_visible_travel-fb3d0acb042014de9c03">[ ] unverified</a> | <a href="#case-in_game_visible_travel-15c823f1992f12a339d8">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ecb32f3b74b6759934db">[ ] unverified</a> | <a href="#case-in_game_visible_travel-aec3b93747a03e5b908f">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:lower-lane-01-a>lower-lane-01-b; entry: lower-lane-01-a; exit: lower-lane-01-b | — | <a href="#case-in_game_visible_travel-15d0ef6416e43a23e26c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c70c77bc357520c826e0">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c7c761820f5a0e38e17c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-54aa42276e920693d789">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:avenue-lane-04-a>avenue-lane-04-b; entry: avenue-lane-04-a; exit: avenue-lane-04-b | — | <a href="#case-in_game_visible_travel-422e0ad896eed7747753">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a3ec9473ded339c2b0e8">[ ] unverified</a> | <a href="#case-in_game_visible_travel-fdc2dfbc6187bd35df37">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4248833c54dbd4e82f04">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:lower-lane-02-a>lower-lane-02-b; entry: lower-lane-02-a; exit: lower-lane-02-b | — | <a href="#case-in_game_visible_travel-72283520a3a97713da28">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c53b1e8898c2baed66ae">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4a5079c9bd3fe1c81349">[ ] unverified</a> | <a href="#case-in_game_visible_travel-3d5a46bf2062e6d154df">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:avenue-lane-01-a>avenue-lane-01-b; entry: avenue-lane-01-a; exit: avenue-lane-01-b</summary>

<a id="case-in_game_visible_travel-7fac93716e874d0e91f9"></a>

**0° CCW: unverified** — `in_game_visible_travel-7fac93716e874d0e91f9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:avenue-lane-01-a>avenue-lane-01-b; entry: avenue-lane-01-a; exit: avenue-lane-01-b.

No observation recorded.

<a id="case-in_game_visible_travel-77b4fb7b0dfbe4ee6d7d"></a>

**90° CCW: unverified** — `in_game_visible_travel-77b4fb7b0dfbe4ee6d7d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:avenue-lane-01-a>avenue-lane-01-b; entry: avenue-lane-01-a; exit: avenue-lane-01-b.

No observation recorded.

<a id="case-in_game_visible_travel-a14404d3c753772da4d6"></a>

**180° CCW: unverified** — `in_game_visible_travel-a14404d3c753772da4d6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:avenue-lane-01-a>avenue-lane-01-b; entry: avenue-lane-01-a; exit: avenue-lane-01-b.

No observation recorded.

<a id="case-in_game_visible_travel-1a9aa27f2500bca1c57c"></a>

**270° CCW: unverified** — `in_game_visible_travel-1a9aa27f2500bca1c57c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:avenue-lane-01-a>avenue-lane-01-b; entry: avenue-lane-01-a; exit: avenue-lane-01-b.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:avenue-lane-02-a>avenue-lane-02-b; entry: avenue-lane-02-a; exit: avenue-lane-02-b</summary>

<a id="case-in_game_visible_travel-ab54caa6dd51363531a9"></a>

**0° CCW: unverified** — `in_game_visible_travel-ab54caa6dd51363531a9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:avenue-lane-02-a>avenue-lane-02-b; entry: avenue-lane-02-a; exit: avenue-lane-02-b.

No observation recorded.

<a id="case-in_game_visible_travel-51f9f4f6e8b84c6ed5ec"></a>

**90° CCW: unverified** — `in_game_visible_travel-51f9f4f6e8b84c6ed5ec`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:avenue-lane-02-a>avenue-lane-02-b; entry: avenue-lane-02-a; exit: avenue-lane-02-b.

No observation recorded.

<a id="case-in_game_visible_travel-a1246218987bf69cdd8b"></a>

**180° CCW: unverified** — `in_game_visible_travel-a1246218987bf69cdd8b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:avenue-lane-02-a>avenue-lane-02-b; entry: avenue-lane-02-a; exit: avenue-lane-02-b.

No observation recorded.

<a id="case-in_game_visible_travel-a9c2d64641fbd2813b28"></a>

**270° CCW: unverified** — `in_game_visible_travel-a9c2d64641fbd2813b28`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:avenue-lane-02-a>avenue-lane-02-b; entry: avenue-lane-02-a; exit: avenue-lane-02-b.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:upper-lane-01-a>upper-lane-01-b; entry: upper-lane-01-a; exit: upper-lane-01-b</summary>

<a id="case-in_game_visible_travel-431853dbe37083269c0f"></a>

**0° CCW: unverified** — `in_game_visible_travel-431853dbe37083269c0f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-a>upper-lane-01-b; entry: upper-lane-01-a; exit: upper-lane-01-b.

No observation recorded.

<a id="case-in_game_visible_travel-3564afda2c0ce75c88ac"></a>

**90° CCW: unverified** — `in_game_visible_travel-3564afda2c0ce75c88ac`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-a>upper-lane-01-b; entry: upper-lane-01-a; exit: upper-lane-01-b.

No observation recorded.

<a id="case-in_game_visible_travel-7070bd5f80862d6e818d"></a>

**180° CCW: unverified** — `in_game_visible_travel-7070bd5f80862d6e818d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-a>upper-lane-01-b; entry: upper-lane-01-a; exit: upper-lane-01-b.

No observation recorded.

<a id="case-in_game_visible_travel-2fdf1bfc58e0f8245797"></a>

**270° CCW: unverified** — `in_game_visible_travel-2fdf1bfc58e0f8245797`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-01-a>upper-lane-01-b; entry: upper-lane-01-a; exit: upper-lane-01-b.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:upper-lane-02-a>upper-lane-02-b; entry: upper-lane-02-a; exit: upper-lane-02-b</summary>

<a id="case-in_game_visible_travel-7e3337d5aff0cb3b9dfd"></a>

**0° CCW: unverified** — `in_game_visible_travel-7e3337d5aff0cb3b9dfd`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-a>upper-lane-02-b; entry: upper-lane-02-a; exit: upper-lane-02-b.

No observation recorded.

<a id="case-in_game_visible_travel-c989abac74362507eb55"></a>

**90° CCW: unverified** — `in_game_visible_travel-c989abac74362507eb55`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-a>upper-lane-02-b; entry: upper-lane-02-a; exit: upper-lane-02-b.

No observation recorded.

<a id="case-in_game_visible_travel-fe2d9e816845210c6ab8"></a>

**180° CCW: unverified** — `in_game_visible_travel-fe2d9e816845210c6ab8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-a>upper-lane-02-b; entry: upper-lane-02-a; exit: upper-lane-02-b.

No observation recorded.

<a id="case-in_game_visible_travel-b1355ac46beb861c388e"></a>

**270° CCW: unverified** — `in_game_visible_travel-b1355ac46beb861c388e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:upper-lane-02-a>upper-lane-02-b; entry: upper-lane-02-a; exit: upper-lane-02-b.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:avenue-lane-03-a>avenue-lane-03-b; entry: avenue-lane-03-a; exit: avenue-lane-03-b</summary>

<a id="case-in_game_visible_travel-fb3d0acb042014de9c03"></a>

**0° CCW: unverified** — `in_game_visible_travel-fb3d0acb042014de9c03`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:avenue-lane-03-a>avenue-lane-03-b; entry: avenue-lane-03-a; exit: avenue-lane-03-b.

No observation recorded.

<a id="case-in_game_visible_travel-15c823f1992f12a339d8"></a>

**90° CCW: unverified** — `in_game_visible_travel-15c823f1992f12a339d8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:avenue-lane-03-a>avenue-lane-03-b; entry: avenue-lane-03-a; exit: avenue-lane-03-b.

No observation recorded.

<a id="case-in_game_visible_travel-ecb32f3b74b6759934db"></a>

**180° CCW: unverified** — `in_game_visible_travel-ecb32f3b74b6759934db`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:avenue-lane-03-a>avenue-lane-03-b; entry: avenue-lane-03-a; exit: avenue-lane-03-b.

No observation recorded.

<a id="case-in_game_visible_travel-aec3b93747a03e5b908f"></a>

**270° CCW: unverified** — `in_game_visible_travel-aec3b93747a03e5b908f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:avenue-lane-03-a>avenue-lane-03-b; entry: avenue-lane-03-a; exit: avenue-lane-03-b.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:lower-lane-01-a>lower-lane-01-b; entry: lower-lane-01-a; exit: lower-lane-01-b</summary>

<a id="case-in_game_visible_travel-15d0ef6416e43a23e26c"></a>

**0° CCW: unverified** — `in_game_visible_travel-15d0ef6416e43a23e26c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-a>lower-lane-01-b; entry: lower-lane-01-a; exit: lower-lane-01-b.

No observation recorded.

<a id="case-in_game_visible_travel-c70c77bc357520c826e0"></a>

**90° CCW: unverified** — `in_game_visible_travel-c70c77bc357520c826e0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-a>lower-lane-01-b; entry: lower-lane-01-a; exit: lower-lane-01-b.

No observation recorded.

<a id="case-in_game_visible_travel-c7c761820f5a0e38e17c"></a>

**180° CCW: unverified** — `in_game_visible_travel-c7c761820f5a0e38e17c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-a>lower-lane-01-b; entry: lower-lane-01-a; exit: lower-lane-01-b.

No observation recorded.

<a id="case-in_game_visible_travel-54aa42276e920693d789"></a>

**270° CCW: unverified** — `in_game_visible_travel-54aa42276e920693d789`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-01-a>lower-lane-01-b; entry: lower-lane-01-a; exit: lower-lane-01-b.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:avenue-lane-04-a>avenue-lane-04-b; entry: avenue-lane-04-a; exit: avenue-lane-04-b</summary>

<a id="case-in_game_visible_travel-422e0ad896eed7747753"></a>

**0° CCW: unverified** — `in_game_visible_travel-422e0ad896eed7747753`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:avenue-lane-04-a>avenue-lane-04-b; entry: avenue-lane-04-a; exit: avenue-lane-04-b.

No observation recorded.

<a id="case-in_game_visible_travel-a3ec9473ded339c2b0e8"></a>

**90° CCW: unverified** — `in_game_visible_travel-a3ec9473ded339c2b0e8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:avenue-lane-04-a>avenue-lane-04-b; entry: avenue-lane-04-a; exit: avenue-lane-04-b.

No observation recorded.

<a id="case-in_game_visible_travel-fdc2dfbc6187bd35df37"></a>

**180° CCW: unverified** — `in_game_visible_travel-fdc2dfbc6187bd35df37`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:avenue-lane-04-a>avenue-lane-04-b; entry: avenue-lane-04-a; exit: avenue-lane-04-b.

No observation recorded.

<a id="case-in_game_visible_travel-4248833c54dbd4e82f04"></a>

**270° CCW: unverified** — `in_game_visible_travel-4248833c54dbd4e82f04`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:avenue-lane-04-a>avenue-lane-04-b; entry: avenue-lane-04-a; exit: avenue-lane-04-b.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:lower-lane-02-a>lower-lane-02-b; entry: lower-lane-02-a; exit: lower-lane-02-b</summary>

<a id="case-in_game_visible_travel-72283520a3a97713da28"></a>

**0° CCW: unverified** — `in_game_visible_travel-72283520a3a97713da28`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-a>lower-lane-02-b; entry: lower-lane-02-a; exit: lower-lane-02-b.

No observation recorded.

<a id="case-in_game_visible_travel-c53b1e8898c2baed66ae"></a>

**90° CCW: unverified** — `in_game_visible_travel-c53b1e8898c2baed66ae`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-a>lower-lane-02-b; entry: lower-lane-02-a; exit: lower-lane-02-b.

No observation recorded.

<a id="case-in_game_visible_travel-4a5079c9bd3fe1c81349"></a>

**180° CCW: unverified** — `in_game_visible_travel-4a5079c9bd3fe1c81349`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-a>lower-lane-02-b; entry: lower-lane-02-a; exit: lower-lane-02-b.

No observation recorded.

<a id="case-in_game_visible_travel-3d5a46bf2062e6d154df"></a>

**270° CCW: unverified** — `in_game_visible_travel-3d5a46bf2062e6d154df`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:lower-lane-02-a>lower-lane-02-b; entry: lower-lane-02-a; exit: lower-lane-02-b.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — pedestrian — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: pedestrian; role: primary; journey: 2:avenue-walkway-01-a>avenue-walkway-01-b; entry: avenue-walkway-01-a; exit: avenue-walkway-01-b | — | <a href="#case-in_game_route_query-6f6c04720a56b410522a">[ ] unverified</a> | <a href="#case-in_game_route_query-6a65b1344e8a923a7058">[ ] unverified</a> | <a href="#case-in_game_route_query-1eb6ef6263510dc9face">[ ] unverified</a> | <a href="#case-in_game_route_query-8709c36f73c9a07f7c85">[ ] unverified</a> |
| **Route Query**<br>Service: pedestrian; role: primary; journey: 2:avenue-walkway-02-a>avenue-walkway-02-b; entry: avenue-walkway-02-a; exit: avenue-walkway-02-b | — | <a href="#case-in_game_route_query-f2fb22064640d44573fc">[ ] unverified</a> | <a href="#case-in_game_route_query-46297a2db020a5af253b">[ ] unverified</a> | <a href="#case-in_game_route_query-18b5fd0b855eaebc6d8e">[ ] unverified</a> | <a href="#case-in_game_route_query-f61e7eb303d6712983da">[ ] unverified</a> |


<details>
<summary>Route Query — Service: pedestrian; role: primary; journey: 2:avenue-walkway-01-a>avenue-walkway-01-b; entry: avenue-walkway-01-a; exit: avenue-walkway-01-b</summary>

<a id="case-in_game_route_query-6f6c04720a56b410522a"></a>

**0° CCW: unverified** — `in_game_route_query-6f6c04720a56b410522a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:avenue-walkway-01-a>avenue-walkway-01-b; entry: avenue-walkway-01-a; exit: avenue-walkway-01-b.

No observation recorded.

<a id="case-in_game_route_query-6a65b1344e8a923a7058"></a>

**90° CCW: unverified** — `in_game_route_query-6a65b1344e8a923a7058`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:avenue-walkway-01-a>avenue-walkway-01-b; entry: avenue-walkway-01-a; exit: avenue-walkway-01-b.

No observation recorded.

<a id="case-in_game_route_query-1eb6ef6263510dc9face"></a>

**180° CCW: unverified** — `in_game_route_query-1eb6ef6263510dc9face`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:avenue-walkway-01-a>avenue-walkway-01-b; entry: avenue-walkway-01-a; exit: avenue-walkway-01-b.

No observation recorded.

<a id="case-in_game_route_query-8709c36f73c9a07f7c85"></a>

**270° CCW: unverified** — `in_game_route_query-8709c36f73c9a07f7c85`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:avenue-walkway-01-a>avenue-walkway-01-b; entry: avenue-walkway-01-a; exit: avenue-walkway-01-b.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: pedestrian; role: primary; journey: 2:avenue-walkway-02-a>avenue-walkway-02-b; entry: avenue-walkway-02-a; exit: avenue-walkway-02-b</summary>

<a id="case-in_game_route_query-f2fb22064640d44573fc"></a>

**0° CCW: unverified** — `in_game_route_query-f2fb22064640d44573fc`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:avenue-walkway-02-a>avenue-walkway-02-b; entry: avenue-walkway-02-a; exit: avenue-walkway-02-b.

No observation recorded.

<a id="case-in_game_route_query-46297a2db020a5af253b"></a>

**90° CCW: unverified** — `in_game_route_query-46297a2db020a5af253b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:avenue-walkway-02-a>avenue-walkway-02-b; entry: avenue-walkway-02-a; exit: avenue-walkway-02-b.

No observation recorded.

<a id="case-in_game_route_query-18b5fd0b855eaebc6d8e"></a>

**180° CCW: unverified** — `in_game_route_query-18b5fd0b855eaebc6d8e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:avenue-walkway-02-a>avenue-walkway-02-b; entry: avenue-walkway-02-a; exit: avenue-walkway-02-b.

No observation recorded.

<a id="case-in_game_route_query-f61e7eb303d6712983da"></a>

**270° CCW: unverified** — `in_game_route_query-f61e7eb303d6712983da`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:avenue-walkway-02-a>avenue-walkway-02-b; entry: avenue-walkway-02-a; exit: avenue-walkway-02-b.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — pedestrian — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: pedestrian; role: primary; journey: 2:avenue-walkway-01-a>avenue-walkway-01-b; entry: avenue-walkway-01-a; exit: avenue-walkway-01-b | — | <a href="#case-in_game_visible_travel-6f6c04720a56b410522a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6a65b1344e8a923a7058">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1eb6ef6263510dc9face">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8709c36f73c9a07f7c85">[ ] unverified</a> |
| **Visible travel**<br>Service: pedestrian; role: primary; journey: 2:avenue-walkway-02-a>avenue-walkway-02-b; entry: avenue-walkway-02-a; exit: avenue-walkway-02-b | — | <a href="#case-in_game_visible_travel-f2fb22064640d44573fc">[ ] unverified</a> | <a href="#case-in_game_visible_travel-46297a2db020a5af253b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-18b5fd0b855eaebc6d8e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f61e7eb303d6712983da">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: pedestrian; role: primary; journey: 2:avenue-walkway-01-a>avenue-walkway-01-b; entry: avenue-walkway-01-a; exit: avenue-walkway-01-b</summary>

<a id="case-in_game_visible_travel-6f6c04720a56b410522a"></a>

**0° CCW: unverified** — `in_game_visible_travel-6f6c04720a56b410522a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:avenue-walkway-01-a>avenue-walkway-01-b; entry: avenue-walkway-01-a; exit: avenue-walkway-01-b.

No observation recorded.

<a id="case-in_game_visible_travel-6a65b1344e8a923a7058"></a>

**90° CCW: unverified** — `in_game_visible_travel-6a65b1344e8a923a7058`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:avenue-walkway-01-a>avenue-walkway-01-b; entry: avenue-walkway-01-a; exit: avenue-walkway-01-b.

No observation recorded.

<a id="case-in_game_visible_travel-1eb6ef6263510dc9face"></a>

**180° CCW: unverified** — `in_game_visible_travel-1eb6ef6263510dc9face`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:avenue-walkway-01-a>avenue-walkway-01-b; entry: avenue-walkway-01-a; exit: avenue-walkway-01-b.

No observation recorded.

<a id="case-in_game_visible_travel-8709c36f73c9a07f7c85"></a>

**270° CCW: unverified** — `in_game_visible_travel-8709c36f73c9a07f7c85`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:avenue-walkway-01-a>avenue-walkway-01-b; entry: avenue-walkway-01-a; exit: avenue-walkway-01-b.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: pedestrian; role: primary; journey: 2:avenue-walkway-02-a>avenue-walkway-02-b; entry: avenue-walkway-02-a; exit: avenue-walkway-02-b</summary>

<a id="case-in_game_visible_travel-f2fb22064640d44573fc"></a>

**0° CCW: unverified** — `in_game_visible_travel-f2fb22064640d44573fc`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:avenue-walkway-02-a>avenue-walkway-02-b; entry: avenue-walkway-02-a; exit: avenue-walkway-02-b.

No observation recorded.

<a id="case-in_game_visible_travel-46297a2db020a5af253b"></a>

**90° CCW: unverified** — `in_game_visible_travel-46297a2db020a5af253b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:avenue-walkway-02-a>avenue-walkway-02-b; entry: avenue-walkway-02-a; exit: avenue-walkway-02-b.

No observation recorded.

<a id="case-in_game_visible_travel-18b5fd0b855eaebc6d8e"></a>

**180° CCW: unverified** — `in_game_visible_travel-18b5fd0b855eaebc6d8e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:avenue-walkway-02-a>avenue-walkway-02-b; entry: avenue-walkway-02-a; exit: avenue-walkway-02-b.

No observation recorded.

<a id="case-in_game_visible_travel-f61e7eb303d6712983da"></a>

**270° CCW: unverified** — `in_game_visible_travel-f61e7eb303d6712983da`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:avenue-walkway-02-a>avenue-walkway-02-b; entry: avenue-walkway-02-a; exit: avenue-walkway-02-b.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 224 cases; unverified: 224</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: avenue-lane-01-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fc72579dde2aefa2879b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-30883e76539a725a3799">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-962c402a4364227f2e32">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-51e10996d7398fc32d87">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-lane-01-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-541c1cf2af0f1df611db">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d9465930775addbcddec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-906fde0cdef35f89bbd3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f64cb67ee7bb63f918fc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-lane-01-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1c9e064218962a77ac1f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2ca2154cbd577ca55bfa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-afa6a01636cf950a3841">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-84789f6d1abdd1a1e403">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-lane-01-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0cb69d67ec7351cfb040">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-913fa8ce04bbd82147a0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d3b9e01548806e3db857">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-38646760eaf2784887fd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-lane-01-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6af4aa1c7bc8f30ea718">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-58dc1efdfc9e7eb357eb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3a8da2a7acfbbe32ccd2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a836692cda5c49710872">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-lane-01-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-237a7c52e55d75964fd0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e85f4642d90146885e02">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ead8aaf0ebcb3a5e26a5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1ac0c1651e3ec5b8fdfd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-lane-01-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d858101c88744f8d539a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-626aaa309122ec6c0883">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6c119cd41bd389a76c2f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e6a20e7c500fc147d39e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-lane-02-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ced02aea377b0c611c1e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3f4e183352c8dffdde29">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-81ae6ce8208857cf2372">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a5b27a91079596b7892c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-lane-02-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4617b0e6726ec6b31efe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-177f37680c87378f363f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-06226cc0cbb847b98ecf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-93fcb37bdaedf0b078c9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-lane-02-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-31b0067c35b73f9df3c2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f8bd2ba59179559614e8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-39feda91c89038842beb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cacc1cd6b9f094619d8d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-lane-02-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e9757a4d61af26cf614e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a978a9d55663d02ec95b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fa0fa1fc3ff723bc889f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-83711bc64a04378d61ce">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-lane-02-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-74e8da79d6f02a39853a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-21e911fd0b63d27e9606">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6a657873a78df77259ae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f2f61fa2f6efa3a7cb1d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-lane-02-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-45b63d24170f5e29763e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-16e35b3b2e6e64c9079c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-892f41ddee4af98e84c3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ab18e6b76bf975723e4b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-lane-02-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c896452ccf3753977692">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ef4f0223b9e4582657a8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0d5ea0551459ac52b385">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-34a394ca54de59d0b7fa">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-01-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-835ad6f4fc32857fd1b2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ce180553e57cdad05e02">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-007a5612ce7ca717bba9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ebdef24251145b6b3550">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-01-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-20a6baabc0cfc3741d24">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a9db056f835ef0b3f96d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-77d6aab25f967dd6d1e7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-25149f56c12ff61b725b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-01-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-495a7dea8a6172418299">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bba054282f8b726f2ccb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-397a7a4b42baabb71110">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e30dacf7c64f14d6875b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-01-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-73f5b322373f1b269f30">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2d0e6b61cf9a1f088c8d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-15c32e6a7e4b5daee71e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9d1319d11c0c16e9deff">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-01-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ef99d8e3617bf2c03c5d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8d9b0b9fb9e48aad81de">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-960d1321dd5d9a45daa9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fd23953f92c14b2ab2e5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-01-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0a023fa7110b084086ac">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5792281ae01e2483dcad">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5c0271acd5d0f1ac890f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-afb4dc30a840500dc648">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-01-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-67a2e40ece9dbe57f5a9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c028a0db64a3ea28788c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a6cf81dd578f93c579aa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d22f1c4ce0b355a8ccb8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-02-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8c021376272e692b189a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-93b45b7c70c06f56a033">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-02e3b347c004ba1b898c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-89ff5b14357d594df6c1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-02-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-abc9ecd0a0b3321cf41b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-05f842119bea3b6f7f33">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a4ccca3ca8cd0c86a343">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-709799dd070968320f1b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-02-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b273531ee22d95fc54f0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-565b07c0b3d816650a82">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-244d39d9897293baef31">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7da9c017a04be157f7da">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-02-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-20ef72fc1859b18ac1d7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-979615a0cfdc351f2c86">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4bf9c945c3ad7e17947c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-75680da1c9d473c7d881">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-02-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3e847175e4fce6dc23bb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-070807a32f848dc8c771">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5974c3f9158b5c294513">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9d44253b8b65e906476d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-02-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2530a99ed0f52dc9226e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e0fd86801734ef3b6d27">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5ff1292b50b2e6375fd0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-16ae50a45bd30f03afb7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-02-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7d71562922c9ebfe4c20">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-151b1b3f29acfb1c4e8a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8c3a451546fc919717ad">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6b00eeb6de8ff25d6d51">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-lane-03-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7fcf8f5411ab049473b4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-82ed16639daaa874b9b8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8976845ce9a7b0641a07">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-de6aa234b0c94b1f8603">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-lane-03-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-af7cc0b17b6423f13560">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ec0e15498d822d1991c9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5f183336f26d3f11e1a4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-714e5ba61abb93a6d4b0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-lane-03-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6e045a6735d38ca0e3e3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b40f403356261945b925">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-28e607bcffca678f17e8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-238e998a5afff70c3ba6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-lane-03-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0057e2c925627948d9ae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ba078e015316d542f699">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ec6615b2065a419ad87d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-95bcf1e230c5a4bb9b42">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-lane-03-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-316a918622f2a7e61037">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cabbc7acae5fd363141c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-671a68b99b09dde1ccb3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0a437e09546335977140">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-lane-03-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1ab8caba3036436f0069">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3ab60539d7f1c110c6ec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-89d1eb5c7ef403e016aa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-541e0b39c7cb084f78fb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-lane-03-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-95466259d9dedd2815a9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-852dc5105ae911f6a29c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cbfcbbe610075994b7d7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2bcce4199f3b002b56b5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-01-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-375402fea370ac5a4c71">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f5eefb26d26251192494">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c914a5e91bc43afd25e9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-834f3e1f8b8d22c2df45">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-01-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c88dc5dce3e3b309c33e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c0690f6ff4726eb22bfd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-78c81c6f0d46fcaef2f4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-05f306e7445be4930848">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-01-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-39d848faf1b1742d45d8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0b101ff096f1529d49bc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e81be8a957b901d4de32">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f8794f12ae9f00942755">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-01-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1ef9c9ce61d57f164f80">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ce4819e3209255e60874">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5a8ca07d1afd234a48ff">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1d5c6d1164966ef0804d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-01-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5367206dd0bd2ef41b24">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4a57575b9de8f06b22fb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-34b96e24a11d104d16e1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ed82a3254271bff55d39">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-01-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3a49a67dbacd5fe2d555">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-851f8309b570f25dc27c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e5e41aea35ec55ed4df8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4b09caab6be9692128fb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-01-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7f96d31a052f4d3ec346">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-75f4f6c2871706bb8c4b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b1960772a86356937122">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d7f9894cd89d05a0ad86">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-lane-04-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d2999e066bd0777906d7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-571373293976e7928db7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c4e04b97c301e2b7030e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-92b3841c7c3bc97c415d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-lane-04-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-db7c52f1697b7179af74">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9df2b808975743edfe5c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-20d845d5666bd015f72f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b07d4f11b9a93f5c315c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-lane-04-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3025a61c0f56212b6246">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4e095e8ed7a4398d4a6e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ea7b89a6f0ecdfc698d5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4286052ffff351bbcfee">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-lane-04-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c4d4a57d032fe3a10394">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cac99c8a082cf315fa8d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7406d568a1f37f514116">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-10d8e74396b994b0fb26">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-lane-04-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-06fbf5296e640078fcef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ef319f6c4607a9ca686e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-88d59b551a5fbae6df46">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cb0f839efa9a32ac0c58">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-lane-04-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b8d21c361afde81b0a8b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-725a57ecff294e9e8162">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f74ee54a2a3926fcb6a7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-15cc90c318e7036b0f9c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-lane-04-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-408da1de5a5b9dfa51a1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d78f33aee8e550b785dc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-926844256dc98237bb05">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bce61ce0e966f9923765">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-02-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6904f59b896dcd5d66f1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f2953ef6115da8c850ea">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-01e5b968d65b07b871c2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-28b9e2da67295f33f849">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-02-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-79d97e48cd6313303f51">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1018d96c1080406042e7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f8b79da7b6b867ba1440">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-07b1449c9c9f96439763">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-02-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cbb22ed4b6230263b059">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-acfc0cdfe5f4d430f8f0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b5ee5b2658e7e8f773ef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4ca82929b3bd8ea4cde9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-02-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bca56d96a56b9bb8cb64">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f4a5c5792678fc434b42">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-409ee7e69341f27e8800">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e4cc0e4445152d6c1687">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-02-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c6104a36faeeb8d864e5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b08913771274737f8e34">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-515ef1c5f7f3c08a6b17">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f98315a50f253dd8807f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-02-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7f14acb3bc5edb450c4d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3b8a418db0c9d70c22c8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-172e10be382d6f299b3a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-443f7a1db468379e665e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-02-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-de867b128ebf299210c6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a86ced3e706a817b69eb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1dcc5d16613f0c1eda8e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a26ebd4598372bbec771">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: avenue-lane-01-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fc72579dde2aefa2879b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fc72579dde2aefa2879b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-01-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-30883e76539a725a3799"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-30883e76539a725a3799`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-01-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-962c402a4364227f2e32"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-962c402a4364227f2e32`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-01-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-51e10996d7398fc32d87"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-51e10996d7398fc32d87`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-01-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-lane-01-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-541c1cf2af0f1df611db"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-541c1cf2af0f1df611db`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-01-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d9465930775addbcddec"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d9465930775addbcddec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-01-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-906fde0cdef35f89bbd3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-906fde0cdef35f89bbd3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-01-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f64cb67ee7bb63f918fc"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f64cb67ee7bb63f918fc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-01-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-lane-01-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1c9e064218962a77ac1f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1c9e064218962a77ac1f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-01-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2ca2154cbd577ca55bfa"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2ca2154cbd577ca55bfa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-01-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-afa6a01636cf950a3841"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-afa6a01636cf950a3841`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-01-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-84789f6d1abdd1a1e403"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-84789f6d1abdd1a1e403`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-01-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-lane-01-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0cb69d67ec7351cfb040"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0cb69d67ec7351cfb040`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-01-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-913fa8ce04bbd82147a0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-913fa8ce04bbd82147a0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-01-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d3b9e01548806e3db857"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d3b9e01548806e3db857`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-01-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-38646760eaf2784887fd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-38646760eaf2784887fd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-01-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-lane-01-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6af4aa1c7bc8f30ea718"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6af4aa1c7bc8f30ea718`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-01-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-58dc1efdfc9e7eb357eb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-58dc1efdfc9e7eb357eb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-01-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3a8da2a7acfbbe32ccd2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3a8da2a7acfbbe32ccd2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-01-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a836692cda5c49710872"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a836692cda5c49710872`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-01-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-lane-01-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-237a7c52e55d75964fd0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-237a7c52e55d75964fd0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-01-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e85f4642d90146885e02"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e85f4642d90146885e02`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-01-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ead8aaf0ebcb3a5e26a5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ead8aaf0ebcb3a5e26a5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-01-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1ac0c1651e3ec5b8fdfd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1ac0c1651e3ec5b8fdfd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-01-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-lane-01-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d858101c88744f8d539a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d858101c88744f8d539a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-01-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-626aaa309122ec6c0883"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-626aaa309122ec6c0883`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-01-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6c119cd41bd389a76c2f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6c119cd41bd389a76c2f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-01-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e6a20e7c500fc147d39e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e6a20e7c500fc147d39e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-01-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-lane-02-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ced02aea377b0c611c1e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ced02aea377b0c611c1e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-02-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3f4e183352c8dffdde29"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3f4e183352c8dffdde29`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-02-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-81ae6ce8208857cf2372"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-81ae6ce8208857cf2372`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-02-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a5b27a91079596b7892c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a5b27a91079596b7892c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-02-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-lane-02-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4617b0e6726ec6b31efe"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4617b0e6726ec6b31efe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-02-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-177f37680c87378f363f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-177f37680c87378f363f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-02-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-06226cc0cbb847b98ecf"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-06226cc0cbb847b98ecf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-02-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-93fcb37bdaedf0b078c9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-93fcb37bdaedf0b078c9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-02-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-lane-02-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-31b0067c35b73f9df3c2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-31b0067c35b73f9df3c2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-02-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f8bd2ba59179559614e8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f8bd2ba59179559614e8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-02-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-39feda91c89038842beb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-39feda91c89038842beb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-02-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cacc1cd6b9f094619d8d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cacc1cd6b9f094619d8d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-02-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-lane-02-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e9757a4d61af26cf614e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e9757a4d61af26cf614e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-02-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a978a9d55663d02ec95b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a978a9d55663d02ec95b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-02-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fa0fa1fc3ff723bc889f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fa0fa1fc3ff723bc889f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-02-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-83711bc64a04378d61ce"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-83711bc64a04378d61ce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-02-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-lane-02-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-74e8da79d6f02a39853a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-74e8da79d6f02a39853a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-02-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-21e911fd0b63d27e9606"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-21e911fd0b63d27e9606`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-02-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6a657873a78df77259ae"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6a657873a78df77259ae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-02-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f2f61fa2f6efa3a7cb1d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f2f61fa2f6efa3a7cb1d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-02-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-lane-02-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-45b63d24170f5e29763e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-45b63d24170f5e29763e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-02-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-16e35b3b2e6e64c9079c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-16e35b3b2e6e64c9079c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-02-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-892f41ddee4af98e84c3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-892f41ddee4af98e84c3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-02-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ab18e6b76bf975723e4b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ab18e6b76bf975723e4b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-02-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-lane-02-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c896452ccf3753977692"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c896452ccf3753977692`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-02-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ef4f0223b9e4582657a8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ef4f0223b9e4582657a8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-02-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0d5ea0551459ac52b385"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0d5ea0551459ac52b385`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-02-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-34a394ca54de59d0b7fa"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-34a394ca54de59d0b7fa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-02-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-01-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-835ad6f4fc32857fd1b2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-835ad6f4fc32857fd1b2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ce180553e57cdad05e02"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ce180553e57cdad05e02`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-007a5612ce7ca717bba9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-007a5612ce7ca717bba9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ebdef24251145b6b3550"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ebdef24251145b6b3550`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-01-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-20a6baabc0cfc3741d24"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-20a6baabc0cfc3741d24`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a9db056f835ef0b3f96d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a9db056f835ef0b3f96d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-77d6aab25f967dd6d1e7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-77d6aab25f967dd6d1e7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-25149f56c12ff61b725b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-25149f56c12ff61b725b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-01-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-495a7dea8a6172418299"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-495a7dea8a6172418299`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bba054282f8b726f2ccb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bba054282f8b726f2ccb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-397a7a4b42baabb71110"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-397a7a4b42baabb71110`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e30dacf7c64f14d6875b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e30dacf7c64f14d6875b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-01-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-73f5b322373f1b269f30"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-73f5b322373f1b269f30`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2d0e6b61cf9a1f088c8d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2d0e6b61cf9a1f088c8d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-15c32e6a7e4b5daee71e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-15c32e6a7e4b5daee71e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9d1319d11c0c16e9deff"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9d1319d11c0c16e9deff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-01-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ef99d8e3617bf2c03c5d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ef99d8e3617bf2c03c5d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8d9b0b9fb9e48aad81de"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8d9b0b9fb9e48aad81de`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-960d1321dd5d9a45daa9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-960d1321dd5d9a45daa9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fd23953f92c14b2ab2e5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fd23953f92c14b2ab2e5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-01-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0a023fa7110b084086ac"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0a023fa7110b084086ac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5792281ae01e2483dcad"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5792281ae01e2483dcad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5c0271acd5d0f1ac890f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5c0271acd5d0f1ac890f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-afb4dc30a840500dc648"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-afb4dc30a840500dc648`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-01-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-67a2e40ece9dbe57f5a9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-67a2e40ece9dbe57f5a9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c028a0db64a3ea28788c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c028a0db64a3ea28788c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a6cf81dd578f93c579aa"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a6cf81dd578f93c579aa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d22f1c4ce0b355a8ccb8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d22f1c4ce0b355a8ccb8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-02-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8c021376272e692b189a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8c021376272e692b189a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-93b45b7c70c06f56a033"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-93b45b7c70c06f56a033`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-02e3b347c004ba1b898c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-02e3b347c004ba1b898c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-89ff5b14357d594df6c1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-89ff5b14357d594df6c1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-02-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-abc9ecd0a0b3321cf41b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-abc9ecd0a0b3321cf41b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-05f842119bea3b6f7f33"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-05f842119bea3b6f7f33`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a4ccca3ca8cd0c86a343"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a4ccca3ca8cd0c86a343`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-709799dd070968320f1b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-709799dd070968320f1b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-02-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b273531ee22d95fc54f0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b273531ee22d95fc54f0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-565b07c0b3d816650a82"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-565b07c0b3d816650a82`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-244d39d9897293baef31"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-244d39d9897293baef31`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7da9c017a04be157f7da"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7da9c017a04be157f7da`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-02-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-20ef72fc1859b18ac1d7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-20ef72fc1859b18ac1d7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-979615a0cfdc351f2c86"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-979615a0cfdc351f2c86`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4bf9c945c3ad7e17947c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4bf9c945c3ad7e17947c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-75680da1c9d473c7d881"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-75680da1c9d473c7d881`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-02-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3e847175e4fce6dc23bb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3e847175e4fce6dc23bb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-070807a32f848dc8c771"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-070807a32f848dc8c771`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5974c3f9158b5c294513"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5974c3f9158b5c294513`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9d44253b8b65e906476d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9d44253b8b65e906476d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-02-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2530a99ed0f52dc9226e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2530a99ed0f52dc9226e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e0fd86801734ef3b6d27"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e0fd86801734ef3b6d27`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5ff1292b50b2e6375fd0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5ff1292b50b2e6375fd0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-16ae50a45bd30f03afb7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-16ae50a45bd30f03afb7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-02-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7d71562922c9ebfe4c20"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7d71562922c9ebfe4c20`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-151b1b3f29acfb1c4e8a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-151b1b3f29acfb1c4e8a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8c3a451546fc919717ad"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8c3a451546fc919717ad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6b00eeb6de8ff25d6d51"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6b00eeb6de8ff25d6d51`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-lane-03-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7fcf8f5411ab049473b4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7fcf8f5411ab049473b4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-03-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-82ed16639daaa874b9b8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-82ed16639daaa874b9b8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-03-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8976845ce9a7b0641a07"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8976845ce9a7b0641a07`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-03-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-de6aa234b0c94b1f8603"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-de6aa234b0c94b1f8603`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-03-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-lane-03-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-af7cc0b17b6423f13560"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-af7cc0b17b6423f13560`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-03-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ec0e15498d822d1991c9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ec0e15498d822d1991c9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-03-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5f183336f26d3f11e1a4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5f183336f26d3f11e1a4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-03-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-714e5ba61abb93a6d4b0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-714e5ba61abb93a6d4b0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-03-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-lane-03-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6e045a6735d38ca0e3e3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6e045a6735d38ca0e3e3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-03-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b40f403356261945b925"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b40f403356261945b925`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-03-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-28e607bcffca678f17e8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-28e607bcffca678f17e8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-03-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-238e998a5afff70c3ba6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-238e998a5afff70c3ba6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-03-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-lane-03-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0057e2c925627948d9ae"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0057e2c925627948d9ae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-03-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ba078e015316d542f699"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ba078e015316d542f699`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-03-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ec6615b2065a419ad87d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ec6615b2065a419ad87d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-03-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-95bcf1e230c5a4bb9b42"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-95bcf1e230c5a4bb9b42`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-03-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-lane-03-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-316a918622f2a7e61037"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-316a918622f2a7e61037`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-03-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cabbc7acae5fd363141c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cabbc7acae5fd363141c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-03-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-671a68b99b09dde1ccb3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-671a68b99b09dde1ccb3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-03-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0a437e09546335977140"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0a437e09546335977140`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-03-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-lane-03-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1ab8caba3036436f0069"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1ab8caba3036436f0069`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-03-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3ab60539d7f1c110c6ec"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3ab60539d7f1c110c6ec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-03-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-89d1eb5c7ef403e016aa"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-89d1eb5c7ef403e016aa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-03-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-541e0b39c7cb084f78fb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-541e0b39c7cb084f78fb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-03-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-lane-03-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-95466259d9dedd2815a9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-95466259d9dedd2815a9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-03-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-852dc5105ae911f6a29c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-852dc5105ae911f6a29c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-03-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cbfcbbe610075994b7d7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cbfcbbe610075994b7d7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-03-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2bcce4199f3b002b56b5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2bcce4199f3b002b56b5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-03-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-01-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-375402fea370ac5a4c71"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-375402fea370ac5a4c71`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f5eefb26d26251192494"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f5eefb26d26251192494`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c914a5e91bc43afd25e9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c914a5e91bc43afd25e9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-834f3e1f8b8d22c2df45"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-834f3e1f8b8d22c2df45`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-01-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c88dc5dce3e3b309c33e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c88dc5dce3e3b309c33e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c0690f6ff4726eb22bfd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c0690f6ff4726eb22bfd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-78c81c6f0d46fcaef2f4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-78c81c6f0d46fcaef2f4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-05f306e7445be4930848"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-05f306e7445be4930848`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-01-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-39d848faf1b1742d45d8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-39d848faf1b1742d45d8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0b101ff096f1529d49bc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0b101ff096f1529d49bc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e81be8a957b901d4de32"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e81be8a957b901d4de32`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f8794f12ae9f00942755"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f8794f12ae9f00942755`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-01-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1ef9c9ce61d57f164f80"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1ef9c9ce61d57f164f80`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ce4819e3209255e60874"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ce4819e3209255e60874`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5a8ca07d1afd234a48ff"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5a8ca07d1afd234a48ff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1d5c6d1164966ef0804d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1d5c6d1164966ef0804d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-01-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5367206dd0bd2ef41b24"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5367206dd0bd2ef41b24`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4a57575b9de8f06b22fb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4a57575b9de8f06b22fb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-34b96e24a11d104d16e1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-34b96e24a11d104d16e1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ed82a3254271bff55d39"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ed82a3254271bff55d39`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-01-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3a49a67dbacd5fe2d555"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3a49a67dbacd5fe2d555`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-851f8309b570f25dc27c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-851f8309b570f25dc27c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e5e41aea35ec55ed4df8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e5e41aea35ec55ed4df8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4b09caab6be9692128fb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4b09caab6be9692128fb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-01-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7f96d31a052f4d3ec346"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7f96d31a052f4d3ec346`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-75f4f6c2871706bb8c4b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-75f4f6c2871706bb8c4b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b1960772a86356937122"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b1960772a86356937122`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d7f9894cd89d05a0ad86"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d7f9894cd89d05a0ad86`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-lane-04-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d2999e066bd0777906d7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d2999e066bd0777906d7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-04-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-571373293976e7928db7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-571373293976e7928db7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-04-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c4e04b97c301e2b7030e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c4e04b97c301e2b7030e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-04-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-92b3841c7c3bc97c415d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-92b3841c7c3bc97c415d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-04-a; to port: lower-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-lane-04-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-db7c52f1697b7179af74"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-db7c52f1697b7179af74`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-04-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9df2b808975743edfe5c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9df2b808975743edfe5c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-04-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-20d845d5666bd015f72f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-20d845d5666bd015f72f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-04-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b07d4f11b9a93f5c315c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b07d4f11b9a93f5c315c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-04-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-lane-04-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3025a61c0f56212b6246"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3025a61c0f56212b6246`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-04-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4e095e8ed7a4398d4a6e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4e095e8ed7a4398d4a6e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-04-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ea7b89a6f0ecdfc698d5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ea7b89a6f0ecdfc698d5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-04-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4286052ffff351bbcfee"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4286052ffff351bbcfee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-04-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-lane-04-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c4d4a57d032fe3a10394"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c4d4a57d032fe3a10394`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-04-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cac99c8a082cf315fa8d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cac99c8a082cf315fa8d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-04-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7406d568a1f37f514116"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7406d568a1f37f514116`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-04-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-10d8e74396b994b0fb26"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-10d8e74396b994b0fb26`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-04-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-lane-04-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-06fbf5296e640078fcef"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-06fbf5296e640078fcef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-04-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ef319f6c4607a9ca686e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ef319f6c4607a9ca686e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-04-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-88d59b551a5fbae6df46"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-88d59b551a5fbae6df46`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-04-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cb0f839efa9a32ac0c58"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cb0f839efa9a32ac0c58`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-04-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-lane-04-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b8d21c361afde81b0a8b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b8d21c361afde81b0a8b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-04-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-725a57ecff294e9e8162"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-725a57ecff294e9e8162`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-04-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f74ee54a2a3926fcb6a7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f74ee54a2a3926fcb6a7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-04-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-15cc90c318e7036b0f9c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-15cc90c318e7036b0f9c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-04-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-lane-04-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-408da1de5a5b9dfa51a1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-408da1de5a5b9dfa51a1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-04-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d78f33aee8e550b785dc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d78f33aee8e550b785dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-04-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-926844256dc98237bb05"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-926844256dc98237bb05`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-04-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bce61ce0e966f9923765"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bce61ce0e966f9923765`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-04-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-02-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6904f59b896dcd5d66f1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6904f59b896dcd5d66f1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f2953ef6115da8c850ea"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f2953ef6115da8c850ea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-01e5b968d65b07b871c2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-01e5b968d65b07b871c2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-28b9e2da67295f33f849"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-28b9e2da67295f33f849`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-a; to port: lower-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-02-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-79d97e48cd6313303f51"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-79d97e48cd6313303f51`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1018d96c1080406042e7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1018d96c1080406042e7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f8b79da7b6b867ba1440"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f8b79da7b6b867ba1440`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-07b1449c9c9f96439763"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-07b1449c9c9f96439763`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-a; to port: avenue-lane-03-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-02-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cbb22ed4b6230263b059"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cbb22ed4b6230263b059`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-acfc0cdfe5f4d430f8f0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-acfc0cdfe5f4d430f8f0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b5ee5b2658e7e8f773ef"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b5ee5b2658e7e8f773ef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4ca82929b3bd8ea4cde9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4ca82929b3bd8ea4cde9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-a; to port: avenue-lane-04-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-02-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bca56d96a56b9bb8cb64"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bca56d96a56b9bb8cb64`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f4a5c5792678fc434b42"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f4a5c5792678fc434b42`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-409ee7e69341f27e8800"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-409ee7e69341f27e8800`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e4cc0e4445152d6c1687"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e4cc0e4445152d6c1687`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-a; to port: avenue-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-02-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c6104a36faeeb8d864e5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c6104a36faeeb8d864e5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b08913771274737f8e34"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b08913771274737f8e34`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-515ef1c5f7f3c08a6b17"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-515ef1c5f7f3c08a6b17`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f98315a50f253dd8807f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f98315a50f253dd8807f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-a; to port: avenue-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-02-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7f14acb3bc5edb450c4d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7f14acb3bc5edb450c4d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3b8a418db0c9d70c22c8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3b8a418db0c9d70c22c8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-172e10be382d6f299b3a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-172e10be382d6f299b3a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-443f7a1db468379e665e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-443f7a1db468379e665e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-a; to port: upper-lane-02-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-02-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-de867b128ebf299210c6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-de867b128ebf299210c6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a86ced3e706a817b69eb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a86ced3e706a817b69eb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1dcc5d16613f0c1eda8e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1dcc5d16613f0c1eda8e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a26ebd4598372bbec771"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a26ebd4598372bbec771`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-a; to port: upper-lane-01-b; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → pedestrian — 64 cases; unverified: 64</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: avenue-lane-01-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e74cb86cea60c8392b39">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fd5a5555b59cc55842e1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f2db5aca062e15913951">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1ad175b0a586fbb21d9c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-lane-01-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-076fd30acb2394d94ae1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f340837e2d68826182a1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8df492832088b1eba5f2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-af02237ee64bd982735e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-lane-02-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5c661a68cb5fd122a1ea">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3fc44d0462d53000c6d1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6be8eb3a9beec8d5dbe0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fcba5a9ef5d82c8d3c34">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-lane-02-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0fdeeae15369a41df225">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f976fc00adbe00ee187a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-06758c1a78c6f348bde4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6bff47f6d177262ebda7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-01-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-36d8b7ee448943818d55">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-796824f3536c602be632">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0c254e27ba5ee7823edd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5071a5668fd7b918f6ae">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-01-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-eaea816be88031f8a7dc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-272ff579c29fffd02d90">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b98c2ccd844f3475b0e9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fd01fa203f76d529ea6c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-02-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-576a3c3ae739576dbb63">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5b1b0d80fed8b1859580">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e014e7c2f23192e480b7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7ac6cb5f2f3198877514">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: upper-lane-02-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a24fe1f8ff4cd43ccb82">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c267f0df583a2619f60c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-118956c9a8ab4c020ba7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-be8f776ab60175a5da57">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-lane-03-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3a52284299c05cbfdcff">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-575c0ba867be7d611b29">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-277c63e15ef8056d295c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c7118f595bcb3324605c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-lane-03-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7e4d89436c99a720f72d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-612158ef72d645e9221f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-723866942ca66d5effd6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ac185892f78ad81fbdd9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-01-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-749e207c8eba9e931b04">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4d82f5b6cfa43e5336c4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a66ede18c7a578e22ee9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c2c2d56d6d795b42ffdb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-01-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f9fe4795fe1b68ac6d9e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aea4632d6466581cbfe0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b2402761cd5010a938d9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-652cac56f1ccfccd8238">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-lane-04-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-64e735e5a8e66e3743e6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-81b4319598e47194c21a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-33aeb6524e003fa48c2e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e716eec09a149a72e487">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-lane-04-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-63eff78d9efb7b4401af">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7b7e3b23a7f6fb79267a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4f5e431ac2ea5ac4d263">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-02456f09956798287c30">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-02-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-36d7d2c8da2e9c5ce4d5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-26c48cad9b59bfc4e8ab">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-45ff84999c7a8bb0a2a5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8324788d19220bd130c4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: lower-lane-02-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-99c2389f75ab1b0aed90">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-61c4c8e74209e23d2439">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-434d26f1e6b5c681d5a7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5305b498033179e46a83">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: avenue-lane-01-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e74cb86cea60c8392b39"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e74cb86cea60c8392b39`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-01-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fd5a5555b59cc55842e1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fd5a5555b59cc55842e1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-01-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f2db5aca062e15913951"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f2db5aca062e15913951`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-01-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1ad175b0a586fbb21d9c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1ad175b0a586fbb21d9c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-01-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-lane-01-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-076fd30acb2394d94ae1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-076fd30acb2394d94ae1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-01-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f340837e2d68826182a1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f340837e2d68826182a1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-01-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8df492832088b1eba5f2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8df492832088b1eba5f2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-01-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-af02237ee64bd982735e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-af02237ee64bd982735e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-01-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-lane-02-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5c661a68cb5fd122a1ea"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5c661a68cb5fd122a1ea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-02-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3fc44d0462d53000c6d1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3fc44d0462d53000c6d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-02-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6be8eb3a9beec8d5dbe0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6be8eb3a9beec8d5dbe0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-02-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fcba5a9ef5d82c8d3c34"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fcba5a9ef5d82c8d3c34`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-02-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-lane-02-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0fdeeae15369a41df225"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0fdeeae15369a41df225`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-02-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f976fc00adbe00ee187a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f976fc00adbe00ee187a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-02-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-06758c1a78c6f348bde4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-06758c1a78c6f348bde4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-02-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6bff47f6d177262ebda7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6bff47f6d177262ebda7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-02-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-01-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-36d8b7ee448943818d55"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-36d8b7ee448943818d55`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-796824f3536c602be632"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-796824f3536c602be632`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0c254e27ba5ee7823edd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0c254e27ba5ee7823edd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5071a5668fd7b918f6ae"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5071a5668fd7b918f6ae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-01-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-eaea816be88031f8a7dc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-eaea816be88031f8a7dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-272ff579c29fffd02d90"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-272ff579c29fffd02d90`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b98c2ccd844f3475b0e9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b98c2ccd844f3475b0e9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fd01fa203f76d529ea6c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fd01fa203f76d529ea6c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-01-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-02-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-576a3c3ae739576dbb63"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-576a3c3ae739576dbb63`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5b1b0d80fed8b1859580"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5b1b0d80fed8b1859580`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e014e7c2f23192e480b7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e014e7c2f23192e480b7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7ac6cb5f2f3198877514"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7ac6cb5f2f3198877514`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: upper-lane-02-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a24fe1f8ff4cd43ccb82"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a24fe1f8ff4cd43ccb82`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c267f0df583a2619f60c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c267f0df583a2619f60c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-118956c9a8ab4c020ba7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-118956c9a8ab4c020ba7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-be8f776ab60175a5da57"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-be8f776ab60175a5da57`.

Confirm this undeclared transfer is unavailable.

Scope: from port: upper-lane-02-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-lane-03-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3a52284299c05cbfdcff"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3a52284299c05cbfdcff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-03-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-575c0ba867be7d611b29"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-575c0ba867be7d611b29`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-03-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-277c63e15ef8056d295c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-277c63e15ef8056d295c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-03-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c7118f595bcb3324605c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c7118f595bcb3324605c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-03-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-lane-03-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7e4d89436c99a720f72d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7e4d89436c99a720f72d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-03-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-612158ef72d645e9221f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-612158ef72d645e9221f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-03-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-723866942ca66d5effd6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-723866942ca66d5effd6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-03-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ac185892f78ad81fbdd9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ac185892f78ad81fbdd9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-03-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-01-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-749e207c8eba9e931b04"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-749e207c8eba9e931b04`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4d82f5b6cfa43e5336c4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4d82f5b6cfa43e5336c4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a66ede18c7a578e22ee9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a66ede18c7a578e22ee9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c2c2d56d6d795b42ffdb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c2c2d56d6d795b42ffdb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-01-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f9fe4795fe1b68ac6d9e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f9fe4795fe1b68ac6d9e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aea4632d6466581cbfe0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-aea4632d6466581cbfe0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b2402761cd5010a938d9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b2402761cd5010a938d9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-652cac56f1ccfccd8238"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-652cac56f1ccfccd8238`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-01-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-lane-04-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-64e735e5a8e66e3743e6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-64e735e5a8e66e3743e6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-04-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-81b4319598e47194c21a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-81b4319598e47194c21a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-04-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-33aeb6524e003fa48c2e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-33aeb6524e003fa48c2e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-04-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e716eec09a149a72e487"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e716eec09a149a72e487`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-04-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-lane-04-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-63eff78d9efb7b4401af"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-63eff78d9efb7b4401af`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-04-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7b7e3b23a7f6fb79267a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7b7e3b23a7f6fb79267a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-04-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4f5e431ac2ea5ac4d263"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4f5e431ac2ea5ac4d263`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-04-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-02456f09956798287c30"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-02456f09956798287c30`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-lane-04-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-02-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-36d7d2c8da2e9c5ce4d5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-36d7d2c8da2e9c5ce4d5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-26c48cad9b59bfc4e8ab"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-26c48cad9b59bfc4e8ab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-45ff84999c7a8bb0a2a5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-45ff84999c7a8bb0a2a5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8324788d19220bd130c4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8324788d19220bd130c4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-a; to port: avenue-walkway-02-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: lower-lane-02-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-99c2389f75ab1b0aed90"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-99c2389f75ab1b0aed90`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-61c4c8e74209e23d2439"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-61c4c8e74209e23d2439`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-434d26f1e6b5c681d5a7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-434d26f1e6b5c681d5a7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5305b498033179e46a83"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5305b498033179e46a83`.

Confirm this undeclared transfer is unavailable.

Scope: from port: lower-lane-02-a; to port: avenue-walkway-01-b; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — pedestrian → road — 64 cases; unverified: 64</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: avenue-walkway-01-a; to port: lower-lane-02-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8e2818c59df03d453238">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-df6b518073b0551cea7c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c1e1006a01f2ce3418e9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-737735d94535dce8a32a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-walkway-01-a; to port: lower-lane-01-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c7e8fcb2c65d9e26afa9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f7ee8ee950b6400fdd48">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c2969cebcc8e93ec126f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aee579b80228bcc0a0d6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-walkway-01-a; to port: avenue-lane-03-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0b4ab4a1afed7545e1bf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-10c3b5331edc18cffb41">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4cc5638e7c22d8f3956f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3139d614a767751dce13">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-walkway-01-a; to port: avenue-lane-04-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a3e1c3c6d7ed27f877be">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a9efa0fc24bca21e00ba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1e0eb4a4d433ee686f89">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eb19b6f6721cf60dcd5c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-walkway-01-a; to port: avenue-lane-01-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1b6910bd19bff706b2b4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-895a18c32079a926ec5e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2e2bdf53bd124227f4e0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c14caec2b4f37409320f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-walkway-01-a; to port: avenue-lane-02-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7a6a470be417209a66ce">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-962b5e16a5b9e6ef5a6d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d57d8988a9c212577942">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f4adf62801121146e839">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-walkway-01-a; to port: upper-lane-02-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d92acfd7d619624f0c22">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8b66529023bddd77016e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6d1849a4ad2ac8a1ebe7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3d24b052ebb2ac66ab36">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-walkway-01-a; to port: upper-lane-01-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-eb322eaed90ec801e5ee">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b6c9e40adee6e356f6bf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-94045ad67ac5160ec2ae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9070ba38e0caef9d8de1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-walkway-02-a; to port: lower-lane-02-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ea799739264e6b43bdf5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-92ee68f47944f824f00f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7702c46b19dbada65524">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d86dcba0b18dd34544b8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-walkway-02-a; to port: lower-lane-01-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-408ef01f75ae27fbdbb8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b4575b26435304f73408">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cd7f8e38d15bab04bad5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3664ef3aa8c92f20dc81">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-walkway-02-a; to port: avenue-lane-03-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-10862139186fa73e6db3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-043dcbc34fdeed93cdbf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fc81b599b39837d1cb35">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cc12c32eae1d78683e42">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-walkway-02-a; to port: avenue-lane-04-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-528536438891031af40f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9bb7eec257ef90a1ba0d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d75f6bbf7202ff1782ef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f8430ee4b6cd533f68db">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-walkway-02-a; to port: avenue-lane-01-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d58d8e476711838fd192">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-630b3e26f36b2460ce56">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c11eda14f922c1301bda">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-708a4d85faee3aafea23">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-walkway-02-a; to port: avenue-lane-02-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9783f4cf74141b923fea">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6580ab5ba34cac642a87">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f393b1aec884bdb7d4c7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dfaa1e5df30bd1a3df15">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-walkway-02-a; to port: upper-lane-02-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1c736fd8b869c3cfc5b2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b5fc5940f6b7b7cb56d4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e68d2d235f42369486c6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-082569f784c1ccec8235">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-walkway-02-a; to port: upper-lane-01-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a0f15d6770d13106d1c1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7c62cf4cf64a5d7491b7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4929c5fe8efb059531f0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-786106f53144af3c8712">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: avenue-walkway-01-a; to port: lower-lane-02-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8e2818c59df03d453238"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8e2818c59df03d453238`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-01-a; to port: lower-lane-02-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-df6b518073b0551cea7c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-df6b518073b0551cea7c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-01-a; to port: lower-lane-02-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c1e1006a01f2ce3418e9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c1e1006a01f2ce3418e9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-01-a; to port: lower-lane-02-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-737735d94535dce8a32a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-737735d94535dce8a32a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-01-a; to port: lower-lane-02-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-walkway-01-a; to port: lower-lane-01-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c7e8fcb2c65d9e26afa9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c7e8fcb2c65d9e26afa9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-01-a; to port: lower-lane-01-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f7ee8ee950b6400fdd48"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f7ee8ee950b6400fdd48`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-01-a; to port: lower-lane-01-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c2969cebcc8e93ec126f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c2969cebcc8e93ec126f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-01-a; to port: lower-lane-01-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aee579b80228bcc0a0d6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-aee579b80228bcc0a0d6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-01-a; to port: lower-lane-01-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-walkway-01-a; to port: avenue-lane-03-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0b4ab4a1afed7545e1bf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0b4ab4a1afed7545e1bf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-01-a; to port: avenue-lane-03-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-10c3b5331edc18cffb41"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-10c3b5331edc18cffb41`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-01-a; to port: avenue-lane-03-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4cc5638e7c22d8f3956f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4cc5638e7c22d8f3956f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-01-a; to port: avenue-lane-03-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3139d614a767751dce13"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3139d614a767751dce13`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-01-a; to port: avenue-lane-03-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-walkway-01-a; to port: avenue-lane-04-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a3e1c3c6d7ed27f877be"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a3e1c3c6d7ed27f877be`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-01-a; to port: avenue-lane-04-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a9efa0fc24bca21e00ba"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a9efa0fc24bca21e00ba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-01-a; to port: avenue-lane-04-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1e0eb4a4d433ee686f89"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1e0eb4a4d433ee686f89`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-01-a; to port: avenue-lane-04-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eb19b6f6721cf60dcd5c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-eb19b6f6721cf60dcd5c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-01-a; to port: avenue-lane-04-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-walkway-01-a; to port: avenue-lane-01-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1b6910bd19bff706b2b4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1b6910bd19bff706b2b4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-01-a; to port: avenue-lane-01-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-895a18c32079a926ec5e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-895a18c32079a926ec5e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-01-a; to port: avenue-lane-01-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2e2bdf53bd124227f4e0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2e2bdf53bd124227f4e0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-01-a; to port: avenue-lane-01-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c14caec2b4f37409320f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c14caec2b4f37409320f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-01-a; to port: avenue-lane-01-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-walkway-01-a; to port: avenue-lane-02-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7a6a470be417209a66ce"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7a6a470be417209a66ce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-01-a; to port: avenue-lane-02-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-962b5e16a5b9e6ef5a6d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-962b5e16a5b9e6ef5a6d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-01-a; to port: avenue-lane-02-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d57d8988a9c212577942"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d57d8988a9c212577942`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-01-a; to port: avenue-lane-02-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f4adf62801121146e839"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f4adf62801121146e839`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-01-a; to port: avenue-lane-02-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-walkway-01-a; to port: upper-lane-02-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d92acfd7d619624f0c22"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d92acfd7d619624f0c22`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-01-a; to port: upper-lane-02-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8b66529023bddd77016e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8b66529023bddd77016e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-01-a; to port: upper-lane-02-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6d1849a4ad2ac8a1ebe7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6d1849a4ad2ac8a1ebe7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-01-a; to port: upper-lane-02-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3d24b052ebb2ac66ab36"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3d24b052ebb2ac66ab36`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-01-a; to port: upper-lane-02-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-walkway-01-a; to port: upper-lane-01-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-eb322eaed90ec801e5ee"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-eb322eaed90ec801e5ee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-01-a; to port: upper-lane-01-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b6c9e40adee6e356f6bf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b6c9e40adee6e356f6bf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-01-a; to port: upper-lane-01-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-94045ad67ac5160ec2ae"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-94045ad67ac5160ec2ae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-01-a; to port: upper-lane-01-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9070ba38e0caef9d8de1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9070ba38e0caef9d8de1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-01-a; to port: upper-lane-01-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-walkway-02-a; to port: lower-lane-02-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ea799739264e6b43bdf5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ea799739264e6b43bdf5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-02-a; to port: lower-lane-02-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-92ee68f47944f824f00f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-92ee68f47944f824f00f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-02-a; to port: lower-lane-02-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7702c46b19dbada65524"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7702c46b19dbada65524`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-02-a; to port: lower-lane-02-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d86dcba0b18dd34544b8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d86dcba0b18dd34544b8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-02-a; to port: lower-lane-02-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-walkway-02-a; to port: lower-lane-01-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-408ef01f75ae27fbdbb8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-408ef01f75ae27fbdbb8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-02-a; to port: lower-lane-01-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b4575b26435304f73408"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b4575b26435304f73408`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-02-a; to port: lower-lane-01-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cd7f8e38d15bab04bad5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cd7f8e38d15bab04bad5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-02-a; to port: lower-lane-01-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3664ef3aa8c92f20dc81"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3664ef3aa8c92f20dc81`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-02-a; to port: lower-lane-01-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-walkway-02-a; to port: avenue-lane-03-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-10862139186fa73e6db3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-10862139186fa73e6db3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-02-a; to port: avenue-lane-03-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-043dcbc34fdeed93cdbf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-043dcbc34fdeed93cdbf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-02-a; to port: avenue-lane-03-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fc81b599b39837d1cb35"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fc81b599b39837d1cb35`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-02-a; to port: avenue-lane-03-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cc12c32eae1d78683e42"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cc12c32eae1d78683e42`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-02-a; to port: avenue-lane-03-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-walkway-02-a; to port: avenue-lane-04-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-528536438891031af40f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-528536438891031af40f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-02-a; to port: avenue-lane-04-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9bb7eec257ef90a1ba0d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9bb7eec257ef90a1ba0d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-02-a; to port: avenue-lane-04-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d75f6bbf7202ff1782ef"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d75f6bbf7202ff1782ef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-02-a; to port: avenue-lane-04-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f8430ee4b6cd533f68db"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f8430ee4b6cd533f68db`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-02-a; to port: avenue-lane-04-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-walkway-02-a; to port: avenue-lane-01-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d58d8e476711838fd192"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d58d8e476711838fd192`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-02-a; to port: avenue-lane-01-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-630b3e26f36b2460ce56"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-630b3e26f36b2460ce56`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-02-a; to port: avenue-lane-01-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c11eda14f922c1301bda"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c11eda14f922c1301bda`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-02-a; to port: avenue-lane-01-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-708a4d85faee3aafea23"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-708a4d85faee3aafea23`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-02-a; to port: avenue-lane-01-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-walkway-02-a; to port: avenue-lane-02-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9783f4cf74141b923fea"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9783f4cf74141b923fea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-02-a; to port: avenue-lane-02-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6580ab5ba34cac642a87"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6580ab5ba34cac642a87`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-02-a; to port: avenue-lane-02-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f393b1aec884bdb7d4c7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f393b1aec884bdb7d4c7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-02-a; to port: avenue-lane-02-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dfaa1e5df30bd1a3df15"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dfaa1e5df30bd1a3df15`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-02-a; to port: avenue-lane-02-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-walkway-02-a; to port: upper-lane-02-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1c736fd8b869c3cfc5b2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1c736fd8b869c3cfc5b2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-02-a; to port: upper-lane-02-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b5fc5940f6b7b7cb56d4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b5fc5940f6b7b7cb56d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-02-a; to port: upper-lane-02-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e68d2d235f42369486c6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e68d2d235f42369486c6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-02-a; to port: upper-lane-02-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-082569f784c1ccec8235"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-082569f784c1ccec8235`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-02-a; to port: upper-lane-02-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-walkway-02-a; to port: upper-lane-01-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a0f15d6770d13106d1c1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a0f15d6770d13106d1c1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-02-a; to port: upper-lane-01-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7c62cf4cf64a5d7491b7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7c62cf4cf64a5d7491b7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-02-a; to port: upper-lane-01-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4929c5fe8efb059531f0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4929c5fe8efb059531f0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-02-a; to port: upper-lane-01-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-786106f53144af3c8712"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-786106f53144af3c8712`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-02-a; to port: upper-lane-01-b; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — pedestrian → pedestrian — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: avenue-walkway-01-a; to port: avenue-walkway-02-b; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c50cb8646bf92a340a1d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d4f4e6cc5e7565637226">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1eae3875751015c83f76">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-108094cfa3a53188a582">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: avenue-walkway-02-a; to port: avenue-walkway-01-b; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c67ff91be487d93153d0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2fd2bb2d7a0fbd784e1c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cb87e57249ca471a72b1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ae23258088e3238eeb85">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: avenue-walkway-01-a; to port: avenue-walkway-02-b; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c50cb8646bf92a340a1d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c50cb8646bf92a340a1d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-01-a; to port: avenue-walkway-02-b; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d4f4e6cc5e7565637226"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d4f4e6cc5e7565637226`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-01-a; to port: avenue-walkway-02-b; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1eae3875751015c83f76"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1eae3875751015c83f76`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-01-a; to port: avenue-walkway-02-b; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-108094cfa3a53188a582"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-108094cfa3a53188a582`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-01-a; to port: avenue-walkway-02-b; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: avenue-walkway-02-a; to port: avenue-walkway-01-b; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c67ff91be487d93153d0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c67ff91be487d93153d0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-02-a; to port: avenue-walkway-01-b; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2fd2bb2d7a0fbd784e1c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2fd2bb2d7a0fbd784e1c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-02-a; to port: avenue-walkway-01-b; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cb87e57249ca471a72b1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cb87e57249ca471a72b1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-02-a; to port: avenue-walkway-01-b; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ae23258088e3238eeb85"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ae23258088e3238eeb85`.

Confirm this undeclared transfer is unavailable.

Scope: from port: avenue-walkway-02-a; to port: avenue-walkway-01-b; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-over-avenue-l0-crossing-diagonal-90deg:canonical-southeast | <a href="#case-preview_review-760a35932621b122fd3d">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-over-avenue-l0-crossing-diagonal-90deg:canonical-top | <a href="#case-preview_review-28ad6bac22317b568e64">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-l1-and-l2-over-avenue-l0-crossing-diagonal-90deg:connection-overview | <a href="#case-preview_review-7c00f03aebffffd93c14">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-over-avenue-l0-crossing-diagonal-90deg:canonical-southeast</summary>

<a id="case-preview_review-760a35932621b122fd3d"></a>

**General: unverified** — `preview_review-760a35932621b122fd3d`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-and-l2-over-avenue-l0-crossing-diagonal-90deg:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-over-avenue-l0-crossing-diagonal-90deg:canonical-top</summary>

<a id="case-preview_review-28ad6bac22317b568e64"></a>

**General: unverified** — `preview_review-28ad6bac22317b568e64`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-and-l2-over-avenue-l0-crossing-diagonal-90deg:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-l1-and-l2-over-avenue-l0-crossing-diagonal-90deg:connection-overview</summary>

<a id="case-preview_review-7c00f03aebffffd93c14"></a>

**General: unverified** — `preview_review-7c00f03aebffffd93c14`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-l1-and-l2-over-avenue-l0-crossing-diagonal-90deg:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

Created on branch `codex/double-decker-diagonal-highway` for a compact Tokyo-style interchange. The earlier source-only schematic remains separately identified in the assembly’s design history. Saved-city resource identifiers are reserved locally and must remain stable; public allocation and redistribution are pending.
