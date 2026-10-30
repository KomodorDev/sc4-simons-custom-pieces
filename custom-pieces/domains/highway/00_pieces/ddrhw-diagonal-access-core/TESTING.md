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

Coordinates the crossing and the ramp landing fragments that share its five construction tiles. It preserves both opposing highway decks, the four avenue car lanes, and both avenue pedestrian channels. The generated records below describe movements measured from saved PATH resources, meaning the game’s directed traffic routes. A measured route does not establish game operation or a complete native joining boundary.

<!-- BEGIN CONNECTIONS -->

### Connections and journeys

Generated from [connections.json](connections.json). Coordinates are canonical east, north, and height in metres. A connection class names an encoded route interface; it does not prove visible deck/wall fit or an in-game test.

Supported placement states: 0° CCW, 90° CCW, 180° CCW, 270° CCW. Each state has its own declared manual scope.

A **port** is one directional transport-path endpoint. **Service** identifies the intended network service (for example HSR, street, or tram); **engine** is its internal traffic-class number, separate from the construction network. **Role** distinguishes primary service from auxiliary paths; sharing a traffic class does not establish service compatibility.

A **tangent** is a unit travel-direction vector: `[0,1]` means north. **Grade** is height gained per horizontal metre. These measured facts describe this subject alone. Compatibility requires a separate comparison of the complete joining boundaries; physical seams and actual game operation require their own evidence. See the [class index](../../connection-classes.jsonc) for shared route-interface membership.

