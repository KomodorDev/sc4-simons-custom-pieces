---
title: "Testing: DD RHW-4 \u2014 Diagonal Highway and Slip-Lane Stamp"
summary: "Inspect this piece\u2019s exact checks, resource evidence, and explicit human observations."
audience: "contributors"
document_type: "reference"
---

# Testing: DD RHW-4 — Diagonal Highway and Slip-Lane Stamp

<!-- PIECE TESTING LAYOUT: 1 -->

[Piece overview ↗ (README)](README.md) · [1. Test scope](#1-test-scope) · [2. Test setup](#2-test-setup) · [3. Software checks](#3-software-checks) · [4. Game checks](#4-game-checks) · [5. Results and known issues](#5-results-and-known-issues) · [6. Design history](#6-design-history)

## 1. Test scope

Inspect the exact `ddrhw-modular-highway-stamp` resources, its complete intrinsic journeys, and its separately placed joins in the [modular assembly](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-modular-diamond/TESTING.md). The stamp retains native Avenue paths underneath the crossing. Two Avenue-only cells use pristine native pavement so that detached compact ramp artwork does not remain underneath the new layout.

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
| `1-N-in-5` | road / 1 / primary | in | [26.207444, -88.0, 6.745132]; [-0.20216938843111806, -0.9793505697049386]; 0.226756787 | `path-interface-85fe4503e80b365632f0` |
| `1-E-out-6` | road / 1 / primary | out | [40.0, -120.142765, 12.25824]; [0.9273187516299904, 0.3742725382330316]; -0.296094955 | `path-interface-5957ca3ff5e80e28e0b3` |
| `1-N-in-7` | road / 1 / primary | in | [44.8, -56.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-668896c488171c19873d` |
| `1-N-in-8` | road / 1 / primary | in | [51.2, -56.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `1-W-out-9` | road / 1 / primary | out | [56.0, -51.2, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `1-W-out-10` | road / 1 / primary | out | [56.0, -44.8, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `1-E-out-11` | road / 1 / primary | out | [72.0, -83.2, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `1-E-out-12` | road / 1 / primary | out | [72.0, -76.8, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `1-S-in-13` | road / 1 / primary | in | [76.8, -72.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `1-S-in-14` | road / 1 / primary | in | [83.2, -72.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-668896c488171c19873d` |
| `1-W-out-15` | road / 1 / primary | out | [88.0, -26.207444, 6.745132]; [-0.9793505697049386, -0.20216938843111806]; -0.226756787 | `path-interface-20a6d5708b4a74c22702` |
| `1-S-in-16` | road / 1 / primary | in | [120.142765, -40.0, 12.25824]; [0.3742725382330316, 0.9273187516299904]; 0.296094955 | `path-interface-7af180e167c309b94d05` |
| `1-N-in-17` | road / 1 / primary | in | [140.8, 8.0, 7.5]; [-0.7071067811865483, -0.7071067811865467]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `1-N-out-18` | road / 1 / primary | out | [140.8, 8.0, 15.0]; [0.7071067811865483, 0.7071067811865467]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `1-N-in-19` | road / 1 / primary | in | [147.2, 8.0, 7.5]; [-0.7071067811865472, -0.7071067811865479]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `1-N-out-20` | road / 1 / primary | out | [147.2, 8.0, 15.0]; [0.7071067811865472, 0.7071067811865479]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `2-N-in-1` | pedestrian / 2 / primary | in | [40.7, -56.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-2ec6b824afff9b450810` |
| `2-W-out-2` | pedestrian / 2 / primary | out | [56.0, -40.7, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-ef45fb4474012bf121a0` |
| `2-E-out-3` | pedestrian / 2 / primary | out | [72.0, -87.3, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-ef45fb4474012bf121a0` |
| `2-S-in-4` | pedestrian / 2 / primary | in | [87.3, -72.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-2ec6b824afff9b450810` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `1-W-in-2` → `1-E-out-6` | primary |
| road | `1-W-in-2` → `1-N-out-20` | primary |
| road | `1-W-in-4` → `1-N-out-18` | primary |
| road | `1-N-in-5` → `1-W-out-3` | primary |
| road | `1-N-in-7` → `1-E-out-11` | primary |
| road | `1-N-in-8` → `1-E-out-12` | primary |
| road | `1-S-in-13` → `1-W-out-9` | primary |
| road | `1-S-in-14` → `1-W-out-10` | primary |
| road | `1-S-in-16` → `1-N-out-20` | primary |
| road | `1-N-in-17` → `1-W-out-15` | primary |
| road | `1-N-in-17` → `1-W-out-3` | primary |
| road | `1-N-in-19` → `1-W-out-1` | primary |
| pedestrian | `2-N-in-1` → `2-E-out-3` | primary |
| pedestrian | `2-S-in-4` → `2-W-out-2` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `1-W-in-2` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-W-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-W-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-E-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-E-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-W-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | road / `1-N-out-18` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-2` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | road / `1-E-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | road / `1-W-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | road / `1-W-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | road / `1-E-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | road / `1-E-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | road / `1-W-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | road / `1-N-out-20` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-4` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-E-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-W-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-W-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-E-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-E-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-W-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-N-out-18` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-N-out-20` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-7` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-7` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-7` | road / `1-E-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-7` | road / `1-W-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-7` | road / `1-W-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-7` | road / `1-E-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-7` | road / `1-W-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-7` | road / `1-N-out-18` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-7` | road / `1-N-out-20` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-7` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-7` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-8` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-8` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-8` | road / `1-E-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-8` | road / `1-W-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-8` | road / `1-W-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-8` | road / `1-E-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-8` | road / `1-W-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-8` | road / `1-N-out-18` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-8` | road / `1-N-out-20` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-8` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-8` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-13` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-13` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-13` | road / `1-E-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-13` | road / `1-W-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-13` | road / `1-E-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-13` | road / `1-E-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-13` | road / `1-W-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-13` | road / `1-N-out-18` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-13` | road / `1-N-out-20` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-13` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-13` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-14` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-14` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-14` | road / `1-E-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-14` | road / `1-W-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-14` | road / `1-E-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-14` | road / `1-E-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-14` | road / `1-W-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-14` | road / `1-N-out-18` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-14` | road / `1-N-out-20` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-14` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-14` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-16` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-16` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-16` | road / `1-E-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-16` | road / `1-W-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-16` | road / `1-W-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-16` | road / `1-E-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-16` | road / `1-E-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-16` | road / `1-W-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-16` | road / `1-N-out-18` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-16` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-16` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-17` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-17` | road / `1-E-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-17` | road / `1-W-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-17` | road / `1-W-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-17` | road / `1-E-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-17` | road / `1-E-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-17` | road / `1-N-out-18` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-17` | road / `1-N-out-20` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-17` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-17` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-19` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-19` | road / `1-E-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-19` | road / `1-W-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-19` | road / `1-W-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-19` | road / `1-E-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-19` | road / `1-E-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-19` | road / `1-W-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-19` | road / `1-N-out-18` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-19` | road / `1-N-out-20` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-19` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-19` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-N-in-1` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-N-in-1` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-N-in-1` | road / `1-E-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-N-in-1` | road / `1-W-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-N-in-1` | road / `1-W-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-N-in-1` | road / `1-E-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-N-in-1` | road / `1-E-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-N-in-1` | road / `1-W-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-N-in-1` | road / `1-N-out-18` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-N-in-1` | road / `1-N-out-20` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-N-in-1` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-S-in-4` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-S-in-4` | road / `1-W-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-S-in-4` | road / `1-E-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-S-in-4` | road / `1-W-out-9` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-S-in-4` | road / `1-W-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-S-in-4` | road / `1-E-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-S-in-4` | road / `1-E-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-S-in-4` | road / `1-W-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-S-in-4` | road / `1-N-out-18` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-S-in-4` | road / `1-N-out-20` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-S-in-4` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use Windows SimCity 4 with NAM 50 and right-hand traffic, including Wine or CrossOver. Follow the [shared build guide](../../../../docs/BUILD_AND_INSTALL.md) for exact input hashes and the captured Avenue dependency. Build the `ddrhw-modular-ramp-kit` set, then prepare the `modular-diagonal-diamond` Highways menu. Building does not install the result. Use flat terrain in a disposable city.

## 3. Software checks

From the repository root, run `python3 -B tools/run_tests.py`. After a local build, run `python3 -B custom-pieces/scp.py verify --output <build directory>`. The domain verifier reads saved PATH and S3D resources: it checks literal ownership, traffic direction, joins, grades below the 30% experimental ceiling, exact stamp references, adaptive resources where declared, model topology, and car corridors. The assembly evidence adds physical joining-profile and support checks. A software pass cannot confirm game appearance or vehicle travel.

## 4. Game checks

Place this component as described in the README and complete the assembly. Inspect each of the four rotations after clicking, rather than relying on the placement preview. For the stamp and terminals, extend the ordinary Avenue, develop nearby zoning, and inspect whether the sidewalk appears and rotates with the roads. Use Route Query on each permitted movement, watch a car complete it, confirm opposing-carriageway turns remain unavailable, save, close the city, and reload. Record an observation only for the exact checklist case actually inspected.

## 5. Results and known issues

The independent source tests and saved-resource reports have separate scopes. The generated checklist below retains their case states and explicit human observations. Every game result for this new subject starts unverified. The experimental 30% grade ceiling exceeds normal real-world highway practice; this compact game family does not claim real-road design approval or native MIS/FLEX interoperability.

<!-- BEGIN MANUAL SUMMARY -->

### Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/3 applicable cases passed; 0 failed, 0 stale.
- [ ] In-game rendering: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Route Query: 0/56 applicable cases passed; 0 failed, 0 stale.
- [ ] Visible travel: 0/56 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 653, passed: 0, failed: 0, stale: 0, not_applicable: 0.

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
<summary>Route Query — road — 48 cases; unverified: 48</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-6; entry: 1-W-in-2; exit: 1-E-out-6 | — | <a href="#case-in_game_route_query-970fc5a9b1d0a8c2372a">[ ] unverified</a> | <a href="#case-in_game_route_query-8d509db94c6599649552">[ ] unverified</a> | <a href="#case-in_game_route_query-c33020a3e21fae47cd95">[ ] unverified</a> | <a href="#case-in_game_route_query-cf08aa444678af25fea9">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-20; entry: 1-W-in-2; exit: 1-N-out-20 | — | <a href="#case-in_game_route_query-5a1d5c5a6d49fee5445c">[ ] unverified</a> | <a href="#case-in_game_route_query-b7a6fb76a381a5a69f53">[ ] unverified</a> | <a href="#case-in_game_route_query-67635cd1c812f70dc7ea">[ ] unverified</a> | <a href="#case-in_game_route_query-8de4e5ac3e4c7411d46f">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-18; entry: 1-W-in-4; exit: 1-N-out-18 | — | <a href="#case-in_game_route_query-a3aff6dcd302447428bb">[ ] unverified</a> | <a href="#case-in_game_route_query-26f3dbdc99408c9c2f4f">[ ] unverified</a> | <a href="#case-in_game_route_query-6097042d68bb1f45e974">[ ] unverified</a> | <a href="#case-in_game_route_query-3af761bdb69f5995b020">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3 | — | <a href="#case-in_game_route_query-b3c07d4ff49097bc85fb">[ ] unverified</a> | <a href="#case-in_game_route_query-297d785345889b7f1643">[ ] unverified</a> | <a href="#case-in_game_route_query-b498ad3d94fdf3097d74">[ ] unverified</a> | <a href="#case-in_game_route_query-2c4ab5415aceb2ebef89">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-7>1-E-out-11; entry: 1-N-in-7; exit: 1-E-out-11 | — | <a href="#case-in_game_route_query-77ae9cee788b8980a1bc">[ ] unverified</a> | <a href="#case-in_game_route_query-f2fc329772540575f90f">[ ] unverified</a> | <a href="#case-in_game_route_query-f025827f93361560782e">[ ] unverified</a> | <a href="#case-in_game_route_query-0ea5b165af8278477b27">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-8>1-E-out-12; entry: 1-N-in-8; exit: 1-E-out-12 | — | <a href="#case-in_game_route_query-4374b03403ce80fb5790">[ ] unverified</a> | <a href="#case-in_game_route_query-c9cda5fadf5e444065dc">[ ] unverified</a> | <a href="#case-in_game_route_query-a2430683019081547ab1">[ ] unverified</a> | <a href="#case-in_game_route_query-ee009412bb3e0a0058aa">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-S-in-13>1-W-out-9; entry: 1-S-in-13; exit: 1-W-out-9 | — | <a href="#case-in_game_route_query-b2dff0b763d01837833a">[ ] unverified</a> | <a href="#case-in_game_route_query-70468881c16fd77a663a">[ ] unverified</a> | <a href="#case-in_game_route_query-d778675f373dc8a9674f">[ ] unverified</a> | <a href="#case-in_game_route_query-ccc04b9826abb6e469cf">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-S-in-14>1-W-out-10; entry: 1-S-in-14; exit: 1-W-out-10 | — | <a href="#case-in_game_route_query-b386e673161cc3353f56">[ ] unverified</a> | <a href="#case-in_game_route_query-76ac6ca31189a55e072c">[ ] unverified</a> | <a href="#case-in_game_route_query-61bffbe2e2c13d77ed3b">[ ] unverified</a> | <a href="#case-in_game_route_query-cc996ede3c27617e32b6">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-S-in-16>1-N-out-20; entry: 1-S-in-16; exit: 1-N-out-20 | — | <a href="#case-in_game_route_query-993d0ba38b14cb3cbcf1">[ ] unverified</a> | <a href="#case-in_game_route_query-b47f23bbc30785f5ccce">[ ] unverified</a> | <a href="#case-in_game_route_query-1c50012a8b078d8c54f1">[ ] unverified</a> | <a href="#case-in_game_route_query-c58fba00ef6094d883dc">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-17>1-W-out-15; entry: 1-N-in-17; exit: 1-W-out-15 | — | <a href="#case-in_game_route_query-8f61501a127ecfa4cc66">[ ] unverified</a> | <a href="#case-in_game_route_query-912a4b6462517796fe06">[ ] unverified</a> | <a href="#case-in_game_route_query-7d74f592e247ec16b770">[ ] unverified</a> | <a href="#case-in_game_route_query-2f87e2ce025bcdb12690">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-17>1-W-out-3; entry: 1-N-in-17; exit: 1-W-out-3 | — | <a href="#case-in_game_route_query-d128aebf7134c1a61f8a">[ ] unverified</a> | <a href="#case-in_game_route_query-b14079296b4b0efb6a0e">[ ] unverified</a> | <a href="#case-in_game_route_query-df48d610b1ff017870c2">[ ] unverified</a> | <a href="#case-in_game_route_query-fdda86d9a449ec5781ff">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-19>1-W-out-1; entry: 1-N-in-19; exit: 1-W-out-1 | — | <a href="#case-in_game_route_query-90deaa158fa729894ee8">[ ] unverified</a> | <a href="#case-in_game_route_query-b6047f99c3d8621a00c0">[ ] unverified</a> | <a href="#case-in_game_route_query-190f62712e03d0096d3b">[ ] unverified</a> | <a href="#case-in_game_route_query-a4c248b3a3b66598e979">[ ] unverified</a> |


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
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-20; entry: 1-W-in-2; exit: 1-N-out-20</summary>

<a id="case-in_game_route_query-5a1d5c5a6d49fee5445c"></a>

**0° CCW: unverified** — `in_game_route_query-5a1d5c5a6d49fee5445c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-20; entry: 1-W-in-2; exit: 1-N-out-20.

No observation recorded.

<a id="case-in_game_route_query-b7a6fb76a381a5a69f53"></a>

**90° CCW: unverified** — `in_game_route_query-b7a6fb76a381a5a69f53`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-20; entry: 1-W-in-2; exit: 1-N-out-20.

No observation recorded.

<a id="case-in_game_route_query-67635cd1c812f70dc7ea"></a>

**180° CCW: unverified** — `in_game_route_query-67635cd1c812f70dc7ea`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-20; entry: 1-W-in-2; exit: 1-N-out-20.

No observation recorded.

<a id="case-in_game_route_query-8de4e5ac3e4c7411d46f"></a>

**270° CCW: unverified** — `in_game_route_query-8de4e5ac3e4c7411d46f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-20; entry: 1-W-in-2; exit: 1-N-out-20.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-18; entry: 1-W-in-4; exit: 1-N-out-18</summary>

<a id="case-in_game_route_query-a3aff6dcd302447428bb"></a>

**0° CCW: unverified** — `in_game_route_query-a3aff6dcd302447428bb`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-18; entry: 1-W-in-4; exit: 1-N-out-18.

No observation recorded.

<a id="case-in_game_route_query-26f3dbdc99408c9c2f4f"></a>

**90° CCW: unverified** — `in_game_route_query-26f3dbdc99408c9c2f4f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-18; entry: 1-W-in-4; exit: 1-N-out-18.

No observation recorded.

<a id="case-in_game_route_query-6097042d68bb1f45e974"></a>

**180° CCW: unverified** — `in_game_route_query-6097042d68bb1f45e974`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-18; entry: 1-W-in-4; exit: 1-N-out-18.

No observation recorded.

<a id="case-in_game_route_query-3af761bdb69f5995b020"></a>

**270° CCW: unverified** — `in_game_route_query-3af761bdb69f5995b020`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-18; entry: 1-W-in-4; exit: 1-N-out-18.

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
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-7>1-E-out-11; entry: 1-N-in-7; exit: 1-E-out-11</summary>

<a id="case-in_game_route_query-77ae9cee788b8980a1bc"></a>

**0° CCW: unverified** — `in_game_route_query-77ae9cee788b8980a1bc`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-7>1-E-out-11; entry: 1-N-in-7; exit: 1-E-out-11.

No observation recorded.

<a id="case-in_game_route_query-f2fc329772540575f90f"></a>

**90° CCW: unverified** — `in_game_route_query-f2fc329772540575f90f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-7>1-E-out-11; entry: 1-N-in-7; exit: 1-E-out-11.

No observation recorded.

<a id="case-in_game_route_query-f025827f93361560782e"></a>

**180° CCW: unverified** — `in_game_route_query-f025827f93361560782e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-7>1-E-out-11; entry: 1-N-in-7; exit: 1-E-out-11.

No observation recorded.

<a id="case-in_game_route_query-0ea5b165af8278477b27"></a>

**270° CCW: unverified** — `in_game_route_query-0ea5b165af8278477b27`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-7>1-E-out-11; entry: 1-N-in-7; exit: 1-E-out-11.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-8>1-E-out-12; entry: 1-N-in-8; exit: 1-E-out-12</summary>

<a id="case-in_game_route_query-4374b03403ce80fb5790"></a>

**0° CCW: unverified** — `in_game_route_query-4374b03403ce80fb5790`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-8>1-E-out-12; entry: 1-N-in-8; exit: 1-E-out-12.

No observation recorded.

<a id="case-in_game_route_query-c9cda5fadf5e444065dc"></a>

**90° CCW: unverified** — `in_game_route_query-c9cda5fadf5e444065dc`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-8>1-E-out-12; entry: 1-N-in-8; exit: 1-E-out-12.

No observation recorded.

<a id="case-in_game_route_query-a2430683019081547ab1"></a>

**180° CCW: unverified** — `in_game_route_query-a2430683019081547ab1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-8>1-E-out-12; entry: 1-N-in-8; exit: 1-E-out-12.

No observation recorded.

<a id="case-in_game_route_query-ee009412bb3e0a0058aa"></a>

**270° CCW: unverified** — `in_game_route_query-ee009412bb3e0a0058aa`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-8>1-E-out-12; entry: 1-N-in-8; exit: 1-E-out-12.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-S-in-13>1-W-out-9; entry: 1-S-in-13; exit: 1-W-out-9</summary>

<a id="case-in_game_route_query-b2dff0b763d01837833a"></a>

**0° CCW: unverified** — `in_game_route_query-b2dff0b763d01837833a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-13>1-W-out-9; entry: 1-S-in-13; exit: 1-W-out-9.

No observation recorded.

<a id="case-in_game_route_query-70468881c16fd77a663a"></a>

**90° CCW: unverified** — `in_game_route_query-70468881c16fd77a663a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-13>1-W-out-9; entry: 1-S-in-13; exit: 1-W-out-9.

No observation recorded.

<a id="case-in_game_route_query-d778675f373dc8a9674f"></a>

**180° CCW: unverified** — `in_game_route_query-d778675f373dc8a9674f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-13>1-W-out-9; entry: 1-S-in-13; exit: 1-W-out-9.

No observation recorded.

<a id="case-in_game_route_query-ccc04b9826abb6e469cf"></a>

**270° CCW: unverified** — `in_game_route_query-ccc04b9826abb6e469cf`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-13>1-W-out-9; entry: 1-S-in-13; exit: 1-W-out-9.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-S-in-14>1-W-out-10; entry: 1-S-in-14; exit: 1-W-out-10</summary>

<a id="case-in_game_route_query-b386e673161cc3353f56"></a>

**0° CCW: unverified** — `in_game_route_query-b386e673161cc3353f56`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-14>1-W-out-10; entry: 1-S-in-14; exit: 1-W-out-10.

No observation recorded.

<a id="case-in_game_route_query-76ac6ca31189a55e072c"></a>

**90° CCW: unverified** — `in_game_route_query-76ac6ca31189a55e072c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-14>1-W-out-10; entry: 1-S-in-14; exit: 1-W-out-10.

No observation recorded.

<a id="case-in_game_route_query-61bffbe2e2c13d77ed3b"></a>

**180° CCW: unverified** — `in_game_route_query-61bffbe2e2c13d77ed3b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-14>1-W-out-10; entry: 1-S-in-14; exit: 1-W-out-10.

No observation recorded.

<a id="case-in_game_route_query-cc996ede3c27617e32b6"></a>

**270° CCW: unverified** — `in_game_route_query-cc996ede3c27617e32b6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-14>1-W-out-10; entry: 1-S-in-14; exit: 1-W-out-10.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-S-in-16>1-N-out-20; entry: 1-S-in-16; exit: 1-N-out-20</summary>

<a id="case-in_game_route_query-993d0ba38b14cb3cbcf1"></a>

**0° CCW: unverified** — `in_game_route_query-993d0ba38b14cb3cbcf1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-16>1-N-out-20; entry: 1-S-in-16; exit: 1-N-out-20.

No observation recorded.

<a id="case-in_game_route_query-b47f23bbc30785f5ccce"></a>

**90° CCW: unverified** — `in_game_route_query-b47f23bbc30785f5ccce`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-16>1-N-out-20; entry: 1-S-in-16; exit: 1-N-out-20.

No observation recorded.

<a id="case-in_game_route_query-1c50012a8b078d8c54f1"></a>

**180° CCW: unverified** — `in_game_route_query-1c50012a8b078d8c54f1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-16>1-N-out-20; entry: 1-S-in-16; exit: 1-N-out-20.

No observation recorded.

<a id="case-in_game_route_query-c58fba00ef6094d883dc"></a>

**270° CCW: unverified** — `in_game_route_query-c58fba00ef6094d883dc`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-16>1-N-out-20; entry: 1-S-in-16; exit: 1-N-out-20.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-17>1-W-out-15; entry: 1-N-in-17; exit: 1-W-out-15</summary>

<a id="case-in_game_route_query-8f61501a127ecfa4cc66"></a>

**0° CCW: unverified** — `in_game_route_query-8f61501a127ecfa4cc66`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-17>1-W-out-15; entry: 1-N-in-17; exit: 1-W-out-15.

No observation recorded.

<a id="case-in_game_route_query-912a4b6462517796fe06"></a>

**90° CCW: unverified** — `in_game_route_query-912a4b6462517796fe06`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-17>1-W-out-15; entry: 1-N-in-17; exit: 1-W-out-15.

No observation recorded.

<a id="case-in_game_route_query-7d74f592e247ec16b770"></a>

**180° CCW: unverified** — `in_game_route_query-7d74f592e247ec16b770`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-17>1-W-out-15; entry: 1-N-in-17; exit: 1-W-out-15.

No observation recorded.

<a id="case-in_game_route_query-2f87e2ce025bcdb12690"></a>

**270° CCW: unverified** — `in_game_route_query-2f87e2ce025bcdb12690`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-17>1-W-out-15; entry: 1-N-in-17; exit: 1-W-out-15.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-17>1-W-out-3; entry: 1-N-in-17; exit: 1-W-out-3</summary>

<a id="case-in_game_route_query-d128aebf7134c1a61f8a"></a>

**0° CCW: unverified** — `in_game_route_query-d128aebf7134c1a61f8a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-17>1-W-out-3; entry: 1-N-in-17; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_route_query-b14079296b4b0efb6a0e"></a>

**90° CCW: unverified** — `in_game_route_query-b14079296b4b0efb6a0e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-17>1-W-out-3; entry: 1-N-in-17; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_route_query-df48d610b1ff017870c2"></a>

**180° CCW: unverified** — `in_game_route_query-df48d610b1ff017870c2`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-17>1-W-out-3; entry: 1-N-in-17; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_route_query-fdda86d9a449ec5781ff"></a>

**270° CCW: unverified** — `in_game_route_query-fdda86d9a449ec5781ff`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-17>1-W-out-3; entry: 1-N-in-17; exit: 1-W-out-3.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-19>1-W-out-1; entry: 1-N-in-19; exit: 1-W-out-1</summary>

<a id="case-in_game_route_query-90deaa158fa729894ee8"></a>

**0° CCW: unverified** — `in_game_route_query-90deaa158fa729894ee8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-19>1-W-out-1; entry: 1-N-in-19; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_route_query-b6047f99c3d8621a00c0"></a>

**90° CCW: unverified** — `in_game_route_query-b6047f99c3d8621a00c0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-19>1-W-out-1; entry: 1-N-in-19; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_route_query-190f62712e03d0096d3b"></a>

**180° CCW: unverified** — `in_game_route_query-190f62712e03d0096d3b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-19>1-W-out-1; entry: 1-N-in-19; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_route_query-a4c248b3a3b66598e979"></a>

**270° CCW: unverified** — `in_game_route_query-a4c248b3a3b66598e979`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-19>1-W-out-1; entry: 1-N-in-19; exit: 1-W-out-1.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 48 cases; unverified: 48</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-2>1-E-out-6; entry: 1-W-in-2; exit: 1-E-out-6 | — | <a href="#case-in_game_visible_travel-970fc5a9b1d0a8c2372a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8d509db94c6599649552">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c33020a3e21fae47cd95">[ ] unverified</a> | <a href="#case-in_game_visible_travel-cf08aa444678af25fea9">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-20; entry: 1-W-in-2; exit: 1-N-out-20 | — | <a href="#case-in_game_visible_travel-5a1d5c5a6d49fee5445c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b7a6fb76a381a5a69f53">[ ] unverified</a> | <a href="#case-in_game_visible_travel-67635cd1c812f70dc7ea">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8de4e5ac3e4c7411d46f">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-18; entry: 1-W-in-4; exit: 1-N-out-18 | — | <a href="#case-in_game_visible_travel-a3aff6dcd302447428bb">[ ] unverified</a> | <a href="#case-in_game_visible_travel-26f3dbdc99408c9c2f4f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6097042d68bb1f45e974">[ ] unverified</a> | <a href="#case-in_game_visible_travel-3af761bdb69f5995b020">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-5>1-W-out-3; entry: 1-N-in-5; exit: 1-W-out-3 | — | <a href="#case-in_game_visible_travel-b3c07d4ff49097bc85fb">[ ] unverified</a> | <a href="#case-in_game_visible_travel-297d785345889b7f1643">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b498ad3d94fdf3097d74">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2c4ab5415aceb2ebef89">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-7>1-E-out-11; entry: 1-N-in-7; exit: 1-E-out-11 | — | <a href="#case-in_game_visible_travel-77ae9cee788b8980a1bc">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f2fc329772540575f90f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-f025827f93361560782e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-0ea5b165af8278477b27">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-8>1-E-out-12; entry: 1-N-in-8; exit: 1-E-out-12 | — | <a href="#case-in_game_visible_travel-4374b03403ce80fb5790">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c9cda5fadf5e444065dc">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a2430683019081547ab1">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ee009412bb3e0a0058aa">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-S-in-13>1-W-out-9; entry: 1-S-in-13; exit: 1-W-out-9 | — | <a href="#case-in_game_visible_travel-b2dff0b763d01837833a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-70468881c16fd77a663a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d778675f373dc8a9674f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ccc04b9826abb6e469cf">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-S-in-14>1-W-out-10; entry: 1-S-in-14; exit: 1-W-out-10 | — | <a href="#case-in_game_visible_travel-b386e673161cc3353f56">[ ] unverified</a> | <a href="#case-in_game_visible_travel-76ac6ca31189a55e072c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-61bffbe2e2c13d77ed3b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-cc996ede3c27617e32b6">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-S-in-16>1-N-out-20; entry: 1-S-in-16; exit: 1-N-out-20 | — | <a href="#case-in_game_visible_travel-993d0ba38b14cb3cbcf1">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b47f23bbc30785f5ccce">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1c50012a8b078d8c54f1">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c58fba00ef6094d883dc">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-17>1-W-out-15; entry: 1-N-in-17; exit: 1-W-out-15 | — | <a href="#case-in_game_visible_travel-8f61501a127ecfa4cc66">[ ] unverified</a> | <a href="#case-in_game_visible_travel-912a4b6462517796fe06">[ ] unverified</a> | <a href="#case-in_game_visible_travel-7d74f592e247ec16b770">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2f87e2ce025bcdb12690">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-17>1-W-out-3; entry: 1-N-in-17; exit: 1-W-out-3 | — | <a href="#case-in_game_visible_travel-d128aebf7134c1a61f8a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b14079296b4b0efb6a0e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-df48d610b1ff017870c2">[ ] unverified</a> | <a href="#case-in_game_visible_travel-fdda86d9a449ec5781ff">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-19>1-W-out-1; entry: 1-N-in-19; exit: 1-W-out-1 | — | <a href="#case-in_game_visible_travel-90deaa158fa729894ee8">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b6047f99c3d8621a00c0">[ ] unverified</a> | <a href="#case-in_game_visible_travel-190f62712e03d0096d3b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a4c248b3a3b66598e979">[ ] unverified</a> |


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
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-20; entry: 1-W-in-2; exit: 1-N-out-20</summary>

<a id="case-in_game_visible_travel-5a1d5c5a6d49fee5445c"></a>

**0° CCW: unverified** — `in_game_visible_travel-5a1d5c5a6d49fee5445c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-20; entry: 1-W-in-2; exit: 1-N-out-20.

No observation recorded.

<a id="case-in_game_visible_travel-b7a6fb76a381a5a69f53"></a>

**90° CCW: unverified** — `in_game_visible_travel-b7a6fb76a381a5a69f53`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-20; entry: 1-W-in-2; exit: 1-N-out-20.

No observation recorded.

<a id="case-in_game_visible_travel-67635cd1c812f70dc7ea"></a>

**180° CCW: unverified** — `in_game_visible_travel-67635cd1c812f70dc7ea`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-20; entry: 1-W-in-2; exit: 1-N-out-20.

No observation recorded.

<a id="case-in_game_visible_travel-8de4e5ac3e4c7411d46f"></a>

**270° CCW: unverified** — `in_game_visible_travel-8de4e5ac3e4c7411d46f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-2>1-N-out-20; entry: 1-W-in-2; exit: 1-N-out-20.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-18; entry: 1-W-in-4; exit: 1-N-out-18</summary>

<a id="case-in_game_visible_travel-a3aff6dcd302447428bb"></a>

**0° CCW: unverified** — `in_game_visible_travel-a3aff6dcd302447428bb`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-18; entry: 1-W-in-4; exit: 1-N-out-18.

No observation recorded.

<a id="case-in_game_visible_travel-26f3dbdc99408c9c2f4f"></a>

**90° CCW: unverified** — `in_game_visible_travel-26f3dbdc99408c9c2f4f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-18; entry: 1-W-in-4; exit: 1-N-out-18.

No observation recorded.

<a id="case-in_game_visible_travel-6097042d68bb1f45e974"></a>

**180° CCW: unverified** — `in_game_visible_travel-6097042d68bb1f45e974`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-18; entry: 1-W-in-4; exit: 1-N-out-18.

No observation recorded.

<a id="case-in_game_visible_travel-3af761bdb69f5995b020"></a>

**270° CCW: unverified** — `in_game_visible_travel-3af761bdb69f5995b020`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-4>1-N-out-18; entry: 1-W-in-4; exit: 1-N-out-18.

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
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-7>1-E-out-11; entry: 1-N-in-7; exit: 1-E-out-11</summary>

<a id="case-in_game_visible_travel-77ae9cee788b8980a1bc"></a>

**0° CCW: unverified** — `in_game_visible_travel-77ae9cee788b8980a1bc`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-7>1-E-out-11; entry: 1-N-in-7; exit: 1-E-out-11.

No observation recorded.

<a id="case-in_game_visible_travel-f2fc329772540575f90f"></a>

**90° CCW: unverified** — `in_game_visible_travel-f2fc329772540575f90f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-7>1-E-out-11; entry: 1-N-in-7; exit: 1-E-out-11.

No observation recorded.

<a id="case-in_game_visible_travel-f025827f93361560782e"></a>

**180° CCW: unverified** — `in_game_visible_travel-f025827f93361560782e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-7>1-E-out-11; entry: 1-N-in-7; exit: 1-E-out-11.

No observation recorded.

<a id="case-in_game_visible_travel-0ea5b165af8278477b27"></a>

**270° CCW: unverified** — `in_game_visible_travel-0ea5b165af8278477b27`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-7>1-E-out-11; entry: 1-N-in-7; exit: 1-E-out-11.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-8>1-E-out-12; entry: 1-N-in-8; exit: 1-E-out-12</summary>

<a id="case-in_game_visible_travel-4374b03403ce80fb5790"></a>

**0° CCW: unverified** — `in_game_visible_travel-4374b03403ce80fb5790`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-8>1-E-out-12; entry: 1-N-in-8; exit: 1-E-out-12.

No observation recorded.

<a id="case-in_game_visible_travel-c9cda5fadf5e444065dc"></a>

**90° CCW: unverified** — `in_game_visible_travel-c9cda5fadf5e444065dc`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-8>1-E-out-12; entry: 1-N-in-8; exit: 1-E-out-12.

No observation recorded.

<a id="case-in_game_visible_travel-a2430683019081547ab1"></a>

**180° CCW: unverified** — `in_game_visible_travel-a2430683019081547ab1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-8>1-E-out-12; entry: 1-N-in-8; exit: 1-E-out-12.

No observation recorded.

<a id="case-in_game_visible_travel-ee009412bb3e0a0058aa"></a>

**270° CCW: unverified** — `in_game_visible_travel-ee009412bb3e0a0058aa`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-8>1-E-out-12; entry: 1-N-in-8; exit: 1-E-out-12.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-S-in-13>1-W-out-9; entry: 1-S-in-13; exit: 1-W-out-9</summary>

<a id="case-in_game_visible_travel-b2dff0b763d01837833a"></a>

**0° CCW: unverified** — `in_game_visible_travel-b2dff0b763d01837833a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-13>1-W-out-9; entry: 1-S-in-13; exit: 1-W-out-9.

No observation recorded.

<a id="case-in_game_visible_travel-70468881c16fd77a663a"></a>

**90° CCW: unverified** — `in_game_visible_travel-70468881c16fd77a663a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-13>1-W-out-9; entry: 1-S-in-13; exit: 1-W-out-9.

No observation recorded.

<a id="case-in_game_visible_travel-d778675f373dc8a9674f"></a>

**180° CCW: unverified** — `in_game_visible_travel-d778675f373dc8a9674f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-13>1-W-out-9; entry: 1-S-in-13; exit: 1-W-out-9.

No observation recorded.

<a id="case-in_game_visible_travel-ccc04b9826abb6e469cf"></a>

**270° CCW: unverified** — `in_game_visible_travel-ccc04b9826abb6e469cf`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-13>1-W-out-9; entry: 1-S-in-13; exit: 1-W-out-9.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-S-in-14>1-W-out-10; entry: 1-S-in-14; exit: 1-W-out-10</summary>

<a id="case-in_game_visible_travel-b386e673161cc3353f56"></a>

**0° CCW: unverified** — `in_game_visible_travel-b386e673161cc3353f56`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-14>1-W-out-10; entry: 1-S-in-14; exit: 1-W-out-10.

No observation recorded.

<a id="case-in_game_visible_travel-76ac6ca31189a55e072c"></a>

**90° CCW: unverified** — `in_game_visible_travel-76ac6ca31189a55e072c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-14>1-W-out-10; entry: 1-S-in-14; exit: 1-W-out-10.

No observation recorded.

<a id="case-in_game_visible_travel-61bffbe2e2c13d77ed3b"></a>

**180° CCW: unverified** — `in_game_visible_travel-61bffbe2e2c13d77ed3b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-14>1-W-out-10; entry: 1-S-in-14; exit: 1-W-out-10.

No observation recorded.

<a id="case-in_game_visible_travel-cc996ede3c27617e32b6"></a>

**270° CCW: unverified** — `in_game_visible_travel-cc996ede3c27617e32b6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-14>1-W-out-10; entry: 1-S-in-14; exit: 1-W-out-10.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-S-in-16>1-N-out-20; entry: 1-S-in-16; exit: 1-N-out-20</summary>

<a id="case-in_game_visible_travel-993d0ba38b14cb3cbcf1"></a>

**0° CCW: unverified** — `in_game_visible_travel-993d0ba38b14cb3cbcf1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-16>1-N-out-20; entry: 1-S-in-16; exit: 1-N-out-20.

No observation recorded.

<a id="case-in_game_visible_travel-b47f23bbc30785f5ccce"></a>

**90° CCW: unverified** — `in_game_visible_travel-b47f23bbc30785f5ccce`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-16>1-N-out-20; entry: 1-S-in-16; exit: 1-N-out-20.

No observation recorded.

<a id="case-in_game_visible_travel-1c50012a8b078d8c54f1"></a>

**180° CCW: unverified** — `in_game_visible_travel-1c50012a8b078d8c54f1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-16>1-N-out-20; entry: 1-S-in-16; exit: 1-N-out-20.

No observation recorded.

<a id="case-in_game_visible_travel-c58fba00ef6094d883dc"></a>

**270° CCW: unverified** — `in_game_visible_travel-c58fba00ef6094d883dc`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-16>1-N-out-20; entry: 1-S-in-16; exit: 1-N-out-20.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-17>1-W-out-15; entry: 1-N-in-17; exit: 1-W-out-15</summary>

<a id="case-in_game_visible_travel-8f61501a127ecfa4cc66"></a>

**0° CCW: unverified** — `in_game_visible_travel-8f61501a127ecfa4cc66`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-17>1-W-out-15; entry: 1-N-in-17; exit: 1-W-out-15.

No observation recorded.

<a id="case-in_game_visible_travel-912a4b6462517796fe06"></a>

**90° CCW: unverified** — `in_game_visible_travel-912a4b6462517796fe06`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-17>1-W-out-15; entry: 1-N-in-17; exit: 1-W-out-15.

No observation recorded.

<a id="case-in_game_visible_travel-7d74f592e247ec16b770"></a>

**180° CCW: unverified** — `in_game_visible_travel-7d74f592e247ec16b770`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-17>1-W-out-15; entry: 1-N-in-17; exit: 1-W-out-15.

No observation recorded.

<a id="case-in_game_visible_travel-2f87e2ce025bcdb12690"></a>

**270° CCW: unverified** — `in_game_visible_travel-2f87e2ce025bcdb12690`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-17>1-W-out-15; entry: 1-N-in-17; exit: 1-W-out-15.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-17>1-W-out-3; entry: 1-N-in-17; exit: 1-W-out-3</summary>

<a id="case-in_game_visible_travel-d128aebf7134c1a61f8a"></a>

**0° CCW: unverified** — `in_game_visible_travel-d128aebf7134c1a61f8a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-17>1-W-out-3; entry: 1-N-in-17; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-b14079296b4b0efb6a0e"></a>

**90° CCW: unverified** — `in_game_visible_travel-b14079296b4b0efb6a0e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-17>1-W-out-3; entry: 1-N-in-17; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-df48d610b1ff017870c2"></a>

**180° CCW: unverified** — `in_game_visible_travel-df48d610b1ff017870c2`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-17>1-W-out-3; entry: 1-N-in-17; exit: 1-W-out-3.

No observation recorded.

<a id="case-in_game_visible_travel-fdda86d9a449ec5781ff"></a>

**270° CCW: unverified** — `in_game_visible_travel-fdda86d9a449ec5781ff`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-17>1-W-out-3; entry: 1-N-in-17; exit: 1-W-out-3.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-19>1-W-out-1; entry: 1-N-in-19; exit: 1-W-out-1</summary>

<a id="case-in_game_visible_travel-90deaa158fa729894ee8"></a>

**0° CCW: unverified** — `in_game_visible_travel-90deaa158fa729894ee8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-19>1-W-out-1; entry: 1-N-in-19; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-b6047f99c3d8621a00c0"></a>

**90° CCW: unverified** — `in_game_visible_travel-b6047f99c3d8621a00c0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-19>1-W-out-1; entry: 1-N-in-19; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-190f62712e03d0096d3b"></a>

**180° CCW: unverified** — `in_game_visible_travel-190f62712e03d0096d3b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-19>1-W-out-1; entry: 1-N-in-19; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-a4c248b3a3b66598e979"></a>

**270° CCW: unverified** — `in_game_visible_travel-a4c248b3a3b66598e979`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-19>1-W-out-1; entry: 1-N-in-19; exit: 1-W-out-1.

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
<summary>Forbidden transfer — road → road — 352 cases; unverified: 352</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-66febcb432cac1b0159c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c1fe082203f24c64969d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ff40df8f9d393c9bea46">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-55c8e6576a230dd161da">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7c40e76bd8c2b4346058">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7c3a1ee772a0e28d22dc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8627911ca84806e594ec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d9be8ce99da2a2a28f26">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cb1d8096403374f1e242">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a998c4cf243381495f10">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bdd78ff6e72928d42545">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-43df4fd2703b9c6341e1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-198dc316adf9147dc23d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8bde6381381d61babfe0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8e848bbab2e966d33fce">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6002915f655d4a596a6e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4d7d1963b00195b4ecd7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d452aa9ea58c216af75b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cbfd73636bb4bbc8d944">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f5a9710d730d80c54dcd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d43e2f8e9f2b30e24418">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5c089990038e58e4c062">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b682a326bf754de49945">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c6e0d4442a7b3516dd37">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-03030d91a135ec960cdb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bf00c3a8401da423e698">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3327dab280cac79e16a0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-40a2c722dfcc528c0a9d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b25a6beded8762da7bd1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9daafcba9c6890df812d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-56fba22bd042ebe4245f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-238e368a9e4e7c1fad99">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cfd406c14ccc7ffe5e6b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-959c2a94d4c60ed3d4af">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2cd193b3a054223b128c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3144f030c47491892a9f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c24ff28a590450ae79b6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ef109a9b840995e2e0b8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2589ace3af7b2310910c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0e27871eb565ab3a111a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-75db42d202240f976d3f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-586e422d101a6471ceb9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1326ed487f3f3aacedbc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b2859c3ca58af73555ce">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c023ade9ddb73040ad5a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7a5cd4af67e8df03d621">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5bab4c9ffd14183aa180">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7c4f5153111cc5ef08c1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d7afccb42ffd3737365c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5fc86d1312e284bd0899">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-21202b842d79087642c9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-faa80473664408c81821">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f7820ea78f9a413160ab">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6cfa91fe73c9fa04b07c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-80a1c4adc67b7b1a3f2c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4ff6a502a8f2201ada5d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-038ac45d6c38b5c75bd9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-93be55b24d4b6781efc4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c20b986a0c52ee202095">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-426238762bb1604457b2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-18bcc3ddb4f43bbc492d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7e9a33f9cf7eda404974">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3c62d9c27238adbfa457">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-53ed9d5ce23742d2c14f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9a2a30813cbe5f01849b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-32c9bdf58e942e86ec39">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e8c8266323cdb24e08b8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-52084fde5d3fd98c4d7c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ab707a58a23111cb6d24">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e9a79435932a75a5b8e9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9cc21ae0d47ae28884d5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8fb3455537336742464d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-93422a00895ba981be05">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5ef40905b56c057a0a5c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fb5fd61a5cd8ecd2a2c6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-77163687061fcb1e182a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-05de384baedba0fdabd1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a7f26d28a2a09b7b385e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ec2680ca61b895db16b0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ef425e91d786fe9cb640">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e8619c9b4d4208509fb0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3433934cc4897c27c1e5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e668715acf380621e9b7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2fe5a59ce3d1adc7cc64">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9a340fa9aadab45ee9b5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9464b7a17bca697a333a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9226605fbb98ae6dff87">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1f415986564eb3fa17c0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-45f069120d53d41b817f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bddc0dddd8d4392332a7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ce548e85c424079c5f27">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fc8149b143c06ec26bf0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bb18a9801562490ade39">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-74414e78c01d589e08b6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9c951838f46612fe4e91">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-94079e4a567c23d426c2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-942f27966016777a316b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a42b1a7d28fd07f7701e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fbde3a4509012968a1ba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-de1533af5fe66f424184">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-dbe3da1852990a5a5623">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c5a0dc05afc7c04501de">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0ef6daa60c828f0a5f93">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9cf85ca944e36900dee7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-7; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c34d9de362ebd902abcf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c2b939c3cbf39bc17854">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3fae02847a3a483a920e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8a76487afb7aaa76b5a8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-7; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8bd49aa53c16ade8325d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-48839b3b6f74e6ceeca6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b60496e7b6678d4c3455">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c87824f557f668faecef">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-7; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-950f2e1665a51caa1bc4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d6f929eef7b60a995a96">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b1a9d97c9d70a6a6f940">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-06ab599d647000f68466">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-7; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c7624f68b679f3d4cb55">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b5207903184aaf55eab7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-919316623654b8042001">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e6d5ebf8aaeb106656fb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-7; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9ae34d8c3cfbb268f938">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a00f7a8630d1e6094f38">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2836371f469542a297f6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a947d1e4b3fd07b66ed1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-7; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-549b58b475c7fc9e023d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-39eb39849a4227e0722d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-74a705e734b49e30a62d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-99c0e087ff8c07578a76">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-7; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4be84acdb23c7b536a6f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-616f38e424f099c4ce50">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c35dafd32009b01a620f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-59fc5a8023cfff886d03">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-7; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1f795fb78b1987b3f3af">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-af4c9b57ccd8d6ef9dbb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a47d861291113cbd14fa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9268d2571b4183609534">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-7; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b82dcf2427dff7644dae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6e20e4cee499ebf2276a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3a5385bf90e4c052fe88">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-952b1404dfca69914723">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-8; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-02ac829809f960238cf0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f54b2e16d1eed6dc57a7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2123cfc1f3f7cdc91393">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6499e7123a31c7895868">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-8; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-01b579da253305b19e0c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7c92aa5657cf26bee3cb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3c6b81094cfccac7a82e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fa38ab7d223d1ba8129c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-8; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a7ae964cb5f097b0812d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-93e15c9aa6b6b9721b0f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bc3a1044a616d24a8e42">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-65729ce5ded5d1b14464">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-8; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-402a6d486911424ecff0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3c4ea2c465576ccfcc49">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d57c2a25761647f2a03e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a090032ab3aa20d8f486">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-8; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f74c346d81fc74312bcc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fb05854d7618cf905359">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-da64ef98f61a1e6451c2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3f377e8fd752784a25ed">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-8; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2a1c693bb5910b7b6db5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5999a471d61b1ab668ca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0f8efc4c778c0f5c8c0a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dfdc1cd5736702567037">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-8; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-47ad65daca01e52896fe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-be89085ae05715ac7f50">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f1308c46f2ecf1892d5e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ee30da99d742d0b67f71">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-8; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2cf7fe728534755cbe3c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8928e4ab937b206e74fb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-35377e8ae569b3409135">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bc65830edbd28e5f93be">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-8; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a5044c756ea880774b1b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1882fe2a39d381970164">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-30343b8c570ff7e01b30">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ae9479deeace5668e89e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-13; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3930800e560ea2ae9448">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d81bdec793ada19e6cc7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c16913f3a64e604a74be">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7551290cadc64e5d316e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-13; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c64401220c98e0675679">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-92aa14f93daf726174c3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-42a74b7ebf441ea8809d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-89f45598833b62db877a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-13; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b34baedf92cc8a1e1850">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0a014aa4182dc43b29c4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-044047c87abe123ac3f0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1ac84bdbd8fa607a3852">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-13; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9b7ef4766b05198e585d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6a80f1e987af6314ad4d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eb3f50a64dc1ddfeb203">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-22749ec6e025f28846a1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-13; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-691d60f8926d3ba78321">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-60395f418b461ab914fc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9108866bc8a46e3860c8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ee4ff83f5c82f76b80ab">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-13; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cd73f23d230c6d7b6d2e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-564febf9ab32d278c3ab">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5f7f13dfe52b9f298926">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fbee0454b988724c5325">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-13; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e3670945219eb58c2744">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-315d12ad097bf5a63b7d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4e813ca3ee0792c2572c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b148cbc1967ee8167bc2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-13; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-934fafda1656f4b4a6d3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2cae219cd37c56baf8b1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-faf4a21169ddd0639f18">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-abab0683964e0a3acf5d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-13; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-64bc1d8f68a09422f3bb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1094e92842c38895b03e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cabfae3d1de4533161f0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-95bffc830f16c35ef67f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-14; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-53d0a09cbcc2d67064c9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cd927f8228af6fb32513">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-512c76a9be027d3238db">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-36b04e6b2dc8ef5be543">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-14; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-19788729d67c181c3eee">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8b2201848adf7e690300">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1d9a4bd44648c5cd3051">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ebf59c61fbe17c36fc6a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-14; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-66f84b66dab33700563f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5bd6d45f998917ae0bae">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-15dec7a8cc378d3194de">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-52a1a8cb1816b2daae06">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-14; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1f7e2a301c6c6e9a6ece">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-933a7a0ee2371e9d8ece">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8bb30554ec73b4b24253">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3ba33973288554a588c2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-14; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-253fb897fc7cd583b4a2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bf6e8d1565971ee19fa2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9f29a2590e6ee223e60c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f97477210633df046a39">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-14; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a162d9c91d48270a99f8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6c6c2d1d6fe0c39b1ca9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-175b094a9b93bf9cf837">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d48f55209cc649349cd0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-14; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c6dd03181040b99825ec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2402a5fa4129827a3f76">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ffa15a25a22c85f9a402">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0f1dc4641a11f1346c1d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-14; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1506e9dde5b3835e3cd8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-96a303261d4c5c77f02c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-20c42c1bbd55c2aeba29">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-63699d7d319a08757393">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-14; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fd55e64b4596f0e11b9e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-78319e04d4aa654cdbbd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-18aad648b769fb5b8312">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-af7738c54931085f66f1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-16; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-912375e61e38abf38ed2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c0a4b5b61fac7618aeff">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5ba61b2e82ae8167c6a4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5b8c50c44a212a972f8b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-16; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ed68e7d3991671bd0b16">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6abd7c0aab4c05b3d229">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f4ed43154a57649434a0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-63c6b130a9422981a30c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-16; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1ad75c690890a8b7ea45">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fe303f806fca8e3824fd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-35e8547955e23e2139bc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eaaf33c1c8f441c1b93a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-16; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-35dbba093bfcc28b4bb9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7608aba76fd3ef1dbbde">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fca35992b6ba89e52f7e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d44b28889eff6ba42228">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-16; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a6dcd80efc365281efee">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fa3f90a7bd181ad453b9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-73aa8239b68e216f3824">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-754100468dbc982e2e96">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-16; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5d1fef44b44298ed9290">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-410bcf619eaf13ad99e3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2d3ccdb820146cb027e4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-95d0c5744d33240bcfd5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-16; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7977bb570c4fdcd68291">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cf3ab505517df340f815">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cb3d13c9869c3acb7d07">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0453e2aa39a0864801a6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-16; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-51f420cc231dc1ed093d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-03227f1be23d14c1e628">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3c132bbc7038a4e74e61">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d11b7c853c0abeb736a1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-16; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-43dcbae61b76f0113fe1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-77ce2c3c1e11fb149183">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1019a913317efbf82020">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ebf840a4d12e2fc37a77">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-17; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8eebd93b1df445815963">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a59a8679a4cc6477137d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-91ad64d4f120dc4e949e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c10f8ed6c24649a0cd28">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-17; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1ae752f1829d7b2c3cfd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6229e332a1edb8c61a0b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-40682d2c02acc90d449b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fcf1f67af4891f98dec2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-17; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a36f03493d9f145dde59">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-23481940510eec36ef7f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e857f1a5b9110965b33f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3aecd3265598a6bb038d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-17; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-337dc10fc669a8cc9c17">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fb18b5260ea0eb253d75">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eb4fd81d984ca2344827">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1f893d4acf0916dc677a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-17; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-29bbd7ea897f4c3b4e1c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d9af61c5581cb4cf5060">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ebe801ecc5db9a1381d8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bad15ad0c803e433b79b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-17; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-620b0d335de85887d6df">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d46606b8cacc420cc1a9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-de6e26d48b5ea4700363">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-038eda5b80b731436663">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-17; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d6d8f130bf846a6bbbe8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aed4a1c392b6f658d016">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-88be1a9041f061cb606d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2f4fcd0c2d8739da44fd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-17; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ddfb84b0c35023ddceba">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1009f57116843a24783a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9f285d02ea014d304918">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a1bfc7ec8477bec81d7e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-19; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b355d1a40002ffce4c85">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e22566055bea1bce9013">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ca6dc418a8e931b74415">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-467531b846f555020b12">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-19; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-10250c9895b993ed9c7f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-341aacaf802e93ca7980">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-66fe8bd96c4e122b1d10">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-958b01ada2e9b0fe085c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-19; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-859b8f8153ec950a5137">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-90eccc3b43238310da61">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8de14e400b91eaac6c7d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3c73c2ca272ed8a30558">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-19; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b626c6b0ecbacee7cf25">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3e8f9fdca09b2f239859">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-71b774cd232d26d7ad52">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2350d0e1cae24b2420f9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-19; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d31a54bab84f0c30a31a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ad7e04c7b423da152314">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cd43e40d176ad4f53d1e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0b5b21c898cc03045e4f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-19; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0029b8d1b59b2a47e23f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-39acc72b0c91a9842d48">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-850870ce96bd7ee14c92">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0404f19ec18bc8d62e29">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-19; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ee513a2f7f6b3c359fd8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9362f8b576d5359f49ab">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0fcd2b36b06dd9d4b389">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5b85f54c994880ca4b39">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-19; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fa94466884e56559c5c2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9676b75c2085671e7920">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b0f1aef8c6fb84218fb3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5ec16524817bc3c86439">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-19; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d36b5be1429fedb7aa14">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f0b602c81224341f6122">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-764a39587477cd6dd799">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3b8aea3429edcde9f05d">[ ] unverified</a> |


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
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cb1d8096403374f1e242"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cb1d8096403374f1e242`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a998c4cf243381495f10"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a998c4cf243381495f10`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bdd78ff6e72928d42545"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bdd78ff6e72928d42545`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-43df4fd2703b9c6341e1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-43df4fd2703b9c6341e1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-198dc316adf9147dc23d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-198dc316adf9147dc23d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8bde6381381d61babfe0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8bde6381381d61babfe0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8e848bbab2e966d33fce"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8e848bbab2e966d33fce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6002915f655d4a596a6e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6002915f655d4a596a6e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4d7d1963b00195b4ecd7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4d7d1963b00195b4ecd7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d452aa9ea58c216af75b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d452aa9ea58c216af75b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cbfd73636bb4bbc8d944"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cbfd73636bb4bbc8d944`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f5a9710d730d80c54dcd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f5a9710d730d80c54dcd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d43e2f8e9f2b30e24418"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d43e2f8e9f2b30e24418`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5c089990038e58e4c062"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5c089990038e58e4c062`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b682a326bf754de49945"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b682a326bf754de49945`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c6e0d4442a7b3516dd37"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c6e0d4442a7b3516dd37`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-03030d91a135ec960cdb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-03030d91a135ec960cdb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bf00c3a8401da423e698"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bf00c3a8401da423e698`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3327dab280cac79e16a0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3327dab280cac79e16a0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-40a2c722dfcc528c0a9d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-40a2c722dfcc528c0a9d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-2; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b25a6beded8762da7bd1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b25a6beded8762da7bd1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9daafcba9c6890df812d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9daafcba9c6890df812d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-56fba22bd042ebe4245f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-56fba22bd042ebe4245f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-238e368a9e4e7c1fad99"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-238e368a9e4e7c1fad99`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-2; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

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
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c023ade9ddb73040ad5a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c023ade9ddb73040ad5a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7a5cd4af67e8df03d621"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7a5cd4af67e8df03d621`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5bab4c9ffd14183aa180"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5bab4c9ffd14183aa180`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7c4f5153111cc5ef08c1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7c4f5153111cc5ef08c1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d7afccb42ffd3737365c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d7afccb42ffd3737365c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5fc86d1312e284bd0899"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5fc86d1312e284bd0899`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-21202b842d79087642c9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-21202b842d79087642c9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-faa80473664408c81821"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-faa80473664408c81821`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f7820ea78f9a413160ab"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f7820ea78f9a413160ab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6cfa91fe73c9fa04b07c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6cfa91fe73c9fa04b07c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-80a1c4adc67b7b1a3f2c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-80a1c4adc67b7b1a3f2c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4ff6a502a8f2201ada5d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4ff6a502a8f2201ada5d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-038ac45d6c38b5c75bd9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-038ac45d6c38b5c75bd9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-93be55b24d4b6781efc4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-93be55b24d4b6781efc4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c20b986a0c52ee202095"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c20b986a0c52ee202095`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-426238762bb1604457b2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-426238762bb1604457b2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-18bcc3ddb4f43bbc492d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-18bcc3ddb4f43bbc492d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7e9a33f9cf7eda404974"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7e9a33f9cf7eda404974`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3c62d9c27238adbfa457"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3c62d9c27238adbfa457`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-53ed9d5ce23742d2c14f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-53ed9d5ce23742d2c14f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-4; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9a2a30813cbe5f01849b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9a2a30813cbe5f01849b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-32c9bdf58e942e86ec39"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-32c9bdf58e942e86ec39`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e8c8266323cdb24e08b8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e8c8266323cdb24e08b8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-52084fde5d3fd98c4d7c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-52084fde5d3fd98c4d7c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-4; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

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
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-05de384baedba0fdabd1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-05de384baedba0fdabd1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a7f26d28a2a09b7b385e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a7f26d28a2a09b7b385e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ec2680ca61b895db16b0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ec2680ca61b895db16b0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ef425e91d786fe9cb640"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ef425e91d786fe9cb640`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e8619c9b4d4208509fb0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e8619c9b4d4208509fb0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3433934cc4897c27c1e5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3433934cc4897c27c1e5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e668715acf380621e9b7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e668715acf380621e9b7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2fe5a59ce3d1adc7cc64"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2fe5a59ce3d1adc7cc64`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9a340fa9aadab45ee9b5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9a340fa9aadab45ee9b5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9464b7a17bca697a333a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9464b7a17bca697a333a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9226605fbb98ae6dff87"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9226605fbb98ae6dff87`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1f415986564eb3fa17c0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1f415986564eb3fa17c0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-45f069120d53d41b817f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-45f069120d53d41b817f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bddc0dddd8d4392332a7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bddc0dddd8d4392332a7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ce548e85c424079c5f27"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ce548e85c424079c5f27`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fc8149b143c06ec26bf0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fc8149b143c06ec26bf0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bb18a9801562490ade39"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bb18a9801562490ade39`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-74414e78c01d589e08b6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-74414e78c01d589e08b6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9c951838f46612fe4e91"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9c951838f46612fe4e91`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-94079e4a567c23d426c2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-94079e4a567c23d426c2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-942f27966016777a316b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-942f27966016777a316b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a42b1a7d28fd07f7701e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a42b1a7d28fd07f7701e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fbde3a4509012968a1ba"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fbde3a4509012968a1ba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-de1533af5fe66f424184"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-de1533af5fe66f424184`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-dbe3da1852990a5a5623"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-dbe3da1852990a5a5623`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c5a0dc05afc7c04501de"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c5a0dc05afc7c04501de`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0ef6daa60c828f0a5f93"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0ef6daa60c828f0a5f93`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9cf85ca944e36900dee7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9cf85ca944e36900dee7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-7; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c34d9de362ebd902abcf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c34d9de362ebd902abcf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c2b939c3cbf39bc17854"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c2b939c3cbf39bc17854`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3fae02847a3a483a920e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3fae02847a3a483a920e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8a76487afb7aaa76b5a8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8a76487afb7aaa76b5a8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-7; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8bd49aa53c16ade8325d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8bd49aa53c16ade8325d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-48839b3b6f74e6ceeca6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-48839b3b6f74e6ceeca6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b60496e7b6678d4c3455"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b60496e7b6678d4c3455`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c87824f557f668faecef"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c87824f557f668faecef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-7; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-950f2e1665a51caa1bc4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-950f2e1665a51caa1bc4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d6f929eef7b60a995a96"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d6f929eef7b60a995a96`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b1a9d97c9d70a6a6f940"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b1a9d97c9d70a6a6f940`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-06ab599d647000f68466"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-06ab599d647000f68466`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-7; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c7624f68b679f3d4cb55"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c7624f68b679f3d4cb55`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b5207903184aaf55eab7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b5207903184aaf55eab7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-919316623654b8042001"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-919316623654b8042001`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e6d5ebf8aaeb106656fb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e6d5ebf8aaeb106656fb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-7; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9ae34d8c3cfbb268f938"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9ae34d8c3cfbb268f938`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a00f7a8630d1e6094f38"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a00f7a8630d1e6094f38`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2836371f469542a297f6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2836371f469542a297f6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a947d1e4b3fd07b66ed1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a947d1e4b3fd07b66ed1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-7; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-549b58b475c7fc9e023d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-549b58b475c7fc9e023d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-39eb39849a4227e0722d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-39eb39849a4227e0722d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-74a705e734b49e30a62d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-74a705e734b49e30a62d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-99c0e087ff8c07578a76"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-99c0e087ff8c07578a76`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-7; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4be84acdb23c7b536a6f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4be84acdb23c7b536a6f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-616f38e424f099c4ce50"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-616f38e424f099c4ce50`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c35dafd32009b01a620f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c35dafd32009b01a620f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-59fc5a8023cfff886d03"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-59fc5a8023cfff886d03`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-7; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1f795fb78b1987b3f3af"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1f795fb78b1987b3f3af`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-af4c9b57ccd8d6ef9dbb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-af4c9b57ccd8d6ef9dbb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a47d861291113cbd14fa"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a47d861291113cbd14fa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9268d2571b4183609534"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9268d2571b4183609534`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-7; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b82dcf2427dff7644dae"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b82dcf2427dff7644dae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6e20e4cee499ebf2276a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6e20e4cee499ebf2276a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3a5385bf90e4c052fe88"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3a5385bf90e4c052fe88`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-952b1404dfca69914723"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-952b1404dfca69914723`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

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
<summary>Forbidden transfer — from port: 1-N-in-8; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-402a6d486911424ecff0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-402a6d486911424ecff0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3c4ea2c465576ccfcc49"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3c4ea2c465576ccfcc49`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d57c2a25761647f2a03e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d57c2a25761647f2a03e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a090032ab3aa20d8f486"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a090032ab3aa20d8f486`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-8; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f74c346d81fc74312bcc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f74c346d81fc74312bcc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fb05854d7618cf905359"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fb05854d7618cf905359`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-da64ef98f61a1e6451c2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-da64ef98f61a1e6451c2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3f377e8fd752784a25ed"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3f377e8fd752784a25ed`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-8; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2a1c693bb5910b7b6db5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2a1c693bb5910b7b6db5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5999a471d61b1ab668ca"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5999a471d61b1ab668ca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0f8efc4c778c0f5c8c0a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0f8efc4c778c0f5c8c0a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dfdc1cd5736702567037"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dfdc1cd5736702567037`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-8; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-47ad65daca01e52896fe"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-47ad65daca01e52896fe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-be89085ae05715ac7f50"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-be89085ae05715ac7f50`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f1308c46f2ecf1892d5e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f1308c46f2ecf1892d5e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ee30da99d742d0b67f71"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ee30da99d742d0b67f71`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-8; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2cf7fe728534755cbe3c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2cf7fe728534755cbe3c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8928e4ab937b206e74fb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8928e4ab937b206e74fb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-35377e8ae569b3409135"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-35377e8ae569b3409135`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bc65830edbd28e5f93be"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bc65830edbd28e5f93be`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-8; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a5044c756ea880774b1b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a5044c756ea880774b1b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1882fe2a39d381970164"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1882fe2a39d381970164`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-30343b8c570ff7e01b30"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-30343b8c570ff7e01b30`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ae9479deeace5668e89e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ae9479deeace5668e89e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-8; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-13; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3930800e560ea2ae9448"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3930800e560ea2ae9448`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d81bdec793ada19e6cc7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d81bdec793ada19e6cc7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c16913f3a64e604a74be"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c16913f3a64e604a74be`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7551290cadc64e5d316e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7551290cadc64e5d316e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-13; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c64401220c98e0675679"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c64401220c98e0675679`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-92aa14f93daf726174c3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-92aa14f93daf726174c3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-42a74b7ebf441ea8809d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-42a74b7ebf441ea8809d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-89f45598833b62db877a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-89f45598833b62db877a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-13; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b34baedf92cc8a1e1850"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b34baedf92cc8a1e1850`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0a014aa4182dc43b29c4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0a014aa4182dc43b29c4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-044047c87abe123ac3f0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-044047c87abe123ac3f0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1ac84bdbd8fa607a3852"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1ac84bdbd8fa607a3852`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-13; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9b7ef4766b05198e585d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9b7ef4766b05198e585d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6a80f1e987af6314ad4d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6a80f1e987af6314ad4d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eb3f50a64dc1ddfeb203"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-eb3f50a64dc1ddfeb203`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-22749ec6e025f28846a1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-22749ec6e025f28846a1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-13; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-691d60f8926d3ba78321"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-691d60f8926d3ba78321`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-60395f418b461ab914fc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-60395f418b461ab914fc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9108866bc8a46e3860c8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9108866bc8a46e3860c8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ee4ff83f5c82f76b80ab"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ee4ff83f5c82f76b80ab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-13; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cd73f23d230c6d7b6d2e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cd73f23d230c6d7b6d2e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-564febf9ab32d278c3ab"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-564febf9ab32d278c3ab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5f7f13dfe52b9f298926"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5f7f13dfe52b9f298926`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fbee0454b988724c5325"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fbee0454b988724c5325`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-13; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e3670945219eb58c2744"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e3670945219eb58c2744`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-315d12ad097bf5a63b7d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-315d12ad097bf5a63b7d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4e813ca3ee0792c2572c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4e813ca3ee0792c2572c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b148cbc1967ee8167bc2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b148cbc1967ee8167bc2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-13; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-934fafda1656f4b4a6d3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-934fafda1656f4b4a6d3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2cae219cd37c56baf8b1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2cae219cd37c56baf8b1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-faf4a21169ddd0639f18"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-faf4a21169ddd0639f18`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-abab0683964e0a3acf5d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-abab0683964e0a3acf5d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-13; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-64bc1d8f68a09422f3bb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-64bc1d8f68a09422f3bb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1094e92842c38895b03e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1094e92842c38895b03e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cabfae3d1de4533161f0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cabfae3d1de4533161f0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-95bffc830f16c35ef67f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-95bffc830f16c35ef67f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-14; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-53d0a09cbcc2d67064c9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-53d0a09cbcc2d67064c9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cd927f8228af6fb32513"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cd927f8228af6fb32513`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-512c76a9be027d3238db"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-512c76a9be027d3238db`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-36b04e6b2dc8ef5be543"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-36b04e6b2dc8ef5be543`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-14; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-19788729d67c181c3eee"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-19788729d67c181c3eee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8b2201848adf7e690300"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8b2201848adf7e690300`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1d9a4bd44648c5cd3051"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1d9a4bd44648c5cd3051`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ebf59c61fbe17c36fc6a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ebf59c61fbe17c36fc6a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-14; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-66f84b66dab33700563f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-66f84b66dab33700563f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5bd6d45f998917ae0bae"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5bd6d45f998917ae0bae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-15dec7a8cc378d3194de"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-15dec7a8cc378d3194de`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-52a1a8cb1816b2daae06"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-52a1a8cb1816b2daae06`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-14; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1f7e2a301c6c6e9a6ece"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1f7e2a301c6c6e9a6ece`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-933a7a0ee2371e9d8ece"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-933a7a0ee2371e9d8ece`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8bb30554ec73b4b24253"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8bb30554ec73b4b24253`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3ba33973288554a588c2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3ba33973288554a588c2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-14; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-253fb897fc7cd583b4a2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-253fb897fc7cd583b4a2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bf6e8d1565971ee19fa2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bf6e8d1565971ee19fa2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9f29a2590e6ee223e60c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9f29a2590e6ee223e60c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f97477210633df046a39"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f97477210633df046a39`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-14; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a162d9c91d48270a99f8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a162d9c91d48270a99f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6c6c2d1d6fe0c39b1ca9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6c6c2d1d6fe0c39b1ca9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-175b094a9b93bf9cf837"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-175b094a9b93bf9cf837`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d48f55209cc649349cd0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d48f55209cc649349cd0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-14; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c6dd03181040b99825ec"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c6dd03181040b99825ec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2402a5fa4129827a3f76"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2402a5fa4129827a3f76`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ffa15a25a22c85f9a402"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ffa15a25a22c85f9a402`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0f1dc4641a11f1346c1d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0f1dc4641a11f1346c1d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-14; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1506e9dde5b3835e3cd8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1506e9dde5b3835e3cd8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-96a303261d4c5c77f02c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-96a303261d4c5c77f02c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-20c42c1bbd55c2aeba29"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-20c42c1bbd55c2aeba29`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-63699d7d319a08757393"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-63699d7d319a08757393`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-14; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fd55e64b4596f0e11b9e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fd55e64b4596f0e11b9e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-78319e04d4aa654cdbbd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-78319e04d4aa654cdbbd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-18aad648b769fb5b8312"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-18aad648b769fb5b8312`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-af7738c54931085f66f1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-af7738c54931085f66f1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

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
<summary>Forbidden transfer — from port: 1-S-in-16; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-35dbba093bfcc28b4bb9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-35dbba093bfcc28b4bb9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7608aba76fd3ef1dbbde"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7608aba76fd3ef1dbbde`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fca35992b6ba89e52f7e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fca35992b6ba89e52f7e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d44b28889eff6ba42228"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d44b28889eff6ba42228`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-16; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a6dcd80efc365281efee"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a6dcd80efc365281efee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fa3f90a7bd181ad453b9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fa3f90a7bd181ad453b9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-73aa8239b68e216f3824"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-73aa8239b68e216f3824`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-754100468dbc982e2e96"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-754100468dbc982e2e96`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-16; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5d1fef44b44298ed9290"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5d1fef44b44298ed9290`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-410bcf619eaf13ad99e3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-410bcf619eaf13ad99e3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2d3ccdb820146cb027e4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2d3ccdb820146cb027e4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-95d0c5744d33240bcfd5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-95d0c5744d33240bcfd5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-16; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7977bb570c4fdcd68291"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7977bb570c4fdcd68291`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cf3ab505517df340f815"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cf3ab505517df340f815`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cb3d13c9869c3acb7d07"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cb3d13c9869c3acb7d07`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0453e2aa39a0864801a6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0453e2aa39a0864801a6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-16; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-51f420cc231dc1ed093d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-51f420cc231dc1ed093d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-03227f1be23d14c1e628"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-03227f1be23d14c1e628`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3c132bbc7038a4e74e61"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3c132bbc7038a4e74e61`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d11b7c853c0abeb736a1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d11b7c853c0abeb736a1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-16; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-43dcbae61b76f0113fe1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-43dcbae61b76f0113fe1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-77ce2c3c1e11fb149183"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-77ce2c3c1e11fb149183`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1019a913317efbf82020"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1019a913317efbf82020`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ebf840a4d12e2fc37a77"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ebf840a4d12e2fc37a77`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-16; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-17; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8eebd93b1df445815963"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8eebd93b1df445815963`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-17; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a59a8679a4cc6477137d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a59a8679a4cc6477137d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-17; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-91ad64d4f120dc4e949e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-91ad64d4f120dc4e949e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-17; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c10f8ed6c24649a0cd28"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c10f8ed6c24649a0cd28`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-17; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-17; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1ae752f1829d7b2c3cfd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1ae752f1829d7b2c3cfd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-17; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6229e332a1edb8c61a0b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6229e332a1edb8c61a0b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-17; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-40682d2c02acc90d449b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-40682d2c02acc90d449b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-17; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fcf1f67af4891f98dec2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fcf1f67af4891f98dec2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-17; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-17; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a36f03493d9f145dde59"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a36f03493d9f145dde59`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-17; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-23481940510eec36ef7f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-23481940510eec36ef7f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-17; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e857f1a5b9110965b33f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e857f1a5b9110965b33f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-17; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3aecd3265598a6bb038d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3aecd3265598a6bb038d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-17; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-17; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-337dc10fc669a8cc9c17"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-337dc10fc669a8cc9c17`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-17; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fb18b5260ea0eb253d75"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fb18b5260ea0eb253d75`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-17; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eb4fd81d984ca2344827"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-eb4fd81d984ca2344827`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-17; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1f893d4acf0916dc677a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1f893d4acf0916dc677a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-17; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-17; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-29bbd7ea897f4c3b4e1c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-29bbd7ea897f4c3b4e1c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-17; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d9af61c5581cb4cf5060"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d9af61c5581cb4cf5060`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-17; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ebe801ecc5db9a1381d8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ebe801ecc5db9a1381d8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-17; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bad15ad0c803e433b79b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bad15ad0c803e433b79b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-17; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-17; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-620b0d335de85887d6df"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-620b0d335de85887d6df`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-17; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d46606b8cacc420cc1a9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d46606b8cacc420cc1a9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-17; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-de6e26d48b5ea4700363"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-de6e26d48b5ea4700363`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-17; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-038eda5b80b731436663"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-038eda5b80b731436663`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-17; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-17; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d6d8f130bf846a6bbbe8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d6d8f130bf846a6bbbe8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-17; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aed4a1c392b6f658d016"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-aed4a1c392b6f658d016`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-17; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-88be1a9041f061cb606d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-88be1a9041f061cb606d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-17; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2f4fcd0c2d8739da44fd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2f4fcd0c2d8739da44fd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-17; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-17; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ddfb84b0c35023ddceba"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ddfb84b0c35023ddceba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-17; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1009f57116843a24783a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1009f57116843a24783a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-17; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9f285d02ea014d304918"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9f285d02ea014d304918`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-17; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a1bfc7ec8477bec81d7e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a1bfc7ec8477bec81d7e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-17; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-19; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b355d1a40002ffce4c85"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b355d1a40002ffce4c85`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e22566055bea1bce9013"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e22566055bea1bce9013`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ca6dc418a8e931b74415"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ca6dc418a8e931b74415`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-467531b846f555020b12"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-467531b846f555020b12`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-W-out-3; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-19; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-10250c9895b993ed9c7f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-10250c9895b993ed9c7f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-341aacaf802e93ca7980"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-341aacaf802e93ca7980`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-66fe8bd96c4e122b1d10"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-66fe8bd96c4e122b1d10`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-958b01ada2e9b0fe085c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-958b01ada2e9b0fe085c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-E-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-19; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-859b8f8153ec950a5137"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-859b8f8153ec950a5137`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-90eccc3b43238310da61"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-90eccc3b43238310da61`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8de14e400b91eaac6c7d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8de14e400b91eaac6c7d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3c73c2ca272ed8a30558"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3c73c2ca272ed8a30558`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-W-out-9; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-19; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b626c6b0ecbacee7cf25"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b626c6b0ecbacee7cf25`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3e8f9fdca09b2f239859"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3e8f9fdca09b2f239859`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-71b774cd232d26d7ad52"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-71b774cd232d26d7ad52`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2350d0e1cae24b2420f9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2350d0e1cae24b2420f9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-19; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d31a54bab84f0c30a31a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d31a54bab84f0c30a31a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ad7e04c7b423da152314"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ad7e04c7b423da152314`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cd43e40d176ad4f53d1e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cd43e40d176ad4f53d1e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0b5b21c898cc03045e4f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0b5b21c898cc03045e4f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-E-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-19; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0029b8d1b59b2a47e23f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0029b8d1b59b2a47e23f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-39acc72b0c91a9842d48"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-39acc72b0c91a9842d48`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-850870ce96bd7ee14c92"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-850870ce96bd7ee14c92`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0404f19ec18bc8d62e29"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0404f19ec18bc8d62e29`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-E-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-19; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ee513a2f7f6b3c359fd8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ee513a2f7f6b3c359fd8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9362f8b576d5359f49ab"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9362f8b576d5359f49ab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0fcd2b36b06dd9d4b389"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0fcd2b36b06dd9d4b389`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5b85f54c994880ca4b39"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5b85f54c994880ca4b39`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-W-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-19; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fa94466884e56559c5c2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fa94466884e56559c5c2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9676b75c2085671e7920"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9676b75c2085671e7920`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b0f1aef8c6fb84218fb3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b0f1aef8c6fb84218fb3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5ec16524817bc3c86439"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5ec16524817bc3c86439`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-N-out-18; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-19; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d36b5be1429fedb7aa14"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d36b5be1429fedb7aa14`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f0b602c81224341f6122"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f0b602c81224341f6122`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-764a39587477cd6dd799"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-764a39587477cd6dd799`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3b8aea3429edcde9f05d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3b8aea3429edcde9f05d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → pedestrian — 80 cases; unverified: 80</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ec80ad41a12a10f10477">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4b52fcfe60b2fea84562">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-580e4ea4df4a1c756c5c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f4d8f9556df8c254950a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-2; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d33a9ff99515e785533a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-303118bee26eb2d58198">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7ec54a14053993cfc638">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9eb0130ec79491b397e0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-10c4a0acbc7c51574909">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-66a9e795153955ff4d76">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-547030d47cbd16454bd6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-050b611466ee9ebd42eb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-4; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-135e7c32048431400296">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8dd758e62612b1cab327">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a640c4b2deee0843931c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c40309a818f862c7a2d4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0834b6565e74b47aefe1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dfd43819d5dfdba49a0f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c8c47026ec9e207165c4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4e721500cc8d3c5bdbe8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-630abeaf75f7b9a53be8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-177520cb8643ca8cfa4a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1740e26e325291f92a9c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6d80d333abbe8fdd91fa">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-7; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9666bc0bae1f36cb0e80">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4db369c037e9351240f8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-038516328358f31bf2c7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f8021d80e7e699ef7c74">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-7; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-32446335bf7839f28bda">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0d82bf78ee545f878842">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8688d8e7478d4f7cd35d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ad86143411982d28d507">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-8; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-58cbef086864c3548663">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c5cabec2244afc3a5cac">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7b5a06f2030b72162299">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-638f8859ac833ebfcd06">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-8; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bbc03c0ac8bc78dfe9eb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bbbf674e5b4429f9641a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-61afa6a46472437117f2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3dcb0b3fab6ccb4444d0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-13; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8fc31b5de321a5aa04ab">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bd27e84275724d985b74">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8afdb8468ab1755e0588">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cb40508f6ba9357d5249">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-13; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1cc555d9a8377f1c27a7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b68eca3e3409d0f46c48">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-54c5a327599116a4e37d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1ad64609f3ecd38dd066">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-14; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8de86385cc533f91762a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7151c24383e28b664f60">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a7feaccc75e4d2ea04b1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-90385a14491cdb992960">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-14; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-440aafef1624959b0ebf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0813934a051e944adcc6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0d082325591540f97716">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b0d319a7508d88544be9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-16; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e1624d872f8476b9b164">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-74980b1e2d92e7993edb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6534e38cab574bd407a3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-759dfbf3027aac38bfb1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-16; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7d3e1937f5db675134bb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9885ce0486461593772e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c585c7421014a7fbcb88">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-57dea1e3cc7b7e554913">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-17; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c7600c8691527eb57e08">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2c11654801aaa64bcb12">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-074b3488c0b66e8dce63">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-52fc4fa2ce8b80df0ef8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-17; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a8fd4549d8d7a077d995">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e802092b30930e30f5ce">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c05bb898d05985078034">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4592435844217982e25d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-19; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3cbf07738791637e195e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0a8502baceef08182502">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2b127a52734190e16ac2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d4d728a74a5ded73f7c8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-19; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5439a3d045ca09d8ef69">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1a8a5ef14528e28f4404">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-88de457689b26c9c0345">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-24131695b00d4e035cb0">[ ] unverified</a> |


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
<summary>Forbidden transfer — from port: 1-N-in-7; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9666bc0bae1f36cb0e80"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9666bc0bae1f36cb0e80`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4db369c037e9351240f8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4db369c037e9351240f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-038516328358f31bf2c7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-038516328358f31bf2c7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f8021d80e7e699ef7c74"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f8021d80e7e699ef7c74`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-7; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-32446335bf7839f28bda"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-32446335bf7839f28bda`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0d82bf78ee545f878842"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0d82bf78ee545f878842`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8688d8e7478d4f7cd35d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8688d8e7478d4f7cd35d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ad86143411982d28d507"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ad86143411982d28d507`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-7; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

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
<summary>Forbidden transfer — from port: 1-S-in-13; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8fc31b5de321a5aa04ab"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8fc31b5de321a5aa04ab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bd27e84275724d985b74"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bd27e84275724d985b74`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8afdb8468ab1755e0588"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8afdb8468ab1755e0588`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cb40508f6ba9357d5249"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cb40508f6ba9357d5249`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-13; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1cc555d9a8377f1c27a7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1cc555d9a8377f1c27a7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b68eca3e3409d0f46c48"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b68eca3e3409d0f46c48`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-54c5a327599116a4e37d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-54c5a327599116a4e37d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1ad64609f3ecd38dd066"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1ad64609f3ecd38dd066`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-13; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-14; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8de86385cc533f91762a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8de86385cc533f91762a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7151c24383e28b664f60"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7151c24383e28b664f60`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a7feaccc75e4d2ea04b1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a7feaccc75e4d2ea04b1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-90385a14491cdb992960"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-90385a14491cdb992960`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-14; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-440aafef1624959b0ebf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-440aafef1624959b0ebf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0813934a051e944adcc6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0813934a051e944adcc6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0d082325591540f97716"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0d082325591540f97716`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b0d319a7508d88544be9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b0d319a7508d88544be9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-14; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

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
<summary>Forbidden transfer — from port: 1-N-in-17; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c7600c8691527eb57e08"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c7600c8691527eb57e08`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-17; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2c11654801aaa64bcb12"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2c11654801aaa64bcb12`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-17; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-074b3488c0b66e8dce63"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-074b3488c0b66e8dce63`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-17; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-52fc4fa2ce8b80df0ef8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-52fc4fa2ce8b80df0ef8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-17; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-17; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a8fd4549d8d7a077d995"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a8fd4549d8d7a077d995`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-17; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e802092b30930e30f5ce"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e802092b30930e30f5ce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-17; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c05bb898d05985078034"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c05bb898d05985078034`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-17; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4592435844217982e25d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4592435844217982e25d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-17; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-19; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3cbf07738791637e195e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3cbf07738791637e195e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0a8502baceef08182502"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0a8502baceef08182502`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2b127a52734190e16ac2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2b127a52734190e16ac2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d4d728a74a5ded73f7c8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d4d728a74a5ded73f7c8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-19; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5439a3d045ca09d8ef69"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5439a3d045ca09d8ef69`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1a8a5ef14528e28f4404"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1a8a5ef14528e28f4404`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-88de457689b26c9c0345"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-88de457689b26c9c0345`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-24131695b00d4e035cb0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-24131695b00d4e035cb0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — pedestrian → road — 80 cases; unverified: 80</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-W-out-1; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-068afd5d04630eb0a817">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-760a6e551a67b6cf2898">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-884e1b24921b9426d69f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7ac4fbacdf0ddd9224de">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-W-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9e73a7e3bccf3ac5cdcd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ce7f0f9e5af6719c85ca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ac96b573558ec65fd3a9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5a355b9ebcb2e66cd613">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-E-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8edc1cc5e26482252bbb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-20dc195a172c27d1e8b6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-73b305935dac9d7d27c7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-acffd45413b07628b39e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-W-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6a7fa7146c5208c3ea03">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4d85f221aff47596459c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-75a662ff951488d52e0f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aca0896dd9085a9b99ef">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-W-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-040fd6cb410278cc1b53">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-03d67744c3e408da8ab6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-82e808354d738c96e64a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-40b0232781e708080ce5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-E-out-11; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d40b779e968ea04bc5fd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3c94d52172637fca1d5e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c2ac241e33312d44442e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2011e8780ef7c302f559">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-E-out-12; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0ff19418709d2493ad67">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5d7d4d757fcab5dca5b0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-716697e2cf24b1134d90">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-479acc8b7bf40d5f7456">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-W-out-15; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d3f4b7c1ce6206d5ab6e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9bf2395d2c9dfa4e3fbf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d33aa1d84f6731f23d3a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-24ef917b23aa82339720">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-N-out-18; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c0e8a0e5a2e69361d80c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-774d192e2d434145225c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-201e305e8e574d3ac381">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0dea8e7303e2270ddea2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-N-out-20; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0281c52aa8b78b591392">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b4a6684715a52ac45551">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7e36fa42b0c5c8a5e3f8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b0f5c97585dd96b23396">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-W-out-1; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-96add150c70ca306c29e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2307d64064d783ab0fe6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-62be5a61830b92aea96a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b692dd8b56e6ba551b64">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-W-out-3; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-652c9b75e15491beff5b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5d0d371416f419c60f22">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4efcb45237581973b77d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a24cbb0f84f97dcdbf7b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-E-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b8c0e1cf53c069ffa9c5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-054d56e34daa60125b1f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-17d3864a2b9e6b0d7e01">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7faf2aac49377a64e6cc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-W-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-86cbb6b44d0444dd8773">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ad0f1d19e94cf92dec0f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a917921c8387c0a471a1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ea90d006e0aa9b186385">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-W-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-da6f0ab98782dd08bd23">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d29cc6beb0653b6a1a01">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f22353c79c4239ebb18f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-73989a38dc42df535b9b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-E-out-11; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e3e51e71e3bddf30643d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-58c7fda71fc6bc726093">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ae07d8cdaefc83458bab">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-244f9958971a36de97df">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-E-out-12; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6496daebe51f6507b37e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ed8573891f2830f39928">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-01bef3d04f2571c57dc8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ac56d8b86efe39ed356d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-W-out-15; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-95791c5ce0194005c2b4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-379e82e7a3bbcd05e0fa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c6298035cb87d24b6685">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-edc04d23b4eaff6c4168">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-N-out-18; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e3c7d837decdd00dd8df">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-509b222004471bf9c415">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d7b133a0bc78bede583b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-42e3a80cf0844c2d3734">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-N-out-20; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0e8600956565bd9c10bf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a699888447385eefd077">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-79df18d3683a3d901412">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2becf66b0691fee463b3">[ ] unverified</a> |


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
<summary>Forbidden transfer — from port: 2-N-in-1; to port: 1-W-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6a7fa7146c5208c3ea03"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6a7fa7146c5208c3ea03`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4d85f221aff47596459c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4d85f221aff47596459c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-75a662ff951488d52e0f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-75a662ff951488d52e0f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aca0896dd9085a9b99ef"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-aca0896dd9085a9b99ef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-N-in-1; to port: 1-W-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-040fd6cb410278cc1b53"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-040fd6cb410278cc1b53`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-03d67744c3e408da8ab6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-03d67744c3e408da8ab6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-82e808354d738c96e64a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-82e808354d738c96e64a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-40b0232781e708080ce5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-40b0232781e708080ce5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-N-in-1; to port: 1-E-out-11; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d40b779e968ea04bc5fd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d40b779e968ea04bc5fd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-E-out-11; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3c94d52172637fca1d5e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3c94d52172637fca1d5e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-E-out-11; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c2ac241e33312d44442e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c2ac241e33312d44442e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-E-out-11; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2011e8780ef7c302f559"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2011e8780ef7c302f559`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-E-out-11; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-N-in-1; to port: 1-E-out-12; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0ff19418709d2493ad67"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0ff19418709d2493ad67`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-E-out-12; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5d7d4d757fcab5dca5b0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5d7d4d757fcab5dca5b0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-E-out-12; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-716697e2cf24b1134d90"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-716697e2cf24b1134d90`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-E-out-12; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-479acc8b7bf40d5f7456"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-479acc8b7bf40d5f7456`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-E-out-12; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-N-in-1; to port: 1-W-out-15; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d3f4b7c1ce6206d5ab6e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d3f4b7c1ce6206d5ab6e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-15; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9bf2395d2c9dfa4e3fbf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9bf2395d2c9dfa4e3fbf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-15; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d33aa1d84f6731f23d3a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d33aa1d84f6731f23d3a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-15; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-24ef917b23aa82339720"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-24ef917b23aa82339720`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-15; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-N-in-1; to port: 1-N-out-18; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c0e8a0e5a2e69361d80c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c0e8a0e5a2e69361d80c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-N-out-18; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-774d192e2d434145225c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-774d192e2d434145225c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-N-out-18; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-201e305e8e574d3ac381"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-201e305e8e574d3ac381`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-N-out-18; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0dea8e7303e2270ddea2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0dea8e7303e2270ddea2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-N-out-18; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-N-in-1; to port: 1-N-out-20; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0281c52aa8b78b591392"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0281c52aa8b78b591392`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-N-out-20; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b4a6684715a52ac45551"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b4a6684715a52ac45551`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-N-out-20; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7e36fa42b0c5c8a5e3f8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7e36fa42b0c5c8a5e3f8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-N-out-20; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b0f5c97585dd96b23396"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b0f5c97585dd96b23396`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-N-out-20; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

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
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-W-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-86cbb6b44d0444dd8773"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-86cbb6b44d0444dd8773`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ad0f1d19e94cf92dec0f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ad0f1d19e94cf92dec0f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a917921c8387c0a471a1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a917921c8387c0a471a1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ea90d006e0aa9b186385"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ea90d006e0aa9b186385`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-9; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-W-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-da6f0ab98782dd08bd23"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-da6f0ab98782dd08bd23`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d29cc6beb0653b6a1a01"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d29cc6beb0653b6a1a01`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f22353c79c4239ebb18f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f22353c79c4239ebb18f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-73989a38dc42df535b9b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-73989a38dc42df535b9b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-E-out-11; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e3e51e71e3bddf30643d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e3e51e71e3bddf30643d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-11; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-58c7fda71fc6bc726093"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-58c7fda71fc6bc726093`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-11; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ae07d8cdaefc83458bab"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ae07d8cdaefc83458bab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-11; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-244f9958971a36de97df"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-244f9958971a36de97df`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-11; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-E-out-12; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6496daebe51f6507b37e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6496daebe51f6507b37e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-12; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ed8573891f2830f39928"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ed8573891f2830f39928`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-12; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-01bef3d04f2571c57dc8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-01bef3d04f2571c57dc8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-12; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ac56d8b86efe39ed356d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ac56d8b86efe39ed356d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-12; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-W-out-15; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-95791c5ce0194005c2b4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-95791c5ce0194005c2b4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-15; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-379e82e7a3bbcd05e0fa"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-379e82e7a3bbcd05e0fa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-15; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c6298035cb87d24b6685"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c6298035cb87d24b6685`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-15; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-edc04d23b4eaff6c4168"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-edc04d23b4eaff6c4168`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-15; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-N-out-18; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e3c7d837decdd00dd8df"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e3c7d837decdd00dd8df`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-18; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-509b222004471bf9c415"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-509b222004471bf9c415`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-18; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d7b133a0bc78bede583b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d7b133a0bc78bede583b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-18; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-42e3a80cf0844c2d3734"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-42e3a80cf0844c2d3734`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-18; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-N-out-20; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0e8600956565bd9c10bf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0e8600956565bd9c10bf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-20; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a699888447385eefd077"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a699888447385eefd077`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-20; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-79df18d3683a3d901412"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-79df18d3683a3d901412`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-20; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2becf66b0691fee463b3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2becf66b0691fee463b3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-20; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

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

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-modular-highway-stamp:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-modular-highway-stamp:canonical-top</summary>

<a id="case-preview_review-6c920606f065b904cb40"></a>

**General: unverified** — `preview_review-6c920606f065b904cb40`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-modular-highway-stamp:canonical-top.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-modular-highway-stamp:connection-overview</summary>

<a id="case-preview_review-2c859da8ec79008b8a8c"></a>

**General: unverified** — `preview_review-2c859da8ec79008b8a8c`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-modular-highway-stamp:connection-overview.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

The modular experiment preserves the accepted compact diamond on its original branch. A new highway stamp retains 25 canonical cell models and all 27 canonical PATHs; two Avenue-only cells restore pristine native pavement. Four R40 ramp continuations and two new terminals attach separately. The retained compact grades and junctions remain independently available under their original identifiers.
