---
title: "Testing: DD RHW-4 — Straight Diagonal Highway Stamp"
summary: "Check this exact component's traffic ownership, complete physical geometry, and scoped game observations."
audience: "contributors"
document_type: "reference"
---

# Testing: DD RHW-4 — Straight Diagonal Highway Stamp

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

Inspect the exact `ddrhw-modular-highway-stamp` resources and the matching complete [assembly](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/TESTING.md). The stamp retains native highway and Avenue through routes, pedestrian routes, and the ramp-route portions inside highway-owned tiles. Some of these ramp-route portions have no external roadway until a separate full ramp is attached. Test cars only after completing the matching assembly.

A **PATH** is a saved traffic-route resource, and an **S3D** is the visible model made from indexed triangles. Model faces can extend beyond the tiles that store this piece's PATHs. A flat physical cut at the native highway edge is different from the traffic connection at a city-tile edge. Check both, rather than assuming that one card describes the entire physical opening.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `1-W-out-1` | road / 1 / primary | out | [-8.0, -147.2, 7.5]; [-0.7071067811865479, -0.7071067811865472]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `1-W-in-2` | road / 1 / primary | in | [-8.0, -147.2, 15.0]; [0.7071067811865479, 0.7071067811865472]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `1-W-out-3` | road / 1 / primary | out | [-8.0, -140.8, 7.5]; [-0.7071067811865467, -0.7071067811865483]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `1-W-in-4` | road / 1 / primary | in | [-8.0, -140.8, 15.0]; [0.7071067811865467, 0.7071067811865483]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `1-N-in-5` | road / 1 / primary | in | [22.634072, -104.0, 7.5]; [-0.11342781758931368, -0.9935462395867267]; 0.0 | `path-interface-80baad95505e6e935a1d` |
| `1-E-out-6` | road / 1 / primary | out | [24.0, -126.669671, 15.0]; [0.9174390336849364, 0.39787638717477336]; 0.0 | `path-interface-ce3cae183318f13b1134` |
| `1-W-out-7` | road / 1 / primary | out | [24.0, -97.960601, 7.5]; [-0.24638679279420395, -0.9691715783784551]; 0.0 | `path-interface-d227520a15c3abcdb327` |
| `1-N-in-8` | road / 1 / primary | in | [26.207444, -88.0, 6.745132]; [-0.20216938843111806, -0.9793505697049386]; 0.226756787 | `path-interface-85fe4503e80b365632f0` |
| `1-N-in-9` | road / 1 / primary | in | [44.8, -56.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-668896c488171c19873d` |
| `1-N-in-10` | road / 1 / primary | in | [51.2, -56.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `1-W-out-11` | road / 1 / primary | out | [56.0, -51.2, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `1-W-out-12` | road / 1 / primary | out | [56.0, -44.8, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `1-E-out-13` | road / 1 / primary | out | [72.0, -83.2, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `1-E-out-14` | road / 1 / primary | out | [72.0, -76.8, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `1-S-in-15` | road / 1 / primary | in | [76.8, -72.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `1-S-in-16` | road / 1 / primary | in | [83.2, -72.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-668896c488171c19873d` |
| `1-W-out-17` | road / 1 / primary | out | [88.0, -26.207444, 6.745132]; [-0.9793505697049386, -0.20216938843111806]; -0.226756787 | `path-interface-20a6d5708b4a74c22702` |
| `1-N-in-18` | road / 1 / primary | in | [97.960601, -24.0, 7.5]; [-0.9691715783784551, -0.24638679279420395]; 0.0 | `path-interface-3dcc6d5eb15355745274` |
| `1-W-out-19` | road / 1 / primary | out | [104.0, -22.634072, 7.5]; [-0.9935462395867267, -0.11342781758931368]; 0.0 | `path-interface-34a26816572a48081146` |
| `1-S-in-20` | road / 1 / primary | in | [126.669671, -24.0, 15.0]; [0.39787638717477336, 0.9174390336849364]; 0.0 | `path-interface-b59a461ae329e598a227` |
| `1-N-in-21` | road / 1 / primary | in | [140.8, 8.0, 7.5]; [-0.7071067811865483, -0.7071067811865467]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `1-N-out-22` | road / 1 / primary | out | [140.8, 8.0, 15.0]; [0.7071067811865483, 0.7071067811865467]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `1-N-in-23` | road / 1 / primary | in | [147.2, 8.0, 7.5]; [-0.7071067811865472, -0.7071067811865479]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `1-N-out-24` | road / 1 / primary | out | [147.2, 8.0, 15.0]; [0.7071067811865472, 0.7071067811865479]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `2-N-in-1` | pedestrian / 2 / primary | in | [40.7, -56.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-2ec6b824afff9b450810` |
| `2-W-out-2` | pedestrian / 2 / primary | out | [56.0, -40.7, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-ef45fb4474012bf121a0` |
| `2-E-out-3` | pedestrian / 2 / primary | out | [72.0, -87.3, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-ef45fb4474012bf121a0` |
| `2-S-in-4` | pedestrian / 2 / primary | in | [87.3, -72.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-2ec6b824afff9b450810` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `1-W-in-2` → `1-E-out-6` | primary |
| road | `1-W-in-2` → `1-N-out-24` | primary |
| road | `1-W-in-4` → `1-N-out-22` | primary |
| road | `1-N-in-5` → `1-W-out-3` | primary |
| road | `1-N-in-8` → `1-W-out-7` | primary |
| road | `1-N-in-9` → `1-E-out-13` | primary |
| road | `1-N-in-10` → `1-E-out-14` | primary |
| road | `1-S-in-15` → `1-W-out-11` | primary |
| road | `1-S-in-16` → `1-W-out-12` | primary |
| road | `1-N-in-18` → `1-W-out-17` | primary |
| road | `1-S-in-20` → `1-N-out-24` | primary |
| road | `1-N-in-21` → `1-W-out-19` | primary |
| road | `1-N-in-21` → `1-W-out-3` | primary |
| road | `1-N-in-23` → `1-W-out-1` | primary |
| pedestrian | `2-N-in-1` → `2-E-out-3` | primary |
| pedestrian | `2-S-in-4` → `2-W-out-2` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `1-W-in-2` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-2` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-2` | road / `1-W-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-2` | road / `1-W-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-2` | road / `1-W-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-2` | road / `1-E-out-13` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-2` | road / `1-E-out-14` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-2` | road / `1-W-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-2` | road / `1-W-out-19` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-2` | road / `1-N-out-22` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-2` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-2` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-4` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-4` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-4` | road / `1-E-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-4` | road / `1-W-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-4` | road / `1-W-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-4` | road / `1-W-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-4` | road / `1-E-out-13` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-4` | road / `1-E-out-14` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-4` | road / `1-W-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-4` | road / `1-W-out-19` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-4` | road / `1-N-out-24` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-4` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-W-in-4` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-5` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-5` | road / `1-E-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-5` | road / `1-W-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-5` | road / `1-W-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-5` | road / `1-W-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-5` | road / `1-E-out-13` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-5` | road / `1-E-out-14` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-5` | road / `1-W-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-5` | road / `1-W-out-19` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-5` | road / `1-N-out-22` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-5` | road / `1-N-out-24` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-5` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-5` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-8` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-8` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-8` | road / `1-E-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-8` | road / `1-W-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-8` | road / `1-W-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-8` | road / `1-E-out-13` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-8` | road / `1-E-out-14` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-8` | road / `1-W-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-8` | road / `1-W-out-19` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-8` | road / `1-N-out-22` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-8` | road / `1-N-out-24` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-8` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-8` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-9` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-9` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-9` | road / `1-E-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-9` | road / `1-W-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-9` | road / `1-W-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-9` | road / `1-W-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-9` | road / `1-E-out-14` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-9` | road / `1-W-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-9` | road / `1-W-out-19` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-9` | road / `1-N-out-22` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-9` | road / `1-N-out-24` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-9` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-9` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-10` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-10` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-10` | road / `1-E-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-10` | road / `1-W-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-10` | road / `1-W-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-10` | road / `1-W-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-10` | road / `1-E-out-13` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-10` | road / `1-W-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-10` | road / `1-W-out-19` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-10` | road / `1-N-out-22` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-10` | road / `1-N-out-24` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-10` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-10` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-15` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-15` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-15` | road / `1-E-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-15` | road / `1-W-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-15` | road / `1-W-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-15` | road / `1-E-out-13` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-15` | road / `1-E-out-14` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-15` | road / `1-W-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-15` | road / `1-W-out-19` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-15` | road / `1-N-out-22` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-15` | road / `1-N-out-24` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-15` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-15` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-16` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-16` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-16` | road / `1-E-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-16` | road / `1-W-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-16` | road / `1-W-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-16` | road / `1-E-out-13` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-16` | road / `1-E-out-14` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-16` | road / `1-W-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-16` | road / `1-W-out-19` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-16` | road / `1-N-out-22` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-16` | road / `1-N-out-24` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-16` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-16` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-18` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-18` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-18` | road / `1-E-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-18` | road / `1-W-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-18` | road / `1-W-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-18` | road / `1-W-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-18` | road / `1-E-out-13` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-18` | road / `1-E-out-14` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-18` | road / `1-W-out-19` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-18` | road / `1-N-out-22` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-18` | road / `1-N-out-24` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-18` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-18` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-20` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-20` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-20` | road / `1-E-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-20` | road / `1-W-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-20` | road / `1-W-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-20` | road / `1-W-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-20` | road / `1-E-out-13` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-20` | road / `1-E-out-14` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-20` | road / `1-W-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-20` | road / `1-W-out-19` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-20` | road / `1-N-out-22` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-20` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-S-in-20` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-21` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-21` | road / `1-E-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-21` | road / `1-W-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-21` | road / `1-W-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-21` | road / `1-W-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-21` | road / `1-E-out-13` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-21` | road / `1-E-out-14` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-21` | road / `1-W-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-21` | road / `1-N-out-22` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-21` | road / `1-N-out-24` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-21` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-21` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-23` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-23` | road / `1-E-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-23` | road / `1-W-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-23` | road / `1-W-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-23` | road / `1-W-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-23` | road / `1-E-out-13` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-23` | road / `1-E-out-14` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-23` | road / `1-W-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-23` | road / `1-W-out-19` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-23` | road / `1-N-out-22` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-23` | road / `1-N-out-24` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-23` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| road / `1-N-in-23` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-N-in-1` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-N-in-1` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-N-in-1` | road / `1-E-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-N-in-1` | road / `1-W-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-N-in-1` | road / `1-W-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-N-in-1` | road / `1-W-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-N-in-1` | road / `1-E-out-13` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-N-in-1` | road / `1-E-out-14` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-N-in-1` | road / `1-W-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-N-in-1` | road / `1-W-out-19` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-N-in-1` | road / `1-N-out-22` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-N-in-1` | road / `1-N-out-24` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-N-in-1` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-S-in-4` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-S-in-4` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-S-in-4` | road / `1-E-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-S-in-4` | road / `1-W-out-7` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-S-in-4` | road / `1-W-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-S-in-4` | road / `1-W-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-S-in-4` | road / `1-E-out-13` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-S-in-4` | road / `1-E-out-14` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-S-in-4` | road / `1-W-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-S-in-4` | road / `1-W-out-19` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-S-in-4` | road / `1-N-out-22` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-S-in-4` | road / `1-N-out-24` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |
| pedestrian / `2-S-in-4` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game outcomes are recorded separately in the test checklist. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use Windows SimCity 4 with NAM 50 and right-hand traffic, including Wine or CrossOver. Follow the [shared build guide](../../../../docs/BUILD_AND_INSTALL.md) for exact dependency hashes and the captured Avenue input. Build the `ddrhw-modular-ramp-kit` set, and prepare the `modular-diagonal-diamond` Highways menu. Building and rendering do not install game files. Use flat terrain in a disposable city, and follow the [piece placement instructions](README.md#2-piece-and-placement).

The default assembly cycles seven R40 components. The four full compact ramps and two retained compact Avenue junctions have separate buttons outside that cycle. Replace a matching ramp pair and its terminal together; the old compact grade-only types do not contain the transferred curved throats.

## 3. Software checks

Follow the [assembly software commands](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/TESTING.md#3-software-checks), including `python3 -B tools/run_tests.py` from the repository root and verification of the selected saved build. The focused family tests check exclusive construction ownership, exact retained high samples, signed slopes, the new R40 sections, the four flat R40 ground ports, and continuous texture phase. The face-partition tests specifically keep a centre pier when its old concrete mesh also contains a curved barrier bridge.

The [independent partition proof](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/evidence/straight-partition-preservation.json) compares complete assembled indexed triangles, original material bytes, UVs, winding, and per-cell PATH bytes against the immutable accepted checkpoint. Re-anchored faces use exactly one float32 translation from their old cell to their new host. The [reviewed model contract](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/checks/straight-partition-models.jsonc) binds each resulting saved model; it does not approve game behaviour.

For physical joins, compare the complete pavement, 1 m underside, Jersey profiles, and inset bridge strips at the native highway edge. For traffic, compare every exposed tile-edge port, including all four ports of each lower full ramp. Standalone model overhang is deliberate; continuous route support must be checked against the assembled model union.

## 4. Game checks

Test the new outside native approach separately from the fixed piece: place a fresh copy with clear space beyond its highway ends, inspect the native DD tile, and extend an already working NAM DD highway to that outside tile with the RealHighway drawing tool. Repeat all four placement orientations, compare both deck directions, and check Route Query, actual travel, occupied neighbours, demolition, and save/reload separately. The [network specification](../../NETWORK_SPEC.md#12-native-highway-approach-experiment) defines the exact helper coordinates and limits. These native-joining observations remain unverified.

Place this component in the complete matching assembly. Inspect the placed result after clicking, including rotations, barriers, pavement, supports, and shadows; the construction preview is a separate observation. Use Route Query on every required movement, watch a car complete it, confirm the opposite-carriageway ramp movements remain unavailable, save the city, close it, and reload it. Test the lower ramps through both intrinsic fragments and their stamp-owned middle tile.

For the stamp and Avenue terminals, extend an ordinary Avenue, develop nearby zoning, and inspect whether pedestrian pavement appears and rotates with the road. Check both pedestrian directions separately. Record only the exact service, direction, pose, and environment actually observed, following the [shared testing procedure](../../../../docs/TESTING.md).

## 5. Results and known issues

The independent partition audit passed its source-preservation comparison. That result is separate from verification of a newly saved DAT and from every human game observation in the generated checklist. The full retained high-prefix traffic centre-lines contain sampled transition minima of approximately 1.735 m on the lower ramps and 3.500 m on the upper ramps. These inherited kinks are preserved by the exact source partition; R40 describes only the new circular sections. The 30% maximum grade is a compact game experiment, rather than a normal real-world highway design limit. Every game result for these corrected resources remains unverified until an explicit matching observation is recorded.

<!-- BEGIN MANUAL SUMMARY -->

### Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/3 applicable cases passed; 0 failed, 0 stale.
- [ ] In-game rendering: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Route Query: 0/64 applicable cases passed; 0 failed, 0 stale.
- [ ] Visible travel: 0/64 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 869, passed: 0, failed: 0, stale: 0, not_applicable: 0.

#### Record an observation

Follow the [shared testing guide](../../../../docs/TESTING.md); copy [the unconfirmed example](checks/observation.example.json) to `checks/observation.json`. Case identifiers are in the expandable sections below. Do not edit generated checkboxes.

From the repository folder containing `custom-pieces`, run after filling `checks/observation.json` and explicitly confirming the exact observation:

```sh
python3 -m scp.content record --record custom-pieces/domains/highway/00_pieces/ddrhw-modular-highway-stamp/checks/manual-tests.json --observation custom-pieces/domains/highway/00_pieces/ddrhw-modular-highway-stamp/checks/observation.json
```

#### Detailed current checks

Each collapsed group shows exact case counts and states. Forbidden transfers are grouped by the directed service pair; the table inside retains every port pair and rotation.

<details>
<summary>Compiled resources — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Compiled resources**<br>Whole subject | <a href="#case-software_resources-1c233e8adbd824473999">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Compiled resources — Whole subject</summary>

<a id="case-software_resources-1c233e8adbd824473999"></a>

**General: unverified** — `software_resources-1c233e8adbd824473999`.

Verify the actual compiled resources and construction rules.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Directed routing graph — Whole subject — 1 case; unverified: 1</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Directed routing graph**<br>Whole subject | <a href="#case-software_connectivity-1c233e8adbd824473999">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Directed routing graph — Whole subject</summary>

<a id="case-software_connectivity-1c233e8adbd824473999"></a>

**General: unverified** — `software_connectivity-1c233e8adbd824473999`.

Verify the declared directed journeys and forbidden transfers.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Preview review — Images — 3 cases; unverified: 3</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-modular-highway-stamp:canonical-southeast | <a href="#case-preview_review-9bb3c44c2f5041b266ff">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-modular-highway-stamp:canonical-top | <a href="#case-preview_review-6c920606f065b904cb40">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-modular-highway-stamp:connection-overview | <a href="#case-preview_review-2c859da8ec79008b8a8c">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-modular-highway-stamp:canonical-southeast</summary>

<a id="case-preview_review-9bb3c44c2f5041b266ff"></a>

**General: unverified** — `preview_review-9bb3c44c2f5041b266ff`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-modular-highway-stamp:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-modular-highway-stamp:canonical-top</summary>

<a id="case-preview_review-6c920606f065b904cb40"></a>

**General: unverified** — `preview_review-6c920606f065b904cb40`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-modular-highway-stamp:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-modular-highway-stamp:connection-overview</summary>

<a id="case-preview_review-2c859da8ec79008b8a8c"></a>

**General: unverified** — `preview_review-2c859da8ec79008b8a8c`.

Inspect this exact preview for tracks, walls, piers, seams, and shadows.

Scope: Image: image:ddrhw-modular-highway-stamp:connection-overview.

No observation recorded.

</details>

</details>

<details>
<summary>In-game rendering — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **In-game rendering**<br>Whole subject | — | <a href="#case-in_game_render-d0ef5112f7b9929ff065">[ ] unverified</a> | <a href="#case-in_game_render-948f4ccaa6b22013b891">[ ] unverified</a> | <a href="#case-in_game_render-db38f3fb19cb92515ff3">[ ] unverified</a> | <a href="#case-in_game_render-de156c30b897b5056f5d">[ ] unverified</a> |


<details>
<summary>In-game rendering — Whole subject</summary>

<a id="case-in_game_render-d0ef5112f7b9929ff065"></a>

**0° CCW: unverified** — `in_game_render-d0ef5112f7b9929ff065`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-948f4ccaa6b22013b891"></a>

**90° CCW: unverified** — `in_game_render-948f4ccaa6b22013b891`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-db38f3fb19cb92515ff3"></a>

**180° CCW: unverified** — `in_game_render-db38f3fb19cb92515ff3`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_render-de156c30b897b5056f5d"></a>

**270° CCW: unverified** — `in_game_render-de156c30b897b5056f5d`.

Inspect the placed tracks, walls, piers, seams, and shadows in SimCity 4.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Placement — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Placement**<br>Whole subject | — | <a href="#case-in_game_placement-d0ef5112f7b9929ff065">[ ] unverified</a> | <a href="#case-in_game_placement-948f4ccaa6b22013b891">[ ] unverified</a> | <a href="#case-in_game_placement-db38f3fb19cb92515ff3">[ ] unverified</a> | <a href="#case-in_game_placement-de156c30b897b5056f5d">[ ] unverified</a> |


<details>
<summary>Placement — Whole subject</summary>

<a id="case-in_game_placement-d0ef5112f7b9929ff065"></a>

**0° CCW: unverified** — `in_game_placement-d0ef5112f7b9929ff065`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-948f4ccaa6b22013b891"></a>

**90° CCW: unverified** — `in_game_placement-948f4ccaa6b22013b891`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-db38f3fb19cb92515ff3"></a>

**180° CCW: unverified** — `in_game_placement-db38f3fb19cb92515ff3`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_placement-de156c30b897b5056f5d"></a>

**270° CCW: unverified** — `in_game_placement-de156c30b897b5056f5d`.

Place this piece or complete blueprint and inspect every occupied tile.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Demolition — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Demolition**<br>Whole subject | — | <a href="#case-in_game_demolition-d0ef5112f7b9929ff065">[ ] unverified</a> | <a href="#case-in_game_demolition-948f4ccaa6b22013b891">[ ] unverified</a> | <a href="#case-in_game_demolition-db38f3fb19cb92515ff3">[ ] unverified</a> | <a href="#case-in_game_demolition-de156c30b897b5056f5d">[ ] unverified</a> |


<details>
<summary>Demolition — Whole subject</summary>

<a id="case-in_game_demolition-d0ef5112f7b9929ff065"></a>

**0° CCW: unverified** — `in_game_demolition-d0ef5112f7b9929ff065`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-948f4ccaa6b22013b891"></a>

**90° CCW: unverified** — `in_game_demolition-948f4ccaa6b22013b891`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-db38f3fb19cb92515ff3"></a>

**180° CCW: unverified** — `in_game_demolition-db38f3fb19cb92515ff3`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_demolition-de156c30b897b5056f5d"></a>

**270° CCW: unverified** — `in_game_demolition-de156c30b897b5056f5d`.

Bulldoze the complete placement and inspect the cleared area.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Save and reload — Whole subject — 4 cases; unverified: 4</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Save and reload**<br>Whole subject | — | <a href="#case-in_game_save_reload-d0ef5112f7b9929ff065">[ ] unverified</a> | <a href="#case-in_game_save_reload-948f4ccaa6b22013b891">[ ] unverified</a> | <a href="#case-in_game_save_reload-db38f3fb19cb92515ff3">[ ] unverified</a> | <a href="#case-in_game_save_reload-de156c30b897b5056f5d">[ ] unverified</a> |


<details>
<summary>Save and reload — Whole subject</summary>

<a id="case-in_game_save_reload-d0ef5112f7b9929ff065"></a>

**0° CCW: unverified** — `in_game_save_reload-d0ef5112f7b9929ff065`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-948f4ccaa6b22013b891"></a>

**90° CCW: unverified** — `in_game_save_reload-948f4ccaa6b22013b891`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-db38f3fb19cb92515ff3"></a>

**180° CCW: unverified** — `in_game_save_reload-db38f3fb19cb92515ff3`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

<a id="case-in_game_save_reload-de156c30b897b5056f5d"></a>

**270° CCW: unverified** — `in_game_save_reload-de156c30b897b5056f5d`.

Save, quit, reload, and inspect the placement and its paths.

Scope: Whole subject.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — road — 56 cases; unverified: 56</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-6; entry: 1-W-in-2; exit: 1-E-out-6 | — | <a href="#case-in_game_route_query-970fc5a9b1d0a8c2372a">[ ] unverified</a> | <a href="#case-in_game_route_query-8d509db94c6599649552">[ ] unverified</a> | <a href="#case-in_game_route_query-c33020a3e21fae47cd95">[ ] unverified</a> | <a href="#case-in_game_route_query-cf08aa444678af25fea9">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-24; entry: 1-W-in-2; exit: 1-N-out-24 | — | <a href="#case-in_game_route_query-ea736bf530766a186dc7">[ ] unverified</a> | <a href="#case-in_game_route_query-d1ee0ad5afbe97e2fc92">[ ] unverified</a> | <a href="#case-in_game_route_query-b79bb9849726642a1ae5">[ ] unverified</a> | <a href="#case-in_game_route_query-6e153157a65d89762711">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-22; entry: 1-W-in-4; exit: 1-N-out-22 | — | <a href="#case-in_game_route_query-375af6274b377b2304e4">[ ] unverified</a> | <a href="#case-in_game_route_query-09aee0cd7aad3786bf50">[ ] unverified</a> | <a href="#case-in_game_route_query-d9f5549a8eb938cd1988">[ ] unverified</a> | <a href="#case-in_game_route_query-22589cc416ac8f0c13db">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3 | — | <a href="#case-in_game_route_query-b3c07d4ff49097bc85fb">[ ] unverified</a> | <a href="#case-in_game_route_query-297d785345889b7f1643">[ ] unverified</a> | <a href="#case-in_game_route_query-b498ad3d94fdf3097d74">[ ] unverified</a> | <a href="#case-in_game_route_query-2c4ab5415aceb2ebef89">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-8>1-W-out-7; entry: 1-N-in-8; exit: 1-W-out-7 | — | <a href="#case-in_game_route_query-9048c50964fc3ec5d5ea">[ ] unverified</a> | <a href="#case-in_game_route_query-d7da987987d33466f7f9">[ ] unverified</a> | <a href="#case-in_game_route_query-2c9f2cc0b78302d9c7e3">[ ] unverified</a> | <a href="#case-in_game_route_query-823ac4fe1a2509ea5d0d">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-9>1-E-out-13; entry: 1-N-in-9; exit: 1-E-out-13 | — | <a href="#case-in_game_route_query-6643b07010e10e7b2728">[ ] unverified</a> | <a href="#case-in_game_route_query-7e515e9ee744163342de">[ ] unverified</a> | <a href="#case-in_game_route_query-73cc9a4de064652d6d7c">[ ] unverified</a> | <a href="#case-in_game_route_query-da031238145f726f638b">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-10>1-E-out-14; entry: 1-N-in-10; exit: 1-E-out-14 | — | <a href="#case-in_game_route_query-a4b387b9926da653f8f2">[ ] unverified</a> | <a href="#case-in_game_route_query-09236388acece8d5be28">[ ] unverified</a> | <a href="#case-in_game_route_query-c35e03552b5c59a2a91e">[ ] unverified</a> | <a href="#case-in_game_route_query-bd82d282b2486f0f6f60">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-S-in-15>1-W-out-11; entry: 1-S-in-15; exit: 1-W-out-11 | — | <a href="#case-in_game_route_query-edeaa440015e64a49645">[ ] unverified</a> | <a href="#case-in_game_route_query-a7be7cd3b909e628ee0b">[ ] unverified</a> | <a href="#case-in_game_route_query-4700901cb5f5af36e088">[ ] unverified</a> | <a href="#case-in_game_route_query-0284562afef1297ecc18">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-S-in-16>1-W-out-12; entry: 1-S-in-16; exit: 1-W-out-12 | — | <a href="#case-in_game_route_query-c8257f891134eb00e196">[ ] unverified</a> | <a href="#case-in_game_route_query-1c3df1ce90676fb250f5">[ ] unverified</a> | <a href="#case-in_game_route_query-ccc0f40fc7cb9f7c5e9c">[ ] unverified</a> | <a href="#case-in_game_route_query-76579cfec570254bdf56">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-18>1-W-out-17; entry: 1-N-in-18; exit: 1-W-out-17 | — | <a href="#case-in_game_route_query-864c3239608bb3a176ac">[ ] unverified</a> | <a href="#case-in_game_route_query-b5ef7fb00c36316672cb">[ ] unverified</a> | <a href="#case-in_game_route_query-003a6735d4069924e1cb">[ ] unverified</a> | <a href="#case-in_game_route_query-69cd2bc4d6588f4e7c8c">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-S-in-20>1-N-out-24; entry: 1-S-in-20; exit: 1-N-out-24 | — | <a href="#case-in_game_route_query-e13f58f805419378832f">[ ] unverified</a> | <a href="#case-in_game_route_query-8c9be941be8b1d21bd08">[ ] unverified</a> | <a href="#case-in_game_route_query-2a8f737ff698bb97998c">[ ] unverified</a> | <a href="#case-in_game_route_query-37406708057d98863fdf">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-21>1-W-out-19; entry: 1-N-in-21; exit: 1-W-out-19 | — | <a href="#case-in_game_route_query-0fe9a5dad2450703e682">[ ] unverified</a> | <a href="#case-in_game_route_query-058d0189ad8f0cb58c67">[ ] unverified</a> | <a href="#case-in_game_route_query-2a24f120fd16495e169f">[ ] unverified</a> | <a href="#case-in_game_route_query-63f10337dae06413c93e">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-21>1-W-out-3; entry: 1-N-in-21; exit: 1-W-out-3 | — | <a href="#case-in_game_route_query-39bb346ad5203198d834">[ ] unverified</a> | <a href="#case-in_game_route_query-8c2fbd9233e5d1c6fe80">[ ] unverified</a> | <a href="#case-in_game_route_query-76b1c6c7872b554cce80">[ ] unverified</a> | <a href="#case-in_game_route_query-e41c12785a6e71fab6c6">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-23>1-W-out-1; entry: 1-N-in-23; exit: 1-W-out-1 | — | <a href="#case-in_game_route_query-68ad13375629ad70fd5c">[ ] unverified</a> | <a href="#case-in_game_route_query-e65b394b6853d6654532">[ ] unverified</a> | <a href="#case-in_game_route_query-0470854de108f8804b54">[ ] unverified</a> | <a href="#case-in_game_route_query-34d43125977816f23eaf">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-6; entry: 1-W-in-2; exit: 1-E-out-6</summary>

<a id="case-in_game_route_query-970fc5a9b1d0a8c2372a"></a>

**0° CCW: unverified** — `in_game_route_query-970fc5a9b1d0a8c2372a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-6; entry: 1-W-in-2; exit: 1-E-out-6.

No observation recorded.

<a id="case-in_game_route_query-8d509db94c6599649552"></a>

**90° CCW: unverified** — `in_game_route_query-8d509db94c6599649552`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-6; entry: 1-W-in-2; exit: 1-E-out-6.

No observation recorded.

<a id="case-in_game_route_query-c33020a3e21fae47cd95"></a>

**180° CCW: unverified** — `in_game_route_query-c33020a3e21fae47cd95`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-6; entry: 1-W-in-2; exit: 1-E-out-6.

No observation recorded.

<a id="case-in_game_route_query-cf08aa444678af25fea9"></a>

**270° CCW: unverified** — `in_game_route_query-cf08aa444678af25fea9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-6; entry: 1-W-in-2; exit: 1-E-out-6.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-24; entry: 1-W-in-2; exit: 1-N-out-24</summary>

<a id="case-in_game_route_query-ea736bf530766a186dc7"></a>

**0° CCW: unverified** — `in_game_route_query-ea736bf530766a186dc7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-24; entry: 1-W-in-2; exit: 1-N-out-24.

No observation recorded.

<a id="case-in_game_route_query-d1ee0ad5afbe97e2fc92"></a>

**90° CCW: unverified** — `in_game_route_query-d1ee0ad5afbe97e2fc92`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-24; entry: 1-W-in-2; exit: 1-N-out-24.

No observation recorded.

<a id="case-in_game_route_query-b79bb9849726642a1ae5"></a>

**180° CCW: unverified** — `in_game_route_query-b79bb9849726642a1ae5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-24; entry: 1-W-in-2; exit: 1-N-out-24.

No observation recorded.

<a id="case-in_game_route_query-6e153157a65d89762711"></a>

**270° CCW: unverified** — `in_game_route_query-6e153157a65d89762711`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-24; entry: 1-W-in-2; exit: 1-N-out-24.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-22; entry: 1-W-in-4; exit: 1-N-out-22</summary>

<a id="case-in_game_route_query-375af6274b377b2304e4"></a>

**0° CCW: unverified** — `in_game_route_query-375af6274b377b2304e4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-22; entry: 1-W-in-4; exit: 1-N-out-22.

No observation recorded.

<a id="case-in_game_route_query-09aee0cd7aad3786bf50"></a>

**90° CCW: unverified** — `in_game_route_query-09aee0cd7aad3786bf50`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-22; entry: 1-W-in-4; exit: 1-N-out-22.

No observation recorded.

<a id="case-in_game_route_query-d9f5549a8eb938cd1988"></a>

**180° CCW: unverified** — `in_game_route_query-d9f5549a8eb938cd1988`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-22; entry: 1-W-in-4; exit: 1-N-out-22.

No observation recorded.

<a id="case-in_game_route_query-22589cc416ac8f0c13db"></a>

**270° CCW: unverified** — `in_game_route_query-22589cc416ac8f0c13db`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-22; entry: 1-W-in-4; exit: 1-N-out-22.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3</summary>

<a id="case-in_game_route_query-b3c07d4ff49097bc85fb"></a>

**0° CCW: unverified** — `in_game_route_query-b3c07d4ff49097bc85fb`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_route_query-297d785345889b7f1643"></a>

**90° CCW: unverified** — `in_game_route_query-297d785345889b7f1643`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_route_query-b498ad3d94fdf3097d74"></a>

**180° CCW: unverified** — `in_game_route_query-b498ad3d94fdf3097d74`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_route_query-2c4ab5415aceb2ebef89"></a>

**270° CCW: unverified** — `in_game_route_query-2c4ab5415aceb2ebef89`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-8>1-W-out-7; entry: 1-N-in-8; exit: 1-W-out-7</summary>

<a id="case-in_game_route_query-9048c50964fc3ec5d5ea"></a>

**0° CCW: unverified** — `in_game_route_query-9048c50964fc3ec5d5ea`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-8>1-W-out-7; entry: 1-N-in-8; exit: 1-W-out-7.

No observation recorded.

<a id="case-in_game_route_query-d7da987987d33466f7f9"></a>

**90° CCW: unverified** — `in_game_route_query-d7da987987d33466f7f9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-8>1-W-out-7; entry: 1-N-in-8; exit: 1-W-out-7.

No observation recorded.

<a id="case-in_game_route_query-2c9f2cc0b78302d9c7e3"></a>

**180° CCW: unverified** — `in_game_route_query-2c9f2cc0b78302d9c7e3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-8>1-W-out-7; entry: 1-N-in-8; exit: 1-W-out-7.

No observation recorded.

<a id="case-in_game_route_query-823ac4fe1a2509ea5d0d"></a>

**270° CCW: unverified** — `in_game_route_query-823ac4fe1a2509ea5d0d`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-8>1-W-out-7; entry: 1-N-in-8; exit: 1-W-out-7.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-9>1-E-out-13; entry: 1-N-in-9; exit: 1-E-out-13</summary>

<a id="case-in_game_route_query-6643b07010e10e7b2728"></a>

**0° CCW: unverified** — `in_game_route_query-6643b07010e10e7b2728`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-9>1-E-out-13; entry: 1-N-in-9; exit: 1-E-out-13.

No observation recorded.

<a id="case-in_game_route_query-7e515e9ee744163342de"></a>

**90° CCW: unverified** — `in_game_route_query-7e515e9ee744163342de`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-9>1-E-out-13; entry: 1-N-in-9; exit: 1-E-out-13.

No observation recorded.

<a id="case-in_game_route_query-73cc9a4de064652d6d7c"></a>

**180° CCW: unverified** — `in_game_route_query-73cc9a4de064652d6d7c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-9>1-E-out-13; entry: 1-N-in-9; exit: 1-E-out-13.

No observation recorded.

<a id="case-in_game_route_query-da031238145f726f638b"></a>

**270° CCW: unverified** — `in_game_route_query-da031238145f726f638b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-9>1-E-out-13; entry: 1-N-in-9; exit: 1-E-out-13.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-10>1-E-out-14; entry: 1-N-in-10; exit: 1-E-out-14</summary>

<a id="case-in_game_route_query-a4b387b9926da653f8f2"></a>

**0° CCW: unverified** — `in_game_route_query-a4b387b9926da653f8f2`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-10>1-E-out-14; entry: 1-N-in-10; exit: 1-E-out-14.

No observation recorded.

<a id="case-in_game_route_query-09236388acece8d5be28"></a>

**90° CCW: unverified** — `in_game_route_query-09236388acece8d5be28`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-10>1-E-out-14; entry: 1-N-in-10; exit: 1-E-out-14.

No observation recorded.

<a id="case-in_game_route_query-c35e03552b5c59a2a91e"></a>

**180° CCW: unverified** — `in_game_route_query-c35e03552b5c59a2a91e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-10>1-E-out-14; entry: 1-N-in-10; exit: 1-E-out-14.

No observation recorded.

<a id="case-in_game_route_query-bd82d282b2486f0f6f60"></a>

**270° CCW: unverified** — `in_game_route_query-bd82d282b2486f0f6f60`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-10>1-E-out-14; entry: 1-N-in-10; exit: 1-E-out-14.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-S-in-15>1-W-out-11; entry: 1-S-in-15; exit: 1-W-out-11</summary>

<a id="case-in_game_route_query-edeaa440015e64a49645"></a>

**0° CCW: unverified** — `in_game_route_query-edeaa440015e64a49645`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-15>1-W-out-11; entry: 1-S-in-15; exit: 1-W-out-11.

No observation recorded.

<a id="case-in_game_route_query-a7be7cd3b909e628ee0b"></a>

**90° CCW: unverified** — `in_game_route_query-a7be7cd3b909e628ee0b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-15>1-W-out-11; entry: 1-S-in-15; exit: 1-W-out-11.

No observation recorded.

<a id="case-in_game_route_query-4700901cb5f5af36e088"></a>

**180° CCW: unverified** — `in_game_route_query-4700901cb5f5af36e088`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-15>1-W-out-11; entry: 1-S-in-15; exit: 1-W-out-11.

No observation recorded.

<a id="case-in_game_route_query-0284562afef1297ecc18"></a>

**270° CCW: unverified** — `in_game_route_query-0284562afef1297ecc18`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-15>1-W-out-11; entry: 1-S-in-15; exit: 1-W-out-11.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-S-in-16>1-W-out-12; entry: 1-S-in-16; exit: 1-W-out-12</summary>

<a id="case-in_game_route_query-c8257f891134eb00e196"></a>

**0° CCW: unverified** — `in_game_route_query-c8257f891134eb00e196`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-16>1-W-out-12; entry: 1-S-in-16; exit: 1-W-out-12.

No observation recorded.

<a id="case-in_game_route_query-1c3df1ce90676fb250f5"></a>

**90° CCW: unverified** — `in_game_route_query-1c3df1ce90676fb250f5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-16>1-W-out-12; entry: 1-S-in-16; exit: 1-W-out-12.

No observation recorded.

<a id="case-in_game_route_query-ccc0f40fc7cb9f7c5e9c"></a>

**180° CCW: unverified** — `in_game_route_query-ccc0f40fc7cb9f7c5e9c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-16>1-W-out-12; entry: 1-S-in-16; exit: 1-W-out-12.

No observation recorded.

<a id="case-in_game_route_query-76579cfec570254bdf56"></a>

**270° CCW: unverified** — `in_game_route_query-76579cfec570254bdf56`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-16>1-W-out-12; entry: 1-S-in-16; exit: 1-W-out-12.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-18>1-W-out-17; entry: 1-N-in-18; exit: 1-W-out-17</summary>

<a id="case-in_game_route_query-864c3239608bb3a176ac"></a>

**0° CCW: unverified** — `in_game_route_query-864c3239608bb3a176ac`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-18>1-W-out-17; entry: 1-N-in-18; exit: 1-W-out-17.

No observation recorded.

<a id="case-in_game_route_query-b5ef7fb00c36316672cb"></a>

**90° CCW: unverified** — `in_game_route_query-b5ef7fb00c36316672cb`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-18>1-W-out-17; entry: 1-N-in-18; exit: 1-W-out-17.

No observation recorded.

<a id="case-in_game_route_query-003a6735d4069924e1cb"></a>

**180° CCW: unverified** — `in_game_route_query-003a6735d4069924e1cb`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-18>1-W-out-17; entry: 1-N-in-18; exit: 1-W-out-17.

No observation recorded.

<a id="case-in_game_route_query-69cd2bc4d6588f4e7c8c"></a>

**270° CCW: unverified** — `in_game_route_query-69cd2bc4d6588f4e7c8c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-18>1-W-out-17; entry: 1-N-in-18; exit: 1-W-out-17.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-S-in-20>1-N-out-24; entry: 1-S-in-20; exit: 1-N-out-24</summary>

<a id="case-in_game_route_query-e13f58f805419378832f"></a>

**0° CCW: unverified** — `in_game_route_query-e13f58f805419378832f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-20>1-N-out-24; entry: 1-S-in-20; exit: 1-N-out-24.

No observation recorded.

<a id="case-in_game_route_query-8c9be941be8b1d21bd08"></a>

**90° CCW: unverified** — `in_game_route_query-8c9be941be8b1d21bd08`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-20>1-N-out-24; entry: 1-S-in-20; exit: 1-N-out-24.

No observation recorded.

<a id="case-in_game_route_query-2a8f737ff698bb97998c"></a>

**180° CCW: unverified** — `in_game_route_query-2a8f737ff698bb97998c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-20>1-N-out-24; entry: 1-S-in-20; exit: 1-N-out-24.

No observation recorded.

<a id="case-in_game_route_query-37406708057d98863fdf"></a>

**270° CCW: unverified** — `in_game_route_query-37406708057d98863fdf`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-20>1-N-out-24; entry: 1-S-in-20; exit: 1-N-out-24.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-21>1-W-out-19; entry: 1-N-in-21; exit: 1-W-out-19</summary>

<a id="case-in_game_route_query-0fe9a5dad2450703e682"></a>

**0° CCW: unverified** — `in_game_route_query-0fe9a5dad2450703e682`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-21>1-W-out-19; entry: 1-N-in-21; exit: 1-W-out-19.

No observation recorded.

<a id="case-in_game_route_query-058d0189ad8f0cb58c67"></a>

**90° CCW: unverified** — `in_game_route_query-058d0189ad8f0cb58c67`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-21>1-W-out-19; entry: 1-N-in-21; exit: 1-W-out-19.

No observation recorded.

<a id="case-in_game_route_query-2a24f120fd16495e169f"></a>

**180° CCW: unverified** — `in_game_route_query-2a24f120fd16495e169f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-21>1-W-out-19; entry: 1-N-in-21; exit: 1-W-out-19.

No observation recorded.

<a id="case-in_game_route_query-63f10337dae06413c93e"></a>

**270° CCW: unverified** — `in_game_route_query-63f10337dae06413c93e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-21>1-W-out-19; entry: 1-N-in-21; exit: 1-W-out-19.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-21>1-W-out-3; entry: 1-N-in-21; exit: 1-W-out-3</summary>

<a id="case-in_game_route_query-39bb346ad5203198d834"></a>

**0° CCW: unverified** — `in_game_route_query-39bb346ad5203198d834`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-21>1-W-out-3; entry: 1-N-in-21; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_route_query-8c2fbd9233e5d1c6fe80"></a>

**90° CCW: unverified** — `in_game_route_query-8c2fbd9233e5d1c6fe80`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-21>1-W-out-3; entry: 1-N-in-21; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_route_query-76b1c6c7872b554cce80"></a>

**180° CCW: unverified** — `in_game_route_query-76b1c6c7872b554cce80`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-21>1-W-out-3; entry: 1-N-in-21; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_route_query-e41c12785a6e71fab6c6"></a>

**270° CCW: unverified** — `in_game_route_query-e41c12785a6e71fab6c6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-21>1-W-out-3; entry: 1-N-in-21; exit: 1-W-out-3.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-23>1-W-out-1; entry: 1-N-in-23; exit: 1-W-out-1</summary>

<a id="case-in_game_route_query-68ad13375629ad70fd5c"></a>

**0° CCW: unverified** — `in_game_route_query-68ad13375629ad70fd5c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-23>1-W-out-1; entry: 1-N-in-23; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_route_query-e65b394b6853d6654532"></a>

**90° CCW: unverified** — `in_game_route_query-e65b394b6853d6654532`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-23>1-W-out-1; entry: 1-N-in-23; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_route_query-0470854de108f8804b54"></a>

**180° CCW: unverified** — `in_game_route_query-0470854de108f8804b54`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-23>1-W-out-1; entry: 1-N-in-23; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_route_query-34d43125977816f23eaf"></a>

**270° CCW: unverified** — `in_game_route_query-34d43125977816f23eaf`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-23>1-W-out-1; entry: 1-N-in-23; exit: 1-W-out-1.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 56 cases; unverified: 56</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-6; entry: 1-W-in-2; exit: 1-E-out-6 | — | <a href="#case-in_game_visible_travel-970fc5a9b1d0a8c2372a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8d509db94c6599649552">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c33020a3e21fae47cd95">[ ] unverified</a> | <a href="#case-in_game_visible_travel-cf08aa444678af25fea9">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-24; entry: 1-W-in-2; exit: 1-N-out-24 | — | <a href="#case-in_game_visible_travel-ea736bf530766a186dc7">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d1ee0ad5afbe97e2fc92">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b79bb9849726642a1ae5">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6e153157a65d89762711">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-22; entry: 1-W-in-4; exit: 1-N-out-22 | — | <a href="#case-in_game_visible_travel-375af6274b377b2304e4">[ ] unverified</a> | <a href="#case-in_game_visible_travel-09aee0cd7aad3786bf50">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d9f5549a8eb938cd1988">[ ] unverified</a> | <a href="#case-in_game_visible_travel-22589cc416ac8f0c13db">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3 | — | <a href="#case-in_game_visible_travel-b3c07d4ff49097bc85fb">[ ] unverified</a> | <a href="#case-in_game_visible_travel-297d785345889b7f1643">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b498ad3d94fdf3097d74">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2c4ab5415aceb2ebef89">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-8>1-W-out-7; entry: 1-N-in-8; exit: 1-W-out-7 | — | <a href="#case-in_game_visible_travel-9048c50964fc3ec5d5ea">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d7da987987d33466f7f9">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2c9f2cc0b78302d9c7e3">[ ] unverified</a> | <a href="#case-in_game_visible_travel-823ac4fe1a2509ea5d0d">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-9>1-E-out-13; entry: 1-N-in-9; exit: 1-E-out-13 | — | <a href="#case-in_game_visible_travel-6643b07010e10e7b2728">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7e515e9ee744163342de">[ ] unverified</a> | <a href="#case-in_game_visible_travel-73cc9a4de064652d6d7c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-da031238145f726f638b">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-10>1-E-out-14; entry: 1-N-in-10; exit: 1-E-out-14 | — | <a href="#case-in_game_visible_travel-a4b387b9926da653f8f2">[ ] unverified</a> | <a href="#case-in_game_visible_travel-09236388acece8d5be28">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c35e03552b5c59a2a91e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-bd82d282b2486f0f6f60">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-S-in-15>1-W-out-11; entry: 1-S-in-15; exit: 1-W-out-11 | — | <a href="#case-in_game_visible_travel-edeaa440015e64a49645">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a7be7cd3b909e628ee0b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4700901cb5f5af36e088">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0284562afef1297ecc18">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-S-in-16>1-W-out-12; entry: 1-S-in-16; exit: 1-W-out-12 | — | <a href="#case-in_game_visible_travel-c8257f891134eb00e196">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1c3df1ce90676fb250f5">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ccc0f40fc7cb9f7c5e9c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-76579cfec570254bdf56">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-18>1-W-out-17; entry: 1-N-in-18; exit: 1-W-out-17 | — | <a href="#case-in_game_visible_travel-864c3239608bb3a176ac">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b5ef7fb00c36316672cb">[ ] unverified</a> | <a href="#case-in_game_visible_travel-003a6735d4069924e1cb">[ ] unverified</a> | <a href="#case-in_game_visible_travel-69cd2bc4d6588f4e7c8c">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-S-in-20>1-N-out-24; entry: 1-S-in-20; exit: 1-N-out-24 | — | <a href="#case-in_game_visible_travel-e13f58f805419378832f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8c9be941be8b1d21bd08">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2a8f737ff698bb97998c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-37406708057d98863fdf">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-21>1-W-out-19; entry: 1-N-in-21; exit: 1-W-out-19 | — | <a href="#case-in_game_visible_travel-0fe9a5dad2450703e682">[ ] unverified</a> | <a href="#case-in_game_visible_travel-058d0189ad8f0cb58c67">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2a24f120fd16495e169f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-63f10337dae06413c93e">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-21>1-W-out-3; entry: 1-N-in-21; exit: 1-W-out-3 | — | <a href="#case-in_game_visible_travel-39bb346ad5203198d834">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8c2fbd9233e5d1c6fe80">[ ] unverified</a> | <a href="#case-in_game_visible_travel-76b1c6c7872b554cce80">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e41c12785a6e71fab6c6">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-23>1-W-out-1; entry: 1-N-in-23; exit: 1-W-out-1 | — | <a href="#case-in_game_visible_travel-68ad13375629ad70fd5c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e65b394b6853d6654532">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0470854de108f8804b54">[ ] unverified</a> | <a href="#case-in_game_visible_travel-34d43125977816f23eaf">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-6; entry: 1-W-in-2; exit: 1-E-out-6</summary>

<a id="case-in_game_visible_travel-970fc5a9b1d0a8c2372a"></a>

**0° CCW: unverified** — `in_game_visible_travel-970fc5a9b1d0a8c2372a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-6; entry: 1-W-in-2; exit: 1-E-out-6.

No observation recorded.

<a id="case-in_game_visible_travel-8d509db94c6599649552"></a>

**90° CCW: unverified** — `in_game_visible_travel-8d509db94c6599649552`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-6; entry: 1-W-in-2; exit: 1-E-out-6.

No observation recorded.

<a id="case-in_game_visible_travel-c33020a3e21fae47cd95"></a>

**180° CCW: unverified** — `in_game_visible_travel-c33020a3e21fae47cd95`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-6; entry: 1-W-in-2; exit: 1-E-out-6.

No observation recorded.

<a id="case-in_game_visible_travel-cf08aa444678af25fea9"></a>

**270° CCW: unverified** — `in_game_visible_travel-cf08aa444678af25fea9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-6; entry: 1-W-in-2; exit: 1-E-out-6.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-24; entry: 1-W-in-2; exit: 1-N-out-24</summary>

<a id="case-in_game_visible_travel-ea736bf530766a186dc7"></a>

**0° CCW: unverified** — `in_game_visible_travel-ea736bf530766a186dc7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-24; entry: 1-W-in-2; exit: 1-N-out-24.

No observation recorded.

<a id="case-in_game_visible_travel-d1ee0ad5afbe97e2fc92"></a>

**90° CCW: unverified** — `in_game_visible_travel-d1ee0ad5afbe97e2fc92`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-24; entry: 1-W-in-2; exit: 1-N-out-24.

No observation recorded.

<a id="case-in_game_visible_travel-b79bb9849726642a1ae5"></a>

**180° CCW: unverified** — `in_game_visible_travel-b79bb9849726642a1ae5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-24; entry: 1-W-in-2; exit: 1-N-out-24.

No observation recorded.

<a id="case-in_game_visible_travel-6e153157a65d89762711"></a>

**270° CCW: unverified** — `in_game_visible_travel-6e153157a65d89762711`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-24; entry: 1-W-in-2; exit: 1-N-out-24.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-22; entry: 1-W-in-4; exit: 1-N-out-22</summary>

<a id="case-in_game_visible_travel-375af6274b377b2304e4"></a>

**0° CCW: unverified** — `in_game_visible_travel-375af6274b377b2304e4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-22; entry: 1-W-in-4; exit: 1-N-out-22.

No observation recorded.

<a id="case-in_game_visible_travel-09aee0cd7aad3786bf50"></a>

**90° CCW: unverified** — `in_game_visible_travel-09aee0cd7aad3786bf50`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-22; entry: 1-W-in-4; exit: 1-N-out-22.

No observation recorded.

<a id="case-in_game_visible_travel-d9f5549a8eb938cd1988"></a>

**180° CCW: unverified** — `in_game_visible_travel-d9f5549a8eb938cd1988`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-22; entry: 1-W-in-4; exit: 1-N-out-22.

No observation recorded.

<a id="case-in_game_visible_travel-22589cc416ac8f0c13db"></a>

**270° CCW: unverified** — `in_game_visible_travel-22589cc416ac8f0c13db`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-22; entry: 1-W-in-4; exit: 1-N-out-22.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3</summary>

<a id="case-in_game_visible_travel-b3c07d4ff49097bc85fb"></a>

**0° CCW: unverified** — `in_game_visible_travel-b3c07d4ff49097bc85fb`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-297d785345889b7f1643"></a>

**90° CCW: unverified** — `in_game_visible_travel-297d785345889b7f1643`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-b498ad3d94fdf3097d74"></a>

**180° CCW: unverified** — `in_game_visible_travel-b498ad3d94fdf3097d74`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-2c4ab5415aceb2ebef89"></a>

**270° CCW: unverified** — `in_game_visible_travel-2c4ab5415aceb2ebef89`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-8>1-W-out-7; entry: 1-N-in-8; exit: 1-W-out-7</summary>

<a id="case-in_game_visible_travel-9048c50964fc3ec5d5ea"></a>

**0° CCW: unverified** — `in_game_visible_travel-9048c50964fc3ec5d5ea`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-8>1-W-out-7; entry: 1-N-in-8; exit: 1-W-out-7.

No observation recorded.

<a id="case-in_game_visible_travel-d7da987987d33466f7f9"></a>

**90° CCW: unverified** — `in_game_visible_travel-d7da987987d33466f7f9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-8>1-W-out-7; entry: 1-N-in-8; exit: 1-W-out-7.

No observation recorded.

<a id="case-in_game_visible_travel-2c9f2cc0b78302d9c7e3"></a>

**180° CCW: unverified** — `in_game_visible_travel-2c9f2cc0b78302d9c7e3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-8>1-W-out-7; entry: 1-N-in-8; exit: 1-W-out-7.

No observation recorded.

<a id="case-in_game_visible_travel-823ac4fe1a2509ea5d0d"></a>

**270° CCW: unverified** — `in_game_visible_travel-823ac4fe1a2509ea5d0d`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-8>1-W-out-7; entry: 1-N-in-8; exit: 1-W-out-7.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-9>1-E-out-13; entry: 1-N-in-9; exit: 1-E-out-13</summary>

<a id="case-in_game_visible_travel-6643b07010e10e7b2728"></a>

**0° CCW: unverified** — `in_game_visible_travel-6643b07010e10e7b2728`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-9>1-E-out-13; entry: 1-N-in-9; exit: 1-E-out-13.

No observation recorded.

<a id="case-in_game_visible_travel-7e515e9ee744163342de"></a>

**90° CCW: unverified** — `in_game_visible_travel-7e515e9ee744163342de`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-9>1-E-out-13; entry: 1-N-in-9; exit: 1-E-out-13.

No observation recorded.

<a id="case-in_game_visible_travel-73cc9a4de064652d6d7c"></a>

**180° CCW: unverified** — `in_game_visible_travel-73cc9a4de064652d6d7c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-9>1-E-out-13; entry: 1-N-in-9; exit: 1-E-out-13.

No observation recorded.

<a id="case-in_game_visible_travel-da031238145f726f638b"></a>

**270° CCW: unverified** — `in_game_visible_travel-da031238145f726f638b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-9>1-E-out-13; entry: 1-N-in-9; exit: 1-E-out-13.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-10>1-E-out-14; entry: 1-N-in-10; exit: 1-E-out-14</summary>

<a id="case-in_game_visible_travel-a4b387b9926da653f8f2"></a>

**0° CCW: unverified** — `in_game_visible_travel-a4b387b9926da653f8f2`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-10>1-E-out-14; entry: 1-N-in-10; exit: 1-E-out-14.

No observation recorded.

<a id="case-in_game_visible_travel-09236388acece8d5be28"></a>

**90° CCW: unverified** — `in_game_visible_travel-09236388acece8d5be28`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-10>1-E-out-14; entry: 1-N-in-10; exit: 1-E-out-14.

No observation recorded.

<a id="case-in_game_visible_travel-c35e03552b5c59a2a91e"></a>

**180° CCW: unverified** — `in_game_visible_travel-c35e03552b5c59a2a91e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-10>1-E-out-14; entry: 1-N-in-10; exit: 1-E-out-14.

No observation recorded.

<a id="case-in_game_visible_travel-bd82d282b2486f0f6f60"></a>

**270° CCW: unverified** — `in_game_visible_travel-bd82d282b2486f0f6f60`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-10>1-E-out-14; entry: 1-N-in-10; exit: 1-E-out-14.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-S-in-15>1-W-out-11; entry: 1-S-in-15; exit: 1-W-out-11</summary>

<a id="case-in_game_visible_travel-edeaa440015e64a49645"></a>

**0° CCW: unverified** — `in_game_visible_travel-edeaa440015e64a49645`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-15>1-W-out-11; entry: 1-S-in-15; exit: 1-W-out-11.

No observation recorded.

<a id="case-in_game_visible_travel-a7be7cd3b909e628ee0b"></a>

**90° CCW: unverified** — `in_game_visible_travel-a7be7cd3b909e628ee0b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-15>1-W-out-11; entry: 1-S-in-15; exit: 1-W-out-11.

No observation recorded.

<a id="case-in_game_visible_travel-4700901cb5f5af36e088"></a>

**180° CCW: unverified** — `in_game_visible_travel-4700901cb5f5af36e088`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-15>1-W-out-11; entry: 1-S-in-15; exit: 1-W-out-11.

No observation recorded.

<a id="case-in_game_visible_travel-0284562afef1297ecc18"></a>

**270° CCW: unverified** — `in_game_visible_travel-0284562afef1297ecc18`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-15>1-W-out-11; entry: 1-S-in-15; exit: 1-W-out-11.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-S-in-16>1-W-out-12; entry: 1-S-in-16; exit: 1-W-out-12</summary>

<a id="case-in_game_visible_travel-c8257f891134eb00e196"></a>

**0° CCW: unverified** — `in_game_visible_travel-c8257f891134eb00e196`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-16>1-W-out-12; entry: 1-S-in-16; exit: 1-W-out-12.

No observation recorded.

<a id="case-in_game_visible_travel-1c3df1ce90676fb250f5"></a>

**90° CCW: unverified** — `in_game_visible_travel-1c3df1ce90676fb250f5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-16>1-W-out-12; entry: 1-S-in-16; exit: 1-W-out-12.

No observation recorded.

<a id="case-in_game_visible_travel-ccc0f40fc7cb9f7c5e9c"></a>

**180° CCW: unverified** — `in_game_visible_travel-ccc0f40fc7cb9f7c5e9c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-16>1-W-out-12; entry: 1-S-in-16; exit: 1-W-out-12.

No observation recorded.

<a id="case-in_game_visible_travel-76579cfec570254bdf56"></a>

**270° CCW: unverified** — `in_game_visible_travel-76579cfec570254bdf56`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-16>1-W-out-12; entry: 1-S-in-16; exit: 1-W-out-12.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-18>1-W-out-17; entry: 1-N-in-18; exit: 1-W-out-17</summary>

<a id="case-in_game_visible_travel-864c3239608bb3a176ac"></a>

**0° CCW: unverified** — `in_game_visible_travel-864c3239608bb3a176ac`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-18>1-W-out-17; entry: 1-N-in-18; exit: 1-W-out-17.

No observation recorded.

<a id="case-in_game_visible_travel-b5ef7fb00c36316672cb"></a>

**90° CCW: unverified** — `in_game_visible_travel-b5ef7fb00c36316672cb`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-18>1-W-out-17; entry: 1-N-in-18; exit: 1-W-out-17.

No observation recorded.

<a id="case-in_game_visible_travel-003a6735d4069924e1cb"></a>

**180° CCW: unverified** — `in_game_visible_travel-003a6735d4069924e1cb`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-18>1-W-out-17; entry: 1-N-in-18; exit: 1-W-out-17.

No observation recorded.

<a id="case-in_game_visible_travel-69cd2bc4d6588f4e7c8c"></a>

**270° CCW: unverified** — `in_game_visible_travel-69cd2bc4d6588f4e7c8c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-18>1-W-out-17; entry: 1-N-in-18; exit: 1-W-out-17.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-S-in-20>1-N-out-24; entry: 1-S-in-20; exit: 1-N-out-24</summary>

<a id="case-in_game_visible_travel-e13f58f805419378832f"></a>

**0° CCW: unverified** — `in_game_visible_travel-e13f58f805419378832f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-20>1-N-out-24; entry: 1-S-in-20; exit: 1-N-out-24.

No observation recorded.

<a id="case-in_game_visible_travel-8c9be941be8b1d21bd08"></a>

**90° CCW: unverified** — `in_game_visible_travel-8c9be941be8b1d21bd08`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-20>1-N-out-24; entry: 1-S-in-20; exit: 1-N-out-24.

No observation recorded.

<a id="case-in_game_visible_travel-2a8f737ff698bb97998c"></a>

**180° CCW: unverified** — `in_game_visible_travel-2a8f737ff698bb97998c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-20>1-N-out-24; entry: 1-S-in-20; exit: 1-N-out-24.

No observation recorded.

<a id="case-in_game_visible_travel-37406708057d98863fdf"></a>

**270° CCW: unverified** — `in_game_visible_travel-37406708057d98863fdf`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-20>1-N-out-24; entry: 1-S-in-20; exit: 1-N-out-24.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-21>1-W-out-19; entry: 1-N-in-21; exit: 1-W-out-19</summary>

<a id="case-in_game_visible_travel-0fe9a5dad2450703e682"></a>

**0° CCW: unverified** — `in_game_visible_travel-0fe9a5dad2450703e682`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-21>1-W-out-19; entry: 1-N-in-21; exit: 1-W-out-19.

No observation recorded.

<a id="case-in_game_visible_travel-058d0189ad8f0cb58c67"></a>

**90° CCW: unverified** — `in_game_visible_travel-058d0189ad8f0cb58c67`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-21>1-W-out-19; entry: 1-N-in-21; exit: 1-W-out-19.

No observation recorded.

<a id="case-in_game_visible_travel-2a24f120fd16495e169f"></a>

**180° CCW: unverified** — `in_game_visible_travel-2a24f120fd16495e169f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-21>1-W-out-19; entry: 1-N-in-21; exit: 1-W-out-19.

No observation recorded.

<a id="case-in_game_visible_travel-63f10337dae06413c93e"></a>

**270° CCW: unverified** — `in_game_visible_travel-63f10337dae06413c93e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-21>1-W-out-19; entry: 1-N-in-21; exit: 1-W-out-19.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-21>1-W-out-3; entry: 1-N-in-21; exit: 1-W-out-3</summary>

<a id="case-in_game_visible_travel-39bb346ad5203198d834"></a>

**0° CCW: unverified** — `in_game_visible_travel-39bb346ad5203198d834`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-21>1-W-out-3; entry: 1-N-in-21; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-8c2fbd9233e5d1c6fe80"></a>

**90° CCW: unverified** — `in_game_visible_travel-8c2fbd9233e5d1c6fe80`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-21>1-W-out-3; entry: 1-N-in-21; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-76b1c6c7872b554cce80"></a>

**180° CCW: unverified** — `in_game_visible_travel-76b1c6c7872b554cce80`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-21>1-W-out-3; entry: 1-N-in-21; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-e41c12785a6e71fab6c6"></a>

**270° CCW: unverified** — `in_game_visible_travel-e41c12785a6e71fab6c6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-21>1-W-out-3; entry: 1-N-in-21; exit: 1-W-out-3.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-23>1-W-out-1; entry: 1-N-in-23; exit: 1-W-out-1</summary>

<a id="case-in_game_visible_travel-68ad13375629ad70fd5c"></a>

**0° CCW: unverified** — `in_game_visible_travel-68ad13375629ad70fd5c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-23>1-W-out-1; entry: 1-N-in-23; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-e65b394b6853d6654532"></a>

**90° CCW: unverified** — `in_game_visible_travel-e65b394b6853d6654532`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-23>1-W-out-1; entry: 1-N-in-23; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-0470854de108f8804b54"></a>

**180° CCW: unverified** — `in_game_visible_travel-0470854de108f8804b54`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-23>1-W-out-1; entry: 1-N-in-23; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-34d43125977816f23eaf"></a>

**270° CCW: unverified** — `in_game_visible_travel-34d43125977816f23eaf`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-23>1-W-out-1; entry: 1-N-in-23; exit: 1-W-out-1.

No observation recorded.

</details>

</details>

<details>
<summary>Route Query — pedestrian — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: pedestrian; role: primary; journey: 2:2-N-in-1>2-E-out-3; entry: 2-N-in-1; exit: 2-E-out-3 | — | <a href="#case-in_game_route_query-4d3847a380323c3058a3">[ ] unverified</a> | <a href="#case-in_game_route_query-4633f89bb655cfead938">[ ] unverified</a> | <a href="#case-in_game_route_query-9e656b7381bba1896360">[ ] unverified</a> | <a href="#case-in_game_route_query-c67f7261c73dd19ec1b1">[ ] unverified</a> |
| **Route Query**<br>Service: pedestrian; role: primary; journey: 2:2-S-in-4>2-W-out-2; entry: 2-S-in-4; exit: 2-W-out-2 | — | <a href="#case-in_game_route_query-74bff4e9f001a185c0cf">[ ] unverified</a> | <a href="#case-in_game_route_query-cce2e6e47030eec349a7">[ ] unverified</a> | <a href="#case-in_game_route_query-27a4609216b8e127e3c8">[ ] unverified</a> | <a href="#case-in_game_route_query-adc5a39cc7f9f0c0f523">[ ] unverified</a> |


<details>
<summary>Route Query — Service: pedestrian; role: primary; journey: 2:2-N-in-1>2-E-out-3; entry: 2-N-in-1; exit: 2-E-out-3</summary>

<a id="case-in_game_route_query-4d3847a380323c3058a3"></a>

**0° CCW: unverified** — `in_game_route_query-4d3847a380323c3058a3`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-N-in-1>2-E-out-3; entry: 2-N-in-1; exit: 2-E-out-3.

No observation recorded.

<a id="case-in_game_route_query-4633f89bb655cfead938"></a>

**90° CCW: unverified** — `in_game_route_query-4633f89bb655cfead938`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-N-in-1>2-E-out-3; entry: 2-N-in-1; exit: 2-E-out-3.

No observation recorded.

<a id="case-in_game_route_query-9e656b7381bba1896360"></a>

**180° CCW: unverified** — `in_game_route_query-9e656b7381bba1896360`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-N-in-1>2-E-out-3; entry: 2-N-in-1; exit: 2-E-out-3.

No observation recorded.

<a id="case-in_game_route_query-c67f7261c73dd19ec1b1"></a>

**270° CCW: unverified** — `in_game_route_query-c67f7261c73dd19ec1b1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-N-in-1>2-E-out-3; entry: 2-N-in-1; exit: 2-E-out-3.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: pedestrian; role: primary; journey: 2:2-S-in-4>2-W-out-2; entry: 2-S-in-4; exit: 2-W-out-2</summary>

<a id="case-in_game_route_query-74bff4e9f001a185c0cf"></a>

**0° CCW: unverified** — `in_game_route_query-74bff4e9f001a185c0cf`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-S-in-4>2-W-out-2; entry: 2-S-in-4; exit: 2-W-out-2.

No observation recorded.

<a id="case-in_game_route_query-cce2e6e47030eec349a7"></a>

**90° CCW: unverified** — `in_game_route_query-cce2e6e47030eec349a7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-S-in-4>2-W-out-2; entry: 2-S-in-4; exit: 2-W-out-2.

No observation recorded.

<a id="case-in_game_route_query-27a4609216b8e127e3c8"></a>

**180° CCW: unverified** — `in_game_route_query-27a4609216b8e127e3c8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-S-in-4>2-W-out-2; entry: 2-S-in-4; exit: 2-W-out-2.

No observation recorded.

<a id="case-in_game_route_query-adc5a39cc7f9f0c0f523"></a>

**270° CCW: unverified** — `in_game_route_query-adc5a39cc7f9f0c0f523`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: pedestrian; role: primary; journey: 2:2-S-in-4>2-W-out-2; entry: 2-S-in-4; exit: 2-W-out-2.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — pedestrian — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: pedestrian; role: primary; journey: 2:2-N-in-1>2-E-out-3; entry: 2-N-in-1; exit: 2-E-out-3 | — | <a href="#case-in_game_visible_travel-4d3847a380323c3058a3">[ ] unverified</a> | <a href="#case-in_game_visible_travel-4633f89bb655cfead938">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9e656b7381bba1896360">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c67f7261c73dd19ec1b1">[ ] unverified</a> |
| **Visible travel**<br>Service: pedestrian; role: primary; journey: 2:2-S-in-4>2-W-out-2; entry: 2-S-in-4; exit: 2-W-out-2 | — | <a href="#case-in_game_visible_travel-74bff4e9f001a185c0cf">[ ] unverified</a> | <a href="#case-in_game_visible_travel-cce2e6e47030eec349a7">[ ] unverified</a> | <a href="#case-in_game_visible_travel-27a4609216b8e127e3c8">[ ] unverified</a> | <a href="#case-in_game_visible_travel-adc5a39cc7f9f0c0f523">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: pedestrian; role: primary; journey: 2:2-N-in-1>2-E-out-3; entry: 2-N-in-1; exit: 2-E-out-3</summary>

<a id="case-in_game_visible_travel-4d3847a380323c3058a3"></a>

**0° CCW: unverified** — `in_game_visible_travel-4d3847a380323c3058a3`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-N-in-1>2-E-out-3; entry: 2-N-in-1; exit: 2-E-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-4633f89bb655cfead938"></a>

**90° CCW: unverified** — `in_game_visible_travel-4633f89bb655cfead938`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-N-in-1>2-E-out-3; entry: 2-N-in-1; exit: 2-E-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-9e656b7381bba1896360"></a>

**180° CCW: unverified** — `in_game_visible_travel-9e656b7381bba1896360`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-N-in-1>2-E-out-3; entry: 2-N-in-1; exit: 2-E-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-c67f7261c73dd19ec1b1"></a>

**270° CCW: unverified** — `in_game_visible_travel-c67f7261c73dd19ec1b1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-N-in-1>2-E-out-3; entry: 2-N-in-1; exit: 2-E-out-3.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: pedestrian; role: primary; journey: 2:2-S-in-4>2-W-out-2; entry: 2-S-in-4; exit: 2-W-out-2</summary>

<a id="case-in_game_visible_travel-74bff4e9f001a185c0cf"></a>

**0° CCW: unverified** — `in_game_visible_travel-74bff4e9f001a185c0cf`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-S-in-4>2-W-out-2; entry: 2-S-in-4; exit: 2-W-out-2.

No observation recorded.

<a id="case-in_game_visible_travel-cce2e6e47030eec349a7"></a>

**90° CCW: unverified** — `in_game_visible_travel-cce2e6e47030eec349a7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-S-in-4>2-W-out-2; entry: 2-S-in-4; exit: 2-W-out-2.

No observation recorded.

<a id="case-in_game_visible_travel-27a4609216b8e127e3c8"></a>

**180° CCW: unverified** — `in_game_visible_travel-27a4609216b8e127e3c8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-S-in-4>2-W-out-2; entry: 2-S-in-4; exit: 2-W-out-2.

No observation recorded.

<a id="case-in_game_visible_travel-adc5a39cc7f9f0c0f523"></a>

**270° CCW: unverified** — `in_game_visible_travel-adc5a39cc7f9f0c0f523`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: pedestrian; role: primary; journey: 2:2-S-in-4>2-W-out-2; entry: 2-S-in-4; exit: 2-W-out-2.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → road — 520 cases; unverified: 520</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-66febcb432cac1b0159c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c1fe082203f24c64969d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ff40df8f9d393c9bea46">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-55c8e6576a230dd161da">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7c40e76bd8c2b4346058">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7c3a1ee772a0e28d22dc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8627911ca84806e594ec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d9be8ce99da2a2a28f26">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1f97103c6012fd006075">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b8cd487e9e7136cd8c48">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-66c80c1cb644ace8207f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-011f7928aa8c3d22a78a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a5849d670704f9abb87d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f337e5b5c8c6bc4e7952">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-38dd5b3a3484f5f63d70">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8f3f656e13d78e550ce4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e02cf196f3710ca20de4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6241dbbb389beb6bd40c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eea4f4a6956dbc7d226b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-77c62d40f4c2bd020b47">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3d06cb94f9207a9fcada">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b0bd9b62df7494693877">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7a594d8bf0fabb33f266">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e680c2517551c1882414">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b737a8d17db4b40c0a27">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2c23b061d1955e366a97">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c6c7fcae8e19cb73b518">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-52f1ff0149d2cb1ee308">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d0bb4e323db3bfbd0fab">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a319a7ce0b28100b3bfd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1f8cfd943042e137980e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e6626490c33696c46c25">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5700e89e3f3a745842fb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-95abb8de669af8a5a3d6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-22aeae3c76db2ad528c0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a026a7caf96979611bad">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-44efb91ed7ded62dab49">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cb8e13e3b1a65c076aa7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-78f7c2020b45da08b163">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8b04872e391375a37ef0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cfd406c14ccc7ffe5e6b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-959c2a94d4c60ed3d4af">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2cd193b3a054223b128c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3144f030c47491892a9f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c24ff28a590450ae79b6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ef109a9b840995e2e0b8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2589ace3af7b2310910c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0e27871eb565ab3a111a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-75db42d202240f976d3f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-586e422d101a6471ceb9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1326ed487f3f3aacedbc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b2859c3ca58af73555ce">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-baf019bc06e6a436c865">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-020528b86134f020e2b4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-76e97f0e1a262e5b3a10">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e8fc673d929819678500">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-75056ac26fa25434d2c3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-685caaa1695fd691daab">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9161d6f0edc12518a41c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d197a4f31cc21e14af45">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-68a98565770e6b07797b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dc1d9c9d1d53085078f0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-57325a6a9b8a321fd2bb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-765822659732907d57c1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-55616ebc1f215c288bf1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c9cee3f9fb5894dd4b4c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c2065a3c03f482a39038">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-117fd4c5c2876d581483">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-687193622616177b181b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-375fcf31920d26cafbce">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2092166a53325dd3c753">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d257b46cb0afe878f8bb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e7400c0b0cf981977c6c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-09e138c6cb6a531b7f12">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-715ab0fe5058054594cc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3ed815a849a59670d9cb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-04cec6cd94fc95132a24">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2cf07cfec27139a0a0e2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-acb59529e5516292da1a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8430a3a24c5e8aa749dc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d50f85053f99ebbebfa6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b3181ad6564eef515272">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6f5d335bd7fc4cc0a139">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e60cb2b9b0336c7076aa">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ab707a58a23111cb6d24">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e9a79435932a75a5b8e9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9cc21ae0d47ae28884d5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8fb3455537336742464d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-93422a00895ba981be05">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5ef40905b56c057a0a5c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fb5fd61a5cd8ecd2a2c6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-77163687061fcb1e182a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bb7ff907001c1f342270">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5eaa2f661a0e5d13865e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f5fcf07dbdaaf10ed722">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ec21ddb5c2b268ef9a25">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c5d5b6b999ee5fada217">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dc3bc33566316c587748">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7a152db07c5c7ac27611">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0f50a941d3ea474bc7f8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e2ef12d36aafc997aef4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cb522175c6967f4c6c42">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c0a120bd55a8eab05717">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-29c707cb6a3a52e181a7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e9bd9ee0fbc3e04edc76">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6450b0906c9f35e99c31">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-961297dbf5ce7703b02c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5d615d7396e61dc9a7d7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2f93ebc52ed34194d76b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-61006f0e1a9b78673835">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-217cd89ae5d13320d53f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3948b7287c41a199a1ee">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a4b364e92f47e2463b23">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-86034158eeaf5c2c2abd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9cbeb07cee1a76650332">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9fbe6e39444b6632169b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1c9f56b0874576d07026">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-732c1fb8e6882d83841c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-56a6a8f276f58d04ad97">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9cf056034ed343cc5bbd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a09db5718943048f9e52">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8122c53772c5bf8546d4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b9e40a0a0f8b03c3260a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e86a513bd3fc512ddc21">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f7e2fb3b8e8986d04506">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fc6778c72a8f04f5acfe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1517a19b86bf6e6e8bfe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b4b223434a4b31f3f127">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-8; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-02ac829809f960238cf0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f54b2e16d1eed6dc57a7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2123cfc1f3f7cdc91393">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6499e7123a31c7895868">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-8; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-01b579da253305b19e0c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7c92aa5657cf26bee3cb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3c6b81094cfccac7a82e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fa38ab7d223d1ba8129c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-8; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a7ae964cb5f097b0812d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-93e15c9aa6b6b9721b0f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bc3a1044a616d24a8e42">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-65729ce5ded5d1b14464">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-8; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-788c2e021dff830d44eb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-784dda93be4fa3734961">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e642650e63107adad790">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-980ad393f2a6d2639131">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-8; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-39a4a4a9688190a6b805">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c57d0d88534896ddcb66">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-37f0e78d6056767891be">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3245d2eaa042ac4b3f08">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-8; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ea834bc4c0816095f504">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-54be62e34182d7188291">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3fc8128f978d27d7ae89">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b2b8f990f3fea7b5ddcc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-8; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0ded73b3c89a281bfa19">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ecbf464047b86fd5dc0e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9fc1c3aa7597eb81d4b2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-315d7932482c47fa676f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-8; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-90c83f6f691c686c3ae2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c5b6e26fa610468f59e0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e18a515a71fbc401dda6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a2ed1a4456bf3b1540dd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-8; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-634a282a9a6d614666ba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-47ba7b4b1bdcc264c1fd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e1ea2abbc56b6dd3fac4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-74ba9d9d3c0b75a436d0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-8; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-94ef907bbefbcaae58bb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-df53dfaeba709067bd67">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1a53c13122d0a13b8400">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bf046748acefdf361a04">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-8; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e5e337c1019acbc8ba2e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-399144bb57b29783ccc0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5397500484ab39f08b28">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0d949a15b920a77718df">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-9; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-965470822944a3d2ad1c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cc9d6c95ef78e4dd0e4a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-19d266b41569be6f346f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-97b2ec66ac58c7bf6668">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-9; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7452431d43202c6f9e8d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-63e27c4385985e337b75">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d3b30a212c6f14e2d37b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5a47fb02531a02a54241">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-9; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e744074af8a8c8e71c0d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-def62301c74745e6d000">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f9fe0cc60665dc9a067a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dffacda7cf402026042e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-9; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6eba86a9d3ac4fe4f860">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8b75bb0143238501cc17">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-83c62527a4fc95642cff">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-933fa31f123cce8e5ee0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-9; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fc795ca84615a36b8297">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-99dc3eae027f1d9aaa42">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3c9ceedb7132057bc993">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9da76144b87b314a347d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-9; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-10b9160ae0e2e5013153">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dedd18761c42b86cabde">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c662e5a1d8d61276d6a9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-50b26a203144ccb59725">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-9; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-14ff71d5b96cf52e1521">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1cd4e4570a134e7fd4f2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b2753af1cda859b3c3cb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9fc0a83cdc5b72ed68d9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-9; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-76c9777e97c953290c65">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f89e468aa25db953b2a6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a09b68d802338d4c6abd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d811065fa7e4dfb72511">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-9; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-63f9bfc5d76f3aed1f63">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8dbb3dc0063a9e0e8409">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c1d48050ce766e6432dd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9e55ac85fe5bdd583b32">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-9; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d6385568433c5d1055cb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-41159b1fc12f83630b80">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5338b1993d17cbb4ae7c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-37114a9c0e3dc683efe8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-9; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e3c6efdbacc0529ec9d9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f87f86f12672f3d2be11">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-73503723ef69008be672">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5d4226d6756c96de12e1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-10; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-597914e7fdf3e7b5df72">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1d36fe8dd1b766a3907b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c73f8b1a39c5b3a81028">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d5dd80ac25c79244a294">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-10; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-618c9e50e5a3bee4381b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-44c064547136fc8987ba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-65ce1cab9a7eea7af255">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7c3f1d270555ad8f0275">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-10; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-231546bf9699caa991b7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-760cae97e9b2ed52983f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a149763fab3bbe182f11">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e4fee1302ea40563c814">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-10; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f41e74f37e96d4e39bca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-169b1d07fe9606e8087d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f405997d8038ac3b7b69">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9e00b099f71686077dc4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-10; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-82348f8ee84c7c11c941">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-03ca9cfb75f65c807905">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7d373be03fd2ef1e350f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-425e23e6e6527e9ba34c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-10; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6ff1b28a66371182f51c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7c20b705cd55ff78c947">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-86ad3db0d672bd5a0fcf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1ca9e939a568545bc0fa">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-10; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b0868afe94eeb08d5dea">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-619d8c903bea66ca3dab">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8c4ef9cddfce8f0d2912">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-64f736c957a97a43b181">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-10; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3d07c0876d7e9e20a30c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-457030efb9cbea0a2942">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1c179c9e385f382d936f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-12fbd375d3d444beef4b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-10; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7666abfc16dcbf3ddd2d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f10f844aae5e5b4c6205">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5802dce72db77e66b89a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-de0b455eb0261025c751">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-10; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-41821b4dfaeaba7fe495">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2e7e9cf945d9f1724609">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1f99b8477204098d6264">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-be178514a51537dcd095">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-10; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d241dd7e1c3828725174">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-134919b3cef7d693ae16">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-469a9e9b1acba84d6395">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-210348f8278e75f67d60">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-15; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a73d75480f0752b7ae6a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c0e91133fbd6f007cc6f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-606bec3860abd1caceac">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0397acfd7d88208531cc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-15; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-19499bd50c9f059a6606">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9ba1049b360695a4edc7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0c3fbf54f4c4b4354c89">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-df67a0ac02bf245ee50a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-15; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-049579e165be9927a7db">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dfdd70ca9be2834ba930">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-23f326e088d442a61c60">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b73869d76a1f4a72d6bb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-15; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3de47e586b531f48199b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aaa35fedf738b1a46bbd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4ba69b910e18e222f079">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e7a84526c5695f4da657">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-15; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-77477b4913726494fe31">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e667dd73fd6391448b3e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fb9933f6c93f8f4f4310">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-be8d52d5c57431568f08">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-15; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-42d8532d8bb9c0614472">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-712451b47b0e9f781a31">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5fb815bdbca78f6e96c7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-581f0c8f798f96c15b93">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-15; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-935f625ee8c0e1d08242">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e814db48d9593ca9a35f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-86faf1f480838f77d82d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c5e613734b3c3764d15c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-15; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4958312f5bf57a13c1e0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-44e0fd0acd587fd68c8e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-33f0c3219f07576ce0c1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-50d04b62143e366ee2aa">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-15; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-72b82a3e0f39c2ec2a46">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c192c5b57334a37b58fe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-98aa291d11976ae0b003">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f02b3df90c55e52dfbcb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-15; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ad55e3d2b78807ce9668">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e0f8aece8d381f4f76ca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-76d9a37daf1aca8f114b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cae86f0bdd383fd32232">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-15; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3df67c811c104f2984aa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f64e55f9a5863b66ae94">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f2a413bacac2f58c6369">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5ed9ed8177b6ae20ae98">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-16; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-912375e61e38abf38ed2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c0a4b5b61fac7618aeff">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5ba61b2e82ae8167c6a4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5b8c50c44a212a972f8b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-16; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ed68e7d3991671bd0b16">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6abd7c0aab4c05b3d229">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f4ed43154a57649434a0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-63c6b130a9422981a30c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-16; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1ad75c690890a8b7ea45">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fe303f806fca8e3824fd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-35e8547955e23e2139bc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eaaf33c1c8f441c1b93a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-16; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5fc41b9b4ce04b1c464b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f9e4ee1295a27e417e32">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6d443ad6505ee35ac840">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1c42c3269a0763c4709e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-16; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-66845eea9758feb98653">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9542d8f3b0543a4b5ec0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-40259b89562be12c26a0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9aa6d258141229e79b05">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-16; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c70afb1acac6ecd182c2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-568e8c0cbf00665ede05">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d14c2e729f4cfd92e4ec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e662cc91e3c4640410c9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-16; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b2729d6e9d1fe9a61470">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b20c48d5d38a3e9439dc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a21614e14136362742da">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-70a013d0eb8dda606a49">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-16; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6cf8710d9275144252ea">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3e7e56dda680be557307">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-909a8daec72e40899131">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-20558afb583e034e662c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-16; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-557f97af7f6db3d1838e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-43b5635aa5b24ae6fd41">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-20de36b605a94c1becd8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a56c4ec46f13e6553386">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-16; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b9573883f5d793e719d6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-11ce2892745999369521">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c2cb53ebd4ba5b8db221">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4ee251de305ad73ed637">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-16; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-709cb7e15c84fec6d0aa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a105c151e43958d978f7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-41bc0b192a59b498489e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f51aaf5587c80f7ed856">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-18; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f638089e12360421d588">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6a225a23f5406b51c16c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-14d83f5222d722f30c16">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c1ef864b9898b707d356">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-18; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6911963bbd8a40fd53b2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-23d79d6be3a19524b5fd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d74ab55edb83beff97c5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d3e672cdcbfe62d629d2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-18; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9f004640671ec6fc1732">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f69b15b3934b05a3d22d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-981d9f6cbfaf57bdf7d2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d7d2625f2b7f0d5bf7f0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-18; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-33ea57c3b47f4fab4265">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6862a4a1646a630c814d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1088a9a1b3e86553138c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9f214e73232298d10cf3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-18; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4c754a2fa5a7b3322671">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-921d57986729ce2520ea">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9789a602919c31c6c430">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e0fcc35f077284450bce">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-18; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c8f9c49b2e79b35c7f72">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-be3b3550ba1ac0e37e89">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3a971d23883f35a333f3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5828bbe14d171c121f86">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-18; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0ad5b5aee2efd79b6e08">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b6d7743d3040ec4cb7f9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-48335676bad1a51bc2d4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9ad4364ec73fdfa5188c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-18; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3c2b375bfce388365056">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5f881f6dbd44755ded44">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8e8264aa5c3e13289758">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-009dd13bae09f3bf90f3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-18; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-96d8899632897712e824">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-591d5eaa9285e6ff7353">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-445ffe75326222aa8680">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-07a23281dfe725707f6b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-18; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a2534efe87face756e94">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9fc82ddf9fa2ef1f868a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-48d1dbafca4429844651">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c23f459dd6c03fb4d73d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-18; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7d8c7883ab50463e1368">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9a96e428d04d1b59cfbf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a7848c1812e7e7c7fec7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2ae2da5e164734a03166">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-20; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2d930edb3296e3183f11">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ca0d3c04d3b666d3b2f2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6bad8c2bda7550e3135a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8f4d8a014d0b113bd843">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-20; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c8b26258a5cfc21e061b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dd722cb2eaf2b9f18660">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-86ce7505249661e610f9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6ce7f2d4ee8d9e12c7ef">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-20; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e44d88fae63a24d69ba6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8b60fcc71fb8f36e18cc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7400ea480be814e4de2d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-106770946cb8364b5d8a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-20; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8ad748762053041f36df">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1bd59ccdebea0a58d79c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-da0a0cbb67605716843f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dec5de2009fe42a4f5a9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-20; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3a2c55b8297cfe7e36e7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-05845b0d958e91327b1a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4a8580e9c3bb35288d92">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-afcac2b779107e0e6f0b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-20; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a252e3384e37eb329555">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-04b54146a09b03edbf2d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-19ef03613391b15ac0a2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ae0fb580c73f2fb0107e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-20; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3c9f68dc1a8a53f39b54">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-de198dd165e379e824b2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-37d992b37a4d0b98017b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-19a77e577af346ad980f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-20; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2d8f945aa3e61b4d1f21">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-31333c2d19df154a0a3c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5beceb4103bbd24f3f90">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-acf042e9aee0b1803279">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-20; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ee37bca0fe980a8c2f18">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-833f9e7c949d784416ae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e39de549a3351b2e8cf9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-60ba78ddd2abb9e101ff">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-20; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a8b5f6c12d3e7fde006e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b586a5bc29165b68dc28">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e9627cf1f4eef92abea1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-acec0d64b8dbc395e39f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-20; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c6c17bca08aae5d4a478">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2dd1c5c6148214128bf8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-82f3b07a9241ac0cfb13">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4e92e7e0f303f9b53226">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-21; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2ae3a341f6c3bba7d308">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-049fb8569470bfeb0112">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7065f650bf3ef456ecfb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-94790b8ae1e6a4e4d63f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-21; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0852594f044bf4f83da1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-00eb5296dc29f6c144ad">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-02df8f46fdbc73cbca76">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7076b3d9b866fdb7454d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-21; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6c4ffa71692998be486b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7e1c5888f222027cfa8c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c8c74f9199d861b1a42d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-150c9337b6181f482edf">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-21; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-48d6cae357c60466a46e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3c3eb7cb0c3ed0f4cc21">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6182b9d6f77282fd187f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-908faa155eef5df14213">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-21; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-112b94731f0455612a1e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ddc914ca6ac9f311bbe8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ae79505f2c2185464232">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9684bc822ff25edbc007">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-21; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cc1bb4c73ec60c953670">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e6f429a979f21ecfc7c8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5ceac68a94d88e298010">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a7564448f5f31d4cf250">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-21; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-16912c82631de0146b46">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-60e645eafd08257e83c8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-60762a95e743c23ffc14">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5790da74217259266abf">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-21; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-dbb49cf458adc5ceec0c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7adc557fc5ec7b6d00e0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d78ce3313989a0c56d83">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-304b6d0c525cfe6fcea2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-21; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-99b665a4d47379fa813e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9b1ef8adb34d45a193ba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8734815516de71a88763">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-27b4a6428ceff160f617">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-21; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-19d94ad67753cc406315">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-abbdd6519196d7629338">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ead3fe3b74aec7045701">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5979dccbf8b3f301701d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-23; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-16ed47fdea403ac439be">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f0105a71aeab75fb51fd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-82aed086debb494aa43f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f186c72d593c7c0733f3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-23; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-17589a2889e78ff869ad">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7e38fa8ec4bc4bebbcfa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-48afb4915484027add0b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-056f870f9fb5038e715b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-23; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e7d3daf87fbb5dec8ffe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-13b0bd991ec8870125ef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-25d408ee2a7dee48c2f8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5b889ad57bf86426bdb6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-23; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bbaa8aba78927e0b95e1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-74f38991a5aeaa05c73c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-98e7bc694aaec7e80178">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3b304cb62eff63b2c806">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-23; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fe0554439cf5aeedb7af">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-67ed6374b440fb1d0c7d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e62af6aaeeeb9901c00b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e99c88965e4c31aced4e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-23; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0bfbf82929f97afe4334">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-213ad0ea85bee2014938">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3ccc62f249a655086681">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0c0e8bf1600ff1e6a8ea">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-23; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-957fc80557cb81697804">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4efc8c99790f3968611a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ddef76a2a832b2ecdbca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6d25010b855403935840">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-23; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8f3abc5750e122181766">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-20b1f155563d84903137">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-81a09adb1eb3a2d3a521">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c230624396175ec921f3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-23; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-670507d543a0deabbaec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c105b37102b40310007e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-30c9408c807f9dc71acb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-60ceed01e5202353af27">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-23; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e524d6d7b0b96f63f81b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7b115c0044bb1fcb20e9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-13a3edab98f7eaae0c45">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7891bb1672d74fb43840">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-23; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fbbfa8eedd7c900a1ee9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fdbbfe848eb976ef2860">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9fc5812612be5af0e349">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-98e678ca6fbc67daf3dc">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-66febcb432cac1b0159c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-66febcb432cac1b0159c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c1fe082203f24c64969d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c1fe082203f24c64969d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ff40df8f9d393c9bea46"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ff40df8f9d393c9bea46`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-55c8e6576a230dd161da"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-55c8e6576a230dd161da`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7c40e76bd8c2b4346058"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7c40e76bd8c2b4346058`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7c3a1ee772a0e28d22dc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7c3a1ee772a0e28d22dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8627911ca84806e594ec"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8627911ca84806e594ec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d9be8ce99da2a2a28f26"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d9be8ce99da2a2a28f26`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1f97103c6012fd006075"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1f97103c6012fd006075`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b8cd487e9e7136cd8c48"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b8cd487e9e7136cd8c48`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-66c80c1cb644ace8207f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-66c80c1cb644ace8207f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-011f7928aa8c3d22a78a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-011f7928aa8c3d22a78a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a5849d670704f9abb87d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a5849d670704f9abb87d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f337e5b5c8c6bc4e7952"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f337e5b5c8c6bc4e7952`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-38dd5b3a3484f5f63d70"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-38dd5b3a3484f5f63d70`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8f3f656e13d78e550ce4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8f3f656e13d78e550ce4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e02cf196f3710ca20de4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e02cf196f3710ca20de4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6241dbbb389beb6bd40c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6241dbbb389beb6bd40c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eea4f4a6956dbc7d226b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-eea4f4a6956dbc7d226b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-77c62d40f4c2bd020b47"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-77c62d40f4c2bd020b47`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3d06cb94f9207a9fcada"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3d06cb94f9207a9fcada`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b0bd9b62df7494693877"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b0bd9b62df7494693877`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7a594d8bf0fabb33f266"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7a594d8bf0fabb33f266`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e680c2517551c1882414"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e680c2517551c1882414`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b737a8d17db4b40c0a27"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b737a8d17db4b40c0a27`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2c23b061d1955e366a97"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2c23b061d1955e366a97`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c6c7fcae8e19cb73b518"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c6c7fcae8e19cb73b518`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-52f1ff0149d2cb1ee308"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-52f1ff0149d2cb1ee308`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d0bb4e323db3bfbd0fab"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d0bb4e323db3bfbd0fab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a319a7ce0b28100b3bfd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a319a7ce0b28100b3bfd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1f8cfd943042e137980e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1f8cfd943042e137980e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e6626490c33696c46c25"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e6626490c33696c46c25`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5700e89e3f3a745842fb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5700e89e3f3a745842fb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-95abb8de669af8a5a3d6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-95abb8de669af8a5a3d6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-22aeae3c76db2ad528c0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-22aeae3c76db2ad528c0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a026a7caf96979611bad"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a026a7caf96979611bad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-44efb91ed7ded62dab49"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-44efb91ed7ded62dab49`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cb8e13e3b1a65c076aa7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cb8e13e3b1a65c076aa7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-78f7c2020b45da08b163"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-78f7c2020b45da08b163`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8b04872e391375a37ef0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8b04872e391375a37ef0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cfd406c14ccc7ffe5e6b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cfd406c14ccc7ffe5e6b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-959c2a94d4c60ed3d4af"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-959c2a94d4c60ed3d4af`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2cd193b3a054223b128c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2cd193b3a054223b128c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3144f030c47491892a9f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3144f030c47491892a9f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c24ff28a590450ae79b6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c24ff28a590450ae79b6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ef109a9b840995e2e0b8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ef109a9b840995e2e0b8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2589ace3af7b2310910c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2589ace3af7b2310910c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0e27871eb565ab3a111a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0e27871eb565ab3a111a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-75db42d202240f976d3f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-75db42d202240f976d3f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-586e422d101a6471ceb9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-586e422d101a6471ceb9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1326ed487f3f3aacedbc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1326ed487f3f3aacedbc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b2859c3ca58af73555ce"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b2859c3ca58af73555ce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-baf019bc06e6a436c865"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-baf019bc06e6a436c865`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-020528b86134f020e2b4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-020528b86134f020e2b4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-76e97f0e1a262e5b3a10"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-76e97f0e1a262e5b3a10`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e8fc673d929819678500"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e8fc673d929819678500`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-75056ac26fa25434d2c3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-75056ac26fa25434d2c3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-685caaa1695fd691daab"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-685caaa1695fd691daab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9161d6f0edc12518a41c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9161d6f0edc12518a41c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d197a4f31cc21e14af45"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d197a4f31cc21e14af45`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-68a98565770e6b07797b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-68a98565770e6b07797b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dc1d9c9d1d53085078f0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-dc1d9c9d1d53085078f0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-57325a6a9b8a321fd2bb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-57325a6a9b8a321fd2bb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-765822659732907d57c1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-765822659732907d57c1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-55616ebc1f215c288bf1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-55616ebc1f215c288bf1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c9cee3f9fb5894dd4b4c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c9cee3f9fb5894dd4b4c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c2065a3c03f482a39038"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c2065a3c03f482a39038`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-117fd4c5c2876d581483"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-117fd4c5c2876d581483`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-687193622616177b181b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-687193622616177b181b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-375fcf31920d26cafbce"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-375fcf31920d26cafbce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2092166a53325dd3c753"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2092166a53325dd3c753`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d257b46cb0afe878f8bb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d257b46cb0afe878f8bb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e7400c0b0cf981977c6c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e7400c0b0cf981977c6c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-09e138c6cb6a531b7f12"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-09e138c6cb6a531b7f12`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-715ab0fe5058054594cc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-715ab0fe5058054594cc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3ed815a849a59670d9cb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3ed815a849a59670d9cb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-04cec6cd94fc95132a24"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-04cec6cd94fc95132a24`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2cf07cfec27139a0a0e2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2cf07cfec27139a0a0e2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-acb59529e5516292da1a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-acb59529e5516292da1a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8430a3a24c5e8aa749dc"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8430a3a24c5e8aa749dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d50f85053f99ebbebfa6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d50f85053f99ebbebfa6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b3181ad6564eef515272"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b3181ad6564eef515272`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6f5d335bd7fc4cc0a139"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6f5d335bd7fc4cc0a139`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e60cb2b9b0336c7076aa"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e60cb2b9b0336c7076aa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ab707a58a23111cb6d24"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ab707a58a23111cb6d24`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e9a79435932a75a5b8e9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e9a79435932a75a5b8e9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9cc21ae0d47ae28884d5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9cc21ae0d47ae28884d5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8fb3455537336742464d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8fb3455537336742464d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-93422a00895ba981be05"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-93422a00895ba981be05`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5ef40905b56c057a0a5c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5ef40905b56c057a0a5c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fb5fd61a5cd8ecd2a2c6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fb5fd61a5cd8ecd2a2c6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-77163687061fcb1e182a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-77163687061fcb1e182a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bb7ff907001c1f342270"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bb7ff907001c1f342270`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5eaa2f661a0e5d13865e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5eaa2f661a0e5d13865e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f5fcf07dbdaaf10ed722"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f5fcf07dbdaaf10ed722`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ec21ddb5c2b268ef9a25"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ec21ddb5c2b268ef9a25`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c5d5b6b999ee5fada217"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c5d5b6b999ee5fada217`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dc3bc33566316c587748"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-dc3bc33566316c587748`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7a152db07c5c7ac27611"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7a152db07c5c7ac27611`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0f50a941d3ea474bc7f8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0f50a941d3ea474bc7f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e2ef12d36aafc997aef4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e2ef12d36aafc997aef4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cb522175c6967f4c6c42"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cb522175c6967f4c6c42`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c0a120bd55a8eab05717"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c0a120bd55a8eab05717`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-29c707cb6a3a52e181a7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-29c707cb6a3a52e181a7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e9bd9ee0fbc3e04edc76"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e9bd9ee0fbc3e04edc76`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6450b0906c9f35e99c31"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6450b0906c9f35e99c31`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-961297dbf5ce7703b02c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-961297dbf5ce7703b02c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5d615d7396e61dc9a7d7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5d615d7396e61dc9a7d7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2f93ebc52ed34194d76b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2f93ebc52ed34194d76b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-61006f0e1a9b78673835"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-61006f0e1a9b78673835`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-217cd89ae5d13320d53f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-217cd89ae5d13320d53f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3948b7287c41a199a1ee"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3948b7287c41a199a1ee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a4b364e92f47e2463b23"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a4b364e92f47e2463b23`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-86034158eeaf5c2c2abd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-86034158eeaf5c2c2abd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9cbeb07cee1a76650332"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9cbeb07cee1a76650332`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9fbe6e39444b6632169b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9fbe6e39444b6632169b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1c9f56b0874576d07026"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1c9f56b0874576d07026`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-732c1fb8e6882d83841c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-732c1fb8e6882d83841c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-56a6a8f276f58d04ad97"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-56a6a8f276f58d04ad97`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9cf056034ed343cc5bbd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9cf056034ed343cc5bbd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a09db5718943048f9e52"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a09db5718943048f9e52`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8122c53772c5bf8546d4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8122c53772c5bf8546d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b9e40a0a0f8b03c3260a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b9e40a0a0f8b03c3260a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e86a513bd3fc512ddc21"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e86a513bd3fc512ddc21`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f7e2fb3b8e8986d04506"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f7e2fb3b8e8986d04506`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fc6778c72a8f04f5acfe"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fc6778c72a8f04f5acfe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1517a19b86bf6e6e8bfe"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1517a19b86bf6e6e8bfe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b4b223434a4b31f3f127"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b4b223434a4b31f3f127`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-8; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-02ac829809f960238cf0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-02ac829809f960238cf0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f54b2e16d1eed6dc57a7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f54b2e16d1eed6dc57a7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2123cfc1f3f7cdc91393"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2123cfc1f3f7cdc91393`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6499e7123a31c7895868"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6499e7123a31c7895868`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-8; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-01b579da253305b19e0c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-01b579da253305b19e0c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7c92aa5657cf26bee3cb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7c92aa5657cf26bee3cb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3c6b81094cfccac7a82e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3c6b81094cfccac7a82e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fa38ab7d223d1ba8129c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fa38ab7d223d1ba8129c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-8; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a7ae964cb5f097b0812d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a7ae964cb5f097b0812d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-93e15c9aa6b6b9721b0f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-93e15c9aa6b6b9721b0f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bc3a1044a616d24a8e42"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bc3a1044a616d24a8e42`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-65729ce5ded5d1b14464"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-65729ce5ded5d1b14464`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-8; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-788c2e021dff830d44eb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-788c2e021dff830d44eb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-784dda93be4fa3734961"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-784dda93be4fa3734961`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e642650e63107adad790"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e642650e63107adad790`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-980ad393f2a6d2639131"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-980ad393f2a6d2639131`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-8; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-39a4a4a9688190a6b805"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-39a4a4a9688190a6b805`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c57d0d88534896ddcb66"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c57d0d88534896ddcb66`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-37f0e78d6056767891be"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-37f0e78d6056767891be`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3245d2eaa042ac4b3f08"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3245d2eaa042ac4b3f08`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-8; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ea834bc4c0816095f504"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ea834bc4c0816095f504`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-54be62e34182d7188291"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-54be62e34182d7188291`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3fc8128f978d27d7ae89"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3fc8128f978d27d7ae89`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b2b8f990f3fea7b5ddcc"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b2b8f990f3fea7b5ddcc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-8; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0ded73b3c89a281bfa19"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0ded73b3c89a281bfa19`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ecbf464047b86fd5dc0e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ecbf464047b86fd5dc0e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9fc1c3aa7597eb81d4b2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9fc1c3aa7597eb81d4b2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-315d7932482c47fa676f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-315d7932482c47fa676f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-8; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-90c83f6f691c686c3ae2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-90c83f6f691c686c3ae2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c5b6e26fa610468f59e0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c5b6e26fa610468f59e0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e18a515a71fbc401dda6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e18a515a71fbc401dda6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a2ed1a4456bf3b1540dd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a2ed1a4456bf3b1540dd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-8; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-634a282a9a6d614666ba"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-634a282a9a6d614666ba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-47ba7b4b1bdcc264c1fd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-47ba7b4b1bdcc264c1fd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e1ea2abbc56b6dd3fac4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e1ea2abbc56b6dd3fac4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-74ba9d9d3c0b75a436d0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-74ba9d9d3c0b75a436d0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-8; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-94ef907bbefbcaae58bb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-94ef907bbefbcaae58bb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-df53dfaeba709067bd67"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-df53dfaeba709067bd67`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1a53c13122d0a13b8400"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1a53c13122d0a13b8400`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bf046748acefdf361a04"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bf046748acefdf361a04`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-8; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e5e337c1019acbc8ba2e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e5e337c1019acbc8ba2e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-399144bb57b29783ccc0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-399144bb57b29783ccc0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5397500484ab39f08b28"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5397500484ab39f08b28`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0d949a15b920a77718df"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0d949a15b920a77718df`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-9; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-965470822944a3d2ad1c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-965470822944a3d2ad1c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cc9d6c95ef78e4dd0e4a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cc9d6c95ef78e4dd0e4a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-19d266b41569be6f346f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-19d266b41569be6f346f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-97b2ec66ac58c7bf6668"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-97b2ec66ac58c7bf6668`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-9; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7452431d43202c6f9e8d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7452431d43202c6f9e8d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-63e27c4385985e337b75"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-63e27c4385985e337b75`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d3b30a212c6f14e2d37b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d3b30a212c6f14e2d37b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5a47fb02531a02a54241"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5a47fb02531a02a54241`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-9; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e744074af8a8c8e71c0d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e744074af8a8c8e71c0d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-def62301c74745e6d000"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-def62301c74745e6d000`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f9fe0cc60665dc9a067a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f9fe0cc60665dc9a067a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dffacda7cf402026042e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dffacda7cf402026042e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-9; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6eba86a9d3ac4fe4f860"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6eba86a9d3ac4fe4f860`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8b75bb0143238501cc17"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8b75bb0143238501cc17`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-83c62527a4fc95642cff"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-83c62527a4fc95642cff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-933fa31f123cce8e5ee0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-933fa31f123cce8e5ee0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-9; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fc795ca84615a36b8297"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fc795ca84615a36b8297`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-99dc3eae027f1d9aaa42"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-99dc3eae027f1d9aaa42`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3c9ceedb7132057bc993"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3c9ceedb7132057bc993`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9da76144b87b314a347d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9da76144b87b314a347d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-9; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-10b9160ae0e2e5013153"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-10b9160ae0e2e5013153`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dedd18761c42b86cabde"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-dedd18761c42b86cabde`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c662e5a1d8d61276d6a9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c662e5a1d8d61276d6a9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-50b26a203144ccb59725"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-50b26a203144ccb59725`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-9; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-14ff71d5b96cf52e1521"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-14ff71d5b96cf52e1521`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1cd4e4570a134e7fd4f2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1cd4e4570a134e7fd4f2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b2753af1cda859b3c3cb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b2753af1cda859b3c3cb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9fc0a83cdc5b72ed68d9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9fc0a83cdc5b72ed68d9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-9; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-76c9777e97c953290c65"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-76c9777e97c953290c65`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f89e468aa25db953b2a6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f89e468aa25db953b2a6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a09b68d802338d4c6abd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a09b68d802338d4c6abd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d811065fa7e4dfb72511"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d811065fa7e4dfb72511`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-9; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-63f9bfc5d76f3aed1f63"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-63f9bfc5d76f3aed1f63`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8dbb3dc0063a9e0e8409"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8dbb3dc0063a9e0e8409`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c1d48050ce766e6432dd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c1d48050ce766e6432dd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9e55ac85fe5bdd583b32"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9e55ac85fe5bdd583b32`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-9; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d6385568433c5d1055cb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d6385568433c5d1055cb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-41159b1fc12f83630b80"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-41159b1fc12f83630b80`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5338b1993d17cbb4ae7c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5338b1993d17cbb4ae7c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-37114a9c0e3dc683efe8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-37114a9c0e3dc683efe8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-9; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e3c6efdbacc0529ec9d9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e3c6efdbacc0529ec9d9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f87f86f12672f3d2be11"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f87f86f12672f3d2be11`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-73503723ef69008be672"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-73503723ef69008be672`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5d4226d6756c96de12e1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5d4226d6756c96de12e1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-10; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-597914e7fdf3e7b5df72"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-597914e7fdf3e7b5df72`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1d36fe8dd1b766a3907b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1d36fe8dd1b766a3907b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c73f8b1a39c5b3a81028"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c73f8b1a39c5b3a81028`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d5dd80ac25c79244a294"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d5dd80ac25c79244a294`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-10; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-618c9e50e5a3bee4381b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-618c9e50e5a3bee4381b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-44c064547136fc8987ba"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-44c064547136fc8987ba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-65ce1cab9a7eea7af255"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-65ce1cab9a7eea7af255`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7c3f1d270555ad8f0275"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7c3f1d270555ad8f0275`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-10; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-231546bf9699caa991b7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-231546bf9699caa991b7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-760cae97e9b2ed52983f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-760cae97e9b2ed52983f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a149763fab3bbe182f11"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a149763fab3bbe182f11`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e4fee1302ea40563c814"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e4fee1302ea40563c814`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-10; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f41e74f37e96d4e39bca"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f41e74f37e96d4e39bca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-169b1d07fe9606e8087d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-169b1d07fe9606e8087d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f405997d8038ac3b7b69"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f405997d8038ac3b7b69`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9e00b099f71686077dc4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9e00b099f71686077dc4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-10; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-82348f8ee84c7c11c941"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-82348f8ee84c7c11c941`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-03ca9cfb75f65c807905"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-03ca9cfb75f65c807905`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7d373be03fd2ef1e350f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7d373be03fd2ef1e350f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-425e23e6e6527e9ba34c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-425e23e6e6527e9ba34c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-10; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6ff1b28a66371182f51c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6ff1b28a66371182f51c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7c20b705cd55ff78c947"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7c20b705cd55ff78c947`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-86ad3db0d672bd5a0fcf"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-86ad3db0d672bd5a0fcf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1ca9e939a568545bc0fa"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1ca9e939a568545bc0fa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-10; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b0868afe94eeb08d5dea"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b0868afe94eeb08d5dea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-619d8c903bea66ca3dab"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-619d8c903bea66ca3dab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8c4ef9cddfce8f0d2912"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8c4ef9cddfce8f0d2912`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-64f736c957a97a43b181"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-64f736c957a97a43b181`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-10; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3d07c0876d7e9e20a30c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3d07c0876d7e9e20a30c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-457030efb9cbea0a2942"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-457030efb9cbea0a2942`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1c179c9e385f382d936f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1c179c9e385f382d936f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-12fbd375d3d444beef4b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-12fbd375d3d444beef4b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-10; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7666abfc16dcbf3ddd2d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7666abfc16dcbf3ddd2d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f10f844aae5e5b4c6205"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f10f844aae5e5b4c6205`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5802dce72db77e66b89a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5802dce72db77e66b89a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-de0b455eb0261025c751"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-de0b455eb0261025c751`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-10; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-41821b4dfaeaba7fe495"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-41821b4dfaeaba7fe495`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2e7e9cf945d9f1724609"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2e7e9cf945d9f1724609`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1f99b8477204098d6264"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1f99b8477204098d6264`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-be178514a51537dcd095"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-be178514a51537dcd095`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-10; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d241dd7e1c3828725174"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d241dd7e1c3828725174`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-134919b3cef7d693ae16"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-134919b3cef7d693ae16`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-469a9e9b1acba84d6395"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-469a9e9b1acba84d6395`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-210348f8278e75f67d60"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-210348f8278e75f67d60`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-15; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a73d75480f0752b7ae6a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a73d75480f0752b7ae6a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c0e91133fbd6f007cc6f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c0e91133fbd6f007cc6f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-606bec3860abd1caceac"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-606bec3860abd1caceac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0397acfd7d88208531cc"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0397acfd7d88208531cc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-15; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-19499bd50c9f059a6606"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-19499bd50c9f059a6606`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9ba1049b360695a4edc7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9ba1049b360695a4edc7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0c3fbf54f4c4b4354c89"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0c3fbf54f4c4b4354c89`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-df67a0ac02bf245ee50a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-df67a0ac02bf245ee50a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-15; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-049579e165be9927a7db"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-049579e165be9927a7db`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dfdd70ca9be2834ba930"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-dfdd70ca9be2834ba930`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-23f326e088d442a61c60"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-23f326e088d442a61c60`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b73869d76a1f4a72d6bb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b73869d76a1f4a72d6bb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-15; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3de47e586b531f48199b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3de47e586b531f48199b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aaa35fedf738b1a46bbd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-aaa35fedf738b1a46bbd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4ba69b910e18e222f079"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4ba69b910e18e222f079`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e7a84526c5695f4da657"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e7a84526c5695f4da657`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-15; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-77477b4913726494fe31"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-77477b4913726494fe31`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e667dd73fd6391448b3e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e667dd73fd6391448b3e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fb9933f6c93f8f4f4310"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fb9933f6c93f8f4f4310`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-be8d52d5c57431568f08"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-be8d52d5c57431568f08`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-15; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-42d8532d8bb9c0614472"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-42d8532d8bb9c0614472`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-712451b47b0e9f781a31"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-712451b47b0e9f781a31`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5fb815bdbca78f6e96c7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5fb815bdbca78f6e96c7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-581f0c8f798f96c15b93"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-581f0c8f798f96c15b93`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-15; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-935f625ee8c0e1d08242"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-935f625ee8c0e1d08242`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e814db48d9593ca9a35f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e814db48d9593ca9a35f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-86faf1f480838f77d82d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-86faf1f480838f77d82d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c5e613734b3c3764d15c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c5e613734b3c3764d15c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-15; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4958312f5bf57a13c1e0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4958312f5bf57a13c1e0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-44e0fd0acd587fd68c8e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-44e0fd0acd587fd68c8e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-33f0c3219f07576ce0c1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-33f0c3219f07576ce0c1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-50d04b62143e366ee2aa"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-50d04b62143e366ee2aa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-15; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-72b82a3e0f39c2ec2a46"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-72b82a3e0f39c2ec2a46`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c192c5b57334a37b58fe"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c192c5b57334a37b58fe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-98aa291d11976ae0b003"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-98aa291d11976ae0b003`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f02b3df90c55e52dfbcb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f02b3df90c55e52dfbcb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-15; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ad55e3d2b78807ce9668"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ad55e3d2b78807ce9668`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e0f8aece8d381f4f76ca"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e0f8aece8d381f4f76ca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-76d9a37daf1aca8f114b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-76d9a37daf1aca8f114b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cae86f0bdd383fd32232"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cae86f0bdd383fd32232`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-15; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3df67c811c104f2984aa"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3df67c811c104f2984aa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f64e55f9a5863b66ae94"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f64e55f9a5863b66ae94`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f2a413bacac2f58c6369"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f2a413bacac2f58c6369`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5ed9ed8177b6ae20ae98"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5ed9ed8177b6ae20ae98`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-16; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-912375e61e38abf38ed2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-912375e61e38abf38ed2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c0a4b5b61fac7618aeff"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c0a4b5b61fac7618aeff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5ba61b2e82ae8167c6a4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5ba61b2e82ae8167c6a4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5b8c50c44a212a972f8b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5b8c50c44a212a972f8b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-16; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ed68e7d3991671bd0b16"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ed68e7d3991671bd0b16`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6abd7c0aab4c05b3d229"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6abd7c0aab4c05b3d229`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f4ed43154a57649434a0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f4ed43154a57649434a0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-63c6b130a9422981a30c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-63c6b130a9422981a30c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-16; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1ad75c690890a8b7ea45"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1ad75c690890a8b7ea45`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fe303f806fca8e3824fd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fe303f806fca8e3824fd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-35e8547955e23e2139bc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-35e8547955e23e2139bc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eaaf33c1c8f441c1b93a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-eaaf33c1c8f441c1b93a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-16; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5fc41b9b4ce04b1c464b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5fc41b9b4ce04b1c464b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f9e4ee1295a27e417e32"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f9e4ee1295a27e417e32`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6d443ad6505ee35ac840"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6d443ad6505ee35ac840`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1c42c3269a0763c4709e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1c42c3269a0763c4709e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-16; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-66845eea9758feb98653"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-66845eea9758feb98653`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9542d8f3b0543a4b5ec0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9542d8f3b0543a4b5ec0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-40259b89562be12c26a0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-40259b89562be12c26a0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9aa6d258141229e79b05"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9aa6d258141229e79b05`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-16; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c70afb1acac6ecd182c2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c70afb1acac6ecd182c2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-568e8c0cbf00665ede05"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-568e8c0cbf00665ede05`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d14c2e729f4cfd92e4ec"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d14c2e729f4cfd92e4ec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e662cc91e3c4640410c9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e662cc91e3c4640410c9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-16; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b2729d6e9d1fe9a61470"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b2729d6e9d1fe9a61470`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b20c48d5d38a3e9439dc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b20c48d5d38a3e9439dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a21614e14136362742da"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a21614e14136362742da`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-70a013d0eb8dda606a49"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-70a013d0eb8dda606a49`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-16; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6cf8710d9275144252ea"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6cf8710d9275144252ea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3e7e56dda680be557307"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3e7e56dda680be557307`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-909a8daec72e40899131"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-909a8daec72e40899131`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-20558afb583e034e662c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-20558afb583e034e662c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-16; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-557f97af7f6db3d1838e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-557f97af7f6db3d1838e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-43b5635aa5b24ae6fd41"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-43b5635aa5b24ae6fd41`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-20de36b605a94c1becd8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-20de36b605a94c1becd8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a56c4ec46f13e6553386"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a56c4ec46f13e6553386`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-16; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b9573883f5d793e719d6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b9573883f5d793e719d6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-11ce2892745999369521"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-11ce2892745999369521`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c2cb53ebd4ba5b8db221"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c2cb53ebd4ba5b8db221`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4ee251de305ad73ed637"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4ee251de305ad73ed637`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-16; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-709cb7e15c84fec6d0aa"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-709cb7e15c84fec6d0aa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a105c151e43958d978f7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a105c151e43958d978f7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-41bc0b192a59b498489e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-41bc0b192a59b498489e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f51aaf5587c80f7ed856"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f51aaf5587c80f7ed856`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-18; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f638089e12360421d588"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f638089e12360421d588`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6a225a23f5406b51c16c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6a225a23f5406b51c16c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-14d83f5222d722f30c16"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-14d83f5222d722f30c16`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c1ef864b9898b707d356"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c1ef864b9898b707d356`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-18; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6911963bbd8a40fd53b2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6911963bbd8a40fd53b2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-23d79d6be3a19524b5fd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-23d79d6be3a19524b5fd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d74ab55edb83beff97c5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d74ab55edb83beff97c5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d3e672cdcbfe62d629d2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d3e672cdcbfe62d629d2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-18; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9f004640671ec6fc1732"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9f004640671ec6fc1732`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f69b15b3934b05a3d22d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f69b15b3934b05a3d22d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-981d9f6cbfaf57bdf7d2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-981d9f6cbfaf57bdf7d2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d7d2625f2b7f0d5bf7f0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d7d2625f2b7f0d5bf7f0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-18; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-33ea57c3b47f4fab4265"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-33ea57c3b47f4fab4265`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6862a4a1646a630c814d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6862a4a1646a630c814d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1088a9a1b3e86553138c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1088a9a1b3e86553138c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9f214e73232298d10cf3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9f214e73232298d10cf3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-18; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4c754a2fa5a7b3322671"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4c754a2fa5a7b3322671`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-921d57986729ce2520ea"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-921d57986729ce2520ea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9789a602919c31c6c430"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9789a602919c31c6c430`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e0fcc35f077284450bce"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e0fcc35f077284450bce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-18; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c8f9c49b2e79b35c7f72"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c8f9c49b2e79b35c7f72`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-be3b3550ba1ac0e37e89"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-be3b3550ba1ac0e37e89`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3a971d23883f35a333f3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3a971d23883f35a333f3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5828bbe14d171c121f86"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5828bbe14d171c121f86`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-18; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0ad5b5aee2efd79b6e08"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0ad5b5aee2efd79b6e08`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b6d7743d3040ec4cb7f9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b6d7743d3040ec4cb7f9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-48335676bad1a51bc2d4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-48335676bad1a51bc2d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9ad4364ec73fdfa5188c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9ad4364ec73fdfa5188c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-18; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3c2b375bfce388365056"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3c2b375bfce388365056`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5f881f6dbd44755ded44"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5f881f6dbd44755ded44`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8e8264aa5c3e13289758"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8e8264aa5c3e13289758`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-009dd13bae09f3bf90f3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-009dd13bae09f3bf90f3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-18; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-96d8899632897712e824"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-96d8899632897712e824`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-591d5eaa9285e6ff7353"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-591d5eaa9285e6ff7353`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-445ffe75326222aa8680"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-445ffe75326222aa8680`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-07a23281dfe725707f6b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-07a23281dfe725707f6b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-18; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a2534efe87face756e94"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a2534efe87face756e94`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9fc82ddf9fa2ef1f868a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9fc82ddf9fa2ef1f868a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-48d1dbafca4429844651"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-48d1dbafca4429844651`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c23f459dd6c03fb4d73d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c23f459dd6c03fb4d73d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-18; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7d8c7883ab50463e1368"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7d8c7883ab50463e1368`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9a96e428d04d1b59cfbf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9a96e428d04d1b59cfbf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a7848c1812e7e7c7fec7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a7848c1812e7e7c7fec7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2ae2da5e164734a03166"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2ae2da5e164734a03166`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-20; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2d930edb3296e3183f11"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2d930edb3296e3183f11`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ca0d3c04d3b666d3b2f2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ca0d3c04d3b666d3b2f2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6bad8c2bda7550e3135a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6bad8c2bda7550e3135a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8f4d8a014d0b113bd843"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8f4d8a014d0b113bd843`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-20; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c8b26258a5cfc21e061b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c8b26258a5cfc21e061b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dd722cb2eaf2b9f18660"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-dd722cb2eaf2b9f18660`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-86ce7505249661e610f9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-86ce7505249661e610f9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6ce7f2d4ee8d9e12c7ef"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6ce7f2d4ee8d9e12c7ef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-20; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e44d88fae63a24d69ba6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e44d88fae63a24d69ba6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8b60fcc71fb8f36e18cc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8b60fcc71fb8f36e18cc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7400ea480be814e4de2d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7400ea480be814e4de2d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-106770946cb8364b5d8a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-106770946cb8364b5d8a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-20; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8ad748762053041f36df"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8ad748762053041f36df`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1bd59ccdebea0a58d79c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1bd59ccdebea0a58d79c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-da0a0cbb67605716843f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-da0a0cbb67605716843f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dec5de2009fe42a4f5a9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dec5de2009fe42a4f5a9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-20; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3a2c55b8297cfe7e36e7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3a2c55b8297cfe7e36e7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-05845b0d958e91327b1a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-05845b0d958e91327b1a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4a8580e9c3bb35288d92"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4a8580e9c3bb35288d92`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-afcac2b779107e0e6f0b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-afcac2b779107e0e6f0b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-20; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a252e3384e37eb329555"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a252e3384e37eb329555`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-04b54146a09b03edbf2d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-04b54146a09b03edbf2d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-19ef03613391b15ac0a2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-19ef03613391b15ac0a2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ae0fb580c73f2fb0107e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ae0fb580c73f2fb0107e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-20; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3c9f68dc1a8a53f39b54"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3c9f68dc1a8a53f39b54`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-de198dd165e379e824b2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-de198dd165e379e824b2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-37d992b37a4d0b98017b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-37d992b37a4d0b98017b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-19a77e577af346ad980f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-19a77e577af346ad980f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-20; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2d8f945aa3e61b4d1f21"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2d8f945aa3e61b4d1f21`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-31333c2d19df154a0a3c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-31333c2d19df154a0a3c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5beceb4103bbd24f3f90"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5beceb4103bbd24f3f90`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-acf042e9aee0b1803279"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-acf042e9aee0b1803279`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-20; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ee37bca0fe980a8c2f18"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ee37bca0fe980a8c2f18`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-833f9e7c949d784416ae"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-833f9e7c949d784416ae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e39de549a3351b2e8cf9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e39de549a3351b2e8cf9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-60ba78ddd2abb9e101ff"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-60ba78ddd2abb9e101ff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-20; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a8b5f6c12d3e7fde006e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a8b5f6c12d3e7fde006e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b586a5bc29165b68dc28"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b586a5bc29165b68dc28`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e9627cf1f4eef92abea1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e9627cf1f4eef92abea1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-acec0d64b8dbc395e39f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-acec0d64b8dbc395e39f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-20; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c6c17bca08aae5d4a478"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c6c17bca08aae5d4a478`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2dd1c5c6148214128bf8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2dd1c5c6148214128bf8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-82f3b07a9241ac0cfb13"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-82f3b07a9241ac0cfb13`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4e92e7e0f303f9b53226"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4e92e7e0f303f9b53226`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-21; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2ae3a341f6c3bba7d308"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2ae3a341f6c3bba7d308`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-049fb8569470bfeb0112"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-049fb8569470bfeb0112`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7065f650bf3ef456ecfb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7065f650bf3ef456ecfb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-94790b8ae1e6a4e4d63f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-94790b8ae1e6a4e4d63f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-21; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0852594f044bf4f83da1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0852594f044bf4f83da1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-00eb5296dc29f6c144ad"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-00eb5296dc29f6c144ad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-02df8f46fdbc73cbca76"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-02df8f46fdbc73cbca76`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7076b3d9b866fdb7454d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7076b3d9b866fdb7454d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-21; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6c4ffa71692998be486b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6c4ffa71692998be486b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7e1c5888f222027cfa8c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7e1c5888f222027cfa8c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c8c74f9199d861b1a42d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c8c74f9199d861b1a42d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-150c9337b6181f482edf"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-150c9337b6181f482edf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-21; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-48d6cae357c60466a46e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-48d6cae357c60466a46e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3c3eb7cb0c3ed0f4cc21"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3c3eb7cb0c3ed0f4cc21`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6182b9d6f77282fd187f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6182b9d6f77282fd187f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-908faa155eef5df14213"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-908faa155eef5df14213`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-21; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-112b94731f0455612a1e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-112b94731f0455612a1e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ddc914ca6ac9f311bbe8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ddc914ca6ac9f311bbe8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ae79505f2c2185464232"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ae79505f2c2185464232`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9684bc822ff25edbc007"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9684bc822ff25edbc007`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-21; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cc1bb4c73ec60c953670"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cc1bb4c73ec60c953670`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e6f429a979f21ecfc7c8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e6f429a979f21ecfc7c8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5ceac68a94d88e298010"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5ceac68a94d88e298010`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a7564448f5f31d4cf250"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a7564448f5f31d4cf250`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-21; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-16912c82631de0146b46"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-16912c82631de0146b46`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-60e645eafd08257e83c8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-60e645eafd08257e83c8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-60762a95e743c23ffc14"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-60762a95e743c23ffc14`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5790da74217259266abf"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5790da74217259266abf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-21; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-dbb49cf458adc5ceec0c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-dbb49cf458adc5ceec0c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7adc557fc5ec7b6d00e0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7adc557fc5ec7b6d00e0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d78ce3313989a0c56d83"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d78ce3313989a0c56d83`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-304b6d0c525cfe6fcea2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-304b6d0c525cfe6fcea2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-21; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-99b665a4d47379fa813e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-99b665a4d47379fa813e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9b1ef8adb34d45a193ba"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9b1ef8adb34d45a193ba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8734815516de71a88763"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8734815516de71a88763`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-27b4a6428ceff160f617"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-27b4a6428ceff160f617`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-21; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-19d94ad67753cc406315"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-19d94ad67753cc406315`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-abbdd6519196d7629338"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-abbdd6519196d7629338`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ead3fe3b74aec7045701"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ead3fe3b74aec7045701`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5979dccbf8b3f301701d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5979dccbf8b3f301701d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-23; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-16ed47fdea403ac439be"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-16ed47fdea403ac439be`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f0105a71aeab75fb51fd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f0105a71aeab75fb51fd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-82aed086debb494aa43f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-82aed086debb494aa43f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f186c72d593c7c0733f3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f186c72d593c7c0733f3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-23; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-17589a2889e78ff869ad"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-17589a2889e78ff869ad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7e38fa8ec4bc4bebbcfa"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7e38fa8ec4bc4bebbcfa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-48afb4915484027add0b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-48afb4915484027add0b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-056f870f9fb5038e715b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-056f870f9fb5038e715b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-23; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e7d3daf87fbb5dec8ffe"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e7d3daf87fbb5dec8ffe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-13b0bd991ec8870125ef"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-13b0bd991ec8870125ef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-25d408ee2a7dee48c2f8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-25d408ee2a7dee48c2f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5b889ad57bf86426bdb6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5b889ad57bf86426bdb6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-7; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-23; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bbaa8aba78927e0b95e1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bbaa8aba78927e0b95e1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-74f38991a5aeaa05c73c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-74f38991a5aeaa05c73c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-98e7bc694aaec7e80178"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-98e7bc694aaec7e80178`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3b304cb62eff63b2c806"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3b304cb62eff63b2c806`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-23; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fe0554439cf5aeedb7af"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fe0554439cf5aeedb7af`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-67ed6374b440fb1d0c7d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-67ed6374b440fb1d0c7d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e62af6aaeeeb9901c00b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e62af6aaeeeb9901c00b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e99c88965e4c31aced4e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e99c88965e4c31aced4e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-23; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0bfbf82929f97afe4334"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0bfbf82929f97afe4334`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-213ad0ea85bee2014938"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-213ad0ea85bee2014938`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3ccc62f249a655086681"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3ccc62f249a655086681`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0c0e8bf1600ff1e6a8ea"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0c0e8bf1600ff1e6a8ea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-E-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-23; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-957fc80557cb81697804"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-957fc80557cb81697804`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4efc8c99790f3968611a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4efc8c99790f3968611a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ddef76a2a832b2ecdbca"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ddef76a2a832b2ecdbca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6d25010b855403935840"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6d25010b855403935840`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-E-out-14; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-23; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8f3abc5750e122181766"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8f3abc5750e122181766`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-20b1f155563d84903137"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-20b1f155563d84903137`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-81a09adb1eb3a2d3a521"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-81a09adb1eb3a2d3a521`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c230624396175ec921f3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c230624396175ec921f3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-23; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-670507d543a0deabbaec"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-670507d543a0deabbaec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c105b37102b40310007e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c105b37102b40310007e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-30c9408c807f9dc71acb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-30c9408c807f9dc71acb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-60ceed01e5202353af27"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-60ceed01e5202353af27`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-19; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-23; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e524d6d7b0b96f63f81b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e524d6d7b0b96f63f81b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7b115c0044bb1fcb20e9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7b115c0044bb1fcb20e9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-13a3edab98f7eaae0c45"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-13a3edab98f7eaae0c45`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7891bb1672d74fb43840"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7891bb1672d74fb43840`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-N-out-22; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-23; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fbbfa8eedd7c900a1ee9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fbbfa8eedd7c900a1ee9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fdbbfe848eb976ef2860"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fdbbfe848eb976ef2860`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9fc5812612be5af0e349"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9fc5812612be5af0e349`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-98e678ca6fbc67daf3dc"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-98e678ca6fbc67daf3dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → pedestrian — 96 cases; unverified: 96</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ec80ad41a12a10f10477">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4b52fcfe60b2fea84562">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-580e4ea4df4a1c756c5c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f4d8f9556df8c254950a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d33a9ff99515e785533a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-303118bee26eb2d58198">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7ec54a14053993cfc638">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9eb0130ec79491b397e0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-10c4a0acbc7c51574909">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-66a9e795153955ff4d76">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-547030d47cbd16454bd6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-050b611466ee9ebd42eb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-135e7c32048431400296">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8dd758e62612b1cab327">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a640c4b2deee0843931c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c40309a818f862c7a2d4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0834b6565e74b47aefe1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dfd43819d5dfdba49a0f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c8c47026ec9e207165c4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4e721500cc8d3c5bdbe8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-630abeaf75f7b9a53be8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-177520cb8643ca8cfa4a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1740e26e325291f92a9c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6d80d333abbe8fdd91fa">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-8; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-58cbef086864c3548663">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c5cabec2244afc3a5cac">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7b5a06f2030b72162299">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-638f8859ac833ebfcd06">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-8; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bbc03c0ac8bc78dfe9eb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bbbf674e5b4429f9641a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-61afa6a46472437117f2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3dcb0b3fab6ccb4444d0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-9; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-089cd1aaf7c2fb3bfacf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9598bd2b5215f3fd603f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-618802fb4b9b2406654e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5d8387283d577d3b7da6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-9; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1fe5334cb603d081f941">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e5f06627df8ea886eaad">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a5ab9cd7ddff6af8d2e4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-97fc6c08618bb8205d53">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-10; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-098f9e53abe8b1651363">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9d1ad8b0a7ca9c9adf48">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-be837ab007e6861c8014">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5797f4941a51aff12ce6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-10; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1dd73ee28da257e80fb0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-37a0768c3dceb8cfe1f0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3125d1fff7838ad8ac3a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4de4ecb104c8f8d8c6fe">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-15; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fe05bb813a7a979d6ad3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-024c476d10a3177daf12">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-22bdc06c50f071fb1b25">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c80f0bba48e21353e00b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-15; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-03b03ae142b58d7fd434">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f6a4d1f0d8845fa219d2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-03f2d09bb0b79da10483">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e4e36cff31bbefb7b7ec">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-16; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e1624d872f8476b9b164">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-74980b1e2d92e7993edb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6534e38cab574bd407a3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-759dfbf3027aac38bfb1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-16; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7d3e1937f5db675134bb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9885ce0486461593772e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c585c7421014a7fbcb88">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-57dea1e3cc7b7e554913">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-18; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a700b86a616db07e84f8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-10831f9e26e68ff27a68">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9cd8f72b92ab45a077fc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8770e5717dbd95e47164">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-18; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-31d57c1f5870f9b594be">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ebe3be93f55fe5c1b7e4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4e271dfc47eee4b1d8fd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b5940484f7845def4255">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-20; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7db9be73bacc3b17f2a8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c464f20c887c8ce01f5e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-57f5fe56869b370b433d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ad76b8db8b6150813265">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-20; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-859460065b5dd9a079f8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6770a40448d85d2c5dff">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bbc84b0903bc7cfa9d8f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0e54e5f369c3761c636e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-21; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e29d40aadbd8c2723ad5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b48e5ef08e3a20ed08e8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c772222be370bcd75285">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-99ff4b8b932bcb4a75a0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-21; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-195851a42a0275c62298">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b80a2d927d101890782d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-af1d5bf54e09d9b55018">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4a2b54a24c0d1fc73972">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-23; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2f1f8858e3f54c2ac00f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ee61a681e4645d0c3306">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-37550ee6592af0882a93">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8bf142cced7b3ebe7bf7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-23; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-52d24a041278f31664e8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-be956e3b807e2a8039fb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-853dccfc49e4ffbee71c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ef74c8f84e38aad734c1">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ec80ad41a12a10f10477"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ec80ad41a12a10f10477`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4b52fcfe60b2fea84562"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4b52fcfe60b2fea84562`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-580e4ea4df4a1c756c5c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-580e4ea4df4a1c756c5c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f4d8f9556df8c254950a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f4d8f9556df8c254950a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d33a9ff99515e785533a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d33a9ff99515e785533a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-303118bee26eb2d58198"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-303118bee26eb2d58198`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7ec54a14053993cfc638"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7ec54a14053993cfc638`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9eb0130ec79491b397e0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9eb0130ec79491b397e0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-10c4a0acbc7c51574909"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-10c4a0acbc7c51574909`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-66a9e795153955ff4d76"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-66a9e795153955ff4d76`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-547030d47cbd16454bd6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-547030d47cbd16454bd6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-050b611466ee9ebd42eb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-050b611466ee9ebd42eb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-135e7c32048431400296"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-135e7c32048431400296`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8dd758e62612b1cab327"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8dd758e62612b1cab327`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a640c4b2deee0843931c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a640c4b2deee0843931c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c40309a818f862c7a2d4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c40309a818f862c7a2d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0834b6565e74b47aefe1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0834b6565e74b47aefe1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dfd43819d5dfdba49a0f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-dfd43819d5dfdba49a0f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c8c47026ec9e207165c4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c8c47026ec9e207165c4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4e721500cc8d3c5bdbe8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4e721500cc8d3c5bdbe8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-630abeaf75f7b9a53be8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-630abeaf75f7b9a53be8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-177520cb8643ca8cfa4a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-177520cb8643ca8cfa4a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1740e26e325291f92a9c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1740e26e325291f92a9c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6d80d333abbe8fdd91fa"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6d80d333abbe8fdd91fa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-8; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-58cbef086864c3548663"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-58cbef086864c3548663`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c5cabec2244afc3a5cac"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c5cabec2244afc3a5cac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7b5a06f2030b72162299"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7b5a06f2030b72162299`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-638f8859ac833ebfcd06"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-638f8859ac833ebfcd06`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-8; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bbc03c0ac8bc78dfe9eb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bbc03c0ac8bc78dfe9eb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bbbf674e5b4429f9641a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bbbf674e5b4429f9641a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-61afa6a46472437117f2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-61afa6a46472437117f2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3dcb0b3fab6ccb4444d0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3dcb0b3fab6ccb4444d0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-9; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-089cd1aaf7c2fb3bfacf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-089cd1aaf7c2fb3bfacf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9598bd2b5215f3fd603f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9598bd2b5215f3fd603f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-618802fb4b9b2406654e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-618802fb4b9b2406654e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5d8387283d577d3b7da6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5d8387283d577d3b7da6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-9; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1fe5334cb603d081f941"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1fe5334cb603d081f941`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e5f06627df8ea886eaad"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e5f06627df8ea886eaad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a5ab9cd7ddff6af8d2e4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a5ab9cd7ddff6af8d2e4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-97fc6c08618bb8205d53"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-97fc6c08618bb8205d53`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-9; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-10; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-098f9e53abe8b1651363"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-098f9e53abe8b1651363`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9d1ad8b0a7ca9c9adf48"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9d1ad8b0a7ca9c9adf48`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-be837ab007e6861c8014"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-be837ab007e6861c8014`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5797f4941a51aff12ce6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5797f4941a51aff12ce6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-10; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1dd73ee28da257e80fb0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1dd73ee28da257e80fb0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-37a0768c3dceb8cfe1f0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-37a0768c3dceb8cfe1f0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3125d1fff7838ad8ac3a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3125d1fff7838ad8ac3a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4de4ecb104c8f8d8c6fe"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4de4ecb104c8f8d8c6fe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-10; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-15; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fe05bb813a7a979d6ad3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fe05bb813a7a979d6ad3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-024c476d10a3177daf12"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-024c476d10a3177daf12`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-22bdc06c50f071fb1b25"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-22bdc06c50f071fb1b25`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c80f0bba48e21353e00b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c80f0bba48e21353e00b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-15; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-03b03ae142b58d7fd434"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-03b03ae142b58d7fd434`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f6a4d1f0d8845fa219d2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f6a4d1f0d8845fa219d2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-03f2d09bb0b79da10483"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-03f2d09bb0b79da10483`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e4e36cff31bbefb7b7ec"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e4e36cff31bbefb7b7ec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-15; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-16; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e1624d872f8476b9b164"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e1624d872f8476b9b164`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-74980b1e2d92e7993edb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-74980b1e2d92e7993edb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6534e38cab574bd407a3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6534e38cab574bd407a3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-759dfbf3027aac38bfb1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-759dfbf3027aac38bfb1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-16; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7d3e1937f5db675134bb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7d3e1937f5db675134bb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9885ce0486461593772e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9885ce0486461593772e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c585c7421014a7fbcb88"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c585c7421014a7fbcb88`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-57dea1e3cc7b7e554913"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-57dea1e3cc7b7e554913`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-18; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a700b86a616db07e84f8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a700b86a616db07e84f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-10831f9e26e68ff27a68"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-10831f9e26e68ff27a68`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9cd8f72b92ab45a077fc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9cd8f72b92ab45a077fc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8770e5717dbd95e47164"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8770e5717dbd95e47164`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-18; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-31d57c1f5870f9b594be"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-31d57c1f5870f9b594be`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ebe3be93f55fe5c1b7e4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ebe3be93f55fe5c1b7e4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4e271dfc47eee4b1d8fd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4e271dfc47eee4b1d8fd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b5940484f7845def4255"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b5940484f7845def4255`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-18; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-20; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7db9be73bacc3b17f2a8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7db9be73bacc3b17f2a8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c464f20c887c8ce01f5e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c464f20c887c8ce01f5e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-57f5fe56869b370b433d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-57f5fe56869b370b433d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ad76b8db8b6150813265"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ad76b8db8b6150813265`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-20; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-859460065b5dd9a079f8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-859460065b5dd9a079f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6770a40448d85d2c5dff"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6770a40448d85d2c5dff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bbc84b0903bc7cfa9d8f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bbc84b0903bc7cfa9d8f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0e54e5f369c3761c636e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0e54e5f369c3761c636e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-20; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-21; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e29d40aadbd8c2723ad5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e29d40aadbd8c2723ad5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b48e5ef08e3a20ed08e8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b48e5ef08e3a20ed08e8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c772222be370bcd75285"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c772222be370bcd75285`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-99ff4b8b932bcb4a75a0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-99ff4b8b932bcb4a75a0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-21; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-195851a42a0275c62298"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-195851a42a0275c62298`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b80a2d927d101890782d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b80a2d927d101890782d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-af1d5bf54e09d9b55018"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-af1d5bf54e09d9b55018`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4a2b54a24c0d1fc73972"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4a2b54a24c0d1fc73972`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-21; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-23; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2f1f8858e3f54c2ac00f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2f1f8858e3f54c2ac00f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ee61a681e4645d0c3306"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ee61a681e4645d0c3306`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-37550ee6592af0882a93"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-37550ee6592af0882a93`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8bf142cced7b3ebe7bf7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8bf142cced7b3ebe7bf7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-23; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-52d24a041278f31664e8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-52d24a041278f31664e8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-be956e3b807e2a8039fb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-be956e3b807e2a8039fb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-853dccfc49e4ffbee71c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-853dccfc49e4ffbee71c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ef74c8f84e38aad734c1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ef74c8f84e38aad734c1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — pedestrian → road — 96 cases; unverified: 96</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-W-out-1; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-068afd5d04630eb0a817">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-760a6e551a67b6cf2898">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-884e1b24921b9426d69f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7ac4fbacdf0ddd9224de">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-W-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9e73a7e3bccf3ac5cdcd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ce7f0f9e5af6719c85ca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ac96b573558ec65fd3a9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5a355b9ebcb2e66cd613">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-E-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8edc1cc5e26482252bbb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-20dc195a172c27d1e8b6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-73b305935dac9d7d27c7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-acffd45413b07628b39e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-W-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7ffdca674b60c7e037d3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ac5c70acb795fa710e13">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9fefee5656a9bcc69a04">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-77fafeb69c615ddd0e8d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-W-out-11; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c43bcec27de64c8e16d8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-867c8c937f8beeabeb79">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0be919dd7bc4edb6a2f5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2ef28efb5eac258e05fb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-W-out-12; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c02562975d17053335fc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-da784e5481090f9a0711">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f1fceb41ce8589a5df37">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8cc3824504103ca6f169">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-E-out-13; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6c5c2b2b490e1fff1f62">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8d3f180bb52857c6ab12">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fdd26b750172ac4fe53b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dccb922ca52483eebaa1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-E-out-14; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1d66ccc315a599e3bf34">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f3628d099e0265b35789">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e5c1f5c3808de8156cf3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d8aca6d07f85d90aafa6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-W-out-17; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-63e341ec390373a6d3b3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ab8d2dba2ac6bff9cd57">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6cf518bc0856e7cd4e57">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a3a3f4d88ecf21534a51">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-W-out-19; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-98be73ca8d2835805f29">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-651e5b564ff2b360c099">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8593bd4fd33ee83f57cb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-216970b3990cd8ecb9c0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-N-out-22; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e5b506bc96d990774565">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-819afcba9b94f559a0f8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b5fb1b38ebf8c198e958">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-435a14fd6cbefe02bbbe">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-N-out-24; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-aa90ff0eba6b7df408af">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9f170a110ef9dd5e813f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-340e83913250894e9f17">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e83433db110989f8e38d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-W-out-1; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-96add150c70ca306c29e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2307d64064d783ab0fe6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-62be5a61830b92aea96a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b692dd8b56e6ba551b64">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-W-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-652c9b75e15491beff5b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5d0d371416f419c60f22">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4efcb45237581973b77d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a24cbb0f84f97dcdbf7b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-E-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b8c0e1cf53c069ffa9c5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-054d56e34daa60125b1f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-17d3864a2b9e6b0d7e01">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7faf2aac49377a64e6cc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-W-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ac7d89934e82fb6a4c82">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-47d30733f1e5d1f0e501">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-444ec3951410de8261dc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-466e475304c8b588af28">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-W-out-11; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-23fba44891ada629af8c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a485b427cdcf02b2e78b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4795e054db47bb95ba28">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-052b122537d7d48c96e3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-W-out-12; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-70457536e3ad8edf9b62">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1c406b7faa9fc214e583">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4f51cdd62a210ec6bbe2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f8f920dfa5453ad4c6f4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-E-out-13; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-df354657735203bd22a6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1c7dc80ad9e445d334e0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f79d07bbfe7de96628a4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-673832c793d6229eada3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-E-out-14; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9bbfc5f673cc3845d4a1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-63b400d9f60b8dde30d4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8ad21699d0438f449ad2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f28017466ca667f59ce9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-W-out-17; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a10daebbead436339ebc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ba289f6454992baee85a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3daf1c0068f7510a7d2a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-405e0528d0ff5daa18c7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-W-out-19; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2bc7a89822116ebcedb9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f1483b205594cf4ced7e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6f3a9eb33c16f26ef5ac">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9dd485572fa392d2fab6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-N-out-22; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-70ee562101147db491ff">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b9e7b5e0ca080167fc73">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6c0733360a4e8a8d1622">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-86968453707d6118cc30">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-N-out-24; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-043d025c03de4f13ccd7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-32d6ac38339f4120e374">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1ef0d53549ee762821d5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cdde890edb76a4ea5553">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: 2-N-in-1; to port: 1-W-out-1; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-068afd5d04630eb0a817"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-068afd5d04630eb0a817`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-1; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-760a6e551a67b6cf2898"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-760a6e551a67b6cf2898`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-1; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-884e1b24921b9426d69f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-884e1b24921b9426d69f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-1; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7ac4fbacdf0ddd9224de"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7ac4fbacdf0ddd9224de`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-1; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-N-in-1; to port: 1-W-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9e73a7e3bccf3ac5cdcd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9e73a7e3bccf3ac5cdcd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ce7f0f9e5af6719c85ca"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ce7f0f9e5af6719c85ca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ac96b573558ec65fd3a9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ac96b573558ec65fd3a9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5a355b9ebcb2e66cd613"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5a355b9ebcb2e66cd613`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-N-in-1; to port: 1-E-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8edc1cc5e26482252bbb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8edc1cc5e26482252bbb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-E-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-20dc195a172c27d1e8b6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-20dc195a172c27d1e8b6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-E-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-73b305935dac9d7d27c7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-73b305935dac9d7d27c7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-E-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-acffd45413b07628b39e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-acffd45413b07628b39e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-E-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-N-in-1; to port: 1-W-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7ffdca674b60c7e037d3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7ffdca674b60c7e037d3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ac5c70acb795fa710e13"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ac5c70acb795fa710e13`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9fefee5656a9bcc69a04"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9fefee5656a9bcc69a04`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-77fafeb69c615ddd0e8d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-77fafeb69c615ddd0e8d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-N-in-1; to port: 1-W-out-11; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c43bcec27de64c8e16d8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c43bcec27de64c8e16d8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-11; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-867c8c937f8beeabeb79"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-867c8c937f8beeabeb79`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-11; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0be919dd7bc4edb6a2f5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0be919dd7bc4edb6a2f5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-11; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2ef28efb5eac258e05fb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2ef28efb5eac258e05fb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-11; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-N-in-1; to port: 1-W-out-12; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c02562975d17053335fc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c02562975d17053335fc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-12; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-da784e5481090f9a0711"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-da784e5481090f9a0711`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-12; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f1fceb41ce8589a5df37"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f1fceb41ce8589a5df37`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-12; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8cc3824504103ca6f169"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8cc3824504103ca6f169`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-12; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-N-in-1; to port: 1-E-out-13; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6c5c2b2b490e1fff1f62"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6c5c2b2b490e1fff1f62`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-E-out-13; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8d3f180bb52857c6ab12"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8d3f180bb52857c6ab12`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-E-out-13; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fdd26b750172ac4fe53b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fdd26b750172ac4fe53b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-E-out-13; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dccb922ca52483eebaa1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dccb922ca52483eebaa1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-E-out-13; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-N-in-1; to port: 1-E-out-14; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1d66ccc315a599e3bf34"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1d66ccc315a599e3bf34`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-E-out-14; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f3628d099e0265b35789"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f3628d099e0265b35789`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-E-out-14; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e5c1f5c3808de8156cf3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e5c1f5c3808de8156cf3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-E-out-14; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d8aca6d07f85d90aafa6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d8aca6d07f85d90aafa6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-E-out-14; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-N-in-1; to port: 1-W-out-17; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-63e341ec390373a6d3b3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-63e341ec390373a6d3b3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-17; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ab8d2dba2ac6bff9cd57"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ab8d2dba2ac6bff9cd57`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-17; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6cf518bc0856e7cd4e57"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6cf518bc0856e7cd4e57`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-17; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a3a3f4d88ecf21534a51"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a3a3f4d88ecf21534a51`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-17; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-N-in-1; to port: 1-W-out-19; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-98be73ca8d2835805f29"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-98be73ca8d2835805f29`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-19; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-651e5b564ff2b360c099"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-651e5b564ff2b360c099`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-19; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8593bd4fd33ee83f57cb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8593bd4fd33ee83f57cb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-19; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-216970b3990cd8ecb9c0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-216970b3990cd8ecb9c0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-19; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-N-in-1; to port: 1-N-out-22; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e5b506bc96d990774565"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e5b506bc96d990774565`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-N-out-22; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-819afcba9b94f559a0f8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-819afcba9b94f559a0f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-N-out-22; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b5fb1b38ebf8c198e958"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b5fb1b38ebf8c198e958`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-N-out-22; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-435a14fd6cbefe02bbbe"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-435a14fd6cbefe02bbbe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-N-out-22; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-N-in-1; to port: 1-N-out-24; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-aa90ff0eba6b7df408af"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-aa90ff0eba6b7df408af`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-N-out-24; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9f170a110ef9dd5e813f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9f170a110ef9dd5e813f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-N-out-24; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-340e83913250894e9f17"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-340e83913250894e9f17`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-N-out-24; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e83433db110989f8e38d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e83433db110989f8e38d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-N-out-24; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-W-out-1; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-96add150c70ca306c29e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-96add150c70ca306c29e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-1; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2307d64064d783ab0fe6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2307d64064d783ab0fe6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-1; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-62be5a61830b92aea96a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-62be5a61830b92aea96a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-1; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b692dd8b56e6ba551b64"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b692dd8b56e6ba551b64`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-1; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-W-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-652c9b75e15491beff5b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-652c9b75e15491beff5b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5d0d371416f419c60f22"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5d0d371416f419c60f22`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4efcb45237581973b77d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4efcb45237581973b77d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a24cbb0f84f97dcdbf7b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a24cbb0f84f97dcdbf7b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-E-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b8c0e1cf53c069ffa9c5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b8c0e1cf53c069ffa9c5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-054d56e34daa60125b1f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-054d56e34daa60125b1f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-17d3864a2b9e6b0d7e01"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-17d3864a2b9e6b0d7e01`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7faf2aac49377a64e6cc"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7faf2aac49377a64e6cc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-W-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ac7d89934e82fb6a4c82"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ac7d89934e82fb6a4c82`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-47d30733f1e5d1f0e501"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-47d30733f1e5d1f0e501`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-444ec3951410de8261dc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-444ec3951410de8261dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-466e475304c8b588af28"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-466e475304c8b588af28`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-7; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-W-out-11; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-23fba44891ada629af8c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-23fba44891ada629af8c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-11; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a485b427cdcf02b2e78b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a485b427cdcf02b2e78b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-11; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4795e054db47bb95ba28"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4795e054db47bb95ba28`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-11; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-052b122537d7d48c96e3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-052b122537d7d48c96e3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-11; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-W-out-12; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-70457536e3ad8edf9b62"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-70457536e3ad8edf9b62`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-12; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1c406b7faa9fc214e583"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1c406b7faa9fc214e583`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-12; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4f51cdd62a210ec6bbe2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4f51cdd62a210ec6bbe2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-12; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f8f920dfa5453ad4c6f4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f8f920dfa5453ad4c6f4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-12; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-E-out-13; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-df354657735203bd22a6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-df354657735203bd22a6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-13; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1c7dc80ad9e445d334e0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1c7dc80ad9e445d334e0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-13; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f79d07bbfe7de96628a4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f79d07bbfe7de96628a4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-13; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-673832c793d6229eada3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-673832c793d6229eada3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-13; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-E-out-14; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9bbfc5f673cc3845d4a1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9bbfc5f673cc3845d4a1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-14; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-63b400d9f60b8dde30d4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-63b400d9f60b8dde30d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-14; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8ad21699d0438f449ad2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8ad21699d0438f449ad2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-14; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f28017466ca667f59ce9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f28017466ca667f59ce9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-14; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-W-out-17; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a10daebbead436339ebc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a10daebbead436339ebc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-17; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ba289f6454992baee85a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ba289f6454992baee85a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-17; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3daf1c0068f7510a7d2a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3daf1c0068f7510a7d2a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-17; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-405e0528d0ff5daa18c7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-405e0528d0ff5daa18c7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-17; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-W-out-19; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2bc7a89822116ebcedb9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2bc7a89822116ebcedb9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-19; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f1483b205594cf4ced7e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f1483b205594cf4ced7e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-19; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6f3a9eb33c16f26ef5ac"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6f3a9eb33c16f26ef5ac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-19; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9dd485572fa392d2fab6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9dd485572fa392d2fab6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-19; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-N-out-22; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-70ee562101147db491ff"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-70ee562101147db491ff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-22; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b9e7b5e0ca080167fc73"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b9e7b5e0ca080167fc73`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-22; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6c0733360a4e8a8d1622"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6c0733360a4e8a8d1622`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-22; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-86968453707d6118cc30"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-86968453707d6118cc30`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-22; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-N-out-24; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-043d025c03de4f13ccd7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-043d025c03de4f13ccd7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-24; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-32d6ac38339f4120e374"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-32d6ac38339f4120e374`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-24; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1ef0d53549ee762821d5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1ef0d53549ee762821d5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-24; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cdde890edb76a4ea5553"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cdde890edb76a4ea5553`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-24; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — pedestrian → pedestrian — 8 cases; unverified: 8</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 2-W-out-2; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3f9b449d6326a1c07276">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-394f6e0bbf1c7327c74c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3089e1a47ee346a06f1c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2a88cb67bc15f270085f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 2-E-out-3; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d1ff89f4be378cb28e6c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-25f56dd922ed70ac2ddf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a155190f27c5c5faf48a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-307151838b8c11a24559">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: 2-N-in-1; to port: 2-W-out-2; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3f9b449d6326a1c07276"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3f9b449d6326a1c07276`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 2-W-out-2; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-394f6e0bbf1c7327c74c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-394f6e0bbf1c7327c74c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 2-W-out-2; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3089e1a47ee346a06f1c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3089e1a47ee346a06f1c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 2-W-out-2; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2a88cb67bc15f270085f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2a88cb67bc15f270085f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 2-W-out-2; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 2-E-out-3; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d1ff89f4be378cb28e6c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d1ff89f4be378cb28e6c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 2-E-out-3; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-25f56dd922ed70ac2ddf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-25f56dd922ed70ac2ddf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 2-E-out-3; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a155190f27c5c5faf48a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a155190f27c5c5faf48a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 2-E-out-3; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-307151838b8c11a24559"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-307151838b8c11a24559`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 2-E-out-3; from service: pedestrian; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The previous experimental stamp included curved branch throats and six extra wing cells. The corrected partition keeps a straight 21-cell stamp, transfers those six construction cells to full ramp owners, and moves all curved high-throat faces into the separately placed ramps. The independent partition audit preserves assembled geometry, UVs, materials, winding, and traffic routes, subject only to the exact float32 re-encoding required by a changed model anchor. Earlier renders and game observations do not approve this corrected ownership split.