| Port | Service / engine / role | Direction | Location; tangent; grade | Connection class |
| --- | --- | --- | --- | --- |
| `1-W-out-1` | road / 1 / primary | out | [-8.0, -8.015569, 0.0]; [-0.7262670265117477, -0.6874126898754375]; 0.0 | `path-interface-3f2ca4e6acea572cf874` |
| `1-N-in-2` | road / 1 / primary | in | [-7.983551, -8.0, 0.0]; [-0.7262670265117477, -0.6874126898754375]; 0.0 | `path-interface-9fee542e2f32b0277e7e` |
| `1-N-in-3` | road / 1 / primary | in | [-3.2, -8.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-668896c488171c19873d` |
| `1-N-in-4` | road / 1 / primary | in | [2.319815, -8.0, 0.0]; [0.09391102439744659, -0.9955805941743854]; 0.0 | `path-interface-4140cdcf597bc98414bc` |
| `1-N-in-5` | road / 1 / primary | in | [3.2, -8.0, 0.0]; [0.7071067811865475, -0.7071067811865476]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `1-W-out-6` | road / 1 / primary | out | [8.0, -35.2, 7.5]; [-0.7071067811865475, -0.7071067811865477]; 0.0 | `path-interface-f9c18bdf77622a5e27b2` |
| `1-W-in-7` | road / 1 / primary | in | [8.0, -35.2, 15.0]; [0.7071067811865475, 0.7071067811865477]; 0.0 | `path-interface-3ed34d9a11bb64d98604` |
| `1-W-out-8` | road / 1 / primary | out | [8.0, -28.8, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-207fc37bf71ddd9e9cc7` |
| `1-W-in-9` | road / 1 / primary | in | [8.0, -28.8, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-3e8c9380dd7fc6c63cb8` |
| `1-W-out-10` | road / 1 / primary | out | [8.0, -3.2, 0.0]; [-0.7071067811865476, 0.7071067811865475]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `1-W-out-11` | road / 1 / primary | out | [8.0, -2.319815, 0.0]; [-0.9955805941743854, 0.09391102439744659]; 0.0 | `path-interface-91cab4fc096c1737c37b` |
| `1-W-out-12` | road / 1 / primary | out | [8.0, 3.2, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `1-W-out-13` | road / 1 / primary | out | [8.0, 7.983551, 0.0]; [-0.6874126898754375, -0.7262670265117477]; 0.0 | `path-interface-41acbae6d917a56fc553` |
| `1-N-in-14` | road / 1 / primary | in | [8.015569, 8.0, 0.0]; [-0.6874126898754375, -0.7262670265117477]; 0.0 | `path-interface-d375ca0ca2d6594f2bcd` |
| `1-E-out-15` | road / 1 / primary | out | [24.0, -35.2, 0.0]; [0.7071067811865475, -0.7071067811865477]; 0.0 | `path-interface-7c732cbad30c1a957476` |
| `1-E-out-16` | road / 1 / primary | out | [24.0, -34.805841, 0.0]; [0.8277151763976565, -0.5611484534069363]; 0.0 | `path-interface-76afa9fcb157c192156c` |
| `1-E-out-17` | road / 1 / primary | out | [24.0, -28.8, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-c97bb85824c6523bf652` |
| `1-S-in-18` | road / 1 / primary | in | [28.8, -24.0, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-1d22b25ce4745f800f2c` |
| `1-N-in-19` | road / 1 / primary | in | [28.8, -8.0, 7.5]; [-0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-aad60a85e4675eaba5de` |
| `1-N-out-20` | road / 1 / primary | out | [28.8, -8.0, 15.0]; [0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-50bfaaffb0d43ee83a9b` |
| `1-S-in-21` | road / 1 / primary | in | [34.805841, -24.0, 0.0]; [-0.5611484534069363, 0.8277151763976565]; 0.0 | `path-interface-24061b69de696e6c8ae8` |
| `1-S-in-22` | road / 1 / primary | in | [35.2, -24.0, 0.0]; [-0.7071067811865477, 0.7071067811865475]; 0.0 | `path-interface-668896c488171c19873d` |
| `1-N-in-23` | road / 1 / primary | in | [35.2, -8.0, 7.5]; [-0.7071067811865477, -0.7071067811865475]; 0.0 | `path-interface-3ecbd7f665c425929ca6` |
| `1-N-out-24` | road / 1 / primary | out | [35.2, -8.0, 15.0]; [0.7071067811865477, 0.7071067811865475]; 0.0 | `path-interface-55ad67244a3a7bbd6c4b` |
| `2-N-in-1` | pedestrian / 2 / primary | in | [-7.3, -8.0, 0.0]; [0.7071067811865476, -0.7071067811865476]; 0.0 | `path-interface-2ec6b824afff9b450810` |
| `2-W-out-2` | pedestrian / 2 / primary | out | [8.0, 7.3, 0.0]; [-0.7071067811865476, 0.7071067811865476]; 0.0 | `path-interface-ef45fb4474012bf121a0` |
| `2-E-out-3` | pedestrian / 2 / primary | out | [24.0, -39.3, 0.0]; [0.7071067811865477, -0.7071067811865475]; 0.0 | `path-interface-ef45fb4474012bf121a0` |
| `2-S-in-4` | pedestrian / 2 / primary | in | [39.3, -24.0, 0.0]; [-0.7071067811865475, 0.7071067811865477]; 0.0 | `path-interface-2ec6b824afff9b450810` |

#### Directed journeys

| Service | Entry → exit | Role |
| --- | --- | --- |
| road | `1-N-in-2` → `1-W-out-1` | primary |
| road | `1-N-in-3` → `1-E-out-16` | primary |
| road | `1-N-in-3` → `1-E-out-15` | primary |
| road | `1-N-in-4` → `1-E-out-16` | primary |
| road | `1-N-in-4` → `1-E-out-15` | primary |
| road | `1-N-in-5` → `1-E-out-17` | primary |
| road | `1-W-in-7` → `1-N-out-24` | primary |
| road | `1-W-in-9` → `1-N-out-20` | primary |
| road | `1-N-in-14` → `1-W-out-13` | primary |
| road | `1-S-in-18` → `1-W-out-10` | primary |
| road | `1-N-in-19` → `1-W-out-8` | primary |
| road | `1-S-in-21` → `1-W-out-11` | primary |
| road | `1-S-in-21` → `1-W-out-12` | primary |
| road | `1-S-in-22` → `1-W-out-11` | primary |
| road | `1-S-in-22` → `1-W-out-12` | primary |
| road | `1-N-in-23` → `1-W-out-6` | primary |
| pedestrian | `2-N-in-1` → `2-E-out-3` | primary |
| pedestrian | `2-S-in-4` → `2-W-out-2` | primary |

#### Forbidden transfers

| From service / port | To service / port | Reason |
| --- | --- | --- |
| road / `1-N-in-2` | road / `1-W-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-2` | road / `1-W-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-2` | road / `1-W-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-2` | road / `1-W-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-2` | road / `1-W-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-2` | road / `1-W-out-13` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-2` | road / `1-E-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-2` | road / `1-E-out-16` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-2` | road / `1-E-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-2` | road / `1-N-out-20` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-2` | road / `1-N-out-24` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-2` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-2` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-3` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-3` | road / `1-W-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-3` | road / `1-W-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-3` | road / `1-W-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-3` | road / `1-W-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-3` | road / `1-W-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-3` | road / `1-W-out-13` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-3` | road / `1-E-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-3` | road / `1-N-out-20` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-3` | road / `1-N-out-24` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-3` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-3` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-4` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-4` | road / `1-W-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-4` | road / `1-W-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-4` | road / `1-W-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-4` | road / `1-W-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-4` | road / `1-W-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-4` | road / `1-W-out-13` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-4` | road / `1-E-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-4` | road / `1-N-out-20` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-4` | road / `1-N-out-24` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-4` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-4` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-W-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-W-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-W-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-W-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-W-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-W-out-13` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-E-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-E-out-16` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-N-out-20` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | road / `1-N-out-24` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-5` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-7` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-7` | road / `1-W-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-7` | road / `1-W-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-7` | road / `1-W-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-7` | road / `1-W-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-7` | road / `1-W-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-7` | road / `1-W-out-13` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-7` | road / `1-E-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-7` | road / `1-E-out-16` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-7` | road / `1-E-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-7` | road / `1-N-out-20` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-7` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-7` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-9` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-9` | road / `1-W-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-9` | road / `1-W-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-9` | road / `1-W-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-9` | road / `1-W-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-9` | road / `1-W-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-9` | road / `1-W-out-13` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-9` | road / `1-E-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-9` | road / `1-E-out-16` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-9` | road / `1-E-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-9` | road / `1-N-out-24` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-9` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-W-in-9` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-14` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-14` | road / `1-W-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-14` | road / `1-W-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-14` | road / `1-W-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-14` | road / `1-W-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-14` | road / `1-W-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-14` | road / `1-E-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-14` | road / `1-E-out-16` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-14` | road / `1-E-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-14` | road / `1-N-out-20` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-14` | road / `1-N-out-24` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-14` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-14` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-18` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-18` | road / `1-W-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-18` | road / `1-W-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-18` | road / `1-W-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-18` | road / `1-W-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-18` | road / `1-W-out-13` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-18` | road / `1-E-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-18` | road / `1-E-out-16` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-18` | road / `1-E-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-18` | road / `1-N-out-20` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-18` | road / `1-N-out-24` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-18` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-18` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-19` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-19` | road / `1-W-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-19` | road / `1-W-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-19` | road / `1-W-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-19` | road / `1-W-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-19` | road / `1-W-out-13` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-19` | road / `1-E-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-19` | road / `1-E-out-16` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-19` | road / `1-E-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-19` | road / `1-N-out-20` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-19` | road / `1-N-out-24` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-19` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-19` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-21` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-21` | road / `1-W-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-21` | road / `1-W-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-21` | road / `1-W-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-21` | road / `1-W-out-13` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-21` | road / `1-E-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-21` | road / `1-E-out-16` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-21` | road / `1-E-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-21` | road / `1-N-out-20` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-21` | road / `1-N-out-24` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-21` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-21` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-22` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-22` | road / `1-W-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-22` | road / `1-W-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-22` | road / `1-W-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-22` | road / `1-W-out-13` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-22` | road / `1-E-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-22` | road / `1-E-out-16` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-22` | road / `1-E-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-22` | road / `1-N-out-20` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-22` | road / `1-N-out-24` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-22` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-S-in-22` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-23` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-23` | road / `1-W-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-23` | road / `1-W-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-23` | road / `1-W-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-23` | road / `1-W-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-23` | road / `1-W-out-13` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-23` | road / `1-E-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-23` | road / `1-E-out-16` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-23` | road / `1-E-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-23` | road / `1-N-out-20` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-23` | road / `1-N-out-24` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-23` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| road / `1-N-in-23` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-N-in-1` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-N-in-1` | road / `1-W-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-N-in-1` | road / `1-W-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-N-in-1` | road / `1-W-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-N-in-1` | road / `1-W-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-N-in-1` | road / `1-W-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-N-in-1` | road / `1-W-out-13` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-N-in-1` | road / `1-E-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-N-in-1` | road / `1-E-out-16` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-N-in-1` | road / `1-E-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-N-in-1` | road / `1-N-out-20` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-N-in-1` | road / `1-N-out-24` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-N-in-1` | pedestrian / `2-W-out-2` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-S-in-4` | road / `1-W-out-1` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-S-in-4` | road / `1-W-out-6` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-S-in-4` | road / `1-W-out-8` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-S-in-4` | road / `1-W-out-10` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-S-in-4` | road / `1-W-out-11` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-S-in-4` | road / `1-W-out-12` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-S-in-4` | road / `1-W-out-13` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-S-in-4` | road / `1-E-out-15` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-S-in-4` | road / `1-E-out-16` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-S-in-4` | road / `1-E-out-17` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-S-in-4` | road / `1-N-out-20` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-S-in-4` | road / `1-N-out-24` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |
| pedestrian / `2-S-in-4` | pedestrian / `2-E-out-3` | No directed route exists between these ports in the saved piece transport paths. In-game confirmation remains unverified. |

Review the test checklist for the exact tested cases and environments.

<!-- END CONNECTIONS -->

## 2. Test setup

Use the exact NAM 50 right-hand-traffic profile in `config/profiles/nam50-rhd.jsonc`, flat terrain, and the [assembly test setup](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#2-test-setup). Keep personal settings and game archives outside Git. Building does not install this component.

## 3. Software checks

From the repository root, build the selected component with `python3 -B custom-pieces/scp.py build --include ddrhw-diagonal-access-core --output custom-pieces/dist/highway-component`, then run `python3 -B custom-pieces/scp.py verify --output custom-pieces/dist/highway-component`. Run the shared [highway checks](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#3-software-checks) for geometry, saved paths, and assembled seams. Model verification checks actual saved triangles and PATH points; it does not merely reread a source label.

## 4. Game checks

Place this component as part of the complete assembly in each of its four rotations. Check its roads, barriers, and neighbouring seams; use Route Query and visible traffic to observe each listed movement independently. Check avenue pedestrians where present. Demolish and replace it, save the city, reload it, and inspect shadows at several game times. Use the [shared observation procedure](../../../../docs/TESTING.md) to record only matching human observations.

## 5. Results and known issues

The current assembly’s executed checks and remaining limitations are recorded in [Results and known issues](../../01_assemblies/ddrhw-l1-and-l2-diagonal-avenue-diamond/TESTING.md#5-results-and-known-issues). This component is experimental and has no human game pass. Native DD models have local overhangs; pavement coverage and corridor face-intersection checks are not a complete vehicle swept-volume or structural proof.

<!-- BEGIN MANUAL SUMMARY -->

### Manual status

Generated from [the exact test cases](#test-checklist) and [authoritative observations](checks/manual-tests.json).

- [ ] Preview review: 0/2 applicable cases passed; 0 failed, 0 stale.
- [ ] In-game rendering: 0/4 applicable cases passed; 0 failed, 0 stale.
- [ ] Route Query: 0/72 applicable cases passed; 0 failed, 0 stale.
- [ ] Visible travel: 0/72 applicable cases passed; 0 failed, 0 stale.

These observations cover only the named services, directions, poses, rotations, and recorded platforms.

<!-- END MANUAL SUMMARY -->

<!-- BEGIN MANUAL CHECKS -->

### Test checklist

Generated from [the authoritative record](checks/manual-tests.json). Only explicit human observations create manual passes; software and preview checks remain separate. Expand a check/service group to see its rotation table, then expand the matching exact scope to copy a case ID and inspect its pose, reviewer, environment, and evidence. Grouping changes only this view; every declared case remains separate.

**States:** [x] passed; [ ] unverified, failed, or stale; N/A is an explicit inapplicable declaration. A dash means no case was declared in that column. Every pass covers only its recorded environment. T means a distinct construction-transposed state.

Four proper rotations are covered. No additional reflected state is established by this record; repeated construction aliases do not create new orientations.

Current totals: unverified: 876, passed: 0, failed: 0, stale: 0, not_applicable: 0.

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
<summary>Route Query — road — 64 cases; unverified: 64</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-2>1-W-out-1; entry: 1-N-in-2; exit: 1-W-out-1 | — | <a href="#case-in_game_route_query-58b2ca5fb460e01291ca">[ ] unverified</a> | <a href="#case-in_game_route_query-8e05d214fda82a0a8647">[ ] unverified</a> | <a href="#case-in_game_route_query-978d768ad7917148f512">[ ] unverified</a> | <a href="#case-in_game_route_query-09fd2c40724d028a6b35">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-3>1-E-out-16; entry: 1-N-in-3; exit: 1-E-out-16 | — | <a href="#case-in_game_route_query-58d138e61953cfb4c768">[ ] unverified</a> | <a href="#case-in_game_route_query-ebf0e32bea7cbd166695">[ ] unverified</a> | <a href="#case-in_game_route_query-b273c208b1836b94e9c4">[ ] unverified</a> | <a href="#case-in_game_route_query-86514b25dacb00bf7caf">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-3>1-E-out-15; entry: 1-N-in-3; exit: 1-E-out-15 | — | <a href="#case-in_game_route_query-1de08ff51f99fa0cbb10">[ ] unverified</a> | <a href="#case-in_game_route_query-ea45a52cdf891e0e4a84">[ ] unverified</a> | <a href="#case-in_game_route_query-9d9c260bcf8052218081">[ ] unverified</a> | <a href="#case-in_game_route_query-a1e53422dc1dc065c163">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-4>1-E-out-16; entry: 1-N-in-4; exit: 1-E-out-16 | — | <a href="#case-in_game_route_query-d3223e0c86f117244461">[ ] unverified</a> | <a href="#case-in_game_route_query-6240126c24de3862c176">[ ] unverified</a> | <a href="#case-in_game_route_query-88eff64583e65b2781f7">[ ] unverified</a> | <a href="#case-in_game_route_query-d3d0ac5f9826eb3d9f84">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-4>1-E-out-15; entry: 1-N-in-4; exit: 1-E-out-15 | — | <a href="#case-in_game_route_query-3fc274076c10af649bd1">[ ] unverified</a> | <a href="#case-in_game_route_query-03136733ba6af816fb5f">[ ] unverified</a> | <a href="#case-in_game_route_query-8f9e7ba0570f9c879665">[ ] unverified</a> | <a href="#case-in_game_route_query-e7e03df9897b546bb641">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-5>1-E-out-17; entry: 1-N-in-5; exit: 1-E-out-17 | — | <a href="#case-in_game_route_query-525596ecf1df306144e4">[ ] unverified</a> | <a href="#case-in_game_route_query-e68d720800a23a37c316">[ ] unverified</a> | <a href="#case-in_game_route_query-5866d00b482747896153">[ ] unverified</a> | <a href="#case-in_game_route_query-75ff29d808892a97dbf4">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-7>1-N-out-24; entry: 1-W-in-7; exit: 1-N-out-24 | — | <a href="#case-in_game_route_query-0f5e46ea13467e2f9e2e">[ ] unverified</a> | <a href="#case-in_game_route_query-1db652454eaa297b2da0">[ ] unverified</a> | <a href="#case-in_game_route_query-686c865fb8f709f83329">[ ] unverified</a> | <a href="#case-in_game_route_query-cc2ad7d7d853e2b3c6af">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-W-in-9>1-N-out-20; entry: 1-W-in-9; exit: 1-N-out-20 | — | <a href="#case-in_game_route_query-9f22367ccfb76c9c91da">[ ] unverified</a> | <a href="#case-in_game_route_query-30b3ac1be7a29bd102a5">[ ] unverified</a> | <a href="#case-in_game_route_query-ece89691b01ea5aef57e">[ ] unverified</a> | <a href="#case-in_game_route_query-ef4eccaf0bd391c3978a">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-14>1-W-out-13; entry: 1-N-in-14; exit: 1-W-out-13 | — | <a href="#case-in_game_route_query-1ea9c882793c11b0e1b2">[ ] unverified</a> | <a href="#case-in_game_route_query-890caf366804e2634806">[ ] unverified</a> | <a href="#case-in_game_route_query-cfba713a50fbc717c7e0">[ ] unverified</a> | <a href="#case-in_game_route_query-3c5652dfb2480ed90bcd">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-S-in-18>1-W-out-10; entry: 1-S-in-18; exit: 1-W-out-10 | — | <a href="#case-in_game_route_query-7d557625ce9423c0ff22">[ ] unverified</a> | <a href="#case-in_game_route_query-be376ba2bd4a83b54990">[ ] unverified</a> | <a href="#case-in_game_route_query-da01dec27c5c4cd5f508">[ ] unverified</a> | <a href="#case-in_game_route_query-2fc7d6ff53b8a31ef288">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-19>1-W-out-8; entry: 1-N-in-19; exit: 1-W-out-8 | — | <a href="#case-in_game_route_query-c6f2c23458040a4ad7a1">[ ] unverified</a> | <a href="#case-in_game_route_query-a266793c4555b81e95fb">[ ] unverified</a> | <a href="#case-in_game_route_query-9927e64084e46d3f3a8a">[ ] unverified</a> | <a href="#case-in_game_route_query-8a6d4d5732f7111d45e0">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-S-in-21>1-W-out-11; entry: 1-S-in-21; exit: 1-W-out-11 | — | <a href="#case-in_game_route_query-18a16f1c64d43655fda4">[ ] unverified</a> | <a href="#case-in_game_route_query-73b7ad25b263a126488b">[ ] unverified</a> | <a href="#case-in_game_route_query-90edb317b794a61ca3a2">[ ] unverified</a> | <a href="#case-in_game_route_query-a23d64122122ad9fcea6">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-S-in-21>1-W-out-12; entry: 1-S-in-21; exit: 1-W-out-12 | — | <a href="#case-in_game_route_query-f24b3c46bb096a4dccd8">[ ] unverified</a> | <a href="#case-in_game_route_query-c2165593f58bf7a5590b">[ ] unverified</a> | <a href="#case-in_game_route_query-6cf2c8fb98ca18f49d8e">[ ] unverified</a> | <a href="#case-in_game_route_query-506994406fddf0804ec8">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-S-in-22>1-W-out-11; entry: 1-S-in-22; exit: 1-W-out-11 | — | <a href="#case-in_game_route_query-0dee53c7bf4056b2d052">[ ] unverified</a> | <a href="#case-in_game_route_query-b427df4eb364d43c8acc">[ ] unverified</a> | <a href="#case-in_game_route_query-2223f1d05efd301b6e26">[ ] unverified</a> | <a href="#case-in_game_route_query-ad6db302422198f16993">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-S-in-22>1-W-out-12; entry: 1-S-in-22; exit: 1-W-out-12 | — | <a href="#case-in_game_route_query-7e4f77a1aefb8bfb2bbd">[ ] unverified</a> | <a href="#case-in_game_route_query-8f7eef13e603e2da6889">[ ] unverified</a> | <a href="#case-in_game_route_query-35e7fba1f0bec65a068c">[ ] unverified</a> | <a href="#case-in_game_route_query-170e346beb2bc9deaff7">[ ] unverified</a> |
| **Route Query**<br>Service: road; role: primary; journey: 1:1-N-in-23>1-W-out-6; entry: 1-N-in-23; exit: 1-W-out-6 | — | <a href="#case-in_game_route_query-26ab56d419535747438c">[ ] unverified</a> | <a href="#case-in_game_route_query-9ce736dadda4958e8e2e">[ ] unverified</a> | <a href="#case-in_game_route_query-9e941def5ab7df150aae">[ ] unverified</a> | <a href="#case-in_game_route_query-e7f0d31d5353cc476ab9">[ ] unverified</a> |


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-2>1-W-out-1; entry: 1-N-in-2; exit: 1-W-out-1</summary>

<a id="case-in_game_route_query-58b2ca5fb460e01291ca"></a>

**0° CCW: unverified** — `in_game_route_query-58b2ca5fb460e01291ca`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-2>1-W-out-1; entry: 1-N-in-2; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_route_query-8e05d214fda82a0a8647"></a>

**90° CCW: unverified** — `in_game_route_query-8e05d214fda82a0a8647`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-2>1-W-out-1; entry: 1-N-in-2; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_route_query-978d768ad7917148f512"></a>

**180° CCW: unverified** — `in_game_route_query-978d768ad7917148f512`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-2>1-W-out-1; entry: 1-N-in-2; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_route_query-09fd2c40724d028a6b35"></a>

**270° CCW: unverified** — `in_game_route_query-09fd2c40724d028a6b35`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-2>1-W-out-1; entry: 1-N-in-2; exit: 1-W-out-1.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-3>1-E-out-16; entry: 1-N-in-3; exit: 1-E-out-16</summary>

<a id="case-in_game_route_query-58d138e61953cfb4c768"></a>

**0° CCW: unverified** — `in_game_route_query-58d138e61953cfb4c768`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-3>1-E-out-16; entry: 1-N-in-3; exit: 1-E-out-16.

No observation recorded.

<a id="case-in_game_route_query-ebf0e32bea7cbd166695"></a>

**90° CCW: unverified** — `in_game_route_query-ebf0e32bea7cbd166695`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-3>1-E-out-16; entry: 1-N-in-3; exit: 1-E-out-16.

No observation recorded.

<a id="case-in_game_route_query-b273c208b1836b94e9c4"></a>

**180° CCW: unverified** — `in_game_route_query-b273c208b1836b94e9c4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-3>1-E-out-16; entry: 1-N-in-3; exit: 1-E-out-16.

No observation recorded.

<a id="case-in_game_route_query-86514b25dacb00bf7caf"></a>

**270° CCW: unverified** — `in_game_route_query-86514b25dacb00bf7caf`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-3>1-E-out-16; entry: 1-N-in-3; exit: 1-E-out-16.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-3>1-E-out-15; entry: 1-N-in-3; exit: 1-E-out-15</summary>

<a id="case-in_game_route_query-1de08ff51f99fa0cbb10"></a>

**0° CCW: unverified** — `in_game_route_query-1de08ff51f99fa0cbb10`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-3>1-E-out-15; entry: 1-N-in-3; exit: 1-E-out-15.

No observation recorded.

<a id="case-in_game_route_query-ea45a52cdf891e0e4a84"></a>

**90° CCW: unverified** — `in_game_route_query-ea45a52cdf891e0e4a84`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-3>1-E-out-15; entry: 1-N-in-3; exit: 1-E-out-15.

No observation recorded.

<a id="case-in_game_route_query-9d9c260bcf8052218081"></a>

**180° CCW: unverified** — `in_game_route_query-9d9c260bcf8052218081`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-3>1-E-out-15; entry: 1-N-in-3; exit: 1-E-out-15.

No observation recorded.

<a id="case-in_game_route_query-a1e53422dc1dc065c163"></a>

**270° CCW: unverified** — `in_game_route_query-a1e53422dc1dc065c163`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-3>1-E-out-15; entry: 1-N-in-3; exit: 1-E-out-15.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-4>1-E-out-16; entry: 1-N-in-4; exit: 1-E-out-16</summary>

<a id="case-in_game_route_query-d3223e0c86f117244461"></a>

**0° CCW: unverified** — `in_game_route_query-d3223e0c86f117244461`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-4>1-E-out-16; entry: 1-N-in-4; exit: 1-E-out-16.

No observation recorded.

<a id="case-in_game_route_query-6240126c24de3862c176"></a>

**90° CCW: unverified** — `in_game_route_query-6240126c24de3862c176`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-4>1-E-out-16; entry: 1-N-in-4; exit: 1-E-out-16.

No observation recorded.

<a id="case-in_game_route_query-88eff64583e65b2781f7"></a>

**180° CCW: unverified** — `in_game_route_query-88eff64583e65b2781f7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-4>1-E-out-16; entry: 1-N-in-4; exit: 1-E-out-16.

No observation recorded.

<a id="case-in_game_route_query-d3d0ac5f9826eb3d9f84"></a>

**270° CCW: unverified** — `in_game_route_query-d3d0ac5f9826eb3d9f84`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-4>1-E-out-16; entry: 1-N-in-4; exit: 1-E-out-16.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-4>1-E-out-15; entry: 1-N-in-4; exit: 1-E-out-15</summary>

<a id="case-in_game_route_query-3fc274076c10af649bd1"></a>

**0° CCW: unverified** — `in_game_route_query-3fc274076c10af649bd1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-4>1-E-out-15; entry: 1-N-in-4; exit: 1-E-out-15.

No observation recorded.

<a id="case-in_game_route_query-03136733ba6af816fb5f"></a>

**90° CCW: unverified** — `in_game_route_query-03136733ba6af816fb5f`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-4>1-E-out-15; entry: 1-N-in-4; exit: 1-E-out-15.

No observation recorded.

<a id="case-in_game_route_query-8f9e7ba0570f9c879665"></a>

**180° CCW: unverified** — `in_game_route_query-8f9e7ba0570f9c879665`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-4>1-E-out-15; entry: 1-N-in-4; exit: 1-E-out-15.

No observation recorded.

<a id="case-in_game_route_query-e7e03df9897b546bb641"></a>

**270° CCW: unverified** — `in_game_route_query-e7e03df9897b546bb641`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-4>1-E-out-15; entry: 1-N-in-4; exit: 1-E-out-15.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-5>1-E-out-17; entry: 1-N-in-5; exit: 1-E-out-17</summary>

<a id="case-in_game_route_query-525596ecf1df306144e4"></a>

**0° CCW: unverified** — `in_game_route_query-525596ecf1df306144e4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-5>1-E-out-17; entry: 1-N-in-5; exit: 1-E-out-17.

No observation recorded.

<a id="case-in_game_route_query-e68d720800a23a37c316"></a>

**90° CCW: unverified** — `in_game_route_query-e68d720800a23a37c316`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-5>1-E-out-17; entry: 1-N-in-5; exit: 1-E-out-17.

No observation recorded.

<a id="case-in_game_route_query-5866d00b482747896153"></a>

**180° CCW: unverified** — `in_game_route_query-5866d00b482747896153`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-5>1-E-out-17; entry: 1-N-in-5; exit: 1-E-out-17.

No observation recorded.

<a id="case-in_game_route_query-75ff29d808892a97dbf4"></a>

**270° CCW: unverified** — `in_game_route_query-75ff29d808892a97dbf4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-5>1-E-out-17; entry: 1-N-in-5; exit: 1-E-out-17.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-7>1-N-out-24; entry: 1-W-in-7; exit: 1-N-out-24</summary>

<a id="case-in_game_route_query-0f5e46ea13467e2f9e2e"></a>

**0° CCW: unverified** — `in_game_route_query-0f5e46ea13467e2f9e2e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-7>1-N-out-24; entry: 1-W-in-7; exit: 1-N-out-24.

No observation recorded.

<a id="case-in_game_route_query-1db652454eaa297b2da0"></a>

**90° CCW: unverified** — `in_game_route_query-1db652454eaa297b2da0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-7>1-N-out-24; entry: 1-W-in-7; exit: 1-N-out-24.

No observation recorded.

<a id="case-in_game_route_query-686c865fb8f709f83329"></a>

**180° CCW: unverified** — `in_game_route_query-686c865fb8f709f83329`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-7>1-N-out-24; entry: 1-W-in-7; exit: 1-N-out-24.

No observation recorded.

<a id="case-in_game_route_query-cc2ad7d7d853e2b3c6af"></a>

**270° CCW: unverified** — `in_game_route_query-cc2ad7d7d853e2b3c6af`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-7>1-N-out-24; entry: 1-W-in-7; exit: 1-N-out-24.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-W-in-9>1-N-out-20; entry: 1-W-in-9; exit: 1-N-out-20</summary>

<a id="case-in_game_route_query-9f22367ccfb76c9c91da"></a>

**0° CCW: unverified** — `in_game_route_query-9f22367ccfb76c9c91da`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-9>1-N-out-20; entry: 1-W-in-9; exit: 1-N-out-20.

No observation recorded.

<a id="case-in_game_route_query-30b3ac1be7a29bd102a5"></a>

**90° CCW: unverified** — `in_game_route_query-30b3ac1be7a29bd102a5`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-9>1-N-out-20; entry: 1-W-in-9; exit: 1-N-out-20.

No observation recorded.

<a id="case-in_game_route_query-ece89691b01ea5aef57e"></a>

**180° CCW: unverified** — `in_game_route_query-ece89691b01ea5aef57e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-9>1-N-out-20; entry: 1-W-in-9; exit: 1-N-out-20.

No observation recorded.

<a id="case-in_game_route_query-ef4eccaf0bd391c3978a"></a>

**270° CCW: unverified** — `in_game_route_query-ef4eccaf0bd391c3978a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-W-in-9>1-N-out-20; entry: 1-W-in-9; exit: 1-N-out-20.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-14>1-W-out-13; entry: 1-N-in-14; exit: 1-W-out-13</summary>

<a id="case-in_game_route_query-1ea9c882793c11b0e1b2"></a>

**0° CCW: unverified** — `in_game_route_query-1ea9c882793c11b0e1b2`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-14>1-W-out-13; entry: 1-N-in-14; exit: 1-W-out-13.

No observation recorded.

<a id="case-in_game_route_query-890caf366804e2634806"></a>

**90° CCW: unverified** — `in_game_route_query-890caf366804e2634806`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-14>1-W-out-13; entry: 1-N-in-14; exit: 1-W-out-13.

No observation recorded.

<a id="case-in_game_route_query-cfba713a50fbc717c7e0"></a>

**180° CCW: unverified** — `in_game_route_query-cfba713a50fbc717c7e0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-14>1-W-out-13; entry: 1-N-in-14; exit: 1-W-out-13.

No observation recorded.

<a id="case-in_game_route_query-3c5652dfb2480ed90bcd"></a>

**270° CCW: unverified** — `in_game_route_query-3c5652dfb2480ed90bcd`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-14>1-W-out-13; entry: 1-N-in-14; exit: 1-W-out-13.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-S-in-18>1-W-out-10; entry: 1-S-in-18; exit: 1-W-out-10</summary>

<a id="case-in_game_route_query-7d557625ce9423c0ff22"></a>

**0° CCW: unverified** — `in_game_route_query-7d557625ce9423c0ff22`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-18>1-W-out-10; entry: 1-S-in-18; exit: 1-W-out-10.

No observation recorded.

<a id="case-in_game_route_query-be376ba2bd4a83b54990"></a>

**90° CCW: unverified** — `in_game_route_query-be376ba2bd4a83b54990`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-18>1-W-out-10; entry: 1-S-in-18; exit: 1-W-out-10.

No observation recorded.

<a id="case-in_game_route_query-da01dec27c5c4cd5f508"></a>

**180° CCW: unverified** — `in_game_route_query-da01dec27c5c4cd5f508`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-18>1-W-out-10; entry: 1-S-in-18; exit: 1-W-out-10.

No observation recorded.

<a id="case-in_game_route_query-2fc7d6ff53b8a31ef288"></a>

**270° CCW: unverified** — `in_game_route_query-2fc7d6ff53b8a31ef288`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-18>1-W-out-10; entry: 1-S-in-18; exit: 1-W-out-10.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-19>1-W-out-8; entry: 1-N-in-19; exit: 1-W-out-8</summary>

<a id="case-in_game_route_query-c6f2c23458040a4ad7a1"></a>

**0° CCW: unverified** — `in_game_route_query-c6f2c23458040a4ad7a1`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-19>1-W-out-8; entry: 1-N-in-19; exit: 1-W-out-8.

No observation recorded.

<a id="case-in_game_route_query-a266793c4555b81e95fb"></a>

**90° CCW: unverified** — `in_game_route_query-a266793c4555b81e95fb`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-19>1-W-out-8; entry: 1-N-in-19; exit: 1-W-out-8.

No observation recorded.

<a id="case-in_game_route_query-9927e64084e46d3f3a8a"></a>

**180° CCW: unverified** — `in_game_route_query-9927e64084e46d3f3a8a`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-19>1-W-out-8; entry: 1-N-in-19; exit: 1-W-out-8.

No observation recorded.

<a id="case-in_game_route_query-8a6d4d5732f7111d45e0"></a>

**270° CCW: unverified** — `in_game_route_query-8a6d4d5732f7111d45e0`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-19>1-W-out-8; entry: 1-N-in-19; exit: 1-W-out-8.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-S-in-21>1-W-out-11; entry: 1-S-in-21; exit: 1-W-out-11</summary>

<a id="case-in_game_route_query-18a16f1c64d43655fda4"></a>

**0° CCW: unverified** — `in_game_route_query-18a16f1c64d43655fda4`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-21>1-W-out-11; entry: 1-S-in-21; exit: 1-W-out-11.

No observation recorded.

<a id="case-in_game_route_query-73b7ad25b263a126488b"></a>

**90° CCW: unverified** — `in_game_route_query-73b7ad25b263a126488b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-21>1-W-out-11; entry: 1-S-in-21; exit: 1-W-out-11.

No observation recorded.

<a id="case-in_game_route_query-90edb317b794a61ca3a2"></a>

**180° CCW: unverified** — `in_game_route_query-90edb317b794a61ca3a2`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-21>1-W-out-11; entry: 1-S-in-21; exit: 1-W-out-11.

No observation recorded.

<a id="case-in_game_route_query-a23d64122122ad9fcea6"></a>

**270° CCW: unverified** — `in_game_route_query-a23d64122122ad9fcea6`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-21>1-W-out-11; entry: 1-S-in-21; exit: 1-W-out-11.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-S-in-21>1-W-out-12; entry: 1-S-in-21; exit: 1-W-out-12</summary>

<a id="case-in_game_route_query-f24b3c46bb096a4dccd8"></a>

**0° CCW: unverified** — `in_game_route_query-f24b3c46bb096a4dccd8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-21>1-W-out-12; entry: 1-S-in-21; exit: 1-W-out-12.

No observation recorded.

<a id="case-in_game_route_query-c2165593f58bf7a5590b"></a>

**90° CCW: unverified** — `in_game_route_query-c2165593f58bf7a5590b`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-21>1-W-out-12; entry: 1-S-in-21; exit: 1-W-out-12.

No observation recorded.

<a id="case-in_game_route_query-6cf2c8fb98ca18f49d8e"></a>

**180° CCW: unverified** — `in_game_route_query-6cf2c8fb98ca18f49d8e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-21>1-W-out-12; entry: 1-S-in-21; exit: 1-W-out-12.

No observation recorded.

<a id="case-in_game_route_query-506994406fddf0804ec8"></a>

**270° CCW: unverified** — `in_game_route_query-506994406fddf0804ec8`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-21>1-W-out-12; entry: 1-S-in-21; exit: 1-W-out-12.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-S-in-22>1-W-out-11; entry: 1-S-in-22; exit: 1-W-out-11</summary>

<a id="case-in_game_route_query-0dee53c7bf4056b2d052"></a>

**0° CCW: unverified** — `in_game_route_query-0dee53c7bf4056b2d052`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-22>1-W-out-11; entry: 1-S-in-22; exit: 1-W-out-11.

No observation recorded.

<a id="case-in_game_route_query-b427df4eb364d43c8acc"></a>

**90° CCW: unverified** — `in_game_route_query-b427df4eb364d43c8acc`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-22>1-W-out-11; entry: 1-S-in-22; exit: 1-W-out-11.

No observation recorded.

<a id="case-in_game_route_query-2223f1d05efd301b6e26"></a>

**180° CCW: unverified** — `in_game_route_query-2223f1d05efd301b6e26`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-22>1-W-out-11; entry: 1-S-in-22; exit: 1-W-out-11.

No observation recorded.

<a id="case-in_game_route_query-ad6db302422198f16993"></a>

**270° CCW: unverified** — `in_game_route_query-ad6db302422198f16993`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-22>1-W-out-11; entry: 1-S-in-22; exit: 1-W-out-11.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-S-in-22>1-W-out-12; entry: 1-S-in-22; exit: 1-W-out-12</summary>

<a id="case-in_game_route_query-7e4f77a1aefb8bfb2bbd"></a>

**0° CCW: unverified** — `in_game_route_query-7e4f77a1aefb8bfb2bbd`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-22>1-W-out-12; entry: 1-S-in-22; exit: 1-W-out-12.

No observation recorded.

<a id="case-in_game_route_query-8f7eef13e603e2da6889"></a>

**90° CCW: unverified** — `in_game_route_query-8f7eef13e603e2da6889`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-22>1-W-out-12; entry: 1-S-in-22; exit: 1-W-out-12.

No observation recorded.

<a id="case-in_game_route_query-35e7fba1f0bec65a068c"></a>

**180° CCW: unverified** — `in_game_route_query-35e7fba1f0bec65a068c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-22>1-W-out-12; entry: 1-S-in-22; exit: 1-W-out-12.

No observation recorded.

<a id="case-in_game_route_query-170e346beb2bc9deaff7"></a>

**270° CCW: unverified** — `in_game_route_query-170e346beb2bc9deaff7`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-S-in-22>1-W-out-12; entry: 1-S-in-22; exit: 1-W-out-12.

No observation recorded.

</details>


<details>
<summary>Route Query — Service: road; role: primary; journey: 1:1-N-in-23>1-W-out-6; entry: 1-N-in-23; exit: 1-W-out-6</summary>

<a id="case-in_game_route_query-26ab56d419535747438c"></a>

**0° CCW: unverified** — `in_game_route_query-26ab56d419535747438c`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-23>1-W-out-6; entry: 1-N-in-23; exit: 1-W-out-6.

No observation recorded.

<a id="case-in_game_route_query-9ce736dadda4958e8e2e"></a>

**90° CCW: unverified** — `in_game_route_query-9ce736dadda4958e8e2e`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-23>1-W-out-6; entry: 1-N-in-23; exit: 1-W-out-6.

No observation recorded.

<a id="case-in_game_route_query-9e941def5ab7df150aae"></a>

**180° CCW: unverified** — `in_game_route_query-9e941def5ab7df150aae`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-23>1-W-out-6; entry: 1-N-in-23; exit: 1-W-out-6.

No observation recorded.

<a id="case-in_game_route_query-e7f0d31d5353cc476ab9"></a>

**270° CCW: unverified** — `in_game_route_query-e7f0d31d5353cc476ab9`.

Use Route Query in SimCity 4 to confirm this directed journey for its service network.

Scope: Service: road; role: primary; journey: 1:1-N-in-23>1-W-out-6; entry: 1-N-in-23; exit: 1-W-out-6.

No observation recorded.

</details>

</details>

<details>
<summary>Visible travel — road — 64 cases; unverified: 64</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-2>1-W-out-1; entry: 1-N-in-2; exit: 1-W-out-1 | — | <a href="#case-in_game_visible_travel-58b2ca5fb460e01291ca">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8e05d214fda82a0a8647">[ ] unverified</a> | <a href="#case-in_game_visible_travel-978d768ad7917148f512">[ ] unverified</a> | <a href="#case-in_game_visible_travel-09fd2c40724d028a6b35">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-3>1-E-out-16; entry: 1-N-in-3; exit: 1-E-out-16 | — | <a href="#case-in_game_visible_travel-58d138e61953cfb4c768">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ebf0e32bea7cbd166695">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b273c208b1836b94e9c4">[ ] unverified</a> | <a href="#case-in_game_visible_travel-86514b25dacb00bf7caf">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-3>1-E-out-15; entry: 1-N-in-3; exit: 1-E-out-15 | — | <a href="#case-in_game_visible_travel-1de08ff51f99fa0cbb10">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ea45a52cdf891e0e4a84">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9d9c260bcf8052218081">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a1e53422dc1dc065c163">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-4>1-E-out-16; entry: 1-N-in-4; exit: 1-E-out-16 | — | <a href="#case-in_game_visible_travel-d3223e0c86f117244461">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6240126c24de3862c176">[ ] unverified</a> | <a href="#case-in_game_visible_travel-88eff64583e65b2781f7">[ ] unverified</a> | <a href="#case-in_game_visible_travel-d3d0ac5f9826eb3d9f84">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-4>1-E-out-15; entry: 1-N-in-4; exit: 1-E-out-15 | — | <a href="#case-in_game_visible_travel-3fc274076c10af649bd1">[ ] unverified</a> | <a href="#case-in_game_visible_travel-03136733ba6af816fb5f">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8f9e7ba0570f9c879665">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e7e03df9897b546bb641">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-5>1-E-out-17; entry: 1-N-in-5; exit: 1-E-out-17 | — | <a href="#case-in_game_visible_travel-525596ecf1df306144e4">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e68d720800a23a37c316">[ ] unverified</a> | <a href="#case-in_game_visible_travel-5866d00b482747896153">[ ] unverified</a> | <a href="#case-in_game_visible_travel-75ff29d808892a97dbf4">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-7>1-N-out-24; entry: 1-W-in-7; exit: 1-N-out-24 | — | <a href="#case-in_game_visible_travel-0f5e46ea13467e2f9e2e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-1db652454eaa297b2da0">[ ] unverified</a> | <a href="#case-in_game_visible_travel-686c865fb8f709f83329">[ ] unverified</a> | <a href="#case-in_game_visible_travel-cc2ad7d7d853e2b3c6af">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-W-in-9>1-N-out-20; entry: 1-W-in-9; exit: 1-N-out-20 | — | <a href="#case-in_game_visible_travel-9f22367ccfb76c9c91da">[ ] unverified</a> | <a href="#case-in_game_visible_travel-30b3ac1be7a29bd102a5">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ece89691b01ea5aef57e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ef4eccaf0bd391c3978a">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-14>1-W-out-13; entry: 1-N-in-14; exit: 1-W-out-13 | — | <a href="#case-in_game_visible_travel-1ea9c882793c11b0e1b2">[ ] unverified</a> | <a href="#case-in_game_visible_travel-890caf366804e2634806">[ ] unverified</a> | <a href="#case-in_game_visible_travel-cfba713a50fbc717c7e0">[ ] unverified</a> | <a href="#case-in_game_visible_travel-3c5652dfb2480ed90bcd">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-S-in-18>1-W-out-10; entry: 1-S-in-18; exit: 1-W-out-10 | — | <a href="#case-in_game_visible_travel-7d557625ce9423c0ff22">[ ] unverified</a> | <a href="#case-in_game_visible_travel-be376ba2bd4a83b54990">[ ] unverified</a> | <a href="#case-in_game_visible_travel-da01dec27c5c4cd5f508">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2fc7d6ff53b8a31ef288">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-19>1-W-out-8; entry: 1-N-in-19; exit: 1-W-out-8 | — | <a href="#case-in_game_visible_travel-c6f2c23458040a4ad7a1">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a266793c4555b81e95fb">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9927e64084e46d3f3a8a">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8a6d4d5732f7111d45e0">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-S-in-21>1-W-out-11; entry: 1-S-in-21; exit: 1-W-out-11 | — | <a href="#case-in_game_visible_travel-18a16f1c64d43655fda4">[ ] unverified</a> | <a href="#case-in_game_visible_travel-73b7ad25b263a126488b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-90edb317b794a61ca3a2">[ ] unverified</a> | <a href="#case-in_game_visible_travel-a23d64122122ad9fcea6">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-S-in-21>1-W-out-12; entry: 1-S-in-21; exit: 1-W-out-12 | — | <a href="#case-in_game_visible_travel-f24b3c46bb096a4dccd8">[ ] unverified</a> | <a href="#case-in_game_visible_travel-c2165593f58bf7a5590b">[ ] unverified</a> | <a href="#case-in_game_visible_travel-6cf2c8fb98ca18f49d8e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-506994406fddf0804ec8">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-S-in-22>1-W-out-11; entry: 1-S-in-22; exit: 1-W-out-11 | — | <a href="#case-in_game_visible_travel-0dee53c7bf4056b2d052">[ ] unverified</a> | <a href="#case-in_game_visible_travel-b427df4eb364d43c8acc">[ ] unverified</a> | <a href="#case-in_game_visible_travel-2223f1d05efd301b6e26">[ ] unverified</a> | <a href="#case-in_game_visible_travel-ad6db302422198f16993">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-S-in-22>1-W-out-12; entry: 1-S-in-22; exit: 1-W-out-12 | — | <a href="#case-in_game_visible_travel-7e4f77a1aefb8bfb2bbd">[ ] unverified</a> | <a href="#case-in_game_visible_travel-8f7eef13e603e2da6889">[ ] unverified</a> | <a href="#case-in_game_visible_travel-35e7fba1f0bec65a068c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-170e346beb2bc9deaff7">[ ] unverified</a> |
| **Visible travel**<br>Service: road; role: primary; journey: 1:1-N-in-23>1-W-out-6; entry: 1-N-in-23; exit: 1-W-out-6 | — | <a href="#case-in_game_visible_travel-26ab56d419535747438c">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9ce736dadda4958e8e2e">[ ] unverified</a> | <a href="#case-in_game_visible_travel-9e941def5ab7df150aae">[ ] unverified</a> | <a href="#case-in_game_visible_travel-e7f0d31d5353cc476ab9">[ ] unverified</a> |


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-2>1-W-out-1; entry: 1-N-in-2; exit: 1-W-out-1</summary>

<a id="case-in_game_visible_travel-58b2ca5fb460e01291ca"></a>

**0° CCW: unverified** — `in_game_visible_travel-58b2ca5fb460e01291ca`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-2>1-W-out-1; entry: 1-N-in-2; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-8e05d214fda82a0a8647"></a>

**90° CCW: unverified** — `in_game_visible_travel-8e05d214fda82a0a8647`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-2>1-W-out-1; entry: 1-N-in-2; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-978d768ad7917148f512"></a>

**180° CCW: unverified** — `in_game_visible_travel-978d768ad7917148f512`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-2>1-W-out-1; entry: 1-N-in-2; exit: 1-W-out-1.

No observation recorded.

<a id="case-in_game_visible_travel-09fd2c40724d028a6b35"></a>

**270° CCW: unverified** — `in_game_visible_travel-09fd2c40724d028a6b35`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-2>1-W-out-1; entry: 1-N-in-2; exit: 1-W-out-1.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-3>1-E-out-16; entry: 1-N-in-3; exit: 1-E-out-16</summary>

<a id="case-in_game_visible_travel-58d138e61953cfb4c768"></a>

**0° CCW: unverified** — `in_game_visible_travel-58d138e61953cfb4c768`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-3>1-E-out-16; entry: 1-N-in-3; exit: 1-E-out-16.

No observation recorded.

<a id="case-in_game_visible_travel-ebf0e32bea7cbd166695"></a>

**90° CCW: unverified** — `in_game_visible_travel-ebf0e32bea7cbd166695`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-3>1-E-out-16; entry: 1-N-in-3; exit: 1-E-out-16.

No observation recorded.

<a id="case-in_game_visible_travel-b273c208b1836b94e9c4"></a>

**180° CCW: unverified** — `in_game_visible_travel-b273c208b1836b94e9c4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-3>1-E-out-16; entry: 1-N-in-3; exit: 1-E-out-16.

No observation recorded.

<a id="case-in_game_visible_travel-86514b25dacb00bf7caf"></a>

**270° CCW: unverified** — `in_game_visible_travel-86514b25dacb00bf7caf`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-3>1-E-out-16; entry: 1-N-in-3; exit: 1-E-out-16.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-3>1-E-out-15; entry: 1-N-in-3; exit: 1-E-out-15</summary>

<a id="case-in_game_visible_travel-1de08ff51f99fa0cbb10"></a>

**0° CCW: unverified** — `in_game_visible_travel-1de08ff51f99fa0cbb10`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-3>1-E-out-15; entry: 1-N-in-3; exit: 1-E-out-15.

No observation recorded.

<a id="case-in_game_visible_travel-ea45a52cdf891e0e4a84"></a>

**90° CCW: unverified** — `in_game_visible_travel-ea45a52cdf891e0e4a84`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-3>1-E-out-15; entry: 1-N-in-3; exit: 1-E-out-15.

No observation recorded.

<a id="case-in_game_visible_travel-9d9c260bcf8052218081"></a>

**180° CCW: unverified** — `in_game_visible_travel-9d9c260bcf8052218081`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-3>1-E-out-15; entry: 1-N-in-3; exit: 1-E-out-15.

No observation recorded.

<a id="case-in_game_visible_travel-a1e53422dc1dc065c163"></a>

**270° CCW: unverified** — `in_game_visible_travel-a1e53422dc1dc065c163`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-3>1-E-out-15; entry: 1-N-in-3; exit: 1-E-out-15.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-4>1-E-out-16; entry: 1-N-in-4; exit: 1-E-out-16</summary>

<a id="case-in_game_visible_travel-d3223e0c86f117244461"></a>

**0° CCW: unverified** — `in_game_visible_travel-d3223e0c86f117244461`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-4>1-E-out-16; entry: 1-N-in-4; exit: 1-E-out-16.

No observation recorded.

<a id="case-in_game_visible_travel-6240126c24de3862c176"></a>

**90° CCW: unverified** — `in_game_visible_travel-6240126c24de3862c176`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-4>1-E-out-16; entry: 1-N-in-4; exit: 1-E-out-16.

No observation recorded.

<a id="case-in_game_visible_travel-88eff64583e65b2781f7"></a>

**180° CCW: unverified** — `in_game_visible_travel-88eff64583e65b2781f7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-4>1-E-out-16; entry: 1-N-in-4; exit: 1-E-out-16.

No observation recorded.

<a id="case-in_game_visible_travel-d3d0ac5f9826eb3d9f84"></a>

**270° CCW: unverified** — `in_game_visible_travel-d3d0ac5f9826eb3d9f84`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-4>1-E-out-16; entry: 1-N-in-4; exit: 1-E-out-16.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-4>1-E-out-15; entry: 1-N-in-4; exit: 1-E-out-15</summary>

<a id="case-in_game_visible_travel-3fc274076c10af649bd1"></a>

**0° CCW: unverified** — `in_game_visible_travel-3fc274076c10af649bd1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-4>1-E-out-15; entry: 1-N-in-4; exit: 1-E-out-15.

No observation recorded.

<a id="case-in_game_visible_travel-03136733ba6af816fb5f"></a>

**90° CCW: unverified** — `in_game_visible_travel-03136733ba6af816fb5f`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-4>1-E-out-15; entry: 1-N-in-4; exit: 1-E-out-15.

No observation recorded.

<a id="case-in_game_visible_travel-8f9e7ba0570f9c879665"></a>

**180° CCW: unverified** — `in_game_visible_travel-8f9e7ba0570f9c879665`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-4>1-E-out-15; entry: 1-N-in-4; exit: 1-E-out-15.

No observation recorded.

<a id="case-in_game_visible_travel-e7e03df9897b546bb641"></a>

**270° CCW: unverified** — `in_game_visible_travel-e7e03df9897b546bb641`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-4>1-E-out-15; entry: 1-N-in-4; exit: 1-E-out-15.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-5>1-E-out-17; entry: 1-N-in-5; exit: 1-E-out-17</summary>

<a id="case-in_game_visible_travel-525596ecf1df306144e4"></a>

**0° CCW: unverified** — `in_game_visible_travel-525596ecf1df306144e4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-5>1-E-out-17; entry: 1-N-in-5; exit: 1-E-out-17.

No observation recorded.

<a id="case-in_game_visible_travel-e68d720800a23a37c316"></a>

**90° CCW: unverified** — `in_game_visible_travel-e68d720800a23a37c316`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-5>1-E-out-17; entry: 1-N-in-5; exit: 1-E-out-17.

No observation recorded.

<a id="case-in_game_visible_travel-5866d00b482747896153"></a>

**180° CCW: unverified** — `in_game_visible_travel-5866d00b482747896153`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-5>1-E-out-17; entry: 1-N-in-5; exit: 1-E-out-17.

No observation recorded.

<a id="case-in_game_visible_travel-75ff29d808892a97dbf4"></a>

**270° CCW: unverified** — `in_game_visible_travel-75ff29d808892a97dbf4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-5>1-E-out-17; entry: 1-N-in-5; exit: 1-E-out-17.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-7>1-N-out-24; entry: 1-W-in-7; exit: 1-N-out-24</summary>

<a id="case-in_game_visible_travel-0f5e46ea13467e2f9e2e"></a>

**0° CCW: unverified** — `in_game_visible_travel-0f5e46ea13467e2f9e2e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-7>1-N-out-24; entry: 1-W-in-7; exit: 1-N-out-24.

No observation recorded.

<a id="case-in_game_visible_travel-1db652454eaa297b2da0"></a>

**90° CCW: unverified** — `in_game_visible_travel-1db652454eaa297b2da0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-7>1-N-out-24; entry: 1-W-in-7; exit: 1-N-out-24.

No observation recorded.

<a id="case-in_game_visible_travel-686c865fb8f709f83329"></a>

**180° CCW: unverified** — `in_game_visible_travel-686c865fb8f709f83329`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-7>1-N-out-24; entry: 1-W-in-7; exit: 1-N-out-24.

No observation recorded.

<a id="case-in_game_visible_travel-cc2ad7d7d853e2b3c6af"></a>

**270° CCW: unverified** — `in_game_visible_travel-cc2ad7d7d853e2b3c6af`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-7>1-N-out-24; entry: 1-W-in-7; exit: 1-N-out-24.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-W-in-9>1-N-out-20; entry: 1-W-in-9; exit: 1-N-out-20</summary>

<a id="case-in_game_visible_travel-9f22367ccfb76c9c91da"></a>

**0° CCW: unverified** — `in_game_visible_travel-9f22367ccfb76c9c91da`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-9>1-N-out-20; entry: 1-W-in-9; exit: 1-N-out-20.

No observation recorded.

<a id="case-in_game_visible_travel-30b3ac1be7a29bd102a5"></a>

**90° CCW: unverified** — `in_game_visible_travel-30b3ac1be7a29bd102a5`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-9>1-N-out-20; entry: 1-W-in-9; exit: 1-N-out-20.

No observation recorded.

<a id="case-in_game_visible_travel-ece89691b01ea5aef57e"></a>

**180° CCW: unverified** — `in_game_visible_travel-ece89691b01ea5aef57e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-9>1-N-out-20; entry: 1-W-in-9; exit: 1-N-out-20.

No observation recorded.

<a id="case-in_game_visible_travel-ef4eccaf0bd391c3978a"></a>

**270° CCW: unverified** — `in_game_visible_travel-ef4eccaf0bd391c3978a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-W-in-9>1-N-out-20; entry: 1-W-in-9; exit: 1-N-out-20.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-14>1-W-out-13; entry: 1-N-in-14; exit: 1-W-out-13</summary>

<a id="case-in_game_visible_travel-1ea9c882793c11b0e1b2"></a>

**0° CCW: unverified** — `in_game_visible_travel-1ea9c882793c11b0e1b2`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-14>1-W-out-13; entry: 1-N-in-14; exit: 1-W-out-13.

No observation recorded.

<a id="case-in_game_visible_travel-890caf366804e2634806"></a>

**90° CCW: unverified** — `in_game_visible_travel-890caf366804e2634806`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-14>1-W-out-13; entry: 1-N-in-14; exit: 1-W-out-13.

No observation recorded.

<a id="case-in_game_visible_travel-cfba713a50fbc717c7e0"></a>

**180° CCW: unverified** — `in_game_visible_travel-cfba713a50fbc717c7e0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-14>1-W-out-13; entry: 1-N-in-14; exit: 1-W-out-13.

No observation recorded.

<a id="case-in_game_visible_travel-3c5652dfb2480ed90bcd"></a>

**270° CCW: unverified** — `in_game_visible_travel-3c5652dfb2480ed90bcd`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-14>1-W-out-13; entry: 1-N-in-14; exit: 1-W-out-13.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-S-in-18>1-W-out-10; entry: 1-S-in-18; exit: 1-W-out-10</summary>

<a id="case-in_game_visible_travel-7d557625ce9423c0ff22"></a>

**0° CCW: unverified** — `in_game_visible_travel-7d557625ce9423c0ff22`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-18>1-W-out-10; entry: 1-S-in-18; exit: 1-W-out-10.

No observation recorded.

<a id="case-in_game_visible_travel-be376ba2bd4a83b54990"></a>

**90° CCW: unverified** — `in_game_visible_travel-be376ba2bd4a83b54990`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-18>1-W-out-10; entry: 1-S-in-18; exit: 1-W-out-10.

No observation recorded.

<a id="case-in_game_visible_travel-da01dec27c5c4cd5f508"></a>

**180° CCW: unverified** — `in_game_visible_travel-da01dec27c5c4cd5f508`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-18>1-W-out-10; entry: 1-S-in-18; exit: 1-W-out-10.

No observation recorded.

<a id="case-in_game_visible_travel-2fc7d6ff53b8a31ef288"></a>

**270° CCW: unverified** — `in_game_visible_travel-2fc7d6ff53b8a31ef288`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-18>1-W-out-10; entry: 1-S-in-18; exit: 1-W-out-10.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-19>1-W-out-8; entry: 1-N-in-19; exit: 1-W-out-8</summary>

<a id="case-in_game_visible_travel-c6f2c23458040a4ad7a1"></a>

**0° CCW: unverified** — `in_game_visible_travel-c6f2c23458040a4ad7a1`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-19>1-W-out-8; entry: 1-N-in-19; exit: 1-W-out-8.

No observation recorded.

<a id="case-in_game_visible_travel-a266793c4555b81e95fb"></a>

**90° CCW: unverified** — `in_game_visible_travel-a266793c4555b81e95fb`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-19>1-W-out-8; entry: 1-N-in-19; exit: 1-W-out-8.

No observation recorded.

<a id="case-in_game_visible_travel-9927e64084e46d3f3a8a"></a>

**180° CCW: unverified** — `in_game_visible_travel-9927e64084e46d3f3a8a`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-19>1-W-out-8; entry: 1-N-in-19; exit: 1-W-out-8.

No observation recorded.

<a id="case-in_game_visible_travel-8a6d4d5732f7111d45e0"></a>

**270° CCW: unverified** — `in_game_visible_travel-8a6d4d5732f7111d45e0`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-19>1-W-out-8; entry: 1-N-in-19; exit: 1-W-out-8.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-S-in-21>1-W-out-11; entry: 1-S-in-21; exit: 1-W-out-11</summary>

<a id="case-in_game_visible_travel-18a16f1c64d43655fda4"></a>

**0° CCW: unverified** — `in_game_visible_travel-18a16f1c64d43655fda4`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-21>1-W-out-11; entry: 1-S-in-21; exit: 1-W-out-11.

No observation recorded.

<a id="case-in_game_visible_travel-73b7ad25b263a126488b"></a>

**90° CCW: unverified** — `in_game_visible_travel-73b7ad25b263a126488b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-21>1-W-out-11; entry: 1-S-in-21; exit: 1-W-out-11.

No observation recorded.

<a id="case-in_game_visible_travel-90edb317b794a61ca3a2"></a>

**180° CCW: unverified** — `in_game_visible_travel-90edb317b794a61ca3a2`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-21>1-W-out-11; entry: 1-S-in-21; exit: 1-W-out-11.

No observation recorded.

<a id="case-in_game_visible_travel-a23d64122122ad9fcea6"></a>

**270° CCW: unverified** — `in_game_visible_travel-a23d64122122ad9fcea6`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-21>1-W-out-11; entry: 1-S-in-21; exit: 1-W-out-11.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-S-in-21>1-W-out-12; entry: 1-S-in-21; exit: 1-W-out-12</summary>

<a id="case-in_game_visible_travel-f24b3c46bb096a4dccd8"></a>

**0° CCW: unverified** — `in_game_visible_travel-f24b3c46bb096a4dccd8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-21>1-W-out-12; entry: 1-S-in-21; exit: 1-W-out-12.

No observation recorded.

<a id="case-in_game_visible_travel-c2165593f58bf7a5590b"></a>

**90° CCW: unverified** — `in_game_visible_travel-c2165593f58bf7a5590b`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-21>1-W-out-12; entry: 1-S-in-21; exit: 1-W-out-12.

No observation recorded.

<a id="case-in_game_visible_travel-6cf2c8fb98ca18f49d8e"></a>

**180° CCW: unverified** — `in_game_visible_travel-6cf2c8fb98ca18f49d8e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-21>1-W-out-12; entry: 1-S-in-21; exit: 1-W-out-12.

No observation recorded.

<a id="case-in_game_visible_travel-506994406fddf0804ec8"></a>

**270° CCW: unverified** — `in_game_visible_travel-506994406fddf0804ec8`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-21>1-W-out-12; entry: 1-S-in-21; exit: 1-W-out-12.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-S-in-22>1-W-out-11; entry: 1-S-in-22; exit: 1-W-out-11</summary>

<a id="case-in_game_visible_travel-0dee53c7bf4056b2d052"></a>

**0° CCW: unverified** — `in_game_visible_travel-0dee53c7bf4056b2d052`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-22>1-W-out-11; entry: 1-S-in-22; exit: 1-W-out-11.

No observation recorded.

<a id="case-in_game_visible_travel-b427df4eb364d43c8acc"></a>

**90° CCW: unverified** — `in_game_visible_travel-b427df4eb364d43c8acc`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-22>1-W-out-11; entry: 1-S-in-22; exit: 1-W-out-11.

No observation recorded.

<a id="case-in_game_visible_travel-2223f1d05efd301b6e26"></a>

**180° CCW: unverified** — `in_game_visible_travel-2223f1d05efd301b6e26`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-22>1-W-out-11; entry: 1-S-in-22; exit: 1-W-out-11.

No observation recorded.

<a id="case-in_game_visible_travel-ad6db302422198f16993"></a>

**270° CCW: unverified** — `in_game_visible_travel-ad6db302422198f16993`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-22>1-W-out-11; entry: 1-S-in-22; exit: 1-W-out-11.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-S-in-22>1-W-out-12; entry: 1-S-in-22; exit: 1-W-out-12</summary>

<a id="case-in_game_visible_travel-7e4f77a1aefb8bfb2bbd"></a>

**0° CCW: unverified** — `in_game_visible_travel-7e4f77a1aefb8bfb2bbd`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-22>1-W-out-12; entry: 1-S-in-22; exit: 1-W-out-12.

No observation recorded.

<a id="case-in_game_visible_travel-8f7eef13e603e2da6889"></a>

**90° CCW: unverified** — `in_game_visible_travel-8f7eef13e603e2da6889`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-22>1-W-out-12; entry: 1-S-in-22; exit: 1-W-out-12.

No observation recorded.

<a id="case-in_game_visible_travel-35e7fba1f0bec65a068c"></a>

**180° CCW: unverified** — `in_game_visible_travel-35e7fba1f0bec65a068c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-22>1-W-out-12; entry: 1-S-in-22; exit: 1-W-out-12.

No observation recorded.

<a id="case-in_game_visible_travel-170e346beb2bc9deaff7"></a>

**270° CCW: unverified** — `in_game_visible_travel-170e346beb2bc9deaff7`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-S-in-22>1-W-out-12; entry: 1-S-in-22; exit: 1-W-out-12.

No observation recorded.

</details>


<details>
<summary>Visible travel — Service: road; role: primary; journey: 1:1-N-in-23>1-W-out-6; entry: 1-N-in-23; exit: 1-W-out-6</summary>

<a id="case-in_game_visible_travel-26ab56d419535747438c"></a>

**0° CCW: unverified** — `in_game_visible_travel-26ab56d419535747438c`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-23>1-W-out-6; entry: 1-N-in-23; exit: 1-W-out-6.

No observation recorded.

<a id="case-in_game_visible_travel-9ce736dadda4958e8e2e"></a>

**90° CCW: unverified** — `in_game_visible_travel-9ce736dadda4958e8e2e`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-23>1-W-out-6; entry: 1-N-in-23; exit: 1-W-out-6.

No observation recorded.

<a id="case-in_game_visible_travel-9e941def5ab7df150aae"></a>

**180° CCW: unverified** — `in_game_visible_travel-9e941def5ab7df150aae`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-23>1-W-out-6; entry: 1-N-in-23; exit: 1-W-out-6.

No observation recorded.

<a id="case-in_game_visible_travel-e7f0d31d5353cc476ab9"></a>

**270° CCW: unverified** — `in_game_visible_travel-e7f0d31d5353cc476ab9`.

Observe traffic visibly complete this directed journey for its service network; Route Query alone does not complete this check.

Scope: Service: road; role: primary; journey: 1:1-N-in-23>1-W-out-6; entry: 1-N-in-23; exit: 1-W-out-6.

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
<summary>Forbidden transfer — road → road — 512 cases; unverified: 512</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 1-N-in-2; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f6847756a2fa9c13bd65">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e2a97532f12f46ef7dcb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-45a197a0a0688b71df58">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2bb7c91d5e89388b8eae">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-2; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-41b322a2a0e43ebfde6c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1fc147c7e7095a0e050e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fa2dd2dc94fdcc60f879">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a72ba20eab2d001b9e97">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-2; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f89d2c6507077e36fea9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f4e8259d6acbd800c552">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-586480dd7f0c7036c5c5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f863db45c083402bb946">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-2; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3555aaca060800cd0287">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-65685b9e8051cf162afc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-66ea3eb7e399c5ff8dc0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b8998cb800df2edadd69">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-2; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f5a1d2fe1315515dfc39">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-788ffcf427281e994923">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ee67bba374923fab2f4d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-988d8ecabd88359d2d2b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-2; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1ac01f2e355c4267c16b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a762da6f0606afa8a462">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a73cf79306fad2022840">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9d95ed182af17d7d7acc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-2; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1dcac3367d75d7d57d2c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c0c85475b63ee76ad94a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a3ce34f3302206d498bd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b8201adaec6814deec9e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-2; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e15a1af24d1d8e30df2c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bdabdfb010e0cc44ab7c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6ceed8c1a52de3e27f55">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1aefe58fdde8a6eefa33">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-2; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-61463ed8dc47c7a1f355">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d1a41f81d36a4759af70">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-45156e28cfb65fe387e0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2429c9af00bf50c55351">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-2; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e77bc300f5a11f70cb47">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-afbdb4c51c25d9390b25">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f9d55b4554095167c3b1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7cba1b54deea002411a0">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-2; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f66b9183ef9ffede310a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0bafc06a1bdcfc473b2f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-af0258236498b8275f10">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f766f06cf0dd1725beca">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-3; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6d23d346e61fe9b278ef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9625a44dda1f396d63b9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6c4e3df10009099eed3f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ce754c748226d05596e4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-3; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-57fde1be0b531e59ad87">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-67ffd56273bb220d6e58">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0560949fec570e4df3a1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a8832d83fdcc6fe8a42f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-3; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-44934c090c2e3b5bc5e0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-45e3fdf267ba9bf6cecf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9a7774e3d1d818eb418c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4cabfb590e1e583ba989">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-3; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-aa4615cf84387a99d01c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8450252c718f5499e464">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8da30acccff0403b4ce3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-625f5a53b58262fe2958">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-3; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3f05bd9fb23b916bdfca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e55d7656980090d86054">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-59ce564949880f47c4fd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-762bc74881f39aa3a579">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-3; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6424fec9960caa7051df">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eee5ed69715e373bdc36">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-edbedd061aec1f9fdb1b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fa8ec6f7c270cc1a7767">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-3; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6aae4378d1289afb296a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-691c62cc15a2d52d5b05">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-da89a1d1e86bba72d180">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d7de791c5ea38290b8d7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-3; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-aa4f160249ddf933c63a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6697e7a421eb4e830719">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-56e44243894ceb40f851">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-05e187d044444256d8f1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-3; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-57aedabce6ffe52aedc4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d323d0126526399765c0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1929e74debbd7778f706">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b05304823436c52f02af">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-3; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7e826ad245797dbe6505">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-17e448ee3fcd5b22027b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9f139c7900168bd910f0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-406af81ce891c5360999">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5df6bbeb24885f9472fd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d9c4e69a6564e9695776">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-37862f16c31d56b6840b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-330b6a53b5e63541701d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-4; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9c611860403759d09e2c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a66cfbb544033d54a135">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0c94f302b121a0ec2201">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-005b9dab1c31a0b12eb1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-4; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-402662a63ebd67670a54">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b01b6d5a900a6affdbcb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b3b35ddf97d141ba9928">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3a09c36876a9ce41431e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-4; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d5ffeb71e38bce8f3608">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a76bf72dd4242ed3d11d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b78c1b2a724812a7efbc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9dbc271ee625799a33bc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-4; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-13367eb9d8b9661f34f7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7dd875d5137fa6a97c46">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-266ada3f0ffb40b64469">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e5e990f013ed6f3c0920">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-4; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ec2d38e5fafda9bc07b0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aa7deca592d5cdca21e3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8668dae6d4e0b785678b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1406c82fde50067946c5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-4; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-637753f6d956acf25737">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-353a36375fa56c132e71">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-29aede3cd3ef033e6a54">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5b78c2a2654b84b95f67">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-4; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-36315888b99ef0213321">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f84052e967d80385c29a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a821c622e008ae043101">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-58452341571995940177">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-4; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-da7fc061e16f3242d71c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1d38f6ad58c31bdde0bd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-99704531f6e44e2a1610">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2f1c70e5af529c168c68">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-4; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1a84a8df2065c454f26e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-006fecf1be4835911f24">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-188006488e8393cd0200">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c467f3c7e35802c8c8f6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b78803e2da613030a212">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e7b0a61eaeb6b24b15d0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6ab578e803f6c3907688">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-22833099507f98025270">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e66d79c78a2610e6a876">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c370654cb47bbbfdcbc0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-07b719761a2c672c4c3d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4cf91edf48aa26399f82">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-80c68d0b63c159c0586c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0c43e1960640a60ecb54">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e2905a82e2ef53ed297a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fa57aa7ccb1ff422d0a3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f088742efbe3c8a13ac6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-963a0fcdd4b6b9cc6b09">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a698ffcbf8ad688b9895">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-73ce1ab4010c2a2601fb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3f22dd028eaadc3b2706">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d5e32107e949658d6c80">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bff5042db07e3dc552fc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ea876f298d931ce012bc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-eb68137b67dfa2a0aabf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-76b691c68b76e7d8ba9b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d4cc5169ae73c5bb59ef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bf2d75ea705c8797e12e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-fba2859d40524b87bd11">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d649da041044b52f6445">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dd3bf180866537a7a972">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d1896d0a8a31e525c5ca">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9e6e9406fde56a61af56">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-680150681b842f24a4fe">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1b6f60a4924c0a436473">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-770a9018e1d79a913282">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4de0bb08cd7b948f4441">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-231c71dda0296efe6f66">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4ab007b7776bf0165b69">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0e016ea2b7aba9c06a07">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6a5d6951ae9b82d56a46">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e7220274b3f289911e76">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-77c943856561e437fb95">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a10f5205c4250042dfd8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3b06094cc08247c0fc2c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a974c277ca7d40527017">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7b6dc3d599a471a087a7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-002b1736749e32136cb8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-7; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1fe426546670021d6f56">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-488525b074a713554e01">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7a230bf7ecf39e4422d4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b2a0090b6f6c29d05278">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-7; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f7ace8eba26c781e21b9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ec910433025b6b063c07">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1957c7125d7be608a367">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-07654cc1ca6d2bbaea7d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-7; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e4232eb76312231f9d2a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fa86099a66cb8aec0cce">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b5ef589f59597343b6d7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7a29f84e4c770407290f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-7; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cbfc276862a7ff8cdcbb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8f94048ba5168501c7d0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3f4d9be705d72f85acf3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0113d73b641b1aae251e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-7; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-93097e5b37d1449fa661">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-01f2aafcec650784a009">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c8e0cc3c6a2021eed46e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-31d491e5aa783011b3a3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-7; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-374b2e4404f849b56600">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-954ab371201d87c5be1c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7f055a7f4d3f087e00ee">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-888a88bb1c112058b75c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-7; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-977a5407186209cbb585">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a47ce57abbdd48ad51d5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-85fba8d7efdb08bb601a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1bce664e4ae094484a7d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-7; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5a0b4fc148043ec95bab">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-94d62b9b04e37ea9e3ac">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3557a01d1f1913f88e38">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7833a7551182298d82e4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-7; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-dbab6f7b6f889a73aeb2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a2f55401febb43f1d3c6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9e0a6e7ec3c49c7841ee">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-389303cca5c62f2c5a5d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-7; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e6f331d32dba7f09da06">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-714254aeff706de0c919">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-02e1bb1db732f131d29e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a12f6ae93a3f959e5cbd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-7; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ba2f416db74fbe5fba6a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1dadfc7c9b4261e3994f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-287988250c7baf46d0bc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1722b0ccac836562e726">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-9; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-73884bae33e3da8fb732">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0ebed5a8776f8063ae1b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f29e27921c40e96e25a9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-64e1f3661d3fa88c0bfb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-9; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3ad819e46e4b6505355a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-481fa68a912fc43ef9ad">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ff77c46819f73751a934">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4fa1bb231073311f3778">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-9; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-129768e67bf056f29025">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6044d06bbd6737fdf6c3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ab57ad2b9dd66152a060">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e7bb631b093f5d4e0c05">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-9; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6c392a7e25fd6554ab16">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9533e1f384d1d15a4cb7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7b6c2648ea5b1c60481c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1ed0ddfff5cb294d2ae1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-9; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8f7ce7903fa9430e48a9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7358839a21c94e49cdb8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2dd17dd3dfb97dd215aa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ac1fed4dc6c439910146">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-9; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-930fb02953c361258bf2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-38bd9c275abcafa192d3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-71f732388b8da0e9cf9e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dff1c121b1aeca30ca08">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-9; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-02f253524843b7fa6ad0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-994a33638018d5ce10cf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9e321ac47d5b1ad3c7d5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ce24c501a54e270c2d33">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-9; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-092f6121ef74cd35b2d1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3e165d913f1eb28de801">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a44a3e01205c12549fa0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4802222a697e773d46c2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-9; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-50a106ad6d9515f377a6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-02e09bb24330e7fbb617">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f2515848c19d3f4aaaf9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-746e031e109715a01997">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-9; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f4273b6434f9b791098d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-85765c8bfba7b7eb127a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cac2f35df13eb1aa2337">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cb8f0fcab06563e8fd4b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-9; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-188ed620cefc57f79b36">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-19aa2a7a7aba91e42b5f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-78748be9972298fe9c17">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c0bc12ecf48bb17365dc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-14; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-35b834b158119328d51f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d078247304e6d0f715ca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b2660182c0ffaeb66961">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ba4a47ce835daee3802c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-14; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3f6188b6261fb1c0b992">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-03cab1edc97b2f77301c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d774288091a18ba99d65">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2749a3e61f030324c0a7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-14; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a9dfac4af90f915eaec2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6491f6e0087a3610722b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b9a85b7330dc99df38fc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7850f36849feb45d2098">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-14; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-87133044d07cf3edf968">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cf5df9df3aa6699ae3d1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1ac8d616c84d2157223a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-330c93035110bacd9dc6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-14; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9f69b4b8f1bf5509e853">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2108d6bebfd6536b8f24">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ebc661f9d7019b280d45">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8931351796ca68a9e02a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-14; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2fa0771ca7603575cd60">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-15a1c2242dd3d15db62b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-729209c03f852813378b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4c27ad86e5411cbc8801">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-14; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c311918a230d8b5666f9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-212ef8b1b9a8cfe7fff5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-612eac47ef418c23f164">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-63a615beb296eae487dc">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-14; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4fd5eed83d0000ca6ff1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-63607945cd371dd2fdf9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-35c34ca1cdc3a0aa41e8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-368514297e862bdef8cf">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-14; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-43fe8cf516dffff3a763">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f5d3d96bf6a2ba94b43e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1ecd993ed466c455a47f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-991e2e10b6703f1cae92">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-14; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1cfdc0f1e8caf1f4fa86">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e70ed9e259c154cb6b7c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-607c7f9dbb861d6cd6c9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-83be25c35308ab94219e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-14; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2579ecd51799eaa3c53d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-af7473f1883ec8b56d52">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cac39b779450dca31406">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c152ac05c9eb042b4255">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-18; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-7ccf2b3c26f25efed2d2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-124c5ebcaf56450a3f2a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-af6e16c120be16d4a877">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c517467b881aa4d8718e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-18; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-72e7e28b160ddd2463dd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-089126c626b742151a6d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ba7298038aef9f641e0f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fa083a8f551b9bbb3ae9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-18; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-97f5796f62104e4b396e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e54bb1b8ef7c5c6eb8e6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-331a0ec0d8b30777947f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3abadc6487c665176575">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-18; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0ae6b01d3b1ed6f28b49">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e9b548bb70b4d1c10dc3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-84bcf0fe8b43b575239a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8d2b00ceff77db7e5939">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-18; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-75344dfbd0277f272890">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a4883115e2929534eac2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6a9876c1c4aef5dde0f0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9f9c09c5b224a74b061f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-18; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cd8b0ed118ffceb398ca">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4247c13bc2eb97d08dc9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9342efe66ff986f6c91a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9ede9e4d47665ea4653d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-18; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-97a902651441db4aeaf4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-46d43b46dfcf3251f3fd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-82f0a9565de7ef76d462">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ee38e342dd5a17a035dd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-18; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-741418ddbebfe9681932">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1ad42e2ddc75e0e50bfc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1b2b2b92127c5722d939">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-890b159cf7af52358f5b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-18; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1a3083fc926fddf2718e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d1b2166661c10e38bde0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1428b24c7dcf01c14a62">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3b02cf72977a2428fe7a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-18; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-15d2a9b4a13219cda826">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0e60024c51d7b03c747c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ec7a57a081f5298857be">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2f644fd783bcf52fd99f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-18; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0efa7c4751656e085d6a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-49c2ca169546e54e2925">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5d9a456ceae375dd7e20">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0c7a41cdfa85aed8f60e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-19; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5a8dabfec4e82891e551">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a2b250aa2c772f0943cd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e340e76dd7404a2fe8f6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-03b28db1869802b21a5f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-19; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f4d10880167f8b281a6f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-200d139728531e66288f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fcfa03c7e354091ff32e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-edbdbab269da0303d5e9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-19; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-40be0108c6416bf7d640">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-47ff6ef19e8c6fca0978">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9332b1f1f1e480b927d8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-35bb01e54859e73f4a78">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-19; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-abdf5bb12f2f3aa50578">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3178c1656310adc72c87">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e08497c3dc86023c1790">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ea6403657a7c6f9fee6f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-19; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-23c0f702afd51dd727d7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-419aed5682fd093c8768">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5aa9e56567b04a8f4d72">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-07b82cde685adee45355">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-19; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4c5bfd54792cd6c504cd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b64495b0283621ee764a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c1ddc81fe874debcea6b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e368eb800a31483e978d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-19; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-91be209cc0b3666cd958">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-92aa8e4f6cb405f5b1dc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-238390079dec81c91c25">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a59605d2a79bfb716463">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-19; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-211e23475df83cfcfbe6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ba6569e4169fff4cb33e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4522a3c53421b60b638b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1842f24c5004b9f335eb">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-19; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6ec0aefb60c7c2a49a4d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c4a416e9bda2ad3cb437">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-812444d9733638fdfeed">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6757265a6a0bd676911b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-19; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ec7e6773141518fa143a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-973afe40aa9c17e96ef9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4c6847c8bbf7a9ae5b34">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1bbed8a31e3f936aeaa6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-19; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a2e1a4d338f3f6f0fb38">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9ffe0d01314061398a75">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-87f0a8d7149c5b46c820">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-67c1cbada0d32c730520">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-21; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f444f32cd96439045f9c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-91ae46afaf0e67caa1d6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e09f3a3e9e469e8d2ab4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ff5ef558ba6872bc5f75">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-21; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9f0c0262635504f558ec">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-141356360fb1174f51be">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-716a3d681a728780e732">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-393e76fc7dd3e7ee3523">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-21; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-425d29cd01c20329d361">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-39aebdc5864f62fef260">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-32b8be463aa2377f03aa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-78b9cf376411d2ecb939">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-21; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-56df90dc3d74e04d45b3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-783ce1b57879bcf51277">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d7a8bed81650490e16dd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6a512137426dbcea44a4">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-21; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-d61c3e5813187b10d58f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f1ded90a1ff021eaa383">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1e03052701ef71238dc8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dec15e5136633c40c1f7">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-21; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-35556091697dc3f7aa27">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-240b728d0528d941b1c3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f1c369c97e5c83a19c8b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aec59af143b3260e190f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-21; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-60fb70ffef1fe13bc596">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5c651b03f123d06c920b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6b052b8d550cad9ac1a8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-47b6c2e0a4edaf727629">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-21; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a21f43e5967d5c9b8c6b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f2cf2c9ea5c86799c940">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f634c7ad37de89b5d3e2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ad2de76d4cf2704f751f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-21; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-64dee723d8a6b37980cd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c4612780a03d75e690dd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1df07684377c75e162cd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-34057bed4ed67121155f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-21; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e091f6243421512cd429">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3b6dd9bd7f163ab3187d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-000285bf3a47735474c3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b0a984a0d89773e89c4c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-22; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5c0d2d683fd048863385">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-827356e538efe8371dc8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-717a5d53a7274122f6a3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-71010554a3b9ed7c53d5">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-22; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-22e4538a80ab7ac1567b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b0b6ed43d64152685842">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c64375005f7d1e610d73">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d0fa34eacc1c2cfd07e9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-22; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ee0cc61fd90961b74530">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5f99fff760eb31b75b6c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-859f493b3136a81abf62">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-48cf722639a21b46c101">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-22; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b98ae1e805ca24992a87">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bea4f2c251d04beeb5e6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6c9ea4c168a489467a15">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8dec386cf8d1e8ce0767">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-22; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-c797f672d479fc19274a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-de9855a85eac7ff442ff">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e1f1f9c4f7ac050ca310">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6904b60af424c1e753a3">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-22; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-db54eb6eef2d3d8deff1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b3b14782dc4f6889bff5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c6a28a3e57b54631f773">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-39a2bc32140d0bdfb098">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-22; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-73b598d9799942e99a96">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-feb0646c93008c3999f5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-372eb5ae45a39a03f79c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fb138a719394c000bd18">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-22; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cae630ac32324d977c92">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-54ff4c7281129b9beea6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9549a7d19c3609436097">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6a02c531bd835b8a4af6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-22; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-79339744e01d8c24be6a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0445492cfa8cd318568b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e4e86212fafce0c21a8e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-badc06ac36430a067e50">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-22; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b18d3deaaeb33542a130">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bc92d2fa4bb7d06f3125">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3b20456682e141138888">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c54a32f4f99dcaaf2783">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-23; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a600d68d9d1554464198">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-535bab940f6f4138e5fa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d144d5071001adc8bfe5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-65a5ecb215d5cbd69816">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-23; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b145c015ed98eef81092">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-361d4eea27dea6a9b9fa">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2de2c508685dfbb6c751">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5b90adb650166b7321d6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-23; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5b30d96bc0da0c85cd95">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2e135463480a373e7372">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-964c03d9329221e6c19e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-30330d00dc1ece9a2538">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-23; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6978a7932ef860eb82e4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-410e5f9c7ebe8d076a5f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b43d40f17d7df1e9fdbb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fd6e828e7794176eb4ca">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-23; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-cc1c5cdc69221e299dc1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2eb20b8145037ad97d60">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-68c3333d38aff4ea743e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8d2f6102a4e0dfb7cd51">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-23; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3f6598c1860f9c6d07cf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1da03699357ba3fd49de">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c249c0296e95e27a4ef6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cd6bae7208850090931f">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-23; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-f509f6807ba07bd67c9f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6cf56d09db6c86a3c2c6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-71aeac46fdd392ac2494">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0606403842b10b481307">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-23; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ca949da2a9096bd08aea">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-20b811c116418a98e27d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b5223ed03b42c1e55937">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-712ea6a59d1420b5c566">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-23; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-9e3a339aebdee6216d33">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d0718d7495f6f301d116">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d10b50b87633a1c419b7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f70bf8ea345937726b06">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-23; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-452c6ff24155024a4136">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-077781144ea9e3204bd3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5c7d5b5503bb2d40424e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-585eea77b0ad908f8a36">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-23; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2c7d64752d34cd2c52a0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-79a3d85faaad943a1412">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e924abc6896e4f9a512e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8f9a2e25004e3c0d4e01">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: 1-N-in-2; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f6847756a2fa9c13bd65"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f6847756a2fa9c13bd65`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e2a97532f12f46ef7dcb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e2a97532f12f46ef7dcb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-45a197a0a0688b71df58"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-45a197a0a0688b71df58`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2bb7c91d5e89388b8eae"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2bb7c91d5e89388b8eae`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

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
<summary>Forbidden transfer — from port: 1-N-in-2; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f89d2c6507077e36fea9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f89d2c6507077e36fea9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f4e8259d6acbd800c552"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f4e8259d6acbd800c552`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-586480dd7f0c7036c5c5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-586480dd7f0c7036c5c5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f863db45c083402bb946"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f863db45c083402bb946`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-2; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3555aaca060800cd0287"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3555aaca060800cd0287`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-65685b9e8051cf162afc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-65685b9e8051cf162afc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-66ea3eb7e399c5ff8dc0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-66ea3eb7e399c5ff8dc0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b8998cb800df2edadd69"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b8998cb800df2edadd69`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-2; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f5a1d2fe1315515dfc39"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f5a1d2fe1315515dfc39`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-788ffcf427281e994923"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-788ffcf427281e994923`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ee67bba374923fab2f4d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ee67bba374923fab2f4d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-988d8ecabd88359d2d2b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-988d8ecabd88359d2d2b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-2; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1ac01f2e355c4267c16b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1ac01f2e355c4267c16b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a762da6f0606afa8a462"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a762da6f0606afa8a462`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a73cf79306fad2022840"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a73cf79306fad2022840`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9d95ed182af17d7d7acc"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9d95ed182af17d7d7acc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-2; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1dcac3367d75d7d57d2c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1dcac3367d75d7d57d2c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c0c85475b63ee76ad94a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c0c85475b63ee76ad94a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a3ce34f3302206d498bd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a3ce34f3302206d498bd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b8201adaec6814deec9e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b8201adaec6814deec9e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-2; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e15a1af24d1d8e30df2c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e15a1af24d1d8e30df2c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bdabdfb010e0cc44ab7c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bdabdfb010e0cc44ab7c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6ceed8c1a52de3e27f55"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6ceed8c1a52de3e27f55`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1aefe58fdde8a6eefa33"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1aefe58fdde8a6eefa33`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-2; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-61463ed8dc47c7a1f355"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-61463ed8dc47c7a1f355`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d1a41f81d36a4759af70"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d1a41f81d36a4759af70`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-45156e28cfb65fe387e0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-45156e28cfb65fe387e0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2429c9af00bf50c55351"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2429c9af00bf50c55351`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-2; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e77bc300f5a11f70cb47"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e77bc300f5a11f70cb47`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-afbdb4c51c25d9390b25"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-afbdb4c51c25d9390b25`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f9d55b4554095167c3b1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f9d55b4554095167c3b1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7cba1b54deea002411a0"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7cba1b54deea002411a0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-2; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f66b9183ef9ffede310a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f66b9183ef9ffede310a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0bafc06a1bdcfc473b2f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0bafc06a1bdcfc473b2f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-af0258236498b8275f10"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-af0258236498b8275f10`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f766f06cf0dd1725beca"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f766f06cf0dd1725beca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-2; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-3; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6d23d346e61fe9b278ef"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6d23d346e61fe9b278ef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9625a44dda1f396d63b9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9625a44dda1f396d63b9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6c4e3df10009099eed3f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6c4e3df10009099eed3f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ce754c748226d05596e4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ce754c748226d05596e4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-3; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-57fde1be0b531e59ad87"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-57fde1be0b531e59ad87`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-67ffd56273bb220d6e58"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-67ffd56273bb220d6e58`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0560949fec570e4df3a1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0560949fec570e4df3a1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a8832d83fdcc6fe8a42f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a8832d83fdcc6fe8a42f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-3; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-44934c090c2e3b5bc5e0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-44934c090c2e3b5bc5e0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-45e3fdf267ba9bf6cecf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-45e3fdf267ba9bf6cecf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9a7774e3d1d818eb418c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9a7774e3d1d818eb418c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4cabfb590e1e583ba989"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4cabfb590e1e583ba989`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-3; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-aa4615cf84387a99d01c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-aa4615cf84387a99d01c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8450252c718f5499e464"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8450252c718f5499e464`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8da30acccff0403b4ce3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8da30acccff0403b4ce3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-625f5a53b58262fe2958"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-625f5a53b58262fe2958`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-3; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3f05bd9fb23b916bdfca"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3f05bd9fb23b916bdfca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e55d7656980090d86054"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e55d7656980090d86054`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-59ce564949880f47c4fd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-59ce564949880f47c4fd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-762bc74881f39aa3a579"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-762bc74881f39aa3a579`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-3; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6424fec9960caa7051df"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6424fec9960caa7051df`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eee5ed69715e373bdc36"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-eee5ed69715e373bdc36`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-edbedd061aec1f9fdb1b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-edbedd061aec1f9fdb1b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fa8ec6f7c270cc1a7767"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fa8ec6f7c270cc1a7767`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-3; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6aae4378d1289afb296a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6aae4378d1289afb296a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-691c62cc15a2d52d5b05"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-691c62cc15a2d52d5b05`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-da89a1d1e86bba72d180"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-da89a1d1e86bba72d180`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d7de791c5ea38290b8d7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d7de791c5ea38290b8d7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-3; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-aa4f160249ddf933c63a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-aa4f160249ddf933c63a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6697e7a421eb4e830719"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6697e7a421eb4e830719`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-56e44243894ceb40f851"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-56e44243894ceb40f851`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-05e187d044444256d8f1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-05e187d044444256d8f1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-3; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-57aedabce6ffe52aedc4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-57aedabce6ffe52aedc4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d323d0126526399765c0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d323d0126526399765c0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1929e74debbd7778f706"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1929e74debbd7778f706`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b05304823436c52f02af"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b05304823436c52f02af`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-3; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7e826ad245797dbe6505"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7e826ad245797dbe6505`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-17e448ee3fcd5b22027b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-17e448ee3fcd5b22027b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9f139c7900168bd910f0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9f139c7900168bd910f0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-406af81ce891c5360999"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-406af81ce891c5360999`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5df6bbeb24885f9472fd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5df6bbeb24885f9472fd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d9c4e69a6564e9695776"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d9c4e69a6564e9695776`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-37862f16c31d56b6840b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-37862f16c31d56b6840b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-330b6a53b5e63541701d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-330b6a53b5e63541701d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-4; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9c611860403759d09e2c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9c611860403759d09e2c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a66cfbb544033d54a135"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a66cfbb544033d54a135`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0c94f302b121a0ec2201"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0c94f302b121a0ec2201`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-005b9dab1c31a0b12eb1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-005b9dab1c31a0b12eb1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-4; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-402662a63ebd67670a54"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-402662a63ebd67670a54`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b01b6d5a900a6affdbcb"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b01b6d5a900a6affdbcb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b3b35ddf97d141ba9928"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b3b35ddf97d141ba9928`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3a09c36876a9ce41431e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3a09c36876a9ce41431e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-4; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d5ffeb71e38bce8f3608"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d5ffeb71e38bce8f3608`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a76bf72dd4242ed3d11d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a76bf72dd4242ed3d11d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b78c1b2a724812a7efbc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b78c1b2a724812a7efbc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9dbc271ee625799a33bc"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9dbc271ee625799a33bc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-4; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-13367eb9d8b9661f34f7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-13367eb9d8b9661f34f7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7dd875d5137fa6a97c46"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7dd875d5137fa6a97c46`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-266ada3f0ffb40b64469"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-266ada3f0ffb40b64469`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e5e990f013ed6f3c0920"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e5e990f013ed6f3c0920`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-4; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ec2d38e5fafda9bc07b0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ec2d38e5fafda9bc07b0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aa7deca592d5cdca21e3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-aa7deca592d5cdca21e3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8668dae6d4e0b785678b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8668dae6d4e0b785678b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1406c82fde50067946c5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1406c82fde50067946c5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-4; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-637753f6d956acf25737"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-637753f6d956acf25737`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-353a36375fa56c132e71"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-353a36375fa56c132e71`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-29aede3cd3ef033e6a54"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-29aede3cd3ef033e6a54`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5b78c2a2654b84b95f67"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5b78c2a2654b84b95f67`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-4; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-36315888b99ef0213321"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-36315888b99ef0213321`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f84052e967d80385c29a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f84052e967d80385c29a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a821c622e008ae043101"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a821c622e008ae043101`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-58452341571995940177"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-58452341571995940177`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-4; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-da7fc061e16f3242d71c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-da7fc061e16f3242d71c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1d38f6ad58c31bdde0bd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1d38f6ad58c31bdde0bd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-99704531f6e44e2a1610"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-99704531f6e44e2a1610`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2f1c70e5af529c168c68"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2f1c70e5af529c168c68`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-4; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1a84a8df2065c454f26e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1a84a8df2065c454f26e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-006fecf1be4835911f24"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-006fecf1be4835911f24`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-188006488e8393cd0200"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-188006488e8393cd0200`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c467f3c7e35802c8c8f6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c467f3c7e35802c8c8f6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b78803e2da613030a212"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b78803e2da613030a212`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e7b0a61eaeb6b24b15d0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e7b0a61eaeb6b24b15d0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6ab578e803f6c3907688"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6ab578e803f6c3907688`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-22833099507f98025270"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-22833099507f98025270`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e66d79c78a2610e6a876"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e66d79c78a2610e6a876`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c370654cb47bbbfdcbc0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c370654cb47bbbfdcbc0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-07b719761a2c672c4c3d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-07b719761a2c672c4c3d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4cf91edf48aa26399f82"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4cf91edf48aa26399f82`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-80c68d0b63c159c0586c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-80c68d0b63c159c0586c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0c43e1960640a60ecb54"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0c43e1960640a60ecb54`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e2905a82e2ef53ed297a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e2905a82e2ef53ed297a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fa57aa7ccb1ff422d0a3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fa57aa7ccb1ff422d0a3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f088742efbe3c8a13ac6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f088742efbe3c8a13ac6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-963a0fcdd4b6b9cc6b09"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-963a0fcdd4b6b9cc6b09`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a698ffcbf8ad688b9895"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a698ffcbf8ad688b9895`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-73ce1ab4010c2a2601fb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-73ce1ab4010c2a2601fb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3f22dd028eaadc3b2706"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3f22dd028eaadc3b2706`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d5e32107e949658d6c80"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d5e32107e949658d6c80`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bff5042db07e3dc552fc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bff5042db07e3dc552fc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ea876f298d931ce012bc"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ea876f298d931ce012bc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-eb68137b67dfa2a0aabf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-eb68137b67dfa2a0aabf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-76b691c68b76e7d8ba9b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-76b691c68b76e7d8ba9b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d4cc5169ae73c5bb59ef"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d4cc5169ae73c5bb59ef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bf2d75ea705c8797e12e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bf2d75ea705c8797e12e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-fba2859d40524b87bd11"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-fba2859d40524b87bd11`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d649da041044b52f6445"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d649da041044b52f6445`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dd3bf180866537a7a972"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-dd3bf180866537a7a972`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d1896d0a8a31e525c5ca"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d1896d0a8a31e525c5ca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9e6e9406fde56a61af56"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9e6e9406fde56a61af56`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-680150681b842f24a4fe"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-680150681b842f24a4fe`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1b6f60a4924c0a436473"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1b6f60a4924c0a436473`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-770a9018e1d79a913282"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-770a9018e1d79a913282`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4de0bb08cd7b948f4441"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4de0bb08cd7b948f4441`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-231c71dda0296efe6f66"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-231c71dda0296efe6f66`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4ab007b7776bf0165b69"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4ab007b7776bf0165b69`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0e016ea2b7aba9c06a07"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0e016ea2b7aba9c06a07`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6a5d6951ae9b82d56a46"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6a5d6951ae9b82d56a46`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e7220274b3f289911e76"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e7220274b3f289911e76`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-77c943856561e437fb95"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-77c943856561e437fb95`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a10f5205c4250042dfd8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a10f5205c4250042dfd8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3b06094cc08247c0fc2c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3b06094cc08247c0fc2c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a974c277ca7d40527017"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a974c277ca7d40527017`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7b6dc3d599a471a087a7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7b6dc3d599a471a087a7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-002b1736749e32136cb8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-002b1736749e32136cb8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-7; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1fe426546670021d6f56"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1fe426546670021d6f56`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-488525b074a713554e01"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-488525b074a713554e01`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7a230bf7ecf39e4422d4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7a230bf7ecf39e4422d4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b2a0090b6f6c29d05278"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b2a0090b6f6c29d05278`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-7; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f7ace8eba26c781e21b9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f7ace8eba26c781e21b9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ec910433025b6b063c07"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ec910433025b6b063c07`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1957c7125d7be608a367"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1957c7125d7be608a367`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-07654cc1ca6d2bbaea7d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-07654cc1ca6d2bbaea7d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-7; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e4232eb76312231f9d2a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e4232eb76312231f9d2a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fa86099a66cb8aec0cce"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-fa86099a66cb8aec0cce`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b5ef589f59597343b6d7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b5ef589f59597343b6d7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7a29f84e4c770407290f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7a29f84e4c770407290f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-7; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cbfc276862a7ff8cdcbb"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cbfc276862a7ff8cdcbb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8f94048ba5168501c7d0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-8f94048ba5168501c7d0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3f4d9be705d72f85acf3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3f4d9be705d72f85acf3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0113d73b641b1aae251e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0113d73b641b1aae251e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-7; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-93097e5b37d1449fa661"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-93097e5b37d1449fa661`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-01f2aafcec650784a009"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-01f2aafcec650784a009`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c8e0cc3c6a2021eed46e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c8e0cc3c6a2021eed46e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-31d491e5aa783011b3a3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-31d491e5aa783011b3a3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-7; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-374b2e4404f849b56600"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-374b2e4404f849b56600`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-954ab371201d87c5be1c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-954ab371201d87c5be1c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7f055a7f4d3f087e00ee"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7f055a7f4d3f087e00ee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-888a88bb1c112058b75c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-888a88bb1c112058b75c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-7; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-977a5407186209cbb585"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-977a5407186209cbb585`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a47ce57abbdd48ad51d5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a47ce57abbdd48ad51d5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-85fba8d7efdb08bb601a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-85fba8d7efdb08bb601a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1bce664e4ae094484a7d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1bce664e4ae094484a7d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-7; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5a0b4fc148043ec95bab"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5a0b4fc148043ec95bab`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-94d62b9b04e37ea9e3ac"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-94d62b9b04e37ea9e3ac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3557a01d1f1913f88e38"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3557a01d1f1913f88e38`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7833a7551182298d82e4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7833a7551182298d82e4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-7; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-dbab6f7b6f889a73aeb2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-dbab6f7b6f889a73aeb2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a2f55401febb43f1d3c6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a2f55401febb43f1d3c6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9e0a6e7ec3c49c7841ee"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9e0a6e7ec3c49c7841ee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-389303cca5c62f2c5a5d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-389303cca5c62f2c5a5d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-7; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e6f331d32dba7f09da06"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e6f331d32dba7f09da06`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-714254aeff706de0c919"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-714254aeff706de0c919`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-02e1bb1db732f131d29e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-02e1bb1db732f131d29e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a12f6ae93a3f959e5cbd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a12f6ae93a3f959e5cbd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-7; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ba2f416db74fbe5fba6a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ba2f416db74fbe5fba6a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1dadfc7c9b4261e3994f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1dadfc7c9b4261e3994f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-287988250c7baf46d0bc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-287988250c7baf46d0bc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1722b0ccac836562e726"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1722b0ccac836562e726`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-9; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-73884bae33e3da8fb732"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-73884bae33e3da8fb732`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0ebed5a8776f8063ae1b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0ebed5a8776f8063ae1b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f29e27921c40e96e25a9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f29e27921c40e96e25a9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-64e1f3661d3fa88c0bfb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-64e1f3661d3fa88c0bfb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-9; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3ad819e46e4b6505355a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3ad819e46e4b6505355a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-481fa68a912fc43ef9ad"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-481fa68a912fc43ef9ad`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ff77c46819f73751a934"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ff77c46819f73751a934`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4fa1bb231073311f3778"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4fa1bb231073311f3778`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-9; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-129768e67bf056f29025"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-129768e67bf056f29025`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6044d06bbd6737fdf6c3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6044d06bbd6737fdf6c3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ab57ad2b9dd66152a060"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ab57ad2b9dd66152a060`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e7bb631b093f5d4e0c05"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e7bb631b093f5d4e0c05`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-9; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6c392a7e25fd6554ab16"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6c392a7e25fd6554ab16`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9533e1f384d1d15a4cb7"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9533e1f384d1d15a4cb7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7b6c2648ea5b1c60481c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7b6c2648ea5b1c60481c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1ed0ddfff5cb294d2ae1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1ed0ddfff5cb294d2ae1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-9; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8f7ce7903fa9430e48a9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8f7ce7903fa9430e48a9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7358839a21c94e49cdb8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7358839a21c94e49cdb8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2dd17dd3dfb97dd215aa"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2dd17dd3dfb97dd215aa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ac1fed4dc6c439910146"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ac1fed4dc6c439910146`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-9; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-930fb02953c361258bf2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-930fb02953c361258bf2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-38bd9c275abcafa192d3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-38bd9c275abcafa192d3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-71f732388b8da0e9cf9e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-71f732388b8da0e9cf9e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dff1c121b1aeca30ca08"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dff1c121b1aeca30ca08`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-9; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-02f253524843b7fa6ad0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-02f253524843b7fa6ad0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-994a33638018d5ce10cf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-994a33638018d5ce10cf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9e321ac47d5b1ad3c7d5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9e321ac47d5b1ad3c7d5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ce24c501a54e270c2d33"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ce24c501a54e270c2d33`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-9; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-092f6121ef74cd35b2d1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-092f6121ef74cd35b2d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3e165d913f1eb28de801"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3e165d913f1eb28de801`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a44a3e01205c12549fa0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-a44a3e01205c12549fa0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4802222a697e773d46c2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4802222a697e773d46c2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-9; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-50a106ad6d9515f377a6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-50a106ad6d9515f377a6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-02e09bb24330e7fbb617"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-02e09bb24330e7fbb617`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f2515848c19d3f4aaaf9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f2515848c19d3f4aaaf9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-746e031e109715a01997"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-746e031e109715a01997`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-9; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f4273b6434f9b791098d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f4273b6434f9b791098d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-85765c8bfba7b7eb127a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-85765c8bfba7b7eb127a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cac2f35df13eb1aa2337"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cac2f35df13eb1aa2337`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cb8f0fcab06563e8fd4b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cb8f0fcab06563e8fd4b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-9; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-188ed620cefc57f79b36"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-188ed620cefc57f79b36`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-19aa2a7a7aba91e42b5f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-19aa2a7a7aba91e42b5f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-78748be9972298fe9c17"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-78748be9972298fe9c17`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c0bc12ecf48bb17365dc"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c0bc12ecf48bb17365dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-14; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-35b834b158119328d51f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-35b834b158119328d51f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d078247304e6d0f715ca"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d078247304e6d0f715ca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b2660182c0ffaeb66961"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b2660182c0ffaeb66961`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ba4a47ce835daee3802c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ba4a47ce835daee3802c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-14; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3f6188b6261fb1c0b992"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3f6188b6261fb1c0b992`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-03cab1edc97b2f77301c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-03cab1edc97b2f77301c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d774288091a18ba99d65"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d774288091a18ba99d65`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2749a3e61f030324c0a7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2749a3e61f030324c0a7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-14; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a9dfac4af90f915eaec2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a9dfac4af90f915eaec2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6491f6e0087a3610722b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6491f6e0087a3610722b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b9a85b7330dc99df38fc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b9a85b7330dc99df38fc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7850f36849feb45d2098"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-7850f36849feb45d2098`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-14; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-87133044d07cf3edf968"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-87133044d07cf3edf968`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cf5df9df3aa6699ae3d1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cf5df9df3aa6699ae3d1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1ac8d616c84d2157223a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1ac8d616c84d2157223a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-330c93035110bacd9dc6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-330c93035110bacd9dc6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-14; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9f69b4b8f1bf5509e853"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9f69b4b8f1bf5509e853`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2108d6bebfd6536b8f24"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2108d6bebfd6536b8f24`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ebc661f9d7019b280d45"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ebc661f9d7019b280d45`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8931351796ca68a9e02a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8931351796ca68a9e02a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-14; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2fa0771ca7603575cd60"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2fa0771ca7603575cd60`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-15a1c2242dd3d15db62b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-15a1c2242dd3d15db62b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-729209c03f852813378b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-729209c03f852813378b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4c27ad86e5411cbc8801"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4c27ad86e5411cbc8801`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-14; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c311918a230d8b5666f9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c311918a230d8b5666f9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-212ef8b1b9a8cfe7fff5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-212ef8b1b9a8cfe7fff5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-612eac47ef418c23f164"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-612eac47ef418c23f164`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-63a615beb296eae487dc"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-63a615beb296eae487dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-14; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4fd5eed83d0000ca6ff1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4fd5eed83d0000ca6ff1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-63607945cd371dd2fdf9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-63607945cd371dd2fdf9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-35c34ca1cdc3a0aa41e8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-35c34ca1cdc3a0aa41e8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-368514297e862bdef8cf"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-368514297e862bdef8cf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-14; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-43fe8cf516dffff3a763"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-43fe8cf516dffff3a763`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f5d3d96bf6a2ba94b43e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f5d3d96bf6a2ba94b43e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1ecd993ed466c455a47f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1ecd993ed466c455a47f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-991e2e10b6703f1cae92"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-991e2e10b6703f1cae92`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-14; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1cfdc0f1e8caf1f4fa86"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1cfdc0f1e8caf1f4fa86`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e70ed9e259c154cb6b7c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e70ed9e259c154cb6b7c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-607c7f9dbb861d6cd6c9"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-607c7f9dbb861d6cd6c9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-83be25c35308ab94219e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-83be25c35308ab94219e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-14; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2579ecd51799eaa3c53d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2579ecd51799eaa3c53d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-af7473f1883ec8b56d52"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-af7473f1883ec8b56d52`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cac39b779450dca31406"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-cac39b779450dca31406`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c152ac05c9eb042b4255"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c152ac05c9eb042b4255`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-18; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-7ccf2b3c26f25efed2d2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-7ccf2b3c26f25efed2d2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-124c5ebcaf56450a3f2a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-124c5ebcaf56450a3f2a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-af6e16c120be16d4a877"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-af6e16c120be16d4a877`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c517467b881aa4d8718e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c517467b881aa4d8718e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-18; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-72e7e28b160ddd2463dd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-72e7e28b160ddd2463dd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-089126c626b742151a6d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-089126c626b742151a6d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ba7298038aef9f641e0f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ba7298038aef9f641e0f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fa083a8f551b9bbb3ae9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fa083a8f551b9bbb3ae9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-18; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-97f5796f62104e4b396e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-97f5796f62104e4b396e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e54bb1b8ef7c5c6eb8e6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e54bb1b8ef7c5c6eb8e6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-331a0ec0d8b30777947f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-331a0ec0d8b30777947f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3abadc6487c665176575"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3abadc6487c665176575`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-18; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0ae6b01d3b1ed6f28b49"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0ae6b01d3b1ed6f28b49`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e9b548bb70b4d1c10dc3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e9b548bb70b4d1c10dc3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-84bcf0fe8b43b575239a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-84bcf0fe8b43b575239a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8d2b00ceff77db7e5939"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8d2b00ceff77db7e5939`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-18; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-75344dfbd0277f272890"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-75344dfbd0277f272890`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a4883115e2929534eac2"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a4883115e2929534eac2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6a9876c1c4aef5dde0f0"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6a9876c1c4aef5dde0f0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9f9c09c5b224a74b061f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9f9c09c5b224a74b061f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-18; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cd8b0ed118ffceb398ca"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cd8b0ed118ffceb398ca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4247c13bc2eb97d08dc9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4247c13bc2eb97d08dc9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9342efe66ff986f6c91a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9342efe66ff986f6c91a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9ede9e4d47665ea4653d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9ede9e4d47665ea4653d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-18; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-97a902651441db4aeaf4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-97a902651441db4aeaf4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-46d43b46dfcf3251f3fd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-46d43b46dfcf3251f3fd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-82f0a9565de7ef76d462"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-82f0a9565de7ef76d462`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ee38e342dd5a17a035dd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ee38e342dd5a17a035dd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-18; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-741418ddbebfe9681932"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-741418ddbebfe9681932`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1ad42e2ddc75e0e50bfc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1ad42e2ddc75e0e50bfc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1b2b2b92127c5722d939"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1b2b2b92127c5722d939`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-890b159cf7af52358f5b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-890b159cf7af52358f5b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-18; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1a3083fc926fddf2718e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1a3083fc926fddf2718e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d1b2166661c10e38bde0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d1b2166661c10e38bde0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1428b24c7dcf01c14a62"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1428b24c7dcf01c14a62`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3b02cf72977a2428fe7a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-3b02cf72977a2428fe7a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-18; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-15d2a9b4a13219cda826"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-15d2a9b4a13219cda826`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0e60024c51d7b03c747c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0e60024c51d7b03c747c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ec7a57a081f5298857be"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ec7a57a081f5298857be`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2f644fd783bcf52fd99f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2f644fd783bcf52fd99f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-18; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0efa7c4751656e085d6a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0efa7c4751656e085d6a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-49c2ca169546e54e2925"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-49c2ca169546e54e2925`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5d9a456ceae375dd7e20"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5d9a456ceae375dd7e20`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0c7a41cdfa85aed8f60e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0c7a41cdfa85aed8f60e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-19; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5a8dabfec4e82891e551"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5a8dabfec4e82891e551`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a2b250aa2c772f0943cd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-a2b250aa2c772f0943cd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e340e76dd7404a2fe8f6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e340e76dd7404a2fe8f6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-03b28db1869802b21a5f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-03b28db1869802b21a5f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-19; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f4d10880167f8b281a6f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f4d10880167f8b281a6f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-200d139728531e66288f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-200d139728531e66288f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fcfa03c7e354091ff32e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fcfa03c7e354091ff32e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-edbdbab269da0303d5e9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-edbdbab269da0303d5e9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-19; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-40be0108c6416bf7d640"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-40be0108c6416bf7d640`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-47ff6ef19e8c6fca0978"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-47ff6ef19e8c6fca0978`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9332b1f1f1e480b927d8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9332b1f1f1e480b927d8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-35bb01e54859e73f4a78"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-35bb01e54859e73f4a78`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-19; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-abdf5bb12f2f3aa50578"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-abdf5bb12f2f3aa50578`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3178c1656310adc72c87"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3178c1656310adc72c87`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e08497c3dc86023c1790"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e08497c3dc86023c1790`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ea6403657a7c6f9fee6f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ea6403657a7c6f9fee6f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-19; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-23c0f702afd51dd727d7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-23c0f702afd51dd727d7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-419aed5682fd093c8768"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-419aed5682fd093c8768`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5aa9e56567b04a8f4d72"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5aa9e56567b04a8f4d72`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-07b82cde685adee45355"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-07b82cde685adee45355`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-19; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4c5bfd54792cd6c504cd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4c5bfd54792cd6c504cd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b64495b0283621ee764a"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b64495b0283621ee764a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c1ddc81fe874debcea6b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c1ddc81fe874debcea6b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e368eb800a31483e978d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e368eb800a31483e978d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-19; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-91be209cc0b3666cd958"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-91be209cc0b3666cd958`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-92aa8e4f6cb405f5b1dc"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-92aa8e4f6cb405f5b1dc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-238390079dec81c91c25"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-238390079dec81c91c25`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a59605d2a79bfb716463"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a59605d2a79bfb716463`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-19; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-211e23475df83cfcfbe6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-211e23475df83cfcfbe6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ba6569e4169fff4cb33e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-ba6569e4169fff4cb33e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4522a3c53421b60b638b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4522a3c53421b60b638b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1842f24c5004b9f335eb"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1842f24c5004b9f335eb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-19; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6ec0aefb60c7c2a49a4d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6ec0aefb60c7c2a49a4d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c4a416e9bda2ad3cb437"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c4a416e9bda2ad3cb437`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-812444d9733638fdfeed"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-812444d9733638fdfeed`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6757265a6a0bd676911b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6757265a6a0bd676911b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-19; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ec7e6773141518fa143a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ec7e6773141518fa143a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-973afe40aa9c17e96ef9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-973afe40aa9c17e96ef9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4c6847c8bbf7a9ae5b34"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4c6847c8bbf7a9ae5b34`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1bbed8a31e3f936aeaa6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1bbed8a31e3f936aeaa6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-19; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a2e1a4d338f3f6f0fb38"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a2e1a4d338f3f6f0fb38`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9ffe0d01314061398a75"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9ffe0d01314061398a75`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-87f0a8d7149c5b46c820"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-87f0a8d7149c5b46c820`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-67c1cbada0d32c730520"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-67c1cbada0d32c730520`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-21; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f444f32cd96439045f9c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f444f32cd96439045f9c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-91ae46afaf0e67caa1d6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-91ae46afaf0e67caa1d6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e09f3a3e9e469e8d2ab4"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e09f3a3e9e469e8d2ab4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ff5ef558ba6872bc5f75"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ff5ef558ba6872bc5f75`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-21; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9f0c0262635504f558ec"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9f0c0262635504f558ec`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-141356360fb1174f51be"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-141356360fb1174f51be`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-716a3d681a728780e732"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-716a3d681a728780e732`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-393e76fc7dd3e7ee3523"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-393e76fc7dd3e7ee3523`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-21; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-425d29cd01c20329d361"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-425d29cd01c20329d361`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-39aebdc5864f62fef260"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-39aebdc5864f62fef260`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-32b8be463aa2377f03aa"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-32b8be463aa2377f03aa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-78b9cf376411d2ecb939"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-78b9cf376411d2ecb939`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-21; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-56df90dc3d74e04d45b3"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-56df90dc3d74e04d45b3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-783ce1b57879bcf51277"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-783ce1b57879bcf51277`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d7a8bed81650490e16dd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d7a8bed81650490e16dd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6a512137426dbcea44a4"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6a512137426dbcea44a4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-21; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-d61c3e5813187b10d58f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-d61c3e5813187b10d58f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f1ded90a1ff021eaa383"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f1ded90a1ff021eaa383`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1e03052701ef71238dc8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1e03052701ef71238dc8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dec15e5136633c40c1f7"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dec15e5136633c40c1f7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-21; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-35556091697dc3f7aa27"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-35556091697dc3f7aa27`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-240b728d0528d941b1c3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-240b728d0528d941b1c3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f1c369c97e5c83a19c8b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f1c369c97e5c83a19c8b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aec59af143b3260e190f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-aec59af143b3260e190f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-21; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-60fb70ffef1fe13bc596"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-60fb70ffef1fe13bc596`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5c651b03f123d06c920b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5c651b03f123d06c920b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6b052b8d550cad9ac1a8"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6b052b8d550cad9ac1a8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-47b6c2e0a4edaf727629"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-47b6c2e0a4edaf727629`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-21; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a21f43e5967d5c9b8c6b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a21f43e5967d5c9b8c6b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f2cf2c9ea5c86799c940"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f2cf2c9ea5c86799c940`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f634c7ad37de89b5d3e2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f634c7ad37de89b5d3e2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ad2de76d4cf2704f751f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ad2de76d4cf2704f751f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-21; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-64dee723d8a6b37980cd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-64dee723d8a6b37980cd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c4612780a03d75e690dd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-c4612780a03d75e690dd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1df07684377c75e162cd"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1df07684377c75e162cd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-34057bed4ed67121155f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-34057bed4ed67121155f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-21; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e091f6243421512cd429"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e091f6243421512cd429`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3b6dd9bd7f163ab3187d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3b6dd9bd7f163ab3187d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-000285bf3a47735474c3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-000285bf3a47735474c3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b0a984a0d89773e89c4c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b0a984a0d89773e89c4c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-22; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5c0d2d683fd048863385"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5c0d2d683fd048863385`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-827356e538efe8371dc8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-827356e538efe8371dc8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-717a5d53a7274122f6a3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-717a5d53a7274122f6a3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-71010554a3b9ed7c53d5"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-71010554a3b9ed7c53d5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-22; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-22e4538a80ab7ac1567b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-22e4538a80ab7ac1567b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b0b6ed43d64152685842"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b0b6ed43d64152685842`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c64375005f7d1e610d73"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c64375005f7d1e610d73`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d0fa34eacc1c2cfd07e9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d0fa34eacc1c2cfd07e9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 1-W-out-6; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-22; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ee0cc61fd90961b74530"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ee0cc61fd90961b74530`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5f99fff760eb31b75b6c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5f99fff760eb31b75b6c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-859f493b3136a81abf62"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-859f493b3136a81abf62`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-48cf722639a21b46c101"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-48cf722639a21b46c101`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-22; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b98ae1e805ca24992a87"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b98ae1e805ca24992a87`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bea4f2c251d04beeb5e6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bea4f2c251d04beeb5e6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6c9ea4c168a489467a15"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6c9ea4c168a489467a15`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8dec386cf8d1e8ce0767"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8dec386cf8d1e8ce0767`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-22; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-c797f672d479fc19274a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-c797f672d479fc19274a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-de9855a85eac7ff442ff"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-de9855a85eac7ff442ff`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e1f1f9c4f7ac050ca310"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e1f1f9c4f7ac050ca310`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6904b60af424c1e753a3"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6904b60af424c1e753a3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-22; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-db54eb6eef2d3d8deff1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-db54eb6eef2d3d8deff1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b3b14782dc4f6889bff5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b3b14782dc4f6889bff5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c6a28a3e57b54631f773"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c6a28a3e57b54631f773`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-39a2bc32140d0bdfb098"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-39a2bc32140d0bdfb098`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-22; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-73b598d9799942e99a96"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-73b598d9799942e99a96`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-feb0646c93008c3999f5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-feb0646c93008c3999f5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-372eb5ae45a39a03f79c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-372eb5ae45a39a03f79c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fb138a719394c000bd18"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fb138a719394c000bd18`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-22; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cae630ac32324d977c92"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cae630ac32324d977c92`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-54ff4c7281129b9beea6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-54ff4c7281129b9beea6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9549a7d19c3609436097"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-9549a7d19c3609436097`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6a02c531bd835b8a4af6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6a02c531bd835b8a4af6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-22; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-79339744e01d8c24be6a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-79339744e01d8c24be6a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0445492cfa8cd318568b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0445492cfa8cd318568b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e4e86212fafce0c21a8e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e4e86212fafce0c21a8e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-badc06ac36430a067e50"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-badc06ac36430a067e50`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-22; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b18d3deaaeb33542a130"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b18d3deaaeb33542a130`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bc92d2fa4bb7d06f3125"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-bc92d2fa4bb7d06f3125`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3b20456682e141138888"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-3b20456682e141138888`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c54a32f4f99dcaaf2783"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c54a32f4f99dcaaf2783`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-23; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a600d68d9d1554464198"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a600d68d9d1554464198`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-535bab940f6f4138e5fa"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-535bab940f6f4138e5fa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d144d5071001adc8bfe5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d144d5071001adc8bfe5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-65a5ecb215d5cbd69816"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-65a5ecb215d5cbd69816`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-1; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-23; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b145c015ed98eef81092"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b145c015ed98eef81092`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-361d4eea27dea6a9b9fa"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-361d4eea27dea6a9b9fa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2de2c508685dfbb6c751"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2de2c508685dfbb6c751`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5b90adb650166b7321d6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5b90adb650166b7321d6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-8; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-23; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5b30d96bc0da0c85cd95"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5b30d96bc0da0c85cd95`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2e135463480a373e7372"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2e135463480a373e7372`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-964c03d9329221e6c19e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-964c03d9329221e6c19e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-30330d00dc1ece9a2538"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-30330d00dc1ece9a2538`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-10; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-23; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6978a7932ef860eb82e4"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6978a7932ef860eb82e4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-410e5f9c7ebe8d076a5f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-410e5f9c7ebe8d076a5f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b43d40f17d7df1e9fdbb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b43d40f17d7df1e9fdbb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fd6e828e7794176eb4ca"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-fd6e828e7794176eb4ca`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-11; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-23; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-cc1c5cdc69221e299dc1"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-cc1c5cdc69221e299dc1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2eb20b8145037ad97d60"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2eb20b8145037ad97d60`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-68c3333d38aff4ea743e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-68c3333d38aff4ea743e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8d2f6102a4e0dfb7cd51"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8d2f6102a4e0dfb7cd51`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-12; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-23; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-3f6598c1860f9c6d07cf"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-3f6598c1860f9c6d07cf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1da03699357ba3fd49de"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1da03699357ba3fd49de`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c249c0296e95e27a4ef6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c249c0296e95e27a4ef6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cd6bae7208850090931f"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-cd6bae7208850090931f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-W-out-13; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-23; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-f509f6807ba07bd67c9f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-f509f6807ba07bd67c9f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6cf56d09db6c86a3c2c6"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6cf56d09db6c86a3c2c6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-71aeac46fdd392ac2494"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-71aeac46fdd392ac2494`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0606403842b10b481307"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0606403842b10b481307`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-E-out-15; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-23; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ca949da2a9096bd08aea"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ca949da2a9096bd08aea`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-20b811c116418a98e27d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-20b811c116418a98e27d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b5223ed03b42c1e55937"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b5223ed03b42c1e55937`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-712ea6a59d1420b5c566"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-712ea6a59d1420b5c566`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-E-out-16; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-23; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-9e3a339aebdee6216d33"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-9e3a339aebdee6216d33`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d0718d7495f6f301d116"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d0718d7495f6f301d116`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d10b50b87633a1c419b7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-d10b50b87633a1c419b7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f70bf8ea345937726b06"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f70bf8ea345937726b06`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-E-out-17; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-23; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-452c6ff24155024a4136"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-452c6ff24155024a4136`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-077781144ea9e3204bd3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-077781144ea9e3204bd3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5c7d5b5503bb2d40424e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5c7d5b5503bb2d40424e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-585eea77b0ad908f8a36"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-585eea77b0ad908f8a36`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-N-out-20; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-23; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2c7d64752d34cd2c52a0"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2c7d64752d34cd2c52a0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-79a3d85faaad943a1412"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-79a3d85faaad943a1412`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e924abc6896e4f9a512e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e924abc6896e4f9a512e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8f9a2e25004e3c0d4e01"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-8f9a2e25004e3c0d4e01`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 1-N-out-24; from service: road; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — road → pedestrian — 96 cases; unverified: 96</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 1-N-in-2; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ee85cf3a7147df07d568">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b596fa38a8e04c5e9e28">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-65c459a7dce39abf5d58">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3026cf2fbcb6701dccff">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-2; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-00cb07143aaab168ebbf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bae5bff22f4b18455c34">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e37e5398857c810f3b03">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9dd6e4beac84f26e1cfe">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-3; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8ccac8ebde60dfefeca5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-266b5af18a5cd0e9483c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-81e70863c529f586bdcb">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f641e661e46cb7c90187">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-3; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-35d0c118eb69622d095d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-de3ad74639897d2578b5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1aca934bf04be4ea024a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a442485a53e27f71b94d">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-4; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-757c8badf2c2e8436069">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f94a7c572ea208767fc9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7b7b08340b62094aaa21">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-473b02bf1068eb47f24c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-4; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-588e02833cfeb37f238c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f7b7341333b774085c77">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f6b1c31532c0d9efe949">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6b04382f8c7cd1049852">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b705647de8e5542d57a2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6506ff56392122b3abc0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-936b7d184918dd1cab1c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-45ef42708826cb46b671">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-5; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-50e8872efe32e5459069">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d14e831e08630812c208">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4bc7aebcb36b49de876f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-71674b3afba4a1f58507">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-7; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4a78c88f6c323bc0c9f6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7c00bec105a7dc70e2bf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2859fb4d338f393b8041">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ac762a876b36d2bb9905">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-7; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1e7ce8640f23c2264743">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-65b06e5a57b490970d78">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f1bb7e77b9f163af6e43">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9e7b3d8e8c99f1e46fa8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-9; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2cf714e229046572fb2c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5a8d0b58a67325d8a9e8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dbc2a6e146852e3bb208">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-27f5811c1c72e8ccae3e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-W-in-9; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e1bb4a0142781e33f075">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-708f68670dfd3f236cc0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4bf770fff63f5e195ca1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-84539ef8fcb5981067af">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-14; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4432654ecae00052e0fc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e91caa3a43351405ca4d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-557b3c82e85b429e8b19">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-35e98ccb52d33932d965">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-14; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-e234e140b9c12a822a7b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f1dc833f67386db0b78e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-be2eb5f3ae2f9e9333d3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1645e309d3a89c04bd68">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-18; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-030490c9afed68f12071">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0a0e34a5e028892c4d9d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2defeb3a0a0e653a1252">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0872cf651bba72dbfa51">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-18; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-130c4bc633a148112d5e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4cf97f4df787de012f6b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c6237cff9be02f339e44">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6b9fad909a84f5b282b2">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-19; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-6bb7982b112f16377758">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3fbcec266d1b80542240">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-357bb78ee2e6ce98cdc5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-733e40a44f21c6965104">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-19; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-2591e83cc4e9928d1ba6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-27334b4f1f5bc5d62cac">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7a159fb134bac5fde372">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-097167b025f68207692e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-21; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-062596692762b9ff8731">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b0e4b0f768837bf8baac">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ac7fd7f635d1adc3cf79">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c14ba10ce1132f89c724">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-21; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-46448e92d7a591a5857f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1fb2aaf2138bc7a53323">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-38317ae497fe69042bc6">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ec7967022c88a7f80a9c">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-22; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a59354fb644e15bd5bef">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-06354c9fdf81b0e3ff01">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1487b64662bb9cbee2ed">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2851f2446773a2e05da6">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-S-in-22; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-abaf6f439a9f6e90b489">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1519c544f701e3f5e8a9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0adfb07ccabff48df748">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a9704dcbab9665c2dafa">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-23; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a00450efd361c889bcb7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4ef71df4ec09f6610d3f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7f964deb6c19f81cc4f5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d5b6bdad2299ec9e4445">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 1-N-in-23; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1b1369f1f5fce25b7094">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-394b42e9ec1c7531decd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-670c36ce4a5f63f54320">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c9448aab9a7c7314ad77">[ ] unverified</a> |


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
<summary>Forbidden transfer — from port: 1-N-in-3; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8ccac8ebde60dfefeca5"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8ccac8ebde60dfefeca5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-266b5af18a5cd0e9483c"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-266b5af18a5cd0e9483c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-81e70863c529f586bdcb"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-81e70863c529f586bdcb`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f641e661e46cb7c90187"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f641e661e46cb7c90187`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-3; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-35d0c118eb69622d095d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-35d0c118eb69622d095d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-de3ad74639897d2578b5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-de3ad74639897d2578b5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1aca934bf04be4ea024a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1aca934bf04be4ea024a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a442485a53e27f71b94d"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a442485a53e27f71b94d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-3; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-4; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-757c8badf2c2e8436069"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-757c8badf2c2e8436069`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f94a7c572ea208767fc9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f94a7c572ea208767fc9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7b7b08340b62094aaa21"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7b7b08340b62094aaa21`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-473b02bf1068eb47f24c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-473b02bf1068eb47f24c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-4; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-588e02833cfeb37f238c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-588e02833cfeb37f238c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f7b7341333b774085c77"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f7b7341333b774085c77`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f6b1c31532c0d9efe949"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f6b1c31532c0d9efe949`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6b04382f8c7cd1049852"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6b04382f8c7cd1049852`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-4; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b705647de8e5542d57a2"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b705647de8e5542d57a2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6506ff56392122b3abc0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6506ff56392122b3abc0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-936b7d184918dd1cab1c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-936b7d184918dd1cab1c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-45ef42708826cb46b671"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-45ef42708826cb46b671`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-5; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-50e8872efe32e5459069"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-50e8872efe32e5459069`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d14e831e08630812c208"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d14e831e08630812c208`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4bc7aebcb36b49de876f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4bc7aebcb36b49de876f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-71674b3afba4a1f58507"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-71674b3afba4a1f58507`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-5; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-7; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4a78c88f6c323bc0c9f6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4a78c88f6c323bc0c9f6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7c00bec105a7dc70e2bf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7c00bec105a7dc70e2bf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2859fb4d338f393b8041"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2859fb4d338f393b8041`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ac762a876b36d2bb9905"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ac762a876b36d2bb9905`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-7; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1e7ce8640f23c2264743"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1e7ce8640f23c2264743`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-65b06e5a57b490970d78"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-65b06e5a57b490970d78`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f1bb7e77b9f163af6e43"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f1bb7e77b9f163af6e43`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9e7b3d8e8c99f1e46fa8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-9e7b3d8e8c99f1e46fa8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-7; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-9; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2cf714e229046572fb2c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2cf714e229046572fb2c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5a8d0b58a67325d8a9e8"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-5a8d0b58a67325d8a9e8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dbc2a6e146852e3bb208"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-dbc2a6e146852e3bb208`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-27f5811c1c72e8ccae3e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-27f5811c1c72e8ccae3e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-W-in-9; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e1bb4a0142781e33f075"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e1bb4a0142781e33f075`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-708f68670dfd3f236cc0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-708f68670dfd3f236cc0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4bf770fff63f5e195ca1"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-4bf770fff63f5e195ca1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-84539ef8fcb5981067af"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-84539ef8fcb5981067af`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-W-in-9; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-14; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4432654ecae00052e0fc"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4432654ecae00052e0fc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e91caa3a43351405ca4d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e91caa3a43351405ca4d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-557b3c82e85b429e8b19"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-557b3c82e85b429e8b19`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-35e98ccb52d33932d965"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-35e98ccb52d33932d965`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-14; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-e234e140b9c12a822a7b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-e234e140b9c12a822a7b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f1dc833f67386db0b78e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f1dc833f67386db0b78e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-be2eb5f3ae2f9e9333d3"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-be2eb5f3ae2f9e9333d3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1645e309d3a89c04bd68"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-1645e309d3a89c04bd68`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-14; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-18; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-030490c9afed68f12071"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-030490c9afed68f12071`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0a0e34a5e028892c4d9d"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0a0e34a5e028892c4d9d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2defeb3a0a0e653a1252"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2defeb3a0a0e653a1252`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0872cf651bba72dbfa51"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0872cf651bba72dbfa51`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-18; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-130c4bc633a148112d5e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-130c4bc633a148112d5e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4cf97f4df787de012f6b"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4cf97f4df787de012f6b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c6237cff9be02f339e44"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c6237cff9be02f339e44`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6b9fad909a84f5b282b2"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-6b9fad909a84f5b282b2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-18; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-19; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-6bb7982b112f16377758"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-6bb7982b112f16377758`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3fbcec266d1b80542240"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3fbcec266d1b80542240`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-357bb78ee2e6ce98cdc5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-357bb78ee2e6ce98cdc5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-733e40a44f21c6965104"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-733e40a44f21c6965104`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-19; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-2591e83cc4e9928d1ba6"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-2591e83cc4e9928d1ba6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-27334b4f1f5bc5d62cac"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-27334b4f1f5bc5d62cac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7a159fb134bac5fde372"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7a159fb134bac5fde372`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-097167b025f68207692e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-097167b025f68207692e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-19; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-21; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-062596692762b9ff8731"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-062596692762b9ff8731`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b0e4b0f768837bf8baac"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-b0e4b0f768837bf8baac`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ac7fd7f635d1adc3cf79"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ac7fd7f635d1adc3cf79`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c14ba10ce1132f89c724"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c14ba10ce1132f89c724`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-21; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-46448e92d7a591a5857f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-46448e92d7a591a5857f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1fb2aaf2138bc7a53323"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1fb2aaf2138bc7a53323`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-38317ae497fe69042bc6"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-38317ae497fe69042bc6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ec7967022c88a7f80a9c"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ec7967022c88a7f80a9c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-21; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-22; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a59354fb644e15bd5bef"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a59354fb644e15bd5bef`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-06354c9fdf81b0e3ff01"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-06354c9fdf81b0e3ff01`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1487b64662bb9cbee2ed"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1487b64662bb9cbee2ed`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2851f2446773a2e05da6"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-2851f2446773a2e05da6`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-S-in-22; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-abaf6f439a9f6e90b489"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-abaf6f439a9f6e90b489`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1519c544f701e3f5e8a9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1519c544f701e3f5e8a9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0adfb07ccabff48df748"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-0adfb07ccabff48df748`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a9704dcbab9665c2dafa"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a9704dcbab9665c2dafa`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-S-in-22; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-23; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a00450efd361c889bcb7"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a00450efd361c889bcb7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4ef71df4ec09f6610d3f"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4ef71df4ec09f6610d3f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7f964deb6c19f81cc4f5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-7f964deb6c19f81cc4f5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d5b6bdad2299ec9e4445"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d5b6bdad2299ec9e4445`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 2-W-out-2; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 1-N-in-23; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1b1369f1f5fce25b7094"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1b1369f1f5fce25b7094`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-394b42e9ec1c7531decd"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-394b42e9ec1c7531decd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-670c36ce4a5f63f54320"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-670c36ce4a5f63f54320`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c9448aab9a7c7314ad77"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c9448aab9a7c7314ad77`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 1-N-in-23; to port: 2-E-out-3; from service: road; to service: pedestrian; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>

</details>

<details>
<summary>Forbidden transfer — pedestrian → road — 96 cases; unverified: 96</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-W-out-1; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-1e73acd9891fcb5a336d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f09685453dbba31bf918">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ee89ea099f7cd626db2d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-37c774b9228f9a186d34">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-W-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-aaa262748984a2617f08">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f98b1241a3bd087f0fe9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5fc514495cfed260edf5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ef653a3a98d9d9eba6b9">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-W-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ced061156bcff10f4d3a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d2ec636c9067b45381a3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0362d6cf09c6b0b251a2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-79f7b0e53bb6b8305f5b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-W-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-0a8dd399c11d9ac44d24">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-874d16e0d7cf0f459150">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2a333e17aa3baa4a5788">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-18f515dd707989a68016">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-W-out-11; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ca45162a2db64e5eac7d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e21b4d7e5284b532dddf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2c01260e1af178b0b31e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-69326eae3de8351a9b06">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-W-out-12; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-4b6d417dee027b4cfc7f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-3548910cd28f87893035">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bb7be583e238451f247f">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-55274f34458a198eb431">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-W-out-13; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b0caf7eff3b6bb15ab2c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6e2bcf23067e8ec2e5c4">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2e8eb0e50a532340339c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-a2e46a8347c4ebcf97cd">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-E-out-15; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-8ef64be1e5bb56aa18bd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-20b74497c9431d1440bf">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-be0ea6666862d75b8c41">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0f7009d197db5a854757">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-E-out-16; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-917869aee40edbc564c9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d04e9d77cc3bd986abd5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b902369bfcae4914fba7">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e97b8308155659a861c1">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-E-out-17; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ecb37f0642ee0d705c0b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-7892098c4eee322b4c38">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bd4c69507d976b06060b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d91465c673f4e4e4cc55">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-N-out-20; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b74434a114cef0abac9b">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9918ec6965600b2dcf85">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1e954a70bf02d18e191d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-462c5df1c34e36d45494">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-N-in-1; to port: 1-N-out-24; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-bb7e7dd37daeefa3d317">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4e38db9091a9acba9a24">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e0ffe065f2157ac41389">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c4fc1d21ddaaf0c4dbd8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-W-out-1; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-49129d7508035298d7c9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-aba432b7819ae43669f1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-54f5d606a075821872d2">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e2a20d424c962b518b86">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-W-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-83ecccb97e837b474289">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-328e1bfe9f2cbc4a40e0">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-c5b65d3a1c490f85aabc">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-22a5d2ae08c1951ab4ba">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-W-out-8; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-3d8d3c6ddfee827b515e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e7746d4f27631b59ab9d">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-78114e77549b48140016">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-d60e4ed0db3729e41562">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-W-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-562a667b5278f5f0cc63">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2ec9d69e45aa0cfaeda1">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-8a8e67c630f170bb6507">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-5f00800a130fdc1d616a">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-W-out-11; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b0c637011ff1e8114e24">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-1ca828a6178bdad96c92">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-fd4ad748e14252bcba86">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-286f505f88244e30aa90">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-W-out-12; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-a4a15d4aedc479a2ecfd">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-e5f1f647de39a7c60825">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f6306a8f2a78daf7f31a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-dd0c017c70d9a758cd4e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-W-out-13; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-784b03bfb2b17c2075e9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0dda33a9bb74f120665e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-09bfa7357104113a6004">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-4a53c0fc271d3de6a25b">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-E-out-15; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-b7e2a9235ff20a2bbdb8">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9355d08c4ca8b812ce95">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-82e4112a1019a8453fee">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-f8d1aba5b86fd9b2fc70">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-E-out-16; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-5925924b2cc76dcacb5e">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-9670ce92d203d3aa30f9">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-902465137bc9a091239c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-b86ceeee8f6157ecf67e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-E-out-17; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-ac73348bbb08a9a58980">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-cd7b9f477657b3293662">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-eae3812042abfe6942d5">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-ab642a62bfb6eefae3c8">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-N-out-20; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-281c56bb0312707e447a">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-0b0cd2b9e1819dbb32f3">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6ac7db637a1217be1d11">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-bbdcd42bc4aca0626f4e">[ ] unverified</a> |
| **Forbidden transfer**<br>from port: 2-S-in-4; to port: 1-N-out-24; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph | — | <a href="#case-in_game_forbidden_transfer-74366e775608c8986f2c">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-6b8166cb4d1308d11616">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-2578ff1ade72b39c3692">[ ] unverified</a> | <a href="#case-in_game_forbidden_transfer-14abaf1a7768b3c823dd">[ ] unverified</a> |


<details>
<summary>Forbidden transfer — from port: 2-N-in-1; to port: 1-W-out-1; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-1e73acd9891fcb5a336d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-1e73acd9891fcb5a336d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-1; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f09685453dbba31bf918"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f09685453dbba31bf918`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-1; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ee89ea099f7cd626db2d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-ee89ea099f7cd626db2d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-1; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-37c774b9228f9a186d34"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-37c774b9228f9a186d34`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-1; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-N-in-1; to port: 1-W-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-aaa262748984a2617f08"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-aaa262748984a2617f08`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f98b1241a3bd087f0fe9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-f98b1241a3bd087f0fe9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5fc514495cfed260edf5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-5fc514495cfed260edf5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ef653a3a98d9d9eba6b9"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ef653a3a98d9d9eba6b9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

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
<summary>Forbidden transfer — from port: 2-N-in-1; to port: 1-W-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-0a8dd399c11d9ac44d24"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-0a8dd399c11d9ac44d24`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-874d16e0d7cf0f459150"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-874d16e0d7cf0f459150`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2a333e17aa3baa4a5788"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2a333e17aa3baa4a5788`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-18f515dd707989a68016"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-18f515dd707989a68016`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-N-in-1; to port: 1-W-out-11; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ca45162a2db64e5eac7d"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ca45162a2db64e5eac7d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-11; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e21b4d7e5284b532dddf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e21b4d7e5284b532dddf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-11; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2c01260e1af178b0b31e"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2c01260e1af178b0b31e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-11; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-69326eae3de8351a9b06"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-69326eae3de8351a9b06`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-11; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-N-in-1; to port: 1-W-out-12; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-4b6d417dee027b4cfc7f"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-4b6d417dee027b4cfc7f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-12; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-3548910cd28f87893035"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-3548910cd28f87893035`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-12; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bb7be583e238451f247f"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bb7be583e238451f247f`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-12; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-55274f34458a198eb431"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-55274f34458a198eb431`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-12; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-N-in-1; to port: 1-W-out-13; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b0caf7eff3b6bb15ab2c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b0caf7eff3b6bb15ab2c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-13; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6e2bcf23067e8ec2e5c4"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6e2bcf23067e8ec2e5c4`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-13; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2e8eb0e50a532340339c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2e8eb0e50a532340339c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-13; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-a2e46a8347c4ebcf97cd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-a2e46a8347c4ebcf97cd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-W-out-13; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-N-in-1; to port: 1-E-out-15; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-8ef64be1e5bb56aa18bd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-8ef64be1e5bb56aa18bd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-E-out-15; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-20b74497c9431d1440bf"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-20b74497c9431d1440bf`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-E-out-15; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-be0ea6666862d75b8c41"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-be0ea6666862d75b8c41`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-E-out-15; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0f7009d197db5a854757"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-0f7009d197db5a854757`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-E-out-15; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-N-in-1; to port: 1-E-out-16; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-917869aee40edbc564c9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-917869aee40edbc564c9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-E-out-16; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d04e9d77cc3bd986abd5"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-d04e9d77cc3bd986abd5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-E-out-16; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b902369bfcae4914fba7"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-b902369bfcae4914fba7`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-E-out-16; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e97b8308155659a861c1"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e97b8308155659a861c1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-E-out-16; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-N-in-1; to port: 1-E-out-17; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ecb37f0642ee0d705c0b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ecb37f0642ee0d705c0b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-E-out-17; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-7892098c4eee322b4c38"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-7892098c4eee322b4c38`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-E-out-17; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bd4c69507d976b06060b"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-bd4c69507d976b06060b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-E-out-17; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-d91465c673f4e4e4cc55"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-d91465c673f4e4e4cc55`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-E-out-17; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-N-in-1; to port: 1-N-out-20; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b74434a114cef0abac9b"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b74434a114cef0abac9b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-N-out-20; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9918ec6965600b2dcf85"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9918ec6965600b2dcf85`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-N-out-20; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1e954a70bf02d18e191d"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-1e954a70bf02d18e191d`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-N-out-20; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-462c5df1c34e36d45494"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-462c5df1c34e36d45494`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-N-out-20; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-N-in-1; to port: 1-N-out-24; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-bb7e7dd37daeefa3d317"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-bb7e7dd37daeefa3d317`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-N-out-24; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4e38db9091a9acba9a24"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-4e38db9091a9acba9a24`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-N-out-24; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e0ffe065f2157ac41389"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-e0ffe065f2157ac41389`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-N-out-24; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c4fc1d21ddaaf0c4dbd8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-c4fc1d21ddaaf0c4dbd8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-N-in-1; to port: 1-N-out-24; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-W-out-1; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-49129d7508035298d7c9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-49129d7508035298d7c9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-1; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-aba432b7819ae43669f1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-aba432b7819ae43669f1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-1; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-54f5d606a075821872d2"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-54f5d606a075821872d2`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-1; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e2a20d424c962b518b86"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-e2a20d424c962b518b86`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-1; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-W-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-83ecccb97e837b474289"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-83ecccb97e837b474289`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-328e1bfe9f2cbc4a40e0"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-328e1bfe9f2cbc4a40e0`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-c5b65d3a1c490f85aabc"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-c5b65d3a1c490f85aabc`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-22a5d2ae08c1951ab4ba"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-22a5d2ae08c1951ab4ba`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-6; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

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
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-W-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-562a667b5278f5f0cc63"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-562a667b5278f5f0cc63`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2ec9d69e45aa0cfaeda1"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-2ec9d69e45aa0cfaeda1`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-8a8e67c630f170bb6507"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-8a8e67c630f170bb6507`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-5f00800a130fdc1d616a"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-5f00800a130fdc1d616a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-10; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-W-out-11; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b0c637011ff1e8114e24"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b0c637011ff1e8114e24`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-11; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-1ca828a6178bdad96c92"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-1ca828a6178bdad96c92`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-11; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-fd4ad748e14252bcba86"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-fd4ad748e14252bcba86`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-11; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-286f505f88244e30aa90"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-286f505f88244e30aa90`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-11; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-W-out-12; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-a4a15d4aedc479a2ecfd"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-a4a15d4aedc479a2ecfd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-12; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-e5f1f647de39a7c60825"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-e5f1f647de39a7c60825`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-12; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f6306a8f2a78daf7f31a"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-f6306a8f2a78daf7f31a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-12; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-dd0c017c70d9a758cd4e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-dd0c017c70d9a758cd4e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-12; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-W-out-13; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-784b03bfb2b17c2075e9"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-784b03bfb2b17c2075e9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-13; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0dda33a9bb74f120665e"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0dda33a9bb74f120665e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-13; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-09bfa7357104113a6004"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-09bfa7357104113a6004`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-13; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-4a53c0fc271d3de6a25b"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-4a53c0fc271d3de6a25b`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-W-out-13; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-E-out-15; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-b7e2a9235ff20a2bbdb8"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-b7e2a9235ff20a2bbdb8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-15; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9355d08c4ca8b812ce95"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9355d08c4ca8b812ce95`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-15; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-82e4112a1019a8453fee"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-82e4112a1019a8453fee`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-15; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-f8d1aba5b86fd9b2fc70"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-f8d1aba5b86fd9b2fc70`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-15; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-E-out-16; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-5925924b2cc76dcacb5e"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-5925924b2cc76dcacb5e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-16; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-9670ce92d203d3aa30f9"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-9670ce92d203d3aa30f9`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-16; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-902465137bc9a091239c"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-902465137bc9a091239c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-16; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-b86ceeee8f6157ecf67e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-b86ceeee8f6157ecf67e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-16; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-E-out-17; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-ac73348bbb08a9a58980"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-ac73348bbb08a9a58980`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-17; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-cd7b9f477657b3293662"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-cd7b9f477657b3293662`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-17; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-eae3812042abfe6942d5"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-eae3812042abfe6942d5`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-17; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-ab642a62bfb6eefae3c8"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-ab642a62bfb6eefae3c8`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-E-out-17; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-N-out-20; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-281c56bb0312707e447a"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-281c56bb0312707e447a`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-20; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-0b0cd2b9e1819dbb32f3"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-0b0cd2b9e1819dbb32f3`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-20; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6ac7db637a1217be1d11"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-6ac7db637a1217be1d11`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-20; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-bbdcd42bc4aca0626f4e"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-bbdcd42bc4aca0626f4e`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-20; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

</details>


<details>
<summary>Forbidden transfer — from port: 2-S-in-4; to port: 1-N-out-24; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph</summary>

<a id="case-in_game_forbidden_transfer-74366e775608c8986f2c"></a>

**0° CCW: unverified** — `in_game_forbidden_transfer-74366e775608c8986f2c`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-24; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-6b8166cb4d1308d11616"></a>

**90° CCW: unverified** — `in_game_forbidden_transfer-6b8166cb4d1308d11616`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-24; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-2578ff1ade72b39c3692"></a>

**180° CCW: unverified** — `in_game_forbidden_transfer-2578ff1ade72b39c3692`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-24; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

No observation recorded.

<a id="case-in_game_forbidden_transfer-14abaf1a7768b3c823dd"></a>

**270° CCW: unverified** — `in_game_forbidden_transfer-14abaf1a7768b3c823dd`.

Confirm this undeclared transfer is unavailable.

Scope: from port: 2-S-in-4; to port: 1-N-out-24; from service: pedestrian; to service: road; basis: not reachable in actual saved PATH graph.

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

<details>
<summary>Preview review — Images — 2 cases; unverified: 2</summary>

| Check / exact scope | General | 0° | 90° | 180° | 270° |
| --- | --- | --- | --- | --- | --- |
| **Preview review**<br>Image: image:ddrhw-diagonal-access-core:canonical-southeast | <a href="#case-preview_review-f171c5fb3e196d1d1198">[ ] unverified</a> | — | — | — | — |
| **Preview review**<br>Image: image:ddrhw-diagonal-access-core:canonical-top | <a href="#case-preview_review-a7ba8c8eb8ed1691e6dd">[ ] unverified</a> | — | — | — | — |


<details>
<summary>Preview review — Image: image:ddrhw-diagonal-access-core:canonical-southeast</summary>

<a id="case-preview_review-f171c5fb3e196d1d1198"></a>

**General: unverified** — `preview_review-f171c5fb3e196d1d1198`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-diagonal-access-core:canonical-southeast.

No observation recorded.

</details>


<details>
<summary>Preview review — Image: image:ddrhw-diagonal-access-core:canonical-top</summary>

<a id="case-preview_review-a7ba8c8eb8ed1691e6dd"></a>

**General: unverified** — `preview_review-a7ba8c8eb8ed1691e6dd`.

Inspect this exact image for paths, surfaces, supports, joins, shadows, and labels.

Scope: Image: image:ddrhw-diagonal-access-core:canonical-top.

No observation recorded.

</details>

</details>

<!-- END MANUAL CHECKS -->

## 6. Design history

Created on branch `codex/double-decker-diagonal-highway` for a compact Tokyo-style interchange. The earlier source-only schematic remains separately identified in the assembly’s design history. Saved-city resource identifiers are reserved locally and must remain stable; public allocation and redistribution are pending.
